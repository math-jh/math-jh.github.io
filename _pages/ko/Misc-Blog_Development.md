---
title: "블로그 개발"
layout: archive_custom
regenerate: true
permalink: /ko/blog_development/
header:
  overlay_image: /assets/images/Misc/Blog_Development/Blog_Development.png
  overlay_filter: 0.5
excerpt: "블로그를 만들고 다듬으며 마주친 문제와 해결 과정을 기록합니다. Jekyll 설정부터 디자인과 자동화까지, 개발일지 형태로 남깁니다."
---
{% assign lang = site.locale %}
{% assign lang_prefix = page.url | truncate: 3, "" %}
{% if lang_prefix contains "en" or lang_prefix contains "ko" %}
  {% assign lang = lang_prefix | append: "/" %}
{% endif %}

{% assign posts = site.categories['Misc / Blog Development'] | where_exp: "post", "post.permalink contains lang" | sort: 'weight' %}
{% include subject-cards.html posts=posts minimal=true %}