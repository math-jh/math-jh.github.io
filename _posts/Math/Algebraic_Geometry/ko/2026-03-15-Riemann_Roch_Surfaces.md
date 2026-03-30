---
title: "Riemann-Roch for Surfaces"
excerpt: "Intersection theory on surfaces and its applications"

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/riemann_roch_surfaces
sidebar: 
    nav: "algebraic_geometry-ko"

header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Riemann_Roch_Surfaces.png
    overlay_filter: 0.5

date: 2026-03-15
last_modified_at: 2026-03-15
weight: 17
published: false
---

## 도입

([§Riemann–Roch Theorem, ⁋명제 7](/ko/math/algebraic_geometry/riemann_roch_theorem#prop7))에서 우리는 surface $$S$$ 위의 divisor $$D$$에 대한 Riemann–Roch 공식을 얻었다:

$$\chi(\mathcal{O}_S(D)) = \chi(\mathcal{O}_S) + \frac{1}{2}(D^2 - D \cdot K_S)$$

이 공식에는 curve의 경우에는 등장하지 않는 항 $$D^2$$와 $$D \cdot K_S$$가 포함되어 있다. 이 항들은 surface 위에서 정의되는 **intersection number**라는 이차 형식의 값을 나타낸다. 이 글에서는 intersection number의 정의와 그 기본 성질을 다루고, 이를 활용하여 Hodge index theorem과 plurigenus에 대한 부등식을 증명한다.

## Intersection Number

Surface $$S$$ 위의 두 curve $$C, D$$를 생각하자. Riemann–Roch 공식에 $$D \cdot K_S$$라는 항이 등장하는 이유를 기하학적으로 이해하려면, 두 divisor가 "얼마나 교차하는지"를 측정하는 수치가 필요하다. 예를 들어, $$\mathbb{P}^2$$에서 degree $$d$$ curve $$C = dH$$와 line $$L = H$$의 교차점 수는 $$d$$개이며, 이것이 $$C \cdot L = d$$라는 교차수로 포착된다. 이 교차수는 Riemann–Roch 공식에서 self-intersection $$D^2$$와 $$D \cdot K_S$$의 값을 계산하는 데 필수적이다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Smooth surface $$S$$ 위의 두 divisor $$C, D$$의 **intersection number<sub>교차수</sub>** $$C \cdot D$$를 다음과 같이 정의한다:

$$C \cdot D = \chi(\mathcal{O}_S(C + D)) - \chi(\mathcal{O}_S(C)) - \chi(\mathcal{O}_S(D)) + \chi(\mathcal{O}_S)$$

</div>

이 정의는 곧 등장할 기하학적 해석을 통해서 직관을 얻을 수 있다. $$C$$와 $$D$$가 curve로서 transversally intersect할 때, 교차수는 단순히 교차점의 개수와 일치한다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> Intersection number는 다음 성질을 만족한다:

1. **Symmetry**: $$C \cdot D = D \cdot C$$
2. **Bilinearity**: $$(aC_1 + bC_2) \cdot D = a(C_1 \cdot D) + b(C_2 \cdot D)$$
3. **Linear equivalence**: $$C \sim C'$$이면 $$C \cdot D = C' \cdot D$$

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Symmetry은 정의에서 $$C + D = D + C$$이므로 자명하다.

Bilinearity의 경우, $$D_1, D_2$$에 대해 정의 1을 적용하면:

$$(C_1 + C_2) \cdot D = \chi(\mathcal{O}(C_1 + C_2 + D)) - \chi(\mathcal{O}(C_1 + C_2)) - \chi(\mathcal{O}(D)) + \chi(\mathcal{O}_S)$$

Riemann–Roch 공식 ([§Riemann–Roch Theorem, ⁋명제 7](/ko/math/algebraic_geometry/riemann_roch_theorem#prop7))에 의해 $$\chi(\mathcal{O}(E))$$는 $$E^2$$와 $$E \cdot K_S$$의 2차 함수이므로, 이 식은 $$C_1 \cdot D + C_2 \cdot D$$로 분해된다.

Linear equivalence $$C \sim C'$$, 즉 $$C - C' = (f)$$에 대해서는 $$\mathcal{O}(C) \cong \mathcal{O}(C')$$이므로 모든 cohomology 차원이 보존되어 교차수도 같다.

</details>

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3 (Geometric interpretation)**</ins> $$C, D$$가 smooth curve이고 transversally intersect하면:

$$C \cdot D = |C \cap D|$$

일반적으로 $$C \cdot D = \sum_{p \in C \cap D} (C \cdot D)_p$$이며, 여기서 $$(C \cdot D)_p$$는 $$p$$에서의 local intersection multiplicity이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

핵심 아이디어는 exact sequence

$$0 \to \mathcal{O}_S(-C) \to \mathcal{O}_S \to \mathcal{O}_C \to 0$$

를 활용하는 것이다. Tensor $$\mathcal{O}_S(D)$$를 취하면

$$0 \to \mathcal{O}_S(D - C) \to \mathcal{O}_S(D) \to \mathcal{O}_C(D) \to 0$$

가 얻어지며, cohomology long exact sequence에서

$$\chi(\mathcal{O}_S(D)) - \chi(\mathcal{O}_S(D - C)) = \chi(\mathcal{O}_C(D))$$

이다. $$C \cap D = \{p_1, \ldots, p_n\}$$일 때 $$\mathcal{O}_C(D)|_{p_i} \cong \mathcal{O}_{C, p_i} / (f_i)$$이며, 여기서 $$f_i$$는 $$D$$를 정의하는 local equation이다. 이로부터 $$\chi(\mathcal{O}_C(D)) = \sum_i \dim(\mathcal{O}_{C, p_i} / (f_i)) = \sum_i (C \cdot D)_{p_i}$$가 얻어진다. Transversal intersection의 경우 각 $$p_i$$에서 $$(C \cdot D)_{p_i} = 1$$이므로 교차수는 교차점의 개수와 일치한다.

</details>

## Serre Duality를 통한 표현

([§Serre Duality, ⁋명제 6](/ko/math/algebraic_geometry/serre_duality#prop6))에 의해 $$h^2(\mathcal{O}(D)) = h^0(\mathcal{O}(K_S - D))$$이다. 따라서 Riemann–Roch 공식은 다음과 같이 쓸 수 있다:

$$h^0(\mathcal{O}(D)) - h^1(\mathcal{O}(D)) + h^0(\mathcal{O}(K_S - D)) = \chi(\mathcal{O}_S) + \frac{1}{2}(D^2 - D \cdot K_S)$$

이 표현은 $$D$$에 대한 정보를 $$K_S - D$$에 대한 정보와 연결해 주며, 특히 $$h^1(\mathcal{O}(D))$$가 작을 때 $$h^0$$에 대한 강력한 추정을 제공한다.

## 예시: $$\mathbb{P}^1 \times \mathbb{P}^1$$

$$\mathbb{P}^2$$에 대한 Riemann–Roch 계산은 이미 ([§Riemann–Roch Theorem, ⁋예시 8](/ko/math/algebraic_geometry/riemann_roch_theorem#ex8))에서 다루었다. 여기서는 다른 근본적인 예시를 살펴본다.

<div class="example" markdown="1">

<ins id="ex4">**예시 4 ($$\mathbb{P}^1 \times \mathbb{P}^1$$)**</ins> $$\mathbb{P}^1 \times \mathbb{P}^1$$에 대해 $$K = -2H_1 - 2H_2$$ (여기서 $$H_1, H_2$$는 각 factor의 hyperplane class), $$\chi(\mathcal{O}) = 1$$이다. Intersection number는 $$H_1^2 = H_2^2 = 0$$, $$H_1 \cdot H_2 = 1$$을 만족한다. Bidegree $$(a, b)$$의 divisor $$D = aH_1 + bH_2$$에 대해:

$$\chi(\mathcal{O}(D)) = 1 + \frac{1}{2}(2ab + 2a + 2b) = (a+1)(b+1)$$

이것은 bidegree $$(a, b)$$ bihomogeneous polynomial의 parameter 개수와 일치한다.

</div>

## Hodge Index Theorem

교차 형식이 surface의 geometry에 대해 어떤 정보를 담고 있는지 알아보기 위해, 먼저 몇 가지 정의를 도입한다.

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> 두 divisor $$D_1, D_2$$가 **numerically equivalent<sub>수치적으로 동치</sub>** $$D_1 \equiv D_2$$라는 것은, 모든 divisor $$E$$에 대해 $$D_1 \cdot E = D_2 \cdot E$$인 것이다. Numerical equivalence class의 집합을

$$\operatorname{Num}(S) = \operatorname{Div}(S) / \{\text{numerical equivalence}\}$$

라고 하며, 교차 형식에 의해 $$\operatorname{Num}(S)$$는 자연스럽게 real vector space 위의 이차 형식을 갖는다.

</div>

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> Surface $$S$$의 **Néron–Severi group**은 ([§Divisors, ⁋정의 8](/ko/math/algebraic_geometry/divisors#def8))에서 정의한 Picard group $$\operatorname{Pic}(S)$$에서 algebraic equivalence를 취한 몫이다:

$$\operatorname{NS}(S) = \operatorname{Pic}(S) / \{\text{algebraic equivalence}\}$$

이것의 rank $$\rho(S) = \operatorname{rank} \operatorname{NS}(S)$$를 $$S$$의 **Picard number**라고 한다.

</div>

Algebraic equivalence는 numerical equivalence보다 강한 관계이므로 $$\operatorname{NS}(S) \otimes \mathbb{R}$$는 $$\operatorname{Num}(S)$$의 부분 공간이며, 특히 $$\rho(S) \le \operatorname{rank} \operatorname{Num}(S)$$이다. ([§선다발과 선형계, ⁋정의 10](/ko/math/algebraic_geometry/linear_systems#def10))에서 ample line bundle을 도입하였는데, ample divisor $$H$$는 교차 형식에 대해 특별한 역할을 한다.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7 (Hodge Index Theorem)**</ins> Smooth projective surface $$S$$와 ample divisor $$H$$에 대해, $$D \cdot H = 0$$이고 $$D \not\equiv 0$$이면 $$D^2 < 0$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명 (sketch)</summary>

$$D \cdot H = 0$$이고 $$D \not\equiv 0$$이라고 하자. $$m \gg 0$$에 대해 $$mH + D$$와 $$mH - D$$가 effective divisor가 되도록 $$m$$을 선택할 수 있다. Effectiveness에 의해 $$(mH + D)^2 \ge 0$$, $$(mH - D)^2 \ge 0$$이고, 이를 전개하면:

$$m^2 H^2 + 2m H \cdot D + D^2 = m^2 H^2 + D^2 \ge 0$$
$$m^2 H^2 - 2m H \cdot D + D^2 = m^2 H^2 + D^2 \ge 0$$

두 부등식이 동일하므로 $$D^2 \ge -m^2 H^2$$만 얻는다. 더 정밀한论证을 위해 $$D \cdot H = 0$$이라는 조건을 다르게 활용한다. $$H$$가 ample이므로, 충분히 큰 $$m$$에 대해 $$mH + tD$$가 effective가 되는 $$t$$의 범위를 고려하면, $$(mH + tD)^2 \ge 0$$에서 $$D^2 \le 0$$을 얻는다. 등호 $$D^2 = 0$$이 성립한다면 $$mH + tD$$와 $$mH - tD$$ 모두 effective가 되므로, $$D \cdot (mH + tD) = tD^2 = 0$$, $$D \cdot (mH - tD) = -tD^2 = 0$$이 성립한다. Riemann–Roch를 적용하면 $$D$$와 $$-D$$ 모두에 대해 section이 존재함을 보일 수 있고, 이로부터 $$D \equiv 0$$이 모순적으로 유도된다. 따라서 $$D^2 < 0$$이다.

</details>

<div class="corollary" markdown="1">

<ins id="cor8">**따름정리 8**</ins> 교차 형식 on $$\operatorname{Num}(S) \otimes \mathbb{R}$$는 signature $$(1, \rho - 1)$$를 갖는다. 즉, positive direction은 하나뿐이며, 이것은 ample cone에 의해 span된다.

</div>

Hodge index theorem의 기하학적 의미는 다음과 같다: surface 위의 교차 형식은 "시간" 방향 하나와 "공간" 방향 $$\rho - 1$$개를 갖는 Minkowski-type 이차 형식이다. 이는 surface의 birational geometry에서 깊은 결과들을 이끌어낸다.

## Application: Plurigenera

<div class="definition" markdown="1">

<ins id="def9">**정의 9**</ins> Surface $$S$$의 **$$m$$-th plurigenus**는

$$P_m(S) = h^0(S, \omega_S^{\otimes m})$$

이다. 여기서 $$\omega_S = \mathcal{O}_S(K_S)$$는 ([§Canonical Bundle, ⁋명제 5](/ko/math/algebraic_geometry/canonical_bundle#prop5))에서 정의한 canonical bundle이다.

</div>

Plurigenus는 surface의 birational equivalence class를 결정하는 중요한 불변량이다. ([§Canonical Bundle](/ko/math/algebraic_geometry/canonical_bundle))에서 살펴본 canonical bundle의 역할과 마찬가지로, $$\omega_S^{\otimes m}$$의 global section은 surface 위의 "multi-differential form"을 parameterize한다.

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10**</ins> $$m \ge 1$$에 대해

$$P_m(S) \ge \chi(\mathcal{O}_S) + \frac{m(m-1)}{2} K_S^2 - h^1(\omega_S^{\otimes m})$$

특히 $$K_S$$가 ample이고 $$m \gg 0$$이면 $$h^1(\omega_S^{\otimes m}) = 0$$이 되어

$$P_m(S) = \chi(\mathcal{O}_S) + \frac{m(m-1)}{2} K_S^2$$

이 성립한다.

</div>

<details class="proof" markdown="1">
<summary>증명 (sketch)</summary>

Riemann–Roch 공식 ([§Riemann–Roch Theorem, ⁋명제 7](/ko/math/algebraic_geometry/riemann_roch_theorem#prop7))에 $$D = mK_S$$를 대입한다:

$$\chi(\omega_S^{\otimes m}) = \chi(\mathcal{O}_S) + \frac{1}{2}\left((mK_S)^2 - (mK_S) \cdot K_S\right) = \chi(\mathcal{O}_S) + \frac{1}{2}\left(m^2 K_S^2 - m K_S^2\right)$$

$$= \chi(\mathcal{O}_S) + \frac{m(m-1)}{2} K_S^2$$

Serre duality에 의해 $$h^2(\omega_S^{\otimes m}) = h^0(\omega_S^{(1-m)})$$이며, $$m \ge 2$$이면 $$K_S^{1-m}$$의 degree가 음수이므로 $$h^0 = 0$$이다. 따라서

$$P_m(S) = h^0(\omega_S^{\otimes m}) = \chi(\omega_S^{\otimes m}) + h^1(\omega_S^{\otimes m}) - h^2(\omega_S^{\otimes m}) \ge \chi(\omega_S^{\otimes m})$$

$$h^1(\omega_S^{\otimes m})$$ 항을 정리하면 첫 번째 부등식이 얻어진다. $$K_S$$가 ample이면 Kodaira vanishing theorem에 의해 $$m \gg 0$$에서 $$h^1(\omega_S^{\otimes m}) = 0$$이 되어 등식이 성립한다.

</details>

## 예시: K3 Surface

<div class="definition" markdown="1">

<ins id="def11">**정의 11**</ins> Smooth projective surface $$S$$가 **K3 surface**라는 것은 다음 두 조건을 만족하는 것이다:
1. $$K_S \sim 0$$ (trivial canonical bundle)
2. $$h^1(S, \mathcal{O}_S) = 0$$

</div>

$$K_S \sim 0$$이므로 Riemann–Roch 공식은 단순해진다:

$$\chi(\mathcal{O}_S(D)) = \chi(\mathcal{O}_S) + \frac{D^2}{2}$$

$$h^1(S, \mathcal{O}_S) = 0$$과 Serre duality $$h^2(\mathcal{O}_S) = h^0(K_S) = h^0(\mathcal{O}_S) = 1$$에 의해 $$\chi(\mathcal{O}_S) = 1 - 0 + 1 = 2$$이다. 따라서:

$$\chi(\mathcal{O}_S(D)) = 2 + \frac{D^2}{2}$$

이 공식에서 $$D^2 \ge -2$$이면 $$\chi(\mathcal{O}_S(D)) \ge 1$$이 되어 $$h^0(\mathcal{O}(D)) \ge 1$$, 즉 $$D$$가 linearly equivalent한 effective divisor가 존재함을 알 수 있다. K3 surface의 이름은 Kummer, Kähler, Kodaira에서 따온 것이다 ([BHPV]).

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[BHPV]** W. Barth, K. Hulek, C. Peters, A. Van de Ven, *Compact Complex Surfaces*, Springer, 2004.
