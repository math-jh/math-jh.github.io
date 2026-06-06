---
title: "집합론"
layout: archive_custom
regenerate: true
permalink: /ko/set_theory/
eyebrow: "수학기초론"
header:
  overlay_color: "transparent"
hero_hue: 274
excerpt: "집합론은 집합과 그 위의 연산, 그리고 무한을 다루는 수학의 토대이다. 관계와 함수, 순서수와 기수, 선택공리를 거치며 이후 모든 분야가 딛고 설 근간이 된다."
---
{% assign lang = site.locale %}
{% assign lang_prefix = page.url | truncate: 3, "" %}
{% if lang_prefix contains "en" or lang_prefix contains "ko" %}
  {% assign lang = lang_prefix | append: "/" %}
{% endif %}

{% assign posts = site.categories['Math / Set Theory'] | where_exp: "post", "post.permalink contains lang" | sort: 'weight' %}
{% include subject-cards.html posts=posts %}

