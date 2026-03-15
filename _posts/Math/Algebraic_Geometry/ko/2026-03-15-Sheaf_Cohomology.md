---
title: "Sheaf Cohomology"
excerpt: "Sheaf cohomology and its applications"

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/sheaf_cohomology
sidebar:
    nav: "algebraic_geometry-ko"

header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Sheaf_Cohomology.png
    overlay_filter: 0.5

date: 2026-03-12
last_modified_at: 2026-03-15
weight: 15

---

Sheaf cohomology는 sheaf theory를 기반으로 하는 powerful tool이다. 이는 line bundle의 global sections의 수를 계산하는 데 사용되며, Riemann-Roch theorem과 같은 중요한 theorem들의 증명에 핵심적인 역할을 한다. 이 절에서 우리는 sheaf cohomology의 정의, 그리고 그 관련된 개념들을 살펴볼 것이다.

## 정의

Sheaf cohomology는 sheaf의 sections space의 subquotient를 통해 정의된다. 이는 coordinate ring의 cohomology와 유사한 구조이다.

<div class="proposition" markdown="1">

<ins id="prop1">**명제 1**</ins> Sheaf cohomology $$H^i(X, \mathcal{F})$$는 sheaf $$\mathcal{F}$$의 $$i$$-th cohomology group이다.\n\n</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Sheaf cohomology는 Čech cohomology를 사용하여 정의된다. 이는 coordinate ring의 cohomology와 유사한 구조이다.\n\n</details>

## Čech Cohomology

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> Čech cohomology는 open cover $$\{U_i\}$$와 sheaf $$\mathcal{F}$$를 사용하여 정의된다.\n\n$$H^i(X, \mathcal{F}) = \frac{\text{Cycles}}{\text{Boundaries}}$$\n\n</div>

기하학적으로, Čech cohomology는 open cover의 intersection을 통해 sheaf의 global sections의 "defect"를 계산한다. 이는 coordinate ring의 cohomology와 유사한 구조이다.

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> **Čech cohomology의 예시**\n\n1. $$\mathbb{P}^1$$에서 $$\mathcal{O}(k)$$: $$H^0(\mathbb{P}^1, \mathcal{O}(k)) = k + 1$$ for $$k \ge 0$$.\n2. $$\mathbb{P}^1$$에서 $$\mathcal{O}(-1)$$: $$H^0(\mathbb{P}^1, \mathcal{O}(-1)) = 0$$.\n\n이는 coordinate ring의 cohomology와 유사한 구조이다.\n\n</div>

## Bott's Formula

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> Bott's formula은 projective space 위의 sheaf cohomology를 계산하는 powerful tool이다.\n\n</div>

<details class="proof" markdown="1">
<summary>증명</summary>

이 정리의 증명은 spectral sequence를 사용한다. 이는 coordinate ring의 cohomology와 유사한 구조이다.\n\n</details>

## Serre Duality

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> Serre duality는 다음과 같은 isomorphism을 제공한다.\n\n$$H^i(X, \mathcal{F}) \cong H^{n-i}(X, \omega_X \otimes \mathcal{F}^\vee)^\vee$$\n\n</div>

기하학적으로, Serre duality는 canonical bundle과 dual space 사이의 deep relationship를 나타낸다. 이는 coordinate ring의 dual space와 유사한 구조이다.

<div class="example" markdown="1">

<ins id="ex6">**예시 6**</ins> **Serre duality의 예시**\n\n1. $$\mathbb{P}^n$$에서 $$\mathcal{O}(k)$$: $$H^i(\mathbb{P}^n, \mathcal{O}(k)) \cong H^{n-i}(\mathbb{P}^n, \mathcal{O}(-k-n-1))^\vee$$.\n\n이는 coordinate ring의 dual space와 유사한 구조이다.\n\n</div>

## 예시의 연속성

<div class="example" markdown="1">

<ins id="ex7">**예시 7**</ins> **Sheaf cohomology의 예시**\n\n1. $$\mathbb{P}^1$$에서 $$\mathcal{O}(k)$$: $$H^0(\mathbb{P}^1, \mathcal{O}(k)) = k + 1$$ for $$k \ge 0$$.\n2. $$\mathbb{P}^1$$에서 $$\mathcal{O}(-1)$$: $$H^0(\mathbb{P}^1, \mathcal{O}(-1)) = 0$$.\n\n이는 coordinate ring의 cohomology와 유사한 구조이다.\n\n</div>

---\n\n**참고문헌**\n\n**[Har]** J. Harris, *Algebraic Geometry: A First Course*, Springer, 1992.\n**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.\n**[Gr]** P. Griffiths and J. Harris, *Principles of Algebraic Geometry*, Wiley, 1978.\n**[HM]** R. Hartshorne, *Algebraic Geometry*, Springer, 1977.\n