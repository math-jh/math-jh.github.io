---
title: "미분방정식의 존재성과 유일성"
description: "초기값 문제를 integral equation으로 바꾸고 축소사상 정리로 Picard–Lindelöf 정리를 증명한다. 립시츠 조건이 빠지면 유일성이 깨지는 반례, 해가 유한시간에 폭발하는 예, Grönwall 부등식을 이용한 유일성과 최대 해 구간, Peano 존재정리의 진술을 다룬다."
excerpt: "Picard–Lindelöf 정리, Grönwall 부등식, 최대 해 구간"

categories: [Math / Analysis]
permalink: /ko/math/analysis/existence_uniqueness_ode
sidebar: 
    nav: "analysis-ko"

date: 2026-06-02
weight: 28

published: false

---

미분방정식 $y' = f(t, y)$에 초기 조건을 주었을 때 해가 존재하는지, 존재한다면 하나뿐인지는 $f$의 성질에 달려 있고, 두 성질은 서로 독립적으로 깨진다. $y' = 3y^{2/3}$, $y(0) = 0$은 해가 무수히 많고, $y' = y^2$, $y(0) = 1$은 해가 하나뿐이지만 유한한 시각에서 발산한다. 이 글에서는 두 현상을 각각 $f$의 어떤 성질이 막아 주는지를 가려낸다.

전략은 미분방정식을 integral equation으로 바꾸어 해를 어떤 함수 공간 위의 사상의 fixed point로 보는 것이다. 그럼 [§완비 거리공간과 축소사상 정리, ⁋정리 5](/ko/math/analysis/contraction_mapping#thm5){: data-lid="3o8dv" }를 적용할 수 있고, 립시츠 조건 아래에서 [정리 4](#thm4){: data-lid="vv3io" }가 나온다. 유일성의 전역적 형태와 해의 최대 존재 구간은 [보조정리 6](#lem6){: data-lid="9iftt" }으로 얻는다.

## 초기값 문제와 적분방정식

$D \subseteq \mathbb{R}^2$를 열린집합, $f : D \rightarrow \mathbb{R}$를 연속함수, $(t_0, y_0) \in D$라 하자.

::: 정의 1
*초기값 문제<sub>initial value problem</sub>*

$$y' = f(t, y), \qquad y(t_0) = y_0 \tag{IVP}$$

의 *해<sub>solution</sub>*는 $t_0$를 포함하는 구간 $I$ 위의 미분가능한 함수 $\varphi$로서, 모든 $t \in I$에 대하여 $(t, \varphi(t)) \in D$이고 $\varphi'(t) = f(t, \varphi(t))$이며 $\varphi(t_0) = y_0$인 것이다. $I$의 끝점에서는 한쪽 미분을 쓴다.
:::

해의 정의에는 구간이 포함되어 있다. 같은 식을 만족하더라도 정의역이 다르면 다른 해로 센다는 점이 뒤의 최대 해 구간의 논의에서 중요해진다.

미분가능성은 방정식 자체가 요구하는 것이어서, 해는 자동으로 $C^1$ 함수이다. $\varphi$가 미분가능하면 연속이고, $f$가 연속이므로 $\varphi'(t) = f(t, \varphi(t))$도 연속이기 때문이다. 이 관찰이 아래의 동치를 가능하게 한다.

::: 명제 2
$I$를 $t_0$를 포함하는 구간, $\varphi : I \rightarrow \mathbb{R}$를 모든 $t$에서 $(t, \varphi(t)) \in D$인 연속함수라 하자. 그럼 $\varphi$가 (IVP)의 해일 필요충분조건은

$$\varphi(t) = y_0 + \int_{t_0}^t f(s, \varphi(s)) \dd{s} \qquad (t \in I) \tag{INT}$$

이다.
:::

::: 증명
$\varphi$가 해이면 $\varphi'$가 연속이므로 [§미적분의 기본정리, ⁋정리 5](/ko/math/analysis/fundamental_theorem_of_calculus#thm5){: data-lid="lcywe" }에 의하여 $\varphi(t) - \varphi(t_0) = \int_{t_0}^t \varphi'(s) \dd{s}$이고, $\varphi' = f(s, \varphi(s))$, $\varphi(t_0) = y_0$을 대입하면 (INT)를 얻는다. 거꾸로 (INT)가 성립하면 $s \mapsto f(s, \varphi(s))$가 연속함수들의 합성이므로 연속이고, [§미적분의 기본정리, ⁋정리 2](/ko/math/analysis/fundamental_theorem_of_calculus#thm2){: data-lid="8zwen" }에 의하여 우변은 미분가능하며 도함수가 $f(t, \varphi(t))$이다. $t = t_0$을 대입하면 $\varphi(t_0) = y_0$이다.
:::

(INT)에는 도함수가 없고 연속함수만 등장한다. 우변을 함수 $\varphi$에 함수를 대응시키는 사상 $T$로 읽으면, 해는 $T\varphi = \varphi$를 만족하는 fixed point이다. 이 사상을 *Picard 작용소<sub>Picard operator</sub>*라 하고, 상수함수 $\varphi_0 \equiv y_0$에서 출발한 *Picard 반복*을 $\varphi_{n+1} = T\varphi_n$으로 정의한다. 가령 $y' = y$, $y(0) = 1$에서는

$$\varphi_{n+1}(t) = 1 + \int_0^t \varphi_n(s) \dd{s}$$

이고, $\varphi_0 = 1$에서 $\varphi_n(t) = \sum_{k=0}^n t^k/k!$이 귀납적으로 얻어져 반복은 $e^t$의 부분합을 차례로 내놓는다. 반복이 항상 수렴하는 것은 아니며, 수렴을 보장하는 것이 다음 절의 조건이다.

## 립시츠 조건

$f$가 연속이기만 하면 (IVP)의 해는 존재하지만 유일하지 않을 수 있다(뒤의 [예시 5](#ex5){: data-lid="bn566" }와 [정리 10](#thm10){: data-lid="gqj2v" }). 유일성을 얻으려면 $y$가 변할 때 $f$의 값이 변하는 정도를 통제해야 한다.

::: 정의 3
$S \subseteq D$ 위에서 $f$가 $y$에 관하여 *립시츠 조건<sub>Lipschitz condition</sub>*을 만족한다는 것은, 상수 $L \geq 0$이 존재하여 $(t, y_1), (t, y_2) \in S$인 모든 $t, y_1, y_2$에 대하여 $\lvert f(t, y_1) - f(t, y_2)\rvert \leq L\lvert y_1 - y_2\rvert$인 것이다. 이때 $L$을 *립시츠 상수<sub>Lipschitz constant</sub>*라 한다. $D$의 모든 점이 이 조건을 만족하는 근방을 가지면 $f$가 $y$에 관하여 *locally Lipschitz*라 한다.
:::

같은 $t$에서만 두 값을 비교한다는 점에 주의한다. $t$에 대해서는 연속성 이상을 요구하지 않는다.

$f$와 $\partial f/\partial y$가 $D$에서 연속이면 $f$는 locally Lipschitz이다. $D$ 안의 직사각형 $R$을 잡으면 $R$은 컴팩트이므로 [§연속함수의 성질, ⁋따름정리 2](/ko/math/analysis/continuous_functions#cor2){: data-lid="x3wr0" }에 의하여 $L = \max_R \lvert \partial f/\partial y\rvert$가 유한하고, $(t, y_1), (t, y_2) \in R$이면 두 점을 잇는 선분이 $R$ 안에 있으므로 [§평균값 정리와 테일러 정리, ⁋정리 3](/ko/math/analysis/mean_value_theorem#thm3){: data-lid="sby69" }에 의하여 $y_1$과 $y_2$ 사이의 어떤 $\xi$에서

$$\lvert f(t, y_1) - f(t, y_2)\rvert = \left\lvert \frac{\partial f}{\partial y}(t, \xi)\right\rvert \lvert y_1 - y_2\rvert \leq L\lvert y_1 - y_2\rvert$$

이다. 그러나 역은 성립하지 않는다. $f(t, y) = \lvert y\rvert$는 $L = 1$인 립시츠 함수이지만 $y = 0$에서 미분가능하지 않다. 반대로 $f(t, y) = y^{2/3}$은 $y = 0$ 근방에서 어떤 $L$로도 립시츠 조건을 만족하지 못한다.

## Picard–Lindelöf 정리

직사각형 $R = [t_0 - a, t_0 + a] \times [y_0 - b, y_0 + b] \subseteq D$를 잡고, $f$가 $R$ 위에서 $y$에 관하여 립시츠 상수 $L$로 립시츠라 하자. $R$이 컴팩트이므로 [§연속함수의 성질, ⁋따름정리 2](/ko/math/analysis/continuous_functions#cor2){: data-lid="lsbxo" }에 의하여 $M = \max_R \lvert f\rvert$가 유한하다. 구간의 반폭을

$$h = \min\Bigl(a, \frac{b}{M}, \frac{1}{2L}\Bigr)$$

로 두고($M = 0$ 또는 $L = 0$이면 해당 항은 제외한다), $I_h = [t_0 - h, t_0 + h]$라 하자.

::: 정리 4 (Picard–Lindelöf)
위의 가정 아래 (IVP)는 $I_h$ 위에서 그래프가 $R$ 안에 놓이는 해를 정확히 하나 가지며, Picard 반복 $\varphi_n$은 이 해로 $I_h$ 위에서 균등수렴한다.
:::

::: 증명
$X$를 $\lVert g - y_0\rVert_\infty \leq b$인 연속함수 $g : I_h \rightarrow \mathbb{R}$들의 집합으로 두고 상한노름이 주는 거리를 부여한다. 여기서 $\lVert g\rVert_\infty = \max_{I_h}\lvert g\rvert$이다. $I_h$가 컴팩트이므로 [§연속함수의 성질, ⁋따름정리 2](/ko/math/analysis/continuous_functions#cor2){: data-lid="9o73p" }에 의하여 최댓값이 존재한다. 연속함수열의 균등극한은 연속이고 상한노름에서 Cauchy인 열은 균등수렴하므로([§균등수렴, ⁋정리 6](/ko/math/analysis/uniform_convergence#thm6){: data-lid="gcmsp" }, [§균등수렴, ⁋명제 3](/ko/math/analysis/uniform_convergence#prop3){: data-lid="6arf5" }) $I_h$ 위의 연속함수 공간은 완비이고, $X$는 그 닫힌 subset이므로 [§완비 거리공간과 축소사상 정리, ⁋명제 2](/ko/math/analysis/contraction_mapping#prop2){: data-lid="york4" }에 의하여 완비 거리공간이다. 상수함수 $y_0$이 $X$에 속하므로 $X \neq \emptyset$이다.

먼저 $T$가 $X$를 $X$로 보냄을 확인한다. $g \in X$이면 $\lvert t - t_0\rvert \leq h \leq a$이고 $\lvert g(t) - y_0\rvert \leq b$이므로 $(t, g(t)) \in R$이고, $s \mapsto f(s, g(s))$는 연속이어서 $Tg$가 정의되고 연속이다. 또 $R$ 위에서 $\lvert f\rvert \leq M$이므로

$$\lvert (Tg)(t) - y_0\rvert \leq \left\lvert \int_{t_0}^t \lvert f(s, g(s))\rvert \dd{s}\right\rvert \leq M\lvert t - t_0\rvert \leq Mh \leq b$$

이다. 구간의 반폭에 $h \leq a$와 $h \leq b/M$을 둔 이유가 여기에 있다. 전자는 $g$가 $f$의 정의역 $R$ 안에서 평가되도록 하고, 후자는 $Tg$의 그래프가 다시 $R$ 안에 머물도록 한다.

다음으로 $T$가 축소사상임을 보인다. $g_1, g_2 \in X$이면 두 그래프가 모두 $R$ 안에 있으므로 립시츠 조건을 적분 안에서 쓸 수 있다. $t \in I_h$에 대하여

$$\begin{aligned}
\lvert (Tg_1)(t) - (Tg_2)(t)\rvert &= \left\lvert \int_{t_0}^t \bigl(f(s, g_1(s)) - f(s, g_2(s))\bigr) \dd{s}\right\rvert \\
&\leq \left\lvert \int_{t_0}^t L\lvert g_1(s) - g_2(s)\rvert \dd{s}\right\rvert \\
&\leq L\lvert t - t_0\rvert \lVert g_1 - g_2\rVert_\infty \leq Lh\lVert g_1 - g_2\rVert_\infty
\end{aligned}$$

이고, $t$에 대해 최댓값을 취하면 $\lVert Tg_1 - Tg_2\rVert_\infty \leq Lh\lVert g_1 - g_2\rVert_\infty$이다. $h \leq 1/(2L)$이므로 $Lh \leq 1/2$이다. 축소상수가 $1$보다 작기만 하면 되므로 $1/2$은 편의상의 선택이고, 이 조건 때문에 $h$가 $L$에 반비례하여 작아진다.

따라서 [§완비 거리공간과 축소사상 정리, ⁋정리 5](/ko/math/analysis/contraction_mapping#thm5){: data-lid="wzt75" }에 의하여 $T$는 $X$ 안에 유일한 fixed point $\varphi$를 가지고, $\varphi_0 = y_0 \in X$에서 출발한 반복 $\varphi_n = T^n \varphi_0$이 $\varphi$로 균등수렴한다. [명제 2](#prop2){: data-lid="695vo" }에 의하여 $X$의 fixed point은 그래프가 $R$ 안에 있는 (IVP)의 해와 같다. 그래프가 $R$ 안에 있는 해 $\psi$는 $\lvert \psi - y_0\rvert \leq b$이므로 $X$의 원소이고, 따라서 $\varphi$와 일치한다.
:::

정리의 유일성은 그래프가 $R$ 안에 있는 해들 사이에서만 말한다. $R$ 밖으로 나가는 해가 있는지는 여기서 결정되지 않으며, 이는 뒤의 [명제 7](#prop7){: data-lid="4ctjd" }에서 해결된다. 또 존재 구간의 길이 $h$는 $a$뿐 아니라 $b/M$과 $1/(2L)$에도 좌우된다. 해가 존재하는 구간이 방정식이 정의된 영역의 크기만으로 정해지지 않는다는 점은 [예시 9](#ex9){: data-lid="jgf9z" }에서 구체적으로 나타난다.

우리는 $y$가 실수값인 경우만 썼지만, $y \in \mathbb{R}^n$인 연립방정식에서도 같은 증명이 그대로 성립한다. $\mathbb{R}^n$에 최댓값 노름 $\lVert y\rVert = \max_i \lvert y_i\rvert$을 쓰면 적분의 노름이 노름의 적분으로 성분별로 평가되므로 위의 모든 부등식이 그대로 유지된다.

립시츠 조건이 빠지면 유일성이 무너진다.

::: 예시 5 (유일성의 실패)
$y' = 3y^{2/3}$, $y(0) = 0$을 보자. 여기서 $f(t, y) = 3y^{2/3}$은 연속이지만 $y \rightarrow 0$일 때

$$\frac{\lvert f(t, y) - f(t, 0)\rvert}{\lvert y - 0\rvert} = \frac{3}{\lvert y\rvert^{1/3}} \rightarrow \infty$$

이므로 $y = 0$의 어떤 근방에서도 립시츠 조건이 성립하지 않는다. 한편 $\varphi \equiv 0$은 해이고 $\varphi(t) = t^3$도 해이다. $\varphi'(t) = 3t^2$이고 $3(t^3)^{2/3} = 3t^2$이기 때문이다. 더 일반적으로 $c_1 \leq 0 \leq c_2$에 대하여

$$\varphi_{c_1, c_2}(t) = \begin{cases} (t - c_1)^3, & t < c_1 \\ 0, & c_1 \leq t \leq c_2 \\ (t - c_2)^3, & t > c_2 \end{cases}$$

도 해이다. 이음점에서 양쪽 도함수가 모두 $0$이므로 $C^1$이고, 각 조각에서는 위의 계산이 그대로 적용된다. 따라서 초기값 문제는 $c_1, c_2$로 매개화되는 해를 무수히 가진다. 이 방정식에서 $\varphi_0 \equiv 0$으로 출발한 Picard 반복은 $T0 = 0$이어서 영원히 $0$에 머문다. 반복은 수렴하지만 그 극한은 해들 중 하나일 뿐이고, $T$는 어떤 구간에서도 축소사상이 아니다.
:::

## Grönwall 부등식

[정리 4](#thm4){: data-lid="d35ij" }는 그래프가 $R$ 안에 있는 해에 대해서만 유일성을 주었다. 임의의 두 해가 일치함을 보이려면 두 해의 차가 $0$임을 직접 평가해야 하고, 여기에 쓰이는 것이 다음 부등식이다.

::: 보조정리 6 (Grönwall 부등식)
$J$를 구간, $t_\ast \in J$, $u : J \rightarrow [0, \infty)$를 연속함수라 하고 $C, L \geq 0$이 모든 $t \in J$에서

$$u(t) \leq C + L\left\lvert \int_{t_\ast}^t u(s) \dd{s}\right\rvert$$

을 만족한다고 하자. 그럼 모든 $t \in J$에서 $u(t) \leq Ce^{L\lvert t - t_\ast\rvert}$이다.
:::

::: 증명
$t \geq t_\ast$인 경우를 먼저 보자. $U(t) = C + L\int_{t_\ast}^t u(s) \dd{s}$로 두면 $u$가 연속이므로 $U$는 미분가능하고 $U' = Lu$이다. 가정은 $u \leq U$이므로 $U' \leq LU$이고, 따라서

$$\frac{\dd{}}{\dd{t}}\Bigl(U(t)e^{-L(t - t_\ast)}\Bigr) = \bigl(U'(t) - LU(t)\bigr)e^{-L(t - t_\ast)} \leq 0$$

이다. 그럼 $U(t)e^{-L(t - t_\ast)} \leq U(t_\ast) = C$이고, $u \leq U$를 다시 쓰면 $u(t) \leq Ce^{L(t - t_\ast)}$이다. $U$의 부호에 대한 가정이 필요하지 않으므로 $C = 0$인 경우도 그대로 포함된다. $t \leq t_\ast$인 경우에는 $v(s) = u(2t_\ast - s)$가 $s \geq t_\ast$에서 같은 가정을 만족하므로 위 결과를 $v$에 적용하면 된다.
:::

$C = 0$인 경우가 유일성의 핵심이다. 이때 결론은 $u \equiv 0$이다. 또 같은 논증에서 $C = \lvert \varphi_1(t_\ast) - \varphi_2(t_\ast)\rvert$로 두면, 두 해의 초기값이 $\delta$만큼 다를 때 $f$가 전체에서 $L$-립시츠이면 두 해의 거리가 $\delta e^{L\lvert t - t_\ast\rvert}$를 넘지 못한다는 평가도 얻는다.

::: 명제 7 (유일성)
$f$가 $D$ 위에서 연속이고 $y$에 관하여 locally Lipschitz라 하자. $\varphi_1, \varphi_2$가 각각 구간 $I_1, I_2$ 위의 (IVP)의 해이면, $I_1 \cap I_2$ 위에서 $\varphi_1 = \varphi_2$이다.
:::

::: 증명
$I = I_1 \cap I_2$는 $t_0$를 포함하는 구간이고, $A = \{t \in I : \varphi_1(t) = \varphi_2(t)\}$로 두자. $t_0 \in A$이고, 두 함수가 연속이므로 $A$는 $I$에서 닫혀 있다. $A$가 $I$에서 열려 있음을 보이면 $I$가 구간이어서 [§연결성과 중간값 정리, ⁋정리 2](/ko/math/analysis/connectedness#thm2){: data-lid="vgx1n" }에 의하여 연결이므로 $A = I$이다.

$t_\ast \in A$라 하고 $c = \varphi_1(t_\ast) = \varphi_2(t_\ast)$로 두자. $(t_\ast, c) \in D$이고 $f$가 locally Lipschitz이므로 $(t_\ast, c)$를 중심으로 하는 직사각형 $R_\ast \subseteq D$와 상수 $L$이 있어서 $f$가 $R_\ast$ 위에서 $L$-립시츠이다. 두 해가 연속이므로 $t_\ast$의 어떤 근방 $J \subseteq I$에서 두 그래프가 모두 $R_\ast$ 안에 있다. $u = \lvert \varphi_1 - \varphi_2\rvert$로 두면 (INT)에 의하여 $t \in J$에서

$$u(t) = \left\lvert \int_{t_\ast}^t \bigl(f(s, \varphi_1(s)) - f(s, \varphi_2(s))\bigr) \dd{s}\right\rvert \leq L\left\lvert \int_{t_\ast}^t u(s) \dd{s}\right\rvert$$

이다. [보조정리 6](#lem6){: data-lid="i7hh8" }을 $C = 0$으로 적용하면 $J$ 위에서 $u \equiv 0$이므로 $J \subseteq A$이다.
:::

이 명제에서 [정리 4](#thm4){: data-lid="ytcvq" }의 유일성 부분이 갖던 제약이 사라진다. $f$가 locally Lipschitz이기만 하면 (IVP)의 두 해는 공통 정의역 위에서 항상 일치한다. 또 한 점에서 갈라진 두 해가 같은 점에서 다시 만나는 일도 없다. [예시 5](#ex5){: data-lid="bzk2n" }의 해들은 모두 $y = 0$ 위의 점에서 갈라지는데, 그 점들에서 립시츠 조건이 깨져 있다.

## 최대 해 구간

이제 $f$가 $D$ 위에서 연속이고 $y$에 관하여 locally Lipschitz라 하자. [정리 4](#thm4){: data-lid="vnakd" }는 각 점 근방에서 해의 존재를 주고, [명제 7](#prop7){: data-lid="3z2xh" }은 두 해가 겹치는 구간에서 일치함을 주므로, 해들을 이어 붙여 더 이상 연장할 수 없는 해를 만들 수 있다.

::: 정리 8 (최대 해)
$(t_0, y_0) \in D$에 대하여 열린구간 $(\alpha, \beta) \ni t_0$ 위의 해 $\varphi$가 있어서 다음이 성립한다.

(1) (IVP)의 모든 해는 $\varphi$의 제한이다. 특히 $\varphi$는 더 큰 구간으로 연장되지 않는다.

(2) $\beta < \infty$이면, 임의의 컴팩트집합 $K \subseteq D$에 대하여 $\tau < \beta$가 있어서 $\tau < t < \beta$에서 $(t, \varphi(t)) \notin K$이다. $\alpha > -\infty$인 경우도 마찬가지이다.
:::

::: 증명
(1) (IVP)의 해들의 모임을 $\mathcal{S}$라 하자. [정리 4](#thm4){: data-lid="nmuki" }와 $D$가 열린집합이라는 사실에서 $\mathcal{S} \neq \emptyset$이다. $(t_0, y_0)$를 중심으로 하는 $D$ 안의 직사각형 위에서 $f$가 립시츠가 되도록 직사각형을 충분히 작게 잡을 수 있기 때문이다.

먼저 $\psi \in \mathcal{S}$의 정의역에 끝점 $t_1$이 속하면 $\psi$를 $t_1$ 너머로 연장할 수 있음을 보인다. $t_1$이 오른쪽 끝점이라 하자. $(t_1, \psi(t_1))$에서 [정리 4](#thm4){: data-lid="5r0sv" }를 적용하면 $[t_1 - h, t_1 + h]$ 위의 해 $\chi$가 있고 $\chi(t_1) = \psi(t_1)$이다. [명제 7](#prop7){: data-lid="ypmh6" }의 증명과 같은 논증으로, 같은 점에서 같은 값을 갖는 $\psi$와 $\chi$는 공통 정의역에서 일치한다. 따라서 $\psi$와 $\chi$를 붙인 함수가 정의되고, 그것이 $t_1$을 내점으로 갖는 해이다. $\chi$가 (IVP)가 아닌 $(t_1, \psi(t_1))$에서의 초기값 문제의 해라는 점은 이 논증에 영향을 주지 않는다. [명제 7](#prop7){: data-lid="keuu4" }이 임의의 초기점에 대해 성립하기 때문이다. 왼쪽 끝점도 같다.

$J$를 $\mathcal{S}$의 모든 해의 정의역의 합집합이라 하자. 두 해는 [명제 7](#prop7){: data-lid="qjuwa" }에 의하여 공통 정의역에서 일치하므로 $t \in J$에 대하여 $t$를 정의역에 포함하는 $\psi \in \mathcal{S}$를 골라 $\varphi(t) = \psi(t)$로 두면 $\varphi : J \rightarrow \mathbb{R}$가 잘 정의된다. 위의 연장 결과에 의하여 $J$의 각 점은 어떤 해의 정의역의 내점이므로 $J$는 열린구간 $(\alpha, \beta)$이고 $\varphi$는 각 점 근방에서 어떤 해와 같아 해이다. 모든 해는 정의상 $\varphi$의 제한이다.

(2) 결론이 거짓이라 하자. 그럼 컴팩트집합 $K \subseteq D$와 $t_n \rightarrow \beta$, $t_n < \beta$인 수열이 있어서 $(t_n, \varphi(t_n)) \in K$이다. $K$가 컴팩트이므로 [§컴팩트성, ⁋정리 5](/ko/math/analysis/compactness#thm5){: data-lid="t3cd5" }에 의하여 부분수열을 취하여 $(t_n, \varphi(t_n)) \rightarrow (\beta, y_\ast) \in K \subseteq D$로 둘 수 있다. $(\beta, y_\ast)$를 중심으로 하는 직사각형 $[\beta - a, \beta + a] \times [y_\ast - b, y_\ast + b] \subseteq D$를 $f$가 그 위에서 립시츠가 되도록 잡고, 립시츠 상수를 $L$, $\lvert f\rvert$의 최댓값을 $M$이라 하자. 충분히 큰 $n$에 대하여 $\lvert t_n - \beta\rvert < a/2$, $\lvert \varphi(t_n) - y_\ast\rvert < b/2$이므로 $(t_n, \varphi(t_n))$을 중심으로 하는 $[t_n - a/2, t_n + a/2] \times [\varphi(t_n) - b/2, \varphi(t_n) + b/2]$는 위의 큰 직사각형 안에 있고, 같은 $L$과 $M$이 그 위에서도 유효하다. 따라서 [정리 4](#thm4){: data-lid="7wd4y" }를 이 작은 직사각형에 적용하면, $n$에 무관한

$$h' = \min\Bigl(\frac{a}{2}, \frac{b}{2M}, \frac{1}{2L}\Bigr)$$

에 대하여 $(t_n, \varphi(t_n))$에서 출발하는 해 $\chi_n$이 $[t_n - h', t_n + h']$ 위에 존재한다. $t_n \rightarrow \beta$이므로 $\beta - t_n < h'$인 $n$을 고르면 $\chi_n$은 $\beta$를 내점으로 가지고, [명제 7](#prop7){: data-lid="m86ry" }에 의하여 $\varphi$와 겹치는 구간에서 일치한다. 그럼 $\varphi$와 $\chi_n$을 붙여 $\varphi$를 $\beta$ 너머로 연장한 해가 얻어지고, 이는 (1)에 모순이다.
:::

(2)는 최대 해가 유한한 끝에서 끝나려면 그래프가 $D$의 어떤 컴팩트집합에도 머무르지 않고 $D$의 boundary로 빠져나가야 함을 말한다. $D = \mathbb{R}^2$인 경우 이는 $\beta < \infty$이면 $\lvert \varphi(t)\rvert \rightarrow \infty$ ($t \rightarrow \beta$)라는 뜻이다. $K = [t_0, \beta] \times [-N, N]$에 적용하면 모든 $N$에 대하여 $t$가 $\beta$에 충분히 가까울 때 $\lvert \varphi(t)\rvert > N$이기 때문이다.

::: 예시 9 (유한시간 폭발)
$y' = y^2$, $y(0) = 1$을 보자. $f(t, y) = y^2$은 $\partial f/\partial y = 2y$가 연속이어서 $\mathbb{R}^2$ 위에서 locally Lipschitz이다. 변수분리로 $\dd{y}/y^2 = \dd{t}$를 적분하면 $-1/y = t + C$이고 $y(0) = 1$에서 $C = -1$이므로

$$\varphi(t) = \frac{1}{1 - t}, \qquad t \in (-\infty, 1)$$

이다. 실제로 $\varphi'(t) = (1 - t)^{-2} = \varphi(t)^2$이다. 이 해는 $t \rightarrow 1^-$에서 $+\infty$로 발산한다. 다른 해 $\psi$가 $1$을 정의역에 포함하면, [명제 7](#prop7){: data-lid="l7d74" }에 의하여 $[0, 1)$에서 $\psi = \varphi$이고 $\psi$가 $t = 1$에서 연속이어야 하는데 $\varphi$는 $1$ 근방에서 유계가 아니므로 모순이다. 따라서 최대 해 구간은 $(-\infty, 1)$이다.

초기값을 $y(0) = y_0 > 0$으로 두면 해는 $y_0/(1 - y_0 t)$이고 폭발 시각은 $1/y_0$이다. 초기값이 클수록 폭발이 빨라진다. $y(0) = 0$이면 해가 $y \equiv 0$이어서 전 구간에서 존재한다. 방정식은 모든 $(t, y)$에서 매끄럽지만 정의역이 전체인 것이 해의 정의역이 전체임을 뜻하지 않는다. 립시츠 상수가 $y$와 함께 $2\lvert y\rvert$로 자라므로, [정리 4](#thm4){: data-lid="mb6k9" }의 $h$가 해가 커질수록 줄어들어 구간을 이어 붙여도 $1$을 넘지 못한다.
:::

반대로 [예시 5](#ex5){: data-lid="1qyjg" }의 방정식은 해가 무수히 많지만 모든 해가 $\mathbb{R}$ 전체에서 정의된다. 따라서 유일성의 실패와 폭발은 서로 다른 현상이다.

## Peano 존재정리

립시츠 조건을 완전히 버리고 $f$의 연속성만 가정하면 존재는 여전히 성립한다.

::: 정리 10 (Peano)
$f$가 직사각형 $R = [t_0 - a, t_0 + a] \times [y_0 - b, y_0 + b]$ 위에서 연속이고 $M = \max_R \lvert f\rvert$이면, (IVP)는 $[t_0 - h, t_0 + h]$, $h = \min(a, b/M)$ 위에서 적어도 하나의 해를 가진다.
:::

증명은 Euler 꺾은선 근사 $\varphi_k$를 만드는 데서 시작한다. 꺾은선은 모두 $R$ 안에 있고 기울기의 크기가 $M$ 이하이므로 uniformly bounded이며 동등연속이다. 따라서 [§동등연속성과 Arzelà–Ascoli 정리, ⁋정리 6](/ko/math/analysis/arzela_ascoli#thm6){: data-lid="1s0vw" }에 의하여 균등수렴하는 부분수열이 있고, 그 극한이 (INT)를 만족한다. 이 정리에서는 극한함수가 해임이 보장될 뿐 어느 부분수열을 택하느냐에 따라 다른 극한이 나올 수 있으며, [예시 5](#ex5){: data-lid="uz9gn" }가 정확히 이 경우이다. $f(t, y) = 3y^{2/3}$은 연속이므로 [정리 10](#thm10){: data-lid="0agcc" }이 적용되어 해의 존재가 보장되지만, 립시츠 조건이 없으므로 [정리 4](#thm4){: data-lid="jhgo5" }와 [명제 7](#prop7){: data-lid="j5dr7" }이 적용되지 않고 유일성이 깨진다. [정리 4](#thm4){: data-lid="v76f7" }가 요구하는 조건이 존재가 아니라 유일성에 필요한 조건임이 여기서 드러난다.

---

**참고문헌**

**[Rud]** W. Rudin, *Principles of mathematical analysis*, 3rd ed., McGraw-Hill, 1976.
