---
title: "Mean Value Theorem"
description: "We prove Rolle's theorem, the mean value theorem, and Cauchy's mean value theorem, and from them develop key applications of derivatives including tests for monotonicity, extrema, and convexity, as well as L'Hospital's rule and optimization."
excerpt: "Mean value theorem and applications: monotonicity, extrema, convexity tests, L'Hospital's rule, optimization"

categories: [Math / Calculus]
permalink: /en/math/calculus/mean_value_theorem
sidebar: 
    nav: "calculus-en"

date: 2026-06-23
weight: 8
translated_at: 2026-08-19T07:15:05+00:00
translation_source: kimi-cli
last_polished_at: 2026-09-29T23:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
In [§Differentiation and Derivatives](/en/math/calculus/derivatives){: data-lid="bt0mi" } we examined the definition of the derivative. Now we will examine what information the derivative carries about a function, and the first step is the mean value theorem.

## Rolle's Theorem and the Mean Value Theorem

::: Definition 1
A function $f$ is said to have a *local maximum* at a point $c$ if, for some open interval containing $c$, every $x$ satisfies $f(x) \leq f(c)$. A *local minimum* is defined symmetrically, and the two are collectively called *local extrema*.
:::

That is, intuitively, saying that $c$ is a local maximum or minimum means that if we consider a sufficiently small neighborhood around $c$, the function value at the point $c$ appears to be the minimum or maximum in that neighborhood. The simplest statement about this is the following.

::: Theorem 2 (Fermat)
If $f$ has a local extremum at an interior point $c$ and is differentiable at $c$, then $f'(c) = 0$.
:::

::: Proof
Consider the case where $f$ has a local maximum at $c$ (for a local minimum, consider $-f$). In a neighborhood of $c$, we have $f(x) \leq f(c)$, so the numerator of the difference quotient $(f(c+h)-f(c))/h$ is less than or equal to $0$. Therefore, on the side where $h > 0$, the difference quotient is less than or equal to $0$ and its limit is $f'(c) \leq 0$, while on the side where $h < 0$, the difference quotient is greater than or equal to $0$ and its limit is $f'(c) \geq 0$. Now, for $f$ to be differentiable at $c$, the two one-sided limits must be equal, so $f'(c) = 0$.
:::

A point where the derivative is $0$ or does not exist is called a *critical point*. Fermat's theorem states that an interior local extremum of a differentiable function must occur at a critical point. However, the converse is false. For example, for $f(x) = x^3$, at $x = 0$ we have $f'(0) = 0$, but it does not have a local extremum.

::: Theorem 3 (Rolle)
If $f$ is continuous on the closed interval $[a,b]$, differentiable on the open interval $(a,b)$, and $f(a) = f(b)$, then $f'(c) = 0$ for some $c \in (a,b)$.
:::

::: Proof
Since $f$ is continuous on $[a,b]$, by [§Continuous Functions, ⁋Theorem 4](/en/math/calculus/continuity#thm4){: data-lid="m699v" } it attains a maximum and a minimum on $[a,b]$. If both occur only at the endpoints, then since $f(a) = f(b)$, the maximum and minimum are equal, so $f$ is constant and $f' = 0$ at all interior points. Otherwise, at least one of the maximum or minimum occurs at an interior point $c$, and since $f$ has a local extremum at $c$, [Theorem 2](#thm2){: data-lid="n724d" } gives $f'(c) = 0$.
:::

::: Theorem 4 (Mean Value Theorem)
If $f$ is continuous on $[a,b]$ and differentiable on $(a,b)$, then

$$f'(c) = \frac{f(b) - f(a)}{b - a}$$

holds for some $c \in (a,b)$.
:::

::: Proof
Subtract the line connecting the two endpoints and apply [Theorem 3](#thm3){: data-lid="2vsww" }. If we define the auxiliary function

$$g(x) = f(x) - \left[ f(a) + \frac{f(b)-f(a)}{b-a}(x - a) \right]$$

then $g$ is continuous on $[a,b]$, differentiable on $(a,b)$, and $g(a) = g(b) = 0$. By [Theorem 3](#thm3){: data-lid="mzwsj" }, $g'(c) = 0$ for some $c \in (a,b)$, and since $g'(c) = f'(c) - (f(b)-f(a))/(b-a)$, the theorem follows.
:::

The claim of [Theorem 4](#thm4){: data-lid="6xez9" } is that somewhere on the interval the instantaneous rate of change equals the average rate of change, connecting the endpoint information $f(a), f(b)$ with the derivative on the interior.

## Applications of the Mean Value Theorem

Now let us examine in earnest how the shape of a function is determined by [Theorem 4](#thm4){: data-lid="1cmzw" }. First, as the simplest example, a function whose derivative is $0$ at all points is a constant function.

::: Corollary 5
If $f$ is differentiable on an interval $I$ and $f'(x) = 0$ at every point, then $f$ is constant on $I$. Consequently, if $f' = g'$ then $f - g$ is constant.
:::

::: Proof
For any two points in $I$ with $x_1 < x_2$, applying [Theorem 4](#thm4){: data-lid="5mly6" } to $[x_1, x_2]$ yields $f(x_2) - f(x_1) = f'(c)(x_2 - x_1) = 0$ for some $c$. Hence $f(x_1) = f(x_2)$ and $f$ is constant. The second claim follows because the derivative of $f - g$ is $0$.
:::

The following is a generalization of [Theorem 4](#thm4){: data-lid="ynuvk" }: whereas [Theorem 4](#thm4){: data-lid="gygau" } compared the growth of the function $f(x)$ with that of $g(x)=x$, the following theorem extends $g(x)$ to the general case. 

::: Theorem 6 (Cauchy)
If $f, g$ are continuous on $[a,b]$ and differentiable on $(a,b)$, then

$$\bigl(f(b) - f(a)\bigr)g'(c) = \bigl(g(b) - g(a)\bigr)f'(c)$$

holds for some $c \in (a,b)$. In particular, if $g(a) \neq g(b)$ and $g' \neq 0$, then $(f(b)-f(a))/(g(b)-g(a)) = f'(c)/g'(c)$.
:::

::: Proof
Setting the auxiliary function $h(x) = \bigl(f(b)-f(a)\bigr)g(x) - \bigl(g(b)-g(a)\bigr)f(x)$, we have $h(a) = h(b) = f(b)g(a) - f(a)g(b)$. By [Theorem 3](#thm3){: data-lid="dq0sk" }, $h'(c) = 0$ for some $c \in (a,b)$, which is precisely the claimed equality.
:::

Setting $g(x) = x$ in [Theorem 6](#thm6){: data-lid="omdku" }, we have $g'(c) = 1$ and $g(b) - g(a) = b - a$, recovering [Theorem 4](#thm4){: data-lid="h1271" }. 

The most frequent application of theorems of this form is to determine the increase or decrease of a function from the sign of its derivative. This is because replacing the difference of function values $f(x_2) - f(x_1)$ by $f'(c)(x_2 - x_1)$, the sign of the derivative determines the sign of this quantity.

::: Proposition 7
Let $f$ be continuous on an interval $I$ and differentiable in the interior of $I$. If at every interior point of $I$, $f'(x) > 0$, then $f$ is strictly increasing on $I$; if $f'(x) < 0$, then strictly decreasing. More weakly, if $f'(x) \geq 0$ at every interior point, then $f$ is nondecreasing.
:::

::: Proof
If we choose any two points in $I$ with $x_1 < x_2$, then $[x_1, x_2]$ is contained in $I$ and $(x_1, x_2)$ lies in the interior of $I$, so applying [Theorem 4](#thm4){: data-lid="8h96y" } to $[x_1, x_2]$ yields

$$f(x_2) - f(x_1) = f'(c)(x_2 - x_1), \qquad c \in (x_1, x_2)$$

for some $c$. Here, since $x_2 - x_1 > 0$, the sign of the right-hand side matches that of $f'(c)$. Therefore, if $f' > 0$ at all points, then $f(x_2) - f(x_1) > 0$, that is, $f(x_1) < f(x_2)$, so $f$ is strictly increasing; if $f' < 0$, strictly decreasing in the same manner; and if $f' \geq 0$, then $f(x_2) - f(x_1) \geq 0$, so $f$ is nondecreasing.
:::

This test is the most practical form of the fact that the derivative controls the function. One must be careful, however, that strict increase does not force $f' > 0$ at every point. For example, $f(x) = x^3$ is strictly increasing on $\mathbb{R}$ but $f'(0) = 0$. That is, the first part of [Proposition 7](#prop7){: data-lid="x8cfq" } is only a sufficient condition, not a necessary one.

::: Example 8
Now, to see an example using this result, let us show that for all $x > 0$, $\ln(1 + x) < x$. First, setting $f(x) = x - \ln(1+x)$, we have $f(0) = 0$ and

$$f'(x) = 1 - \frac{1}{1+x} = \frac{x}{1+x} > 0 \qquad (x > 0)$$

holds. By [Proposition 7](#prop7){: data-lid="11ha4" }, $f$ is strictly increasing on $[0, \infty)$, so if $x > 0$, then $f(x) > f(0) = 0$, that is, $x > \ln(1+x)$. Similarly, applying the same argument to $g(x) = \ln(1+x) - x/(1+x)$ gives $g(0) = 0$ and $g'(x) = x/(1+x)^2 > 0$, so $x/(1+x) < \ln(1+x)$ also follows; combining these, we see that

$$\frac{x}{1+x} < \ln(1+x) < x \qquad (x > 0)$$

holds.
:::

Meanwhile, by slightly shifting our viewpoint on the equality $f(b) - f(a) = f'(c)(b-a)$ in [Theorem 4](#thm4){: data-lid="0aups" }, we obtain a more quantitative result: on the interval $[a,b]$, the minimum and maximum of $f'(x)$ control the difference of function values.

::: Proposition 9
If $f$ is continuous on $[a,b]$, differentiable on $(a,b)$, and $m \leq f'(x) \leq M$ for all $x$, then

$$m(b - a) \leq f(b) - f(a) \leq M(b - a)$$

holds. In particular, if $\lvert f'(x)\rvert \leq L$, then $\lvert f(b) - f(a)\rvert \leq L\lvert b - a\rvert$.
:::

::: Proof
By [Theorem 4](#thm4){: data-lid="wcl4r" }, we pick a point satisfying $f(b) - f(a) = f'(c)(b-a)$ with $c \in (a,b)$. By assumption $m \leq f'(c) \leq M$ and $b - a > 0$, so multiplying through by $b - a$ gives

$$m(b-a) \leq f'(c)(b-a) \leq M(b-a)$$

and the middle term is $f(b) - f(a)$. The second claim follows by applying the same inequality to $-L \leq f'(x) \leq L$ to obtain $\lvert f(b) - f(a)\rvert \leq L(b-a)$.
:::

On the other hand, [Theorem 3](#thm3){: data-lid="crjto" } is also used to bound the number of roots of a function from above by the number of roots of its derivative. This is because between any two distinct roots of the function there must lie at least one root of the derivative.

{% diagram Math/Calculus/Mean_Value_Theorem-1.svg width="14.76em" alt="Parabola and tangent for root separation" %}

That is, intuitively, after a function has a root, in order to have the next root it must *turn* its direction of travel so that the function value returns to $0$, and this is accounted for as a point where the derivative becomes $0$. Writing this more clearly in mathematical terms, we have the following.

::: Proposition 10 (Root separation)
If $f$ is differentiable on an interval $I$ and $f'$ has on $I$ at most $k$ roots, then $f$ has on $I$ at most $k + 1$ roots.
:::

::: Proof
Assume for contradiction that $f$ has in $I$ distinct roots $x_0 < x_1 < \cdots < x_k < x_{k+1}$, $k + 2$ in number. On each adjacent pair $[x_{i-1}, x_i]$, since $f(x_{i-1}) = f(x_i) = 0$, by [Theorem 3](#thm3){: data-lid="27rz2" }

$$f'(c_i) = 0, \qquad c_i \in (x_{i-1}, x_i)$$

holds for some $c_i$. The points $c_1 < c_2 < \cdots < c_{k+1}$ obtained in this way are $k + 1$ distinct points, and since they are all roots of $f'$, this contradicts the assumption that $f'$ has at most $k$ roots. Therefore, $f$ has at most $k + 1$ roots.
:::

This principle is especially useful when dealing with the number of roots of non-polynomial functions, because for polynomials there generally exists a method (even if not always) to determine roots through the powerful tool of factorization, whereas for an arbitrary function this task is not so obvious. In the following example, we examine how this process works through a polynomial that does not factor.

::: Example 11
Let us show that the equation $x^3 + x - 1 = 0$ has exactly one real root. If we set $f(x) = x^3 + x - 1$, then $f(0) = -1 < 0$ and $f(1) = 1 > 0$, so by [§Continuous Functions, ⁋Theorem 5](/en/math/calculus/continuity#thm5){: data-lid="f44rx" } there is at least one root in $(0, 1)$. On the other hand, since

$$f'(x) = 3x^2 + 1 > 0$$

$f'$ has no roots. In [Proposition 10](#prop10){: data-lid="v03on" }, if $k = 0$, then $f$ has at most one root. Since there is at least one and at most one, there is exactly one real root.
:::

Recall from [Theorem 2](#thm2){: data-lid="nc9bw" } that extrema can only occur at critical points. Therefore, to find extrema we first locate critical points (which are relatively easy to find), and then determine which of them actually give extrema. The following proposition assists in this process.

::: Proposition 12
Let $f$ be continuous in a neighborhood of $c$ and differentiable in that neighborhood except at $c$. If to the left of $c$, $f' > 0$ and to the right $f' < 0$, then $f$ has a local maximum at $c$. If the signs are reversed, a local minimum; if there is no sign change, not an extremum.
:::

::: Proof
By [Proposition 7](#prop7){: data-lid="5uvtb" }, $f$ is increasing on the interval to the left of $c$ and decreasing on the interval to the right, so in a neighborhood of $c$, for all $x$ we have $f(x) \leq f(c)$. Hence $c$ is a local maximum. The remaining cases are similar.
:::

This test is immediately useful in optimization problems. If the domain is an open interval, it suffices to identify extrema among critical points; if the domain is a closed interval $[a, b]$, the endpoints are also candidates. This is because a continuous function attains a maximum and minimum on a closed bounded interval ([§Continuous Functions, ⁋Theorem 4](/en/math/calculus/continuity#thm4){: data-lid="erg9y" }), and these values occur only at critical points or at the endpoints of the interval.

::: Proposition 13 (Global extrema on a closed interval)
If $f$ is continuous on a closed bounded interval $[a, b]$ and differentiable on $(a, b)$, then the maximum and minimum values of $f$ are attained in the candidate set consisting of the critical points in $(a, b)$ and the two endpoints $a, b$.
:::

::: Proof
By [§Continuous Functions, ⁋Theorem 4](/en/math/calculus/continuity#thm4){: data-lid="g687d" }, $f$ attains a maximum at some point $c \in [a, b]$. If $c$ is an endpoint, it is in the candidate set. If $c$ lies in the interior $(a, b)$, then $f$ has a global maximum at $c$ and hence in particular a local maximum, so by [Theorem 2](#thm2){: data-lid="ks0f0" }, $f'(c) = 0$, that is, a critical point. The minimum is treated the same way. Thus both extrema occur within the specified set.
:::

For example, optimizing $f(x) = x^3 - 3x$ on $[-2, 2]$, by comparing the critical points of $f'(x) = 3(x-1)(x+1)$, namely $x = \pm 1$, and the values at the two endpoints $f(-2) = -2$, $f(-1) = 2$, $f(1) = -2$, $f(2) = 2$, we obtain the maximum $2$ ($x = -1, 2$) and minimum $-2$ ($x = -2, 1$).

The following is an example that brings together the criteria so far to analyze the entire graph of a function.

::: Example 14 (Comprehensive graph analysis)
Let the function $f(x) = x e^{-x}$ be given on $\mathbb{R}$. Its first and second derivatives are

$$f'(x) = (1 - x)e^{-x}, \qquad f''(x) = (x - 2)e^{-x}$$

Since $e^{-x} > 0$, the sign of $f'$ is determined by $1 - x$ and that of $f''$ by $x - 2$. Hence by [Proposition 7](#prop7){: data-lid="ixqid" }, the function is strictly increasing for $x < 1$ and strictly decreasing for $x > 1$. Also, by [Proposition 12](#prop12){: data-lid="n7l3e" }, from the change in sign of $f'$ at $x = 1$, it has the local maximum $f(1) = e^{-1}$. Finally, since $\lim_{x\rightarrow\infty} x e^{-x} = 0$ and $\lim_{x\rightarrow -\infty} x e^{-x} = -\infty$, the graph descends to negative infinity on the left, reaches at $x = 1$ the highest point $e^{-1}$, and then descends, asymptotically approaching the $x$-axis.
:::

## Extrema and Convexity Tests

While the first derivative carries information about extrema as above, the second derivative tells us the direction in which the graph bends.

::: Definition 15
A function $f$ is said to be *convex* on an interval $I$ if, for any two points in $I$, $x_1, x_2$, and any $0 \leq t \leq 1$,

$$f\bigl((1-t)x_1 + t x_2\bigr) \leq (1-t)f(x_1) + t f(x_2)$$

holds. That is, the graph lies below the chord joining the two points. If the inequality is reversed, it is called *concave*.
:::

::: Proposition 16
Let $f$ be twice differentiable on an interval $I$. If on $I$ we have $f''(x) \geq 0$, then $f$ is convex, and if $f''(x) \leq 0$, concave.
:::

::: Proof
If $f'' \geq 0$, then by [Proposition 7](#prop7){: data-lid="92e50" }, $f'$ is nondecreasing. That convexity is equivalent to $f'$ being increasing is verified by the mean value theorem. For $x_1 < x < x_2$, applying [Theorem 4](#thm4){: data-lid="cviq7" } to $[x_1, x]$ and $[x, x_2]$ yields $\xi_1 < \xi_2$ for some $\xi_1, \xi_2$ such that

$$\frac{f(x)-f(x_1)}{x - x_1} = f'(\xi_1) \leq f'(\xi_2) = \frac{f(x_2)-f(x)}{x_2 - x}$$

and rearranging this gives the inequality of [Definition 15](#def15){: data-lid="is9e5" }. In the case $f'' \leq 0$, one can apply the same argument to $-f$.
:::

A point where convexity and concavity separate, that is, where the bending direction of the graph changes, is called an *inflection point*. For example, for the function $f$ of [Example 14](#ex14){: data-lid="ssc5c" }, for $x < 2$ we have $f'' < 0$, so the function is concave here, and for $x > 2$ we have $f'' > 0$, so the function is convex here. In this case, the inflection point is $x = 2$, and across this boundary the bending direction of the graph changes.

The second derivative is also used in testing critical points.

::: Proposition 17 (Second derivative test)
If $f'(c) = 0$ and $f''(c) < 0$, then $f$ has a local maximum at $c$, and if $f''(c) > 0$, a local minimum.
:::

::: Proof
Suppose $f''(c) < 0$. Since $f'(c) = 0$,

$$f''(c) = \lim_{x\rightarrow c}\frac{f'(x) - f'(c)}{x - c} = \lim_{x\rightarrow c}\frac{f'(x)}{x - c} < 0$$

and therefore in a neighborhood of $c$ we have $f'(x)/(x - c) < 0$. That is, to the left of $c$ ($x < c$) we have $f'(x) > 0$, and to the right, $f'(x) < 0$; by [Proposition 12](#prop12){: data-lid="hi5kp" }, $f$ has a local maximum at $c$.
:::

Indeed, for the function $f$ of [Example 14](#ex14){: data-lid="9js2y" }, the value of the second derivative at the critical point $x=1$ is $-e^{-1}<0$, and one can verify that $f$ has a local maximum at $x=1$.

## Indeterminate Limits and L'Hôpital's Rule

Cauchy's mean value theorem converts indeterminate limits of the form $0/0$ into a ratio of derivatives.

::: Theorem 18 (L'Hôpital's rule)
Let $f, g$ be differentiable in some punctured neighborhood of $a$, with $g' \neq 0$ in that neighborhood, and suppose

$$\lim_{x\rightarrow a} f(x) = \lim_{x\rightarrow a} g(x) = 0$$

If the limit 

$$\lim_{x\rightarrow a} f'(x)/g'(x) = L$$

exists, then

$$\lim_{x \rightarrow a} \frac{f(x)}{g(x)} = L$$

:::

::: Proof
If we set $f(a) = g(a) = 0$ by (re)defining both functions at $a$, then both are continuous at $a$. Also, for $x$ in that neighborhood, if $g(x) = g(a)$, then by [Theorem 3](#thm3){: data-lid="42nuq" }, between $a$ and $x$ there would be a root of $g'$, contradicting the hypothesis; hence $g(x) \neq g(a) = 0$. Sufficiently close to $a$, for $x$, applying [Theorem 6](#thm6){: data-lid="wv4p9" } between $a$ and $x$ gives

$$\frac{f(x)}{g(x)} = \frac{f(x) - f(a)}{g(x) - g(a)} = \frac{f'(\xi_x)}{g'(\xi_x)}$$

there is $\xi_x$ between $a$ and $x$. As $x \rightarrow a$, we have $\xi_x \rightarrow a$, so the right-hand side converges to $L$.
:::

For example,

$$\lim_{x\rightarrow 0} (\sin x)/x$$

is of the form $0/0$, and the ratio of derivatives is $\cos x / 1 \rightarrow 1$, so the value is $1$. L'Hôpital's rule can be applied repeatedly if the resulting ratio is again indeterminate. Meanwhile, although the above theorem treated only the $0/0$ form at a finite point, the same Cauchy mean value theorem argument extends to cases involving infinity.

::: Remark 19
L'Hôpital's rule also holds in the following variants.

1. For one-sided limits $x \rightarrow a^+$, $x \rightarrow a^-$, it holds unchanged by sending $x$ to $a$ from only one side in the proof.
2. For $x \rightarrow \infty$, the $0/0$ form: if we substitute $t = 1/x$, then $F(t) = f(1/t)$ and $G(t) = g(1/t)$ become, as $t \rightarrow 0^+$, of the form $0/0$, and since by the chain rule $F'(t)/G'(t) = f'(1/t)/g'(1/t)$, this can be proved by applying 1.
3. For the limit $x\rightarrow a$, the case of the $\infty/\infty$ form where both the denominator and the numerator diverge requires a slight additional argument. First, for a fixed $x_0$, and for any point between $a$ and $x_0$, say $x$, by [Theorem 6](#thm6){: data-lid="ff7ky" }
    
    $$\frac{f(x)-f(x_0)}{g(x)-g(x_0)}=\frac{f'(\xi)}{g'(\xi)}$$

    holds for some $\xi$ between $x$ and $x_0$. If we choose $x_0$ close to $a$, the intermediate $\xi$ lying between them also gets close to $a$, so from the fact that, as in the hypothesis of [Theorem 18](#thm18){: data-lid="i7nes" }, as $\xi\rightarrow a$ the right-hand side converges to $L$, by choosing $x_0$ sufficiently close to $a$ we can also make the ratio on the left-hand side as close to $L$ as desired. Finally, keeping this chosen $x_0$ fixed and sending $x\rightarrow a$, since $f(x), g(x)\rightarrow\infty$, the contribution of the two fixed terms $f(x_0), g(x_0)$ vanishes, so the difference between the left-hand side and $f(x)/g(x)$ goes to $0$. Therefore, by first choosing $x_0$ to trap the left-hand side near $L$, and then sending $x$ sufficiently close to $a$, $f(x)/g(x)$ also becomes as close to $L$ as desired, which means $\lim_{x\rightarrow a} f(x)/g(x)=L$.
:::

---

**References**

**[Ste]** J. Stewart, *Calculus*, 8th ed., Cengage Learning, 2016.  
**[Kim]** 김홍종, *미적분학 1·2*, 제3개정판, 서울대학교출판문화원, 2020.
