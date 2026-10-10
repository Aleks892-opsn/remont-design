// ПРОТЕКТОР: загрузка, качение колеса от прокрутки, таймер визита, плашки, запись на время
(function () {
  'use strict';

  var motion = document.documentElement.classList.contains('motion');
  var $ = function (id) { return document.getElementById(id); };
  var pad = function (n) { return String(n).padStart(2, '0'); };

  /* ---------- Открыто ли сейчас (8:00–22:00 каждый день) ---------- */
  var setOpen = function () {
    var h = new Date().getHours();
    var open = h >= 8 && h < 22;
    var text = open ? 'Сейчас открыто, до 22:00' : 'Сейчас закрыто, откроемся в 8:00';
    ['open-dot', 'open-dot-2'].forEach(function (id) { $(id).classList.toggle('is-open', open); });
    $('open-text').textContent = open ? 'Открыто до 22:00, без выходных' : 'Закрыто, откроемся в 8:00';
    $('open-text-2').textContent = text;
  };
  setOpen();
  setInterval(setOpen, 60000);
  $('year').textContent = new Date().getFullYear();

  /* ---------- Загрузка: счётчик до 100, экран уезжает, колесо въезжает ---------- */
  var hero = document.querySelector('.hero');
  var startHero = function () { hero.classList.add('is-in'); };
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
  var onScroll = function () {
    ticking = false;
    var y = window.scrollY;
    header.classList.toggle('is-solid', y > 40);
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
  window.addEventListener('scroll', function () {
    if (!ticking) { ticking = true; requestAnimationFrame(onScroll); }
  }, { passive: true });
  onScroll();
  if (!motion) {
    timer.textContent = '25:00';
    rail.style.width = '100%';
    steps.forEach(function (li) { li.classList.add('is-on'); });
  }

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
  var sizeFooter = function () { fitWord(); main.style.setProperty('--footer-h', footer.offsetHeight + 'px'); };
  sizeFooter();
  window.addEventListener('resize', sizeFooter);
  if (document.fonts) document.fonts.ready.then(sizeFooter);

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
  var whenText = function () {
    if (!state.time) return '';
    var i = dayList.indexOf(state.day);
    var dayName = i === 0 ? 'сегодня' : i === 1 ? 'завтра' : DAYS[state.day.getDay()] + ', ' + state.day.getDate() + ' ' + MONTHS[state.day.getMonth()];
    return dayName + ' в ' + state.time;
  };
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
  var phone = $('phone');
  phone.addEventListener('input', function () {
    var d = phone.value.replace(/\D/g, '');
    if (d[0] === '7' || d[0] === '8') d = d.slice(1);
    d = d.slice(0, 10);
    var out = '+7';
    if (d.length) out += ' (' + d.slice(0, 3);
    if (d.length >= 3) out += ') ' + d.slice(3, 6);
    if (d.length >= 6) out += '-' + d.slice(6, 8);
    if (d.length >= 8) out += '-' + d.slice(8, 10);
    phone.value = d.length ? out : '';
  });

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
    $('book-form').hidden = true;
    $('book-done').hidden = false;
    $('book-done').focus();
  });
  $('book-again').addEventListener('click', function () {
    $('book-done').hidden = true;
    $('book-form').hidden = false;
    renderSlots();
  });
})();
