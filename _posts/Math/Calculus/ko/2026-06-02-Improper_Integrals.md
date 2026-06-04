---
title: "이상적분"
description: "적분 구간이 무한하거나 피적분함수가 발산하는 이상적분을 극한으로 정의하고, p-적분과 비교판정·극한비교·절대수렴으로 수렴을 판정한다. 무한급수의 적분판정과 감마함수와의 연관을 본다."
excerpt: "무한구간 이상적분, 특이적분, 비교판정, 절대수렴"

categories: [Math / Calculus]
permalink: /ko/math/calculus/improper_integrals
sidebar: 
    nav: "calculus-ko"

date: 2026-06-02
last_modified_at: 2026-06-02
weight: 12

published: false
---

[§정적분](/ko/math/calculus/definite_integral)은 유한한 구간에서 유계인 함수에 대해 정의되었다. 그러나 구간이 무한히 뻗거나 피적분함수가 한 점에서 무한히 커지는 경우에도 "넓이"를 논하고 싶을 때가 많다 — 확률분포의 전체 질량, 발산하는 함수 아래의 넓이 등. 이를 유한 구간 적분의 극한을 통해 정의하는 것이 이상적분이다.

## 이상적분의 정의

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> $$f$$가 모든 $$t > a$$에서 $$[a, t]$$에서 적분가능할 때, *무한구간 이상적분*을

$$\int_a^{\infty} f(x)\,dx = \lim_{t \to \infty}\int_a^t f(x)\,dx$$

으로 정의하고, 이 극한이 (유한한 값으로) 존재하면 이상적분이 *수렴*한다고 한다. $$\int_{-\infty}^b$$도 대칭적으로 정의하며, 양쪽이 무한할 때는 $$\int_{-\infty}^{\infty} f = \int_{-\infty}^c f + \int_c^{\infty} f$$로 두되 두 조각이 *각각* 수렴할 것을 요구한다.

</div>

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> $$f$$가 $$b$$에서 무한히 커지지만 모든 $$t < b$$에서 $$[a, t]$$에서 적분가능할 때, *특이적분*을

$$\int_a^{b} f(x)\,dx = \lim_{t \to b^-}\int_a^t f(x)\,dx$$

으로 정의한다. 특이점이 구간 내부에 있으면 그 점에서 둘로 나눈다.

</div>

이상적분의 수렴은 결국 적분의 극한이 존재하는가의 문제이다. $$\int_0^\infty \sin x\,dx$$처럼 극한이 진동하면 발산한다.

## 기준 적분과 비교판정

수렴·발산의 경계를 보여 주는 기준 예가 거듭제곱함수의 적분이다.

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> $$\displaystyle\int_1^{\infty}\frac{dx}{x^p}$$는 $$p > 1$$일 때 수렴하고 $$p \leq 1$$일 때 발산한다. 실제로 $$p \neq 1$$이면 $$\int_1^t x^{-p}\,dx = \dfrac{t^{1-p} - 1}{1 - p}$$인데, $$t \to \infty$$일 때 $$t^{1-p}$$는 $$p > 1$$이면 $$0$$으로, $$p < 1$$이면 무한으로 간다. $$p = 1$$이면 $$\int_1^t \tfrac1x\,dx = \ln t \to \infty$$로 발산한다. 따라서 $$p > 1$$에서만 수렴하며, 그 값은 $$\dfrac{1}{p-1}$$이다.

</div>

피적분함수가 음이 아니면, 적분값이 단조증가하므로 급수에서와 같은 비교판정이 성립한다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4 (비교판정)**</ins> $$x \geq a$$에서 $$0 \leq f(x) \leq g(x)$$라 하자. $$\int_a^\infty g$$가 수렴하면 $$\int_a^\infty f$$도 수렴하고, $$\int_a^\infty f$$가 발산하면 $$\int_a^\infty g$$도 발산한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$F(t) = \int_a^t f$$는 $$f \geq 0$$이므로 $$t$$에 대해 증가하고, 단조성 ([§정적분, ⁋명제 4](/ko/math/calculus/definite_integral#prop4))에 의해

$$F(t) \leq \int_a^t g \leq \int_a^\infty g$$

로 위로 유계이다. 위로 유계인 증가함수는 $$t \to \infty$$에서 극한을 가지므로 $$\int_a^\infty f$$가 수렴한다. 둘째 주장은 대우이다.

</details>

비교할 함수를 직접 만들기 어려우면, 급수에서처럼 *극한비교판정*을 쓴다: $$\dfrac{f(x)}{g(x)} \to c$$ ($$0 < c < \infty$$) 이면 두 적분이 함께 수렴·발산한다.

<div class="example" markdown="1">

<ins id="ex5">**예시 5 (수렴 계산)**</ins> 직접 계산되는 예로 $$\displaystyle\int_0^\infty e^{-x}\,dx = \lim_{t\to\infty}\bigl[-e^{-x}\bigr]_0^t = \lim_{t\to\infty}(1 - e^{-t}) = 1$$이고, $$\displaystyle\int_1^\infty \frac{dx}{x^2} = \bigl[-\tfrac1x\bigr]_1^\infty = 1$$이다 (예시 3에서 $$p = 2$$). 비교판정의 예로 $$\int_1^\infty e^{-x^2}\,dx$$는 $$x \geq 1$$에서 $$e^{-x^2} \leq e^{-x}$$이고 $$\int_1^\infty e^{-x}$$가 수렴하므로 수렴한다.

</div>

<div class="example" markdown="1">

<ins id="ex6">**예시 6 (특이적분)**</ins> 끝점에서 발산하는 경우도 거듭제곱이 기준이다. $$\displaystyle\int_0^1 \frac{dx}{x^p}$$는 $$\int_t^1 x^{-p}\,dx$$의 $$t \to 0^+$$ 극한으로, $$p < 1$$이면 수렴하고 $$p \geq 1$$이면 발산한다 (무한구간의 경우와 부등호 방향이 반대임에 유의). 가령 $$\displaystyle\int_0^1 \frac{dx}{\sqrt x} = \bigl[2\sqrt x\bigr]_0^1 = 2$$로 수렴하지만, $$\int_0^1 \tfrac{dx}{x}$$는 발산한다.

</div>

<div class="example" markdown="1">

<ins id="ex7">**예시 7 (양쪽 무한)**</ins> $$\displaystyle\int_{-\infty}^{\infty} \frac{dx}{1 + x^2} = \lim_{t\to\infty}\bigl[\arctan x\bigr]_{-t}^{t} = \frac\pi2 - \Bigl(-\frac\pi2\Bigr) = \pi$$이다.

</div>

부호가 바뀌는 피적분함수는 절댓값을 취해 양항으로 환원한다.

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> $$\int_a^\infty \lvert f\rvert$$이 수렴하면 $$\int_a^\infty f$$도 수렴한다 (절대수렴).

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$0 \leq f + \lvert f\rvert \leq 2\lvert f\rvert$$이므로 비교판정으로 $$\int_a^\infty (f + \lvert f\rvert)$$이 수렴하고, $$\int_a^\infty f = \int_a^\infty (f + \lvert f\rvert) - \int_a^\infty \lvert f\rvert$$도 수렴한다.

</details>

## 더 많은 예와 응용

비교판정과 극한비교판정은 직접 적분되지 않는 경우에 위력을 발휘한다.

<div class="example" markdown="1">

<ins id="ex9">**예시 9 (비교·극한비교)**</ins> $$\displaystyle\int_1^\infty \frac{dx}{x^2 + \sqrt x}$$는 $$\dfrac{1}{x^2 + \sqrt x} \leq \dfrac{1}{x^2}$$이고 $$\int_1^\infty x^{-2}$$가 수렴하므로 수렴한다. 한편 $$\displaystyle\int_1^\infty \frac{dx}{\sqrt{x^2 + 1}}$$은 $$\dfrac{1}{\sqrt{x^2+1}} \big/ \dfrac1x \to 1$$이라 극한비교로 $$\int_1^\infty x^{-1}$$ (발산) 과 운명을 같이하여 발산한다.

</div>

<div class="example" markdown="1">

<ins id="ex10">**예시 10 (감마함수)**</ins> $$\Gamma(s) = \displaystyle\int_0^\infty x^{s-1}e^{-x}\,dx$$는 $$s > 0$$에서 수렴한다 ($$0$$ 근처는 $$x^{s-1}$$의 특이적분이 $$s>0$$에서 수렴, $$\infty$$ 근처는 $$e^{-x}$$가 압도). 부분적분으로

$$\Gamma(s+1) = \bigl[-x^s e^{-x}\bigr]_0^\infty + s\int_0^\infty x^{s-1}e^{-x}\,dx = s\,\Gamma(s)$$

이고 $$\Gamma(1) = \int_0^\infty e^{-x}\,dx = 1$$이므로 $$\Gamma(n) = (n-1)!$$이다. 즉 감마함수는 계승을 실수로 확장한다.

</div>

<div class="example" markdown="1">

<ins id="ex11">**예시 11 (적분판정)**</ins> 양의 감소 연속함수 $$f$$에 대해 $$\sum_n f(n)$$과 $$\int_1^\infty f$$가 함께 수렴·발산한다. 이를 $$f(x) = x^{-p}$$에 적용하면 예시 3의 적분 판정이 곧바로 $$p$$-급수 $$\sum n^{-p}$$의 판정 ([§무한급수, ⁋예시 2](/ko/math/calculus/series#ex2)) 을 준다. 또 $$f(x) = \dfrac{1}{x\ln x}$$이면 $$\int_2^\infty \dfrac{dx}{x\ln x} = \bigl[\ln\ln x\bigr]_2^\infty = \infty$$이므로 $$\sum \dfrac{1}{n\ln n}$$도 발산한다.

</div>

<div class="example" markdown="1">

<ins id="ex12">**예시 12 (치환으로 계산)**</ins> 치환적분은 이상적분에도 그대로 쓰인다. $$u = x^2$$로 두면

$$\int_0^\infty x\,e^{-x^2}\,dx = \frac12\int_0^\infty e^{-u}\,du = \frac12$$

이고, $$u = \ln x$$로 두면 $$\displaystyle\int_e^\infty \frac{dx}{x(\ln x)^2} = \int_1^\infty \frac{du}{u^2} = 1$$이다.

</div>

<div class="example" markdown="1">

<ins id="ex13">**예시 13 (내부 특이점)**</ins> 특이점이 적분 구간 *내부*에 있으면 반드시 그 점에서 나누어 각각의 수렴을 따져야 한다. $$\displaystyle\int_{-1}^1 \frac{dx}{x^2}$$을 무심코 $$\bigl[-\tfrac1x\bigr]_{-1}^1 = -2$$로 계산하면 틀린다 — 피적분함수가 양수인데 음수가 나오는 모순이다. $$x = 0$$에서 특이하므로 $$\int_{-1}^0 + \int_0^1$$로 나누면 각 조각이 $$\int_0^1 x^{-2}$$ ($$p = 2 \geq 1$$, 발산) 이므로 전체가 발산한다.

</div>

## 더 많은 계산과 판정

지금까지의 정의·판정을 좀 더 다양한 피적분함수에 적용해 본다. 우선 무한구간과 끝점 특이성이 한 적분 안에 함께 나타나는 경우를 보자. 이때는 적분을 두 조각으로 나누어 각 끝에서의 거동을 따로 다스려야 한다.

<div class="example" markdown="1">

<ins id="ex14">**예시 14 (두 끝의 동시 처리)**</ins> $$\displaystyle\int_0^\infty \frac{dx}{\sqrt{x}\,(1+x)}$$를 살펴보자. 피적분함수는 $$x \to 0^+$$에서 $$\sim x^{-1/2}$$로 특이하고 $$x \to \infty$$에서 $$\sim x^{-3/2}$$로 감소하므로, 임의의 점 $$1$$에서 둘로 나눈다. $$0$$ 근처에서는

$$\frac{1}{\sqrt x\,(1+x)} \leq \frac{1}{\sqrt x}, \qquad \int_0^1 \frac{dx}{\sqrt x} = 2 < \infty$$

이라 수렴하고 (예시 6, $$p = \tfrac12 < 1$$), $$\infty$$ 근처에서는

$$\frac{1}{\sqrt x\,(1+x)} \leq \frac{1}{\sqrt x \cdot x} = \frac{1}{x^{3/2}}, \qquad \int_1^\infty \frac{dx}{x^{3/2}} < \infty$$

이라 수렴한다 (예시 3, $$p = \tfrac32 > 1$$). 두 조각이 모두 수렴하므로 전체가 수렴한다. 실제로 $$u = \sqrt x$$로 치환하면

$$\int_0^\infty \frac{dx}{\sqrt x\,(1+x)} = \int_0^\infty \frac{2\,du}{1 + u^2} = 2 \cdot \frac\pi2 = \pi$$

로 값까지 계산된다 (예시 7).

</div>

특이성이 어느 점에서 어떤 차수로 일어나는지 가늠하는 표준 도구가 극한비교판정이다. 다음 예는 피적분함수가 두 끝에서 서로 다른 거듭제곱처럼 행동하는 전형적인 상황이다.

<div class="example" markdown="1">

<ins id="ex15">**예시 15 (극한비교의 활용)**</ins> $$\displaystyle\int_1^\infty \frac{x\,dx}{x^3 - x + 2}$$의 수렴을 보자. $$x \to \infty$$에서 분모가 $$x^3$$처럼 커지므로 피적분함수는 $$x^{-2}$$처럼 행동할 것이다. 실제로 $$g(x) = x^{-2}$$와 비교하면

$$\frac{x/(x^3 - x + 2)}{1/x^2} = \frac{x^3}{x^3 - x + 2} = \frac{1}{1 - x^{-2} + 2x^{-3}} \xrightarrow{\;x\to\infty\;} 1$$

이고 극한이 $$0 < 1 < \infty$$이므로, 극한비교판정에 의해 주어진 적분은 $$\int_1^\infty x^{-2}\,dx$$ (수렴) 와 운명을 같이하여 수렴한다.

</div>

부분적분은 이상적분의 값을 닫힌 형태로 끌어내는 데 유용하다. 경계항이 극한에서 사라지는지를 반드시 확인해야 한다.

<div class="example" markdown="1">

<ins id="ex16">**예시 16 (부분적분)**</ins> $$\displaystyle\int_0^\infty x\,e^{-x}\,dx$$를 부분적분으로 계산한다. $$u = x$$, $$dv = e^{-x}\,dx$$로 두면 $$du = dx$$, $$v = -e^{-x}$$이고

$$\begin{aligned}
\int_0^t x\,e^{-x}\,dx &= \bigl[-x\,e^{-x}\bigr]_0^t + \int_0^t e^{-x}\,dx \\
&= -t\,e^{-t} + \bigl[-e^{-x}\bigr]_0^t \\
&= -t\,e^{-t} + (1 - e^{-t})
\end{aligned}$$

이다. $$t \to \infty$$일 때 $$t\,e^{-t} \to 0$$이고 $$e^{-t} \to 0$$이므로

$$\int_0^\infty x\,e^{-x}\,dx = 1$$

을 얻는다. 이는 예시 10의 $$\Gamma(2) = 1! = 1$$과 일치한다.

</div>

대칭성을 이용하면 계산이 크게 줄어든다. 우함수·기함수 여부를 먼저 살피는 습관이 도움이 된다.

<div class="example" markdown="1">

<ins id="ex17">**예시 17 (대칭과 발산)**</ins> $$\displaystyle\int_{-\infty}^\infty \frac{x\,dx}{1 + x^2}$$를 보자. 피적분함수는 기함수이므로 대칭적 극한 $$\int_{-t}^t$$는 항상 $$0$$이 되어 *코시 주값*은 $$0$$이다. 그러나 정의 1은 두 조각이 *각각* 수렴할 것을 요구하는데,

$$\int_0^t \frac{x\,dx}{1+x^2} = \tfrac12\bigl[\ln(1+x^2)\bigr]_0^t = \tfrac12\ln(1 + t^2) \xrightarrow{\;t\to\infty\;} \infty$$

이라 $$\int_0^\infty$$ 조각이 발산한다. 따라서 이 이상적분은 (표준적 의미로) 발산한다. 코시 주값이 존재한다고 해서 이상적분이 수렴하는 것은 아님을 보여 주는 예이다.

</div>

거듭제곱과 로그가 섞인 피적분함수의 수렴 경계도 자주 등장한다. 다음은 로그 인자가 거듭제곱의 경계 $$p = 1$$을 어떻게 미세하게 바꾸는지 보여 준다.

<div class="example" markdown="1">

<ins id="ex18">**예시 18 (로그 인자)**</ins> $$\displaystyle\int_2^\infty \frac{dx}{x(\ln x)^p}$$는 $$u = \ln x$$로 치환하면 $$du = dx/x$$이고

$$\int_2^\infty \frac{dx}{x(\ln x)^p} = \int_{\ln 2}^\infty \frac{du}{u^p}$$

이 되어, 무한구간 거듭제곱적분 (예시 3) 으로 환원된다. 따라서 이 적분은 $$p > 1$$일 때 수렴하고 $$p \leq 1$$일 때 발산한다. 특히 $$p = 1$$인 $$\int_2^\infty \frac{dx}{x\ln x}$$는 발산하며 (예시 11), 이는 $$\frac1x$$만으로는 수렴을 끌어내지 못하던 $$p = 1$$ 경계가 로그를 한 제곱 더 붙여야 비로소 수렴 쪽으로 넘어감을 보여 준다.

</div>

마지막으로, 적분 자체가 닫힌 형태로 계산되지 않더라도 부등식만으로 값의 범위를 가둘 수 있다. 다음 예는 수렴을 보이는 동시에 적분값의 상계를 준다.

<div class="example" markdown="1">

<ins id="ex19">**예시 19 (수렴값의 범위 추정)**</ins> $$\displaystyle\int_0^\infty e^{-x^2}\,dx$$의 수렴과 상계를 동시에 얻어 보자. $$[0,1]$$에서는 연속이라 적분이 유한하고, $$x \geq 1$$에서는 $$x^2 \geq x$$이므로 $$e^{-x^2} \leq e^{-x}$$이다. 따라서

$$\begin{aligned}
\int_0^\infty e^{-x^2}\,dx &= \int_0^1 e^{-x^2}\,dx + \int_1^\infty e^{-x^2}\,dx \\
&\leq \int_0^1 1\,dx + \int_1^\infty e^{-x}\,dx \\
&= 1 + \bigl[-e^{-x}\bigr]_1^\infty = 1 + e^{-1}
\end{aligned}$$

로 수렴하며 그 값이 $$1 + e^{-1}$$ 이하임을 알 수 있다 (참고로 정확한 값은 $$\tfrac{\sqrt\pi}{2}$$이다). 이처럼 비교판정은 수렴 여부뿐 아니라 정량적 상계도 함께 준다.

</div>

절대수렴이 아니어도 수렴하는 이상적분이 있다. $$\displaystyle\int_0^\infty \frac{\sin x}{x}\,dx = \frac\pi2$$는 수렴하지만 $$\int_0^\infty \bigl\lvert\tfrac{\sin x}{x}\bigr\rvert\,dx$$는 발산하므로 *조건수렴*이며, 이는 급수의 조건수렴에 대응한다. 발산하는 적분에도 대칭적 극한으로 값을 부여하는 *코시 주값* 같은 정밀화가 있으나, 표준적 수렴과는 구별해야 한다.

이처럼 이상적분의 수렴 이론은 무한급수의 그것과 평행하며 (적분판정, 예시 11), 수렴하는 이상적분은 감마함수 (예시 10) 처럼 새로운 함수를 정의하는 데 쓰인다. 함수를 무한히 더하거나 적분하는 이런 극한 과정 전반의 엄밀한 취급은 해석학에서 이루어지며, 적분판정의 일반적 서술은 [\[해석학\] §무한급수](/ko/math/analysis/series)로 이어진다.
