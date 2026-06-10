---
title: "스킴"
layout: archive_custom
regenerate: true
permalink: /ko/scheme_theory/
eyebrow: "대수학"
header:
  overlay_color: "transparent"
hero_hue: 25
excerpt: "스킴 이론은 가환환을 기하적 공간으로 바라보는 그로텐디크의 언어이다. 스펙트럼과 구조층, 사상을 통해 대수적 다양체를 현대적 언어로 다시 번역한다."
---
{% assign lang = site.locale %}
{% assign lang_prefix = page.url | truncate: 3, "" %}
{% if lang_prefix contains "en" or lang_prefix contains "ko" %}
  {% assign lang = lang_prefix | append: "/" %}
{% endif %}

{% assign cat_posts = site.categories['Math / Scheme Theory'] %}
{% if cat_posts %}
{% assign posts = cat_posts | where_exp: "post", "post.permalink contains lang" | sort: 'weight' %}
{% else %}
{% assign posts = "" | split: "" %}
{% endif %}
{% include subject-cards.html posts=posts %}

