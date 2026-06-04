---
title: "군론"
layout: archive_custom
regenerate: true
permalink: /ko/group_theory/
header:
  overlay_image: /assets/images/Math/Group_Theory/Group_Theory.png
  overlay_filter: 0.5
excerpt: "군론은 대칭을 대수적으로 포착하는 군과 그 작용을 공부하는 분야이다. 부분군과 정규부분군, 군의 작용과 실로우 정리를 거쳐 구조의 분류로 나아간다."
---
{% assign lang = site.locale %}
{% assign lang_prefix = page.url | truncate: 3, "" %}
{% if lang_prefix contains "en" or lang_prefix contains "ko" %}
  {% assign lang = lang_prefix | append: "/" %}
{% endif %}

{% assign posts = site.categories['Math / Group Theory'] | where_exp: "post", "post.permalink contains lang" | sort: 'weight' %}
{% include subject-cards.html posts=posts %}

