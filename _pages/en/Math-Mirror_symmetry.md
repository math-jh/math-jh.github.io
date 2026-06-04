---
title: "Mirror Symmetry"
layout: archive_custom
regenerate: true
permalink: /en/mirror_symmetry/
header:
  overlay_image: /assets/images/Math/Mirror_Symmetry/Mirror_Symmetry.png
  overlay_filter: 0.5
---
{% assign lang = site.locale %}
{% assign lang_prefix = page.url | truncate: 3, "" %}
{% if lang_prefix contains "en" or lang_prefix contains "ko" %}
  {% assign lang = lang_prefix | append: "/" %}
{% endif %}

{% assign posts = site.categories['Math / Mirror Symmetry'] | where_exp: "post", "post.permalink contains lang" | sort: 'weight' %}
{% include subject-cards.html posts=posts %}

