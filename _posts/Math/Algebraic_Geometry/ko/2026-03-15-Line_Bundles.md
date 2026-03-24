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

우리는 앞선 글에서 다양체 $X$ 위의 divisor들을 정의하고, 이들의 linear equivalence class들이 $\operatorname{Cl}(X)$를 이룸을 보았다. 그러나 모든 divisor가 어떤 유리함수의 zero/pole으로부터 오는 것은 아니다. 예를 들어 [§인자, ⁋예시 11]에서 $\operatorname{Cl}(\mathbb{P}^n) \cong \mathbb{Z}$이므로 ([§인자, ⁋예시 11](/ko/math/algebraic_geometry/divisors#ex11)), $$\mathbb{P}^n$$에서 일반적인 divisor $dH$는 $d \ge 0$일 때만 어떤 함수의 zero set으로 나온다.

이러한 제약을 극복하기 위해 우리는 *line bundle*을 도입한다. Line bundle $\mathcal{L}$은 각 점 $p \in X$에 1차원 벡터공간을 대응시키는 기하학적 대상이며, $\mathcal{L}$의 section $s$는 자연스럽게 divisor $\operatorname{div}(s)$를 정의한다. 이 관점에서는 임의의 divisor $D$에 대해 $\mathcal{O}_X(D)$라는 line bundle을 만들 수 있고, 그 section들이 $D$보다 크거나 같은 divisor들에 대응된다. 즉, line bundle은 divisor를 "함수의 zero/pole"이라는 제약에서 벗어나 독립적으로 다룰 수 있게 해 준다.

## Line Bundle의 정의

Line bundle, 더 나아가 이 글의 뒷부분에서 정의할 vector bundle은 미분기하에서와 마찬가지 방식으로 정의된다. ([\[미분다양체\] §접다발과 여접다발, ⁋정의 1](/ko/math/manifold/tangent_and_cotangent_bundles#def1))

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Variety $$X$$ 위의 *line bundle* $$\mathcal{L}$$은 다음과 같은 데이터로 구성된다.

1. Projection $$\pi: \mathcal{L} \to X$$.
2. $$X$$의 open cover $$\{U_i\}$$와 각 $$i$$에 대한 *local trivialization* $$\phi_i: \pi^{-1}(U_i) \overset{\sim}{\longrightarrow} U_i \times \mathbb{A}^1$$. 이들이 정의하는
    
    $$\phi_j \circ \phi_i^{-1}: (U_i \cap U_j) \times \mathbb{A}^1 \to (U_i \cap U_j) \times \mathbb{A}^1$$

    는 적당한 *transition function* $$g_{ij} \in \mathcal{O}_X(U_i \cap U_j)^\ast$$에 대하여 $$(p, t) \mapsto (p, g_{ij}(p)t)$$의 꼴이다.

</div>

그럼 다음 명제는 거의 자명하다. 

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2 (Cocycle condition)**</ins> Transition functions $$\{g_{ij}\}$$는 다음의 *cocycle condition*을 만족한다.

1. $$g_{ii} = 1$$ for all $$i$$.
2. $$g_{ij} = g_{ji}^{-1}$$ for all $$i, j$$.
3. $$g_{ij} g_{jk} = g_{ik}$$ on $$U_i \cap U_j \cap U_k$$ for all $$i, j, k$$.

</div>

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> *Trivial line bundle* $$\mathcal{O}_X = X \times \mathbb{A}^1$$은 모든 transition function이 $$g_{ij} = 1$$인 line bundle이다. 이는 "twist가 없는" 가장 간단한 line bundle이다.

</div>

[명제 2](#prop2)는 흔한 gluing condition으로, 이 조건에 의해 line bundle은 일종의 sheaf로 생각할 수 있다. ([\[위상수학\] §층, ⁋정의 1](/ko/math/topology/sheaves#def1)) 구체적으로, 우리는 line bundle $$\mathcal{L}$$이 주어졌을 때, 이 line bundle의 section sheaf

Line bundle은 sheaf 이론의 언어로 *invertible sheaf*로 표현할 수 있다. 이 관점은 line bundle의 section들을 다루는 데 더 자연스럽다.

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> Sheaf $$\mathcal{F}$$가 *invertible*이라는 것은 각 점 $$p \in X$$의 근방 $$U$$에서 $$\mathcal{F}\vert_U \cong \mathcal{O}_U$$인 것이다. 즉, $$\mathcal{F}$$가 국소적으로 구조층과 동형인 sheaf이다.

</div>

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> Line bundle $$\mathcal{L}$$의 section sheaf $$\mathcal{O}_X(\mathcal{L})$$은 invertible sheaf이다. 역으로, 모든 invertible sheaf는 유일한 line bundle로부터 온다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Line bundle $$\mathcal{L}$$의 section sheaf는 각 open set $$U$$에 대해

$$\mathcal{O}_X(\mathcal{L})(U) = \{s: U \to \mathcal{L} \mid \pi \circ s = \operatorname{id}_U\}$$

으로 정의된다. Local trivialization $$\phi_i: \pi^{-1}(U_i) \to U_i \times \mathbb{A}^1$$에 의해 $$\mathcal{O}_X(\mathcal{L})|_{U_i} \cong \mathcal{O}_{U_i}$$이다. 따라서 $$\mathcal{O}_X(\mathcal{L})$$은 invertible sheaf이다.

역으로, invertible sheaf $$\mathcal{F}$$가 주어지면, local isomorphism $$\mathcal{F}|_{U_i} \cong \mathcal{O}_{U_i}$$들로부터 transition functions을 정의할 수 있고, 이로부터 line bundle을 재구성할 수 있다.

</details>

이 명제에 의해 우리는 line bundle과 invertible sheaf를 동의어로 사용할 수 있다. 관습적으로 $$\mathcal{L}$$로 표기할 때는 line bundle을, $$\mathcal{O}_X(\mathcal{L})$$로 표기할 때는 sheaf를 강조한다.

## Tensor Product와 Dual

Vector bundle의 세계에서는 fiberwise 선형대수 연산을 통해 새로운 bundle을 구성하는 것이 자연스럽다. 각 점 $$p$$에서의 fiber $$\mathcal{L}_p$$가 1차원 벡터공간이므로, 두 1차원 벡터공간의 tensor product이나 dual 공간을 취하는 것은 여전히 1차원 벡터공간을 준다. 이러한 fiberwise 연산이 전역적으로 모여 새로운 line bundle을 이루며, 이는 벡터 공간에서의 tensor product과 쌍대공간의 유추이다. 이러한 연산들은 Picard group의 구조를 이해하는 데 필수적이다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> 두 line bundle $$\mathcal{L}, \mathcal{M}$$의 tensor product $$\mathcal{L} \otimes \mathcal{M}$$도 line bundle이다. 그 transition functions은 $$\{g_{ij} h_{ij}\}$$이다. 여기서 $$\{g_{ij}\}, \{h_{ij}\}$$는 각각 $$\mathcal{L}, \mathcal{M}$$의 transition functions이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Tensor product의 fiber는 $$\mathcal{L}_p \otimes_{\mathbb{K}} \mathcal{M}_p$$이고, 이는 두 1차원 벡터공간의 tensor product이므로 다시 1차원이다. Transition function은 $$\phi_j \circ \phi_i^{-1}$$과 $$\psi_j \circ \psi_i^{-1}$$의 곱이 되므로 $$g_{ij} h_{ij}$$이다.

</details>

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> Line bundle $$\mathcal{L}$$의 *dual bundle* $$\mathcal{L}^\vee = \mathcal{H}om_{\mathcal{O}_X}(\mathcal{L}, \mathcal{O}_X)$$도 line bundle이다. 그 transition functions은 $$\{g_{ij}^{-1}\}$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Dual bundle의 fiber는 $$\mathcal{L}_p^\vee = \operatorname{Hom}_{\mathbb{K}}(\mathcal{L}_p, \mathbb{K})$$이고, 이는 1차원 벡터공간의 dual이므로 다시 1차원이다. Transition function은 $$g_{ij}$$의 inverse이다.

</details>

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> 임의의 line bundle $$\mathcal{L}$$에 대해 $$\mathcal{L} \otimes \mathcal{L}^\vee \cong \mathcal{O}_X$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$\mathcal{L} \otimes \mathcal{L}^\vee$$의 transition functions은 $$g_{ij} \cdot g_{ij}^{-1} = 1$$이므로 trivial bundle이다.

</details>

## Picard Group

지금까지 우리는 개별 line bundle의 구조를 살펴보았다. 이제 한 걸음 더 나아가, 다양체 $$X$$ 위의 모든 line bundle들을 체계적으로 분류하는 group을 구성해보자. 이 분류가 중요한 이유는 line bundle들이 다양체의 기하학적 성질을 포착하는 불변량이기 때문이다. 예를 들어, $$\operatorname{Pic}(\mathbb{P}^n) \cong \mathbb{Z}$$라는 사실은 $$\mathbb{P}^n$$의 기하학이 단일 정수로 매개화됨을 의미하며, 이는 사영공간의 매우 특별한 구조를 반영한다. 더 일반적으로 Picard group의 rank, torsion, torsion-free part 등은 다양체의 복잡성을 측정하는 중요한 지표이다.

<div class="definition" markdown="1">

<ins id="def9">**정의 9**</ins> 다양체 $$X$$의 *Picard group* $$\operatorname{Pic}(X)$$는 $$X$$ 위의 line bundle들의 isomorphism class들의 집합에 tensor product를 연산으로 하여 얻어진 group이다. 항등원은 trivial bundle $$\mathcal{O}_X$$이고, $$\mathcal{L}$$의 inverse는 $$\mathcal{L}^\vee$$이다.

</div>

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10**</ins> $$\operatorname{Pic}(X)$$는 abelian group이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Tensor product는 commutative이고 associative이다. [명제 8](#prop8)에 의해 $$\mathcal{L} \otimes \mathcal{L}^\vee \cong \mathcal{O}_X$$이므로 inverse가 존재한다.

</details>

<div class="example" markdown="1">

<ins id="ex11">**예시 11**</ins> **$$\mathbb{A}^n$$의 Picard group**: $$\operatorname{Pic}(\mathbb{A}^n) = 0$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$\mathbb{A}^n = \mathbb{V}(\emptyset) \subseteq \mathbb{A}^n$$의 coordinate ring $$\mathbb{K}[\x_1, \ldots, \x_n]$$는 unique factorization domain이다. 이 경우 모든 line bundle은 trivial이다. 이는 ([§Divisors, ⁋예시 9](/ko/math/algebraic_geometry/divisors#ex9))에서 $$\operatorname{Cl}(\mathbb{A}^n) = 0$$임과 일치한다.

</details>

<div class="example" markdown="1">

<ins id="ex12">**예시 12**</ins> **$$\mathbb{P}^n$$의 Picard group**: $$\operatorname{Pic}(\mathbb{P}^n) \cong \mathbb{Z}$$이다. 생성원은 *hyperplane bundle* $$\mathcal{O}_{\mathbb{P}^n}(1)$$이다.

</div>

$$\mathcal{O}_{\mathbb{P}^n}(1)$$은 다음과 같이 정의된다. $$\mathbb{P}^n$$의 standard open cover $$U_i = \{[x_0 : \cdots : x_n] \mid x_i \ne 0\}$$에서, transition functions은 $$g_{ij} = x_i/x_j$$이다. 일반적으로 $$\mathcal{O}_{\mathbb{P}^n}(d)$$는 $$g_{ij} = (x_i/x_j)^d$$를 transition functions으로 갖는 line bundle이며, $$\operatorname{div}(x_0^d) = dH$$에 대응된다. 여기서 $$H = \mathbb{V}(x_0)$$는 hyperplane divisor이다.

## Divisor와 Line Bundle의 관계

이제 우리는 divisor와 line bundle 사이의 본질적인 연결을 확립한다.

<div class="definition" markdown="1">

<ins id="def13">**정의 13**</ins> Cartier divisor $$D = \{(U_i, f_i)\}$$에 대하여, line bundle $$\mathcal{O}_X(D)$$를 transition functions $$g_{ij} = f_i/f_j$$로 정의한다.

</div>

<div class="proposition" markdown="1">

<ins id="prop14">**명제 14**</ins> 위의 정의는 well-defined이다. 즉, 서로 동치인 Cartier divisor들은 isomorphic한 line bundle을 정의한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

두 Cartier divisor $$\{(U_i, f_i)\}$$와 $$\{(V_j, g_j)\}$$가 동치이면, $$f_i/g_j \in \mathcal{O}_X(U_i \cap V_j)^\ast$$이다. 이들로부터 정의되는 line bundle들의 transition functions은 서로 compatible하므로 isomorphic한 line bundle을 정의한다.

</details>

<div class="proposition" markdown="1">

<ins id="prop15">**명제 15**</ins> Principal divisor $$\operatorname{div}(f)$$에 대하여 $$\mathcal{O}_X(\operatorname{div}(f)) \cong \mathcal{O}_X$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Principal divisor $$\operatorname{div}(f) = \{(X, f)\}$$의 transition function은 $$g_{ij} = f/f = 1$$이므로 trivial bundle이다.

</details>

<div class="proposition" markdown="1">

<ins id="prop16">**명제 16**</ins> Smooth variety $$X$$에 대하여 $$\operatorname{Pic}(X) \cong \operatorname{Cl}(X)$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Cartier divisor $$D \mapsto \mathcal{O}_X(D)$$는 $$\operatorname{CaDiv}(X)$$에서 $$\operatorname{Pic}(X)$$로의 group homomorphism이다. [명제 15](#prop15)에 의해 principal divisor들은 trivial bundle에 대응되므로, 이는 $$\operatorname{Cl}(X) = \operatorname{CaDiv}(X)/\operatorname{Prin}(X)$$에서 $$\operatorname{Pic}(X)$$로의 isomorphism을 유도한다.

역으로, line bundle $$\mathcal{L}$$이 주어지면, $$\mathcal{L}$$의 *rational section*$$^1$$ $$s$$를 선택하여 divisor $$\operatorname{div}(s)$$를 정의할 수 있다. 이 방향의 핵심 아이디어는 다음과 같다. $$\mathcal{L}$$은 국소적으로 $$\mathcal{O}_X$$와 동형이므로, Zariski open dense 부분집합 $$U \subseteq X$$에서 $$\mathcal{L}|_U \cong \mathcal{O}_U$$이다. 이 동형 하에서 $$\mathcal{O}_U$$의 상수 section $$1$$의 원상을 $$s$$라 하면, $$s$$는 $$U$$ 위에서 nowhere vanishing이며 $$X$$의 나머지 부분에서 극점과 영점을 가질 수 있다. $$s$$의 zero/pole locus로부터 Weil divisor $$\operatorname{div}(s) = \sum_P v_P(s) P$$를 정의할 수 있으며, 여기서 $$v_P(s)$$는 *order of vanishing*$$^2$$, 즉 section $$s$$가 점 $$P$$에서 0이 되는 차수이다. 다른 rational section $$s' = fs$$ ($$f \in \mathbb{K}(X)^\ast$$)를 선택하면 $$\operatorname{div}(s') = \operatorname{div}(f) + \operatorname{div}(s)$$이므로, linear equivalence class $$[\operatorname{div}(s)]$$는 선택에 무관하게 well-defined이다. 이 well-definedness가 이 방향의 증명에서 핵심이다. 따라서 $$\mathcal{L} \mapsto [\operatorname{div}(s)]$$는 $$\operatorname{Pic}(X)$$에서 $$\operatorname{Cl}(X)$$로의 inverse map을 정의한다.

</details>

---

$$^1$$ *Rational section*은 line bundle의 일반적인 위치(generic point)에서의 section이다. 정칙 section과 달리, 유한 개의 점에서 극점을 가질 수 있다.

$$^2$$ *Order of vanishing* $$v_P(s)$$는 section $$s$$의 국소 표현에서 uniformizer의 거듭제곱 지수이다. 즉, $$s$$가 점 $$P$$ 근방에서 $$t^{v_P(s)}$$ (여기서 $$t$$는 $$P$$에서의 uniformizer)의 꼴로 나타나면, $$v_P(s)$$는 $$s$$가 $$P$$에서 0이 되는 차수를 나타낸다.

## Vector Bundle

지금까지 우리는 1차원 벡터공간을 fiber로 갖는 line bundle을 살펴보았다. 이 개념을 일반화하여 각 fiber가 고차원 벡터공간인 *vector bundle*을 정의할 수 있다. Vector bundle은 다양체의 접공간, 법공간 등 기하학적으로 자연스럽게 등장하는 구조를 포착하며, 미분기하학에서의 접다발, 벡터장 등의 개념의 대수기하학적 아날로그이다. Line bundle은 rank 1 vector bundle의 특수한 경우이며, vector bundle 이론의 관점에서 line bundle의 성질들을 더욱 명확하게 이해할 수 있다.

<div class="definition" markdown="1">

<ins id="def17">**정의 17**</ins> 다양체 $$X$$ 위의 *rank r vector bundle* $$\mathcal{E}$$는 다음과 같은 데이터로 구성된다.

1. 전사 사상 $$\pi: \mathcal{E} \to X$$.
2. $$X$$의 open cover $$\{U_i\}$$와 각 $$i$$에 대한 isomorphism $$\phi_i: \pi^{-1}(U_i) \to U_i \times \mathbb{A}^r$$ (local trivialization).
3. 각 $$i, j$$에 대해 $$\phi_j \circ \phi_i^{-1}: (U_i \cap U_j) \times \mathbb{A}^r \to (U_i \cap U_j) \times \mathbb{A}^r$$이 $$(p, v) \mapsto (p, g_{ij}(p)v)$$의 꼴인 조건. 여기서 $$g_{ij} \in \operatorname{GL}_r(\mathcal{O}_X(U_i \cap U_j))$$는 *transition function*이라 부른다.

</div>

Line bundle의 정의와 비교하면, 유일한 차이는 fiber가 $$\mathbb{A}^1$$ 대신 $$\mathbb{A}^r$$이고, transition function이 $$\mathcal{O}_X(U_i \cap U_j)^\ast = \operatorname{GL}_1(\mathcal{O}_X(U_i \cap U_j))$$ 대신 $$\operatorname{GL}_r(\mathcal{O}_X(U_i \cap U_j))$$ 값을 갖는다는 점이다. 따라서 line bundle은 정확히 rank 1 vector bundle이다.

<div class="proposition" markdown="1">

<ins id="prop18">**명제 18**</ins> Transition functions $$\{g_{ij}\}$$는 다음의 *cocycle condition*을 만족한다.

1. $$g_{ii} = I_r$$ for all $$i$$.
2. $$g_{ij} = g_{ji}^{-1}$$ for all $$i, j$$.
3. $$g_{ij} g_{jk} = g_{ik}$$ on $$U_i \cap U_j \cap U_k$$ for all $$i, j, k$$.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

[명제 2](#prop2)의 증명과 동일하다. 다만 $$g_{ij}$$가 행렬값을 가지므로 곱셈의 순서에 주의해야 한다.

</details>

<div class="example" markdown="1">

<ins id="ex19">**예시 19**</ins> *Trivial vector bundle* $$\mathcal{O}_X^{\oplus r} = X \times \mathbb{A}^r$$은 모든 transition function이 $$g_{ij} = I_r$$인 rank $$r$$ vector bundle이다.

</div>

<div class="example" markdown="1">

<ins id="ex20">**예시 20**</ins> *Tangent bundle* $$\mathcal{T}_X$$는 다양체 $$X$$의 각 점 $$p$$에 그 점에서의 tangent space $$T_p X$$를 대응시키는 vector bundle이다. 만약 $$X$$가 $$n$$차원 smooth variety이면 $$\mathcal{T}_X$$는 rank $$n$$ vector bundle이다. Local coordinate $$\x_1, \ldots, \x_n$$에서 $$\mathcal{T}_X$$의 local frame은 $$\partial/\partial \x_1, \ldots, \partial/\partial \x_n$$으로 주어진다.

</div>

<div class="example" markdown="1">

<ins id="ex21">**예시 21**</ins> *Cotangent bundle* (또는 *canonical bundle*) $$\Omega_X^1 = \mathcal{T}_X^\vee$$는 tangent bundle의 dual이다. 각 점 $$p$$에서 fiber는 cotangent space $$T_p^\ast X$$이며, 이는 $$T_p X$$의 dual space이다. Rank $$n$$ 다양체에서 $$\Omega_X^1$$은 rank $$n$$ vector bundle이고, local coordinate에서 $$d\x_1, \ldots, d\x_n$$이 local frame을 이룬다. Top exterior power $$\omega_X = \bigwedge^n \Omega_X^1$$은 *canonical line bundle*이라 불리며, Serre duality 등에서 중요한 역할을 한다.

</div>

Vector bundle에 대해서도 line bundle과 유사한 연산을 정의할 수 있다. 두 vector bundle $$\mathcal{E}, \mathcal{F}$$의 tensor product $$\mathcal{E} \otimes \mathcal{F}$$는 fiberwise tensor product로 정의되며, 그 transition functions은 $$g_{ij}^{\mathcal{E}} \otimes g_{ij}^{\mathcal{F}}$$이다. Dual bundle $$\mathcal{E}^\vee$$의 transition functions은 $$\left(g_{ij}^{\mathcal{E}}\right)^{-t}$$ (inverse transpose)이다. 또한 direct sum $$\mathcal{E} \oplus \mathcal{F}$$는 fiberwise direct sum으로 정의되며, 이때 transition functions은 block diagonal 행렬 $$\begin{pmatrix} g_{ij}^{\mathcal{E}} & 0 \\ 0 & g_{ij}^{\mathcal{F}} \end{pmatrix}$$이 된다.

## Sections of Line Bundles

Line bundle $$\mathcal{L}$$을 이해하는 가장 직접적인 방법 중 하나는 그 section들을 연구하는 것이다. Section은 line bundle의 각 fiber에서 원소를 선택하는 "함수"로, 이는 함수의 개념을 일반화한 것이다. Trivial bundle $$\mathcal{O}_X$$의 section은 단순히 $$X$$ 위의 정칙함수이지만, 일반적인 line bundle의 section은 "twisted function"으로 해석할 수 있다. Global section들의 공간 $$H^0(X, \mathcal{L})$$은 단순한 벡터공간이지만, 그 dimension과 구조는 다양체 $$X$$와 line bundle $$\mathcal{L}$$의 기하학에 대한 풍부한 정보를 담고 있다. 특히 $$\mathcal{L}$$이 *very ample*인 경우, $$H^0(X, \mathcal{L})$$은 $$X$$를 사영공간에 매장하는 데 사용될 수 있으며, 이는 line bundle이 다양체의 기하학을 연구하는 강력한 도구임을 보여준다.

<div class="definition" markdown="1">

<ins id="def22">**정의 22**</ins> Line bundle $$\mathcal{L}$$의 *global section*들은 $$H^0(X, \mathcal{L})$$로 표기하며, 이는 $$\mathcal{L}$$의 section sheaf의 전역 section들의 공간이다. 즉, $$H^0(X, \mathcal{L}) = \mathcal{O}_X(\mathcal{L})(X)$$는 각 점에 대해 $$\mathcal{L}$$의 fiber 내의 원소를 대응시키는 정칙 사상들의 집합이다.

</div>

<div class="proposition" markdown="1">

<ins id="prop23">**명제 23**</ins> [§Divisors](/ko/math/algebraic_geometry/divisors)에서 정의한 *effective divisor* (모든 계수가 음이 아닌 divisor) $$D$$에 대하여, $$H^0(X, \mathcal{O}_X(D))$$는 $$D$$보다 크거나 같은 effective divisor들에 대응되는 rational function들의 공간과 자연스럽게 동형이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$\mathcal{O}_X(D)$$의 section $$s$$는 각 $$U_i$$에서 $$s_i \in \mathcal{O}_X(U_i)$$로 표현되고, $$U_i \cap U_j$$에서 $$s_i = (f_i/f_j) s_j$$를 만족한다. 이는 rational function $$f = s_i/f_i$$를 정의하며, $$\operatorname{div}(f) + D \ge 0$$을 만족한다. 역으로, 이러한 $$f$$로부터 section $$s$$를 재구성할 수 있다.

</details>

<div class="example" markdown="1">

<ins id="ex24">**예시 24**</ins> **$$\mathbb{P}^n$$의 line bundle sections**: $$H^0(\mathbb{P}^n, \mathcal{O}_{\mathbb{P}^n}(d))$$는 차수 $$d$$의 동차다항식들의 공간과 동형이다. 이는 ([§사영다양체, ⁋정의 2](/ko/math/algebraic_geometry/projective_varieties#def2))에서 정의된 homogeneous coordinates $$\x_0, \ldots, \x_n$$에 의해 생성된다.

</div>

## Tautological Bundle

사영공간 $$\mathbb{P}^n$$ 위에는 특별한 line bundle이 존재하는데, 이는 $$\mathbb{P}^n$$의 정의 자체로부터 자연스럽게 유도된다. 이 *tautological bundle*은 $$\mathbb{P}^n$$의 각 점이 나타내는 직선을 그 점에 대응시키는 bundle로, $$\mathcal{O}_{\mathbb{P}^n}(-1)$$과 동형이다. 이 bundle은 사영공간의 기하학을 이해하는 데 근본적인 역할을 하며, Grassmannian으로의 일반화를 통해 더 높은 차원의 기하학적 구조를 연구하는 데에도 핵심적인 도구가 된다.

<div class="definition" markdown="1">

<ins id="def25">**정의 25**</ins> $$\mathbb{P}^n$$ 위의 *tautological line bundle* $$\mathcal{O}_{\mathbb{P}^n}(-1)$$은 다음과 같이 정의된다. $$\mathbb{P}^n$$의 각 점 $$[x] = [x_0 : \cdots : x_n]$$은 $$\mathbb{A}^{n+1}$$의 원점을 지나는 직선 $$\ell_{[x]} = \{(\lambda x_0, \ldots, \lambda x_n) \mid \lambda \in \mathbb{K}\}$$을 결정한다. 이 직선을 그 점의 fiber로 갖는 line bundle을 정의한다.

$$\mathcal{O}_{\mathbb{P}^n}(-1) = \{([x], v) \in \mathbb{P}^n \times \mathbb{A}^{n+1} \mid v \in \ell_{[x]}\}$$

</div>

이 정의에서 각 fiber $$\mathcal{O}_{\mathbb{P}^n}(-1)_{[x]}$$는 점 $$[x]$$가 나타내는 직선 그 자체이다. 사영화 $$\mathbb{A}^{n+1} \setminus \{0\} \to \mathbb{P}^n$$의 각 fiber가 바로 이 직선들이므로, tautological bundle은 사영화의 구조를 bundle의 언어로 재해석한 것이라 이해할 수 있다.

<div class="proposition" markdown="1">

<ins id="prop26">**명제 26**</ins> Tautological bundle $$\mathcal{O}_{\mathbb{P}^n}(-1)$$은 위 [예시 12](#ex12)에서 정의한 $$\mathcal{O}_{\mathbb{P}^n}(1)$$의 dual이다. 즉, $$\mathcal{O}_{\mathbb{P}^n}(-1) \cong \mathcal{O}_{\mathbb{P}^n}(1)^\vee$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Standard open cover $$U_i = \{[x] \mid x_i \ne 0\}$$에서 $$\mathcal{O}_{\mathbb{P}^n}(-1)$$의 local trivialization을 구성하자. 점 $$([x], v) \in \mathcal{O}_{\mathbb{P}^n}(-1)$$에 대해, $$v \in \ell_{[x]}$$이므로 $$v = \lambda x$$인 어떤 $$\lambda \in \mathbb{K}$$가 존재한다. $$U_i$$ 위에서 $$\phi_i: \pi^{-1}(U_i) \to U_i \times \mathbb{A}^1$$을 $$\phi_i([x], v) = ([x], v_i)$$로 정의하자. 이때 $$v_i$$는 $$v$$의 $$i$$번째 좌표이다. 역사상 $$\phi_i^{-1}([x], t)$$는 $$v_i = t$$이고 $$v \in \ell_{[x]}$$인 $$v$$를 찾아야 한다. $$v = \lambda x$$이면 $$\lambda x_i = t$$이므로 $$\lambda = t/x_i$$이고, 따라서 $$v = (t/x_i) x$$이다.

이제 $$U_i \cap U_j$$에서의 transition function을 계산하자. $$\phi_j \circ \phi_i^{-1}([x], t) = \phi_j([x], (t/x_i) x) = ([x], t x_j / x_i)$$이다. 따라서 $$g_{ij}([x]) = x_j/x_i$$이고, 이는 $$\mathcal{O}_{\mathbb{P}^n}(1)$$의 transition function $$x_i/x_j$$의 inverse이다.

</details>

이 명제는 $$\mathcal{O}_{\mathbb{P}^n}(-1)$$의 표기법을 정당화한다. $$\mathcal{O}_{\mathbb{P}^n}(d)$$의 transition functions이 $$(x_i/x_j)^d$$이므로, $$d = -1$$인 경우가 바로 tautological bundle이다. 특히 $$H^0(\mathbb{P}^n, \mathcal{O}_{\mathbb{P}^n}(-1)) = 0$$임을 알 수 있는데, 이는 tautological bundle이 non-vanishing global section을 갖지 않음을 의미한다. 이는 각 fiber가 서로 다른 직선이므로, 모든 점에서 동시에 0이 아닌 값을 갖는 section을 선택할 수 없기 때문이다.

### Grassmannian으로의 일반화

Tautological bundle의 개념은 사영공간에서 Grassmannian으로 자연스럽게 일반화된다. Grassmannian $$\operatorname{Gr}(k, n)$$은 $$n$$차원 벡터공간의 $$k$$차원 부분공간들의 공간이며, $$\operatorname{Gr}(1, n+1) = \mathbb{P}^n$$이다. 이 일반화에서 tautological bundle은 rank $$k$$ vector bundle이 되며, 이와 쌍대를 이루는 *quotient bundle*도 자연스럽게 정의된다.

<div class="definition" markdown="1">

<ins id="def27">**정의 27**</ins> Grassmannian $$\operatorname{Gr}(k, n)$$ 위에 다음 두 vector bundle을 정의한다.

1. *Tautological bundle* $$S$$: 각 점 $$[V] \in \operatorname{Gr}(k, n)$$ (여기서 $$V \subseteq \mathbb{A}^n$$는 $$k$$차원 부분공간)에 그 부분공간 $$V$$ 자체를 fiber로 대응시키는 rank $$k$$ vector bundle.
   $$S = \{([V], v) \in \operatorname{Gr}(k, n) \times \mathbb{A}^n \mid v \in V\}$$

2. *Quotient bundle* $$Q$$: 각 점 $$[V]$$에 몫공간 $$\mathbb{A}^n / V$$를 fiber로 대응시키는 rank $$n-k$$ vector bundle.
   $$Q = \{([V], [w]) \in \operatorname{Gr}(k, n) \times (\mathbb{A}^n / S) \mid [w] \in \mathbb{A}^n / V\}$$

</div>

이들 사이에는 자연스러운 short exact sequence가 존재한다.

$$0 \to S \to \mathcal{O}_{\operatorname{Gr}(k,n)}^{\oplus n} \to Q \to 0$$

여기서 가운데 항은 $$\operatorname{Gr}(k, n) \times \mathbb{A}^n$$으로, trivial bundle of rank $$n$$이다. 첫 번째 사상은 각 점 $$([V], v) \in S$$를 $$([V], v) \in \mathcal{O}^{\oplus n}$$으로 포함시키는 것이고, 두 번째 사상은 $$([V], w) \in \mathcal{O}^{\oplus n}$$을 $$([V], [w]) \in Q$$로 보내는 quotient map이다.

<div class="proposition" markdown="1">

<ins id="prop28">**명제 28**</ins> $$\operatorname{Gr}(1, n+1) = \mathbb{P}^n$$에서 tautological bundle $$S$$는 $$\mathcal{O}_{\mathbb{P}^n}(-1)$$과 동형이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$\operatorname{Gr}(1, n+1)$$의 각 점은 $$\mathbb{A}^{n+1}$$의 1차원 부분공간, 즉 원점을 지나는 직선이다. 이는 정확히 $$\mathbb{P}^n$$의 점에 해당한다. Tautological bundle $$S$$의 각 fiber는 이 직선 그 자체이므로, 이는 [정의 25](#def25)에서 정의한 $$\mathcal{O}_{\mathbb{P}^n}(-1)$$과 동일하다.

</details>

이 명제는 Grassmannian의 tautological bundle이 사영공간에서는 익숙한 $$\mathcal{O}(-1)$$으로 귀결됨을 보여준다. Quotient bundle $$Q$$의 경우, $$\operatorname{Gr}(1, n+1) = \mathbb{P}^n$$에서 rank $$n$$이며, 이는 tangent bundle $$\mathcal{T}_{\mathbb{P}^n}$$과 밀접한 관계가 있다. 실제로 $$\mathcal{T}_{\mathbb{P}^n} \cong \operatorname{Hom}(S, Q) \cong S^\vee \otimes Q$$가 성립한다.

Grassmannian 위의 tautological bundle과 quotient bundle은 Schubert calculus, quantum cohomology 등 현대 대수기하학의 핵심 도구이며, 이들의 Chern class들은 Grassmannian의 cohomology ring을 생성한다. 이는 tautological bundle이 단순히 하나의 예시를 넘어, 대수기하학 전반에 걸쳐 근본적인 구조임을 시사한다.

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.
