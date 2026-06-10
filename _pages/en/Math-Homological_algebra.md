---
title: "Homological Algebra"
layout: archive_custom
regenerate: true
permalink: /en/homological_algebra/
header:
  overlay_color: "transparent"
hero_hue: 227
excerpt: "Homological algebra measures the properties of algebraic structures through chain complexes and their homology. Via exact sequences, derived functors, and Ext and Tor, it links topology, geometry, and algebra."
---
{% assign lang = site.locale %}
{% assign lang_prefix = page.url | truncate: 3, "" %}
{% if lang_prefix contains "en" or lang_prefix contains "ko" %}
  {% assign lang = lang_prefix | append: "/" %}
{% endif %}

{% assign cat_posts = site.categories['Math / Homological Algebra'] %}
{% if cat_posts %}
{% assign posts = cat_posts | where_exp: "post", "post.permalink contains lang" | sort: 'weight' %}
{% else %}
{% assign posts = "" | split: "" %}
{% endif %}
{% include subject-cards.html posts=posts %}

