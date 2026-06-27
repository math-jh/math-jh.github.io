---
title: "Singular Value Decomposition"
description: "For an arbitrary real matrix, singular values are defined via the spectral decomposition of the product with its transpose. The singular value decomposition is then constructed as a product of orthogonal and diagonal matrices, and this leads to the definition of a general Moore-Penrose pseudoinverse."
excerpt: "Orthogonal decomposition of arbitrary real matrices"

categories: [Math / Linear Algebra]
permalink: /en/math/linear_algebra/singular_value_decomposition
sidebar: 
    nav: "linear_algebra-en"


date: 2026-06-27

weight: 123
translated_at: 2026-06-27T20:00:01+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-27T20:00:01+00:00
---
The tools discussed so far all apply to $$n\times n$$ matrices, i.e., linear operators. A general $$m\times n$$ matrix is not square, so we cannot directly speak of eigenvalues or diagonalization. In this post, we cover the singular value decomposition, which decomposes an arbitrary rectangular matrix into a product of two orthogonal matrices and one diagonal matrix. The starting point is the observation that for any $$A$$, the matrix $$A^tA$$ is always a real symmetric matrix, so the spectral theorem applies.

## Singular Value Decomposition

<div class="proposition" markdown="1">

<ins id="prop1">**Proposition 1**</ins> For any matrix $$A\in\Mat_{m\times n}(\mathbb{R})$$, the matrix $$A^tA\in\Mat_n(\mathbb{R})$$ is a positive semidefinite self-adjoint operator. In particular, all eigenvalues of $$A^tA$$ are non-negative real numbers.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Since $$(A^tA)^t=A^t(A^t)^t=A^tA$$, the matrix $$A^tA$$ is symmetric, i.e., a self-adjoint operator on $$\mathbb{R}^n$$. Moreover, for any $$v\in\mathbb{R}^n$$,

$$\langle A^tAv,v\rangle=\langle Av,Av\rangle=\lVert Av\rVert^2\geq 0$$

so $$A^tA$$ is positive semidefinite. ([§Spectral Theorem, ⁋Definition 8](/en/math/linear_algebra/spectral_theorem#def8)) Therefore, by [§Spectral Theorem, ⁋Proposition 9](/en/math/linear_algebra/spectral_theorem#prop9), all eigenvalues of $$A^tA$$ are non-negative.

</details>

Since all eigenvalues of the matrix $$A^tA$$ are non-negative, we can take their square roots.

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> For a matrix $$A\in\Mat_{m\times n}(\mathbb{R})$$, write the eigenvalues of $$A^tA$$, counted with multiplicity, as $$\sigma_1^2\geq\sigma_2^2\geq\cdots\geq\sigma_n^2\geq 0$$. The non-negative real numbers $$\sigma_i=\sqrt{\sigma_i^2}$$ are called the *singular values* of $$A$$.

</div>

Our main claim is then as follows.

<div class="proposition" markdown="1">

<ins id="thm3">**Theorem 3 (Singular Value Decomposition)**</ins> For any matrix $$A\in\Mat_{m\times n}(\mathbb{R})$$, there exist orthogonal matrices $$U\in\Mat_m(\mathbb{R})$$ and $$V\in\Mat_n(\mathbb{R})$$, and an $$m\times n$$ diagonal matrix $$\Sigma$$ whose $$(i,i)$$-entry is the singular value $$\sigma_i$$ of $$A$$ and whose remaining entries are $$0$$, such that

$$A=U\Sigma V^t$$

holds.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

By [Proposition 1](#prop1), $$A^tA$$ is self-adjoint, so by [§Spectral Theorem, ⁋Theorem 5](/en/math/linear_algebra/spectral_theorem#thm5) there exists an orthonormal basis $$\{v_1,\ldots, v_n\}$$ of $$\mathbb{R}^n$$ consisting of eigenvectors of $$A^tA$$. Order the eigenvalues as $$\sigma_1^2\geq\cdots\geq\sigma_n^2\geq 0$$, and suppose $$\sigma_1,\ldots,\sigma_r$$ are positive and $$\sigma_{r+1}=\cdots=\sigma_n=0$$. That is, $$A^tAv_i=\sigma_i^2v_i$$.

For each $$1\leq i\leq r$$, define

$$u_i=\frac{1}{\sigma_i}Av_i\in\mathbb{R}^m$$

Then for $$1\leq i,j\leq r$$,

$$\langle u_i,u_j\rangle=\frac{1}{\sigma_i\sigma_j}\langle Av_i,Av_j\rangle=\frac{1}{\sigma_i\sigma_j}\langle A^tAv_i,v_j\rangle=\frac{\sigma_i^2}{\sigma_i\sigma_j}\langle v_i,v_j\rangle=\frac{\sigma_i}{\sigma_j}\delta_{ij}=\delta_{ij}$$

so $$\{u_1,\ldots, u_r\}$$ is an orthonormal set in $$\mathbb{R}^m$$. We can extend this to obtain an orthonormal basis $$\{u_1,\ldots, u_m\}$$ of $$\mathbb{R}^m$$. ([§Inner Product Spaces, §§Orthonormal Basis](/en/math/linear_algebra/inner_product_spaces#정규직교기저))

On the other hand, for $$r<i\leq n$$,

$$\lVert Av_i\rVert^2=\langle Av_i,Av_i\rangle=\langle A^tAv_i,v_i\rangle=\sigma_i^2\langle v_i,v_i\rangle=0$$

so $$Av_i=0$$. Now define $$U=(u_1\mid\cdots\mid u_m)$$ with columns $$u_i$$ and $$V=(v_1\mid\cdots\mid v_n)$$ with columns $$v_i$$. Both matrices are orthogonal since their columns are orthonormal. Let $$\Sigma$$ be the $$m\times n$$ diagonal matrix whose $$(i,i)$$-entry is $$\sigma_i$$ ($$1\leq i\leq r$$) and whose remaining entries are $$0$$. Comparing the $$i$$-th columns of $$AV$$ and $$U\Sigma$$, for $$1\leq i\leq r$$ we have

$$Av_i=\sigma_iu_i$$

and the $$i$$-th column of $$U\Sigma$$ is also $$\sigma_iu_i$$, while for $$i>r$$ we have $$Av_i=0$$ and the $$i$$-th column of $$\Sigma$$ is $$0$$, so the $$i$$-th column of $$U\Sigma$$ is also $$0$$. Therefore $$AV=U\Sigma$$, and since $$V$$ is orthogonal, multiplying both sides on the right by $$V^t=V^{-1}$$ yields $$A=U\Sigma V^t$$.

</details>

The singular value decomposition re-expresses the rank of a matrix in the language of singular values.

<div class="proposition" markdown="1">

<ins id="cor4">**Corollary 4**</ins> The rank of a matrix $$A\in\Mat_{m\times n}(\mathbb{R})$$ equals the number of non-zero singular values.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

In $$A=U\Sigma V^t$$, the matrices $$U$$ and $$V$$ are invertible, so $$\rank A=\rank\Sigma$$. The non-zero entries of $$\Sigma$$ are precisely the positive singular values $$\sigma_1,\ldots,\sigma_r$$, and these lie in distinct rows and columns, so the non-zero columns of $$\Sigma$$ are exactly $$r$$ in number and are linearly independent. Therefore $$\rank A=r$$.

</details>

## General Pseudoinverse

In [§Least Squares Method, ⁋Definition 7](/en/math/linear_algebra/least_squares_method#def7), we defined the pseudoinverse when $$A$$ has full column rank or full row rank, and we announced that the definition in the general case would use the singular value decomposition. We now present that definition.

<div class="definition" markdown="1">

<ins id="def5">**Definition 5**</ins> Let a singular value decomposition $$A=U\Sigma V^t$$ of a matrix $$A\in\Mat_{m\times n}(\mathbb{R})$$ be given. For the positive singular values $$\sigma_i$$ of $$\Sigma$$, let $$\Sigma^+$$ be the $$n\times m$$ diagonal matrix whose $$(i,i)$$-entry is $$1/\sigma_i$$ and whose remaining entries are $$0$$. Then we define the *Moore–Penrose pseudoinverse* of $$A$$ as

$$A^+=V\Sigma^+U^t$$

</div>

For this to make sense, we must verify that the definition does not depend on the choice of singular value decomposition. This follows from the next proposition.

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6**</ins> The matrix $$A^+$$ of [Definition 5](#def5) satisfies all four conditions

$$AA^+A=A,\quad A^+AA^+=A^+,\quad (AA^+)^t=AA^+,\quad (A^+A)^t=A^+A$$

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

$$\Sigma\Sigma^+$$ is the $$m\times m$$ diagonal matrix whose $$(i,i)$$-entry is $$1$$ for $$1\leq i\leq r$$ and $$0$$ otherwise, and $$\Sigma^+\Sigma$$ is the $$n\times n$$ diagonal matrix defined in the same way. Both are symmetric, and one can verify directly entrywise that $$\Sigma\Sigma^+\Sigma=\Sigma$$ and $$\Sigma^+\Sigma\Sigma^+=\Sigma^+$$. Now using $$A=U\Sigma V^t$$, $$A^+=V\Sigma^+U^t$$, and $$U^tU=I$$, $$V^tV=I$$, we have

$$AA^+=U\Sigma V^tV\Sigma^+U^t=U(\Sigma\Sigma^+)U^t,\qquad A^+A=V(\Sigma^+\Sigma)V^t$$

Since $$\Sigma\Sigma^+$$ and $$\Sigma^+\Sigma$$ are symmetric, $$AA^+$$ and $$A^+A$$ are also symmetric, which establishes the third and fourth conditions. Moreover,

$$AA^+A=U(\Sigma\Sigma^+)U^tU\Sigma V^t=U(\Sigma\Sigma^+\Sigma)V^t=U\Sigma V^t=A$$

and similarly

$$A^+AA^+=V(\Sigma^+\Sigma)V^tV\Sigma^+U^t=V(\Sigma^+\Sigma\Sigma^+)U^t=V\Sigma^+U^t=A^+$$

so the first and second conditions also hold.

</details>

Now, in [§Least Squares Method, ⁋Definition 7](/en/math/linear_algebra/least_squares_method#def7) we saw that the above four conditions uniquely determine $$A^+$$, so the $$A^+$$ of [Definition 5](#def5) is well defined independently of the choice of singular value decomposition, and we also know that the two definitions agree in the full-rank case. For example, if $$A$$ has full column rank, then $$A^tA$$ is invertible, and one can verify directly from

$$\bigl((A^tA)^{-1}A^t\bigr)A=I_n,\qquad A\bigl((A^tA)^{-1}A^t\bigr)=A(A^tA)^{-1}A^t$$

that the matrix $$(A^tA)^{-1}A^t$$ satisfies all four conditions above.

Geometrically, the singular value decomposition $$A=U\Sigma V^t$$ means that an arbitrary linear map $$A$$ decomposes as a composition of a rotation or reflection with respect to an orthonormal basis, a scaling by $$\sigma_i$$ along each axis, and another rotation or reflection. The columns $$v_i$$ of $$V$$ are called the *right singular vectors*, and the columns $$u_i$$ of $$U$$ are called the *left singular vectors*; these are the eigenvectors of $$A^tA$$ and $$AA^t$$, respectively.

---

**References**

**[Goc]** M.S. Gockenbach, *Finite-dimensional linear algebra*, Discrete Mathematics and its applications, Taylor&Francis, 2011.  
**[TB]** L.N. Trefethen and D. Bau, *Numerical linear algebra*, SIAM, 1997.  
**[Str]** G. Strang, *Linear algebra and its applications*, 4th ed., Cengage Learning, 2006.

---
