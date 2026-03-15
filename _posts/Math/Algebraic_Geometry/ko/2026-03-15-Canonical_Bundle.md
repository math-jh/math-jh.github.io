---
title: "정규 다발 (Canonical Bundle)"
excerpt: "Canonical bundle on algebraic varieties"

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/canonical_bundle
sidebar:
    nav: "algebraic_geometry-ko"

header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Canonical_Bundle.png
    overlay_filter: 0.5

date: 2026-03-12
last_modified_at: 2026-03-15
weight: 13

---

정규 다발(canonical bundle)은 대수다양체 위의 가장 중요한 line bundle 중 하나이다. 이는 "holomorphic 1-forms"의 line bundle이며, 다양체의 "canonical class"를 정의하는 기초이다. 이 절에서 우리는 정규 다발의 정의, 주요 예시, 그리고 Riemann-Roch theorem과의 연결을 살펴볼 것이다.

## 정의

정규 다발의 기본 아이디어는 다양체 위의 "holomorphic differential forms"을 취급하는 것이다. 즉, 다양체 위의 "cotangent bundle"의 top exterior power이다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 다양체 $$X$$ 위의 *canonical bundle* $$\Omega_X^1$$는 cotangent bundle $$T_X^\vee$$의 top exterior power이다.\n\n$$\Omega_X^1 = \bigwedge^n T_X^\vee$$\n\n여기서 $$n = \dim X$$. Projective variety의 경우, canonical bundle은 hyperplane section의 normal bundle이다.\n\n</div>

기하학적으로, canonical bundle은 다양체 위의 "canonical coordinate"를 취급하는 것이다. 즉, 다양체가 "자연스러운" 1-form을 가지고 있는지를 나타낸다. 이는 다양체의 "torsion"를 판별하는 핵심 도구이다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> 다양체 $$X$$ 위의 canonical bundle $$\Omega_X^1$$의 fiber는 "cotangent space" $$T_p^\vee$$의 top exterior power이다.\n\n</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Canonical bundle은 cotangent bundle $$T_X^\vee$$의 $$n$$-th exterior power이므로, fiber는 $$T_p^\vee$$의 top exterior power $$\bigwedge^n T_p^\vee$$이다. This is dual to tangent space.\n\n</details>

## Canonical Class

Canonical bundle은 Picard group의 element를 정의한다. 이를 *canonical class* $$K_X$$라고 부른다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> 다양체 $$X$$ 위의 *canonical class* $$K_X$$는 canonical bundle $$\Omega_X^1$$의 isomorphism class이다.\n\n</div>

기하학적으로, canonical class는 다양체의 "canonical coordinate"를 나타낸다. Picard group에서 zero element은 trivial bundle이므로, canonical class는 다양체가 "trivial canonical bundle"을 가지는지를 나타낸다. 이는 다양체의 "torsion"를 판별하는 핵심 도구이다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> Canonical class $$K_X$$는 Picard group $$\mathrm{Pic}(X)$$의 element이다.\n\n</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Canonical bundle $$\Omega_X^1$$는 line bundle이므로, Picard group의 element이다. This element is denoted $$K_X$$. Trivial canonical bundle corresponds to zero element in Picard group.\n\n</details>

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> Canonical bundle $$\Omega_X^1$$의 degree $$\deg \Omega_X^1$$는 다양체 $$X$$의 *genus* $$g$$와 관련이 있다.\n\n</div>

<details class="proof" markdown="1">
<summary>증명</summary>

For curves, degree is related to genus: $$\deg \Omega_C^1 = 2g - 2$$. For surfaces, degree is more complicated. General formula: $$\deg \Omega_X^1 = 2\chi(\mathcal{O}_X) - 2$$.\n\n</details>

## 주요 예시

정규 다발의 주요 예시를 살펴보겠다. 이들은 다양체의 canonical class를 이해하는 데 중요하다.

<div class="example" markdown="1">

<ins id="ex6">**예시 6**</ins> **Affine space** $$\mathbb{A}^n$$\n\n$$\Omega_{\mathbb{A}^n}^1 = \mathcal{O}_{\mathbb{A}^n}^{\oplus n}$$. Canonical class is trivial. $$\mathrm{Pic}(\mathbb{A}^n) = 0$$.\n\n</div>

<div class="example" markdown="1">

<ins id="ex7">**예시 7**</ins> **Projective space** $$\mathbb{P}^n$$\n\n$$\Omega_{\mathbb{P}^n}^1 = \mathcal{O}_{\mathbb{P}^n}(-n-1)$$. Canonical class is degree $$-n-1$$. $$\mathrm{Pic}(\mathbb{P}^n) \cong \mathbb{Z}$$. This is a fundamental result.\n\n</div>

<div class="example" markdown="1">

<ins id="ex8">**예시 8**</ins> **Quadric hypersurface** $$Q \subseteq \mathbb{P}^n$$\n\n$$\Omega_Q^1 = \mathcal{O}_Q(-n-1)$$. Canonical class is same as projective space because quadric is "stably equivalent".\n\n</div>

<div class="example" markdown="1">

<ins id="ex9">**예시 9**</ins> **Abelian variety** $$A$$\n\n$$\Omega_A^1 = \mathcal{O}_A^{\oplus n}$$. Canonical class is trivial. $$\mathrm{Pic}^0(A)$$ is large.\n\n</div>

<div class="example" markdown="1">

<ins id="ex10">**예시 10**</ins> **K3 surface** $$X$$\n\n$$\Omega_X^1$$ is torsion-free and has degree 0. $$\mathrm{Pic}(X) \cap H^1(X, \mathcal{O}_X) = 0$$. Canonical class is primitive.\n\n</div>

## Riemann-Roch Theorem과의 연결

정규 다발은 Riemann-Roch theorem을 연구하는 기초이다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> (Riemann-Roch for curves) Curve $$C$$의 genus $$g$$에 대해,\n\n$$\chi(C, \mathcal{O}_C(D)) = \deg D + 1 - g$$\n\n여기서 $$D$$는 divisor, $$\chi$$는 Euler characteristic.\n\n</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Riemann-Roch theorem for curves: $$\chi(C, \mathcal{L}) = \deg \mathcal{L} + 1 - g$$. This is fundamental for curve theory.\n\n</details>

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> (Riemann-Roch for surfaces) Surface $$X$$의 canonical class $$K_X$$에 대해,\n\n$$\chi(X, \mathcal{O}_X(D)) = \frac{1}{2}D \cdot (D - K_X) + \chi(\mathcal{O}_X)$$\n\n여기서 $$\cdot$$는 intersection product, $$\chi$$는 Euler characteristic.\n\n</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Riemann-Roch for surfaces extends the curve case. The canonical class appears in the formula because of the Todd class.\n\n</details>

<div class="example" markdown="1">

<ins id="ex11">**예시 11**</ins> **Genus 0 curve**: $$C \cong \mathbb{P}^1$$. $$\deg K_C = -2$$. Riemann-Roch: $$\chi(C, \mathcal{O}_C(D)) = \deg D + 1$$. This is consistent.\n\n</div>

<div class="example" markdown="1">

<ins id="ex12">**예시 12**</ins> **Genus 1 curve**: Elliptic curve $$E$$. $$\deg K_E = 0$$. Canonical bundle is trivial. Riemann-Roch: $$\chi(E, \mathcal{O}_E(D)) = \deg D$$. This is correct.\n\n</div>

---\n\n**참고문헌**\n\n**[Har]** J. Harris, *Algebraic Geometry: A First Course*, Springer, 1992.\n**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.\n**[Gr]** P. Griffiths and J. Harris, *Principles of Algebraic Geometry*, Wiley, 1978.\n**[Ful]** W. Fulton, *Intersection Theory*, Springer, 1984.\n