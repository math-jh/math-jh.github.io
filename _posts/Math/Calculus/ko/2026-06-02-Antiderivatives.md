---
title: "부정적분"
description: "미분의 역연산인 부정적분(원시함수)을 정의하고, 두 원시함수가 상수 차이로만 다름을 평균값 정리로부터 보인다. 기본 함수들의 부정적분과 선형성을 정리하여 적분 계산의 토대를 마련한다."
excerpt: "원시함수, 상수 차이의 유일성, 기본 부정적분"

categories: [Math / Calculus]
permalink: /ko/math/calculus/antiderivatives
sidebar: 
    nav: "calculus-ko"

header:
    overlay_image: /assets/images/Math/Calculus/Antiderivatives.png
    overlay_filter: 0.5

date: 2026-06-02
last_modified_at: 2026-06-02
weight: 8

published: false
---

지금까지 함수로부터 도함수를 구하는 미분을 다루었다. 이제 방향을 뒤집어, 도함수가 주어졌을 때 원래 함수를 되찾는 문제를 생각한다. 이 역연산은 다음 글들에서 다룰 정적분과 [§미적분의 기본정리](/ko/math/calculus/fundamental_theorem_of_calculus)를 통해 넓이·길이·부피의 계산과 이어진다.

## 원시함수

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 구간 $$I$$에서 정의된 함수 $$f$$에 대하여, $$I$$의 모든 점에서 $$F'(x) = f(x)$$를 만족하는 미분가능한 함수 $$F$$를 $$f$$의 *원시함수<sub>antiderivative</sub>*라 한다.

</div>

예를 들어 $$F(x) = x^2$$은 $$f(x) = 2x$$의 원시함수이다. 그런데 $$x^2 + 1$$, $$x^2 - 5$$도 모두 도함수가 $$2x$$이므로 원시함수이다. 원시함수는 유일하지 않지만, 그 비유일성은 상수항에 국한된다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> $$F$$가 구간 $$I$$에서 $$f$$의 원시함수이면, $$f$$의 모든 원시함수는 상수 $$C$$에 대해 $$F(x) + C$$의 꼴이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$G$$도 $$f$$의 원시함수라 하면 $$(G - F)' = f - f = 0$$이다. 평균값 정리의 따름정리 ([§평균값 정리, ⁋따름정리 5](/ko/math/calculus/mean_value_theorem#cor5))에 의해 구간에서 도함수가 항등적으로 $$0$$인 함수는 상수이므로, $$G - F = C$$인 상수 $$C$$가 있어 $$G = F + C$$이다.

</details>

이 명제에 따라 $$f$$의 원시함수 전체를 하나의 표현으로 묶어

$$\int f(x)\,dx = F(x) + C$$

로 적고, 이를 $$f$$의 *부정적분<sub>indefinite integral</sub>*이라 한다. 여기서 $$C$$를 *적분상수*라 한다. 구간이 연결되어 있다는 가정은 본질적이다: 정의역이 끊겨 있으면 각 조각마다 상수가 달라질 수 있다.

## 기본 부정적분

미분 공식 ([§미분법](/ko/math/calculus/differentiation_rules))을 거꾸로 읽으면 기본 함수들의 부정적분을 얻는다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3 (부정적분의 선형성)**</ins> $$f, g$$가 원시함수를 가지고 $$a, b$$가 상수이면

$$\int \bigl(a f(x) + b g(x)\bigr)\,dx = a\int f(x)\,dx + b\int g(x)\,dx$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$F, G$$를 각각 $$f, g$$의 원시함수라 하면, 미분의 선형성 ([§미분과 도함수, ⁋명제 3](/ko/math/calculus/derivatives#prop3))에 의해 $$(aF + bG)' = af + bg$$이므로 $$aF + bG$$가 $$af + bg$$의 원시함수이다.

</details>

거듭제곱·삼각·지수함수의 도함수 공식을 뒤집으면 다음을 얻는다.

$$\int x^n\,dx = \frac{x^{n+1}}{n+1} + C\ (n \neq -1), \qquad \int \frac{1}{x}\,dx = \ln\lvert x\rvert + C,$$

$$\int e^x\,dx = e^x + C, \qquad \int \cos x\,dx = \sin x + C, \qquad \int \sin x\,dx = -\cos x + C.$$

<div class="example" markdown="1">

<ins id="ex4">**예시 4**</ins> 선형성과 위 공식으로

$$\int (3x^2 - 4\cos x + e^x)\,dx = x^3 - 4\sin x + e^x + C$$

이다. 미분하면 피적분함수로 돌아옴을 직접 확인할 수 있다.

</div>

미분과 달리 부정적분은 기계적으로 구해지지 않는다. 합성·곱의 미분법을 거꾸로 활용하는 치환적분과 부분적분 같은 기법은 [§적분법](/ko/math/calculus/integration_techniques)에서 다룬다. 또한 지금은 "도함수가 $$f$$인 함수가 존재하는가"라는 존재성을 다루지 않았는데, $$f$$가 연속이면 원시함수가 반드시 존재한다는 사실은 정적분을 도입한 뒤 [§미적분의 기본정리](/ko/math/calculus/fundamental_theorem_of_calculus)에서 비로소 증명된다.
