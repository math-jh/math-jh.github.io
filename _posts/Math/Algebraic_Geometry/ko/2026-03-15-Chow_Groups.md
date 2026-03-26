---
title: "Chow Groups"
excerpt: "Chow groups and the cycle class map"

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/chow_groups
sidebar: 
    nav: "algebraic_geometry-ko"

header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Chow_Groups.png
    overlay_filter: 0.5

date: 2026-03-15
last_modified_at: 2026-03-15
weight: 19
published: false
---

## 도입

Chow group은 variety의 "algebraic cycle"들의 group이다. 이는 homology/cohomology의 대수적 아날로그로, intersection theory의 기본적인 setting을 제공한다.

Chow group은 variety를 subvariety들의 "형식합"으로 이해하게 해주며, 두 cycle의 "intersection"을 정의할 수 있게 한다.

## Algebraic Cycles

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Variety $$X$$의 **algebraic $$k$$-cycle<sub>대수적 $$k$$-사이클</sub>**은 $$X$$의 $$k$$차원 닫힌 기약 부분다양체들의 형식합이다:

$$Z = \sum_{i} n_i V_i$$

여기서 $$V_i \subset X$$는 $$k$$차원 기약 닫힌 부분다양체이고 $$n_i \in \mathbb{Z}$$이다.

$$k$$-cycle들의 free abelian group을 $$Z_k(X)$$로 표기한다.

</div>

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> **Codimension $$k$$ cycle**은 $$(n-k)$$-cycle과 같다 (여기서 $$n = \dim X$$). 이를 $$Z^k(X) = Z_{n-k}(X)$$로 표기한다.

</div>

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> $$\mathbb{P}^2$$에서:
- $$Z_2(\mathbb{P}^2)$$: points들의 형식합
- $$Z_1(\mathbb{P}^2)$$: curves들의 형식합
- $$Z_0(\mathbb{P}^2)$$: $$\mathbb{P}^2$$ 자체의 정수배

</div>

## Rational Equivalence

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> **Rational function** $$f \in \mathbb{K}(Y)^\ast$$ on $$(k+1)$$-dimensional variety $$Y$$에 대해 **principal cycle**을 다음과 같이 정의한다:

$$\operatorname{div}(f) = \sum_{V \subset Y, \dim V = k} v_V(f) \cdot V$$

여기서 $$v_V(f)$$는 $$f$$의 $$V$$에서의 valuation (order of zero/pole)이다.

</div>

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> 두 $$k$$-cycle $$Z_1, Z_2$$가 **rationally equivalent<sub>유리 동치</sub>**라는 것은 $$Z_1 - Z_2 = \sum_j \operatorname{div}(f_j)$$를 만족하는 principal cycle들의 유한합이 존재하는 것이다. 이를 $$Z_1 \sim_{\text{rat}} Z_2$$로 표기한다.

</div>

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> Rational equivalence는 $$Z_k(X)$$ 위의 equivalence relation이다.

</div>

## Chow Groups

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> **Chow group<sub>Chow 군</sub>** $$\operatorname{CH}_k(X)$$를 $$k$$-cycle들을 rational equivalence로 나눈 group으로 정의한다:

$$\operatorname{CH}_k(X) = Z_k(X) / \sim_{\text{rat}}$$

Codimension $$k$$ Chow group: $$\operatorname{CH}^k(X) = \operatorname{CH}_{n-k}(X)$$

</div>

<div class="example" markdown="1">

<ins id="ex8">**예시 8 ($$\mathbb{P}^n$$)**</ins> $$\operatorname{CH}_k(\mathbb{P}^n) \cong \mathbb{Z}$$ for all $$k$$.

생성원은 $$k$$-dimensional linear subspace이다. 이는 $$\operatorname{Cl}(\mathbb{P}^n) \cong \mathbb{Z}$$과 일치한다.

</div>

<div class="example" markdown="1">

<ins id="ex9">**예시 9 (Smooth curve)**</ins> Smooth projective curve $$C$$에 대해:

- $$\operatorname{CH}_1(C) \cong \mathbb{Z}$$ (생성원: $$C$$ 자체)
- $$\operatorname{CH}_0(C) \cong \operatorname{Cl}(C)$$ (divisor class group)

</div>

<div class="example" markdown="1">

<ins id="ex10">**예시 10 (Affine space)**</ins> $$\operatorname{CH}_k(\mathbb{A}^n) = 0$$ for $$k < n$$.

$$\operatorname{CH}_n(\mathbb{A}^n) \cong \mathbb{Z}$$ (생성원: $$\mathbb{A}^n$$ 자체).

</div>

## Functoriality

<div class="proposition" markdown="1">

<ins id="prop11">**명제 11 (Pushforward)**</ins> Proper morphism $$f: X \to Y$$에 대해 pushforward $$f_\ast: \operatorname{CH}_k(X) \to \operatorname{CH}_k(Y)$$가 존재한다.

Subvariety $$V \subset X$$에 대해:

$$f_\ast[V] = \begin{cases}
\deg(V / f(V)) \cdot [f(V)] & \dim f(V) = \dim V \\
0 & \dim f(V) < \dim V
\end{cases}$$

</div>

<div class="proposition" markdown="1">

<ins id="prop12">**명제 12 (Pullback)**</ins> Flat morphism $$f: X \to Y$$에 대해 pullback $$f^\ast: \operatorname{CH}^k(Y) \to \operatorname{CH}^k(X)$$가 존재한다.

</div>

<div class="example" markdown="1">

<ins id="ex13">**예시 13**</ins> Projection $$\pi: \mathbb{P}^1 \times \mathbb{P}^1 \to \mathbb{P}^1$$에 대해:

$$\pi_\ast[\mathbb{P}^1 \times \{p\}] = [p] \in \operatorname{CH}_0(\mathbb{P}^1) \cong \mathbb{Z}$$

</div>

## Relation to Other Theories

<div class="proposition" markdown="1">

<ins id="prop14">**명제 14 (vs. Divisor class group)**</ins> Smooth variety $$X$$에 대해:

$$\operatorname{CH}^1(X) \cong \operatorname{Cl}(X) \cong \operatorname{Pic}(X)$$

</div>

<div class="proposition" markdown="1">

<ins id="prop15">**명제 15 (vs. Homology)**</ins> Complex variety $$X$$에 대해 **cycle class map**이 존재한다:

$$\operatorname{CH}_k(X) \to H_{2k}(X, \mathbb{Z})$$

이 map은 일반적으로 injective도 surjective도 아니다.

</div>

## Chow Ring

<div class="proposition" markdown="1">

<ins id="prop16">**명제 16**</ins> Smooth variety $$X$$에 대해 Chow group $$\operatorname{CH}^\ast(X) = \bigoplus_k \operatorname{CH}^k(X)$$는 intersection product에 대해 **graded ring**을 이룬다.

</div>

<div class="example" markdown="1">

<ins id="ex17">**예시 17 ($$\mathbb{P}^n$$)**</ins> $$\operatorname{CH}^\ast(\mathbb{P}^n) \cong \mathbb{Z}[H] / (H^{n+1})$$

여기서 $$H$$는 hyperplane class이다. $$H^k$$는 $$k$$-codimensional linear subspace를 나타낸다.

</div>

---

**참고문헌**

**[Ful]** W. Fulton, *Intersection Theory*, Springer, 1984.  
**[Har]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.
