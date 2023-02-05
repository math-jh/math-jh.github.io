---
title: "선형대수학"
layout: archive_custom
permalink: /ko/linear_algebra
---
{% assign lang = site.locale %}
{% assign lang_prefix = page.url | truncate: 3, "" %}
{% if lang_prefix contains "en" or lang_prefix contains "ko" %}
  {% assign lang = lang_prefix | remove_first: "/" %}
{% endif %}

{% assign posts = site.categories['Math / Linear Algebra'] | where_exp: "post", "post.permalink contains lang" | sort: 'weight' %}
{% for post in posts %} {% include archive-single.html type=page.entries_layout %} {% endfor %}

[<span class="material-icons md-18" style="vertical-align:-.1em;">&#xE5C4;</span> Back to [Math] directory]({{ lang_prefix }}/math/)
{: style="text-align: right;"}
