---
title: "토릭 기하학"
layout: archive_custom
regenerate: true
permalink: /ko/toric_geometry/
eyebrow: "대수기하학"
header:
  overlay_color: "transparent"
hero_hue: 41
excerpt: "토릭기하학은 부채(fan)와 같은 조합적 자료로 기술되는 토릭다양체를 공부하는 분야이다. 격자와 콘의 조합론을 통해 대수기하의 풍부하고, 계산가능한 예시를 제공한다."
---
{% assign lang = site.locale %}
{% assign lang_prefix = page.url | truncate: 3, "" %}
{% if lang_prefix contains "en" or lang_prefix contains "ko" %}
  {% assign lang = lang_prefix | append: "/" %}
{% endif %}

{% assign cat_posts = site.categories['Math / Toric Geometry'] %}
{% if cat_posts %}
{% assign posts = cat_posts | where_exp: "post", "post.permalink contains lang" | sort: 'weight' %}
{% else %}
{% assign posts = "" | split: "" %}
{% endif %}
{% include subject-cards.html posts=posts %}

