---
title: "Manifolds"
layout: archive_custom
regenerate: true
permalink: /en/manifolds/
header:
  overlay_color: "transparent"
hero_hue: 84
excerpt: "The theory of differentiable manifolds develops calculus on spaces that locally look like Euclidean space. Through tangent spaces, vector fields, and differential forms, it sets the stage for geometry and physics."
---
{% assign lang = site.locale %}
{% assign lang_prefix = page.url | truncate: 3, "" %}
{% if lang_prefix contains "en" or lang_prefix contains "ko" %}
  {% assign lang = lang_prefix | append: "/" %}
{% endif %}

{% assign posts = site.categories['Math / Manifolds'] | where_exp: "post", "post.permalink contains lang" | sort: 'weight' %}
{% include subject-cards.html posts=posts %}

