---
title: "멱급수"
description: "변수의 거듭제곱으로 이루어진 멱급수와 수렴요경, 수렴역을 다룬다. 초등함수의 멱급수 전개, 계수의 유일성, 멱급수의 사칙연산, 해석함수의 정의를 논한다."
excerpt: "멱급수와 수렴요경, 초등함수의 전개, 해석함수"

categories: [Math / Calculus]
permalink: /ko/math/calculus/power_series
sidebar: 
    nav: "calculus-ko"

date: 2026-06-02
weight: 5

published: false
---

[§무한급수](/ko/math/calculus/series)의 각 항을 변수 $$x$$의 거듭제곱으로 두면, 수 대신 함수를 정의하는 급수가 된다. 멱급수는 다항식을 무한 차수로 확장한 것으로, 함수를 극한까지 다항식으로 근사하는 길을 열어 준다. 미적분학에서 등장하는 거의 모든 초등함수가 멱급수로 표현되며, 이는 함수를 다루는 데 강력한 도구가 된다.

## 멱급수와 수렴반경

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 중심 $$a$$에서의 *멱급수<sub>power series</sub>*는 계수열 $$(c_n)_{n\geq 0}$$에 대해

$$\sum_{n=0}^{\infty} c_n (x - a)^n = c_0 + c_1(x-a) + c_2(x-a)^2 + \cdots$$

꼴의 급수이다. 이 급수가 수렴하는 $$x$$들의 모임을 *수렴역<sub>domain of convergence</sub>*이라 하고, 그 위에서 급수의 합은 $$x$$의 함수를 정의한다.

</div>

논의를 간단히 하기 위해 이후 $$a = 0$$인 경우, 즉 $$\sum c_n x^n$$을 주로 다룬다 (일반적인 경우는 $$x$$를 $$x - a$$로 바꾸면 된다). $$x = 0$$에서는 첫 항 $$c_0$$만 남아 모든 멱급수가 수렴하므로 수렴역은 비어 있지 않다. 핵심 질문은 그 밖의 어디서 수렴하는가인데, 놀랍게도 수렴역은 언제나 원점을 중심으로 하는 구간이 된다.

<div class="proposition" markdown="1">

<ins id="thm2">**정리 2 (수렴반경)**</ins> 각 멱급수 $$\sum c_n x^n$$에 대하여 $$0 \leq R \leq \infty$$인 *수렴반경<sub>radius of convergence</sub>* $$R$$이 존재하여, $$\lvert x\rvert < R$$이면 절대수렴하고 $$\lvert x\rvert > R$$이면 발산한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

핵심은 다음의 비교 보조사실이다: 멱급수가 어떤 $$x_0 \neq 0$$에서 수렴하면, $$\lvert x\rvert < \lvert x_0\rvert$$인 모든 $$x$$에서 절대수렴한다. 실제로 $$\sum c_n x_0^n$$이 수렴하면 일반항이 $$0$$으로 가므로 유계여서 $$\lvert c_n x_0^n\rvert \leq M$$인 $$M$$이 있고, $$r = \lvert x/x_0\rvert < 1$$로 두면

$$\lvert c_n x^n\rvert = \lvert c_n x_0^n\rvert \cdot r^n \leq M r^n$$

이다. 우변은 공비 $$r < 1$$의 수렴하는 기하급수이므로, 비교판정 ([§무한급수, ⁋정리 4](/ko/math/calculus/series#thm4))에 의해 $$\sum c_n x^n$$이 절대수렴한다.

이제 $$R = \sup\{\,\lvert x\rvert : \sum c_n x^n \text{이 수렴}\,\}$$로 두자 (수렴하는 $$x$$가 무계이면 $$R = \infty$$). $$\lvert x\rvert < R$$이면 정의에 의해 $$\lvert x\rvert < \lvert x_0\rvert$$이면서 수렴하는 $$x_0$$이 있고, 위 보조사실로 $$x$$에서 절대수렴한다. $$\lvert x\rvert > R$$이면 상한의 정의상 발산한다.

</details>

수렴반경은 보통 비판정이나 근판정으로 계산한다. $$\left\lvert\dfrac{c_{n+1}}{c_n}\right\rvert \to L$$이면 항 $$c_n x^n$$의 비가 $$L\lvert x\rvert$$로 가므로 $$R = 1/L$$이고, 더 일반적으로는 *코시–아다마르 공식*

$$\frac{1}{R} = \limsup_{n\to\infty} \lvert c_n\rvert^{1/n}$$

이 항상 성립한다.

<div class="example" markdown="1">

<ins id="ex3">**예시 3 (수렴반경 계산)**</ins> 비판정으로 $$\dfrac{\lvert c_{n+1}\rvert}{\lvert c_n\rvert}$$의 극한을 보면:

$$\sum \frac{x^n}{n!}:\ \frac{n!}{(n+1)!} = \frac{1}{n+1} \to 0 \implies R = \infty,$$

$$\sum n!\,x^n:\ \frac{(n+1)!}{n!} = n+1 \to \infty \implies R = 0,$$

$$\sum \frac{x^n}{n^2}:\ \frac{n^2}{(n+1)^2} \to 1 \implies R = 1.$$

즉 첫 급수는 모든 $$x$$에서, 둘째는 $$x = 0$$에서만, 셋째는 $$\lvert x\rvert < 1$$에서 수렴한다.

</div>

수렴반경의 *경계* $$\lvert x\rvert = R$$에서의 거동은 정리 2가 말해 주지 않으며, 급수마다 따로 살펴야 한다. 세 급수 $$\sum x^n$$, $$\sum \dfrac{x^n}{n}$$, $$\sum \dfrac{x^n}{n^2}$$은 모두 $$R = 1$$이지만, $$x = 1$$에서 각각 발산(기하급수)·발산(조화급수)·수렴($$p=2$$)하고, $$x = -1$$에서 각각 발산·수렴(교대조화급수)·수렴한다. 경계의 미묘함은 멱급수 이론의 깊은 부분으로 이어진다.


## 초등함수의 전개

지수·삼각함수는 다음의 멱급수와 일치하며, 셋 다 수렴요경이 $$\infty$$이다.

<div class="example" markdown="1">

<ins id="ex4">**예시 4 (지수·삼각함수)**</ins> 

$$e^x = \sum_{n=0}^\infty \frac{x^n}{n!}, \qquad \sin x = \sum_{n=0}^\infty \frac{(-1)^n x^{2n+1}}{(2n+1)!}, \qquad \cos x = \sum_{n=0}^\infty \frac{(-1)^n x^{2n}}{(2n)!}.$$

오일러 공식 $$e^{ix} = \cos x + i\sin x$$은 이들 급수에서 형식적으로 따라 나온다.

</div>

전개가 유일함은 다음에서 따른다. 한 함수가 두 멱급수로 표현되면 두 급수의 계수가 모두 일치한다는 것이다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5 (계수의 유일성)**</ins> $$\lvert x\rvert < R$$에서 $$\sum c_n x^n = \sum d_n x^n$$이면 모든 $$n$$에 대해 $$c_n = d_n$$이다.

</div>


일반화된 이항정리로 임의의 실수 $$\alpha$$에 대해

$$(1+x)^\alpha = \sum_{n=0}^\infty \binom{\alpha}{n} x^n, \qquad \binom{\alpha}{n} = \frac{\alpha(\alpha-1)\cdots(\alpha-n+1)}{n!} \qquad (\lvert x\rvert < 1)$$

도 성립하며, $$\alpha$$가 음의 정수나 분수일 때 무한급수가 된다.

## 멱급수의 연산

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> $$f(x) = \sum a_n x^n$$, $$g(x) = \sum b_n x^n$$이 각각 수렴요경 $$R_f, R_g$$를 가지면, $$\lvert x\rvert < \min(R_f, R_g)$$에서

$$f(x) + g(x) = \sum_{n=0}^\infty (a_n + b_n)x^n, \qquad f(x)g(x) = \sum_{n=0}^\infty \left(\sum_{k=0}^n a_k b_{n-k}\right) x^n$$

이다. 곱의 계수는 두 계수열의 *코시 곱<sub>Cauchy product</sub>*이다.

</div>

코시 곱은 두 다항식을 곱해 같은 차수의 항을 모으는 것을 무한 차수로 확장한 것이다. 가령 $$\dfrac{1}{1-x} = \sum x^n$$을 자신과 곱하면 $$n$$차 계수가 $$\sum_{k=0}^n 1\cdot 1 = n+1$$이 되어 $$\dfrac{1}{(1-x)^2} = \sum (n+1)x^n$$을 얻는다.

## 해석함수

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> 함수 $$f$$가 점 $$a$$ 근방에서 그곳을 중심으로 하는 멱급수와 일치하면 $$f$$가 $$a$$에서 *해석적<sub>analytic</sub>*이라 한다. 정의역의 모든 점에서 해석적이면 $$f$$를 *해석함수*라 한다.

</div>

정의 7에 의해 해석함수는 자신의 테일러 급수와 일치한다. 그러나 그 역은 거짓이다. $$f(x) = e^{-1/x^2}$$ ($$f(0) = 0$$) 은 $$\mathbb{R}$$ 전체에서 매끄럽지만 $$0$$에서 모든 계도함수가 $$0$$이어서 그 테일러 급수가 항등적으로 $$0$$이고, 따라서 $$0$$의 어떤 근방에서도 $$f$$와 일치하지 않는다 — $$f$$는 $$0$$에서 해석적이지 않다. 즉 매끄러움이 해석성을 보장하지 못하는 것이며, 테일러 급수가 함수로 수렴하는지는 미분법을 배운 뒤 테일러 정리에서 나머지항을 통해 판정할 수 있다. 이 간극을 메우는 복소해석학에서는 (복소)미분가능성이 곧 해석성과 동치가 되어 사정이 극적으로 달라진다.



이렇게 멱급수는 함수를 무한 차수 다항식으로 다루게 해 주어, 미분방정식의 급수해·수치 근사·특수함수의 정의 등 응용이 광범위하다. 멱급수의 균등수렴과 해석함수의 엄밀한 이론은 해석학 [\[해석학\] §멱급수와 해석함수](/ko/math/analysis/power_series)에서 다룬다.
