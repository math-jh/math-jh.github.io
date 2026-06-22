---
title: "미분법"
description: "곱과 몫의 미분법, 연쇄법칙을 증명하고, 삼각함수·지수함수·로그함수의 도함수와 역함수의 미분법을 정리한다. 이로써 초등함수로 이루어진 임의의 함수를 체계적으로 미분할 수 있게 된다."
excerpt: "곱·몫의 미분법, 연쇄법칙, 초등함수의 도함수"

categories: [Math / Calculus]
permalink: /ko/math/calculus/differentiation_rules
sidebar: 
    nav: "calculus-ko"

date: 2026-06-02
weight: 7

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

$$h \to 0$$일 때 첫 항의 차분몫은 $$f'(a)$$로, $$g(a+h)$$는 $$g$$의 연속성 ([§미분과 도함수, ⁋명제 2](/ko/math/calculus/derivatives#prop2))에 의해 $$g(a)$$로 수렴한다. 둘째 항의 차분몫은 $$g'(a)$$로 수렴한다. 극한법칙 ([§함수의 극한, ⁋명제 5](/ko/math/calculus/functions_and_limits#prop5))에 의해 합은 $$f'(a)g(a) + f(a)g'(a)$$로 수렴한다.

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

예를 들어 $$f(x) = e^x$$의 역함수 $$f^{-1}(y) = \ln y$$에 대하여, $$f'(x) = e^x$$이므로

$$(\ln y)' = \frac{1}{f'(f^{-1}(y))} = \frac{1}{e^{\ln y}} = \frac{1}{y}$$

이다. 이것이 앞 절에서 미루어 두었던 자연로그의 도함수 $$(\ln x)' = 1/x$$의 유도이다. 역삼각함수의 도함수도 같은 틀로 얻는다. $$f(x) = \sin x$$를 $$(-\tfrac{\pi}{2}, \tfrac{\pi}{2})$$로 제한하면 단조증가하여 역함수 $$\arcsin$$을 가지며, $$f'(x) = \cos x = \sqrt{1 - \sin^2 x}$$가 그 구간에서 양수이므로

$$(\arcsin y)' = \frac{1}{\cos(\arcsin y)} = \frac{1}{\sqrt{1 - y^2}} \qquad (\lvert y\rvert < 1)$$

를 얻는다. 같은 방식으로 $$(\arctan y)' = 1/(1 + y^2)$$도 따른다.

## 예시와 계산

지금까지 모은 규칙들은 그 자체로는 짧지만, 합성과 곱·몫이 겹겹이 쌓인 함수에 적용할 때 비로소 위력을 드러낸다. 이 절에서는 규칙들을 결합해 구체적인 도함수를 계산하는 예를 펼쳐 보인다. 핵심은 함수를 가장 바깥 연산부터 안쪽으로 분해하여, 각 단계에 알맞은 규칙을 차례로 적용하는 것이다.

<div class="example" markdown="1">

<ins id="ex6">**예시 6 (곱과 연쇄법칙의 결합)**</ins> $$h(x) = x^2 \sin(3x)$$를 미분하자. 곱의 미분법 (명제 1) 으로 두 인자를 갈라 놓고, 둘째 인자에는 연쇄법칙 (정리 3) 을 쓴다.

$$\begin{aligned}
h'(x) &= (x^2)' \sin(3x) + x^2 \cdot \bigl(\sin(3x)\bigr)' \\
&= 2x \sin(3x) + x^2 \cdot \cos(3x)\cdot (3x)' \\
&= 2x \sin(3x) + 3x^2 \cos(3x)
\end{aligned}$$

여기서 $$\bigl(\sin(3x)\bigr)' = \cos(3x)\cdot 3$$은 바깥함수 $$\sin$$의 도함수 $$\cos$$를 안쪽함수 값 $$3x$$에서 평가한 뒤, 안쪽함수의 도함수 $$3$$을 곱한 것이다.

</div>

연쇄법칙이 여러 겹으로 중첩될 때는 가장 바깥 연산에서 시작하여 한 겹씩 벗겨 내려간다. 다음 예가 이 절차를 보여 준다.

<div class="example" markdown="1">

<ins id="ex7">**예시 7 (이중 합성)**</ins> $$h(x) = \sqrt{1 + \cos^2 x}$$를 미분하자. 바깥부터 제곱근, 제곱, 코사인의 세 겹이다.

$$\begin{aligned}
h'(x) &= \frac{1}{2\sqrt{1 + \cos^2 x}}\cdot \bigl(1 + \cos^2 x\bigr)' \\
&= \frac{1}{2\sqrt{1 + \cos^2 x}}\cdot 2\cos x \cdot (\cos x)' \\
&= \frac{1}{2\sqrt{1 + \cos^2 x}}\cdot 2\cos x \cdot (-\sin x) \\
&= \frac{-\cos x \sin x}{\sqrt{1 + \cos^2 x}}
\end{aligned}$$

각 줄은 한 겹의 연쇄법칙에 대응한다. 첫 줄에서 제곱근의 도함수, 둘째 줄에서 제곱의 도함수, 셋째 줄에서 코사인의 도함수를 차례로 끌어냈다.

</div>

<div class="example" markdown="1">

<ins id="ex8">**예시 8 (몫의 미분법)**</ins> 탄젠트의 도함수를 몫의 미분법 (명제 2) 으로 다시 확인하자. $$\tan x = \sin x / \cos x$$이므로

$$\begin{aligned}
(\tan x)' &= \frac{(\sin x)'\cos x - \sin x\,(\cos x)'}{\cos^2 x} \\
&= \frac{\cos x \cdot \cos x - \sin x \cdot(-\sin x)}{\cos^2 x} \\
&= \frac{\cos^2 x + \sin^2 x}{\cos^2 x} = \frac{1}{\cos^2 x} = \sec^2 x
\end{aligned}$$

이다. 같은 방법으로 $$\cot x = \cos x/\sin x$$에서 $$(\cot x)' = -\csc^2 x$$를 얻는다.

</div>

곱이 셋 이상일 때는 곱의 미분법을 반복 적용하면 된다. 일반적으로 $$f_1 f_2 \cdots f_n$$의 도함수는 한 인자씩만 미분한 항들의 합이다. 다음 예는 이 패턴을 로그미분법으로 정리하는 방법을 보여 준다.

<div class="example" markdown="1">

<ins id="ex9">**예시 9 (로그미분법)**</ins> 인자가 여럿이거나 지수에 변수가 있는 함수는 양변에 로그를 취한 뒤 미분하면 편하다. $$y = x^x$$ ($$x > 0$$) 를 보자. $$\ln y = x \ln x$$의 양변을 미분하면, 좌변에는 연쇄법칙으로

$$\frac{y'}{y} = (x\ln x)' = \ln x + x\cdot \frac{1}{x} = \ln x + 1$$

이 되고, 따라서

$$y' = y\,(\ln x + 1) = x^x(\ln x + 1)$$

이다. 같은 기법으로 $$y = \dfrac{(x+1)^2 \sqrt{x-1}}{x^3}$$ 같은 곱·몫·거듭제곱의 덩어리도, $$\ln y = 2\ln(x+1) + \tfrac12\ln(x-1) - 3\ln x$$를 미분해 $$y'/y$$를 구한 뒤 $$y$$를 곱하면 간단히 처리된다.

</div>

도함수 공식은 한 번 더 미분하여 고계도함수를 구하는 데도 그대로 쓰인다. 규칙을 반복 적용할 때 규칙성이 드러나는 경우가 많다.

<div class="example" markdown="1">

<ins id="ex10">**예시 10 (고계도함수)**</ins> $$f(x) = \dfrac{1}{x}= x^{-1}$$의 도함수를 거듭 구하면

$$\begin{aligned}
f'(x) &= -x^{-2}, \\
f''(x) &= 2x^{-3}, \\
f'''(x) &= -6x^{-4},
\end{aligned}$$

이고, 일반적으로 $$f^{(n)}(x) = (-1)^n n!\,x^{-(n+1)}$$임을 귀납적으로 얻는다. 한편 $$g(x) = \sin x$$는 미분할 때마다 $$\cos x, -\sin x, -\cos x, \sin x$$로 네 단계 만에 제자리로 돌아오므로 $$g^{(n)}(x) = \sin\bigl(x + \tfrac{n\pi}{2}\bigr)$$로 한꺼번에 쓸 수 있다.

</div>

마지막으로, 변수 $$x, y$$가 한 방정식으로 음함수적으로 얽혀 있을 때 연쇄법칙은 $$y$$를 $$x$$의 함수로 보고 양변을 미분하는 *음함수 미분법*으로 이어진다.

<div class="example" markdown="1">

<ins id="ex11">**예시 11 (음함수 미분법)**</ins> 단위원 $$x^2 + y^2 = 1$$ 위에서 $$y$$를 $$x$$의 함수로 보고 양변을 $$x$$로 미분하면, $$y^2$$ 항에 연쇄법칙이 적용되어

$$2x + 2y\,\frac{dy}{dx} = 0 \quad\Longrightarrow\quad \frac{dy}{dx} = -\frac{x}{y}$$

를 얻는다. 가령 점 $$\bigl(\tfrac{1}{2}, \tfrac{\sqrt 3}{2}\bigr)$$에서 접선의 기울기는 $$-\dfrac{1/2}{\sqrt 3/2} = -\dfrac{1}{\sqrt 3}$$이다. 이처럼 $$y$$를 명시적으로 풀지 않고도 도함수를 구할 수 있다는 점이 음함수 미분법의 이점이다.

</div>

이로써 다항·유리·삼각·지수·로그함수와 그 합성으로 이루어진 거의 모든 함수를 미분할 수 있다.

## 도함수의 불연속

지금까지의 규칙으로 도함수를 구하고 나면 그 도함수가 다시 연속인지 물을 수 있는데, 놀랍게도 어디서나 미분가능한 함수조차 도함수가 불연속일 수 있다.

<div class="example" markdown="1">

<ins id="ex12">**예시 12 (미분가능하지만 $$C^1$$급이 아닌 함수)**</ins> 함수

$$f(x) = \begin{cases} x^2 \sin(1/x) & (x \neq 0) \\ 0 & (x = 0) \end{cases}$$

는 모든 점에서 미분가능하다. $$x \neq 0$$에서는 곱의 미분법 (명제 1) 과 연쇄법칙 (정리 3) 으로 $$f'(x) = 2x\sin(1/x) - \cos(1/x)$$이고, $$0$$에서는 차분몫이 $$\dfrac{x^2 \sin(1/x)}{x} = x\sin(1/x) \to 0$$이므로 $$f'(0) = 0$$이다. 그런데 $$x \to 0$$일 때 $$2x\sin(1/x) \to 0$$이지만 $$\cos(1/x)$$는 $$[-1, 1]$$ 사이를 무한히 진동하여 극한을 갖지 않으므로, $$f'$$은 $$0$$에서 불연속이다. 즉 $$f$$는 어디서나 미분가능하지만 도함수가 연속이 아니어서 ([§미분과 도함수, ⁋정의 5](/ko/math/calculus/derivatives#def5)의) $$C^1$$급이 아니다.

</div>

그럼에도 도함수가 아무 모양으로나 불연속일 수는 없다. 도함수는 연속이 아니더라도 임의의 중간값을 반드시 취하므로(*Darboux 정리*) 점프 불연속을 가질 수 없으며, 예시 12에서 나타난 불연속도 점프가 아니라 진동에 의한 것이다.

## 멱급수의 항별 미분

무한급수를 항별로 미분할 수 있는지는 일반적으로 미묘하지만, 멱급수는 수렴반경 안에서 항별 미분이 가능하다.

<div class="proposition" markdown="1">

<ins id="prop13">**명제 13 (멱급수의 항별 미분)**</ins> $$f(x) = \sum_{n=0}^\infty c_n x^n$$이 수렴반경 $$R > 0$$을 가지면, $$f$$는 $$\lvert x\rvert < R$$에서 미분가능하며

$$f'(x) = \sum_{n=1}^\infty n\,c_n x^{n-1}$$

이고, 이 급수의 수렴반경도 $$R$$이다.

</div>

<div class="example" markdown="1">

<ins id="ex14">**예시 14**</ins> 기하급수 $$\dfrac{1}{1-x} = \sum_{n=0}^\infty x^n$$ ($$\lvert x\rvert < 1$$) 을 미분하면

$$\frac{1}{(1-x)^2} = \sum_{n=1}^\infty n x^{n-1}$$

이고, 양변에 $$x$$를 곱하면

$$\sum_{n=1}^\infty n x^n = \frac{x}{(1-x)^2} \qquad (\lvert x\rvert < 1)$$

이다. 가령 $$x = \tfrac12$$을 넣으면 $$\sum_{n\geq 1} n/2^n = 2$$를 얻는다.

</div>
