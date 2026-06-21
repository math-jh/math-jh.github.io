---
title: "완전교차"
description: "Global section들의 가족이 정의하는 vanishing scheme, locally principal embedding과 effective Cartier divisor를 다루고, 정칙열로 잘리는 완전교차의 codimension이 자르는 방정식의 개수와 일치함을 보인다."
excerpt: "Vanishing scheme의 codimension과 complete intersection"

categories: [Math / Scheme Theory]
permalink: /ko/math/scheme_theory/complete_intersections
sidebar: 
    nav: "scheme_theory-ko"

date: 2025-03-08
weight: 15

published: false

drift_needed: true

---

닫힌 부분스킴의 중요한 예시 중 하나는 [§닫힌 부분스킴, ⁋정의 7](/ko/math/scheme_theory/closed_subschemes#def7)에서 정의한 vanishing scheme이며, 이에 대한 motivation은 당연히 유클리드 공간 $$\mathbb{R}^n$$과 그 위에서 정의되는 함수 $$f: \mathbb{R}^n \rightarrow \mathbb{R}$$에 대하여 $$f^{-1}(0)$$으로 정의되는 $$\mathbb{R}^n$$의 초곡면 $$f=0$$이다. 

한편 우리는 더 일반적으로 global section들의 (유한한) family $$s_1,\ldots, s_k\in \Gamma(X, \mathcal{O}_X)$$가 주어졌을 때 이들이 정의하는 vanishing scheme $$Z(s_1,\ldots, s_k)$$에도 관심이 있다. 직관적으로 이는 우선 $$X$$에서 global section $$s_1$$을 사용하여 만든 vanishing scheme $$\iota_1:Z(s_1)\hookrightarrow X$$을 생각한 후, $$Z(s_1)$$의 global section 

$$s_2\vert_{Z(s_1)}=\iota^\sharp(X)(s_2)\in(\iota_1)_\ast \mathcal{O}_{Z(s_1)}(X)=\Gamma(Z(s_1), \mathcal{O}_{Z(s_1)})$$

을 통해 $$Z(s_1)$$에서 $$s_2\vert_{Z(s_1)}$$의 vanishing scheme을 찾아나가는 것을 반복하여 얻어질 것이며, 물론 이를 위해서는 이 과정이 $$s_1, \ldots, s_k$$의 순서에 무관하게 같은 scheme을 주어야 할 것이다. 


## Locally principal embedding

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Closed embedding $$\iota: Z \hookrightarrow X$$가 *locally principal*이라는 것은 $$X$$의 적당한 open cover $$\{U_i\}$$가 존재하여, $$\iota$$의 공역을 각각의 $$U_i$$로 제한하여 얻어지는 closed embedding들

$$\iota\vert^{U_i}: \iota^{-1}(U_i) \rightarrow U_i$$

마다 적당한 $$s_i\in \Gamma(U_i, \mathcal{O}_X)$$가 존재하여 두 closed embedding $$\iota\vert^{U_i}$$와 $$Z(s_i)\hookrightarrow U_i$$가 isomorphic한 것이다. 

</div>

그럼 만일 $$\iota: Z\hookrightarrow X$$가 locally principal이라면, 정의의 $$U_i$$들 각각을 affine open set들로 덮고 $$s_i$$들을 이들로 제한시키면 $$\{U_i\}$$들이 affine open covering이라 가정하여도 된다. 

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> Closed embedding $$\iota: Z \hookrightarrow X$$가 *effective Cartier divisor*라는 것은 $$X$$의 affine open cover $$\{U_i=\Spec A_i\}$$가 존재하여, 각각의 closed embedding들

$$\iota\vert^{U_i}:\iota^{-1}(U_i) \rightarrow U_i$$

마다 적당한 non-zerodivisor $$s_i\in A_i=\Gamma(U_i, \mathcal{O}_X)$$가 존재하여 두 closed embedding $$\iota^{U_i}$$와 $$Z(s_i)\hookrightarrow U_i$$가 isomorphic한 것이다.

</div>

정의에 의해 locally principal embedding은 대략적으로 ideal sheaf가 (국소적으로는) 하나의 원소로 생성되는 것, 즉 principal ideal인 것이고 effective Cartier divisor는 적절한 affine cover를 잡으면 이 하나의 원소가 non-zerodivisor이도록 할 수 있는 것이다. 따라서 임의의 effective Cartier divisor는 locally principal이지만 그 역은 성립하지 않는다.

## 여차원과 완전교차

이제 도입부에서 예고한, 여러 global section들의 family가 정의하는 vanishing scheme을 구성한다. Scheme $$X$$와 global section들 $$s_1,\ldots, s_k\in \Gamma(X, \mathcal{O}_X)$$가 주어졌다 하자. 각 affine open set $$U=\Spec A$$ 위에서 $$s_i$$는 $$A$$의 원소 $$s_i\vert_U$$로 제한되며, 우리는 ideal $$(s_1\vert_U,\ldots, s_k\vert_U)$$가 정의하는 $$U$$의 closed subscheme을 생각할 수 있다. 이들은 $$U$$를 옮겨다닐 때 서로 합치되어 $$X$$의 closed subscheme을 정의하는데, 이를 $$Z(s_1,\ldots, s_k)$$로 적고 $$s_1,\ldots, s_k$$의 *vanishing scheme*이라 부른다. 정의하는 ideal $$(s_1,\ldots, s_k)$$는 $$s_i$$들의 순서에 무관하므로 $$Z(s_1,\ldots, s_k)$$ 또한 순서에 무관하며, 도입부에서 말한 "$$Z(s_1)$$에서 $$s_2$$의 vanishing scheme을 찾아나가는" 과정은 scheme-theoretic 교집합

$$Z(s_1,\ldots, s_k)=Z(s_1)\cap \cdots\cap Z(s_k)$$

으로 정확히 실현된다. 각 affine open 위에서 $$(s_1,\ldots, s_k)=\sum_{i=1}^k(s_i)$$이기 때문이다.

우선 $$k=1$$, 즉 하나의 non-zerodivisor가 정의하는 effective Cartier divisor의 여차원을 살펴본다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> Locally noetherian scheme $$X$$ 위의 effective Cartier divisor $$\iota:Z\hookrightarrow X$$에 대하여, $$Z$$의 모든 irreducible component는 $$X$$에서 codimension $$1$$을 갖는다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

여차원은 국소적으로 계산되므로, [정의 2](#def2)의 affine open cover $$\{U_i=\Spec A_i\}$$ 가운데 하나를 택하여 $$Z\cap U_i=Z(s_i)$$이고 $$s_i\in A_i$$가 non-zerodivisor인 경우만 보면 충분하다. $$Z$$의 irreducible component $$W$$가 $$U_i$$와 만난다면 $$W\cap U_i$$는 $$Z(s_i)$$의 irreducible component이다. [§차원, ⁋명제 11](/ko/math/scheme_theory/dimension#prop11)에 의하여 $$Z(s_i)$$의 component는 $$U_i$$에서 codimension $$0$$이거나 $$1$$인데, codimension $$0$$인 component는 $$U_i$$ 자신의 irreducible component, 즉 $$A_i$$의 minimal prime ideal $$\mathfrak{p}$$에 대응된다. 만일 $$W\cap U_i$$가 그러한 component라면 $$s_i$$가 그 위에서 소멸하므로 $$s_i\in \mathfrak{p}$$이다. 그런데 noetherian ring에서 non-zerodivisor는 어떠한 minimal prime ideal에도 속하지 않으므로 ([\[가환대수학\] §동반소아이디얼, ⁋정리 7](/ko/math/commutative_algebra/associated_primes#thm7)) 이는 $$s_i$$가 non-zerodivisor라는 가정에 모순이다. 따라서 $$W\cap U_i$$의 codimension은 $$1$$이고, [§차원, ⁋명제 7](/ko/math/scheme_theory/dimension#prop7)에 의하여 $$W$$의 $$X$$에서의 codimension 또한 $$1$$이다.

</details>

이제 이를 여러 번 잘라낸 일반적인 경우를 정의한다. 핵심은 자르는 section들이 단순한 non-zerodivisor를 넘어 *정칙열*을 이루어야 한다는 것이다.

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> Locally noetherian scheme $$X$$의 closed embedding $$\iota:Z\hookrightarrow X$$가 codimension $$k$$의 *완전교차<sub>complete intersection</sub>*, 혹은 codimension $$k$$의 *regular embedding*이라는 것은 $$X$$의 affine open cover $$\{U_i=\Spec A_i\}$$가 존재하여, 각각의 $$U_i$$에 대해 $$Z\cap U_i=Z(s_{i,1},\ldots, s_{i,k})$$이고 $$(s_{i,1},\ldots, s_{i,k})$$가 $$A_i$$-regular sequence ([\[가환대수학\] §정칙국소환, ⁋정의 2](/ko/math/commutative_algebra/regular_local_rings#def2))인 것이다.

</div>

엄밀히는 def4의 성질은 국소적으로만 정칙열을 요구하므로 *국소 완전교차<sub>local complete intersection</sub>*라 부르는 것이 정확하다. 한편 $$k=1$$의 완전교차는 정확히 effective Cartier divisor인데, regular sequence의 첫 원소는 그저 $$(s)$$가 proper이도록 하는 non-zerodivisor이기 때문이다. 다음 명제는 완전교차가 그 이름값을 한다는 것, 즉 codimension이 자르는 방정식의 개수와 정확히 일치함을 보여준다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> Codimension $$k$$의 완전교차 $$\iota:Z\hookrightarrow X$$의 모든 irreducible component는 $$X$$에서 codimension $$k$$를 갖는다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

다시 국소적이므로 [정의 4](#def4)의 cover 가운데 하나에 대해 $$X=\Spec A$$, $$Z=Z(s_1,\ldots, s_k)$$이고 $$(s_1,\ldots, s_k)$$가 $$A$$-regular sequence인 경우만 보면 충분하다. $$Z$$의 irreducible component $$W$$에 대응되는 $$A$$의 prime ideal을 $$\mathfrak{p}$$라 하면 $$\mathfrak{p}$$는 $$A/(s_1,\ldots, s_k)$$의 minimal prime이므로 

$$\dim A_\mathfrak{p}/(s_1,\ldots, s_k)=\dim\bigl(A/(s_1,\ldots, s_k)\bigr)_\mathfrak{p}=0$$

이다. 한편 [§차원, ⁋명제 7](/ko/math/scheme_theory/dimension#prop7)에 의하여 $$\codim_X W=\dim A_\mathfrak{p}$$이므로, $$\dim A_\mathfrak{p}=k$$임을 보이면 된다. 

이를 위해 다음 사실을 보인다.

> Noetherian local ring $$(R,\mathfrak{m})$$의 non-zerodivisor $$s\in\mathfrak{m}$$에 대하여 $$\dim R/(s)=\dim R-1$$이다.

[§차원, ⁋명제 11](/ko/math/scheme_theory/dimension#prop11)을 $$\Spec R$$에 적용하면 $$V(s)$$의 모든 component는 codimension $$0$$ 또는 $$1$$이고, $$s$$가 non-zerodivisor이므로 ([\[가환대수학\] §동반소아이디얼, ⁋정리 7](/ko/math/commutative_algebra/associated_primes#thm7)) $$s$$는 어떠한 minimal prime에도 속하지 않아 codimension $$0$$인 component는 없다. 따라서 $$V(s)$$의 모든 component는 codimension $$1$$이고, $$\dim R/(s)=\dim R-1$$이다. 

이제 $$(s_1,\ldots, s_k)$$가 $$A$$-regular sequence이므로 localization $$A_\mathfrak{p}$$에서도 regular sequence이며 (localization은 non-zerodivisor를 보존한다), 각 $$s_{i+1}$$은 $$A_\mathfrak{p}/(s_1,\ldots, s_i)$$의 non-zerodivisor이다. 위 사실을 $$i=0,1,\ldots, k-1$$에 차례로 적용하면 

$$0=\dim A_\mathfrak{p}/(s_1,\ldots, s_k)=\dim A_\mathfrak{p}-k$$

를 얻으므로 $$\dim A_\mathfrak{p}=k$$, 즉 $$\codim_X W=k$$이다.

</details>

<div class="example" markdown="1">

<ins id="ex6">**예시 6**</ins> 

1. 유클리드 공간 $$\mathbb{A}^n_\mathbb{K}=\Spec\mathbb{K}[\x_1,\ldots, \x_n]$$과 상수가 아닌 다항식 $$f$$를 생각하자. $$\mathbb{K}[\x_1,\ldots, \x_n]$$이 integral domain이므로 $$0\neq f$$는 non-zerodivisor이고, 따라서 초곡면 $$Z(f)\hookrightarrow\mathbb{A}^n_\mathbb{K}$$은 effective Cartier divisor, 즉 codimension $$1$$의 완전교차이다. 

2. 좌표부분공간 $$Z(\x_1,\ldots, \x_k)\hookrightarrow \mathbb{A}^n_\mathbb{K}$$를 생각하자. 각 $$i$$에 대하여 

	$$\mathbb{K}[\x_1,\ldots, \x_n]/(\x_1,\ldots, \x_i)\cong\mathbb{K}[\x_{i+1},\ldots, \x_n]$$

	은 integral domain이므로 $$\x_{i+1}$$은 이 환에서 non-zerodivisor이다. 즉 $$(\x_1,\ldots, \x_k)$$는 regular sequence이고, $$Z(\x_1,\ldots, \x_k)$$는 codimension $$k$$의 완전교차이다. [명제 5](#prop5)와 부합하게 이 부분공간의 codimension은 정확히 $$k$$이다. 

</div>

<div class="remark" markdown="1">

<ins id="rmk7">**참고 7**</ins> [정의 4](#def4)는 정칙열을 *국소적으로만* 요구한다. 이보다 강한 조건으로, projective scheme $$Z\subseteq \mathbb{P}^n$$이 codimension만큼의 동차다항식들의 vanishing으로 *대역적으로* 잘리는 경우를 *대역적 완전교차*라 부른다. 이 둘은 일치하지 않는다. 예를 들어 $$\mathbb{P}^3$$ 안의 꼬인 삼차곡선<sub>twisted cubic</sub>은 codimension $$2$$의 국소 완전교차이지만, 두 개의 동차다항식만으로는 잘리지 않아 대역적 완전교차는 아니다. 

</div>

