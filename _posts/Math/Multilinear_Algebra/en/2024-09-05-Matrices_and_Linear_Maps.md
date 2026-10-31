---
title: "Matrices and Linear Maps"
description: "We define matrices as coordinate representations of linear maps and show that matrix multiplication corresponds to composition of linear maps. The relationship between linear maps on free modules and their matrix representations is treated systematically."
excerpt: "Matrix representations of linear maps between free modules and coordinate systems"

categories: [Math / Multilinear Algebra]
permalink: /en/math/multilinear_algebra/matrices_and_linear_maps
sidebar: 
    nav: "multilinear_algebra-en"

date: 2024-09-05
weight: 7
translated_at: 2026-06-01T17:00:07+00:00
translation_source: kimi-cli
last_polished_at: 2026-10-23T23:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
## Coordinate Representation

We now examine the relationship between matrices and linear maps. This can be regarded as a generalization of [\[Linear Algebra\] §Fundamental Theorem of Linear Algebra, ⁋Theorem 5](/en/math/linear_algebra/ftla#thm5){: data-lid="5u97v" }.

Let a free $A$-module $M$ be given, and fix a basis $\mathcal{B}=(e_i)_{i\in I}$ of $M$. Then any $x\in M$ can be written as

$$x=\sum_{i\in I} x_i e_i,\qquad x_i\in A$$

and the column vector $(x_{i0})_{(i,0)\in I\times\{0\}}$ consisting of the $x_i$ corresponding to the coefficients of the $e_i$ in this linear combination is called the *coordinate representation of $x$ with respect to $\mathcal{B}$* and written as $[x]_\mathcal{B}$. On the other hand, it is also worth noting that using the coordinate form, $x_i$ can be written without complicated explanation as the equation

$$x_i=\langle x,e_i^\ast\rangle\tag{1}$$

([§Dual Spaces, ⁋Definition 6](/en/math/multilinear_algebra/dual_spaces#def6){: data-lid="y8nzd" }).

## Matrix Representation of Linear Maps

For the remainder of this post, we assume that two free $A$-modules $M,N$ are given, and fix their bases $\mathcal{B}=(e_i)_{i\in I}$, $\mathcal{C}=(f_j)_{j\in J}$.

::: Definition 1
In the above situation, suppose an arbitrary $A$-linear map $u:M \rightarrow N$ is given. Then the *matrix representation* of $u$ means the following matrix:

$$[u]_\mathcal{C}^\mathcal{B}=(f_j^\ast(u(e_i)))_{(j,i)\in J\times I}=(\langle u(e_i), f_j^\ast\rangle)_{(j,i)\in J\times I}$$

:::

Then first, the following holds.

::: Proposition 2
The $i$-th column of the matrix representation $[u]_\mathcal{C}^\mathcal{B}$ of a linear map $u:M \rightarrow N$ equals the coordinate representation $[u(e_i)]_\mathcal{C}$ of $u(e_i)$ with respect to $\mathcal{C}$.
:::
::: Proof
By definition, the $i$-th column of $[u]_\mathcal{C}^\mathcal{B}$ is given by the formula

$$(f_j^\ast(u(e_i)))_{j\in J}=(\langle u(e_i), f_j^\ast\rangle)_{j\in J}$$

Now, by the preceding equation (1), the $j$-th component of this column vector is precisely the coefficient of $f_j$ when $u(e_i)$ is expressed as a linear combination with respect to the basis $\mathcal{C}$.
:::

If another $A$-linear map $v:M \rightarrow N$ is given, we can verify that

$$[u+v]_\mathcal{C}^\mathcal{B}=[u]_\mathcal{C}^\mathcal{B}+[v]_\mathcal{C}^\mathcal{B}$$

holds. Also, if $\alpha$ is contained in the center of $A$, then $\alpha u$ is an $A$-linear map, and one can see that the matrix representation of this $A$-linear map is given by

$$[\alpha u]_\mathcal{C}^\mathcal{B}=\alpha[u]_\mathcal{C}^\mathcal{B}$$

In summary, $u\mapsto [u]_\mathcal{C}^\mathcal{B}$ is a $Z(A)$-module homomorphism from $\Hom_{\lMod{A}}(M,N)$ to $\Mat_{J\times I}(A)$. This $Z(A)$-linear map is injective, since $u=0$ is equivalent to $u(e_i)=0$ for all $i\in I$. On the other hand, if $J$ is a finite set, then for any element $(x_{ji})$ of $\Mat_{J\times I}(A)$, we can define $u\in\Hom_\lMod{A}(M,N)$ by the formula

$$u(e_i)=\sum_{j\in J} x_{ji} f_j$$

to construct the inverse of the above $Z(A)$-linear map, so this becomes a $Z(A)$-isomorphism.

## Product of Matrix Representations

We previously examined how to define the product of two matrices. As in [\[Linear Algebra\] §Fundamental Theorem of Linear Algebra, ⁋Theorem 5](/en/math/linear_algebra/ftla#thm5){: data-lid="21nb7" }, the product of these matrices corresponds to the composition of linear maps. First, let us prove the following proposition.

::: Proposition 3
If $A$ is commutative and $I,J$ are finite sets, then for any linear map $u:M \rightarrow N$ and any $x\in M$, the formula

$$[u(x)]_\mathcal{C}=[u]_\mathcal{C}^\mathcal{B}[x]_\mathcal{B}$$

holds.
:::
::: Proof
We can verify that the right-hand side yields a column vector, and by formula (2) of [§Matrices, §§Matrix Multiplication](/en/math/multilinear_algebra/matrices#matrix-multiplication){: data-lid="e123n" }, the $j$-th component of the right-hand side is

$$\left([u]_\mathcal{C}^\mathcal{B}[x]_\mathcal{B}\right)_{j0}=\sum_{i\in I}\left([u]_\mathcal{C}^\mathcal{B}\right)_{ji}\left([x]_\mathcal{B}\right)_{i0}=\sum_{i\in I}\left\langle u(e_i),f_j^\ast\right\rangle \left\langle x,e_i^\ast\right\rangle$$

On the other hand, looking at the left-hand side, since $x=\sum_{i\in I}x_i e_i$, the $j$-th component of $[u(x)]_\mathcal{C}$ is

$$\langle u(x),f_j^\ast\rangle=\left\langle u\left(\sum_{i\in I} x_i e_i\right), f_j^\ast\right\rangle=\left\langle \sum_{i\in I} x_i u(e_i), f_j^\ast\right\rangle=\sum_{i\in I}x_i\langle u(e_i),f_j^\ast\rangle=\sum_{i\in I}\left\langle u(e_i),f_j^\ast\right\rangle \left\langle x,e_i^\ast\right\rangle$$

yielding the desired result.
:::

Combining this with [Proposition 2](#prop2){: data-lid="3b8cl" }, we obtain the following.

::: Corollary 4
Suppose $A$ is commutative and three $A$-modules $M,N,L$ are given, and fix finite bases $\mathcal{B}=(e_i)_{i\in I},\mathcal{C}=(f_j)_{j\in J},\mathcal{D}=(g_k)_{k\in K}$. Then for any linear maps $u:M \rightarrow N$, $v:N \rightarrow L$, the formula

$$[v \circ u]_\mathcal{D}^\mathcal{B}=[v]_\mathcal{D}^\mathcal{C}[u]_\mathcal{C}^\mathcal{B}$$

holds.
:::
::: Proof
Since for any $x\in M$,

$$[v \circ u]_\mathcal{D}^\mathcal{B}[x]_\mathcal{B}=[(v \circ u)(x)]_\mathcal{D}=[v(u(x))]_\mathcal{D}=[v]_\mathcal{D}^\mathcal{C}[u(x)]_\mathcal{C}=[v]_\mathcal{D}^\mathcal{C}[u]_\mathcal{C}^\mathcal{B}[x]_\mathcal{B}$$

we obtain the desired result from the $Z(A)$-isomorphism $\Mat_{K\times I}(A)\cong\Hom_\lMod{A}(M,L)$.
:::

## Transpose of Matrix Representations

Meanwhile, the transpose of a matrix also has a corresponding notion for linear maps.

::: Proposition 5
If $I,J$ are finite sets, then for any linear map $u:M \rightarrow N$, the formula

$$\left([u]_\mathcal{C}^\mathcal{B}\right)^t=\left[u^t\right]_{\mathcal{B}^\ast}^{\mathcal{C}^\ast}$$

holds. Here $\mathcal{B}^\ast$ and $\mathcal{C}^\ast$ are the dual bases of $\mathcal{B},\mathcal{C}$ respectively.
:::
::: Proof
By [§Dual Spaces, ⁋Proposition 8](/en/math/multilinear_algebra/dual_spaces#prop8){: data-lid="d8nlt" }, we may identify $M$ with $M^{\ast\ast}$, under which $\mathcal{B}$ corresponds to the dual basis of $\mathcal{B}^\ast$, namely $\mathcal{B}^{\ast\ast}$. Now

$$\left(\left[u^t\right]_{\mathcal{B}^\ast}^{\mathcal{C}^\ast}\right)_{ij}=\langle u^t(f_j^\ast), e_i^{\ast\ast}\rangle=\langle e_i, u^t(f_j^\ast)\rangle=\langle u(e_i), f_j^\ast\rangle=\left([u]_\mathcal{C}^\mathcal{B}\right)_{ji}=\left(\left([u]_\mathcal{C}^\mathcal{B}\right)^t\right)_{ij} $$

so we obtain the desired result.
:::

## Matrix Representations and Trace

Suppose $A$ is a commutative ring. Previously we defined the trace of a linear map in [§Hom and the Tensor Product, ⁋Definition 6](/en/math/multilinear_algebra/hom_and_tensor#def6){: data-lid="odc8j" }. Now, for any $n\times n$ matrix $X$, let us define the trace of $X$ by

$$\tr(X)=\sum_{i=1}^n x_{ii}$$

Then for any $u\in\End_\rMod{A}(M)$, fixing a basis $\mathcal{B}=(e_i)_{1\leq i\leq n}$ and considering $[u]_\mathcal{B}^\mathcal{B}$, we have

$$\tr([u]_\mathcal{B}^\mathcal{B})=\sum_{i=1}^n ([u]_\mathcal{B}^\mathcal{B})_{ii}=\sum_{i=1}^n\langle u(e_i), e_i^\ast\rangle$$

On the other hand, since for obvious reasons

$$u(x)=\sum_{i=1}^n \langle x, e_i^\ast\rangle u(e_i)$$

we obtain $\tr(u)=\tr([u]_\mathcal{B}^\mathcal{B})$. From this, for $X\in\Mat_{m\times n}(A)$, $Y\in\Mat_{n\times m}(A)$,

$$\tr(XY)=\tr(YX)$$

holds.

## Block Matrices

Finally, we consider more generally the case where two free $A$-modules $M,N$ are each written in the form of a direct sum of submodules

$$M=\bigoplus_{i\in I}M_i,\qquad N=\bigoplus_{j\in J} N_j$$

In particular, if all of the $M_i$, $N_j$ are $A$, this is the exact same situation as above. Then any $x$ can be written uniquely in the form

$$x=\sum_{i\in I} x_i,\qquad x_i\in M_i$$

and we define the coordinate representation of $x$ with respect to this decomposition as

$$[x]_I=(x_{i0})_{i\in I}$$

Also, for any $A$-linear map $u: M \rightarrow N$, once we write

$$u(x_i)=\sum_{j\in J} u_{ji}(x_i),\qquad u_{ji}(x_i)\in N_j$$

the following matrix

$$[u]^I_J=(u_{ji})_{(j,i)\in J\times I}$$

is well-defined. This matrix can be regarded as a $J\times I$ matrix whose $(j,i)$ entry is an element of $\Hom_{\lMod{A}}(M_i,N_j)$.

Even with this generalization, one can verify that all the propositions examined above still hold. In particular, matrix multiplication is noteworthy: suppose $I,J$ are both finite, and in addition each of the $M_i$ and $N_j$ has a finite basis $\mathcal{B}_i$, $\mathcal{C}_j$. Then the collection of all their bases forms, for $M$ and $N$ respectively, the bases $\mathcal{B},\mathcal{C}$. Then one can verify that representing the linear map $u:M \rightarrow N$ as a matrix with respect to these bases equals the matrix obtained by substituting into the above $[u]_J^I$ the matrix representations of each entry $u_{ji}$ with respect to the bases $\mathcal{B}_i$, $\mathcal{C}_j$; and this behaves meaningfully under matrix multiplication. That is, for another direct sum $L=\bigoplus_{k\in K} L_k$ and basis $\mathcal{D}=\bigcup \mathcal{D}_k$, if we write $v:N \rightarrow L$ in the same manner, the matrix representation of $v\circ u$ with respect to the bases $\mathcal{B}, \mathcal{D}$ becomes the matrix having the following matrix

$$\sum_{j\in J}[v_{kj}]_{\mathcal{D}_k}^{\mathcal{C}_j}[u_{ji}]_{\mathcal{C}_j}^{\mathcal{B}_i}$$

in its $(k,i)$ entry.

---

**References**

**[Bou]** Bourbaki, N. Algebra I. *Elements of Mathematics*. Springer. 1998.
