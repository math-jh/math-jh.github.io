---
title: "Continuous Functions"
description: "This post defines continuity of a function using limits and explores the algebraic operations and composition of continuous functions. It also covers the extreme value theorem and the intermediate value theorem, which are fundamental properties of continuous functions on closed intervals."
excerpt: "Definition of continuity and properties of continuous functions: extreme value and intermediate value theorems"

categories: [Math / Calculus]
permalink: /en/math/calculus/continuity
sidebar: 
    nav: "calculus-en"

date: 2026-06-19
weight: 2

drift_needed: true
translated_at: 2026-07-11T03:02:55+00:00
translation_source: kimi-cli
---
We have already defined limits rigorously in [§Limits of Functions](/en/math/calculus/functions_and_limits), so we now define continuity on top of them.

## Definition of Continuity

Intuitively, a continuous function is one that is "connected without breaks," but the tools needed to make this precise are already at hand in the form of limits.

::: Definition 1
A function $$f$$ is said to be *continuous* at a point $$a$$ in its domain if

$$\lim_{x \to a} f(x) = f(a)$$

holds. If $$f$$ is continuous at every point of its domain, we call $$f$$ a *continuous function*.
:::

Rewriting this in the $$\epsilon$$-$$\delta$$ language, for any $$\epsilon > 0$$ there exists some $$\delta > 0$$ such that

$$\lvert x - a\rvert < \delta\Rightarrow\lvert f(x) - f(a)\rvert < \epsilon$$

holds. Here the condition $$0 < \lvert x-a\rvert$$ excluding $$x = a$$ has disappeared, because when $$x = a$$ we have $$\lvert f(a)-f(a)\rvert = 0 < \epsilon$$ automatically, so there is no need to exclude it.

Unpacking this definition, we see that three things must all be satisfied for continuity to hold.

1. $$f(a)$$ is defined. 
2. The limit $$\lim_{x\to a} f(x)$$ exists.
3. The two values above are equal.

The type of discontinuity depends on which of these conditions fails; we will return to this after examining some basic properties of continuous functions.

## Operations on Continuous Functions

Since continuity is the statement that the limit value equals the function value, [§Limits of Functions, ⁋Proposition 5](/en/math/calculus/functions_and_limits#prop5) carries over directly as operations on continuous functions.

::: Proposition 2
If $$f$$ and $$g$$ are continuous at $$a$$, then $$f+g$$, $$cf$$ (where $$c$$ is a constant), and $$fg$$ are also continuous at $$a$$; and if $$g(a) \neq 0$$, then $$f/g$$ is continuous at $$a$$ as well. Moreover, if $$f$$ is continuous at $$a$$ and $$g$$ is continuous at $$f(a)$$, then the composite function $$g \circ f$$ is continuous at $$a$$.
:::

::: Proof
Only the composite function case is new. Let any $$\epsilon > 0$$ be given. Since $$g$$ is continuous at $$b := f(a)$$, there exists some $$\eta > 0$$ such that

$$\lvert y - b\rvert < \eta\Rightarrow\lvert g(y) - g(b)\rvert < \epsilon$$

holds. Again, since $$f$$ is continuous at $$a$$, for this $$\eta$$ there exists a corresponding $$\delta > 0$$ such that

$$\lvert x-a\rvert < \delta\Rightarrow\lvert f(x) - b\rvert < \eta$$

holds. Chaining the two steps, when $$\lvert x-a\rvert < \delta$$ we have $$y = f(x)$$ satisfying $$\lvert y - b\rvert < \eta$$, and therefore $$\lvert g(f(x)) - g(f(a))\rvert < \epsilon$$.
:::

We can verify that constant functions and the identity function $$f(x)=x$$ are continuous. Hence, by repeatedly taking sums and products of these, any polynomial is continuous; and by further taking quotients, any rational function is continuous everywhere except where its denominator is zero. Here is a slightly less obvious example of a continuous function.

::: Example 3
Let us show that the trigonometric function $$\sin x$$ is continuous at every point of its domain. From the sum-to-product formulas for trigonometric functions, we know that

$$\lvert \sin x - \sin a\rvert= \left\lvert 2\cos\frac{x+a}{2}\sin\frac{x-a}{2}\right\rvert \leq 2\left\lvert \sin\frac{x-a}{2}\right\rvert$$

always holds. Now applying the inequality $$\lvert \sin t\rvert \leq \lvert t\rvert$$ obtained in [§Limits of Functions, ⁋Example 10](/en/math/calculus/functions_and_limits#ex10), we get for any $$a \in \mathbb{R}$$

$$\lvert \sin x - \sin a\rvert\leq\lvert x-a\rvert$$

so it suffices to take $$\delta = \epsilon$$.
:::

Now the $$\cos$$ function can be obtained by translating the $$\sin$$ function, so it is continuous by [Proposition 2](#prop2); and consequently, by the same kind of argument as above, $$\tan x$$ is also continuous everywhere except where its denominator is zero.

## Properties of Continuous Functions on a Closed Interval

On the other hand, one useful property of continuous functions is that if $$f$$ is continuous at $$a$$ and $$f(a) > 0$$, then by taking $$\delta$$ corresponding to $$\epsilon = f(a)/2$$ we can ensure that $$f$$ remains positive in the $$\delta$$-neighborhood of $$a$$. This simple fact is useful in itself, and it also generalizes to the following theorems.

::: Theorem 4 (Extreme Value Theorem)
If $$f$$ is continuous on a closed interval $$[a,b]$$, then $$f$$ attains a maximum and a minimum on $$[a,b]$$. That is, there exist $$c, d \in [a,b]$$ such that $$f(d) \leq f(x) \leq f(c)$$ for all $$x \in [a,b]$$.
:::

::: Theorem 5 (Intermediate Value Theorem)
If $$f$$ is continuous on a closed interval $$[a,b]$$ and $$f(a) \neq f(b)$$, then for any value $$y$$ between $$f(a)$$ and $$f(b)$$ there exists $$c \in (a,b)$$ such that $$f(c) = y$$.
:::

The proofs of these two theorems essentially require the *completeness* of the real numbers.

Finally, it is convenient to classify the ways in which continuity can fail, as this helps describe the behavior of functions.

::: Definition 6 (Classification of Discontinuities)
When a function $$f$$ is discontinuous at a point $$a$$, we divide the situation into three cases according to the behavior of the two one-sided limits $$\lim_{x\to a^\pm} f(x)$$.

1. *Removable discontinuity*: the limit $$\lim_{x\to a} f(x)$$ exists but is different from $$f(a)$$, or $$f(a)$$ is undefined. Redefining (or defining) $$f(a)$$ to be the limit value restores continuity. Example: $$(x^2-1)/(x-1)$$ at $$a=1$$.
2. *Jump discontinuity*: both one-sided limits exist but are different. Example: $$\lvert x\rvert/x$$ at $$a=0$$.
3. *Essential discontinuity*: at least one of the one-sided limits does not exist (oscillates or diverges). Example: $$\sin(1/x)$$ at $$a=0$$.
:::

## Monotone Functions and Inverse Functions

An important application of the Intermediate Value Theorem is the continuity of inverse functions. A function is said to be *strictly increasing* (or strictly decreasing) on an interval if $$x_1 < x_2$$ always implies $$f(x_1) < f(x_2)$$ (or $$>$$); such functions are collectively called *strictly monotone*. A strictly monotone function is obviously injective, so it has an inverse on its image.

::: Proposition 7
If $$f$$ is continuous and strictly monotone on an interval $$I$$, then its image $$J = f(I)$$ is also an interval, and the inverse function $$f^{-1} : J \to I$$ is likewise a continuous strictly monotone function.
:::

::: Proof
Suppose $$f$$ is strictly increasing. That $$J$$ is an interval follows from the Intermediate Value Theorem: since $$f$$ takes every value between any two of its values, there are no gaps in $$J$$. That the inverse function $$f^{-1}$$ is strictly increasing follows immediately from the strict increasingness of $$f$$. To show continuity, if $$f^{-1}$$ had a point of discontinuity, then a jump would occur in the image of $$f^{-1}$$, making $$I$$ not an interval; but this contradicts the fact that $$I$$ is an interval. Therefore $$f^{-1}$$ is continuous.
:::

For instance, $$f(x) = x^n$$ (for $$x \geq 0$$, with $$n$$ a natural number) is continuous and strictly increasing, so its inverse, the $$n$$th root $$\sqrt[n]{x}$$, is also continuous. Likewise, the inverse trigonometric functions, which are inverses of suitably restricted trigonometric functions, are all continuous. With this we have assembled the basic properties of continuous functions.
