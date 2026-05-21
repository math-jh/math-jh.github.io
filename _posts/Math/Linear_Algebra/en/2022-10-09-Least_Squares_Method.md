---
title: "Least Squares Method"
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

<ins id="ex2">**Example 2**</ins> Suppose three points $$(0,1)$$, $$(1,3)$$, $$(2,4)$$ in the plane are given, and consider the problem of finding the line $$y=ax+b$$ that best fits them. If the three points all lay on a single line, the system of equations in the unknowns $$a,b$$

$$\begin{aligned}a\cdot 0+b&=1\\ a\cdot 1+b&=3\\ a\cdot 2+b&=4\end{aligned}$$

would have to have a solution, but since the three points are not collinear, no exact solution exists. Writing this system in the form $$Ax=y$$,

$$A=\begin{pmatrix}0&1\\ 1&1\\ 2&1\end{pmatrix},\qquad x=\begin{pmatrix}a\\ b\end{pmatrix},\qquad y=\begin{pmatrix}1\\ 3\\ 4\end{pmatrix}$$

where the first column of $$A$$ holds the $$x$$-coordinate of each point and the second column holds the constant $$1$$. By [Proposition 1](#prop1), the $$(a,b)$$ minimizing $$\lVert Ax-y\rVert$$ is given by the solution of the normal equation

$$A^tAx=A^ty$$

A direct computation gives

$$A^tA=\begin{pmatrix}5&3\\ 3&3\end{pmatrix},\qquad A^ty=\begin{pmatrix}11\\ 8\end{pmatrix}$$

and since $$\det(A^tA)=5\cdot 3-3\cdot 3=6\neq 0$$, the matrix $$A^tA$$ is invertible. Therefore

$$\begin{pmatrix}a\\ b\end{pmatrix}=(A^tA)^{-1}A^ty=\frac{1}{6}\begin{pmatrix}3&-3\\ -3&5\end{pmatrix}\begin{pmatrix}11\\ 8\end{pmatrix}=\frac{1}{6}\begin{pmatrix}9\\ 7\end{pmatrix}=\begin{pmatrix}3/2\\ 7/6\end{pmatrix}$$

Thus the line that best fits the three points in the least-squares sense is $$y=\frac{3}{2}x+\frac{7}{6}$$.

</div>

More generally, even if we choose the inner product $$\langle-,-\rangle$$ as the $$L^2$$-inner product on a space of functions rather than the dot product, similar examples can be repeated.

## Pseudoinverse

This time, conversely, we consider the case where $$m< n$$ for a matrix $$A\in\Mat_{m\times n}(\mathbb{R})$$.

First, suppose arbitrary $$A\in\Mat_{m\times n}(\mathbb{R})$$ and $$y\in\im(A)$$ are given, and assume that $$A$$ is not injective. Then there exist nonzero vectors $$u$$ satisfying $$Au=0$$, and thus, if one vector $$x$$ satisfying $$Ax=y$$ is given, we can see that $$x+u$$ are also solutions. Now let us find the solution with the smallest norm among these and call it the *minimum-norm solution*. That is, the set of all solutions of $$Ax=y$$ has the form $$x_0+\ker A$$ for a particular solution $$x_0$$, and we seek the point on this affine subspace that minimizes the norm.

This is exactly the situation handled by the projection theorem of [§Inner Product Spaces, ⁋Theorem 9](/en/math/linear_algebra/inner_product_spaces#thm9). The point minimizing the distance from the origin to the affine subspace $$x_0+\ker A$$ is unique, and the vector drawn from this point to the affine subspace is orthogonal to $$\ker A$$. Hence the minimum-norm solution is the unique solution lying in $$(\ker A)^\perp$$. On the other hand, by [§Bilinear Forms, ⁋Proposition 5](/en/math/linear_algebra/bilinear_form#prop5) we have $$(\ker A)^\perp=\im A^t$$. Summarizing,

<div class="proposition" markdown="1">

<ins id="prop3">**Proposition 3**</ins> For any matrix $$A\in\Mat_{m\times n}(\mathbb{R})$$ and $$y\in\im A$$, among the solutions of the equation $$Ax=y$$ there exists a unique solution of minimum norm, and it is the unique solution belonging to $$\im A^t$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Since $$y\in\im A$$, there exists $$x_0$$ with $$Ax_0=y$$, and the set of all solutions of $$Ax=y$$ equals $$x_0+\ker A$$. By [§Bilinear Forms, ⁋Proposition 5](/en/math/linear_algebra/bilinear_form#prop5),

$$\mathbb{R}^n=\ker A\oplus(\ker A)^\perp$$

holds, so we can decompose $$x_0$$ as $$x_0=p+q$$ with $$p\in (\ker A)^\perp$$ and $$q\in\ker A$$. Then $$p=x_0-q$$ is also a solution of $$Ax=y$$, and for any solution $$x=p+u$$ (with $$u\in\ker A$$), since $$p\perp u$$, the Pythagorean theorem gives

$$\lVert x\rVert^2=\lVert p\rVert^2+\lVert u\rVert^2\geq \lVert p\rVert^2.$$

Equality holds only when $$u=0$$, i.e. $$x=p$$, so the minimum-norm solution is uniquely $$p$$. Moreover, by the same proposition $$(\ker A)^\perp=\im A^t$$, so $$p\in\im A^t$$.

</details>

Now we consider the case in which this minimum-norm solution can be computed explicitly. When $$A$$ has *full row rank*, i.e. $$\rank A=m$$, we have $$\im A=\mathbb{R}^m$$, so $$Ax=y$$ has a solution for every $$y\in\mathbb{R}^m$$, and by the proposition above the minimum-norm solution is uniquely determined on $$\im A^t$$.

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4**</ins> If a matrix $$A\in\Mat_{m\times n}(\mathbb{R})$$ satisfies $$\rank A=m$$, then $$AA^t\in\Mat_m(\mathbb{R})$$ is invertible, and for any $$y\in\mathbb{R}^m$$ the minimum-norm solution of the equation $$Ax=y$$ is given by

$$x=A^t(AA^t)^{-1}y.$$

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

We first show that $$AA^t$$ is invertible. Since $$AA^t$$ is an $$m\times m$$ square matrix, it suffices to show that $$AA^tz=0$$ has only $$z=0$$ as a solution. Suppose $$AA^tz=0$$. Then

$$\lVert A^tz\rVert^2=\langle A^tz, A^tz\rangle=\langle z, AA^tz\rangle=0,$$

so $$A^tz=0$$, i.e. $$z\in\ker A^t$$. But since $$\rank A^t=\rank A=m$$, the map $$A^t$$ is injective, and therefore $$z=0$$. Hence $$AA^t$$ is invertible.

Now setting $$x=A^t(AA^t)^{-1}y$$,

$$Ax=AA^t(AA^t)^{-1}y=y,$$

so $$x$$ is a solution of $$Ax=y$$. Furthermore, $$x=A^t\big((AA^t)^{-1}y\big)\in\im A^t$$, so by [Proposition 3](#prop3) $$x$$ is the minimum-norm solution.

</details>

As seen in the proof, from the fact that the minimum-norm solution lies in $$\im A^t$$, we may assume $$x=A^tz$$ and substitute into $$Ax=y$$ to solve $$AA^tz=y$$, obtaining $$z=(AA^t)^{-1}y$$. Here $$A^t(AA^t)^{-1}$$ is the *right inverse* of $$A$$, i.e. the matrix satisfying $$A\cdot A^t(AA^t)^{-1}=I_m$$.

The least-squares case treated in the previous section and the minimum-norm case treated in this section can be viewed as dual situations. When $$A$$ has *full column rank*, i.e. $$\rank A=n$$, the matrix $$A^tA$$ is invertible, so the normal equation of [Proposition 1](#prop1) gives the unique least-squares solution $$x=(A^tA)^{-1}A^ty$$, and here $$(A^tA)^{-1}A^t$$ is the left inverse of $$A$$. On the other hand, when $$A$$ has full row rank, the right inverse $$A^t(AA^t)^{-1}$$ gives the minimum-norm solution as above. The concept that unifies these two matrices is the following.

<div class="definition" markdown="1">

<ins id="def5">**Definition 5**</ins> For a matrix $$A\in\Mat_{m\times n}(\mathbb{R})$$, the matrix $$A^+\in\Mat_{n\times m}(\mathbb{R})$$ defined by

$$A^+:=(A^tA)^{-1}A^t$$

if $$A$$ has full column rank, and by

$$A^+:=A^t(AA^t)^{-1}$$

if $$A$$ has full row rank, is called the *Moore-Penrose pseudoinverse* of $$A$$.

</div>

The two formulas above cannot be used directly in the general situation with no rank assumption on $$A$$, because at least one of $$A^tA$$ and $$AA^t$$ fails to be invertible. The pseudoinverse of a general matrix is defined via the singular value decomposition, and when $$A$$ falls into one of the two cases above, that definition agrees with the formulas above. In this case $$A^+$$ is known to be uniquely characterized by the four conditions

$$AA^+A=A,\quad A^+AA^+=A^+,\quad (AA^+)^t=AA^+,\quad (A^+A)^t=A^+A,$$

through which one verifies that $$A^+$$ is well defined by $$A$$.

<div class="remark" markdown="1">

<ins id="rmk6">**Remark 6**</ins> If $$A$$ is an invertible square matrix, then $$A^+=A^{-1}$$ holds. This is because both $$A^tA$$ and $$AA^t$$ are invertible, so $$A^+=(A^tA)^{-1}A^t=A^{-1}(A^t)^{-1}A^t=A^{-1}$$. In this sense the pseudoinverse generalizes the notion of inverse.

</div>

Introducing the pseudoinverse unifies the least squares of the previous section and the minimum norm of this section into a single formula. When $$A$$ has full column rank, $$x=A^+y=(A^tA)^{-1}A^ty$$ is the unique least-squares solution minimizing $$\lVert Ax-y\rVert$$, and when $$A$$ has full row rank, $$x=A^+y=A^t(AA^t)^{-1}y$$ is the minimum-norm solution of $$Ax=y$$. For a general matrix as well, $$x=A^+y$$ gives the unique solution of minimum norm among those minimizing $$\lVert Ax-y\rVert$$, and thus the problems treated separately in the two sections are naturally unified into the single object of the pseudoinverse.
