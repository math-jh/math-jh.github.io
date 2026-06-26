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
drift_needed: true
translated_at: 2026-06-26T11:00:02+00:00
translation_source: kimi-cli
---
The reason we defined the limit and continuity of a function first, and then defined the limit of a sequence and infinite series, is largely twofold. The first reason is that the method of exhaustion used in definite integration requires dealing with infinite series anyway, so we wanted to prevent the limit of sequences from interrupting the flow from differentiation to integration. The second reason is precisely to define power series first in this article.

Power series provide another way of writing functions, and by introducing them we can handle functions more easily that could not be treated in high school. For example, when defining the exponential function $$2^x$$ in high school, we did not rigorously define the function values at irrational numbers; to do so would require the completeness of real numbers used in [§Continuous Functions, ⁋Theorem 5](/en/math/calculus/continuity#thm5) or [§Limits of Sequences, ⁋Proposition 7](/en/math/calculus/sequences#prop7). Moreover, after defining the exponential function, when defining the natural constant in [§Limits of Sequences, ⁋Example 8](/en/math/calculus/sequences#ex8), we had to resort to somewhat vague methods, such as <em-ko>an exponential function that differentiates to itself</em-ko>. On the other hand, if we define the exponential function $$e^x$$ by a power series, none of this complexity arises, and we can also express cleanly functions that do not have an elementary antiderivative, such as the integral of $$e^{-x^2}$$.

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

Because of its shape, the radius of convergence of a power series is usually computed using the ratio test or [§Infinite Series, ⁋Proposition 8](/en/math/calculus/series#prop8). For instance, applying the ratio test, if $$\left\lvert c_{n+1}/c_n\right\rvert \to L$$ then the ratio of adjacent terms approaches $$L\lvert x\rvert$$, so we know that setting $$R = 1/L$$ works, and more generally,

$$\frac{1}{R} = \limsup_{n\to\infty} \lvert c_n\rvert^{1/n}$$

always holds. For example, applying the ratio test to $$\sum_n x^n/n!$$, the ratio of adjacent terms is $$\lvert x\rvert/(n+1) \to 0$$, so $$R = \infty$$; that is, this power series converges on the entire real line.

## Expansion of Elementary Functions

One of the benefits of introducing power series early is that we can define the exponential function in a more solid way.

<div class="example" markdown="1">

<ins id="ex3">**Example 3 (Exponential function)**</ins> We write the power series converging over all real numbers seen above as

$$e^x = \sum_{n=0}^\infty \frac{x^n}{n!}$$

In particular, substituting $$x = 1$$ gives $$e = \sum 1/n!$$, and this number coincides with the natural constant defined as the limit $$\lim(1 + 1/n)^n$$ in [§Limits of Sequences, ⁋Example 8](/en/math/calculus/sequences#ex8).

The proof is as follows. Let the limit value of that limit be $$L = \lim(1+1/n)^n$$, and let the partial sum of the series be $$s_m = \sum 1/k!$$. Then in [§Limits of Sequences, ⁋Example 8](/en/math/calculus/sequences#ex8) above, we already showed by the binomial theorem that

$$\left(1 + \frac1n\right)^n = \sum_{k=0}^n \binom{n}{k}\frac{1}{n^k} = \sum_{k=0}^n \frac{1}{k!}\prod_{j=0}^{k-1}\left(1 - \frac{j}{n}\right)$$

and also that this sequence is increasing, so its limit $$L$$ is the supremum of the terms.

First, since each factor $$1 - j/n$$ in the product is at most $$1$$, the above sum is at most $$\sum_{k=0}^n 1/k! = s_n$$, and the partial sums are in turn at most their limit $$s = \sum_{n=0}^\infty 1/n!$$, so $$(1 + 1/n)^n \leq s$$ for all $$n$$. Since $$L$$ is the supremum of the terms and $$s$$ is an upper bound, we obtain $$L \leq s$$. Conversely, fixing $$m$$ and considering only $$n \geq m$$, we drop the nonnegative latter terms in the above sum to obtain

$$\left(1 + \frac1n\right)^n \geq \sum_{k=0}^m \frac{1}{k!}\prod_{j=0}^{k-1}\left(1 - \frac{j}{n}\right)$$

Since the left-hand side is at most $$L$$, the right-hand side is also at most $$L$$, and fixing $$m$$ while sending $$n \to \infty$$, the right-hand side is a finite sum and each factor satisfies $$1 - j/n \to 1$$, so by [§Limits of Functions, ⁋Proposition 5](/en/math/calculus/functions_and_limits#prop5) ([§Limits of Sequences, ⁋Proposition 2](/en/math/calculus/sequences#prop2)) it converges to $$s_m$$. If all terms of a convergent sequence are at most $$L$$, then its limit is also at most $$L$$, so $$s_m \leq L$$, and sending $$m \to \infty$$ again gives $$s \leq L$$. Combining the two inequalities yields $$L = s$$, that is, the $$e$$ defined in the two posts is the same number.

</div>

## Operations on Power Series

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4**</ins> If $$f(x) = \sum a_n x^n$$ and $$g(x) = \sum b_n x^n$$ have radii of convergence $$R_f$$ and $$R_g$$ respectively, then for $$\lvert x\rvert < \min(R_f, R_g)$$ we have

$$f(x) + g(x) = \sum_{n=0}^\infty (a_n + b_n)x^n, \qquad f(x)g(x) = \sum_{n=0}^\infty \left(\sum_{k=0}^n a_k b_{n-k}\right) x^n$$

The coefficients of the product are the *Cauchy product* of the two coefficient sequences.

</div>

The Cauchy product extends to infinite degree the process of multiplying two polynomials and collecting terms of the same degree. For example, multiplying $$1/(1-x) = \sum_n x^n$$ by itself gives the $$n$$th coefficient as $$\sum_{k=0}^n 1\cdot 1 = n+1$$, yielding $$1/(1-x)^2 = \sum_n (n+1)x^n$$.

## Analytic Functions

<div class="definition" markdown="1">

<ins id="def5">**Definition 5**</ins> A function $$f$$ is said to be *analytic* at a point $$a$$ if it agrees with a power series centered at $$a$$ in some neighborhood of $$a$$. If $$f$$ is analytic at every point of its domain, we call $$f$$ an *analytic function*.

</div>

By [Definition 5](#def5), an analytic function coincides with its Taylor series. However, the converse is false. The function $$f(x) = e^{-1/x^2}$$ (with $$f(0) = 0$$) is smooth on all of $$\mathbb{R}$$, but all its derivatives at $$0$$ vanish, so its Taylor series is identically $$0$$; hence it does not agree with $$f$$ in any neighborhood of $$0$$, and $$f$$ is not analytic at $$0$$. Thus smoothness does not guarantee analyticity, and whether a Taylor series converges to the function can be determined by examining the remainder term in Taylor's theorem after learning differentiation.
