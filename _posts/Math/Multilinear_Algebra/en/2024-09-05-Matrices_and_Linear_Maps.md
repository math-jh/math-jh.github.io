---
title: "Matrices and Linear Maps"
description: "We define matrices as coordinate representations of linear maps and show that matrix multiplication corresponds to composition of linear maps. The relationship between linear maps on free modules and their matrix representations is treated systematically."
excerpt: "Matrix representations of linear maps between free modules and coordinate systems"

categories: [Math / Multilinear Algebra]
permalink: /en/math/multilinear_algebra/matrices_and_linear_maps
header:
    overlay_image: /assets/images/Math/Multilinear_Algebra/Matrices_and_Linear_Maps.png
    overlay_filter: 0.5
sidebar: 
    nav: "multilinear_algebra-en"

date: 2024-09-05
last_modified_at: 2024-09-19
weight: 7
translated_at: 2026-06-01T17:00:07+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-01T17:00:07+00:00
---
## Coordinate Representation

We now examine the relationship between matrices and linear maps. This can be regarded as a generalization of [[Linear Algebra] §Fundamental Theorem of Linear Algebra, ⁋Theorem 5](/en/math/linear_algebra/ftla#thm5). For convenience,

let a free $$A$$-module $$M$$ be given, and fix a basis $$\mathcal{B}=(e_i)_{i\in I}$$ of $$M$$. Then any $$x\in M$$ can be written as

$$x=\sum_{i\in I} x_i e_i,\qquad x_i\in A$$

and the column vector $$(x_{i0})_{(i,0)\in I\times\{0\}}$$ consisting of the coefficients $$x_i$$ of the $$e_i$$ in this linear combination is called the *coordinate representation with respect to $$\mathcal{B}$$*, denoted by $$[x]_\mathcal{B}$$. It is also worth noting that, using the coordinate form, we can write $$x_i$$ simply as

$$x_i=\langle x,e_i^\ast\rangle\tag{1}$$

without further ado. ([§Dual Spaces, ⁋Definition 6](/en/math/multilinear_algebra/dual_spaces#def6))

## Matrix Representation of Linear Maps

For the remainder of this post, we assume that two free $$A$$-modules $$M,N$$ are given, and fix their bases $$\mathcal{B}=(e_i)_{i\in I}$$, $$\mathcal{C}=(f_j)_{j\in J}$$.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> In the above situation, suppose an arbitrary $$A$$-linear map $$u:M \rightarrow N$$ is given. Then the *matrix representation* of $$u$$ is the matrix

$$[u]_\mathcal{C}^\mathcal{B}=(f_j^\ast(u(e_i)))_{(j,i)\in J\times I}=(\langle u(e_i), f_j^\ast\rangle)_{(j,i)\in J\times I}$$.

</div>

We first note the following.

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> The $$i$$-th column of the matrix representation $$[u]_\mathcal{C}^\mathcal{B}$$ of a linear map $$u:M \rightarrow N$$ equals the coordinate representation $$[u(e_i)]_\mathcal{C}$$ of $$u(e_i)$$ with respect to $$\mathcal{C}$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

By definition, the $$i$$-th column of $$[u]_\mathcal{C}^\mathcal{B}$$ is given by

$$(f_j^\ast(u(e_i)))_{j\in J}=(\langle u(e_i), f_j^\ast\rangle)_{j\in J}$$.

The $$j$$-th component of this column vector is, by the preceding formula (1), precisely the coefficient of $$f_j$$ when $$u(e_i)$$ is expressed as a linear combination with respect to the basis $$\mathcal{C}$$.

</details>

If another $$A$$-linear map $$v:M \rightarrow N$$ is given, we can verify that

$$[u+v]_\mathcal{C}^\mathcal{B}=[u]_\mathcal{C}^\mathcal{B}+[v]_\mathcal{C}^\mathcal{B}$$

holds. Moreover, if $$\alpha$$ lies in the center of $$A$$, then $$\alpha u$$ is an $$A$$-linear map, and the matrix representation of this $$A$$-linear map is given by

$$[\alpha u]_\mathcal{C}^\mathcal{B}=\alpha[u]_\mathcal{C}^\mathcal{B}$$.

In summary, $$u\mapsto [u]_\mathcal{C}^\mathcal{B}$$ is a $$Z(A)$$-module homomorphism from $$\Hom_{\lMod{A}}(M,N)$$ to $$\Mat_{J\times I}(A)$$. This $$Z(A)$$-linear map is injective, since $$u=0$$ is equivalent to $$u(e_i)=0$$ for all $$i\in I$$. On the other hand, if $$J$$ is finite, then for any element $$(x_{ji})$$ of $$\Mat_{J\times I}(A)$$, we can define $$u\in\Hom_\lMod{A}$$ by the formula

$$u(e_i)=\sum_{j\in J} \langle u(e_i),f_j^\ast\rangle f_j$$

to construct the inverse of the above $$Z(A)$$-linear map; hence it is a $$Z(A)$$-isomorphism.

## Product of Matrix Representations

We previously examined how the product of two matrices is defined. As in [[Linear Algebra] §Fundamental Theorem of Linear Algebra, ⁋Theorem 5](/en/math/linear_algebra/ftla#thm5), this product corresponds to the composition of linear maps. Let us first prove the following proposition.

<div class="proposition" markdown="1">

<ins id="prop3">**Proposition 3**</ins> If $$I,J$$ are finite sets, then for any linear map $$u:M \rightarrow N$$ and any $$x\in M$$, the formula

$$[u(x)]_\mathcal{C}=[u]_\mathcal{C}^\mathcal{B}[x]_\mathcal{B}$$

holds.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

We can verify that the right-hand side yields a column vector, and by formula (2) of [§Matrices, §§Matrix Multiplication](/en/math/multilinear_algebra/matrices#matrix-multiplication), its $$j$$-th component is

$$\left([u]_\mathcal{C}^\mathcal{B}[x]_\mathcal{B}\right)_{j0}=\sum_{i\in I}\left([u]_\mathcal{C}^\mathcal{B}\right)_{ji}\left([x]_\mathcal{B}\right)_{i0}=\sum_{i\in I}\left\langle u(e_i),f_j^\ast\right\rangle \left\langle x,e_i^\ast\right\rangle$$.

On the other hand, since $$x=\sum_{i\in I}x_i e_i$$, the $$j$$-th component of $$[u(x)]_\mathcal{C}$$ is

$$\langle u(x),f_j^\ast\rangle=\left\langle u\left(\sum_{i\in I} x_i e_i\right), f_j^\ast\right\rangle=\left\langle \sum_{i\in I} x_i u(e_i), f_j^\ast\right\rangle=\sum_{i\in I}x_i\langle u(e_i),f_j^\ast\rangle=\sum_{i\in I}\left\langle u(e_i),f_j^\ast\right\rangle \left\langle x,e_i^\ast\right\rangle$$

yielding the desired result.

</details>

Combining this with [Proposition 2](#prop2), we obtain the following.

<div class="proposition" markdown="1">

<ins id="cor4">**Corollary 4**</ins> Suppose three $$A$$-modules $$M,N,L$$ are given, and fix finite bases $$\mathcal{B}=(e_i)_{i\in I},\mathcal{C}=(f_j)_{j\in J},\mathcal{D}=(g_k)_{k\in K}$$. Then for any linear maps $$u:M \rightarrow N$$, $$v:N \rightarrow L$$, the formula

$$[v \circ u]_\mathcal{D}^\mathcal{B}=[v]_\mathcal{D}^\mathcal{C}[u]_\mathcal{C}^\mathcal{B}$$

holds.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

For any $$x\in M$$,

$$[v \circ u]_\mathcal{D}^\mathcal{B}[x]_\mathcal{B}=[(v \circ u)(x)]_\mathcal{D}=[(v(u(x))]_\mathcal{D}=[v]_\mathcal{D}^\mathcal{C}[u(x)]_\mathcal{C}=[v]_\mathcal{D}^\mathcal{C}[u]_\mathcal{C}^\mathcal{B}[x]_\mathcal{B}$$

so from the $$Z(A)$$-isomorphism $$\Mat_{K\times I}(A)\cong\Hom_\lMod{A}(M,L)$$ we obtain the desired result.

</details>

## Transpose of Matrix Representations

The transpose of a matrix also has a corresponding notion for linear maps.

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> If $$I,J$$ are finite sets, then for any linear map $$u:M \rightarrow N$$, the formula

$$\left([u]_\mathcal{C}^\mathcal{B}\right)^t=\left[u^\ast\right]_{\mathcal{B}^\ast}^{\mathcal{C}^\ast}$$

holds. Here $$\mathcal{B}^\ast$$ and $$\mathcal{C}^\ast$$ are the dual bases of $$\mathcal{B},\mathcal{C}$$ respectively.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

By [§Dual Spaces, ⁋Proposition 8](/en/math/multilinear_algebra/dual_spaces#prop8), we may identify $$M$$ with $$M^{\ast\ast}$$, and then $$\mathcal{B}$$ corresponds to the dual basis $$\mathcal{B}^{\ast\ast}$$ of $$\mathcal{B}^\ast$$. Now

$$\left(\left[u^\ast\right]_{\mathcal{B}^\ast}^{\mathcal{C}^\ast}\right)_{ji}=\langle u^\ast(f_j^\ast), e_i^{\ast\ast}\rangle=\langle e_i, u^\ast(f^\ast)\rangle=\langle u(e_i), f_j^\ast\rangle=\left([u]_\mathcal{C}^\mathcal{B}\right)_{ij}=\left(\left([u]_\mathcal{C}^\mathcal{B}\right)^t\right)_{ji} $$

so we obtain the desired result.

</details>

## Matrix Representations and Trace

Previously we defined the trace of a linear map in [§Hom and Tensor Products, ⁋Definition 6](/en/math/multilinear_algebra/hom_and_tensor#def6). Now, for any $$n\times n$$ matrix $$X$$, we define the trace of $$X$$ by

$$\tr(X)=\sum_{i=1}^n x_{ii}$$.

Then for any $$u\in\End_\rMod{A}(M)$$, fixing a basis $$\mathcal{B}=(e_i)_{1\leq i\leq n}$$ and considering $$[u]_\mathcal{B}^\mathcal{B}$$, we have

$$\tr([u]_\mathcal{B}^\mathcal{B})=\sum_{i=1}^n ([u]_\mathcal{B}^\mathcal{B})_{ii}=\sum_{i=1}^n\langle u(e_i), e_i^\ast\rangle$$.

On the other hand, for obvious reasons

$$u(x)=\sum_{i=1}^n \langle x, e_i^\ast\rangle u(e_i)$$

so we obtain $$\tr(u)=\tr([u]_\mathcal{B}^\mathcal{B})$$. From this, for $$X\in\Mat_{m\times n}(A)$$, $$Y\in\Mat_{n\times m}(A)$$,

$$\tr(XY)=\tr(YX)$$

holds.

## Block Matrices

Finally, we consider the more general situation in which two free $$A$$-modules $$M,N$$ are each written as a direct sum of submodules

$$M=\bigoplus_{i\in I}M_i,\qquad N=\bigoplus_{j\in J} N_j$$.

In the special case where all the $$M_i$$ and $$N_j$$ are equal to $$A$$, this reduces to the situation above. Then any $$x$$ can be written uniquely as

$$x=\sum_{i\in I} x_i,\qquad x_i\in M_i$$

and we define the coordinate representation of $$x$$ with respect to this decomposition as

$$[x]_I=(x_{i0})_{i\in I}$$.

Also, for any $$A$$-linear map $$u: M \rightarrow N$$, writing

$$u(x_i)=\sum_{j\in J} u_{ji}(x_i),\qquad u_{ji}(x_i)\in N_j$$

the matrix

$$[u]^I_J=(u_{ji})_{(j,i)\in J\times I}$$

is well-defined. This matrix can be regarded as a $$J\times I$$ matrix over the ring

$$H=\bigoplus_{(j,i)\in J\times I}\Hom_{\lMod{A}}(M_i,N_j)$$.

Even with this generalization, all the propositions examined above remain valid. In particular, the product of matrices is noteworthy: suppose $$I,J$$ are both finite, and moreover each $$M_i$$ and $$N_j$$ has finite bases $$\mathcal{B}_i$$, $$\mathcal{C}_j$$. Then the unions of these bases form bases $$\mathcal{B},\mathcal{C}$$ of $$M$$ and $$N$$ respectively. The matrix representing a linear map $$u:M \rightarrow N$$ with respect to these bases can be verified to equal the matrix obtained by substituting, for each entry $$u_{ji}$$ in the above $$[u]_J^I$$, its matrix representation with respect to the bases $$\mathcal{B}_i$$, $$\mathcal{C}_j$$; and this behaves meaningfully under matrix multiplication. That is, for another direct sum $$L=\bigoplus_{k\in K} L_k$$ and basis $$\mathcal{D}=\bigcup \mathcal{D}_k$$, writing $$v:N \rightarrow L$$ in the same manner, the matrix representation of $$v\circ u$$ with respect to the bases $$\mathcal{B}, \mathcal{D}$$ is the matrix whose $$(k,i)$$-entry is the matrix

$$\sum_{j\in J}[v_{kj}]_{\mathcal{D}_k}^{\mathcal{C}_j}[u_{ji}]_{\mathcal{C}_j}^{\mathcal{B}_i}$$.
