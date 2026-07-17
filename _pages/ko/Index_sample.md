---
title: "찾아보기 (조판 샘플)"
layout: archive_custom
regenerate: true
sitemap: false
permalink: /ko/misc/index_sample
---

블로그에서 사용한 용어들을 정리해둔 페이지입니다. 굵은 쪽이 본문에서 주로 쓰는 표기입니다.

<div class="term-index">
  <div class="term-index__bar">
    <nav class="term-index__letters" aria-label="알파벳 바로가기">
      {%- for pair in site.data.terms -%}
      <a href="#idx-{{ pair[0] }}">{{ pair[0] }}</a>
      {%- endfor -%}
    </nav>
    <input class="term-index__filter" type="search" placeholder="필터 (영문·한글)" aria-label="용어 필터">
  </div>

  {%- for pair in site.data.terms %}
  <section class="term-index__section" id="idx-{{ pair[0] }}">
    <h2 class="term-index__letter"><span>{{ pair[0] }}</span></h2>
    <ul class="term-index__list">
      {%- for t in pair[1] %}
      <li class="term-index__entry{% unless t.defs or t.refs %} term-index__entry--bare{% endunless %}" id="{{ t.id }}" data-search="{{ t.en | remove: '$' | downcase }} {{ t.ko | remove: '$' }}">
        <span class="term-index__t">
          {%- if t.primary == "ko" -%}
          <span class="term-index__alt">{{ t.en }} · </span><b class="term-index__term">{{ t.ko }}</b>
          {%- else -%}
          <b class="term-index__term">{{ t.en }}</b><span class="term-index__alt"> · {{ t.ko }}</span>
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
    });
    empty.hidden = any;
  });
})();
</script>
