---
title: "연결성과 중간값 정리"
description: "거리공간의 subset에 대한 connectedness를 정의하고, ℝ의 connected subset이 정확히 구간임을 증명한다. 연속함수가 connectedness를 보존함을 보여 중간값 정리를 얻고, fixed point와 홀수차 polynomial의 real root에 응용한다. path-connectedness와 topologist's sine curve로 두 개념이 다름을 확인한다."
excerpt: "connected set, 구간, 중간값 정리, path-connectedness"

categories: [Math / Analysis]
permalink: /ko/math/analysis/connectedness
sidebar: 
    nav: "analysis-ko"

date: 2026-06-02
weight: 13

published: false

---

[\[미적분학\] §연속함수, ⁋정리 5](/ko/math/calculus/continuity#thm5)는 연속함수의 그래프가 끊어지지 않는다는 직관과 함께 도구로 받아들여졌다. 이 직관이 실수의 어떤 성질에 의존하는지는 유리수 위에서 정리가 깨지는 데서 드러난다. $f(x) = x^2 - 2$는 $\mathbb{Q}$ 위의 연속함수이고 $f(0) = -2 < 0 < 2 = f(2)$이지만 $\mathbb{Q}$에는 $f$의 영점이 없다. 정의역에서 빠진 것은 $\sqrt{2}$ 하나이며, 이 한 점 때문에 $\mathbb{Q}\cap[0,2]$는 두 조각으로 갈라진다. 이 글에서는 갈라지지 않는다는 성질을 connectedness로 정식화하고, 그것이 연속함수에 의해 보존됨을 보여 중간값 정리를 얻는다.

## 연결집합

[§거리공간과 열린집합·닫힌집합, ⁋정의 1](/ko/math/analysis/metric_spaces#def1)의 거리공간 $X$와 $E \subseteq X$를 생각하자. $E$의 subset $A$가 *relatively open set*이라는 것은 $X$의 열린집합 $U$가 있어 $A = U \cap E$인 것이다. 이는 $E$를 그 자체로 거리공간으로 보았을 때의 [§거리공간과 열린집합·닫힌집합, ⁋정의 8](/ko/math/analysis/metric_spaces#def8)의 열린집합과 같다.

::: 정의 1
거리공간 $X$의 subset $E$가 *disconnected<sub>비연결</sub>*라는 것은, $E = A \cup B$이면서 $A$, $B$가 $E$의 서로소인 비어 있지 않은 relatively open set인 것이다. 이러한 분해가 존재하지 않을 때 $E$를 *connected<sub>연결</sub>*라 한다.
:::

$A$와 $B$가 서로소이면서 합집합이 $E$이므로 $A$는 $B$의 $E$에서의 여집합이고, 따라서 $A$와 $B$는 $E$ 안에서 닫힌집합이기도 하다. 그러므로 $E$가 connected라는 것은 $E$ 안에서 열려 있고 동시에 닫혀 있는 subset이 $\emptyset$과 $E$뿐이라는 것과 같다. 공집합과 한 점으로 이루어진 집합은 비어 있지 않은 두 조각으로 나눌 수 없으므로 connected이다.

분해를 만들 때 $A$, $B$를 $E$ 바깥의 열린집합으로 잡아도 되지만, $A \cap B = \emptyset$이어야 하는 곳은 $E$ 안이라는 점에 주의해야 한다. 가령 $\mathbb{R}$의 subset $[0,1]\cup[2,3]$은 $A = [0,1]$, $B = [2,3]$로 분해되며, 이 둘은 $\mathbb{R}$ 안에서는 열려 있지 않지만 $A = (-1, 3/2) \cap E$, $B = (3/2, 4) \cap E$로 쓰이므로 relatively open이다.

$\mathbb{R}$에서 connected인 집합이 무엇인지는 완전히 결정된다. $E \subseteq \mathbb{R}$이 *구간*이라는 것은 $x, y \in E$이고 $x < z < y$이면 $z \in E$인 것이다. 한 점, 공집합, 열린·닫힌·반열린 구간, ray, $\mathbb{R}$ 전체가 모두 이 조건을 만족한다.

::: 정리 2
$\mathbb{R}$의 subset $E$가 connected인 것은 $E$가 구간인 것과 동치이다.
:::

::: 증명
$E$가 구간이 아니라 하자. 그럼 $x, y \in E$와 $x < z < y$인 $z \notin E$가 있다. $A = E \cap (-\infty, z)$, $B = E \cap (z, \infty)$로 두면 둘 다 relatively open이고, $x \in A$, $y \in B$이며 $A \cap B = \emptyset$이다. $z \notin E$이므로 $A \cup B = E$이다. 따라서 $E$는 disconnected이다.

거꾸로 $E$가 구간이면서 $E = A \cup B$로 분해된다고 하자. $a \in A$, $b \in B$를 택하고, 필요하면 $A$와 $B$의 이름을 바꾸어 $a < b$라 하자. $E$가 구간이므로 $[a, b] \subseteq E$이다. 집합 $A \cap [a, b]$는 $a$를 포함하고 $b$로 위에서 유계이므로 [§실수의 완비성, ⁋정의 3](/ko/math/analysis/completeness_of_reals#def3)에 의하여 상한 $s = \sup (A \cap [a, b])$가 존재하고 $a \leq s \leq b$이다. 따라서 $s \in E$이며, $s \in A$이거나 $s \in B$이다.

$s \in A$인 경우를 보자. $b \in B$이고 $A \cap B = \emptyset$이므로 $s \neq b$, 즉 $s < b$이다. $A$가 relatively open이므로 어떤 $\delta > 0$에 대해 $(s - \delta, s + \delta) \cap E \subseteq A$이다. 이 $\delta$를 $s + \delta \leq b$가 되도록 줄이면 $(s, s + \delta) \subseteq [a, b] \subseteq E$이므로 $(s, s+\delta) \subseteq A \cap [a, b]$가 된다. 그런데 이 구간의 점은 $s$보다 크므로 $s$가 상한이라는 데 모순이다.

$s \in B$인 경우를 보자. $a \in A$이므로 $s \neq a$, 즉 $s > a$이다. $B$가 relatively open이므로 어떤 $\delta > 0$에 대해 $(s - \delta, s + \delta) \cap E \subseteq B$이고, $\delta \leq s - a$로 줄여 둘 수 있다. 그럼 $(s - \delta, s] \subseteq [a, b] \subseteq E$이므로 $(s - \delta, s] \subseteq B$이고, $A \cap B = \emptyset$이므로 이 구간은 $A$와 만나지 않는다. 따라서 $A \cap [a, b]$의 모든 원소는 $s - \delta$ 이하이고 $\sup (A \cap [a,b]) \leq s - \delta < s$가 되어 모순이다.

두 경우 모두 모순이므로 구간 $E$는 connected이다.
:::

[정리 2](#thm2)의 두 번째 방향이 [§실수의 완비성, ⁋정의 3](/ko/math/analysis/completeness_of_reals#def3)이 쓰이는 곳이다. 상한의 존재를 쓰지 않으면 증명이 성립하지 않으며, 실제로 $\mathbb{Q}$의 구간 $\mathbb{Q} \cap [0, 2]$는 위의 첫 방향의 논증에서처럼 $\sqrt{2}$로 갈라져 connected가 아니다. 이때 $\mathbb{Q} \cap [0,2]$는 $\mathbb{Q}$ 안에서 "$x < y < z$이면 $y$도 속한다"는 구간 조건을 만족하지만 이 조건이 $\mathbb{R}$의 구간과 달리 connectedness를 보장하지 못한다.

## 연속함수와 중간값 정리

Compactness가 연속함수에 의해 보존되었듯([§연속함수의 성질, ⁋정리 1](/ko/math/analysis/continuous_functions#thm1)) connectedness도 보존된다. 증명의 착상은 image에서의 분해를 preimage로 끌어올려 정의역의 분해를 만드는 것이다. 연속함수에서는 열린집합의 preimage가 열려 있다([§함수의 극한과 연속, ⁋명제 5](/ko/math/analysis/limits_and_continuity#prop5)).

::: 정리 3
$f : X \rightarrow Y$가 거리공간 사이의 연속함수이고 $E \subseteq X$가 connected이면 $f(E)$도 connected이다.
:::

::: 증명
$f(E)$가 connected가 아니라 하고 $f(E) = A \cup B$를 서로소인 비어 있지 않은 relatively open set으로의 분해라 하자. $Y$의 열린집합 $U$, $V$로 $A = U \cap f(E)$, $B = V \cap f(E)$라 쓰고,

$$A' = \{x \in E \mid f(x) \in A\} = E \cap f^{-1}(U), \quad B' = \{x \in E \mid f(x) \in B\} = E \cap f^{-1}(V)$$

로 두자. $f$가 연속이므로 $f^{-1}(U)$, $f^{-1}(V)$는 $X$의 열린집합이고 $A'$, $B'$는 $E$의 relatively open set이다. $A$가 비어 있지 않으므로 $f(x) \in A$인 $x \in E$가 있어 $A' \neq \emptyset$이고, 같은 이유로 $B' \neq \emptyset$이다. $E$의 각 점은 $f$에 의해 $A$나 $B$로 가므로 $A' \cup B' = E$이고, $A \cap B = \emptyset$이므로 $A' \cap B' = \emptyset$이다. 이는 $E$가 connected라는 가정에 모순이다.
:::

[정리 2](#thm2)와 [정리 3](#thm3)을 합치면 중간값 정리가 나온다. 여기서 두 실수 $u, v$에 대해 $y$가 $u$와 $v$ 사이에 있다는 것은 $\min\{u, v\} \leq y \leq \max\{u, v\}$인 것으로 약속한다.

::: 따름정리 4 (중간값 정리)
$I \subseteq \mathbb{R}$가 구간이고 $f : I \rightarrow \mathbb{R}$가 연속이면 다음이 성립한다.

1. $f(I)$는 구간이다.
2. $a, b \in I$이고 $y$가 $f(a)$와 $f(b)$ 사이에 있으면, $a$와 $b$ 사이의 $c$로서 $f(c) = y$인 것이 존재한다.
:::

::: 증명
(1) [정리 2](#thm2)에 의해 $I$는 connected이고, [정리 3](#thm3)에 의해 $f(I)$는 connected이므로, 다시 [정리 2](#thm2)에 의해 구간이다.

(2) $a \leq b$라 하자. $[a, b]$는 $I$에 포함되는 구간이므로 (1)을 $f$의 $[a,b]$로의 제한에 적용하면 $f([a, b])$가 구간이다. 이 구간은 $f(a)$와 $f(b)$를 포함하므로 그 사이의 $y$도 포함하고, 따라서 $f(c) = y$인 $c \in [a, b]$가 있다. $b < a$이면 역할을 바꾸면 된다.
:::

이 증명에서 연속성은 [정리 3](#thm3)에서, 정의역의 구조는 [정리 2](#thm2)에서 쓰였고 둘이 독립적으로 기여한다. 따라서 정의역이 구간이라는 가정을 빼면 결론이 깨진다. $f : [0, 1]\cup[2, 3] \rightarrow \mathbb{R}$를 $[0,1]$에서 $0$, $[2,3]$에서 $1$로 두면 $f$는 연속이지만 $1/2$를 취하지 않는다. 앞서 본 $\mathbb{Q}$ 위의 $x^2 - 2$도 같은 현상이다.

한편 [따름정리 4](#cor4)의 역, 곧 구간을 구간으로 보내는 함수가 연속이라는 명제는 성립하지 않는다.

::: 예시 5
$f : \mathbb{R} \rightarrow \mathbb{R}$를 $x \neq 0$에서 $f(x) = \sin(1/x)$, $f(0) = 0$으로 정의하자. $f$는 $0$에서 연속이 아니지만 모든 구간 $J$에 대해 $f(J)$는 구간이다.

실제로 $0 \notin J$이면 $f$가 $J$ 위에서 연속이므로 [따름정리 4](#cor4)의 (1)에 의해 $f(J)$가 구간이다. $J = \{0\}$이면 $f(J) = \{0\}$이다. 그 외의 경우 $J$는 $0$과 다른 한 점을 포함하는 구간이므로 어떤 $\varepsilon > 0$에 대해 $(0, \varepsilon) \subseteq J$ 또는 $(-\varepsilon, 0) \subseteq J$이다. 앞의 경우를 보자. $k$가 충분히 크면 $x = 1/(\pi/2 + 2\pi k)$와 $x = 1/(3\pi/2 + 2\pi k)$가 $(0, \varepsilon)$에 속하고 이 점들에서 $f$의 값은 각각 $1$, $-1$이다. $f$는 $(0, \varepsilon)$에서 연속이므로 $f((0,\varepsilon))$은 $-1$과 $1$을 포함하는 구간이고, $f(J) \subseteq [-1, 1]$이므로 $f(J) = [-1, 1]$이다. 뒤의 경우도 같다.
:::

즉 중간값 성질은 연속성보다 약한 조건이다. [따름정리 4](#cor4)를 쓸 때에는 연속성을 어디서 확인했는지를 구간 전체에서 점검해야 하며, 사잇값을 취한다는 사실로부터 연속성을 거꾸로 이끌어서는 안 된다.

## 응용

중간값 정리의 직접적인 쓰임은 방정식의 해의 존재이다. 연속함수가 두 점에서 서로 다른 부호를 가지면 그 사이에서 $0$을 지난다. 이를 이용하면 다음을 얻는다.

::: 명제 6
$f : [0, 1] \rightarrow [0, 1]$이 연속이면 $f(c) = c$인 $c \in [0, 1]$이 존재한다.
:::

::: 증명
$g(x) = f(x) - x$는 $[0, 1]$에서 연속이다. $f$의 치역이 $[0,1]$에 포함되므로 $g(0) = f(0) \geq 0$이고 $g(1) = f(1) - 1 \leq 0$이다. 따라서 $0$은 $g(0)$과 $g(1)$ 사이에 있고, [따름정리 4](#cor4)의 (2)에 의해 $g(c) = 0$인 $c \in [0, 1]$이 존재한다.
:::

정의역과 공역이 같은 구간 $[0,1]$이라는 가정이 모두 쓰인다. $f(x) = x + 1$은 $\mathbb{R}$ 위에서 연속이지만 fixed point가 없고, $f(x) = x/2$는 $(0, 1]$을 자기 자신으로 보내지 않는다. 구간 $(0,1)$에서 $f(x) = x^2$은 $(0, 1)$을 자기 자신으로 보내지만 $f(x) = x$의 해는 $0$, $1$뿐이어서 fixed point가 없다. 닫힌구간이 필요한 이유는 위 증명이 $g(0) \geq 0$, $g(1) \leq 0$이라는 끝점에서의 값에 의존하기 때문이다.

::: 명제 7
홀수 $n$에 대하여 실계수 $n$차 polynomial $p$는 real root를 가진다.
:::

::: 증명
최고차 계수로 나누어 $p(x) = x^n + a_{n-1} x^{n-1} + \cdots + a_0$이라 해도 root는 변하지 않는다. $R = 1 + \sum_{i=0}^{n-1} \lvert a_i\rvert$로 두고 $\lvert x\rvert \geq R$이라 하자. $R > 1$이므로 $\lvert x\rvert \geq 1$이고 $i \leq n - 1$에 대해 $\lvert x\rvert^i \leq \lvert x\rvert^{n-1}$이므로

$$\Bigl\lvert \sum_{i=0}^{n-1} a_i x^i \Bigr\rvert \leq \Bigl(\sum_{i=0}^{n-1} \lvert a_i\rvert\Bigr)\lvert x\rvert^{n-1} < R \lvert x\rvert^{n-1} \leq \lvert x\rvert^n$$

이 성립한다. 두 번째 부등식은 $\sum \lvert a_i\rvert < R$과 $\lvert x\rvert^{n-1} > 0$에서, 마지막 부등식은 $\lvert x\rvert \geq R$에서 나온다. 따라서 $x = R$에서 $p(R) \geq R^n - \bigl\lvert \sum a_i R^i\bigr\rvert > 0$이다. $n$이 홀수이므로 $x = -R$에서는 $(-R)^n = -R^n$이고 $p(-R) \leq -R^n + \bigl\lvert \sum a_i (-R)^i\bigr\rvert < 0$이다. $p$는 $[-R, R]$에서 연속이고 $0$은 $p(-R)$과 $p(R)$ 사이에 있으므로 [따름정리 4](#cor4)의 (2)에 의해 $p(c) = 0$인 $c$가 존재한다.
:::

짝수차 polynomial에서는 두 끝에서 부호가 같아 위 논증이 작동하지 않으며, $x^2 + 1$이 real root가 없는 예이다.

## 경로연결

Connectedness를 확인하는 가장 직접적인 방법은 두 점을 집합 안의 곡선으로 잇는 것이다.

::: 정의 8
거리공간의 subset $E$가 *path-connected<sub>경로연결</sub>*라는 것은, 임의의 $x, y \in E$에 대해 연속함수 $\gamma : [0, 1] \rightarrow X$로서 $\gamma([0,1]) \subseteq E$, $\gamma(0) = x$, $\gamma(1) = y$인 것이 존재하는 것이다.
:::

$\mathbb{R}^n$의 볼록집합 $E$는 $\gamma(t) = (1-t)x + ty$가 $E$ 안에 머무르므로 path-connected이다. 이 정의로부터 connectedness가 곧바로 따라 나온다.

::: 명제 9
Path-connected인 집합은 connected이다.
:::

::: 증명
$E$가 path-connected이면서 $E = A \cup B$가 서로소인 비어 있지 않은 relatively open set으로의 분해라 하자. $A = U \cap E$, $B = V \cap E$인 열린집합 $U, V$를 잡는다. $x \in A$, $y \in B$를 택하고 $\gamma(0) = x$, $\gamma(1) = y$, $\gamma([0,1]) \subseteq E$인 연속함수 $\gamma$를 잡자. $\gamma$의 image가 $E$에 포함되므로 $\gamma^{-1}(A) = \gamma^{-1}(U)$, $\gamma^{-1}(B) = \gamma^{-1}(V)$이고 이들은 $[0,1]$의 열린집합이다. 이 둘은 $0$과 $1$을 각각 포함하여 비어 있지 않고, $A \cap B = \emptyset$이므로 서로소이며, 합집합은 $[0,1]$이다. 이는 $[0,1]$이 connected라는 [정리 2](#thm2)에 모순이다.
:::

역은 성립하지 않는다. 이를 보이는 표준적인 예가 topologist's sine curve이며, 증명에 [정리 3](#thm3)과 [따름정리 4](#cor4)가 모두 쓰인다. 먼저 connectedness가 closure로 전달됨을 확인하자.

::: 보조정리 10
$G$가 거리공간 $X$의 connected subset이고 $G \subseteq S \subseteq \overline{G}$이면 $S$도 connected이다.
:::

::: 증명
$S = A \cup B$가 서로소인 비어 있지 않은 relatively open set으로의 분해라 하자. $A \cap G$와 $B \cap G$는 $G$의 서로소인 relatively open set이고 합집합이 $G$이다. $G$가 connected이므로 둘 중 하나가 비어 있어야 하며, 일반성을 잃지 않고 $B \cap G = \emptyset$이라 하자. $b \in B$를 택하고 $X$의 열린집합 $V$로 $B = V \cap S$라 쓰면 $V$는 $b$의 이웃이다. $b \in S \subseteq \overline{G}$이므로 $V$는 $G$의 점 $g$를 포함하고, $G \subseteq S$이므로 $g \in V \cap S = B$이다. 이는 $B \cap G = \emptyset$에 모순이다.
:::

::: 예시 11 (topologist's sine curve)
$\mathbb{R}^2$에서 $G = \{(x, \sin(1/x)) \mid 0 < x \leq 1\}$, $L = \{0\} \times [-1, 1]$, $S = G \cup L$이라 하자. 그럼 $S$는 connected이지만 path-connected가 아니다.

*Connected임.* $G$는 구간 $(0, 1]$의 연속함수 $x \mapsto (x, \sin(1/x))$에 의한 image이므로 [정리 2](#thm2), [정리 3](#thm3)에 의해 connected이다. $G \subseteq S$이므로 $S \subseteq \overline{G}$만 보이면 [보조정리 10](#lem10)이 적용된다. $(0, y) \in L$에 대해 $\theta = \arcsin y \in [-\pi/2, \pi/2]$로 두고 $x_k = 1/(\theta + 2\pi k)$ ($k \geq 1$)로 놓자. $\theta + 2\pi k \geq 3\pi/2 > 1$이므로 $x_k \in (0, 1]$이고 $\sin(1/x_k) = \sin\theta = y$이다. $x_k \rightarrow 0$이므로 $(x_k, y) \in G$가 $(0, y)$로 수렴하여 $(0, y) \in \overline{G}$이다.

*Path-connected가 아님.* $\gamma = (\gamma_1, \gamma_2) : [0,1] \rightarrow S$가 연속이고 $\gamma(0) = (0, 0) \in L$, $\gamma(1) = (1, \sin 1) \in G$라 하자. 집합 $\{t \mid \gamma_1(t) = 0\}$은 닫혀 있고 $0$을 포함하며 $1$을 포함하지 않으므로, 그 상한 $t^\ast$는 이 집합에 속하고 $t^\ast < 1$이다. $\gamma_1(t^\ast) = 0$이므로 $\gamma(t^\ast) \in L$이고 $y_0 = \gamma_2(t^\ast)$로 놓는다. $t > t^\ast$이면 $\gamma_1(t) > 0$이므로 $\gamma(t) \in G$, 곧 $\gamma_2(t) = \sin(1/\gamma_1(t))$이다.

$\gamma$가 $t^\ast$에서 연속이므로 $\delta > 0$이 있어 $\lvert t - t^\ast\rvert < \delta$이면 $\lvert \gamma_2(t) - y_0\rvert < 1$이다. $t_1 \in (t^\ast, t^\ast + \delta) \cap [0,1]$을 하나 잡고 $c = \gamma_1(t_1) > 0$이라 하자. $\gamma_1$은 $[t^\ast, t_1]$에서 연속이고 $\gamma_1(t^\ast) = 0$, $\gamma_1(t_1) = c$이므로 [따름정리 4](#cor4)의 (2)에 의해 $[0, c]$의 모든 값을 취한다. $k$를 $2\pi k + \pi/2 > 1/c$가 되도록 크게 잡으면 $x_+ = 1/(2\pi k + \pi/2)$와 $x_- = 1/(2\pi k + 3\pi/2)$가 모두 $(0, c)$에 속하므로, $\gamma_1(u_\pm) = x_\pm$인 $u_\pm \in (t^\ast, t_1)$이 있다. 그럼 $\gamma_2(u_+) = \sin(2\pi k + \pi/2) = 1$, $\gamma_2(u_-) = \sin(2\pi k + 3\pi/2) = -1$이고 둘 다 $y_0$에서 거리가 $1$ 미만이어야 하는데, $1 - (-1) = 2$이므로 불가능하다. 따라서 $(0,0)$과 $(1, \sin 1)$을 잇는 path는 없다.
:::

$S$의 두 부분 $G$와 $L$은 각각 path-connected이고 서로 닿아 있지만, $L$ 근처에서 $G$가 무한히 진동하기 때문에 path가 $L$에서 $G$로 빠져나올 방법이 없다. Connectedness는 분해가 없음만을 요구하므로 이 진동을 문제 삼지 않는다.

---

**참고문헌**

**[Rud]** W. Rudin, *Principles of mathematical analysis*, 3rd ed., McGraw-Hill, 1976.
