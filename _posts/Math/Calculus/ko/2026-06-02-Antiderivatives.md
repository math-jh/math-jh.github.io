---
title: "부정적분"
description: "미분의 역연산인 부정적분(원시함수)을 정의하고, 두 원시함수가 상수 차이로만 다름을 평균값 정리로부터 보인다. 기본 함수들의 부정적분과 선형성, 추측에 의한 적분, 초기조건, 비초등 원시함수를 다룬다."
excerpt: "원시함수, 상수 차이의 유일성, 기본 부정적분, 초기조건"

categories: [Math / Calculus]
permalink: /ko/math/calculus/antiderivatives
sidebar: 
    nav: "calculus-ko"

date: 2026-06-02
weight: 8

published: false
---

지금까지 함수로부터 도함수를 구하는 미분을 다루었다. 이제 방향을 뒤집어, 도함수가 주어졌을 때 원래 함수를 되찾는 문제를 생각한다. 이는 가장 단순한 미분방정식 $$F' = f$$를 푸는 것이기도 하다. 물리적으로는 가속도에서 속도를, 속도에서 위치를 복원하는 일이며, 수학적으로는 다음 글들의 정적분과 [§미적분의 기본정리](/ko/math/calculus/fundamental_theorem_of_calculus)를 통해 넓이·길이·부피의 계산과 이어진다.

## 원시함수

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 구간 $$I$$에서 정의된 함수 $$f$$에 대하여, $$I$$의 모든 점에서 $$F'(x) = f(x)$$를 만족하는 미분가능한 함수 $$F$$를 $$f$$의 *원시함수<sub>antiderivative</sub>*라 한다.

</div>

예를 들어 $$F(x) = x^2$$은 $$f(x) = 2x$$의 원시함수이다. 그런데 $$x^2 + 1$$, $$x^2 - 5$$도 모두 도함수가 $$2x$$이므로 원시함수이다. 즉 한 원시함수에 상수를 더해도 여전히 원시함수이다. 기하학적으로는 같은 모양의 곡선을 위아래로 평행이동한 무리가 모두 같은 도함수(같은 기울기 분포)를 가지는 셈이다. 원시함수는 이처럼 유일하지 않지만, 그 비유일성은 정확히 상수항에 국한된다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> $$F$$가 구간 $$I$$에서 $$f$$의 원시함수이면, $$f$$의 모든 원시함수는 상수 $$C$$에 대해 $$F(x) + C$$의 꼴이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$G$$도 $$f$$의 원시함수라 하면 $$(G - F)' = f - f = 0$$이다. 평균값 정리의 따름정리 ([§평균값 정리, ⁋따름정리 5](/ko/math/calculus/mean_value_theorem#cor5))에 의해 구간에서 도함수가 항등적으로 $$0$$인 함수는 상수이므로, $$G - F = C$$인 상수 $$C$$가 있어 $$G = F + C$$이다.

</details>

이 명제에 따라 $$f$$의 원시함수 전체를 하나의 표현으로 묶어

$$\int f(x)\,dx = F(x) + C$$

로 적고, 이를 $$f$$의 *부정적분<sub>indefinite integral</sub>*이라 한다. 여기서 $$C$$를 *적분상수*, $$f$$를 *피적분함수*, 기호 $$dx$$를 적분변수의 표시로 본다. 명제 2가 보장하는 "상수 차이뿐"이라는 사실 덕분에 적분상수 $$C$$ 하나로 모든 원시함수를 한꺼번에 나타낼 수 있다.

구간이 연결되어 있다는 가정은 본질적이다. 정의역이 끊겨 있으면 각 조각마다 상수가 달라질 수 있다. 가령 $$1/x$$는 $$x > 0$$과 $$x < 0$$에서 따로 정의되는데, $$F(x) = \ln\lvert x\rvert$$에 두 조각에서 서로 다른 상수를 더한 것도 모두 $$1/x$$의 원시함수이므로, 정의역 전체에서는 "상수 차이뿐"이라는 명제가 그대로 적용되지 않는다.

## 기본 부정적분

미분 공식 ([§미분법](/ko/math/calculus/differentiation_rules))을 거꾸로 읽으면 기본 함수들의 부정적분을 얻는다. 먼저 부정적분도 미분처럼 선형이다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3 (부정적분의 선형성)**</ins> $$f, g$$가 원시함수를 가지고 $$a, b$$가 상수이면

$$\int \bigl(a f(x) + b g(x)\bigr)\,dx = a\int f(x)\,dx + b\int g(x)\,dx$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$F, G$$를 각각 $$f, g$$의 원시함수라 하면, 미분의 선형성 ([§미분과 도함수, ⁋명제 3](/ko/math/calculus/derivatives#prop3))에 의해

$$(aF + bG)' = aF' + bG' = af + bg$$

이므로 $$aF + bG$$가 $$af + bg$$의 원시함수이다.

</details>

거듭제곱·삼각·지수·로그함수와 역삼각함수의 도함수 공식을 뒤집으면 다음의 기본 공식들을 얻는다. 각 공식은 우변을 미분하면 피적분함수가 됨을 확인하여 검산할 수 있다 (적당한 구간에서).

$$\int x^r\,dx = \frac{x^{r+1}}{r+1} + C\ (r \neq -1), \qquad \int \frac{1}{x}\,dx = \ln\lvert x\rvert + C,$$

$$\int e^x\,dx = e^x + C, \qquad \int a^x\,dx = \frac{a^x}{\ln a} + C\ (a > 0,\, a \neq 1),$$

$$\int \cos x\,dx = \sin x + C, \qquad \int \sin x\,dx = -\cos x + C, \qquad \int \sec^2 x\,dx = \tan x + C,$$

$$\int \frac{dx}{1 + x^2} = \arctan x + C, \qquad \int \frac{dx}{\sqrt{1 - x^2}} = \arcsin x + C.$$

거듭제곱 공식이 실수 지수 $$r$$에 대해서도 성립함($$r = -1$$만 예외)에 유의한다. 음수·분수 지수도 같은 공식을 따른다:

$$\int \sqrt{x}\,dx = \int x^{1/2}\,dx = \frac23 x^{3/2} + C, \qquad \int \frac{dx}{x^2} = \int x^{-2}\,dx = -\frac1x + C, \qquad \int \frac{dx}{\sqrt{x}} = 2\sqrt{x} + C.$$

각 결과는 우변을 미분하면 피적분함수가 됨을 확인하여 검산된다. $$r = -1$$만은 거듭제곱 규칙이 $$x^0/0$$으로 깨지며, 그 자리를 $$\ln\lvert x\rvert$$가 메운다.

<div class="example" markdown="1">

<ins id="ex4">**예시 4**</ins> 선형성과 위 공식으로

$$\int (3x^2 - 4\cos x + e^x)\,dx = x^3 - 4\sin x + e^x + C,$$

$$\int \left(\frac{2}{x} + \sec^2 x - \frac{5}{1+x^2}\right)dx = 2\ln\lvert x\rvert + \tan x - 5\arctan x + C$$

이다. 피적분함수가 표준형이 아니면 먼저 대수적으로 변형한다. 삼각항등식으로 $$\displaystyle\int \tan^2 x\,dx = \int(\sec^2 x - 1)\,dx = \tan x - x + C$$이고, 전개로 $$\displaystyle\int (2x+1)^2\,dx = \int(4x^2 + 4x + 1)\,dx = \tfrac43 x^3 + 2x^2 + x + C$$이며, 분수를 나누어 $$\displaystyle\int \frac{x^2+1}{x}\,dx = \int\Bigl(x + \frac1x\Bigr)dx = \tfrac12 x^2 + \ln\lvert x\rvert + C$$이다.

</div>

## 추측에 의한 적분

미분과 달리 부정적분은 기계적으로 구해지지 않으므로, "미분하면 이것이 되는 함수"를 추측한 뒤 검산하는 것이 기본 전략이다. 특히 연쇄법칙의 역을 알아보는 눈이 중요하다.

<div class="example" markdown="1">

<ins id="ex5">**예시 5**</ins> $$\displaystyle\int 2x\,e^{x^2}\,dx$$를 구하자. $$\dfrac{d}{dx}e^{x^2} = 2x\,e^{x^2}$$임을 알아채면 곧바로 $$\int 2x\,e^{x^2}\,dx = e^{x^2} + C$$이다. 마찬가지로 $$\dfrac{d}{dx}(\sin x)^3 = 3(\sin x)^2\cos x$$에서 $$\displaystyle\int \sin^2 x\,\cos x\,dx = \tfrac13\sin^3 x + C$$를 얻는다. 이렇게 "안쪽 함수의 도함수가 곱해져 있는" 꼴은 연쇄법칙을 거꾸로 적용한 것으로, 이를 체계화한 것이 [§적분법](/ko/math/calculus/integration_techniques)의 치환적분이다.

</div>

## 초기조건과 미분방정식

적분상수 $$C$$는 *초기조건*이 주어지면 하나로 결정된다. 이것이 부정적분으로 미분방정식을 푸는 기본 방식이다.

<div class="example" markdown="1">

<ins id="ex6">**예시 6 (초기조건)**</ins> $$F'(x) = 3x^2 + 1$$이고 $$F(1) = 5$$인 $$F$$를 구하자. 부정적분으로 $$F(x) = x^3 + x + C$$이고, 초기조건 $$F(1) = 1 + 1 + C = 5$$에서 $$C = 3$$이다. 따라서 $$F(x) = x^3 + x + 3$$으로 유일하게 정해진다.

</div>

도함수가 두 번 주어지면 두 번 적분하며, 그때마다 초기조건이 적분상수를 하나씩 고정한다.

<div class="example" markdown="1">

<ins id="ex7">**예시 7 (자유낙하)**</ins> 중력가속도 $$-g$$로 떨어지는 물체의 위치 $$s(t)$$는 $$s''(t) = -g$$를 만족한다. 한 번 적분하면 속도 $$s'(t) = -gt + C_1$$이고 초기속도 $$s'(0) = v_0$$에서 $$C_1 = v_0$$이다. 다시 적분하면 $$s(t) = -\tfrac12 g t^2 + v_0 t + C_2$$이고 초기위치 $$s(0) = s_0$$에서 $$C_2 = s_0$$이다. 따라서 $$s(t) = s_0 + v_0 t - \tfrac12 g t^2$$로, 익숙한 등가속도 운동 공식이 두 번의 적분과 두 초기조건에서 나온다.

</div>

## 표준형으로의 변형

기본 공식에 곧바로 맞지 않는 피적분함수는 대수적·삼각적 변형으로 표준형을 만든다. 특히 분모가 이차식이면 완전제곱으로 역탄젠트·역사인 꼴을, 삼각함수의 거듭제곱이면 배각공식으로 일차 꼴을 만든다.

<div class="example" markdown="1">

<ins id="ex8">**예시 8 (분모가 이차식)**</ins> 상수를 맞추면 $$\displaystyle\int \frac{dx}{x^2 + 4} = \int \frac{dx}{4\bigl((x/2)^2 + 1\bigr)} = \frac12\arctan\frac{x}{2} + C$$이다. 분모에 일차항이 있으면 완전제곱을 한다:

$$\int \frac{dx}{x^2 + 2x + 5} = \int \frac{dx}{(x+1)^2 + 4} = \frac12\arctan\frac{x+1}{2} + C.$$

같은 요령으로 $$\sqrt{a^2 - x^2}$$ 꼴의 분모는 역사인으로 이어진다.

</div>

<div class="example" markdown="1">

<ins id="ex9">**예시 9 (삼각함수의 거듭제곱)**</ins> 배각공식 $$\cos 2x = 1 - 2\sin^2 x = 2\cos^2 x - 1$$로 차수를 낮춘다.

$$\int \sin^2 x\,dx = \int \frac{1 - \cos 2x}{2}\,dx = \frac{x}{2} - \frac{\sin 2x}{4} + C,$$

$$\int \cos^2 x\,dx = \int \frac{1 + \cos 2x}{2}\,dx = \frac{x}{2} + \frac{\sin 2x}{4} + C.$$

두 결과를 더하면 $$\int(\sin^2 x + \cos^2 x)\,dx = \int 1\,dx = x + C$$로 항등식과 일치함이 확인된다.

</div>

분모가 더 복잡한 유리식은 부분분수로 분해하여 각 조각을 위 표준형으로 적분한다. 가령

$$\int \frac{dx}{x^2 - 1} = \int \frac12\left(\frac{1}{x-1} - \frac{1}{x+1}\right)dx = \frac12\ln\left\lvert \frac{x-1}{x+1}\right\rvert + C$$

이다. 무리식은 적절한 치환으로 삼각함수 적분으로 바꾼다. 이러한 기법의 체계적 전개는 [§적분법](/ko/math/calculus/integration_techniques)에서 다룬다.

## 응용

부정적분의 가장 직접적인 응용은 변화율로부터 양 자체를 복원하는 것이다.

<div class="example" markdown="1">

<ins id="ex10">**예시 10 (속도에서 위치로)**</ins> 직선 위를 움직이는 물체의 속도가 $$v(t) = \cos t$$이고 $$t = 0$$에서의 위치가 $$s(0) = 2$$라 하자. 위치는 속도의 원시함수이므로

$$s(t) = \int \cos t\,dt = \sin t + C$$

이고, $$s(0) = \sin 0 + C = 2$$에서 $$C = 2$$이다. 따라서 $$s(t) = \sin t + 2$$이다. 가속도 $$a(t)$$만 주어졌다면 두 번 적분하여 두 초기조건(초기 속도·위치)으로 두 상수를 고정한다.

</div>

<div class="example" markdown="1">

<ins id="ex11">**예시 11 (검산)**</ins> 부정적분은 미분으로 곧장 검산된다. $$\displaystyle\int x\cos x\,dx = x\sin x + \cos x + C$$라 주장하면, 우변을 미분하여

$$\frac{d}{dx}\bigl(x\sin x + \cos x\bigr) = \sin x + x\cos x - \sin x = x\cos x$$

로 피적분함수가 되살아남을 확인한다. 적분 결과의 정당성은 언제나 이렇게 미분으로 검증할 수 있으며, 이 점이 부정적분이 미분의 역연산임을 다시 보여준다. (이 적분 자체를 구하는 부분적분은 [§적분법](/ko/math/calculus/integration_techniques)에서 다룬다.)

</div>

## 비초등 원시함수와 존재성

기법을 모두 동원해도 초등함수로 표현되지 않는 부정적분이 존재한다. $$e^{-x^2}$$, $$\dfrac{\sin x}{x}$$, $$\dfrac{1}{\ln x}$$ 같은 함수는 연속이므로 원시함수를 *가지지만*, 그 원시함수가 다항·유리·삼각·지수·로그함수의 유한 합성으로는 표현되지 않음이 리우빌의 이론으로 증명된다. 따라서 "적분이 안 된다"는 말은 흔히 "초등함수로 안 적힌다"는 뜻이며, 그 적분값 자체는 (정적분으로서) 멀쩡히 존재한다. 정규분포의 누적분포함수 $$\int e^{-x^2}\,dx$$가 그 대표적 예이다.

여기서 "연속함수는 원시함수를 가진다"는 존재성을 우리는 아직 증명하지 않았다. 미분 공식을 뒤집는 방식은 운 좋게 원시함수를 *찾았을* 때만 작동할 뿐, 일반적 존재를 보장하지 못한다. 이 존재성은 정적분을 도입한 뒤 [§미적분의 기본정리](/ko/math/calculus/fundamental_theorem_of_calculus)에서 가변상한 적분 $$F(x) = \int_a^x f$$가 $$f$$의 원시함수임을 보임으로써 비로소 증명된다. 그 다리를 놓으려면 먼저 정적분을 정의해야 하며, 그것이 다음 글 [§정적분](/ko/math/calculus/definite_integral)의 주제이다.
