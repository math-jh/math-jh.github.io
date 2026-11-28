---
title: "미분법"
description: "멱급수의 항별 미분으로 지수함수의 도함수를 얻고, 삼각함수의 도함수와 곱·연쇄법칙, 몫의 미분법, 역함수의 미분법을 정리한다. 이로써 초등함수로 이루어진 함수를 체계적으로 미분할 수 있게 된다."
excerpt: "멱급수의 항별 미분, 초등함수의 도함수, 곱의 미분법, 몫의 미분법, 연쇄법칙"

categories: [Math / Calculus]
permalink: /ko/math/calculus/differentiation_rules
sidebar: 
    nav: "calculus-ko"

date: 2026-06-22
weight: 7
revising: true

---

우리는 [§미분과 도함수](/ko/math/calculus/derivatives){: data-lid="65feo" }에서 미분의 정의와 기본적인 성질들을 다루었다. 이번 글에서 우리는 구체적인 함수에 대한 미분들과, 일반적인 함수들에 대해 적용되는 미분규칙들을 다룬다.

## 멱급수의 항별 미분

우리는 [§미분과 도함수, ⁋명제 5](/ko/math/calculus/derivatives#prop5){: data-lid="4405y" } 직후에 다항함수는 항별로 미분할 수 있다는 것을 살펴보았다. 일반적으로 미분은 무한합과 잘 어울리지 <em-ko>않지만</em-ko>, 멱급수의 경우 그 수렴반경 안에서는 다음 명제에 의해 항별 미분이 가능하다.

::: 명제 1 (멱급수의 항별 미분)
멱급수 $f(x) = \sum_{n=0}^\infty c_n x^n$이 수렴반경 $R > 0$을 가지면, $f$는 $\lvert x\rvert < R$에서 미분가능하고

$$f'(x) = \sum_{n=1}^\infty n c_n x^{n-1}$$

이며, 이 급수의 수렴반경도 $R$이다.
:::

두 급수의 수렴반경이 같다는 것은 [§멱급수, ⁋정리 2](/ko/math/calculus/power_series#thm2){: data-lid="git2g" } 직전에 쓴 것과 같은 비교 논증으로 보일 수 있다.

$\lvert a\rvert<r<R$로 잡고 $\lvert a+h\rvert<r$인 $h\neq 0$을 생각하자. [§미분과 도함수, ⁋예시 2](/ko/math/calculus/derivatives#ex2){: data-lid="0gs1n" }의 인수분해를 이용하면 평균변화율을 이루는 각 항에 대해

$$\left\lvert c_n\frac{(a+h)^n-a^n}{h}\right\rvert\leq n\lvert c_n\rvert r^{n-1}$$

이다. 우변을 합한 급수는 수렴하므로, 뒤쪽 항들의 합의 절댓값을 $h$와 무관하게 원하는 만큼 작게 만들 수 있다. 앞쪽의 유한합에서는 항마다 $h\rightarrow 0$인 극한을 취할 수 있으므로, 전체 평균변화율의 극한도 각 항의 극한 $nc_na^{n-1}$을 합한 값과 같다.

## 삼각함수와 지수함수의 도함수

본격적으로 미분규칙들을 살펴보기 전에, 우리는 다양한 함수들의 도함수를 유도한다. 

우선 지수함수는 [§멱급수, ⁋예시 3](/ko/math/calculus/power_series#ex3){: data-lid="00w8x" }에서 $e^x = \sum_{n\geq 0} x^n/n!$로 정의하였다. 이제 [명제 1](#prop1){: data-lid="z8pkw" }을 적용하면 그 미분은 항별 미분의 합

$$(e^x)' = \sum_{n=1}^\infty n \frac{x^{n-1}}{n!} = \sum_{n=1}^\infty \frac{x^{n-1}}{(n-1)!} = \sum_{m=0}^\infty \frac{x^m}{m!} = e^x$$

이므로, 지수함수는 미분에 대해 불변이다. 이는, 고등학교에서는 다음의 극한

$$\lim_{h\rightarrow 0}(e^h-1)/h = 1$$

로부터 얻어지는 결과였다.

삼각함수 또한 머지않아 멱급수의 형태로 쓸 것이지만, 우선은 두 극한

$$\lim_{h \rightarrow 0} \frac{\sin h}{h} = 1, \qquad \lim_{h \rightarrow 0} \frac{1 - \cos h}{h} = 0$$

을 사용하여 얻어내기로 한다. 첫 극한은 [§함수의 극한, ⁋예시 10](/ko/math/calculus/functions_and_limits#ex10){: data-lid="gvxns" }에서 조임정리로 얻었고, 둘째 극한은 같은 예시가 세운 부등식 $\lvert 1 - \cos h\rvert \leq h^2/2$로부터 $\lvert(1 - \cos h)/h\rvert \leq \lvert h\rvert/2$가 되어 따라온다. 

::: 명제 2 (삼각함수의 도함수)
모든 점에서 $(\sin x)' = \cos x$이고 $(\cos x)' = -\sin x$이다.
:::

::: 증명
덧셈정리 $\sin(x+h) = \sin x\cos h + \cos x \sin h$로 평균변화율을 가르면

$$\frac{\sin(x+h) - \sin x}{h} = \sin x \cdot \frac{\cos h - 1}{h} + \cos x \cdot \frac{\sin h}{h}$$

이고, $h \rightarrow 0$일 때 위 두 극한에 의해 $\sin x \cdot 0 + \cos x \cdot 1 = \cos x$로 수렴한다. $\cos x$의 도함수도 같은 방법으로 얻는다.
:::

## 여러가지 미분법

이제 우리는 일반적인 형태에 적용되는 미분규칙들을 정의한다. [§미분과 도함수, ⁋명제 5](/ko/math/calculus/derivatives#prop5){: data-lid="ogd67" }에서 우리는 미분이 상수곱과 덧셈에 대해서는 잘 행동하는 것을 보았지만, 곱에 대해서는 단순히 분배되지 않는다.

::: 명제 3 (곱의 미분법)
$f, g$가 $a$에서 미분가능하면 $fg$도 $a$에서 미분가능하고

$$(fg)'(a) = f'(a) g(a) + f(a) g'(a)$$

이다.
:::

::: 증명
평균변화율에 같은 항을 더하고 빼면

$$\frac{f(a+h)g(a+h) - f(a)g(a)}{h} = \frac{f(a+h)-f(a)}{h} g(a+h) + f(a) \frac{g(a+h)-g(a)}{h}$$

이다. $h \rightarrow 0$일 때 첫 항의 평균변화율은 $f'(a)$로, $g(a+h)$는 $g$의 연속성으로 ([§미분과 도함수, ⁋명제 3](/ko/math/calculus/derivatives#prop3){: data-lid="hzft9" }) $g(a)$로, 둘째 항의 평균변화율은 $g'(a)$로 수렴하므로, [§함수의 극한, ⁋명제 5](/ko/math/calculus/functions_and_limits#prop5){: data-lid="edoso" }에 의해 합은 $f'(a)g(a) + f(a)g'(a)$로 수렴한다.
:::

가장 널리 쓰이는 규칙은 합성함수의 미분이다.

::: 정리 4 (연쇄법칙)
$f$가 $a$에서 미분가능하고 $g$가 $b = f(a)$에서 미분가능하면, 합성 $g \circ f$도 $a$에서 미분가능하고

$$(g \circ f)'(a) = g'(f(a)) f'(a)$$

이다.
:::

::: 증명
$g$의 미분가능성을 보조함수

$$\varphi(y) = \begin{cases} \frac{g(y) - g(b)}{y - b}, & y \neq b,\\[1mm] g'(b), & y = b \end{cases}$$

로 옮긴다. 미분가능성의 정의에 의해 $\varphi$는 $b$에서 연속이고, 모든 $y$에 대해 $g(y) - g(b) = \varphi(y)(y - b)$가 성립한다. $y = f(a+h)$를 대입하면

$$\frac{g(f(a+h)) - g(f(a))}{h} = \varphi(f(a+h)) \frac{f(a+h) - f(a)}{h}$$

이고, $h \rightarrow 0$일 때 $f$의 연속성으로 $\varphi(f(a+h)) \rightarrow \varphi(b) = g'(b)$이며 둘째 인자는 $f'(a)$로 수렴하므로, 극한은 $g'(f(a))f'(a)$이다.
:::

이제 몫의 미분법은 곱의 미분법과 연쇄법칙의 따름정리로 따라온다.

::: 따름정리 5 (몫의 미분법)
$f, g$가 $a$에서 미분가능하고 $g(a) \neq 0$이면 $f/g$도 $a$에서 미분가능하고

$$\left(\frac{f}{g}\right)'(a) = \frac{f'(a) g(a) - f(a) g'(a)}{g(a)^2}$$

이다.
:::

::: 증명
함수 $h(t)=1/t$로 정의하면 $1/g =h \circ g$이고, [§미분과 도함수, ⁋예시 2](/ko/math/calculus/derivatives#ex2){: data-lid="1hzrt" }에 의해 $h'(t)=-1/t^2$이다. 따라서 [정리 4](#thm4){: data-lid="xpo63" }에 의해 $(1/g)'(a) = -g(a)^{-2}g'(a)$이다. 이제 $f/g = f\cdot(1/g)$에 곱의 미분법을 적용하면

$$\left(\frac{f}{g}\right)'(a) = \frac{f'(a)}{g(a)} - \frac{f(a)g'(a)}{g(a)^2} = \frac{f'(a)g(a) - f(a)g'(a)}{g(a)^2}$$

을 얻는다.
:::

가령 $\tan x = \sin x/\cos x$에서 $(\tan x)' = (\cos^2 x + \sin^2 x)/\cos^2 x = \sec^2 x$이고, 같은 방법으로 $(\cot x)' = -\csc^2 x$이다.

마지막으로, 함수가 단조이면 그 역함수의 도함수도 따로 계산할 필요 없이 곧바로 얻어진다.

::: 명제 6 (역함수의 미분)
$f$가 한 구간에서 연속인 단조함수로 역함수 $f^{-1}$를 가지고, $f$가 $a$에서 미분가능하며 $f'(a) \neq 0$이라 하자. 그러면 $f^{-1}$은 $b = f(a)$에서 미분가능하고

$$(f^{-1})'(b) = \frac{1}{f'(a)} = \frac{1}{f'(f^{-1}(b))}$$

이다.
:::

::: 증명
$f$가 정의된 구간을 $I$, 그 image를 $J = f(I)$라 하자. $f$는 단조이면서 역함수를 가져 단사이므로 순단조이고, 따라서 [§연속함수, ⁋명제 7](/ko/math/calculus/continuity#prop7){: data-lid="t16wr" }에 의해 $f^{-1} : J \rightarrow I$는 연속이다.

이제 $y \in J$가 $y \neq b$이면 $x = f^{-1}(y)$는 단사성에 의해 $a = f^{-1}(b)$와 다르므로, $f^{-1}$의 평균변화율을

$$\frac{f^{-1}(y) - f^{-1}(b)}{y - b} = \frac{x - a}{f(x) - f(a)} = \left(\frac{f(x)-f(a)}{x-a}\right)^{-1}$$

로 고쳐 쓸 수 있다. $y \rightarrow b$일 때 $f^{-1}$의 연속성에 의해 $x \rightarrow a$이고 우변의 괄호 안은 $f'(a)$로 수렴하므로, $f'(a) \neq 0$과 [§함수의 극한, ⁋명제 5](/ko/math/calculus/functions_and_limits#prop5){: data-lid="bpd9d" }의 4에 의해 위 평균변화율은 $1/f'(a)$로 수렴한다. 즉 $f^{-1}$은 $b$에서 미분가능하고 $(f^{-1})'(b) = 1/f'(a)$이다.
:::

이로써 우리는 앞에서 살펴본 함수들의 역함수에 대한 미분 또한 진행할 수 있다. 가령, $e^x$의 역함수 $\ln$에 대해 $(e^x)' = e^x$이므로 $(\ln y)' = 1/e^{\ln y} = 1/y$이고, $\sin$을 $(-\pi/2, \pi/2)$로 제한한 역함수 $\arcsin$에 대해서는 $f'(x) = \cos x = \sqrt{1 - \sin^2 x} > 0$이므로

$$(\arcsin y)' = \frac{1}{\sqrt{1 - y^2}} \qquad (\lvert y\rvert < 1)$$

이며, 같은 방식으로 $(\arctan y)' = 1/(1 + y^2)$이다.

로그함수의 도함수를 알면 거듭제곱의 미분 공식을 임의의 실수 지수 $r$로 확장할 수 있다. $x>0$에서 $x^r=e^{r\ln x}$이므로 [정리 4](#thm4){: data-lid="9kebn" }에 의해

$$(x^r)'=e^{r\ln x}\cdot\frac{r}{x}=rx^{r-1}$$

이다.

밑이 $b>0$인 지수함수도 $b^x=e^{x\ln b}$로 쓰면 연쇄법칙으로 미분할 수 있다. $b\neq 1$이면 $x>0$에서 밑변환 공식 $\log_b x=(\ln x)/(\ln b)$로 로그함수의 도함수도 구할 수 있다. 두 결과는 각각

$$(b^x)'=b^x\ln b,\qquad (\log_b x)'=\frac{1}{x\ln b}$$

이다. 가령 $(2^x)'=2^x\ln 2$이다.

진동하는 함수에 $x$를 거듭 곱하면 원점 근방에서 진동의 폭이 줄어들어 미분가능성이 달라질 수 있다.

::: 예시 7 (진동과 미분가능성)
함수 $f$와 $g$를 $x\neq 0$에서

$$f(x)=x\sin(1/x),\qquad g(x)=x^2\sin(1/x)$$

로 두고 $f(0)=g(0)=0$으로 정의하자. [§함수의 극한, ⁋예시 11](/ko/math/calculus/functions_and_limits#ex11){: data-lid="i73q8" }에 의해 $f$는 $0$에서 연속이고, $g(x)=xf(x)$이므로 $g$도 $0$에서 연속이다. 두 함수의 $0$에서의 평균변화율은 각각

$$\frac{f(h)-f(0)}{h}=\sin(1/h),\qquad \frac{g(h)-g(0)}{h}=h\sin(1/h)$$

이다. $h\rightarrow 0$일 때 첫 식은 진동하여 극한이 없으므로 $f$는 $0$에서 미분가능하지 않다. 둘째 식은 $0$으로 수렴하므로 $g'(0)=0$이다.

$x\neq 0$에서는 곱의 미분법과 연쇄법칙으로

$$f'(x)=\sin(1/x)-\frac{\cos(1/x)}{x},\qquad g'(x)=2x\sin(1/x)-\cos(1/x)$$

이다. $x\rightarrow 0$일 때 $g'(x)$의 첫 항은 $0$으로 수렴하고 둘째 항은 진동하여 극한을 갖지 않으므로 $g'$은 $0$에서 불연속이다. 따라서 $g$는 어디서나 미분가능하고 $0$에서 도함수가 불연속이어서 [§미분과 도함수, ⁋정의 6](/ko/math/calculus/derivatives#def6){: data-lid="gd3pp" }의 $C^1$급 조건을 만족하지 않는다.
:::

*Darboux 정리*에 따르면 도함수는 두 점에서 취한 값 사이의 모든 값을 취하므로 점프 불연속을 가질 수 없다. [예시 7](#ex7){: data-lid="e0sir" }에서 $g'$의 불연속은 진동에서 비롯된다.

## 미분법의 응용

마지막으로 지금까지 살펴본 규칙들을 적용하는 법을 살펴보며 이 글을 마친다. 먼저, [명제 1](#prop1){: data-lid="ms3m5" }은, 우리가 멱급수를 도입한 이유와는 다소 주객이 전도된 방향이지만, 급수의 값을 구할 때 사용할 수 있다. 

::: 예시 8 (무한급수의 합)
기하급수 ([§무한급수, ⁋예시 2](/ko/math/calculus/series#ex2){: data-lid="we10a" })

$$\frac{1}{1-x} = \sum_{n=0}^\infty x^n \qquad (\lvert x\rvert < 1)$$

의 양변을 미분하자. 좌변은 연쇄법칙으로 

$$\left(\frac{1}{1-x}\right)' = 1/(1-x)^2$$

이고, 우변은 [명제 1](#prop1){: data-lid="p7bvq" }을 적용하면 $\sum_{n\geq 1} n x^{n-1}$이므로

$$\sum_{n=1}^\infty n x^{n-1} = \frac{1}{(1-x)^2} \qquad (\lvert x\rvert < 1)$$

이고, 양변에 $x$를 곱하면

$$\sum_{n\geq 1} n x^n = \frac{x}{(1-x)^2}$$

를 얻는다. 가령 $x = 1/2$를 대입하면, 우리는 급수의 합 $\sum_{n\geq 1} n/2^n = 2$도 계산할 수 있다.
:::

두 번째 응용은 미적분학이라는 이 카테고리에 조금 더 부합하는 결과로, 실제로 주어진 함수를 미분하는 규칙을 알려준다.

::: 예시 9 (여러가지 미분법)
방정식이 $y$를 $x$의 함수로 정해진 경우, $y'$를 구하기 위해 $y=...$ 형태로 명시적인 식을 구하는 것은 비효율적이거나, 그러한 형태를 취했을 때 깔끔한 미분이 나오지 않는 경우가 많다. 이런 상황에서 $y$를 $x$의 함수로 보고 양변을 미분한 뒤 $y'$에 대해 푸는 것을 *음함수 미분법<sub>implicit differentiation</sub>*이라 한다. 가령, 단위원 $x^2 + y^2 = 1$에서 양변을 미분하면 

$$2x + 2y y' = 0$$

이므로, $y \neq 0$인 점에서 $y' = -x/y$를 얻고, 따라서 그러한 점 $(x_0,y_0)$에서의 접선의 기울기를 구할 수 있다.

지수에 변수가 있는 함수는 양변에 로그를 취한 뒤 미분하는 *로그 미분법<sub>logarithmic differentiation</sub>*이 편하다. 예를 들어 $y = x^x$ ($x > 0$) 에서 $\ln y = x\ln x$의 양변을 미분하면, $(\ln y)' = y'/y$와 곱의 미분법으로

$$\frac{y'}{y} = \ln x + 1 \quad\implies\quad y' = x^x(\ln x + 1)$$

이다.
:::

---

**참고문헌**

**[Ste]** J. Stewart, *Calculus*, 8th ed., Cengage Learning, 2016.  
**[Kim]** 김홍종, *미적분학 1·2*, 제3개정판, 서울대학교출판문화원, 2020.
