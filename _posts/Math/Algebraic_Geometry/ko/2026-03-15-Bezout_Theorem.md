---
title: "Bézout's Theorem"
excerpt: "Bézout's theorem and its applications"

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/bezout_theorem
sidebar: 
    nav: "algebraic_geometry-ko"

header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Bezout_Theorem.png
    overlay_filter: 0.5

date: 2026-03-15
last_modified_at: 2026-03-31
weight: 21
published: false
---

## 도입

**Bézout's theorem**은 projective space 안의 두 variety의 intersection에 대한 고전적인 정리이다. 가장 간단한 형태로, $$\mathbb{P}^2$$ 안의 degree $$m$$과 $$n$$인 두 curve는 (공통 성분이 없으면) 정확히 $$mn$$개의 점에서 만난다.

이 정리는 intersection theory의 기본적인 응용이며, 많은 기하학적 결과의 기초가 된다. 본 글에서는 hypersurface의 degree와 Chow ring에서의 class ([§Chow Groups, ⁋명제 7](/ko/math/algebraic_geometry/chow_groups#prop7)), intersection multiplicity ([§Intersection Multiplicity, ⁋정의 1](/ko/math/algebraic_geometry/intersection_multiplicity#def1)), 그리고 intersection product ([§Intersection Product, ⁋명제 3](/ko/math/algebraic_geometry/intersection_product#prop3))의 개념을 사용한다.

## Statement

<div class="proposition" markdown="1">

<ins id="prop1">**명제 1 (Bézout's Theorem)**</ins> $$\mathbb{P}^n$$ 안의 차수 $$d_1, \ldots, d_r$$의 hypersurface $$H_1, \ldots, H_r$$이 공통 성분을 갖지 않는다면:

$$\deg(H_1 \cap \cdots \cap H_r) = d_1 \cdots d_r$$

여기서 intersection은 multiplicity를 고려한 "scheme-theoretic" intersection이다.

</div>

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2 (Curves in $$\mathbb{P}^2$$)**</ins> $$\mathbb{P}^2$$ 안의 차수 $$m$$, $$n$$인 두 curve $$C, D$$가 공통 성분을 갖지 않으면:

$$\sum_{p \in C \cap D} i_p(C, D) = mn$$

</div>

명제 1과 명제 2에서 "공통 성분이 없다"는 조건은 필수적이다. 예를 들어 $$C = D$$이면 두 curve는 무한히 많은 점에서 만나므로 결론이 성립하지 않는다.

## Examples

<div class="example" markdown="1">

<ins id="ex3">**예시 3 (Line과 Curve)**</ins> $$\mathbb{P}^2$$ 안의 차수 $$d$$ curve $$C$$와 line $$L$$을 생각하자.

- $$L$$이 $$C$$의 component가 아니면 $$|C \cap L| = d$$ (multiplicity 포함)
- 예: Cubic curve는 line과 3점에서 만남

</div>

<div class="example" markdown="1">

<ins id="ex4">**예시 4 (Two Conics)**</ins> 두 conic (degree 2 curves)은 4점에서 만난다.

예: $$C_1: \x^2 + \y^2 = \z^2$$ (circle), $$C_2: \x\y = 0$$ (two lines)

$$C_1 \cap C_2$$는 4점: $$[1:0:1]$$, $$[1:0:-1]$$, $$[0:1:1]$$, $$[0:1:-1]$$

$$2 \times 2 = 4$$. ✓

</div>

<div class="example" markdown="1">

<ins id="ex5">**예시 5 (Tangent Case)**</ins> $$C: \y = \x^2$$와 $$L: \y = 0$$을 $$\mathbb{P}^2$$에서 생각하자.

$$C \cap L$$은 원점에서 multiplicity 2로 만난다.

$$\deg C = 2$$, $$\deg L = 1$$, $$2 \times 1 = 2$$. ✓

</div>

## Proof via Chow Ring

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> $$\operatorname{CH}^\ast(\mathbb{P}^n) = \mathbb{Z}[H] / (H^{n+1})$$에서 degree $$d_i$$ hypersurface $$H_i$$의 class는 $$d_i H$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Degree $$d_i$$ hypersurface $$H_i$$가 주어지면, [§Chow Groups, ⁋명제 7](/ko/math/algebraic_geometry/chow_groups#prop7)에 의해 $$\operatorname{CH}^\ast(\mathbb{P}^n) = \mathbb{Z}[H]/(H^{n+1})$$이며, $$H_i$$의 class는 $$c_i H$$ 형태로 표현된다. 여기서 $$c_i$$를 결정하려면, generic hyperplane $$L$$ (class $$H$$)과 $$H_i$$의 intersection을 고려하면 된다. $$H_i$$가 degree $$d_i$$ polynomial $$f$$로 정의되고 $$L$$이 linear polynomial $$\ell$$로 정의될 때, $$(f, \ell)$$로 생성된 ideal의 variety는 $$\mathbb{P}^{n-2}$$ 안의 degree $$d_i$$ hypersurface이며, 특히 $$n = 2$$인 경우 $$|H_i \cap L| = d_i$$ (multiplicity 포함)이다. 따라서 [명제 1](#prop1)에 의해 $$H_i \cdot H = d_i$$이고, class는 $$d_i H$$가 된다.

Intersection product:

$$[H_1] \cdot \cdots \cdot [H_r] = (d_1 H) \cdots (d_r H) = d_1 \cdots d_r \cdot H^r$$

$$H^r$$은 codimension $$r$$ linear subspace의 class이고, 그 degree는 1이다.

따라서:

$$\deg(H_1 \cap \cdots \cap H_r) = d_1 \cdots d_r$$

</details>

## Generalization

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7 (General Bézout)**</ins> $$\mathbb{P}^n$$ 안의 variety $$V, W$$에 대해, $$V$$와 $$W$$가 proper intersection을 가지면:

$$\deg(V \cap W) = \deg(V) \cdot \deg(W)$$

Variety가 여러 hypersurface의 intersection으로 표현될 수 있으므로, 이 정리는 hypersurface 경우 ([명제 1](#prop1))에서 Chow ring의 multiplicativity를 통해 자연스럽게 유도된다.

</div>

<div class="example" markdown="1">

<ins id="ex8">**예시 8 ($$\mathbb{P}^3$$)**</ins> $$\mathbb{P}^3$$ 안의 two quadric surfaces $$Q_1, Q_2$$ (degree 2)의 intersection은 degree 4 curve이다.

$$Q_1 \cap Q_2$$는 elliptic curve (genus 1) 또는 rational curve의 union일 수 있다.

</div>

## Applications

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9 (Cubic Curve의 9점)**</ins> 두 cubic curve $$C_1, C_2$$가 9점 $$p_1, \ldots, p_9$$에서 만나면, 이 9점을 지나는 임의의 cubic curve는 $$C_1$$과 $$C_2$$의 linear combination이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$\mathbb{P}^2$$ 위의 cubic curve는 homogeneous degree 3 polynomial로 정의되며, $$\dim H^0(\mathbb{P}^2, \mathcal{O}(3)) = 10$$이다. 각 점 $$p_i$$를 지나는 것은 polynomial space에 하나의 linear condition을 부과하므로, 9개 점을 지나는 cubic의 공간은 codimension이 최대 9이고, 따라서 적어도 1차원이다.

$$C_1, C_2$$는 이 9점을 지나는 서로 다른 두 cubic이므로, 이 둘은 cubic space 안에서 독립적인 원소를 이룬다. 9점 조건 아래에서 cubic space는 codimension $$\leq 9$$이므로 $$C_1, C_2$$가 span하는 2차원 부분공간이 9점 조건을 만족하는 cubic의 전체 공간이다. 따라서 9점을 지나는 임의의 cubic $$C_3$$은 $$C_3 = \lambda C_1 + \mu C_2$$로 쓸 수 있다.

</details>

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10 (Pascal's Theorem)**</ins> Conic 위의 6점 $$p_1, \ldots, p_6$$에 대해, $$p_1 p_2$$, $$p_3 p_4$$, $$p_5 p_6$$이 collinear이면 $$p_2 p_3$$, $$p_4 p_5$$, $$p_6 p_1$$도 collinear이다.

</div>

<details class="proof" markdown="1">
<summary>증명 (Sketch)</summary>

Cubic curve $$C$$를 다음으로 정의하자:
$$C = \overline{p_1 p_2} \cup \overline{p_3 p_4} \cup \overline{p_5 p_6}$$

$$C$$는 conic과 9점에서 만난다 (conic 위의 6점 + 3 intersection point).

Pascal line $$L$$을 지나는 다른 cubic $$C'$$을 정의하면, Bézout에 의해 $$C$$와 $$C'$$이 같은 9점을 지나야 한다.

이로부터 결과가 따른다.

</details>

<div class="proposition" markdown="1">

<ins id="prop11">**명제 11 (Max Number of Double Points)**</ins> Degree $$d$$ plane curve가 가질 수 있는 최대 double point의 개수는 $$\binom{d-1}{2}$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Smooth degree $$d$$ curve $$C \subset \mathbb{P}^2$$의 경우, adjunction formula $$K_C = (K_{\mathbb{P}^2} \otimes \mathcal{O}(C))\vert_C$$와 genus formula $$2g - 2 = C \cdot (C + K_{\mathbb{P}^2})$$를 적용한다. $$K_{\mathbb{P}^2} = \mathcal{O}(-3)$$이고 $$[C] = dH$$이므로:

$$2g - 2 = d(d-3) \implies g = \frac{(d-1)(d-2)}{2}$$

Double point $$p$$에서 curve $$C$$가 singular하면, blow-up $$\pi: \tilde{\mathbb{P}}^2 \to \mathbb{P}^2$$에서 $$p$$를 exceptional divisor $$E$$로 교체한 strict transform $$\tilde{C}$$는 smooth curve가 된다. 특히 $$p$$가 ordinary double point (node)이면 $$\tilde{C}$$는 $$E$$와 서로 다른 두 점에서 transversally 만나고, singularity correction term $$\delta_p = 1$$이므로 arithmetic genus가 정확히 1 감소한다. 따라서 $$n$$개의 double point가 있는 curve의 (normalization의) genus는:

$$g = \frac{(d-1)(d-2)}{2} - n$$

Genus가 음수가 될 수 없으므로 $$n \leq \binom{d-1}{2}$$이다.

</details>

## Complex Analytic Perspective

<div class="proposition" markdown="1">

<ins id="prop12">**명제 12 (Topological Interpretation)**</ins> $$\mathbb{P}^n_\mathbb{C}$$에서 Bézout's theorem은 topological 의미를 갖는다:

$$\sum_{p \in V \cap W} i_p(V, W) = [V] \cup [W] \in H^{2n}(\mathbb{P}^n, \mathbb{Z}) \cong \mathbb{Z}$$

Cohomology class의 cup product가 intersection number를 계산한다. Chow ring과 cohomology ring 사이의 cycle class map $$\operatorname{cl}: \operatorname{CH}^\ast(X) \to H^{2\ast}(X, \mathbb{Z})$$가 $$\mathbb{P}^n$$에서 동형사상이므로, Chow ring에서의 intersection product 계산이 cohomology에서의 cup product로 번역된다.

</div>

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[Ful]** W. Fulton, *Intersection Theory*, Springer, 1984.
