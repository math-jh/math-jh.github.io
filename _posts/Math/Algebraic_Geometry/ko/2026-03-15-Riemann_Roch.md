---
title: "리만-로흐 정리 (Riemann-Roch Theorem)"
excerpt: "Riemann-Roch theorem and its applications"

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/riemann_roch
sidebar:
    nav: "algebraic_geometry-ko"

header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Riemann_Roch.png
    overlay_filter: 0.5

date: 2026-03-12
last_modified_at: 2026-03-15
weight: 14

---

리만-로흐 정리(Riemann-Roch theorem)는 대수기하학에서 가장 중요한 정리 중 하나이다. 이 정리는 line bundle의 global sections의 수를 계산하는 방법을 제공하며, Picard group와 Riemann-Roch invariant와 밀접한 관계가 있다. 이 절에서 우리는 리만-로흐 정리의 정의, 그리고 그 관련된 개념들을 살펴볼 것이다.

## 정의

리만-로흐 정리는 line bundle의 global sections의 수를 계산하는 방법을 제공한다. 이는 coordinate ring의 dimension을 계산하는 방법과 유사한 구조이다.

<div class="proposition" markdown="1">

<ins id="prop1">**명제 1**</ins> 기역 다양체 $$X$$ 위의 line bundle $$\mathcal{L}$$에 대해, 리만-로흐 정리는 다음과 같다.\n\n$$h^0(X, \mathcal{L}) - h^0(X, \omega_X \otimes \mathcal{L}^\vee) = \chi(\mathcal{L}) = \deg \mathcal{L} + 1 - g$$\n\n여기서 $$g$$는 genus이다.\n\n</div>

<details class="proof" markdown="1">
<summary>증명</summary>

이 정리의 증명은 sheaf cohomology를 사용한다. 이는 coordinate ring의 dimension을 계산하는 방법과 유사한 구조이다.\n\n</details>

## 예시

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins> **리만-로흐 정리의 예시**\n\n1. $$\mathbb{P}^1$$에서 $$\mathcal{O}(k)$$: $$h^0(\mathbb{P}^1, \mathcal{O}(k)) = k + 1$$ for $$k \ge 0$$.\n2. $$\mathbb{P}^2$$에서 $$\mathcal{O}(k)$$: $$h^0(\mathbb{P}^2, \mathcal{O}(k)) = \binom{k+2}{2}$$.\n\n이는 coordinate ring의 dimension을 계산하는 방법과 유사한 구조이다.\n\n</div>

## Degree

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> Line bundle $$\mathcal{L}$$의 degree는 다음과 같이 계산된다.\n\n$$\deg \mathcal{L} = \sum_{p \in X} \operatorname{ord}_p(\mathcal{L})$$\n\n여기서 $$\operatorname{ord}_p(\mathcal{L})$$는 line bundle의 local trivialization에서의 order이다.\n\n</div>

<details class="proof" markdown="1">
<summary>증명</summary>

이는 coordinate ring의 degree와 유사한 구조이다. 이는 line bundle의 "twisting" 정도를 측정한다.\n\n</details>

## 예시의 연속성

<div class="example" markdown="1">

<ins id="ex4">**예시 4**</ins> **Degree의 예시**\n\n1. $$\mathbb{A}^n$$의 trivial bundle: $$\deg \mathcal{O}_{\mathbb{A}^n} = 0$$. 모든 point에서 order가 0이므로.\n2. $$\mathbb{P}^n$$의 hyperplane bundle: $$\deg \mathcal{O}_{\mathbb{P}^n}(1) = 1$$. hyperplane section의 degree는 1이다.\n\n이는 coordinate ring의 degree와 유사한 구조이다.\n\n</div>

## 완전 선형 시스템

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> 완전 선형 시스템 $$|D|$$의 dimension은 $$h^0(X, \mathcal{O}_X(D)) - 1$$이다.\n\n</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Global sections space $$H^0(X, \mathcal{O}_X(D))$$는 vector space이며, 완전 선형 시스템은 그 위의 effective divisors의 subspace이다. Zero section은 제외하므로, dimension은 $$h^0(X, \mathcal{O}_X(D)) - 1$$이다.\n\n</details>

## Base Locus

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> Line bundle $$\mathcal{L}$$의 base locus $$\mathrm{Bs}|\mathcal{L}|$$는 모든 element $$D' \in |\mathcal{L}|$$가 포함하는 divisor의 공유되는 component들의 집합이다.\n\n</div>

<details class="proof" markdown="1">
<summary>증명</summary>

이는 coordinate ring의 singular locus와 유사한 구조이다. Base locus가 비어있는 경우, linear system은 "basepoint-free"이다.\n\n</details>

## 예시의 연속성

<div class="example" markdown="1">

<ins id="ex5">**예시 5**</ins> **Riemann-Roch 정리의 예시**\n\n1. $$\mathbb{P}^1$$에서 $$\mathcal{O}(k)$$: $$h^0(\mathbb{P}^1, \mathcal{O}(k)) = k + 1$$ for $$k \ge 0$$.\n2. $$\mathbb{P}^2$$에서 $$\mathcal{O}(k)$$: $$h^0(\mathbb{P}^2, \mathcal{O}(k)) = \binom{k+2}{2}$$.\n\n이는 coordinate ring의 dimension을 계산하는 방법과 유사한 구조이다.\n\n</div>

---\n\n**참고문헌**\n\n**[Har]** J. Harris, *Algebraic Geometry: A First Course*, Springer, 1992.\n**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.\n**[Gr]** P. Griffiths and J. Harris, *Principles of Algebraic Geometry*, Wiley, 1978.\n**[HM]** R. Hartshorne, *Algebraic Geometry*, Springer, 1977.\n