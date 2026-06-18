---
title: "미적분학"
category: "Math / Calculus"
layout: archive_custom
regenerate: true
permalink: /ko/calculus/
eyebrow: "교양수학"
header:
  overlay_color: "transparent"
hero_hue: 281
excerpt: "미적분학은 함수의 변화율과 누적, 즉 미분과 적분을 다루는 분야이다. 극한에서 출발해 도함수와 적분, 급수를 통해 변화를 정량적으로 분석한다."
---
{% assign lang = site.locale %}
{% assign lang_prefix = page.url | truncate: 3, "" %}
{% if lang_prefix contains "en" or lang_prefix contains "ko" %}
  {% assign lang = lang_prefix | append: "/" %}
{% endif %}

{% assign cat_posts = site.categories['Math / Calculus'] %}
{% if cat_posts %}
{% assign posts = cat_posts | where_exp: "post", "post.permalink contains lang" | sort: 'weight' %}
{% else %}
{% assign posts = "" | split: "" %}
{% endif %}
{% include subject-cards.html posts=posts %}

