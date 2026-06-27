---
title: "Integration"
description: "Indefinite integrals (antiderivatives) are defined as the inverse of differentiation, and definite integrals are introduced as the limit of Riemann sums over partitions. The text covers the fact that any two antiderivatives differ only by a constant, the linearity and basic formulas of indefinite integrals, the integrability of continuous functions, the linearity, additivity, and monotonicity of integrals, the mean value theorem for integrals, and the interpretation of the definite integral as signed area."
excerpt: "Antiderivatives, indefinite integrals, Riemann sums, definite integrals, and the mean value theorem"

categories: [Math / Calculus]
permalink: /en/math/calculus/integration
sidebar: 
    nav: "calculus-en"

date: 2026-06-26
weight: 10
translated_at: 2026-06-27T10:30:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-27T10:30:02+00:00
---
We have so far defined the limit of a function and then defined the derivative as the limit of the average rate of change. In this post, we present the inverse operation of that process—the integral—and examine several of its properties.

## Antiderivatives

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> For a function $$f$$ defined on an interval $$I$$, a differentiable function $$F$$ satisfying $$F'(x) = f(x)$$ at every point of $$I$$ is called an *antiderivative* of $$f$$.

</div>

For example, $$F(x) = x^2$$ is an antiderivative of $$f(x) = 2x$$. However, $$x^2 + 1$$ and $$x^2 - 5$$ also have derivative $$2x$$, so they are antiderivatives as well. That is, adding a constant to one antiderivative still yields an antiderivative. Geometrically, the entire family of curves obtained by shifting the same shape vertically all share the same derivative (the same slope distribution). Thus an antiderivative is not unique, but any two can differ only by a constant term.

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> If $$F$$ is an antiderivative of $$f$$ on an interval $$I$$, then every antiderivative of $$f$$ has the form $$F(x) + C$$ for some constant $$C$$.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

If $$G$$ is also an antiderivative of $$f$$, then $$(G - F)' = f - f = 0$$. By [§Mean Value Theorem, ⁋Corollary 5](/en/math/calculus/mean_value_theorem#cor5), a function whose derivative is identically zero on an interval is constant; hence there is a constant $$C$$ with $$G - F = C$$, i.e. $$G = F + C$$.

</details>

In view of this proposition, we collect all antiderivatives of $$f$$ into a single expression and write

$$\int f(x)dx = F(x) + C,$$

which we call the *indefinite integral* of $$f$$. Here $$C$$ is the *constant of integration*, $$f$$ is the *integrand*, and the symbol $$dx$$ indicates the variable of integration. Thanks to the fact guaranteed by [Proposition 2](#prop2)—that antiderivatives differ only by a constant—the single constant $$C$$ suffices to represent all of them at once.

The assumption we are implicitly making, namely that the interval is connected, is not essential in all respects, but the above proposition holds only when the interval is connected. If the domain is broken into separate pieces, a different constant may be chosen on each piece. For instance, $$1/x$$ is defined separately on $$x > 0$$ and $$x < 0$$; adding different constants to $$F(x) = \ln\lvert x\rvert$$ on the two pieces still yields antiderivatives of $$1/x$$, so the literal statement "differ only by a constant" does not apply over the whole domain.

Under the assumption that the interval is connected, the constant of integration $$C$$ is determined exactly once an *initial condition* is given. This is the basic method of solving differential equations by indefinite integration. For example, if $$F'(x) = 3x^2 + 1$$ and $$F(1) = 5$$, then from the indefinite integral $$F(x) = x^3 + x + C$$ we substitute the initial condition to obtain $$1 + 1 + C = 5$$, so $$C = 3$$ and $$F(x) = x^3 + x + 3$$ is uniquely determined.

## Properties and Examples of Indefinite Integrals

Meanwhile, in [§Differentiation Rules](/en/math/calculus/differentiation_rules) we examined the derivatives of various functions, and because indefinite integration is the reverse of differentiation, we can derive integration formulas from them. Before doing so, let us establish the linearity of the indefinite integral.

<div class="proposition" markdown="1">

<ins id="prop3">**Proposition 3 (Linearity of the Indefinite Integral)**</ins> If $$f$$ and $$g$$ have antiderivatives and $$a, b$$ are constants, then

$$\int \bigl(a f(x) + b g(x)\bigr)dx = a\int f(x)dx + b\int g(x)dx.$$

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

Let $$F$$ and $$G$$ be antiderivatives of $$f$$ and $$g$$, respectively. Then by [§Derivatives, ⁋Proposition 4](/en/math/calculus/derivatives#prop4),

$$(aF + bG)' = aF' + bG' = af + bg,$$

so $$aF + bG$$ is an antiderivative of $$af + bg$$.

</details>

Now, reversing the derivative formulas from [§Differentiation Rules](/en/math/calculus/differentiation_rules), we obtain the following basic formulas. That is, differentiating the right-hand side of each formula yields the integrand.

$$\int x^rdx = \frac{x^{r+1}}{r+1} + C\ (r \neq -1), \qquad \int \frac{1}{x}dx = \ln\lvert x\rvert + C,$$

$$\int e^xdx = e^x + C, \qquad \int \cos xdx = \sin x + C, \qquad \int \sin xdx = -\cos x + C,\qquad \int \sec^2 xdx = \tan x + C,$$

$$\int \frac{dx}{1 + x^2} = \arctan x + C, \qquad \int \frac{dx}{\sqrt{1 - x^2}} = \arcsin x + C.$$

Combining linearity with these formulas allows us to integrate arbitrary sums of basic functions term by term. When the integrand is not in standard form, we first reshape it using other tools—for example, using the trigonometric identity

$$\tan^2 x = \sec^2 x - 1$$

or splitting the fraction $$(x^2+1)/x$$ into $$x + 1/x$$ so that each term matches the formulas above.

In particular, the two especially useful techniques of substitution and integration by parts are, respectively, the reversals of [§Differentiation Rules, ⁋Theorem 4](/en/math/calculus/differentiation_rules#thm4) and [§Differentiation Rules, ⁋Proposition 3](/en/math/calculus/differentiation_rules#prop3).

<div class="proposition" markdown="1">

<ins id="thm4">**Theorem 4 (Integration by Substitution)**</ins> If $$g$$ is differentiable and $$f$$ is continuous, then

$$\int f(g(x)) g'(x) dx = \int f(u) du \quad (u = g(x)).$$

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

Let $$F$$ be an antiderivative of $$f$$. Then by [§Differentiation Rules, ⁋Theorem 4](/en/math/calculus/differentiation_rules#thm4),

$$\frac{d}{dx}F(g(x)) = F'(g(x))g'(x) = f(g(x))g'(x),$$

so $$F(g(x))$$ is an antiderivative of the left-hand integrand. Therefore $$\int f(g(x))g'(x)dx = F(g(x)) + C = F(u) + C = \int f(u)du$$.

</details>

In practice, one sets $$u = g(x)$$ and $$du = g'(x) dx$$, rewrites the expression entirely in terms of $$u$$, integrates, and then substitutes back. For example, with $$u = \cos x$$ we get $$\int \tan x dx = -\int du/u = -\ln\lvert\cos x\rvert + C$$, and by the same method $$\int x/(x^2+1) dx = \ln(x^2+1)/2 + C$$.

<div class="proposition" markdown="1">

<ins id="thm5">**Theorem 5 (Integration by Parts)**</ins> If $$u, v$$ are differentiable and their derivatives are continuous, then

$$\int u v' dx = uv - \int u' v dx.$$

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

By [§Differentiation Rules, ⁋Proposition 3](/en/math/calculus/differentiation_rules#prop3), $$(uv)' = u'v + uv'$$, so $$uv' = (uv)' - u'v$$. Integrating both sides, we obtain the claim from $$\int (uv)' dx = uv$$.

</details>

The key is to choose $$u$$ as the factor that simplifies upon differentiation and $$v'$$ as the factor that can be integrated. For example, $$\int x e^x dx$$ with $$u = x$$ gives $$xe^x - e^x + C$$; for functions like logarithms or inverse trigonometric functions whose derivatives are actually simpler, we place them in the $$u$$ slot with $$v' = 1$$ (so $$\int \ln x dx = x\ln x - x + C$$). Sometimes integration by parts does not simplify the integrand but returns it to itself; in that case we treat the original integral as an unknown and solve algebraically.

<div class="example" markdown="1">

<ins id="ex6">**Example 6**</ins> For $$I = \int e^x\cos x dx$$, integrating by parts twice brings us back to the original integral. With $$u = e^x$$ and $$v' = \cos x$$,

$$I = e^x\sin x - \int e^x\sin x dx = e^x\sin x - \Bigl(-e^x\cos x + \int e^x\cos x dx\Bigr) = e^x(\sin x + \cos x) - I$$

so $$2I = e^x(\sin x + \cos x)$$, hence

$$I = \frac{e^x(\sin x + \cos x)}{2} + C.$$

</div>

Rational functions whose denominator factors can be decomposed into partial fractions, and then each piece integrates to a logarithm or an arctangent. For instance,

$$\frac{1}{x^2-1} = \frac{1}{2}\left(\frac{1}{x-1} - \frac{1}{x+1}\right)$$

gives

$$\int \frac{dx}{x^2 - 1} = \frac{1}{2}\ln\left\lvert\frac{x-1}{x+1}\right\rvert + C,$$

and when the denominator contains an irreducible quadratic, completing the square lets us use an arctangent:

$$\int \frac{dx}{x^2 + 2x + 5} = \frac{1}{2}\arctan\frac{x+1}{2} + C.$$

For radicals such as $$\sqrt{a^2 - x^2}$$ or $$\sqrt{a^2 + x^2}$$, a trigonometric substitution eliminates the radical. For example, in $$\int \sqrt{1 - x^2} dx$$ with $$x = \sin\theta$$,

$$\int \cos^2\theta d\theta = \frac{1}{2}(\arcsin x + x\sqrt{1-x^2}) + C.$$

Powers of trigonometric functions themselves are handled by reducing the degree via identities or by substitution. Odd powers are integrated by peeling off one factor and substituting:

$$\int \sin^3 x dx = -\cos x + \frac{1}{3}\cos^3 x + C,$$

while even powers are reduced using double-angle formulas:

$$\int \sin^2 x dx = \frac{x}{2} - \frac{\sin 2x}{4} + C.$$

Repeated integration by parts yields recurrence relations that lower the degree step by step, allowing systematic treatment of integrals involving mixed powers.

<div class="example" markdown="1">

<ins id="ex7">**Example 7 (Recurrence Relation)**</ins> For $$I_n = \int x^n e^x dx$$, integrating by parts with $$u = x^n$$ and $$v' = e^x$$ gives

$$I_n = x^n e^x - n I_{n-1}.$$

Starting from $$I_0 = e^x$$, we obtain successively

$$I_1 = (x-1)e^x, \quad I_2 = (x^2 - 2x + 2)e^x,$$

lowering the degree at each step. In the same way one obtains the recurrence

$$\int \sin^n x dx = -\frac{1}{n} \sin^{n-1}x\cos x + \frac{n-1}{n}\int \sin^{n-2}x dx.$$

</div>

Even with these techniques, some integrals cannot be expressed in terms of elementary functions; examples include $$\int e^{-x^2} dx$$ and $$\int (\sin x)/x dx$$. Such functions are nevertheless well defined as definite integrals, and they themselves define new functions, as we shall see from the Fundamental Theorem of Calculus.

## Partitions and Riemann Sums

The integral described above was defined as the inverse operation of differentiation, but historically integration arose from a different problem: finding the total accumulated quantity. For example, measuring the area under a curve $$y = f(x)$$ above an interval $$[a,b]$$. The idea of the following definition is to approximate this area by thin rectangles and then make the subdivision infinitely fine.

<div class="definition" markdown="1">

<ins id="def8">**Definition 8**</ins> A *partition* of the closed interval $$[a, b]$$ is a finite set of points $$a = x_0 < x_1 < \cdots < x_n = b$$. The length of each subinterval $$[x_{i-1}, x_i]$$ is denoted $$\Delta x_i = x_i - x_{i-1}$$, and the length of the longest subinterval is called the *mesh* of the partition, $$\lVert P\rVert = \max_i \Delta x_i$$. Choosing a sample point $$c_i \in [x_{i-1}, x_i]$$ in each subinterval, we call

$$S(P, f) = \sum_{i=1}^{n} f(c_i)\Delta x_i$$

the *Riemann sum* of the function $$f$$.

</div>

![Riemann sum](/assets/images/Math/Calculus/Integration-1.svg){:style="width:24.05em" class="invert" .align-center}

A Riemann sum approximates the area under the curve by rectangles of width $$\Delta x_i$$ and height $$f(c_i)$$. Taking the sample points $$c_i$$ to be the left endpoint, right endpoint, or points giving the minimum or maximum of the function on each subinterval yields the left and right Riemann sums, or the lower and upper sums, respectively. Intuitively, we expect that as the partition is made arbitrarily fine, this approximation converges to a single value independent of the choice of sample points.

<div class="definition" markdown="1">

<ins id="def9">**Definition 9**</ins> If there exists a real number $$S$$ such that for every $$\varepsilon > 0$$ there is a $$\delta > 0$$ with $$\lvert S(P, f) - S\rvert < \varepsilon$$ for every partition and every choice of sample points satisfying $$\lVert P\rVert < \delta$$, then $$f$$ is said to be *integrable* on $$[a,b]$$, and $$S$$ is called the *definite integral*, written

$$\int_a^b f(x)dx = S.$$

The numbers $$a$$ and $$b$$ are called the lower and upper limits of integration, respectively.

</div>

We can apply this definition directly to compute definite integrals. Dividing $$[0,1]$$ into $$n$$ equal parts and choosing the right endpoints $$c_i = i/n$$, the Riemann sum for

$$\int_0^1 xdx$$

is

$$\sum_{i=1}^n \frac{i}{n}\cdot\frac1n = \frac{1}{n^2}\cdot\frac{n(n+1)}{2} = \frac{n+1}{2n} \to \frac12,$$

and similarly

$$\int_0^1 x^2dx = \lim_{n\to\infty}\sum_{i=1}^n \frac{i^2}{n^3} = \lim_{n\to\infty}\frac{n(n+1)(2n+1)}{6n^3} = \frac13.$$

In particular, the first result can also be checked immediately from the area formula for a triangle.

<div class="proposition" markdown="1">

<ins id="thm10">**Theorem 10**</ins> Every function continuous on $$[a, b]$$ is integrable.

</div>

The proof of this theorem is beyond our present scope, so we must accept it and move on.

## Properties of the Definite Integral

Since a Riemann sum is defined as a sum and a limit, the definite integral inherits the following properties.

<div class="proposition" markdown="1">

<ins id="prop11">**Proposition 11**</ins> If $$f, g$$ are integrable on $$[a,b]$$, then the following hold.

1. For constants $$\alpha, \beta$$, $$\int_a^b (\alpha f(x) + \beta g(x))dx = \alpha\int_a^b f(x)dx + \beta\int_a^b g(x)dx$$.
2. For $$a < c < b$$, $$\int_a^b f(x)dx = \int_a^c f(x)dx + \int_c^b f(x)dx$$.
3. If $$f(x) \leq g(x)$$ for all $$x$$, then $$\int_a^b f(x)dx \leq \int_a^b g(x)dx$$.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

All three properties hold at the level of Riemann sums and are preserved in the limit. Linearity follows from $$S(P, \alpha f + \beta g) = \alpha S(P, f) + \beta S(P, g)$$, and monotonicity follows from $$f(c_i) \leq g(c_i)$$ implying $$S(P, f) \leq S(P, g)$$. The additivity over intervals is obtained by considering only partitions that include $$c$$ as a subdivision point, so the Riemann sum splits into the sums over the two subintervals.

</details>

By convention we set $$\int_a^a f(x)dx = 0$$ and $$\int_b^a f(x)dx = -\int_a^b f(x)dx$$; then additivity holds regardless of the order of $$a, b, c$$. From monotonicity two useful estimates follow. First, if $$m \leq f \leq M$$, then

$$m(b-a) \leq \int_a^b f(x)dx \leq M(b-a).$$

Second, applying this to $$-\lvert f\rvert \leq f \leq \lvert f\rvert$$ yields the integral version of the triangle inequality:

$$\left\lvert \int_a^b f(x)dx\right\rvert  \leq \int_a^b \lvert f(x)\rvert dx.$$

Applying the first inequality to continuous functions, one can show that the integral value is exactly attained by the function value at some point.

<div class="proposition" markdown="1">

<ins id="prop12">**Proposition 12 (Mean Value Theorem for Integrals)**</ins> If $$f$$ is continuous on $$[a,b]$$, then there exists $$c \in [a,b]$$ such that

$$\int_a^b f(x)dx = f(c)(b-a).$$

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

By [§Continuous Functions, ⁋Theorem 4](/en/math/calculus/continuity#thm4), $$f$$ attains a minimum $$m$$ and a maximum $$M$$ on $$[a,b]$$. From the calculation above, the average value

$$\frac{1}{b-a}\int_a^b f(x)dx$$

lies in $$[m, M]$$; hence by [§Continuous Functions, ⁋Theorem 5](/en/math/calculus/continuity#thm5) there exists $$c$$ with $$f(c) = \frac{1}{b-a}\int_a^b f(x)dx$$.

</details>

Here

$$\frac{1}{b-a}\int_a^b f(x)dx$$

is called the *average value* of $$f$$ on $$[a,b]$$, and [Proposition 12](#prop12) states that a continuous function actually attains its average value at least at one point.

## Area and Applications

The definite integral is most intuitively understood as <em>signed</em> area. For example, on an interval where $$f < 0$$, each term $$f(c_i)\Delta x_i$$ of the Riemann sum is negative, so $$\int_a^b f(x)dx$$ attaches a minus sign to the region enclosed by the $$x$$-axis and the graph of $$f$$. This viewpoint becomes especially clear when the function changes sign over the interval of integration, and it is here that the integral version of the triangle inequality appears as a strict inequality, distinguishing the case where a single integral cancels positive and negative areas to give $$0$$ from the case where the actual area requires absolute values.

<div class="example" markdown="1">

<ins id="ex13">**Example 13**</ins> The reason $$\int_{-1}^{1} xdx = 0$$ is that the negative area on $$[-1,0]$$ and the positive area on $$[0,1]$$ exactly cancel. Each piece is a right triangle with base and height $$1$$, so its area is $$\frac{1}{2}$$; splitting the integral using the second part of [Proposition 11](#prop11),

$$\int_{-1}^{1} xdx = \int_{-1}^{0} xdx + \int_{0}^{1} xdx = -\frac{1}{2} + \frac{1}{2} = 0.$$

If one wants the *actual* area enclosed by the curve and the $$x$$-axis, one must integrate the absolute value $$\lvert x\rvert$$, obtaining

$$\int_{-1}^{1} \lvert x\rvert dx = \int_{-1}^{0} (-x)dx + \int_{0}^{1} xdx = \frac{1}{2} + \frac{1}{2} = 1.$$

This is a concrete instance where the integral triangle inequality $$\bigl\lvert\int f\bigr\rvert \leq \int \lvert f\rvert$$ holds as a strict inequality $$0 < 1$$, and each piece is immediately verified by the triangle area formula. This calculation also agrees with the earlier computation of the triangle area via Riemann sums.

</div>

Because the mean value theorem converts an integral into a function value at a single point, it is frequently used in dealing with inequalities or in inferring average behavior. The same theorem holds for weighted integrals, provided the weight has a fixed sign.

<div class="proposition" markdown="1">

<ins id="prop14">**Proposition 14 (Weighted Mean Value Theorem)**</ins> If $$f$$ is continuous on $$[a,b]$$ and $$\mu$$ is integrable on $$[a,b]$$ with $$\mu \geq 0$$, then there exists $$c \in [a,b]$$ such that

$$\int_a^b f(x)\mu(x)dx = f(c)\int_a^b \mu(x)dx.$$

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

By [§Continuous Functions, ⁋Theorem 4](/en/math/calculus/continuity#thm4), $$f$$ attains a minimum $$m$$ and a maximum $$M$$. Since $$\mu \geq 0$$, we have $$m\mu(x) \leq f(x)\mu(x) \leq M\mu(x)$$; integrating and using monotonicity and linearity gives

$$m\int_a^b \mu(x)dx \leq \int_a^b f(x)\mu(x) dx\leq M\int_a^b \mu(x) dx.$$

If $$\int_a^b \mu(x)dx = 0$$, then the middle integral is also $$0$$ and the equality holds for any $$c$$. If $$\int_a^b \mu(x)dx > 0$$, dividing the above inequality by that value yields

$$\frac{\int_a^b f(x)\mu(x) dx}{\int_a^b \mu(x)dx} \in [m, M],$$

and by [§Continuous Functions, ⁋Theorem 5](/en/math/calculus/continuity#thm5) there exists $$c$$ attaining this value. Multiplying back by $$\int_a^b \mu(x)dx$$ completes the proof.

</details>

If we set $$\mu \equiv 1$$, the weighted mean value theorem reduces to [Proposition 12](#prop12); thus [Proposition 14](#prop14) is a generalization of the mean value theorem, which may be thought of as adding a kind of density.
