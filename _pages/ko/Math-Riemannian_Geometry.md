---
title: "리만기하학"
layout: archive_custom
regenerate: true
permalink: /ko/riemannian_geometry/
eyebrow: "미분기하학"
header:
  overlay_color: "transparent"
hero_hue: 116
excerpt: "리만기하학은 다양체에 길이와 각을 재는 리만계량을 부여하고 그 곡률을 공부하는 분야이다. 측지선과 곡률 텐서를 통해 휘어진 공간의 기하를 다룬다."
---
{% assign lang = site.locale %}
{% assign lang_prefix = page.url | truncate: 3, "" %}
{% if lang_prefix contains "en" or lang_prefix contains "ko" %}
  {% assign lang = lang_prefix | append: "/" %}
{% endif %}

{% assign posts = site.categories['Math / Riemannian Geometry'] | where_exp: "post", "post.permalink contains lang" | sort: 'weight' %}
{% include subject-cards.html posts=posts %}

