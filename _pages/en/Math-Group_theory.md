---
title: "Group Theory"
layout: archive_custom
regenerate: true
permalink: /en/group_theory/
header:
  overlay_color: "transparent"
hero_hue: 209
excerpt: "Group theory studies groups, which capture symmetry algebraically, together with their actions. Through subgroups and normal subgroups, group actions and the Sylow theorems, it moves toward classifying structure."
---
{% assign lang = site.locale %}
{% assign lang_prefix = page.url | truncate: 3, "" %}
{% if lang_prefix contains "en" or lang_prefix contains "ko" %}
  {% assign lang = lang_prefix | append: "/" %}
{% endif %}

{% assign posts = site.categories['Math / Group Theory'] | where_exp: "post", "post.permalink contains lang" | sort: 'weight' %}
{% include subject-cards.html posts=posts %}

