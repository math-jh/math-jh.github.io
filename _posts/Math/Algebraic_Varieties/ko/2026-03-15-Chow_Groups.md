---
title: "Chow Groups"
excerpt: "Chow groups and the cycle class map"

categories: [Math / Algebraic Varieties]
permalink: /ko/math/algebraic_varieties/chow_groups
sidebar: 
    nav: "algebraic_varieties-ko"

header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Chow_Groups.png
    overlay_filter: 0.5

date: 2026-03-15
last_modified_at: 2026-03-15
weight: 19
published: false
---

## 도입

이 글에서는 variety 위의 *algebraic cycle*<sub>대수적 순환</sub>들의 group인 Chow group을 정의한다. 이는 homology/cohomology의 대수적 아날로그로, intersection theory의 기본적인 설정을 제공한다.

([§인자](/ko/math/algebraic_varieties/divisors))에서 우리는 codimension 1 closed irreducible subvariety들의 formal sum인 divisor와, rational equivalence로 모은 divisor class group $$\Cl(X)$$를 정의했다. Chow group은 이를 임의 차원으로 확장한 것이다: $$k$$-dimensional closed irreducible subvariety들의 formal sum을 rational equivalence로 나누어 $$\operatorname{CH}_k(X)$$를 얻는다. 이렇게 하면 variety의 "위상적 정보" 가운데 대수적으로 기술할 수 있는 부분을 남기고, 그렇지 않은 정보는 버리게 된다. 예를 들어 $$\operatorname{CH}_0(\mathbb{A}^n) = 0$$이므로 affine space 위의 점들은 Chow group에서 모두 동치이다 — 이는 $$\mathbb{A}^n$$이 "대수적으로 구부러질 여지"가 없기 때문에 점의 위치라는 정보를 보존하지 못하는 것이다.

Chow group은 variety를 subvariety들의 "formal sum"으로 이해하게 해주며, 두 cycle 사이의 *intersection*<sub>교차</sub>을 정의할 수 있게 한다. 교차에 대한 자세한 내용은 ([§Intersection Multiplicity](/ko/math/algebraic_varieties/intersection_multiplicity))에서 다룬다.

## 대수적 순환

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Variety $$X$$의 *algebraic $$k$$-cycle*<sub>대수적 $$k$$-순환</sub>은 $$X$$의 $$k$$-dimensional closed irreducible subvariety들의 formal sum이다:

$$Z = \sum_{i} n_i V_i$$

여기서 $$V_i \subset X$$는 $$k$$-dimensional closed irreducible subvariety이고 $$n_i \in \mathbb{Z}$$이다.

$$k$$-cycle들이 이루는 free abelian group을 $$Z_k(X)$$로 표기한다.

</div>

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> *Codimension $$k$$ cycle*<sub>여차원 $$k$$ 순환</sub>은 $$(n-k)$$-cycle과 같다 (여기서 $$n = \dim X$$). 이를 $$Z^k(X) = Z_{n-k}(X)$$로 표기한다.

</div>

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> $$\mathbb{P}^2$$에서 $$Z_2(\mathbb{P}^2)$$는 $$\mathbb{P}^2$$ 자체의 정수배로 이루어지고, $$Z_1(\mathbb{P}^2)$$는 curve들의 formal sum이며, $$Z_0(\mathbb{P}^2)$$는 점들의 formal sum이다.

</div>

## 유리 동치

([§인자](/ko/math/algebraic_varieties/divisors))에서 우리는 rational function의 영점과 극점의 정보를 담는 principal divisor를 정의했다. 이 개념을 임의의 차원으로 확장하면 rational equivalence를 정의할 수 있다.

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> Variety $$X$$의 $$(k+1)$$-dimensional closed irreducible subvariety $$Y \subset X$$ 위의 rational function $$f \in \mathbb{K}(Y)^\ast$$에 대해 *principal cycle*<sub>주순환</sub> $$\divisor(f) \in Z_k(X)$$를 다음과 같이 정의한다:

$$\divisor(f) = \sum_{V \subset Y, \dim V = k} v_V(f) \cdot V$$

여기서 합은 $$Y$$의 codimension 1 closed irreducible subvariety $$V$$들에 대해 돌고, $$v_V(f)$$는 $$f$$의 $$V$$에서의 valuation (영점 또는 극점의 order)이다. $$f \in \mathbb{K}(Y)^\ast$$이므로 $$v_V(f) = 0$$인 $$V$$는 유한 개뿐이며, 따라서 $$\divisor(f)$$는 유한합이다.

</div>

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> 두 $$k$$-cycle $$Z_1, Z_2$$가 *rationally equivalent*<sub>유리 동치</sub>라는 것은, $$X$$의 $$(k+1)$$-dimensional closed irreducible subvariety $$Y_j$$와 그 위의 rational function $$f_j \in \mathbb{K}(Y_j)^\ast$$들이 존재하여

$$Z_1 - Z_2 = \sum_j \divisor(f_j)$$

을 만족하는 것이다. 이를 $$Z_1 \sim_{\text{rat}} Z_2$$로 표기한다.

</div>

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> Rational equivalence는 $$Z_k(X)$$ 위의 동치관계이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

**Reflexivity**: $$Z - Z = 0 = \divisor(1)$$이므로 $$Z \sim_{\text{rat}} Z$$이다. **Symmetry**: $$Z_1 - Z_2 = \sum_j \divisor(f_j)$$이면 $$Z_2 - Z_1 = \sum_j \divisor(f_j^{-1}) = -\sum_j \divisor(f_j)$$이므로 $$Z_2 \sim_{\text{rat}} Z_1$$이다. **Transitivity**: $$Z_1 \sim_{\text{rat}} Z_2$$이고 $$Z_2 \sim_{\text{rat}} Z_3$$이라면, $$Z_1 - Z_2 = \sum_i \divisor(f_i)$$, $$Z_2 - Z_3 = \sum_j \divisor(g_j)$$이므로

$$Z_1 - Z_3 = (Z_1 - Z_2) + (Z_2 - Z_3) = \sum_i \divisor(f_i) + \sum_j \divisor(g_j)$$

역시 principal cycle들의 유한합이므로 $$Z_1 \sim_{\text{rat}} Z_3$$이다.

</details>

## Chow group

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> *Chow group*<sub>Chow 군</sub> $$\operatorname{CH}_k(X)$$를 $$k$$-cycle들을 rational equivalence로 나눈 group으로 정의한다:

$$\operatorname{CH}_k(X) = Z_k(X) / \sim_{\text{rat}}$$

Codimension $$k$$ Chow group: $$\operatorname{CH}^k(X) = \operatorname{CH}_{n-k}(X)$$.

</div>

<div class="example" markdown="1">

<ins id="ex8">**예시 8 ($$\mathbb{P}^n$$)**</ins> 모든 $$k$$에 대해 $$\operatorname{CH}_k(\mathbb{P}^n) \cong \mathbb{Z}$$이다.

$$k$$-dimensional linear subspace $$\mathbb{P}^k \subset \mathbb{P}^n$$를 $$\ell_k$$라 하자. 임의의 $$k$$-dimensional irreducible subvariety $$V \subset \mathbb{P}^n$$에 대해, 적당한 정수 $$d \geq 0$$이 존재하여 $$[V] \sim_{\text{rat}} d \cdot \ell_k$$이다. 이 정수 $$d$$는 $$V$$와 일반 위치의 $$(n-k)$$-dimensional linear subspace 사이의 intersection multiplicity ([§Intersection Multiplicity](/ko/math/algebraic_varieties/intersection_multiplicity))와 일치한다. 따라서 $$\operatorname{CH}_k(\mathbb{P}^n)$$는 $$[\ell_k]$$에 의해 생성되고 $$\mathbb{Z}$$와 동형이다. 이는 $$\Cl(\mathbb{P}^n) \cong \mathbb{Z}$$과 일치한다.

</div>

<div class="example" markdown="1">

<ins id="ex9">**예시 9 (Smooth curve)**</ins> Smooth projective curve $$C$$에 대해 $$\operatorname{CH}_1(C) \cong \mathbb{Z}$$이며 생성원은 $$C$$ 자체이고, $$\operatorname{CH}_0(C) \cong \Cl(C)$$이다.

</div>

<div class="example" markdown="1">

<ins id="ex10">**예시 10 (Affine space)**</ins> $$k < n$$에 대해 $$\operatorname{CH}_k(\mathbb{A}^n) = 0$$이고, $$\operatorname{CH}_n(\mathbb{A}^n) \cong \mathbb{Z}$$이며 그 생성원은 $$\mathbb{A}^n$$ 자체이다. 이는 $$\Cl(\mathbb{A}^n) = 0$$ ([§인자, ⁋예시 10](/ko/math/algebraic_varieties/divisors#ex10))와 같은 정신이다: $$\mathbb{A}^n$$에는 "대수적으로 움직일 수 있는 여지"가 충분하여, 임의의 $$k$$-dimensional irreducible subvariety $$V$$에 대해 곱공간 $$\mathbb{A}^1 \times V$$를 통해 family를 구성하면 $$V$$가 rational equivalence로 $$0$$이 됨을 보일 수 있다.

</div>

## 함자성

<div class="definition" markdown="1">

<ins id="def11">**정의 11**</ins> Variety 사이의 morphism $$f: X \to Y$$가 *proper*<sub>고유 사상</sub>라는 것은, 임의의 base change $$Y' \to Y$$에 대해 유도된 사상 $$f_{Y'}: X \times_Y Y' \to Y'$$가 위상공간으로서 닫힌 사상이라는 뜻이다 (이를 *universally closed*라 한다). 기하적으로 proper morphism은 점들이 "무한대로 도피"하는 것을 허용하지 않는다: 닫힌 집합의 image는 항상 닫힌 집합이며, 이 성질은 base change 후에도 보존된다. 본 글에서 다루는 모든 variety는 separated이고 morphism은 finite type이라 가정하므로, 위 universally closed 조건만으로 proper의 정의가 완성된다. Projective morphism은 항상 proper이다.

</div>

<div class="definition" markdown="1">

<ins id="def12">**정의 12**</ins> Proper morphism $$f: X \to Y$$와 subvariety $$V \subset X$$에 대해, $$\dim f(V) = \dim V$$일 때 $$\deg(V/f(V))$$를 residue field extension degree로 정의한다:

$$\deg(V/f(V)) = [\mathbb{K}(V) : \mathbb{K}(f(V))]$$

이는 $$f$$가 $$V$$에서 $$f(V)$$로 유도하는 field extension의 차수이며, $$f(V)$$의 일반적인 점 위의 fiber에 들어있는 점의 수로 이해할 수 있다.

</div>

<div class="proposition" markdown="1">

<ins id="prop13">**명제 13**</ins> Proper morphism $$f: X \to Y$$에 대해 pushforward $$f_\ast: \operatorname{CH}_k(X) \to \operatorname{CH}_k(Y)$$가 존재한다. Subvariety $$V \subset X$$에 대해

$$f_\ast[V] = \begin{cases}
\deg(V / f(V)) \cdot [f(V)] & \dim f(V) = \dim V \\
0 & \dim f(V) < \dim V
\end{cases}$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

자세한 증명은 [Ful, §1.4]를 참조하라.

</details>

<div class="definition" markdown="1">

<ins id="def14">**정의 14**</ins> Morphism $$f: X \to Y$$가 *flat*<sub>평탄 사상</sub>이라는 것은, 임의의 점 $$x \in X$$에 대해 local ring $$\mathcal{O}_{X,x}$$가 $$\mathcal{O}_{Y,f(x)}$$-module로서 flat인 것이다. 즉, 임의의 $$\mathcal{O}_{Y,f(x)}$$-module들의 단사 사상 $$M \hookrightarrow N$$에 대해 $$M \otimes_{\mathcal{O}_{Y,f(x)}} \mathcal{O}_{X,x} \to N \otimes_{\mathcal{O}_{Y,f(x)}} \mathcal{O}_{X,x}$$도 단사 사상이다. 직관적으로, fiber의 차원이 일정하고, parameter를 연속적으로 변화시킬 때 fiber의 구조가 "연속적으로 변한다"는 것을 의미한다.

</div>

<div class="proposition" markdown="1">

<ins id="prop15">**명제 15**</ins> Flat morphism $$f: X \to Y$$에 대해 pullback $$f^\ast: \operatorname{CH}^k(Y) \to \operatorname{CH}^k(X)$$가 존재한다. 구체적으로, subvariety $$V \subset Y$$에 대해 $$f^\ast[V] = [f^{-1}(V)]$$이다. Flatness에 의해 $$\codim_X(f^{-1}(V)) = \codim_Y(V)$$가 보장되므로 codimension 표기 $$\operatorname{CH}^k$$로 보면 이 사상이 well-defined이다. (Dimension 표기로 보면 fiber의 relative dimension $$r$$만큼 차원이 증가하여 $$f^\ast: \operatorname{CH}_k(Y) \to \operatorname{CH}_{k+r}(X)$$이다.)

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

자세한 증명은 [Ful, §1.7]을 참조하라.

</details>

<div class="example" markdown="1">

<ins id="ex16">**예시 16**</ins> Projection $$\pi: \mathbb{P}^1 \times \mathbb{P}^1 \to \mathbb{P}^1$$에 대해:

$$\pi_\ast[\mathbb{P}^1 \times \{p\}] = [p] \in \operatorname{CH}_0(\mathbb{P}^1) \cong \mathbb{Z}$$

잔여체 확대 차수가 $$[\mathbb{K}(\mathbb{P}^1 \times \{p\}) : \mathbb{K}(\{p\})] = 1$$이므로 계수가 $$\deg = 1$$이다. 즉, fiber $$\mathbb{P}^1 \times \{p\}$$가 한 점 위로 일대일로 대응되므로 pushforward가 순환의 차원을 유지하면서 그대로 내려보낸다.

</div>

## 다른 이론들과의 관계

<div class="proposition" markdown="1">

<ins id="prop17">**명제 17**</ins> Smooth variety $$X$$에 대해

$$\operatorname{CH}^1(X) \cong \Cl(X) \cong \Pic(X)$$

이 성립한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$\operatorname{CH}^1(X) = \operatorname{CH}_{n-1}(X)$$는 codimension 1 closed irreducible subvariety(즉 Weil divisor의 성분)들의 rational equivalence에 의한 quotient group이다. $$X$$가 smooth이므로 모든 local ring이 regular이며, regular local ring이 UFD라는 사실에 의해 ([Hart, Theorem II.6.2A] 참조) $$X$$는 locally factorial이고, 따라서 Weil divisor와 Cartier divisor가 일치한다.

$$\Cl(X)$$는 Weil divisor들의 linear equivalence에 의한 quotient group이다. 두 동치 관계를 비교하자: rational equivalence는 임의의 $$(k+1)$$-dimensional subvariety $$Y$$ 위의 rational function $$f \in \mathbb{K}(Y)^\ast$$의 principal cycle $$\divisor(f)$$에 의해 생성되고, linear equivalence는 $$X$$ 자체 위의 rational function $$f \in \mathbb{K}(X)^\ast$$의 principal divisor $$\divisor(f)$$에 의해서만 생성된다.

하지만 codimension 1에서는 임의의 $$n$$-dimensional closed irreducible subvariety $$Y \subset X$$가 $$X$$ 자체뿐이므로 ($$\dim X = n$$), rational equivalence와 linear equivalence는 동일한 동치 관계이다. 따라서 $$\operatorname{CH}^1(X) \cong \Cl(X)$$. $$\Cl(X) \cong \Pic(X)$$는 ([§인자](/ko/math/algebraic_varieties/divisors))에서 이미 확인하였다.

</details>

<div class="proposition" markdown="1">

<ins id="prop18">**명제 18**</ins> Complex variety $$X$$에 대해 **cycle class map**

$$\cl: \operatorname{CH}_k(X) \to H^{\text{BM}}_{2k}(X, \mathbb{Z})$$

이 존재한다. 여기서 $$H^{\text{BM}}_\ast$$는 Borel–Moore homology이다. Borel–Moore homology는 일반적인 singular homology와 달리 비콤팩트 공간에서도 well-defined한 homology with closed support이며, $$2k$$ 차원이 등장하는 것은 $$k$$-dimensional algebraic cycle이 복소위상에서 실수 차원 $$2k$$를 갖는 것을 반영한다. $$X$$가 smooth projective variety이면 Poincaré duality에 의해 이는

$$\cl: \operatorname{CH}^k(X) \to H^{2k}(X, \mathbb{Z})$$

으로 볼 수 있다. 이 map은 일반적으로 injective도 surjective도 아니다. Hodge conjecture는 $$\cl$$의 image를 $$\mathbb{Q}$$-coefficients로 기술하는 것과 관련된 유명한 미해결 문제이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

자세한 구성과 증명은 [Ful, §19.1]을 참조하라.

</details>

## Chow ring

<div class="proposition" markdown="1">

<ins id="prop19">**명제 19**</ins> Smooth variety $$X$$에 대해 $$\operatorname{CH}^\ast(X) = \bigoplus_k \operatorname{CH}^k(X)$$는 intersection product에 대해 graded ring을 이룬다. Intersection product $$\operatorname{CH}^k(X) \times \operatorname{CH}^l(X) \to \operatorname{CH}^{k+l}(X)$$의 자세한 정의는 ([§Intersection Product](/ko/math/algebraic_varieties/intersection_product))에서 다룬다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

자세한 증명은 [Ful, §8.1]을 참조하라.

</details>

<div class="example" markdown="1">

<ins id="ex20">**예시 20 ($$\mathbb{P}^n$$)**</ins> $$\operatorname{CH}^\ast(\mathbb{P}^n) \cong \mathbb{Z}[H] / (H^{n+1})$$

여기서 $$H$$는 hyperplane class이다. $$H^k$$는 $$k$$-codimensional linear subspace를 나타낸다.

</div>

---

**참고문헌**

**[Ful]** W. Fulton, *Intersection Theory*, Springer, 1984.  
**[Har]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.
