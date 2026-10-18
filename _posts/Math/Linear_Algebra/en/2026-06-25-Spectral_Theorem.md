---
title: "Spectral Theorem"
description: "We define self-adjoint operators on real inner product spaces and show that all their eigenvalues are real. Furthermore, we prove that every self-adjoint operator admits an orthonormal basis of eigenvectors, establishing the orthogonal diagonalization of real symmetric matrices."
excerpt: "Orthogonal diagonalization of self-adjoint operators"

categories: [Math / Linear Algebra]
permalink: /en/math/linear_algebra/spectral_theorem
sidebar: 
    nav: "linear_algebra-en"


date: 2026-06-25

weight: 24
translated_at: 2026-06-26T22:00:01+00:00
translation_source: kimi-cli
last_polished_at: 2026-10-18T11:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
In [§Eigenspace Decomposition](/en/math/linear_algebra/eigenspace_decomposition){: data-lid="19v4e" }, we examined when a matrix is diagonalizable. Additionally, if an inner product is given on the space, we can explore whether these eigenvectors can be made mutually orthogonal, that is, whether diagonalization through an orthonormal basis is possible.

In this post, we show that the answer to this question is the self-adjoint operator. As we saw in [§Inner Product Spaces](/en/math/linear_algebra/inner_product_spaces){: data-lid="wv2au" }, an inner product essentially depends heavily on the base field, so we divide this theorem into the cases where the base field is $\mathbb{R}$ and $\mathbb{C}$, treating the latter separately in [§Complex Spectral Theorem](/en/math/linear_algebra/complex_spectral_theorem){: data-lid="0rrud" }.

## Self-Adjoint Operator

In [§Inner Product Spaces](/en/math/linear_algebra/inner_product_spaces){: data-lid="7084z" }, on an $\mathbb{R}$-inner product space $V$, for a linear operator $L:V\rightarrow V$, we defined the adjoint $L^t:V\rightarrow V$ as the operator obtained by translating, via the isomorphism $V\cong V^\ast$ given by the inner product, the dual $L^\ast$. This is the unique operator that, for any $v,w\in V$, satisfies $\langle Lv,w\rangle=\langle v,L^t w\rangle$. We pay special attention to operators that coincide with their own adjoint.

::: Definition 1
On an $\mathbb{R}$-inner product space $V$, a linear operator $L:V\rightarrow V$ is called *self-adjoint* if $L=L^t$, that is,

$$\langle Lv,w\rangle=\langle v,Lw\rangle$$

holds for all $v,w\in V$.
:::

## Reality of Eigenvalues

The key fact in the diagonalization of a self-adjoint operator is that the eigenvalues of a (real) symmetric matrix are always real.

::: Lemma 2
All eigenvalues of a real symmetric matrix $A$ are real. That is, all roots of the characteristic polynomial of $A$ are real.
:::
::: Proof
The characteristic polynomial of $A$ is a polynomial of degree $n$ with real coefficients, and by [§Characteristic Polynomial, ⁋Theorem 8](/en/math/linear_algebra/characteristic_polynomial#thm8){: data-lid="ox2uu" }, when extended to $\mathbb{C}$, this polynomial has $n$ roots $\lambda$.

Now consider a corresponding eigenvector $z\in\mathbb{C}^n$, let the vector obtained by taking the complex conjugate of each component of $z$ be $\bar{z}$, and consider the following complex number

$$s=\bar{z}^tAz$$

First, since $Az=\lambda z$,

$$s=\bar{z}^t(\lambda z)=\lambda(\bar{z}^tz)=\lambda\sum_{i=1}^n\lvert z_i\rvert^2$$

On the other hand, since $s$ is a $1\times 1$ matrix, it is equal to its own transpose, and using that $A$ is a real symmetric matrix so that $A=A^t=\bar{A}$, its complex conjugate is

$$\bar{s}=\overline{\bar{z}^tAz}=z^t\bar{A}\bar{z}=z^tA\bar{z}=(z^tA\bar{z})^t=\bar{z}^tA^tz=\bar{z}^tAz=s$$

whence $s$ is real. However, $\sum_i\lvert z_i\rvert^2$ is a positive real number since $z\neq 0$, and therefore for $s=\lambda\sum_i\lvert z_i\rvert^2$ to be real, $\lambda$ must also be real.
:::

Moving the polynomial to $\mathbb{C}$ is inevitable for the proof of this proposition, and indeed in the next post we will prove the complex version of the spectral theorem. In particular, from this we know that a self-adjoint operator always has an eigenvalue (and hence an eigenvector).

::: Corollary 3
On a non-$0$ $\mathbb{R}$-inner product space $V$, a self-adjoint operator $L:V\rightarrow V$ always has an eigenvector.
:::
::: Proof
Choosing an orthonormal basis of $V$, the matrix representation of $L$, $A$, is a real symmetric matrix. Since $\dim V\geq 1$, the characteristic polynomial of $A$ has degree at least $1$, and by the fundamental theorem of algebra it has a root in $\mathbb{C}$. By [Lemma 2](#lem2){: data-lid="28c8g" }, this root is real, so $A$ has a real eigenvalue $\lambda$. Then $\lambda I-A$ is singular, so there exists, satisfying $(\lambda I-A)v=0$, a nonzero $v\in\mathbb{R}^n$, and this is an eigenvector of $L$.
:::

## Spectral Theorem

We now prove that if a self-adjoint operator $L$ preserves a subspace of $V$, $U$ (that is, if $L(U)\subseteq U$ holds), then its orthogonal complement is also invariant under this operator. This is, of course, essential for sequentially constructing the *orthogonal* basis that we proposed in the introduction.

::: Lemma 4
On an $\mathbb{R}$-inner product space $V$, for a self-adjoint operator $L:V\rightarrow V$ and a subspace satisfying $L(U)\subseteq U$, $U\leq V$, we have $L(U^\perp)\subseteq U^\perp$.
:::
::: Proof
Choose any $w\in U^\perp$. For any $u\in U$, since $L$ is self-adjoint,

$$\langle Lw,u\rangle=\langle w,Lu\rangle$$

and since $L(U)\subseteq U$, we have $Lu\in U$, and since $w\in U^\perp$, it follows that $\langle w,Lu\rangle=0$. That is, $\langle Lw,u\rangle=0$ holds for all $u\in U$, so $Lw\in U^\perp$.
:::

We are now ready to prove the spectral theorem.

::: Theorem 5 (Spectral Theorem)
On an $\mathbb{R}$-inner product space $V$, for a self-adjoint operator $L:V\rightarrow V$, there exists an orthonormal basis consisting of eigenvectors of $L$ for $V$. In particular, all of these eigenvalues are real.
:::
::: Proof
We prove this by induction on $\dim V$. If $\dim V=0$, there is nothing to show. Suppose $\dim V\geq 1$. By [Corollary 3](#cor3){: data-lid="x5zd0" }, $L$ has an eigenvector, and dividing it by its norm, we obtain an eigenvector with $\lVert v_1\rVert=1$, $v_1$. Its eigenvalue $\lambda_1$ is real by [Lemma 2](#lem2){: data-lid="g4eay" }.

Let $U=\span v_1$. Then $L(U)\subseteq U$, so by [Lemma 4](#lem4){: data-lid="io0z1" }, $L(U^\perp)\subseteq U^\perp$. On the other hand, since the inner product restricted to $U$ is non-degenerate, by [§Bilinear Forms, ⁋Proposition 8](/en/math/linear_algebra/bilinear_form#prop8){: data-lid="mjjrs" } we have $V=U\oplus U^\perp$ and $\dim U^\perp=\dim V-1$. Also, for the restriction to $U^\perp$, $L\vert_{U^\perp}:U^\perp\rightarrow U^\perp$, since for any $w,w'\in U^\perp$ we still have $\langle Lw,w'\rangle=\langle w,Lw'\rangle$, it is again self-adjoint on $U^\perp$. Therefore, by the inductive hypothesis, there exists an orthonormal basis consisting of eigenvectors of $L\vert_{U^\perp}$ for $U^\perp$, $\{v_2,\ldots, v_n\}$.

These vectors are all also eigenvectors of $L$, and since $v_1\in U$ and $v_2,\ldots, v_n\in U^\perp$, $v_1$ is orthogonal to the rest. Therefore, $\{v_1,v_2,\ldots, v_n\}$ is an orthonormal basis consisting of eigenvectors of $L$ for $V$.
:::

In the language of matrices, the spectral theorem means orthogonal diagonalization of real symmetric matrices.

::: Corollary 6
For any real symmetric matrix $A$, there exist an orthogonal matrix $Q$ and a real diagonal matrix $D$ such that 

$$A=QDQ^t$$

holds. Here, the diagonal entries of $D$ are the eigenvalues of $A$, and the columns of $Q$ are the corresponding orthonormal eigenvectors. 
:::
::: Proof
Viewing $A$ as a self-adjoint operator on $\mathbb{R}^n$, by [Theorem 5](#thm5){: data-lid="w9szm" }, there exists an orthonormal basis of eigenvectors of $A$, $\{v_1,\ldots, v_n\}$. Let $Av_i=\lambda_iv_i$, and with $v_i$ as columns, consider the matrix $Q=(v_1\mid\cdots\mid v_n)$. Since the columns of $Q$ are orthonormal, $Q$ is an orthogonal matrix. ([§Inner Product Spaces, ⁋Definition 7](/en/math/linear_algebra/inner_product_spaces#def7){: data-lid="q6oue" }) Then 

$$AQ=(Av_1\mid\cdots\mid Av_n)=(\lambda_1v_1\mid\cdots\mid\lambda_nv_n)=QD$$

where $D=\diag(\lambda_1,\ldots,\lambda_n)$. Multiplying both sides on the right by $Q^t=Q^{-1}$, we obtain $A=QDQ^t$. 
:::

The spectral theorem also shows that eigenspaces corresponding to distinct eigenvalues are automatically orthogonal. 

::: Corollary 7
On an $\mathbb{R}$-inner product space $V$, for a self-adjoint operator $L$, two distinct eigenvalues $\lambda\neq\mu$, and corresponding eigenvectors $v,w$, we have $\langle v,w\rangle=0$. Therefore, $V$ decomposes into an orthogonal direct sum of eigenspaces. 
:::
::: Proof
Since $L$ is self-adjoint, 

$$\lambda\langle v,w\rangle=\langle Lv,w\rangle=\langle v,Lw\rangle=\mu\langle v,w\rangle$$

and thus $(\lambda-\mu)\langle v,w\rangle=0$. Since $\lambda\neq\mu$, we have $\langle v,w\rangle=0$. Grouping the vectors of the orthonormal basis from [Theorem 5](#thm5){: data-lid="xih5t" } by their eigenvalues, we obtain an orthonormal basis for each eigenspace, and by the orthogonality just shown, distinct eigenspaces are orthogonal. 
:::

## Positive definite operator

Among self-adjoint operators, those whose eigenvalues are all positive deserve a separate name. 

::: Definition 8
On an $\mathbb{R}$-inner product space $V$, a self-adjoint operator $L:V\rightarrow V$ is said to be *positive semidefinite* if for all $v\in V$ we have $\langle Lv,v\rangle\geq 0$, and *positive definite* if for all $0\neq v\in V$ we have $\langle Lv,v\rangle> 0$.
:::

::: Proposition 9
On an $\mathbb{R}$-inner product space $V$, a self-adjoint operator $L$ is positive semidefinite if and only if all eigenvalues of $L$ are greater than or equal to $0$, and positive definite if and only if all eigenvalues of $L$ are positive. 
:::
::: Proof
By [Theorem 5](#thm5){: data-lid="sbxff" }, choose an orthonormal basis of eigenvectors of $L$, $\{v_1,\ldots, v_n\}$, and let $Lv_i=\lambda_iv_i$. For any $v=\sum_i a_iv_i$, we have 

$$\langle Lv,v\rangle=\left\langle\sum_i a_i\lambda_iv_i,\sum_j a_jv_j\right\rangle=\sum_i\lambda_ia_i^2$$

The last equality follows from $\langle v_i,v_j\rangle=\delta_{ij}$. If all $\lambda_i\geq 0$, this value is always greater than or equal to $0$, and conversely, if some $\lambda_i<0$, then for $v=v_i$ we have $\langle Lv_i,v_i\rangle=\lambda_i<0$. Thus, positive semidefiniteness is equivalent to all eigenvalues being greater than or equal to $0$. Since it is verified in the same manner that for $0\neq v$, having $\sum_i\lambda_ia_i^2>0$ is equivalent to all $\lambda_i>0$, the assertion for positive definiteness also holds. 
:::

The matrix of a positive definite operator also decomposes concisely via triangular matrices. In fact, this decomposition is an even simpler form, for symmetric positive definite matrices, of the LU decomposition of general square matrices defined in [§Gaussian Elimination, ⁋Definition 8](/en/math/linear_algebra/Gaussian_elimination#def8){: data-lid="5e5z4" }, and it reduces the amount of computation by half in that only $L$ needs to be computed and the $U$ part is obtained automatically.

::: Proposition 10 (Cholesky Decomposition)
For a positive definite real symmetric matrix $A$, there exists a unique lower triangular matrix $L$ whose diagonal entries are all positive such that $A=LL^t$.
:::
::: Proof
We show existence by induction on the size of $A$, $n$. If $n=1$, then in $A=(a)$, $a>0$ by positive definiteness, so setting $L=(\sqrt{a})$ suffices. Suppose $n\geq 2$ and split $A$ as

$$A=\begin{pmatrix}\alpha&b^t\\ b&A'\end{pmatrix}$$

Here $\alpha=A_{11}>0$ is positive by positive definiteness. The *Schur complement* $A''=A'-\alpha^{-1}bb^t$ is also positive definite, because for any $0\neq y\in\mathbb{R}^{n-1}$, setting $x=-\alpha^{-1}(b^ty)$ gives

$$\begin{pmatrix}x&y^t\end{pmatrix}A\begin{pmatrix}x\\ y\end{pmatrix}=\alpha x^2+2x(b^ty)+y^tA'y=y^tA''y$$

and the left-hand side is positive by the positive definiteness of $A$. By the inductive hypothesis, since $A''=L'L'^t$ for some lower triangular matrix $L'$ with positive diagonal entries, setting

$$L=\begin{pmatrix}\sqrt{\alpha}&0\\ \alpha^{-1/2}b&L'\end{pmatrix}$$

gives

$$LL^t=\begin{pmatrix}\alpha&b^t\\ b&\alpha^{-1}bb^t+L'L'^t\end{pmatrix}=\begin{pmatrix}\alpha&b^t\\ b&A'\end{pmatrix}=A$$

and the diagonal entries of $L$ are all positive. Uniqueness follows from the first column being determined by $\sqrt{\alpha}$ and $\alpha^{-1/2}b$, and from $L'$ being inductively unique.
:::


---

**References**

**[Goc]** M.S. Gockenbach, *Finite-dimensional linear algebra*, Discrete Mathematics and its applications, Taylor&Francis, 2011.  
**[Lee]** 이인석, *선형대수와 군*, 서울대학교 출판문화원, 2005.

---
