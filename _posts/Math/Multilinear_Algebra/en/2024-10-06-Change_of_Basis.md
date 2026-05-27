---
title: "Change of Basis"
excerpt: "Square matrices and invertible matrices, transformation of matrices under change of basis"

categories: [Math / Multilinear Algebra]
permalink: /en/math/multilinear_algebra/change_of_basis
header:
    overlay_image: /assets/images/Math/Multilinear_Algebra/Change_of_Basis.png
    overlay_filter: 0.5
sidebar: 
    nav: "multilinear_algebra-en"

date: 2024-10-06
last_modified_at: 2024-10-06
weight: 8
translated_at: 2026-05-28T11:36:15+00:00
translation_source: kimi-cli
---
## Square Matrices

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> An $$I\times I$$ matrix is called a *square matrix*. Their collection is denoted $$\Mat_I(A)$$.

</div>

In particular, when $$I$$ is a finite set and $$A$$ is commutative, $$\Mat_{n}(A)$$ has special properties: this object is not only an $$A$$-module but also carries a multiplication defined on it. That is, $$\Mat_{n}(A)$$ is an $$A$$-algebra.

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> In this situation, $$\Mat_n(A)$$ is a unital associative algebra.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

That $$\Mat_n(A)$$ is an associative $$A$$-algebra is obvious from [§Matrices, §§Matrix Multiplication](/en/math/multilinear_algebra/matrices#matrix-multiplication). We can verify that the identity element for multiplication in $$\Mat_n(A)$$ is the identity matrix

$$I_n=\begin{pmatrix}1&0&\cdots&0\\0&1&\cdots&0\\\vdots&\vdots&\ddots&\vdots\\0&0&\cdots&1\end{pmatrix}$$

</details>

$$M_n(A)$$ has the canonical basis $$(E_{ij})$$, and considering the structure constants for these gives the expression

$$E_{ij}E_{jk}=\delta_{jh}E_{ik}$$

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> Among the elements of $$\Mat_n(A)$$, those for which a multiplicative inverse exists are collected and denoted $$\GL_n(A)$$.

</div>

Fix a basis $$\mathcal{B}=(e_i)_{i\in I}$$ of a free $$A$$-module $$M$$, and let $$\lvert I\rvert=n$$. Then for any $$u\in \End_{\lMod{A}}(M)$$, we have $$\[u\]_{\mathcal{B}}^\mathcal{B}\in\Mat_n(A)$$, and if $$u$$ is an isomorphism then by [§Matrices and Linear Maps, ⁋Corollary 4](/en/math/multilinear_algebra/matrices_and_linear_maps#cor4) we have $$\[u\]_{\mathcal{B}}^\mathcal{B}\in\GL_n(A)$$. Then by [§Dual Spaces, ⁋Proposition 5](/en/math/multilinear_algebra/dual_spaces#prop5) and [§Matrices and Linear Maps, ⁋Proposition 5](/en/math/multilinear_algebra/matrices_and_linear_maps#prop5), the following formula

$$\bigl([u^{-1}]_{\mathcal{B}}^\mathcal{B}\bigr)^t=\bigl(\bigl[u^\ast\bigr]_{\mathcal{B}^\ast}^{\mathcal{B}^\ast}\bigr)^{-1}$$

holds.

## Change of Basis

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4**</ins> Let an arbitrary $$A$$-module $$M$$ and a finite basis $$\mathcal{B}=(e_i)_{i\in I}$$ of $$M$$ be given. Then the following formula

$$e_i'=\sum_{j=1}^n a_{ji}e_i,\qquad 1\leq i\leq n$$

giving a basis of $$M$$ is equivalent to the existence of an inverse matrix for the square matrix $$(a_{ji})$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

The given matrix $$(a_{ji})$$ is simply the matrix representation $$\[u\]_{\mathcal{B}}^\mathcal{B}\in\Mat_n(A)$$ with respect to $$\mathcal{B}$$ of the linear map $$u\in\End_{\lMod{A}}(M)$$ defined by

$$u:e_i\mapsto e_i'=\sum_{j=1}^n a_{ji}e_i$$

Now, this matrix having an inverse is equivalent to $$u$$ being an isomorphism, which is in turn equivalent to $$(u(e_i))_{i\in I}$$ being a basis of $$M$$.

</details>

Conversely to the above proof, we may also think of the matrix $$(a_{ji})$$ as the matrix representation of the identity map $$\id_M:M \rightarrow M$$ with respect to different bases. Let us write the basis $$(e_i')$$ as $$\mathcal{B}'$$. Then

$$\id_M(e_i')=\sum_{j=1}^n a_{ji}e_i$$

so

$$([\id_M]^{\mathcal{B}'}_\mathcal{B})=(\langle \id_M(e_i'), e_j^\ast\rangle)_{(j,i)\in J\times I}=(a_{ji})_{(j,i)\in J\times I}$$

From this perspective, this matrix is also called the *change-of-basis matrix* from $$\mathcal{B}'$$ to $$\mathcal{B}$$.

More generally, the following holds.

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> Let two $$A$$-modules $$M,N$$ and their finite bases $$\mathcal{B}=(e_i)_{i\in I}$$, $$\mathcal{C}=(f_j)_{j\in J}$$ be given. For other bases $$\mathcal{B}'=(e_i')_{i\in I}$$ of $$M$$ and $$\mathcal{C}'=(f_j')_{j\in J}$$ of $$N$$, the following formula

$$[u]_{\mathcal{C}'}^{\mathcal{B}'}=[\id_N]^\mathcal{C}_{\mathcal{C}'}[u]^\mathcal{B}_\mathcal{C}[\id_M]^{\mathcal{B}'}_{\mathcal{B}}$$

holds.

</div>

## Similar Matrices

<div class="definition" markdown="1">

<ins id="def6">**Definition 6**</ins> Two $$m\times n$$ matrices $$X, X'$$ are called *equivalent* if there exist square matrices $$P\in\GL_m(A)$$ and $$Q\in\GL_n(A)$$ such that $$X'=PXQ$$.

</div>

In the same context as the discussion before [[Basic Linear Algebra] §Change of Basis, ⁋Definition 2](/en/math/multilinear_algebra/change_of_basis#def2), it is better to consider the following finer equivalence relation than equivalent matrices.

<div class="definition" markdown="1">

<ins id="def7">**Definition 7**</ins> Two $$n\times n$$ matrices $$X, X'$$ are called *similar* if there exists a square matrix $$P\in\GL_n(A)$$ such that $$X'=PXP^{-1}$$.

</div>

Then, setting $$M=N$$, $$\mathcal{B}=\mathcal{C}$$, and $$\mathcal{B}'=\mathcal{C}'$$ in [Proposition 5](#prop5) above, we see that the matrix representations of an element $$u$$ of $$\End_\rMod{A}(M)$$ with respect to different bases are similar to each other.
