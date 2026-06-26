---
title: "Complex Inner Product Spaces"
description: "We define a conjugate-symmetric Hermitian inner product on a complex vector space, and show that the Cauchy-Schwarz inequality and the Gram-Schmidt process remain valid. We also discuss the adjoint given by the conjugate transpose, and unitary matrices that preserve the inner product."
excerpt: "Hermitian inner product on the complex numbers"

categories: [Math / Linear Algebra]
permalink: /en/math/linear_algebra/complex_inner_product_spaces
sidebar: 
    nav: "linear_algebra-en"


date: 2026-06-23

weight: 118
translated_at: 2026-06-26T21:00:01+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-26T21:00:01+00:00
---
## Complex Inner Product and Norm

In [§Inner Product Spaces](/en/math/linear_algebra/inner_product_spaces), we defined an inner product on an $\mathbb{R}$-vector space. The defining condition of an inner product is positive-definiteness, i.e., $\langle v,v\rangle\geq 0$, which requires an ordering on $\mathbb{K}$ and thus does not immediately carry over to a general field. In particular, on $\mathbb{C}$, if we simply set $\langle v,w\rangle=\sum_i v_iw_i$, then $\langle v,v\rangle=\sum_i v_i^2$ becomes a complex number and we can no longer speak of its sign. The remedy is to take the complex conjugate of one variable: since $\sum_i\bar v_iv_i=\sum_i\lvert v_i\rvert^2$ is always a non-negative real number, we modify the inner product so that it is conjugate-linear in one variable. Such an inner product is called a *Hermitian inner product*, and in this post we examine how the theory of [§Inner Product Spaces](/en/math/linear_algebra/inner_product_spaces) carries over to $\mathbb{C}$-vector spaces equipped with one.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> A function $\langle-,-\rangle:V\times V\rightarrow\mathbb{C}$ on a $\mathbb{C}$-vector space $V$ is called a *Hermitian inner product* if it satisfies the following:

1. (Conjugate-symmetry) For any $v,w\in V$, $\langle w,v\rangle=\overline{\langle v,w\rangle}$;
2. (Linearity in the second argument) For any $v,w,w'\in V$ and $\alpha\in\mathbb{C}$, $\langle v,w+w'\rangle=\langle v,w\rangle+\langle v,w'\rangle$ and $\langle v,\alpha w\rangle=\alpha\langle v,w\rangle$;
3. (Positive-definiteness) For any $v\in V$, $\langle v,v\rangle\geq 0$, and equality holds only when $v=0$.

A space $V$ equipped with such a $\langle-,-\rangle$ is called a *complex inner product space*.

</div>

Setting $v=w$ in condition 1 gives $\langle v,v\rangle=\overline{\langle v,v\rangle}$, so $\langle v,v\rangle$ is always real, and thus the inequality in condition 3 is meaningful. As for condition 2, the inner product is linear in the second variable by definition, but conjugate-linear in the first. Indeed, combining conditions 1 and 2 yields

$$\langle \alpha v,w\rangle=\overline{\langle w,\alpha v\rangle}=\overline{\alpha\langle w,v\rangle}=\bar\alpha\overline{\langle w,v\rangle}=\bar\alpha\langle v,w\rangle$$

so the scalar emerges with a conjugate in the first variable. A form that is linear in one variable and conjugate-linear in the other is called a *sesquilinear form*. The choice of which variable is linear is a matter of convention; in physics it is common to take the first variable as linear.

The most basic example is the *standard Hermitian inner product* on $\mathbb{C}^n$:

$$\langle v,w\rangle=\sum_{i=1}^n\bar v_iw_i=\bar v^tw.$$

Here, conjugate-symmetry follows from $\overline{\bar v^tw}=v^t\bar w=\overline{w}^{\,t}v$, linearity in the second variable follows immediately from the properties of matrix multiplication, and $\langle v,v\rangle=\sum_i\lvert v_i\rvert^2$ is positive whenever $v\neq 0$, so the product is positive-definite.

Meanwhile, since condition 3 implies that $\langle v,v\rangle$ is a non-negative real number, we can define the magnitude of a vector exactly as in the real case.

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> On a complex inner product space $V$, we define the *norm* $\lVert-\rVert:V\rightarrow\mathbb{R}$ by the formula

$$\lVert v\rVert=\sqrt{\langle v,v\rangle}.$$

</div>

However, unlike the real case, the inner product itself takes complex values, so conjugates appear when verifying the properties of the norm. First, for any $v,w\in V$, the sum of $\langle v,w\rangle$ and $\langle w,v\rangle=\overline{\langle v,w\rangle}$ is twice the real part, i.e., $\langle v,w\rangle+\langle w,v\rangle=2\Real\langle v,w\rangle$. Using this, we obtain

$$\lVert v+w\rVert^2=\langle v+w,v+w\rangle=\lVert v\rVert^2+2\Real\langle v,w\rangle+\lVert w\rVert^2.$$

The Cauchy–Schwarz inequality is the key tool in this expansion.

<div class="proposition" markdown="1">

<ins id="prop3">**Proposition 3 (Cauchy–Schwarz)**</ins> For any vectors $v,w$ in a complex inner product space $V$,

$$\lvert\langle v,w\rangle\rvert\leq\lVert v\rVert\lVert w\rVert$$

holds. Equality holds if and only if $v,w$ are linearly dependent.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

If $w=0$, both sides are $0$, so the inequality holds. Suppose $w\neq 0$ and set

$$\lambda=\frac{\langle w,v\rangle}{\langle w,w\rangle}.$$

Then $\langle w,v-\lambda w\rangle=\langle w,v\rangle-\lambda\langle w,w\rangle=0$, so $v-\lambda w$ is orthogonal to $w$. Substituting $v=\lambda w+(v-\lambda w)$, we obtain

$$0\leq\lVert v-\lambda w\rVert^2=\langle v-\lambda w,v-\lambda w\rangle=\lVert v\rVert^2-\bar\lambda\langle w,v\rangle=\lVert v\rVert^2-\frac{\lvert\langle v,w\rangle\rvert^2}{\lVert w\rVert^2}.$$

The last equality follows from

$$\bar\lambda\langle w,v\rangle=\frac{\overline{\langle w,v\rangle}\langle w,v\rangle}{\lVert w\rVert^2}=\frac{\lvert\langle w,v\rangle\rvert^2}{\lVert w\rVert^2}$$

and the fact that $\lvert\langle w,v\rangle\rvert=\lvert\langle v,w\rangle\rvert$. Rearranging gives $\lvert\langle v,w\rangle\rvert^2\leq\lVert v\rVert^2\lVert w\rVert^2$, and equality holds exactly when $v-\lambda w=0$, i.e., when $v,w$ are linearly dependent.

</details>

From this the triangle inequality follows. Applying $\Real\langle v,w\rangle\leq\lvert\langle v,w\rangle\rvert\leq\lVert v\rVert\lVert w\rVert$ to the expression $\lVert v+w\rVert^2=\lVert v\rVert^2+2\Real\langle v,w\rangle+\lVert w\rVert^2$ obtained above, we get

$$\lVert v+w\rVert^2\leq\lVert v\rVert^2+2\lVert v\rVert\lVert w\rVert+\lVert w\rVert^2=(\lVert v\rVert+\lVert w\rVert)^2$$

and thus $\lVert v+w\rVert\leq\lVert v\rVert+\lVert w\rVert$. That $\lVert\alpha v\rVert=\lvert\alpha\rvert\lVert v\rVert$ is immediate from $\langle\alpha v,\alpha v\rangle=\bar\alpha\alpha\langle v,v\rangle=\lvert\alpha\rvert^2\lVert v\rVert^2$, so $\lVert-\rVert$ is indeed a norm. ([§Inner Product Spaces, ⁋Definition 2](/en/math/linear_algebra/inner_product_spaces#def2))

## Orthonormal Basis

As in the real case, two vectors $v,w$ in a complex inner product space are said to be orthogonal when $\langle v,w\rangle=0$, and a basis of mutually orthogonal vectors each of magnitude $1$ is called an orthonormal basis. Here too, the Gram–Schmidt process works exactly as before: given a basis $\{x_1,\ldots,x_n\}$, set $\hat x_1=x_1$ and define

$$\hat x_k=x_k-\sum_{i=1}^{k-1}\frac{\langle\hat x_i,x_k\rangle}{\langle\hat x_i,\hat x_i\rangle}\hat x_i.$$

Then $\langle\hat x_j,\hat x_k\rangle=0$ ($j<k$) is verified inductively, so $\{\hat x_1,\ldots,\hat x_n\}$ is an orthogonal basis. One must be careful that the numerator is $\langle\hat x_i,x_k\rangle$ and not $\langle x_k,\hat x_i\rangle$: for the projection to point in the correct direction, $\hat x_i$ must be placed in the first variable, i.e., the conjugate-linear slot.

If $\mathcal{B}=\{x_1,\ldots,x_n\}$ is an orthonormal basis, then for any $v=\sum_iv_ix_i$, the coefficients are obtained by applying $\langle x_i,-\rangle$:

$$\langle x_i,v\rangle=\sum_jv_j\langle x_i,x_j\rangle=v_i.$$

Thus

$$v=\sum_{i=1}^n\langle x_i,v\rangle x_i.$$

Since the second variable is linear, the order $\langle x_i,v\rangle$ matters when extracting coefficients; using $\langle v,x_i\rangle$ would give the conjugate.

Orthogonal decomposition into subspaces also holds unchanged. For a subspace $U\leq V$ of a complex inner product space $V$, the restriction of the inner product to $U$ is again a Hermitian inner product, so $U$ has an orthonormal basis $\{x_1,\ldots,x_k\}$, which can be extended to an orthonormal basis of $V$. Setting $U^\perp=\{v\in V:\langle u,v\rangle=0\text{ for all }u\in U\}$, we have

$$V=U\oplus U^\perp,\qquad\dim U^\perp=\dim V-\dim U.$$

## Adjoint Operators and Unitary Matrices

For a linear operator $L:V\rightarrow V$ on a complex inner product space $V$, we define its *adjoint* $L^\ast$ exactly as in the real case: the unique operator satisfying

$$\langle Lv,w\rangle=\langle v,L^\ast w\rangle\qquad\text{for all }v,w\in V.$$

The matrix representation with respect to an orthonormal basis reveals the nature of $L^\ast$.

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4**</ins> Let $\mathcal{B}=\{e_1,\ldots,e_n\}$ be an orthonormal basis of a complex inner product space $V$ and let $A=[L]_\mathcal{B}^\mathcal{B}$. Then the matrix representation of $L^\ast$ is the *conjugate transpose* $A^\ast=\bar A^t$ of $A$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Since $Le_i=\sum_kA_{ki}e_k$, we have $\langle e_j,Le_i\rangle=\sum_kA_{ki}\langle e_j,e_k\rangle=A_{ji}$. Then by the definition of the adjoint and conjugate-symmetry,

$$[L^\ast]_{ij}=\langle e_i,L^\ast e_j\rangle=\langle Le_i,e_j\rangle=\overline{\langle e_j,Le_i\rangle}=\overline{A_{ji}}$$

so the $(i,j)$-entry of the matrix representation of $L^\ast$ is $\overline{A_{ji}}$, i.e., $A^\ast=\bar A^t$.

</details>

Thus, whereas the adjoint was given by the transpose in a real inner product space, it is given by the conjugate transpose in a complex inner product space.

Meanwhile, operators preserving the inner product were represented by orthogonal matrices in the real case; the complex analogue is the unitary matrix.

<div class="definition" markdown="1">

<ins id="def5">**Definition 5**</ins> A matrix $U\in\Mat_n(\mathbb{C})$ is called a *unitary matrix* if

$$U^\ast U=UU^\ast=I.$$

An operator $L$ on a complex inner product space satisfying $L^\ast L=I$ is called a *unitary operator*.

</div>

From [§Isomorphisms, ⁋Theorem 7](/en/math/linear_algebra/isomorphic_vector_spaces#thm7), we know that $U^\ast U=I$ automatically implies $UU^\ast=I$, so either condition alone suffices. A unitary operator is exactly an operator that preserves the inner product. Indeed, if $L$ preserves the inner product, then for any $v,w$ we have $\langle v,w\rangle=\langle Lv,Lw\rangle=\langle v,L^\ast Lw\rangle$ for all $v$, so $L^\ast L=I$; conversely, if $L^\ast L=I$, then

$$\langle Lv,Lw\rangle=\langle v,L^\ast Lw\rangle=\langle v,w\rangle$$

and $L$ preserves the inner product. That the change-of-basis matrix between two orthonormal bases is always unitary is verified by the same computation as in the real case, except that because of conjugate-symmetry one change-of-basis matrix is the conjugate transpose of the other. This unitary matrix and the conjugate-transpose adjoint form the foundation for developing the spectral theorem of normal operators, which generalizes self-adjoint operators.

---

**References**

**[Goc]** M.S. Gockenbach, *Finite-dimensional linear algebra*, Discrete Mathematics and its applications, Taylor&Francis, 2011.  
**[Lee]** 이인석, *선형대수와 군*, 서울대학교 출판문화원, 2005.

---
