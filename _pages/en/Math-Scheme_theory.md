---
title: "Scheme Theory"
layout: archive_custom
regenerate: true
permalink: /en/scheme_theory/
header:
  overlay_color: "transparent"
hero_hue: 25
excerpt: "Scheme theory is Grothendieck's language for viewing commutative rings as geometric spaces. Through spectra, structure sheaves, and morphisms, it rebuilds algebraic geometry on a modern foundation."
---
{% assign lang = site.locale %}
{% assign lang_prefix = page.url | truncate: 3, "" %}
{% if lang_prefix contains "en" or lang_prefix contains "ko" %}
  {% assign lang = lang_prefix | append: "/" %}
{% endif %}

{% assign cat_posts = site.categories['Math / Scheme Theory'] %}
{% if cat_posts %}
{% assign posts = cat_posts | where_exp: "post", "post.permalink contains lang" | sort: 'weight' %}
{% else %}
{% assign posts = "" | split: "" %}
{% endif %}
{% include subject-cards.html posts=posts %}

