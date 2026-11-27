---
title: "Continuous Functions"
description: "This post defines the continuity of a function using limits and covers arithmetic operations and compositions of continuous functions, along with key properties of continuous functions on closed intervals: the Extreme Value Theorem and the Intermediate Value Theorem."
excerpt: "Definition of continuity and continuous function properties: Extreme and Intermediate Value Theorems"

categories: [Math / Calculus]
permalink: /en/math/calculus/continuity
sidebar: 
    nav: "calculus-en"

date: 2026-06-19
weight: 2
translated_at: 2026-11-21T07:20:37+00:00
translation_source: antigravity-gemini-3.8-flash-high
last_polished_at: 2026-11-21T23:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
Having rigorously defined limits in [§Limits of Functions](/en/math/calculus/functions_and_limits){: data-lid="a1hts" }, we can define continuity on that basis.

## Definition of Continuity

Intuitively, a continuous function is a function that is *connected without breaks*, and the tool needed to formulate this rigorously is already at hand in the form of limits.

::: Definition 1
A function $f$ is *continuous* at a point $a$ in its domain if

$$\lim_{x \rightarrow a} f(x)=f(a)$$

holds. If $f$ is continuous at every point of its domain, we call $f$ a *continuous function*.
:::

Written out in terms of the $\epsilon$-$\delta$ formulation, this means that for every $\epsilon>0$ there exists some $\delta > 0$ such that for all $x$ in the domain,

$$\lvert x-a\rvert < \delta\implies\lvert f(x)-f(a)\rvert<\epsilon$$

holds. The only difference is that the condition excluding $x=a$, namely $0<\lvert x-a\rvert$, has disappeared, because when $x=a$, $\lvert f(a)-f(a)\rvert=0<\epsilon$ holds automatically, so there is no need to exclude it.

Continuity can still be defined in the same way even when the domain does not contain an entire neighborhood of $a$. For example, if the domain is a closed interval $[a,b]$, continuity at the endpoint $a$ means $\lim_{x\rightarrow a^+} f(x)=f(a)$ in terms of the right-hand limit of [§Limits of Functions, ⁋Definition 12](/en/math/calculus/functions_and_limits#def12){: data-lid="azr5a" }, and continuity at the endpoint $b$ means $\lim_{x\rightarrow b^-} f(x)=f(b)$ in terms of the left-hand limit.

Breaking down this definition, we see that for continuity to hold, all three of the following conditions must be satisfied.

1. $f(a)$ is defined.
2. The limit $\lim_{x\rightarrow a} f(x)$ exists.
3. The two values above are equal.

The type of discontinuity depends on which of these conditions fails; we will return to this after examining the basic properties of continuous functions.

## Operations on Continuous Functions

Since continuity states that the limit coincides with the function value, [§Limits of Functions, ⁋Proposition 5](/en/math/calculus/functions_and_limits#prop5){: data-lid="nn0lo" } carries over directly to operations on continuous functions.

::: Proposition 2
If $f$ and $g$ are continuous at $a$, then $f+g$, $cf$ (where $c$ is a constant), and $fg$ are also continuous at $a$, and if $g(a)\neq 0$, then $f/g$ is continuous at $a$ as well. Moreover, if $f$ is continuous at $a$ and $g$ is continuous at $f(a)$, then the composite function $g \circ f$ is continuous at $a$.
:::
::: Proof
Only the assertion about the composite function is a new result. Let $\epsilon>0$ be given. Then first, since $g$ is continuous at $b:=f(a)$, there exists some $\eta>0$ such that

$$\lvert y-b\rvert < \eta\implies\lvert g(y)-g(b)\rvert < \epsilon$$

holds. Next, since $f$ is continuous at $a$, for this $\eta$ there exists $\delta > 0$ such that

$$\lvert x-a\rvert < \delta\implies\lvert f(x)-b\rvert < \eta$$

holds. Combining the two steps, whenever $\lvert x-a\rvert < \delta$, the value $y=f(x)$ satisfies $\lvert y-b\rvert < \eta$, and hence $\lvert g(f(x))-g(f(a))\rvert < \epsilon$.
:::

We can check that constant functions and the linear function $f(x)=x$ are continuous. Consequently, repeatedly taking sums and products shows that every polynomial function is continuous, and taking quotients of these shows that every rational function is continuous everywhere except at points where the denominator is $0$. The following is a slightly less trivial example of a continuous function.

::: Example 3
Let us show that the trigonometric function $\sin x$ is continuous at every point of its domain. From the sum-to-product identity for trigonometric functions, we know that

$$\lvert \sin x - \sin a\rvert= \left\lvert 2\cos\frac{x+a}{2}\sin\frac{x-a}{2}\right\rvert \leq 2\left\lvert \sin\frac{x-a}{2}\right\rvert$$

always holds. Meanwhile, the inequality for $0<t<\pi/2$ obtained in [§Limits of Functions, ⁋Example 10](/en/math/calculus/functions_and_limits#ex10){: data-lid="7ms67" }, namely $\sin t \leq t$, extends (since even when $t\geq\pi/2$ we have $\lvert \sin t\rvert \leq 1 < t$, and $\sin(-t)=-\sin t$) to yield, for all real $t$, the inequality $\lvert \sin t\rvert \leq \lvert t\rvert$. Applying this, for any $a\in\mathbb{R}$ we have

$$\lvert \sin x-\sin a\rvert\leq\lvert x-a\rvert$$

so it suffices to set $\delta=\epsilon$.
:::

Now, since the $\cos$ function can be obtained by translating the $\sin$ function, it is continuous by [Proposition 2](#prop2){: data-lid="e9wis" }, and hence their ratio $\tan x$ is also continuous everywhere except at points where the denominator is $0$.

## Properties of Continuous Functions on Closed Intervals

One useful property of continuous functions is that if $f$ is continuous at $a$ and $f(a) > 0$, then for $\epsilon = f(a)/2$ we can choose a corresponding $\delta$, so that in this case, on the neighborhood of $a$ of radius $\delta$, $f$ is always positive. This simple fact is not only useful in its own right, but also generalizes to the following theorems.

::: Theorem 4 (Extreme value theorem)
If $f$ is continuous on a closed interval $[a,b]$, then $f$ attains a maximum and a minimum on $[a,b]$. That is, there exist $c,d \in [a,b]$ such that for all $x \in [a,b]$, $f(d)\leq f(x)\leq f(c)$.
:::

::: Theorem 5 (Intermediate value theorem)
If $f$ is continuous on a closed interval $[a,b]$ and $f(a)\neq f(b)$, then for any value between $f(a)$ and $f(b)$, say $y$, the equation $f(c)=y$ holds for some $c \in (a,b)$.
:::

Since the proofs of these two theorems essentially require the completeness of the real numbers, we will accept them as facts without proof.

We have already seen above that continuity requires three conditions: (1) the function value is defined, (2) the limit exists, and (3) these two values are equal. We can now classify the types of discontinuities according to which of these conditions fails.

::: Definition 6 (Classification of discontinuities)
Suppose that a function $f$ is defined on some deleted neighborhood of $a$, and either it is not continuous at $a$ or $f(a)$ is undefined. Then, depending on whether the two one-sided limits $\lim_{x\rightarrow a^\pm} f(x)$ exist and agree, we classify this discontinuity as follows.

1. *Removable discontinuity*: the limit $\lim_{x\rightarrow a} f(x)$ exists, but either it differs from $f(a)$ or $f(a)$ is undefined.
2. *Jump discontinuity*: both one-sided limits exist, but they are not equal.
3. *Essential discontinuity*: at least one of the one-sided limits does not exist (oscillating or diverging).
:::

For example, the function $(x^2-1)/(x-1)$ is undefined where the denominator is $0$, namely at $x=1$; however, if we newly *define* its value at $x=1$ to be $2$, the discontinuity of this function is removed, and such functions form the first type. An example of the second type is $\lvert x\rvert/x$, which we examined right after [§Limits of Functions, ⁋Definition 12](/en/math/calculus/functions_and_limits#def12){: data-lid="13sia" }: while being undefined at $x=0$ is already a problem for this function, the bigger problem is that as $x\rightarrow 0^+$ it gives $1$ and as $x\rightarrow 0^-$ it gives $-1$, so the two one-sided limits yield different values. The final type collects all kinds of limits not belonging to these two categories; for example, $\sin(1/x)$ is of this kind at the origin.

## Monotone Functions and Inverse Functions

One important application of the intermediate value theorem is the continuity of inverse functions. A function is *strictly increasing* (or strictly decreasing) on an interval if $x_1<x_2$ always implies $f(x_1)<f(x_2)$ (or $>$), and such functions are collectively called *strictly monotone*. A strictly monotone function is trivially injective, and therefore has an inverse function on its image.

::: Proposition 7
If $f$ is continuous and strictly monotone on an interval $I$, then its image $J=f(I)$ is also an interval, and its inverse function $f^{-1}:J \rightarrow I$ is also a continuous strictly monotone function.
:::
::: Proof
It suffices to prove the case where $f$ is strictly increasing; the strictly decreasing case follows by reversing all inequalities and repeating the same argument.

First, let us show that $J$ is an interval. That is, given any two elements in the image of $f$, we must show that any element between them also lies in the image of $f$. This is precisely the content of [Theorem 5](#thm5){: data-lid="1jn9x" }, so the claim holds. Next, the fact that the inverse function $f^{-1}$ is strictly increasing follows immediately by reading the inequality expressing that $f$ is strictly increasing from the perspective of the inverse function.

Now, to prove continuity, let $y_0\in J$ be arbitrary, set $x_0=f^{-1}(y_0)$, and suppose $\epsilon>0$ is given. For convenience, we consider only the case where $x_0$ lies in the interior of the interval $I$. Then we can choose $x_1,x_2\in I$ such that the inequality

$$x_0-\epsilon<x_1<x_0<x_2 < x_0 + \epsilon$$

holds. Then, for $y_1=f(x_1)$ and $y_2=f(x_2)$, if we set $\delta=\min(y_0-y_1, y_2-y_0)>0$, then whenever $\lvert y-y_0\rvert<\delta$ for $y\in J$, we have $y_1<y<y_2$. Since $f^{-1}$ is strictly increasing, applying $f^{-1}$ to this inequality yields $x_1<f^{-1}(y)<x_2$, and by the choice of $x_1,x_2$, it follows that $\lvert f^{-1}(y) - x_0\rvert < \epsilon$.

In the case where $x_0$ is an endpoint of $I$, so that points of $I$ lie on only one side, we simply choose the corresponding point among $x_1$ and $x_2$ and repeat the same argument.
:::

For example, $f(x) = x^n$ ($x \geq 0$, with $n$ a natural number) is continuous and strictly increasing, so its inverse, the $n$th root $\sqrt[n]{x}$, is also continuous. Similarly, the inverse trigonometric functions and the like, which are inverses of restricted trigonometric functions, are all continuous.

For a rational exponent $p/q$ with $q>0$, we can use roots to set $b^{p/q}=(\sqrt[q]{b})^p$ for $b>0$ and show that this is continuous in $b$. For an irrational exponent $\alpha$, we can take a sequence of rational numbers $r_n$ tending to $\alpha$ and define $x^\alpha$ for $x>0$ as the limit of $x^{r_n}$. Justifying this construction requires the completeness of the real numbers, so we omit the details here.

---

**References**

**[Ste]** J. Stewart, *Calculus*, 8th ed., Cengage Learning, 2016.  
**[Kim]** 김홍종, *미적분학 1·2*, 제3개정판, 서울대학교출판문화원, 2020.
