---
title: "Commutative Algebra"
layout: archive_custom
regenerate: true
permalink: /en/commutative_algebra/
header:
  overlay_color: "transparent"
hero_hue: 231
excerpt: "Commutative algebra studies commutative rings and the modules over them. Through localization, primary decomposition, and dimension theory, it provides the local foundation of algebraic geometry."
---
{% assign lang = site.locale %}
{% assign lang_prefix = page.url | truncate: 3, "" %}
{% if lang_prefix contains "en" or lang_prefix contains "ko" %}
  {% assign lang = lang_prefix | append: "/" %}
{% endif %}

{% assign posts = site.categories['Math / Commutative Algebra'] | where_exp: "post", "post.permalink contains lang" | sort: 'weight' %}
{% include subject-cards.html posts=posts %}

