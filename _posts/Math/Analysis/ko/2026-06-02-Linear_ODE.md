---
title: "선형 미분방정식계"
description: "선형 미분방정식계의 해가 구간 전체에서 전역적으로 존재하고 유일함을 보인다. 상수계수 선형계의 해를 행렬지수로 표현하고, 그 계산이 계수행렬의 고윳값 구조로 환원됨을 본다."
excerpt: "선형계의 전역 존재유일성, 행렬지수, 고윳값과 해"

categories: [Math / Analysis]
permalink: /ko/math/analysis/linear_ode
sidebar: 
    nav: "analysis-ko"

date: 2026-06-02
weight: 22

published: false
---

[§미분방정식의 존재성과 유일성](/ko/math/analysis/existence_uniqueness_ode)에서 립시츠 조건 아래 해가 국소적으로 존재함을 보았다. 미분방정식 가운데 가장 잘 이해된 부류가 선형계이며, 여기서는 해가 전역적으로 존재할 뿐 아니라 선형대수로 명시적으로 풀린다. 이로써 해석학의 미분방정식 이론이 선형대수와 만난다.

## 선형계의 전역 존재유일성

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> $$n$$차 벡터값 함수 $$y(t) \in \mathbb{R}^n$$에 대한 *선형 미분방정식계*는

$$y'(t) = A(t)\,y(t) + b(t)$$

꼴이다. 여기서 $$A(t)$$는 $$n\times n$$ 행렬값, $$b(t)$$는 벡터값 연속함수이다. $$b \equiv 0$$이면 *제차*라 한다.

</div>

<div class="proposition" markdown="1">

<ins id="thm2">**정리 2**</ins> $$A(t), b(t)$$가 구간 $$I$$에서 연속이면, 임의의 초기 조건 $$y(t_0) = y_0$$에 대한 해가 $$I$$ 전체에서 유일하게 존재한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

우변을 $$f(t, y) = A(t)y + b(t)$$로 두면, 두 벡터 $$y_1, y_2$$에 대해 $$b(t)$$ 항이 상쇄되어

$$\begin{aligned}
\lvert f(t, y_1) - f(t, y_2)\rvert &= \lvert A(t)y_1 - A(t)y_2\rvert \\
&= \lvert A(t)(y_1 - y_2)\rvert \\
&\leq \lVert A(t)\rVert\,\lvert y_1 - y_2\rvert
\end{aligned}$$

이 성립한다. 여기서 $$\lVert A(t)\rVert$$은 행렬의 작용소노름이다. $$A(t)$$의 각 성분이 $$I$$에서 연속이므로 $$t \mapsto \lVert A(t)\rVert$$도 연속이고, 따라서 $$I$$의 임의의 컴팩트 부분구간에서 유계이다 ([§연속함수의 성질, ⁋따름정리 2](/ko/math/analysis/continuous_functions#cor2)). 그 유계값을 립시츠 상수로 삼으면 $$f$$는 $$y$$에 대해 균일하게 립시츠 조건을 만족하므로, 피카르–린델뢰프 정리 ([§미분방정식의 존재성과 유일성, ⁋정리 4](/ko/math/analysis/existence_uniqueness_ode#thm4))에 의해 국소해가 존재한다.

전역으로의 확장이 핵심인데, 비선형의 경우와 달리 립시츠 상수가 해의 크기 $$\lvert y\rvert$$에 전혀 의존하지 않는다는 점이 결정적이다. 실제로 해가 존재하는 구간에서 $$\lvert y(t)\rvert$$의 성장은

$$\frac{d}{dt}\lvert y\rvert \leq \lvert y'\rvert = \lvert A(t)y + b(t)\rvert \leq \lVert A(t)\rVert\,\lvert y\rvert + \lvert b(t)\rvert$$

로 통제되고, 그뢴발 부등식을 적용하면 $$\lvert y(t)\rvert$$이 컴팩트 부분구간에서 유계로 머문다. 따라서 해가 구간의 끝점으로 다가가도 발산하지 않으므로 $$I$$ 전체로 연장된다.

</details>

비선형 방정식의 해가 유한 시간에 발산할 수 있는 것과 달리, 선형계의 해는 계수가 정의된 구간 전체에 걸쳐 존재한다. 가령 스칼라 방정식 $$y' = y^2$$, $$y(0) = 1$$은 $$y(t) = 1/(1-t)$$이라 $$t \to 1^-$$에서 폭발하지만, 이는 우변 $$y^2$$의 립시츠 상수가 $$\lvert y\rvert$$에 따라 무한히 커지는 비선형성 때문이다. 선형계에서는 이런 일이 원천적으로 일어나지 않는다.

## 행렬지수와 상수계수 해

$$A$$가 상수행렬인 제차계 $$y' = Ay$$는 한 변수 지수함수의 직접적 일반화로 풀린다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> $$n\times n$$ 행렬 $$A$$의 *행렬지수<sub>matrix exponential</sub>*를

$$e^{A} = \sum_{k=0}^{\infty}\frac{A^k}{k!} = I + A + \frac{A^2}{2!} + \cdots$$

으로 정의한다. 이 급수는 모든 $$A$$에 대해 (성분별로) 절대수렴한다.

</div>

급수의 수렴은 부분합이 코시열을 이룸을 보이면 된다. 작용소노름이 곱에 대해 $$\lVert A^k\rVert \leq \lVert A\rVert^k$$로 열등승법적이므로

$$\left\lVert \frac{A^k}{k!}\right\rVert \leq \frac{\lVert A\rVert^k}{k!}$$

이고, 우변의 합 $$\sum_k \lVert A\rVert^k/k! = e^{\lVert A\rVert}$$이 수렴하는 스칼라 급수이다. 따라서 바이어슈트라스 M-판정 ([§균등수렴, ⁋정리 4](/ko/math/analysis/uniform_convergence#thm4))에 의해 행렬급수가 (성분별로, 그리고 노름에서) 절대수렴하며, $$\lVert e^A\rVert \leq e^{\lVert A\rVert}$$이라는 유용한 부등식도 함께 얻는다.

행렬지수는 스칼라 지수의 여러 성질을 그대로 물려받지만, 한 가지 중요한 예외가 있다. $$A$$와 $$B$$가 *교환할 때*, 즉 $$AB = BA$$일 때에만

$$e^{A + B} = e^A e^B$$

가 성립한다. 일반적으로는 $$AB \neq BA$$이면 이 등식이 깨진다. 이 사실에서 $$e^A$$가 항상 가역이며 그 역이 $$e^{-A}$$임이 따라 나오는데, $$A$$와 $$-A$$는 언제나 교환하므로 $$e^A e^{-A} = e^{A - A} = e^0 = I$$이기 때문이다. 또 한 매개변수족 $$t \mapsto e^{tA}$$는 $$e^{(s+t)A} = e^{sA}e^{tA}$$를 만족해 가역행렬들의 곱셈군 안에서 일매개변수부분군을 이룬다.

행렬지수를 멱급수로 항별 미분하면

$$\frac{d}{dt}e^{tA} = \frac{d}{dt}\sum_{k=0}^\infty \frac{t^k A^k}{k!} = \sum_{k=1}^\infty \frac{t^{k-1}A^k}{(k-1)!} = A\sum_{j=0}^\infty \frac{t^j A^j}{j!} = A\,e^{tA}$$

이므로 (항별 미분의 정당성은 멱급수의 균등수렴에서 나온다) 다음을 얻는다.

<div class="proposition" markdown="1">

<ins id="thm4">**정리 4**</ins> 상수계수 제차계 $$y' = Ay$$, $$y(0) = y_0$$의 유일한 해는

$$y(t) = e^{tA}\,y_0$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$y(t) = e^{tA}y_0$$이 해가 됨을 직접 확인한다. 초기 조건은

$$y(0) = e^{0\cdot A}\,y_0 = I\,y_0 = y_0$$

으로 성립하고, 앞서 구한 미분 공식 $$\dfrac{d}{dt}e^{tA} = A e^{tA}$$를 쓰면

$$y'(t) = \frac{d}{dt}\bigl(e^{tA}y_0\bigr) = A e^{tA}y_0 = A\,y(t)$$

이므로 $$y' = Ay$$를 만족한다. 따라서 $$y(t) = e^{tA}y_0$$은 해이며, 상수계수계도 정리 2의 가정($$A(t) \equiv A$$가 연속, $$b \equiv 0$$)을 충족하므로 그 유일성에 의해 이것이 유일한 해이다.

</details>

## 고윳값을 통한 계산

행렬지수 $$e^{tA}$$를 무한급수로 직접 더하는 일은 실용적이지 않다. 다행히 그 계산은 $$A$$의 고유구조로 완전히 환원된다. $$A$$가 고윳값 $$\lambda$$와 고유벡터 $$v$$를 가지면 $$A v = \lambda v$$, $$A^k v = \lambda^k v$$이므로

$$e^{tA}v = \sum_{k=0}^\infty \frac{t^k A^k}{k!}v = \sum_{k=0}^\infty \frac{t^k \lambda^k}{k!}v = e^{\lambda t}\,v$$

가 되어, $$y(t) = e^{\lambda t}v$$가 곧 해이다. 즉 고유벡터 방향으로는 행렬지수가 스칼라 지수로 단순화된다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> $$A$$가 대각화되어 $$A = P D P^{-1}$$ ($$D = \diag(\lambda_1, \dots, \lambda_n)$$) 이면

$$e^{tA} = P\,e^{tD}\,P^{-1}, \qquad e^{tD} = \diag\bigl(e^{\lambda_1 t}, \dots, e^{\lambda_n t}\bigr)$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$A^k = (PDP^{-1})^k = P D^k P^{-1}$$이므로 (중간의 $$P^{-1}P$$가 모두 상쇄된다) 급수에 넣으면

$$\begin{aligned}
e^{tA} &= \sum_{k=0}^\infty \frac{t^k A^k}{k!} = \sum_{k=0}^\infty \frac{t^k P D^k P^{-1}}{k!} \\
&= P\left(\sum_{k=0}^\infty \frac{t^k D^k}{k!}\right)P^{-1} = P\,e^{tD}\,P^{-1}
\end{aligned}$$

이다. 대각행렬의 거듭제곱은 성분별 거듭제곱이므로 $$D^k = \diag(\lambda_1^k, \dots, \lambda_n^k)$$이고, 따라서 $$e^{tD}$$의 $$i$$번째 대각성분은 $$\sum_k t^k\lambda_i^k/k! = e^{\lambda_i t}$$이다.

</details>

따라서 $$A$$가 대각화되면 — 고유벡터들이 기저를 이루면 — 해는 $$e^{\lambda_i t}$$ 꼴의 항들의 선형결합으로 명시적으로 적힌다. 구체적으로 초기값 $$y_0$$을 고유벡터 기저로 $$y_0 = \sum_i c_i v_i$$로 전개하면

$$y(t) = e^{tA}y_0 = \sum_{i=1}^n c_i\,e^{\lambda_i t}\,v_i$$

가 되어, 각 고유모드가 자신의 고윳값에 따라 독립적으로 지수증감한다.

## 예시와 계산

가장 단순한 경우부터 차례로 계산해 본다. 먼저 고윳값이 실수이고 서로 다른 대각화 가능한 경우이다.

<div class="example" markdown="1">

<ins id="ex6">**예시 6 (실수 고윳값)**</ins> $$A = \begin{pmatrix} 1 & 1 \\ 0 & 2 \end{pmatrix}$$의 고윳값은 $$\lambda_1 = 1$$, $$\lambda_2 = 2$$이고, 대응하는 고유벡터는 각각 $$v_1 = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$$, $$v_2 = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$$이다. 명제 5에 따라

$$e^{tA} = P\begin{pmatrix} e^{t} & 0 \\ 0 & e^{2t} \end{pmatrix}P^{-1}, \qquad P = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix},\ \ P^{-1} = \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix}$$

이다. 곱을 전개하면

$$\begin{aligned}
e^{tA} &= \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}\begin{pmatrix} e^{t} & 0 \\ 0 & e^{2t} \end{pmatrix}\begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix} \\
&= \begin{pmatrix} e^{t} & e^{2t} \\ 0 & e^{2t} \end{pmatrix}\begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix} \\
&= \begin{pmatrix} e^{t} & e^{2t} - e^{t} \\ 0 & e^{2t} \end{pmatrix}
\end{aligned}$$

을 얻는다. 가령 $$y(0) = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$$이면 $$y(t) = e^{tA}y(0) = \begin{pmatrix} e^{2t} \\ e^{2t} \end{pmatrix}$$이다.

</div>

다음은 고윳값이 켤레복소수쌍인 경우로, 오일러 공식을 통해 해가 진동(삼각함수)으로 나타남을 본다.

<div class="example" markdown="1">

<ins id="ex7">**예시 7 (복소 고윳값과 진동)**</ins> 회전형 행렬 $$A = \begin{pmatrix} 0 & -\omega \\ \omega & 0 \end{pmatrix}$$ ($$\omega > 0$$) 의 고윳값은 $$\lambda = \pm i\omega$$로 순허수이다. 거듭제곱을 계산하면 $$A^2 = -\omega^2 I$$이므로

$$\begin{aligned}
e^{tA} &= \sum_{k=0}^\infty \frac{t^k A^k}{k!} = \left(\sum_{m=0}^\infty \frac{(-1)^m (\omega t)^{2m}}{(2m)!}\right)I + \left(\sum_{m=0}^\infty \frac{(-1)^m (\omega t)^{2m+1}}{(2m+1)!}\right)\frac{A}{\omega} \\
&= \cos(\omega t)\,I + \sin(\omega t)\,\frac{A}{\omega} \\
&= \begin{pmatrix} \cos\omega t & -\sin\omega t \\ \sin\omega t & \cos\omega t \end{pmatrix}
\end{aligned}$$

가 되어, $$e^{tA}$$가 각속도 $$\omega$$의 회전행렬임을 본다. 해 $$y(t) = e^{tA}y_0$$은 원점을 중심으로 일정한 반지름 $$\lvert y_0\rvert$$로 도는 원운동이다. 이는 단진동 방정식 $$u'' + \omega^2 u = 0$$을 일차계 $$y = (u, u')$$로 환원한 형태이며, 고윳값의 허수부 $$\omega$$가 진동의 각진동수임을 보여 준다.

</div>

대각화되지 않는 경우, 즉 고유벡터가 기저를 이루지 못하는 *결손<sub>defective</sub>* 행렬에서는 조르당 표준형을 써야 하고, 그 결과 $$t^j e^{\lambda t}$$ 꼴의 다항식 인자가 등장한다.

<div class="example" markdown="1">

<ins id="ex8">**예시 8 (결손 행렬과 조르당 블록)**</ins> $$A = \begin{pmatrix} \lambda & 1 \\ 0 & \lambda \end{pmatrix}$$는 고윳값 $$\lambda$$를 중복으로 가지나 고유벡터가 일차원뿐이라 대각화되지 않는다. $$A = \lambda I + N$$, $$N = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$$로 쓰면 $$\lambda I$$와 $$N$$이 교환하고 $$N^2 = 0$$이므로

$$\begin{aligned}
e^{tA} &= e^{t\lambda I}\,e^{tN} = e^{\lambda t}I\cdot\bigl(I + tN\bigr) \\
&= e^{\lambda t}\begin{pmatrix} 1 & t \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} e^{\lambda t} & t\,e^{\lambda t} \\ 0 & e^{\lambda t} \end{pmatrix}
\end{aligned}$$

이다. 멱영부분 $$N$$ 때문에 급수가 유한항에서 끊겨 $$e^{tN} = I + tN$$이 되고, 그 결과 비대각 성분에 $$t\,e^{\lambda t}$$라는 다항식 곱하기 지수 항이 나타난다. 이것이 일반적으로 결손 고윳값이 해에 $$t^j e^{\lambda t}$$ 꼴을 들여오는 메커니즘이다.

</div>

## 비제차계와 매개변수변환

이제 $$b(t) \neq 0$$인 비제차계로 돌아간다. 제차계의 행렬지수를 알면 비제차계의 해도 적분으로 닫힌 형태로 적을 수 있다.

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9 (매개변수변환 공식)**</ins> 상수계수 비제차계 $$y' = Ay + b(t)$$, $$y(t_0) = y_0$$의 유일한 해는

$$y(t) = e^{(t - t_0)A}\,y_0 + \int_{t_0}^{t} e^{(t - s)A}\,b(s)\,ds$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

핵심 착상은 *적분인자* $$e^{-tA}$$를 곱하는 것이다. $$y' - Ay = b(t)$$의 양변에 $$e^{-tA}$$를 왼쪽에서 곱하면, 좌변이 완전미분이 됨을 확인할 수 있다:

$$\begin{aligned}
\frac{d}{dt}\bigl(e^{-tA}y\bigr) &= -A e^{-tA}y + e^{-tA}y' = e^{-tA}\bigl(y' - Ay\bigr) = e^{-tA}b(t).
\end{aligned}$$

여기서 $$\dfrac{d}{dt}e^{-tA} = -A e^{-tA}$$를 썼다. 이제 양변을 $$t_0$$에서 $$t$$까지 적분하면

$$e^{-tA}y(t) - e^{-t_0 A}y_0 = \int_{t_0}^t e^{-sA}b(s)\,ds$$

이고, 양변에 왼쪽에서 $$e^{tA}$$를 곱한 뒤 $$e^{tA}e^{-t_0 A} = e^{(t-t_0)A}$$, $$e^{tA}e^{-sA} = e^{(t-s)A}$$ ($$tA$$와 $$-sA$$가 교환하므로) 를 쓰면 주어진 공식을 얻는다.

</details>

우변의 첫 항 $$e^{(t-t_0)A}y_0$$은 제차해(초기조건을 나르는 부분)이고, 적분항은 강제항 $$b(s)$$가 $$s$$ 시점부터 $$t$$까지 행렬지수로 전파되어 누적된 *특수해*이다. 이는 스칼라 일차방정식 $$y' = ay + b(t)$$의 적분인자 풀이를 행렬로 그대로 들어올린 것이다.

<div class="example" markdown="1">

<ins id="ex10">**예시 10 (강제항이 있는 계)**</ins> 스칼라 방정식 $$y' = -y + e^{-t}$$, $$y(0) = 0$$을 명제 9로 풀자. $$A = -1$$, $$b(s) = e^{-s}$$, $$t_0 = 0$$이므로 $$e^{(t-s)A} = e^{-(t-s)}$$이고

$$\begin{aligned}
y(t) &= e^{-t}\cdot 0 + \int_0^t e^{-(t-s)}\,e^{-s}\,ds \\
&= \int_0^t e^{-t}\,ds = e^{-t}\int_0^t ds = t\,e^{-t}
\end{aligned}$$

이다. 강제항이 제차해 $$e^{-t}$$와 *공명*하여 (지수가 일치하여) 해에 $$t\,e^{-t}$$라는 다항식 인자가 생기는 전형적인 예이다. 직접 미분으로 검산하면 $$y'(t) = e^{-t} - t e^{-t} = -y + e^{-t}$$이고 $$y(0) = 0$$임을 확인할 수 있다.

</div>

마지막으로, 고윳값의 실수부가 해의 장기거동을 어떻게 지배하는지를 정리해 둔다.

<div class="proposition" markdown="1">

<ins id="prop11">**명제 11 (점근적 안정성)**</ins> 상수계수 제차계 $$y' = Ay$$에서 $$A$$의 모든 고윳값 $$\lambda$$가 $$\Real\lambda < 0$$을 만족하면, 모든 해는 $$t \to \infty$$에서 $$y(t) \to 0$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

조르당 표준형으로 $$e^{tA}$$의 각 성분은 유한 개의 $$t^j e^{\lambda t}$$ 꼴 항의 합이며, 여기서 $$\lambda$$는 고윳값, $$j$$는 해당 조르당 블록 크기 미만의 음이 아닌 정수이다. 각 항의 크기는

$$\lvert t^j e^{\lambda t}\rvert = t^j e^{(\Real\lambda)\,t}$$

인데, 가정에서 $$\Real\lambda < 0$$이므로 지수의 감쇠가 다항식 $$t^j$$의 증가를 압도하여 $$t \to \infty$$에서 $$0$$으로 간다. 따라서 $$e^{tA} \to 0$$이고, 임의의 $$y_0$$에 대해 $$y(t) = e^{tA}y_0 \to 0$$이다.

</details>

대칭적으로, 어떤 고윳값이 $$\Real\lambda > 0$$이면 그 모드를 따라 해가 지수적으로 발산하고, 고윳값이 모두 순허수이면 예시 7처럼 해가 진동하며 유계로 머문다. 이렇게 평형 $$y = 0$$의 안정·불안정·중립 거동이 고윳값의 실수부 부호로 한꺼번에 읽힌다.

이렇게 선형 미분방정식의 풀이는 행렬의 고윳값·고유벡터 — 곧 선형사상의 스펙트럼 구조 ([\[다중선형대수학\] §행렬과 선형사상](/ko/math/multilinear_algebra/matrices_and_linear_maps)) — 로 완전히 귀착된다. 미분방정식의 해의 정성적 거동(평형의 안정성, 진동, 발산)이 고윳값의 실수부와 허수부로 읽힌다는 사실은 동역학계 이론의 출발점이며, 해석학·선형대수·기하가 만나는 지점이다.
