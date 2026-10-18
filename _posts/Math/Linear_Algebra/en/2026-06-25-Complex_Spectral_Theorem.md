---
title: "Complex Spectral Theorem"
description: "We define normal operators on complex inner product spaces as a generalization of self-adjoint operators, and prove that normal operators are precisely the operators diagonalizable with respect to an orthonormal basis. As special cases, we obtain the real eigenvalues of self-adjoint operators and the unit circle eigenvalues of unitary operators."
excerpt: "unitary diagonalization of normal operators"

categories: [Math / Linear Algebra]
permalink: /en/math/linear_algebra/complex_spectral_theorem
sidebar: 
    nav: "linear_algebra-en"


date: 2026-06-25

weight: 25
translated_at: 2026-06-26T21:30:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-10-18T07:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
In [§Spectral Theorem](/en/math/linear_algebra/spectral_theorem){: data-lid="osc4r" }, we saw that a self-adjoint operator on an $\mathbb{R}$-inner product space is precisely diagonalized by an orthonormal basis, and that in the process we necessarily had to ascend to $\mathbb{C}$. Now we examine what theorem the spectral theorem gives for complex matrices.

## Self-Adjoint and Normal Operators

First, just as in the real case, the first step is to give a name to an operator that coincides with its own adjoint.

::: Definition 1
A linear operator $L:V\rightarrow V$ on a complex inner product space $V$ is called *self-adjoint*, or *Hermitian*, if $L=L^\ast$, that is, $\langle Lv,w\rangle=\langle v,Lw\rangle$ for all $v,w\in V$.
:::

That is, when $V^\ast$ is transferred to $V$ via the isomorphism given by the inner product, this means that the dual operator $L^\ast: V^\ast\rightarrow V^\ast$ translated to $V$ is itself. In the case of real matrices, this yielded a symmetric matrix, but for complex numbers the only difference is that this yields a conjugate-transpose matrix. A point that can be somewhat confusing is that $L^\ast$ now becomes a notation denoting both the conjugate-transpose and the dual map, but as we saw above, if we view $V$ and $V^\ast$ as the same via the isomorphism given by the complex inner product space, the two actually become the same, so there is no real harm.

One difference from the real case is that it is now <em>not</em> only self-adjoint operators that are diagonalized by an orthonormal basis, and for this, we must generalize as in the following definition.

::: Definition 2
A linear operator $L:V\rightarrow V$ on a complex inner product space $V$ is called a *normal operator* if

$$LL^\ast=L^\ast L$$

holds.
:::

Then in particular, a self-adjoint operator is a normal operator since $LL^\ast=L^2=L^\ast L$, and a unitary operator is as well. ([§Complex Inner Product Spaces, ⁋Definition 6](/en/math/linear_algebra/complex_inner_product_spaces#def6){: data-lid="5btee" }) Not only that, but a *skew-Hermitian* operator satisfying $L^\ast=-L$ is also a normal operator since $LL^\ast=-L^2=L^\ast L$; as such, normal operators form a broad class containing many special cases, and the goal of this post is to show that they are precisely the operators diagonalized by an orthonormal basis.

## Schur Decomposition

On a complex inner product space, even an arbitrary linear operator can be shown to be similar to an upper triangular matrix with respect to an orthonormal basis. This is the Schur decomposition, and in the case of a normal operator, this upper triangular matrix automatically becomes diagonal, giving back the complex spectral theorem.

::: Theorem 3 (Schur)
On a complex inner product space $V$, for any linear operator $L:V\rightarrow V$, the matrix representation of $L$ is an upper triangular matrix with respect to some orthonormal basis of $V$. In the language of matrices, for any $A\in\Mat_n(\mathbb{C})$ there exist a unitary matrix $U$ and an upper triangular matrix $T$ such that $A=UTU^\ast$.
:::
::: Proof
We proceed by induction on $\dim V$. We need to show that $V$ has an orthonormal basis $\{e_1,\ldots,e_n\}$ such that for each $j$ we have $Le_j\in\span(e_1,\ldots,e_j)$. The case $\dim V\leq 1$ is trivial, so let $\dim V=n\geq 2$.

The characteristic polynomial of $L^\ast$ has degree at least $1$, so by [§Characteristic Polynomial, ⁋Theorem 8](/en/math/linear_algebra/characteristic_polynomial#thm8){: data-lid="xqzr1" } it has a root; thus $L^\ast$ has, for some eigenvalue $\mu$, an eigenvector of norm $\lVert e_n\rVert=1$, namely $e_n$. Now in $V$, consider the complement of the line spanned by $e_n$, $W=(\span e_n)^\perp$. Then

$$\langle Lw,e_n\rangle=\langle w,L^\ast e_n\rangle=\langle w,\mu e_n\rangle=\mu\langle w,e_n\rangle=0$$

so $Lw\in W$. That is, $W$ is invariant under $L$, and hence we may view $L\vert_W$ as a linear operator defined on $W$; now by the induction hypothesis, $W$ has an orthonormal basis $\{e_1,\ldots,e_{n-1}\}$ such that for each $j\leq n-1$ we have $Le_j\in\span(e_1,\ldots,e_j)$.

Then $\{e_1,\ldots,e_n\}$ is an orthonormal basis of $V$, and for $j<n$ we have $Le_j\in\span(e_1,\ldots,e_j)$ while for $j=n$ we trivially have $Le_n\in V=\span(e_1,\ldots,e_n)$. Thus the matrix representation of $L$ with respect to this basis is upper triangular. Letting $U$ be the matrix whose columns are the vectors of this basis, $U$ is unitary ([§Complex Inner Product Spaces, ⁋Definition 6](/en/math/linear_algebra/complex_inner_product_spaces#def6){: data-lid="m9l4l" }) and $U^\ast AU=T$ is upper triangular, so $A=UTU^\ast$.
:::

The upper triangular matrix $T$ is similar to $A$, so it has the same characteristic polynomial, and the characteristic polynomial of an upper triangular matrix is $\prod_i(\x-T_{ii})$; thus the diagonal entries of $T$, $T_{11},\ldots,T_{nn}$, contain exactly the eigenvalues of $A$ with multiplicity. The Schur decomposition states that any complex matrix can reveal its eigenvalues on the diagonal by a unitary transformation alone.

If in addition the given matrix was normal, then this upper triangular matrix further becomes diagonal.

::: Corollary 4
A normal matrix $A\in\Mat_n(\mathbb{C})$ is diagonalized by a unitary matrix.
:::
::: Proof
By [Theorem 3](#thm3){: data-lid="scc8a" }, we can write $A=UTU^\ast$ with $T$ upper triangular, and what we need to show is that if $A$ is normal, then $T$ is a diagonal matrix. First, since $U$ is unitary, $T=U^\ast AU$ is also a normal matrix, and we show that $T$, being upper triangular and normal, is diagonal by induction on the rows of $T$.

First, since $T$ is upper triangular, the first column of $T$ is $(T_{11},0,\ldots,0)^t$, and thus $\lVert Te_1\rVert^2=\lvert T_{11}\rvert^2$. On the other hand, the first column of $T^\ast$ is the conjugate of the first row of $T$, so $\lVert T^\ast e_1\rVert^2=\sum_{j}\lvert T_{1j}\rvert^2$. Since $T$ is normal,

$$\lVert Te_1\rVert^2=\langle Te_1,Te_1\rangle=\langle e_1,T^\ast Te_1\rangle=\langle e_1,TT^\ast e_1\rangle=\langle T^\ast e_1,T^\ast e_1\rangle=\lVert T^\ast e_1\rVert^2$$

and thus $\lvert T_{11}\rvert^2=\sum_{j}\lvert T_{1j}\rvert^2$, so for $j>1$ we have $T_{1j}=0$. That is, the first row is all $0$ except for the diagonal entry. Then the second and lower rows of $T$ form an $(n-1)\times(n-1)$ upper triangular normal matrix obtained by removing the first row and column, so inductively it too is diagonal, and hence $T$ as a whole is diagonal. Therefore $A=UTU^\ast$ is a unitary diagonalization.
:::

The Schur decomposition forms a nice contrast with [§Jordan Canonical Form](/en/math/linear_algebra/Jordan_canonical_form){: data-lid="blwr3" }. While the Jordan canonical form uses a generally non-unitary change of basis to put a matrix into a canonical block form, the Schur decomposition restricts the change of basis to be unitary, giving up a canonical form and settling for an upper triangular form instead. The latter has the advantage of being numerically stable because orthonormality is preserved, and is frequently used in applications.

## Complex Spectral Theorem

The unitary diagonalization of a normal matrix is a direct consequence of [Theorem 3](#thm3){: data-lid="kot0j" }. More precisely, the complex version of the spectral theorem shows that a normal operator is exactly an operator diagonalized by an orthonormal basis.

::: Theorem 5 (Complex Spectral Theorem)
On a complex inner product space $V$, a linear operator $L:V\rightarrow V$ is a normal operator if and only if there exists an orthonormal basis consisting of eigenvectors of $L$ for $V$.
:::
::: Proof
First, if $L$ is normal, then it is clear by [Corollary 4](#cor4){: data-lid="sibgn" } that $L$ is diagonalized by an orthonormal basis, so the crux is the converse. Suppose there exists an orthonormal basis consisting of eigenvectors of $L$, say $\{v_1,\ldots,v_n\}$, such that $Lv_i=\lambda_i v_i$. Then by [§Complex Inner Product Spaces, ⁋Proposition 5](/en/math/linear_algebra/complex_inner_product_spaces#prop5){: data-lid="8mdl2" }, the matrix representation of $L^\ast$ with respect to this basis is $\diag(\bar{\lambda}_1,\ldots,\bar{\lambda}_n)$. Now since two diagonal matrices commute, $LL^\ast=L^\ast L$, and therefore $L$ is a normal operator.
:::

In the language of matrices, this theorem is (as seen in the proof) about the unitary diagonalization of a normal matrix.

::: Corollary 6
A matrix $A\in\Mat_n(\mathbb{C})$ is a normal matrix if and only if there exist a unitary matrix $U$ and a diagonal matrix $D$ such that

$$A=UDU^\ast$$

holds. In this case, the diagonal entries of $D$ are the eigenvalues of $A$, and the columns of $U$ are the corresponding orthonormal eigenvectors.
:::

## Special Cases

As explained above, self-adjoint operators and unitary operators are normal operators, so by [Theorem 5](#thm5){: data-lid="k5fdw" } they are both diagonalized by an orthonormal basis. What makes them special is that the diagonal matrix obtained as a result of diagonalization has a special form.

::: Proposition 7
All eigenvalues of a self-adjoint operator on a complex inner product space are real, and all eigenvalues of a unitary operator have absolute value $1$.
:::
::: Proof
Let $L$ be self-adjoint and let $Lv=\lambda v$, $v\neq 0$. Then we can compute $\langle Lv,v\rangle=\langle v, Lv\rangle$ in two ways. First, using linearity in the second variable,

$$\langle v,Lv\rangle=\langle v,\lambda v\rangle=\lambda\lVert v\rVert^2$$

On the other hand, using conjugate-linearity in the first variable,

$$\langle Lv,v\rangle=\langle\lambda v,v\rangle=\bar{\lambda}\lVert v\rVert^2$$

so comparing the two expressions, $\lambda\lVert v\rVert^2=\bar{\lambda}\lVert v\rVert^2$ and since $\lVert v\rVert^2>0$ we get $\lambda=\bar{\lambda}$, i.e., $\lambda$ is real.

To see the second result, let $L$ be unitary and let $Lv=\lambda v$, $v\neq 0$. A unitary operator preserves the inner product, so

$$\lVert v\rVert^2=\langle Lv,Lv\rangle=\langle\lambda v,\lambda v\rangle=\bar{\lambda}\lambda\lVert v\rVert^2=\lvert\lambda\rvert^2\lVert v\rVert^2$$

and since $\lVert v\rVert^2>0$ we get $\lvert\lambda\rvert^2=1$, i.e., $\lvert\lambda\rvert=1$.
:::

The complex spectral theorem includes the real version ([§Spectral Theorem, ⁋Theorem 5](/en/math/linear_algebra/spectral_theorem#thm5){: data-lid="x8ljq" }) as a special case. That is, a real symmetric matrix $A$ has real entries, so regarded as a complex matrix we have $A^\ast=\bar{A}^t=A^t=A$, making it self-adjoint over the complex numbers as well, and hence by [Proposition 7](#prop7){: data-lid="71nsi" } all its eigenvalues are real. If an eigenvalue $\lambda$ is real, $A-\lambda I$ is a real matrix, so its kernel also has the same dimension over the real numbers, and therefore one can choose eigenvectors within the real numbers to form an orthonormal basis.

---

**References**

**[Goc]** M.S. Gockenbach, *Finite-dimensional linear algebra*, Discrete Mathematics and its applications, Taylor&Francis, 2011.  
**[Lee]** 이인석, *선형대수와 군*, 서울대학교 출판문화원, 2005.

---
