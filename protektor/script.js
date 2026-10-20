// ПРОТЕКТОР: загрузка, качение колеса от прокрутки, таймер визита, плашки, запись на время
(function () {
  'use strict';

  var motion = document.documentElement.classList.contains('motion');
  var $ = function (id) { return document.getElementById(id); };
  var pad = function (n) { return String(n).padStart(2, '0'); };
  var clamp = function (v, a, b) { return Math.min(b, Math.max(a, v)); };
  // Телефонная раскладка (≤640px): свой первый экран, гармошка услуг, лента времени, запись и меню-шторка
  var phoneMQ = matchMedia('(max-width: 640px)');
  var isPhone = function () { return phoneMQ.matches; };

  /* ---------- Открыто ли сейчас (8:00–22:00 каждый день) ---------- */
  var setOpen = function () {
    var h = new Date().getHours();
    var open = h >= 8 && h < 22;
    var text = open ? 'Сейчас открыто, до 22:00' : 'Сейчас закрыто, откроемся в 8:00';
    ['open-dot', 'open-dot-2', 'open-dot-3', 'open-dot-4'].forEach(function (id) { $(id).classList.toggle('is-open', open); });
    $('open-text').textContent = open ? 'Открыто до 22:00, без выходных' : 'Закрыто, откроемся в 8:00';
    $('open-text-2').textContent = text;
    $('open-text-3').textContent = open ? 'Открыто до 22:00' : 'Откроемся в 8:00';
  };
  setOpen();
  setInterval(setOpen, 60000);
  $('year').textContent = new Date().getFullYear();

  /* ---------- Загрузка: счётчик до 100, экран уезжает, колесо въезжает ---------- */
  var hero = document.querySelector('.hero');
  var phoneHero = null; // заполняется ниже
  var startHero = function () {
    hero.classList.add('is-in');
    if (phoneHero) phoneHero.start();
  };
  if (motion) {
    var count = $('loader-count');
    var bar = $('loader-bar');
    var t0 = performance.now();
    var DURATION = 1500;
    var fontsReady = document.fonts ? document.fonts.ready : Promise.resolve();
    var finished = false;
    var finish = function () {
      if (finished) return;
      finished = true;
      $('loader').classList.add('is-done');
      setTimeout(startHero, 350);
      setTimeout(function () { $('loader').remove(); }, 1200);
    };
    var tick = function (now) {
      var p = Math.min(1, (now - t0) / DURATION);
      var eased = 1 - Math.pow(1 - p, 2);
      count.textContent = p >= 1 ? '100' : pad(Math.floor(eased * 100));
      bar.style.width = (eased * 100) + '%';
      if (p < 1) requestAnimationFrame(tick);
      else fontsReady.then(function () { setTimeout(finish, 180); });
    };
    requestAnimationFrame(tick);
    setTimeout(finish, 4000); // страховка, если что-то зависло
  } else {
    startHero();
  }

  /* ---------- Прокрутка: шапка, вращение колёс, лента протектора, таймер ---------- */
  var header = $('header');
  var heroWheel = $('hero-wheel');
  var bigWheel = document.querySelector('.wheel__art');
  var belt = document.querySelector('[data-belt]');
  // На телефоне лент несколько — между всеми блоками; едут все вместе
  var belts = document.querySelectorAll('[data-belt]');
  // На телефоне лента едет медленно и догоняет прокрутку плавно, а не рывками
  var beltNow = 0, beltTo = 0, beltRaf = 0;
  var beltStep = function () {
    beltNow += (beltTo - beltNow) * 0.12;
    if (Math.abs(beltTo - beltNow) < 0.1) beltNow = beltTo;
    var v = (beltNow % 840).toFixed(2) + 'px';
    for (var i = 0; i < belts.length; i++) belts[i].style.setProperty('--belt', v);
    beltRaf = beltNow === beltTo ? 0 : requestAnimationFrame(beltStep);
  };
  var moveBelt = function (y) {
    beltTo = -y * 0.2;
    if (!beltRaf) beltRaf = requestAnimationFrame(beltStep);
  };
  var visit = $('visit');
  var timer = $('visit-timer');
  var rail = $('visit-rail');
  var railWheel = $('visit-wh');
  var steps = Array.prototype.slice.call(document.querySelectorAll('#visit-steps li'));
  // Колесо 1080px в диаметре: при прокрутке на X пикселей «проезжает» X — поворот X / (π·d) оборотов
  var degPerPx = 360 / (Math.PI * 1080);

  // На телефоне колесо — готовые картинки-слои: крутим их через transform (это делает видеокарта, без перерисовки SVG)
  var setRot = function (wrap, deg) {
    if (!wrap) return;
    if (isPhone()) {
      var imgs = wrap.querySelectorAll('.mwheel__rot');
      for (var i = 0; i < imgs.length; i++) imgs[i].style.transform = 'rotate(' + deg + 'deg)';
      return;
    }
    wrap.querySelectorAll('.tire-rot').forEach(function (g) { g.style.setProperty('--rot', deg + 'deg'); });
  };

  var ticking = false;
  var phoneJobs = []; // обработчики прокрутки телефонных блоков (добавляются ниже)
  var deskJobs = [];  // то же для компьютера — для блоков, которые устроены одинаково
  var wideVisit = matchMedia('(min-width: 1081px)'); // на широком экране «25 минут» — вертикальная лента, как на телефоне
  var onScroll = function () {
    ticking = false;
    var y = window.scrollY;
    header.classList.toggle('is-solid', y > 40);
    // Лента протектора едет при прокрутке — и на компьютере, и на телефоне
    if (belt && motion) moveBelt(y);
    if (isPhone()) {
      // Сначала все замеры, потом все записи — чтобы не дёргать раскладку на каждом кадре
      var writes = phoneJobs.map(function (job) { return job(y); });
      writes.forEach(function (w) { if (w) w(); });
      return;
    }
    var dw = deskJobs.map(function (job) { return job(y); });
    dw.forEach(function (w) { if (w) w(); });
    if (!motion) return;

    setRot(heroWheel, y * degPerPx * 2.2);

    if (bigWheel) {
      var r = bigWheel.getBoundingClientRect();
      setRot(bigWheel, (innerHeight - r.top) * 0.18);
    }

    // Закреплённый блок визита (планшет): прогресс от 0 до 1 → таймер 00:00…25:00 и шаги по очереди
    if (wideVisit.matches) return;
    var vr = visit.getBoundingClientRect();
    var total = visit.offsetHeight - innerHeight;
    var p = Math.min(1, Math.max(0, -vr.top / total));
    var secs = Math.round(p * 25 * 60);
    timer.textContent = pad(Math.floor(secs / 60)) + ':' + pad(secs % 60);
    rail.style.width = (p * 100) + '%';
    // колёсико катится по ленте: поворот ровно на пройденный путь
    if (railWheel) railWheel.style.transform = 'rotate(' + (rail.parentNode.offsetWidth * p / (Math.PI * 44) * 360).toFixed(1) + 'deg)';
    var on = Math.min(steps.length, Math.floor(p * steps.length + 0.35));
    steps.forEach(function (li, i) { li.classList.toggle('is-on', i < on); });
    steps.forEach(function (li, i) { li.classList.toggle('is-now', i === Math.max(0, on - 1)); });
  };
  var requestScroll = function () {
    if (!ticking) { ticking = true; requestAnimationFrame(onScroll); }
  };
  window.addEventListener('scroll', requestScroll, { passive: true });
  onScroll();

  /* ---------- Активный пункт меню ---------- */
  var navLinks = Array.prototype.slice.call(document.querySelectorAll('.header__nav a'));
  if ('IntersectionObserver' in window) {
    var spy = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        navLinks.forEach(function (a) { a.classList.toggle('is-active', a.getAttribute('href') === '#' + e.target.id); });
      });
    }, { rootMargin: '-45% 0px -50% 0px' });
    navLinks.forEach(function (a) { var s = document.querySelector(a.getAttribute('href')); if (s) spy.observe(s); });

    // Плашки вокруг колеса появляются по очереди, один раз
    var tags = $('wheel-tags');
    var tagIO = new IntersectionObserver(function (entries) {
      if (!entries[0].isIntersecting) return;
      Array.prototype.forEach.call(tags.children, function (li, i) { li.style.transitionDelay = (i * 110) + 'ms'; });
      tags.classList.add('is-in');
      tagIO.disconnect();
    }, { threshold: 0.3 });
    tagIO.observe(tags);
  } else {
    $('wheel-tags').classList.add('is-in');
  }

  /* ---------- Футер под страницей: отступ снизу равен его высоте ---------- */
  var footer = $('footer');
  var main = $('main');
  // Слово «ПРОТЕКТОР» в футере подгоняем ровно под ширину строки
  var word = document.querySelector('.footer__word');
  var fitWord = function () {
    word.style.fontSize = '200px';
    var cs = getComputedStyle(word.parentElement);
    var avail = word.parentElement.clientWidth - parseFloat(cs.paddingLeft) - parseFloat(cs.paddingRight);
    word.style.fontSize = Math.floor(200 * avail / word.scrollWidth) + 'px';
  };
  // Подгоняем только при смене ширины: на телефоне resize прилетает и от панели браузера —
  // пересчёт шрифта по каждому такому событию мог раскачивать раскладку
  var footerW = 0;
  var sizeFooter = function (force) {
    if (force === true || innerWidth !== footerW) { footerW = innerWidth; fitWord(); }
    var h = footer.offsetHeight + 'px';
    if (main.style.getPropertyValue('--footer-h') !== h) main.style.setProperty('--footer-h', h);
  };
  sizeFooter(true);
  window.addEventListener('resize', sizeFooter);
  if (document.fonts) document.fonts.ready.then(function () { sizeFooter(true); });


  /* ---------- Цены ----------
     Суммы в рублях — средние по рынку, сверьте со своими. Для услуг с byRadius — по одной сумме на каждый размер.
     Если поставить null, на сайте покажется «[цена]».
     photo — фон карточки на телефоне: файл assets/prices/<photo>.webp (16:9, серый). Нет файла — в углу просто колесо. */
  var RADII = ['R13', 'R14', 'R15', 'R16', 'R17', 'R18', 'R19', 'R20', 'R21', 'R22'];
  var PRICES = [
    { what: 'Переобувка', name: 'Шиномонтаж комплекта', note: 'снять, перебортовать, отбалансировать, поставить', photo: 'montazh', byRadius: { R13: 2000, R14: 2200, R15: 2400, R16: 2800, R17: 3200, R18: 3600, R19: 4200, R20: 4800, R21: 5400, R22: 6000 } },
    { what: 'Балансировка', name: 'Балансировка четырёх колёс', note: 'на станке', photo: 'balans', byRadius: { R13: 800, R14: 900, R15: 1000, R16: 1100, R17: 1300, R18: 1500, R19: 1700, R20: 1900, R21: 2100, R22: 2400 } },
    { what: 'Балансировка', name: 'Финишная балансировка', note: 'на автомобиле, если бьёт руль', price: 2000, photo: 'finish' },
    { what: 'Ремонт прокола', name: 'Ремонт прокола', note: 'за колесо, гарантия 12 месяцев', price: 600, photo: 'prokol' },
    { what: 'Ремонт прокола', name: 'Ремонт бокового пореза', note: 'после осмотра', price: 1500, photo: 'porez', from: true },
    { what: 'Правка дисков', name: 'Правка литого диска', note: 'за диск', price: 1500, photo: 'disk', from: true },
    { what: 'Хранение шин', name: 'Сезонное хранение', note: 'за комплект', price: 3500, photo: 'hranenie', key: 'storage' },
    { what: 'Переобувка', mobile: true, name: 'Выезд к клиенту', note: 'по Москве', price: 3000, photo: 'vyezd', from: true },
    { what: 'Переобувка', name: 'Азот в шины', note: 'для всех клиентов', free: true, photo: 'azot' }
  ];
  var rub = function (n) { return n.toLocaleString('ru-RU') + ' ₽'; };
  var priceText = function (item, radius) {
    if (item.free) return { text: 'Бесплатно', tbd: false };
    var v = item.byRadius ? item.byRadius[radius] : item.price;
    if (v == null) return { text: '[цена]', tbd: true };
    return { text: (item.from ? 'от ' : '') + rub(v), tbd: false };
  };
  var priceRadius = 'R16';
  var renderPrices = function () {
    $('price-table').innerHTML = PRICES.map(function (item) {
      var p = priceText(item, priceRadius);
      // Стрелка-кнопка видна только на телефоне: ведёт к записи и сразу отмечает услугу
      return '<div class="price-row">' + (item.photo ? '<i class="price-row__ph" style="background-image:url(assets/prices/' + item.photo + '.webp)" aria-hidden="true"></i>' : '') + '<b>' + item.name + '<small>' + item.note + '</small></b><span class="' + (p.tbd ? 'is-tbd' : '') + '">' + p.text + '</span>' +
        '<a class="price-row__go" href="#book" data-mbook-what="' + item.what + '"' + (item.mobile ? ' data-mobile-service' : '') + ' aria-label="Записаться: ' + item.name + '"></a></div>';
    }).join('');
    $('price-foot').textContent = 'Цены для дисков ' + priceRadius + '. Точную сумму за ремонт и правку назовём после осмотра.';
    document.querySelectorAll('[data-price]').forEach(function (el) {
      var item = PRICES.filter(function (x) { return x.key === el.dataset.price; })[0];
      if (item) el.textContent = priceText(item, priceRadius).text;
    });
  };

  /* ---------- Сезонная подсказка: по месяцу ---------- */
  var SEASON = [
    { months: [2, 3], tag: 'Весна', text: 'Пора на летнюю, когда днём стабильно +5…+7 °C и ночью уже без заморозков. В апреле очереди — запишитесь заранее.' },
    { months: [4, 5, 6, 7], tag: 'Лето', text: 'Сезон спокойный: хорошее время проверить балансировку, выправить диски после зимних ям и сдать зимнюю резину на хранение.' },
    { months: [8, 9, 10], tag: 'Осень', text: 'Пора на зимнюю, когда ночью около нуля. Первый снег — самые длинные очереди, лучше записаться заранее.' },
    { months: [11, 0, 1], tag: 'Зима', text: 'Поймали яму или прокол — приезжайте: ремонтируем проколы с гарантией 12 месяцев и правим литые диски.' }
  ];
  var nowMonth = new Date().getMonth();
  var season = SEASON.filter(function (x) { return x.months.indexOf(nowMonth) >= 0; })[0];
  $('season-tag').textContent = season.tag;
  $('season-text').textContent = season.text;

  /* ---------- Запись на время ---------- */
  var DAYS = ['вс', 'пн', 'вт', 'ср', 'чт', 'пт', 'сб'];
  var MONTHS = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря'];
  var state = { day: null, time: null, radius: 'R16' };

  // Пример занятости: детерминированно по дню и времени, чтобы сетка выглядела живой
  var busy = function (date, h, m) {
    var seed = date.getDate() * 31 + h * 7 + m;
    return (seed * 9301 + 49297) % 233280 / 233280 < 0.28;
  };

  var radioGroup = function (container, items, onPick) {
    container.innerHTML = '';
    items.forEach(function (it) {
      var b = document.createElement('button');
      b.type = 'button';
      b.className = it.cls;
      b.setAttribute('role', 'radio');
      b.setAttribute('aria-checked', String(!!it.checked));
      b.tabIndex = it.checked ? 0 : -1;
      b.innerHTML = it.html;
      if (it.disabled) { b.disabled = true; b.setAttribute('aria-label', it.label + ', занято'); }
      else if (it.label) b.setAttribute('aria-label', it.label);
      b.addEventListener('click', function () {
        container.querySelectorAll('[role="radio"]').forEach(function (x) { x.setAttribute('aria-checked', 'false'); x.tabIndex = -1; });
        b.setAttribute('aria-checked', 'true');
        b.tabIndex = 0;
        onPick(it.value);
      });
      container.appendChild(b);
    });
    // Стрелки переключают выбор внутри группы
    container.onkeydown = function (e) {
      if (['ArrowRight', 'ArrowLeft', 'ArrowDown', 'ArrowUp'].indexOf(e.key) < 0) return;
      var list = Array.prototype.filter.call(container.querySelectorAll('[role="radio"]'), function (x) { return !x.disabled; });
      var i = list.indexOf(document.activeElement);
      var next = list[(i + (e.key === 'ArrowRight' || e.key === 'ArrowDown' ? 1 : -1) + list.length) % list.length];
      if (next) { next.focus(); next.click(); }
      e.preventDefault();
    };
  };

  var today = new Date();
  today.setHours(0, 0, 0, 0);
  var dayList = [];
  for (var d = 0; d < 7; d++) {
    var dt = new Date(today);
    dt.setDate(today.getDate() + d);
    dayList.push(dt);
  }

  var renderSlots = function () {
    var date = state.day;
    var now = new Date();
    var items = [];
    for (var h = 8; h < 22; h++) {
      for (var m = 0; m < 60; m += 30) {
        var label = h + ':' + pad(m);
        var slot = new Date(date);
        slot.setHours(h, m);
        var past = slot <= now;
        items.push({ cls: 'slot', html: label, value: label, label: label, disabled: past || busy(date, h, m), checked: label === state.time });
      }
    }
    if (state.time && items.some(function (x) { return x.value === state.time && x.disabled; })) state.time = null;
    radioGroup($('slots'), items, function (v) { state.time = v; state.custom = true; summary(); });
  };

  // Сразу предлагаем ближайшее свободное окно (на компьютере оно крупно в красной плашке)
  state.day = dayList[0];
  (function () {
    var now = new Date();
    for (var i = 0; i < dayList.length; i++) for (var h = 8; h < 22; h++) for (var m = 0; m < 60; m += 30) {
      var slot = new Date(dayList[i]);
      slot.setHours(h, m);
      if (slot > now && !busy(dayList[i], h, m)) { state.day = dayList[i]; state.time = h + ':' + pad(m); return; }
    }
  })();
  radioGroup($('days'), dayList.map(function (dt, i) {
    return {
      cls: 'day',
      html: '<span>' + (i === 0 ? 'сегодня' : i === 1 ? 'завтра' : DAYS[dt.getDay()]) + '</span><b>' + dt.getDate() + '</b>',
      label: dt.getDate() + ' ' + MONTHS[dt.getMonth()],
      value: dt,
      checked: dt === state.day
    };
  }), function (v) { state.day = v; renderSlots(); summary(); });
  renderSlots();

  radioGroup($('radius'), ['R13', 'R14', 'R15', 'R16', 'R17', 'R18', 'R19', 'R20', 'R21', 'R22'].map(function (r) {
    return { cls: 'radius', html: r, value: r, label: 'Диски ' + r, checked: r === state.radius };
  }), function (v) { state.radius = v; summary(); });

  var mobile = $('mobile');
  mobile.addEventListener('change', function () {
    $('address-field').hidden = !mobile.checked;
    summary();
  });
  document.querySelectorAll('[data-mobile-service]').forEach(function (a) {
    a.addEventListener('click', function () { mobile.checked = true; $('address-field').hidden = false; summary(); });
  });
  $('what').addEventListener('change', function () { summary(); });

  var whatList = function () {
    return Array.prototype.map.call(document.querySelectorAll('#what input:checked'), function (x) { return x.value.toLowerCase(); });
  };
  var whenFor = function (day, time) {
    if (!time) return '';
    var i = dayList.indexOf(day);
    var dayName = i === 0 ? 'сегодня' : i === 1 ? 'завтра' : DAYS[day.getDay()] + ', ' + day.getDate() + ' ' + MONTHS[day.getMonth()];
    return dayName + ' в ' + time;
  };
  var whenText = function () { return whenFor(state.day, state.time); };
  var summary = function () {
    var w = whatList();
    var parts = [];
    parts.push(state.time ? 'Ждём вас ' + whenText() : 'Выберите время слева');
    parts.push((w.length ? w.join(', ') : 'услуга не выбрана') + ', диски ' + state.radius);
    if (mobile.checked) parts.push('с выездом к вам');
    $('summary').textContent = parts.join('. ') + '.';
    $('send').textContent = state.time ? 'Записаться на ' + state.time : 'Записаться';
    // Красная плашка на компьютере
    var di = dayList.indexOf(state.day);
    $('bnow-kick').textContent = state.custom ? 'Ваше время' : 'Ближайшее свободное';
    $('bnow-time').textContent = state.time || '—';
    $('bnow-day').textContent = (di === 0 ? 'Сегодня' : di === 1 ? 'Завтра' : DAYS[state.day.getDay()]) + ', ' + state.day.getDate() + ' ' + MONTHS[state.day.getMonth()];
    $('bnow-what').textContent = (w.length ? w.join(', ') : 'услуга не выбрана') + ' · ' + state.radius + (mobile.checked ? ' · выезд к вам' : '');
  };
  summary();

  // Телефон: +7 (XXX) XXX-XX-XX
  var maskPhone = function (inp) {
    inp.addEventListener('input', function () {
      var d = inp.value.replace(/\D/g, '');
      if (d[0] === '7' || d[0] === '8') d = d.slice(1);
      d = d.slice(0, 10);
      var out = '+7';
      if (d.length) out += ' (' + d.slice(0, 3);
      if (d.length >= 3) out += ') ' + d.slice(3, 6);
      if (d.length >= 6) out += '-' + d.slice(6, 8);
      if (d.length >= 8) out += '-' + d.slice(8, 10);
      inp.value = d.length ? out : '';
    });
  };
  var phone = $('phone');
  maskPhone(phone);

  $('book-form').addEventListener('submit', function (e) {
    e.preventDefault();
    var err = '';
    var bad = null;
    ['name', 'phone', 'address'].forEach(function (id) { $(id).classList.remove('is-bad'); });
    if (!state.time) err = 'Выберите время — свободные окна подсвечены.';
    else if (!whatList().length) err = 'Отметьте, что нужно сделать.';
    else if (mobile.checked && $('address').value.trim().length < 5) { err = 'Укажите адрес, куда приехать.'; bad = $('address'); }
    else if ($('name').value.trim().length < 2) { err = 'Напишите, как к вам обращаться.'; bad = $('name'); }
    else if (phone.value.replace(/\D/g, '').length !== 11) { err = 'Проверьте телефон: нужно 10 цифр после +7.'; bad = phone; }
    else if (!$('consent').checked) err = 'Отметьте согласие на обработку данных.';
    $('book-error').textContent = err;
    if (bad) { bad.classList.add('is-bad'); bad.focus(); }
    if (err) return;

    // TODO: отправить заявку (Telegram-бот, CRM или почта)
    $('book-done-text').textContent = $('name').value.trim() + ', ждём вас ' + whenText() + '. ' +
      (mobile.checked ? 'Мастер приедет по адресу: ' + $('address').value.trim() + '. ' : '') +
      'Если планы поменяются — позвоните, перенесём.';
    showDone();
  });
  var showDone = function () {
    $('book-form').hidden = true;
    $('mbook').hidden = true;
    $('mbook-voice').hidden = true;
    $('book-done').hidden = false;
    $('book-done').focus();
  };
  radioGroup($('price-radius'), RADII.map(function (r) {
    return { cls: 'radius', html: r, value: r, label: 'Цены для дисков ' + r, checked: r === priceRadius };
  }), function (v) { priceRadius = v; renderPrices(); });
  renderPrices();

  $('book-again').addEventListener('click', function () {
    $('book-done').hidden = true;
    $('book-form').hidden = false;
    $('mbook').hidden = false;
    $('mbook-voice').hidden = false;
    renderSlots();
    mbook.refresh();
  });

  /* =====================================================================
     ТЕЛЕФОН (≤640px). На планшете и компьютере эти блоки скрыты стилями.
     ===================================================================== */

  /* ---------- Запись: ближайшее свободное время ----------
     Та же логика, что в большой форме: те же окна по 30 минут, та же занятость busy(),
     те же проверки и тот же экран «Записали». */
  var mbook = (function () {
    var form = $('mbook'), pick = $('mbook-pick'), other = $('mbook-other'), err = $('mbook-error');
    var timeEl = $('mbook-time'), mphone = $('mphone'), mmobile = $('mmobile');
    var ms = { day: dayList[0], time: null, radius: 'R16', custom: false };
    var DAYS_SHORT = function (i) { return i === 0 ? 'сегодня' : i === 1 ? 'завтра' : DAYS[dayList[i].getDay()]; };
    var plural = function (n) { var a = n % 10, b = n % 100; return n + ' ' + (a === 1 && b !== 11 ? 'окно' : a >= 2 && a <= 4 && (b < 12 || b > 14) ? 'окна' : 'окон'); };
    // Окна дня: прошедшие не показываем, занятые — зачёркнуты
    var slotsFor = function (date) {
      var now = new Date(), out = [];
      for (var h = 8; h < 22; h++) for (var m = 0; m < 60; m += 30) {
        var s = new Date(date); s.setHours(h, m);
        if (s <= now) continue;
        out.push({ t: h + ':' + pad(m), off: busy(date, h, m) });
      }
      return out;
    };
    var nearest = function () {
      for (var i = 0; i < dayList.length; i++) {
        var free = slotsFor(dayList[i]).filter(function (x) { return !x.off; });
        if (free.length) return { day: dayList[i], time: free[0].t };
      }
      return { day: dayList[0], time: null };
    };
    var whatList = function () { return Array.prototype.map.call(document.querySelectorAll('#mwhat input:checked'), function (x) { return x.value; }); };
    var flashT = 0;
    var paint = function (flash) {
      var di = dayList.indexOf(ms.day), dd = ms.day;
      var dayName = (di === 0 ? 'Сегодня' : di === 1 ? 'Завтра' : DAYS[dd.getDay()].replace(/^./, function (c) { return c.toUpperCase(); })) + ', ' + dd.getDate() + ' ' + MONTHS[dd.getMonth()];
      var w = whatList();
      timeEl.textContent = ms.time || '—';
      $('mbook-day').textContent = dayName;
      $('mbook-what').textContent = (w.length ? w.join(', ').toLowerCase() : 'услуга не выбрана') + ' · ' + ms.radius + (mmobile.checked ? ' · выезд к вам' : '');
      $('mbook-kick').textContent = ms.custom ? 'Ваше время' : 'Ближайшее свободное';
      $('msend').textContent = ms.time ? 'Записаться на ' + ms.time : 'Выберите время';
      $('mbook-ok').textContent = ms.time ? 'Готово — ' + DAYS_SHORT(di) + ', ' + ms.time : 'Готово';
      if (flash && motion) {
        timeEl.classList.add('is-flash');
        clearTimeout(flashT);
        flashT = setTimeout(function () { timeEl.classList.remove('is-flash'); }, 450);
      }
    };
    var renderSlots = function () {
      var list = slotsFor(ms.day);
      $('mfree').textContent = plural(list.filter(function (x) { return !x.off; }).length);
      $('mempty').hidden = !!list.length;
      $('mslots').hidden = !list.length;
      if (ms.time && !list.some(function (x) { return x.t === ms.time && !x.off; })) ms.time = null;
      radioGroup($('mslots'), list.map(function (x) {
        return { cls: 'slot', html: x.t, value: x.t, label: x.t, disabled: x.off, checked: x.t === ms.time };
      }), function (v) { ms.time = v; ms.custom = true; err.textContent = ''; paint(true); });
    };
    var renderDays = function () {
      radioGroup($('mdays'), dayList.map(function (dt, i) {
        return { cls: 'day', html: '<span>' + DAYS_SHORT(i) + '</span><b>' + dt.getDate() + '</b>', label: dt.getDate() + ' ' + MONTHS[dt.getMonth()], value: dt, checked: dt === ms.day };
      }), function (v) { ms.day = v; ms.custom = true; renderSlots(); paint(true); });
    };
    radioGroup($('mradius'), RADII.map(function (r) {
      return { cls: 'radius', html: r, value: r, label: 'Диски ' + r, checked: r === ms.radius };
    }), function (v) { ms.radius = v; paint(); });

    // Раскрытие панели. Высота анимируется через grid-template-rows, а всё, что могло
    // раскачивать страницу во время анимации, отключено: якорение прокрутки (overflow-anchor: none),
    // подгонка шрифтов по resize и прилипание лент. Крупное время имеет постоянный размер.
    var setOpen = function (open) {
      pick.classList.toggle('is-open', open);
      other.setAttribute('aria-expanded', String(open));
    };
    other.addEventListener('click', function () { setOpen(other.getAttribute('aria-expanded') !== 'true'); });
    $('mbook-ok').addEventListener('click', function () {
      var r = other.getBoundingClientRect();
      setOpen(false);
      other.focus({ preventScroll: true });
      if (r.top < 64) window.scrollTo({ top: window.scrollY + r.top - 140, behavior: motion ? 'smooth' : 'auto' });
    });

    var setMobile = function (on) {
      mmobile.checked = on;
      $('maddress-field').hidden = !on;
      paint();
    };
    mmobile.addEventListener('change', function () { setMobile(mmobile.checked); });
    $('mwhat').addEventListener('change', function () { err.textContent = ''; paint(); });
    maskPhone(mphone);

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var msg = '', bad = null;
      ['mname', 'mphone', 'maddress'].forEach(function (id) { $(id).classList.remove('is-bad'); });
      if (!ms.time) { msg = 'Выберите время — нажмите «Выбрать другое время».'; setOpen(true); }
      else if (!whatList().length) { msg = 'Отметьте, что нужно сделать.'; setOpen(true); }
      else if (mmobile.checked && $('maddress').value.trim().length < 5) { msg = 'Укажите адрес, куда приехать.'; bad = $('maddress'); }
      else if ($('mname').value.trim().length < 2) { msg = 'Напишите, как к вам обращаться.'; bad = $('mname'); }
      else if (mphone.value.replace(/\D/g, '').length !== 11) { msg = 'Проверьте телефон: нужно 10 цифр после +7.'; bad = mphone; }
      else if (!$('mconsent').checked) msg = 'Отметьте согласие на обработку данных.';
      err.textContent = msg;
      if (bad) { bad.classList.add('is-bad'); bad.focus(); }
      if (msg) return;
      // TODO: отправить заявку (Telegram-бот, CRM или почта) — так же, как из большой формы
      $('book-done-text').textContent = $('mname').value.trim() + ', ждём вас ' + whenFor(ms.day, ms.time) + '. ' +
        (mmobile.checked ? 'Мастер приедет по адресу: ' + $('maddress').value.trim() + '. ' : '') +
        'Если планы поменяются — позвоните, перенесём.';
      showDone();
    });

    // Кнопки «Записаться» в карусели услуг и стрелки в ценах отмечают нужную услугу.
    // Слушаем на документе: строки цен перерисовываются при смене размера дисков
    document.addEventListener('click', function (e) {
      var a = e.target.closest && e.target.closest('[data-mbook-what]');
      if (a) {
        var v = a.getAttribute('data-mbook-what');
        document.querySelectorAll('#mwhat input').forEach(function (x) { x.checked = x.value === v; });
        paint();
      }
      if (e.target.closest && e.target.closest('[data-mobile-service]')) setMobile(true);
    });

    var refresh = function () {
      if (!ms.custom) { var n = nearest(); ms.day = n.day; ms.time = n.time; }
      renderDays(); renderSlots(); paint();
    };
    refresh();
    return { refresh: refresh };
  })();

  /* ---------- Меню-шторка ---------- */
  (function () {
    var sheet = $('msheet'), scrim = $('mscrim'), openBtn = $('menu-open');
    var lastFocus = null;
    var isOpen = function () { return sheet.classList.contains('is-open'); };
    var open = function () {
      lastFocus = document.activeElement;
      sheet.style.removeProperty('--dy');
      sheet.classList.add('is-open');
      scrim.classList.add('is-open');
      document.documentElement.classList.add('is-locked');
      openBtn.setAttribute('aria-expanded', 'true');
      setTimeout(function () { var a = sheet.querySelector('nav a'); if (a && isOpen()) a.focus({ preventScroll: true }); }, 60);
    };
    var close = function (restore) {
      if (!isOpen()) return;
      sheet.classList.remove('is-open', 'is-drag');
      scrim.classList.remove('is-open');
      document.documentElement.classList.remove('is-locked');
      openBtn.setAttribute('aria-expanded', 'false');
      if (restore && lastFocus) lastFocus.focus({ preventScroll: true });
    };
    openBtn.addEventListener('click', open);
    scrim.addEventListener('click', function () { close(true); });
    $('menu-close').addEventListener('click', function () { close(true); });
    sheet.querySelectorAll('a').forEach(function (a) { a.addEventListener('click', function () { close(false); }); });
    document.addEventListener('keydown', function (e) {
      if (!isOpen()) return;
      if (e.key === 'Escape') { close(true); return; }
      if (e.key === 'Tab') { // фокус не уходит из шторки
        var f = Array.prototype.slice.call(sheet.querySelectorAll('a, button'));
        var i = f.indexOf(document.activeElement);
        if (e.shiftKey && i <= 0) { f[f.length - 1].focus(); e.preventDefault(); }
        else if (!e.shiftKey && i === f.length - 1) { f[0].focus(); e.preventDefault(); }
      }
    });
    // Свайп вниз закрывает. Короткое касание остаётся обычным нажатием на ссылку
    var sy = null, dy = 0, dragging = false, pid = null;
    sheet.addEventListener('pointerdown', function (e) {
      if (e.button > 0) return;
      sy = e.clientY; dy = 0; dragging = false; pid = e.pointerId;
    });
    sheet.addEventListener('pointermove', function (e) {
      if (sy === null || e.pointerId !== pid) return;
      dy = Math.max(0, e.clientY - sy);
      if (!dragging && dy > 8) {
        dragging = true;
        sheet.classList.add('is-drag');
        try { sheet.setPointerCapture(pid); } catch (er) {}
      }
      if (dragging) sheet.style.setProperty('--dy', dy + 'px');
    });
    var end = function () {
      if (sy === null) return;
      sy = null;
      if (!dragging) return;
      sheet.classList.remove('is-drag');
      if (dy > 80) close(false); else sheet.style.setProperty('--dy', '0px');
    };
    sheet.addEventListener('pointerup', end);
    sheet.addEventListener('pointercancel', end);
    // после перетаскивания не считаем отпускание пальца нажатием на ссылку
    sheet.addEventListener('click', function (e) { if (dragging) { e.preventDefault(); e.stopPropagation(); dragging = false; } }, true);
    phoneMQ.addEventListener('change', function () { if (!isPhone()) close(false); });
  })();

  /* ---------- Карусель услуг: свайп вбок, карточка, на которую пролистали, — красная ---------- */
  (function () {
    var track = $('mcar-track');
    if (!track) return;
    var cards = Array.prototype.slice.call(track.querySelectorAll('.mcar__card'));
    var tires = cards.map(function (c) { return c.querySelector('.mcar__tire'); });
    var ticks = Array.prototype.slice.call(document.querySelectorAll('#mcar-ticks span'));
    var prev = $('mcar-prev'), next = $('mcar-next'), num = $('mcar-n');
    var cur = 0, raf = 0;
    var step = function () { return (cards[1].offsetLeft - cards[0].offsetLeft) || 1; };
    var draw = function () {
      raf = 0;
      var s = step();
      var i = Math.max(0, Math.min(cards.length - 1, Math.round(track.scrollLeft / s)));
      if (motion) {
        var deg = 'rotate(' + (track.scrollLeft * 0.45).toFixed(1) + 'deg)';
        for (var k = 0; k < tires.length; k++) tires[k].style.transform = deg;
      }
      if (i === cur) return;
      cur = i;
      num.textContent = pad(i + 1);
      cards.forEach(function (c, k) { c.classList.toggle('is-now', k === i); });
      ticks.forEach(function (t, k) { t.classList.toggle('is-on', k === i); t.classList.toggle('is-past', k < i); });
      prev.disabled = i === 0;
      next.disabled = i === cards.length - 1;
    };
    track.addEventListener('scroll', function () { if (!raf) raf = requestAnimationFrame(draw); }, { passive: true });
    // Компьютер: карточки не листаются — выбранная услуга становится большой красной слева, колесо вкатывается в неё
    var wide = matchMedia('(min-width: 1081px)');
    var pick = function (i) {
      if (i === cur) return;
      cur = i;
      num.textContent = pad(i + 1);
      cards.forEach(function (c, k) { c.classList.toggle('is-now', k === i); c.setAttribute('aria-current', String(k === i)); });
      if (motion && tires[i].animate) {
        tires[i].animate([
          { transform: 'translate3d(180px, 60px, 0) rotate(300deg)', opacity: 0 },
          { transform: 'translate3d(0, 0, 0) rotate(0deg)', opacity: 0.9 }
        ], { duration: 950, easing: 'cubic-bezier(.22,.8,.2,1)' });
      }
    };
    var go = function (i) {
      if (wide.matches) { pick(i); return; }
      track.scrollTo({ left: i * step(), behavior: motion ? 'smooth' : 'auto' });
    };
    wide.addEventListener('change', function () { if (!wide.matches) track.scrollLeft = cur * step(); });
    cards.forEach(function (c, k) {
      c.tabIndex = 0;
      c.addEventListener('click', function (e) { if (!e.target.closest('a')) go(k); });
      c.addEventListener('keydown', function (e) { if ((e.key === 'Enter' || e.key === ' ') && e.target === c) { go(k); e.preventDefault(); } });
    });
    prev.addEventListener('click', function () { go(Math.max(0, cur - 1)); });
    next.addEventListener('click', function () { go(Math.min(cards.length - 1, cur + 1)); });
    track.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowRight') { go(Math.min(cards.length - 1, cur + 1)); e.preventDefault(); }
      if (e.key === 'ArrowLeft') { go(Math.max(0, cur - 1)); e.preventDefault(); }
    });
  })();

  /* ---------- Вопросы на компьютере: список слева, ответ на выбранный — в красной плашке справа ---------- */
  (function () {
    var card = $('faq-card');
    if (!card) return;
    var items = Array.prototype.slice.call(document.querySelectorAll('.faq__item'));
    var wide = matchMedia('(min-width: 1081px)');
    var show = function (i, anim) {
      items.forEach(function (d, k) {
        d.classList.toggle('is-sel', k === i);
        d.querySelector('summary').setAttribute('aria-current', String(k === i));
      });
      $('faq-n').textContent = pad(i + 1) + ' / ' + pad(items.length);
      $('faq-q').textContent = items[i].querySelector('summary').textContent;
      $('faq-a').textContent = items[i].querySelector('p').textContent;
      if (anim && motion) { card.classList.remove('is-swap'); void card.offsetWidth; card.classList.add('is-swap'); }
    };
    items.forEach(function (d, i) {
      d.querySelector('summary').addEventListener('click', function (e) {
        if (!wide.matches) return;
        e.preventDefault();
        show(i, true);
      });
    });
    show(0, false);
  })();

  /* ---------- Лента времени: линия заполняется по прокрутке, колёсико катится по ней ---------- */
  (function () {
    var line = document.querySelector('.mtl__line');
    var wheel = document.querySelector('.mtl__wheel');
    var steps = Array.prototype.slice.call(document.querySelectorAll('.mtl__step'));
    if (!motion) { steps.forEach(function (s) { s.classList.add('is-on'); }); return; }
    var job = function (desk) {
      var lr = line.getBoundingClientRect();
      if (lr.bottom < -200 || lr.top > innerHeight + 200) return null;
      var fill = clamp(innerHeight * 0.62 - lr.top, 0, lr.height);
      var tops = steps.map(function (s) { return s.getBoundingClientRect().top + 14 - lr.top; });
      var d = wheel.offsetWidth || 34;
      return function () {
        line.style.setProperty('--fill', fill.toFixed(1) + 'px');
        wheel.style.setProperty('--r', (fill / (Math.PI * d) * 360).toFixed(1) + 'deg');
        steps.forEach(function (s, i) { s.classList.toggle('is-on', tops[i] <= fill + 1); });
        // На компьютере рядом с лентой тикает таймер: 00:00 в начале, 25:00 в конце
        if (desk) {
          var secs = Math.round(fill / (lr.height || 1) * 25 * 60);
          timer.textContent = pad(Math.floor(secs / 60)) + ':' + pad(secs % 60);
        }
      };
    };
    phoneJobs.push(function () { return job(false); });
    deskJobs.push(function () { return wideVisit.matches ? job(true) : null; });
  })();

  /* ---------- Колесо на ленте: крутится на месте от прокрутки и от свайпа плашек ---------- */
  (function () {
    var track = $('wheel-tags');
    var cards = Array.prototype.slice.call(track.children);
    var count = $('wheel-count');
    var cur = -1;
    // Колесо плавно догоняет нужный угол на каждом кадре — без рывков при свайпе
    var rotNow = null, rotTo = 0, rotRaf = 0;
    var rotStep = function () {
      rotNow += (rotTo - rotNow) * 0.14;
      if (Math.abs(rotTo - rotNow) < 0.05) rotNow = rotTo;
      setRot(bigWheel, rotNow.toFixed(2));
      rotRaf = rotNow === rotTo ? 0 : requestAnimationFrame(rotStep);
    };
    var turnTo = function (deg) {
      rotTo = deg;
      if (rotNow === null || !motion) { rotNow = deg; setRot(bigWheel, deg.toFixed(2)); return; }
      if (!rotRaf) rotRaf = requestAnimationFrame(rotStep);
    };
    var index = function () {
      if (track.scrollLeft + track.clientWidth >= track.scrollWidth - 4) return cards.length - 1;
      var left = track.getBoundingClientRect().left + parseFloat(getComputedStyle(track).paddingLeft);
      var best = 0, bd = 1e9;
      cards.forEach(function (c, i) { var d = Math.abs(c.getBoundingClientRect().left - left); if (d < bd) { bd = d; best = i; } });
      return best;
    };
    var wheelJob = function () {
      var r = bigWheel.getBoundingClientRect();
      if (r.bottom < -100 || r.top > innerHeight + 100) return null;
      var step = (cards[1].offsetLeft - cards[0].offsetLeft) || 1;
      var rot = (motion ? (innerHeight - r.top) * 0.18 : 0) + track.scrollLeft / step * 60;
      var i = index();
      return function () {
        turnTo(rot);
        if (i === cur) return;
        cur = i;
        count.textContent = pad(i + 1);
        cards.forEach(function (c, k) { c.classList.toggle('is-now', k === i); });
      };
    };
    phoneJobs.push(wheelJob);
    track.addEventListener('scroll', requestScroll, { passive: true });
    cards.forEach(function (c, k) {
      c.addEventListener('click', function () {
        if (!isPhone()) return;
        track.scrollTo({ left: c.offsetLeft - parseFloat(getComputedStyle(track).paddingLeft), behavior: motion ? 'smooth' : 'auto' });
      });
    });
    // На компьютере подсветка и счётчик не нужны
    phoneMQ.addEventListener('change', function () { if (!isPhone()) { cards.forEach(function (c) { c.classList.remove('is-now'); }); cur = -1; } });
  })();

  // Фото первого экрана на телефоне: если файла пока нет — прячем пустое место
  (function () {
    var fig = $('hero-photo');
    if (!fig) return;
    var img = fig.querySelector('img');
    var fail = function () { fig.hidden = true; hero.classList.add('no-photo'); };
    if (img.complete && !img.naturalWidth) fail();
    img.addEventListener('error', fail);
  })();

  /* ---------- Телефон: машина заезжает с фарами, тормозит с дымом из-под колеса, гасит фары ---------- */
  var carIntro = (function () {
    var fig = $('hero-photo'), car = $('hero-car'), lamp = $('hero-lamp'), cv = $('hero-smoke');
    if (!fig || !car || !cv) return function () {};
    var img = car.querySelector('img'), ctx = cv.getContext('2d');
    var IW = 1536, IH = 1240;                 // размер фото
    var LAMP = [330, 397], WHEEL = [814, 1097]; // фара и точка касания колеса на фото, px

    // Фото вписано как object-fit: cover, object-position: 0% 55% — пересчитываем точку фото в точку блока
    var place = function (pt) {
      var W = fig.clientWidth, H = fig.clientHeight, k = Math.max(W / IW, H / IH);
      return { x: pt[0] * k, y: (H - IH * k) * 0.55 + pt[1] * k, k: k };
    };

    // Клубы дыма: мягкий круг, «изъеденный» шумом; несколько разных, чтобы дым не повторялся
    var noise = function (n) {
      var g = [], i;
      for (i = 0; i < (n + 1) * (n + 1); i++) g.push(Math.random());
      return function (x, y) {
        var xi = Math.floor(x), yi = Math.floor(y), xf = x - xi, yf = y - yi;
        var at = function (a, b) { return g[(b % n) * (n + 1) + (a % n)]; };
        var sx = xf * xf * (3 - 2 * xf), sy = yf * yf * (3 - 2 * yf);
        var top = at(xi, yi) + (at(xi + 1, yi) - at(xi, yi)) * sx;
        var bot = at(xi, yi + 1) + (at(xi + 1, yi + 1) - at(xi, yi + 1)) * sx;
        return top + (bot - top) * sy;
      };
    };
    var makePuff = function () {
      var S = 160, c = document.createElement('canvas');
      c.width = c.height = S;
      var x2 = c.getContext('2d'), im = x2.createImageData(S, S), d = im.data;
      var n1 = noise(8), n2 = noise(16), n3 = noise(32);
      for (var y = 0; y < S; y++) for (var x = 0; x < S; x++) {
        var dx = x / S - 0.5, dy = y / S - 0.5, r = Math.sqrt(dx * dx + dy * dy) * 2;
        var fall = Math.max(0, 1 - r); fall = fall * fall * (3 - 2 * fall);
        var t = n1(x / S * 4, y / S * 4) * 0.55 + n2(x / S * 8, y / S * 8) * 0.3 + n3(x / S * 16, y / S * 16) * 0.15;
        var a = Math.max(0, Math.min(1, (t - 0.32) * 1.9)) * fall;
        var shade = 205 + t * 40, q = (y * S + x) * 4;
        d[q] = shade; d[q + 1] = shade; d[q + 2] = shade + 6; d[q + 3] = a * 255;
      }
      x2.putImageData(im, 0, 0);
      return c;
    };
    var puffs = null, parts = [], raf = 0, last = 0, emitFrom = 0, emitUntil = 0;

    var fit = function () {
      var r = cv.getBoundingClientRect(), d = Math.min(devicePixelRatio || 1, 2);
      cv.width = Math.round(r.width * d); cv.height = Math.round(r.height * d);
      ctx.setTransform(d, 0, 0, d, 0, 0);
    };
    var emit = function (now) {
      // k — масштаб от ширины фото; размер клубов ограничиваем, чтобы на большом экране дым не слипался в пятно
      var p = place(WHEEL), k = fig.clientWidth / 400, ks = Math.min(k, 1.25);
      var top = fig.clientHeight * 0.4; // холст начинается на 40% выше фото
      var shift = new DOMMatrix(getComputedStyle(car).transform).m41 || 0;
      var burst = now < emitFrom + 280, n = burst ? 6 : 3;
      for (var i = 0; i < n; i++) {
        var back = Math.random();
        parts.push({
          x: p.x + shift + (back * 40 - 18) * k, y: top + p.y + (Math.random() * 10 - 6) * k,
          // выброс назад вдоль земли — быстро гаснет, дальше дым всплывает сам
          vx: (burst ? 1.2 + back * 2.6 : 0.4 + back * 1.4) * k, vy: -(Math.random() * 0.35) * k,
          r: (6 + Math.random() * 9) * ks, gr: (0.55 + Math.random() * 0.6) * ks,
          rot: Math.random() * 6.28, spin: (Math.random() - 0.5) * 0.018,
          seed: Math.random() * 100, img: puffs[(Math.random() * puffs.length) | 0],
          a: 0.22 + Math.random() * 0.26, life: 0, max: 1800 + Math.random() * 1600
        });
      }
    };
    var tick = function (now) {
      var dt = Math.min(48, now - (last || now)); last = now;
      if (now >= emitFrom && now < emitUntil) emit(now);
      var r = cv.getBoundingClientRect();
      ctx.clearRect(0, 0, r.width, r.height);
      for (var i = parts.length - 1; i >= 0; i--) {
        var q = parts[i];
        q.life += dt;
        if (q.life > q.max) { parts.splice(i, 1); continue; }
        var f = dt / 16;
        q.vx *= Math.pow(0.955, f); q.vy = q.vy * Math.pow(0.97, f) - 0.012 * f * (q.r / 40);
        q.x += (q.vx + Math.sin(q.life * 0.0021 + q.seed) * 0.35) * f;
        q.y += q.vy * f;
        q.r += q.gr * f * (1 - q.life / q.max * 0.6);
        q.rot += q.spin * f;
        var life = q.life / q.max;
        ctx.globalAlpha = q.a * Math.min(1, q.life / 120) * Math.pow(1 - life, 1.6);
        ctx.save(); ctx.translate(q.x, q.y); ctx.rotate(q.rot);
        ctx.drawImage(q.img, -q.r, -q.r, q.r * 2, q.r * 2);
        ctx.restore();
      }
      ctx.globalAlpha = 1;
      if (parts.length || now < emitUntil) raf = requestAnimationFrame(tick);
      else { raf = 0; ctx.clearRect(0, 0, r.width, r.height); }
    };

    return function () {
      if (!car.animate || fig.hidden) return;
      var l = place(LAMP);
      lamp.style.left = l.x.toFixed(1) + 'px'; lamp.style.top = l.y.toFixed(1) + 'px';
      if (!puffs) puffs = [makePuff(), makePuff(), makePuff(), makePuff()];
      fit();
      // 1. Заезд справа (машина смотрит влево), резкое торможение в конце
      car.animate([
        { transform: 'translateX(125%)', filter: 'blur(3px)', offset: 0 },
        { transform: 'translateX(30%)', filter: 'blur(2px)', offset: 0.55, easing: 'cubic-bezier(.2,.75,.3,1)' },
        { transform: 'translateX(0)', filter: 'blur(0)', offset: 1 }
      ], { duration: 1100, delay: 150, fill: 'backwards', easing: 'cubic-bezier(.3,.1,.6,1)' });
      // 2. Клевок носом при торможении и откат назад
      car.animate([
        { rotate: '0deg' }, { rotate: '-1.7deg', offset: 0.35 }, { rotate: '0.5deg', offset: 0.7 }, { rotate: '0deg' }
      ], { duration: 750, delay: 1050, easing: 'ease-out' });
      // 3. Фары горят с начала, после остановки моргают и гаснут
      lamp.animate([
        { opacity: 1, offset: 0 }, { opacity: 1, offset: 0.62 },
        { opacity: 0.15, offset: 0.66 }, { opacity: 0.9, offset: 0.7 },
        { opacity: 0.9, offset: 0.74 }, { opacity: 0, offset: 0.86 }, { opacity: 0, offset: 1 }
      ], { duration: 4200, fill: 'forwards' });
      // 4. Дым — с начала торможения, меньше секунды
      var t0 = performance.now();
      emitFrom = t0 + 800; emitUntil = t0 + 1650; last = 0;
      if (!raf) raf = requestAnimationFrame(tick);
    };
  })();

  // Верхний отступ первого экрана на телефоне = ровно низ шапки + небольшой зазор (шапка может быть сдвинута в превью)
  var fitHeroTop = function () {
    if (!isPhone()) { hero.style.removeProperty('--hero-top'); return; }
    var hb = header.getBoundingClientRect();
    hero.style.setProperty('--hero-top', Math.round(hb.bottom + window.scrollY + 16) + 'px');
  };
  fitHeroTop();
  window.addEventListener('resize', fitHeroTop);
  if (document.fonts) document.fonts.ready.then(fitHeroTop);

  /* ---------- Первый экран: колесо въезжает, катится дальше от прокрутки, потом текст ---------- */
  phoneHero = (function () {
    var groups = Array.prototype.slice.call(heroWheel.querySelectorAll('.mwheel__rot'));
    var ENTER = 1300;          // длительность въезда, мс
    var t0 = null, done = !motion, raf = 0, x0 = 0;
    var ease = function (t) { return 1 - Math.pow(1 - t, 3); };
    var size = function () { return heroWheel.offsetWidth || 400; };
    var startX = function () { return -(innerWidth / 2 + size() / 2 + 24); };
    var draw = function (now, dKnown) {
      return; // колесо на первом экране телефона убрано
      if (!isPhone() || !motion) return;
      var d = dKnown || size();
      var enter = done ? 0 : t0 === null ? x0 : x0 * (1 - ease(clamp((now - t0) / ENTER, 0, 1)));
      var x = enter + Math.min(window.scrollY, innerHeight * 1.5) * 0.9;
      // поворот ровно на пройденный путь: x / (π·D) оборотов; D — диаметр шины (98% картинки)
      var deg = x / (Math.PI * d * 0.98) * 360;
      heroWheel.style.transform = 'translate3d(' + x.toFixed(2) + 'px,0,0)';
      for (var i = 0; i < groups.length; i++) groups[i].style.transform = 'rotate(' + deg.toFixed(2) + 'deg)';
    };
    var reveal = function () {
      hero.classList.add('m-in');
      setTimeout(function () { hero.classList.add('m-done'); }, 1600);
    };
    var loop = function (now) {
      draw(now);
      if (now - t0 < ENTER) raf = requestAnimationFrame(loop);
      else { done = true; draw(now); reveal(); }
    };
    if (motion && isPhone()) { x0 = startX(); draw(0); }
    phoneJobs.push(function () { var d = size(); return function () { draw(performance.now(), d); }; });
    // при переходе через 640px: на компьютере вращением снова управляет общий обработчик
    phoneMQ.addEventListener('change', function () {
      if (isPhone()) {
        if (hero.classList.contains('is-in') && t0 === null) { done = true; reveal(); }
      } else {
        groups.forEach(function (g) { g.style.transform = ''; });
        heroWheel.style.transform = '';
      }
      requestScroll();
    });
    return {
      start: function () {
        if (!motion) { done = true; hero.classList.add('m-in', 'm-done'); return; }
        // Машина заезжает с фарами и тормозит с дымом — и на телефоне, и на компьютере
        done = true;
        hero.classList.add('m-photo');
        carIntro();
        if (isPhone()) setTimeout(reveal, 450); else hero.classList.add('m-in', 'm-done');
      }
    };
  })();
  if (!motion) hero.classList.add('m-in', 'm-done');
  onScroll(); // все блоки готовы — первый кадр
  if (!motion) {
    timer.textContent = '25:00';
    rail.style.width = '100%';
    steps.forEach(function (li) { li.classList.add('is-on'); });
  }
  window.addEventListener('resize', requestScroll);
})();
