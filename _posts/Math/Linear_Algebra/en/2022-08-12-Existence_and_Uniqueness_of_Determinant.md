---
title: "Existence and Uniqueness of the Determinant"
description: "Permutations of the symmetric group are classified into even and odd permutations, and the unique existence of the determinant is proven using the properties of alternating multilinear maps."
excerpt: "Existence, uniqueness proof, and computation methods of the determinant"

categories: [Math / Linear Algebra]
permalink: /en/math/linear_algebra/existence_and_uniqueness_of_determinant
sidebar: 
    nav: "linear_algebra-en"


date: 2022-08-12

weight: 14
translated_at: 2026-09-25T03:15:05+00:00
translation_source: antigravity-gemini-3.8-flash-high
---
In this post, we show that the determinant exists uniquely and examine how to compute it.

## Symmetric Groups

In this section, we define the symmetric group. We present the results introduced here without proofs, but if desired, the proofs can be found in [\[Group Theory\] §Symmetric Groups](/en/math/group_theory/symmetric_groups){: data-lid="6sup7" }.

::: Definition 1
The collection of all bijections from the set $\{1,\ldots, n\}$ to itself is called the *symmetric group*, and is denoted by $S_n$. An element of $S_n$ is called a *permutation*.
:::

The elements of $S_n$ form a group under function composition, where the identity element is $\id$ and the inverse of a function $\tau\in S_n$ is the inverse function $\tau^{-1}$.

Among the elements of $S_n$, the simplest after $\id$ are functions that pick two elements from $\{1,\ldots, n\}$ and swap their positions. For example, for $i,j\in \{1,\ldots, n\}$, the function defined by

$$\tau(k)=\begin{cases}i&\text{if $k=j$,}\\j&\text{if $k=i$,}\\k&\text{otherwise.}\end{cases}$$

is such a function. Such a function is called a *transposition*.

It is well known that every element of $S_n$ can always be expressed as a finite composition of transpositions. Suppose an arbitrary element $\tau\in S_n$ is given, and suppose two ways of expressing $\tau$ as a composition of transpositions are given as in

$$\tau=\upsilon_1\circ\upsilon_2\circ\cdots\circ\upsilon_k=\upsilon_1'\circ\upsilon_2'\circ\cdots\circ\upsilon_m'.$$

In general, $m$ and $k$ need not be equal, but whether $m,k$ are even or odd is always the same. If this number is even, we call $\tau$ an *even permutation*, and if it is odd, an *odd permutation*. Then we can define the function $\sgn:S_n\rightarrow\{-1,1\}$ by

$$\sgn(\tau)=\begin{cases}1&\text{if $\tau$ is even}\\-1&\text{if $\tau$ is odd}\end{cases}$$

This function is a group homomorphism. That is, for any $\tau,\tau'\in S_n$,

$$\sgn(\tau\circ\tau')=\sgn(\tau)\sgn(\tau')$$

holds.

Suppose an arbitrary alternating multilinear map $f:(\mathbb{K}^n)^n\rightarrow \mathbb{K}$ is given. Then by the definition of $\sgn$, we see that

$$f(v_1,v_2,\ldots, v_n)=\sgn(\tau)f(v_{\tau(1)},v_{\tau(2)},\ldots, v_{\tau(n)})$$

holds.

## Existence and Uniqueness of the Determinant

::: Lemma 2
There exists a unique function $D$ satisfying [§Determinant, ⁋Definition 4](/en/math/linear_algebra/determinant#def4){: data-lid="z5mif" }.
:::
::: Proof
Let $f$ be an alternating multilinear map. For any $v_1,\ldots, v_n\in \mathbb{K}^n$, if we write

$$v_i=v_1^ie_1+\cdots+v_n^ie_n,\qquad i=1,\ldots, n$$

then

$$\begin{aligned}f(v_1,\ldots, v_n)&=\sum_{i_1=1}^nv_{i_1}^1f(e_{i_1},v_2,\ldots, v_n)\\
&=\sum_{i_1,i_2=1}^n v_{i_1}^1v_{i_2}^2f(e_{i_1},e_{i_2},v_3,\ldots, v_n)\\&=\cdots\\&=\sum_{i_1,\ldots, i_n=1}^nv_{i_1}^1v_{i_2}^2\ldots v_{i_n}^nf(e_{i_1},\ldots, e_{i_n})\end{aligned}$$

holds. By [§Determinant, ⁋Proposition 3](/en/math/linear_algebra/determinant#prop3){: data-lid="zj3f0" }, if there are identical indices among $i_1,\ldots, i_n$, the value of $f(e_{i_1},\ldots,e_{i_n})$ is always 0, so the right-hand side becomes

$$f(v_1,\ldots, v_n)=\sum_{\tau\in S_n}v^1_{\tau(1)}v^2_{\tau(2)}\cdots v^n_{\tau(n)}f(e_{\tau(1)},\ldots, e_{\tau(n)})$$

By the property of $\sgn$ examined earlier, this is again equal to

$$f(v_1,\ldots, v_n)=\sum_{\tau\in S_n}\sgn(\tau)v^1_{\tau(1)}v^2_{\tau(2)}\cdots v^n_{\tau(n)}f(e_1,e_2,\ldots, e_n)\tag{1}$$

Therefore, if $D,D'$ are two functions satisfying the definition of the determinant, then since

$$D(e_1,\ldots, e_n)=D'(e_1,\ldots, e_n)=1$$

it follows from equation (1) that $D=D'$ must hold.

For existence, similarly motivated by equation (1), if we define

$$D(v_1,\ldots, v_n)=\sum_{\tau\in S_n}\sgn(\tau)v^1_{\tau(1)}v^2_{\tau(2)}\cdots v^n_{\tau(n)}$$

it suffices to show that $D$ is indeed an alternating multilinear map. Since this is simply repeating the above calculation in reverse, we omit it.
:::

Therefore, the determinant is well-defined, and we denote it by $\det$. In the course of proving the proposition above, we obtained a formula for the determinant $\det A$. That is, for a matrix $A$, if we denote its $i$-th column vector by $A_i$, then in $A_i$, the $j$-th component is equal to $A_{ji}$, and therefore

$$\det A=\sum_{\tau\in S_n}\sgn(\tau)A_{\tau(1)1}A_{\tau(2)2}\cdots A_{\tau(n)n}\tag{2}$$

holds. For example, in the case $n=2$, the two elements of $S_2$ are $\id$, and the function swapping $1$ and $2$, namely $\tau$, so the determinant is

$$\det A=\sum_{\tau\in S_n}\sgn(\tau)A_{\tau(1)1}A_{\tau(2)2}\cdots A_{\tau(n)n}=\sgn(\id)A_{11}A_{22}+\sgn(\tau)A_{21}A_{12}=A_{11}A_{22}-A_{21}A_{12}$$

In general, when $n$ is large, directly calculating the value of the determinant using this formula is cumbersome, but the above formula is very helpful when proving various properties of the determinant.

::: Corollary 3
For any matrix $A\in\Mat_n(\mathbb{K})$, we have $\det(A^t)=\det A$.
:::
::: Proof
First, for transpositions $\upsilon_i$, if $\tau=\upsilon_1\circ\ldots\upsilon_k$, then $\tau^{-1}=\upsilon_k^{-1}\circ\cdots\circ\upsilon_1^{-1}$, so $\sgn(\tau)=\sgn(\tau^{-1})$ always holds. Now, from the definition of $A^t$, we have $A_{ij}=(A^t)_{ji}$, and since

$$\det(A^t)=\sum_{\tau\in S_n}\sgn(\tau)A_{1\tau(1)}\cdots A_{n\tau(n)}=\sum_{\tau\in S_n}\sgn(\tau^{-1})A_{\tau^{-1}(1)1}\cdots A_{\tau^{-1}(n)n}$$

we obtain the desired result.
:::

Also, from the above equation, we see that the determinant preserves multiplication.

::: Lemma 4
For any matrices $A,B\in\Mat_n(\mathbb{K})$, we have $\det(AB)=\det(A)\det(B)$.
:::
::: Proof
For the matrix $AB$, the $i,j$-entry is obtained from the equation

$$(AB)_{ij}=\sum_{k=1}^nA_{ik}B_{kj}$$

Therefore, 

$$\begin{aligned}\det(AB)&=\det((AB)_1, (AB)_2,\ldots, (AB)_n)\\&=\sum_{\tau\in S_n}\sgn(\tau)(AB)_{\tau(1)1}(AB)_{\tau(2)2}\cdots(AB)_{\tau(n)n}\\&=\sum_{\tau\in S_n}\sgn(\tau)\left(\sum_{i_1=1}^nA_{\tau(1)i_1}B_{i_11}\right)\cdots\left(\sum_{i_n=1}^nA_{\tau(n)i_n}B_{i_nn}\right)\\&=\sum_{\tau\in S_n}\sum_{i_1,\ldots, i_n=1}^n\sgn(\tau)A_{\tau(1)i_1}\cdots A_{\tau(n)i_n}B_{i_11}\cdots B_{i_nn}\\&=\sum_{i_1,\ldots, i_n=1}^nB_{i_11}\cdots B_{i_nn}\left(\sum_{\tau\in S_n}\sgn(\tau)A_{\tau(1)i_1}\cdots A_{\tau(n)i_n}\right)\\&=\sum_{i_1,\ldots, i_n=1}^n\det(A_{i_1},\ldots, A_{i_n})B_{i_11}\cdots B_{i_nn}\end{aligned}$$

By [§Determinant, ⁋Proposition 3](/en/math/linear_algebra/determinant#prop3){: data-lid="1kgu4" }, if there are duplicate indices among $i_1,\ldots, i_n$, the value of $\det(A_{i_1},\ldots, A_{i_n})$ is always 0, so on the right-hand side of the above equation, only terms where $i_1,\ldots, i_n$ are distinct remain. Now, if we define $\upsilon\in S_n$ to be the element satisfying the equation

$$\upsilon(1)=i_1,\ldots, \upsilon(n)=i_n$$

the right-hand side of the above equation becomes

$$\sum_{\upsilon\in S_n}\sgn(\upsilon)\det(A)B_{\upsilon(1)1}\cdots B_{\upsilon(n)n}=\det(A)\det(B)$$

which completes the proof.
:::

In the previous post, we gave a geometric explanation that a matrix $A$ being invertible is equivalent to $\det A\neq 0$. Using the preceding [Lemma 4](#lem4){: data-lid="mh6o9" }, we can prove this rigorously.

::: Proposition 5
For any matrix $A\in\Mat_n(\mathbb{K})$, $\det A\neq 0$ is equivalent to $A$ being invertible.
:::
::: Proof
From [§Fundamental Theorem of Linear Algebra](/en/math/linear_algebra/ftla){: data-lid="ga49b" }, we know that $A$ being invertible is equivalent to the linear map defined by $A$, $L_A:\mathbb{K}^n\rightarrow \mathbb{K}^n$, being invertible. Since $\mathbb{K}^n$ is finite-dimensional, this is in turn equivalent to $L_A$ being surjective, which is equivalent to the basis of $\col(A)$, the column vectors $A_1,\ldots, A_n$, being linearly independent. If $A_1,\ldots, A_n$ are not linearly independent, then by [§Determinant, ⁋Proposition 3](/en/math/linear_algebra/determinant#prop3){: data-lid="zcri0" } we have $\det A=0$. That is, if $\det A\neq 0$, then $A$ is invertible.

Conversely, assume that $A$ is invertible. Then from the equation

$$1=\det(I)=\det(A^{-1}A)=\det(A^{-1})\det(A)\tag{3}$$

we see that $\det A\neq 0$.
:::

From equation (3) appearing in the proof of the above proposition, we obtain the following corollary.

::: Corollary 6
For an invertible matrix $A\in\Mat_n(\mathbb{K})$, we have $\det(A^{-1})=(\det A)^{-1}$.
:::

## Triangular Matrices and the Determinant

The formula examined above is inefficient because one must compute $n!$ numbers to find the determinant. However, in certain cases this formula applies usefully.

::: Definition 7
A matrix $A\in\Mat_n(\mathbb{K})$ is an *upper triangular matrix* if whenever $i>j$, we have $A_{ij}=0$. Similarly, if whenever $i < j$ we have $A_{ij}=0$, then $A$ is called a *lower triangular matrix*, and an upper or lower triangular matrix is called simply a *triangular matrix*.

Meanwhile, for a matrix $A$, the entries $A_{ii}$ are called the *diagonal entries* of $A$, and if whenever $i\neq j$ we have $A_{ij}=0$, then $A$ is called a *diagonal matrix*. 
:::

In particular, every $n\times n$ row echelon matrix is an upper triangular matrix. ([§Gaussian Elimination, ⁋Definition 4](/en/math/linear_algebra/Gaussian_elimination#def4){: data-lid="bogif" })

::: Proposition 8
For any triangular matrix $A$, $\det(A)$ is equal to the product of its diagonal entries.
:::
::: Proof
Let us look again at the formula for the determinant examined above:

$$\det A=\sum_{\tau\in S_n}\sgn(\tau)A_{\tau(1)1}A_{\tau(2)2}\cdots A_{\tau(n)n}$$

For any $\tau\in S_n$, since $\tau$ is a bijection, if $\tau(i)>i$ for some $i$, then necessarily $\tau(j)<j$ for some $j$. Therefore, the terms summed in the above expression are always 0 except when $\tau=\id$. 
:::

By [§Gaussian Elimination](/en/math/linear_algebra/Gaussian_elimination){: data-lid="kek14" }, any matrix can be transformed into a row echelon form by repeatedly applying elementary row operations. Since every row echelon form is an upper triangular matrix, the proposition above makes it very easy to compute the determinant of the row echelon form obtained in this way. On the other hand, applying elementary row operations is equivalent to multiplying by elementary matrices. Therefore, if starting from a matrix $A$, we repeatedly apply elementary row operations $E_1,\ldots, E_k$ to obtain a row echelon form $A'$, then since

$$A'=E_kE_{k-1}\cdots E_1 A$$

we have 

$$\det(A')=\det(E_k)\det(E_{k-1})\cdots\det(E_1)\det(A)$$

Thus, let us examine the determinants of the elementary matrices $E_{i,j}$, $E'_{i,r}$, and $E''_{i,j,r}$. First, in the case of $E_{i,j}$ and $E'_{i,r}$, from the definition of the determinant it is easy to see that 

$$\det E_{i,j}=-1,\quad \det E'_{i,r}=r$$

Moreover, $E''_{i,j,r}$ is always a triangular matrix, and since the product of its diagonal entries is 1, we have $\det E''_{i,j,r}=1$. 

## Determinant of a Block Matrix

Meanwhile, using formula (2) for the determinant, we can also compute the determinant of a block matrix. 

::: Proposition 9
Let $A\in\Mat_k(\mathbb{K})$, and let $I$ be the $l\times l$ identity matrix. Then the determinant of the block matrix

$$\begin{pmatrix}A&O\\O&I\end{pmatrix}$$

is equal to $\det A$.
:::
::: Proof
The proof is almost identical to that of [Proposition 8](#prop8){: data-lid="dbzx9" }. Computing the determinant of the given matrix using equation (2), we have

$$\det \begin{pmatrix}A&O\\O&I\end{pmatrix}=\sum_{\tau\in S_{k+l}}\sgn(\tau)A_{\tau(1)1}A_{\tau(2)2}\cdots A_{\tau(k)k}B_{\tau(k+1)(k+1)}\cdots B_{\tau(k+l)(k+l)}$$

Here, $B_{k+i}$ is the element having only its $(k+i)$-th component equal to $1$ and all other components equal to $0$ in $\mathbb{K}^{k+l}$. Then, unless

$$\tau(k+1)=k+1,\ldots,\tau(k+l)=k+l$$

holds, the terms added on the right-hand side are always 0; therefore, with the last $l$ elements fixed, we only need to compute the sum over $\tau$. That is, the determinant of the given matrix becomes exactly identical to equation (2), and thus the proposition holds. 
:::

::: Corollary 10
For $A\in\Mat_k(\mathbb{K}),B\in\Mat_l(\mathbb{K}), C\in\Mat_{l\times k}(\mathbb{K})$, the determinant of the block matrix

$$\begin{pmatrix}A&O\\C&B\end{pmatrix}$$

is equal to $\det A\det B$.
:::
::: Proof
This is immediate from the identity

$$\begin{pmatrix}A&O\\C&B\end{pmatrix}=\begin{pmatrix}A&O\\O&I\end{pmatrix}\begin{pmatrix}I&O\\C&I\end{pmatrix}\begin{pmatrix}I&O\\O&B\end{pmatrix}$$

along with [Proposition 9](#prop9){: data-lid="l13qf" } and [Lemma 4](#lem4){: data-lid="ausxq" }. The middle matrix is a lower triangular matrix whose diagonal entries are all 1, so its determinant is 1 by [Proposition 8](#prop8){: data-lid="283r5" }. For the last matrix, performing $l$ row swaps followed by $l$ column swaps results in $2l$ sign changes, so the determinant of the given matrix becomes equal to $\det B$.
:::

We can extend the above results inductively without difficulty. That is,

$$\det\begin{pmatrix}A_{11}&A_{12}&\cdots&A_{1n}\\O&A_{22}&\cdots&A_{2n}\\\vdots&\vdots&\ddots&\vdots\\O&O&\cdots&A_{nn}\end{pmatrix}=\det A_{11}\det A_{22}\cdots\det A_{nn}$$

holds. However, when expressed as a block matrix, if it is not triangular, a similar result does *not* hold. For example, for the block matrix

$$\begin{pmatrix}A&B\\C&D\end{pmatrix}$$

the value of its determinant is generally different from $\det A\det D-\det B\det C$.


## Laplace Expansion

Given an order-$n$ square matrix $A$, one of the easiest ways to compute the determinant of $A$ is to use the Laplace expansion, which we introduce now. For this, we need a definition.

::: Definition 11
Let a matrix $A\in\Mat_n(\mathbb{K})$ be given. For $1\leq i,j\leq n$, $A^{(i,j)}$ is the square matrix obtained from the matrix $A$ by deleting the $i$-th row and the $j$-th column, of order $(n-1)$.  
:::

The Laplace expansion expresses the determinant of $A$ in terms of the $\det A^{(i,j)}$. 

::: Theorem 12
For any matrix $A\in\Mat_n(\mathbb{K})$ and any $1\leq i\leq n$, the identity

$$\det A=\sum_{j=1}^n(-1)^{i+j}A_{ij}\det (A^{(i,j)})$$

holds.
:::
::: Proof
First, fix $i,j$. Starting from $A$, replace all entries in the $i$-th row with $0$ while leaving only the $j$-th entry, and let this matrix be $B_j$. After that, swap rows $i-1$ times to move the $i$-th row to the first row, and swap columns $j-1$ times to move the $j$-th column to the first column, and let this matrix be $B_j'$. Then

$$B_j'=\begin{pmatrix}A_{ij}&0&\cdots&0\\A_{1j}&&&\\\vdots&&A^{(i,j)}&\\A_{nj}&&&\end{pmatrix}$$

Now by [Corollary 10](#cor10){: data-lid="zo1sz" }, the determinant of this matrix is equal to $A_{ij}\det A^{(i,j)}$, and hence

$$\det B_j=(-1)^{i+j-2}\det B_j'=(-1)^{i+j-2}A_{ij}\det A^{(i,j)}=(-1)^{i+j}A_{ij}\det A^{(i,j)}$$

On the other hand, by [Corollary 3](#cor3){: data-lid="k303y" }, the determinant is also multilinear with respect to rows; using multilinearity with respect to the $i$-th row, the sum of the determinants of the $B_j$ is equal to the determinant of $A$, so we obtain the desired identity:

$$\det A=\sum_{j=1}^n\det B_j=\sum_{j=1}^n (-1)^{i+j}A_{ij}\det A^{(i,j)}$$
:::

---

**References**

**[Goc]** M.S. Gockenbach, *Finite-dimensional linear algebra*, Discrete Mathematics and its applications, Taylor&Francis, 2011.

---
