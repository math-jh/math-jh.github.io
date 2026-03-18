---
title: "Sheaves on Varieties"
excerpt: "Presheaves, sheaves, and locally free sheaves on algebraic varieties"

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/sheaves_on_varieties
sidebar: 
    nav: "algebraic_geometry-ko"

header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Sheaves_on_Varieties.png
    overlay_filter: 0.5

date: 2026-03-15
last_modified_at: 2026-03-15
weight: 15
---

## 도입

Variety $$X$$를 연구할 때, $$X$$ 위의 "함수들"을 이해하는 것이 중요하다. 하지만 단순히 전역 함수 $$\mathcal{O}(X)$$만 고려하는 것으로는 부족하다. 각 열린집합 $$U \subseteq X$$ 위의 함수 $$\mathcal{O}(U)$$를 함께 고려해야 $$X$$의 국소적 성질을 파악할 수 있다.

**Sheaf**는 이러한 "함수들의 체계"를 형식화한 도구이다. Sheaf는 위상공간 위에 정의된 대수적 구조로, 국소적 데이터를 전역적 데이터와 연결해준다.

## Presheaf와 Sheaf

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 위상공간 $$X$$ 위의 **presheaf<sub>전층</sub>** $$\mathcal{F}$$는 다음 데이터로 구성된다:

1. 각 열린집합 $$U \subseteq X$$에 대해 abelian group $$\mathcal{F}(U)$$
2. 각 inclusion $$V \subseteq U$$에 대해 restriction map $$\rho_{UV}: \mathcal{F}(U) \to \mathcal{F}(V)$$

이들이 다음을 만족한다:
- $$\mathcal{F}(\emptyset) = 0$$
- $$\rho_{UU} = \operatorname{id}$$
- $$W \subseteq V \subseteq U$$이면 $$\rho_{UW} = \rho_{VW} \circ \rho_{UV}$$

</div>

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> Presheaf $$\mathcal{F}$$가 **sheaf<sub>층</sub>**라는 것은 다음 두 조건을 만족하는 것이다:

1. **Locality**: 열린집합 $$U$$의 open cover $$\{U_i\}$$와 $$s, t \in \mathcal{F}(U)$$에 대해, 모든 $$i$$에 대해 $$s|_{U_i} = t|_{U_i}$$이면 $$s = t$$이다.

2. **Gluing**: 열린집합 $$U$$의 open cover $$\{U_i\}$$와 $$s_i \in \mathcal{F}(U_i)$$에 대해, 모든 $$i, j$$에 대해 $$s_i|_{U_i \cap U_j} = s_j|_{U_i \cap U_j}$$이면 $$s \in \mathcal{F}(U)$$가 존재하여 $$s|_{U_i} = s_i$$이다.

</div>

<div class="example" markdown="1">

<ins id="ex3">**예시 3 (Structure sheaf)**</ins> Variety $$X$$의 **structure sheaf<sub>구조층</sub>** $$\mathcal{O}_X$$는 각 열린집합 $$U$$에 정칙함수 $$\mathcal{O}_X(U)$$를 대응시킨다. 이것은 sheaf이다.

</div>

<div class="example" markdown="1">

<ins id="ex4">**예시 4 (Constant presheaf)**</ins> 위상공간 $$X$$와 abelian group $$A$$에 대해, 모든 열린집합 $$U \neq \emptyset$$에 대해 $$\mathcal{F}(U) = A$$로 정의하면 이것은 presheaf이지만 일반적으로 sheaf가 아니다.

Sheaf로 만들려면 **constant sheaf** $$\underline{A}$$를 정의해야 한다: $$\underline{A}(U)$$는 $$U$$ 위의 locally constant function $$U \to A$$이다.

</div>

## Stalk과 Sheafification

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> 점 $$x \in X$$에서의 **stalk<sub>줄기</sub>** $$\mathcal{F}_x$$를 다음과 같이 정의한다:

$$\mathcal{F}_x = \varinjlim_{U \ni x} \mathcal{F}(U)$$

즉, $$x$$의 열린근방 $$U$$ 위의 section들의 direct limit이다.

</div>

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> Presheaf $$\mathcal{F}$$에 대해, 이를 포함하는 최소의 sheaf $$\mathcal{F}^+$$가 존재한다. 이를 **sheafification<sub>층화</sub>**이라 한다.

</div>

## Locally Free Sheaf

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> $$\mathcal{O}_X$$-module $$\mathcal{E}$$가 **locally free<sub>국소 자유 층</sub>**라는 것은 각 점 $$x \in X$$에 대해 열린근방 $$U$$와 isomorphism $$\mathcal{E}|_U \cong \mathcal{O}_U^{\oplus r}$$가 존재하는 것이다.

Rank $$r$$의 locally free sheaf는 rank $$r$$의 vector bundle에 대응한다. Rank 1의 locally free sheaf는 line bundle (= invertible sheaf)이다.

</div>

<div class="example" markdown="1">

<ins id="ex8">**예시 8 (Tangent sheaf)**</ins> Smooth variety $$X$$의 **tangent sheaf<sub>접선층</sub>** $$\mathcal{T}_X$$는 vector field들의 sheaf이다. 이것은 rank $$n = \dim X$$의 locally free sheaf이다.

</div>

<div class="example" markdown="1">

<ins id="ex9">**예시 9 (Cotangent sheaf)**</ins> $$\Omega_X^1 = \mathcal{T}_X^\vee$$는 cotangent sheaf이다. Rank $$n$$의 locally free sheaf이다.

</div>

## Sheaf Hom과 Tensor

<div class="definition" markdown="1">

<ins id="def10">**정의 10**</ins> 두 $$\mathcal{O}_X$$-module $$\mathcal{F}, \mathcal{G}$$에 대해:

$$\mathscr{H}om_{\mathcal{O}_X}(\mathcal{F}, \mathcal{G})(U) = \operatorname{Hom}_{\mathcal{O}_U}(\mathcal{F}|_U, \mathcal{G}|_U)$$

$$\mathcal{F} \otimes_{\mathcal{O}_X} \mathcal{G}(U) = \mathcal{F}(U) \otimes_{\mathcal{O}_X(U)} \mathcal{G}(U)$$

</div>

<div class="proposition" markdown="1">

<ins id="prop11">**명제 11**</ins> $$\mathcal{E}$$가 locally free of rank $$r$$이면 $$\mathscr{H}om(\mathcal{E}, \mathcal{F}) \cong \mathcal{E}^\vee \otimes \mathcal{F}$$이다. 여기서 $$\mathcal{E}^\vee = \mathscr{H}om(\mathcal{E}, \mathcal{O}_X)$$는 dual이다.

</div>

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[God]** R. Godement, *Topologie algébrique et théorie des faisceaux*, Hermann, 1958.
