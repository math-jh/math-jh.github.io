---
title: "Mathematics"
layout: archive_custom
regenerate: true
permalink: /en/math/
author_profile: true
---
{% assign lang = site.locale %}
{% assign lang_prefix = page.url | truncate: 3, "" %}
{% if lang_prefix contains "en" or lang_prefix contains "ko" %}
  {% assign lang = lang_prefix | append: "/" %}
{% endif %}

## General

- [Linear Algebra](/en/linear_algebra/)

## Foundations

- [Set Theory](/en/set_theory/)
- [Category Theory](/en/category_theory/)

## Algebra

- [Algebraic Structures](/en/algebraic_structures/)
- [Group Theory](/en/group_theory/)
- [Ring Theory](/en/ring_theory/)
- [Multilinear Algebra](/en/multilinear_algebra/)
- [Field Theory](/en/field_theory/)
- [Homological Algebra](/en/homological_algebra/)
- [Commutative Algebra](/en/commutative_algebra/)

## Geometry & Topology

- [Topology](/en/topology/)
- [Manifolds](/en/manifold/)
- [Riemannian Geometry](/en/riemannian_geometry/)
- [Algebraic Topology](/en/algebraic_topology/)
- [Algebraic Varieties](/en/algebraic_varieties/)
- [Scheme Theory](/en/scheme_theory/)
- [Symplectic Geometry](/en/symplectic_geometry/)
- [Toric Geometry](/en/toric_geometry/)

## Other

- [Lie Theory](/en/lie_theory/)
- [Representation Theory](/en/representation_theory/)
- [Mirror Symmetry](/en/mirror_symmetry/)
