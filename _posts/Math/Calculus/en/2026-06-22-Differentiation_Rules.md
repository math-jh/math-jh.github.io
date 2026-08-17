---
title: "Differentiation"
description: "We derive the derivative of the exponential function through termwise differentiation of power series, and summarize the derivatives of trigonometric functions along with the product, chain, quotient, and inverse function rules. This provides a systematic way to differentiate any function built from elementary functions."
excerpt: "Termwise differentiation of power series, derivatives of elementary functions, product, quotient, and chain rules"

categories: [Math / Calculus]
permalink: /en/math/calculus/differentiation_rules
sidebar: 
    nav: "calculus-en"

date: 2026-06-22
weight: 7
translated_at: 2026-08-17T18:17:10+00:00
translation_source: kimi-cli
---
We covered the definition of differentiation and its basic properties in [§Differentiation and Derivatives](/en/math/calculus/derivatives). In this post, we treat derivatives of concrete functions and differentiation rules applicable to general functions.

## Term-by-Term Differentiation of Power Series

First, for any natural number $n$, the derivative of $x^n$ at a point $a$ is

$$\lim_{h\rightarrow 0}\frac{(a+h)^n-a^n}{h}=\lim_{h\rightarrow 0}\frac{na^{n-1}h+\ldots}{h}=na^{n-1}$$

as can be verified, and similarly for a negative integer $n = -m$, putting the difference quotient over a common denominator gives

$$\frac{(a+h)^{-m} - a^{-m}}{h} = -\frac{(a+h)^m - a^m}{h}\cdot\frac{1}{(a+h)^ma^m}$$

so that $(x^n)' = n x^{n-1}$ holds for all integers $n$.

On the other hand, by linearity a polynomial is differentiated term by term, so this also yields a differentiation rule for arbitrary polynomial functions. However, in general distributing differentiation term by term in an *infinite* sum is not obvious, and the following proposition guarantees that this is permitted for power series.

::: Proposition 1 (Term-by-term differentiation of power series)
If the power series $f(x) = \sum_{n=0}^\infty c_n x^n$ has radius of convergence $R > 0$, then $f$ is differentiable for $\lvert x\rvert < R$ and

$$f'(x) = \sum_{n=1}^\infty n c_n x^{n-1}$$

and this series also has radius of convergence $R$.
:::

That the series on the right-hand side has radius of convergence $R$ itself follows from the fact that $n^{1/n}$ converges to $1$ as $n\rightarrow \infty$, but we lack the tools to rigorously justify that it actually equals $f'(x)$, so we shall accept this and move on.

## Derivatives of Trigonometric and Exponential Functions

Before examining differentiation rules in earnest, we derive the derivatives of various functions.

First, the exponential function was defined in [§Power Series, ⁋Example 3](/en/math/calculus/power_series#ex3) by $e^x = \sum_{n\geq 0} x^n/n!$. Applying [Proposition 1](#prop1), its derivative is the sum of term-by-term differentiations

$$(e^x)' = \sum_{n=1}^\infty n \frac{x^{n-1}}{n!} = \sum_{n=1}^\infty \frac{x^{n-1}}{(n-1)!} = \sum_{m=0}^\infty \frac{x^m}{m!} = e^x$$

so the exponential function is invariant under differentiation. In high school this result was obtained from the limit

$$\lim_{h\rightarrow 0}(e^h-1)/h = 1$$

Trigonometric functions will also soon be written in power-series form, but for now we derive them using the two limits

$$\lim_{h \rightarrow 0} \frac{\sin h}{h} = 1, \qquad \lim_{h \rightarrow 0} \frac{1 - \cos h}{h} = 0$$

The first limit was obtained by the squeeze theorem in [§Limits of Functions, ⁋Example 10](/en/math/calculus/functions_and_limits#ex10), and the second follows from the same example's inequality $\lvert 1 - \cos h\rvert \leq h^2/2$, which gives $\lvert(1 - \cos h)/h\rvert \leq \lvert h\rvert/2$.

::: Proposition 2 (Derivatives of trigonometric functions)
At every point $(\sin x)' = \cos x$ and $(\cos x)' = -\sin x$.
:::

::: Proof
Using the addition formula $\sin(x+h) = \sin x\cos h + \cos x \sin h$, we split the difference quotient as

$$\frac{\sin(x+h) - \sin x}{h} = \sin x \cdot \frac{\cos h - 1}{h} + \cos x \cdot \frac{\sin h}{h}$$

and as $h \rightarrow 0$ the two limits above give $\sin x \cdot 0 + \cos x \cdot 1 = \cos x$. The derivative of $\cos x$ is obtained in the same way.
:::

## Various Differentiation Rules

We now define differentiation rules applicable to general forms. In [§Differentiation and Derivatives, ⁋Proposition 4](/en/math/calculus/derivatives#prop4) we saw that differentiation behaves well with respect to constant multiples and addition, but it does not simply distribute over products.

::: Proposition 3 (Product rule)
If $f, g$ are differentiable at $a$, then $fg$ is also differentiable at $a$ and

$$(fg)'(a) = f'(a) g(a) + f(a) g'(a)$$

holds.
:::

::: Proof
Adding and subtracting the same term in the difference quotient gives

$$\frac{f(a+h)g(a+h) - f(a)g(a)}{h} = \frac{f(a+h)-f(a)}{h} g(a+h) + f(a) \frac{g(a+h)-g(a)}{h}$$

As $h \rightarrow 0$, the difference quotient in the first term converges to $f'(a)$, $g(a+h)$ converges to $g(a)$ by continuity of $g$ ([§Differentiation and Derivatives, ⁋Proposition 2](/en/math/calculus/derivatives#prop2)), and the difference quotient in the second term converges to $g'(a)$, so by [§Limits of Functions, ⁋Proposition 5](/en/math/calculus/functions_and_limits#prop5) the sum converges to $f'(a)g(a) + f(a)g'(a)$.
:::

The most widely used rule is the derivative of a composite function.

::: Theorem 4 (Chain rule)
If $f$ is differentiable at $a$ and $g$ is differentiable at $b = f(a)$, then the composition $g \circ f$ is also differentiable at $a$ and

$$(g \circ f)'(a) = g'(f(a)) f'(a)$$

holds.
:::

::: Proof
We encode the differentiability of $g$ in the auxiliary function

$$\varphi(y) = \begin{cases} \frac{g(y) - g(b)}{y - b}, & y \neq b,\\[1mm] g'(b), & y = b \end{cases}$$

By definition of differentiability, $\varphi$ is continuous at $b$, and $g(y) - g(b) = \varphi(y)(y - b)$ holds for all $y$. Substituting $y = f(a+h)$ gives

$$\frac{g(f(a+h)) - g(f(a))}{h} = \varphi(f(a+h)) \frac{f(a+h) - f(a)}{h}$$

and as $h \rightarrow 0$, continuity of $f$ yields $\varphi(f(a+h)) \rightarrow \varphi(b) = g'(b)$ while the second factor converges to $f'(a)$, so the limit is $g'(f(a))f'(a)$.
:::

The quotient rule now follows as a corollary of the product rule and the chain rule.

::: Corollary 5 (Quotient rule)
If $f, g$ are differentiable at $a$ and $g(a) \neq 0$, then $f/g$ is also differentiable at $a$ and

$$\left(\frac{f}{g}\right)'(a) = \frac{f'(a) g(a) - f(a) g'(a)}{g(a)^2}$$

holds.
:::

::: Proof
Defining $h(t)=1/t$, we have $1/g =h \circ g$, and by the derivative of integer powers $h'(t)=-1/t^2$, so by [Theorem 4](#thm4) we get $(1/g)'(a) = -g(a)^{-2}g'(a)$. Applying the product rule to $f/g = f\cdot(1/g)$ now yields

$$\left(\frac{f}{g}\right)'(a) = \frac{f'(a)}{g(a)} - \frac{f(a)g'(a)}{g(a)^2} = \frac{f'(a)g(a) - f(a)g'(a)}{g(a)^2}$$

as desired.
:::

For instance, from $\tan x = \sin x/\cos x$ we get $(\tan x)' = (\cos^2 x + \sin^2 x)/\cos^2 x = \sec^2 x$, and similarly $(\cot x)' = -\csc^2 x$.

Finally, if a function is monotone then the derivative of its inverse is obtained immediately without separate computation.

::: Proposition 6 (Derivative of inverse function)
Let $f$ be a monotone continuous function on an interval having inverse $f^{-1}$, and suppose $f$ is differentiable at $a$ with $f'(a) \neq 0$. Then $f^{-1}$ is differentiable at $b = f(a)$ and

$$(f^{-1})'(b) = \frac{1}{f'(a)} = \frac{1}{f'(f^{-1}(b))}$$

holds.
:::

::: Proof
Let $I$ be the interval on which $f$ is defined and let $J = f(I)$ be its image. Since $f$ is monotone and has an inverse, it is injective, hence strictly monotone, and therefore $f^{-1} : J \rightarrow I$ is continuous by [§Continuous Functions, ⁋Proposition 7](/en/math/calculus/continuity#prop7).

Now if $y \in J$ with $y \neq b$, then $x = f^{-1}(y)$ differs from $a = f^{-1}(b)$ by injectivity, so we can rewrite the difference quotient of $f^{-1}$ as

$$\frac{f^{-1}(y) - f^{-1}(b)}{y - b} = \frac{x - a}{f(x) - f(a)} = \left(\frac{f(x)-f(a)}{x-a}\right)^{-1}$$

As $y \rightarrow b$, continuity of $f^{-1}$ gives $x \rightarrow a$, and the expression in parentheses on the right converges to $f'(a)$, so by $f'(a) \neq 0$ and part 4 of [§Limits of Functions, ⁋Proposition 5](/en/math/calculus/functions_and_limits#prop5) the above difference quotient converges to $1/f'(a)$. That is, $f^{-1}$ is differentiable at $b$ and $(f^{-1})'(b) = 1/f'(a)$.
:::

With this we can also proceed with derivatives of the inverses of the functions examined above. For instance, for the inverse $\ln$ of $e^x$, since $(e^x)' = e^x$ we have $(\ln y)' = 1/e^{\ln y} = 1/y$, and for the inverse $\arcsin$ of $\sin$ restricted to $(-\pi/2, \pi/2)$, since $f'(x) = \cos x = \sqrt{1 - \sin^2 x} > 0$ we have

$$(\arcsin y)' = \frac{1}{\sqrt{1 - y^2}} \qquad (\lvert y\rvert < 1)$$

and similarly $(\arctan y)' = 1/(1 + y^2)$.

On the other hand, once we compute a derivative using the rules developed so far, we may ask whether that derivative is again continuous; yet even a function differentiable everywhere can have a discontinuous derivative.

::: Example 7 (A differentiable function that is not $C^1$)
The function

$$f(x) = \begin{cases} x^2 \sin(1/x) & (x \neq 0) \\ 0 & (x = 0) \end{cases}$$

is differentiable at every point. For $x \neq 0$, the product rule and chain rule give $f'(x) = 2x\sin(1/x) - \cos(1/x)$, and at $0$ the difference quotient is $x\sin(1/x) \rightarrow 0$, so $f'(0) = 0$. However, as $x \rightarrow 0$ we have $2x\sin(1/x) \rightarrow 0$ but $\cos(1/x)$ oscillates infinitely often between $[-1, 1]$ without approaching a limit, so $f'$ is discontinuous at $0$. That is, $f$ is differentiable everywhere but not of class $C^1$ (in the sense of [§Differentiation and Derivatives, ⁋Definition 5](/en/math/calculus/derivatives#def5)).
:::

Nevertheless, a derivative cannot be discontinuous in just any manner. Even if a derivative is not continuous, it necessarily attains every intermediate value (*Darboux's theorem*), so it cannot have a jump discontinuity, and the discontinuity exhibited in [Example 7](#ex7) is due to oscillation rather than a jump.

## Applications of Differentiation Rules

We close this post by examining how to apply the rules developed so far. First, although somewhat contrary to the reason we introduced power series, [Proposition 1](#prop1) can be used to evaluate series.

::: Example 8 (Sum of an infinite series)
Differentiating both sides of the geometric series ([§Infinite Series, ⁋Example 2](/en/math/calculus/series#ex2))

$$\frac{1}{1-x} = \sum_{n=0}^\infty x^n \qquad (\lvert x\rvert < 1)$$

The left-hand side is by the chain rule

$$\left(\frac{1}{1-x}\right)' = 1/(1-x)^2$$

and the right-hand side becomes $\sum_{n\geq 1} n x^{n-1}$ by [Proposition 1](#prop1), so

$$\sum_{n=1}^\infty n x^{n-1} = \frac{1}{(1-x)^2} \qquad (\lvert x\rvert < 1)$$

and multiplying both sides by $x$ gives

$$\sum_{n\geq 1} n x^n = \frac{x}{(1-x)^2}$$

For instance, substituting $x = 1/2$, we can also compute the series sum $\sum_{n\geq 1} n/2^n = 2$.
:::

The second application is a result more befitting the calculus category, giving an actual rule for differentiating a given function.

::: Example 9 (Various differentiation methods)
When an equation defines $y$ as a function of $x$, solving for an explicit expression of the form $y=...$ in order to find $y'$ is often inefficient, or such a form may not yield a clean differentiation. In this situation, viewing $y$ as a function of $x$ and differentiating both sides before solving for $y'$ is called *implicit differentiation*. For example, differentiating both sides of the unit circle $x^2 + y^2 = 1$ gives

$$2x + 2y y' = 0$$

so at points where $y \neq 0$ we obtain $y' = -x/y$, and hence can find the slope of the tangent line at such a point $(x_0,y_0)$.

For functions with a variable in the exponent, *logarithmic differentiation* is convenient: take the logarithm of both sides and then differentiate. For example, for $y = x^x$ ($x > 0$), differentiating both sides of $\ln y = x\ln x$ and using $(\ln y)' = y'/y$ together with the product rule gives

$$\frac{y'}{y} = \ln x + 1 \quad\Longrightarrow\quad y' = x^x(\ln x + 1)$$

as desired.
:::

---

**References**

**[Ste]** J. Stewart, *Calculus*, 8th ed., Cengage Learning, 2016.  
**[Kim]** 김홍종, *미적분학 1·2*, 제3개정판, 서울대학교출판문화원, 2020.
