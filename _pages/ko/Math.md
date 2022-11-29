---
title: "Math"
layout: archive_custom
permalink: /ko/math/
author_profile: true
---
{% assign lang = site.locale %}
{% assign lang_prefix = page.url | truncate: 3, "" %}
{% if lang_prefix contains "en" or lang_prefix contains "ko" %}
  {% assign lang = lang_prefix | remove_first: "/" %}
{% endif %}

## 수학기초론

- [Set Theory]({{ lang_prefix }}/set_theory/)

## 대수학

