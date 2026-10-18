---
title: "Singular Value Decomposition"
description: "For an arbitrary real matrix, singular values are defined via the spectral decomposition of the product with its transpose. The singular value decomposition is then constructed as a product of orthogonal and diagonal matrices, and this leads to the definition of a general pseudoinverse."
excerpt: "Orthogonal decomposition of arbitrary real matrices"

categories: [Math / Linear Algebra]
permalink: /en/math/linear_algebra/singular_value_decomposition
sidebar: 
    nav: "linear_algebra-en"


date: 2026-06-27

weight: 26
translated_at: 2026-06-27T20:00:01+00:00
translation_source: kimi-cli
last_polished_at: 2026-10-18T15:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
The tools we have discussed so far all apply to $n\times n$ matrices, i.e., linear operators. Since a general $m\times n$ matrix is not square, we cannot directly speak of eigenvalues or diagonalization. In this post, we cover the singular value decomposition, which decomposes an arbitrary real matrix into a product of two orthogonal matrices and one diagonal matrix. The starting point is the observation that for any $A$, the matrix $A^tA$ is always a real symmetric matrix, so the spectral theorem applies.

## Singular Value Decomposition

::: Proposition 1
For any matrix $A\in\Mat_{m\times n}(\mathbb{R})$, the matrix $A^tA\in\Mat_n(\mathbb{R})$ is a positive semidefinite self-adjoint operator. In particular, all eigenvalues of $A^tA$ are real numbers greater than or equal to $0$.
:::
::: Proof
Since $(A^tA)^t=A^t(A^t)^t=A^tA$, the matrix $A^tA$ is a symmetric matrix, i.e., a self-adjoint operator on $\mathbb{R}^n$. Moreover, for any $v\in\mathbb{R}^n$,

$$\langle A^tAv,v\rangle=\langle Av,Av\rangle=\lVert Av\rVert^2\geq 0$$

so $A^tA$ is positive semidefinite. ([§Spectral Theorem, ⁋Definition 8](/en/math/linear_algebra/spectral_theorem#def8){: data-lid="ultrl" }) Therefore, by [§Spectral Theorem, ⁋Proposition 9](/en/math/linear_algebra/spectral_theorem#prop9){: data-lid="zkvp6" }, all eigenvalues of $A^tA$ are greater than or equal to $0$.
:::

Since all eigenvalues of the matrix $A^tA$ are non-negative, we can take their square roots.

::: Definition 2
For a matrix $A\in\Mat_{m\times n}(\mathbb{R})$, when we write the eigenvalues of $A^tA$, counted with multiplicity, as $\sigma_1^2\geq\sigma_2^2\geq\cdots\geq\sigma_n^2\geq 0$, the non-negative real numbers $\sigma_i=\sqrt{\sigma_i^2}$ are called the *singular values* of $A$.
:::

Our main claim is then as follows.

::: Theorem 3 (Singular Value Decomposition)
For any matrix $A\in\Mat_{m\times n}(\mathbb{R})$, there exist orthogonal matrices $U\in\Mat_m(\mathbb{R})$, $V\in\Mat_n(\mathbb{R})$, and, with $(i,i)$-entry being the singular value $\sigma_i$ of $A$ and the remaining entries being $0$, an $m\times n$ diagonal matrix $\Sigma$ such that 

$$A=U\Sigma V^t$$

holds.
:::
::: Proof
By [Proposition 1](#prop1){: data-lid="aqnpm" }, $A^tA$ is self-adjoint, so by [§Spectral Theorem, ⁋Theorem 5](/en/math/linear_algebra/spectral_theorem#thm5){: data-lid="faehg" }, there exists, consisting of eigenvectors of $A^tA$, an orthonormal basis of $\mathbb{R}^n$, $\{v_1,\ldots, v_n\}$. Order the eigenvalues as $\sigma_1^2\geq\cdots\geq\sigma_n^2\geq 0$, and suppose $\sigma_1,\ldots,\sigma_r$ are positive and $\sigma_{r+1}=\cdots=\sigma_n=0$. That is, $A^tAv_i=\sigma_i^2v_i$.

For each $1\leq i\leq r$, define

$$u_i=\frac{1}{\sigma_i}Av_i\in\mathbb{R}^m$$

Then for $1\leq i,j\leq r$,

$$\langle u_i,u_j\rangle=\frac{1}{\sigma_i\sigma_j}\langle Av_i,Av_j\rangle=\frac{1}{\sigma_i\sigma_j}\langle A^tAv_i,v_j\rangle=\frac{\sigma_i^2}{\sigma_i\sigma_j}\langle v_i,v_j\rangle=\frac{\sigma_i}{\sigma_j}\delta_{ij}=\delta_{ij}$$

so $\{u_1,\ldots, u_r\}$ is an orthonormal set in $\mathbb{R}^m$. Extending this, we can obtain an orthonormal basis of $\mathbb{R}^m$, $\{u_1,\ldots, u_m\}$. ([§Dimension of Vector Spaces, ⁋Proposition 5](/en/math/linear_algebra/dimension#prop5){: data-lid="8ff95" }, [§Inner Product Spaces, §§Orthonormal Bases](/en/math/linear_algebra/inner_product_spaces#orthonormal-bases){: data-lid="4wm8i" }) 

On the other hand, for $r<i\leq n$,

$$\lVert Av_i\rVert^2=\langle Av_i,Av_i\rangle=\langle A^tAv_i,v_i\rangle=\sigma_i^2\langle v_i,v_i\rangle=0$$

so $Av_i=0$. Now, defining the matrix with columns $u_i$ as $U=(u_1\mid\cdots\mid u_m)$ and the matrix with columns $v_i$ as $V=(v_1\mid\cdots\mid v_n)$, both matrices are orthogonal matrices since their columns are orthonormal. Let $\Sigma$ be the matrix whose $(i,i)$-entry is $\sigma_i$ ($1\leq i\leq r$) and remaining entries are $0$, an $m\times n$ diagonal matrix. When comparing the columns of $AV$ and $U\Sigma$ at column $i$, for $1\leq i\leq r$ we have

$$Av_i=\sigma_iu_i$$

and for $U\Sigma$, the $i$-th column is also $\sigma_iu_i$, while for $i>r$, we have $Av_i=0$, and since in $\Sigma$ the $i$-th column is $0$, in $U\Sigma$ the $i$-th column is also $0$. Therefore $AV=U\Sigma$, and since $V$ is orthogonal, multiplying both sides on the right by $V^t=V^{-1}$ yields $A=U\Sigma V^t$.
:::

The singular value decomposition re-expresses the rank of a matrix in the language of singular values. 

::: Corollary 4
The rank of a matrix $A\in\Mat_{m\times n}(\mathbb{R})$ equals the number of non-$0$ singular values.
:::
::: Proof
In $A=U\Sigma V^t$, since $U,V$ are invertible, $\rank A=\rank\Sigma$. The entries of $\Sigma$ other than $0$ are only the positive singular values $\sigma_1,\ldots,\sigma_r$, and since these lie in distinct rows and columns, the columns of $\Sigma$ other than $0$ are exactly $r$ in number and are linearly independent. Therefore $\rank A=r$.
:::

## General Pseudoinverse

In [§Least Squares Method, ⁋Definition 7](/en/math/linear_algebra/least_squares_method#def7){: data-lid="fimxb" }, we defined the pseudoinverse when $A$ has full column rank or full row rank, and we announced that the definition in the general case would use the singular value decomposition. We now present that definition. 

::: Definition 5
For a matrix $A\in\Mat_{m\times n}(\mathbb{R})$, let a singular value decomposition $A=U\Sigma V^t$ be given. For $\Sigma$, with respect to its positive singular values $\sigma_i$, let the matrix whose $(i,i)$-entry is $1/\sigma_i$ and remaining entries are $0$, an $n\times m$ diagonal matrix, be $\Sigma^+$. Then we define the *Moore-Penrose pseudoinverse* of $A$ as

$$A^+=V\Sigma^+U^t$$
:::

For this to make sense, we must verify that the definition does not depend on the choice of singular value decomposition. This follows from the next proposition.

::: Proposition 6
The matrix $A^+$ of [Definition 5](#def5){: data-lid="n9ovz" } satisfies all four conditions

$$AA^+A=A,\quad A^+AA^+=A^+,\quad (AA^+)^t=AA^+,\quad (A^+A)^t=A^+A$$
:::
::: Proof
$\Sigma\Sigma^+$ is the $m\times m$ diagonal matrix whose $(i,i)$-entry is $1$ for $1\leq i\leq r$ and $0$ otherwise, and $\Sigma^+\Sigma$ is the $n\times n$ diagonal matrix defined in the same way. Both are symmetric, and one can verify directly entrywise that $\Sigma\Sigma^+\Sigma=\Sigma$ and $\Sigma^+\Sigma\Sigma^+=\Sigma^+$. Now using $A=U\Sigma V^t$, $A^+=V\Sigma^+U^t$, and $U^tU=I$, $V^tV=I$, we have

$$AA^+=U\Sigma V^tV\Sigma^+U^t=U(\Sigma\Sigma^+)U^t,\qquad A^+A=V(\Sigma^+\Sigma)V^t$$

Since $\Sigma\Sigma^+$ and $\Sigma^+\Sigma$ are symmetric, $AA^+$ and $A^+A$ are also symmetric, which establishes the third and fourth conditions. Moreover,

$$AA^+A=U(\Sigma\Sigma^+)U^tU\Sigma V^t=U(\Sigma\Sigma^+\Sigma)V^t=U\Sigma V^t=A$$

and similarly

$$A^+AA^+=V(\Sigma^+\Sigma)V^tV\Sigma^+U^t=V(\Sigma^+\Sigma\Sigma^+)U^t=V\Sigma^+U^t=A^+$$

so the first and second conditions also hold.
:::

Now, since we saw in [§Least Squares Method, ⁋Definition 7](/en/math/linear_algebra/least_squares_method#def7){: data-lid="j55ph" } that the above four conditions uniquely determine $A^+$, not only is $A^+$ of [Definition 5](#def5){: data-lid="a6ok6" } well defined independently of the choice of singular value decomposition, but we also know that the two definitions agree in the full-rank case. For example, if $A$ has full column rank, then $A^tA$ is invertible, and one can verify directly from

$$\bigl((A^tA)^{-1}A^t\bigr)A=I_n,\qquad A\bigl((A^tA)^{-1}A^t\bigr)=A(A^tA)^{-1}A^t$$

that the matrix $(A^tA)^{-1}A^t$ satisfies all four conditions above. Here, since $A^tA$ is symmetric, $\bigl((A^tA)^{-1}\bigr)^t=(A^tA)^{-1}$, and thus $A(A^tA)^{-1}A^t$ is also symmetric.

Geometrically, the singular value decomposition $A=U\Sigma V^t$ means that an arbitrary linear map $A$ decomposes as a composition of a rotation or reflection with respect to an orthonormal basis, a scaling by $\sigma_i$ along each axis, and another rotation or reflection. The columns $v_i$ of $V$ are called the *right singular vectors*, and the columns $u_i$ of $U$ are called the *left singular vectors*; these are the eigenvectors of $A^tA$ and $AA^t$, respectively.

---

**References**

**[Goc]** M.S. Gockenbach, *Finite-dimensional linear algebra*, Discrete Mathematics and its applications, Taylor&Francis, 2011.  

---
