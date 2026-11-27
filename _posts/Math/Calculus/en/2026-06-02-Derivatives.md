---
title: "Differentiation and Derivatives"
description: "This post defines the derivative at a point as a limit representing a function's instantaneous rate of change and shows that differentiability implies continuity. It also covers derivative functions, higher-order derivatives, the differential as a linear approximation, and the hierarchy of differentiability and smoothness."
excerpt: "Derivative definition, differentiability and continuity, derivative functions, and higher-order derivatives"

categories: [Math / Calculus]
permalink: /en/math/calculus/derivatives
sidebar: 
    nav: "calculus-en"

date: 2026-06-02
weight: 6
translated_at: 2026-11-27T19:17:17+00:00
translation_source: antigravity-gemini-3.8-flash-high
last_polished_at: 2026-11-27T23:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
In [§Continuous Functions](/en/math/calculus/continuity){: data-lid="jv8y8" }, we reformulated the definition of continuity of a function in the $\epsilon$-$\delta$ language introduced earlier. The natural next step is to define the derivative of a function.

## Definition of the Derivative

The definition of differentiability is also the same as in high school. That is, the slope of the line joining the two points $(a,f(a))$ and $(x,f(x))$ is given by the average rate of change $\frac{f(x)-f(a)}{x-a}$, and taking the limit as $x$ approaches $a$ yields the derivative; the only difference from high school is that the limit used in this definition has actually been mathematically defined.

::: Definition 1
A function $f$ is *differentiable* at a point $a$ if the limit

$$\lim_{x\rightarrow a} \frac{f(x)-f(a)}{x-a}=\lim_{h\rightarrow 0} \frac{f(a+h)-f(a)}{h}$$

exists. In this case, this value is called the *derivative* of $f$ at $a$ and is denoted by $f'(a)$. If $f$ is differentiable at every point in its domain, the function $f'$ defined by $x \mapsto f'(x)$ is called the *derivative function* of $f$.
:::

The two expressions in the definition are, of course, the same upon setting $x=a+h$, and by the preceding discussion of the average rate of change, the derivative $f'(a)$ has the geometric meaning of being the slope of the tangent line to the graph at the point $(a, f(a))$. Meanwhile, any line is completely determined by its slope and a point on it; in particular, since it is already given that this tangent line passes through $(a,f(a))$, the tangent line to a function differentiable at $a$ is given by

$$y=f(a)+f'(a)(x-a)$$

Near $a$, this linear function best approximates $f$, so for small $h$ we write $f(a+h) \approx f(a)+f'(a)h$. Following Leibniz notation, the derivative is also written as

$$\frac{\dd{f}}{\dd{x}},\qquad \frac{d}{\dd{x}}f$$

and the like, though in calculus the notation $f'$ is often sufficient.

We will treat derivatives of a wider variety of functions in earnest in the next post, but the following example illustrates derivatives that can be computed directly from the definition.

::: Example 2 (Differentiation of functions of the form $x^\alpha$)
Since the average rate of change of a constant function is always $0$, its derivative is also $0$. For $f(x)=x^2$, simplifying the average rate of change as

$$\frac{(a+h)^2-a^2}{h}=2a+h$$

gives $f'(a)=2a$. More generally, for a positive integer $n$, factoring the difference of powers yields

$$\frac{(a+h)^n-a^n}{h}=\sum_{j=0}^{n-1}(a+h)^{n-1-j}a^j$$

so when we take the limit as $h\rightarrow 0$, each of the $n$ terms on the right-hand side converges to $a^{n-1}$, whence $(x^n)'=nx^{n-1}$.

For a negative integer exponent $-m$, the function $x^{-m}$ is defined only at points other than the origin. At a point $a$ in its domain, putting the average rate of change over a common denominator gives

$$\frac{(a+h)^{-m}-a^{-m}}{h}=-\frac{(a+h)^m-a^m}{h}\cdot\frac{1}{(a+h)^ma^m}$$

As $h\rightarrow 0$, the two fractions converge to $ma^{m-1}$ and $1/a^{2m}$, respectively, so the derivative at $a$ is $-ma^{-m-1}$.

Now, for a rational exponent $p/q$, let us consider the derivative of the function $x^{p/q}$. When representing any rational number in this form, we may take $p$ to be an arbitrary integer and $q$ to be a positive integer. In general, since the domain becomes an issue when dealing with roots (that is, $1/q$-th powers), we regard this function as defined only for $x>0$. Then for any point $a$ in the domain, setting $u=\sqrt[q]{a+h}$ and $v=\sqrt[q]{a}$ gives $h=u^q-v^q$, so

$$\frac{(a+h)^{p/q}-a^{p/q}}{h}=\frac{(u^p-v^p)/(u-v)}{(u^q-v^q)/(u-v)}$$

By [§Limits of Functions, ⁋Corollary 6](/en/math/calculus/functions_and_limits#cor6){: data-lid="bubh4" }, as $h\rightarrow 0$ we have $u\rightarrow v$. By the derivatives of integer powers obtained above, the numerator and denominator on the right-hand side converge to $pv^{p-1}$ and $qv^{q-1}$, respectively. Since $q>0$ and $v>0$, the limit of the denominator is positive. Therefore, applying part 4 of [§Limits of Functions, ⁋Proposition 5](/en/math/calculus/functions_and_limits#prop5){: data-lid="chuau" } yields

$$\lim_{h\rightarrow 0}\frac{(a+h)^{p/q}-a^{p/q}}{h}=\frac{pv^{p-1}}{qv^{q-1}}=\frac{p}{q}a^{p/q-1}$$

Therefore, for $x>0$, we have $(x^{p/q})'=(p/q)x^{p/q-1}$.
:::

More generally, for any real number $\alpha$, the derivative of the function $x^\alpha$ on its domain is given by $\alpha x^{\alpha-1}$. While this can of course be proved using the squeeze theorem and a sequence of rational numbers converging to $\alpha$, we will defer this calculation for now in order to carry it out in the next post using applications of differentiation.

## Differentiability and Continuity

As mentioned above, we will leave the computation of derivatives of various functions primarily to the next post, and in this post we will focus a bit more on the general properties of differentiation and differentiable functions. The first property of a differentiable function is that it is automatically continuous.

::: Proposition 3
If $f$ is differentiable at $a$, then $f$ is continuous at $a$.
:::
::: Proof
For $x \neq a$, we have

$$f(x)-f(a)=\frac{f(x)-f(a)}{x-a}\cdot(x-a)$$

As $x \rightarrow a$, the first factor on the right-hand side converges to $f'(a)$ and the second factor converges to $0$, so by [§Limits of Functions, ⁋Proposition 5](/en/math/calculus/functions_and_limits#prop5){: data-lid="hocyr" },

$$\lim_{x\rightarrow a}\bigl(f(x)-f(a)\bigr)=f'(a)\cdot 0=0$$

Therefore, $f$ is continuous at $a$.
:::

In other words, differentiability is a stronger condition than continuity. The converse, however, does not hold. A standard example is $f(x)=\lvert x\rvert$, which is continuous at $0$ but not differentiable there.

{% diagram Math/Calculus/Derivatives-1.svg width="11.21em" alt="Graph of the absolute value function" %}

Indeed, since

$$\frac{f(h)-f(0)}{h}=\frac{\lvert h\rvert}{h}=\begin{cases}1&\text{if $h>0$}\\-1&\text{if $h<0$}\end{cases}$$

for the difference quotient of this function, the limit as $h \rightarrow 0^+$ is $1$ and the limit as $h \rightarrow 0^-$ is $-1$; since these differ, the limit does not exist. In the terminology of [§Continuous Functions, ⁋Definition 6](/en/math/calculus/continuity#def6){: data-lid="yv82t" }, this corresponds to the derivative having a jump discontinuity at the origin. To see a case where the derivative has an essential singularity, consider $f(x)=\sqrt[3]{x}$. At $0$, this function has a *vertical tangent* where the difference quotient diverges as $h^{-2/3} \rightarrow \infty$, so the value of the derivative does not exist in the limit $x\rightarrow 0$.

{% diagram Math/Calculus/Derivatives-2.svg width="12.46em" alt="Vertical tangent of the cube root function" %}

Similarly, $f(x)=x^{2/3}$ forms a *cusp* at $0$, where the left- and right-hand difference quotients diverge to $\mp\infty$.

{% diagram Math/Calculus/Derivatives-3.svg width="13.17em" alt="Cusp of the 2/3-power function" %}

While these are examples that fail to be differentiable at only one or two points, nondifferentiability can be far more severe: there even exist functions that are continuous everywhere on $\mathbb{R}$ yet have no tangent line at any point ([Weierstrass function](https://en.wikipedia.org/wiki/Weierstrass_function)).

Conversely, differentiability is a local property that can hold at only a single point, so extreme examples of the following form are also possible.

::: Example 4 (A function differentiable at only one point)
Consider the function

$$f(x)=\begin{cases} x^2 & (x \in \mathbb{Q}) \\ 0 & (x \notin \mathbb{Q}) \end{cases}$$

For $a \neq 0$, the values of the function along rational and irrational sequences converging to $a$ separate into $a^2$ and $0$, respectively; hence $f$ is discontinuous there, and by the contrapositive of [Proposition 3](#prop3){: data-lid="v5ru4" }, it is not differentiable. On the other hand, at $0$ we have $\lvert f(x)\rvert \leq x^2$, so it is continuous, and the difference quotient satisfies

$$\left\lvert \frac{f(x)-f(0)}{x-0} \right\rvert=\frac{\lvert f(x)\rvert}{\lvert x\rvert} \leq \lvert x\rvert \rightarrow 0$$

so $f'(0)=0$ exists. Thus $f$ is differentiable only at $0$.
:::

## Properties of Differentiation

By definition, a derivative is ultimately the limit of a function (namely, the difference quotient), so from [§Limits of Functions, ⁋Proposition 5](/en/math/calculus/functions_and_limits#prop5){: data-lid="4jdpl" } we can prove that differentiation is also linear.

::: Proposition 5
If $f, g$ are differentiable at $a$ and $c$ is a constant, then $f+g$ and $cf$ are also differentiable at $a$, and

$$(f+g)'(a)=f'(a)+g'(a), \qquad (cf)'(a)=c f'(a)$$
:::
::: Proof
The average rate of change splits as

$$\frac{(f+g)(a+h)-(f+g)(a)}{h}=\frac{f(a+h)-f(a)}{h}+\frac{g(a+h)-g(a)}{h}$$

and since each term converges to $f'(a), g'(a)$, respectively, their sum also converges by [§Limits of Functions, ⁋Proposition 5](/en/math/calculus/functions_and_limits#prop5){: data-lid="bwos3" }. Inspecting the expression for the average rate of change of $cf$ yields the same result.
:::

Applying the derivatives of integer powers obtained in [Example 2](#ex2){: data-lid="8l9ug" } together with [Proposition 5](#prop5){: data-lid="q0vtg" }, we can verify that the derivative of any polynomial $P(x)=\sum_{k=0}^n c_k x^k$ is

$$P'(x)=\sum_{k=1}^n k c_k x^{k-1}$$

That is, when differentiating, the constant term vanishes and the remaining terms are differentiated individually. For instance, if $P(x)=x^3-2x+1$, then $P'(x)=3x^2-2$.

Meanwhile, since the derivative $f'$ is itself a function, we can differentiate it again if it is differentiable.

::: Definition 6
If the derivative of $f$, namely $f'$, is differentiable, its derivative $f''=(f')'$ is called the *second derivative*. Repeating this process to differentiate $n$ times yields the *$n$th derivative* $f^{(n)}$, and we set $f^{(0)}=f$. If $f^{(n)}$ exists and is continuous on an interval, then $f$ is said to be *of class $C^n$* on that interval; if derivatives of all orders exist, it is said to be *of class $C^\infty$* or *smooth*.
:::

The second derivative $f''$ is the rate of change of the rate of change; if $f$ represents position, then $f''$ is acceleration. Moreover, the sign of $f''$ tells us the direction in which the graph bends, namely the concavity and convexity of the function. Differentiating a polynomial more times than its degree yields $0$, and since $0$ is a constant function, it can be differentiated indefinitely and its value remains $0$. Hence every polynomial is $C^\infty$.

Furthermore, since the derivative is essentially a function, we can consider its continuity and, as we saw immediately after [Proposition 3](#prop3){: data-lid="hr67q" }, apply the classification in [§Continuous Functions, ⁋Definition 6](/en/math/calculus/continuity#def6){: data-lid="vjc5i" }. For such cases, defining the two limits separately makes it convenient to handle differentiability at corners or endpoints.

::: Definition 7
We define the *right-hand derivative* and *left-hand derivative* of a function $f$ at a point $a$ by

$$f'_+(a) := \lim_{h \rightarrow 0^+} \frac{f(a+h)-f(a)}{h}, \qquad f'_-(a) := \lim_{h \rightarrow 0^-} \frac{f(a+h)-f(a)}{h}$$

respectively.
:::

One point to be careful about, although the names can easily cause confusion, is that the right-hand derivative $f'_+(a)$ is clearly different from the right-hand limit of the derivative $f'(x)$ as $x\rightarrow a^+$. The function $f$ is differentiable at $a$ if and only if both the right-hand derivative and the left-hand derivative exist and are equal, in which case their common value is $f'(a)$. This is nothing more than applying to the average rate of change the fact that a limit exists only when the two one-sided limits coincide. For example, revisiting the absolute value function $f(x)=\lvert x\rvert$, we have $f'_+(0)=1$ and $f'_-(0)=-1$; since the two differ, we immediately confirm that it is not differentiable at $0$.

For instance, when the domain is $[0,\infty)$ and $f(x)=\sqrt{x}$, we use the usual average rate of change at ordinary points, whereas at the endpoint $0$ we can define the derivative by taking the limit of the average rate of change from the right. However, for $h>0$,

$$\frac{f(h)-f(0)}{h}=\frac{\sqrt{h}}{h}=\frac{1}{\sqrt{h}}$$

and since this value diverges to $+\infty$ as $h\rightarrow 0^+$, we see that the right-hand derivative does not exist at $0$.

---

**References**

**[Ste]** J. Stewart, *Calculus*, 8th ed., Cengage Learning, 2016.  
**[Kim]** 김홍종, *미적분학 1·2*, 제3개정판, 서울대학교출판문화원, 2020.
