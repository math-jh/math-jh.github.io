---
title: "선형대수학"
layout: archive_custom
regenerate: true
permalink: /ko/linear_algebra/
eyebrow: "교양수학"
header:
  overlay_color: "transparent"
hero_hue: 249
excerpt: "선형대수학은 벡터공간과 선형사상을 공부하는 분야이다. 기저와 차원에서 시작해 행렬 표현·고유공간 분해·쌍대공간으로 이어지며, 이후 거의 모든 수학에서 쓰이는 기본 언어를 다진다."
---
{% assign lang = site.locale %}
{% assign lang_prefix = page.url | truncate: 3, "" %}
{% if lang_prefix contains "en" or lang_prefix contains "ko" %}
  {% assign lang = lang_prefix | append: "/" %}
{% endif %}

{% assign cat_posts = site.categories['Math / Linear Algebra'] %}
{% if cat_posts %}
{% assign posts = cat_posts | where_exp: "post", "post.permalink contains lang" | sort: 'weight' %}
{% else %}
{% assign posts = "" | split: "" %}
{% endif %}
{% include subject-cards.html posts=posts %}
