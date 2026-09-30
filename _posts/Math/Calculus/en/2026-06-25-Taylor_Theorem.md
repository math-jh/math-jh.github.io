---
title: "Taylor's Theorem"
description: "We define Taylor polynomials for approximating functions and prove Taylor's theorem with the Lagrange remainder using the Cauchy mean value theorem. We cover Maclaurin expansions of elementary functions, remainder estimation, and applications to limit and approximation calculations."
excerpt: "Taylor polynomials, Lagrange remainder, Maclaurin expansions, approximation and limits"

categories: [Math / Calculus]
permalink: /en/math/calculus/taylor_theorem
sidebar: 
    nav: "calculus-en"

date: 2026-06-25
weight: 9
translated_at: 2026-08-19T07:45:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-09-30T03:15:05+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
[§Differentiation and Derivatives](/en/math/calculus/derivatives){: data-lid="uf9ok" }, we saw that differentiating a function once yields its derivative, which gives the tangent line

$$f(x) \approx f(a) + f'(a)(x-a)$$

to the function. Viewed from another angle, this approximates a given function by a linear polynomial, and applying differentiation repeatedly can turn this into a more refined approximation.

## Taylor Polynomials

If a function $f$ at a point $a$ is $n$-times differentiable, we can construct, with the value at $a$ and the first $n$ derivative values identical to those of $f$, a polynomial of degree $n$.

::: Definition 1
When $f$ at a point $a$ is $n$-times differentiable, the *Taylor polynomial of $f$ at $a$ of degree $n$* is

$$P_n(x) = \sum_{k=0}^{n} \frac{f^{(k)}(a)}{k!}(x - a)^k = f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2 + \cdots + \frac{f^{(n)}(a)}{n!}(x-a)^n$$

In particular, the case where the center is $a = 0$ is called the *Maclaurin polynomial*.
:::

In practice, one can always shift any function to the origin, compute there, and then translate back, so taking $a=0$ as the definition causes no real difficulty.

## Taylor's Theorem

As claimed above, Taylor expansion is a method of approximating a given function by an $n$-th degree polynomial. Consider the following graph.

{% diagram Math/Calculus/Taylor_Theorem-1.svg width="23.68em" alt="The sine function and its Taylor polynomial approximations" %}

This graph shows the first few Taylor expansions of the sine function, and from the figure we can see that the approximation indeed approaches the $\sin$ function. However, to prove mathematically that this actually reduces the error, we need the following theorem.

::: Theorem 2 (Taylor's theorem, Lagrange remainder)
If $f$, on an interval containing $a$ and $x$, is $n+1$ times differentiable, then between $a$ and $x$, for some $c$,

$$f(x) = \sum_{k=0}^{n} \frac{f^{(k)}(a)}{k!}(x-a)^k + R_n(x), \qquad R_n(x) = \frac{f^{(n+1)}(c)}{(n+1)!}(x - a)^{n+1}$$

holds.
:::

::: Proof
Fix $x \neq a$, and between $a$ and $x$, for a variable $t$, define two auxiliary functions

$$g(t) = f(x) - \sum_{k=0}^{n}\frac{f^{(k)}(t)}{k!}(x-t)^k, \qquad h(t) = (x - t)^{n+1}$$

The endpoint values are $g(x) = 0$, $g(a) = f(x) - P_n(x) = R_n(x)$, and $h(x) = 0$, $h(a) = (x-a)^{n+1}$. Differentiating $g$, adjacent terms cancel and only

$$g'(t) = -\frac{f^{(n+1)}(t)}{n!}(x - t)^n$$

remains, while $h'(t) = -(n+1)(x-t)^n$. Applying [§Mean Value Theorem, ⁋Theorem 6](/en/math/calculus/mean_value_theorem#thm6){: data-lid="j4wzu" } between $a$ and $x$,

$$\bigl(g(x) - g(a)\bigr)h'(c) = \bigl(h(x) - h(a)\bigr)g'(c)$$

holds for some $c$. Substituting the values gives

$$(-R_n(x))\bigl(-(n+1)(x-c)^n\bigr) = \bigl(-(x-a)^{n+1}\bigr)\left(-\frac{f^{(n+1)}(c)}{n!}(x-c)^n\right)$$

and canceling $(x-c)^n$ from both sides and simplifying yields $R_n(x) = f^{(n+1)}(c)(x-a)^{n+1}/(n+1)!$.
:::

Therefore, if we now compute the remainder term in the above theorem and show that as $n \rightarrow \infty$, $R_n(x) \rightarrow 0$, we know that the function coincides with the infinite series. The infinite series obtained in this way is called the *Taylor series* of $f$ (or the Maclaurin series if the center is $0$).

Let us follow through these calculations in a few concrete examples.

::: Example 3
Since any derivative of $f(x) = e^x$ is itself, as verified in [§Differentiation](/en/math/calculus/differentiation_rules){: data-lid="0zmhp" }, for any $k$ we have $f^{(k)}(0) = 1$. Therefore, the Taylor polynomial is

$$P_n(x) = \sum_{k=0}^n \frac{x^k}{k!}$$

Between $0$ and $x$, for some $c$, the remainder is given by

$$R_n(x) = \frac{e^c x^{n+1}}{(n+1)!}$$

and since for fixed $x$,

$$\lvert R_n(x)\rvert \leq \frac{e^{\lvert x\rvert}\lvert x\rvert^{n+1}}{(n+1)!} \rightarrow 0 \qquad (n \rightarrow \infty)$$

([§Limits of Sequences, ⁋Example 6](/en/math/calculus/sequences#ex6){: data-lid="4l0s1" }), for all real $x$

$$e^x = \sum_{k=0}^{\infty}\frac{x^k}{k!}$$

holds. In particular, if $x = 1$, then $e = \sum_{k=0}^\infty 1/k!$.
:::

Similarly, for the trigonometric functions that we know, the following holds.

::: Example 4 (Trigonometric functions)
For $\sin x$, the derivatives are periodic: $\cos x, -\sin x, -\cos x, \sin x$, so $f^{(k)}(0)$ repeats $0, 1, 0, -1$. Since all derivatives are bounded by $\lvert f^{(n+1)}\rvert \leq 1$, by the same argument as in [Example 3](#ex3){: data-lid="i8ddn" } above we can show that the remainder goes to $0$, and thus for all $x$,

$$\sin x = \sum_{k=0}^\infty \frac{(-1)^k x^{2k+1}}{(2k+1)!}, \qquad \cos x = \sum_{k=0}^\infty \frac{(-1)^k x^{2k}}{(2k)!}$$
:::

The following is an example where the radius of convergence is not infinite.

::: Example 5 (Logarithmic function)
For $\ln(1+x)$, since $f^{(k)}(0) = (-1)^{k-1}(k-1)!$, we have

$$\ln(1+x) = \sum_{k=1}^\infty \frac{(-1)^{k-1}}{k} x^k \qquad (-1 < x \leq 1)$$

and differentiating this yields the infinite series formula

$$\frac{1}{1+x}=\sum_{k=0}^\infty (-1)^{k}x^k \qquad (\lvert x\rvert < 1)$$

([§Differentiation, ⁋Proposition 1](/en/math/calculus/differentiation_rules#prop1){: data-lid="bvyms" }). More generally, for the following generalized binomial series defined for a real $\alpha$:

$$(1+x)^\alpha = \sum_{k=0}^\infty \binom{\alpha}{k} x^k, \qquad \binom{\alpha}{k} = \frac{\alpha(\alpha-1)\cdots(\alpha-k+1)}{k!} \qquad (\lvert x\rvert < 1)$$

this is the case $\alpha = -1$. As another example, $\alpha = 1/2$ gives

$$\sqrt{1+x} = 1 + \frac{x}{2} - \frac{x^2}{8} + \cdots$$
:::

As in [Example 4](#ex4){: data-lid="7jlla" } above, when all derivatives are simultaneously bounded by a single constant, the Taylor series is equal to the function itself. Formally written, this is as follows.

::: Proposition 6
If $f$ is infinitely differentiable on an interval containing $a$, say $I$, and for some constant $M$, for all $n$ and all $x \in I$, $\lvert f^{(n)}(x)\rvert \leq M$, then $f$ coincides with its Taylor series on $I$.
:::

::: Proof
The remainder in Taylor's theorem is

$$\lvert R_n(x)\rvert = \frac{\lvert f^{(n+1)}(c)\rvert}{(n+1)!}\lvert x-a\rvert^{n+1} \leq \frac{M\lvert x-a\rvert^{n+1}}{(n+1)!}$$

For fixed $x$, as $n \rightarrow \infty$ the right-hand side goes to $0$ ([§Limits of Sequences, ⁋Example 6](/en/math/calculus/sequences#ex6){: data-lid="zmb5i" }, $r^n/n! \rightarrow 0$), so $R_n(x) \rightarrow 0$ and the partial sums converge to $f(x)$.
:::

Meanwhile, [Theorem 2](#thm2){: data-lid="12v03" } is essentially numerical, and using it, we can evaluate by hand how accurate an approximation is. For instance, if we approximate $\sin(0.1)$ by $P_3(x) = x - x^3/6$, the fourth-order remainder is $\lvert R_3(0.1)\rvert \leq (0.1)^4/4! \approx 4.2\times 10^{-6}$, so we can verify that it is accurate to five decimal places; and the error in truncating $e = \sum_k 1/k!$ after the first $n+1$ terms is $\lvert R_n(1)\rvert \leq 3/(n+1)!$ ($e^c < 3$).

As another example, since Taylor expansion does not merely retain the highest-degree or lowest-degree term, it can be used powerfully in computing limits of the form $0/0$.

::: Example 7 (Limit)
Let us find the limit $\lim_{x\rightarrow 0}(e^x - 1 - x)/x^2$. From [Example 3](#ex3){: data-lid="l8bo0" }, $e^x = 1 + x + x^2/2 + x^3/6 + \cdots$, so

$$\frac{e^x - 1 - x}{x^2} = \frac{x^2/2 + x^3/6 + \cdots}{x^2} = \frac{1}{2} + \frac{x}{6} + \cdots \rightarrow \frac{1}{2}$$

This is a result that can also be confirmed by applying [§Mean Value Theorem, ⁋Theorem 18](/en/math/calculus/mean_value_theorem#thm18){: data-lid="o1adk" } twice; because the Taylor expansion retains information up to higher-order terms, information still remains even after canceling from both the denominator and numerator.
:::

---

**References**

**[Ste]** J. Stewart, *Calculus*, 8th ed., Cengage Learning, 2016.  
**[Kim]** 김홍종, *미적분학 1·2*, 제3개정판, 서울대학교출판문화원, 2020.
