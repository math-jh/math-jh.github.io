---
title: "Power Series"
description: "This post covers power series formed by repeated powers of a variable, their radius of convergence, and their values. It also examines power series expansions of elementary functions, arithmetic operations on power series, and the definition of analytic functions."
excerpt: "Power series, radius of convergence, elementary function expansions, and analytic functions"

categories: [Math / Calculus]
permalink: /en/math/calculus/power_series
sidebar: 
    nav: "calculus-en"

date: 2026-06-22
weight: 5
translated_at: 2026-06-21T21:00:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-21T21:00:02+00:00
---
The main reasons we defined limits of sequences and infinite series before limits and continuity of functions are twofold. The first reason is that we will need to handle infinite series anyway for the Riemann sums used in definite integrals, so we wanted to avoid having limits of sequences disrupt the flow from differentiation to integration. The second reason is precisely to define power series early in this article.

A power series is essentially another way of writing a function, and its importance lies in the fact that by introducing it, we can handle functions much more easily that we could not deal with in high school. For example, when we defined the exponential function $$2^x$$ in high school, we did not rigorously define its values at irrational numbers; in fact, defining values in such a way requires the completeness of the real numbers, which was needed in [§Continuous Functions, ⁋Theorem 5](/en/math/calculus/continuity#thm5) or [§Limits of Sequences, ⁋Proposition 7](/en/math/calculus/sequences#prop7). Moreover, after defining the exponential function, when we defined the natural constant in [§Limits of Sequences, ⁋Example 8](/en/math/calculus/sequences#ex8), we had to resort to somewhat vague descriptions such as <em>the exponential function that remains itself upon differentiation</em>. On the other hand, defining the exponential function $$e^x$$ as a power series does not require such complexity, and moreover, functions that do not have an elementary antiderivative, such as the integral of $$e^{-x^2}$$, can be neatly expressed as a power series.

## Power Series and Radius of Convergence

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> A *power series* centered at $$a$$ is a series of the form

$$\sum_{n=0}^{\infty} c_n (x - a)^n = c_0 + c_1(x-a) + c_2(x-a)^2 + \cdots$$

for a sequence $$(c_n)_{n\geq 0}$$. The set of $$x$$ for which this series converges is called the *domain of convergence*, and the sum of the series defines a function of $$x$$ on this domain.

</div>

To simplify the discussion, we will mainly deal with the case $$a = 0$$, i.e., $$\sum c_n x^n$$, from now on; the general case can be reduced to this by replacing $$x$$ with $$x - a$$, so this is not a significant loss of generality.

From the definition, at $$x = 0$$ only the first term $$c_0$$ remains, so the domain of convergence is at least nonempty. Furthermore, if a power series converges at some $$x_0 \neq 0$$, then this power series converges absolutely for all $$x$$ with $$\lvert x\rvert < \lvert x_0\rvert$$. This is because if $$\sum c_n x_0^n$$ converges, then the general term goes to $$0$$, so there exists an $$M$$ such that $$\lvert c_n x_0^n\rvert \leq M$$, and letting $$r = \lvert x/x_0\rvert < 1$$, we have

$$\lvert c_n x^n\rvert = \lvert c_n x_0^n\rvert \cdot r^n \leq M r^n$$

and the right-hand side is a convergent geometric series with common ratio $$r < 1$$, so we can apply [§Infinite Series, ⁋Theorem 6](/en/math/calculus/series#thm6). Now let $$R$$ be the supremum of the absolute values of the $$x$$ at which the series converges (if there are unboundedly many such $$x$$, set $$R=\infty$$). If $$\lvert x\rvert<R$$, then there exists an $$x_0$$ with $$\lvert x\rvert<\lvert x_0\rvert$$ at which the series converges, so it converges absolutely by the fact shown above; if $$\lvert x\rvert>R$$, then it diverges by the definition of the supremum. Thus we obtain the following theorem.

<div class="proposition" markdown="1">

<ins id="thm2">**Theorem 2 (Radius of Convergence)**</ins> For each power series $$\sum c_n x^n$$, there exists a *radius of convergence* $$R$$ with $$0 \leq R \leq \infty$$ such that the series converges absolutely if $$\lvert x\rvert < R$$ and diverges if $$\lvert x\rvert > R$$.

</div>

The case $$R=0$$ is interpreted as the given power series converging only at $$x=0$$ (and thus is not of interest to us), while the opposite extreme $$R=\infty$$ is interpreted as the given power series converging on the entire real line. Apart from these two cases, the radius of convergence does not determine convergence at $$\lvert x\rvert=R$$, and in fact all combinations are possible depending on the power series.

Because of its form, the radius of convergence of a power series is usually computed by the ratio test or the root test. For example, applying the ratio test, if $$\left\lvert c_{n+1}/c_n\right\rvert \to L$$, then the ratio of adjacent terms approaches $$L\lvert x\rvert$$, so we can set $$R = 1/L$$, and more generally

$$\frac{1}{R} = \limsup_{n\to\infty} \lvert c_n\rvert^{1/n}$$

always holds.

<div class="example" markdown="1">

<ins id="ex3">**Example 3 (Computing the Radius of Convergence)**</ins> For example,

$$\sum \frac{x^n}{n!}:\frac{n!}{(n+1)!} = \frac{1}{n+1} \to 0 \implies R = \infty$$

so this series converges on the entire real line.

</div>

## Expansion of Elementary Functions

As mentioned above, one of the benefits of introducing power series early is that we can define the exponential function in a more rigorous way.

<div class="example" markdown="1">

<ins id="ex4">**Example 4 (Exponential Function)**</ins> We write the power series from [Example 3](#ex3) as

$$e^x = \sum_{n=0}^\infty \frac{x^n}{n!}$$

In particular, substituting $$x = 1$$ gives $$e = \sum 1/n!$$, and this number coincides with the natural constant defined as the limit $$\lim(1 + 1/n)^n$$ in [§Limits of Sequences, ⁋Example 8](/en/math/calculus/sequences#ex8).

The proof is as follows. Let $$L = \lim(1+1/n)^n$$ be the limit value and $$s_m = \sum 1/k!$$ be the partial sum of the series. In [§Limits of Sequences, ⁋Example 8](/en/math/calculus/sequences#ex8) above, we already showed by the binomial theorem that

$$\left(1 + \frac1n\right)^n = \sum_{k=0}^n \binom{n}{k}\frac{1}{n^k} = \sum_{k=0}^n \frac{1}{k!}\prod_{j=0}^{k-1}\left(1 - \frac{j}{n}\right)$$

and also showed that this sequence is increasing and that its limit $$L$$ is the supremum of its terms.

First, since each factor $$1 - j/n$$ in the product is at most $$1$$, the above sum is at most $$\sum_{k=0}^n 1/k! = s_n$$, and the partial sum is again at most its limit $$s = \sum_{n=0}^\infty 1/n!$$, so $$(1 + 1/n)^n \leq s$$ for all $$n$$. Since $$L$$ is the supremum of the terms and $$s$$ is an upper bound, we obtain $$L \leq s$$. Conversely, fixing $$m$$ and considering only $$n \geq m$$, dropping the nonnegative terms on the right side of the above sum gives

$$\left(1 + \frac1n\right)^n \geq \sum_{k=0}^m \frac{1}{k!}\prod_{j=0}^{k-1}\left(1 - \frac{j}{n}\right)$$

The left-hand side is at most $$L$$, so the right-hand side is also at most $$L$$, and sending $$n \to \infty$$ with $$m$$ fixed, the right-hand side is a finite sum and each factor satisfies $$1 - j/n \to 1$$, so by the limit laws ([§Limits of Sequences, ⁋Proposition 2](/en/math/calculus/sequences#prop2)) it converges to $$s_m$$. If all terms of a convergent sequence are at most $$L$$, then its limit is also at most $$L$$, so $$s_m \leq L$$, and sending $$m \to \infty$$ gives $$s \leq L$$. Combining the two inequalities yields $$L = s$$, i.e., the $$e$$ defined in both ways is the same number.

</div>

## Operations on Power Series

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> If $$f(x) = \sum a_n x^n$$ and $$g(x) = \sum b_n x^n$$ have radii of convergence $$R_f$$ and $$R_g$$ respectively, then for $$\lvert x\rvert < \min(R_f, R_g)$$ we have

$$f(x) + g(x) = \sum_{n=0}^\infty (a_n + b_n)x^n, \qquad f(x)g(x) = \sum_{n=0}^\infty \left(\sum_{k=0}^n a_k b_{n-k}\right) x^n$$

The coefficients of the product are the *Cauchy product* of the two coefficient sequences.

</div>

The Cauchy product is the extension to infinite degree of multiplying two polynomials and collecting terms of the same degree. For example, multiplying $$\dfrac{1}{1-x} = \sum x^n$$ by itself gives the $$n$$-th coefficient as $$\sum_{k=0}^n 1\cdot 1 = n+1$$, yielding $$\dfrac{1}{(1-x)^2} = \sum (n+1)x^n$$.

## Analytic Functions

<div class="definition" markdown="1">

<ins id="def6">**Definition 6**</ins> A function $$f$$ is said to be *analytic* at a point $$a$$ if it coincides with a power series centered at $$a$$ in a neighborhood of $$a$$. If $$f$$ is analytic at every point of its domain, it is called an *analytic function*.

</div>

By Definition 6, an analytic function coincides with its Taylor series. However, the converse is false. The function $$f(x) = e^{-1/x^2}$$ (with $$f(0) = 0$$) is smooth on all of $$\mathbb{R}$$, but all derivatives at $$0$$ are $$0$$, so its Taylor series is identically $$0$$, and thus it does not coincide with $$f$$ in any neighborhood of $$0$$; hence $$f$$ is not analytic at $$0$$. That is, smoothness does not guarantee analyticity, and whether the Taylor series converges to the function can be determined via the remainder term in Taylor's theorem after learning differentiation. In complex analysis, which bridges this gap, (complex) differentiability is equivalent to analyticity, and the situation changes dramatically.

In this way, power series allow us to treat functions as polynomials of infinite degree, and they have wide applications in series solutions of differential equations, numerical approximation, and definitions of special functions. The rigorous theory of uniform convergence of power series and analytic functions is treated in analysis [\[Analysis\] §Power Series and Analytic Functions](/en/math/analysis/power_series).
