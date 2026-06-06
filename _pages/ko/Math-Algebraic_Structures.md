---
title: "대수적 구조"
layout: archive_custom
regenerate: true
permalink: /ko/algebraic_structures/
eyebrow: "대수학"
header:
  overlay_color: "transparent"
hero_hue: 204
excerpt: "대수적 구조는 군·환·가군과 같이 연산이 주어진 집합들을 통합적으로 공부하는 분야이다. 준동형사상과 몫구조를 중심으로, 대부분의 대수구조들이 공유하는 기초를 세운다."
---
{% assign lang = site.locale %}
{% assign lang_prefix = page.url | truncate: 3, "" %}
{% if lang_prefix contains "en" or lang_prefix contains "ko" %}
  {% assign lang = lang_prefix | append: "/" %}
{% endif %}

{% assign posts = site.categories['Math / Algebraic Structures'] | where_exp: "post", "post.permalink contains lang" | sort: 'weight' %}
{% include subject-cards.html posts=posts %}

