---
title: "미적분의 기본정리"
description: "Riemann 적분 위에서 미적분의 기본정리를 엄밀하게 증명한다. 가변상한 적분이 연속이며 피적분함수가 연속인 점에서 미분가능함을 보이고, 원시함수를 통한 정적분의 평가정리를 확립한다."
excerpt: "가변상한 적분의 미분, 평가정리, 미분과 적분의 역관계"

categories: [Math / Analysis]
permalink: /ko/math/analysis/fundamental_theorem_of_calculus
sidebar: 
    nav: "analysis-ko"

date: 2026-06-02
weight: 15

published: false
---

[§Riemann 적분](/ko/math/analysis/riemann_integral)에서 적분을 엄밀하게 정초하고, [§미분](/ko/math/analysis/differentiation)에서 미분을 다시 세웠다. 미적분의 기본정리는 이 둘이 서로의 역연산임을 밝히며, [\[미적분학\] §미적분의 기본정리](/ko/math/calculus/fundamental_theorem_of_calculus)에서 다룬 내용을 이제 완비성 위에서 증명한다.

미분은 한 점에서의 순간 변화율을, 적분은 한 구간 위에서의 누적량을 잰다. 표면적으로 이 둘은 서로 무관해 보인다 — 하나는 국소적이고 다른 하나는 대역적이며, 미분은 차분몫의 극한으로, 적분은 분할에 따른 상합·하합의 극대극소로 정의된다. 미적분의 기본정리가 말하는 바는, 그럼에도 두 연산이 서로를 정확히 되돌린다는 것이다. 누적량을 상한에 대해 미분하면 원래의 피적분함수가 되살아나고(제1형), 거꾸로 한 함수의 도함수를 적분하면 그 함수의 증분이 복원된다(제2형).

이 정리가 실용적으로 중요한 이유는, 적분을 분할의 극한으로 직접 계산하는 일이 거의 불가능에 가깝기 때문이다. 정의에 충실하게 $$\int_0^1 x^2\,dx$$를 구하려면 $$\sum_{i} (i/n)^2 \cdot (1/n)$$ 류의 합의 극한을 다뤄야 하지만, 원시함수 $$x^3/3$$ 하나를 안다면 평가정리가 즉시 값 $$1/3$$을 내어 준다. 우리는 가변상한 적분이 연속이며 연속점에서 미분가능함을 보이고(제1형), 이를 통해 원시함수에 의한 정적분 평가(제2형)를 확립한 뒤, 여러 계산 예시로 두 형태가 실제로 어떻게 쓰이는지를 본다.

## 가변상한 적분

적분의 상한을 변수로 두어 얻는 함수가 논의의 출발점이다. $$f$$가 $$[a,b]$$에서 적분가능하면, 각 $$x \in [a,b]$$에 대해 $$[a,x]$$ 위의 적분값이 하나 정해지므로 새 함수

$$F(x) = \int_a^x f$$

가 정의된다. 이를 $$f$$의 *가변상한 적분<sub>integral with variable upper limit</sub>*이라 부른다. 직관적으로 $$F(x)$$는 $$a$$에서 $$x$$까지 누적된 넓이이며, 우리가 가장 먼저 밝힐 것은 이 누적이 상한의 변화에 대해 얼마나 매끄럽게 반응하는가이다. 먼저 $$F$$가 연속임을, 그다음 $$f$$가 연속인 점에서는 $$F$$가 미분가능함을 본다.

<div class="proposition" markdown="1">

<ins id="prop1">**명제 1**</ins> $$f$$가 $$[a,b]$$에서 Riemann 적분가능하면 $$F(x) = \displaystyle\int_a^x f$$는 $$[a,b]$$에서 (립시츠) 연속이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$f$$는 적분가능하므로 유계이고, 따라서 $$\lvert f\rvert \leq M$$인 상수 $$M$$이 있다. $$x < y$$에 대해 구간가법성으로 $$F(y) - F(x) = \int_x^y f$$이며, 적분의 단조성과 절댓값 부등식으로

$$\begin{aligned}
\lvert F(y) - F(x)\rvert
&= \left\lvert \int_x^y f \right\rvert \\
&\leq \int_x^y \lvert f\rvert \\
&\leq \int_x^y M \\
&= M(y - x)
\end{aligned}$$

가 성립한다. 임의의 두 점 $$x, y$$에 대해 $$\lvert F(y) - F(x)\rvert \leq M\lvert y - x\rvert$$이므로 $$F$$는 립시츠 상수 $$M$$의 립시츠 연속이고, 특히 연속이다.

</details>

립시츠 연속이라는 결론은 단순한 연속보다 강하다. $$f$$가 유계라는 사실만으로 $$F$$의 변동이 상한의 변화에 선형으로 묶이며, 이는 $$F$$를 다루기 매우 편하게 만든다. 그러나 적분가능성만으로는 $$F$$가 미분가능하다고까지 말할 수 없다. 가령 $$f$$가 한 점에서 도약하면 $$F$$는 그 점에서 꺾여 좌우 미분계수가 달라진다. 미분가능성을 보장하려면 그 점에서 $$f$$의 연속성이 필요하며, 이것이 다음 정리의 내용이다.

<div class="proposition" markdown="1">

<ins id="thm2">**정리 2 (제1형)**</ins> 위의 $$F$$에 대하여, $$f$$가 점 $$x_0$$에서 연속이면 $$F$$는 $$x_0$$에서 미분가능하고 $$F'(x_0) = f(x_0)$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

구간가법성으로 $$F(x_0 + h) - F(x_0) = \int_{x_0}^{x_0+h} f$$이므로 차분몫은

$$\frac{F(x_0 + h) - F(x_0)}{h} = \frac1h\int_{x_0}^{x_0 + h} f$$

이다. 핵심 착상은 상수 $$f(x_0)$$ 또한 $$\frac1h\int_{x_0}^{x_0+h} f(x_0)\,dt = f(x_0)$$로 적분 형태로 쓸 수 있다는 점이며, 이를 이용해 차분몫과 목표값 $$f(x_0)$$의 차이를 하나의 적분으로 모은다. $$f$$가 $$x_0$$에서 연속이므로, 임의의 $$\varepsilon > 0$$에 대해 $$\lvert t - x_0\rvert < \delta$$이면 $$\lvert f(t) - f(x_0)\rvert < \varepsilon$$인 $$\delta > 0$$이 있다. $$0 < \lvert h\rvert < \delta$$이면 적분 구간의 모든 $$t$$가 $$x_0$$에서 $$\delta$$ 이내에 있으므로

$$\begin{aligned}
\left\lvert \frac{F(x_0+h) - F(x_0)}{h} - f(x_0)\right\rvert
&= \left\lvert \frac1h\int_{x_0}^{x_0+h} f(t)\,dt - \frac1h\int_{x_0}^{x_0+h} f(x_0)\,dt\right\rvert \\
&= \left\lvert \frac1h\int_{x_0}^{x_0+h}\bigl(f(t) - f(x_0)\bigr)\,dt\right\rvert \\
&\leq \frac{1}{\lvert h\rvert}\left\lvert \int_{x_0}^{x_0+h}\lvert f(t) - f(x_0)\rvert\,dt\right\rvert \\
&\leq \frac{1}{\lvert h\rvert}\cdot \varepsilon\lvert h\rvert \\
&= \varepsilon
\end{aligned}$$

가 성립한다. $$\varepsilon$$이 임의였으므로 차분몫은 $$h \to 0$$일 때 $$f(x_0)$$로 수렴하며, 따라서 $$F$$는 $$x_0$$에서 미분가능하고 $$F'(x_0) = f(x_0)$$이다.

</details>

특히 $$f$$가 $$[a,b]$$ 전체에서 연속이면 모든 점에서 $$F'(x) = f(x)$$이므로 $$F$$는 $$f$$의 원시함수이다. 즉 연속함수는 언제나 원시함수를 가지며, 그 하나가 바로 가변상한 적분 $$F(x) = \int_a^x f$$이다. 이는 존재 자체가 비자명한 결론이다 — 적분이라는 대역적 구성을 거치지 않고서는 일반적인 연속함수의 원시함수를 닫힌 형태로 쓸 길이 없으며, 가령 $$f(t) = e^{-t^2}$$의 원시함수는 초등함수로 표현되지 않지만 제1형은 그것이 함수 $$F(x) = \int_0^x e^{-t^2}\,dt$$로서 존재함을 보장한다.

## 평가정리

제1형이 "적분한 뒤 미분하면 제자리"라는 한쪽 방향을 다뤘다면, 평가정리(제2형)는 그 반대 방향 — "미분한 뒤 적분하면 증분이 복원된다" — 을 다룬다. 주목할 점은 제2형의 가정이 제1형보다 약하다는 것이다. $$f$$에 연속성을 요구하지 않고 적분가능성만 가정하며, 원시함수 $$G$$는 끝점을 포함한 닫힌구간에서 연속이고 열린구간에서 미분가능하면 충분하다. 증명의 핵심 도구는 평균값 정리로, 분할의 각 조각에서 $$G$$의 증분을 한 점에서의 도함수값 $$f(t_i)$$로 바꿔치기하여 $$G(b) - G(a)$$를 $$f$$의 한 리만 합으로 변신시킨다.

<div class="proposition" markdown="1">

<ins id="thm3">**정리 3 (제2형)**</ins> $$f$$가 $$[a,b]$$에서 적분가능하고 $$G$$가 $$[a,b]$$에서 연속이며 $$(a,b)$$에서 $$G' = f$$를 만족하는 함수이면

$$\int_a^b f = G(b) - G(a)$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

임의의 분할 $$P : a = x_0 < \cdots < x_n = b$$를 잡는다. 각 부분구간 $$[x_{i-1}, x_i]$$에서 $$G$$는 연속이고 그 내부에서 미분가능하므로, 평균값 정리 ([§평균값 정리와 테일러 정리, ⁋정리 3](/ko/math/analysis/mean_value_theorem#thm3))에 의해

$$G(x_i) - G(x_{i-1}) = G'(t_i)\,(x_i - x_{i-1}) = f(t_i)\,\Delta x_i$$

인 점 $$t_i \in (x_{i-1}, x_i)$$이 존재한다 (여기서 $$G' = f$$를 썼다). 이제 $$i = 1$$부터 $$n$$까지 합하면 좌변은 망원합으로 접혀

$$\begin{aligned}
G(b) - G(a)
&= \sum_{i=1}^n \bigl(G(x_i) - G(x_{i-1})\bigr) \\
&= \sum_{i=1}^n f(t_i)\,\Delta x_i
\end{aligned}$$

가 된다. 우변은 표본점 $$t_i$$로 만든 $$f$$의 한 리만 합이다. 각 부분구간에서 하한·상한을 잡으면 $$m_i \leq f(t_i) \leq M_i$$이므로 이 리만 합은 하합과 상합 사이에 끼이고,

$$L(P, f) \leq G(b) - G(a) \leq U(P, f)$$

가 모든 분할 $$P$$에 대해 성립한다. $$f$$가 적분가능하므로 분할을 충분히 잘게 하면 $$L(P, f)$$와 $$U(P, f)$$가 모두 $$\int_a^b f$$로 수렴하고, 가운데에 끼인 상수 $$G(b) - G(a)$$가 그 값과 같아야 한다. 따라서 $$\int_a^b f = G(b) - G(a)$$이다.

</details>

증명에서 $$G(b) - G(a)$$가 분할에 무관한 상수임에도 임의의 분할의 리만 합과 같다는 점이 결정적이다. 분할을 아무리 잘게 해도 그 합은 변하지 않으므로 극한값과 일치할 수밖에 없다. 또한 제2형이 제1형과 합쳐지면 강력한 따름이 나온다. $$f$$가 연속이면 제1형의 $$F(x) = \int_a^x f$$가 원시함수이고, 임의의 다른 원시함수 $$G$$는 $$(G - F)' = 0$$이므로 평균값 정리에 의해 $$G = F + C$$ 꼴로 상수만큼만 다르다. 따라서 $$G(b) - G(a) = F(b) - F(a) = \int_a^b f$$가 되어, 어느 원시함수를 쓰든 같은 값을 준다.

## 예시와 계산

두 형태가 실제 계산에서 어떻게 작동하는지를 본다. 먼저 평가정리는 원시함수 하나만 알면 정적분을 끝점에서의 값 차이로 환원한다.

<div class="example" markdown="1">

<ins id="ex4">**예시 4 (다항·지수의 정적분)**</ins> $$\int_0^1 x^2\,dx$$를 정의에서 직접 계산하는 대신, $$G(x) = x^3/3$$이 $$G'(x) = x^2$$을 만족하는 원시함수임을 관찰한다. 평가정리로

$$\int_0^1 x^2\,dx = G(1) - G(0) = \frac{1}{3} - 0 = \frac13$$

이다. 마찬가지로 $$G(x) = e^x$$이 자신의 원시함수이므로

$$\int_0^1 e^x\,dx = e^1 - e^0 = e - 1$$

이고, $$G(x) = -\cos x$$에서 $$G'(x) = \sin x$$이므로

$$\int_0^{\pi} \sin x\,dx = \bigl[-\cos x\bigr]_0^{\pi} = -\cos\pi + \cos 0 = 1 + 1 = 2$$

이다. 어느 경우든 분할의 극한을 다룰 필요 없이 끝점 대입만으로 값이 나온다.

</div>

제1형은 반대로, 적분으로 정의된 함수를 미분할 때 위력을 발휘한다. 합성이 끼면 연쇄법칙과 결합된다.

<div class="example" markdown="1">

<ins id="ex5">**예시 5 (가변상한 적분의 미분)**</ins> $$f$$가 연속일 때 $$\dfrac{d}{dx}\int_a^x f(t)\,dt = f(x)$$가 제1형의 직접적 귀결이다. 상한이 함수 $$u(x)$$인 경우에는 $$F(x) = \int_a^{u(x)} f$$를 $$\Phi(u) = \int_a^u f$$와 $$u(x)$$의 합성으로 보고 연쇄법칙을 적용한다. $$\Phi'(u) = f(u)$$이므로

$$\frac{d}{dx}\int_a^{u(x)} f(t)\,dt = f\bigl(u(x)\bigr)\,u'(x)$$

이다. 구체적으로

$$\frac{d}{dx}\int_0^{x^2} \cos t\,dt = \cos(x^2)\cdot 2x = 2x\cos(x^2)$$

이고, 상한과 하한이 모두 변수인 경우는 구간가법성으로 쪼개

$$\frac{d}{dx}\int_{x}^{x^2} e^{t^2}\,dt = e^{(x^2)^2}\cdot 2x - e^{x^2}\cdot 1 = 2x\,e^{x^4} - e^{x^2}$$

처럼 계산한다.

</div>

제1형이 보장하는 원시함수의 존재는, 닫힌 형태가 없는 적분조차 미분가능한 함수를 정의함을 뜻한다. 이는 특수함수를 정의하는 표준적 방식이다.

<div class="example" markdown="1">

<ins id="ex6">**예시 6 (초등적이지 않은 원시함수)**</ins> $$f(t) = e^{-t^2}$$은 $$\mathbb{R}$$에서 연속이지만 그 원시함수는 초등함수로 표현되지 않는다. 그럼에도 제1형은

$$\operatorname{erf}(x) = \frac{2}{\sqrt{\pi}}\int_0^x e^{-t^2}\,dt$$

가 모든 $$x$$에서 잘 정의된 미분가능 함수임을 보장하며, 그 도함수는

$$\operatorname{erf}'(x) = \frac{2}{\sqrt{\pi}}\,e^{-x^2}$$

이다. 같은 방식으로 적분로그 $$\operatorname{li}(x) = \int_2^x \dfrac{dt}{\ln t}$$나 프레넬 적분 $$\int_0^x \sin(t^2)\,dt$$도 적분을 통해 정의되고, 그 미분은 다시 피적분함수가 된다. 적분은 이렇게 새로운 함수를 만들어 내는 생성 장치 구실을 한다.

</div>

평가정리와 제1형을 결합하면 적분을 다루는 기본 규칙들이 따라 나온다. 다음은 부분적분의 엄밀한 근거이다.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7 (부분적분)**</ins> $$u, v$$가 $$[a,b]$$에서 연속미분가능하면

$$\int_a^b u\,v'\,dx = \bigl[u\,v\bigr]_a^b - \int_a^b u'\,v\,dx$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

곱의 미분법으로 $$(uv)' = u'v + uv'$$이고, $$u, v$$가 연속미분가능하므로 $$(uv)'$$는 연속, 따라서 적분가능하다. 양변을 $$[a,b]$$에서 적분한 뒤 $$uv$$가 $$(uv)'$$의 원시함수임을 써서 평가정리를 적용하면

$$\begin{aligned}
\bigl[u\,v\bigr]_a^b
&= \int_a^b (uv)'\,dx \\
&= \int_a^b u'\,v\,dx + \int_a^b u\,v'\,dx
\end{aligned}$$

가 된다. 우변의 한 항을 좌변으로 옮기면 주장한 등식을 얻는다.

</details>

부분적분은 한 인수의 미분을 다른 인수의 미분으로 옮겨 적분을 단순화한다. 가령 $$u = x$$, $$v' = e^x$$로 두면 $$u' = 1$$, $$v = e^x$$이므로

$$\int_0^1 x\,e^x\,dx = \bigl[x\,e^x\bigr]_0^1 - \int_0^1 e^x\,dx = e - (e - 1) = 1$$

이다. 마찬가지로 치환적분도 제1형과 연쇄법칙의 결합으로 정당화된다.

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8 (치환적분)**</ins> $$\varphi$$가 $$[a,b]$$에서 연속미분가능하고 $$f$$가 $$\varphi$$의 치역을 포함하는 구간에서 연속이면

$$\int_a^b f\bigl(\varphi(x)\bigr)\,\varphi'(x)\,dx = \int_{\varphi(a)}^{\varphi(b)} f(u)\,du$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$f$$가 연속이므로 제1형에 의해 원시함수 $$F(u) = \int_{\varphi(a)}^{u} f$$가 존재하고 $$F' = f$$이다. 합성 $$F \circ \varphi$$에 연쇄법칙을 적용하면

$$\begin{aligned}
\bigl(F\circ\varphi\bigr)'(x)
&= F'\bigl(\varphi(x)\bigr)\,\varphi'(x) \\
&= f\bigl(\varphi(x)\bigr)\,\varphi'(x)
\end{aligned}$$

이므로 $$F\circ\varphi$$는 좌변 피적분함수의 원시함수이다. 평가정리로

$$\begin{aligned}
\int_a^b f\bigl(\varphi(x)\bigr)\,\varphi'(x)\,dx
&= \bigl(F\circ\varphi\bigr)(b) - \bigl(F\circ\varphi\bigr)(a) \\
&= F\bigl(\varphi(b)\bigr) - F\bigl(\varphi(a)\bigr) \\
&= \int_{\varphi(a)}^{\varphi(b)} f(u)\,du
\end{aligned}$$

를 얻는다 (마지막 등식은 $$F$$의 정의에서 따른다).

</details>

치환은 적분을 더 다루기 쉬운 변수로 바꾼다. 예컨대 $$\varphi(x) = x^2$$, $$f(u) = e^u$$로 두면 $$\varphi'(x) = 2x$$이므로

$$\int_0^1 2x\,e^{x^2}\,dx = \int_{0}^{1} e^u\,du = e - 1$$

이 되어, 합성과 곱의 형태로 얽혀 있던 적분이 단순한 지수의 적분으로 풀린다.

평가정리는 [\[미적분학\] §적분법](/ko/math/calculus/integration_techniques)의 치환·부분적분이 의존하던 토대이며, 이제 그 가정들이 모두 엄밀하게 증명되었다. 한 함수의 적분을 넘어 함수들의 열의 극한과 적분·미분이 어떻게 교환되는지는 다음 글 [§함수열과 점별수렴](/ko/math/analysis/sequences_of_functions)에서 다룬다.
