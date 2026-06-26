---
title: "이상적분"
description: "적분 구간이 무한하거나 피적분함수가 발산하는 이상적분을 극한으로 정의하고, p-적분과 비교판정·극한비교·절대수렴으로 수렴을 판정한다. 무한급수의 적분판정과 감마함수와의 연관을 본다."
excerpt: "무한구간 이상적분, 특이적분, 비교판정, 절대수렴"

categories: [Math / Calculus]
permalink: /ko/math/calculus/improper_integrals
sidebar: 
    nav: "calculus-ko"

date: 2026-06-02
weight: 12
published: false
---

[§적분](/ko/math/calculus/integration)은 유한한 구간에서 유계인 함수에 대해 정의되었다. 그러나 구간이 무한히 뻗거나 피적분함수가 한 점에서 무한히 커지는 경우에도 "넓이"를 논하고 싶을 때가 많다. 확률분포의 전체 질량이나 발산하는 함수 아래의 넓이가 그런 예이다. 이를 유한 구간 적분의 극한을 통해 정의하는 것이 이상적분이다.

## 이상적분의 정의

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> $$f$$가 모든 $$t > a$$에서 $$[a, t]$$에서 적분가능할 때, *무한구간 이상적분*을

$$\int_a^{\infty} f(x) dx = \lim_{t \to \infty}\int_a^t f(x) dx$$

으로 정의하고, 이 극한이 (유한한 값으로) 존재하면 이상적분이 *수렴*한다고 한다. $$\int_{-\infty}^b$$도 대칭적으로 정의하며, 양쪽이 무한할 때는 $$\int_{-\infty}^{\infty} f = \int_{-\infty}^c f + \int_c^{\infty} f$$로 두되 두 조각이 *각각* 수렴할 것을 요구한다.

</div>

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> $$f$$가 $$b$$에서 무한히 커지지만 모든 $$t < b$$에서 $$[a, t]$$에서 적분가능할 때, *특이적분*을

$$\int_a^{b} f(x) dx = \lim_{t \to b^-}\int_a^t f(x) dx$$

으로 정의한다. 특이점이 구간 내부에 있으면 그 점에서 둘로 나눈다.

</div>

이상적분의 수렴은 결국 적분의 극한이 존재하는가의 문제이다. 가령 $$\int_0^\infty \sin x dx$$는 $$\int_0^t \sin x dx = 1 - \cos t$$가 진동하므로 발산한다.

## 기준 적분과 비교판정

수렴·발산의 경계를 보여 주는 기준 예가 거듭제곱함수의 적분이다.

<div class="example" markdown="1">

<ins id="ex3">**예시 3 (p-적분)**</ins> $$\int_1^{\infty} x^{-p} dx$$는 $$p > 1$$일 때 수렴하고 $$p \leq 1$$일 때 발산한다. 실제로 $$p \neq 1$$이면 $$\int_1^t x^{-p} dx = (t^{1-p} - 1)/(1 - p)$$인데, $$t \to \infty$$일 때 $$t^{1-p}$$는 $$p > 1$$이면 $$0$$으로, $$p < 1$$이면 무한으로 간다. $$p = 1$$이면 $$\int_1^t x^{-1} dx = \ln t \to \infty$$로 발산한다. 따라서 $$p > 1$$에서만 수렴하며, 그 값은 $$1/(p-1)$$이다.

</div>

피적분함수가 음이 아니면, 적분값이 단조증가하므로 급수에서와 같은 비교판정이 성립한다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4 (비교판정)**</ins> $$x \geq a$$에서 $$0 \leq f(x) \leq g(x)$$라 하자. $$\int_a^\infty g$$가 수렴하면 $$\int_a^\infty f$$도 수렴하고, $$\int_a^\infty f$$가 발산하면 $$\int_a^\infty g$$도 발산한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$F(t) = \int_a^t f$$는 $$f \geq 0$$이므로 $$t$$에 대해 증가하고, 단조성 ([§적분, ⁋명제 11](/ko/math/calculus/integration#prop11))에 의해

$$F(t) \leq \int_a^t g \leq \int_a^\infty g$$

로 위로 유계이다. 위로 유계인 증가함수는 $$t \to \infty$$에서 극한을 가지므로 $$\int_a^\infty f$$가 수렴한다. 둘째 주장은 대우이다.

</details>

비교 대상은 거의 항상 [예시 3](#ex3)의 거듭제곱이나 지수함수 $$e^{-x}$$이다. 가령 $$\int_1^\infty e^{-x^2} dx$$는 $$x \geq 1$$에서 $$e^{-x^2} \leq e^{-x}$$이고 $$\int_1^\infty e^{-x} dx = e^{-1}$$이 수렴하므로 수렴하며, $$\int_1^\infty (x^2 + \sqrt x)^{-1} dx$$는 $$1/(x^2+\sqrt x) \leq 1/x^2$$이라 수렴한다. 비교할 함수를 직접 만들기 어려우면, 급수에서처럼 *[§무한급수, ⁋명제 7](/ko/math/calculus/series#prop7)*을 쓴다. $$f(x)/g(x) \to c$$ ($$0 < c < \infty$$) 이면 두 적분이 함께 수렴·발산하므로, 피적분함수가 $$x \to \infty$$에서 어떤 거듭제곱처럼 행동하는지만 보면 된다. 예를 들어 $$x/(x^3 - x + 2)$$를 $$g(x) = x^{-2}$$와 비교하면

$$\frac{x/(x^3 - x + 2)}{1/x^2} = \frac{x^3}{x^3 - x + 2} \xrightarrow{ x\to\infty } 1$$

이라, $$\int_1^\infty x/(x^3 - x + 2) dx$$는 $$\int_1^\infty x^{-2} dx$$ (수렴) 와 운명을 같이한다. 치환적분도 이상적분에 그대로 쓰여 비교 대상을 만든다. $$u = \ln x$$로 두면 $$\int_2^\infty \frac{dx}{x(\ln x)^p} = \int_{\ln 2}^\infty u^{-p} du$$로 환원되어 ([예시 3](#ex3)) $$p > 1$$에서만 수렴하니, $$1/x$$만으로는 끌어내지 못하던 $$p = 1$$ 경계가 로그를 한 제곱 더 붙여야 비로소 수렴 쪽으로 넘어감을 본다.

끝점에서 발산하는 특이적분에도 같은 거듭제곱이 기준이 되지만, 부등호 방향이 뒤집힌다.

<div class="example" markdown="1">

<ins id="ex5">**예시 5 (특이점에서의 p-적분)**</ins> $$\int_0^1 x^{-p} dx$$는 $$\int_t^1 x^{-p} dx$$의 $$t \to 0^+$$ 극한으로, $$p < 1$$이면 수렴하고 $$p \geq 1$$이면 발산한다. 무한구간([예시 3](#ex3))에서는 큰 $$p$$가 빨리 감소해 수렴을 돕지만, 특이점 근처에서는 큰 $$p$$가 더 빨리 폭발해 발산을 부른다. 가령 $$\int_0^1 x^{-1/2} dx = \bigl[2\sqrt x\bigr]_0^1 = 2$$로 수렴하지만, $$\int_0^1 x^{-1} dx$$는 발산한다.

</div>

부호가 바뀌는 피적분함수는 절댓값을 취해 양항으로 환원한다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6 (절대수렴)**</ins> $$\int_a^\infty \lvert f\rvert$$이 수렴하면 $$\int_a^\infty f$$도 수렴한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$0 \leq f + \lvert f\rvert \leq 2\lvert f\rvert$$이므로 비교판정으로 $$\int_a^\infty (f + \lvert f\rvert)$$이 수렴하고, $$\int_a^\infty f = \int_a^\infty (f + \lvert f\rvert) - \int_a^\infty \lvert f\rvert$$도 수렴한다.

</details>

역은 성립하지 않는다. $$\int_0^\infty \frac{\sin x}{x} dx = \frac\pi2$$는 수렴하지만 $$\int_0^\infty \lvert \sin x/x\rvert dx$$는 발산하므로 *조건수렴*이며, 이는 급수의 조건수렴에 대응한다.

## 감마함수와 적분판정

수렴하는 이상적분은 새로운 함수를 정의하거나 무한급수의 수렴을 판정하는 데 쓰인다.

<div class="example" markdown="1">

<ins id="ex7">**예시 7 (감마함수)**</ins> $$\Gamma(s) = \int_0^\infty x^{s-1}e^{-x} dx$$는 $$s > 0$$에서 수렴한다. $$0$$ 근처는 $$x^{s-1}$$의 특이적분이 $$s > 0$$에서 수렴하고 ([예시 5](#ex5)), $$\infty$$ 근처는 $$e^{-x}$$가 거듭제곱을 압도하기 때문이다. 부분적분으로

$$\Gamma(s+1) = \bigl[-x^s e^{-x}\bigr]_0^\infty + s\int_0^\infty x^{s-1}e^{-x} dx = s \Gamma(s)$$

이고 $$\Gamma(1) = \int_0^\infty e^{-x} dx = 1$$이므로 $$\Gamma(n) = (n-1)!$$이다. 즉 감마함수는 계승을 실수로 확장한다.

</div>

<div class="example" markdown="1">

<ins id="ex8">**예시 8 (적분판정)**</ins> 양의 감소 연속함수 $$f$$에 대해 $$\sum_n f(n)$$과 $$\int_1^\infty f$$가 함께 수렴·발산한다. 이를 $$f(x) = x^{-p}$$에 적용하면 [예시 3](#ex3)의 적분 판정이 곧바로 $$p$$-급수 $$\sum_n n^{-p}$$의 판정 ([§무한급수, ⁋예시 2](/ko/math/calculus/series#ex2)) 을 준다. 또 $$f(x) = 1/(x\ln x)$$이면 $$\int_2^\infty \frac{dx}{x\ln x} = \bigl[\ln\ln x\bigr]_2^\infty = \infty$$이므로 $$\sum_n 1/(n\ln n)$$도 발산한다.

</div>

마지막 두 예는 정의에 깔린 두 가지 미묘함을 드러낸다. 특이점이 구간 내부에 숨어 있거나, 대칭적 극한이 존재한다고 해서 이상적분이 수렴하는 것은 아니라는 점이다.

<div class="example" markdown="1">

<ins id="ex9">**예시 9 (내부 특이점)**</ins> 특이점이 적분 구간 *내부*에 있으면 반드시 그 점에서 나누어 각각의 수렴을 따져야 한다. $$\int_{-1}^1 x^{-2} dx$$을 무심코 $$\bigl[-x^{-1}\bigr]_{-1}^1 = -2$$로 계산하면 틀린다. 피적분함수가 양수인데 음수가 나오는 모순이다. $$x = 0$$에서 특이하므로 $$\int_{-1}^0 + \int_0^1$$로 나누면 각 조각이 $$\int_0^1 x^{-2} dx$$ ($$p = 2 \geq 1$$, 발산) 이므로 전체가 발산한다.

</div>

<div class="example" markdown="1">

<ins id="ex10">**예시 10 (대칭과 발산)**</ins> $$\int_{-\infty}^\infty \frac{x dx}{1 + x^2}$$의 피적분함수는 기함수이므로 대칭적 극한 $$\int_{-t}^t$$는 항상 $$0$$이 되어 *코시 주값*은 $$0$$이다. 그러나 [정의 1](#def1)은 두 조각이 *각각* 수렴할 것을 요구하는데,

$$\int_0^t \frac{x dx}{1+x^2} = \frac12\bigl[\ln(1+x^2)\bigr]_0^t = \frac12\ln(1 + t^2) \xrightarrow{ t\to\infty } \infty$$

이라 $$\int_0^\infty$$ 조각이 발산한다. 따라서 이 이상적분은 (표준적 의미로) 발산한다. 코시 주값이 존재한다고 해서 이상적분이 수렴하는 것은 아님을 보여 주는 예이다.

</div>

이처럼 이상적분의 수렴 이론은 무한급수의 그것과 평행하며 (적분판정, [예시 8](#ex8)), 수렴하는 이상적분은 [예시 7](#ex7) 처럼 새로운 함수를 정의하는 데 쓰인다. 함수를 무한히 더하거나 적분하는 이런 극한 과정 전반의 엄밀한 취급은 해석학에서 이루어지며, 적분판정의 일반적 서술은 [\[해석학\] §무한급수](/ko/math/analysis/series)로 이어진다.
</content>
</invoke>
