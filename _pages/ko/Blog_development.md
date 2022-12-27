---
title: "블로그 개발"
layout: archive_custom
permalink: /ko/blog_development/
---
{% assign lang = site.locale %}
{% assign lang_prefix = page.url | truncate: 3, "" %}
{% if lang_prefix contains "en" or lang_prefix contains "ko" %}
  {% assign lang = lang_prefix | remove_first: "/" %}
{% endif %}

{% assign posts = site.categories['Blog Development'] | where_exp: "post", "post.permalink contains lang" | sort: 'weight' %}
{% for post in posts %} {% include archive-single.html type=page.entries_layout %} {% endfor %}