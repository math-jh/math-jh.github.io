---
title: "Stone–Weierstrass 정리"
description: "컴팩트 구간 위의 연속함수가 다항식으로 균등근사된다는 Weierstrass 근사정리를 Bernstein 다항식으로 증명하고, 이를 점을 분리하고 어디서도 사라지지 않는 함수 대수로 일반화한 Stone–Weierstrass 정리를 증명한다. 복소판에서 켤레에 닫힘이 필요한 이유, 삼각다항식의 조밀성, 컴팩트성이 빠지면 실패하는 예를 다룬다."
excerpt: "Weierstrass 근사정리, Stone–Weierstrass 정리(실수판·복소판), 삼각다항식의 조밀성, 가정이 빠진 반례"

categories: [Math / Analysis]
permalink: /ko/math/analysis/stone_weierstrass
sidebar: 
    nav: "analysis-ko"

date: 2026-10-13
weight: 23

published: false

---

[§균등수렴, ⁋정리 6](/ko/math/analysis/uniform_convergence#thm6){: data-lid="u5kit" }에서 보았듯이 연속함수열의 균등극한은 다시 연속함수이다. 따라서 polynomial과 같이 다루기 쉬운 함수들의 균등극한으로 얻어지는 함수는 연속이어야 한다. 이 글의 주제는 그 역으로, 컴팩트 집합 위에서는 연속함수가 다루기 쉬운 함수들로 얼마든지 정밀하게 근사된다는 사실이다. 먼저 구간 위의 polynomial에 대한 Weierstrass 근사정리를 증명하고, 이를 polynomial의 어떤 성질이 근사를 가능하게 하는가에 대한 답인 Stone–Weierstrass 정리로 확장한다.

컴팩트 거리공간 $X$ 위의 연속함수 전체를 $C(X)$로 적고, 상한노름 $\lVert f\rVert = \sup_{x \in X}\lvert f(x)\rvert$에 대한 거리를 쓴다. [§연속함수의 성질, ⁋따름정리 2](/ko/math/analysis/continuous_functions#cor2){: data-lid="seq16" }에서 보았듯이 $X$가 컴팩트이면 $C(X)$의 모든 원소는 bounded이므로 $\lVert f\rVert$는 유한하다. $A \subseteq C(X)$가 *조밀하다*는 것은 모든 $f \in C(X)$와 $\varepsilon > 0$에 대해 $\lVert f - g\rVert < \varepsilon$인 $g \in A$가 존재한다는 것, 곧 모든 연속함수가 $A$의 원소들의 균등극한이라는 것이다. $C(X,\mathbb{R})$과 $C(X,\mathbb{C})$를 구별해야 할 때는 이렇게 적는다.

## Weierstrass 근사정리

$[0,1]$ 위의 함수 $f$에 대해 다음의 polynomial을 *Bernstein polynomial*이라 한다.

$$B_n f(x) = \sum_{k=0}^n f\left(\frac{k}{n}\right) \binom{n}{k} x^k (1-x)^{n-k}$$

$w_{n,k}(x) = \binom{n}{k}x^k(1-x)^{n-k}$로 적으면 $B_n f(x)$는 표본점 $k/n$에서의 값 $f(k/n)$을 가중치 $w_{n,k}(x)$로 평균한 것이다. 가중치는 $x$가 $k/n$ 근처일 때 크므로, $n$이 커지면 평균은 $f(x)$ 근처의 값들에 집중되리라 기대된다. 이를 정량화하는 데 필요한 것은 가중치의 합과 일차·이차 모멘트이다.

::: 보조정리 1 (Bernstein 항등식)
모든 $x \in \mathbb{R}$과 $n \geq 1$에 대해 다음이 성립한다.

$$\sum_{k=0}^n w_{n,k}(x) = 1, \quad \sum_{k=0}^n k  w_{n,k}(x) = nx, \quad \sum_{k=0}^n (k - nx)^2 w_{n,k}(x) = nx(1-x)$$
:::

::: 증명
이항정리 $(x+y)^n = \sum_k \binom{n}{k}x^k y^{n-k}$에서 $y = 1-x$를 대입하면 첫째 식이 나온다. 이항정리의 양변을 $x$에 대해 한 번, 두 번 미분하면

$$n(x+y)^{n-1} = \sum_k k\binom{n}{k}x^{k-1}y^{n-k}, \quad n(n-1)(x+y)^{n-2} = \sum_k k(k-1)\binom{n}{k}x^{k-2}y^{n-k}$$

이고, 각각에 $x$, $x^2$을 곱한 뒤 $y = 1-x$를 대입하면 $\sum_k k w_{n,k} = nx$와 $\sum_k k(k-1) w_{n,k} = n(n-1)x^2$을 얻는다. 따라서 $\sum_k k^2 w_{n,k} = n(n-1)x^2 + nx$이고,

$$\begin{aligned}
\sum_k (k-nx)^2 w_{n,k} &= \sum_k k^2 w_{n,k} - 2nx\sum_k k w_{n,k} + n^2x^2\sum_k w_{n,k} \\
&= n(n-1)x^2 + nx - 2n^2x^2 + n^2x^2 = nx(1-x)
\end{aligned}$$

가 된다.
:::

$x \in [0,1]$이면 $x(1-x) \leq 1/4$이므로 셋째 항등식은 $\sum_k (k/n - x)^2 w_{n,k}(x) \leq 1/(4n)$을 준다. 이 부등식에서 $x$에 무관한 상수 $1/(4n)$이 나온다는 점이 균등수렴을 보장한다.

::: 정리 2 (Weierstrass 근사정리)
$f$가 $[a,b]$ 위의 연속함수이면, 임의의 $\varepsilon > 0$에 대해 polynomial $p$가 존재하여 모든 $x \in [a,b]$에 대해 $\lvert f(x) - p(x)\rvert < \varepsilon$이다.
:::

::: 증명
먼저 $[a,b] = [0,1]$인 경우를 보인다. 일반의 경우는 $t = (x-a)/(b-a)$로 $[a,b]$를 $[0,1]$로 옮기면 $g(t) = f(a + (b-a)t)$가 $[0,1]$ 위의 연속함수가 되고, $g$를 근사하는 polynomial $q(t)$에 대해 $p(x) = q((x-a)/(b-a))$가 다시 polynomial이므로 환원된다.

$f \in C[0,1]$이라 하자. $f$는 컴팩트 집합 위의 연속함수이므로 bounded이고([§연속함수의 성질, ⁋따름정리 2](/ko/math/analysis/continuous_functions#cor2){: data-lid="obxov" }) 균등연속이다([§연속함수의 성질, ⁋정리 6](/ko/math/analysis/continuous_functions#thm6){: data-lid="ndbyp" }). $M = \lVert f\rVert$로 두고 $\varepsilon > 0$이 주어졌다고 하자. 균등연속성에 의해 $\lvert s - t\rvert < \delta$이면 $\lvert f(s) - f(t)\rvert < \varepsilon/2$인 $\delta > 0$이 존재한다. 여기서 $\delta$는 $x$에 무관하게 잡힌다는 점이 중요하다.

[보조정리 1](#lem1){: data-lid="b26m9" }의 첫째 식에 의해 $f(x) = \sum_k f(x) w_{n,k}(x)$이므로

$$\lvert B_nf(x) - f(x)\rvert \leq \sum_{k=0}^n \left\lvert f\left(\frac{k}{n}\right) - f(x)\right\rvert w_{n,k}(x)$$

이다. 고정된 $x$에 대해 지표 $k$를 $\lvert k/n - x\rvert < \delta$인 것과 $\lvert k/n - x\rvert \geq \delta$인 것으로 나눈다. 첫째 부류에서는 $\lvert f(k/n) - f(x)\rvert < \varepsilon/2$이므로, 이 부류의 합은 $\frac{\varepsilon}{2}\sum_k w_{n,k}(x) = \varepsilon/2$ 이하이다. 둘째 부류에서는 $\lvert f(k/n) - f(x)\rvert \leq 2M$이고 $(k/n - x)^2/\delta^2 \geq 1$이므로 항마다 $w_{n,k}(x) \leq (k/n - x)^2 w_{n,k}(x)/\delta^2$이다. 따라서 이 부류의 합은 [보조정리 1](#lem1){: data-lid="37m4t" }의 셋째 식에 의해

$$2M \sum_{\lvert k/n - x\rvert \geq \delta} w_{n,k}(x) \leq \frac{2M}{\delta^2}\sum_{k=0}^n \left(\frac{k}{n} - x\right)^2 w_{n,k}(x) \leq \frac{M}{2n\delta^2}$$

이하이다. $N$을 $M/(2N\delta^2) < \varepsilon/2$이도록 잡으면, $n \geq N$일 때 모든 $x \in [0,1]$에 대해 $\lvert B_nf(x) - f(x)\rvert < \varepsilon$이다. $\varepsilon/2$를 두 부류에 한 번씩 배분한 것이 이 선택의 이유이며, $N$은 $M$, $\delta$, $\varepsilon$에만 의존하므로 수렴은 균등하다.
:::

증명에서 $f$의 연속성은 균등연속성의 형태로, 그리고 $[0,1]$의 compactness는 그 균등연속성과 $M$의 유한성을 통해 쓰였다. 또 Bernstein polynomial은 $f$가 매끄러울 때에도 $f$의 도함수를 근사하는 것 이상을 보장하지 않는다. 위의 증명이 주는 것은 함수값의 균등근사뿐이다.

## 함수 대수

[정리 2](#thm2){: data-lid="29lgn" }의 증명에서 polynomial 자체의 구조는 거의 쓰이지 않았다. polynomial이 합과 곱에 대해 닫혀 있고, 상수를 포함하며, $x$ 자체가 서로 다른 두 점을 구별한다는 사실이 근사를 가능하게 한다. 이 세 성질을 다음 용어로 정리한다.

::: 정의 3
$A \subseteq C(X,\mathbb{R})$이 합, 곱, 실수배에 대해 닫혀 있으면 $A$를 *subalgebra*라 한다. $A$가 *점을 분리한다<sub>separates points</sub>*는 것은 서로 다른 $x, y \in X$마다 $f(x) \neq f(y)$인 $f \in A$가 존재한다는 것이고, $A$가 *어디서도 사라지지 않는다<sub>vanishes at no point</sub>*는 것은 모든 $x \in X$마다 $f(x) \neq 0$인 $f \in A$가 존재한다는 것이다.
:::

상수함수를 포함하는 subalgebra는 어디서도 사라지지 않는다. polynomial 전체는 상수를 포함하고 $f(x) = x$로 점을 분리한다. 한편 두 조건은 근사에 대해 필요하다. 모든 $f \in A$가 $f(x) = f(y)$를 만족하는 $x \neq y$가 있으면, 균등수렴은 점별수렴을 함의하므로 $A$의 균등극한도 같은 등식을 만족한다. 따라서 $A$는 $C(X)$에서 조밀할 수 없다. 마찬가지로 모든 $f \in A$가 $x_0$에서 $0$이면 극한도 $x_0$에서 $0$이므로, 상수함수 $1$을 근사할 수 없다. 두 조건이 충분하다는 것이 다음 정리이다.

## Stone–Weierstrass 정리: 실수판

::: 정리 4 (Stone–Weierstrass 정리)
$X$가 컴팩트 거리공간이고 $A \subseteq C(X,\mathbb{R})$이 점을 분리하며 어디서도 사라지지 않는 subalgebra이면, $A$는 $C(X,\mathbb{R})$에서 조밀하다.
:::

증명은 세 단계로 이루어진다. $A$의 균등폐포 $B$가 절댓값과 max, min에 대해 닫혀 있음을 보이고, 두 점에서 임의의 값을 갖는 함수를 $A$에서 만든 뒤, 컴팩트성으로 이 함수들을 이어 붙인다.

::: 보조정리 5
$A$가 $C(X,\mathbb{R})$의 subalgebra이고 $B$가 $A$의 상한노름에 대한 폐포이면, $B$도 subalgebra이다. 또 $f \in B$이면 $\lvert f\rvert \in B$이고, 따라서 $f, g \in B$에 대해 $\max(f,g)$와 $\min(f,g)$도 $B$의 원소이다.
:::

::: 증명
$f_n \to f$, $g_n \to g$가 균등수렴이고 $f_n, g_n \in A$라 하자. 합과 실수배는 노름의 삼각부등식으로 곧바로 따른다. 곱은

$$\lVert f_ng_n - fg\rVert \leq \lVert f_n\rVert \lVert g_n - g\rVert + \lVert g\rVert \lVert f_n - f\rVert$$

에서, $\lVert f_n\rVert$이 $\lVert f\rVert + 1$ 이하로 bounded이므로 $0$으로 간다. 따라서 $B$는 subalgebra이다.

$f \in B$이고 $a = \lVert f\rVert > 0$이라 하자 ($a = 0$이면 $f = 0 \in B$이다). $\varepsilon > 0$에 대해 [정리 2](#thm2){: data-lid="wk2ze" }를 $[-a,a]$ 위의 함수 $y \mapsto \lvert y\rvert$에 적용하면 polynomial $P$가 존재하여 $\lvert y\rvert \leq a$이면 $\lvert P(y) - \lvert y\rvert\rvert < \varepsilon$이다. $y = 0$을 넣으면 $\lvert P(0)\rvert < \varepsilon$이므로, $Q = P - P(0)$는 $Q(0) = 0$이고 $\lvert y\rvert \leq a$에서 $\lvert Q(y) - \lvert y\rvert\rvert < 2\varepsilon$이다. 상수항을 $0$으로 맞추는 이유는 $B$가 상수함수를 포함한다고 보장할 수 없기 때문이다. $Q(y) = \sum_{k=1}^m c_ky^k$이므로 $Q \circ f = \sum_{k=1}^m c_kf^k$이고, 이는 $B$가 subalgebra이므로 $B$의 원소이다. 모든 $x$에서 $\lvert f(x)\rvert \leq a$이므로 $\lVert Q \circ f - \lvert f\rvert\rVert \leq 2\varepsilon$이다. $\varepsilon$이 임의이고 $B$가 닫혀 있으므로 $\lvert f\rvert \in B$이다. 마지막 주장은 $\max(f,g) = (f + g + \lvert f - g\rvert)/2$, $\min(f,g) = (f + g - \lvert f - g\rvert)/2$에서 나온다.
:::

::: 보조정리 6
$A$가 점을 분리하며 어디서도 사라지지 않는 subalgebra이면, 서로 다른 $x, y \in X$와 임의의 $c, d \in \mathbb{R}$에 대해 $f(x) = c$, $f(y) = d$인 $f \in A$가 존재한다.
:::

::: 증명
$A$가 점을 분리하므로 $g(x) \neq g(y)$인 $g \in A$가 있고, 어디서도 사라지지 않으므로 $h(x) \neq 0$인 $h \in A$와 $k(y) \neq 0$인 $k \in A$가 있다. $u = gk - g(x)k$, $v = gh - g(y)h$로 두면 $u, v \in A$이고,

$$u(x) = 0, \quad u(y) = (g(y) - g(x))k(y) \neq 0, \quad v(y) = 0, \quad v(x) = (g(x) - g(y))h(x) \neq 0$$

이다. 따라서 $f = c v/v(x) + d u/u(y)$가 $f(x) = c$, $f(y) = d$를 만족하는 $A$의 원소이다.
:::

[정리 4](#thm4){: data-lid="hr62u" }의 증명. $B$를 $A$의 폐포라 하자. $B$가 닫혀 있으므로, 모든 $f \in C(X,\mathbb{R})$와 $\varepsilon > 0$에 대해 $\lVert f - g\rVert \leq \varepsilon$인 $g \in B$를 찾으면 충분하다. $X$가 한 점이면 어디서도 사라지지 않는 $A$는 $0$이 아닌 상수를 포함하고, 그 실수배가 $C(X,\mathbb{R}) = \mathbb{R}$ 전체이므로 자명하다. 이하 $X$는 두 점 이상이라 하자.

$x \in X$를 고정한다. 각 $y \neq x$에 대해 [보조정리 6](#lem6){: data-lid="911af" }으로 $g_y \in A$를 $g_y(x) = f(x)$, $g_y(y) = f(y)$가 되도록 잡고, 열린집합 $J_y = \{t \in X : g_y(t) > f(t) - \varepsilon\}$를 둔다. $x$와 $y$는 모두 $J_y$에 속하므로 $\{J_y\}_{y \neq x}$는 $X$의 열린 덮개이다. $X$가 컴팩트하므로 유한개의 $y_1, \dots, y_m$이 $X$를 덮고, $h_x = \max(g_{y_1}, \dots, g_{y_m})$로 두면 [보조정리 5](#lem5){: data-lid="uws62" }에 의해 $h_x \in B$이다. 구성에 의해 $h_x(x) = f(x)$이고, 모든 $t \in X$에 대해 $h_x(t) > f(t) - \varepsilon$이다.

이제 $x$를 움직인다. 열린집합 $V_x = \{t \in X : h_x(t) < f(t) + \varepsilon\}$는 $h_x(x) = f(x)$이므로 $x$를 포함하고, 따라서 $\{V_x\}_{x \in X}$는 $X$의 열린 덮개이다. 다시 compactness로 유한개의 $x_1, \dots, x_n$이 $X$를 덮고, $g = \min(h_{x_1}, \dots, h_{x_n}) \in B$로 두자. 모든 $t$에 대해 $g(t) > f(t) - \varepsilon$이고, $t \in V_{x_j}$인 $j$에서 $g(t) \leq h_{x_j}(t) < f(t) + \varepsilon$이다. 따라서 $\lVert f - g\rVert \leq \varepsilon$이다.

증명에서 compactness는 두 번, 열린 덮개에서 유한 부분덮개를 뽑는 데만 쓰였다. 이 유한성이 있어야 $\max$와 $\min$이 유한개의 함수에 대한 연산이 되어 $B$ 안에 머문다.

::: 따름정리 7
$A \subseteq C(X,\mathbb{R})$이 상수함수를 포함하고 점을 분리하는 subalgebra이면 $A$는 조밀하다. 특히 $K \subseteq \mathbb{R}^n$이 컴팩트이면, $n$변수 polynomial의 $K$ 위로의 제한 전체는 $C(K,\mathbb{R})$에서 조밀하다.
:::

::: 증명
앞 문장은 상수를 포함하는 subalgebra가 어디서도 사라지지 않음에서 [정리 4](#thm4){: data-lid="fyt4m" }로 따른다. polynomial은 상수를 포함하는 subalgebra이고, 서로 다른 $p, q \in K$는 어떤 좌표 $x_i$에서 $p_i \neq q_i$이므로 좌표함수 $x_i$가 둘을 구별한다.
:::

[따름정리 7](#cor7){: data-lid="iyphc" }의 $n = 1$, $K = [a,b]$인 경우가 [정리 2](#thm2){: data-lid="rdcyf" }이지만, 증명이 [정리 2](#thm2){: data-lid="pfie5" }를 쓰므로 이는 새로운 증명이 아니다.

## 복소판과 켤레에 대한 닫힘

복소수값 함수 $C(X,\mathbb{C})$에서는 subalgebra를 복소수배에 대해 닫힌 것으로, 점의 분리와 어디서도 사라지지 않음은 같은 방식으로 정의한다. 이때 실수판의 가정만으로는 결론이 성립하지 않으며, 켤레에 대한 닫힘이 추가로 필요하다.

::: 정리 8 (Stone–Weierstrass 정리, 복소판)
$X$가 컴팩트 거리공간이고 $A \subseteq C(X,\mathbb{C})$가 점을 분리하며 어디서도 사라지지 않는 subalgebra이고, $f \in A$이면 켤레 $\bar{f} \in A$이면, $A$는 $C(X,\mathbb{C})$에서 조밀하다.
:::

::: 증명
$A_{\mathbb{R}}$을 $A$의 실수값 원소 전체라 하면 $A_{\mathbb{R}}$은 $C(X,\mathbb{R})$의 subalgebra이다. $f = u + iv \in A$이면 $\bar{f} \in A$이므로 $u = (f + \bar{f})/2$와 $v = (f - \bar{f})/(2i)$가 모두 $A$에 속하고 실수값이므로 $A_{\mathbb{R}}$의 원소이다.

$A_{\mathbb{R}}$이 [정리 4](#thm4){: data-lid="tuk4b" }의 가정을 만족함을 보인다. 서로 다른 $x, y$에 대해 $f(x) \neq f(y)$인 $f = u + iv \in A$가 있으면 $u(x) \neq u(y)$ 또는 $v(x) \neq v(y)$이므로 $u$ 또는 $v$가 $x, y$를 분리한다. 마찬가지로 $f(x) \neq 0$인 $f \in A$에 대해 $u(x) \neq 0$ 또는 $v(x) \neq 0$이다. 따라서 [정리 4](#thm4){: data-lid="ggf0s" }에 의해 $A_{\mathbb{R}}$은 $C(X,\mathbb{R})$에서 조밀하다. 임의의 $g = g_1 + ig_2 \in C(X,\mathbb{C})$에 대해 $\lVert g_j - u_j\rVert < \varepsilon/2$인 $u_j \in A_{\mathbb{R}}$를 잡으면 $u_1 + iu_2 \in A$이고 $\lVert g - (u_1 + iu_2)\rVert < \varepsilon$이다.
:::

켤레에 대한 닫힘을 뺄 수 없다는 것은 다음 예가 보여 준다.

::: 예시 9
$X = \{z \in \mathbb{C} : \lvert z\rvert = 1\}$이고 $A$를 $z$의 계수가 복소수인 polynomial $p(z) = \sum_{k=0}^m c_kz^k$의 $X$ 위로의 제한 전체라 하자. $A$는 상수를 포함하는 subalgebra이고 $z$가 점을 분리하지만, 연속함수 $\bar{z}$를 근사하지 못한다. 실제로 $k \geq 0$이면

$$\int_0^{2\pi} e^{ik\theta}e^{i\theta}\dd{\theta} = 0$$

이므로 모든 $p \in A$에 대해 $\int_0^{2\pi} p(e^{i\theta})e^{i\theta}\dd{\theta} = 0$이다. 반면 $\overline{e^{i\theta}} e^{i\theta} = 1$이므로 $\bar{z}$에 대해서는 이 적분이 $2\pi$이다. 따라서 모든 $p \in A$에 대해

$$2\pi = \left\lvert\int_0^{2\pi}\left(\overline{e^{i\theta}} - p(e^{i\theta})\right)e^{i\theta}\dd{\theta}\right\rvert \leq 2\pi \lVert \bar{z} - p\rVert$$

이고 $\lVert \bar{z} - p\rVert \geq 1$이다. 제한은 상한노름을 키우지 않으므로, 닫힌 단위원판 $\{\lvert z\rvert \leq 1\}$ 위에서도 $z$의 polynomial은 $\bar{z}$로부터 거리 $1$ 이상에 있어 조밀하지 않다.
:::

증명이 실패하는 지점은 $A_{\mathbb{R}}$이다. 이 예에서 $A_{\mathbb{R}}$은 상수함수뿐이므로 점을 분리하지 못한다. 실수부 $\operatorname{Re}z$ 자체가 $A$에 없기 때문이다.

## 삼각다항식

연속이고 $2\pi$-주기적인 $f : \mathbb{R} \to \mathbb{C}$에 대해, $F(e^{i\theta}) = f(\theta)$로 단위원 $\mathbb{T} = \{\lvert z\rvert = 1\}$ 위의 함수 $F$를 정의한다. 주기성 때문에 $F$는 잘 정의되고, $e^{i\theta_0}$ 근방에서 $\theta \mapsto e^{i\theta}$가 $(\theta_0 - \pi, \theta_0 + \pi)$에서 $\mathbb{T}\setminus\{-e^{i\theta_0}\}$로의 homeomorphism이므로 $F$는 연속이다. 이 대응은 상한노름을 보존하는 일대일 대응 $C(\mathbb{T},\mathbb{C}) \cong \{$연속 $2\pi$-주기함수$\}$를 준다. $\mathbb{T}$가 컴팩트이므로 [정리 8](#thm8){: data-lid="cswvk" }을 쓸 수 있다.

*trigonometric polynomial<sub>삼각다항식</sub>*은 $T(\theta) = \sum_{k=-N}^N c_ke^{ik\theta}$ 꼴의 함수이다. $e^{ik\theta} = \cos k\theta + i\sin k\theta$이므로 이는 $\cos k\theta$, $\sin k\theta$의 일차결합과 같다.

::: 따름정리 10
$f$가 연속인 $2\pi$-주기함수이면, 임의의 $\varepsilon > 0$에 대해 trigonometric polynomial $T$가 존재하여 모든 $\theta \in \mathbb{R}$에 대해 $\lvert f(\theta) - T(\theta)\rvert < \varepsilon$이다. $f$가 실수값이면 $T$를 $a_0 + \sum_{k=1}^N (a_k\cos k\theta + b_k\sin k\theta)$, $a_k, b_k \in \mathbb{R}$ 꼴로 잡을 수 있다.
:::

::: 증명
$A$를 $\mathbb{T}$ 위의 함수 $z^k$ $(k \in \mathbb{Z})$의 일차결합 전체라 하자. $z^jz^k = z^{j+k}$이므로 $A$는 subalgebra이고, $\overline{z^k} = z^{-k}$이므로 켤레에 닫혀 있으며, 상수 $z^0 = 1$을 포함하고, $z$가 $\mathbb{T}$의 점을 분리한다. [정리 8](#thm8){: data-lid="busr7" }에 의해 $A$는 $C(\mathbb{T},\mathbb{C})$에서 조밀하고, 이를 $\theta$의 함수로 옮기면 첫째 주장이다. $f$가 실수값이면 $\lvert f - \operatorname{Re}T\rvert \leq \lvert f - T\rvert$이고 $\operatorname{Re}T$는 $\cos k\theta$, $\sin k\theta$의 실계수 일차결합이므로 둘째 주장도 성립한다.
:::

주기성은 필수이다. trigonometric polynomial $T$는 $T(0) = T(2\pi)$를 만족하므로, 구간 $[0,2\pi]$ 위의 연속함수 $f(\theta) = \theta$에 대해 $\lVert f - T\rVert \geq \max(\lvert T(0)\rvert, \lvert 2\pi - T(0)\rvert) \geq \pi$이다. $[0,2\pi]$ 위에서는 trigonometric polynomial이 $0$과 $2\pi$를 분리하지 못하므로 [정리 4](#thm4){: data-lid="umq79" }의 가정이 깨진다. 원 $\mathbb{T}$ 위에서는 두 점이 같은 점이다.

## 컴팩트하지 않은 정의역

[정리 2](#thm2){: data-lid="bofok" }는 임의의 컴팩트 구간 $[-R,R]$ 위에서 성립하지만, $R$이 $x$에 따라 커지는 것을 허용하지 않는다. 정의역 전체에서 균등한 근사는 컴팩트하지 않은 정의역에서는 일반적으로 불가능하다. 정리의 가정 중 polynomial 쪽은 아무것도 달라지지 않는다. polynomial은 여전히 상수를 포함하고 $x$로 점을 분리하는 subalgebra이다.

::: 예시 11
$X = \mathbb{R}$에서 $f(x) = \sin x$를 polynomial로 상한노름 $1/2$ 이내로 근사할 수 있다고 하자. $\lvert \sin x - p(x)\rvert < 1/2$이면 $p$는 $\mathbb{R}$ 위에서 bounded이고, bounded인 polynomial은 상수 $c$이다. 그러나 $\sin x = 1$인 점에서 $\lvert 1 - c\rvert < 1/2$, $\sin x = -1$인 점에서 $\lvert -1 - c\rvert < 1/2$이므로 $2 \leq \lvert 1 - c\rvert + \lvert 1 + c\rvert < 1$이 되어 모순이다.
:::

위 예는 근사 대상이 bounded인데도 실패하므로, 문제가 근사 대상이 bounded라는 점이 아니라 polynomial이 유한한 차수로 무한히 진동할 수 없다는 데 있음을 보여 준다. 정의역이 bounded이지만 닫혀 있지 않은 경우에도 같은 일이 일어난다.

::: 예시 12
$X = (0,1)$에서 bounded인 연속함수 $f(x) = \sin(1/x)$를 생각하자. 어떤 polynomial $p$가 $\lvert f - p\rvert < 1/2$을 모든 $x \in (0,1)$에서 만족한다고 하자. $p$는 $[0,1]$ 위의 연속함수이므로 $x \to 0$일 때 $p(x) \to p(0)$이다. 한편 $x_n = 1/(\pi/2 + 2n\pi)$에서 $f(x_n) = 1$이고 $y_n = 1/(3\pi/2 + 2n\pi)$에서 $f(y_n) = -1$이며 두 수열 모두 $0$으로 수렴한다. 따라서 $\lvert 1 - p(0)\rvert \leq 1/2$이고 $\lvert -1 - p(0)\rvert \leq 1/2$이어서 $2 \leq 1$이 되어 모순이다.
:::

두 예에서 [정리 4](#thm4){: data-lid="30e5y" }의 증명이 깨지는 곳은 열린 덮개에서 유한 부분덮개를 뽑는 단계이다. $\mathbb{R}$이나 $(0,1)$에서는 $J_y$의 유한 부분족이 $X$ 전체를 덮는다고 보장할 수 없고, 무한개의 $g_y$에 대한 상한은 더 이상 $A$의 폐포 안의 연속함수가 아니다.

---

**참고문헌**

**[Rud]** W. Rudin, *Principles of mathematical analysis*, 3rd ed., McGraw-Hill, 1976.
