---
title: "Differentiation"
description: "We derive the derivative of the exponential function by differentiating power series term by term, and summarize the derivatives of trigonometric functions along with the product, chain, quotient, and inverse function rules. This gives a systematic way to differentiate any function built from elementary functions."
excerpt: "Termwise differentiation of power series, derivatives of elementary functions, product, quotient, and chain rules"

categories: [Math / Calculus]
permalink: /en/math/calculus/differentiation_rules
sidebar: 
    nav: "calculus-en"

date: 2026-06-22
weight: 7
translated_at: 2026-06-24T08:00:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-24T08:00:02+00:00
---
We covered the definition of differentiation and its basic properties in [§Derivatives](/en/math/calculus/derivatives). In this post, we treat derivatives of concrete functions and differentiation rules that apply to general functions.

## Term-by-Term Differentiation of Power Series

First, for any natural number $$n$$, the derivative of $$x^n$$ at a point $$a$$ is

$$\lim_{h\rightarrow 0}\frac{(a+h)^n-a^n}{h}=\lim_{h\rightarrow 0}\frac{na^{n-1}h+\ldots}{h}=na^{n-1}$$

which can be verified directly, and similarly for a negative integer $$n = -m$$, putting the difference quotient over a common denominator gives

$$\frac{(a+h)^{-m} - a^{-m}}{h} = -\frac{(a+h)^m - a^m}{h}\cdot\frac{1}{(a+h)^ma^m}$$

so that in the end $$(x^n)' = n x^{n-1}$$ holds for all integers $$n$$.

Meanwhile, by linearity a polynomial is differentiated term by term, so this also yields the differentiation rule for arbitrary polynomial functions. However, in general distributing differentiation termwise in an <em>infinite</em> sum is not obvious, and the following proposition guarantees that this is permitted for power series.

<div class="proposition" markdown="1">

<ins id="prop1">**Proposition 1 (Term-by-Term Differentiation of Power Series)**</ins> If a power series $$f(x) = \sum_{n=0}^\infty c_n x^n$$ has radius of convergence $$R > 0$$, then $$f$$ is differentiable for $$\lvert x\rvert < R$$ and

$$f'(x) = \sum_{n=1}^\infty n\,c_n x^{n-1}$$

and this series also has radius of convergence $$R$$.

</div>

That the radius of convergence of the series on the right-hand side is $$R$$ itself follows from the fact that $$n^{1/n}$$ converges to $$1$$ as $$n\rightarrow \infty$$, but to rigorously justify that this is actually equal to $$f'(x)$$ our tools are insufficient, so we shall accept this and move on.

## Derivatives of Trigonometric and Exponential Functions

Before examining differentiation rules in earnest, we derive the derivatives of several functions.

First, the exponential function was defined in [§Power Series, ⁋Example 3](/en/math/calculus/power_series#ex3) by $$e^x = \sum_{n\geq 0} x^n/n!$$. Applying [Proposition 1](#prop1) now, its derivative is the sum of the term-by-term derivatives

$$(e^x)' = \sum_{n=1}^\infty n\,\frac{x^{n-1}}{n!} = \sum_{n=1}^\infty \frac{x^{n-1}}{(n-1)!} = \sum_{m=0}^\infty \frac{x^m}{m!} = e^x$$

so the exponential function is invariant under differentiation. In high school, this result was obtained from the limit

$$\lim_{h\to 0}(e^h-1)/h = 1$$

We will also soon write trigonometric functions as power series, but for now we derive them as in high school using the two limits

$$\lim_{h \to 0} \frac{\sin h}{h} = 1, \qquad \lim_{h \to 0} \frac{1 - \cos h}{h} = 0$$

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2 (Derivatives of Trigonometric Functions)**</ins> At every point $$(\sin x)' = \cos x$$ and $$(\cos x)' = -\sin x$$.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

Using the addition formula $$\sin(x+h) = \sin x\cos h + \cos x \sin h$$, split the difference quotient as

$$\frac{\sin(x+h) - \sin x}{h} = \sin x \cdot \frac{\cos h - 1}{h} + \cos x \cdot \frac{\sin h}{h}$$

and as $$h \to 0$$, by the two limits above this converges to $$\sin x \cdot 0 + \cos x \cdot 1 = \cos x$$. The derivative of $$\cos x$$ is obtained in the same way.

</details>

## Various Differentiation Rules

We now state differentiation rules that apply to general forms. In [§Derivatives, ⁋Proposition 4](/en/math/calculus/derivatives#prop4) we saw that differentiation behaves well with respect to constant multiples and addition, but it does not simply distribute over products.

<div class="proposition" markdown="1">

<ins id="prop3">**Proposition 3 (Product Rule)**</ins> If $$f, g$$ are differentiable at $$a$$, then $$fg$$ is also differentiable at $$a$$ and

$$(fg)'(a) = f'(a)\,g(a) + f(a)\,g'(a)$$

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

Adding and subtracting the same term in the difference quotient gives

$$\frac{f(a+h)g(a+h) - f(a)g(a)}{h} = \frac{f(a+h)-f(a)}{h}\,g(a+h) + f(a)\,\frac{g(a+h)-g(a)}{h}$$

As $$h \to 0$$, the difference quotient in the first term converges to $$f'(a)$$, $$g(a+h)$$ converges to $$g(a)$$ by continuity of $$g$$ ([§Derivatives, ⁋Proposition 2](/en/math/calculus/derivatives#prop2)), and the difference quotient in the second term converges to $$g'(a)$$, so by [§Limits of Functions, ⁋Proposition 5](/en/math/calculus/functions_and_limits#prop5) the sum converges to $$f'(a)g(a) + f(a)g'(a)$$.

</details>

The most widely used rule is the differentiation of composite functions.

<div class="proposition" markdown="1">

<ins id="thm4">**Theorem 4 (Chain Rule)**</ins> If $$f$$ is differentiable at $$a$$ and $$g$$ is differentiable at $$b = f(a)$$, then the composition $$g \circ f$$ is also differentiable at $$a$$ and

$$(g \circ f)'(a) = g'(f(a))\,f'(a)$$

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

Encode the differentiability of $$g$$ in the auxiliary function

$$\varphi(y) = \begin{cases} \frac{g(y) - g(b)}{y - b}, & y \neq b,\\[1mm] g'(b), & y = b \end{cases}$$

By the definition of differentiability, $$\varphi$$ is continuous at $$b$$, and for all $$y$$ we have $$g(y) - g(b) = \varphi(y)(y - b)$$. Substituting $$y = f(a+h)$$ gives

$$\frac{g(f(a+h)) - g(f(a))}{h} = \varphi(f(a+h))\,\frac{f(a+h) - f(a)}{h}$$

and as $$h \to 0$$, by continuity of $$f$$ we have $$\varphi(f(a+h)) \to \varphi(b) = g'(b)$$, while the second factor converges to $$f'(a)$$, so the limit is $$g'(f(a))f'(a)$$.

</details>

The quotient rule now follows as a corollary of the product rule and the chain rule.

<div class="proposition" markdown="1">

<ins id="cor5">**Corollary 5 (Quotient Rule)**</ins> If $$f, g$$ are differentiable at $$a$$ and $$g(a) \neq 0$$, then $$f/g$$ is also differentiable at $$a$$ and

$$\left(\frac{f}{g}\right)'(a) = \frac{f'(a)\,g(a) - f(a)\,g'(a)}{g(a)^2}$$

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

Defining the function $$h(t)=1/t$$, we have $$1/g =h \circ g$$, and by the derivative of integer powers $$h'(t)=-1/t^2$$, so by [Theorem 4](#thm4) we have $$(1/g)'(a) = -g(a)^{-2}g'(a)$$. Applying the product rule to $$f/g = f\cdot(1/g)$$ now gives

$$\left(\frac{f}{g}\right)'(a) = \frac{f'(a)}{g(a)} - \frac{f(a)g'(a)}{g(a)^2} = \frac{f'(a)g(a) - f(a)g'(a)}{g(a)^2}$$

</details>

For example, from $$\tan x = \sin x/\cos x$$ we have $$(\tan x)' = (\cos^2 x + \sin^2 x)/\cos^2 x = \sec^2 x$$, and similarly $$(\cot x)' = -\csc^2 x$$.

Finally, if a function is monotone then the derivative of its inverse function is obtained immediately without separate calculation.

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6 (Derivative of the Inverse Function)**</ins> Let $$f$$ be a continuous monotone function on an interval having inverse function $$f^{-1}$$, and suppose $$f$$ is differentiable at $$a$$ with $$f'(a) \neq 0$$. Then $$f^{-1}$$ is differentiable at $$b = f(a)$$ and

$$(f^{-1})'(b) = \frac{1}{f'(a)} = \frac{1}{f'(f^{-1}(b))}$$

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

Assuming $$f^{-1}$$ is differentiable at $$b$$, differentiating both sides of the identity $$f(f^{-1}(y)) = y$$ by the chain rule gives $$f'(f^{-1}(b))\cdot(f^{-1})'(b) = 1$$, and since $$f'(a) \neq 0$$ the proof is complete.

</details>

With this we can also proceed to differentiate the inverses of the functions examined above. For example, for the inverse $$\ln$$ of $$e^x$$, since $$(e^x)' = e^x$$ we have $$(\ln y)' = 1/e^{\ln y} = 1/y$$, and for the inverse $$\arcsin$$ of $$\sin$$ restricted to $$(-\pi/2, \pi/2)$$, since $$f'(x) = \cos x = \sqrt{1 - \sin^2 x} > 0$$ we have

$$(\arcsin y)' = \frac{1}{\sqrt{1 - y^2}} \qquad (\lvert y\rvert < 1)$$

and in the same way $$(\arctan y)' = 1/(1 + y^2)$$.

On the other hand, once we have computed a derivative using the rules so far, we may ask whether that derivative is again continuous; even a function differentiable everywhere can have a discontinuous derivative.

<div class="example" markdown="1">

<ins id="ex7">**Example 7 (A Differentiable but Not $$C^1$$ Function)**</ins> The function

$$f(x) = \begin{cases} x^2 \sin(1/x) & (x \neq 0) \\ 0 & (x = 0) \end{cases}$$

is differentiable at every point. For $$x \neq 0$$, by the product rule and the chain rule $$f'(x) = 2x\sin(1/x) - \cos(1/x)$$, and at $$0$$ the difference quotient is $$x\sin(1/x) \to 0$$ so $$f'(0) = 0$$. However, as $$x \to 0$$ we have $$2x\sin(1/x) \to 0$$ but $$\cos(1/x)$$ oscillates infinitely within $$[-1, 1]$$ and has no limit, so $$f'$$ is discontinuous at $$0$$. That is, $$f$$ is differentiable everywhere but its derivative is not continuous, so it is not $$C^1$$ (in the sense of [§Derivatives, ⁋Definition 5](/en/math/calculus/derivatives#def5)).

</div>

Nevertheless, derivatives cannot be discontinuous in just any manner. Even if a derivative is not continuous, it must necessarily assume every intermediate value (*Darboux's theorem*), so it cannot have jump discontinuities, and the discontinuity appearing in [Example 7](#ex7) is not a jump but one caused by oscillation.

## Applications of Differentiation Rules

We close this post by examining how to apply the rules covered so far. First, [Proposition 1](#prop1) can be used to compute the value of a series, albeit in a direction somewhat contrary to the reason we introduced power series.

<div class="example" markdown="1">

<ins id="ex8">**Example 8 (Sum of an Infinite Series)**</ins> Differentiate both sides of the geometric series ([§Infinite Series, ⁋Example 2](/en/math/calculus/series#ex2))

$$\frac{1}{1-x} = \sum_{n=0}^\infty x^n \qquad (\lvert x\rvert < 1)$$

The left-hand side is by the chain rule

$$\left(\frac{1}{1-x}\right)' = 1/(1-x)^2$$

and the right-hand side, applying [Proposition 1](#prop1), is $$\sum_{n\geq 1} n x^{n-1}$$, so

$$\sum_{n=1}^\infty n x^{n-1} = \frac{1}{(1-x)^2} \qquad (\lvert x\rvert < 1)$$

and multiplying both sides by $$x$$ gives

$$\sum_{n\geq 1} n x^n = \frac{x}{(1-x)^2}$$

For example, substituting $$x = 1/2$$, we can also compute the sum of the series $$\sum_{n\geq 1} n/2^n = 2$$.

</div>

The second application is a result more fitting to the category of calculus, actually telling us rules for differentiating a given function.

<div class="example" markdown="1">

<ins id="ex9">**Example 9 (Various Differentiation Rules)**</ins> When an equation determines $$y$$ as a function of $$x$$, to find $$y'$$ it is often inefficient or leads to an unclean derivative to obtain an explicit expression of the form $$y=...$$. In such situations, viewing $$y$$ as a function of $$x$$ and differentiating both sides, then solving for $$y'$$, is called *implicit differentiation*. For example, differentiating both sides of the unit circle $$x^2 + y^2 = 1$$ gives

$$2x + 2y\,y' = 0$$

so we obtain $$y' = -x/y$$, and thus we can find the slope of the tangent line at a given point $$(x_0,y_0)$$.

For functions with a variable in the exponent, it is convenient to use *logarithmic differentiation*, taking the logarithm of both sides and then differentiating. For example, for $$y = x^x$$ ($$x > 0$$), differentiating both sides of $$\ln y = x\ln x$$ and using $$(\ln y)' = y'/y$$ and the product rule gives

$$\frac{y'}{y} = \ln x + 1 \quad\Longrightarrow\quad y' = x^x(\ln x + 1)$$

</div>
