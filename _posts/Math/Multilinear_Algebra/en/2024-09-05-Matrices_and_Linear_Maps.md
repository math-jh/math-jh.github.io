---title: "Matrices and Linear Maps"
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
translated_at: 2026-05-28T11:36:15+00:00
translation_source: kimi-cli
---
## Coordinate Representation

Now we examine the relationship between matrices and linear maps. This can be thought of as a generalization of [[Linear Algebra] §Fundamental Theorem of Linear Algebra, ⁋Theorem 5](/en/math/linear_algebra/ftla#thm5). For convenience,

let a free $$A$$-module $$M$$ be given, and fix a basis $$\mathcal{B}=(e_i)_{i\in I}$$ of $$M$$. Then any $$x\in M$$ can be written as

$$x=\sum_{i\in I} x_i e_i,\qquad x_i\in A$$

and the column vector $$(x_{i0})_{(i,0)\in I\times\{0\}}$$ consisting of the coefficients $$x_i$$ corresponding to the $$e_i$$ when expressed as such a linear combination is called the *coordinate representation with respect to $$\mathcal{B}$$* and is denoted by $$[x]_\mathcal{B}$$. On the other hand, it is also worth noting that using the coordinate form, we can write $$x_i$$ simply as the formula

$$x_i=\langle x,e_i^\ast\rangle\tag{1}$$

without complicated explanation. ([§Dual Spaces, ⁋Definition 6](/en/math/multilinear_algebra/dual_spaces#def6))

## Matrix Representation of Linear Maps

In the remainder of this post, we assume that two free $$A$$-modules $$M,N$$ are given, and fix their bases $$\mathcal{B}=(e_i)_{i\in I}$$, $$\mathcal{C}=(f_j)_{j\in J}$$.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> In the situation above, suppose any $$A$$-linear map $$u:M \rightarrow N$$ is given. Then the *matrix representation* of $$u$$ is the following matrix

$$[u]_\mathcal{C}^\mathcal{B}=(f_j^\ast(u(e_i)))_{(j,i)\in J\times I}=(\langle u(e_i), f_j^\ast\rangle)_{(j,i)\in J\times I}$$.

</div>

Then the following holds first.

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> The $$i$$-th column of the matrix representation $$[u]_\mathcal{C}^\mathcal{B}$$ of a linear map $$u:M \rightarrow N$$ is equal to the coordinate representation $$[u(e_i)]_\mathcal{C}$$ of $$u(e_i)$$ with respect to $$\mathcal{C}$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

By definition, the $$i$$-th column of $$[u]_\mathcal{C}^\mathcal{B}$$ is given by the following formula

$$(f_j^\ast(u(e_i)))_{j\in J}=(\langle u(e_i), f_j^\ast\rangle)_{j\in J}$$.

Now the $$j$$-th component of this column vector is, by the preceding formula (1), exactly the coefficient of $$f_j$$ when $$u(e_i)$$ is expressed as a linear combination with respect to the basis $$\mathcal{C}$$.

</details>

If another $$A$$-linear map $$v:M \rightarrow N$$ is given, we can verify that

$$[u+v]_\mathcal{C}^\mathcal{B}=[u]_\mathcal{C}^\mathcal{B}+[v]_\mathcal{C}^\mathcal{B}$$

holds. Also, if $$\alpha$$ is contained in the center of $$A$$, then $$\alpha u$$ is an $$A$$-linear map, and the matrix representation of this $$A$$-linear map is given by

$$[\alpha u]_\mathcal{C}^\mathcal{B}=\alpha[u]_\mathcal{C}^\mathcal{B}$$.

To summarize, $$u\mapsto [u]_\mathcal{C}^\mathcal{B}$$ is a $$Z(A)$$-module homomorphism from $$\Hom_{\lMod{A}}(M,N)$$ to $$\Mat_{J\times I}(A)$$. This $$Z(A)$$-linear map is injective, because $$u=0$$ and $$u(e_i)=0$$ for all $$i\in I$$ are equivalent. On the other hand, if $$J$$ is a finite set, then for any element $$(x_{ji})$$ of $$\Mat_{J\times I}(A)$$, we can define $$u\in\Hom_\lMod{A}$$ by the following formula

$$u(e_i)=\sum_{j\in J} \langle u(e_i),f_j^\ast\rangle f_j$$

to construct the inverse of the above $$Z(A)$$-linear map, so it becomes a $$Z(A)$$-isomorphism.

## Product of Matrix Representations

We previously examined how to define the product of two matrices. As with [[Linear Algebra] §Fundamental Theorem of Linear Algebra, ⁋Theorem 5](/en/math/linear_algebra/ftla#thm5), the product of these matrices corresponds to the composition of linear maps. Let us first prove the following proposition.

<div class="proposition" markdown="1">

<ins id="prop3">**Proposition 3**</ins> If $$I,J$$ are finite sets, then for any linear map $$u:M \rightarrow N$$ and $$x\in M$$, the following formula

$$[u(x)]_\mathcal{C}=[u]_\mathcal{C}^\mathcal{B}[x]_\mathcal{B}$$

holds.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

We can verify that the expression on the right-hand side yields a column vector, and then by formula (2) of [§Matrices, §§Matrix Multiplication](/en/math/multilinear_algebra/matrices#matrix-multiplication), the $$j$$-th component of the right-hand side expression is

$$\left([u]_\mathcal{C}^\mathcal{B}[x]_\mathcal{B}\right)_{j0}=\sum_{i\in I}\left([u]_\mathcal{C}^\mathcal{B}\right)_{ji}\left([x]_\mathcal{B}\right)_{i0}=\sum_{i\in I}\left\langle u(e_i),f_j^\ast\right\rangle \left\langle x,e_i^\ast\right\rangle$$.

On the other hand, examining the left-hand side, since $$x=\sum_{i\in I}x_i e_i$$, the $$j$$-th component of $$[u(x)]_\mathcal{C}$$ becomes

$$\langle u(x),f_j^\ast\rangle=\left\langle u\left(\sum_{i\in I} x_i e_i\right), f_j^\ast\right\rangle=\left\langle \sum_{i\in I} x_i u(e_i), f_j^\ast\right\rangle=\sum_{i\in I}x_i\langle u(e_i),f_j^\ast\rangle=\sum_{i\in I}\left\langle u(e_i),f_j^\ast\right\rangle \left\langle x,e_i^\ast\right\rangle$$

yielding the desired result.

</details>

Combining this with [Proposition 2](#prop2), we obtain the following result.

<div class="proposition" markdown="1">

<ins id="cor4">**Corollary 4**</ins> Suppose three $$A$$-modules $$M,N,L$$ are given, and fix finite bases $$\mathcal{B}=(e_i)_{i\in I},\mathcal{C}=(f_j)_{j\in J},\mathcal{D}=(g_k)_{k\in K}$$. Then for any linear maps $$u:M \rightarrow N$$, $$v:N \rightarrow L$$, the following formula

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

On the other hand, the transpose of a matrix also has a corresponding concept in linear maps.

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> If $$I,J$$ are finite sets, then for any linear map $$u:M \rightarrow N$$, the following formula

$$\left([u]_\mathcal{C}^\mathcal{B}\right)^t=\left[u^\ast\right]_{\mathcal{B}^\ast}^{\mathcal{C}^\ast}$$

holds. Here $$\mathcal{B}^\ast$$ and $$\mathcal{C}^\ast$$ are the dual bases of $$\mathcal{B},\mathcal{C}$$ respectively.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

By [§Dual Spaces, ⁋Proposition 8](/en/math/multilinear_algebra/dual_spaces#prop8), we may identify $$M$$ and $$M^{\ast\ast}$$, and then $$\mathcal{B}$$ corresponds to the dual basis $$\mathcal{B}^{\ast\ast}$$ of $$\mathcal{B}^\ast$$. Now

$$\left(\left[u^\ast\right]_{\mathcal{B}^\ast}^{\mathcal{C}^\ast}\right)_{ji}=\langle u^\ast(f_j^\ast), e_i^{\ast\ast}\rangle=\langle e_i, u^\ast(f^\ast)\rangle=\langle u(e_i), f_j^\ast\rangle=\left([u]_\mathcal{C}^\mathcal{B}\right)_{ij}=\left(\left([u]_\mathcal{C}^\mathcal{B}\right)^t\right)_{ji} $$

so we obtain the desired result.

</details>

## Matrix Representations and Trace

Previously we defined the trace of a linear map in [§Hom and Tensor Products, ⁋Definition 4](/en/math/multilinear_algebra/hom_and_tensor#def6). This time, for any $$n\times n$$ matrix $$X$$, let us define the trace of $$X$$ by the following formula

$$\tr(X)=\sum_{i=1}^n x_{ii}$$.

Then for any $$u\in\End_\rMod{A}(M)$$, fixing a basis $$\mathcal{B}=(e_i)_{1\leq i\leq n}$$ and considering $$[u]_\mathcal{B}^\mathcal{B}$$, we have

$$\tr([u]_\mathcal{B}^\mathcal{B})=\sum_{i=1}^n ([u]_\mathcal{B}^\mathcal{B})_{ii}=\sum_{i=1}^n\langle u(e_i), e_i^\ast\rangle$$.

On the other hand, for obvious reasons

$$u(x)=\sum_{i=1}^n \langle x, e_i^\ast\rangle u(e_i)$$

so we obtain $$\tr(u)=\tr([u]_\mathcal{B}^\mathcal{B})$$. From this, for $$X\in\Mat_{m\times n}(A)$$, $$Y\in\Mat_{n\times m}(A)$$

$$\tr(XY)=\tr(YX)$$

holds.

## Block Matrices

Finally, we consider the case where two free $$A$$-modules $$M,N$$ are each written as a direct sum of submodules

$$M=\bigoplus_{i\in I}M_i,\qquad N=\bigoplus_{j\in J} N_j$$.

In particular, if all the $$M_i$$, $$N_j$$ are equal to $$A$$, this is the same situation as above. Then any $$x$$ can be written uniquely in the form

$$x=\sum_{i\in I} x_i,\qquad x_i\in M_i$$

and we define the coordinate representation of $$x$$ with respect to this decomposition as

$$[x]_I=(x_{i0})_{i\in I}$$.

Also, for any $$A$$-linear map $$u: M \rightarrow N$$, writing

$$u(x_i)=\sum_{j\in J} u_{ji}(x_i),\qquad u_{ji}(x_i)\in N_j$$

the following matrix

$$[u]^I_J=(u_{ji})_{(j,i)\in J\times I}$$

is well-defined. This matrix can be thought of as a $$J\times I$$ matrix defined over the following ring

$$H=\bigoplus_{(j,i)\in J\times I}\Hom_{\lMod{A}}(M_i,N_j)$$.

Even with this generalization, we can verify that all the propositions examined above still hold as they are. In particular, the product of matrices is worth noting: suppose $$I,J$$ are both finite, and furthermore each $$M_i$$ and $$N_j$$ has finite bases $$\mathcal{B}_i$$, $$\mathcal{C}_j$$. Then the collections of all these bases form bases $$\mathcal{B},\mathcal{C}$$ of $$M$$ and $$N$$ respectively. Then representing a linear map $$u:M \rightarrow N$$ as a matrix with respect to this basis can be verified to be equal to the matrix obtained by substituting, for each component $$u_{ji}$$ in the above $$[u]_J^I$$, its matrix representation with respect to the bases $$\mathcal{B}_i$$, $$\mathcal{C}_j$$, and this behaves meaningfully with respect to matrix multiplication. That is, for another direct sum $$L=\bigoplus_{k\in K} L_k$$ and basis $$\mathcal{D}=\bigcup \mathcal{D}_k$$, writing $$v:N \rightarrow L$$ in the same way, the matrix representation of $$v\circ u$$ with respect to the bases $$\mathcal{B}, \mathcal{D}$$ becomes the matrix whose $$(k,i)$$-component is the matrix

$$\sum_{j\in J}[v_{kj}]_{\mathcal{D}_k}^{\mathcal{C}_j}[u_{ji}]_{\mathcal{C}_j}^{\mathcal{B}_i}$$.
