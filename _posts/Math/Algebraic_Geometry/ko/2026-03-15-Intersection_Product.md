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
last_modified_at: 2026-03-31
weight: 20
published: false
---

## 도입

Chow group $$\operatorname{CH}^\ast(X)$$는 단순한 abelian group이 아니라, **intersection product**라는 곱셈 구조를 갖는다. 이 product는 두 cycle의 "intersection"을 formalize한 것이다. 본 글은 Chow group ([§Chow_Groups](/ko/math/algebraic_geometry/chow_groups)), intersection multiplicity ([§Intersection_Multiplicity](/ko/math/algebraic_geometry/intersection_multiplicity)), line bundle ([§Line_Bundles](/ko/math/algebraic_geometry/line_bundles))에 대한 기본 지식을 전제로 한다.

Intersection product가 필요한 이유를 알아보자. Surface $$S$$ 위의 두 curve $$C, D$$를 생각하자. $$C \cdot D = \sum_p i_p(C,D)$$로 교차 수를 계산할 수 있는데, 이 정수는 $$C$$와 $$D$$의 "위치"만이 아니라 "rational equivalence class"에 의존한다. 즉, 두 curve의 intersection은 각 curve 자체보다는 그들이 대표하는 Chow class의 곱셈으로 이해되어야 한다. 이는 topology에서 singular homology group $$H_\ast(X)$$가 단순한 abelian group이 아니라 **homology ring** 구조를 가지는 것과 완전히 같은 현상이다 — Poincaré dual을 통한 cap product가 homology class 사이의 곱셈을 주듯이, Chow group에서는 intersection product가 같은 역할을 한다.

구체적인 예로, $$\mathbb{P}^2$$에서 degree $$d_1$$ curve $$C_1$$과 degree $$d_2$$ curve $$C_2$$가 있다면 Bézout 정리에 의해 $$C_1 \cdot C_2 = d_1 d_2$$이다. 이 결과는 두 curve의 구체적인 위치에 무관하며, 오직 그들의 Chow class $$d_1[H]$$와 $$d_2[H]$$의 곱 $$d_1 d_2 H^2$$로부터 얻어진다. Intersection product는 이러한 계산을 일반적인 smooth variety에서 가능하게 하는 algebraic 구조이다.

## Basic Definition

<div class="proposition" markdown="1">

<ins id="prop1">**명제 1 (Intersection Product)**</ins> Smooth variety $$X$$ 위에서 codimension $$k$$, $$l$$의 두 cycle $$Z, W$$의 **intersection product** $$Z \cdot W \in \operatorname{CH}^{k+l}(X)$$를 정의할 수 있다. 교환법칙 $$Z \cdot W = W \cdot Z$$, 결합법칙 $$(Z_1 \cdot Z_2) \cdot Z_3 = Z_1 \cdot (Z_2 \cdot Z_3)$$, 분배법칙 $$Z \cdot (W_1 + W_2) = Z \cdot W_1 + Z \cdot W_2$$을 만족하며, $$[X] \in \operatorname{CH}^0(X)$$가 항등원 역할을 한다.

**증명 sketch.** Intersection product를 정의하는 핵심 아이디어는 다음과 같다. 주어진 cycle $$Z \in \operatorname{CH}^k(X)$$와 $$W \in \operatorname{CH}^l(X)$$에 대해, $$Z$$를 rational equivalence 내에서 적절히 "이동"시켜 $$Z' \sim_{\text{rat}} Z$$이고 $$Z'$$가 $$W$$와 properly intersect하도록 만든다 (이것이 [명제 6 (Moving Lemma)](#prop6)의 내용이다). 그러면 $$Z' \cdot W$$를 proper intersection으로 계산할 수 있다:

$$Z' \cdot W = \sum_{Z \subset Z' \cap W} i_Z(Z', W) [Z]$$

이것을 $$Z \cdot W$$로 정의한다. Moving lemma는 $$Z'$$의 선택에 의존하지 않음을 보장하므로 well-defined이며, 교환·결합·분배 법칙은 proper intersection에서의 intersection multiplicity의 성질로부터 따라온다.

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

일반적으로 두 subvariety $$V, W \subset X$$는 properly intersect하지 않는다 — 교차의 어떤 component가 예상보다 낮은 codimension을 가질 수 있다. 예를 들어 $$\mathbb{P}^3$$에서 두 surface가 curve를 공유하면 교차의 component 중에 curve가 포함되어 codimension이 $$1+1 = 2$$가 아닌 $$1$$이 된다. Intersection product를 codimension의 덧셈에 맞게 정의하려면 이를 피해야 하며, moving lemma는 cycle을 rational equivalence 내에서 "움직여" proper intersection을 달성하는 정리이다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6 (Moving Lemma)**</ins> Quasi-projective variety $$X$$와 cycle $$Z \in \operatorname{CH}^k(X)$$에 대해, 임의의 cycle $$W \in \operatorname{CH}^l(X)$$에 대해 $$Z' \sim_{\text{rat}} Z$$이고 $$Z'$$과 $$W$$가 properly intersect하는 $$Z'$$가 존재한다.

</div>

핵심 아이디어는 다음과 같다. $$Z$$를 구성하는 irreducible component $$V_i$$마다, $$V_i$$를 포함하는 충분히 "일반적인" hypersurface $$H_i$$로 자르고, $$V_i \cap H_1 \cap \cdots \cap H_s$$와 같은 형태의 cycle을 취한다. "일반적"이라는 것은 $$H_i$$가 $$W$$와 generic한 위치에서 만나도록 선택하는 것이며, 이렇게 하면 차원이 적절히 떨어져 proper intersection을 이룬다. 이 과정이 rational equivalence를 보존함을 보이는 것이 증명의 핵심이다.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> Moving lemma에 의해 intersection product를 정의할 수 있다. $$Z' \sim_{\text{rat}} Z$$이고 $$Z'$$이 $$W$$와 properly intersect하도록 선택한 뒤, $$Z \cdot W := Z' \cdot W$$로 정의한다. 여기서 우변은 proper intersection에 대한 intersection multiplicity의 합으로 주어진다 ([명제 4](#prop4)). $$Z'$$의 다른 선택이 같은 결과를 주는지 확인해야 하는데, 이는 moving lemma가 $$Z'$$의 "충분한 일반성"을 보장함과 rational equivalence와의 호환성으로부터 따른다.

</div>

## Deformation to Normal Cone

Moving lemma는 quasi-projective setting에서 intersection product를 정의하는 고전적 방법이지만, general scheme에서는 증명이 매우 어렵고 기술적이다. 이에 대한 대안이 **deformation to normal cone**이다.

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8 (Deformation to Normal Cone)**</ins> Closed embedding $$i: Y \hookrightarrow X$$에 대해, $$Y$$의 $$X$$ 안에서의 normal bundle $$N_{Y/X}$$를 사용하여 intersection product를 정의할 수 있다.

</div>

이 방법의 핵심 아이디어는 다음과 같다. $$\mathbb{A}^1$$을 매개변수로 하는 family $$M \subset X \times \mathbb{A}^1$$을 구성하는데, $$t \neq 0$$에서의 fiber $$M_t$$는 "이동된" $$X$$ (즉 $$X$$ 자신)이고, $$t = 0$$에서의 fiber $$M_0$$이 normal cone $$C_{Y/X}$$와 같아지도록 한다. 즉, $$X$$를 연속적으로 변형하여 $$Y$$의 "정규원뿔"으로 수축시키는 것이다. 이 family의 존재는 intersection product의 well-definedness를 이 family에 대한 pushforward/pullback의 호환성으로 환원시킨다.

이 접근은 moving lemma와 달리 scheme에 대한 추가 가정 (quasi-projectivity 등)이 필요하지 않아 더 일반적이며, Fulton의 *Intersection Theory*에서 채택한 주요 프레임워크이다. Pushforward $$f_\ast$$와 pullback $$f^\ast$$는 [§Chow_Groups, ⁋명제 11](/ko/math/algebraic_geometry/chow_groups#prop11) 및 [§Chow_Groups, ⁋명제 12](/ko/math/algebraic_geometry/chow_groups#prop12)에서 정의되었다.

## Examples

<div class="example" markdown="1">

<ins id="ex9">**예시 9 ($$\mathbb{P}^n$$)**</ins> $$\operatorname{CH}^\ast(\mathbb{P}^n) \cong \mathbb{Z}[H] / (H^{n+1})$$이다. 여기서 $$H = [\text{hyperplane}] \in \operatorname{CH}^1(\mathbb{P}^n)$$로, $$H^k$$는 $$k$$-codimensional linear subspace의 class와 같다. Degree $$d$$ hypersurface $$V(f)$$에 대해서는 $$[V(f)] = dH$$이다.

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

<ins id="prop12">**명제 12**</ins> Line bundle $$L$$과 cycle $$Z \in \operatorname{CH}_k(X)$$에 대해 $$c_1(L) \cap Z \in \operatorname{CH}_{k-1}(X)$$를 정의할 수 있다. 여기서 **first Chern class** $$c_1(L) \in \operatorname{CH}^1(X)$$는 line bundle $$L$$에 대응하는 divisor class이며, $$L$$이 Cartier divisor $$D$$에 의해 주어지면 $$c_1(L) = [D] \in \operatorname{CH}^1(X)$$이다. 이 대응은 [§Divisors](/ko/math/algebraic_geometry/divisors)와 [§Line_Bundles](/ko/math/algebraic_geometry/line_bundles)에서 다룬 Cartier divisor와 line bundle 사이의 동치관계에 근거한다.

$$c_1(L) \cap Z$$를 구체적으로 정의하려면, $$L = \mathcal{O}(D)$$라 하자. Divisor $$D = \sum n_i V_i$$에 대해 $$D$$와 $$Z$$가 properly intersect하면 $$c_1(L) \cap Z = \sum n_i [V_i \cap Z]$$로, intersection multiplicity까지 포함하면 $$\sum n_i \cdot (V_i \cdot Z)$$로 정의된다. Proper intersection이 아닌 경우 moving lemma나 deformation to normal cone을 사용한다.

</div>

<div class="proposition" markdown="1">

<ins id="prop13">**명제 13**</ins> $$L = \mathcal{O}(D)$$이면:

$$c_1(L) \cap [X] = [D] \in \operatorname{CH}^1(X)$$

</div>

## Projection Formula

<div class="proposition" markdown="1">

<ins id="prop14">**명제 14 (Projection Formula)**</ins> Proper morphism $$f: X \to Y$$와 $$\alpha \in \operatorname{CH}^\ast(X)$$, $$\beta \in \operatorname{CH}^\ast(Y)$$에 대해 $$f_\ast(\alpha \cdot f^\ast \beta) = f_\ast(\alpha) \cdot \beta$$가 성립한다.

**증명 sketch.** $$\alpha = [V]$$, $$\beta = [W]$$ (irreducible subvariety)인 경우로 국소화한다. $$f^\ast[W] = [f^{-1}(W)]$$ (scheme-theoretic inverse image)이므로 $$[V] \cdot f^\ast[W] = [V \cap f^{-1}(W)]$$이다. 한편 $$f_\ast(\alpha) \cdot \beta = [f(V)] \cdot [W]$$에서, 양쪽 모두 $$f(V) \cap W$$ 위에서의 intersection multiplicity로 계산된다. Proper morphism이므로 $$f|_V: V \to f(V)$$가 proper map이고, $$V \cap f^{-1}(W)$$와 $$f(V) \cap W$$ 사이의 fiber 차원이 일정함을 이용하여 두 multiplicity가 같음을 보인다.

</div>

---

**참고문헌**

**[Ful]** W. Fulton, *Intersection Theory*, Springer, 1984.  
**[Har]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.
