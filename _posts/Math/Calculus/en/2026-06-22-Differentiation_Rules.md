---
title: "Differentiation"
description: "We obtain the derivative of the exponential function through termwise differentiation of power series, and summarize the derivatives of trigonometric functions, the product and chain rules, the quotient rule, and the inverse function rule. This makes it possible to systematically differentiate functions composed of elementary functions."
excerpt: "Termwise power series differentiation, elementary function derivatives, product, quotient, and chain rules"

categories: [Math / Calculus]
permalink: /en/math/calculus/differentiation_rules
sidebar: 
    nav: "calculus-en"

date: 2026-06-22
weight: 7
translated_at: 2026-08-19T05:45:05+00:00
translation_source: kimi-cli
last_polished_at: 2026-09-29T07:15:05+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
We covered the definition of differentiation and its basic properties in [§Differentiation and Derivatives](/en/math/calculus/derivatives){: data-lid="65feo" }. In this post, we treat derivatives of concrete functions and differentiation rules applicable to general functions.

## Term-by-Term Differentiation of Power Series

In [§Differentiation and Derivatives, ⁋Example 2](/en/math/calculus/derivatives#ex2) we saw that $(x^n)'=nx^{n-1}$ for positive integers $n$. Together with linearity from [§Differentiation and Derivatives, ⁋Proposition 5](/en/math/calculus/derivatives#prop5){: data-lid="4405y" }, this gives term-by-term differentiation for polynomials. The following proposition extends term-by-term differentiation to power series inside their radius of convergence.

::: Proposition 1 (Term-by-term differentiation of power series)
If the power series $f(x) = \sum_{n=0}^\infty c_n x^n$ has radius of convergence $R > 0$, then $f$ is differentiable for $\lvert x\rvert < R$ and

$$f'(x) = \sum_{n=1}^\infty n c_n x^{n-1}$$

and this series also has radius of convergence $R$.
:::

That the series on the right-hand side has radius of convergence $R$ itself follows from the fact that as $n\rightarrow \infty$, $n^{1/n}$ converges to $1$, but we lack the tools to rigorously justify that it actually equals $f'(x)$, so we shall accept this and move on.

## Derivatives of Trigonometric and Exponential Functions

Before examining differentiation rules in earnest, we derive the derivatives of various functions.

First, the exponential function was defined in [§Power Series, ⁋Example 3](/en/math/calculus/power_series#ex3){: data-lid="00w8x" } by $e^x = \sum_{n\geq 0} x^n/n!$. Applying [Proposition 1](#prop1){: data-lid="z8pkw" }, its derivative is the sum of term-by-term derivatives

$$(e^x)' = \sum_{n=1}^\infty n \frac{x^{n-1}}{n!} = \sum_{n=1}^\infty \frac{x^{n-1}}{(n-1)!} = \sum_{m=0}^\infty \frac{x^m}{m!} = e^x$$

so the exponential function is invariant under differentiation. In high school, it was from the limit

$$\lim_{h\rightarrow 0}(e^h-1)/h = 1$$

that this result was obtained.

Trigonometric functions will also soon be written in power-series form, but for now, using the two limits

$$\lim_{h \rightarrow 0} \frac{\sin h}{h} = 1, \qquad \lim_{h \rightarrow 0} \frac{1 - \cos h}{h} = 0$$

we obtain them. The first limit was obtained by the squeeze theorem in [§Limits of Functions, ⁋Example 10](/en/math/calculus/functions_and_limits#ex10){: data-lid="gvxns" }, and the second limit follows from the inequality $\lvert 1 - \cos h\rvert \leq h^2/2$ established in that same example, which yields $\lvert(1 - \cos h)/h\rvert \leq \lvert h\rvert/2$.

::: Proposition 2 (Derivatives of trigonometric functions)
At every point $(\sin x)' = \cos x$ and $(\cos x)' = -\sin x$.
:::

::: Proof
Splitting the difference quotient using the addition formula $\sin(x+h) = \sin x\cos h + \cos x \sin h$, we have

$$\frac{\sin(x+h) - \sin x}{h} = \sin x \cdot \frac{\cos h - 1}{h} + \cos x \cdot \frac{\sin h}{h}$$

and as $h \rightarrow 0$, by the two limits above this converges to $\sin x \cdot 0 + \cos x \cdot 1 = \cos x$. The derivative of $\cos x$ is obtained in the same way.
:::

## Various Differentiation Rules

We now define differentiation rules applicable to general forms. In [§Differentiation and Derivatives, ⁋Proposition 5](/en/math/calculus/derivatives#prop5){: data-lid="ogd67" } we saw that differentiation behaves well with respect to constant multiples and addition, but it does not simply distribute over products.

::: Proposition 3 (Product rule)
If $f, g$ are differentiable at $a$, then $fg$ is also differentiable at $a$ and

$$(fg)'(a) = f'(a) g(a) + f(a) g'(a)$$

holds.
:::

::: Proof
Adding and subtracting the same term in the difference quotient gives

$$\frac{f(a+h)g(a+h) - f(a)g(a)}{h} = \frac{f(a+h)-f(a)}{h} g(a+h) + f(a) \frac{g(a+h)-g(a)}{h}$$

As $h \rightarrow 0$, the difference quotient in the first term converges to $f'(a)$, $g(a+h)$ converges to $g(a)$ by the continuity of $g$ ([§Differentiation and Derivatives, ⁋Proposition 3](/en/math/calculus/derivatives#prop3){: data-lid="hzft9" }), and the difference quotient in the second term converges to $g'(a)$, so by [§Limits of Functions, ⁋Proposition 5](/en/math/calculus/functions_and_limits#prop5){: data-lid="edoso" } the sum converges to $f'(a)g(a) + f(a)g'(a)$.
:::

The most widely used rule is the derivative of a composite function.

::: Theorem 4 (Chain rule)
If $f$ is differentiable at $a$ and $g$ is differentiable at $b = f(a)$, then the composition $g \circ f$ is also differentiable at $a$ and

$$(g \circ f)'(a) = g'(f(a)) f'(a)$$

holds.
:::

::: Proof
We transfer the differentiability of $g$ to the auxiliary function

$$\varphi(y) = \begin{cases} \frac{g(y) - g(b)}{y - b}, & y \neq b,\\[1mm] g'(b), & y = b \end{cases}$$

By definition of differentiability, $\varphi$ is continuous at $b$, and $g(y) - g(b) = \varphi(y)(y - b)$ holds for all $y$. Substituting $y = f(a+h)$ gives

$$\frac{g(f(a+h)) - g(f(a))}{h} = \varphi(f(a+h)) \frac{f(a+h) - f(a)}{h}$$

and as $h \rightarrow 0$, by the continuity of $f$ we have $\varphi(f(a+h)) \rightarrow \varphi(b) = g'(b)$, and the second factor converges to $f'(a)$, so the limit is $g'(f(a))f'(a)$.
:::

The quotient rule now follows as a corollary of the product rule and the chain rule.

::: Corollary 5 (Quotient rule)
If $f, g$ are differentiable at $a$ and $g(a) \neq 0$, then $f/g$ is also differentiable at $a$ and

$$\left(\frac{f}{g}\right)'(a) = \frac{f'(a) g(a) - f(a) g'(a)}{g(a)^2}$$

holds.
:::

::: Proof
Set $h(t)=1/t$, so that $1/g=h\circ g$. By [§Differentiation and Derivatives, ⁋Example 2](/en/math/calculus/derivatives#ex2), $h'(t)=-1/t^2$, so [Theorem 4](#thm4){: data-lid="xpo63" } gives $(1/g)'(a)=-g(a)^{-2}g'(a)$. Now applying the product rule to $f/g = f\cdot(1/g)$, we obtain

$$\left(\frac{f}{g}\right)'(a) = \frac{f'(a)}{g(a)} - \frac{f(a)g'(a)}{g(a)^2} = \frac{f'(a)g(a) - f(a)g'(a)}{g(a)^2}$$
:::

For instance, from $\tan x = \sin x/\cos x$ we have $(\tan x)' = (\cos^2 x + \sin^2 x)/\cos^2 x = \sec^2 x$, and by the same method $(\cot x)' = -\csc^2 x$.

Finally, if a function is monotone, the derivative of its inverse is also obtained immediately without separate computation.

::: Proposition 6 (Derivative of an inverse function)
Let $f$ be a continuous monotone function on an interval having an inverse $f^{-1}$, and suppose $f$ is differentiable at $a$ with $f'(a) \neq 0$. Then $f^{-1}$ is differentiable at $b = f(a)$ and

$$(f^{-1})'(b) = \frac{1}{f'(a)} = \frac{1}{f'(f^{-1}(b))}$$

holds.
:::

::: Proof
Let $f$ be defined on the interval $I$, and let its image be $J = f(I)$. Since $f$ is monotone and has an inverse, it is injective, hence strictly monotone, and therefore $f^{-1} : J \rightarrow I$ is continuous by [§Continuous Functions, ⁋Proposition 7](/en/math/calculus/continuity#prop7){: data-lid="t16wr" }.

Now, if $y \in J$ satisfies $y \neq b$, then $x = f^{-1}(y)$ differs from $a = f^{-1}(b)$ by injectivity, so we can rewrite the difference quotient of $f^{-1}$ as

$$\frac{f^{-1}(y) - f^{-1}(b)}{y - b} = \frac{x - a}{f(x) - f(a)} = \left(\frac{f(x)-f(a)}{x-a}\right)^{-1}$$

As $y \rightarrow b$, the continuity of $f^{-1}$ gives $x \rightarrow a$, and the expression in parentheses on the right converges to $f'(a)$, so by $f'(a) \neq 0$ and part 4 of [§Limits of Functions, ⁋Proposition 5](/en/math/calculus/functions_and_limits#prop5){: data-lid="bpd9d" }, the above difference quotient converges to $1/f'(a)$. That is, $f^{-1}$ is differentiable at $b$ and $(f^{-1})'(b) = 1/f'(a)$.
:::

With this, we can also proceed with differentiating the inverses of the functions examined above. For instance, for the inverse of $e^x$, namely $\ln$, since $(e^x)' = e^x$, we have $(\ln y)' = 1/e^{\ln y} = 1/y$, and for the inverse of $\sin$ restricted to $(-\pi/2, \pi/2)$, namely $\arcsin$, since $f'(x) = \cos x = \sqrt{1 - \sin^2 x} > 0$, we have

$$(\arcsin y)' = \frac{1}{\sqrt{1 - y^2}} \qquad (\lvert y\rvert < 1)$$

and in the same manner, $(\arctan y)' = 1/(1 + y^2)$.

The derivative of the logarithm lets us extend the power rule to any real exponent $r$. For $x>0$ we have $x^r=e^{r\ln x}$, so by [Theorem 4](#thm4){: data-lid="9kebn" },

$$(x^r)'=e^{r\ln x}\cdot\frac{r}{x}=rx^{r-1}.$$

For a base $b>0$, writing $b^x=e^{x\ln b}$ gives the derivative by the chain rule. If $b\neq 1$, the change-of-base formula $\log_b x=(\ln x)/(\ln b)$ gives the derivative of the logarithm for $x>0$. The two formulas are

$$(b^x)'=b^x\ln b,\qquad (\log_b x)'=\frac{1}{x\ln b}.$$

For example, $(2^x)'=2^x\ln 2$.

Successive multiplication by $x$ reduces the amplitude of an oscillating function near the origin and can change its differentiability there.

::: Example 7 (Oscillation and differentiability)
For $x\neq 0$, set

$$f(x)=x\sin(1/x),\qquad g(x)=x^2\sin(1/x),$$

and define $f(0)=g(0)=0$. By [§Limits of Functions, ⁋Example 11](/en/math/calculus/functions_and_limits#ex11){: data-lid="i73q8" }, $f$ is continuous at $0$. Since $g(x)=xf(x)$, $g$ is also continuous at $0$. Their difference quotients at $0$ are

$$\frac{f(h)-f(0)}{h}=\sin(1/h),\qquad \frac{g(h)-g(0)}{h}=h\sin(1/h).$$

As $h\rightarrow 0$, the first expression oscillates without a limit, so $f$ is not differentiable at $0$. The second expression tends to $0$, so $g'(0)=0$.

For $x\neq 0$, the product rule and chain rule give

$$f'(x)=\sin(1/x)-\frac{\cos(1/x)}{x},\qquad g'(x)=2x\sin(1/x)-\cos(1/x).$$

As $x\rightarrow 0$, the first term of $g'(x)$ tends to $0$ and the second oscillates without a limit. Hence $g'$ is discontinuous at $0$. Thus $g$ is differentiable everywhere and fails the $C^1$ condition in [§Differentiation and Derivatives, ⁋Definition 6](/en/math/calculus/derivatives#def6){: data-lid="gd3pp" }.
:::

By *Darboux's theorem*, a derivative takes every value between its values at any two points, so it cannot have a jump discontinuity. The discontinuity of $g'$ in [Example 7](#ex7){: data-lid="e0sir" } arises from oscillation.

## Applications of Differentiation Rules

Finally, we conclude this post by examining how to apply the rules examined so far. First, although this direction somewhat puts the cart before the horse compared to the reason we introduced power series, [Proposition 1](#prop1){: data-lid="ms3m5" } can be used to evaluate series.

::: Example 8 (Sum of an infinite series)
Let us differentiate both sides of the geometric series ([§Infinite Series, ⁋Example 2](/en/math/calculus/series#ex2){: data-lid="we10a" }):

$$\frac{1}{1-x} = \sum_{n=0}^\infty x^n \qquad (\lvert x\rvert < 1)$$

By the chain rule, the left-hand side is

$$\left(\frac{1}{1-x}\right)' = 1/(1-x)^2$$

and applying [Proposition 1](#prop1){: data-lid="p7bvq" } to the right-hand side gives $\sum_{n\geq 1} n x^{n-1}$, so

$$\sum_{n=1}^\infty n x^{n-1} = \frac{1}{(1-x)^2} \qquad (\lvert x\rvert < 1)$$

and multiplying both sides by $x$, we obtain

$$\sum_{n\geq 1} n x^n = \frac{x}{(1-x)^2}$$

For instance, substituting $x = 1/2$, we can also compute the sum of the series $\sum_{n\geq 1} n/2^n = 2$.
:::

The second application is a result that fits this category of calculus a bit better, telling us a rule for actually differentiating a given function.

::: Example 9 (Various differentiation methods)
When an equation defines $y$ as a function of $x$, finding an explicit expression of the form $y=...$ in order to find $y'$ is often inefficient, or taking such a form often does not yield a clean derivative. In this situation, viewing $y$ as a function of $x$, differentiating both sides, and then solving for $y'$ is called *implicit differentiation*. For instance, differentiating both sides for the unit circle $x^2 + y^2 = 1$ gives

$$2x + 2y y' = 0$$

so at points where $y \neq 0$, we obtain $y' = -x/y$, and thus can find the slope of the tangent line at such a point $(x_0,y_0)$.

For functions with a variable in the exponent, *logarithmic differentiation* (taking the logarithm of both sides and then differentiating) is convenient. For example, for $y = x^x$ ($x > 0$), differentiating both sides of $\ln y = x\ln x$ and using $(\ln y)' = y'/y$ together with the product rule gives

$$\frac{y'}{y} = \ln x + 1 \quad\implies\quad y' = x^x(\ln x + 1)$$
:::

---

**References**

**[Ste]** J. Stewart, *Calculus*, 8th ed., Cengage Learning, 2016.  
**[Kim]** 김홍종, *미적분학 1·2*, 제3개정판, 서울대학교출판문화원, 2020.
