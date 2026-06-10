---
title: "곡면에서의 리만-로흐 정리"
description: "곡선에서의 리만-로흐 정리를 곡면으로 일반화하는 과정에서 교차수를 정의하고, 호지 지표 정리와 복수 생성자에 대한 부등식을 증명하며, 교차 형식의 기하학적 의미를 살펴본다."
excerpt: "Intersection theory on surfaces and its applications"

categories: [Math / Algebraic Varieties]
permalink: /ko/math/algebraic_varieties/riemann_roch_surfaces
sidebar: 
    nav: "algebraic_varieties-ko"

date: 2026-05-04
last_modified_at: 2026-05-09
weight: 16
---

우리는 앞선 글에서 Riemann-Roch 정리를 곡선에서 살펴보았다. 본질적으로 Riemann-Roch 정리는 Euler characteristic을 다른 정량적인 수치들로 계산하는 것으로, 더 일반적으로 우리는 임의의 경우로 이를 일반화할 수도 있으나 이번 글에서는 surface로의 일반화만  다루기로 한다.

다시 curve $$C$$에서의 Riemann-Roch formula ([§곡선에서의 리만-로흐 정리, ⁋명제 3](/ko/math/algebraic_varieties/riemann_roch_theorem#prop3))

$$\ell(D) - \ell(K_C - D) = \deg D + 1 - g$$

를 살펴보면, 이 식의 좌변은 본질적으로 $$\mathcal{O}_C(D)$$의 Euler characteristic이며 [§곡선에서의 리만-로흐 정리, ⁋보조정리 2](/ko/math/algebraic_varieties/riemann_roch_theorem#lem2)가 이 부분이 두 개의 항만으로 나온다는 것을 보장한다. 그러나 이제 곡면에서 이를 일반화하기 위해서는 base space의 차원이 하나 커지므로 추가적인 항이 등장할 것이며, 이에 대응하여 우변의 식 또한 추가적인 항이 등장하게 될 것이다.

직관적으로, 위 식의 우변에서 등장하는 $$\deg D$$는 일종의 선형인 항이라 생각할 수 있으나, 이렇게 곡면에서의 일반화를 하는 과정에서 우리는 추가적인 <em-ko>이차항들</em-ko> $$D\cdot D$$, $$D\cdot K_S$$ 등을 고려하게 된다. 이들은 surface 위의 두 divisor가 얼마나 교차하는지를 담고 있는 양으로, curve case에서의 divisor들, 즉 점들은 곡선 안에서 일반적으로 만나지 않지만, 곡면에서의 divisor들, 즉 곡선들은 이 곡면 안에서 일반적으로 유한 개의 점에서 만나기 때문에 생겨난다. 

이 글에서는 intersection number의 정의와 그 기본 성질을 다루고, Riemann–Roch 공식을 엄밀하게 유도한 뒤, 이를 활용하여 Hodge index theorem과 plurigenera에 대한 부등식을 증명한다. 또한 교차 형식이 surface의 birational geometry에서 갖는 의미를 살펴본다.

## 교차수

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

## 곡면에서의 리만-로흐 정리

이제 우리는 Riemann-Roch 정리를 곡면으로 확장할 때 필요한 언어를 전부 가지고 있다. 이제 우리에게 필요한 것은 다음의 보조정리이다. 

<div class="proposition" markdown="1">

<ins id="lem3">**보조정리 3 (Genus formula)**</ins> Smooth projective surface $$S$$ 위의 smooth irreducible curve $$D$$에 대해

$$2g(D) - 2 = D^2 + D \cdot K_S$$

이 성립한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Adjunction formula ([§표준선다발, ⁋명제 9](/ko/math/algebraic_varieties/canonical_bundle#prop9))에 의해

$$\omega_D \cong (\omega_S \otimes \mathcal{O}_S(D))\vert_D$$

이다. 양변의 degree를 취하면

$$\deg(\omega_D) = \deg(\omega_S\vert_D) + \deg(\mathcal{O}_D(D))$$

이다. 우리는 앞서 [§곡선에서의 리만-로흐 정리, ⁋명제 3](/ko/math/algebraic_varieties/riemann_roch_theorem#prop3)의 결과로 $$\deg(\omega_D)=2g-2$$라는 것을 유도하였으며 우변의 두 항만 intersection numbery로 해석하면 된다. 우선 $$\omega_S\vert_D$$는 $$D$$ 위로 restriction된 canonical bundle로, 이는 $$D$$와 canonical divisor $$K_S$$의 교차수를 측정한다. 구체적으로 $$K_S$$가 $$\omega_S$$에 대응하는 divisor이므로, $$\omega_S\vert_D$$의 degree는 $$D$$ 위에서 $$K_S$$가 차지하는 점들의 수, 즉 $$D \cdot K_S$$가 된다. 비슷하게 $$\mathcal{O}_D(D)$$는 $$D$$의 normal bundle $$\mathcal{N}_{D/S}$$에 해당하며, 이는 $$D$$가 $$S$$ 안에서 자기 자신과 만나는 정도를 측정한다. 이 bundle의 degree는 $$D$$의 self-intersection number $$D^2$$와 일치한다. 이들을 종합하면

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

이다. 이 때, $$\mathcal{O}_D(D)$$는 $$D$$ 위에 정의된 line bundle이므로, 곡선에서의 Riemann–Roch ([§곡선에서의 리만-로흐 정리, ⁋명제 3](/ko/math/algebraic_varieties/riemann_roch_theorem#prop3))에 의해

$$\rchi(\mathcal{O}_D(D)) = D^2 + 1 - g(D)$$

이다. 앞선 [보조정리 3](#lem3)에서 

$$g(D) = \frac{1}{2}(D^2 + D \cdot K_S) + 1$$

이므로, 이를 대입하면

$$\rchi(\mathcal{O}_D(D)) = D^2 + 1 - \frac{1}{2}(D^2 + D \cdot K_S) - 1 = \frac{1}{2}D \cdot (D - K_S)$$

이다. 따라서

$$\rchi(\mathcal{O}_S(D)) = \rchi(\mathcal{O}_S) + \frac{1}{2}D \cdot (D - K_S)$$

를 얻는다.

이제 우리는 이를 일반적인 divisor $$D$$에 대해 이를 일반화해야 한다. 우리는 우선 $$S$$ 위의 ample divisor $$H$$를 고정하자. 그럼 Serre vanishing theorem ([§사영공간의 코호몰로지, ⁋명제 4](/ko/math/algebraic_varieties/cohomology_of_projective_spaces#prop4))에 의해, 충분히 큰 $$n$$에 대해 

$$H^1(S, \mathcal{O}_S(D + nH)) = H^2(S, \mathcal{O}_S(D + nH)) = 0$$

이다. 따라서

$$\rchi(\mathcal{O}_S(D + nH)) = h^0(\mathcal{O}_S(D + nH))$$

가 성립한다. 한편 $$D+nH$$는 effective divisor이므로, 앞선 논증에 의해 $$D+nH$$에 대해서는 원하는 등식이 성립한다. 따라서 $$n$$에 대한 두 함수 $$f(n) = \rchi(\mathcal{O}(D+nH))$$와 $$g(n) = \frac{1}{2}(D+nH)\cdot(D+nH-K_S) + \rchi(\mathcal{O}_S)$$를 생각하면 이들은 충분히 큰 $$n$$에 대해서는 항상 일치한다. 그런데 앞서 언급한 Snapper's theorem에 의해 $$\rchi(\mathcal{O}_S(D+nH))$$는 $$n$$에 대한 다항식이고, 무한히 많은 점들에 대해 그 값이 일치하는 다항식은 서로 같으므로 $$f$$와 $$g$$는 사실 같은 다항식이다. 즉, 모든 $$n$$에 대해 $$f(n) = g(n)$$이며 특히 $$n = 0$$을 대입하면

$$\rchi(\mathcal{O}(D)) = \frac{1}{2}D\cdot(D-K_S) + \rchi(\mathcal{O}_S)$$

를 얻는다.

</details>

Curve의 경우와 마찬가지로, 만약 $$D$$가 충분히 "양의" 방향이라면 $$h^1$$과 $$h^2$$가 사라져 $$\rchi(\mathcal{O}_S(D)) = h^0(S, \mathcal{O}_S(D))$$가 된다. 이는 ([§선형계, ⁋정의 10](/ko/math/algebraic_varieties/linear_systems#def10))에서 정의한 ampleness 개념과 밀접하게 관련되어 있다.

<div class="example" markdown="1">

<ins id="ex5">**예시 5 ($$\mathbb{P}^2$$)**</ins> 우리는 $$\mathbb{P}^2$$에서 hyperplane class $$H$$를 고정하면

$$K_{\mathbb{P}^2} = -3H, \qquad \rchi(\mathcal{O}_{\mathbb{P}^2}) = 1$$

임을 안다.  ([§표준선다발, ⁋명제 7](/ko/math/algebraic_varieties/canonical_bundle#prop7), [§사영공간의 코호몰로지, ⁋따름정리 3](/ko/math/algebraic_varieties/cohomology_of_projective_spaces#cor3)) $$\mathbb{P}^2$$에서 임의의 두 직선은 일반적으로 한 점에서 만나므로, $$H$$의 self-intersection number는 1이며 따라서 임의의 divisor $$D = dH$$에 대해

$$\rchi(\mathcal{O}_{\mathbb{P}^2}(d)) = \frac{1}{2}dH \cdot (dH + 3H) + 1 = \frac{1}{2}d(d+3) + 1$$

이 성립한다. 이것이 실제로 성립한다는 것은 [§사영공간의 코호몰로지, ⁋따름정리 3](/ko/math/algebraic_varieties/cohomology_of_projective_spaces#cor3)의 결과이다. 특별히 $$d \ge 0$$에 대해서는 $$h^0 = \binom{d+2}{2}$$이고 $$h^1 = h^2 = 0$$임을 알고 있으므로, 이것이 위에서 언급한 $$h^1, h^2$$의 vanishing에 대한 직접적인 예시가 된다. 

</div>

<div class="example" markdown="1">

<ins id="ex6">**예시 6 (Blow-up of $$\mathbb{P}^2$$)**</ins> 이제 우리는 $$\mathbb{P}^2$$의 한 점 $$p$$에서의 blow-up $$\pi: \widetilde{\mathbb{P}}^2 \to \mathbb{P}^2$$을 생각한다. [§표준선다발, ⁋명제 12](/ko/math/algebraic_varieties/canonical_bundle#prop12)에 의해, canonical bundle은 다음의 식

$$K_{\widetilde{\mathbb{P}}^2} = \pi^\ast K_{\mathbb{P}^2} + E = -3H + E$$

으로 주어진다. $$\mathbb{P}^2$$에서는 hyperplane class $$H$$가 점 $$p$$를 피하도록 잡을 수 있으므로 $$H \cdot E = 0$$이다. 한편 $$E \cong \mathbb{P}^1$$이며, $$E$$의 normal bundle $$\mathcal{N}_{E/\widetilde{\mathbb{P}}^2}$$는 $$\mathcal{O}_{\mathbb{P}^1}(-1)$$와 isomorphic하며 이로부터 self-intersection number $$E^2 = \deg(\mathcal{N}_{E/\widetilde{\mathbb{P}}^2}) = -1$$이며, 기하학적으로 이는 $$E$$가 한 점으로 collapse되면서 주변에서 "접혀 들어가" negativity를 갖게 됨을 의미한다. 따라서 일반적인 divisor $$D = dH - kE$$에 대해서는

$$\rchi(\mathcal{O}_{\widetilde{\mathbb{P}}^2}(dH - kE)) = \frac{1}{2}(dH - kE) \cdot (dH - kE + 3H - E) + 1 = \frac{1}{2}d(d+3) - \frac{1}{2}k(k+1) + 1$$

임을 계산할 수 있다.

</div>

한편 곡선에서의 Riemann-Roch 정리는 위의 [명제 4](#prop4)에서 [§세르 쌍대성, ⁋명제 4](/ko/math/algebraic_varieties/serre_duality#prop4)를 적용하여 $$h^1$$ 부분을 $$h^0$$으로 바꾼 것으로, 곡면에서의 경우에도 이를 활용하여 $$h^2(\mathcal{O}(D)) = h^0(\omega_S(-D))$$로 적을 수 있고, 그럼 Riemann–Roch 공식은 다음의 식

$$h^0(\mathcal{O}(D)) - h^1(\mathcal{O}(D)) + h^0(\omega_S(-D)) = \rchi(\mathcal{O}_S) + \frac{1}{2}(D^2 - D \cdot K_S)$$

으로 변하게 된다. 일반적으로 $$h^1(\mathcal{O}(D))$$는 직접 계산하기 어려운 항이지만, 만일 이 값이 0이거나 충분히 작다고 가정할 수 있다면 우리는 $$h^0(\mathcal{O}(D))$$와 $$h^0(\omega_S(-D))$$ 중 적어도 하나가 충분히 크다는 것을 보일 수 있다. 이를 위한 강력한 도구 중 하나는 다음의 Kodaira vanishing theorem이다.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7 (Kodaira Vanishing Theorem)**</ins> Smooth projective variety $$X$$와 ample line bundle $$L$$에 대하여,

$$H^i(X, \omega_X \otimes L) = 0$$

가 모든 $$i > 0$$에 대해 성립한다.

</div>

Kodaira vanishing theorem의 본격적인 응용은 다음 글에서 다룬다. 이 공식의 유용성을 이해하기 위해 두 극단적인 경우를 생각해 보자. 만일 $$D$$가 "충분히 양수", 즉 $$D \cdot H$$가 ample divisor $$H$$에 대해 충분히 크다면, $$K_S - D$$는 "음수" 방향이 되어 $$h^0(\omega_S(-D)) = 0$$이 되고 Riemann–Roch는 $$h^0$$에 대한 하한을 준다. 반대로 $$D$$가 "충분히 음수"이면 $$h^0(\mathcal{O}(D)) = 0$$이 되고 $$K_S - D$$의 정보를 얻는다. 이러한 "양수와 음수의 대칭"은 Serre duality가 만들어내는 현상이다.

$$\mathbb{P}^2$$에 대한 Riemann–Roch 계산은 이미 [예시 5](#ex5)에서 다루었다. 여기서는 다른 근본적인 예시를 살펴본다.

<div class="example" markdown="1">

<ins id="ex8">**예시 8 ($$\mathbb{P}^1 \times \mathbb{P}^1$$)**</ins> $$\mathbb{P}^1 \times \mathbb{P}^1$$을 생각하자. 이 surface의 divisor class group은 $$\mathbb{Z} \oplus \mathbb{Z}$$이며, 각 factor의 hyperplane class $$H_1, H_2$$가 generator로, 이들은 첫 번째와 두 번째 factor를 고정하고 $$\mathbb{P}^1$$의 copy를 붙인 것들이다. 즉 기하학적으로 $$H_1$$은 첫 번째 factor의 점들에 대응하는 "수평" fiber들이고, $$H_2$$는 두 번째 factor의 점들에 대응하는 "수직" fiber들이다. 두 수평 fiber는 서로 평행이므로 만나지 않아 $$H_1^2 = 0$$이고, 마찬가지로 $$H_2^2 = 0$$이다. 반면 수평 fiber와 수직 fiber는 항상 한 점에서 만나므로 $$H_1 \cdot H_2 = 1$$이다.

Canonical divisor는 $$K = -2H_1 - 2H_2$$이며, 이는 $$\mathbb{P}^1$$의 canonical divisor $$-2H$$로부터 오는 것이다. 한편 structure sheaf의 Euler characteristic의 경우, Künneth formula를 사용하여

$$\rchi(\mathcal{O}) = \rchi(\mathcal{O}_{\mathbb{P}^1}) \cdot \rchi(\mathcal{O}_{\mathbb{P}^1}) = 1 \cdot 1 = 1$$

가 됨을 확인할 수 있다. 이는 [\[대수적 위상수학\] §코호몰로지, ⁋따름정리 10](/ko/math/algebraic_topology/cohomology#cor10)과 유사한 결과이기는 하지만 그 증명은 다소 기술적인 부분이 있어 생략하기로 한다. 이제 이를 사용하여 bidegree $$(a, b)$$의 divisor $$D = aH_1 + bH_2$$에 대해 Riemann–Roch 공식을 적용하면

$$\rchi(\mathcal{O}(D)) = 1 + \frac{1}{2}(D^2 - D \cdot K)$$

을 얻는다. 여기서 $$D^2 = (aH_1 + bH_2)^2 = 2ab$$이고, $$D \cdot K =  -2a - 2b$$이므로

$$\rchi(\mathcal{O}(D)) = 1 + \frac{1}{2}(2ab + 2a + 2b) = (a+1)(b+1)$$

을 얻는다. 이는 bidegree $$(a, b)$$를 갖는 bihomogeneous polynomial의 parameter 개수와 일치한다. 예를 들어 $$D = H_1 + H_2$$는 $$(1,1)$$-bidegree 곡선으로, $$\rchi = 4$$이며 이는 $$\mathbb{P}^1 \times \mathbb{P}^1$$ 위의 $$(1,1)$$-곡선이 conic과 동치라는 사실과 부합한다.

</div>

## 호지 지표 정리

고정된 smooth variety $$X$$에 대하여, 우리는 $$X$$의 divisor들의 모임 $$\Pic(X)$$이 $$1$$차원의 cohomology에 해당하는 것을 안다. ([§층 코호몰로지, ⁋명제 22](/ko/math/algebraic_varieties/sheaf_cohomology#prop22)) 한편 cohomology 위에 정의된 cup product는 일반적으로 intersection product의 dual이므로 ([\[대수적 위상수학\] §푸앵카레 쌍대성, ⁋예시 16](/ko/math/algebraic_topology/Poincare_duality#ex16)) cohomology를 algebra로서 이해하기 위해서는 intersection product를 이해하면 충분하다. 그런데 우리는 곡면의 경우를 탐구하고 있으므로, nontrivial한 원소가 등장하는 것은 오직 세 개의 차원 $$H^0, H^1, H^2$$에서 뿐이며, cup product는 graded multiplication이므로 이들의 곱이 nontrivial하게 의미가 있는 것은 $$1$$차원의 원소들을 서로 곱할 때, 즉 divisor들의 intersection product에 해당하는 경우뿐이다.

따라서 우리는 divisor들을 모아두고, 이들의 intersection product가 무엇인지 살펴보아 cohomology ring의 곱셈구조를 살펴볼 수 있다. 이를 위해 우선 다음을 정의한다. 

<div class="definition" markdown="1">

<ins id="def9">**정의 9**</ins> 두 divisor $$D_1, D_2$$가 *numerically equivalent<sub>수치적으로 동치</sub>* $$D_1 \equiv D_2$$라는 것은, 모든 divisor $$E$$에 대해 $$D_1 \cdot E = D_2 \cdot E$$인 것이다. Numerical equivalence class의 집합을

$$\Num(S) = \Div(S) / \{\text{numerical equivalence}\}$$

라고 하며, real vector space $$\Num(S) \otimes \mathbb{R}$$ 위에 intersection product가 유도하는 quadratic form을 *intersection form*이라 부른다. 

</div>

위의 동치관계는 별다른 것이 아니고, divisor들의 intersection product를 생각할 때 같은 값을 주는 원소들은 같은 것으로 보는 equivalence class에 불과하다. 일반적으로 numerical equivalence는 linear equivalence보다 약한 관계이므로, numerically equivalent한 두 divisor는 서로 linearly equivalent하지 않을 수도 있다. 

한편, ample line bundle과 대응되는 ample divisor ([§선형계, ⁋정의 10](/ko/math/algebraic_varieties/linear_systems#def10)) $$H$$는 intersection product에서 특별한 역할을 한다. 이는 근본적으로 (very) ample divisor와 effective divisor의 intersection number는 반드시 양수라는 사실로부터 기인하는 것으로, 이는 very ample divisor를 이용하여 projective variety를 projective space 안으로 넣었을 때, effective divisor와 very ample divisor의 실제 교집합을 생각하여 증명할 수 있다. 이를 활용하면 다음을 얻는다. 

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10 (Hodge Index Theorem)**</ins> Smooth projective surface $$S$$와 ample divisor $$H$$를 고정하자. 만일 divisor $$D$$가 $$D \cdot H = 0$$이고 $$D \not\equiv 0$$을 만족하면 $$D^2 < 0$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

우선 $$D^2>0$$이라 가정하자. [§사영공간의 코호몰로지, ⁋명제 10](/ko/math/algebraic_varieties/cohomology_of_projective_spaces#prop10)를 사용하면 우리는 $$H_n=D+nH$$가 very ample이도록 할 수 있다. 그럼

$$D \cdot H_n = D^2 + n(D \cdot H) = D^2 > 0$$

이다. 한편 Serre duality에 의해 $$h^2(\mathcal{O}(mD)) = h^0(\omega_S(-mD))$$이며, $$m \gg 0$$일 때

$$(K_S - mD) \cdot H_n = K_S \cdot H_n - m(D \cdot H_n) = K_S \cdot H_n - mD^2 < 0$$

이 된다. 그런데 우리는 $$H_n$$을 very ample이도록 잡았으므로, 이 부등식은 $$K_S-mD$$가 effective divisor가 아니라는 것을 보여준다. 즉 $$h^0(\omega_S(-mD)) = 0$$이다. 이제 $$\rchi(\mathcal{O}(mD)) = h^0(\mathcal{O}(mD)) - h^1(\mathcal{O}(mD)) + h^2(\mathcal{O}(mD))$$에서 $$h^2 = 0$$이므로, $$m \gg 0$$에서 

$$h^0(\mathcal{O}(mD)) \geq \rchi(\mathcal{O}(mD))$$

이다. 그런데 [명제 4](#prop4)에 의해

$$\rchi(\mathcal{O}(mD)) = \rchi(\mathcal{O}_S) + \frac{m^2 D^2 - m D \cdot K_S}{2}$$

이고, 우리는 $$D^2 > 0$$이라 가정하고 있으므로 $$\lvert m\rvert$$이 커질 때 $$\rchi(\mathcal{O}(mD))$$ 또한 무한히 커진다는 것을 안다. 즉 충분히 큰 $$m > 0$$에 대해 $$mD$$가 effective divisor가 되고, 그럼 위의 논의에 의해 $$mD \cdot H > 0$$이다. 그러나 이는 $$D \cdot H = 0$$에 모순이고, 따라서 $$D^2 \leq 0$$이다.

이제 $$D^2\neq 0$$임을 보여 증명을 마무리하자. 결론에 반하여 $$D^2 = 0$$이고 $$D \cdot H = 0$$이며 $$D \not\equiv 0$$이라 하면, $$D \not\equiv 0$$이므로 $$D \cdot E \ne 0$$인 어떤 divisor $$E$$가 존재한다. 이제

$$E' = (H^2)\,E - (E \cdot H)\,H$$

로 정의하면 $$E' \cdot H = (H^2)(E \cdot H) - (E \cdot H)(H^2) = 0$$이고,  $$D \cdot H = 0$$이므로

$$D \cdot E' = (H^2)(D \cdot E) - (E \cdot H)(D \cdot H) = (H^2)(D \cdot E) \ne 0$$

이다. 이제 앞선 논증과 비슷하게 $$F_n := nD + E'$$이라 하면 $$F_n \cdot H = n(D \cdot H) + (E' \cdot H) = 0$$이고

$$F_n^2 = n^2 D^2 + 2n(D \cdot E') + E'^2 = 2n(D \cdot E') + E'^2$$

이다. 그럼 $$D \cdot E' \ne 0$$이므로 $$n$$의 부호를 적절히 택하고 $$\lvert n \rvert$$을 키워주면 $$F_n^2 > 0$$이도록 할 수 있다. 그러나 $$F_n \cdot H = 0$$이므로, 앞선 논증을 $$D=F_n$$에 적용하면 $$F_n^2 \le 0$$이어야 하므로 모순이다. 

</details>

그럼 이로부터 다음의 따름정리를 얻는다.

<div class="proposition" markdown="1">

<ins id="cor11">**따름정리 11**</ins> $$\Num(S) \otimes \mathbb{R}$$ 위의 intersection form은 signature $$(1, \rho - 1)$$를 갖는다. 

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Ample divisor $$H$$에 대해 $$H^2 > 0$$이므로 intersection form은 적어도 하나의 positive direction을 갖는다. 그런데 [명제 10](#prop10)에 의해 $$H$$에 orthogonal인 모든 nonzero 방향은 음의 self-intersection을 가지므로 증명이 완료된다. 

</details>

즉, surface 위의 "양수" 방향은 본질적으로 하나뿐이며, 다른 모든 방향은 어떤 의미에서 "음수"로 생각할 수 있다. 이 결과는 surface의 birational geometry에서 minimal model의 유일성과 같은 깊은 결과들을 이끌어낸다.

## Plurigenera

Curve의 경우, genus $$g$$는 curve의 birational equivalence class를 완전히 결정한다. Surface에서는 상황이 더 복잡한데, 그 이유는 birational equivalence가 cohomology의 차원을 모두 보존하지 않기 때문이다. 그러나 canonical bundle의 tensor power의 global section 차원은 birational invariant이며, 이 값들이 surface의 birational type에 대한 필수적인 정보를 제공한다.

<div class="definition" markdown="1">

<ins id="def12">**정의 12**</ins> Surface $$S$$의 *$$m$$-th plurigenus*는

$$P_m(S) = h^0(S, \omega_S^{\otimes m})$$

이다. 

</div>

여기서 $$\omega_S$$는 ([§표준선다발, ⁋정의 5](/ko/math/algebraic_varieties/canonical_bundle#def5))에서 정의한 canonical bundle이다. 특히 $$m = 1$$인 경우 $$P_1(S) = h^0(\omega_S) = p_g(S)$$는 geometric genus이며, plurigenus들의 열 $$\{P_m(S)\}_{m \ge 1}$$은 어떤 의미에서 이것을 확장한 것이라 할 수 있다. 이는 surface의 birational equivalence class를 결정하는 중요한 불변량이다.

다음 글에서는 Kodaira vanishing theorem을 다루며, 이 정리가 plurigenera의 계산과 surface의 classification에 어떻게 활용되는지 살펴 본다.

---

**참고문헌**

**[Hart]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[BHPV]** W. Barth, K. Hulek, C. Peters, A. Van de Ven, *Compact Complex Surfaces*, Springer, 2004.  
**[Huyb]** D. Huybrechts, *Lectures on K3 Surfaces*, Cambridge University Press, 2016.