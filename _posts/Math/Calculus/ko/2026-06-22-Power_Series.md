---
title: "멱급수"
description: "변수의 거듭제곱으로 이루어진 멱급수와 수렴반경과 그 값을 다룬다. 초등함수의 멱급수 전개, 계수의 유일성, 멱급수의 사칙연산, 해석함수의 정의를 살펴본다."
excerpt: "멱급수와 수렴반경, 초등함수의 전개, 해석함수"

categories: [Math / Calculus]
permalink: /ko/math/calculus/power_series
sidebar: 
    nav: "calculus-ko"

date: 2026-06-22
weight: 5

published: false
---

우리가 함수의 극한과 연속성을 정의한 직후, 수열의 극한과 무한급수를 먼저 정의한 이유는 크게 두 가지이다. 첫 번째 이유는 정적분에서 사용해야 하는 구분구적법을 위해서는 어차피 무한급수를 다루어야 하는데, 미분에서 적분으로 이어지는 흐름을 수열의 극한이 방해하지 않도록 하기 위해서이며, 두 번째 이유는 바로 이 글에서 멱급수를 우선 정의하기 위해서이다. 

멱급수는 기본적으로 함수를 적는 또 다른 방법으로, 이것이 중요한 이유는 이를 도입함으로써 우리가 고등학교 때 다룰 수 없었던 함수들을 더욱 쉽게 다룰 수 있다는 점에 있다. 가령, 우리는 고등학교에서 지수함수 $$2^x$$를 정의할 때, 무리수에서의 함숫값 등을 엄밀한 방식으로 정의하지는 않았으며, 실은 그와 같은 방식으로 함숫값을 정의하기 위해서는 앞서 [§연속함수, ⁋정리 5](/ko/math/calculus/continuity#thm5)나 [§수열의 극한, ⁋명제 8](/ko/math/calculus/sequences#prop8)에서 필요했던 실수의 성질, 즉 완비성이 필요하다. 뿐만 아니라, 지수함수를 정의한 후 [§수열의 극한, ⁋예시 9](/ko/math/calculus/sequences#ex9)의 자연상수를 정의할 때에도 우리는 <em-ko>미분해도 자기 자신이 나오는 지수함수</em-ko>등으로, 다소 불명확한 방식을 택했어야 한다. 반면, 멱급수로 지수함수 $$e^x$$를 정의하는 것에는 이와 같은 복잡함이 필요하지 않으며, 뿐만 아니라 $$e^{-x^2}$$의 적분과 같이 초등함수로 나타나지 않는 함수도 멱급수로는 깔끔하게 표현할 수 있다. 

## 멱급수와 수렴반경

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 중심 $$a$$에서의 *멱급수<sub>power series</sub>*는 수열 $$(c_n)_{n\geq 0}$$에 대해

$$\sum_{n=0}^{\infty} c_n (x - a)^n = c_0 + c_1(x-a) + c_2(x-a)^2 + \cdots$$

꼴의 급수이다. 이 급수가 수렴하는 $$x$$들의 모임을 *domain of convergence<sub>수렴역</sub>*이라 하고, 그 위에서 급수의 합은 $$x$$의 함수를 정의한다.

</div>

논의를 간단히 하기 위해 이후 $$a = 0$$인 경우, 즉 $$\sum c_n x^n$$을 주로 다루며, 일반적인 경우는 $$x$$를 $$x - a$$로 바꾸면 되므로 이는 일반성을 크게 잃어버리는 가정이 아니다. 

정의로부터, $$x = 0$$에서는 첫 항 $$c_0$$만 남으므로 domain of convergence는 적어도 공집합이 아니다. 뿐만 아니라, 만일 멱급수가 어떤 $$x_0 \neq 0$$에서 수렴하면, 이 멱급수는 $$\lvert x\rvert < \lvert x_0\rvert$$인 모든 $$x$$에서 절대수렴한다는 것을 알 수 있다. 이는 만일 $$\sum c_n x_0^n$$이 수렴하면 일반항이 $$0$$으로 가므로, $$\lvert c_n x_0^n\rvert \leq M$$인 $$M$$이 있고, $$r = \lvert x/x_0\rvert < 1$$로 두면

$$\lvert c_n x^n\rvert = \lvert c_n x_0^n\rvert \cdot r^n \leq M r^n$$

이며 우변은 공비 $$r < 1$$의 수렴하는 기하급수이므로 [§무한급수, ⁋정리 6](/ko/math/calculus/series#thm6)을 적용할 수 있기 때문이다. 이로부터 다음의 정리를 얻는다. 

<div class="proposition" markdown="1">

<ins id="thm2">**정리 2 (수렴반경)**</ins> 각 멱급수 $$\sum c_n x^n$$에 대하여 $$0 \leq R \leq \infty$$인 *수렴반경<sub>radius of convergence</sub>* $$R$$이 존재하여, $$\lvert x\rvert < R$$이면 절대수렴하고 $$\lvert x\rvert > R$$이면 발산한다.

</div>

여기서 $$R=0$$인 경우는 주어진 멱급수가 $$x=0$$에서만 수렴하는 경우로 해석되며 (따라서 우리의 관심사가 아니다), 반대쪽 극한인 $$R=\ingty$$의 경우는 주어진 멱급수가 실수 전체에서 수렴하는 경우로 해석된다. 이 두 경우를 제외하면, 수렴반경은 $$\lvert x\rvert=R$$인 경우에 대한 수렴여부는 결정해주지 않으며 실제로 멱급수에 따라 모든 조합이 가능하다.

그 모양으로 인해, 멱급수의 수렴반경은 보통 비판정이나 근판정으로 계산한다. 가령 비판정법을 적용하여 $$\left\lvert c_{n+1}/c_n\right\rvert \to L$$이면 인접한 항의 비가 $$L\lvert x\rvert$$로 가므로 $$R = 1/L$$으로 두면 된다는 것을 알고, 더 일반적으로는 

$$\frac{1}{R} = \limsup_{n\to\infty} \lvert c_n\rvert^{1/n}$$

이 항상 성립한다.

<div class="example" markdown="1">

<ins id="ex3">**예시 3 (수렴반경 계산)**</ins> 가령, 

$$\sum \frac{x^n}{n!}:\ \frac{n!}{(n+1)!} = \frac{1}{n+1} \to 0 \implies R = \infty$$

이므로 이 급수는 실수 전체에서 수렴한다. 

</div>

## 초등함수의 전개

위에서 언급하였듯, 멱급수를 일찍 도입하여 얻는 이득 중 하나는 지수함수를 더 확실한 방법으로 정의할 수 있다는 것이다. 

<div class="example" markdown="1">

<ins id="ex4">**예시 4 (지수함수)**</ins> 앞서 살펴본 [예시 3](#ex3)의 멱급수를

$$e^x = \sum_{n=0}^\infty \frac{x^n}{n!}$$

으로 나타낸다. 

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

<ins id="prop6">**명제 6**</ins> $$f(x) = \sum a_n x^n$$, $$g(x) = \sum b_n x^n$$이 각각 수렴반경 $$R_f, R_g$$를 가지면, $$\lvert x\rvert < \min(R_f, R_g)$$에서

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
