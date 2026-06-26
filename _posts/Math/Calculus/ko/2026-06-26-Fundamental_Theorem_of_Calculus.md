---
title: "미적분의 기본정리"
description: "미분과 적분이 서로 역연산임을 밝히는 미적분의 기본정리를 두 형태로 증명한다. 가변상한 적분이 피적분함수의 원시함수임을 보이고, 이를 통해 정적분을 원시함수의 차로 계산하는 평가정리와 그 응용, 멱급수의 항별 적분을 다룬다."
excerpt: "기본정리, 원시함수의 존재, 라이프니츠 규칙, 멱급수의 항별 적분"

categories: [Math / Calculus]
permalink: /ko/math/calculus/fundamental_theorem_of_calculus
sidebar: 
    nav: "calculus-ko"

date: 2026-06-26
weight: 11
---

우리는 앞선 글에서 서로 다른 두 종류의 적분, 즉 부정적분과 정적분을 정의했다. 부정적분은 미분의 역과정이라는 데에 그 의미가 있으며, 정적분은 그 자체로 곡선 아래의 넓이라는 기하학적 의미를 갖는다. 미적분의 기본정리는 이 둘이 어떤 방식으로는 완전히 같은 과정이라는 것을 보이며, 미적분학 자체가 여기서부터 탄생했다고 볼 수도 있다. 

## 미적분의 기본정리

부정적분은 그 정의부터가 미분의 역과정이므로, 이 과정에서 의미가 있는 것은 정적분이 실제로 미분의 역과정과 비슷한 결과를 준다는 것이다. 그러나 정적분은 결국 값을 내놓는 도구이므로, 그 결과물이 함수가 나오지는 않는다. 이에 우리는 정적분의 위쪽 끝을 변수로 두어 다음과 같은 함수

$$\int_a^x f(t)dt$$

로 둔다. 여기서 $$t$$는 그냥 dummy variable로, 위끝에 (이미) 들어간 $$x$$와 헷갈리지 않도록 하기 위해 도입한 변수이며, 헷갈리지 않을 수 있다면 $$t$$도 얼마든지 $$x$$로 써도 된다. 

<div class="proposition" markdown="1">

<ins id="thm1">**정리 1 (미적분의 기본정리)**</ins> $$f$$가 $$[a,b]$$에서 연속이고 $$F(x) = \int_a^x f(t)dt$$로 정의하면, $$F$$는 $$[a,b]$$에서 미분가능하고 모든 $$x$$에서

$$F'(x) = f(x)$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

[§적분, ⁋명제 11](/ko/math/calculus/integration#prop11)의 둘째 결과에 의해, $$h>0$$에 대해서는

$$F(x+h) - F(x) = \int_a^{x+h} f - \int_a^x f = \int_x^{x+h} f(t)dt$$

이다. 그럼 $$f$$가 $$[x, x+h]$$에서 연속이므로 [§연속함수, ⁋정리 4](/ko/math/calculus/continuity#thm4)에 의해 그 구간에서 최솟값 $$m_h$$와 최댓값 $$M_h$$를 가지며, [§적분, ⁋명제 11](/ko/math/calculus/integration#prop11)의 셋째 결과에 의해

$$m_h \leq \frac{F(x+h) - F(x)}{h} \leq M_h$$

이 성립한다. 이제 $$h \to 0$$일 때 구간 $$[x, x+h]$$가 한 점 $$x$$로 줄어들고, $$f$$의 연속성에 의해 $$m_h, M_h \to f(x)$$이므로, [§함수의 극한, ⁋명제 8](/ko/math/calculus/functions_and_limits#prop8)에 의해 평균변화율이 $$f(x)$$로 수렴한다. $$h < 0$$인 경우도 비슷한 방식으로 증명을 완료할 수 있다. 

</details>

이 정리는 <em-ko>넓이가 쌓이는 속도가 곧 높이</em-ko>라는 직관의 엄밀한 표현이다. 즉, 적분으로 정의된 함수 $$F(x)$$가 한 점에서 늘어나는 비율 $$F'(x)$$는 바로 그 점에서의 피적분함수 값 $$f(x)$$이다.

<div class="proposition" markdown="1">

<ins id="cor2">**따름정리 2**</ins> $$[a,b]$$에서 연속인 모든 함수는 원시함수를 가진다. 구체적으로 $$F(x) = \int_a^x f(t)dt$$가 그 중 하나이다.

</div>

위에서 정의한 $$F(x)$$는 적분상수 $$C$$의 값을 하나로 고정한 것으로, 구체적으로 $$F(a)=0$$이도록 하는 적분상수를 택한 것으로 생각할 수 있다.

한편, 위의 따름정리는 이는 임의의 함수의 적분이 초등함수의 꼴로 나타난다는 것과는 다른 이야기로, 오직 위의 식으로 정의한 $$\int_a^x f(t)dt$$가 <em-ko>그 자체로</em-ko> $$f$$의 원시함수라는 것이다. 가령 다음 예시를 보자. 

<div class="example" markdown="1">

<ins id="ex3">**예시 3 (특수함수의 도함수)**</ins> *오차함수<sub>error function</sub>*는

$$\erf(x) = \frac{2}{\sqrt{\pi}}\int_0^x e^{-t^2}dt$$

로 정의된다. $$e^{-t^2}$$의 원시함수는 초등함수로 적히지 않으므로 이 적분은 닫힌 꼴이 없지만, [정리 1](#thm1)에 의해 $$\erf$$는 미분가능하고

$$\erf'(x) = \frac{2}{\sqrt{\pi}}e^{-x^2}$$

이다. 마찬가지로 *적분로그* $$\li(x) = \int_2^x dt/\ln t$$도 $$\li'(x) = 1/\ln x$$로 도함수가 즉시 나온다. 이처럼 적분으로 정의된 함수는 그 자체로 미적분의 대상이 된다.

</div>

이보다 약간 더 발전한 형태의 표현은 [명제 7](#prop7)에서 멱급수의 적분을 살펴본 후 다시 도입하게 된다.

한편 [정리 1](#thm1)과, 미분이 $$0$$인 함수는 상수함수뿐이라는 사실을 결합하면, 정적분을 원시함수의 차로 계산하는 강력한 도구를 얻는다.

<div class="proposition" markdown="1">

<ins id="thm4">**정리 4**</ins> $$f$$가 $$[a,b]$$에서 연속이고 $$G$$가 $$f$$의 임의의 원시함수이면

$$\int_a^b f(x)dx = G(b) - G(a)$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$F(x) = \int_a^x f$$로 두면 [정리 1](#thm1)에 의해 $$F$$도 $$f$$의 원시함수이다. 두 원시함수는 상수 차이뿐이므로 ([§평균값 정리, ⁋따름정리 5](/ko/math/calculus/mean_value_theorem#cor5)) $$F = G + C$$인 상수 $$C$$가 있다. $$F(a) = \int_a^a f = 0$$이므로 $$C = -G(a)$$이고, 따라서

$$\int_a^b f = F(b) = G(b) + C = G(b) - G(a)$$

이다.

</details>

흔히 $$G(b) - G(a)$$를 $$\bigl[G(x)\bigr]_a^b$$로 적는다. 이 정리 덕분에 정적분의 계산은 리만 합의 극한이 아니라 원시함수를 찾는 문제로 환원된다. 가령 $$\int_0^1 x^2dx = \bigl[x^3/3\bigr]_0^1 = 1/3$$은 [§적분](/ko/math/calculus/integration)에서 리만 합으로 힘겹게 얻은 값과 일치하지만, 여기서는 전혀 다른 계산, 즉 원시함수에 양 끝점을 대입하는 것으로 얻어진다.

특히 [정리 1](#thm1)은 적분의 상·하한이 변수에 의존할 때 [§미분법, ⁋정리 4](/ko/math/calculus/differentiation_rules#thm4)과 결합된다. 상한이 함수 $$g(x)$$이면 $$F(u) = \int_a^u f$$로 두어 $$\int_a^{g(x)} f = F(g(x))$$이고, $$F'(u) = f(u)$$이므로 연쇄법칙으로 $$\frac{d}{dx}\int_a^{g(x)} f(t)dt = f(g(x))g'(x)$$이다. 상·하한이 모두 변수이면 이를 두 개의 구간으로 나누어 양쪽에 적용하면 된다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5 (라이프니츠 규칙)**</ins> $$f$$가 연속이고 $$g, h$$가 미분가능하면

$$\frac{d}{dx}\int_{h(x)}^{g(x)} f(t)dt = f(g(x))g'(x) - f(h(x))h'(x)$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

임의의 고정점 $$c$$를 잡아 [§적분, ⁋명제 11](/ko/math/calculus/integration#prop11)의 구간가법성으로 적분을 둘로 나눈다.

$$\int_{h(x)}^{g(x)} f(t)dt = \int_c^{g(x)} f(t)dt - \int_c^{h(x)} f(t)dt$$

이다. $$F(u) = \int_c^v f(v)dv$$로 두면[정리 1](#thm1)에 의해 $$F'(u) = f(u)$$이고, 우변은 $$F(g(x)) - F(h(x))$$이다. 연쇄법칙을 두 항에 각각 적용하면

$$\begin{aligned}
\frac{d}{dx}\bigl[F(g(x)) - F(h(x))\bigr] &= F'(g(x))g'(x) - F'(h(x))h'(x) \\[2pt]
&= f(g(x))g'(x) - f(h(x))h'(x)
\end{aligned}$$

를 얻는다.

</details>

단, 주의할 것은 피적분함수가 적분구간에서 정의되지 않거나 불연속일 때 발생한다. 다음의 예시를 보자.

<div class="example" markdown="1">

<ins id="ex6">**예시 6**</ins> 적분

$$\int_{-1}^{1} \frac{dx}{x^2}$$

에 형식적으로 

$$\bigl[-x^{-1}\bigr]_{-1}^{1} = -1 - 1 = -2$$

를 대입하면 음수가 나오는데, 피적분함수 $$1/x^2$$는 항상 양수이므로 이는 명백히 틀린 계산이다. 이것이 틀린 원인은 $$x = 0$$에서 피적분함수가 발산하여 $$[-1,1]$$에서 연속이 아니라는 데 있다. [정리 4](#thm4)의 가정이 깨졌으므로 이 정리를 그대로 쓸 수 없으며, 실제로 이 적분은 발산한다.

</div>

## 멱급수의 항별 적분

한편, 적분은 멱급수와도 잘 어울린다. 다음 명제 또한 증명을 위해서는 해석학의 지식이 필요하므로, 이는 우선 사실로 받아들이기로 한다. 

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7 (멱급수의 항별 적분)**</ins> $$f(x) = \sum_{n=0}^\infty c_n x^n$$이 수렴반경 $$R > 0$$을 가지면, $$\lvert x\rvert < R$$에서

$$\int_0^x f(t)dt = \sum_{n=0}^\infty \frac{c_n}{n+1} x^{n+1}$$

이고, 이 급수의 수렴반경도 $$R$$이다.

</div>

그럼 앞서 [예시 3](#ex3)에서 살펴본 $$e^{-x^2}$$가 어떤 형태로 쓰이는지 알 수 있다. 

<div class="example" markdown="1">

<ins id="ex8">**예시 8**</ins> [예시 3](#ex3)의 오차함수로 돌아가자. 지수함수의 멱급수로부터 

$$e^{-t^2} = \sum_{n=0}^\infty \frac{(-1)^n}{n!}t^{2n}$$

이며, 그 수렴반경은 $$\infty$$이다. 이제 [명제 7](#prop7)로 항별 적분하면

$$\int_0^x e^{-t^2}dt = \sum_{n=0}^\infty \frac{(-1)^n}{n!(2n+1)}x^{2n+1}$$

이고, 따라서

$$\erf(x) = \frac{2}{\sqrt{\pi}}\sum_{n=0}^\infty \frac{(-1)^n}{n!(2n+1)}x^{2n+1}$$

이다. 

즉, 여전히 원시함수가 초등함수로 적히지는 않지만, 이와 같이 명시적으로 멱급수로는 적어줄 수 있다. 

비슷한 방법으로 방법으로 $$1/(1 + x^2)$$와 $$1/(1+x)$$를 항별 적분하면 각각의 수렴반경 내에서

$$\arctan x = \sum_{n=0}^\infty \frac{(-1)^n}{2n+1} x^{2n+1}$$

그리고

$$\ln(1+x) = \sum_{n=1}^\infty \frac{(-1)^{n-1}}{n} x^n$$

을 얻는다.

</div>