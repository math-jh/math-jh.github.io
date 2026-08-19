---
title: "The Fundamental Theorem of Calculus"
description: "This post proves the fundamental theorem of calculus in two forms, showing that differentiation and integration are inverse operations. It also covers how definite integrals can be evaluated using antiderivatives, along with applications and termwise integration of power series."
excerpt: "Fundamental theorem, existence of primitives, Leibniz rule, termwise integration of power series"

categories: [Math / Calculus]
permalink: /en/math/calculus/fundamental_theorem_of_calculus
sidebar: 
    nav: "calculus-en"

date: 2026-06-26
weight: 11
translated_at: 2026-08-19T08:15:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-08-19T08:15:04+00:00
---
In a previous post we defined two different kinds of integrals: the indefinite integral and the definite integral. The indefinite integral derives its meaning from being the inverse process of differentiation, while the definite integral carries an intrinsic geometric meaning as the area under a curve. The fundamental theorem of calculus shows that these two are, in a certain sense, entirely the same process; indeed, one could say that calculus itself was born from this observation.

## The Fundamental Theorem of Calculus

Since the indefinite integral is defined from the outset as the inverse of differentiation, the meaningful question in this context is whether the definite integral actually yields something similar to an inverse of differentiation. However, because the definite integral ultimately produces a numerical value, its output is not a function. To address this, we let the upper limit of the definite integral be a variable and consider the function

$$\int_a^x f(t)\dd{t}.$$

Here $t$ is merely a dummy variable, introduced to avoid confusion with $x$ which already appears in the upper limit; if there is no risk of confusion, one may just as well write $x$ in place of $t$.

::: Theorem 1 (Fundamental theorem of calculus)
If $f$ is continuous on $[a,b]$ and we define $F(x)=\int_a^x f(t)\dd{t}$, then $F$ is differentiable on $[a,b]$ and at every $x$ we have

$$F'(x)=f(x).$$

Here differentiability at the endpoints $a,b$ means the right-hand and left-hand derivatives of [§Differentiation and Derivatives, ⁋Definition 6](/en/math/calculus/derivatives#def6).
:::

::: Proof
By the second part of [§Integration, ⁋Proposition 11](/en/math/calculus/integration#prop11), for $h>0$ we have

$$F(x+h)-F(x)=\int_a^{x+h}f-\int_a^x f=\int_x^{x+h}f(t)\dd{t}.$$

Since $f$ is continuous on $[x,x+h]$, by [§Continuous Functions, ⁋Theorem 4](/en/math/calculus/continuity#thm4) it attains a minimum $m_h$ and a maximum $M_h$ on that interval, and by the third part of [§Integration, ⁋Proposition 11](/en/math/calculus/integration#prop11) we have

$$m_h\le \frac{F(x+h)-F(x)}{h}\le M_h.$$

Now as $h\to 0$ the interval $[x,x+h]$ shrinks to the single point $x$, and by continuity of $f$ we have $m_h,M_h\to f(x)$; hence by [§Limits of Functions, ⁋Proposition 8](/en/math/calculus/functions_and_limits#prop8) the average rate of change converges to $f(x)$. The case $h<0$ can be handled in a similar manner.
:::

This theorem is a rigorous expression of the intuition that *the rate at which area accumulates is precisely the height*. In other words, the rate $F'(x)$ at which the function $F(x)$ defined by integration increases at a point is exactly the value $f(x)$ of the integrand at that point.

::: Corollary 2
Every function continuous on $[a,b]$ has a primitive. Specifically, $F(x)=\int_a^x f(t)\dd{t}$ is one such primitive.
:::

The function $F(x)$ defined above fixes the integration constant $C$ to a single value; concretely, one may think of it as choosing the constant so that $F(a)=0$.

On the other hand, the above corollary is a different matter from the statement that the integral of an arbitrary function can be expressed in terms of elementary functions. It asserts only that $\int_a^x f(t)\dd{t}$ defined by the above formula is *in itself* a primitive of $f$. Consider the following example.

::: Example 3 (Derivative of a special function)
The *error function* is defined by

$$\erf(x)=\frac{2}{\sqrt{\pi}}\int_0^x e^{-t^2}\dd{t}.$$

The primitive of $e^{-t^2}$ cannot be written as an elementary function, so this integral has no closed form; however, by [Theorem 1](#thm1) the function $\erf$ is differentiable and

$$\erf'(x)=\frac{2}{\sqrt{\pi}}e^{-x^2}.$$

Likewise, the *logarithmic integral* $\mathrm{Li}(x)=\int_2^x \dd{t}/\ln t$ has derivative $\mathrm{Li}'(x)=1/\ln x$ immediately for $x>1$. In this way, a function defined by an integral becomes an object of calculus in its own right.
:::

A slightly more advanced version of this statement will be introduced again after we examine term-by-term integration of power series in [Proposition 7](#prop7).

Meanwhile, combining [Theorem 1](#thm1) with the fact that a function whose derivative is $0$ must be constant yields a powerful tool for computing definite integrals as differences of primitives.

::: Theorem 4
If $f$ is continuous on $[a,b]$ and $G$ is any primitive of $f$, then

$$\int_a^b f(x)\dd{x}=G(b)-G(a).$$
:::

::: Proof
Let $F(x)=\int_a^x f$. By [Theorem 1](#thm1), $F$ is also a primitive of $f$. Any two primitives differ by a constant, so (by [§Mean Value Theorem, ⁋Corollary 5](/en/math/calculus/mean_value_theorem#cor5)) there exists a constant $C$ such that $F=G+C$. Since $F(a)=\int_a^a f=0$, we have $C=-G(a)$, and therefore

$$\int_a^b f=F(b)=G(b)+C=G(b)-G(a).$$
:::

One commonly writes $G(b)-G(a)$ as $\bigl[G(x)\bigr]_a^b$. Thanks to this theorem, the computation of a definite integral is reduced to the problem of finding a primitive rather than taking a limit of Riemann sums. For instance, $\int_0^1 x^2\dd{x}=\bigl[x^3/3\bigr]_0^1=1/3$ agrees with the value obtained laboriously via Riemann sums in [§Integration](/en/math/calculus/integration), but here it is obtained by an entirely different calculation, namely substituting the endpoints into the primitive.

In particular, [Theorem 1](#thm1) combines with [§Differentiation, ⁋Theorem 4](/en/math/calculus/differentiation_rules#thm4) when the upper and lower limits of integration depend on a variable. If the upper limit is a function $g(x)$, then letting $F(u)=\int_a^u f$ we have $\int_a^{g(x)} f=F(g(x))$, and since $F'(u)=f(u)$ the chain rule gives $\frac{d}{\dd{x}}\int_a^{g(x)} f(t)\dd{t}=f(g(x))g'(x)$. If both limits are variable, one splits the interval into two parts and applies the rule to each side.

::: Proposition 5 (Leibniz rule)
If $f$ is continuous on an interval $I$, and $g,h$ are differentiable with values in $I$, then

$$\frac{d}{\dd{x}}\int_{h(x)}^{g(x)} f(t)\dd{t}=f(g(x))g'(x)-f(h(x))h'(x).$$
:::

::: Proof
Pick a point $c$ in $I$ and split the integral into two parts using the additivity over intervals from [§Integration, ⁋Proposition 11](/en/math/calculus/integration#prop11):

$$\int_{h(x)}^{g(x)} f(t)\dd{t}=\int_c^{g(x)} f(t)\dd{t}-\int_c^{h(x)} f(t)\dd{t}.$$

Letting $F(u)=\int_c^u f(v)\dd{v}$, we have $F'(u)=f(u)$ by [Theorem 1](#thm1), and the right-hand side is $F(g(x))-F(h(x))$. Applying the chain rule to each term gives

$$\begin{aligned}
\frac{d}{\dd{x}}\bigl[F(g(x))-F(h(x))\bigr] &= F'(g(x))g'(x)-F'(h(x))h'(x) \\[2pt]
&= f(g(x))g'(x)-f(h(x))h'(x).
\end{aligned}$$
:::

However, one must be careful when the integrand is not defined or is discontinuous on the interval of integration. Consider the following example.

::: Example 6
For the integral

$$\int_{-1}^{1} \frac{\dd{x}}{x^2}$$

a formal substitution of

$$\bigl[-x^{-1}\bigr]_{-1}^{1}=-1-1=-2$$

yields a negative number, but the integrand $1/x^2$ is always positive, so this is clearly a wrong calculation. The reason it fails is that the integrand diverges at $x=0$ and is therefore not continuous on $[-1,1]$. Since the hypothesis of [Theorem 4](#thm4) is violated, one cannot apply the theorem as is; in fact, this integral diverges.
:::

## Term-by-Term Integration of Power Series

On the other hand, integration also goes hand in hand with power series. The following proposition likewise requires knowledge of analysis for its proof, so we shall accept it as fact for now.

::: Proposition 7 (Term-by-term integration of power series)
If $f(x)=\sum_{n=0}^\infty c_n x^n$ has radius of convergence $R>0$, then for $\lvert x\rvert<R$

$$\int_0^x f(t)\dd{t}=\sum_{n=0}^\infty \frac{c_n}{n+1}x^{n+1},$$

and this series also has radius of convergence $R$.
:::

Then we can see in what form the function $e^{-x^2}$ examined in [Example 3](#ex3) can be written.

::: Example 8
Returning to the error function of [Example 3](#ex3). From the power series of the exponential function,

$$e^{-t^2}=\sum_{n=0}^\infty \frac{(-1)^n}{n!}t^{2n},$$

whose radius of convergence is $\infty$. Now term-by-term integration via [Proposition 7](#prop7) gives

$$\int_0^x e^{-t^2}\dd{t}=\sum_{n=0}^\infty \frac{(-1)^n}{n!(2n+1)}x^{2n+1},$$

and therefore

$$\erf(x)=\frac{2}{\sqrt{\pi}}\sum_{n=0}^\infty \frac{(-1)^n}{n!(2n+1)}x^{2n+1}.$$

That is, although the primitive still cannot be written as an elementary function, it can be expressed explicitly as a power series in this way.

By a similar method, term-by-term integration of $1/(1+x^2)$ and $1/(1+x)$ yields, within their respective radii of convergence,

$$\arctan x=\sum_{n=0}^\infty \frac{(-1)^n}{2n+1}x^{2n+1}$$

and

$$\ln(1+x)=\sum_{n=1}^\infty \frac{(-1)^{n-1}}{n}x^n.$$
:::

---

**References**

**[Ste]** J. Stewart, *Calculus*, 8th ed., Cengage Learning, 2016.  
**[Kim]** 김홍종, *미적분학 1·2*, 제3개정판, 서울대학교출판문화원, 2020.
