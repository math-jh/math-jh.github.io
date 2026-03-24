---
title: "Riemann-Roch for Surfaces"
excerpt: "The Riemann-Roch theorem for algebraic surfaces"

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/riemann_roch_surfaces
sidebar: 
    nav: "algebraic_geometry-ko"

header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Riemann_Roch_Surfaces.png
    overlay_filter: 0.5

date: 2026-03-15
last_modified_at: 2026-03-15
weight: 20
---

## 도입

이전 글 ([§Riemann-Roch](/ko/math/algebraic_geometry/riemann_roch))에서 우리는 curve를 위한 Riemann-Roch theorem을 살펴보았다. 이제 이를 **surface** (2차원 variety)로 일반화한다.

Surface를 위한 Riemann-Roch는 intersection number를 포함하며, curve의 경우보다 더 복잡하지만 더 풍부한 정보를 제공한다.

## Intersection Number

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Smooth surface $$S$$ 위의 두 divisor $$C, D$$의 **intersection number<sub>교차수</sub>** $$C \cdot D$$를 다음과 같이 정의한다:

$$C \cdot D = \dim \Gamma(S, \mathcal{O}(C + D)) - \dim \Gamma(S, \mathcal{O}(C)) - \dim \Gamma(S, \mathcal{O}(D)) + \dim \Gamma(S, \mathcal{O}_S)$$

</div>

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> Intersection number의 성질:

1. **Symmetry**: $$C \cdot D = D \cdot C$$
2. **Bilinearity**: $$(aC_1 + bC_2) \cdot D = a(C_1 \cdot D) + b(C_2 \cdot D)$$
3. **Linear equivalence**: $$C \sim C'$$이면 $$C \cdot D = C' \cdot D$$

</div>

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3 (Geometric interpretation)**</ins> $$C, D$$가 smooth curve이고 transversally intersect하면:

$$C \cdot D = |C \cap D|$$

일반적으로 $$C \cdot D = \sum_{p \in C \cap D} (C \cdot D)_p$$ (local intersection multiplicity의 합)

</div>

## Riemann-Roch Theorem

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4 (Riemann-Roch for Surfaces)**</ins> Smooth projective surface $$S$$와 divisor $$D$$에 대해:

$$\chi(\mathcal{O}(D)) = \chi(\mathcal{O}_S) + \frac{1}{2}(D^2 - D \cdot K_S)$$

여기서:
- $$D^2 = D \cdot D$$ (self-intersection)
- $$K_S$$는 canonical divisor
- $$\chi(\mathcal{O}(D)) = h^0(\mathcal{O}(D)) - h^1(\mathcal{O}(D)) + h^2(\mathcal{O}(D))$$

</div>

<div class="corollary" markdown="1">

<ins id="cor5">**따름정리 5 (Noether's Formula)**</ins>

$$\chi(\mathcal{O}_S) = \frac{1}{12}(K_S^2 + c_2(S))$$

여기서 $$c_2(S)$$는 second Chern class (topological Euler characteristic과 같음).

</div>

## Serre Duality를 통한 표현

<div class="corollary" markdown="1">

<ins id="cor6">**따름정리 6**</ins> Serre duality에 의해 $$h^2(\mathcal{O}(D)) = h^0(\mathcal{O}(K_S - D))$$이므로:

$$h^0(\mathcal{O}(D)) - h^1(\mathcal{O}(D)) + h^0(\mathcal{O}(K_S - D)) = \chi(\mathcal{O}_S) + \frac{1}{2}(D^2 - D \cdot K_S)$$

</div>

## 예시들

<div class="example" markdown="1">

<ins id="ex7">**예시 7 ($$\mathbb{P}^2$$)**</ins> $$\mathbb{P}^2$$에 대해:
- $$K_{\mathbb{P}^2} = -3H$$
- $$\chi(\mathcal{O}_{\mathbb{P}^2}) = 1$$
- $$H^2 = 1$$

Degree $$d$$ curve $$C = dH$$에 대해:

$$\chi(\mathcal{O}(C)) = 1 + \frac{1}{2}(d^2 + 3d) = \frac{(d+1)(d+2)}{2}$$

이것은 degree $$d$$ homogeneous polynomial의 차원과 일치한다.

</div>

<div class="example" markdown="1">

<ins id="ex8">**예시 8 ($$\mathbb{P}^1 \times \mathbb{P}^1$$)**</ins> $$\mathbb{P}^1 \times \mathbb{P}^1$$에 대해:
- $$K = -2H_1 - 2H_2$$ (여기서 $$H_1, H_2$$는 각 factor의 hyperplane)
- $$\chi(\mathcal{O}) = 1$$
- $$H_1^2 = H_2^2 = 0$$, $$H_1 \cdot H_2 = 1$$

Bidegree $$(a, b)$$의 divisor $$D = aH_1 + bH_2$$에 대해:

$$\chi(\mathcal{O}(D)) = 1 + \frac{1}{2}(2ab - (-2a - 2b)) = 1 + ab + a + b = (a+1)(b+1)$$

</div>

<div class="example" markdown="1">

<ins id="ex9">**예시 9 (K3 Surface)**</ins> K3 surface $$S$$는:
- $$K_S \sim 0$$
- $$\chi(\mathcal{O}_S) = 2$$

Riemann-Roch:

$$\chi(\mathcal{O}(D)) = 2 + \frac{D^2}{2}$$

</div>

## Hodge Index Theorem

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10 (Hodge Index)**</ins> Smooth projective surface $$S$$와 ample divisor $$H$$에 대해, $$D \cdot H = 0$$이고 $$D \not\sim 0$$이면 $$D^2 < 0$$이다.

</div>

<div class="corollary" markdown="1">

<ins id="cor11">**따름정리 11**</ins> Intersection form on $$\operatorname{Num}(S) = \operatorname{Div}(S) / \{\text{numerical equivalence}\}$$는 signature $$(1, \rho - 1)$$를 갖는다. 여기서 $$\rho = \operatorname{rank} \operatorname{NS}(S)$$는 Picard number이다.

</div>

## Application: Plurigenera

<div class="definition" markdown="1">

<ins id="def12">**정의 12**</ins> Surface $$S$$의 **$$m$$-th plurigenus**:

$$P_m(S) = h^0(S, \omega_S^{\otimes m})$$

</div>

<div class="proposition" markdown="1">

<ins id="prop13">**명제 13**</ins> Riemann-Roch에 의해:

$$P_m(S) \geq \chi(\mathcal{O}_S) + \frac{m(m-1)}{2} K_S^2 - h^1(\omega_S^{\otimes m})$$

$$K_S$$가 ample이고 $$m \gg 0$$이면 equality가 성립한다.

</div>

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[BHPV]** W. Barth, K. Hulek, C. Peters, A. Van de Ven, *Compact Complex Surfaces*, Springer, 2004.
