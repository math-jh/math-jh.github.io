---
title: "Spectral Theorem"
description: "We define self-adjoint operators on inner product spaces and show that all their eigenvalues are real. Furthermore, we prove that every self-adjoint operator admits an orthonormal basis of eigenvectors, establishing the orthogonal diagonalization of real symmetric matrices."
excerpt: "Orthogonal diagonalization of self-adjoint operators"

categories: [Math / Linear Algebra]
permalink: /en/math/linear_algebra/spectral_theorem
sidebar: 
    nav: "linear_algebra-en"


date: 2026-06-25

weight: 120
translated_at: 2026-06-26T22:00:01+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-26T22:00:01+00:00
---
We investigated in [§Eigenspace Decomposition](/en/math/linear_algebra/eigenspace_decomposition) when a matrix is diagonalizable. Additionally, if an inner product is given on the space, we can explore whether these eigenvectors can be made mutually orthogonal—that is, whether diagonalization through an orthonormal basis is possible.

In this post, we show that the answer to this question is the self-adjoint operator. As we saw in [§Inner Product Spaces](/en/math/linear_algebra/inner_product_spaces), the inner product depends heavily on the base field, so we divide this theorem into the cases where the base field is $$\mathbb{R}$$ and $$\mathbb{C}$$, treating the latter separately in [§Complex Spectral Theorem](/en/math/linear_algebra/complex_spectral_theorem).

## Self-Adjoint Operator

In [§Inner Product Spaces](/en/math/linear_algebra/inner_product_spaces), we defined the adjoint $$L^t:V\rightarrow V$$ of a linear operator $$L:V\rightarrow V$$ on an $$\mathbb{R}$$-inner product space $$V$$ as the operator obtained by translating the dual $$L^\ast$$ via the isomorphism $$V\cong V^\ast$$ given by the inner product. This is the unique operator satisfying $$\langle Lv,w\rangle=\langle v,L^t w\rangle$$ for all $$v,w\in V$$. We pay special attention to operators that coincide with their own adjoint.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> A linear operator $$L:V\rightarrow V$$ on an $$\mathbb{R}$$-inner product space $$V$$ is called *self-adjoint* if $$L=L^t$$, that is,

$$\langle Lv,w\rangle=\langle v,Lw\rangle$$

holds for all $$v,w\in V$$.

</div>

## Reality of Eigenvalues

The key fact in the diagonalization of a self-adjoint operator is that the eigenvalues of a (real) symmetric matrix are always real.

<div class="proposition" markdown="1">

<ins id="lem2">**Lemma 2**</ins> All eigenvalues of a real symmetric matrix $$A$$ are real. That is, all roots of the characteristic polynomial of $$A$$ are real.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

The characteristic polynomial of $$A$$ is a polynomial of degree $$n$$ with real coefficients, and by the fundamental theorem of algebra ([§Characteristic Polynomial, ⁋Theorem 8](/en/math/linear_algebra/characteristic_polynomial#thm8)), this polynomial has $$n$$ roots $$\lambda$$ when extended to $$\mathbb{C}$$.

Now consider an eigenvector $$z\in\mathbb{C}^n$$ corresponding to such a root, and let $$\bar z$$ be the vector obtained by taking the complex conjugate of each component of $$z$$. Consider the complex number

$$s=\bar z^tAz$$

First, since $$Az=\lambda z$$,

$$s=\bar z^t(\lambda z)=\lambda(\bar z^tz)=\lambda\sum_{i=1}^n\lvert z_i\rvert^2$$

On the other hand, since $$s$$ is a $$1\times 1$$ matrix, it equals its own transpose, and using that $$A$$ is a real symmetric matrix so that $$A=A^t=\bar A$$, its complex conjugate is

$$\bar s=\overline{\bar z^tAz}=z^t\bar A\bar z=z^tA\bar z=(z^tA\bar z)^t=\bar z^tA^tz=\bar z^tAz=s$$

Thus, $$s$$ is real. However, since $$z\neq 0$$, the sum $$\sum_i\lvert z_i\rvert^2$$ is a positive real number, and therefore for $$s=\lambda\sum_i\lvert z_i\rvert^2$$ to be real, $$\lambda$$ must also be real.

</details>

The necessity of moving the polynomial to $$\mathbb{C}$$ for the proof of this proposition is inevitable, and indeed in the next post we will prove the complex version of the spectral theorem. In particular, from this we know that a self-adjoint operator always has an eigenvalue (and hence an eigenvector).

<div class="proposition" markdown="1">

<ins id="cor3">**Corollary 3**</ins> A self-adjoint operator $$L:V\rightarrow V$$ on a nonzero $$\mathbb{R}$$-inner product space $$V$$ always has an eigenvector.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Choosing an orthonormal basis of $$V$$, the matrix representation $$A$$ of $$L$$ is a real symmetric matrix. Since $$\dim V\geq 1$$, the characteristic polynomial of $$A$$ has degree at least $$1$$, and by the fundamental theorem of algebra it has a root in $$\mathbb{C}$$. By [Lemma 2](#lem2), this root is real, so $$A$$ has a real eigenvalue $$\lambda$$. Then $$\lambda I-A$$ is singular, so there exists a nonzero $$v\in\mathbb{R}^n$$ satisfying $$(\lambda I-A)v=0$$, and this is an eigenvector of $$L$$.

</details>

## Spectral Theorem

We now prove that if a self-adjoint operator $$L$$ preserves a subspace $$U$$ of $$V$$—that is, if $$L(U)\subseteq U$$ holds—then its orthogonal complement is also invariant under this operator. This is, of course, essential for constructing the *orthogonal* basis sequentially as we proposed in the introduction.

<div class="proposition" markdown="1">

<ins id="lem4">**Lemma 4**</ins> For a self-adjoint operator $$L:V\rightarrow V$$ on an $$\mathbb{R}$$-inner product space $$V$$ and a subspace $$U\leq V$$ satisfying $$L(U)\subseteq U$$, we have $$L(U^\perp)\subseteq U^\perp$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Choose any $$w\in U^\perp$$. For any $$u\in U$$, since $$L$$ is self-adjoint,

$$\langle Lw,u\rangle=\langle w,Lu\rangle$$

and since $$L(U)\subseteq U$$, we have $$Lu\in U$$, and since $$w\in U^\perp$$, it follows that $$\langle w,Lu\rangle=0$$. Thus $$\langle Lw,u\rangle=0$$ holds for all $$u\in U$$, so $$Lw\in U^\perp$$.

</details>

We are now ready to prove the spectral theorem.

<div class="proposition" markdown="1">

<ins id="thm5">**Theorem 5 (Spectral Theorem)**</ins> For a self-adjoint operator $$L:V\rightarrow V$$ on an $$\mathbb{R}$$-inner product space $$V$$, there exists an orthonormal basis of $$V$$ consisting of eigenvectors of $$L$$. In particular, all of these eigenvalues are real.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

We prove this by induction on $$\dim V$$. The case $$\dim V=0$$ is trivial. Suppose $$\dim V\geq 1$$. By [Corollary 3](#cor3), $$L$$ has an eigenvector, and dividing by its norm we obtain an eigenvector $$v_1$$ with $$\lVert v_1\rVert=1$$. Its eigenvalue $$\lambda_1$$ is real by [Lemma 2](#lem2).

Let $$U=\span v_1$$. Then $$L(U)\subseteq U$$, so by [Lemma 4](#lem4), $$L(U^\perp)\subseteq U^\perp$$. On the other hand, as we saw in the discussion after [§Inner Product Spaces, ⁋Theorem 9](/en/math/linear_algebra/inner_product_spaces#thm9), we have $$V=U\oplus U^\perp$$ and $$\dim U^\perp=\dim V-1$$. Moreover, the restriction $$L\vert_{U^\perp}:U^\perp\rightarrow U^\perp$$ still satisfies $$\langle Lw,w'\rangle=\langle w,Lw'\rangle$$ for all $$w,w'\in U^\perp$$, so it is again self-adjoint on $$U^\perp$$. Therefore, by the inductive hypothesis, there exists an orthonormal basis $$\{v_2,\ldots, v_n\}$$ of $$U^\perp$$ consisting of eigenvectors of $$L\vert_{U^\perp}$$.

These vectors are also eigenvectors of $$L$$, and since $$v_1\in U$$ and $$v_2,\ldots, v_n\in U^\perp$$, the vector $$v_1$$ is orthogonal to the rest. Therefore $$\{v_1,v_2,\ldots, v_n\}$$ is an orthonormal basis of $$V$$ consisting of eigenvectors of $$L$$.

</details>

In the language of matrices, the spectral theorem means orthogonal diagonalization of real symmetric matrices.

<div class="proposition" markdown="1">

<ins id="cor6">**Corollary 6**</ins> For any real symmetric matrix $$A$$, there exist an orthogonal matrix $$Q$$ and a real diagonal matrix $$D$$ such that

$$A=QDQ^t$$

holds. Here the diagonal entries of $$D$$ are the eigenvalues of $$A$$, and the columns of $$Q$$ are the corresponding orthonormal eigenvectors.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Viewing $$A$$ as a self-adjoint operator on $$\mathbb{R}^n$$, by [Theorem 5](#thm5) there exists an orthonormal basis $$\{v_1,\ldots, v_n\}$$ consisting of eigenvectors of $$A$$. Let $$Av_i=\lambda_iv_i$$, and consider the matrix $$Q=(v_1\mid\cdots\mid v_n)$$ having $$v_i$$ as columns. Since the columns of $$Q$$ are orthonormal, $$Q$$ is an orthogonal matrix. ([§Inner Product Spaces, ⁋Definition 7](/en/math/linear_algebra/inner_product_spaces#def7)) Then

$$AQ=(Av_1\mid\cdots\mid Av_n)=(\lambda_1v_1\mid\cdots\mid\lambda_nv_n)=QD$$

where $$D=\diag(\lambda_1,\ldots,\lambda_n)$$. Multiplying both sides on the right by $$Q^t=Q^{-1}$$, we obtain $$A=QDQ^t$$.

</details>

The spectral theorem also shows that eigenspaces corresponding to distinct eigenvalues are automatically orthogonal.

<div class="proposition" markdown="1">

<ins id="cor7">**Corollary 7**</ins> For a self-adjoint operator $$L$$ on an $$\mathbb{R}$$-inner product space $$V$$ and two distinct eigenvalues $$\lambda\neq\mu$$ with corresponding eigenvectors $$v,w$$, we have $$\langle v,w\rangle=0$$. Therefore, $$V$$ decomposes as an orthogonal direct sum of eigenspaces.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Since $$L$$ is self-adjoint,

$$\lambda\langle v,w\rangle=\langle Lv,w\rangle=\langle v,Lw\rangle=\mu\langle v,w\rangle$$

and thus $$(\lambda-\mu)\langle v,w\rangle=0$$. Since $$\lambda\neq\mu$$, we have $$\langle v,w\rangle=0$$. Grouping the orthonormal basis from [Theorem 5](#thm5) by eigenvalues, we obtain an orthonormal basis for each eigenspace, and by the orthogonality just shown, distinct eigenspaces are orthogonal.

</details>

## Positive Definite Operator

Among self-adjoint operators, those whose eigenvalues are all positive deserve a separate name.

<div class="definition" markdown="1">

<ins id="def8">**Definition 8**</ins> A self-adjoint operator $$L:V\rightarrow V$$ on an $$\mathbb{R}$$-inner product space $$V$$ is called *positive semidefinite* if $$\langle Lv,v\rangle\geq 0$$ for all $$v\in V$$, and *positive definite* if $$\langle Lv,v\rangle> 0$$ for all $$0\neq v\in V$$.

</div>

<div class="proposition" markdown="1">

<ins id="prop9">**Proposition 9**</ins> A self-adjoint operator $$L$$ on an $$\mathbb{R}$$-inner product space $$V$$ is positive semidefinite if and only if all eigenvalues of $$L$$ are nonnegative, and positive definite if and only if all eigenvalues of $$L$$ are positive.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

By [Theorem 5](#thm5), choose an orthonormal basis $$\{v_1,\ldots, v_n\}$$ consisting of eigenvectors of $$L$$, and let $$Lv_i=\lambda_iv_i$$. For any $$v=\sum_i a_iv_i$$,

$$\langle Lv,v\rangle=\left\langle\sum_i a_i\lambda_iv_i,\sum_j a_jv_j\right\rangle=\sum_i\lambda_ia_i^2$$

The last equality follows from $$\langle v_i,v_j\rangle=\delta_{ij}$$. If all $$\lambda_i\geq 0$$, then this value is always nonnegative, and conversely if some $$\lambda_i<0$$, then for $$v=v_i$$ we have $$\langle Lv_i,v_i\rangle=\lambda_i<0$$. Thus positive semidefiniteness is equivalent to all eigenvalues being nonnegative. The equivalence for positive definiteness—that $$\sum_i\lambda_ia_i^2>0$$ for all $$0\neq v$$ is equivalent to all $$\lambda_i>0$$—is verified in the same way.

</details>

The matrix of a positive definite operator also admits a concise decomposition via a triangular matrix. In fact, this decomposition is a simplified form of the LU decomposition ([§Gaussian Elimination, ⁋Definition 8](/en/math/linear_algebra/Gaussian_elimination#def8)) for general square matrices, specialized to symmetric positive definite matrices: only the $$L$$ factor needs to be computed, since the $$U$$ factor is determined automatically, thus halving the computational cost.

<div class="proposition" markdown="1">

<ins id="prop10">**Proposition 10 (Cholesky Decomposition)**</ins> For a positive definite real symmetric matrix $$A$$, there exists a unique lower triangular matrix $$L$$ with all positive diagonal entries such that $$A=LL^t$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

We show existence by induction on the size $$n$$ of $$A$$. If $$n=1$$, then $$A=(a)$$ and by positive definiteness $$a>0$$, so we can take $$L=(\sqrt a)$$. Suppose $$n\geq 2$$ and split $$A$$ as

$$A=\begin{pmatrix}\alpha&b^t\\ b&A'\end{pmatrix}$$

Here $$\alpha=A_{11}>0$$ is positive by positive definiteness. The *Schur complement* $$A''=A'-\alpha^{-1}bb^t$$ is also positive definite, because for any $$0\neq y\in\mathbb{R}^{n-1}$$, setting $$x=-\alpha^{-1}(b^ty)$$ gives

$$\begin{pmatrix}x&y^t\end{pmatrix}A\begin{pmatrix}x\\ y\end{pmatrix}=\alpha x^2+2x(b^ty)+y^tA'y=y^tA''y$$

and the left-hand side is positive by the positive definiteness of $$A$$. By the inductive hypothesis, there exists a lower triangular $$L'$$ with positive diagonal entries such that $$A''=L'L'^t$$, so setting

$$L=\begin{pmatrix}\sqrt\alpha&0\\ \alpha^{-1/2}b&L'\end{pmatrix}$$

gives

$$LL^t=\begin{pmatrix}\alpha&b^t\\ b&\alpha^{-1}bb^t+L'L'^t\end{pmatrix}=\begin{pmatrix}\alpha&b^t\\ b&A'\end{pmatrix}=A$$

and all diagonal entries of $$L$$ are positive. Uniqueness follows from the first column being determined by $$\sqrt\alpha$$ and $$\alpha^{-1/2}b$$, and from $$L'$$ being unique inductively.

</details>


---

**References**

**[Goc]** M.S. Gockenbach, *Finite-dimensional linear algebra*, Discrete Mathematics and its applications, Taylor&Francis, 2011.  
**[Lee]** 이인석, *선형대수와 군*, 서울대학교 출판문화원, 2005.

---
