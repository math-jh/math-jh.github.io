---
title: "Čech Cohomology"
excerpt: "Čech cohomology and its relation to sheaf cohomology"

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/cech_cohomology
sidebar: 
    nav: "algebraic_geometry-ko"

header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Cech_Cohomology.png
    overlay_filter: 0.5

date: 2026-03-15
last_modified_at: 2026-04-02
weight: 13
published: false
---

이 글의 내용은 [§Sheaf Cohomology](/ko/math/algebraic_geometry/sheaf_cohomology)에 통합되었습니다.

## 도입

Sheaf cohomology ([§Sheaf Cohomology, ⁋정의 1](/ko/math/algebraic_geometry/sheaf_cohomology#def1))는 global section functor의 right derived functor로 정의된다. 이 정의는 범주론적으로 깔끔하지만, 그 추상성 때문에 구체적인 계산이 어렵다. 가령 주어진 sheaf $$\mathcal{F}$$에 대하여 $$H^1(X, \mathcal{F})$$의 원소를 직접 묘사하려면 injective resolution을 구성해야 하는데, 이는 대부분의 경우 실질적으로 불가능하다.

이러한 어려움을 극복하기 위해 우리는 **Čech cohomology**를 도입한다. Čech cohomology는 위상공간 $$X$$의 open cover $$\mathfrak{U} = \{U_i\}$$를 선택하고, sheaf $$\mathcal{F}$$의 각 overlap $$U_{i_0} \cap \cdots \cap U_{i_p}$$ 위에서의 section들로부터 직접 cochain complex를 구성하는 방식이다. 이 정의는 open cover라는 구체적인 데이터를 사용하므로 계산이 훨씬 용이하며, 특히 [§선다발과 벡터다발](/ko/math/algebraic_geometry/line_bundles)에서 살펴본 line bundle의 transition function들이 자연스럽게 Čech 1-cocycle을 이룬다는 사실을 통해 기하학적 대상과 cohomological data의 대응을 직접적으로 관찰할 수 있다.

물론 Čech cohomology가 open cover의 선택에 의존한다는 문제가 있다. 그러나 다행히 "좋은" 조건 하에서 — 구체적으로 open cover의 모든 유한 교집합에서 sheaf가 acyclic일 때 — Čech cohomology는 sheaf cohomology와 완전히 일치한다. 특히 scheme 위의 quasi-coherent sheaf와 affine open cover의 경우 이 조건이 자동으로 충족되므로, 대수기하학의 많은 상황에서 Čech cohomology는 sheaf cohomology를 계산하는 실질적인 도구가 된다.

## Čech Complex

고전적인 de Rham cohomology에서 우리는 미분형식들의 complex $$0 \to \Omega^0 \to \Omega^1 \to \Omega^2 \to \cdots$$를 구성하고, 이 complex의 cohomology를 계산하는 방식으로 위상불변량을 얻었다. Čech cohomology는 비슷한 전략을 따르지만, 미분형식 대신 sheaf의 section을, exterior derivative 대신 open cover의 교집합 구조에서 오는 coboundary map을 사용한다. 구체적으로, $$p$$개의 열린집합이 겹치는 영역 위에서의 section들이 $$p$$-cochain을 이루고, coboundary map은 $$p$$-cochain을 $$(p+1)$$-cochain으로 보낸다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 위상공간 $$X$$의 open cover $$\mathfrak{U} = \{U_i\}_{i \in I}$$와 sheaf $$\mathcal{F}$$에 대해 **Čech complex** $$C^\bullet(\mathfrak{U}, \mathcal{F})$$를 다음과 같이 정의한다. 여기서 인덱스 집합 $$I$$에는 임의의 전순서(total order)가 주어져 있다고 가정한다:

$$C^p(\mathfrak{U}, \mathcal{F}) = \prod_{i_0 < \cdots < i_p} \mathcal{F}(U_{i_0} \cap \cdots \cap U_{i_p})$$

Coboundary map $$d: C^p \to C^{p+1}$$은:

$$(d\alpha)_{i_0 \cdots i_{p+1}} = \sum_{k=0}^{p+1} (-1)^k \alpha_{i_0 \cdots \hat{i_k} \cdots i_{p+1}}\vert_{U_{i_0 \cdots i_{p+1}}}$$

</div>

이 정의가 well-defined이기 위해서는 $$d \circ d = 0$$이 성립해야 한다. 이는 alternating sum의 구조로부터 직접 확인된다. 구체적으로, $$d(d\alpha)$$를 계산해보면 각각의 $$\alpha_{i_0 \cdots \hat{i_k} \hat{i_l} \cdots i_{p+2}}$$가 정확히 두 번, 부호만 반대로 나타나 모두 상쇄되기 때문이다. 따라서 $$C^\bullet(\mathfrak{U}, \mathcal{F})$$는 cochain complex를 이룬다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> **Čech cohomology<sub>체흐 코호몰로지</sub>** $$\check{H}^p(\mathfrak{U}, \mathcal{F})$$를 cohomology of Čech complex로 정의한다:

$$\check{H}^p(\mathfrak{U}, \mathcal{F}) = H^p(C^\bullet(\mathfrak{U}, \mathcal{F}))$$

</div>

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> $$p = 0$$일 때를 살펴보자. Čech complex의 정의에 의하여 $$C^0(\mathfrak{U}, \mathcal{F}) = \prod_i \mathcal{F}(U_i)$$이고, $$C^0$$에서 $$C^1$$로의 coboundary map은

$$(ds)_{ij} = s_j\vert_{U_i \cap U_j} - s_i\vert_{U_i \cap U_j}$$

이다. 따라서

$$\check{H}^0(\mathfrak{U}, \mathcal{F}) = \ker(d: C^0 \to C^1) = \{(s_i) \in \prod_i \mathcal{F}(U_i) : s_i\vert_{U_i \cap U_j} = s_j\vert_{U_i \cap U_j} \text{ for all } i, j\}$$

이다. Sheaf의 gluing condition ([\[위상수학\] §층, ⁋정의 1](/ko/math/topology/sheaves#def1))에 의해 이러한 section들의 family는 정확히 $$X$$ 전체 위에서의 section, 즉 $$\Gamma(X, \mathcal{F})$$와 일치한다. 즉, $$\check{H}^0(\mathfrak{U}, \mathcal{F}) = H^0(X, \mathcal{F})$$이며 이는 open cover의 선택과 무관하다.

</div>

<div class="example" markdown="1">

<ins id="ex4">**예시 4**</ins> $$p = 1$$일 때를 생각하자. 1-cochain은 각 $$U_i \cap U_j$$ 위의 section $$s_{ij} \in \mathcal{F}(U_i \cap U_j)$$들의 모임이며, 1-cocycle은 cocycle condition

$$s_{ij} + s_{jk} = s_{ik} \quad\text{on } U_i \cap U_j \cap U_k$$

을 만족하는 것들이다. 한편 1-coboundary는 0-cochain $$(t_i)$$로부터 유도되는 것, 즉 $$s_{ij} = t_j\vert_{U_i \cap U_j} - t_i\vert_{U_i \cap U_j}$$의 꼴이다.

따라서 $$\check{H}^1(\mathfrak{U}, \mathcal{F})$$는 "각각의 overlap 위에서 section이 주어져 있고, 세 개 이상의 열린집합이 겹치는 곳에서는 이 section들이 compatible하지만, 이를 하나의 전역 section으로 이어붙일 수는 없는" 데이터들의 모임을 coboundary에 의한 동치관계로 나눈 것이다. 이는 $$\mathcal{F}$$의 **torsor** (또는 principal homogeneous space)를 분류한다. 예를 들어, 만약 $$\mathcal{F} = \mathcal{O}_X$$라면 $$\check{H}^1(\mathfrak{U}, \mathcal{O}_X)$$는 $$X$$의 위상이 만들어내는 "함수의 이음새 불일치"를 측정하는 양이다.

</div>

## Refinement와 Direct Limit

지금까지 우리는 하나의 open cover $$\mathfrak{U}$$에 대하여 Čech cohomology $$\check{H}^p(\mathfrak{U}, \mathcal{F})$$를 정의하였다. 그러나 일반적으로 서로 다른 open cover는 서로 다른 Čech cohomology를 줄 수 있다. 가령 하나의 열린집합 $$U_0 = X$$으로 이루어진 cover에서는 모든 교집합이 $$X$$이므로 $$\check{H}^p$$가 $$p = 0$$에서만 0이 아닌 값을 갖는다. 더 조밀한 cover를 사용할수록 더 많은 위상적 정보를 포착할 수 있으므로, 우리는 open cover들 사이의 관계를 규명하고 모든 open cover에 대한 정보를 종합할 필요가 있다.

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> Open cover $$\mathfrak{V} = \{V_j\}$$가 $$\mathfrak{U} = \{U_i\}$$의 **refinement**라는 것은 각 $$j$$에 대해 $$V_j \subseteq U_{\tau(j)}$$인 함수 $$\tau: J \to I$$가 존재하는 것이다.

</div>

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> Refinement $$\mathfrak{V} \preceq \mathfrak{U}$$에 대해 natural map $$\check{H}^p(\mathfrak{U}, \mathcal{F}) \to \check{H}^p(\mathfrak{V}, \mathcal{F})$$가 존재한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Refinement map $$\tau: J \to I$$가 주어지면, $$\tau$$를 사용하여 Čech complex 사이의 map을 정의할 수 있다:

$$\rho_{\mathfrak{V}\mathfrak{U}}: C^p(\mathfrak{U}, \mathcal{F}) \to C^p(\mathfrak{V}, \mathcal{F}), \quad (\rho_{\mathfrak{V}\mathfrak{U}}\alpha)_{j_0 \cdots j_p} = \alpha_{\tau(j_0) \cdots \tau(j_p)}\vert_{V_{j_0 \cdots j_p}}$$

이 map이 differential과 commute함을 확인하자. $$\alpha \in C^p(\mathfrak{U}, \mathcal{F})$$에 대하여

$$(d(\rho\alpha))_{j_0 \cdots j_{p+1}} = \sum_{k=0}^{p+1} (-1)^k (\rho\alpha)_{j_0 \cdots \hat{j_k} \cdots j_{p+1}} = \sum_{k=0}^{p+1} (-1)^k \alpha_{\tau(j_0) \cdots \widehat{\tau(j_k)} \cdots \tau(j_{p+1})}$$

이다. 한편 $$\rho(d\alpha)$$의 같은 성분은 $$d\alpha$$의 $$\tau(j_0), \ldots, \tau(j_{p+1})$$ 성분이 되는데, 만일 $$\tau(j_0), \ldots, \tau(j_{p+1})$$ 중에 중복이 없다면 이는 위와 동일하다. 중복이 있는 경우, 예를 들어 $$\tau(j_a) = \tau(j_b)$$라면 $$(d\alpha)_{\tau(j_0) \cdots \tau(j_{p+1})} = 0$$이고 $$(d(\rho\alpha))_{j_0 \cdots j_{p+1}}$$도 alternating sum의 성질에 의해 0이 되어 양쪽이 일치한다. 따라서 $$\rho$$는 differential과 commute하며 cohomology로 내려온다.

다른 refinement map $$\tau': J \to I$$를 선택하더라도, $$\rho_\tau - \rho_{\tau'}$$가 chain homotopic임을 보일 수 있으므로 cohomology에서 같은 map을 유도한다.

</details>

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> **Čech cohomology of $$X$$**를 모든 open cover에 대한 direct limit로 정의한다:

$$\check{H}^p(X, \mathcal{F}) = \varinjlim_{\mathfrak{U}} \check{H}^p(\mathfrak{U}, \mathcal{F})$$

</div>

Direct limit을 취하는 것은 open cover를 점점 더 조밀하게 만들면서 cohomology 정보를 "모두 합친다"는 의미이다. [명제 6](#prop6)에 의해 refinement 관계는 cohomology 사이의 map을 유도하므로, 이들로 이루어진 directed system의 direct limit을 취할 수 있다. 특히 이 direct limit은 $$p = 0$$에서는 $$H^0(X, \mathcal{F})$$와 일치한다. 왜냐하면 임의의 open cover에 대해 $$\check{H}^0(\mathfrak{U}, \mathcal{F}) = \Gamma(X, \mathcal{F})$$이므로 direct limit도 같은 값이 되기 때문이다.

## Čech와 Sheaf Cohomology의 비교

<div class="definition" markdown="1">

<ins id="def8">**정의 8 (Acyclic)**</ins> Sheaf $$\mathcal{F}$$가 **acyclic**이라는 것은 모든 $$i > 0$$에 대해 $$H^i(X, \mathcal{F}) = 0$$인 것이다. 예를 들어 **flasque sheaf**, 즉 임의의 열린집합 $$V \subseteq U$$에 대해 제한 사상 $$\mathcal{F}(U) \to \mathcal{F}(V)$$가 surjective인 sheaf는 acyclic이다. Injective sheaf 역시 항상 flasque이므로 acyclic이다. 대수기하학에서 특히 중요한 것은 quasi-coherent sheaf가 affine scheme 위에서 acyclic이라는 사실이다.

</div>

이제 Čech cohomology와 sheaf cohomology ([§Sheaf Cohomology, ⁋정의 1](/ko/math/algebraic_geometry/sheaf_cohomology#def1)) 사이의 관계를 살펴본다. 핵심 도구는 **double complex**와 거기서 유도되는 **spectral sequence**이다.

Double complex $$C^{\bullet,\bullet}$$는 두 방향의 differential $$d_h: C^{p,q} \to C^{p+1,q}$$와 $$d_v: C^{p,q} \to C^{p,q+1}$$를 갖는 이중 graded 대상으로, $$d_h^2 = d_v^2 = 0$$이며 $$d_h d_v + d_v d_h = 0$$을 만족한다. 우리의 상황에서는 $$C^{p,q} = C^p(\mathfrak{U}, \mathcal{I}^q)$$로 설정하는데, 여기서 $$\mathcal{I}^\bullet$$은 $$\mathcal{F}$$의 injective resolution이다. 즉, 첫 번째 방향은 Čech complex의 방향이고, 두 번째 방향은 injective resolution의 방향이다.

Double complex에는 두 가지 자연스러운 filtration이 존재한다. 첫 번째는 첫 번째 인덱스 $$p$$에 의한 filtration으로, 이로부터 얻어지는 spectral sequence는 먼저 $$q$$-방향(=sheaf 방향)으로 cohomology를 취한 후 $$p$$-방향(=Čech 방향)으로 계산한다. 두 번째는 $$q$$에 의한 filtration으로, 반대로 먼저 Čech 방향으로 cohomology를 취한 후 sheaf 방향으로 계산한다. 두 spectral sequence는 동일한 total complex의 cohomology로 수렴하며, 이 사실이 Čech cohomology와 sheaf cohomology를 연결하는 열쇠가 된다.

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> Natural map $$\check{H}^p(X, \mathcal{F}) \to H^p(X, \mathcal{F})$$가 존재한다. 이 map은 $$p = 0, 1$$에서는 항상 isomorphism이지만, $$p \geq 2$$에서는 일반적으로 surjection이 아닐 수 있으며, injective도 아닐 수 있다. 다만 paracompact Hausdorff 공간에서는 모든 degree에서 isomorphism이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

우리는 double complex $$C^{p,q} = \check{C}^p(\mathfrak{U}, \mathcal{I}^q)$$를 구성한다. 여기서 $$\mathcal{F} \to \mathcal{I}^\bullet$$은 $$\mathcal{F}$$의 injective resolution이고, $$\check{C}^p(\mathfrak{U}, -)$$는 Čech complex의 $$p$$번째 성분이다. Horizontal differential은 Čech coboundary $$d_h$$이고, vertical differential은 injective resolution의 differential $$d_v$$이다.

**두 번째 filtration(q에 의한 filtration):** 먼저 vertical 방향, 즉 각 $$p$$에 대해 $$\mathcal{I}^\bullet$$의 방향으로 cohomology를 취한다:

$${''}E_1^{p,q} = H^q(\check{C}^p(\mathfrak{U}, \mathcal{I}^\bullet))$$

각 $$p$$에 대해 $$\check{C}^p(\mathfrak{U}, \mathcal{I}^\bullet)$$은 $$\mathcal{I}^\bullet$$을 제한해서 얻은 complex의 곱이므로, $$E_1$$ 페이지의 $$p$$-번째 열은 $$\prod_{i_0 < \cdots < i_p} \mathcal{I}^\bullet(U_{i_0 \cdots i_p})$$의 cohomology이다. 즉,

$${''}E_1^{p,q} = \prod_{i_0 < \cdots < i_p} H^q(U_{i_0 \cdots i_p}, \mathcal{I}^p)$$

이다. 그런데 $$\mathcal{I}^p$$는 injective sheaf이므로 flasque이고, flasque sheaf는 임의의 열린집합 위에서 cohomology가 소멸한다. 따라서 $$H^q(U_{i_0 \cdots i_p}, \mathcal{I}^p) = 0$$ for $$q > 0$$이며,

$${''}E_1^{p,q} = 0 \quad (q > 0), \qquad {''}E_1^{p,0} = \prod_{i_0 < \cdots < i_p} \mathcal{I}^p(U_{i_0 \cdots i_p}) = \check{C}^p(\mathfrak{U}, \mathcal{I}^p)$$

이다. 특히 $$q = 0$$일 때 $$\check{C}^p(\mathfrak{U}, \mathcal{I}^p)$$들의 column은 injective resolution $$\mathcal{I}^\bullet$$의 global section complex $$\Gamma(X, \mathcal{I}^\bullet)$$과 같으므로, 이 spectral sequence는 $$E_2$$ 페이지에서 degenerate하여

$$H^n(\mathrm{Tot}) \cong {''}E_2^{0,n} = H^n(\Gamma(X, \mathcal{I}^\bullet)) = H^n(X, \mathcal{F})$$

을 준다.

**첫 번째 filtration(p에 의한 filtration):** 반대로 horizontal 방향, 즉 각 $$q$$에 대해 Čech 방향으로 먼저 cohomology를 취한다:

$${'}E_1^{p,q} = H^p(\check{C}^\bullet(\mathfrak{U}, \mathcal{I}^q)) = \check{H}^p(\mathfrak{U}, \mathcal{I}^q)$$

Injective sheaf $$\mathcal{I}^q$$는 flasque이고, flasque sheaf에 대해서는 $$\check{H}^p(\mathfrak{U}, \mathcal{I}^q) = 0$$ for $$p > 0$$이며 $$\check{H}^0(\mathfrak{U}, \mathcal{I}^q) = \Gamma(X, \mathcal{I}^q)$$이다. 따라서

$${'}E_1^{p,q} = 0 \quad (p > 0), \qquad {'}E_1^{0,q} = \Gamma(X, \mathcal{I}^q)$$

이며, 이 spectral sequence 역시 $$E_2$$에서 degenerate하여 동일한 결과 $$H^n(\mathrm{Tot}) \cong H^n(X, \mathcal{F})$$를 준다.

**Natural map의 구성:** 이제 $$\check{C}^\bullet(\mathfrak{U}, \mathcal{F})$$에서 total complex로의 map을 정의한다. $$\mathcal{F} \to \mathcal{I}^0$$로의 inclusion에 의해 $$\check{C}^p(\mathfrak{U}, \mathcal{F}) \to \check{C}^p(\mathfrak{U}, \mathcal{I}^0) \hookrightarrow \mathrm{Tot}^p$$가 주어지며, 이것이 cohomology로 내려온다. Direct limit을 취하면 $$\check{H}^p(X, \mathcal{F}) \to H^p(X, \mathcal{F})$$를 얻는다. □

</details>

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10 (Leray)**</ins> Open cover $$\mathfrak{U} = \{U_i\}$$에 대해 $$U_{i_0 \cdots i_p}$$에서 $$\mathcal{F}$$가 acyclic (즉 $$H^{>0}(U_{i_0 \cdots i_p}, \mathcal{F}) = 0$$)이면:

$$\check{H}^p(\mathfrak{U}, \mathcal{F}) \cong H^p(X, \mathcal{F})$$

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

명제 10의 증명은 명제 9와 동일한 double complex를 사용하지만, acyclic 조건에 의해 한쪽 filtration에서 더 강한 결론을 얻는다. 구체적으로, 명제 9에서는 두 filtration 모두 injective sheaf의 flasque 성질을 이용하여 degenerate시켰다면, 여기서는 acyclic 조건을 사용하여 한쪽 filtration에서 Čech cohomology를 직접 얻는다.

명제 9의 증명에서 구성한 double complex $$C^{p,q} = \check{C}^p(\mathfrak{U}, \mathcal{I}^q)$$를 다시 살펴보자. 여기서 $$\mathcal{I}^\bullet$$은 $$\mathcal{F}$$의 injective resolution이다.

**두 번째 filtration(q에 의한 filtration):** 먼저 vertical 방향, 즉 각 $$p$$에 대해 $$\mathcal{I}^\bullet$$의 방향으로 cohomology를 취한다:

$${''}E_1^{p,q} = H^q(\check{C}^p(\mathfrak{U}, \mathcal{I}^\bullet))$$
각 $$p$$에 대해 $$\check{C}^p(\mathfrak{U}, \mathcal{I}^\bullet)$$은 $$\mathcal{I}^\bullet$$을 제한해서 얻은 complex의 곱이므로, $$E_1$$ 페이지의 $$p$$-번째 열은 $$\prod_{i_0 < \cdots < i_p} \mathcal{I}^\bullet(U_{i_0 \cdots i_p})$$의 cohomology이다. 즉,

$${''}E_1^{p,q} = \prod_{i_0 < \cdots < i_p} H^q(U_{i_0 \cdots i_p}, \mathcal{F})$$
이다. 여기서 **acyclic 조건**을 사용한다: 모든 유한 교집합 $$U_{i_0 \cdots i_p}$$에서 $$\mathcal{F}$$가 acyclic이므로 $$H^q(U_{i_0 \cdots i_p}, \mathcal{F}) = 0$$ for $$q > 0$$이다. 따라서

$${''}E_1^{p,q} = 0 \quad (q > 0), \qquad {''}E_1^{p,0} = \prod_{i_0 < \cdots < i_p} \mathcal{F}(U_{i_0 \cdots i_p}) = \check{C}^p(\mathfrak{U}, \mathcal{F})$$
이 spectral sequence는 $$E_2$$에서 degenerate하여

$$H^n(\mathrm{Tot}) \cong {''}E_2^{n,0} = \check{H}^n(\mathfrak{U}, \mathcal{F})$$

을 준다.

**첫 번째 filtration(p에 의한 filtration):** 반대로 horizontal 방향으로 먼저 cohomology를 취하면

$${'}E_1^{p,q} = \check{H}^p(\mathfrak{U}, \mathcal{I}^q)$$

이다. Injective sheaf $$\mathcal{I}^q$$는 flasque이고, flasque sheaf에 대해서는 $$\check{H}^p(\mathfrak{U}, \mathcal{I}^q) = 0$$ for $$p > 0$$이며 $$\check{H}^0(\mathfrak{U}, \mathcal{I}^q) = \Gamma(X, \mathcal{I}^q)$$이다. 따라서 $$'E_1^{p,q} = 0$$ for $$p > 0$$이고 $$'E_1^{0,q} = \Gamma(X, \mathcal{I}^q)$$이며, 이 spectral sequence 역시 $$E_2$$에서 degenerate하여

$$H^n(\mathrm{Tot}) \cong {'}E_2^{0,n} = H^n(\Gamma(X, \mathcal{I}^\bullet)) = H^n(X, \mathcal{F})$$

을 준다.

두 spectral sequence는 동일한 total complex의 cohomology를 계산하므로

$$\check{H}^n(\mathfrak{U}, \mathcal{F}) \cong H^n(\mathrm{Tot}) \cong H^n(X, \mathcal{F})$$

이다. □

</details>

<div class="proposition" markdown="1">

<ins id="cor11">**따름정리 11**</ins> Separated scheme $$X$$ 위의 quasi-coherent sheaf $$\mathcal{F}$$와 affine open cover $$\mathfrak{U}$$에 대해:

$$\check{H}^p(\mathfrak{U}, \mathcal{F}) \cong H^p(X, \mathcal{F})$$

</div>

이는 [명제 10](#prop10)의 직접적인 따름정리이다. Affine scheme $$U = \operatorname{Spec} A$$ 위에서 quasi-coherent sheaf $$\mathcal{F} = \widetilde{M}$$의 cohomology는 모두 0이므로(즉 $$H^i(U, \mathcal{F}) = 0$$ for $$i > 0$$), [명제 10](#prop10)의 acyclic 조건을 확인하려면 affine open cover의 모든 유한 교집합이 다시 affine scheme이면 충분하다. Separated scheme에서는 두 affine 열린집합의 교집합이 다시 affine이며(이는 diagonal $$\Delta_X \hookrightarrow X \times X$$가 closed immersion이라는 사실과 동치이다), 따라서 임의의 유한 개의 affine 열린집합의 교집합도 inductively affine이 되어 acyclic 조건이 자동으로 충족된다. 이 사실은 대수기하학에서 Čech cohomology가 sheaf cohomology의 실질적인 계산 도구로 널리 사용되는 이유이다.

## 예시: Circle 위의 Constant Sheaf

지금까지의 이론을 구체적인 계산 예시로 확인해보자. 가장 고전적인 예시는 circle $$S^1$$ 위에서의 constant sheaf $$\underline{\mathbb{Z}}$$의 Čech cohomology를 계산하는 것이다. 이 예시는 Čech complex의 작동 방식을 직접적으로 보여주며, 그 결과가 우리의 위상적 직관과 일치한다는 것을 확인할 수 있다.

<div class="example" markdown="1">

<ins id="ex12">**예시 12 ($$S^1$$)**</ins> Circle $$S^1$$을 두 개의 열린 호 $$U_1, U_2$$로 cover하자. $$U_1 \cap U_2$$는 두 개의 연결성분 $$V_1, V_2$$를 갖는다.

Constant sheaf $$\underline{\mathbb{Z}}$$에 대해 Čech complex를 계산하자. 먼저 $$C^0 = \mathcal{F}(U_1) \times \mathcal{F}(U_2) = \mathbb{Z} \times \mathbb{Z}$$이다. $$C^1 = \mathcal{F}(U_1 \cap U_2) = \mathcal{F}(V_1) \times \mathcal{F}(V_2) = \mathbb{Z} \times \mathbb{Z}$$이다. Coboundary map $$d: C^0 \to C^1$$은

$$d(s_1, s_2) = s_2\vert_{U_1 \cap U_2} - s_1\vert_{U_1 \cap U_2} = (s_2 - s_1, s_2 - s_1)$$

이다(여기서 $$V_1, V_2$$ 각각에서 $$s_2 - s_1$$의 값이 같은 이유는 $$U_1, U_2$$가 각각 연결되어 있어 constant sheaf의 section이 각각 하나의 정수로 결정되기 때문이다).

이제 각 cohomology group을 계산한다.

- **$$\check{H}^0(\mathfrak{U}, \underline{\mathbb{Z}})$$**: $$\ker(d) = \{(s_1, s_2) : s_1 = s_2\} \cong \mathbb{Z}$$. 이것은 $$S^1$$ 전체 위에서의 상수함수이며, $$\Gamma(S^1, \underline{\mathbb{Z}}) \cong \mathbb{Z}$$와 일치한다.

- **$$\check{H}^1(\mathfrak{U}, \underline{\mathbb{Z}})$$**: 1-cocycle은 $$(a, b) \in \mathbb{Z} \times \mathbb{Z}$$이다. Coboundary는 $$d(s_1, s_2) = (s_2 - s_1, s_2 - s_1)$$의 꼴이므로, cocycle $$(a, b)$$와 $$(a', b')$$이 같은 cohomology class에 속할 필요충분조건은 $$a - a' = b - b'$$인 것이다. 따라서 invariant는 차이 $$a - b \in \mathbb{Z}$$이고, $$\check{H}^1(\mathfrak{U}, \underline{\mathbb{Z}}) \cong \mathbb{Z}$$이다.

이 결과 $$\check{H}^1(S^1, \mathbb{Z}) \cong \mathbb{Z}$$는 $$S^1$$의 "빈 구멍"이 하나 있다는 위상적 사실을 cohomology가 정확히 포착하고 있음을 보여준다. 일반적으로 $$H^1(S^1, \mathbb{Z}) \cong \mathbb{Z}$$와 일치한다.

</div>


## Application: Line Bundle의 분류

앞서 우리는 line bundle이 transition function $$g_{ij} \in \mathcal{O}_X^\ast(U_i \cap U_j)$$들로 결정된다는 것을 보았다 ([§선다발과 벡터다발, ⁋명제 2](/ko/math/algebraic_geometry/line_bundles#prop2)). Transition function들은 cocycle condition $$g_{ij}g_{jk} = g_{ik}$$을 만족하는데, 이는 multiplicative notation으로 쓴 Čech 1-cocycle condition에 정확히 해당한다. 또한 line bundle의 isomorphism은 각 $$U_i$$ 위에서의 함수 $$h_i \in \mathcal{O}_X^\ast(U_i)$$에 의해 $$g_{ij} \mapsto h_i g_{ij} h_j^{-1}$$로 transition function이 변하는 것이므로, 이 역시 Čech 1-coboundary에 의한 동치관계와 일치한다. 즉, line bundle의 isomorphism class는 $$\check{H}^1(X, \mathcal{O}_X^\ast)$$의 원소와 자연스럽게 대응된다.

이 관찰을 엄밀하게 정리하면 다음을 얻는다. 여기서 주의할 점은 $$\mathcal{O}_X^\ast$$가 곱셈적 구조를 갖는 sheaf of (abelian) groups이므로, Čech cohomology에서 coboundary 관계가 덧셈적이 아닌 곱셈적으로 표현된다는 것이다. 구체적으로 1-coboundary는 $$(g_{ij}) = (h_i \cdot h_j^{-1})$$의 꼴이다.

<div class="proposition" markdown="1">

<ins id="prop13">**명제 13**</ins> $$\check{H}^1(X, \mathcal{O}_X^\ast) \cong \operatorname{Pic}(X)$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

우선 $$\check{H}^1(X, \mathcal{O}_X^\ast)$$에서 $$\operatorname{Pic}(X)$$로의 map을 정의한다. Čech 1-cocycle $$(g_{ij}) \in \check{Z}^1(\mathfrak{U}, \mathcal{O}_X^\ast)$$가 주어지면, 이를 transition function으로 하는 line bundle $$\mathcal{L}$$을 구성한다. 구체적으로, 각 $$U_i$$ 위에서는 trivial bundle $$U_i \times \mathbb{A}^1$$을 잡고, $$U_i \cap U_j$$ 위에서는 $$(p, t) \mapsto (p, g_{ij}(p)t)$$으로 접착한다. Cocycle condition $$g_{ij}g_{jk} = g_{ik}$$에 의해 이 접착이 consistent하므로 well-defined line bundle이 얻어진다.

Coboundary에 의해 동치인 두 cocycle $$g_{ij}^{\mathcal{L}} = h_i g_{ij}^{\mathcal{M}} h_j^{-1}$$이 주어지면, 대응하는 두 line bundle 사이의 isomorphism을 $$\varphi_i: \mathcal{L}\vert_{U_i} \to \mathcal{M}\vert_{U_i}$$, $$v \mapsto h_i^{-1} v$$로 정의한다. 그러면 $$\varphi_i$$와 $$\varphi_j$$가 $$U_i \cap U_j$$에서 compatible임은

$$g_{ij}^{\mathcal{M}} \cdot \varphi_j(v) = g_{ij}^{\mathcal{M}} h_j^{-1} v = h_i^{-1} (h_i g_{ij}^{\mathcal{M}} h_j^{-1}) v = h_i^{-1} g_{ij}^{\mathcal{L}} v = \varphi_i(g_{ij}^{\mathcal{L}} v)$$

에서 확인된다. 따라서 map $$\check{H}^1(\mathfrak{U}, \mathcal{O}_X^\ast) \to \operatorname{Pic}(X)$$가 well-defined이다.

역으로, 임의의 line bundle $$\mathcal{L}$$은 ([§선다발과 벡터다발, ⁋정의 1](/ko/math/algebraic_geometry/line_bundles#def1))에 의해 적당한 open cover $$\mathfrak{U}$$ 위에서 transition function $$g_{ij}$$로 표현되며, 이는 Čech 1-cocycle을 이룬다. Line bundle isomorphism은 정확히 coboundary에 의한 동치관계에 해당하므로, 이 map의 kernel은 coboundary들이다. 따라서 $$\check{H}^1(\mathfrak{U}, \mathcal{O}_X^\ast) \to \operatorname{Pic}(X)$$는 injective이다.

Direct limit을 취하면 $$\check{H}^1(X, \mathcal{O}_X^\ast) \cong \operatorname{Pic}(X)$$를 얻는다.

</details>

이 명제는 line bundle의 기하학적 분류 문제가 cohomology의 대수적 계산 문제로 번역됨을 보여준다. 가령 $$\operatorname{Pic}(X)$$의 원소를 찾는 문제는 이제 $$\mathcal{O}_X^\ast$$-valued Čech 1-cocycle을 분류하는 문제가 되며, 이는 구체적인 계산이 가능한 형태이다.

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[God]** R. Godement, *Topologie algébrique et théorie des faisceaux*, Hermann, 1958.
