---
title: "미분법"
description: "멱급수의 항별 미분으로 지수함수의 도함수를 얻고, 삼각함수의 도함수와 곱·연쇄법칙, 몫의 미분법, 역함수의 미분법을 정리한다. 이로써 초등함수로 이루어진 함수를 체계적으로 미분할 수 있게 된다."
excerpt: "멱급수의 항별 미분, 초등함수의 도함수, 곱·몫·연쇄법칙"

categories: [Math / Calculus]
permalink: /ko/math/calculus/differentiation_rules
sidebar: 
    nav: "calculus-ko"

date: 2026-06-22
weight: 7


---

우리는 [§미분과 도함수](/ko/math/calculus/derivatives)에서 미분의 정의와 기본적인 성질들을 다루었다. 이번 글에서 우리는 구체적인 함수에 대한 미분들과, 일반적인 함수들에 대해 적용되는 미분규칙들을 다룬다.

## 멱급수의 항별 미분

우선 임의의 자연수 $$n$$에 대하여, $$x^n$$의 점 $$a$$에서의 미분은 

$$\lim_{h\rightarrow 0}\frac{(a+h)^n-a^n}{h}=\lim_{h\rightarrow 0}\frac{na^{n-1}h+\ldots}{h}=na^{n-1}$$

으로 주어지는 것을 확인할 수 있으며, 비슷하게 음의 정수 $$n = -m$$에 대해서도 평균변화율을 통분하면

$$\frac{(a+h)^{-m} - a^{-m}}{h} = -\frac{(a+h)^m - a^m}{h}\cdot\frac{1}{(a+h)^ma^m}$$

이므로, 결국 모든 정수 $$n$$에 대해 $$(x^n)' = n x^{n-1}$$이 성립한다.

한편, 선형성에 의해 다항식은 항별로 미분되므로 이는 임의의 다항함수에 대한 미분규칙 또한 준다. 그러나 일반적으로 <em-ko>무한</em-ko>합에서 미분을 항마다 분배하는 것은 자명하지 않은데, 다음 명제는 멱급수에 대해서는 이것이 허용됨을 보장한다.

<div class="proposition" markdown="1">

<ins id="prop1">**명제 1 (멱급수의 항별 미분)**</ins> 멱급수 $$f(x) = \sum_{n=0}^\infty c_n x^n$$이 수렴반경 $$R > 0$$을 가지면, $$f$$는 $$\lvert x\rvert < R$$에서 미분가능하고

$$f'(x) = \sum_{n=1}^\infty n\,c_n x^{n-1}$$

이며, 이 급수의 수렴반경도 $$R$$이다.

</div>

우변의 급수의 수렴반경이 $$R$$이 된다는 것 자체는 $$n\rightarrow \infty$$일 때 $$n^{1/n}$$이 $$1$$로 수렴한다는 것으로부터 얻어지지만, 이것이 실제로 $$f'(x)$$와 같다는 것을 엄밀히 정당화하기에는 우리의 도구가 부족하므로 이는 받아들이고 넘어가기로 한다. 

## 삼각함수와 지수함수의 도함수

본격적으로 미분규칙들을 살펴보기 전에, 우리는 다양한 함수들의 도함수를 유도한다. 

우선 지수함수는 [§멱급수, ⁋예시 3](/ko/math/calculus/power_series#ex3)에서 $$e^x = \sum_{n\geq 0} x^n/n!$$로 정의하였다. 이제 [명제 1](#prop1)을 적용하면 그 미분은 항별 미분의 합

$$(e^x)' = \sum_{n=1}^\infty n\,\frac{x^{n-1}}{n!} = \sum_{n=1}^\infty \frac{x^{n-1}}{(n-1)!} = \sum_{m=0}^\infty \frac{x^m}{m!} = e^x$$

이므로, 지수함수는 미분에 대해 불변이다. 이는, 고등학교에서는 다음의 극한

$$\lim_{h\to 0}(e^h-1)/h = 1$$

로부터 얻어지는 결과였다.

삼각함수 또한 머지않아 멱급수의 형태로 쓸 것이지만, 우선은 고등학교때와 마찬가지로 두 극한

$$\lim_{h \to 0} \frac{\sin h}{h} = 1, \qquad \lim_{h \to 0} \frac{1 - \cos h}{h} = 0$$

을 사용하여 얻어내기로 한다. 

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2 (삼각함수의 도함수)**</ins> 모든 점에서 $$(\sin x)' = \cos x$$이고 $$(\cos x)' = -\sin x$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

덧셈정리 $$\sin(x+h) = \sin x\cos h + \cos x \sin h$$로 평균변화율을 가르면

$$\frac{\sin(x+h) - \sin x}{h} = \sin x \cdot \frac{\cos h - 1}{h} + \cos x \cdot \frac{\sin h}{h}$$

이고, $$h \to 0$$일 때 위 두 극한에 의해 $$\sin x \cdot 0 + \cos x \cdot 1 = \cos x$$로 수렴한다. $$\cos x$$의 도함수도 같은 방법으로 얻는다.

</details>

## 여러가지 미분법

이제 우리는 일반적인 형태에 적용되는 미분규칙들을 정의한다. [§미분과 도함수, ⁋명제 4](/ko/math/calculus/derivatives#prop4)에서 우리는 미분이 상수곱과 덧셈에 대해서는 잘 행동하는 것을 보았지만, 곱에 대해서는 단순히 분배되지 않는다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3 (곱의 미분법)**</ins> $$f, g$$가 $$a$$에서 미분가능하면 $$fg$$도 $$a$$에서 미분가능하고

$$(fg)'(a) = f'(a)\,g(a) + f(a)\,g'(a)$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

평균변화율에 같은 항을 더하고 빼면

$$\frac{f(a+h)g(a+h) - f(a)g(a)}{h} = \frac{f(a+h)-f(a)}{h}\,g(a+h) + f(a)\,\frac{g(a+h)-g(a)}{h}$$

이다. $$h \to 0$$일 때 첫 항의 평균변화율은 $$f'(a)$$로, $$g(a+h)$$는 $$g$$의 연속성 ([§미분과 도함수, ⁋명제 2](/ko/math/calculus/derivatives#prop2))으로 $$g(a)$$로, 둘째 항의 평균변화율은 $$g'(a)$$로 수렴하므로, [§함수의 극한, ⁋명제 5](/ko/math/calculus/functions_and_limits#prop5)에 의해 합은 $$f'(a)g(a) + f(a)g'(a)$$로 수렴한다.

</details>

가장 널리 쓰이는 규칙은 합성함수의 미분이다.

<div class="proposition" markdown="1">

<ins id="thm4">**정리 4 (연쇄법칙)**</ins> $$f$$가 $$a$$에서 미분가능하고 $$g$$가 $$b = f(a)$$에서 미분가능하면, 합성 $$g \circ f$$도 $$a$$에서 미분가능하고

$$(g \circ f)'(a) = g'(f(a))\,f'(a)$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$g$$의 미분가능성을 보조함수

$$\varphi(y) = \begin{cases} \frac{g(y) - g(b)}{y - b}, & y \neq b,\\[1mm] g'(b), & y = b \end{cases}$$

로 옮긴다. 미분가능성의 정의에 의해 $$\varphi$$는 $$b$$에서 연속이고, 모든 $$y$$에 대해 $$g(y) - g(b) = \varphi(y)(y - b)$$가 성립한다. $$y = f(a+h)$$를 대입하면

$$\frac{g(f(a+h)) - g(f(a))}{h} = \varphi(f(a+h))\,\frac{f(a+h) - f(a)}{h}$$

이고, $$h \to 0$$일 때 $$f$$의 연속성으로 $$\varphi(f(a+h)) \to \varphi(b) = g'(b)$$이며 둘째 인자는 $$f'(a)$$로 수렴하므로, 극한은 $$g'(f(a))f'(a)$$이다.

</details>

이제 몫의 미분법은 곱의 미분법과 연쇄법칙의 따름정리로 따라온다.

<div class="proposition" markdown="1">

<ins id="cor5">**따름정리 5 (몫의 미분법)**</ins> $$f, g$$가 $$a$$에서 미분가능하고 $$g(a) \neq 0$$이면 $$f/g$$도 $$a$$에서 미분가능하고

$$\left(\frac{f}{g}\right)'(a) = \frac{f'(a)\,g(a) - f(a)\,g'(a)}{g(a)^2}$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

함수 $$h(t)=1/t$$로 정의하면 $$1/g =h \circ g$$이고, 정수 거듭제곱의 미분으로 $$h'(t)=-1/t^2$$이므로, [정리 4](#thm4)에 의해 $$(1/g)'(a) = -g(a)^{-2}g'(a)$$이다. 이제 $$f/g = f\cdot(1/g)$$에 곱의 미분법을 적용하면

$$\left(\frac{f}{g}\right)'(a) = \frac{f'(a)}{g(a)} - \frac{f(a)g'(a)}{g(a)^2} = \frac{f'(a)g(a) - f(a)g'(a)}{g(a)^2}$$

을 얻는다.

</details>

가령 $$\tan x = \sin x/\cos x$$에서 $$(\tan x)' = (\cos^2 x + \sin^2 x)/\cos^2 x = \sec^2 x$$이고, 같은 방법으로 $$(\cot x)' = -\csc^2 x$$이다.

마지막으로, 함수가 단조이면 그 역함수의 도함수도 따로 계산할 필요 없이 곧바로 얻어진다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6 (역함수의 미분)**</ins> $$f$$가 한 구간에서 연속인 단조함수로 역함수 $$f^{-1}$$를 가지고, $$f$$가 $$a$$에서 미분가능하며 $$f'(a) \neq 0$$이라 하자. 그러면 $$f^{-1}$$은 $$b = f(a)$$에서 미분가능하고

$$(f^{-1})'(b) = \frac{1}{f'(a)} = \frac{1}{f'(f^{-1}(b))}$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$f^{-1}$$이 $$b$$에서 미분가능함을 받아들이면, 항등식 $$f(f^{-1}(y)) = y$$의 양변을 연쇄법칙으로 미분하여 $$f'(f^{-1}(b))\cdot(f^{-1})'(b) = 1$$을 얻고, $$f'(a) \neq 0$$이므로 증명이 완료된다.

</details>

이로써 우리는 앞에서 살펴본 함수들의 역함수에 대한 미분 또한 진행할 수 있다. 가령, $$e^x$$의 역함수 $$\ln$$에 대해 $$(e^x)' = e^x$$이므로 $$(\ln y)' = 1/e^{\ln y} = 1/y$$이고, $$\sin$$을 $$(-\pi/2, \pi/2)$$로 제한한 역함수 $$\arcsin$$에 대해서는 $$f'(x) = \cos x = \sqrt{1 - \sin^2 x} > 0$$이므로

$$(\arcsin y)' = \frac{1}{\sqrt{1 - y^2}} \qquad (\lvert y\rvert < 1)$$

이며, 같은 방식으로 $$(\arctan y)' = 1/(1 + y^2)$$이다.

한편 지금까지의 규칙으로 도함수를 구하고 나면 그 도함수가 다시 연속인지 물을 수 있는데, 어디서나 미분가능한 함수조차 도함수가 불연속일 수 있다.

<div class="example" markdown="1">

<ins id="ex7">**예시 7 (미분가능하지만 $$C^1$$급이 아닌 함수)**</ins> 함수

$$f(x) = \begin{cases} x^2 \sin(1/x) & (x \neq 0) \\ 0 & (x = 0) \end{cases}$$

는 모든 점에서 미분가능하다. $$x \neq 0$$에서는 곱의 미분법과 연쇄법칙으로 $$f'(x) = 2x\sin(1/x) - \cos(1/x)$$이고, $$0$$에서는 평균변화율이 $$x\sin(1/x) \to 0$$이므로 $$f'(0) = 0$$이다. 그런데 $$x \to 0$$일 때 $$2x\sin(1/x) \to 0$$이지만 $$\cos(1/x)$$는 $$[-1, 1]$$ 사이를 무한히 진동하여 극한을 갖지 않으므로, $$f'$$은 $$0$$에서 불연속이다. 즉 $$f$$는 어디서나 미분가능하지만 도함수가 연속이 아니어서 ([§미분과 도함수, ⁋정의 5](/ko/math/calculus/derivatives#def5)의) $$C^1$$급이 아니다.

</div>

그럼에도 도함수가 아무 모양으로나 불연속일 수는 없다. 도함수는 연속이 아니더라도 임의의 중간값을 반드시 취하므로(*Darboux 정리*) 점프 불연속을 가질 수 없으며, [예시 7](#ex7)에서 나타난 불연속도 점프가 아니라 진동에 의한 것이다.

## 미분법의 응용

마지막으로 지금까지 살펴본 규칙들을 적용하는 법을 살펴보며 이 글을 마친다. 먼저, [명제 1](#prop1)은, 우리가 멱급수를 도입한 이유와는 다소 주객이 전도된 방향이지만, 급수의 값을 구할 때 사용할 수 있다. 

<div class="example" markdown="1">

<ins id="ex8">**예시 8 (무한급수의 합)**</ins> 기하급수 ([§무한급수, ⁋예시 2](/ko/math/calculus/series#ex2))

$$\frac{1}{1-x} = \sum_{n=0}^\infty x^n \qquad (\lvert x\rvert < 1)$$

의 양변을 미분하자. 좌변은 연쇄법칙으로 

$$\left(\frac{1}{1-x}\right)' = 1/(1-x)^2$$

이고, 우변은 [명제 1](#prop1)을 적용하면 $$\sum_{n\geq 1} n x^{n-1}$$이므로

$$\sum_{n=1}^\infty n x^{n-1} = \frac{1}{(1-x)^2} \qquad (\lvert x\rvert < 1)$$

이고, 양변에 $$x$$를 곱하면

$$\sum_{n\geq 1} n x^n = \frac{x}{(1-x)^2}$$

를 얻는다. 가령 $$x = 1/2$$를 대입하면, 우리는 급수의 합 $$\sum_{n\geq 1} n/2^n = 2$$도 계산할 수 있다.

</div>

두 번째 응용은 미적분학이라는 이 카테고리에 조금 더 부합하는 결과로, 실제로 주어진 함수를 미분하는 규칙을 알려준다.

<div class="example" markdown="1">

<ins id="ex9">**예시 9 (여러가지 미분법)**</ins> 방정식이 $$y$$를 $$x$$의 함수로 정해진 경우, $$y'$$를 구하기 위해 $$y=...$$ 형태로 명시적인 식을 구하는 것은 비효율적이거나, 그러한 형태를 취했을 때 깔끔한 미분이 나오지 않는 경우가 많다. 이런 상황에서 $$y$$를 $$x$$의 함수로 보고 양변을 미분한 뒤 $$y'$$에 대해 푸는 것을 *음함수 미분법<sub>implicit differentiation</sub>*이라 한다. 가령, 단위원 $$x^2 + y^2 = 1$$에서 양변을 미분하면 

$$2x + 2y\,y' = 0$$

이므로, $$y' = -x/y$$를 얻고, 따라서 주어진 점 $$(x_0,y_0)$$에서의 접선의 기울기를 구할 수 있다.

지수에 변수가 있는 함수는 양변에 로그를 취한 뒤 미분하는 *로그 미분법<sub>logarithmic differentiation</sub>*이 편하다. 예를 들어 $$y = x^x$$ ($$x > 0$$) 에서 $$\ln y = x\ln x$$의 양변을 미분하면, $$(\ln y)' = y'/y$$와 곱의 미분법으로

$$\frac{y'}{y} = \ln x + 1 \quad\Longrightarrow\quad y' = x^x(\ln x + 1)$$

이다.

</div>
