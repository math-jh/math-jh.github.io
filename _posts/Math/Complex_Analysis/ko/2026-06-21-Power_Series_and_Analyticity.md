---
title: "멱급수와 해석성"
description: "Cauchy 적분공식에서 핵을 기하급수로 전개하여, 정칙함수가 각 점 근방에서 자신의 Taylor 급수로 전개됨을 보이고 그 수렴반지름이 가장 가까운 특이점까지의 거리 이상임을 밝힌다. 역으로 수렴 멱급수가 정칙임을 더해 정칙성과 해석성이 동치임을 증명하고, 항별 미적분, 영점의 위수, Cauchy 곱을 다룬다."
excerpt: "Taylor 급수 전개, 정칙=해석적, 수렴반지름과 특이점, 항별 미분과 적분, 영점의 위수, Cauchy 곱"

categories: [Math / Complex Analysis]
permalink: /ko/math/complex_analysis/power_series_and_analyticity
sidebar: 
    nav: "complex_analysis-ko"

date: 2026-06-21
weight: 6

published: false
---

Cauchy 적분공식은 ([§Cauchy 적분공식, ⁋정리 1](/ko/math/complex_analysis/cauchy_integral_formula#thm1)) 정칙함수의 내부값을 경계적분 한 번으로 복원해 주었고, 그 적분기호 안에서 미분을 반복할 수 있어 정칙함수가 무한히 미분가능함을 ([§Cauchy 적분공식, ⁋따름정리 3](/ko/math/complex_analysis/cauchy_integral_formula#cor3)) 끌어냈다. 무한미분가능성이 확보되면 자연스럽게 떠오르는 물음은, 정칙함수가 각 점에서 자신의 Taylor 급수와 실제로 일치하느냐는 것이다. 실변수에서는 무한히 미분가능해도 Taylor 급수가 함수로 수렴하지 않을 수 있어 이 일치는 결코 자동이 아니다 ([\[해석학\] §멱급수와 해석함수, ⁋정의 4](/ko/math/analysis/power_series#def4) 뒤에 든 $$e^{-1/x^2}$$의 예). 그러나 복소변수에서는 사정이 완전히 다르다. Cauchy 적분공식의 핵 $$1/(w-z)$$를 기하급수로 펼치기만 하면 정칙함수가 언제나 자신의 Taylor 급수로 전개됨이 곧장 따라 나오며, 그 수렴반지름은 중심에서 가장 가까운 특이점까지의 거리 이상으로 보장된다. 역으로 수렴하는 멱급수의 합은 정칙이므로 ([§정칙함수, ⁋정리 9](/ko/math/complex_analysis/holomorphic_functions#thm9)), 정칙성과 한 점 근방에서의 멱급수 전개 가능성은 서로 완전히 같은 조건이 된다. 정칙함수를 가리키는 *해석함수<sub>analytic function</sub>*라는 또 하나의 이름은 바로 이 동치에서 비롯한다.

## 정칙함수의 Taylor 전개

핵심 발상은 Cauchy 적분공식의 핵을 기하급수로 펼치는 것이다. 중심 $$z_0$$을 둘러싼 경계원 위의 $$w$$와 그 내부의 점 $$z$$에 대해

$$\frac{1}{w - z} = \frac{1}{(w - z_0) - (z - z_0)} = \frac{1}{w - z_0}\cdot\frac{1}{1 - \frac{z - z_0}{w - z_0}}$$

으로 쓰면, $$\lvert z - z_0\rvert < \lvert w - z_0\rvert$$인 한 마지막 인수가 공비 $$(z - z_0)/(w - z_0)$$의 기하급수로 전개된다. 이를 적분공식에 대입하고 경계원 위에서 균등수렴하는 급수를 항별로 적분하면, $$f(z)$$가 $$(z - z_0)^n$$의 멱급수로 쓰이고 그 계수가 정확히 Cauchy 미분공식이 주는 $$f^{(n)}(z_0)/n!$$로 떨어진다.

<div class="proposition" markdown="1">

<ins id="thm1">**정리 1 (Taylor 전개)**</ins> $$f$$가 열린 원판 $$D(z_0, R)$$에서 정칙이라 하자. 그러면 모든 $$z \in D(z_0, R)$$에 대하여

$$f(z) = \sum_{n=0}^{\infty} \frac{f^{(n)}(z_0)}{n!}\,(z - z_0)^n$$

이고, 이 멱급수는 $$D(z_0, R)$$에서 절대수렴한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$z \in D(z_0, R)$$을 고정하고, $$\lvert z - z_0\rvert < r < R$$이 되도록 반지름 $$r$$을 잡는다. 닫힌 원판 $$\overline{D(z_0, r)}$$이 정칙 영역에 들어 있으므로 Cauchy 적분공식 ([§Cauchy 적분공식, ⁋정리 1](/ko/math/complex_analysis/cauchy_integral_formula#thm1)) 에 의해

$$f(z) = \frac{1}{2\pi i}\oint_{\lvert w - z_0\rvert = r} \frac{f(w)}{w - z}\,dw$$

이다. 경계원 위에서 $$\lvert w - z_0\rvert = r$$이고 $$\lvert z - z_0\rvert < r$$이므로 공비

$$q = \frac{z - z_0}{w - z_0}, \qquad \lvert q\rvert = \frac{\lvert z - z_0\rvert}{r} < 1$$

의 크기가 $$1$$보다 작아 핵을 기하급수로 전개할 수 있다. 곧

$$\frac{1}{w - z} = \frac{1}{w - z_0}\sum_{n=0}^{\infty}\left(\frac{z - z_0}{w - z_0}\right)^n = \sum_{n=0}^{\infty}\frac{(z - z_0)^n}{(w - z_0)^{n+1}}$$

이다. 우변의 급수는 $$w$$가 경계원 위를 움직일 때 $$\lvert q\rvert \leq \lvert z - z_0\rvert/r < 1$$로 공비가 $$w$$에 무관하게 위로 유계이므로, 경계원 위에서 균등수렴한다. $$f(w)$$가 경계원 위에서 유계이므로 ($$\lvert f(w)\rvert \leq M$$이라 하자) 이 균등수렴은 $$f(w)/(w - z_0)$$를 곱한 뒤에도 유지되고, 따라서 합과 적분의 순서를 바꿀 수 있어

$$f(z) = \frac{1}{2\pi i}\oint_{\lvert w - z_0\rvert = r}\left(\sum_{n=0}^{\infty}\frac{f(w)\,(z - z_0)^n}{(w - z_0)^{n+1}}\right)dw = \sum_{n=0}^{\infty}\left(\frac{1}{2\pi i}\oint_{\lvert w - z_0\rvert = r}\frac{f(w)}{(w - z_0)^{n+1}}\,dw\right)(z - z_0)^n$$

이다. 괄호 안의 적분은 Cauchy 미분공식 ([§Cauchy 적분공식, ⁋정리 2](/ko/math/complex_analysis/cauchy_integral_formula#thm2)) 에 의해 $$f^{(n)}(z_0)/n!$$과 같으므로

$$f(z) = \sum_{n=0}^{\infty}\frac{f^{(n)}(z_0)}{n!}\,(z - z_0)^n$$

을 얻는다. 절대수렴은 위 항별 어림에서 일반항의 크기가 $$\lvert f^{(n)}(z_0)/n!\rvert\,\lvert z - z_0\rvert^n \leq M\,(\lvert z - z_0\rvert/r)^n$$으로 수렴하는 기하급수에 지배되기 때문이다 (Cauchy 부등식 [§Cauchy 적분공식, ⁋정리 4](/ko/math/complex_analysis/cauchy_integral_formula#thm4) 로 $$\lvert f^{(n)}(z_0)/n!\rvert \leq M/r^n$$). 끝으로 $$z$$가 임의였고 $$r < R$$을 $$z$$에 맞춰 잡았으므로 전개는 $$D(z_0, R)$$ 전체에서 성립한다.

</details>

정리 1은 정칙함수가 정칙 영역 안의 어느 점을 중심으로 잡아도 그 점을 중심으로 하는 멱급수로 전개됨을 말한다. 계수가 $$f^{(n)}(z_0)/n!$$로 도함수에 의해 결정되므로 이 급수는 정확히 $$f$$의 Taylor 급수이며, 실변수에서와 달리 나머지항의 거동을 따로 따질 필요 없이 항상 함수 자신으로 수렴한다. 전개의 중심을 $$z_0$$으로 옮겨 놓고 보면, 한 점에서 무한히 미분가능하다는 국소적 정보가 그 점 근방 전체에서의 함수값을 멱급수를 통해 완전히 복원한다는 뜻이다.

전개가 성립하는 반지름에 관해서는 정리 1이 이미 다음을 함의한다. $$f$$가 $$D(z_0, R)$$ 전체에서 정칙이기만 하면 Taylor 급수가 그 원판 전체에서 수렴하므로, 멱급수의 수렴반지름은 $$R$$ 이상이다. 이를 특이점의 언어로 다시 적으면 수렴반지름의 기하학적 의미가 드러난다.

<div class="proposition" markdown="1">

<ins id="cor2">**따름정리 2 (수렴반지름과 특이점)**</ins> $$f$$가 점 $$z_0$$에서 정칙이라 하고, $$f$$의 $$z_0$$에서의 Taylor 급수의 수렴반지름을 $$\rho$$라 하자. 그러면 $$\rho$$은 $$z_0$$을 중심으로 하여 $$f$$가 정칙하게 확장되는 가장 큰 열린 원판의 반지름과 같다. 특히 $$f$$가 $$D(z_0, R)$$에서 정칙이면 $$\rho \geq R$$이고, 곧 $$\rho$$은 $$z_0$$에서 $$f$$의 가장 가까운 특이점까지의 거리 이상이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$f$$가 정칙하게 확장되는 가장 큰 열린 원판의 반지름을 $$R_\ast \in (0, \infty]$$이라 하자. 곧 $$f$$는 $$D(z_0, R_\ast)$$에서 정칙이지만 그보다 큰 어떤 중심 $$z_0$$의 원판으로도 정칙하게 확장되지 않는다. 정리 1을 $$D(z_0, R_\ast)$$에 적용하면 Taylor 급수가 이 원판 전체에서 수렴하므로 수렴반지름은 $$\rho \geq R_\ast$$이다.

반대로 $$\rho > R_\ast$$이라 가정하면, 멱급수 $$\sum_n \frac{f^{(n)}(z_0)}{n!}(z - z_0)^n$$가 $$D(z_0, \rho)$$에서 수렴하고, 수렴 멱급수의 합은 그 수렴원판에서 정칙이므로 ([§정칙함수, ⁋정리 9](/ko/math/complex_analysis/holomorphic_functions#thm9)) 이 급수는 $$D(z_0, \rho) \supsetneq D(z_0, R_\ast)$$에서 정칙인 함수 $$g$$를 정의한다. $$g$$는 $$D(z_0, R_\ast)$$에서 $$f$$와 일치하므로 $$f$$를 더 큰 원판 $$D(z_0, \rho)$$로 정칙하게 확장한 것이 되어, $$R_\ast$$이 그러한 원판의 최대 반지름이라는 정의에 어긋난다. 따라서 $$\rho = R_\ast$$이다.

마지막 진술은 $$f$$가 $$D(z_0, R)$$에서 정칙이면 정의상 $$R_\ast \geq R$$이므로 $$\rho \geq R$$이라는 데서 나온다. 가장 가까운 특이점까지의 거리란 $$f$$가 정칙하게 확장되지 못하게 막는 점까지의 거리이므로, $$\rho = R_\ast$$은 그 거리와 같다 (특이점이 없으면 $$\rho = \infty$$).

</details>

따름정리 2는 멱급수의 수렴반지름이라는 순전히 해석적인 양이 실은 함수의 특이점이라는 기하학적 자료에 의해 결정됨을 보여 준다. 가령 $$1/(1 + z^2)$$는 실축 위에서는 매끄럽고 유계이지만 $$z = \pm i$$에서 분모가 소멸하므로, 원점에서의 Taylor 급수 $$\sum_n (-1)^n z^{2n}$$의 수렴반지름은 가장 가까운 특이점 $$\pm i$$까지의 거리인 $$1$$이다. 실변수만 보아서는 왜 하필 반지름이 $$1$$인지 설명할 길이 없던 현상이, 복소평면으로 올라가 허축 위의 특이점을 보면 곧장 해명된다.

## 정칙성과 해석성의 동치

이제 정칙함수가 해석적이라는 정리 1의 결론과, 멱급수의 합이 정칙이라는 역방향을 합쳐 두 개념의 동치를 정식으로 적는다. 함수가 한 점 근방에서 그곳을 중심으로 하는 멱급수와 일치하면 그 점에서 해석적이라 하는데 ([\[해석학\] §멱급수와 해석함수, ⁋정의 4](/ko/math/analysis/power_series#def4)), 복소변수에서는 이 해석성이 정칙성과 완전히 같은 조건이 된다.

<div class="proposition" markdown="1">

<ins id="thm3">**정리 3 (정칙 $$\iff$$ 해석적)**</ins> 열린집합 $$\Omega \subseteq \mathbb{C}$$ 위의 함수 $$f$$에 대하여 다음 두 조건은 동치이다.

1. $$f$$는 $$\Omega$$에서 정칙이다.
2. $$f$$는 $$\Omega$$의 각 점 $$z_0$$에서 해석적이다. 곧 각 $$z_0 \in \Omega$$의 어떤 근방에서 $$f$$가 그 점을 중심으로 하는 멱급수의 합으로 표현된다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$(1) \Rightarrow (2)$$. $$f$$가 $$\Omega$$에서 정칙이고 $$z_0 \in \Omega$$이라 하자. $$\Omega$$가 열려 있으므로 $$D(z_0, R) \subseteq \Omega$$인 $$R > 0$$이 있고, 정리 1에 의해 $$f$$는 이 원판에서 자신의 Taylor 급수와 같다. 곧 $$f$$는 $$z_0$$의 근방 $$D(z_0, R)$$에서 멱급수의 합이므로 $$z_0$$에서 해석적이다.

$$(2) \Rightarrow (1)$$. $$z_0 \in \Omega$$을 임의로 잡으면 가정에 의해 어떤 근방 $$D(z_0, r) \subseteq \Omega$$에서 $$f(z) = \sum_{n} a_n (z - z_0)^n$$이 성립한다. 수렴하는 멱급수의 합은 그 수렴원판에서 정칙이므로 ([§정칙함수, ⁋정리 9](/ko/math/complex_analysis/holomorphic_functions#thm9)) $$f$$는 $$D(z_0, r)$$에서, 특히 $$z_0$$에서 복소미분가능하다. $$z_0$$이 임의였으므로 $$f$$는 $$\Omega$$의 모든 점에서 복소미분가능하고, 따라서 $$\Omega$$에서 정칙이다 ([§정칙함수, ⁋정의 2](/ko/math/complex_analysis/holomorphic_functions#def2)).

</details>

정리 3은 복소해석에서 "정칙"과 "해석적"이라는 두 용어가 같은 함수족을 가리킴을 확정한다. 정칙성은 한 번의 복소미분가능성이라는 국소적 미분 조건으로 정의되고 해석성은 멱급수 전개라는 대수적·해석적 조건으로 정의되지만, 복소변수에서는 둘이 정확히 겹친다. 이 동치 덕분에 정칙함수를 다룰 때 미분의 관점과 급수의 관점을 자유로이 오갈 수 있으며, 한쪽에서 자명한 사실이 다른 쪽에서는 비자명한 정리가 되기도 한다. 실변수와의 결정적 차이는 $$(2) \Rightarrow (1)$$이 아니라 $$(1) \Rightarrow (2)$$에 있다. 실해석에서는 무한미분가능성이 해석성을 함의하지 않지만, 복소변수에서는 한 번의 미분가능성이 이미 해석성을 강제한다.

## 항별 미분과 적분

해석성과 정칙성이 같으므로, 정칙함수에 대한 연산을 그 멱급수 표현 위에서 항별로 수행할 수 있다. 멱급수는 수렴원판 안에서 마치 다항식처럼 미분되고 적분되며, 이 항별 연산은 ([§정칙함수, ⁋정리 9](/ko/math/complex_analysis/holomorphic_functions#thm9)) 의 항별미분과 그 원시함수 구성으로 정당화된다. 미분 쪽은 이미 정리 1에서 도함수가 다시 같은 중심의 멱급수로 주어짐을 보았으니, 여기서는 도함수의 계수가 어떻게 이동하는지와 항별 적분을 함께 정리한다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4 (항별 미분과 적분)**</ins> $$f(z) = \sum_{n=0}^{\infty} a_n (z - z_0)^n$$이 수렴반지름 $$\rho > 0$$을 가진다고 하자. 그러면 항별 미분 급수와 항별 적분 급수

$$\sum_{n=1}^{\infty} n\,a_n (z - z_0)^{n-1}, \qquad \sum_{n=0}^{\infty} \frac{a_n}{n+1}\,(z - z_0)^{n+1}$$

은 모두 같은 수렴반지름 $$\rho$$을 가지며, $$D(z_0, \rho)$$에서 각각 $$f'(z)$$와 $$f$$의 한 원시함수 $$F$$ (곧 $$F' = f$$, $$F(z_0) = 0$$) 를 나타낸다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

먼저 수렴반지름이 보존됨을 본다. $$\lim_{n\to\infty} n^{1/n} = 1$$이므로 Cauchy–Hadamard 공식 ([\[해석학\] §멱급수와 해석함수, ⁋정리 1](/ko/math/analysis/power_series#thm1)) 에서

$$\limsup_{n\to\infty}\lvert n\,a_n\rvert^{1/n} = \left(\lim_{n\to\infty} n^{1/n}\right)\limsup_{n\to\infty}\lvert a_n\rvert^{1/n} = \limsup_{n\to\infty}\lvert a_n\rvert^{1/n}$$

이고, 같은 식이 계수 $$a_n/(n+1)$$에 대해서도 $$\lim_{n\to\infty}(n+1)^{1/n} = 1$$로 성립한다. 따라서 세 급수의 수렴반지름이 모두 같은 $$\rho$$이다.

항별 미분이 $$f'$$을 준다는 것은 멱급수의 정칙성과 항별미분 정리의 내용 그대로이다 ([§정칙함수, ⁋정리 9](/ko/math/complex_analysis/holomorphic_functions#thm9)). 항별 적분에 대해서는 $$G(z) = \sum_{n=0}^{\infty} \frac{a_n}{n+1}(z - z_0)^{n+1}$$이 위에서 보인 대로 $$D(z_0, \rho)$$에서 수렴하므로 같은 항별미분 정리에 의해 정칙이고, 그 도함수는 항별로

$$G'(z) = \sum_{n=0}^{\infty} \frac{a_n}{n+1}\cdot(n+1)(z - z_0)^n = \sum_{n=0}^{\infty} a_n (z - z_0)^n = f(z)$$

이다. 또 $$z = z_0$$을 대입하면 $$G(z_0) = 0$$이므로, $$F = G$$가 $$F' = f$$와 $$F(z_0) = 0$$을 만족하는 원시함수이다.

</details>

명제 4의 두 연산은 정칙함수의 멱급수가 형식적인 다항식 조작과 똑같이 행동함을 보장한다. 미분은 지수를 하나 내려 $$a_n \mapsto n\,a_n$$로, 적분은 지수를 하나 올려 $$a_n \mapsto a_n/(n+1)$$로 계수를 옮기되, 어느 쪽도 수렴반지름을 줄이거나 늘리지 않는다. 수렴반지름이 보존된다는 점은 미분이나 적분이 새로운 특이점을 만들거나 없애지 않음을 따름정리 2의 관점에서 다시 말한 것이기도 하다. 실제 계산에서는 알려진 급수, 가령 기하급수 $$\sum_n z^n = 1/(1 - z)$$를 항별로 미분·적분하여 $$1/(1 - z)^2$$이나 $$-\log(1 - z)$$ 같은 함수의 전개를 손쉽게 얻는 데 쓰인다.

## 영점의 위수

해석성은 정칙함수가 영점 근방에서 어떻게 사라지는지를 정밀하게 기술하게 해 준다. $$f(z_0) = 0$$이면 Taylor 급수의 상수항이 사라지고, 더 높은 차수의 계수까지 차례로 사라지는 정도가 영점의 깊이를 잰다. 항등적으로 $$0$$이 아닌 정칙함수에서는 이 사라짐이 유한한 차수에서 멈추며, 그 차수가 영점의 위수이다.

<div class="definition" markdown="1">

<ins id="def5">**정의 5 (영점의 위수)**</ins> $$f$$가 $$z_0$$에서 정칙이고 $$f(z_0) = 0$$이며 $$z_0$$의 어떤 근방에서 $$f$$가 항등적으로 $$0$$은 아니라 하자. $$z_0$$에서의 Taylor 계수 $$a_n = f^{(n)}(z_0)/n!$$ 가운데 $$0$$이 아닌 것이 처음 나타나는 지수, 곧

$$m = \min\{\,n \geq 0 : a_n \neq 0\,\}$$

을 $$z_0$$에서 $$f$$의 *영점의 위수<sub>order of the zero</sub>*라 한다.

</div>

영점이라는 가정에서 $$a_0 = f(z_0) = 0$$이므로 위수는 항상 $$m \geq 1$$이다. 위수 $$1$$인 영점을 *단순영점<sub>simple zero</sub>*이라 부르고, 이는 $$f(z_0) = 0$$이면서 $$f'(z_0) \neq 0$$인 경우와 같다. 위수 $$m$$이 잘 정의되려면 그런 $$0$$이 아닌 계수가 존재해야 하는데, 만일 모든 $$a_n$$이 $$0$$이면 Taylor 급수가 항등적으로 $$0$$이 되어 정리 1에 의해 $$f$$가 $$z_0$$의 근방에서 항등적으로 $$0$$이 되므로, 그 경우를 정의에서 배제한 것이다. 위수의 핵심은 영점에서 $$(z - z_0)^m$$을 정확히 그만큼 뽑아낼 수 있다는 다음 인수분해이다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6 (영점의 인수분해)**</ins> $$f$$가 $$z_0$$에서 정칙이고 그곳에서 위수 $$m \geq 1$$인 영점을 가진다고 하자. 그러면 $$z_0$$의 어떤 근방에서 정칙이고 $$g(z_0) \neq 0$$인 함수 $$g$$가 존재하여 그 근방에서

$$f(z) = (z - z_0)^m\,g(z)$$

가 성립한다. 역으로 이러한 인수분해가 성립하면 $$f$$는 $$z_0$$에서 위수 $$m$$인 영점을 가진다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

정리 1에 의해 $$z_0$$의 어떤 원판 $$D(z_0, R)$$에서 $$f(z) = \sum_{n=0}^{\infty} a_n (z - z_0)^n$$이다. 위수의 정의에서 $$a_0 = \cdots = a_{m-1} = 0$$이고 $$a_m \neq 0$$이므로, 합을 $$n = m$$부터 시작하도록 다시 적고 $$(z - z_0)^m$$을 묶어내면

$$f(z) = \sum_{n=m}^{\infty} a_n (z - z_0)^n = (z - z_0)^m \sum_{k=0}^{\infty} a_{m+k}(z - z_0)^k$$

이다. 여기서

$$g(z) = \sum_{k=0}^{\infty} a_{m+k}(z - z_0)^k$$

로 두면, 이 멱급수는 원래 급수에서 앞쪽 유한 개 항을 떼고 지수를 평행이동한 것이므로 같은 수렴반지름을 가져 $$D(z_0, R)$$에서 수렴하고, 따라서 정칙이다 ([§정칙함수, ⁋정리 9](/ko/math/complex_analysis/holomorphic_functions#thm9)). 또 $$g(z_0) = a_m \neq 0$$이다. 이로써 $$f(z) = (z - z_0)^m g(z)$$를 얻는다.

역으로 $$f(z) = (z - z_0)^m g(z)$$이고 $$g$$가 $$z_0$$에서 정칙이며 $$g(z_0) \neq 0$$이라 하자. $$g$$를 $$g(z) = \sum_{k=0}^{\infty} b_k (z - z_0)^k$$로 전개하면 $$b_0 = g(z_0) \neq 0$$이고, 곱하면

$$f(z) = \sum_{k=0}^{\infty} b_k (z - z_0)^{m+k}$$

이므로 $$f$$의 Taylor 계수는 $$n < m$$에서 모두 $$0$$이고 $$n = m$$에서 $$b_0 \neq 0$$이다. 따라서 $$f$$는 $$z_0$$에서 위수 $$m$$인 영점을 가진다.

</details>

명제 6은 정칙함수의 영점이 다항식의 근과 똑같은 방식으로 인수 $$(z - z_0)^m$$을 내놓되, 남는 인수 $$g$$가 영점에서 사라지지 않는 정칙함수라는 점만 다름을 보인다. 이 인수분해에서 $$g(z_0) \neq 0$$이라는 조건이 $$g$$가 $$z_0$$ 근방에서 부호 없이 $$0$$에서 떨어져 있게 하므로, $$z_0$$ 근처에서 $$f$$의 영점은 $$z_0$$ 하나뿐이다. 곧 항등적으로 $$0$$이 아닌 정칙함수의 영점은 고립되어 있다. 또 위수 $$m$$은 $$f$$가 영점 근방에서 $$\lvert f(z)\rvert \approx \lvert g(z_0)\rvert\,\lvert z - z_0\rvert^m$$의 비율로 사라짐을 알려 주어, 영점의 깊이를 정량적으로 잰다.

<div class="example" markdown="1">

<ins id="ex7">**예시 7 (위수의 계산)**</ins> 함수 $$f(z) = z^2(e^z - 1)$$의 원점에서의 영점의 위수를 구한다. $$e^z = \sum_{n\geq 0} z^n/n!$$이므로 ([§정칙함수, ⁋정의 10](/ko/math/complex_analysis/holomorphic_functions#def10))

$$e^z - 1 = z + \frac{z^2}{2!} + \frac{z^3}{3!} + \cdots = z\left(1 + \frac{z}{2!} + \frac{z^2}{3!} + \cdots\right)$$

이고, 괄호 안의 멱급수는 원점에서 값이 $$1 \neq 0$$이므로 $$e^z - 1$$은 원점에서 위수 $$1$$인 영점을 가진다. 따라서

$$f(z) = z^2(e^z - 1) = z^3\left(1 + \frac{z}{2!} + \frac{z^2}{3!} + \cdots\right)$$

이고 마지막 인수가 원점에서 $$1 \neq 0$$이므로, 명제 6에 의해 $$f$$는 원점에서 위수 $$3$$인 영점을 가진다. 인수가 곱해질 때 위수가 더해진다는 일반 규칙의 한 사례이다.

</div>

## Cauchy 곱

두 정칙함수의 곱도 정칙이므로 다시 멱급수로 전개되며, 그 계수는 두 인수의 계수로부터 유한 합으로 표현된다. 이것이 멱급수의 Cauchy 곱으로, 두 급수의 항을 형식적으로 모두 곱한 뒤 같은 차수끼리 묶어 얻는다. 정칙함수의 곱셈을 계수 수준에서 명시적으로 수행하게 해 주어, 전개를 도함수 계산 없이 대수적으로 결합하는 데 쓰인다.

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8 (Cauchy 곱)**</ins> 두 멱급수 $$f(z) = \sum_{n=0}^{\infty} a_n (z - z_0)^n$$과 $$g(z) = \sum_{n=0}^{\infty} b_n (z - z_0)^n$$이 각각 수렴반지름 $$\rho_f, \rho_g > 0$$을 가진다고 하자. 그러면 곱 $$fg$$은 $$\rho = \min(\rho_f, \rho_g)$$ 이상의 수렴반지름을 가지는 멱급수

$$f(z)\,g(z) = \sum_{n=0}^{\infty} c_n (z - z_0)^n, \qquad c_n = \sum_{k=0}^{n} a_k\,b_{n-k}$$

으로 전개되며, 이 전개는 $$D(z_0, \rho)$$에서 성립한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

두 급수는 모두 $$D(z_0, \rho)$$에서 절대수렴하므로 (정리 1의 절대수렴, 또는 각자의 수렴원판이 $$D(z_0, \rho)$$을 포함하므로), 절대수렴하는 두 급수의 곱을 재배열하는 정리를 적용할 수 있다. 곱 $$f(z)g(z)$$의 모든 항 $$a_k (z - z_0)^k \cdot b_l (z - z_0)^l$$을 더하되 절대수렴이 임의의 재배열을 허용하므로, 같은 총차수 $$k + l = n$$인 항끼리 묶으면

$$f(z)\,g(z) = \sum_{k=0}^{\infty}\sum_{l=0}^{\infty} a_k\,b_l\,(z - z_0)^{k+l} = \sum_{n=0}^{\infty}\left(\sum_{k=0}^{n} a_k\,b_{n-k}\right)(z - z_0)^n$$

이 되어 주장하는 계수 $$c_n = \sum_{k=0}^{n} a_k b_{n-k}$$를 얻는다. 한편 $$f$$와 $$g$$가 모두 $$D(z_0, \rho)$$에서 정칙이므로 그 곱 $$fg$$도 $$D(z_0, \rho)$$에서 정칙이고 ([§정칙함수, ⁋명제 3](/ko/math/complex_analysis/holomorphic_functions#prop3)), 정리 1에 의해 그 Taylor 급수가 $$D(z_0, \rho)$$ 전체에서 수렴하므로 곱급수의 수렴반지름은 $$\rho$$ 이상이다.

</details>

명제 8의 계수 공식 $$c_n = \sum_{k=0}^{n} a_k b_{n-k}$$는 두 계수열의 합성곱이며, 차수 $$n$$의 계수가 두 인수에서 차수의 합이 $$n$$이 되는 모든 조합의 기여를 모은 것이다. 이는 다항식의 곱셈을 무한급수로 확장한 것에 지나지 않으나, 정칙함수의 절대수렴이 재배열을 정당화해 주는 덕분에 유한 다항식에서와 똑같이 작동한다. 곱의 수렴반지름이 두 인수의 더 작은 쪽 이상이라는 결론도 따름정리 2의 시각에서 자연스럽다. 곱 $$fg$$의 특이점은 $$f$$나 $$g$$ 가운데 적어도 하나가 특이한 곳에서만 생기므로, 가장 가까운 특이점까지의 거리가 두 함수 각각의 그것보다 가까워질 수 없기 때문이다.

<div class="example" markdown="1">

<ins id="ex9">**예시 9 (Cauchy 곱으로 얻는 전개)**</ins> 기하급수 $$\dfrac{1}{1 - z} = \sum_{n=0}^{\infty} z^n$$ ($$\lvert z\rvert < 1$$) 을 자기 자신과 Cauchy 곱하여 $$1/(1 - z)^2$$의 전개를 얻는다. $$a_n = b_n = 1$$이므로

$$c_n = \sum_{k=0}^{n} a_k\,b_{n-k} = \sum_{k=0}^{n} 1 = n + 1$$

이고, 따라서

$$\frac{1}{(1 - z)^2} = \left(\sum_{n=0}^{\infty} z^n\right)^2 = \sum_{n=0}^{\infty} (n + 1)\,z^n \qquad (\lvert z\rvert < 1)$$

이다. 이는 기하급수를 명제 4로 항별 미분하여 얻는 $$\dfrac{1}{(1 - z)^2} = \sum_{n=1}^{\infty} n\,z^{n-1} = \sum_{n=0}^{\infty}(n+1)z^n$$과 정확히 일치하여, Cauchy 곱과 항별 미분이 같은 전개를 줌을 확인해 준다. 두 인수의 수렴반지름이 모두 $$1$$이고 곱의 수렴반지름도 $$1$$이어서 ($$z = 1$$이 $$1/(1-z)^2$$의 특이점이므로) 명제 8의 어림이 등호로 달성되는 경우이기도 하다.

</div>

---

**참고문헌**

**[Ahl]** L.V. Ahlfors, *Complex analysis*, 3rd ed., McGraw–Hill, 1979.

**[Con]** J.B. Conway, *Functions of one complex variable I*, 2nd ed., Graduate Texts in Mathematics 11, Springer, 1978.

**[SS]** E.M. Stein, R. Shakarchi, *Complex analysis*, Princeton Lectures in Analysis II, Princeton University Press, 2003.
</content>
</invoke>
