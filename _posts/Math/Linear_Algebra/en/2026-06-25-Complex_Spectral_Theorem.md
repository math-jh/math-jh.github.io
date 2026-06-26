---
title: "Complex Spectral Theorem"
description: "We define normal operators on complex inner product spaces as a generalization of self-adjoint operators, and prove that an operator is normal if and only if it is diagonalizable with respect to an orthonormal basis. As special cases, we recover the real eigenvalues of self-adjoint operators and the unimodular eigenvalues of unitary operators."
excerpt: "unitary diagonalization of normal operators"

categories: [Math / Linear Algebra]
permalink: /en/math/linear_algebra/complex_spectral_theorem
sidebar: 
    nav: "linear_algebra-en"


date: 2026-06-25

weight: 121
translated_at: 2026-06-26T21:30:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-26T21:30:02+00:00
---
In [§Spectral Theorem](/en/math/linear_algebra/spectral_theorem), we saw that a self-adjoint operator on a $$\mathbb{R}$$-inner product space is precisely diagonalized by an orthonormal basis, and in that process we necessarily had to ascend to $$\mathbb{C}$$. Now we examine what the spectral theorem says for complex matrices.

## Self-Adjoint and Normal Operators

First, just as in the real case, we give a name to an operator that coincides with its own adjoint.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> A linear operator $$L:V\rightarrow V$$ on a complex inner product space $$V$$ is called *self-adjoint*, or *Hermitian*, if $$L=L^\ast$$; equivalently, $$\langle Lv,w\rangle=\langle v,Lw\rangle$$ for all $$v,w\in V$$.

</div>

That is, via the isomorphism furnished by the inner product, when we identify $$V^\ast$$ with $$V$$, the dual operator $$L^\ast: V^\ast\rightarrow V^\ast$$ translated to $$V$$ is exactly $$L$$ itself. For real matrices this yields a symmetric matrix; for complex matrices the only difference is that one obtains the conjugate-transpose. A slightly confusing point is that $$L^\ast$$ now denotes both the conjugate-transpose and the dual map, but as we saw above, if we regard $$V$$ and $$V^\ast$$ as the same via the isomorphism given by a complex inner product, these two actually coincide, so there is no real harm.

One point that differs from the real case is that it is <em>not</em> only self-adjoint operators that are diagonalized by an orthonormal basis; for this we need the following generalization.

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> A linear operator $$L:V\rightarrow V$$ on a complex inner product space $$V$$ is called a *normal operator* if

$$LL^\ast=L^\ast L$$

holds.

</div>

Then in particular a self-adjoint operator satisfies $$LL^\ast=L^2=L^\ast L$$, so it is normal, and a unitary operator is as well. ([§Complex Inner Product Spaces, ⁋Definition 5](/en/math/linear_algebra/complex_inner_product_spaces#def5)) Moreover, a *skew-Hermitian* operator satisfying $$L^\ast=-L$$ also satisfies $$LL^\ast=-L^2=L^\ast L$$, so it is normal. Thus normal operators form a broad class containing many special cases, and the goal of this post is to show that they are exactly the operators diagonalized by an orthonormal basis.

## Schur Decomposition

On a complex inner product space, any linear operator can be shown to be similar to an upper triangular matrix with respect to an orthonormal basis. This is the Schur decomposition, and for a normal operator this upper triangular matrix automatically becomes diagonal, giving back the complex spectral theorem.

<div class="proposition" markdown="1">

<ins id="thm3">**Theorem 3 (Schur)**</ins> For any linear operator $$L:V\rightarrow V$$ on a complex inner product space $$V$$, there exists an orthonormal basis of $$V$$ with respect to which the matrix representation of $$L$$ is upper triangular. In the language of matrices, for any $$A\in\Mat_n(\mathbb{C})$$ there exist a unitary matrix $$U$$ and an upper triangular matrix $$T$$ such that $$A=UTU^\ast$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

We proceed by induction on $$\dim V$$. We need to show that there exists an orthonormal basis $$\{e_1,\ldots,e_n\}$$ of $$V$$ such that for each $$j$$ we have $$Le_j\in\span(e_1,\ldots,e_j)$$. The case $$\dim V\leq 1$$ is trivial, so let $$\dim V=n\geq 2$$.

The characteristic polynomial of $$L^\ast$$ has degree at least $$1$$, so by [§Characteristic Polynomial, ⁋Theorem 8](/en/math/linear_algebra/characteristic_polynomial#thm8) it has a root, and thus $$L^\ast$$ has an eigenvector $$e_n$$ with $$\lVert e_n\rVert=1$$. Now consider the complement $$W=(\span e_n)^\perp$$ of the line spanned by $$e_n$$ in $$V$$. Then

$$\langle Lw,e_n\rangle=\langle w,L^\ast e_n\rangle=\langle w,\mu e_n\rangle=\mu\langle w,e_n\rangle=0$$

so $$Lw\in W$$. That is, $$W$$ is invariant under $$L$$, and hence we may view $$L\vert_W$$ as a linear operator on $$W$$; by the induction hypothesis there exists an orthonormal basis $$\{e_1,\ldots,e_{n-1}\}$$ of $$W$$ such that for each $$j\leq n-1$$ we have $$Le_j\in\span(e_1,\ldots,e_j)$$.

Then $$\{e_1,\ldots,e_n\}$$ is an orthonormal basis of $$V$$, and for $$j<n$$ we have $$Le_j\in\span(e_1,\ldots,e_j)$$ while for $$j=n$$ we trivially have $$Le_n\in V=\span(e_1,\ldots,e_n)$$. Thus the matrix representation of $$L$$ with respect to this basis is upper triangular. Letting $$U$$ be the matrix whose columns are the vectors of this basis, $$U$$ is unitary ([§Complex Inner Product Spaces, ⁋Definition 5](/en/math/linear_algebra/complex_inner_product_spaces#def5)) and $$U^\ast AU=T$$ is upper triangular, so $$A=UTU^\ast$$.

</details>

The upper triangular matrix $$T$$ is similar to $$A$$, so it has the same characteristic polynomial, and the characteristic polynomial of an upper triangular matrix is $$\prod_i(\x-T_{ii})$$; thus the diagonal entries $$T_{11},\ldots,T_{nn}$$ of $$T$$ contain exactly the eigenvalues of $$A$$ with multiplicity. The Schur decomposition says that any complex matrix can reveal its eigenvalues on the diagonal by a unitary transformation alone.

If in addition the given matrix is normal, then this upper triangular matrix further becomes diagonal.

<div class="proposition" markdown="1">

<ins id="cor4">**Corollary 4**</ins> A normal matrix $$A\in\Mat_n(\mathbb{C})$$ is diagonalized by a unitary matrix.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

By [Theorem 3](#thm3) we may write $$A=UTU^\ast$$ with $$T$$ upper triangular, and we need to show that if $$A$$ is normal then $$T$$ is diagonal. Since $$U$$ is unitary, $$T=U^\ast AU$$ is also normal, and we show by induction on the rows of $$T$$ that an upper triangular normal matrix is diagonal.

First, since $$T$$ is upper triangular, its first column is $$(T_{11},0,\ldots,0)^t$$, and thus $$\lVert Te_1\rVert^2=\lvert T_{11}\rvert^2$$. On the other hand, the first column of $$T^\ast$$ is the conjugate of the first row of $$T$$, so $$\lVert T^\ast e_1\rVert^2=\sum_{j}\lvert T_{1j}\rvert^2$$. Since $$T$$ is normal,

$$\lVert Te_1\rVert^2=\langle Te_1,Te_1\rangle=\langle e_1,T^\ast Te_1\rangle=\langle e_1,TT^\ast e_1\rangle=\langle T^\ast e_1,T^\ast e_1\rangle=\lVert T^\ast e_1\rVert^2$$

and thus $$\lvert T_{11}\rvert^2=\sum_{j}\lvert T_{1j}\rvert^2$$, so $$T_{1j}=0$$ for $$j>1$$. That is, the first row is zero except for the diagonal entry. Then the second and lower rows of $$T$$ form an $$(n-1)\times(n-1)$$ upper triangular normal matrix with the first row and column removed, so inductively it too is diagonal, and hence $$T$$ as a whole is diagonal. Therefore $$A=UTU^\ast$$ is a unitary diagonalization.

</details>

The Schur decomposition forms a nice contrast with [§Jordan Canonical Form](/en/math/linear_algebra/Jordan_canonical_form). The Jordan canonical form uses a generally non-unitary change of basis to put a matrix into a canonical block form, whereas the Schur decomposition restricts the change of basis to be unitary at the cost of giving up a canonical form and settling for an upper triangular one. The latter preserves orthonormality and is numerically stable, an advantage that makes it frequently used in applications.

## Complex Spectral Theorem

The unitary diagonalization of a normal matrix is a direct consequence of [Theorem 3](#thm3). More precisely, the complex version of the spectral theorem shows that a normal operator is exactly an operator diagonalized by an orthonormal basis.

<div class="proposition" markdown="1">

<ins id="thm5">**Theorem 5 (Complex Spectral Theorem)**</ins> A linear operator $$L:V\rightarrow V$$ on a complex inner product space $$V$$ is a normal operator if and only if there exists an orthonormal basis of $$V$$ consisting of eigenvectors of $$L$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

If $$L$$ is normal, then it is diagonalized by an orthonormal basis by [Corollary 4](#cor4), so the key is the converse. Suppose there exists an orthonormal basis $$\{v_1,\ldots,v_n\}$$ of $$V$$ consisting of eigenvectors of $$L$$ with $$Lv_i=\lambda_i v_i$$. Then by [§Complex Inner Product Spaces, ⁋Proposition 4](/en/math/linear_algebra/complex_inner_product_spaces#prop4), the matrix representation of $$L^\ast$$ with respect to this basis is $$\diag(\bar\lambda_1,\ldots,\bar\lambda_n)$$. Now two diagonal matrices commute, so $$LL^\ast=L^\ast L$$, and hence $$L$$ is normal.

</details>

In the language of matrices, this theorem says (as we saw in the proof) that a normal matrix admits a unitary diagonalization.

<div class="proposition" markdown="1">

<ins id="cor6">**Corollary 6**</ins> A matrix $$A\in\Mat_n(\mathbb{C})$$ is a normal matrix if and only if there exist a unitary matrix $$U$$ and a diagonal matrix $$D$$ such that

$$A=UDU^\ast$$

holds. In this case, the diagonal entries of $$D$$ are the eigenvalues of $$A$$, and the columns of $$U$$ are the corresponding orthonormal eigenvectors.

</div>

## Special Cases

As explained above, self-adjoint operators and unitary operators are normal, so by [Theorem 5](#thm5) they are both diagonalized by an orthonormal basis. What makes them special is that the diagonal matrix obtained from the diagonalization has a particular form.

<div class="proposition" markdown="1">

<ins id="prop7">**Proposition 7**</ins> All eigenvalues of a self-adjoint operator on a complex inner product space are real, and all eigenvalues of a unitary operator have absolute value $$1$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Let $$L$$ be self-adjoint with $$Lv=\lambda v$$, $$v\neq 0$$. Then we can compute $$\langle Lv,v\rangle=\langle v, Lv\rangle$$ in two ways. First, using linearity in the second variable,

$$\langle v,Lv\rangle=\langle v,\lambda v\rangle=\lambda\lVert v\rVert^2.$$

On the other hand, using conjugate-linearity in the first variable,

$$\langle Lv,v\rangle=\langle\lambda v,v\rangle=\bar\lambda\lVert v\rVert^2$$

so comparing the two expressions, $$\lambda\lVert v\rVert^2=\bar\lambda\lVert v\rVert^2$$ and since $$\lVert v\rVert^2>0$$ we get $$\lambda=\bar\lambda$$, i.e., $$\lambda$$ is real.

To see the second result, let $$L$$ be unitary with $$Lv=\lambda v$$, $$v\neq 0$$. A unitary operator preserves the inner product, so

$$\lVert v\rVert^2=\langle Lv,Lv\rangle=\langle\lambda v,\lambda v\rangle=\bar\lambda\lambda\lVert v\rVert^2=\lvert\lambda\rvert^2\lVert v\rVert^2$$

and since $$\lVert v\rVert^2>0$$ we get $$\lvert\lambda\rvert^2=1$$, i.e., $$\lvert\lambda\rvert=1$$.

</details>

The complex spectral theorem includes the real version ([§Spectral Theorem, ⁋Theorem 5](/en/math/linear_algebra/spectral_theorem#thm5)) as a special case. That is, a real symmetric matrix $$A$$ has real entries, so regarded as a complex matrix we have $$A^\ast=\bar A^t=A^t=A$$, making it self-adjoint over the complex numbers as well, and hence by [Proposition 7](#prop7) all its eigenvalues are real.

---

**References**

**[Axl]** S. Axler, *Linear algebra done right*, 3rd ed., Undergraduate Texts in Mathematics, Springer, 2015.  
**[Goc]** M.S. Gockenbach, *Finite-dimensional linear algebra*, Discrete Mathematics and its applications, Taylor&Francis, 2011.  
**[Lee]** 이인석, *선형대수와 군*, 서울대학교 출판문화원, 2005.

---
