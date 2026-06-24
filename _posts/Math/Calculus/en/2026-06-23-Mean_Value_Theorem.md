---
title: "Mean Value Theorem"
description: "We prove Rolle's theorem, the mean value theorem, and Cauchy's mean value theorem, then develop key applications of derivatives including tests for monotonicity, extrema, convexity, L'Hopital's rule, and optimization."
excerpt: "Mean value theorem and its applications: monotonicity, extrema, convexity, L'Hopital's rule, optimization"

categories: [Math / Calculus]
permalink: /en/math/calculus/mean_value_theorem
sidebar: 
    nav: "calculus-en"

date: 2026-06-23
weight: 8
translated_at: 2026-06-24T15:00:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-24T15:00:02+00:00
---
In [§Derivatives](/en/math/calculus/derivatives) we examined the definition of the derivative. Now we investigate what information the derivative carries about a function, and the first step is the mean value theorem.

## Rolle's Theorem and the Mean Value Theorem

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> A function $$f$$ is said to have a *local maximum* at a point $$c$$ if $$f(x) \leq f(c)$$ for all $$x$$ in some open interval containing $$c$$. A *local minimum* is defined symmetrically, and the two are collectively called a *local extremum*.

</div>

Intuitively, $$c$$ being a local maximum or minimum means that if we consider a sufficiently small neighborhood around $$c$$, the function value at $$c$$ appears to be the minimum or maximum within that neighborhood. The simplest statement about this is as follows.

<div class="proposition" markdown="1">

<ins id="thm2">**Theorem 2 (Fermat)**</ins> If $$f$$ has a local extremum at an interior point $$c$$ and is differentiable at $$c$$, then $$f'(c) = 0$$.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

Consider the case where $$c$$ is a local maximum (for a local minimum, look at $$-f$$). Since $$f(x) \leq f(c)$$ near $$c$$, the numerator of the difference quotient $$(f(c+h)-f(c))/h$$ is at most $$0$$. Thus for $$h > 0$$ the difference quotient is at most $$0$$ and its limit is $$f'(c) \leq 0$$, while for $$h < 0$$ the difference quotient is at least $$0$$ and its limit is $$f'(c) \geq 0$$. Since $$f$$ is differentiable at $$c$$, the two one-sided limits must agree, so $$f'(c) = 0$$.

</details>

A point where the derivative is $$0$$ or does not exist is called a *critical point*. Fermat's theorem says that an interior extremum of a differentiable function must occur at a critical point. However, the converse is false: for example, $$f(x) = x^3$$ has $$f'(0) = 0$$ but does not have a local extremum at $$x = 0$$.

<div class="proposition" markdown="1">

<ins id="thm3">**Theorem 3 (Rolle)**</ins> If $$f$$ is continuous on the closed interval $$[a,b]$$, differentiable on the open interval $$(a,b)$$, and $$f(a) = f(b)$$, then there exists $$c \in (a,b)$$ such that $$f'(c) = 0$$.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

Since $$f$$ is continuous on $$[a,b]$$, by [§Continuous Functions, ⁋Theorem 4](/en/math/calculus/continuity#thm4) it attains a maximum and a minimum on $$[a,b]$$. If both occur only at the endpoints, then since $$f(a) = f(b)$$ the maximum and minimum are equal, so $$f$$ is constant and $$f' = 0$$ at every interior point. Otherwise at least one of the maximum or minimum occurs at an interior point $$c$$, which is then a local extremum, so by [Theorem 2](#thm2) we have $$f'(c) = 0$$.

</details>

<div class="proposition" markdown="1">

<ins id="thm4">**Theorem 4 (Mean Value Theorem)**</ins> If $$f$$ is continuous on $$[a,b]$$ and differentiable on $$(a,b)$$, then there exists $$c \in (a,b)$$ satisfying

$$f'(c) = \frac{f(b) - f(a)}{b - a}.$$

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

Subtract the secant line through the two endpoints and apply [Theorem 3](#thm3). Define the auxiliary function

$$g(x) = f(x) - \left[ f(a) + \frac{f(b)-f(a)}{b-a}(x - a) \right].$$

Then $$g$$ is continuous on $$[a,b]$$, differentiable on $$(a,b)$$, and $$g(a) = g(b) = 0$$. By [Theorem 3](#thm3) there exists $$c \in (a,b)$$ with $$g'(c) = 0$$, and since $$g'(c) = f'(c) - (f(b)-f(a))/(b-a)$$ the theorem follows.

</details>

The assertion of [Theorem 4](#thm4) is that somewhere on the interval the instantaneous rate of change equals the average rate of change, thereby connecting the endpoint data $$f(a), f(b)$$ with the interior derivative.

## Applications of the Mean Value Theorem

Now let us examine in earnest how the shape of a function is determined from [Theorem 4](#thm4). As the simplest example, a function whose derivative is $$0$$ at every point is constant.

<div class="proposition" markdown="1">

<ins id="cor5">**Corollary 5**</ins> If $$f$$ is differentiable on an interval $$I$$ and $$f'(x) = 0$$ at every point, then $$f$$ is constant on $$I$$. Consequently, if $$f' = g'$$ then $$f - g$$ is constant.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

For any two points $$x_1 < x_2$$ in $$I$$, applying [Theorem 4](#thm4) to $$[x_1, x_2]$$ yields $$f(x_2) - f(x_1) = f'(c)(x_2 - x_1) = 0$$ for some $$c$$. Hence $$f(x_1) = f(x_2)$$ and $$f$$ is constant. The second claim follows because the derivative of $$f - g$$ is $$0$$.

</details>

Next is a generalization of [Theorem 4](#thm4): whereas [Theorem 4](#thm4) compared the growth of $$f(x)$$ and $$g(x)=x$$, the following theorem extends this to a general $$g(x)$$.

<div class="proposition" markdown="1">

<ins id="thm6">**Theorem 6 (Cauchy)**</ins> If $$f, g$$ are continuous on $$[a,b]$$ and differentiable on $$(a,b)$$, then there exists $$c \in (a,b)$$ satisfying

$$\bigl(f(b) - f(a)\bigr)g'(c) = \bigl(g(b) - g(a)\bigr)f'(c).$$

In particular, if $$g(a) \neq g(b)$$ and $$g' \neq 0$$, then $$(f(b)-f(a))/(g(b)-g(a)) = f'(c)/g'(c)$$.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

Define the auxiliary function $$h(x) = \bigl(f(b)-f(a)\bigr)g(x) - \bigl(g(b)-g(a)\bigr)f(x)$$; then $$h(a) = h(b) = f(b)g(a) - f(a)g(b)$$. By [Theorem 3](#thm3) there exists $$c \in (a,b)$$ with $$h'(c) = 0$$, which is exactly the claimed equality.

</details>

Setting $$g(x) = x$$ in [Theorem 6](#thm6) gives $$g'(c) = 1$$ and $$g(b) - g(a) = b - a$$, so [Theorem 4](#thm4) is recovered.

The form in which such theorems are most often applied is reading the increase or decrease of a function from the sign of its derivative. Replacing the difference of function values $$f(x_2) - f(x_1)$$ by $$f'(c)(x_2 - x_1)$$, the sign of the derivative immediately determines the sign of this value.

<div class="proposition" markdown="1">

<ins id="prop7">**Proposition 7**</ins> Let $$f$$ be differentiable on an interval $$I$$. If $$f'(x) > 0$$ at every interior point of $$I$$, then $$f$$ is strictly increasing on $$I$$; if $$f'(x) < 0$$, it is strictly decreasing. More weakly, if $$f'(x) \geq 0$$ then $$f$$ is non-decreasing.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

Pick any two points $$x_1 < x_2$$ in $$I$$ and apply [Theorem 4](#thm4) to $$[x_1, x_2]$$ to obtain

$$f(x_2) - f(x_1) = f'(c)(x_2 - x_1), \qquad c \in (x_1, x_2).$$

Since $$x_2 - x_1 > 0$$, the sign of the right-hand side matches that of $$f'(c)$$. Thus if $$f' > 0$$ everywhere, then $$f(x_2) - f(x_1) > 0$$, i.e. $$f(x_1) < f(x_2)$$, so $$f$$ is strictly increasing; similarly for $$f' < 0$$, and if $$f' \geq 0$$ then $$f(x_2) - f(x_1) \geq 0$$ so $$f$$ is not decreasing.

</details>

This test is the most practical form of the fact that the derivative controls the function. Note that strict increase does not force $$f' > 0$$ at every point: for example, $$f(x) = x^3$$ is strictly increasing on $$\mathbb{R}$$ but $$f'(0) = 0$$. Thus the first part of [Proposition 7](#prop7) is only a sufficient condition, not a necessary one.

<div class="example" markdown="1">

<ins id="ex8">**Example 8**</ins> As an example using this result, we show that $$\ln(1 + x) < x$$ for all $$x > 0$$. Set $$f(x) = x - \ln(1+x)$$; then $$f(0) = 0$$ and

$$f'(x) = 1 - \frac{1}{1+x} = \frac{x}{1+x} > 0 \qquad (x > 0).$$

By [Proposition 7](#prop7), $$f$$ is strictly increasing on $$[0, \infty)$$, so for $$x > 0$$ we have $$f(x) > f(0) = 0$$, i.e. $$x > \ln(1+x)$$. Similarly, applying the same argument to $$g(x) = \ln(1+x) - x/(1+x)$$ gives $$g(0) = 0$$ and $$g'(x) = x/(1+x)^2 > 0$$, so $$x/(1+x) < \ln(1+x)$$ as well. Combining these,

$$\frac{x}{1+x} < \ln(1+x) < x \qquad (x > 0).$$

</div>

Meanwhile, by shifting perspective slightly on the equality $$f(b) - f(a) = f'(c)(b-a)$$ from [Theorem 4](#thm4), we obtain a more quantitative result: the minimum and maximum of $$f'(x)$$ on $$[a,b]$$ control the difference of function values.

<div class="proposition" markdown="1">

<ins id="prop9">**Proposition 9**</ins> If $$f$$ is continuous on $$[a,b]$$, differentiable on $$(a,b)$$, and $$m \leq f'(x) \leq M$$ for all $$x$$, then

$$m(b - a) \leq f(b) - f(a) \leq M(b - a).$$

In particular, if $$\lvert f'(x)\rvert \leq L$$ then $$\lvert f(b) - f(a)\rvert \leq L\lvert b - a\rvert$$.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

By [Theorem 4](#thm4) pick $$c \in (a,b)$$ with $$f(b) - f(a) = f'(c)(b-a)$$. By hypothesis $$m \leq f'(c) \leq M$$ and $$b - a > 0$$, so multiplying the three inequalities by $$b - a$$ yields

$$m(b-a) \leq f'(c)(b-a) \leq M(b-a),$$

and the middle term is $$f(b) - f(a)$$. The second claim follows by applying the same inequality to $$-L \leq f'(x) \leq L$$ to obtain $$\lvert f(b) - f(a)\rvert \leq L(b-a)$$.

</details>

Meanwhile, [Theorem 3](#thm3) is also used to bound the number of zeros of a function from above by the number of zeros of its derivative. This is because between any two distinct zeros of the function there must lie at least one zero of the derivative.

![Parabola and tangent for root separation](/assets/images/Math/Calculus/Mean_Value_Theorem-1.svg){:style="width:14.76em" class="invert" .align-center}

Intuitively, after a function has a zero, in order to reach the next zero it must <em>turn around</em> so that the function value returns to $$0$$, and this turning point is where the derivative becomes $$0$$. Stating this more precisely:

<div class="proposition" markdown="1">

<ins id="prop10">**Proposition 10 (Root Separation)**</ins> If $$f$$ is differentiable on an interval $$I$$ and $$f'$$ has at most $$k$$ zeros on $$I$$, then $$f$$ has at most $$k + 1$$ zeros on $$I$$.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

Assume for contradiction that $$f$$ has $$k + 2$$ distinct zeros $$x_0 < x_1 < \cdots < x_k < x_{k+1}$$ on $$I$$. On each adjacent pair $$[x_{i-1}, x_i]$$ we have $$f(x_{i-1}) = f(x_i) = 0$$, so by [Theorem 3](#thm3) there exists

$$f'(c_i) = 0, \qquad c_i \in (x_{i-1}, x_i).$$

The points $$c_1 < c_2 < \cdots < c_{k+1}$$ thus obtained are $$k + 1$$ distinct zeros of $$f'$$, contradicting the hypothesis that $$f'$$ has at most $$k$$ zeros. Hence $$f$$ has at most $$k + 1$$ zeros.

</details>

This principle is especially useful when dealing with the number of zeros of non-polynomial functions, because for polynomials there is usually (though not always) the strong tool of factorization to locate zeros, whereas for arbitrary functions this is far from obvious. In the next example we illustrate how this works for a polynomial that does not factor nicely.

<div class="example" markdown="1">

<ins id="ex11">**Example 11**</ins> We show that the equation $$x^3 + x - 1 = 0$$ has exactly one real root. Set $$f(x) = x^3 + x - 1$$; then $$f(0) = -1 < 0$$ and $$f(1) = 1 > 0$$, so by [§Continuous Functions, ⁋Theorem 5](/en/math/calculus/continuity#thm5) there is at least one root in $$(0, 1)$$. On the other hand,

$$f'(x) = 3x^2 + 1 > 0,$$

so $$f'$$ has no zeros. Taking $$k = 0$$ in [Proposition 10](#prop10), $$f$$ has at most one zero. Since there is at least one and at most one, there is exactly one real root.

</div>

Recall from [Theorem 2](#thm2) that local extrema can occur only at critical points. Therefore, to find extrema we first locate the critical points (which are relatively easy to find) and then determine which of them actually give extrema. The following proposition assists in this process.

<div class="proposition" markdown="1">

<ins id="prop12">**Proposition 12**</ins> Let $$f$$ be continuous near $$c$$ and differentiable in a punctured neighborhood of $$c$$. If $$f' > 0$$ to the left of $$c$$ and $$f' < 0$$ to the right of $$c$$, then $$f$$ has a local maximum at $$c$$. If the signs are reversed, it is a local minimum; if there is no sign change, it is not a local extremum.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

By [Proposition 7](#prop7), $$f$$ is increasing on the left interval of $$c$$ and decreasing on the right interval, so for all $$x$$ near $$c$$ we have $$f(x) \leq f(c)$$. Hence $$c$$ is a local maximum. The remaining cases are similar.

</details>

Such tests are used directly in optimization problems. If the domain is an open interval, it suffices to screen critical points for extrema; if the domain is a closed interval $$[a, b]$$, the endpoints are also candidates. A continuous function on a closed bounded interval attains its maximum and minimum ([§Continuous Functions, ⁋Theorem 4](/en/math/calculus/continuity#thm4)), and these values occur only at critical points or at the endpoints of the interval.

<div class="proposition" markdown="1">

<ins id="prop13">**Proposition 13 (Global Extrema on a Closed Interval)**</ins> If $$f$$ is continuous on a closed bounded interval $$[a, b]$$ and differentiable on $$(a, b)$$, then the maximum and minimum values of $$f$$ are attained among the finite candidate set consisting of the critical points in $$(a, b)$$ and the two endpoints $$a, b$$.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

By [§Continuous Functions, ⁋Theorem 4](/en/math/calculus/continuity#thm4), $$f$$ attains its maximum at some point $$c \in [a, b]$$. If $$c$$ is an endpoint, it is in the candidate set. If $$c$$ lies in the interior $$(a, b)$$, then it is a global maximum and hence in particular a local maximum, so by Fermat's theorem ([Theorem 2](#thm2)) we have $$f'(c) = 0$$, i.e. $$c$$ is a critical point. The minimum is analogous. Thus both extrema occur within the stated finite set.

</details>

For example, to optimize $$f(x) = x^3 - 3x$$ on $$[-2, 2]$$, we compare the values at the critical points $$x = \pm 1$$ of $$f'(x) = 3(x-1)(x+1)$$ with the endpoint values $$f(-2) = -2$$, $$f(-1) = 2$$, $$f(1) = -2$$, $$f(2) = 2$$, obtaining maximum $$2$$ (at $$x = -1, 2$$) and minimum $$-2$$ (at $$x = -2, 1$$).

Next is an example that assembles the tests developed so far to analyze the entire graph of a function.

<div class="example" markdown="1">

<ins id="ex14">**Example 14 (Comprehensive Graph Analysis)**</ins> Let the function $$f(x) = x e^{-x}$$ be given on $$\mathbb{R}$$. Its first and second derivatives are

$$f'(x) = (1 - x)e^{-x}, \qquad f''(x) = (x - 2)e^{-x}.$$

Since $$e^{-x} > 0$$, the sign of $$f'$$ is determined by $$1 - x$$ and the sign of $$f''$$ by $$x - 2$$. Thus by [Proposition 7](#prop7) the function is strictly increasing for $$x < 1$$ and strictly decreasing for $$x > 1$$. Moreover, by [Proposition 12](#prop12), the sign change of $$f'$$ at $$x = 1$$ gives a local maximum with value $$f(1) = e^{-1}$$. Finally, since $$\lim_{x\to\infty} x e^{-x} = 0$$ and $$\lim_{x\to -\infty} x e^{-x} = -\infty$$, the graph descends from negative infinity on the left, reaches its highest point $$e^{-1}$$ at $$x = 1$$, and then asymptotically approaches the $$x$$-axis.

</div>

## Tests for Extrema and Convexity

If the first derivative contains information about extrema as above, the second derivative tells us the direction in which the graph bends.

<div class="definition" markdown="1">

<ins id="def15">**Definition 15**</ins> A function $$f$$ is said to be *convex* on an interval $$I$$ if for any two points $$x_1, x_2$$ in $$I$$ and any $$0 \leq t \leq 1$$,

$$f\bigl((1-t)x_1 + t x_2\bigr) \leq (1-t)f(x_1) + t f(x_2)$$

holds. That is, the graph lies below the chord joining the two points. If the inequality is reversed, $$f$$ is called *concave*.

</div>

<div class="proposition" markdown="1">

<ins id="prop16">**Proposition 16**</ins> Let $$f$$ be twice differentiable on an interval $$I$$. If $$f''(x) \geq 0$$ on $$I$$ then $$f$$ is convex; if $$f''(x) \leq 0$$ then $$f$$ is concave.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

If $$f'' \geq 0$$ then by [Proposition 7](#prop7), $$f'$$ is increasing. That convexity is equivalent to $$f'$$ being increasing can be verified by the mean value theorem. For $$x_1 < x < x_2$$, applying [Theorem 4](#thm4) to $$[x_1, x]$$ and $$[x, x_2]$$ yields $$\xi_1 < \xi_2$$ with

$$\frac{f(x)-f(x_1)}{x - x_1} = f'(\xi_1) \leq f'(\xi_2) = \frac{f(x_2)-f(x)}{x_2 - x},$$

and rearranging gives the inequality of [Definition 15](#def15).

</details>

A point where convex and concave change, i.e. where the bending direction of the graph changes, is called an *inflection point*. For example, for the function $$f$$ of [Example 14](#ex14), we have $$f'' < 0$$ for $$x < 2$$ so the function is concave there, and $$f'' > 0$$ for $$x > 2$$ so it is convex there. The inflection point is $$x = 2$$, and the graph changes its bending direction across this point.

The second derivative is also used to test critical points.

<div class="proposition" markdown="1">

<ins id="prop17">**Proposition 17 (Second Derivative Test)**</ins> If $$f'(c) = 0$$ and $$f''(c) < 0$$ then $$f$$ has a local maximum at $$c$$; if $$f''(c) > 0$$ then it has a local minimum.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

Suppose $$f''(c) < 0$$. Since $$f'(c) = 0$$,

$$f''(c) = \lim_{x\to c}\frac{f'(x) - f'(c)}{x - c} = \lim_{x\to c}\frac{f'(x)}{x - c} < 0,$$

so near $$c$$ we have $$f'(x)/(x - c) < 0$$. That is, to the left of $$c$$ ($$x < c$$) we have $$f'(x) > 0$$ and to the right $$f'(x) < 0$$, so by [Proposition 12](#prop12), $$c$$ is a local maximum.

</details>

Indeed, for the function $$f$$ of [Example 14](#ex14), at the critical point $$x=1$$ the second derivative has value $$-e^{-1} < 0$$, confirming that $$f$$ has a local maximum at $$x=1$$.

## Indeterminate Limits and L'Hôpital's Rule

Cauchy's mean value theorem converts $$0/0$$ indeterminate limits into a ratio of derivatives.

<div class="proposition" markdown="1">

<ins id="thm18">**Theorem 18 (L'Hôpital's Rule)**</ins> Let $$f, g$$ be differentiable near $$a$$ with $$g' \neq 0$$, and suppose

$$\lim_{x\to a} f(x) = \lim_{x\to a} g(x) = 0.$$

If the limit

$$\lim_{x\to a} f'(x)/g'(x) = L$$

exists, then

$$\lim_{x \to a} \frac{f(x)}{g(x)} = L.$$

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

Define (or redefine) $$f(a) = g(a) = 0$$ so that both functions are continuous at $$a$$. For $$x$$ sufficiently close to $$a$$, applying [Theorem 6](#thm6) between $$a$$ and $$x$$ gives

$$\frac{f(x)}{g(x)} = \frac{f(x) - f(a)}{g(x) - g(a)} = \frac{f'(\xi_x)}{g'(\xi_x)}$$

for some $$\xi_x$$ between $$a$$ and $$x$$. As $$x \to a$$ we also have $$\xi_x \to a$$, so the right-hand side converges to $$L$$.

</details>

For example,

$$\lim_{x\to 0} (\sin x)/x$$

is of the form $$0/0$$, and the ratio of derivatives is $$\cos x / 1 \to 1$$, so the value is $$1$$. L'Hôpital's rule can be applied repeatedly if the ratio after one application is again indeterminate. The theorem above only treated the $$0/0$$ form at a finite point, but the same Cauchy mean value argument extends to cases involving infinity.

<div class="remark" markdown="1">

<ins id="rmk19">**Remark 19**</ins> L'Hôpital's rule also holds in the following variants.

1. One-sided limits $$x \to a^+$$, $$x \to a^-$$: the proof works unchanged if we send $$x$$ to $$a$$ from only one side.
2. The $$0/0$$ form as $$x \to \infty$$: substitute $$t = 1/x$$; then $$F(t) = f(1/t)$$, $$G(t) = g(1/t)$$ become a $$0/0$$ form as $$t \to 0^+$$, and by the chain rule $$F'(t)/G'(t) = f'(1/t)/g'(1/t)$$, so case 1 reduces it.
3. The $$\infty/\infty$$ form where numerator and denominator both diverge as $$x \to a$$ requires a small additional argument. Fix $$x_0$$; then for $$x$$ between $$a$$ and $$x_0$$, by [Theorem 6](#thm6) there exists $$\xi$$ between $$x$$ and $$x_0$$ such that
    
    $$\frac{f(x)-f(x_0)}{g(x)-g(x_0)}=\frac{f'(\xi)}{g'(\xi)}.$$
    
    Choosing $$x_0$$ close to $$a$$ forces $$\xi$$ close to $$a$$ as well, so under the hypothesis of [Theorem 18](#thm18) the right-hand side converges to $$L$$ as $$\xi \to a$$. Hence by taking $$x_0$$ sufficiently close to $$a$$, the left-hand ratio can be made arbitrarily close to $$L$$. Finally, since $$f(x), g(x)\to\infty$$ as $$x\to a$$, the fixed terms $$f(x_0), g(x_0)$$ become negligible, so this ratio has the same limit as $$f(x)/g(x)$$, and therefore $$\lim_{x\to a} f(x)/g(x)=L$$.

</div>
