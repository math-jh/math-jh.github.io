---
title: "다변수함수와 편미분"
description: "여러 변수의 함수에 대해 편미분과 기울기, 방향도함수를 정의하고, 미분가능성을 일차 근사로 정식화한다. 다변수 연쇄법칙, 혼합편미분의 클레로 정리, 접평면과 극값을 worked 예시로 다룬다."
excerpt: "편미분과 기울기, 미분가능성, 다변수 연쇄법칙, 극값"

categories: [Math / Calculus]
permalink: /ko/math/calculus/partial_derivatives
sidebar: 
    nav: "calculus-ko"

date: 2026-06-02
weight: 16

published: false
---

지금까지의 미분은 한 변수 함수에 관한 것이었다. [§미분과 도함수](/ko/math/calculus/derivatives)에서 미분이 일차 근사 $$f(a+h) \approx f(a) + f'(a)h$$임을 강조했는데, 이 관점이 여러 변수로의 확장에서 핵심이 된다. 이 글에서는 $$\mathbb{R}^n$$에서 $$\mathbb{R}$$로 가는 함수의 미분을 다룬다. 변수가 여럿이면 "변화율"이 방향마다 다르므로, 미분의 개념 자체가 한 변수보다 미묘해진다.

## 편미분과 기울기

가장 단순한 변화율은 한 좌표축 방향으로만 움직일 때의 것이다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 함수 $$f(x_1, \ldots, x_n)$$의 점 $$a$$에서 변수 $$x_i$$에 대한 *편미분<sub>partial derivative</sub>*은 나머지 변수를 고정한 채 $$x_i$$로만 미분한 것이다.

$$\frac{\partial f}{\partial x_i}(a) = \lim_{h\to 0}\frac{f(a + h e_i) - f(a)}{h}$$

여기서 $$e_i$$는 $$i$$번째 표준기저벡터이다. 모든 편미분을 모은 벡터 $$\nabla f(a) = \left(\dfrac{\partial f}{\partial x_1}(a), \ldots, \dfrac{\partial f}{\partial x_n}(a)\right)$$를 $$f$$의 *기울기<sub>gradient</sub>*라 한다.

</div>

편미분의 계산은 한 변수 미분과 똑같되, 나머지 변수를 상수로 취급할 뿐이다.

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins> $$f(x, y) = x^2 y + \sin(xy)$$의 편미분은

$$\frac{\partial f}{\partial x} = 2xy + y\cos(xy), \qquad \frac{\partial f}{\partial y} = x^2 + x\cos(xy)$$

이다. $$\partial f/\partial x$$를 구할 때 $$y$$를 상수로 보고, 둘째 항은 연쇄법칙을 쓴다. 기울기는 $$\nabla f = (2xy + y\cos(xy),\ x^2 + x\cos(xy))$$이다.

</div>

## 미분가능성

편미분은 좌표축 방향의 변화율만 보므로, 함수의 진정한 "일차 근사 가능성"을 담기에는 부족하다. 일차 근사를 직접 요구하는 것이 옳은 미분 개념이다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> $$f$$가 점 $$a$$에서 *미분가능<sub>differentiable</sub>*하다는 것은, 벡터 $$L$$이 존재하여

$$\lim_{h \to 0}\frac{f(a + h) - f(a) - L\cdot h}{\lVert h\rVert} = 0$$

이 성립하는 것이다. 이 경우 $$L = \nabla f(a)$$이고, $$f(a+h) \approx f(a) + \nabla f(a)\cdot h$$가 최선의 일차 근사이다.

</div>

미분가능성은 편미분의 존재보다 강하다. 편미분이 모두 존재해도 미분가능하지 않을 수 있는데, 가령 $$f(x,y) = \dfrac{xy}{x^2+y^2}$$ ($$f(0,0)=0$$) 은 원점에서 두 편미분이 모두 $$0$$이지만, 대각선 $$y = x$$를 따라가면 $$f = 1/2$$로 일정해 연속조차 아니다. 그러나 편미분이 연속이면 이런 병리가 사라진다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> $$f$$의 모든 편미분이 $$a$$ 근방에서 존재하고 $$a$$에서 연속이면 ($$f$$가 $$C^1$$이면), $$f$$는 $$a$$에서 미분가능하다.

</div>

기울기는 함수가 가장 빠르게 증가하는 방향을 가리킨다. 임의의 단위벡터 $$u$$ 방향의 변화율인 *방향도함수*가 $$D_u f(a) = \nabla f(a)\cdot u$$로 주어지므로, 코시–슈바르츠 부등식에 의해 $$\nabla f$$와 같은 방향일 때 최대가 되고 그 값은 $$\lVert\nabla f\rVert$$이다. 미분가능한 점에서 일차 근사 $$z = f(a) + \nabla f(a)\cdot(x - a)$$는 곡면의 *접평면*을 준다. 가령 $$f(x,y) = x^2 + y^2$$의 $$(1, 2)$$에서는 $$\nabla f = (2, 4)$$이고 $$f(1,2) = 5$$이므로 접평면이 $$z = 2x + 4y - 5$$이다.

## 연쇄법칙과 혼합편미분

<div class="proposition" markdown="1">

<ins id="thm5">**정리 5 (다변수 연쇄법칙)**</ins> $$f$$가 미분가능하고 $$x(t) = (x_1(t), \ldots, x_n(t))$$가 미분가능한 곡선이면, 합성 $$t \mapsto f(x(t))$$도 미분가능하고

$$\frac{d}{dt} f(x(t)) = \nabla f(x(t)) \cdot x'(t) = \sum_{i=1}^n \frac{\partial f}{\partial x_i}\,\frac{dx_i}{dt}$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

미분가능성에 의해 $$f(x(t+\Delta t)) - f(x(t)) = \nabla f(x(t))\cdot \Delta x + o(\lVert\Delta x\rVert)$$이고, 곡선의 미분가능성으로 $$\Delta x = x'(t)\Delta t + o(\Delta t)$$이다. 둘을 결합하여 양변을 $$\Delta t$$로 나누고 $$\Delta t \to 0$$을 취하면 오차항이 사라져 공식을 얻는다.

</details>

<div class="example" markdown="1">

<ins id="ex6">**예시 6**</ins> $$z = f(x,y)$$에서 $$x = r\cos\theta$$, $$y = r\sin\theta$$이면 연쇄법칙으로

$$\frac{\partial z}{\partial r} = \frac{\partial f}{\partial x}\cos\theta + \frac{\partial f}{\partial y}\sin\theta$$

이다. 이렇게 한 변수가 여러 변수에 의존할 때 편미분이 사슬처럼 연결되며, 좌표변환에서 거듭 쓰인다.

</div>

이계편미분에 대해서는 미분의 순서가 (적절한 연속성 아래) 문제되지 않는다.

<div class="proposition" markdown="1">

<ins id="thm7">**정리 7 (클레로)**</ins> 두 혼합편미분 $$\dfrac{\partial^2 f}{\partial x\,\partial y}$$와 $$\dfrac{\partial^2 f}{\partial y\,\partial x}$$가 모두 존재하고 한 점 근방에서 연속이면, 그 점에서 둘이 같다.

</div>

## 극값

한 변수에서 극값이 임계점에서 일어났듯, 다변수에서도 미분가능한 함수의 극값은 $$\nabla f = 0$$인 *임계점*에서만 일어난다 (각 편미분이 $$0$$이어야 하므로). 임계점이 극대·극소·안장점 중 어느 것인지는 이계편미분으로 이루어진 헤세 행렬의 부호로 판정한다.

가령 $$f(x,y) = x^2 + y^2 - 2x - 4y$$는 $$\nabla f = (2x - 2,\ 2y - 4) = 0$$에서 임계점 $$(1, 2)$$를 가지며, $$f = (x-1)^2 + (y-2)^2 - 5$$로 완전제곱하면 그 점에서 최솟값 $$-5$$임이 곧장 보인다. 그러나 완전제곱이 늘 가능하지는 않으므로, 일반적으로는 헤세 행렬 $$H = \begin{pmatrix} f_{xx} & f_{xy} \\ f_{yx} & f_{yy}\end{pmatrix}$$의 부호로 판정한다. $$\det H > 0$$이고 $$f_{xx} > 0$$이면 극소, $$\det H > 0$$이고 $$f_{xx} < 0$$이면 극대, $$\det H < 0$$이면 *안장점*이다.

<div class="example" markdown="1">

<ins id="ex8">**예시 8 (안장점)**</ins> $$f(x,y) = x^2 - y^2$$은 $$\nabla f = (2x, -2y) = 0$$에서 임계점 $$(0,0)$$을 가진다. 헤세 행렬은 $$\begin{pmatrix} 2 & 0 \\ 0 & -2\end{pmatrix}$$로 $$\det H = -4 < 0$$이므로 안장점이다. 실제로 $$x$$축을 따라가면 $$f = x^2$$로 극소, $$y$$축을 따라가면 $$f = -y^2$$로 극대라, 방향에 따라 오르내리는 말안장 모양이다.

</div>

제약조건 $$g(x,y) = c$$ 아래에서 $$f$$의 극값을 찾는 문제는 라그랑주 승수법으로 다룬다: 극값점에서 $$\nabla f = \lambda\nabla g$$가 성립하는 $$\lambda$$가 존재하므로, 이 식과 제약식을 연립해 푼다.

## 방향도함수와 기울기

방향도함수가 기울기와 어떻게 맞물리는지를 구체적인 계산으로 풀어 보자. 단위벡터 $$u$$를 따라 움직일 때의 변화율은 정의상 한 변수 함수 $$g(t) = f(a + tu)$$의 $$t = 0$$에서의 도함수인데, 연쇄법칙(정리 5)을 $$x(t) = a + tu$$에 적용하면 $$g'(0) = \nabla f(a)\cdot u$$가 곧바로 나온다.

기울기가 가리키는 방향이 최대 증가 방향이라는 사실은 방향도함수 공식과 코시–슈바르츠 부등식의 직접적 귀결이며, 별도의 명제로 정식화해 둘 만하다.

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9 (최대 경사 방향)**</ins> $$f$$가 $$a$$에서 미분가능하고 $$\nabla f(a) \neq 0$$이면, 단위벡터 방향의 방향도함수 $$D_u f(a)$$는 $$u = \nabla f(a)/\lVert\nabla f(a)\rVert$$일 때 최대가 되고, 그 최댓값은 $$\lVert\nabla f(a)\rVert$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

미분가능성에 의해 임의의 단위벡터 $$u$$에 대해 $$D_u f(a) = \nabla f(a)\cdot u$$이다. 코시–슈바르츠 부등식으로

$$\begin{aligned}
D_u f(a) = \nabla f(a)\cdot u &\leq \lVert\nabla f(a)\rVert\,\lVert u\rVert \\
&= \lVert\nabla f(a)\rVert
\end{aligned}$$

이고, 등호는 $$u$$가 $$\nabla f(a)$$와 같은 방향, 즉 $$u = \nabla f(a)/\lVert\nabla f(a)\rVert$$일 때 성립한다. 따라서 이 $$u$$에서 방향도함수가 최댓값 $$\lVert\nabla f(a)\rVert$$를 가진다. 같은 논리로 반대 방향에서 최솟값 $$-\lVert\nabla f(a)\rVert$$를 가지므로, $$-\nabla f$$는 가장 가파른 감소 방향이다.

</details>

명제 9는 기울기를 따라 내려가며 최솟값을 찾는 경사하강법의 기하학적 근거가 된다. 한편 기울기는 등위면 $$f = c$$에 수직이다: 등위면 위의 곡선 $$x(t)$$에 대해 $$f(x(t)) = c$$가 상수이므로, 연쇄법칙으로 $$\nabla f\cdot x'(t) = 0$$이 되어 기울기가 모든 접벡터와 직교하기 때문이다.

## 헤세 행렬과 이차 판정

임계점이 극대·극소·안장점 중 무엇인지를 가르는 것은 그 점에서의 이차 거동이다. 미분가능한 함수의 임계점 근방 전개

$$f(a + h) \approx f(a) + \tfrac{1}{2}\, h^\top H\, h, \qquad H = \begin{pmatrix} f_{xx} & f_{xy} \\ f_{yx} & f_{yy}\end{pmatrix}$$

에서 일차항이 $$\nabla f(a) = 0$$으로 사라지므로, 증감은 이차형식 $$h^\top H h$$의 부호가 결정한다. 이 이차형식이 양으로 정부호이면 극소, 음으로 정부호이면 극대, 부호가 갈리면 안장점이다.

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10 (이계도함수 판정)**</ins> $$f$$가 $$C^2$$이고 $$a$$가 임계점($$\nabla f(a) = 0$$)이라 하자. 판별식 $$D = f_{xx}f_{yy} - f_{xy}^2 = \det H$$에 대해, $$D > 0$$이고 $$f_{xx} > 0$$이면 $$a$$는 극소, $$D > 0$$이고 $$f_{xx} < 0$$이면 극대, $$D < 0$$이면 안장점이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

대칭행렬 $$H$$의 이차형식 $$Q(h) = h^\top H h$$를 본다. $$f_{xx} \neq 0$$일 때 완전제곱으로

$$\begin{aligned}
Q(h_1, h_2) &= f_{xx}h_1^2 + 2 f_{xy}h_1 h_2 + f_{yy}h_2^2 \\
&= f_{xx}\!\left(h_1 + \tfrac{f_{xy}}{f_{xx}}h_2\right)^2 + \frac{f_{xx}f_{yy} - f_{xy}^2}{f_{xx}}\,h_2^2
\end{aligned}$$

로 정리된다. $$D = f_{xx}f_{yy} - f_{xy}^2 > 0$$이면 둘째 항의 계수 $$D/f_{xx}$$가 $$f_{xx}$$와 같은 부호이므로 두 항의 부호가 일치해, $$f_{xx} > 0$$이면 $$Q > 0$$ (정부호, 극소), $$f_{xx} < 0$$이면 $$Q < 0$$ (음정부호, 극대)이다. $$D < 0$$이면 두 항의 부호가 반대라 $$Q$$가 양·음의 값을 모두 가지므로 안장점이다.

</details>

판정을 실제 함수에 적용해 보자. 다음 예시는 임계점이 둘 이상이고 그중 일부가 안장점인 경우를 보여 준다.

<div class="example" markdown="1">

<ins id="ex11">**예시 11 (극값 분류)**</ins> $$f(x,y) = x^3 - 3x + y^2$$의 임계점을 모두 찾아 분류하자. $$\nabla f = (3x^2 - 3,\ 2y) = 0$$에서 $$x = \pm 1$$, $$y = 0$$이므로 임계점은 $$(1, 0)$$과 $$(-1, 0)$$이다. 이계편미분은

$$f_{xx} = 6x, \qquad f_{yy} = 2, \qquad f_{xy} = 0, \qquad D = 12x$$

이다. 점 $$(1,0)$$에서는 $$D = 12 > 0$$, $$f_{xx} = 6 > 0$$이므로 극소이고, 점 $$(-1,0)$$에서는 $$D = -12 < 0$$이므로 안장점이다. 극솟값은 $$f(1,0) = 1 - 3 = -2$$이다.

</div>

마지막으로 제약 극값을 라그랑주 승수법으로 끝까지 푸는 예를 본다. 무제약 임계점 분석과 달리, 제약식과 $$\nabla f = \lambda\nabla g$$를 함께 연립해야 한다.

<div class="example" markdown="1">

<ins id="ex12">**예시 12 (라그랑주 승수)**</ins> 제약 $$g(x,y) = x^2 + y^2 = 1$$ 위에서 $$f(x,y) = xy$$의 극값을 찾자. $$\nabla f = (y, x)$$, $$\nabla g = (2x, 2y)$$이므로 $$\nabla f = \lambda\nabla g$$는

$$\begin{aligned}
y &= 2\lambda x, \\
x &= 2\lambda y
\end{aligned}$$

이다. 두 식을 곱하면 $$xy = 4\lambda^2 xy$$이므로 $$xy = 0$$이거나 $$\lambda^2 = 1/4$$이다. $$xy = 0$$이면 제약식에서 $$(\pm 1, 0)$$ 또는 $$(0, \pm 1)$$이 나오고 이때 $$f = 0$$이다. $$\lambda = \pm \tfrac12$$이면 $$y = \pm x$$이고 제약식 $$2x^2 = 1$$에서 $$x = \pm 1/\sqrt2$$이므로

$$f = xy = \pm \tfrac12$$

이다. 따라서 단위원 위에서 $$f = xy$$의 최댓값은 $$\tfrac12$$, 최솟값은 $$-\tfrac12$$이다.

</div>

