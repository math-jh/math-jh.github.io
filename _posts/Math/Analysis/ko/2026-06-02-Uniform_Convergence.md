---
title: "균등수렴"
description: "함수열의 균등수렴을 상한노름으로 정의하고 균등 Cauchy 판정과 Weierstrass M-판정을 증명한다. 균등극한이 연속성을 보존하고 적분·미분과 극한이 교환되는 조건을 밝히며, Dini 정리와 각 가정이 필요한 반례를 다룬다."
excerpt: "균등수렴, M-판정, 연속성·적분·미분과 극한의 교환, Dini 정리"

categories: [Math / Analysis]
permalink: /ko/math/analysis/uniform_convergence
sidebar: 
    nav: "analysis-ko"

date: 2026-06-02
weight: 21

published: false

---

[§함수열과 점별수렴, ⁋예시 2](/ko/math/analysis/sequences_of_functions#ex2), [§함수열과 점별수렴, ⁋예시 3](/ko/math/analysis/sequences_of_functions#ex3), [§함수열과 점별수렴, ⁋예시 4](/ko/math/analysis/sequences_of_functions#ex4)에서 보았듯이 점별수렴은 연속성도, 적분값도, 도함수도 극한으로 넘겨 주지 못한다. 점별수렴은 각 점 $x$마다 따로 $N$을 허용하기 때문에, 점이 바뀜에 따라 필요한 $N$이 한없이 커질 수 있다. 이 글에서는 $N$을 모든 점에 공통으로 요구하는 수렴을 정의하고, 그 아래에서 세 가지 교환이 성립하는 조건을 정리한다.

## 균등수렴과 상한노름

::: 정의 1
집합 $E$ 위의 함수열 $(f_n)$이 $f$로 *균등수렴<sub>uniform convergence</sub>*한다는 것은, 임의의 $\varepsilon > 0$에 대하여 $x$에 무관한 $N$이 존재하여 모든 $n \geq N$과 모든 $x \in E$에 대해

$$\lvert f_n(x) - f(x)\rvert < \varepsilon$$

이 성립하는 것이다.
:::

점별수렴의 정의에서는 $N$이 $\varepsilon$과 $x$에 모두 의존하고, 균등수렴에서는 $\varepsilon$에만 의존한다. 이 차이는 상한으로 표현된다. $\lVert g\rVert_\infty = \sup_{x \in E}\lvert g(x)\rvert \in [0, \infty]$로 두면, [정의 1](#def1)의 조건은 $n \geq N$일 때 $\lVert f_n - f\rVert_\infty \leq \varepsilon$이 성립하는 것과 같다. 모든 $x$에서 $<\varepsilon$이면 상한은 $\leq \varepsilon$이고, 역으로 상한이 $\leq \varepsilon/2$이면 모든 $x$에서 $<\varepsilon$이므로 $\varepsilon$을 반으로 줄여 두 조건이 서로 따라 나온다. 따라서

$$f_n \rightarrow f \text{ 균등수렴} \iff \lVert f_n - f\rVert_\infty \rightarrow 0$$

이다. 균등수렴 여부는 $f$를 알고 있으면 수열 $\lVert f_n - f\rVert_\infty$를 계산해서 판정한다. 균등수렴은 정의역 $E$에도 의존하므로 어느 집합 위에서의 수렴인지를 항상 밝혀야 한다.

::: 예시 2
$[0, \infty)$ 위에서 $f_n(x) = nx e^{-nx}$는 점별로 $0$에 수렴한다. $x = 0$에서는 모든 항이 $0$이고, $x > 0$에서는 $nx e^{-nx} \rightarrow 0$이다. 그러나 $f_n'(x) = n(1 - nx)e^{-nx}$이므로 $f_n$은 $x = 1/n$에서 최댓값 $f_n(1/n) = 1/e$를 가져 $\lVert f_n\rVert_\infty = 1/e$이고, 균등수렴하지 않는다. 최댓값의 위치 $1/n$이 $0$으로 움직이면서 높이는 줄어들지 않는 것이다.

반면 $a > 0$이면 $[a, \infty)$ 위에서는 균등수렴한다. $f_n$은 $x \geq 1/n$에서 감소하므로 $n \geq 1/a$이면 $\lVert f_n\rVert_{\infty} = f_n(a) = na e^{-na}$이고, 이것이 $0$으로 가기 때문이다.
:::

## 균등 Cauchy 조건

극한함수를 모르는 채 균등수렴을 확인하려면 수열의 Cauchy 조건에 해당하는 판정이 필요하다 ([§Cauchy 수열과 완비성, ⁋정의 1](/ko/math/analysis/cauchy_sequences#def1)).

::: 명제 3 (균등 Cauchy 판정)
실수값 함수열 $(f_n)$이 $E$ 위에서 어떤 함수로 균등수렴하는 것은, 임의의 $\varepsilon > 0$에 대하여 $x$에 무관한 $N$이 존재하여 모든 $m, n \geq N$과 모든 $x \in E$에 대해 $\lvert f_m(x) - f_n(x)\rvert < \varepsilon$이 성립하는 것과 동치이다. 이 조건을 만족하는 열을 *균등 Cauchy<sub>uniformly Cauchy</sub>*라 한다.
:::

::: 증명
$f_n \rightarrow f$ 균등수렴이라 하자. $\varepsilon > 0$에 대해 $n \geq N$이면 $\lVert f_n - f\rVert_\infty < \varepsilon/2$인 $N$을 잡으면, $m, n \geq N$일 때 모든 $x$에 대해

$$\lvert f_m(x) - f_n(x)\rvert \leq \lvert f_m(x) - f(x)\rvert + \lvert f(x) - f_n(x)\rvert < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon$$

이다.

역으로 $(f_n)$이 균등 Cauchy라 하자. 각 $x$를 고정하면 $(f_n(x))$는 Cauchy 수열이므로 [§Cauchy 수열과 완비성, ⁋정리 4](/ko/math/analysis/cauchy_sequences#thm4)에 의해 수렴한다. 그 극한을 $f(x)$라 하자. $\varepsilon > 0$에 대해 균등 Cauchy 조건의 $N$을 잡으면, $n \geq N$이고 모든 $x$에 대해 $m \geq N$인 모든 $m$에서 $\lvert f_m(x) - f_n(x)\rvert < \varepsilon$이다. 여기서 $x$와 $n$을 고정하고 $m \rightarrow \infty$로 보내면 $\lvert f(x) - f_n(x)\rvert \leq \varepsilon$을 얻는다. 이것이 모든 $x$와 $n \geq N$에서 성립하므로 $\lVert f - f_n\rVert_\infty \leq \varepsilon$이고, 균등수렴이 증명되었다. 극한을 취한 뒤에는 부등호가 등호를 포함하는 $\leq$로 바뀌는 점에 주의한다.
:::

## Weierstrass M-판정

function series $\sum f_n$의 균등수렴은 부분합 $s_N = \sum_{n=1}^N f_n$의 균등수렴이다.

::: 정리 4 (Weierstrass M-판정)
$E$ 위에서 모든 $x$에 대해 $\lvert f_n(x)\rvert \leq M_n$이고 수치급수 $\sum M_n$이 수렴하면, $\sum f_n$은 $E$ 위에서 균등수렴하고 각 점에서 절대수렴한다.
:::

::: 증명
$m > n$일 때 모든 $x$에 대해

$$\lvert s_m(x) - s_n(x)\rvert = \Bigl\lvert \sum_{k=n+1}^m f_k(x)\Bigr\rvert \leq \sum_{k=n+1}^m M_k$$

이다. $\sum M_k$가 수렴하므로 $\varepsilon > 0$에 대해 $m > n \geq N$이면 $\sum_{k=n+1}^m M_k < \varepsilon$인 $N$이 있고, 이 $N$은 $x$에 의존하지 않는다([§무한급수와 수렴판정법, ⁋정리 3](/ko/math/analysis/series#thm3)). 따라서 $(s_n)$은 균등 Cauchy이고 [명제 3](#prop3)에 의해 균등수렴한다. 각 $x$에서 $\sum\lvert f_n(x)\rvert \leq \sum M_n < \infty$이므로 절대수렴도 성립한다.
:::

$M_n$은 각 항의 상한 $\lVert f_n\rVert_\infty$로 잡는 것이 가장 좋고, 그 값을 계산해서 수치급수 판정법으로 수렴 여부를 보면 된다. 가령 $\sum \sin(nx)/n^2$은 $\lvert\sin(nx)\rvert \leq 1$로 $x$ 의존성이 사라져 $M_n = 1/n^2$을 얻고 [§무한급수와 수렴판정법, ⁋명제 9](/ko/math/analysis/series#prop9)에 의하여 $\sum 1/n^2$이 수렴하므로 $\mathbb{R}$ 전체에서 균등수렴한다. M-판정은 충분조건일 뿐이다. 상수함수열 $f_n \equiv (-1)^n/n$을 항으로 하는 급수는 균등수렴하지만 $\lVert f_n\rVert_\infty = 1/n$이어서 $\sum M_n$은 발산한다.

::: 예시 5 (정의역에 따라 달라지는 균등수렴)
기하급수 $\sum_{n=0}^\infty x^n$은 $0 < r < 1$에 대해 $[-r, r]$ 위에서 $M_n = r^n$으로 M-판정을 통과하므로 균등수렴한다. 그러나 $(-1, 1)$ 전체에서는 균등수렴하지 않는다. 합은 $1/(1-x)$이고 부분합과의 차이는 $\lvert x^{N+1}/(1-x)\rvert$인데, $x \rightarrow 1^-$일 때 이 값이 한없이 커지므로 $\lVert\cdot\rVert_\infty = \infty$이기 때문이다. 합집합 $(-1,1) = \bigcup_r [-r, r]$의 각 compact subset에서는 균등수렴하지만 전체에서는 하지 못하는 현상이다.
:::

## 연속성의 보존

::: 정리 6
$E$ 위의 연속함수들의 열 $(f_n)$이 $f$로 균등수렴하면 $f$도 $E$ 위에서 연속이다.
:::

::: 증명
$a \in E$와 $\varepsilon > 0$을 잡는다. 균등수렴으로 $\lVert f_n - f\rVert_\infty < \varepsilon/3$인 $n$을 하나 고정한다. $f_n$이 $a$에서 연속이므로 $\lvert x - a\rvert < \delta$이면 $\lvert f_n(x) - f_n(a)\rvert < \varepsilon/3$인 $\delta > 0$이 있다. 이때 $\lvert x - a\rvert < \delta$인 $x \in E$에 대해

$$\lvert f(x) - f(a)\rvert \leq \lvert f(x) - f_n(x)\rvert + \lvert f_n(x) - f_n(a)\rvert + \lvert f_n(a) - f(a)\rvert < \varepsilon$$

이다. 가운데 항은 $n$을 고정한 뒤에 $\delta$를 고르므로 통제되고, 양 끝의 항은 균등성 덕분에 $x$와 $a$ 두 점에서 같은 $n$으로 동시에 통제된다. 점별수렴이면 $n$이 $x$마다 달라져서 이 논증이 성립하지 않는다.
:::

연속함수열의 극한이 불연속이면 수렴은 균등하지 않다. $[0,1]$ 위에서 $x^n$이 $x = 1$에서만 $1$을 취하는 함수로 수렴하는 것이 그 예이다. 역은 성립하지 않는다. 극한이 연속이어도 균등수렴하지 않을 수 있고, [예시 2](#ex2)가 그렇다.

## 적분과 극한의 교환

::: 정리 7
$[a,b]$ 위에서 Riemann integrable한 함수들의 열 $(f_n)$이 $f$로 균등수렴하면 $f$도 Riemann integrable이고

$$\lim_{n\rightarrow\infty}\int_a^b f_n = \int_a^b f$$

이다.
:::

::: 증명
$\varepsilon_n = \lVert f_n - f\rVert_\infty$라 하자. 균등수렴이므로 $\varepsilon_n \rightarrow 0$이고, 특히 충분히 큰 $n$에서 $\varepsilon_n < \infty$이다. 이런 $n$에 대해 $f_n - \varepsilon_n \leq f \leq f_n + \varepsilon_n$이고 $f_n$이 bounded이므로 $f$도 bounded이다. 상적분 $\overline{\int}$과 하적분 $\underline{\int}$의 단조성에 의해

$$\int_a^b (f_n - \varepsilon_n) \leq \underline{\int_a^b} f \leq \overline{\int_a^b} f \leq \int_a^b (f_n + \varepsilon_n)$$

이므로 $0 \leq \overline{\int} f - \underline{\int} f \leq 2\varepsilon_n(b-a)$이다. $n \rightarrow \infty$로 보내면 두 적분이 같으므로 $f$는 Riemann integrable이다 ([§Riemann 적분, ⁋정의 4](/ko/math/analysis/riemann_integral#def4)). 이제 같은 부등식과 [§Riemann 적분, ⁋명제 13](/ko/math/analysis/riemann_integral#prop13)에서

$$\Bigl\lvert \int_a^b f_n - \int_a^b f\Bigr\rvert \leq \int_a^b \lvert f_n - f\rvert \leq \varepsilon_n (b - a) \rightarrow 0$$

을 얻는다.
:::

급수에 적용하면 $\sum f_n$이 균등수렴하는 경우 항별 적분 $\int \sum f_n = \sum \int f_n$이 성립한다. 부분합이 유한합이므로 [§Riemann 적분, ⁋명제 12](/ko/math/analysis/riemann_integral#prop12)의 선형성만 쓰면 된다. 균등성이 빠지면 교환이 깨진다.

::: 예시 8
$[0,1]$ 위에서 $f_n(x) = nx(1-x^2)^n$은 연속이고 $0$으로 점별수렴한다. $x = 0, 1$에서는 모든 항이 $0$이고, $0 < x < 1$에서는 $(1-x^2)^n$이 기하급수적으로 줄어 $n$을 이기기 때문이다. 그러나 $u = x^2$으로 [§미적분의 기본정리, ⁋명제 8](/ko/math/analysis/fundamental_theorem_of_calculus#prop8)에 의해 치환하면

$$\int_0^1 f_n = \frac{n}{2}\int_0^1 (1-u)^n \dd{u} = \frac{n}{2(n+1)} \rightarrow \frac{1}{2} \neq 0 = \int_0^1 \lim_{n\rightarrow\infty} f_n$$

이다. 수렴이 균등하지 않다는 것은 $f_n(1/\sqrt{n}) = \sqrt{n}(1 - 1/n)^n$에서도 보인다. $n \geq 2$에서 $(1 - 1/n)^n \geq 1/4$이므로 $\lVert f_n\rVert_\infty \geq \sqrt{n}/4 \rightarrow \infty$이다.
:::

## 미분과 극한의 교환

미분은 적분과 달리 균등수렴만으로는 교환되지 않고, 도함수열의 수렴을 요구해야 한다. 아래 정리에서 $f_n$은 실수값 함수이다.

::: 정리 9
$[a,b]$ 위에서 미분가능한 함수들의 열 $(f_n)$이 다음 두 조건을 만족한다고 하자. 어떤 점 $x_0 \in [a,b]$에서 $(f_n(x_0))$이 수렴하고, 도함수열 $(f_n')$이 $[a,b]$ 위에서 균등수렴한다. 그러면 $(f_n)$은 $[a,b]$ 위에서 어떤 $f$로 균등수렴하고, $f$는 미분가능하며 모든 $x \in [a,b]$에서

$$f'(x) = \lim_{n\rightarrow\infty} f_n'(x)$$

이다.
:::

::: 증명
먼저 [§평균값 정리와 테일러 정리, ⁋정리 3](/ko/math/analysis/mean_value_theorem#thm3)을 $f_n - f_m$에 적용하면, $s \neq t$인 $[a,b]$의 두 점에 대해 $s$와 $t$ 사이의 어떤 점 $\xi$에서

$$\lvert (f_n - f_m)(s) - (f_n - f_m)(t)\rvert = \lvert s - t\rvert \lvert f_n'(\xi) - f_m'(\xi)\rvert \leq \lvert s - t\rvert \lVert f_n' - f_m'\rVert_\infty \tag{$\ast$}$$

이다.

*$f_n$이 균등수렴한다.* $\varepsilon > 0$이 주어지면, $(f_n(x_0))$이 Cauchy이고 $(f_n')$이 균등 Cauchy이므로 $n, m \geq N$에서 $\lvert f_n(x_0) - f_m(x_0)\rvert < \varepsilon/2$이고 $\lVert f_n' - f_m'\rVert_\infty < \varepsilon/(2(b-a))$인 $N$이 있다. $(\ast)$에 $s = x$, $t = x_0$를 넣으면 $\lvert s - t\rvert \leq b - a$이므로 모든 $x$에 대해

$$\lvert f_n(x) - f_m(x)\rvert \leq \lvert (f_n - f_m)(x) - (f_n - f_m)(x_0)\rvert + \lvert f_n(x_0) - f_m(x_0)\rvert < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon$$

이다. $(f_n)$이 균등 Cauchy이므로 [명제 3](#prop3)에 의해 어떤 $f$로 균등수렴한다. ($b-a$로 나눈 것은 $(\ast)$의 우변을 $b-a$로 키워도 $\varepsilon/2$ 이하가 되게 하기 위해서이다.)

*$f'$이 존재하고 $\lim f_n'$과 같다.* $x \in [a,b]$를 고정하고 $t \neq x$에 대해

$$\phi_n(t) = \frac{f_n(t) - f_n(x)}{t - x}, \qquad \phi(t) = \frac{f(t) - f(x)}{t - x}$$

로 둔다. $\phi_n(t) \rightarrow \phi(t)$이고 $t \rightarrow x$일 때 $\phi_n(t) \rightarrow f_n'(x)$이다. $\varepsilon > 0$에 대해 $n, m \geq N$이면 $\lVert f_n' - f_m'\rVert_\infty < \varepsilon/3$인 $N$을 잡는다. $(\ast)$로부터 모든 $t \neq x$에 대해 $\lvert\phi_n(t) - \phi_m(t)\rvert \leq \varepsilon/3$이다. 이 식에서 $t \rightarrow x$로 보내면 $\lvert f_n'(x) - f_m'(x)\rvert \leq \varepsilon/3$이므로 $(f_n'(x))$는 Cauchy이고 극한 $g(x)$를 가지며, $m \rightarrow \infty$로 보내면 $\lvert f_n'(x) - g(x)\rvert \leq \varepsilon/3$이다. 또 같은 식에서 $m \rightarrow \infty$로 보내면 모든 $t \neq x$에 대해 $\lvert \phi_n(t) - \phi(t)\rvert \leq \varepsilon/3$이다. 이제 $n = N$으로 고정하고, $\phi_N(t) \rightarrow f_N'(x)$이므로 $0 < \lvert t - x\rvert < \delta$이면 $\lvert\phi_N(t) - f_N'(x)\rvert < \varepsilon/3$인 $\delta$를 잡으면, 이 $t$에 대해

$$\lvert \phi(t) - g(x)\rvert \leq \lvert\phi(t) - \phi_N(t)\rvert + \lvert\phi_N(t) - f_N'(x)\rvert + \lvert f_N'(x) - g(x)\rvert < \varepsilon$$

이다. 따라서 $f'(x) = g(x) = \lim f_n'(x)$이다.
:::

두 극한 $t \rightarrow x$와 $n \rightarrow \infty$를 바꾸는 단계에서 $(f_n')$의 균등 Cauchy 성질이 모든 $t$에 대해 $\phi_n - \phi_m$을 한꺼번에 통제하는 데 쓰였다. [정리 9](#thm9)의 각 가정이 필요한 이유는 다음 반례들에서 드러난다.

::: 예시 10
(1) 도함수열의 균등수렴이 빠진 경우. $\mathbb{R}$ 위에서 $f_n(x) = \sin(nx)/\sqrt{n}$은 $\lVert f_n\rVert_\infty = 1/\sqrt{n} \rightarrow 0$이므로 $0$으로 균등수렴한다. 그러나 $f_n'(0) = \sqrt{n} \rightarrow \infty$이어서 $\lim f_n'(0) \neq 0 = (\lim f_n)'(0)$이다. $f_n$의 균등수렴만으로는 도함수열이 수렴하지도 않는다.

(2) 균등수렴하는 $f_n$의 극한이 미분가능하지 않을 수도 있다. $f_n(x) = \sqrt{x^2 + 1/n^2}$는 매끄럽고 $0 \leq f_n(x) - \lvert x\rvert = (1/n^2)/(f_n(x) + \lvert x\rvert) \leq 1/n$이므로 $\lvert x\rvert$로 균등수렴하는데, $\lvert x\rvert$는 $0$에서 미분불가능하다. 이 경우 $f_n'(x) = x/\sqrt{x^2 + 1/n^2}$는 $x = 0$ 근처에서 균등수렴하지 않는다.

(3) 한 점에서의 수렴이 빠진 경우. 상수함수 $f_n \equiv n$은 $f_n' \equiv 0$이 균등수렴하지만 $(f_n)$ 자체는 어느 점에서도 수렴하지 않는다.
:::

## Dini 정리

균등수렴하지 않는 수렴이 연속함수의 극한으로 일어나는 것을 막는 조건으로 compactness와 단조성이 있다. 연속함수열의 점별극한이 연속이고 수렴이 단조적이면, 컴팩트 집합 위에서는 점별수렴이 곧 균등수렴이다.

::: 정리 11 (Dini)
$K$가 컴팩트 거리공간이고 $f_n$, $f$가 $K$ 위의 연속함수이며 모든 $x \in K$에서 $f_n(x) \rightarrow f(x)$이고 $f_n(x) \geq f_{n+1}(x)$ ($n \geq 1$)라 하자. 그러면 $f_n \rightarrow f$는 $K$ 위에서 균등하다.
:::

::: 증명
$g_n = f_n - f$로 두면 $g_n$은 연속이고 $g_n \geq g_{n+1} \geq 0$이며 모든 점에서 $g_n(x) \rightarrow 0$이다. $\varepsilon > 0$을 잡고 $K_n = \{x \in K : g_n(x) \geq \varepsilon\}$이라 하자. $g_n$이 연속이므로 $K_n$은 $K$의 closed subset이고, 따라서 컴팩트이다. $g_{n+1} \leq g_n$이므로 $K_{n+1} \subseteq K_n$이다. 어떤 $x$가 모든 $K_n$에 속하면 모든 $n$에서 $g_n(x) \geq \varepsilon$이어서 $g_n(x) \rightarrow 0$에 모순이므로 $\bigcap_n K_n = \emptyset$이다. 모든 $K_n$이 비어 있지 않다면 비어 있지 않은 컴팩트 집합의 감소열이 되어 교집합이 비어 있지 않으므로 ([§컴팩트성, ⁋정리 10](/ko/math/analysis/compactness#thm10)), 어떤 $K_N$은 공집합이다. $K_N = \emptyset$이면 $n \geq N$에서 $K_n \subseteq K_N$도 공집합이므로 모든 $x \in K$에 대해 $0 \leq g_n(x) < \varepsilon$이다.
:::

$f_n(x) \leq f_{n+1}(x)$인 증가열의 경우에는 $-f_n$에 [정리 11](#thm11)을 적용하면 된다. [정리 11](#thm11)의 네 가정, 곧 compactness, 극한의 연속성, 연속성, 단조성은 각각 필요하다.

::: 예시 12
(1) compactness가 빠진 경우. $[0,1)$ 위에서 $x^n$은 연속이고 $n$에 대해 감소하며 연속함수 $0$으로 점별수렴한다. 그러나 $\lVert x^n\rVert_\infty = 1$이어서 균등수렴하지 않는다.

(2) 극한의 연속성이 빠진 경우. $[0,1]$은 컴팩트이고 $x^n$은 연속이며 감소하지만 극한이 $x = 1$에서만 $1$인 함수여서 불연속이고, 균등수렴하지 않는다. [정리 6](#thm6)에 의해 연속함수열의 균등극한은 연속이어야 하므로, [정리 11](#thm11)의 결론이 성립하려면 극한의 연속성이 필요하다.

(3) 단조성이 빠진 경우. [예시 8](#ex8)의 $f_n(x) = nx(1-x^2)^n$은 컴팩트집합 $[0,1]$ 위의 연속함수이고 연속함수 $0$으로 점별수렴하지만 $\lVert f_n\rVert_\infty \rightarrow \infty$이다. 이 열은 $n$에 대해 단조가 아니다. 각 $x$에서 $f_n(x)$는 처음에는 증가하다가 나중에 $0$으로 줄어든다.
:::

---

**참고문헌**

**[Rud]** W. Rudin, *Principles of mathematical analysis*, 3rd ed., McGraw-Hill, 1976.
