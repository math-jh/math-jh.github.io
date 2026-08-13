---
title: "멱급수와 해석함수"
description: "멱급수의 수렴반경을 코시–아다마르 공식으로 정하고, 수렴반경 안의 컴팩트집합에서 균등수렴함을 보인다. 그로부터 항별 미분이 정당화되어 멱급수의 합이 해석함수임을 증명한다."
excerpt: "코시–아다마르 수렴반경, 균등수렴, 항별 미분과 해석함수"

categories: [Math / Analysis]
permalink: /ko/math/analysis/power_series
sidebar: 
    nav: "analysis-ko"

date: 2026-06-02
weight: 18

drift_needed: true

published: false
---

[\[미적분학\] §멱급수](/ko/math/calculus/power_series)에서 멱급수의 항별 미분·적분을 받아들였다. 이제 [§균등수렴](/ko/math/analysis/uniform_convergence)을 갖추었으므로 그 근거를 엄밀하게 세운다. 핵심은 멱급수가 수렴반경 안에서 균등수렴한다는 것이다.

## 수렴반경

::: 정리 1 (코시–아다마르)
멱급수 $\sum_{n=0}^\infty c_n (x - a)^n$에 대하여

$$R = \frac{1}{\limsup_{n\rightarrow\infty} \lvert c_n\rvert^{1/n}}$$

으로 두면 ($0$과 $\infty$는 통상적으로 해석한다), $\lvert x - a\rvert < R$이면 절대수렴하고 $\lvert x - a\rvert > R$이면 발산한다.
:::

::: 증명
근판정의 양 $\limsup \lvert c_n (x-a)^n\rvert^{1/n} = \lvert x - a\rvert \limsup\lvert c_n\rvert^{1/n} = \lvert x - a\rvert/R$를 본다. [§무한급수, ⁋정리 10](/ko/math/analysis/series#thm10)은 극한이 존재하는 경우를 다루므로, $\limsup$만 있는 일반의 경우를 직접 본다. 이 값이 $1$보다 작으면, 곧 $\lvert x - a\rvert < R$이면 그 값과 $1$ 사이의 $\theta$를 잡아 충분히 큰 $n$에서 $\lvert c_n (x-a)^n\rvert \leq \theta^n$이므로 [§무한급수, ⁋정리 4](/ko/math/analysis/series#thm4)에 의해 절대수렴하고, $1$보다 크면 무한히 많은 $n$에서 $\lvert c_n (x-a)^n\rvert \geq 1$이어서 일반항이 $0$으로 가지 않으므로 [§무한급수, ⁋명제 3](/ko/math/analysis/series#prop3)에 의해 발산한다.
:::

## 균등수렴과 항별 미분

수렴반경 안에서는 (끝까지는 아니어도) 컴팩트하게 균등수렴한다.

::: 정리 2
$0 < r < R$이면 멱급수는 $\lvert x - a\rvert \leq r$에서 균등수렴한다.
:::

::: 증명
$\lvert x - a\rvert \leq r$이면 $\lvert c_n(x-a)^n\rvert \leq \lvert c_n\rvert r^n =: M_n$이고, $r < R$이므로 $\sum M_n$이 수렴한다 ([정리 1](#thm1)). [§균등수렴, ⁋정리 4](/ko/math/analysis/uniform_convergence#thm4)에 의해 균등수렴한다.
:::

균등수렴과 연속성 보존으로부터 멱급수의 합은 수렴반경 안에서 연속이고, 항별 미분이 정당화된다.

::: 정리 3
$f(x) = \sum_{n=0}^\infty c_n (x-a)^n$이 수렴반경 $R > 0$을 가지면, $f$는 $\lvert x - a\rvert < R$에서 무한히 미분가능하고

$$f'(x) = \sum_{n=1}^\infty n c_n (x - a)^{n-1}$$

이며, 이 도함수 급수도 수렴반경 $R$을 가진다. 따라서 $c_n = f^{(n)}(a)/n!$이다.
:::

::: 증명
$\lim n^{1/n} = 1$이므로 항별 미분한 급수의 수렴반경도 $1/\limsup\lvert n c_n\rvert^{1/n} = R$로 같다. $\lvert x - a\rvert \leq r$에서 원래 급수의 부분합열이 수렴하고 그 도함수열, 곧 도함수 급수의 부분합열이 균등수렴하므로 ([정리 2](#thm2)), 도함수열이 균등수렴하고 함수열이 한 점에서 수렴하면 극한함수가 미분가능하며 그 도함수가 도함수열의 극한이 된다는 정리를 가져다 쓰면 ([Rud] §7), $f'$가 항별 미분으로 주어진다. 이를 반복하면 $f$가 무한히 미분가능하고, $x = a$를 대입하면 $f^{(n)}(a) = n! c_n$이다.
:::

## 해석함수

::: 정의 4
함수 $f$가 점 $a$ 근방에서 그곳을 중심으로 하는 멱급수와 일치하면 $f$가 $a$에서 *해석적<sub>analytic</sub>*이라 한다.
:::

[정리 3](#thm3)에 의해 해석함수는 무한히 미분가능하고 자신의 테일러 급수와 같다. 그러나 그 역은 거짓이다: $f(x) = e^{-1/x^2}$ ($f(0) = 0$) 은 무한히 미분가능하지만 $0$에서 모든 도함수가 $0$이어서 테일러 급수가 항등적으로 $0$이고, 따라서 $0$에서 해석적이지 않다. 즉 [\[미적분학\] §테일러 정리](/ko/math/calculus/taylor_theorem)의 테일러 급수가 함수로 수렴하는지는 나머지항의 거동에 달려 있으며, 매끄러움만으로는 보장되지 않는다.

[정리 3](#thm3)의 마지막 등식 $c_n = f^{(n)}(a)/n!$은 해석함수가 자신을 정의하는 멱급수에 의해 계수까지 완전히 결정됨을 말한다. 이로부터 곧바로 다음의 유일성이 따른다: 한 함수가 같은 중심에서 두 멱급수로 표현되면 두 급수의 모든 계수가 일치한다.

::: 명제 5 (계수의 유일성)
$\lvert x - a\rvert < R$에서 $\sum_{n=0}^\infty c_n (x-a)^n = \sum_{n=0}^\infty d_n (x-a)^n$이면 모든 $n$에 대해 $c_n = d_n$이다.
:::

::: 증명
두 멱급수의 공통의 합을 $f$라 두면, [정리 3](#thm3)에 의해 $f$는 $\lvert x - a\rvert < R$에서 무한히 미분가능하고 양쪽 표현으로부터 계수가 동시에 도함수로 읽힌다. 곧

$$\begin{aligned}
c_n &= \frac{f^{(n)}(a)}{n!}, \\
d_n &= \frac{f^{(n)}(a)}{n!}
\end{aligned}$$

이므로 모든 $n$에 대해 $c_n = d_n$이다. 도함수 $f^{(n)}(a)$는 함수 $f$만으로 결정되는 값이므로, 표현이 두 개 있더라도 계수는 하나로 강제된다.
:::

[명제 5](#prop5)는 멱급수 전개가 유일함을 보장하므로, 어떤 방법으로든 함수를 멱급수로 적어내기만 하면 그것이 곧 테일러 급수임을 안다. 가령 점화식이나 미정계수법으로 얻은 급수도, [정리 3](#thm3)을 통해 자동으로 해당 함수의 테일러 전개가 된다.

## 수렴반경의 계산

[정리 1](#thm1)은 모든 멱급수에 통하지만, 실제 계산에서는 [§무한급수, ⁋정리 7](/ko/math/analysis/series#thm7)이 더 다루기 쉬운 경우가 많다. 계수의 비 $\lvert c_{n+1}/c_n\rvert$이 극한을 가지면 그 극한의 역수가 곧 수렴반경이 된다.

::: 명제 6 (비판정에 의한 수렴반경)
$c_n \neq 0$이 충분히 큰 $n$에서 성립하고 $\lim_{n\rightarrow\infty}\lvert c_{n+1}/c_n\rvert = L$이 존재하면, 멱급수 $\sum c_n (x-a)^n$의 수렴반경은 $R = 1/L$이다 ($L = 0$이면 $R = \infty$, $L = \infty$이면 $R = 0$).
:::

::: 증명
고정된 $x \neq a$에서 항 $c_n (x-a)^n$에 비판정을 적용하면

$$\begin{aligned}
\lim_{n\rightarrow\infty}\left\lvert\frac{c_{n+1}(x-a)^{n+1}}{c_n (x-a)^n}\right\rvert
&= \lvert x - a\rvert \cdot \lim_{n\rightarrow\infty}\left\lvert\frac{c_{n+1}}{c_n}\right\rvert \\
&= L \lvert x - a\rvert
\end{aligned}$$

이다. 이 값이 $1$보다 작으면, 곧 $\lvert x - a\rvert < 1/L$이면 절대수렴하고, $1$보다 크면 발산한다. 따라서 수렴반경은 $R = 1/L$이다. 비판정으로 극한이 존재할 때 근판정의 $\limsup$도 같은 값을 가지므로, 이는 [정리 1](#thm1)과 모순되지 않는다.
:::

가령 $c_n = n^2/2^n$이면 $\lvert c_{n+1}/c_n\rvert = (1/2)(n+1)^2/n^2 \rightarrow 1/2$이므로 [명제 6](#prop6)에서 곧바로 $R = 2$를 얻는다. 그러나 계수가 진동하여 비의 극한이 아예 존재하지 않는 급수에서는 [명제 6](#prop6)이 무력하고, Cauchy–Hadamard 공식의 $\limsup$만이 답을 준다.

::: 예시 7 (비판정이 통하지 않는 경우)
계수가 짝·홀에 따라 달라 비의 극한이 없을 때는 근판정을 쓴다. 멱급수

$$\sum_{n=0}^\infty c_n x^n, \qquad c_n = \begin{cases} 2^n & (n\ \text{짝수}) \\ 3^n & (n\ \text{홀수}) \end{cases}$$

에서는 $\lvert c_{n+1}/c_n\rvert$이 $2^{n+1}/3^n$과 $3^{n+1}/2^n$ 사이를 오가 극한이 없다. 그러나 근판정의 양은

$$\begin{aligned}
\lvert c_n\rvert^{1/n} &= \begin{cases} 2 & (n\ \text{짝수}) \\ 3 & (n\ \text{홀수}) \end{cases} \\
\limsup_{n\rightarrow\infty}\lvert c_n\rvert^{1/n} &= 3
\end{aligned}$$

이므로 [정리 1](#thm1)에 의해 $R = 1/3$이다. 이처럼 $\limsup$은 진동하는 계수에도 항상 정의된다.
:::

## 응용: 항별 미분의 계산

[정리 3](#thm3)의 항별 미분은 알려진 멱급수에서 새 항등식을 끌어내는 도구이다. 수렴반경 안에서 멱급수는 다항식처럼 다룰 수 있으므로, 미분·적분과 대입을 자유롭게 조합해 함수의 값이나 수치급수의 합을 얻는다.

::: 예시 8 (등비급수의 미분)
기하급수 $1/(1-x) = \sum_{n=0}^\infty x^n$ ($\lvert x\rvert < 1$) 을 [정리 3](#thm3)으로 항별 미분하면

$$\begin{aligned}
\frac{d}{\dd{x}}\frac{1}{1-x} &= \frac{1}{(1-x)^2}, \\
\frac{d}{\dd{x}}\sum_{n=0}^\infty x^n &= \sum_{n=1}^\infty n x^{n-1}
\end{aligned}$$

이므로 $1/(1-x)^2 = \sum_{n=1}^\infty n x^{n-1}$이고, 양변에 $x$를 곱하면

$$\sum_{n=1}^\infty n x^n = \frac{x}{(1-x)^2} \qquad (\lvert x\rvert < 1)$$

을 얻는다. $x = 1/2$을 대입하면 $\sum_{n=1}^\infty n/2^n = 2$라는 수치급수의 합이 따라 나온다.
:::

같은 도구로 $e^x = \sum_{n\geq 0} x^n/n!$ ($R = \infty$) 을 항별 미분하면 첨자를 한 칸 밀어 $(e^x)' = e^x$가 급수 차원에서 회복되고, $\sin, \cos$도 마찬가지여서 기본 도함수 공식이 모두 항별 미분으로 따라 나온다.

해석함수는 실해석학과 complex analysis를 잇는 다리이며, 멱급수를 복소수 변수로 확장하면 한층 강력한 이론이 펼쳐진다. 다음으로는 미분을 여러 변수로 확장하는 [§다변수 미분](/ko/math/analysis/multivariable_differentiation)으로 나아간다.

---

**참고문헌**

**[Rud]** W. Rudin, *Principles of mathematical analysis*, 3rd ed., McGraw-Hill, 1976.
