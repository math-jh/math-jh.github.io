---
title: "Riemannian Geometry"
layout: archive_custom
regenerate: true
permalink: /en/riemannian_geometry/
header:
  overlay_color: "transparent"
hero_hue: 116
excerpt: "Riemannian geometry equips manifolds with a metric measuring length and angle, and studies their curvature. Through geodesics and the curvature tensor, it handles the geometry of curved spaces."
---
{% assign lang = site.locale %}
{% assign lang_prefix = page.url | truncate: 3, "" %}
{% if lang_prefix contains "en" or lang_prefix contains "ko" %}
  {% assign lang = lang_prefix | append: "/" %}
{% endif %}

{% assign posts = site.categories['Math / Riemannian Geometry'] | where_exp: "post", "post.permalink contains lang" | sort: 'weight' %}
{% include subject-cards.html posts=posts %}

