---
title: "Complex Inner Product Spaces"
description: "We define a conjugate-symmetric Hermitian inner product on a complex vector space and verify that the Cauchy-Schwarz inequality and the Gram-Schmidt process remain valid. We then discuss the adjoint defined by conjugate transpose and unitary matrices that preserve the inner product."
excerpt: "Hermitian inner products over complex numbers"

categories: [Math / Linear Algebra]
permalink: /en/math/linear_algebra/complex_inner_product_spaces
sidebar: 
    nav: "linear_algebra-en"


date: 2026-06-23

weight: 118
translated_at: 2026-07-11T11:00:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-07-11T11:00:02+00:00
---
## Complex Inner Product and Norm

In [§Inner Product Spaces](/en/math/linear_algebra/inner_product_spaces), we defined an inner product on an $\mathbb{R}$-vector space. The defining condition of an inner product is positive-definiteness, i.e., $\langle v,v\rangle\geq 0$, which requires an ordering on $\mathbb{K}$ and thus does not carry over directly to a general field. In particular, on $\mathbb{C}$, if we take $\langle v,w\rangle=\sum_i v_iw_i$ verbatim, then $\langle v,v\rangle=\sum_i v_i^2$ becomes a complex number and we cannot speak of its sign. The remedy is to take the complex conjugate of one variable. Since $\sum_i\bar v_iv_i=\sum_i\lvert v_i\rvert^2$ is always a non-negative real number, we modify the inner product so that it becomes conjugate-linear in one variable. We call such an inner product a *Hermitian inner product*, and in this post we examine how the theory of [§Inner Product Spaces](/en/math/linear_algebra/inner_product_spaces) carries over to $\mathbb{C}$-vector spaces equipped with one.

::: Definition 1
A function $\langle-,-\rangle:V\times V\rightarrow\mathbb{C}$ on a $\mathbb{C}$-vector space $V$ is called a *Hermitian inner product* if it satisfies the following:

1. (Conjugate-symmetry) For any $v,w\in V$, $\langle w,v\rangle=\overline{\langle v,w\rangle}$;
2. (Linearity in the second argument) For any $v,w,w'\in V$ and $\alpha\in\mathbb{C}$, $\langle v,w+w'\rangle=\langle v,w\rangle+\langle v,w'\rangle$ and $\langle v,\alpha w\rangle=\alpha\langle v,w\rangle$;
3. (Positive-definiteness) For any $v\in V$, $\langle v,v\rangle\geq 0$, and equality holds only when $v=0$.

A $V$ equipped with such a $\langle-,-\rangle$ is called a *complex inner product space*.
:::

Setting $v=w$ in condition 1 gives $\langle v,v\rangle=\overline{\langle v,v\rangle}$, so $\langle v,v\rangle$ is always real, and hence the inequality in the third condition is meaningful. As for the second condition, by definition this inner product is linear in the second variable but conjugate-linear in the first; indeed, combining conditions 1 and 2 yields

$$\langle \alpha v,w\rangle=\overline{\langle w,\alpha v\rangle}=\overline{\alpha\langle w,v\rangle}=\bar\alpha\overline{\langle w,v\rangle}=\bar\alpha\langle v,w\rangle$$

so the scalar emerges with its conjugate in the first variable. A form that is linear in one variable and conjugate-linear in the other is called a *sesquilinear form*. The choice of which variable is linear is a matter of convention; in physics it is common to take the first variable to be linear.

The most basic example is the *standard Hermitian inner product* on $\mathbb{C}^n$,

$$\langle v,w\rangle=\sum_{i=1}^n\bar v_iw_i=\bar v^tw.$$

Here conjugate-symmetry follows from $\overline{\bar v^tw}=v^t\bar w=\overline{w}^tv$, linearity in the second variable follows immediately from the properties of matrix multiplication, and $\langle v,v\rangle=\sum_i\lvert v_i\rvert^2$ is positive whenever $v\neq 0$, so the product is positive-definite.

Meanwhile, since $\langle v,v\rangle$ is a non-negative real number by the third condition, we can define the length of a vector in exactly the same way as in the real case.

::: Definition 2
On a complex inner product space $V$, the *norm* $\lVert-\rVert:V\rightarrow\mathbb{R}$ is defined by

$\lVert v\rVert=\sqrt{\langle v,v\rangle}.$
:::

However, unlike the real case, the inner product itself takes complex values, so conjugates appear when verifying the properties of the norm. First, for any $v,w\in V$, the sum of $\langle v,w\rangle$ and $\langle w,v\rangle=\overline{\langle v,w\rangle}$ is twice the real part, i.e., $\langle v,w\rangle+\langle w,v\rangle=2\Real\langle v,w\rangle$. Using this, we obtain

$$\lVert v+w\rVert^2=\langle v+w,v+w\rangle=\lVert v\rVert^2+2\Real\langle v,w\rangle+\lVert w\rVert^2.$$

The Cauchy–Schwarz inequality is the key tool in this expansion.

::: Proposition 3 (Cauchy–Schwarz)
For any vectors $v,w$ in a complex inner product space $V$,

$$\lvert\langle v,w\rangle\rvert\leq\lVert v\rVert\lVert w\rVert$$

holds. Equality holds if and only if $v,w$ are linearly dependent.
:::
::: Proof
If $w=0$, both sides are $0$, so the inequality holds. Suppose $w\neq 0$ and set

$$\lambda=\frac{\langle w,v\rangle}{\langle w,w\rangle}.$$

Then $\langle w,v-\lambda w\rangle=\langle w,v\rangle-\lambda\langle w,w\rangle=0$, so $v-\lambda w$ is orthogonal to $w$. Substituting $v=\lambda w+(v-\lambda w)$, we get

$$0\leq\lVert v-\lambda w\rVert^2=\langle v-\lambda w,v-\lambda w\rangle=\lVert v\rVert^2-\bar\lambda\langle w,v\rangle=\lVert v\rVert^2-\frac{\lvert\langle v,w\rangle\rvert^2}{\lVert w\rVert^2}.$$

The last equality follows from

$$\bar\lambda\langle w,v\rangle=\frac{\overline{\langle w,v\rangle}\langle w,v\rangle}{\lVert w\rVert^2}=\frac{\lvert\langle w,v\rangle\rvert^2}{\lVert w\rVert^2}$$

and $\lvert\langle w,v\rangle\rvert=\lvert\langle v,w\rangle\rvert$. Rearranging gives $\lvert\langle v,w\rangle\rvert^2\leq\lVert v\rVert^2\lVert w\rVert^2$, and equality holds exactly when $v-\lambda w=0$, i.e., when $v,w$ are linearly dependent.
:::

From this, the triangle inequality follows. Applying $\Real\langle v,w\rangle\leq\lvert\langle v,w\rangle\rvert\leq\lVert v\rVert\lVert w\rVert$ to the expression $\lVert v+w\rVert^2=\lVert v\rVert^2+2\Real\langle v,w\rangle+\lVert w\rVert^2$ obtained above, we get

$$\lVert v+w\rVert^2\leq\lVert v\rVert^2+2\lVert v\rVert\lVert w\rVert+\lVert w\rVert^2=(\lVert v\rVert+\lVert w\rVert)^2$$

and thus $\lVert v+w\rVert\leq\lVert v\rVert+\lVert w\rVert$. That $\lVert\alpha v\rVert=\lvert\alpha\rvert\lVert v\rVert$ follows immediately from $\langle\alpha v,\alpha v\rangle=\bar\alpha\alpha\langle v,v\rangle=\lvert\alpha\rvert^2\lVert v\rVert^2$, so $\lVert-\rVert$ is indeed a norm. ([§Inner Product Spaces, ⁋Definition 2](/en/math/linear_algebra/inner_product_spaces#def2))

## Orthonormal basis

Just as in the real case, in a complex inner product space we say two vectors $v,w$ are orthogonal when $\langle v,w\rangle=0$, and a basis whose vectors all have norm $1$ and are pairwise orthogonal is called an orthonormal basis. Here too, the Gram–Schmidt process works exactly as before: given a basis $\{x_1,\ldots,x_n\}$, set $\hat x_1=x_1$ and define

$$\hat x_k=x_k-\sum_{i=1}^{k-1}\frac{\langle\hat x_i,x_k\rangle}{\langle\hat x_i,\hat x_i\rangle}\hat x_i;$$

then $\langle\hat x_j,\hat x_k\rangle=0$ ($j<k$) is verified inductively, so $\{\hat x_1,\ldots,\hat x_n\}$ becomes an orthogonal basis. One point requiring care is that the numerator is $\langle\hat x_i,x_k\rangle$, not $\langle x_k,\hat x_i\rangle$: for the projection to point in the correct direction, $\hat x_i$ must be placed in the first variable, the conjugate-linear side.

If $\mathcal{B}=\{x_1,\ldots,x_n\}$ is an orthonormal basis, then for any $v=\sum_iv_ix_i$ the coefficients are obtained by applying $\langle x_i,-\rangle$:

$$\langle x_i,v\rangle=\sum_jv_j\langle x_i,x_j\rangle=v_i.$$

That is,

$$v=\sum_{i=1}^n\langle x_i,v\rangle x_i.$$

Since the second variable is linear, the order $\langle x_i,v\rangle$ matters when extracting coefficients; using $\langle v,x_i\rangle$ would yield the conjugate.

Orthogonal decomposition into subspaces also holds as before. For a subspace $U\leq V$ of a complex inner product space $V$, the restriction of the inner product to $U$ is again Hermitian, so $U$ has an orthonormal basis $\{x_1,\ldots,x_k\}$, which can be extended to an orthonormal basis of $V$. Set $U^\perp=\{v\in V:\langle u,v\rangle=0\text{ for all }u\in U\}$.

::: Proposition 4
For any subspace $U\leq V$ of a complex inner product space $V$,

$$V=U\oplus U^\perp,\qquad\dim U^\perp=\dim V-\dim U$$

hold. Furthermore, the natural projection $p:V\rightarrow V/U$ (from [§Quotient Spaces, ⁋Definition 3](/en/math/linear_algebra/quotient_space#def3)) restricted to $U^\perp$ gives $p\vert_{U^\perp}:U^\perp\rightarrow V/U$, which is an isomorphism; thus $U^\perp$ realizes the quotient space $V/U$ canonically.
:::
::: Proof
Above, we extended an orthonormal basis $\{x_1,\ldots,x_n\}$ of $V$ from one $\{x_1,\ldots,x_k\}$ of $U$, so the remaining vectors $\{x_{k+1},\ldots,x_n\}$ are orthogonal to $U$ and span $U^\perp$. Hence $V=U\oplus U^\perp$ and $\dim U^\perp=\dim V-\dim U$. Now $\ker p=U$, so the kernel of $p\vert_{U^\perp}$ is $U^\perp\cap U=\{0\}$, making it injective; and since $V=U+U^\perp$, it is surjective, hence an isomorphism.
:::

Here positive-definiteness is decisive. If the inner product is positive-definite, then any element $u$ of $U\cap U^\perp$ satisfies $\langle u,u\rangle=0$, so $u=0$; thus every subspace $U$ automatically satisfies $U\cap U^\perp=\{0\}$. For a general symmetric bilinear form this orthogonal decomposition and canonical isomorphism require non-degeneracy of the subspace ([§Bilinear Forms, ⁋Proposition 9](/en/math/linear_algebra/bilinear_form#prop9)), but for positive-definite cases, including Hermitian inner products, it holds without any additional condition.

## Adjoint Operators and Unitary Matrices

For a linear operator $L:V\rightarrow V$ on a complex inner product space $V$, we define its *adjoint* $L^\ast$ as the unique operator satisfying

$$\langle Lv,w\rangle=\langle v,L^\ast w\rangle\qquad\text{for all }v,w\in V$$

just as in the real case. The nature of $L^\ast$ can be understood through its matrix representation with respect to an orthonormal basis.

::: Proposition 5
Let $\mathcal{B}=\{e_1,\ldots,e_n\}$ be an orthonormal basis of a complex inner product space $V$ and let $A=[L]_\mathcal{B}^\mathcal{B}$. Then the matrix representation of $L^\ast$ is the *conjugate transpose* $A^\ast=\bar A^t$ of $A$.
:::
::: Proof
Since $Le_i=\sum_kA_{ki}e_k$, we have $\langle e_j,Le_i\rangle=\sum_kA_{ki}\langle e_j,e_k\rangle=A_{ji}$. Then by the definition of the adjoint and conjugate-symmetry,

$$[L^\ast]_{ij}=\langle e_i,L^\ast e_j\rangle=\langle Le_i,e_j\rangle=\overline{\langle e_j,Le_i\rangle}=\overline{A_{ji}}$$

so the $(i,j)$-entry of the matrix representation of $L^\ast$ is $\overline{A_{ji}}$, i.e., $A^\ast=\bar A^t$.
:::

Thus, whereas the adjoint was given by the transpose in a real inner product space, in a complex inner product space it becomes the conjugate transpose.

Meanwhile, operators preserving the inner product were represented by orthogonal matrices in the real case. The complex analogue is the unitary matrix.

::: Definition 6
A matrix $U\in\Mat_n(\mathbb{C})$ is called a *unitary matrix* if

$$U^\ast U=UU^\ast=I$$

holds. An operator $L$ on a complex inner product space is called a *unitary operator* if it satisfies $L^\ast L=I$.
:::

From [§Isomorphisms, ⁋Theorem 7](/en/math/linear_algebra/isomorphic_vector_spaces#thm7), we know that if $U^\ast U=I$ then automatically $UU^\ast=I$ as well, so one condition is sufficient. A unitary operator is precisely an operator that preserves the inner product. Indeed, if $L$ preserves the inner product, then for any $v,w$ we have $\langle v,w\rangle=\langle Lv,Lw\rangle=\langle v,L^\ast Lw\rangle$ for all $v$, so $L^\ast L=I$; conversely, if $L^\ast L=I$ then

$$\langle Lv,Lw\rangle=\langle v,L^\ast Lw\rangle=\langle v,w\rangle$$

so it preserves the inner product. The fact that the change-of-basis matrix between two orthonormal bases is always unitary can also be verified by the same computation as in the real case, except that due to conjugate-symmetry, one change-of-basis matrix becomes the conjugate transpose of the other. This unitary matrix and the conjugate-transpose adjoint form the foundation for developing the spectral theorem of normal operators, which generalizes self-adjoint operators.

## QR Decomposition

Combining the Gram–Schmidt process with unitary matrices yields a standard decomposition of invertible matrices. The columns $a_1,\ldots,a_n$ of an invertible matrix $A\in\Mat_n(\mathbb{C})$ form a basis of $\mathbb{C}^n$, so we can apply the Gram–Schmidt process to them; in this process, the $k$th vector is constructed using only the first $k$ columns. Therefore, the matrix comparing the orthogonalization result to the original columns must be upper triangular, and organizing this observation gives the following.

::: Proposition 7 (QR decomposition)
Any invertible matrix $A\in\Mat_n(\mathbb{C})$ is uniquely decomposed as a product of a unitary matrix $Q$ and an upper triangular matrix $R$ whose diagonal entries are all positive real numbers:

$A=QR$
:::
::: Proof
Since $A$ is invertible, its columns $a_1,\ldots,a_n$ form a basis of $\mathbb{C}^n$. Applying the Gram–Schmidt process for the standard Hermitian inner product, we obtain an orthogonal basis $\hat a_1,\ldots,\hat a_n$, and normalize by setting $q_k=\hat a_k/\lVert\hat a_k\rVert$. Solving the Gram–Schmidt formula for $a_k$ gives

$$a_k=\hat a_k+\sum_{i=1}^{k-1}\frac{\langle\hat a_i,a_k\rangle}{\langle\hat a_i,\hat a_i\rangle}\hat a_i=\lVert\hat a_k\rVert q_k+\sum_{i=1}^{k-1}\langle q_i,a_k\rangle q_i$$

Let $Q$ be the matrix with columns $q_1,\ldots,q_n$, and define the matrix $R$ by

$$R_{kk}=\lVert\hat a_k\rVert,\qquad R_{ik}=\langle q_i,a_k\rangle\quad(i<k),\qquad R_{ik}=0\quad(i>k)$$

Then the above equation becomes exactly $A=QR$. Since the columns of $Q$ form an orthonormal basis, $(Q^\ast Q)_{ij}=\langle q_i,q_j\rangle$ equals $1$ when $i=j$ and $0$ otherwise, so $Q^\ast Q=I$; hence $Q$ is unitary, and $R$ is an upper triangular matrix with diagonal entries $\lVert\hat a_k\rVert>0$.

To show uniqueness, suppose $A=Q_1R_1=Q_2R_2$ are two decompositions satisfying the conditions, and set $T=Q_2^\ast Q_1=R_2R_1^{-1}$. First, an invertible upper triangular matrix is precisely an invertible matrix that sends the subspace $\span(e_1,\ldots,e_k)$ to itself for each $k=1,\ldots,n$; therefore the inverse and product of such matrices are again upper triangular. Moreover, the diagonal entries of a product of two triangular matrices are the products of the corresponding diagonal entries, so the diagonal entries of $R_1^{-1}$ are $(R_1)_{kk}^{-1}$, and the diagonal entries of $T=R_2R_1^{-1}$ are $(R_2)_{kk}/(R_1)_{kk}$, hence all positive real numbers. On the other hand, $T=Q_2^\ast Q_1$ is a product of unitary matrices, so it is unitary; thus $T^{-1}=T^\ast$, where the left-hand side is the inverse of an upper triangular matrix and hence upper triangular, while the right-hand side is the conjugate transpose of an upper triangular matrix and hence lower triangular. Therefore $T^{-1}$, and consequently $T$, is a diagonal matrix. The diagonal entries of a unitary diagonal matrix must have absolute value $1$, but the diagonal entries of $T$ are positive real numbers, so they are all $1$; hence $T=I$. This means $Q_1=Q_2$ and $R_1=R_2$.
:::

We call this decomposition the *QR decomposition*. As the proof shows, this is simply the Gram–Schmidt process translated into the language of matrices. The columns of $Q$ record the result of orthogonalization, and $R$ records the coefficients used in that process. In particular, if the columns of $A$ are already orthonormal, i.e., if $A$ is already unitary, then the decomposition degenerates to $Q=A$, $R=I$. The same proof works verbatim for the real case: any invertible matrix $A\in\Mat_n(\mathbb{R})$ is uniquely decomposed as a product of an orthogonal matrix and ([§Inner Product Spaces, §§Orthogonal Matrices](/en/math/linear_algebra/inner_product_spaces#직교행렬)) an upper triangular matrix whose diagonal entries are all positive real numbers. Since every step of the above proof consists only of the four arithmetic operations, inner products, and norms on the entries of $A$, the two factors $Q,R$ depend continuously on $A$.

On the other hand, one can arrive at the same decomposition using reflections instead of the Gram–Schmidt process. For a nonzero vector $v\in\mathbb{C}^n$, the *Householder reflection*

$$H_v=I-2\frac{vv^\ast}{v^\ast v}$$

satisfies $H_v^\ast=H_v$ and $H_v^2=I$, so it is a unitary matrix; it fixes the vectors in $v^\perp$ and sends $v$ to $-v$, i.e., it is the reflection across the hyperplane $v^\perp$. For two vectors $x\neq y$ of equal norm with $\langle y,x\rangle$ real, setting $v=x-y$ gives $H_vx=y$, which can be checked by direct computation. Thus for the first column $a_1$ of an invertible matrix $A$, choosing $\alpha$ so that $\lvert\alpha\rvert=\lVert a_1\rVert$ and $\langle\alpha e_1,a_1\rangle$ is real, we obtain a Householder reflection $H_1$ sending $a_1$ to $\alpha e_1$. Then the first column of $H_1A$ is aligned in the $e_1$ direction, and repeating the same process on the remaining lower-right block (the reflection of the lower block is extended to a reflection of $\mathbb{C}^n$ fixing the earlier coordinates) makes $H_{n-1}\cdots H_1A$ upper triangular. That is, setting $Q=H_1\cdots H_{n-1}$ gives $A=QR$; however, the diagonal entries of $R$ obtained this way may deviate from positive real numbers by a factor of a complex number of absolute value $1$, so correcting by a diagonal unitary matrix recovers the form of [Proposition 7](#prop7). This construction is numerically more stable than the Gram–Schmidt process in floating-point arithmetic, and is therefore the standard method for computing the $QR$ decomposition in numerical computation.

---

**References**

**[Goc]** M.S. Gockenbach, *Finite-dimensional linear algebra*, Discrete Mathematics and its applications, Taylor&Francis, 2011.  
**[Lee]** 이인석, *선형대수와 군*, 서울대학교 출판문화원, 2005.

---
