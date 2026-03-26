---
title: "Intersection Product"
excerpt: "The intersection product on Chow groups"

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/intersection_product
sidebar: 
    nav: "algebraic_geometry-ko"

header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Intersection_Product.png
    overlay_filter: 0.5

date: 2026-03-15
last_modified_at: 2026-03-15
weight: 20
published: false
---

## 도입

Chow group $$\operatorname{CH}^\ast(X)$$는 단순한 abelian group이 아니라, **intersection product**라는 곱셈 구조를 갖는다. 이 product는 두 cycle의 "intersection"을 formalize한 것이다.

Intersection product는 variety의 geometry를 algebra적으로 연구하는 핵심 도구이다.

## Basic Definition

<div class="proposition" markdown="1">

<ins id="prop1">**명제 1 (Intersection Product)**</ins> Smooth variety $$X$$ 위에서 codimension $$k$$, $$l$$의 두 cycle $$Z, W$$의 **intersection product** $$Z \cdot W \in \operatorname{CH}^{k+l}(X)$$를 정의할 수 있다. 이는 다음 성질을 만족한다:

1. **Commutativity**: $$Z \cdot W = W \cdot Z$$
2. **Associativity**: $$(Z_1 \cdot Z_2) \cdot Z_3 = Z_1 \cdot (Z_2 \cdot Z_3)$$
3. **Distributivity**: $$Z \cdot (W_1 + W_2) = Z \cdot W_1 + Z \cdot W_2$$
4. **Identity**: $$[X] \cdot Z = Z$$ (여기서 $$[X] \in \operatorname{CH}^0(X)$$)

</div>

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> Intersection product에 의해 $$\operatorname{CH}^\ast(X) = \bigoplus_k \operatorname{CH}^k(X)$$는 **graded ring**이 된다. 이를 **Chow ring**이라 부른다.

</div>

## Proper Intersection

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> 두 subvariety $$V, W \subset X$$가 **properly intersect<sub>적절히 교차</sub>**한다는 것은 모든 component $$Z$$ of $$V \cap W$$에 대해:

$$\operatorname{codim}(Z) = \operatorname{codim}(V) + \operatorname{codim}(W)$$

인 것이다.

</div>

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> $$V, W$$가 properly intersect하면:

$$[V] \cdot [W] = \sum_{Z \subset V \cap W} i_Z(V, W) [Z]$$

여기서 $$i_Z(V, W)$$는 intersection multiplicity이다.

</div>

<div class="example" markdown="1">

<ins id="ex5">**예시 5 ($$\mathbb{P}^2$$)**</ins> $$\mathbb{P}^2$$에서 두 line $$L_1, L_2$$가 점 $$p$$에서 만나면:

$$[L_1] \cdot [L_2] = [p] \in \operatorname{CH}^2(\mathbb{P}^2)$$

$$\operatorname{CH}^\ast(\mathbb{P}^2) = \mathbb{Z}[H] / (H^3)$$에서 $$[L_i] = H$$이고 $$H^2 = [p]$$이다.

</div>

## Moving Lemma

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6 (Moving Lemma)**</ins> Quasi-projective variety $$X$$와 cycle $$Z \in \operatorname{CH}^k(X)$$에 대해, 임의의 cycle $$W \in \operatorname{CH}^l(X)$$에 대해 $$Z' \sim_{\text{rat}} Z$$이고 $$Z'$$과 $$W$$가 properly intersect하는 $$Z'$$가 존재한다.

</div>

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> Moving lemma에 의해 intersection product를 정의할 수 있다:
1. $$Z' \sim_{\text{rat}} Z$$이고 $$Z'$$이 $$W$$와 properly intersect하도록 선택
2. $$Z \cdot W := Z' \cdot W$$ (proper intersection으로 계산)
3. Well-defined임을 확인

</div>

## Deformation to Normal Cone

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8 (Deformation to Normal Cone)**</ins> Closed embedding $$i: Y \hookrightarrow X$$에 대해, $$Y$$의 $$X$$ 안에서의 normal bundle $$N_{Y/X}$$를 사용하여 intersection product를 정의할 수 있다.

이 방법은 moving lemma 없이도 intersection product를 정의한다.

</div>

## Examples

<div class="example" markdown="1">

<ins id="ex9">**예시 9 ($$\mathbb{P}^n$$)**</ins> $$\operatorname{CH}^\ast(\mathbb{P}^n) \cong \mathbb{Z}[H] / (H^{n+1})$$

- $$H = [\text{hyperplane}] \in \operatorname{CH}^1(\mathbb{P}^n)$$
- $$H^k = [k\text{-codimensional linear subspace}]$$
- Degree $$d$$ hypersurface $$V(f)$$에 대해 $$[V(f)] = dH$$

</div>

<div class="example" markdown="1">

<ins id="ex10">**예시 10 (Surface)**</ins> Surface $$S$$ 위의 두 curve $$C, D$$에 대해:

$$[C] \cdot [D] = \sum_{p \in C \cap D} i_p(C, D) [p] \in \operatorname{CH}^2(S)$$

$$\operatorname{CH}^2(S) \cong \mathbb{Z}$$ (zero-cycles modulo rational equivalence)에서 이것은 정수로 식별된다:

$$C \cdot D = \sum_{p \in C \cap D} i_p(C, D)$$

</div>

<div class="example" markdown="1">

<ins id="ex11">**예시 11 ($$\mathbb{P}^1 \times \mathbb{P}^1$$)**</ins> $$\operatorname{CH}^\ast(\mathbb{P}^1 \times \mathbb{P}^1) \cong \mathbb{Z}[H_1, H_2] / (H_1^2, H_2^2)$$

여기서 $$H_1 = [\mathbb{P}^1 \times \{p\}]$$, $$H_2 = [\{p\} \times \mathbb{P}^1]$$이다.

Bidegree $$(a, b)$$의 curve $$C$$에 대해 $$[C] = aH_1 + bH_2$$이다.

</div>

## Intersection with Line Bundle

<div class="proposition" markdown="1">

<ins id="prop12">**명제 12**</ins> Line bundle $$L$$과 cycle $$Z \in \operatorname{CH}_k(X)$$에 대해:

$$c_1(L) \cap Z \in \operatorname{CH}_{k-1}(X)$$

가 존재한다. 여기서 $$c_1(L)$$은 first Chern class이다.

</div>

<div class="proposition" markdown="1">

<ins id="prop13">**명제 13**</ins> $$L = \mathcal{O}(D)$$이면:

$$c_1(L) \cap [X] = [D] \in \operatorname{CH}^1(X)$$

</div>

## Projection Formula

<div class="proposition" markdown="1">

<ins id="prop14">**명제 14 (Projection Formula)**</ins> Proper morphism $$f: X \to Y$$와 $$\alpha \in \operatorname{CH}^\ast(X)$$, $$\beta \in \operatorname{CH}^\ast(Y)$$에 대해:

$$f_\ast(\alpha \cdot f^\ast \beta) = f_\ast(\alpha) \cdot \beta$$

</div>

---

**참고문헌**

**[Ful]** W. Fulton, *Intersection Theory*, Springer, 1984.  
**[Har]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.
