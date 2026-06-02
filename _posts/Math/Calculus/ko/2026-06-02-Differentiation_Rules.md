---
title: "미분법"
description: "곱과 몫의 미분법, 연쇄법칙을 증명하고, 삼각함수·지수함수·로그함수의 도함수와 역함수의 미분법을 정리한다. 이로써 초등함수로 이루어진 임의의 함수를 체계적으로 미분할 수 있게 된다."
excerpt: "곱·몫의 미분법, 연쇄법칙, 초등함수의 도함수"

categories: [Math / Calculus]
permalink: /ko/math/calculus/differentiation_rules
sidebar: 
    nav: "calculus-ko"

header:
    overlay_image: /assets/images/Math/Calculus/Differentiation_Rules.png
    overlay_filter: 0.5

date: 2026-06-02
last_modified_at: 2026-06-02
weight: 4

published: false
---

[§미분과 도함수](/ko/math/calculus/derivatives)에서 미분의 선형성과 거듭제곱함수의 미분 공식을 얻었다. 그러나 함수의 곱·몫·합성이나 삼각·지수·로그함수가 섞이면 정의의 극한을 매번 직접 계산하는 것은 번거롭다. 이 글에서는 그러한 계산을 기계적으로 수행하게 해 주는 미분 규칙들을 정리한다.

## 곱과 몫의 미분법

미분은 선형 연산이지만, 곱에 대해서는 단순히 분배되지 않는다.

<div class="proposition" markdown="1">

<ins id="prop1">**명제 1 (곱의 미분법)**</ins> $$f, g$$가 $$a$$에서 미분가능하면 $$fg$$도 $$a$$에서 미분가능하고

$$(fg)'(a) = f'(a)\,g(a) + f(a)\,g'(a)$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

차분몫에 같은 항을 더하고 빼는 표준 기법을 쓴다.

$$\frac{f(a+h)g(a+h) - f(a)g(a)}{h} = \frac{f(a+h)-f(a)}{h}\,g(a+h) + f(a)\,\frac{g(a+h)-g(a)}{h}$$

$$h \to 0$$일 때 첫 항의 차분몫은 $$f'(a)$$로, $$g(a+h)$$는 $$g$$의 연속성 ([§미분과 도함수, ⁋명제 2](/ko/math/calculus/derivatives#prop2))에 의해 $$g(a)$$로 수렴한다. 둘째 항의 차분몫은 $$g'(a)$$로 수렴한다. 극한법칙 ([§함수와 극한, ⁋명제 3](/ko/math/calculus/functions_and_limits#prop3))에 의해 합은 $$f'(a)g(a) + f(a)g'(a)$$로 수렴한다.

</details>

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2 (몫의 미분법)**</ins> $$f, g$$가 $$a$$에서 미분가능하고 $$g(a) \neq 0$$이면 $$f/g$$도 $$a$$에서 미분가능하고

$$\left(\frac{f}{g}\right)'(a) = \frac{f'(a)\,g(a) - f(a)\,g'(a)}{g(a)^2}$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

먼저 $$1/g$$의 도함수를 구한다. $$g$$가 연속이고 $$g(a) \neq 0$$이므로 $$a$$ 근방에서 $$g \neq 0$$이고,

$$\frac{1}{h}\left(\frac{1}{g(a+h)} - \frac{1}{g(a)}\right) = -\frac{1}{g(a+h)g(a)}\cdot\frac{g(a+h)-g(a)}{h}$$

는 $$h \to 0$$일 때 $$-\dfrac{g'(a)}{g(a)^2}$$로 수렴한다. 따라서 $$(1/g)'(a) = -g'(a)/g(a)^2$$이다. 이제 $$f/g = f\cdot(1/g)$$에 곱의 미분법을 적용하면

$$\left(\frac{f}{g}\right)'(a) = f'(a)\frac{1}{g(a)} + f(a)\left(-\frac{g'(a)}{g(a)^2}\right) = \frac{f'(a)g(a) - f(a)g'(a)}{g(a)^2}$$

을 얻는다.

</details>

## 연쇄법칙

합성함수의 미분은 미적분에서 가장 널리 쓰이는 규칙이다.

<div class="proposition" markdown="1">

<ins id="thm3">**정리 3 (연쇄법칙)**</ins> $$f$$가 $$a$$에서 미분가능하고 $$g$$가 $$b = f(a)$$에서 미분가능하면, 합성 $$g \circ f$$도 $$a$$에서 미분가능하고

$$(g \circ f)'(a) = g'(f(a))\,f'(a)$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$g$$가 $$b$$에서 미분가능하다는 사실을 다음 보조함수로 옮긴다.

$$\varphi(y) = \begin{cases} \dfrac{g(y) - g(b)}{y - b}, & y \neq b,\\[1mm] g'(b), & y = b. \end{cases}$$

미분가능성의 정의에 의해 $$\varphi$$는 $$b$$에서 연속이고, 모든 $$y$$에 대해 $$g(y) - g(b) = \varphi(y)(y - b)$$가 성립한다. $$y = f(a+h)$$를 대입하면

$$\frac{g(f(a+h)) - g(f(a))}{h} = \varphi(f(a+h))\,\frac{f(a+h) - f(a)}{h}$$

이다. $$h \to 0$$일 때 $$f$$의 연속성으로 $$f(a+h) \to f(a) = b$$이고 $$\varphi$$의 연속성으로 $$\varphi(f(a+h)) \to \varphi(b) = g'(b)$$이며, 둘째 인자는 $$f'(a)$$로 수렴한다. 따라서 극한은 $$g'(f(a))f'(a)$$이다.

</details>

예를 들어 $$\dfrac{d}{dx}(x^2 + 1)^{10} = 10(x^2+1)^9 \cdot 2x$$이다.

## 삼각함수·지수함수·로그함수의 도함수

삼각함수의 미분은 다음 극한에 기댄다 (라디안 단위에서 부채꼴의 넓이를 비교하여 얻는다).

$$\lim_{h \to 0} \frac{\sin h}{h} = 1, \qquad \lim_{h \to 0} \frac{1 - \cos h}{h} = 0$$

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4 (삼각함수의 도함수)**</ins> 모든 점에서 $$(\sin x)' = \cos x$$, $$(\cos x)' = -\sin x$$이고, $$\cos x \neq 0$$인 점에서 $$(\tan x)' = \sec^2 x$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

덧셈정리 $$\sin(x+h) = \sin x\cos h + \cos x \sin h$$를 쓰면

$$\frac{\sin(x+h) - \sin x}{h} = \sin x \cdot \frac{\cos h - 1}{h} + \cos x \cdot \frac{\sin h}{h}$$

이고, $$h \to 0$$일 때 위 두 극한에 의해 $$\sin x \cdot 0 + \cos x \cdot 1 = \cos x$$로 수렴한다. $$\cos x$$의 도함수도 같은 방법으로 얻으며, $$\tan x = \sin x/\cos x$$에 몫의 미분법을 적용하면 $$(\tan x)' = (\cos^2 x + \sin^2 x)/\cos^2 x = \sec^2 x$$이다.

</details>

지수함수와 로그함수에 대해서는 $$\lim_{h\to 0}\dfrac{e^h - 1}{h} = 1$$이라는 사실 (이는 $$e$$를 그렇게 되도록 정하는 밑이라고 보아도 좋다) 로부터

$$\frac{e^{x+h} - e^x}{h} = e^x \cdot \frac{e^h - 1}{h} \to e^x$$

이므로 $$(e^x)' = e^x$$이다. 일반 밑에 대해서는 $$a^x = e^{x\ln a}$$와 연쇄법칙으로 $$(a^x)' = a^x \ln a$$를 얻는다. 자연로그의 도함수 $$(\ln x)' = 1/x$$는 다음 절의 역함수 미분법으로 유도한다.

## 역함수의 미분

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5 (역함수의 미분)**</ins> $$f$$가 한 구간에서 연속인 단조함수로 역함수 $$f^{-1}$$를 가지고, $$f$$가 $$a$$에서 미분가능하며 $$f'(a) \neq 0$$이라 하자. 그러면 $$f^{-1}$$은 $$b = f(a)$$에서 미분가능하고

$$(f^{-1})'(b) = \frac{1}{f'(f^{-1}(b))} = \frac{1}{f'(a)}$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$f^{-1}$$이 $$b$$에서 미분가능하다는 것을 받아들이면, 항등식 $$f(f^{-1}(y)) = y$$의 양변을 연쇄법칙으로 미분하여 $$f'(f^{-1}(b))\cdot(f^{-1})'(b) = 1$$을 얻고, $$f'(a) \neq 0$$이므로 공식이 따른다. ($$f^{-1}$$의 미분가능성 자체는 차분몫 $$\frac{f^{-1}(y)-f^{-1}(b)}{y-b}$$를 $$u = f^{-1}(y)$$로 치환하여 $$f$$의 차분몫의 역수로 보고, $$f^{-1}$$의 연속성을 이용하면 확인된다.)

</details>

예를 들어 $$f(x) = e^x$$의 역함수 $$f^{-1}(y) = \ln y$$에 대하여, $$f'(x) = e^x$$이므로 $$(\ln y)' = 1/e^{\ln y} = 1/y$$이다. 같은 방법으로 역삼각함수의 도함수, 가령 $$(\arcsin x)' = 1/\sqrt{1 - x^2}$$도 얻는다.

이로써 다항·유리·삼각·지수·로그함수와 그 합성으로 이루어진 거의 모든 함수를 미분할 수 있다. 이렇게 얻은 도함수가 함수의 증감·극값·그래프 모양에 어떤 정보를 주는지는 [§평균값 정리](/ko/math/calculus/mean_value_theorem)와 [§도함수의 응용](/ko/math/calculus/applications_of_derivatives)에서 다루고, 함수를 다항식으로 근사하는 데 도함수를 거듭 사용하는 방법은 [§테일러 정리](/ko/math/calculus/taylor_theorem)에서 다룬다.
