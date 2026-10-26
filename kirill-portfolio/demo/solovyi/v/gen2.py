# Живые варианты первого экрана «Соловьи»: зелёный + белый, движение и интерактив
HEAD = '''<!doctype html>
<html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>ЖК «Соловьи» · {t}</title><meta name="robots" content="noindex">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Unbounded:wght@500;600;700&family=Manrope:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>{css}</style></head><body>'''
BASE = '''
:root{--g:#1f4d3a;--g2:#163a2c;--gl:#eaf2ed;--line:#d7e4dc;--mute:#5d6f66;--ease:cubic-bezier(.16,1,.3,1);--fh:"Unbounded",system-ui,sans-serif;--fb:"Manrope",system-ui,sans-serif}
*{box-sizing:border-box;margin:0;padding:0}
body{background:#fff;color:var(--g);font:400 16px/1.5 var(--fb);-webkit-font-smoothing:antialiased;overflow-x:hidden}
a{color:inherit;text-decoration:none} img{display:block;max-width:100%}
.top{position:relative;z-index:5;display:flex;align-items:center;gap:20px;padding:16px 18px}
.logo{display:flex;align-items:center;gap:10px;font:700 15px var(--fh)}
.logo i{width:36px;height:36px;border-radius:50%;background:var(--g);color:#fff;display:grid;place-items:center;font-size:19px}
.nav{display:none;gap:26px;font-size:14px;font-weight:500}
.sp{flex:1}
.call{height:44px;padding:0 16px;display:inline-flex;align-items:center;gap:8px;border-radius:999px;border:1.5px solid currentColor;font-weight:600;font-size:14px}
.call .l{display:none}
.btn{height:58px;display:inline-flex;align-items:center;justify-content:center;gap:10px;padding:0 28px;border-radius:999px;font-weight:700;font-size:16px;transition:transform .3s var(--ease),background .3s}
.btn:active{transform:scale(.98)}
.btn i{font-size:19px;transition:transform .3s var(--ease)}
.btn:hover i{transform:translate(3px,-3px)}
.btn--g{background:var(--g);color:#fff}.btn--g:hover{background:var(--g2)}
.btn--w{background:#fff;color:var(--g)}
.rv{opacity:0;filter:blur(10px);transform:translate3d(0,18px,0);transition:opacity 1s var(--ease),filter 1s var(--ease),transform 1.1s var(--ease);transition-delay:var(--d,0s)}
.ld .rv{opacity:1;filter:blur(0);transform:none}
.mq{overflow:hidden;white-space:nowrap;background:var(--g);color:#fff;padding:16px 0}
.mq div{display:inline-flex;gap:34px;padding-right:34px;font:500 15px var(--fh);animation:mq 26s linear infinite}
.mq span{display:inline-flex;align-items:center;gap:34px}
.mq span::after{content:"";width:7px;height:7px;border-radius:50%;background:#fff;opacity:.5}
@keyframes mq{to{transform:translateX(-50%)}}
@media(min-width:900px){.top{padding:22px 48px}.nav{display:flex}.call .l{display:inline}.call .s{display:none}}
@media(prefers-reduced-motion:reduce){.rv{transition:none;opacity:1;filter:none;transform:none}.mq div{animation:none}}
'''
TOP = '<header class="top rv"><a class="logo" href="#"><i class="ti ti-feather"></i>ЖК Соловьи</a><nav class="nav"><a href="#">Дома</a><a href="#">Планировки</a><a href="#">Ипотека</a><a href="#">Контакты</a></nav><span class="sp"></span><a class="call" href="tel:+79228993550"><i class="ti ti-phone"></i><span class="l">8 (922) 899-35-50</span><span class="s">Позвонить</span></a></header>'
CTA = 'href="https://t.me/ElenaYurevna13" target="_blank" rel="noopener"'
MQ = '<div class="mq" aria-hidden="true"><div>' + ''.join('<span>%s</span>' % t for t in ['Готовые дома', 'Закрытая территория', '10 минут до Оренбурга', 'Семейная ипотека', 'Экскурсия по посёлку'] * 2) + '</div></div>'
END = '<script>requestAnimationFrame(function(){requestAnimationFrame(function(){document.body.classList.add("ld")})});</script>'

V = {}

# 5. Арка: фото в форме арки, плавающие плашки, бегущая строка
V['5'] = ('Арка', '''
.h{min-height:100svh;display:flex;flex-direction:column;background:radial-gradient(70% 60% at 85% 30%,var(--gl),#fff 70%)}
.g{flex:1;display:grid;gap:30px;padding:10px 18px 30px;align-items:center}
.t{display:flex;flex-direction:column;gap:18px}
.k{align-self:flex-start;display:inline-flex;align-items:center;gap:8px;height:34px;padding:0 14px;border-radius:999px;background:var(--gl);font-size:13px;font-weight:700}
.k i{width:8px;height:8px;border-radius:50%;background:var(--g);animation:pl 2s ease-out infinite}
@keyframes pl{0%{box-shadow:0 0 0 0 rgba(31,77,58,.45)}70%{box-shadow:0 0 0 9px rgba(31,77,58,0)}}
h1{font:600 clamp(32px,4.4vw,66px)/1.04 var(--fh);letter-spacing:-.03em}
h1 u{text-decoration:none;position:relative;white-space:nowrap}
h1 u::after{content:"";position:absolute;left:0;right:0;bottom:.04em;height:.14em;background:var(--g);opacity:.18;border-radius:9px;transform:scaleX(0);transform-origin:0 50%;transition:transform 1s var(--ease) 1.1s}
.ld h1 u::after{transform:none}
.sub{color:var(--mute);max-width:38ch}
.row{display:flex;flex-wrap:wrap;gap:10px;align-items:center}
.sz{display:flex;gap:6px}
.sz b{height:40px;padding:0 14px;display:inline-flex;align-items:center;border-radius:999px;border:1.5px solid var(--line);font:600 14px var(--fh)}
.arch{position:relative;justify-self:center;width:min(100%,520px);aspect-ratio:4/5}
.arch .ph{position:absolute;inset:0;border-radius:28px;overflow:hidden;box-shadow:0 40px 80px -40px rgba(31,77,58,.6)}
.arch img{width:100%;height:100%;object-fit:cover;transform:scale(1.12);transition:transform 2.2s var(--ease)}
.ld .arch img{transform:none}
.chip{position:absolute;z-index:2;display:flex;align-items:center;gap:10px;padding:12px 16px;border-radius:18px;background:rgba(255,255,255,.92);-webkit-backdrop-filter:blur(10px);backdrop-filter:blur(10px);box-shadow:0 18px 40px -20px rgba(31,77,58,.5);font-weight:600;font-size:14px;will-change:transform}
.chip i{width:36px;height:36px;border-radius:12px;background:var(--g);color:#fff;display:grid;place-items:center;font-size:19px}
.chip small{display:block;font-weight:500;color:var(--mute);font-size:12px}
.c1{left:-6px;top:18%}.c2{right:-6px;top:48%}.c3{left:6%;bottom:6%}
.in{display:flex;gap:6px;position:absolute;z-index:2;right:12px;bottom:12px}
@media(min-width:900px){.g{grid-template-columns:.85fr 1.15fr;gap:56px;padding:10px 48px 40px}.c1{left:-50px;top:12%}.c2{right:-24px;top:42%}.c3{left:-40px;bottom:10%}.arch{width:100%;aspect-ratio:auto;height:min(70svh,620px)}.arch img{object-position:50% 72%}}
''', '<section class="h">' + TOP + '''<div class="g"><div class="t">
<span class="k rv" style="--d:.2s"><i></i>Готовые дома — можно заезжать</span>
<h1 class="rv" style="--d:.3s">Свой дом в <u>10 минутах</u> от Оренбурга</h1>
<p class="sub rv" style="--d:.4s">Закрытая территория, готовые дома 120, 138 и 170 м². Семейная ипотека. Приезжайте посмотреть вживую.</p>
<div class="row rv" style="--d:.5s"><a class="btn btn--g" ''' + CTA + '''>Записаться на экскурсию<i class="ti ti-arrow-up-right"></i></a><div class="sz"><b>120 м²</b><b>138 м²</b><b>170 м²</b></div></div></div>
<div class="arch rv" style="--d:.25s"><div class="ph"><picture><source media="(min-width:900px)" srcset="house-d.webp"><img src="house-m.webp" alt="Дом в ЖК «Соловьи»"></picture></div>
<div class="chip c1" data-f="1.2"><i class="ti ti-lock"></i><div>Закрытая<small>территория посёлка</small></div></div>
<div class="chip c2" data-f="-1"><i class="ti ti-road"></i><div>10 минут<small>до Оренбурга</small></div></div>
<div class="chip c3" data-f=".8"><i class="ti ti-home-heart"></i><div>Семейная ипотека<small>на готовые дома</small></div></div></div>
</div>''' + MQ + '''</section>''', '''
// плашки покачиваются и смещаются за курсором
var ch=document.querySelectorAll('.chip'),t0=performance.now(),mx=0,my=0;
addEventListener('mousemove',function(e){mx=e.clientX/innerWidth-.5;my=e.clientY/innerHeight-.5});
if(!matchMedia('(prefers-reduced-motion: reduce)').matches)(function f(t){var s=(t-t0)/1000;ch.forEach(function(c,i){var k=+c.dataset.f;c.style.transform='translate3d('+(mx*24*k)+'px,'+(Math.sin(s*1.2+i*2)*6+my*18*k)+'px,0)'});requestAnimationFrame(f)})(t0);
''')

# 6. Выбор дома: вкладки 120/138/170 меняют фото и цифры
V['6'] = ('Выбор дома', '''
body{background:var(--g)}
.h{min-height:100svh;display:flex;flex-direction:column;background:var(--g);color:#fff}
.top .logo i{background:#fff;color:var(--g)}
.g{flex:1;display:grid;gap:22px;padding:10px 18px 24px}
.t{display:flex;flex-direction:column;gap:16px;justify-content:center}
h1{font:600 clamp(30px,4.2vw,62px)/1.05 var(--fh);letter-spacing:-.03em}
.sub{color:rgba(255,255,255,.75);max-width:38ch}
.tabs{display:flex;gap:6px;padding:6px;border-radius:999px;background:rgba(255,255,255,.08);align-self:flex-start;position:relative}
.tabs button{position:relative;z-index:1;height:46px;padding:0 18px;border:0;background:none;color:rgba(255,255,255,.75);font:600 15px var(--fh);cursor:pointer;transition:color .3s}
.tabs button.on{color:var(--g)}
.tabs .pill{position:absolute;z-index:0;top:6px;bottom:6px;left:6px;border-radius:999px;background:#fff;transition:transform .5s var(--ease),width .5s var(--ease)}
.stat{display:grid;grid-template-columns:repeat(3,1fr);gap:8px}
.stat div{padding:14px;border-radius:18px;border:1px solid rgba(255,255,255,.18)}
.stat b{display:block;font:600 24px/1 var(--fh)}
.stat span{display:block;margin-top:6px;font-size:12px;color:rgba(255,255,255,.7)}
.view{position:relative;border-radius:28px;overflow:hidden;min-height:320px;background:#2a5c47}
.view img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:0;transform:scale(1.06);transition:opacity .8s var(--ease),transform 1.4s var(--ease)}
.view img.on{opacity:1;transform:none}
.tag{position:absolute;z-index:2;left:14px;top:14px;padding:8px 14px;border-radius:999px;background:#fff;color:var(--g);font:600 14px var(--fh)}
@media(min-width:900px){.g{grid-template-columns:.9fr 1.1fr;gap:48px;padding:10px 48px 40px}.view{min-height:0}}
''', '<section class="h">' + TOP + '''<div class="g"><div class="t">
<h1 class="rv" style="--d:.2s">Выберите свой готовый дом</h1>
<p class="sub rv" style="--d:.3s">Закрытая территория в 10 минутах от Оренбурга. Семейная ипотека.</p>
<div class="tabs rv" style="--d:.4s" id="tabs"><span class="pill"></span><button class="on" type="button" data-i="0">120 м²</button><button type="button" data-i="1">138 м²</button><button type="button" data-i="2">170 м²</button></div>
<div class="stat rv" style="--d:.5s"><div><b id="s1">120</b><span>м² площадь</span></div><div><b>10</b><span>минут до города</span></div><div><b>3</b><span>варианта домов</span></div></div>
<a class="btn btn--w rv" style="--d:.6s" ''' + CTA + '''>Записаться на экскурсию<i class="ti ti-arrow-up-right"></i></a></div>
<div class="view rv" style="--d:.3s"><span class="tag" id="tag">Готовый дом</span><img class="on" src="house-d.webp" alt="Дом 120 м²"><img src="village-l.webp" alt="Посёлок"><img src="interior-l.webp" alt="Гостиная"></div>
</div>''' + MQ.replace('class="mq"', 'class="mq" style="background:#fff;color:var(--g)"') + '''</section>''', '''
var tabs=document.getElementById('tabs'),bs=tabs.querySelectorAll('button'),pill=tabs.querySelector('.pill'),im=document.querySelectorAll('.view img'),s1=document.getElementById('s1'),tag=document.getElementById('tag'),A=[120,138,170];
function go(i){bs.forEach(function(b,j){b.classList.toggle('on',i===j)});im.forEach(function(m,j){m.classList.toggle('on',i===j)});pill.style.width=bs[i].offsetWidth+'px';pill.style.transform='translateX('+(bs[i].offsetLeft-6)+'px)';tag.textContent=['Готовый дом','Вид на посёлок','Внутри дома'][i];
 var from=+s1.textContent,to=A[i],t0=performance.now();(function f(t){var p=Math.min(1,(t-t0)/600);s1.textContent=Math.round(from+(to-from)*(1-Math.pow(1-p,3)));if(p<1)requestAnimationFrame(f)})(t0)}
bs.forEach(function(b,i){b.addEventListener('click',function(){go(i)})});go(0);addEventListener('resize',function(){go([].indexOf.call(bs,tabs.querySelector('.on')))});
''')

# 7. Раскрытие: фото в маленькой рамке раскрывается на весь экран при прокрутке
V['7'] = ('Раскрытие', '''
.h{text-align:center}
.t{padding:14px 18px 0;display:flex;flex-direction:column;align-items:center;gap:16px}
.k{display:inline-flex;align-items:center;gap:8px;height:34px;padding:0 14px;border-radius:999px;background:var(--gl);font-size:13px;font-weight:700}
h1{font:600 clamp(34px,6vw,96px)/1 var(--fh);letter-spacing:-.035em;max-width:14ch}
h1 span{display:inline-block}
.sub{color:var(--mute);max-width:40ch}
.pin{height:220svh;margin-top:26px}
.st{position:sticky;top:0;height:100svh;display:grid;place-items:center;overflow:hidden}
.fr{position:relative;width:var(--w,78vw);height:var(--hh,46svh);border-radius:var(--r,28px);overflow:hidden;will-change:width,height}
.fr img{width:100%;height:100%;object-fit:cover;transform:scale(var(--s,1.15))}
.ov{position:absolute;inset:0;background:linear-gradient(180deg,rgba(22,58,44,0) 40%,rgba(22,58,44,.85));opacity:var(--o,0)}
.cap{position:absolute;left:0;right:0;bottom:0;padding:22px 18px;color:#fff;text-align:left;display:grid;gap:14px;opacity:var(--o,0);transform:translateY(calc((1 - var(--o,0)) * 30px))}
.cap b{font:600 clamp(22px,2.6vw,38px)/1.1 var(--fh);max-width:18ch}
.cap .sz{display:flex;gap:8px;flex-wrap:wrap}
.cap .sz span{height:40px;padding:0 16px;display:inline-flex;align-items:center;border-radius:999px;background:rgba(255,255,255,.14);border:1px solid rgba(255,255,255,.3);font:600 14px var(--fh)}
.cap .btn{justify-self:start}
.hint{margin-top:20px;font-size:13px;color:var(--mute);display:flex;align-items:center;gap:6px;justify-content:center}
@media(min-width:900px){.cap{padding:48px;grid-template-columns:1fr auto;align-items:end}.cap .sz{grid-column:1}.cap .btn{grid-column:2;grid-row:1/3}}
''', TOP + '''<section class="h"><div class="t">
<span class="k rv" style="--d:.2s">Закрытый посёлок · 10 минут от Оренбурга</span>
<h1 class="rv" style="--d:.3s">Дом, в&nbsp;который можно заехать уже сейчас</h1>
<p class="sub rv" style="--d:.4s">Готовые дома 120, 138 и 170 м². Семейная ипотека.</p>
<a class="btn btn--g rv" style="--d:.5s" ''' + CTA + '''>Записаться на экскурсию<i class="ti ti-arrow-up-right"></i></a></div>
<div class="pin" id="pin"><div class="st"><div class="fr" id="fr"><picture><source media="(min-width:900px)" srcset="house-d.webp"><img src="house-m.webp" alt="Готовый дом"></picture><div class="ov"></div>
<div class="cap"><b>Готовые дома на закрытой территории</b><div class="sz"><span>120 м²</span><span>138 м²</span><span>170 м²</span></div><a class="btn btn--w" ''' + CTA + '''>Хочу на экскурсию<i class="ti ti-arrow-up-right"></i></a></div></div></div></div></section>''' + MQ, '''
var pin=document.getElementById('pin'),fr=document.getElementById('fr'),tk=false;
function up(){tk=false;var r=pin.getBoundingClientRect(),p=Math.min(1,Math.max(0,-r.top/(r.height-innerHeight)*1.4)),e=1-Math.pow(1-p,3);
 fr.style.setProperty('--w',(78+22*e)+'vw');fr.style.setProperty('--hh',(46+54*e)+'svh');fr.style.setProperty('--r',(28*(1-e))+'px');fr.style.setProperty('--s',(1.15-.15*e));fr.style.setProperty('--o',Math.max(0,(p-.55)/.45));}
addEventListener('scroll',function(){if(!tk){tk=true;requestAnimationFrame(up)}},{passive:true});addEventListener('resize',up);up();
''')

# 8. Вырезанный дом: стоит на странице без фона, вокруг плавают плашки
V['8'] = ('Вырезанный дом', V['5'][1].replace('.arch{','.archX{') + """
.stage{position:relative;justify-self:center;width:100%;max-width:640px;padding:40px 0 30px}
.blob{position:absolute;left:50%;top:50%;width:92%;aspect-ratio:1;transform:translate(-50%,-52%);border-radius:50%;background:radial-gradient(circle at 50% 40%,#d9e9df,#eaf2ed 60%,rgba(234,242,237,0) 71%)}
.house{position:relative;z-index:1;width:100%;filter:drop-shadow(0 30px 30px rgba(31,77,58,.22));transform:translate3d(0,30px,0) scale(.96);opacity:0;transition:transform 1.4s var(--ease) .3s,opacity 1s var(--ease) .3s}
.ld .house{transform:none;opacity:1}
.ground{position:absolute;z-index:0;left:6%;right:6%;bottom:28px;height:34px;border-radius:50%;background:radial-gradient(closest-side,rgba(31,77,58,.28),rgba(31,77,58,0))}
.stage{padding:64px 0 76px}.stage .chip{padding:9px 12px;font-size:13px}.stage .chip i{width:30px;height:30px;font-size:16px}.stage .c1{left:0;top:0}.stage .c2{right:0;top:0}.stage .c3{left:50%;bottom:6px;margin-left:-90px}.ground{bottom:70px}
@media(min-width:900px){.stage{max-width:none;padding:40px 0 30px}.stage .chip{padding:12px 16px;font-size:14px}.stage .chip i{width:36px;height:36px;font-size:19px}.stage .c3{margin-left:0}.ground{bottom:28px}.stage .c1{left:2%;top:0}.stage .c2{right:-10px;top:22%}.stage .c3{left:12%;bottom:-4px}}
""", V['5'][2].split('<div class="arch rv"')[0] + """<div class="stage rv" style="--d:.2s"><span class="blob"></span><span class="ground"></span><img class="house" src="house-cut.webp" alt="Дом в ЖК «Соловьи»">
<div class="chip c1" data-f="1.2"><i class="ti ti-lock"></i><div>Закрытая<small>территория посёлка</small></div></div>
<div class="chip c2" data-f="-1"><i class="ti ti-road"></i><div>10 минут<small>до Оренбурга</small></div></div>
<div class="chip c3" data-f=".8"><i class="ti ti-home-heart"></i><div>Семейная ипотека<small>на готовые дома</small></div></div></div>
</div>""" + MQ + '</section>', V['5'][3])

for k, (name, css, html, js) in V.items():
    open(k + '.html', 'w').write(HEAD.format(t=name, css=BASE + css) + html + END + '<script>(function(){' + js + '})();</script></body></html>')
print('ok')
