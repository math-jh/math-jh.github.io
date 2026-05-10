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

직관적으로 이 정의는 [§인자, ⁋정의 3](/ko/math/algebraic_varieties/divisors#def3)을, $$Y$$를 ambient variety 삼아 반복한 것에 불과하며 따라서 해당 정의의 자연스러운 일반화이다. 다소 미묘한 부분은 해당 글의 도입에서 언급한 normality로, $$X$$가 좋은 (가령 normal) variety라 하더라도 $$X$$의 임의의 subvariety는 그러한 성질을 물려받지 않을 수 있으므로 이 경우에는 normalization이 조금 더 필수적으로 들어간다는 것이다. 이를 염두에 두고 다음을 정의한다. 

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> 두 $$k$$-cycle $$Z_1, Z_2$$가 *rationally equivalent*<sub>유리 동치</sub>라는 것은, $$X$$의 $$(k+1)$$-dimensional closed irreducible subvariety $$Y_j$$와 그 위의 rational function $$f_j \in \mathbb{K}(Y_j)^\ast$$들이 존재하여

$$Z_1 - Z_2 = \sum_j \divisor(f_j)$$

을 만족하는 것이다. 이를 $$Z_1 \sim_{\text{rat}} Z_2$$로 표기한다.

</div>

즉, divisor class group을 정의할 때와 마찬가지로 우리는 principal divisor만큼의 차이만 나는 divisor를 같은 것으로 볼 것이다. 이 동치관계는 이전 [\[대수다양체\] §인자, ⁋정의 9](/ko/math/algebraic_varieties/divisors#def9) 직후에 설명한 직관과 동일하게, homotopy의 개념을 대수기하학으로 옮겨온 것으로 생각할 수 있다.

그럼 다음 명제가 성립한다. 

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> Rational equivalence는 $$Z_k(X)$$ 위의 동치관계이다.

</div>

이에 대한 증명은 거의 [§인자, ⁋명제 8](/ko/math/algebraic_varieties/divisors#prop8)을 반복하는 것이므로 여기서는 생략하기로 한다. 이 명제의 결과로 우리는 드디어 다음을 정의할 수 있다. 

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> $$k$$번째 *Chow group*<sub>저우 군</sub> $$\CH_k(X)$$를 $$k$$-cycle들을 rational equivalence로 나눈 group

$$\CH_k(X) = Z_k(X) / \sim_{\text{rat}}$$

으로 정의한다. 

</div>

Codimension $$k$$ Chow group은 $$\CH^k(X) = \CH_{n-k}(X)$$로 정의하고, 위에서 말한 것과 같이 cohomology convention이 필요한 상황에서 주로 사용한다. 

## 함자성

대수위상에서 homology 및 cohomology는 임의의 연속함수에 대해 functoriality를 갖지만, Chow group은 그렇지 않다. Chow group은 **proper morphism**에 대해서만 pushforward functoriality를, **flat morphism**에 대해서만 pullback functoriality를 갖는다. 이는 algebraic variety의 위상적 특성(특히 Zariski topology) 때문이다. 

Variety 사이의 morphism $$f: X \to Y$$가 **proper**<sub>고유 사상</sub>이라는 것은, 대략적으로 말해 compactness의 상대적 버전이라고 생각할 수 있다. 그러나 algebraic variety에서 compactness는 위상수학과는 다르게 작동한다: Zariski topology에서는 Hausdorff 성질이 일반적으로 성립하지 않고, 따라서 일반적인 위상공간에서처럼 "닫힌 집합의 유한 부분집합" 정도로 생각할 수 없다. 대신 proper morphism은 "점들이 무한대로 도망가지 않는" 사상으로, base change 후에도 닫힌 사상으로 남는 (universally closed) 성질로 정의된다. 구체적인 예시로, $$\mathbb{A}^1 \hookrightarrow \mathbb{P}^1$$의 inclusion은 proper이 아닌데, 이는 $$x \to \infty$$로 갈 때 점이 projective line의 추가된 점, 즉 무한대로 도망가서 사라지기 때문이다. 반면 $$\mathbb{P}^n \to \operatorname{pt}$$는 projective space 자체가 compact하므로 점이 도망갈 곳이 없어 proper이다. 기억해둘 가장 중요한 사실은 **projective morphism은 항상 proper**이라는 것이다. 엄밀한 정의는 [§스킴 사상의 성질들](/ko/math/scheme_theory/properties_of_scheme_morphisms)을 참조하라.

왜 pushforward가 properness를 요구하는지를 이해하기 위해, 우리는 먼저 non-proper morphism에서 무엇이 잘못되는지 살펴 보아야 한다. 예를 들어 $$\mathbb{A}^1 \to \operatorname{pt}$$를 생각하자. 만약 이 사상에 대해 pushforward를 정의하려 한다면, $$[\mathbb{A}^1]$$를 점 하나에 대응시켜야 한다. 그러나 $$\mathbb{A}^1$$은 non-compact하여 그 위의 점들이 무한대로 도망갈 수 있으므로, 이 대응은 유한한 정수 계수를 가질 수 없다. 이는 Borel–Moore homology가 임의의 연속함수에 대해 covariant functoriality를 갖지 못하는 것과 정확히 같은 현상이다. 반면 proper morphism은 fiber가 유한한 개수의 점으로 구성되도록 강제하며, 따라서 $$V$$를 $$f(V)$$ 위로 본 후 "몇 겹으로 덮는지"를 세는 것이 가능해진다. [명제 6](#prop6)에서 등장하는 $$\deg(V/f(V))$$는 바로 이 겹침의 횟수를 센 것으로, residue field extension $$[\mathbb{K}(V) : \mathbb{K}(f(V))]$$를 통해 계산된다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> Proper morphism $$f: X \to Y$$에 대해 pushforward $$f_\ast: \CH_k(X) \to \CH_k(Y)$$가 존재한다. Subvariety $$V \subset X$$에 대해, $$f_\ast[V]$$는 $$f(V)$$ 위로 $$V$$를 "덮어씌우는" 것으로 생각할 수 있다. $$\dim f(V) = \dim V$$일 때 $$V$$는 $$f(V)$$를 $$\deg(V/f(V))$$겹으로 덮으며, 이때 $$f_\ast[V] = \deg(V/f(V)) \cdot [f(V)]$$이다. $$\dim f(V) < \dim V$$일 때는 $$f_\ast[V] = 0$$이다.

</div>

직관적으로, proper morphism은 "점이 도망가지 않으므로" $$V$$의 image $$f(V)$$ 위에 $$V$$가 유한하게 겹쳐지게 된다. $$\deg(V/f(V))$$는 이 겹침의 횟수, 즉 $$V$$가 $$f(V)$$를 몇 겹으로 덮는지를 센 것이다. 이 degree는 residue field extension $$[\mathbb{K}(V) : \mathbb{K}(f(V))]$$로 계산되며, properness가 없었다면 이 겹침이 무한해져 degree를 셀 수 없었을 것이다.

Morphism $$f: X \to Y$$가 **flat**<sub>평탄 사상</sub>이라는 것은, $$Y$$ 위의 각 점에 대한 fiber를 생각할 때 그 차원이 일정하고, $$Y$$의 parameter가 변함에 따라 fiber의 구조가 갑작스럽게 변하지 않고 부드럽게 바뀌는 사상이다. 예를 들어 $$y^2 = x^3 + t$$로 주어진 family를 보면, $$t \neq 0$$에서는 fiber가 smooth elliptic curve이지만 $$t = 0$$에서는 cusp singularity가 나타나면서 구조가 급격히 달라진다. 이러한 갑작스러운 특이점의 출현이 바로 flatness가 깨지는 전형적인 상황이다. 이와 같이 flat morphism은 fiber들이 일정한 차원을 유지하면서 smooth family를 이루는 직관을 갖는다. 엄밀한 정의는 [§스킴 사상의 성질들](/ko/math/scheme_theory/properties_of_scheme_morphisms)을 참조하라.

Pullback $f^\ast$가 flat morphism에 대해서만 정의되는 이유는, non-flat morphism에서는 base change 시 fiber의 차원이나 구조가 갑자기 달라질 수 있기 때문이다. 예를 들어 closed embedding $i: Z \hookrightarrow X$는 일반적으로 flat이 아닌데, 이 때 단순히 $[V \cap Z]$로 정의하면 intersection multiplicity를 놓치거나 차원이 예상과 다르게 될 수 있다. Flat morphism은 이런 갑작스러운 변화를 막아 pullback이 일관되게 정의되도록 한다.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> Flat morphism $$f: X \to Y$$에 대해 pullback $$f^\ast: \CH^k(Y) \to \CH^k(X)$$가 존재한다. Subvariety $$V \subset Y$$에 대해 $$f^\ast[V] = [f^{-1}(V)]$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

자세한 증명은 [Ful, §1.7]을 참조하라.

</details>

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8 (Localization Exact Sequence)**</ins> $$Z \subset X$$가 closed subvariety이고 $$U = X \setminus Z$$이면, 다음의 exact sequence가 성립한다:

$$\operatorname{CH}_k(Z) \xrightarrow{i_\ast} \operatorname{CH}_k(X) \xrightarrow{j^\ast} \operatorname{CH}_k(U) \to 0$$

여기서 $$i: Z \hookrightarrow X$$는 closed embedding이고 $$j: U \hookrightarrow X$$는 open embedding이다.

</div>

<div class="example" markdown="1">

<ins id="ex9">**예시 9**</ins> 우선 가장 친숙한 예시인 $$\mathbb{A}^n$$과 $$\mathbb{P}^n$$의 Chow group을 살펴보자. 

우선 affine space의 경우, 임의의 $$k$$-dimensional irreducible closed subvariety는 $$0$$과 rationally equivalent하다. 이를 위해 $$(k+1)$$-dimensional projective variety $$\mathbb{P}^1\times V$$를 생각하자.

먼저 $$k < n$$에 대해 $$\CH_k(\mathbb{A}^n) = 0$$이고, $$\CH_n(\mathbb{A}^n) \cong \mathbb{Z}$$이며 그 생성원은 $$\mathbb{A}^n$$ 자체이다. 이는 $$\Cl(\mathbb{A}^n) = 0$$ ([§인자, ⁋예시 10](/ko/math/algebraic_varieties/divisors#ex10))와 같은 정신이다. 구체적으로, $$V \subset \mathbb{A}^n$$를 $$k$$-dimensional irreducible closed subvariety라 하자. $$\mathbb{P}^1 \times V$$를 생각하면 이는 $$(k+1)$$-dimensional projective variety이다. $$\mathbb{P}^1$$의 coordinate $$t \in \mathbb{K}(\mathbb{P}^1)^\times$$를 $$\mathbb{P}^1 \times V$$로 pull-back하면 $$\divisor(t) = \{0\} \times V - \{\infty\} \times V$$가 되므로, $$\{0\} \times V$$와 $$\{\infty\} \times V$$는 rationally equivalent하다. $$\{0\} \times V$$를 $$\mathbb{A}^n$$에 대응시키면 $$V$$가 되고, $$\{\infty\} \times V$$는 $$\mathbb{A}^n$$의 compactification $$\mathbb{P}^n$$의 무한대 hyperplane에 해당하므로 $$\mathbb{A}^n$$ 안에서는 0으로 본다. 따라서 $$[V] \sim_{\text{rat}} 0$$이다.

한편 $$\mathbb{P}^n$$의 경우, 모든 $$k$$에 대해 $$\CH_k(\mathbb{P}^n) \cong \mathbb{Z}$$이다. $$k$$-dimensional linear subspace $$\mathbb{P}^k \subset \mathbb{P}^n$$를 $$\ell_k$$라 하자. 임의의 $$k$$-dimensional irreducible subvariety $$V \subset \mathbb{P}^n$$에 대해, 적당한 정수 $$d \geq 0$$이 존재하여 $$[V] \sim_{\text{rat}} d \cdot \ell_k$$이다. 이 정수 $$d$$는 $$V$$와 일반 위치의 $$(n-k)$$-dimensional linear subspace 사이의 intersection multiplicity ([§Intersection Product, ⁋정의 1](/ko/math/algebraic_varieties/intersection_product#def1))와 일치한다. 따라서 $$\CH_k(\mathbb{P}^n)$$는 $$[\ell_k]$$에 의해 생성되고 $$\mathbb{Z}$$와 동형이다. 이는 $$\Cl(\mathbb{P}^n) \cong \mathbb{Z}$$과 일치한다.

</div>

<div class="example" markdown="1">

<ins id="ex10">**예시 13 (Smooth curve)**</ins> Smooth projective curve $$C$$에 대해 $$\CH_1(C) \cong \mathbb{Z}$$이며 생성원은 $$C$$ 자체이고, $$\CH_0(C) \cong \Cl(C)$$이다.

</div>

<div class="example" markdown="1">

<ins id="ex11">**예시 11**</ins> Projection $$\pi: \mathbb{P}^1 \times \mathbb{P}^1 \to \mathbb{P}^1$$에 대해:

$$\pi_\ast[\mathbb{P}^1 \times \{p\}] = [p] \in \CH_0(\mathbb{P}^1) \cong \mathbb{Z}$$

잔여체 확대 차수가 $$[\mathbb{K}(\mathbb{P}^1 \times \{p\}) : \mathbb{K}(\{p\})] = 1$$이므로 계수가 $$\deg = 1$$이다. 즉, fiber $$\mathbb{P}^1 \times \{p\}$$가 한 점 위로 일대일로 대응되므로 pushforward가 순환의 차원을 유지하면서 그대로 내려보낸다.

</div>

## 다른 이론들과의 관계

<div class="proposition" markdown="1">

<ins id="prop12">**명제 12**</ins> Smooth variety $$X$$에 대해

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

<ins id="prop13">**명제 13**</ins> Complex variety $$X$$에 대해 **cycle class map**

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

<ins id="prop14">**명제 14**</ins> Smooth variety $$X$$에 대해 $$\CH^\ast(X) = \bigoplus_k \CH^k(X)$$는 intersection product에 대해 graded ring을 이룬다. Intersection product $$\CH^k(X) \times \CH^l(X) \to \CH^{k+l}(X)$$의 자세한 정의는 ([§Intersection Product](/ko/math/algebraic_varieties/intersection_product))에서 다룬다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

자세한 증명은 [Ful, §8.1]을 참조하라.

</details>

<div class="example" markdown="1">

<ins id="ex15">**예시 18 ($\mathbb{P}^n$)**</ins> $$\CH^\ast(\mathbb{P}^n) \cong \mathbb{Z}[H] / (H^{n+1})$$

여기서 $$H$$는 hyperplane class이다. $$H^k$$는 $$k$$-codimensional linear subspace를 나타낸다.

</div>

---

**참고문헌**

**[Ful]** W. Fulton, *Intersection Theory*, Springer, 1984.  
**[Har]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.
