---
title: "유리사상"
excerpt: "Rational maps and birational equivalence"

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/rational_maps
sidebar: 
    nav: "algebraic_geometry-ko"

header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Rational_Maps.png
    overlay_filter: 0.5

date: 2026-03-12
last_modified_at: 2026-03-12
weight: 5

---

[§정칙사상](/ko/math/algebraic_geometry/regular_maps)에서 우리는 준사영다양체 사이의 "다항식 사상"인 regular map을 정의했다. 그러나 모든 다항식 함수가 모든 점에서 정의되는 것은 아니다. 예를 들어 $(x, y) \mapsto [x : y]$는 원점에서 정의되지 않는다. 이 절에서 우리는 "대부분의 점에서" 정의되는 함수인 *유리사상*을 연구한다.

## 유리함수

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 준사영다양체 $X$ 위의 *rational function<sub>유리함수</sub>*란 $X$의 어떤 비어있지 않은 열린부분집합 $U$에서 정의된 regular function $f: U \to \mathbb{K}$를 말한다. 두 rational function $f: U \to \mathbb{K}$와 $g: V \to \mathbb{K}$는 $U \cap V$에서 일치할 때 같은 것으로 본다.

</div>

$X$ 위의 모든 rational function들의 집합을 $\mathbb{K}(X)$로 표기한다. 이는 field를 이룬다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> 기약 아핀다양체 $X$에 대해 $\mathbb{K}(X)$는 coordinate ring $\mathbb{K}[X]$의 fraction field와 같다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$\mathbb{K}[X]$의 원소는 $X$ 전체에서 정의되는 regular function이다. $\mathbb{K}(X)$의 원소는 $X$의 열린부분집합에서 정의되는 regular function이다. 기약다양체에서 두 열린부분집합의 교집합은 비어있지 않으므로, $f/g \in \text{Frac}(\mathbb{K}[X])$는 $X \setminus V(g)$에서 정의되는 rational function이다. 역으로, 임의의 rational function은 어떤 열린집합 $U$에서 다항식으로 표현되고, $U$는 principal open set들의 합집합이므로 fraction field의 원소로 표현된다.

</details>

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins>

1. $\mathbb{K}(\mathbb{A}^n) = \mathbb{K}(x_1, \ldots, x_n)$ (rational function field)
2. $\mathbb{K}(\mathbb{P}^n) = \mathbb{K}(x_1/x_0, \ldots, x_n/x_0) \cong \mathbb{K}(t_1, \ldots, t_n)$
3. $\mathbb{K}(V(y - x^2)) = \mathbb{K}(x)$

</div>

## 유리사상의 정의

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> 기약 준사영다양체 $X, Y$ 사이의 *rational map<sub>유리사상</sub>*이란 $X$의 어떤 비어있지 않은 열린부분집합 $U$에서 정의된 regular map $\varphi: U \to Y$를 말한다. 두 rational map $\varphi: U \to Y$와 $\psi: V \to Y$는 $U \cap V$에서 일치할 때 같은 것으로 본다.

</div>

Rational map은 보통 $\varphi: X \dashrightarrow Y$로 표기하며, 점선은 "모든 점에서 정의되지 않을 수 있음"을 나타낸다.

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> Rational map $\varphi: X \dashrightarrow Y$의 *domain of definition* $\text{dom}(\varphi)$는 $\varphi$가 정의되는 점들의 집합이다. 이는 $X$의 열린부분집합이다.

</div>

<div class="example" markdown="1">

<ins id="ex6">**예시 6**</ins> $\mathbb{P}^2 \dashrightarrow \mathbb{P}^1$, $[x : y : z] \mapsto [x : y]$는 rational map이다. Domain은 $\mathbb{P}^2 \setminus \{[0 : 0 : 1]\}$이다.

</div>

<div class="example" markdown="1">

<ins id="ex7">**예시 7**</ins> $\mathbb{A}^2 \dashrightarrow \mathbb{P}^1$, $(x, y) \mapsto [x : y]$는 rational map이다. Domain은 $\mathbb{A}^2 \setminus \{(0, 0)\}$이다.

</div>

## Birational Equivalence

<div class="definition" markdown="1">

<ins id="def8">**정의 8**</ins> Rational map $\varphi: X \dashrightarrow Y$가 *birational map*이라는 것은 역 rational map $\psi: Y \dashrightarrow X$가 존재하여 $\psi \circ \varphi = \text{id}_X$와 $\varphi \circ \psi = \text{id}_Y$가 (정의되는 곳에서) 성립하는 것이다.

</div>

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> 다음이 동치이다.

1. $X$와 $Y$는 birationally equivalent하다.
2. $\mathbb{K}(X) \cong \mathbb{K}(Y)$ (as fields)
3. $X$와 $Y$의 isomorphic한 비어있지 않은 열린부분집합들이 존재한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

(1) $\Rightarrow$ (2): Birational map $\varphi: X \dashrightarrow Y$는 $\mathbb{K}(Y) \to \mathbb{K}(X)$의 field isomorphism을 유도한다.

(2) $\Rightarrow$ (3): $\mathbb{K}(X) \cong \mathbb{K}(Y)$이면, 이 isomorphism은 rational map $\varphi: X \dashrightarrow Y$를 정의한다. $\varphi$가 isomorphism인 열린부분집합들을 찾을 수 있다.

(3) $\Rightarrow$ (1): 자명하다.

</details>

<div class="example" markdown="1">

<ins id="ex10">**예시 10**</ins> $\mathbb{P}^1$과 $V(xy - zw) \subset \mathbb{P}^3$은 birationally equivalent하다. 둘 다 rational function field $\mathbb{K}(t)$를 갖는다.

</div>

## Rational Map과 Blow-up

<div class="example" markdown="1">

<ins id="ex11">**예시 11**</ins> **Blow-up of $\mathbb{A}^2$ at origin**: 

$$\text{Bl}_0 \mathbb{A}^2 = \{((x, y), [u : v]) \in \mathbb{A}^2 \times \mathbb{P}^1 \mid xv = yu\}$$

Projection $\pi: \text{Bl}_0 \mathbb{A}^2 \to \mathbb{A}^2$는 birational map이고, 원점 위의 fiber는 $\mathbb{P}^1$이다.

</div>

---

**참고문헌**

**[Har]** J. Harris, *Algebraic Geometry: A First Course*, Springer, 1992.  
**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.
