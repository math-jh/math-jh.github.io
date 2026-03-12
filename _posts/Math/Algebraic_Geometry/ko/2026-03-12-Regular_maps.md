---
title: "정칙사상"
excerpt: "Regular maps between quasi-projective varieties"

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/regular_maps
sidebar: 
    nav: "algebraic_geometry-ko"

header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Regular_Maps.png
    overlay_filter: 0.5

date: 2026-03-12
last_modified_at: 2026-03-12
weight: 4

---

[§준사영다양체](/ko/math/algebraic_geometry/quasi_projective_varieties)에서 우리는 아핀다양체와 사영다양체를 모두 포함하는 준사영다양체의 개념을 정의했다. 이제 우리는 이들 사이의 "다항식 사상"을 정확히 정규화할 것이다. 이미 아핀다양체와 사영다양체의 경우 morphism을 정의했지만, 준사영다양체의 경우는 더 일반적인 정의가 필요하다.

## 정칙사상의 정의

준사영다양체의 morphism은 국소적으로 다항식으로 표현되는 함수이다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 준사영다양체 $$X$$ 위의 점 $$p$$에서의 *regular function<sub>정칙함수</sub>*란 $$p$$의 어떤 열린근방 $$U$$에서 정의된 함수 $$f: U \to \mathbb{K}$$로서, $$f$$가 $$U$$에서 다항식으로 표현되는 것을 말한다.

</div>

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> 준사영다양체 $$X$$ 위의 *regular function*이란 모든 점에서 regular function인 함수 $$f: X \to \mathbb{K}$$를 말한다. $$X$$ 위의 모든 regular function들의 집합을 $$\mathcal{O}(X)$$ 또는 $$\mathcal{O}_X(X)$$로 표기한다.

</div>

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins>

1. 아핀다양체 $$X$$에서 $$\mathcal{O}(X) = \mathbb{K}[X]$$이다.
2. $$\mathbb{P}^n$$에서 $$\mathcal{O}(\mathbb{P}^n) = \mathbb{K}$$이다. (상수함수만 존재)
3. $$\mathbb{A}^2 \setminus \{(0,0)\}$$에서 $$\mathcal{O}(X) = \mathbb{K}[x, y]$$이다.

</div>

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> 준사영다양체 $$X, Y$$ 사이의 *regular map<sub>정칙사상</sub>* (또는 *morphism*) $$\varphi: X \to Y$$는 다음 조건을 만족하는 함수이다:

$$Y$$의 임의의 열린부분집합 $$V$$와 regular function $$f \in \mathcal{O}(V)$$에 대해, $$f \circ \varphi: \varphi^{-1}(V) \to \mathbb{K}$$는 regular function이다.

</div>

즉, regular map은 regular function을 pullback하는 함수이다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> 아핀다양체와 사영다양체의 경우, 위 정의는 이전의 morphism 정의와 일치한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

아핀다양체의 경우, [§아핀다양체, ⁋명제 14](/ko/math/algebraic_geometry/affine_varieties#prop14)에서 morphism이 coordinate ring homomorphism을 유도함을 보였다. 이는 regular function을 pullback한다는 것과 같다.

사영다양체의 경우, 정의에 의해 각 점에서 homogeneous polynomials로 표현되므로, regular function의 pullback은 여전히 regular function이다.

</details>

## 정칙사상의 합성과 동형

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> Regular map의 합성은 regular map이다. 항등사상은 regular map이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$\varphi: X \to Y$$, $$\psi: Y \to Z$$가 regular map이라 하자. $$f \in \mathcal{O}(W)$$ ($$W \subseteq Z$$ 열린집합)라면, $$\psi^{-1}(W)$$에서 $$f \circ \psi$$는 regular이고, $$\varphi^{-1}(\psi^{-1}(W))$$에서 $$(f \circ \psi) \circ \varphi = f \circ (\psi \circ \varphi)$$는 regular이다. 따라서 $$\psi \circ \varphi$$는 regular map이다.

</details>

따라서 준사영다양체들과 regular map들은 category를 이룬다.

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> Regular map $$\varphi: X \to Y$$가 *isomorphism<sub>동형사상</sub>*이라는 것은 역함수 $$\psi: Y \to X$$가 존재하여 $$\psi$$도 regular map인 것이다.

</div>

<div class="example" markdown="1">

<ins id="ex8">**예시 8**</ins>

1. $$\mathbb{A}^1 \to V(y - x^2) \subset \mathbb{A}^2$$, $$t \mapsto (t, t^2)$$는 isomorphism이다.
2. $$\mathbb{P}^1 \to V(x_0 x_2 - x_1^2) \subset \mathbb{P}^2$$, $$[x : y] \mapsto [x^2 : xy : y^2]$$는 isomorphism이다.
3. $$\mathbb{A}^1 \setminus \{0\} \to V(xy - 1) \subset \mathbb{A}^2$$, $$t \mapsto (t, 1/t)$$는 isomorphism이다.

</div>

## 정칙사상의 성질

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> Regular map $$\varphi: X \to Y$$는 연속함수이다. (Zariski 위상에서)

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$Z \subseteq Y$$가 닫힌집합이라면, $$Z = V(f_1, \ldots, f_k)$$ for some regular functions $$f_i$$ on some open cover of $$Y$$이다. 그럼 $$\varphi^{-1}(Z) = V(f_1 \circ \varphi, \ldots, f_k \circ \varphi)$$이고, 각 $$f_i \circ \varphi$$는 regular이므로 $$\varphi^{-1}(Z)$$는 닫힌집합이다.

</details>

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10**</ins> 닫힌집합으로의 regular map의 제한은 regular map이다. 열린집합으로의 regular map의 제한도 regular Map이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Regular function의 정의에 의해 자명하다.

</details>

## Examples

<div class="example" markdown="1">

<ins id="ex11">**예시 11**</ins> **Projection**: $$\mathbb{A}^2 \to \mathbb{A}^1$$, $$(x, y) \mapsto x$$는 regular map이다.

</div>

<div class="example" markdown="1">

<ins id="ex12">**예시 12**</ins> **Inclusion**: $$\mathbb{A}^1 \hookrightarrow \mathbb{P}^1$$, $$t \mapsto [t : 1]$$는 regular map이다.

</div>

<div class="example" markdown="1">

<ins id="ex13">**예시 13**</ins> **Veronese embedding**: $$\mathbb{P}^n \to \mathbb{P}^N$$, $$[x_0 : \cdots : x_n] \mapsto [\cdots : x_i x_j : \cdots]$$ (모든 단항식 $$x_i x_j$$)은 regular map이다. 여기서 $$N = \binom{n+2}{2} - 1$$이다.

</div>

---

**참고문헌**

**[Har]** J. Harris, *Algebraic Geometry: A First Course*, Springer, 1992.  
**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.
