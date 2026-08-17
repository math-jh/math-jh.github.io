---
title: "Mean Value Theorem"
description: "We prove Rolle's theorem, the mean value theorem, and Cauchy's mean value theorem, then develop key applications of derivatives including tests for monotonicity, extrema, and convexity, as well as L'Hospital's rule and optimization."
excerpt: "Mean value theorem and its applications: monotonicity, extrema, convexity, L'Hospital's rule, optimization"

categories: [Math / Calculus]
permalink: /en/math/calculus/mean_value_theorem
sidebar: 
    nav: "calculus-en"

date: 2026-06-23
weight: 8
translated_at: 2026-08-17T19:49:26+00:00
translation_source: kimi-cli
---
In [§Differentiation and Derivatives](/en/math/calculus/derivatives) we examined the definition of the derivative. Now we turn to what information the derivative carries about a function, and the first key result is the mean value theorem.

## Rolle's Theorem and the Mean Value Theorem

::: Definition 1
A function $f$ is said to have a *local maximum* at a point $c$ if $f(x) \leq f(c)$ for every $x$ in some open interval containing $c$. A *local minimum* is defined symmetrically, and the two are collectively called *local extrema*.
:::

Intuitively, saying that $c$ is a local maximum or minimum means that if we look at a sufficiently small neighborhood around $c$, the function value at $c$ appears to be the largest or smallest in that neighborhood. The simplest statement about this is the following.

::: Theorem 2 (Fermat)
If $f$ has a local extremum at an interior point $c$ and is differentiable at $c$, then $f'(c) = 0$.
:::

::: Proof
Consider the case where $f$ has a local maximum at $c$ (the local minimum case follows by looking at $-f$). Since $f(x) \leq f(c)$ in a neighborhood of $c$, the numerator of the difference quotient $(f(c+h)-f(c))/h$ is non-positive. Hence for $h > 0$ the difference quotient is non-positive and its limit gives $f'(c) \leq 0$, while for $h < 0$ the difference quotient is non-negative and its limit gives $f'(c) \geq 0$. Since $f$ is differentiable at $c$, the two one-sided limits must agree, so $f'(c) = 0$.
:::

A point where the derivative is zero or does not exist is called a *critical point*. Fermat's theorem says that any interior local extremum of a differentiable function must occur at a critical point. The converse is false: for example, $f(x) = x^3$ satisfies $f'(0) = 0$ but has no extremum at $x = 0$.

::: Theorem 3 (Rolle)
If $f$ is continuous on the closed interval $[a,b]$, differentiable on the open interval $(a,b)$, and $f(a) = f(b)$, then there exists $c \in (a,b)$ such that $f'(c) = 0$.
:::

::: Proof
Since $f$ is continuous on $[a,b]$, by [§Continuous Functions, ⁋Theorem 4](/en/math/calculus/continuity#thm4) it attains a maximum and a minimum on $[a,b]$. If both occur only at the endpoints, then $f(a) = f(b)$ implies the maximum and minimum are equal, so $f$ is constant and $f' = 0$ at every interior point. Otherwise at least one of the maximum or minimum occurs at an interior point $c$, and since $f$ then has a local extremum at $c$, [Theorem 2](#thm2) gives $f'(c) = 0$.
:::

::: Theorem 4 (Mean Value Theorem)
If $f$ is continuous on $[a,b]$ and differentiable on $(a,b)$, then there exists $c \in (a,b)$ such that

$$f'(c) = \frac{f(b) - f(a)}{b - a}.$$

:::

::: Proof
Subtract the secant line through the two endpoints and apply [Theorem 3](#thm3). Set

$$g(x) = f(x) - \left[ f(a) + \frac{f(b)-f(a)}{b-a}(x - a) \right].$$

Then $g$ is continuous on $[a,b]$, differentiable on $(a,b)$, and $g(a) = g(b) = 0$. By [Theorem 3](#thm3) there exists $c \in (a,b)$ with $g'(c) = 0$, and since $g'(c) = f'(c) - (f(b)-f(a))/(b-a)$, the theorem follows.
:::

The claim of [Theorem 4](#thm4) is that somewhere on the interval the instantaneous rate of change equals the average rate of change, thereby connecting the endpoint data $f(a), f(b)$ with the interior derivative.

## Applications of the Mean Value Theorem

Now let us examine in earnest how the shape of a function is determined by [Theorem 4](#thm4). The simplest example is that a function whose derivative is zero everywhere must be constant.

::: Corollary 5
If $f$ is differentiable on an interval $I$ and $f'(x) = 0$ at every point, then $f$ is constant on $I$. Consequently, if $f' = g'$ then $f - g$ is constant.
:::

::: Proof
For any two points $x_1 < x_2$ in $I$, applying [Theorem 4](#thm4) to $[x_1, x_2]$ yields $f(x_2) - f(x_1) = f'(c)(x_2 - x_1) = 0$ for some $c$. Hence $f(x_1) = f(x_2)$ and $f$ is constant. The second claim follows because the derivative of $f - g$ is zero.
:::

The next result generalizes [Theorem 4](#thm4): whereas [Theorem 4](#thm4) compared the growth of $f(x)$ with that of $g(x) = x$, the following theorem extends this to a general $g(x)$.

::: Theorem 6 (Cauchy)
If $f, g$ are continuous on $[a,b]$ and differentiable on $(a,b)$, then there exists $c \in (a,b)$ such that

$$\bigl(f(b) - f(a)\bigr)g'(c) = \bigl(g(b) - g(a)\bigr)f'(c).$$

In particular, if $g(a) \neq g(b)$ and $g' \neq 0$, then $(f(b)-f(a))/(g(b)-g(a)) = f'(c)/g'(c)$.
:::

::: Proof
Set $h(x) = \bigl(f(b)-f(a)\bigr)g(x) - \bigl(g(b)-g(a)\bigr)f(x)$. Then $h(a) = h(b) = f(b)g(a) - f(a)g(b)$. By [Theorem 3](#thm3) there exists $c \in (a,b)$ with $h'(c) = 0$, which is exactly the claimed equality.
:::

Setting $g(x) = x$ in [Theorem 6](#thm6) gives $g'(c) = 1$ and $g(b) - g(a) = b - a$, recovering [Theorem 4](#thm4).

The most frequent application of results of this form is reading the increase or decrease of a function from the sign of its derivative. Replacing the difference $f(x_2) - f(x_1)$ by $f'(c)(x_2 - x_1)$, the sign of the derivative immediately determines the sign of this value.

::: Proposition 7
Let $f$ be continuous on an interval $I$ and differentiable in the interior of $I$. If $f'(x) > 0$ at every interior point of $I$, then $f$ is strictly increasing on $I$; if $f'(x) < 0$, then strictly decreasing. More weakly, if $f'(x) \geq 0$ at every interior point, then $f$ is non-decreasing.
:::

::: Proof
Pick any two points $x_1 < x_2$ in $I$; then $[x_1, x_2] \subseteq I$ and $(x_1, x_2)$ lies in the interior of $I$, so applying [Theorem 4](#thm4) to $[x_1, x_2]$ yields

$$f(x_2) - f(x_1) = f'(c)(x_2 - x_1), \qquad c \in (x_1, x_2).$$

Since $x_2 - x_1 > 0$, the sign of the right-hand side matches that of $f'(c)$. Thus if $f' > 0$ everywhere, then $f(x_2) - f(x_1) > 0$, i.e. $f(x_1) < f(x_2)$, so $f$ is strictly increasing; if $f' < 0$, strictly decreasing in the same way; and if $f' \geq 0$, then $f(x_2) - f(x_1) \geq 0$, so $f$ is non-decreasing.
:::

This test is the most practical form of the fact that the derivative controls the function. One must be careful, however, that strict increase does not force $f' > 0$ at every point. For example, $f(x) = x^3$ is strictly increasing on $\mathbb{R}$ but $f'(0) = 0$. Thus the first part of [Proposition 7](#prop7) is only a sufficient condition, not a necessary one.

::: Example 8
As an application, let us show that $\ln(1 + x) < x$ for all $x > 0$. Set $f(x) = x - \ln(1+x)$; then $f(0) = 0$ and

$$f'(x) = 1 - \frac{1}{1+x} = \frac{x}{1+x} > 0 \qquad (x > 0).$$

By [Proposition 7](#prop7), $f$ is strictly increasing on $[0, \infty)$, so for $x > 0$ we have $f(x) > f(0) = 0$, i.e. $x > \ln(1+x)$. Similarly, applying the same argument to $g(x) = \ln(1+x) - x/(1+x)$ gives $g(0) = 0$ and $g'(x) = x/(1+x)^2 > 0$, yielding $x/(1+x) < \ln(1+x)$. Combining these,

$$\frac{x}{1+x} < \ln(1+x) < x \qquad (x > 0).$$

:::

Meanwhile, by slightly shifting our viewpoint on the equality $f(b) - f(a) = f'(c)(b-a)$ from [Theorem 4](#thm4), we obtain a more quantitative result: the minimum and maximum of $f'(x)$ on $[a,b]$ control the difference of function values.

::: Proposition 9
If $f$ is continuous on $[a,b]$, differentiable on $(a,b)$, and $m \leq f'(x) \leq M$ for all $x$, then

$$m(b - a) \leq f(b) - f(a) \leq M(b - a).$$

In particular, if $\lvert f'(x)\rvert \leq L$, then $\lvert f(b) - f(a)\rvert \leq L\lvert b - a\rvert$.
:::

::: Proof
By [Theorem 4](#thm4) pick $c \in (a,b)$ with $f(b) - f(a) = f'(c)(b-a)$. By assumption $m \leq f'(c) \leq M$ and $b - a > 0$, so multiplying through by $b - a$ gives

$$m(b-a) \leq f'(c)(b-a) \leq M(b-a),$$

and the middle term is $f(b) - f(a)$. The second claim follows by applying the same inequality to $-L \leq f'(x) \leq L$ to obtain $\lvert f(b) - f(a)\rvert \leq L(b-a)$.
:::

On the other hand, [Theorem 3](#thm3) is also used to bound the number of roots of a function by the number of roots of its derivative. This is because between any two distinct roots of the function there must lie at least one root of the derivative.

{% diagram Math/Calculus/Mean_Value_Theorem-1.svg width="14.76em" alt="Parabola and tangent for root separation" %}

Intuitively, after a function has a root, in order to reach the next root it must *turn around* and bring the function value back to $0$, and the point where this turn occurs is where the derivative becomes $0$. Stated more mathematically:

::: Proposition 10 (Root separation)
If $f$ is differentiable on an interval $I$ and $f'$ has at most $k$ roots in $I$, then $f$ has at most $k + 1$ roots in $I$.
:::

::: Proof
Assume for contradiction that $f$ has $k + 2$ distinct roots $x_0 < x_1 < \cdots < x_k < x_{k+1}$ in $I$. On each adjacent pair $[x_{i-1}, x_i]$ we have $f(x_{i-1}) = f(x_i) = 0$, so by [Theorem 3](#thm3) there exists

$$f'(c_i) = 0, \qquad c_i \in (x_{i-1}, x_i).$$

The points $c_1 < c_2 < \cdots < c_{k+1}$ thus obtained are $k + 1$ distinct points, all roots of $f'$, contradicting the assumption that $f'$ has at most $k$ roots. Hence $f$ has at most $k + 1$ roots.
:::

This principle is especially useful when dealing with non-polynomial functions, because while polynomials have the powerful tool of factorization to analyze roots (not always, but often), for arbitrary functions this is far from obvious. In the next example we illustrate how this works for a polynomial that does not factor nicely.

::: Example 11
Let us show that the equation $x^3 + x - 1 = 0$ has exactly one real root. Set $f(x) = x^3 + x - 1$; then $f(0) = -1 < 0$ and $f(1) = 1 > 0$, so by [§Continuous Functions, ⁋Theorem 5](/en/math/calculus/continuity#thm5) there is at least one root in $(0, 1)$. On the other hand,

$$f'(x) = 3x^2 + 1 > 0,$$

so $f'$ has no roots. Taking $k = 0$ in [Proposition 10](#prop10), $f$ has at most one root. Since there is at least one and at most one, there is exactly one real root.
:::

Recall from [Theorem 2](#thm2) that extrema can only occur at critical points. Therefore, to find extrema we first locate critical points (which are relatively easy to find), and then determine which of them actually give extrema. The following proposition assists in this process.

::: Proposition 12
Let $f$ be continuous in a neighborhood of $c$ and differentiable in that neighborhood except possibly at $c$. If $f' > 0$ to the left of $c$ and $f' < 0$ to the right of $c$, then $f$ has a local maximum at $c$. If the signs are reversed, a local minimum; if there is no sign change, not an extremum.
:::

::: Proof
By [Proposition 7](#prop7), $f$ is increasing on the interval to the left of $c$ and decreasing on the interval to the right, so for all $x$ in a neighborhood of $c$ we have $f(x) \leq f(c)$. Hence $c$ is a local maximum. The remaining cases are similar.
:::

This test is immediately useful in optimization problems. If the domain is an open interval, it suffices to identify extrema among critical points; if the domain is a closed interval $[a, b]$, the endpoints are also candidates. This is because a continuous function attains a maximum and minimum on a closed bounded interval ([§Continuous Functions, ⁋Theorem 4](/en/math/calculus/continuity#thm4)), and these values occur only at critical points or at the endpoints of the interval.

::: Proposition 13 (Global extrema on a closed interval)
If $f$ is continuous on a closed bounded interval $[a, b]$ and differentiable on $(a, b)$, then the maximum and minimum values of $f$ are attained among the candidate set consisting of the critical points in $(a, b)$ and the two endpoints $a, b$.
:::

::: Proof
By [§Continuous Functions, ⁋Theorem 4](/en/math/calculus/continuity#thm4), $f$ attains its maximum at some point $c \in [a, b]$. If $c$ is an endpoint, it is in the candidate set. If $c$ lies in the interior $(a, b)$, then $f$ has a global maximum at $c$ and hence in particular a local maximum, so by [Theorem 2](#thm2) we have $f'(c) = 0$, i.e. $c$ is a critical point. The minimum is treated the same way. Thus both extrema occur in the specified set.
:::

For example, to optimize $f(x) = x^3 - 3x$ on $[-2, 2]$, we compare the values at the critical points $x = \pm 1$ of $f'(x) = 3(x-1)(x+1)$ and the two endpoints: $f(-2) = -2$, $f(-1) = 2$, $f(1) = -2$, $f(2) = 2$, obtaining maximum $2$ (at $x = -1, 2$) and minimum $-2$ (at $x = -2, 1$).

The following example brings together all the criteria developed so far to analyze the complete graph of a single function.

::: Example 14 (Comprehensive graph analysis)
Let $f(x) = x e^{-x}$ be given on $\mathbb{R}$. Its first and second derivatives are

$$f'(x) = (1 - x)e^{-x}, \qquad f''(x) = (x - 2)e^{-x}.$$

Since $e^{-x} > 0$, the sign of $f'$ is determined by $1 - x$ and that of $f''$ by $x - 2$. Hence by [Proposition 7](#prop7) the function is strictly increasing for $x < 1$ and strictly decreasing for $x > 1$. Moreover, by [Proposition 12](#prop12), $f$ has a local maximum at $x = 1$ where the sign of $f'$ changes, with value $f(1) = e^{-1}$. Finally, since $\lim_{x\rightarrow\infty} x e^{-x} = 0$ and $\lim_{x\rightarrow -\infty} x e^{-x} = -\infty$, the graph descends from negative infinity on the left, reaches its highest point $e^{-1}$ at $x = 1$, and then asymptotically approaches the $x$-axis.
:::

## Extrema and Convexity Tests

Just as the first derivative carries information about extrema, the second derivative tells us the direction in which the graph bends.

::: Definition 15
A function $f$ is *convex* on an interval $I$ if for any two points $x_1, x_2$ in $I$ and any $0 \leq t \leq 1$,

$$f\bigl((1-t)x_1 + t x_2\bigr) \leq (1-t)f(x_1) + t f(x_2).$$

That is, the graph lies below the chord joining the two points. If the inequality is reversed, $f$ is called *concave*.
:::

::: Proposition 16
Let $f$ be twice differentiable on an interval $I$. If $f''(x) \geq 0$ on $I$, then $f$ is convex; if $f''(x) \leq 0$, then $f$ is concave.
:::

::: Proof
If $f'' \geq 0$, then by [Proposition 7](#prop7) the derivative $f'$ is non-decreasing. That convexity is equivalent to $f'$ being increasing can be verified using the mean value theorem. For $x_1 < x < x_2$, applying [Theorem 4](#thm4) to $[x_1, x]$ and $[x, x_2]$ yields $\xi_1 < \xi_2$ with

$$\frac{f(x)-f(x_1)}{x - x_1} = f'(\xi_1) \leq f'(\xi_2) = \frac{f(x_2)-f(x)}{x_2 - x},$$

and rearranging gives the inequality of [Definition 15](#def15). The case $f'' \leq 0$ follows by applying the same argument to $-f$.
:::

A point where convex and concave behavior switch, i.e. where the bending direction of the graph changes, is called an *inflection point*. For example, for the function $f$ of [Example 14](#ex14), we have $f'' < 0$ for $x < 2$, so the function is concave there, and $f'' > 0$ for $x > 2$, so it is convex there. The inflection point is $x = 2$, and the bending direction of the graph changes across this point.

The second derivative is also useful in testing critical points.

::: Proposition 17 (Second derivative test)
If $f'(c) = 0$ and $f''(c) < 0$, then $f$ has a local maximum at $c$; if $f''(c) > 0$, a local minimum.
:::

::: Proof
Suppose $f''(c) < 0$. Since $f'(c) = 0$,

$$f''(c) = \lim_{x\rightarrow c}\frac{f'(x) - f'(c)}{x - c} = \lim_{x\rightarrow c}\frac{f'(x)}{x - c} < 0,$$

so in a neighborhood of $c$ we have $f'(x)/(x - c) < 0$. That is, $f'(x) > 0$ to the left of $c$ ($x < c$) and $f'(x) < 0$ to the right, and by [Proposition 12](#prop12) $f$ has a local maximum at $c$.
:::

Indeed, for the function $f$ of [Example 14](#ex14), the value of the second derivative at the critical point $x=1$ is $-e^{-1}<0$, confirming that $f$ has a local maximum at $x=1$.

## Indeterminate Limits and L'Hôpital's Rule

Cauchy's mean value theorem converts $0/0$ indeterminate limits into a ratio of derivatives.

::: Theorem 18 (L'Hôpital's rule)
Let $f, g$ be differentiable in some punctured neighborhood of $a$, with $g' \neq 0$ in that neighborhood, and suppose

$$\lim_{x\rightarrow a} f(x) = \lim_{x\rightarrow a} g(x) = 0.$$

If the limit

$$\lim_{x\rightarrow a} f'(x)/g'(x) = L$$

exists, then

$$\lim_{x \rightarrow a} \frac{f(x)}{g(x)} = L.$$

:::

::: Proof
Redefine $f(a) = g(a) = 0$ so that both functions are continuous at $a$. Also, for $x$ in the neighborhood, if $g(x) = g(a)$ then by [Theorem 3](#thm3) there would be a root of $g'$ between $a$ and $x$, contradicting the hypothesis; hence $g(x) \neq g(a) = 0$. For $x$ sufficiently close to $a$, applying [Theorem 6](#thm6) between $a$ and $x$ gives

$$\frac{f(x)}{g(x)} = \frac{f(x) - f(a)}{g(x) - g(a)} = \frac{f'(\xi_x)}{g'(\xi_x)}$$

for some $\xi_x$ between $a$ and $x$. As $x \rightarrow a$, we have $\xi_x \rightarrow a$, so the right-hand side converges to $L$.
:::

For example,

$$\lim_{x\rightarrow 0} (\sin x)/x$$

is of the form $0/0$, and the ratio of derivatives is $\cos x / 1 \rightarrow 1$, so the value is $1$. L'Hôpital's rule can be applied repeatedly if the resulting ratio is again indeterminate. The theorem above treated only the $0/0$ form at a finite point, but the same Cauchy mean value argument extends to cases involving infinity.

::: Remark 19
L'Hôpital's rule also holds in the following variants.

1. For one-sided limits $x \rightarrow a^+$, $x \rightarrow a^-$, the proof works unchanged by sending $x$ to $a$ from only one side.
2. For $x \rightarrow \infty$ in the $0/0$ form, set $t = 1/x$; then $F(t) = f(1/t)$ and $G(t) = g(1/t)$ give a $0/0$ form as $t \rightarrow 0^+$, and by the chain rule $F'(t)/G'(t) = f'(1/t)/g'(1/t)$, so variant 1 applies.
3. For the $\infty/\infty$ form where both numerator and denominator diverge as $x \rightarrow a$, a small additional argument is needed. Fix $x_0$; then for $x$ between $a$ and $x_0$, by [Theorem 6](#thm6) there exists $\xi$ between $x$ and $x_0$ such that
    
    $$\frac{f(x)-f(x_0)}{g(x)-g(x_0)}=\frac{f'(\xi)}{g'(\xi)}.$$
    
    Taking $x_0$ close to $a$ forces the intermediate $\xi$ close to $a$ as well, so under the hypothesis of [Theorem 18](#thm18) the right-hand side converges to $L$ as $\xi \rightarrow a$. Hence by choosing $x_0$ sufficiently close to $a$ we can make the left-hand ratio as close to $L$ as desired. Then keeping this $x_0$ fixed and sending $x \rightarrow a$, since $f(x), g(x)\rightarrow\infty$ the contribution of the fixed terms $f(x_0), g(x_0)$ vanishes and the difference between the left-hand side and $f(x)/g(x)$ goes to $0$. Thus first trapping the left-hand side near $L$ by choosing $x_0$, and then sending $x$ sufficiently close to $a$, brings $f(x)/g(x)$ arbitrarily close to $L$, which means $\lim_{x\rightarrow a} f(x)/g(x)=L$.
:::

---

**References**

**[Ste]** J. Stewart, *Calculus*, 8th ed., Cengage Learning, 2016.  
**[Kim]** 김홍종, *미적분학 1·2*, 제3개정판, 서울대학교출판문화원, 2020.
