---
title: "리 이론"
layout: archive_custom
regenerate: true
permalink: /ko/lie_theory/
header:
  overlay_color: "transparent"
hero_hue: 100
excerpt: "리 이론은 연속적 대칭을 담는 리 군과, 그 무한소 구조인 리 대수를 공부하는 분야이다. 지수사상과 근계·가중치를 통해 기하와 표현론을 잇는다."
---
{% assign lang = site.locale %}
{% assign lang_prefix = page.url | truncate: 3, "" %}
{% if lang_prefix contains "en" or lang_prefix contains "ko" %}
  {% assign lang = lang_prefix | append: "/" %}
{% endif %}

{% assign posts = site.categories['Math / Lie Theory'] | where_exp: "post", "post.permalink contains lang" | sort: 'weight' %}
{% include subject-cards.html posts=posts %}

