---
title: "벡터장"
description: "공간의 각 점에 벡터를 대응시키는 벡터장을 도입하고, 기울기장과 보존장·퍼텐셜을 정의한다. 발산과 회전을 정의하고 그 의미를 살피며, curl(grad)=0·div(curl)=0과 보존장의 무회전성을 보인다."
excerpt: "벡터장과 기울기장, 보존장과 퍼텐셜, 발산과 회전, 미분 항등식"

categories: [Math / Calculus]
permalink: /ko/math/calculus/vector_fields
sidebar: 
    nav: "calculus-ko"

date: 2026-06-02
weight: 16
published: false
---

스칼라장이 공간의 각 점에 수 하나를 주는 함수였다면, 벡터장은 각 점에 벡터 하나를 준다. 유체의 속도, 힘, 전기장처럼 방향과 크기를 함께 갖는 양이 벡터장이고, 이들을 미분하는 발산과 회전은 흐름이 한 점에서 솟거나 휘도는 정도를 잰다. 이 언어가 뒤이은 선적분·면적분과 적분정리의 토대가 된다.

## 벡터장

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 영역 $$D \subseteq \mathbb{R}^n$$의 각 점 $$x$$에 벡터 $$F(x) \in \mathbb{R}^n$$을 대응시키는 함수 $$F\colon D \to \mathbb{R}^n$$을 *벡터장<sub>vector field</sub>*이라 한다. 평면에서는 $$F(x,y) = (P(x,y), Q(x,y))$$, 공간에서는 $$F(x,y,z) = (P, Q, R)$$로 적고, 각 성분 $$P, Q, R$$가 $$C^1$$이면 $$F$$를 $$C^1$$ 벡터장이라 한다.

</div>

벡터장은 각 점에 그 점에서 출발하는 화살표를 꽂은 그림으로 떠올린다. 유체의 흐름이라면 각 점에서의 유속, 중력장이라면 각 점에 놓인 시험질량이 받는 힘이다. 스칼라함수의 기울기는 자연스러운 벡터장을 낳는다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> $$C^1$$ 스칼라함수 $$f$$의 기울기 $$\nabla f = (\partial f/\partial x_1, \ldots, \partial f/\partial x_n)$$로 주어지는 벡터장을 $$f$$의 *기울기장<sub>gradient field</sub>*이라 한다. 어떤 스칼라함수 $$f$$에 대해 $$F = \nabla f$$로 쓸 수 있는 벡터장 $$F$$를 *보존장<sub>conservative field</sub>*이라 하고, 그 $$f$$를 $$F$$의 *퍼텐셜<sub>potential</sub>*이라 한다.

</div>

기울기장은 각 점에서 $$f$$가 가장 가파르게 증가하는 방향을 가리킨다 ([§다변수함수와 편미분, ⁋명제 6](/ko/math/calculus/partial_derivatives#prop6)). 등위면 $$f = c$$에 수직인 이 벡터장이 보존장의 전형이며, 중력장과 정전기장이 모두 퍼텐셜을 갖는 보존장이다. 모든 벡터장이 보존장은 아니므로, 주어진 $$F$$가 어떤 $$f$$의 기울기인지를 판정하는 것이 중심 문제가 된다. 그 판정에 쓰이는 두 미분연산을 도입한다.

## 발산과 회전

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> $$C^1$$ 벡터장 $$F = (P, Q, R)$$의 *발산<sub>divergence</sub>*은 스칼라장

$$\operatorname{div} F = \nabla \cdot F = \frac{\partial P}{\partial x} + \frac{\partial Q}{\partial y} + \frac{\partial R}{\partial z}$$

이고, *회전<sub>curl</sub>*은 벡터장

$$\operatorname{curl} F = \nabla \times F = \left(\frac{\partial R}{\partial y} - \frac{\partial Q}{\partial z},\ \frac{\partial P}{\partial z} - \frac{\partial R}{\partial x},\ \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\right)$$

이다. 형식적으로 $$\nabla = (\partial_x, \partial_y, \partial_z)$$를 벡터로 보아 점곱·교차곱을 취한 것이다.

</div>

발산은 한 점에서 벡터장이 솟아나는(또는 빨려드는) 정도, 곧 단위부피당 흘러나가는 양을 잰다. $$\operatorname{div} F > 0$$인 점은 흐름의 원천, $$< 0$$인 점은 흡입구이며, 발산정리에서 이 직관이 엄밀해진다. 회전은 벡터장이 한 점 둘레로 휘도는 정도와 그 축을 가리키며, 작은 바람개비를 흐름에 놓았을 때 도는 각속도에 대응한다. 평면벡터장 $$F = (P, Q)$$는 회전을 스칼라 $$\partial Q/\partial x - \partial P/\partial y$$로 (공간벡터장의 회전에서 $$z$$성분만 남긴 것으로) 본다.

<div class="example" markdown="1">

<ins id="ex4">**예시 4 (지름장과 회전장)**</ins> 지름 방향으로 뻗는 $$F(x,y,z) = (x, y, z)$$는 $$\operatorname{div} F = 1 + 1 + 1 = 3$$으로 어디서나 양이고 (모든 점이 원천), $$\operatorname{curl} F = 0$$이다. 실제로 $$F = \nabla\bigl((x^2+y^2+z^2)/2\bigr)$$인 보존장이다. 반대로 $$z$$축 둘레로 도는 $$G(x,y,z) = (-y, x, 0)$$은 $$\operatorname{div} G = 0$$(솟음 없는 순환)이지만 $$\operatorname{curl} G = (0, 0, 2)$$로 $$z$$축 방향으로 일정하게 휘돈다.

</div>

## 미분 항등식

발산과 회전은 두 가지 항등식으로 기울기와 얽힌다. 둘 다 혼합편미분이 순서에 무관하다는 [§다변수함수와 편미분, ⁋정리 5](/ko/math/calculus/partial_derivatives#thm5)에서 나온다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> $$C^2$$ 함수 $$f$$와 $$C^2$$ 벡터장 $$F$$에 대해

$$\operatorname{curl}(\nabla f) = 0, \qquad \operatorname{div}(\operatorname{curl} F) = 0$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$\nabla f = (f_x, f_y, f_z)$$의 회전의 첫 성분은 $$\partial_y f_z - \partial_z f_y = f_{zy} - f_{yz}$$인데 클레로 정리로 $$0$$이고, 나머지 두 성분도 같은 이유로 $$0$$이다. 또 $$\operatorname{curl} F = (R_y - Q_z,\ P_z - R_x,\ Q_x - P_y)$$의 발산은

$$\partial_x(R_y - Q_z) + \partial_y(P_z - R_x) + \partial_z(Q_x - P_y) = (R_{yx} - R_{xy}) + (P_{zy} - P_{yz}) + (Q_{xz} - Q_{zx})$$

로 묶이고, 각 괄호가 클레로 정리로 $$0$$이다.

</details>

첫 항등식은 보존장 판정의 필요조건을 준다. $$F = \nabla f$$이면 $$\operatorname{curl} F = \operatorname{curl}(\nabla f) = 0$$이므로, 회전이 $$0$$이 아닌 벡터장은 결코 보존장이 아니다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> 보존장은 무회전이다. 즉 $$C^1$$ 벡터장 $$F$$가 보존장이면 $$\operatorname{curl} F = 0$$이다. 평면벡터장 $$F = (P, Q)$$의 경우 이는 $$\partial Q/\partial x = \partial P/\partial y$$와 같다.

</div>

이 조건은 필요조건일 뿐이며, 그 역(무회전이면 보존)은 정의역의 모양에 달려 있다. 정의역에 "구멍"이 없으면, 곧 단순연결이면 역도 성립하지만, 구멍이 있으면 무회전이면서도 보존장이 아닌 벡터장이 존재한다. 이 미묘한 점은 선적분과 그린 정리에서 정밀하게 다룬다. 한편 필요조건만으로도 퍼텐셜을 실제로 찾는 길이 열린다.

<div class="example" markdown="1">

<ins id="ex7">**예시 7 (퍼텐셜 복원)**</ins> $$F = (2xy,\ x^2 + z,\ y)$$를 보자. 회전을 계산하면

$$\operatorname{curl} F = (\partial_y y - \partial_z(x^2+z),\ \partial_z(2xy) - \partial_x y,\ \partial_x(x^2+z) - \partial_y(2xy)) = (1 - 1,\ 0,\ 2x - 2x) = 0$$

이라 보존장일 가능성이 있다. 퍼텐셜 $$f$$를 찾으려면 $$f_x = 2xy$$에서 $$f = x^2 y + g(y, z)$$, 이를 $$f_y = x^2 + g_y = x^2 + z$$와 맞추면 $$g_y = z$$, 곧 $$g = yz + h(z)$$, 마지막으로 $$f_z = y + h'(z) = y$$에서 $$h' = 0$$이다. 따라서 $$f = x^2 y + yz$$가 퍼텐셜이고 $$F = \nabla f$$임이 확인된다. 무회전이 실제로 보존으로 이어진 것은 $$F$$의 정의역이 구멍 없는 $$\mathbb{R}^3$$ 전체이기 때문이다.

</div>
