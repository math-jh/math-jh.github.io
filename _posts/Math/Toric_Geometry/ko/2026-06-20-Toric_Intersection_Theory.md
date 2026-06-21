---
title: "토릭 다양체의 교차 이론"
description: "매끄러운 완비 토릭 다양체의 Chow 환을 팬의 조합론으로부터 기술한다. Cone과 orbit closure의 대응, torus-invariant divisor들의 교차수를 팬과 polytope에서 읽어내는 방법, 그리고 linear relation과 Stanley-Reisner relation으로 주어지는 Chow 환의 표현을 다룬다."
excerpt: "Fan의 조합론으로 읽어내는 매끄러운 완비 토릭 다양체의 Chow 환과 교차수"

categories: [Math / Toric Geometry]
permalink: /ko/math/toric_geometry/toric_intersection_theory

sidebar:
    nav: "toric_geometry-ko"

date: 2026-06-20
weight: 7
published: false
---

[\[대수다양체\] §교차곱, ⁋정의 7](/ko/math/algebraic_varieties/intersection_product#def7)에서 우리는 smooth variety $$X$$의 Chow group들 $$\CH^\ast(X) = \bigoplus_k \CH^k(X)$$이 intersection product에 의해 graded ring을 이룸을 보았고, 이를 Chow ring이라 불렀다. 일반적인 variety에서 Chow ring을 명시적으로 계산하는 일은 대단히 어렵지만, toric variety의 경우 모든 것이 fan $$\Sigma$$의 조합론으로 환원된다. 이번 글의 목표는 smooth complete toric variety $$X_\Sigma$$에 대해 그 Chow ring을 fan의 데이터로 완전히 기술하고, torus-invariant divisor들의 교차수를 cone과 polytope으로부터 직접 읽어내는 방법을 정리하는 것이다.

이하에서 $$N \cong \mathbb{Z}^n$$은 rank $$n$$의 lattice, $$M = \Hom_\mathbb{Z}(N, \mathbb{Z})$$는 그 dual lattice이며, $$\Sigma$$는 $$N_\mathbb{R}$$ 위의 fan으로 그것이 정의하는 toric variety $$X_\Sigma$$가 smooth complete라고 가정한다. $$\Sigma(d)$$로 $$\Sigma$$의 $$d$$차원 cone들의 모임을, $$\Sigma(1)$$로 ray들의 모임을 적으며, 각 $$\rho \in \Sigma(1)$$에 대해 $$v_\rho \in N$$은 그 primitive generator이다. $$X_\Sigma$$가 smooth이므로 ([§토릭 다양체의 정의, ⁋명제 11](/ko/math/toric_geometry/toric_varieties#prop11)) 모든 cone $$\sigma \in \Sigma$$의 generator들은 lattice $$N$$의 $$\mathbb{Z}$$-basis의 일부를 이룬다 ([§아핀 토릭 다양체, ⁋정의 8](/ko/math/toric_geometry/affine_toric_varieties#def8)).

## Cone과 orbit closure의 대응

[§토릭 다양체의 정의, ⁋명제 5](/ko/math/toric_geometry/toric_varieties#prop5) 직후에 보았듯, $$X_\Sigma$$의 $$T_N$$-action에 의한 orbit들은 fan의 cone들과 일대일 대응한다. 구체적으로 $$d$$차원 cone $$\sigma \in \Sigma(d)$$에 대응하는 orbit $$O(\sigma)$$는 차원 $$n - d$$의 torus $$(\mathbb{C}^\ast)^{n-d}$$와 isomorphic하다. Chow ring을 다루기 위해서는 이 orbit이 아니라 그 Zariski closure가 필요하다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Cone $$\sigma \in \Sigma$$에 대해, orbit $$O(\sigma)$$의 Zariski closure를 *orbit closure<sub>궤도 폐포</sub>* $$V(\sigma)$$라 적는다. 즉

$$V(\sigma) = \overline{O(\sigma)} \subseteq X_\Sigma$$

이다.

</div>

$$O(\sigma)$$의 차원이 $$n - d$$이므로 $$V(\sigma)$$는 codimension $$d$$의 irreducible closed subvariety이며, 따라서 cycle class $$[V(\sigma)] \in \CH^d(X_\Sigma)$$을 정의한다 ([\[대수다양체\] §저우 군, ⁋정의 5](/ko/math/algebraic_varieties/chow_groups#def5)). 두 극단적인 경우가 익숙하다. $$d = 0$$일 때, 즉 $$\sigma = \{0\}$$일 때 $$V(\{0\}) = X_\Sigma$$ 전체이며 이는 $$\CH^0(X_\Sigma)$$의 fundamental class이다. $$d = 1$$일 때, 즉 ray $$\rho \in \Sigma(1)$$에 대해 $$V(\rho)$$는 codimension $$1$$의 irreducible subvariety, 즉 [§토러스 인자와 선다발, ⁋정의 1](/ko/math/toric_geometry/toric_divisors#def1)의 torus-invariant prime divisor $$D_\rho$$와 정확히 일치한다. 우리는 이하에서 $$V(\rho) = D_\rho$$로 두고 이 두 표기를 자유로이 혼용한다.

반대편 극단으로, $$X_\Sigma$$가 complete이고 $$\sigma$$가 maximal cone, 즉 $$\dim \sigma = n$$이면 $$O(\sigma)$$는 $$0$$차원 orbit, 즉 $$T_N$$의 fixed point이며 $$V(\sigma)$$는 그 한 점이다. 이는 $$\CH^n(X_\Sigma)$$의 class를 준다.

Orbit closure $$V(\sigma)$$ 자체도 toric variety의 구조를 갖는다. 더 정확히는, $$\sigma$$를 포함하는 cone들이 quotient lattice $$N(\sigma) = N / (N \cap \mathbb{R}\sigma)$$ 안에서 *star* $$\operatorname{Star}(\sigma)$$라 불리는 fan을 이루고, $$V(\sigma)$$는 이 fan이 정의하는 toric variety와 동형이다. 이 사실은 orbit closure 사이의 교차를 다시 더 작은 toric variety 위의 문제로 환원해 주며, 아래 교차수 계산의 바탕이 된다.

## Linear relation과 Stanley-Reisner relation

이제 우리는 ray들이 주는 divisor class $$[D_\rho] \in \CH^1(X_\Sigma)$$들이 Chow ring 전체를 generate한다는 사실과, 그들 사이에 성립하는 관계를 기술한다. 두 종류의 관계가 있다. 하나는 [§토러스 인자와 선다발, ⁋명제 3](/ko/math/toric_geometry/toric_divisors#prop3)의 character divisor로부터 오는 *linear* relation이고, 다른 하나는 cone을 이루지 않는 ray들의 곱이 사라진다는 *Stanley-Reisner* relation이다.

먼저 linear relation을 본다. [§토러스 인자와 선다발, ⁋명제 3](/ko/math/toric_geometry/toric_divisors#prop3)에 의해 임의의 $$m \in M$$에 대해 character $$\rchi^m$$의 divisor는

$$\divisor(\rchi^m) = \sum_{\rho \in \Sigma(1)} \langle m, v_\rho \rangle D_\rho$$

이며, 이는 principal divisor이므로 $$\CH^1(X_\Sigma) \cong \Cl(X_\Sigma)$$ ([\[대수다양체\] §저우 군, ⁋명제 11](/ko/math/algebraic_varieties/chow_groups#prop11)) 안에서 $$0$$이 된다. 따라서 각 $$m \in M$$은 divisor class 사이의 선형 관계

$$\sum_{\rho \in \Sigma(1)} \langle m, v_\rho \rangle [D_\rho] = 0$$

을 준다. $$M$$이 $$\{e_1^\ast, \ldots, e_n^\ast\}$$로 generate되므로 $$n$$개의 독립적인 관계가 얻어진다.

다음으로 Stanley-Reisner relation을 본다. 이는 본질적으로 ray들의 곱 $$D_{\rho_1} \cdots D_{\rho_k}$$가 그 ray들이 함께 하나의 cone을 이룰 때만 비자명하다는 사실이다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> 서로 다른 ray들 $$\rho_1, \ldots, \rho_k \in \Sigma(1)$$에 대해 다음이 성립한다.

1. 만일 $$\rho_1, \ldots, \rho_k$$가 함께 하나의 cone $$\sigma = \rho_1 + \cdots + \rho_k \in \Sigma$$를 이루면, $$X_\Sigma$$가 smooth라는 가정 하에 $$\CH^\ast(X_\Sigma)$$ 안에서

    $$[D_{\rho_1}] \cdots [D_{\rho_k}] = [V(\sigma)]$$

    이 성립한다.
2. 만일 $$\rho_1, \ldots, \rho_k$$가 $$\Sigma$$의 어떤 cone도 이루지 않으면

    $$[D_{\rho_1}] \cdots [D_{\rho_k}] = 0$$

    이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

(1) 먼저 $$k = 2$$인 경우를 보고 귀납적으로 일반화한다. 두 ray $$\rho_1, \rho_2$$가 $$2$$차원 cone $$\tau = \rho_1 + \rho_2 \in \Sigma$$를 이룬다고 하자. $$X_\Sigma$$가 smooth이므로 $$v_{\rho_1}, v_{\rho_2}$$는 $$N$$의 $$\mathbb{Z}$$-basis의 일부를 이루며, 두 divisor $$D_{\rho_1}, D_{\rho_2}$$는 affine chart $$U_\tau \cong \mathbb{C}^n$$ 위에서 서로 다른 두 좌표 hyperplane으로 나타난다. 이 두 hyperplane은 transverse하게 만나므로 그 교차는 정확히 codimension $$2$$의 부분다양체 $$V(\tau)$$이고, 교차 중복도는 $$1$$이다 ([\[대수다양체\] §교차곱, ⁋명제 4](/ko/math/algebraic_varieties/intersection_product#prop4)). 따라서 $$[D_{\rho_1}] \cdot [D_{\rho_2}] = [V(\tau)]$$이다.

이제 $$\sigma = \rho_1 + \cdots + \rho_k$$가 smooth cone이라 하자. Affine chart $$U_\sigma \cong \mathbb{C}^n$$ 위에서 $$v_{\rho_1}, \ldots, v_{\rho_k}$$는 $$N$$의 basis $$v_{\rho_1}, \ldots, v_{\rho_n}$$로 확장되며, 각 $$D_{\rho_i}$$는 이에 dual인 좌표 $$\rchi^{v_{\rho_i}^\ast}$$의 zero locus, 즉 한 좌표 hyperplane으로 나타난다. 서로 다른 $$k$$개의 좌표 hyperplane들은 transverse하게 만나 codimension $$k$$의 좌표 부분공간 $$V(\sigma)$$를 이루고, 그 교차 중복도는 모두 $$1$$이다. Chow ring의 결합성 ([\[대수다양체\] §교차곱, ⁋명제 6](/ko/math/algebraic_varieties/intersection_product#prop6))과 위 $$k=2$$ 계산을 반복 적용하면

$$[D_{\rho_1}] \cdots [D_{\rho_k}] = [V(\sigma)]$$

을 얻는다.

(2) $$\rho_1, \ldots, \rho_k$$가 $$\Sigma$$의 어떤 cone도 이루지 않는다고 하자. 그러면 어떤 maximal cone도 이들 ray를 모두 포함하지 못한다. Divisor $$D_{\rho_i}$$의 support는 정확히 ray $$\rho_i$$를 포함하는 cone들에 대응하는 orbit들의 합집합이므로, 교집합 $$\bigcap_i \operatorname{Supp} D_{\rho_i}$$는 $$\rho_1, \ldots, \rho_k$$를 모두 면으로 갖는 cone에 대응하는 orbit들로 이루어진다. 그러한 cone이 $$\Sigma$$에 존재하지 않으므로 이 교집합은 공집합이다. 한편 [\[대수다양체\] §교차곱, ⁋보조정리 8](/ko/math/algebraic_varieties/intersection_product#lem8)의 moving lemma에 의해 $$[D_{\rho_1}] \cdots [D_{\rho_k}]$$는 generic하게 transverse한 대표원으로 계산할 수 있는데, 각 $$D_{\rho_i}$$는 $$\divisor(\rchi^{m_i})$$만큼 이동시켜도 같은 class를 주므로 ($$m_i \in M$$), 적절한 character 이동으로 얻은 대표원들의 교집합 또한 비어 있게 만들 수 있다. 따라서 곱은 $$0$$이다.

</details>

명제 2의 (2)가 *Stanley-Reisner relation*이다. Fan $$\Sigma$$의 ray 집합 $$\Sigma(1)$$ 위에서, "함께 하나의 cone을 이루는 ray들의 부분집합"을 face라 부르면 $$\Sigma$$는 추상적인 simplicial complex의 구조를 가지며, cone을 이루지 않는 부분집합 $$\{\rho_{i_1}, \ldots, \rho_{i_k}\}$$을 *non-face*라 부른다. 명제 2의 (2)는 정확히 모든 non-face에 대응하는 monomial $$\x_{\rho_{i_1}} \cdots \x_{\rho_{i_k}}$$이 사라진다는 진술이다. 이 두 종류의 관계가 Chow ring을 완전히 결정한다는 것이 다음 절의 주제이다.

<div class="remark" markdown="1">

<ins id="rmk3">**참고 3**</ins> 명제 2의 (1)에서 우리는 $$X_\Sigma$$의 smoothness를 본질적으로 사용했다. $$X_\Sigma$$가 smooth가 아니라 simplicial일 뿐인 일반적 경우에는 우변에 cone의 *multiplicity* $$\operatorname{mult}(\sigma) = [N_\sigma : \mathbb{Z}v_{\rho_1} + \cdots + \mathbb{Z}v_{\rho_k}]$$가 곱해져

$$[D_{\rho_1}] \cdots [D_{\rho_k}] = \frac{1}{\operatorname{mult}(\sigma)}\,[V(\sigma)], \qquad [V(\sigma)] = \operatorname{mult}(\sigma)\,[D_{\rho_1}] \cdots [D_{\rho_k}]$$

의 꼴로 나타난다 ([CLS] Proposition 12.5.2). 여기서 $$N_\sigma = N \cap \mathbb{R}\sigma$$는 $$\sigma$$가 span하는 부분공간 안의 lattice이다. Smooth cone은 그 generator가 $$N_\sigma$$의 basis를 이루어 $$\mult(\sigma) = 1$$이므로, 위 식은 명제 2의 (1)로 환원된다. Simplicial이지만 smooth가 아닌 경우 Chow group이 torsion을 가질 수 있어 위 식은 $$\CH^\ast(X_\Sigma)_\mathbb{Q}$$ 위에서만 성립한다.

</div>

## Chow 환의 표현

이제 위의 관찰을 하나의 ring isomorphism으로 묶는다. 각 ray $$\rho \in \Sigma(1)$$에 변수 $$\x_\rho$$를 대응시킨 polynomial ring을 생각하면 (이는 [§Cox 구성과 GIT quotient, ⁋정의 7](/ko/math/toric_geometry/cox_construction#def7)의 Cox ring과 같은 변수 집합이다), divisor class $$[D_\rho]$$들이 $$\x_\rho$$의 상이 되도록 하는 surjection을 만들 수 있고, 그 kernel이 정확히 linear relation과 Stanley-Reisner relation으로 generate된다.

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> Fan $$\Sigma$$에 대해 polynomial ring $$\mathbb{Z}[\x_\rho \mid \rho \in \Sigma(1)]$$ 안에서 다음 두 ideal을 정의한다.

1. *Stanley-Reisner ideal<sub>스탠리-라이스너 아이디얼</sub>* $$\mathcal{I}_{SR}$$은 $$\Sigma$$의 non-face들이 주는 monomial

    $$\x_{\rho_{i_1}} \cdots \x_{\rho_{i_k}}, \qquad \{\rho_{i_1}, \ldots, \rho_{i_k}\} \text{ does not span a cone of } \Sigma$$

    들이 생성하는 ideal이다.
2. *linear ideal<sub>선형 아이디얼</sub>* $$\mathcal{J}_{\mathrm{lin}}$$은 $$m$$이 $$M$$ 위를 움직일 때의 선형형식

    $$\sum_{\rho \in \Sigma(1)} \langle m, v_\rho \rangle\, \x_\rho, \qquad m \in M$$

    들이 생성하는 ideal이다.

</div>

$$\mathcal{I}_{SR}$$은 모든 non-face에 대응하는 monomial을 다 모을 필요 없이, 그 중 *minimal*한 non-face들에 대응하는 monomial만 generator로 취하면 충분하다. $$\mathcal{J}_{\mathrm{lin}}$$은 $$M$$의 basis $$e_1^\ast, \ldots, e_n^\ast$$가 주는 $$n$$개의 선형형식으로 generate된다. 이 둘의 합을 quotient하면 Chow ring이 나온다.

<div class="proposition" markdown="1">

<ins id="thm5">**정리 5 (Chow ring의 조합론적 표현)**</ins> $$X_\Sigma$$가 smooth complete toric variety이면, $$\x_\rho \mapsto [D_\rho]$$로 정의되는 사상은 graded ring의 isomorphism

$$\CH^\ast(X_\Sigma) \cong \mathbb{Z}[\x_\rho \mid \rho \in \Sigma(1)] \,/\, (\mathcal{I}_{SR} + \mathcal{J}_{\mathrm{lin}})$$

을 유도한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

표기를 위해 $$R = \mathbb{Z}[\x_\rho \mid \rho \in \Sigma(1)]$$이라 두자. $$\x_\rho \mapsto [D_\rho]$$는 ring homomorphism $$\varphi: R \to \CH^\ast(X_\Sigma)$$로 유일하게 확장된다. 우리는 $$\varphi$$가 surjective이고 $$\ker \varphi = \mathcal{I}_{SR} + \mathcal{J}_{\mathrm{lin}}$$임을 보인다.

$$\varphi$$가 $$\mathcal{I}_{SR}$$과 $$\mathcal{J}_{\mathrm{lin}}$$을 모두 $$0$$으로 보냄은 이미 보았다. 즉 $$\mathcal{J}_{\mathrm{lin}}$$의 generator는 $$\varphi$$ 하에서 $$\sum_\rho \langle m, v_\rho\rangle [D_\rho] = [\divisor(\rchi^m)] = 0$$이 되고 ([§토러스 인자와 선다발, ⁋명제 3](/ko/math/toric_geometry/toric_divisors#prop3)), $$\mathcal{I}_{SR}$$의 generator는 명제 2의 (2)에 의해 $$0$$이 된다. 따라서 $$\varphi$$는 quotient ring $$\overline{\varphi}: R/(\mathcal{I}_{SR} + \mathcal{J}_{\mathrm{lin}}) \to \CH^\ast(X_\Sigma)$$로 factor된다.

다음으로 $$\overline{\varphi}$$의 surjectivity를 본다. $$X_\Sigma$$가 smooth이므로 Chow group은 orbit closure들로 generate된다. 구체적으로, complete toric variety에 대해 cycle class들 $$\{[V(\sigma)] : \sigma \in \Sigma\}$$이 $$\CH^\ast(X_\Sigma)$$를 $$\mathbb{Z}$$-module로서 generate한다. 이는 fan의 cone들이 주는 affine cell들에 의한 stratification과 localization exact sequence ([\[대수다양체\] §저우 군, ⁋명제 8](/ko/math/algebraic_varieties/chow_groups#prop8))를 cone 차원에 대해 귀납적으로 적용하여 얻어진다. 각 $$[V(\sigma)]$$는 명제 2의 (1)에 의해 $$\sigma$$를 generate하는 ray들의 divisor 곱 $$[D_{\rho_1}] \cdots [D_{\rho_k}]$$로 표현되므로 $$[D_\rho]$$들의 monomial이며, 따라서 $$\varphi$$의 image에 속한다. 결국 $$\overline{\varphi}$$는 surjective이다.

마지막으로 injectivity를 본다. 이를 직접 보이는 대신, $$X_\Sigma$$가 smooth complete일 때 두 graded abelian group이 각 차수에서 같은 유한 rank를 가짐을 이용한다. $$X_\Sigma$$가 smooth complete이면 maximal cone들이 주는 affine cell에 의한 cellular decomposition이 존재하여 $$\CH^k(X_\Sigma)$$는 free abelian group이며 그 차수별 rank는 fan의 $$h$$-vector로 주어진다. 한편 quotient $$R/(\mathcal{I}_{SR} + \mathcal{J}_{\mathrm{lin}})$$의 차수별 rank도 동일한 $$h$$-vector로 계산됨이 알려져 있다 ([Sta] 또는 [CLS] Theorem 12.4.4). 두 graded group이 surjection $$\overline{\varphi}$$로 연결되어 있고 각 차수에서 같은 유한 rank를 가지므로, free abelian group 사이의 차수별 surjection이 rank를 보존하면 isomorphism이라는 사실로부터 $$\overline{\varphi}$$는 isomorphism이다.

</details>

정리 5는 smooth complete toric variety의 Chow ring을 fan으로부터 완전히 기계적으로 계산하게 해 준다. 변수는 ray의 개수 $$\lvert \Sigma(1) \rvert$$만큼이고, linear ideal이 $$n$$개의 변수를 소거하므로 $$\CH^1(X_\Sigma) \cong \Cl(X_\Sigma)$$의 rank가 $$\lvert \Sigma(1) \rvert - n$$이 되는 것은 [§토러스 인자와 선다발, ⁋명제 4](/ko/math/toric_geometry/toric_divisors#prop4)의 exact sequence와 부합한다.

<div class="remark" markdown="1">

<ins id="rmk6">**참고 6**</ins> 정리 5의 표현은 $$X_\Sigma$$가 smooth complete일 때 위상적 cohomology ring $$H^\ast(X_\Sigma, \mathbb{Z})$$의 표현과도 일치한다. Smooth complete toric variety는 odd cohomology가 사라지고 cycle class map ([\[대수다양체\] §저우 군, ⁋명제 12](/ko/math/algebraic_varieties/chow_groups#prop12))이 isomorphism $$\CH^k(X_\Sigma) \cong H^{2k}(X_\Sigma, \mathbb{Z})$$을 주기 때문이다. 따라서 위 ideal 표현은 Danilov와 Jurkiewicz에 의한 toric variety의 cohomology ring 계산으로도 알려져 있다.

</div>

## 교차수와 polytope

Chow ring을 알면 $$0$$차원 class까지 곱을 내려보내 *교차수*를 얻을 수 있다. $$X_\Sigma$$가 complete이므로 $$\CH^n(X_\Sigma) \cong \mathbb{Z}$$이며, 한 점의 class $$[\mathrm{pt}]$$가 generator이다. Codimension의 합이 $$n$$인 divisor들의 곱은 $$\CH^n(X_\Sigma)$$의 원소, 즉 정수배의 점이 되고, 그 정수를 교차수라 부른다. Smooth case에서 이 교차수는 maximal cone의 조합론으로 직접 읽힌다.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> $$X_\Sigma$$가 smooth complete toric variety이고 $$\rho_1, \ldots, \rho_n \in \Sigma(1)$$이 서로 다른 ray라 하자. 그러면 교차수 $$D_{\rho_1} \cdots D_{\rho_n} \in \CH^n(X_\Sigma) \cong \mathbb{Z}$$는 다음과 같다.

$$D_{\rho_1} \cdots D_{\rho_n} = \begin{cases} 1 & \text{if } \rho_1 + \cdots + \rho_n \in \Sigma(n), \\ 0 & \text{otherwise.} \end{cases}$$

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

만일 $$\rho_1, \ldots, \rho_n$$이 함께 cone을 이루지 않으면 명제 2의 (2)에 의해 곱이 $$0$$이다. 함께 cone을 이루는 경우, 그 cone $$\sigma = \rho_1 + \cdots + \rho_n$$은 $$n$$차원이므로 maximal cone이고, 명제 2의 (1)에 의해

$$D_{\rho_1} \cdots D_{\rho_n} = [V(\sigma)]$$

이다. $$\sigma$$가 maximal cone이고 $$X_\Sigma$$가 complete이므로 $$V(\sigma)$$는 $$T_N$$의 fixed point 하나, 즉 한 점이다. 따라서 $$[V(\sigma)] = [\mathrm{pt}]$$이고 교차수는 $$1$$이다. (Smoothness에 의해 $$\operatorname{mult}(\sigma) = 1$$이므로 참고 3의 일반 공식에서도 같은 값을 얻는다.)

</details>

명제 7은 smooth complete toric variety의 모든 top-degree 교차수를 maximal cone의 목록으로부터 즉시 읽게 해 준다. 같은 ray가 중복되어 나타나는 self-intersection $$D_{\rho_1}^{a_1} \cdots D_{\rho_s}^{a_s}$$ ($$\sum a_i = n$$)의 경우에는 명제 7만으로는 부족하고 linear relation을 사용하여 중복된 ray를 다른 ray들로 바꿔 써야 한다. 아래 예시들에서 이 계산을 구체적으로 수행한다.

한편 $$D_\rho$$들이 nef인 ample divisor를 이룰 때에는 교차수가 대응 polytope의 부피로 해석된다. [§토러스 인자와 선다발, ⁋명제 9](/ko/math/toric_geometry/toric_divisors#prop9)에서 보았듯 ample torus-invariant divisor $$D = \sum_\rho a_\rho D_\rho$$는 strictly convex piecewise linear function $$\psi_D$$를 통해 lattice polytope

$$P_D = \{m \in M_\mathbb{R} \mid \langle m, v_\rho \rangle \ge -a_\rho \text{ for all } \rho \in \Sigma(1)\}$$

을 결정한다. 이 때 $$D$$의 $$n$$중 self-intersection은 polytope의 normalized volume이 된다.

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> $$X_\Sigma$$가 $$n$$차원 smooth complete toric variety이고 $$D$$가 ample torus-invariant divisor라 하자. 그러면

$$D^n = n!\, \vol(P_D)$$

이 성립한다. 여기서 $$\vol(P_D)$$는 lattice $$M$$에 대한 Euclidean volume, 즉 unit lattice cube의 부피를 $$1$$로 정규화한 부피이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

[§토러스 인자와 선다발, ⁋명제 7](/ko/math/toric_geometry/toric_divisors#prop7)에 의해 $$D$$에 대응하는 line bundle $$\mathcal{O}_{X_\Sigma}(D)$$의 global section은 $$P_D \cap M$$의 lattice point들에 대응하는 character $$\rchi^m$$들로 basis를 이루므로

$$\dim_\mathbb{C} H^0(X_\Sigma, \mathcal{O}_{X_\Sigma}(kD)) = \#(kP_D \cap M)$$

이다. $$D$$가 ample이므로 충분히 큰 $$k$$에 대해 고차 cohomology가 사라지고, 따라서 좌변은 Euler characteristic $$\chi(\mathcal{O}_{X_\Sigma}(kD))$$와 같다. Asymptotic Riemann-Roch에 의해 이 Euler characteristic은 $$k$$에 대한 차수 $$n$$의 다항식이며 그 최고차항은

$$\chi(\mathcal{O}_{X_\Sigma}(kD)) = \frac{D^n}{n!}\, k^n + O(k^{n-1})$$

이다. 한편 lattice point의 개수 $$\#(kP_D \cap M)$$는 Ehrhart 다항식으로, 그 최고차항은 $$\vol(P_D)\, k^n$$이다. 두 다항식의 최고차항을 비교하면 $$D^n / n! = \vol(P_D)$$, 즉 $$D^n = n!\, \vol(P_D)$$를 얻는다.

</details>

이 결과는 toric variety의 교차 이론과 볼록 기하의 격자점 셈을 잇는 다리이다. 가장 단순한 예로 $$\mathbb{P}^n$$의 hyperplane class $$H$$는 $$P_H$$가 standard simplex $$\Delta_n$$이 되어 $$H^n = n!\, \vol(\Delta_n) = n! \cdot \frac{1}{n!} = 1$$을 주며, 이는 $$\CH^\ast(\mathbb{P}^n) = \mathbb{Z}[H]/(H^{n+1})$$에서 $$H^n = [\mathrm{pt}]$$인 것과 일치한다 ([\[대수다양체\] §교차곱, ⁋예시 10](/ko/math/algebraic_varieties/intersection_product#ex10)).

## 사영공간

이제 위 도구들을 구체적인 예시에 적용한다. 가장 먼저 $$\mathbb{P}^n$$을 본다.

<div class="example" markdown="1">

<ins id="ex9">**예시 9 ($$\mathbb{P}^n$$)**</ins> [§토릭 다양체의 정의, ⁋예시 10](/ko/math/toric_geometry/toric_varieties#ex10)에서 보았듯 $$\mathbb{P}^n$$의 fan은 $$n+1$$개의 ray $$\rho_0, \ldots, \rho_n$$을 가지며 그 primitive generator는

$$v_i = e_i \ (1 \le i \le n), \qquad v_0 = -e_1 - \cdots - e_n$$

이고, maximal cone들은 이들 중 하나를 뺀 $$n$$개로 생성되는 $$n$$차원 cone들이다. 따라서 $$n+1$$개 ray 전체의 임의의 $$n$$개 부분집합은 항상 하나의 maximal cone을 이루며, $$n+1$$개 ray 전체 $$\{\rho_0, \ldots, \rho_n\}$$만이 유일한 minimal non-face이다. 그러므로

$$\mathcal{I}_{SR} = (\x_0 \x_1 \cdots \x_n)$$

이다. Linear relation은 각 $$m = e_j^\ast$$에 대해 $$\sum_i \langle e_j^\ast, v_i \rangle \x_i = \x_j - \x_0 = 0$$, 즉 $$\x_j = \x_0$$ ($$1 \le j \le n$$)을 준다. 따라서 정리 5에 의해

$$\CH^\ast(\mathbb{P}^n) \cong \mathbb{Z}[\x_0, \ldots, \x_n] / (\x_0 \cdots \x_n,\ \x_1 - \x_0,\ \ldots,\ \x_n - \x_0)$$

이며, 모든 $$\x_i$$를 $$H := \x_0$$로 동일시하면 유일한 Stanley-Reisner 관계가 $$H^{n+1} = 0$$이 되어

$$\CH^\ast(\mathbb{P}^n) \cong \mathbb{Z}[H] / (H^{n+1})$$

을 회복한다. 이는 [\[대수다양체\] §교차곱, ⁋예시 10](/ko/math/algebraic_varieties/intersection_product#ex10)의 결과와 정확히 일치한다. 교차수의 관점에서, 명제 7에 의해 서로 다른 $$n$$개의 $$D_i$$의 곱은 그들이 maximal cone을 이루므로 항상 $$1$$이고, 가령 $$D_1 \cdots D_n = [\mathrm{pt}]$$이다. 한편 $$H^n = D_0^n$$은 linear relation으로 $$D_0 = D_1 = \cdots$$이 되므로 $$D_0^n = D_1 D_2 \cdots D_n = 1$$로 계산되어 같은 답을 준다.

</div>

## 사영선의 곱

다음으로 가장 단순한 비자명 곱공간 $$\mathbb{P}^1 \times \mathbb{P}^1$$을 본다. 여기서는 Picard rank가 $$2$$이고, Chow ring이 두 개의 독립적인 hyperplane class로 generate된다.

<div class="example" markdown="1">

<ins id="ex10">**예시 10 ($$\mathbb{P}^1 \times \mathbb{P}^1$$)**</ins> [§Cox 구성과 GIT quotient, ⁋예시 11](/ko/math/toric_geometry/cox_construction#ex11)에서 보았듯 $$\mathbb{P}^1 \times \mathbb{P}^1$$의 fan은 $$N = \mathbb{Z}^2$$에서 $$4$$개의 ray

$$v_1 = (1, 0), \quad v_2 = (0, 1), \quad v_3 = (-1, 0), \quad v_4 = (0, -1)$$

을 가지며, maximal cone은 인접한 두 ray로 생성되는 $$4$$개

$$\sigma_{12} = \rho_1 + \rho_2, \quad \sigma_{23} = \rho_2 + \rho_3, \quad \sigma_{34} = \rho_3 + \rho_4, \quad \sigma_{41} = \rho_4 + \rho_1$$

이다. 마주보는 두 ray $$\{\rho_1, \rho_3\}$$과 $$\{\rho_2, \rho_4\}$$는 cone을 이루지 않으므로 이들이 minimal non-face이고, 따라서

$$\mathcal{I}_{SR} = (\x_1 \x_3,\ \x_2 \x_4)$$

이다. Linear relation은 $$m = e_1^\ast$$에 대해 $$\langle e_1^\ast, v_1\rangle \x_1 + \cdots = \x_1 - \x_3 = 0$$, $$m = e_2^\ast$$에 대해 $$\x_2 - \x_4 = 0$$을 주어 $$\x_1 = \x_3$$, $$\x_2 = \x_4$$이다. $$H_1 := \x_1 = \x_3$$, $$H_2 := \x_2 = \x_4$$로 두면 Stanley-Reisner 관계는 $$H_1^2 = 0$$, $$H_2^2 = 0$$이 되어

$$\CH^\ast(\mathbb{P}^1 \times \mathbb{P}^1) \cong \mathbb{Z}[H_1, H_2] / (H_1^2,\ H_2^2)$$

을 얻는다. 이는 [\[대수다양체\] §교차곱, ⁋예시 12](/ko/math/algebraic_varieties/intersection_product#ex12)의 결과와 일치한다. 교차수를 직접 확인하면, $$\rho_1, \rho_2$$는 maximal cone $$\sigma_{12}$$를 이루므로 명제 7에 의해 $$D_1 D_2 = H_1 H_2 = 1 = [\mathrm{pt}]$$이고, $$\rho_1, \rho_3$$은 cone을 이루지 않으므로 $$D_1 D_3 = H_1^2 = 0$$이다. 따라서 두 곡선 $$C = aH_1 + bH_2$$, $$C' = a'H_1 + b'H_2$$의 교차수는

$$C \cdot C' = (aH_1 + bH_2)(a'H_1 + b'H_2) = (ab' + a'b)\, H_1 H_2 = ab' + a'b$$

이다.

이를 polytope 부피로도 확인할 수 있다. Ample divisor $$D = H_1 + H_2$$에 대응하는 polytope $$P_D$$는 정사각형 $$[0,1] \times [0,1]$$로 그 정규화 부피가 $$1$$이며, 명제 8에 의해 $$D^2 = 2!\cdot 1 = 2$$이다. 한편 Chow ring에서 $$D^2 = (H_1 + H_2)^2 = H_1^2 + 2 H_1 H_2 + H_2^2 = 2 H_1 H_2 = 2$$로 같은 값을 얻는다.

</div>

## 토릭 blow-up

마지막으로, smooth complete toric variety의 가장 기본적인 birational 변형인 점에서의 blow-up이 교차 이론에서 어떻게 나타나는지를 본다. [§토릭 다양체의 정의, ⁋명제 11](/ko/math/toric_geometry/toric_varieties#prop11) 직후에 보았듯 fan의 refinement는 toric morphism을 주며, 그 중 *star subdivision*은 정확히 torus-fixed point에서의 blow-up에 대응한다. $$\mathbb{P}^2$$의 한 fixed point를 blow-up하는 경우를 구체적으로 계산한다.

<div class="example" markdown="1">

<ins id="ex11">**예시 11 ($$\mathbb{P}^2$$의 점에서의 blow-up)**</ins> $$\mathbb{P}^2$$의 fan은 $$N = \mathbb{Z}^2$$에서 ray

$$v_1 = e_1, \quad v_2 = e_2, \quad v_0 = -e_1 - e_2$$

와 maximal cone $$\sigma_{01} = \rho_0 + \rho_1$$, $$\sigma_{12} = \rho_1 + \rho_2$$, $$\sigma_{02} = \rho_0 + \rho_2$$를 갖는다. Cone $$\sigma_{12} = \mathrm{cone}(e_1, e_2)$$에 대응하는 fixed point에서 blow-up을 하려면, 이 cone을 그 안의 새 ray

$$v_3 = e_1 + e_2$$

로 *star subdivision*한다. 즉 $$\sigma_{12}$$를 두 cone $$\rho_1 + \rho_3 = \mathrm{cone}(e_1, e_1 + e_2)$$와 $$\rho_2 + \rho_3 = \mathrm{cone}(e_2, e_1 + e_2)$$로 쪼갠다. 결과 fan $$\Sigma'$$은 $$4$$개의 ray $$\rho_0, \rho_1, \rho_2, \rho_3$$과 $$4$$개의 maximal cone

$$\sigma_{01} = \rho_0 + \rho_1, \quad \sigma_{02} = \rho_0 + \rho_2, \quad \rho_1 + \rho_3, \quad \rho_2 + \rho_3$$

을 가지며, 각 maximal cone의 두 generator가 $$\mathbb{Z}^2$$의 basis를 이루므로 ($$\det$$가 모두 $$\pm 1$$) $$X_{\Sigma'}$$은 smooth complete이다. 이 $$X_{\Sigma'}$$이 $$\mathbb{P}^2$$를 한 점에서 blow-up한 surface $$\Bl_p \mathbb{P}^2$$이며, 새 ray $$\rho_3$$이 exceptional divisor $$E = D_{\rho_3}$$에 대응한다.

이제 Chow ring을 계산한다. Cone을 이루지 않는 ray 쌍은 $$\{\rho_0, \rho_3\}$$ (원점에서 멀어지는 방향이 정반대), $$\{\rho_1, \rho_2\}$$ (원래 $$\sigma_{12}$$였으나 subdivision으로 직접 cone을 이루지 않게 됨) 두 가지이다. 따라서

$$\mathcal{I}_{SR} = (\x_0 \x_3,\ \x_1 \x_2)$$

이다. Linear relation은 $$m = e_1^\ast$$에 대해

$$\langle e_1^\ast, v_0\rangle \x_0 + \langle e_1^\ast, v_1\rangle \x_1 + \langle e_1^\ast, v_2\rangle \x_2 + \langle e_1^\ast, v_3\rangle \x_3 = -\x_0 + \x_1 + \x_3 = 0,$$

$$m = e_2^\ast$$에 대해 $$-\x_0 + \x_2 + \x_3 = 0$$을 준다. 이로부터 $$\x_1 = \x_0 - \x_3$$, $$\x_2 = \x_0 - \x_3$$이다. 생성원으로 $$H := \x_0$$ (pullback된 hyperplane class)와 $$E := \x_3$$를 택하면 $$\x_1 = \x_2 = H - E$$이고, 두 Stanley-Reisner 관계는

$$\x_0 \x_3 = H E = 0, \qquad \x_1 \x_2 = (H - E)^2 = 0$$

이 된다. 둘째 관계를 전개하면 $$H^2 - 2 HE + E^2 = 0$$인데 $$HE = 0$$이므로 $$H^2 + E^2 = 0$$, 즉 $$E^2 = -H^2$$이다. 따라서

$$\CH^\ast(\Bl_p \mathbb{P}^2) \cong \mathbb{Z}[H, E] / (HE,\ H^2 + E^2)$$

이며, 교차수의 관점에서

$$H^2 = 1, \qquad H \cdot E = 0, \qquad E^2 = -1$$

을 얻는다. 마지막으로 $$H^2 = 1$$임을 명제 7로 확인하자. $$H = \x_0 = D_0$$이지만 $$\rho_0$$만으로는 $$2$$차원 cone을 이룰 수 없으므로 linear relation으로 바꿔 써야 한다. $$H^2 = H \cdot \x_1 + H \cdot \x_3$$이 아니라, $$\x_1 = H - E$$에서 $$H = \x_1 + \x_3 = D_1 + E$$이므로 $$H^2 = H(D_1 + E) = H D_1 + HE = H D_1$$이고, 다시 $$H = D_1 + E$$를 대입하면 $$H D_1 = (D_1 + E) D_1 = D_1^2 + E D_1$$이다. 여기서 $$\rho_1, \rho_3$$은 maximal cone $$\rho_1 + \rho_3$$을 이루므로 명제 7에 의해 $$E D_1 = D_3 D_1 = 1$$이고, $$D_1^2$$은 $$\x_1 \x_2 = 0$$ 즉 $$D_1 D_2 = 0$$과 $$D_1 = D_2$$ (둘 다 $$H - E$$)로부터 $$D_1^2 = D_1 D_2 = 0$$이다. 따라서 $$H^2 = 0 + 1 = 1$$로 기대값과 일치한다. 

이 계산은 blow-up의 표준적 사실, 즉 exceptional divisor의 self-intersection $$E^2 = -1$$과 pullback class의 보존 $$H^2 = 1$$, 그리고 $$E$$가 pullback class와 만나지 않음 $$H \cdot E = 0$$을 fan의 조합론만으로 재현한 것이다.

</div>

---

**참고문헌**

**[Ful]** W. Fulton, *Introduction to Toric Varieties*, Annals of Mathematics Studies, Princeton University Press, 1993.  
**[CLS]** D. Cox, J. Little, H. Schenck, *Toric Varieties*, Graduate Studies in Mathematics, American Mathematical Society, 2011.  
**[Oda]** T. Oda, *Convex Bodies and Algebraic Geometry*, Ergebnisse der Mathematik und ihrer Grenzgebiete, Springer, 1988.  
**[Sta]** R. Stanley, *Combinatorics and Commutative Algebra*, 2nd ed., Progress in Mathematics, Birkhäuser, 1996.
