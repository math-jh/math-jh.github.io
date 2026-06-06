---
title: "환론"
layout: archive_custom
regenerate: true
permalink: /ko/ring_theory/
eyebrow: "대수학"
header:
  overlay_color: "transparent"
hero_hue: 213
excerpt: "환론은 덧셈과 곱셈이 함께 주어진 환과 그 아이디얼을 공부하는 분야이다. 정역과 체로의 확장, 인수분해와 가군을 통해 가환대수와 대수기하의 토대가 된다."
---
{% assign lang = site.locale %}
{% assign lang_prefix = page.url | truncate: 3, "" %}
{% if lang_prefix contains "en" or lang_prefix contains "ko" %}
  {% assign lang = lang_prefix | append: "/" %}
{% endif %}

{% assign posts = site.categories['Math / Ring Theory'] | where_exp: "post", "post.permalink contains lang" | sort: 'weight' %}
{% include subject-cards.html posts=posts %}

