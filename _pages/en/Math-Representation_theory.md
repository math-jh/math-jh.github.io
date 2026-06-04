---
title: "Representation Theory"
layout: archive_custom
regenerate: true
permalink: /en/representation_theory/
header:
  overlay_color: "transparent"
hero_hue: 236
excerpt: "Representation theory studies the structure of groups and algebras by realizing their elements as linear transformations. Through irreducible representations, characters, and weights, it analyzes symmetry in the language of linear algebra."
---
{% assign lang = site.locale %}
{% assign lang_prefix = page.url | truncate: 3, "" %}
{% if lang_prefix contains "en" or lang_prefix contains "ko" %}
  {% assign lang = lang_prefix | append: "/" %}
{% endif %}

{% assign posts = site.categories['Math / Representation Theory'] | where_exp: "post", "post.permalink contains lang" | sort: 'weight' %}
{% include subject-cards.html posts=posts %}

