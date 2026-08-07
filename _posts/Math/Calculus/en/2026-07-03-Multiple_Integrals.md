---
title: "Multiple Integrals"
description: "This post defines multiple integrals of multivariable functions via Riemann sums and covers Fubini's theorem for reducing them to iterated integrals. It also explores change of variables using the Jacobian, coordinate systems such as polar, cylindrical, and spherical, and applications including Gaussian integrals and volume calculations through double and triple integrals."
excerpt: "Multiple integrals, Fubini's theorem, change of variables, and the Jacobian"

categories: [Math / Calculus]
permalink: /en/math/calculus/multiple_integrals
sidebar: 
    nav: "calculus-en"

date: 2026-07-03
weight: 15
translated_at: 2026-07-05T20:00:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-07-05T20:00:02+00:00
---
We defined multivariable functions and examined their derivatives in [§Multivariable Functions and Partial Derivatives](/en/math/calculus/partial_derivatives). Now it is time to look at integration.

## Multiple Integrals

Just as a single-variable definite integral sums function values over an interval, in several variables we sum function values over a region. Let us start with a closed box in $\mathbb{R}^n$.

::: Definition 1
For a bounded function $f$ on a closed box $R = [a_1,b_1]\times\cdots\times[a_n,b_n]\subseteq \mathbb{R}^n$, partition $R$ into small boxes (of volume $\Delta V$), choose a sample point $\mathbf{x}^\ast$ in each piece, and form the Riemann sum

$$\sum f(\mathbf{x}^\ast) \Delta V$$

If this converges to a single value as the partition is refined, that value is called the *multiple integral* of $f$ and is written

$$\int_R f \dd{V}$$

When it is necessary to exhibit the variables, we also write

$$\int\cdots\int_R f(x_1,\ldots,x_n) \dd{x_1}\cdots \dd{x_n}$$
:::

Depending on the dimension, this integral computes different quantities. For $n=1$ it is the familiar definite integral, namely the area under a curve. For $n=2$ and $f\geq 0$, the quantity computed is the volume of the solid whose base is the region $R$ and whose top is the surface $z=f(x,y)$; this case is specially called the *double integral*. The $\dd{V}$ above is notation with $n$-dimensional volume in mind, but since two-dimensional volume, i.e. area, is already familiar, it is customary to write

$$\iint_R f \dd{A}$$

for this case. Looking at this, the meaning of the integral becomes clearer: each term $f(x_i^\ast, y_j^\ast) \Delta A_{ij}$ of the Riemann sum is the volume of a thin column with base area $\Delta A_{ij}$ and height $f$, and the double integral is the limit obtained by assembling these columns to approximate the solid and then letting the partition become infinitely fine. Raising the dimension by one to $n=3$ gives the *triple integral*

$$\iiint_E f \dd{V}$$

Continuous functions are multiple-integrable, and the integral over a general region $D$ is defined as the integral of the function extended to be zero outside $D$ inside a box containing $D$. If the boundary of $D$ consists of smooth surfaces and the function is continuous on them, the integral is well defined, and one can verify that the basic properties of integrals hold exactly as in the single-variable case. In this post, rather than enumerating them one by one, we briefly summarize only those that are newly appearing.

## Fubini's Theorem

The definition of a multiple integral is an $n$-dimensional limit, so it is difficult to compute directly. Fortunately it reduces to an *iterated integral*, integrating one variable at a time.

::: Theorem 2 (Fubini)
If $f$ is continuous on the box $R = [a_1,b_1]\times\cdots\times[a_n,b_n]$, then

$$\int_R f \dd{V} = \int_{a_1}^{b_1}\left(\int_{a_2}^{b_2}\cdots\left(\int_{a_n}^{b_n} f(x_1,\ldots,x_n) \dd{x_n}\right)\cdots \dd{x_2}\right)\dd{x_1}$$

and the order of integration may be changed arbitrarily.
:::

A rigorous proof essentially relies on the analytical fact that $f$ is uniformly continuous on the compact box $R$, so we omit it in this post. In any case, the inner integrals on the right-hand side of the theorem are ordinary definite integrals in which one variable is held constant and another is integrated, so a multiple integral becomes a repetition of single-variable integrals solved by [§The Fundamental Theorem of Calculus](/en/math/calculus/fundamental_theorem_of_calculus) and integration techniques. If the integrand separates variables as $f(x_1,\ldots,x_n) = g_1(x_1)\cdots g_n(x_n)$ and the region is a box, one step further: the multiple integral decomposes into the product of $n$ single-variable integrals

$$(\int_{a_1}^{b_1} g_1)\cdots(\int_{a_n}^{b_n} g_n)$$

For general regions the limits of integration may depend on other variables. Taking $n=2$ as an example, if

$$D = \{(x,y) \mid a\leq x\leq b,\ g_1(x)\leq y\leq g_2(x)\}$$

then

$$\iint_D f \dd{A} = \int_a^b \int_{g_1(x)}^{g_2(x)} f(x,y) \dd{y} \dd{x}$$

and the upper and lower limits of the inner integral become functions of the outer variable. Therefore, to integrate the same region in the opposite order one must describe the region with $y$ as the independent variable. For instance, the triangle with vertices $(0,0), (1,0), (1,1)$ can be written as

$$0 \leq x \leq 1,\quad 0 \leq y \leq x$$

but to switch the order one can also write

$$0 \leq y \leq 1,\quad y \leq x \leq 1$$

The choice of order does not change the answer, but it is common that the inner integral is elementary in one order and not in the other.

::: Example 3 (Changing the order of integration)
The double integral

$$\int_0^1 \int_x^1 e^{y^2} \dd{y} \dd{x}$$

cannot be solved from the inside because the antiderivative of $e^{y^2}$ is not elementary. However, the region of integration is $\{0 \leq x \leq y \leq 1\}$, so changing the order brings the outer variable into the limits and creates a new factor $y$:

$$\int_0^1 \int_0^y e^{y^2} \dd{x} \dd{y} = \int_0^1 y e^{y^2} \dd{y} = \frac{1}{2}(e - 1)$$
:::

## Change of Variables

What corresponds to substitution in a single variable is change of variables in several variables, and the Jacobian determinant takes the place of the length ratio $g'$.

::: Theorem 4 (Change of Variables)
If a one-to-one $C^1$ map $\mathbf{x} = \mathbf{T}(\mathbf{u})$ sends a region $D'\subseteq \mathbb{R}^n$ onto $D$ and the Jacobian determinant is nonzero on $D'$, then

$$\int_D f(\mathbf{x}) \dd{V} = \int_{D'} f(\mathbf{T}(\mathbf{u})) \lvert \det J_{\mathbf{T}}(\mathbf{u})\rvert \dd{V'}$$

Here $J_{\mathbf{T}}$ is the *Jacobi matrix* collecting the partial derivatives of $\mathbf{T}$

$$J_{\mathbf{T}}=\begin{pmatrix} \partial x_1/\partial u_1 & \cdots & \partial x_1/\partial u_n \\ \vdots & \ddots & \vdots \\ \partial x_n/\partial u_1 & \cdots & \partial x_n/\partial u_n\end{pmatrix}$$
:::
Again, since we have agreed to treat linear algebra as a black box, we defer the proof to analysis. In any case, what matters is the intuition: the Jacobian determinant $\lvert\det J_{\mathbf{T}}\rvert$ is the local scaling factor by which $\mathbf{T}$ expands volume. That is, a small box in $\mathbf{u}$-space is carried by $\mathbf{T}$ to a small parallelepiped in $\mathbf{x}$-space whose volume is the original box's volume multiplied by $\lvert\det J_{\mathbf{T}}\rvert$, so the volume element transforms as $\dd{V} = \lvert\det J_{\mathbf{T}}(\mathbf{u})\rvert \dd{V}'$. For $n=2$ the parallelepiped becomes a parallelogram, and the area formed by the two edge vectors $\mathbf{T}_u \Delta u$ and $\mathbf{T}_v \Delta v$ (where $\mathbf{T}_u, \mathbf{T}_v$ are the partial derivative vectors of $\mathbf{T}$) is exactly $\lvert\det J_{\mathbf{T}}\rvert \Delta u \Delta v$. Substituting this expression into the Riemann sum and taking the limit yields [Theorem 4](#thm4), and the absolute value is present because volume is always positive.

The most common use of change of variables is to switch coordinate systems, and since we have introduced only $2\times 2$ and $3\times 3$ determinants, these are the only ones that appear in our examples.

::: Example 5 (Change of variables for double integrals — polar coordinates)
The most common change of variables for double integrals is polar coordinates $x = r\cos\theta$, $y = r\sin\theta$. Then the Jacobian determinant is

$$\det J = \det\begin{pmatrix}\cos\theta & -r\sin\theta \\ \sin\theta & r\cos\theta\end{pmatrix} = r$$

so $\dd{A} = r \dd{r} \dd{\theta}$. This extra factor $r$ often unlocks integrals that were stuck in rectangular coordinates. For example, the double integral over the unit disk $D$

$$\iint_D e^{-(x^2+y^2)} \dd{A} = \int_0^{2\pi} \int_0^1 e^{-r^2} r \dd{r}\dd{\theta} = \pi(1 - e^{-1})$$

because the antiderivative of $e^{-r^2} r$ is explicitly given by $-e^{-r^2}/2$, so the computation can be completed.
:::

Using the example above, we can evaluate the Gaussian integral, which could not be solved by a single variable alone.

::: Example 6 (Gaussian integral)
Let us find the value of the integral $I = \int_{-\infty}^{\infty} e^{-x^2} \dd{x}$. Regarding its square $I^2$ as an integral in two independent variables,

$$\begin{aligned}
I^2 &= \left(\int_{-\infty}^\infty e^{-x^2} \dd{x}\right) \left(\int_{-\infty}^\infty e^{-y^2} \dd{y}\right) \\
&= \iint_{\mathbb{R}^2} e^{-x^2}e^{-y^2} \dd{A} = \iint_{\mathbb{R}^2} e^{-(x^2+y^2)} \dd{A}
\end{aligned}$$

and changing to polar coordinates gives $x^2 + y^2 = r^2$, so

$$\begin{aligned}
I^2 &= \int_0^{2\pi} \int_0^\infty e^{-r^2} r \dd{r} \dd{\theta} \\
&= \int_0^{2\pi} \Bigl[-\frac{1}{2} e^{-r^2}\Bigr]_{r=0}^{r=\infty} \dd{\theta} = \int_0^{2\pi}\frac{1}{2} \dd{\theta} = \pi
\end{aligned}$$

and therefore $I = \sqrt\pi$.
:::

The classical example in two dimensions is only the polar coordinate system, but in three dimensions there are two substitutions: spherical and cylindrical coordinates, and computing with them in the appropriate way is helpful in evaluating many integrals.

::: Example 7 (Change of variables for triple integrals — spherical and cylindrical coordinates)
First, *cylindrical coordinates* $(r, \theta, z)$ are obtained by adding the height $z$ to the polar coordinates in the plane,

$$x = r\cos\theta,\quad y = r\sin\theta, \quad z = z$$

and the Jacobian determinant is

$$\det J = \det\begin{pmatrix}\cos\theta & -r\sin\theta & 0 \\ \sin\theta & r\cos\theta & 0 \\ 0 & 0 & 1\end{pmatrix} = r$$

so $\dd{V} = r \dd{r} \dd{\theta} \dd{z}$.

For *spherical coordinates* $(\rho, \phi, \theta)$, a point is described by the distance $\rho$ from the origin, the angle $\phi$ from the positive $z$-axis, and the azimuthal angle $\theta$:

$$x = \rho\sin\phi\cos\theta, \quad y = \rho\sin\phi\sin\theta, \quad z = \rho\cos\phi$$

Computing its Jacobian determinant gives

$$\det J = \det\begin{pmatrix} \sin\phi\cos\theta & \rho\cos\phi\cos\theta & -\rho\sin\phi\sin\theta \\ \sin\phi\sin\theta & \rho\cos\phi\sin\theta & \rho\sin\phi\cos\theta \\ \cos\phi & -\rho\sin\phi & 0 \end{pmatrix} = \rho^2\sin\phi$$

so $\dd{V} = \rho^2\sin\phi \dd{\rho} \dd{\phi} \dd{\theta}$. For example, the volume of a ball of radius $R$ separates in spherical coordinates into

$$\iiint_{B_R} \dd{V} = \left(\int_0^{2\pi} \dd{\theta}\right)\left(\int_0^\pi \sin\phi \dd{\phi}\right)\left(\int_0^R \rho^2 \dd{\rho}\right) = 2\pi\cdot 2\cdot \frac{R^3}{3} = \frac{4\pi R^3}{3}$$

which can be derived in this way.
:::

---

**References**

**[Ste]** J. Stewart, *Calculus*, 8th ed., Cengage Learning, 2016.  
**[Kim]** 김홍종, *미적분학 1·2*, 제3개정판, 서울대학교출판문화원, 2020.
