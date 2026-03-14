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
last_modified_at: 2026-03-13
weight: 7

---

미분기하학에서 접공간은 곡면의 국소적 구조를 이해하는 핵심 도구이다. 곡면 위의 한 점에서 접평면을 생각하면 그 점 근처에서 곡면이 어떻게 생겼는지 직관을 얻을 수 있다. 대수기하학에서도 접공간의 개념을 정의할 수 있으며, 이를 통해 다양체의 "매끄러움"을 판별할 수 있다. 이 절에서 우리는 접공간을 여러 관점에서 정의하고, 매끄러운 점과 특이점을 구별하며, 마지막으로 특이점에서 접공간보다 더 정확한 정보를 주는 접원뿔을 소개한다.

## 접공간의 정의

아핀다양체 $$X = V(f_1, \ldots, f_k) \subseteq \mathbb{A}^n$$의 점 $$p$$에서, 우리는 $$X$$를 $$p$$ 근처에서 선형화하여 접공간을 정의할 수 있다. 미분기하학에서처럼, 각 defining equation $$f_i = 0$$을 $$p$$에서 선형화하면 $$f_i$$의 differential $$df_i$$를 얻고, 이들의 공통 kernel이 접공간이 된다.

<div class="definition" markdown="1">

<ins id="def1">\ast\ast정의 1\ast\ast</ins> 아핀다양체 $$X = V(f_1, \ldots, f_k) \subseteq \mathbb{A}^n$$의 점 $$p = (p_1, \ldots, p_n)$$에서의 *tangent space<sub>접공간</sub>* $$T_p X$$를

$$T_p X = \{v \in \mathbb{K}^n \mid (df_i)_p(v) = 0 \text{ for all } i\}$$

으로 정의한다. 여기서 $$(df_i)_p$$는 $$f_i$$의 $$p$$에서의 differential로,

$$(df_i)_p(v) = \sum_{j=1}^n \frac{\partial f_i}{\partial x_j}(p) v_j$$

이다.

</div>

기하학적으로, $$T_p X$$는 $$p$$를 지나면서 $$X$$에 "접하는" 모든 직선들의 모임이다. 점 $$p + \epsilon v$$가 $$X$$ 위에 있다면 ($$\epsilon$$이 매우 작을 때), $$v \in T_p X$$이다. 이는 $$f_i(p + \epsilon v) \approx f_i(p) + \epsilon (df_i)_p(v) = \epsilon (df_i)_p(v)$$이고, $$f_i(p) = 0$$이므로 $$(df_i)_p(v) = 0$$이어야 하기 때문이다.

<div class="proposition" markdown="1">

<ins id="prop2">\ast\ast명제 2\ast\ast</ins> $$T_p X$$는 $$\mathbb{K}$$-벡터공간이며, 그 차원은 $$n - \text{rank}(J_p)$$이다. 여기서 $$J_p$$는 $$k \times n$$ Jacobian matrix

$$J_p = \left(\frac{\partial f_i}{\partial x_j}(p)\right)_{1 \le i \le k, 1 \le j \le n}$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

각 $$(df_i)_p: \mathbb{K}^n \to \mathbb{K}$$는 linear functional이다. $$T_p X$$는 이들의 kernel들의 교집합이므로 $$\mathbb{K}^n$$의 부분공간이다. Jacobian matrix $$J_p$$의 행들은 이 linear functional들의 좌표표현이므로,

$$T_p X = \ker(J_p) = \{v \in \mathbb{K}^n \mid J_p v = 0\}$$

이다. Rank-nullity theorem에 의해 $$\dim T_p X = n - \text{rank}(J_p)$$이다.

</details>

## Coordinate Ring을 통한 정의

접공간을 coordinate ring의 언어로 표현할 수 있다. 이 정의는 아핀다양체에 국한되지 않고, 임의의 준사영다양체에 적용할 수 있다는 장점이 있다.

<div class="proposition" markdown="1">

<ins id="prop3">\ast\ast명제 3\ast\ast</ins> 점 $$p \in X$$에서 $$T_p X \cong (\mathfrak{m}_p / \mathfrak{m}_p^2)^\ast$$이다. 여기서 $$\mathfrak{m}_p = \{f \in \mathbb{K}[X] \mid f(p) = 0\}$$는 $$\mathbb{K}[X]$$의 maximal ideal이고, $$(-)^\ast$$는 $$\mathbb{K}$$-dual space를 의미한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$\mathfrak{m}_p$$는 $$p$$에서 vanish하는 regular function들의 ideal이다. $$\mathfrak{m}_p / \mathfrak{m}_p^2$$의 원소는 $$p$$에서의 "first-order infinitesimal deformation"으로 생각할 수 있다. 구체적으로, $$f \in \mathfrak{m}_p$$를 $$f = \sum_i a_i (x_i - p_i) + \text{higher order terms}$$로 전개하면, $$f \mod \mathfrak{m}_p^2$$는 linear term $$\sum_i a_i (x_i - p_i)$$만을 기억한다.

이제 linear map $$\varphi: T_p X \to (\mathfrak{m}_p / \mathfrak{m}_p^2)^\ast$$를 다음과 같이 정의하자. $$v \in T_p X$$에 대해, $$\varphi(v)(\bar{f}) = (df)_p(v)$$이다. 여기서 $$\bar{f}$$는 $$f \mod \mathfrak{m}_p^2$$이다.

- $$\varphi$$가 well-defined: $$f \in \mathfrak{m}_p^2$$이면 $$f$$의 linear term이 없으므로 $$(df)_p = 0$$이다.
- $$\varphi$$가 injective: $$(df)_p(v) = 0$$ for all $$f \in \mathfrak{m}_p$$이면 $$v \in T_p X$$이다.
- $$\varphi$$가 surjective: $$(\mathfrak{m}_p / \mathfrak{m}_p^2)^\ast$$의 임의의 원소는 linear functional $$\sum_i c_i (x_i - p_i) \mapsto \sum_i c_i a_i$$의 꼴이고, 이는 $$v = (a_1, \ldots, a_n)$$에 의해 realize된다.

따라서 $$T_p X \cong (\mathfrak{m}_p / \mathfrak{m}_p^2)^\ast$$이다.

</details>

이 정의는 다음과 같이 해석할 수 있다. $$\mathfrak{m}_p / \mathfrak{m}_p^2$$는 $$p$$에서의 "first-order data"를 담고 있고, 그 dual space는 이 data를 $$\mathbb{K}$$로 보내는 linear map들, 즉 "방향 미분"들의 공간이다. Tangent vector는 바로 이 방향 미분 연산자에 해당한다.

## 매끄러운 점과 특이점

접공간의 차원은 항상 다양체의 차원 이상이다. 특이점에서는 접공간이 "너무 커서" 다양체의 차원보다 크다.

<div class="proposition" markdown="1">

<ins id="prop4">\ast\ast명제 4\ast\ast</ins> 기약 다양체 $$X$$의 임의의 점 $$p$$에 대해 $$\dim T_p X \ge \dim X$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$X = V(f_1, \ldots, f_k) \subseteq \mathbb{A}^n$$이라 하자. $$X$$가 기역이고 $$\dim X = d$$라면, $$X$$의 generic point $$p$$에서 Jacobian $$J_p$$의 rank는 $$n - d$$이다. 이는 $$X$$의 coordinate ring $$\mathbb{K}[X]$$가 $$d$$차원이고, generic point에서 $$d$$개의 "자유로운 방향"이 존재함을 의미한다.

다른 점에서는 추가적인 constraint가 있을 수 있어 Jacobian의 rank가 감소할 수 있다. Rank가 감소하면 $$\dim T_p X = n - \text{rank}(J_p)$$가 증가한다. 따라서 모든 점 $$p$$에서 $$\dim T_p X \ge d = \dim X$$이다.

</details>

<div class="definition" markdown="1">

<ins id="def5">\ast\ast정의 5\ast\ast</ins> 점 $$p \in X$$가 *smooth point<sub>매끄러운 점</sub>* (또는 *nonsingular point*)라는 것은 $$\dim T_p X = \dim X$$인 것이다. 그렇지 않으면 (즉, $$\dim T_p X > \dim X$$이면) *singular point<sub>특이점</sub>*이라 부른다.

</div>

기하학적으로, smooth point에서는 접공간이 다양체의 "진짜 차원"과 일치한다. 즉, 다양체가 그 점 근처에서 "예상대로" 생겼다는 것이다. 반면 singular point에서는 접공간이 너무 커서, 다양체가 그 점에서 "특이한" 구조를 갖는다.

<div class="example" markdown="1">

<ins id="ex6">\ast\ast예시 6\ast\ast</ins> Smooth point와 singular point의 기본 예시들이다.

1. $$\mathbb{A}^n$$의 모든 점은 smooth point이다. $$\mathbb{A}^n$$은 defining equation이 없으므로 $$T_p \mathbb{A}^n = \mathbb{K}^n$$이고, $$\dim T_p \mathbb{A}^n = n = \dim \mathbb{A}^n$$이다.
2. Parabola $$V(y - x^2)$$의 모든 점은 smooth point이다. $$f = y - x^2$$에 대해 $$\nabla f = (-2x, 1)$$이고, 이는 모든 점에서 nonzero이다. 따라서 $$\dim T_p X = 2 - 1 = 1 = \dim X$$이다.
3. Cusp $$V(y^2 - x^3)$$의 원점은 singular point이다. $$f = y^2 - x^3$$에 대해 $$\nabla f = (-3x^2, 2y)$$이고, 원점에서 $$\nabla f(0,0) = (0, 0)$$이다. 따라서 $$T_0 X = \mathbb{K}^2$$이고 $$\dim T_0 X = 2 > 1 = \dim X$$이다.

</div>

<div class="example" markdown="1">

<ins id="ex7">\ast\ast예시 7\ast\ast</ins> \ast\astCusp\ast\ast: $$X = V(y^2 - x^3) \subset \mathbb{A}^2$$를 더 자세히 살펴보자. 이 곡선은 원점에서 "뾰족하게" 끝난다. 원점에서의 Jacobian은

$$J_0 = \begin{pmatrix} -3x^2 & 2y \end{pmatrix}_{(0,0)} = \begin{pmatrix} 0 & 0 \end{pmatrix}$$

이므로 $$\dim T_0 X = 2 - 0 = 2 > 1 = \dim X$$이다. 기하학적으로, 접공간이 2차원이라는 것은 모든 방향이 "접한다"는 것을 의미하며, 이는 곡선이 원점에서 너무 뾰족해서 어떤 방향으로도 접선을 정의할 수 없음을 나타낸다.

</div>

<div class="example" markdown="1">

<ins id="ex8">\ast\ast예시 8\ast\ast</ins> \ast\astNode\ast\ast: $$X = V(y^2 - x^2(x+1)) \subset \mathbb{A}^2$$를 생각하자. 이 곡선은 원점에서 두 갈래로 갈라진다. 원점에서의 Jacobian은

$$J_0 = \begin{pmatrix} -2x - 3x^2 & 2y \end{pmatrix}_{(0,0)} = \begin{pmatrix} 0 & 0 \end{pmatrix}$$

이므로 원점은 singular point이다. 기하학적으로, 접공간이 2차원이라는 것은 두 갈래의 접선 방향이 모두 포함된다는 것을 의미한다. 구체적으로, $$y^2 - x^2(x+1) \approx y^2 - x^2 = (y-x)(y+x)$$이므로, 원점 근처에서 곡선은 $$y = x$$와 $$y = -x$$ 두 직선의 합집합처럼 보인다.

</div>

## Jacobian Criterion

Jacobian criterion은 smooth point를 효율적으로 판별하는 방법이다.

<div class="proposition" markdown="1">

<ins id="prop9">\ast\ast명제 9\ast\ast</ins> (Jacobian Criterion) $$X = V(f_1, \ldots, f_k) \subseteq \mathbb{A}^n$$이 기약 다양체이고 $$p \in X$$라 하자. 그럼 $$p$$가 smooth point일 필요충분조건은 Jacobian matrix $$J_p$$의 rank가 $$n - \dim X$$인 것이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

[명제 2](#prop2)에서 $$\dim T_p X = n - \text{rank}(J_p)$$임을 보였다. [정의 5](#def5)에서 $$p$$가 smooth point라는 것은 $$\dim T_p X = \dim X$$인 것이다. 따라서 $$p$$가 smooth point일 필요충분조건은

$$n - \text{rank}(J_p) = \dim X$$

즉, $$\text{rank}(J_p) = n - \dim X$$인 것이다.

</details>

이 정리는 smooth point를 판별하는 실용적인 방법을 제공한다. $$X = V(f_1, \ldots, f_k)$$이고 $$\dim X = d$$라면, $$p$$가 smooth point이려면 $$J_p$$의 rank가 정확히 $$n - d$$이어야 한다. 이는 $$k$$개의 defining equation 중 정확히 $$n - d$$개가 $$p$$에서 "독립적"이어야 함을 의미한다.

<div class="remark" markdown="1">

Jacobian criterion을 적용하려면 $$X$$의 차원을 미리 알아야 한다. 차원을 모르는 경우, $$J_p$$의 rank의 최댓값을 $$r$$이라 하면 $$\dim X \ge n - r$$이고, $$p$$가 smooth point이면 $$\dim X = n - r$$이다.

</div>

## 매끄러운 점들의 존재

기약 다양체는 "대부분의 점에서" 매끄럽다. 이는 대수기하학의 기본 정리 중 하나이다.

<div class="proposition" markdown="1">

<ins id="prop10">\ast\ast명제 10\ast\ast</ins> 기역 다양체 $$X$$의 smooth points들의 집합 $$X_{\text{sm}}$$은 $$X$$의 dense open subset이다. 특히, $$X_{\text{sm}} \ne \emptyset$$이다.

</div>

이 정리의 증명은 Jacobian criterion을 사용한다. $$X = V(f_1, \ldots, f_k)$$이고 $$\dim X = d$$라면, smooth points는

$$X_{\text{sm}} = \{p \in X \mid \text{rank}(J_p) = n - d\}$$

이다. Rank $$\ge n - d$$인 조건은 minors의 non-vanishing으로 표현되므로 열린조건이고, generic point에서 rank가 $$n - d$$에 도달하므로 $$X_{\text{sm}}$$은 nonempty dense open subset이다.

<div class="definition" markdown="1">

<ins id="def11">\ast\ast정의 11\ast\ast</ins> 다양체 $$X$$가 *smooth* (또는 *nonsingular*)라는 것은 모든 점이 smooth point인 것이다. 즉, $$X_{\text{sm}} = X$$이다. 그렇지 않으면 (즉, singular point가 존재하면) *singular*라 부른다.

</div>

<div class="example" markdown="1">

<ins id="ex12">\ast\ast예시 12\ast\ast</ins> Smooth variety와 singular variety의 예시들이다.

1. $$\mathbb{A}^n$$과 $$\mathbb{P}^n$$은 smooth하다. 이들의 모든 점에서 접공간의 차원이 $$n$$으로 일치한다.
2. Parabola $$V(y - x^2)$$는 smooth하다. 모든 점에서 $$\nabla(y - x^2) \ne 0$$이다.
3. Cusp $$V(y^2 - x^3)$$은 singular이다. 원점이 singular point이다.
4. Node $$V(y^2 - x^2(x+1))$$은 singular이다. 원점이 singular point이다.
5. Smooth projective curve는 모든 점에서 매끄러운 1차원 사영다양체이다. 예를 들어 smooth plane curve $$V(F) \subset \mathbb{P}^2$$ ($$F$$가 기역 동차다항식)는 모든 점 $$p$$에서 $$\nabla F(p) \ne 0$$이면 smooth하다.

</div>

## 접원뿔

Singular point에서는 tangent space가 너무 커서 다양체의 국소적 구조를 정확히 반영하지 못한다. 이 경우 *tangent cone*이 더 정확한 정보를 제공한다.

<div class="definition" markdown="1">

<ins id="def13">\ast\ast정의 13\ast\ast</ins> 점 $$p \in X$$에서의 *tangent cone* $$TC_p X$$는 $$p$$에서의 initial ideal로 정의되는 cone이다. 구체적으로, $$X = V(f_1, \ldots, f_k)$$이고 각 $$f_i$$를 $$p$$에서 전개하면

$$f_i = f_i^{(d_i)} + \text{higher order terms}$$

이고, 여기서 $$f_i^{(d_i)}$$는 $$f_i$$의 lowest degree homogeneous part (initial form)이다. 그럼

$$TC_p X = V(f_1^{(d_1)}, \ldots, f_k^{(d_k)})$$

이다.

</div>

Tangent cone은 다양체를 점 $$p$$에서 "확대"하여 가장 낮은 차수의 항만 남긴 것이다. Smooth point에서는 tangent cone이 tangent space와 같다. Singular point에서는 tangent cone이 tangent space보다 더 정확한 정보를 준다.

<div class="example" markdown="1">

<ins id="ex14">\ast\ast예시 14\ast\ast</ins> \ast\astCusp의 tangent cone\ast\ast: $$X = V(y^2 - x^3)$$의 원점에서, $$f = y^2 - x^3$$의 lowest degree term은 $$y^2$$이다. 따라서

$$TC_0 X = V(y^2)$$

이다. 이는 $$y = 0$$ 직선을 "두 번" count한 것이며, cusp가 $$x$$-축 방향으로 뾰족하게 끝남을 보여준다. 비교하면, tangent space $$T_0 X = \mathbb{K}^2$$는 모든 방향을 포함하여 너무 크다.

</div>

<div class="example" markdown="1">

<ins id="ex15">\ast\ast예시 15\ast\ast</ins> \ast\astNode의 tangent cone\ast\ast: $$X = V(y^2 - x^2(x+1))$$의 원점에서, $$f = y^2 - x^2(x+1)$$의 lowest degree term은 $$y^2 - x^2 = (y-x)(y+x)$$이다. 따라서

$$TC_0 X = V((y-x)(y+x)) = V(y-x) \cup V(y+x)$$

이다. 이는 node에서 곡선이 두 직선 $$y = x$$와 $$y = -x$$의 방향으로 갈라짐을 정확히 보여준다.

</div>

---

\ast\ast참고문헌\ast\ast

\ast\ast[Har]\ast\ast J. Harris, *Algebraic Geometry: A First Course*, Springer, 1992.  
\ast\ast[Sha]\ast\ast I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.
