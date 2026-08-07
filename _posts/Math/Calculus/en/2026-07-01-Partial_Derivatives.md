---
title: "Multivariable Functions and Partial Derivatives"
description: "This post defines partial derivatives, gradients, and directional derivatives for functions of several variables, and formalizes differentiability through first-order approximation. It covers the multivariable chain rule, Clairaut's theorem on mixed partials, and worked examples of tangent planes and extrema."
excerpt: "Partial derivatives, gradients, differentiability, multivariable chain rule, and extrema"

categories: [Math / Calculus]
permalink: /en/math/calculus/partial_derivatives
sidebar: 
    nav: "calculus-en"

date: 2026-07-01
weight: 14
translated_at: 2026-07-13T22:00:03+00:00
translation_source: kimi-cli
last_polished_at: 2026-07-13T22:00:03+00:00
---
In the previous post, we dealt with functions that raise the dimension of the codomain, sending one real number to several real numbers—that is, parameterized curves $\mathbf{r}:\mathbb{R}\rightarrow\mathbb{R}^n$. Now we go the other way, raising the dimension of the domain, and deal with multivariable functions $f:\mathbb{R}^m\rightarrow\mathbb{R}$ that send several real numbers to one real number. Differentiation still retains its essence as a linear approximation near a point, but because the domain becomes a vector space, there are infinitely many directions from which one can approach, so direction becomes important, and the linear approximation is given not by a single number but by a linear map. Since vector spaces, inner products, and norms were covered in [§Curves and Vector-Valued Functions](/en/math/calculus/vector_functions), in this post we briefly review linear maps, matrices, and determinants—the core tools of multivariable differentiation—and then treat partial derivatives and the gradient, differentiability, the multivariable chain rule, and extrema.

## Linear Maps and Matrices

The essence of differentiation is a linear approximation near a point. When the domain is the vector space $\mathbb{R}^m$, the linear approximation at a point is given not by a single number but by a linear map from $\mathbb{R}^m$ to $\mathbb{R}$, and this is what makes multivariable differentiation fundamentally different from single-variable differentiation. Therefore, before formally defining the derivative, we briefly review linear maps, their matrix representations, and determinants.

A function $T:\mathbb{R}^m\rightarrow\mathbb{R}^n$ between vector spaces is called a *linear map* if for any vectors $\mathbf{v},\mathbf{w}\in\mathbb{R}^m$ and any real number $c\in\mathbb{R}$,

$$T(\mathbf{v}+\mathbf{w})=T(\mathbf{v})+T(\mathbf{w}),\qquad T(c \mathbf{v})=cT(\mathbf{v})$$

hold. That is, a linear map is a function that preserves addition and scalar multiplication. A linear map from $\mathbb{R}^m$ to $\mathbb{R}^n$ can be expressed in the form of a *matrix* that explicitly lists $n\times m$ coordinates:

$$A=\begin{pmatrix} a_{11} & \cdots & a_{1m} \\ \vdots & \ddots & \vdots \\ a_{n1} & \cdots & a_{nm} \end{pmatrix}$$

but a detailed treatment of this is deferred to linear algebra. All we need to remember is that a linear map is essentially a matrix, and in our case, the *determinant*—a value defined for every square matrix, i.e., every $n\times n$ matrix—is particularly important. Intuitively, this is a value indicating how much the linear map stretches or shrinks volume; in low dimensions it is given by

$$\det\begin{pmatrix} a & b \\ c & d \end{pmatrix}=ad-bc$$

and

$$\det\begin{pmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{pmatrix}=a_{11}a_{22}a_{33}+a_{12}a_{23}a_{31}+a_{13}a_{21}a_{32}-a_{13}a_{22}a_{31}-a_{11}a_{23}a_{32}-a_{12}a_{21}a_{33}.$$

## Limits and Continuity of Multivariable Functions

Before defining the derivative, we need to review limits and continuity of multivariable functions. For single-variable functions, it was sufficient to look at the limit from two directions: the left and right of a point $a$. However, when the domain becomes $\mathbb{R}^m$, there are infinitely many paths approaching a point $\mathbf{a}$, so some care is needed.

::: Definition 1
A multivariable function $f: \mathbb{R}^m \rightarrow \mathbb{R}$ has *limit* $L$ at a point $\mathbf{a}$ if for every $\epsilon > 0$ there exists a $\delta > 0$ such that

$$0 < \lVert \mathbf{x} - \mathbf{a}\rVert < \delta \quad\implies\quad \lvert f(\mathbf{x}) - L\rvert < \epsilon$$

holds for all $\mathbf{x}$ satisfying $0 < \lVert \mathbf{x} - \mathbf{a}\rVert < \delta$. We write this as $\lim_{\mathbf{x}\rightarrow\mathbf{a}} f(\mathbf{x}) = L$, and in particular when $\lim_{\mathbf{x}\rightarrow\mathbf{a}} f(\mathbf{x}) = f(\mathbf{a})$ we say $f$ is *continuous* at $\mathbf{a}$.
:::

The form of this definition is essentially the same as for single-variable functions; the only difference is that the one-dimensional distance $\lvert x - a\rvert$ is replaced by the $m$-dimensional distance $\lVert\mathbf{x} - \mathbf{a}\rVert$. However, for example, to verify that the limit of a given function is $L$, it is **not enough** to check that the following limit

$$\lim_{t\rightarrow 0}f(\mathbf{a}+t\mathbf{v})=L$$

holds for every direction $\mathbf{v}=(v_1, \ldots, v_m)$. For instance, if we define $f:\mathbb{R}^2\rightarrow \mathbb{R}$ by

$$f(\mathbf{x})=\begin{cases}1&\text{if $y=x^2$,}\\ 0&\text{otherwise}\end{cases}$$

then this function has limit $0$ along every straight-line direction, but along the curve $y=x^2$ the limit is $1$. This warning is especially important in the remainder of this post when we define partial derivatives and discuss the differentiability of multivariable functions.

## Differentiation of Multivariable Functions

Now, as promised, we examine the case of multivariable functions—that is, functions that assign a value to each point of $\mathbb{R}^m$. In this case, the function can approach a point not just from the left or right, but from all directions, so direction becomes important when defining the derivative.

The simplest rate of change is the one when moving along only one coordinate axis.

::: Definition 2
The *partial derivative* of a multivariable function $f(x_1, \ldots, x_n)$ at a point $\mathbf{a}$ with respect to the variable $x_i$ is the derivative with respect to $x_i$ alone while holding the remaining variables fixed. That is, it is given by

$$\frac{\partial f}{\partial x_i}(  \mathbf{a}) = \lim_{h\rightarrow 0}\frac{f(\mathbf{a} + h \mathbf{e}_i) - f(\mathbf{a})}{h}$$

where $\mathbf{e}_i$ is the standard basis vector whose $i$th component is $1$ and whose remaining components are $0$. The vector collecting all partial derivatives

$$\nabla f(\mathbf{a}) = \left(\frac{\partial f}{\partial x_1}(\mathbf{a}), \ldots, \frac{\partial f}{\partial x_n}(\mathbf{a})\right)$$

is called the *gradient* of $f$.
:::

Computing partial derivatives is exactly the same as single-variable differentiation except that the remaining variables are treated as constants, so all differentiation rules for single-variable functions apply directly.

However, differentiability requires some caution. To see this, recall that the existence of the limit

$$\lim_{h\rightarrow 0} \frac{f(a+h)-f(a)}{h}$$

means looking at the limit from both directions. In this case the limit yields **a single number**, which is exactly the slope of the tangent line touching the curve.

To generalize this, we must pay attention to two things: one is that $h$ is now an element of a vector space and can approach $0$ from every direction, and the other is that the linear approximation is no longer expressed by a single number. For example, think of a plane tangent to a surface; to parametrize this plane, two variables are needed in addition to the point of tangency.

To resolve this, let us rewrite the familiar equation of a line in the form of an inner product. On the plane, the line passing through a point $\mathbf{a}=(a_1,a_2)$ and perpendicular to a vector $\mathbf{n}=(n_1,n_2)$ is given by the condition that any point $\mathbf{x}=(x,y)$ on it satisfies

$$\mathbf{n}\cdot(\mathbf{x}-\mathbf{a})=0,$$

and substituting everything in gives

$$n_1(x-a_1)+n_2(y-a_2)=0,$$

which is the familiar equation of a line. Similarly, for a *hyperplane* in $\mathbb{R}^m$ passing through a point $\mathbf{a}=(a_1,\ldots, a_m)$ and perpendicular to a vector $\mathbf{n}=(n_1,\ldots, n_m)$, a point $\mathbf{x}=(x_1,\ldots, x_m)$ on it satisfies the same equation

$$\mathbf{n}\cdot(\mathbf{x}-\mathbf{a})=0,$$

which expands to

$$n_1(x_1-a_1)+\cdots+n_m(x_m-a_m)=0,$$

giving the expected form of a linear expression. Finally, writing the limit in the linear expression

$$\lim_{h\rightarrow 0}\frac{f(a+h)-f(a)}{h}=k$$

by moving the right-hand side across as

$$\lim_{h\rightarrow 0}\frac{f(a+h)-(f(a)+kh)}{h}=0,$$

this expression means that the function value $f(a+h)$ near the point $a$ is linearly approximated by the line $y=f(a)+kh$. Since we have seen above how to write linear expressions in $\mathbb{R}^m$, the following definition is now clear.

::: Definition 3
A multivariable function $f$ is *differentiable* at a point $\mathbf{a}$ if there exists a vector $\mathbf{n}$ such that

$$\lim_{\mathbf{h} \rightarrow 0}\frac{f(\mathbf{a} + \mathbf{h}) - f(\mathbf{a}) - \mathbf{n}\cdot \mathbf{h}}{\lVert \mathbf{h}\rVert} = 0$$

holds.
:::

Then the most surprising point is that the vector $\mathbf{n}$ defined in this way actually coincides with the gradient vector $\nabla f(\mathbf{a})$ examined in [Definition 2](#def2) above.

::: Proposition 4
If $f$ is differentiable at a point $\mathbf{a}$, then the vector $\mathbf{n}$ in [Definition 3](#def3) is $\mathbf{n} = \nabla f(\mathbf{a})$, and $f(\mathbf{a}+\mathbf{h}) \approx f(\mathbf{a}) + \nabla f(\mathbf{a})\cdot \mathbf{h}$ is the best linear approximation.
:::

::: Proof
Setting $\mathbf{h} = t \mathbf{e}_i$ in the limit of [Definition 3](#def3), we have $\lVert \mathbf{h}\rVert = \lvert t\rvert$, so

$$\lim_{t \rightarrow 0}\frac{f(\mathbf{a} + t \mathbf{e}_i) - f(\mathbf{a}) - \mathbf{n}\cdot (t \mathbf{e}_i)}{\lvert t\rvert} = 0.$$

We have $\mathbf{n}\cdot (t \mathbf{e}_i) = t n_i$. When $t>0$, $\lvert t\rvert = t$, so rearranging the numerator of the limit by $t$ gives $\frac{f(\mathbf{a} + t \mathbf{e}_i) - f(\mathbf{a})}{t} - n_i$, which by the definition of the partial derivative converges to $\frac{\partial f}{\partial x_i}(\mathbf{a}) - n_i$. The same logic for $t<0$ gives the same conclusion, so for the limit to be $0$ we must have $n_i = \frac{\partial f}{\partial x_i}(\mathbf{a})$. Collecting this for all $i$ gives $\mathbf{n} = \nabla f(\mathbf{a})$.
:::

Note here that we have explicitly separated [Definition 3](#def3) and [Proposition 4](#prop4). [Proposition 4](#prop4) says that **if** the function $f$ is differentiable, then the vector $\mathbf{n}$ satisfying that condition is $\nabla f$; one must **not** interpret this conversely to mean that if all partial derivatives exist and $\nabla f$ is well defined, then $f$ is differentiable. Instead, the following condition shows that a continuous function $f$ is differentiable if each of its partial derivatives is continuous.

::: Proposition 5
If all partial derivatives of a continuous function $f$ exist in a neighborhood of $\mathbf{a}$ and are all continuous at $\mathbf{a}$, then $f$ is differentiable at $\mathbf{a}$.
:::
::: Proof
To simplify notation, we show this for two variables $f(x,y)$ at the point $(a,b)$. The same argument repeated coordinate by coordinate works in general dimensions. Moving one coordinate at a time in the vector $(h,k)$, we split

$$f(a+h, b+k) - f(a,b) = \bigl(f(a+h, b+k) - f(a, b+k)\bigr) + \bigl(f(a, b+k) - f(a,b)\bigr)$$

so that each bracket changes only one variable; by the mean value theorem, for suitable $\theta_1, \theta_2 \in (0,1)$,

$$f(a+h,b+k) - f(a,b) = f_x(a+\theta_1 h, b+k) h + f_y(a, b+\theta_2 k) k,$$

and subtracting $\nabla f(a,b)\cdot(h,k) = f_x(a,b)h + f_y(a,b)k$ gives

$$f(a+h,b+k) - f(a,b) - \nabla f(a,b)\cdot(h,k) = \bigl(f_x(a+\theta_1 h, b+k) - f_x(a,b)\bigr)h + \bigl(f_y(a, b+\theta_2 k) - f_y(a,b)\bigr)k.$$

Since $f_x, f_y$ are continuous at $(a,b)$, both brackets go to $0$ as $(h,k)\rightarrow(0,0)$, and because $\lvert h\rvert, \lvert k\rvert \le \lVert(h,k)\rVert$, the limit in [Definition 3](#def3) holds. Thus $f$ is differentiable at $(a,b)$ and its gradient is $\nabla f(a,b)$.
:::

## Chain Rule and Mixed Partial Derivatives

Now we examine the chain rule for multivariable functions. If only one of the variables input to a multivariable function is given as a composition with another function, then the chain rule can be applied in the same way as in single-variable differentiation using the partial derivative with respect to that variable; the problem arises when several variables input to the multivariable function are defined through other functions.

For this we need a curve $\mathbf{x}(t) = (x_1(t), \ldots, x_n(t))$ parameterized by a single parameter $t$; as defined in [§Curves and Vector-Valued Functions, ⁋Proposition 2](/en/math/calculus/vector_functions#prop2), this is differentiable when each component $x_i(t)$ is differentiable as a single-variable function, and its tangent vector $\mathbf{x}'(t) = (x_1'(t), \ldots, x_n'(t))$ is well defined. Under this, the following holds.

::: Theorem 6 (Multivariable Chain Rule)
If $f$ is differentiable and $\mathbf{x}(t) = (x_1(t), \ldots, x_n(t))$ is a differentiable curve, then the composition $t \mapsto f(\mathbf{x}(t))$ is also differentiable and

$$\frac{d}{\dd{t}} f(\mathbf{x}(t)) = \nabla f(\mathbf{x}(t)) \cdot \mathbf{x}'(t) = \sum_{i=1}^n \frac{\partial f}{\partial x_i} \frac{\dd{x_i}}{\dd{t}}.$$

:::
::: Proof
Applying [Definition 3](#def3) at the point $\mathbf{x}(t)$ with increment $\Delta\mathbf{x}=\mathbf{x}(t+\Delta t)-\mathbf{x}(t)$, as $\Delta t\rightarrow 0$ we have

$$\frac{f(\mathbf{x}(t+\Delta t))-f(\mathbf{x}(t))-\nabla f(\mathbf{x}(t))\cdot\Delta\mathbf{x}}{\lVert\Delta\mathbf{x}\rVert}\rightarrow 0.$$

Dividing both sides by $\Delta t$, the right-hand side splits into a linear term $\nabla f(\mathbf{x}(t))\cdot\frac{\Delta\mathbf{x}}{\Delta t}$ and a remainder term, which is the quantity that went to $0$ above multiplied by $\lVert\Delta\mathbf{x}\rVert/\Delta t$. By differentiability of the curve, $\Delta\mathbf{x}/\Delta t\rightarrow\mathbf{x}'(t)$, so $\lVert\Delta\mathbf{x}\rVert/\lvert\Delta t\rvert$ is bounded, and therefore the remainder term also vanishes as $\Delta t\rightarrow 0$, yielding the formula.
:::

[Theorem 6](#thm6) says that partial derivatives chain together like a chain when one variable depends on several variables, and it is mainly used in coordinate changes. For example, if in $z = f(x,y)$ we change to polar coordinates $x = r\cos\theta$, $y = r\sin\theta$, then $\partial z/\partial r = f_x\cos\theta + f_y\sin\theta$ follows immediately.

On the other hand, for second partial derivatives, the order of differentiation does not matter (under appropriate continuity).

::: Theorem 7 (Clairaut)
If the two mixed partial derivatives $\frac{\partial^2 f}{\partial x \partial y}$ and $\frac{\partial^2 f}{\partial y \partial x}$ both exist and are continuous in a neighborhood of a point, then they are equal at that point.
:::
::: Proof
Let the point be $(a,b)$ and consider the second difference

$$\Delta = f(a+h, b+k) - f(a+h, b) - f(a, b+k) + f(a, b).$$

Setting $\varphi(x) = f(x, b+k) - f(x, b)$, we have $\Delta = \varphi(a+h) - \varphi(a)$, and by the mean value theorem, for a suitable $\theta_1\in(0,1)$, $\Delta = \varphi'(a+\theta_1 h)h = \bigl(f_x(a+\theta_1 h, b+k) - f_x(a+\theta_1 h, b)\bigr)h$. Applying the mean value theorem again to the inner difference with respect to $y$, for a suitable $\theta_2\in(0,1)$,

$$\Delta = \frac{\partial^2 f}{\partial y \partial x}(a+\theta_1 h, b+\theta_2 k) hk.$$

Symmetrically, setting $\psi(y) = f(a+h, y) - f(a, y)$ and swapping the roles of $x$ and $y$, for suitable $\theta_3, \theta_4\in(0,1)$,

$$\Delta = \frac{\partial^2 f}{\partial x \partial y}(a+\theta_3 h, b+\theta_4 k) hk.$$

Dividing both expressions by $hk$ and taking the limit as $(h,k)\rightarrow(0,0)$, since the two mixed partial derivatives are continuous at $(a,b)$, the right-hand sides converge to $\frac{\partial^2 f}{\partial y\partial x}(a,b)$ and $\frac{\partial^2 f}{\partial x\partial y}(a,b)$ respectively, so they are equal.
:::

## Directional Derivatives and the Gradient

The *directional derivative* $D_{\mathbf{u}} f(\mathbf{a})$, which is the rate of change when moving along a unit vector $\mathbf{u}$, is by definition the derivative at $t = 0$ of the single-variable function $g(t) = f(\mathbf{a} + t\mathbf{u})$; applying the chain rule of [Theorem 6](#thm6) to $\mathbf{x}(t) = \mathbf{a} + t\mathbf{u}$ gives $D_{\mathbf{u}} f(\mathbf{a}) = g'(0) = \nabla f(\mathbf{a})\cdot \mathbf{u}$ immediately. Then the following holds.

::: Proposition 8 (Direction of Steepest Ascent)
If $f$ is differentiable at $\mathbf{a}$ and $\nabla f(\mathbf{a}) \neq 0$, then the directional derivative $D_{\mathbf{u}} f(\mathbf{a})$ in the direction of a unit vector $\mathbf{u}$ is maximized when $\mathbf{u} = \nabla f(\mathbf{a})/\lVert\nabla f(\mathbf{a})\rVert$, and the maximum value is $\lVert\nabla f(\mathbf{a})\rVert$.
:::

::: Proof
By differentiability, for any unit vector $\mathbf{u}$ we have $D_{\mathbf{u}} f(\mathbf{a}) = \nabla f(\mathbf{a})\cdot \mathbf{u}$. By the Cauchy–Schwarz inequality,

$$\begin{aligned}
D_{\mathbf{u}} f(\mathbf{a}) = \nabla f(\mathbf{a})\cdot \mathbf{u} &\leq \lVert\nabla f(\mathbf{a})\rVert \lVert \mathbf{u}\rVert \\
&= \lVert\nabla f(\mathbf{a})\rVert
\end{aligned}$$

and equality holds when $\mathbf{u}$ is in the same direction as $\nabla f(\mathbf{a})$, i.e., when $\mathbf{u} = \nabla f(\mathbf{a})/\lVert\nabla f(\mathbf{a})\rVert$. Therefore the directional derivative attains its maximum value $\lVert\nabla f(\mathbf{a})\rVert$ at this $\mathbf{u}$. By the same logic, the minimum value $-\lVert\nabla f(\mathbf{a})\rVert$ is attained in the opposite direction, so $-\nabla f$ is the direction of steepest descent.
:::

[Proposition 8](#prop8) provides the geometric justification for gradient descent, which finds a minimum by moving along the gradient. Meanwhile, the gradient is perpendicular to level surfaces $f = c$: for a curve $\mathbf{x}(t)$ on a level surface, $f(\mathbf{x}(t)) = c$ is constant, so by the chain rule $\nabla f\cdot \mathbf{x}'(t) = 0$, meaning the gradient is orthogonal to every tangent vector.

## Extrema and the Hessian Matrix

Just as extrema of single-variable functions occurred at critical points, extrema of differentiable multivariable functions can only occur at *critical points* where $\nabla f = 0$, since each partial derivative must be zero. In the single-variable case we could determine whether a critical point was a local maximum or minimum using the second derivative ([§Mean Value Theorem, ⁋Proposition 17](/en/math/calculus/mean_value_theorem#prop17)), and a similar situation occurs for multivariable functions.

However, one must be careful: because there are now many directions in which one can differentiate, there can exist a point that is a local minimum in one direction and a local maximum in another. Such a point is called a *saddle point*. In this section we will determine when a critical point is a local maximum, local minimum, or saddle point; for computational convenience we restrict our attention to multivariable functions defined on $\mathbb{R}^2$.

Taylor expanding a differentiable function of two variables near a critical point, the first-order term vanishes because $\nabla f(\mathbf{a}) = 0$, and the remaining second-order term is

$$f(\mathbf{a}+\mathbf{h}) \approx f(\mathbf{a}) + \frac{1}{2}\bigl(f_{xx}(\mathbf{a})h_1^2 + 2f_{xy}(\mathbf{a})h_1 h_2 + f_{yy}(\mathbf{a})h_2^2\bigr).$$

The coefficients of this quadratic form collected into a square matrix give the *Hessian matrix* at the critical point $\mathbf{a}$, given by the expression

$$H = \begin{pmatrix} f_{xx} & f_{xy} \\ f_{yx} & f_{yy}\end{pmatrix}.$$

The increase or decrease at the critical point is determined by the definiteness of this quadratic form, which we explain in the language of the discriminant as follows.

::: Proposition 9 (Second Derivative Test)
Let $f$ be $C^2$ and let $\mathbf{a}$ be a critical point ($\nabla f(\mathbf{a}) = 0$), and consider the discriminant $D = f_{xx}f_{yy} - f_{xy}^2 = \det H$ of the Hessian matrix above.

1. If $D > 0$ and $f_{xx} > 0$, then $\mathbf{a}$ is a local minimum.
2. If $D > 0$ and $f_{xx} < 0$, then this point is a local maximum.
3. If $D < 0$, then this point is a saddle point.
:::

::: Proof
Consider the quadratic term $f_{xx}h_1^2 + 2f_{xy}h_1 h_2 + f_{yy}h_2^2$ remaining from the expansion near a critical point. First, when $f_{xx} \neq 0$, completing the square with respect to $h_1$ gives

$$\begin{aligned}
f_{xx}h_1^2 + 2f_{xy}h_1 h_2 + f_{yy}h_2^2
&= f_{xx} \left(h_1 + \frac{f_{xy}}{f_{xx}}h_2\right)^2 + \frac{f_{xx}f_{yy} - f_{xy}^2}{f_{xx}} h_2^2 \\
&= f_{xx} \left(h_1 + \frac{f_{xy}}{f_{xx}}h_2\right)^2 + \frac{D}{f_{xx}} h_2^2
\end{aligned}$$

so the sign of the first term follows $f_{xx}$, and the sign of the second term follows $D/f_{xx}$. In particular, if $D > 0$ then $D/f_{xx}$ has the same sign as $f_{xx}$, so the two terms have the same sign. Additionally, if $f_{xx} > 0$, then the quadratic terms are always positive as long as they are not both zero, so the function values increase near $\mathbf{a}$ and this point becomes a local minimum; conversely, if $f_{xx} < 0$ they are always negative and it is a local maximum. On the other hand, if $D < 0$ the two terms have opposite signs, so depending on the ratio of $h_1, h_2$ the quadratic term takes both positive and negative values, and $\mathbf{a}$ is a saddle point.
:::

The saddle point that appears when the discriminant is negative can be said to be the simplest critical point where the function rises and falls depending on direction.

::: Example 10 (Saddle point)
$f(x,y) = x^2 - y^2$ has a critical point at $(0,0)$ where $\nabla f = (2x, -2y) = 0$. The Hessian matrix is $\begin{pmatrix} 2 & 0 \\ 0 & -2\end{pmatrix}$ with $\det H = -4 < 0$, so it is a saddle point. Indeed, along the $x$-axis we have $f = x^2$, a local minimum, and along the $y$-axis we have $f = -y^2$, a local maximum, forming a saddle shape that rises and falls depending on direction. The figure below shows the surface $z = x^2 - y^2$, with the origin (black dot) being the saddle point.

{% diagram Math/Calculus/Partial_Derivatives-1.svg width="21.37em" alt="saddle_surface" %}
:::

However, note that when $D=0$ the above test gives no information whatsoever. In such cases one must use an appropriate method suited to each situation.

## Lagrange Multipliers

One of the nice applications of differentiation was finding extrema of a function on a given interval $[a,b]$. We treat this for multivariable functions. The difference is that the variables are no longer a simple interval; for example, one may also consider a situation where the variables must satisfy some constraint $g(\mathbf{x}) = c$. For instance, finding the point closest to the origin on a given surface, or minimizing cost within fixed resources, are of this kind. The standard tool for finding such *constrained extrema* is the method of Lagrange multipliers.

::: Proposition 11 (Lagrange Multipliers)
Let $f, g:\mathbb{R}^n\rightarrow\mathbb{R}$ be $C^1$, and suppose a point $\mathbf{a}$ is a local extremum of $f$ subject to the constraint $g(\mathbf{x}) = c$ and that $\nabla g(\mathbf{a}) \neq 0$. Then there exists a real number $\lambda$ such that

$$\nabla f(\mathbf{a}) = \lambda \nabla g(\mathbf{a})$$

holds.
:::
::: Proof
Pick any smooth curve $\mathbf{x}(t)$ on the constraint surface $\{g = c\}$ passing through $\mathbf{a}$ ($\mathbf{x}(0) = \mathbf{a}$). Since $g(\mathbf{x}(t)) = c$ is constant, differentiating by [Theorem 6](#thm6) gives $\nabla g(\mathbf{a}) \cdot \mathbf{x}'(0) = 0$, and on the other hand, since $\mathbf{a}$ gives an extremum of $f$ under the constraint, $t \mapsto f(\mathbf{x}(t))$ also has an extremum at $t = 0$, and therefore $\nabla f(\mathbf{a}) \cdot \mathbf{x}'(0) = 0$. That is, both vectors $\nabla f(\mathbf{a})$ and $\nabla g(\mathbf{a})$ are orthogonal to the tangent space of the constraint surface. But since the whole space is $n$-dimensional and the tangent space of the constraint surface is $n-1$-dimensional, there is only one such direction, and therefore there exists a real number $\lambda$ such that $\nabla f(\mathbf{a}) = \lambda \nabla g(\mathbf{a})$.
:::

In actual computation, the newly introduced real number $\lambda$ is added as an unknown and the system consisting of $\nabla f = \lambda \nabla g$ together with the constraint equation $g = c$ is solved simultaneously; this $\lambda$ is called the *Lagrange multiplier*.

::: Example 12 (Lagrange Multipliers)
Find the extrema of $f(x,y) = xy$ subject to the constraint $g(x,y) = x^2 + y^2 = 1$. Since $\nabla f = (y, x)$ and $\nabla g = (2x, 2y)$, the equation $\nabla f = \lambda \nabla g$ gives

$$\begin{aligned}
y &= 2\lambda x, \\
x &= 2\lambda y.
\end{aligned}$$

Multiplying the two equations gives $xy = 4\lambda^2 xy$, so either $xy = 0$ or $\lambda^2 = 1/4$. If $xy = 0$, the constraint gives $(\pm 1, 0)$ or $(0, \pm 1)$, and then $f = 0$. If $\lambda = \pm 1/2$, then $y = \pm x$ and the constraint $2x^2 = 1$ gives $x = \pm 1/\sqrt2$, so $f = xy = \pm 1/2$. Therefore, on the unit circle, the maximum value of $f = xy$ is $1/2$ and the minimum value is $-1/2$.
:::

---

**References**

**[Ste]** J. Stewart, *Calculus*, 8th ed., Cengage Learning, 2016.  
**[Kim]** 김홍종, *미적분학 1·2*, 제3개정판, 서울대학교출판문화원, 2020.
