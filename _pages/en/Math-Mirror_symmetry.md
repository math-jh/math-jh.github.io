---
title: "Mirror Symmetry"
layout: archive_custom
regenerate: true
permalink: /en/mirror_symmetry/
header:
  overlay_color: "transparent"
hero_hue: 329
excerpt: "Mirror symmetry studies the phenomenon that the symplectic geometry of one Calabi-Yau manifold corresponds to the complex geometry of another. Arising from string theory, it links enumerative geometry and homological algebra."
---
{% assign lang = site.locale %}
{% assign lang_prefix = page.url | truncate: 3, "" %}
{% if lang_prefix contains "en" or lang_prefix contains "ko" %}
  {% assign lang = lang_prefix | append: "/" %}
{% endif %}

{% assign posts = site.categories['Math / Mirror Symmetry'] | where_exp: "post", "post.permalink contains lang" | sort: 'weight' %}
{% include subject-cards.html posts=posts %}

