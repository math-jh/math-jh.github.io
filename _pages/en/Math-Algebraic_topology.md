---
title: "Algebraic Topology"
layout: archive_custom
regenerate: true
permalink: /en/algebraic_topology/
header:
  overlay_color: "transparent"
hero_hue: 156
excerpt: "Algebraic topology distinguishes the shape of spaces by assigning algebraic invariants such as groups and rings. Through homotopy, homology, and cohomology, it translates topological information into algebra."
---
{% assign lang = site.locale %}
{% assign lang_prefix = page.url | truncate: 3, "" %}
{% if lang_prefix contains "en" or lang_prefix contains "ko" %}
  {% assign lang = lang_prefix | append: "/" %}
{% endif %}

{% assign posts = site.categories['Math / Algebraic Topology'] | where_exp: "post", "post.permalink contains lang" | sort: 'weight' %}
{% include subject-cards.html posts=posts %}

