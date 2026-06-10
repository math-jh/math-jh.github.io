---
title: "Toric Geometry"
layout: archive_custom
regenerate: true
permalink: /en/toric_geometry/
header:
  overlay_color: "transparent"
hero_hue: 41
excerpt: "Toric geometry studies toric varieties, which are described by combinatorial data such as fans. Through the combinatorics of lattices and cones, it provides a rich supply of examples in algebraic geometry."
---
{% assign lang = site.locale %}
{% assign lang_prefix = page.url | truncate: 3, "" %}
{% if lang_prefix contains "en" or lang_prefix contains "ko" %}
  {% assign lang = lang_prefix | append: "/" %}
{% endif %}

{% assign cat_posts = site.categories['Math / Toric Geometry'] %}
{% if cat_posts %}
{% assign posts = cat_posts | where_exp: "post", "post.permalink contains lang" | sort: 'weight' %}
{% else %}
{% assign posts = "" | split: "" %}
{% endif %}
{% include subject-cards.html posts=posts %}

