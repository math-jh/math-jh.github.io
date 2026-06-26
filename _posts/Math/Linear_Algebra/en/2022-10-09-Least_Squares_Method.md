---
title: "Least Squares Method"
description: "We derive the least squares method via normal equations in Euclidean and inner product spaces, and cover line fitting for planar points and the pseudoinverse."
excerpt: "Orthogonal projections and least squares"

categories: [Math / Linear Algebra]
permalink: /en/math/linear_algebra/least_squares_method
sidebar: 
    nav: "linear_algebra-en"


date: 2022-10-09

weight: 119
translated_at: 2026-06-26T20:30:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-26T20:30:02+00:00
---
## Least Squares Method

The method of least squares we introduce now is first considered for Euclidean spaces $$\mathbb{R}^n$$ with the dot product defined on them. However, as was done in [§Bilinear Forms, §§Non-degenerate Bilinear Forms](/en/math/linear_algebra/bilinear_form#비퇴화-쌍선형형식), this can be generalized to an arbitrary $$\mathbb{R}$$-inner product space in the same way.

Consider an arbitrary matrix $$A\in\Mat_{m\times n}(\mathbb{R})$$ and the system of linear equations $$Ax=y$$. If $$m=n$$ and $$A$$ is invertible, this equation has a unique solution, but this is not the case in general. In particular, consider the case where $$m>n$$. Then since $$\rank(A)\leq n< m$$, for most $$y$$—excluding those vectors lying in the image of $$A$$—this equation cannot be solved.

A typical example is finding an appropriate function that represents given data. Of course, using Lagrange interpolation we can choose a suitable basis and find an $$n$$-th degree function approximating the given $$n+1$$ data points, but if we try to find a linear function representing this data, we cannot find an exact solution unless all the given $$n+1$$ points lie on a single straight line.

We project an arbitrary given vector $$y$$ onto $$\im A$$, and then solve the equation $$Ax=\hat y$$ for this vector $$\hat y=\proj_{\im(A)}y$$. However, from the previous post we know that $$y-\hat y\in (\im A)^\perp$$, so we know that

$$\langle y-\hat y, v\rangle=0\qquad\text{for all $v\in \im A$}$$

holds. Therefore we obtain the following equation:

$$\langle y-\hat y, Au\rangle=0\qquad\text{for all $u\in \mathbb{R}^n$}$$

Now moving $$A$$ to the left gives

$$\langle A^t(y-\hat y), u\rangle=0\qquad\text{for all $u\in\mathbb{R}^n$}$$

and since $$\langle-,-\rangle$$ is non-degenerate, we know that $$A^t(y-\hat y)=0$$. Now since $$\hat y=Ax$$, we obtain the equation

$$A^tAx=A^ty$$

This process can be summarized as follows.

<div class="proposition" markdown="1">

<ins id="prop1">**Proposition 1**</ins> For an arbitrary matrix $$A\in\Mat_{m\times n}(\mathbb{R})$$ and $$y\in\mathbb{R}^m$$, a vector $$x\in\mathbb{R}^n$$ minimizes the value of the real number $$\lVert Au-y\rVert$$ if and only if the following equation holds:

$$A^tAx=A^ty$$

</div>

The example discussed in the introduction can be solved in the following way.

<div class="example" markdown="1">

<ins id="ex2">**Example 2**</ins> Suppose three points $$(0,1)$$, $$(1,3)$$, $$(2,4)$$ are given in the plane, and consider the problem of finding the straight line $$y=ax+b$$ that best fits these points. If all three points lie on a single straight line, then the system of equations in the unknowns $$a,b$$

$$\begin{aligned}a\cdot 0+b&=1\\ a\cdot 1+b&=3\\ a\cdot 2+b&=4\end{aligned}$$

must have a solution, but since the three points are not collinear, no exact solution exists. Writing this system of equations in the form $$Ax=y$$, we have

$$A=\begin{pmatrix}0&1\\ 1&1\\ 2&1\end{pmatrix},\qquad x=\begin{pmatrix}a\\ b\end{pmatrix},\qquad y=\begin{pmatrix}1\\ 3\\ 4\end{pmatrix}$$

where the first column of $$A$$ contains the $$x$$-coordinates of each point, and the second column contains the constant $$1$$. By [Proposition 1](#prop1), the pair $$(a,b)$$ that minimizes $$\lVert Ax-y\rVert$$ is given as the solution of the normal equation

$$A^tAx=A^ty$$

Direct computation gives

$$A^tA=\begin{pmatrix}5&3\\ 3&3\end{pmatrix},\qquad A^ty=\begin{pmatrix}11\\ 8\end{pmatrix}$$

and since $$\det(A^tA)=5\cdot 3-3\cdot 3=6\neq 0$$, the matrix $$A^tA$$ is invertible. Therefore we obtain

$$\begin{pmatrix}a\\ b\end{pmatrix}=(A^tA)^{-1}A^ty=\frac{1}{6}\begin{pmatrix}3&-3\\ -3&5\end{pmatrix}\begin{pmatrix}11\\ 8\end{pmatrix}=\frac{1}{6}\begin{pmatrix}9\\ 7\end{pmatrix}=\begin{pmatrix}3/2\\ 7/6\end{pmatrix}$$

That is, the straight line that best represents the given three points in the least-squares sense is $$y=\frac{3}{2}x+\frac{7}{6}$$.

![linear least squares fit](/assets/images/Math/Linear_Algebra/Least_Squares_Method-1.svg){:style="width:11.95em" class="invert" .align-center}

</div>

More generally, even if we choose the inner product $$\langle-,-\rangle$$ to be the $$L^2$$-inner product on a space of functions instead of the dot product, we can repeat similar examples.

What was essentially used in [Example 2](#ex2) is only the fact that the function to be found is linear in the unknown coefficients. That is, as long as the model we wish to use is of the form of a linear combination $$c_1f_1+\cdots+c_kf_k$$ of previously chosen functions $$f_1,\ldots, f_k$$, we can construct a matrix $$A$$ whose $$(i,j)$$-entry is the value of $$f_j$$ at the $$i$$-th data point and solve the same normal equation to obtain the coefficients $$c_j$$. In particular, [Example 2](#ex2) was the case with $$f_1(t)=t$$, $$f_2(t)=1$$, and the same method applies directly to the case of general polynomial functions as well.

<div class="example" markdown="1">

<ins id="ex3">**Example 3**</ins> Consider the problem of finding the quadratic function $$y=a\x^2+b\x+c$$ that best represents the four points $$(-2,5)$$, $$(-1,2)$$, $$(1,1)$$, $$(2,4)$$ in the plane. Stacking the values of $$(\x^2,\x,1)$$ at each point as rows gives

$$A=\begin{pmatrix}4&-2&1\\ 1&-1&1\\ 1&1&1\\ 4&2&1\end{pmatrix},\qquad x=\begin{pmatrix}a\\ b\\ c\end{pmatrix},\qquad y=\begin{pmatrix}5\\ 2\\ 1\\ 4\end{pmatrix}$$

Direct computation gives

$$A^tA=\begin{pmatrix}34&0&10\\ 0&10&0\\ 10&0&4\end{pmatrix},\qquad A^ty=\begin{pmatrix}39\\ -3\\ 12\end{pmatrix}$$

The second row separates to give $$10b=-3$$, i.e., $$b=-\frac{3}{10}$$ immediately, and the remaining two unknowns are found by solving

$$\begin{pmatrix}34&10\\ 10&4\end{pmatrix}\begin{pmatrix}a\\ c\end{pmatrix}=\begin{pmatrix}39\\ 12\end{pmatrix}$$

The determinant of this coefficient matrix is $$34\cdot 4-10\cdot 10=36$$, so it is invertible, and solving gives $$a=1$$, $$c=\frac{1}{2}$$. Therefore the parabola that best represents these four points in the least-squares sense is $$y=\x^2-\frac{3}{10}\x+\frac{1}{2}$$.

![quadratic least squares fit](/assets/images/Math/Linear_Algebra/Least_Squares_Method-2.svg){:style="width:19.74em" class="invert" .align-center}

</div>

Looking back at the derivation of [Proposition 1](#prop1), the $$Ax$$ produced by the least-squares solution $$x$$ was exactly equal to the vector $$\proj_{\im A}y$$ obtained by projecting $$y$$ onto $$\im A$$, and this was the starting point that led to the equation $$A^tAx=A^ty$$. That is, the approximation $$\hat y=Ax$$ is the foot of the perpendicular from $$y$$ to $$\im A$$, and the error $$y-\hat y$$ is perpendicular to $$\im A$$. In particular, if $$A$$ has full column rank so that $$A^tA$$ is invertible, then $$x=(A^tA)^{-1}A^ty$$, so the approximation is given by

$$\hat y=A(A^tA)^{-1}A^ty$$

The matrix $$P=A(A^tA)^{-1}A^t$$ appearing here represents the orthogonal projection onto $$\im A$$.

<div class="example" markdown="1">

<ins id="ex4">**Example 4**</ins> Returning to [Example 2](#ex2), let us compute the error with respect to the approximating function directly. Since $$x=(\tfrac{3}{2},\tfrac{7}{6})$$, we have

$$\hat y=Ax=\begin{pmatrix}0&1\\ 1&1\\ 2&1\end{pmatrix}\begin{pmatrix}3/2\\ 7/6\end{pmatrix}=\begin{pmatrix}7/6\\ 8/3\\ 25/6\end{pmatrix}$$

and therefore the error is

$$y-\hat y=\begin{pmatrix}1\\ 3\\ 4\end{pmatrix}-\begin{pmatrix}7/6\\ 8/3\\ 25/6\end{pmatrix}=\begin{pmatrix}-1/6\\ 1/3\\ -1/6\end{pmatrix}$$

Taking the inner product of this error with each of the two columns $$(0,1,2)$$ and $$(1,1,1)$$ of $$A$$ gives

$$0\cdot\left(-\tfrac{1}{6}\right)+1\cdot\tfrac{1}{3}+2\cdot\left(-\tfrac{1}{6}\right)=0,\qquad -\tfrac{1}{6}+\tfrac{1}{3}-\tfrac{1}{6}=0$$

so we can verify that the error is perpendicular to $$\im A$$. At this time, the error is $$\lVert y-\hat y\rVert^2=\frac{1}{36}(1+4+1)=\frac{1}{6}$$, which quantitatively represents the degree to which the given three points fail to be collinear.

</div>

## Pseudoinverse

Now we consider the opposite case: a matrix $$A\in\Mat_{m\times n}(\mathbb{R})$$ with $$m< n$$.

First, suppose arbitrary $$A\in\Mat_{m\times n}(\mathbb{R})$$ and $$y\in\im(A)$$ are given, and assume $$A$$ is not injective. Then there exist non-zero vectors $$u$$ satisfying $$Au=0$$, and therefore if a vector $$x$$ satisfying $$Ax=y$$ is given, we can see that the $$x+u$$ are also solutions. Now let us find among these the solution with the smallest norm and call it the *minimum-norm solution*. That is, the entire set of solutions of $$Ax=y$$ forms $$x_0+\ker A$$ for a particular solution $$x_0$$, and we seek the point on this affine subspace that minimizes the norm.

This is exactly the situation treated by the projection theorem in [§Inner Product Spaces, ⁋Theorem 9](/en/math/linear_algebra/inner_product_spaces#thm9). The point that minimizes the distance from the origin to the affine subspace $$x_0+\ker A$$ is unique, and the vector drawn from this point to the affine subspace is perpendicular to $$\ker A$$. Therefore the minimum-norm solution is the unique solution lying in $$(\ker A)^\perp$$. On the other hand, by [§Bilinear Forms, ⁋Proposition 5](/en/math/linear_algebra/bilinear_form#prop5), we have $$(\ker A)^\perp=\im A^t$$. This can be summarized as follows.

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> For an arbitrary matrix $$A\in\Mat_{m\times n}(\mathbb{R})$$ and $$y\in\im A$$, among the solutions of the equation $$Ax=y$$ there exists a unique solution that minimizes the norm, and this is the unique solution belonging to $$\im A^t$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Since $$y\in\im A$$, there exists $$x_0$$ satisfying $$Ax_0=y$$, and the entire set of solutions of $$Ax=y$$ is $$x_0+\ker A$$. By [§Bilinear Forms, ⁋Proposition 5](/en/math/linear_algebra/bilinear_form#prop5),

$$\mathbb{R}^n=\ker A\oplus(\ker A)^\perp$$

holds, so we can decompose $$x_0$$ as $$x_0=p+q$$. Here $$p\in (\ker A)^\perp$$ and $$q\in\ker A$$. Then $$p=x_0-q$$ is also a solution of $$Ax=y$$, and for any solution $$x=p+u$$ (where $$u\in\ker A$$), since $$p\perp u$$, by the Pythagorean theorem

$$\lVert x\rVert^2=\lVert p\rVert^2+\lVert u\rVert^2\geq \lVert p\rVert^2$$

holds. Equality holds only when $$u=0$$, i.e., $$x=p$$, so the solution minimizing the norm is unique and equals $$p$$. Also, by the same proposition $$(\ker A)^\perp=\im A^t$$, so $$p\in\im A^t$$.

</details>

Now let us consider the case where we can construct this minimum-norm solution explicitly. If $$A$$ is of *full row rank*, i.e., $$\rank A=m$$, then $$\im A=\mathbb{R}^m$$, so $$Ax=y$$ has a solution for all $$y\in\mathbb{R}^m$$, and by the above proposition the minimum-norm solution is uniquely determined on $$\im A^t$$.

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6**</ins> If a matrix $$A\in\Mat_{m\times n}(\mathbb{R})$$ satisfies $$\rank A=m$$, then $$AA^t\in\Mat_m(\mathbb{R})$$ is invertible, and for any $$y\in\mathbb{R}^m$$ the minimum-norm solution of the equation $$Ax=y$$ is given by

$$x=A^t(AA^t)^{-1}y$$

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First we show that $$AA^t$$ is invertible. Since $$AA^t$$ is an $$m\times m$$ square matrix, it suffices to show that $$AA^tz=0$$ has only the solution $$z=0$$. If $$AA^tz=0$$, then

$$\lVert A^tz\rVert^2=\langle A^tz, A^tz\rangle=\langle z, AA^tz\rangle=0$$

so $$A^tz=0$$, i.e., $$z\in\ker A^t$$. However, since $$\rank A^t=\rank A=m$$, the map $$A^t$$ is injective, and therefore $$z=0$$. This shows that $$AA^t$$ is invertible.

Now setting $$x=A^t(AA^t)^{-1}y$$, we have

$$Ax=AA^t(AA^t)^{-1}y=y$$

so $$x$$ is a solution of $$Ax=y$$. Moreover, since $$x=A^t\big((AA^t)^{-1}y\big)\in\im A^t$$, by [Proposition 5](#prop5) the vector $$x$$ is the minimum-norm solution.

</details>

As seen in the proof, from the fact that the minimum-norm solution lies on $$\im A^t$$ we can assume the form $$x=A^tz$$, substitute this into $$Ax=y$$, and solve $$AA^tz=y$$ to obtain $$z=(AA^t)^{-1}y$$. Then $$A^t(AA^t)^{-1}$$ becomes a *right inverse* of $$A$$, i.e., a matrix satisfying $$A\cdot A^t(AA^t)^{-1}=I_m$$.

The case of least squares treated in the previous section and the case of minimum norm treated in this section can be viewed as dual situations. When $$A$$ is of *full column rank*, i.e., $$\rank A=n$$, the matrix $$A^tA$$ becomes invertible and the normal equation of [Proposition 1](#prop1) gives the unique least-squares solution $$x=(A^tA)^{-1}A^ty$$, and then $$(A^tA)^{-1}A^t$$ becomes a left inverse of $$A$$. On the other hand, when $$A$$ is of full row rank, the right inverse $$A^t(AA^t)^{-1}$$ gives the minimum-norm solution as above. The following concept unifies these two matrices.

<div class="definition" markdown="1">

<ins id="def7">**Definition 7**</ins> For a matrix $$A\in\Mat_{m\times n}(\mathbb{R})$$, if $$A$$ has full column rank we define

$$A^\dagger:=(A^tA)^{-1}A^t$$

and if $$A$$ has full row rank we define

$$A^\dagger:=A^t(AA^t)^{-1}$$

The matrix $$A^\dagger\in\Mat_{n\times m}(\mathbb{R})$$ defined in this way is called the *Moore-Penrose pseudoinverse* of $$A$$.

</div>

The two formulas above cannot be used directly in the general situation without the rank assumption on $$A$$, because at least one of $$A^tA$$ or $$AA^t$$ is not invertible. The pseudoinverse for a general matrix is defined using singular value decomposition, and when $$A$$ falls into one of the two cases above, this definition coincides with the formulas above. It is known that $$A^\dagger$$ is then uniquely characterized by the following four conditions:

$$AA^\dagger A=A,\quad A^\dagger AA^\dagger=A^\dagger,\quad (AA^\dagger)^t=AA^\dagger,\quad (A^\dagger A)^t=A^\dagger A$$

and through this we can verify that $$A^\dagger$$ is well-defined by $$A$$.

<div class="remark" markdown="1">

<ins id="rmk8">**Remark 8**</ins> If $$A$$ is an invertible square matrix, then $$A^\dagger=A^{-1}$$ holds. This is because both $$A^tA$$ and $$AA^t$$ are invertible, so $$A^\dagger=(A^tA)^{-1}A^t=A^{-1}(A^t)^{-1}A^t=A^{-1}$$. In this sense, the pseudoinverse generalizes the notion of an inverse.

</div>

With the introduction of the pseudoinverse, the least squares of the previous section and the minimum norm of this section are unified into a single formula. When $$A$$ has full column rank, $$x=A^\dagger y=(A^tA)^{-1}A^ty$$ is the unique least-squares solution minimizing $$\lVert Ax-y\rVert$$, and when $$A$$ has full row rank, $$x=A^\dagger y=A^t(AA^t)^{-1}y$$ is the minimum-norm solution of $$Ax=y$$. Even for a general matrix, $$x=A^\dagger y$$ gives the unique solution among those minimizing $$\lVert Ax-y\rVert$$ that again has minimum norm, and thus the problems treated separately in the two sections are naturally unified into a single object called the pseudoinverse.
