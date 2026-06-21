---
title: "토릭 다양체의 층 코호몰로지"
description: "토릭 다양체 위의 torus-invariant divisor가 정의하는 line bundle의 층 코호몰로지를 fan과 polytope의 조합론으로부터 계산한다. Global section의 격자점 기술, 고차 코호몰로지의 character lattice graded 기술, Demazure vanishing, 그리고 complete toric variety에서 구조층의 고차 코호몰로지 소멸을 다루고 P^n과 P^1×P^1을 명시적으로 계산한다."
excerpt: "Fan과 polytope의 조합론으로 읽어내는 토릭 다양체의 층 코호몰로지와 Demazure vanishing"

categories: [Math / Toric Geometry]
permalink: /ko/math/toric_geometry/toric_cohomology

sidebar:
    nav: "toric_geometry-ko"

date: 2026-06-20
weight: 8
published: false
---

[§토러스 인자와 선다발, ⁋명제 7](/ko/math/toric_geometry/toric_divisors#prop7)에서 우리는 torus-invariant Weil divisor $$D$$가 정의하는 sheaf $$\mathcal{O}_{X_\Sigma}(D)$$의 global section이 lattice $$M$$ 위의 조합론적 조건으로 완전히 기술됨을 보았다. 이번 글의 목표는 이 기술을 고차 코호몰로지 $$H^i(X_\Sigma, \mathcal{O}_{X_\Sigma}(D))$$ ($$i > 0$$)까지 확장하는 것이다. 일반적인 variety에서 층 코호몰로지를 명시적으로 계산하는 일은 어렵지만 ([\[대수다양체\] §층 코호몰로지](/ko/math/algebraic_varieties/sheaf_cohomology)), toric variety에서는 모든 차수의 코호몰로지가 fan $$\Sigma$$의 조합론으로 환원되며, 특히 nef divisor에 대한 Demazure vanishing과 complete toric variety에서 구조층의 고차 코호몰로지 소멸이라는 강력한 결론을 얻는다.

이하에서 $$N \cong \mathbb{Z}^n$$은 rank $$n$$의 lattice, $$M = \Hom_\mathbb{Z}(N, \mathbb{Z})$$는 그 dual lattice이며, $$\Sigma$$는 $$N_\mathbb{R}$$ 위의 fan으로 $$X_\Sigma$$를 그것이 정의하는 toric variety로 둔다. $$\Sigma(1)$$은 ray들의 모임이고 각 $$\rho \in \Sigma(1)$$에 대해 $$v_\rho \in N$$은 그 primitive generator이다. Torus-invariant Weil divisor는 $$D = \sum_{\rho \in \Sigma(1)} a_\rho D_\rho$$ ([§토러스 인자와 선다발, ⁋정의 2](/ko/math/toric_geometry/toric_divisors#def2))의 꼴이며, 우리는 $$\mathcal{O}_{X_\Sigma}(D)$$의 코호몰로지가 lattice $$M$$의 character로 graded됨을 본질적으로 사용한다. 계수체는 $$\mathbb{C}$$로 둔다.

## Global section의 격자점 기술

먼저 $$H^0$$을 다시 정리한다. 이것은 이미 [§토러스 인자와 선다발, ⁋명제 7](/ko/math/toric_geometry/toric_divisors#prop7)에서 증명한 결과이지만, 이번 글에서 고차 코호몰로지를 graded 형태로 다루기 위한 출발점이므로 polytope의 언어로 다시 적어 둔다. Divisor $$D = \sum_\rho a_\rho D_\rho$$에 대해 polyhedron

$$P_D = \{m \in M_\mathbb{R} \mid \langle m, v_\rho \rangle \ge -a_\rho \text{ for all } \rho \in \Sigma(1)\}$$

을 $$D$$의 *polytope*이라 부른다. $$X_\Sigma$$가 complete이고 $$D$$가 Cartier이면 $$P_D$$는 lattice polytope이다.

<div class="proposition" markdown="1">

<ins id="prop1">**명제 1 (Global section의 격자점 기술)**</ins> Torus-invariant Weil divisor $$D = \sum_{\rho \in \Sigma(1)} a_\rho D_\rho$$에 대해

$$H^0(X_\Sigma, \mathcal{O}_{X_\Sigma}(D)) = \bigoplus_{m \in P_D \cap M} \mathbb{C} \cdot \rchi^m$$

이 성립한다. 특히 $$X_\Sigma$$가 complete이면 이 공간은 유한차원이며 그 차원은 $$\#(P_D \cap M)$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

[§토러스 인자와 선다발, ⁋명제 7](/ko/math/toric_geometry/toric_divisors#prop7)에 의해 $$H^0(X_\Sigma, \mathcal{O}_{X_\Sigma}(D))$$은 조건 $$\langle m, v_\rho \rangle \ge -a_\rho$$ ($$\forall \rho \in \Sigma(1)$$)을 만족하는 $$m \in M$$들의 character $$\rchi^m$$으로 basis를 이룬다. 이 조건은 정확히 $$m \in P_D$$를 뜻하므로 basis를 이루는 character는 $$P_D \cap M$$로 색인된다. $$X_\Sigma$$가 complete이면 $$\Sigma$$의 support가 $$N_\mathbb{R}$$ 전체이므로 ray들이 $$N_\mathbb{R}$$를 span하고, 따라서 $$P_D$$는 위로 유계인 polyhedron, 즉 polytope이 되어 $$P_D \cap M$$이 유한집합이다.

</details>

이 description은 $$D$$가 nef일 때 [\[대수다양체\] §사영공간의 코호몰로지, ⁋정의 2](/ko/math/algebraic_varieties/cohomology_of_projective_spaces#def2)의 Euler characteristic 계산에서 핵심적으로 쓰이며, 격자점의 개수 $$\#(kP_D \cap M)$$가 Ehrhart 다항식을 이루어 교차수와 polytope의 부피를 잇는다 ([§토릭 다양체의 교차 이론, ⁋명제 8](/ko/math/toric_geometry/toric_intersection_theory#prop8)). 우리의 다음 과제는 같은 character grading을 $$i > 0$$의 코호몰로지로 끌어올리는 것이다.

## 고차 코호몰로지의 character grading

$$T_N$$이 $$\mathcal{O}_{X_\Sigma}(D)$$에 작용하므로 그 코호몰로지 전체가 character lattice $$M$$으로 graded된다. 각 weight $$m \in M$$의 graded piece를 fan의 조합론으로 명시적으로 적는 것이 목표이며, 그 답은 $$N_\mathbb{R}$$ 안의 어떤 부분집합의 *reduced cohomology*로 주어진다. 먼저 그 부분집합을 정의한다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> Torus-invariant Weil divisor $$D = \sum_{\rho \in \Sigma(1)} a_\rho D_\rho$$와 $$m \in M$$에 대해, $$N_\mathbb{R}$$의 부분집합

$$V_{D, m} = \bigcup_{\substack{\sigma \in \Sigma}} \operatorname{conv}\bigl(\{ v_\rho \mid \rho \in \sigma(1),\ \langle m, v_\rho \rangle < -a_\rho \}\bigr)$$

를 $$D$$와 $$m$$의 *support set<sub>받침 집합</sub>*이라 부른다. 여기서 $$\sigma(1)$$은 cone $$\sigma$$의 ray들의 모임이고 $$\operatorname{conv}$$는 convex hull이다.

</div>

직관적으로 $$V_{D, m}$$은 character $$\rchi^m$$이 "section이 되기에 부족한" ray들, 즉 $$\langle m, v_\rho \rangle < -a_\rho$$인 ray $$\rho$$들의 primitive generator를 모아 각 cone 안에서 convex hull을 취해 이어붙인 도형이다. $$m \in P_D$$이면 그러한 ray가 하나도 없어 $$V_{D, m} = \varnothing$$이고, 그 외에는 $$\lvert \Sigma \rvert$$ 안의 어떤 polytope들의 합집합이 된다. 다음 정리는 이 도형의 위상이 정확히 weight $$m$$의 코호몰로지를 결정함을 말한다. 여기서 $$\widetilde{H}^j$$는 reduced singular cohomology이며, 관례상 빈 집합에 대해

$$\widetilde{H}^{-1}(\varnothing; \mathbb{C}) = \mathbb{C}, \qquad \widetilde{H}^j(\varnothing; \mathbb{C}) = 0 \ (j \ge 0)$$

으로 둔다.

<div class="proposition" markdown="1">

<ins id="thm3">**정리 3 (코호몰로지의 조합론적 기술)**</ins> Torus-invariant Weil divisor $$D$$에 대해, 모든 $$i \ge 0$$에서 $$H^i(X_\Sigma, \mathcal{O}_{X_\Sigma}(D))$$은 $$M$$으로 graded되며 각 weight $$m \in M$$의 piece는

$$H^i(X_\Sigma, \mathcal{O}_{X_\Sigma}(D))_m \cong \widetilde{H}^{i-1}(V_{D, m}; \mathbb{C})$$

로 주어진다. 따라서

$$H^i(X_\Sigma, \mathcal{O}_{X_\Sigma}(D)) = \bigoplus_{m \in M} \widetilde{H}^{i-1}(V_{D, m}; \mathbb{C}).$$

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

증명의 골격은 $$\mathcal{O}_{X_\Sigma}(D)$$를 Čech 복합체로 계산하되, $$T_N$$-작용에 의한 weight decomposition을 각 차수에서 취하는 것이다. 자세한 전개는 [CLS] Theorem 9.1.3을 따른다.

$$X_\Sigma$$의 affine open cover로 maximal cone들이 주는 $$\{U_\sigma\}_{\sigma \in \Sigma_{\max}}$$를 택한다. 각 $$U_\sigma$$는 affine이므로 $$\mathcal{O}_{X_\Sigma}(D)$$에 대해 acyclic하고 ([\[대수다양체\] §층 코호몰로지, ⁋명제 12](/ko/math/algebraic_varieties/sheaf_cohomology#prop12)), 유한 교집합 $$U_{\sigma_0} \cap \cdots \cap U_{\sigma_p} = U_{\sigma_0 \cap \cdots \cap \sigma_p}$$ 역시 affine이므로, Leray의 정리 ([\[대수다양체\] §층 코호몰로지, ⁋정리 11](/ko/math/algebraic_varieties/sheaf_cohomology#thm11))에 의해 이 cover로 계산한 Čech 코호몰로지가 층 코호몰로지와 일치한다.

각 affine chart 위의 section $$H^0(U_\sigma, \mathcal{O}_{X_\Sigma}(D))$$은 [§토러스 인자와 선다발, ⁋명제 7](/ko/math/toric_geometry/toric_divisors#prop7)의 국소판에 의해 $$\langle m, v_\rho \rangle \ge -a_\rho$$ ($$\rho \in \sigma(1)$$)를 만족하는 $$\rchi^m$$들로 spanned되며, 따라서 $$T_N$$-작용에 대해 $$M$$으로 graded된다. 이 grading은 교집합 위에서도 보존되고 Čech coboundary와 호환되므로, 전체 Čech 복합체가 weight $$m$$ 성분으로 분해된다. 고정된 $$m$$에 대한 weight-$$m$$ Čech 복합체에서, chart $$U_\sigma$$가 $$\rchi^m$$을 section으로 가질 조건은 모든 $$\rho \in \sigma(1)$$에 대해 $$\langle m, v_\rho \rangle \ge -a_\rho$$인 것, 즉 $$\sigma$$가 $$\langle m, v_\rho \rangle < -a_\rho$$인 ray를 하나도 갖지 않는 것이다.

이로부터 weight-$$m$$ 복합체는 $$\rchi^m$$이 "들어가는" chart들이 이루는 단체적 데이터의 (reduced) 코호몰로지를 계산하는 복합체가 됨을 확인할 수 있고, 표준적인 nerve 논증을 거치면 그 코호몰로지가 정확히 정의 2의 $$V_{D, m}$$의 reduced cohomology $$\widetilde{H}^{i-1}(V_{D,m}; \mathbb{C})$$로 동일시된다. 차수 이동 $$i \mapsto i - 1$$은 Čech 복합체의 $$\check{C}^0$$ 항이 reduced cohomology의 $$(-1)$$차 자리에 대응하기 때문이며, 이 때문에 $$V_{D,m} = \varnothing$$인 경우 $$\widetilde{H}^{-1}(\varnothing) = \mathbb{C}$$가 $$H^0$$의 한 character 차원을 정확히 준다. 빈 집합에 대한 이 관례 하에서 $$i = 0$$ 항을 모으면 명제 1과 일치함을 확인할 수 있다.

</details>

정리 3은 토릭 코호몰로지 계산을 순수하게 조합론적 문제로 환원한다. 각 $$m \in M$$마다 $$N_\mathbb{R}$$ 안의 한 도형 $$V_{D, m}$$을 그리고 그 위상을 읽으면 되는 것이다. $$V_{D, m} = \varnothing$$인 $$m$$들이 $$H^0$$을 주고 ($$\widetilde{H}^{-1}(\varnothing) = \mathbb{C}$$), $$V_{D, m}$$이 비지 않으면서 위상적으로 비자명한 $$m$$들이 고차 코호몰로지를 만든다. 실제 계산에서 가장 중요한 경우는 $$X_\Sigma$$가 complete이고 $$D$$가 nef일 때인데, 이 경우 모든 $$V_{D, m}$$이 contractible하거나 비어 있어 고차 코호몰로지가 통째로 사라진다. 이것이 다음 절의 Demazure vanishing이다.

<div class="remark" markdown="1">

<ins id="rmk4">**참고 4**</ins> 정의 2의 support set $$V_{D, m}$$은 문헌에 따라 동치인 여러 형태로 나타난다. [CLS]는 $$\lvert \Sigma \rvert$$ 안에서 $$\langle m, \cdot \rangle + \psi_D \ge 0$$ 또는 $$< 0$$이 되는 영역의 위상으로 기술하며, Cox의 local cohomology 접근 ([CLS] §9.5)은 Cox ring 위의 monomial ideal에 대한 local cohomology로 같은 답을 준다. 또한 $$X_\Sigma$$가 complete이면 $$\lvert \Sigma \rvert = N_\mathbb{R}$$가 contractible하므로 Mayer–Vietoris 또는 긴 완전열을 통해 $$V_{D, m}$$의 reduced cohomology를 그 여집합의 그것으로 바꿔 쓸 수 있고, 이 형태가 Demazure vanishing의 증명에서 편리하다.

</div>

## Demazure vanishing

이제 nef divisor에 대한 고차 코호몰로지 소멸을 본다. Divisor $$D$$가 *nef<sub>numerically effective</sub>*라는 것은 모든 irreducible complete curve $$C \subseteq X_\Sigma$$에 대해 교차수 $$D \cdot C \ge 0$$인 것이다. Complete toric variety에서 nef 조건은 $$D$$가 Cartier일 때 그에 대응하는 piecewise linear function $$\psi_D$$ ([§토러스 인자와 선다발, ⁋명제 6](/ko/math/toric_geometry/toric_divisors#prop6))가 *convex*한 것, 즉 $$\psi_D$$가 위로 볼록인 것과 동치이다. 이는 ample에 대응하는 strictly convex ([§토러스 인자와 선다발, ⁋정의 8](/ko/math/toric_geometry/toric_divisors#def8))의 부등호를 등호 허용으로 완화한 조건이다. nef인 Cartier divisor는 동치로 basepoint-free, 즉 대응 line bundle이 globally generated인 것으로도 특징지어진다 ([\[대수다양체\] §사영공간의 코호몰로지, ⁋정의 6](/ko/math/algebraic_varieties/cohomology_of_projective_spaces#def6)).

<div class="proposition" markdown="1">

<ins id="thm5">**정리 5 (Demazure vanishing)**</ins> $$X_\Sigma$$가 complete toric variety이고 $$D$$가 nef인 torus-invariant Cartier divisor라 하자. 그러면

$$H^i(X_\Sigma, \mathcal{O}_{X_\Sigma}(D)) = 0 \qquad (i > 0)$$

이 성립한다. 특히 $$X_\Sigma$$가 smooth이고 $$D$$가 nef이면 같은 결론이 성립한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

정리 3에 의해 각 $$m \in M$$에서 $$H^i(X_\Sigma, \mathcal{O}_{X_\Sigma}(D))_m = \widetilde{H}^{i-1}(V_{D, m}; \mathbb{C})$$이므로, 모든 $$m \in M$$에 대해 $$V_{D, m}$$이 비어 있거나 contractible함을 보이면 $$i > 0$$에서 $$\widetilde{H}^{i-1}(V_{D,m}) = 0$$이 되어 증명이 끝난다.

$$D$$가 nef이므로 $$\psi_D$$는 convex piecewise linear function이고, 각 maximal cone $$\sigma$$ 위에서 $$\psi_D(v) = \langle m_\sigma, v \rangle$$ ($$m_\sigma \in M$$)이며 convexity로부터 모든 $$v \in N_\mathbb{R}$$에서 $$\psi_D(v) \le \langle m_\sigma, v \rangle$$가 성립한다 ([§토러스 인자와 선다발, ⁋명제 6](/ko/math/toric_geometry/toric_divisors#prop6) 직후 및 [§토러스 인자와 선다발, ⁋정의 8](/ko/math/toric_geometry/toric_divisors#def8)). 부호 규약 $$\psi_D(v_\rho) = -a_\rho$$를 상기하면, 조건 $$\langle m, v_\rho \rangle < -a_\rho$$는 $$\langle m, v_\rho \rangle < \psi_D(v_\rho)$$, 즉 $$\langle m - \,\cdot\,, v_\rho\rangle$$의 부호 문제로 바뀐다. 함수

$$h_m(v) = \langle m, v \rangle - \psi_D(v)$$

를 생각하면, $$\psi_D$$가 convex이므로 $$h_m$$은 concave piecewise linear function이고, $$V_{D, m}$$은 정확히 $$h_m(v_\rho) < 0$$인 ray $$v_\rho$$들이 각 cone 안에서 이루는 convex hull들의 합집합이다.

이제 핵심 관찰은 다음이다. Concave 함수 $$h_m$$에 대해 sublevel set처럼 보이는 $$V_{D,m}$$이 사실 star-shaped 또는 비어 있음을 보인다. 만약 모든 $$\rho$$에서 $$h_m(v_\rho) \ge 0$$이면 $$V_{D, m} = \varnothing$$이다. 그렇지 않으면 어떤 ray에서 $$h_m < 0$$이다. $$X_\Sigma$$가 complete이므로 $$\lvert \Sigma \rvert = N_\mathbb{R}$$이고 $$h_m$$은 $$N_\mathbb{R}$$ 전체에서 정의된 concave piecewise linear 함수이다. Concave 함수의 strict sublevel set $$\{v : h_m(v) < 0\}$$은 convex 집합의 여집합이므로 일반적으로 convex가 아니지만, fan 구조와 호환된 $$V_{D, m}$$은 다음 의미에서 $$\lvert \Sigma \rvert$$ 안에서 *deformation retract*로 한 점에 수축한다. $$h_m$$이 concave이고 그 최댓값이 $$\{h_m \ge 0\}$$ 위에서 달성되므로, 각 ray 방향을 따라 원점 쪽으로 (또는 $$h_m$$이 증가하는 방향으로) 밀어 올리는 선형 homotopy가 $$V_{D, m}$$을 $$V_{D, m}$$ 안의 한 점 또는 빈 집합으로 수축시킨다. 따라서 $$V_{D, m}$$은 비어 있거나 contractible하며, 어느 경우든 $$\widetilde{H}^{j}(V_{D, m}; \mathbb{C}) = 0$$ ($$j \ge 0$$)이다.

그러므로 모든 $$i > 0$$과 모든 $$m \in M$$에 대해 $$H^i(X_\Sigma, \mathcal{O}_{X_\Sigma}(D))_m = \widetilde{H}^{i-1}(V_{D, m}; \mathbb{C}) = 0$$이고, weight를 모두 합하면 $$H^i(X_\Sigma, \mathcal{O}_{X_\Sigma}(D)) = 0$$을 얻는다. Smooth인 경우 Cartier와 Weil이 일치하므로 nef Weil divisor에 대해서도 같은 결론이 성립한다.

</details>

Demazure vanishing은 toric variety에서 nef line bundle이 acyclic임을 말한다. 이는 일반적인 projective variety에서 ample line bundle에 대한 Serre vanishing ([\[대수다양체\] §사영공간의 코호몰로지, ⁋명제 4](/ko/math/algebraic_varieties/cohomology_of_projective_spaces#prop4))이 "충분히 큰 twist에 대해서만" 소멸을 주는 것에 비해 훨씬 강하다. Toric의 조합론적 강성 덕분에 twist 없이 nef 자체에서 즉시 소멸이 일어나며, 이는 nef cone의 모든 lattice point에서 코호몰로지가 $$H^0$$에 집중됨을 뜻한다. 한 가지 직접적 귀결로, nef divisor의 Euler characteristic이 $$H^0$$의 차원과 같아져 lattice point counting $$\#(P_D \cap M)$$로 계산된다.

<div class="proposition" markdown="1">

<ins id="cor6">**따름정리 6**</ins> $$X_\Sigma$$가 complete toric variety이고 $$D$$가 nef Cartier divisor이면

$$\chi(\mathcal{O}_{X_\Sigma}(D)) = \dim_\mathbb{C} H^0(X_\Sigma, \mathcal{O}_{X_\Sigma}(D)) = \#(P_D \cap M)$$

이 성립한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Euler characteristic의 정의 $$\chi(\mathcal{O}_{X_\Sigma}(D)) = \sum_{i \ge 0} (-1)^i \dim H^i(X_\Sigma, \mathcal{O}_{X_\Sigma}(D))$$ ([\[대수다양체\] §사영공간의 코호몰로지, ⁋정의 2](/ko/math/algebraic_varieties/cohomology_of_projective_spaces#def2))에서, 정리 5에 의해 $$i > 0$$ 항이 모두 사라지므로 $$\chi = \dim H^0$$이다. 명제 1에 의해 $$\dim H^0 = \#(P_D \cap M)$$이다.

</details>

## 구조층의 고차 코호몰로지 소멸

Demazure vanishing의 가장 단순하고 중요한 특수경우는 $$D = 0$$, 즉 구조층 $$\mathcal{O}_{X_\Sigma}$$ 자체에 대한 것이다. 영 divisor는 자명하게 nef Cartier divisor이므로 다음을 얻는다.

<div class="proposition" markdown="1">

<ins id="cor7">**따름정리 7**</ins> $$X_\Sigma$$가 complete toric variety이면

$$H^i(X_\Sigma, \mathcal{O}_{X_\Sigma}) = 0 \qquad (i > 0)$$

이고, $$H^0(X_\Sigma, \mathcal{O}_{X_\Sigma}) = \mathbb{C}$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$D = 0$$은 $$\psi_D \equiv 0$$에 대응하며 이는 convex piecewise linear function이므로 nef Cartier divisor이다. 따라서 정리 5에 의해 $$H^i(X_\Sigma, \mathcal{O}_{X_\Sigma}) = 0$$ ($$i > 0$$)이다. $$H^0$$의 경우 명제 1에서 $$P_0 = \{m \in M_\mathbb{R} \mid \langle m, v_\rho \rangle \ge 0 \ \forall \rho\}$$인데, $$X_\Sigma$$가 complete이면 ray들이 $$N_\mathbb{R}$$를 span하므로 이 조건을 만족하는 $$m$$은 $$m = 0$$뿐이다. 따라서 $$P_0 \cap M = \{0\}$$이고 $$H^0(X_\Sigma, \mathcal{O}_{X_\Sigma}) = \mathbb{C} \cdot \rchi^0 = \mathbb{C}$$이다.

</details>

따름정리 7은 complete toric variety가 코호몰로지의 관점에서 매우 "단순"함을 말한다. 구조층의 고차 코호몰로지가 통째로 사라지므로, 가령 smooth complete toric variety는 Hodge 수 $$h^{0, q} = \dim H^q(X_\Sigma, \mathcal{O}_{X_\Sigma}) = 0$$ ($$q > 0$$)을 가지며, 이는 smooth complete toric variety가 홀수 차수 코호몰로지를 갖지 않고 그 코호몰로지가 algebraic cycle로 채워진다는 사실 ([§토릭 다양체의 교차 이론, ⁋참고 6](/ko/math/toric_geometry/toric_intersection_theory#rmk6))과 정합적이다. 또한 이로부터 picard group과 class group을 잇는 exponential 계열 논증에서 $$\Pic(X_\Sigma)$$가 free이고 위상적 $$H^2$$와 일치함을 끌어낼 수 있다.

## 사영공간

이제 위 도구들을 구체적 예시에 적용해 고전적 답을 회복한다. 먼저 $$\mathbb{P}^n$$ 위의 $$\mathcal{O}(d)$$의 코호몰로지가 [\[대수다양체\] §사영공간의 코호몰로지, ⁋명제 1](/ko/math/algebraic_varieties/cohomology_of_projective_spaces#prop1)의 Bott 공식과 일치함을 확인한다.

<div class="example" markdown="1">

<ins id="ex8">**예시 8 ($$\mathbb{P}^n$$ 위의 $$\mathcal{O}(d)$$)**</ins> [§Cox 구성과 GIT quotient, ⁋예시 10](/ko/math/toric_geometry/cox_construction#ex10)에서 보았듯 $$\mathbb{P}^n$$의 fan은 ray $$\rho_0, \ldots, \rho_n$$을 가지며 그 primitive generator는

$$v_i = e_i \ (1 \le i \le n), \qquad v_0 = -e_1 - \cdots - e_n$$

이고, hyperplane class $$H = D_0$$에 대응하는 divisor가 $$d > 0$$에 대해 $$\mathcal{O}_{\mathbb{P}^n}(d) = \mathcal{O}_{\mathbb{P}^n}(dH)$$를 준다. $$D = dH = d D_0$$이므로 $$a_0 = d$$, $$a_i = 0$$ ($$i \ge 1$$)이다.

먼저 $$d \ge 0$$인 경우를 본다. $$\psi_{dH}$$는 [§토러스 인자와 선다발, ⁋예시 11](/ko/math/toric_geometry/toric_divisors#ex11)에서 본 $$\psi_H$$의 $$d$$배이며, $$\psi_H$$가 strictly convex이므로 $$d \ge 0$$에서 $$\psi_{dH}$$는 convex이고 따라서 $$dH$$는 nef이다. 정리 5에 의해 $$H^i(\mathbb{P}^n, \mathcal{O}(d)) = 0$$ ($$i > 0$$)이고, 명제 1에 의해 $$H^0$$은

$$P_{dH} = \{m \in M_\mathbb{R} \mid \langle m, v_0 \rangle \ge -d,\ \langle m, v_i \rangle \ge 0 \ (1 \le i \le n)\}$$

의 lattice point들이 준다. $$m = (m_1, \ldots, m_n)$$로 적으면 조건은 $$m_i \ge 0$$과 $$-(m_1 + \cdots + m_n) \ge -d$$, 즉 $$\sum m_i \le d$$이다. 이는 $$d$$배 표준 simplex $$d\Delta_n$$이며 그 격자점의 개수는

$$\#(d\Delta_n \cap M) = \binom{n + d}{n}$$

이다. 이것은 정확히 차수 $$d$$의 동차 다항식 공간 $$\mathbb{C}[\x_0, \ldots, \x_n]_d$$의 차원으로, [\[대수다양체\] §사영공간의 코호몰로지, ⁋명제 1](/ko/math/algebraic_varieties/cohomology_of_projective_spaces#prop1)의 $$q = 0$$, $$d \ge 0$$ 경우와 일치한다.

이제 $$d < 0$$인 경우를 본다. $$d < 0$$이면 $$a_0 = d < 0$$이고 $$P_{dH}$$의 조건 $$m_i \ge 0$$, $$\sum m_i \le d < 0$$은 양립 불가능하므로 $$P_{dH} \cap M = \varnothing$$, 즉 $$H^0 = 0$$이다. 고차 코호몰로지는 정리 3으로 계산한다. Weight $$m$$의 piece는 $$\widetilde{H}^{i-1}(V_{dH, m})$$인데, $$V_{dH, m}$$은 $$\langle m, v_\rho \rangle < -a_\rho$$인 ray들로 이루어진다. $$\mathbb{P}^n$$의 fan에서 $$n+1$$개의 ray 중 $$n$$개씩이 maximal cone을 이루고 $$n+1$$개 전체는 cone을 이루지 않으므로 ([§토릭 다양체의 교차 이론, ⁋예시 9](/ko/math/toric_geometry/toric_intersection_theory#ex9)), 모든 $$n+1$$개 ray가 "부족한" weight $$m$$에 대해서는 $$V_{dH, m}$$이 $$n+1$$개 점 $$\{v_0, \ldots, v_n\}$$ 각각을 따로 담되 그들이 함께 하나의 cone을 이루지 못해 합집합이 $$n$$차원 구면 $$S^{n-1}$$과 호모토피 동치인 boundary 복합체를 이룬다. 이 때 $$\widetilde{H}^{n-1}(V_{dH, m}; \mathbb{C}) = \mathbb{C}$$이 되어 $$H^n$$에 기여하고, 그 외 차수는 $$0$$이다. 이러한 $$m$$들을 세면 $$\langle m, v_i \rangle < 0$$ ($$0 \le i \le n$$)인 $$m$$, 즉 $$m_i < 0$$과 $$\sum m_i > d$$를 만족하는 격자점들로 그 개수가 $$\binom{-d-1}{n} = \binom{-d - 1}{-d - n - 1}$$이다. 이는 [\[대수다양체\] §사영공간의 코호몰로지, ⁋명제 1](/ko/math/algebraic_varieties/cohomology_of_projective_spaces#prop1)의 $$q = n$$, $$d \le -n-1$$ 경우 $$\mathbb{C}[\x_0^{-1}, \ldots, \x_n^{-1}]_{-d-n-1}$$의 차원과 일치한다. 중간 차수 $$0 < i < n$$에서는 모든 weight $$m$$에 대해 $$V_{dH, m}$$이 비어 있거나 contractible하여 $$H^i = 0$$이며, 이로써 Bott 공식 전체가 fan의 조합론으로부터 회복된다.

</div>

## 사영선의 곱

다음으로 Picard rank가 $$2$$인 가장 단순한 곱공간 $$\mathbb{P}^1 \times \mathbb{P}^1$$ 위에서 bidegree $$(a, b)$$ line bundle의 코호몰로지를 계산한다.

<div class="example" markdown="1">

<ins id="ex9">**예시 9 ($$\mathbb{P}^1 \times \mathbb{P}^1$$)**</ins> [§Cox 구성과 GIT quotient, ⁋예시 11](/ko/math/toric_geometry/cox_construction#ex11)에서 보았듯 $$\mathbb{P}^1 \times \mathbb{P}^1$$의 fan은 $$N = \mathbb{Z}^2$$에서 $$4$$개의 ray

$$v_1 = (1, 0), \quad v_2 = (0, 1), \quad v_3 = (-1, 0), \quad v_4 = (0, -1)$$

을 가지며 maximal cone은 인접한 두 ray로 생성되는 $$4$$개이다. 두 hyperplane class를 [§토릭 다양체의 교차 이론, ⁋예시 10](/ko/math/toric_geometry/toric_intersection_theory#ex10)에서처럼 $$H_1 = D_1 = D_3$$, $$H_2 = D_2 = D_4$$로 두면, line bundle $$\mathcal{O}(a, b)$$는 divisor $$D = a D_3 + b D_4$$ ($$a, b \in \mathbb{Z}$$)에 대응한다. (Linear equivalence로 $$D_1 \sim D_3$$, $$D_2 \sim D_4$$이므로 이 한 표현이 일반적인 bidegree를 모두 준다. 우리의 부호 규약 $$P_D=\{m\mid \langle m,v_\rho\rangle\ge -a_\rho\}$$에서 이 표현이 아래의 표준 polytope $$[0,a]\times[0,b]$$를 준다.)

$$a, b \ge 0$$인 경우, $$D$$의 polytope은

$$P_D = \{(m_1, m_2) \in M_\mathbb{R} \mid m_1 \ge 0,\ m_1 \le a,\ m_2 \ge 0,\ m_2 \le b\} = [0, a] \times [0, b]$$

인 직사각형이다. 이 divisor는 nef이므로 (각 인자에서 $$\psi$$가 convex) 정리 5에 의해 $$H^i = 0$$ ($$i > 0$$)이고, 명제 1에 의해

$$\dim H^0(\mathbb{P}^1 \times \mathbb{P}^1, \mathcal{O}(a, b)) = \#([0,a]\times[0,b] \cap \mathbb{Z}^2) = (a + 1)(b + 1)$$

이다. 이는 Künneth 공식 $$H^0(\mathcal{O}(a, b)) = H^0(\mathbb{P}^1, \mathcal{O}(a)) \otimes H^0(\mathbb{P}^1, \mathcal{O}(b))$$과 $$\dim H^0(\mathbb{P}^1, \mathcal{O}(d)) = d + 1$$ ($$d \ge 0$$)로부터 얻는 $$(a+1)(b+1)$$과 일치한다.

부호가 섞인 경우, 가령 $$a \ge 0$$이고 $$b \le -2$$를 보자. 이 때 $$D = a D_3 + b D_4$$는 nef가 아니므로 정리 3을 직접 쓴다. 각 weight $$m = (m_1, m_2)$$에서 $$V_{D, m}$$은 ray 조건 $$\langle m, v_\rho \rangle < -a_\rho$$로 결정되는데, $$\rho_1, \rho_3$$ 방향($$m_1$$ 성분)에서는 $$0 \le m_1 \le a$$가 가능하여 위상에 기여하지 않고, $$\rho_2, \rho_4$$ 방향($$m_2$$ 성분)에서는 $$m_2 > b$$이면서 $$m_2 < 0$$인 두 조건이 동시에 만족되어 마주보는 두 ray $$v_2, v_4$$가 모두 $$V_{D, m}$$에 들어간다. 이 두 점 $$\{v_2, v_4\} = \{(0,1), (0,-1)\}$$은 cone을 이루지 못하므로 $$V_{D, m}$$이 두 점의 disjoint union, 즉 $$S^0$$과 호모토피 동치가 되어 $$\widetilde{H}^0(V_{D, m}; \mathbb{C}) = \mathbb{C}$$이고 나머지 reduced cohomology는 $$0$$이다. 따라서 $$H^1$$에만 기여하며, 그러한 $$m$$의 개수는 $$0 \le m_1 \le a$$인 $$a + 1$$개의 $$m_1$$과 $$b < m_2 < 0$$인 $$-b - 1$$개의 $$m_2$$를 곱한

$$\dim H^1(\mathbb{P}^1 \times \mathbb{P}^1, \mathcal{O}(a, b)) = (a + 1)(-b - 1)$$

이다. 이것은 Künneth $$H^1(\mathcal{O}(a,b)) = H^0(\mathbb{P}^1, \mathcal{O}(a)) \otimes H^1(\mathbb{P}^1, \mathcal{O}(b))$$과 $$\dim H^1(\mathbb{P}^1, \mathcal{O}(b)) = -b - 1$$ ($$b \le -2$$)로부터 얻는 값과 일치한다. $$a, b$$가 모두 $$\le -2$$인 경우에는 네 ray 전체가 $$V_{D, m}$$에 들어가 boundary가 $$S^1$$과 호모토피 동치가 되어 $$\widetilde{H}^1 = \mathbb{C}$$을 주고, 이는 $$H^2(\mathcal{O}(a,b))$$를 채운다. 이렇게 $$\mathbb{P}^1 \times \mathbb{P}^1$$의 모든 line bundle 코호몰로지가 fan의 격자점 셈으로 환원된다.

</div>

이 두 예시는 정리 3의 조합론적 기술이 고전적인 Bott 공식과 Künneth 분해를 모두 fan의 데이터로부터 재현함을 보여 준다. 핵심은 코호몰로지가 항상 character lattice $$M$$으로 graded되고, 각 weight의 기여가 $$N_\mathbb{R}$$ 안의 한 도형 $$V_{D, m}$$의 reduced cohomology라는 단일 원리로 통제된다는 점이다. Nef divisor에서는 이 도형들이 모두 자명해져 Demazure vanishing이 성립하고, 그 특수경우로 complete toric variety의 구조층이 acyclic해진다.

---

**참고문헌**

**[Ful]** W. Fulton, *Introduction to Toric Varieties*, Annals of Mathematics Studies, Princeton University Press, 1993.  
**[CLS]** D. Cox, J. Little, H. Schenck, *Toric Varieties*, Graduate Studies in Mathematics, American Mathematical Society, 2011.  
**[Dem]** M. Demazure, *Sous-groupes algébriques de rang maximum du groupe de Cremona*, Ann. Sci. École Norm. Sup. **3** (1970), 507–588.  
**[Mus]** M. Mustaţă, *Vanishing theorems on toric varieties*, Tohoku Math. J. **54** (2002), 451–470.
