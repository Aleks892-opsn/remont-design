# Демо: четыре варианта первого экрана и блока «О себе» в теме «Красная ночь»
import gen
TH = gen.THEMES['v1']
ARR = gen.ARR

COMMON_CSS = '''
.sec-next{padding:80px 0 120px}
.ph-full img{width:100%;height:auto;display:block}
.rv{opacity:0;transform:translate3d(0,26px,0)}
@media(prefers-reduced-motion:reduce){.rv{opacity:1;transform:none}}
'''

VARIANTS = {}

# 1. Фото во всю ширину, имя наезжает снизу + факты карточками
VARIANTS['h1'] = dict(title='Фото во всю ширину', css='''
.h1x{position:relative;padding-top:64px}
.h1x__ph{position:relative;overflow:hidden}
.h1x__ph img{width:100%;height:auto;transform:scale(1.15)}
.h1x__ph::after{content:"";position:absolute;inset:auto 0 0 0;height:38%;background:linear-gradient(0deg,var(--bg),transparent)}
.h1x__name{position:relative;z-index:2;margin-top:-.62em;font:var(--hw) var(--nf,25vw)/.82 var(--fh);letter-spacing:var(--ls);white-space:nowrap}
.h1x__name .ln>span{display:inline-block}
.h1x__lead{margin-top:16px;font:var(--hw) clamp(24px,3vw,40px)/1.12 var(--fh);letter-spacing:var(--ls);max-width:15ch}
.h1x__lead em{font-style:normal;color:var(--acc)}
.h1x__b{margin-top:22px;display:grid;grid-template-columns:1fr 1fr;gap:10px}
.h1x__b .btn{padding:0 14px;font-size:15px}
.ab1{padding:90px 0 0}
.ab1__k{font-size:14px;color:var(--mute)}
.ab1__h{margin-top:10px;font:var(--hw) clamp(30px,4.5vw,56px)/1.05 var(--fh);letter-spacing:var(--ls);max-width:16ch}
.ab1__rail{margin-top:26px;display:flex;gap:12px;overflow-x:auto;scroll-snap-type:x mandatory;padding:0 18px 10px;scrollbar-width:none}
.ab1__rail::-webkit-scrollbar{display:none}
.fact{flex:none;width:72%;max-width:300px;scroll-snap-align:start;padding:24px;border-radius:var(--r);background:var(--card);border:1px solid var(--line);min-height:230px;display:flex;flex-direction:column}
.fact b{font:var(--hw) 72px/1 var(--fh);letter-spacing:var(--ls);color:var(--acc)}
.fact h3{margin-top:auto;font:var(--hw) 22px/1.15 var(--fh)}
.fact p{margin-top:6px;color:var(--mute);font-size:15px}
.fact--acc{background:var(--acc);border-color:var(--acc)}
.fact--acc b,.fact--acc p{color:#fff}
@media(min-width:900px){.h1x .w{display:grid;grid-template-columns:1fr 1fr;gap:56px;align-items:end}.h1x__ph{order:2;border-radius:var(--r)}.h1x__ph::after{display:none}.h1x__name{margin-top:0}.h1x{padding:110px 0 40px}.h1x__b{display:flex}.ab1__rail{padding:0 48px 10px}.fact{width:300px}}
''', html=f'''
<section class="h1x"><div class="w">
 <div class="h1x__ph ph-full"><img src="img/kirill.webp" alt="Кирилл"></div>
 <div class="h1x__t">
  <h1 class="h1x__name fitname"><span class="ln"><span>Кирилл</span></span></h1>
  <p class="h1x__lead" data-split>Делаю сайты, которые <em>приводят</em> клиентов</p>
  <div class="h1x__b rv"><a class="btn btn--acc" href="#">Работы{ARR}</a><a class="btn btn--line" href="#">Написать</a></div>
 </div>
</div></section>
<section class="ab1"><div class="w"><p class="ab1__k rv">О себе</p><h2 class="ab1__h" data-split>Коротко, кто делает ваш сайт</h2></div>
 <div class="ab1__rail">
  <div class="fact"><b>18</b><h3>лет</h3><p>Делаю сайты сам, без студий и посредников.</p></div>
  <div class="fact fact--acc"><b>1</b><h3>человек на проекте</h3><p>Пишете мне, и вам отвечает тот, кто делает сайт.</p></div>
  <div class="fact"><b>3</b><h3>сайта в портфолио</h3><p>Шиномонтаж, авиакомпания и строительство домов.</p></div>
  <div class="fact"><b>2-3</b><h3>варианта дизайна</h3><p>Выбираете до того, как я начну собирать.</p></div>
 </div>
</section>''', js='''
gsap.fromTo('.h1x__ph img',{scale:1.25},{scale:1,duration:1.8,ease:'expo.out'});
gsap.from('.h1x__name .ln>span',{yPercent:110,duration:1.3,ease:'expo.out',delay:.2});
gsap.to('.h1x__ph img',{yPercent:10,ease:'none',scrollTrigger:{trigger:'.h1x',start:'top top',end:'bottom top',scrub:true}});
gsap.from('.fact',{x:80,opacity:0,stagger:.1,duration:1,ease:'expo.out',scrollTrigger:{trigger:'.ab1__rail',start:'top 85%'}});
''')

# 2. Пропуск-бейдж + манифест строками
VARIANTS['h2'] = dict(title='Пропуск', css='''
.h2x{padding:86px 0 30px;overflow:hidden}
.h2x__lead{font:var(--hw) clamp(34px,6vw,76px)/1 var(--fh);letter-spacing:var(--ls);text-align:center}
.h2x__lead em{font-style:normal;color:var(--acc)}
.pass-wrap{position:relative;margin:120px auto 0;width:min(84vw,380px);perspective:1200px}
.strap{position:absolute;left:50%;top:-80px;width:34px;height:96px;margin-left:-17px;background:repeating-linear-gradient(90deg,var(--acc) 0 6px,var(--acc2) 6px 12px);border-radius:4px}
.pass{position:relative;border-radius:22px;background:#151517;border:1px solid #2c2c30;padding:14px;transform-origin:50% -60px;box-shadow:0 40px 80px -30px rgba(0,0,0,.9),0 0 0 1px rgba(255,255,255,.03) inset}
.pass__hole{width:56px;height:10px;border-radius:6px;background:#0b0b0c;margin:2px auto 12px}
.pass__ph{border-radius:14px;overflow:hidden}
.pass__ph img{width:100%;height:auto}
.pass__row{display:flex;justify-content:space-between;align-items:flex-end;margin-top:14px;padding:0 4px}
.pass__row b{display:block;font:var(--hw) 34px/1 var(--fh);letter-spacing:var(--ls)}
.pass__row span{display:block;margin-top:4px;font-size:13px;color:var(--mute)}
.pass__st{display:inline-flex;align-items:center;gap:6px;height:30px;padding:0 12px;border-radius:999px;background:color-mix(in srgb,var(--acc) 18%,transparent);color:var(--acc);font-size:12px;font-weight:700}
.pass__st i{width:7px;height:7px;border-radius:50%;background:var(--acc)}
.pass__bc{margin-top:12px;height:34px;background:repeating-linear-gradient(90deg,#f5f3ef 0 2px,transparent 2px 5px,#f5f3ef 5px 6px,transparent 6px 9px);opacity:.75;border-radius:4px}
.h2x__b{margin-top:30px;display:flex;justify-content:center;gap:10px}
.ab2{padding:100px 0 0}
.ab2__k{font-size:14px;color:var(--mute)}
.mf{margin-top:18px;display:grid;gap:0}
.mf p{padding:22px 0;border-top:1px solid var(--line);font:var(--hw) clamp(26px,4vw,52px)/1.08 var(--fh);letter-spacing:var(--ls);color:#4a4945;transition:color .5s}
.mf p.on{color:var(--t)}
.mf p span{position:relative;color:inherit}
.mf p.on span{color:var(--acc)}
.mf small{display:block;margin-top:8px;font:500 15px/1.5 var(--fb);letter-spacing:0;color:var(--mute)}
''', html=f'''
<section class="h2x"><div class="w">
 <h1 class="h2x__lead" data-split>Сайты, которые <em>приводят</em> клиентов</h1>
 <div class="pass-wrap"><div class="strap"></div><div class="pass" id="pass">
  <div class="pass__hole"></div>
  <div class="pass__ph ph-full"><img src="img/kirill.webp" alt="Кирилл"></div>
  <div class="pass__row"><div><b>Кирилл</b><span>Веб-дизайнер, 18 лет</span></div><span class="pass__st"><i></i>Беру проекты</span></div>
  <div class="pass__bc"></div>
 </div></div>
 <div class="h2x__b rv"><a class="btn btn--acc" href="#">Работы{ARR}</a><a class="btn btn--line" href="#">Написать</a></div>
</div></section>
<section class="ab2"><div class="w"><p class="ab2__k rv">О себе</p>
 <div class="mf">
  <p>Не шаблоны, а <span>свой дизайн</span><small>Каждый сайт рисую под нишу, а не беру готовую тему.</small></p>
  <p>Не «красиво», а <span>заявки</span><small>Главное обещание бизнеса на первом экране и путь к кнопке.</small></p>
  <p>Не студия, а <span>один человек</span><small>Мне 18, и сайт от первого эскиза до запуска делаю я сам.</small></p>
  <p>Не сюрприз, а <span>выбор</span><small>Показываю 2-3 варианта дизайна до начала сборки.</small></p>
 </div>
</div></section>''', js='''
gsap.from('#pass',{rotation:-14,y:-120,opacity:0,duration:1.8,ease:'elastic.out(1,.45)',delay:.3});
gsap.from('.strap',{scaleY:0,transformOrigin:'50% 0',duration:.8,ease:'expo.out',delay:.2});
var pass=document.getElementById('pass');
if(matchMedia('(hover: hover)').matches){document.addEventListener('mousemove',function(e){var x=e.clientX/innerWidth-.5,y=e.clientY/innerHeight-.5;gsap.to(pass,{rotationY:x*14,rotationX:-y*10,duration:.8,ease:'power3.out'});});}
gsap.to(pass,{rotation:4,ease:'none',scrollTrigger:{trigger:'.h2x',start:'top top',end:'bottom top',scrub:true}});
document.querySelectorAll('.mf p').forEach(function(p){ScrollTrigger.create({trigger:p,start:'top 72%',onEnter:function(){p.classList.add('on')},onLeaveBack:function(){p.classList.remove('on')}});});
''')

# 3. Обложка журнала + вопрос-ответ
VARIANTS['h3'] = dict(title='Обложка', css='''
.h3x{padding:76px 0 30px}
.cover{position:relative;border-radius:var(--r);overflow:hidden;border:1px solid var(--line)}
.cover img{width:100%;height:auto}
.cover__mast{position:absolute;left:0;right:0;top:0;padding:14px 16px 0;display:flex;justify-content:space-between;align-items:flex-start}
.cover__mast b{font:var(--hw) var(--nf,22vw)/.82 var(--fh);letter-spacing:var(--ls);color:#fff;mix-blend-mode:normal;text-shadow:0 10px 40px rgba(0,0,0,.4)}
.cover__no{font-size:12px;color:#fff;opacity:.8;text-align:right;line-height:1.3}
.cover__line{position:absolute;z-index:2;max-width:46%;padding:10px 12px;border-left:3px solid var(--acc);background:rgba(10,10,10,.55);-webkit-backdrop-filter:blur(8px);backdrop-filter:blur(8px);color:#fff;font-size:13px;line-height:1.3}
.cover__line b{display:block;font:var(--hw) 20px/1.05 var(--fh);color:#fff}
.cl1{left:12px;top:44%}.cl2{right:12px;top:62%;border-left:0;border-right:3px solid var(--acc);text-align:right}.cl3{left:12px;bottom:14px}
.h3x__lead{margin-top:24px;font:var(--hw) clamp(28px,4vw,52px)/1.08 var(--fh);letter-spacing:var(--ls)}
.h3x__lead em{font-style:normal;color:var(--acc)}
.h3x__b{margin-top:20px;display:grid;grid-template-columns:1fr 1fr;gap:10px}
.h3x__b .btn{padding:0 14px;font-size:15px}
.ab3{padding:100px 0 0}
.ab3__h{font:var(--hw) clamp(34px,5vw,64px)/1 var(--fh);letter-spacing:var(--ls)}
.ab3__h em{font-style:normal;color:var(--acc)}
.qa{margin-top:24px;border-top:1px solid var(--line)}
.qa__i{border-bottom:1px solid var(--line)}
.qa__q{width:100%;display:flex;justify-content:space-between;align-items:center;gap:14px;padding:20px 0;background:none;border:0;color:var(--t);font:var(--hw) clamp(20px,2.4vw,28px)/1.2 var(--fh);letter-spacing:var(--ls);text-align:left;cursor:pointer}
.qa__q i{flex:none;width:40px;height:40px;border-radius:50%;border:1px solid var(--line);display:grid;place-items:center;font-style:normal;font-size:20px;transition:transform .5s cubic-bezier(.16,1,.3,1),background .3s}
.qa__i.open .qa__q i{transform:rotate(45deg);background:var(--acc);border-color:var(--acc)}
.qa__a{display:grid;grid-template-rows:0fr;transition:grid-template-rows .6s cubic-bezier(.16,1,.3,1)}
.qa__i.open .qa__a{grid-template-rows:1fr}
.qa__a>div{overflow:hidden}
.qa__a p{padding:0 0 20px;color:var(--mute);max-width:46ch}
@media(min-width:900px){.h3x .w{display:grid;grid-template-columns:.9fr 1.1fr;gap:56px;align-items:center}.h3x__t{order:-1}.h3x__b{display:flex}}
''', html=f'''
<section class="h3x"><div class="w">
 <div class="cover"><img src="img/kirill.webp" alt="Кирилл">
  <div class="cover__mast"><b class="fitname"><span class="ln"><span>Кирилл</span></span></b><span class="cover__no">№ 01<br>2026</span></div>
  <div class="cover__line cl1"><b>3 сайта</b>шиномонтаж, авиа, стройка</div>
  <div class="cover__line cl2"><b>18 лет</b>и уже делаю сайты под ключ</div>
  <div class="cover__line cl3"><b>Беру проекты</b>пишите в Telegram</div>
 </div>
 <div class="h3x__t"><h1 class="h3x__lead" data-split>Делаю сайты, которые <em>приводят</em> клиентов</h1>
  <div class="h3x__b rv"><a class="btn btn--acc" href="#">Работы{ARR}</a><a class="btn btn--line" href="#">Написать</a></div></div>
</div></section>
<section class="ab3"><div class="w"><h2 class="ab3__h" data-split>Почему <em>я</em></h2>
 <div class="qa">
  <div class="qa__i open"><button class="qa__q" type="button">Кто вы?<i>+</i></button><div class="qa__a"><div><p>Меня зовут Кирилл, мне 18. Делаю лендинги для бизнеса: от разбора ниши до запуска сайта.</p></div></div></div>
  <div class="qa__i"><button class="qa__q" type="button">Чем вы лучше шаблона?<i>+</i></button><div class="qa__a"><div><p>Дизайн рисую под вашу нишу и ваше главное обещание. Шаблон одинаковый у всех, ваш сайт будет только у вас.</p></div></div></div>
  <div class="qa__i"><button class="qa__q" type="button">Как понять, что получится?<i>+</i></button><div class="qa__a"><div><p>До сборки показываю 2-3 варианта дизайна. Собираю только тот, что вы выбрали.</p></div></div></div>
  <div class="qa__i"><button class="qa__q" type="button">С кем я буду общаться?<i>+</i></button><div class="qa__a"><div><p>Со мной. Без менеджеров: вы пишете тому, кто делает сайт.</p></div></div></div>
 </div>
</div></section>''', js='''
gsap.from('.cover img',{scale:1.2,duration:1.8,ease:'expo.out'});
gsap.from('.cover__mast b .ln>span',{yPercent:110,duration:1.2,ease:'expo.out',delay:.3});
gsap.from('.cover__line',{x:function(i){return i===1?60:-60},opacity:0,stagger:.15,duration:1,ease:'expo.out',delay:.8});
document.querySelectorAll('.qa__i').forEach(function(it){it.querySelector('.qa__q').addEventListener('click',function(){var o=it.classList.contains('open');document.querySelectorAll('.qa__i').forEach(function(x){x.classList.remove('open')});if(!o)it.classList.add('open');});});
gsap.from('.qa__i',{y:30,opacity:0,stagger:.08,duration:.9,ease:'expo.out',scrollTrigger:{trigger:'.qa',start:'top 85%'}});
''')

# 4. Переписка + навыки-плашки
VARIANTS['h4'] = dict(title='Переписка', css='''
.h4x{padding:84px 0 30px}
.chat{display:grid;gap:10px;max-width:440px}
.msg{max-width:84%;padding:12px 16px;border-radius:20px 20px 20px 6px;background:var(--card);border:1px solid var(--line);font-size:17px;line-height:1.4;opacity:0;transform:translateY(14px) scale(.96);transform-origin:0 100%}
.msg b{color:var(--acc)}
.msg--ph{padding:6px;border-radius:20px 20px 20px 6px;width:84%}
.msg--ph img{border-radius:15px;width:100%;height:auto}
.msg--me{justify-self:end;border-radius:20px 20px 6px 20px;background:var(--acc);border-color:var(--acc);color:#fff;transform-origin:100% 100%}
.typing{display:inline-flex;gap:4px;padding:14px 16px;border-radius:20px;background:var(--card);border:1px solid var(--line);width:max-content;opacity:0}
.typing i{width:7px;height:7px;border-radius:50%;background:var(--mute);animation:ty 1s infinite}
.typing i:nth-child(2){animation-delay:.15s}.typing i:nth-child(3){animation-delay:.3s}
@keyframes ty{50%{transform:translateY(-4px);opacity:.4}}
.h4x__h{margin-top:30px;font:var(--hw) clamp(32px,5vw,64px)/1.03 var(--fh);letter-spacing:var(--ls)}
.h4x__h em{font-style:normal;color:var(--acc)}
.h4x__b{margin-top:22px;display:grid;grid-template-columns:1fr 1fr;gap:10px}
.h4x__b .btn{padding:0 14px;font-size:15px}
.ab4{padding:100px 0 0;overflow:hidden}
.ab4__t{font:var(--hw) clamp(26px,3.6vw,46px)/1.15 var(--fh);letter-spacing:var(--ls);max-width:20ch}
.ab4__t span{color:var(--mute)}
.chips{margin-top:30px;display:flex;flex-direction:column;gap:10px}
.chips__row{display:flex;gap:10px;width:max-content}
.chips__row span{display:inline-flex;align-items:center;gap:8px;height:52px;padding:0 22px;border-radius:999px;border:1px solid var(--line);font:var(--hw) 18px var(--fh);white-space:nowrap}
.chips__row span.a{background:var(--acc);border-color:var(--acc);color:#fff}
@media(min-width:900px){.h4x .w{display:grid;grid-template-columns:1fr 1fr;gap:60px;align-items:center}.h4x__b{display:flex}.chat{order:2}}
''', html=f'''
<section class="h4x"><div class="w">
 <div class="chat" id="chat">
  <div class="msg">Привет! Я <b>Кирилл</b>, мне 18</div>
  <div class="msg msg--ph ph-full"><img src="img/kirill.webp" alt="Кирилл"></div>
  <div class="msg">Делаю сайты для бизнеса, которые приводят заявки</div>
  <div class="msg msg--me">А примеры есть?</div>
  <div class="typing" id="typing"><i></i><i></i><i></i></div>
  <div class="msg">Конечно, три сайта ниже. Каждый можно открыть</div>
 </div>
 <div><h1 class="h4x__h" data-split>Сайты, которые <em>приводят</em> клиентов</h1>
  <div class="h4x__b rv"><a class="btn btn--acc" href="#">Работы{ARR}</a><a class="btn btn--line" href="#">Написать</a></div></div>
</div></section>
<section class="ab4"><div class="w"><p class="ab4__t rv">Беру сайт целиком. <span>От первого эскиза до запуска, без студий и менеджеров.</span></p></div>
 <div class="chips">
  <div class="chips__row" id="r1"><span class="a">Дизайн под нишу</span><span>Анимации</span><span>Версия для телефона</span><span class="a">Запуск</span><span>Домен</span><span>Дизайн под нишу</span><span>Анимации</span><span>Версия для телефона</span></div>
  <div class="chips__row" id="r2"><span>Разбор конкурентов</span><span class="a">2-3 варианта дизайна</span><span>Тексты</span><span>Скорость</span><span class="a">Заявки</span><span>Разбор конкурентов</span><span>2-3 варианта дизайна</span><span>Тексты</span></div>
 </div>
</section>''', js='''
var tl=gsap.timeline({delay:.3}),ms=document.querySelectorAll('#chat .msg');
tl.to(ms[0],{opacity:1,y:0,scale:1,duration:.5,ease:'back.out(1.6)'})
  .to(ms[1],{opacity:1,y:0,scale:1,duration:.7,ease:'back.out(1.4)'},'+=.35')
  .to(ms[2],{opacity:1,y:0,scale:1,duration:.5,ease:'back.out(1.6)'},'+=.4')
  .to(ms[3],{opacity:1,y:0,scale:1,duration:.5,ease:'back.out(1.6)'},'+=.6')
  .to('#typing',{opacity:1,duration:.2},'+=.3').to('#typing',{opacity:0,height:0,padding:0,duration:.2},'+=1')
  .to(ms[4],{opacity:1,y:0,scale:1,duration:.5,ease:'back.out(1.6)'});
gsap.fromTo('#r1',{x:0},{x:-300,ease:'none',scrollTrigger:{trigger:'.ab4',start:'top bottom',end:'bottom top',scrub:true}});
gsap.fromTo('#r2',{x:-300},{x:0,ease:'none',scrollTrigger:{trigger:'.ab4',start:'top bottom',end:'bottom top',scrub:true}});
''')

SPLIT_JS = r'''
document.querySelectorAll('[data-split]').forEach(function (el) {
  el.innerHTML = el.innerHTML.split(/<br\s*\/?>/i).map(function (line) {
    return line.trim().split(/\s+(?![^<]*>)/).map(function (w) { return '<span class="ln"><span>' + w + '</span></span>'; }).join(' ');
  }).join('<br>');
});
document.querySelectorAll('.fitname').forEach(function (nm) {
  var inner = nm.querySelector('.ln');
  var fit = function () { nm.style.setProperty('--nf', '100px'); var box = nm.parentNode.getBoundingClientRect().width - 8; nm.style.setProperty('--nf', Math.min(100 * box / inner.getBoundingClientRect().width, 240) + 'px'); };
  fit(); addEventListener('resize', fit); if (document.fonts) document.fonts.ready.then(fit);
});
'''

def page(k, v):
    return f'''<!doctype html>
<html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Кирилл: {v["title"]}</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family={TH["fonts"]}&display=swap" rel="stylesheet">
<style>{gen.BASE_CSS}{TH["css"]}{COMMON_CSS}{v["css"]}</style></head>
<body>
<header class="nav"><div class="w"><b>Кирилл</b><nav><a href="#">Работы</a><a href="#">Процесс</a><a class="tg" href="#">Telegram</a></nav></div></header>
<main>{v["html"]}
<div class="sec-next"><div class="w"><h2 class="h2" data-split>Примеры<br><em>сайтов</em></h2></div></div>
</main>
<script>{SPLIT_JS}</script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
<script>
(function(){{
  if (!window.gsap || matchMedia('(prefers-reduced-motion: reduce)').matches) {{ document.querySelectorAll('.rv,.msg,.typing').forEach(function(e){{e.style.opacity=1;e.style.transform='none';}}); return; }}
  gsap.registerPlugin(ScrollTrigger);
  gsap.from('main [data-split] .ln>span', {{ yPercent: 110, duration: 1.1, stagger: .05, ease: 'expo.out', delay: .4 }});
  document.querySelectorAll('.rv').forEach(function(e){{ gsap.to(e, {{ opacity: 1, y: 0, duration: 1, ease: 'expo.out', scrollTrigger: {{ trigger: e, start: 'top 92%' }} }}); }});
  {v["js"]}
}})();
</script>
</body></html>'''

for k, v in VARIANTS.items():
    open(f'{k}.html', 'w').write(page(k, v))
print('ok')
