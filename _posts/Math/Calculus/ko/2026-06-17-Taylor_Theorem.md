---
title: "테일러 정리"
description: "함수를 한 점 근방에서 다항식으로 근사하는 테일러 다항식을 정의하고, 그 오차를 고계도함수로 정확히 평가하는 테일러 정리를 라그랑주 나머지 형태로 증명한다. 지수·삼각함수의 전개를 예로 든다."
excerpt: "테일러 다항식, 라그랑주 나머지, 테일러 정리"

categories: [Math / Calculus]
permalink: /ko/math/calculus/taylor_theorem
sidebar: 
    nav: "calculus-ko"

header:
    overlay_image: /assets/images/Math/Calculus/Taylor_Theorem.png
    overlay_filter: 0.5

date: 2026-06-17
last_modified_at: 2026-06-17

weight: 7

published: false
---

[§도함수의 응용](/ko/math/calculus/applications_of_derivatives)에서 일계도함수로 함수의 모양을 읽었다. 미분계수 $$f'(a)$$는 본래 $$f(x) \approx f(a) + f'(a)(x-a)$$라는 일차 근사였으니 ([§미분과 도함수](/ko/math/calculus/derivatives)), 자연스러운 다음 물음은 고계도함수를 동원하여 함수를 더 높은 차수의 다항식으로 근사하는 것, 그리고 그 오차를 정량적으로 통제하는 것이다.

## 테일러 다항식

함수 $$f$$가 $$a$$에서 $$n$$번 미분가능하면, $$a$$에서의 도함수 값들이 일치하도록 차수 $$n$$의 다항식을 맞출 수 있다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> $$f$$가 $$a$$에서 $$n$$번 미분가능할 때, $$f$$의 $$a$$에서의 *$$n$$차 테일러 다항식<sub>Taylor polynomial</sub>*은

$$P_n(x) = \sum_{k=0}^{n} \frac{f^{(k)}(a)}{k!}(x - a)^k = f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2 + \cdots + \frac{f^{(n)}(a)}{n!}(x-a)^n$$

이다. 여기서 $$f^{(k)}$$는 $$f$$를 $$k$$번 미분한 함수이고 $$f^{(0)} = f$$로 본다.

</div>

$$P_n$$은 $$k = 0, 1, \ldots, n$$에 대해 $$P_n^{(k)}(a) = f^{(k)}(a)$$를 만족하는 유일한 차수 $$\leq n$$의 다항식이다. $$n = 1$$이면 $$P_1(x) = f(a) + f'(a)(x-a)$$로 접선, 곧 일차 근사와 같다.

## 테일러 정리

근사 $$f \approx P_n$$의 오차 $$R_n(x) = f(x) - P_n(x)$$를 고계도함수로 정확히 표현하는 것이 다음 정리이다.

<div class="proposition" markdown="1">

<ins id="thm2">**정리 2 (테일러 정리, 라그랑주 나머지)**</ins> $$f$$가 $$a$$와 $$x$$를 포함하는 구간에서 $$n+1$$번 미분가능하면, $$a$$와 $$x$$ 사이의 어떤 $$c$$에 대하여

$$f(x) = P_n(x) + R_n(x), \qquad R_n(x) = \frac{f^{(n+1)}(c)}{(n+1)!}(x - a)^{n+1}$$

이 성립한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$x \neq a$$를 고정하고, $$a$$와 $$x$$ 사이의 $$t$$에 대해 두 보조함수

$$g(t) = f(x) - \sum_{k=0}^{n}\frac{f^{(k)}(t)}{k!}(x-t)^k, \qquad h(t) = (x - t)^{n+1}$$

을 둔다. $$g(x) = 0$$, $$g(a) = f(x) - P_n(x) = R_n(x)$$이고 $$h(x) = 0$$, $$h(a) = (x-a)^{n+1}$$이다. $$g$$를 미분하면 인접한 항들이 상쇄되어

$$g'(t) = -\frac{f^{(n+1)}(t)}{n!}(x - t)^n$$

만 남고, $$h'(t) = -(n+1)(x-t)^n$$이다. 코시 평균값 정리 ([§평균값 정리, ⁋정리 6](/ko/math/calculus/mean_value_theorem#thm6))를 $$a$$와 $$x$$ 사이에 적용하면

$$\bigl(g(x) - g(a)\bigr)h'(c) = \bigl(h(x) - h(a)\bigr)g'(c)$$

인 $$c$$가 존재한다. 값을 대입하면 $$(-R_n(x))\bigl(-(n+1)(x-c)^n\bigr) = \bigl(-(x-a)^{n+1}\bigr)\Bigl(-\dfrac{f^{(n+1)}(c)}{n!}(x-c)^n\Bigr)$$이고, 양변의 $$(x-c)^n$$을 소거하여 정리하면 $$R_n(x) = \dfrac{f^{(n+1)}(c)}{(n+1)!}(x-a)^{n+1}$$을 얻는다.

</details>

$$n = 0$$인 경우의 테일러 정리는 정확히 평균값 정리 ([§평균값 정리, ⁋정리 4](/ko/math/calculus/mean_value_theorem#thm4))이다. 따라서 테일러 정리는 평균값 정리를 고계도함수로 끌어올린 것으로 볼 수 있다.

## 초등함수의 전개

나머지항을 평가하면 다항식 근사의 정확도를 구체적으로 가늠할 수 있다.

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> $$f(x) = e^x$$는 모든 계도함수가 $$e^x$$이고 $$f^{(k)}(0) = 1$$이므로, $$a = 0$$에서의 테일러 다항식은 $$P_n(x) = \sum_{k=0}^n \dfrac{x^k}{k!}$$이다. 나머지는 $$0$$과 $$x$$ 사이의 어떤 $$c$$에 대해 $$R_n(x) = \dfrac{e^c}{(n+1)!}x^{n+1}$$이다. 고정된 $$x$$에서 $$\lvert R_n(x)\rvert \leq \dfrac{e^{\lvert x\rvert}\lvert x\rvert^{n+1}}{(n+1)!} \to 0$$ ($$n \to \infty$$) 이므로

$$e^x = \sum_{k=0}^{\infty}\frac{x^k}{k!}$$

이 모든 실수 $$x$$에서 성립한다. 같은 방법으로 $$\sin x = \sum_{k=0}^\infty \dfrac{(-1)^k}{(2k+1)!}x^{2k+1}$$, $$\cos x = \sum_{k=0}^\infty \dfrac{(-1)^k}{(2k)!}x^{2k}$$를 얻는다.

</div>

예시 3에서 본 것처럼, $$n \to \infty$$일 때 나머지 $$R_n(x) \to 0$$이면 함수는 무한급수

$$f(x) = \sum_{k=0}^{\infty}\frac{f^{(k)}(a)}{k!}(x-a)^k$$

로 표현되며, 이를 $$f$$의 *테일러 급수<sub>Taylor series</sub>*라 한다. 그러나 모든 매끄러운 함수가 자신의 테일러 급수와 같지는 않으며, 이 미묘한 문제와 멱급수의 수렴 이론은 [§멱급수](/ko/math/calculus/power_series)에서, 그리고 엄밀한 형태로는 해석학 [\[해석학\] §멱급수와 해석함수](/ko/math/analysis/power_series)에서 다룬다. 본 글의 나머지항 평가는 적분을 도입하면 [§미적분의 기본정리](/ko/math/calculus/fundamental_theorem_of_calculus)를 통해 적분형 나머지로도 표현된다.
