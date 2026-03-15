---
title: "Intersection Theory"
excerpt: "Intersection theory on algebraic varieties"

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/intersection_theory
sidebar:
    nav: "algebraic_geometry-ko"

header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Intersection_Theory.png
    overlay_filter: 0.5

date: 2026-03-12
last_modified_at: 2026-03-15
weight: 16

---

Intersection theory는 대수기하학에서 가장 중요한 tool 중 하나이다. 이는 다양체들의 intersection의 수를 계산하는 방법을 제공하며, Bézout's theorem과 같은 중요한 theorem들의 증명에 핵심적인 역할을 한다. 이 절에서 우리는 intersection theory의 정의, 그리고 그 관련된 개념들을 살펴볼 것이다.

## 정의

Intersection theory는 다양체들의 intersection의 수를 계산하는 방법을 제공한다. 이는 coordinate ring의 intersection과 유사한 구조이다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Intersection theory는 다양체들의 intersection의 수를 계산하는 tool이다.\n\n</div>

기하학적으로, intersection theory는 다양체들의 intersection의 수를 계산하는 powerful tool이다. 이는 coordinate ring의 intersection과 유사한 구조이다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> Intersection theory는 다양체들의 intersection의 수를 계산하는 tool이다.\n\n</div>

<details class="proof" markdown="1">
<summary>증명</summary>

이는 coordinate ring의 intersection과 유사한 구조이다.\n\n</details>

## Chow Groups

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> Chow group $$A^k(X)$$는 cycle들의 equivalence classes를 정의한다.\n\n</div>

기하학적으로, Chow group는 cycle들의 equivalence classes를 정의하는 group이다. 이는 coordinate ring의 equivalence classes와 유사한 구조이다.

<div class="example" markdown="1">

<ins id="ex4">**예시 4**</ins> **Chow group의 예시**\n\n1. $$\mathbb{P}^n$$에서 $$A^k(\mathbb{P}^n) \cong \mathbb{Z}$$. 이는 coordinate ring의 equivalence classes와 유사한 구조이다.\n\n</div>

## Intersection Product

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> Intersection product $$A^k(X) \times A^l(X) \to A^{k+l}(X)$$은 다양체들의 intersection을 계산한다.\n\n</div>

기하학적으로, intersection product은 다양체들의 intersection을 계산하는 bilinear map이다. 이는 coordinate ring의 product와 유사한 구조이다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> Intersection product은 commutative이고 associative이다.\n\n</div>

<details class="proof" markdown="1">
<summary>증명</summary>

이는 coordinate ring의 product와 유사한 구조이다.\n\n</details>

## Bézout's Theorem

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> Bézout's theorem은 projective plane 위의 curve들의 intersection의 수를 계산한다.\n\n</div>

<details class="proof" markdown="1">
<summary>증명</summary>

이 정리의 증명은 intersection theory를 사용한다. 이는 coordinate ring의 intersection과 유사한 구조이다.\n\n</details>

## 예시의 연속성

<div class="example" markdown="1">

<ins id="ex8">**예시 8**</ins> **Intersection theory의 예시**\n\n1. $$\mathbb{P}^2$$에서 두 직선의 intersection: $$\deg(L_1) \cdot \deg(L_2) = 1 \cdot 1 = 1$$.\n2. $$\mathbb{P}^2$$에서 선과 conic의 intersection: $$\deg(L) \cdot \deg(C) = 1 \cdot 2 = 2$$.\n\n이는 coordinate ring의 intersection과 유사한 구조이다.\n\n</div>

---\n\n**참고문헌**\n\n**[Har]** J. Harris, *Algebraic Geometry: A First Course*, Springer, 1992.\n**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.\n**[Gr]** P. Griffiths and J. Harris, *Principles of Algebraic Geometry*, Wiley, 1978.\n**[HM]** R. Hartshorne, *Algebraic Geometry*, Springer, 1977.\n