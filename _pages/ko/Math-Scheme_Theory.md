---
title: "스킴"
layout: archive_custom
regenerate: true
permalink: /ko/scheme_theory/
header:
  overlay_image: /assets/images/Math/Scheme_Theory/Scheme_Theory.png
  overlay_filter: 0.5
excerpt: "스킴 이론은 가환환을 기하적 공간으로 바라보는 그로텐디크의 언어이다. 스펙트럼과 구조층, 사상을 통해 대수기하를 현대적 토대 위에 다시 세운다."
---
{% assign lang = site.locale %}
{% assign lang_prefix = page.url | truncate: 3, "" %}
{% if lang_prefix contains "en" or lang_prefix contains "ko" %}
  {% assign lang = lang_prefix | append: "/" %}
{% endif %}

{% assign posts = site.categories['Math / Scheme Theory'] | where_exp: "post", "post.permalink contains lang" | sort: 'weight' %}
{% include subject-cards.html posts=posts %}

