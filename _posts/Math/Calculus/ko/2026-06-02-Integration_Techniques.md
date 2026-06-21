---
title: "적분법"
description: "미적분의 기본정리로 정적분 계산이 원시함수 찾기로 환원되므로, 연쇄법칙과 곱의 미분법을 거꾸로 활용하는 치환적분과 부분적분을 증명한다. 유리함수의 부분분수 분해, 삼각치환, 삼각함수 적분을 worked 예시로 다룬다."
excerpt: "치환적분, 부분적분, 부분분수, 삼각치환"

categories: [Math / Calculus]
permalink: /ko/math/calculus/integration_techniques
sidebar: 
    nav: "calculus-ko"

date: 2026-06-02
weight: 14

published: false
---

[§미적분의 기본정리](/ko/math/calculus/fundamental_theorem_of_calculus)에 의해 정적분의 계산은 원시함수를 찾는 문제로 환원된다. 그러나 원시함수는 미분처럼 기계적으로 구해지지 않으므로, 미분 규칙들을 거꾸로 읽어 피적분함수를 표준형으로 변형하는 기법이 필요하다. 두 핵심 기법인 치환적분과 부분적분은 각각 연쇄법칙과 곱의 미분법의 역이며, 여기에 유리함수의 부분분수, 무리식의 삼각치환이 더해진다.

## 치환적분

연쇄법칙 $$\dfrac{d}{dx}F(g(x)) = F'(g(x))g'(x)$$를 거꾸로 읽으면, "안쪽 함수의 도함수가 곱해진" 꼴의 적분을 단순화하는 치환적분을 얻는다.

<div class="proposition" markdown="1">

<ins id="thm1">**정리 1 (치환적분)**</ins> $$g$$가 미분가능하고 $$f$$가 연속이면

$$\int f(g(x))\,g'(x)\,dx = \int f(u)\,du \quad (u = g(x))$$

이고, 정적분에서는 $$\displaystyle\int_a^b f(g(x))\,g'(x)\,dx = \int_{g(a)}^{g(b)} f(u)\,du$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$F$$를 $$f$$의 원시함수라 하면 연쇄법칙 ([§미분법, ⁋정리 3](/ko/math/calculus/differentiation_rules#thm3))에 의해

$$\frac{d}{dx}F(g(x)) = F'(g(x))\,g'(x) = f(g(x))\,g'(x)$$

이므로, $$F(g(x))$$가 좌변 피적분함수의 원시함수이다. 따라서 부정적분은 $$F(g(x)) + C = F(u) + C$$와 같다. 정적분의 경우 평가정리 ([§미적분의 기본정리, ⁋정리 3](/ko/math/calculus/fundamental_theorem_of_calculus#thm3))로

$$\int_a^b f(g(x))g'(x)\,dx = \bigl[F(g(x))\bigr]_a^b = F(g(b)) - F(g(a)) = \int_{g(a)}^{g(b)} f(u)\,du$$

를 얻는다.

</details>

실용에서는 $$u = g(x)$$, $$du = g'(x)\,dx$$로 두고 식을 $$u$$만으로 바꾸어 적분한 뒤 되돌린다.

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins> $$u = x^2$$, $$du = 2x\,dx$$로 두면 $$\displaystyle\int 2x\,e^{x^2}\,dx = \int e^u\,du = e^u + C = e^{x^2} + C$$이다. 같은 방식으로 $$u = x^2 + 1$$로 $$\displaystyle\int \frac{x}{x^2+1}\,dx = \frac12\int \frac{du}{u} = \frac12\ln(x^2+1) + C$$이고, $$u = \cos x$$로 $$\displaystyle\int \tan x\,dx = \int \frac{\sin x}{\cos x}\,dx = -\int \frac{du}{u} = -\ln\lvert\cos x\rvert + C$$이다.

</div>

<div class="example" markdown="1">

<ins id="ex3">**예시 3 (정적분의 치환)**</ins> 정적분에서는 끝값도 함께 바꾼다. $$\displaystyle\int_0^1 x\sqrt{1 + x^2}\,dx$$에서 $$u = 1 + x^2$$로 두면 $$du = 2x\,dx$$이고 $$x : 0 \to 1$$일 때 $$u : 1 \to 2$$이므로

$$\int_0^1 x\sqrt{1+x^2}\,dx = \frac12\int_1^2 \sqrt{u}\,du = \frac12\cdot\frac23\bigl[u^{3/2}\bigr]_1^2 = \frac13\bigl(2\sqrt2 - 1\bigr)$$

이다. 끝값을 바꾸면 원래 변수로 되돌릴 필요가 없다.

</div>

## 부분적분

곱의 미분법 $$(uv)' = u'v + uv'$$를 거꾸로 읽으면 부분적분을 얻는다. 이는 곱으로 이루어진 피적분함수를 다루는 주된 도구이다.

<div class="proposition" markdown="1">

<ins id="thm4">**정리 4 (부분적분)**</ins> $$u, v$$가 미분가능하고 그 도함수가 연속이면

$$\int u\,v'\,dx = uv - \int u'\,v\,dx$$

이고, 정적분에서는 $$\displaystyle\int_a^b u\,v'\,dx = \bigl[uv\bigr]_a^b - \int_a^b u'\,v\,dx$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

곱의 미분법 ([§미분법, ⁋명제 1](/ko/math/calculus/differentiation_rules#prop1))으로 $$(uv)' = u'v + uv'$$이므로 $$uv' = (uv)' - u'v$$이다. 양변을 적분하고 $$\int (uv)'\,dx = uv$$를 쓰면 부정적분 형태를, 평가정리를 적용하면 정적분 형태를 얻는다.

</details>

핵심은 $$u$$를 미분하면 단순해지는 쪽, $$v'$$을 적분할 수 있는 쪽으로 고르는 것이다.

<div class="example" markdown="1">

<ins id="ex5">**예시 5**</ins> $$\displaystyle\int x\,e^x\,dx$$에서 $$u = x$$, $$v' = e^x$$로 두면 $$u' = 1$$, $$v = e^x$$이므로

$$\int x e^x\,dx = x e^x - \int e^x\,dx = x e^x - e^x + C$$

이다. 로그·역삼각함수는 미분이 간단해지므로 $$u$$로 둔다: $$v' = 1$$로 보아 $$\displaystyle\int \ln x\,dx = x\ln x - \int x\cdot\frac1x\,dx = x\ln x - x + C$$이다.

</div>

<div class="example" markdown="1">

<ins id="ex6">**예시 6 (순환형)**</ins> $$I = \displaystyle\int e^x\cos x\,dx$$는 부분적분을 두 번 하면 자기 자신이 돌아온다. $$u = e^x$$, $$v' = \cos x$$로 두면

$$I = e^x\sin x - \int e^x\sin x\,dx = e^x\sin x - \Bigl(-e^x\cos x + \int e^x\cos x\,dx\Bigr) = e^x(\sin x + \cos x) - I$$

이므로 $$2I = e^x(\sin x + \cos x)$$, 곧 $$I = \dfrac{e^x(\sin x + \cos x)}{2} + C$$이다.

</div>

## 유리함수의 부분분수

분모가 인수분해되는 유리함수는 부분분수로 분해하면 각 조각이 로그·역탄젠트로 적분된다.

<div class="example" markdown="1">

<ins id="ex7">**예시 7**</ins> $$\dfrac{1}{x^2 - 1} = \dfrac12\Bigl(\dfrac{1}{x-1} - \dfrac{1}{x+1}\Bigr)$$로 분해하면

$$\int \frac{dx}{x^2 - 1} = \frac12\bigl(\ln\lvert x-1\rvert - \ln\lvert x+1\rvert\bigr) + C = \frac12\ln\left\lvert\frac{x-1}{x+1}\right\rvert + C$$

이다. 분모에 기약 이차식이 있으면 완전제곱 후 역탄젠트로 간다: $$\displaystyle\int \frac{dx}{x^2 + 2x + 5} = \int \frac{dx}{(x+1)^2 + 4} = \frac12\arctan\frac{x+1}{2} + C$$.

</div>

## 삼각치환과 삼각함수 적분

$$\sqrt{a^2 - x^2}$$, $$\sqrt{a^2 + x^2}$$ 같은 무리식은 삼각함수로 치환하면 무리식이 사라진다.

<div class="example" markdown="1">

<ins id="ex8">**예시 8 (삼각치환)**</ins> $$\displaystyle\int \sqrt{1 - x^2}\,dx$$에서 $$x = \sin\theta$$ ($$dx = \cos\theta\,d\theta$$, $$\sqrt{1-x^2} = \cos\theta$$) 로 두면

$$\int \sqrt{1-x^2}\,dx = \int \cos^2\theta\,d\theta = \frac\theta2 + \frac{\sin 2\theta}{4} + C = \frac12\bigl(\arcsin x + x\sqrt{1-x^2}\bigr) + C$$

이다. 이를 $$[-1,1]$$에서 정적분하면 반원의 넓이 $$\pi/2$$가 나온다.

</div>

<div class="example" markdown="1">

<ins id="ex9">**예시 9 (삼각함수 적분)**</ins> 삼각함수의 거듭제곱은 항등식으로 차수를 낮추거나 치환한다. 홀수 거듭제곱은 하나를 떼어 치환하고($$u = \cos x$$로 $$\int \sin^3 x\,dx = \int(1-\cos^2 x)\sin x\,dx = -\cos x + \tfrac13\cos^3 x + C$$), 짝수 거듭제곱은 배각공식으로 낮춘다($$\int \sin^2 x\,dx = \tfrac x2 - \tfrac{\sin 2x}{4} + C$$).

</div>

## 점화식과 정적분에의 적용

부분적분을 반복하면 차수를 한 단계씩 낮추는 *점화식*을 얻는다. 거듭제곱이 섞인 적분을 체계적으로 처리하는 데 유용하다.

<div class="example" markdown="1">

<ins id="ex10">**예시 10 (점화식)**</ins> $$I_n = \displaystyle\int x^n e^x\,dx$$에 $$u = x^n$$, $$v' = e^x$$로 부분적분하면

$$I_n = x^n e^x - n\int x^{n-1}e^x\,dx = x^n e^x - n I_{n-1}$$

이다. $$I_0 = e^x$$에서 시작하면 $$I_1 = (x-1)e^x$$, $$I_2 = (x^2 - 2x + 2)e^x$$로 차수를 내려가며 구해진다. 같은 방식으로 $$\int \sin^n x\,dx$$도 $$\int \sin^n = -\tfrac1n \sin^{n-1}x\cos x + \tfrac{n-1}{n}\int \sin^{n-2}x\,dx$$라는 점화식을 가진다.

</div>

<div class="example" markdown="1">

<ins id="ex11">**예시 11 (정적분)**</ins> 정적분에서는 두 기법이 끝값과 함께 작동한다. 부분적분으로

$$\int_1^e \ln x\,dx = \bigl[x\ln x\bigr]_1^e - \int_1^e 1\,dx = (e - 0) - (e - 1) = 1$$

이고, 치환으로 ($$u = \sin x$$, $$x : 0 \to \pi/2$$일 때 $$u : 0 \to 1$$)

$$\int_0^{\pi/2} \sin^2 x\cos x\,dx = \int_0^1 u^2\,du = \frac13$$

이다.

</div>

<div class="example" markdown="1">

<ins id="ex12">**예시 12 (기법의 결합)**</ins> 한 적분에 여러 기법이 함께 쓰이기도 한다. $$\displaystyle\int \frac{dx}{x^2 + x} = \int \frac{dx}{x(x+1)}$$는 부분분수로

$$\int \left(\frac1x - \frac{1}{x+1}\right)dx = \ln\lvert x\rvert - \ln\lvert x+1\rvert + C = \ln\left\lvert\frac{x}{x+1}\right\rvert + C$$

이고, $$\displaystyle\int x\arctan x\,dx$$는 부분적분($$u = \arctan x$$, $$v' = x$$) 후 남는 유리식을 다시 정리하여

$$\int x\arctan x\,dx = \frac{x^2}{2}\arctan x - \frac12\int \frac{x^2}{1+x^2}\,dx = \frac{x^2}{2}\arctan x - \frac12\bigl(x - \arctan x\bigr) + C$$

이 된다.

</div>

이러한 기법으로도 초등함수로 표현되지 않는 적분 — 가령 $$\int e^{-x^2}\,dx$$, $$\int \frac{\sin x}{x}\,dx$$ — 이 존재하지만, 그래도 정적분 값 자체는 잘 정의된다 ([§정적분](/ko/math/calculus/definite_integral)).
