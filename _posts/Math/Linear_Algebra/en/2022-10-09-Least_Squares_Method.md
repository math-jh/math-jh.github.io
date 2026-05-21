---
title: "Least Squares Method (Draft)"
excerpt: "Orthogonal Projection and the Least Squares Method"

categories: [Math / Linear Algebra]
permalink: /en/math/linear_algebra/least_squares_method
sidebar: 
    nav: "linear_algebra-en"

header:
    overlay_image: /assets/images/Math/Linear_Algebra/Least_Squares_Method.png
    overlay_filter: 0.5

date: 2022-10-09
last_modified_at: 2022-10-09

weight: 118
translated_at: 2026-05-21T13:00:02+00:00
translation_source: kimi-cli
---
## Least Squares Method

We first consider the method of least squares, which we are about to introduce, in the setting of Euclidean spaces $$\mathbb{R}^n$$ equipped with the dot product. However, we can generalize it to a general $$\mathbb{R}$$-inner product space in exactly the same way as we did in [§Bilinear Forms, §§Non-degenerate Bilinear Forms](/en/math/linear_algebra/bilinear_form#비퇴화-쌍선형형식).

Consider an arbitrary matrix $$A\in\Mat_{m\times n}(\mathbb{R})$$ and the system of linear equations $$Ax=y$$. If $$m=n$$ and $$A$$ is invertible, then this equation has a unique solution, but this is not the case in general. In particular, consider the case where $$m>n$$. Then since $$\rank(A)\leq n< m$$, for most $$y$$ not belonging to the image of $$A$$, this equation cannot be solved.

A typical example is finding an appropriate function that represents given data. Of course, using Lagrange interpolation we can find an $$n$$-th degree function approximating the given $$n+1$$ data points by choosing an appropriate basis, but if we try to find a linear function representing this data, for example, we cannot find an exact solution unless all the given $$n+1$$ points lie on a single straight line.

We project an arbitrary given vector $$y$$ onto $$\im A$$, and then solve the equation $$Ax=y'$$ for this vector $$y'=\proj_{\im(A)}y$$. However, since we know from the previous post that $$y-y'\in (\im A)^\perp$$, we also know that

$$\langle y-y', v\rangle=0\qquad\text{for all $v\in \im A$}$$

Therefore, we obtain the following equation:

$$\langle y-y', Au\rangle=0\qquad\text{for all $u\in \mathbb{R}^n$}$$

Now, moving $$A$$ to the left,

$$\langle A^t(y-y'), u\rangle=0\qquad\text{for all $u\in\mathbb{R}^n$}$$

and since $$\langle-,-\rangle$$ is non-degenerate, we know that $$A^t(y-y')=0$$. Now since $$y'=Ax$$, we obtain the equation

$$A^tAx=A^ty$$

Summarizing this process, we have the following.

<div class="proposition" markdown="1">

<ins id="prop1">**Proposition 1**</ins> For any matrix $$A\in\Mat_{m\times n}(\mathbb{R})$$ and $$y\in\mathbb{R}^m$$, a vector $$x\in\mathbb{R}^n$$ minimizes the value of the real number $$\lVert Au-y\rVert$$ if and only if the following equation holds:

$$A^tAx=A^ty$$

</div>

The example discussed in the introduction can be solved in the following way.

<div class="example" markdown="1">

<ins id="ex2">**Example 2**</ins> 

</div>

More generally, even if we choose the inner product $$\langle-,-\rangle$$ as the $$L^2$$-inner product on a space of functions rather than the dot product, similar examples can be repeated.

## Pseudoinverse

This time, conversely, we consider the case where $$m< n$$ for a matrix $$A\in\Mat_{m\times n}(\mathbb{R})$$.

First, suppose arbitrary $$A\in\Mat_{m\times n}(\mathbb{R})$$ and $$y\in\im(A)$$ are given, and assume that $$A$$ is not injective. Then there exist nonzero vectors $$u$$ satisfying $$Au=0$$, and thus, if one vector $$x$$ satisfying $$Ax=y$$ is given, we can see that $$x+u$$ are also solutions. Now let us find the solution with the smallest norm among these and call it the *minimum-norm solution*.
