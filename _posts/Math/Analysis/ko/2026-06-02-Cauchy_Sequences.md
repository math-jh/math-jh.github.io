---
title: "Cauchy 수열과 완비성"
description: "극한값을 모르는 채로 수렴을 판정하게 해 주는 Cauchy 수열을 정의하고, 실수에서 수렴과 Cauchy가 동치임을 Bolzano–Weierstrass 정리로 증명한다. 유리수에서의 반례, 인접한 항의 차가 0으로 가도 Cauchy가 아닌 예, 인접 차가 등비로 줄어드는 수열의 수렴을 함께 다룬다."
excerpt: "Cauchy 수열의 정의, 실수에서의 Cauchy 판정법, 유리수 반례와 수축수열"

categories: [Math / Analysis]
permalink: /ko/math/analysis/cauchy_sequences
sidebar: 
    nav: "analysis-ko"

date: 2026-06-02
weight: 5

published: false

---

수열 $(a_n)$이 $L$로 수렴한다는 [§수열의 수렴, ⁋정의 1](/ko/math/analysis/convergence_of_sequences#def1)는 극한 $L$을 미리 알고 있어야 쓸 수 있다. 극한을 모르고 수렴을 확정하는 방법은 [§수열의 수렴, ⁋정리 8](/ko/math/analysis/convergence_of_sequences#thm8) 하나뿐이었다. 점화식이나 급수로 정의된 수열은 대개 단조하지 않고, 극한값은 수렴을 알고 난 뒤에야 구할 수 있다. 이 글의 목표는 항들 서로 사이의 거리만으로 수렴을 판정하는 조건, 곧 Cauchy 조건이 실수에서는 수렴과 동치임을 보이는 것이다. 이 동치는 $\mathbb{Q}$에서는 성립하지 않으며, 그 차이가 실수의 완비성이 하는 일을 드러낸다.

## Cauchy 수열

::: 정의 1
수열 $(a_n)$이 *Cauchy 수열<sub>Cauchy sequence</sub>*이라는 것은, 임의의 $\varepsilon > 0$에 대하여 자연수 $N$이 존재하여 모든 $m, n \geq N$에 대해 $\lvert a_m - a_n\rvert < \varepsilon$이 성립하는 것이다.
:::

수렴의 정의는 항과 극한 사이의 거리를 통제하지만, 이 정의는 항과 항 사이의 거리를 통제한다. 여기서 $m, n$은 $N$ 이상의 임의의 두 첨자이며, 서로 인접할 필요가 없다. 이 점은 뒤의 예시에서 결정적으로 쓰인다.

수렴하는 수열은 Cauchy이다.

::: 명제 2
수렴하는 실수열은 Cauchy 수열이다.
:::

::: 증명
$a_n \rightarrow L$이라 하고 $\varepsilon > 0$을 임의로 잡는다. 두 항의 거리를 $L$을 경유하는 두 거리의 합으로 쪼갤 것이므로, 각각을 $\varepsilon/2$ 미만으로 만들어 합이 $\varepsilon$ 미만이 되도록 $N$을 고른다. 즉 $n \geq N$이면 $\lvert a_n - L\rvert < \varepsilon/2$인 $N$을 잡는다. 그러면 $m, n \geq N$에 대하여 삼각부등식에 의해

$$\lvert a_m - a_n\rvert \leq \lvert a_m - L\rvert + \lvert L - a_n\rvert < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon$$

이다.
:::

::: 명제 3
Cauchy 수열은 bounded이다.
:::

::: 증명
$\varepsilon = 1$에 대응하는 $N$을 잡으면, $n \geq N$에서 $\lvert a_n - a_N\rvert < 1$이므로 $\lvert a_n\rvert < \lvert a_N\rvert + 1$이다. 나머지 항은 유한개이므로

$$M = \max\{\lvert a_1\rvert, \ldots, \lvert a_{N-1}\rvert, \lvert a_N\rvert + 1\}$$

로 두면 모든 $n$에서 $\lvert a_n\rvert \leq M$이다.
:::

## Cauchy 판정법

이제 역방향을 보인다. 증명의 구조는 다음과 같다. Cauchy 수열은 [명제 3](#prop3)에 의해 bounded이므로 [§부분수열과 Bolzano–Weierstrass 정리, ⁋정리 4](/ko/math/analysis/bolzano_weierstrass#thm4)에 의해 수렴 부분수열을 가진다. 그 극한을 $L$이라 하면, 부분수열의 항들이 $L$에 가깝고 수열의 항들이 서로 가까우므로 전체 수열의 항도 $L$에 가깝다.

::: 정리 4 (Cauchy 판정법)
실수열 $(a_n)$이 수렴하는 것은 $(a_n)$이 Cauchy 수열인 것과 동치이다.
:::

::: 증명
수렴하면 Cauchy라는 것은 [명제 2](#prop2)이다. 역으로 $(a_n)$이 Cauchy 수열이라 하자. [명제 3](#prop3)에 의해 $(a_n)$은 bounded이므로, [§부분수열과 Bolzano–Weierstrass 정리, ⁋정리 4](/ko/math/analysis/bolzano_weierstrass#thm4)에 의해 수렴하는 부분수열 $a_{n_k} \rightarrow L$이 존재한다.

$a_n \rightarrow L$을 보인다. $\varepsilon > 0$을 임의로 잡는다. $\lvert a_n - L\rvert$를 $\lvert a_n - a_{n_k}\rvert$와 $\lvert a_{n_k} - L\rvert$의 합으로 쪼갤 것이므로, 각각을 $\varepsilon/2$ 미만으로 만든다. Cauchy 조건에 의해 $m, n \geq N$이면 $\lvert a_m - a_n\rvert < \varepsilon/2$인 $N$이 존재한다. 부분수열의 수렴에 의해 $K$가 존재하여 $k \geq K$이면 $\lvert a_{n_k} - L\rvert < \varepsilon/2$이다. 이제 $k \geq \max\{K, N\}$을 하나 고르면 $n_k \geq k \geq N$이므로 $a_{n_k}$는 두 조건을 모두 만족한다. 따라서 모든 $n \geq N$에 대하여

$$\lvert a_n - L\rvert \leq \lvert a_n - a_{n_k}\rvert + \lvert a_{n_k} - L\rvert < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon$$

이고, $a_n \rightarrow L$이다.
:::

이 증명에서 실수의 성질이 쓰인 곳은 Bolzano–Weierstrass 정리뿐이며, 이는 [§실수의 완비성, ⁋정의 3](/ko/math/analysis/completeness_of_reals#def3)에서 나온다. 같은 논증이 다른 공간에서 어떻게 깨지는지를 다음 예시가 보여 준다.

## 유리수에서의 반례

Cauchy 수열이 항상 수렴하는 성질은 $\mathbb{R}$의 성질이며, 수렴하는 점이 공간 안에 있어야 한다는 조건이 숨어 있다. 같은 정의를 $\mathbb{Q}$에서 적용하면 판정법이 깨진다.

::: 예시 5 (유리수에서 수렴하지 않는 Cauchy 수열)
$a_n = \lfloor 10^n\sqrt{2}\rfloor/10^n$, 즉 $\sqrt{2}$를 소수점 아래 $n$째 자리에서 버린 값이라 하자($a_1 = 1.4$, $a_2 = 1.41$, $a_3 = 1.414, \ldots$). 각 $a_n$은 유리수이고 $0 \leq \sqrt{2} - a_n < 10^{-n}$이다. $m \geq n \geq N$이면 $a_m$과 $a_n$ 모두 구간 $(\sqrt{2} - 10^{-N},\ \sqrt{2}]$에 들어 있으므로

$$\lvert a_m - a_n\rvert < 10^{-N}$$

이다. 임의의 $\varepsilon > 0$에 대해 $10^{-N} < \varepsilon$이 되도록 $N$을 잡으면 $(a_n)$은 Cauchy이다. 이 검증에는 극한이 등장하지 않는다.

그러나 $(a_n)$은 $\mathbb{Q}$ 안에서 수렴하지 않는다. $a_n \rightarrow q$인 유리수 $q$가 있다면, 이 수렴은 $\mathbb{R}$에서도 성립한다. 그런데 $0 \leq \sqrt{2} - a_n < 10^{-n}$이므로 $\mathbb{R}$에서 $a_n \rightarrow \sqrt{2}$이고, [§수열의 수렴, ⁋명제 2](/ko/math/analysis/convergence_of_sequences#prop2)에 의해 $q = \sqrt{2}$가 된다. $\sqrt{2}$가 무리수이므로 모순이다.
:::

$\mathbb{R}$에서는 같은 수열이 $\sqrt{2}$로 수렴한다. 완비성은 이처럼 Cauchy 수열이 모이는 점이 빠져 있는 일이 없다는 뜻이다. 거리공간으로 일반화되면 이것이 *완비 거리공간*의 정의가 된다.

## 인접한 항의 차와 Cauchy 조건

$\lvert a_{n+1} - a_n\rvert \rightarrow 0$은 Cauchy 조건에서 $m = n+1$인 경우만 남긴 것에 해당한다. 이 조건은 Cauchy 조건에서 따라 나오지만 그 역은 성립하지 않는다. 인접한 항의 차가 작아도 작은 걸음이 쌓여 먼 거리가 될 수 있기 때문이다.

::: 예시 6 (조화급수의 부분합과 $\log n$)
$s_n = \sum_{k=1}^{n} 1/k$이라 하면 $s_{n+1} - s_n = 1/(n+1) \rightarrow 0$이다. 그러나 $(s_n)$은 Cauchy가 아니다. 임의의 $N$에 대해 $n = N$, $m = 2N$을 택하면 $m, n \geq N$이고

$$\begin{aligned}
s_{2N} - s_N &= \sum_{k=N+1}^{2N} \frac{1}{k} \\
&\geq N \cdot \frac{1}{2N} = \frac{1}{2}
\end{aligned}$$

이다. 따라서 $\varepsilon = 1/2$에 대하여 어떤 $N$을 잡아도 Cauchy 조건이 성립하지 않는다. [정리 4](#thm4)에 의해 $(s_n)$은 수렴하지 않는다.

$a_n = \log n$도 마찬가지이다. 평균값 정리에 의해 $\log(n+1) - \log n \leq 1/n \rightarrow 0$이지만, $\log(2N) - \log N = \log 2$이므로 $\varepsilon = \log 2$에 대하여 Cauchy 조건이 성립하지 않는다. 사실 이 수열은 bounded가 아니므로 [명제 3](#prop3)의 대우로도 Cauchy가 아님이 바로 나온다.
:::

이 예시에서 위반된 것은 Cauchy 조건에서 $m$과 $n$이 서로 멀리 떨어질 수 있다는 점이다. $N$ 이상의 인접하지 않은 첨자 쌍을 함께 통제해야 한다는 것이 Cauchy 조건의 요점이며, 인접 차만으로는 수렴을 보장하지 못한다. 이를 보장하려면 인접 차가 합쳐서 유한할 정도로 빠르게 줄어든다는 추가 조건이 필요하다. 다음 명제는 그러한 조건의 표준적인 형태이다.

## Contractive sequence

::: 명제 7 (Contractive sequence)
실수열 $(a_n)$에 대하여 $0 < c < 1$이 존재하여 모든 $n \geq 1$에서

$$\lvert a_{n+2} - a_{n+1}\rvert \leq c\lvert a_{n+1} - a_n\rvert$$

이 성립하면, $(a_n)$은 Cauchy 수열이고 따라서 수렴한다.
:::

::: 증명
$d_n = \lvert a_{n+1} - a_n\rvert$이라 하자. 가정은 $d_{n+1} \leq c d_n$이므로 귀납적으로 $d_n \leq c^{n-1} d_1$이다. $m > n$이면 삼각부등식과 등비급수의 합에 의해

$$\begin{aligned}
\lvert a_m - a_n\rvert &\leq \sum_{k=n}^{m-1} d_k \\
&\leq d_1 \sum_{k=n}^{m-1} c^{k-1} \\
&\leq d_1 \cdot \frac{c^{n-1}}{1-c}
\end{aligned}$$

이다. $0 < c < 1$이므로 $c^{n-1} \rightarrow 0$이다. 따라서 $\varepsilon > 0$이 주어지면 $d_1 c^{N-1}/(1-c) < \varepsilon$인 $N$을 잡을 수 있고, $m > n \geq N$에서 $\lvert a_m - a_n\rvert \leq d_1 c^{n-1}/(1-c) \leq d_1 c^{N-1}/(1-c) < \varepsilon$이다. $m = n$인 경우는 자명하고 $m < n$인 경우는 $m$과 $n$을 바꾸면 된다. 따라서 $(a_n)$은 Cauchy이고, [정리 4](#thm4)에 의해 수렴한다.
:::

이 명제는 극한값에 대한 정보를 주지 않는다. 수렴이 확보된 뒤에는 점화식의 양변에 극한을 취해 극한값을 구한다.

::: 예시 8 ($a_{n+1} = 1 + 1/a_n$)
$a_1 = 1$, $a_{n+1} = 1 + 1/a_n$으로 정의된 수열은 수렴한다. 귀납적으로 $a_n \geq 1$이므로 $a_{n+1} \leq 2$이고, 이어서 $n \geq 2$에서 $1 \leq a_n \leq 2$이다. 또 $n \geq 3$이면 $a_{n-1} \leq 2$이므로 $a_n = 1 + 1/a_{n-1} \geq 3/2$이다. 따라서 $n = 2$에서 $a_2 a_1 = 2$, $n = 3$에서 $a_3 a_2 = 3$이고 $n \geq 4$에서는 $a_n a_{n-1} \geq 9/4$이므로, 모든 $n \geq 2$에서 $a_n a_{n-1} \geq 2$이다. 점화식에서

$$a_{n+1} - a_n = \frac{1}{a_n} - \frac{1}{a_{n-1}} = \frac{a_{n-1} - a_n}{a_n a_{n-1}}$$

이므로 $n \geq 2$에서 $\lvert a_{n+1} - a_n\rvert \leq \frac{1}{2}\lvert a_n - a_{n-1}\rvert$이다. 첫 항부터 수축 조건이 성립하는 것은 아니므로, 수열 $b_n = a_{n+1}$에 [명제 7](#prop7)을 적용한다. $(b_n)$이 수렴하므로 $(a_n)$도 수렴하고, 극한 $L$은 $L \geq 1$이며 $L = 1 + 1/L$을 만족한다. 즉 $L^2 - L - 1 = 0$이고 $L = (1 + \sqrt{5})/2$이다.
:::

---

**참고문헌**

**[Rud]** W. Rudin, *Principles of mathematical analysis*, 3rd ed., McGraw-Hill, 1976.
