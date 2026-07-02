---
title: "다변수함수와 편미분"
description: "여러 변수의 함수에 대해 편미분과 기울기, 방향도함수를 정의하고, 미분가능성을 일차 근사로 정식화한다. 다변수 연쇄법칙, 혼합편미분의 클레로 정리, 접평면과 극값을 worked 예시로 다룬다."
excerpt: "편미분과 기울기, 미분가능성, 다변수 연쇄법칙, 극값"

categories: [Math / Calculus]
permalink: /ko/math/calculus/partial_derivatives
sidebar: 
    nav: "calculus-ko"

date: 2026-07-01
weight: 13
---

지금까지 다룬 미적분학은 다소 과하게 말하자면 고등학교 수준의 수학을 엄밀하게 형식화한 것에 지나지 않는다. 이번 글부터 우리는 우리가 다루는 함수들을 더 일반적으로 택하여, 실제로 새로운 내용을 시작할 것이다. 

우리의 일반화의 방향은 차원을 늘리는 방향으로 진행된다. 즉, 지금까지의 함수들이 모두 $$f:\mathbb{R}\rightarrow\mathbb{R}$$이었다면 지금부터 다룰 함수들은 $$\mathbb{R}^m$$에서 $$\mathbb{R}^n$$으로 가는 함수들이며, 우리는 우선 함수의 정의역을 $$\mathbb{R}$$에서 $$\mathbb{R}^m$$으로 올리는 것부터 시작한다. 

## 벡터공간

우리의 정의역 $$\mathbb{R}^m$$은 벡터공간이며, 미분은 이 공간 위에서 정의된 함수를 <em-ko>선형화</em-ko>하는 것이므로 본질적으로 이를 위해서는 선형대수학의 지식이 어느정도는 필요하다. 그러나 이를 위해 선형대수학을 처음부터 쌓는 것은 다소 과한 감이 있으므로, 우리에게 필요한 개념과 결과만 간략하게 정리하고 넘어가기로 하자.

$$\mathbb{R}^m$$는 *벡터공간<sub>vector space</sub>*이며, 이 공간의 원소를 *벡터<sub>vector</sub>*라 부른다. 이들은 다음의 순서쌍

$$\mathbf{a}=(a_1, \ldots, a_m)\qquad a_i\in\mathbb{R}$$

로 쓰이는 원소들이며, 이들 벡터들 사이에는 두 가지 기본 연산이 있다. 하나는 두 벡터 $$\mathbf{v}=(v_1,\ldots,v_m)$$와 $$\mathbf{w}=(w_1,\ldots,w_m)$$를 더하는 *덧셈* 

$$\mathbf{v}+\mathbf{w}=(v_1+w_1,\ldots,v_m+w_m)$$

이고, 다른 하나는 실수 $$c$$를 곱하는 *스칼라곱* 

$$c\mathbf{v}=(cv_1,\ldots,cv_m)$$

이다. 이 연산들은 좌표평면에서 본 벡터 연산을 $$m$$차원으로 그대로 옮긴 것이며, 교환법칙과 결합법칙, 분배법칙 등이 자연스럽게 성립한다.

우리가 다루는 공간은 유클리드 공간이므로 여기에 내적과 노름도 함께 사용한다. 두 벡터 $$\mathbf{v},\mathbf{w}\in\mathbb{R}^m$$의 *내적<sub>inner product</sub>*은 좌표별 곱의 합

$$\mathbf{v}\cdot \mathbf{w}=v_1w_1+\cdots+v_mw_m$$

으로 정의되고, 이로부터 벡터의 *norm<sub>노름</sub>*, 즉 크기는 $$\lVert \mathbf{v}\rVert=\sqrt{\mathbf{v}\cdot \mathbf{v}}$$로 주어진다. 내적은 두 벡터가 이루는 각도를 재는 데에도 쓰이며, 특히 $$\mathbf{v}\cdot \mathbf{w}=0$$일 때 두 벡터가 서로 *직교<sub>orthogonal</sub>*한다고 한다. 

한편, 세 차원 $$\mathbb{R}^3$$에서는 추가로 *외적<sub>cross product</sub>*이 정의된다. 두 벡터 $$\mathbf{v},\mathbf{w}\in\mathbb{R}^3$$에 대해 외적 $$\mathbf{v}\times \mathbf{w}$$는 $$\mathbf{v}$$와 $$\mathbf{w}$$ 모두에 직교하면서 방향이 오른손 법칙을 따르고, 크기는 $$\mathbf{v}$$와 $$\mathbf{w}$$가 이루는 평행사변형의 넓이와 같은 벡터이다. 좌표로는

$$\mathbf{v}\times \mathbf{w}=(v_2w_3-v_3w_2,\ v_3w_1-v_1w_3,\ v_1w_2-v_2w_1)$$

로 계산한다. 외적은 곡면의 접평면이나 회전을 다룰 때 자연스럽게 등장하지만, 이 글에서는 주로 직교하는 벡터를 만드는 도구로만 기억해도 충분하다.

벡터공간 사이의 함수 $$T:\mathbb{R}^m\rightarrow\mathbb{R}^n$$이 *선형사상<sub>linear map</sub>*이라는 것은, 임의의 벡터 $$\mathbf{v},\mathbf{w}\in\mathbb{R}^m$$과 실수 $$c\in\mathbb{R}$$에 대해

$$T(\mathbf{v}+\mathbf{w})=T(\mathbf{v})+T(\mathbf{w}),\qquad T(c \mathbf{v})=cT(\mathbf{v})$$

이 성립하는 것이다. 즉 선형사상은 덧셈과 스칼라곱을 보존하는 함수이다. $$\mathbb{R}^m$$에서 $$\mathbb{R}^n$$으로 가는 선형사상은 $$n\times m$$개의 좌표들을 명시적으로 적은 *행렬<sub>matrix</sub>*

$$A=\begin{pmatrix} a_{11} & \cdots & a_{1m} \\ \vdots & \ddots & \vdots \\ a_{n1} & \cdots & a_{nm} \end{pmatrix}$$

의 꼴로 표현할 수 있으나, 이를 자세히 다루는 것은 선형대수학으로 미룬다. 기억할 것은 선형사상이 곧 행렬이라는 것 뿐이며, 우리 경우에는 정사각행렬, 즉 $$n\times n$$ 행렬마다 정의되는 *행렬식<sub>determinant</sub>*이라는 값이 특히 중요하다. 직관적으로 이는 선형사상이 부피를 얼마나 늘이거나 줄이는지를 나타내는 값으로, 낮은 차원의 경우에는

$$\det\begin{pmatrix} a & b \\ c & d \end{pmatrix}=ad-bc$$

그리고

$$\det\begin{pmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{pmatrix}=a_{11}a_{22}a_{33}+a_{12}a_{23}a_{31}+a_{13}a_{21}a_{32}-a_{13}a_{22}a_{31}-a_{11}a_{23}a_{32}-a_{12}a_{21}a_{33}$$

으로 주어진다. 

## 다변수함수의 극한과 연속

미분을 정의하기에 앞서, 다변수함수의 극한과 연속을 짚고 넘어가야 한다. 일변수함수에서 극한은 점 $$a$$의 양쪽, 즉 좌·우 두 방향만 보면 충분했다. 그러나 정의역이 $$\mathbb{R}^m$$이 되면 점 $$\mathbf{a}$$로 다가오는 경로가 무수히 많아지므로 다소 주의할 필요가 있다. 

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 다변수함수 $$f: \mathbb{R}^m \to \mathbb{R}$$가 점 $$\mathbf{a}$$에서 *극한<sub>limit</sub>* $$L$$을 가진다는 것은, 임의의 $$\varepsilon > 0$$에 대해 어떤 $$\delta > 0$$가 존재하여

$$0 < \lVert \mathbf{x} - \mathbf{a}\rVert < \delta \quad\Rightarrow\quad \lvert f(\mathbf{x}) - L\rvert < \varepsilon$$

가 $$0 < \lVert \mathbf{x} - \mathbf{a}\rVert < \delta$$를 만족하는 모든 $$\mathbf{x}$$에 대해 성립하는 것이다. 이를 $$\lim_{\mathbf{x}\to\mathbf{a}} f(\mathbf{x}) = L$$로 쓰며, 특히 $$\lim_{\mathbf{x}\to\mathbf{a}} f(\mathbf{x}) = f(\mathbf{a})$$일 때 $$f$$는 $$\mathbf{a}$$에서 *연속<sub>continuous</sub>*이라 한다.

</div>

이 정의의 형식은 일변수와 본질적으로 같으며, 차이는 $$1$$차원에서의 거리 $$\lvert x - a\rvert$$가 $$m$$차원에서의 거리 $$\lVert\mathbf{x} - \mathbf{a}\rVert$$로 바뀐 것이 전부다. 그러나, 예를 들어, 주어진 함수의 극한값이 $$L$$임을 확인하기 위해서는 임의의 방향 $$\mathbb{v}=(v_1, \ldots, v_m)$$에 대하여 다음 극한

$$\lim_{t\rightarrow 0}f(\mathbf{a}+t\mathbf{v})=L$$

인 것만 확인하면 <em-ko>안된다</em-ko>. 가령 함수 $$f:\mathbb{R}^2\rightarrow \mathbb{R}$$

$$f(\mathbf{x})=\begin{cases}1&\text{if $y=x^2$,}\\ 0&\text{otherwise}\end{cases}$$

으로 정의한다면 이 함수는 모든 직선 방향에서 그 극한이 $$0$$이지만 곡선 $$y=x^2$$을 따라가는 경로에서는 극한값이 $$1$$이다. 이 주의는 특히 이번 글의 나머지에서 편미분을 정의한 후 다변수함수의 미분을 논할 때 특히 신경써야 한다. 

## 다변수함수의 미분

이제 우리는 예고했던대로 다변수함수, 즉 $$\mathbb{R}^m$$의 점마다 함숫값을 대응시키는 함수의 경우를 살펴본다. 이 경우, 함수는 좌극한이나 우극한 뿐만 아니라, 온갖 방향에서 한 점으로 향할 수 있으므로, 미분을 정의할 때 방향이 중요해진다. 

가장 단순한 변화율은 한 좌표축 방향으로만 움직일 때의 것이다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> 다변수함수 $$f(x_1, \ldots, x_n)$$의 점 $$\mathbf{a}$$에서 변수 $$x_i$$에 대한 *편미분<sub>partial derivative</sub>*은 나머지 변수를 고정한 채 $$x_i$$로만 미분한 것이다. 즉, 

$$\frac{\partial f}{\partial x_i}(  \mathbf{a}) = \lim_{h\to 0}\frac{f(\mathbf{a} + h \mathbf{e}_i) - f(\mathbf{a})}{h}$$

으로 주어지며, 여기서 $$\mathbf{e}_i$$는 $$i$$번째 성분만 $$1$$, 나머지 성분은 $$0$$인 표준기저벡터이다. 모든 편미분을 모은 벡터 

$$\nabla f(\mathbf{a}) = \left(\frac{\partial f}{\partial x_1}(\mathbf{a}), \ldots, \frac{\partial f}{\partial x_n}(\mathbf{a})\right)$$

를 $$f$$의 *기울기<sub>gradient</sub>*라 한다.

</div>

편미분의 계산은 일변수 미분과 똑같되 나머지 변수를 상수로 취급할 뿐이므로, 일변수함수에서의 미분법이 그대로 적용된다. 

그러나 미분가능성의 경우는 다소 주의가 필요하다. 이를 확인하기 위해 다음 극한의 존재성

$$\lim_{h\rightarrow 0} \frac{f(a+h)-f(a)}{h}$$

은 양쪽 방향에서의 극한을 모두 보는 것임을 기억하자. 이 경우 위의 극한은 <em-ko>숫자 하나</em-ko>를 주며, 이는 정확히 곡선에 접하는 접선의 기울기이다. 

이를 일반화하려면 두 가지를 주의해야 하는데, 하나는 $$h$$가 이제 벡터공간의 원소로서 모든 방향에서 $$0$$을 향해 올 수 있다는 것이고, 다른 하나는 이제 더 이상 선형근사가 숫자 하나로 표현되지 않는다는 것이다. 가령 곡면에 접하는 평면을 생각해보면, 이 평면을 매개하기 위해서는 접점을 제외하고도 두 개의 변수가 필요하다. 

이를 해결하기 위해 우리에게 익숙한 직선의 방정식을 내적의 꼴로 다시 써보자. 평면 위에서 점 $$\mathbf{a}=(a_1,a_2)$$를 지나며 벡터 $$\mathbf{n}=(n_1,n_2)$$에 수직인 직선은, 그 위의 임의의 점 $$\mathbf{x}=(x,y)$$이 다음 방정식

$$\mathbf{n}\cdot(\mathbf{x}-\mathbf{a})=0$$

을 만족한다는 조건으로 주어지며, 이를 모두 대입해보면

$$n_1(x-a_1)+n_2(y-a_2)=0,$$

즉 우리에게 익숙한 직선의 방정식이 나온다. 비슷하게, $$\mathbb{R}^m$$에서의 한 점 $$\mathbf{a}=(a_1,\ldots, a_m)$$를 지나며 벡터 $$\mathbf{n}=(n_1,\ldots, n_m)$$에 수직인 *초평면<sub>hypersurface</sub>* 위의 점 $$\mathbf{x}=(x_1,\ldots, x_m)$$은 같은 방정식

$$\mathbf{n}\cdot(\mathbf{x}-\mathbf{a})=0$$

으로 주어지며, 이를 풀어쓰면

$$n_1(x_1-a_1)+\cdots+n_m(x_m-a_m)=0$$

이 되어 우리가 기대하던 일차식의 꼴이 된다. 이제 마지막으로 일차식에서의 극한

$$\lim_{h\rightarrow 0}\frac{f(a+h)-f(a)}{h}=k$$

의 우변을 이항하여 다음의 식

$$\lim_{h\rightarrow 0}\frac{f(a+h)-(f(a)+kh)}{h}=0$$

의 꼴로 쓰면, 이 식은 점 $$a$$ 근방에서의 함숫값 $$f(a+h)$$가 직선 $$y=f(a)+kh$$로 일차근사된다는 것을 의미한다. 우리는 위에서 $$\mathbb{R}^m$$의 일차식을 어떻게 적을 수 있는지 살펴보았으므로, 이제 다음 정의가 명확하다. 

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> 다변수함수 $$f$$가 점 $$\mathbf{a}$$에서 *미분가능<sub>differentiable</sub>*하다는 것은, 벡터 $$\mathbf{n}$$이 존재하여

$$\lim_{\mathbf{h} \to 0}\frac{f(\mathbf{a} + \mathbf{h}) - f(\mathbf{a}) - \mathbf{n}\cdot \mathbf{h}}{\lVert \mathbf{h}\rVert} = 0$$

이 성립하는 것이다.

</div>

그럼 가장 놀라운 점은 이렇게 정의된 벡터 $$\mathbf{n}$$이 실제로는 위의 [정의 2](#def2)에서 살펴본 기울기 벡터 $$\nabla f(\mathbf{a})$$와 일치한다는 것이다. 

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> $$f$$가 점 $$\mathbf{a}$$에서 미분가능하면, [정의 3](#def3)의 벡터 $$\mathbf{n}$$은 $$\mathbf{n} = \nabla f(\mathbf{a})$$이고, $$f(\mathbf{a}+\mathbf{h}) \approx f(\mathbf{a}) + \nabla f(\mathbf{a})\cdot \mathbf{h}$$가 최선의 일차 근사이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

[정의 3](#def3)의 극한에서 $$\mathbf{h} = t \mathbf{e}_i$$로 두면, $$\lVert \mathbf{h}\rVert = \lvert t\rvert$$이므로

$$\lim_{t \to 0}\frac{f(\mathbf{a} + t \mathbf{e}_i) - f(\mathbf{a}) - \mathbf{n}\cdot (t \mathbf{e}_i)}{\lvert t\rvert} = 0$$

이다. $$\mathbf{n}\cdot (t \mathbf{e}_i) = t n_i$$이다. $$t>0$$일 때 $$\lvert t\rvert = t$$이므로 위 극한의 분자를 $$t$$로 정리하면 $$\frac{f(\mathbf{a} + t \mathbf{e}_i) - f(\mathbf{a})}{t} - n_i$$이고, 이는 편미분의 정의에 의해 $$\frac{\partial f}{\partial x_i}(\mathbf{a}) - n_i$$로 수렴한다. $$t<0$$일 때도 같은 논리로 같은 결론이므로, 위 극한이 $$0$$이 되려면 $$n_i = \frac{\partial f}{\partial x_i}(\mathbf{a})$$이어야 한다. 모든 $$i$$에 대해 이를 모으면 $$\mathbf{n} = \nabla f(\mathbf{a})$$이다.

</details>

여기에서 [정의 3](#def3)과 [명제 4](#prop4)를 명확하게 분리하여 서술했다는 것을 주목하자. [명제 4](#prop4)는, <em-ko>만일</em-ko> 함수 $$f$$가 미분가능하다면, 그 조건을 만족하는 $$\mathbf{n}$$이 $$\nabla f$$라는 것이며, 이를 거꾸로 해석하여 모든 편미분이 존재하여 $$\nabla f$$가 잘 정의되면 함수 $$f$$가 미분가능하다고 이해하면 <em-ko>안된다.</em-ko> 대신 다음의 조건은 각각의 편미분이 연속이라면 연속함수 $$f$$가 미분가능하다는 것을 보여준다. 

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> 연속함수 $$f$$의 모든 편미분이 $$\mathbf{a}$$ 근방에서 존재하고, 이들이 모두 $$\mathbf{a}$$에서 연속이라면 $$f$$는 $$\mathbf{a}$$에서 미분가능하다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

표기를 간단히 하기 위해 두 변수 $$f(x,y)$$와 점 $$(a,b)$$에서 보이자. 일반 차원도 같은 논법을 좌표마다 반복하면 된다. 벡터 $$(h,k)$$를 한 좌표씩 움직여

$$f(a+h, b+k) - f(a,b) = \bigl(f(a+h, b+k) - f(a, b+k)\bigr) + \bigl(f(a, b+k) - f(a,b)\bigr)$$

로 쪼개면, 각 괄호는 한 변수만 변하므로 평균값정리에 의해 적당한 $$\theta_1, \theta_2 \in (0,1)$$에 대해

$$f(a+h,b+k) - f(a,b) = f_x(a+\theta_1 h, b+k) h + f_y(a, b+\theta_2 k) k$$

이며, 여기에서 $$\nabla f(a,b)\cdot(h,k) = f_x(a,b)h + f_y(a,b)k$$를 빼면

$$f(a+h,b+k) - f(a,b) - \nabla f(a,b)\cdot(h,k) = \bigl(f_x(a+\theta_1 h, b+k) - f_x(a,b)\bigr)h + \bigl(f_y(a, b+\theta_2 k) - f_y(a,b)\bigr)k$$

를 얻는다. 그럼 $$f_x, f_y$$가 $$(a,b)$$에서 연속이므로 $$(h,k)\to(0,0)$$일 때 두 괄호가 모두 $$0$$으로 가고, $$\lvert h\rvert, \lvert k\rvert \le \lVert(h,k)\rVert$$이므로 [정의 3](#def3)의 극한이 성립한다. 즉, $$f$$는 $$(a,b)$$에서 미분가능하고 그 기울기는 $$\nabla f(a,b)$$이다.

</details>

## 연쇄법칙과 혼합편미분

이제 우리는 다변수함수의 연쇄법칙을 살펴본다. 만일 다변수함수가 입력으로 받는 변수 중 하나만이 다른 함수와의 합성으로 나타난다면 이는 해당 변수에 대한 편미분을 사용하여 일변수미분과 동일하게 연쇄법칙을 적용할 수 있지만, 문제는 다변수함수가 입력으로 받는 변수 여럿이 다른 함수를 거쳐 정의되었을 때 나타난다. 

이를 위해서는 하나의 매개변수 $$t$$로 매개화된 곡선 $$\mathbf{x}(t) = (x_1(t), \ldots, x_n(t))$$을 생각해야 한다. 즉, 점 $$\mathbf{x}$$가 $$t$$에 따라 $$\mathbb{R}^n$$ 속을 움직이는 경우를 생각하자. 그럼 이 곡선이 *미분가능하다*는 것은 각 좌표 함수 $$x_i(t)$$가 일변수 함수로서 $$t$$에 대해 미분가능하다는 뜻이고, 그때 성분별 미분을 모은 벡터 

$$\mathbf{x}'(t) = (x_1'(t), \ldots, x_n'(t))$$

가 잘 정의되어 점 $$\mathbf{x}(t)$$에서 곡선에 접하는 방향과 속력을 담는 접벡터가 된다. 이는 우리가 현재 진행중인 일반화의 방향(즉 정의역을 $$\mathbb{R}^m$$으로 확장하는 방향)과는 다른 방향의 일반화로, 이 과정이 끝나면 더 일반적으로 공역의 차원 또한 늘리게 된다. 어쨌든 이와 같은 정의 하에서 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="thm6">**정리 6 (다변수 연쇄법칙)**</ins> $$f$$가 미분가능하고 $$\mathbf{x}(t) = (x_1(t), \ldots, x_n(t))$$가 미분가능한 곡선이면, 합성 $$t \mapsto f(\mathbf{x}(t))$$도 미분가능하고

$$\frac{d}{dt} f(\mathbf{x}(t)) = \nabla f(\mathbf{x}(t)) \cdot \mathbf{x}'(t) = \sum_{i=1}^n \frac{\partial f}{\partial x_i} \frac{dx_i}{dt}$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

[정의 3](#def3)을 점 $$\mathbf{x}(t)$$와 변화량 $$\Delta\mathbf{x}=\mathbf{x}(t+\Delta t)-\mathbf{x}(t)$$에 적용하면 $$\Delta t\to 0$$일 때

$$\frac{f(\mathbf{x}(t+\Delta t))-f(\mathbf{x}(t))-\nabla f(\mathbf{x}(t))\cdot\Delta\mathbf{x}}{\lVert\Delta\mathbf{x}\rVert}\to 0$$

이다. 양변을 $$\Delta t$$로 나누면 우변은 일차항 $$\nabla f(\mathbf{x}(t))\cdot\frac{\Delta\mathbf{x}}{\Delta t}$$과 나머지항으로 갈라지는데, 이 나머지항은 위에서 $$0$$으로 간 양에 $$\lVert\Delta\mathbf{x}\rVert/\Delta t$$가 곱해진 것이다. 곡선의 미분가능성으로 $$\Delta\mathbf{x}/\Delta t\to\mathbf{x}'(t)$$이므로 $$\lVert\Delta\mathbf{x}\rVert/\lvert\Delta t\rvert$$가 유계이며, 따라서 나머지항도 $$\Delta t\to 0$$에서 $$0$$으로 사라져 공식을 얻는다.

</details>

[정리 6](#thm6)는 한 변수가 여러 변수에 의존할 때 편미분이 사슬처럼 연결됨을 말하며, 좌표변환에서 주로 쓰인다. 가령 $$z = f(x,y)$$에서 극좌표 $$x = r\cos\theta$$, $$y = r\sin\theta$$로 바꾸면 $$\partial z/\partial r = f_x\cos\theta + f_y\sin\theta$$가 곧바로 나온다.

한편, 이계편미분에 대해서는 미분의 순서가 (적절한 연속성 아래) 문제되지 않는다.

<div class="proposition" markdown="1">

<ins id="thm7">**정리 7 (Clairaut)**</ins> 두 혼합편미분 $$\frac{\partial^2 f}{\partial x \partial y}$$와 $$\frac{\partial^2 f}{\partial y \partial x}$$가 모두 존재하고 한 점 근방에서 연속이면, 그 점에서 둘이 같다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

점을 $$(a,b)$$라 하고 이차 차분

$$\Delta = f(a+h, b+k) - f(a+h, b) - f(a, b+k) + f(a, b)$$

를 생각한다. $$\varphi(x) = f(x, b+k) - f(x, b)$$로 두면 $$\Delta = \varphi(a+h) - \varphi(a)$$이고, 평균값정리로 적당한 $$\theta_1\in(0,1)$$에 대해 $$\Delta = \varphi'(a+\theta_1 h)h = \bigl(f_x(a+\theta_1 h, b+k) - f_x(a+\theta_1 h, b)\bigr)h$$이다. 안쪽 차분에 다시 $$y$$에 대한 평균값정리를 적용하면 적당한 $$\theta_2\in(0,1)$$에 대해

$$\Delta = \frac{\partial^2 f}{\partial y \partial x}(a+\theta_1 h, b+\theta_2 k) hk$$

를 얻는다. 대칭적으로 $$\psi(y) = f(a+h, y) - f(a, y)$$로 두고 $$x$$와 $$y$$의 역할을 바꾸면 적당한 $$\theta_3, \theta_4\in(0,1)$$에 대해

$$\Delta = \frac{\partial^2 f}{\partial x \partial y}(a+\theta_3 h, b+\theta_4 k) hk$$

이다. 두 식을 $$hk$$로 나눈 뒤 $$(h,k)\to(0,0)$$의 극한을 취하면, 두 혼합편미분이 $$(a,b)$$에서 연속이므로 우변이 각각 $$\frac{\partial^2 f}{\partial y\partial x}(a,b)$$와 $$\frac{\partial^2 f}{\partial x\partial y}(a,b)$$로 수렴하여 둘이 같다.

</details>

## 방향도함수와 기울기

단위벡터 $$\mathbf{u}$$를 따라 움직일 때의 변화율인 *방향도함수* $$D_{\mathbf{u}} f(\mathbf{a})$$는 정의상 한 변수 함수 $$g(t) = f(\mathbf{a} + t\mathbf{u})$$의 $$t = 0$$에서의 도함수인데, [정리 6](#thm6)의 연쇄법칙을 $$\mathbf{x}(t) = \mathbf{a} + t\mathbf{u}$$에 적용하면 $$D_{\mathbf{u}} f(\mathbf{a}) = g'(0) = \nabla f(\mathbf{a})\cdot \mathbf{u}$$가 곧바로 나온다. 그럼 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8 (최대 경사 방향)**</ins> $$f$$가 $$\mathbf{a}$$에서 미분가능하고 $$\nabla f(\mathbf{a}) \neq 0$$이면, 단위벡터 방향의 방향도함수 $$D_{\mathbf{u}} f(\mathbf{a})$$는 $$\mathbf{u} = \nabla f(\mathbf{a})/\lVert\nabla f(\mathbf{a})\rVert$$일 때 최대가 되고, 그 최댓값은 $$\lVert\nabla f(\mathbf{a})\rVert$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

미분가능성에 의해 임의의 단위벡터 $$\mathbf{u}$$에 대해 $$D_{\mathbf{u}} f(\mathbf{a}) = \nabla f(\mathbf{a})\cdot \mathbf{u}$$이다. 코시–슈바르츠 부등식으로

$$\begin{aligned}
D_{\mathbf{u}} f(\mathbf{a}) = \nabla f(\mathbf{a})\cdot \mathbf{u} &\leq \lVert\nabla f(\mathbf{a})\rVert \lVert \mathbf{u}\rVert \\
&= \lVert\nabla f(\mathbf{a})\rVert
\end{aligned}$$

이고, 등호는 $$\mathbf{u}$$가 $$\nabla f(\mathbf{a})$$와 같은 방향, 즉 $$\mathbf{u} = \nabla f(\mathbf{a})/\lVert\nabla f(\mathbf{a})\rVert$$일 때 성립한다. 따라서 이 $$\mathbf{u}$$에서 방향도함수가 최댓값 $$\lVert\nabla f(\mathbf{a})\rVert$$를 가진다. 같은 논리로 반대 방향에서 최솟값 $$-\lVert\nabla f(\mathbf{a})\rVert$$를 가지므로, $$-\nabla f$$는 가장 가파른 감소 방향이다.

</details>

[명제 8](#prop8)은 기울기를 따라 내려가며 최솟값을 찾는 경사하강법의 기하학적 근거가 된다. 한편 기울기는 등위면 $$f = c$$에 수직이다: 등위면 위의 곡선 $$\mathbf{x}(t)$$에 대해 $$f(\mathbf{x}(t)) = c$$가 상수이므로, 연쇄법칙으로 $$\nabla f\cdot \mathbf{x}'(t) = 0$$이 되어 기울기가 모든 접벡터와 직교하기 때문이다.

## 극값과 헤세 행렬

한 변수에서 극값이 임계점에서 일어났듯, 다변수에서도 미분가능한 함수의 극값은 각 편미분이 $$0$$이 되어야 하므로 $$\nabla f = 0$$인 *임계점*에서만 일어난다. 일변수함수의 경우 우리는 이 임계점이 극대인지, 극소인지를 이계도함수를 사용하여 판단할 수 있었는데 ([§평균값 정리, ⁋명제 17](/ko/math/calculus/mean_value_theorem#prop17)), 비슷한 상황이 다변수함수에서도 일어난다. 

다만 주의할 것은, 이제 미분을 취할 수 있는 방향이 여럿이므로 한 방향에서는 극소, 다른 한 방향에서는 극대인 점이 존재할 수 있다는 것이다. 이러한 점을 *안장점<sub>saddle point</sub>*이라 부른다. 이 섹션에서 우리는 임계점이 언제 극대, 극소, 안장점인지를 판별할 것인데, 계산의 편의상 $$\mathbb{R}^2$$에서 정의된 다변수함수로 우리 관심을 제한한다. 

미분가능한 이변수함수의 임계점 근방에서 테일러 전개하면, 일차항이 $$\nabla f(\mathbf{a}) = 0$$으로 사라지고 남는 이차항은

$$f(\mathbf{a}+\mathbf{h}) \approx f(\mathbf{a}) + \frac{1}{2}\bigl(f_{xx}(\mathbf{a})h_1^2 + 2f_{xy}(\mathbf{a})h_1 h_2 + f_{yy}(\mathbf{a})h_2^2\bigr)$$

이다. 이 이차형식의 계수들을 사각 행렬로 모은 것이 임계점 $$\mathbf{a}$$에서의 *헤세 행렬<sub>Hessian</sub>*로, 이는 다음의 식

$$H = \begin{pmatrix} f_{xx} & f_{xy} \\ f_{yx} & f_{yy}\end{pmatrix}$$

으로 주어진다. 임계점의 증감은 이 이차형식의 부호가 정하며, 이를 우리 상황에 맞추어 판별식의 언어로 풀어 설명하면 다음과 같다. 

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9 (이계도함수 판정)**</ins> $$f$$가 $$C^2$$이고 $$\mathbf{a}$$가 임계점($$\nabla f(\mathbf{a}) = 0$$)이라 하고, 위 헤세 행렬의 판별식  $$D = f_{xx}f_{yy} - f_{xy}^2 = \det H$$을 생각하자.

1. $$D > 0$$이고 $$f_{xx} > 0$$이면 $$\mathbf{a}$$는 극소이다. 
2. $$D > 0$$이고 $$f_{xx} < 0$$이면 이 점은 극대이다. 
3. $$D < 0$$이면 이 점은 안장점이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

임계점 근방 전개에서 남는 이차항 $$f_{xx}h_1^2 + 2f_{xy}h_1 h_2 + f_{yy}h_2^2$$을 보자.우선 $$f_{xx} \neq 0$$일 때, 이를 $$h_1$$에 대해 완전제곱꼴로 바꾸면

$$\begin{aligned}
f_{xx}h_1^2 + 2f_{xy}h_1 h_2 + f_{yy}h_2^2
&= f_{xx} \left(h_1 + \frac{f_{xy}}{f_{xx}}h_2\right)^2 + \frac{f_{xx}f_{yy} - f_{xy}^2}{f_{xx}} h_2^2 \\
&= f_{xx} \left(h_1 + \frac{f_{xy}}{f_{xx}}h_2\right)^2 + \frac{D}{f_{xx}} h_2^2
\end{aligned}$$

이며, 따라서 첫째 항의 부호는 $$f_{xx}$$를 따르고, 둘째 항의 부호는 $$D/f_{xx}$$를 따른다. 특히 $$D > 0$$이면 $$D/f_{xx}$$가 $$f_{xx}$$와 같은 부호여서 두 항의 부호가 일치한다. 추가적으로 $$f_{xx} > 0$$이면, 이차항들이 $$0$$이 아닌 한 항상 양수라 $$\mathbf{a}$$ 근방에서 함숫값이 더 커져 이 점이 극소점이 되며, 반대로 $$f_{xx} < 0$$이면 항상 음수라 극대이다. 반면 $$D < 0$$이면 두 항의 부호가 반대이므로 $$h_1, h_2$$의 비율에 따라 이차항이 양과 음 양쪽 값을 모두 가지며, $$\mathbf{a}$$는 안장점이다.

</details>

판별식이 음일 때 나타나는 안장점은 방향에 따라 함수가 오르내리는 가장 단순한 임계점이라 할 수 있다.

<div class="example" markdown="1">

<ins id="ex10">**예시 10 (안장점)**</ins> $$f(x,y) = x^2 - y^2$$은 $$\nabla f = (2x, -2y) = 0$$에서 임계점 $$(0,0)$$을 가진다. 헤세 행렬은 $$\begin{pmatrix} 2 & 0 \\ 0 & -2\end{pmatrix}$$로 $$\det H = -4 < 0$$이므로 안장점이다. 실제로 $$x$$축을 따라가면 $$f = x^2$$로 극소, $$y$$축을 따라가면 $$f = -y^2$$로 극대라, 방향에 따라 오르내리는 말안장 모양이다. 아래 그림은 이 곡면 $$z = x^2 - y^2$$의 모습으로, 원점(검은 점)이 안장점이다.

![saddle_surface](/assets/images/Math/Calculus/Partial_Derivatives-1.svg){:style="width:21.37em" class="invert" .align-center}

</div>

다만, $$D=0$$인 경우에는 위의 판별법이 어떠한 정보도 주지 않는 것에 유의하자. 이러한 경우는 각각의 상황에 맞는 방식을 적절히 사용하여야 한다.

## 라그랑주 승수법

미분법의 좋은 응용 중 하나는 주어진 구간 $$[a,b]$$ 안에서 함수의 극값을 찾는 것이었다. 우리는 이를 다변수함수에서 다룬다. 차이점은 이제 변수가 단순한 구간이 아니라는 것이며, 예를 들어 변수가 어떤 제약 $$g(\mathbf{x}) = c$$를 만족해야 하는 상황 또한 생각하게 된마. 이를테면 주어진 곡면 위에서 원점에 가장 가까운 점을 찾거나 고정된 자원 안에서 비용을 최소화하는 문제가 그렇다. 이러한 *제약극값<sub>constrained extremum</sub>*을 찾는 표준 도구가 라그랑주 승수법이다.

<div class="proposition" markdown="1">

<ins id="prop11">**명제 11 (라그랑주 승수)**</ins> $$f, g:\mathbb{R}^n\rightarrow\mathbb{R}$$가 $$C^1$$이고, 점 $$\mathbf{a}$$가 제약 $$g(\mathbf{x}) = c$$를 만족하는 점들 위에서 $$f$$의 local extrema이며 $$\nabla g(\mathbf{a}) \neq 0$$이라 하자. 그러면 어떤 실수 $$\lambda$$에 대해

$$\nabla f(\mathbf{a}) = \lambda \nabla g(\mathbf{a})$$

가 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

제약면 $$\{g = c\}$$ 위에서 $$\mathbf{a}$$를 지나는 임의의 매끄러운 곡선 $$\mathbf{x}(t)$$ ($$\mathbf{x}(0) = \mathbf{a}$$)를 잡자. $$g(\mathbf{x}(t)) = c$$가 상수이므로 [정리 6](#thm6)으로 미분하면 $$\nabla g(\mathbf{a}) \cdot \mathbf{x}'(0) = 0$$이고, 한편 $$\mathbf{a}$$가 제약 아래에서 $$f$$의 극값을 주므로 $$t \mapsto f(\mathbf{x}(t))$$도 $$t = 0$$에서 극값을 가지고, 따라서 $$\nabla f(\mathbf{a}) \cdot \mathbf{x}'(0) = 0$$이다. 즉, 두 벡터 $$\nabla f(\mathbf{a})$$와 $$\nabla g(\mathbf{a})$$ 모두가 제약면의 접공간에 직교한다. 그런데 전체 공간이 $$3$$차원이고, 제약면의 접공간이 $$2$$차원이므로 이러한 방향은 하나 뿐이고, 따라서 $$\nabla f(\mathbf{a}) = \lambda \nabla g(\mathbf{a})$$인 실수 $$\lambda$$가 존재한다.

</details>

실제 계산에서는 새로 도입된 실수 $$\lambda$$를 미지수로 추가하여 $$\nabla f = \lambda \nabla g$$와 제약식 $$g = c$$를 함께 연립하여 푸는데, 이 $$\lambda$$를 *라그랑주 승수<sub>Lagrange multiplier</sub>*라 부른다.

<div class="example" markdown="1">

<ins id="ex12">**예시 12 (라그랑주 승수)**</ins> 제약 $$g(x,y) = x^2 + y^2 = 1$$ 위에서 $$f(x,y) = xy$$의 극값을 찾자. $$\nabla f = (y, x)$$, $$\nabla g = (2x, 2y)$$이므로 $$\nabla f = \lambda \nabla g$$는

$$\begin{aligned}
y &= 2\lambda x, \\
x &= 2\lambda y
\end{aligned}$$

이다. 두 식을 곱하면 $$xy = 4\lambda^2 xy$$이므로 $$xy = 0$$이거나 $$\lambda^2 = 1/4$$이다. $$xy = 0$$이면 제약식에서 $$(\pm 1, 0)$$ 또는 $$(0, \pm 1)$$이 나오고 이때 $$f = 0$$이다. $$\lambda = \pm 1/2$$이면 $$y = \pm x$$이고 제약식 $$2x^2 = 1$$에서 $$x = \pm 1/\sqrt2$$이므로 $$f = xy = \pm 1/2$$이다. 따라서 단위원 위에서 $$f = xy$$의 최댓값은 $$1/2$$, 최솟값은 $$-1/2$$이다.

</div>
