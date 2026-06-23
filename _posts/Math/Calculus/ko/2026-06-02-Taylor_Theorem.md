---
title: "테일러 정리"
description: "함수를 다항식으로 근사하는 테일러 다항식을 정의하고, 라그랑주 나머지를 가진 테일러 정리를 코시 평균값 정리로 증명한다. 초등함수의 매클로린 전개, 나머지의 평가, 극한·근사 계산에의 응용을 다룬다."
excerpt: "테일러 다항식, 라그랑주 나머지, 매클로린 전개, 근사와 극한"

categories: [Math / Calculus]
permalink: /ko/math/calculus/taylor_theorem
sidebar: 
    nav: "calculus-ko"

date: 2026-06-02
weight: 10

drift_needed: true

published: false
---

[§미분과 도함수](/ko/math/calculus/derivatives)에서 미분계수 $$f'(a)$$가 함수의 일차 근사 $$f(x) \approx f(a) + f'(a)(x-a)$$를 준다고 보았다. 이는 그래프를 접선으로 대신하는 것인데, 접선은 곡선의 휘어짐을 담지 못한다. 더 높은 계도함수를 동원하여 함수를 더 높은 차수의 다항식으로 근사하고, 그 오차를 정량적으로 통제하는 것이 테일러 정리이다. 다항식은 사칙연산만으로 계산되므로, 복잡한 초등함수를 다항식으로 바꾸는 이 도구는 근사 계산·극한·미분방정식 등 미적분학 전반에서 쓰인다.

## 테일러 다항식

함수 $$f$$가 점 $$a$$에서 $$n$$번 미분가능하면, $$a$$에서 함숫값과 처음 $$n$$개의 도함수 값을 $$f$$와 똑같이 갖는 차수 $$n$$의 다항식을 만들 수 있다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> $$f$$가 점 $$a$$에서 $$n$$번 미분가능할 때, $$f$$의 $$a$$에서의 *$$n$$차 테일러 다항식<sub>Taylor polynomial</sub>*은

$$P_n(x) = \sum_{k=0}^{n} \frac{f^{(k)}(a)}{k!}(x - a)^k = f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2 + \cdots + \frac{f^{(n)}(a)}{n!}(x-a)^n$$

이다. 중심이 $$a = 0$$인 경우를 특히 *매클로린 다항식<sub>Maclaurin polynomial</sub>*이라 한다.

</div>

$$P_n$$은 $$k = 0, 1, \ldots, n$$에 대해 $$P_n^{(k)}(a) = f^{(k)}(a)$$를 만족하는 차수 $$\leq n$$의 유일한 다항식이다. 실제로 $$(x-a)^k$$를 $$k$$번 미분하면 $$k!$$, 그 이상 미분하면 $$0$$, 그 미만으로 미분한 뒤 $$x=a$$를 넣으면 $$0$$이 되므로, $$P_n^{(k)}(a)$$는 정확히 $$k$$번째 항에서만 $$f^{(k)}(a)$$를 남긴다. $$n = 1$$이면 $$P_1(x) = f(a) + f'(a)(x-a)$$로 접선, 곧 일차 근사와 같다. 차수가 올라갈수록 $$P_n$$은 $$a$$ 근방에서 $$f$$에 더 밀착한다.

## 테일러 정리

근사 $$f \approx P_n$$의 오차 $$R_n(x) = f(x) - P_n(x)$$를 고계도함수로 정확히 표현하는 것이 다음 정리이다.

<div class="proposition" markdown="1">

<ins id="thm2">**정리 2 (테일러 정리, 라그랑주 나머지)**</ins> $$f$$가 $$a$$와 $$x$$를 포함하는 구간에서 $$n+1$$번 미분가능하면, $$a$$와 $$x$$ 사이의 어떤 $$c$$에 대하여

$$f(x) = \sum_{k=0}^{n} \frac{f^{(k)}(a)}{k!}(x-a)^k + R_n(x), \qquad R_n(x) = \frac{f^{(n+1)}(c)}{(n+1)!}(x - a)^{n+1}$$

이 성립한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$x \neq a$$를 고정하고, $$a$$와 $$x$$ 사이의 변수 $$t$$에 대해 두 보조함수

$$g(t) = f(x) - \sum_{k=0}^{n}\frac{f^{(k)}(t)}{k!}(x-t)^k, \qquad h(t) = (x - t)^{n+1}$$

을 둔다. 끝값은 $$g(x) = 0$$, $$g(a) = f(x) - P_n(x) = R_n(x)$$이고 $$h(x) = 0$$, $$h(a) = (x-a)^{n+1}$$이다. $$g$$를 미분하면 인접한 항들이 망원합처럼 상쇄되어

$$g'(t) = -\frac{f^{(n+1)}(t)}{n!}(x - t)^n$$

만 남고, $$h'(t) = -(n+1)(x-t)^n$$이다. [§평균값 정리, ⁋정리 6](/ko/math/calculus/mean_value_theorem#thm6)를 $$a$$와 $$x$$ 사이에 적용하면

$$\bigl(g(x) - g(a)\bigr)h'(c) = \bigl(h(x) - h(a)\bigr)g'(c)$$

인 $$c$$가 존재한다. 값을 대입하면

$$(-R_n(x))\bigl(-(n+1)(x-c)^n\bigr) = \bigl(-(x-a)^{n+1}\bigr)\left(-\frac{f^{(n+1)}(c)}{n!}(x-c)^n\right)$$

이고, 양변의 $$(x-c)^n$$을 소거하여 정리하면 $$R_n(x) = f^{(n+1)}(c)(x-a)^{n+1}/(n+1)!$$을 얻는다.

</details>

$$n = 0$$인 경우의 테일러 정리는 정확히 평균값 정리 ([§평균값 정리, ⁋정리 4](/ko/math/calculus/mean_value_theorem#thm4))이다. 따라서 테일러 정리는 평균값 정리를 고계도함수로 끌어올린 것으로 볼 수 있으며, $$R_n$$이 $$(x-a)^{n+1}$$에 비례하므로 차수가 높을수록 근방에서 오차가 빠르게 줄어든다.

## 초등함수의 매클로린 전개

나머지항을 평가하여 $$n \to \infty$$에서 $$R_n(x) \to 0$$임을 보이면, 함수가 무한급수와 일치한다. 그 무한급수를 $$f$$의 *테일러 급수* (중심이 $$0$$이면 매클로린 급수) 라 한다.

<div class="example" markdown="1">

<ins id="ex3">**예시 3 (지수함수)**</ins> $$f(x) = e^x$$는 모든 계도함수가 $$e^x$$이고 $$f^{(k)}(0) = 1$$이므로, 매클로린 다항식은 $$P_n(x) = \sum_{k=0}^n x^k/k!$$이다. 나머지는 $$0$$과 $$x$$ 사이의 어떤 $$c$$에 대해 $$R_n(x) = e^c x^{n+1}/(n+1)!$$이고, 고정된 $$x$$에서

$$\lvert R_n(x)\rvert \leq \frac{e^{\lvert x\rvert}\lvert x\rvert^{n+1}}{(n+1)!} \to 0 \qquad (n \to \infty)$$

이므로 모든 실수 $$x$$에서

$$e^x = \sum_{k=0}^{\infty}\frac{x^k}{k!}$$

이 성립한다. 특히 $$x = 1$$이면 $$e = \sum_{k=0}^\infty 1/k!$$이다.

</div>

<div class="example" markdown="1">

<ins id="ex4">**예시 4 (삼각함수)**</ins> $$\sin x$$는 도함수가 $$\cos x, -\sin x, -\cos x, \sin x$$로 주기적이라 $$f^{(k)}(0)$$이 $$0, 1, 0, -1$$을 반복한다. 모든 계도함수가 $$\lvert f^{(n+1)}\rvert \leq 1$$로 유계이므로 [예시 3](#ex3)과 같은 논법으로 나머지가 $$0$$으로 가, 모든 $$x$$에서

$$\sin x = \sum_{k=0}^\infty \frac{(-1)^k x^{2k+1}}{(2k+1)!}, \qquad \cos x = \sum_{k=0}^\infty \frac{(-1)^k x^{2k}}{(2k)!}$$

이다.

</div>

<div class="example" markdown="1">

<ins id="ex5">**예시 5 (로그·이항)**</ins> $$\ln(1+x)$$는 $$f^{(k)}(0) = (-1)^{k-1}(k-1)!$$이므로

$$\ln(1+x) = \sum_{k=1}^\infty \frac{(-1)^{k-1}}{k} x^k \qquad (-1 < x \leq 1)$$

이고, 일반화된 이항급수는 실수 $$\alpha$$에 대해

$$(1+x)^\alpha = \sum_{k=0}^\infty \binom{\alpha}{k} x^k, \qquad \binom{\alpha}{k} = \frac{\alpha(\alpha-1)\cdots(\alpha-k+1)}{k!} \qquad (\lvert x\rvert < 1)$$

이다. 특수한 경우로 $$\alpha = -1$$은 기하급수 $$1/(1+x) = \sum_k (-1)^k x^k$$를, $$\alpha = 1/2$$은 $$\sqrt{1+x} = 1 + x/2 - x^2/8 + \cdots$$를 준다. 이 전개들은 무한급수이므로 수렴역이 제한됨에 유의한다 ($$e^x, \sin, \cos$$는 모든 $$x$$에서 수렴).

</div>

## 나머지의 평가와 수렴

매끄럽다고 해서 테일러 급수가 항상 함수와 일치하지는 않는다. 일치 여부는 전적으로 나머지 $$R_n$$의 거동에 달려 있다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> $$f$$가 $$a$$를 포함하는 구간 $$I$$에서 무한히 미분가능하고, 어떤 상수 $$M$$에 대해 모든 $$n$$과 모든 $$x \in I$$에서 $$\lvert f^{(n)}(x)\rvert \leq M$$이면, $$f$$는 $$I$$에서 자신의 테일러 급수와 일치한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

테일러 정리의 나머지는

$$\lvert R_n(x)\rvert = \frac{\lvert f^{(n+1)}(c)\rvert}{(n+1)!}\lvert x-a\rvert^{n+1} \leq \frac{M\,\lvert x-a\rvert^{n+1}}{(n+1)!}$$

이다. 우변은 고정된 $$x$$에서 $$n \to \infty$$일 때 $$0$$으로 가므로 ([§수열의 극한, ⁋예시 6](/ko/math/calculus/sequences#ex6)의 $$r^n/n! \to 0$$), $$R_n(x) \to 0$$이고 부분합이 $$f(x)$$로 수렴한다.

</details>

[명제 6](#prop6)은 $$\sin, \cos$$ (도함수가 모두 $$1$$로 유계) 의 전개를 즉시 정당화한다. 그러나 도함수가 유계가 아니면 사정이 달라진다. $$f(x) = e^{-1/x^2}$$ ($$f(0)=0$$) 은 $$0$$에서 모든 계도함수가 $$0$$이어서 매클로린 급수가 항등적으로 $$0$$이지만 $$f$$ 자신은 $$0$$이 아니므로, 테일러 급수가 함수와 일치하지 않는다. 매끄러움이 해석성을 보장하지 못하는 것이다 ([§멱급수](/ko/math/calculus/power_series)).

## 응용: 근사와 극한

나머지 평가는 근삿값의 오차를 보증한다. 가령 $$\sin(0.1)$$을 $$P_3(x) = x - x^3/6$$로 근사하면 4차 나머지가 $$\lvert R_3(0.1)\rvert \leq (0.1)^4/4! \approx 4.2\times 10^{-6}$$이라 소수점 다섯째 자리까지 정확하고, $$e = \sum_k 1/k!$$를 처음 $$n+1$$항에서 끊은 오차는 $$\lvert R_n(1)\rvert \leq 3/(n+1)!$$ ($$e^c < 3$$) 이라 $$n = 9$$만 해도 $$3/10! \approx 8\times 10^{-7}$$ 이하로, 계승 분모 덕에 수렴이 매우 빠르다.

테일러 전개는 $$0/0$$ 꼴 극한에도 강력하여, 분자·분모를 각각 전개해 최저차항을 비교하면 [§도함수의 응용, ⁋정리 6](/ko/math/calculus/applications_of_derivatives#thm6)를 거듭 적용하지 않고도 극한을 읽어낼 수 있다.

<div class="example" markdown="1">

<ins id="ex7">**예시 7 (극한)**</ins> 극한 $$\lim_{x\to 0}(e^x - 1 - x)/x^2$$를 구하자. [예시 3](#ex3)에서 $$e^x = 1 + x + x^2/2 + x^3/6 + \cdots$$이므로

$$\frac{e^x - 1 - x}{x^2} = \frac{x^2/2 + x^3/6 + \cdots}{x^2} = \frac12 + \frac{x}{6} + \cdots \to \frac12$$

이다. 로피탈 정리를 두 번 적용한 결과와 일치하되, 전개는 고차 정보까지 한눈에 보여준다.

</div>

테일러 정리는 나머지를 명시적으로 주는 라그랑주 형태 외에, 정성적인 *페아노 형태*로도 자주 쓰인다. $$f$$가 $$a$$에서 $$n$$번 미분가능하면

$$f(x) = P_n(x) + o\bigl((x-a)^n\bigr) \qquad (x \to a)$$

가 성립한다. 즉 오차가 $$(x-a)^n$$보다 빠르게 $$0$$으로 간다. 이 형태는 [예시 7](#ex7)처럼 극한을 계산할 때 나머지를 일일이 평가하지 않고 "$$o$$" 기호로 묶어 두기에 편리하다.

이처럼 테일러 정리는 함수를 다항식으로 바꾸어 계산을 단순화한다. 엄밀한 형태는 해석학 [\[해석학\] §평균값 정리와 테일러 정리](/ko/math/analysis/mean_value_theorem)와 [\[해석학\] §멱급수와 해석함수](/ko/math/analysis/power_series)에서 다룬다.
