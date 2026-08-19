---
title: "Power Series"
description: "This post covers power series formed by powers of a variable, their radius of convergence, and their values. It also examines power series expansions of elementary functions, addition and multiplication of power series, and the definition of analytic functions."
excerpt: "Power series, radius of convergence, elementary function expansions, and analytic functions"

categories: [Math / Calculus]
permalink: /en/math/calculus/power_series
sidebar: 
    nav: "calculus-en"

date: 2026-06-22
weight: 5
translated_at: 2026-08-19T06:15:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-08-19T06:15:04+00:00
---
There are two main reasons we defined the limit and continuity of functions before defining the limit of sequences and infinite series. First, the method of exhaustion used in definite integration requires infinite series in any case, and we did not want the flow from differentiation to integration to be interrupted by the limit of sequences. Second, we wished to define power series first in this post.

Power series provide another way of writing functions, and their introduction makes it easier to handle functions that could not be treated in high school. For example, when defining the exponential function $2^x$ in high school, we did not rigorously define its values at irrational numbers; doing so requires the completeness of the real numbers used in [§Continuous Functions, ⁋Theorem 5](/en/math/calculus/continuity#thm5) or [§Limits of Sequences, ⁋Proposition 7](/en/math/calculus/sequences#prop7). Moreover, even after defining the exponential function, when defining the natural constant in [§Limits of Sequences, ⁋Example 8](/en/math/calculus/sequences#ex8) we had to resort to a somewhat ambiguous description: *the exponential function that remains itself upon differentiation*. By contrast, if we define the exponential function $e^x$ by a power series, none of this complexity arises, and we can neatly express even functions that are not elementary, such as the integral of $e^{-x^2}$.

## Power Series and Radius of Convergence

::: Definition 1
A *power series* centered at $a$ is a series of the form

$$\sum_{n=0}^{\infty} c_n (x - a)^n = c_0 + c_1(x-a) + c_2(x-a)^2 + \cdots$$

for a sequence $(c_n)_{n\geq 0}$. The set of $x$ for which this series converges is called the *domain of convergence*, and the sum of the series defines a function of $x$ on this set.
:::

To simplify the discussion, we henceforth mainly treat the case $a = 0$, that is, $\sum c_n x^n$; the general case follows by replacing $x$ with $x - a$, so this is not a significant loss of generality.

From the definition, at $x = 0$ only the first term $c_0$ remains, so the domain of convergence is at least nonempty. Moreover, if a power series converges at some $x_0 \neq 0$, then this power series converges absolutely for all $x$ with $\lvert x\rvert < \lvert x_0\rvert$. This is because if $\sum c_n x_0^n$ converges, the general term tends to $0$, so there exists $M$ with $\lvert c_n x_0^n\rvert \leq M$, and setting $r = \lvert x/x_0\rvert < 1$ gives

$$\lvert c_n x^n\rvert = \lvert c_n x_0^n\rvert \cdot r^n \leq M r^n$$

and the right-hand side is a convergent geometric series with common ratio $r < 1$, so we may apply [§Infinite Series, ⁋Theorem 6](/en/math/calculus/series#thm6). Now let $R$ be the supremum of the absolute values of convergent $x$ (if there are infinitely many such $x$, set $R=\infty$). If $\lvert x\rvert<R$, then there exists a convergent $x_0$ with $\lvert x\rvert<\lvert x_0\rvert$, so the fact shown above gives absolute convergence; if $\lvert x\rvert>R$, then by the definition of supremum the series diverges. Thus we obtain the following theorem.

::: Theorem 2 (Radius of convergence)
For each power series $\sum c_n x^n$, there exists a *radius of convergence* $R$ with $0 \leq R \leq \infty$ such that the series converges absolutely when $\lvert x\rvert < R$ and diverges when $\lvert x\rvert > R$.
:::

When $R=0$, this is interpreted as the given power series converging only at $x=0$ (hence not of interest to us); at the opposite extreme $R=\infty$, the given power series converges for all real numbers. Apart from these two cases, the radius of convergence does not determine convergence at $\lvert x\rvert=R$, and in fact all combinations are possible depending on the power series.

Because of its form, the radius of convergence of a power series is usually computed by the ratio test or [§Infinite Series, ⁋Proposition 8](/en/math/calculus/series#prop8). For example, when $c_n \neq 0$ for sufficiently large $n$, applying the ratio test and assuming $\left\lvert c_{n+1}/c_n\right\rvert \rightarrow L$, the ratio of adjacent terms approaches $L\lvert x\rvert$, so we may set $R = 1/L$; more generally,

$$\frac{1}{R} = \limsup_{n\rightarrow\infty} \lvert c_n\rvert^{1/n}$$

always holds. For example, applying the ratio test to $\sum_n x^n/n!$, the ratio of adjacent terms is $\lvert x\rvert/(n+1) \rightarrow 0$, so $R = \infty$, that is, this power series converges for all real numbers.

## Expansions of Elementary Functions

One of the benefits of introducing power series early is that the exponential function can be defined in a more rigorous way.

::: Example 3 (Exponential function)
We write the power series converging for all real numbers seen above as

$$e^x = \sum_{n=0}^\infty \frac{x^n}{n!}$$

In particular, substituting $x = 1$ gives $e = \sum 1/n!$, and this number coincides with the natural constant defined as the limit $\lim(1 + 1/n)^n$ in [§Limits of Sequences, ⁋Example 8](/en/math/calculus/sequences#ex8).

The proof is as follows. Let $L = \lim(1+1/n)^n$ be the limit value and $s_m = \sum 1/k!$ be the partial sum of the series. In [§Limits of Sequences, ⁋Example 8](/en/math/calculus/sequences#ex8) above, we already showed by the binomial theorem that

$$\left(1 + \frac1n\right)^n = \sum_{k=0}^n \binom{n}{k}\frac{1}{n^k} = \sum_{k=0}^n \frac{1}{k!}\prod_{j=0}^{k-1}\left(1 - \frac{j}{n}\right)$$

and also that this sequence is increasing so that its limit $L$ is the supremum of its terms.

First, since each factor $1 - j/n$ in the product is at most $1$, the above sum is at most $\sum_{k=0}^n 1/k! = s_n$, and the partial sum is again at most its limit $s = \sum_{n=0}^\infty 1/n!$, so $(1 + 1/n)^n \leq s$ for all $n$. Since $L$ is the supremum of the terms and $s$ is an upper bound, we obtain $L \leq s$. Conversely, fixing $m$ and considering only $n \geq m$, we drop the nonnegative later terms in the above sum to obtain

$$\left(1 + \frac1n\right)^n \geq \sum_{k=0}^m \frac{1}{k!}\prod_{j=0}^{k-1}\left(1 - \frac{j}{n}\right)$$

The left-hand side is at most $L$, so the right-hand side is also at most $L$, and sending $n \rightarrow \infty$ with $m$ fixed, the right-hand side is a finite sum and each factor satisfies $1 - j/n \rightarrow 1$, so by [§Limits of Sequences, ⁋Proposition 2](/en/math/calculus/sequences#prop2) it converges to $s_m$. If every term of a convergent sequence is at most $L$, then its limit is also at most $L$, so $s_m \leq L$, and sending $m \rightarrow \infty$ gives $s \leq L$. Combining the two inequalities yields $L = s$, that is, the $e$ defined in the two posts is the same number.
:::

## Operations on Power Series

::: Proposition 4
If $f(x) = \sum a_n x^n$ and $g(x) = \sum b_n x^n$ have radii of convergence $R_f, R_g$ respectively, then for $\lvert x\rvert < \min(R_f, R_g)$,

$$f(x) + g(x) = \sum_{n=0}^\infty (a_n + b_n)x^n, \qquad f(x)g(x) = \sum_{n=0}^\infty \left(\sum_{k=0}^n a_k b_{n-k}\right) x^n$$

The coefficients of the product are the *Cauchy product* of the two coefficient sequences.
:::

The Cauchy product is the extension to infinite degree of multiplying two polynomials and collecting terms of the same degree. For example, multiplying $1/(1-x) = \sum_n x^n$ by itself, the coefficient of degree $n$ becomes $\sum_{k=0}^n 1\cdot 1 = n+1$, yielding $1/(1-x)^2 = \sum_n (n+1)x^n$. Applying this computation to $\sum_n x^n/n!$ and $\sum_n y^n/n!$, the $n$th term becomes by the binomial theorem $\sum_{k=0}^n x^ky^{n-k}/(k!(n-k)!) = (x+y)^n/n!$, yielding the exponential law $e^{x+y} = e^xe^y$, which justifies the notation writing the series as $e^x$ in [Example 3](#ex3).

## Analytic Functions

::: Definition 5
If a function $f$ coincides in a neighborhood of a point $a$ with a power series centered there, we say $f$ is *analytic* at $a$. If $f$ is analytic at every point of its domain, we call $f$ an *analytic function*.
:::

An analytic function coincides with its Taylor series. However, the converse is false. The function $f(x) = e^{-1/x^2}$ (with $f(0) = 0$) is smooth on all of $\mathbb{R}$ but has all derivatives $0$ at $0$, so its Taylor series is identically $0$ and thus does not coincide with $f$ in any neighborhood of $0$; hence $f$ is not analytic at $0$. That is, smoothness does not guarantee analyticity, and whether the Taylor series converges to the function can be determined via the remainder term in Taylor's theorem after learning differentiation.

---

**References**

**[Ste]** J. Stewart, *Calculus*, 8th ed., Cengage Learning, 2016.  
**[Kim]** 김홍종, *미적분학 1·2*, 제3개정판, 서울대학교출판문화원, 2020.
