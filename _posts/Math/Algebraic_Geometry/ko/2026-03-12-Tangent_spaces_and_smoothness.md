---
title: "접공간과 매끄러움"
excerpt: "Tangent spaces and smoothness of algebraic varieties"

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/tangent_spaces_and_smoothness
sidebar: 
    nav: "algebraic_geometry-ko"

header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Tangent_Spaces.png
    overlay_filter: 0.5

date: 2026-03-12
last_modified_at: 2026-03-12
weight: 7

---

미분기하학에서 접공간은 곡면의 국소적 구조를 이해하는 핵심 도구이다. 대수기하학에서도 접공간의 개념을 정의할 수 있으며, 이를 통해 다양체의 "매끄러움"을 판별할 수 있다.

## 접공간의 정의

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 아핀다양체 $$X = V(f_1, \ldots, f_k) \subseteq \mathbb{A}^n$$의 점 $$p$$에서의 *tangent space<sub>접공간</sub>* $$T_p X$$를

$$$T_p X = \{v \in \mathbb{K}^n \mid (df_i)_p(v) = 0 \text{ for all } i\}$$$

으로 정의한다. 여기서 $$(df_i)_p$$는 $$f_i$$의 $$p$$에서의 differential이다.

</div>

구체적으로, $$(df_i)_p(v) = \sum_{j=1}^n \frac{\partial f_i}{\partial x_j}(p) v_j$$이다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> $$T_p X$$는 $$\mathbb{K}$$-벡터공간이며, 그 차원은 $$n - \text{rank}(J_p)$$이다. 여기서 $$J_p$$는 Jacobian matrix $$\left(\frac{\partial f_i}{\partial \x_j}(p)\right)$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$(df_i)_p$$는 linear functional이므로 $$T_p X$$는 이들의 kernel의 교집합이다. 따라서 vector space이며, dimension은 rank-nullity theorem에 의해 $$n - \text{rank}(J_p)$$이다.

</details>

## Coordinate Ring을 통한 정의

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> 점 $$p \in X$$에서 $$T_p X \cong (\mathfrak{m}_p / \mathfrak{m}_p^2)^\ast$$이다. 여기서 $$\mathfrak{m}_p = \{f \in \mathbb{K}[X] \mid f(p) = 0\}$$는 maximal ideal이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$\mathfrak{m}_p$$는 $$p$$에서 vanish하는 함수들의 ideal이다. $$\mathfrak{m}_p / \mathfrak{m}_p^2$$의 원소는 $$p$$에서의 first-order infinitesimal deformation이다. 이들의 dual은 tangent vector들이다.

</details>

이 정의는 아핀다양체에 국한되지 않고, 임의의 준사영다양체에 적용할 수 있다.

## 매끄러운 점과 특이점

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> 기약 다양체 $$X$$의 임의의 점 $$p$$에 대해 $$\dim T_p X \ge \dim X$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$X$$의 generic point에서 $$\dim T_p X = \dim X$$이다. 다른 점에서는 더 많은 constraint가 있을 수 있으므로 dimension이 증가할 수 있다.

</details>

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> 점 $$p \in X$$가 *smooth point<sub>매끄러운 점</sub>* (또는 *nonsingular point*)라는 것은 $$\dim T_p X = \dim X$$인 것이다. 그렇지 않으면 *singular point<sub>특이점</sub>*이라 부른다.

</div>

<div class="example" markdown="1">

<ins id="ex6">**예시 6**</ins>

1. $$\mathbb{A}^n$$의 모든 점은 smooth point이다. ($$T_p \mathbb{A}^n = \mathbb{K}^n$$)
2. $$V(\y - \x^2)$$의 모든 점은 smooth point이다.
3. $$V(\y^2 - \x^3)$$의 원점은 singular point이다. ($$T_0 X = \mathbb{K}^2$$, but $$\dim X = 1$$)

</div>

<div class="example" markdown="1">

<ins id="ex7">**예시 7**</ins> **Cusp**: $$X = V(\y^2 - \x^3) \subset \mathbb{A}^2$$의 원점에서

$$$J_0 = \begin{pmatrix} -3\x^2 & 2\y \end{pmatrix}_{(0,0)} = \begin{pmatrix} 0 & 0 \end{pmatrix}$$$

이므로 $$\dim T_0 X = 2 - 0 = 2 > 1 = \dim X$$이다. 따라서 원점은 singular point이다.

</div>

<div class="example" markdown="1">

<ins id="ex8">**예시 8**</ins> **Node**: $$X = V(\y^2 - \x^2(\x+1)) \subset \mathbb{A}^2$$의 원점에서

$$$J_0 = \begin{pmatrix} -2\x - 3\x^2 & 2\y \end{pmatrix}_{(0,0)} = \begin{pmatrix} 0 & 0 \end{pmatrix}$$$

이므로 원점은 singular point이다. 이 점에서 곡선은 두 갈래로 갈라진다.

</div>

## Jacobian Criterion

<div class="theorem" markdown="1">

<ins id="thm9">**정리 9**</ins> (Jacobian Criterion) $$X = V(f_1, \ldots, f_k) \subseteq \mathbb{A}^n$$이 기약 다양체이고 $$p \in X$$라 하자. 그럼 $$p$$가 smooth point일 필요충분조건은 Jacobian matrix $$J_p$$의 rank가 $$n - \dim X$$인 것이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$\dim T_p X = n - \text{rank}(J_p)$$이고, $$p$$가 smooth point라는 것은 $$\dim T_p X = \dim X$$인 것이다. 따라서 $$\text{rank}(J_p) = n - \dim X$$이다.

</details>

## Smooth Points의 존재

<div class="theorem" markdown="1">

<ins id="thm10">**정리 10**</ins> 기역 다양체 $$X$$의 smooth points들의 집합은 $$X$$의 dense open subset이다.

</div>

이 정리에 의해, 기역 다양체는 "대부분의 점에서" 매끄럽다.

<div class="definition" markdown="1">

<ins id="def11">**정의 11**</ins> 다양체 $$X$$가 *smooth* (또는 *nonsingular*)라는 것은 모든 점이 smooth point인 것이다.

</div>

<div class="example" markdown="1">

<ins id="ex12">**예시 12**</ins>

1. $$\mathbb{A}^n$$과 $$\mathbb{P}^n$$은 smooth하다.
2. $$V(\y - \x^2)$$는 smooth하다.
3. $$V(\y^2 - \x^3)$$은 singular이다. (원점이 singular point)
4. Smooth projective curve는 모든 점에서 매끄러운 사영곡선이다.

</div>

## Tangent Cone

Singular point에서는 tangent space가 너무 크다. 대신 *tangent cone*을 정의하면 더 정확한 정보를 얻을 수 있다.

<div class="definition" markdown="1">

<ins id="def13">**정의 13**</ins> 점 $$p \in X$$에서의 *tangent cone* $$TC_p X$$는 $$p$$에서의 initial ideal로 정의되는 cone이다.

</div>

<div class="example" markdown="1">

<ins id="ex14">**예시 14**</ins> $$X = V(\y^2 - \x^3)$$의 원점에서, tangent cone은 $$V(\y^2)$$이다. 이는 $$\y = 0$$ 직선 (두 번)이며, cusp의 방향을 보여준다.

</div>

---

**참고문헌**

**[Har]** J. Harris, *Algebraic Geometry: A First Course*, Springer, 1992.  
**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.
