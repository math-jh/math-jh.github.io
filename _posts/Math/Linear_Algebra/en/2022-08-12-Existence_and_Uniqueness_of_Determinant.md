---
title: "Existence and Uniqueness of the Determinant"
excerpt: "Existence and uniqueness proof of the determinant, and methods for computing it"

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
translated_at: 2026-05-26T17:00:02+00:00
translation_source: kimi-cli
---
In this post we show that the determinant exists uniquely, and examine methods for computing it.

## The Symmetric Group

In this section we define the symmetric group. The results introduced here are presented without detailed proof, but the proofs can be found in [\[Group Theory\] §Symmetric Groups](/en/math/group_theory/symmetric_groups) if desired.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> The collection of all bijections from the set $$\{1,\ldots, n\}$$ to itself is called the *symmetric group*, denoted $$S_n$$. The elements of $$S_n$$ are called *permutations*.

</div>

The elements of $$S_n$$ form a group under function composition, with identity element $$\id$$, and the inverse of a function $$\tau\in S_n$$ is the inverse function $$\tau^{-1}$$.

Among the elements of $$S_n$$, the simplest ones after $$\id$$ are the functions that choose two elements from $$\{1,\ldots, n\}$$ and swap their positions. For example, for $$i,j\in \{1,\ldots, n\}$$, the function defined by

$$\tau(k)=\begin{cases}i&\text{if $k=j$,}\\j&\text{if $k=i$,}\\k&\text{otherwise.}\end{cases}$$

is such a function. These functions are called *transpositions*.

It is well known that every element of $$S_n$$ can be expressed as a finite composition of transpositions. Suppose an arbitrary element $$\tau\in S_n$$ is given, and suppose two ways of expressing $$\tau$$ as a composition of transpositions are given as follows:

$$\tau=\upsilon_1\circ\upsilon_2\circ\cdots\circ\upsilon_n=\upsilon_1'\circ\upsilon_2'\circ\cdots\circ\upsilon_m'.$$

In general, $$m$$ and $$n$$ need not be equal, but the parity of $$m$$ and $$n$$ is always the same. If this number is even, $$\tau$$ is called an *even permutation*, and if odd, an *odd permutation*. Then we can define the function $$\sgn:S_n\rightarrow\{-1,1\}$$ by

$$\sgn(\tau)=\begin{cases}1&\text{if $\tau$ is even}\\-1&\text{if $\tau$ is odd}\end{cases}$$

This function is a group homomorphism. That is, for any $$\tau,\tau'\in S_n$$,

$$\sgn(\tau\circ\tau')=\sgn(\tau)\sgn(\tau')$$

holds.

Suppose an arbitrary alternating multilinear map $$f:(\mathbb{K}^n)^n\rightarrow \mathbb{K}$$ is given. Then by the definition of $$\sgn$$, we can see that

$$f(v_1,v_2,\ldots, v_n)=\sgn(\tau)f(v_{\tau(1)},v_{\tau(2)},\ldots, v_{\tau(n)})$$

holds.

## Existence and Uniqueness of the Determinant

<div class="proposition" markdown="1">

<ins id="lem2">**Lemma 2**</ins> The function $$D$$ satisfying [§Determinant, ⁋Definition 4](/en/math/linear_algebra/determinant#def4) exists uniquely.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Let $$f$$ be an alternating linear map. For arbitrary $$v_1,\ldots, v_n\in V$$, if

$$v_i=v_1^ie_1+\cdots v_n^ie_n,\qquad i=1,\ldots, n$$

then

$$\begin{aligned}f(v_1,\ldots, v_n)&=\sum_{i_1=1}^nv_{i_1}^1f(e_{i_1},v_2,\ldots, v_n)\\
&=\sum_{i_1,i_2=1}^n v_{i_1}^1v_{i_2}^2f(e_{i_1},e_{i_2},v_3,\ldots, v_n)\\&=\cdots\\&=\sum_{i_1,\ldots, i_n=1}^nv_{i_1}^1v_{i_2}^2\ldots, v_{i_n}^nf(e_{i_1},\ldots, e_{i_n})\end{aligned}$$

holds. By [§Determinant, ⁋Proposition 3](/en/math/linear_algebra/determinant#prop3), if there are duplicates among $$i_1,\ldots, i_n$$, then the value of $$f(e_{i_1},\ldots,e_{i_n})$$ is always 0, so the right-hand side becomes

$$f(v_1,\ldots, v_n)=\sum_{\tau\in S_n}v^1_{\tau(1)}v^2_{\tau(2)}\cdots v^n_{\tau(n)}f(e_{\tau(1)},\ldots, e_{\tau(n)})$$

By the property of $$\sgn$$ examined above, this is again equal to

$$f(v_1,\ldots, v_n)=\sum_{\tau\in S_n}\sgn(\tau)v^1_{\tau(1)}v^2_{\tau(2)}\cdots v^n_{\tau(n)}f(e_1,e_2,\ldots, e_n)\tag{1}$$

Therefore, if $$D,D'$$ are two functions satisfying the definition of the determinant, then

$$D(e_1,\ldots, e_n)=D'(e_1,\ldots, e_n)=1$$

so by equation (1), $$D=D'$$ must necessarily hold.

For existence, similarly taking a hint from equation (1), we define

$$D(v_1,\ldots, v_n)=\sum_{\tau\in S_n}\sgn(\tau)v^1_{\tau(1)}v^2_{\tau(2)}\cdots v^n_{\tau(n)}$$

and then show that $$D$$ is actually an alternating multilinear map. This is simply repeating the above calculation in reverse, so we omit it.

</details>

Thus the determinant is well-defined, and we write it as $$\det$$. From the proof of the above proposition, we obtained an explicit formula for the determinant $$\det A$$. That is, denoting the $$i$$-th column vector of a matrix $$A$$ by $$A_i$$, the $$j$$-th component of $$A_i$$ is $$A_{ji}$$, and therefore

$$\det A=\sum_{\tau\in S_n}\sgn(\tau)A_{\tau(1)1}A_{\tau(2)2}\cdots A_{\tau(n)n}\tag{2}$$

For example, when $$n=2$$, the two elements of $$S_2$$ are $$\id$$ and the function $$\tau$$ that swaps 1 and 2, so the determinant is

$$\det A=\sum_{\tau\in S_n}\sgn(\tau)A_{\tau(1)1}A_{\tau(2)2}\cdots A_{\tau(n)n}=\sgn(\id)A_{11}A_{22}+\sgn(\tau)A_{21}A_{12}=A_{11}A_{22}-A_{21}A_{12}$$

In general, when $$n$$ is large, directly computing the determinant using this formula is cumbersome, but the above formula is very helpful when proving various properties of the determinant.

<div class="proposition" markdown="1">

<ins id="cor4">**Corollary 4**</ins> For any matrix $$A\in\Mat_n(\mathbb{K})$$, $$\det(A^t)=\det A$$ holds.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, for transpositions $$\upsilon_i$$, if $$\tau=\upsilon_1\circ\ldots\upsilon_k$$ then $$\tau^{-1}=\upsilon_k^{-1}\circ\cdots\circ\upsilon_1^{-1}$$, so $$\sgn(\tau)=\sgn(\tau^{-1})$$ always holds. Now from the definition of $$A^t$$, we have $$A_{ij}=(A^t)_{ji}$$, and

$$\det(A^t)=\sum_{\tau\in S_n}\sgn(\tau)A_{1\tau(1)}\cdots A_{n\tau(n)}=\sum_{\tau\in S_n}\sgn(\tau^{-1})A_{\tau^{-1}(1)1}\cdots A_{\tau^{-1}(n)n}$$

from which we obtain the desired result.

</details>

Also, from the above formula we can see that the determinant preserves multiplication.

<div class="proposition" markdown="1">

<ins id="lem5">**Lemma 5**</ins> For any matrices $$A,B\in\Mat_n(\mathbb{K})$$, $$\det(AB)=\det(A)\det(B)$$ holds.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

The $$(i,j)$$-entry of the matrix $$AB$$ is given by the formula

$$(AB)_{ij}=\sum_{k=1}^nA_{ik}B_{kj}$$

Therefore,

$$\begin{aligned}\det(AB)&=\det((AB)_1, (AB)_2,\ldots, (AB)_n)\\&=\sum_{\tau\in S_n}\sgn(\tau)(AB)_{\tau(1)1}(AB)_{\tau(2)2}\cdots(AB)_{\tau(n)n}\\&=\sum_{\tau\in S_n}\sgn(\tau)\left(\sum_{i_1=1}^nA_{\tau(1)i_1}B_{i_11}\right)\cdots\left(\sum_{i_n=1}^nA_{\tau(n)i_n}B_{i_nn}\right)\\&=\sum_{\tau\in S_n}\sum_{i_1,\ldots, i_n=1}^n\sgn(\tau)A_{\tau(1)i_1}\cdots A_{\tau(n)i_n}B_{i_11}\cdots B_{i_nn}\\&=\sum_{i_1,\ldots, i_n=1}^nB_{i_11}\cdots B_{i_nn}\left(\sum_{\tau\in S_n}\sgn(\tau)A_{\tau(1)1}\cdots A_{\tau(n)n}\right)\\&=\sum_{i_1,\ldots, i_n=1}^n\det(A_{i_1},\ldots, A_{i_n})B_{i_11}\cdots B_{i_nn}\end{aligned}$$

Now define $$\upsilon\in S_n$$ to be the element satisfying

$$\upsilon(1)=i_1,\ldots, \upsilon(n)=i_n$$

Then the right-hand side of the above expression becomes

$$\sum_{\upsilon\in S_n}\sgn(\upsilon)\det(A)B_{\upsilon(1)1}\cdots B_{\upsilon(n)n}=\det(A)\det(B)$$

thus completing the proof.

</details>

In the previous post we explained geometrically that a matrix $$A$$ is invertible if and only if $$\det A\neq 0$$. Using [Lemma 5](#lem5) above, we can prove this rigorously.

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6**</ins> For any matrix $$A\in\Mat_n(\mathbb{K})$$, $$\det A\neq 0$$ is equivalent to $$A$$ being invertible.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

From the fundamental theorem of linear algebra, we know that $$A$$ being invertible is equivalent to the linear map $$L_A:\mathbb{K}^n\rightarrow \mathbb{K}^n$$ defined by $$A$$ being invertible. Since $$\mathbb{K}^n$$ is finite-dimensional, this is equivalent to $$L_A$$ being surjective, which is equivalent to the column vectors $$A_1,\ldots, A_n$$ forming a basis of $$\col(A)$$, i.e., being linearly independent. If $$A_1,\ldots, A_n$$ are not linearly independent, then by [§Determinant, ⁋Proposition 3](/en/math/linear_algebra/determinant#prop3), $$\det A=0$$. That is, if $$\det A\neq 0$$, then $$A$$ is invertible.

Conversely, assume $$A$$ is invertible. Then from the formula

$$1=\det(I)=\det(A^{-1}A)=\det(A^{-1})\det(A)\tag{3}$$

we know that $$\det A\neq 0$$.

</details>

From equation (3) appearing in the proof of the above proposition, we obtain the following corollary.

<div class="proposition" markdown="1">

<ins id="cor7">**Corollary 7**</ins> For an invertible matrix $$A\in\Mat_n(\mathbb{K})$$, $$\det(A^{-1})=(\det A)^{-1}$$ holds.

</div>

## Triangular Matrices and the Determinant

The formula examined above is inefficient because it requires computing $$n!$$ terms to find the determinant. However, in certain cases this formula applies usefully.

<div class="definition" markdown="1">

<ins id="def8">**Definition 8**</ins> A matrix $$A\in\Mat_n(\mathbb{K})$$ is called an *upper triangular matrix* if $$A_{ij}=0$$ whenever $$i>j$$. Similarly, if $$A_{ij}=0$$ whenever $$i < j$$, then $$A$$ is called a *lower triangular matrix*, and upper and lower triangular matrices are collectively called simply *triangular matrices*.

On the other hand, the entries $$A_{ii}$$ of a matrix $$A$$ are called the *diagonal entries*, and if $$A_{ij}=0$$ whenever $$i\neq j$$, then $$A$$ is called a *diagonal matrix*.

</div>

In particular, every $$n\times n$$ row echelon matrix is an upper triangular matrix. ([§Gaussian Elimination, ⁋Definition 4](/en/math/linear_algebra/Gaussian_elimination#def4))


<div class="proposition" markdown="1">

<ins id="prop9">**Proposition 9**</ins> For any triangular matrix $$A$$, $$\det(A)$$ equals the product of the diagonal entries.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Let us examine once more the determinant formula

$$\det A=\sum_{\tau\in S_n}\sgn(\tau)A_{\tau(1)1}A_{\tau(2)2}\cdots A_{\tau(n)n}$$

For any $$\tau\in S_n$$, since $$\tau$$ is a bijection, if there exists an $$i$$ such that $$\tau(i)>i$$, then there must necessarily exist a $$j$$ such that $$\tau(j)<j$$. Therefore, among the terms summed in the above formula, all are 0 except when $$\tau=\id$$.

</details>

By [§Gaussian Elimination](/en/math/linear_algebra/Gaussian_elimination), any matrix can be transformed into row echelon form by repeated elementary row operations. Since every row echelon matrix is an upper triangular matrix, by the above proposition we can very easily find the determinant of the resulting row echelon matrix. On the other hand, applying elementary row operations is equivalent to multiplying by elementary matrices. Therefore, if from a matrix $$A$$ we obtain a row echelon matrix $$A'$$ by repeated elementary row operations $$E_1,\ldots, E_k$$, then

$$A'=E_kE_{k-1}\cdots E_1 A$$

so

$$\det(A')=\det(E_k)\det(E_{k-1})\cdots\det(E_1)\det(A)$$

Thus let us examine the determinants of the elementary matrices $$E_{i,j}$$, $$E'_{i,r}$$, and $$E''_{i,j,r}$$. First, for $$E_{i,j}$$ and $$E'_{i,r}$$, from the definition of the determinant we can easily see that

$$\det E_{i,j}=-1,\quad \det E'_{i,r}=r$$

Also, $$E''_{i,j,r}$$ is necessarily a triangular matrix, and since the product of its diagonal entries is 1, $$\det E''_{i,j,r}=1$$ holds.

## Determinant of a Block Matrix

On the other hand, using formula (2) for the determinant, we can also find the determinant of a block matrix.

<div class="proposition" markdown="1">

<ins id="prop10">**Proposition 10**</ins> Let $$A\in\Mat_k(\mathbb{K})$$ and let $$I$$ be the $$l\times l$$ identity matrix. Then the determinant of the block matrix

$$\begin{pmatrix}A&O\\O&I\end{pmatrix}$$

equals $$\det A$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

This is almost identical to the proof of [Proposition 9](#prop9). Computing the determinant of the given matrix using formula (2), we get

$$\det \begin{pmatrix}A&O\\O&I\end{pmatrix}=\sum_{\tau\in S_{k+l}}\sgn(\tau)A_{\tau(1)1}A_{\tau(2)2}\cdots A_{\tau(k)k}B_{\tau(k+1)(k+1)}\cdots B_{\tau(k+l)(k+l)}$$

Here $$B_{k+i}$$ is the element of $$\mathbb{K}^{k+l}$$ whose $$(k+i)$$-th component is 1 and all other components are 0. Then unless

$$\tau(k+1)=k+1,\ldots,\tau(k+l)=k+1$$

the terms summed on the right-hand side are always 0, so we only need to sum over those $$\tau$$ for which the last $$l$$ entries are fixed. That is, the determinant of the given matrix becomes exactly the same as formula (2), so the given proposition holds.

</details>

<div class="proposition" markdown="1">

<ins id="cor11">**Corollary 11**</ins> For $$A\in\Mat_k(\mathbb{K}),B\in\Mat_l(\mathbb{K}), C\in\Mat_{l\times k}(\mathbb{K})$$, the determinant of the block matrix

$$\begin{pmatrix}A&O\\C&B\end{pmatrix}$$

equals $$\det A\det B$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

This follows immediately from the formula

$$\begin{pmatrix}A&O\\C&B\end{pmatrix}=\begin{pmatrix}A&O\\O&E\end{pmatrix}\begin{pmatrix}I&O\\O&I\end{pmatrix}\begin{pmatrix}I&O\\O&B\end{pmatrix}$$

and [Proposition 10](#prop10), and [Lemma 5](#lem5). For the last matrix, after $$l$$ row swaps and $$l$$ column swaps, there are $$2l$$ sign changes, so the determinant of the given matrix becomes equal to $$\det B$$.

</details>

It is not difficult to extend the above results inductively. That is,

$$\det\begin{pmatrix}A_{11}&A_{12}&\cdots&A_{1n}\\O&A_{22}&\cdots&A_{2n}\\\vdots&\vdots&\ddots&\vdots\\O&O&\cdots&A_{nn}\end{pmatrix}=\det A_{11}\det A_{22}\cdots\det A_{nn}$$

holds. However, when the block matrix does not form a triangular matrix, a similar result does not hold. For example, the determinant of the block matrix

$$\begin{pmatrix}A&B\\C&D\end{pmatrix}$$

is generally not equal to $$\det A\det D-\det B\det C$$.


## Laplace Expansion

When an $$n\times n$$ square matrix $$A$$ is given, one of the easiest ways to find its determinant is to use the Laplace expansion, which we now introduce. For this, a definition is needed.

<div class="definition" markdown="1">

<ins id="def12">**Definition 12**</ins> Let a matrix $$A\in\Mat_n(\mathbb{K})$$ be given. For $$1\leq i,j\leq n$$, $$A^{(i,j)}$$ is the $$(n-1)\times (n-1)$$ square matrix obtained by deleting the $$i$$-th row and $$j$$-th column of $$A$$.

</div>

The Laplace expansion expresses the determinant of $$A$$ as a formula in terms of the $$\det A^{(i,j)}$$.

<div class="proposition" markdown="1">

<ins id="thm13">**Theorem 13**</ins> For any matrix $$A\in\Mat_n(\mathbb{K})$$ and any $$1\leq i\leq n$$, the following formula holds:

$$\det A=\sum_{j=1}^n(-1)^{i+j}A_{ij}\det (A^{(i,j)})$$

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First fix $$i,j$$. Let $$B_j$$ be the matrix obtained from $$A$$ by replacing all entries in the $$i$$-th row with 0, except leaving the $$j$$-th entry unchanged. Then, swap rows $$i-1$$ times to bring the $$i$$-th row to the first row, and swap columns $$j-1$$ times to bring the $$j$$-th column to the first column, and call the resulting matrix $$B_j'$$. Then

$$B_j'=\begin{pmatrix}A_{ij}&0&\cdots&0\\A_{1j}&&&\\\vdots&&A^{(i,j)}&\\A_{nj}&&&\end{pmatrix}$$

Now by [Proposition 10](#prop10), the determinant of this matrix equals $$A_{ij}\det A^{(i,j)}$$, and therefore

$$\det B_j=(-1)^{i+j-2}\det B_j'=(-1)^{i+j-2}A_{ij}\det A^{(i,j)}=(-1)^{i+j}A_{ij}\det A^{(i,j)}$$

On the other hand, using multilinearity in the $$i$$-th column, the sum of the determinants of the $$B_j$$ equals the determinant of $$A$$, so we obtain the desired formula

$$\det A=\sum_{j=1}^n\det B_j=\sum_{j=1}^n (-1)^{i+j}A_{ij}\det A^{(i,j)}$$

</details>

---

**References**

**[Goc]** M.S. Gockenbach, *Finite-dimensional linear algebra*, Discrete Mathematics and its applications, Taylor&Francis, 2011.

---
