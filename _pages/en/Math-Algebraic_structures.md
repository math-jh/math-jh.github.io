---
title: "Algebraic Structures"
layout: archive_custom
regenerate: true
permalink: /en/algebraic_structures/
header:
  overlay_color: "transparent"
hero_hue: 204
excerpt: "Algebraic structures studies sets equipped with operations, such as groups, rings, and modules, in a unified way. Centered on homomorphisms and quotient structures, it lays the groundwork shared by every later algebraic field."
---
{% assign lang = site.locale %}
{% assign lang_prefix = page.url | truncate: 3, "" %}
{% if lang_prefix contains "en" or lang_prefix contains "ko" %}
  {% assign lang = lang_prefix | append: "/" %}
{% endif %}

{% assign posts = site.categories['Math / Algebraic Structures'] | where_exp: "post", "post.permalink contains lang" | sort: 'weight' %}
{% include subject-cards.html posts=posts %}

