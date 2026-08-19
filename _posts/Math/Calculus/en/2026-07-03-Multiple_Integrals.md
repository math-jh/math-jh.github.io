---
title: "Multiple Integrals"
description: "This post defines multiple integrals of functions of several variables via Riemann sums and covers Fubini's theorem for reducing them to iterated integrals. It also explores change of variables using the Jacobian determinant, with worked examples in double and triple integrals involving polar, cylindrical, and spherical coordinates, Gaussian integrals, and volume computations."
excerpt: "Multiple integrals, Fubini's theorem, change of variables and the Jacobian determinant"

categories: [Math / Calculus]
permalink: /en/math/calculus/multiple_integrals
sidebar: 
    nav: "calculus-en"

date: 2026-07-03
weight: 15
translated_at: 2026-08-19T10:15:05+00:00
translation_source: kimi-cli
last_polished_at: 2026-08-19T10:15:05+00:00
---
We defined multivariable functions and examined their derivatives in [§Functions of Several Variables and Partial Derivatives](/en/math/calculus/partial_derivatives). Now we turn to integration.

## Multiple Integrals

Just as the single-variable definite integral sums function values over an interval, in several variables we sum function values over a region. Let us begin with closed boxes in $\mathbb{R}^n$.

::: Definition 1
For a bounded function $f$ on a closed box $R = [a_1,b_1]\times\cdots\times[a_n,b_n]\subseteq \mathbb{R}^n$, partition $R$ into small boxes (of volume $\Delta V$), choose a sample point $\mathbf{x}^\ast$ in each piece, and form the Riemann sum

$$\sum f(\mathbf{x}^\ast) \Delta V$$

If this converges to a single value as the partition is refined, that value is called the *multiple integral* of $f$ and is written

$$\int_R f \dd{V}$$

When we need to exhibit the variables, we also write

$$\int\cdots\int_R f(x_1,\ldots,x_n) \dd{x_1}\cdots \dd{x_n}$$
:::

Depending on the dimension, this integral computes different quantities. When $n=1$ it is the familiar definite integral, i.e. the area under a curve. When $n=2$ and $f\geq 0$, the quantity computed is the volume of the solid whose base is the region $R$ and whose top is the surface $z=f(x,y)$; the case $n=2$ is specially called the *double integral*. The notation $\dd{V}$ above is meant to evoke $n$-dimensional volume, but since two-dimensional volume, i.e. area, is already familiar, it is customary to write instead

$$\iint_R f \dd{A}$$

when we wish to make the meaning clearer. Each term $f(x_i^\ast, y_j^\ast) \Delta A_{ij}$ of the Riemann sum is the volume of a thin column with base area $\Delta A_{ij}$ and height $f$, and the double integral is the limit obtained by assembling these columns to approximate the solid and then letting the partition become infinitely fine. Raising the dimension by one more to $n=3$ gives the *triple integral*

$$\iiint_E f \dd{V}$$

Continuous functions are multiple-integrable, and the integral over a general region $D$ that is not a box is defined as the integral of the function extended to be $0$ outside $D$ inside a box containing $D$. If the boundary of $D$ consists of smooth surfaces and the function is continuous on them, the integral is well defined, and one can verify that the basic properties of integration hold exactly as in the single-variable case. Rather than enumerate them one by one, we shall only briefly summarize the new points that arise in this article.

## Fubini's Theorem

The definition of a multiple integral is an $n$-dimensional limit, so it is difficult to compute directly. Fortunately it reduces to an *iterated integral*, integrating one variable at a time.

::: Theorem 2 (Fubini)
If $f$ is continuous on the box $R = [a_1,b_1]\times\cdots\times[a_n,b_n]$, then

$$\int_R f \dd{V} = \int_{a_1}^{b_1}\left(\int_{a_2}^{b_2}\cdots\left(\int_{a_n}^{b_n} f(x_1,\ldots,x_n) \dd{x_n}\right)\cdots \dd{x_2}\right)\dd{x_1}$$

and the order of integration may be changed arbitrarily.
:::

A rigorous proof relies essentially on the analytic properties of continuous functions, so we omit it here. In any case, the inner integrals on the right-hand side of the theorem are ordinary definite integrals in which one variable is held constant and we integrate with respect to the other, so a multiple integral becomes a repetition of single-variable integrals solved by the Fundamental Theorem of Calculus and integration techniques from [§The Fundamental Theorem of Calculus](/en/math/calculus/fundamental_theorem_of_calculus). If the integrand separates variables as $f(x_1,\ldots,x_n) = g_1(x_1)\cdots g_n(x_n)$ and the region is a box, we can go one step further: the multiple integral decomposes into the product of $n$ single-variable integrals

$$(\int_{a_1}^{b_1} g_1)\cdots(\int_{a_n}^{b_n} g_n)$$

For a general region the limits of integration may depend on the other variables. Taking $n=2$ as an example, if

$$D = \{(x,y) \mid a\leq x\leq b,\ g_1(x)\leq y\leq g_2(x)\}$$

then

$$\iint_D f \dd{A} = \int_a^b \int_{g_1(x)}^{g_2(x)} f(x,y) \dd{y} \dd{x}$$

and the upper limit of the inner integral becomes a function of the outer variable. Hence, to integrate the same region in the opposite order we must describe the region in terms of $y$ instead. For instance, the triangle with vertices $(0,0), (1,0), (1,1)$ can be written as

$$0 \leq x \leq 1,\quad 0 \leq y \leq x$$

but to switch the order we can write instead

$$0 \leq y \leq 1,\quad y \leq x \leq 1$$

The choice of order does not change the answer, but it is common that the inner integral evaluates to an elementary function in one order and fails to do so in the other.

::: Example 3 (Changing the order of integration)
The double integral

$$\int_0^1 \int_x^1 e^{y^2} \dd{y} \dd{x}$$

cannot be evaluated from the inside because the antiderivative of $e^{y^2}$ is not elementary. However, the region of integration is $\{0 \leq x \leq y \leq 1\}$, so switching the order brings the outer variable to the limits of the region and introduces a new factor $y$:

$$\int_0^1 \int_0^y e^{y^2} \dd{x} \dd{y} = \int_0^1 y e^{y^2} \dd{y} = \frac{1}{2}(e - 1)$$
:::

## Change of Variables

The multivariable analogue of single-variable substitution is change of variables, where the Jacobian determinant takes the place of the length ratio $g'$.

::: Theorem 4 (Change of variables)
If a $C^1$ map $\mathbf{x} = \mathbf{T}(\mathbf{u})$ sends a region $D'\subseteq \mathbb{R}^n$ onto $D$, is one-to-one on the interior of $D'$, and has nonzero Jacobian determinant, then for $f$ continuous on $D$

$$\int_D f(\mathbf{x}) \dd{V} = \int_{D'} f(\mathbf{T}(\mathbf{u})) \lvert \det J_{\mathbf{T}}(\mathbf{u})\rvert \dd{V'}$$

Here $J_{\mathbf{T}}$ is the *Jacobi matrix* formed from the partial derivatives of $\mathbf{T}$

$$J_{\mathbf{T}}=\begin{pmatrix} \partial x_1/\partial u_1 & \cdots & \partial x_1/\partial u_n \\ \vdots & \ddots & \vdots \\ \partial x_n/\partial u_1 & \cdots & \partial x_n/\partial u_n\end{pmatrix}$$
:::

Again, since we have agreed to treat linear algebra as a black box, we defer the proof to analysis. In any case, what matters is the intuition: the Jacobian determinant $\lvert\det J_{\mathbf{T}}\rvert$ is the local scaling factor by which $\mathbf{T}$ expands volume. That is, a small box in $\mathbf{u}$-space is carried by $\mathbf{T}$ to a small parallelepiped in $\mathbf{x}$-space whose volume is the original box's volume multiplied by $\lvert\det J_{\mathbf{T}}\rvert$, so the volume element transforms as $\dd{V} = \lvert\det J_{\mathbf{T}}(\mathbf{u})\rvert \dd{V'}$. In dimension $n=2$ the parallelepiped becomes a parallelogram, and the area formed by the two edges $\mathbf{T}_u \Delta u$ and $\mathbf{T}_v \Delta v$ (where $\mathbf{T}_u, \mathbf{T}_v$ are the partial derivative vectors of $\mathbf{T}$) is exactly $\lvert\det J_{\mathbf{T}}\rvert \Delta u \Delta v$. Substituting this into the Riemann sum and taking the limit yields [Theorem 4](#thm4); the absolute value is needed because volume is always positive.

The most common use of change of variables is to switch coordinate systems, and since we have only introduced determinants of $2\times 2$ and $3\times 3$ matrices, these will be the only examples we treat.

::: Example 5 (Change of variables in double integrals, polar coordinates)
The most common change of variables for double integrals is polar coordinates $x = r\cos\theta$, $y = r\sin\theta$. Then the Jacobian determinant is

$$\det J = \det\begin{pmatrix}\cos\theta & -r\sin\theta \\ \sin\theta & r\cos\theta\end{pmatrix} = r$$

so $\dd{A} = r \dd{r} \dd{\theta}$. This extra factor $r$ often unlocks integrals that were stuck in rectangular coordinates. For example, over the unit disk $D$ the double integral

$$\iint_D e^{-(x^2+y^2)} \dd{A} = \int_0^{2\pi} \int_0^1 e^{-r^2} r \dd{r}\dd{\theta} = \pi(1 - e^{-1})$$

can be completed because the antiderivative of $e^{-r^2} r$ is explicitly $-e^{-r^2}/2$.
:::

Using the example above, we can evaluate the Gaussian integral, which does not succumb to a single variable.

::: Example 6 (Gaussian integral)
Let us find the value of the integral $I = \int_{-\infty}^{\infty} e^{-x^2} \dd{x}$. For $x \geq 1$ we have $e^{-x^2} \leq e^{-x}$ and $\int_1^\infty e^{-x} \dd{x}$ converges, so by [§Improper Integrals, ⁋Proposition 3](/en/math/calculus/improper_integrals#prop3) the integral $\int_0^\infty e^{-x^2} \dd{x}$ converges, and since $e^{-x^2}$ takes the same value at $x$ and $-x$, $\int_{-\infty}^0 e^{-x^2} \dd{x}$ also converges. Hence this improper integral converges. Now on the square $Q_t = [-t,t]\times[-t,t]$ the integrand separates variables, so by [Theorem 2](#thm2)

$$\left(\int_{-t}^{t} e^{-x^2} \dd{x}\right)^2 = \left(\int_{-t}^{t} e^{-x^2} \dd{x}\right)\left(\int_{-t}^{t} e^{-y^2} \dd{y}\right) = \iint_{Q_t} e^{-(x^2+y^2)} \dd{A}$$

Since both improper integrals converge, as $t \rightarrow \infty$ the integral $\int_{-t}^{t} e^{-x^2} \dd{x}$ approaches $I$, and therefore the left-hand side of the above equation goes to $I^2$. On the other hand, over the disk $B_s$ of radius $s$, the calculation of [Example 5](#ex5) repeats verbatim to give

$$\iint_{B_s} e^{-(x^2+y^2)} \dd{A} = \int_0^{2\pi} \int_0^s e^{-r^2} r \dd{r} \dd{\theta} = \pi(1 - e^{-s^2})$$

Now $B_t \subseteq Q_t \subseteq B_{\sqrt{2}t}$ and the integrand is positive, so the integral is monotone in the region, yielding

$$\pi(1 - e^{-t^2}) \leq \left(\int_{-t}^{t} e^{-x^2} \dd{x}\right)^2 \leq \pi(1 - e^{-2t^2})$$

and since both ends approach $\pi$ as $t \rightarrow \infty$, we obtain $I^2 = \pi$, i.e. $I = \sqrt\pi$.
:::

The classical example in two dimensions is just polar coordinates, but in three dimensions there are two substitutions: spherical coordinates and cylindrical coordinates, and computing with them appropriately is helpful for evaluating many integrals.

::: Example 7 (Change of variables in triple integrals, spherical and cylindrical coordinates)
First, *cylindrical coordinates* $(r, \theta, z)$ are obtained by adding the height $z$ to polar coordinates in the plane:

$$x = r\cos\theta,\quad y = r\sin\theta, \quad z = z$$

The Jacobian determinant is

$$\det J = \det\begin{pmatrix}\cos\theta & -r\sin\theta & 0 \\ \sin\theta & r\cos\theta & 0 \\ 0 & 0 & 1\end{pmatrix} = r$$

so $\dd{V} = r \dd{r} \dd{\theta} \dd{z}$.

For *spherical coordinates* $(\rho, \phi, \theta)$, a point is described by its distance $\rho$ from the origin, the angle $\phi$ from the positive $z$-axis, and the azimuthal angle $\theta$:

$$x = \rho\sin\phi\cos\theta, \quad y = \rho\sin\phi\sin\theta, \quad z = \rho\cos\phi$$

Computing its Jacobian determinant gives

$$\det J = \det\begin{pmatrix} \sin\phi\cos\theta & \rho\cos\phi\cos\theta & -\rho\sin\phi\sin\theta \\ \sin\phi\sin\theta & \rho\cos\phi\sin\theta & \rho\sin\phi\cos\theta \\ \cos\phi & -\rho\sin\phi & 0 \end{pmatrix} = \rho^2\sin\phi$$

so $\dd{V} = \rho^2\sin\phi \dd{\rho} \dd{\phi} \dd{\theta}$. For example, the volume of a ball of radius $R$ can be derived in spherical coordinates because the three variables separate:

$$\iiint_{B_R} \dd{V} = \left(\int_0^{2\pi} \dd{\theta}\right)\left(\int_0^\pi \sin\phi \dd{\phi}\right)\left(\int_0^R \rho^2 \dd{\rho}\right) = 2\pi\cdot 2\cdot \frac{R^3}{3} = \frac{4\pi R^3}{3}$$
:::

---

**References**

**[Ste]** J. Stewart, *Calculus*, 8th ed., Cengage Learning, 2016.  
**[Kim]** 김홍종, *미적분학 1·2*, 제3개정판, 서울대학교출판문화원, 2020.
