---
title: "Field Theory"
layout: archive_custom
regenerate: true
permalink: /en/field_theory/
header:
  overlay_image: /assets/images/Math/Field_Theory/Field_Theory.png
  overlay_filter: 0.5
---
{% assign lang = site.locale %}
{% assign lang_prefix = page.url | truncate: 3, "" %}
{% if lang_prefix contains "en" or lang_prefix contains "ko" %}
  {% assign lang = lang_prefix | append: "/" %}
{% endif %}

{% assign posts = site.categories['Math / Field Theory'] | where_exp: "post", "post.permalink contains lang" | sort: 'weight' %}
{% include subject-cards.html posts=posts %}

