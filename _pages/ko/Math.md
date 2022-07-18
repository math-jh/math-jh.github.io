---
title: "Math"
layout: archive_custom
permalink: /ko/math
author_profile: true
---
{% assign lang = site.locale %}
{% assign lang_prefix = page.url | truncate: 3, "" %}
{% if lang_prefix contains "en" or lang_prefix contains "ko" %}
  {% assign lang = lang_prefix | remove_first: "/" %}
{% endif %}

## Preliminaries
- [Elementary Calculus]()
- [Linear Algebra]({{ lang_prefix }}/linear_algebra/)


## Foundations

- [Set Theory]({{ lang_prefix }}/set_theory/)
- [Category Theory]()

## Algebraic Structure

- [Groups]({{ lang_prefix }}/groups/)
- [Rings]({{ lang_prefix }}/rings/)
- [Modules]({{ lang_prefix }}/modules/)
- [Algebras]({{ lang_prefix }}/algebras/)
- [Galois theory]({{ lang_prefix }}/galois_theory/)
