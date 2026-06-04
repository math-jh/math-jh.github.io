---
title: "대수다양체"
layout: archive_custom
regenerate: true
permalink: /ko/algebraic_varieties/
header:
  overlay_color: "transparent"
hero_hue: 9
excerpt: "대수다양체는 다항식의 영점으로 정의되는 기하적 대상을 공부하는 분야이다. 사영다양체와 차원·매끄러움, 인자를 통해 대수와 기하를 잇는 다리가 된다."
---
{% assign lang = site.locale %}
{% assign lang_prefix = page.url | truncate: 3, "" %}
{% if lang_prefix contains "en" or lang_prefix contains "ko" %}
  {% assign lang = lang_prefix | append: "/" %}
{% endif %}

{% assign posts = site.categories['Math / Algebraic Varieties'] | where_exp: "post", "post.permalink contains lang" | sort: 'weight' %}
{% include subject-cards.html posts=posts %}

