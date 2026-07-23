---
title: "기호 찾아보기"
layout: archive_custom
regenerate: true
permalink: /ko/notations
close_button: false
published: false
---

블로그에서 사용하는 기호와 표기를 카테고리별로 정리해둔 페이지입니다. 관례 문자는 대략적인 관례이며 엄격히 지켜지지는 않습니다.

<div class="term-index term-index--notation">
  <div class="term-index__bar">
    <nav class="term-index__letters" aria-label="카테고리 바로가기">
      {%- for g in site.data.notations -%}
      <a href="#ntn-{{ g.category }}">{{ g.title }}</a>
      {%- endfor -%}
    </nav>
    <label class="term-index__search">
      <svg viewBox="0 0 16 16" width="13" height="13" aria-hidden="true"><circle cx="7" cy="7" r="4.2" fill="none" stroke="currentColor" stroke-width="1.4"/><line x1="10.2" y1="10.2" x2="14" y2="14" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/></svg>
      <input class="term-index__filter" type="search" name="search" placeholder="기호 검색 (기호/의미)" aria-label="기호 검색" autocomplete="off" autocorrect="off" autocapitalize="none" spellcheck="false" data-1p-ignore data-lpignore="true" data-bwignore data-form-type="other">
    </label>
  </div>

  {%- for g in site.data.notations %}
  <section class="term-index__section" id="ntn-{{ g.category }}">
    <h2 class="term-index__heading">{{ g.title }}</h2>
    {%- if g.conventions and g.conventions != empty %}
    <p class="term-index__sublabel">관례 문자</p>
    <ul class="term-index__list">
      {%- for n in g.conventions %}
      <li class="term-index__entry{% unless n.defs and n.defs != empty %} term-index__entry--bare{% endunless %}" data-search="{{ n.symbol | remove: '\' | downcase }} {{ n.meaning | remove: '$' | downcase }}">
        <span class="term-index__t">
          <b class="term-index__term">${{ n.symbol }}$</b><span class="term-index__alt"> · {{ n.meaning }}</span>
        </span><span class="term-index__lead"></span>
        {%- if n.defs and n.defs != empty -%}
        <span class="term-index__defs">
          {%- for d in n.defs -%}
          <a href="{{ d.url }}">{{ d.label }}</a>{% unless forloop.last %} · {% endunless %}
          {%- endfor -%}
        </span>
        {%- endif -%}
      </li>
      {%- endfor %}
    </ul>
    <p class="term-index__sublabel">표기법</p>
    {%- endif %}
    <ul class="term-index__list">
      {%- for n in g.items %}
      <li class="term-index__entry{% unless n.defs and n.defs != empty %} term-index__entry--bare{% endunless %}" data-search="{{ n.symbol | remove: '\' | downcase }} {{ n.meaning | remove: '$' | downcase }}">
        <span class="term-index__t">
          <b class="term-index__term">${{ n.symbol }}$</b><span class="term-index__alt"> · {{ n.meaning }}</span>
        </span><span class="term-index__lead"></span>
        {%- if n.defs and n.defs != empty -%}
        <span class="term-index__defs">
          {%- for d in n.defs -%}
          <a href="{{ d.url }}">{{ d.label }}</a>{% unless forloop.last %} · {% endunless %}
          {%- endfor -%}
        </span>
        {%- endif -%}
      </li>
      {%- endfor %}
    </ul>
  </section>
  {%- endfor %}

  <p class="term-index__empty" hidden>일치하는 기호가 없습니다.</p>
</div>

<script>
(function () {
  var input = document.querySelector('.term-index__filter');
  if (!input) return;
  var entries  = [].slice.call(document.querySelectorAll('.term-index__entry'));
  var sections = [].slice.call(document.querySelectorAll('.term-index__section'));
  var empty    = document.querySelector('.term-index__empty');
  var bar      = document.querySelector('.term-index__bar');
  var letters  = {};
  [].slice.call(document.querySelectorAll('.term-index__letters a')).forEach(function (a) {
    letters[a.getAttribute('href').slice(1)] = a;
  });

  // 필터: 기호(백슬래시 제거)·의미 부분일치. 절이 통째로 비면 카테고리도 흐려진다.
  input.addEventListener('input', function () {
    var q = input.value.trim().toLowerCase();
    var any = false;
    entries.forEach(function (li) {
      var hit = !q || li.getAttribute('data-search').indexOf(q) !== -1;
      li.hidden = !hit;
      if (hit) any = true;
    });
    sections.forEach(function (sec) {
      sec.hidden = !!q && !sec.querySelector('.term-index__entry:not([hidden])');
      var a = letters[sec.id];
      if (a) a.classList.toggle('is-dim', sec.hidden);
    });
    empty.hidden = any;
    spy();
  });

  // 앵커 착지점: sticky 바에 가리지 않도록 실측 높이를 --term-bar-h 로 넘긴다
  // (SCSS 의 scroll-margin-top 이 이 변수를 읽는다). 바는 폭에 따라 여러 줄로
  // 접히고 글꼴 로드 뒤에도 높이가 변하므로 ResizeObserver 로 따라간다.
  function syncBarHeight() {
    document.documentElement.style.setProperty('--term-bar-h', (bar.offsetHeight + 8) + 'px');
  }
  syncBarHeight();
  if (window.ResizeObserver) new ResizeObserver(syncBarHeight).observe(bar);
  else window.addEventListener('resize', syncBarHeight, { passive: true });

  // 스크롤 스파이: sticky 바 바로 아래에 걸린 절의 카테고리를 진하게
  var active = null;
  function spy() {
    var line = bar.getBoundingClientRect().bottom + 10;
    var cur = null;
    for (var i = 0; i < sections.length; i++) {
      if (sections[i].hidden) continue;
      if (sections[i].getBoundingClientRect().top <= line) cur = sections[i];
      else break;
    }
    var id = cur ? cur.id : null;
    if (id === active) return;
    if (active && letters[active]) letters[active].classList.remove('is-active');
    if (id && letters[id]) letters[id].classList.add('is-active');
    active = id;
  }
  var ticking = false;
  window.addEventListener('scroll', function () {
    if (ticking) return;
    ticking = true;
    requestAnimationFrame(function () { ticking = false; spy(); });
  }, { passive: true });
  spy();
})();
</script>
