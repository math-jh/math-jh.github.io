---
title: "Least Squares Method"
description: "This post derives the least squares method via normal equations in Euclidean and inner product spaces, and covers line fitting for points on a plane as well as the pseudoinverse."
excerpt: "Orthogonal Projection and Least Squares Method"

categories: [Math / Linear Algebra]
permalink: /en/math/linear_algebra/least_squares_method
sidebar: 
    nav: "linear_algebra-en"


date: 2022-10-09
last_modified_at: 2022-10-09

weight: 118
translated_at: 2026-06-01T03:00:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-01T03:00:04+00:00
---
## Least Squares Method

We first develop the least squares method in the setting of Euclidean spaces $$\mathbb{R}^n$$ equipped with the dot product. However, just as in [§Bilinear Forms, §§Non-Degenerate Bilinear Forms](/en/math/linear_algebra/bilinear_form#non-degenerate-bilinear-forms), this can be generalized to an arbitrary $$\mathbb{R}$$-inner product space.

Consider an arbitrary matrix $$A\in\Mat_{m\times n}(\mathbb{R})$$ and the system of linear equations $$Ax=y$$. If $$m=n$$ and $$A$$ is invertible, this equation has a unique solution, but in general this is not the case. Let us consider especially the case $$m>n$$. Then $$\rank(A)\leq n< m$$, so for most $$y$$ other than those in the image of $$A$$, this equation cannot be solved.

A representative example is finding an appropriate function that represents various given data. Of course, using Lagrange interpolation we can choose an appropriate basis to find an $$n$$-th degree function approximating $$n+1$$ given data points, but if we try to find a linear function representing this data, for example, we cannot find an exact solution unless all $$n+1$$ given points lie on a single line.

We project a given vector $$y$$ onto $$\im A$$, and then solve the equation $$Ax=y'$$ for this vector $$y'=\proj_{\im(A)}y$$. Since we saw in the previous post that $$y-y'\in (\im A)^\perp$$, we have

$$\langle y-y', v\rangle=0\qquad\text{for all $v\in \im A$}$$

and therefore we obtain

$$\langle y-y', Au\rangle=0\qquad\text{for all $u\in \mathbb{R}^n$}$$

Moving $$A$$ to the left gives

$$\langle A^t(y-y'), u\rangle=0\qquad\text{for all $u\in\mathbb{R}^n$}$$

and since $$\langle-,-\rangle$$ is non-degenerate we know that $$A^t(y-y')=0$$. Since $$y'=Ax$$, we obtain the equation

$$A^tAx=A^ty$$

We summarize this process as follows.

<div class="proposition" markdown="1">

<ins id="prop1">**Proposition 1**</ins> For any matrix $$A\in\Mat_{m\times n}(\mathbb{R})$$ and any $$y\in\mathbb{R}^m$$, a vector $$x\in\mathbb{R}^n$$ minimizes the value of $$\lVert Au-y\rVert$$ if and only if it satisfies the equation

$$A^tAx=A^ty$$

</div>

The example discussed in the introduction can be solved in the following way.

<div class="example" markdown="1">

<ins id="ex2">**Example 2**</ins> Suppose three points $$(0,1)$$, $$(1,3)$$, $$(2,4)$$ are given in the plane, and consider the problem of finding the line $$y=ax+b$$ that best fits them. If all three points lay on a single line, then the system of equations in the unknowns $$a,b$$

$$\begin{aligned}a\cdot 0+b&=1\\ a\cdot 1+b&=3\\ a\cdot 2+b&=4\end{aligned}$$

would have a solution, but since the three points do not lie on a line, an exact solution does not exist. Writing this system in the form $$Ax=y$$ gives

$$A=\begin{pmatrix}0&1\\ 1&1\\ 2&1\end{pmatrix},\qquad x=\begin{pmatrix}a\\ b\end{pmatrix},\qquad y=\begin{pmatrix}1\\ 3\\ 4\end{pmatrix}$$

where the first column of $$A$$ contains the $$x$$-coordinates of each point, and the second column contains the constant $$1$$. By [Proposition 1](#prop1), the pair $$(a,b)$$ minimizing $$\lVert Ax-y\rVert$$ is given as the solution of the normal equation

$$A^tAx=A^ty$$

Direct computation yields

$$A^tA=\begin{pmatrix}5&3\\ 3&3\end{pmatrix},\qquad A^ty=\begin{pmatrix}11\\ 8\end{pmatrix}$$

and since $$\det(A^tA)=5\cdot 3-3\cdot 3=6\neq 0$$, the matrix $$A^tA$$ is invertible. Therefore we obtain

$$\begin{pmatrix}a\\ b\end{pmatrix}=(A^tA)^{-1}A^ty=\frac{1}{6}\begin{pmatrix}3&-3\\ -3&5\end{pmatrix}\begin{pmatrix}11\\ 8\end{pmatrix}=\frac{1}{6}\begin{pmatrix}9\\ 7\end{pmatrix}=\begin{pmatrix}3/2\\ 7/6\end{pmatrix}$$

That is, the line that best fits the three given points in the least squares sense is $$y=\frac{3}{2}x+\frac{7}{6}$$.

</div>

More generally, even if we choose the inner product $$\langle-,-\rangle$$ to be the $$L^2$$-inner product on a space of functions rather than the dot product, similar examples can be carried out.

## Pseudoinverse

This time, conversely, we consider the case where the matrix $$A\in\Mat_{m\times n}(\mathbb{R})$$ satisfies $$m< n$$.

First suppose arbitrary $$A\in\Mat_{m\times n}(\mathbb{R})$$ and $$y\in\im(A)$$ are given, and assume that $$A$$ is not injective. Then there exist nonzero vectors $$u$$ satisfying $$Au=0$$, and thus if a vector $$x$$ satisfying $$Ax=y$$ is given, the vectors $$x+u$$ are also solutions. Let us now find among these the solution with the smallest norm and call it the *minimum-norm solution*. That is, the entire set of solutions to $$Ax=y$$ forms the affine subspace $$x_0+\ker A$$ for a particular solution $$x_0$$, and we seek the point minimizing the norm on this affine subspace.

This is exactly the situation addressed by the projection theorem in [§Inner Product Spaces, ⁋Theorem 9](/en/math/linear_algebra/inner_product_spaces#thm9). The point minimizing the distance from the origin to the affine subspace $$x_0+\ker A$$ is unique, and the vector drawn from this point to the affine subspace is perpendicular to $$\ker A$$. Therefore the minimum-norm solution is the unique solution lying in $$(\ker A)^\perp$$. On the other hand, by [§Bilinear Forms, ⁋Proposition 5](/en/math/linear_algebra/bilinear_form#prop5) we have $$(\ker A)^\perp=\im A^t$$. We summarize this as follows.

<div class="proposition" markdown="1">

<ins id="prop3">**Proposition 3**</ins> For any matrix $$A\in\Mat_{m\times n}(\mathbb{R})$$ and any $$y\in\im A$$, among the solutions of the equation $$Ax=y$$ there exists a unique solution minimizing the norm, and this is the unique solution belonging to $$\im A^t$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Since $$y\in\im A$$, there exists $$x_0$$ satisfying $$Ax_0=y$$, and the set of all solutions of $$Ax=y$$ equals $$x_0+\ker A$$. By [§Bilinear Forms, ⁋Proposition 5](/en/math/linear_algebra/bilinear_form#prop5),

$$\mathbb{R}^n=\ker A\oplus(\ker A)^\perp$$

holds, so we can decompose $$x_0$$ as $$x_0=p+q$$. Here $$p\in (\ker A)^\perp$$ and $$q\in\ker A$$. Then $$p=x_0-q$$ is also a solution of $$Ax=y$$, and for any solution $$x=p+u$$ (with $$u\in\ker A$$), since $$p\perp u$$, the Pythagorean theorem gives

$$\lVert x\rVert^2=\lVert p\rVert^2+\lVert u\rVert^2\geq \lVert p\rVert^2$$

Equality holds only when $$u=0$$, that is, only when $$x=p$$, so the solution minimizing the norm is unique and equals $$p$$. Moreover, by the same proposition $$(\ker A)^\perp=\im A^t$$, so $$p\in\im A^t$$.

</details>

Let us now consider the case where we can compute this minimum-norm solution explicitly. If $$A$$ has *full row rank*, that is, if $$\rank A=m$$, then $$\im A=\mathbb{R}^m$$, so $$Ax=y$$ has a solution for every $$y\in\mathbb{R}^m$$, and by the above proposition the minimum-norm solution is uniquely determined on $$\im A^t$$.

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4**</ins> If a matrix $$A\in\Mat_{m\times n}(\mathbb{R})$$ satisfies $$\rank A=m$$, then $$AA^t\in\Mat_m(\mathbb{R})$$ is invertible, and for any $$y\in\mathbb{R}^m$$ the minimum-norm solution of the equation $$Ax=y$$ is given by

$$x=A^t(AA^t)^{-1}y$$

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First we show that $$AA^t$$ is invertible. Since $$AA^t$$ is an $$m\times m$$ square matrix, it suffices to show that $$AA^tz=0$$ has only the solution $$z=0$$. Suppose $$AA^tz=0$$; then

$$\lVert A^tz\rVert^2=\langle A^tz, A^tz\rangle=\langle z, AA^tz\rangle=0$$

so $$A^tz=0$$, that is, $$z\in\ker A^t$$. But since $$\rank A^t=\rank A=m$$, the map $$A^t$$ is injective, and therefore $$z=0$$. This shows that $$AA^t$$ is invertible.

Now set $$x=A^t(AA^t)^{-1}y$$; then

$$Ax=AA^t(AA^t)^{-1}y=y$$

so $$x$$ is a solution of $$Ax=y$$. Moreover, since $$x=A^t\big((AA^t)^{-1}y\big)\in\im A^t$$, by [Proposition 3](#prop3) the vector $$x$$ is the minimum-norm solution.

</details>

As we saw in the proof, from the fact that the minimum-norm solution lies on $$\im A^t$$ we may assume the form $$x=A^tz$$, substitute this into $$Ax=y$$, and solve $$AA^tz=y$$ to obtain $$z=(AA^t)^{-1}y$$. Then $$A^t(AA^t)^{-1}$$ becomes a *right inverse* of $$A$$, that is, a matrix satisfying $$A\cdot A^t(AA^t)^{-1}=I_m$$.

The case of least squares treated in the previous section and the case of minimum norm treated in this section can be regarded as dual situations to each other. If $$A$$ has *full column rank*, that is, if $$\rank A=n$$, then $$A^tA$$ is invertible and the normal equation of [Proposition 1](#prop1) gives the unique least squares solution $$x=(A^tA)^{-1}A^ty$$; in this case $$(A^tA)^{-1}A^t$$ becomes a left inverse of $$A$$. On the other hand, if $$A$$ has full row rank, then as above the right inverse $$A^t(AA^t)^{-1}$$ gives the minimum-norm solution. The following concept unifies these two matrices.

<div class="definition" markdown="1">

<ins id="def5">**Definition 5**</ins> For a matrix $$A\in\Mat_{m\times n}(\mathbb{R})$$, if $$A$$ has full column rank we define

$$A^+:=(A^tA)^{-1}A^t$$

and if $$A$$ has full row rank we define

$$A^+:=A^t(AA^t)^{-1}$$

The matrix $$A^+\in\Mat_{n\times m}(\mathbb{R})$$ is called the *Moore-Penrose pseudoinverse* of $$A$$.

</div>

These two formulas cannot be used as they are in a general situation without the rank assumption on $$A$$, because at least one of $$A^tA$$ or $$AA^t$$ is not invertible. The pseudoinverse for a general matrix is defined using the singular value decomposition, and when $$A$$ falls into one of the two cases above, this definition coincides with the formulas above. It is known that $$A^+$$ is then uniquely characterized by the following four conditions:

$$AA^+A=A,\quad A^+AA^+=A^+,\quad (AA^+)^t=AA^+,\quad (A^+A)^t=A^+A$$

and through this one can verify that $$A^+$$ is well defined by $$A$$.

<div class="remark" markdown="1">

<ins id="rmk6">**Remark 6**</ins> If $$A$$ is an invertible square matrix, then $$A^+=A^{-1}$$ holds. This is because both $$A^tA$$ and $$AA^t$$ are invertible, so that $$A^+=(A^tA)^{-1}A^t=A^{-1}(A^t)^{-1}A^t=A^{-1}$$. In this sense the pseudoinverse generalizes the notion of an inverse.

</div>

Introducing the pseudoinverse unifies the least squares problem of the previous section and the minimum-norm problem of this section into a single formula. If $$A$$ has full column rank, then $$x=A^+y=(A^tA)^{-1}A^ty$$ is the unique least squares solution minimizing $$\lVert Ax-y\rVert$$, and if $$A$$ has full row rank, then $$x=A^+y=A^t(AA^t)^{-1}y$$ is the minimum-norm solution of $$Ax=y$$. Even for a general matrix, $$x=A^+y$$ gives the unique solution among those minimizing $$\lVert Ax-y\rVert$$ that again has the smallest norm, and thus the problems treated separately in the two sections are naturally unified into a single object called the pseudoinverse.
