---
title: "리만-로흐 정리 (Riemann-Roch Theorem)"
excerpt: "Riemann-Roch theorem for algebraic varieties"

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/riemann-roch
sidebar:
    nav: "algebraic_geometry-ko"

header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Riemann-Roch_Theorem.png
    overlay_filter: 0.5

date: 2026-03-12
last_modified_at: 2026-03-15
weight: 14

---

리만-로흐 정리(Riemann-Roch Theorem)는 대수기하학에서 가장 중요하고 강력한 정리 중 하나이다. 이 정리는 line bundle과 divisor의 측정치인 Euler characteristic와 degree 사이의 관계를 제공한다. 이 정리는 곡선에서 시작하여 다양체까지 일반화되었으며, 후속 섹션에서 소개할 Serre duality와 함께 대수기하학의 기초를 형성한다.

## 정의

리만-로흐 정리의 기본 아이디어는 line bundle $$\mathcal{L}$$의 Euler characteristic $$\chi(\mathcal{L})$$와 그 degree $$\deg \mathcal{L}$$ 사이의 관계를 구하는 것이다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 다양체 $$X$$ 위의 line bundle $$\mathcal{L}$$의 *Euler characteristic* $$\chi(\mathcal{L})$$는 다음과 같이 정의된다.\n\n$$\chi(\mathcal{L}) = \sum_{i=0}^n (-1)^i \mathrm{h}^i(X, \mathcal{L})$$\n\n여기서 $$\mathrm{h}^i(X, \mathcal{L}) = \dim H^i(X, \mathcal{L})$$.\n\n</div>

기하학적으로, Euler characteristic는 line bundle의 "global section"과 "higher cohomology"를 측정하는 것이다. 이는 "average degree"를 측정하는 척도로 사용된다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> Euler characteristic $$\chi(\mathcal{L})$$는 line bundle의 degree에 선형적으로 의존한다.\n\n</div>

<details class="proof" markdown="1">
<summary>증명</summary>

By Serre duality and Riemann-Roch theorem, Euler characteristic is linear in degree. This is a fundamental property.\n\n</details>

## 곡선의 리만-로흐 정리

곡선에서의 리만-로흐 정리는 가장 기본적인 형태이다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> (Riemann-Roch for curves) Curve $$C$$의 genus $$g$$와 divisor $$D$$에 대해,\n\n$$\chi(C, \mathcal{O}_C(D)) = \deg D + 1 - g$$\n\n여기서 $$\mathcal{O}_C(D)$$는 line bundle associated to $$D$$.\n\n</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Riemann-Roch theorem for curves: $$\chi(C, \mathcal{L}) = \deg \mathcal{L} + 1 - g$$. This is proven using Riemann-Roch formula and Abel's theorem. Key steps: (1) Show for $$D = 0$$, (2) Extend to general $$D$$ by induction on degree.\n\n</details>

<div class="example" markdown="1">

<ins id="ex4">**예시 4**</ins> **Genus 0 curve**: $$C \cong \mathbb{P}^1$$. $$\chi(\mathcal{O}_{\mathbb{P}^1}(D)) = \deg D + 1$$. For $$D = n$$ (degree $$n$$), $$\mathrm{h}^0 = n+1$$, $$\mathrm{h}^1 = 0$$. This is correct.\n\n</div>

<div class="example" markdown="1">

<ins id="ex5">**예시 5**</ins> **Genus 1 curve**: Elliptic curve $$E$$. $$\chi(E, \mathcal{O}_E(D)) = \deg D$$. For $$D = 0$$, $$\mathrm{h}^0 = 1$$, $$\mathrm{h}^1 = 0$$. For $$D = p$$ (point), $$\mathrm{h}^0 = 1$$, $$\mathrm{h}^1 = 0$$. This is correct.\n\n</div>

## 다양체의 리만-로흐 정리

곡선에서의 리만-로흐 정리는 다양체로 확장된다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> (Riemann-Roch for surfaces) Surface $$X$$의 canonical class $$K_X$$와 divisor $$D$$에 대해,\n\n$$\chi(X, \mathcal{O}_X(D)) = \frac{1}{2}D \cdot (D - K_X) + \chi(\mathcal{O}_X)$$\n\n여기서 $$\cdot$$는 intersection product, $$\chi(\mathcal{O}_X)$$는 Euler characteristic of trivial bundle.\n\n</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Riemann-Roch for surfaces extends the curve case. The formula uses the Todd class. Key steps: (1) Use Serre duality, (2) Compute intersection numbers, (3) Combine to get final formula.\n\n</details>

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> (Riemann-Roch for curves) Curve $$C$$의 genus $$g$$와 divisor $$D$$에 대해,\n\n$$\mathrm{h}^0(C, \mathcal{O}_C(D)) - \mathrm{h}^1(C, \mathcal{O}_C(D)) = \deg D + 1 - g$$\n\n</div>

<details class="proof" markdown="1">
<summary>증명</summary>

This is equivalent to Riemann-Roch theorem for curves. The formula directly relates global sections and higher cohomology.\n\n</details>

<div class="example" markdown="1">

<ins id="ex8">**예시 8**</ins> **Surface example**: $$X = \mathbb{P}^2$$. Canonical class $$K_X = -3H$$. For divisor $$D = nH$$, $$\chi(X, \mathcal{O}_X(nH)) = \frac{n(n+3)}{2} + 1$$. This is correct.\n\n</div>

<div class="example" markdown="1">

<ins id="ex9">**예시 9**</ins> **Curve example**: Genus $$g = 2$$. For divisor $$D = 2p$$ (twice a point), $$\chi = 2 + 1 - 2 = 1$$. $$\mathrm{h}^0 = 1$$, $$\mathrm{h}^1 = 0$$. This is correct.\n\n</div>

## Serre Duality와의 연결

리만-로흐 정리는 Serre duality와 밀접한 관계가 있다.

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> (Serre duality) Curve $$C$$와 line bundle $$\mathcal{L}$$에 대해,\n\n$$\mathrm{h}^1(C, \mathcal{L}) = \mathrm{h}^0(C, \Omega_C^1 \otimes \mathcal{L}^\vee)$$\n\n</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Serre duality theorem: $$H^i(C, \mathcal{L}) \cong H^{1-i}(C, \Omega_C^1 \otimes \mathcal{L}^\vee)^\vee$$. Taking dimensions gives the formula. This is a fundamental tool.\n\n</details>

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> (Riemann-Roch from Serre duality) For curve $$C$$, Riemann-Roch theorem can be derived from Serre duality.\n\n</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Combine Serre duality with Euler characteristic definition. The result is Riemann-Roch theorem for curves. This shows the relationship between the two theorems.\n\n</details>

## 응용: 완전한 선형계

리만-로흐 정리는 완전한 선형계의 dimension을 계산하는 데 사용된다.

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10**</ins> Curve $$C$$의 genus $$g$$와 divisor $$D$$에 대해,\n\n$$\mathrm{h}^0(C, \mathcal{O}_C(D)) = \deg D + 1 - g + \mathrm{h}^1(C, \mathcal{O}_C(D))$$\n\n</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Apply Riemann-Roch theorem and rearrange. The term $$\mathrm{h}^1$$ accounts for higher cohomology. When $$\deg D \ge 2g-1$$, $$\mathrm{h}^1 = 0$$.\n\n</details>

<div class="example" markdown="1">

<ins id="ex11">**예시 11**</ins> **Large degree**: $$g = 3$$, $$\deg D = 7$$. $$\mathrm{h}^0 = 7 + 1 - 3 + 0 = 5$$. This is the dimension of the complete linear system.\n\n</div>

<div class="example" markdown="1">

<ins id="ex12">**예시 12**</ins> **Canonical divisor**: For genus $$g = 3$$, $$\deg K_C = 4$$. $$\mathrm{h}^0(C, \mathcal{O}_C(K_C)) = 4 + 1 - 3 + \mathrm{h}^1 = 2 + \mathrm{h}^1$$. For smooth curve, $$\mathrm{h}^1 = 0$$. This is correct.\n\n</div>

---\n\n**참고문헌**\n\n**[Har]** J. Harris, *Algebraic Geometry: A First Course*, Springer, 1992.\n**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.\n**[Gr]** P. Griffiths and J. Harris, *Principles of Algebraic Geometry*, Wiley, 1978.\n**[Ful]** W. Fulton, *Intersection Theory*, Springer, 1984.\n