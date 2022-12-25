---
title: "수학"
layout: archive_custom
permalink: /ko/math/
author_profile: true
---
{% assign lang = site.locale %}
{% assign lang_prefix = page.url | truncate: 3, "" %}
{% if lang_prefix contains "en" or lang_prefix contains "ko" %}
  {% assign lang = lang_prefix | remove_first: "/" %}
{% endif %}

## 교양수학

- [선형대수학](/ko/linear_algebra/)

## 수학기초론

- [집합론](/ko/set_theory/)

## 대수학

- [대수적 구조](/ko/algebraic_structures/)
- [텐서대수](/ko/tensor_algebra/)
- [호몰로지 대수학](/ko/homological_algebra/)

## 기하학 및 위상수학

- [위상수학](/ko/topology/)
- [미분다양체](/ko/manifold/)
- [사교기하학](/ko/symplectic_geometry/)

## 기타

- [찾아보기](/ko/misc/index)