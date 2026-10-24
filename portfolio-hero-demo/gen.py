ARR='<svg viewBox="0 0 24 24"><path d="M7 17 17 7M9 7h8v8"/></svg>'
def win(src,alt,cls=''):
    return f'<div class="win {cls}"><i class="b"><s></s><s></s><s></s></i><img src="img/{src}.webp" alt="{alt}"></div>'
SITES=[('protektor-1','ПРОТЕКТОР','Шиномонтаж'),('altitude-1','Altitude','Авиакомпания'),('forte-1','FORTE','Строительство домов')]
def page(title,font,css,body):
    return f'''<!doctype html>
<html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family={font}:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="base.css">
<style>body{{font-family:"{font.replace('+',' ')}",system-ui,sans-serif;-webkit-font-smoothing:antialiased}}
{css}</style></head><body>
{body}
<script>requestAnimationFrame(function(){{document.body.classList.add('ld')}});</script>
</body></html>'''
def nav(btn):
    return f'<header class="nav"><b>Кирилл</b><span></span><a class="l" href="#">Работы</a><a class="l" href="#">Обо мне</a><a class="btn {btn}" href="#">Написать</a></header>'

# 1. Сплит + полоса работ
h1=page('Вариант 1','Manrope','''
body{background:#ecebe7;color:#121212}
.h{min-height:100dvh;display:grid;grid-template-rows:1fr auto;padding:96px 40px 28px;gap:28px}
.g{display:grid;grid-template-columns:1.2fr .8fr;gap:56px;align-items:center}
h1{font-size:clamp(44px,5.2vw,82px);font-weight:800;line-height:1;letter-spacing:-.045em}
h1 em{font-style:normal;color:#ff4b1f}
p{margin-top:22px;font-size:19px;color:#5d5c58;max-width:40ch;font-weight:500}
.b1{margin-top:30px;display:flex;gap:10px}.acc{background:#ff4b1f;color:#fff}.acc:hover{background:#e83c12}.ln{border:1.5px solid #121212}.ln:hover{background:#121212;color:#ecebe7}
.ph{height:min(560px,58vh);border-radius:28px;overflow:hidden}.ph img{width:100%;height:100%;object-fit:cover;object-position:50% 25%}
.strip{display:grid;grid-template-columns:auto 1fr 1fr 1fr;gap:14px;align-items:center}
.strip>b{font-size:14px;font-weight:700;color:#5d5c58;padding-right:10px;line-height:1.3}
.s{display:flex;gap:12px;align-items:center;padding:8px;border-radius:18px;background:#fbfbf9;transition:transform .4s var(--ease)}
.s:hover{transform:translateY(-4px)}
.s .win{width:120px;flex:none;border-radius:10px;box-shadow:none}.s .win i.b{height:14px}.s .win i.b s{width:4px;height:4px}
.s span{font-weight:800;font-size:17px;letter-spacing:-.02em;line-height:1.2}.s small{display:block;font-weight:600;font-size:13px;color:#5d5c58;letter-spacing:0}
@media(max-width:899px){.h{padding:90px 16px 20px}.g{grid-template-columns:1fr;gap:28px}.ph{height:auto;aspect-ratio:4/5}.strip{grid-template-columns:1fr}}
''',nav('acc')+f'''<section class="h"><div class="g"><div>
<h1 class="in" style="--d:.1s">Делаю сайты, которые <em>продают</em> с первого экрана</h1>
<p class="in" style="--d:.25s">Меня зовут Кирилл, мне 18. Лендинги под ключ: дизайн, анимации, запуск.</p>
<div class="b1 in" style="--d:.4s"><a class="btn acc" href="#">Смотреть работы{ARR}</a></div></div>
<div class="ph in" style="--d:.2s"><img src="img/kirill.webp" alt="Кирилл"></div></div>
<div class="strip in" style="--d:.55s"><b>Последние<br>работы</b>'''+''.join(f'<a class="s" href="#">{win(s,n)}<span>{n}<small>{c}</small></span></a>' for s,n,c in SITES)+'</div></section>')

# 2. Имя с фото внутри строки
h2=page('Вариант 2','Onest','''
body{background:#f1f1ee;color:#111}
.h{min-height:100dvh;display:flex;flex-direction:column;justify-content:center;padding:100px 40px 48px}
.nm{display:flex;align-items:center;justify-content:center;gap:.08em;font-weight:800;font-size:min(17vw,30vh);line-height:.85;letter-spacing:-.06em}
.nm .p{width:.95em;height:.82em;border-radius:999px;overflow:hidden;flex:none;transform:scaleX(0);transition:transform 1.2s var(--ease) .35s}
.ld .nm .p{transform:none}
.nm .p img{width:100%;height:100%;object-fit:cover;object-position:50% 22%}
.nm .w{display:inline-block;overflow:hidden}.nm .w span{display:inline-block;transform:translateY(100%);transition:transform 1.1s var(--ease)}
.ld .nm .w span{transform:none}
.row{margin-top:48px;display:grid;grid-template-columns:1fr auto 1fr;align-items:end;gap:32px}
.row h1{font-size:clamp(24px,2.4vw,36px);font-weight:700;letter-spacing:-.025em;line-height:1.15;max-width:18ch}
.row h1 em{font-style:normal;background:#d6ff3f;padding:0 .12em;border-radius:6px}
.row p{color:#5c5d59;max-width:30ch;justify-self:end;text-align:right}
.ink{background:#111;color:#fff}.ink:hover{background:#2a2b2e}
@media(max-width:899px){.h{padding:90px 16px 28px}.row{grid-template-columns:1fr;gap:18px}.row p{justify-self:start;text-align:left}.nm{font-size:15vw}}
''',nav('ink')+f'''<section class="h">
<div class="nm" aria-label="Кирилл"><span class="w"><span>КИР</span></span><span class="p"><img src="img/kirill.webp" alt="Кирилл"></span><span class="w"><span style="transition-delay:.1s">ИЛЛ</span></span></div>
<div class="row"><h1 class="in" style="--d:.5s">Делаю сайты, которые <em>продают</em> с первого экрана</h1>
<a class="btn ink in" style="--d:.65s" href="#">Смотреть работы{ARR}</a>
<p class="in" style="--d:.6s">Мне 18. Лендинги под ключ: дизайн, анимации, версия для телефона и запуск.</p></div></section>''')

# 3. Кино
h3=page('Вариант 3','Onest','''
body{background:#0e0f10;color:#f2f2ee}
.h{position:relative;min-height:100dvh;display:flex;align-items:flex-end;overflow:hidden}
.ph{position:absolute;inset:0 0 0 44%}.ph img{width:100%;height:100%;object-fit:cover;object-position:50% 25%;transform:scale(1.08);transition:transform 2.4s var(--ease)}
.ld .ph img{transform:none}
.ph::after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,#0e0f10 0%,rgba(14,15,16,.5) 22%,rgba(14,15,16,0) 50%),linear-gradient(0deg,rgba(14,15,16,.7),rgba(14,15,16,0) 35%)}
.t{position:relative;padding:0 40px 56px;width:100%}
.k{color:#d4ff3a;font-weight:600}
h1{margin-top:18px;font-size:clamp(46px,6.6vw,108px);font-weight:800;line-height:.94;letter-spacing:-.045em}
h1 .ln{display:block;overflow:hidden;padding-bottom:.04em}h1 .ln span{display:block;transform:translateY(105%);transition:transform 1.2s var(--ease)}
.ld h1 .ln span{transform:none}
p{margin-top:22px;color:#9d9e99;font-size:18px;max-width:36ch}
.acc{background:#d4ff3a;color:#0e0f10}.acc:hover{background:#e2ff78}
.bt{margin-top:28px}
@media(max-width:899px){.ph{inset:0}.ph::after{background:linear-gradient(180deg,rgba(14,15,16,.1),rgba(14,15,16,.2) 35%,#0e0f10 80%)}.t{padding:0 16px 32px}}
''',nav('acc')+f'''<section class="h"><div class="ph"><img src="img/kirill.webp" alt="Кирилл"></div>
<div class="t"><p class="k in" style="--d:.1s;margin:0;color:#d4ff3a">Веб-дизайнер, 18 лет</p>
<h1><span class="ln"><span style="transition-delay:.2s">Сайты,</span></span><span class="ln"><span style="transition-delay:.3s">которые</span></span><span class="ln"><span style="transition-delay:.4s">продают</span></span></h1>
<p class="in" style="--d:.7s">Меня зовут Кирилл. Делаю лендинги под ключ: дизайн, анимации, запуск.</p>
<div class="bt in" style="--d:.8s"><a class="btn acc" href="#">Смотреть работы{ARR}</a></div></div></section>''')

# 4. Работы веером
h4=page('Вариант 4','Geologica','''
body{background:#e9eaee;color:#101114}
.h{min-height:100dvh;display:grid;grid-template-columns:.9fr 1.1fr;align-items:center;gap:40px;padding:90px 40px 40px;overflow:hidden}
.me{display:flex;align-items:center;gap:14px}
.me img{width:64px;height:64px;border-radius:50%;object-fit:cover;object-position:50% 25%}
.me b{display:block;font-size:18px}.me span{color:#5b5e66;font-size:15px}
h1{margin-top:32px;font-size:clamp(40px,4.4vw,70px);font-weight:700;line-height:1.02;letter-spacing:-.04em}
h1 em{font-style:normal;color:#2b4cff}
p{margin-top:20px;color:#5b5e66;font-size:18px;max-width:36ch}
.acc{background:#2b4cff;color:#fff}.acc:hover{background:#1f3de0}.bt{margin-top:28px}
.fan{position:relative;height:min(600px,70vh)}
.fan .win{position:absolute;width:76%;transition:transform 1.1s var(--ease),opacity .8s var(--ease)}
.fan .w0{left:0;top:4%;transform:translate3d(30%,40px,0) rotate(0);opacity:0;z-index:1}
.fan .w1{left:12%;top:24%;transform:translate3d(10%,40px,0);opacity:0;z-index:2;transition-delay:.12s}
.fan .w2{left:24%;top:44%;transform:translate3d(-8%,40px,0);opacity:0;z-index:3;transition-delay:.24s}
.ld .fan .w0{transform:rotate(-6deg);opacity:1}.ld .fan .w1{transform:rotate(-1deg);opacity:1}.ld .fan .w2{transform:rotate(4deg);opacity:1}
.fan:hover .w0{transform:translate3d(-6%,-6%,0) rotate(-9deg)}.fan:hover .w2{transform:translate3d(6%,6%,0) rotate(7deg)}
.tag{position:absolute;z-index:4;right:2%;bottom:2%;padding:12px 18px;border-radius:18px;background:#fff;font-size:15px;font-weight:600;box-shadow:0 20px 40px -20px rgba(16,17,20,.35)}
.tag b{display:block;font-size:26px;letter-spacing:-.03em}
@media(max-width:899px){.h{grid-template-columns:minmax(0,1fr);padding:90px 16px 30px}h1{font-size:34px}.fan{height:300px}.fan .win{width:72%}}
''',nav('acc')+f'''<section class="h"><div>
<div class="me in" style="--d:.05s"><img src="img/kirill.webp" alt="Кирилл"><div><b>Кирилл</b><span>веб-дизайнер, 18 лет</span></div></div>
<h1 class="in" style="--d:.15s">Делаю сайты, которые <em>продают</em> с первого экрана</h1>
<p class="in" style="--d:.3s">Лендинги под ключ: дизайн, анимации, версия для телефона и запуск.</p>
<div class="bt in" style="--d:.45s"><a class="btn acc" href="#">Смотреть работы{ARR}</a></div></div>
<div class="fan">{win('protektor-1','ПРОТЕКТОР','w0')}{win('altitude-1','Altitude','w1')}{win('forte-1','FORTE','w2')}<div class="tag in" style="--d:1s"><b>3 сайта</b>шиномонтаж, авиа, стройка</div></div></section>''')

# 5. Бенто
h5=page('Вариант 5','Geologica','''
body{background:#e9eaee;color:#101114}
.h{min-height:100dvh;display:grid;grid-template-columns:1.2fr .9fr 1fr 1fr;grid-template-rows:1fr 1fr;gap:10px;padding:10px}
.t{border-radius:26px;background:#fbfbfc;overflow:hidden;position:relative;opacity:0;transform:translateY(16px) scale(.985);transition:opacity .8s var(--ease),transform .9s var(--ease);transition-delay:calc(var(--i)*.07s)}
.ld .t{opacity:1;transform:none}
.i{grid-row:1/3;padding:34px;display:flex;flex-direction:column}
.i .lg{display:flex;justify-content:space-between;font-weight:700}.i .lg span{color:#5b5e66;font-weight:500}
.i h1{margin-top:auto;font-size:clamp(32px,3vw,48px);font-weight:700;line-height:1.03;letter-spacing:-.04em}
.i h1 em{font-style:normal;color:#2b4cff}
.i p{margin-top:14px;color:#5b5e66}
.acc{background:#2b4cff;color:#fff;align-self:flex-start;margin-top:24px}
.p{grid-row:1/3}.p img{width:100%;height:100%;object-fit:cover;object-position:50% 25%}
.s{display:flex;flex-direction:column}.s .sh{flex:1;position:relative;overflow:hidden}.s .sh img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:top;transition:transform 1.2s var(--ease)}
.s:hover .sh img{transform:scale(1.05)}
.s .c{display:flex;justify-content:space-between;align-items:center;padding:12px 16px}.s .c b{font-size:17px}.s .c small{display:block;color:#5b5e66;font-size:13px}
.s .c i{width:36px;height:36px;border-radius:50%;background:#e9eaee;display:grid;place-items:center}.s .c svg{width:15px;height:15px;fill:none;stroke:#101114;stroke-width:2.2;stroke-linecap:round;stroke-linejoin:round}
.s0{grid-column:3/5}
@media(max-width:899px){.h{grid-template-columns:1fr 1fr;grid-template-rows:auto}.i,.p{grid-column:1/-1;grid-row:auto}.p{height:420px}.s0{grid-column:1/-1}.s .sh{min-height:150px}}
''',f'''<section class="h"><div class="t i" style="--i:0"><div class="lg">Кирилл<span>Работы</span></div>
<h1>Делаю сайты, которые <em>продают</em> с первого экрана</h1><p>Мне 18. Лендинги под ключ: дизайн, анимации, запуск.</p>
<a class="btn acc" href="#">Написать в Telegram{ARR}</a></div>
<div class="t p" style="--i:1"><img src="img/kirill.webp" alt="Кирилл"></div>'''+''.join(f'<a class="t s s{k}" style="--i:{k+2}" href="#"><div class="sh"><img src="img/{s}.webp" alt="{n}"></div><div class="c"><div><b>{n}</b><small>{c}</small></div><i>{ARR}</i></div></a>' for k,(s,n,c) in enumerate(SITES))+'</section>')

for i,h in enumerate([h1,h2,h3,h4,h5],1):
    open(f'h{i}.html','w').write(h)
print('ok')
