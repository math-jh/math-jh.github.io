---
title: "미적분의 기본정리"
description: "미분과 적분이 서로 역연산임을 밝히는 미적분의 기본정리를 두 형태로 증명한다. 가변상한 적분이 피적분함수의 원시함수임을 보이고, 이를 통해 정적분을 원시함수의 차로 계산하는 평가정리와 그 응용을 다룬다."
excerpt: "기본정리 제1형, 원시함수의 존재, 평가정리, 라이프니츠 규칙"

categories: [Math / Calculus]
permalink: /ko/math/calculus/fundamental_theorem_of_calculus
sidebar: 
    nav: "calculus-ko"

date: 2026-06-02
weight: 12
drift_needed: true

published: false
---

미분과 적분은 서로 다른 동기에서 출발했다. 미분은 접선의 기울기·순간변화율을, 정적분 ([§정적분](/ko/math/calculus/definite_integral))은 곡선 아래의 넓이·누적된 양을 잰다. 역사적으로도 접선 문제와 구적 문제는 수천 년간 별개로 연구되었다. 미적분의 기본정리는 이 둘이 정확히 서로의 역연산임을 밝히며, 뉴턴과 라이프니츠가 이 사실을 포착한 것이 곧 미적분학의 탄생이다. 이 글에서는 그 정리를 두 형태로 세운다.

## 가변상한 적분과 제1형

연속함수 $$f$$의 정적분에서 위끝을 변수로 두어 새 함수를 만든다. 이 *가변상한 적분*이 다리 역할을 한다.

<div class="proposition" markdown="1">

<ins id="thm1">**정리 1 (미적분의 기본정리, 제1형)**</ins> $$f$$가 $$[a,b]$$에서 연속이고 $$F(x) = \int_a^x f(t)\,dt$$로 정의하면, $$F$$는 $$[a,b]$$에서 미분가능하고 모든 $$x$$에서

$$F'(x) = f(x)$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$h > 0$$에 대해 구간가법성 ([§정적분, ⁋명제 4](/ko/math/calculus/definite_integral#prop4))으로

$$F(x+h) - F(x) = \int_a^{x+h} f - \int_a^x f = \int_x^{x+h} f(t)\,dt$$

이다. $$f$$가 $$[x, x+h]$$에서 연속이므로 그 구간에서 최솟값 $$m_h$$와 최댓값 $$M_h$$를 가지며 ([§연속함수, ⁋정리 4](/ko/math/calculus/continuity#thm4)), 단조성에 의해 $$m_h\, h \leq \int_x^{x+h} f \leq M_h\, h$$, 곧

$$m_h \leq \frac{F(x+h) - F(x)}{h} \leq M_h$$

이다. $$h \to 0$$일 때 구간 $$[x, x+h]$$가 한 점 $$x$$로 줄어들고 $$f$$의 연속성으로 $$m_h, M_h \to f(x)$$이므로, [§함수의 극한, ⁋명제 8](/ko/math/calculus/functions_and_limits#prop8)에 의해 차분몫이 $$f(x)$$로 수렴한다. $$h < 0$$인 경우도 같은 평가로 처리되므로 $$F'(x) = f(x)$$이다.

</details>

제1형은 "넓이가 쌓이는 속도가 곧 높이"라는 직관의 엄밀한 표현이다. 가변상한 적분 $$F(x)$$가 한 점에서 늘어나는 비율 $$F'(x)$$는 바로 그 점에서의 피적분함수 값 $$f(x)$$이다. 이로써 부정적분에서 미뤄 둔 존재성 문제도 해결된다.

<div class="proposition" markdown="1">

<ins id="cor2">**따름정리 2**</ins> $$[a,b]$$에서 연속인 모든 함수는 원시함수를 가진다. 구체적으로 $$F(x) = \int_a^x f$$가 그 하나이다.

</div>

이는 [§부정적분](/ko/math/calculus/antiderivatives)에서 예고했던 사실로, 연속이라는 조건만으로 원시함수의 존재가 보장됨을 말한다. $$e^{-x^2}$$처럼 초등함수로 적히지 않는 원시함수도 이렇게 적분으로서 멀쩡히 존재한다.

## 평가정리

제1형과 평균값 정리의 따름정리를 결합하면, 정적분을 원시함수의 차로 계산하는 강력한 도구를 얻는다.

<div class="proposition" markdown="1">

<ins id="thm3">**정리 3 (미적분의 기본정리, 제2형)**</ins> $$f$$가 $$[a,b]$$에서 연속이고 $$G$$가 $$f$$의 임의의 원시함수이면

$$\int_a^b f(x)\,dx = G(b) - G(a)$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$F(x) = \int_a^x f$$로 두면 [정리 1](#thm1)에 의해 $$F$$도 $$f$$의 원시함수이다. 두 원시함수는 상수 차이뿐이므로 ([§평균값 정리, ⁋따름정리 5](/ko/math/calculus/mean_value_theorem#cor5)) $$F = G + C$$인 상수 $$C$$가 있다. $$F(a) = \int_a^a f = 0$$이므로 $$C = -G(a)$$이고, 따라서

$$\int_a^b f = F(b) = G(b) + C = G(b) - G(a)$$

이다.

</details>

흔히 $$G(b) - G(a)$$를 $$\bigl[G(x)\bigr]_a^b$$로 적는다. 평가정리 덕분에 정적분의 계산은 리만 합의 극한이 아니라 원시함수를 찾는 문제로 환원된다. 가령 $$\int_0^1 x^2\,dx = \bigl[x^3/3\bigr]_0^1 = 1/3$$은 [§정적분](/ko/math/calculus/definite_integral)에서 리만 합으로 힘겹게 얻은 값과 일치하되, 여기서는 원시함수를 대입해 즉시 나온다.

평가정리는 *순변화 정리*로도 읽을 수 있다. $$G$$를 $$F$$로, $$f$$를 $$F'$$로 보면

$$\int_a^b F'(x)\,dx = F(b) - F(a)$$

이니, "변화율 $$F'$$을 누적하면 순변화량 $$F(b) - F(a)$$"라는 뜻이다. 속도를 적분하면 변위가, 한계비용을 적분하면 총비용의 증가분이 나오는 것이 그 예이다. 이는 정적분이 단순한 넓이를 넘어 누적된 양을 재는 도구임을 다시 확인해 준다.

## 적분으로 정의된 함수

제1형이 보장한 원시함수의 존재는, 초등함수로 적히지 않는 피적분함수를 다룰 때 특히 빛난다. 그런 함수의 정적분은 닫힌 꼴을 갖지 못하지만, 가변상한 적분으로 정의된 함수 자체는 미분가능한 어엿한 함수이며 제1형으로 그 도함수를 즉시 안다.

<div class="example" markdown="1">

<ins id="ex4">**예시 4 (특수함수의 도함수)**</ins> *오차함수<sub>error function</sub>*는

$$\erf(x) = \frac{2}{\sqrt{\pi}}\int_0^x e^{-t^2}\,dt$$

로 정의된다. $$e^{-t^2}$$의 원시함수는 초등함수로 적히지 않으므로 이 적분은 닫힌 꼴이 없지만, 제1형 ([정리 1](#thm1)) 에 의해 $$\erf$$는 미분가능하고

$$\erf'(x) = \frac{2}{\sqrt{\pi}}\,e^{-x^2}$$

이다. 마찬가지로 *적분로그* $$\li(x) = \int_2^x dt/\ln t$$도 $$\li'(x) = 1/\ln x$$로 도함수가 즉시 나온다. 이처럼 적분으로 정의된 함수는 그 자체로 미적분의 대상이 된다.

</div>

## 라이프니츠 규칙

제1형은 적분의 상·하한이 변수에 의존할 때 [§미분법, ⁋정리 4](/ko/math/calculus/differentiation_rules#thm4)과 결합된다. 상한이 함수 $$g(x)$$이면 $$F(u) = \int_a^u f$$로 두어 $$\int_a^{g(x)} f = F(g(x))$$이고, $$F'(u) = f(u)$$이므로 연쇄법칙으로 $$\frac{d}{dx}\int_a^{g(x)} f(t)\,dt = f(g(x))\,g'(x)$$이다. 상·하한이 모두 변수이면 구간가법성으로 둘로 나누어 양쪽에 적용하면 된다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5 (일반 라이프니츠 규칙)**</ins> $$f$$가 연속이고 $$g, h$$가 미분가능하면

$$\frac{d}{dx}\int_{h(x)}^{g(x)} f(t)\,dt = f(g(x))\,g'(x) - f(h(x))\,h'(x)$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

임의의 고정점 $$c$$를 잡아 구간가법성 ([§정적분, ⁋명제 4](/ko/math/calculus/definite_integral#prop4))으로 적분을 둘로 나눈다.

$$\int_{h(x)}^{g(x)} f(t)\,dt = \int_c^{g(x)} f(t)\,dt - \int_c^{h(x)} f(t)\,dt$$

이다. $$F(u) = \int_c^u f$$로 두면 제1형 ([정리 1](#thm1)) 으로 $$F'(u) = f(u)$$이고, 우변은 $$F(g(x)) - F(h(x))$$이다. 연쇄법칙을 두 항에 각각 적용하면

$$\begin{aligned}
\frac{d}{dx}\bigl[F(g(x)) - F(h(x))\bigr] &= F'(g(x))\,g'(x) - F'(h(x))\,h'(x) \\[2pt]
&= f(g(x))\,g'(x) - f(h(x))\,h'(x)
\end{aligned}$$

를 얻는다.

</details>

가령 $$\Phi(x) = \int_{x}^{x^2} e^{t^2}\,dt$$에서는 $$f(t) = e^{t^2}$$, $$g(x) = x^2$$, $$h(x) = x$$이므로 $$\Phi'(x) = e^{x^4}\cdot 2x - e^{x^2}$$이다. 원시함수가 초등함수로 적히지 않아도 도함수는 이렇게 명시적으로 얻어진다.

평가정리의 한 가지 흔한 함정은 피적분함수가 적분구간에서 정의되지 않거나 불연속일 때 발생한다. 평가정리는 $$[a,b]$$ 전체에서의 연속성을 가정하므로, 그 가정이 깨지면 원시함수처럼 보이는 식을 기계적으로 대입해서는 안 된다.

<div class="example" markdown="1">

<ins id="ex6">**예시 6 (가정 위반)**</ins> $$\int_{-1}^{1} dx/x^2$$에 형식적으로 $$\bigl[-x^{-1}\bigr]_{-1}^{1} = -1 - 1 = -2$$를 대입하면 음수가 나오는데, 피적분함수 $$1/x^2$$는 항상 양수이므로 이는 명백히 틀렸다. 원인은 $$x = 0$$에서 피적분함수가 발산하여 $$[-1,1]$$에서 연속이 아니라는 데 있다. [정리 3](#thm3)의 가정이 깨졌으므로 평가정리를 그대로 쓸 수 없으며, 실제로 이 적분은 발산한다.

</div>

## 적분의 평균값 정리

마지막으로, 평가정리는 적분에 관한 평균값을 정의하고 평균값 정리의 적분판을 세우는 데에도 쓰인다. 연속함수의 가변상한 적분이 미분가능하다는 사실에 미분의 [§평균값 정리, ⁋정리 4](/ko/math/calculus/mean_value_theorem#thm4)를 적용하면 다음을 얻는다.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7 (적분의 평균값 정리)**</ins> $$f$$가 $$[a,b]$$에서 연속이면, 어떤 $$\xi \in [a,b]$$가 존재하여

$$\int_a^b f(x)\,dx = f(\xi)\,(b-a)$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$F(x) = \int_a^x f$$로 두면 제1형 ([정리 1](#thm1)) 에 의해 $$F$$는 $$[a,b]$$에서 미분가능하고 $$F'(x) = f(x)$$이다. 미분의 평균값 정리 ([§평균값 정리, ⁋정리 4](/ko/math/calculus/mean_value_theorem#thm4))를 $$F$$에 적용하면, 어떤 $$\xi \in (a,b)$$가 존재하여

$$\frac{F(b) - F(a)}{b - a} = F'(\xi) = f(\xi)$$

이다. $$F(b) - F(a) = \int_a^b f$$이고 $$F(a) = 0$$이므로, 양변에 $$b - a$$를 곱하면 $$\int_a^b f = f(\xi)(b-a)$$를 얻는다.

</details>

값 $$\frac{1}{b-a}\int_a^b f$$를 $$f$$의 $$[a,b]$$에서의 *평균값<sub>average value</sub>*이라 하며, [명제 7](#prop7)은 연속함수가 자신의 평균값을 구간 안 어딘가에서 실제로 취한다는 뜻이다.
</content>
</invoke>
