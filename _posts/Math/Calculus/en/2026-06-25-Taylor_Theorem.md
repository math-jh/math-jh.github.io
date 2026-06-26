---
title: "Taylor's Theorem"
description: "This post defines Taylor polynomials for approximating functions, proves Taylor's theorem with the Lagrange remainder via Cauchy's mean value theorem, and covers Maclaurin expansions of elementary functions, remainder estimation, and applications to limit and approximation calculations."
excerpt: "Taylor polynomials, Lagrange remainder, Maclaurin series, approximation and limits"

categories: [Math / Calculus]
permalink: /en/math/calculus/taylor_theorem
sidebar: 
    nav: "calculus-en"

date: 2026-06-25
weight: 9
translated_at: 2026-06-24T19:00:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-24T19:00:02+00:00
---
In [§Derivatives](/en/math/calculus/derivatives), we verified that differentiating a function once yields the derivative that gives the tangent line

$$f(x) \approx f(a) + f'(a)(x-a)$$

Viewed from another angle, this approximates a given function by a linear polynomial, and repeated differentiation lets us refine this into a more accurate approximation.

## Taylor Polynomials

If a function $$f$$ is $$n$$-times differentiable at a point $$a$$, we can construct a polynomial of degree $$n$$ whose value and first $$n$$ derivatives at $$a$$ agree with those of $$f$$.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> When $$f$$ is $$n$$-times differentiable at a point $$a$$, the *$$n$$th-degree Taylor polynomial* of $$f$$ at $$a$$ is

$$P_n(x) = \sum_{k=0}^{n} \frac{f^{(k)}(a)}{k!}(x - a)^k = f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2 + \cdots + \frac{f^{(n)}(a)}{n!}(x-a)^n$$

The special case with center $$a = 0$$ is called the *Maclaurin polynomial*.

</div>

In practice, since we can always shift any function to the origin, compute there, and then translate back, treating the $$a=0$$ case as the definition causes no real problem.

## Taylor's Theorem

As claimed above, Taylor expansion is a method of approximating a given function by an $$n$$th-degree polynomial. Consider the following graph.

![sin function and its Taylor polynomial approximations](/assets/images/Math/Calculus/Taylor_Theorem-1.svg){:style="width:23.68em" class="invert" .align-center}

This graph shows the first few Taylor expansions of the sine function, and from the picture we can see that the approximation indeed gets closer to the $$\sin$$ function. However, to prove mathematically that this actually reduces the error, we need the following theorem.

<div class="proposition" markdown="1">

<ins id="thm2">**Theorem 2 (Taylor's Theorem, Lagrange Remainder)**</ins> If $$f$$ is $$(n+1)$$-times differentiable on an interval containing $$a$$ and $$x$$, then for some $$c$$ between $$a$$ and $$x$$,

$$f(x) = \sum_{k=0}^{n} \frac{f^{(k)}(a)}{k!}(x-a)^k + R_n(x), \qquad R_n(x) = \frac{f^{(n+1)}(c)}{(n+1)!}(x - a)^{n+1}$$

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

Fix $$x \neq a$$, and for a variable $$t$$ between $$a$$ and $$x$$ define two auxiliary functions

$$g(t) = f(x) - \sum_{k=0}^{n}\frac{f^{(k)}(t)}{k!}(x-t)^k, \qquad h(t) = (x - t)^{n+1}$$

The endpoint values are $$g(x) = 0$$, $$g(a) = f(x) - P_n(x) = R_n(x)$$, and $$h(x) = 0$$, $$h(a) = (x-a)^{n+1}$$. Differentiating $$g$$ causes adjacent terms to cancel, leaving only

$$g'(t) = -\frac{f^{(n+1)}(t)}{n!}(x - t)^n$$

and $$h'(t) = -(n+1)(x-t)^n$$. Applying [§Mean Value Theorem, ⁋Theorem 6](/en/math/calculus/mean_value_theorem#thm6) between $$a$$ and $$x$$, there exists a $$c$$ such that

$$\bigl(g(x) - g(a)\bigr)h'(c) = \bigl(h(x) - h(a)\bigr)g'(c)$$

Substituting the values gives

$$(-R_n(x))\bigl(-(n+1)(x-c)^n\bigr) = \bigl(-(x-a)^{n+1}\bigr)\left(-\frac{f^{(n+1)}(c)}{n!}(x-c)^n\right)$$

and canceling $$(x-c)^n$$ from both sides and rearranging yields $$R_n(x) = f^{(n+1)}(c)(x-a)^{n+1}/(n+1)!$$.

</details>

Therefore, if we now compute the remainder term in the above theorem and show that $$R_n(x) \to 0$$ as $$n \to \infty$$, we know that the function agrees with the infinite series. The infinite series obtained in this way is called the *Taylor series* of $$f$$ (if the center is $$0$$, it is called the Maclaurin series).

Let us follow through these calculations in a few concrete examples.

<div class="example" markdown="1">

<ins id="ex3">**Example 3**</ins> Since we have verified that every derivative of $$f(x) = e^x$$ is itself, we have $$f^{(k)}(0) = 1$$ for every $$k$$. Thus the Taylor polynomial is

$$P_n(x) = \sum_{k=0}^n \frac{x^k}{k!}$$

The remainder is given, for some $$c$$ between $$0$$ and $$x$$, by

$$R_n(x) = \frac{e^c x^{n+1}}{(n+1)!}$$

and for fixed $$x$$,

$$\lvert R_n(x)\rvert \leq \frac{e^{\lvert x\rvert}\lvert x\rvert^{n+1}}{(n+1)!} \to 0 \qquad (n \to \infty)$$

so ([§Limits of Sequences, ⁋Example 6](/en/math/calculus/sequences#ex6)) for every real number $$x$$,

$$e^x = \sum_{k=0}^{\infty}\frac{x^k}{k!}$$

holds. In particular, for $$x = 1$$ we have $$e = \sum_{k=0}^\infty 1/k!$$.

</div>

Similarly, for the trigonometric functions we already know, the following holds.

<div class="example" markdown="1">

<ins id="ex4">**Example 4 (Trigonometric Functions)**</ins> Since the derivatives of $$\sin x$$ are periodic: $$\cos x, -\sin x, -\cos x, \sin x$$, the values $$f^{(k)}(0)$$ repeat $$0, 1, 0, -1$$. Since all derivatives are bounded by $$\lvert f^{(n+1)}\rvert \leq 1$$, we can show by the same argument as in [Example 3](#ex3) that the remainder goes to $$0$$, and therefore for every $$x$$,

$$\sin x = \sum_{k=0}^\infty \frac{(-1)^k x^{2k+1}}{(2k+1)!}, \qquad \cos x = \sum_{k=0}^\infty \frac{(-1)^k x^{2k}}{(2k)!}$$

</div>

The next is an example where the radius of convergence is not infinite.

<div class="example" markdown="1">

<ins id="ex5">**Example 5 (Logarithm)**</ins> For $$\ln(1+x)$$ we have $$f^{(k)}(0) = (-1)^{k-1}(k-1)!$$, so

$$\ln(1+x) = \sum_{k=1}^\infty \frac{(-1)^{k-1}}{k} x^k \qquad (-1 < x \leq 1)$$

and differentiating this gives the infinite series expression

$$\frac{1}{1+x}=\sum_{k=0}^\infty (-1)^{k}x^k$$

More generally, this is the case $$\alpha = -1$$ of the generalized binomial series defined for a real number $$\alpha$$ by

$$(1+x)^\alpha = \sum_{k=0}^\infty \binom{\alpha}{k} x^k, \qquad \binom{\alpha}{k} = \frac{\alpha(\alpha-1)\cdots(\alpha-k+1)}{k!} \qquad (\lvert x\rvert < 1)$$

As another example, $$\alpha = 1/2$$ gives

$$\sqrt{1+x} = 1 + \frac{x}{2} - \frac{x^2}{8} + \cdots$$

</div>

The examples above show in particular that when the derivatives are bounded, the Taylor series of a function equals the function itself. Formally stated, this is as follows.

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6**</ins> If $$f$$ is infinitely differentiable on an interval $$I$$ containing $$a$$, and there exists a constant $$M$$ such that $$\lvert f^{(n)}(x)\rvert \leq M$$ for all $$n$$ and all $$x \in I$$, then $$f$$ agrees with its Taylor series on $$I$$.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

The remainder from Taylor's theorem satisfies

$$\lvert R_n(x)\rvert = \frac{\lvert f^{(n+1)}(c)\rvert}{(n+1)!}\lvert x-a\rvert^{n+1} \leq \frac{M \lvert x-a\rvert^{n+1}}{(n+1)!}$$

The right-hand side goes to $$0$$ as $$n \to \infty$$ for fixed $$x$$ ([§Limits of Sequences, ⁋Example 6](/en/math/calculus/sequences#ex6), $$r^n/n! \to 0$$), so $$R_n(x) \to 0$$ and the partial sums converge to $$f(x)$$.

</details>

Meanwhile, [Theorem 2](#thm2) is essentially numerical: using it, we can evaluate by hand how accurate an approximation is. For instance, if we approximate $$\sin(0.1)$$ by $$P_3(x) = x - x^3/6$$, the fourth-degree remainder is $$\lvert R_3(0.1)\rvert \leq (0.1)^4/4! \approx 4.2\times 10^{-6}$$, so we can verify that it is accurate to five decimal places, and the error in truncating $$e = \sum_k 1/k!$$ after the first $$n+1$$ terms is $$\lvert R_n(1)\rvert \leq 3/(n+1)!$$ (since $$e^c < 3$$).

As another example, since Taylor expansion is not merely remembering the highest-degree or lowest-degree term, it can be used powerfully when computing limits of the form $$0/0$$.

<div class="example" markdown="1">

<ins id="ex7">**Example 7 (Limit)**</ins> Let us find the limit $$\lim_{x\to 0}(e^x - 1 - x)/x^2$$. From [Example 3](#ex3), we have $$e^x = 1 + x + x^2/2 + x^3/6 + \cdots$$, so

$$\frac{e^x - 1 - x}{x^2} = \frac{x^2/2 + x^3/6 + \cdots}{x^2} = \frac12 + \frac{x}{6} + \cdots \to \frac12$$

This is a result that can also be verified by applying l'Hôpital's rule twice; the reason Taylor expansion works is that it retains information about higher-order terms, so even after canceling the denominator with the numerator, information still remains.

</div>
