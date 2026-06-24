---
title: "테일러 정리"
description: "함수를 다항식으로 근사하는 테일러 다항식을 정의하고, 라그랑주 나머지를 가진 테일러 정리를 코시 평균값 정리로 증명한다. 초등함수의 매클로린 전개, 나머지의 평가, 극한·근사 계산에의 응용을 다룬다."
excerpt: "테일러 다항식, 라그랑주 나머지, 매클로린 전개, 근사와 극한"

categories: [Math / Calculus]
permalink: /ko/math/calculus/taylor_theorem
sidebar: 
    nav: "calculus-ko"

date: 2026-06-25
weight: 9

---

[§미분과 도함수](/ko/math/calculus/derivatives)에서 우리는 함수를 한번 미분하여 얻어진 미분계수가 함수의 접선 

$$f(x) \approx f(a) + f'(a)(x-a)$$

을 주는 것을 확인하였다. 관점을 바꿔서 보면 이것은 주어진 함수를 1차식으로 근사하는 것으로, 미분을 여러 차례 적용하면 이를 더 정교한 근사로 바꿀 수 있다.

## 테일러 다항식

함수 $$f$$가 점 $$a$$에서 $$n$$번 미분가능하면, $$a$$에서 함숫값과 처음 $$n$$개의 도함수 값을 $$f$$와 똑같이 갖는 차수 $$n$$의 다항식을 만들 수 있다. 

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> $$f$$가 점 $$a$$에서 $$n$$번 미분가능할 때, $$f$$의 $$a$$에서의 *$$n$$차 테일러 다항식<sub>Taylor polynomial</sub>*은

$$P_n(x) = \sum_{k=0}^{n} \frac{f^{(k)}(a)}{k!}(x - a)^k = f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2 + \cdots + \frac{f^{(n)}(a)}{n!}(x-a)^n$$

이다. 중심이 $$a = 0$$인 경우를 특히 *매클로린 다항식<sub>Maclaurin polynomial</sub>*이라 한다.

</div>

실질적으로 사용할 때에는 어차피 모든 함수를 원점으로 옮겨놓고 계산한 후 원래대로 평행이동 시키면 되므로, $$a=0$$인 경우를 정의로 취급해도 큰 문제는 없다. 

## 테일러 정리

위에서 주장한 것과 같이, 테일러 전개는 주어진 함수를, $$n$$차다항식으로 근사하는 방식이다. 다음 그래프를 보자. 

![sin 함수와 그 테일러 다항식 근사](/assets/images/Math/Calculus/Taylor_Theorem-1.svg){:style="width:23.68em" class="invert" .align-center}

이 그래프는 sin함수의 처음 몇 개의 테일러 전개를 그린 것으로, 위의 그림을 보면 실제로 이 근사가 점점 $$\sin$$ 함수에 가까워지는 것을 확인할 수 있다. 그러나 이것이 실제로 오차를 줄여나간다는 것을 수학적으로 증명하기 위해서는 다음 정리가 필요하다. 

<div class="proposition" markdown="1">

<ins id="thm2">**정리 2 (테일러 정리, 라그랑주 나머지)**</ins> $$f$$가 $$a$$와 $$x$$를 포함하는 구간에서 $$n+1$$번 미분가능하면, $$a$$와 $$x$$ 사이의 어떤 $$c$$에 대하여

$$f(x) = \sum_{k=0}^{n} \frac{f^{(k)}(a)}{k!}(x-a)^k + R_n(x), \qquad R_n(x) = \frac{f^{(n+1)}(c)}{(n+1)!}(x - a)^{n+1}$$

이 성립한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$x \neq a$$를 고정하고, $$a$$와 $$x$$ 사이의 변수 $$t$$에 대해 두 보조함수

$$g(t) = f(x) - \sum_{k=0}^{n}\frac{f^{(k)}(t)}{k!}(x-t)^k, \qquad h(t) = (x - t)^{n+1}$$

을 둔다. 끝값은 $$g(x) = 0$$, $$g(a) = f(x) - P_n(x) = R_n(x)$$이고 $$h(x) = 0$$, $$h(a) = (x-a)^{n+1}$$이다. $$g$$를 미분하면 인접한 항들이 서로 상쇄되어

$$g'(t) = -\frac{f^{(n+1)}(t)}{n!}(x - t)^n$$

만 남고, $$h'(t) = -(n+1)(x-t)^n$$이다. [§평균값 정리, ⁋정리 6](/ko/math/calculus/mean_value_theorem#thm6)를 $$a$$와 $$x$$ 사이에 적용하면

$$\bigl(g(x) - g(a)\bigr)h'(c) = \bigl(h(x) - h(a)\bigr)g'(c)$$

인 $$c$$가 존재한다. 값을 대입하면

$$(-R_n(x))\bigl(-(n+1)(x-c)^n\bigr) = \bigl(-(x-a)^{n+1}\bigr)\left(-\frac{f^{(n+1)}(c)}{n!}(x-c)^n\right)$$

이고, 양변의 $$(x-c)^n$$을 소거하여 정리하면 $$R_n(x) = f^{(n+1)}(c)(x-a)^{n+1}/(n+1)!$$을 얻는다.

</details>

따라서, 이제 위 정리의 나머지항을 계산하여 $$n \to \infty$$에서 $$R_n(x) \to 0$$임을 보이면, 함수가 무한급수와 일치한다는 것을 안다. 이렇게 얻어지는 무한급수를 $$f$$의 *테일러 급수* (중심이 $$0$$이면 매클로린 급수) 라 한다.

실제 몇몇 예시에서 이들 계산을 따라가보자.

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> $$f(x) = e^x$$의 임의의 미분은 자기 자신인 것을 확인하였으므로, 임의의 $$k$$에 대하여 $$f^{(k)}(0) = 1$$이다. 따라서 테일러 다항식은

$$P_n(x) = \sum_{k=0}^n \frac{x^k}{k!}$$

이다. 나머지는 $$0$$과 $$x$$ 사이의 어떤 $$c$$에 대해 

$$R_n(x) = \frac{e^c x^{n+1}}{(n+1)!}$$

으로 주어지고, 고정된 $$x$$에서

$$\lvert R_n(x)\rvert \leq \frac{e^{\lvert x\rvert}\lvert x\rvert^{n+1}}{(n+1)!} \to 0 \qquad (n \to \infty)$$

이므로 ([§수열의 극한, ⁋예시 6](/ko/math/calculus/sequences#ex6)) 모든 실수 $$x$$에서

$$e^x = \sum_{k=0}^{\infty}\frac{x^k}{k!}$$

이 성립한다. 특히 $$x = 1$$이면 $$e = \sum_{k=0}^\infty 1/k!$$이다.

</div>

비슷하게, 우리가 알고 있는 삼각함수에서도 다음이 성립한다. 

<div class="example" markdown="1">

<ins id="ex4">**예시 4 (삼각함수)**</ins> $$\sin x$$는 도함수가 $$\cos x, -\sin x, -\cos x, \sin x$$로 주기적이므로, $$f^{(k)}(0)$$이 $$0, 1, 0, -1$$을 반복한다. 모든 미분이 $$\lvert f^{(n+1)}\rvert \leq 1$$로 유계이므로, 위의 [예시 3](#ex3)과 같은 논법으로 나머지가 $$0$$으로 간다는 것을 보일 수 있고, 따라서 모든 $$x$$에서

$$\sin x = \sum_{k=0}^\infty \frac{(-1)^k x^{2k+1}}{(2k+1)!}, \qquad \cos x = \sum_{k=0}^\infty \frac{(-1)^k x^{2k}}{(2k)!}$$

이다.

</div>

다음은 수렴반경이 무한대가 아닌 예시이다.

<div class="example" markdown="1">

<ins id="ex5">**예시 5 (로그함수)**</ins> $$\ln(1+x)$$는 $$f^{(k)}(0) = (-1)^{k-1}(k-1)!$$이므로

$$\ln(1+x) = \sum_{k=1}^\infty \frac{(-1)^{k-1}}{k} x^k \qquad (-1 < x \leq 1)$$

으로, 이를 미분해보면 무한급수의 식

$$\frac{1}{1+x}=\sum_{k=0}^\infty (-1)^{k}x^k$$

을 얻는다. 이는 더 일반적으로, 실수 $$\alpha$$에 대해 정의된 다음의 일반화된 이항급수

$$(1+x)^\alpha = \sum_{k=0}^\infty \binom{\alpha}{k} x^k, \qquad \binom{\alpha}{k} = \frac{\alpha(\alpha-1)\cdots(\alpha-k+1)}{k!} \qquad (\lvert x\rvert < 1)$$

의 $$\alpha = -1$$인 경우이다. 또 다른 예시로 $$\alpha = 1/2$$은 

$$\sqrt{1+x} = 1 + \frac{x}{2} - \frac{x^2}{8} + \cdots$$

를 준다. 

</div>

위의 예시들은 특히 도함수가 유계인 경우 그 테일러 급수가 자기자신과 같다는 것을 보여준다. 이를 정식으로 적으면 다음과 같다. 

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> $$f$$가 $$a$$를 포함하는 구간 $$I$$에서 무한히 미분가능하고, 어떤 상수 $$M$$에 대해 모든 $$n$$과 모든 $$x \in I$$에서 $$\lvert f^{(n)}(x)\rvert \leq M$$이면, $$f$$는 $$I$$에서 자신의 테일러 급수와 일치한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

테일러 정리의 나머지는

$$\lvert R_n(x)\rvert = \frac{\lvert f^{(n+1)}(c)\rvert}{(n+1)!}\lvert x-a\rvert^{n+1} \leq \frac{M\,\lvert x-a\rvert^{n+1}}{(n+1)!}$$

이다. 우변은 고정된 $$x$$에서 $$n \to \infty$$일 때 $$0$$으로 가므로 ([§수열의 극한, ⁋예시 6](/ko/math/calculus/sequences#ex6)의 $$r^n/n! \to 0$$), $$R_n(x) \to 0$$이고 부분합이 $$f(x)$$로 수렴한다.

</details>

한편, [정리 2](#thm2)는 본질적으로 수치적인 것으로, 이를 사용하면 근삿값이 얼마나 정확한지를 손으로 평가할 수 있다. 가령 $$\sin(0.1)$$을 $$P_3(x) = x - x^3/6$$로 근사하면, 4차 나머지가 $$\lvert R_3(0.1)\rvert \leq (0.1)^4/4! \approx 4.2\times 10^{-6}$$이라 소수점 다섯째 자리까지 정확하다는 것을 확인할 수 있으며, $$e = \sum_k 1/k!$$를 처음 $$n+1$$항에서 끊은 오차는 $$\lvert R_n(1)\rvert \leq 3/(n+1)!$$ ($$e^c < 3$$) 임을 알 수 있다. 

또 다른 예시로, 테일러 전개는 단순히 최고차항 혹은 최저차항만 기억하는 것이 아니므로, $$0/0$$ 꼴의 극한을 계산할 때 강력하게 사용할 수 있다. 

<div class="example" markdown="1">

<ins id="ex7">**예시 7 (극한)**</ins> 극한 $$\lim_{x\to 0}(e^x - 1 - x)/x^2$$를 구하자. [예시 3](#ex3)에서 $$e^x = 1 + x + x^2/2 + x^3/6 + \cdots$$이므로

$$\frac{e^x - 1 - x}{x^2} = \frac{x^2/2 + x^3/6 + \cdots}{x^2} = \frac12 + \frac{x}{6} + \cdots \to \frac12$$

이다. 이는 로피탈 정리를 두 번 적용하여도 확인할 수 있는 결과로, 테일러 전개가 고차식의 정보까지 기억하고 있으므로 이를 분모와 분자 양쪽에서 약분해도 여전히 정보가 남아있기 때문이다. 

</div>