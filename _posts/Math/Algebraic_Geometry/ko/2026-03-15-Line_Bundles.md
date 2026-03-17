---
title: "Line Bundles"
excerpt: "Line bundles, invertible sheaves, and the Picard group"

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/line_bundles
sidebar:
    nav: "algebraic_geometry-ko"

header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Line_Bundles.png
    overlay_filter: 0.5

date: 2026-03-15
last_modified_at: 2026-03-15
weight: 10

---

[\[Divisors\]](/ko/math/algebraic_geometry/divisors)에서 우리는 유리함수의 영점과 극점을 형식합으로 표현하는 divisor의 개념을 정의했다. Divisor class group $$\operatorname{Cl}(X)$$는 divisor들의 선형 동치류들의 group이며, 이는 다양체의 중요한 불변량이다. 이제 우리는 divisor와 밀접하게 관련된 또 다른 중요한 개념인 *line bundle*을 소개한다.

Line bundle은 다양체 위의 각 점에 1차원 벡터공간을 대응시키는 "twisted product"이다. 가장 간단한 예는 trivial line bundle $$X \times \mathbb{A}^1 \to X$$이지만, 일반적으로 line bundle은 국소적으로는 trivial하면서 전역적으로는 "twisted"된 구조를 가질 수 있다. Line bundle들의 isomorphism class들은 *Picard group*을 형성하며, 이는 [명제 16](#prop16)에서 보듯 divisor class group과 자연스럽게 동형이다.

## Line Bundle의 정의

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 다양체 $$X$$ 위의 *line bundle* (또는 *invertible sheaf*) $$\mathcal{L}$$은 다음과 같은 데이터로 구성된다.

1. 전사 사상 $$\pi: \mathcal{L} \to X$$.
2. $$X$$의 open cover $$\{U_i\}$$와 각 $$i$$에 대한 isomorphism $$\phi_i: \pi^{-1}(U_i) \to U_i \times \mathbb{A}^1$$ (이를 *local trivialization*이라 부른다).
3. 각 $$i, j$$에 대해 $$\phi_j \circ \phi_i^{-1}: (U_i \cap U_j) \times \mathbb{A}^1 \to (U_i \cap U_j) \times \mathbb{A}^1$$이 $$(p, t) \mapsto (p, g_{ij}(p)t)$$의 꼴인 조건. 여기서 $$g_{ij} \in \mathcal{O}_X(U_i \cap U_j)^\ast$$는 *transition function*이라 부른다. $$\mathcal{O}_X(U_i \cap U_j)^\ast$$는 교차 부분 $$U_i \cap U_j$$ 위의 nowhere vanishing 정칙함수들의 곱셈군을 의미한다.

</div>

각 점 $$p \in X$$에 대해 fiber $$\mathcal{L}_p = \pi^{-1}(p)$$는 1차원 벡터공간이다. Local trivialization $$\phi_i$$는 $$U_i$$ 위에서 $$\mathcal{L}$$을 trivial bundle $$U_i \times \mathbb{A}^1$$과 동형으로 만든다. Transition function $$g_{ij}$$는 두 trivialization 사이의 "twist"를 측정한다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> Transition functions $$\{g_{ij}\}$$는 다음의 *cocycle condition*을 만족한다.

1. $$g_{ii} = 1$$ for all $$i$$.
2. $$g_{ij} = g_{ji}^{-1}$$ for all $$i, j$$.
3. $$g_{ij} g_{jk} = g_{ik}$$ on $$U_i \cap U_j \cap U_k$$ for all $$i, j, k$$.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

이들은 모두 $$\phi_j \circ \phi_i^{-1}$$의 정의로부터 직접 따른다. 예를 들어, $$U_i \cap U_j \cap U_k$$에서

$$(p, t) \xrightarrow{\phi_i^{-1}} (p, t) \xrightarrow{\phi_k} (p, g_{ik}(p)t)$$

$$(p, t) \xrightarrow{\phi_i^{-1}} (p, t) \xrightarrow{\phi_j} (p, g_{ij}(p)t) \xrightarrow{\phi_k} (p, g_{jk}(p)g_{ij}(p)t)$$

이 두 경로가 같아야 하므로 $$g_{ik} = g_{jk} g_{ij}$$이다.

</details>

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> *Trivial line bundle* $$\mathcal{O}_X = X \times \mathbb{A}^1$$은 모든 transition function이 $$g_{ij} = 1$$인 line bundle이다. 이는 "twist가 없는" 가장 간단한 line bundle이다.

</div>

## Invertible Sheaf로서의 Line Bundle

Line bundle은 sheaf 이론의 언어로 *invertible sheaf*로 표현할 수 있다. 이 관점은 line bundle의 section들을 다루는 데 더 자연스럽다.

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> Sheaf $$\mathcal{F}$$가 *invertible*이라는 것은 각 점 $$p \in X$$의 근방 $$U$$에서 $$\mathcal{F}|_U \cong \mathcal{O}_U$$인 것이다. 즉, $$\mathcal{F}$$가 국소적으로 구조층과 동형인 sheaf이다.

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

$$\mathbb{A}^n = \mathbb{V}(\emptyset) \subseteq \mathbb{A}^n$$의 coordinate ring $$\mathbb{K}[\x_1, \ldots, \x_n]$$는 unique factorization domain이다. 이 경우 모든 line bundle은 trivial이다. 이는 [\[Divisors\] §예시 9](/ko/math/algebraic_geometry/divisors#ex9)에서 $$\operatorname{Cl}(\mathbb{A}^n) = 0$$임과 일치한다.

</details>

<div class="example" markdown="1">

<ins id="ex12">**예시 12**</ins> **$$\mathbb{P}^n$$의 Picard group**: $$\operatorname{Pic}(\mathbb{P}^n) \cong \mathbb{Z}$$이다. 생성원은 *hyperplane bundle* $$\mathcal{O}_{\mathbb{P}^n}(1)$$이다.

</div>

$$\mathcal{O}_{\mathbb{P}^n}(1)$$은 다음과 같이 정의된다. $$\mathbb{P}^n$$의 standard open cover $$U_i = \{[x_0 : \cdots : x_n] \mid x_i \ne 0\}$$에서, transition functions은 $$g_{ij} = x_j/x_i$$이다. 일반적으로 $$\mathcal{O}_{\mathbb{P}^n}(d)$$는 $$g_{ij} = (x_j/x_i)^d$$를 transition functions으로 갖는 line bundle이며, $$\operatorname{div}(x_0^d) = dH$$에 대응된다. 여기서 $$H = \mathbb{V}(x_0)$$는 hyperplane divisor이다.

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

역으로, line bundle $$\mathcal{L}$$이 주어지면, $$\mathcal{L}$$의 *rational section* $$s$$를 다음과 같이 선택하여 divisor $$\operatorname{div}(s)$$를 정의할 수 있다. $$\mathcal{L}$$은 국소적으로 $$\mathcal{O}_X$$와 동형이므로, Zariski open dense 부분집합 $$U \subseteq X$$에서 $$\mathcal{L}|_U \cong \mathcal{O}_U$$이다. 이 동형 하에서 $$\mathcal{O}_U$$의 상수 section $$1$$의 원상을 $$s$$라 하면, $$s$$는 $$U$$ 위에서 nowhere vanishing이며 $$X$$의 나머지 부분에서 극점과 영점을 가질 수 있다. $$s$$의 zero/pole locus로부터 Weil divisor $$\operatorname{div}(s) = \sum_P v_P(s) P$$를 정의할 수 있으며, 여기서 $$v_P(s)$$는 점 $$P$$에서의 소멸 차수이다. 다른 rational section $$s' = fs$$ ($$f \in \mathbb{K}(X)^\ast$$)를 선택하면 $$\operatorname{div}(s') = \operatorname{div}(f) + \operatorname{div}(s)$$이므로, linear equivalence class $$[\operatorname{div}(s)]$$는 well-defined이다. 따라서 $$\mathcal{L} \mapsto [\operatorname{div}(s)]$$는 $$\operatorname{Pic}(X)$$에서 $$\operatorname{Cl}(X)$$로의 inverse map을 정의한다.

</details>

## Sections of Line Bundles

<div class="definition" markdown="1">

<ins id="def17">**정의 17**</ins> Line bundle $$\mathcal{L}$$의 *global section*들은 $$H^0(X, \mathcal{L})$$로 표기하며, 이는 $$\mathcal{L}$$의 section sheaf의 전역 section들의 공간이다. 즉, $$H^0(X, \mathcal{L}) = \mathcal{O}_X(\mathcal{L})(X)$$는 각 점에 대해 $$\mathcal{L}$$의 fiber 내의 원소를 대응시키는 정칙 사상들의 집합이다.

</div>

<div class="proposition" markdown="1">

<ins id="prop18">**명제 18**</ins> Effective divisor $$D$$에 대하여, $$H^0(X, \mathcal{O}_X(D))$$는 $$D$$보다 크거나 같은 effective divisor들에 대응되는 rational function들의 공간과 자연스럽게 동형이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$\mathcal{O}_X(D)$$의 section $$s$$는 각 $$U_i$$에서 $$s_i \in \mathcal{O}_X(U_i)$$로 표현되고, $$U_i \cap U_j$$에서 $$s_i = (f_i/f_j) s_j$$를 만족한다. 이는 rational function $$f = s_i/f_i$$를 정의하며, $$\operatorname{div}(f) + D \ge 0$$을 만족한다. 역으로, 이러한 $$f$$로부터 section $$s$$를 재구성할 수 있다.

</details>

<div class="example" markdown="1">

<ins id="ex19">**예시 19**</ins> **$$\mathbb{P}^n$$의 line bundle sections**: $$H^0(\mathbb{P}^n, \mathcal{O}_{\mathbb{P}^n}(d))$$는 차수 $$d$$의 동차다항식들의 공간과 동형이다. 이는 [\[사영다양체\] §동차다항식과 사영공간](/ko/math/algebraic_geometry/projective_varieties#def2)에서 정의된 homogeneous coordinates $$\x_0, \ldots, \x_n$$에 의해 생성된다.

</div>

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.
