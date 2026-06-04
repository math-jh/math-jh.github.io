---
title: "다변수 미분"
description: "다변수함수의 미분을 일차근사를 주는 선형사상으로 정의하고, 야코비 행렬로 표현한다. 연쇄법칙을 선형사상의 합성으로 깔끔하게 증명하고, 편미분이 연속이면 미분가능함을 보인다."
excerpt: "선형사상으로서의 미분, 야코비 행렬, 연쇄법칙"

categories: [Math / Analysis]
permalink: /ko/math/analysis/multivariable_differentiation
sidebar: 
    nav: "analysis-ko"

date: 2026-06-02
last_modified_at: 2026-06-02
weight: 19

published: false
---

[\[미적분학\] §다변수함수와 편미분](/ko/math/calculus/partial_derivatives)에서 편미분과 기울기를 다루었다. 다변수 미분의 본질을 가장 잘 드러내는 관점은 미분을 하나의 *선형사상* — 함수를 한 점 근방에서 가장 잘 근사하는 일차사상 — 으로 보는 것이며, 이것이 한 변수의 "$$f(a+h)\approx f(a)+f'(a)h$$"를 곧바로 일반화한다.

한 변수에서 도함수 $$f'(a)$$는 하나의 수였지만, 그 수가 하는 일은 증분 $$h$$를 받아 함수값의 변화 $$f'(a)h$$를 돌려주는 *곱하기 사상*이다. 변수가 여럿이 되면 입력 $$h \in \mathbb{R}^n$$과 출력 $$f(a+h)-f(a) \in \mathbb{R}^m$$이 모두 벡터이므로, 둘을 잇는 가장 단순한 대응은 더 이상 한 수가 아니라 선형사상이다. 따라서 미분의 올바른 일반화는 "도함수"라는 수가 아니라 $$\mathbb{R}^n$$에서 $$\mathbb{R}^m$$으로 가는 선형사상이며, 이 사상이 함수를 한 점에서 *접*하는 일차 모형을 준다. 이 관점은 정의를 통일할 뿐 아니라, 연쇄법칙을 행렬의 곱으로 환원하고 역함수 정리 같은 깊은 결과로 가는 길을 닦는다.

## 선형사상으로서의 미분

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> $$f : \mathbb{R}^n \to \mathbb{R}^m$$이 점 $$a$$에서 *미분가능<sub>differentiable</sub>*하다는 것은, 선형사상 $$Df(a) : \mathbb{R}^n \to \mathbb{R}^m$$이 존재하여

$$\lim_{h \to 0}\frac{\lVert f(a + h) - f(a) - Df(a)h\rVert}{\lVert h\rVert} = 0$$

이 성립하는 것이다. 이 $$Df(a)$$를 $$f$$의 $$a$$에서의 *(전)미분*이라 한다.

</div>

미분이 선형사상이라는 점이 한 변수와의 본질적 차이이다. 한 변수에서는 그 선형사상이 수 $$f'(a)$$를 곱하는 것이었다. 정의 1의 조건을 풀어 쓰면, 잔차 $$r(h) = f(a+h) - f(a) - Df(a)h$$가 $$\lVert h\rVert$$보다 더 빨리 $$0$$으로 수렴한다는 뜻이다. 즉

$$f(a + h) = f(a) + Df(a)h + r(h), \qquad \frac{\lVert r(h)\rVert}{\lVert h\rVert} \to 0 \;\;(h \to 0)$$

으로, 일차다항식 $$h \mapsto f(a) + Df(a)h$$가 $$f$$를 $$a$$에서 *1차 오차로* 근사한다. 흔히 $$r(h) = o(\lVert h\rVert)$$로 쓰며, "리틀-오" 표기는 $$h \to 0$$일 때 $$\lVert r(h)\rVert/\lVert h\rVert \to 0$$임을 줄인 것이다. 이 근사의 유일성, 즉 두 선형사상이 모두 같은 잔차 조건을 만족하면 서로 같다는 사실은 명제 2에서 야코비 행렬과 함께 따라 나온다.

미분가능하면 연속이라는 가장 기본적인 귀결을 먼저 짚어 둔다. $$h \to 0$$일 때 $$Df(a)h \to 0$$ (선형사상은 연속) 이고 $$r(h) \to 0$$이므로 $$f(a+h) \to f(a)$$이며, 따라서 $$f$$는 $$a$$에서 연속이다. 반면 편미분이 모두 존재해도 함수가 연속조차 아닐 수 있는데, 이는 편미분이 좌표축 방향의 정보만 담는 데 반해 전미분은 모든 방향을 한꺼번에 통제하기 때문이다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> $$f$$가 $$a$$에서 미분가능하면 모든 편미분이 존재하고, $$Df(a)$$를 표준기저로 나타낸 행렬은 야코비 행렬

$$J_f(a) = \left(\frac{\partial f_i}{\partial x_j}(a)\right)_{i,j}$$

이다. 특히 $$Df(a)$$는 유일하다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

정의 1에서 증분 $$h$$를 좌표축 방향 $$h = t e_j$$ ($$t \in \mathbb{R}$$, $$t \to 0$$) 로 제한하자. 이때 $$\lVert h\rVert = \lvert t\rvert$$이므로 잔차 조건은

$$\begin{aligned}
0 &= \lim_{t \to 0} \frac{\lVert f(a + te_j) - f(a) - Df(a)(te_j)\rVert}{\lvert t\rvert} \\
&= \lim_{t \to 0} \left\lVert \frac{f(a + te_j) - f(a)}{t} - Df(a)e_j \right\rVert
\end{aligned}$$

이 되어, 차분비가 벡터 $$Df(a)e_j$$로 수렴한다. 한편 차분비의 $$i$$번째 성분은 정의상 편미분

$$\lim_{t \to 0} \frac{f_i(a + te_j) - f_i(a)}{t} = \frac{\partial f_i}{\partial x_j}(a)$$

이므로, 극한벡터 $$Df(a)e_j$$의 $$i$$번째 성분이 $$\dfrac{\partial f_i}{\partial x_j}(a)$$이다. 즉 모든 편미분이 존재하고, $$Df(a)$$를 표준기저로 나타낸 행렬의 $$j$$번째 열이 $$j$$번째 편미분 벡터 $$\left(\dfrac{\partial f_i}{\partial x_j}(a)\right)_i$$이다. 이로써 그 행렬이 야코비 행렬 $$J_f(a)$$임이 확인된다. 마지막으로 $$Df(a)$$의 모든 열이 $$f$$에 의해 위와 같이 결정되므로 선형사상 $$Df(a)$$ 자체가 유일하다.

</details>

야코비 행렬은 미분이라는 선형사상의 *좌표 표현*일 뿐, 미분 그 자체는 좌표와 무관한 사상임을 강조해 둔다. $$m = 1$$인 실숫값 함수에서는 $$J_f(a)$$가 한 줄짜리 행렬, 곧 기울기벡터 $$\nabla f(a) = \left(\dfrac{\partial f}{\partial x_1}(a), \dots, \dfrac{\partial f}{\partial x_n}(a)\right)$$의 전치이며, $$Df(a)h = \nabla f(a) \cdot h$$로 내적이 된다. 반대로 $$n = 1$$인 곡선 $$\gamma : \mathbb{R} \to \mathbb{R}^m$$에서는 $$J_\gamma(t)$$가 한 열짜리, 곧 속도벡터 $$\gamma'(t)$$이다.

편미분이 모두 존재해도 미분가능성이 따라오지 않는다는 점은 다변수 미분의 미묘함을 단적으로 보여 준다. 가령 $$f(x,y) = \dfrac{xy}{x^2 + y^2}$$ ($$(x,y)\neq(0,0)$$, $$f(0,0)=0$$) 은 원점에서 두 편미분이 모두 $$0$$으로 존재하지만, 직선 $$y=x$$를 따라가면 $$f(x,x) = \tfrac12 \not\to 0$$이어서 연속조차 아니므로 미분가능하지 않다. 편미분은 좌표축 방향만 보는 데 반해 전미분은 모든 방향을 동시에 통제하기 때문이며, 이 간극을 메우는 충분조건이 아래 명제 4이다. 구체적인 야코비 계산의 예는 §예시와 계산에서 더 다룬다.

## 연쇄법칙

선형사상 관점의 진가는 연쇄법칙이 사상의 합성으로 깔끔하게 표현되는 데 있다.

<div class="proposition" markdown="1">

<ins id="thm3">**정리 3 (연쇄법칙)**</ins> $$f$$가 $$a$$에서, $$g$$가 $$b = f(a)$$에서 미분가능하면 $$g \circ f$$가 $$a$$에서 미분가능하고

$$D(g \circ f)(a) = Dg(f(a)) \circ Df(a)$$

이다. 행렬로는 야코비 행렬의 곱 $$J_{g\circ f}(a) = J_g(b)\,J_f(a)$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$A = Df(a)$$, $$B = Dg(b)$$로 두자. 두 함수의 미분가능성에서

$$f(a + h) = b + Ah + r(h), \qquad g(b + k) = g(b) + Bk + s(k)$$

이고 $$r(h) = o(\lVert h\rVert)$$, $$s(k) = o(\lVert k\rVert)$$이다. $$k = Ah + r(h)$$로 두면 $$f(a+h) = b + k$$이므로

$$\begin{aligned}
(g \circ f)(a + h) &= g(b + k) = g(b) + Bk + s(k) \\
&= g(b) + B\bigl(Ah + r(h)\bigr) + s(k) \\
&= (g\circ f)(a) + BA\,h + \underbrace{\bigl(B\,r(h) + s(k)\bigr)}_{=: \,\rho(h)}
\end{aligned}$$

가 된다. 남은 일은 잔차 $$\rho(h) = B\,r(h) + s(k)$$가 $$o(\lVert h\rVert)$$임을 보이는 것이다. 첫 항은 $$B$$가 선형사상이므로 어떤 상수 $$C$$에 대해 $$\lVert B\,r(h)\rVert \le C\,\lVert r(h)\rVert = o(\lVert h\rVert)$$이다. 둘째 항은, 먼저 $$k = Ah + r(h)$$가 $$\lVert k\rVert \le \lVert A\rVert\,\lVert h\rVert + \lVert r(h)\rVert \le C'\lVert h\rVert$$ ($$h$$가 충분히 작을 때) 로 $$\lVert h\rVert$$ 정도의 크기임에 주의한다. 그러면

$$\frac{\lVert s(k)\rVert}{\lVert h\rVert} = \frac{\lVert s(k)\rVert}{\lVert k\rVert}\cdot \frac{\lVert k\rVert}{\lVert h\rVert} \le \frac{\lVert s(k)\rVert}{\lVert k\rVert}\cdot C'$$

인데, $$h \to 0$$이면 $$k \to 0$$이므로 $$\lVert s(k)\rVert/\lVert k\rVert \to 0$$ (단 $$k = 0$$인 경우 $$s(k) = 0$$로 처리) 이고, 따라서 우변이 $$0$$으로 간다. 두 항을 합쳐 $$\rho(h) = o(\lVert h\rVert)$$이므로 정의 1에 의해 $$g\circ f$$는 $$a$$에서 미분가능하고 $$D(g\circ f)(a) = BA = Dg(b)\circ Df(a)$$이다.

</details>

행렬로 옮기면 연쇄법칙은 야코비 행렬의 곱셈이 된다. 성분으로 풀어 쓰면, $$g\circ f$$의 $$i$$행 $$j$$열 성분이

$$\frac{\partial (g\circ f)_i}{\partial x_j}(a) = \sum_{k} \frac{\partial g_i}{\partial y_k}(b)\,\frac{\partial f_k}{\partial x_j}(a)$$

라는 익숙한 합 꼴이며, 이는 행렬곱 $$J_g(b)J_f(a)$$의 $$(i,j)$$ 성분에 다름 아니다. 선형사상 합성의 행렬이 행렬곱이라는 선형대수의 사실 덕분에, 일변수 연쇄법칙의 한 줄 공식이 다변수에서 행렬곱 한 줄로 그대로 살아남는다. 연쇄법칙의 가장 흔한 특수경우는 곡선을 따른 변화율로, 아래 §예시와 계산의 예시 7에서 별도로 다룬다.

## 연속미분가능성

편미분의 존재만으로는 미분가능성이 보장되지 않지만, 편미분이 연속이면 충분하다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> $$f$$의 모든 편미분이 $$a$$ 근방에서 존재하고 $$a$$에서 연속이면 ($$f$$가 $$C^1$$이면), $$f$$는 $$a$$에서 미분가능하다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

실숫값($$m=1$$)인 경우를 보이면 충분하다 (성분별로 적용하면 일반 $$m$$이 따른다). 증분 $$h = (h_1, \dots, h_n)$$을 한 좌표씩 켜며 차를 망원합으로 분해한다. $$a^{(0)} = a$$, $$a^{(j)} = a + (h_1, \dots, h_j, 0, \dots, 0)$$로 두면

$$f(a + h) - f(a) = \sum_{j=1}^n \bigl(f(a^{(j)}) - f(a^{(j-1)})\bigr)$$

이다. $$a^{(j)}$$와 $$a^{(j-1)}$$는 $$j$$번째 좌표만 $$h_j$$만큼 다르므로, 각 차에 한 변수 평균값 정리 ([§평균값 정리와 테일러 정리, ⁋정리 3](/ko/math/analysis/mean_value_theorem#thm3))를 적용하면 $$a^{(j-1)}$$와 $$a^{(j)}$$ 사이의 어떤 점 $$\xi_j$$에 대해

$$f(a^{(j)}) - f(a^{(j-1)}) = \frac{\partial f}{\partial x_j}(\xi_j)\,h_j$$

이다. 이를 모아 빼고 더하면

$$\begin{aligned}
f(a + h) - f(a) - \sum_{j=1}^n \frac{\partial f}{\partial x_j}(a)\,h_j
&= \sum_{j=1}^n \left( \frac{\partial f}{\partial x_j}(\xi_j) - \frac{\partial f}{\partial x_j}(a) \right) h_j
\end{aligned}$$

가 된다. $$\lvert h_j\rvert \le \lVert h\rVert$$이므로 코시–슈바르츠 부등식 또는 단순한 크기 비교로

$$\frac{\left\lvert f(a + h) - f(a) - \sum_j \tfrac{\partial f}{\partial x_j}(a)h_j \right\rvert}{\lVert h\rVert} \le \sum_{j=1}^n \left\lvert \frac{\partial f}{\partial x_j}(\xi_j) - \frac{\partial f}{\partial x_j}(a) \right\rvert$$

이다. 한편 $$h \to 0$$이면 모든 $$\xi_j \to a$$이고, 편미분 $$\dfrac{\partial f}{\partial x_j}$$가 $$a$$에서 연속이므로 우변의 각 항이 $$0$$으로 간다. 따라서 좌변도 $$0$$으로 가며, 이는 선형사상 $$h \mapsto \sum_j \dfrac{\partial f}{\partial x_j}(a)h_j$$가 곧 $$Df(a)$$임을 — 즉 $$f$$가 $$a$$에서 미분가능함을 — 뜻한다.

</details>

명제 4의 조건은 충분조건일 뿐 필요조건은 아니다. 미분가능하지만 편미분이 불연속인 함수가 존재하므로, "$$C^1$$"은 미분가능성보다 진정으로 강하다. 그럼에도 실제로 마주치는 거의 모든 함수 — 다항식, 유리식, 지수·삼각함수의 합성 — 는 정의역에서 $$C^1$$이며, 따라서 야코비 행렬을 적는 것만으로 미분가능성이 보장된다. 이 점이 명제 4를 계산에서 가장 자주 쓰는 판정 도구로 만든다.

<div class="example" markdown="1">

<ins id="ex5">**예시 5 (미분가능하나 $$C^1$$이 아닌 함수)**</ins> $$f : \mathbb{R} \to \mathbb{R}$$를

$$f(x) = \begin{cases} x^2 \sin\dfrac{1}{x}, & x \neq 0, \\ 0, & x = 0 \end{cases}$$

로 두자. $$x \neq 0$$에서 곱·연쇄법칙으로 $$f'(x) = 2x\sin\dfrac1x - \cos\dfrac1x$$이고, $$x = 0$$에서는

$$f'(0) = \lim_{t\to 0}\frac{t^2\sin(1/t)}{t} = \lim_{t\to 0} t\sin\frac1t = 0$$

이므로 $$f$$는 모든 점에서 미분가능하다. 그러나 $$x \to 0$$일 때 $$f'(x)$$의 $$-\cos\dfrac1x$$ 항이 진동하여 극한이 없으므로 $$f'$$는 $$0$$에서 불연속이다. 즉 미분가능성이 도함수의 연속성을 함의하지 않으며, 명제 4의 역이 거짓임을 보인다.

</div>

명제 4 덕분에 야코비 행렬을 적기만 하면 미분가능성이 보장되는 경우가 대부분이다. 다음 두 예시는 그렇게 얻은 야코비 행렬과 연쇄법칙의 전형적인 쓰임이다.

<div class="example" markdown="1">

<ins id="ex6">**예시 6 (야코비 행렬의 계산)**</ins> $$f : \mathbb{R}^2 \to \mathbb{R}^2$$를 극좌표 변환

$$f(r, \theta) = (r\cos\theta,\ r\sin\theta)$$

로 두자. 성분들이 모두 $$C^1$$이므로 $$f$$는 미분가능하고, 각 성분의 편미분을 모으면 야코비 행렬은

$$J_f(r, \theta) = \begin{pmatrix} \dfrac{\partial}{\partial r}(r\cos\theta) & \dfrac{\partial}{\partial \theta}(r\cos\theta) \\[2mm] \dfrac{\partial}{\partial r}(r\sin\theta) & \dfrac{\partial}{\partial \theta}(r\sin\theta) \end{pmatrix} = \begin{pmatrix} \cos\theta & -r\sin\theta \\ \sin\theta & r\cos\theta \end{pmatrix}$$

이다. 그 행렬식은

$$\det J_f(r,\theta) = \cos\theta \cdot r\cos\theta - (-r\sin\theta)\cdot \sin\theta = r(\cos^2\theta + \sin^2\theta) = r$$

로, 극좌표 적분에서 등장하는 면적 배율 $$r$$가 정확히 미분의 행렬식임을 보여 준다.

</div>

<div class="example" markdown="1">

<ins id="ex7">**예시 7 (곡선을 따른 변화율)**</ins> $$g : \mathbb{R}^n \to \mathbb{R}$$가 미분가능하고 $$\gamma : \mathbb{R} \to \mathbb{R}^n$$이 미분가능한 곡선일 때, 합성 $$t \mapsto g(\gamma(t))$$의 변화율을 구하자. 연쇄법칙에서 $$Dg(\gamma(t))$$는 $$1 \times n$$ 행렬 (기울기) 이고 $$D\gamma(t)$$는 $$n \times 1$$ 행렬 (속도) 이므로

$$\frac{d}{dt}\,g(\gamma(t)) = Dg(\gamma(t))\,\gamma'(t) = \sum_{j=1}^n \frac{\partial g}{\partial x_j}(\gamma(t))\,\gamma_j'(t) = \nabla g(\gamma(t)) \cdot \gamma'(t)$$

이다. 특히 $$\gamma(t) = a + t v$$인 직선을 넣으면 $$\gamma'(t) = v$$이므로 $$t = 0$$에서 $$\dfrac{d}{dt}\Big\vert_{t=0} g(a + tv) = \nabla g(a)\cdot v$$, 곧 방향 $$v$$로의 방향도함수가 기울기와 $$v$$의 내적임을 얻는다.

</div>

## 평균값 정리와 응용

일변수에서 평균값 정리는 $$f(b) - f(a) = f'(\xi)(b-a)$$라는 등식이었다. 다변수 실숫값 함수에서도 같은 형태가 살아남으며, 이것이 명제 4의 증명에서 본 분해의 일반적 형태이다.

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8 (다변수 평균값 정리)**</ins> $$f : \mathbb{R}^n \to \mathbb{R}$$이 선분 $$[a, a+h] = \{a + th : 0 \le t \le 1\}$$ 위의 모든 점에서 미분가능하면, 어떤 $$\theta \in (0,1)$$가 존재하여

$$f(a + h) - f(a) = \nabla f(a + \theta h)\cdot h$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

보조함수 $$\varphi : [0,1] \to \mathbb{R}$$를 $$\varphi(t) = f(a + th)$$로 두자. $$\gamma(t) = a + th$$는 미분가능하고 $$\gamma'(t) = h$$이므로, 예시 7의 연쇄법칙에 의해 $$\varphi$$는 미분가능하고

$$\varphi'(t) = \nabla f(a + th)\cdot h$$

이다. 한 변수 평균값 정리 ([§평균값 정리와 테일러 정리, ⁋정리 3](/ko/math/analysis/mean_value_theorem#thm3))를 $$\varphi$$에 적용하면 어떤 $$\theta \in (0,1)$$에 대해

$$\varphi(1) - \varphi(0) = \varphi'(\theta)$$

인데, 좌변은 $$f(a+h) - f(a)$$이고 우변은 $$\nabla f(a+\theta h)\cdot h$$이므로 주장이 따른다.

</details>

벡터값 함수($$m \ge 2$$)에서는 이 등식이 성립하지 않음에 유의한다. 가령 $$\gamma(t) = (\cos t, \sin t)$$는 $$\gamma(2\pi) - \gamma(0) = 0$$이지만 $$\gamma'(t) = (-\sin t, \cos t)$$는 결코 $$0$$이 아니어서, 좌변을 한 점에서의 미분으로 표현할 수 없다. 대신 노름에 대한 부등식 형태가 살아남는데, 이로부터 다음 따름정리를 얻는다.

<div class="proposition" markdown="1">

<ins id="cor9">**따름정리 9**</ins> 볼록 집합 $$U$$ 위에서 $$f : U \to \mathbb{R}$$가 미분가능하고 $$\nabla f \equiv 0$$이면, $$f$$는 $$U$$에서 상수이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$U$$의 임의의 두 점 $$a, a+h$$를 잡으면, $$U$$가 볼록이므로 선분 $$[a, a+h]$$가 $$U$$에 들어 있다. 명제 8을 적용하면 어떤 $$\theta \in (0,1)$$에 대해

$$f(a + h) - f(a) = \nabla f(a + \theta h)\cdot h = 0 \cdot h = 0$$

이므로 $$f(a+h) = f(a)$$이다. 두 점이 임의였으므로 $$f$$는 $$U$$에서 상수이다.

</details>

이 따름정리는 일변수에서 "도함수가 $$0$$이면 상수"라는 사실의 다변수 판본으로, 두 함수의 기울기가 같으면 둘이 상수 차이임을 — 따라서 퍼텐셜이 상수배까지 유일함을 — 보장한다.

## 예시와 계산

<div class="example" markdown="1">

<ins id="ex10">**예시 10 (선형사상과 이차형식의 미분)**</ins> 두 가지 기본적인 함수의 미분을 계산하자. 먼저 선형사상 $$L : \mathbb{R}^n \to \mathbb{R}^m$$, 곧 $$L(x) = Mx$$ ($$M$$은 상수 행렬) 의 경우

$$L(a + h) - L(a) = M(a+h) - Ma = Mh$$

이므로 잔차가 정확히 $$0$$이고, 따라서 $$DL(a) = M$$이 모든 $$a$$에서 성립한다. 즉 선형사상의 미분은 자기 자신이다. 다음으로 이차형식 $$q(x) = x^\top M x$$ ($$M$$은 대칭) 의 경우

$$\begin{aligned}
q(a + h) - q(a) &= (a+h)^\top M (a+h) - a^\top M a \\
&= a^\top M h + h^\top M a + h^\top M h \\
&= 2\,a^\top M h + h^\top M h
\end{aligned}$$

이고, $$h^\top M h = O(\lVert h\rVert^2) = o(\lVert h\rVert)$$이므로 $$Dq(a)h = 2\,a^\top M h$$, 곧 $$\nabla q(a) = 2Ma$$이다. $$M = I$$이면 $$q(x) = \lVert x\rVert^2$$이고 $$\nabla q(a) = 2a$$로, 익숙한 결과를 회복한다.

</div>

<div class="example" markdown="1">

<ins id="ex11">**예시 11 (연쇄법칙으로 합성 야코비 계산)**</ins> $$f : \mathbb{R}^2 \to \mathbb{R}^2$$를 $$f(x, y) = (x^2 - y^2,\ 2xy)$$, $$g : \mathbb{R}^2 \to \mathbb{R}$$를 $$g(u, v) = u^2 + v^2$$로 두고 $$g \circ f$$의 야코비를 두 방법으로 구하자. 두 야코비는

$$J_f(x, y) = \begin{pmatrix} 2x & -2y \\ 2y & 2x \end{pmatrix}, \qquad J_g(u, v) = \begin{pmatrix} 2u & 2v \end{pmatrix}$$

이고, $$b = f(x,y) = (x^2 - y^2, 2xy)$$에서 평가한 뒤 연쇄법칙으로 곱하면

$$\begin{aligned}
J_{g\circ f}(x,y) &= J_g(b)\,J_f(x,y) \\
&= \begin{pmatrix} 2(x^2 - y^2) & 2(2xy) \end{pmatrix} \begin{pmatrix} 2x & -2y \\ 2y & 2x \end{pmatrix} \\
&= \begin{pmatrix} 4x(x^2 - y^2) + 8xy^2 & -4y(x^2 - y^2) + 8x^2 y \end{pmatrix} \\
&= \begin{pmatrix} 4x(x^2 + y^2) & 4y(x^2 + y^2) \end{pmatrix}.
\end{aligned}$$

직접 합성하면 $$(g\circ f)(x,y) = (x^2 - y^2)^2 + (2xy)^2 = (x^2 + y^2)^2$$이고, 이를 미분하면 $$\dfrac{\partial}{\partial x}(x^2+y^2)^2 = 4x(x^2+y^2)$$, $$\dfrac{\partial}{\partial y}(x^2+y^2)^2 = 4y(x^2+y^2)$$로 두 결과가 일치한다.

</div>

미분을 선형사상으로 보는 이 관점은 미분이 가역일 때 함수 자신이 국소적으로 가역이라는 강력한 결론으로 이어진다. 이것이 다음 글 [§역함수 정리와 음함수 정리](/ko/math/analysis/inverse_function_theorem)의 주제이다.
