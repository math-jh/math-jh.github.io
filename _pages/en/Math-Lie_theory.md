---
title: "Lie Theory"
layout: archive_custom
regenerate: true
permalink: /en/lie_theory/
header:
  overlay_color: "transparent"
hero_hue: 100
excerpt: "Lie theory studies Lie groups, which carry continuous symmetry, and their infinitesimal counterparts, Lie algebras. Through the exponential map, root systems, and weights, it connects geometry and representation theory."
---
{% assign lang = site.locale %}
{% assign lang_prefix = page.url | truncate: 3, "" %}
{% if lang_prefix contains "en" or lang_prefix contains "ko" %}
  {% assign lang = lang_prefix | append: "/" %}
{% endif %}

{% assign posts = site.categories['Math / Lie Theory'] | where_exp: "post", "post.permalink contains lang" | sort: 'weight' %}
{% include subject-cards.html posts=posts %}

