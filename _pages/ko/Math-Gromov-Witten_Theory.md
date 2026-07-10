---
title: "그로모프-위튼 이론"
category: "Math / Gromov-Witten Theory"
layout: archive_custom
regenerate: true
permalink: /ko/gromov-witten_theory/
eyebrow: "거울대칭"
header:
  overlay_color: "transparent"
hero_hue: 48
excerpt: "그로모프-위튼 이론은 대상 공간 안의 안정사상 moduli 위에서 virtual fundamental class를 잡아 곡선의 개수를 세는 분야이다. Perfect obstruction theory와 log 기하를 통해 열거기하의 불변량을 엄밀하게 정의한다."
---
{% assign lang = site.locale %}
{% assign lang_prefix = page.url | truncate: 3, "" %}
{% if lang_prefix contains "en" or lang_prefix contains "ko" %}
  {% assign lang = lang_prefix | append: "/" %}
{% endif %}

{% assign cat_posts = site.categories['Math / Gromov-Witten Theory'] %}
{% if cat_posts %}
{% assign posts = cat_posts | where_exp: "post", "post.permalink contains lang" | sort: 'weight' %}
{% else %}
{% assign posts = "" | split: "" %}
{% endif %}
{% include subject-cards.html posts=posts %}
