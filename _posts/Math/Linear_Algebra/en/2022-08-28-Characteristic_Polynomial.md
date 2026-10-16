---
title: "Characteristic Polynomial"
description: "We define the characteristic polynomial of matrices and linear maps, and use it to introduce the concepts of eigenvalues and spectrum. We also show that the characteristic polynomial of a linear map is independent of the choice of basis, by using the fact that similar matrices have the same characteristic polynomial."
excerpt: "The characteristic polynomial of a matrix"

categories: [Math / Linear Algebra]
permalink: /en/math/linear_algebra/characteristic_polynomial
sidebar: 
    nav: "linear_algebra-en"


date: 2022-08-28

weight: 15
translated_at: 2026-06-01T01:00:05+00:00
translation_source: kimi-cli
last_polished_at: 2026-10-16T23:15:05+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
Now we examine the characteristic polynomial of a matrix and of a linear map, and through it define eigenvalues.

## Characteristic Polynomial and Eigenvalues

::: Definition 1
For any order-$n$ square matrix $A$, the *characteristic polynomial* of $A$ is defined as the polynomial in $\x$ given by $\det(\x I-A)$.
:::

From the formula

$$\det(\x I-A)=\sum_{\tau\in S_n}\sgn(\tau)(\x I-A)_{\tau(1),1}\cdots(\x I-A)_{\tau(n),n}\tag{1}$$

we see that the degree of the characteristic polynomial of $A$ is at most $n$. This is because each polynomial added on the right-hand side is a product of $n$ factors, where each $(\x I-A)_{\tau(k),k}$ is, only when $\tau(k)=k$, linear in $\x$, and constant otherwise. Hence, if the characteristic polynomial actually has degree $n$, we know that the degree-$n$ term *must* appear only when for every $k$ the relation $\tau(k)=k$ holds for $\tau$, that is, when $\tau=\id_{S_n}$. In this case, the corresponding term is

$$(\x I-A)_{1,1}\cdots(\x I-A)_{n,n}=(\x-A_{11})\cdots(\x-A_{nn})\tag{2}$$

and expanding this shows that the coefficient of $\x^n$ is $1$, so we see that the degree of the characteristic polynomial is always $n$.

If $\tau(i)\neq i$ holds for some $i$, then by the pigeonhole principle there must also exist another $j$ for which $\tau(j)\neq j$ holds. From this we see that among the terms added on the right-hand side of equation (1), there is no polynomial of degree $n-1$. That is, the degree-($n-1$) term of the characteristic polynomial must arise solely from equation (2), and in this case we see that its coefficient is

$$-(A_{1,1}+\cdots+A_{n,n})$$

Finally, let us find the constant term of the characteristic polynomial. For this purpose, it suffices to substitute $\x=0$ into the characteristic polynomial. Then the result is

$$\det(0I-A)=\det(-A)=(-1)^n\det(A)$$

Therefore we have proved the following proposition.

::: Proposition 2
The characteristic polynomial of an order-$n$ square matrix is always a polynomial of degree $n$; the coefficient of the degree-($n-1$) term of the characteristic polynomial equals $-\tr A$, and its constant term equals $(-1)^n\det A$.
:::

The roots of the characteristic polynomial provide important information when studying a matrix.

::: Definition 3
For an $n\times n$ matrix $A$, the roots of the characteristic polynomial of $A$, $\det(\x I-A)=0$, are called the *eigenvalues* of $A$. The collection of eigenvalues of $A$ is called the *spectrum* of $A$, and this set is denoted by $\Spec(A)$.
:::

Consider two similar $n\times n$ matrices $A,B$. Then from $A=PBP^{-1}$, we obtain

$$\det(\x I-A)=\det(\x I-PBP^{-1})=\det(P(\x I-B)P^{-1})=\det P\det(\x I-B)\det P^{-1}=\det(\x I-B)$$

Therefore, the characteristic polynomials of $A$ and $B$ are equal. From this we obtain the following corollaries.

::: Corollary 4
For any finite-dimensional vector space $V$ and linear map $L:V\rightarrow V$, defining the characteristic polynomial of $L$ as the characteristic polynomial of the matrix $[L]_\mathcal{B}^\mathcal{B}$ is well-defined.
:::
::: Proof
That is, we must show that for a basis of $V$, choosing instead of $\mathcal{B}$ another basis $\mathcal{C}$ does not change the characteristic polynomial of $L$. By the preceding argument, it suffices to observe from the formula after [\[Multilinear Algebra\] §Change of Basis, ⁋Proposition 5](/en/math/multilinear_algebra/change_of_basis#prop5){: data-lid="3xukk" } that the two matrix representations $[L]_\mathcal{B}^\mathcal{B}$ and $[L]_\mathcal{C}^\mathcal{C}$ are similar matrices.
:::

For convenience, all subsequent discussion will be phrased in terms of matrices, but by the above corollary we can prove the same results for any linear map $L$ as well.

::: Corollary 5
Similar matrices have the same trace and determinant.
:::
::: Proof
From the preceding argument we know that $A$ and $B$ have the same characteristic polynomial, and by [Proposition 2](#prop2){: data-lid="zij1p" } the trace and determinant of a matrix are determined by its characteristic polynomial.
:::

In particular, given any linear map $L:V\rightarrow V$, by decomposing $[L]_\mathcal{B}^\mathcal{B}$ via matrix diagonalization (which we will cover in the next post), we can decompose $V$ into the eigenspaces of $L$.

## Algebraic Multiplicity

Eigenvalues are all roots of the characteristic polynomial, but some eigenvalues may have greater multiplicity than others. This is defined as follows.

::: Definition 6
Suppose that in $\mathbb{K}[\x]$ we are given an arbitrary nonzero polynomial $p(\x)$, and let $a\in\mathbb{K}$ be a root of $p(\x)=0$. If $(\x-a)^k$ divides $p(\x)$ but $(\x-a)^{k+1}$ does not divide $p(\x)$, then the *multiplicity* of $a$ is defined to be $k$.
:::

Let the characteristic polynomial of an $n\times n$ matrix $A$ be $p_A(\x)$, and let $\lambda$ be an eigenvalue of $A$. Then, as a root of $p_A$, the multiplicity of $\lambda$ is called the *algebraic multiplicity* of $\lambda$. This terminology serves to distinguish it from the *geometric multiplicity*, which we will define shortly.

Suppose that in $\mathbb{K}[\x]$ an arbitrary element $p(\x)$ is given. If $p$ is a polynomial of degree $n$, then $p$ has at most $n$ roots. However, $p$ need not have exactly $n$ roots.

::: Example 7
For example, let $\mathbb{K}=\mathbb{R}$ and consider the $2\times 2$ square matrix

$$J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$$

Then the characteristic polynomial of $J$ is $\x^2+1$, and this polynomial has no roots in $\mathbb{R}$.
:::

A field in which this does not happen (that is, a field in which every nonconstant polynomial always has a root) is called an *algebraically closed field*. The following *Fundamental Theorem of Algebra* can be proved algebraically or through analysis, but since any approach is difficult at our current level, we accept it as fact and move on.

::: Theorem 8 (Fundamental Theorem of Algebra)
The set of complex numbers $\mathbb{C}$ is an algebraically closed field.
:::

The characteristic equation of the matrix $J$ in [Example 7](#ex7){: data-lid="fvymc" } above has no roots in $\mathbb{R}$, but has two roots in $\mathbb{C}$. Going forward, as in this case, it will be important to distinguish over which field the roots of a polynomial are defined.

## Eigenvectors and Geometric Multiplicity

Consider an $n\times n$ matrix $A$ and its eigenvalue $\lambda$. Then by definition the matrix $\lambda I-A$ is singular, and therefore

$$(\lambda I-A)v=0$$

is satisfied by some nonzero vector $v$.

::: Definition 9
For an $n\times n$ matrix $A$ and an eigenvalue $\lambda$, if $Av=\lambda v$ holds for a nonzero vector $v$, it is called an *eigenvector* corresponding to $\lambda$ for $A$.
:::

For a matrix $A$, let us gather all the eigenvectors corresponding to $\lambda$ together with the zero vector, and denote this set by $E_\lambda$. Then one can easily verify that $E_\lambda$ forms a vector space. This is called the *eigenspace* corresponding to $\lambda$. Since $E_\lambda$ always contains at least one nonzero vector, $\dim E_\lambda$ is always greater than $0$.

::: Definition 10
For an $n\times n$ matrix $A$ and an eigenvalue $\lambda$, the dimension of $E_\lambda$, $\dim E_\lambda$, is called the *geometric multiplicity* of $\lambda$.
:::



---

**References**

**[Goc]** M.S. Gockenbach, *Finite-dimensional linear algebra*, Discrete Mathematics and its applications, Taylor&Francis, 2011.

---
