---
title: "Topology"
layout: archive_custom
regenerate: true
permalink: /en/topology/
header:
  overlay_color: "transparent"
hero_hue: 124
excerpt: "Topology studies the properties of spaces using only the notions of continuity and neighborhood. Through connectedness, compactness, and the separation axioms, it lays the foundation for analysis and geometry."
---
{% assign lang = site.locale %}
{% assign lang_prefix = page.url | truncate: 3, "" %}
{% if lang_prefix contains "en" or lang_prefix contains "ko" %}
  {% assign lang = lang_prefix | append: "/" %}
{% endif %}

{% assign cat_posts = site.categories['Math / Topology'] %}
{% if cat_posts %}
{% assign posts = cat_posts | where_exp: "post", "post.permalink contains lang" | sort: 'weight' %}
{% else %}
{% assign posts = "" | split: "" %}
{% endif %}
{% include subject-cards.html posts=posts %}

