---
title: "Calculus"
layout: archive_custom
regenerate: true
permalink: /en/calculus/
header:
  overlay_color: "transparent"
hero_hue: 281
excerpt: "Calculus studies the rates of change and accumulation of functions, namely differentiation and integration. Starting from limits, it analyzes change quantitatively through derivatives, integrals, and series."
---
{% assign lang = site.locale %}
{% assign lang_prefix = page.url | truncate: 3, "" %}
{% if lang_prefix contains "en" or lang_prefix contains "ko" %}
  {% assign lang = lang_prefix | append: "/" %}
{% endif %}

{% assign cat_posts = site.categories['Math / Calculus'] %}
{% if cat_posts %}
{% assign posts = cat_posts | where_exp: "post", "post.permalink contains lang" | sort: 'weight' %}
{% else %}
{% assign posts = "" | split: "" %}
{% endif %}
{% include subject-cards.html posts=posts %}
