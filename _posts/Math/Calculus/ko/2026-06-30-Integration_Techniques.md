---
title: "적분법"
description: "미적분의 기본정리로 정적분 계산이 원시함수 찾기로 환원되므로, 합성과 곱의 미분법을 거꾸로 활용하는 치환적분과 부분적분을 증명한다. 유리함수의 부분분수 분해와 삼각치환도 개관한다."
excerpt: "치환적분, 부분적분, 부분분수와 삼각치환"

categories: [Math / Calculus]
permalink: /ko/math/calculus/integration_techniques
sidebar: 
    nav: "calculus-ko"

header:
    overlay_image: /assets/images/Math/Calculus/Integration_Techniques.png
    overlay_filter: 0.5

date: 2026-06-30
last_modified_at: 2026-06-30

weight: 11

published: false
---

[§미적분의 기본정리](/ko/math/calculus/fundamental_theorem_of_calculus)에 의해 정적분의 계산은 원시함수를 찾는 문제로 환원된다. 그러나 원시함수는 기계적으로 구해지지 않으므로, 미분 규칙들을 거꾸로 읽어 적분을 변형하는 기법이 필요하다. 두 핵심 기법인 치환적분과 부분적분은 각각 연쇄법칙과 곱의 미분법의 역이다.

## 치환적분

<div class="proposition" markdown="1">

<ins id="thm1">**정리 1 (치환적분)**</ins> $$g$$가 미분가능하고 $$f$$가 연속이면

$$\int f(g(x))\,g'(x)\,dx = \int f(u)\,du \quad (u = g(x))$$

이고, 정적분에서는 $$\displaystyle\int_a^b f(g(x))g'(x)\,dx = \int_{g(a)}^{g(b)} f(u)\,du$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$F$$를 $$f$$의 원시함수라 하면 연쇄법칙 ([§미분법, ⁋정리 3](/ko/math/calculus/differentiation_rules#thm3))에 의해 $$\dfrac{d}{dx}F(g(x)) = F'(g(x))g'(x) = f(g(x))g'(x)$$이므로, $$F(g(x))$$가 좌변 피적분함수의 원시함수이다. 따라서 부정적분은 $$F(g(x)) + C = F(u) + C$$와 같다. 정적분의 경우 평가정리 ([§미적분의 기본정리, ⁋정리 3](/ko/math/calculus/fundamental_theorem_of_calculus#thm3))로 $$F(g(b)) - F(g(a)) = \int_{g(a)}^{g(b)} f(u)\,du$$를 얻는다.

</details>

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins> $$\displaystyle\int 2x\,e^{x^2}\,dx$$에서 $$u = x^2$$로 두면 $$du = 2x\,dx$$이므로 $$\int e^u\,du = e^u + C = e^{x^2} + C$$이다.

</div>

## 부분적분

<div class="proposition" markdown="1">

<ins id="thm3">**정리 3 (부분적분)**</ins> $$u, v$$가 미분가능하고 그 도함수가 연속이면

$$\int u\,v'\,dx = uv - \int u'\,v\,dx$$

이고, 정적분에서는 $$\displaystyle\int_a^b u\,v'\,dx = \bigl[uv\bigr]_a^b - \int_a^b u'\,v\,dx$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

곱의 미분법 ([§미분법, ⁋명제 1](/ko/math/calculus/differentiation_rules#prop1))으로 $$(uv)' = u'v + uv'$$이므로 $$uv'= (uv)' - u'v$$이다. 양변을 적분하고 $$\int (uv)'\,dx = uv$$를 쓰면 부정적분 형태를, 평가정리를 적용하면 정적분 형태를 얻는다.

</details>

<div class="example" markdown="1">

<ins id="ex4">**예시 4**</ins> $$\displaystyle\int x\,e^x\,dx$$에서 $$u = x$$, $$v' = e^x$$로 두면 $$u' = 1$$, $$v = e^x$$이므로 $$\int x e^x\,dx = x e^x - \int e^x\,dx = x e^x - e^x + C$$이다.

</div>

## 유리함수와 삼각치환

위 두 기법에 더해, 함수의 형태에 맞춘 표준 변형이 있다. *유리함수*의 적분은 분모를 인수분해하여 부분분수로 분해하면 $$\dfrac{1}{x - a}$$와 $$\dfrac{1}{(x-a)^2 + b^2}$$ 꼴의 적분으로 귀착되어, 각각 로그와 역탄젠트로 적분된다. $$\sqrt{a^2 - x^2}$$ 같은 무리식은 $$x = a\sin\theta$$ 등의 *삼각치환*으로 삼각함수의 적분으로 바꾼다.

이러한 기법으로도 초등함수로 표현되지 않는 적분 — 가령 $$\int e^{-x^2}\,dx$$ — 이 존재하지만, 그래도 정적분 값 자체는 잘 정의된다 ([§정적분](/ko/math/calculus/definite_integral)). 적분 구간이나 피적분함수가 무한으로 발산하는 경우의 적분은 다음 글 [§이상적분](/ko/math/calculus/improper_integrals)에서 다룬다.
