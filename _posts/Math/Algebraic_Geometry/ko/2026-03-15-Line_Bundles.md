---
title: "선형 꾸러미 (Line Bundles)"
excerpt: "Line bundles on algebraic varieties"

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/line_bundles
sidebar:
    nav: "algebraic_geometry-ko"

header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Line_Bundles.png
    overlay_filter: 0.5

date: 2026-03-12
last_modified_at: 2026-03-15
weight: 10

---

선형 꾸러미(line bundle)는 다양체 위의 "반지" (ring)를 취급하는 객체이다. 즉, 다양체 위의 각 점에서 스칼라배를 할 수 있는 공간에 구조를 부여한다. 선형 꾸러미는 Picard group를 정의하는 핵심 도구이며, divisor와 밀접한 관계가 있다. 이 절에서 우리는 선형 꾸러미의 정의, Picard group, 그리고 divisor와의 연결을 살펴볼 것이다.

## 정의

선형 꾸러미의 기본 아이디어는 다양체 위의 "local trivial line bundle"를 정의하는 것이다. 아핀다양체 $$X$$에서 각 점 $$p$$ 근처에서는 line bundle이 "flat" (trivial)하게 생긴다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 다양체 $$X$$ 위의 *line bundle* $$\mathcal{L}$$는 다음과 같은 commutative diagram을 만족하는 데이터이다.\n\n$$\begin{array}{ccc}\mathcal{L} & \xrightarrow{\pi} & X\\\ni & \nearrow & \downarrow \\ \mathbb{A}^1 & \xrightarrow{\text{flat}} & X\end{array}$$\n\n여기서 $$\pi$$는 projection이고, 각 $$p \in X$$에 대해 fiber $$\pi^{-1}(p) \cong \mathbb{A}^1$$이며, local trivializations $$\phi_i: \pi^{-1}(U_i) \to U_i \times \mathbb{A}^1$$이 존재한다.\n\n</div>

기하학적으로, line bundle은 다양체 위의 "torsor" (translation)로 생각할 수 있다. 각 fiber는 1차원 vector space이고, cross-section은 "regular function"의 일종이다. 이는 다양체 위의 "vector bundle"의 가장 기본적인 경우이다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> 선형 꾸러미 $$\mathcal{L}$$의 fiber $$\mathcal{L}_p = \pi^{-1}(p)$$는 1차원 vector space이며, $$\mathcal{L}_p \cong \mathbb{A}^1$$이다.\n\n</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Line bundle의 정의에서 fiber는 $$\mathbb{A}^1$$과 isomorphic이다. Local trivialization $$\phi_i$$ restricts to isomorphism $$\pi^{-1}(U_i) \cap \mathcal{L}_p \to \{p\} \times \mathbb{A}^1 \cong \mathbb{A}^1$$ on each fiber. Thus each fiber is a 1-dimensional vector space.

</details>

## Tensor Product

두 line bundle $$\mathcal{L}, \mathcal{M}$$의 tensor product $$\mathcal{L} \otimes \mathcal{M}$$도 line bundle이다. Tensor product은 fiber-wise이며, 각 fiber에서는 $$\mathcal{L}_p \otimes \mathcal{M}_p \cong \mathcal{L}_p \otimes \mathcal{M}_p \cong \mathbb{A}^1$$이다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> 두 line bundle $$\mathcal{L}, \mathcal{M}$$의 tensor product $$\mathcal{L} \otimes \mathcal{M}$$는 line bundle이다. Fiber-wise, $$\mathcal{L}_p \otimes \mathcal{M}_p \cong \mathbb{A}^1$$ for all $$p \in X$$.\n\n</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Local trivializations $$\phi_i, \psi_i$$를 사용하여 $$\mathcal{L} \otimes \mathcal{M}$$의 local trivialization을 정의할 수 있다. Fiber-wise tensor product은 1-dimensional vector space이므로, $$\mathcal{L} \otimes \mathcal{M}$$도 line bundle이다.

</details>

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> Line bundle $$\mathcal{L}$$의 dual $$\mathcal{L}^\vee = \mathcal{H}om(\mathcal{L}, \mathcal{O}_X)$$는 line bundle이다.\n\n</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Dual bundle의 fiber $$\mathcal{H}om(\mathcal{L}_p, \mathbb{A}^1) \cong \mathcal{L}_p^\vee$$도 1-dimensional vector space이므로, $$\mathcal{L}^\vee$$는 line bundle이다. Local trivializations을 사용하여 $$\mathcal{H}om(\mathcal{L}, \mathcal{O}_X)$$의 local trivialization을 정의할 수 있다.

</details>

## Picard Group

Line bundle들의 isomorphism classes는 *Picard group*을 형성한다. 이 group은 line bundle들의 tensor product에 의해 group structure를 갖는다.

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> 다양체 $$X$$ 위의 *Picard group* $$\mathrm{Pic}(X)$$는 line bundle들의 isomorphism classes에 tensor product에 의한 group structure를 부여한 것이다.\n\n</div>

기하학적으로, Picard group는 "나침반의 방향"을 측정한다. 즉, 어떤 line bundle이 기본 line bundle (trivial bundle)과 "twisted"되었는지를 측정한다. Picard group의 zero element은 trivial line bundle $$\mathcal{O}_X$$이다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> Picard group $$\mathrm{Pic}(X)$$는 abelian group이다.\n\n</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Tensor product은 commutative이므로, $$\mathrm{Pic}(X)$$도 commutative abelian group이다. Identity element은 trivial bundle $$\mathcal{O}_X$$이고, inverse는 dual bundle $$\mathcal{L}^\vee$$이다.

</details>

<div class="example" markdown="1">

<ins id="ex7">**예시 7**</ins> **Picard group의 예시들**\n\n1. $$\mathbb{A}^n$$: $$\mathrm{Pic}(\mathbb{A}^n) = 0$$. 모든 line bundle은 trivial이다.\n2. $$\mathbb{P}^n$$: $$\mathrm{Pic}(\mathbb{P}^n) \cong \mathbb{Z}$$. Hyperplane bundle $$\mathcal{O}_{\mathbb{P}^n}(1)$$ generates the group.\n3. $$X = V(xy) \subseteq \mathbb{A}^2$$: $$\mathrm{Pic}(X) = 0$$. Components $$V(x)$$와 $$V(y)$$는 trivial bundle로 연결된다.\n\n</div>

## Divisor와의 연결

Line bundle과 divisor 사이의 관계는 매우 중요하다. 각 divisor는 line bundle을 유도하고, 각 line bundle은 divisor를 유도한다.

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> 기역 다양체 $$X$$ 위의 divisor $$D$$는 line bundle $$\mathcal{L}_D$$를 유도한다.\n\n</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Effective divisor $$D = \sum_i n_i Z_i$$에서 각 component $$Z_i = V(f_i)$$는 hyperplane section의 일종이다. Local trivialization $$\{ (U_i, f_i) \}$$를 사용하여 line bundle $$\mathcal{L}_D$$를 정의할 수 있다. 이는 principal divisor에 대해 trivial bundle을 유도한다.

</details>

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> 기역 다양체 $$X$$ 위의 line bundle $$\mathcal{L}$$는 divisor $$D = \mathrm{div}(\mathcal{L})$$를 유도한다.\n\n</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Line bundle $$\mathcal{L}$$의 transition functions $$g_{ij} \in \mathcal{O}_X(U_i \cap U_j)^\ast$$에 대해, divisor $$D = \sum_{ij} v_{Z_{ij}}(g_{ij}) Z_{ij}$$를 정의한다. 여기서 $$Z_{ij} = V(g_{ij})$$은 component이다. 이 divisor는 principal divisor $$\mathrm{div}(g_{ij})$$의 합이다.

</details>

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10**</ins> Picard group $$\mathrm{Pic}(X)$$와 divisor class group $$\mathrm{Cl}(X)$$는 isomorphic하다.\n\n</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Divisor $$D$$에 associated line bundle $$\mathcal{L}_D$$를 정의하고, line bundle $$\mathcal{L}$$에 associated divisor $$\mathrm{div}(\mathcal{L})$$를 정의한다. Principal divisor에 대해 trivial bundle을 유도하므로, quotient는 isomorphic하다.

</details>

## Sections와 Degree

Line bundle $$\mathcal{L}$$의 section $$s \in H^0(X, \mathcal{L})$$는 divisor $$\mathrm{div}(s)$$를 유도한다. 이는 line bundle이 "twisted"된 정도(degree)를 나타낸다.

<div class="definition" markdown="1">

<ins id="def11">**정의 11**</ins> 기역 다양체 $$X$$ 위의 line bundle $$\mathcal{L}$$의 *degree* $$\deg \mathcal{L}$$는 다음과 같이 정의된다.\n\n$$\deg \mathcal{L} = \sum_{p \in X} \operatorname{ord}_p(\mathcal{L})$$\n\n여기서 $$\operatorname{ord}_p(\mathcal{L})$$는 line bundle의 local trivialization에서의 order.\n\n</div>

기하학적으로, degree는 line bundle이 "얼마나 많이" twisted되었는지를 측정한다. Projective space에서 hyperplane bundle $$\mathcal{O}_{\mathbb{P}^n}(1)$$은 degree 1을 가진다. Higher degree bundles는 "더 많이" twisted된다.

<div class="example" markdown="1">

<ins id="ex12">**예시 12**</ins> **Degree의 예시들**\n\n1. $$\mathbb{A}^n$$의 trivial bundle: $$\deg \mathcal{O}_{\mathbb{A}^n} = 0$$.\n2. $$\mathbb{P}^n$$의 hyperplane bundle: $$\deg \mathcal{O}_{\mathbb{P}^n}(1) = 1$$.\n3. $$\mathbb{P}^n$$의 $$k$$-times tensor: $$\deg \mathcal{O}_{\mathbb{P}^n}(k) = k$$.\n\n</div>

---\n\n**참고문헌**\n\n**[Har]** J. Harris, *Algebraic Geometry: A First Course*, Springer, 1992.\n**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.\n**[Gr]** P. Griffiths and J. Harris, *Principles of Algebraic Geometry*, Wiley, 1978.\n