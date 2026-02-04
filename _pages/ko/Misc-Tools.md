---
title: "도구"
layout: archive_custom
permalink: /ko/tools
---
{% assign lang = site.locale %}
{% assign lang_prefix = page.url | truncate: 3, "" %}
{% if lang_prefix contains "en" or lang_prefix contains "ko" %}
  {% assign lang = lang_prefix | remove_first: "/" %}
{% endif %}

{% assign posts = site.categories['Misc / Peripherals'] | where_exp: "post", "post.permalink contains lang" | sort: 'weight' %}
{% assign tools-posts = posts | where_exp: "post", "post.permalink contains '/tools/'" | sort: 'weight' %}
{% for post in tools-posts %} {% include archive-single.html type=page.entries_layout %} {% endfor %}