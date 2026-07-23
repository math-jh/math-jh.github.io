---
title: "Differentiation and Derivatives"
description: "We define the derivative as the limit of the instantaneous rate of change and show that differentiability implies continuity. We also cover derivatives and higher-order derivatives, linear approximation, and the hierarchy of differentiability and smoothness."
excerpt: "Definition of derivative, differentiability and continuity, derivative and higher-order derivatives"

categories: [Math / Calculus]
permalink: /en/math/calculus/derivatives
sidebar: 
    nav: "calculus-en"

date: 2026-06-02
weight: 6
translated_at: 2026-07-11T10:00:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-07-11T10:00:02+00:00
---
In [§Continuous Functions](/en/math/calculus/continuity) we reformulated the notion of a function being continuous in the language of $\epsilon-\delta$ introduced earlier. The natural next step is to define the derivative of a function.

## Definition of the Derivative

The slope of the line joining two points $(a, f(a))$ and $(x, f(x))$ is the average rate of change $\frac{f(x) - f(a)}{x - a}$, and taking the limit as $x$ approaches $a$ yields the derivative.

::: Definition 1
A function $f$ is said to be *differentiable* at a point $a$ if the limit

$$f'(a) := \lim_{x \rightarrow a} \frac{f(x) - f(a)}{x - a} = \lim_{h \rightarrow 0} \frac{f(a+h) - f(a)}{h}$$

exists. This value $f'(a)$ is called the *derivative* of $f$ at $a$. If $f$ is differentiable at every point of its domain, the function $f'$ defined by $a \mapsto f'(a)$ is called the *derivative function* of $f$.
:::

Of course, the two expressions are obviously the same upon setting $x = a + h$, and by the preceding discussion on the average rate of change, the derivative $f'(a)$ is the slope of the tangent line to the graph at the point $(a, f(a))$. Moreover, any straight line is completely determined by its slope and one point on it; in particular, since this tangent line passes through $(a, f(a))$ by construction, the tangent line to a function differentiable at $a$ is given by

$$y = f(a) + f'(a)(x - a).$$

This linear function approximates $f$ best near $a$, so for small $h$ we write $f(a+h) \approx f(a) + f'(a)h$. Following Leibniz, the derivative is also written as

$$\frac{df}{dx},\qquad \frac{d}{dx}f$$

and so on, but in calculus the notation $f'$ is often sufficient.

Applying the definition directly, for instance, the average rate of change of $f(x) = x^2$ is $\frac{(a+h)^2 - a^2}{h} = 2a + h$, so $f'(a) = 2a$; the derivative of a constant function is always $0$. In the same way, for $f(x) = 1/x$ ($x \neq 0$) we put the average rate of change over a common denominator to obtain $f'(a) = -1/a^2$, and for $f(x) = \sqrt x$ ($x > 0$) we rationalize the numerator to get $f'(a) = 1/(2\sqrt a)$.

## Differentiability and Continuity

Differentiability is a stronger condition than continuity.

::: Proposition 2
If $f$ is differentiable at $a$, then $f$ is continuous at $a$.
:::

::: Proof
For $x \neq a$ we have

$$f(x) - f(a) = \frac{f(x)-f(a)}{x-a}\cdot(x-a).$$

As $x \rightarrow a$, the first factor on the right converges to $f'(a)$ and the second factor converges to $0$, so by [§Limits of Functions, ⁋Proposition 5](/en/math/calculus/functions_and_limits#prop5),

$$\lim_{x\rightarrow a}\bigl(f(x)-f(a)\bigr) = f'(a)\cdot 0 = 0.$$

Hence $f$ is continuous at $a$.
:::

However, the converse does not hold. A typical example is $f(x) = \lvert x\rvert$: this function is continuous at $0$ but not differentiable there.

![Graph of the absolute value function](/assets/images/Math/Calculus/Derivatives-1.svg){:style="width:11.21em" class="invert" .align-center}

Indeed,

$$\frac{f(h)-f(0)}{h} = \frac{\lvert h\rvert}{h}=\begin{cases}1&\text{if $h>0$}\\-1&\text{if $h<0$}\end{cases}$$

so the derivative of this function is $1$ as $h \rightarrow 0^+$ and $-1$ as $h \rightarrow 0^-$; the one-sided limits differ, so the limit does not exist.

As a similar example, $f(x) = \sqrt[3]{x}$ has a *vertical tangent* at $0$, where the average rate of change diverges as $h^{-2/3} \rightarrow \infty$.

![Vertical tangent of the cube root function](/assets/images/Math/Calculus/Derivatives-2.svg){:style="width:12.46em" class="invert" .align-center}

On the other hand, $f(x) = x^{2/3}$ forms a *cusp* at $0$, where the left and right average rates of change diverge to $\mp\infty$.

![Cusp of the 2/3-power function](/assets/images/Math/Calculus/Derivatives-3.svg){:style="width:13.17em" class="invert" .align-center}

These are examples of non-differentiability at only one or two points, but non-differentiability can be far worse: there even exist functions like Weierstrass's function $W(x) = \sum_{n=0}^\infty a^n\cos(b^n\pi x)$ that are continuous on all of $\mathbb{R}$ yet have no tangent at any point.

Conversely, differentiability is a local property that can hold at a single point alone, so the following extreme example is also possible.

::: Example 3 (A function differentiable at only one point)
Consider the function

$$f(x) = \begin{cases} x^2 & (x \in \mathbb{Q}) \\ 0 & (x \notin \mathbb{Q}) \end{cases}$$

For $a \neq 0$, along a sequence of rationals and a sequence of irrationals converging to $a$ the function values split to $a^2$ and $0$ respectively, so $f$ is discontinuous and hence not differentiable by the contrapositive of [Proposition 2](#prop2). On the other hand, at $0$ we have $\lvert f(x)\rvert \leq x^2$, so $f$ is continuous, and the average rate of change satisfies

$$\left\lvert \frac{f(x) - f(0)}{x - 0} \right\rvert = \frac{\lvert f(x)\rvert}{\lvert x\rvert} \leq \lvert x\rvert \rightarrow 0$$

so $f'(0) = 0$ exists. That is, $f$ is differentiable only at $0$.
:::

## Properties of Differentiation

Meanwhile, since the derivative is ultimately the limit of the average rate of change, we can prove from [§Limits of Functions, ⁋Proposition 5](/en/math/calculus/functions_and_limits#prop5) that differentiation also enjoys linearity.

::: Proposition 4
If $f$ and $g$ are differentiable at $a$ and $c$ is a constant, then $f + g$ and $cf$ are also differentiable at $a$, and

$$(f+g)'(a) = f'(a) + g'(a), \qquad (cf)'(a) = c f'(a).$$
:::

::: Proof
The average rate of change splits as

$$\frac{(f+g)(a+h)-(f+g)(a)}{h} = \frac{f(a+h)-f(a)}{h} + \frac{g(a+h)-g(a)}{h},$$

and since each term converges to $f'(a)$ and $g'(a)$, the sum also converges by [§Limits of Functions, ⁋Proposition 5](/en/math/calculus/functions_and_limits#prop5). Examining the average rate of change for $cf$ gives the same result.
:::

On the other hand, since the derivative $f'$ is again a function, if it is differentiable we can differentiate it once more.

::: Definition 5
If the derivative $f'$ of $f$ is differentiable, its derivative is called the *second derivative* $f'' = (f')'$. Repeating this, the result of differentiating $n$ times is called the *$n$th derivative* $f^{(n)}$, and we set $f^{(0)} = f$. If $f^{(n)}$ exists and is continuous on some interval, we say $f$ is *of class $C^n$* on that interval, and if derivatives of all orders exist, we say $f$ is *of class $C^\infty$* or *smooth*.
:::

The second derivative $f''$ is the rate of change of the rate of change; if $f$ represents position, then $f''$ is acceleration. The sign of $f''$ also tells us the direction in which the graph bends (convex or concave). In this post we do not aim to differentiate specific functions, but in the next post we will see that polynomials and functions such as $\sin$, $\cos$, and $\exp$ are smooth.

Finally, just as a limit exists only when the left and right limits agree, the existence of a derivative also depends on whether the left and right average rates of change agree. Stating this separately allows us to treat differentiability at corners and endpoints precisely.

::: Definition 6
The *right-hand derivative* and *left-hand derivative* of a function $f$ at a point $a$ are defined respectively by

$$f'_+(a) := \lim_{h \rightarrow 0^+} \frac{f(a+h) - f(a)}{h}, \qquad f'_-(a) := \lim_{h \rightarrow 0^-} \frac{f(a+h) - f(a)}{h}.$$

Both one-sided derivatives exist and are equal if and only if $f$ is differentiable at $a$, and then their common value is $f'(a)$.
:::

This is nothing more than applying the fact that a limit exists only when both one-sided limits agree to the average rate of change. (See [§Limits of Functions](/en/math/calculus/functions_and_limits).) Revisiting the absolute value function $f(x) = \lvert x\rvert$, we have $f'_+(0) = 1$ and $f'_-(0) = -1$; the two differ, so it is immediately confirmed that $f$ is not differentiable at $0$. One-sided derivatives are also used naturally when discussing differentiability at an endpoint of the domain: for example, the behavior of $f(x) = \sqrt x$ at $0$ on the interval $[0, \infty)$ has meaning only through the right-hand derivative.
