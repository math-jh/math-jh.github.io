---
title: "곡면에서의 리만-로흐 정리"
excerpt: "Intersection theory on surfaces and its applications"

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/riemann_roch_surfaces
sidebar: 
    nav: "algebraic_geometry-ko"

header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Riemann_Roch_Surfaces.png
    overlay_filter: 0.5

date: 2026-05-04
last_modified_at: 2026-05-06
weight: 17
published: false
---

우리는 앞선 글에서 Riemann-Roch 정리를 곡선에서 살펴보았다. 본질적으로 Riemann-Roch 정리는 Euler characteristic을 다른 정량적인 수치들로 계산하는 것으로, 더 일반적으로 우리는 임의의 경우로 이를 일반화할 수도 있으나 이번 글에서는 surface로의 일반화만  다루기로 한다.

다시 curve $$C$$에서의 Riemann-Roch formula ([§곡선에서의 리만-로흐 정리, ⁋명제 3](/ko/math/algebraic_geometry/riemann_roch_theorem#prop3))

$$\ell(D) - \ell(K_C - D) = \deg D + 1 - g$$

를 살펴보면, 이 식의 좌변은 본질적으로 $$\mathcal{O}_C(D)$$의 Euler characteristic이며 [§곡선에서의 리만-로흐 정리, ⁋보조정리 2](/ko/math/algebraic_geometry/riemann_roch_theorem#lem2)가 이 부분이 두 개의 항만으로 나온다는 것을 보장한다. 그러나 이제 곡면에서 이를 일반화하기 위해서는 base space의 차원이 하나 커지므로 추가적인 항이 등장할 것이며, 이에 대응하여 우변의 식 또한 추가적인 항이 등장하게 될 것이다.

직관적으로, 위 식의 우변에서 등장하는 $$\deg D$$는 일종의 선형인 항이라 생각할 수 있으나, 이렇게 곡면에서의 일반화를 하는 과정에서 우리는 추가적인 <em-ko>이차항들</em-ko> $$D\cdot D$$, $$D\cdot K_S$$ 등을 고려하게 된다. 이들은 surface 위의 두 divisor가 얼마나 교차하는지를 담고 있는 양으로, curve case에서의 divisor들, 즉 점들은 곡선 안에서 일반적으로 만나지 않지만, 곡면에서의 divisor들, 즉 곡선들은 이 곡면 안에서 일반적으로 유한 개의 점에서 만나기 때문에 생겨난다. 

이 글에서는 intersection number의 정의와 그 기본 성질을 다루고, Riemann–Roch 공식을 엄밀하게 유도한 뒤, 이를 활용하여 Hodge index theorem과 plurigenera에 대한 부등식을 증명한다. 또한 교차 형식이 surface의 birational geometry에서 갖는 의미를 살펴본다.

## Intersection Number

우리의 출발점은 다소 추상적으로 보일 수 있는 Euler characteristic을 이용한 정의이다. 이 정의의 장점은 linear equivalence에 대해 불변이라는 사실이 즉시 따라온다는 것으로, 정의 직후 이것이 실제로 교차점의 수를 세고 있음을 확인할 것이다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Smooth surface $$S$$ 위의 두 divisor $$C, D$$의 *intersection number<sub>교차수</sub>* $$C \cdot D$$를 다음과 같이 정의한다.

$$C \cdot D = \rchi(\mathcal{O}_S(C + D)) - \rchi(\mathcal{O}_S(C)) - \rchi(\mathcal{O}_S(D)) + \rchi(\mathcal{O}_S)$$

</div>

이들의 기하학적 의미를 살펴보기 위해, $$C$$와 $$D$$가 각각 global section $$s \in H^0(\mathcal{O}(C))$$, $$t \in H^0(\mathcal{O}(D))$$로 정의되는 effective divisor라 하자. 그럼 이들의 common zero locus는 $$C \cap D$$이며, 다음 exact sequence가 성립한다.

$$0 \to \mathcal{O} \xrightarrow{(t,-s)} \mathcal{O}(C) \oplus \mathcal{O}(D) \xrightarrow{(s,t)} \mathcal{O}(C+D) \to \mathcal{O}_{C \cap D} \to 0$$

여기서 첫 번째 화살표는 $$h \mapsto (ht, -hs)$$, 두 번째 화살표는 $$(f, g) \mapsto fs + gt$$이고, 마지막 화살표는 $$\mathcal{O}(C+D)$$에서 $$C \cap D$$ 위로의 자연스러운 restriction map이다. 그럼 Euler characteristic의 additivity에 의하여

$$C \cdot D = \rchi(\mathcal{O}_{C \cap D})$$

이며, 이 때 $$C\cap D$$는 곡선 두 개의 교집합, 즉 점들이고 따라서 우변의 Euler characteristic은 정확히 $$C\cap D$$의 점들의 갯수를 세게 된다. 다소 미묘한 부분은 이것이 잘 정의되기 위해서는 $$C$$와 $$D$$가 일반적인 위치에 있어야 한다는 것인데, 이를 위해 우리는 두 곡선 $$C,D$$가 점 $$p$$에서 *transversally intersect*한다는 것을 다음의 조건

$$T_pC\oplus T_pD\cong T_pS$$

으로 정의한다. 가령 $$\mathbb{A}^2$$에서, $$\x=0$$은 자기 자신과 transversally intersect하지 않으며 $$\y=\x^3$$은 $$\y=0$$과 transversally intersect하지 않는다. 반면 $$\y=\x$$와 $$\y=-\x$$는 transversal하게 만난다. 뿐만 아니라, 이 예시는 intersection multiplicity의 직관 또한 제공하는데, $$\y=\x$$와 $$\y=-\x$$의 (원점에서의) intersection multiplicity는 $$1$$이지만 $$\y=\x^3$$과 $$\y=0$$의 intersection multiplicity는 $$3$$이다. 그럼 $$C$$와 $$D$$가 transversal하게 만나지 않을 수도 있는 일반적인 경우에서는 

$$\rchi(\mathcal{O}_{C \cap D}) = \sum_{p \in C \cap D} (C \cdot D)_p$$

가 성립하며, 여기서 $$(C \cdot D)_p$$는 $$p$$에서의 local intersection multiplicity이다. 이 때 이 식에서 $$C\cap D$$가 점들의 유한집합 대신 curve가 되는 상황을 막기 위해서는 (가령 $$C=D$$인 상황을 막기 위해서는) 우리는 $$C,D$$가 공통의 component를 갖지 않는다 가정한다. 

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> 다음은 intersection number의 성질들이다. 

1. *Symmetry.* $$C \cdot D = D \cdot C$$가 성립한다.
2. *Bilinearity.* $$(aC_1 + bC_2) \cdot D = a(C_1 \cdot D) + b(C_2 \cdot D)$$가 성립한다. 
3. *Linear invariance.* Linearly equivalent한 두 divisor $$C \sim C'$$에 대해 $$C \cdot D = C' \cdot D$$가 항상 성립한다.

</div>

Symmetry는 위에서 보인 직관에 의해 자명하며, linear invariance 또한 거의 자명하다. 의외로 가장 덜 자명한 것은 bilinearity인데, 이는 보통 Snapper's theorem으로 설명할 수 있다. Snapper's theorem에 의하면, projective variety 위의 임의의 coherent sheaf $$\mathcal{F}$$, line bundles $$L_1, \ldots, L_k$$에 대해, Euler characteristic 

$$\rchi(\mathcal{F} \otimes L_1^{\otimes n_1} \otimes \cdots \otimes L_k^{\otimes n_k})$$

는 $$n_1, \ldots, n_k$$에 대한 다항식으로 주어진다. 그럼 특히 intersection number의 정의에서 $$\rchi(\mathcal{O}_S(aC_1 + bC_2 + D))$$는 $$a, b$$에 대한 다항식이 되며, 이 다항식의 이차 계수를 비교한 것이 bilinearity가 된다.

## 곡면에서의 Riemann–Roch 정리

이제 우리는 Riemann-Roch 정리를 곡면으로 확장할 때 필요한 언어를 전부 가지고 있다. 이제 우리에게 필요한 것은 다음의 보조정리이다. 

<div class="proposition" markdown="1">

<ins id="lem3">**보조정리 3 (Genus formula)**</ins> Smooth projective surface $$S$$ 위의 smooth irreducible curve $$D$$에 대해

$$2g(D) - 2 = D^2 + D \cdot K_S$$

이 성립한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Adjunction formula ([§표준선다발, ⁋명제 9](/ko/math/algebraic_geometry/canonical_bundle#prop9))에 의해

$$\omega_D \cong (\omega_S \otimes \mathcal{O}_S(D))\vert_D$$

이다. 양변의 degree를 취하면

$$\deg(\omega_D) = \deg(\omega_S\vert_D) + \deg(\mathcal{O}_D(D))$$

이다. 우리는 앞서 [§곡선에서의 리만-로흐 정리, ⁋명제 3](/ko/math/algebraic_geometry/riemann_roch_theorem#prop3)의 결과로 $$\deg(\omega_D)=2g-2$$라는 것을 유도하였으며 우변의 두 항만 intersection numbery로 해석하면 된다. 우선 $$\omega_S\vert_D$$는 $$D$$ 위로 restriction된 canonical bundle로, 이는 $$D$$와 canonical divisor $$K_S$$의 교차수를 측정한다. 구체적으로 $$K_S$$가 $$\omega_S$$에 대응하는 divisor이므로, $$\omega_S\vert_D$$의 degree는 $$D$$ 위에서 $$K_S$$가 차지하는 점들의 수, 즉 $$D \cdot K_S$$가 된다. 비슷하게 $$\mathcal{O}_D(D)$$는 $$D$$의 normal bundle $$\mathcal{N}_{D/S}$$에 해당하며, 이는 $$D$$가 $$S$$ 안에서 자기 자신과 만나는 정도를 측정한다. 이 bundle의 degree는 $$D$$의 self-intersection number $$D^2$$와 일치한다. 이들을 종합하면

$$2g(D) - 2 = D \cdot K_S + D^2$$

를 얻는다. 

</details>

그럼 Riemann-Roch 정리는 곡면에서 다음과 같이 주어진다. 

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4 (Riemann–Roch for surfaces)**</ins> Smooth projective surface $$S$$ 위의 divisor $$D$$에 대해

$$\rchi(\mathcal{O}_S(D)) = \frac{1}{2} D \cdot (D - K_S) + \rchi(\mathcal{O}_S)$$

이 성립한다. 

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

우선 $$D$$가 smooth irreducible effective divisor인 경우를 보자. 다음의 short exact sequence

$$0 \to \mathcal{O}_S \to \mathcal{O}_S(D) \to \mathcal{O}_D(D) \to 0$$

로부터 Euler characteristic의 additivity에 의해

$$\rchi(\mathcal{O}_S(D)) = \rchi(\mathcal{O}_S) + \rchi(\mathcal{O}_D(D))$$

이다. 이 때, $$\mathcal{O}_D(D)$$는 $$D$$ 위에 정의된 line bundle이므로, 곡선에서의 Riemann–Roch ([§곡선에서의 리만-로흐 정리, ⁋명제 3](/ko/math/algebraic_geometry/riemann_roch_theorem#prop3))에 의해

$$\rchi(\mathcal{O}_D(D)) = D^2 + 1 - g(D)$$

이다. 앞선 [보조정리 3](#lem3)에서 

$$g(D) = \frac{1}{2}(D^2 + D \cdot K_S) + 1$$

이므로, 이를 대입하면

$$\rchi(\mathcal{O}_D(D)) = D^2 + 1 - \frac{1}{2}(D^2 + D \cdot K_S) - 1 = \frac{1}{2}D \cdot (D - K_S)$$

이다. 따라서

$$\rchi(\mathcal{O}_S(D)) = \rchi(\mathcal{O}_S) + \frac{1}{2}D \cdot (D - K_S)$$

를 얻는다.

이제 우리는 이를 일반적인 divisor $$D$$에 대해 이를 일반화해야 한다. 우리는 우선 $$S$$ 위의 ample divisor $$H$$를 고정하자. 그럼 Serre vanishing theorem ([§사영공간의 코호몰로지, ⁋명제 4](/ko/math/algebraic_geometry/cohomology_of_projective_spaces#prop4))에 의해, 충분히 큰 $$n$$에 대해 

$$H^1(S, \mathcal{O}_S(D + nH)) = H^2(S, \mathcal{O}_S(D + nH)) = 0$$

이다. 따라서

$$\rchi(\mathcal{O}_S(D + nH)) = h^0(\mathcal{O}_S(D + nH))$$

가 성립한다. 한편 $$D+nH$$는 effective divisor이므로, 앞선 논증에 의해 $$D+nH$$에 대해서는 원하는 등식이 성립한다. 따라서 $$n$$에 대한 두 함수 $$f(n) = \rchi(\mathcal{O}(D+nH))$$와 $$g(n) = \frac{1}{2}(D+nH)\cdot(D+nH-K_S) + \rchi(\mathcal{O}_S)$$를 생각하면 이들은 충분히 큰 $$n$$에 대해서는 항상 일치한다. 그런데 앞서 언급한 Snapper's theorem에 의해 $$\rchi(\mathcal{O}_S(D+nH))$$는 $$n$$에 대한 다항식이고, 무한히 많은 점들에 대해 그 값이 일치하는 다항식은 서로 같으므로 $$f$$와 $$g$$는 사실 같은 다항식이다. 즉, 모든 $$n$$에 대해 $$f(n) = g(n)$$이며 특히 $$n = 0$$을 대입하면

$$\rchi(\mathcal{O}(D)) = \frac{1}{2}D\cdot(D-K_S) + \rchi(\mathcal{O}_S)$$

를 얻는다.

</details>

Curve의 경우와 마찬가지로, 만약 $$D$$가 충분히 "양의" 방향이라면 $$h^1$$과 $$h^2$$가 사라져 $$\rchi(\mathcal{O}_S(D)) = h^0(S, \mathcal{O}_S(D))$$가 된다. 이는 ([§선형계, ⁋정의 10](/ko/math/algebraic_geometry/linear_systems#def10))에서 정의한 ampleness 개념과 밀접하게 관련되어 있다.

<div class="example" markdown="1">

<ins id="ex5">**예시 5 ($$\mathbb{P}^2$$)**</ins> 우리는 $$\mathbb{P}^2$$에서 hyperplane class $$H$$를 고정하면

$$K_{\mathbb{P}^2} = -3H, \qquad \rchi(\mathcal{O}_{\mathbb{P}^2}) = 1$$

임을 안다.  ([§표준선다발, ⁋명제 7](/ko/math/algebraic_geometry/canonical_bundle#prop7), [§사영공간의 코호몰로지, ⁋따름정리 3](/ko/math/algebraic_geometry/cohomology_of_projective_spaces#cor3)) $$\mathbb{P}^2$$에서 임의의 두 직선은 일반적으로 한 점에서 만나므로, $$H$$의 self-intersection number는 1이며 따라서 임의의 divisor $$D = dH$$에 대해

$$\rchi(\mathcal{O}_{\mathbb{P}^2}(d)) = \frac{1}{2}dH \cdot (dH + 3H) + 1 = \frac{1}{2}d(d+3) + 1$$

이 성립한다. 이것이 실제로 성립한다는 것은 [§사영공간의 코호몰로지, ⁋정리 3](/ko/math/algebraic_geometry/cohomology_of_projective_spaces#cor3)의 결과이다. 특별히 $$d \ge 0$$에 대해서는 $$h^0 = \binom{d+2}{2}$$이고 $$h^1 = h^2 = 0$$임을 알고 있으므로, 이것이 위에서 언급한 $$h^1, h^2$$의 vanishing에 대한 직접적인 예시가 된다. 

</div>

<div class="example" markdown="1">

<ins id="ex6">**예시 6 (Blow-up of $$\mathbb{P}^2$$)**</ins> 이제 우리는 $$\mathbb{P}^2$$의 한 점 $$p$$에서의 blow-up $$\pi: \widetilde{\mathbb{P}}^2 \to \mathbb{P}^2$$을 생각한다. [§표준선다발, ⁋명제 12](/ko/math/algebraic_geometry/canonical_bundle#prop12)에 의해, canonical bundle은 다음의 식

$$K_{\widetilde{\mathbb{P}}^2} = \pi^\ast K_{\mathbb{P}^2} + E = -3H + E$$

으로 주어진다. $$\mathbb{P}^2$$에서는 hyperplane class $$H$$가 점 $$p$$를 피하도록 잡을 수 있으므로 $$H \cdot E = 0$$이다. 한편 $$E \cong \mathbb{P}^1$$이며, $$E$$의 normal bundle $$\mathcal{N}_{E/\widetilde{\mathbb{P}}^2}$$는 $$\mathcal{O}_{\mathbb{P}^1}(-1)$$와 isomorphic하며 이로부터 self-intersection number $$E^2 = \deg(\mathcal{N}_{E/\widetilde{\mathbb{P}}^2}) = -1$$이며, 기하학적으로 이는 $$E$$가 한 점으로 collapse되면서 주변에서 "접혀 들어가" negativity를 갖게 됨을 의미한다. 따라서 일반적인 divisor $$D = dH - kE$$에 대해서는

$$\rchi(\mathcal{O}_{\widetilde{\mathbb{P}}^2}(dH - kE)) = \frac{1}{2}(dH - kE) \cdot (dH - kE + 3H - E) + 1 = \frac{1}{2}d(d+3) - \frac{1}{2}k(k+1) + 1$$

임을 계산할 수 있다.

</div>

한편 곡선에서의 Riemann-Roch 정리는 위의 [명제 4](#prop4)에서 [§세르 쌍대성, ⁋명제 4](/ko/math/algebraic_geometry/serre_duality#prop4)를 적용하여 $$h^1$$ 부분을 $$h^0$$으로 바꾼 것으로, 곡면에서의 경우에도 이를 활용하여 $$h^2(\mathcal{O}(D)) = h^0(\mathcal{O}(K_S - D))$$로 적을 수 있고, 그럼 Riemann–Roch 공식은 다음의 식

$$h^0(\mathcal{O}(D)) - h^1(\mathcal{O}(D)) + h^0(\mathcal{O}(K_S - D)) = \rchi(\mathcal{O}_S) + \frac{1}{2}(D^2 - D \cdot K_S)$$

으로 변하게 된다. 일반적으로 $$h^1(\mathcal{O}(D))$$는 직접 계산하기 어려운 항이지만, 만일 이 값이 0이거나 충분히 작다고 가정할 수 있다면—예를 들어 Kodaira vanishing theorem이 적용 가능한 경우—우리는 $$h^0(\mathcal{O}(D))$$와 $$h^0(\mathcal{O}(K_S - D))$$ 중 적어도 하나가 충분히 크다는 것을 보일 수 있다.

이 공식의 유용성을 이해하기 위해 두 극단적인 경우를 생각해 보자. 만일 $$D$$가 "충분히 양수", 즉 $$D \cdot H$$가 ample divisor $$H$$에 대해 충분히 크다면, $$K_S - D$$는 "음수" 방향이 되어 $$h^0(\mathcal{O}(K_S - D)) = 0$$이 되고 Riemann–Roch는 $$h^0$$에 대한 하한을 준다. 반대로 $$D$$가 "충분히 음수"이면 $$h^0(\mathcal{O}(D)) = 0$$이 되고 $$K_S - D$$의 정보를 얻는다. 이러한 "양수와 음수의 대칭"은 Serre duality가 만들어내는 현상이다.

$$\mathbb{P}^2$$에 대한 Riemann–Roch 계산은 이미 [예시 5](#ex5)에서 다루었다. 여기서는 다른 근본적인 예시를 살펴본다.

<div class="example" markdown="1">

<ins id="ex7">**예시 7 ($$\mathbb{P}^1 \times \mathbb{P}^1$$)**</ins> $$\mathbb{P}^1 \times \mathbb{P}^1$$을 생각하자. 이 surface의 divisor class group은 $$\mathbb{Z} \oplus \mathbb{Z}$$이며, 각 factor의 hyperplane class $$H_1, H_2$$가 generator이다. 기하학적으로 $$H_1$$은 첫 번째 factor의 점들에 대응하는 "수평" fiber들이고, $$H_2$$는 두 번째 factor의 점들에 대응하는 "수직" fiber들이다. 두 수평 fiber는 서로 평행이므로 만나지 않아 $$H_1^2 = 0$$이고, 마찬가지로 $$H_2^2 = 0$$이다. 반면 수평 fiber와 수직 fiber는 항상 한 점에서 만나므로 $$H_1 \cdot H_2 = 1$$이다.

Canonical divisor는 $$K = -2H_1 - 2H_2$$이다. 구조층의 Euler characteristic은 Kunneth 공식에 의해 $$\rchi(\mathcal{O}) = \rchi(\mathcal{O}_{\mathbb{P}^1}) \cdot \rchi(\mathcal{O}_{\mathbb{P}^1}) = 1 \cdot 1 = 1$$이다. Bidegree $$(a, b)$$의 divisor $$D = aH_1 + bH_2$$에 대해 Riemann–Roch 공식을 적용하면:

$$\rchi(\mathcal{O}(D)) = 1 + \frac{1}{2}(D^2 - D \cdot K)$$

여기서 $$D^2 = (aH_1 + bH_2)^2 = 2ab$$이고 (양변을 전개하면 $$a^2 H_1^2 + 2ab H_1 \cdot H_2 + b^2 H_2^2 = 2ab$$), $$D \cdot K = (aH_1 + bH_2) \cdot (-2H_1 - 2H_2) = -2a - 2b$$이다. 따라서

$$\rchi(\mathcal{O}(D)) = 1 + \frac{1}{2}(2ab + 2a + 2b) = (a+1)(b+1)$$

이것은 bidegree $$(a, b)$$ bihomogeneous polynomial의 parameter 개수와 일치한다. 예를 들어 $$D = H_1 + H_2$$는 $$(1,1)$$-bidegree 곡선으로, $$\rchi = 4$$이며 이는 $$\mathbb{P}^1 \times \mathbb{P}^1$$ 위의 (1,1)-곡선이 conic과 동치라는 사실과 부합한다.

</div>

## Hodge Index Theorem

교차 형식이 surface의 geometry에 대해 어떤 정보를 담고 있는지 이해하는 것은 대수기하학에서 중요한 문제이다. $$\mathbb{P}^2$$의 경우 $$\operatorname{Num}(S)$$는 $$\mathbb{Z}$$이고 교차 형식은 $$H \mapsto H^2 = 1$$로 주어지므로 양의 정부호이다. 그러나 일반적인 surface에서는 교차 형식이 부정부호이거나 퇴화할 수 있다. Hodge index theorem은 surface 위의 교차 형식이 Minkowski space와 유사한 부호수를 갖는다는 것, 즉 positive direction은 단 하나뿐이라는 것을 말해준다.

이 결과를 서술하기 위해 먼저 몇 가지 정의를 도입한다. 교차수가 linear equivalence에 대해 불변이라는 [명제 2](#prop2)의 성질은, 교차수가 divisor의 수치적인 정보만을 담고 있음을 시사한다. 이를 공식화하면 다음과 같다.

<div class="definition" markdown="1">

<ins id="def8">**정의 8**</ins> 두 divisor $$D_1, D_2$$가 *numerically equivalent<sub>수치적으로 동치</sub>* $$D_1 \equiv D_2$$라는 것은, 모든 divisor $$E$$에 대해 $$D_1 \cdot E = D_2 \cdot E$$인 것이다. Numerical equivalence class의 집합을

$$\operatorname{Num}(S) = \Div(S) / \{\text{numerical equivalence}\}$$

라고 하며, 교차 형식에 의해 $$\operatorname{Num}(S) \otimes \mathbb{R}$$는 자연스럽게 real vector space 위의 이차 형식을 갖는다.

</div>

Numerical equivalence는 linear equivalence보다 약한 관계이다. 즉 $$D_1 \sim D_2$$이면 $$D_1 \equiv D_2$$이지만, 그 역은 일반적으로 성립하지 않는다. 예를 들어 abelian surface 위에서는 torsion line bundle이 존재할 수 있어, $$nD \sim 0$$이지만 $$D \not\sim 0$$인 divisor $$D$$가 존재한다. 이 경우 $$D \equiv 0$$이지만 $$D \not\sim 0$$이다.

<div class="definition" markdown="1">

<ins id="def9">**정의 9**</ins> Surface $$S$$의 *Néron–Severi group*은 ([§선다발과 벡터다발, ⁋정의 9](/ko/math/algebraic_geometry/line_bundles#def9))에서 정의한 Picard group $$\Pic(S)$$에서 algebraic equivalence를 취한 몫이다:

$$\operatorname{NS}(S) = \Pic(S) / \{\text{algebraic equivalence}\}$$

이것의 rank $$\rho(S) = \rank \operatorname{NS}(S)$$를 $$S$$의 *Picard number*라고 한다.

</div>

Algebraic equivalence는 numerical equivalence보다 강한 관계이므로 $$\operatorname{NS}(S) \otimes \mathbb{R}$$는 $$\operatorname{Num}(S)$$의 부분 공간이며, 특히 $$\rho(S) \le \rank \operatorname{Num}(S)$$이다. 사실 divisor (= codimension 1 cycle)에 대해서는 Matsusaka의 정리에 의해 algebraic equivalence와 numerical equivalence가 일치함(up to torsion)이 이미 증명되어 있으므로, $$\operatorname{NS}(S) \otimes \mathbb{Q} = \operatorname{Num}(S) \otimes \mathbb{Q}$$이다. 보다 일반적으로, 임의의 codimension의 cycle에 대해 homological equivalence와 numerical equivalence가 일치할 것이라는 Grothendieck의 standard conjecture D는 아직 미해결 문제이다. ([§선다발과 벡터다발, ⁋정의 9](/ko/math/algebraic_geometry/line_bundles#def9))에서 정의한 Picard group은 divisor class들을 분류하는 대수적 대상이며, Néron–Severi group은 여기서 "연속적인" 변화를 factor out하여 얻어지는 이산적인 불변량이다. Picard number $$\rho(S)$$는 surface의 "효과적인" divisor class의 차원을 나타낸다. 예를 들어 $$\mathbb{P}^2$$의 경우 $$\rho = 1$$이며, $$\mathbb{P}^1 \times \mathbb{P}^1$$의 경우 $$\rho = 2$$이다.

([§선형계, ⁋정의 10](/ko/math/algebraic_geometry/linear_systems#def10))에서 정의한 ample line bundle과 대응되는 ample divisor $$H$$는 교차 형식에 대해 특별한 역할을 한다.

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10 (Hodge Index Theorem)**</ins> Smooth projective surface $$S$$와 ample divisor $$H$$에 대해, $$D \cdot H = 0$$이고 $$D \not\equiv 0$$이면 $$D^2 < 0$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$D \cdot H = 0$$이고 $$D \not\equiv 0$$이라고 하자.

**단계 1: $$D^2 \le 0$$임을 보인다.**

만일 $$D^2 > 0$$이라 하자. Riemann–Roch에 의해

$$\rchi(\mathcal{O}(nD)) = \rchi(\mathcal{O}_S) + \frac{n^2 D^2 - n D \cdot K_S}{2}$$

인데, $$D^2 > 0$$이므로 $$n \to \infty$$에서 $$\rchi(\mathcal{O}(nD)) \to +\infty$$이다. Serre duality에 의해 $$h^2(\mathcal{O}(nD)) = h^0(\mathcal{O}(K_S - nD))$$이며, $$n \gg 0$$에서는 $$K_S - nD$$의 intersection number가 음의 방향으로 충분히 커져 $$h^0 = 0$$이 된다. 따라서 $$h^0(\mathcal{O}(nD)) \ge \rchi(\mathcal{O}(nD)) \to +\infty$$이어서, 충분히 큰 $$n > 0$$에 대해 $$nD$$가 effective이다.

그러나 effective divisor $$E \ge 0$$와 ample divisor $$H$$의 교차는 항상 $$E \cdot H > 0$$이다. 한편 $$nD \cdot H = n(D \cdot H) = 0$$이므로 $$nD$$는 effective일 수 없다. 이는 모순이며, 따라서 $$D^2 \le 0$$이다.

**단계 2: $$D^2 = 0$$도 불가능함을 보인다.**

$$D^2 = 0$$이고 $$D \cdot H = 0$$이며 $$D \not\equiv 0$$이라고 가정하자. $$D \not\equiv 0$$이므로, $$D \cdot E \ne 0$$인 어떤 divisor $$E$$가 존재한다.

이 $$E$$로부터 $$H$$에 직교하는 새로운 divisor를 만든다. 즉

$$E' = (H^2)\,E - (E \cdot H)\,H$$

로 정의하면 $$E' \cdot H = (H^2)(E \cdot H) - (E \cdot H)(H^2) = 0$$이다. 또한 $$D \cdot H = 0$$이므로

$$D \cdot E' = (H^2)(D \cdot E) - (E \cdot H)(D \cdot H) = (H^2)(D \cdot E) \ne 0$$

이다 ($$H^2 > 0$$, $$D \cdot E \ne 0$$이므로).

이제 정수 $$n$$을 잡아 $$F_n := nD + E'$$를 생각하자. $$F_n \cdot H = n(D \cdot H) + (E' \cdot H) = 0$$이고

$$F_n^2 = n^2 D^2 + 2n(D \cdot E') + E'^2 = 2n(D \cdot E') + E'^2$$

이다. $$D \cdot E' \ne 0$$이므로 $$n$$의 부호를 적절히 택해 $$\lvert n \rvert$$이 충분히 크면 $$F_n^2 > 0$$이 된다. 그러나 $$F_n \cdot H = 0$$이므로 단계 1에 의해 $$F_n^2 \le 0$$이어야 한다. 모순이다.

따라서 $$D \cdot E = 0$$인 모든 $$E$$에 대해 동일한 논증이 성립하지 않으려면 처음 가정 자체가 잘못된 것이며, 결국 $$D \equiv 0$$이어야 한다. 이는 $$D \not\equiv 0$$ 가정에 모순이므로 $$D^2 = 0$$은 불가능하다. 그러므로 $$D^2 < 0$$이다.

</details>

<div class="proposition" markdown="1">

<ins id="cor11">**따름정리 11**</ins> 교차 형식 on $$\operatorname{Num}(S) \otimes \mathbb{R}$$는 signature $$(1, \rho - 1)$$를 갖는다. 즉, positive direction은 하나뿐이며, 이것은 ample cone에 의해 span된다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Ample divisor $$H$$에 대해 $$H^2 > 0$$이므로 교차 형식은 적어도 하나의 positive direction을 갖는다. Hodge index theorem에 의해 $$H$$에 orthogonal인 모든 nonzero 방향은 음의 self-intersection을 갖는다. 따라서 $$\operatorname{Num}(S) \otimes \mathbb{R}$$을 $$\mathbb{R} \cdot H$$와 그 orthogonal complement로 분해하면, 전자에서 이차 형식은 양의 정부호이고 후자에서는 음의 정부호이다. Sylvester의 관성법칙에 의해 signature는 $$(1, \rho - 1)$$이다.

</details>

Hodge index theorem의 기하학적 의미는 다음과 같다. Surface 위의 교차 형식은 특수상대성이론의 Minkowski space와 유사하게, positive direction 하나와 negative direction $$\rho - 1$$개를 갖는 이차 형식이다. Ample cone이 이 유일한 positive direction을 span하므로, surface 위의 "양수" 방향은 본질적으로 하나뿐이며, 다른 모든 방향은 어떤 의미에서 "음수"이다. 이 결과는 surface의 birational geometry에서 minimal model의 유일성과 같은 깊은 결과들을 이끌어낸다.

## Noether 공식

<div class="proposition" markdown="1">

<ins id="prop12">**명제 12**</ins> (Noether Formula) Smooth projective surface $$S$$에 대해

$$K_S^2 + c_2(S) = 12\,\rchi(\mathcal{O}_S)$$

이 성립한다. 여기서 $$K_S^2 = K_S \cdot K_S$$는 canonical divisor의 self-intersection number이고, $$c_2(S)$$는 tangent bundle의 top Chern class이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

먼저 $$D = K_S$$를 [명제 4](#prop4)에 대입하면

$$\rchi(\mathcal{O}(K_S)) = \frac{1}{2}K_S \cdot (K_S - K_S) + \rchi(\mathcal{O}_S) = \rchi(\mathcal{O}_S)$$

이다. 한편 Serre duality에 의해 $$h^i(K_S) = h^{2-i}(\mathcal{O}_S)$$이므로

$$\rchi(\mathcal{O}(K_S)) = h^0(K_S) - h^1(K_S) + h^2(K_S) = h^2(\mathcal{O}_S) - h^1(\mathcal{O}_S) + h^0(\mathcal{O}_S) = \rchi(\mathcal{O}_S)$$

이다. 이는 직접 계산으로 확인할 수 있으며, $$c_2$$가 등장하지 않으므로 이 접근만으로는 Noether 공식을 유도할 수 없다.

대신 다음과 같이 증명한다. 먼저 Gauss–Bonnet 정리에 의해 compact complex surface의 topological Euler characteristic은

$$e(S) = c_2(T_S) = 2 - 2b_1 + b_2$$

이다. Smooth projective surface는 Kähler이므로 Hodge theory를 적용할 수 있다. Hodge decomposition에 의해 $$b_1 = 2q$$이고, $$H^2(S, \mathbb{C}) = H^{2,0} \oplus H^{1,1} \oplus H^{0,2}$$에서 $$H^{2,0} \oplus H^{0,2}$$는 positive definite이고 $$H^{1,1}$$ 위의 교차 형식은 signature $$(1, h^{1,1}-1)$$를 갖는다. 따라서

$$b_2^+ = 2p_g + 1, \quad b_2^- = h^{1,1} - 1, \quad \tau = b_2^+ - b_2^- = 2p_g + 2 - h^{1,1}$$

이다. 한편 Hirzebruch의 표시 정리에 의해

$$\tau = \frac{1}{3}(K_S^2 - 2e(S))$$

이다. 이들을 정리하면

$$\begin{aligned}
K_S^2 + e(S) &= 3\tau + 2e(S) + e(S) \\
&= 3(2p_g + 2 - h^{1,1}) + 3(2 - 4q + 2p_g + h^{1,1}) \\
&= 12p_g + 12 - 12q \\
&= 12(1 - q + p_g) = 12\,\rchi(\mathcal{O}_S)
\end{aligned}$$

를 얻는다. Gauss–Bonnet 정리에 의해 $$e(S) = c_2(S)$$이므로 $$K_S^2 + c_2(S) = 12\,\rchi(\mathcal{O}_S)$$가 성립한다.

</details>

Noether 공식은 곡면의 세 가지 기본적인 불변량인 canonical self-intersection $$K_S^2$$, topological Euler number $$c_2(S)$$, 그리고 holomorphic Euler characteristic $$\rchi(\mathcal{O}_S)$$ 사이의 관계를 제공한다. 이는 곡면의 분류에서 핵심적인 역할을 한다.

<div class="example" markdown="1">

<ins id="ex13">**예시 13**</ins> **$$\mathbb{P}^2$$**: $$K_{\mathbb{P}^2} = -3H$$이므로 $$K_{\mathbb{P}^2}^2 = (-3H)^2 = 9$$이고, $$\rchi(\mathcal{O}_{\mathbb{P}^2}) = 1$$이다. Noether 공식에 의해 $$9 + c_2 = 12$$, 즉 $$c_2(\mathbb{P}^2) = 3$$이다. 이는 $$\mathbb{P}^2$$의 topological Euler characteristic이 3이라는 것을 의미하며, 이는 $$\mathbb{P}^2$$의 cell decomposition $$\{\text{pt}\} \subset \mathbb{P}^1 \subset \mathbb{P}^2$$ (점 + affine 직선 + affine 평면)으로부터 $$\rchi_{\text{top}} = 1 + 1 + 1 = 3$$으로도 확인된다.

</div>

## Application: Plurigenera

Curve의 경우, genus $$g$$는 curve의 birational equivalence class를 완전히 결정한다. Surface에서는 상황이 더 복잡한데, 그 이유는 birational equivalence가 cohomology의 차원을 모두 보존하지 않기 때문이다. 그러나 canonical bundle의 tensor power의 global section 차원은 birational invariant이며, 이 값들이 surface의 birational type에 대한 필수적인 정보를 제공한다.

<div class="definition" markdown="1">

<ins id="def14">**정의 14**</ins> Surface $$S$$의 *$$m$$-th plurigenus*는

$$P_m(S) = h^0(S, \omega_S^{\otimes m})$$

이다. 여기서 $$\omega_S = \mathcal{O}_S(K_S)$$는 ([§표준선다발, ⁋정의 5](/ko/math/algebraic_geometry/canonical_bundle#def5))에서 정의한 canonical bundle이다.

</div>

$$m = 1$$인 경우 $$P_1(S) = h^0(\omega_S) = p_g(S)$$는 geometric genus이다. Plurigenus들의 열 $$\{P_m(S)\}_{m \ge 1}$$은 surface의 birational equivalence class를 결정하는 중요한 불변량이다. ([§표준선다발, ⁋정의 5](/ko/math/algebraic_geometry/canonical_bundle#def5))에서 살펴본 canonical bundle의 역할과 마찬가지로, $$\omega_S^{\otimes m}$$의 global section은 surface 위의 "multi-differential form", 즉 $$m$$개의 canonical divisor를 tensor한 형태의 differential form을 parameterize한다. 예를 들어 local coordinate $$z_1, z_2$$에서 $$\omega_S^{\otimes m}$$의 section은 $$f(z_1, z_2)(dz_1 \wedge dz_2)^{\otimes m}$$의 꼴로 쓰인다.

Plurigenus의 증가율은 surface의 Kodaira dimension과 밀접하게 관련되어 있다. Kodaira dimension $$\kappa(S)$$는 $$P_m(S)$$의 $$m$$에 대한 증가 차수로 정의된다. 구체적으로, 모든 $$m \ge 1$$에 대해 $$P_m(S) = 0$$이면 $$\kappa = -\infty$$이다. 그렇지 않은 경우, $$\kappa(S)$$는 $$P_m(S) / m^\kappa$$가 유계(bounded)가 되는 최소의 정수 $$\kappa$$로 정의된다. 즉 $$\kappa(S) = \min\{k \in \mathbb{Z}_{\ge 0} : P_m(S) = O(m^k)\}$$이다. 이 정의에 의하면 $$\kappa = 0$$은 $$P_m(S)$$가 항상 $$0$$ 또는 $$1$$이면서 모든 $$m$$에 대해 $$0$$인 것은 아닌 경우이며, $$\kappa = 1$$은 $$P_m(S) \sim cm$$으로 선형 성장하는 경우, $$\kappa = 2$$는 $$P_m(S) \sim cm^2$$으로 이차 성장하는 경우이다. Surface의 경우 $$\kappa \in \{-\infty, 0, 1, 2\}$$이다.

<div class="proposition" markdown="1">

<ins id="prop15">**명제 15**</ins> $$m \ge 2$$에 대해, 만일 $$h^0(\mathcal{O}_S((1-m)K_S)) = 0$$이면

$$P_m(S) \ge \rchi(\mathcal{O}_S) + \frac{m(m-1)}{2} K_S^2$$

이다. 가설 $$h^0(\mathcal{O}_S((1-m)K_S)) = 0$$은 Serre duality에 의해 $$h^2(\omega_S^{\otimes m}) = 0$$과 동치이며, 이는 $$m \gg 0$$에서 항상 만족된다—$$(1-m)K_S$$가 어떤 effective divisor보다도 "더 음수"이기 때문이다.

특히 $$K_S$$가 ample이고 $$m \ge 2$$이면

$$P_m(S) = \rchi(\mathcal{O}_S) + \frac{m(m-1)}{2} K_S^2$$

이 성립한다. 따라서 $$K_S$$가 ample인 surface는 Kodaira dimension $$2$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Riemann–Roch 공식 ([명제 4](#prop4))에 $$D = mK_S$$를 대입한다:

$$\rchi(\omega_S^{\otimes m}) = \rchi(\mathcal{O}_S) + \frac{1}{2}\left((mK_S)^2 - (mK_S) \cdot K_S\right) = \rchi(\mathcal{O}_S) + \frac{1}{2}\left(m^2 K_S^2 - m K_S^2\right)$$

$$= \rchi(\mathcal{O}_S) + \frac{m(m-1)}{2} K_S^2$$

한편 $$\rchi(\omega_S^{\otimes m}) = h^0(\omega_S^{\otimes m}) - h^1(\omega_S^{\otimes m}) + h^2(\omega_S^{\otimes m})$$이다. Serre duality에 의해 $$h^2(\omega_S^{\otimes m}) = h^0(\mathcal{O}_S((1-m)K_S))$$이다. 이 값은 명제의 가설에 의해 $$0$$이다. 따라서

$$P_m(S) = h^0(\omega_S^{\otimes m}) = \rchi(\omega_S^{\otimes m}) + h^1(\omega_S^{\otimes m}) \ge \rchi(\omega_S^{\otimes m}) = \rchi(\mathcal{O}_S) + \frac{m(m-1)}{2} K_S^2$$

이다. 이로써 첫 번째 부등식이 얻어진다.

이제 $$K_S$$가 ample인 경우를 생각하자. Kodaira vanishing theorem에 의해, ample line bundle $$\mathcal{L}$$에 대해 $$H^i(X, \mathcal{L} \otimes \omega_X) = 0$$ for $$i > 0$$이다. $$\omega_S^{\otimes m} = \mathcal{O}_S(mK_S) = \mathcal{O}_S((m-1)K_S) \otimes \omega_S$$이고, $$K_S$$가 ample이면 $$m \ge 2$$에서 $$(m-1)K_S$$도 ample이므로

$$h^1(\omega_S^{\otimes m}) = 0$$

이다. 따라서 $$P_m(S) = \rchi(\omega_S^{\otimes m})$$이 되어 등식이 성립한다. 또한 $$K_S^2 > 0$$이므로 $$P_m(S)$$는 $$m^2$$의 차수로 증가하며, 이로부터 $$\kappa(S) = 2$$임을 확인할 수 있다.

</details>

## 예시: K3 Surface

지금까지의 도구들을 구체적인 surface에 적용해 보자. K3 surface는 canonical bundle이 trivial인 surface 중 가장 중요한 부류이다. "K3"라는 이름은 André Weil이 1958년에 명명한 것으로, Kummer, Kähler, Kodaira 세 수학자의 이름과 카라코람의 아름다운 산 K2를 동시에 기리고 있다 ([BHPV], [Huyb]). 이들은 각각 K3 surface의 서로 다른 측면을 연구하였다.

<div class="definition" markdown="1">

<ins id="def16">**정의 16**</ins> Smooth projective surface $$S$$가 *K3 surface*라는 것은 $$K_S \sim 0$$ (trivial canonical bundle)이고 $$h^1(S, \mathcal{O}_S) = 0$$인 것이다.

</div>

K3 surface의 가장 친숙한 예시는 $$\mathbb{P}^3$$ 안의 quartic surface, 즉 degree $$4$$ homogeneous 다항식의 zero set이다. ([§표준선다발, ⁋명제 9](/ko/math/algebraic_geometry/canonical_bundle#prop9))에서 다룬 adjunction formula에 의해 $$\mathbb{P}^3$$ 안의 degree $$d$$ smooth hypersurface $$S$$의 canonical bundle은

$$K_S = (K_{\mathbb{P}^3} + S)\vert_S = (\mathcal{O}_{\mathbb{P}^3}(-4) + \mathcal{O}_{\mathbb{P}^3}(d))\vert_S = \mathcal{O}_S(d - 4)$$

이다. 따라서 $$d = 4$$이면 $$K_S = \mathcal{O}_S(0) = 0$$이 되어 trivial canonical bundle을 갖는다. 또한 Lefschetz hyperplane theorem에 의해 $$H^1(S, \mathbb{C}) \cong H^1(\mathbb{P}^3, \mathbb{C}) = 0$$이고, Hodge decomposition $$H^1(S, \mathbb{C}) = H^{1,0}(S) \oplus H^{0,1}(S)$$에서 $$H^{0,1}(S) \cong H^1(S, \mathcal{O}_S)$$이므로 $$h^1(S, \mathcal{O}_S) = 0$$이 성립한다.

$$K_S \sim 0$$이므로 K3 surface 위에서 Riemann–Roch 공식은 극도로 단순해진다. Canonical bundle이 trivial이므로 $$D \cdot K_S = 0$$이고 $$K_S^2 = 0$$이며, 따라서

$$\rchi(\mathcal{O}_S(D)) = \rchi(\mathcal{O}_S) + \frac{D^2}{2}$$

이다. $$h^1(S, \mathcal{O}_S) = 0$$과 Serre duality $$h^2(\mathcal{O}_S) = h^0(K_S) = h^0(\mathcal{O}_S) = 1$$에 의해 $$\rchi(\mathcal{O}_S) = 1 - 0 + 1 = 2$$이다. 따라서:

$$\rchi(\mathcal{O}_S(D)) = 2 + \frac{D^2}{2}$$

이 공식은 K3 surface의 기하학을 이해하는 강력한 도구이다. 예를 들어 $$D^2 \ge -2$$이면 $$\rchi(\mathcal{O}_S(D)) \ge 1$$이 되어, $$h^0(\mathcal{O}(D)) \ge 1$$ 또는 $$h^0(\mathcal{O}(-D)) \ge 1$$이 성립한다. 전자의 경우 $$D$$가 linearly equivalent한 effective divisor가 존재한다는 것을 의미한다. 특히 $$D^2 = -2$$이면 $$\rchi(\mathcal{O}(D)) = 1$$이고, 만일 $$h^0(\mathcal{O}(D)) = 0$$이라면 Serre duality에 의해 $$h^2(\mathcal{O}(D)) = h^0(\mathcal{O}(-D)) \ge 1$$이어야 하는데, 이는 $$-D$$가 effective라는 뜻이다. 따라서 $$D$$ 또는 $$-D$$ 중 적어도 하나는 effective이다.

K3 surface 위에서 $$D^2 = -2$$를 갖는 effective divisor $$D$$에 대해, adjunction formula $$2p_a - 2 = D^2 + D \cdot K_S = -2$$에서 arithmetic genus $$p_a(D) = 0$$을 얻는다. 만일 $$D$$가 기약 곡선(irreducible curve)이면, $$p_a(D) = 0$$은 $$D \cong \mathbb{P}^1$$임을 의미한다. (일반적으로 effective divisor는 여러 기약 성분으로 분해될 수 있으므로, $$D$$가 기약이라는 조건이 필요하다.) 이러한 기약 곡선을 $$(-2)$$-curve라 부르며, K3 surface의 automorphism group을 이해하는 데 핵심적인 역할을 한다.

한편 K3 surface의 모든 plurigenus는 같다. $$K_S \sim 0$$이므로 $$\omega_S^{\otimes m} \cong \mathcal{O}_S$$이고, 따라서 $$P_m(S) = h^0(\mathcal{O}_S) = 1$$ for all $$m \ge 1$$이다. 이는 K3 surface가 Kodaira dimension $$0$$임을 의미한다.

[명제 15](#prop15)의 부등식은 $$h^0(\mathcal{O}_S((1-m)K_S)) = 0$$ (Serre duality에 의해 $$h^2(\omega_S^{\otimes m}) = 0$$과 동치)이라는 조건 하에서 성립한다. 그런데 K3 surface에서는 $$K_S \sim 0$$이므로 $$\omega_S^{\otimes(1-m)} \cong \mathcal{O}_S$$이고 $$h^0(\mathcal{O}_S((1-m)K_S)) = h^0(\mathcal{O}_S) = 1 \ne 0$$이어서 가설이 위배된다. 실제로 $$K_S^2 = 0$$, $$\rchi(\mathcal{O}_S) = 2$$이므로 [명제 15](#prop15)의 우변은 $$2$$이지만 $$P_m(S) = 1 < 2$$이다. 이는 $$h^2$$ 항이 0이 아니기 때문이며, full Euler characteristic은 $$\rchi(\omega_S^{\otimes m}) = h^0 - h^1 + h^2 = 1 - 0 + 1 = 2$$로 부등식의 우변과 정확히 일치한다. 이 예시는 $$h^2 = 0$$ 가정이 실제로 필요하다는 것을 잘 보여준다.

---

**참고문헌**

**[Hart]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[BHPV]** W. Barth, K. Hulek, C. Peters, A. Van de Ven, *Compact Complex Surfaces*, Springer, 2004.  
**[Huyb]** D. Huybrechts, *Lectures on K3 Surfaces*, Cambridge University Press, 2016.