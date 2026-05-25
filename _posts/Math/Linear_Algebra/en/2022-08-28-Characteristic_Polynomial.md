---
title: "Characteristic Polynomial"
excerpt: "The characteristic polynomial of a matrix"

categories: [Math / Linear Algebra]
permalink: /en/math/linear_algebra/characteristic_polynomial
sidebar: 
    nav: "linear_algebra-en"

header:
    overlay_image: /assets/images/Math/Linear_Agebra/Characteristic_Polynomial.png
    overlay_filter: 0.5

date: 2022-08-28
last_modified_at: 2022-08-29

weight: 15
translated_at: 2026-05-25T09:30:03+00:00
translation_source: kimi-cli
---
Now we examine the characteristic polynomial of matrices and linear maps, and through this we define eigenvalues.

## Characteristic Polynomial and Eigenvalues

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> For any $n\times n$ square matrix $A$, we define the *characteristic polynomial* of $A$ as the polynomial in $x$ given by $\det(x I-A)$.

</div>

From the formula

$$\det(x I-A)=\sum_{\tau\in S_n}\sgn(\tau)(x I-A)_{\tau(1),1}\cdots(x I-A)_{\tau(n),n}\tag{1}$$

we can see that the degree of the characteristic polynomial of $A$ is at most $n$. This is because each summand on the right-hand side is a product of $n$ terms, and each $(x I-A)_{\tau(k),k}$ is linear in $x$ only when $\tau(k)=k$, and constant otherwise. From this, if the characteristic polynomial is actually of degree $n$, we know that the degree-$n$ term must *necessarily* appear only when $\tau(k)=k$ for all $k$, that is, when $\tau=\id_{S_n}$. In this case, the corresponding term becomes

$$(x I-A)_{1,1}\cdots(x I-A)_{n,n}=(x-A_{11})\cdots(x-A_{nn})\tag{2}$$

and expanding this shows that the coefficient of $x$ is $1$, so we can conclude that the degree of the characteristic polynomial is always $n$.

If there exists an $i$ such that $\tau(i)\neq i$, then by the pigeonhole principle there must also exist another $j$ such that $\tau(j)\neq j$. From this we see that there are no terms of degree $n-1$ among the summands on the right-hand side of (1). That is, the degree-$(n-1)$ term of the characteristic polynomial arises only from (2), and its coefficient is

$$-(A_{1,1}+\cdots+A_{n,n})$$

Finally, let us find the constant term of the characteristic polynomial. To do this, we simply substitute $x=0$ into the characteristic polynomial. Then the result is

$$\det(0I-A)=\det(-A)=(-1)^n\det(A)$$

Thus we have proved the following proposition.

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> The characteristic polynomial of an $n\times n$ square matrix is always a polynomial of degree $n$, the coefficient of the degree-$(n-1)$ term is $-\tr A$, and the constant term is $(-1)^n\det A$.

</div>

The roots of the characteristic polynomial provide important information when studying matrices.

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> For an $n\times n$ matrix $A$, we call the solutions of $A$'s characteristic equation $\det(x I-A)=0$ the *eigenvalues* of $A$. The set of eigenvalues of $A$ is called the *spectrum* of $A$, and is denoted $\Spec(A)$.

</div>

Consider two similar $n\times n$ matrices $A$ and $B$. Then from $A=PBP^{-1}$ we obtain

$$\det(x I-A)=\det(x I-PBP^{-1})=\det(P(x I-B)P^{-1})=\det P\det(x I-B)\det P^{-1}=\det(x I-B)$$

Thus $A$ and $B$ have the same characteristic polynomial. From this we obtain the following corollaries.

<div class="proposition" markdown="1">

<ins id="cor4">**Corollary 4**</ins> For any linear map $L:V\rightarrow V$, defining the characteristic polynomial of $L$ as the characteristic polynomial of the matrix $[L]_\mathcal{B}^\mathcal{B}$ is well-defined.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

That is, we must show that the characteristic polynomial of $L$ does not change even if we choose a basis $\mathcal{C}$ of $V$ instead of $\mathcal{B}$. By the preceding argument, it suffices to observe from the equation after [§Change of Basis, ⁋Definition 2](/en/math/multilinear_algebra/change_of_basis#def2) that the two matrix representations $[L]_\mathcal{B}^\mathcal{B}$ and $[L]_\mathcal{C}^\mathcal{C}$ are similar matrices.

</details>

For convenience, all subsequent discussion will be unified as being about matrices, but through the above corollary we can prove the same content for any linear map $L$ as well.

<div class="proposition" markdown="1">

<ins id="cor5">**Corollary 5**</ins> Similar matrices have the same trace and determinant.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

From the preceding argument we know that $A$ and $B$ have the same characteristic polynomial, and from [Proposition 2](#prop2) the trace and determinant of a matrix are determined by its characteristic polynomial.

</details>

In particular, when an arbitrary linear map $L:V\rightarrow V$ is given, by diagonalizing $[L]_\mathcal{B}^\mathcal{B}$ through matrix diagonalization, which we will cover in the next post, we can decompose $V$ into eigenspaces of $L$.

## Algebraic Multiplicity

Although all eigenvalues are roots of the characteristic polynomial, some eigenvalues may have greater multiplicity than others. This is defined as follows.

<div class="definition" markdown="1">

<ins id="def6">**Definition 6**</ins> Let $p(x)$ be an arbitrary polynomial in $\mathbb{K}[x]$, and let $a\in\mathbb{K}$ be a root of $p(x)=0$. If $(x-a)^k$ divides $p(x)$ but $(x-a)^{k+1}$ does not divide $p(x)$, then we define the *multiplicity* of $a$ as $k$.

</div>

Let $p_A(x)$ be the characteristic polynomial of an $n\times n$ matrix $A$, and let $\lambda$ be an eigenvalue of $A$. Then the multiplicity of $\lambda$ as a root of $p_A$ is called the *algebraic multiplicity* of $\lambda$. This terminology serves to distinguish it from the *geometric multiplicity*, which we will define shortly.

Let $p(x)$ be an arbitrary element of $\mathbb{K}[x]$. If $p$ is a polynomial of degree $n$, then $p$ has at most $n$ roots. However, $p$ need not have exactly $n$ roots.

<div class="example" markdown="1">

<ins id="ex7">**Example 7**</ins> For example, let $\mathbb{K}=\mathbb{R}$ and consider the $2\times 2$ matrix

$$J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$$

Then the characteristic polynomial of $J$ is $x^2+1$, and this polynomial has no roots in $\mathbb{R}$.

</div>

A field in which this does not happen is called an *algebraically closed field*. The following *fundamental theorem of algebra* can be proved algebraically or through analysis, but either way is beyond our current level, so we accept it as a fact and move on.

<div class="proposition" markdown="1">

<ins id="thm8">**Theorem 8 (Fundamental Theorem of Algebra)**</ins> The set of complex numbers $\mathbb{C}$ is an algebraically closed field.

</div>

The characteristic equation of the matrix $J$ in [Example 7](#ex7) above has no solutions in $\mathbb{R}$, but has two solutions in $\mathbb{C}$. Going forward, it will be important to distinguish over which field the roots of a polynomial are defined.

## Eigenvectors and Geometric Multiplicity

Consider an $n\times n$ matrix $A$ and its eigenvalue $\lambda$. Then by definition the matrix $\lambda I-A$ is singular, and therefore there exists a non-zero vector $v$ satisfying

$$(\lambda I-A)v=0$$

<div class="definition" markdown="1">

<ins id="def9">**Definition 9**</ins> For an $n\times n$ matrix $A$ and an eigenvalue $\lambda$, a vector $v$ satisfying $Av=\lambda v$ is called an *eigenvector* of $A$ corresponding to $\lambda$.

</div>

For a matrix $A$, let us collect all eigenvectors corresponding to $\lambda$ and denote this set by $E_\lambda$. Then one can easily verify that $E_\lambda$ forms a vector space. This is called the *eigenspace* corresponding to $\lambda$. Since $E_\lambda$ always contains at least one non-zero vector, $\dim E_\lambda$ is always greater than $0$.

<div class="definition" markdown="1">

<ins id="def10">**Definition 10**</ins> For an $n\times n$ matrix $A$ and an eigenvalue $\lambda$, the dimension $\dim E_\lambda$ of $E_\lambda$ is called the *geometric multiplicity* of $\lambda$.

</div>

---

**References**

**[Goc]** M.S. Gockenbach, *Finite-dimensional linear algebra*, Discrete Mathematics and its applications, Taylor&Francis, 2011.

---
