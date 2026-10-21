/* Варианты блоков FORTE. Каждый вариант — кадр 1440 px, уменьшается под ширину экрана. */
(function () {
  var A = '<i>↗</i>';
  var SV = [
    ['01', 'Дом под ключ', 'Газобетон или кирпич, отделка, инженерия. Заезжаете с чемоданом.', 'от 6,8 млн ₽', '6 мес', 'sv-house'],
    ['02', 'Коттеджи', 'Большие дома с панорамами и террасами, проект под ваш участок.', 'от 12 млн ₽', 'по проекту', 'pr-lake'],
    ['03', 'Тёплый контур', 'Фундамент, стены, кровля и окна. Отделку делаете сами.', 'от 3,9 млн ₽', '', 'sv-shell'],
    ['04', 'Коммерческие здания', 'Офисы, магазины, базы отдыха, с проектом и согласованиями.', 'по проекту', '', 'sv-comm']
  ];
  var ST = [
    ['Выезд на участок', 'Инженер бесплатно смотрит грунт и подъезды.', '1 день'],
    ['Проект и смета', 'Каждая статья расходов — построчно.', '1–3 дня'],
    ['Договор', 'Цена и сроки прописаны и не меняются.', '1 день'],
    ['Стройка', 'Платите по этапам, фотоотчёт каждую пятницу.', '4–9 мес'],
    ['Ключи', 'Приёмка вместе с вами, гарантия 10 лет.', '1 день']
  ];
  var PR = [
    ['Дом в «Лесных Далях»', 'Истра, 2025 · газобетон · 2 этажа', '210 м²', '7 мес', 'pr-dali'],
    ['Коттедж у озера', 'Дмитров, 2024 · кирпич · панорамы', '260 м²', '9 мес', 'pr-lake'],
    ['Вилла с бассейном', 'Одинцово, 2025 · плоская кровля', '180 м²', '6 мес', 'pr-villa'],
    ['Дом в соснах', 'Красногорск, 2024 · фахверк, стекло', '160 м²', '6 мес', 'pr-pines'],
    ['Квартал «Грин»', 'Мытищи, 2023 · таунхаусы', '4 × 140 м²', '11 мес', 'pr-green']
  ];
  var RV = [
    ['Марина и Олег', 'Дом 180 м², Истра', '★★★★★', 'Цена в итоге совпала с договором до рубля. Фотоотчёты приходили по пятницам — мы ни разу не ездили на стройку зря.', 'pr-dali'],
    ['Дмитрий', 'Коттедж 260 м², Дмитров', '★★★★☆', 'Сдали на две недели раньше срока. Одна звезда долой — долго согласовывали цвет фасада, но это скорее мы капризничали.', 'pr-lake'],
    ['Елена', 'Дом 140 м², Красногорск', '★★★★★', 'Прораб Андрей — отдельное спасибо. Звонил сам, предупреждал обо всём заранее. Через год приезжали по гарантии — за день всё поправили.', 'pr-pines']
  ];
  var WY = [
    ['150 км', 'от МКАД', 'Москва и область', 'Выезд инженера и доставка материалов — бесплатно. Работаем в 40+ посёлках.'],
    ['0 ₽', 'доплат', 'Цена в договоре не меняется', 'Если материалы подорожали — это наш риск, не ваш. Все работы и материалы в смете построчно.'],
    ['10 лет', 'гарантии', 'Гарантия на дом', 'На фундамент, стены и кровлю. Приезжаем по гарантии за 48 часов.'],
    ['60', 'мастеров', 'Своя бригада и техника', 'Не перепродаём заказы. 60 мастеров в штате и свой автопарк.']
  ];
  var FQ = [
    ['Может ли цена вырасти во время стройки?', 'Нет. Цена фиксируется в договоре. Если материалы дорожают, это наш риск. Меняется, только если вы сами решите что-то добавить.'],
    ['Как платить?', 'По этапам: фундамент, коробка, кровля, отделка. Платите только за готовый и принятый этап. Работаем с ипотекой и материнским капиталом.'],
    ['Можно строить зимой?', 'Да. Фундамент и коробку возводим круглый год с прогревом бетона. Зимой даже проще с подъездом техники к участку.'],
    ['Что, если что-то сломается после сдачи?', 'Гарантия 10 лет на фундамент, стены и кровлю, 2 года на инженерные системы. Приезжаем за 48 часов.'],
    ['У меня свой проект. Возьмётесь?', 'Да. Проверим его и посчитаем смету. Если нужно, адаптируем под участок и бюджет.']
  ];
  var img = function (n) { return '../opora-site/img/' + n + '.webp'; };
  var head = function (eb, h, lead, extra) {
    return '<p class="eb">' + eb + '</p><h2 class="h2">' + h + '</h2>' + (lead ? '<p class="lead">' + lead + '</p>' : '') + (extra || '');
  };

  var B = [];

  /* ===== 1. Что строим (светлый) ===== */
  B.push({ t: 'Что строим', n: 'светлый блок', v: [
    { k: 'А', name: 'Список и большое фото', d: 'Слева четыре направления крупными строками с ценой. Наводите на строку — справа меняется большое вертикальное фото с ценой и сроком. Выбранное направление оранжевое.', dk: false, h:
      '<div style="display:grid;grid-template-columns:1fr 520px;gap:80px;align-items:start">' +
      '<div>' + head('Что строим', 'Четыре направления —<br>одна <em>команда</em>', 'От фундамента до ключей — своими силами, без субподрядчиков, с одним ответственным прорабом.') +
      '<ul style="margin-top:56px;border-top:1px solid var(--line)">' + SV.map(function (s, i) {
        return '<li style="display:grid;grid-template-columns:70px 1fr auto auto;align-items:center;gap:24px;padding:30px 0;border-bottom:1px solid var(--line)">' +
          '<span style="font:800 15px var(--f);color:' + (i === 0 ? 'var(--or)' : 'var(--mute)') + '">' + s[0] + '</span>' +
          '<b style="font:900 34px/1.1 var(--f);letter-spacing:-.035em;color:' + (i === 0 ? 'var(--or)' : 'var(--ink)') + '">' + s[1] + '</b>' +
          '<span style="font:700 17px var(--f);white-space:nowrap">' + s[3] + '</span>' +
          '<span class="arr' + (i === 0 ? '' : ' gh') + '">↗</span></li>';
      }).join('') + '</ul></div>' +
      '<div class="shell" style="margin-top:20px"><div class="ph ov" style="height:700px;border-radius:30px"><img src="' + img('sv-house') + '" alt=""><div class="cap"><span class="chip w">01 · Самое частое</span><p style="margin-top:16px;font:900 38px/1.05 var(--f);letter-spacing:-.04em">Дом под ключ</p><p style="margin-top:10px;font-size:16px;opacity:.88;max-width:380px">Газобетон или кирпич, отделка, инженерия. Заезжаете с чемоданом.</p><div class="row" style="margin-top:22px;gap:28px"><div><p style="font-size:13px;opacity:.7">Цена</p><b style="font-size:24px">от 6,8 млн ₽</b></div><div><p style="font-size:13px;opacity:.7">Срок</p><b style="font-size:24px">6 мес</b></div></div></div></div></div></div>' },
    { k: 'Б', name: 'Асимметричная витрина', d: 'Фото-плитки разного размера: «Дом под ключ» самая большая, рядом высокая «Коттеджи» и две поменьше. На каждой цена и стрелка. Сразу видны все направления.', dk: false, h:
      '<div style="display:flex;justify-content:space-between;align-items:flex-end;gap:60px">' + '<div>' + head('Что строим', 'Четыре направления —<br>одна <em>команда</em>') + '</div><p class="lead" style="margin:0 0 8px;max-width:420px">От фундамента до ключей — своими силами, без субподрядчиков, с одним ответственным прорабом.</p></div>' +
      '<div style="display:grid;grid-template-columns:1.5fr 1fr 1fr;grid-template-rows:330px 330px;gap:16px;margin-top:64px">' +
      SV.map(function (s, i) {
        var pos = ['grid-row:1/span 2', 'grid-row:1/span 2', '', ''][i];
        return '<div class="shell" style="' + pos + '"><div class="ph ov" style="height:100%"><img src="' + img(s[5]) + '" alt=""><div class="cap" style="display:flex;align-items:flex-end;justify-content:space-between;gap:16px"><div><span class="chip ' + (i === 0 ? '' : 'w') + '" style="' + (i === 0 ? 'background:var(--or);color:#fff' : '') + '">' + s[3] + '</span><p style="margin-top:14px;font:900 ' + (i === 0 ? 40 : 26) + 'px/1.05 var(--f);letter-spacing:-.035em">' + s[1] + '</p>' + (i < 2 ? '<p style="margin-top:8px;font-size:15px;opacity:.88;max-width:340px">' + s[2] + '</p>' : '') + '</div><span class="arr">↗</span></div></div></div>';
      }).join('').replace('grid-row:1/span 2"><div class="ph ov" style="height:100%"><img src="img/pr-lake', 'grid-row:1/span 2;grid-column:2"><div class="ph ov" style="height:100%"><img src="img/pr-lake') +
      '</div>' }
  ]});

  /* ===== 2. Конфигуратор (тёмный) ===== */
  B.push({ t: 'Конфигуратор', n: 'тёмный блок', v: [
    { k: 'А', name: 'Студия', d: 'Слева большое фото дома, на нём метки «Фасад» и «Кровля». Справа панель: площадь ползунком, этажи, фасад и кровля, внизу крупная цена оранжевым. Меняете параметр — цена пересчитывается.', dk: true, h:
      head('Конфигуратор', 'Соберите дом — <em>увидите цену</em> сразу') +
      '<div style="display:grid;grid-template-columns:1fr 470px;gap:20px;margin-top:56px">' +
      '<div class="shell"><div class="ph" style="height:100%;min-height:640px"><img src="' + img('modern') + '" alt="">' +
      '<span class="chip w" style="position:absolute;left:38%;top:30%">● Фасад: графит</span><span class="chip w" style="position:absolute;left:58%;top:12%">● Кровля: плоская</span><span class="chip" style="position:absolute;left:28px;bottom:28px;background:rgba(0,0,0,.55);color:#fff">↔ Поверните дом</span></div></div>' +
      '<div class="shell"><div class="core" style="height:100%;padding:36px;display:flex;flex-direction:column;gap:30px">' +
      '<div><div class="row" style="justify-content:space-between"><span class="mut" style="font-weight:600">Площадь</span><b style="font-size:22px">160 м²</b></div><div style="position:relative;height:6px;margin-top:18px;border-radius:3px;background:rgba(255,255,255,.12)"><i style="position:absolute;left:0;top:0;bottom:0;width:42%;border-radius:3px;background:var(--or)"></i><i style="position:absolute;left:42%;top:50%;width:24px;height:24px;margin:-12px 0 0 -12px;border-radius:50%;background:#fff;box-shadow:0 0 0 6px rgba(255,106,26,.3)"></i></div></div>' +
      '<div><p class="mut" style="font-weight:600;margin-bottom:12px">Этажность</p><div class="seg"><span>1 этаж</span><span class="on">2 этажа</span></div></div>' +
      '<div><p class="mut" style="font-weight:600;margin-bottom:12px">Фасад</p><div class="row" style="gap:10px">' + [['#e9e4dc', 'Штукатурка'], ['#2c2f33', 'Графит', 1], ['#a8743f', 'Дерево'], ['#9a4b32', 'Кирпич']].map(function (c) { return '<span style="display:grid;justify-items:center;gap:8px;font-size:13px;color:' + (c[2] ? '#fff' : 'var(--dmute)') + '"><i style="width:58px;height:58px;border-radius:18px;background:' + c[0] + ';box-shadow:' + (c[2] ? '0 0 0 3px var(--black),0 0 0 5px var(--or)' : 'inset 0 0 0 1px rgba(255,255,255,.15)') + '"></i>' + c[1] + '</span>'; }).join('') + '</div></div>' +
      '<div><p class="mut" style="font-weight:600;margin-bottom:12px">Кровля</p><div class="seg"><span class="on">Плоская</span><span>Скатная</span></div></div>' +
      '<div style="margin-top:auto;padding-top:24px;border-top:1px solid var(--dline)"><div class="row" style="justify-content:space-between;align-items:flex-end"><div><p class="mut" style="font-size:14px">Дом под ключ</p><p class="big" style="font-size:54px;color:var(--or);margin-top:6px">8,3 млн ₽</p></div><div style="text-align:right"><p class="mut" style="font-size:14px">Срок</p><b style="font-size:24px">7 мес</b></div></div><span class="btn" style="width:100%;justify-content:space-between;margin-top:22px">Получить точную смету' + A + '</span></div>' +
      '</div></div></div>' },
    { k: 'Б', name: 'Конструктор в одну линию', d: 'Наверху фото дома во всю ширину. Под ним все настройки в одну строку: площадь, этажи, фасад, кровля. Внизу белая полоса-итог: площадь, цена, срок и кнопка. Чисто, как настройка машины на сайте автосалона.', dk: true, h:
      '<div style="display:flex;justify-content:space-between;align-items:flex-end;gap:60px">' + '<div>' + head('Конфигуратор', 'Соберите <em>свой дом</em>') + '</div><p class="lead" style="margin:0 0 8px;max-width:440px">Выберите этажи, фасад и кровлю. Расчёт ориентировочный — точную смету пришлём за день.</p></div>' +
      '<div class="shell" style="margin-top:56px"><div class="ph" style="height:520px"><img src="' + img('modern') + '" alt="" style="object-position:50% 60%"></div></div>' +
      '<div style="display:grid;grid-template-columns:1.3fr auto auto auto;gap:40px;align-items:end;margin-top:40px;padding:0 8px">' +
      '<div><div class="row" style="justify-content:space-between"><span class="mut" style="font-weight:600">Площадь</span><b>160 м²</b></div><div style="position:relative;height:6px;margin-top:22px;border-radius:3px;background:rgba(255,255,255,.12)"><i style="position:absolute;left:0;top:0;bottom:0;width:42%;border-radius:3px;background:var(--or)"></i><i style="position:absolute;left:42%;top:50%;width:24px;height:24px;margin:-12px 0 0 -12px;border-radius:50%;background:#fff"></i></div></div>' +
      '<div><p class="mut" style="font-weight:600;margin-bottom:12px">Этажи</p><div class="seg"><span>1</span><span class="on">2</span></div></div>' +
      '<div><p class="mut" style="font-weight:600;margin-bottom:12px">Фасад</p><div class="row" style="gap:8px">' + ['#e9e4dc', '#2c2f33', '#a8743f', '#9a4b32'].map(function (c, i) { return '<i style="width:44px;height:44px;border-radius:50%;background:' + c + ';box-shadow:' + (i === 1 ? '0 0 0 3px var(--black),0 0 0 5px var(--or)' : 'inset 0 0 0 1px rgba(255,255,255,.18)') + '"></i>'; }).join('') + '</div></div>' +
      '<div><p class="mut" style="font-weight:600;margin-bottom:12px">Кровля</p><div class="seg"><span class="on">Плоская</span><span>Скатная</span></div></div></div>' +
      '<div style="display:grid;grid-template-columns:repeat(3,auto) 1fr;align-items:center;gap:64px;margin-top:40px;padding:26px 26px 26px 40px;border-radius:30px;background:#fff;color:var(--ink)"><div><p style="font-size:14px;color:var(--mute)">Площадь</p><b style="font-size:26px">160 м²</b></div><div><p style="font-size:14px;color:var(--mute)">Дом под ключ</p><b class="big" style="font-size:40px;color:var(--or)">8,3 млн ₽</b></div><div><p style="font-size:14px;color:var(--mute)">Срок</p><b style="font-size:26px">7 мес</b></div><span class="btn" style="justify-self:end">Получить точную смету' + A + '</span></div>' }
  ]});

  /* ===== 3. Как работаем (светлый) ===== */
  B.push({ t: 'Как работаем', n: 'светлый блок', v: [
    { k: 'А', name: 'Лестница этапов', d: 'Пять этапов ступенями вверх — как дом растёт этаж за этажом. Каждая ступень — карточка с номером, сроком и описанием. Самая длинная «Стройка» оранжевая. При прокрутке ступени поднимаются по очереди.', dk: false, h:
      '<div style="display:flex;justify-content:space-between;align-items:flex-end;gap:60px">' + '<div>' + head('Как работаем', 'От выезда <em>до ключей</em>') + '</div><p class="lead" style="margin:0 0 8px;max-width:440px">Пять этапов без сюрпризов: вы знаете цену, срок и что происходит на участке — каждый день.</p></div>' +
      '<div style="display:grid;grid-template-columns:repeat(5,1fr);gap:14px;align-items:end;margin-top:72px;height:640px">' +
      ST.map(function (s, i) {
        var on = i === 3;
        return '<div class="shell" style="height:' + (60 + i * 10) + '%"><div class="core" style="height:100%;padding:30px 26px;display:flex;flex-direction:column;' + (on ? 'background:var(--or);color:#fff' : '') + '"><span class="big" style="font-size:64px;color:' + (on ? '#fff' : 'var(--or)') + '">0' + (i + 1) + '</span><b style="margin-top:auto;font:800 22px/1.2 var(--f);letter-spacing:-.02em">' + s[0] + '</b><p style="margin-top:8px;font-size:15px;line-height:1.5;color:' + (on ? 'rgba(255,255,255,.9)' : 'var(--ink2)') + '">' + s[1] + '</p><span class="chip" style="margin-top:18px;align-self:flex-start;' + (on ? 'background:rgba(0,0,0,.18);color:#fff' : '') + '">' + s[2] + '</span></div></div>';
      }).join('') + '</div>' },
    { k: 'Б', name: 'Шкала времени', d: 'Широкая шкала от выезда до ключей: длина каждого отрезка — сколько длится этап, поэтому сразу видно, что основное время занимает стройка. Под шкалой этапы с описанием.', dk: false, h:
      head('Как работаем', 'От выезда до ключей — <em>4–9 месяцев</em>', 'Пять этапов без сюрпризов: вы знаете цену, срок и что происходит на участке — каждый день.') +
      '<div class="shell" style="margin-top:64px"><div class="core" style="padding:48px 48px 44px">' +
      '<div style="display:grid;grid-template-columns:1fr 1.4fr 1fr 6fr 1fr;gap:6px;height:84px">' + ST.map(function (s, i) { return '<div style="border-radius:18px;padding:0 18px;display:flex;align-items:center;justify-content:space-between;background:' + (i === 3 ? 'var(--or)' : 'var(--bg)') + ';color:' + (i === 3 ? '#fff' : 'var(--ink)') + '"><b style="font-size:18px">0' + (i + 1) + '</b>' + (i === 3 ? '<span style="font-weight:700">' + s[2] + ' · основное время</span>' : '') + '</div>'; }).join('') + '</div>' +
      '<div style="display:grid;grid-template-columns:repeat(5,1fr);gap:36px;margin-top:40px">' + ST.map(function (s, i) { return '<div><p style="font:800 14px var(--f);color:var(--or)">0' + (i + 1) + ' · ' + s[2] + '</p><b style="display:block;margin-top:10px;font:800 21px/1.2 var(--f);letter-spacing:-.02em">' + s[0] + '</b><p style="margin-top:8px;font-size:15px;line-height:1.5;color:var(--ink2)">' + s[1] + '</p></div>'; }).join('') + '</div>' +
      '</div></div>' }
  ]});

  /* ===== 4. Стройка онлайн (тёмный) ===== */
  B.push({ t: 'Стройка онлайн', n: 'тёмный блок', v: [
    { k: 'А', name: 'Кабинет на экране', d: 'Слева текст, справа личный кабинет как настоящее приложение: дом, прогресс по этапам, 62%, до сдачи 11 недель, прораб и свежие фото с датами. Показывает, что клиент видит стройку каждый день.', dk: true, h:
      '<div style="display:grid;grid-template-columns:420px 1fr;gap:80px;align-items:center">' +
      '<div>' + head('Стройка онлайн', 'Вы видите <em>каждый день</em> стройки', 'В личном кабинете — прогресс по этапам и свежие фото с датами. На участок можно не ездить.') + '<span class="btn" style="margin-top:36px">Как это работает' + A + '</span></div>' +
      '<div class="shell"><div class="core" style="padding:34px">' +
      '<div class="row" style="justify-content:space-between"><div><p class="mut" style="font-size:14px">Ваш дом</p><b style="font-size:24px">Дом 180 м², Истра</b></div><span class="chip">● Идут работы</span></div>' +
      '<div style="display:grid;grid-template-columns:repeat(6,1fr);gap:6px;margin-top:28px">' + ['Фундамент', 'Стены', 'Кровля', 'Окна', 'Отделка', 'Готово'].map(function (s, i) { return '<div><i style="display:block;height:8px;border-radius:4px;background:' + (i < 3 ? 'var(--or)' : i === 3 ? 'linear-gradient(90deg,var(--or) 40%,rgba(255,255,255,.12) 40%)' : 'rgba(255,255,255,.12)') + '"></i><span style="display:block;margin-top:10px;font-size:13px;color:' + (i < 4 ? '#fff' : 'var(--dmute)') + '">' + s + '</span></div>'; }).join('') + '</div>' +
      '<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-top:28px">' + [['62%', 'готовности'], ['11 недель', 'до сдачи'], ['Андрей К.', 'прораб']].map(function (s) { return '<div style="padding:20px;border-radius:20px;background:var(--card2)"><b style="font-size:26px">' + s[0] + '</b><p class="mut" style="font-size:14px">' + s[1] + '</p></div>'; }).join('') + '</div>' +
      '<p class="mut" style="margin-top:28px;font-size:14px">Фотоотчёт · пятница, 14:20</p><div style="display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-top:12px">' + [['found', '3 окт'], ['site', '10 окт'], ['terrace', '17 окт']].map(function (p) { return '<div class="ph" style="height:180px;border-radius:20px"><img src="' + img(p[0]) + '" alt=""><span class="chip w" style="position:absolute;left:12px;bottom:12px;height:28px;font-size:12px">' + p[1] + '</span></div>'; }).join('') + '</div>' +
      '</div></div></div>' },
    { k: 'Б', name: 'Лента фотоотчётов', d: 'Большое кольцо прогресса 62% и «до сдачи 11 недель», рядом лента крупных фото по неделям с датами — как плёнка стройки. Видно, как дом растёт от фундамента до террасы.', dk: true, h:
      '<div style="display:flex;justify-content:space-between;align-items:flex-end;gap:60px">' + '<div>' + head('Стройка онлайн', 'Дом растёт —<br><em>вы это видите</em>') + '</div><p class="lead" style="margin:0 0 8px;max-width:420px">Каждую пятницу прораб присылает фото с датами в личный кабинет. На участок можно не ездить.</p></div>' +
      '<div style="display:grid;grid-template-columns:340px repeat(3,1fr);gap:16px;margin-top:64px;align-items:stretch">' +
      '<div class="shell"><div class="core" style="height:100%;padding:34px;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center"><div style="position:relative;width:220px;height:220px;border-radius:50%;background:conic-gradient(var(--or) 0 62%,rgba(255,255,255,.1) 62%);display:grid;place-items:center"><div style="width:184px;height:184px;border-radius:50%;background:var(--card);display:grid;place-content:center"><b class="big" style="font-size:60px">62%</b><span class="mut" style="font-size:14px">готовности</span></div></div><b style="margin-top:28px;font-size:22px">До сдачи 11 недель</b><p class="mut" style="font-size:15px;margin-top:6px">Дом 180 м², Истра · прораб Андрей К.</p></div></div>' +
      [['found', 'Неделя 3', 'Фундамент'], ['site', 'Неделя 9', 'Стены'], ['terrace', 'Неделя 16', 'Терраса']].map(function (p) { return '<div class="shell"><div class="ph ov" style="height:520px"><img src="' + img(p[0]) + '" alt=""><div class="cap"><span class="chip" style="background:var(--or);color:#fff">' + p[1] + '</span><p style="margin-top:12px;font:800 24px var(--f)">' + p[2] + '</p></div></div></div>'; }).join('') + '</div>' }
  ]});

  /* ===== 5. Прораб (светлый) ===== */
  B.push({ t: 'Прораб', n: 'светлый блок', v: [
    { k: 'А', name: 'Цитата и портрет', d: 'Слева крупная цитата прораба «Я отвечаю за ваш дом лично» и три цифры. Справа фото с табличкой «Андрей Котов, главный прораб» и зелёной точкой «сейчас на объекте». Кнопка «Написать прорабу».', dk: false, h:
      '<div style="display:grid;grid-template-columns:1fr 540px;gap:90px;align-items:center">' +
      '<div><p class="eb">Кто отвечает за дом</p><p style="margin-top:30px;font:900 120px/0.7 var(--f);color:var(--or)">“</p><p style="font:800 52px/1.12 var(--f);letter-spacing:-.04em">Я отвечаю за ваш дом лично и всегда на связи в мессенджере.</p>' +
      '<div style="display:grid;grid-template-columns:repeat(3,1fr);margin-top:56px;border-top:1px solid var(--line)">' + [['18', 'лет на стройке'], ['100%', 'домов сдали в срок'], ['1', 'прораб на весь объект']].map(function (s, i) { return '<div style="padding:26px 24px 0 ' + (i ? '24px' : '0') + ';' + (i ? 'border-left:1px solid var(--line)' : '') + '"><b class="big" style="font-size:52px">' + s[0] + '</b><p class="mut" style="margin-top:8px;font-size:15px">' + s[1] + '</p></div>'; }).join('') + '</div>' +
      '<span class="btn" style="margin-top:44px">Написать прорабу' + A + '</span></div>' +
      '<div class="shell"><div class="ph" style="height:660px"><img src="' + img('plan') + '" alt="" style="object-position:40% 50%"><div style="position:absolute;left:20px;right:20px;bottom:20px;padding:22px 24px;border-radius:22px;background:rgba(255,255,255,.94);display:flex;align-items:center;justify-content:space-between"><div><b style="font-size:22px">Андрей Котов</b><p class="mut" style="font-size:14px">Главный прораб FORTE</p></div><span class="chip" style="background:#e5f6ea;color:#1f8a43">● Сейчас на объекте</span></div></div></div></div>' },
    { k: 'Б', name: 'Визитка', d: 'В центре большая визитка прораба, слегка повёрнутая, как будто лежит на столе: имя, должность, цифры, кнопки «Написать» и «Позвонить». По бокам фото с объекта и короткий текст. Тепло и по-человечески.', dk: false, h:
      '<div style="text-align:center"><p class="eb">Кто отвечает за дом</p><h2 class="h2">Один человек — <em>от фундамента до ключей</em></h2></div>' +
      '<div style="position:relative;height:620px;margin-top:56px">' +
      '<div class="ph" style="position:absolute;left:0;top:60px;width:330px;height:440px;transform:rotate(-4deg);border-radius:26px;box-shadow:0 30px 60px -30px rgba(0,0,0,.4)"><img src="' + img('found') + '" alt=""></div>' +
      '<div class="ph" style="position:absolute;right:0;top:40px;width:330px;height:440px;transform:rotate(3deg);border-radius:26px;box-shadow:0 30px 60px -30px rgba(0,0,0,.4)"><img src="' + img('site') + '" alt=""></div>' +
      '<div class="shell" style="position:absolute;left:50%;top:40px;width:600px;margin-left:-300px;transform:rotate(-1.5deg);background:rgba(13,13,13,.06)"><div class="core" style="padding:44px 48px;box-shadow:0 40px 80px -30px rgba(0,0,0,.35)">' +
      '<div class="row" style="justify-content:space-between"><span style="font:900 20px var(--f);letter-spacing:.1em">FORTE</span><span class="chip" style="background:#e5f6ea;color:#1f8a43">● На объекте</span></div>' +
      '<p style="margin-top:48px;font:900 50px/1 var(--f);letter-spacing:-.045em">Андрей Котов</p><p class="mut" style="margin-top:10px;font-size:17px">Главный прораб · отвечает лично</p>' +
      '<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-top:36px">' + [['18 лет', 'на стройке'], ['100%', 'в срок'], ['1', 'на объект']].map(function (s) { return '<div style="padding:18px;border-radius:18px;background:var(--bg)"><b style="font-size:24px">' + s[0] + '</b><p class="mut" style="font-size:13px">' + s[1] + '</p></div>'; }).join('') + '</div>' +
      '<div class="row" style="margin-top:32px"><span class="btn sm">Написать' + A + '</span><span class="btn sm ink">Позвонить' + A + '</span></div></div></div>' +
      '</div>' }
  ]});

  /* ===== 6. Проекты (тёмный) ===== */
  B.push({ t: 'Проекты', n: 'тёмный блок', v: [
    { k: 'А', name: 'Большой кадр и список', d: 'Слева большое фото выбранного проекта с площадью, сроком и кнопкой «Показать вживую». Справа список всех пяти проектов: нажали на строку — сменилось фото.', dk: true, h:
      '<div style="display:flex;justify-content:space-between;align-items:flex-end;gap:60px"><div>' + head('Проекты', 'Построили <em>240+</em> домов.<br>Вот некоторые') + '</div><p class="lead" style="margin:0 0 8px;max-width:420px">Каждый — реальный объект с фотоотчётом. Покажем вживую в посёлке рядом с вами.</p></div>' +
      '<div style="display:grid;grid-template-columns:1fr 440px;gap:20px;margin-top:64px">' +
      '<div class="shell"><div class="ph ov" style="height:640px"><img src="' + img('pr-dali') + '" alt=""><div class="cap" style="display:flex;justify-content:space-between;align-items:flex-end;gap:20px"><div><span class="chip" style="background:var(--or);color:#fff">01 / 05</span><p style="margin-top:16px;font:900 44px/1.05 var(--f);letter-spacing:-.04em">Дом в «Лесных Далях»</p><p style="margin-top:8px;opacity:.85">Истра, 2025 · газобетон · 2 этажа</p></div><div class="row" style="gap:32px;flex:none"><div><p style="font-size:13px;opacity:.7">Площадь</p><b style="font-size:26px">210 м²</b></div><div><p style="font-size:13px;opacity:.7">Срок</p><b style="font-size:26px">7 мес</b></div></div></div></div></div>' +
      '<div class="shell"><div class="core" style="height:100%;padding:12px;display:flex;flex-direction:column;gap:6px">' + PR.map(function (p, i) { return '<div style="display:grid;grid-template-columns:92px 1fr;gap:18px;align-items:center;padding:12px;border-radius:22px;' + (i === 0 ? 'background:var(--card2);box-shadow:inset 3px 0 0 var(--or)' : '') + '"><div class="ph" style="height:76px;border-radius:16px"><img src="' + img(p[4]) + '" alt=""></div><div><b style="font-size:17px;line-height:1.25;display:block;color:' + (i === 0 ? '#fff' : 'rgba(255,255,255,.8)') + '">' + p[0] + '</b><p class="mut" style="font-size:13px;margin-top:4px">' + p[2] + ' · ' + p[3] + '</p></div></div>'; }).join('') + '<span class="btn" style="margin-top:auto;justify-content:space-between">Показать вживую' + A + '</span></div></div></div>' },
    { k: 'Б', name: 'Лента-слайдер', d: 'Проекты идут широкой лентой, которая уходит за правый край — понятно, что можно листать. Первая карточка крупнее. Под лентой полоска прогресса и стрелки.', dk: true, h:
      '<div style="display:flex;justify-content:space-between;align-items:flex-end;gap:60px"><div>' + head('Проекты', 'Построили <em>240+</em> домов') + '</div><div class="row"><span class="arr gh">←</span><span class="arr">→</span></div></div>' +
      '<div style="display:flex;gap:16px;margin-top:56px;margin-right:-100px">' + PR.map(function (p, i) { return '<div class="shell" style="flex:none;width:' + (i === 0 ? 640 : 420) + 'px"><div class="ph ov" style="height:560px"><img src="' + img(p[4]) + '" alt=""><div class="cap"><p class="mut" style="color:rgba(255,255,255,.75);font-size:14px">0' + (i + 1) + ' · ' + p[1] + '</p><p style="margin-top:8px;font:900 ' + (i === 0 ? 36 : 26) + 'px/1.1 var(--f);letter-spacing:-.035em">' + p[0] + '</p><div class="row" style="margin-top:14px;gap:10px"><span class="chip w">' + p[2] + '</span><span class="chip w">' + p[3] + '</span></div></div></div></div>'; }).join('') + '</div>' +
      '<div class="row" style="margin-top:36px;gap:24px"><span style="font:800 15px var(--f)">01 / 05</span><div style="flex:1;height:3px;border-radius:2px;background:rgba(255,255,255,.12)"><i style="display:block;width:20%;height:100%;border-radius:2px;background:var(--or)"></i></div><span class="btn sm">Показать вживую' + A + '</span></div>' }
  ]});

  /* ===== 7. Отзывы (светлый) ===== */
  B.push({ t: 'Отзывы', n: 'светлый блок', v: [
    { k: 'А', name: 'Одна большая цитата', d: 'Один отзыв на весь блок: крупная цитата, звёзды, кто сказал и фото их дома. Стрелками листаются остальные. Читается как история, а не как сетка.', dk: false, h:
      '<div style="display:grid;grid-template-columns:1fr 460px;gap:90px;align-items:center">' +
      '<div><p class="eb">Отзывы · говорят хозяева</p><p class="stars" style="margin-top:34px;font-size:24px">★★★★★</p><p style="margin-top:22px;font:800 46px/1.18 var(--f);letter-spacing:-.035em">«Цена в итоге совпала с договором <span style="color:var(--or)">до рубля</span>. Фотоотчёты приходили по пятницам — мы ни разу не ездили на стройку зря.»</p>' +
      '<div class="row" style="margin-top:44px;justify-content:space-between"><div class="row" style="gap:16px"><span style="display:grid;place-items:center;width:58px;height:58px;border-radius:50%;background:var(--or);color:#fff;font:800 20px var(--f)">М</span><div><b style="font-size:19px">Марина и Олег</b><p class="mut" style="font-size:15px">Дом 180 м², Истра</p></div></div><div class="row"><span style="font:800 15px var(--f);margin-right:10px">01 / 03</span><span class="arr gh">←</span><span class="arr">→</span></div></div></div>' +
      '<div class="shell" style="transform:rotate(2deg)"><div class="ph ov" style="height:560px"><img src="' + img('pr-dali') + '" alt=""><div class="cap"><span class="chip w">Их дом</span><p style="margin-top:10px;font:800 22px var(--f)">Дом 180 м², Истра</p></div></div></div></div>' },
    { k: 'Б', name: 'Три отзыва с фото домов', d: 'Три карточки разной высоты, как стопка писем. Наверху каждой — фото дома, который построили, под ним отзыв. Средняя выше остальных.', dk: false, h:
      '<div style="display:flex;justify-content:space-between;align-items:flex-end;gap:60px"><div>' + head('Отзывы', 'Говорят <em>хозяева</em>') + '</div><p class="lead" style="margin:0 0 8px;max-width:400px">Три семьи, три дома. Каждый можно посмотреть вживую.</p></div>' +
      '<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:18px;margin-top:64px;align-items:start">' + RV.map(function (r, i) { return '<div class="shell" style="margin-top:' + [60, 0, 90][i] + 'px"><div class="core" style="padding:12px 12px 32px"><div class="ph" style="height:220px;border-radius:22px"><img src="' + img(r[4]) + '" alt=""></div><div style="padding:24px 20px 0"><p class="stars">' + r[2] + '</p><p style="margin-top:14px;font:600 18px/1.55 var(--f)">«' + r[3] + '»</p><div class="row" style="margin-top:22px;gap:14px"><span style="display:grid;place-items:center;width:46px;height:46px;border-radius:50%;background:var(--or-soft);color:var(--or);font:800 17px var(--f)">' + r[0][0] + '</span><div><b>' + r[0] + '</b><p class="mut" style="font-size:14px">' + r[1] + '</p></div></div></div></div></div>'; }).join('') + '</div>' }
  ]});

  /* ===== 8. Почему FORTE (тёмный) ===== */
  B.push({ t: 'Почему FORTE', n: 'тёмный блок', v: [
    { k: 'А', name: 'Четыре большие цифры', d: 'Сетка 2×2 с тонкими линиями: в каждой ячейке огромная цифра (150 км, 0 ₽ доплат, 10 лет, 60 мастеров), под ней заголовок и пояснение. Как отчёт компании — строго и убедительно.', dk: true, h:
      '<div style="display:flex;justify-content:space-between;align-items:flex-end;gap:60px"><div>' + head('Почему FORTE', 'Строим честно —<br>и это <em>видно в цифрах</em>') + '</div></div>' +
      '<div style="display:grid;grid-template-columns:1fr 1fr;margin-top:72px;border-top:1px solid var(--dline)">' + WY.map(function (w, i) { return '<div style="padding:56px ' + (i % 2 ? '0 56px 64px' : '64px 56px 0') + ';border-bottom:1px solid var(--dline);' + (i % 2 ? 'border-left:1px solid var(--dline)' : '') + '"><div class="row" style="align-items:baseline;gap:14px"><b class="big" style="font-size:110px;color:' + (i === 1 ? 'var(--or)' : '#fff') + '">' + w[0] + '</b><span class="mut" style="font-size:20px;font-weight:600">' + w[1] + '</span></div><b style="display:block;margin-top:26px;font:800 26px var(--f);letter-spacing:-.02em">' + w[2] + '</b><p class="mut" style="margin-top:10px;font-size:17px;line-height:1.6;max-width:460px">' + w[3] + '</p></div>'; }).join('') + '</div>' },
    { k: 'Б', name: 'Фото и четыре причины', d: 'Слева высокое фото стройки с крупной подписью «60 мастеров в штате». Справа четыре причины столбиком с оранжевыми номерами. Меньше цифр, больше доверия через живую картинку.', dk: true, h:
      '<div style="display:grid;grid-template-columns:520px 1fr;gap:90px;align-items:start">' +
      '<div class="shell"><div class="ph ov" style="height:780px"><img src="' + img('site') + '" alt=""><div class="cap"><p class="big" style="font-size:88px">60</p><p style="font:800 24px var(--f);margin-top:6px">мастеров в штате</p><p style="margin-top:8px;opacity:.85">и свой автопарк — заказы не перепродаём</p></div></div></div>' +
      '<div style="padding-top:30px">' + head('Почему FORTE', 'Строим <em>честно</em>') +
      '<ul style="margin-top:52px">' + WY.map(function (w, i) { return '<li style="display:grid;grid-template-columns:80px 1fr;gap:20px;padding:30px 0;border-top:1px solid var(--dline)"><span class="big" style="font-size:38px;color:var(--or)">0' + (i + 1) + '</span><div><b style="font:800 26px var(--f);letter-spacing:-.02em">' + w[2] + '</b><p class="mut" style="margin-top:8px;font-size:17px;line-height:1.6">' + w[3] + '</p></div></li>'; }).join('') + '</ul></div></div>' }
  ]});

  /* ===== 9. Вопросы (светлый) ===== */
  B.push({ t: 'Вопросы', n: 'светлый блок', v: [
    { k: 'А', name: 'Аккордеон и карточка помощи', d: 'Слева заголовок и тёмная карточка «Не нашли ответ?» с кнопкой. Справа пять вопросов, первый раскрыт. Спокойно и привычно — на сайте ничего не прыгает.', dk: false, h:
      '<div style="display:grid;grid-template-columns:440px 1fr;gap:90px;align-items:start">' +
      '<div>' + head('Вопросы', 'Коротко <em>о главном</em>', 'Самое частое, что спрашивают перед стройкой.') +
      '<div class="shell" style="margin-top:44px;background:rgba(13,13,13,.06)"><div class="core" style="padding:34px;background:var(--black);color:#fff"><b style="font:800 26px var(--f)">Не нашли ответ?</b><p style="margin-top:10px;color:var(--dmute);font-size:16px">Инженер перезвонит и ответит на любой вопрос.</p><span class="btn" style="margin-top:28px">Задать вопрос' + A + '</span></div></div></div>' +
      '<ul style="border-top:1px solid var(--line)">' + FQ.map(function (q, i) { return '<li style="padding:32px 0;border-bottom:1px solid var(--line)"><div class="row" style="justify-content:space-between;gap:30px"><b style="font:800 26px/1.25 var(--f);letter-spacing:-.025em;color:' + (i === 0 ? 'var(--or)' : 'var(--ink)') + '">' + q[0] + '</b><span class="arr' + (i === 0 ? '' : ' gh') + '" style="font-size:24px">' + (i === 0 ? '−' : '+') + '</span></div>' + (i === 0 ? '<p style="margin-top:16px;max-width:640px;font-size:18px;line-height:1.6;color:var(--ink2)">' + q[1] + '</p>' : '') + '</li>'; }).join('') + '</ul></div>' },
    { k: 'Б', name: 'Все ответы сразу', d: 'Пять вопросов карточками, ответ виден сразу — ничего не надо нажимать. Шестая карточка оранжевая: «Не нашли ответ? Задать вопрос».', dk: false, h:
      '<div style="text-align:center">' + head('Вопросы', 'Коротко <em>о главном</em>') + '</div>' +
      '<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:64px">' + FQ.map(function (q, i) { return '<div class="shell"><div class="core" style="height:100%;padding:36px 34px"><span class="big" style="font-size:30px;color:var(--or)">0' + (i + 1) + '</span><b style="display:block;margin-top:18px;font:800 23px/1.25 var(--f);letter-spacing:-.02em">' + q[0] + '</b><p style="margin-top:14px;font-size:16px;line-height:1.6;color:var(--ink2)">' + q[1] + '</p></div></div>'; }).join('') +
      '<div class="shell"><div class="core" style="height:100%;padding:36px 34px;background:var(--or);color:#fff;display:flex;flex-direction:column"><b style="font:900 34px/1.1 var(--f);letter-spacing:-.035em">Не нашли<br>ответ?</b><p style="margin-top:14px;font-size:16px;line-height:1.6;opacity:.92">Инженер перезвонит и ответит на любой вопрос.</p><span class="btn wh" style="margin-top:auto;align-self:flex-start">Задать вопрос' + A + '</span></div></div></div>' }
  ]});

  /* ===== 10. Заявка (светлый) ===== */
  var FORM = '<div style="display:grid;grid-template-columns:1fr 1fr;gap:16px"><div class="fld"><span>Имя</span><i>Ваше имя</i></div><div class="fld"><span>Телефон</span><i>+7 (___) ___-__-__</i></div></div><div class="fld" style="margin-top:18px"><span>Что строим</span><div class="row" style="flex-wrap:wrap;gap:8px"><span class="chip" style="height:44px;padding:0 18px;background:var(--ink);color:#fff">Дом под ключ</span><span class="chip" style="height:44px;padding:0 18px;background:var(--bg);color:var(--ink2)">Коттедж</span><span class="chip" style="height:44px;padding:0 18px;background:var(--bg);color:var(--ink2)">Тёплый контур</span><span class="chip" style="height:44px;padding:0 18px;background:var(--bg);color:var(--ink2)">Коммерческое</span></div></div><div class="fld" style="margin-top:18px"><span>Комментарий</span><i style="height:96px;align-items:flex-start;padding-top:18px">Участок, площадь, пожелания</i></div><span class="btn" style="width:100%;justify-content:space-between;margin-top:26px">Получить расчёт' + A + '</span><p class="mut" style="margin-top:14px;font-size:14px;text-align:center">Перезвоним в течение 15 минут в рабочее время</p>';
  B.push({ t: 'Заявка', n: 'светлый блок', v: [
    { k: 'А', name: 'Форма на фото дома', d: 'Слева большое фото дома в сумерках с заголовком «Обсудим ваш дом» и тремя обещаниями. Справа белая форма. Эмоция и действие рядом.', dk: false, h:
      '<div style="display:grid;grid-template-columns:1fr 560px;gap:20px">' +
      '<div class="shell"><div class="ph ov" style="height:100%;min-height:720px"><img src="' + img('dusk2') + '" alt=""><div class="cap" style="left:48px;bottom:48px"><p class="eb" style="color:rgba(255,255,255,.75)">Расчёт за 1 день</p><p style="margin-top:18px;font:900 68px/1.02 var(--f);letter-spacing:-.045em">Обсудим<br>ваш дом</p><ul style="margin-top:30px;display:grid;gap:12px;font-size:18px">' + ['Бесплатный выезд инженера на участок', 'Проект и смета по этапам', 'Цена фиксируется в договоре'].map(function (t) { return '<li class="row" style="gap:14px"><i style="display:grid;place-items:center;width:28px;height:28px;border-radius:50%;background:var(--or);font-style:normal;font-size:14px">✓</i>' + t + '</li>'; }).join('') + '</ul></div></div></div>' +
      '<div class="shell"><div class="core" style="height:100%;padding:44px 40px">' + '<b style="font:900 32px var(--f);letter-spacing:-.03em">Заявка на расчёт</b><p class="mut" style="margin:8px 0 30px">Ответим и договоримся о выезде.</p>' + FORM + '</div></div></div>' },
    { k: 'Б', name: 'Оранжевая плашка', d: 'Большая оранжевая плашка на весь блок: слева крупный заголовок и три обещания, справа белая форма. Самое яркое место сайта — сразу понятно, куда нажать.', dk: false, h:
      '<div class="shell"><div class="core" style="padding:72px;background:radial-gradient(70% 90% at 0 0,#ff8b47,transparent 60%),var(--or);color:#fff;display:grid;grid-template-columns:1fr 540px;gap:72px;align-items:center">' +
      '<div><p class="eb" style="color:rgba(255,255,255,.8)">Расчёт за 1 день</p><p style="margin-top:20px;font:900 84px/1 var(--f);letter-spacing:-.05em">Обсудим<br>ваш дом</p><ul style="margin-top:36px;display:grid;gap:14px;font-size:19px">' + ['Бесплатный выезд инженера на участок', 'Проект и смета по этапам', 'Цена фиксируется в договоре'].map(function (t) { return '<li class="row" style="gap:14px"><i style="display:grid;place-items:center;width:30px;height:30px;border-radius:50%;background:#fff;color:var(--or);font-style:normal;font-size:14px;font-weight:800">✓</i>' + t + '</li>'; }).join('') + '</ul></div>' +
      '<div style="padding:40px;border-radius:30px;background:#fff;color:var(--ink);box-shadow:0 40px 80px -30px rgba(120,40,0,.5)">' + FORM + '</div></div></div>' }
  ]});

  /* ===== 11. Подвал (тёмный) ===== */
  B.push({ t: 'Подвал', n: 'тёмный блок', v: [
    { k: 'А', name: 'Огромное FORTE', d: 'Сверху финальная фраза и кнопка, ниже контакты в четыре колонки. Внизу логотип FORTE на всю ширину экрана — оранжевый, как подпись под сайтом.', dk: true, h:
      '<div style="display:flex;justify-content:space-between;align-items:flex-end;gap:60px"><p style="max-width:780px;font:800 46px/1.15 var(--f);letter-spacing:-.035em">Иногда один правильный подрядчик экономит <span style="color:var(--or)">год нервов и миллионы рублей</span></p><span class="btn">Запросить расчёт' + A + '</span></div>' +
      '<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:24px;margin-top:80px;padding-top:36px;border-top:1px solid var(--dline)">' + [['Телефон', '+7 (000) 000-00-00'], ['Почта', '[почта компании]'], ['Офис', 'Москва, ул. Строителей, 12'], ['Часы', 'Ежедневно 9:00–21:00']].map(function (c) { return '<div><p class="mut" style="font-size:14px">' + c[0] + '</p><b style="display:block;margin-top:8px;font-size:19px">' + c[1] + '</b></div>'; }).join('') + '</div>' +
      '<p style="margin:70px -20px -170px;font:900 380px/0.8 var(--f);letter-spacing:-.07em;color:var(--or);white-space:nowrap">FORTE</p>' },
    { k: 'Б', name: 'Фото дома и контакты', d: 'Подвал на фоне фото дома в сумерках: крупная финальная фраза, кнопка, ниже прозрачные карточки с телефоном, почтой, адресом и часами работы. Сайт заканчивается красиво, а не таблицей ссылок.', dk: true, h:
      '<div style="position:absolute;inset:0"><img src="' + img('hero-dusk') + '" alt="" style="width:100%;height:100%;object-fit:cover;opacity:.55"><i style="position:absolute;inset:0;background:linear-gradient(to top,#0b0b0b 25%,rgba(11,11,11,.4))"></i></div>' +
      '<div style="position:relative;padding-top:120px"><span style="font:900 24px var(--f);letter-spacing:.14em">FORTE</span><p style="margin-top:30px;max-width:860px;font:900 60px/1.06 var(--f);letter-spacing:-.045em">Иногда один правильный подрядчик экономит <span style="color:var(--or)">год нервов</span></p><span class="btn" style="margin-top:40px">Запросить расчёт дома' + A + '</span>' +
      '<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:80px">' + [['Телефон', '+7 (000) 000-00-00'], ['Почта', '[почта компании]'], ['Офис', 'Москва, ул. Строителей, 12'], ['Часы', 'Ежедневно 9:00–21:00']].map(function (c) { return '<div style="padding:24px 26px;border-radius:24px;background:rgba(255,255,255,.07);box-shadow:inset 0 0 0 1px rgba(255,255,255,.1)"><p class="mut" style="font-size:14px">' + c[0] + '</p><b style="display:block;margin-top:8px;font-size:18px">' + c[1] + '</b></div>'; }).join('') + '</div>' +
      '<div class="row" style="justify-content:space-between;margin-top:48px;padding-top:24px;border-top:1px solid var(--dline);font-size:14px;color:var(--dmute)"><span>© FORTE, 2026</span><span>Наверх ↑</span></div></div>' }
  ]});

  var m = document.getElementById('m');
  m.innerHTML = B.map(function (b, i) {
    return '<section class="blk" id="b' + (i + 1) + '"><div class="blk__h"><b>' + (i + 1) + '</b><h2>' + b.t + '</h2><span>' + b.n + '</span></div>' +
      b.v.map(function (v) { return '<div class="var"><div class="var__h"><b>' + (i + 1) + v.k + '</b><strong>' + v.name + '</strong><span>' + v.d + '</span></div><div class="fr"><div class="s' + (v.dk ? ' dk' : '') + '">' + v.h + '</div></div></div>'; }).join('') + '</section>';
  }).join('');
  var fit = function () { document.querySelectorAll('.fr').forEach(function (f) { f.style.setProperty('--z', f.clientWidth / 1440); }); };
  addEventListener('resize', fit); fit();
})();
