// Общие данные о работах для всех вариантов портфолио
// TODO: ссылка на Telegram Кирилла
window.TG = 'https://t.me/';
window.CASES = [
  {
    id: 'protektor', name: 'ПРОТЕКТОР', niche: 'Шиномонтаж', url: 'https://protektorvercelapp.vercel.app',
    task: 'Чтобы человек записался на шиномонтаж сам, без звонка, и не боялся очереди.',
    idea: 'Главное обещание на первом экране: «Переобуем за 25 минут». Весь сайт его доказывает.',
    done: ['Красная машина и обещание «за 25 минут» на первом экране', 'Прайс без мелкого шрифта', 'Блок «25 минут» по шагам с таймером', 'Запись на точное время в пару нажатий']
  },
  {
    id: 'altitude', name: 'Altitude', niche: 'Авиакомпания', url: 'https://altitude-airlines.vercel.app',
    task: 'Показать, что лететь с этой компанией удобно, а цена честная: без доплат за багаж.',
    idea: 'Ощущение полёта с первой секунды: небо, облака и самолёт на первом экране.',
    done: ['Заставка: посадочный талон и вход в облака', 'Классы: от эконома до частного джета', 'История компании по годам', 'Гарантии: багаж включён, цена фиксируется']
  },
  {
    id: 'forte', name: 'FORTE', niche: 'Строительство домов', url: 'https://forte-stroy.vercel.app',
    task: 'Снять главный страх заказчика: что цена дома вырастет уже во время стройки.',
    idea: 'Сделать цену и процесс прозрачными: всё можно посчитать и проверить на сайте.',
    done: ['Надпись FORTE уходит за крышу дома', 'Конфигуратор: собираешь дом и видишь цену', 'Один прораб от фундамента до ключей', 'Отзывы с фото построенных домов']
  }
];
window.STEPS = [
  ['ti-search', 'Разбор', 'Изучаю нишу, конкурентов и десятки сайтов-референсов.'],
  ['ti-bulb', 'Идея', 'Нахожу главное обещание сайта и порядок блоков.'],
  ['ti-pencil', 'Дизайн', 'Показываю 2-3 варианта на выбор до сборки.'],
  ['ti-code', 'Сборка', 'Вёрстка, анимации, версия для телефона.'],
  ['ti-rocket', 'Запуск', 'Публикую сайт и помогаю подключить домен.']
];
window.onReady = function (fn) { if (document.readyState !== 'loading') fn(); else document.addEventListener('DOMContentLoaded', fn); };
window.revealAll = function () {
  document.querySelectorAll('.js-tg').forEach(function (a) { a.href = TG; a.target = '_blank'; a.rel = 'noopener'; });
  requestAnimationFrame(function () { document.body.classList.add('ld'); });
  if (!('IntersectionObserver' in window)) { document.querySelectorAll('.rv').forEach(function (e) { e.classList.add('in'); }); return; }
  var io = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } }); }, { rootMargin: '0px 0px -6% 0px' });
  document.querySelectorAll('.rv').forEach(function (e) { io.observe(e); });
};
// экраны телефона в мокапе сменяются сами
window.autoSlides = function (root, ms) {
  root.querySelectorAll('[data-slides]').forEach(function (box) {
    var imgs = box.querySelectorAll('img'), i = 0;
    if (imgs.length < 2 || matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    setInterval(function () { imgs[i].classList.remove('on'); i = (i + 1) % imgs.length; imgs[i].classList.add('on'); }, ms || 2600);
  });
};
