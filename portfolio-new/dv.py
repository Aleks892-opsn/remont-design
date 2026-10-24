# Демо: три варианта компьютерной раскладки блоков (телефон не меняется)
import gen, av

D = {}

# 1. Крупно: большие фото и окна сайтов, разбор под окном в три колонки, шаги в ряд
D['d1'] = ('Крупно', '''
@media(min-width:900px){
 .hero .w{grid-template-columns:1.15fr .85fr;gap:72px}
 .hero__lead{font-size:clamp(48px,4.8vw,80px);line-height:1.02;max-width:12ch}
 .hero__b{margin-top:36px}
 .hero__b .btn{height:64px;padding:0 34px;font-size:17px}
 .cover{max-height:86svh}
 .about .w{gap:80px}
 .abc__h{font-size:clamp(48px,5vw,84px)!important}
 .case__in{padding:110px 0 60px}
 .case .w{grid-template-columns:1fr;grid-template-areas:"top" "win" "info";row-gap:56px}
 .case__head{display:grid;grid-template-columns:1fr auto;align-items:end;column-gap:40px;row-gap:14px}
 .case__top{grid-column:1/-1}
 .case__n{font-size:clamp(44px,4vw,64px)}
 .case__pitch{margin:0 0 10px;font-size:20px;color:var(--mute)}
 .case__shot{display:grid;grid-template-columns:1fr;width:min(1040px,calc((100svh - 420px) * 1.6));justify-self:center}
 .case__win{border-radius:18px}
 .case__go{justify-self:center;margin-top:34px;width:auto}
 .case__info{grid-template-columns:1fr 1fr;gap:16px;max-width:1040px;width:100%;justify-self:center;margin-top:10px}
 .case__info>div{position:relative;overflow:hidden;padding:32px 34px;border-radius:26px}
 .case__info>div:nth-child(1){background:linear-gradient(140deg,#ff3434,#b80f17);color:#fff;box-shadow:0 30px 60px -30px rgba(255,43,43,.6)}
 .case__info>div:nth-child(1)::after{content:"";position:absolute;right:-60px;top:-60px;width:200px;height:200px;border-radius:50%;border:30px solid rgba(255,255,255,.1)}
 .case__info>div:nth-child(1) h3{color:#fff}
 .case__info>div:nth-child(1) h3::before{background:#fff}
 .case__info>div:nth-child(1) p{color:#fff}
 .case__info>div:nth-child(2){background:#140c0d;border:1px solid rgba(255,43,43,.45)}
 .case__info>div:nth-child(2)::after{content:"";position:absolute;left:0;top:28px;bottom:28px;width:4px;border-radius:0 4px 4px 0;background:var(--acc)}
 .case__info>div:nth-child(3){grid-column:1/-1;background:radial-gradient(80% 140% at 100% 0%,rgba(255,43,43,.28),transparent 60%),#121012;border:1px solid var(--line)}
 .case__info h3{display:inline-flex;align-items:center;gap:10px;font-size:13px}
 .case__info h3::before{content:"";width:22px;height:2px;background:var(--acc)}
 .case__info p{margin-top:14px;font-size:18px;line-height:1.55;color:var(--t)}
 .case__info ul{display:flex;flex-wrap:wrap;gap:12px;margin-top:20px;counter-reset:dn}
 .case__info li{counter-increment:dn;display:inline-flex;align-items:center;gap:12px;padding:12px 22px 12px 12px;border-radius:999px;background:var(--acc);color:#fff;font-size:16px;font-weight:500;box-shadow:0 14px 30px -16px rgba(255,43,43,.8);transition:transform .35s cubic-bezier(.16,1,.3,1)}
 .case__info li:hover{transform:translateY(-3px)}
 .case__info li::before{content:counter(dn);position:static;width:30px;height:30px;margin:0;border-radius:50%;background:#fff;color:var(--acc);display:grid;place-items:center;font:700 14px var(--fh);box-shadow:none}
 .case__info>.case__go{display:none}
 .how__g{grid-template-columns:1fr!important;gap:50px!important}
 .how__l{position:static!important;display:flex;justify-content:space-between;align-items:end;gap:40px}
 .how__list{display:grid;grid-template-columns:repeat(5,1fr);gap:24px}
 .how__line{left:28px;right:28px;top:27px;bottom:auto;width:auto;height:2px}
 .how__line i{transform-origin:0 50%;transform:scaleX(0)}
 .step{grid-template-columns:1fr;gap:20px;padding:0}
 .step h3{padding-top:0}
}

@media(max-width:899px){
 .case__info{gap:10px}
 .case__info>div{position:relative;overflow:hidden;padding:24px 22px;border-radius:22px}
 .case__info>div:nth-child(1){background:linear-gradient(140deg,#ff3434,#b80f17);color:#fff;box-shadow:0 30px 60px -30px rgba(255,43,43,.6)}
 .case__info>div:nth-child(1)::after{content:"";position:absolute;right:-70px;top:-70px;width:180px;height:180px;border-radius:50%;border:30px solid rgba(255,255,255,.1)}
 .case__info>div:nth-child(1) h3{color:#fff}
 .case__info>div:nth-child(1) h3::before{background:#fff}
 .case__info>div:nth-child(1) p{color:#fff}
 .case__info>div:nth-child(2){background:#140c0d;border:1px solid rgba(255,43,43,.45)}
 .case__info>div:nth-child(2)::after{content:"";position:absolute;left:0;top:28px;bottom:28px;width:4px;border-radius:0 4px 4px 0;background:var(--acc)}
 .case__info>div:nth-child(3){background:radial-gradient(80% 140% at 100% 0%,rgba(255,43,43,.28),transparent 60%),#121012;border:1px solid var(--line)}
 .case__info h3{display:inline-flex;align-items:center;gap:10px;font-size:13px}
 .case__info h3::before{content:"";width:22px;height:2px;background:var(--acc)}
 .case__info p{margin-top:14px;font-size:16px;line-height:1.5;color:var(--t)}
 .case__info ul{display:flex;flex-wrap:wrap;gap:8px;margin-top:16px;counter-reset:dn}
 .case__info li{counter-increment:dn;display:inline-flex;align-items:center;gap:12px;padding:10px 16px 10px 10px;border-radius:999px;background:var(--acc);color:#fff;font-size:14.5px;font-weight:500;line-height:1.3;box-shadow:0 14px 30px -16px rgba(255,43,43,.8);transition:transform .35s cubic-bezier(.16,1,.3,1)}
 .case__info li:hover{transform:translateY(-3px)}
 .case__info li::before{content:counter(dn);position:static;width:26px;height:26px;flex:none;margin:0;border-radius:50%;background:#fff;color:var(--acc);display:grid;place-items:center;font:700 14px var(--fh);box-shadow:none}
 .case__info li:hover{transform:none}
}
''', '''
if (window.gsap && matchMedia('(min-width: 900px)').matches) { gsap.killTweensOf('.how__line i'); gsap.fromTo('.how__line i', { scaleX: 0, scaleY: 1 }, { scaleX: 1, ease: 'none', scrollTrigger: { trigger: '.how__list', start: 'top 75%', end: 'bottom 40%', scrub: 1 } }); }
''')

# 2. Сцена: имя за фото во всю ширину, разбор слева закреплён, окно сайта справа крупно, шаги карточками
D['d2'] = ('Сцена', '''
@media(min-width:900px){
 .hero{padding:90px 0 40px}
 .hero .w{grid-template-columns:1fr;justify-items:center;text-align:center;position:relative}
 .cover{border:0;background:none;overflow:visible;max-height:none;aspect-ratio:auto;width:min(460px,34vw);justify-self:center;order:1}
 .hero__photo{border-radius:var(--r);height:auto!important}
 .hero__photo img{width:100%!important;height:auto!important}
 .cover__mast{position:absolute;left:50%;top:auto;bottom:18%;width:100vw;transform:translateX(-50%);padding:0;text-align:center;z-index:-1}
 .hero__name{font-size:min(23vw,330px)!important;color:var(--acc);text-shadow:none;opacity:.95}
 .cover__no{right:-120px;bottom:20px;color:var(--mute)}
 .hero__txt{order:2;display:flex;flex-direction:column;align-items:center;margin-top:26px}
 .hero__lead{font-size:clamp(34px,3vw,48px);max-width:none}
 .hero__b{justify-content:center}
 .case .w{grid-template-columns:.75fr 1.25fr;grid-template-areas:"top win" "info win";align-items:start;column-gap:64px}
 .case__in{justify-content:center}
 .case__shot{align-self:center}
 .case__win{border-radius:16px;transform:perspective(1600px) rotateY(-6deg);transform-origin:0 50%}
 .case__n{font-size:clamp(56px,6vw,100px)}
 .case__info{gap:22px}
 .case__info p,.case__info li{font-size:16px}
 .how__list{display:grid;grid-template-columns:1fr 1fr;gap:14px}
 .how__line{display:none}
 .step{grid-template-columns:1fr;padding:28px;border-radius:var(--r);background:var(--card);border:1px solid var(--line);min-height:210px;align-content:space-between}
 .step:first-of-type{grid-column:1/-1;background:var(--acc);border-color:var(--acc)}
 .step:first-of-type b{background:#fff;border-color:#fff;color:var(--acc)}
 .step:first-of-type p{color:rgba(255,255,255,.85)}
 .step.on{border-color:color-mix(in srgb,var(--acc) 60%,var(--line))}
}
''', '')

# 3. Редакция: три колонки на первом экране, огромные номера работ, шаги строками во всю ширину
D['d3'] = ('Редакция', '''
@media(min-width:900px){
 .hero .w{grid-template-columns:1fr minmax(0,440px) 1fr;gap:48px;align-items:end}
 .hero__txt{order:0;align-self:end}
 .hero__lead{font-size:clamp(34px,3vw,50px)}
 .cover{order:1;justify-self:center;max-height:80svh}
 .hero .w::after{content:"Веб-дизайнер, 18 лет. Делаю лендинги под ключ: дизайн, анимации, версия для телефона и запуск. Беру новые проекты.";order:2;align-self:end;font-size:17px;line-height:1.6;color:var(--mute);border-top:1px solid var(--line);padding-top:18px}
 .case .w{grid-template-columns:1.3fr .7fr;grid-template-areas:"top top" "win info";column-gap:56px;align-items:center}
 .case__head{position:relative!important;padding-left:clamp(170px,15vw,250px)!important}
 .case__top{position:static!important}
 .case__top{position:relative!important}
 .case__no{position:absolute;left:calc(-1 * clamp(170px,15vw,250px));top:0;font-size:clamp(130px,14vw,230px);line-height:.8;color:transparent;-webkit-text-stroke:2px var(--acc)}
 .case__top{padding-top:6px}
 .case__bar,.case__top .tag{display:none}
 .case__info{border-left:1px solid var(--line);padding-left:32px;gap:24px}
 .how__g{grid-template-columns:1fr!important}
 .how__l{position:static!important}
 .how__line{display:none}
 .how__list{border-top:1px solid var(--line)}
 .step{grid-template-columns:140px 1fr 1.2fr;align-items:center;gap:30px;padding:26px 0;border-bottom:1px solid var(--line)}
 .step b{width:auto;height:auto;border:0;background:none!important;font-size:64px;color:var(--line);border-radius:0;transform:none!important;justify-content:start}
 .step.on b{color:var(--acc)}
 .step>div{display:contents}
 .step h3{padding:0;font-size:36px}
 .step p{margin:0;font-size:17px}
}
''', '''
if (matchMedia('(min-width: 900px)').matches) document.querySelectorAll('.case__no').forEach(function (n) { n.textContent = n.textContent.trim().slice(0, 2); });
''')

if __name__ == '__main__':
    for k, (name, css, js) in D.items():
        a = dict(av.AB['a3'])
        a['css'] = a['css'] + css
        a['js'] = a['js'] + js
        open(f'{k}.html', 'w').write(gen.page('v1', gen.THEMES['v1'], about=a))
    print('ok')
