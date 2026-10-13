---
title: "미분"
description: "도함수를 극한으로 정의하고 미분가능성이 연속성을 함의함을 보인다. 분모가 0이 되는 점을 피하는 연쇄법칙의 엄밀한 증명, 도함수가 불연속일 수 있는 예, 극값에서 도함수가 0이라는 조건, 도함수의 중간값 성질(Darboux 정리), 역함수의 미분을 다룬다."
excerpt: "도함수의 정의, 연쇄법칙의 엄밀한 증명, Darboux 정리, 역함수의 미분"

categories: [Math / Analysis]
permalink: /ko/math/analysis/differentiation
sidebar: 
    nav: "analysis-ko"

date: 2026-06-02
weight: 14

published: false

---

[\[미적분학\] §미분과 도함수, ⁋정의 1](/ko/math/calculus/derivatives#def1){: data-lid="uwerr" }에서 다룬 미분을 이 글에서는 실수의 완비성과 연속함수의 이론 위에서 다시 세운다. 연쇄법칙의 흔한 증명이 어디서 틀리는지, 도함수가 어떤 성질을 가지고 어떤 성질을 갖지 못하는지가 주된 내용이다.

## 도함수의 정의

::: 정의 1
$I$를 구간, $f : I \to \mathbb{R}$, $a \in I$라 하자. 극한

$$f'(a) = \lim_{x \to a} \frac{f(x) - f(a)}{x - a}$$

이 존재할 때 $f$가 $a$에서 *미분가능*하다고 하고, 이 극한을 $f$의 $a$에서의 *derivative*라 한다. $f$가 $I$의 모든 점에서 미분가능하면 $a \mapsto f'(a)$로 주어지는 함수 $f' : I \to \mathbb{R}$를 $f$의 *도함수*라 한다.
:::

극한은 $x \in I \setminus \{a\}$에 대해 취하므로, $a$가 $I$의 끝점이면 $f'(a)$는 자동으로 단측 derivative가 된다. 아래에서 닫힌구간 $[a, b]$ 위의 미분가능성은 이 뜻으로 읽는다.

::: 명제 2
$f$가 $a$에서 미분가능하면 $a$에서 연속이다.
:::

::: 증명
$x \neq a$에 대해 $f(x) - f(a) = \bigl(f(x) - f(a)\bigr)/(x - a) \cdot (x - a)$이고, $x \to a$일 때 우변은 $f'(a) \cdot 0 = 0$으로 수렴한다. 따라서 $f(x) \to f(a)$이다.
:::

역은 성립하지 않는다. $f(x) = \lvert x\rvert$는 $0$에서 연속이지만, $x > 0$에서 difference quotient가 $1$, $x < 0$에서 $-1$이므로 $x \to 0$에서 극한이 존재하지 않는다.

## 도함수가 연속이 아닌 함수

미분가능한 함수의 도함수가 연속일 필요는 없다.

::: 예시 3
$f(x) = x^2 \sin(1/x)$ ($x \neq 0$), $f(0) = 0$으로 정의하자. $0$에서는

$$\left\lvert\frac{f(x) - f(0)}{x - 0}\right\rvert = \lvert x \sin(1/x)\rvert \leq \lvert x\rvert \to 0$$

이므로 $f'(0) = 0$이다. $x \neq 0$에서는 [\[미적분학\] §미분법, ⁋명제 3](/ko/math/calculus/differentiation_rules#prop3){: data-lid="jvlm3" }과 [\[미적분학\] §미분법, ⁋정리 4](/ko/math/calculus/differentiation_rules#thm4){: data-lid="zh5i3" }에 의하여

$$f'(x) = 2x \sin\frac{1}{x} - \cos\frac{1}{x}$$

이다. 따라서 $f$는 $\mathbb{R}$ 전체에서 미분가능하다. 그런데 $x_n = 1/(2\pi n)$이면 $f'(x_n) = -1$이고 $y_n = 1/((2n+1)\pi)$이면 $f'(y_n) = 1$이다. 두 수열 모두 $0$으로 수렴하지만 $f'$의 값은 서로 다른 수로 가므로 [§함수의 극한과 연속, ⁋정리 2](/ko/math/analysis/limits_and_continuity#thm2){: data-lid="k3r36" }에 의하여 $x \to 0$에서 $f'(x)$의 극한이 존재하지 않고, 특히 $f'$는 $0$에서 연속이 아니다.
:::

이 함수는 한 가지 사실을 더 보여 준다. $f(1/(n\pi)) = 0$이므로 $f$는 $f(0) = 0$과 같은 값을 $0$의 어느 근방에서도 $0$이 아닌 점에서 취한다. 다음 절의 연쇄법칙 증명은 바로 이 현상 때문에 흔한 형태로는 틀린다.

## 연쇄법칙

::: 정리 4 (연쇄법칙)
$I$, $J$를 구간, $f : I \to \mathbb{R}$, $f(I) \subseteq J$, $g : J \to \mathbb{R}$라 하자. $f$가 $a \in I$에서, $g$가 $b = f(a)$에서 미분가능하면 $g \circ f$는 $a$에서 미분가능하고

$$(g \circ f)'(a) = g'(f(a)) f'(a)$$

이다.
:::

흔한 증명은 $x \neq a$에서

$$\frac{g(f(x)) - g(f(a))}{x - a} = \frac{g(f(x)) - g(f(a))}{f(x) - f(a)} \cdot \frac{f(x) - f(a)}{x - a}$$

로 쓰고 두 인수의 극한을 따로 취한다. 이 식은 $f(x) \neq f(a)$를 요구하는데, $a$에 가까운 $x \neq a$에서 $f(x) = f(a)$가 되는 점이 있으면 정의되지 않는다. [예시 3](#ex3){: data-lid="7mj5s" }의 $f$와 $a = 0$이 그런 경우이고, $f$가 상수함수인 경우도 마찬가지이다. 증명을 고치는 방법은 첫째 인수를 분모가 $0$이어도 의미가 있는 형태로 바꾸는 것이다.

::: 증명
$J$ 위에서 함수 $h$를

$$h(y) = \frac{g(y) - g(b)}{y - b} \quad (y \neq b), \qquad h(b) = g'(b)$$

로 정의한다. $g$가 $b$에서 미분가능하다는 것이 곧 $h$가 $b$에서 연속이라는 것이다. 모든 $y \in J$에 대해 $g(y) - g(b) = h(y)(y - b)$가 성립한다. $y = b$이면 양변이 $0$이기 때문이다. 여기에 $y = f(x)$를 대입하면 모든 $x \in I$에 대해

$$g(f(x)) - g(f(a)) = h(f(x)) \bigl(f(x) - f(a)\bigr)$$

이고, $f(x) = f(a)$인 점에서도 양변이 모두 $0$이므로 식이 성립한다. $x \neq a$이면

$$\frac{g(f(x)) - g(f(a))}{x - a} = h(f(x)) \cdot \frac{f(x) - f(a)}{x - a}$$

이다. [명제 2](#prop2){: data-lid="v305w" }에 의하여 $f$는 $a$에서 연속이고 $h$는 $b = f(a)$에서 연속이므로 [§함수의 극한과 연속, ⁋명제 6](/ko/math/analysis/limits_and_continuity#prop6){: data-lid="mkcvc" }에 의하여 $h \circ f$는 $a$에서 연속이다. 따라서 $x \to a$일 때 우변은 $h(b) f'(a) = g'(f(a)) f'(a)$로 수렴한다.
:::

## 극값과 Darboux 정리

::: 명제 5
$f : I \to \mathbb{R}$가 $I$의 내점 $c$에서 극대 또는 극소이고 $c$에서 미분가능하면 $f'(c) = 0$이다.
:::

::: 증명
$c$에서 극대라 하자. 즉 $c$의 어떤 근방에서 $f(x) \leq f(c)$이다. 이 근방에서 $x > c$이면 $(f(x) - f(c))/(x - c) \leq 0$이고 $x < c$이면 $(f(x) - f(c))/(x - c) \geq 0$이다. $c$가 내점이므로 두 방향 모두에서 $x \to c$를 취할 수 있고, 극한 $f'(c)$는 $\leq 0$이면서 $\geq 0$이다. 극소인 경우는 $-f$에 적용하면 된다.
:::

세 가지 점에 주의해야 한다. 역은 성립하지 않는다. $f(x) = x^3$은 $f'(0) = 0$이지만 $0$은 극값이 아니다. 내점이라는 가정이 필요하다. $[0, 1]$ 위의 $f(x) = x$는 끝점 $1$에서 최대이지만 $f'(1) = 1$이다. 미분가능성도 필요하다. $\lvert x\rvert$는 $0$에서 극소이지만 도함수가 존재하지 않는다.

미분가능한 함수의 도함수는 연속일 필요가 없지만, 연속함수가 갖는 중간값 성질은 그대로 갖는다.

::: 정리 6 (Darboux 정리)
$f$가 $[a, b]$에서 미분가능하고 $f'(a) \neq f'(b)$라 하자. $\lambda$가 $f'(a)$와 $f'(b)$ 사이의 수이면 $f'(c) = \lambda$인 $c \in (a, b)$가 존재한다.
:::

::: 증명
$f'(a) < \lambda < f'(b)$인 경우를 보이면 충분하다. 반대 부등식의 경우는 $-f$와 $-\lambda$에 적용하면 된다. $g(x) = f(x) - \lambda x$라 하면 $g$는 $[a, b]$에서 미분가능하고 $g'(a) < 0 < g'(b)$이다. $g$는 연속이므로 [§연속함수의 성질, ⁋따름정리 2](/ko/math/analysis/continuous_functions#cor2){: data-lid="ldwcj" }에 의하여 $[a, b]$에서 최솟값을 갖는다. 최솟값을 취하는 점 $c$가 $a$나 $b$가 아님을 보이자.

$g'(a) < 0$이므로 [§함수의 극한과 연속, ⁋정의 1](/ko/math/analysis/limits_and_continuity#def1){: data-lid="hkty9" }에 의하여 어떤 $\delta > 0$이 있어 $a < x < a + \delta$에서 $(g(x) - g(a))/(x - a) < 0$이다. 이때 $x - a > 0$이므로 $g(x) < g(a)$이고, $g(a)$는 최솟값이 될 수 없다. 같은 방식으로 $g'(b) > 0$이므로 $b - \delta < x < b$에서 $(g(x) - g(b))/(x - b) > 0$인데 $x - b < 0$이므로 $g(x) < g(b)$이고, $g(b)$도 최솟값이 아니다.

따라서 $c \in (a, b)$이고, $c$는 $g$의 내점 극소이므로 [명제 5](#prop5){: data-lid="kpx26" }에 의하여 $g'(c) = f'(c) - \lambda = 0$이다.
:::

가정에 $f'$의 연속성이 없다는 점이 요점이다. 증명은 최대·최소 정리를 $g$에 적용했을 뿐 $f'$ 자체에는 중간값 정리를 쓰지 않는다. 다음 따름정리는 도함수가 가질 수 있는 불연속의 형태를 제한한다.

::: 따름정리 7
$f$가 구간 $I$에서 미분가능하고 $c \in I$라 하자. 단측극한 $\lim_{x \to c+} f'(x)$가 (유한한 값으로) 존재하면 그 값은 $f'(c)$이다. $x \to c-$인 경우도 같다.
:::

::: 증명
$L = \lim_{x \to c+} f'(x) \neq f'(c)$라 가정하고, $L > f'(c)$인 경우를 보자. $f'(c) < \lambda < L$인 $\lambda$를 잡으면 어떤 $\delta > 0$이 있어 $c < x < c + \delta$에서 $f'(x) > \lambda$이다. 이런 $x$ 하나를 고르면 $[c, x]$에서 $f'(c) < \lambda < f'(x)$이므로 [정리 6](#thm6){: data-lid="8hrp9" }에 의하여 $f'(t) = \lambda$인 $t \in (c, x)$가 있다. 그런데 $t$는 $(c, c + \delta)$에 속하므로 $f'(t) > \lambda$이어야 하여 모순이다. $L < f'(c)$인 경우와 $x \to c-$인 경우도 같은 논증이다.
:::

따라서 도함수는 jump 불연속을 가질 수 없고, 예를 들어 부호함수 $\sgn(x)$는 어떤 구간 위에서도 도함수가 될 수 없다. 도함수의 불연속은 [예시 3](#ex3){: data-lid="g2b0e" }의 $\cos(1/x)$처럼 단측극한이 존재하지 않는 방식으로만 일어난다.

## 역함수의 미분

::: 정리 8 (역함수의 미분)
$I$를 구간, $f : I \to \mathbb{R}$를 연속이고 strictly monotone인 함수라 하고 $J = f(I)$, $g = f^{-1} : J \to I$라 하자. $f$가 $a \in I$에서 미분가능하고 $f'(a) \neq 0$이면 $g$는 $b = f(a)$에서 미분가능하고

$$g'(b) = \frac{1}{f'(a)}$$

이다.
:::

::: 증명
$f$는 strictly increasing이라 하자. decreasing인 경우는 $-f$에 적용하면 된다. [§연결성과 중간값 정리, ⁋따름정리 4](/ko/math/analysis/connectedness#cor4){: data-lid="mumko" }에 의하여 $J$는 구간이고, $g$도 strictly increasing이다.

먼저 $g$가 $b$에서 연속임을 보인다. $\varepsilon > 0$이 주어졌다고 하자. $I$에서 $a - \varepsilon < x_1 < a < x_2 < a + \varepsilon$인 점 $x_1, x_2$를 잡는다. 단, $a$가 $I$의 끝점이면 존재하는 쪽의 점만 잡는다. $f$가 strictly increasing이므로 $f(x_1) < b < f(x_2)$이고, $\delta = \min\{b - f(x_1), f(x_2) - b\}$로 두자. $y \in J$, $\lvert y - b\rvert < \delta$이면 $f(x_1) < y < f(x_2)$이고, $g$가 increasing이므로 $x_1 < g(y) < x_2$, 곧 $\lvert g(y) - a\rvert < \varepsilon$이다. 여기서 $\delta$를 두 거리의 최솟값으로 잡은 것은 $y$가 $f(x_1)$과 $f(x_2)$ 사이에 머물도록 하기 위해서이다.

이제 $y \in J \setminus \{b\}$에 대해 $x = g(y)$라 하면 $x \neq a$이고 $y = f(x)$이므로

$$\frac{g(y) - g(b)}{y - b} = \frac{x - a}{f(x) - f(a)} = \left(\frac{f(x) - f(a)}{x - a}\right)^{-1}$$

이다. $f$가 단사이므로 우변의 괄호 안은 $x \neq a$에서 $0$이 아니다. $y \to b$이면 $g$의 연속성에 의하여 $x = g(y) \to a$이고 $x \neq a$이므로, 괄호 안은 $f'(a) \neq 0$으로 수렴한다. 따라서 좌변은 $1/f'(a)$로 수렴한다.
:::

가정 $f'(a) \neq 0$은 필요하다. $f(x) = x^3$은 $\mathbb{R}$ 위에서 연속이고 strictly increasing이며 $f'(0) = 0$이다. 이때 역함수 $g(y) = y^{1/3}$의 $0$에서의 difference quotient $y^{-2/3}$는 $y \to 0$에서 발산하므로 $g$는 $0$에서 미분가능하지 않다. 일반적으로도 $f'(a) = 0$이면 $g$가 $b$에서 미분가능할 수 없다. 미분가능하다면 [정리 4](#thm4){: data-lid="ewlqn" }에 의하여 $g(f(x)) = x$의 $a$에서의 derivative로 $g'(b) f'(a) = 1$을 얻게 되어 $f'(a) = 0$과 모순이기 때문이다.

---

**참고문헌**

**[Rud]** W. Rudin, *Principles of mathematical analysis*, 3rd ed., McGraw-Hill, 1976.
