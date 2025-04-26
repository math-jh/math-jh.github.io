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
- [범주론](/ko/category_theory/)

## 대수학

- [대수적 구조](/ko/algebraic_structures/)
- [군론](/ko/group_theory/)
- [환룐](/ko/ring_theory/)
- [다중선형대수학](/ko/multilinear_algebra/)
- [체론](/ko/field_theory/)
- [호몰로지 대수학](/ko/homological_algebra/)
- [가환대수학](/ko/commutative_algebra/)

## 기하학 및 위상수학

- [위상수학](/ko/topology/)
- [미분다양체](/ko/manifold/)
- [리만기하학](/ko/riemannian_geometry/)
- [대수적 위상수학](/ko/algebraic_topology/)
- [대수기하학](/ko/algebraic_geometry/)
- [사교기하학](/ko/symplectic_geometry/)

## 기타

- [찾아보기](/ko/misc/index)