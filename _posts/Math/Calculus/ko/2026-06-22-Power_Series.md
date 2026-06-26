---
title: "멱급수"
description: "변수의 거듭제곱으로 이루어진 멱급수와 수렴반경과 그 값을 다룬다. 초등함수의 멱급수 전개, 멱급수의 사칙연산, 해석함수의 정의를 살펴본다."
excerpt: "멱급수와 수렴반경, 초등함수의 전개, 해석함수"

categories: [Math / Calculus]
permalink: /ko/math/calculus/power_series
sidebar: 
    nav: "calculus-ko"

date: 2026-06-22
weight: 5
---

우리가 함수의 극한과 연속성을 정의한 직후, 수열의 극한과 무한급수를 먼저 정의한 이유는 크게 두 가지이다. 첫 번째 이유는 정적분에서 사용해야 하는 구분구적법을 위해서는 어차피 무한급수를 다루어야 하는데, 미분에서 적분으로 이어지는 흐름을 수열의 극한이 방해하지 않도록 하기 위해서이며, 두 번째 이유는 바로 이 글에서 멱급수를 우선 정의하기 위해서이다. 

멱급수는 함수를 적는 또 다른 방법으로, 이를 도입하면 고등학교에서 다룰 수 없었던 함수들을 더 쉽게 다룰 수 있다. 가령 고등학교에서 지수함수 $$2^x$$를 정의할 때 우리는 무리수에서의 함숫값을 엄밀하게 정의하지 않았는데, 그렇게 정의하려면 앞서 [§연속함수, ⁋정리 5](/ko/math/calculus/continuity#thm5)나 [§수열의 극한, ⁋명제 7](/ko/math/calculus/sequences#prop7)에서 쓴 실수의 완비성이 필요하다. 또 지수함수를 정의한 뒤 [§수열의 극한, ⁋예시 8](/ko/math/calculus/sequences#ex8)의 자연상수를 정의할 때에도 <em-ko>미분해도 자기 자신이 나오는 지수함수</em-ko>처럼 다소 불명확한 방식을 택해야 했다. 반면 멱급수로 지수함수 $$e^x$$를 정의하면 이런 복잡함이 없고, $$e^{-x^2}$$의 적분처럼 초등함수로 나타나지 않는 함수도 깔끔하게 표현할 수 있다. 

## 멱급수와 수렴반경

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 중심 $$a$$에서의 *멱급수<sub>power series</sub>*는 수열 $$(c_n)_{n\geq 0}$$에 대해

$$\sum_{n=0}^{\infty} c_n (x - a)^n = c_0 + c_1(x-a) + c_2(x-a)^2 + \cdots$$

꼴의 급수이다. 이 급수가 수렴하는 $$x$$들의 모임을 *domain of convergence<sub>수렴역</sub>*이라 하고, 그 위에서 급수의 합은 $$x$$의 함수를 정의한다.

</div>

논의를 간단히 하기 위해 이후 $$a = 0$$인 경우, 즉 $$\sum c_n x^n$$을 주로 다루며, 일반적인 경우는 $$x$$를 $$x - a$$로 바꾸면 되므로 이는 일반성을 크게 잃어버리는 가정이 아니다. 

정의로부터, $$x = 0$$에서는 첫 항 $$c_0$$만 남으므로 domain of convergence는 적어도 공집합이 아니다. 뿐만 아니라, 만일 멱급수가 어떤 $$x_0 \neq 0$$에서 수렴하면, 이 멱급수는 $$\lvert x\rvert < \lvert x_0\rvert$$인 모든 $$x$$에서 절대수렴한다는 것을 알 수 있다. 이는 만일 $$\sum c_n x_0^n$$이 수렴하면 일반항이 $$0$$으로 가므로, $$\lvert c_n x_0^n\rvert \leq M$$인 $$M$$이 있고, $$r = \lvert x/x_0\rvert < 1$$로 두면

$$\lvert c_n x^n\rvert = \lvert c_n x_0^n\rvert \cdot r^n \leq M r^n$$

이며 우변은 공비 $$r < 1$$의 수렴하는 기하급수이므로 [§무한급수, ⁋정리 6](/ko/math/calculus/series#thm6)을 적용할 수 있기 때문이다. 이제 수렴하는 $$x$$들의 절댓값의 상한을 $$R$$ (그런 $$x$$가 무계이면 $$R=\infty$$)이라 두자. $$\lvert x\rvert<R$$이면 $$\lvert x\rvert<\lvert x_0\rvert$$이면서 수렴하는 $$x_0$$이 존재하여 앞서 보인 사실로 절대수렴하고, $$\lvert x\rvert>R$$이면 상한의 정의상 발산하므로, 다음의 정리를 얻는다. 

<div class="proposition" markdown="1">

<ins id="thm2">**정리 2 (수렴반경)**</ins> 각 멱급수 $$\sum c_n x^n$$에 대하여 $$0 \leq R \leq \infty$$인 *수렴반경<sub>radius of convergence</sub>* $$R$$이 존재하여, $$\lvert x\rvert < R$$이면 절대수렴하고 $$\lvert x\rvert > R$$이면 발산한다.

</div>

여기서 $$R=0$$인 경우는 주어진 멱급수가 $$x=0$$에서만 수렴하는 경우로 해석되며 (따라서 우리의 관심사가 아니다), 반대쪽 극한인 $$R=\infty$$의 경우는 주어진 멱급수가 실수 전체에서 수렴하는 경우로 해석된다. 이 두 경우를 제외하면, 수렴반경은 $$\lvert x\rvert=R$$인 경우에 대한 수렴여부는 결정해주지 않으며 실제로 멱급수에 따라 모든 조합이 가능하다.

그 모양으로 인해, 멱급수의 수렴반경은 보통 비판정이나 [§무한급수, ⁋명제 8](/ko/math/calculus/series#prop8)으로 계산한다. 가령 비판정법을 적용하여 $$\left\lvert c_{n+1}/c_n\right\rvert \to L$$이면 인접한 항의 비가 $$L\lvert x\rvert$$로 가므로 $$R = 1/L$$으로 두면 된다는 것을 알고, 더 일반적으로는 

$$\frac{1}{R} = \limsup_{n\to\infty} \lvert c_n\rvert^{1/n}$$

이 항상 성립한다. 가령 $$\sum_n x^n/n!$$에 비판정을 적용하면 인접한 항의 비가 $$\lvert x\rvert/(n+1) \to 0$$이므로 $$R = \infty$$, 곧 이 멱급수는 실수 전체에서 수렴한다.

## 초등함수의 전개

멱급수를 일찍 도입하여 얻는 이득 중 하나는 지수함수를 더 확실한 방법으로 정의할 수 있다는 것이다. 

<div class="example" markdown="1">

<ins id="ex3">**예시 3 (지수함수)**</ins> 앞서 본 실수 전체에서 수렴하는 멱급수를

$$e^x = \sum_{n=0}^\infty \frac{x^n}{n!}$$

으로 나타낸다. 특히 $$x = 1$$을 넣으면 $$e = \sum 1/n!$$인데, 이 수는 [§수열의 극한, ⁋예시 8](/ko/math/calculus/sequences#ex8)에서 극한 $$\lim(1 + 1/n)^n$$으로 정의했던 자연상수와 일치한다. 

이에 대한 증명은 다음과 같다. 해당 극한의 극한값을 $$L = \lim(1+1/n)^n$$, 급수의 부분합을 $$s_m = \sum 1/k!$$이라 두면, 위의 [§수열의 극한, ⁋예시 8](/ko/math/calculus/sequences#ex8)에서 이미 이항정리로

$$\left(1 + \frac1n\right)^n = \sum_{k=0}^n \binom{n}{k}\frac{1}{n^k} = \sum_{k=0}^n \frac{1}{k!}\prod_{j=0}^{k-1}\left(1 - \frac{j}{n}\right)$$

임을 보였고, 또 이 수열이 증가하여 그 극한 $$L$$이 항들의 상한임을 보였다.

먼저 각 곱의 인수 $$1 - j/n$$이 $$1$$ 이하이므로 위 합은 $$\sum_{k=0}^n 1/k! = s_n$$ 이하이고, 부분합은 다시 그 극한 $$s = \sum_{n=0}^\infty 1/n!$$ 이하이므로, 모든 $$n$$에서 $$(1 + 1/n)^n \leq s$$이다. $$L$$이 항들의 상한이고 $$s$$가 그 상계이므로 $$L \leq s$$를 얻는다. 반대로 $$m$$을 고정하고 $$n \geq m$$인 $$n$$만 보면, 위 합에서 음이 아닌 뒤쪽 항들을 버려

$$\left(1 + \frac1n\right)^n \geq \sum_{k=0}^m \frac{1}{k!}\prod_{j=0}^{k-1}\left(1 - \frac{j}{n}\right)$$

을 얻는다. 좌변은 $$L$$ 이하이므로 우변 또한 $$L$$ 이하이고, $$m$$을 고정한 채 $$n \to \infty$$를 보내면 우변은 유한합이고 각 인수가 $$1 - j/n \to 1$$이므로 [§함수의 극한, ⁋명제 5](/ko/math/calculus/functions_and_limits#prop5) ([§수열의 극한, ⁋명제 2](/ko/math/calculus/sequences#prop2))에 의해 $$s_m$$으로 수렴한다. 수렴하는 수열의 모든 항이 $$L$$ 이하이면 그 극한도 $$L$$ 이하이므로 $$s_m \leq L$$이고, 다시 $$m \to \infty$$를 보내면 $$s \leq L$$이다. 두 부등식을 합쳐 $$L = s$$, 즉 두 글에서 정의한 $$e$$는 같은 수이다.

</div>

## 멱급수의 연산

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> $$f(x) = \sum a_n x^n$$, $$g(x) = \sum b_n x^n$$이 각각 수렴반경 $$R_f, R_g$$를 가지면, $$\lvert x\rvert < \min(R_f, R_g)$$에서

$$f(x) + g(x) = \sum_{n=0}^\infty (a_n + b_n)x^n, \qquad f(x)g(x) = \sum_{n=0}^\infty \left(\sum_{k=0}^n a_k b_{n-k}\right) x^n$$

이다. 곱의 계수는 두 계수열의 *코시 곱<sub>Cauchy product</sub>*이다.

</div>

코시 곱은 두 다항식을 곱해 같은 차수의 항을 모으는 것을 무한 차수로 확장한 것이다. 가령 $$1/(1-x) = \sum_n x^n$$을 자신과 곱하면 $$n$$차 계수가 $$\sum_{k=0}^n 1\cdot 1 = n+1$$이 되어 $$1/(1-x)^2 = \sum_n (n+1)x^n$$을 얻는다.

## 해석함수

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> 함수 $$f$$가 점 $$a$$ 근방에서 그곳을 중심으로 하는 멱급수와 일치하면 $$f$$가 $$a$$에서 *해석적<sub>analytic</sub>*이라 한다. 정의역의 모든 점에서 해석적이면 $$f$$를 *해석함수*라 한다.

</div>

[정의 5](#def5)에 의해 해석함수는 자신의 테일러 급수와 일치한다. 그러나 그 역은 거짓이다. $$f(x) = e^{-1/x^2}$$ ($$f(0) = 0$$) 은 $$\mathbb{R}$$ 전체에서 매끄럽지만 $$0$$에서 모든 계도함수가 $$0$$이어서 그 테일러 급수가 항등적으로 $$0$$이고, 따라서 $$0$$의 어떤 근방에서도 $$f$$와 일치하지 않아 $$f$$는 $$0$$에서 해석적이지 않다. 즉 매끄러움이 해석성을 보장하지 못하는 것이며, 테일러 급수가 함수로 수렴하는지는 미분법을 배운 뒤 테일러 정리에서 나머지항을 통해 판정할 수 있다. 
