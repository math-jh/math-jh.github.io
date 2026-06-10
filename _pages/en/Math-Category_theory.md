---
title: "Category Theory"
layout: archive_custom
regenerate: true
permalink: /en/category_theory/
header:
  overlay_color: "transparent"
hero_hue: 306
excerpt: "Category theory treats mathematical structures abstractly through objects, morphisms, and the universal properties between them. Functors, natural transformations, limits, and adjunctions let it connect disparate fields in a single language."
---
{% assign lang = site.locale %}
{% assign lang_prefix = page.url | truncate: 3, "" %}
{% if lang_prefix contains "en" or lang_prefix contains "ko" %}
  {% assign lang = lang_prefix | append: "/" %}
{% endif %}

{% assign cat_posts = site.categories['Math / Category Theory'] %}
{% if cat_posts %}
{% assign posts = cat_posts | where_exp: "post", "post.permalink contains lang" | sort: 'weight' %}
{% else %}
{% assign posts = "" | split: "" %}
{% endif %}
{% include subject-cards.html posts=posts %}

