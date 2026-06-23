---
title: "Differentiation"
description: "We derive the derivative of the exponential function via termwise differentiation of power series, and summarize the derivatives of trigonometric functions along with the product, chain, quotient, and inverse function rules. This provides a systematic framework for differentiating functions built from elementary functions."
excerpt: "Termwise differentiation of power series, derivatives of elementary functions, product, quotient, and chain rules"

categories: [Math / Calculus]
permalink: /en/math/calculus/differentiation_rules
sidebar: 
    nav: "calculus-en"

date: 2026-06-22
weight: 7
translated_at: 2026-06-22T21:00:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-22T21:00:02+00:00
---
We covered the definition of differentiation and its basic properties in [§Derivatives](/en/math/calculus/derivatives). In this post, we treat derivatives of concrete functions and differentiation rules that apply to general functions.

## Term-by-Term Differentiation of Power Series

First, for any natural number $$n$$, we can verify that the derivative of $$x^n$$ at a point $$a$$ is given by

$$\lim_{h\rightarrow 0}\frac{(a+h)^n-a^n}{h}=\lim_{h\rightarrow 0}\frac{na^{n-1}h+\ldots}{h}=na^{n-1}$$

and similarly, for a negative integer $$n = -m$$, after putting the difference quotient over a common denominator we have

$$\frac{(a+h)^{-m} - a^{-m}}{h} = -\frac{(a+h)^m - a^m}{h}\cdot\frac{1}{(a+h)^ma^m}$$

so that ultimately $$(x^n)' = n x^{n-1}$$ holds for every integer $$n$$.

On the other hand, by linearity a polynomial is differentiated term by term, so this also gives the differentiation rule for an arbitrary polynomial function. However, in general it is not obvious that differentiation can be distributed term by term in an <em>infinite</em> sum; the following proposition guarantees that this is permitted for power series.

<div class="proposition" markdown="1">

<ins id="prop1">**Proposition 1 (Term-by-Term Differentiation of Power Series)**</ins> If a power series $$f(x) = \sum_{n=0}^\infty c_n x^n$$ has radius of convergence $$R > 0$$, then $$f$$ is differentiable for $$\lvert x\rvert < R$$ and

$$f'(x) = \sum_{n=1}^\infty n\,c_n x^{n-1}$$

and the radius of convergence of this series is also $$R$$.

</div>

That the radius of convergence of the series on the right-hand side is $$R$$ itself follows from the fact that $$n^{1/n}$$ converges to $$1$$ as $$n\rightarrow \infty$$, but our tools are insufficient to rigorously justify that this actually equals $$f'(x)$$, so we shall accept this and move on.

## Derivatives of Trigonometric and Exponential Functions

Before looking at differentiation rules in earnest, we derive the derivatives of various functions.

First, the exponential function was defined in [§Power Series, ⁋Example 3](/en/math/calculus/power_series#ex3) by $$e^x = \sum_{n\geq 0} x^n/n!$$. Applying [Proposition 1](#prop1), its derivative is the sum of the term-by-term derivatives

$$(e^x)' = \sum_{n=1}^\infty n\,\frac{x^{n-1}}{n!} = \sum_{n=1}^\infty \frac{x^{n-1}}{(n-1)!} = \sum_{m=0}^\infty \frac{x^m}{m!} = e^x$$

so the exponential function is invariant under differentiation. In high school this was obtained from the limit

$$\lim_{h\to 0}(e^h-1)/h = 1$$

Trigonometric functions will also soon be written as power series, but for now we shall derive them using the same two limits as in high school:

$$\lim_{h \to 0} \frac{\sin h}{h} = 1, \qquad \lim_{h \to 0} \frac{1 - \cos h}{h} = 0$$

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2 (Derivatives of Trigonometric Functions)**</ins> At every point $$(\sin x)' = \cos x$$ and $$(\cos x)' = -\sin x$$.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

Using the addition formula $$\sin(x+h) = \sin x\cos h + \cos x \sin h$$ to split the difference quotient, we have

$$\frac{\sin(x+h) - \sin x}{h} = \sin x \cdot \frac{\cos h - 1}{h} + \cos x \cdot \frac{\sin h}{h}$$

and as $$h \to 0$$, by the two limits above this converges to $$\sin x \cdot 0 + \cos x \cdot 1 = \cos x$$. The derivative of $$\cos x$$ is obtained in the same way.

</details>

## Various Differentiation Rules

Now we define differentiation rules that apply to general forms. In [§Derivatives, ⁋Proposition 4](/en/math/calculus/derivatives#prop4) we saw that differentiation behaves well with respect to constant multiples and addition, but it does not simply distribute over products.

<div class="proposition" markdown="1">

<ins id="prop3">**Proposition 3 (Product Rule)**</ins> If $$f, g$$ are differentiable at $$a$$, then $$fg$$ is also differentiable at $$a$$ and

$$(fg)'(a) = f'(a)\,g(a) + f(a)\,g'(a)$$

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

Adding and subtracting the same term in the difference quotient gives

$$\frac{f(a+h)g(a+h) - f(a)g(a)}{h} = \frac{f(a+h)-f(a)}{h}\,g(a+h) + f(a)\,\frac{g(a+h)-g(a)}{h}$$

As $$h \to 0$$, the difference quotient in the first term converges to $$f'(a)$$, and $$g(a+h)$$ converges to $$g(a)$$ by the continuity of $$g$$ ([§Derivatives, ⁋Proposition 2](/en/math/calculus/derivatives#prop2)), while the difference quotient in the second term converges to $$g'(a)$$; hence by the limit laws ([§Limits of Functions, ⁋Proposition 5](/en/math/calculus/functions_and_limits#prop5)) the sum converges to $$f'(a)g(a) + f(a)g'(a)$$.

</details>

The most widely used rule is the differentiation of composite functions.

<div class="proposition" markdown="1">

<ins id="thm4">**Theorem 4 (Chain Rule)**</ins> If $$f$$ is differentiable at $$a$$ and $$g$$ is differentiable at $$b = f(a)$$, then the composition $$g \circ f$$ is also differentiable at $$a$$ and

$$(g \circ f)'(a) = g'(f(a))\,f'(a)$$

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

We transfer the differentiability of $$g$$ to the auxiliary function

$$\varphi(y) = \begin{cases} \frac{g(y) - g(b)}{y - b}, & y \neq b,\\[1mm] g'(b), & y = b \end{cases}$$

By the definition of differentiability, $$\varphi$$ is continuous at $$b$$, and for every $$y$$ we have $$g(y) - g(b) = \varphi(y)(y - b)$$. Substituting $$y = f(a+h)$$ gives

$$\frac{g(f(a+h)) - g(f(a))}{h} = \varphi(f(a+h))\,\frac{f(a+h) - f(a)}{h}$$

and as $$h \to 0$$, by the continuity of $$f$$ we have $$\varphi(f(a+h)) \to \varphi(b) = g'(b)$$, while the second factor converges to $$f'(a)$$, so the limit is $$g'(f(a))f'(a)$$.

</details>

The quotient rule now follows as a corollary of the product rule and the chain rule.

<div class="proposition" markdown="1">

<ins id="cor5">**Corollary 5 (Quotient Rule)**</ins> If $$f, g$$ are differentiable at $$a$$ and $$g(a) \neq 0$$, then $$f/g$$ is also differentiable at $$a$$ and

$$\left(\frac{f}{g}\right)'(a) = \frac{f'(a)\,g(a) - f(a)\,g'(a)}{g(a)^2}$$

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

Defining the function $$h(t)=1/t$$, we have $$1/g =h \circ g$$, and by the differentiation of integer powers $$h'(t)=-1/t^2$$, so by the chain rule $$(1/g)'(a) = -g(a)^{-2}g'(a)$$. Applying the product rule to $$f/g = f\cdot(1/g)$$ now gives

$$\left(\frac{f}{g}\right)'(a) = \frac{f'(a)}{g(a)} - \frac{f(a)g'(a)}{g(a)^2} = \frac{f'(a)g(a) - f(a)g'(a)}{g(a)^2}$$

</details>

For example, from $$\tan x = \sin x/\cos x$$ we obtain $$(\tan x)' = (\cos^2 x + \sin^2 x)/\cos^2 x = \sec^2 x$$, and similarly $$(\cot x)' = -\csc^2 x$$.

Finally, if a function is monotone, the derivative of its inverse function is obtained immediately without a separate calculation.

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6 (Differentiation of Inverse Functions)**</ins> Let $$f$$ be a continuous monotone function on an interval having an inverse function $$f^{-1}$$, and suppose $$f$$ is differentiable at $$a$$ with $$f'(a) \neq 0$$. Then $$f^{-1}$$ is differentiable at $$b = f(a)$$ and

$$(f^{-1})'(b) = \frac{1}{f'(a)} = \frac{1}{f'(f^{-1}(b))}$$

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

Accepting that $$f^{-1}$$ is differentiable at $$b$$, we differentiate both sides of the identity $$f(f^{-1}(y)) = y$$ by the chain rule to obtain $$f'(f^{-1}(b))\cdot(f^{-1})'(b) = 1$$, and since $$f'(a) \neq 0$$ the proof is complete.

</details>

With this we can also proceed to differentiate the inverses of the functions examined above. For example, for the inverse $$\ln$$ of $$e^x$$, since $$(e^x)' = e^x$$ we have $$(\ln y)' = 1/e^{\ln y} = 1/y$$, and for the inverse $$\arcsin$$ of $$\sin$$ restricted to $$(-\pi/2, \pi/2)$$, since $$f'(x) = \cos x = \sqrt{1 - \sin^2 x} > 0$$ we have

$$(\arcsin y)' = \frac{1}{\sqrt{1 - y^2}} \qquad (\lvert y\rvert < 1)$$

and in the same way $$(\arctan y)' = 1/(1 + y^2)$$.

On the other hand, once we have obtained the derivative using the rules developed so far, we may ask whether that derivative is again continuous; even a function differentiable everywhere can have a discontinuous derivative.

<div class="example" markdown="1">

<ins id="ex7">**Example 7 (A Function Differentiable but Not $$C^1$$)**</ins> The function

$$f(x) = \begin{cases} x^2 \sin(1/x) & (x \neq 0) \\ 0 & (x = 0) \end{cases}$$

is differentiable at every point. For $$x \neq 0$$, by the product rule and the chain rule $$f'(x) = 2x\sin(1/x) - \cos(1/x)$$, and at $$0$$ the difference quotient is $$x\sin(1/x) \to 0$$, so $$f'(0) = 0$$. However, as $$x \to 0$$ we have $$2x\sin(1/x) \to 0$$ but $$\cos(1/x)$$ oscillates infinitely often between $$[-1, 1]$$ and has no limit, so $$f'$$ is discontinuous at $$0$$. That is, $$f$$ is differentiable everywhere but its derivative is not continuous, so it is not $$C^1$$ (in the sense of [§Derivatives, ⁋Definition 5](/en/math/calculus/derivatives#def5)).

</div>

Nevertheless, a derivative cannot be discontinuous in just any manner. Even if a derivative is not continuous, it necessarily takes every intermediate value (*Darboux's theorem*), so it cannot have a jump discontinuity, and the discontinuity exhibited in [Example 7](#ex7) is not a jump but one caused by oscillation.

## Applications of Differentiation Rules

Finally, we close this post by examining how to apply the rules we have developed so far. First, [Proposition 1](#prop1) can be used to evaluate series, though this is somewhat contrary to the reason we introduced power series.

<div class="example" markdown="1">

<ins id="ex8">**Example 8 (Sum of an Infinite Series)**</ins> Differentiate both sides of the geometric series ([§Infinite Series, ⁋Theorem 6](/en/math/calculus/series#thm6))

$$\frac{1}{1-x} = \sum_{n=0}^\infty x^n \qquad (\lvert x\rvert < 1)$$

The left-hand side is, by the chain rule,

$$\left(\frac{1}{1-x}\right)' = 1/(1-x)^2$$

and applying [Proposition 1](#prop1) to the right-hand side gives $$\sum_{n\geq 1} n x^{n-1}$$, so

$$\sum_{n=1}^\infty n x^{n-1} = \frac{1}{(1-x)^2} \qquad (\lvert x\rvert < 1)$$

and multiplying both sides by $$x$$ we obtain

$$\sum_{n\geq 1} n x^n = \frac{x}{(1-x)^2}$$

For example, substituting $$x = 1/2$$, we can also compute the sum of the series $$\sum_{n\geq 1} n/2^n = 2$$.

</div>

The second application is a result more fitting to the category of calculus, actually telling us the rule for differentiating a given function.

<div class="example" markdown="1">

<ins id="ex9">**Example 9 (Various Differentiation Rules)**</ins> When an equation determines $$y$$ as a function of $$x$$, it is often inefficient or leads to an inelegant differentiation to find an explicit expression of the form $$y=...$$. In such a situation, treating $$y$$ as a function of $$x$$ and differentiating both sides, then solving for $$y'$$, is called *implicit differentiation*. For example, differentiating both sides of the unit circle $$x^2 + y^2 = 1$$ gives

$$2x + 2y\,y' = 0$$

so we obtain $$y' = -x/y$$, and thus we can find the slope of the tangent line at a given point $$(x_0,y_0)$$.

For functions with a variable in the exponent, it is convenient to use *logarithmic differentiation*, taking the logarithm of both sides before differentiating. For example, for $$y = x^x$$ ($$x > 0$$), differentiating both sides of $$\ln y = x\ln x$$ and using $$(\ln y)' = y'/y$$ together with the product rule gives

$$\frac{y'}{y} = \ln x + 1 \quad\Longrightarrow\quad y' = x^x(\ln x + 1)$$

</div>
