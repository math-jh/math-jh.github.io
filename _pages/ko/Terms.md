---
title: "찾아보기"
layout: archive_custom
regenerate: true
permalink: /ko/terms
close_button: false
---

블로그에서 사용한 용어들을 정리해둔 페이지입니다. 굵은 쪽이 본문에서 주로 쓰는 표기입니다.

<div class="term-index">
  <div class="term-index__bar">
    <nav class="term-index__letters" aria-label="알파벳 바로가기">
      {%- for pair in site.data.terms -%}
      {%- if pair[1] and pair[1] != empty -%}
      <a href="#idx-{{ pair[0] }}">{{ pair[0] }}</a>
      {%- endif -%}
      {%- endfor -%}
    </nav>
    <label class="term-index__search">
      <svg viewBox="0 0 16 16" width="13" height="13" aria-hidden="true"><circle cx="7" cy="7" r="4.2" fill="none" stroke="currentColor" stroke-width="1.4"/><line x1="10.2" y1="10.2" x2="14" y2="14" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/></svg>
      <input class="term-index__filter" type="search" name="search" placeholder="용어 검색 (한글/영어)" aria-label="용어 검색" autocomplete="off" autocorrect="off" autocapitalize="none" spellcheck="false" data-1p-ignore data-lpignore="true" data-bwignore data-form-type="other">
    </label>
  </div>

  {%- for pair in site.data.terms %}
  {%- if pair[1] and pair[1] != empty %}
  <section class="term-index__section" id="idx-{{ pair[0] }}">
    <h2 class="term-index__letter"><span>{{ pair[0] }}</span></h2>
    <ul class="term-index__list">
      {%- for t in pair[1] %}
      <li class="term-index__entry{% unless t.defs or t.refs %} term-index__entry--bare{% endunless %}" id="{{ t.id }}" data-search="{{ t.en | remove: '$' | downcase | escape }} {{ t.ko | remove: '$' | escape }}{% if t.alias %} {{ t.alias | join: ' ' | remove: '$' | escape }}{% endif %}">
        <span class="term-index__t">
          {%- if t.primary == "ko" -%}
          <span class="term-index__alt">{{ t.en }} · </span><b class="term-index__term">{{ t.ko }}</b>
          {%- else -%}
          <b class="term-index__term">{{ t.en }}</b>{% if t.ko and t.ko != "" %}<span class="term-index__alt"> · {{ t.ko }}</span>{% endif %}
          {%- endif -%}
        </span><span class="term-index__lead"></span>
        {%- if t.defs -%}
        <span class="term-index__defs">
          {%- for d in t.defs -%}
          <a href="{{ d.url }}">{{ d.label }}</a>{% unless forloop.last %} · {% endunless %}
          {%- endfor -%}
        </span>
        {%- endif -%}
        {%- if t.refs -%}
        <span class="term-index__refs">
          {%- for d in t.refs -%}
          <a href="{{ d.url }}">{{ d.label }}</a>{% unless forloop.last %} · {% endunless %}
          {%- endfor -%}
        </span>
        {%- endif -%}
        {%- if t.see -%}
        <span class="term-index__see">
          {%- for s in t.see -%}
          <a href="#{{ s.id }}">{% if s.lang == "ko" %}<em-ko>{{ s.label }}</em-ko>{% else %}<i>{{ s.label }}</i>{% endif %}</a>{% unless forloop.last %}, {% endunless %}
          {%- endfor -%}
        </span>
        {%- endif -%}
      </li>
      {%- endfor %}
    </ul>
  </section>
  {%- endif %}
  {%- endfor %}

  <p class="term-index__empty" hidden>일치하는 용어가 없습니다.</p>
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

  // 필터: 표제어(영문·한글) 부분일치. 절이 통째로 비면 그 글자도 흐려진다.
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
  // (SCSS 의 scroll-margin-top 이 이 변수를 읽는다). 바는 폭에 따라 두 줄로
  // 접히고 글꼴 로드 뒤에도 높이가 변하므로 ResizeObserver 로 따라간다.
  function syncBarHeight() {
    document.documentElement.style.setProperty('--term-bar-h', (bar.offsetHeight + 8) + 'px');
  }
  syncBarHeight();
  if (window.ResizeObserver) new ResizeObserver(syncBarHeight).observe(bar);
  else window.addEventListener('resize', syncBarHeight, { passive: true });

  // 스크롤 스파이: sticky 바 바로 아래에 걸린 절의 글자를 진하게
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
