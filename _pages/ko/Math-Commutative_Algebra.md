---
title: "가환대수학"
layout: archive_custom
regenerate: true
permalink: /ko/commutative_algebra/
header:
  overlay_color: "transparent"
hero_hue: 231
excerpt: "가환대수학은 가환환과 그 위의 가군을 공부하는 분야이다. 국소화와 준소분해, 차원 이론을 통해 대수기하학의 국소적 토대를 제공한다."
---
{% assign lang = site.locale %}
{% assign lang_prefix = page.url | truncate: 3, "" %}
{% if lang_prefix contains "en" or lang_prefix contains "ko" %}
  {% assign lang = lang_prefix | append: "/" %}
{% endif %}

{% assign posts = site.categories['Math / Commutative Algebra'] | where_exp: "post", "post.permalink contains lang" | sort: 'weight' %}
{% include subject-cards.html posts=posts %}

