---
title: "주변기기"
layout: archive_custom
regenerate: true
permalink: /ko/peripherals
eyebrow: "기타"
header:
  overlay_color: "transparent"
hero_hue: 0
hero_sat: "0%"
---
{% assign lang = site.locale %}
{% assign lang_prefix = page.url | truncate: 3, "" %}
{% if lang_prefix contains "en" or lang_prefix contains "ko" %}
  {% assign lang = lang_prefix | append: "/" %}
{% endif %}

## 키보드
{% assign kb = site.categories['Misc / Peripherals'] | where_exp: "post", "post.permalink contains lang" | where_exp: "post", "post.permalink contains '/keyboards/'" | sort: 'weight' %}
{% include subject-cards.html posts=kb minimal=true %}

## 도구
{% assign tl = site.categories['Misc / Peripherals'] | where_exp: "post", "post.permalink contains lang" | where_exp: "post", "post.permalink contains '/tools/'" | sort: 'weight' %}
{% include subject-cards.html posts=tl minimal=true %}
