# Варианты первого экрана «Соловьи»: только зелёный и белый, фото — временная заглушка
G='#1f4d3a'
BASE='''
:root{--g:#1f4d3a;--g2:#163a2c;--gl:#e9f1ec;--w:#fff;--mute:#5d6f66;--ease:cubic-bezier(.16,1,.3,1);--fh:"Unbounded",system-ui,sans-serif;--fb:"Manrope",system-ui,sans-serif}
*{box-sizing:border-box;margin:0;padding:0}
body{background:var(--w);color:var(--g);font:400 16px/1.5 var(--fb);-webkit-font-smoothing:antialiased}
a{color:inherit;text-decoration:none}
.ph{position:relative;overflow:hidden;background:repeating-linear-gradient(135deg,#dfeae3 0 14px,#d4e3da 14px 28px);display:grid;place-items:center;color:var(--g);text-align:center}
.ph span{padding:10px 16px;border-radius:999px;background:rgba(255,255,255,.85);font-size:14px;font-weight:600}
.ph.dk{background:repeating-linear-gradient(135deg,#2a5c47 0 14px,#255340 14px 28px);color:#fff}
.ph.dk span{background:rgba(0,0,0,.25)}
.top{display:flex;align-items:center;gap:20px;padding:16px 18px}
.logo{display:flex;align-items:center;gap:10px;font:700 15px var(--fh)}
.logo i{width:34px;height:34px;border-radius:50%;background:var(--g);color:#fff;display:grid;place-items:center;font:700 14px var(--fh);font-style:normal}
.nav{display:none;gap:26px;font-size:14px;font-weight:500}
.sp{flex:1}
.call{height:42px;padding:0 16px;display:inline-flex;align-items:center;border-radius:999px;border:1.5px solid currentColor;font-weight:600;font-size:14px}
.call .l{display:none}
.k{display:inline-flex;align-items:center;gap:8px;height:32px;padding:0 14px;border-radius:999px;font-size:13px;font-weight:700}
.k i{width:7px;height:7px;border-radius:50%;background:currentColor}
h1{font:600 clamp(30px,4.6vw,64px)/1.06 var(--fh);letter-spacing:-.025em}
.sub{font-size:16px;max-width:40ch}
.sizes{display:flex;gap:8px}
.sz{flex:1;padding:12px 14px;border-radius:16px}
.sz b{display:block;font:600 clamp(15px,4.4vw,20px)/1 var(--fh);white-space:nowrap}
.sz span{display:block;margin-top:4px;font-size:12px;opacity:.75}
.btn{height:56px;display:inline-flex;align-items:center;justify-content:center;gap:10px;padding:0 28px;border-radius:999px;font-weight:700;font-size:16px;transition:transform .3s var(--ease)}
.btn:active{transform:scale(.98)}
.btn svg{width:18px;height:18px;fill:none;stroke:currentColor;stroke-width:2.2;stroke-linecap:round;stroke-linejoin:round}
.btn--g{background:var(--g);color:#fff}
.btn--w{background:#fff;color:var(--g)}
.rv{opacity:0;filter:blur(10px);transform:translate3d(0,16px,0);transition:opacity 1s var(--ease),filter 1s var(--ease),transform 1s var(--ease);transition-delay:var(--d,0s)}
.ld .rv{opacity:1;filter:blur(0);transform:none}
@media(min-width:900px){.top{padding:22px 48px}.nav{display:flex}.call .l{display:inline}.call .s{display:none}}
@media(prefers-reduced-motion:reduce){.rv{transition:none;opacity:1;filter:none;transform:none}}
'''
ARR='<svg viewBox="0 0 24 24"><path d="M7 17 17 7M9 7h8v8"/></svg>'
def top(cls=''): return f'<header class="top rv {cls}"><a class="logo" href="#"><i>С</i>ЖК Соловьи</a><nav class="nav"><a href="#">Дома</a><a href="#">Планировки</a><a href="#">Ипотека</a><a href="#">Контакты</a></nav><span class="sp"></span><a class="call" href="tel:+79228993550"><span class="l">8 (922) 899-35-50</span><span class="s">Позвонить</span></a></header>'
H1='Готовые дома в&nbsp;10&nbsp;минутах от&nbsp;Оренбурга'
SUB='Закрытая территория, можно заезжать. Приезжайте посмотреть вживую.'
def sizes(c): return '<div class="sizes rv" style="--d:.55s">'+''.join(f'<div class="sz {c}"><b>{m} м²</b><span>готовый дом</span></div>' for m in (120,138,170))+'</div>'
CTA=f'href="https://t.me/ElenaYurevna13" target="_blank" rel="noopener"'

V={}
# 1 Сплит: белый слева, фото справа
V['1']=('Сплит','''
.h{min-height:100svh;display:flex;flex-direction:column}
.g{flex:1;display:grid;gap:22px;padding:8px 18px 22px}
.t{display:flex;flex-direction:column;gap:16px;justify-content:center}
.k{background:var(--gl);color:var(--g);align-self:flex-start}
.sub{color:var(--mute)}
.sz{background:var(--gl)}
.btn{align-self:stretch}
.photo{border-radius:26px;min-height:300px}
@media(min-width:900px){.g{grid-template-columns:1fr 1fr;gap:48px;padding:8px 48px 40px}.btn{align-self:flex-start}.photo{min-height:0}}
''',f'''<section class="h">{top()}<div class="g"><div class="t">
<span class="k rv" style="--d:.2s"><i></i>Семейная ипотека</span>
<h1 class="rv" style="--d:.3s">{H1}</h1><p class="sub rv" style="--d:.4s">{SUB}</p>{sizes('')}
<a class="btn btn--g rv" style="--d:.65s" {CTA}>Записаться на экскурсию{ARR}</a></div>
<div class="photo ph rv" style="--d:.25s"><span>Фото дома</span></div></div></section>''')

# 2 Зелёный экран: текст по центру, фото широкой полосой снизу
V['2']=('Зелёный','''
body{background:var(--g)}
.h{min-height:100svh;display:flex;flex-direction:column;background:var(--g);color:#fff}
.top .logo i{background:#fff;color:var(--g)}
.c{padding:24px 18px 0;text-align:center;display:flex;flex-direction:column;align-items:center;gap:16px}
.k{background:rgba(255,255,255,.12);color:#fff}
h1{max-width:16ch}
.sub{color:rgba(255,255,255,.78)}
.sizes{width:100%;max-width:520px}
.sz{background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.2);text-align:left}
.photo{margin:26px 10px 10px;flex:1;min-height:260px;border-radius:26px}
@media(min-width:900px){.c{padding-top:40px}.photo{margin:40px 24px 24px}}
''',f'''<section class="h">{top()}<div class="c">
<span class="k rv" style="--d:.2s"><i></i>Семейная ипотека</span>
<h1 class="rv" style="--d:.3s">{H1}</h1><p class="sub rv" style="--d:.4s">{SUB}</p>{sizes('')}
<a class="btn btn--w rv" style="--d:.65s" {CTA}>Записаться на экскурсию{ARR}</a></div>
<div class="photo ph dk rv" style="--d:.5s"><span>Фото дома</span></div></section>''')

# 3 Фото на весь экран, белая карточка с текстом
V['3']=('Карточка на фото','''
.h{position:relative;min-height:100svh;display:flex;flex-direction:column;padding:10px}
.photo{position:absolute;inset:10px;border-radius:26px}
.top{position:relative;z-index:2;color:#fff}
.top .logo i{background:#fff;color:var(--g)}
.card{position:relative;z-index:2;margin-top:auto;background:#fff;border-radius:22px;padding:22px;display:flex;flex-direction:column;gap:14px;max-width:560px}
.k{background:var(--gl);color:var(--g);align-self:flex-start}
h1{font-size:clamp(26px,3.4vw,46px)}
.sub{color:var(--mute)}
.sz{background:var(--gl)}
.btn{align-self:stretch}
@media(min-width:900px){.h{padding:16px}.photo{inset:16px}.card{margin:auto 0 24px 24px;padding:32px}.btn{align-self:flex-start}}
''',f'''<section class="h"><div class="photo ph dk"><span>Фото дома на весь экран</span></div>{top()}
<div class="card rv" style="--d:.3s"><span class="k"><i></i>Семейная ипотека</span>
<h1>{H1}</h1><p class="sub">{SUB}</p>{sizes('')}
<a class="btn btn--g" {CTA}>Записаться на экскурсию{ARR}</a></div></section>''')

# 4 Журнал: белый, крупный заголовок сверху, фото и зелёный блок с площадями
V['4']=('Журнал','''
.h{min-height:100svh;display:flex;flex-direction:column}
.hd{padding:10px 18px 0;display:grid;gap:14px}
.k{background:var(--g);color:#fff;justify-self:start}
h1{font-size:clamp(34px,6vw,92px);line-height:1}
.sub{color:var(--mute)}
.bt{flex:1;display:grid;gap:10px;padding:20px 10px 10px}
.photo{border-radius:24px;min-height:240px}
.gb{background:var(--g);color:#fff;border-radius:24px;padding:22px;display:flex;flex-direction:column;gap:14px;justify-content:space-between}
.gb .sizes{flex-direction:column}
.gb .sz{background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.2);display:flex;justify-content:space-between;align-items:center}
.gb .sz span{margin:0}
@media(min-width:900px){.hd{padding:10px 48px 0;grid-template-columns:1.4fr .6fr;align-items:end}.hd .k{grid-column:1/-1}.bt{grid-template-columns:1.6fr .7fr;padding:28px 24px 24px}}
''',f'''<section class="h">{top()}<div class="hd">
<span class="k rv" style="--d:.2s"><i></i>Семейная ипотека</span>
<h1 class="rv" style="--d:.3s">{H1}</h1><p class="sub rv" style="--d:.4s">{SUB}</p></div>
<div class="bt"><div class="photo ph rv" style="--d:.45s"><span>Фото дома</span></div>
<div class="gb rv" style="--d:.55s">{sizes('').replace(' rv" style="--d:.55s"','"')}
<a class="btn btn--w" {CTA}>Записаться на экскурсию{ARR}</a></div></div></section>''')

for k,(name,css,html) in V.items():
    open(f'{k}.html','w').write(f'''<!doctype html>
<html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>ЖК «Соловьи» · вариант {k}</title><meta name="robots" content="noindex">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Unbounded:wght@600;700&family=Manrope:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>{BASE}{css}</style></head><body>{html}
<script>requestAnimationFrame(function(){{requestAnimationFrame(function(){{document.body.classList.add('ld')}})}});</script></body></html>''')
print('ok')
