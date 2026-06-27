---
title: "이상적분"
description: "적분 구간이 무한하거나 피적분함수가 발산하는 이상적분을 극한으로 정의하고, p-적분과 비교판정·극한비교·절대수렴으로 수렴을 판정한다. 수렴하는 이상적분으로 감마함수를 정의한다."
excerpt: "무한구간 이상적분, 특이적분, 비교판정, 절대수렴"

categories: [Math / Calculus]
permalink: /ko/math/calculus/improper_integrals
sidebar: 
    nav: "calculus-ko"

date: 2026-06-26
weight: 12
published: false
---

우리가 지금까지 살펴본 적분은 유한한 구간에서 유계인 함수에 대해 정의되었다. 그러나 구간이 무한히 뻗거나, 피적분함수가 한 점에서 무한히 커지는 경우에도 그 넓이를 논하고 싶을 때가 많다. 이번 글에서는 이를 유한 구간 적분의 극한을 통해 정의한다.

## 이상적분의 정의

우선 다음을 정의한다. 

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> $$f$$가 모든 $$t > a$$에서 $$[a, t]$$에서 적분가능할 때, 무한구간 *이상적분<sub>improper integral</sub>*을

$$\int_a^{\infty} f(x) dx = \lim_{t \to \infty}\int_a^t f(x) dx$$

으로 정의하고, 이 극한이 유한한 값으로 존재하면 이상적분이 *수렴*한다고 한다. 마찬가지로, 만일 $$f$$가 모든 $$t<b$$에서 $$[t,a]$$에서 적분가능할 때, 다음의 식

$$\int_{-\infty}^b f(x)dx=\lim_{t \to -\infty}\int_t^b f(x) dx$$

이 유한한 값으로 존재하면 이상적분이 수렴한다고 한다. 만일 어떠한 $$c$$에 대하여 두 이상적분

$$\int_{-\infty}^c f(x) dx,\qquad \int_c^{\infty} f(x) dx$$

이 각각 수렴할 경우 이들의 합 

$$\int_{-\infty}^c f(x) dx + \int_c^{\infty} f(x) dx$$

을 간략하게 다음의 식

$$\int_{-\infty}^{\infty} f(x) dx$$

으로 나타낸다. 

</div>

위의 정의에서 두 이상적분

$$\int_a^\infty f(x)dx,\qquad \int_{-\infty}^b f(x)dx$$

의 정의는 비교적 명확하다. 다소 애매할 수 있는 부분은 양쪽이 모두 무한대인 이상적분으로, 우선 우리는 이 적분이 정의된다면, 그 값은 분할점 $$c$$의 선택에 의존하지 않는다는 것을 알 수 있다. 이는 만일 다른 $$c'$$를 택하더라도,

$$\begin{aligned}\int_{-\infty}^c f(x)dx+\int_c^\infty f(x)dx&=\lim_{s\rightarrow-\infty}\int_s^c f(x)dx+\lim_{t\rightarrow \infty}\int_c^t f(x)dx\\&=\lim_{s\rightarrow-\infty}\left(\int_s^c f(x)dx+\int_c^{c'} f(x)dx\right)+\lim_{t\rightarrow \infty}\left(\int_c^t f(x)dx-\int_c^{c'} f(x)dx\right)\\&=\lim_{s\rightarrow-\infty}\int_s^{c'} f(x)dx+\lim_{t\rightarrow \infty}\int_{c'}^t f(x)dx\\&=\int_{-\infty}^{c'} f(x)dx+\int_{c'}^\infty f(x)dx\end{aligned}$$

가 되어 이 값이 같기 때문이다. 보다 주의를 기울일만한 곳은 이 양쪽 극한을 <em-ko>독립적으로</em-ko> 보낸다는 데에 있다. 예를 들어, 부호함수

$$\sgn(x)=\begin{cases}1&\text{if $x>0$}\\0&\text{if $x=0$}\\-1&\text{if $x<0$}\end{cases}$$

로 정의하면, 고정된 $$t>0$$에 대하여 이 함수를 $$-t$$부터 $$t$$까지 적분한 값은 $$0$$이고, 따라서

$$\lim_{t\rightarrow\infty}\int_{-t}^t \sgn(x)dx=0$$

이지만, 위의 정의에 따르면 $$\sgn$$의 이상적분은 정의되지 않는다. 가령 만일 우리가 $$-t$$에서 $$2t$$까지를 적분구간으로 둔 후 $$t\rightarrow\infty$$인 극한을 취했다면 이 극한이 발산했을 것이므로 이는 필수적인 제약이다. 

비슷하게 우리는 한 점에서 발산하는 함수의 적분 또한 극한값으로 정의한다. 

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> $$f$$가 $$c$$에서 무한히 커지지만 모든 $$t < c$$에서 $$[a, t]$$에서 적분가능할 때, *특이적분*을

$$\int_a^c f(x) dx = \lim_{t \to c^-}\int_a^t f(x) dx$$

으로 정의한다. 비슷하게 만일 $$f$$가 $$c$$에서 무한히 커지지만 모든 $$c<t$$에서 $$[t, b]$$에서 적분가능할 때, 그 특이적분을

$$\int_c^b f(x) dx = \lim_{t \to c^+}\int_t^b f(x) dx$$

으로 정의한다. 만일 $$[a,b]$$ 내부의 점 $$c$$에서 $$f$$가 무한히 커지는 경우, 이 특이적분을

$$\int_a^b f(x)dx=\lim_{t\rightarrow c^-}\int_a^t f(x)dx+\lim_{s\rightarrow c^+} \int_s^b f(x)dx$$

으로 정의한다. 

</div>

역시 $$c$$가 구간 내부에 있는 경우 위의 [정의 1](#def1)과 같은 미묘함이 여전히 존재한다. 가령

$$\lim_{t\rightarrow 0^-}\int_{-1}^t \frac{dx}{x}+\lim_{s\rightarrow 0^+}\int_s^1\frac{dx}{x}$$

은 각각이 정의되지 않지만, 만일

$$\lim_{t\rightarrow 0^+}\left(\int_{-1}^{-t} \frac{dx}{x}+\int_t^1\frac{dx}{x}\right)$$

와 같은 식으로 묶었다면 이 값이 $$0$$이 되는 문제가 생겼을 것이다. 

## 이상적분의 비교판정

많은 이상적분은 원시함수를 명시적으로 구할 수 없어 그 값을 직접 계산하기 어렵다. 그러나 수렴 여부만이라면 더 다루기 쉬운 함수와 비교하여 판정할 수 있다. 피적분함수가 음이 아니면 적분값이 적분구간에 대해 단조증가하므로, 급수에서와 같은 비교판정이 성립한다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3 (비교판정)**</ins> $$x \geq a$$에서 $$0 \leq f(x) \leq g(x)$$라 하자. $$\int_a^\infty g(x) dx$$가 수렴하면 $$\int_a^\infty f(x) dx$$도 수렴하고, $$\int_a^\infty f(x) dx$$가 발산하면 $$\int_a^\infty g(x) dx$$도 발산한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$F(t) = \int_a^t f(x) dx$$는 $$f \geq 0$$이므로 $$t$$에 대해 증가하고, [§적분, ⁋명제 11](/ko/math/calculus/integration#prop11)의 단조성에 의해

$$F(t) \leq \int_a^t g(x) dx \leq \int_a^\infty g(x) dx$$

로 위로 유계이다. 위로 유계인 증가함수는 $$t \to \infty$$에서 극한을 가지므로 $$\int_a^\infty f(x) dx$$가 수렴한다. 둘째 주장은 대우이다.

</details>

직접 부등식 $$0 \leq f \leq g$$를 세우기 어려울 때는 급수에서처럼 극한비교를 쓴다. 즉, 두 양함수가 $$f(x)/g(x) \to c$$ ($$0 < c < \infty$$) 를 만족하면 [§무한급수, ⁋명제 7](/ko/math/calculus/series#prop7)과 같은 논증으로 두 적분이 함께 수렴·발산하므로, 피적분함수가 $$x \to \infty$$에서 어떤 함수처럼 행동하는지만 알면 판정이 끝난다.

부호가 바뀌는 피적분함수는 절댓값을 취해 양항으로 환원한다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4 (절대수렴)**</ins> $$\int_a^\infty \lvert f(x)\rvert dx$$이 수렴하면 $$\int_a^\infty f(x) dx$$도 수렴한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$0 \leq f + \lvert f\rvert \leq 2\lvert f\rvert$$이므로 [명제 3](#prop3)으로 $$\int_a^\infty (f(x) + \lvert f(x)\rvert) dx$$이 수렴하고, $$\int_a^\infty f(x) dx = \int_a^\infty (f(x) + \lvert f(x)\rvert) dx - \int_a^\infty \lvert f(x)\rvert dx$$도 수렴한다.

</details>

역은 성립하지 않는다. $$\int_0^\infty \frac{\sin x}{x} dx = \frac\pi2$$는 수렴하지만 $$\int_0^\infty \lvert \sin x/x\rvert dx$$는 발산하므로 *조건수렴*이며, 이는 급수의 조건수렴에 대응한다.

위의 두 판정은 무한구간 적분에 대해 서술했지만, 치환을 거치면 끝점에서 발산하는 특이적분에도 그대로 적용된다. $$f$$가 좌측 끝점 $$c$$에서 특이한 $$\int_c^b f(x) dx$$에서 $$u = 1/(x - c)$$로 두면 $$x \to c^+$$가 $$u \to \infty$$에 대응하고, 적분구간의 방향까지 맞추면

$$\int_c^b f(x) dx = \int_{1/(b-c)}^\infty \frac{f(c + 1/u)}{u^2} du$$

로 무한구간 적분이 된다. 곱해진 $$u^{-2} > 0$$은 부등식과 절댓값을 보존하므로 [명제 3](#prop3)과 [명제 4](#prop4)가 특이적분의 수렴 판정에도 그대로 성립한다.

이 판정들이 실제로 쓰이려면 비교할 표준 함수가 있어야 하는데, 그 역할은 거의 항상 거듭제곱함수나 지수함수 $$e^{-x}$$가 맡는다. 그중 거듭제곱함수의 적분은 수렴과 발산을 가르는 (거의) sharp한 경계를 보여 준다.

<div class="example" markdown="1">

<ins id="ex5">**예시 5 (p-적분)**</ins> 거듭제곱의 이상적분은 무한구간과 특이점에서 정확히 반대의 경계를 보인다. 무한구간 $$\int_1^{\infty} x^{-p} dx$$는 $$p > 1$$에서 수렴하고 $$p \leq 1$$에서 발산하는 반면, 특이점을 포함하는 $$\int_0^1 x^{-p} dx$$는 거꾸로 $$p < 1$$에서 수렴하고 $$p \geq 1$$에서 발산한다. 이 계산은 둘 다 같은 원시함수에서 나오는데, $$p \neq 1$$이면

$$\int_1^t x^{-p} dx = \frac{t^{1-p} - 1}{1 - p}, \qquad \int_t^1 x^{-p} dx = \frac{1 - t^{1-p}}{1 - p}$$

이고, 좌측 이상적분의 경우 $$t \to \infty$$에서 $$p > 1$$일 때 $$t^{1-p}$$가 $$0$$으로 가고, 우측 특이적분의 경우 $$t \to 0^+$$에서 $$p < 1$$일 때 $$t^{1-p}$$가 $$0$$으로 수렴해 적분이 유한해진다. 이 때 각각의 수렴값은 

$$\int_1^\infty x^{-p} dx = \frac{1}{p - 1} \quad (p > 1), \qquad \int_0^1 x^{-p} dx = \frac{1}{1 - p} \quad (p < 1)$$

이다. 직관적으로 이는 무한구간에서는 큰 $$p$$가 빨리 감소해 수렴을 돕지만, 특이점 근처에서는 큰 $$p$$가 더 빨리 증가해 발산이 일어나는 것으로 볼 수 있으며, 이는 $$1/x$$와 $$1/x^2$$를 그린 다음의 그림에서 직관적으로 설명된다. 

![1/x와 1/x²의 그래프](/assets/images/Math/Calculus/Improper_Integrals-1.svg){:style="width:12.69em" class="invert" .align-center}

</div>

단 이 경계 $$p = 1$$은 약간 미묘한 것이다. 치환적분은 이상적분에도 그대로 쓸 수 있으므로, $$u = \ln x$$로 두면

$$\int_2^\infty \frac{dx}{x(\ln x)^p} = \int_{\ln 2}^\infty u^{-p} du$$

가 되어 이 값은 $$p > 1$$일 때 수렴하게 된다. 즉 $$p = 1$$인 $$1/x$$ 자체는 발산하지만 로그를 한 제곱 이상 붙이면 경계가 다시 수렴 쪽으로 옮겨 간다. 즉, 거듭제곱만 놓고 보면 $$p = 1$$이 정확한 경계이지만 로그 인자를 끼우면 더 미세하게 갈라지며, 이 때문에 우리는 앞에서 이 경계가 <em-ko>거의</em-ko> sharp하다고 말하였다. 

한편, 수렴하는 이상적분은 새로운 함수를 정의하는 데 쓰인다.

<div class="example" markdown="1">

<ins id="ex6">**예시 6 (감마함수)**</ins> 이상적분으로 정의된 다음의 함수

$$\Gamma(s) = \int_0^\infty x^{s-1}e^{-x} dx$$

는 $$s > 0$$에서 수렴한다. $$0$$ 근처는 $$x^{s-1}$$의 특이적분이 $$s > 0$$에서 수렴하고 ([예시 5](#ex5)), $$\infty$$ 근처는 $$e^{-x}$$가 거듭제곱을 압도하기 때문이다. 부분적분으로

$$\Gamma(s+1) = \bigl[-x^s e^{-x}\bigr]_0^\infty + s\int_0^\infty x^{s-1}e^{-x} dx = s \Gamma(s)$$

이고 $$\Gamma(1) = \int_0^\infty e^{-x} dx = 1$$이므로 $$\Gamma(n) = (n-1)!$$이다. 즉 감마함수는 팩토리얼을 실수로 확장한다.

</div>
