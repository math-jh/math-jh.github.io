---
title: "호몰로지 대수학"
layout: archive_custom
regenerate: true
permalink: /ko/homological_algebra/
header:
  overlay_color: "transparent"
hero_hue: 227
excerpt: "호몰로지 대수학은 사슬복합체와 그 호몰로지를 통해 대수적 구조의 성질을 측정하는 분야이다. 완전열과 유도함자, Ext와 Tor를 통해 위상·기하·대수를 잇는다."
---
{% assign lang = site.locale %}
{% assign lang_prefix = page.url | truncate: 3, "" %}
{% if lang_prefix contains "en" or lang_prefix contains "ko" %}
  {% assign lang = lang_prefix | append: "/" %}
{% endif %}

{% assign posts = site.categories['Math / Homological Algebra'] | where_exp: "post", "post.permalink contains lang" | sort: 'weight' %}
{% include subject-cards.html posts=posts %}

