---
title: "거울대칭"
layout: archive_custom
regenerate: true
permalink: /ko/mirror_symmetry/
header:
  overlay_image: /assets/images/Math/Mirror_Symmetry/Mirror_Symmetry.png
  overlay_filter: 0.5
excerpt: "거울대칭은 한 칼라비-야우 다양체의 심플렉틱 기하가 다른 다양체의 복소기하와 대응한다는 현상을 공부하는 분야이다. 끈 이론에서 출발해 열거기하와 호몰로지 대수를 잇는다."
---
{% assign lang = site.locale %}
{% assign lang_prefix = page.url | truncate: 3, "" %}
{% if lang_prefix contains "en" or lang_prefix contains "ko" %}
  {% assign lang = lang_prefix | append: "/" %}
{% endif %}

{% assign posts = site.categories['Math / Mirror Symmetry'] | where_exp: "post", "post.permalink contains lang" | sort: 'weight' %}
{% include subject-cards.html posts=posts %}

