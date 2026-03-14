---
title: "준사영다양체"
excerpt: "Quasi-projective varieties as the natural class of objects in algebraic geometry"

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/quasi_projective_varieties
sidebar: 
    nav: "algebraic_geometry-ko"

header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Quasi_Projective_Varieties.png
    overlay_filter: 0.5

date: 2026-03-12
last_modified_at: 2026-03-12
weight: 3

---

[§아핀다양체](/ko/math/algebraic_geometry/affine_varieties)와 [§사영다양체](/ko/math/algebraic_geometry/projective_varieties)에서 우리는 각각 아핀공간과 사영공간의 부분집합으로 정의되는 기하적 대상들을 살펴보았다. 그러나 대수기하학에서 가장 자연스러운 대상들은 이 둘을 모두 포함하는 더 큰 범주에 속한다. 이 절에서 우리는 *quasi-projective variety*를 정의하고, 이것이 아핀다양체와 사영다양체를 모두 포함함을 보인다.

## Quasi-projective variety의 정의

Projective space의 열린부분집합은 자연스러운 기하적 대상이다. 예를 들어, $$\mathbb{P}^2$$에서 직선 $$\x_0=0$$을 제거한 여집합은 projective variety가 아니지만, 여전히 다항식으로 정의되는 대상이며, 심지어 affine variety이기도 하다. 

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Projective variety $$Y \subseteq \mathbb{P}^n$$의 열린부분집합 $$X \subseteq Y$$를 *quasi-projective variety<sub>준사영다양체</sub>*라 부른다.

</div>

즉, quasi-projective variety는 projective variety $$Y$$와 그 속의 닫힌집합 $$Z$$에 대해 $$X = Y \setminus Z$$의 꼴로 쓰여지는 집합이다.

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins> 위에서 살펴봤듯, 각 $$U_i \cong \mathbb{A}^n$$은 $$\mathbb{P}^n$$의 열린부분집합이므로 quasi-projective variety이다. 따라서 모든 affine variety는 quasi-projective variety이다. 또 임의의 projective variety는 당연히 quasi-projective variety이다. 

</div>

## Zariski 위상

Quasi-projective variety $$X \subseteq Y \subseteq \mathbb{P}^n$$에는 $$Y$$로부터 물려받는 subspace topology가 존재한다. 

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> Quasi-projective variety $$X$$의 *Zariski topology*은 projective variety $$Y$$의 위상을 $$X$$로 제한한 것이다. 즉, $$X$$의 닫힌집합들은 projective variety $$Z\subset Y\subset\mathbb{P}^n$$에 대하여 $$X \cap Z$$의 꼴이다. 

</div>

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> Zariski topology는 실제로 위상이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

[§사영다양체, ⁋명제 4](/ko/math/algebraic_geometry/projective_varieties#prop4)로부터 자명하다. 

</details>

## Quasi-projective variety 사이의 사상

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> Quasi-projective variety $$X \subseteq \mathbb{P}^n$$과 $$Y \subseteq \mathbb{P}^m$$ 사이의 *morphism<sub>사상</sub>* $$\varphi: X \to Y$$는 각 점 $$p \in X$$에 대해 다음을 만족하는 함수이다:

$$p$$의 적당한 열린근방 $$U \subseteq X$$와 homogeneous polynomials $$F_0, \ldots, F_m$$ of the same degree가 존재하여

$$\varphi(p) = [F_0(p) : \cdots : F_m(p)]$$

이고, 모든 $$p \in U$$에 대해 $$F_i(p)$$들이 동시에 $$0$$이 아니다.

</div>

이 정의는 국소적으로 projective variety의 morphism과 같은 꼴이라는 것을 의미한다. 

<div class="example" markdown="1">

<ins id="ex6">**예시 6**</ins> Projective variety와 affine variety들을 엮어주는 함수들이 새로운 것들이다. 가령 quotient map

$$\mathbb{A}^{n+1}\setminus\{(0,\ldots, 0)\}\rightarrow \mathbb{P}^n;\qquad (x_0,\ldots, x_n)\mapsto [x_0:\cdots:x_n]$$

은 quasi-projective variety들 사이의 morphism이다. 

</div>

또, 다음 정의도 자명하다. 

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> Morphism $$\varphi: X \to Y$$가 *isomorphism<sub>동형사상</sub>*이라는 것은 역함수 $$\psi: Y \to X$$가 존재하여 $$\psi$$도 morphism인 것이다.

</div>

## 열린집합과 닫힌집합의 Quasi-projective variety 구조

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> Quasi-projective variety $$X$$의 열린부분집합과 닫힌부분집합은 모두 quasi-projective variety이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$X$$가 사영다양체 $$Y$$의 열린부분집합이라 하자.

- $$X$$의 열린부분집합 $$U$$는 $$Y$$의 열린부분집합이므로 quasi-projective variety이다.
- $$X$$의 닫힌부분집합 $$Z = X \cap W$$ ($$W$$는 사영다양체)는 $$Y \cap W$$의 열린부분집합이므로 quasi-projective variety이다.

</details>

## 왜 Quasi-projective variety인가?

Quasi-projective variety라는 범주가 자연스러운 이유는 **국소적으로 affine variety처럼 다룰 수 있기 때문**이다. [§사영다양체, 명제 11](/ko/math/algebraic_geometry/projective_varieties#prop11)에서 보았듯, 사영다양체 $$Y$$의 각 점은 standard affine open set $$U_i \cong \mathbb{A}^n$$ 중 하나에 속한다. 따라서 quasi-projective variety $$X = Y \setminus Z$$의 각 점 $$p$$에 대해서도 $$p \in X \cap U_i$$인 $$i$$가 존재하고, $$X \cap U_i$$는 affine variety의 열린부분집합이다.

이는 미분다양체(manifold)에서 각 점의 열린근방이 $$\mathbb{R}^n$$과 동형인 chart를 갖는 것과 비슷하다. Quasi-projective variety의 morphism 정의에서 "각 점 $$p$$의 열린근방 $$U$$"를 잡는 것은 바로 이 chart를 선택하는 것에 해당한다.

즉, quasi-projective variety 범주는:
- 아핀다양체를 포함하고
- 사영다양체를 포함하면서
- 동시에 **국소적으로는 항상 affine setting에서 작업할 수 있는**

가장 자연스러운 범주이다. 다음 절 [§정칙사상](/ko/math/algebraic_geometry/regular_maps)에서 우리는 이 점을 더 자세히 탐구할 것이다.

---

**참고문헌**

**[Har]** J. Harris, *Algebraic Geometry: A First Course*, Springer, 1992.  
**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.
