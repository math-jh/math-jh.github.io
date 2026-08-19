---
title: "Continuous Functions"
description: "We define continuity of a function using limits, and discuss the arithmetic and composition of continuous functions, along with the extreme value theorem and the intermediate value theorem for functions on closed intervals."
excerpt: "Definition of continuity and properties of continuous functions: extreme and intermediate value theorems"

categories: [Math / Calculus]
permalink: /en/math/calculus/continuity
sidebar: 
    nav: "calculus-en"

date: 2026-06-19
weight: 2
translated_at: 2026-08-19T04:45:05+00:00
translation_source: kimi-cli
last_polished_at: 2026-08-19T04:45:05+00:00
---
We have already rigorously defined limits in [§Limits of Functions](/en/math/calculus/functions_and_limits), so we now define continuity on top of that.

## Definition of Continuity

Intuitively, a continuous function is one that is "connected without breaks," but the tool needed to make this precise is already at hand in the form of limits.

::: Definition 1
A function $f$ is said to be *continuous* at a point $a$ in its domain if

$$\lim_{x \rightarrow a} f(x) = f(a)$$

holds. If $f$ is continuous at every point of its domain, we call $f$ a *continuous function*.
:::

Writing this out in $\epsilon$-$\delta$ language, for every $\epsilon > 0$ there exists some $\delta > 0$ such that for all $x$ in the domain,

$$\lvert x - a\rvert < \delta\implies\lvert f(x) - f(a)\rvert < \epsilon$$

holds. Note that the condition $0 < \lvert x-a\rvert$ excluding $x = a$ has disappeared; this is because when $x = a$, we automatically have $\lvert f(a)-f(a)\rvert = 0 < \epsilon$, so there is no need to exclude it.

If we read this with $x$ restricted to the domain, continuity still makes sense even when the domain does not contain an entire neighborhood of $a$. For example, if the domain is a closed interval $[a,b]$, continuity at the endpoint $a$ means the right-hand limit $\lim_{x\rightarrow a^+} f(x) = f(a)$ as in [§Limits of Functions, ⁋Definition 12](/en/math/calculus/functions_and_limits#def12), and continuity at the endpoint $b$ means the left-hand limit $\lim_{x\rightarrow b^-} f(x) = f(b)$. Whenever we speak of continuity on a closed interval $[a,b]$ or on an interval $I$ below, we always mean this.

Unpacking this definition, we see that for continuity to hold, all three of the following must be satisfied:

1. $f(a)$ is defined.
2. The limit $\lim_{x\rightarrow a} f(x)$ exists.
3. These two values are equal.

Depending on which of these conditions fails, different types of discontinuity arise; we will return to this after examining the basic properties of continuous functions.

## Operations on Continuous Functions

Since continuity is the statement that the limit value coincides with the function value, [§Limits of Functions, ⁋Proposition 5](/en/math/calculus/functions_and_limits#prop5) carries over directly to operations on continuous functions.

::: Proposition 2
If $f$ and $g$ are continuous at $a$, then $f+g$, $cf$ (where $c$ is a constant), and $fg$ are also continuous at $a$, and if $g(a) \neq 0$, then $f/g$ is continuous at $a$ as well. Moreover, if $f$ is continuous at $a$ and $g$ is continuous at $f(a)$, then the composite function $g \circ f$ is continuous at $a$.
:::

::: Proof
Only the composite function is new. Let an arbitrary $\epsilon > 0$ be given. Since $g$ is continuous at $b := f(a)$, there exists some $\eta > 0$ such that

$$\lvert y - b\rvert < \eta\implies\lvert g(y) - g(b)\rvert < \epsilon$$

holds. Again, since $f$ is continuous at $a$, for this $\eta$ there exists a corresponding $\delta > 0$ such that

$$\lvert x-a\rvert < \delta\implies\lvert f(x) - b\rvert < \eta$$

holds. Chaining these two steps, if $\lvert x-a\rvert < \delta$, then $y = f(x)$ satisfies $\lvert y - b\rvert < \eta$, so $\lvert g(f(x)) - g(f(a))\rvert < \epsilon$.
:::

We can verify that constant functions and the linear function $f(x)=x$ are continuous. Therefore, by repeated addition and multiplication, any polynomial function is continuous, and by taking quotients, any rational function is continuous everywhere except where the denominator is zero. The following is a slightly less obvious example of a continuous function.

::: Example 3
Let us show that the trigonometric function $\sin x$ is continuous at every point of its domain. From the sum-to-product formula for trigonometric functions, we know that

$$\lvert \sin x - \sin a\rvert= \left\lvert 2\cos\frac{x+a}{2}\sin\frac{x-a}{2}\right\rvert \leq 2\left\lvert \sin\frac{x-a}{2}\right\rvert$$

always holds. On the other hand, the inequality $\sin t \leq t$ ($0 < t < \pi/2$) obtained in [§Limits of Functions, ⁋Example 10](/en/math/calculus/functions_and_limits#ex10) extends to the inequality $\lvert \sin t\rvert \leq \lvert t\rvert$ for all real $t$, because when $t \geq \pi/2$ we have $\lvert \sin t\rvert \leq 1 < t$, and $\sin(-t) = -\sin t$. Applying this, for any $a \in \mathbb{R}$ we have

$$\lvert \sin x - \sin a\rvert\leq\lvert x-a\rvert$$

so we may simply take $\delta = \epsilon$.
:::

Now the $\cos$ function can be obtained by translating the $\sin$ function, so it is continuous by [Proposition 2](#prop2), and hence by the argument above, $\tan x$ is also continuous everywhere except where the denominator is zero.

## Properties of Continuous Functions on a Closed Interval

Meanwhile, one useful property of continuous functions is that if $f$ is continuous at $a$ and $f(a) > 0$, then by taking $\delta$ corresponding to $\epsilon = f(a)/2$, the function $f$ remains positive in the $\delta$-neighborhood of $a$. This simple fact is useful in itself, and it also generalizes to the following theorems.

::: Theorem 4 (Extreme Value Theorem)
If $f$ is continuous on a closed interval $[a,b]$, then $f$ attains a maximum and a minimum on $[a,b]$. That is, there exist $c, d \in [a,b]$ such that $f(d) \leq f(x) \leq f(c)$ for all $x \in [a,b]$.
:::

::: Theorem 5 (Intermediate Value Theorem)
If $f$ is continuous on a closed interval $[a,b]$ and $f(a) \neq f(b)$, then for any value $y$ between $f(a)$ and $f(b)$, there exists $c \in (a,b)$ such that $f(c) = y$.
:::

The proofs of these two theorems essentially require the *completeness* of the real numbers.

In [Theorem 5](#thm5), the word "between" means excluding the two endpoint values $f(a)$ and $f(b)$, and accordingly the conclusion gives $c$ in the open interval $(a,b)$. If one wishes to include the case where $y$ equals one of the two endpoint values or where $f(a) = f(b)$, one simply finds $c \in [a,b]$ with $f(c) = y$, and then $c$ can be taken to be $a$ or $b$.

Finally, it is convenient to classify the ways in which continuity can fail when describing properties of functions. The jump discontinuity of $\lvert x\rvert/x$ mentioned in [§Limits of Functions](/en/math/calculus/functions_and_limits) is one such type.

::: Definition 6 (Classification of Discontinuities)
Suppose a function $f$ is defined on some deleted neighborhood of $a$ and is not continuous at $a$, or $f(a)$ is not defined. Then this discontinuity is divided into the following three types according to the existence and agreement of the two one-sided limits $\lim_{x\rightarrow a^\pm} f(x)$.

1. *removable discontinuity*: the limit $\lim_{x\rightarrow a} f(x)$ exists but differs from $f(a)$, or $f(a)$ is not defined. If $f(a)$ is (re)defined to be the limit value, the function becomes continuous. Example: $(x^2-1)/(x-1)$ ($a=1$).
2. *jump discontinuity*: both one-sided limits exist but are different. Example: $\lvert x\rvert/x$ ($a=0$).
3. *essential discontinuity*: at least one of the one-sided limits does not exist (oscillating or diverging). Example: $\sin(1/x)$ ($a=0$).
:::

## Monotone Functions and Inverse Functions

One important application of the intermediate value theorem is the continuity of inverse functions. A function is said to be *strictly increasing* (or *strictly decreasing*) on an interval if $x_1 < x_2$ always implies $f(x_1) < f(x_2)$ (or $>$), and such functions are collectively called *strictly monotone*. A strictly monotone function is obviously injective, so it has an inverse on its image.

::: Proposition 7
If $f$ is continuous and strictly monotone on an interval $I$, then its image $J = f(I)$ is also an interval, and the inverse function $f^{-1} : J \rightarrow I$ is also a continuous strictly monotone function.
:::

::: Proof
It suffices to consider the case where $f$ is strictly increasing; the strictly decreasing case follows by reversing all inequalities and repeating the same argument. That $J$ is an interval follows from the intermediate value theorem: since $f$ takes every value between two of its values, $J$ has no gaps. That $f^{-1}$ is strictly increasing follows immediately from the strict increasingness of $f$.

To show continuity, let $y_0 \in J$ and $x_0 = f^{-1}(y_0)$, and let $\epsilon > 0$ be given. If there are points of $I$ on both sides of $x_0$, then since $I$ is an interval we can choose $x_1, x_2 \in I$ with $x_0 - \epsilon < x_1 < x_0 < x_2 < x_0 + \epsilon$. Since $f$ is strictly increasing, $y_1 := f(x_1) < y_0 < f(x_2) =: y_2$, and setting $\delta = \min(y_0 - y_1, y_2 - y_0) > 0$, every $y \in J$ with $\lvert y - y_0\rvert < \delta$ satisfies $y_1 < y < y_2$. By the strict increasingness of $f^{-1}$, we have $x_1 < f^{-1}(y) < x_2$, so $\lvert f^{-1}(y) - x_0\rvert < \epsilon$. If $x_0$ is an endpoint of $I$ so that points of $I$ lie on only one side, we simply take only the corresponding one of $x_1$ and $x_2$ and repeat the same argument; the opposite inequality follows automatically from $x_0$ being the minimum or maximum of $I$.
:::

For example, $f(x) = x^n$ ($x \geq 0$, $n$ a natural number) is continuous and strictly increasing, so its inverse, the $n$th root $\sqrt[n]{x}$, is also continuous. Likewise, inverse trigonometric functions, obtained by restricting trigonometric functions, are all continuous. Thus we have established the basic properties of continuous functions.

---

**References**

**[Ste]** J. Stewart, *Calculus*, 8th ed., Cengage Learning, 2016.  
**[Kim]** 김홍종, *미적분학 1·2*, 제3개정판, 서울대학교출판문화원, 2020.
