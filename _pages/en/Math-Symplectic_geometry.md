---
title: "Symplectic Geometry"
layout: archive_custom
regenerate: true
permalink: /en/symplectic_geometry/
header:
  overlay_color: "transparent"
hero_hue: 1
excerpt: "Symplectic geometry studies the phase spaces of classical mechanics geometrically, on manifolds equipped with a symplectic form. Through Hamiltonian flows and moment maps, it connects dynamics and geometry."
---
{% assign lang = site.locale %}
{% assign lang_prefix = page.url | truncate: 3, "" %}
{% if lang_prefix contains "en" or lang_prefix contains "ko" %}
  {% assign lang = lang_prefix | append: "/" %}
{% endif %}

{% assign posts = site.categories['Math / Symplectic Geometry'] | where_exp: "post", "post.permalink contains lang" | sort: 'weight' %}
{% include subject-cards.html posts=posts %}

