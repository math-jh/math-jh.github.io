---
title: "미적분의 기본정리"
description: "미분과 적분이 서로 역연산임을 밝히는 미적분의 기본정리를 두 형태로 증명한다. 가변상한 적분이 피적분함수의 원시함수임을 보이고, 이를 통해 정적분을 원시함수의 차로 계산하는 평가정리와 그 응용을 다룬다."
excerpt: "기본정리 제1형, 원시함수의 존재, 평가정리, 라이프니츠 규칙"

categories: [Math / Calculus]
permalink: /ko/math/calculus/fundamental_theorem_of_calculus
sidebar: 
    nav: "calculus-ko"

date: 2026-06-02
last_modified_at: 2026-06-02
weight: 10

published: false
---

미분과 적분은 서로 다른 동기에서 출발했다. 미분은 접선의 기울기·순간변화율을, 정적분 ([§정적분](/ko/math/calculus/definite_integral))은 곡선 아래의 넓이·누적된 양을 잰다. 역사적으로도 접선 문제와 구적 문제는 수천 년간 별개로 연구되었다. 미적분의 기본정리는 이 둘이 정확히 서로의 역연산임을 밝히며, 뉴턴과 라이프니츠가 이 사실을 포착한 것이 곧 미적분학의 탄생이다. 이 글에서는 그 정리를 두 형태로 세운다.

## 가변상한 적분과 제1형

연속함수 $$f$$의 정적분에서 위끝을 변수로 두어 새 함수를 만든다. 이 *가변상한 적분*이 다리 역할을 한다.

<div class="proposition" markdown="1">

<ins id="thm1">**정리 1 (미적분의 기본정리, 제1형)**</ins> $$f$$가 $$[a,b]$$에서 연속이고 $$F(x) = \displaystyle\int_a^x f(t)\,dt$$로 정의하면, $$F$$는 $$[a,b]$$에서 미분가능하고 모든 $$x$$에서

$$F'(x) = f(x)$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$h > 0$$에 대해 구간가법성 ([§정적분, ⁋명제 4](/ko/math/calculus/definite_integral#prop4))으로

$$F(x+h) - F(x) = \int_a^{x+h} f - \int_a^x f = \int_x^{x+h} f(t)\,dt$$

이다. $$f$$가 $$[x, x+h]$$에서 연속이므로 그 구간에서 최솟값 $$m_h$$와 최댓값 $$M_h$$를 가지며 ([§연속함수, ⁋정리 3](/ko/math/calculus/continuity#thm3)), 단조성에 의해 $$m_h\, h \leq \int_x^{x+h} f \leq M_h\, h$$, 곧

$$m_h \leq \frac{F(x+h) - F(x)}{h} \leq M_h$$

이다. $$h \to 0$$일 때 구간 $$[x, x+h]$$가 한 점 $$x$$로 줄어들고 $$f$$의 연속성으로 $$m_h, M_h \to f(x)$$이므로, 조임정리에 의해 차분몫이 $$f(x)$$로 수렴한다. $$h < 0$$인 경우도 같은 평가로 처리되므로 $$F'(x) = f(x)$$이다.

</details>

제1형은 "넓이가 쌓이는 속도가 곧 높이"라는 직관의 엄밀한 표현이다. 가변상한 적분 $$F(x)$$가 한 점에서 늘어나는 비율 $$F'(x)$$는 바로 그 점에서의 피적분함수 값 $$f(x)$$이다. 이로써 부정적분에서 미뤄 둔 존재성 문제도 해결된다.

<div class="proposition" markdown="1">

<ins id="cor2">**따름정리 2**</ins> $$[a,b]$$에서 연속인 모든 함수는 원시함수를 가진다. 구체적으로 $$F(x) = \int_a^x f$$가 그 하나이다.

</div>

이는 [§부정적분, ⁋명제 2](/ko/math/calculus/antiderivatives#prop2) 부근에서 예고했던 사실로, 연속이라는 조건만으로 원시함수의 존재가 보장됨을 말한다. $$e^{-x^2}$$처럼 초등함수로 적히지 않는 원시함수도 이렇게 적분으로서 멀쩡히 존재한다.

## 평가정리

제1형과 평균값 정리의 따름정리를 결합하면, 정적분을 원시함수의 차로 계산하는 강력한 도구를 얻는다.

<div class="proposition" markdown="1">

<ins id="thm3">**정리 3 (미적분의 기본정리, 제2형)**</ins> $$f$$가 $$[a,b]$$에서 연속이고 $$G$$가 $$f$$의 임의의 원시함수이면

$$\int_a^b f(x)\,dx = G(b) - G(a)$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$F(x) = \int_a^x f$$로 두면 정리 1에 의해 $$F$$도 $$f$$의 원시함수이다. 두 원시함수는 상수 차이뿐이므로 ([§평균값 정리, ⁋따름정리 5](/ko/math/calculus/mean_value_theorem#cor5)) $$F = G + C$$인 상수 $$C$$가 있다. $$F(a) = \int_a^a f = 0$$이므로 $$C = -G(a)$$이고, 따라서

$$\int_a^b f = F(b) = G(b) + C = G(b) - G(a)$$

이다.

</details>

흔히 $$G(b) - G(a)$$를 $$\bigl[G(x)\bigr]_a^b$$로 적는다. 평가정리 덕분에 정적분의 계산은 리만 합의 극한이 아니라 원시함수를 찾는 문제로 환원된다.

<div class="example" markdown="1">

<ins id="ex4">**예시 4**</ins> 기본 부정적분으로 원시함수를 찾아 대입한다.

$$\int_0^1 x^2\,dx = \left[\frac{x^3}{3}\right]_0^1 = \frac13, \qquad \int_0^{\pi} \sin x\,dx = \bigl[-\cos x\bigr]_0^{\pi} = 2, \qquad \int_1^e \frac{dx}{x} = \bigl[\ln x\bigr]_1^e = 1.$$

특히 $$\int_0^1 x^2 = \tfrac13$$은 [§정적분](/ko/math/calculus/definite_integral)에서 리만 합으로 힘겹게 얻은 값과 일치하되, 여기서는 즉시 나온다.

</div>

## 응용

제1형은 적분의 상한이 더 복잡한 함수일 때 연쇄법칙과 결합된다.

<div class="example" markdown="1">

<ins id="ex5">**예시 5 (라이프니츠 규칙)**</ins> $$H(x) = \displaystyle\int_0^{x^2} \sin t\,dt$$의 도함수를 구하자. $$F(u) = \int_0^u \sin t\,dt$$로 두면 $$H(x) = F(x^2)$$이고, 제1형으로 $$F'(u) = \sin u$$이므로 연쇄법칙에 의해

$$H'(x) = F'(x^2)\cdot 2x = 2x\sin(x^2)$$

이다. 일반적으로 $$\dfrac{d}{dx}\displaystyle\int_{a}^{g(x)} f(t)\,dt = f(g(x))\,g'(x)$$이며, 상·하한이 모두 변수이면 구간가법성으로 둘로 나누어 적용한다.

</div>

평가정리는 *순변화 정리*로도 읽을 수 있다. $$G$$를 $$F$$로, $$f$$를 $$F'$$로 보면

$$\int_a^b F'(x)\,dx = F(b) - F(a)$$

이니, "변화율 $$F'$$을 누적하면 순변화량 $$F(b) - F(a)$$"라는 뜻이다. 속도를 적분하면 변위가, 한계비용을 적분하면 총비용의 증가분이 나오는 것이 그 예이다. 이는 정적분이 단순한 넓이를 넘어 누적된 양을 재는 도구임을 다시 확인해 준다.

<div class="example" markdown="1">

<ins id="ex6">**예시 6 (순변화)**</ins> 속도가 $$v(t) = 3t^2 - 2t$$ (m/s) 인 물체가 $$t = 0$$부터 $$t = 2$$까지 움직인 변위는 $$\displaystyle\int_0^2 (3t^2 - 2t)\,dt = \bigl[t^3 - t^2\bigr]_0^2 = 8 - 4 = 4$$ (m) 이다. 반면 이동한 *거리*는 속도의 절댓값을 적분해야 하므로, $$v$$의 부호가 바뀌는 구간을 나누어 $$\int_0^2 \lvert v\rvert$$을 계산해야 한다 — 변위와 거리의 차이가 부호 있는 적분과 절댓값 적분의 차이로 드러난다.

</div>

## 예시와 계산

평가정리를 손에 쥐었으니, 리만 합의 극한으로는 엄두도 못 낼 정적분들이 원시함수 한 줄로 풀린다. 아래에서는 기본 부정적분의 목록을 다양한 정적분에 적용하면서, 평가정리가 실제 계산에서 어떻게 작동하는지 단계별로 펼쳐 본다. 핵심은 언제나 동일하다 — 피적분함수의 원시함수 $$G$$를 하나 찾고, 두 끝값에서의 차 $$G(b) - G(a)$$를 취한다.

<div class="example" markdown="1">

<ins id="ex7">**예시 7 (멱함수와 지수함수)**</ins> 멱함수의 원시함수는 지수를 하나 올린 뒤 그 지수로 나눈 것이다. $$n \neq -1$$인 경우

$$\begin{aligned}
\int_1^2 x^3\,dx &= \left[\frac{x^4}{4}\right]_1^2 = \frac{16}{4} - \frac{1}{4} = \frac{15}{4}, \\[4pt]
\int_0^4 \sqrt{x}\,dx &= \int_0^4 x^{1/2}\,dx = \left[\frac{2}{3}x^{3/2}\right]_0^4 = \frac{2}{3}\cdot 8 = \frac{16}{3}, \\[4pt]
\int_1^2 \frac{dx}{x^2} &= \int_1^2 x^{-2}\,dx = \bigl[-x^{-1}\bigr]_1^2 = -\frac12 + 1 = \frac12
\end{aligned}$$

이다. 지수함수와 자연로그의 경우에는

$$\int_0^{1} e^{x}\,dx = \bigl[e^x\bigr]_0^{1} = e - 1, \qquad \int_1^{e^2} \frac{dx}{x} = \bigl[\ln x\bigr]_1^{e^2} = 2$$

이다. 모든 계산이 "원시함수를 적고 두 끝값을 대입한다"는 한 가지 절차로 환원됨에 주목하자.

</div>

피적분함수가 음수 값을 가지면 정적분도 음수가 될 수 있다. 정적분은 부호 있는 넓이를 재므로, $$x$$축 아래의 영역은 음의 기여를 한다. 평가정리는 이 부호까지 자동으로 처리해 준다.

<div class="example" markdown="1">

<ins id="ex8">**예시 8 (부호 있는 넓이)**</ins> $$\sin x$$를 $$[0, 2\pi]$$에서 적분하면

$$\int_0^{2\pi} \sin x\,dx = \bigl[-\cos x\bigr]_0^{2\pi} = -\cos(2\pi) + \cos 0 = -1 + 1 = 0$$

이다. $$[0,\pi]$$에서의 양의 넓이 $$2$$와 $$[\pi, 2\pi]$$에서의 음의 넓이 $$-2$$가 정확히 상쇄된 결과이다. 곡선과 $$x$$축 사이의 실제 넓이를 원했다면

$$\int_0^{2\pi} \lvert \sin x\rvert\,dx = \int_0^{\pi}\sin x\,dx - \int_{\pi}^{2\pi}\sin x\,dx = 2 + 2 = 4$$

처럼 부호가 바뀌는 점에서 구간을 쪼개어 절댓값을 적분해야 한다.

</div>

제1형이 보장한 원시함수의 존재는, 초등함수로 적히지 않는 피적분함수를 다룰 때 특히 빛난다. 그런 함수의 정적분은 닫힌 꼴을 갖지 못하지만, 가변상한 적분으로 정의된 함수 자체는 미분가능한 어엿한 함수이며 제1형으로 그 도함수를 즉시 안다.

<div class="example" markdown="1">

<ins id="ex9">**예시 9 (특수함수의 도함수)**</ins> *오차함수<sub>error function</sub>*는

$$\operatorname{erf}(x) = \frac{2}{\sqrt{\pi}}\int_0^x e^{-t^2}\,dt$$

로 정의된다. $$e^{-t^2}$$의 원시함수는 초등함수로 적히지 않으므로 이 적분은 닫힌 꼴이 없지만, 제1형 (정리 1) 에 의해 $$\operatorname{erf}$$는 미분가능하고

$$\operatorname{erf}'(x) = \frac{2}{\sqrt{\pi}}\,e^{-x^2}$$

이다. 마찬가지로 *적분로그* $$\operatorname{li}(x) = \int_2^x \dfrac{dt}{\ln t}$$도 $$\operatorname{li}'(x) = \dfrac{1}{\ln x}$$로 도함수가 즉시 나온다. 이처럼 적분으로 정의된 함수는 그 자체로 미적분의 대상이 된다.

</div>

제1형과 연쇄법칙을 결합한 라이프니츠 규칙 (예시 5) 은, 적분의 상한뿐 아니라 하한까지 변수일 때로 자연스럽게 확장된다. 다음 명제는 그 일반형을 정리한 것이다.

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10 (일반 라이프니츠 규칙)**</ins> $$f$$가 연속이고 $$g, h$$가 미분가능하면

$$\frac{d}{dx}\int_{h(x)}^{g(x)} f(t)\,dt = f(g(x))\,g'(x) - f(h(x))\,h'(x)$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

임의의 고정점 $$c$$를 잡아 구간가법성 ([§정적분, ⁋명제 4](/ko/math/calculus/definite_integral#prop4))으로 적분을 둘로 나눈다.

$$\int_{h(x)}^{g(x)} f(t)\,dt = \int_c^{g(x)} f(t)\,dt - \int_c^{h(x)} f(t)\,dt$$

이다. $$F(u) = \int_c^u f$$로 두면 제1형 (정리 1) 으로 $$F'(u) = f(u)$$이고, 우변은 $$F(g(x)) - F(h(x))$$이다. 연쇄법칙을 두 항에 각각 적용하면

$$\begin{aligned}
\frac{d}{dx}\bigl[F(g(x)) - F(h(x))\bigr] &= F'(g(x))\,g'(x) - F'(h(x))\,h'(x) \\[2pt]
&= f(g(x))\,g'(x) - f(h(x))\,h'(x)
\end{aligned}$$

를 얻는다.

</details>

<div class="example" markdown="1">

<ins id="ex11">**예시 11 (양끝 변수 적분)**</ins> $$\displaystyle\Phi(x) = \int_{x}^{x^2} e^{t^2}\,dt$$의 도함수를 구하자. 명제 10에서 $$f(t) = e^{t^2}$$, $$g(x) = x^2$$, $$h(x) = x$$이므로 $$g'(x) = 2x$$, $$h'(x) = 1$$이고

$$\Phi'(x) = e^{(x^2)^2}\cdot 2x - e^{x^2}\cdot 1 = 2x\,e^{x^4} - e^{x^2}$$

이다. 원시함수가 초등함수로 적히지 않아도 도함수는 이렇게 명시적으로 얻어진다.

</div>

평가정리의 한 가지 흔한 함정은 피적분함수가 적분구간에서 정의되지 않거나 불연속일 때 발생한다. 평가정리는 $$[a,b]$$ 전체에서의 연속성을 가정하므로, 그 가정이 깨지면 원시함수처럼 보이는 식을 기계적으로 대입해서는 안 된다.

<div class="example" markdown="1">

<ins id="ex12">**예시 12 (가정 위반)**</ins> $$\displaystyle\int_{-1}^{1} \frac{dx}{x^2}$$에 형식적으로 $$\bigl[-x^{-1}\bigr]_{-1}^{1} = -1 - 1 = -2$$를 대입하면 음수가 나오는데, 피적분함수 $$1/x^2$$는 항상 양수이므로 이는 명백히 틀렸다. 원인은 $$x = 0$$에서 피적분함수가 발산하여 $$[-1,1]$$에서 연속이 아니라는 데 있다. 정리 3의 가정이 깨졌으므로 평가정리를 그대로 쓸 수 없으며, 이런 적분은 [§이상적분](/ko/math/calculus/improper_integrals)에서 극한으로 따로 다룬다 — 실제로 이 적분은 발산한다.

</div>

마지막으로, 평가정리는 적분에 관한 평균값을 정의하고 평균값 정리의 적분판을 세우는 데에도 쓰인다. 연속함수의 가변상한 적분이 미분가능하다는 사실에 미분의 평균값 정리를 적용하면 다음을 얻는다.

<div class="proposition" markdown="1">

<ins id="prop13">**명제 13 (적분의 평균값 정리)**</ins> $$f$$가 $$[a,b]$$에서 연속이면, 어떤 $$\xi \in [a,b]$$가 존재하여

$$\int_a^b f(x)\,dx = f(\xi)\,(b-a)$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$F(x) = \int_a^x f$$로 두면 제1형 (정리 1) 에 의해 $$F$$는 $$[a,b]$$에서 미분가능하고 $$F'(x) = f(x)$$이다. 미분의 평균값 정리 ([§평균값 정리, ⁋정리 4](/ko/math/calculus/mean_value_theorem#thm4))를 $$F$$에 적용하면, 어떤 $$\xi \in (a,b)$$가 존재하여

$$\frac{F(b) - F(a)}{b - a} = F'(\xi) = f(\xi)$$

이다. $$F(b) - F(a) = \int_a^b f$$이고 $$F(a) = 0$$이므로, 양변에 $$b - a$$를 곱하면 $$\int_a^b f = f(\xi)(b-a)$$를 얻는다.

</details>

값 $$\dfrac{1}{b-a}\int_a^b f$$를 $$f$$의 $$[a,b]$$에서의 *평균값<sub>average value</sub>*이라 하며, 명제 13은 연속함수가 자신의 평균값을 구간 안 어딘가에서 실제로 취한다는 뜻이다. 가령 $$f(x) = x^2$$의 $$[0,3]$$에서의 평균값은 $$\dfrac{1}{3}\int_0^3 x^2\,dx = \dfrac{1}{3}\cdot 9 = 3$$이고, $$f(\xi) = \xi^2 = 3$$을 만족하는 $$\xi = \sqrt{3} \in (0,3)$$이 그 평균을 실현한다.

평가정리 덕분에 정적분의 계산은 원시함수를 찾는 문제로 귀착되며, 이를 위한 치환적분·부분적분 같은 기법은 다음 글 [§적분법](/ko/math/calculus/integration_techniques)에서 다룬다. 정적분에서는 이 기법들이 적분의 끝값까지 함께 변환하는 형태로 쓰인다. 적분 구간이나 피적분함수가 무한으로 가는 경우로의 확장은 [§이상적분](/ko/math/calculus/improper_integrals)에서, 그리고 본 정리의 가정인 연속함수의 적분가능성에 대한 엄밀한 증명은 [\[해석학\] §미적분의 기본정리](/ko/math/analysis/fundamental_theorem_of_calculus)에서 다룬다.
