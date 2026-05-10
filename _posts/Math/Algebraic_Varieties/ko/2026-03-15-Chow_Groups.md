---
title: "저우 군"
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
weight: 18
published: false
---

앞서 우리는 [\[대수다양체\] §곡면에서의 리만-로흐 정리, ⁋정의 1](/ko/math/algebraic_varieties/riemann_roch_surfaces#def1)에서 두 divisor의 intersection number를 정의했다. 이는 당연히 아주 흥미로운 개념으로, 이번 글에서 우리는 임의의 variety 위에서 이 개념을 일반화하기 위해 *Chow group*을 정의한다. 

## 저우 군

[§인자, ⁋정의 1](/ko/math/algebraic_varieties/divisors#def1)에서 우리는 codimension 1 closed irreducible subvariety들의 formal sum을 (Weil) divisor로 정의하였고, 이들을 up to linear equivalence로 모아 divisor class group $$\Cl(X)$$를 정의했다. 이와 유사하게, Chow group은 $$k$$-dimensional closed irreducible subvariety들의 formal sum을 up to rational equivalence로 모아둔 것이다. 

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Variety $$X$$의 *algebraic $$k$$-cycle*<sub>대수적 $$k$$-순환</sub>은 $$X$$의 $$k$$-dimensional closed irreducible subvariety들의 formal sum

$$Z = \sum_{i} n_i V_i$$

이다. 여기서 $$V_i \subset X$$는 $$k$$-dimensional closed irreducible subvariety이고 $$n_i \in \mathbb{Z}$$이다. $$k$$-cycle들이 이루는 free abelian group을 $$Z_k(X)$$로 표기한다.

</div>

그 정의에 의해 algebraic $$k$$-cycle은 homology에 가까운 것이다. 만일 이를 (duality를 통해) cohomology의 관점에서 해석해야 할 일이 있을 때에는 *codimension $$k$$ cycle*<sub>여차원 $$k$$ 순환</sub>을 $$Z^k(X) = Z_{n-k}(X)$$ (단 $$n = \dim X$$)로 표기한다. 위에서 언급한 것과 같이 Chow group은 이들 $$Z_k(X)$$에 특정한 equivalence를 취하여 얻어지는 것이다. 

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> Variety $$X$$의 $$(k+1)$$-dimensional closed irreducible subvariety $$Y \subset X$$ 위의 rational function $$f \in \mathbb{K}(Y)^\ast$$에 대해 *principal cycle*<sub>주순환</sub> $$\divisor(f) \in Z_k(X)$$를 다음의 식

$$\divisor(f) = \sum_{V \subset Y, \dim V = k} v_V(f) \cdot V$$

으로 정의한다. 여기서 $$v_V(f)$$는 $$f$$의 $$V$$에서의 valuation이다. 

</div>

직관적으로 이 정의는 [§인자, ⁋정의 3](/ko/math/algebraic_varieties/divisors#def3)를, $$Y$$를 ambient variety 삼아 반복한 것에 불과하며 따라서 해당 정의의 자연스러운 일반화이다. 다소 미묘한 부분은 해당 글의 도입에서 언급한 normality로, $$X$$가 좋은 (가령 normal) variety라 하더라도 $$X$$의 임의의 subvariety는 그러한 성질을 물려받지 않을 수 있으므로 이 경우에는 normalization이 조금 더 필수적으로 들어간다는 것이다. 이를 염두에 두고 다음을 정의한다. 

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> 두 $$k$$-cycle $$Z_1, Z_2$$가 *rationally equivalent*<sub>유리 동치</sub>라는 것은, $$X$$의 $$(k+1)$$-dimensional closed irreducible subvariety $$Y_j$$와 그 위의 rational function $$f_j \in \mathbb{K}(Y_j)^\ast$$들이 존재하여

$$Z_1 - Z_2 = \sum_j \divisor(f_j)$$

을 만족하는 것이다. 이를 $$Z_1 \sim_{\text{rat}} Z_2$$로 표기한다.

</div>

즉, divisor class group을 정의할 때와 마찬가지로 우리는 principal divisor만큼의 차이만 나는 divisor를 같은 것으로 볼 것이다. 그럼 다음 명제가 성립한다. 

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> Rational equivalence는 $$Z_k(X)$$ 위의 동치관계이다.

</div>

이에 대한 증명은 거의 [§인자, ⁋명제 8](/ko/math/algebraic_varieties/divisors#prop8)를 반복하는 것이므로 여기서는 생략하기로 한다. 이 명제의 결과로 우리는 드디어 다음을 정의할 수 있다. 

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> $$k$$번째 *Chow group*<sub>저우 군</sub> $$\CH_k(X)$$를 $$k$$-cycle들을 rational equivalence로 나눈 group

$$\CH_k(X) = Z_k(X) / \sim_{\text{rat}}$$

으로 정의한다. 

</div>

Codimension $$k$$ Chow group은 $$\CH^k(X) = \CH_{n-k}(X)$$로 정의하고, 위에서 말한 것과 같이 cohomology convention이 필요한 상황에서 주로 사용한다. 다음은 Chow group의 예시들이다. 

<div class="example" markdown="1">

<ins id="ex6">**예시 6**</ins> 우선 가장 친숙한 예시인 $$\mathbb{A}^n$$과 $$\mathbb{P}^n$$의 Chow group을 살펴보자. 

먼저 $$k < n$$에 대해 $$\CH_k(\mathbb{A}^n) = 0$$이고, $$\CH_n(\mathbb{A}^n) \cong \mathbb{Z}$$이며 그 생성원은 $$\mathbb{A}^n$$ 자체이다. 이는 $$\Cl(\mathbb{A}^n) = 0$$ ([§인자, ⁋예시 10](/ko/math/algebraic_varieties/divisors#ex10))와 같은 정신이다. 구체적으로, $$V \subset \mathbb{A}^n$$를 $$k$$-dimensional irreducible closed subvariety라 하자. $$\mathbb{P}^1 \times V$$를 생각하면 이는 $$(k+1)$$-dimensional projective variety이다. $$\mathbb{P}^1$$의 coordinate $$t \in \mathbb{K}(\mathbb{P}^1)^\times$$를 $$\mathbb{P}^1 \times V$$로 pull-back하면 $$\divisor(t) = \{0\} \times V - \{\infty\} \times V$$가 되므로, $$\{0\} \times V$$와 $$\{\infty\} \times V$$는 rationally equivalent하다. $$\{0\} \times V$$를 $$\mathbb{A}^n$$에 대응시키면 $$V$$가 되고, $$\{\infty\} \times V$$는 $$\mathbb{A}^n$$의 compactification $$\mathbb{P}^n$$의 무한대 hyperplane에 해당하므로 $$\mathbb{A}^n$$ 안에서는 0으로 본다. 따라서 $$[V] \sim_{\text{rat}} 0$$이다.

한편 $$\mathbb{P}^n$$의 경우, 모든 $$k$$에 대해 $$\CH_k(\mathbb{P}^n) \cong \mathbb{Z}$$이다. $$k$$-dimensional linear subspace $$\mathbb{P}^k \subset \mathbb{P}^n$$를 $$\ell_k$$라 하자. 임의의 $$k$$-dimensional irreducible subvariety $$V \subset \mathbb{P}^n$$에 대해, 적당한 정수 $$d \geq 0$$이 존재하여 $$[V] \sim_{\text{rat}} d \cdot \ell_k$$이다. 이 정수 $$d$$는 $$V$$와 일반 위치의 $$(n-k)$$-dimensional linear subspace 사이의 intersection multiplicity ([§교차곱, ⁋정의 1](/ko/math/algebraic_varieties/intersection_product#def1))와 일치한다. 따라서 $$\CH_k(\mathbb{P}^n)$$는 $$[\ell_k]$$에 의해 생성되고 $$\mathbb{Z}$$와 동형이다. 이는 $$\Cl(\mathbb{P}^n) \cong \mathbb{Z}$$과 일치한다.

</div>

<div class="example" markdown="1">

<ins id="ex7">**예시 7 (Smooth curve)**</ins> Smooth projective curve $$C$$에 대해 $$\CH_1(C) \cong \mathbb{Z}$$이며 생성원은 $$C$$ 자체이고, $$\CH_0(C) \cong \Cl(C)$$이다.

</div>

## 함자성

<div class="definition" markdown="1">

<ins id="def8">**정의 8**</ins> Variety 사이의 morphism $$f: X \to Y$$가 *proper*<sub>고유 사상</sub>라는 것은, 임의의 base change $$Y' \to Y$$에 대해 유도된 사상 $$f_{Y'}: X \times_Y Y' \to Y'$$가 위상공간으로서 닫힌 사상이라는 뜻이다 (이를 *universally closed*라 한다). 기하적으로 proper morphism은 점들이 "무한대로 도피"하는 것을 허용하지 않는다: 닫힌 집합의 image는 항상 닫힌 집합이며, 이 성질은 base change 후에도 보존된다. 본 글에서 다루는 모든 variety는 separated이고 morphism은 finite type이라 가정하므로, 위 universally closed 조건만으로 proper의 정의가 완성된다. Projective morphism은 항상 proper이다.

</div>

<div class="definition" markdown="1">

<ins id="def9">**정의 9**</ins> Proper morphism $$f: X \to Y$$와 subvariety $$V \subset X$$에 대해, $$\dim f(V) = \dim V$$일 때 $$\deg(V/f(V))$$를 residue field extension degree로 정의한다:

$$\deg(V/f(V)) = [\mathbb{K}(V) : \mathbb{K}(f(V))]$$

이는 $$f$$가 $$V$$에서 $$f(V)$$로 유도하는 field extension의 차수이며, $$f(V)$$의 일반적인 점 위의 fiber에 들어있는 점의 수로 이해할 수 있다.

</div>

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10**</ins> Proper morphism $$f: X \to Y$$에 대해 pushforward $$f_\ast: \CH_k(X) \to \CH_k(Y)$$가 존재한다. Subvariety $$V \subset X$$에 대해

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

<ins id="def11">**정의 11**</ins> Morphism $$f: X \to Y$$가 *flat*<sub>평탄 사상</sub>이라는 것은, 임의의 점 $$x \in X$$에 대해 local ring $$\mathcal{O}_{X,x}$$가 $$\mathcal{O}_{Y,f(x)}$$-module로서 flat인 것이다. 즉, 임의의 $$\mathcal{O}_{Y,f(x)}$$-module들의 단사 사상 $$M \hookrightarrow N$$에 대해 $$M \otimes_{\mathcal{O}_{Y,f(x)}} \mathcal{O}_{X,x} \to N \otimes_{\mathcal{O}_{Y,f(x)}} \mathcal{O}_{X,x}$$도 단사 사상이다. 직관적으로, fiber의 차원이 일정하고, parameter를 연속적으로 변화시킬 때 fiber의 구조가 "연속적으로 변한다"는 것을 의미한다.

</div>

<div class="proposition" markdown="1">

<ins id="prop12">**명제 12**</ins> Flat morphism $$f: X \to Y$$에 대해 pullback $$f^\ast: \CH^k(Y) \to \CH^k(X)$$가 존재한다. 구체적으로, subvariety $$V \subset Y$$에 대해 $$f^\ast[V] = [f^{-1}(V)]$$이다. Flatness에 의해 $$\codim_X(f^{-1}(V)) = \codim_Y(V)$$가 보장되므로 codimension 표기 $$\CH^k$$로 보면 이 사상이 well-defined이다. (Dimension 표기로 보면 fiber의 relative dimension $$r$$만큼 차원이 증가하여 $$f^\ast: \CH_k(Y) \to \CH_{k+r}(X)$$이다.)

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

자세한 증명은 [Ful, §1.7]을 참조하라.

</details>

<div class="example" markdown="1">

<ins id="ex13">**예시 13**</ins> Projection $$\pi: \mathbb{P}^1 \times \mathbb{P}^1 \to \mathbb{P}^1$$에 대해:

$$\pi_\ast[\mathbb{P}^1 \times \{p\}] = [p] \in \CH_0(\mathbb{P}^1) \cong \mathbb{Z}$$

잔여체 확대 차수가 $$[\mathbb{K}(\mathbb{P}^1 \times \{p\}) : \mathbb{K}(\{p\})] = 1$$이므로 계수가 $$\deg = 1$$이다. 즉, fiber $$\mathbb{P}^1 \times \{p\}$$가 한 점 위로 일대일로 대응되므로 pushforward가 순환의 차원을 유지하면서 그대로 내려보낸다.

</div>

## 다른 이론들과의 관계

<div class="proposition" markdown="1">

<ins id="prop14">**명제 14**</ins> Smooth variety $$X$$에 대해

$$\CH^1(X) \cong \Cl(X) \cong \Pic(X)$$

이 성립한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$\CH^1(X) = \CH_{n-1}(X)$$는 codimension 1 closed irreducible subvariety(즉 Weil divisor의 성분)들의 rational equivalence에 의한 quotient group이다. $$X$$가 smooth이므로 모든 local ring이 regular이며, regular local ring이 UFD라는 사실에 의해 ([Hart, Theorem II.6.2A] 참조) $$X$$는 locally factorial이고, 따라서 Weil divisor와 Cartier divisor가 일치한다.

$$\Cl(X)$$는 Weil divisor들의 linear equivalence에 의한 quotient group이다. 두 동치 관계를 비교하자: rational equivalence는 임의의 $$(k+1)$$-dimensional subvariety $$Y$$ 위의 rational function $$f \in \mathbb{K}(Y)^\ast$$의 principal cycle $$\divisor(f)$$에 의해 생성되고, linear equivalence는 $$X$$ 자체 위의 rational function $$f \in \mathbb{K}(X)^\ast$$의 principal divisor $$\divisor(f)$$에 의해서만 생성된다.

하지만 codimension 1에서는 임의의 $$n$$-dimensional closed irreducible subvariety $$Y \subset X$$가 $$X$$ 자체뿐이므로 ($$\dim X = n$$), rational equivalence와 linear equivalence는 동일한 동치 관계이다. 따라서 $$\CH^1(X) \cong \Cl(X)$$. $$\Cl(X) \cong \Pic(X)$$는 ([§인자](/ko/math/algebraic_varieties/divisors))에서 이미 확인하였다.

</details>

<div class="proposition" markdown="1">

<ins id="prop15">**명제 15**</ins> Complex variety $$X$$에 대해 **cycle class map**

$$\cl: \CH_k(X) \to H^{\text{BM}}_{2k}(X, \mathbb{Z})$$

이 존재한다. 여기서 $$H^{\text{BM}}_\ast$$는 Borel–Moore homology이다. Borel–Moore homology는 일반적인 singular homology와 달리 비콤팩트 공간에서도 well-defined한 homology with closed support이며, $$2k$$ 차원이 등장하는 것은 $$k$$-dimensional algebraic cycle이 복소위상에서 실수 차원 $$2k$$를 갖는 것을 반영한다. $$X$$가 smooth projective variety이면 Poincaré duality에 의해 이는

$$\cl: \CH^k(X) \to H^{2k}(X, \mathbb{Z})$$

으로 볼 수 있다. 이 map은 일반적으로 injective도 surjective도 아니다. Hodge conjecture는 $$\cl$$의 image를 $$\mathbb{Q}$$-coefficients로 기술하는 것과 관련된 유명한 미해결 문제이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

자세한 구성과 증명은 [Ful, §19.1]을 참조하라.

</details>

## Chow ring

<div class="proposition" markdown="1">

<ins id="prop16">**명제 16**</ins> Smooth variety $$X$$에 대해 $$\CH^\ast(X) = \bigoplus_k \CH^k(X)$$는 intersection product에 대해 graded ring을 이룬다. Intersection product $$\CH^k(X) \times \CH^l(X) \to \CH^{k+l}(X)$$의 자세한 정의는 ([§Intersection Product](/ko/math/algebraic_varieties/intersection_product))에서 다룬다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

자세한 증명은 [Ful, §8.1]을 참조하라.

</details>

<div class="example" markdown="1">

<ins id="ex17">**예시 17 ($$\mathbb{P}^n$$)**</ins> $$\CH^\ast(\mathbb{P}^n) \cong \mathbb{Z}[H] / (H^{n+1})$$

여기서 $$H$$는 hyperplane class이다. $$H^k$$는 $$k$$-codimensional linear subspace를 나타낸다.

</div>

---

**참고문헌**

**[Ful]** W. Fulton, *Intersection Theory*, Springer, 1984.  
**[Har]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.
