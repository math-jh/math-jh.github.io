---
title: "Improper Integrals"
description: "Improper integrals with infinite intervals of integration or divergent integrands are defined as limits, and their convergence is determined using p-integrals, the comparison test, limit comparison, and absolute convergence. The gamma function is defined using convergent improper integrals."
excerpt: "Improper integrals over infinite intervals, singular integrals, comparison test, absolute convergence"

categories: [Math / Calculus]
permalink: /en/math/calculus/improper_integrals
sidebar: 
    nav: "calculus-en"

date: 2026-06-26
weight: 12
translated_at: 2026-08-19T08:45:05+00:00
translation_source: kimi-cli
last_polished_at: 2026-09-30T11:15:05+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
The integrals we have examined so far were defined for bounded functions on finite intervals. However, we often wish to discuss the area even when the interval extends to infinity or when the integrand becomes infinitely large at a point. In this post, we define this through the limits of integrals over finite intervals.

## Definition of Improper Integrals

First, we define the following.

::: Definition 1
When $f$ is integrable on $[a, t]$ for all $t > a$, we define the *improper integral* over an infinite interval as

$$\int_a^{\infty} f(x) \dd{x} = \lim_{t \rightarrow \infty}\int_a^t f(x) \dd{x}$$

and say that the improper integral *converges* if this limit exists as a finite value. Likewise, if $f$ is integrable on $[t,b]$ for all $t<b$, and the expression

$$\int_{-\infty}^b f(x)\dd{x}=\lim_{t \rightarrow -\infty}\int_t^b f(x) \dd{x}$$

exists as a finite value, we say that the improper integral converges. If for some $c$ the two improper integrals

$$\int_{-\infty}^c f(x) \dd{x},\qquad \int_c^{\infty} f(x) \dd{x}$$

each converge, we denote their sum

$$\int_{-\infty}^c f(x) \dd{x} + \int_c^{\infty} f(x) \dd{x}$$

simply by the expression

$$\int_{-\infty}^{\infty} f(x) \dd{x}$$
:::

In the definition above, the definition of the two improper integrals

$$\int_a^\infty f(x)\dd{x},\qquad \int_{-\infty}^b f(x)\dd{x}$$

is relatively clear. The part that may seem somewhat ambiguous is the improper integral where both ends are infinite. First, we can see that if this integral is defined, its value does not depend on the choice of the splitting point $c$. This is because even if we choose another $c'$,

$$\begin{aligned}\int_{-\infty}^c f(x)\dd{x}+\int_c^\infty f(x)\dd{x}&=\lim_{s\rightarrow-\infty}\int_s^c f(x)\dd{x}+\lim_{t\rightarrow \infty}\int_c^t f(x)\dd{x}\\&=\lim_{s\rightarrow-\infty}\left(\int_s^c f(x)\dd{x}+\int_c^{c'} f(x)\dd{x}\right)+\lim_{t\rightarrow \infty}\left(\int_c^t f(x)\dd{x}-\int_c^{c'} f(x)\dd{x}\right)\\&=\lim_{s\rightarrow-\infty}\int_s^{c'} f(x)\dd{x}+\lim_{t\rightarrow \infty}\int_{c'}^t f(x)\dd{x}\\&=\int_{-\infty}^{c'} f(x)\dd{x}+\int_{c'}^\infty f(x)\dd{x}\end{aligned}$$

and thus this value is the same. What requires more attention is that we take these two limits *independently*. For example, if we define the sign function by

$$\sgn(x)=\begin{cases}1&\text{if $x>0$}\\0&\text{if $x=0$}\\-1&\text{if $x<0$}\end{cases}$$

then for a fixed $t>0$, the value obtained by integrating this function from $-t$ to $t$ is $0$, and thus

$$\lim_{t\rightarrow\infty}\int_{-t}^t \sgn(x)\dd{x}=0$$

yet according to the definition above, the improper integral of $\sgn$ is not defined. For instance, had we set the interval of integration from $-t$ to $2t$ and then taken the limit $t\rightarrow\infty$, this limit would have diverged, so this is an essential restriction.

Similarly, we also define the integral of a function that diverges at a single point as a limit.

::: Definition 2
When $f$ is not bounded near $c$ but for all $a \leq t < c$ is integrable on $[a, t]$, we define the *improper integral* by

$$\int_a^c f(x) \dd{x} = \lim_{t \rightarrow c^-}\int_a^t f(x) \dd{x}$$

Similarly, if $f$ is not bounded near $c$ but for all $c < t \leq b$ is integrable on $[t, b]$, we define its improper integral by

$$\int_c^b f(x) \dd{x} = \lim_{t \rightarrow c^+}\int_t^b f(x) \dd{x}$$

If, in the interior of $[a,b]$, near a point $c$, $f$ is not bounded, we define this improper integral by

$$\int_a^b f(x)\dd{x}=\lim_{t\rightarrow c^-}\int_a^t f(x)\dd{x}+\lim_{s\rightarrow c^+} \int_s^b f(x)\dd{x}$$

:::

Again, when $c$ lies in the interior of the interval, the same subtlety as in [Definition 1](#def1){: data-lid="bof2y" } above still persists. For instance, in

$$\lim_{t\rightarrow 0^-}\int_{-1}^t \frac{\dd{x}}{x}+\lim_{s\rightarrow 0^+}\int_s^1\frac{\dd{x}}{x}$$

neither term is defined, but had we grouped them as

$$\lim_{t\rightarrow 0^+}\left(\int_{-1}^{-t} \frac{\dd{x}}{x}+\int_t^1\frac{\dd{x}}{x}\right)$$

the problem would have arisen that this value becomes $0$.

## Convergence Tests for Improper Integrals

Many improper integrals are difficult to compute directly because an antiderivative cannot be found explicitly. However, convergence alone can be determined by comparison with a more tractable function. When the integrand is nonnegative, the value of the integral is monotonically increasing with respect to the interval of integration, so a comparison test as in series holds.

::: Proposition 3 (Comparison test)
For $x \geq a$, let $0 \leq f(x) \leq g(x)$. If $\int_a^\infty g(x) \dd{x}$ converges, then $\int_a^\infty f(x) \dd{x}$ also converges; and if $\int_a^\infty f(x) \dd{x}$ diverges, then $\int_a^\infty g(x) \dd{x}$ also diverges.
:::

::: Proof
$F(t) = \int_a^t f(x) \dd{x}$, since $f \geq 0$, is increasing with respect to $t$, and by the monotonicity of [§Integration, ⁋Proposition 11](/en/math/calculus/integration#prop11){: data-lid="uz0b9" },

$$F(t) \leq \int_a^t g(x) \dd{x} \leq \int_a^\infty g(x) \dd{x}$$

so it is bounded above. An increasing function that is bounded above has a limit as $t \rightarrow \infty$, hence $\int_a^\infty f(x) \dd{x}$ converges. The second claim is the contrapositive.
:::

When the inequality $0 \leq f \leq g$ is difficult to establish directly, we use limit comparison just as for series. That is, if two positive functions satisfy $f(x)/g(x) \rightarrow c$ ($0 < c < \infty$), then the same argument as in [§Infinite Series, ⁋Proposition 7](/en/math/calculus/series#prop7){: data-lid="hpcql" } shows that the two integrals converge or diverge together; hence it suffices to know what function the integrand behaves like as $x \rightarrow \infty$ to complete the test.

For integrands that change sign, we take absolute values to reduce to positive terms.

::: Proposition 4 (Absolute convergence)
If $f$ is, for every $t > a$, integrable on $[a, t]$ and $\int_a^\infty \lvert f(x)\rvert \dd{x}$ converges, then $\int_a^\infty f(x) \dd{x}$ also converges.
:::

::: Proof
Since $0 \leq f + \lvert f\rvert \leq 2\lvert f\rvert$, [Proposition 3](#prop3){: data-lid="xdge1" } implies that $\int_a^\infty (f(x) + \lvert f(x)\rvert) \dd{x}$ converges, and therefore $\int_a^\infty f(x) \dd{x} = \int_a^\infty (f(x) + \lvert f(x)\rvert) \dd{x} - \int_a^\infty \lvert f(x)\rvert \dd{x}$ also converges.
:::

The converse does not hold. While $\int_0^\infty \frac{\sin x}{x} \dd{x}$ converges, $\int_0^\infty \lvert \sin x/x\rvert \dd{x}$ diverges, so this is *conditional convergence*, which corresponds to conditional convergence of series.

The two criteria above were stated for integrals over infinite intervals, but via substitution they apply directly to singular integrals that diverge at an endpoint as well. If $f$ is singular at the left endpoint $c$ in $\int_c^b f(x) \dd{x}$, setting $u = 1/(x - c)$ makes $x \rightarrow c^+$ correspond to $u \rightarrow \infty$, and matching the orientation of the interval of integration yields

$$\int_c^b f(x) \dd{x} = \int_{1/(b-c)}^\infty \frac{f(c + 1/u)}{u^2} \dd{u}$$

which is an integral over an infinite interval. The multiplied factor $u^{-2} > 0$ preserves inequalities and absolute values, so [Proposition 3](#prop3){: data-lid="2czby" } and [Proposition 4](#prop4){: data-lid="dvtce" } remain valid as convergence tests for singular integrals as well.

For these tests to be useful in practice, one needs standard functions to compare against, and this role is almost always filled by power functions or the exponential function $e^{-x}$. Among these, the integral of a power function provides an (almost) sharp boundary between convergence and divergence.

::: Example 5 (p-integrals)
Improper integrals of powers exhibit exactly opposite boundaries on infinite intervals and at singular points. The integral over an infinite interval $\int_1^{\infty} x^{-p} \dd{x}$ converges for $p > 1$ and diverges for $p \leq 1$, whereas $\int_0^1 x^{-p} \dd{x}$, which contains a singular point, conversely converges for $p < 1$ and diverges for $p \geq 1$. Both computations arise from the same antiderivative: for $p \neq 1$,

$$\int_1^t x^{-p} \dd{x} = \frac{t^{1-p} - 1}{1 - p}, \qquad \int_t^1 x^{-p} \dd{x} = \frac{1 - t^{1-p}}{1 - p}$$

and for the improper integral on the left, as $t \rightarrow \infty$ when $p > 1$, $t^{1-p}$ tends to $0$, while for the singular integral on the right, as $t \rightarrow 0^+$ when $p < 1$, $t^{1-p}$ converges to $0$, making the integral finite. In this case, the respective values of convergence are

$$\int_1^\infty x^{-p} \dd{x} = \frac{1}{p - 1} \quad (p > 1), \qquad \int_0^1 x^{-p} \dd{x} = \frac{1}{1 - p} \quad (p < 1)$$

. Intuitively, this can be understood as: on an infinite interval, a large $p$ decreases rapidly, aiding convergence, but near a singular point, a large $p$ increases more rapidly, causing divergence; this can be clearly seen visually in the following figure plotting $1/x$ and $1/x^2$.

{% diagram Math/Calculus/Improper_Integrals-1.svg width="12.69em" alt="Graphs of 1/x and 1/x²" %}
:::

However, this boundary $p = 1$ is somewhat subtle. Since substitution can be used directly for improper integrals as well, setting $u = \ln x$ yields

$$\int_2^\infty \frac{\dd{x}}{x(\ln x)^p} = \int_{\ln 2}^\infty u^{-p} \dd{u}$$

which converges when $p > 1$. That is, for $p = 1$, $1/x$ itself diverges, but attaching a logarithm raised to a power greater than one shifts the boundary back toward convergence. In other words, considering powers alone, $p = 1$ is the exact boundary, but inserting a logarithmic factor produces a finer distinction; this is why we said earlier that this boundary is *almost* sharp.

Meanwhile, convergent improper integrals are used to define new functions.

::: Example 6 (Gamma function)
The following function, defined as an improper integral,

$$\Gamma(s) = \int_0^\infty x^{s-1}e^{-x} \dd{x}$$

converges for $s > 0$. This is because near $0$, the singular integral of $x^{s-1}$ converges for $s > 0$ ([Example 5](#ex5){: data-lid="oxlfh" }), and near $\infty$, $e^{-x}$ dominates any power. By integration by parts,

$$\Gamma(s+1) = \bigl[-x^s e^{-x}\bigr]_0^\infty + s\int_0^\infty x^{s-1}e^{-x} \dd{x} = s \Gamma(s)$$

and since $\Gamma(1) = \int_0^\infty e^{-x} \dd{x} = 1$, we have $\Gamma(n) = (n-1)!$. That is, the gamma function extends the factorial to real numbers.
:::

---

**References**

**[Ste]** J. Stewart, *Calculus*, 8th ed., Cengage Learning, 2016.  
**[Kim]** 김홍종, *미적분학 1·2*, 제3개정판, 서울대학교출판문화원, 2020.
