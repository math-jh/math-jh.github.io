---
title: "선다발과 벡터다발"
excerpt: "Line bundles, invertible sheaves, and the Picard group"

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/line_bundles
sidebar:
    nav: "algebraic_geometry-ko"

header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Line_Bundles.png
    overlay_filter: 0.5

date: 2026-03-15
last_modified_at: 2026-03-25
weight: 9

---

우리는 앞선 글에서 다양체 $X$ 위의 divisor들을 정의하고, 이들의 linear equivalence class들이 $\Cl(X)$를 이룸을 보았다. 그러나 모든 divisor가 어떤 유리함수의 zero/pole으로부터 오는 것은 아니다. 예를 들어 $\Cl(\mathbb{P}^n) \cong \mathbb{Z}$이므로 ([§인자, ⁋예시 11](/ko/math/algebraic_geometry/divisors#ex11)), $$\mathbb{P}^n$$에서 일반적인 divisor $dH$는 $d \ge 0$일 때만 어떤 함수의 zero set으로 나온다.

이러한 제약을 극복하기 위해 우리는 *line bundle*을 도입한다. Line bundle $\mathcal{L}$은 각 점 $p \in X$에 1차원 벡터공간을 대응시키는 기하학적 대상이며, $\mathcal{L}$의 section $s$는 자연스럽게 divisor $\divisor(s)$를 정의한다. 이 관점에서는 임의의 divisor $D$에 대해 $\mathcal{O}_X(D)$라는 line bundle을 만들 수 있고, 그 section들이 $D$보다 크거나 같은 divisor들에 대응된다. 즉, line bundle은 divisor를 함수의 zero 혹은 pole이라는 제약에서 벗어나 독립적으로 다룰 수 있게 해 준다.

## Line Bundle의 정의

Line bundle, 더 나아가 이 글의 뒷부분에서 정의할 vector bundle은 미분기하 등등의 다른 분야에서와 마찬가지 방식으로 정의된다. ([\[미분다양체\] §접다발과 여접다발, ⁋정의 1](/ko/math/manifold/tangent_and_cotangent_bundles#def1) 혹은 [\[대수적 위상수학\] §특성류, ⁋정의 2](/ko/math/algebraic_topology/characteristic_classes#def2) 등등)

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Variety $$X$$ 위의 *line bundle* $$\mathcal{L}$$은 다음과 같은 데이터로 구성된다.

1. Projection $$\pi: \mathcal{L} \to X$$.
2. $$X$$의 open cover $$\{U_i\}$$와 각 $$i$$에 대한 *local trivialization* $$\phi_i: \pi^{-1}(U_i) \overset{\sim}{\longrightarrow} U_i \times \mathbb{A}^1$$. 이들이 정의하는
    
    $$\phi_j \circ \phi_i^{-1}: (U_i \cap U_j) \times \mathbb{A}^1 \to (U_i \cap U_j) \times \mathbb{A}^1$$

    는 적당한 *transition function* $$g_{ij} \in \mathcal{O}_X(U_i \cap U_j)^\ast$$에 대하여 $$(p, t) \mapsto (p, g_{ij}(p)t)$$의 꼴이다.

</div>

두 line bundle $\mathcal{L}, \mathcal{M} \to X$ 사이의 *morphism* $\varphi \colon \mathcal{L} \to \mathcal{M}$은 각 점 $p \in X$에서 fiber 사이의 $\mathbb{K}$-linear map $\varphi_p \colon \mathcal{L}_p \to \mathcal{M}_p$를 정의하며, 적당한 open cover $\{U_k\}$ 위에서 $\mathcal{O}_X(U_k)$-module homomorphism

$$\varphi_k \colon \mathcal{O}_{U_k} \to \mathcal{O}_{U_k}$$

으로 표현될 수 있고, 이들 사이에

$$g^{\mathcal{M}}_{kl} \circ \varphi_l = \varphi_k \circ g^{\mathcal{L}}_{kl}$$

이 성립한다. Line bundle의 fiber는 1차원이므로, 각 $\varphi_k$는 적당한 $h_k \in \mathcal{O}_X(U_k)$에 의한 곱셈 $s \mapsto h_k s$로 주어진다. $\varphi$가 각 fiber에서 bijective일 때, 이를 *isomorphism*이라 부르고 $\mathcal{L} \cong \mathcal{M}$으로 표기한다. Fiber가 1차원이므로 이는 각 점에서 nonzero scalar를 주는 것과 같으며, 즉 compatible하게 $h_k \in \mathcal{O}_X(U_k)^\ast$를 선택하는 것과 동치이다.

그럼 다음 명제는 cocycle condition의 정의로부터 직접 확인된다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2 (Cocycle condition)**</ins> Transition functions $$\{g_{ij}\}$$는 다음의 *cocycle condition*을 만족한다.

1. $$g_{ii} = 1$$ for all $$i$$.
2. $$g_{ij} = g_{ji}^{-1}$$ for all $$i, j$$.
3. $$g_{ij} g_{jk} = g_{ik}$$ on $$U_i \cap U_j \cap U_k$$ for all $$i, j, k$$.

</div>

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> *Trivial line bundle* $$\mathcal{O}_X = X \times \mathbb{A}^1$$은 모든 transition function이 $$g_{ij} = 1$$인 line bundle이다. 이는 twist가 없는 가장 간단한 line bundle이다. 

</div>

따라서 [정의 1](#def1)의 둘째 조건은 line bundle $\mathcal{L}$이 적당한 열린집합 $U \subseteq X$로 제한했을 때 trivial line bundle과 isomorphic한 것을 의미한다.

[명제 2](#prop2)는 흔한 gluing condition으로, 이 조건에 의해 line bundle은 일종의 sheaf로 생각할 수 있다. ([\[위상수학\] §층, ⁋정의 1](/ko/math/topology/sheaves#def1)) 구체적으로, 우리는 line bundle $$\mathcal{L}$$이 주어졌을 때, 이 line bundle의 section sheaf를

$$U\mapsto \mathcal{O}_X(\mathcal{L})(U)=\{s: U \to \mathcal{L} \mid \pi \circ s = \id_U\}$$

으로 정의한다. 즉 $$\mathcal{O}_X(\mathcal{L})$$은 surjection $$\pi$$의 section들의 sheaf이다. ([\[위상수학\] §층, ⁋예시 9](/ko/math/topology/sheaves#ex9))

그럼 Local trivialization $$\phi_i: \pi^{-1}(U_i) \to U_i \times \mathbb{A}^1$$에 의해 $$\mathcal{O}_X(\mathcal{L})\vert_{U_i} \cong \mathcal{O}_{U_i}$$이다. 이를 통해 우리는 $$U_i$$ 위에서는 국소적으로 이 section들을 일상적인 $$\mathbb{K}$$-valued 함수처럼 생각할 수 있다. 

이는 다음을 의미한다. 

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> Sheaf $$\mathcal{F}$$가 *invertible*이라는 것은 각 점 $$p \in X$$의 근방 $$U$$에서 $$\mathcal{F}\vert_U \cong \mathcal{O}_U$$인 것이다. 

</div>

위에서 우리가 보인 것은 line bundle의 section sheaf는 invertible이라는 것이다. 다음 명제는 그 역 또한 성립한다는 것을 보여준다. 

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> Line bundle $$\mathcal{L}$$의 section sheaf $$\mathcal{O}_X(\mathcal{L})$$은 invertible sheaf이다. 역으로, 모든 invertible sheaf는 유일한 line bundle로부터 온다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Invertible sheaf $$\mathcal{F}$$에 대하여, local isomorphism $$\mathcal{F}\vert_{U_i} \cong \mathcal{O}_{U_i}$$들로부터 transition functions을 정의할 수 있고, 이로부터 line bundle을 재구성할 수 있다.

</details>

이 명제에 의해 우리는 line bundle과 invertible sheaf가 같은 개념인 것을 안다. 관습적으로 $$\mathcal{L}$$로 표기할 때는 line bundle으로 부르고, $$\mathcal{O}_X(\mathcal{L})$$로 표기할 때는 invertible sheaf라 불러서 그 맥락을 강조한다.

## Line bundle의 연산

미분기하의 세계에서는 fiberwise하게 선형대수에서의 연산을 가져와서 새로운 bundle을 구성하는 것이 자연스럽다. 대수기하에서도 마찬가지인데, 우선 우리는 line bundle의 경우를 살펴보고 있으므로 지금 살펴봐야 할 것은 $$\otimes$$와 $$\Hom$$, 그 중에서도 dual $$(-)^\vee$$이다. 

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> 두 line bundle $$\mathcal{L}, \mathcal{M}$$의 tensor product $$\mathcal{L} \otimes \mathcal{M}$$도 line bundle이다. 그 transition functions은 $$\{g_{ij} h_{ij}\}$$이다. 여기서 $$\{g_{ij}\}, \{h_{ij}\}$$는 각각 $$\mathcal{L}, \mathcal{M}$$의 transition functions이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

Tensor product의 fiber는 $$\mathcal{L}_p \otimes_{\mathbb{K}} \mathcal{M}_p$$이고, 이는 두 1차원 벡터공간의 tensor product이므로 다시 1차원이다. Transition function은 $$\phi_j \circ \phi_i^{-1}$$과 $$\psi_j \circ \psi_i^{-1}$$의 곱이 되므로 $$g_{ij} h_{ij}$$이다.

</details>

임의의 line bundle $$\mathcal{L}$$에 대하여, $$\mathcal{L}$$의 dual bundle $$\mathcal{L}^\vee$$는 각 fiber가

$$\mathcal{L}_x^\vee=\Hom_\mathbb{K}(\mathcal{L}_x, \mathbb{K})$$

로 주어지는 bundle이다. 만일 [명제 5](#prop5)를 따라 line bundle들을 (invertible) sheaf로 생각한다면 $$\mathcal{L}^\vee$$는 sheaf Hom $$\sHom_{\mathcal{O}_X}(\mathcal{L}, \mathcal{O}_X)$$에 해당하는 line bundle이다. 

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> Line bundle $$\mathcal{L}$$의 *dual bundle* $$\mathcal{L}^\vee$$도 line bundle이며, 그 transition functions은 $$\{g_{ij}^{-1}\}$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Dual bundle의 fiber는 $$\mathcal{L}_p^\vee = \Hom_{\mathbb{K}}(\mathcal{L}_p, \mathbb{K})$$이고, 이는 1차원 벡터공간의 dual이므로 다시 1차원이다. Transition function은 $$g_{ij}$$의 inverse이다.

</details>

이제 다음 명제는 $$\otimes$$와 $$(-)^\vee$$의 관계를 보여주며, 이 관계는 Picard group을 정의할 때 중요한 역할을 한다. 

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> 임의의 line bundle $$\mathcal{L}$$에 대해 $$\mathcal{L} \otimes \mathcal{L}^\vee \cong \mathcal{O}_X$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$\mathcal{L} \otimes \mathcal{L}^\vee$$의 transition functions은 $$g_{ij} \cdot g_{ij}^{-1} = 1$$이므로 trivial bundle이다.

</details>

언제나와 마찬가지로, line bundle 또한 충분히 작은 affine open set 위에서 살펴보아 그 구조를 이해할 수 있다. Line bundle $$\mathcal{L}$$을 생각하고, $$\mathcal{L}$$이 trivial이도록 하는 affine open subset $$U_i$$를 택하자. 그럼 projection map

$$\pi\vert_{\pi^{-1}(U_i)}:\pi^{-1}(U_i) \rightarrow U_i$$

는 affine variety 사이의 함수이고 따라서 [§아핀다양체, ⁋명제 16](/ko/math/algebraic_geometry/affine_varieties#prop19)로부터 coordinate ring 사이의 ring homomorphism이 유도된다. 이 ring homomorphism은 $$\pi^{-1}(U_i)$$의 coordinate ring을 $$U_i$$의 coordinate ring을 계수로 갖는 module로 만들고, 차원을 고려해보면 그 rank는 1이다. $$U_i$$의 임의의 열린집합에서도 $$\mathcal{L}$$은 trivial하므로, 우리는 line bundle은 affine-local하게는 coordinate ring 위의 invertible module이 된다는 것을 확인할 수 있다. ([\[가환대수학\] §분수아이디얼, ⁋정의 1](/ko/math/commutative_algebra/fractional_ideals#def1)) 그럼 이 때 line bundle들 위에서 정의되는 연산 $$\otimes$$와 $$\vee$$는 각각 [\[가환대수학\] §분수아이디얼, ⁋정리 3](/ko/math/commutative_algebra/fractional_ideals#thm3)의 연산으로부터 오는 것이며, 따라서 [\[가환대수학\] §분수아이디얼, ⁋정의 5](/ko/math/commutative_algebra/fractional_ideals#def5)을 따라 다음의 이름을 붙이는 것이 어색하지 않다.

<div class="definition" markdown="1">

<ins id="def9">**정의 9**</ins> Variety $$X$$의 *Picard group* $$\Pic(X)$$는 $$X$$ 위의 line bundle들의 isomorphism class들의 집합에 tensor product를 연산으로 하여 얻어진 group이다. 항등원은 trivial bundle $$\mathcal{O}_X$$이고, $$\mathcal{L}$$의 inverse는 $$\mathcal{L}^\vee$$이다.

</div>

여기서 trivial bundle이 실제로 항등원의 역할을 한다는 것은 [예시 3](#ex3)과 [명제 6](#prop6)에 의해 직접 확인된다. 뿐만 아니라, tensor product의 성질에 의해 다음이 성립한다. 

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10**</ins> $$\Pic(X)$$는 abelian group이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

[명제 6](#prop6)에 의해 tensor product은 line bundle들의 이항연산이며, [명제 8](#prop8)에 의해 $$\mathcal{O}_X$$가 항등원이고 $$\mathcal{L}^\vee$$가 $$\mathcal{L}$$의 역원이다. Tensor product의 교환법칙 $$\mathcal{L} \otimes \mathcal{M} \cong \mathcal{M} \otimes \mathcal{L}$$과 결합법칙 $$(\mathcal{L} \otimes \mathcal{M}) \otimes \mathcal{N} \cong \mathcal{L} \otimes (\mathcal{M} \otimes \mathcal{N})$$은 transition functions의 수준에서 $$g_{ij}h_{ij} = h_{ij}g_{ij}$$ 및 $$(g_{ij}h_{ij})k_{ij} = g_{ij}(h_{ij}k_{ij})$$로부터 직접 얻어진다.

</details>

앞선 글에서와 마찬가지로, 우리의 toy example은 $$\mathbb{A}^n$$과 $$\mathbb{P}^n$$이다. 

<div class="example" markdown="1">

<ins id="ex11">**예시 11**</ins> $$\mathbb{A}^n$$의 coordinate ring $$R = \mathbb{K}[\x_1, \ldots, \x_n]$$은 UFD이며, 위 논의에 의해 $$\mathbb{A}^n$$ 위의 line bundle은 $$R$$ 위의 invertible module과 correspondence한다. ([\[가환대수학\] §분수아이디얼, ⁋정리 4](/ko/math/commutative_algebra/fractional_ideals#thm4))에 의해 UFD 위의 invertible module은 free이므로, $$\Pic(\mathbb{A}^n) = 0$$이다.

</div>


<div class="example" markdown="1">

<ins id="ex12">**예시 12**</ins> $$\mathbb{P}^n$$의 line bundle $$\mathcal{O}_{\mathbb{P}^n}(d)$$를 다음과 같이 정의한다. 우선 각각의 standard open cover

$$U_i = \{[x_0 : \cdots : x_n] \mid x_i \ne 0\}$$

가 이 bundle의 trivializing open set이다. 즉, 이들 위에서 $$\mathcal{O}_{\mathbb{P}^n}(d)$$는 trivial line bundle이다. 이제 이들 사이의 transition map은 각각의 $$U_i \cap U_j$$에서 $$\mathcal{O}_{U_j}\vert_{U_i \cap U_j} \to \mathcal{O}_{U_i}\vert_{U_i \cap U_j}$$를 다음의 식

$$g_{ij}: f\mapsto (x_i/x_j)^df $$

로 정의한다. 즉, 각 점 $$x \in U_i \cap U_j$$와 그 점에서의 fiber $$v \in \mathcal{O}_{\mathbb{P}^n}(d)_x\cong \mathbb{A}^1$$에 대하여, transition map은

$$g_{ij}(x): v \mapsto (x_i/x_j)^d(x) \cdot v$$

로 주어진다. 이러한 방식으로 우리는 group homomorphism 

$$\mathbb{Z}\rightarrow \Pic(\mathbb{P}^n);\qquad d\mapsto [\mathcal{O}_{\mathbb{P}^n}(d)]$$

을 정의할 수 있다. 

우리의 주장은 이것이 isomorphism이라는 것이다. 우선 임의의 line bundle $$\mathcal{L}$$에 대하여, $$\mathcal{L}\vert_{U_i}$$는 [예시 11](#ex11)에 의해 trivial line bundle과 isomorphic하므로, 각각의 $$U_i\cap U_j$$의 transition function $$h_{ij}$$가 $$\mathcal{L}$$을 완전히 결정한다. 그런데 정의에 의해 $$U_i\cap U_j$$에서 $$h_{ij}\in \mathcal{O}_{\mathbb{P}^n}(U_i\cap U_j)^\ast$$이므로 $$h_{ij}$$는 반드시 $$c_{ij}(x_i/x_j)^d$$ 꼴이다. 이 때 transition function이 상수배인 line bundle은 trivial하므로 이로부터 위의 group homomorphism이 surjective인 것을 안다. 비슷하게, $$\mathcal{O}_{\mathbb{P}^n}(d)\cong \mathcal{O}_{\mathbb{P}^n}(d')$$라 두고 transition function을 비교해보면, 

$$\mathcal{O}_{\mathbb{P}^n}(d-d')\cong \mathcal{O}_{\mathbb{P}^n}(d)\otimes \mathcal{O}_{\mathbb{P}^n}(-d')\cong \mathcal{O}_{\mathbb{P}^n}(d)\otimes \mathcal{O}_{\mathbb{P}^n}(d')^\vee\cong \mathcal{O}_{\mathbb{P}^n}$$

이기 위해서는 반드시 $$d-d'=0$$이어야 하므로 이는 injective하기도 하다. 

</div>

직관적으로, $$\mathbb{P}^n$$의 line bundle $$\mathcal{O}_{\mathbb{P}^n}(d)$$에서의 정수 $$d$$는 fiber가 base를 따라 이동할 때 꼬이는 횟수를 측정하는 지표로 이해할 수 있다. $$d=0$$일 때 $$\mathcal{O}(0)$$는 trivial bundle이므로 꼬임이 없고, $$d>0$$이면 한 방향으로 $$d$$번 꼬이며 $$d<0$$이면 반대 방향으로 $$\lvert d\rvert$$번 꼬인다. 이는 transition function $$g_{ij}(x) = (x_i/x_j)^d(x)$$에서 $$d$$가 꼬임의 정도를 직접적으로 나타냄을 뜻한다. 다만 이 직관은 다소 부정확할 수 있으므로 [예시 16](#ex16) 이후에 약간의 설명을 보충해야 한다. 

한편 projective space $$\mathbb{P}^n$$ 위에는 그 정의 자체로부터 자연스럽게 유도되는 특별한 line bundle이 존재한다. 이 *tautological bundle*은 $$\mathbb{P}^n$$의 각 점이 나타내는 직선을 그 점에 대응시키는 bundle로, projective space의 기하학을 이해하는 데 근본적인 역할을 한다.

<div class="definition" markdown="1">

<ins id="def13">**정의 13**</ins> $$\mathbb{P}^n$$의 각 점 $$x = [x_0 : \cdots : x_n]$$은 $$\mathbb{A}^{n+1}$$의 원점을 지나는 직선 $$\ell_x = \{(\lambda x_0, \ldots, \lambda x_n) \mid \lambda \in \mathbb{K}\}$$을 각 점에 달아준 공간 

$$\mathcal{O}_{\mathbb{P}^n}(-1) = \{(x, v) \in \mathbb{P}^n \times \mathbb{A}^{n+1} \mid v \in \ell_x\}$$

을 생각하자. 그럼 $$\mathcal{O}_{\mathbb{P}^n}(-1)$$에서 $$\mathbb{P}^n$$으로의 projection map $$\pi=\pr_1$$이 정의하는 line bundle을 $$\mathbb{P}^n$$ 위의 *tautological line bundle*이라 부른다.

</div>

즉, 이 정의에서 각 fiber $$\mathcal{O}_{\mathbb{P}^n}(-1)_x$$는 점 $$x$$가 나타내는 직선 그 자체이다. 그 표기가 알려주듯, 다음이 성립한다. 구별을 위해 다음 명제에서만은 $$\mathcal{O}_{\mathbb{P}^n}(-1)$$은 [예시 12](#ex12)가 아니라 [정의 13](#def13)의 bundle인 것으로 생각하자. 

<div class="proposition" markdown="1">

<ins id="prop14">**명제 14**</ins> Tautological bundle $$\mathcal{O}_{\mathbb{P}^n}(-1)$$은 위 [예시 12](#ex12)에서 정의한 $$\mathcal{O}_{\mathbb{P}^n}(1)$$의 dual이다. 즉, $$\mathcal{O}_{\mathbb{P}^n}(-1) \cong \mathcal{O}_{\mathbb{P}^n}(1)^\vee$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Standard open cover $$U_i = \{x \mid x_i \ne 0\}$$ 위에서 $$\mathcal{O}_{\mathbb{P}^n}(-1)$$의 local trivialization을 구성하자. 임의의 $$(x, v) \in \mathcal{O}_{\mathbb{P}^n}(-1)$$에 대해 $$v = \lambda x$$ ($$\lambda \in \mathbb{K}$$)로 쓸 수 있으므로, $$\phi_i(x, v) = (x, v_i)$$로 정의하면 $$\phi_i: \pi^{-1}(U_i) \to U_i \times \mathbb{A}^1$$이 된다. 역사상은 $$\phi_i^{-1}(x, t) = (x, (t/x_i)\, x)$$이다. $$U_i \cap U_j$$에서의 transition function은 $$\phi_j \circ \phi_i^{-1}(x, t) = (x, t x_j / x_i)$$에서 $$g_{ij}(x) = x_j/x_i$$를 얻는다. 이는 $$\mathcal{O}_{\mathbb{P}^n}(1)$$의 transition function $$x_i/x_j$$의 inverse이다.

</details>

특히 $$\mathbb{P}^1$$의 경우에서 $$\mathcal{O}(-1)$$을 살펴보면 위에서 직관적으로 설명한 <em-ko>꼬임</em-ko>의 의미가 훨씬 명확하다. $$\mathbb{A}^2\setminus \{0\}$$에서 $$\mathbb{P}^1$$을 만드는 과정은 우선, $$\mathbb{A}^2\setminus\{0\}$$을 radial projection을 통해 단위원으로 만든 후, 단위원의 antipodal point들을 identify하는 것으로 생각할 수 있는데, 이 과정에서 반대방향의 두 벡터가 identify되는 일, 즉 fiber가 꼬이는 일이 발생하기 때문이다. 이러한 꼬임을 보는 방법 중 하나는 line bundle $$\mathcal{L}$$의 section을 보는 것이다. 

<div class="definition" markdown="1">

<ins id="def15">**정의 15**</ins> Line bundle $$\mathcal{L}$$의 *global section*들의 공간을 $$\Gamma(X, \mathcal{L})$$로 표기한다. 즉, $$\Gamma(X, \mathcal{L})$$는 각 점 $$x\in X$$마다 fiber $$\pi^{-1}(x)\subset \mathcal{L}$$ 내의 원소를 대응시키는 regular map들의 집합이다.

</div>

Global section space의 또 다른 대중적인 표기법 중 하나는 $$H^0(X, \mathcal{L})$$이다. 이 표기법은 [§층 코호몰로지, ⁋정의 1](/ko/math/algebraic_geometry/sheaf_cohomology#def1)에서 정당화될 것이나, 그 전까지는 $$\Gamam(X, \mathcal{L})$$을 사용하기로 한다. 

<div class="example" markdown="1">

<ins id="ex16">**예시 16**</ins> $$\mathcal{O}_{\mathbb{P}^n}(-1)$$의 global section은 $$0$$뿐이다. 즉,

$$\Gamma(\mathbb{P}^n, \mathcal{O}_{\mathbb{P}^n}(-1)) = 0$$

이다. 이를 확인하기 위해 우리는 [명제 14](#prop14)에서 구한 transition function $$g_{ij} = \x_j/\x_i$$를 사용한다. Global section $$s$$는 각 $$U_i$$에서

$$s_i \in \mathcal{O}(U_i) = \mathbb{K}[\x_0/\x_i, \ldots, \x_n/\x_i]$$

로 표현되고, $$U_i \cap U_j$$에서 $$s_j = (\x_i/\x_j)\, s_i$$를 만족해야 한다. $$\mathcal{O}(U_i) \to \mathcal{O}(U_i \cap U_j)$$가 embedding이므로, $$(\x_j/\x_i)\, s_i$$가 $$\mathcal{O}(U_j) = \mathbb{K}[\x_0/\x_j, \ldots, \x_n/\x_j]$$에 속해야 한다. 이는 $$s_i$$가 homogeneous degree $$-1$$ 항만 가져야 함을 의미하지만, $$\mathcal{O}(U_i)$$는 degree $$\geq 0$$ 항들만 포함하므로 $$s_i = 0$$이다. 

</div>

이 명제는 tautological bundle의 <em-ko>꼬임</em-ko>을 section의 관점에서 보여준다. 가령, $$\Gamma(\mathbb{P}^1, \mathcal{O}(-1))=0$$이라는 사실은 특히 모든 $$x\in \mathbb{P}^1$$마다 fiber의 1을 대응시키는 "상수함수" 또한 존재하지 않는다는 것을 의미한다. 이는, 위의 기하학적 관점에서 보면, $$\mathbb{P}^1$$을 한 바퀴를 돌아왔을 때 원래의 1이 아니라 (예를 들면) $$-1$$이 되어있기 때문이다.

한편 [예시 16](#ex16)의 계산은 임의의 $$d$$에 대해서도 확장할 수 있는데, 특히 임의의 $$d<0$$에 대하여 $$\Gamma(\mathbb{P}^1, \mathcal{O}(-1))=0$$인 것을 동일한 논리로 보일 수 있으며, $$d=0$$인 경우, 즉 $$\mathcal{O}_{\mathbb{P}^n}(0)=\mathcal{O}_{\mathbb{P}^n}$$의 경우에는 section들이 homogeneous polynomial of degree $$0$$, 즉 상수함수들이라는 것을 확인할 수 있으므로 [§준사영다양체, ⁋예시 6](/ko/math/algebraic_geometry/quasi_projective_varieties#ex6)의 계산이 다시 확인된다. 

주의를 기울일 부분은 $$d>0$$인 경우이다. 이 경우 section들은 [예시 16](#ex16)과 정확히 동일한 계산에 의해 homogeneous polynomial of degree $$d$$들임을 확인할 수 있다. 특히 $$\Gamma(\mathbb{P}^n, \mathcal{O}(d))\neq 0$$이며, 이는 [예시 12](#ex12) 이후의 직관이 다소 과하게 단순화되었다는 것을 보여주는 계산이라 생각할 수 있다. 

이 현상에 대한 더 정확한 설명은 다음과 같다. 편의상 $$\mathbb{P}^1$$에서의 예시를 보자. $$\mathcal{O}(-1)$$의 section들은 homogeneous of degree $$-1$$이므로, 특히 다음의 꼴

$$s([x_0:x_1])=\frac{a}{x_0}+\frac{b}{x_1}$$

이고 이 함수가 $$\mathbb{P}^1$$ 전체에서 정의되기 위해서는 반드시 $$a=b=0$$이어야 한다. 반면, $$\mathcal{O}(1)$$의 section들은 homogeneous polynomial of degree $$1$$이므로, 다음의 꼴

$$s([x_0:x_1])=ax_0+bx_1$$

의 함수들이며 위와는 달리 $$a,b$$에 어떠한 제약도 없다. 직관적으로, $$\mathcal{O}(-1)$$의 section들은 분모로 인해 zero section을 넘을 수 없고, 따라서 모든 section이 "$$1$$이 $$-1$$에 붙는", 꼬임이 만들어내는 문제를 피해갈 수 없다. 이 꼬임은 $$\mathcal{O}(1)$$에서도 같은 문제를 만든다. 즉 "constant section" $$s([x_0:x_1])$$은 $$\mathcal{O}(1)$$에서도 마찬가지로 section이 아니다. 그러나 이번에는 $$\mathcal{O}(1)$$의 section들이 zero section을 넘어갈 수 있기 때문에 $$\Gamma(\mathbb{P}^1, \mathcal{O}(1))\neq 0$$이게 된다. 

## Divisor -- Line Bundle correspondence

이제 우리는 divisor와 line bundle 사이의 본질적인 연결을 확립한다. 우선 우리는 Cartier divisor로부터 line bundle을 만들 수 있다는 것을 보인다. 

<div class="definition" markdown="1">

<ins id="def17">**정의 17**</ins> Cartier divisor $$D = \{(U_i, f_i)\}$$에 대하여, line bundle $$\mathcal{O}_X(D)$$를 transition function들 $$g_{ij} = f_i/f_j$$로 정의한다.

</div>

즉, $$U_i$$들 위에서는 trivial bundle로 잡고, 이를 각각의 overlap에서 Cartier divisor가 담고 있는 정확히 그 정보를 이용하여 이어주는 것이다. 만일 $$\mathcal{O}_X(D)$$를 sheaf로 본다면, 즉 위에서 정의한 line bundle의 sheaf of sections를 생각한다면 각각의 열린집합 $$U$$ 위에서 $$\mathcal{O}_X(D)(U)$$는 (sheaf로서) 다음 식

$$\divisor(f)+D\geq 0$$

을 만족하는 함수들의 sheaf이다. 즉 $$\mathcal{O}_X(D)$$는, 만일 $$D$$를 codimension $$1$$ subvariety of $$X$$로 본다면, $$D$$를 따라 최대 order $$1$$의 pole을 가질 수 있는 rational function들의 sheaf이다. 거꾸로 $$\mathcal{O}_X(-D)$$는 다음의 식

$$\divisor(f)-D\geq 0$$

으로 주어지며, 이는 정확히 $$D$$ 위에서 vanish하는 함수들의 sheaf이다. 즉

$$\mathcal{O}_X(-D)(U)=\{f\in \mathcal{O}_X(U)\mid \text{$f$ vanishes on $D\cap U$}\}$$

이며, 이로부터 다음의 short exact sequence

$$0\rightarrow \mathcal{O}_X(-D)\rightarrow \mathcal{O}_X\rightarrow \mathcal{O}_D\rightarrow 0$$

을 얻는다. 그럼 $$\mathcal{O}_X(-D)$$는 $$D$$를 정의하는 ideal들의 sheaf이며 이러한 이유로 이를 $$\mathcal{I}_D$$로 적고 *ideal sheaf*라 부른다.

<div class="proposition" markdown="1">

<ins id="prop18">**명제 18**</ins> 위의 정의는 well-defined이다. 즉, 서로 동치인 Cartier divisor들은 isomorphic한 line bundle을 정의한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

두 Cartier divisor $$\{(U_i, f_i)\}$$와 $$\{(V_j, g_j)\}$$가 동치이면, $$f_i/g_j \in \mathcal{O}_X(U_i \cap V_j)^\ast$$이다. 이들로부터 정의되는 line bundle들의 transition functions은 서로 compatible하므로 isomorphic한 line bundle을 정의한다.

</details>

예를 들어, 임의의 principal divisor $$\divisor(f)$$에 대하여 transition function은 $$1$$이므로 trivial bundle이 된다. 이제 line bundle과 Cartier divisor 사이의 관계를 정리한다.

<div class="proposition" markdown="1">

<ins id="prop19">**명제 19**</ins> 임의의 variety $$X$$에 대하여 $$\Pic(X) \cong \CaCl(X)$$이다. 

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

우선 $$D \mapsto \mathcal{O}_X(D)$$가 $$\CaDiv(X)$$에서 $$\Pic(X)$$로의 group homomorphism임을 확인한다. Cartier divisor $$D = \{(U_i, f_i)\}$$에 대해 $$\mathcal{O}_X(D)$$의 transition function은 $$g_{ij} = f_i/f_j \in \mathcal{O}_X(U_i \cap U_j)^\times$$이므로 line bundle을 정의한다. Principal divisor $$\divisor(h)$$는 transition function이 $$1$$이므로 trivial bundle에 대응되고, 따라서 $$\CaCl(X) = \CaDiv(X)/\Prin(X)$$에서 $$\Pic(X)$$로의 well-defined group homomorphism을 유도한다.

이것이 isomorphism임을 보이기 위해, 임의의 line bundle $$\mathcal{L}$$이 주어졌다고 하자. Trivializing open $$U \subseteq X$$에서 $$\mathcal{L}\vert_U \cong \mathcal{O}_U$$이므로, $$\mathcal{O}_U$$의 constant section $$1$$에 대응되는 $$s \in \mathcal{L}(U)$$를 잡을 수 있으며, 이 $$s$$는 nonzero rational section이다. 이제 $$\mathcal{L}$$의 trivializing cover $$\{U_i\}$$를 생각하자. 각 $$U_i$$에서 trivialization $$\psi_i\colon \mathcal{L}\vert_{U_i} \cong \mathcal{O}_{U_i}$$를 잡고, $$f_i := \psi_i(s\vert_{U_i \cap U}) \in \mathcal{O}_X(U_i \cap U) \subseteq \mathbb{K}(X)$$를 정의한다. 그러면 $$U_i \cap U_j \cap U$$ 위에서 $$f_i = g_{ij} f_j$$이고, $$X$$가 irreducible이므로 $$U_i \cap U_j \cap U$$는 $$U_i \cap U_j$$의 dense open subset이므로 이 관계는 $$U_i \cap U_j$$ 전체에서 성립한다. 즉 $$f_i/f_j = g_{ij} \in \mathcal{O}_X(U_i \cap U_j)^\times$$이므로 $$D = \{(U_i, f_i)\}$$는 Cartier divisor이고, $$\mathcal{O}_X(D)$$의 transition function이 $$\{g_{ij}\}$$이므로 $$\mathcal{O}_X(D) \cong \mathcal{L}$$이다.

마지막으로 injectivity를 보인다. $$\mathcal{O}_X(D) \cong \mathcal{O}_X(D')$$이면 두 line bundle의 transition function이 같으므로 $$f_i/f_i' = f_j/f_j'$$ on $$U_i \cap U_j$$ (모든 $$i, j$$). 다시 $$U_i \cap U_j$$의 dense open subset에서 이 관계가 성립하므로 $$f_i/f_i'$$는 모든 $$i$$에 대해 동일한 rational function $$h \in \mathbb{K}(X)^\times$$이고, $$D - D' = \divisor(h)$$이므로 linearly equivalent하다.

</details>

만일 $$X$$가 smooth라면, $$\CaCl(X)\cong \Cl(X)$$임을 이미 알고 있다. 이들의 관계는 다음 commutative diagram에 담겨있다. 

img

## Pullback of Line Bundles

Morphism $$\varphi: X \to Y$$가 주어졌을 때, $$Y$$ 위의 line bundle을 $$X$$ 위로 "당기는" 연산은 자연스럽게 정의된다. 예를 들어, $$Y$$ 위의 hypersurface를 $$\varphi$$에 의해 $$X$$ 위로 당기면, 이에 대응하는 line bundle도 함께 당겨져야 한다. 이 pullback 연산은 Picard group 사이의 group homomorphism을 유도하며, embedding의 경우 ambient space의 line bundle을 부분다양체로 제한하는 것으로 이해할 수 있다.

<div class="proposition" markdown="1">

<ins id="prop20">**명제 20**</ins> Morphism $$\varphi: X \to Y$$와 $$Y$$ 위의 line bundle $$\mathcal{L}$$에 대하여, *pullback* $$\varphi^\ast \mathcal{L}$$은 $$X$$ 위의 line bundle이다. 그 transition functions은 $$\{g_{ij} \circ \varphi\}$$이다. 여기서 $$\{g_{ij}\}$$는 $$\mathcal{L}$$의 transition functions이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Line bundle $$\mathcal{L}$$이 open cover $$\{U_i\}$$ 위에서 transition functions $$\{g_{ij}\}$$로 주어졌다고 하자. Pullback $$\varphi^\ast \mathcal{L}$$은 open cover $$\{\varphi^{-1}(U_i)\}$$ 위에서 transition functions $$\{g_{ij} \circ \varphi\}$$로 정의된다. $$\varphi^\ast \mathcal{L}$$이 $$X$$ 위의 line bundle임을 확인하려면, transition function들이 cocycle 조건을 만족하면 된다.

Cocycle 조건 세 가지를 모두 확인한다.

1. $$g_{ii} \circ \varphi = 1 \circ \varphi = 1$$ since $$g_{ii} = 1$$.
2. $$(g_{ij} \circ \varphi)(g_{ji} \circ \varphi) = (g_{ij} g_{ji}) \circ \varphi = 1 \circ \varphi = 1$$ since $$g_{ij} g_{ji} = 1$$.
3. $$(g_{ij} \circ \varphi)(g_{jk} \circ \varphi) = (g_{ij} g_{jk}) \circ \varphi = g_{ik} \circ \varphi$$ since $$g_{ij} g_{jk} = g_{ik}$$.

따라서 $$\{g_{ij} \circ \varphi\}$$는 cocycle condition을 만족한다.

</details>

<div class="proposition" markdown="1">

<ins id="prop21">**명제 21**</ins> Pullback은 group homomorphism $$\varphi^\ast: \operatorname{Pic}(Y) \to \operatorname{Pic}(X)$$를 유도한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$\varphi^\ast(\mathcal{L} \otimes \mathcal{M}) \cong \varphi^\ast \mathcal{L} \otimes \varphi^\ast \mathcal{M}$$이고 $$\varphi^\ast \mathcal{O}_Y \cong \mathcal{O}_X$$이므로, pullback은 group homomorphism이다.

이를 확인하기 위해 transition function 관점에서 살펴보자. $$\mathcal{L} \otimes \mathcal{M}$$의 transition function은 $$g_{ij}^{\mathcal{L}} g_{ij}^{\mathcal{M}}$$이므로, $$\varphi^\ast(\mathcal{L} \otimes \mathcal{M})$$의 transition function은 $$(g_{ij}^{\mathcal{L}} g_{ij}^{\mathcal{M}}) \circ \varphi = (g_{ij}^{\mathcal{L}} \circ \varphi)(g_{ij}^{\mathcal{M}} \circ \varphi)$$이다. 이는 각각 $$\varphi^\ast\mathcal{L}$과 $\varphi^\ast\mathcal{M}$$의 transition function이므로, $$\varphi^\ast(\mathcal{L} \otimes \mathcal{M}) \cong \varphi^\ast\mathcal{L} \otimes \varphi^\ast\mathcal{M}$$을 얻는다. 또한 $$\mathcal{O}_Y$$의 transition function은 모두 $$1$$이므로 $$\varphi^\ast\mathcal{O}_Y$$의 transition function도 $$1$$, 즉 $$\varphi^\ast\mathcal{O}_Y \cong \mathcal{O}_X$$이다.

</details>

<div class="example" markdown="1">

<ins id="ex22">**예시 22**</ins> Embedding $$i: C \hookrightarrow \mathbb{P}^n$$에 대해, $$i^\ast \mathcal{O}_{\mathbb{P}^n}(1)$$은 curve $$C$$ 위의 line bundle이다. 이를 $$C$$ 위의 *hyperplane bundle*이라 부르며, $$\mathcal{O}_C(1)$$로 표기한다. 일반적으로 $$\mathcal{O}_C(1)$$은 nontrivial인데, 예를 들어 $$C = \mathbb{P}^1 \subset \mathbb{P}^n$$일 때 $$\mathcal{O}_C(1) = \mathcal{O}_{\mathbb{P}^1}(1)$$은 [예시 12](#ex12)에서 본 바와 같이 nontrivial line bundle이다. "Hyperplane bundle"이라는 이름은, $$\mathbb{P}^n$$의 hypersurface 중 degree $$1$$인 것, 즉 hyperplane $$H$$에 대응하는 line bundle $$\mathcal{O}_{\mathbb{P}^n}(1)$$을 $$C$$ 위로 당겼을 때 얻어지는 bundle이라는 의미에서 붙여졌다.

</div>

## Vector Bundle

지금까지 우리는 1차원 벡터공간을 fiber로 갖는 line bundle을 살펴보았다. 이 개념을 일반화하여 각 fiber가 고차원 벡터공간인 *vector bundle*을 정의할 수 있다. Vector bundle은 다양체의 접공간, 법공간 등 기하학적으로 자연스럽게 등장하는 구조를 포착하며, 미분기하학에서의 접다발, 벡터장 등의 개념의 대수기하학적 아날로그이다. Line bundle은 rank 1 vector bundle의 특수한 경우이며, vector bundle 이론의 관점에서 line bundle의 성질들을 더욱 명확하게 이해할 수 있다.

<div class="definition" markdown="1">

<ins id="def23">**정의 23**</ins> 다양체 $$X$$ 위의 *rank r vector bundle* $$\mathcal{E}$$는 다음과 같은 데이터로 구성된다.

1. Projection $$\pi: \mathcal{E} \to X$$.
2. $$X$$의 open cover $$\{U_i\}$$와 각 $$i$$에 대한 *local trivialization* $$\phi_i: \pi^{-1}(U_i) \overset{\sim}{\longrightarrow} U_i \times \mathbb{A}^r$$. 이들이 정의하는

    $$\phi_j \circ \phi_i^{-1}: (U_i \cap U_j) \times \mathbb{A}^r \to (U_i \cap U_j) \times \mathbb{A}^r$$

    는 적당한 *transition function* $$g_{ij} \in \operatorname{GL}_r(\mathcal{O}_X(U_i \cap U_j))$$에 대하여 $$(p, v) \mapsto (p, g_{ij}(p)v)$$의 꼴이다.

</div>

Line bundle의 정의와 비교하면, 유일한 차이는 fiber가 $$\mathbb{A}^1$$ 대신 $$\mathbb{A}^r$$이고, transition function이 $$\mathcal{O}_X(U_i \cap U_j)^\ast = \operatorname{GL}_1(\mathcal{O}_X(U_i \cap U_j))$$ 대신 $$\operatorname{GL}_r(\mathcal{O}_X(U_i \cap U_j))$$ 값을 갖는다는 점이다. 따라서 line bundle은 정확히 rank 1 vector bundle이다.

[명제 2](#prop2)와 같은 cocycle condition이 성립한다. 다만 transition function이 행렬값을 가지므로 곱셈의 순서에 주의해야 한다.

<div class="example" markdown="1">

<ins id="ex24">**예시 24**</ins> 가장 단순한 예시는 line bundle $$\mathcal{O}_X$$로부터 오는 rank $$r$$ *trivial vector bundle* $$\mathcal{O}_X^{\oplus r}$$이다. 이는 line bundle $$\mathcal{O}_X$$를 $$r$$번 direct sum하여 얻어지는 것이다. 

기하학적으로 중요한 대상들은 tangent bundle과 cotangent bundle이다. *Tangent bundle* $$\mathcal{T}_X$$는 각 점 $$p \in X$$에 tangent space $$T_p X$$를 fiber로 갖는 vector bundle로, 만약 $$X$$가 $$n$$차원 smooth variety이면 rank $$n$$ vector bundle이고, local coordinate $$\x_1, \ldots, \x_n$$에서 $$\partial/\partial \x_1, \ldots, \partial/\partial \x_n$$이 local frame을 이룬다. *Cotangent bundle* $$\Omega_X^1 = \mathcal{T}_X^\vee$$는 tangent bundle의 dual이며, local coordinate에서 $$d\x_1, \ldots, d\x_n$$이 local frame을 이룬다.

직관적으로 $$\Omega_X^1$$은 $$X$$ 위에 정의된 differential $$1$$-form들의 bundle이므로, 이들을 $$r$$번 텐서하여 $$r$$-form들의 bundle을 얻을 수 있다. 이들 중 제일 흥미로운 것은 top exterior power $$\omega_X = \bigwedge^n \Omega_X^1$$으로, 이는 rank $$1$$ vector bundle, 즉 line bundle이며 미분기하학에서였다면 volume form들의 bundle이라 생각할 수 있었을 것이다. 우리는 이를 *canonical line bundle*이라 부른다. 

</div>

위와 같이 vector bundle에 대해서도 line bundle과 유사한 연산을 정의할 수 있다. 두 vector bundle $$\mathcal{E}, \mathcal{F}$$의 tensor product $$\mathcal{E} \otimes \mathcal{F}$$는 fiberwise tensor product로 정의되며, 그 transition functions은 $$g_{ij}^{\mathcal{E}} \otimes g_{ij}^{\mathcal{F}}$$이다. Dual bundle $$\mathcal{E}^\vee$$의 transition functions은 $$\left(g_{ij}^{\mathcal{E}}\right)^{-t}$$ (inverse transpose)이다. 또한 direct sum $$\mathcal{E} \oplus \mathcal{F}$$는 fiberwise direct sum으로 정의되며, 이때 transition functions은 block diagonal matrix $$\begin{pmatrix} g_{ij}^{\mathcal{E}} & 0 \\ 0 & g_{ij}^{\mathcal{F}} \end{pmatrix}$$이 된다.

## Tautological Bundle on Grassmannian

위에서 정의한 $$\mathbb{P}^n$$ 위의 tautological bundle $$\mathcal{O}_{\mathbb{P}^n}(-1)$$은 Grassmannian으로 자연스럽게 일반화된다. Grassmannian $$\Gr(k, n)$$은 $$n$$차원 벡터공간의 $$k$$차원 부분공간들의 공간이며, 이 일반화에서 tautological bundle은 rank $$k$$ vector bundle이 되며, 이와 쌍대를 이루는 *quotient bundle*도 자연스럽게 정의된다.

<div class="definition" markdown="1">

<ins id="def25">**정의 25**</ins> Grassmannian $$\Gr(k, n)$$ 위에 다음 두 vector bundle을 정의한다.

1. *Tautological bundle* $$S$$: 각 점 $$[V] \in \Gr(k, n)$$ (여기서 $$V \subseteq \mathbb{A}^n$$는 $$k$$차원 부분공간)에 그 부분공간 $$V$$ 자체를 fiber로 대응시키는 rank $$k$$ vector bundle.
   $$S = \{([V], v) \in \Gr(k, n) \times \mathbb{A}^n \mid v \in V\}$$

2. *Quotient bundle* $$Q$$: 각 점 $$[V]$$에 몫공간 $$\mathbb{A}^n / V$$를 fiber로 대응시키는 rank $$n-k$$ vector bundle.
   $$Q = \{([V], [w]) \in \Gr(k, n) \times (\mathbb{A}^n / S) \mid [w] \in \mathbb{A}^n / V\}$$

</div>

이들 사이에는 자연스러운 short exact sequence가 존재한다.

$$0 \to S \to \mathcal{O}_{\Gr(k,n)}^{\oplus n} \to Q \to 0$$

여기서 가운데 항은 $$\Gr(k, n) \times \mathbb{A}^n$$으로, trivial bundle of rank $$n$$이다. 첫 번째 사상은 각 점 $$([V], v) \in S$$를 $$([V], v) \in \mathcal{O}^{\oplus n}$$으로 포함시키는 것이고, 두 번째 사상은 $$([V], w) \in \mathcal{O}^{\oplus n}$$을 $$([V], [w]) \in Q$$로 보내는 quotient map이다.

<div class="proposition" markdown="1">

<ins id="prop26">**명제 26**</ins> $$\Gr(1, n+1) = \mathbb{P}^n$$에서 tautological bundle $$S$$는 $$\mathcal{O}_{\mathbb{P}^n}(-1)$$과 isomorphic하다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$\Gr(1, n+1)$$의 각 점은 $$\mathbb{A}^{n+1}$$의 1차원 부분공간, 즉 원점을 지나는 직선이다. 이는 정확히 $$\mathbb{P}^n$$의 점에 해당한다. Tautological bundle $$S$$의 각 fiber는 이 직선 그 자체이므로, 이는 [정의 13](#def13)에서 정의한 $$\mathcal{O}_{\mathbb{P}^n}(-1)$$과 동일하다.

</details>

이 명제는 Grassmannian의 tautological bundle이 사영공간에서는 익숙한 $$\mathcal{O}(-1)$$으로 귀결됨을 보여준다. Quotient bundle $$Q$$의 경우, $$\Gr(1, n+1) = \mathbb{P}^n$$에서 rank $$n$$이며, 이는 tangent bundle $$\mathcal{T}_{\mathbb{P}^n}$$과 밀접한 관계가 있다. 실제로 $$\mathcal{T}_{\mathbb{P}^n} \cong \Hom(S, Q) \cong S^\vee \otimes Q$$가 성립한다.

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.