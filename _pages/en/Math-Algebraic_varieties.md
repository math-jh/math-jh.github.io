---
title: "Algebraic Varieties"
layout: archive_custom
regenerate: true
permalink: /en/algebraic_varieties/
header:
  overlay_color: "transparent"
hero_hue: 9
excerpt: "The theory of algebraic varieties studies geometric objects defined as the zero sets of polynomials. Through projective varieties, dimension, smoothness, and divisors, it connects algebra and geometry."
---
{% assign lang = site.locale %}
{% assign lang_prefix = page.url | truncate: 3, "" %}
{% if lang_prefix contains "en" or lang_prefix contains "ko" %}
  {% assign lang = lang_prefix | append: "/" %}
{% endif %}

{% assign cat_posts = site.categories['Math / Algebraic Varieties'] %}
{% if cat_posts %}
{% assign posts = cat_posts | where_exp: "post", "post.permalink contains lang" | sort: 'weight' %}
{% else %}
{% assign posts = "" | split: "" %}
{% endif %}
{% include subject-cards.html posts=posts %}

