---
title: "저우 군"
description: "다양체 위에서 divisor class group을 일반화한 Chow group을 정의하고, algebraic cycle과 rational equivalence의 개념을 통해 교차수를 임의의 다양체로 확장하는 방법을 다룬다."
excerpt: "Chow groups and the cycle class map"

categories: [Math / Algebraic Varieties]
permalink: /ko/math/algebraic_varieties/chow_groups
sidebar: 
    nav: "algebraic_varieties-ko"

header:
    overlay_image: /assets/images/Math/Algebraic_Varieties/Chow_Groups.png
    overlay_filter: 0.5

date: 2026-05-11
last_modified_at: 2026-05-11
weight: 18
---

앞서 우리는 [§곡면에서의 리만-로흐 정리, ⁋정의 1](/ko/math/algebraic_varieties/riemann_roch_surfaces#def1)에서 두 divisor의 intersection number를 정의했다. 이는 당연히 아주 흥미로운 개념으로, 이번 글에서 우리는 임의의 variety 위에서 이 개념을 일반화하기 위해 *Chow group*을 정의한다. 

## 저우 군

[§인자, ⁋정의 1](/ko/math/algebraic_varieties/divisors#def1)에서 우리는 codimension 1 closed irreducible subvariety들의 formal sum을 (Weil) divisor로 정의하였고, 이들을 up to linear equivalence로 모아 divisor class group $$\Cl(X)$$를 정의했다. 이와 유사하게, Chow group은 $$k$$-dimensional closed irreducible subvariety들의 formal sum을 up to rational equivalence로 모아둔 것이다. 

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Variety $$X$$의 *algebraic $$k$$-cycle*<sub>대수적 $k$-순환</sub>은 $$X$$의 $$k$$-dimensional closed irreducible subvariety들의 formal sum

$$Z = \sum_{i} n_i V_i$$

이다. 여기서 $$V_i \subset X$$는 $$k$$-dimensional closed irreducible subvariety이고 $$n_i \in \mathbb{Z}$$이다. $$k$$-cycle들이 이루는 free abelian group을 $$Z_k(X)$$로 표기한다.

</div>

그 정의에 의해 algebraic $$k$$-cycle은 homology에 가까운 것이다. 만일 이를 (duality를 통해) cohomology의 관점에서 해석해야 할 일이 있을 때에는 *codimension $$k$$ cycle*<sub>여차원 $k$ 순환</sub>을 $$Z^k(X) = Z_{n-k}(X)$$ (단 $$n = \dim X$$)로 표기한다. 위에서 언급한 것과 같이 Chow group은 이들 $$Z_k(X)$$에 특정한 equivalence를 취하여 얻어지는 것이다. 

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

즉, divisor class group을 정의할 때와 마찬가지로 우리는 principal divisor만큼의 차이만 나는 divisor를 같은 것으로 볼 것이다. 이 동치관계는 이전 [§인자, ⁋정의 9](/ko/math/algebraic_varieties/divisors#def9) 직후에 설명한 직관과 동일하게, homotopy의 개념을 대수기하학으로 옮겨온 것으로 생각할 수 있다.

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

대수위상에서 homology 및 cohomology는 임의의 연속함수에 대해 functoriality를 갖지만, Chow group은 그렇지 않다. Chow group은 **proper morphism**에 대해서만 pushforward functoriality를, **flat morphism**에 대해서만 pullback functoriality를 갖는다. 

우선 두 variety 사이의 morphism $$f: X \to Y$$가 *proper morphism*이라는 것은 대략적으로 compact map의 대수기하적 analogue라 할 수 있다. ([\[스킴\] §값매김환, ⁋정의 8](/ko/math/scheme_theory/valuative_criteria#def8)) 다소 주의할 것은, compactness의 경우 대수기하학에서는 잘 작동하지 않으므로 이를 곧바로 옮겨올 수는 없다는 것이다. 직관은 compact map의 fiber와 image가 무한대로 새어나가지 않듯이 proper morphism 또한 그러하다는 것이며, 특히 중요한 것은 이 fiber를 묘사하는 데 유한 개의 좌표만 추가적으로 필요하다는 것이다. ([\[스킴\] §스킴 사상의 성질들, ⁋예시 15](/ko/math/scheme_theory/properties_of_scheme_morphisms#ex15)) 이 때 필요한 좌표의 개수는 function field의 extension degree $$[\mathbb{K}(V):\mathbb{K}(f(V))]$$으로 계산되며, 이는 $$V$$와 $$f(V)$$가 같은 차원일 때 정의된다. 편의상

$$\deg(V/f(V))=\begin{cases}[\mathbb{K}(V):\mathbb{K}(f(V))]&\text{if $\dim f(V)=\dim V$,}\\ 0&\text{if $\dim f(V)<\dim V$}\end{cases}$$

으로 적으면, 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> Proper morphism $$f: X \to Y$$에 대해 pushforward $$f_\ast: \CH_k(X) \to \CH_k(Y)$$가 존재한다. 특히, 임의의 subvariety $$V\subset X$$에 대하여, 

$$f_\ast[V]=\deg(V/f(V))[f(V)]$$

가 성립한다. 

</div>

즉 직관적으로 proper morphism $$f$$를 통해 algebraic cycle $$[V]$$가 degree $$d$$만큼 겹쳐져 $$[f(V)]$$로 옮겨진다면 $$f_\ast[V]$$는 바로 이 degree를 잡아내는 것이다. 

이제 우리는 pullback을 살펴본다. 이는 homology convention보다는 cohomology convention에 가까운 것이므로, 우리는 codimension $$k$$ Chow group을 생각한다. Pullback $$f^\ast: \CH^k(Y)\rightarrow \CH^k(X)$$는 직관적으로 target $$Y$$의 cycle을 받은 후, 이를 fiber 방향으로 늘려주어 source에서의 cycle을 주는 것으로 생각할 수 있다. 그럼 이것이 잘 정의되기 위해서는 $$Y$$의 각 점에 대한 fiber의 차원이 일정하고, 또 $$Y$$의 각 점을 parameter로 볼 때, 이 parameter에 따라 fiber의 구조가 갑작스레 바뀌지 않아야 한다. *Flat morphism*이 바로 이러한 성질을 반영하는 morphism으로, 이러한 경우에 우리는 다음의 명제를 얻는다. 

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> Flat morphism $$f: X \to Y$$에 대해 pullback $$f^\ast: \CH^k(Y) \to \CH^k(X)$$가 존재한다. Subvariety $$V \subset Y$$에 대해 $$f^\ast[V] = [f^{-1}(V)]$$이다.

</div>

## 저우 군의 계산

우리는 지금까지 두 가지 종류의 functoriality를 살펴 보았는데, 이들을 함께 사용하면 Chow group의 구조를 더 잘 이해할 수 있다. 예를 들어 $$Z \subset X$$를 closed subvariety라 하고 $$U = X \setminus Z$$라 하자. 그럼 $$i: Z \hookrightarrow X$$는 closed embedding이므로 proper morphism이고, 따라서 pushforward $$i_\ast$$가 정의된다. 한편 $$j: U \hookrightarrow X$$는 open embedding이므로 flat morphism이고, 따라서 pullback $$j^\ast$$가 정의된다. 

여기서 한 가지 짚고 넘어갈 것은, 원래 pullback $$j^\ast$$는 cohomology convention $$\CH^k$$에 대해 정의되는 contravariant 연산이다. 그러나 open embedding의 경우에는 $$U$$가 $$X$$와 같은 차원을 가지므로, $$k$$-dimensional cycle을 그대로 $$U$$로 제한하는 것이 자연스럽게 정의된다. 

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8 (Localization Exact Sequence)**</ins> $$Z \subset X$$가 closed subvariety이고 $$U = X \setminus Z$$이면, 다음의 exact sequence가 성립한다:

$$\operatorname{CH}_k(Z) \xrightarrow{i_\ast} \operatorname{CH}_k(X) \xrightarrow{j^\ast} \operatorname{CH}_k(U) \to 0$$

여기서 $$i: Z \hookrightarrow X$$는 closed embedding이고 $$j: U \hookrightarrow X$$는 open embedding이다.

</div>

이 exact sequence가 성립하는 이유는 다음과 같다. 먼저 $$j^\ast$$가 surjective인 것은 자명하다. 더 중요한 것은 $$\ker j^\ast = \im i_\ast$$인 것으로, $$U$$에서 사라지는 cycle은 반드시 $$Z$$를 따라 쌓여있는 cycle들 뿐이라는 의미이며 이는 $$U$$가 $$X\setminus Z$$로 정의되었으므로 자명하다. 

다음 예시는 여러 Chow group을 계산할 때 기본 출발점이 된다. 

<div class="example" markdown="1">

<ins id="ex9">**예시 9**</ins> 가장 기본적인 예시로, 

$$\CH_k(\mathbb{A}^n)=\begin{cases}\mathbb{Z}&\text{if $k=n$}\\0&\text{otherwise}\end{cases}$$

그리고 

$$\CH_k(\mathbb{P}^n)=\mathbb{Z}\qquad\text{for all $0\leq k\leq n$}$$

이 성립한다. 이는 Euclidean space와 projective space의 homology와 일치하는 결과로, 우리가 정의한 Chow group이 실제로 기하적 직관을 잘 반영함을 보여준다. 

</div>

일반적으로

<div class="example" markdown="1">

<ins id="ex10">**예시 10**</ins> 위의 예시를 더 직관적으로 보기 위해 degree $$d$$ morphism $$f: \mathbb{P}^1 \to \mathbb{P}^1$$을

$$f([x:y]) = [x^d:y^d]$$

으로 정의하면 이는 proper이며, $$\mathbb{P}^1$$ 위의 coordinate $$t = x/y$$에 대해 $$f^\ast(t) = t^d$$이므로 field extension $$\mathbb{K}(\mathbb{P}^1) \hookrightarrow \mathbb{K}(\mathbb{P}^1)$$는 $$t \mapsto t^d$$에 의해 주어지고, 이 때의 extension degree는 $$d$$이다. 따라서 [명제 6](#prop6)에 의해

$$f_\ast[\mathbb{P}^1] = d \cdot [\mathbb{P}^1] \in \CH_1(\mathbb{P}^1) \cong \mathbb{Z}$$

가 성립한다. 즉, $$\mathbb{P}^1$$가 $$\mathbb{P}^1$$ 위로 $$d$$겹으로 덮혀지며, pushforward는 이를 잡아내는 역할을 한다.

</div>

그 정의에 의해 다음 명제는 거의 자명하다. 

<div class="proposition" markdown="1">

<ins id="prop11">**명제 11**</ins> Smooth variety $$X$$에 대해

$$\CH^1(X) \cong \Cl(X) \cong \Pic(X)$$

이 성립한다.

</div>

또, 우리는 [예시 9](#ex9)에서 $$\mathbb{A}^n$$과 $$\mathbb{P}^n$$의 경우 classical한 계산과 맞아떨어짐을 보았는데, 이는 다음과 같이 엄밀하게 formulate할 수 있다. 

<div class="proposition" markdown="1">

<ins id="prop12">**명제 12**</ins> Complex variety $$X$$에 대해 *cycle class map*

$$\cl: \CH_k(X) \to H^{\text{BM}}_{2k}(X, \mathbb{Z})$$

이 존재한다. 이는 algebraic cycle을 위상적으로 해석하는 사상으로, $$X$$가 smooth projective이면 Poincaré duality에 의해 $$\cl: \CH^k(X) \to H^{2k}(X, \mathbb{Z})$$로 볼 수 있다.

</div>

여기서 우변의 $$H^{\text{BM}}$$은 Borel-Moore homology로, singular homology와는 다르게 (non-compact 상황에서) closed oriented submanifold를 Borel-Moore homology에서의 class로 볼 수 있으며, 이런 관점에서 우리의 Chow group과는 singular cohomology보다는 Borel-Moore homology가 조금 더 맞는 analogue임을 알 수 있다. 또 $$X$$는 complex variety이므로 우변의 차원은 두 배가 되어 $$2k$$가 되는 것도 주목할 만하다.

## 저우 환

우리는 이번 글을 intersection product를 도입하기 위한 motivation으로서 다음 명제를 소개하며 마친다.

<div class="proposition" markdown="1">

<ins id="prop13">**명제 13**</ins> Smooth variety $$X$$에 대해 $$\CH^\ast(X) = \bigoplus_k \CH^k(X)$$는 intersection product에 대해 graded ring을 이룬다. ([§교차곱](/ko/math/algebraic_varieties/intersection_product))

</div>
 
이 ring 구조는 [명제 12](#prop12)와 마찬가지로 기존에 알고있던 cohomology ring 구조와도 맞아떨어진다. 

<div class="example" markdown="1">

<ins id="ex14">**예시 14 ($\mathbb{P}^n$)**</ins> $$\CH^\ast(\mathbb{P}^n) \cong \mathbb{Z}[H] / (H^{n+1})$$

여기서 $$H$$는 hyperplane class이다. $$H^k$$는 $$k$$-codimensional linear subspace를 나타낸다.

</div>

[명제 13](#prop13)의 intersection product는 다음 글에서 엄밀히 소개하게 될 것이다. 

---

**참고문헌**

**[Ful]** W. Fulton, *Intersection Theory*, Springer, 1984.  
**[Har]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.
