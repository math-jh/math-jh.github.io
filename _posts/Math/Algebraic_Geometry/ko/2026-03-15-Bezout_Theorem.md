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
last_modified_at: 2026-03-15
weight: 24
---

## 도입

**Bézout's theorem**은 projective space 안의 두 variety의 intersection에 대한 고전적인 정리이다. 가장 간단한 형태로, $$\mathbb{P}^2$$ 안의 degree $$m$$과 $$n$$인 두 curve는 (공통 성분이 없으면) 정확히 $$mn$$개의 점에서 만난다.

이 정리는 intersection theory의 기본적인 응용이며, 많은 기하학적 결과의 기초가 된다.

## Statement

<div class="theorem" markdown="1">

<ins id="thm1">**정리 1 (Bézout's Theorem)**</ins> $$\mathbb{P}^n$$ 안의 차수 $$d_1, \ldots, d_r$$의 hypersurface $$H_1, \ldots, H_r$$이 공통 성분을 갖지 않는다면:

$$\deg(H_1 \cap \cdots \cap H_r) = d_1 \cdots d_r$$

여기서 intersection은 multiplicity를 고려한 "scheme-theoretic" intersection이다.

</div>

<div class="corollary" markdown="1">

<ins id="cor2">**따름정리 2 (Curves in $$\mathbb{P}^2$$)**</ins> $$\mathbb{P}^2$$ 안의 차수 $$m$$, $$n$$인 두 curve $$C, D$$가 공통 성분을 갖지 않으면:

$$\sum_{p \in C \cap D} i_p(C, D) = mn$$

</div>

<div class="remark" markdown="1">

<ins id="rem3">**참고 3**</ins> "공통 성분이 없다"는 조건이 중요하다. 예를 들어 $$C = D$$이면 무한히 많은 점에서 만난다.

</div>

## Examples

<div class="example" markdown="1">

<ins id="ex4">**예시 4 (Line과 Curve)**</ins> $$\mathbb{P}^2$$ 안의 차수 $$d$$ curve $$C$$와 line $$L$$을 생각하자.

- $$L$$이 $$C$$의 component가 아니면 $$|C \cap L| = d$$ (multiplicity 포함)
- 예: Cubic curve는 line과 3점에서 만남

</div>

<div class="example" markdown="1">

<ins id="ex5">**예시 5 (Two Conics)**</ins> 두 conic (degree 2 curves)은 4점에서 만난다.

예: $$C_1: x^2 + y^2 = z^2$$ (circle), $$C_2: xy = 0$$ (two lines)

$$C_1 \cap C_2$$는 4점: $$[1:0:1]$$, $$[1:0:-1]$$, $$[0:1:1]$$, $$[0:1:-1]$$

$$2 \times 2 = 4$$. ✓

</div>

<div class="example" markdown="1">

<ins id="ex6">**예시 6 (Tangent Case)**</ins> $$C: y = x^2$$와 $$L: y = 0$$을 $$\mathbb{P}^2$$에서 생각하자.

$$C \cap L$$은 원점에서 multiplicity 2로 만난다.

$$\deg C = 2$$, $$\deg L = 1$$, $$2 \times 1 = 2$$. ✓

</div>

## Proof via Chow Ring

<div class="proof" markdown="1">

<ins id="proof7">**증명 (Chow ring을 통한)**</ins>

$$\operatorname{CH}^\ast(\mathbb{P}^n) = \mathbb{Z}[H] / (H^{n+1})$$에서 degree $$d_i$$ hypersurface $$H_i$$의 class는 $$d_i H$$이다.

Intersection product:

$$[H_1] \cdot \cdots \cdot [H_r] = (d_1 H) \cdots (d_r H) = d_1 \cdots d_r \cdot H^r$$

$$H^r$$은 codimension $$r$$ linear subspace의 class이고, 그 degree는 1이다.

따라서:

$$\deg(H_1 \cap \cdots \cap H_r) = d_1 \cdots d_r$$

</div>

## Generalization

<div class="theorem" markdown="1">

<ins id="thm8">**정리 8 (General Bézout)**</ins> $$\mathbb{P}^n$$ 안의 variety $$V, W$$에 대해 (적절한 조건 하에):

$$\deg(V \cap W) = \deg(V) \cdot \deg(W)$$

</div>

<div class="example" markdown="1">

<ins id="ex9">**예시 9 ($$\mathbb{P}^3$$)**</ins> $$\mathbb{P}^3$$ 안의 two quadric surfaces $$Q_1, Q_2$$ (degree 2)의 intersection은 degree 4 curve이다.

$$Q_1 \cap Q_2$$는 elliptic curve (genus 1) 또는 rational curve의 union일 수 있다.

</div>

## Applications

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10 (Cubic Curve의 9점)**</ins> 두 cubic curve $$C_1, C_2$$가 9점 $$p_1, \ldots, p_9$$에서 만나면, 이 9점을 지나는 임의의 cubic curve는 $$C_1$$과 $$C_2$$의 linear combination이다.

</div>

<div class="corollary" markdown="1">

<ins id="cor11">**따름정리 11 (Pascal's Theorem)**</ins> Conic 위의 6점 $$p_1, \ldots, p_6$$에 대해, $$p_1 p_2$$, $$p_3 p_4$$, $$p_5 p_6$$이 collinear이면 $$p_2 p_3$$, $$p_4 p_5$$, $$p_6 p_1$$도 collinear이다.

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

<ins id="prop12">**명제 12 (Max Number of Double Points)**</ins> Degree $$d$$ plane curve가 가질 수 있는 최대 double point의 개수는 $$\binom{d-1}{2}$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Double point에서의 multiplicity는 2이다. 따라서 $$n$$개의 double point가 있으면 총 multiplicity는 $$2n$$이다.

Generic line이 curve와 $$d$$점에서 만나므로, double point를 지나는 line은 $$(d-2) + 2 = d$$점에서 만난다.

Double point들의 수가 너무 많으면 모든 double point를 지나는 curve가 존재하게 되어矛盾. 자세한 계산으로 $$\binom{d-1}{2}$$를 얻는다.

</details>

## Complex Analytic Perspective

<div class="remark" markdown="1">

<ins id="rem13">**참고 13**</ins> $$\mathbb{P}^n_\mathbb{C}$$에서 Bézout's theorem은 topological 의미를 갖는다:

$$\sum_{p \in V \cap W} i_p(V, W) = [V] \cup [W] \in H^{2n}(\mathbb{P}^n, \mathbb{Z}) \cong \mathbb{Z}$$

Cohomology class의 cup product가 intersection number를 계산한다.

</div>

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[Ful]** W. Fulton, *Intersection Theory*, Springer, 1984.
