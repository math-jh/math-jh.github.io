---
title: "Improper Integrals"
description: "Improper integrals over infinite intervals or with unbounded integrands are defined as limits. We use p-integrals, comparison tests, limit comparison, and absolute convergence to determine whether they converge. The convergent improper integrals are used to define the gamma function."
excerpt: "Infinite and singular integrals, comparison test, absolute convergence"

categories: [Math / Calculus]
permalink: /en/math/calculus/improper_integrals
sidebar: 
    nav: "calculus-en"

date: 2026-06-26
weight: 12
translated_at: 2026-08-17T21:15:04+00:00
translation_source: kimi-cli
---
The integrals we have examined so far were defined for bounded functions on finite intervals. However, we often wish to discuss area even when the interval extends infinitely, or when the integrand becomes arbitrarily large at a point. In this post, we define these through limits of integrals over finite intervals.

## Definition of Improper Integrals

We first make the following definition.

::: Definition 1
If $f$ is integrable on $[a,t]$ for every $t > a$, we define the improper integral over the infinite interval as

$$\int_a^{\infty} f(x) \dd{x} = \lim_{t \rightarrow \infty}\int_a^t f(x) \dd{x}$$

and say that the improper integral *converges* if this limit exists as a finite value. Likewise, if $f$ is integrable on $[t,b]$ for every $t < b$, and the expression

$$\int_{-\infty}^b f(x)\dd{x}=\lim_{t \rightarrow -\infty}\int_t^b f(x) \dd{x}$$

exists as a finite value, we say that the improper integral converges. If for some $c$ both improper integrals

$$\int_{-\infty}^c f(x) \dd{x},\qquad \int_c^{\infty} f(x) \dd{x}$$

converge, we abbreviate their sum

$$\int_{-\infty}^c f(x) \dd{x} + \int_c^{\infty} f(x) \dd{x}$$

by the expression

$$\int_{-\infty}^{\infty} f(x) \dd{x}.$$
:::

In the definition above, the definitions of the two improper integrals

$$\int_a^\infty f(x)\dd{x},\qquad \int_{-\infty}^b f(x)\dd{x}$$

are relatively clear. The somewhat ambiguous part is the improper integral with infinities on both sides; first, we can see that if this integral is defined, its value does not depend on the choice of the splitting point $c$. This is because if we choose a different $c'$,

$$\begin{aligned}\int_{-\infty}^c f(x)\dd{x}+\int_c^\infty f(x)\dd{x}&=\lim_{s\rightarrow-\infty}\int_s^c f(x)\dd{x}+\lim_{t\rightarrow \infty}\int_c^t f(x)\dd{x}\\&=\lim_{s\rightarrow-\infty}\left(\int_s^c f(x)\dd{x}+\int_c^{c'} f(x)\dd{x}\right)+\lim_{t\rightarrow \infty}\left(\int_c^t f(x)\dd{x}-\int_c^{c'} f(x)\dd{x}\right)\\&=\lim_{s\rightarrow-\infty}\int_s^{c'} f(x)\dd{x}+\lim_{t\rightarrow \infty}\int_{c'}^t f(x)\dd{x}\\&=\int_{-\infty}^{c'} f(x)\dd{x}+\int_{c'}^\infty f(x)\dd{x}\end{aligned}$$

so the value is the same. A more noteworthy point is that we send these two limits *independently*. For example, defining the sign function by

$$\sgn(x)=\begin{cases}1&\text{if $x>0$}\\0&\text{if $x=0$}\\-1&\text{if $x<0$}\end{cases}$$

the integral of this function from $-t$ to $t$ is $0$ for any fixed $t>0$, and thus

$$\lim_{t\rightarrow\infty}\int_{-t}^t \sgn(x)\dd{x}=0;$$

however, according to the definition above, the improper integral of $\sgn$ is not defined. For instance, if we had taken the interval from $-t$ to $2t$ and then let $t\rightarrow\infty$, this limit would have diverged, so this restriction is essential.

Similarly, we also define the integral of a function that diverges at a single point as a limit.

::: Definition 2
If $f$ is not bounded near $c$ but is integrable on $[a, t]$ for every $a \leq t < c$, we define the *improper integral* by

$$\int_a^c f(x) \dd{x} = \lim_{t \rightarrow c^-}\int_a^t f(x) \dd{x}$$

Similarly, if $f$ is not bounded near $c$ but is integrable on $[t, b]$ for every $c < t \leq b$, we define the improper integral by

$$\int_c^b f(x) \dd{x} = \lim_{t \rightarrow c^+}\int_t^b f(x) \dd{x}$$

If $f$ is not bounded near a point $c$ in the interior of $[a,b]$, we define this improper integral by

$$\int_a^b f(x)\dd{x}=\lim_{t\rightarrow c^-}\int_a^t f(x)\dd{x}+\lim_{s\rightarrow c^+} \int_s^b f(x)\dd{x}$$

:::

Again, when $c$ lies in the interior of the interval, the same subtlety as in [Definition 1](#def1) still exists. For instance,

$$\lim_{t\rightarrow 0^-}\int_{-1}^t \frac{\dd{x}}{x}+\lim_{s\rightarrow 0^+}\int_s^1\frac{\dd{x}}{x}$$

is not defined term by term, but if we had grouped them as

$$\lim_{t\rightarrow 0^+}\left(\int_{-1}^{-t} \frac{\dd{x}}{x}+\int_t^1\frac{\dd{x}}{x}\right)$$

the value would have turned out to be $0$.

## Convergence Tests for Improper Integrals

Many improper integrals cannot be evaluated explicitly because we cannot find an antiderivative in closed form. However, to determine convergence alone, we can compare with a more tractable function. When the integrand is non-negative, the integral is monotone increasing with respect to the domain of integration, so the comparison test, just as for series, applies.

::: Proposition 3 (Comparison test)
Suppose $0 \leq f(x) \leq g(x)$ for $x \geq a$. If $\int_a^\infty g(x) \dd{x}$ converges, then $\int_a^\infty f(x) \dd{x}$ also converges; and if $\int_a^\infty f(x) \dd{x}$ diverges, then $\int_a^\infty g(x) \dd{x}$ also diverges.
:::

::: Proof
Since $f \geq 0$, the function $F(t) = \int_a^t f(x) \dd{x}$ is increasing in $t$, and by monotonicity from [§Integration, ⁋Proposition 11](/en/math/calculus/integration#prop11),

$$F(t) \leq \int_a^t g(x) \dd{x} \leq \int_a^\infty g(x) \dd{x}$$

so it is bounded above. An increasing function that is bounded above has a limit as $t \rightarrow \infty$, so $\int_a^\infty f(x) \dd{x}$ converges. The second claim is the contrapositive.
:::

When it is difficult to establish the inequality $0 \leq f \leq g$ directly, we use a limit comparison just as for series. That is, if two positive functions satisfy $f(x)/g(x) \rightarrow c$ ($0 < c < \infty$), then the same argument as in [§Infinite Series, ⁋Proposition 7](/en/math/calculus/series#prop7) shows that the two integrals converge or diverge together; hence it suffices to know which function the integrand behaves like as $x \rightarrow \infty$.

For integrands that change sign, we take absolute values to reduce to the positive case.

::: Proposition 4 (Absolute convergence)
If $f$ is integrable on $[a, t]$ for every $t > a$ and $\int_a^\infty \lvert f(x)\rvert \dd{x}$ converges, then $\int_a^\infty f(x) \dd{x}$ also converges.
:::

::: Proof
Since $0 \leq f + \lvert f\rvert \leq 2\lvert f\rvert$, [Proposition 3](#prop3) implies that $\int_a^\infty (f(x) + \lvert f(x)\rvert) \dd{x}$ converges, and hence $\int_a^\infty f(x) \dd{x} = \int_a^\infty (f(x) + \lvert f(x)\rvert) \dd{x} - \int_a^\infty \lvert f(x)\rvert \dd{x}$ also converges.
:::

The converse does not hold. $\int_0^\infty \frac{\sin x}{x} \dd{x}$ converges, but $\int_0^\infty \lvert \sin x/x\rvert \dd{x}$ diverges, so it is *conditionally convergent*, which corresponds to conditional convergence of series.

The two criteria above were stated for integrals over infinite intervals, but after a change of variables they apply equally well to improper integrals that diverge at an endpoint. For $\int_c^b f(x) \dd{x}$ where $f$ is singular at the left endpoint $c$, set $u = 1/(x - c)$; then $x \rightarrow c^+$ corresponds to $u \rightarrow \infty$, and matching the orientation of the interval of integration gives

$$\int_c^b f(x) \dd{x} = \int_{1/(b-c)}^\infty \frac{f(c + 1/u)}{u^2} \dd{u}$$

which is an integral over an infinite interval. The factor $u^{-2} > 0$ preserves inequalities and absolute values, so [Proposition 3](#prop3) and [Proposition 4](#prop4) remain valid as convergence tests for improper integrals.

For these tests to be useful in practice, one needs standard functions to compare against, and the role is almost always filled by power functions or the exponential function $e^{-x}$. Among them, the integral of a power function provides a (nearly) sharp boundary between convergence and divergence.

::: Example 5 (p-integrals)
Improper integrals of powers exhibit exactly opposite behavior at infinite intervals and singular points. The infinite interval $\int_1^{\infty} x^{-p} \dd{x}$ converges for $p > 1$ and diverges for $p \leq 1$, whereas the integral $\int_0^1 x^{-p} \dd{x}$ containing a singular point conversely converges for $p < 1$ and diverges for $p \geq 1$. Both computations arise from the same antiderivative: for $p \neq 1$,

$$\int_1^t x^{-p} \dd{x} = \frac{t^{1-p} - 1}{1 - p}, \qquad \int_t^1 x^{-p} \dd{x} = \frac{1 - t^{1-p}}{1 - p}$$

For the left improper integral, as $t \rightarrow \infty$, the term $t^{1-p}$ tends to $0$ when $p > 1$; for the right singular integral, as $t \rightarrow 0^+$, the term $t^{1-p}$ converges to $0$ when $p < 1$, making the integral finite. The respective limiting values are

$$\int_1^\infty x^{-p} \dd{x} = \frac{1}{p - 1} \quad (p > 1), \qquad \int_0^1 x^{-p} \dd{x} = \frac{1}{1 - p} \quad (p < 1)$$

Intuitively, on an infinite interval a large $p$ causes rapid decay, helping convergence, whereas near a singular point a large $p$ causes faster blow-up, leading to divergence; this can be seen clearly by plotting $1/x$ and $1/x^2$.

{% diagram Math/Calculus/Improper_Integrals-1.svg width="12.69em" alt="Graphs of 1/x and 1/x²" %}
:::

However, this boundary $p = 1$ is somewhat subtle. Since substitution works for improper integrals just as well, setting $u = \ln x$ gives

$$\int_2^\infty \frac{\dd{x}}{x(\ln x)^p} = \int_{\ln 2}^\infty u^{-p} \dd{u}$$

which converges for $p > 1$. Thus $1/x$ itself diverges at $p = 1$, but attaching a logarithm raised to a power greater than one shifts the boundary back toward convergence. In other words, considering only powers, $p = 1$ is the exact boundary, but inserting a logarithmic factor produces a finer split; this is why we said earlier that this boundary is *almost* sharp.

On the other hand, convergent improper integrals can be used to define new functions.

::: Example 6 (Gamma function)
The following function defined as an improper integral

$$\Gamma(s) = \int_0^\infty x^{s-1}e^{-x} \dd{x}$$

converges for $s > 0$. Near $0$, the singular integral of $x^{s-1}$ converges for $s > 0$ ([Example 5](#ex5)), and near $\infty$, the exponential $e^{-x}$ dominates any power. By integration by parts,

$$\Gamma(s+1) = \bigl[-x^s e^{-x}\bigr]_0^\infty + s\int_0^\infty x^{s-1}e^{-x} \dd{x} = s \Gamma(s)$$

and since $\Gamma(1) = \int_0^\infty e^{-x} \dd{x} = 1$, we have $\Gamma(n) = (n-1)!$. Thus the gamma function extends the factorial to real numbers.
:::

---

**References**

**[Ste]** J. Stewart, *Calculus*, 8th ed., Cengage Learning, 2016.  
**[Kim]** 김홍종, *미적분학 1·2*, 제3개정판, 서울대학교출판문화원, 2020.
