---
title: "Complex Inner Product Spaces"
description: "We define a conjugate-symmetric Hermitian inner product on a complex vector space and verify that the Cauchy-Schwarz inequality and the Gram-Schmidt process remain valid. Furthermore, we discuss the adjoint given by the conjugate transpose and unitary matrices that preserve the inner product, combining them to prove the QR decomposition of invertible matrices."
excerpt: "Hermitian inner products defined over the complex numbers"

categories: [Math / Linear Algebra]
permalink: /en/math/linear_algebra/complex_inner_product_spaces
sidebar: 
    nav: "linear_algebra-en"


date: 2026-06-23

weight: 22
translated_at: 2026-07-11T11:00:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-10-18T03:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
## Complex Inner Product and Norm

In [§Inner Product Spaces](/en/math/linear_algebra/inner_product_spaces){: data-lid="d1ekl" }, we defined an inner product on an $\mathbb{R}$-vector space. The key condition of an inner product is positive-definiteness, namely $\langle v,v\rangle\geq 0$, which requires an ordering on $\mathbb{K}$ and thus does not carry over directly to a general field. In particular, on $\mathbb{C}$, if we use $\langle v,w\rangle=\sum_i v_iw_i$ as is, then $\langle v,v\rangle=\sum_i v_i^2$ becomes a complex number and we cannot speak of its sign. The solution is to take the complex conjugate of one variable, since $\sum_i\bar{v}_iv_i=\sum_i\lvert v_i\rvert^2$ is always a non-negative real number. An inner product modified in this way to be conjugate-linear in one variable is called a *Hermitian inner product*, and in this post we examine how the theory of [§Inner Product Spaces](/en/math/linear_algebra/inner_product_spaces){: data-lid="ueu5l" } carries over to $\mathbb{C}$-vector spaces equipped with one.

::: Definition 1
A function $\langle-,-\rangle:V\times V\rightarrow\mathbb{C}$ on a $\mathbb{C}$-vector space $V$ is called a *Hermitian inner product* if it satisfies the following:

1. (Conjugate-symmetry) For any $v,w\in V$, $\langle w,v\rangle=\overline{\langle v,w\rangle}$;
2. (Linearity on second argument) For any $v,w,w'\in V$ and $\alpha\in\mathbb{C}$, $\langle v,w+w'\rangle=\langle v,w\rangle+\langle v,w'\rangle$ and $\langle v,\alpha w\rangle=\alpha\langle v,w\rangle$;
3. (Positive-definiteness) For any $v\in V$, $\langle v,v\rangle\geq 0$, and equality holds only when $v=0$.

A space $V$ equipped with such a $\langle-,-\rangle$ is called a *complex inner product space*.
:::

Setting $v=w$ in condition 1 gives $\langle v,v\rangle=\overline{\langle v,v\rangle}$, so $\langle v,v\rangle$ is always real, and hence the inequality in the third condition makes sense. As for the second condition, by definition this inner product is linear in the second variable but conjugate-linear in the first; in fact, combining conditions 1 and 2 yields

$$\langle \alpha v,w\rangle=\overline{\langle w,\alpha v\rangle}=\overline{\alpha\langle w,v\rangle}=\bar{\alpha}\overline{\langle w,v\rangle}=\bar{\alpha}\langle v,w\rangle$$

so the scalar comes out with its conjugate from the first variable. A form that is linear in one variable and conjugate-linear in the other is called a *sesquilinear form*. Taking the second variable to be linear is a matter of convention; in mathematical literature, the convention of taking the first variable to be linear is common.

The most basic example is the *standard Hermitian inner product* on $\mathbb{C}^n$,

$$\langle v,w\rangle=\sum_{i=1}^n\bar{v}_iw_i=\bar{v}^tw$$

Here, conjugate-symmetry follows from $\overline{\bar{v}^tw}=v^t\bar{w}=\overline{w}^tv$, linearity in the second variable follows immediately from the properties of matrix multiplication, and since $\langle v,v\rangle=\sum_i\lvert v_i\rvert^2$ is positive when $v\neq 0$, it is positive-definite.

Meanwhile, since $\langle v,v\rangle$ is a non-negative real number by the third condition, we can define the length of a vector in exactly the same way as in the real case.

::: Definition 2
On a complex inner product space $V$, the *norm* $\lVert-\rVert:V\rightarrow\mathbb{R}$ is defined by

$$\lVert v\rVert=\sqrt{\langle v,v\rangle}$$
:::

However, unlike the real case, the inner product itself takes complex values, so conjugates appear when verifying the properties of the norm. First, for any $v,w\in V$, the sum of $\langle v,w\rangle$ and $\langle w,v\rangle=\overline{\langle v,w\rangle}$ is twice the real part, i.e., $\langle v,w\rangle+\langle w,v\rangle=2\Real\langle v,w\rangle$. Using this, we obtain

$$\lVert v+w\rVert^2=\langle v+w,v+w\rangle=\lVert v\rVert^2+2\Real\langle v,w\rangle+\lVert w\rVert^2$$

The Cauchy-Schwarz inequality is the key tool in this expansion.

::: Proposition 3 (Cauchy-Schwarz)
In a complex inner product space $V$, for any vectors $v,w$,

$$\lvert\langle v,w\rangle\rvert\leq\lVert v\rVert\lVert w\rVert$$

holds. Equality holds if and only if $v,w$ are linearly dependent.
:::
::: Proof
If $w=0$, both sides are $0$, so the inequality holds. Suppose $w\neq 0$ and set

$$\lambda=\frac{\langle w,v\rangle}{\langle w,w\rangle}$$

Then $\langle w,v-\lambda w\rangle=\langle w,v\rangle-\lambda\langle w,w\rangle=0$, so $v-\lambda w$ is orthogonal to $w$. Therefore, substituting $v=\lambda w+(v-\lambda w)$, we obtain

$$0\leq\lVert v-\lambda w\rVert^2=\langle v-\lambda w,v-\lambda w\rangle=\lVert v\rVert^2-\bar{\lambda}\langle w,v\rangle=\lVert v\rVert^2-\frac{\lvert\langle v,w\rangle\rvert^2}{\lVert w\rVert^2}$$

The last equality follows from

$$\bar{\lambda}\langle w,v\rangle=\frac{\overline{\langle w,v\rangle}\langle w,v\rangle}{\lVert w\rVert^2}=\frac{\lvert\langle w,v\rangle\rvert^2}{\lVert w\rVert^2}$$

and $\lvert\langle w,v\rangle\rvert=\lvert\langle v,w\rangle\rvert$. Rearranging both sides gives $\lvert\langle v,w\rangle\rvert^2\leq\lVert v\rVert^2\lVert w\rVert^2$, and equality holds precisely when $v-\lambda w=0$, that is, when $v,w$ are linearly dependent.
:::

From this, the triangle inequality follows. In $\lVert v+w\rVert^2=\lVert v\rVert^2+2\Real\langle v,w\rangle+\lVert w\rVert^2$ obtained above, applying $\Real\langle v,w\rangle\leq\lvert\langle v,w\rangle\rvert\leq\lVert v\rVert\lVert w\rVert$ gives

$$\lVert v+w\rVert^2\leq\lVert v\rVert^2+2\lVert v\rVert\lVert w\rVert+\lVert w\rVert^2=(\lVert v\rVert+\lVert w\rVert)^2$$

and thus we obtain $\lVert v+w\rVert\leq\lVert v\rVert+\lVert w\rVert$. Since $\lVert\alpha v\rVert=\lvert\alpha\rvert\lVert v\rVert$ is evident from $\langle\alpha v,\alpha v\rangle=\bar{\alpha}\alpha\langle v,v\rangle=\lvert\alpha\rvert^2\lVert v\rVert^2$, $\lVert-\rVert$ is indeed a norm. ([§Inner Product Spaces, ⁋Definition 2](/en/math/linear_algebra/inner_product_spaces#def2){: data-lid="mkgoq" })

## Orthonormal basis

Just as in the real case, in a complex inner product space two vectors $v,w$ are said to be orthogonal when they satisfy $\langle v,w\rangle=0$, and a basis whose vectors all have norm $1$ and are pairwise orthogonal is called an orthonormal basis. In this case as well, just as in the real case, the Gram-Schmidt process works in the same way: given a basis $\{x_1,\ldots,x_n\}$, setting $\hat{x}_1=x_1$ and defining

$$\hat{x}_k=x_k-\sum_{i=1}^{k-1}\frac{\langle\hat{x}_i,x_k\rangle}{\langle\hat{x}_i,\hat{x}_i\rangle}\hat{x}_i$$

one checks inductively that $\langle\hat{x}_j,\hat{x}_k\rangle=0$ ($j<k$), so $\{\hat{x}_1,\ldots,\hat{x}_n\}$ becomes an orthogonal basis. What requires some attention is that the numerator is $\langle\hat{x}_i,x_k\rangle$ and not $\langle x_k,\hat{x}_i\rangle$; for the projection to be subtracted in the correct direction, $\hat{x}_i$ must be placed in the first variable, that is, on the conjugate-linear side.

If $\mathcal{B}=\{x_1,\ldots,x_n\}$ is an orthonormal basis, then for any $v=\sum_iv_ix_i$, the coefficients are obtained by taking $\langle x_i,-\rangle$:

$$\langle x_i,v\rangle=\sum_jv_j\langle x_i,x_j\rangle=v_i$$

That is,

$$v=\sum_{i=1}^n\langle x_i,v\rangle x_i$$

Since the second variable is linear, the order in $\langle x_i,v\rangle$ is important when extracting coefficients; using $\langle v,x_i\rangle$ yields its conjugate.

Orthogonal decomposition into subspaces also holds as before. In a complex inner product space $V$, for a subspace $U\leq V$, the restriction of the inner product to $U$ is again a Hermitian inner product, so $U$ has an orthonormal basis $\{x_1,\ldots,x_k\}$, which can be extended to an orthonormal basis of $V$ containing it. Set $U^\perp=\{v\in V\mid\langle u,v\rangle=0\text{ for all }u\in U\}$.

::: Proposition 4
In a complex inner product space $V$, for any subspace $U\leq V$,

$$V=U\oplus U^\perp,\qquad\dim U^\perp=\dim V-\dim U$$

holds. Furthermore, the natural projection $p:V\rightarrow V/U$ of [§Quotient Spaces, ⁋Definition 3](/en/math/linear_algebra/quotient_space#def3){: data-lid="3akqh" } restricted to $U^\perp$, $p\vert_{U^\perp}:U^\perp\rightarrow V/U$, is an isomorphism; thus $U^\perp$ canonically realizes the quotient space $V/U$.
:::
::: Proof
Above, since we extended an orthonormal basis of $V$, $\{x_1,\ldots,x_n\}$, from that of $U$, $\{x_1,\ldots,x_k\}$, the remaining $\{x_{k+1},\ldots,x_n\}$ are orthogonal to $U$ and span $U^\perp$. Hence $V=U\oplus U^\perp$ and $\dim U^\perp=\dim V-\dim U$. Then since $\ker p=U$, the kernel of $p\vert_{U^\perp}$ is $U^\perp\cap U=\{0\}$, so it is injective, and since $V=U+U^\perp$, it is surjective, hence an isomorphism.
:::

Here positive-definiteness is decisive. If the inner product is positive-definite, then any element of $U\cap U^\perp$, $u$, satisfies $\langle u,u\rangle=0$, so $u=0$; thus every subspace $U$ automatically satisfies $U\cap U^\perp=\{0\}$. For a general symmetric bilinear form, this orthogonal decomposition and canonical isomorphism require non-degeneracy of the subspace ([§Bilinear Forms, ⁋Proposition 9](/en/math/linear_algebra/bilinear_form#prop9){: data-lid="sokdr" }), but in the positive-definite case, including Hermitian inner products, they hold without any condition.

## Adjoint Operators and Unitary Matrices

On a complex inner product space $V$, for a linear operator $L:V\rightarrow V$, just as in the real case, we define its *adjoint* $L^\ast$ as the unique operator satisfying

$$\langle Lv,w\rangle=\langle v,L^\ast w\rangle\qquad\text{for all }v,w\in V$$

The existence of such an operator is verified by taking an orthonormal basis $\{x_1,\ldots,x_n\}$ and setting $L^\ast w=\sum_i\langle Lx_i,w\rangle x_i$; this is because $\langle Lx_i,w\rangle$ is linear in $w$, so $L^\ast$ is linear, and both $\langle Lv,w\rangle$ and $\langle v,L^\ast w\rangle$ are conjugate-linear in $v$ and agree at $v=x_j$, and uniqueness follows from positive-definiteness. The nature of $L^\ast$ can be understood through its matrix representation with respect to an orthonormal basis.

::: Proposition 5
Let $\mathcal{B}=\{e_1,\ldots,e_n\}$ be an orthonormal basis of a complex inner product space $V$, and let $A=[L]_\mathcal{B}^\mathcal{B}$. Then the matrix representation of $L^\ast$ is the *conjugate transpose* of $A$, $A^\ast=\bar{A}^t$.
:::
::: Proof
Since $Le_i=\sum_kA_{ki}e_k$, we have $\langle e_j,Le_i\rangle=\sum_kA_{ki}\langle e_j,e_k\rangle=A_{ji}$. Then from the definition of the adjoint and conjugate-symmetry,

$$[L^\ast]_{ij}=\langle e_i,L^\ast e_j\rangle=\langle Le_i,e_j\rangle=\overline{\langle e_j,Le_i\rangle}=\overline{A_{ji}}$$

so the matrix representation of $L^\ast$ has $(i,j)$-entry $\overline{A_{ji}}$, that is, $A^\ast=\bar{A}^t$.
:::

That is, whereas the adjoint was given by the transpose in a real inner product space, in a complex inner product space it becomes the conjugate transpose.

Meanwhile, operators preserving the inner product were represented by orthogonal matrices in the real case. In the complex case, the counterpart is the unitary matrix.

::: Definition 6
A matrix $U\in\Mat_n(\mathbb{C})$ is called a *unitary matrix* if

$$U^\ast U=UU^\ast=I$$

holds. An operator $L$ on a complex inner product space is called a *unitary operator* if it satisfies $L^\ast L=I$.
:::

From [§Isomorphisms, ⁋Theorem 7](/en/math/linear_algebra/isomorphic_vector_spaces#thm7){: data-lid="0gvw9" }, we see that if $U^\ast U=I$, then automatically $UU^\ast=I$, so either condition is sufficient. A unitary operator is precisely an operator that preserves the inner product. Indeed, if $L$ preserves the inner product, then for any $v,w$, since $\langle v,w\rangle=\langle Lv,Lw\rangle=\langle v,L^\ast Lw\rangle$ holds for all $v$, we have $L^\ast L=I$; conversely, if $L^\ast L=I$, then

$$\langle Lv,Lw\rangle=\langle v,L^\ast Lw\rangle=\langle v,w\rangle$$

so it preserves the inner product. The fact that the change-of-basis matrix between two orthonormal bases is always a unitary matrix can also be verified by the same computation as in the real case, except that due to conjugate-symmetry, one change-of-basis matrix becomes the conjugate transpose of the other. These unitary matrices and the conjugate transpose adjoint form the foundation for developing the spectral theorem for normal operators, which generalize self-adjoint operators.

## QR Decomposition

Combining the Gram-Schmidt process with unitary matrices yields a standard decomposition of invertible matrices. The columns $a_1,\ldots,a_n$ of an invertible matrix $A\in\Mat_n(\mathbb{C})$ form a basis of $\mathbb{C}^n$, so we can apply the Gram-Schmidt process to them; in this process, the $k$th vector is constructed using only the first $k$ columns. Therefore, the matrix comparing the result of orthogonalization to the original columns must be upper triangular, and putting this together gives the following.

::: Proposition 7 (QR decomposition)
Any invertible matrix $A\in\Mat_n(\mathbb{C})$ is uniquely decomposed as a product of a unitary matrix $Q$ and an upper triangular matrix $R$ whose diagonal entries are all positive real numbers:

$$A=QR$$
:::
::: Proof
Since $A$ is invertible, its columns $a_1,\ldots,a_n$ form a basis of $\mathbb{C}^n$. Applying the Gram–Schmidt process with respect to the standard Hermitian inner product, we obtain an orthogonal basis $\hat{a}_1,\ldots,\hat{a}_n$, and normalize by setting $q_k=\hat{a}_k/\lVert\hat{a}_k\rVert$. Solving the Gram–Schmidt formula for $a_k$ gives

$$a_k=\hat{a}_k+\sum_{i=1}^{k-1}\frac{\langle\hat{a}_i,a_k\rangle}{\langle\hat{a}_i,\hat{a}_i\rangle}\hat{a}_i=\lVert\hat{a}_k\rVert q_k+\sum_{i=1}^{k-1}\langle q_i,a_k\rangle q_i$$

Therefore, letting $Q$ be the matrix with columns $q_1,\ldots,q_n$ and defining the matrix $R$ by

$$R_{kk}=\lVert\hat{a}_k\rVert,\qquad R_{ik}=\langle q_i,a_k\rangle\quad(i<k),\qquad R_{ik}=0\quad(i>k)$$

the above equation becomes precisely $A=QR$. Since the columns of $Q$ form an orthonormal basis, $(Q^\ast Q)_{ij}=\langle q_i,q_j\rangle$ equals $1$ when $i=j$ and $0$ otherwise, so $Q^\ast Q=I$; that is, $Q$ is a unitary matrix, and $R$ is an upper triangular matrix whose diagonal entries are $\lVert\hat{a}_k\rVert>0$.

To show uniqueness, suppose $A=Q_1R_1=Q_2R_2$ are two decompositions satisfying the conditions, and set $T=Q_2^\ast Q_1=R_2R_1^{-1}$. First, an invertible upper triangular matrix is precisely an invertible matrix that, for each $k=1,\ldots,n$, sends the subspace $\span(e_1,\ldots,e_k)$ onto itself; therefore, the inverse and product of such matrices are again upper triangular. Also, since the diagonal entries of a product of two triangular matrices are the products of the corresponding diagonal entries, the diagonal entries of $R_1^{-1}$ are $(R_1)_{kk}^{-1}$, and the diagonal entries of $T=R_2R_1^{-1}$ are $(R_2)_{kk}/(R_1)_{kk}$, that is, all positive real numbers. On the other hand, $T=Q_2^\ast Q_1$ is unitary as a product of unitary matrices, so $T^{-1}=T^\ast$; here the left-hand side is the inverse of an upper triangular matrix and thus upper triangular, while the right-hand side is the conjugate transpose of an upper triangular matrix and thus lower triangular. Therefore $T^{-1}$, and hence $T$, is a diagonal matrix. The diagonal entries of a unitary diagonal matrix must have absolute value $1$, but the diagonal entries of $T$ are positive real numbers, so they are all $1$, which means $T=I$. This means $Q_1=Q_2$ and $R_1=R_2$.
:::

This decomposition is called the *QR decomposition*, and as the proof shows, this is the Gram–Schmidt process translated into the language of matrices. The columns of $Q$ record the results of orthogonalization, and $R$ records the coefficients used in that process. In particular, if the columns of $A$ are already orthonormal, that is, if $A$ is already a unitary matrix, then the decomposition degenerates to $Q=A$, $R=I$. The same proof works verbatim for the real case as well: any invertible matrix $A\in\Mat_n(\mathbb{R})$ is uniquely decomposed as the product of an orthogonal matrix ([§Inner Product Spaces, §§Orthogonal Matrices](/en/math/linear_algebra/inner_product_spaces#orthogonal-matrices){: data-lid="twz70" }) and an upper triangular matrix whose diagonal entries are all positive real numbers; and since every step of the above proof consists only of the four arithmetic operations, inner products, and norms on the entries of $A$, the two factors $Q,R$ depend continuously on $A$.

On the other hand, one can also arrive at the same decomposition using reflections instead of the Gram–Schmidt process. For a vector $0\neq v\in\mathbb{C}^n$, the *Householder reflection*

$$H_v=I-2\frac{vv^\ast}{v^\ast v}$$

satisfies $H_v^\ast=H_v$ and $H_v^2=I$, and thus is a unitary matrix; it fixes vectors in $v^\perp$ and sends $v$ to $-v$, that is, it is the reflection across the hyperplane $v^\perp$. For two vectors of equal norm with $\langle y,x\rangle$ real and $x\neq y$, setting $v=x-y$ gives $H_vx=y$, which can be verified by direct computation; thus for an invertible matrix $A$, if for its first column $a_1$ we arrange that $\lvert\alpha\rvert=\lVert a_1\rVert$ and that $\langle\alpha e_1,a_1\rangle$ is real, choosing $\alpha$ so as to send $a_1$ to $\alpha e_1$ yields a Householder reflection $H_1$. Here, there are two values of $\alpha$ satisfying the conditions, differing only in sign; choosing the one for which $\alpha e_1\neq a_1$ ensures that $v=a_1-\alpha e_1\neq 0$. Then the first column of $H_1A$ is aligned in the direction of $e_1$, and repeating the same process on the remaining lower-right block (the reflection of the lower block being extended to a reflection of $\mathbb{C}^n$ that fixes the earlier coordinates) makes $H_{n-1}\cdots H_1A$ an upper triangular matrix. That is, setting $Q=H_1\cdots H_{n-1}$ gives $A=QR$; the diagonal entries of $R$ obtained this way may deviate from positive real numbers by a complex factor of absolute value $1$, so correcting by a diagonal unitary matrix recovers the form of [Proposition 7](#prop7){: data-lid="ktidb" }. This construction is numerically more stable than the Gram–Schmidt process in floating-point arithmetic, and is therefore used as the standard method for finding the $QR$ decomposition in numerical computation.

---

**References**

**[Goc]** M.S. Gockenbach, *Finite-dimensional linear algebra*, Discrete Mathematics and its applications, Taylor&Francis, 2011.  
**[Lee]** 이인석, *선형대수와 군*, 서울대학교 출판문화원, 2005.

---
