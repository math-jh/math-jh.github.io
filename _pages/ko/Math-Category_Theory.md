---
title: "범주론"
layout: archive_custom
regenerate: true
permalink: /ko/category_theory/
eyebrow: "수학기초론"
header:
  overlay_color: "transparent"
hero_hue: 306
excerpt: "범주론은 대상과 사상, 그리고 그 사이의 보편성질을 통해 수학적 구조를 추상적으로 다루는 분야이다. 함자와 자연변환, 극한과 수반을 통해 서로 다른 분야를 하나의 언어로 통합한다."
---
{% assign lang = site.locale %}
{% assign lang_prefix = page.url | truncate: 3, "" %}
{% if lang_prefix contains "en" or lang_prefix contains "ko" %}
  {% assign lang = lang_prefix | append: "/" %}
{% endif %}

{% assign cat_posts = site.categories['Math / Category Theory'] %}
{% if cat_posts %}
{% assign posts = cat_posts | where_exp: "post", "post.permalink contains lang" | sort: 'weight' %}
{% else %}
{% assign posts = "" | split: "" %}
{% endif %}
{% include subject-cards.html posts=posts %}

