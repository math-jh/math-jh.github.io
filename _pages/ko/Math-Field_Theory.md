---
title: "체론"
layout: archive_custom
regenerate: true
permalink: /ko/field_theory/
eyebrow: "대수학"
header:
  overlay_color: "transparent"
hero_hue: 222
excerpt: "체론은 사칙연산이 자유로운 체와 그 확장을 공부하는 분야이다. 갈루아 이론을 통해 다항식의 가해성과 작도 문제를 대칭의 언어로 풀어낸다."
---
{% assign lang = site.locale %}
{% assign lang_prefix = page.url | truncate: 3, "" %}
{% if lang_prefix contains "en" or lang_prefix contains "ko" %}
  {% assign lang = lang_prefix | append: "/" %}
{% endif %}

{% assign cat_posts = site.categories['Math / Field Theory'] %}
{% if cat_posts %}
{% assign posts = cat_posts | where_exp: "post", "post.permalink contains lang" | sort: 'weight' %}
{% else %}
{% assign posts = "" | split: "" %}
{% endif %}
{% include subject-cards.html posts=posts %}

