---
title: "Continuous Functions"
description: "We define continuity of a function using limits and explore the arithmetic and composition of continuous functions. We also cover the extreme value theorem and the intermediate value theorem, which are fundamental properties of continuous functions on a closed interval."
excerpt: "Definition of continuity and properties of continuous functions — the extreme and intermediate value theorems"

categories: [Math / Calculus]
permalink: /en/math/calculus/continuity
sidebar: 
    nav: "calculus-en"

date: 2026-06-19
weight: 2
translated_at: 2026-06-19T16:30:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-19T16:30:02+00:00
---
We rigorously defined limits in [§Functions and Limits of Sequences](/en/math/calculus/functions_and_limits), and the natural next step is continuity.

## Definition of Continuity

Essentially, the only part of the definition of continuity that was not rigorous was the limit part, and since we have already rigorously defined limits in the previous post, the following definition is essentially free.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> A function $$f$$ is said to be *continuous* at a point $$a$$ in its domain if

$$\lim_{x \to a} f(x) = f(a)$$

holds. If $$f$$ is continuous at every point in its domain, we call $$f$$ a *continuous function*.

</div>

Unpacked, this means that for any $$\epsilon > 0$$, there exists some $$\delta > 0$$ such that

$$\lvert x - a\rvert < \delta\Rightarrow\lvert f(x) - f(a)\rvert < \epsilon$$

holds. Here the condition $$0 < \lvert x-a\rvert$$ excluding $$x = a$$ has disappeared, because when $$x = a$$, we have $$\lvert f(a)-f(a)\rvert = 0 < \epsilon$$ automatically, so there is no need to exclude it.

Taking this definition apart, we see that for continuity to hold, three conditions must all be satisfied:

1. $$f(a)$$ is defined.
2. The limit $$\lim_{x\to a} f(x)$$ exists.
3. The two values above are equal to each other.

Depending on which of these conditions fails, the type of discontinuity varies; we will return to this after examining the basic properties of continuous functions.

## Operations on Continuous Functions

First, the following proposition is an immediate consequence of [§Functions and Limits, ⁋Proposition 4](/en/math/calculus/functions_and_limits#prop4).

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> If $$f$$ and $$g$$ are continuous at $$a$$, then $$f+g$$, $$cf$$ (where $$c$$ is a constant), and $$fg$$ are also continuous at $$a$$, and if $$g(a) \neq 0$$, then $$f/g$$ is continuous at $$a$$ as well. Moreover, if $$f$$ is continuous at $$a$$ and $$g$$ is continuous at $$f(a)$$, then the composite function $$g \circ f$$ is continuous at $$a$$.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

Only the composition is a new result. Let an arbitrary $$\epsilon > 0$$ be given. Since $$g$$ is continuous at $$b := f(a)$$, there exists some $$\eta > 0$$ such that

$$\lvert y - b\rvert < \eta\Rightarrow\lvert g(y) - g(b)\rvert < \epsilon$$

holds. Again, since $$f$$ is continuous at $$a$$, there exists a corresponding $$\delta > 0$$ for this $$\eta$$ such that

$$\lvert x-a\rvert < \delta\Rightarrow\lvert f(x) - b\rvert < \eta$$

holds. Chaining the two steps, when $$\lvert x-a\rvert < \delta$$, we have $$y = f(x)$$ satisfying $$\lvert y - b\rvert < \eta$$, and therefore $$\lvert g(f(x)) - g(f(a))\rvert < \epsilon$$.

</details>

We can verify that constant functions and the identity function $$f(x)=x$$ are continuous. Therefore, by repeatedly taking sums and products of these, any polynomial is continuous, and by further taking quotients, any rational function is continuous everywhere except at points where the denominator is zero. The following is a slightly less obvious example of a continuous function.

<div class="example" markdown="1">

<ins id="ex3">**Example 3**</ins> Let us show that the sine function $$\sin x$$ is continuous at every point in its domain. From the addition formula for sine, we know that

$$\lvert \sin x - \sin a\rvert= \left\lvert 2\cos\frac{x+a}{2}\sin\frac{x-a}{2}\right\rvert \leq 2\left\lvert \sin\frac{x-a}{2}\right\rvert$$

always holds. Now applying the inequality $$\lvert \sin t\rvert \leq \lvert t\rvert$$ obtained in [§Functions and Limits of Sequences, ⁋Example 10](/en/math/calculus/functions_and_limits#ex10), we have for any $$a \in \mathbb{R}$$

$$\lvert \sin x - \sin a\rvert\leq\lvert x-a\rvert$$

holds, so we may take $$\delta = \epsilon$$.

</div>

Now the cosine function can be obtained by translating the sine function, so it is continuous by [Proposition 2](#prop2), and therefore by the same argument as above, $$\tan x$$ is also continuous everywhere except at points where the denominator is zero.

## Properties of Continuous Functions on a Closed Interval

On the other hand, one useful property of continuous functions is that if $$f$$ is continuous at $$a$$ and $$f(a) > 0$$, then taking the $$\delta$$ corresponding to $$\epsilon = f(a)/2$$, we see that $$f$$ is always positive in the $$\delta$$-neighborhood of $$a$$. This simple fact is useful in itself, and is also generalized by the following theorems.

<div class="proposition" markdown="1">

<ins id="thm4">**Theorem 4 (Extreme Value Theorem)**</ins> If $$f$$ is continuous on a closed interval $$[a,b]$$, then $$f$$ attains a maximum and a minimum on $$[a,b]$$. That is, there exist some $$c, d \in [a,b]$$ such that for all $$x \in [a,b]$$, we have $$f(d) \leq f(x) \leq f(c)$$.

</div>

<div class="proposition" markdown="1">

<ins id="thm5">**Theorem 5 (Intermediate Value Theorem)**</ins> If $$f$$ is continuous on a closed interval $$[a,b]$$ and $$f(a) \neq f(b)$$, then for any value $$y$$ between $$f(a)$$ and $$f(b)$$, there exists $$c \in (a,b)$$ such that $$f(c) = y$$.

</div>

The proofs of these two theorems essentially require the *completeness* of the real numbers, so we postpone rigorous proofs until after introducing completeness, to be covered in the analysis category.

Finally, it is convenient to classify the ways in which continuity can fail, as this helps describe the behavior of functions.

<div class="definition" markdown="1">

<ins id="def6">**Definition 6 (Classification of Discontinuities)**</ins> When a function $$f$$ is discontinuous at a point $$a$$, we divide it into the following three cases according to the behavior of the two one-sided limits $$\lim_{x\to a^\pm} f(x)$$.

1. *Removable discontinuity*: The limit $$\lim_{x\to a} f(x)$$ exists but is different from $$f(a)$$, or $$f(a)$$ is undefined. If we (re)define $$f(a)$$ to be the limit value, the function becomes continuous. Example: $$\dfrac{x^2-1}{x-1}$$ ($$a=1$$).
2. *Jump discontinuity*: Both one-sided limits exist but are different from each other. Example: $$\dfrac{\lvert x\rvert}{x}$$ ($$a=0$$).
3. *Essential discontinuity*: At least one of the one-sided limits does not exist (oscillates or diverges). Example: $$\sin\dfrac1x$$ ($$a=0$$).

</div>

## Monotone Functions and Inverse Functions

One important application of the intermediate value theorem is the continuity of inverse functions. A function is said to be *strictly increasing* (or strictly decreasing) on an interval if $$x_1 < x_2$$ always implies $$f(x_1) < f(x_2)$$ (or $$>$$), and such functions are collectively called *strictly monotone*. A strictly monotone function is obviously injective, so it has an inverse function on its image.

<div class="proposition" markdown="1">

<ins id="prop7">**Proposition 7**</ins> If $$f$$ is continuous and strictly monotone on an interval $$I$$, then its image $$J = f(I)$$ is also an interval, and the inverse function $$f^{-1} : J \to I$$ is also a continuous strictly monotone function.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

Suppose $$f$$ is strictly increasing. That $$J$$ is an interval follows from the intermediate value theorem: since $$f$$ takes every value between two of its values, there are no gaps in $$J$$. That the inverse function $$f^{-1}$$ is strictly increasing follows immediately from the strict monotonicity of $$f$$. To show continuity, if $$f^{-1}$$ had a point of discontinuity, there would be a jump in the image of $$f^{-1}$$, making $$I$$ not an interval, which contradicts the fact that $$I$$ is an interval. Therefore $$f^{-1}$$ is continuous.

</details>

For example, $$f(x) = x^n$$ ($$x \geq 0$$, $$n$$ a natural number) is continuous and strictly increasing, so its inverse function, the $$n$$th root $$\sqrt[n]{x}$$, is also continuous. Likewise, inverse trigonometric functions, which are inverses of suitably restricted trigonometric functions, are all continuous. This proposition forms the foundation for establishing the inverse function differentiation formula in [§Differentiation Rules](/en/math/calculus/differentiation_rules).

With this, we have established the basic properties of continuous functions. In the next post, [§Derivatives and Differentiation](/en/math/calculus/derivatives), we define the local rate of change, namely differentiation, for "smooth" functions among continuous functions. There we will see that differentiability is a stronger condition than continuity.
