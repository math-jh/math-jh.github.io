---
title: "Change of Basis"
description: "A change of basis transforms one basis of a finite-dimensional vector space into another, and it relies on the invertibility of square matrices to establish equivalence between bases."
excerpt: "Square matrices and invertible matrices, transformation of matrices under change of basis"

categories: [Math / Multilinear Algebra]
permalink: /en/math/multilinear_algebra/change_of_basis
sidebar: 
    nav: "multilinear_algebra-en"

date: 2024-10-06
last_modified_at: 2024-10-06
weight: 8
translated_at: 2026-06-01T18:00:06+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-01T18:00:06+00:00
---
## Square Matrices

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> An $$I\times I$$ matrix is called a *square matrix*. We denote the collection of all such matrices by $$\Mat_I(A)$$.

</div>

In particular, when $$I$$ is finite and $$A$$ is commutative, $$\Mat_{n}(A)$$ has additional structure: it is not merely an $$A$$-module, but also carries a multiplication. That is, $$\Mat_{n}(A)$$ is an $$A$$-algebra.

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> In this situation, $$\Mat_n(A)$$ is a unital associative algebra.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

That $$\Mat_n(A)$$ is an associative $$A$$-algebra follows immediately from [§Matrices, §§Matrix Multiplication](/en/math/multilinear_algebra/matrices#matrix-multiplication). The identity element for multiplication in $$\Mat_n(A)$$ is the identity matrix

$$I_n=\begin{pmatrix}1&0&\cdots&0\\0&1&\cdots&0\\\vdots&\vdots&\ddots&\vdots\\0&0&\cdots&1\end{pmatrix}$$

as is readily verified.

</details>

$$M_n(A)$$ has the canonical basis $$(E_{ij})$$, and the structure constants with respect to this basis are given by

$$E_{ij}E_{jk}=\delta_{jh}E_{ik}$$

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> We denote by $$\GL_n(A)$$ the subset of $$\Mat_n(A)$$ consisting of those elements that admit a multiplicative inverse.

</div>

Fix a basis $$\mathcal{B}=(e_i)_{i\in I}$$ of a free $$A$$-module $$M$$, and let $$\lvert I\rvert=n$$. Then for any $$u\in \End_{\lMod{A}}(M)$$, we have $$[u]_{\mathcal{B}}^\mathcal{B}\in\Mat_n(A)$$; moreover, if $$u$$ is an isomorphism, then by [§Matrices and Linear Maps, ⁋Corollary 4](/en/math/multilinear_algebra/matrices_and_linear_maps#cor4) we have $$[u]_{\mathcal{B}}^\mathcal{B}\in\GL_n(A)$$. In this case, [§Dual Spaces, ⁋Proposition 5](/en/math/multilinear_algebra/dual_spaces#prop5) and [§Matrices and Linear Maps, ⁋Proposition 5](/en/math/multilinear_algebra/matrices_and_linear_maps#prop5) yield the identity

$$\bigl([u^{-1}]_{\mathcal{B}}^\mathcal{B}\bigr)^t=\bigl(\bigl[u^\ast\bigr]_{\mathcal{B}^\ast}^{\mathcal{B}^\ast}\bigr)^{-1}$$

## Change of Basis

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4**</ins> Let $$M$$ be an arbitrary $$A$$-module and let $$\mathcal{B}=(e_i)_{i\in I}$$ be a finite basis of $$M$$. Then the formula

$$e_i'=\sum_{j=1}^n a_{ji}e_i,\qquad 1\leq i\leq n$$

defines a basis of $$M$$ if and only if the square matrix $$(a_{ji})$$ is invertible.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

The given matrix $$(a_{ji})$$ is precisely the matrix representation $$[u]_{\mathcal{B}}^\mathcal{B}\in\Mat_n(A)$$ with respect to $$\mathcal{B}$$ of the linear map $$u\in\End_{\lMod{A}}(M)$$ defined by

$$u:e_i\mapsto e_i'=\sum_{j=1}^n a_{ji}e_i$$

This matrix is invertible if and only if $$u$$ is an isomorphism, which in turn holds if and only if $$(u(e_i))_{i\in I}$$ is a basis of $$M$$.

</details>

Conversely, we may also regard the matrix $$(a_{ji})$$ as the matrix representation of the identity map $$\id_M:M \rightarrow M$$ with respect to different bases. Write the basis $$(e_i')$$ as $$\mathcal{B}'$$. Then

$$\id_M(e_i')=\sum_{j=1}^n a_{ji}e_i$$

and thus

$$([\id_M]^{\mathcal{B}'}_\mathcal{B})=(\langle \id_M(e_i'), e_j^\ast\rangle)_{(j,i)\in J\times I}=(a_{ji})_{(j,i)\in J\times I}$$

From this perspective, this matrix is also called the *change-of-basis matrix* from $$\mathcal{B}'$$ to $$\mathcal{B}$$.

More generally, we have the following.

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> Let $$M$$ and $$N$$ be $$A$$-modules with finite bases $$\mathcal{B}=(e_i)_{i\in I}$$ and $$\mathcal{C}=(f_j)_{j\in J}$$, respectively. For other bases $$\mathcal{B}'=(e_i')_{i\in I}$$ of $$M$$ and $$\mathcal{C}'=(f_j')_{j\in J}$$ of $$N$$, the formula

$$[u]_{\mathcal{C}'}^{\mathcal{B}'}=[\id_N]^\mathcal{C}_{\mathcal{C}'}[u]^\mathcal{B}_\mathcal{C}[\id_M]^{\mathcal{B}'}_{\mathcal{B}}$$

holds.

</div>

## Similar Matrices

<div class="definition" markdown="1">

<ins id="def6">**Definition 6**</ins> Two $$m\times n$$ matrices $$X, X'$$ are called *equivalent* if there exist square matrices $$P\in\GL_m(A)$$ and $$Q\in\GL_n(A)$$ such that $$X'=PXQ$$.

</div>

In the same context as the discussion preceding [§Change of Basis, ⁋Definition 6](/en/math/multilinear_algebra/change_of_basis#def6), it is preferable to consider the following finer equivalence relation rather than mere equivalence of matrices.

<div class="definition" markdown="1">

<ins id="def7">**Definition 7**</ins> Two $$n\times n$$ matrices $$X, X'$$ are called *similar* if there exists a square matrix $$P\in\GL_n(A)$$ such that $$X'=PXP^{-1}$$.

</div>

Then, setting $$M=N$$, $$\mathcal{B}=\mathcal{C}$$, and $$\mathcal{B}'=\mathcal{C}'$$ in [Proposition 5](#prop5) above, we see that the matrix representations of an element $$u\in\End_\rMod{A}(M)$$ with respect to different bases are similar to one another.
