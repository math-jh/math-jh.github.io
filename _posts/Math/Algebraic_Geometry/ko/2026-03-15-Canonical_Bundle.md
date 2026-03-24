---
title: "Canonical Bundle"
excerpt: "Canonical bundle and canonical divisor"

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/canonical_bundle
sidebar:
    nav: "algebraic_geometry-ko"

header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Canonical_Bundle.png
    overlay_filter: 0.5

date: 2026-03-15
last_modified_at: 2026-03-15
weight: 13

---

([§Linear Systems](/ko/math/algebraic_geometry/linear_systems))에서 우리는 line bundle의 global sections들이 projective space를 형성함을 보았다. 이제 우리는 다양체의 가장 중요한 line bundle 중 하나인 *canonical bundle*을 소개한다. Canonical bundle은 다양체의 "자연스러운" line bundle로, differential form들의 bundle이다.

Canonical bundle은 Serre duality, Riemann-Roch theorem 등 대수기하학의 가장 중요한 정리들에서 핵심적인 역할을 한다. 또한 canonical bundle은 다양체의 "orientation"과 밀접하게 관련되어 있으며, 다양체가 "얼마나 휘어있는지"를 측정하는 도구이다.

## Cotangent Bundle

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Smooth variety $$X$$의 *cotangent sheaf* $$\Omega_X^1$$는 각 점 $$p \in X$$에서 Zariski cotangent space $$T_p^\ast X = \mathfrak{m}_p/\mathfrak{m}_p^2$$를 fiber로 갖는 sheaf이다. 여기서 $$\mathfrak{m}_p$$는 $$p$$에서의 maximal ideal이다.

</div>

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> Affine variety $$X = \operatorname{Spec} A$$에서 $$\Omega_X^1$$는 Kähler differentials $$\Omega_{A/\mathbb{K}}^1$$의 sheaf이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Kähler differentials $$\Omega_{A/\mathbb{K}}^1$$는 $$A$$-module로, universal property를 만족한다. 각 점 $$p$$에서의 stalk은 $$\Omega_{A/\mathbb{K}}^1 \otimes_A \kappa(p)$$이고, 이는 $$\mathfrak{m}_p/\mathfrak{m}_p^2$$와 자연스럽게 동형이다.

</details>

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> **$$\mathbb{A}^n$$의 cotangent sheaf**: $$\Omega_{\mathbb{A}^n}^1 \cong \mathcal{O}_{\mathbb{A}^n}^{\oplus n}$$이다. 이는 coordinate ring $$\mathbb{K}[\x_1, \ldots, \x_n]$$의 Kähler differentials이 free module $$\bigoplus_{i=1}^n \mathbb{K}[\x_1, \ldots, \x_n] d\x_i$$이기 때문이다.

</div>

## Canonical Bundle의 정의

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> Smooth variety $$X$$ of dimension $$n$$의 *canonical sheaf* (또는 *canonical bundle*) $$\omega_X$$는 cotangent sheaf의 top exterior power이다.

$$\omega_X = \bigwedge^n \Omega_X^1$$

</div>

Canonical bundle은 $$n$$-form들의 sheaf이다. 각 점 $$p$$에서 fiber는 $$\bigwedge^n T_p^\ast X$$이고, 이는 1차원 벡터공간이다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> Canonical sheaf $$\omega_X$$는 invertible sheaf이다. 즉, line bundle이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$\Omega_X^1$$은 locally free sheaf of rank $$n$$이고, 그 top exterior power는 locally free sheaf of rank 1이다. 따라서 $$\omega_X$$는 invertible sheaf이다.

</details>

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> Canonical bundle $$\omega_X$$에 대응하는 divisor를 *canonical divisor*라 하고 $$K_X$$로 표기한다. 즉, $$\omega_X \cong \mathcal{O}_X(K_X)$$이다.

</div>

Canonical divisor는 유일하게 결정되지 않고 linear equivalence class만이 잘 정의된다. 즉, $$K_X$$는 $$\operatorname{Cl}(X)$$의 원소이다.

## 예시들

<div class="example" markdown="1">

<ins id="ex7">**예시 7**</ins> **$$\mathbb{A}^n$$의 canonical bundle**: $$\omega_{\mathbb{A}^n} \cong \mathcal{O}_{\mathbb{A}^n}$$이다. 이는 [예시 3](#ex3)에서 $$\Omega_{\mathbb{A}^n}^1 \cong \mathcal{O}_{\mathbb{A}^n}^{\oplus n}$$이므로

$$\omega_{\mathbb{A}^n} = \bigwedge^n \Omega_{\mathbb{A}^n}^1 \cong \bigwedge^n \mathcal{O}_{\mathbb{A}^n}^{\oplus n} \cong \mathcal{O}_{\mathbb{A}^n}$$

이기 때문이다. 따라서 $$K_{\mathbb{A}^n} \sim 0$$이다.

</div>

<div class="example" markdown="1">

<ins id="ex8">**예시 8**</ins> **$$\mathbb{P}^n$$의 canonical bundle**: $$\omega_{\mathbb{P}^n} \cong \mathcal{O}_{\mathbb{P}^n}(-n-1)$$이다. Canonical divisor는 $$K_{\mathbb{P}^n} = -(n+1)H$$이다. 여기서 $$H$$는 hyperplane divisor이다.

</div>

<div class="example" markdown="1">

<ins id="ex9">**예시 9**</ins> **Smooth curve의 canonical bundle**: 기약 smooth projective curve $$C$$에 대해, $$\omega_C$$는 regular 1-form들의 sheaf이다. Canonical divisor $$K_C$$는 degree $$2g-2$$를 갖는다. 여기서 $$g$$는 $$C$$의 genus이다.

</div>

## Adjunction Formula

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10**</ins> (Adjunction Formula) Smooth variety $$X$$의 smooth divisor $$D$$에 대해

$$\omega_D \cong \omega_X \otimes \mathcal{O}_X(D)|_D$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Exact sequence $$0 \to \mathcal{I}_D/\mathcal{I}_D^2 \to \Omega_X^1|_D \to \Omega_D^1 \to 0$$으로부터

$$\omega_D \cong \omega_X|_D \otimes \det(\mathcal{I}_D/\mathcal{I}_D^2)^{-1}$$

을 얻는다. 여기서 $$\mathcal{I}_D/\mathcal{I}_D^2 \cong \mathcal{O}_X(-D)|_D$$이므로

$$\omega_D \cong \omega_X|_D \otimes \mathcal{O}_X(D)|_D$$

이다.

</details>

Adjunction formula는 divisor의 canonical bundle을 ambient variety의 canonical bundle로 표현한다. 이는 hypersurface의 canonical bundle을 계산하는 데 매우 유용하다.

<div class="example" markdown="1">

<ins id="ex11">**예시 11**</ins> **Smooth plane curve**: $$C \subset \mathbb{P}^2$$가 degree $$d$$의 smooth curve라 하자. Adjunction formula에 의해

$$\omega_C \cong \omega_{\mathbb{P}^2}|_C \otimes \mathcal{O}_{\mathbb{P}^2}(C)|_C \cong \mathcal{O}_{\mathbb{P}^2}(-3)|_C \otimes \mathcal{O}_{\mathbb{P}^2}(d)|_C \cong \mathcal{O}_C(d-3)$$

이다. 따라서 $$K_C \sim (d-3)H|_C$$이다. 여기서 $$H$$는 $$\mathbb{P}^2$$의 hyperplane이다.

</div>

## Dualizing Sheaf

Canonical bundle은 *dualizing sheaf*의 관점에서도 이해할 수 있다. 이는 Serre duality와 밀접하게 관련되어 있다.

<div class="proposition" markdown="1">

<ins id="prop12">**명제 12**</ins> (Serre Duality) Smooth projective variety $$X$$ of dimension $$n$$에 대해, 임의의 coherent sheaf $$\mathcal{F}$$에 대하여

$$H^i(X, \mathcal{F})^\ast \cong H^{n-i}(X, \omega_X \otimes \mathcal{F}^\vee)$$

이다.

</div>

Serre duality는 cohomology group 사이의 duality를 제공한다. 이는 특히 $$H^n(X, \omega_X) \cong \mathbb{K}$$임을 의미한다.

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.
