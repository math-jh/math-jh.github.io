---
title: "Ring Theory"
layout: archive_custom
regenerate: true
permalink: /en/ring_theory/
header:
  overlay_color: "transparent"
hero_hue: 213
excerpt: "Ring theory studies rings, which carry both addition and multiplication, along with their ideals. Through domains and fields, factorization, and modules, it becomes the foundation of commutative algebra and algebraic geometry."
---
{% assign lang = site.locale %}
{% assign lang_prefix = page.url | truncate: 3, "" %}
{% if lang_prefix contains "en" or lang_prefix contains "ko" %}
  {% assign lang = lang_prefix | append: "/" %}
{% endif %}

{% assign cat_posts = site.categories['Math / Ring Theory'] %}
{% if cat_posts %}
{% assign posts = cat_posts | where_exp: "post", "post.permalink contains lang" | sort: 'weight' %}
{% else %}
{% assign posts = "" | split: "" %}
{% endif %}
{% include subject-cards.html posts=posts %}

