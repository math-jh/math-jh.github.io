---
title: "Riemann–Stieltjes 적분"
description: "증가함수 α에 대한 Darboux 상합과 하합으로 Riemann–Stieltjes 적분을 정의하고, 판정법과 연속함수의 적분가능성을 증명한다. α가 계단함수이면 유한합으로, C¹이면 Riemann 적분 ∫fα'dx로 환원됨을 보이고, f와 α가 같은 쪽으로 불연속인 점에서 적분이 존재하지 않는 반례와 부분적분, 확률분포의 기댓값 ∫g dF, 유계변동함수까지 다룬다."
excerpt: "증가함수에 대한 적분의 정의, 계단함수와 C¹ 함수로의 환원, 부분적분, 기댓값, 유계변동함수"

categories: [Math / Analysis]
permalink: /ko/math/analysis/riemann_stieltjes_integral
sidebar: 
    nav: "analysis-ko"

date: 2026-10-13
weight: 19

published: false

---

[\[미적분학\] §적분, ⁋정의 9](/ko/math/calculus/integration#def9){: data-lid="vqxgg" }의 Riemann 합 $\sum f(t_i)\Delta x_i$에서 각 부분구간 $[x_{i-1}, x_i]$는 길이 $\Delta x_i$만큼의 비중으로 기여한다. 비중을 길이가 아닌 다른 양으로 바꾸면 적분의 용도가 크게 넓어진다. 막대 $[a,b]$ 위에 질량이 분포해 있고 $\alpha(x)$가 $[a,x]$에 놓인 질량이라 하자. 부분구간 $[x_{i-1}, x_i]$의 질량은 $\alpha(x_i) - \alpha(x_{i-1})$이므로, 위치 $x$의 함수 $f(x)$를 질량으로 가중해 모두 더한 양은 $\sum f(t_i)(\alpha(x_i) - \alpha(x_{i-1}))$로 근사된다. 질량이 밀도 함수로 주어지면 이 합은 Riemann 합과 다르지 않다. 그러나 한 점에 질량이 몰려 있으면 그 점의 밀도는 존재하지 않고, $\alpha$는 그 점에서 값이 점프한다. 길이 대신 $\alpha$의 증분을 쓰는 적분은 이런 경우까지 한 식으로 다룬다. 확률분포의 기댓값이 같은 구조를 갖는다.

## 정의와 상합·하합

이 글에서 $\alpha$는 $[a,b]$ 위의 *increasing function*, 곧 $x \leq y$이면 $\alpha(x) \leq \alpha(y)$인 함수이다. $\alpha$의 증분이 음이 아니라는 사실이 [§Riemann 적분, ⁋정의 1](/ko/math/analysis/riemann_integral#def1){: data-lid="6gexr" }의 상합·하합 논법을 그대로 가져올 수 있는 이유이다.

::: 정의 1 (Riemann–Stieltjes 적분)
$[a,b]$의 분할 $P = \{x_0 < x_1 < \cdots < x_n\}$($x_0 = a$, $x_n = b$)과 bounded function $f : [a,b] \to \mathbb{R}$에 대하여 $I_i = [x_{i-1}, x_i]$, $\Delta\alpha_i = \alpha(x_i) - \alpha(x_{i-1}) \geq 0$, $m_i = \inf_{I_i} f$, $M_i = \sup_{I_i} f$로 두고

$$L(P, f, \alpha) = \sum_{i=1}^n m_i \Delta\alpha_i, \qquad U(P, f, \alpha) = \sum_{i=1}^n M_i \Delta\alpha_i$$

를 각각 *하합<sub>lower sum</sub>*, *상합<sub>upper sum</sub>*이라 한다. 

$$\underline{\int_a^b} f\dd{\alpha} = \sup_P L(P, f, \alpha), \qquad \overline{\int_a^b} f\dd{\alpha} = \inf_P U(P, f, \alpha)$$

가 같을 때 $f$는 $\alpha$에 대하여 *Riemann–Stieltjes 적분가능*하다고 하고, $f \in \mathcal{R}(\alpha)$로 적는다. 공통값을 $\int_a^b f\dd{\alpha}$로 적는다.
:::

$\alpha(x) = x$이면 $\Delta\alpha_i = \Delta x_i$이므로 위 정의는 [§Riemann 적분, ⁋정의 4](/ko/math/analysis/riemann_integral#def4){: data-lid="h5iaj" }와 일치한다. 한편 $\alpha$가 증가함수라는 가정을 빼면 $\Delta\alpha_i$의 부호가 섞여 $L \leq U$가 깨지므로 상합과 하합으로 정의할 수 없다. 이 경우는 마지막 절에서 다룬다.

::: 보조정리 2 (세분)
$P \subseteq P'$이면 $L(P, f, \alpha) \leq L(P', f, \alpha)$이고 $U(P', f, \alpha) \leq U(P, f, \alpha)$이다.
:::

::: 증명
점 하나를 더하는 경우를 보이면 충분하다. 더해지는 점 $c$가 $x_{j-1} < c < x_j$를 만족한다고 하자. 하합에서 달라지는 항은 $m_j \Delta\alpha_j$ 하나이고, 이것이 $m' = \inf_{[x_{j-1}, c]} f$, $m'' = \inf_{[c, x_j]} f$를 쓴 두 항으로 갈라진다. 더 작은 집합 위의 infimum은 줄어들지 않으므로 $m', m'' \geq m_j$이고, $\alpha(c) - \alpha(x_{j-1})$와 $\alpha(x_j) - \alpha(c)$가 모두 음이 아니므로

$$\begin{aligned}
m'(\alpha(c) - \alpha(x_{j-1})) + m''(\alpha(x_j) - \alpha(c)) &\geq m_j(\alpha(c) - \alpha(x_{j-1})) + m_j(\alpha(x_j) - \alpha(c)) \\
&= m_j \Delta\alpha_j
\end{aligned}$$

이다. 상합은 $U(P, f, \alpha) = -L(P, -f, \alpha)$이므로 같은 방식으로 따른다.
:::

임의의 두 분할 $P, Q$에 대하여 $L(P, f, \alpha) \leq L(P \cup Q, f, \alpha) \leq U(P \cup Q, f, \alpha) \leq U(Q, f, \alpha)$이다. 따라서 하합들은 모두 상합 하나 아래에 있고, $\underline{\int} f\dd{\alpha} \leq \overline{\int} f\dd{\alpha}$이다.

::: 정리 3 (Riemann 판정법)
Bounded function $f$에 대하여 $f \in \mathcal{R}(\alpha)$인 것은 모든 $\varepsilon > 0$에 대하여 $U(P, f, \alpha) - L(P, f, \alpha) < \varepsilon$인 분할 $P$가 존재하는 것과 동치이다.
:::

::: 증명
($\Leftarrow$) 그런 $P$에 대하여 $L(P, f, \alpha) \leq \underline{\int} f\dd{\alpha} \leq \overline{\int} f\dd{\alpha} \leq U(P, f, \alpha)$이므로 $0 \leq \overline{\int} - \underline{\int} < \varepsilon$이다. $\varepsilon$이 임의이므로 두 적분은 같다.

($\Rightarrow$) 공통값을 $I$라 하자. Supremum과 infimum의 정의에 의하여 $L(P_1, f, \alpha) > I - \varepsilon/2$, $U(P_2, f, \alpha) < I + \varepsilon/2$인 분할 $P_1, P_2$가 있다. 두 부등식의 오차를 합쳐 $\varepsilon$이 되도록 $\varepsilon/2$씩 잡은 것이다. $P = P_1 \cup P_2$로 두면 [보조정리 2](#lem2){: data-lid="ptr0b" }에 의하여 $U(P, f, \alpha) - L(P, f, \alpha) \leq U(P_2, f, \alpha) - L(P_1, f, \alpha) < \varepsilon$이다.
:::

위 증명에서 $U - L$은 분할을 세분할수록 줄어든다. 따라서 $\varepsilon$에 대한 분할 $P$를 하나 찾으면 $P$의 모든 세분 $P'$에 대하여도 $U(P', f, \alpha) - L(P', f, \alpha) < \varepsilon$이다. 이때 $P'$의 각 $I_i$에서 점 $t_i$를 임의로 골라 만든 합 $\sum f(t_i)\Delta\alpha_i$는 $L(P', f, \alpha)$와 $U(P', f, \alpha)$ 사이에 있고 $\int f\dd{\alpha}$도 그 사이에 있으므로, 둘의 차는 $\varepsilon$보다 작다.

## 적분가능한 함수

::: 정리 4 (연속함수)
$f$가 $[a,b]$에서 연속이면 임의의 증가함수 $\alpha$에 대하여 $f \in \mathcal{R}(\alpha)$이다.
:::

::: 증명
$A = \alpha(b) - \alpha(a) \geq 0$이라 하고 $\varepsilon > 0$이 주어졌다고 하자. $\eta = \varepsilon/(A+1)$로 둔다. 분모에 1을 더한 것은 $A = 0$인 경우를 따로 다루지 않기 위해서이고, $\eta A < \varepsilon$이 되도록 하는 것이 목적이다. $[a,b]$는 compact이므로 $f$는 uniformly continuous이다([§연속함수의 성질, ⁋정리 6](/ko/math/analysis/continuous_functions#thm6){: data-lid="ow86z" }). 따라서 $\lvert x - y\rvert < \delta$이면 $\lvert f(x) - f(y)\rvert < \eta$인 $\delta > 0$이 있다. $\lVert P\rVert < \delta$인 분할 $P$를 잡으면 각 $I_i$에서 $M_i - m_i \leq \eta$이고,

$$U(P, f, \alpha) - L(P, f, \alpha) = \sum_{i=1}^n (M_i - m_i)\Delta\alpha_i \leq \eta \sum_{i=1}^n \Delta\alpha_i = \eta A < \varepsilon$$

이다. [정리 3](#thm3){: data-lid="9ddju" }에 의하여 $f \in \mathcal{R}(\alpha)$이다.
:::

적분가능성은 $\alpha$가 무엇이냐에 따라 달라진다. 연속함수는 모든 $\alpha$에 대하여 적분가능하지만, 불연속점이 있는 $f$는 $\alpha$에 따라 적분가능할 수도, 아닐 수도 있다. 이는 뒤의 절에서 구체적으로 본다. 다음으로, 적분이 적분기 $\alpha$에 대하여 선형임을 확인해 두자.

::: 명제 5 (적분기에 대한 선형성)
$\alpha_1, \alpha_2$가 증가함수이고 $f \in \mathcal{R}(\alpha_1) \cap \mathcal{R}(\alpha_2)$이면 $f \in \mathcal{R}(\alpha_1 + \alpha_2)$이고

$$\int_a^b f\dd{(\alpha_1 + \alpha_2)} = \int_a^b f\dd{\alpha_1} + \int_a^b f\dd{\alpha_2}$$

이다.
:::

::: 증명
$\Delta(\alpha_1 + \alpha_2)_i = \Delta(\alpha_1)_i + \Delta(\alpha_2)_i$이고 $m_i, M_i$는 $\alpha$와 무관하므로 모든 분할 $P$에 대하여 $U(P, f, \alpha_1 + \alpha_2) = U(P, f, \alpha_1) + U(P, f, \alpha_2)$이고 하합도 같다. $\varepsilon > 0$이 주어졌을 때 [정리 3](#thm3){: data-lid="7e19m" }에서 얻은 $\alpha_1, \alpha_2$에 대한 분할의 합집합을 $P$라 하면, 세분에서 $U - L$이 줄어드므로 $U(P, f, \alpha_k) - L(P, f, \alpha_k) < \varepsilon$이 $k = 1, 2$에 대하여 성립한다. 그럼 $U(P, f, \alpha_1 + \alpha_2) - L(P, f, \alpha_1 + \alpha_2) < 2\varepsilon$이므로 $f \in \mathcal{R}(\alpha_1 + \alpha_2)$이다. 또 $\int f\dd{(\alpha_1 + \alpha_2)}$와 $\int f\dd{\alpha_1} + \int f\dd{\alpha_2}$는 모두 $L(P, f, \alpha_1 + \alpha_2)$와 $U(P, f, \alpha_1 + \alpha_2)$ 사이에 있으므로 차가 $2\varepsilon$보다 작고, $\varepsilon$이 임의이므로 같다.
:::

## 계단함수에 대한 적분

$\alpha$의 변화가 몇 개의 점에서만 일어나면 적분은 유한합이 된다. $a \leq s_1 < \cdots < s_N \leq b$이고 $\alpha$가 $[a, s_1)$, $(s_1, s_2)$, $\ldots$, $(s_N, b]$의 각 구간에서 상수일 때 $\alpha$를 *계단함수<sub>step function</sub>*라 부른다. 각 $s_k$에서의 점프를 $c_k = \alpha(s_k+) - \alpha(s_k-)$로 적는다. 단 양 끝에서는 $\alpha(a-) = \alpha(a)$, $\alpha(b+) = \alpha(b)$로 약속한다. 점프의 크기에는 $s_k$에서의 값 $\alpha(s_k)$가 들어가지 않는다는 점에 주의하자. $\alpha(s_k)$는 $\alpha(s_k-)$와 $\alpha(s_k+)$ 사이의 어느 값이어도 된다.

::: 정리 6 (계단함수에 대한 적분)
$\alpha$가 위와 같은 계단함수이고 bounded function $f$가 각 $s_k$에서 연속이면 $f \in \mathcal{R}(\alpha)$이고

$$\int_a^b f\dd{\alpha} = \sum_{k=1}^N c_k f(s_k)$$

이다.
:::

::: 증명
$S = \sum_k c_k f(s_k)$, $C = \sum_k c_k = \alpha(b) - \alpha(a)$라 하자. $\eta > 0$이 주어졌을 때, $f$가 각 $s_k$에서 연속이므로 $\lvert x - s_k\rvert < \delta$이면 $\lvert f(x) - f(s_k)\rvert < \eta$인 $\delta > 0$이 있다. 필요하면 $\delta$를 줄여 $2\delta$가 인접한 $s_k$ 사이의 간격 중 가장 짧은 것보다 작도록 하자. $P$를 $a$, $b$, 각 $s_k$, 그리고 $[a,b]$ 안에 있는 $s_k \pm \delta/2$로 이루어진 분할이라 하자.

$\alpha$는 각 구간 $(s_k, s_{k+1})$에서 상수이므로, 양 끝점이 모두 같은 열린 구간에 있는 부분구간에서는 $\Delta\alpha_i = 0$이다. $\Delta\alpha_i \neq 0$일 수 있는 부분구간은 $s_k$의 바로 앞 구간 $[s_k - \delta/2, s_k]$와 바로 뒤 구간 $[s_k, s_k + \delta/2]$뿐이고, 두 구간의 증분의 합은 $\alpha(s_k+) - \alpha(s_k-) = c_k$이다. 두 구간 위에서 $f(s_k) - \eta \leq f \leq f(s_k) + \eta$이므로 이 항들의 기여는 $[c_k(f(s_k) - \eta), c_k(f(s_k) + \eta)]$에 있고, 따라서

$$S - \eta C \leq L(P, f, \alpha) \leq U(P, f, \alpha) \leq S + \eta C$$

이다. 그럼 $S - \eta C \leq \underline{\int} f\dd{\alpha} \leq \overline{\int} f\dd{\alpha} \leq S + \eta C$이고 $\eta$가 임의이므로 두 적분은 모두 $S$이다.
:::

이 정리에서 $f$의 연속성은 $\alpha$가 점프하는 점에서만 필요하고, 다른 점에서 $f$가 얼마나 거칠어도 상관없다. 이는 $\alpha$가 그 밖의 점에서는 증분을 만들지 않기 때문이다. 가령 $\alpha = \lfloor x \rfloor$를 $[0, n]$ 위에서 생각하면 $\alpha$는 $1, 2, \ldots, n$에서 크기 1로 점프하므로, $f(x) = x^2$에 대하여 $\int_0^n x^2\dd{\lfloor x \rfloor} = 1 + 4 + \cdots + n^2$이다. $\lfloor x \rfloor$는 거의 모든 점에서 도함수가 0이지만 이 적분은 0이 아니다. $\int f\dd{\alpha}$를 "$\int f\alpha'\dd{x}$"로 읽는 것은 $\alpha$가 미분가능할 때만 허용된다.

[정리 6](#thm6){: data-lid="606t8" }의 가정 "$f$가 점프하는 점에서 연속"을 단순히 "$f$와 $\alpha$가 같은 점에서 동시에 불연속이 아님"으로 읽어서는 안 된다. 실제로 필요한 조건은 방향까지 고려한 것이고, 이를 두 단계로 나누어 확인한다. 먼저 같은 쪽으로 불연속이면 적분이 존재하지 않는다.

::: 명제 7 (같은 쪽으로의 불연속)
$\alpha$를 증가함수, $f$를 bounded function이라 하자. $c \in [a, b)$에서 $\alpha(c+) > \alpha(c)$이고 $f$가 $c$에서 오른쪽 연속이 아니면 $f \notin \mathcal{R}(\alpha)$이다. 마찬가지로 $c \in (a, b]$에서 $\alpha(c-) < \alpha(c)$이고 $f$가 $c$에서 왼쪽 연속이 아니면 $f \notin \mathcal{R}(\alpha)$이다.
:::

::: 증명
오른쪽의 경우만 보이면 되고, 왼쪽은 $x \mapsto -x$로 구간을 뒤집어 같은 논증을 적용한다. $\delta = \alpha(c+) - \alpha(c) > 0$이라 하자. $f$가 $c$에서 오른쪽 연속이 아니므로 어떤 $\eta > 0$이 있어, 모든 $h > 0$에 대하여 $\lvert f(x) - f(c)\rvert \geq \eta$인 $x \in (c, c+h)$가 존재한다. 임의의 분할 $P$에 대하여 $U(P, f, \alpha) - L(P, f, \alpha) \geq \eta\delta$임을 보이면 [정리 3](#thm3){: data-lid="3j48y" }에 모순이다.

$c$가 $P$의 분할점 $x_j$인 경우를 먼저 보자. 부분구간 $[c, x_{j+1}]$에서 $\Delta\alpha_{j+1} = \alpha(x_{j+1}) - \alpha(c) \geq \alpha(c+) - \alpha(c) = \delta$이고, $M_{j+1} - m_{j+1} \geq \lvert f(x) - f(c)\rvert \geq \eta$인 $x \in (c, x_{j+1})$가 있다. 다른 항은 음이 아니므로 $U - L \geq \eta\delta$이다. $c$가 어떤 $(x_{j-1}, x_j)$ 안에 있으면 $\Delta\alpha_j = \alpha(x_j) - \alpha(x_{j-1}) \geq \alpha(c+) - \alpha(c) = \delta$이고, $[x_{j-1}, x_j] \supseteq [c, x_j]$이므로 같은 이유로 $M_j - m_j \geq \eta$이다. 이때도 $U - L \geq \eta\delta$이다.
:::

::: 예시 8 (같은 점에서 불연속이지만 방향이 다른 경우)
$[a,b] = [-1, 1]$에서 $\alpha(x) = 0$ ($x < 0$), $\alpha(x) = 1$ ($x \geq 0$)이라 하자. $\alpha$는 0에서 왼쪽 불연속이다($\alpha(0-) = 0 < \alpha(0) = 1 = \alpha(0+)$). $f_1(x) = 1$ ($x < 0$), $f_1(x) = 0$ ($x \geq 0$)은 0에서 왼쪽 불연속이므로 [명제 7](#prop7){: data-lid="v0vvx" }에 의하여 $f_1 \notin \mathcal{R}(\alpha)$이다. $f_2(x) = 0$ ($x \leq 0$), $f_2(x) = 1$ ($x > 0$)은 0에서 불연속이지만 왼쪽 연속이다. 0을 분할점으로 갖는 분할 $P$에서 $\Delta\alpha_i \neq 0$인 부분구간은 $[x_{j-1}, 0]$ 하나이고 그 위에서 $f_2 = 0$이므로 $U(P, f_2, \alpha) = L(P, f_2, \alpha) = 0$이다. 따라서 $f_2 \in \mathcal{R}(\alpha)$이고 $\int f_2\dd{\alpha} = 0 = f_2(0) \cdot 1$이다.
:::

[예시 8](#ex8){: data-lid="f6kim" }의 $f_2$가 적분가능한 것은 분할의 세분으로 정의한 적분의 성질이다. 분할의 mesh를 0으로 보내는 극한으로 적분을 정의하면 0이 분할점이 아닌 부분구간에서 $\Delta\alpha = 1$이고 표본점이 $f_2 = 0$인 점이나 $f_2 = 1$인 점 어느 쪽이든 될 수 있으므로 합이 수렴하지 않는다. 이 정의에서는 $f$와 $\alpha$가 한 점에서 같이 불연속이기만 하면 방향과 무관하게 적분이 존재하지 않는다. 이 글의 정의에서 [정리 6](#thm6){: data-lid="ryxtt" }의 연속성 가정은 점프가 일어나는 쪽의 연속성으로 약해질 수 있다. 가령 $\alpha(s) = \alpha(s+)$이면 $[s - \delta/2, s]$에서만 $\Delta\alpha \neq 0$이므로 $f$가 $s$에서 왼쪽 연속이기만 하면 증명이 그대로 돈다.

## $\alpha$가 미분가능한 경우

::: 정리 9 ($\alpha \in C^1$)
$\alpha$가 $[a,b]$에서 $C^1$인 증가함수이고 $f$가 bounded function이면 $f \in \mathcal{R}(\alpha)$인 것은 $f\alpha' \in \mathcal{R}$(Riemann 적분가능)인 것과 동치이고, 이때

$$\int_a^b f\dd{\alpha} = \int_a^b f(x)\alpha'(x)\dd{x}$$

이다.
:::

::: 증명
$M = \sup \lvert f\rvert$이라 하고 $\varepsilon > 0$이 주어졌다고 하자. $\varepsilon' = \varepsilon/(M+1)$로 둔다. $\alpha'$는 연속이므로 [정리 4](#thm4){: data-lid="a9jig" }(의 $\alpha(x) = x$인 경우)에 의하여 Riemann 적분가능하고, [정리 3](#thm3){: data-lid="grn5e" }에 의하여 $U(P_0, \alpha') - L(P_0, \alpha') < \varepsilon'$인 분할 $P_0$가 있다. $P_0$의 임의의 세분 $P$에 대하여 같은 부등식이 성립한다.

각 $I_i$에서 [§평균값 정리와 테일러 정리, ⁋정리 3](/ko/math/analysis/mean_value_theorem#thm3){: data-lid="7unaq" }에 의하여 $\Delta\alpha_i = \alpha'(t_i)\Delta x_i$인 $t_i \in (x_{i-1}, x_i)$가 있다. 임의의 $s_i \in I_i$에 대하여 $\lvert \alpha'(s_i) - \alpha'(t_i)\rvert$는 $I_i$ 위에서 $\alpha'$의 $\sup - \inf$ 이하이므로

$$\sum_i \lvert \alpha'(s_i) - \alpha'(t_i)\rvert \Delta x_i \leq U(P, \alpha') - L(P, \alpha') < \varepsilon'$$

이다. 그럼

$$\Bigl\lvert \sum_i f(s_i)\Delta\alpha_i - \sum_i f(s_i)\alpha'(s_i)\Delta x_i \Bigr\rvert \leq M \sum_i \lvert \alpha'(t_i) - \alpha'(s_i)\rvert \Delta x_i < \varepsilon$$

이다. 각 $s_i$는 서로 독립적으로 $I_i$ 위에서 움직일 수 있고 $\Delta\alpha_i \geq 0$, $\Delta x_i > 0$이므로, 양변에서 $s_i$에 대한 supremum을 취하면 $\lvert U(P, f, \alpha) - U(P, f\alpha')\rvert \leq \varepsilon$이다. Infimum을 취하면 $\lvert L(P, f, \alpha) - L(P, f\alpha')\rvert \leq \varepsilon$도 얻는다.

상합은 세분에서 줄어드므로 상적분은 $P_0$의 세분들에 대한 상합의 infimum이다. 따라서 위 부등식에서 $\lvert \overline{\int} f\dd{\alpha} - \overline{\int} f\alpha'\dd{x}\rvert \leq \varepsilon$이고, 하적분도 마찬가지이다. $\varepsilon$이 임의이므로 $f$의 $\alpha$에 대한 상적분과 하적분은 각각 $f\alpha'$의 상적분과 하적분과 같다. 그러므로 한쪽이 같은 값을 가지는 것과 다른 쪽이 그런 것은 동치이고, 값도 같다.
:::

$\alpha(x) = x$이면 $\alpha' = 1$이므로 이 정리는 [정의 1](#def1){: data-lid="e2inc" }이 Riemann 적분을 포함한다는 말과 같다. 이 정리는 $\alpha$에 점프가 없고 도함수가 연속일 때의 환원이고, 점프가 있는 경우는 [정리 6](#thm6){: data-lid="oz7p4" }이 담당한다. 둘은 [명제 5](#prop5){: data-lid="nqma4" }로 합쳐진다.

## 확률분포의 기댓값

확률변수 $X$의 누적분포함수 $F(x) = P(X \leq x)$는 증가함수이고, $X$의 값이 모두 $(a, b]$에 놓이도록 $[a,b]$를 잡으면 $F(a) = 0$, $F(b) = 1$이다. 구간의 왼쪽 끝을 $F(a) = 0$이 되도록 잡는 것이 중요하다. $a$에 확률이 몰려 있으면 $F(a) > 0$이고, 약속 $\alpha(a-) = \alpha(a)$ 때문에 그 점의 질량이 $\int_a^b$에 반영되지 않는다. 연속함수 $g$에 대하여

$$E[g(X)] = \int_a^b g\dd{F}$$

로 쓰면 이산분포와 연속분포가 같은 식에 들어간다. $X$가 $s_1 < \cdots < s_N$의 값을 확률 $p_k$로 취하면 $F$는 $s_k$에서 크기 $p_k$로 점프하는 계단함수이고 [정리 6](#thm6){: data-lid="2axvv" }에 의하여 $E[g(X)] = \sum_k p_k g(s_k)$이다. $X$가 연속인 밀도 $\rho$를 가지면 $F(x) = \int_a^x \rho$는 [§미적분의 기본정리, ⁋정리 2](/ko/math/analysis/fundamental_theorem_of_calculus#thm2){: data-lid="us5nl" }에 의하여 $C^1$이고 $F' = \rho$이므로 [정리 9](#thm9){: data-lid="615fz" }에 의하여 $E[g(X)] = \int_a^b g(x)\rho(x)\dd{x}$이다.

두 성분이 섞인 분포도 같은 식으로 계산된다. $X$가 확률 $p$로 점 $s \in (a, b]$에 있고 확률 $1 - p$로 연속 밀도 $\rho$를 따르면 $F(x) = p\mathbf{1}_{[s, \infty)}(x) + (1-p)\int_a^x \rho$이다. 연속함수 $g$는 두 항 각각에 대하여 적분가능하므로([정리 4](#thm4){: data-lid="g9r2u" }) [명제 5](#prop5){: data-lid="dj5u4" }에 의하여 적분이 두 항으로 갈라지고, [정리 6](#thm6){: data-lid="32x00" }과 [정리 9](#thm9){: data-lid="vqf1s" }를 각각 적용하면

$$E[g(X)] = p g(s) + (1-p)\int_a^b g(x)\rho(x)\dd{x}$$

이다. 밀도 함수로는 이런 분포의 점질량을 표현할 수 없으므로 $\int g\dd{F}$가 이 경우의 자연스러운 표기이다.

## 부분적분

::: 정리 10 (부분적분)
$f, \alpha$가 모두 $[a,b]$ 위의 증가함수라 하자. $f \in \mathcal{R}(\alpha)$인 것은 $\alpha \in \mathcal{R}(f)$인 것과 동치이고, 이때

$$\int_a^b f\dd{\alpha} + \int_a^b \alpha\dd{f} = f(b)\alpha(b) - f(a)\alpha(a)$$

이다.
:::

::: 증명
분할 $P$에 대하여 $f, \alpha$가 증가함수이므로 $I_i$ 위에서 $\sup f = f(x_i)$, $\inf f = f(x_{i-1})$이고 $\alpha$도 같다. 따라서 $U(P, f, \alpha) = \sum f(x_i)\Delta\alpha_i$, $L(P, \alpha, f) = \sum \alpha(x_{i-1})\Delta f_i$이고, 항별로

$$f(x_i)(\alpha(x_i) - \alpha(x_{i-1})) + \alpha(x_{i-1})(f(x_i) - f(x_{i-1})) = f(x_i)\alpha(x_i) - f(x_{i-1})\alpha(x_{i-1})$$

이므로 합하면 $U(P, f, \alpha) + L(P, \alpha, f) = f(b)\alpha(b) - f(a)\alpha(a) =: B$이다. 같은 방식으로 $L(P, f, \alpha) + U(P, \alpha, f) = B$이다. 두 등식을 빼면

$$U(P, \alpha, f) - L(P, \alpha, f) = U(P, f, \alpha) - L(P, f, \alpha)$$

이다. 같은 분할 $P$에서 두 차가 같으므로, [정리 3](#thm3){: data-lid="19ppp" }에 의하여 $f \in \mathcal{R}(\alpha)$이면 $\alpha \in \mathcal{R}(f)$이고 역도 성립한다. 이때 $L(P, \alpha, f) = B - U(P, f, \alpha)$의 supremum을 $P$에 대하여 취하면 $\int \alpha\dd{f} = B - \overline{\int} f\dd{\alpha} = B - \int f\dd{\alpha}$이다.
:::

$f$와 $\alpha$가 같은 점에서 같은 쪽으로 불연속이면 $f \in \mathcal{R}(\alpha)$도 $\alpha \in \mathcal{R}(f)$도 성립하지 않는다는 점이 [명제 7](#prop7){: data-lid="g06me" }에서 나온다. 부분적분은 두 적분이 존재할 때의 등식이 아니라, 한쪽의 존재가 다른 쪽의 존재를 함축한다는 내용까지 담고 있다. 가령 $f(x) = x$와 $\alpha = \lfloor x \rfloor$를 $[0, n]$에서 생각하면 [정리 6](#thm6){: data-lid="pj7w4" }에 의하여 $\int x\dd{\lfloor x \rfloor} = 1 + \cdots + n = n(n+1)/2$이므로, [정리 10](#thm10){: data-lid="3eobc" }에 의하여 $\int_0^n \lfloor x \rfloor\dd{x} = n^2 - n(n+1)/2 = n(n-1)/2$이다. 이는 Abel의 합산법을 적분의 언어로 쓴 것에 해당한다.

## 유계변동함수

적분기가 증가함수라는 가정은 두 증가함수의 차로 쓸 수 있는 함수까지 넓힐 수 있다.

::: 정의 11 (유계변동함수)
함수 $\alpha : [a,b] \to \mathbb{R}$의 *total variation<sub>전변동</sub>*을 $V_a^b(\alpha) = \sup_P \sum_{i=1}^n \lvert \alpha(x_i) - \alpha(x_{i-1})\rvert$로 정의한다. 이 값이 유한할 때 $\alpha$를 *유계변동함수<sub>function of bounded variation</sub>*라 한다.
:::

증가함수 $\alpha$는 모든 합이 $\alpha(b) - \alpha(a)$이므로 유계변동함수이다. $\lvert \alpha(x) - \alpha(y)\rvert \leq L\lvert x - y\rvert$를 만족하는 Lipschitz 함수는 $V_a^b(\alpha) \leq L(b - a)$이므로 역시 그렇고, 특히 $C^1$ 함수가 그렇다.

::: 정리 12 (Jordan 분해)
$\alpha$가 유계변동함수이면 $\alpha = \alpha_1 - \alpha_2$인 증가함수 $\alpha_1, \alpha_2$가 존재한다.
:::

::: 증명
$V(x) = V_a^x(\alpha)$($V(a) = 0$)로 두고 $\alpha_1 = V$, $\alpha_2 = V - \alpha$로 정한다. $V$는 bounded이다. $a \leq x < y \leq b$에 대하여 $[a, x]$의 임의의 분할에 점 $y$를 덧붙이면 $[a, y]$의 분할이 되므로 $V(y) \geq (\text{그 분할의 합}) + \lvert \alpha(y) - \alpha(x)\rvert$이고, 분할에 대한 supremum을 취하면 $V(y) \geq V(x) + \lvert \alpha(y) - \alpha(x)\rvert$이다. 따라서 $V$는 증가하고, $V(y) - V(x) \geq \alpha(y) - \alpha(x)$에서 $V - \alpha$도 증가한다.
:::

유계변동함수 $\alpha = \alpha_1 - \alpha_2$와 연속함수 $f$에 대하여 $\int f\dd{\alpha} := \int f\dd{\alpha_1} - \int f\dd{\alpha_2}$로 정의한다. [정리 4](#thm4){: data-lid="pw5du" }에 의하여 우변의 두 적분이 존재한다. 이 값은 분해의 선택과 무관하다. $\alpha_1 - \alpha_2 = \beta_1 - \beta_2$이면 $\alpha_1 + \beta_2 = \beta_1 + \alpha_2$이므로 [명제 5](#prop5){: data-lid="qcfu2" }에 의하여 $\int f\dd{\alpha_1} + \int f\dd{\beta_2} = \int f\dd{\beta_1} + \int f\dd{\alpha_2}$이고, 이항하면 두 분해에서 같은 값을 얻는다.

---

**참고문헌**

**[Rud]** W. Rudin, *Principles of mathematical analysis*, 3rd ed., McGraw-Hill, 1976.
