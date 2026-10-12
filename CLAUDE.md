# Правила проекта

Отвечать пользователю по-русски. Пользователь делает лендинги (REMONT DESIGN, ПРОТЕКТОР и следующие).

## Скилы при работе над сайтами

Когда делаем или переделываем сайт, используй все подходящие скилы из `.claude/skills/`, а не только один:

- Дизайн и вкус: design-taste-frontend, frontend-design, high-end-visual-design, minimalist-ui, redesign-existing-projects, theme-factory.
- Анимации: gsap-core, gsap-scrolltrigger, gsap-performance (прокрутка, закрепление блоков, параллакс); find-animation-opportunities (где добавить движение), improve-animations (аудит и план), animation-performance (плавность без рывков).
- Качество: web-design-guidelines, web-quality-audit, performance, core-web-vitals.
- Поиск: seo, seo-audit (включая локальное SEO), schema (разметка JSON-LD: адрес, часы, телефон).
- Поиск новых скилов: find-skills (`npx skills find` в этой среде не работает — искать через `https://skills.sh/api/search?q=...`). Перед установкой показать содержимое скила и ставить только после «да» пользователя.

## Как начинаем новый сайт (обязательно)

Пользователь называет нишу. Прежде чем предлагать дизайн, просмотри и проанализируй ВСЕ источники из списка ниже, именно этот список:

- Лендинги: land-book.com, lapa.ninja, onepagelove.com, landingfolio.com, saaslandingpage.com
- Общие подборки: siteinspire.com, httpster.net, maxibestof.one, bestwebsite.gallery, curated.design, minimal.gallery, darkmodedesign.com
- Эффекты и анимации: hoverstat.es, tympanus.net/codrops, gsap.com/showcase, framer.com/gallery
- Отдельные блоки: refero.design, mobbin.com, navbar.gallery, footer.design, unsection.com
- Шрифты: typewolf.com, fontsinuse.com
- Концепты: dribbble.com, behance.net, muz.li

Порядок:
1. Открыть сайты в браузере (Chromium через Playwright) и искать по нише и по близким темам.
2. Из каждой группы взять что-то своё: раскладку и оформление блоков (лендинги, подборки, блоки), эффекты и анимации (эффекты), шрифтовые пары (шрифты), смелые идеи (концепты).
3. Показать пользователю найденное: что откуда берём, со ссылками на конкретные примеры. Собирать сайт, только когда пользователь выберет.
4. Если какой-то сайт не открылся (блокирует автоматический доступ), честно сказать, какие именно, а не делать вид, что смотрел.
5. При сборке использовать все подходящие скилы (см. выше).

## Референсы (полный список; для анализа ниши — список выше)

Пароль к «Полке референсов»: protektor.

- https://polka-refov.vercel.app/ — «Полка референсов»
- https://land-book.com/ — лендинги
- https://www.awwwards.com/ — лучшие сайты, премии
- https://thefwa.com/ — премия FWA, экспериментальные сайты
- https://www.cssdesignawards.com/ — премия CSSDA
- https://godly.website/ — подборка «вау»-сайтов, видео-превью
- https://www.siteinspire.com/ — подборка по стилям и отраслям
- https://www.lapa.ninja/ — лендинги
- https://onepagelove.com/ — одностраничные сайты
- https://www.landingfolio.com/ — лендинги и блоки по типам
- https://saaslandingpage.com/ — лендинги SaaS
- https://minimal.gallery/ — минимализм
- https://httpster.net/ — подборка сайтов
- https://hoverstat.es/ — сайты с интересными эффектами
- https://maxibestof.one/ — подборка сайтов
- https://refero.design/ — референсы по экранам и элементам
- https://mobbin.com/ — экраны приложений и сайтов
- https://www.darkmodedesign.com/ — тёмные сайты
- https://bestwebsite.gallery/ — подборка сайтов
- https://curated.design/ — подборка сайтов
- https://navbar.gallery/ — шапки и меню
- https://footer.design/ — футеры
- https://unsection.com/ — отдельные блоки сайтов
- https://tympanus.net/codrops/ — эффекты и анимации с кодом
- https://gsap.com/showcase/ — сайты на GSAP
- https://www.framer.com/gallery/ — сайты на Framer
- https://muz.li/ — вдохновение для дизайнеров
- https://dribbble.com/ и https://www.behance.net/ — концепты дизайнеров
- https://www.typewolf.com/ и https://fontsinuse.com/ — шрифты в реальных проектах
- https://ratingruneta.ru/ и https://goldensite.ru/ — лучшие российские сайты
