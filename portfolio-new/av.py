# Демо: четыре варианта блока «О себе» внутри полного портфолио (тема «Красная ночь»)
import gen

AB = {}
ARR = gen.ARR

# 1. Текст с картинками внутри строк
AB['a1'] = dict(title='Текст с картинками', css='''
.aba{padding:110px 0 90px}
.aba__k{font-size:14px;color:var(--mute);margin-bottom:18px}
.aba__t{font:var(--hw) clamp(32px,5.4vw,76px)/1.12 var(--fh);letter-spacing:var(--ls)}
.aba__t .wd{opacity:.15}
.pill{display:inline-block;vertical-align:middle;width:1.7em;height:.95em;margin:0 .08em;border-radius:999px;overflow:hidden;transform:scale(0);box-shadow:0 0 0 2px var(--bg),0 0 0 3px var(--line)}
.pill img{width:100%;height:100%;object-fit:cover}
.pill--me img{object-position:50% 38%}
.aba__t em{font-style:normal;color:var(--acc)}
.aba__s{margin-top:34px;font-size:17px;color:var(--mute);max-width:40ch}
''', html='''
<section class="about aba"><div class="w">
 <p class="aba__k">О себе</p>
 <p class="aba__t" id="abaT"><span class="wd">Я</span> <span class="wd">Кирилл,</span> <span class="pill pill--me"><img src="img/kirill.webp" alt=""></span> <span class="wd">мне</span> <span class="wd">18.</span> <span class="wd">Делаю</span> <span class="wd">сайты</span> <span class="wd">для</span> <span class="pill"><img src="img/protektor-1.webp" alt=""></span> <span class="wd">шиномонтажа,</span> <span class="pill"><img src="img/altitude-1.webp" alt=""></span> <span class="wd">авиакомпании</span> <span class="wd">и</span> <span class="pill"><img src="img/forte-1.webp" alt=""></span> <span class="wd">стройки.</span> <span class="wd">Каждый</span> <span class="wd">под</span> <span class="wd">свою</span> <span class="wd"><em>нишу,</em></span> <span class="wd">а</span> <span class="wd">не</span> <span class="wd">по</span> <span class="wd"><em>шаблону.</em></span></p>
 <p class="aba__s">Пишете мне, и отвечает тот, кто делает ваш сайт. Без менеджеров и студий.</p>
</div></section>''', js='''
(function(){ if(!window.gsap||matchMedia('(prefers-reduced-motion: reduce)').matches){document.querySelectorAll('.aba .wd').forEach(function(w){w.style.opacity=1});document.querySelectorAll('.pill').forEach(function(p){p.style.transform='none'});return;}
 var tl=gsap.timeline({scrollTrigger:{trigger:'#abaT',start:'top 80%',end:'bottom 45%',scrub:true}});
 document.querySelectorAll('#abaT > span').forEach(function(el,i){ if(el.classList.contains('pill')) tl.to(el,{scale:1,ease:'back.out(2)',duration:1},i*.5); else tl.to(el,{opacity:1,duration:.6},i*.5); });
})();''')

# 2. Колода карточек, которые смахиваются
AB['a2'] = dict(title='Колода карточек', css='''
.abb{padding:100px 0 90px;overflow:hidden}
.abb .w{display:grid;gap:34px}
.abb__k{font-size:14px;color:var(--mute)}
.abb__h{margin-top:10px;font:var(--hw) clamp(32px,4.6vw,60px)/1.04 var(--fh);letter-spacing:var(--ls)}
.abb__h em{font-style:normal;color:var(--acc)}
.abb__p{margin-top:14px;color:var(--mute);max-width:32ch}
.deck{position:relative;height:380px;max-width:360px;width:100%;justify-self:center;touch-action:pan-y}
.dc{position:absolute;inset:0;border-radius:26px;padding:28px;display:flex;flex-direction:column;cursor:grab;user-select:none;box-shadow:0 30px 60px -25px rgba(0,0,0,.8)}
.dc:active{cursor:grabbing}
.dc b{font:var(--hw) 84px/1 var(--fh);letter-spacing:var(--ls)}
.dc h3{margin-top:auto;font:var(--hw) 28px/1.1 var(--fh);letter-spacing:var(--ls)}
.dc p{margin-top:8px;font-size:16px;opacity:.85}
.dc--r{background:var(--acc);color:#fff}
.dc--w{background:#f3f1ec;color:#111}
.dc--d{background:#1c1c1f;color:var(--t);border:1px solid var(--line)}
.dc--d b{color:var(--acc)}
.dc--g{background:#2b2b30;color:var(--t)}
.deck__ui{display:flex;justify-content:space-between;align-items:center;max-width:360px;width:100%;justify-self:center;margin-top:-10px}
.deck__ui span{font-size:14px;color:var(--mute)}
.deck__ui button{height:48px;padding:0 20px;border-radius:999px;border:1px solid var(--line);background:none;color:var(--t);font:600 14px var(--fb);cursor:pointer}
@media(min-width:900px){.abb .w{grid-template-columns:1fr 1fr;align-items:center}.deck,.deck__ui{justify-self:end}.deck__ui{grid-column:2}}
''', html='''
<section class="about abb"><div class="w">
 <div><p class="abb__k">О себе</p><h2 class="abb__h">Четыре карты <em>про меня</em></h2><p class="abb__p">Смахните карточку пальцем или нажмите «Дальше».</p></div>
 <div class="deck" id="deck">
  <div class="dc dc--r"><b>18</b><h3>лет, и делаю сайты</h3><p>Меня зовут Кирилл. Лендинги для бизнеса под ключ.</p></div>
  <div class="dc dc--w"><b>1</b><h3>человек на проекте</h3><p>Без менеджеров: вы пишете тому, кто делает сайт.</p></div>
  <div class="dc dc--d"><b>2-3</b><h3>варианта дизайна</h3><p>Выбираете до того, как я начну собирать.</p></div>
  <div class="dc dc--g"><b>0</b><h3>шаблонов</h3><p>Каждый сайт рисую под нишу и главное обещание бизнеса.</p></div>
 </div>
 <div class="deck__ui"><span id="deckN">1 / 4</span><button type="button" id="deckNext">Дальше</button></div>
</div></section>''', js='''
(function(){
 var deck=document.getElementById('deck'); if(!deck) return;
 var cards=[].slice.call(deck.children), n=cards.length, idx=0, busy=false;
 var lay=function(anim){ cards.forEach(function(c,i){ var p=(i-idx+n)%n; var props={zIndex:n-p,y:p*14,scale:1-p*.05,rotation:p?(p%2?3:-3):0,opacity:p>2?0:1}; if(window.gsap&&anim) gsap.to(c,Object.assign({duration:.6,ease:'expo.out'},props)); else if(window.gsap) gsap.set(c,props); else {c.style.zIndex=n-p;c.style.transform='translateY('+p*14+'px) scale('+(1-p*.05)+')';} }); document.getElementById('deckN').textContent=(idx+1)+' / '+n; };
 var fly=function(dir){ if(busy) return; busy=true; var c=cards[idx]; var go=function(){ idx=(idx+1)%n; lay(true); busy=false; };
  if(window.gsap) gsap.to(c,{x:dir*innerWidth,rotation:dir*25,duration:.5,ease:'power2.in',onComplete:function(){gsap.set(c,{x:0});go();}}); else go(); };
 lay(false);
 document.getElementById('deckNext').addEventListener('click',function(){fly(1)});
 var sx=0,dx=0,drag=false;
 deck.addEventListener('pointerdown',function(e){ if(busy) return; drag=true; sx=e.clientX; dx=0; deck.setPointerCapture(e.pointerId); });
 deck.addEventListener('pointermove',function(e){ if(!drag) return; dx=e.clientX-sx; if(window.gsap) gsap.set(cards[idx],{x:dx,rotation:dx/18}); });
 deck.addEventListener('pointerup',function(){ if(!drag) return; drag=false; if(Math.abs(dx)>80) fly(dx>0?1:-1); else if(window.gsap) gsap.to(cards[idx],{x:0,rotation:0,duration:.5,ease:'back.out(2)'}); });
 if(window.gsap&&!matchMedia('(prefers-reduced-motion: reduce)').matches) gsap.from(cards,{y:120,opacity:0,rotation:-10,stagger:.08,duration:1,ease:'expo.out',scrollTrigger:{trigger:deck,start:'top 80%'},onComplete:function(){lay(false)}});
})();''')

# 3. Спросите меня: чат с кнопками-вопросами
AB['a3'] = dict(title='Спросите меня', css='''
.abc{padding:100px 0 90px}
.abc .w{display:grid;gap:30px}
.abc__k{font-size:14px;color:var(--mute)}
.abc__h{margin-top:10px;font:var(--hw) clamp(32px,4.6vw,60px)/1.04 var(--fh);letter-spacing:var(--ls)}
.abc__h em{font-style:normal;color:var(--acc)}
.chatb{border-radius:24px;background:var(--card);border:1px solid var(--line);padding:16px;display:flex;flex-direction:column;gap:10px;min-height:380px}
.chatb__top{display:flex;align-items:center;gap:10px;padding-bottom:12px;border-bottom:1px solid var(--line)}
.chatb__top img{width:40px;height:40px;border-radius:50%;object-fit:cover;object-position:50% 35%}
.chatb__top b{display:block;font-size:15px}
.chatb__top span{font-size:12px;color:#4ade80}
.chatb__log{display:flex;flex-direction:column;gap:8px;flex:1;max-height:440px;min-height:220px;overflow-y:auto;padding:4px 0;scroll-behavior:smooth}
.chatb__go{margin-top:6px;width:100%}
.bb{max-width:86%;padding:11px 15px;border-radius:18px 18px 18px 6px;background:#232327;color:#f3f1ec;font-size:16px;line-height:1.42}
.bb--me{align-self:flex-end;border-radius:18px 18px 6px 18px;background:var(--acc);color:#fff}
.bb--ty{display:inline-flex;gap:4px;width:max-content}
.bb--ty i{width:7px;height:7px;border-radius:50%;background:var(--mute);animation:tyb 1s infinite}
.bb--ty i:nth-child(2){animation-delay:.15s}.bb--ty i:nth-child(3){animation-delay:.3s}
@keyframes tyb{50%{transform:translateY(-4px);opacity:.4}}
.qs{display:flex;flex-wrap:wrap;gap:8px}
.qs button{height:42px;padding:0 16px;border-radius:999px;border:1px solid var(--acc);background:none;color:var(--t);font:500 14px var(--fb);cursor:pointer;transition:background .25s,opacity .25s}
.qs button:hover{background:color-mix(in srgb,var(--acc) 18%,transparent)}
.qs button.used{opacity:.35;pointer-events:none}
@media(min-width:900px){.abc .w{grid-template-columns:.9fr 1.1fr;align-items:center}}
''', html='''
<section class="about abc"><div class="w">
 <div><p class="abc__k">О себе</p><h2 class="abc__h">Спросите <em>меня</em></h2><p style="margin-top:14px;color:var(--mute);max-width:32ch">Ответил на вопросы, которые чаще всего задают перед заказом сайта. Нажимайте.</p></div>
 <div class="chatb">
  <div class="chatb__top"><img src="img/kirill.webp" alt=""><div><b>Кирилл</b><span>в сети</span></div></div>
  <div class="chatb__log" id="log"><div class="bb">Привет! Я Кирилл, делаю сайты для бизнеса. Выберите вопрос ниже, отвечу как в переписке.</div></div>
  <div class="qs" id="qs">
   <button type="button" data-a="Я Кирилл, мне 18 лет. Веб-дизайном занимаюсь около года.<br><br>Делаю лендинги для бизнеса под ключ: сам рисую дизайн, собираю сайт, оживляю его анимацией и запускаю.">Кто ты?</button>
   <button type="button" data-a="Шаблон одинаковый у сотен компаний, и клиент его не запоминает.<br><br>Я рисую дизайн под вашу нишу и главное обещание клиентам. Поэтому сайт выделяется среди конкурентов и ведёт к заявке.">Почему не шаблон?</button>
   <button type="button" data-a="1. Коротко обсуждаем ваш бизнес.<br>2. Разбираю нишу и конкурентов.<br>3. Показываю 2-3 варианта дизайна.<br>4. Собираю выбранный, вместе с версией для телефона.<br>5. Запускаю сайт и помогаю с доменом.">Как проходит работа?</button>
   <button type="button" data-a="Зависит от задачи и объёма. Точную цену назову после короткого разбора и зафиксирую её до начала работы. Никаких доплат по ходу.">Сколько стоит?</button>
   <button type="button" data-a="Тоже зависят от объёма. Срок называю заранее, после разбора, и вы знаете дату запуска с самого начала.">Какие сроки?</button>
   <button type="button" data-a="Рассказать о бизнесе и клиентах, прислать логотип и фото, если они есть. С текстами помогу.">Что нужно от меня?</button>
   <button type="button" data-a="Да. Версию для телефона продумываю отдельно, а не просто сжимаю компьютерную. Большинство клиентов заходят на сайт именно с телефона.">А на телефоне будет удобно?</button>
   <button type="button" data-a="Да. Сначала вы выбираете дизайн из вариантов, а правки по ходу мы обсуждаем и согласуем заранее.">Можно вносить правки?</button>
   <button type="button" data-a="Помогаю подключить домен и проверить, что заявки доходят. Если позже понадобится что-то поменять, просто напишите.">Что после запуска?</button>
   <button type="button" data-a="Напишите мне в Telegram, кнопка ниже. Отвечу и предложу, каким может быть ваш сайт.">Как с тобой связаться?</button>
  </div>
  <a class="btn btn--acc js-tg chatb__go" href="#">Написать в Telegram{ARR}</a>
 </div>
</div></section>''', js='''
(function(){
 var log=document.getElementById('log'); if(!log) return;
 var add=function(cls,html){ var d=document.createElement('div'); d.className='bb '+cls; d.innerHTML=html; log.appendChild(d); log.scrollTop=log.scrollHeight; if(window.gsap) gsap.from(d,{y:12,opacity:0,scale:.95,duration:.45,ease:'back.out(1.6)'}); return d; };
 document.querySelectorAll('#qs button').forEach(function(b){ b.addEventListener('click',function(){
  b.classList.add('used'); add('bb--me',b.textContent); var t=add('bb--ty','<i></i><i></i><i></i>');
  setTimeout(function(){ t.remove(); add('',b.getAttribute('data-a')); },900);
 }); });
})();''')

# 4. Переключатель «Обычно / Со мной»
AB['a4'] = dict(title='Обычно или со мной', css='''
.abd{padding:100px 0 90px}
.abd__k{font-size:14px;color:var(--mute)}
.abd__h{margin-top:10px;font:var(--hw) clamp(32px,4.6vw,60px)/1.04 var(--fh);letter-spacing:var(--ls)}
.abd__h em{font-style:normal;color:var(--acc)}
.sw{margin-top:26px;display:inline-flex;position:relative;padding:5px;border-radius:999px;background:var(--card);border:1px solid var(--line)}
.sw button{position:relative;z-index:1;height:48px;padding:0 22px;border:0;background:none;color:var(--mute);font:600 15px var(--fb);cursor:pointer;transition:color .3s}
.sw button.on{color:#fff}
.sw i{position:absolute;z-index:0;top:5px;bottom:5px;left:5px;border-radius:999px;background:var(--acc);transition:transform .5s cubic-bezier(.16,1,.3,1),width .5s cubic-bezier(.16,1,.3,1)}
.cmp{margin-top:26px;display:grid;gap:10px}
.cr{position:relative;display:grid;grid-template-columns:44px 1fr;gap:14px;align-items:center;padding:18px;border-radius:var(--r);background:var(--card);border:1px solid var(--line);overflow:hidden}
.cr__ic{width:44px;height:44px;border-radius:50%;display:grid;place-items:center;font-size:20px;font-weight:700;background:#26262a;color:var(--mute);transition:background .4s,color .4s}
.abd.me .cr__ic{background:var(--acc);color:#fff}
.cr__tx{position:relative;height:3.1em;overflow:hidden}
.cr__tx span{position:absolute;left:0;right:0;top:0;font:var(--hw) clamp(18px,2vw,24px)/1.3 var(--fh);letter-spacing:var(--ls);transition:transform .6s cubic-bezier(.16,1,.3,1),opacity .4s}
.cr__tx .b{transform:translateY(110%);opacity:0;color:var(--t)}
.cr__tx .a{color:var(--mute)}
.abd.me .cr__tx .a{transform:translateY(-110%);opacity:0}
.abd.me .cr__tx .b{transform:none;opacity:1}
@media(min-width:900px){.cmp{grid-template-columns:1fr 1fr}}
''', html='''
<section class="about abd" id="abd"><div class="w">
 <p class="abd__k">О себе</p><h2 class="abd__h">Как обычно и как <em>со мной</em></h2>
 <div class="sw" id="sw"><i></i><button type="button" class="on" data-m="0">Обычно</button><button type="button" data-m="1">Со мной</button></div>
 <div class="cmp">
  <div class="cr"><span class="cr__ic">1</span><div class="cr__tx"><span class="a">Задачу передают через менеджера</span><span class="b">Пишете напрямую тому, кто делает сайт</span></div></div>
  <div class="cr"><span class="cr__ic">2</span><div class="cr__tx"><span class="a">Берут готовый шаблон</span><span class="b">Рисую дизайн под вашу нишу</span></div></div>
  <div class="cr"><span class="cr__ic">3</span><div class="cr__tx"><span class="a">Показывают один вариант</span><span class="b">Даю 2-3 варианта на выбор</span></div></div>
  <div class="cr"><span class="cr__ic">4</span><div class="cr__tx"><span class="a">Телефон доделывают по остатку</span><span class="b">Отдельно продумываю версию для телефона</span></div></div>
 </div>
</div></section>''', js='''
(function(){
 var sec=document.getElementById('abd'); if(!sec) return;
 var sw=document.getElementById('sw'), bs=sw.querySelectorAll('button'), pill=sw.querySelector('i');
 var set=function(m){ bs.forEach(function(b){b.classList.toggle('on',+b.dataset.m===m)}); var b=bs[m]; pill.style.width=b.offsetWidth+'px'; pill.style.transform='translateX('+(b.offsetLeft-5)+'px)'; sec.classList.toggle('me',m===1); };
 bs.forEach(function(b){b.addEventListener('click',function(){set(+b.dataset.m)})});
 set(0); addEventListener('resize',function(){set(sec.classList.contains('me')?1:0)});
 if(window.ScrollTrigger) ScrollTrigger.create({trigger:sec,start:'top 35%',once:true,onEnter:function(){setTimeout(function(){set(1)},400)}});
 else setTimeout(function(){set(1)},1500);
 if(window.gsap&&!matchMedia('(prefers-reduced-motion: reduce)').matches) gsap.from('.cr',{y:30,opacity:0,stagger:.08,duration:.9,ease:'expo.out',scrollTrigger:{trigger:'.cmp',start:'top 85%'}});
})();''')

for v in AB.values():
    v['html'] = v['html'].replace('{ARR}', ARR)

if __name__ == '__main__':
    for k, v in AB.items():
        open(f'{k}.html', 'w').write(gen.page('v1', gen.THEMES['v1'], about=v))
    print('ok')
