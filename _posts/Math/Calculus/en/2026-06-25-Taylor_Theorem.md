---
title: "Taylor's Theorem"
description: "We define Taylor polynomials for approximating functions and prove Taylor's theorem with Lagrange remainder using the Cauchy mean value theorem. We also cover Maclaurin expansions of elementary functions, remainder estimation, and applications to limit and approximation calculations."
excerpt: "Taylor polynomials, Lagrange remainder, Maclaurin series, approximation and limits"

categories: [Math / Calculus]
permalink: /en/math/calculus/taylor_theorem
sidebar: 
    nav: "calculus-en"

date: 2026-06-25
weight: 9
translated_at: 2026-08-17T20:15:05+00:00
translation_source: kimi-cli
---
In [§Differentiation and Derivatives](/en/math/calculus/derivatives), we saw that differentiating a function once gives its derivative, which yields the tangent line

$$f(x) \approx f(a) + f'(a)(x-a)$$

to the function. Viewed differently, this approximates a given function by a linear polynomial, and applying differentiation repeatedly yields a more refined approximation.

## Taylor Polynomials

If a function $f$ is $n$-times differentiable at a point $a$, we can construct a degree-$n$ polynomial whose value at $a$ and first $n$ derivatives agree with those of $f$.

::: Definition 1
When $f$ is $n$-times differentiable at $a$, the *Taylor polynomial* of degree $n$ for $f$ at $a$ is

$$P_n(x) = \sum_{k=0}^{n} \frac{f^{(k)}(a)}{k!}(x - a)^k = f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2 + \cdots + \frac{f^{(n)}(a)}{n!}(x-a)^n.$$

In the special case where the center is $a = 0$, it is called the *Maclaurin polynomial*.
:::

In practice, one can always shift every function to the origin, compute there, and then translate back, so taking $a=0$ as the definition causes no real problem.

## Taylor's Theorem

As claimed above, Taylor expansion is a way of approximating a given function by an $n$-th degree polynomial. Consider the following graph.

{% diagram Math/Calculus/Taylor_Theorem-1.svg width="23.68em" alt="The sine function and its Taylor polynomial approximations" %}

This graph shows the first few Taylor expansions of the sine function, and from the figure we can see that the approximation indeed gets closer to the $\sin$ function. However, to prove mathematically that this actually reduces the error, we need the following theorem.

::: Theorem 2 (Taylor's theorem, Lagrange remainder)
If $f$ is $(n+1)$-times differentiable on an interval containing $a$ and $x$, then for some $c$ between $a$ and $x$,

$$f(x) = \sum_{k=0}^{n} \frac{f^{(k)}(a)}{k!}(x-a)^k + R_n(x), \qquad R_n(x) = \frac{f^{(n+1)}(c)}{(n+1)!}(x - a)^{n+1}$$

holds.
:::

::: Proof
Fix $x \neq a$ and define two auxiliary functions of a variable $t$ between $a$ and $x$:

$$g(t) = f(x) - \sum_{k=0}^{n}\frac{f^{(k)}(t)}{k!}(x-t)^k, \qquad h(t) = (x - t)^{n+1}.$$

The endpoint values are $g(x) = 0$, $g(a) = f(x) - P_n(x) = R_n(x)$, and $h(x) = 0$, $h(a) = (x-a)^{n+1}$. Differentiating $g$, adjacent terms cancel and only

$$g'(t) = -\frac{f^{(n+1)}(t)}{n!}(x - t)^n$$

remains, while $h'(t) = -(n+1)(x-t)^n$. Applying [§Mean Value Theorem, ⁋Theorem 6](/en/math/calculus/mean_value_theorem#thm6) between $a$ and $x$, there exists $c$ such that

$$\bigl(g(x) - g(a)\bigr)h'(c) = \bigl(h(x) - h(a)\bigr)g'(c).$$

Substituting the values gives

$$(-R_n(x))\bigl(-(n+1)(x-c)^n\bigr) = \bigl(-(x-a)^{n+1}\bigr)\left(-\frac{f^{(n+1)}(c)}{n!}(x-c)^n\right),$$

and canceling $(x-c)^n$ from both sides yields $R_n(x) = f^{(n+1)}(c)(x-a)^{n+1}/(n+1)!$.
:::

Therefore, if we now compute the remainder term in the above theorem and show that $R_n(x) \rightarrow 0$ as $n \rightarrow \infty$, we know that the function coincides with the infinite series. The infinite series obtained in this way is called the *Taylor series* of $f$ (if the center is $0$, the Maclaurin series).

Let us follow through these calculations in a few concrete examples.

::: Example 3
Since any derivative of $f(x) = e^x$ is itself, as verified in [§Differentiation](/en/math/calculus/differentiation_rules), we have $f^{(k)}(0) = 1$ for every $k$. Hence the Taylor polynomial is

$$P_n(x) = \sum_{k=0}^n \frac{x^k}{k!}.$$

The remainder is given, for some $c$ between $0$ and $x$, by

$$R_n(x) = \frac{e^c x^{n+1}}{(n+1)!},$$

and for fixed $x$,

$$\lvert R_n(x)\rvert \leq \frac{e^{\lvert x\rvert}\lvert x\rvert^{n+1}}{(n+1)!} \rightarrow 0 \qquad (n \rightarrow \infty)$$

([§Limits of Sequences, ⁋Example 6](/en/math/calculus/sequences#ex6)), so

$$e^x = \sum_{k=0}^{\infty}\frac{x^k}{k!}$$

holds for all real $x$. In particular, for $x = 1$ we get $e = \sum_{k=0}^\infty 1/k!$.
:::

Similarly, for the trigonometric functions we know, the following holds.

::: Example 4 (Trigonometric functions)
Since the derivatives of $\sin x$ are periodic: $\cos x, -\sin x, -\cos x, \sin x$, the values $f^{(k)}(0)$ repeat $0, 1, 0, -1$. All derivatives are bounded by $\lvert f^{(n+1)}\rvert \leq 1$, so by the same argument as in [Example 3](#ex3) the remainder goes to $0$, and thus for all $x$,

$$\sin x = \sum_{k=0}^\infty \frac{(-1)^k x^{2k+1}}{(2k+1)!}, \qquad \cos x = \sum_{k=0}^\infty \frac{(-1)^k x^{2k}}{(2k)!}.$$
:::

The next is an example where the radius of convergence is not infinite.

::: Example 5 (Logarithm)
For $\ln(1+x)$ we have $f^{(k)}(0) = (-1)^{k-1}(k-1)!$, so

$$\ln(1+x) = \sum_{k=1}^\infty \frac{(-1)^{k-1}}{k} x^k \qquad (-1 < x \leq 1),$$

and differentiating this gives the infinite series identity

$$\frac{1}{1+x}=\sum_{k=0}^\infty (-1)^{k}x^k \qquad (\lvert x\rvert < 1).$$

([§Differentiation, ⁋Proposition 1](/en/math/calculus/differentiation_rules#prop1)) This is the case $\alpha = -1$ of the more general binomial series defined for real $\alpha$:

$$(1+x)^\alpha = \sum_{k=0}^\infty \binom{\alpha}{k} x^k, \qquad \binom{\alpha}{k} = \frac{\alpha(\alpha-1)\cdots(\alpha-k+1)}{k!} \qquad (\lvert x\rvert < 1).$$

As another example, $\alpha = 1/2$ gives

$$\sqrt{1+x} = 1 + \frac{x}{2} - \frac{x^2}{8} + \cdots.$$
:::

As in [Example 4](#ex4) above, if all derivatives are simultaneously bounded by a single constant, then the Taylor series equals the function itself. Writing this formally gives the following.

::: Proposition 6
If $f$ is infinitely differentiable on an interval $I$ containing $a$, and there exists a constant $M$ such that $\lvert f^{(n)}(x)\rvert \leq M$ for all $n$ and all $x \in I$, then $f$ coincides with its Taylor series on $I$.
:::

::: Proof
The remainder in Taylor's theorem satisfies

$$\lvert R_n(x)\rvert = \frac{\lvert f^{(n+1)}(c)\rvert}{(n+1)!}\lvert x-a\rvert^{n+1} \leq \frac{M\lvert x-a\rvert^{n+1}}{(n+1)!}.$$

For fixed $x$, the right-hand side goes to $0$ as $n \rightarrow \infty$ ([§Limits of Sequences, ⁋Example 6](/en/math/calculus/sequences#ex6), $r^n/n! \rightarrow 0$), so $R_n(x) \rightarrow 0$ and the partial sums converge to $f(x)$.
:::

Meanwhile, [Theorem 2](#thm2) is essentially numerical: using it, we can by hand assess how accurate an approximation is. For instance, approximating $\sin(0.1)$ by $P_3(x) = x - x^3/6$, the fourth-degree remainder is $\lvert R_3(0.1)\rvert \leq (0.1)^4/4! \approx 4.2\times 10^{-6}$, so we can verify accuracy to five decimal places; and the error in truncating $e = \sum_k 1/k!$ after the first $n+1$ terms is $\lvert R_n(1)\rvert \leq 3/(n+1)!$ (since $e^c < 3$).

As another example, since Taylor expansion remembers not just the highest or lowest degree term, it can be used powerfully in computing limits of $0/0$ form.

::: Example 7 (Limit)
Let us find the limit $\lim_{x\rightarrow 0}(e^x - 1 - x)/x^2$. From [Example 3](#ex3), $e^x = 1 + x + x^2/2 + x^3/6 + \cdots$, so

$$\frac{e^x - 1 - x}{x^2} = \frac{x^2/2 + x^3/6 + \cdots}{x^2} = \frac12 + \frac{x}{6} + \cdots \rightarrow \frac12.$$

This is a result that can also be checked by applying [§Mean Value Theorem, ⁋Theorem 18](/en/math/calculus/mean_value_theorem#thm18) twice, and the reason Taylor expansion succeeds is that it retains information from higher-degree terms, so after canceling with the denominator and numerator, information still remains.
:::

---

**References**

**[Ste]** J. Stewart, *Calculus*, 8th ed., Cengage Learning, 2016.  
**[Kim]** 김홍종, *미적분학 1·2*, 제3개정판, 서울대학교출판문화원, 2020.
