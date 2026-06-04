---
title: "멱급수"
description: "변수의 거듭제곱으로 이루어진 멱급수와 수렴반경을 다루고, 수렴반경 안에서 항별 미분·적분이 가능함을 이용해 초등함수의 멱급수 전개를 얻는다. 계수의 유일성, 멱급수의 사칙연산, 해석함수와 매끄러움의 차이를 논한다."
excerpt: "멱급수와 수렴반경, 항별 미분·적분, 초등함수의 전개, 해석함수"

categories: [Math / Calculus]
permalink: /ko/math/calculus/power_series
sidebar: 
    nav: "calculus-ko"

date: 2026-06-02
last_modified_at: 2026-06-02
weight: 15

published: false
---

[§무한급수](/ko/math/calculus/series)의 각 항을 변수 $$x$$의 거듭제곱으로 두면, 수 대신 함수를 정의하는 급수가 된다. 멱급수는 다항식을 무한 차수로 확장한 것으로, [§테일러 정리](/ko/math/calculus/taylor_theorem)에서 본 함수의 다항식 근사를 극한까지 밀고 간 형태이다. 미적분학에서 등장하는 거의 모든 초등함수가 멱급수로 표현되며, 그 덕분에 미분·적분이 단순한 지수 조작으로 환원되고, 초등함수로 풀리지 않는 미분방정식조차 급수해로 다룰 수 있게 된다.

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

## 항별 미분과 적분

멱급수가 정의하는 함수는 수렴반경 안에서 마치 (무한 차수) 다항식처럼 항별로 미분하고 적분할 수 있다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> $$f(x) = \sum_{n=0}^\infty c_n x^n$$이 수렴반경 $$R > 0$$을 가지면, $$f$$는 $$\lvert x\rvert < R$$에서 미분가능하며

$$f'(x) = \sum_{n=1}^\infty n\,c_n x^{n-1}, \qquad \int_0^x f(t)\,dt = \sum_{n=0}^\infty \frac{c_n}{n+1} x^{n+1}$$

이고, 두 급수의 수렴반경도 $$R$$이다.

</div>

수렴반경이 보존됨은 $$\lim_n n^{1/n} = 1$$이라 $$\limsup\lvert n c_n\rvert^{1/n} = \limsup\lvert c_n\rvert^{1/n}$$임에서 따른다. 항별 미분이 정당함의 엄밀한 근거는 멱급수가 수렴반경 안의 컴팩트 부분에서 *균등수렴*한다는 데 있으며, 그 증명은 해석학 [\[해석학\] §멱급수와 해석함수](/ko/math/analysis/power_series)에서 다룬다. 명제 4는 알려진 멱급수에서 새로운 멱급수를 끌어내는 강력한 도구이다.

<div class="example" markdown="1">

<ins id="ex5">**예시 5 (로그와 역탄젠트)**</ins> 기하급수 $$\dfrac{1}{1 - x} = \sum_{n=0}^\infty x^n$$ ($$\lvert x\rvert < 1$$) 을 항별 적분하면

$$-\ln(1 - x) = \sum_{n=1}^\infty \frac{x^n}{n} \quad\Longrightarrow\quad \ln(1+x) = \sum_{n=1}^\infty \frac{(-1)^{n-1}}{n} x^n$$

을 얻고, $$\dfrac{1}{1 + x^2} = \sum_{n=0}^\infty (-1)^n x^{2n}$$을 항별 적분하면

$$\arctan x = \sum_{n=0}^\infty \frac{(-1)^n}{2n+1} x^{2n+1}$$

을 얻는다.

</div>

<div class="example" markdown="1">

<ins id="ex6">**예시 6**</ins> 항별 미분은 합을 계산하는 데에도 쓰인다. $$\dfrac{1}{1-x} = \sum x^n$$을 미분하면 $$\dfrac{1}{(1-x)^2} = \sum_{n=1}^\infty n x^{n-1}$$이고, 양변에 $$x$$를 곱하면

$$\sum_{n=1}^\infty n x^n = \frac{x}{(1-x)^2} \qquad (\lvert x\rvert < 1)$$

이다. 가령 $$x = \tfrac12$$을 넣으면 $$\sum_{n\geq 1} n/2^n = 2$$를 얻는다.

</div>

## 초등함수의 전개

[§테일러 정리](/ko/math/calculus/taylor_theorem)에서 보듯 지수·삼각함수는 다음의 멱급수와 일치하며, 셋 다 수렴반경이 $$\infty$$이다.

<div class="example" markdown="1">

<ins id="ex7">**예시 7 (지수·삼각함수)**</ins> 

$$e^x = \sum_{n=0}^\infty \frac{x^n}{n!}, \qquad \sin x = \sum_{n=0}^\infty \frac{(-1)^n x^{2n+1}}{(2n+1)!}, \qquad \cos x = \sum_{n=0}^\infty \frac{(-1)^n x^{2n}}{(2n)!}.$$

이 전개를 항별 미분하면 $$(e^x)' = e^x$$, $$(\sin x)' = \cos x$$ 같은 익숙한 공식이 급수 차원에서 즉시 확인된다. 또 $$\sin, \cos$$의 급수에서 $$e^{ix} = \cos x + i\sin x$$라는 오일러 공식이 형식적으로 따라 나온다.

</div>

전개가 유일함은 다음에서 따른다. 한 함수가 두 멱급수로 표현되면 두 급수의 계수가 모두 일치한다는 것이다.

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8 (계수의 유일성)**</ins> $$\lvert x\rvert < R$$에서 $$\sum c_n x^n = \sum d_n x^n$$이면 모든 $$n$$에 대해 $$c_n = d_n$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$f(x) = \sum c_n x^n$$로 두면 명제 4에 의해 $$f$$는 무한히 미분가능하고, 항별 미분을 $$k$$번 한 뒤 $$x = 0$$을 대입하면 첫 항 외에는 모두 사라져 $$f^{(k)}(0) = k!\,c_k$$가 된다. 따라서 $$c_k = f^{(k)}(0)/k!$$로 $$f$$에 의해 유일하게 결정되며, 같은 논리로 $$d_k = f^{(k)}(0)/k!$$이므로 $$c_k = d_k$$이다.

</details>

특히 $$c_n = f^{(n)}(0)/n!$$이므로, 멱급수로 표현되는 함수는 자신의 테일러 급수와 일치한다. 일반화된 이항정리로 임의의 실수 $$\alpha$$에 대해

$$(1+x)^\alpha = \sum_{n=0}^\infty \binom{\alpha}{n} x^n, \qquad \binom{\alpha}{n} = \frac{\alpha(\alpha-1)\cdots(\alpha-n+1)}{n!} \qquad (\lvert x\rvert < 1)$$

도 성립하며, $$\alpha$$가 음의 정수나 분수일 때 무한급수가 된다.

## 멱급수의 연산

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> $$f(x) = \sum a_n x^n$$, $$g(x) = \sum b_n x^n$$이 각각 수렴반경 $$R_f, R_g$$를 가지면, $$\lvert x\rvert < \min(R_f, R_g)$$에서

$$f(x) + g(x) = \sum_{n=0}^\infty (a_n + b_n)x^n, \qquad f(x)g(x) = \sum_{n=0}^\infty \left(\sum_{k=0}^n a_k b_{n-k}\right) x^n$$

이다. 곱의 계수는 두 계수열의 *코시 곱<sub>Cauchy product</sub>*이다.

</div>

코시 곱은 두 다항식을 곱해 같은 차수의 항을 모으는 것을 무한 차수로 확장한 것이다. 가령 $$\dfrac{1}{1-x} = \sum x^n$$을 자신과 곱하면, $$n$$차 계수가 $$\sum_{k=0}^n 1\cdot 1 = n+1$$이 되어 $$\dfrac{1}{(1-x)^2} = \sum (n+1)x^n$$을 얻는데, 이는 예시 6의 결과와 일치한다.

## 해석함수

<div class="definition" markdown="1">

<ins id="def10">**정의 10**</ins> 함수 $$f$$가 점 $$a$$ 근방에서 그곳을 중심으로 하는 멱급수와 일치하면 $$f$$가 $$a$$에서 *해석적<sub>analytic</sub>*이라 한다. 정의역의 모든 점에서 해석적이면 $$f$$를 *해석함수*라 한다.

</div>

명제 4와 8에 의해 해석함수는 무한히 미분가능하고 자신의 테일러 급수와 일치한다. 그러나 그 역은 거짓이다. $$f(x) = e^{-1/x^2}$$ ($$f(0) = 0$$) 은 $$\mathbb{R}$$ 전체에서 매끄럽지만 $$0$$에서 모든 계도함수가 $$0$$이어서 그 테일러 급수가 항등적으로 $$0$$이고, 따라서 $$0$$의 어떤 근방에서도 $$f$$와 일치하지 않는다 — $$f$$는 $$0$$에서 해석적이지 않다. 즉 매끄러움은 해석성보다 약하며, 테일러 급수가 함수로 수렴하는지는 [§테일러 정리](/ko/math/calculus/taylor_theorem)의 나머지항이 $$0$$으로 가는지에 달려 있다. 이 간극을 메우는 복소해석학에서는 (복소)미분가능성이 곧 해석성과 동치가 되어 사정이 극적으로 달라진다.

수렴반경의 경계에서 멱급수가 수렴하는 경우, 그 값은 안쪽에서의 극한과 이어진다는 아벨의 정리가 성립한다. 이를 예시 5의 $$\arctan x = \sum \frac{(-1)^n}{2n+1}x^{2n+1}$$에 적용하면, $$x = 1$$에서 우변이 교대급수로 수렴하므로 $$\dfrac{\pi}{4} = \arctan 1 = 1 - \dfrac13 + \dfrac15 - \dfrac17 + \cdots$$라는 라이프니츠 급수를 얻고, $$\ln(1+x)$$에 $$x = 1$$을 넣으면 $$\ln 2 = 1 - \tfrac12 + \tfrac13 - \cdots$$이다.

## 응용: 멱급수해

멱급수의 위력은 미분방정식을 푸는 데서 잘 드러난다. 해를 미지의 계수를 가진 멱급수로 놓고 항별 미분한 뒤 점화식을 세우면, 초등함수로 닫혀 있지 않은 방정식도 계수를 차례로 결정해 풀 수 있다.

<div class="example" markdown="1">

<ins id="ex11">**예시 11 (멱급수해)**</ins> $$y' = y$$, $$y(0) = 1$$을 풀자. $$y = \sum_{n=0}^\infty c_n x^n$$으로 놓으면 $$y(0) = c_0 = 1$$이고, 항별 미분으로

$$y' = \sum_{n=1}^\infty n c_n x^{n-1} = \sum_{n=0}^\infty (n+1)c_{n+1} x^n$$

이다. $$y' = y$$의 양변에서 계수의 유일성 (명제 8) 으로 $$(n+1)c_{n+1} = c_n$$, 곧 $$c_{n+1} = \dfrac{c_n}{n+1}$$이 강제된다. $$c_0 = 1$$에서 시작하면 $$c_n = \dfrac{1}{n!}$$이므로 $$y = \sum_{n=0}^\infty \dfrac{x^n}{n!} = e^x$$이다. 알려진 해 $$e^x$$를 급수해의 형태로 복원한 것이며, 같은 방법이 베셀 방정식처럼 초등함수로 풀리지 않는 경우에 특수함수를 정의해 준다.

</div>

알려진 전개에 특정 값을 대입하면 수치급수의 합도 얻는다. $$-\ln(1-x) = \sum_{n\geq 1} x^n/n$$에 $$x = \tfrac12$$을 넣으면

$$\sum_{n=1}^\infty \frac{1}{n\,2^n} = -\ln\Bigl(1 - \tfrac12\Bigr) = \ln 2$$

이고, $$e^x = \sum x^n/n!$$에 $$x = -1$$을 넣으면 $$\sum_{n=0}^\infty \dfrac{(-1)^n}{n!} = e^{-1}$$이다. 이렇게 함수의 전개 하나가 무수한 수치급수의 합을 한꺼번에 결정한다.

이렇게 멱급수는 함수를 무한 차수 다항식으로 다루게 해 주어, 미분방정식의 급수해·수치 근사·특수함수의 정의 등 응용이 광범위하다. 지금까지의 미적분이 한 변수에 관한 것이었다면, 다음 글 [§다변수함수와 편미분](/ko/math/calculus/partial_derivatives)에서는 여러 변수의 함수로 넘어간다. 멱급수의 균등수렴과 해석함수의 엄밀한 이론은 해석학 [\[해석학\] §멱급수와 해석함수](/ko/math/analysis/power_series)에서 다룬다.
