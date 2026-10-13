---
title: "Riemann 적분"
description: "Darboux 상합과 하합으로 Riemann 적분을 정의하고, 모든 ε에 대해 상합과 하합의 차를 ε보다 작게 하는 분할이 존재한다는 Riemann 판정법을 증명한다. 연속함수, 단조함수, 불연속점이 유한한 bounded function의 적분가능성과 Dirichlet 함수, Thomae 함수의 예를 다루고, 적분의 선형성, 단조성, 구간가법성과 f의 제곱, 절댓값의 적분가능성을 보인다."
excerpt: "Darboux 합, Riemann 판정법, 적분가능한 함수의 부류, 적분의 기본 성질"

categories: [Math / Analysis]
permalink: /ko/math/analysis/riemann_integral
sidebar: 
    nav: "analysis-ko"

date: 2026-06-02
weight: 16

published: false

---

구간 $[a,b]$ 위의 bounded function $f$의 적분은 그래프 아래의 넓이를 직사각형 띠들로 근사하여 얻는다. [\[미적분학\] §적분, ⁋정의 9](/ko/math/calculus/integration#def9){: data-lid="pwj8v" }에서는 분할의 각 부분구간에서 임의로 고른 점의 함숫값을 높이로 하는 Riemann 합의 극한으로 이를 정의하였다. 이 글에서는 점을 고르는 대신 각 부분구간에서 $f$의 infimum과 supremum을 높이로 삼는 Darboux 합을 쓴다. 부분구간에서 고른 점의 함숫값은 infimum과 supremum 사이에 있으므로 어떤 Riemann 합도 같은 분할의 두 Darboux 합 사이에 놓이고, 두 Darboux 합이 같은 값으로 모이면 Riemann 합의 극한도 그 값이 된다. 이 방식의 적분가능성은 Riemann 합의 극한으로 정의한 적분가능성과 동치이며 적분값도 같다. 극한을 직접 다루는 대신 상합과 하합이라는 두 개의 실수만 비교하면 되므로 증명이 훨씬 간결해진다.

## 분할과 Darboux 합

::: 정의 1 (분할과 Darboux 합)
$[a,b]$의 *분할<sub>partition</sub>*은 $a = x_0 < x_1 < \cdots < x_n = b$인 유한집합 $P = \{x_0, \dots, x_n\}$이다. 각 $i$에 대하여 $I_i = [x_{i-1}, x_i]$, $\Delta x_i = x_i - x_{i-1}$로 적고, $\lVert P\rVert = \max_i \Delta x_i$를 $P$의 *mesh*라 한다. Bounded function $f : [a,b] \to \mathbb{R}$에 대하여

$$m_i = \inf_{x \in I_i} f(x), \qquad M_i = \sup_{x \in I_i} f(x)$$

로 두고

$$L(P, f) = \sum_{i=1}^n m_i \Delta x_i, \qquad U(P, f) = \sum_{i=1}^n M_i \Delta x_i$$

를 각각 $P$에 대한 $f$의 *하합<sub>lower sum</sub>*과 *상합<sub>upper sum</sub>*이라 한다.
:::

$f$가 bounded이므로 $m_i, M_i$는 모두 실수이고 $m_i \leq M_i$이므로 $L(P,f) \leq U(P,f)$이다. 각 $I_i$에서 점 $t_i$를 골라 만든 Riemann 합 $\sum_i f(t_i)\Delta x_i$는 $m_i \leq f(t_i) \leq M_i$에 의하여 $L(P,f)$와 $U(P,f)$ 사이에 있다. 하합은 $f$ 아래에 내접하는 띠들의 넓이이고 상합은 $f$를 덮는 띠들의 넓이이므로, 분할을 잘게 할수록 두 합이 서로 가까워지기를 기대할 수 있다. 다음 보조정리는 이 기대의 첫 번째 절반, 곧 분할을 세분하면 하합은 줄지 않고 상합은 늘지 않는다는 사실이다.

::: 보조정리 2 (세분)
$P \subseteq P'$인 두 분할에 대하여 $L(P, f) \leq L(P', f)$이고 $U(P', f) \leq U(P, f)$이다.
:::

::: 증명
$P'$이 $P$에 점 하나만 더한 경우를 보이면, 일반적인 경우는 점을 하나씩 더하는 과정을 유한 번 반복하여 얻는다. 더해지는 점 $c$가 $x_{j-1} < c < x_j$를 만족한다고 하자. 하합에서 달라지는 항은 $m_j \Delta x_j$ 하나이고, 이것이 $m' = \inf_{[x_{j-1}, c]} f$와 $m'' = \inf_{[c, x_j]} f$로 쪼개진다. subset 위의 infimum은 원래 집합 위의 infimum보다 작지 않으므로 $m' \geq m_j$, $m'' \geq m_j$이고

$$\begin{aligned}
m'(c - x_{j-1}) + m''(x_j - c) &\geq m_j (c - x_{j-1}) + m_j (x_j - c) \\
&= m_j \Delta x_j
\end{aligned}$$

이다. 따라서 $L(P', f) \geq L(P, f)$이다. 상합은 $U(P, f) = -L(P, -f)$이므로 하합의 경우에서 곧바로 따른다.
:::

한 분할의 하합이 그 분할의 상합보다 작다는 것은 정의에서 바로 나오지만, 서로 다른 두 분할 $P, Q$에 대해서는 $L(P,f) \leq U(Q,f)$가 자명하지 않다. 두 분할을 모두 세분하는 $P \cup Q$를 거치면 된다.

::: 명제 3
임의의 두 분할 $P, Q$에 대하여 $L(P, f) \leq U(Q, f)$이다.
:::

::: 증명
[보조정리 2](#lem2){: data-lid="ujm3y" }에 의하여

$$L(P, f) \leq L(P \cup Q, f) \leq U(P \cup Q, f) \leq U(Q, f)$$

이다.
:::

## 상적분과 하적분

[명제 3](#prop3){: data-lid="7fgvx" }에 의하여 하합들의 집합은 위로 bounded이고 상합들의 집합은 아래로 bounded이다. 따라서 이들의 supremum과 infimum이 [§실수의 완비성, ⁋정의 3](/ko/math/analysis/completeness_of_reals#def3){: data-lid="aghpm" }에 의하여 존재한다.

::: 정의 4 (Riemann 적분)
Bounded function $f : [a,b] \to \mathbb{R}$에 대하여

$$\underline{\int_a^b} f = \sup_P L(P, f), \qquad \overline{\int_a^b} f = \inf_P U(P, f)$$

를 각각 *하적분<sub>lower integral</sub>*과 *상적분<sub>upper integral</sub>*이라 한다. 두 값이 같을 때 $f$를 $[a,b]$에서 *Riemann 적분가능<sub>Riemann integrable</sub>*하다고 하고, 공통값을 $\int_a^b f(x)\dd{x}$ 또는 $\int_a^b f$로 적는다.
:::

[명제 3](#prop3){: data-lid="4i1h7" }에서 $Q$를 고정하고 $P$에 대한 supremum을 취하면 $\underline{\int} f \leq U(Q, f)$이고, 이어서 $Q$에 대한 infimum을 취하면 $\underline{\int} f \leq \overline{\int} f$이다. 그러므로 적분가능성은 이 부등식이 등식이라는 조건이다. 정의 자체가 bounded function에 대해서만 이루어졌다는 점에 주의해야 한다. Bounded가 아닌 함수는 상합이나 하합이 정의되지 않으므로 이 글의 의미로는 적분가능하지 않다.

## Riemann 판정법

[정의 4](#def4){: data-lid="m2ypp" }를 그대로 쓰면 상적분과 하적분의 값을 먼저 알아야 하는데, 실제로는 그 값을 모르는 채 적분가능성부터 확인하고 싶은 경우가 대부분이다. 다음 판정법은 분할 하나만 찾으면 된다고 말해 준다.

::: 정리 5 (Riemann 판정법)
Bounded function $f : [a,b] \to \mathbb{R}$이 적분가능한 것은 모든 $\varepsilon > 0$에 대하여 $U(P, f) - L(P, f) < \varepsilon$인 분할 $P$가 존재하는 것과 동치이다.
:::

::: 증명
($\Leftarrow$) 임의의 $\varepsilon > 0$과 이를 만족하는 $P$에 대하여 $L(P,f) \leq \underline{\int} f \leq \overline{\int} f \leq U(P,f)$이므로 $0 \leq \overline{\int} f - \underline{\int} f < \varepsilon$이다. $\varepsilon$이 임의이므로 두 적분은 같다.

($\Rightarrow$) 공통값을 $I$라 하자. Supremum과 infimum의 정의에 의하여 $L(P_1, f) > I - \varepsilon/2$인 분할 $P_1$과 $U(P_2, f) < I + \varepsilon/2$인 분할 $P_2$가 있다. 두 분할에서 $\varepsilon/2$씩 가져오는 것은 합쳐서 $\varepsilon$이 되도록 하기 위한 것이다. $P = P_1 \cup P_2$로 두면 [보조정리 2](#lem2){: data-lid="68yie" }에 의하여 $L(P_1, f) \leq L(P, f)$이고 $U(P, f) \leq U(P_2, f)$이므로 $U(P, f) - L(P, f) < (I + \varepsilon/2) - (I - \varepsilon/2) = \varepsilon$이다.
:::

[보조정리 2](#lem2){: data-lid="enddw" }에 의하여 $U(P,f) - L(P,f) < \varepsilon$인 분할을 세분해도 같은 부등식이 유지된다. 이후의 증명에서는 필요한 분할 몇 개를 공통세분 하나로 합치는 데 이 사실을 계속 쓴다.

## 연속함수와 단조함수

::: 정리 6
$[a,b]$ 위의 연속함수는 Riemann 적분가능하다.
:::

::: 증명
$[a,b]$가 컴팩트이므로 [§연속함수의 성질, ⁋정리 6](/ko/math/analysis/continuous_functions#thm6){: data-lid="lmsmx" }에 의하여 $f$는 균등연속이다. $\varepsilon > 0$이 주어졌다고 하고 $\varepsilon' = \varepsilon / (2(b-a))$로 두자. 균등연속성에 의하여 $\lvert x - y\rvert < \delta$이면 $\lvert f(x) - f(y)\rvert < \varepsilon'$인 $\delta > 0$이 점의 위치와 무관하게 존재한다. $\lVert P\rVert < \delta$인 분할 $P$를 하나 고르면(구간을 충분히 많은 등간격으로 나누면 된다), 각 $I_i$의 두 점 $x, y$는 $\lvert x - y\rvert \leq \Delta x_i < \delta$이므로 $f(x) - f(y) < \varepsilon'$이다. $x$에 대해 supremum, $y$에 대해 infimum을 취하면 $M_i - m_i \leq \varepsilon'$이고

$$U(P, f) - L(P, f) = \sum_{i=1}^n (M_i - m_i)\Delta x_i \leq \varepsilon' \sum_{i=1}^n \Delta x_i = \frac{\varepsilon}{2} < \varepsilon$$

이다. [정리 5](#thm5){: data-lid="vlhgs" }에 의하여 $f$는 적분가능하다.
:::

$\varepsilon'$을 $\varepsilon/(b-a)$로 잡지 않고 절반으로 잡은 것은, supremum과 infimum을 취하는 과정에서 부등호 $<$가 $\leq$로 약해져 마지막 결과가 $\varepsilon$ 이하로만 얻어지기 때문이다. 증명의 핵심은 균등연속성이 부분구간의 폭 $\delta$를 모든 위치에 대해 한꺼번에 통제한다는 점이다. 점별 연속성만 쓰면 $\delta$가 점마다 달라져 하나의 분할로 모든 진동 $M_i - m_i$를 동시에 작게 만들 수 없다.

연속성이 적분가능성에 필요한 조건은 아니다. 불연속점이 많아도 함수가 한쪽 방향으로만 움직이면 적분가능하다.

::: 정리 7
$[a,b]$ 위의 단조함수는 Riemann 적분가능하다.
:::

::: 증명
$f$가 증가함수라 하자. 그럼 $f(a) \leq f \leq f(b)$이므로 $f$는 bounded이다. 구간을 $n$등분한 분할 $P_n$에서 $\Delta x_i = (b-a)/n$이고, $f$가 증가하므로 $m_i = f(x_{i-1})$, $M_i = f(x_i)$이다. 따라서

$$\begin{aligned}
U(P_n, f) - L(P_n, f) &= \frac{b-a}{n} \sum_{i=1}^n \bigl(f(x_i) - f(x_{i-1})\bigr) \\
&= \frac{b-a}{n}\bigl(f(b) - f(a)\bigr)
\end{aligned}$$

이다. 둘째 등호는 합이 망원급수로 소거되기 때문이다. 우변은 $n \to \infty$일 때 $0$으로 가므로 주어진 $\varepsilon$보다 작게 하는 $n$이 있고, [정리 5](#thm5){: data-lid="vdpan" }에 의하여 $f$는 적분가능하다. 감소함수의 경우는 $m_i = f(x_i)$, $M_i = f(x_{i-1})$이 되어 같은 계산에서 $f(b) - f(a)$의 부호만 바뀐다.
:::

단조함수는 점프 불연속점을 가질 수 있고, 그 개수가 무한이어도 상관없다. 가령 $[0,1]$ 위에서

$$f(x) = \sum_{1/k \leq x} 2^{-k}$$

(합은 자연수 $k$ 위에서 취한다)로 정의된 함수는 증가함수이고 각 $x = 1/k$에서 크기 $2^{-k}$의 점프를 가지므로 불연속점이 무한히 많지만, [정리 7](#thm7){: data-lid="ifmwv" }에 의하여 적분가능하다.

## 불연속점이 있는 함수

::: 정리 8
$[a,b]$ 위의 bounded function이 유한개의 점을 제외한 모든 점에서 연속이면 Riemann 적분가능하다.
:::

::: 증명
$[a,b]$ 위에서 $\lvert f\rvert \leq K$ ($K > 0$)라 하고, 불연속점을 $c_1 < \cdots < c_k$라 하자($k = 0$이면 [정리 6](#thm6){: data-lid="cyccb" }이다). $\varepsilon > 0$이 주어졌다고 하고 $\eta > 0$을 $\eta < \varepsilon/(8Kk)$이고 닫힌구간 $[c_j - \eta, c_j + \eta]$들이 서로 소가 되도록 작게 잡는다. 열린구간 $V_j = (c_j - \eta, c_j + \eta)$들을 $[a,b]$에서 제거한 집합 $C$는 컴팩트이고, $f$는 $C$의 모든 점에서 연속이므로 $f$를 $C$로 제한한 함수는 균등연속이다. $\varepsilon' = \varepsilon / (2(b-a))$에 대응하는 $\delta$를 잡자.

분할 $P$를 다음과 같이 만든다. $a$, $b$, 그리고 $[a,b]$ 안에 있는 $c_j \pm \eta$를 분점으로 하면, 이 분점들 사이의 각 구간은 어떤 $[c_j - \eta, c_j + \eta]$ 안에 들어 있거나 모든 $V_j$와 서로 소여서 $C$ 안에 들어 있다. 후자의 구간들을 길이 $\delta$ 미만으로 더 쪼갠다. 전자의 구간들에서는 $M_i - m_i \leq 2K$이고 이들의 길이의 합은 $2k\eta$ 이하이다. 후자에서는 [정리 6](#thm6){: data-lid="ot7i2" }의 논증과 같이 $M_i - m_i \leq \varepsilon'$이다. 따라서

$$U(P, f) - L(P, f) \leq 2K \cdot 2k\eta + \varepsilon'(b-a) < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon$$

이고 [정리 5](#thm5){: data-lid="dagir" }에 의하여 $f$는 적분가능하다.
:::

Bounded라는 가정은 빼면 안 된다. $f(x) = 1/x$ ($x > 0$), $f(0) = 0$은 불연속점이 $0$ 하나뿐이지만 bounded가 아니어서 상합이 정의되지 않고, 따라서 Riemann 적분가능하지 않다.

이제 불연속점이 유한개를 넘어서는 두 예를 비교한다. 두 함수 모두 불연속점이 $[0,1]$에서 조밀하지만 결과는 반대이다.

::: 예시 9 (Dirichlet 함수)
$f : [0,1] \to \mathbb{R}$을 유리수에서 $1$, 무리수에서 $0$으로 정의한다. 유리수와 무리수는 각각 $\mathbb{R}$에서 조밀하므로 임의의 분할의 모든 부분구간에서 $m_i = 0$, $M_i = 1$이다. 따라서 모든 분할 $P$에 대하여

$$L(P, f) = 0, \qquad U(P, f) = \sum_{i=1}^n \Delta x_i = 1$$

이고 $\underline{\int} f = 0 \neq 1 = \overline{\int} f$이다. $f$는 Riemann 적분가능하지 않다.
:::

::: 예시 10 (Thomae 함수)
$f : [0,1] \to \mathbb{R}$을, $x$가 기약분수 $p/q$ ($q \geq 1$)로 적히면 $f(x) = 1/q$, 무리수이면 $f(x) = 0$으로 정의한다. 이 함수는 적분가능하고 $\int_0^1 f = 0$이다.

$\varepsilon > 0$이 주어졌다고 하고 $1/N < \varepsilon/2$인 자연수 $N$을 잡는다. $f(x) \geq 1/N$인 점들의 집합은 $q \leq N$인 기약분수 $p/q$들이므로 유한집합이고, 그 원소의 수를 $k$라 하자. $\lVert P\rVert < \varepsilon/(4k)$인 분할 $P$를 잡는다. 무리수가 조밀하므로 모든 부분구간에서 $m_i = 0$이고 $L(P, f) = 0$이다. 이 점들을 하나도 포함하지 않는 부분구간에서는 $M_i \leq 1/N$이다. 이 점들을 포함하는 부분구간은 각 점이 많아야 두 개의 부분구간에 속하므로 $2k$개 이하이고, 이들에서는 $M_i \leq 1$이며 길이의 합은 $2k \cdot \varepsilon/(4k) = \varepsilon/2$ 이하이다. 따라서

$$U(P, f) - L(P, f) \leq \frac{1}{N}(b-a) + \frac{\varepsilon}{2} < \varepsilon$$

이고 [정리 5](#thm5){: data-lid="jx950" }에 의하여 $f$는 적분가능하다. 모든 하합이 $0$이므로 적분값은 $0$이다.

같은 논증으로 $f$는 모든 무리수에서 연속이다. $x_0$가 무리수이고 $\varepsilon > 0$이면, $f \geq \varepsilon$인 점은 유한개이고 $x_0$는 그중에 없으므로, $x_0$의 충분히 작은 근방에서는 $f < \varepsilon$이다. 반면 유리수 $p/q$에서는 $f(p/q) = 1/q > 0$인데 그 근방에 $f = 0$인 무리수가 있으므로 불연속이다. 따라서 불연속점 집합은 $[0,1]$의 유리수 전체이고, [정리 8](#thm8){: data-lid="qykxw" }로는 이 함수의 적분가능성을 얻을 수 없다.
:::

Dirichlet 함수와 Thomae 함수는 모두 유리수에서 불연속이지만, Dirichlet 함수의 진동은 모든 점에서 $1$로 일정한 반면 Thomae 함수의 진동은 점프의 크기 $1/q$가 $q$와 함께 $0$으로 모이기 때문에 상합과 하합의 차에 기여하는 부분이 작게 통제된다. 이 현상을 정확히 기술하는 것이 다음 판정법이다.

::: 정리 11 (Lebesgue 판정법)
Bounded function $f : [a,b] \to \mathbb{R}$이 Riemann 적분가능한 것은 $f$의 불연속점 집합이 측도 $0$인 것과 동치이다. 여기서 집합 $S \subseteq \mathbb{R}$이 *측도 $0$*이라 함은 모든 $\varepsilon > 0$에 대하여 $S$를 덮는 가산개의 구간들로 길이의 합이 $\varepsilon$ 미만인 것이 있다는 뜻이다.
:::

가산집합은 측도 $0$이므로 Thomae 함수는 이 판정법과 부합한다. Dirichlet 함수의 불연속점 집합은 $[0,1]$ 전체이고 이는 측도 $0$이 아니다. 유한집합은 측도 $0$이므로 [정리 8](#thm8){: data-lid="r5663" }은 이 판정법의 특수한 경우이고, 단조함수의 불연속점은 가산개이므로 [정리 7](#thm7){: data-lid="w5tak" }도 그러하다. 이 글에서는 측도의 도구가 필요한 이 정리를 진술만 한다.

## 적분의 성질

적분의 기본 성질은 모두 Darboux 합을 비교하여 얻는다.

::: 명제 12 (선형성과 단조성)
$f, g$가 $[a,b]$에서 적분가능하면 $f + g$와 $cf$ ($c \in \mathbb{R}$)도 적분가능하고

$$\int_a^b (f + g) = \int_a^b f + \int_a^b g, \qquad \int_a^b cf = c\int_a^b f$$

이다. 또한 $f \leq g$이면 $\int_a^b f \leq \int_a^b g$이다.
:::

::: 증명
합을 먼저 보자. 각 $I_i$의 모든 점 $x$에서 $\inf f + \inf g \leq f(x) + g(x) \leq \sup f + \sup g$이므로 $\inf f + \inf g \leq \inf (f+g)$, $\sup (f+g) \leq \sup f + \sup g$이고, 이를 모든 $i$에 대해 합하면 임의의 분할에서

$$L(P, f) + L(P, g) \leq L(P, f+g) \leq U(P, f+g) \leq U(P, f) + U(P, g)$$

이다. $\varepsilon > 0$에 대하여 [정리 5](#thm5){: data-lid="nnzy5" }로 $f$, $g$에 대한 $\varepsilon/2$-분할을 각각 잡고 그 공통세분을 $P$라 하면 [보조정리 2](#lem2){: data-lid="7m0ao" }에 의하여 $P$에서 $U(P,f) - L(P,f) < \varepsilon/2$, $U(P,g) - L(P,g) < \varepsilon/2$이다. 위 부등식에서 $U(P, f+g) - L(P, f+g) < \varepsilon$이므로 $f+g$는 적분가능하다. 또 $L(P,f) \leq \int f \leq U(P,f)$이고 $U(P,f) - L(P,f) < \varepsilon/2$이므로 $U(P,f) < \int f + \varepsilon/2$이고, $g$도 같으므로

$$\int (f+g) \leq U(P, f+g) \leq U(P, f) + U(P, g) < \int f + \int g + \varepsilon$$

이다. 마찬가지로 $\int(f+g) \geq L(P, f+g) > \int f + \int g - \varepsilon$이다. $\varepsilon$이 임의이므로 $\int (f+g) = \int f + \int g$이다.

상수배는 $c \geq 0$이면 각 $I_i$에서 $\inf (cf) = c \inf f$, $\sup(cf) = c \sup f$이므로 $L(P, cf) = cL(P,f)$, $U(P, cf) = cU(P,f)$이고, 이를 상적분과 하적분에 옮기면 된다. $c < 0$이면 infimum과 supremum이 서로 바뀌어 $L(P, cf) = cU(P, f)$, $U(P, cf) = cL(P, f)$이고, $\sup_P cU(P,f) = c \inf_P U(P,f) = c\int f$이므로 하적분이 $c\int f$이다. 상적분도 같은 값이 된다.

단조성은 $f \leq g$이면 모든 분할에서 $L(P, f) \leq L(P, g)$이므로 supremum을 취하여 $\int f = \underline{\int} f \leq \underline{\int} g = \int g$로 얻는다.
:::

다음 명제의 증명에는 각 부분구간에서의 진동 $M_i - m_i$가 함숫값의 차이로 계산된다는 사실을 쓴다. 곧 $x, y \in I_i$에 대하여 $f(x) - f(y) \leq M_i - m_i$이므로 $\sup_{x,y \in I_i} \lvert f(x) - f(y)\rvert \leq M_i - m_i$이고, 역으로 $\eta > 0$에 대해 $f(x) > M_i - \eta$, $f(y) < m_i + \eta$인 $x, y$를 잡으면 $f(x) - f(y) > M_i - m_i - 2\eta$이므로

$$M_i - m_i = \sup_{x, y \in I_i} \lvert f(x) - f(y)\rvert$$

이다.

::: 명제 13
$f, g$가 $[a,b]$에서 적분가능하면 $\lvert f\rvert$, $f^2$, $fg$도 적분가능하고 $\bigl\lvert \int_a^b f\bigr\rvert \leq \int_a^b \lvert f\rvert$이다.
:::

::: 증명
$\lvert f\rvert \leq K$라 하고 $\varepsilon > 0$이라 하자. $x, y \in I_i$에 대하여 $\bigl\lvert \lvert f(x)\rvert - \lvert f(y)\rvert \bigr\rvert \leq \lvert f(x) - f(y)\rvert$이므로 위의 공식에 의하여 $\lvert f\rvert$의 진동은 $f$의 진동 이하이고 $U(P, \lvert f\rvert) - L(P, \lvert f\rvert) \leq U(P, f) - L(P, f)$이다. 같은 방식으로 $\lvert f(x)^2 - f(y)^2\rvert = \lvert f(x) + f(y)\rvert \lvert f(x) - f(y)\rvert \leq 2K \lvert f(x) - f(y)\rvert$이므로 $U(P, f^2) - L(P, f^2) \leq 2K\bigl(U(P, f) - L(P, f)\bigr)$이다. $f$의 $\varepsilon/(2K)$-분할은 이 부등식에 의하여 $f^2$의 $\varepsilon$-분할이므로 [정리 5](#thm5){: data-lid="o1kpw" }에 의하여 $\lvert f\rvert$와 $f^2$은 적분가능하다. $fg = \frac{1}{4}\bigl((f+g)^2 - (f-g)^2\bigr)$이고 $f \pm g$는 [명제 12](#prop12){: data-lid="4gphv" }에 의하여 적분가능하므로 $fg$도 적분가능하다. 마지막으로 $-\lvert f\rvert \leq f \leq \lvert f\rvert$에 [명제 12](#prop12){: data-lid="nurgb" }의 단조성과 선형성을 적용하면 $-\int \lvert f\rvert \leq \int f \leq \int \lvert f\rvert$이다.
:::

[명제 13](#prop13){: data-lid="fk31u" }의 역은 성립하지 않는다.

::: 예시 14 ($\lvert f\rvert$는 적분가능하지만 $f$는 아닌 경우)
$f : [0,1] \to \mathbb{R}$을 유리수에서 $1$, 무리수에서 $-1$로 정의한다. $\lvert f\rvert = 1$은 상수함수이므로 적분가능하다. 그러나 모든 부분구간에서 $m_i = -1$, $M_i = 1$이어서 모든 분할에 대하여 $U(P, f) - L(P, f) = 2$이고, [정리 5](#thm5){: data-lid="vo9vd" }에 의하여 $f$는 적분가능하지 않다.
:::

[명제 13](#prop13){: data-lid="f1uwk" }에서 $f^2$과 $\lvert f\rvert$가 적분가능했던 것은 $y \mapsto y^2$과 $y \mapsto \lvert y\rvert$가 bounded 구간에서 Lipschitz여서 함숫값의 차이를 위에서 $f$의 진동으로 통제할 수 있었기 때문이다. 적분가능한 함수에 임의의 함수를 합성해도 적분가능성이 유지되는 것은 아니다.

::: 예시 15 (적분가능한 함수의 합성)
$f$를 [예시 10](#ex10){: data-lid="ievll" }에서 정의한 함수라 하고 $h : \mathbb{R} \to \mathbb{R}$을 $h(0) = 0$, $y \neq 0$에서 $h(y) = 1$로 정의한다. $h$는 불연속점이 $0$ 하나뿐인 bounded function이므로 [정리 8](#thm8){: data-lid="9drin" }에 의하여 적분가능하고, $f$도 적분가능하다. 그런데 $f(x) > 0$인 것은 $x$가 유리수인 것과 동치이므로 $h \circ f$는 유리수에서 $1$, 무리수에서 $0$인 함수, 곧 [예시 9](#ex9){: data-lid="ktpel" }와 같은 함수이다. 따라서 $h \circ f$는 적분가능하지 않다.
:::

마지막으로 적분구간을 쪼개고 이어 붙이는 성질을 본다.

::: 명제 16 (구간가법성)
$a < c < b$일 때 $f$가 $[a,b]$에서 적분가능한 것은 $[a,c]$와 $[c,b]$에서 각각 적분가능한 것과 동치이며, 이때

$$\int_a^b f = \int_a^c f + \int_c^b f$$

이다.
:::

::: 증명
$c$를 분점으로 가지는 $[a,b]$의 분할 $P$는 $[a,c]$의 분할 $P_1$과 $[c,b]$의 분할 $P_2$의 합집합이고, 상합과 하합은 각각 두 부분의 합으로 갈라진다. 곧 $U(P, f) = U(P_1, f) + U(P_2, f)$, $L(P, f) = L(P_1, f) + L(P_2, f)$이고

$$U(P, f) - L(P, f) = \bigl(U(P_1, f) - L(P_1, f)\bigr) + \bigl(U(P_2, f) - L(P_2, f)\bigr)$$

이다. 두 괄호는 모두 $0$ 이상이므로 좌변이 $\varepsilon$ 미만인 것과 두 괄호가 모두 $\varepsilon$ 미만인 것은 (각각 $\varepsilon$을 적절히 바꾸면) 서로 필요충분이다. 한편 임의의 분할은 $c$를 추가해도 [보조정리 2](#lem2){: data-lid="oyewb" }에 의하여 $U - L$이 커지지 않으므로, 판정에는 $c$를 분점으로 가지는 분할만 보면 충분하다. [정리 5](#thm5){: data-lid="fcqw8" }에 의하여 적분가능성의 동치가 따른다.

적분값은, 적분가능할 때 $\int_a^b f \leq U(P, f) = U(P_1, f) + U(P_2, f) < \int_a^c f + \int_c^b f + \varepsilon$이고 같은 방식으로 $\int_a^b f \geq L(P,f) > \int_a^c f + \int_c^b f - \varepsilon$이므로 $\varepsilon$이 임의임에서 얻어진다.
:::

---

**참고문헌**

**[Rud]** W. Rudin, *Principles of mathematical analysis*, 3rd ed., McGraw-Hill, 1976.
