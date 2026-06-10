---
title: "Set Theory"
layout: archive_custom
regenerate: true
permalink: /en/set_theory/
header:
  overlay_color: "transparent"
hero_hue: 274
excerpt: "Set theory is the foundation of mathematics, concerned with sets, their operations, and the infinite. Through relations and functions, ordinals and cardinals, and the axiom of choice, it supplies the language every later field rests on."
---
{% assign lang = site.locale %}
{% assign lang_prefix = page.url | truncate: 3, "" %}
{% if lang_prefix contains "en" or lang_prefix contains "ko" %}
  {% assign lang = lang_prefix | append: "/" %}
{% endif %}

{% assign cat_posts = site.categories['Math / Set Theory'] %}
{% if cat_posts %}
{% assign posts = cat_posts | where_exp: "post", "post.permalink contains lang" | sort: 'weight' %}
{% else %}
{% assign posts = "" | split: "" %}
{% endif %}
{% include subject-cards.html posts=posts %}

