---
title: "사교기하학"
layout: archive_custom
regenerate: true
permalink: /ko/symplectic_geometry/
eyebrow: "거울대칭"
header:
  overlay_color: "transparent"
hero_hue: 1
excerpt: "사교기하학은 사교형식이 주어진 다양체 위에서 고전역학의 위상공간을 기하적으로 공부하는 분야이다. 이는 거울대칭의 한쪽 면을 이루는 토대이다."
---
{% assign lang = site.locale %}
{% assign lang_prefix = page.url | truncate: 3, "" %}
{% if lang_prefix contains "en" or lang_prefix contains "ko" %}
  {% assign lang = lang_prefix | append: "/" %}
{% endif %}

{% assign posts = site.categories['Math / Symplectic Geometry'] | where_exp: "post", "post.permalink contains lang" | sort: 'weight' %}
{% include subject-cards.html posts=posts %}

