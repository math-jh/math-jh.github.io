---
title: "Differentiation and Derivatives"
description: "We define the derivative as the limit of the instantaneous rate of change of a function, and show that differentiability implies continuity. We also cover higher-order derivatives, linear approximation, and the hierarchy of smoothness conditions."
excerpt: "Definition of derivative, differentiability and continuity, derivatives and higher-order derivatives"

categories: [Math / Calculus]
permalink: /en/math/calculus/derivatives
sidebar: 
    nav: "calculus-en"

date: 2026-06-02
weight: 6
translated_at: 2026-08-17T16:46:38+00:00
translation_source: kimi-cli
---
We previously reformulated the notion of a function being continuous in the language of $\epsilon$-$\delta$ in [§Continuous Functions](/en/math/calculus/continuity). The natural next step is to define the derivative of a function.

## Definition of the Derivative

The slope of the line through two points $(a, f(a))$ and $(x, f(x))$ is the average rate of change $\frac{f(x) - f(a)}{x - a}$, and taking the limit as $x$ approaches $a$ yields the derivative.

::: Definition 1
A function $f$ is said to be *differentiable* at a point $a$ if the limit

$$f'(a) := \lim_{x \rightarrow a} \frac{f(x) - f(a)}{x - a} = \lim_{h \rightarrow 0} \frac{f(a+h) - f(a)}{h}$$

exists. This value $f'(a)$ is called the *derivative* of $f$ at $a$. If $f$ is differentiable at every point of its domain, the function $f'$ defined by $a \mapsto f'(a)$ is called the *derivative function* of $f$.
:::

The two expressions are, of course, trivially the same upon setting $x=a+h$, and by the discussion of the average rate of change above, the derivative $f'(a)$ is the slope of the tangent line to the graph at the point $(a, f(a))$. On the other hand, any line is completely determined by its slope and one point on it; in particular, since this tangent line passes through $(a,f(a))$ by construction, the tangent line to a function differentiable at $a$ is given by

$$y = f(a) + f'(a)(x - a).$$

This linear function best approximates $f$ near $a$, so we write $f(a+h) \approx f(a) + f'(a)h$ when $h$ is small. The derivative is also written following Leibniz as

$$\frac{\dd{f}}{\dd{x}},\qquad \frac{d}{\dd{x}}f$$

and so on, but in calculus the $f'$ notation is often sufficient.

Applying the definition directly, for instance, the average rate of change of $f(x) = x^2$ is $\frac{(a+h)^2 - a^2}{h} = 2a + h$, so $f'(a) = 2a$, and the derivative of a constant function is always $0$. In the same way, for $f(x) = 1/x$ ($x \neq 0$) we obtain $f'(a) = -1/a^2$ by simplifying the average rate of change, and for $f(x) = \sqrt x$ ($x > 0$) we obtain $f'(a) = 1/(2\sqrt a)$ by rationalizing the numerator.

## Differentiability and Continuity

Differentiability is a stronger condition than continuity.

::: Proposition 2
If $f$ is differentiable at $a$, then $f$ is continuous at $a$.
:::

::: Proof
For $x \neq a$,

$$f(x) - f(a) = \frac{f(x)-f(a)}{x-a}\cdot(x-a).$$

As $x \rightarrow a$, the first factor on the right converges to $f'(a)$ and the second factor converges to $0$, so by [§Limits of Functions, ⁋Proposition 5](/en/math/calculus/functions_and_limits#prop5),

$$\lim_{x\rightarrow a}\bigl(f(x)-f(a)\bigr) = f'(a)\cdot 0 = 0.$$

Therefore $f$ is continuous at $a$.
:::

However, the converse does not hold. A representative example is $f(x) = \lvert x\rvert$, which is continuous at $0$ but not differentiable there.

{% diagram Math/Calculus/Derivatives-1.svg width="11.21em" alt="Graph of the absolute value function" %}

Indeed,

$$\frac{f(h)-f(0)}{h} = \frac{\lvert h\rvert}{h}=\begin{cases}1&\text{if $h>0$}\\-1&\text{if $h<0$}\end{cases}$$

so the limit of the average rate of change of this function does not exist, because it approaches $1$ as $h \rightarrow 0^+$ and $-1$ as $h \rightarrow 0^-$, differing from each other.

As a similar example, $f(x) = \sqrt[3]{x}$ has a *vertical tangent* at $0$, where the average rate of change diverges as $h^{-2/3} \rightarrow \infty$.

{% diagram Math/Calculus/Derivatives-2.svg width="12.46em" alt="Vertical tangent of the cube root function" %}

On the other hand, $f(x) = x^{2/3}$ forms a *cusp* at $0$, where the left and right average rates of change diverge to $\mp\infty$.

{% diagram Math/Calculus/Derivatives-3.svg width="13.17em" alt="Cusp of the function x^{2/3}" %}

These are examples that fail to be differentiable only at one or two points, but nondifferentiability can be far worse: there even exist functions like Weierstrass's function that are continuous on all of $\mathbb{R}$ yet have no tangent line at any point.

Conversely, differentiability is a local property that may hold at only a single point, so the following extreme example is also possible.

::: Example 3 (A function differentiable at only one point)
Consider the function

$$f(x) = \begin{cases} x^2 & (x \in \mathbb{Q}) \\ 0 & (x \notin \mathbb{Q}) \end{cases}.$$

For $a \neq 0$, taking a sequence of rationals and a sequence of irrationals both converging to $a$, the function values diverge to $a^2$ and $0$ respectively, so $f$ is discontinuous, and by the contrapositive of [Proposition 2](#prop2) it is not differentiable. On the other hand, at $0$ we have $\lvert f(x)\rvert \leq x^2$, so $f$ is continuous, and the average rate of change satisfies

$$\left\lvert \frac{f(x) - f(0)}{x - 0} \right\rvert = \frac{\lvert f(x)\rvert}{\lvert x\rvert} \leq \lvert x\rvert \rightarrow 0,$$

so $f'(0) = 0$ exists. That is, $f$ is differentiable only at $0$.
:::

## Properties of Differentiation

Meanwhile, since the derivative is ultimately the limit of the average rate of change, we can prove from [§Limits of Functions, ⁋Proposition 5](/en/math/calculus/functions_and_limits#prop5) that differentiation also possesses linearity.

::: Proposition 4
If $f, g$ are differentiable at $a$ and $c$ is a constant, then $f + g$ and $cf$ are also differentiable at $a$, and

$$(f+g)'(a) = f'(a) + g'(a), \qquad (cf)'(a) = c f'(a).$$
:::

::: Proof
The average rate of change splits as

$$\frac{(f+g)(a+h)-(f+g)(a)}{h} = \frac{f(a+h)-f(a)}{h} + \frac{g(a+h)-g(a)}{h},$$

and since each term converges to $f'(a), g'(a)$, the sum also converges by [§Limits of Functions, ⁋Proposition 5](/en/math/calculus/functions_and_limits#prop5). The same result for $cf$ follows by examining its average rate of change.
:::

On the other hand, since the derivative $f'$ is itself a function, if it is differentiable we can differentiate it again.

::: Definition 5
If the derivative $f'$ of $f$ is differentiable, its derivative is called the *second derivative* $f'' = (f')'$. Repeating this, the function obtained by differentiating $n$ times is called the *$n$-th derivative* $f^{(n)}$, and we set $f^{(0)} = f$. If $f^{(n)}$ exists and is continuous on some interval, we say $f$ is of *class $C^n$* on that interval, and if derivatives of all orders exist, we say $f$ is of *class $C^\infty$* or *smooth*.
:::

The second derivative $f''$ is the rate of change of the rate of change; if $f$ is position, then $f''$ is acceleration. Also, the sign of $f''$ tells us the direction in which the graph bends (convex or concave). In this post we do not aim to differentiate specific functions, but in the next post we will see that polynomial functions and functions such as $\sin, \cos, \exp$ are smooth.

Finally, just as a limit exists only when the left and right limits agree, the existence of the derivative also depends on whether the left and right average rates of change agree. Isolating this allows us to handle differentiability at corners and endpoints precisely.

::: Definition 6
The *right-hand derivative* and *left-hand derivative* of a function $f$ at a point $a$ are defined respectively by

$$f'_+(a) := \lim_{h \rightarrow 0^+} \frac{f(a+h) - f(a)}{h}, \qquad f'_-(a) := \lim_{h \rightarrow 0^-} \frac{f(a+h) - f(a)}{h}.$$
:::

Both one-sided derivatives exist and are equal if and only if $f$ is differentiable at $a$, and their common value is $f'(a)$. This is nothing more than applying the fact that a limit exists only when both one-sided limits agree to the average rate of change. ([§Limits of Functions](/en/math/calculus/functions_and_limits)) Revisiting the absolute value function $f(x) = \lvert x\rvert$, we have $f'_+(0) = 1$ and $f'_-(0) = -1$, which differ, so nondifferentiability at $0$ is immediately confirmed. A one-sided derivative is also used naturally when discussing differentiability at an endpoint of the domain; for instance, the differentiability of $f(x) = \sqrt x$ defined on $[0, \infty)$ at $0$ is meaningful only via the right-hand derivative.

---

**References**

**[Ste]** J. Stewart, *Calculus*, 8th ed., Cengage Learning, 2016.  
**[Kim]** 김홍종, *미적분학 1·2*, 제3개정판, 서울대학교출판문화원, 2020.
