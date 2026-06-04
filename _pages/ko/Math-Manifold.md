---
title: "미분다양체"
layout: archive_custom
regenerate: true
permalink: /ko/manifold/
header:
  overlay_color: "transparent"
hero_hue: 84
excerpt: "미분다양체는 국소적으로 유클리드 공간처럼 보이는 공간 위에서 미적분을 전개하는 분야이다. 접공간과 벡터장, 미분형식을 통해 기하와 물리의 무대를 세운다."
---
{% assign lang = site.locale %}
{% assign lang_prefix = page.url | truncate: 3, "" %}
{% if lang_prefix contains "en" or lang_prefix contains "ko" %}
  {% assign lang = lang_prefix | append: "/" %}
{% endif %}

{% assign posts = site.categories['Math / Manifold'] | where_exp: "post", "post.permalink contains lang" | sort: 'weight' %}
{% include subject-cards.html posts=posts %}

