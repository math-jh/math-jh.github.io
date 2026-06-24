---
title: "적분법"
description: "미적분의 기본정리로 정적분 계산이 원시함수 찾기로 환원되므로, 연쇄법칙과 곱의 미분법을 거꾸로 활용하는 치환적분과 부분적분을 증명한다. 유리함수의 부분분수 분해, 삼각치환, 삼각함수 적분을 worked 예시로 다룬다."
excerpt: "치환적분, 부분적분, 부분분수, 삼각치환"

categories: [Math / Calculus]
permalink: /ko/math/calculus/integration_techniques
sidebar: 
    nav: "calculus-ko"

date: 2026-06-02
weight: 13
drift_needed: true

published: false
---

[§미적분의 기본정리](/ko/math/calculus/fundamental_theorem_of_calculus)에 의해 정적분의 계산은 원시함수를 찾는 문제로 환원된다. 그러나 원시함수는 미분처럼 기계적으로 구해지지 않으므로, 미분 규칙들을 거꾸로 읽어 피적분함수를 표준형으로 변형하는 기법이 필요하다. 두 핵심 기법인 치환적분과 부분적분은 각각 [§미분법, ⁋정리 4](/ko/math/calculus/differentiation_rules#thm4)과 [§미분법, ⁋명제 3](/ko/math/calculus/differentiation_rules#prop3)의 역이며, 여기에 유리함수의 부분분수, 무리식의 삼각치환이 더해진다.

## 치환적분

연쇄법칙 $$\frac{d}{dx}F(g(x)) = F'(g(x))g'(x)$$를 거꾸로 읽으면, "안쪽 함수의 도함수가 곱해진" 꼴의 적분을 단순화하는 치환적분을 얻는다.

<div class="proposition" markdown="1">

<ins id="thm1">**정리 1 (치환적분)**</ins> $$g$$가 미분가능하고 $$f$$가 연속이면

$$\int f(g(x))\,g'(x)\,dx = \int f(u)\,du \quad (u = g(x))$$

이고, 정적분에서는

$$\int_a^b f(g(x))\,g'(x)\,dx = \int_{g(a)}^{g(b)} f(u)\,du$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$F$$를 $$f$$의 원시함수라 하면 [§미분법, ⁋정리 4](/ko/math/calculus/differentiation_rules#thm4)에 의해

$$\frac{d}{dx}F(g(x)) = F'(g(x))\,g'(x) = f(g(x))\,g'(x)$$

이므로, $$F(g(x))$$가 좌변 피적분함수의 원시함수이다. 따라서 부정적분은 $$F(g(x)) + C = F(u) + C$$와 같다. 정적분의 경우 평가정리 ([§미적분의 기본정리, ⁋정리 3](/ko/math/calculus/fundamental_theorem_of_calculus#thm3))로

$$\int_a^b f(g(x))g'(x)\,dx = \bigl[F(g(x))\bigr]_a^b = F(g(b)) - F(g(a)) = \int_{g(a)}^{g(b)} f(u)\,du$$

를 얻는다.

</details>

실용에서는 $$u = g(x)$$, $$du = g'(x)\,dx$$로 두고 식을 $$u$$만으로 바꾸어 적분한 뒤 되돌린다. 가령 $$u = \cos x$$로 두면 $$\int \tan x\,dx = -\int du/u = -\ln\lvert\cos x\rvert + C$$이고, 같은 요령으로 $$\int x/(x^2+1)\,dx = \tfrac12\ln(x^2+1) + C$$를 얻는다. 정적분에서는 끝값까지 함께 옮기면 원래 변수로 되돌릴 필요가 없다. 예컨대 $$\int_0^1 x\sqrt{1+x^2}\,dx$$는 $$u = 1+x^2$$로 $$x : 0 \to 1$$을 $$u : 1 \to 2$$로 바꾸어 $$\tfrac12\int_1^2 \sqrt{u}\,du = \tfrac13(2\sqrt2 - 1)$$이 된다.

## 부분적분

곱의 미분법 $$(uv)' = u'v + uv'$$를 거꾸로 읽으면 부분적분을 얻는다. 이는 곱으로 이루어진 피적분함수를 다루는 주된 도구이다.

<div class="proposition" markdown="1">

<ins id="thm2">**정리 2 (부분적분)**</ins> $$u, v$$가 미분가능하고 그 도함수가 연속이면

$$\int u\,v'\,dx = uv - \int u'\,v\,dx$$

이고, 정적분에서는

$$\int_a^b u\,v'\,dx = \bigl[uv\bigr]_a^b - \int_a^b u'\,v\,dx$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

[§미분법, ⁋명제 3](/ko/math/calculus/differentiation_rules#prop3)으로 $$(uv)' = u'v + uv'$$이므로 $$uv' = (uv)' - u'v$$이다. 양변을 적분하고 $$\int (uv)'\,dx = uv$$를 쓰면 부정적분 형태를, 평가정리를 적용하면 정적분 형태를 얻는다.

</details>

핵심은 $$u$$를 미분하면 단순해지는 쪽, $$v'$$을 적분할 수 있는 쪽으로 고르는 것이다. 가령 $$\int x e^x\,dx$$는 $$u = x$$로 두어 $$x e^x - e^x + C$$가 되고, 로그·역삼각함수처럼 미분이 도리어 간단해지는 함수는 $$v' = 1$$로 보아 $$u$$ 자리에 놓는다($$\int \ln x\,dx = x\ln x - x + C$$). 부분적분이 피적분함수를 단순화하지 않고 자기 자신으로 되돌아오는 경우도 있는데, 이때는 원래 적분을 미지수로 보고 대수적으로 푼다.

<div class="example" markdown="1">

<ins id="ex3">**예시 3 (순환형)**</ins> $$I = \int e^x\cos x\,dx$$는 부분적분을 두 번 하면 자기 자신이 돌아온다. $$u = e^x$$, $$v' = \cos x$$로 두면

$$I = e^x\sin x - \int e^x\sin x\,dx = e^x\sin x - \Bigl(-e^x\cos x + \int e^x\cos x\,dx\Bigr) = e^x(\sin x + \cos x) - I$$

이므로 $$2I = e^x(\sin x + \cos x)$$, 곧 $$I = \frac{e^x(\sin x + \cos x)}{2} + C$$이다.

</div>

## 유리함수의 부분분수

분모가 인수분해되는 유리함수는 부분분수로 분해하면 각 조각이 로그·역탄젠트로 적분된다. 예컨대 $$1/(x^2-1) = \tfrac12\bigl(1/(x-1) - 1/(x+1)\bigr)$$로 가르면

$$\int \frac{dx}{x^2 - 1} = \frac12\bigl(\ln\lvert x-1\rvert - \ln\lvert x+1\rvert\bigr) + C = \frac12\ln\left\lvert\frac{x-1}{x+1}\right\rvert + C$$

이다. 분모에 기약 이차식이 있으면 완전제곱으로 묶어 역탄젠트로 가는데, $$\int dx/(x^2 + 2x + 5) = \int dx/((x+1)^2 + 4) = \tfrac12\arctan\bigl((x+1)/2\bigr) + C$$가 그 꼴이다.

## 삼각치환과 삼각함수 적분

$$\sqrt{a^2 - x^2}$$, $$\sqrt{a^2 + x^2}$$ 같은 무리식은 삼각함수로 치환하면 무리식이 사라진다. $$\int \sqrt{1 - x^2}\,dx$$에서 $$x = \sin\theta$$($$dx = \cos\theta\,d\theta$$, $$\sqrt{1-x^2} = \cos\theta$$) 로 두면

$$\int \sqrt{1-x^2}\,dx = \int \cos^2\theta\,d\theta = \frac\theta2 + \frac{\sin 2\theta}{4} + C = \frac12\bigl(\arcsin x + x\sqrt{1-x^2}\bigr) + C$$

이고, 이를 $$[-1,1]$$에서 정적분하면 반원의 넓이 $$\pi/2$$가 나온다. 삼각함수 자체의 거듭제곱은 항등식으로 차수를 낮추거나 치환하는데, 홀수 거듭제곱은 하나를 떼어 치환하고($$u = \cos x$$로 $$\int \sin^3 x\,dx = -\cos x + \tfrac13\cos^3 x + C$$), 짝수 거듭제곱은 배각공식으로 낮춘다($$\int \sin^2 x\,dx = \tfrac x2 - \tfrac{\sin 2x}{4} + C$$).

여러 기법은 한 적분에서 함께 쓰이기도 한다. 가령 $$\int x\arctan x\,dx$$는 부분적분($$u = \arctan x$$, $$v' = x$$) 후 남는 유리식을 $$x^2/(1+x^2) = 1 - 1/(1+x^2)$$로 갈라 적분하여 $$\tfrac{x^2}{2}\arctan x - \tfrac12(x - \arctan x) + C$$가 된다.

## 점화식

부분적분을 반복하면 차수를 한 단계씩 낮추는 점화식을 얻는다. 거듭제곱이 섞인 적분을 체계적으로 처리하는 데 유용하다.

<div class="example" markdown="1">

<ins id="ex4">**예시 4 (점화식)**</ins> $$I_n = \int x^n e^x\,dx$$에 $$u = x^n$$, $$v' = e^x$$로 부분적분하면

$$I_n = x^n e^x - n\int x^{n-1}e^x\,dx = x^n e^x - n I_{n-1}$$

이다. $$I_0 = e^x$$에서 시작하면 $$I_1 = (x-1)e^x$$, $$I_2 = (x^2 - 2x + 2)e^x$$로 차수를 내려가며 구해진다. 같은 방식으로 $$\int \sin^n x\,dx$$도

$$\int \sin^n x\,dx = -\frac1n \sin^{n-1}x\cos x + \frac{n-1}{n}\int \sin^{n-2}x\,dx$$

라는 점화식을 가진다.

</div>

이러한 기법으로도 초등함수로 표현되지 않는 적분, 가령 $$\int e^{-x^2}\,dx$$나 $$\int (\sin x)/x\,dx$$가 존재하지만, 그래도 정적분 값 자체는 잘 정의된다 ([§정적분](/ko/math/calculus/definite_integral)).
</content>
</invoke>
