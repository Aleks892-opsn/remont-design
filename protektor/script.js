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
  var visit = $('visit');
  var timer = $('visit-timer');
  var rail = $('visit-rail');
  var steps = Array.prototype.slice.call(document.querySelectorAll('#visit-steps li'));
  // Колесо 1080px в диаметре: при прокрутке на X пикселей «проезжает» X — поворот X / (π·d) оборотов
  var degPerPx = 360 / (Math.PI * 1080);

  var setRot = function (wrap, deg) {
    if (!wrap) return;
    wrap.querySelectorAll('.tire-rot').forEach(function (g) { g.style.setProperty('--rot', deg + 'deg'); });
  };

  var ticking = false;
  var phoneJobs = []; // обработчики прокрутки телефонных блоков (добавляются ниже)
  var onScroll = function () {
    ticking = false;
    var y = window.scrollY;
    header.classList.toggle('is-solid', y > 40);
    if (isPhone()) {
      // Сначала все замеры, потом все записи — чтобы не дёргать раскладку на каждом кадре
      var writes = phoneJobs.map(function (job) { return job(y); });
      writes.forEach(function (w) { if (w) w(); });
      return;
    }
    if (!motion) return;

    setRot(heroWheel, y * degPerPx * 2.2);
    if (belt) belt.style.setProperty('--belt', (-y * 0.6 % 120) + 'px');

    if (bigWheel) {
      var r = bigWheel.getBoundingClientRect();
      setRot(bigWheel, (innerHeight - r.top) * 0.18);
    }

    // Закреплённый блок визита: прогресс от 0 до 1 → таймер 00:00…25:00 и шаги по очереди
    var vr = visit.getBoundingClientRect();
    var total = visit.offsetHeight - innerHeight;
    var p = Math.min(1, Math.max(0, -vr.top / total));
    var secs = Math.round(p * 25 * 60);
    timer.textContent = pad(Math.floor(secs / 60)) + ':' + pad(secs % 60);
    rail.style.width = (p * 100) + '%';
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
     Впишите суммы в рублях вместо null. Для услуг с byRadius — по одной сумме на каждый размер.
     Пока стоит null, на сайте показывается «[цена]». */
  var RADII = ['R13', 'R14', 'R15', 'R16', 'R17', 'R18', 'R19', 'R20', 'R21', 'R22'];
  var PRICES = [
    { name: 'Шиномонтаж комплекта', note: 'снять, перебортовать, отбалансировать, поставить', byRadius: { R13: null, R14: null, R15: null, R16: null, R17: null, R18: null, R19: null, R20: null, R21: null, R22: null } },
    { name: 'Балансировка четырёх колёс', note: 'на станке', byRadius: { R13: null, R14: null, R15: null, R16: null, R17: null, R18: null, R19: null, R20: null, R21: null, R22: null } },
    { name: 'Финишная балансировка', note: 'на автомобиле, если бьёт руль', price: null },
    { name: 'Ремонт прокола', note: 'за колесо, гарантия 12 месяцев', price: null },
    { name: 'Ремонт бокового пореза', note: 'после осмотра', price: null, from: true },
    { name: 'Правка литого диска', note: 'за диск', price: null, from: true },
    { name: 'Сезонное хранение', note: 'за комплект', price: null, key: 'storage' },
    { name: 'Выезд к клиенту', note: 'по [город]', price: null, from: true },
    { name: 'Азот в шины', note: 'для всех клиентов', free: true }
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
      return '<div class="price-row"><b>' + item.name + '<small>' + item.note + '</small></b><span class="' + (p.tbd ? 'is-tbd' : '') + '">' + p.text + '</span></div>';
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
    radioGroup($('slots'), items, function (v) { state.time = v; summary(); });
  };

  radioGroup($('days'), dayList.map(function (dt, i) {
    return {
      cls: 'day',
      html: '<span>' + (i === 0 ? 'сегодня' : i === 1 ? 'завтра' : DAYS[dt.getDay()]) + '</span><b>' + dt.getDate() + '</b>',
      label: dt.getDate() + ' ' + MONTHS[dt.getMonth()],
      value: dt,
      checked: i === 0
    };
  }), function (v) { state.day = v; renderSlots(); summary(); });
  state.day = dayList[0];
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

    // Кнопки «Записаться» в гармошке услуг отмечают нужную услугу
    document.querySelectorAll('[data-mbook-what]').forEach(function (a) {
      a.addEventListener('click', function () {
        var v = a.getAttribute('data-mbook-what');
        document.querySelectorAll('#mwhat input').forEach(function (x) { x.checked = x.value === v; });
        paint();
      });
    });
    document.querySelectorAll('[data-mobile-service]').forEach(function (a) {
      a.addEventListener('click', function () { setMobile(true); });
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

  /* ---------- Гармошка услуг: тап раскрывает, строка посередине экрана — красная ---------- */
  (function () {
    var rows = Array.prototype.slice.call(document.querySelectorAll('.msvc__row'));
    rows.forEach(function (row) {
      var btn = row.querySelector('.msvc__btn');
      btn.addEventListener('click', function () {
        var open = !row.classList.contains('is-open');
        rows.forEach(function (r) { r.classList.remove('is-open'); r.querySelector('.msvc__btn').setAttribute('aria-expanded', 'false'); });
        if (open) { row.classList.add('is-open'); btn.setAttribute('aria-expanded', 'true'); }
        // раскрытие меняет высоты — обновим подсветку после анимации
        setTimeout(requestScroll, 480);
      });
    });
    var act = null;
    phoneJobs.push(function () {
      var mid = innerHeight / 2, next = null;
      for (var i = 0; i < rows.length; i++) {
        var r = rows[i].getBoundingClientRect();
        if (r.top <= mid && r.bottom > mid) { next = rows[i]; break; }
      }
      if (next === act) return null;
      return function () {
        if (act) act.classList.remove('is-act');
        if (next) next.classList.add('is-act');
        act = next;
      };
    });
  })();

  /* ---------- Лента времени: линия заполняется по прокрутке, колёсико катится по ней ---------- */
  (function () {
    var line = document.querySelector('.mtl__line');
    var wheel = document.querySelector('.mtl__wheel');
    var steps = Array.prototype.slice.call(document.querySelectorAll('.mtl__step'));
    if (!motion) { steps.forEach(function (s) { s.classList.add('is-on'); }); return; }
    phoneJobs.push(function () {
      var lr = line.getBoundingClientRect();
      if (lr.bottom < -200 || lr.top > innerHeight + 200) return null;
      var fill = clamp(innerHeight * 0.62 - lr.top, 0, lr.height);
      var tops = steps.map(function (s) { return s.getBoundingClientRect().top + 14 - lr.top; });
      return function () {
        line.style.setProperty('--fill', fill.toFixed(1) + 'px');
        wheel.style.setProperty('--r', (fill / (Math.PI * 34) * 360).toFixed(1) + 'deg');
        steps.forEach(function (s, i) { s.classList.toggle('is-on', tops[i] <= fill + 1); });
      };
    });
  })();

  /* ---------- Колесо на ленте: крутится на месте от прокрутки и от свайпа плашек ---------- */
  (function () {
    var track = $('wheel-tags');
    var cards = Array.prototype.slice.call(track.children);
    var count = $('wheel-count');
    var cur = -1;
    var index = function () {
      if (track.scrollLeft + track.clientWidth >= track.scrollWidth - 4) return cards.length - 1;
      var left = track.getBoundingClientRect().left + parseFloat(getComputedStyle(track).paddingLeft);
      var best = 0, bd = 1e9;
      cards.forEach(function (c, i) { var d = Math.abs(c.getBoundingClientRect().left - left); if (d < bd) { bd = d; best = i; } });
      return best;
    };
    phoneJobs.push(function () {
      var r = bigWheel.getBoundingClientRect();
      if (r.bottom < -100 || r.top > innerHeight + 100) return null;
      var step = (cards[1].offsetLeft - cards[0].offsetLeft) || 1;
      var rot = (motion ? (innerHeight - r.top) * 0.18 : 0) + track.scrollLeft / step * 60;
      var i = index();
      return function () {
        setRot(bigWheel, rot.toFixed(2));
        if (i === cur) return;
        cur = i;
        count.textContent = pad(i + 1);
        cards.forEach(function (c, k) { c.classList.toggle('is-now', k === i); });
      };
    });
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

  /* ---------- Первый экран: колесо въезжает, катится дальше от прокрутки, потом текст ---------- */
  phoneHero = (function () {
    var groups = Array.prototype.slice.call(heroWheel.querySelectorAll('.tire-rot'));
    var ENTER = 1300;          // длительность въезда, мс
    var t0 = null, done = !motion, raf = 0, x0 = 0;
    var ease = function (t) { return 1 - Math.pow(1 - t, 3); };
    var size = function () { return heroWheel.offsetWidth || 400; };
    var startX = function () { return -(innerWidth / 2 + size() / 2 + 24); };
    var draw = function (now, dKnown) {
      if (!isPhone() || !motion) return;
      var d = dKnown || size();
      var enter = done ? 0 : t0 === null ? x0 : x0 * (1 - ease(clamp((now - t0) / ENTER, 0, 1)));
      var x = enter + Math.min(window.scrollY, innerHeight * 1.5) * 0.9;
      // поворот ровно на пройденный путь: x / (π·D) оборотов; D — диаметр шины (98% картинки)
      var deg = x / (Math.PI * d * 0.98) * 360;
      heroWheel.style.setProperty('--wx', x.toFixed(2) + 'px');
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
      }
      requestScroll();
    });
    return {
      start: function () {
        if (!isPhone() || !motion) { done = true; hero.classList.add('m-in', 'm-done'); return; }
        x0 = startX();
        t0 = performance.now();
        raf = requestAnimationFrame(loop);
      }
    };
  })();
  if (!motion) hero.classList.add('m-in', 'm-done');
  if (isPhone()) onScroll(); // телефонные блоки готовы — первый кадр
  if (!motion) {
    timer.textContent = '25:00';
    rail.style.width = '100%';
    steps.forEach(function (li) { li.classList.add('is-on'); });
  }
  window.addEventListener('resize', requestScroll);
})();
