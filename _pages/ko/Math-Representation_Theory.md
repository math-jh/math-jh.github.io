---
title: "표현론"
layout: archive_custom
regenerate: true
permalink: /ko/representation_theory/
eyebrow: "대수학"
header:
  overlay_color: "transparent"
hero_hue: 236
excerpt: "표현론은 군과 대수의 원소를 선형변환으로 실현하여 그 구조를 공부하는 분야이다. 기약표현과 지표, 가중치를 통해 대칭을 선형대수의 언어로 분석한다."
---
{% assign lang = site.locale %}
{% assign lang_prefix = page.url | truncate: 3, "" %}
{% if lang_prefix contains "en" or lang_prefix contains "ko" %}
  {% assign lang = lang_prefix | append: "/" %}
{% endif %}

{% assign cat_posts = site.categories['Math / Representation Theory'] %}
{% if cat_posts %}
{% assign posts = cat_posts | where_exp: "post", "post.permalink contains lang" | sort: 'weight' %}
{% else %}
{% assign posts = "" | split: "" %}
{% endif %}
{% include subject-cards.html posts=posts %}

