---
title: "미분"
description: "미분가능성을 Carathéodory의 연속인자 형태로 정식화하여, 미분이 연속을 함의함과 연쇄법칙을 깔끔하게 증명한다. 미적분학에서 다룬 미분을 실수의 완비성 위에서 엄밀하게 재정초한다."
excerpt: "Carathéodory 미분, 미분가능성과 연속, 연쇄법칙"

categories: [Math / Analysis]
permalink: /ko/math/analysis/differentiation
sidebar: 
    nav: "analysis-ko"

header:
    overlay_image: /assets/images/Math/Analysis/Differentiation.png
    overlay_filter: 0.5

date: 2026-06-02
last_modified_at: 2026-06-02
weight: 12

published: false
---

[\[미적분학\] §미분과 도함수](/ko/math/calculus/derivatives)에서 미분을 차분몫의 극한으로 정의하였다. 이제 극한과 연속의 엄밀한 이론을 갖추었으므로, 미분을 다시 정초하되 차분몫의 분모가 사라지는 번거로움을 피하는 Carathéodory의 동치 형태를 채택한다.

## Carathéodory 미분

<div class="proposition" markdown="1">

<ins id="prop1">**명제 1**</ins> 구간 $$I$$에서 정의된 $$f$$가 $$a \in I$$에서 미분가능한 것은, $$a$$에서 연속인 함수 $$\varphi : I \to \mathbb{R}$$가 존재하여 모든 $$x \in I$$에 대해

$$f(x) - f(a) = \varphi(x)\,(x - a)$$

가 성립하는 것과 동치이다. 이때 $$\varphi(a) = f'(a)$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$f$$가 $$a$$에서 미분가능하면 $$\varphi(x) = \dfrac{f(x)-f(a)}{x-a}$$ ($$x \neq a$$), $$\varphi(a) = f'(a)$$로 두면 미분가능성의 정의가 곧 $$\varphi$$의 $$a$$에서의 연속이다. 거꾸로 그런 연속 $$\varphi$$가 있으면 $$x \neq a$$에서 $$\dfrac{f(x)-f(a)}{x-a} = \varphi(x) \to \varphi(a)$$이므로 $$f'(a) = \varphi(a)$$가 존재한다.

</details>

이 형태는 분모 $$x - a$$를 곱셈으로 옮겨 두어, 미분의 기본 정리들을 극한 조작 없이 함수의 연속성만으로 끌어낸다.

## 미분가능성과 연속

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> $$f$$가 $$a$$에서 미분가능하면 $$a$$에서 연속이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

명제 1의 $$\varphi$$를 쓰면 $$f(x) = f(a) + \varphi(x)(x-a)$$이다. 우변은 $$a$$에서 연속인 함수들의 곱과 합이므로 ([§함수의 극한과 연속](/ko/math/analysis/limits_and_continuity)), $$x \to a$$일 때 $$f(x) \to f(a) + \varphi(a)\cdot 0 = f(a)$$이다.

</details>

## 연쇄법칙

Carathéodory 형태의 진가는 연쇄법칙의 증명에서 드러난다.

<div class="proposition" markdown="1">

<ins id="thm3">**정리 3 (연쇄법칙)**</ins> $$f$$가 $$a$$에서, $$g$$가 $$b = f(a)$$에서 미분가능하면 $$g \circ f$$가 $$a$$에서 미분가능하고 $$(g\circ f)'(a) = g'(f(a))f'(a)$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

명제 1로 $$a$$에서 연속인 $$\varphi$$와 $$b$$에서 연속인 $$\psi$$가 있어 $$f(x) - f(a) = \varphi(x)(x-a)$$, $$g(y) - g(b) = \psi(y)(y - b)$$이다. $$y = f(x)$$를 대입하면

$$g(f(x)) - g(f(a)) = \psi(f(x))\,\bigl(f(x) - f(a)\bigr) = \psi(f(x))\,\varphi(x)\,(x - a)$$

이다. $$f$$가 $$a$$에서 연속이고 $$\psi$$가 $$b = f(a)$$에서 연속이므로 $$x \mapsto \psi(f(x))\varphi(x)$$는 $$a$$에서 연속이고, 명제 1에 의해 $$g\circ f$$가 $$a$$에서 미분가능하며 그 미분계수는 $$\psi(f(a))\varphi(a) = g'(b)f'(a)$$이다.

</details>

차분몫을 직접 다룰 때 생기던 "$$f(x) - f(a) = 0$$일 때 0으로 나누는" 문제가 이 증명에는 전혀 나타나지 않는다. 같은 방식으로 합·곱·몫의 미분법도 엄밀하게 재현된다 ([\[미적분학\] §미분법](/ko/math/calculus/differentiation_rules)).

## 사칙연산의 미분법

연쇄법칙과 마찬가지로, 합·곱·몫의 미분법도 Carathéodory 인자를 결합하는 방식으로 분모를 거치지 않고 곧장 따라 나온다. 핵심은 명제 1의 연속인자 $$\varphi$$가 곱셈으로 깔끔하게 분배된다는 점이다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4 (곱의 미분법)**</ins> $$f, g$$가 $$a$$에서 미분가능하면 곱 $$fg$$도 $$a$$에서 미분가능하고

$$(fg)'(a) = f'(a)\,g(a) + f(a)\,g'(a)$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

명제 1로 $$a$$에서 연속인 $$\varphi, \psi$$가 있어 모든 $$x \in I$$에 대해 $$f(x) - f(a) = \varphi(x)(x-a)$$, $$g(x) - g(a) = \psi(x)(x-a)$$이고 $$\varphi(a) = f'(a)$$, $$\psi(a) = g'(a)$$이다. 두 항등식을 이용해 $$f(x)g(x) - f(a)g(a)$$를 전개하면

$$\begin{aligned}
f(x)g(x) - f(a)g(a) &= \bigl(f(x) - f(a)\bigr)g(x) + f(a)\bigl(g(x) - g(a)\bigr) \\
&= \varphi(x)(x-a)\,g(x) + f(a)\,\psi(x)(x-a) \\
&= \bigl[\varphi(x)\,g(x) + f(a)\,\psi(x)\bigr](x-a)
\end{aligned}$$

이다. 대괄호 안을 $$\Phi(x) = \varphi(x)g(x) + f(a)\psi(x)$$로 두면, $$\varphi, \psi, g$$가 모두 $$a$$에서 연속이므로 ($$g$$의 연속은 명제 2에서) $$\Phi$$도 $$a$$에서 연속이다. 따라서 명제 1에 의해 $$fg$$가 $$a$$에서 미분가능하고

$$(fg)'(a) = \Phi(a) = \varphi(a)g(a) + f(a)\psi(a) = f'(a)g(a) + f(a)g'(a)$$

이다.

</details>

여기서 결정적인 단계는 $$f(x)g(x) - f(a)g(a)$$를 두 차이의 합으로 쪼갠 첫 줄로, 한쪽에서는 $$f$$의 변화를, 다른 쪽에서는 $$g$$의 변화를 분리해 각각에 연속인자를 적용한다. 같은 분해 기법으로 몫의 미분법도 얻는다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5 (몫의 미분법)**</ins> $$f, g$$가 $$a$$에서 미분가능하고 $$g(a) \neq 0$$이면 $$f/g$$가 $$a$$의 한 근방에서 정의되어 $$a$$에서 미분가능하고

$$\left(\frac{f}{g}\right)'(a) = \frac{f'(a)g(a) - f(a)g'(a)}{g(a)^2}$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$g$$가 $$a$$에서 연속이고 $$g(a) \neq 0$$이므로, 연속함수의 부호 보존성 ([§함수의 극한과 연속](/ko/math/analysis/limits_and_continuity))에 의해 $$a$$의 한 근방에서 $$g$$는 $$0$$이 되지 않아 $$f/g$$가 정의된다. 그 근방에서 명제 1의 $$\varphi, \psi$$를 써서 차이를 정리하면

$$\begin{aligned}
\frac{f(x)}{g(x)} - \frac{f(a)}{g(a)} &= \frac{f(x)g(a) - f(a)g(x)}{g(x)g(a)} \\
&= \frac{\bigl(f(x)-f(a)\bigr)g(a) - f(a)\bigl(g(x)-g(a)\bigr)}{g(x)g(a)} \\
&= \frac{\varphi(x)g(a) - f(a)\psi(x)}{g(x)g(a)}\,(x-a)
\end{aligned}$$

이다. 분수로 둔 계수를 $$\Psi(x)$$라 하면 분자·분모가 모두 $$a$$에서 연속이고 분모 $$g(x)g(a)$$가 $$a$$에서 $$g(a)^2 \neq 0$$이므로 $$\Psi$$는 $$a$$에서 연속이다. 명제 1에 의해 $$f/g$$가 미분가능하고

$$\left(\frac{f}{g}\right)'(a) = \Psi(a) = \frac{\varphi(a)g(a) - f(a)\psi(a)}{g(a)^2} = \frac{f'(a)g(a) - f(a)g'(a)}{g(a)^2}$$

이다.

</details>

특히 $$f \equiv 1$$로 두면 $$\left(1/g\right)'(a) = -g'(a)/g(a)^2$$라는 역수의 미분법을 얻는다. 합의 미분법 $$(f+g)'(a) = f'(a) + g'(a)$$는 인자가 그대로 $$\varphi(x) + \psi(x)$$가 되어 더욱 직접적으로 따라 나오므로, 미분은 함수의 선형결합에 대해 선형으로 작용한다.

## 역함수의 미분

연쇄법칙의 한 응용으로 역함수의 미분계수를 계산할 수 있다. Carathéodory 형태는 여기서도 0으로 나누는 일을 피하게 해 준다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6 (역함수의 미분)**</ins> $$f$$가 구간 $$I$$에서 연속이고 단사이며 $$a \in I$$에서 미분가능하고 $$f'(a) \neq 0$$이라 하자. 역함수 $$f^{-1}$$이 $$b = f(a)$$에서 미분가능하면

$$(f^{-1})'(b) = \frac{1}{f'(a)} = \frac{1}{f'(f^{-1}(b))}$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$f^{-1}(f(x)) = x$$가 $$I$$의 모든 $$x$$에서 성립한다. 양변을 $$a$$에서 미분하되 좌변에는 연쇄법칙 (정리 3) 을 적용하면

$$(f^{-1})'(f(a))\cdot f'(a) = 1$$

이다. $$f(a) = b$$이고 $$f'(a) \neq 0$$이므로 양변을 $$f'(a)$$로 나누어 $$(f^{-1})'(b) = 1/f'(a)$$를 얻는다. $$a = f^{-1}(b)$$이므로 둘째 등식도 따른다.

</details>

가령 $$f(x) = x^n$$ ($$n \geq 1$$, $$x > 0$$) 의 역함수 $$f^{-1}(y) = y^{1/n}$$에 대해, $$f'(x) = nx^{n-1}$$이므로 $$y = x^n$$에서

$$(f^{-1})'(y) = \frac{1}{n x^{n-1}} = \frac{1}{n\,(y^{1/n})^{n-1}} = \frac{1}{n}\,y^{\frac{1}{n}-1}$$

이 되어, 유리수 지수에 대한 거듭제곱 미분법이 정수 지수의 경우로부터 복원된다.

## 예시와 계산

지금까지의 규칙을 구체적인 함수에 적용해 보자. 먼저 미분가능성과 연속의 위계를 분명히 하는 표준적인 예시를 든다.

<div class="example" markdown="1">

<ins id="ex7">**예시 7 (연속이지만 미분 불가능)**</ins> 절댓값 함수 $$f(x) = \lvert x\rvert$$는 $$\mathbb{R}$$ 전체에서 연속이지만 $$0$$에서 미분가능하지 않다. 명제 1의 형태로 보면, $$a = 0$$에서

$$f(x) - f(0) = \lvert x\rvert = \varphi(x)\,x, \qquad \varphi(x) = \begin{cases} 1 & (x > 0), \\ -1 & (x < 0) \end{cases}$$

를 만족하는 $$\varphi$$는 $$x = 0$$에서 좌우 극한이 $$-1$$과 $$1$$로 달라 연속으로 확장될 수 없다. 따라서 $$0$$에서 미분가능하지 않으며, 이는 명제 2의 역 — "연속이면 미분가능" — 이 거짓임을 보인다.

</div>

미분가능성이 연속보다 진정으로 강한 조건임을 보았으니, 이번에는 정의에서 출발해 한 점에서의 미분계수를 직접 계산해 본다.

<div class="example" markdown="1">

<ins id="ex8">**예시 8 (다항식의 연속인자)**</ins> $$f(x) = x^2$$에 대해 $$a$$에서의 연속인자를 직접 구하자. 차이를 인수분해하면

$$f(x) - f(a) = x^2 - a^2 = (x + a)(x - a)$$

이므로 $$\varphi(x) = x + a$$이다. 이는 다항식으로서 $$\mathbb{R}$$ 전체에서 연속이고, 명제 1에 의해 $$f'(a) = \varphi(a) = 2a$$이다. 같은 방식으로 $$g(x) = x^3$$이면

$$g(x) - g(a) = x^3 - a^3 = (x^2 + ax + a^2)(x - a)$$

이므로 $$\varphi(x) = x^2 + ax + a^2$$이고 $$g'(a) = 3a^2$$이다. 차분몫의 극한을 따로 계산할 필요 없이 인수분해가 곧 미분계수를 준다.

</div>

곱의 미분법과 결합하면 임의의 다항식의 미분이 즉시 계산된다.

<div class="example" markdown="1">

<ins id="ex9">**예시 9 (곱·몫의 미분법 적용)**</ins> $$h(x) = x^2(x+1)$$의 미분을 명제 4로 계산하면

$$\begin{aligned}
h'(x) &= (x^2)'\,(x+1) + x^2\,(x+1)' \\
&= 2x\,(x+1) + x^2\cdot 1 \\
&= 3x^2 + 2x
\end{aligned}$$

이고, 이는 $$h(x) = x^3 + x^2$$을 직접 미분한 결과와 일치한다. 한편 몫 $$k(x) = \dfrac{x}{x^2+1}$$의 미분은 명제 5로

$$k'(x) = \frac{1\cdot(x^2+1) - x\cdot 2x}{(x^2+1)^2} = \frac{1 - x^2}{(x^2+1)^2}$$

이 되어, 분자 $$1 - x^2$$의 부호로부터 $$k$$가 $$\lvert x\rvert < 1$$에서 증가하고 $$\lvert x\rvert > 1$$에서 감소함을 읽어낼 수 있다.

</div>

마지막으로 연쇄법칙과 역함수 미분법이 한꺼번에 쓰이는 예시를 본다.

<div class="example" markdown="1">

<ins id="ex10">**예시 10 (합성과 역함수)**</ins> $$F(x) = (x^2 + 1)^{3}$$을 $$g(u) = u^3$$, $$f(x) = x^2 + 1$$의 합성 $$F = g \circ f$$로 보면, 정리 3에 의해

$$F'(x) = g'(f(x))\,f'(x) = 3(x^2+1)^2 \cdot 2x = 6x\,(x^2+1)^2$$

이다. 또 $$f(x) = x^3 + x$$는 $$\mathbb{R}$$에서 단조증가하여 단사이고 $$f'(x) = 3x^2 + 1 > 0$$이므로, 명제 6에 의해 그 역함수는 모든 점에서 미분가능하며, 가령 $$f(1) = 2$$에서

$$(f^{-1})'(2) = \frac{1}{f'(1)} = \frac{1}{3\cdot 1 + 1} = \frac{1}{4}$$

이다. 역함수의 명시적 식 없이도 한 점에서의 미분계수를 얻을 수 있다는 점이 명제 6의 실용적 가치이다.

</div>

이러한 계산들은 모두 명제 1의 연속인자 형태에서 출발하여, 극한 조작을 함수의 연속성 판정으로 환원한다. 미분의 대수적 규칙 전체가 "연속인자를 결합해 다시 연속인자를 만든다"는 한 가지 원리로 통합되는 것이다.

이렇게 엄밀한 토대 위에서, 미분이 함수의 거동을 통제하는 핵심 정리 — 평균값 정리와 그 고계 일반화인 테일러 정리 — 를 다음 글 [§평균값 정리와 테일러 정리](/ko/math/analysis/mean_value_theorem)에서 다룬다.
