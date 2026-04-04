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

이 공식은 curve의 Riemann–Roch 정리의 자연스러운 일반화이다. Curve $$C$$ 위에서는 임의의 divisor $$D$$에 대해 $$\dim H^0(C, \mathcal{O}(D)) - \dim H^1(C, \mathcal{O}(D)) = \deg D + 1 - g$$가 성립하였는데, 여기서 $$\deg D$$는 선형인 항이었다. 반면 surface로 넘어가면 새로운 현상이 나타난다. 위 공식에는 $$D^2 := D \cdot D$$ (self-intersection)와 $$D \cdot K_S$$라는 이차항이 등장하며, 이들은 surface 위의 두 divisor가 "얼마나 교차하는지"를 측정하는 intersection number로 이해된다.

이러한 이차항들이 등장하는 이유는 근본적으로 surface가 curve보다 한 차원 높다는 데 있다. Curve 위에서는 divisor들이 점들의 유한 집합이므로 두 divisor의 "교차"라는 개념이 자명하지만, surface 위에서는 두 curve가 일반적으로 유한 개의 점에서 만나며 그 만남의 정도를 정량화하는 것이 필수적이다. 이러한 정량화는 단순히 교차점의 개수를 세는 것 이상으로, divisor의 self-intersection이라는 개념까지 자연스럽게 이끈다. 예를 들어 $$\mathbb{P}^2$$에서 두 직선은 항상 한 점에서 만나지만, 하나의 직선을 "자기 자신과" 교차시키는 것은 직관적으로는 불가능해 보인다. 그러나 linear equivalence를 통해 이를 엄밀하게 정의할 수 있으며, 이때 $$\ell \sim \ell'$$인 다른 직선 $$\ell'$$을 택하면 $$\ell \cdot \ell' = 1$$이 되어 $$\ell^2 = 1$$을 얻는다.

이 글에서는 intersection number의 정의와 그 기본 성질을 다루고, 이를 활용하여 Hodge index theorem과 plurigenus에 대한 부등식을 증명한다. 또한 교차 형식이 surface의 birational geometry에서 갖는 의미를 살펴본다.

## Intersection Number

Surface $$S$$ 위의 두 curve $$C, D$$를 생각하자. Curve의 세계에서는 divisor가 점들의 유한 집합이었으므로, 두 divisor의 "교차"를 논하는 것은 의미가 없었다. 그러나 surface에서는 두 curve가 일반적으로 유한 개의 점에서 만나며, 이 만남의 기하학적 정보—특히 교차점의 수와 각 교차점에서의 multiplicity—는 surface의 birational geometry를 이해하는 데 핵심적인 역할을 한다.

Riemann–Roch 공식에 $$D \cdot K_S$$라는 항이 등장하는 이유를 기하학적으로 이해하려면, 두 divisor가 "얼마나 교차하는지"를 측정하는 수치가 필요하다. 예를 들어, $$\mathbb{P}^2$$에서 degree $$d$$ curve $$C = dH$$와 line $$L = H$$의 교차점 수는 $$d$$개이며, 이것이 $$C \cdot L = d$$라는 교차수로 포착된다. 이 교차수는 Riemann–Roch 공식에서 self-intersection $$D^2$$와 $$D \cdot K_S$$의 값을 계산하는 데 필수적이다.

우리의 출발점은 다소 추상적으로 보일 수 있는 Euler characteristic을 이용한 정의이다. 이 정의의 장점은 linear equivalence에 대해 불변이라는 사실이 즉시 따라온다는 것이며, 곧 기하학적 해석을 통해 이것이 실제로 교차점의 수를 세고 있음을 확인할 것이다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Smooth surface $$S$$ 위의 두 divisor $$C, D$$의 *intersection number<sub>교차수</sub>* $$C \cdot D$$를 다음과 같이 정의한다:

$$C \cdot D = \chi(\mathcal{O}_S(C + D)) - \chi(\mathcal{O}_S(C)) - \chi(\mathcal{O}_S(D)) + \chi(\mathcal{O}_S)$$

</div>

이 정의는 곧 [명제 3](#prop3)의 기하학적 해석을 통해서 직관을 얻을 수 있다. $$C$$와 $$D$$가 curve로서 transversally intersect할 때, 교차수는 단순히 교차점의 개수와 일치한다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> Intersection number는 다음 성질을 만족한다. 우선 **symmetry** $$C \cdot D = D \cdot C$$가 성립하며, 첫 번째 변수에 대해 **bilinearity** $$(aC_1 + bC_2) \cdot D = a(C_1 \cdot D) + b(C_2 \cdot D)$$가 성립한다. 마지막으로 **linear equivalence에 대한 불변성**, 즉 $$C \sim C'$$이면 $$C \cdot D = C' \cdot D$$가 성립한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Symmetry는 정의에서 $$C + D = D + C$$이므로 자명하다.

Bilinearity를 보이자. 우선 첫 번째 변수에 대한 additivity를 확인한다. 정의에 의해

$$(C_1 + C_2) \cdot D = \chi(\mathcal{O}(C_1 + C_2 + D)) - \chi(\mathcal{O}(C_1 + C_2)) - \chi(\mathcal{O}(D)) + \chi(\mathcal{O}_S)$$

이며, 한편

$$C_1 \cdot D + C_2 \cdot D = \chi(\mathcal{O}(C_1 + D)) - \chi(\mathcal{O}(C_1)) - \chi(\mathcal{O}(D)) + \chi(\mathcal{O}_S) \\+ \chi(\mathcal{O}(C_2 + D)) - \chi(\mathcal{O}(C_2)) - \chi(\mathcal{O}(D)) + \chi(\mathcal{O}_S)$$

이다. 이들의 차를 구하면

$$(C_1 + C_2) \cdot D - (C_1 \cdot D + C_2 \cdot D) \\= \bigl(\chi(\mathcal{O}(C_1 + C_2 + D)) - \chi(\mathcal{O}(C_1 + D)) - \chi(\mathcal{O}(C_2 + D)) + \chi(\mathcal{O}(D))\bigr) \\- \bigl(\chi(\mathcal{O}(C_1 + C_2)) - \chi(\mathcal{O}(C_1)) - \chi(\mathcal{O}(C_2)) + \chi(\mathcal{O}_S)\bigr)$$

이다. 이 차이가 0임을 보이는 핵심은 Snapper의 정리이다. 즉, coherent sheaf $$\mathcal{F}$$에 대해 함수 $$\operatorname{Pic}(S) \to \mathbb{Z}$$, $$D \mapsto \chi(\mathcal{F} \otimes \mathcal{O}(D))$$는 $$\operatorname{Pic}(S)$$ 위에서 차수 $$\le \dim S = 2$$의 polynomial이라는 것이다. 이로부터 임의의 세 line bundle $$L_1, L_2, L_3$$에 대해 third difference

$$\Delta^3 \chi(\mathcal{F}; L_1, L_2, L_3) := \sum_{I \subseteq \{1,2,3\}} (-1)^{3-|I|} \chi\left(\mathcal{F} \otimes \bigotimes_{i \in I} L_i\right) = 0$$

이 성립한다. $$\mathcal{F} = \mathcal{O}_S$$로 놓고 $$L_1 = \mathcal{O}(C_1)$$, $$L_2 = \mathcal{O}(C_2)$$, $$L_3 = \mathcal{O}(D)$$로 택하면, 위 식의 전개가 정확히

$$\bigl(\chi(\mathcal{O}(C_1 + C_2 + D)) - \chi(\mathcal{O}(C_1 + D)) - \chi(\mathcal{O}(C_2 + D)) + \chi(\mathcal{O}(D))\bigr) \\- \bigl(\chi(\mathcal{O}(C_1 + C_2)) - \chi(\mathcal{O}(C_1)) - \chi(\mathcal{O}(C_2)) + \chi(\mathcal{O}_S)\bigr) = 0$$

이 되어 additivity가 성립한다. Scalar multiplication의 경우, $$nC \cdot D$$가 $$n$$에 대해 차수 2 이하의 polynomial이므로 $$(n+1)C \cdot D - nC \cdot D - C \cdot D$$를 계산하면 역시 third difference가 되어 선형성이 따른다.

Linear equivalence $$C \sim C'$$, 즉 $$C - C' = (f)$$에 대해서는 $$\mathcal{O}(C) \cong \mathcal{O}(C')$$이므로 모든 cohomology 차원이 보존되어 교차수도 같다.

</details>

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3 (Geometric interpretation)**</ins> $$C, D$$가 공통 성분을 갖지 않는 curve이고 transversally intersect하면:

$$C \cdot D = \lvert C \cap D \rvert$$

일반적으로 $$C \cdot D = \sum_{p \in C \cap D} (C \cdot D)_p$$이며, 여기서 $$(C \cdot D)_p$$는 $$p$$에서의 local intersection multiplicity이다. 만약 $$C$$와 $$D$$가 공통 성분 $$F$$를 갖는다면 $$C \cdot D$$는 $$F$$를 따른 무한한 교차를 포함하게 되므로, 교차수의 기하학적 해석을 위해서는 공통 성분이 없다는 조건이 필수적이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

핵심 아이디어는 exact sequence

$$0 \to \mathcal{O}_S(-C) \to \mathcal{O}_S \to \mathcal{O}_C \to 0$$

를 활용하는 것이다. 이 sequence에서 첫 번째 사상은 effective divisor $$C$$를 정의하는 global section $$s_C \in H^0(\mathcal{O}_S(C))$$에 의한 곱셈 $$\mathcal{O}_S(-C) \to \mathcal{O}_S$$, 즉 $$1 \mapsto s_C$$이며, 두 번째 사상은 restriction $$\mathcal{O}_S \to \mathcal{O}_S/\mathcal{O}_S(-C) \cong \mathcal{O}_C$$이다. 양변에 $$\mathcal{O}_S(D)$$를 tensor하면

$$0 \to \mathcal{O}_S(D - C) \to \mathcal{O}_S(D) \to \mathcal{O}_C(D) \to 0$$

를 얻는다. 여기서 $$\mathcal{O}_C(D) = \mathcal{O}_S(D)\vert_C$$는 line bundle $$\mathcal{O}_S(D)$$의 curve $$C$$ 위로의 제한이다. 이 exact sequence의 cohomology long exact sequence에서 Euler characteristic을 취하면

$$\chi(\mathcal{O}_S(D)) - \chi(\mathcal{O}_S(D - C)) = \chi(\mathcal{O}_C(D))$$

이다. 한편 교차수의 정의에 의해

$$C \cdot D = \chi(\mathcal{O}(C + D)) - \chi(\mathcal{O}(C)) - \chi(\mathcal{O}(D)) + \chi(\mathcal{O}_S)$$

이며, 위에서 $$D$$를 $$D + C$$로, $$C$$를 $$C$$로 놓으면 $$\chi(\mathcal{O}(C + D)) - \chi(\mathcal{O}(D)) = \chi(\mathcal{O}_C(D))$$이고, 비슷하게 $$\chi(\mathcal{O}(C)) - \chi(\mathcal{O}_S) = \chi(\mathcal{O}_C)$$이므로

$$C \cdot D = \chi(\mathcal{O}_C(D)) - \chi(\mathcal{O}_C)$$

이다. 이제 $$\mathcal{O}_C(D)$$의 기하학적 의미를 살펴보자. $$\mathcal{O}_C(D) = \mathcal{O}_S(D)\vert_C$$는 curve $$C$$ 위의 line bundle으로, $$D$$를 정의하는 국소 방정식의 정보를 담고 있다. 구체적으로, $$C \cap D = \{p_1, \ldots, p_r\}$$라 하자. $$C$$와 $$D$$가 transversal intersection이라면, 각 교차점 $$p_i$$에서 $$D$$를 정의하는 local equation $$g_i$$는 $$C$$의 접선 방향으로 0이 아닌 미분을 가지므로, $$g_i$$는 $$C$$ 위에서 $$p_i$$에서만 0이 되는 국소 함수이다. 따라서 $$\mathcal{O}_C(D)$$는 $$C$$ 위에서 점들 $$p_1, \ldots, p_r$$에 각각 multiplicity 1을 갖는 divisor에 대응하는 line bundle이다. 즉 $$\deg(\mathcal{O}_C(D)) = r$$이다. Curve 위의 line bundle의 Euler characteristic은 Riemann–Roch에 의해

$$\chi(\mathcal{O}_C(D)) = \deg(\mathcal{O}_C(D)) + 1 - g(C) = \sum_i (C \cdot D)_{p_i} + \chi(\mathcal{O}_C)$$

이므로, $$C \cdot D = \chi(\mathcal{O}_C(D)) - \chi(\mathcal{O}_C) = \sum_i (C \cdot D)_{p_i}$$가 얻어진다. Transversal intersection의 경우 각 $$p_i$$에서 $$(C \cdot D)_{p_i} = 1$$이므로 교차수는 교차점의 개수와 일치한다.

</details>

## Serre Duality를 통한 표현

([§Serre Duality, ⁋명제 6](/ko/math/algebraic_geometry/serre_duality#prop6))에 의해 $$h^2(\mathcal{O}(D)) = h^0(\mathcal{O}(K_S - D))$$이다. 이 관계는 교차 형식의 이차항들이 실제로 cohomology의 정보를 담고 있다는 것을 보여준다. 구체적으로, Riemann–Roch 공식은 다음과 같이 쓸 수 있다:

$$h^0(\mathcal{O}(D)) - h^1(\mathcal{O}(D)) + h^0(\mathcal{O}(K_S - D)) = \chi(\mathcal{O}_S) + \frac{1}{2}(D^2 - D \cdot K_S)$$

이 표현은 $$D$$에 대한 정보를 $$K_S - D$$에 대한 정보와 연결해 준다. 특히 $$h^1(\mathcal{O}(D))$$는 직접 계산하기 어려운 항이지만, 만일 이 값이 0이거나 충분히 작다고 가정할 수 있다면—예를 들어 Kodaira vanishing theorem이 적용 가능한 경우—우리는 $$h^0(\mathcal{O}(D))$$와 $$h^0(\mathcal{O}(K_S - D))$$ 중 적어도 하나가 충분히 크다는 것을 보일 수 있다.

이 공식의 유용성을 이해하기 위해 두 극단적인 경우를 생각해 보자. 만일 $$D$$가 "충분히 양수", 즉 $$D \cdot H$$가 ample divisor $$H$$에 대해 충분히 크다면, $$K_S - D$$는 "음수" 방향이 되어 $$h^0(\mathcal{O}(K_S - D)) = 0$$이 되고 Riemann–Roch는 $$h^0$$에 대한 하한을 준다. 반대로 $$D$$가 "충분히 음수"이면 $$h^0(\mathcal{O}(D)) = 0$$이 되고 $$K_S - D$$의 정보를 얻는다. 이러한 "양수와 음수의 대칭"은 Serre duality가 만들어내는 현상이다.

## 예시: $$\mathbb{P}^1 \times \mathbb{P}^1$$

$$\mathbb{P}^2$$에 대한 Riemann–Roch 계산은 이미 ([§Riemann–Roch Theorem, ⁋예시 8](/ko/math/algebraic_geometry/riemann_roch_theorem#ex8))에서 다루었다. 여기서는 다른 근본적인 예시를 살펴본다.

<div class="example" markdown="1">

<ins id="ex4">**예시 4 ($$\mathbb{P}^1 \times \mathbb{P}^1$$)**</ins> $$\mathbb{P}^1 \times \mathbb{P}^1$$을 생각하자. 이 surface의 divisor class group은 $$\mathbb{Z} \oplus \mathbb{Z}$$이며, 각 factor의 hyperplane class $$H_1, H_2$$가 generator이다. 기하학적으로 $$H_1$$은 첫 번째 factor의 점들에 대응하는 "수평" fiber들이고, $$H_2$$는 두 번째 factor의 점들에 대응하는 "수직" fiber들이다. 두 수평 fiber는 서로 평행이므로 만나지 않아 $$H_1^2 = 0$$이고, 마찬가지로 $$H_2^2 = 0$$이다. 반면 수평 fiber와 수직 fiber는 항상 한 점에서 만나므로 $$H_1 \cdot H_2 = 1$$이다.

Canonical divisor는 $$K = -2H_1 - 2H_2$$이다. 구조층의 Euler characteristic은 Kunneth 공식에 의해 $$\chi(\mathcal{O}) = \chi(\mathcal{O}_{\mathbb{P}^1}) \cdot \chi(\mathcal{O}_{\mathbb{P}^1}) = 1 \cdot 1 = 1$$이다. Bidegree $$(a, b)$$의 divisor $$D = aH_1 + bH_2$$에 대해 Riemann–Roch 공식을 적용하면:

$$\chi(\mathcal{O}(D)) = 1 + \frac{1}{2}(D^2 - D \cdot K)$$

여기서 $$D^2 = (aH_1 + bH_2)^2 = 2ab$$이고 (양변을 전개하면 $$a^2 H_1^2 + 2ab H_1 \cdot H_2 + b^2 H_2^2 = 2ab$$), $$D \cdot K = (aH_1 + bH_2) \cdot (-2H_1 - 2H_2) = -2a - 2b$$이다. 따라서

$$\chi(\mathcal{O}(D)) = 1 + \frac{1}{2}(2ab + 2a + 2b) = (a+1)(b+1)$$

이것은 bidegree $$(a, b)$$ bihomogeneous polynomial의 parameter 개수와 일치한다. 예를 들어 $$D = H_1 + H_2$$는 $$(1,1)$$-bidegree 곡선으로, $$\chi = 4$$이며 이는 $$\mathbb{P}^1 \times \mathbb{P}^1$$ 위의 (1,1)-곡선이 conic과 동치라는 사실과 부합한다.

</div>

## Hodge Index Theorem

교차 형식이 surface의 geometry에 대해 어떤 정보를 담고 있는지 이해하는 것은 대수기하학에서 중요한 문제이다. $$\mathbb{P}^2$$의 경우 $$\operatorname{Num}(S)$$는 $$\mathbb{Z}$$이고 교차 형식은 $$H \mapsto H^2 = 1$$로 주어지므로 양의 정부호이다. 그러나 일반적인 surface에서는 교차 형식이 부정부호이거나 퇴화할 수 있다. Hodge index theorem은 surface 위의 교차 형식이 Minkowski space와 유사한 부호수를 갖는다는 것, 즉 positive direction은 단 하나뿐이라는 것을 말해준다.

이 결과를 서술하기 위해 먼저 몇 가지 정의를 도입한다. 교차수가 linear equivalence에 대해 불변이라는 [명제 2](#prop2)의 성질은, 교차수가 divisor의 numerical한 정보만을 담고 있음을 시사한다. 이를 공식화하면 다음과 같다.

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> 두 divisor $$D_1, D_2$$가 *numerically equivalent<sub>수치적으로 동치</sub>* $$D_1 \equiv D_2$$라는 것은, 모든 divisor $$E$$에 대해 $$D_1 \cdot E = D_2 \cdot E$$인 것이다. Numerical equivalence class의 집합을

$$\operatorname{Num}(S) = \operatorname{Div}(S) / \{\text{numerical equivalence}\}$$

라고 하며, 교차 형식에 의해 $$\operatorname{Num}(S) \otimes \mathbb{R}$$는 자연스럽게 real vector space 위의 이차 형식을 갖는다.

</div>

Numerical equivalence는 linear equivalence보다 약한 관계이다. 즉 $$D_1 \sim D_2$$이면 $$D_1 \equiv D_2$$이지만, 그 역은 일반적으로 성립하지 않는다. 예를 들어 abelian surface 위에서는 torsion line bundle이 존재할 수 있어, $$nD \sim 0$$이지만 $$D \not\sim 0$$인 divisor $$D$$가 존재한다. 이 경우 $$D \equiv 0$$이지만 $$D \not\sim 0$$이다.

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> Surface $$S$$의 *Néron–Severi group*은 ([§인자, ⁋정의 8](/ko/math/algebraic_geometry/divisors#def8))에서 정의한 Picard group $$\operatorname{Pic}(S)$$에서 algebraic equivalence를 취한 몫이다:

$$\operatorname{NS}(S) = \operatorname{Pic}(S) / \{\text{algebraic equivalence}\}$$

이것의 rank $$\rho(S) = \operatorname{rank} \operatorname{NS}(S)$$를 $$S$$의 *Picard number*라고 한다.

</div>

Algebraic equivalence는 numerical equivalence보다 강한 관계이므로 $$\operatorname{NS}(S) \otimes \mathbb{R}$$는 $$\operatorname{Num}(S)$$의 부분 공간이며, 특히 $$\rho(S) \le \operatorname{rank} \operatorname{Num}(S)$$이다. 사실 divisor (= codimension 1 cycle)에 대해서는 Matsusaka의 정리에 의해 algebraic equivalence와 numerical equivalence가 일치함(up to torsion)이 이미 증명되어 있으므로, $$\operatorname{NS}(S) \otimes \mathbb{Q} = \operatorname{Num}(S) \otimes \mathbb{Q}$$이다. 보다 일반적으로, 임의의 codimension의 cycle에 대해 homological equivalence와 numerical equivalence가 일치할 것이라는 Grothendieck의 standard conjecture D는 아직 미해결 문제이다. ([§선다발과 벡터다발, ⁋정의 9](/ko/math/algebraic_geometry/line_bundles#def9))에서 정의한 Picard group은 divisor class들을 분류하는 대수적 대상이며, Néron–Severi group은 여기서 "연속적인" 변화를 factor out하여 얻어지는 이산적인 불변량이다. Picard number $$\rho(S)$$는 surface의 "효과적인" divisor class의 차원을 나타낸다. 예를 들어 $$\mathbb{P}^2$$의 경우 $$\rho = 1$$이며, $$\mathbb{P}^1 \times \mathbb{P}^1$$의 경우 $$\rho = 2$$이다.

([§선다발과 벡터다발, ⁋명제 21](/ko/math/algebraic_geometry/line_bundles#prop21))에서 정의한 ample line bundle과 대응되는 ample divisor $$H$$는 교차 형식에 대해 특별한 역할을 한다.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7 (Hodge Index Theorem)**</ins> Smooth projective surface $$S$$와 ample divisor $$H$$에 대해, $$D \cdot H = 0$$이고 $$D \not\equiv 0$$이면 $$D^2 < 0$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$D \cdot H = 0$$이고 $$D \not\equiv 0$$이라고 하자.

**단계 1: $$D^2 \le 0$$임을 보인다.**

만일 $$D^2 > 0$$이라 하자. Riemann–Roch에 의해

$$\chi(\mathcal{O}(nD)) = \chi(\mathcal{O}_S) + \frac{n^2 D^2 - n D \cdot K_S}{2}$$

인데, $$D^2 > 0$$이므로 $$n \to \infty$$에서 $$\chi(\mathcal{O}(nD)) \to +\infty$$이다. Serre duality에 의해 $$h^2(\mathcal{O}(nD)) = h^0(\mathcal{O}(K_S - nD))$$이며, $$n \gg 0$$에서는 $$K_S - nD$$의 intersection number가 음의 방향으로 충분히 커져 $$h^0 = 0$$이 된다. 따라서 $$h^0(\mathcal{O}(nD)) \ge \chi(\mathcal{O}(nD)) \to +\infty$$이어서, 충분히 큰 $$n > 0$$에 대해 $$nD$$가 effective이다.

그러나 effective divisor $$E \ge 0$$와 ample divisor $$H$$의 교차는 항상 $$E \cdot H > 0$$이다. 한편 $$nD \cdot H = n(D \cdot H) = 0$$이므로 $$nD$$는 effective일 수 없다. 이는 모순이며, 따라서 $$D^2 \le 0$$이다.

**단계 2: $$D^2 = 0$$도 불가능함을 보인다.**

$$D^2 = 0$$이라고 가정하자. $$\operatorname{Num}(S) \otimes \mathbb{R}$$의 2차원 부분공간 $$V = \operatorname{span}(D, H)$$에서 교차 형식의 행렬을 생각하자. Basis $$\{D, H\}$$에 대한 교차 형식의 행렬은

$$M = \begin{pmatrix} D^2 & D \cdot H \\ H \cdot D & H^2 \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ 0 & H^2 \end{pmatrix}$$

이며, 그 행렬식은

$$\det M = (D^2)(H^2) - (D \cdot H)^2 = 0 \cdot H^2 - 0 = 0$$

이다. 단계 1에서 $$D^2 \le 0$$임을 보였고, 임의의 실수 $$a, b$$에 대해

$$(aD + bH)^2 = a^2 D^2 + 2ab(D \cdot H) + b^2 H^2 = b^2 H^2 \ge 0$$

이므로, $$V$$ 위에서 교차 형식은 반정부호(semi-definite)이다. 행렬식이 0이므로 이 형식은 degenerate이며, 그 kernel은 $$D$$ 자신을 포함한다. ($$D \cdot D = 0$$, $$D \cdot H = 0$$이므로 $$D \in \ker$$이다.)

이제 kernel을 정확히 계산하자. $$V$$ 위에서 이차형식 $$q(v) = v^2$$의 kernel은 $$\ker(q) = \{v \in V : v \cdot w = 0 \text{ for all } w \in V\}$$이다. $$V = \operatorname{span}(D, H)$$이므로 $$v = aD + bH$$가 kernel에 있으려면 $$v \cdot D = 0$$과 $$v \cdot H = 0$$을 모두 만족해야 한다. 첫째로 $$v \cdot H = bH^2 = 0$$에서 $$b = 0$$이고, 따라서 $$\ker(q) = \mathbb{R} \cdot D$$이다.

한편 반정부호이면서 degenerate인 이차형식의 kernel에 있는 벡터 $$D$$는 $$V$$의 모든 원소와 직교하므로, 특히 $$D \cdot H = 0$$이다. 그러나 $$D \not\equiv 0$$이라고 가정했으므로, $$\operatorname{Num}(S) \otimes \mathbb{R}$$ 전체에서 어떤 divisor $$E$$에 대해 $$D \cdot E \ne 0$$이다. 이 $$E$$의 $$H$$-방향 성분과 $$H$$-수직 성분으로의 분해 $$E = E_H + E_\perp$$ ($$E_\perp \cdot H = 0$$)를 생각하면, $$D \cdot E = D \cdot E_\perp$$이다. 그런데 $$E_\perp \in H^\perp$$이고 $$D \in \ker(q) \subset V = \operatorname{span}(D, H)$$이므로, $$D \cdot E_\perp \ne 0$$이려면 $$E_\perp$$가 $$V$$ 밖에 있어야 한다. 그러나 이 경우 $$E_\perp$$를 포함하도록 $$V$$를 확장한 부분공간 $$V' = \operatorname{span}(D, H, E_\perp)$$에서도 교차 형식은 $$H$$ 방향에서만 양의 값을 가져야 하며, 단계 1의 결과에 의해 $$H^\perp \cap V'$$에서는 이차형식이 음정부호이다. 따라서 $$D \cdot E_\perp \ne 0$$은 $$D^2 \ne 0$$ 또는 $$D \cdot H \ne 0$$을 함축해야 하는데, $$D^2 = 0$$이고 $$D \cdot H = 0$$이므로 모순이다.

결론적으로 $$D^2 = 0$$이면 $$D \equiv 0$$이어야 하는데, 이는 가정 $$D \not\equiv 0$$에 모순이다. 그러므로 $$D^2 < 0$$이다.

</details>

<div class="corollary" markdown="1">

<ins id="cor8">**따름정리 8**</ins> 교차 형식 on $$\operatorname{Num}(S) \otimes \mathbb{R}$$는 signature $$(1, \rho - 1)$$를 갖는다. 즉, positive direction은 하나뿐이며, 이것은 ample cone에 의해 span된다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Ample divisor $$H$$에 대해 $$H^2 > 0$$이므로 교차 형식은 적어도 하나의 positive direction을 갖는다. Hodge index theorem에 의해 $$H$$에 orthogonal인 모든 nonzero 방향은 음의 self-intersection을 갖는다. 따라서 $$\operatorname{Num}(S) \otimes \mathbb{R}$$을 $$\mathbb{R} \cdot H$$와 그 orthogonal complement로 분해하면, 전자에서 이차 형식은 양의 정부호이고 후자에서는 음의 정부호이다. Sylvester의 관성법칙에 의해 signature는 $$(1, \rho - 1)$$이다.

</details>

Hodge index theorem의 기하학적 의미는 다음과 같다. Surface 위의 교차 형식은 특수상대성이론의 Minkowski space와 유사하게, positive direction 하나와 negative direction $$\rho - 1$$개를 갖는 이차 형식이다. Ample cone이 이 유일한 positive direction을 span하므로, surface 위의 "양수" 방향은 본질적으로 하나뿐이며, 다른 모든 방향은 어떤 의미에서 "음수"이다. 이 결과는 surface의 birational geometry에서 minimal model의 유일성과 같은 깊은 결과들을 이끌어낸다.

## Application: Plurigenera

Curve의 경우, genus $$g$$는 curve의 birational equivalence class를 완전히 결정한다. Surface에서는 상황이 더 복잡한데, 그 이유는 birational equivalence가 cohomology의 차원을 모두 보존하지 않기 때문이다. 그러나 canonical bundle의 tensor power의 global section 차원은 birational invariant이며, 이 값들이 surface의 birational type에 대한 필수적인 정보를 제공한다.

<div class="definition" markdown="1">

<ins id="def9">**정의 9**</ins> Surface $$S$$의 *$$m$$-th plurigenus*는

$$P_m(S) = h^0(S, \omega_S^{\otimes m})$$

이다. 여기서 $$\omega_S = \mathcal{O}_S(K_S)$$는 ([§Canonical Bundle, ⁋명제 5](/ko/math/algebraic_geometry/canonical_bundle#prop5))에서 정의한 canonical bundle이다.

</div>

$$m = 1$$인 경우 $$P_1(S) = h^0(\omega_S) = p_g(S)$$는 geometric genus이다. Plurigenus들의 열 $$\{P_m(S)\}_{m \ge 1}$$은 surface의 birational equivalence class를 결정하는 중요한 불변량이다. ([§Canonical Bundle](/ko/math/algebraic_geometry/canonical_bundle))에서 살펴본 canonical bundle의 역할과 마찬가지로, $$\omega_S^{\otimes m}$$의 global section은 surface 위의 "multi-differential form", 즉 $$m$$개의 canonical divisor를 tensor한 형태의 differential form을 parameterize한다. 예를 들어 local coordinate $$z_1, z_2$$에서 $$\omega_S^{\otimes m}$$의 section은 $$f(z_1, z_2)(dz_1 \wedge dz_2)^{\otimes m}$$의 꼴로 쓰인다.

Plurigenus의 증가율은 surface의 Kodaira dimension과 밀접하게 관련되어 있다. Kodaira dimension $$\kappa(S)$$는 $$P_m(S)$$의 $$m$$에 대한 증가 차수로 정의된다. 구체적으로, 모든 $$m \ge 1$$에 대해 $$P_m(S) = 0$$이면 $$\kappa = -\infty$$이다. 그렇지 않은 경우, $$\kappa(S)$$는 $$P_m(S) / m^\kappa$$가 유계(bounded)가 되는 최소의 정수 $$\kappa$$로 정의된다. 즉 $$\kappa(S) = \min\{k \in \mathbb{Z}_{\ge 0} : P_m(S) = O(m^k)\}$$이다. 이 정의에 의하면 $$\kappa = 0$$은 $$P_m(S)$$가 항상 $$0$$ 또는 $$1$$이면서 모든 $$m$$에 대해 $$0$$인 것은 아닌 경우이며, $$\kappa = 1$$은 $$P_m(S) \sim cm$$으로 선형 성장하는 경우, $$\kappa = 2$$는 $$P_m(S) \sim cm^2$$으로 이차 성장하는 경우이다. Surface의 경우 $$\kappa \in \{-\infty, 0, 1, 2\}$$이다.

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10**</ins> $$m \ge 2$$에 대해, 만일 $$h^0(\mathcal{O}_S((1-m)K_S)) = 0$$이면

$$P_m(S) \ge \chi(\mathcal{O}_S) + \frac{m(m-1)}{2} K_S^2$$

이다. 가설 $$h^0(\mathcal{O}_S((1-m)K_S)) = 0$$은 Serre duality에 의해 $$h^2(\omega_S^{\otimes m}) = 0$$과 동치이며, 이는 $$m \gg 0$$에서 항상 만족된다—$$(1-m)K_S$$가 어떤 effective divisor보다도 “더 음수”이기 때문이다.

특히 $$K_S$$가 ample이고 $$m \ge 2$$이면

$$P_m(S) = \chi(\mathcal{O}_S) + \frac{m(m-1)}{2} K_S^2$$

이 성립한다. 따라서 $$K_S$$가 ample인 surface는 Kodaira dimension $$2$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Riemann–Roch 공식 ([§Riemann–Roch Theorem, ⁋명제 7](/ko/math/algebraic_geometry/riemann_roch_theorem#prop7))에 $$D = mK_S$$를 대입한다:

$$\chi(\omega_S^{\otimes m}) = \chi(\mathcal{O}_S) + \frac{1}{2}\left((mK_S)^2 - (mK_S) \cdot K_S\right) = \chi(\mathcal{O}_S) + \frac{1}{2}\left(m^2 K_S^2 - m K_S^2\right)$$

$$= \chi(\mathcal{O}_S) + \frac{m(m-1)}{2} K_S^2$$

한편 $$\chi(\omega_S^{\otimes m}) = h^0(\omega_S^{\otimes m}) - h^1(\omega_S^{\otimes m}) + h^2(\omega_S^{\otimes m})$$이다. Serre duality에 의해 $$h^2(\omega_S^{\otimes m}) = h^0(\mathcal{O}_S((1-m)K_S))$$이다. 이 값은 명제의 가설에 의해 $$0$$이다. 따라서

$$P_m(S) = h^0(\omega_S^{\otimes m}) = \chi(\omega_S^{\otimes m}) + h^1(\omega_S^{\otimes m}) \ge \chi(\omega_S^{\otimes m}) = \chi(\mathcal{O}_S) + \frac{m(m-1)}{2} K_S^2$$

이다. 이로써 첫 번째 부등식이 얻어진다.

이제 $$K_S$$가 ample인 경우를 생각하자. Kodaira vanishing theorem에 의해, ample line bundle $$\mathcal{L}$$에 대해 $$H^i(X, \mathcal{L} \otimes \omega_X) = 0$$ for $$i > 0$$이다. $$\omega_S^{\otimes m} = \mathcal{O}_S(mK_S) = \mathcal{O}_S((m-1)K_S) \otimes \omega_S$$이고, $$K_S$$가 ample이면 $$m \ge 2$$에서 $$(m-1)K_S$$도 ample이므로

$$h^1(\omega_S^{\otimes m}) = 0$$

이다. 따라서 $$P_m(S) = \chi(\omega_S^{\otimes m})$$이 되어 등식이 성립한다. 또한 $$K_S^2 > 0$$이므로 $$P_m(S)$$는 $$m^2$$의 차수로 증가하며, 이로부터 $$\kappa(S) = 2$$임을 확인할 수 있다.

</details>

## 예시: K3 Surface

지금까지의 도구들을 구체적인 surface에 적용해 보자. K3 surface는 canonical bundle이 trivial인 surface 중 가장 중요한 부류이다. "K3"라는 이름은 André Weil이 1958년에 명명한 것으로, Kummer, Kähler, Kodaira 세 수학자의 이름과 카라코람의 아름다운 산 K2를 동시에 기리고 있다 ([BHPV], [Huyb]). 이들은 각각 K3 surface의 서로 다른 측면을 연구하였다.

<div class="definition" markdown="1">

<ins id="def11">**정의 11**</ins> Smooth projective surface $$S$$가 *K3 surface*라는 것은 $$K_S \sim 0$$ (trivial canonical bundle)이고 $$h^1(S, \mathcal{O}_S) = 0$$인 것이다.

</div>

K3 surface의 가장 친숙한 예시는 $$\mathbb{P}^3$$ 안의 quartic surface, 즉 degree $$4$$ homogeneous 다항식의 zero set이다. ([§Canonical Bundle](/ko/math/algebraic_geometry/canonical_bundle))에서 다룬 adjunction formula에 의해 $$\mathbb{P}^3$$ 안의 degree $$d$$ smooth hypersurface $$S$$의 canonical bundle은

$$K_S = (K_{\mathbb{P}^3} + S)\vert_S = (\mathcal{O}_{\mathbb{P}^3}(-4) + \mathcal{O}_{\mathbb{P}^3}(d))\vert_S = \mathcal{O}_S(d - 4)$$

이다. 따라서 $$d = 4$$이면 $$K_S = \mathcal{O}_S(0) = 0$$이 되어 trivial canonical bundle을 갖는다. 또한 Lefschetz hyperplane theorem에 의해 $$h^1(S, \mathcal{O}_S) = 0$$이 성립한다.

$$K_S \sim 0$$이므로 K3 surface 위에서 Riemann–Roch 공식은 극도로 단순해진다. Canonical bundle이 trivial이므로 $$D \cdot K_S = 0$$이고 $$K_S^2 = 0$$이며, 따라서

$$\chi(\mathcal{O}_S(D)) = \chi(\mathcal{O}_S) + \frac{D^2}{2}$$

이다. $$h^1(S, \mathcal{O}_S) = 0$$과 Serre duality $$h^2(\mathcal{O}_S) = h^0(K_S) = h^0(\mathcal{O}_S) = 1$$에 의해 $$\chi(\mathcal{O}_S) = 1 - 0 + 1 = 2$$이다. 따라서:

$$\chi(\mathcal{O}_S(D)) = 2 + \frac{D^2}{2}$$

이 공식은 K3 surface의 기하학을 이해하는 강력한 도구이다. 예를 들어 $$D^2 \ge -2$$이면 $$\chi(\mathcal{O}_S(D)) \ge 1$$이 되어, $$h^0(\mathcal{O}(D)) \ge 1$$ 또는 $$h^0(\mathcal{O}(-D)) \ge 1$$이 성립한다. 전자의 경우 $$D$$가 linearly equivalent한 effective divisor가 존재한다는 것을 의미한다. 특히 $$D^2 = -2$$이면 $$\chi(\mathcal{O}(D)) = 1$$이고, 만일 $$h^0(\mathcal{O}(D)) = 0$$이라면 Serre duality에 의해 $$h^2(\mathcal{O}(D)) = h^0(\mathcal{O}(-D)) \ge 1$$이어야 하는데, 이는 $$-D$$가 effective라는 뜻이다. 따라서 $$D$$ 또는 $$-D$$ 중 적어도 하나는 effective이다.

K3 surface 위에서 $$D^2 = -2$$를 갖는 effective divisor $$D$$에 대해, adjunction formula $$2p_a - 2 = D^2 + D \cdot K_S = -2$$에서 arithmetic genus $$p_a(D) = 0$$을 얻는다. 만일 $$D$$가 기약 곡선(irreducible curve)이면, $$p_a(D) = 0$$은 $$D \cong \mathbb{P}^1$$임을 의미한다. (일반적으로 effective divisor는 여러 기약 성분으로 분해될 수 있으므로, $$D$$가 기약이라는 조건이 필요하다.) 이러한 기약 곡선을 $$(-2)$$-curve라 부르며, K3 surface의 automorphism group을 이해하는 데 핵심적인 역할을 한다.

한편 K3 surface의 모든 plurigenus는 같다. $$K_S \sim 0$$이므로 $$\omega_S^{\otimes m} \cong \mathcal{O}_S$$이고, 따라서 $$P_m(S) = h^0(\mathcal{O}_S) = 1$$ for all $$m \ge 1$$이다. 이는 K3 surface가 Kodaira dimension $$0$$임을 의미한다.

[명제 10](#prop10)의 부등식은 $$K_S$$가 effective이고 $$h^2(\omega_S^{\otimes m}) = 0$$이라는 조건 하에서 성립한다. K3 surface에서는 $$K_S \sim 0$$으로 effective이므로 첫 번째 조건은 만족하지만, $$\omega_S^{\otimes(1-m)} \cong \mathcal{O}_S$$이므로 Serre duality에 의해 $$h^2(\omega_S^{\otimes m}) = h^0(\mathcal{O}_S) = 1 \ne 0$$이어서 두 번째 조건이 위배된다. 실제로 $$K_S^2 = 0$$, $$\chi(\mathcal{O}_S) = 2$$이므로 [명제 10](#prop10)의 우변은 $$2$$이지만 $$P_m(S) = 1 < 2$$이다. 이는 $$h^2$$ 항이 0이 아니기 때문이며, full Euler characteristic은 $$\chi(\omega_S^{\otimes m}) = h^0 - h^1 + h^2 = 1 - 0 + 1 = 2$$로 부등식의 우변과 정확히 일치한다. 이 예시는 $$h^2 = 0$$ 가정이 실제로 필요하다는 것을 잘 보여준다.

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[BHPV]** W. Barth, K. Hulek, C. Peters, A. Van de Ven, *Compact Complex Surfaces*, Springer, 2004.  
**[Huyb]** D. Huybrechts, *Lectures on K3 Surfaces*, Cambridge University Press, 2016.
