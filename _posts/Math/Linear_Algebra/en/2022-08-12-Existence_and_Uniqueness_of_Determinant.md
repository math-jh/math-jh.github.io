---
title: "Existence and Uniqueness of the Determinant"
excerpt: "Existence and uniqueness of the determinant, proofs, and computational methods"

categories: [Math / Linear Algebra]
permalink: /en/math/linear_algebra/existence_and_uniqueness_of_determinant
sidebar: 
    nav: "linear_algebra-en"

header:
    overlay_image: /assets/images/Math/Linear_Algebra/Existence_and_Uniqueness_of_Determinant.png
    overlay_filter: 0.5

date: 2022-08-12
last_modified_at: 2022-08-12

weight: 14
translated_at: 2026-05-21T07:00:02+00:00
translation_source: kimi-cli
---
In this post we show that the determinant exists uniquely, and examine methods for computing it.

## Symmetric Groups

In this section we define the symmetric group. We proceed without detailed proofs for the results introduced here, but if desired, the proofs can be found in [\[Group Theory\] §Symmetric Groups](/en/math/group_theory/symmetric_groups).

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> The collection of all bijections from the set $$\{1,\ldots, n\}$$ to itself is called the *symmetric group*, denoted $$S_n$$. The elements of $$S_n$$ are called *permutations*.

</div>

The elements of $$S_n$$ form a group under function composition; the identity element is $$\id$$, and the inverse of a function $$\tau\in S_n$$ is its inverse function $$\tau^{-1}$$.

Among the elements of $$S_n$$, the simplest ones after $$\id$$ are the functions that choose two elements of $$\{1,\ldots, n\}$$ and swap their positions. For example, for $$i,j\in \{1,\ldots, n\}$$, the function defined by the following formula

$$\tau(k)=\begin{cases}i&\text{if $k=j$,}\\j&\text{if $k=i$,}\\k&\text{otherwise.}\end{cases}$$

is such a function. These functions are called *transpositions*.

It is well known that every element of $$S_n$$ can always be expressed as a finite composition of transpositions. Suppose an arbitrary element $$\tau\in S_n$$ is given, and suppose two ways of expressing $$\tau$$ as a composition of transpositions are given as in the following formula.

$$\tau=\upsilon_1\circ\upsilon_2\circ\cdots\circ\upsilon_n=\upsilon_1'\circ\upsilon_2'\circ\cdots\circ\upsilon_m'.$$

In general, $$m$$ and $$n$$ need not be equal, but the parity of $$m$$ and $$n$$ is always the same. If this number is even, $$\tau$$ is called an *even permutation*, and if it is odd, an *odd permutation*. Then we can define a function $$\sgn:S_n\rightarrow\{-1,1\}$$ by the following formula

$$\sgn(\tau)=\begin{cases}1&\text{if $\tau$ is even}\\-1&\text{if $\tau$ is odd}\end{cases}$$

This function becomes a group homomorphism. That is, for any $$\tau,\tau'\in S_n$$, 

$$\sgn(\tau\circ\tau')=\sgn(\tau)\sgn(\tau')$$

holds.

Suppose an arbitrary alternating multilinear map $$f:(\mathbb{K}^n)^n\rightarrow \mathbb{K}$$ is given. Then, by the definition of $$\sgn$$, 

$$f(v_1,v_2,\ldots, v_n)=\sgn(\tau)f(v_{\tau(1)},v_{\tau(2)},\ldots, v_{\tau(n)})$$

we can see that this holds.

## Existence and Uniqueness of the Determinant

<div class="proposition" markdown="1">

<ins id="lem2">**Lemma 2**</ins> A function $$D$$ satisfying [§Determinant, ⁋Definition 4](/en/math/linear_algebra/determinant#def4) exists uniquely.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Suppose $$f$$ is an alternating multilinear map. For any $$v_1,\ldots, v_n\in V$$, if

$$v_i=v_1^ie_1+\cdots v_n^ie_n,\qquad i=1,\ldots, n$$

then

$$\begin{aligned}f(v_1,\ldots, v_n)&=\sum_{i_1=1}^nv_{i_1}^1f(e_{i_1},v_2,\ldots, v_n)\\
&=\sum_{i_1,i_2=1}^n v_{i_1}^1v_{i_2}^2f(e_{i_1},e_{i_2},v_3,\ldots, v_n)\\&=\cdots\\&=\sum_{i_1,\ldots, i_n=1}^nv_{i_1}^1v_{i_2}^2\ldots, v_{i_n}^nf(e_{i_1},\ldots, e_{i_n})\end{aligned}$$

holds. By [§Determinant, ⁋Proposition 3](/en/math/linear_algebra/determinant#prop3), if any of the $$i_1,\ldots, i_n$$ are equal, the value of $$f(e_{i_1},\ldots,e_{i_n})$$ is always 0, so the right-hand side becomes

$$f(v_1,\ldots, v_n)=\sum_{\tau\in S_n}v^1_{\tau(1)}v^2_{\tau(2)}\cdots v^n_{\tau(n)}f(e_{\tau(1)},\ldots, e_{\tau(n)})$$

By the property of $$\sgn$$ examined earlier, this is again equal to

$$f(v_1,\ldots, v_n)=\sum_{\tau\in S_n}\sgn(\tau)v^1_{\tau(1)}v^2_{\tau(2)}\cdots v^n_{\tau(n)}f(e_1,e_2,\ldots, e_n)\tag{1}$$

Therefore, if $$D,D'$$ are two functions satisfying the definition of the determinant,

$$D(e_1,\ldots, e_n)=D'(e_1,\ldots, e_n)=1$$

so by equation (1), $$D=D'$$ must hold.

For existence, similarly taking a hint from equation (1), we define

$$D(v_1,\ldots, v_n)=\sum_{\tau\in S_n}\sgn(\tau)v^1_{\tau(1)}v^2_{\tau(2)}\cdots v^n_{\tau(n)}$$

and show that $$D$$ is actually an alternating multilinear map. This is simply repeating the above calculation in the reverse direction, so we omit it.

</details>

Therefore the determinant is well defined, and we write it as $$\det$$. In the proof process of the above proposition, we obtained a formula for the determinant $$\det A$$. That is, denoting the $$i$$-th column vector of the matrix $$A$$ by $$A_i$$, the $$j$$-th component of $$A_i$$ is $$A_{ji}$$, and thus

$$\det A=\sum_{\tau\in S_n}\sgn(\tau)A_{\tau(1)1}A_{\tau(2)2}\cdots A_{\tau(n)n}\tag{2}$$

For example, when $$n=2$$, the two elements of $$S_2$$ are $$\id$$ and the function $$\tau$$ swapping the positions of $$1$$ and $$2$$, so the determinant is

$$\det A=\sum_{\tau\in S_n}\sgn(\tau)A_{\tau(1)1}A_{\tau(2)2}\cdots A_{\tau(n)n}=\sgn(\id)A_{11}A_{22}+\sgn(\tau)A_{21}A_{12}=A_{11}A_{22}-A_{21}A_{12}$$

In general, when $$n$$ is large, directly computing the value of the determinant using this formula is cumbersome, but the above formula is very helpful when proving various properties of the determinant.

<div class="proposition" markdown="1">

<ins id="cor4">**Corollary 4**</ins> For any matrix $$A\in\Mat_n(\mathbb{K})$$, $$\det(A^t)=\det A$$ holds.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, for transpositions $$\upsilon_i$$, if $$\tau=\upsilon_1\circ\ldots\circ\upsilon_k$$, then $$\tau^{-1}=\upsilon_k^{-1}\circ\cdots\circ\upsilon_1^{-1}$$, so $$\sgn(\tau)=\sgn(\tau^{-1})$$ always holds. Now, from the definition of $$A^t$$, we have $$A_{ij}=(A^t)_{ji}$$, and

$$\det(A^t)=\sum_{\tau\in S_n}\sgn(\tau)A_{1\tau(1)}\cdots A_{n\tau(n)}=\sum_{\tau\in S_n}\sgn(\tau^{-1})A_{\tau^{-1}(1)1}\cdots A_{\tau^{-1}(n)n}$$

so we obtain the desired result.

</details>

Also, from the above formula we can see that the determinant preserves multiplication.

<div class="proposition" markdown="1">

<ins id="lem5">**Lemma 5**</ins> For any matrices $$A,B\in\Mat_n(\mathbb{K})$$, $$\det(AB)=\det(A)\det(B)$$ holds.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

The $$(i,j)$$-entry of the matrix $$AB$$ is given by the following formula

$$(AB)_{ij}=\sum_{k=1}^nA_{ik}B_{kj}$$

Therefore,

$$\begin{aligned}\det(AB)&=\det((AB)_1, (AB)_2,\ldots, (AB)_n)\\&=\sum_{\tau\in S_n}\sgn(\tau)(AB)_{\tau(1)1}(AB)_{\tau(2)2}\cdots(AB)_{\tau(n)n}\\&=\sum_{\tau\in S_n}\sgn(\tau)\left(\sum_{i_1=1}^nA_{\tau(1)i_1}B_{i_11}\right)\cdots\left(\sum_{i_n=1}^nA_{\tau(n)i_n}B_{i_nn}\right)\\&=\sum_{\tau\in S_n}\sum_{i_1,\ldots, i_n=1}^n\sgn(\tau)A_{\tau(1)i_1}\cdots A_{\tau(n)i_n}B_{i_11}\cdots B_{i_nn}\\&=\sum_{i_1,\ldots, i_n=1}^nB_{i_11}\cdots B_{i_nn}\left(\sum_{\tau\in S_n}\sgn(\tau)A_{\tau(1)1}\cdots A_{\tau(n)n}\right)\\&=\sum_{i_1,\ldots, i_n=1}^n\det(A_{i_1},\ldots, A_{i_n})B_{i_11}\cdots B_{i_nn}\end{aligned}$$

Now, defining $$\upsilon\in S_n$$ as an element satisfying the following formula

$$\upsilon(1)=i_1,\ldots, \upsilon(n)=i_n$$

the right-hand side of the above formula becomes

$$\sum_{\upsilon\in S_n}\sgn(\upsilon)\det(A)B_{\upsilon(1)1}\cdots B_{\upsilon(n)n}=\det(A)\det(B)$$

and thus the proof is complete.

</details>

In the previous post, we explained geometrically that a matrix $$A$$ being invertible is equivalent to $$\det A\neq 0$$. Using [Lemma 5](#lem5), we can prove this rigorously.

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6**</ins> For any matrix $$A\in\Mat_n(\mathbb{K})$$, $$\det A\neq 0$$ is equivalent to $$A$$ being invertible.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

From the fundamental theorem of linear algebra, we know that $$A$$ being invertible is equivalent to the linear map $$L_A:\mathbb{K}^n\rightarrow \mathbb{K}^n$$ defined by $$A$$ being invertible. Since $$\mathbb{K}^n$$ is finite-dimensional, this is again equivalent to $$L_A$$ being surjective, which is equivalent to the column vectors $$A_1,\ldots, A_n$$, which form a basis of $$\col(A)$$, being linearly independent. If $$A_1,\ldots, A_n$$ are not linearly independent, then by [§Determinant, ⁋Proposition 3](/en/math/linear_algebra/determinant#prop3), we have $$\det A=0$$. That is, if $$\det A\neq 0$$, then $$A$$ is invertible.

Conversely, suppose $$A$$ is invertible. Then from the following formula

$$1=\det(I)=\det(A^{-1}A)=\det(A^{-1})\det(A)\tag{3}$$

we know that $$\det A\neq 0$$.

</details>

From equation (3) appearing in the proof of the above proposition, we obtain the following corollary.

<div class="proposition" markdown="1">

<ins id="cor7">**Corollary 7**</ins> For an invertible matrix $$A\in\Mat_n(\mathbb{K})$$, $$\det(A^{-1})=(\det A)^{-1}$$ holds.

</div>

## Triangular Matrices and Determinants

The formula examined earlier is inefficient because computing the determinant requires calculating $$n!$$ terms. However, in certain cases this formula can be usefully applied.

<div class="definition" markdown="1">

<ins id="def8">**Definition 8**</ins> A matrix $$A\in\Mat_n(\mathbb{K})$$ is called an *upper triangular matrix* if $$A_{ij}=0$$ whenever $$i>j$$. Similarly, if $$A_{ij}=0$$ whenever $$i < j$$, then $$A$$ is called a *lower triangular matrix*, and upper and lower triangular matrices are collectively called simply *triangular matrices*.

Meanwhile, the entries $$A_{ii}$$ of a matrix $$A$$ are called its *diagonal entries*, and if $$A_{ij}=0$$ whenever $$i\neq j$$, then $$A$$ is called a *diagonal matrix*.

</div>

In particular, every $$n\times n$$ row echelon matrix is an upper triangular matrix. ([§Gaussian Elimination, ⁋Definition 2](/en/math/linear_algebra/Gaussian_elimination#def2))


<div class="proposition" markdown="1">

<ins id="prop9">**Proposition 9**</ins> For any triangular matrix $$A$$, $$\det(A)$$ equals the product of the diagonal entries.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Let us examine again the determinant formula

$$\det A=\sum_{\tau\in S_n}\sgn(\tau)A_{\tau(1)1}A_{\tau(2)2}\cdots A_{\tau(n)n}$$

examined above. For any $$\tau\in S_n$$, since $$\tau$$ is a bijection, if there exists an $$i$$ such that $$\tau(i)>i$$, then there must exist a $$j$$ such that $$\tau(j)<j$$. Therefore, the terms added in the above formula are always 0 except when $$\tau=\id$$.

</details>

By [§Gaussian Elimination](/en/math/linear_algebra/Gaussian_elimination), any matrix can be transformed into a row echelon matrix by repeated elementary row operations. Since every row echelon matrix is an upper triangular matrix, the determinant of the row echelon matrix obtained in this way can be computed very easily using the above proposition. Meanwhile, applying elementary row operations is the same as multiplying by elementary matrices. Therefore, if we obtain a row echelon matrix $$A'$$ from a matrix $$A$$ by repeated elementary row operations $$E_1,\ldots, E_k$$,

$$A'=E_kE_{k-1}\cdots E_1 A$$

so

$$\det(A')=\det(E_k)\det(E_{k-1})\cdots\det(E_1)\det(A)$$

Therefore, let us examine the determinants of the elementary matrices $$E_{i,j}$$, $$E'_{i,r}$$, $$E''_{i,j,r}$$. First, for $$E_{i,j}$$ and $$E'_{i,r}$$, from the definition of the determinant,

$$\det E_{i,j}=-1,\quad \det E'_{i,r}=r$$

we can easily see that. Also, $$E''_{i,j,r}$$ is always a triangular matrix, and since the product of its diagonal entries is 1, $$\det E''_{i,j,r}=1$$ holds.

## Determinants of Block Matrices

Meanwhile, using the determinant formula (2), we can also find the determinant of a block matrix.

<div class="proposition" markdown="1">

<ins id="prop10">**Proposition 10**</ins> Let $$A\in\Mat_k(\mathbb{K})$$ and let $$I$$ be the $$l\times l$$ identity matrix. Then the determinant of the following block matrix

$$\begin{pmatrix}A&O\\O&I\end{pmatrix}$$

is equal to $$\det A$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

This is almost identical to the proof of [Proposition 9](#prop9). Computing the determinant of the given matrix using equation (2), we have

$$\det \begin{pmatrix}A&O\\O&I\end{pmatrix}=\sum_{\tau\in S_{k+l}}\sgn(\tau)A_{\tau(1)1}A_{\tau(2)2}\cdots A_{\tau(k)k}B_{\tau(k+1)(k+1)}\cdots B_{\tau(k+l)(k+l)}$$

Here $$B_{k+i}$$ is the element of $$\mathbb{K}^{k+l}$$ whose $$(k+i)$$-th component is 1 and whose remaining components are all 0. Then

$$\tau(k+1)=k+1,\ldots,\tau(k+l)=k+1$$

unless this holds, the terms added on the right-hand side are always 0, and thus we only need to compute the sum over those $$\tau$$ for which the last $$l$$ entries are fixed. That is, the determinant of the given matrix becomes exactly the same as equation (2), so the given proposition holds.

</details>

<div class="proposition" markdown="1">

<ins id="cor11">**Corollary 11**</ins> For $$A\in\Mat_k(\mathbb{K}),B\in\Mat_l(\mathbb{K}), C\in\Mat_{l\times k}(\mathbb{K})$$, the determinant of the following block matrix

$$\begin{pmatrix}A&O\\C&B\end{pmatrix}$$

is equal to $$\det A\det B$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

The following formula

$$\begin{pmatrix}A&O\\C&B\end{pmatrix}=\begin{pmatrix}A&O\\O&E\end{pmatrix}\begin{pmatrix}I&O\\O&I\end{pmatrix}\begin{pmatrix}I&O\\O&B\end{pmatrix}$$

together with [Proposition 10](#prop10) and [Lemma 5](#lem5) makes this obvious. For the last matrix, after $$l$$ row swaps and then $$l$$ column swaps, there are $$2l$$ sign changes, so the determinant of the given matrix becomes equal to $$\det B$$.

</details>

It is not difficult to extend the above results inductively. That is,

$$\det\begin{pmatrix}A_{11}&A_{12}&\cdots&A_{1n}\\O&A_{22}&\cdots&A_{2n}\\\vdots&\vdots&\ddots&\vdots\\O&O&\cdots&A_{nn}\end{pmatrix}=\det A_{11}\det A_{22}\cdots\det A_{nn}$$

holds. However, if the block matrix does not become a triangular matrix when expressed in block form, a similar result <em-ko>does not hold</em-ko>. For instance, for the following block matrix

$$\begin{pmatrix}A&B\\C&D\end{pmatrix}$$

the value of its determinant is generally not equal to $$\det A\det D-\det B\det C$$.


## Laplace Expansion

When an $$n\times n$$ square matrix $$A$$ is given, one of the easiest ways to find the determinant of $$A$$ is to use the Laplace expansion, which we now introduce. For this, a definition is needed.

<div class="definition" markdown="1">

<ins id="def12">**Definition 12**</ins> Suppose a matrix $$A\in\Mat_n(\mathbb{K})$$ is given. For $$1\leq i,j\leq n$$, $$A^{(i,j)}$$ is the $$(n-1)\times(n-1)$$ square matrix obtained by deleting the $$i$$-th row and $$j$$-th column of the matrix $$A$$.

</div>

The Laplace expansion expresses the determinant of $$A$$ as a formula in terms of the $$\det A^{(i,j)}$$.

<div class="proposition" markdown="1">

<ins id="thm13">**Theorem 13**</ins> For any matrix $$A\in\Mat_n(\mathbb{K})$$ and any $$1\leq i\leq n$$, the following formula

$$\det A=\sum_{j=1}^n(-1)^{i+j}A_{ij}\det (A^{(i,j)})$$

holds.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, fix $$i,j$$. Let $$B_j$$ be the matrix obtained from $$A$$ by changing all entries of the $$i$$-th row to 0, except leaving only the $$j$$-th entry. Then, swapping the order of rows $$i-1$$ times to bring the $$i$$-th row to the first row, and swapping the order of columns $$j-1$$ times to bring the $$j$$-th column to the first column, let us call the resulting matrix $$B_j'$$. Then

$$B_j'=\begin{pmatrix}A_{ij}&0&\cdots&0\\A_{1j}&&&\\\vdots&&A^{(i,j)}&\\A_{nj}&&&\end{pmatrix}$$

Now, by [Proposition 10](#prop10), the determinant of this matrix equals $$A_{ij}\det A^{(i,j)}$$, and thus

$$\det B_j=(-1)^{i+j-2}\det B_j'=(-1)^{i+j-2}A_{ij}\det A^{(i,j)}=(-1)^{i+j}A_{ij}\det A^{(i,j)}$$

Meanwhile, using multilinearity in the $$i$$-th column, the sum of the determinants of the $$B_j$$ equals the determinant of $$A$$, so we obtain the desired formula

$$\det A=\sum_{j=1}^n\det B_j=\sum_{j=1}^n (-1)^{i+j}A_{ij}\det A^{(i,j)}$$

</details>

---

**References**

**[Goc]** M.S. Gockenbach, *Finite-dimensional linear algebra*, Discrete Mathematics and its applications, Taylor&Francis, 2011.

---
