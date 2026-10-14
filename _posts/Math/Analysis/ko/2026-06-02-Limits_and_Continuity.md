---
title: "함수의 극한과 연속"
description: "거리공간 사이의 함수에 대하여 극한과 연속을 ε-δ로 정의하고, 수열판정과 열린집합의 preimage를 통한 동치 조건을 증명한다. 합성과 사칙연산의 연속성, 불연속의 분류, Dirichlet 함수와 Thomae 함수, 단조함수의 불연속점이 가산임을 다룬다."
excerpt: "ε-δ 극한, 수열판정, 연속의 동치 정의, 불연속의 분류와 Thomae 함수"

categories: [Math / Analysis]
permalink: /ko/math/analysis/limits_and_continuity
sidebar: 
    nav: "analysis-ko"

date: 2026-06-02
weight: 11

published: false

---

[\[미적분학\] §함수의 극한, ⁋정의 2](/ko/math/calculus/functions_and_limits#def2){: data-lid="kf1l4" }와 [\[미적분학\] §연속함수, ⁋정의 1](/ko/math/calculus/continuity#def1){: data-lid="qcsc6" }에서 실함수의 극한과 연속을 $\varepsilon$-$\delta$로 다루었다. 이 글에서는 정의역과 공역을 [§거리공간과 열린집합·닫힌집합, ⁋정의 1](/ko/math/analysis/metric_spaces#def1){: data-lid="4solv" }의 거리공간으로 넓히고, 극한과 연속을 수열과 열린집합의 언어로 다시 쓴다. 이후 글에서 연속함수의 성질을 증명할 때 쓰는 도구는 이 세 가지 표현을 상황에 따라 바꿔 쓰는 것이다. 뒷부분에서는 실함수의 불연속점이 어떤 모양일 수 있는지를 Dirichlet 함수, Thomae 함수, 단조함수의 순서로 살핀다.

이 글에서 $(X, d_X)$와 $(Y, d_Y)$는 거리공간이고 $f : X \rightarrow Y$는 함수이다. $B_X(a, \delta)$는 $X$에서의 열린 공을 뜻한다.

## 함수의 극한

함수의 극한은 $x$가 $a$에 가까워질 때 $f(x)$의 행동만을 묻는 개념이므로, $f(a)$의 값이나 $f$가 $a$에서 정의되었는지와 무관해야 한다. 그래서 $x = a$를 비교에서 제외한다. 또 $a$ 가까이에 $a$ 이외의 점이 정의역에 없다면 극한이라는 말에 내용이 없으므로, $a$는 $X$의 *집적점<sub>limit point</sub>*, 곧 모든 $\delta > 0$에 대하여 $0 < d_X(x, a) < \delta$인 $x \in X$가 존재하는 점이라고 가정한다.

::: 정의 1
$a$가 $X$의 집적점이고 $L \in Y$라 하자. 임의의 $\varepsilon > 0$에 대하여 $\delta > 0$이 존재하여

$$0 < d_X(x, a) < \delta \implies d_Y(f(x), L) < \varepsilon$$

이 성립하면 $x \rightarrow a$일 때 $f(x)$는 $L$로 *수렴<sub>converge</sub>*한다고 하고, $\lim_{x \rightarrow a} f(x) = L$로 적는다.
:::

$\delta$는 $\varepsilon$뿐 아니라 점 $a$에도 의존해서 잡힌다. 또 한 $\varepsilon$에 대하여 조건을 만족하는 $\delta$가 하나 있으면 더 작은 $\delta$도 모두 조건을 만족하므로, 증명에서는 필요한 만큼 $\delta$를 줄여도 된다. 유한개의 조건을 동시에 만족시킬 때 $\delta$들의 최솟값을 잡는 것이 이 성질에 기댄 것이다.

극한을 수열로 판정하는 방법은 다음과 같다.

::: 정리 2 (수열판정)
$a$가 $X$의 집적점이고 $L \in Y$라 하자. $\lim_{x \rightarrow a} f(x) = L$인 것은, $X \setminus \{a\}$의 점으로 이루어지고 $a$로 수렴하는 모든 수열 $(x_n)$에 대하여 $f(x_n) \rightarrow L$인 것과 동치이다.
:::

::: 증명
극한이 $L$이라 하고, $x_n \in X \setminus \{a\}$이며 $x_n \rightarrow a$라 하자. $\varepsilon > 0$이 주어지면 [정의 1](#def1){: data-lid="1k3qm" }의 $\delta$를 잡는다. $x_n \rightarrow a$이므로 어떤 $N$이 있어 $n \geq N$이면 $d_X(x_n, a) < \delta$이고, $x_n \neq a$이므로 $0 < d_X(x_n, a) < \delta$이다. 따라서 $n \geq N$이면 $d_Y(f(x_n), L) < \varepsilon$이다.

역으로 $\lim_{x \rightarrow a} f(x) = L$이 아니라 하자. 그러면 어떤 $\varepsilon > 0$에 대하여, 모든 $\delta > 0$이 조건을 만족하지 못한다. 곧 $0 < d_X(x, a) < \delta$이면서 $d_Y(f(x), L) \geq \varepsilon$인 $x$가 있다. $\delta = 1/n$에 대하여 이러한 $x$를 $x_n$으로 잡으면 $x_n \in X \setminus \{a\}$이고 $d_X(x_n, a) < 1/n$이므로 $x_n \rightarrow a$이다. 그런데 모든 $n$에 대하여 $d_Y(f(x_n), L) \geq \varepsilon$이므로 $f(x_n)$은 $L$로 수렴하지 않는다.
:::

두 가지를 짚어 둔다. 첫째, 수열이 $a$를 값으로 갖지 않는다는 조건을 빼면 정리가 틀린다. $f(0) = 1$이고 $x \neq 0$에서 $f(x) = 0$인 함수는 $x \rightarrow 0$일 때 극한이 $0$이지만, 상수열 $x_n = 0$에서는 $f(x_n) = 1$이다. 둘째, $a$가 집적점이므로 $0 < d_X(x_n, a) < 1/n$인 점 $x_n$을 잡을 수 있고, 이는 $X \setminus \{a\}$에서 $a$로 수렴하는 수열이다. 이 수열에서 $f(x_n)$은 어떤 극한으로 수렴하더라도 [§수열의 수렴, ⁋명제 2](/ko/math/analysis/convergence_of_sequences#prop2){: data-lid="8ccad" }에 의하여 한 값으로만 수렴한다. 따라서 극한 $L$이 존재하면 유일하고, $\lim_{x \rightarrow a} f(x)$라는 표기가 성립한다.

## 연속

::: 정의 3
$a \in X$라 하자. 임의의 $\varepsilon > 0$에 대하여 $\delta > 0$이 존재하여

$$d_X(x, a) < \delta \implies d_Y(f(x), f(a)) < \varepsilon$$

이 성립하면 $f$는 $a$에서 *연속<sub>continuous</sub>*이라고 한다. $f$가 $X$의 모든 점에서 연속이면 $f$를 연속함수라 한다.
:::

[정의 1](#def1){: data-lid="3uid8" }과 달리 $x = a$를 제외하지 않으며, $a$가 집적점일 필요도 없다. $a$가 $X$의 isolated point이면 $\delta$를 충분히 작게 잡았을 때 $d_X(x, a) < \delta$인 $x$는 $a$뿐이므로 $f$는 $a$에서 자동으로 연속이다. $a$가 집적점이면 $x = a$에서 부등식은 $0 < \varepsilon$이 되어 항상 성립하므로, $f$가 $a$에서 연속인 것은 $\lim_{x \rightarrow a} f(x) = f(a)$인 것과 동치이다.

연속은 정의역에 의존한다. $x \mapsto 1/x$는 $\mathbb{R} \setminus \{0\}$에서 연속함수이지만, $0$을 포함하는 어떤 정의역으로 확장해도 $0$에서는 연속이 아니다. 이 함수가 $a > 0$에서 연속임을 보면서 $\delta$를 잡는 방법을 확인한다. $x > 0$에 대하여

$$\left\lvert \frac{1}{x} - \frac{1}{a} \right\rvert = \frac{\lvert x - a\rvert}{x a}$$

이고, 분모의 $x$가 $0$ 가까이로 내려가지 않도록 $\lvert x - a\rvert < a/2$로 제한하면 $x > a/2$이므로 우변은 $2\lvert x - a\rvert/a^2$보다 작다. 따라서 $\delta = \min\{a/2, \varepsilon a^2/2\}$로 두면 $\lvert x - a\rvert < \delta$일 때 좌변이 $\varepsilon$보다 작다. 이처럼 $\delta$는 먼저 분모를 통제하는 상한을 정하고, 남은 인수를 $\varepsilon$ 이하로 만드는 상한을 더해 둘의 최솟값으로 잡는다. 또한 $\delta$가 $a$에 의존하며 $a \rightarrow 0$일 때 $0$으로 가는 것을 볼 수 있다.

다음 정리는 연속을 점열과 열린집합으로 나타낸다.

::: 정리 4 (연속의 동치 조건)
$a \in X$에 대하여 다음 세 조건은 서로 동치이다.

(a) $f$가 $a$에서 연속이다.

(b) $a$로 수렴하는 모든 수열 $(x_n)$에 대하여 $f(x_n) \rightarrow f(a)$이다.

(c) $f(a)$를 포함하는 $Y$의 모든 열린집합 $V$에 대하여, $a$를 포함하는 $X$의 열린집합 $U$가 존재하여 $f(U) \subseteq V$이다.
:::

::: 증명
(a)$\Rightarrow$(b). $x_n \rightarrow a$라 하고 $\varepsilon > 0$이 주어졌다고 하자. [정의 3](#def3){: data-lid="x5hix" }의 $\delta$를 잡으면, $x_n \rightarrow a$이므로 어떤 $N$이 있어 $n \geq N$에서 $d_X(x_n, a) < \delta$이고, 따라서 $d_Y(f(x_n), f(a)) < \varepsilon$이다.

(b)$\Rightarrow$(a). (a)가 아니라 하자. 그러면 어떤 $\varepsilon > 0$에 대하여 모든 $\delta > 0$에서 $d_X(x, a) < \delta$이면서 $d_Y(f(x), f(a)) \geq \varepsilon$인 $x$가 있다. $\delta = 1/n$에 대한 이러한 점을 $x_n$이라 하면 $x_n \rightarrow a$이지만 $f(x_n)$은 $f(a)$로 수렴하지 않으므로 (b)가 성립하지 않는다.

(a)$\Rightarrow$(c). $V$가 $f(a)$를 포함하는 [§거리공간과 열린집합·닫힌집합, ⁋정의 8](/ko/math/analysis/metric_spaces#def8){: data-lid="jz8bx" }의 열린집합이면 $B_Y(f(a), \varepsilon) \subseteq V$인 $\varepsilon > 0$이 있다. 이 $\varepsilon$에 대한 $\delta$를 잡고 $U = B_X(a, \delta)$로 두면, $U$는 열린 공이므로 [§거리공간과 열린집합·닫힌집합, ⁋명제 9](/ko/math/analysis/metric_spaces#prop9){: data-lid="k64mg" }에 의하여 열린집합이고 $x \in U$이면 $f(x) \in B_Y(f(a), \varepsilon) \subseteq V$이다.

(c)$\Rightarrow$(a). $\varepsilon > 0$이 주어지면 $V = B_Y(f(a), \varepsilon)$은 [§거리공간과 열린집합·닫힌집합, ⁋명제 9](/ko/math/analysis/metric_spaces#prop9){: data-lid="wtkx7" }에 의하여 $f(a)$를 포함하는 열린집합이다. (c)의 $U$는 $a$를 포함하는 [§거리공간과 열린집합·닫힌집합, ⁋정의 8](/ko/math/analysis/metric_spaces#def8){: data-lid="wc2ww" }의 열린집합이므로 $B_X(a, \delta) \subseteq U$인 $\delta > 0$이 있고, $d_X(x, a) < \delta$이면 $f(x) \in f(U) \subseteq V$, 곧 $d_Y(f(x), f(a)) < \varepsilon$이다.
:::

(b)에서는 [정리 2](#thm2){: data-lid="8ue6k" }와 달리 $x_n \neq a$를 요구하지 않는다. 상수열 $x_n = a$에서는 $f(x_n) = f(a)$이므로 조건이 자명하게 성립하기 때문이다.

(c)는 점 $a$에서의 연속을 거리 없이 표현한 것이다. 이를 모든 점에서 모으면 다음과 같다.

::: 명제 5 (열린집합의 preimage)
$f$가 $X$의 모든 점에서 연속인 것은, $Y$의 모든 열린집합 $V$에 대하여 preimage $f^{-1}(V)$가 $X$의 열린집합인 것과 동치이다.
:::

::: 증명
$f$가 연속이고 $V$가 $Y$의 열린집합이라 하자. 각 $a \in f^{-1}(V)$에 대하여 $f(a) \in V$이므로 [정리 4](#thm4){: data-lid="f4uj3" }의 (c)에서 $a$를 포함하는 열린집합 $U_a$가 있어 $f(U_a) \subseteq V$, 곧 $U_a \subseteq f^{-1}(V)$이다. 그러므로 $f^{-1}(V) = \bigcup_a U_a$는 열린집합의 합집합이다.

역으로 모든 열린집합의 preimage가 열려 있다 하자. $a \in X$와 $f(a)$를 포함하는 열린집합 $V$에 대하여 $U = f^{-1}(V)$는 $a$를 포함하는 열린집합이고 $f(U) \subseteq V$이므로 (c)가 성립한다.
:::

[명제 5](#prop5){: data-lid="tm5ka" }가 거리를 언급하지 않는다는 점이 [\[위상수학\] §연속함수, ⁋정의 1](/ko/math/topology/continuous_functions#def1){: data-lid="iz8wi" }에서 연속을 위상공간 사이의 함수로 일반화하는 출발점이다. 이 명제는 열린집합의 preimage에 대한 것이고, 열린집합의 image에 대한 것이 아니다. $x \mapsto x^2$은 연속이지만 열린집합 $(-1, 1)$의 image는 $[0, 1)$로 열려 있지 않다. 또한 $V$는 $Y$의 열린집합이어야 하며, 공역을 $\mathbb{R}$에서 $f$의 치역 같은 subset으로 줄이면 열린집합의 범위가 달라진다.

## 합성과 사칙연산

::: 명제 6 (합성의 연속)
$f : X \rightarrow Y$가 $a$에서 연속이고 $g : Y \rightarrow Z$가 $f(a)$에서 연속이면 $g \circ f$는 $a$에서 연속이다.
:::

::: 증명
$x_n \rightarrow a$이면 $f$의 연속성과 [정리 4](#thm4){: data-lid="fji4v" }의 (b)에서 $f(x_n) \rightarrow f(a)$이다. 다시 $g$가 $f(a)$에서 연속이므로 $g(f(x_n)) \rightarrow g(f(a))$이다. [정리 4](#thm4){: data-lid="werz7" }의 (b)$\Rightarrow$(a)에 의하여 $g \circ f$는 $a$에서 연속이다.
:::

극한에 대해서는 같은 방식이 통하지 않는다. $\lim_{x \rightarrow a} f(x) = b$이고 $\lim_{y \rightarrow b} g(y) = L$이라 해도 $\lim_{x \rightarrow a} g(f(x)) = L$이라고 할 수 없다. $f(x) = 0$ (상수)이고 $g(0) = 1$, $y \neq 0$에서 $g(y) = 0$이면 $\lim_{y \rightarrow 0} g(y) = 0$이지만 $g(f(x)) = 1$이다. $f(x) \neq b$이거나 $g$가 $b$에서 연속이어야 하며, 증명에서 $f(x_n) \neq b$가 필요했던 것과 같은 이유이다.

공역이 $\mathbb{R}$인 함수에 대해서는 연산이 보존된다.

::: 명제 7 (사칙연산의 연속)
$f, g : X \rightarrow \mathbb{R}$가 $a$에서 연속이면 $f + g$와 $fg$는 $a$에서 연속이다. $g(a) \neq 0$이면 $g$가 $0$이 되지 않는 점들의 집합 $\{x \in X \mid g(x) \neq 0\}$ 위에서 정의된 $f/g$가 $a$에서 연속이다.
:::

::: 증명
$a$로 수렴하는 수열 $(x_n)$을 임의로 잡는다. [정리 4](#thm4){: data-lid="d8bw7" }의 (b)에서 $f(x_n) \rightarrow f(a)$, $g(x_n) \rightarrow g(a)$이다. [§수열의 수렴, ⁋정리 5](/ko/math/analysis/convergence_of_sequences#thm5){: data-lid="81g3k" }에 의하여 $f(x_n) + g(x_n) \rightarrow f(a) + g(a)$이고 $f(x_n) g(x_n) \rightarrow f(a) g(a)$이다. $f/g$의 정의역에 있는 수열 $(x_n)$에 대하여 $g(x_n) \neq 0$이고 $g(a) \neq 0$이므로 $f(x_n)/g(x_n) \rightarrow f(a)/g(a)$이다. 각 경우에 [정리 4](#thm4){: data-lid="1t92j" }의 (b)$\Rightarrow$(a)를 적용하면 된다.
:::

상수함수와 항등함수 $x \mapsto x$가 연속임은 정의에서 바로 나오므로, [명제 7](#prop7){: data-lid="k787l" }을 반복하면 polynomial이 $\mathbb{R}$ 전체에서 연속이고 유리함수 $p/q$가 $q \neq 0$인 모든 점에서 연속임을 얻는다. 극한에 대해서도 같은 증명으로 $\lim_{x \rightarrow a}$가 사칙연산과 교환함이 나온다. 이때는 [정리 2](#thm2){: data-lid="gq3r8" }를 써서 $x_n \neq a$인 수열만 다루면 된다.

## 불연속의 분류

이 절에서 $f : I \rightarrow \mathbb{R}$이고 $I$는 구간, $a$는 $I$의 interior point이다. $x \rightarrow a$에서의 극한은 $x < a$와 $x > a$ 쪽이 서로 다를 수 있으므로, 제한된 함수의 극한을 따로 둔다. $I \cap (a, \infty)$로 제한한 $f$의 $a$에서의 극한을 *우극한*이라 하고 $f(a+)$로 적는다. 같은 방식으로 $I \cap (-\infty, a)$로 제한한 함수의 극한을 *좌극한*이라 하고 $f(a-)$로 적는다.

양쪽 극한이 모두 존재하고 같으면 $\lim_{x \rightarrow a} f(x)$가 존재하고 그 공통값과 같다. 두 $\delta$ 중 작은 쪽을 택하면 되기 때문이다. 역도 정의에서 곧바로 나오므로, 극한이 존재하는 것은 $f(a-) = f(a+)$인 것과 동치이고 $f$가 $a$에서 연속인 것은 $f(a-) = f(a) = f(a+)$인 것과 동치이다. 따라서 $f$가 $a$에서 연속이 아닐 때 다음 중 정확히 하나가 일어난다.

::: 정의 8 (불연속의 분류)
$f$가 $a$에서 연속이 아니라 하자.

(i) $f(a-)$와 $f(a+)$가 존재하고 서로 같다. 이때 $a$를 *removable discontinuity<sub>제거가능 불연속</sub>*이라 한다.

(ii) $f(a-)$와 $f(a+)$가 존재하고 서로 다르다. 이때 $a$를 *jump discontinuity<sub>도약 불연속</sub>*이라 한다.

(iii) $f(a-)$와 $f(a+)$ 중 적어도 하나가 존재하지 않는다. 이때 $a$를 *essential discontinuity<sub>본질적 불연속</sub>*이라 한다.
:::

(i)에서는 $f(a)$의 값을 공통 극한으로 바꾸면 $a$에서 연속이 되며, 이것이 제거가능이라는 이름의 이유이다. $f(a)$가 원래 정의되어 있지 않아도 같은 방식으로 정의할 수 있다. (ii)에서는 $f(a)$의 값이 무엇이든 불연속이다. (i)과 (ii)를 합쳐 Rudin은 first kind의 불연속이라 하고, (iii)을 second kind라 한다 [Rud].

::: 예시 9 (essential discontinuity)
$f(x) = \sin(1/x)$ ($x \neq 0$), $f(0) = 0$으로 정의하면 $0$은 essential discontinuity이다. 두 수열 $x_n = 1/(2\pi n + \pi/2)$와 $y_n = 1/(2\pi n + 3\pi/2)$는 모두 $0$보다 크고 $0$으로 수렴하지만 $f(x_n) = 1$, $f(y_n) = -1$이다. [정리 2](#thm2){: data-lid="61z0r" }에 의하여 우극한이 존재하면 두 수열에서의 값은 같은 극한으로 수렴해야 하므로 우극한은 존재하지 않는다. $f$가 홀함수이므로 좌극한도 존재하지 않는다.
:::

이 예시에서 $f(0)$의 값은 전혀 영향을 주지 않는다. $f(0)$을 어떻게 바꾸어도 불연속이 해소되지 않는다는 점에서 (iii)은 (i)과 근본적으로 다르다.

::: 예시 10 (Dirichlet 함수)
$D : \mathbb{R} \rightarrow \mathbb{R}$를 $x \in \mathbb{Q}$이면 $D(x) = 1$, $x \notin \mathbb{Q}$이면 $D(x) = 0$으로 정의한다. $D$는 모든 점에서 essential discontinuity를 갖는다. $a \in \mathbb{R}$과 $n \geq 1$에 대하여 $\mathbb{Q}$와 $\mathbb{R} \setminus \mathbb{Q}$가 $\mathbb{R}$에서 dense이므로 ([§실수의 완비성, ⁋정리 8](/ko/math/analysis/completeness_of_reals#thm8){: data-lid="6jbjd" }) 구간 $(a, a + 1/n)$에서 유리수 $x_n$과 무리수 $y_n$을 하나씩 고를 수 있다. $x_n, y_n \rightarrow a$이고 $D(x_n) = 1$, $D(y_n) = 0$이므로, [정리 2](#thm2){: data-lid="lw5gc" }에 의하여 $D$의 우극한은 존재하지 않는다. 구간 $(a - 1/n, a)$에서 같은 논증을 하면 좌극한도 존재하지 않는다.
:::

## Thomae 함수

연속인 점과 불연속인 점이 서로 섞이는 예로 Thomae 함수가 있다. $x \in \mathbb{Q}$는 $x = p/q$ ($p \in \mathbb{Z}$, $q \geq 1$, $p$와 $q$는 서로소)로 유일하게 적히며, 이 $q$를 $x$의 분모라 한다. $T : \mathbb{R} \rightarrow \mathbb{R}$를 유리수 $x$에서 $T(x) = 1/q$ ($q$는 $x$의 분모)로, 무리수 $x$에서 $T(x) = 0$으로 정의한다.

::: 명제 11 (Thomae 함수)
모든 $a \in \mathbb{R}$에 대하여 $\lim_{x \rightarrow a} T(x) = 0$이다. 따라서 $T$는 무리수에서 연속이고 유리수에서 removable discontinuity를 갖는다.
:::

::: 증명
$a \in \mathbb{R}$과 $\varepsilon > 0$이 주어졌다고 하자. $T \geq 0$이므로 $0 < \lvert x - a\rvert < \delta$이면 $T(x) < \varepsilon$이도록 $\delta$를 잡으면 된다. $T(x) \geq \varepsilon$인 $x$는 유리수 $p/q$이고 $1/q \geq \varepsilon$, 곧 $q \leq 1/\varepsilon$이다. 구간 $(a - 1, a + 1)$ 안에서 이러한 $x$는 유한개이다. 분모 $q$가 고정되었을 때 $p/q \in (a - 1, a + 1)$인 $p$는 구간 $(q(a-1), q(a+1))$ 안의 정수이므로 유한개이고, 가능한 $q$ 역시 유한개이기 때문이다. 이 유한집합에서 $a$를 제외한 점들을 $x_1, \ldots, x_m$이라 하고

$$\delta = \min\{1, \lvert x_1 - a\rvert, \ldots, \lvert x_m - a\rvert\}$$

로 둔다($m = 0$이면 $\delta = 1$). 그러면 $0 < \lvert x - a\rvert < \delta$일 때 $x \in (a - 1, a + 1)$이고 $x$는 $x_1, \ldots, x_m$ 중 어느 것도 아니므로 $T(x) < \varepsilon$이다.

$a$가 무리수이면 $T(a) = 0$이므로 극한값이 함숫값과 같아 $T$는 $a$에서 연속이다. $a$가 유리수이면 $T(a) > 0$이므로 극한값 $0$과 다르고, 좌극한과 우극한이 모두 $0$이므로 removable discontinuity이다.
:::

$\delta$를 잡을 때 쓴 것은 $\varepsilon$ 이상인 값을 갖는 점이 $a$ 가까이에 유한개뿐이라는 사실이다. 이것이 $\delta$를 $\varepsilon$에 따라 유한개의 점을 피하는 최솟값으로 잡는 이유이다. 또 Dirichlet 함수와 달리 $T$의 불연속점 집합 $\mathbb{Q}$는 $\mathbb{R}$에서 dense이다. 함수는 dense한 집합 위에서 불연속일 수 있고, 그러면서도 극한이 모든 점에서 존재할 수 있다.

## 단조함수의 불연속점

Dirichlet 함수는 불연속점이 $\mathbb{R}$ 전체이다. 단조함수에서는 불연속점이 훨씬 적다.

$f : I \rightarrow \mathbb{R}$가 구간 $I$ 위에서 increasing이라 하자. $a \in I$에 대하여 $a$가 $I$의 오른쪽 끝점이 아니면 $f(a+) = \inf\{f(x) \mid x \in I, x > a\}$로, 왼쪽 끝점이 아니면 $f(a-) = \sup\{f(x) \mid x \in I, x < a\}$로 둔다. $a$가 $I$의 왼쪽 끝점이면 $f(a-) = f(a)$로, 오른쪽 끝점이면 $f(a+) = f(a)$로 약속한다. 이 값들이 실제로 한쪽 극한이 되며 $f(a-) \leq f(a) \leq f(a+)$임을 먼저 보인다.

::: 정리 12 (단조함수의 불연속점)
$I$가 구간이고 $f : I \rightarrow \mathbb{R}$가 monotone function이라 하자. 그러면 $f$는 $I$의 모든 점에서 한쪽 극한을 갖고, $I$의 interior point에서 불연속이면 jump discontinuity이다. 또 $f$의 불연속점의 집합은 countable이다.
:::

::: 증명
$f$가 increasing인 경우만 보면 된다. 그렇지 않으면 $-f$에 적용한다.

$a$가 $I$의 왼쪽 끝점이 아니라 하고 $f(a-) = \sup\{f(x) \mid x < a\}$가 한쪽 극한임을 보인다. $f$가 increasing이므로 이 집합은 $f(a)$로 bounded above이다. $\varepsilon > 0$이 주어지면 상한에 대한 [§실수의 완비성, ⁋명제 4](/ko/math/analysis/completeness_of_reals#prop4){: data-lid="t0jp8" }에 의하여 $x_0 < a$가 있어 $f(x_0) > f(a-) - \varepsilon$이다. $\delta = a - x_0$로 두면 $a - \delta < x < a$일 때 $f(x_0) \leq f(x) \leq f(a-)$이므로 $0 \leq f(a-) - f(x) < \varepsilon$이다. 따라서 $\lim_{x \rightarrow a-} f(x) = f(a-)$이다. 우극한도 같은 방식으로 $\inf$에 대하여 보이며, $f(x) \leq f(a)$ ($x < a$), $f(a) \leq f(x)$ ($x > a$)에서 $f(a-) \leq f(a) \leq f(a+)$이다.

$f$가 $a$에서 연속인 것은 $f(a-) = f(a) = f(a+)$인 것이고, 부등식 $f(a-) \leq f(a) \leq f(a+)$에 의하여 이는 $f(a-) = f(a+)$와 동치이다. 따라서 $a$가 불연속점이면 $f(a-) < f(a+)$이다. $a$가 interior point이면 두 한쪽 극한이 존재하고 서로 다르므로 [정의 8](#def8){: data-lid="6sm5o" }의 (ii)에 해당하는 jump discontinuity이다.

불연속점 $a$마다 열린 구간 $J_a = (f(a-), f(a+))$를 대응시킨다. $f(a-) < f(a+)$이므로 $J_a$는 공집합이 아니다. $a < b$가 모두 불연속점이면 $I$가 구간이므로 $a < x < b$인 $x \in I$가 있고, $f(a+) \leq f(x) \leq f(b-)$이므로 $J_a$와 $J_b$는 서로소이다. 각 $J_a$에서 [§실수의 완비성, ⁋정리 8](/ko/math/analysis/completeness_of_reals#thm8){: data-lid="e0jif" }에 의하여 유리수 $r_a$를 하나 고르면 서로 다른 불연속점에 대하여 $r_a$도 서로 다르므로, $a \mapsto r_a$는 불연속점의 집합에서 $\mathbb{Q}$로 가는 단사함수이다. 따라서 불연속점의 집합은 countable이다.
:::

증명에서 쓴 것은 $\mathbb{R}$의 공집합이 아닌 열린 구간이 모두 유리수를 포함하므로, 서로소인 열린 구간들의 모임은 countable이라는 사실이다. 단조함수는 essential discontinuity를 갖지 않으며 jump의 크기는 서로소 구간으로 쌓여 그 개수가 제한된다.

---

**참고문헌**

**[Rud]** W. Rudin, *Principles of mathematical analysis*, 3rd ed., McGraw-Hill, 1976.
