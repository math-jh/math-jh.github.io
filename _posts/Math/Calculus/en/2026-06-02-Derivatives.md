---
title: "Differentiation and Derivatives"
description: "We define the derivative as the limit of the difference quotient and show that differentiability implies continuity. We also cover higher-order derivatives, linear approximation, and the hierarchy between differentiability and smoothness."
excerpt: "Definition of the derivative, differentiability and continuity, higher-order derivatives"

categories: [Math / Calculus]
permalink: /en/math/calculus/derivatives
sidebar: 
    nav: "calculus-en"

date: 2026-06-02
weight: 6
translated_at: 2026-06-22T18:00:03+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-22T18:00:03+00:00
---
We previously reformulated what it means for a function to be continuous in the language of $$\epsilon-\delta$$ in [§Continuous Functions](/en/math/calculus/continuity). The natural next step is to define the derivative of a function.

## Definition of the Derivative

The slope of the line through two points $$(a, f(a))$$ and $$(x, f(x))$$ is the average rate of change $$\frac{f(x) - f(a)}{x - a}$$, and taking the limit as $$x$$ approaches $$a$$ gives the derivative.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> A function $$f$$ is said to be *differentiable* at a point $$a$$ if the limit

$$f'(a) := \lim_{x \to a} \frac{f(x) - f(a)}{x - a} = \lim_{h \to 0} \frac{f(a+h) - f(a)}{h}$$

exists. This value $$f'(a)$$ is called the *derivative* of $$f$$ at $$a$$. If $$f$$ is differentiable at every point in its domain, the function $$f'$$ defined by $$a \mapsto f'(a)$$ is called the *derivative function* of $$f$$.

</div>

The two expressions are obviously the same upon setting $$x = a + h$$, and by the preceding discussion on average rate of change, the derivative $$f'(a)$$ is the slope of the tangent line to the graph at the point $$(a, f(a))$$. Moreover, any line is completely determined by its slope and a point on it; since this tangent line passes through $$(a, f(a))$$ by construction, the tangent line to a function differentiable at $$a$$ is given by

$$y = f(a) + f'(a)(x - a).$$

This linear function approximates $$f$$ best near $$a$$, so we write $$f(a+h) \approx f(a) + f'(a)h$$ when $$h$$ is small. The derivative is also written, following Leibniz, as

$$\frac{df}{dx},\qquad \frac{d}{dx}f$$

but in calculus the $$f'$$ notation is often sufficient.

Applying the definition directly: for example, the average rate of change of $$f(x) = x^2$$ is $$\frac{(a+h)^2 - a^2}{h} = 2a + h$$, so $$f'(a) = 2a$$; the derivative of a constant function is always $$0$$. Similarly, for $$f(x) = 1/x$$ ($$x \neq 0$$) we find $$f'(a) = -1/a^2$$ by simplifying the average rate of change, and for $$f(x) = \sqrt x$$ ($$x > 0$$) we rationalize the numerator to obtain $$f'(a) = 1/(2\sqrt a)$$.

## Differentiability and Continuity

Differentiability is a stronger condition than continuity.

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> If $$f$$ is differentiable at $$a$$, then $$f$$ is continuous at $$a$$.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

For $$x \neq a$$,

$$f(x) - f(a) = \frac{f(x)-f(a)}{x-a}\cdot(x-a)$$

holds. As $$x \to a$$, the first factor on the right converges to $$f'(a)$$ and the second to $$0$$, so by [§Limits of Functions, ⁋Proposition 5](/en/math/calculus/functions_and_limits#prop5),

$$\lim_{x\to a}\bigl(f(x)-f(a)\bigr) = f'(a)\cdot 0 = 0.$$

Therefore $$f$$ is continuous at $$a$$.

</details>

However, the converse does not hold. The standard example is $$f(x) = \lvert x\rvert$$, which is continuous at $$0$$ but not differentiable there.

![Graph of the absolute value function](/assets/images/Math/Calculus/Derivatives-1.svg){:style="width:11.21em" class="invert" .align-center}

Indeed,

$$\frac{f(h)-f(0)}{h} = \frac{\lvert h\rvert}{h}=\begin{cases}1&\text{if $h>0$}\\-1&\text{if $h<0$}\end{cases}$$

so the derivative from the right is $$1$$ as $$h \to 0^+$$ and from the left is $$-1$$ as $$h \to 0^-$$; since the one-sided limits differ, the limit does not exist.

A similar example is $$f(x) = \sqrt[3]{x}$$, which has a *vertical tangent* at $$0$$ because its average rate of change diverges as $$h^{-2/3} \to \infty$$.

![Vertical tangent of the cube root function](/assets/images/Math/Calculus/Derivatives-2.svg){:style="width:12.46em" class="invert" .align-center}

On the other hand, $$f(x) = x^{2/3}$$ forms a *cusp* at $$0$$ where the left and right average rates of change diverge to $$\mp\infty$$.

![Cusp of the $2/3$-power function](/assets/images/Math/Calculus/Derivatives-3.svg){:style="width:13.17em" class="invert" .align-center}

These are examples of non-differentiability at only one or two points, but non-differentiability can be far worse: there even exist functions like Weierstrass's function $$W(x) = \sum_{n=0}^\infty a^n\cos(b^n\pi x)$$ that are continuous everywhere on $$\mathbb{R}$$ yet have no tangent at any point.

Conversely, differentiability is a local property that may hold at only a single point, so the following extreme example is possible.

<div class="example" markdown="1">

<ins id="ex3">**Example 3 (A function differentiable at only one point)**</ins> Consider the function

$$f(x) = \begin{cases} x^2 & (x \in \mathbb{Q}) \\ 0 & (x \notin \mathbb{Q}) \end{cases}$$

At $$a \neq 0$$, the function values diverge to $$a^2$$ and $$0$$ along rational and irrational sequences converging to $$a$$, so $$f$$ is discontinuous and hence not differentiable by the contrapositive of Proposition 2. At $$0$$, however, $$\lvert f(x)\rvert \leq x^2$$ ensures continuity, and the average rate of change satisfies

$$\left\lvert \frac{f(x) - f(0)}{x - 0} \right\rvert = \frac{\lvert f(x)\rvert}{\lvert x\rvert} \leq \lvert x\rvert \to 0$$

so $$f'(0) = 0$$ exists. Thus $$f$$ is differentiable only at $$0$$.

</div>

## Properties of Differentiation

Meanwhile, since the derivative is ultimately the limit of the average rate of change, we can prove from [§Limits of Functions, ⁋Proposition 5](/en/math/calculus/functions_and_limits#prop5) that differentiation also satisfies linearity.

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4**</ins> If $$f, g$$ are differentiable at $$a$$ and $$c$$ is a constant, then $$f + g$$ and $$cf$$ are also differentiable at $$a$$ and

$$(f+g)'(a) = f'(a) + g'(a), \qquad (cf)'(a) = c f'(a)$$

hold.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

The average rate of change decomposes as

$$\frac{(f+g)(a+h)-(f+g)(a)}{h} = \frac{f(a+h)-f(a)}{h} + \frac{g(a+h)-g(a)}{h}$$

and since each term converges to $$f'(a), g'(a)$$, the sum also converges by the limit laws. The same result for $$cf$$ follows by inspecting its average rate of change.

</details>

Since the derivative $$f'$$ is itself a function, we can differentiate it again if it is differentiable.

<div class="definition" markdown="1">

<ins id="def5">**Definition 5**</ins> If the derivative $$f'$$ of $$f$$ is differentiable, its derivative is called the *second derivative* $$f'' = (f')'$$. Repeating this, the $$n$$-th derivative obtained by differentiating $$n$$ times is denoted $$f^{(n)}$$, with $$f^{(0)} = f$$. If $$f^{(n)}$$ exists and is continuous on some interval, we say $$f$$ is of *class $$C^n$$* on that interval, and if derivatives of all orders exist, we say $$f$$ is of *class $$C^\infty$$* or *smooth*.

</div>

The second derivative $$f''$$ is the rate of change of the rate of change; if $$f$$ represents position, then $$f''$$ is acceleration. The sign of $$f''$$ also tells us the direction in which the graph bends (convexity or concavity). Although the goal of this post is not to differentiate concrete functions, in the next post we will see that polynomial functions and functions such as $$\sin, \cos, \exp$$ are smooth.

Finally, just as a limit exists only when the left and right limits agree, the existence of a derivative also depends on whether the left and right average rates of change agree. Separating this out allows us to treat differentiability precisely at corners and endpoints.

<div class="definition" markdown="1">

<ins id="def6">**Definition 6**</ins> The *right-hand derivative* and *left-hand derivative* of a function $$f$$ at a point $$a$$ are defined respectively by

$$f'_+(a) := \lim_{h \to 0^+} \frac{f(a+h) - f(a)}{h}, \qquad f'_-(a) := \lim_{h \to 0^-} \frac{f(a+h) - f(a)}{h}$$

The function $$f$$ is differentiable at $$a$$ if and only if both one-sided derivatives exist and are equal, and their common value is $$f'(a)$$.

</div>

This is nothing more than applying the fact that a limit exists only when both one-sided limits agree ([§Limits of Functions](/en/math/calculus/functions_and_limits)) to the average rate of change. Revisiting the absolute value function $$f(x) = \lvert x\rvert$$, we have $$f'_+(0) = 1$$ and $$f'_-(0) = -1$$, which differ, so it is immediately confirmed to be non-differentiable at $$0$$. One-sided derivatives also arise naturally when discussing differentiability at endpoints of the domain; for instance, the behavior of $$f(x) = \sqrt x$$ defined on $$[0, \infty)$$ at $$0$$ is meaningful only through the right-hand derivative.
