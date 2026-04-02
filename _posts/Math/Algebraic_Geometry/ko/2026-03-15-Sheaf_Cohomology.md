---
title: "Sheaf Cohomology"
excerpt: "Sheaf cohomology and its applications"

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/sheaf_cohomology
sidebar:
    nav: "algebraic_geometry-ko"

header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Sheaf_Cohomology.png
    overlay_filter: 0.5

date: 2026-03-15
last_modified_at: 2026-04-02
weight: 13
---

([\[위상수학\] §층](/ko/math/topology/sheaves))에서 우리는 sheaf 개념을 정의하였다. Sheaf의 핵심 철학은 국소적 데이터를 전역적 데이터로 결합하는 것이었다. 가령 ([§선다발과 벡터다발](/ko/math/algebraic_geometry/line_bundles))에서 우리는 line bundle $$\mathcal{L}$$의 global section space $$H^0(X, \mathcal{L})$$을 정의하였고, 그 차원을 계산하는 것이 line bundle의 분류에 핵심적임을 살펴보았다.

그러나 sheaf가 우리에게 주는 유일한 정보가 global section뿐이라면 기하학적 도구로서의 활용도는 크지 않을 것이다. 우리의 철학에 따르면, 모든 기하학적 대상은 위상공간과 그 위에 정의된 sheaf의 pair이므로, sheaf 자체를 input으로 받아 새로운 불변량을 output으로 내놓는 기계가 필요하다. 이 글에서 우리는 sheaf의 *cohomology*를 정의하고, 이것이 바로 이러한 역할을 한다는 것을 살펴본다. Sheaf cohomology는 국소적 데이터(각 열린집합 위의 section)가 전역적으로 어떻게 결합되는지를 측정하는 도구이며, Riemann-Roch 정리와 Serre duality의 핵심적인 구성요소이다.

## Derived Functor로서의 정의

Sheaf cohomology를 정의하기 위해 우리는 먼저 global section functor의 성질을 살펴보아야 한다. Variety $$X$$ 위의 quasi-coherent sheaf들의 category $$\mathfrak{Qcoh}(X)$$에서 $$\mathbb{K}$$-vector space들의 category로의 global section functor

$$\Gamma(X, -): \mathfrak{Qcoh}(X) \to \mathrm{Vect}_\mathbb{K}, \qquad \mathcal{F} \mapsto \mathcal{F}(X)$$

는 left exact이다. 구체적으로, sheaf의 short exact sequence $$0 \to \mathcal{F}' \to \mathcal{F} \to \mathcal{F}'' \to 0$$에 $$\Gamma$$를 적용하면

$$0 \to \Gamma(X, \mathcal{F}') \to \Gamma(X, \mathcal{F}) \to \Gamma(X, \mathcal{F}'')$$

는 exact이다. 이것이 성립하는 이유는, 각각의 exactness 조건이 점 $$x \in X$$에서의 exactness로부터 국소적으로 확인되기 때문이다. 예를 들어 $$\Gamma(X, \mathcal{F}') \to \Gamma(X, \mathcal{F})$$이 injective인 것은 $$\mathcal{F}' \to \mathcal{F}$$이 각 점에서 injective이므로 global section에서도 injective인 것으로부터 자명하다.

그러나 우변의 surjection $$\Gamma(X, \mathcal{F}) \to \Gamma(X, \mathcal{F}'') \to 0$$은 일반적으로 성립하지 않는다. ([§선다발과 벡터다발, ⁋예시 16](/ko/math/algebraic_geometry/line_bundles#ex16))에서 우리는 $$\mathcal{O}_{\mathbb{P}^n}(-1)$$의 global section이 $$0$$뿐임을 보았는데, 이는 surjection $$\mathcal{O}_{\mathbb{P}^n}^{\oplus(n+1)} \to \mathcal{O}_{\mathbb{P}^n}(1)$$을 생각하면 $$\Gamma$$를 적용한 후 surjectivity가 깨지는 구체적인 예시가 된다. 즉 $$\Gamma$$는 right exact하지 않으며, 이 "전역화에서 손실되는 정보"를 측정하는 것이 바로 sheaf cohomology의 역할이다.

이를 엄밀하게 구현하기 위해 우리는 homological algebra의 도구를 사용한다. Abelian category에서 left exact functor의 정보 손실을 측정하는 표준적인 방법은 right derived functor를 구성하는 것이다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Quasi-coherent sheaf $$\mathcal{F}$$의 *injective resolution*은 exact sequence

$$0 \to \mathcal{F} \to \mathcal{I}^0 \to \mathcal{I}^1 \to \mathcal{I}^2 \to \cdots$$

이다. 여기서 각 $$\mathcal{I}^i$$는 injective quasi-coherent sheaf이다.

</div>

Quasi-coherent sheaf의 category에는 충분한 injective object가 존재하므로, 임의의 quasi-coherent sheaf $$\mathcal{F}$$는 항상 injective resolution을 갖는다. 이제 global section functor $$\Gamma$$를 injective resolution에 적용하면 복합체(complex)

$$0 \to \Gamma(X, \mathcal{I}^0) \to \Gamma(X, \mathcal{I}^1) \to \Gamma(X, \mathcal{I}^2) \to \cdots$$

를 얻는다. $$\Gamma$$가 left exact이므로 $$H^0(\Gamma(X, \mathcal{I}^\bullet)) = \ker(\Gamma(X, \mathcal{I}^0) \to \Gamma(X, \mathcal{I}^1))$$은 원래의 $$\Gamma(X, \mathcal{F})$$와 동형이다. 일반적으로 이 복합체의 cohomology가 바로 sheaf cohomology를 정의한다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> Variety $$X$$ 위의 quasi-coherent sheaf $$\mathcal{F}$$에 대하여, $$i$$번째 *sheaf cohomology* $$H^i(X, \mathcal{F})$$를

$$H^i(X, \mathcal{F}) = \frac{\ker(\Gamma(X, \mathcal{I}^i) \to \Gamma(X, \mathcal{I}^{i+1}))}{\operatorname{im}(\Gamma(X, \mathcal{I}^{i-1}) \to \Gamma(X, \mathcal{I}^i))}$$

으로 정의한다. 여기서 $$\mathcal{I}^\bullet$$은 $$\mathcal{F}$$의 injective resolution이다.

</div>

이 정의가 잘 되려면 $$H^i$$가 injective resolution의 선택에 무관해야 하는데, 이는 homological algebra의 표준적인 논증으로부터 보장된다. 두 injective resolution은 chain homotopy equivalence 관계에 있으므로, $$\Gamma$$를 적용한 복합체의 cohomology는 동형이다.

$$i = 0$$인 경우, 위에서 논의한 대로 $$H^0(X, \mathcal{F}) \cong \Gamma(X, \mathcal{F})$$이다. $$i > 0$$인 경우, $$H^i$$는 전역 section의 "장애물"을 측정한다. 구체적으로, $$H^1(X, \mathcal{F})$$는 local section들을 전역적으로 "붙이는" 과정에서 나타나는 실패 정도를 나타낸다. 만약 $$H^1 = 0$$이면, 국소적 데이터가 항상 전역적으로 결합될 수 있다는 뜻이다. 더 높은 $$H^i$$들은 더 복잡한 국소-전역 장애물들을 측정한다.

## Čech Cohomology와의 관계

[정의 2](#def2)는 sheaf cohomology의 정의로서는 엄밀하지만, injective resolution을 명시적으로 구성하는 것은 일반적으로 매우 어렵다. 따라서 실제 계산에서는 다른 관점에서 cohomology를 정의하는 Čech approach를 사용한다. Čech cohomology의 아이디어는 단순하다: sheaf의 cohomology가 "local data를 global data로 결합하는 과정에서의 장애물"이라면, 이 장애물을 열린집합들의 cover 위에서 직접 측정할 수 있어야 한다. 구체적으로, 각 열린집합 위의 section이 주어졌을 때 이들이 얼마나 잘 "붙여지는"지를 교차점에서의 불일치로 측정하는 것이다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> Finite open cover $$\mathcal{U} = \{U_1, \ldots, U_r\}$$에 대하여, $$p$$-차 *Čech 복합체* $$C^p(\mathcal{U}, \mathcal{F})$$를

$$C^p(\mathcal{U}, \mathcal{F}) = \prod_{i_0 < \cdots < i_p} \mathcal{F}(U_{i_0} \cap \cdots \cap U_{i_p})$$

으로 정의한다. 즉, $$p$$-cochain은 $$p+1$$개의 열린집합들의 교차점 위에 정의된 section들의 모임이다. $$p = 0$$이면 $$C^0 = \prod_i \mathcal{F}(U_i)$$이고, $$p = 1$$이면 $$C^1 = \prod_{i < j} \mathcal{F}(U_i \cap U_j)$$이다.

이제 이 cochain group들 사이의 *Čech 미분* $$d^p: C^p \to C^{p+1}$$를 다음과 같이 정의한다. $$p$$-cochain $$\alpha = (\alpha_{i_0 \cdots i_p})$$에 대하여,

$$(d^p\alpha)_{i_0 \cdots i_{p+1}} = \sum_{k=0}^{p+1} (-1)^k \alpha_{i_0 \cdots \widehat{i_k} \cdots i_{p+1}}$$

이다. 여기서 $$\widehat{i_k}$$는 index $$i_k$$를 생략한다는 의미이다.

이 미분의 직관적 의미를 $$p = 0$$과 $$p = 1$$의 경우로 이해할 수 있다. $$p = 0$$에서 각 $$s_i \in \mathcal{F}(U_i)$$는 열린집합 $$U_i$$ 위의 local section이다. Čech 미분은 $$(d^0 s)_{ij} = s_j|_{U_i \cap U_j} - s_i|_{U_i \cap U_j}$$로, 즉 두 인접한 local section의 제한의 차이를 계산한다. $$d^0 s = 0$$이라는 것은 모든 $$U_i \cap U_j$$에서 $$s_i|_{U_i \cap U_j} = s_j|_{U_i \cap U_j}$$라는 뜻이며, sheaf의 gluing 조건에 의해 이는 global section의 존재와 동치이다. $$p = 1$$에서 cocycle 조건 $$d^1 \alpha = 0$$은 세 열린집합 $$U_i \cap U_j \cap U_k$$ 위에서 $$\alpha_{ij} - \alpha_{ik} + \alpha_{jk} = 0$$을 의미하는데, 이는 local section들의 "불일치"가 순환을 따라 합해지면 0이 된다는 일관성 조건이다.

임의의 $$p$$에 대하여 $$d^2 = 0$$임은 교대 부호의 계산으로부터 직접 확인된다.

</div>

<div class="definition" markdown="1">

<ins id="def4">**정의 4** Open cover $$\mathcal{U}$$에 대한 *Čech cohomology* $$\check{H}^p(\mathcal{U}, \mathcal{F})$$를

$$\check{H}^p(\mathcal{U}, \mathcal{F}) = \frac{\ker d^p}{\operatorname{im} d^{p-1}}$$

으로 정의한다. Cover의 refinement는 자연스러운 사상 $$\check{H}^p(\mathcal{U}, \mathcal{F}) \to \check{H}^p(\mathcal{V}, \mathcal{F})$$를 유도하므로, *Čech cohomology* $$\check{H}^p(X, \mathcal{F})$$를 모든 open cover에 대한 direct limit로 정의한다.

일반적으로 $$\check{H}^p(X, \mathcal{F})$$와 [정의 2](#def2)의 $$H^p(X, \mathcal{F})$$는 동형이라고 보장되지 않는다. 그러나 다행히 대수기하학에서 등장하는 대부분의 sheaf에 대해서는 둘이 일치한다.

</div>

이처럼 Čech cohomology와 sheaf cohomology는 본질적으로 다른 정의에서 출발하지만, 적절한 조건 하에서는 서로 동형이 된다. 이를 보장하는 가장 중요한 결과가 Leray 정리이다. Leray 정리의 조건인 acyclicity는 직관적으로, 각 열린집합 (과 그들의 교차점) 위에서는 cohomology가 자명하다는 뜻이다. 즉, 각 열린집합 위에서는 local data가 완벽하게 global data로 결합될 수 있다는 의미이며, 이 경우 cover가 충분히 좋으면 전체 공간에서의 cohomology도 Čech 복합체만으로 계산할 수 있다. 특히 대수기하학에서는 Serre의 기본 정리에 의하여 affine scheme 위에서 quasi-coherent sheaf의 cohomology가 모두 소멸하므로 ($$H^i(\operatorname{Spec} A, \widetilde{M}) = 0$$ for $$i > 0$$), quasi-coherent sheaf에 대하여 affine open cover를 사용하면 acyclicity 조건이 자동으로 만족된다. 따라서 이 경우 Čech cohomology와 sheaf cohomology가 일치한다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5** (Leray 정리) Open cover $$\mathcal{U} = \{U_i\}$$가 다음 조건을 만족하면, Čech cohomology가 sheaf cohomology와 동형이다:

$$H^s(U_{i_0} \cap \cdots \cap U_{i_p}, \mathcal{F}) = 0 \quad \text{for all } s > 0, \text{ all finite intersections}$$

즉, 이 조건 하에서 $$\check{H}^p(\mathcal{U}, \mathcal{F}) \cong H^p(X, \mathcal{F})$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Leray 정리의 증명은 double complex를 통한 spectral sequence argument에 의한다. Cover $$\mathcal{U} = \{U_i\}$$와 $$\mathcal{F}$$의 injective resolution $$\mathcal{I}^\bullet$$에 대하여 double complex

$$C^{p,q} = C^p(\mathcal{U}, \mathcal{I}^q) = \prod_{i_0 < \cdots < i_p} \Gamma(U_{i_0} \cap \cdots \cap U_{i_p}, \mathcal{I}^q)$$

를 생각하자. 이 복합체는 두 방향의 미분을 갖는다: Čech 미분 $$d_\mathrm{\check{C}}: C^{p,q} \to C^{p+1,q}$$와 resolution의 미분 $$d_\mathcal{I}: C^{p,q} \to C^{p,q+1}$$이다.

이 double complex의 total complex $$\operatorname{Tot}(C^{\bullet,\bullet})$$의 cohomology를 두 가지 방식으로 계산할 수 있다. 첫째, column-wise filtration을 사용하면 Čech-to-derived functor spectral sequence를 얻으며, 그 $$E_2$$ 페이지는 $$E_2^{p,q} = \check{H}^p(\mathcal{U}, \mathcal{H}^q(\mathcal{F}))$$이다. 여기서 $$\mathcal{H}^q(\mathcal{F})$$는 presheaf $$U \mapsto H^q(U, \mathcal{F})$$이다.

이제 acyclicity 조건 $$H^s(U_{i_0} \cap \cdots \cap U_{i_p}, \mathcal{F}) = 0$$ ($$s > 0$$)에 의하여, presheaf $$\mathcal{H}^q(\mathcal{F})$$의 모든 값이 $$0$$이므로 $$q > 0$$인 열이 모두 소멸한다. 따라서 spectral sequence는 $$E_2$$ 페이지에서 이미 degenerate하고, 유일하게 남은 항은 $$E_2^{p,0} = \check{H}^p(\mathcal{U}, \mathcal{H}^0(\mathcal{F})) = \check{H}^p(\mathcal{U}, \mathcal{F})$$이다.

둘째, row-wise filtration을 사용하면 total complex의 cohomology가 $$H^p(X, \mathcal{F})$$와 동형인 것을 확인할 수 있다. 이는 injective sheaf가 항상 flasque이고, flasque sheaf는 모든 open subset 위에서의 제한이 surjective이므로 Čech 복합체가 exact하게 되어 Čech cohomology가 자명하기 때문이다. 두 결과를 비교하면 $$\check{H}^p(\mathcal{U}, \mathcal{F}) \cong H^p(X, \mathcal{F})$$를 얻는다.

</details>

## Long Exact Sequence

Sheaf cohomology의 핵심 도구 중 하나는 short exact sequence에서 유도되는 long exact sequence이다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6** Sheaf의 short exact sequence

$$0 \to \mathcal{F}' \to \mathcal{F} \to \mathcal{F}'' \to 0$$

에 대하여, 긴 완전열

$$0 \to H^0(X, \mathcal{F}') \to H^0(X, \mathcal{F}) \to H^0(X, \mathcal{F}'') \xrightarrow{\delta} H^1(X, \mathcal{F}') \to \cdots$$

이 존재한다. 여기서 $$\delta$$는 *connecting homomorphism*이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Short exact sequence $$0 \to \mathcal{F}' \to \mathcal{F} \to \mathcal{F}'' \to 0$$가 주어졌다 하자. Horseshoe lemma에 의해 이 short exact sequence를 injective resolution의 level로 올릴 수 있다. 구체적으로, $$\mathcal{F}'$$과 $$\mathcal{F}''$$의 injective resolution $$\mathcal{I}'^\bullet$$과 $$\mathcal{I}''^\bullet$$을 각각 선택하면, $$\mathcal{F}$$의 injective resolution $$\mathcal{I}^\bullet$$과 short exact sequence of complexes

$$0 \to \mathcal{I}'^\bullet \to \mathcal{I}^\bullet \to \mathcal{I}''^\bullet \to 0$$

이 존재한다. 여기서 각 항 $$0 \to \mathcal{I}'^i \to \mathcal{I}^i \to \mathcal{I}''^i \to 0$$은 split exact이다. $$\mathcal{I}'^i$$가 injective object이므로 inclusion $$\mathcal{I}'^i \hookrightarrow \mathcal{I}^i$$에 대하여 항등사상 $$\mathcal{I}'^i \to \mathcal{I}'^i$$를 $$\mathcal{I}^i$$로 확장하는 retraction $$\mathcal{I}^i \to \mathcal{I}'^i$$가 존재하며, 이로부터 sequence는 split한다.

이제 global section functor $$\Gamma$$를 적용하면 복합체들의 short exact sequence

$$0 \to \Gamma(X, \mathcal{I}'^\bullet) \to \Gamma(X, \mathcal{I}^\bullet) \to \Gamma(X, \mathcal{I}''^\bullet) \to 0$$

를 얻는다. 우변의 surjectivity는 각 단계에서의 sequence가 split exact이므로 $$\Gamma$$를 적용한 후에도 exact하기 때문이다. 이제 이 short exact sequence of complexes에 ([\[동대수학\] §Homology, ⁋정리 2](/ko/math/homological_algebra/homology#thm2))의 long exact sequence of cohomology를 적용하면 원하는 long exact sequence

$$\cdots \to H^i(X, \mathcal{F}') \to H^i(X, \mathcal{F}) \to H^i(X, \mathcal{F}'') \xrightarrow{\delta} H^{i+1}(X, \mathcal{F}') \to \cdots$$

를 얻는다. Connecting homomorphism $$\delta$$의 구체적인 작용은 다음과 같다. 원소 $$[\alpha''] \in H^i(X, \mathcal{F}'')$$가 주어지면, 이를 나타내는 cocycle $$\alpha'' \in \Gamma(X, \mathcal{I}''^i)$$를 잡고, $$\Gamma(X, \mathcal{I}^i) \to \Gamma(X, \mathcal{I}''^i)$$가 surjective이므로 $$\alpha \in \Gamma(X, \mathcal{I}^i)$$로 lift한다. 그럼 $$d\alpha$$는 $$\Gamma(X, \mathcal{I}''^{i+1})$$에서 $$0$$으로 보내지므로 $$\Gamma(X, \mathcal{I}'^{i+1})$$의 원소가 되고, 이것이 바로 $$\delta[\alpha'']$$를 정의한다.

</details>

## $$\mathbb{P}^n$$에서의 Cohomology 계산

이제 우리는 Čech cohomology를 사용하여 $$\mathbb{P}^1$$ 위의 line bundle $$\mathcal{O}(k)$$의 cohomology를 직접 계산한다. 이를 위해 standard open cover $$U_0 = \{x_0 \ne 0\}$$, $$U_1 = \{x_1 \ne 0\}$$를 사용한다. 각각의 $$U_i$$에서 좌표함수를 $$t_i = x_{1-i}/x_i$$라 두자. 그럼 $$U_0 \cap U_1$$에서 $$t_0 = 1/t_1$$이고, $$\mathcal{O}(k)$$의 transition function은 $$g_{01} = (x_1/x_0)^k = t_0^{-k}$$이다.

<div class="example" markdown="1">

<ins id="ex7">**예시 7**</ins> **$$H^0(\mathbb{P}^1, \mathcal{O}(k))$$의 계산** Čech complex는

$$0 \to C^0 = \mathcal{O}(k)(U_0) \times \mathcal{O}(k)(U_1) \xrightarrow{d^0} C^1 = \mathcal{O}(k)(U_0 \cap U_1) \to 0$$

이다. Čech 미분의 계산을 위해, $$\mathcal{O}(k)$$의 section을 모두 $$U_0$$의 좌표 $$t_0$$로 표현하자. $$s_0 \in \mathcal{O}(k)(U_0)$$는 $$t_0$$의 다항식이고, $$s_1 \in \mathcal{O}(k)(U_1)$$은 $$U_1$$의 좌표 $$t_1$$의 다항식이며, 이를 $$U_0$$ 좌표로 변환하면 $$g_{10} \cdot s_1(t_0^{-1}) = t_0^{k} s_1(t_0^{-1})$$가 된다 (여기서 $$g_{10} = (x_0/x_1)^k = t_0^k$$는 $$U_1 \to U_0$$ 방향의 transition function이다). 따라서

$$d^0(s_0, s_1) = t_0^{k} s_1(t_0^{-1}) - s_0(t_0) \in \mathcal{O}(k)(U_0 \cap U_1)$$

이다. $$H^0$$는 $$\ker d^0$$이므로, 이 차이가 0이 되는 section들의 공간이다. 이는 정확히 global section의 공간이다.

$$k \ge 0$$인 경우, $$\mathcal{O}(k)(U_0) = \mathbb{K}[t_0]$$이고, $$\mathcal{O}(k)(U_1) = \mathbb{K}[t_1] = \mathbb{K}[t_0^{-1}]$$이다. Global section은 $$U_0 \cap U_1$$에서 두 좌표계 사이의 변환을 고려할 때 모두 regular이어야 하므로, $$t_0$$에 대한 degree $$\le k$$인 다항식이다. 보다 정확히, $$s_0(t_0) = a_0 + a_1 t_0 + \cdots + a_k t_0^k \in \mathbb{K}[t_0]$$가 주어지면 $$t_0^k s_1(t_0^{-1}) = s_0(t_0)$$이 되려면 $$s_1(t_1) = a_k + a_{k-1}t_1 + \cdots + a_0 t_1^k$$이어야 하며, 이는 $$\mathbb{K}[t_1]$$의 원소이다. 따라서 $$\dim H^0(\mathbb{P}^1, \mathcal{O}(k)) = k+1$$이다. ([§선다발과 벡터다발, ⁋예시 16](/ko/math/algebraic_geometry/line_bundles#ex16))

$$k < 0$$인 경우, $$s_0(t_0) \in \mathbb{K}[t_0]$$이고 $$t_0^k s_1(t_0^{-1}) = s_0(t_0)$$를 만족해야 하는데, $$s_1 \in \mathbb{K}[t_0^{-1}]$$이므로 $$t_0^k s_1(t_0^{-1})$$은 $$t_0$$에 대해 degree $$\le k < 0$$인 항들로 구성된다. 반면 $$s_0(t_0)$$는 degree $$\ge 0$$이어야 하므로, 양쪽 모두를 만족하는 것은 $$s_0 = 0$$뿐이다. 따라서 $$H^0(\mathbb{P}^1, \mathcal{O}(k)) = 0$$이다.

</div>

<div class="example" markdown="1">

<ins id="ex8">**예시 8**</ins> **$$H^1(\mathbb{P}^1, \mathcal{O}(k))$$의 계산** $$H^1$$은 $$C^1 / \operatorname{im} d^0$$이다. 모든 section을 $$U_0$$의 좌표 $$t_0$$로 표현하면, Čech complex에서 $$C^1 = \mathcal{O}(k)(U_0 \cap U_1) = \mathbb{K}[t_0, t_0^{-1}]$$이다. 예시 7에서 계산한 Čech 미분에 의해

$$\operatorname{im} d^0 = \{t_0^{k} p(t_0^{-1}) - q(t_0) \mid p \in \mathbb{K}[t_0^{-1}],\; q \in \mathbb{K}[t_0]\}$$

이다. 여기서 $$q(t_0) = s_0(t_0) \in \mathcal{O}(k)(U_0) = \mathbb{K}[t_0]$$은 $$U_0$$-좌표에서의 section이고, $$p(t_0^{-1}) = s_1(t_0^{-1}) \in \mathbb{K}[t_0^{-1}]$$은 $$U_1$$-좌표에서의 section $$s_1(t_1)$$을 $$U_0$$-좌표의 독립변수로 치환한 것이다. 전체 transition function을 포함한 항 $$t_0^k p(t_0^{-1})$$이 바로 $$U_1$$의 section을 $$U_0$$ 좌표계로 변환한 결과이다.

$$k \ge 0$$인 경우, $$t_0^{k}p(t_0^{-1})$$는 $$t_0^k(a_0 + a_1 t_0^{-1} + \cdots) = a_0 t_0^k + a_1 t_0^{k-1} + \cdots$$이므로 degree $$\ge 0$$인 모든 항과 degree $$\le k$$인 모든 항을 제공하고, $$-q(t_0)$$는 degree $$\ge 0$$인 항들을 제공한다. 두 부분을 합치면 degree $$\le k$$와 degree $$\ge 0$$의 항들을 모두 cover할 수 있으며, 나머지 degree $$> k$$인 양의 차수 항들은 $$q(t_0)$$의 고차항으로 처리된다. 결과적으로 임의의 Laurent 다항식을 $$\operatorname{im} d^0$$로 표현할 수 있으므로 $$H^1(\mathbb{P}^1, \mathcal{O}(k)) = 0$$이다.

$$k < 0$$인 경우 (즉 $$-k > 0$$), $$t_0^{k}p(t_0^{-1}) = t_0^{k}(a_0 + a_1 t_0^{-1} + \cdots) = a_0 t_0^{k} + a_1 t_0^{k-1} + \cdots$$는 degree $$\le k < 0$$인 항들을 제공하고, $$-q(t_0)$$는 degree $$\ge 0$$인 항들을 제공한다. 따라서 $$\operatorname{im} d^0$$가 cover하는 degree는 $$\le k$$와 $$\ge 0$$이며, 그 사이의 간격 $$k+1, k+2, \ldots, -1$$에 해당하는 항들은 $$\operatorname{im} d^0$$로 표현할 수 없다. 이 간격의 크기가 정확히 $$|k| - 1 = -k - 1$$이므로 $$\dim H^1(\mathbb{P}^1, \mathcal{O}(k)) = -k - 1$$이다.

</div>

위의 계산을 종합하면 $$\mathbb{P}^1$$의 cohomology가 완전히 결정된다. $$H^0$$과 $$H^1$$의 차원이 서로 반대 방향으로 움직이는 것은 Serre duality의 초기 예시이다.

<div class="example" markdown="1">

<ins id="ex9">**예시 9**</ins> **$$\mathbb{P}^n$$의 cohomology** $$\mathbb{P}^n$$ 위에서도 동일한 방법으로 Čech cohomology를 계산할 수 있다. Standard open cover $$U_i = \{x_i \ne 0\}$$를 사용하면, $$\mathbb{P}^n$$의 line bundle $$\mathcal{O}_{\mathbb{P}^n}(k)$$의 cohomology는 다음과 같다.

$$k \ge 0$$인 경우, $$\dim H^0(\mathbb{P}^n, \mathcal{O}(k)) = \binom{n+k}{k}$$이고 나머지 $$H^i = 0$$ ($$i > 0$$)이다. 여기서 $$H^0(\mathbb{P}^n, \mathcal{O}(k))$$는 $$n+1$$개 변수 $$x_0, \ldots, x_n$$의 degree $$k$$ 동차다항식들의 공간과 동형이며, 그 차원 $$\binom{n+k}{k} = \binom{n+k}{n}$$는 $$n+1$$개 변수의 degree $$k$$ 단항식의 개수와 일치한다. Higher cohomology가 소멸하는 것은 Čech 복합체의 직접 계산으로부터 얻어진다. $$k \ge 0$$이면 각 교차점 위에서의 transition function이 Laurent 다항식의 음수 차수 부분을 생성하지 않아, 모든 higher Čech cohomology가 소멸한다. 이는 Čech 복합체의 직접 계산으로부터 얻어지며, ([§Cohomology of Line Bundles](/ko/math/algebraic_geometry/cohomology_of_line_bundles))에서 상세히 다룬다.

$$k \le -n-1$$인 경우, $$\dim H^n(\mathbb{P}^n, \mathcal{O}(k)) = \binom{-k-1}{n}$$이고 나머지 $$H^i = 0$$ ($$i < n$$)이다. 여기서 $$H^n$$만이 nonzero인 이유는 다음과 같이 이해할 수 있다. Čech 복합체에서 $$H^n$$은 $$n+1$$개의 chart가 모두 겹치는 교차점 $$U_0 \cap \cdots \cap U_n$$ 위에서의 section으로부터 계산되는데, $$\mathbb{P}^n$$의 standard open cover는 $$n+1$$개의 chart로 구성되므로 $$p > n$$인 cochain group $$C^p$$는 자명하게 $$0$$이다. 따라서 $$H^n$$이 최상위 cohomology이며, $$k \le -n-1$$일 때만 이 교차점 위에서 nontrivial한 cocycle이 존재할 수 있다. 차원 $$\binom{-k-1}{n}$$은 $$\mathbb{P}^1$$의 경우와 동일한 방식으로 Laurent 다항식의 분석으로부터 얻어진다.

마지막으로 $$-n \le k \le -1$$인 경우, 모든 $$H^i = 0$$이다. 이는 다음과 같이 이해할 수 있다. $$k < 0$$이므로 $$\mathcal{O}(k)$$의 global section이 없어 $$H^0 = 0$$이다. 반면 $$k \ge -n$$이면 Čech 복합체의 Laurent 다항식 분석에서 각 degree의 gap이 발생하지 않아 higher cohomology도 소멸한다. 구체적으로, 앞서 설명한 대로 cochain group이 $$C^0, \ldots, C^n$$까지만 존재하므로, Čech 미분의 분석에서 $$-n \le k \le -1$$일 때 각 $$p$$에 대해 $$\operatorname{im} d^{p-1} = \ker d^p$$가 성립한다.

</div>

## Serre Duality 미리보기

Sheaf cohomology의 가장 중요한 응용 중 하나는 ([§선다발과 벡터다발, ⁋예시 24](/ko/math/algebraic_geometry/line_bundles#ex24))에서 도입한 canonical bundle $$\omega_X$$과 관련된 Serre duality이다. 위의 [예시 7](#ex7), [예시 8](#ex8)에서 살펴본 $$\mathbb{P}^1$$의 cohomology는 이미 Serre duality의 특수한 경우로 해석할 수 있다. $$\mathbb{P}^1$$의 canonical bundle은 $$\omega_{\mathbb{P}^1} = \mathcal{O}(-2)$$이며, Serre duality에 의해

$$H^i(\mathbb{P}^1, \mathcal{O}(k))^\ast \cong H^{1-i}(\mathbb{P}^1, \omega_{\mathbb{P}^1} \otimes \mathcal{O}(-k)) = H^{1-i}(\mathbb{P}^1, \mathcal{O}(-k-2))$$

이 성립한다. 이를 $$i=0$$에 적용하면 $$\dim H^0(\mathbb{P}^1, \mathcal{O}(k)) = \dim H^1(\mathbb{P}^1, \mathcal{O}(-k-2))$$을 얻고, [예시 7](#ex7)과 [예시 8](#ex8)의 결과와 정확히 일치하는 것을 확인할 수 있다. 일반적인 정리는 §Serre Duality에서 다룬다.

<div class="misc" markdown="1">
**미리보기 (Serre Duality).** Smooth projective variety $$X$$ of dimension $$n$$과 임의의 locally free sheaf $$\mathcal{E}$$에 대하여, 자연스러운 동형

$$H^i(X, \mathcal{E})^\ast \cong H^{n-i}(X, \omega_X \otimes \mathcal{E}^\vee)$$

이 존재한다고 알려져 있다. 특히 $$\mathcal{E} = \mathcal{O}_X$$인 경우 $$H^i(X, \mathcal{O}_X)^\ast \cong H^{n-i}(X, \omega_X)$$이고, $$i = n$$이면 $$H^n(X, \omega_X) \cong \mathbb{K}$$이다. 전체 증명과 응용은 §Serre Duality에서 다룬다.
</div>

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.  
