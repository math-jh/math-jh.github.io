---
title: "멱급수"
description: "변수의 거듭제곱으로 이루어진 멱급수를 정의하고, 수렴반경을 비판정으로 결정한다. 수렴반경 안에서 항별 미분과 적분이 가능함을 받아들이고, 이를 통해 기본 함수들의 멱급수 전개를 얻는다."
excerpt: "멱급수와 수렴반경, 항별 미분·적분, 멱급수 전개"

categories: [Math / Calculus]
permalink: /ko/math/calculus/power_series
sidebar: 
    nav: "calculus-ko"

header:
    overlay_image: /assets/images/Math/Calculus/Power_Series.png
    overlay_filter: 0.5

date: 2026-06-02
last_modified_at: 2026-06-02
weight: 15

published: false
---

[§무한급수](/ko/math/calculus/series)의 각 항을 변수 $$x$$의 거듭제곱으로 두면, 수 대신 함수를 정의하는 급수가 된다. 멱급수는 다항식을 무한 차수로 확장한 것으로, [§테일러 정리](/ko/math/calculus/taylor_theorem)에서 본 함수의 다항식 근사를 극한까지 밀고 간 형태이다.

## 멱급수와 수렴반경

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 중심 $$a$$에서의 *멱급수<sub>power series</sub>*는 계수 $$(c_n)$$에 대해

$$\sum_{n=0}^{\infty} c_n (x - a)^n$$

꼴의 급수이다. 이 급수가 수렴하는 $$x$$들의 모임에서 그 합은 $$x$$의 함수를 정의한다.

</div>

멱급수가 수렴하는 범위는 언제나 중심을 둘러싼 구간이다.

<div class="proposition" markdown="1">

<ins id="thm2">**정리 2 (수렴반경)**</ins> 각 멱급수 $$\sum c_n (x-a)^n$$에 대하여 $$0 \leq R \leq \infty$$인 *수렴반경<sub>radius of convergence</sub>* $$R$$이 존재하여, $$\lvert x - a\rvert < R$$이면 (절대)수렴하고 $$\lvert x - a\rvert > R$$이면 발산한다. $$\left\lvert\dfrac{c_{n+1}}{c_n}\right\rvert \to L$$이면 $$R = 1/L$$이다 ($$L = 0$$이면 $$R = \infty$$).

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

비판정 ([§무한급수, ⁋정리 4](/ko/math/calculus/series#thm4))을 항 $$c_n(x-a)^n$$에 적용하면, 연속한 항의 비의 절댓값이 $$\left\lvert\dfrac{c_{n+1}}{c_n}\right\rvert\lvert x - a\rvert \to L\lvert x - a\rvert$$이다. 이 값이 $$1$$보다 작으면, 곧 $$\lvert x - a\rvert < 1/L$$이면 절대수렴하고, $$1$$보다 크면 발산한다. 따라서 $$R = 1/L$$이다. (일반적으로는 근판정으로 $$R = 1/\limsup\lvert c_n\rvert^{1/n}$$이 성립한다.)

</details>

수렴반경의 경계 $$\lvert x - a\rvert = R$$에서의 수렴 여부는 급수마다 따로 살펴야 한다.

## 항별 미분과 적분

멱급수가 정의하는 함수는 수렴반경 안에서 마치 다항식처럼 다룰 수 있다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> $$f(x) = \sum_{n=0}^\infty c_n (x-a)^n$$이 수렴반경 $$R > 0$$을 가지면, $$f$$는 $$\lvert x - a\rvert < R$$에서 미분가능하며 항별로 미분·적분할 수 있다. 즉

$$f'(x) = \sum_{n=1}^\infty n\,c_n (x-a)^{n-1}, \qquad \int f(x)\,dx = C + \sum_{n=0}^\infty \frac{c_n}{n+1}(x-a)^{n+1}$$

이고 두 급수의 수렴반경도 $$R$$이다.

</div>

이 사실의 엄밀한 근거는 멱급수가 수렴반경 안에서 *균등수렴*한다는 데 있으며, 그 증명은 해석학 [\[해석학\] §멱급수와 해석함수](/ko/math/analysis/power_series)에서 다룬다.

<div class="example" markdown="1">

<ins id="ex4">**예시 4**</ins> 기하급수 $$\dfrac{1}{1 - x} = \sum_{n=0}^\infty x^n$$ ($$\lvert x\rvert < 1$$) 을 항별 적분하면 $$-\ln(1 - x) = \sum_{n=1}^\infty \dfrac{x^n}{n}$$을 얻고, $$\dfrac{1}{1 + x^2} = \sum_{n=0}^\infty (-1)^n x^{2n}$$을 항별 적분하면 $$\arctan x = \sum_{n=0}^\infty \dfrac{(-1)^n}{2n+1}x^{2n+1}$$을 얻는다.

</div>

명제 3을 반복하면 $$c_n = \dfrac{f^{(n)}(a)}{n!}$$이 따르므로, 멱급수로 표현되는 함수는 자신의 테일러 급수와 일치한다. 이런 함수를 *해석함수*라 하며, 그 이론은 [\[해석학\] §멱급수와 해석함수](/ko/math/analysis/power_series)에서 다룬다. 지금까지의 미적분이 한 변수에 관한 것이었다면, 다음 글 [§다변수함수와 편미분](/ko/math/calculus/partial_derivatives)에서는 여러 변수의 함수로 넘어간다.
