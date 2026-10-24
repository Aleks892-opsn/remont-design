# Собирает три варианта портфолио из одной разметки и трёх тем
CASES = [
    dict(id='protektor', name='ПРОТЕКТОР', niche='Шиномонтаж', url='https://protektorvercelapp.vercel.app', host='protektor.ru',
         pitch='Шиномонтаж, куда записываются сами',
         task='Люди не хотят звонить и стоять в очереди. Нужно, чтобы запись занимала минуту.',
         sol='Главное обещание вынес на первый экран: «Переобуем за 25 минут». Каждый следующий блок его доказывает.',
         done=['Первый экран с красной машиной и обещанием', 'Цены по размеру колеса без звёздочек', 'Запись на точное время в три шага']),
    dict(id='altitude', name='Altitude', niche='Авиакомпания', url='https://altitude-airlines.vercel.app', host='altitude.ru',
         pitch='Авиакомпания с честной ценой',
         task='Билеты все продают одинаково. Нужно, чтобы человек почувствовал полёт и поверил цене.',
         sol='Небо, облака и самолёт с первой секунды, а рядом понятные гарантии: багаж включён, цена не меняется.',
         done=['Заставка с посадочным талоном', 'Четыре класса: от эконома до частного джета', 'Блок «Цена не меняется» с разбором билета']),
    dict(id='forte', name='FORTE', niche='Строительство домов', url='https://forte-stroy.vercel.app', host='forte-stroy.ru',
         pitch='Стройка без сюрпризов в смете',
         task='Главный страх заказчика: цена дома вырастет, когда стройка уже началась.',
         sol='Сделал цену и процесс прозрачными: дом можно собрать и посчитать прямо на сайте.',
         done=['Надпись FORTE уходит за крышу дома', 'Конфигуратор: меняешь дом и видишь цену', 'Отзывы с фото построенных домов']),
]
STEPS = [('Разбор', 'Изучаю нишу, конкурентов и десятки сильных сайтов.'),
         ('Идея', 'Нахожу главное обещание и выстраиваю блоки вокруг него.'),
         ('Дизайн', 'Показываю 2-3 варианта. Собираю только тот, что выбрали.'),
         ('Сборка', 'Вёрстка, анимации и отдельная версия для телефона.'),
         ('Запуск', 'Публикую сайт и помогаю подключить домен.')]

THEMES = {
    'v1': dict(title='Красная ночь', fonts='Wix+Madefor+Display:wght@500;700;800&family=Wix+Madefor+Text:wght@400;500;600',
               css='''
:root{--bg:#0b0b0c;--bg2:#141416;--card:#17171a;--line:#2a2a2e;--t:#f5f3ef;--mute:#9a978f;--acc:#ff2b2b;--acc2:#b8101a;--on:#fff;
--fh:"Wix Madefor Display",sans-serif;--fb:"Wix Madefor Text",sans-serif;--hw:800;--ls:-.045em;--r:22px;--rb:999px}
.hero__photo{border-radius:var(--r)}
.case__win{box-shadow:0 0 0 1px #2c2c30,0 50px 120px -40px rgba(255,43,43,.45)}
.case::before{content:"";position:absolute;inset:0;background:radial-gradient(50% 40% at 70% 50%,rgba(255,43,43,.16),transparent 70%);pointer-events:none}
.cta{background:radial-gradient(60% 70% at 50% 100%,rgba(255,43,43,.35),transparent 70%)}
'''),
    'v2': dict(title='Вечер', fonts='Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,500;1,600&family=Commissioner:wght@400;500;600',
               css='''
:root{--bg:#120f0d;--bg2:#1a1613;--card:#1d1916;--line:#352d27;--t:#f1e9de;--mute:#a69a8c;--acc:#d23a4d;--acc2:#8e1c2b;--on:#fff;
--fh:"Cormorant Garamond",serif;--hw:600;--fb:"Commissioner",sans-serif;--ls:-.02em;--r:0px;--rb:0px}
h1,.h2,.case__n,.cta__h,.about__t,.loader__n{font-style:normal}
.hero__lead em,.h2 em,.cta__h em{font-style:italic;color:var(--acc)}
.hero__lead em{font-style:italic}
.hero__photo{outline:1px solid var(--line);outline-offset:10px}
.case__win{box-shadow:0 0 0 1px var(--line),0 50px 100px -40px rgba(0,0,0,.9)}
.step b{border-radius:0!important}
.btn{letter-spacing:.06em;text-transform:uppercase;font-size:13px}
.about__t{font-size:clamp(28px,4.4vw,58px)!important;line-height:1.12!important}
'''),
    'v3': dict(title='Плакат', fonts='Dela+Gothic+One&family=Golos+Text:wght@400;500;600;700',
               css='''
:root{--bg:#efede8;--bg2:#e6e3dc;--card:#fff;--line:#d3cfc6;--t:#111;--mute:#5f5c56;--acc:#e2231a;--acc2:#b0150f;--on:#fff;
--fh:"Dela Gothic One",sans-serif;--hw:400;--fb:"Golos Text",sans-serif;--ls:-.02em;--r:28px;--rb:999px}
.loader{background:#111!important;color:#efede8}
.hero__photo{border-radius:var(--r);box-shadow:12px 12px 0 #111}
.case{background:#111;color:#efede8}
.case .tag{border-color:#3a3a3a;color:#bdbab3}
.case p,.case li{color:#cfccc5}
.case__win{box-shadow:0 0 0 1px #333}
#case-altitude{background:var(--bg);color:var(--t)}
#case-altitude p,#case-altitude li{color:var(--mute)}
#case-altitude .tag{border-color:var(--line);color:var(--mute)}
#case-altitude .case__win{box-shadow:12px 12px 0 #111}
.mq{background:var(--acc);color:#fff;border:0}
.step b{background:#fff!important}
.step.on b{background:var(--acc)!important}
.cta{background:var(--acc);color:#fff}
.cta .btn--acc{background:#111;color:#fff}
.cta__p{color:rgba(255,255,255,.85)!important}
.nav{color:#111}
'''),
}

ARR = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 17 17 7M9 7h8v8"/></svg>'

BASE_CSS = '''
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
[data-rv],.ln>span{will-change:transform,opacity}
body[data-anim=blur] .ln,body[data-anim=scale] .ln{overflow:visible}
body[data-anim=flip] .ln{perspective:600px}
body{background:var(--bg);color:var(--t);font:400 16px/1.6 var(--fb);-webkit-font-smoothing:antialiased;overflow-x:hidden}
img{display:block;max-width:100%}
a{color:inherit;text-decoration:none}
.w{width:100%;max-width:1320px;margin:0 auto;padding:0 18px}
@media(min-width:900px){.w{padding:0 48px}}
h1,.h2,.case__n,.cta__h,.loader__n,.about__t,.hero__lead{font-family:var(--fh);font-weight:var(--hw);letter-spacing:var(--ls)}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:12px;height:58px;padding:0 28px;border-radius:var(--rb);font:600 16px var(--fb);white-space:nowrap;transition:background .3s,color .3s,transform .3s cubic-bezier(.16,1,.3,1)}
.btn svg{width:18px;height:18px;fill:none;stroke:currentColor;stroke-width:2.2;stroke-linecap:round;stroke-linejoin:round;transition:transform .35s cubic-bezier(.16,1,.3,1)}
.btn:hover svg{transform:translate(3px,-3px)}
.btn:active{transform:scale(.97)}
.btn--acc{background:var(--acc);color:var(--on)}
.btn--acc:hover{background:var(--acc2)}
.btn--line{border:1px solid var(--line)}
.btn--line:hover{border-color:var(--t)}
.tag{display:inline-flex;align-items:center;height:32px;padding:0 14px;border:1px solid var(--line);border-radius:var(--rb);font-size:13px;font-weight:500;color:var(--mute)}
.ln{display:inline-block;vertical-align:top;overflow:hidden;padding-bottom:.1em;margin-bottom:-.1em}
.ln>span{display:inline-block;will-change:transform}

/* заставка */
.loader{position:fixed;inset:0;z-index:100;background:var(--bg);display:grid;place-items:center}
.loader__n{font-size:clamp(48px,14vw,150px);line-height:1;overflow:hidden;display:flex}
.loader__n span{display:inline-block;transform:translateY(110%)}
.loader__bar{position:absolute;left:18px;right:18px;bottom:40px;height:2px;background:var(--line)}
.loader__bar i{display:block;height:100%;background:var(--acc);transform-origin:0 50%;transform:scaleX(0)}

.nav{position:fixed;z-index:50;top:0;left:0;right:0;color:var(--t);background:linear-gradient(180deg,var(--bg) 0%,color-mix(in srgb,var(--bg) 70%,transparent) 60%,transparent);transition:transform .5s cubic-bezier(.16,1,.3,1)}
.nav.hide{transform:translateY(-100%)}
.nav .w{display:flex;align-items:center;justify-content:space-between;height:72px}
.nav b{font:var(--hw) 20px var(--fh);letter-spacing:-.01em}
.nav nav{display:flex;gap:26px;font-size:15px;font-weight:500}
.nav nav a{display:none}
.nav nav a.tg{display:inline}
@media(min-width:900px){.nav nav a{display:inline}}

/* первый экран: обложка журнала, фото целиком */
.hero{position:relative;padding:76px 0 40px}
.hero .w{display:grid;gap:24px}
.cover{position:relative;border-radius:var(--r);overflow:hidden;border:1px solid var(--line)}
.hero__photo{overflow:hidden;clip-path:inset(100% 0 0 0)}
.hero__photo img{width:100%;height:auto;transform:scale(1.18);transform-origin:50% 60%}
.cover__mast{position:absolute;left:0;right:0;top:0;padding:12px 14px 0;pointer-events:none}
.hero__name{font-size:var(--nf,22vw);line-height:.84;white-space:nowrap;color:#fff;text-shadow:0 10px 40px rgba(0,0,0,.35)}
.cover__no{position:absolute;right:14px;bottom:14px;font-size:12px;line-height:1.3;color:#fff;opacity:.85;text-align:right}
.hero__lead{font-size:clamp(28px,4vw,54px);line-height:1.08;text-wrap:balance}
.hero__lead em{font-style:normal;color:var(--acc)}
.hero__b{margin-top:20px;display:grid;grid-template-columns:1fr 1fr;gap:10px}
.hero__b .btn{padding:0 14px;font-size:15px}
@media(min-width:900px){
 .hero{min-height:100svh;display:flex;align-items:center;padding:96px 0 50px}
 .hero .w{grid-template-columns:1fr 1fr;gap:64px;align-items:center}
 .hero__txt{order:-1}
 .hero__b{display:flex}
 .hero__b .btn{padding:0 28px}
 .cover{justify-self:end;max-height:84svh;aspect-ratio:1856/2304}
 .cover{width:min(560px,calc(84svh * 1856 / 2304));aspect-ratio:auto;max-height:none}
 .hero__photo{clip-path:none}
 .hero__photo img{width:100%;height:auto;transform:none}
}
/* бегущая строка */
.mq{overflow:hidden;border-top:1px solid var(--line);border-bottom:1px solid var(--line);padding:18px 0;white-space:nowrap}
.mq__t{display:inline-flex;gap:40px;padding-right:40px;font:var(--hw) clamp(26px,4vw,52px)/1 var(--fh);letter-spacing:var(--ls);animation:mq 22s linear infinite}
.mq__t span{display:inline-flex;align-items:center;gap:40px}
.mq__t span::after{content:"✦";color:var(--acc);font-size:.6em}
@keyframes mq{to{transform:translateX(-50%)}}

/* обо мне: слова проявляются при прокрутке */
.about{padding:110px 0}
.about__t{font-size:clamp(28px,4.2vw,60px);line-height:1.15;max-width:22ch}
.about__t .wd{opacity:.14;transition:none}
.about__s{margin-top:44px;display:grid;grid-template-columns:repeat(3,1fr);gap:12px;max-width:760px}
.about__s div{padding-top:14px;border-top:1px solid var(--line)}
.about__s b{display:block;font:var(--hw) clamp(34px,4vw,54px)/1 var(--fh);letter-spacing:var(--ls)}
.about__s span{display:block;margin-top:6px;font-size:14px;color:var(--mute)}

/* работы */
.wk-h{padding:30px 0 0}
.h2{font-size:clamp(38px,6vw,84px);line-height:1.02;text-wrap:balance}
.h2 em{font-style:normal;color:var(--acc)}
.case{position:relative;overflow:hidden}
.case__in{min-height:100svh;display:flex;flex-direction:column;justify-content:center;padding:84px 0 34px}
.case .w{display:grid;gap:22px}
.case__top{display:flex;align-items:center;gap:12px}
.case__no{font:var(--hw) 15px var(--fh);color:var(--acc)}
.case__bar{flex:1;height:1px;background:var(--line);position:relative}
.case__bar i{position:absolute;inset:0;background:var(--acc);transform-origin:0 50%;transform:scaleX(0)}
.case__n{font-size:clamp(44px,8vw,110px);line-height:.95}
.case__pitch{margin-top:8px;font-size:clamp(18px,1.7vw,22px);font-weight:500}
.case__win{border-radius:14px;overflow:hidden;background:#0d0d0e}
.case__bar2{display:flex;align-items:center;gap:6px;height:30px;padding:0 12px;background:#1d1d20}
.case__bar2 i{width:9px;height:9px;border-radius:50%;background:#3d3d42}
.case__bar2 span{margin-left:10px;font-size:11px;color:#8c8c92}
.case__view{position:relative;aspect-ratio:16/10;overflow:hidden}
.case__strip{position:absolute;left:0;top:0;width:100%;will-change:transform}
.case__strip img{width:100%;aspect-ratio:16/10;object-fit:cover}
@media(max-width:899px){.case__strip{position:absolute;inset:0}.case__strip img{position:absolute;inset:0;height:100%;opacity:0;transition:opacity .9s ease}.case__strip img.on{opacity:1}}

.case__info{display:grid;gap:16px}
.case__info h3{font-size:13px;font-weight:600;text-transform:uppercase;letter-spacing:.12em;color:var(--acc)}
.case__info p{margin-top:4px;color:var(--mute)}
.case__info ul{list-style:none;display:grid;gap:6px;margin-top:6px}
.case__info li{position:relative;padding-left:22px;color:var(--mute)}
.case__info li::before{content:"";position:absolute;left:0;top:.75em;width:12px;height:2px;background:var(--acc)}
.case__go{width:100%;margin-top:26px}
@media(min-width:900px){
 .case .w{grid-template-columns:.8fr 1.2fr;grid-template-areas:"top top" "info win";column-gap:56px;row-gap:26px;align-items:center}
 .case__head{grid-area:top}
 .case__shot{grid-area:win}
 .case__go{width:auto}
 .case__info{grid-area:info}
}
@media(max-width:899px){.case__info p,.case__info ul{font-size:15px}}

/* процесс: шаги по линии, которая заполняется при прокрутке */
.how{padding:110px 0}
.how__g{display:grid;gap:36px}
.how__p{margin-top:18px;font-size:17px;color:var(--mute);max-width:34ch}
.how__l .btn{margin-top:26px}
.how__list{position:relative}
.how__line{position:absolute;left:27px;top:28px;bottom:28px;width:2px;background:var(--line)}
.how__line i{position:absolute;inset:0;background:var(--acc);transform-origin:50% 0;transform:scaleY(0)}
.step{position:relative;display:grid;grid-template-columns:56px 1fr;gap:18px;padding:16px 0;align-items:start}
.step b{position:relative;z-index:1;width:56px;height:56px;border-radius:50%;display:grid;place-items:center;background:var(--bg);border:1px solid var(--line);font:var(--hw) 17px var(--fh);color:var(--mute);transition:background .4s,color .4s,border-color .4s,transform .4s cubic-bezier(.16,1,.3,1)}
.step.on b{background:var(--acc);border-color:var(--acc);color:var(--on);transform:scale(1.06)}
.step h3{padding-top:8px;font:var(--hw) clamp(24px,2.4vw,32px)/1.1 var(--fh);letter-spacing:var(--ls);transition:color .4s}
.step p{margin-top:6px;color:var(--mute);max-width:38ch}
@media(min-width:900px){.how__g{grid-template-columns:.85fr 1.15fr;gap:70px;align-items:start}.how__l{position:sticky;top:120px}}

/* сайт открывается прямо в портфолио */
.case__win{display:block;position:relative;cursor:pointer;border:0;padding:0;text-align:left;width:100%}
.case__open{position:absolute;z-index:2;right:12px;bottom:12px;display:inline-flex;align-items:center;gap:8px;height:42px;padding:0 16px;border-radius:999px;background:var(--acc);color:var(--on);font:600 14px var(--fb);box-shadow:0 10px 30px -8px rgba(0,0,0,.6);transition:transform .35s cubic-bezier(.16,1,.3,1)}
.case__open svg{width:15px;height:15px;fill:none;stroke:currentColor;stroke-width:2.4;stroke-linecap:round;stroke-linejoin:round}
.case__win:hover .case__open{transform:scale(1.06)}
.vw{position:fixed;inset:0;z-index:300;display:flex;flex-direction:column;background:#0b0b0c}
.vw[hidden]{display:none}
.vw__bar{flex:none;display:flex;align-items:center;gap:10px;height:56px;padding:0 10px 0 16px;background:#141416;color:#fff;border-bottom:1px solid #2a2a2e}
.vw__bar b{flex:1;font:600 16px var(--fb)}
.vw__bar a,.vw__bar button{height:38px;padding:0 14px;border-radius:999px;border:1px solid #3a3a3f;background:none;color:#fff;font:500 13px var(--fb);display:inline-flex;align-items:center;cursor:pointer}
.vw__bar button{background:var(--acc);border-color:var(--acc)}
.vw iframe{flex:1;width:100%;border:0;background:#fff}
/* связь */
.cta{position:relative;padding:120px 0 40px;text-align:center;overflow:hidden}
.cta__h{font-size:clamp(48px,10vw,150px);line-height:.95}
.cta__h em{font-style:normal;color:var(--acc)}
.cta__p{margin:24px auto 0;max-width:36ch;font-size:18px;color:var(--mute)}
.cta .btn{margin-top:34px;height:66px;padding:0 36px;font-size:17px}
.foot{display:flex;justify-content:space-between;margin-top:110px;padding:22px 0 0;border-top:1px solid var(--line);font-size:13px;color:var(--mute);text-align:left}
@media(prefers-reduced-motion:reduce){.loader{display:none}.hero__photo{clip-path:none}.step b{transition:none}.hero__photo img{transform:none}.about__t .wd{opacity:1}.mq__t{animation:none}}
'''

JS = r'''
(function () {
  var reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  // делим заголовки на строки-слова для появления снизу
  document.querySelectorAll('[data-split]').forEach(function (el) {
    el.innerHTML = el.innerHTML.split(/<br\s*\/?>/i).map(function (line) {
      return line.trim().split(/\s+(?![^<]*>)/).map(function (w) { return '<span class="ln"><span>' + w + '</span></span>'; }).join(' ');
    }).join('<br>');
  });
  document.querySelectorAll('[data-words]').forEach(function (el) {
    el.innerHTML = el.textContent.trim().split(/\s+/).map(function (w) { return '<span class="wd">' + w + '</span>'; }).join(' ');
  });
  var nm = document.querySelector('.hero__name'), nin = nm && nm.querySelector('.ln');
  var fitName = function () { if (!nm) return; nm.style.setProperty('--nf', '100px'); var col = nm.closest('.cover').getBoundingClientRect().width - 28; nm.style.setProperty('--nf', Math.min(100 * col / nin.getBoundingClientRect().width, 260) + 'px'); };
  fitName(); addEventListener('resize', fitName); if (document.fonts) document.fonts.ready.then(fitName);
  var vw = document.getElementById('vw'), vf = document.getElementById('vwF');
  var closeVw = function () { vw.hidden = true; vf.src = 'about:blank'; document.documentElement.style.overflow = '';  };
  document.querySelectorAll('[data-open]').forEach(function (b) { b.addEventListener('click', function (e) {
    e.preventDefault(); var u = b.getAttribute('data-open');
    vf.src = u; document.getElementById('vwN').textContent = b.getAttribute('data-name'); document.getElementById('vwO').href = u;
    vw.hidden = false; document.documentElement.style.overflow = 'hidden'; 
    if (window.gsap && !reduce) gsap.fromTo(vw, { clipPath: 'inset(100% 0 0 0)' }, { clipPath: 'inset(0% 0 0 0)', duration: .8, ease: 'expo.out' });
  }); });
  document.getElementById('vwX').addEventListener('click', closeVw);
  addEventListener('keydown', function (e) { if (e.key === 'Escape' && !vw.hidden) closeVw(); });
  // телефон: в окне сайта блоки сменяют друг друга, пока окно на экране
  var mob = matchMedia('(max-width: 899px)');
  document.querySelectorAll('.case__strip').forEach(function (st) {
    var im = st.querySelectorAll('img'), k = 0, timer = null; im[0].classList.add('on');
    var io = new IntersectionObserver(function (es) { es.forEach(function (e) {
      clearInterval(timer);
      if (e.isIntersecting && mob.matches && !reduce) timer = setInterval(function () { im[k].classList.remove('on'); k = (k + 1) % im.length; im[k].classList.add('on'); }, 2600);
    }); }, { threshold: .4 });
    io.observe(st);
  });
  // шапка прячется при прокрутке вниз и возвращается при прокрутке вверх
  var nav = document.querySelector('.nav'), lastY = 0, ticking = false;
  addEventListener('scroll', function () { if (ticking) return; ticking = true; requestAnimationFrame(function () { var y = scrollY; nav.classList.toggle('hide', y > lastY && y > 200); lastY = y; ticking = false; }); }, { passive: true });

  if (reduce || !window.gsap) { var l = document.querySelector('.loader'); if (l) l.remove(); return; }
  gsap.registerPlugin(ScrollTrigger);
  gsap.defaults({ ease: 'power3.out', force3D: true });
  var E = 'power4.out';
  // набор анимаций выбирается атрибутом data-anim у body
  var MODE = document.body.getAttribute('data-anim') || 'blur';
  var MODES = {
    rise:  { word: { yPercent: 105, autoAlpha: 0 }, block: { y: 34, autoAlpha: 0 }, blockTo: { y: 0, autoAlpha: 1 }, d: .9, st: .07 },
    blur:  { word: { autoAlpha: 0, filter: 'blur(14px)', y: 8 }, block: { autoAlpha: 0, filter: 'blur(12px)', y: 14 }, blockTo: { autoAlpha: 1, filter: 'blur(0px)', y: 0 }, d: 1.1, st: .09, ease: 'power2.out' },
    wipe:  { heading: true, block: { clipPath: 'inset(0 0 100% 0)', y: 24 }, blockTo: { clipPath: 'inset(0 0 0% 0)', y: 0 }, d: 1.1, st: .1, ease: 'power3.inOut' },
    flip:  { word: { rotationX: -95, yPercent: 30, autoAlpha: 0, transformOrigin: '50% 100%' }, block: { rotationX: -22, y: 40, autoAlpha: 0, transformPerspective: 900, transformOrigin: '50% 0%' }, blockTo: { rotationX: 0, y: 0, autoAlpha: 1 }, d: 1, st: .08 },
    scale: { word: { scale: .4, autoAlpha: 0, transformOrigin: '50% 80%' }, block: { scale: .9, autoAlpha: 0 }, blockTo: { scale: 1, autoAlpha: 1 }, d: 1, st: .07, ease: 'back.out(1.4)' }
  };
  var M = MODES[MODE] || MODES.rise, ME = M.ease || E;
  var wordAnim = function (h, extra) {
    if (M.heading) return gsap.fromTo(h, { clipPath: 'inset(0 100% 0 0)' }, Object.assign({ clipPath: 'inset(0 0% 0 0)', duration: 1.2, ease: 'power3.inOut' }, extra));
    return gsap.from(h.querySelectorAll('.ln>span'), Object.assign({}, M.word, { duration: M.d, stagger: M.st, ease: ME }, extra));
  };

  // заставка, затем первый экран по шагам: фото, имя, заголовок по словам, кнопки
  var DESK = matchMedia('(min-width: 900px)').matches;
  var tl = gsap.timeline();
  tl.fromTo('.loader__n span', { yPercent: 110 }, { yPercent: 0, duration: .7, stagger: .04, ease: E }, 0)
    .to('.loader__bar i', { scaleX: 1, duration: .8, ease: 'power2.inOut' }, 0)
    .to('.loader', { yPercent: -100, duration: .8, ease: 'power3.inOut' }, .9)
    .set('.loader', { display: 'none' })
    .add(DESK ? gsap.fromTo('.cover', { autoAlpha: 0, y: 30, filter: 'blur(14px)' }, { autoAlpha: 1, y: 0, filter: 'blur(0px)', duration: 1.3, ease: 'power3.out', clearProps: 'filter' }) : gsap.timeline().to('.hero__photo', { clipPath: 'inset(0% 0 0 0)', duration: 1.2, ease: E }, 0).to('.hero__photo img', { scale: 1, duration: 1.6, ease: E }, 0), 1.25)
    .from('.cover__no', { autoAlpha: 0, y: 10, duration: .6 }, 1.9)
    .add(wordAnim(document.querySelector('.hero__lead')), 1.85)
    .fromTo('.hero [data-fade]', M.block, Object.assign({}, M.blockTo, { duration: .9, stagger: .12, ease: ME }), 2.35);

  // заголовки: слова поднимаются по очереди, когда блок доходит до экрана
  document.querySelectorAll('[data-split]').forEach(function (h) {
    if (h.closest('.hero')) return;
    wordAnim(h, { scrollTrigger: { trigger: h, start: 'top 88%', once: true } });
  });
  // остальной текст и карточки: плавно снизу, по очереди
  var rv = gsap.utils.toArray('.mq, .case__top, .case__pitch, .case__info > *, .case__go, .how__l > p, .step, .cta__p, .cta .btn, section.about .w > *, .chatb');
  gsap.set(rv, M.block);
  ScrollTrigger.batch(rv, { start: 'top 90%', once: true, onEnter: function (b) { gsap.to(b, Object.assign({}, M.blockTo, { duration: M.d, stagger: .1, ease: ME, overwrite: true })); } });

  // окно сайта: плавно выезжает и проявляется
  gsap.utils.toArray('.case__win').forEach(function (w) {
    if (MODE === 'scale') gsap.fromTo(w, { scale: .82, borderRadius: 40 }, { scale: 1, borderRadius: 14, ease: 'none', scrollTrigger: { trigger: w, start: 'top 95%', end: 'top 45%', scrub: 1 } });
    else if (MODE === 'wipe') gsap.fromTo(w, { clipPath: 'inset(0 0 100% 0 round 14px)' }, { clipPath: 'inset(0 0 0% 0 round 14px)', duration: 1.3, ease: 'power3.inOut', scrollTrigger: { trigger: w, start: 'top 88%', once: true } });
    else gsap.from(w, { y: 50, autoAlpha: 0, scale: .97, filter: MODE === 'blur' ? 'blur(16px)' : 'blur(0px)', duration: 1.1, ease: E, scrollTrigger: { trigger: w, start: 'top 90%', once: true } });
  });

  var mm = gsap.matchMedia();
  mm.add('(min-width: 900px)', function () {
    // фото на первом экране чуть отстаёт при прокрутке
    // секция работы закрепляется, внутри окна плавно проезжают главные блоки
    document.querySelectorAll('.case').forEach(function (c) {
      var strip = c.querySelector('.case__strip'), view = c.querySelector('.case__view'), n = strip.children.length;
      gsap.timeline({ scrollTrigger: { trigger: c, start: 'top top', end: '+=' + (n * 60) + '%', pin: true, scrub: 1, anticipatePin: 1, invalidateOnRefresh: true } })
        .to(strip, { y: function () { return -(view.offsetHeight * (n - 1)); }, ease: 'none' }, 0)
        .to(c.querySelector('.case__bar i'), { scaleX: 1, ease: 'none' }, 0);
    });
  });
  mm.add('(max-width: 899px)', function () {
    document.querySelectorAll('.case__bar i').forEach(function (b) { gsap.to(b, { scaleX: 1, ease: 'none', scrollTrigger: { trigger: b.closest('.case'), start: 'top 80%', end: 'bottom 60%', scrub: true } }); });
  });

  // процесс: линия заполняется, шаги загораются по очереди
  gsap.to('.how__line i', { scaleY: 1, ease: 'none', scrollTrigger: { trigger: '.how__list', start: 'top 65%', end: 'bottom 65%', scrub: 1 } });
  document.querySelectorAll('.step').forEach(function (st) {
    ScrollTrigger.create({ trigger: st, start: 'top 65%', onEnter: function () { st.classList.add('on'); }, onLeaveBack: function () { st.classList.remove('on'); } });
  });

  // кнопка в конце тянется к курсору
  if (matchMedia('(hover: hover)').matches) document.querySelectorAll('.mag').forEach(function (b) {
    var xTo = gsap.quickTo(b, 'x', { duration: .5, ease: 'power3' }), yTo = gsap.quickTo(b, 'y', { duration: .5, ease: 'power3' });
    b.addEventListener('mousemove', function (e) { var r = b.getBoundingClientRect(); xTo((e.clientX - r.left - r.width / 2) * .3); yTo((e.clientY - r.top - r.height / 2) * .4); });
    b.addEventListener('mouseleave', function () { xTo(0); yTo(0); });
  });
  addEventListener('load', function () { ScrollTrigger.refresh(); });
})();
'''

def case_html(c, i):
    imgs = ''.join(f'<img src="img/{c["id"]}-{k}.webp" alt="{c["name"]}, блок {k}" loading="lazy">' for k in range(1, 5))
    lis = ''.join(f'<li>{d}</li>' for d in c['done'])
    return f'''<section class="case" id="case-{c["id"]}"><div class="case__in"><div class="w">
<div class="case__head"><div class="case__top"><span class="case__no">0{i+1} / 03</span><span class="case__bar"><i></i></span><span class="tag">{c["niche"]}</span></div>
<h3 class="case__n" data-split>{c["name"]}</h3><p class="case__pitch">{c["pitch"]}</p></div>
<div class="case__shot"><a class="case__win" href="sites/{c["id"]}/index.html" data-open="sites/{c["id"]}/index.html" data-name="{c["name"]}"><div class="case__bar2"><i></i><i></i><i></i><span>{c["url"].replace("https://","")}</span></div><div class="case__view"><div class="case__strip">{imgs}</div></div></a><a class="btn btn--acc case__go" href="sites/{c["id"]}/index.html" data-open="sites/{c["id"]}/index.html" data-name="{c["name"]}">Открыть сайт{ARR}</a></div>
<div class="case__info"><div><h3>Задача</h3><p>{c["task"]}</p></div><div><h3>Решение</h3><p>{c["sol"]}</p></div><div><h3>Что сделал</h3><ul>{lis}</ul></div></div>
</div></div></section>'''

ABOUT_DEFAULT = '''<section class="about"><div class="w">
 <p class="about__t" data-words>Мне 18, и я делаю сайты не для галочки. Каждый начинаю с разбора ниши, а заканчиваю тем, что сайт приводит заявки с компьютера и телефона.</p>
 <div class="about__s"><div><b>3</b><span>сайта в портфолио</span></div><div><b>3</b><span>разные ниши</span></div><div><b>100%</b><span>работаю сам, без посредников</span></div></div>
</div></section>
'''

def page(key, th, about=None):
    cases = ''.join(case_html(c, i) for i, c in enumerate(CASES))
    steps = ''.join(f'<div class="step"><b>0{i+1}</b><div><h3>{s}</h3><p>{d}</p></div></div>' for i, (s, d) in enumerate(STEPS))
    mq = ''.join(f'<span>{t}</span>' for t in ['Дизайн', 'Анимации', 'Версия для телефона', 'Запуск'] * 2)
    about_html = about['html'] if about else ABOUT_DEFAULT
    about_css = about['css'] if about else ''
    about_js = about['js'] if about else ''
    return f'''<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Кирилл, веб-дизайнер</title>
<meta name="description" content="Кирилл, 18 лет. Лендинги под ключ для бизнеса: дизайн, анимации, запуск.">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family={th["fonts"]}&display=swap" rel="stylesheet">
<link rel="preload" as="image" href="img/kirill.webp">
<style>{BASE_CSS}{th["css"]}{about_css}</style>
</head>
<body>
<div class="loader" aria-hidden="true"><div class="loader__n"><span>К</span><span>и</span><span>р</span><span>и</span><span>л</span><span>л</span></div><div class="loader__bar"><i></i></div></div>
<header class="nav"><div class="w"><b>Кирилл</b><nav><a href="#works">Работы</a><a href="#how">Процесс</a><a class="tg js-tg" href="https://t.me/kirillostapov" target="_blank" rel="noopener">Telegram</a></nav></div></header>
<main>
<section class="hero"><div class="w">
 <div class="cover"><div class="hero__photo"><img src="img/kirill.webp" alt="Кирилл" fetchpriority="high"></div><span class="cover__no">№ 01<br>2026</span></div>
 <div class="hero__txt"><h1 class="hero__lead" data-split>Делаю сайты, которые <em>приводят</em> клиентов</h1>
  <div class="hero__b" data-fade><a class="btn btn--acc" href="#works">Работы{ARR}</a><a class="btn btn--line js-tg" href="https://t.me/kirillostapov" target="_blank" rel="noopener">Написать</a></div></div>
</div></section>
<div class="mq" aria-hidden="true"><div class="mq__t">{mq}</div></div>
{about_html}<div class="wk-h" id="works"><div class="w"><h2 class="h2" data-split>Примеры<br><em>сайтов</em></h2></div></div>
{cases}
<section class="how" id="how"><div class="w how__g"><div class="how__l"><h2 class="h2" data-split>Как я <em>работаю</em></h2><p class="how__p">Пять шагов от первого сообщения до готового сайта. Вы видите каждый этап и выбираете дизайн до того, как я начну собирать.</p></div><div class="how__list"><span class="how__line"><i></i></span>{steps}</div></div></section>
<section class="cta" id="contact"><div class="w">
 <h2 class="cta__h" data-split>Есть задача?<br><em>Обсудим.</em></h2>
 <p class="cta__p">Напишите пару слов о бизнесе. Отвечу и предложу, каким может быть ваш сайт.</p>
 <a class="btn btn--acc mag js-tg" href="https://t.me/kirillostapov" target="_blank" rel="noopener">Написать в Telegram{ARR}</a>
 <footer class="foot"><span>Кирилл, веб-дизайнер</span><span>2026</span></footer>
</div></section>
</main>
<div class="vw" id="vw" hidden><div class="vw__bar"><b id="vwN"></b><a id="vwO" href="#" target="_blank" rel="noopener">Новая вкладка</a><button type="button" id="vwX">Закрыть</button></div><iframe id="vwF" title="Сайт"></iframe></div>
<script>
// TODO: ссылка на Telegram Кирилла
var TG = 'https://t.me/kirillostapov';
document.querySelectorAll('.js-tg').forEach(function (a) {{ a.href = TG; a.target = '_blank'; a.rel = 'noopener'; }});
</script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
<script>{JS}</script>
<script>{about_js}</script>
</body>
</html>'''

if __name__ == '__main__':
  for k, th in THEMES.items():
    open(f'{k}.html', 'w').write(page(k, th))
  print('ok')
