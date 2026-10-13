---
title: "이상적분"
description: "구간이 유계가 아니거나 피적분함수가 유계가 아닌 경우로 Riemann 적분을 확장하는 이상적분을 정의하고, Cauchy 판정, 비교판정, 극한비교판정으로 수렴을 판정한다. 적분 sin x/x의 조건수렴, 적분판정법, 피적분함수가 0으로 가지 않는 수렴 예, 주값과의 차이를 다룬다."
excerpt: "이상적분의 정의, Cauchy 판정·비교판정, 조건수렴, 적분판정법, 주값"

categories: [Math / Analysis]
permalink: /ko/math/analysis/improper_integrals
sidebar: 
    nav: "analysis-ko"

date: 2026-10-13
weight: 18

published: false

---

[§Riemann 적분, ⁋정의 4](/ko/math/analysis/riemann_integral#def4){: data-lid="zfu91" }에서 정의한 적분은 컴팩트구간 위의 bounded function에 대한 것이다. $\int_1^\infty x^{-2}\dd{x}$나 $\int_0^1 x^{-1/2}\dd{x}$처럼 구간이 유계가 아니거나 함수가 유계가 아닌 경우에는 상합과 하합 자체가 의미를 잃는다. 이런 적분은 컴팩트구간 위의 적분을 먼저 구한 다음 구간을 늘리거나 singular point로 접근시키는 극한으로 정의한다. 계산 위주의 설명은 [\[미적분학\] §이상적분, ⁋정의 1](/ko/math/calculus/improper_integrals#def1){: data-lid="xfmio" }과 [\[미적분학\] §이상적분, ⁋정의 2](/ko/math/calculus/improper_integrals#def2){: data-lid="j7k02" }에 있고, 이 글은 수렴 판정을 엄밀하게 다룬다.

## 이상적분의 정의

::: 정의 1
$a \lt \beta \leq \infty$이고 $f : [a,\beta) \rightarrow \mathbb{R}$가 모든 $c \in (a,\beta)$에 대하여 $[a,c]$에서 Riemann integrable이라 하자. 극한

$$\int_a^\beta f(x)\dd{x} = \lim_{c \rightarrow \beta^-} \int_a^c f(x)\dd{x}$$

가 실수로 존재하면 *이상적분<sub>improper integral</sub>* $\int_a^\beta f$가 *수렴*한다고 하고, 그 극한값을 적분값으로 정한다. 극한이 존재하지 않거나 $\pm\infty$이면 *발산*한다고 한다.
:::

$\beta = \infty$이면 구간이 유계가 아닌 경우이고, $\beta$가 유한하며 $f$가 $\beta$ 근방에서 유계가 아니면 함수가 유계가 아닌 경우이다. singular point가 왼쪽 끝점 $\alpha$에 있는 $f : (\alpha, b] \rightarrow \mathbb{R}$에는 $\lim_{c \rightarrow \alpha^+} \int_c^b f$로 같은 방식의 정의를 쓴다. singular point가 양쪽 끝이거나 구간 내부의 점 $c$에 있는 경우에는 singular point에서 구간을 둘로 쪼개어, 두 이상적분이 *각각* 수렴할 때에만 수렴한다고 하고 그 합을 적분값으로 정한다. 쪼개는 점은 어디에 잡아도 상관이 없다. [§Riemann 적분, ⁋명제 16](/ko/math/analysis/riemann_integral#prop16){: data-lid="sz2ci" }에 의하여 $\int_a^b = \int_a^c + \int_c^b$이므로 $\int_a^\beta f$의 수렴 여부는 $\int_c^\beta f$의 수렴 여부와 같기 때문이다. 이후의 정리는 $[a,\beta)$ 형태에 대해 쓰며, 다른 형태는 구간을 쪼개거나 $x \mapsto -x$로 옮겨 같은 방식으로 다룬다.

$f$가 $[a,\beta]$ 전체에서 Riemann integrable이면 이상적분은 새로운 것을 주지 않는다. $\lvert f\rvert \leq M$이라 하면 $\lvert \int_a^\beta f - \int_a^c f\rvert = \lvert\int_c^\beta f\rvert \leq M(\beta - c)$이고 이는 $c \rightarrow \beta^-$에서 $0$으로 가므로, 이상적분은 Riemann 적분과 같은 값으로 수렴한다. 가령 $\sin x/x$는 $x = 0$에서 값 $1$을 주어 연속으로 확장되므로 $\int_0^1 (\sin x/x)\dd{x}$는 보통의 적분이다.

이상적분의 기본 예는 거듭제곱이다.

::: 명제 2 (p-적분)
$p \gt 0$에 대하여 $\int_1^\infty x^{-p}\dd{x}$는 $p \gt 1$일 때 수렴하고 $p \leq 1$일 때 발산한다. $\int_0^1 x^{-p}\dd{x}$는 $p \lt 1$일 때 수렴하고 $p \geq 1$일 때 발산한다.
:::

::: 증명
$p \neq 1$이면 $b \gt 1$에서 [§미적분의 기본정리, ⁋정리 5](/ko/math/analysis/fundamental_theorem_of_calculus#thm5){: data-lid="fa5ee" }에 의하여 $\int_1^b x^{-p}\dd{x} = (b^{1-p} - 1)/(1-p)$이다. $p \gt 1$이면 $b^{1-p} \rightarrow 0$이므로 $1/(p-1)$로 수렴하고, $p \lt 1$이면 $b^{1-p} \rightarrow \infty$이므로 발산한다. $p = 1$이면 $\int_1^b x^{-1}\dd{x} = \ln b \rightarrow \infty$이다. 원점 쪽 적분도 $0 \lt c \lt 1$에서 $\int_c^1 x^{-p}\dd{x} = (1 - c^{1-p})/(1-p)$ ($p \neq 1$), $-\ln c$ ($p = 1$)이므로, $c \rightarrow 0^+$에서 $p \lt 1$일 때만 $1/(1-p)$로 수렴한다.
:::

$[1,\infty)$ 쪽은 $p \gt 1$, $(0,1]$ 쪽은 $p \lt 1$이므로 경계 $p = 1$에서 두 적분이 모두 발산하고, 따라서 $\int_0^\infty x^{-p}\dd{x}$는 어떤 $p$에서도 수렴하지 않는다. 한편 singular point가 있는 적분에 [§미적분의 기본정리, ⁋정리 5](/ko/math/analysis/fundamental_theorem_of_calculus#thm5){: data-lid="p86m2" }를 기계적으로 적용하는 것은 흔한 실수이다. $\int_{-1}^1 x^{-2}\dd{x}$에 원시함수 $-1/x$를 대입하면 $-2$가 나오지만, 피적분함수는 양수인데 적분값이 음수일 수 없다. 이 적분은 $0$에서 쪼개면 $\int_0^1 x^{-2}\dd{x}$가 [명제 2](#prop2){: data-lid="28mgg" }에 의해 발산하므로 이상적분으로서 발산한다. 기본정리는 $[a,b]$에서 적분가능한 도함수에 대한 정리이다.

## Cauchy 판정

극한값을 모르는 채로 수렴만 판정하려면 [§Cauchy 수열과 완비성, ⁋정리 4](/ko/math/analysis/cauchy_sequences#thm4){: data-lid="jgo1r" }의 아이디어를 함수에 적용한다.

::: 명제 3 (Cauchy 판정)
$f : [a,\infty) \rightarrow \mathbb{R}$가 모든 $[a,t]$에서 Riemann integrable이라 하자. $\int_a^\infty f$가 수렴하는 것과 다음이 동치이다. 임의의 $\varepsilon \gt 0$에 대하여 $M$이 존재하여 $b \gt c \gt M$이면 $\lvert\int_c^b f\rvert \lt \varepsilon$이다.
:::

$[a,\beta)$, $\beta$ 유한의 경우에는 "$b \gt c \gt M$"을 "$\beta - \delta \lt c \lt b \lt \beta$"로 바꾸면 증명이 그대로 성립한다.

::: 증명
$F(t) = \int_a^t f$로 두면 $\int_c^b f = F(b) - F(c)$이므로, 주장은 $\lim_{t \rightarrow \infty} F(t)$가 존재하는 것과 $F$가 Cauchy 조건을 만족하는 것의 동치이다.

수렴하면 극한을 $L$이라 하고 $\varepsilon/2$에 대한 $M$을 잡는다. $t \gt M$이면 $\lvert F(t) - L\rvert \lt \varepsilon/2$이므로 $b \gt c \gt M$에서 $\lvert F(b) - F(c)\rvert \leq \lvert F(b) - L\rvert + \lvert L - F(c)\rvert \lt \varepsilon$이다.

역으로 Cauchy 조건을 가정하자. 수열 $x_n = F(a+n)$은 $a + n \gt M$인 $n$에서 $\lvert x_n - x_m\rvert \lt \varepsilon$이므로 Cauchy 수열이고, [§Cauchy 수열과 완비성, ⁋정리 4](/ko/math/analysis/cauchy_sequences#thm4){: data-lid="vryvk" }에 의하여 어떤 $L$로 수렴한다. 이제 $\varepsilon \gt 0$이 주어졌을 때 $\varepsilon/2$에 대한 $M$을 잡고, $a + N \gt M$이면서 $\lvert x_N - L\rvert \lt \varepsilon/2$인 $N$을 고른다. 이런 $N$은 $x_n \rightarrow L$이므로 충분히 큰 $N$에서 존재한다. $t \gt M$이면 $\lvert F(t) - L\rvert \leq \lvert F(t) - F(a+N)\rvert + \lvert x_N - L\rvert \lt \varepsilon$이다. 여기서 $\varepsilon/2$씩 나눈 것은 두 항을 합쳐 $\varepsilon$ 안에 넣기 위해서이다.
:::

수열만으로는 충분하지 않다는 점에 주의한다. $F(a+n)$이 수렴해도 $F(t)$는 $t$가 정수 사이를 움직이는 동안 발산할 수 있고, 위 증명의 마지막 단계가 그 틈을 메운다.

## 절대수렴

::: 정리 4
$f$가 모든 $[a,t]$에서 Riemann integrable이고 $\int_a^\infty \lvert f\rvert$가 수렴하면 $\int_a^\infty f$도 수렴한다.
:::

::: 증명
[§Riemann 적분, ⁋명제 13](/ko/math/analysis/riemann_integral#prop13){: data-lid="inmdu" }에 의하여 Riemann integrable한 함수의 절댓값도 Riemann integrable이므로 $\int_c^b \lvert f\rvert$가 의미를 가지고, 같은 명제에 의해 $\lvert\int_c^b f\rvert \leq \int_c^b \lvert f\rvert$이다. $\varepsilon \gt 0$이 주어지면 $\int_a^\infty \lvert f\rvert$에 [명제 3](#prop3){: data-lid="9qg28" }을 적용하여 $b \gt c \gt M$에서 $\int_c^b \lvert f\rvert \lt \varepsilon$이 되는 $M$을 얻는다. 같은 $M$에 대해 $\lvert\int_c^b f\rvert \lt \varepsilon$이므로, [명제 3](#prop3){: data-lid="ohnai" }에 의해 $\int_a^\infty f$가 수렴한다.
:::

$\int_a^\infty \lvert f\rvert$가 수렴할 때 $\int_a^\infty f$가 *절대수렴*한다고 하고, 수렴하지만 절대수렴하지 않을 때 *조건수렴*한다고 한다. [정리 4](#thm4){: data-lid="7ecdc" }의 역은 성립하지 않으며, 반례는 아래에서 구한다.

## 비교판정

$f \geq 0$이면 $F(t) = \int_a^t f$가 $t$에 대해 증가하므로 수렴은 단조수렴의 문제가 되고, 극한값을 몰라도 상계만으로 판정이 된다.

::: 정리 5 (비교판정)
$f, g : [a,\beta) \rightarrow \mathbb{R}$가 각 $[a,t]$에서 Riemann integrable이고 $0 \leq f \leq g$라 하자. $\int_a^\beta g$가 수렴하면 $\int_a^\beta f$도 수렴하고 $\int_a^\beta f \leq \int_a^\beta g$이다. 따라서 $\int_a^\beta f$가 발산하면 $\int_a^\beta g$도 발산한다.
:::

::: 증명
$F(t) = \int_a^t f$, $G(t) = \int_a^t g$로 둔다. $f, g \geq 0$이므로 둘 다 증가하고, $G$의 극한은 $\sup G$이다. $\int_a^\beta g = S$라 하면 $F(t) \leq G(t) \leq S$이므로 $F$는 위로 유계이다. $F$의 상한을 $S'$이라 하자. $\varepsilon \gt 0$에 대하여 $F(t_0) \gt S' - \varepsilon$인 $t_0$가 있고, $F$가 증가하므로 $t \gt t_0$에서 $S' - \varepsilon \lt F(t) \leq S'$이다. 따라서 $F(t) \rightarrow S' \leq S$이다.
:::

가령 $x \geq 1$에서 $e^{-x^2} \leq e^{-x}$이고 $\int_1^\infty e^{-x}\dd{x} = e^{-1}$이므로 [정리 5](#thm5){: data-lid="eosoe" }에 의하여 $\int_0^\infty e^{-x^2}\dd{x}$는 수렴한다. 구간 $[0,1]$ 위의 부분은 연속함수의 보통 적분이다. 부등식은 구간의 끝 쪽에서만 성립하면 충분하다. $[a,c]$ 위의 적분은 유한한 수이므로 수렴 여부에 영향을 주지 않기 때문이다.

부등식을 직접 확인하기 번거로우면 비의 극한을 쓴다.

::: 정리 6 (limit comparison test)
$f, g : [a,\beta) \rightarrow [0,\infty)$가 각 $[a,t]$에서 Riemann integrable이고 $g \gt 0$이며 $L = \lim_{x \rightarrow \beta^-} f(x)/g(x)$가 존재한다고 하자. $0 \lt L \lt \infty$이면 $\int_a^\beta f$와 $\int_a^\beta g$는 수렴 여부가 같다. $L = 0$이고 $\int_a^\beta g$가 수렴하면 $\int_a^\beta f$도 수렴한다.
:::

::: 증명
$0 \lt L \lt \infty$이면 $\varepsilon = L/2$로 잡는다. $\beta$에 충분히 가까운 $x \in [c,\beta)$에서 $\lvert f/g - L\rvert \lt L/2$, 즉 $(L/2) g \leq f \leq (3L/2) g$이다. $\varepsilon$을 $L$보다 작은 값으로 잡아야 하한 $L - \varepsilon$이 양수가 되어 두 방향의 비교가 모두 가능하고, $L/2$는 그중 가장 단순한 선택이다. $\int_c^\beta g$가 수렴하면 오른쪽 부등식과 [정리 5](#thm5){: data-lid="v1jd2" }로 $\int_c^\beta f$가 수렴하고, $\int_c^\beta f$가 수렴하면 왼쪽 부등식으로 $\int_c^\beta g$가 수렴한다. $[a,c]$ 위의 부분은 수렴 여부에 영향이 없으므로 결론을 얻는다.

$L = 0$이면 $\varepsilon = 1$로 잡아 $c$ 이후에서 $f \leq g$이고, [정리 5](#thm5){: data-lid="f5ipq" }를 적용한다.
:::

가령 $\int_0^1 (\sin x) x^{-3/2}\dd{x}$는 $g = x^{-1/2}$와 $f/g = \sin x/x \rightarrow 1$로 비교되어, [명제 2](#prop2){: data-lid="mowht" }의 $p = 1/2 \lt 1$에 의해 수렴한다. 또 $\int_1^\infty (x^3 + x)^{-1/2}\dd{x}$는 $g = x^{-3/2}$와의 비가 $(1 + x^{-2})^{-1/2} \rightarrow 1$이므로 $p = 3/2 \gt 1$에 의해 수렴한다.

비교판정과 limit comparison test는 $f, g \geq 0$ 가정 아래에서만 말할 수 있다. 부호가 바뀌는 함수에서는 $F$의 단조성이 사라져 상계만으로 수렴을 얻을 수 없고, 다음 절의 예처럼 절대수렴하지 않는 수렴이 나타난다.

## 조건수렴의 예

::: 명제 7 (Dirichlet 적분)
$\int_0^\infty (\sin x/x)\dd{x}$는 수렴하지만 절대수렴하지 않는다.
:::

::: 증명
$[0,1]$ 위의 부분은 앞에서 본 대로 연속함수의 보통 적분이므로, $\int_1^\infty (\sin x/x)\dd{x}$만 보면 된다. $b \gt 1$에 대하여 [§미적분의 기본정리, ⁋명제 7](/ko/math/analysis/fundamental_theorem_of_calculus#prop7){: data-lid="1m52a" }로 부분적분을 하면

$$\int_1^b \frac{\sin x}{x}\dd{x} = \cos 1 - \frac{\cos b}{b} - \int_1^b \frac{\cos x}{x^2}\dd{x}$$

이다. $\lvert\cos b/b\rvert \leq 1/b \rightarrow 0$이다. 또 $\lvert\cos x/x^2\rvert \leq x^{-2}$이고 $\int_1^\infty x^{-2}\dd{x}$가 수렴하므로, [정리 5](#thm5){: data-lid="5qb3h" }와 [정리 4](#thm4){: data-lid="a08gz" }에 의해 $\int_1^\infty (\cos x/x^2)\dd{x}$가 수렴한다. 따라서 우변이 $b \rightarrow \infty$에서 수렴하고 이상적분이 수렴한다. 부분적분은 $\sin x$를 적분하는 쪽(원시함수 $-\cos x$)과 $1/x$를 미분하는 쪽에 나누어야 한다. 그래야 새 피적분함수가 $x^{-2}$로 감쇠하여 절대수렴한다.

절대수렴하지 않음을 보이자. $\lvert\sin x\rvert/x$는 음이 아니므로 $\int_0^b \lvert\sin x\rvert/x\dd{x}$는 $b$에 대해 증가하고, 수열 $b = n\pi$에서 유계가 아님을 보이면 충분하다. $[(k-1)\pi, k\pi]$ 위에서 $1/x \geq 1/(k\pi)$이고 $\int_{(k-1)\pi}^{k\pi}\lvert\sin x\rvert\dd{x} = 2$이므로

$$\int_0^{n\pi} \frac{\lvert\sin x\rvert}{x}\dd{x} \geq \sum_{k=1}^n \frac{1}{k\pi}\int_{(k-1)\pi}^{k\pi}\lvert\sin x\rvert\dd{x} = \frac{2}{\pi}\sum_{k=1}^n \frac{1}{k}$$

이고, [§무한급수와 수렴판정법, ⁋예시 4](/ko/math/analysis/series#ex4){: data-lid="vrf1o" }에 의하여 조화급수가 발산하므로 우변은 $n \rightarrow \infty$에서 무한대로 간다.
:::

적분값 자체는 $\pi/2$이지만 이 글의 도구로는 구해지지 않는다. 한편 $\int_0^\infty \lvert\sin x\rvert/x\dd{x}$의 발산 때문에 조건수렴이라는 말이 의미를 갖는다. 급수에서 조건수렴하는 급수의 항을 재배열하면 합이 바뀌는 현상이 있었듯이([§급수의 재배열과 곱, ⁋정리 7](/ko/math/analysis/rearrangements_and_products#thm7){: data-lid="uifbu" }), 이상적분에서도 조건수렴하는 적분은 다루기 까다롭다.

## 적분판정법

급수와 이상적분은 피적분함수가 단조일 때 서로를 판정해 준다.

::: 정리 8 (적분판정법)
$f : [1,\infty) \rightarrow [0,\infty)$가 감소함수이면 $\sum_{n=1}^\infty f(n)$이 수렴하는 것과 $\int_1^\infty f$가 수렴하는 것이 동치이다.
:::

::: 증명
[§Riemann 적분, ⁋정리 7](/ko/math/analysis/riemann_integral#thm7){: data-lid="tlwi7" }에 의하여 단조함수는 컴팩트구간에서 Riemann integrable이므로 $\int_1^b f$가 정의된다. $n \leq x \leq n+1$에서 $f(n+1) \leq f(x) \leq f(n)$이므로 [§Riemann 적분, ⁋명제 12](/ko/math/analysis/riemann_integral#prop12){: data-lid="52udz" }의 단조성에 의하여 적분하면 $f(n+1) \leq \int_n^{n+1} f \leq f(n)$이다. $n = 1, \ldots, N-1$에 대해 더하면

$$\sum_{n=2}^N f(n) \leq \int_1^N f \leq \sum_{n=1}^{N-1} f(n)$$

이다. 급수가 합 $S$로 수렴하면 오른쪽 부등식에서 모든 $N$에 대해 $\int_1^N f \leq S$이다. $b \leq N$이면 $f \geq 0$에 의해 $\int_1^b f \leq \int_1^N f \leq S$이므로 $F(b) = \int_1^b f$는 증가하고 위로 유계이며, 단조수렴에 의해 수렴한다. 역으로 $\int_1^\infty f = I$이면 왼쪽 부등식에서 $\sum_{n=2}^N f(n) \leq I$이므로 항이 음이 아닌 급수의 부분합이 위로 유계가 되어 급수가 수렴한다.
:::

이 정리를 $f(x) = x^{-p}$에 적용하면 [§무한급수와 수렴판정법, ⁋명제 9](/ko/math/analysis/series#prop9){: data-lid="p19mz" }에서 다룬 $p$-급수의 판정이 [명제 2](#prop2){: data-lid="2x9kz" }에서 곧바로 나온다.

::: 따름정리 9
$\sum_{n=1}^\infty n^{-p}$는 $p \gt 1$일 때 수렴하고 $p \leq 1$일 때 발산한다.
:::

::: 증명
$p \gt 0$이면 $x^{-p}$는 감소하는 양의 함수이므로 [정리 8](#thm8){: data-lid="veidf" }과 [명제 2](#prop2){: data-lid="dsq8f" }가 곧바로 적용된다. $p \leq 0$이면 항 $n^{-p}$가 $0$으로 가지 않으므로 발산한다.
:::

[정리 8](#thm8){: data-lid="jjy1o" }의 두 가정은 모두 필요하다. $f(x) = \sin^2(\pi x)$는 음이 아니지만 감소하지 않고, $f(n) = 0$이므로 $\sum f(n)$은 수렴하는데 각 $[n, n+1]$에서 $\int_n^{n+1} f = 1/2$이므로 $\int_1^\infty f$는 발산한다.

## 수렴하는 이상적분과 피적분함수의 거동

급수 $\sum a_n$이 수렴하면 [§무한급수와 수렴판정법, ⁋명제 2](/ko/math/analysis/series#prop2){: data-lid="zjvon" }에 의하여 $a_n \rightarrow 0$이다. 이상적분에서는 대응하는 명제 "$\int_a^\infty f$가 수렴하면 $f(x) \rightarrow 0$"이 성립하지 않는다.

::: 예시 10
$n \geq 2$에 대하여 $g_n$을 $[n - n^{-2}, n + n^{-2}]$ 위에서 $x = n$일 때 값 $1$인 삼각형 모양(꼭짓점이 $(n,1)$이고 양 끝에서 $0$인 연속함수)이고 그 밖에서는 $0$인 함수라 하고, $f = \sum_{n \geq 2} g_n$으로 둔다. $n \geq 2$이면 $n^{-2} \leq 1/4$이므로 이 구간들은 서로소이고 $f$는 연속이다. $g_n$ 아래의 넓이는 밑변 $2n^{-2}$, 높이 $1$인 삼각형이므로 $n^{-2}$이다. 따라서 $\int_0^b f$는 $b$에 대해 증가하고 $\sum_{n \geq 2} n^{-2}$로 위로 유계이므로 단조수렴에 의해 수렴한다. 그러나 모든 $n$에서 $f(n) = 1$이므로 $f(x) \rightarrow 0$이 아니다. 높이를 $n$, 밑변을 $2n^{-3}$으로 바꾸면 넓이는 여전히 $n^{-2}$이고 $f$는 유계도 아니다.
:::

$f$가 가운데에서 계속 큰 값을 가질 수 있는 이유는 큰 값을 갖는 구간의 길이가 충분히 빨리 줄기 때문이다. 이 예는 $f \geq 0$이어도 성립하므로 부호의 진동 때문이 아니다. 부호의 진동으로 인한 다른 형태도 있다. $\int_0^\infty \sin(x^2)\dd{x}$에서 $[0,1]$ 위의 부분은 보통의 적분이고, [§미적분의 기본정리, ⁋명제 8](/ko/math/analysis/fundamental_theorem_of_calculus#prop8){: data-lid="upb3n" }로 $t = x^2$으로 치환하면 $\int_1^b \sin(x^2)\dd{x} = \int_1^{b^2} \sin t/(2\sqrt{t})\dd{t}$이다. [§미적분의 기본정리, ⁋명제 7](/ko/math/analysis/fundamental_theorem_of_calculus#prop7){: data-lid="cerfs" }로 부분적분하면 $\cos 1/2 - \cos(b^2)/(2b) - \int_1^{b^2}\cos t/(4t^{3/2})\dd{t}$이고, 마지막 적분은 [명제 2](#prop2){: data-lid="w5b59" }와 [정리 5](#thm5){: data-lid="f5dir" }에 의하여 $t^{-3/2}$로 절대수렴하므로 [정리 4](#thm4){: data-lid="038ae" }에 의하여 이상적분이 수렴한다. 그런데 $\sin(x^2)$은 $x \rightarrow \infty$에서 $-1$과 $1$ 사이를 점점 빠르게 오가며 극한을 갖지 않는다.

## 주값

$\int_{-\infty}^\infty$는 [정의 1](#def1){: data-lid="no1z6" }에 의해 $0$ 같은 한 점에서 쪼개어 양쪽이 각각 수렴해야 한다. 이 요구를 약하게 바꾼 것이 주값이다.

::: 정의 11 (주값)
$f : \mathbb{R} \rightarrow \mathbb{R}$가 모든 컴팩트구간에서 Riemann integrable일 때, 극한

$$\operatorname{p.v.}\int_{-\infty}^\infty f(x)\dd{x} = \lim_{R \rightarrow \infty}\int_{-R}^R f(x)\dd{x}$$

가 존재하면 이를 *주값<sub>Cauchy principal value</sub>*이라 한다. $a \lt c \lt b$이고 $f$가 $c$ 근방에서 유계가 아닐 때에는 $\operatorname{p.v.}\int_a^b f = \lim_{\delta \rightarrow 0^+}\bigl(\int_a^{c-\delta} f + \int_{c+\delta}^b f\bigr)$로 정의한다.
:::

주값은 양쪽을 같은 속도로 늘리거나 좁힌다는 점에서 이상적분보다 약하다.

::: 명제 12
$\int_{-\infty}^\infty f$가 수렴하면 주값이 존재하고 이상적분과 같다.
:::

::: 증명
[§Riemann 적분, ⁋명제 16](/ko/math/analysis/riemann_integral#prop16){: data-lid="v646l" }에 의하여 $\int_{-R}^R f = \int_{-R}^0 f + \int_0^R f$이고, 이상적분이 수렴한다는 것은 $\int_0^\infty f$와 $\int_{-\infty}^0 f$가 각각 수렴한다는 뜻이므로 $R \rightarrow \infty$에서 두 항이 각각 수렴하여 그 합이 이상적분값이 된다.
:::

역은 성립하지 않는다. $f(x) = x$는 $\int_{-R}^R x\dd{x} = 0$이므로 $\operatorname{p.v.}\int_{-\infty}^\infty x\dd{x} = 0$이지만, $\int_0^R x\dd{x} = R^2/2 \rightarrow \infty$이므로 $\int_{-\infty}^\infty x\dd{x}$는 발산한다. 주값은 대칭인 구간을 택한 데에 의존한다. 같은 함수에 대해 $\int_{-R}^{2R} x\dd{x} = 3R^2/2 \rightarrow \infty$이므로 비대칭으로 늘리면 값이 달라진다. singular point가 있는 경우도 마찬가지로 $\operatorname{p.v.}\int_{-1}^1 x^{-1}\dd{x} = 0$이지만, 이상적분 $\int_0^1 x^{-1}\dd{x}$가 [명제 2](#prop2){: data-lid="ieeae" }에 의해 발산하므로 $\int_{-1}^1 x^{-1}\dd{x}$는 발산한다.

---

**참고문헌**

**[Rud]** W. Rudin, *Principles of mathematical analysis*, 3rd ed., McGraw-Hill, 1976.
