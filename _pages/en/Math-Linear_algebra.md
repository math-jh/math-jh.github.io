---
title: "Linear Algebra"
layout: archive_custom
regenerate: true
permalink: /en/linear_algebra/
header:
  overlay_image: /assets/images/Math/Linear_Algebra/Linear_Algebra.png
  overlay_filter: 0.5
---
{% assign lang = site.locale %}
{% assign lang_prefix = page.url | truncate: 3, "" %}
{% if lang_prefix contains "en" or lang_prefix contains "ko" %}
  {% assign lang = lang_prefix | append: "/" %}
{% endif %}

{% assign posts = site.categories['Math / Linear Algebra'] | where_exp: "post", "post.permalink contains lang" | sort: 'weight' %}
{% include subject-cards.html posts=posts %}

