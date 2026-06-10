---
title: "위상수학"
layout: archive_custom
regenerate: true
permalink: /ko/topology/
eyebrow: "위상수학"
header:
  overlay_color: "transparent"
hero_hue: 124
excerpt: "위상수학은 연속성과 근방의 개념만으로 공간의 성질을 공부하는 분야이다. 연결성·컴팩트성·분리공리를 통해 해석학과 기하학의 토대를 마련한다."
---
{% assign lang = site.locale %}
{% assign lang_prefix = page.url | truncate: 3, "" %}
{% if lang_prefix contains "en" or lang_prefix contains "ko" %}
  {% assign lang = lang_prefix | append: "/" %}
{% endif %}

{% assign cat_posts = site.categories['Math / Topology'] %}
{% if cat_posts %}
{% assign posts = cat_posts | where_exp: "post", "post.permalink contains lang" | sort: 'weight' %}
{% else %}
{% assign posts = "" | split: "" %}
{% endif %}
{% include subject-cards.html posts=posts %}

