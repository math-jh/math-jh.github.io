---
title: "Linear Algebra"
layout: archive_custom
regenerate: true
permalink: /en/linear_algebra/
header:
  overlay_color: "transparent"
hero_hue: 249
excerpt: "Linear algebra studies vector spaces and the linear maps between them. Starting from bases and dimension, it builds through matrix representations, eigenspace decomposition, and dual spaces into a language used across nearly all of mathematics."
---
{% assign lang = site.locale %}
{% assign lang_prefix = page.url | truncate: 3, "" %}
{% if lang_prefix contains "en" or lang_prefix contains "ko" %}
  {% assign lang = lang_prefix | append: "/" %}
{% endif %}

{% assign posts = site.categories['Math / Linear Algebra'] | where_exp: "post", "post.permalink contains lang" | sort: 'weight' %}
{% include subject-cards.html posts=posts %}

