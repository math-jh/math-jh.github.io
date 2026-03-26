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
last_modified_at: 2026-03-15
weight: 14
published: false
---

## 도입

Sheaf cohomology는 derived functor로 정의되어 추상적이며 계산하기 어렵다. **Čech cohomology**는 open cover를 사용하여 더 구체적으로 cohomology를 계산하는 방법을 제공한다.

중요한 점은 "좋은" 조건 하에서 Čech cohomology가 sheaf cohomology와 일치한다는 것이다.

## Čech Complex

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 위상공간 $$X$$의 open cover $$\mathfrak{U} = \{U_i\}_{i \in I}$$와 sheaf $$\mathcal{F}$$에 대해 **Čech complex** $$C^\bullet(\mathfrak{U}, \mathcal{F})$$를 다음과 같이 정의한다:

$$C^p(\mathfrak{U}, \mathcal{F}) = \prod_{i_0 < \cdots < i_p} \mathcal{F}(U_{i_0} \cap \cdots \cap U_{i_p})$$

Coboundary map $$d: C^p \to C^{p+1}$$은:

$$(d\alpha)_{i_0 \cdots i_{p+1}} = \sum_{k=0}^{p+1} (-1)^k \alpha_{i_0 \cdots \hat{i_k} \cdots i_{p+1}}|_{U_{i_0 \cdots i_{p+1}}}$$

</div>

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> **Čech cohomology<sub>체흐 코호몰로지</sub>** $$\check{H}^p(\mathfrak{U}, \mathcal{F})$$를 cohomology of Čech complex로 정의한다:

$$\check{H}^p(\mathfrak{U}, \mathcal{F}) = H^p(C^\bullet(\mathfrak{U}, \mathcal{F}))$$

</div>

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> $$p = 0$$일 때:

$$\check{H}^0(\mathfrak{U}, \mathcal{F}) = \{(s_i) \in \prod_i \mathcal{F}(U_i) : s_i|_{U_i \cap U_j} = s_j|_{U_i \cap U_j} \text{ for all } i, j\}$$

Sheaf의 gluing condition에 의해 이것은 $$\Gamma(X, \mathcal{F})$$와 같다.

</div>

<div class="example" markdown="1">

<ins id="ex4">**예시 4**</ins> $$p = 1$$일 때:

$$\check{H}^1(\mathfrak{U}, \mathcal{F})$$는 $$s_{ij} \in \mathcal{F}(U_i \cap U_j)$$들 중 cocycle condition $$s_{ij} + s_{jk} = s_{ik}$$를 만족하는 것들의 coboundary $$s_{ij} = t_i - t_j$$에 의한 quotient이다.

이것은 $$\mathcal{F}$$의 **torsor** (또는 principal homogeneous space)를 분류한다.

</div>

## Refinement와 Direct Limit

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> Open cover $$\mathfrak{V} = \{V_j\}$$가 $$\mathfrak{U} = \{U_i\}$$의 **refinement**라는 것은 각 $$j$$에 대해 $$V_j \subseteq U_{\tau(j)}$$인 함수 $$\tau: J \to I$$가 존재하는 것이다.

</div>

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> Refinement $$\mathfrak{V} \preceq \mathfrak{U}$$에 대해 natural map $$\check{H}^p(\mathfrak{U}, \mathcal{F}) \to \check{H}^p(\mathfrak{V}, \mathcal{F})$$가 존재한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Refinement map $$\tau: J \to I$$가 주어지면, $$\tau$$를 사용하여 Čech complex 사이의 map을 정의할 수 있다:

$$\rho_{\mathfrak{V}\mathfrak{U}}: C^p(\mathfrak{U}, \mathcal{F}) \to C^p(\mathfrak{V}, \mathcal{F}), \quad (\rho_{\mathfrak{V}\mathfrak{U}}\alpha)_{j_0 \cdots j_p} = \alpha_{\tau(j_0) \cdots \tau(j_p)}|_{V_{j_0 \cdots j_p}}$$

이 map이 differential과 commute하므로 cohomology로 내려온다. 다른 refinement map의 선택은 cohomology에서 같은 map을 유도한다.

</details>

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> **Čech cohomology of $$X$$**를 모든 open cover에 대한 direct limit로 정의한다:

$$\check{H}^p(X, \mathcal{F}) = \varinjlim_{\mathfrak{U}} \check{H}^p(\mathfrak{U}, \mathcal{F})$$

</div>

## Čech와 Sheaf Cohomology의 비교

<div class="definition" markdown="1">

<ins id="def8">**정의 8 (Acyclic)**</ins> Sheaf $$\mathcal{F}$$가 **acyclic**이라는 것은 모든 $$i > 0$$에 대해 $$H^i(X, \mathcal{F}) = 0$$인 것이다. 예를 들어 flasque sheaf, injective sheaf, fine sheaf는 모두 acyclic이다.

</div>

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> Natural map $$\check{H}^p(X, \mathcal{F}) \to H^p(X, \mathcal{F})$$가 존재한다.

</div>

<details class="proof" markdown="1">
<summary>증명 (Sketch)</summary>

이 map은 Čech complex에서 injective resolution으로 가는 canonical map에서 유도된다. 구체적으로, $$\mathcal{F}$$의 injective resolution $$\mathcal{F} \to \mathcal{I}^\bullet$$을 선택하면, Čech complex $$C^\bullet(\mathfrak{U}, \mathcal{F})$$에서 double complex $$C^\bullet(\mathfrak{U}, \mathcal{I}^\bullet)$$를 구성할 수 있다. 이 double complex의 두 spectral sequence가 각각 Čech cohomology와 sheaf cohomology로 수렴하며, 이로부터 natural map이 존재함을 알 수 있다.

</details>

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10 (Leray)**</ins> Open cover $$\mathfrak{U} = \{U_i\}$$에 대해 $$U_{i_0 \cdots i_p}$$에서 $$\mathcal{F}$$가 acyclic (즉 $$H^{>0}(U_{i_0 \cdots i_p}, \mathcal{F}) = 0$$)이면:

$$\check{H}^p(\mathfrak{U}, \mathcal{F}) \cong H^p(X, \mathcal{F})$$

</div>

<details class="proof" markdown="1">
<summary>증명 (Sketch)</summary>

Acyclic 조건 하에서 앞의 증명에서 언급한 double complex의 spectral sequence가 $$E_2$$ 페이지에서 degenerate한다. 이는 cover의 교집합에서 higher cohomology가 사라지기 때문이다. 따라서 Čech cohomology가 derived functor cohomology와 동형이다.

</details>

<div class="corollary" markdown="1">

<ins id="cor11">**따름정리 11**</ins> Quasi-coherent sheaf $$\mathcal{F}$$ on scheme $$X$$와 affine open cover $$\mathfrak{U}$$에 대해:

$$\check{H}^p(\mathfrak{U}, \mathcal{F}) \cong H^p(X, \mathcal{F})$$

(Affine scheme에서 quasi-coherent sheaf는 acyclic이므로)

</div>

## 예시: Circle 위의 Constant Sheaf

<div class="example" markdown="1">

<ins id="ex12">**예시 12 ($$S^1$$)**</ins> Circle $$S^1$$을 두 개의 열린 호 $$U_1, U_2$$로 cover하자. $$U_1 \cap U_2$$는 두 개의 연결성분 $$V_1, V_2$$를 갖는다.

Constant sheaf $$\underline{\mathbb{Z}}$$에 대해:

- $$\check{H}^0(\mathfrak{U}, \underline{\mathbb{Z}}) = \mathbb{Z}$$
- $$\check{H}^1(\mathfrak{U}, \underline{\mathbb{Z}}) = \mathbb{Z}$$

이것은 $$H^1(S^1, \mathbb{Z}) \cong \mathbb{Z}$$와 일치한다.

</div>

## Application: Line Bundle의 분류

<div class="proposition" markdown="1">

<ins id="prop13">**명제 13**</ins> $$\check{H}^1(X, \mathcal{O}_X^\ast) \cong \operatorname{Pic}(X)$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명 (Sketch)</summary>

Line bundle $$L$$은 open cover $$\{U_i\}$$ 위에서 transition function $$g_{ij} \in \mathcal{O}_X^\ast(U_i \cap U_j)$$로 표현된다. Cocycle condition:

$$g_{ij} g_{jk} = g_{ik} \quad \text{on } U_i \cap U_j \cap U_k$$

이것이 정확히 Čech 1-cocycle condition이다. Isomorphism은 coboundary $$g_{ij} = h_i h_j^{-1}$$에 의해 주어지므로:

$$\operatorname{Pic}(X) \cong \check{H}^1(X, \mathcal{O}_X^\ast)$$

</details>

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[God]** R. Godement, *Topologie algébrique et théorie des faisceaux*, Hermann, 1958.
