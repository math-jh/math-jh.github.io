---
title: "LLM 작업실"
layout: archive_custom
regenerate: true
permalink: /ko/llm_workshop/
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

{% assign cat_posts = site.categories['Misc / LLM Workshop'] %}
{% if cat_posts %}
{% assign posts = cat_posts | where_exp: "post", "post.permalink contains lang" | sort: 'weight' %}
{% else %}
{% assign posts = "" | split: "" %}
{% endif %}
{% include subject-cards.html posts=posts minimal=true splitweight=99 %}
