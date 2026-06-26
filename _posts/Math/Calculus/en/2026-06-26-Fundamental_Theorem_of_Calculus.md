---
title: "The Fundamental Theorem of Calculus"
description: "We prove the fundamental theorem of calculus in two forms, showing that differentiation and integration are inverse operations. We demonstrate that an integral with a variable upper limit is an antiderivative of the integrand, and use this to derive the evaluation theorem for computing definite integrals, along with applications and term-by-term integration of power series."
excerpt: "The fundamental theorem, existence of antiderivatives, Leibniz rule, term-by-term integration of power series"

categories: [Math / Calculus]
permalink: /en/math/calculus/fundamental_theorem_of_calculus
sidebar: 
    nav: "calculus-en"

date: 2026-06-26
weight: 11
translated_at: 2026-06-26T13:30:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-26T13:30:02+00:00
---
We previously defined two different kinds of integrals: the indefinite integral and the definite integral. The indefinite integral is meaningful as the reverse process of differentiation, while the definite integral carries its own geometric meaning as the area under a curve. The fundamental theorem of calculus shows that these two are, in some sense, exactly the same process, and one could even say that calculus itself was born from this insight.

## Fundamental Theorem of Calculus

Since the indefinite integral is defined as the reverse of differentiation, the meaningful part of this process is that the definite integral actually yields a result similar to the reverse of differentiation. However, the definite integral is ultimately a tool that produces a value, so its output is not a function. To address this, we take the upper limit of the definite integral as a variable and define the following function:

$$\int_a^x f(t)dt$$

Here, $$t$$ is simply a dummy variable introduced to avoid confusion with $$x$$, which already appears in the upper limit; if no confusion arises, $$t$$ can just as well be replaced by $$x$$.

<div class="proposition" markdown="1">

<ins id="thm1">**Theorem 1 (Fundamental Theorem of Calculus)**</ins> If $$f$$ is continuous on $$[a,b]$$ and we define $$F(x) = \int_a^x f(t)dt$$, then $$F$$ is differentiable on $$[a,b]$$ and for every $$x$$,

$$F'(x) = f(x)$$

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

By the second result of [§Integration, ⁋Proposition 11](/en/math/calculus/integration#prop11), for $$h>0$$ we have

$$F(x+h) - F(x) = \int_a^{x+h} f - \int_a^x f = \int_x^{x+h} f(t)dt$$

Since $$f$$ is continuous on $$[x, x+h]$$, by [§Continuous Functions, ⁋Theorem 4](/en/math/calculus/continuity#thm4) it attains a minimum $$m_h$$ and a maximum $$M_h$$ on that interval, and by the third result of [§Integration, ⁋Proposition 11](/en/math/calculus/integration#prop11),

$$m_h \leq \frac{F(x+h) - F(x)}{h} \leq M_h$$

holds. Now as $$h \to 0$$, the interval $$[x, x+h]$$ shrinks to the single point $$x$$, and by the continuity of $$f$$ we have $$m_h, M_h \to f(x)$$; thus by [§Limits of Functions, ⁋Proposition 8](/en/math/calculus/functions_and_limits#prop8) the average rate of change converges to $$f(x)$$. The case $$h < 0$$ can be handled in a similar manner to complete the proof.

</details>

This theorem is a rigorous expression of the intuition that <em-ko>the rate at which area accumulates is precisely the height</em-ko>. That is, the rate at which the function $$F(x)$$ defined by integration increases at a point, $$F'(x)$$, is exactly the value of the integrand at that point, $$f(x)$$.

<div class="proposition" markdown="1">

<ins id="cor2">**Corollary 2**</ins> Every function continuous on $$[a,b]$$ has a primitive. Specifically, $$F(x) = \int_a^x f(t)dt$$ is one such primitive.

</div>

The $$F(x)$$ defined above fixes the constant of integration $$C$$ to a single value; concretely, one may think of it as choosing the constant of integration so that $$F(a)=0$$.

On the other hand, this corollary is a different story from the claim that the integral of an arbitrary function can be expressed in terms of elementary functions: it only says that $$\int_a^x f(t)dt$$ defined by the above formula is <em-ko>in itself</em-ko> a primitive of $$f$$. Consider the following example.

<div class="example" markdown="1">

<ins id="ex3">**Example 3 (Derivatives of special functions)**</ins> The *error function* is defined by

$$\erf(x) = \frac{2}{\sqrt{\pi}}\int_0^x e^{-t^2}dt$$

Since the primitive of $$e^{-t^2}$$ cannot be written in terms of elementary functions, this integral has no closed form; however, by [Theorem 1](#thm1), $$\erf$$ is differentiable and

$$\erf'(x) = \frac{2}{\sqrt{\pi}}e^{-x^2}$$

Likewise, the *logarithmic integral* $$\li(x) = \int_2^x dt/\ln t$$ immediately yields $$\li'(x) = 1/\ln x$$. In this way, functions defined by integration become subjects of calculus in their own right.

</div>

A slightly more advanced form of this expression will be reintroduced after we examine the integration of power series in [Proposition 7](#prop7).

Meanwhile, combining [Theorem 1](#thm1) with the fact that a function with zero derivative must be constant, we obtain a powerful tool for computing definite integrals as the difference of primitives.

<div class="proposition" markdown="1">

<ins id="thm4">**Theorem 4**</ins> If $$f$$ is continuous on $$[a,b]$$ and $$G$$ is any primitive of $$f$$, then

$$\int_a^b f(x)dx = G(b) - G(a)$$

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

Let $$F(x) = \int_a^x f$$; then by [Theorem 1](#thm1), $$F$$ is also a primitive of $$f$$. Two primitives differ only by a constant ([§Mean Value Theorem, ⁋Corollary 5](/en/math/calculus/mean_value_theorem#cor5)), so there exists a constant $$C$$ such that $$F = G + C$$. Since $$F(a) = \int_a^a f = 0$$, we have $$C = -G(a)$$, and therefore

$$\int_a^b f = F(b) = G(b) + C = G(b) - G(a)$$

</details>

The difference $$G(b) - G(a)$$ is commonly written as $$\bigl[G(x)\bigr]_a^b$$. Thanks to this theorem, the computation of a definite integral is reduced to the problem of finding a primitive rather than taking the limit of Riemann sums. For example, $$\int_0^1 x^2dx = \bigl[x^3/3\bigr]_0^1 = 1/3$$ agrees with the value obtained laboriously via Riemann sums in [§Integration](/en/math/calculus/integration), but here it is obtained by an entirely different calculation: substituting the endpoints into the primitive.

In particular, [Theorem 1](#thm1) combines with [§Differentiation Rules, ⁋Theorem 4](/en/math/calculus/differentiation_rules#thm4) when the upper or lower limit of integration depends on a variable. If the upper limit is a function $$g(x)$$, letting $$F(u) = \int_a^u f$$ gives $$\int_a^{g(x)} f = F(g(x))$$, and since $$F'(u) = f(u)$$, the chain rule yields $$\frac{d}{dx}\int_a^{g(x)} f(t)dt = f(g(x))g'(x)$$. If both limits are variable, split the interval into two parts and apply the result to each side.

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5 (Leibniz rule)**</ins> If $$f$$ is continuous and $$g, h$$ are differentiable, then

$$\frac{d}{dx}\int_{h(x)}^{g(x)} f(t)dt = f(g(x))g'(x) - f(h(x))h'(x)$$

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

Pick an arbitrary fixed point $$c$$ and split the integral into two parts using the additivity over intervals from [§Integration, ⁋Proposition 11](/en/math/calculus/integration#prop11):

$$\int_{h(x)}^{g(x)} f(t)dt = \int_c^{g(x)} f(t)dt - \int_c^{h(x)} f(t)dt$$

Letting $$F(u) = \int_c^v f(v)dv$$, by [Theorem 1](#thm1) we have $$F'(u) = f(u)$$, and the right-hand side is $$F(g(x)) - F(h(x))$$. Applying the chain rule to each term gives

$$\begin{aligned}
\frac{d}{dx}\bigl[F(g(x)) - F(h(x))\bigr] &= F'(g(x))g'(x) - F'(h(x))h'(x) \\[2pt]
&= f(g(x))g'(x) - f(h(x))h'(x)
\end{aligned}$$

</details>

However, care must be taken when the integrand is undefined or discontinuous on the interval of integration. Consider the following example.

<div class="example" markdown="1">

<ins id="ex6">**Example 6**</ins> For the integral

$$\int_{-1}^{1} \frac{dx}{x^2}$$

formally substituting

$$\bigl[-x^{-1}\bigr]_{-1}^{1} = -1 - 1 = -2$$

yields a negative number, but since the integrand $$1/x^2$$ is always positive, this is clearly a wrong calculation. The reason this is wrong is that the integrand diverges at $$x = 0$$ and is therefore not continuous on $$[-1,1]$$. Since the hypothesis of [Theorem 4](#thm4) is violated, we cannot apply the theorem as is, and in fact this integral diverges.

</div>

## Term-by-Term Integration of Power Series

Meanwhile, integration also pairs well with power series. The following proposition likewise requires knowledge of analysis for its proof, so we shall accept it as a fact for now.

<div class="proposition" markdown="1">

<ins id="prop7">**Proposition 7 (Term-by-term integration of power series)**</ins> If $$f(x) = \sum_{n=0}^\infty c_n x^n$$ has radius of convergence $$R > 0$$, then for $$\lvert x\rvert < R$$,

$$\int_0^x f(t)dt = \sum_{n=0}^\infty \frac{c_n}{n+1} x^{n+1}$$

and this series also has radius of convergence $$R$$.

</div>

Then we can see in what form the $$e^{-x^2}$$ examined earlier in [Example 3](#ex3) appears.

<div class="example" markdown="1">

<ins id="ex8">**Example 8**</ins> Returning to the error function of [Example 3](#ex3). From the power series of the exponential function,

$$e^{-t^2} = \sum_{n=0}^\infty \frac{(-1)^n}{n!}t^{2n}$$

and its radius of convergence is $$\infty$$. Now integrating term by term using [Proposition 7](#prop7),

$$\int_0^x e^{-t^2}dt = \sum_{n=0}^\infty \frac{(-1)^n}{n!(2n+1)}x^{2n+1}$$

and therefore

$$\erf(x) = \frac{2}{\sqrt{\pi}}\sum_{n=0}^\infty \frac{(-1)^n}{n!(2n+1)}x^{2n+1}$$

Thus, although the primitive still cannot be written in terms of elementary functions, it can be written explicitly as a power series in this way.

By a similar method, term-by-term integration of $$1/(1 + x^2)$$ and $$1/(1+x)$$ yields, within their respective radii of convergence,

$$\arctan x = \sum_{n=0}^\infty \frac{(-1)^n}{2n+1} x^{2n+1}$$

and

$$\ln(1+x) = \sum_{n=1}^\infty \frac{(-1)^{n-1}}{n} x^n$$

</div>
