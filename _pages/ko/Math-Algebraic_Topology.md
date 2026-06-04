---
title: "대수적 위상수학"
layout: archive_custom
regenerate: true
permalink: /ko/algebraic_topology/
header:
  overlay_color: "transparent"
hero_hue: 156
excerpt: "대수적 위상수학은 공간에 군·환 같은 대수적 불변량을 대응시켜 그 모양을 구별하는 분야이다. 호모토피와 호몰로지·코호몰로지를 통해 위상적 정보를 대수로 번역한다."
---
{% assign lang = site.locale %}
{% assign lang_prefix = page.url | truncate: 3, "" %}
{% if lang_prefix contains "en" or lang_prefix contains "ko" %}
  {% assign lang = lang_prefix | append: "/" %}
{% endif %}

{% assign posts = site.categories['Math / Algebraic Topology'] | where_exp: "post", "post.permalink contains lang" | sort: 'weight' %}
{% include subject-cards.html posts=posts %}

