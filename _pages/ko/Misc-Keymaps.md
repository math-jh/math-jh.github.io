---
title: "키맵"
layout: archive_custom
permalink: /ko/keymaps
---
{% assign lang = site.locale %}
{% assign lang_prefix = page.url | truncate: 3, "" %}
{% if lang_prefix contains "en" or lang_prefix contains "ko" %}
  {% assign lang = lang_prefix | remove_first: "/" %}
{% endif %}

{% assign posts = site.categories['Misc / Peripherals'] | where_exp: "post", "post.permalink contains lang" | sort: 'weight' %}
{% assign keyboard-posts = posts | where_exp: "post", "post.permalink contains '/keyboards/'" | sort: 'weight' %}
{% for post in keyboard-posts %} {% include archive-single.html type=page.entries_layout %} {% endfor %}