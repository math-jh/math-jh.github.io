---
title: "Integration"
description: "Indefinite integrals (antiderivatives) are defined as the inverse operation of differentiation, and definite integrals are introduced as limits of Riemann sums over partitions. The text covers the fact that two antiderivatives differ only by a constant, the linearity and basic formulas of indefinite integrals, the integrability of continuous functions, the linearity, interval additivity, and monotonicity of integrals, the mean value theorem, and its meaning as signed area."
excerpt: "Antiderivatives, indefinite integrals, Riemann sums, definite integrals, properties, and mean value theorem"

categories: [Math / Calculus]
permalink: /en/math/calculus/integration
sidebar: 
    nav: "calculus-en"

date: 2026-06-26
weight: 10
translated_at: 2026-08-19T09:15:05+00:00
translation_source: kimi-cli
last_polished_at: 2026-09-30T15:15:07+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
We have so far defined the limit of a function and, using the limit of the average rate of change, defined the derivative. In this post, we organize integration, the inverse operation of that process, and examine its various properties. 

## Antiderivatives

::: Definition 1
For a function $f$ defined on an interval $I$, a differentiable function $F$ satisfying $F'(x) = f(x)$ at every point of $I$ is called an *antiderivative* of $f$.
:::

For example, $F(x) = x^2$ is an antiderivative of $f(x) = 2x$. However, $x^2 + 1$ and $x^2 - 5$ also both have derivative $2x$, so they are antiderivatives as well. That is, adding a constant to an antiderivative still yields an antiderivative. Geometrically, an entire family of curves obtained by shifting the same curve vertically all share the same derivative (the same slope distribution). Antiderivatives are thus not unique, but they can differ only by a constant term.

::: Proposition 2
If $F$ is an antiderivative of $f$ on an interval $I$, then every antiderivative of $f$ has the form $F(x) + C$ for some constant $C$.
:::

::: Proof
If $G$ is also an antiderivative of $f$, then $(G - F)' = f - f = 0$. By [§Mean Value Theorem, ⁋Corollary 5](/en/math/calculus/mean_value_theorem#cor5){: data-lid="urwiw" }, a function whose derivative is identically $0$ on an interval is constant, so there exists a constant $C$ with $G - F = C$, hence $G = F + C$.
:::

In accordance with this proposition, we collect all antiderivatives of $f$ into a single expression, written as

$$\int f(x)\dd{x} = F(x) + C$$

and call this the *indefinite integral* of $f$. Here, we regard $C$ as the *constant of integration*, $f$ as the *integrand*, and the symbol $\dd{x}$ as indicating the variable of integration. Thanks to the fact, guaranteed by [Proposition 2](#prop2){: data-lid="p0x8b" }, that they differ "only by a constant", we can represent all antiderivatives at once with the single constant of integration $C$.

What we implicitly assume, namely that the interval is connected, is not strictly essential, but the above proposition holds only when the interval is connected. This is because if the domain is disconnected, the constant may differ on each piece. For instance, $1/x$ is defined separately for $x > 0$ and $x < 0$; since adding different constants on the two pieces to $F(x) = \ln\lvert x\rvert$ also yields antiderivatives of $1/x$, the statement that they differ "only by a constant" does not literally apply on the entire domain.

Under the assumption that the interval is connected, the constant of integration $C$ is uniquely determined once an *initial condition* is given. This is the basic method of solving differential equations using indefinite integrals. For example, if $F'(x) = 3x^2 + 1$ and $F(1) = 5$, substituting the initial condition into the indefinite integral $F(x) = x^3 + x + C$ yields $1 + 1 + C = 5$, that is, $C = 3$, so that $F(x) = x^3 + x + 3$ is uniquely determined. 

## Properties and Examples of Indefinite Integrals

Meanwhile, in [§Differentiation](/en/math/calculus/differentiation_rules){: data-lid="vu214" }, we examined the derivatives of various functions, and because indefinite integration is the reverse of differentiation, we can derive integration formulas from them. First, before that, let us show the linearity of indefinite integrals.

::: Proposition 3 (Linearity of indefinite integration)
If $f, g$ have antiderivatives and $a, b$ are constants, then

$$\int \bigl(a f(x) + b g(x)\bigr)\dd{x} = a\int f(x)\dd{x} + b\int g(x)\dd{x}$$

:::

::: Proof
Let $F, G$ be antiderivatives of $f, g$ respectively. Then by [§Differentiation and Derivatives, ⁋Proposition 4](/en/math/calculus/derivatives#prop4){: data-lid="3pj9t" },

$$(aF + bG)' = aF' + bG' = af + bg$$

so $aF + bG$ is an antiderivative of $af + bg$.
:::

Reversing the derivative formulas for various functions from [§Differentiation](/en/math/calculus/differentiation_rules){: data-lid="drxbj" } now yields the following basic formulas. That is, differentiating the right-hand side of each formula recovers the integrand.

$$\int x^r\dd{x} = \frac{x^{r+1}}{r+1} + C\ (r \neq -1), \qquad \int \frac{1}{x}\dd{x} = \ln\lvert x\rvert + C,$$

$$\int e^x\dd{x} = e^x + C, \qquad \int \cos x\dd{x} = \sin x + C, \qquad \int \sin x\dd{x} = -\cos x + C,\qquad \int \sec^2 x\dd{x} = \tan x + C,$$

$$\int \frac{\dd{x}}{1 + x^2} = \arctan x + C, \qquad \int \frac{\dd{x}}{\sqrt{1 - x^2}} = \arcsin x + C.$$

Combining linearity with these formulas allows us to integrate arbitrary sums of basic functions term by term. When the integrand is not in standard form, we first manipulate it using other tools, for instance rewriting via the trigonometric identity

$$\tan^2 x = \sec^2 x - 1$$

or splitting the fraction $(x^2+1)/x$ into $x + 1/x$ so that each term matches one of the formulas above.

Especially useful are integration by substitution and integration by parts, which are respectively the reverses of [§Differentiation, ⁋Theorem 4](/en/math/calculus/differentiation_rules#thm4){: data-lid="vhmth" } and [§Differentiation, ⁋Proposition 3](/en/math/calculus/differentiation_rules#prop3){: data-lid="4c97f" }.

::: Theorem 4 (Integration by substitution)
If $f$ has an antiderivative on an interval $I$, $g$ is differentiable, and for all $x$, $g(x) \in I$, then

$$\int f(g(x)) g'(x) \dd{x} = \int f(u) \dd{u} \quad (u = g(x))$$

:::

::: Proof
Let $F$ be an antiderivative of $f$. Then by [§Differentiation, ⁋Theorem 4](/en/math/calculus/differentiation_rules#thm4){: data-lid="lftt1" },

$$\frac{d}{\dd{x}}F(g(x)) = F'(g(x))g'(x) = f(g(x))g'(x)$$

so $F(g(x))$ is an antiderivative of the left-hand integrand. Therefore $\int f(g(x))g'(x)\dd{x} = F(g(x)) + C = F(u) + C = \int f(u)\dd{u}$.
:::

In practice, one sets $u = g(x)$ and $\dd{u} = g'(x) \dd{x}$, rewrites the expression entirely in terms of $u$, integrates, and then substitutes back. For example, with $u = \cos x$,

$$\int \tan x \dd{x} = -\int \frac{\dd{u}}{u} = -\ln\lvert\cos x\rvert + C$$

and by the same method

$$\int \frac{x}{x^2+1} \dd{x} = \frac{1}{2}\ln(x^2+1) + C$$

is obtained.

::: Theorem 5 (Integration by parts)
If $u, v$ are differentiable and their derivatives are continuous, then

$$\int u v' \dd{x} = uv - \int u' v \dd{x}$$

:::

::: Proof
By [§Differentiation, ⁋Proposition 3](/en/math/calculus/differentiation_rules#prop3){: data-lid="wys3l" }, $(uv)' = u'v + uv'$, so $uv' = (uv)' - u'v$, and integrating both sides, the claim follows from $\int (uv)' \dd{x} = uv$.
:::

The key is to choose $u$ as the factor that simplifies upon differentiation, and $v'$ as the factor that can be integrated. For example, in $\int x e^x \dd{x}$, setting $u = x$ gives $xe^x - e^x + C$, while for functions such as logarithms or inverse trigonometric functions whose derivatives actually become simpler, we take $v' = 1$ and place them in the $u$ position ($\int \ln x \dd{x} = x\ln x - x + C$). There are also cases where integration by parts does not simplify the integrand but returns to the original integral; then we treat the original integral as an unknown and solve algebraically.

::: Example 6
$I = \int e^x\cos x \dd{x}$ returns to itself after two applications of integration by parts. Setting $u = e^x$ and $v' = \cos x$,

$$I = e^x\sin x - \int e^x\sin x \dd{x} = e^x\sin x - \Bigl(-e^x\cos x + \int e^x\cos x \dd{x}\Bigr) = e^x(\sin x + \cos x) - I$$

so $2I = e^x(\sin x + \cos x)$, that is,

$$I = \frac{e^x(\sin x + \cos x)}{2} + C$$

:::

For rational functions whose denominator factors, decomposing into partial fractions allows each piece to be integrated into a logarithm or arctangent. For instance, splitting

$$\frac{1}{x^2-1} = \frac{1}{2}\left(\frac{1}{x-1} - \frac{1}{x+1}\right)$$

gives

$$\int \frac{\dd{x}}{x^2 - 1} = \frac{1}{2}\ln\left\lvert\frac{x-1}{x+1}\right\rvert + C$$

and when the denominator contains an irreducible quadratic, one can complete the square and make use of the arctangent as in

$$\int \frac{\dd{x}}{x^2 + 2x + 5} = \frac{1}{2}\arctan\frac{x+1}{2} + C$$

Radical expressions such as $\sqrt{a^2 - x^2}$ and $\sqrt{a^2 + x^2}$ can have their radicals eliminated by trigonometric substitution. For example, in $\int \sqrt{1 - x^2} \dd{x}$, setting $x = \sin\theta$ yields

$$\int \cos^2\theta \dd{\theta} = \frac{1}{2}(\arcsin x + x\sqrt{1-x^2}) + C$$

Powers of trigonometric functions themselves are reduced in degree using identities or handled by substitution. Odd powers are integrated by setting aside one factor and substituting, as in

$$\int \sin^3 x \dd{x} = -\cos x + \frac{1}{3}\cos^3 x + C$$

while even powers are reduced in degree via double-angle formulas to obtain

$$\int \sin^2 x \dd{x} = \frac{x}{2} - \frac{\sin 2x}{4} + C$$

Repeated integration by parts yields recurrence relations that lower the degree one step at a time, systematically treating integrals involving mixed powers.

::: Example 7 (Recurrence relation)
For $I_n = \int x^n e^x \dd{x}$, integration by parts with $u = x^n$ and $v' = e^x$ gives

$$I_n = x^n e^x - n I_{n-1}$$

Starting from $I_0 = e^x$, one obtains

$$I_1 = (x-1)e^x, \quad I_2 = (x^2 - 2x + 2)e^x$$

by descending in degree. In the same manner, one also obtains the recurrence relation

$$\int \sin^n x \dd{x} = -\frac{1}{n} \sin^{n-1}x\cos x + \frac{n-1}{n}\int \sin^{n-2}x \dd{x}$$

:::

Even with these techniques, some integrals cannot be expressed in terms of elementary functions, such as $\int e^{-x^2} \dd{x}$ or $\int (\sin x)/x \dd{x}$. Such functions are nevertheless well defined as definite integrals, and that they define new functions in their own right will be seen in the Fundamental Theorem of Calculus.

## Partitions and Riemann Sums

The integration examined above is defined as the inverse operation of differentiation, but historically integration began in a different way, namely from the problem of finding the total amount when a quantity accumulates. For example, measuring the area under the curve $y = f(x)$ over the interval $[a,b]$ falls into this category. The idea of the following definition is to approximate this area by slicing it into thin rectangles and making the subdivision arbitrarily fine.

::: Definition 8
A *partition* $P$ of the closed interval $[a, b]$ is a finite set of points $a = x_0 < x_1 < \cdots < x_n = b$. The length of each subinterval $[x_{i-1}, x_i]$ is denoted $\Delta x_i = x_i - x_{i-1}$, and the length of the longest subinterval is called the *mesh* $\lVert P\rVert = \max_i \Delta x_i$ of the partition. Choosing a sample point $c_i \in [x_{i-1}, x_i]$ in each subinterval, the sum

$$S(P, f) = \sum_{i=1}^{n} f(c_i)\Delta x_i$$

is called the *Riemann sum* of the function $f$.
:::

{% diagram Math/Calculus/Integration-1.svg width="24.05em" alt="Riemann sum" %}

A Riemann sum is the area approximating the region under the curve by rectangles of width $\Delta x_i$ and height $f(c_i)$. Taking the sample points $c_i$ to be the left endpoint, the right endpoint, or points giving the minimum or maximum of the function on each subinterval yields, respectively, the left and right Riemann sums, and the lower and upper sums. Intuitively, we expect that as the partition is made infinitely fine, this approximation converges to a single value independent of the choice of sample points.

::: Definition 9
If there exists a real number $S$ such that for every $\epsilon > 0$ there is a $\delta > 0$ such that $\lvert S(P, f) - S\rvert < \epsilon$ holds for all partitions with $\lVert P\rVert < \delta$ and all choices of sample points, then $f$ is said to be *integrable* on $[a,b]$ and $S$ is called the *definite integral*, written as

$$\int_a^b f(x)\dd{x} = S$$

$a$ and $b$ are called the lower and upper limits of integration, respectively.
:::

This definition can be applied directly to compute definite integrals. Dividing $[0,1]$ into $n$ equal parts and choosing the right endpoint $c_i = i/n$, the Riemann sum for

$$\int_0^1 x\dd{x}$$

is

$$\sum_{i=1}^n \frac{i}{n}\cdot\frac{1}{n} = \frac{1}{n^2}\cdot\frac{n(n+1)}{2} = \frac{n+1}{2n} \rightarrow \frac{1}{2}$$

and in the same way,

$$\int_0^1 x^2\dd{x} = \lim_{n\rightarrow\infty}\sum_{i=1}^n \frac{i^2}{n^3} = \lim_{n\rightarrow\infty}\frac{n(n+1)(2n+1)}{6n^3} = \frac{1}{3}$$

In particular, the first result can also be trivially checked from the area formula for a triangle.

::: Theorem 10
A function continuous on $[a, b]$ is integrable.
:::

The proof of this theorem also lies beyond our current scope, so we must accept it and move on. The following three facts concerning integrability are also at the same level, so we shall accept and use them together in subsequent arguments.

- A function integrable on $[a,b]$ is also integrable on any subinterval.
- If $f$ is integrable, then $\lvert f\rvert$ is also integrable.
- The product of two integrable functions is also integrable.

## Properties of the Definite Integral

Meanwhile, since a Riemann sum is defined as a sum and a limit, the definite integral inherits the following properties.

::: Proposition 11
If $f, g$ are integrable on $[a,b]$, then the following hold.

1. For constants $\alpha, \beta$, $\int_a^b (\alpha f(x) + \beta g(x))\dd{x} = \alpha\int_a^b f(x)\dd{x} + \beta\int_a^b g(x)\dd{x}$.
2. For $a < c < b$, $\int_a^b f(x)\dd{x} = \int_a^c f(x)\dd{x} + \int_c^b f(x)\dd{x}$.
3. If for all $x$ we have $f(x) \leq g(x)$, then $\int_a^b f(x)\dd{x} \leq \int_a^b g(x)\dd{x}$.
:::

::: Proof
All three properties hold at the level of Riemann sums and are preserved in the limit. Linearity follows from $S(P, \alpha f + \beta g) = \alpha S(P, f) + \beta S(P, g)$, and monotonicity follows from $f(c_i) \leq g(c_i)$ implying $S(P, f) \leq S(P, g)$. The second result is obtained by considering only partitions that include $c$ as a subdivision point, so that the Riemann sum splits into the Riemann sums over the two subintervals.
:::

By convention, setting $\int_a^a f(x)\dd{x} = 0$ and $\int_b^a f(x)\dd{x} = -\int_a^b f(x)\dd{x}$ makes the second result valid regardless of the order of $a, b, c$. From the third result, two useful computations follow. First, if $m \leq f \leq M$, then

$$m(b-a) \leq \int_a^b f(x)\dd{x} \leq M(b-a)$$

Second, applying this to $-\lvert f\rvert \leq f \leq \lvert f\rvert$ yields the integral version of the triangle inequality:

$$\left\lvert \int_a^b f(x)\dd{x}\right\rvert  \leq \int_a^b \lvert f(x)\rvert \dd{x}$$

Applying the first inequality to continuous functions, one can show that the integral value is attained exactly by the function value at some point.

::: Proposition 12 (Mean Value Theorem for Integrals)
If $f$ is continuous on $[a,b]$, then 

$$\int_a^b f(x)\dd{x} = f(c)(b-a)$$

holds for some $c \in [a,b]$.
:::

::: Proof
By [§Continuous Functions, ⁋Theorem 4](/en/math/calculus/continuity#thm4){: data-lid="zio3w" }, $f$ attains a minimum $m$ and a maximum $M$ on $[a,b]$. From the above computation, the average value 

$$\frac{1}{b-a}\int_a^b f(x)\dd{x}$$

lies in $[m, M]$. If this value equals $m$ or $M$, we choose $c$ to be a point attaining the minimum or maximum (the case where $f$ is constant, so $m = M$, is included here); otherwise we apply [§Continuous Functions, ⁋Theorem 5](/en/math/calculus/continuity#thm5){: data-lid="4qkel" } to the interval between the points attaining the minimum and maximum to obtain a $c$ taking that value, that is, such that $f(c) = \frac{1}{b-a}\int_a^b f(x)\dd{x}$ holds for $c$.
:::

Here 

$$\frac{1}{b-a}\int_a^b f(x)\dd{x}$$

is called the *average value* of $f$ on $[a,b]$, and [Proposition 12](#prop12){: data-lid="t4k2u" } states that a continuous function actually attains its average value at least at one point.

## Area and Applications

The definite integral is most intuitively understood as *signed* area. For instance, on an interval where $f < 0$, the terms $f(c_i)\Delta x_i$ of the Riemann sum are negative, so $\int_a^b f(x)\dd{x}$ attaches a minus sign to the region enclosed by the $x$-axis and $f$. This perspective becomes especially clear when the sign of the function changes over the interval of integration, and in distinguishing the case where a single integral cancels positive and negative areas to give $0$ from the case where the actual area requires absolute values, the integral version of the triangle inequality examined above appears as a strict inequality.

::: Example 13
The reason $\int_{-1}^{1} x\dd{x} = 0$ is that the negative area on $[-1,0]$ and the positive area on $[0,1]$ cancel exactly. Each piece is a right triangle with base and height $1$, so its area is $\frac{1}{2}$, and splitting using the second result of [Proposition 11](#prop11){: data-lid="p6uew" } gives

$$\int_{-1}^{1} x\dd{x} = \int_{-1}^{0} x\dd{x} + \int_{0}^{1} x\dd{x} = -\frac{1}{2} + \frac{1}{2} = 0$$

If one wants the *actual* area enclosed by the curve and the $x$-axis, one must integrate $\lvert x\rvert$ with the sign removed, giving

$$\int_{-1}^{1} \lvert x\rvert \dd{x} = \int_{-1}^{0} (-x)\dd{x} + \int_{0}^{1} x\dd{x} = \frac{1}{2} + \frac{1}{2} = 1$$

This is a concrete instance where the integral version of the triangle inequality $\bigl\lvert\int_a^b f(x) \dd{x}\bigr\rvert \leq \int_a^b \lvert f(x)\rvert \dd{x}$ holds not with equality but with the strict inequality $0 < 1$, and the value of each piece is verified immediately from the area of a triangle. This calculation also agrees with the earlier computation of the area of a triangle via Riemann sums.
:::

Because the Mean Value Theorem replaces an integral by a function value at a single point, it is frequently used when dealing with inequalities or inferring average properties. For an integral multiplied by a weight as well, the same theorem holds as long as the sign of the weight is constant.

::: Proposition 14 (Weighted Mean Value Theorem)
If $f$ is continuous on $[a,b]$ and $\mu$ is integrable on $[a,b]$ with $\mu \geq 0$, then there exists $c \in [a,b]$ such that

$$\int_a^b f(x)\mu(x)\dd{x} = f(c)\int_a^b \mu(x)\dd{x}$$

:::

::: Proof
By [§Continuous Functions, ⁋Theorem 4](/en/math/calculus/continuity#thm4){: data-lid="utufw" }, $f$ attains a minimum $m$ and a maximum $M$. Since $\mu \geq 0$, we have $m\mu(x) \leq f(x)\mu(x) \leq M\mu(x)$, and integrating using monotonicity and linearity gives

$$m\int_a^b \mu(x)\dd{x} \leq \int_a^b f(x)\mu(x) \dd{x}\leq M\int_a^b \mu(x) \dd{x}$$

If $\int_a^b \mu(x)\dd{x} = 0$, then the middle integral is also $0$, so the equality holds for any $c$. If $\int_a^b \mu(x)\dd{x} > 0$, dividing the above inequality by this value yields

$$\frac{\int_a^b f(x)\mu(x) \dd{x}}{\int_a^b \mu(x)\dd{x}} \in [m, M]$$

If this value equals $m$ or $M$, we choose $c$ to be a point attaining the minimum or maximum; otherwise, we apply [§Continuous Functions, ⁋Theorem 5](/en/math/calculus/continuity#thm5){: data-lid="ryo7o" } to the interval between the two points attaining the minimum and maximum to obtain $c$ taking this value. Therefore, multiplying both sides by $\int_a^b \mu(x)\dd{x}$ yields the claimed equality.
:::

If we set $\mu \equiv 1$, the Weighted Mean Value Theorem reduces to [Proposition 12](#prop12){: data-lid="2y8p5" }; thus [Proposition 14](#prop14){: data-lid="wvmxj" } can be thought of as a generalization of the Mean Value Theorem, adding a kind of density.

---

**References**

**[Ste]** J. Stewart, *Calculus*, 8th ed., Cengage Learning, 2016.  
**[Kim]** 김홍종, *미적분학 1·2*, 제3개정판, 서울대학교출판문화원, 2020.
