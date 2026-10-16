"""Telegram-бот, который оценивает калорийность еды по фото с помощью Claude."""

import base64
import html
import json
import logging
import os
import sqlite3
from datetime import date

import anthropic
from telegram import Update
from telegram.constants import ChatAction, ParseMode
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

logging.basicConfig(
    format="%(asctime)s %(levelname)s %(name)s: %(message)s", level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)
log = logging.getLogger("calorie-bot")

TELEGRAM_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
MODEL = os.environ.get("CLAUDE_MODEL", "claude-opus-5-5")
DB_PATH = os.environ.get("DB_PATH", "calories.db")

client = anthropic.AsyncAnthropic()  # читает ANTHROPIC_API_KEY из окружения

SYSTEM_PROMPT = """Ты — диетолог-нутрициолог. Пользователь присылает фото еды \
(иногда с подписью) или текстовое описание того, что он съел.

Определи каждое блюдо или продукт, оцени вес порции в граммах по визуальным \
признакам (размер тарелки, приборов, рук, упаковки) и посчитай калории и БЖУ \
по типичным справочным значениям. Если в подписи указан вес или состав — \
используй эти данные, они точнее твоей оценки.

Пиши названия блюд и комментарии по-русски. Если на фото нет еды, верни \
is_food = false и пустой список items. В comment кратко укажи, что могло \
сильно повлиять на точность (скрытое масло, соус, неочевидный размер порции)."""

NUTRITION_SCHEMA = {
    "type": "object",
    "properties": {
        "is_food": {"type": "boolean"},
        "items": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "grams": {"type": "number"},
                    "kcal": {"type": "number"},
                    "protein_g": {"type": "number"},
                    "fat_g": {"type": "number"},
                    "carbs_g": {"type": "number"},
                },
                "required": ["name", "grams", "kcal", "protein_g", "fat_g", "carbs_g"],
                "additionalProperties": False,
            },
        },
        "confidence": {"type": "string", "enum": ["низкая", "средняя", "высокая"]},
        "comment": {"type": "string"},
    },
    "required": ["is_food", "items", "confidence", "comment"],
    "additionalProperties": False,
}


# ---------- хранилище дневника ----------

def db() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        """CREATE TABLE IF NOT EXISTS meals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            day TEXT NOT NULL,
            title TEXT NOT NULL,
            kcal REAL NOT NULL,
            protein REAL NOT NULL,
            fat REAL NOT NULL,
            carbs REAL NOT NULL
        )"""
    )
    return conn


def save_meal(user_id: int, title: str, totals: dict) -> None:
    with db() as conn:
        conn.execute(
            "INSERT INTO meals (user_id, day, title, kcal, protein, fat, carbs) "
            "VALUES (?, ?, ?, ?, ?, ?, ?)",
            (user_id, date.today().isoformat(), title, totals["kcal"],
             totals["protein_g"], totals["fat_g"], totals["carbs_g"]),
        )


def today_meals(user_id: int) -> list[tuple]:
    with db() as conn:
        return conn.execute(
            "SELECT title, kcal, protein, fat, carbs FROM meals "
            "WHERE user_id = ? AND day = ? ORDER BY id",
            (user_id, date.today().isoformat()),
        ).fetchall()


def delete_last_meal(user_id: int) -> str | None:
    with db() as conn:
        row = conn.execute(
            "SELECT id, title FROM meals WHERE user_id = ? AND day = ? "
            "ORDER BY id DESC LIMIT 1",
            (user_id, date.today().isoformat()),
        ).fetchone()
        if row is None:
            return None
        conn.execute("DELETE FROM meals WHERE id = ?", (row[0],))
        return row[1]


# ---------- обращение к Claude ----------

async def analyze(content: list[dict]) -> dict | None:
    """Возвращает разобранный JSON с оценкой или None, если модель отказалась."""
    response = await client.beta.messages.create(
        model=MODEL,
        max_tokens=16000,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": content}],
        output_config={
            "effort": "medium",
            "format": {"type": "json_schema", "schema": NUTRITION_SCHEMA},
        },
        betas=["server-side-fallback-2026-07-01"],
        fallbacks="default",
    )
    if response.stop_reason == "refusal":
        log.warning("Claude declined the request: %s", response.stop_details)
        return None
    text = next(b.text for b in response.content if b.type == "text")
    return json.loads(text)


def totals_of(items: list[dict]) -> dict:
    keys = ("kcal", "protein_g", "fat_g", "carbs_g")
    return {k: sum(i[k] for i in items) for k in keys}


def format_result(result: dict) -> str:
    lines = ["🍽 <b>Что на тарелке:</b>"]
    for i in result["items"]:
        lines.append(
            f"• {html.escape(i['name'])} (~{i['grams']:.0f} г) — <b>{i['kcal']:.0f} ккал</b>\n"
            f"   Б {i['protein_g']:.0f} / Ж {i['fat_g']:.0f} / У {i['carbs_g']:.0f}"
        )
    t = totals_of(result["items"])
    lines.append(
        f"\n🔥 <b>Итого: {t['kcal']:.0f} ккал</b>\n"
        f"Белки {t['protein_g']:.0f} г · Жиры {t['fat_g']:.0f} г · "
        f"Углеводы {t['carbs_g']:.0f} г"
    )
    lines.append(f"\nТочность оценки: {result['confidence']}")
    if result["comment"]:
        lines.append(f"💡 {html.escape(result['comment'])}")
    lines.append("\nЗаписал в дневник. /today — итог за день, /undo — удалить.")
    return "\n".join(lines)


async def process(update: Update, content: list[dict]) -> None:
    msg = update.effective_message
    await msg.chat.send_action(ChatAction.TYPING)
    try:
        result = await analyze(content)
    except anthropic.RateLimitError:
        await msg.reply_text("Слишком много запросов, попробуйте через минуту.")
        return
    except anthropic.APIError:
        log.exception("Claude API error")
        await msg.reply_text("Не получилось связаться с сервисом анализа. Попробуйте позже.")
        return

    if result is None:
        await msg.reply_text("Не могу обработать этот запрос. Пришлите, пожалуйста, фото еды.")
        return
    if not result["is_food"] or not result["items"]:
        await msg.reply_text("Не вижу на фото еды 🤔 Пришлите снимок блюда.")
        return

    title = ", ".join(i["name"] for i in result["items"])
    save_meal(update.effective_user.id, title, totals_of(result["items"]))
    await msg.reply_text(format_result(result), parse_mode=ParseMode.HTML)


# ---------- обработчики Telegram ----------

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Привет! 👋 Я считаю калории по фото.\n\n"
        "📸 Пришлите фото еды — я определю блюда, вес порций, калории и БЖУ.\n"
        "✍️ Можно добавить подпись: «порция 250 г», «жарено на масле».\n"
        "💬 Или просто напишите, что съели: «овсянка 200 г с бананом».\n\n"
        "/today — сколько съедено за сегодня\n"
        "/undo — удалить последнюю запись"
    )


async def on_photo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = update.message
    if msg.photo:
        tg_file = await msg.photo[-1].get_file()  # самое большое разрешение
        media_type = "image/jpeg"
    else:  # изображение, отправленное файлом
        tg_file = await msg.document.get_file()
        media_type = msg.document.mime_type
        if media_type not in ("image/jpeg", "image/png", "image/webp", "image/gif"):
            await msg.reply_text("Этот формат не поддерживается, пришлите JPG или PNG.")
            return

    data = await tg_file.download_as_bytearray()
    content = [
        {
            "type": "image",
            "source": {
                "type": "base64",
                "media_type": media_type,
                "data": base64.standard_b64encode(bytes(data)).decode("utf-8"),
            },
        },
        {"type": "text", "text": f"Подпись пользователя: {msg.caption}"
         if msg.caption else "Посчитай калории на фото."},
    ]
    await process(update, content)


async def on_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await process(update, [{"type": "text", "text": f"Я съел: {update.message.text}"}])


async def today(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    meals = today_meals(update.effective_user.id)
    if not meals:
        await update.message.reply_text("Сегодня пока ничего не записано.")
        return
    lines = ["📒 <b>Сегодня:</b>"]
    for title, kcal, *_ in meals:
        lines.append(f"• {html.escape(title)} — {kcal:.0f} ккал")
    kcal, p, f, c = (sum(m[i] for m in meals) for i in range(1, 5))
    lines.append(
        f"\n🔥 <b>Всего: {kcal:.0f} ккал</b>\n"
        f"Белки {p:.0f} г · Жиры {f:.0f} г · Углеводы {c:.0f} г"
    )
    await update.message.reply_text("\n".join(lines), parse_mode=ParseMode.HTML)


async def undo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    title = delete_last_meal(update.effective_user.id)
    if title is None:
        await update.message.reply_text("Удалять нечего — за сегодня записей нет.")
    else:
        await update.message.reply_text(f"Удалил: {title}")


def main() -> None:
    db().close()
    app = Application.builder().token(TELEGRAM_TOKEN).concurrent_updates(True).build()
    app.add_handler(CommandHandler(["start", "help"], start))
    app.add_handler(CommandHandler("today", today))
    app.add_handler(CommandHandler("undo", undo))
    app.add_handler(MessageHandler(filters.PHOTO | filters.Document.IMAGE, on_photo))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, on_text))
    log.info("Бот запущен")
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
