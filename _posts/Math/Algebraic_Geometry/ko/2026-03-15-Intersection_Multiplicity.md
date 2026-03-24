---
title: "Intersection Multiplicity"
excerpt: "Intersection multiplicity and Bezout's theorem for curves"

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/intersection_multiplicity
sidebar: 
    nav: "algebraic_geometry-ko"

header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Intersection_Multiplicity.png
    overlay_filter: 0.5

date: 2026-03-15
last_modified_at: 2026-03-15
weight: 21
---

## 도입

평면 $$\mathbb{A}^2$$에서 두 곡선 $$y = 0$$과 $$y = x^2$$이 원점에서 만난다. 이 두 곡선은 단순히 "만난다"고 말하는 것으로는 충분하지 않다. 원점에서 얼마나 "강하게" 만나는가?

**Intersection multiplicity**는 두 variety가 한 점에서 얼마나 "복잡하게" 만나는지를 측정하는 정수이다. 이것은 Bézout's theorem, Chow groups 등의 기초가 된다.

## Definition

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Affine space $$\mathbb{A}^n$$의 점 $$p$$에서 두 variety $$V, W$$의 **intersection multiplicity<sub>교차 중복도</sub>** $$i_p(V, W)$$를 다음과 같이 정의한다:

$$i_p(V, W) = \dim_{\mathbb{K}} \mathcal{O}_{\mathbb{A}^n, p} / (I(V) + I(W))$$

여기서 $$\mathcal{O}_{\mathbb{A}^n, p}$$는 $$p$$에서의 local ring이다.

</div>

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins> $$\mathbb{A}^2$$에서 $$V: y = 0$$과 $$W: y = x^2$$가 원점에서 만난다.

- $$I(V) = (y)$$, $$I(W) = (y - x^2)$$
- $$\mathcal{O}_{\mathbb{A}^2, 0} / (y, y - x^2) = \mathcal{O}_{\mathbb{A}^2, 0} / (y, x^2)$$
- 이것은 basis $$\{1, x\}$$를 갖는 2차원 vector space

따라서 $$i_0(V, W) = 2$$이다.

</div>

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> $$\mathbb{A}^2$$에서 $$V: y = 0$$과 $$W: y = x^3$$이 원점에서 만난다.

$$\mathcal{O}_{\mathbb{A}^2, 0} / (y, x^3)$$은 basis $$\{1, x, x^2\}$$를 갖는 3차원 vector space이다.

따라서 $$i_0(V, W) = 3$$이다.

</div>

## Properties

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> Intersection multiplicity의 기본 성질:

1. $$i_p(V, W) \geq 0$$이고, $$p \notin V \cap W$$이면 $$i_p(V, W) = 0$$
2. $$V, W$$가 $$p$$에서 transversely intersect하면 $$i_p(V, W) = 1$$
3. $$i_p(V, W) = i_p(W, V)$$ (symmetry)
4. $$\dim V + \dim W = n$$이면 $$i_p(V, W) < \infty$$

</div>

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5 (Additivity)**</ins> $$V = V_1 \cup V_2$$이면:

$$i_p(V, W) = i_p(V_1, W) + i_p(V_2, W)$$

</div>

## Projective Case

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> $$\mathbb{P}^n$$의 점 $$p$$에서 두 variety $$V, W$$의 intersection multiplicity를 affine chart에서의 값으로 정의한다. 이는 affine chart의 선택과 무관하다.

</div>

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7 (Bezout for Curves in $$\mathbb{P}^2$$)**</ins> $$\mathbb{P}^2$$에서 degree $$m$$, $$n$$의 두 curve $$C, D$$가 공통 성분을 갖지 않으면:

$$\sum_{p \in C \cap D} i_p(C, D) = mn$$

</div>

<div class="example" markdown="1">

<ins id="ex8">**예시 8**</ins> Circle $$C: x^2 + y^2 = z^2$$과 line $$L: y = z$$을 $$\mathbb{P}^2$$에서 생각하자.

$$C \cap L$$은 한 점 $$[0:1:1]$$에서 multiplicity 2로 만난다. (Substituting $$y = z$$ into $$x^2 + y^2 = z^2$$ gives $$x^2 = 0$$.)

Check: $$\deg C = 2$$, $$\deg L = 1$$, $$2 \times 1 = 2$$. ✓

</div>

## Dimension Formula

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> $$\dim V + \dim W = n$$이고 $$V \cap W$$가 finite set이면:

$$\sum_{p \in V \cap W} i_p(V, W) = \deg(V) \cdot \deg(W)$$

</div>

## Local Ring Interpretation

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10**</ins> $$V, W$$가 $$p$$에서 smooth하고 transversely intersect하면:

$$i_p(V, W) = \dim_{\mathbb{K}} \mathcal{O}_{V \cap W, p}$$

즉, intersection multiplicity는 local ring의 dimension이다.

</div>

<div class="example" markdown="1">

<ins id="ex11">**예시 11 (Double point)**</ins> $$V: y = 0$$, $$W: y = x^2$$의 경우:

- $$V \cap W$$는 점 $$p = (0, 0)$$ 하나
- $$\mathcal{O}_{V \cap W, p} = \mathbb{K}[x]_{(x)} / (x^2)$$
- Dimension = 2

따라서 $$i_p(V, W) = 2$$이다.

</div>

## Relation to Tangent Spaces

<div class="proposition" markdown="1">

<ins id="prop12">**명제 12**</ins> $$V, W$$가 $$p$$에서 smooth하면:

$$i_p(V, W) = 1 \iff T_p V + T_p W = \mathbb{A}^n$$

즉, tangent space가 transversely intersect하면 multiplicity 1이다.

</div>

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[Ful]** W. Fulton, *Intersection Theory*, Springer, 1984.
