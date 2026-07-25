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
translated_at: 2026-06-27T18:30:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-27T18:30:02+00:00
---
The integrals we have examined so far were defined for bounded functions on finite intervals. However, we often want to discuss area even when the interval extends to infinity or the integrand becomes infinite at a point. In this post we define such cases as limits of integrals over finite intervals.

## Definition of Improper Integrals

We first give the following definition.

::: Definition 1
If $f$ is integrable on $[a, t]$ for every $t > a$, we define the *improper integral* over the infinite interval by

$$\int_a^{\infty} f(x) \mathop{dx} = \lim_{t \rightarrow \infty}\int_a^t f(x) \mathop{dx}$$

and say that the improper integral *converges* if this limit exists as a finite value. Similarly, if $f$ is integrable on $[t, b]$ for every $t < b$, then the expression

$$\int_{-\infty}^b f(x)\mathop{dx}=\lim_{t \rightarrow -\infty}\int_t^b f(x) \mathop{dx}$$

is said to converge if the limit exists as a finite value. If for some $c$ both improper integrals

$$\int_{-\infty}^c f(x) \mathop{dx},\qquad \int_c^{\infty} f(x) \mathop{dx}$$

converge, we denote their sum

$$\int_{-\infty}^c f(x) \mathop{dx} + \int_c^{\infty} f(x) \mathop{dx}$$

concisely by the expression

$$\int_{-\infty}^{\infty} f(x) \mathop{dx}$$
:::

In the above definition, the two improper integrals

$$\int_a^\infty f(x)\mathop{dx},\qquad \int_{-\infty}^b f(x)\mathop{dx}$$

are relatively clear. The slightly ambiguous part is the integral with infinity on both sides. We first observe that if this integral is defined, its value does not depend on the choice of the partition point $c$. This is because if we choose another $c'$,

$$\begin{aligned}\int_{-\infty}^c f(x)\mathop{dx}+\int_c^\infty f(x)\mathop{dx}&=\lim_{s\rightarrow-\infty}\int_s^c f(x)\mathop{dx}+\lim_{t\rightarrow \infty}\int_c^t f(x)\mathop{dx}\\&=\lim_{s\rightarrow-\infty}\left(\int_s^c f(x)\mathop{dx}+\int_c^{c'} f(x)\mathop{dx}\right)+\lim_{t\rightarrow \infty}\left(\int_c^t f(x)\mathop{dx}-\int_c^{c'} f(x)\mathop{dx}\right)\\&=\lim_{s\rightarrow-\infty}\int_s^{c'} f(x)\mathop{dx}+\lim_{t\rightarrow \infty}\int_{c'}^t f(x)\mathop{dx}\\&=\int_{-\infty}^{c'} f(x)\mathop{dx}+\int_{c'}^\infty f(x)\mathop{dx}\end{aligned}$$

so the values are equal. A more subtle point deserving attention is that we send these two limits *independently*. For example, defining the sign function by

$$\sgn(x)=\begin{cases}1&\text{if $x>0$}\\0&\text{if $x=0$}\\-1&\text{if $x<0$}\end{cases}$$

for a fixed $t>0$ the integral of this function from $-t$ to $t$ is $0$, and hence

$$\lim_{t\rightarrow\infty}\int_{-t}^t \sgn(x)\mathop{dx}=0$$

but according to the above definition the improper integral of $\sgn$ is not defined. If we had taken the interval from $-t$ to $2t$ and then let $t\rightarrow\infty$, the limit would have diverged, so this restriction is essential.

Similarly, we define the integral of a function that blows up at a point as a limit.

::: Definition 2
If $f$ becomes infinite at $c$ but is integrable on $[a, t]$ for every $t < c$, we define the *singular integral* by

$$\int_a^c f(x) \mathop{dx} = \lim_{t \rightarrow c^-}\int_a^t f(x) \mathop{dx}$$

Similarly, if $f$ becomes infinite at $c$ but is integrable on $[t, b]$ for every $c < t$, we define its singular integral by

$$\int_c^b f(x) \mathop{dx} = \lim_{t \rightarrow c^+}\int_t^b f(x) \mathop{dx}$$

If $f$ becomes infinite at a point $c$ inside $[a,b]$, we define this singular integral by

$$\int_a^b f(x)\mathop{dx}=\lim_{t\rightarrow c^-}\int_a^t f(x)\mathop{dx}+\lim_{s\rightarrow c^+} \int_s^b f(x)\mathop{dx}$$
:::

Again, when $c$ lies inside the interval, the same subtlety as in [Definition 1](#def1) remains. For instance,

$$\lim_{t\rightarrow 0^-}\int_{-1}^t \frac{dx}{x}+\lim_{s\rightarrow 0^+}\int_s^1\frac{dx}{x}$$

is not defined in each term separately, but if we had grouped them as

$$\lim_{t\rightarrow 0^+}\left(\int_{-1}^{-t} \frac{dx}{x}+\int_t^1\frac{dx}{x}\right)$$

the value would have become $0$, which is problematic.

## Convergence Tests for Improper Integrals

Many improper integrals cannot be evaluated explicitly because an antiderivative is unavailable. However, convergence alone can be decided by comparison with a more manageable function. When the integrand is non-negative the integral is monotonically increasing in the interval of integration, so a comparison test analogous to that for series holds.

::: Proposition 3 (Comparison Test)
Suppose $0 \leq f(x) \leq g(x)$ for $x \geq a$. If $\int_a^\infty g(x) \mathop{dx}$ converges then $\int_a^\infty f(x) \mathop{dx}$ also converges, and if $\int_a^\infty f(x) \mathop{dx}$ diverges then $\int_a^\infty g(x) \mathop{dx}$ also diverges.
:::

::: Proof
$F(t) = \int_a^t f(x) \mathop{dx}$ is increasing in $t$ because $f \geq 0$, and by monotonicity ([§Integration, ⁋Proposition 11](/en/math/calculus/integration#prop11))

$$F(t) \leq \int_a^t g(x) \mathop{dx} \leq \int_a^\infty g(x) \mathop{dx}$$

so it is bounded above. An increasing function bounded above has a limit as $t \rightarrow \infty$, so $\int_a^\infty f(x) \mathop{dx}$ converges. The second claim is the contrapositive.
:::

When the direct inequality $0 \leq f \leq g$ is difficult to establish, we use a limit comparison as in series. That is, if two positive functions satisfy $f(x)/g(x) \rightarrow c$ ($0 < c < \infty$), then by the same argument as in [§Infinite Series, ⁋Proposition 7](/en/math/calculus/series#prop7) the two integrals converge or diverge together, so it suffices to know which function the integrand behaves like as $x \rightarrow \infty$.

For integrands that change sign we reduce to the positive case by taking absolute values.

::: Proposition 4 (Absolute Convergence)
If $\int_a^\infty \lvert f(x)\rvert \mathop{dx}$ converges then $\int_a^\infty f(x) \mathop{dx}$ also converges.
:::

::: Proof
Since $0 \leq f + \lvert f\rvert \leq 2\lvert f\rvert$, by [Proposition 3](#prop3) the integral $\int_a^\infty (f(x) + \lvert f(x)\rvert) \mathop{dx}$ converges, and therefore $\int_a^\infty f(x) \mathop{dx} = \int_a^\infty (f(x) + \lvert f(x)\rvert) \mathop{dx} - \int_a^\infty \lvert f(x)\rvert \mathop{dx}$ also converges.
:::

The converse does not hold. $\int_0^\infty \frac{\sin x}{x} \mathop{dx} = \frac\pi2$ converges but $\int_0^\infty \lvert \sin x/x\rvert \mathop{dx}$ diverges, so it is *conditionally convergent*, corresponding to conditional convergence of series.

The two tests above were stated for integrals over infinite intervals, but after a change of variables they apply equally to singular integrals that diverge at an endpoint. For $\int_c^b f(x) \mathop{dx}$ with $f$ singular at the left endpoint $c$, setting $u = 1/(x - c)$ makes $x \rightarrow c^+$ correspond to $u \rightarrow \infty$, and matching the orientation of the interval gives

$$\int_c^b f(x) \mathop{dx} = \int_{1/(b-c)}^\infty \frac{f(c + 1/u)}{u^2} \mathop{du}$$

which becomes an integral over an infinite interval. The factor $u^{-2} > 0$ preserves inequalities and absolute values, so [Proposition 3](#prop3) and [Proposition 4](#prop4) remain valid for convergence tests of singular integrals.

For these tests to be useful in practice we need standard functions to compare against, and the role is almost always played by power functions or the exponential $e^{-x}$. Among them, the integral of a power function exhibits a (nearly) sharp boundary between convergence and divergence.

::: Example 5 (p-integral)
The improper integral of a power shows exactly opposite boundaries at infinity and at a singularity. The infinite interval $\int_1^{\infty} x^{-p} \mathop{dx}$ converges for $p > 1$ and diverges for $p \leq 1$, whereas the singularity-inclusive integral $\int_0^1 x^{-p} \mathop{dx}$ conversely converges for $p < 1$ and diverges for $p \geq 1$. Both calculations come from the same antiderivative: for $p \neq 1$,

$$\int_1^t x^{-p} \mathop{dx} = \frac{t^{1-p} - 1}{1 - p}, \qquad \int_t^1 x^{-p} \mathop{dx} = \frac{1 - t^{1-p}}{1 - p}$$

and for the left improper integral $t^{1-p} \rightarrow 0$ as $t \rightarrow \infty$ when $p > 1$, while for the right singular integral $t^{1-p} \rightarrow 0$ as $t \rightarrow 0^+$ when $p < 1$, making the integral finite. In each case the convergent values are

$$\int_1^\infty x^{-p} \mathop{dx} = \frac{1}{p - 1} \quad (p > 1), \qquad \int_0^1 x^{-p} \mathop{dx} = \frac{1}{1 - p} \quad (p < 1)$$

Intuitively, on an infinite interval a large $p$ causes rapid decrease and helps convergence, whereas near a singularity a large $p$ causes more rapid increase and leads to divergence; this can be seen clearly in the following figure, which plots $1/x$ and $1/x^2$.

{% diagram Math/Calculus/Improper_Integrals-1.svg width="12.69em" alt="Graphs of 1/x and 1/x²" %}
:::

However, the boundary $p = 1$ is somewhat subtle. Since substitution remains valid for improper integrals, setting $u = \ln x$ gives

$$\int_2^\infty \frac{dx}{x(\ln x)^p} = \int_{\ln 2}^\infty u^{-p} \mathop{du}$$

which converges for $p > 1$. Thus $1/x$ itself diverges at $p = 1$, but attaching a power of logarithm one or higher shifts the boundary back toward convergence. In other words, considering powers alone, $p = 1$ is the exact boundary, but inserting a logarithmic factor splits it more finely; this is why we said above that this boundary is *almost* sharp.

On the other hand, convergent improper integrals are used to define new functions.

::: Example 6 (Gamma function)
The function defined by the improper integral

$$\Gamma(s) = \int_0^\infty x^{s-1}e^{-x} \mathop{dx}$$

converges for $s > 0$. Near $0$ the singular integral of $x^{s-1}$ converges for $s > 0$ ([Example 5](#ex5)), and near $\infty$ the exponential $e^{-x}$ overwhelms any power. Integration by parts gives

$$\Gamma(s+1) = \bigl[-x^s e^{-x}\bigr]_0^\infty + s\int_0^\infty x^{s-1}e^{-x} \mathop{dx} = s \Gamma(s)$$

and since $\Gamma(1) = \int_0^\infty e^{-x} \mathop{dx} = 1$ we have $\Gamma(n) = (n-1)!$. Thus the gamma function extends the factorial to real numbers.
:::
