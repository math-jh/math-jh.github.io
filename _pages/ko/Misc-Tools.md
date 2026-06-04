---
title: "도구"
layout: archive_custom
regenerate: true
permalink: /ko/tools
header:
  overlay_image: /assets/images/Misc/Tools/Tools.png
  overlay_filter: 0.5
---
{% assign lang = site.locale %}
{% assign lang_prefix = page.url | truncate: 3, "" %}
{% if lang_prefix contains "en" or lang_prefix contains "ko" %}
  {% assign lang = lang_prefix | append: "/" %}
{% endif %}

{% assign posts = site.categories['Misc / Peripherals'] | where_exp: "post", "post.permalink contains lang" | where_exp: "post", "post.permalink contains '/tools/'" | sort: 'weight' %}
{% include subject-cards.html posts=posts minimal=true %}