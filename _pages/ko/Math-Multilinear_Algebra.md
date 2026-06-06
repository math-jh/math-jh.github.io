---
title: "다중선형대수학"
layout: archive_custom
regenerate: true
permalink: /ko/multilinear_algebra/
eyebrow: "대수학"
header:
  overlay_color: "transparent"
hero_hue: 218
excerpt: "다중선형대수학은 여러 벡터에 대해 선형인 사상, 즉 텐서를 공부하는 분야로, 이를 위해 우리는 일반적인 환 위에서의 선형대수 이론을 전개하고, 텐서곱과 외대수·대칭대수를 통해 미분기하와 표현론의 도구를 마련한다."
---
{% assign lang = site.locale %}
{% assign lang_prefix = page.url | truncate: 3, "" %}
{% if lang_prefix contains "en" or lang_prefix contains "ko" %}
  {% assign lang = lang_prefix | append: "/" %}
{% endif %}

{% assign posts = site.categories['Math / Multilinear Algebra'] | where_exp: "post", "post.permalink contains lang" | sort: 'weight' %}
{% include subject-cards.html posts=posts %}

