---
title: "Change of Basis"
description: "Change of basis deals with the process of transitioning from a given basis to another in finite-dimensional vector spaces, establishing the equivalence relation of bases and invertibility conditions for square matrices."
excerpt: "Square matrices, invertible matrices, and matrix transformations under change of basis"

categories: [Math / Multilinear Algebra]
permalink: /en/math/multilinear_algebra/change_of_basis
sidebar: 
    nav: "multilinear_algebra-en"

date: 2024-10-06
weight: 8
translated_at: 2026-09-25T15:15:06+00:00
translation_source: antigravity-gemini-3.8-flash-high
---
## Square Matrices

::: Definition 1
An $I\times I$ matrix is called a *square matrix*. We denote the collection of these matrices by $\Mat_I(A)$.
:::

In particular, when $I$ is a finite set and $A$ is commutative, $\Mat_{n}(A)$ has special properties: not only is this object an $A$-module, but it also has a multiplication defined on it. That is, $\Mat_{n}(A)$ is an $A$-algebra. 

::: Proposition 2
In this setting, $\Mat_n(A)$ is a unital associative algebra.
:::
::: Proof
That $\Mat_n(A)$ is an associative $A$-algebra was already verified in [§Matrices, §§Matrix Multiplication](/en/math/multilinear_algebra/matrices#matrix-multiplication){: data-lid="qpbzv" }. One can verify that the identity element for multiplication on $\Mat_n(A)$ is the following identity matrix:

$$I_n=\begin{pmatrix}1&0&\cdots&0\\0&1&\cdots&0\\\vdots&\vdots&\ddots&\vdots\\0&0&\cdots&1\end{pmatrix}$$
:::

$\Mat_n(A)$ has a canonical basis $(E_{ij})$; considering their structure constants, we can write the following relation:

$$E_{ij}E_{hk}=\delta_{jh}E_{ik}$$

::: Definition 3
Among the elements of $\Mat_n(A)$, the collection of those that have an inverse with respect to multiplication is denoted by $\GL_n(A)$. 
:::

For a free $A$-module $M$, fix a basis $\mathcal{B}=(e_i)_{i\in I}$, and let $\lvert I\rvert=n$. Then for any $u\in \End_{\lMod{A}}(M)$, we have $[u]_{\mathcal{B}}^\mathcal{B}\in\Mat_n(A)$, and if $u$ is an isomorphism, then $[u]_{\mathcal{B}}^\mathcal{B}\in\GL_n(A)$ by [§Matrices and Linear Maps, ⁋Corollary 4](/en/math/multilinear_algebra/matrices_and_linear_maps#cor4){: data-lid="98wrl" }. Then by [§Dual Spaces, ⁋Proposition 5](/en/math/multilinear_algebra/dual_spaces#prop5){: data-lid="oze3w" } and [§Matrices and Linear Maps, ⁋Proposition 5](/en/math/multilinear_algebra/matrices_and_linear_maps#prop5){: data-lid="rsngm" }, the equation

$$\bigl([u^{-1}]_{\mathcal{B}}^\mathcal{B}\bigr)^t=\bigl(\bigl[u^t\bigr]_{\mathcal{B}^\ast}^{\mathcal{B}^\ast}\bigr)^{-1}$$

holds. 

## Change of Basis

::: Proposition 4
Let an $A$-module $M$ and a finite basis of $M$, $\mathcal{B}=(e_i)_{i\in I}$, be given. Then the family

$$e_i'=\sum_{j=1}^n a_{ji}e_j,\qquad 1\leq i\leq n$$

is a basis of $M$ if and only if the square matrix $(a_{ji})$ is invertible.
:::
::: Proof
The given matrix $(a_{ji})$ is, via the formula

$$u:e_i\mapsto e_i'=\sum_{j=1}^n a_{ji}e_j$$

defining the linear map $u\in\End_{\lMod{A}}(M)$, precisely its matrix representation with respect to $\mathcal{B}$, given by $[u]_{\mathcal{B}}^\mathcal{B}\in\Mat_n(A)$. Now, this matrix having an inverse is equivalent to $u$ being an isomorphism, which in turn is equivalent to $(u(e_i))_{i\in I}$ being a basis of $M$. 
:::

Conversely to the above proof, the matrix $(a_{ji})$ can also be thought of as the matrix representation of the identity map $\id_M:M \rightarrow M$ with respect to two different bases. Let us write the basis $(e_i')$ as $\mathcal{B}'$. Then, since 

$$\id_M(e_i')=\sum_{j=1}^n a_{ji}e_j$$

, we have

$$([\id_M]^{\mathcal{B}'}_\mathcal{B})=(\langle \id_M(e_i'), e_j^\ast\rangle)_{(j,i)\in I\times I}=(a_{ji})_{(j,i)\in I\times I}$$

. From this perspective, this matrix is also called the *change-of-basis matrix* from $\mathcal{B}'$ to $\mathcal{B}$. 

More generally, the following holds.

::: Proposition 5
Let two $A$-modules $M,N$ and their respective finite bases $\mathcal{B}=(e_i)_{i\in I}$ and $\mathcal{C}=(f_j)_{j\in J}$ be given, and let $u:M \rightarrow N$ be an $A$-linear map. For other bases of $M$ and $N$, denoted by $\mathcal{B}'=(e_i')_{i\in I}$ and $\mathcal{C}'=(f_j')_{j\in J}$ respectively, the equation

$$[u]_{\mathcal{C}'}^{\mathcal{B}'}=[\id_N]^\mathcal{C}_{\mathcal{C}'}[u]^\mathcal{B}_\mathcal{C}[\id_M]^{\mathcal{B}'}_{\mathcal{B}}$$

holds.
:::

## Similar Matrices

::: Definition 6
Two $m\times n$ matrices $X, X'$ are said to be *equivalent* if there exist square matrices $P\in\GL_m(A)$ and $Q\in\GL_n(A)$ such that $X'=PXQ$. 
:::

In the same vein as the discussion preceding [Definition 6](#def6){: data-lid="uxnic" }, it is better to consider the following equivalence relation, which is finer than that of equivalent matrices.

::: Definition 7
Two $n\times n$ matrices $X, X'$ are said to be *similar* if there exists a square matrix $P\in\GL_n(A)$ such that $X'=PXP^{-1}$. 
:::

Then, setting $M=N$, $\mathcal{B}=\mathcal{C}$, and $\mathcal{B}'=\mathcal{C}'$ in [Proposition 5](#prop5){: data-lid="gde8w" } above, we see that for an element of $\End_{\lMod{A}}(M)$, $u$, its matrix representations with respect to different bases are similar to each other. 

---

**References**

**[Bou]** Bourbaki, N. Algebra I. *Elements of Mathematics*. Springer. 1998.
