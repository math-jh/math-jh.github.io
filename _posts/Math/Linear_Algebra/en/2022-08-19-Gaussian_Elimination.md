---
title: "Gaussian Elimination"
description: "We use Gaussian elimination to find the inverse of a matrix and prove equivalent conditions for invertibility. We also analyze the equivalence relation determined by rank, based on the relationship between matrices and linear transformations."
excerpt: "Gaussian elimination and inverse matrices"

categories: [Math / Linear Algebra]
permalink: /en/math/linear_algebra/Gaussian_elimination
sidebar: 
    nav: "linear_algebra-en"


date: 2022-08-19

weight: 12
translated_at: 2026-06-25T12:30:03+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-25T12:30:03+00:00
---
In the previous post, we learned that linear maps between vector spaces are essentially the same as matrices. From this perspective, if two $$m\times n$$ matrices $$A,B$$ satisfy

$$B=PAQ\tag{1}$$

for suitable invertible matrices $$P,Q$$, we might want to regard these matrices $$A,B$$ as essentially the same. However, if we allow complete freedom in choosing bases of the two vector spaces $$V,W$$ on which these matrices $$L_A, L_B: V\rightarrow W$$ act, then we have seen that any two matrices of the same rank must be treated as identical. Therefore, in [§Fundamental Theorem of Linear Algebra, ⁋Definition 8](/en/math/linear_algebra/ftla#def8), we had to define a finer equivalence relation. Roughly speaking, if the only information contained in the matrix $$A$$ in equation (1) is the rank of $$A$$, then the remaining information is contained in the matrices $$P,Q$$—that is, in the *linear operators* from $$V$$ to $$V$$ or from $$W$$ to $$W$$. If we fix a basis of $$V$$ (or $$W$$) to examine these, this equivalence relation is not so unnatural. Thus, for the time being, our discussion proceeds with a fixed vector space $$V$$ and basis $$\mathcal{B}$$. In other words, we examine $$n\times n$$ matrices. The powerful tool for this is the determinant, which we define in the next post.

On the other hand, we proved that for an arbitrary matrix $$A$$ to be invertible, it must necessarily be a square matrix, using the trace of a matrix ([§Matrices, ⁋Definition 6](/en/math/linear_algebra/matrices#def6)). Now that we know matrices and linear maps are the same, this result is obvious by [§Isomorphisms, ⁋Corollary 4](/en/math/linear_algebra/isomorphic_vector_spaces#cor4). However, we have not yet examined how to compute this inverse matrix. The method is simple, so we could have presented it right after [§Matrices](/en/math/linear_algebra/matrices), but now that we have begun to examine $$n\times n$$ matrices in earnest, we briefly introduce this procedure.

First, we show the following simple lemma.

<div class="proposition" markdown="1">

<ins id="lem1">**Lemma 1**</ins> For a matrix $$A\in\Mat_n(\mathbb{K})$$, the following three conditions are all equivalent.

1. $$A$$ is invertible.
2. There exists a suitable $$B\in\Mat_n(\mathbb{K})$$ such that $$AB=I$$.
3. There exists a suitable $$B\in\Mat_n(\mathbb{K})$$ such that $$BA=I$$.

Moreover, if the second or third condition holds, then $$B=A^{-1}$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

That the first condition implies each of the second and third is obvious, so it suffices to show the converse directions.

First, assume that there exists a suitable $$B\in\Mat_n(\mathbb{K})$$ such that $$AB=I$$. Then by the fundamental theorem of linear algebra,

$$L_A\circ L_B=\id_{\mathbb{K}^n}$$

holds. Since $$\id_{\mathbb{K}^n}$$ is bijective, we know that $$L_A:\mathbb{K}^n\rightarrow \mathbb{K}^n$$ is surjective. ([\[Set Theory\] §Retractions and Sections, ⁋Proposition 3](/en/math/set_theory/retraction_and_section#prop3)) Therefore, from the equation ([§Isomorphisms, ⁋Theorem 7](/en/math/linear_algebra/isomorphic_vector_spaces#thm7))

$$\rank L_A+\nullity L_A=\dim \mathbb{K}^n=n$$

we know that $$\nullity L_A=0$$. That is, $$L_A$$ is also injective, and thus $$L_A$$ is bijective and the matrix $$A$$ is invertible. Now, multiplying both sides of the equation $$AB=I$$ on the left by $$A^{-1}$$, we obtain $$B=A^{-1}$$.

Similarly, one can prove that the third condition implies the first.

</details>

Of course, thinking again that matrices and linear maps are the same, this is obvious because the inverse of a function satisfies the same property.

Now, let an arbitrary $$n\times n$$ invertible matrix $$B$$ be given. Thinking of $$B$$ as a linear map from $$\mathbb{K}^n$$ to $$\mathbb{K}^n$$, $$B$$ is completely determined by where it sends the basis $$e_1,\ldots, e_n$$ of $$\mathbb{K}^n$$. Therefore, to compute the matrix $$A^{-1}$$, it suffices to know where $$A^{-1}$$ sends each basis element $$e_i$$. If we denote this value by the vector $$v_i$$, then the matrix $$A$$ is given by $$(v_1\mid v_2\mid\cdots\mid v_n)$$, and each $$v_i$$ is defined by the following equation:

$$v_i=A^{-1}e_i\iff Av_i=e_i\tag{2}$$

## Gaussian-Jordan Elimination

Now, consider the following system of linear equations:

$$\begin{aligned}a_{11}x_{1}+a_{12}x_2+\cdots+a_{1n}x_n&=b_1\\a_{21}x_1+a_{22}x_2+\cdots+a_{2n}x_n&=b_2\\\hspace{10pt}\vdots&\\a_{mn}x_1+a_{m2}x_2+\cdots+a_{mn}x_n&=b_m\end{aligned}\tag{3}$$

By [§Matrices, ⁋Definition 1](/en/math/linear_algebra/matrices#def1), the above system can be written as $$Ax=b$$ for the following matrices:

$$A=\begin{pmatrix}a_{11}&a_{12}&\cdots&a_{1n}\\a_{21}&a_{22}&\cdots&a_{2n}\\\vdots&\vdots&\ddots&\vdots\\a_{m1}&a_{m2}&\cdots&a_{mn}\end{pmatrix},\quad x=\begin{pmatrix}x_1\\x_2\\\vdots\\x_n\end{pmatrix},\quad b=\begin{pmatrix}b_1\\b_2\\\vdots\\b_m\end{pmatrix}$$

If $$m=n$$ and the inverse of matrix $$A$$ exists, then the solution to this system is uniquely determined by the equation

$$x=A^{-1}b\iff Ax=b$$

and this is exactly the equation we need to find the inverse matrix. If $$m\neq n$$ or the inverse of $$A$$ does not exist, the solution to the above system may not exist, or there may be infinitely many. We examine *Gaussian elimination*, which can be usefully applied even in this case.

Assume that there exists $$1\leq i\leq n$$ such that $$a_{ji}=0$$ holds for all $$j$$. In this case, if

$$x_1=c_1,\quad x_2=c_2,\quad \ldots,\quad x_i=c_i,\quad\ldots,\quad x_n=c_n$$

is a solution to equation (3), then the following tuple with $$x_i$$ changed to an arbitrary $$d_i$$:

$$x_1=c_1,\quad x_2=c_2,\quad\ldots,\quad x_i=d_i,\quad\ldots,\quad x_n=c_n$$

is also a solution to equation (3). Therefore, if all $$a_{ij}$$ are $$0$$, then if $$b$$ is the zero vector, equation (3) has every tuple in $$\mathbb{K}^n$$ as a solution, and otherwise no solution exists. To avoid such trivial cases, we assume that at least one $$a_{ij}$$ is not zero.

Now, define the integer $$k$$ as <phrase>the smallest integer among those for which there exists $$1\leq j\leq m$$ such that $$a_{jk}\neq 0$$</phrase>, and for this fixed $$k$$, choose the smallest integer $$j$$ satisfying $$a_{jk}\neq 0$$. Now, move the $$j$$-th equation

$$a_{j1}x_1+a_{j2}x_2+\cdots+a_{jk}x_k+\cdots+a_{nk}x_n=b_j$$

to the top of the system:

$$\begin{aligned}a_{j1}x_{1}+a_{j2}x_2+\cdots+a_{jn}x_n&=b_j\\a_{11}x_1+a_{12}x_2+\cdots+a_{1n}x_n&=b_1\\\hspace{10pt}\vdots&\\a_{mn}x_1+a_{m2}x_2+\cdots+a_{mn}x_n&=b_m\end{aligned}$$

Then by the definition of $$a_{jk}$$, the coefficients $$a_{j1},a_{j2},\ldots, a_{j,(k-1)}$$ and the coefficients below them must all be zero. Now, for each equation

$$a_{i1}x_1+a_{i2}x_2+\cdots+a_{in}x_n=b_i$$

multiply the first equation by $$-a_{ik}/a_{jk}$$ and add it to obtain:

$$\left(a_{i1}-\frac{a_{ik}}{a_{jk}}a_{j1}\right)x_1+\left(a_{i2}-\frac{a_{ik}}{a_{jk}}a_{j2}\right)x_2+\cdots+\left(a_{ik}-\frac{a_{ik}}{a_{jk}}a_{jk}\right)x_k+\cdots+\left(a_{in}-\frac{a_{ik}}{a_{jk}}a_{jn}\right)x_n=b_i-\frac{a_{ik}}{a_{jk}}b_k$$

In the above equation, the coefficients of $$x_1,\ldots, x_{k-1}$$ were already all zero, and by the operation just performed, the coefficient of $$x_k$$ also becomes zero. That is, after this process, the coefficients of $$x_1,\ldots, x_{k-1}$$ are all zero, and among the coefficients of $$x_k$$, the only nonzero one is in the first row.

Now, repeat this process for the $$n-1$$ equations from the second row to the last row, and again for the $$n-2$$ equations from the third row to the last row. Continuing this until reaching the last row, equation (3) finally satisfies the following two conditions (*):

1. If there is an equation where all coefficients are zero, this equation is located at the bottom of the system.
2. For every equation that is not all zeros, the first nonzero coefficient in this equation is to the right of the coefficient with this property in the equation above it.


<div class="example" markdown="1">

<ins id="ex2">**Example 2**</ins> The following system of equations satisfies the above two conditions.

$$\begin{aligned}x_1+2x_2+4x_3+3x_4&=2\\\phantom{x_1+}3x_2\phantom{+2x_3}+6x_4&=3\\\phantom{x_1+2x_2+}x_3+5x_4&=1\end{aligned}$$

With a little additional manipulation, we can immediately find the solution to the system from this equation. Let us call the first nonzero coefficient in each equation the *leading coefficient*. For example, in the above system, the leading coefficient of the first equation is 1, the coefficient of $$x_1$$; the leading coefficient of the second equation is 3, the coefficient of $$x_2$$; and the leading coefficient of the last equation is 1, the coefficient of $$x_3$$.

Now, eliminate all coefficients above the leading coefficient in each row. That is, we must eliminate the term $$4x_3$$ above the leading coefficient of the last equation, and the term $$2x_2$$ above the leading coefficient of the second equation. To do this, multiply the last equation by 4 and subtract it from the first equation, and multiply the second equation by $$2/3$$ and subtract it from the first equation. Also, to make the equation cleaner, multiply both sides of the second equation by $$1/3$$, and the result is as follows.

$$\begin{aligned}x_1\phantom{+2x_2+4x_3}-21x_4&=-4\\\phantom{x_1+}x_2\phantom{+2x_3}+\phantom{1}2x_4&=1\\\phantom{x_1+2x_2+}x_3+\phantom{1}5x_4&=1\end{aligned}$$

From this, we can see that the general solution to the above system of equations is

$$x_1=-4+21x_4,\quad x_2=1-2x_4,\quad x_3=1-5x_4$$

</div>

The method of solving a system of equations through the process described so far is called *Gaussian elimination* or *Gaussian-Jordan elimination*.

## Elementary Row Operations and Gaussian Elimination

The system of equations (3) given initially could be simply expressed as $$Ax=b$$ using matrices. Gaussian elimination shows that by appropriately changing this matrix $$A$$ and $$b$$, we can write this equation as $$A'x=b'$$, where the matrix $$A'$$ can be chosen to satisfy the two conditions (*).

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> For a given matrix $$A$$, an *elementary row operation* refers to the following three operations:

1. Swapping two entire rows,
2. Multiplying a row by a nonzero constant,
3. Adding a multiple of one row to another row.

</div>

The specific [Example 2](#ex2) we examined was about appropriately manipulating a system of linear equations to satisfy condition (*) and then writing it in a specific way. However, it is worth noting that the calculations examined before that were also essentially obtained from elementary row operations (corresponding equation manipulations).

Also, we define the following.

<div class="definition" markdown="1">

<ins id="def4">**Definition 4**</ins> Let an $$m\times n$$ matrix $$A$$ be given. For any $$1\leq i\leq m$$, if the integer $$j_0(i)=\min\{j\leq n\mid a_{ij}\neq 0\}$$ is well-defined, we call $$a_{i,j_0(i)}$$ the *leading coefficient* of the $$i$$-th row. Additionally, if the following two conditions are satisfied:

1. If $$a_{i1}, a_{i2},\ldots, a_{in}=0$$, then for all $$k$$ satisfying $$i < k$$, $$a_{k1}, a_{k2},\ldots, a_{kn}=0$$.
2. If $$i < i'$$ and both integers $$j_0(i), j_0(i')$$ are well-defined, then necessarily $$j_0(i) < j_0(i')$$.

then we call the matrix $$A$$ a *row echelon matrix*. If additionally

1. $$a_{i, j_0(i)}$$ is always 1, and
2. for all $$i'\neq i$$, $$a_{i', j_0(i)}=0$$

then we call $$A$$ a *reduced row echelon matrix*.

</div>

Therefore, synthesizing the discussion from the previous section, Gaussian elimination can be said to be the process of making a row echelon matrix, or further a reduced row echelon matrix, from a matrix $$A$$ through elementary row operations. Generally, there can be various row echelon forms made from a given matrix $$A$$, but it is well known that the reduced row echelon form is uniquely determined. We do not prove this uniqueness since we will not use it.

Returning to the system of equations (3), swapping the order of each equation, multiplying both sides of each equation by a constant, and adding a multiple of each equation to another equation are familiar solution methods from when we first encountered systems of equations, so they are not strange. However, if we write the same system as $$Ax=b$$ through matrices, it is not clear why elementary row operations applied to $$A$$ affect $$b$$ in the same way. Now, let an arbitrary $$m\times n$$ matrix be given, and let us consider several $$m\times m$$ matrices.

First, $$E_{i,j}$$ is the matrix obtained from the $$m\times m$$ identity matrix $$I$$ by swapping the $$i$$-th and $$j$$-th rows. For example, $$E_{1,2}$$ is the following matrix:

$$E_{1,2}=\begin{pmatrix}0&1&0&\cdots&0\\1&0&0&\cdots&0\\ 0&0&1&\cdots&0\\\vdots&\vdots&\vdots&\ddots&\vdots\\ 0&0&0&\cdots&1\end{pmatrix}$$

On the other hand, $$E'_{i,r}$$ is the matrix obtained by multiplying the $$i$$-th row of the $$m\times m$$ identity matrix $$I$$ by $$r$$. For example, $$E'_{1,r}$$ is the following matrix:

$$E'_{1,r}=\begin{pmatrix}r&0&0&\cdots&0\\0&1&0&\cdots&0\\ 0&0&1&\cdots&0\\\vdots&\vdots&\vdots&\ddots&\vdots\\ 0&0&0&\cdots&1\end{pmatrix}$$

Finally, $$E''_{i,j,r}$$ is the matrix obtained by changing the $$(j,i)$$-entry of the $$m\times m$$ identity matrix $$I$$ to $$r$$. For example, $$E''_{1,2,r}$$ is the following matrix:

$$E''_{1,2,r}=\begin{pmatrix}1&0&0&\cdots&0\\r&1&0&\cdots&0\\ 0&0&1&\cdots&0\\\vdots&\vdots&\vdots&\ddots&\vdots\\ 0&0&0&\cdots&1\end{pmatrix}$$

These are collectively called *elementary matrices*. Now, if we compute $$E_{ij}A$$, $$E'_{i,r}A$$, and $$E''_{i,j,r}A$$ respectively:

1. $$E_{ij}A$$ is the matrix obtained by swapping the $$i$$-th and $$j$$-th rows of $$A$$,
2. $$E'_{i,r}A$$ is the matrix obtained by multiplying the $$i$$-th row of $$A$$ by the constant $$r$$,
3. $$E''_{i,j,r}A$$ is the matrix obtained by adding ($$i$$-th row)$$\times r$$ to the $$j$$-th row of $$A$$

we can easily verify these. That is, performing elementary row operations on matrix $$A$$ is the same as multiplying by the matrices $$E_{ij}$$, $$E_{i,r}'$$, or $$E_{i,j,r}''$$ defined above, and applying the above manipulations to the system of equations $$Ax=b$$ is the same as multiplying both sides on the left by the corresponding elementary matrix $$E$$ to obtain $$(EA)x=(Eb)$$.

All elementary matrices $$E$$ are invertible. This is obvious from the fact that we can apply the elementary row operation corresponding to the elementary matrix to the resulting matrix again to obtain the original matrix.

## Augmented Matrix

Now, when an arbitrary system of linear equations is given, we can manipulate the system to find its solution. As we saw at the beginning of this post, finding the inverse of an arbitrary $$n\times n$$ invertible matrix is nothing more than solving $$n$$ systems of linear equations, so by repeating the above method $$n$$ times for equation (1) needed to find the inverse matrix, we can also find the inverse matrix. The augmented matrix introduced from now on is needed only for notational convenience and the computational convenience that follows from it.

The basic idea is that when performing Gaussian elimination, the columns do not mix with each other, which can also be said to be obvious from the definition of matrix multiplication if we think of elementary row operations as multiplication by the elementary matrices examined above. Moreover, when performing Gaussian elimination, since the right-hand side containing constants is subjected to the same operations as the left-hand side, we can add the components of the right-hand side to the matrix and compute them all at once.

<div class="example" markdown="1">

<ins id="ex5">**Example 5**</ins> Let us use the system of equations given in [Example 2](#ex2):

$$\begin{aligned}x_1+2x_2+4x_3+3x_4&=2\\\phantom{x_1+}3x_2\phantom{+2x_3}+6x_4&=3\\\phantom{x_1+2x_2+}x_3+5x_4&=1\end{aligned}$$

From this system of equations, we consider the following *augmented matrix*:

$$\begin{pmatrix} 1&2&4&3&2\\ 0&3&0&6&3\\ 0&0&1&5&1\end{pmatrix}$$

The rightmost column of this matrix corresponds to the right-hand side of the system of equations, and the rest corresponds to the coefficients in front of the variables of the system of equations. Now, let us apply the same operations as in [Example 2](#ex2) to this matrix. First, subtract 4 times the last row from the first row to obtain the following matrix:

$$\begin{pmatrix}1&2&0&-17&-2\\ 0&3&0&6&3\\0&0&1&5&1\end{pmatrix}$$

Now, subtract $$2/3$$ times the second row from the first row to obtain the following matrix:

$$\begin{pmatrix}1&0&0&-21&-4\\0&3&0&6&3\\0&0&1&5&1\end{pmatrix}$$

and multiply the second row by $$1/3$$ to obtain:

$$\begin{pmatrix}1&0&0&-21&-4\\0&1&0&2&1\\0&0&1&5&1\end{pmatrix}$$

Restoring the system of equations from this augmented matrix, we know that this is exactly what we obtained in [Example 2](#ex2):

$$\begin{aligned}x_1\phantom{+2x_2+4x_3}-21x_4&=-4\\\phantom{x_1+}x_2\phantom{+2x_3}+\phantom{1}2x_4&=1\\\phantom{x_1+2x_2+}x_3+\phantom{1}5x_4&=1\end{aligned}$$

</div>

The example just examined is essentially no different from the calculation of [Example 2](#ex2) (even in terms of convenience). A meaningful difference is obtained when finding the inverse matrix by using the augmented matrix. For this, consider the case where the matrix $$A$$ defining the system of equations (3) is an $$n\times n$$ invertible matrix. First, the following lemma is obvious.

<div class="proposition" markdown="1">

<ins id="lem6">**Lemma 6**</ins> Any $$n\times n$$ reduced row echelon matrix is either the identity matrix or has a column consisting only of $$0$$s.

</div>

As mentioned earlier, all elementary matrices are invertible, and we can restore the original matrix by multiplying the inverses of the elementary row operations we performed on the reduced row echelon form of the given matrix in order. That is, if some $$n\times n$$ matrix has a column consisting only of $$0$$s, then this matrix is not invertible, and therefore the original matrix cannot be invertible. In other words, the reduced row echelon form of an $$n\times n$$ matrix is the identity matrix.

Now, when an arbitrary $$n\times n$$ invertible matrix is given, we can solve the $$n$$ systems of equations $$Av_i=e_i$$ all at once using the augmented matrix. That is, by appending $$e_1,\ldots, e_n$$ all at once to form the $$2n\times n$$ matrix $$(A\mid I_n)$$, and converting this to reduced row echelon form, the rear $$n\times n$$ matrix becomes the inverse of the original matrix.

<div class="example" markdown="1">

<ins id="ex7">**Example 7**</ins> Let us find the inverse of the following matrix:

$$A=\begin{pmatrix}1&2&4\\ 0&3&0\\ 0&0&1\end{pmatrix}$$

The augmented matrix is

$$(A\mid I_3)=\begin{pmatrix}1&2&4&1&0&0\\0&3&0&0&1&0\\ 0&0&1&0&0&1\end{pmatrix}$$

and first, subtracting 4 times the last row from the first row gives the following matrix:

$$\begin{pmatrix}1&2&0&1&0&-4\\ 0&3&0&0&1&0\\0&0&1&0&0&1\end{pmatrix}$$

Now, subtracting $$2/3$$ times the second row from the first row gives the following matrix:

$$\begin{pmatrix}1&0&0&1&-2/3&-4\\0&3&0&0&1&0\\0&0&1&0&0&1\end{pmatrix}$$

and finally, multiplying the second row by $$1/3$$ gives:

$$\begin{pmatrix}1&0&0&1&-2/3&-4\\0&1&0&0&1/3&0\\0&0&1&0&0&1\end{pmatrix}$$

That is, the inverse of the given matrix $$A$$ is

$$A^{-1}=\begin{pmatrix}1&-2/3&-4\\0&1/3&0\\0&0&1\end{pmatrix}$$

</div>

## LU Decomposition

Earlier, we examined Gaussian elimination from the perspective of elementary row operations. Now, if we organize the same process in terms of matrix multiplication, we can see that any matrix can be decomposed into the product of two triangular matrices.

<div class="definition" markdown="1">

<ins id="def8">**Definition 8**</ins> For a square matrix $$A$$, when $$A$$ is decomposed as $$A=LU$$, if $$L$$ is a lower triangular matrix with all diagonal entries equal to $$1$$ and $$U$$ is an upper triangular matrix, we call this the *LU decomposition* of $$A$$.

</div>

Consider a matrix for which Gaussian elimination can be performed without row exchanges and without multiplying an entire row by a constant. That is, suppose that using only the elementary row operation of "adding a multiple of one row to another row," we can obtain an upper triangular matrix $$U$$. If the elementary matrices used in this process are $$E_1,E_2,\ldots,E_k$$ in order, then

$$E_k\cdots E_2E_1A=U$$

holds. Here, each $$E_i$$ is an elementary matrix in the form of a lower triangular matrix with diagonal entries equal to $$1$$, so its inverse $$E_i^{-1}$$ is also a lower triangular matrix with diagonal entries equal to $$1$$, and the product of these also maintains the same form. Therefore, we can write:

$$A=(E_1^{-1}\cdots E_k^{-1})U$$

and setting $$L=E_1^{-1}\cdots E_k^{-1}$$, we obtain $$A=LU$$.

Of course, to perform Gaussian elimination in this way, the pivot to be used at each step must be nonzero. That is, LU decomposition exists only when this condition is satisfied. The following is a summary of this result.

<div class="proposition" markdown="1">

<ins id="thm9">**Theorem 9**</ins> For a square matrix $$A$$, the following holds.

1. If Gaussian elimination can be performed without row exchanges and without multiplying a row by a constant, then $$A$$ has an LU decomposition.
2. If both $$A=LU$$ and $$A=L'U'$$ are LU decompositions with the diagonal entries of $$L,L'$$ equal to $$1$$, then $$L=L'$$ and $$U=U'$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Existence is obvious from the above discussion. Let us show uniqueness. If $$LU=L'U'$$, then since $$L'$$ is invertible,

$$(L')^{-1}L=U'(U)^{-1}$$

The left side is the product of two lower triangular matrices, so it is a lower triangular matrix, and the right side is the product of two upper triangular matrices, so it is an upper triangular matrix. Therefore, both sides are diagonal matrices. Moreover, since the diagonal entries of $$L$$ and $$(L')^{-1}$$ are all $$1$$, the diagonal entries of the left side are also all $$1$$. That is, both sides are the identity matrix, and we obtain $$L=L'$$, $$U=U'$$.

</details>

The usefulness of LU decomposition is prominent when solving the system of equations $$Ax=b$$. If $$A=LU$$ is decomposed, then $$Ax=b$$ can be written as $$L(Ux)=b$$, and we solve this by separating it into:

$$Ly=b,\qquad Ux=y$$

Each equation is a system of equations for a lower triangular or upper triangular matrix, so the solution can be found by simple forward or backward substitution.

<div class="example" markdown="1">

<ins id="ex10">**Example 10**</ins> Consider the matrix

$$A=\begin{pmatrix}2&1&1\\4&3&3\\8&7&9\end{pmatrix}$$

Multiply the first row by $$-2$$ and add it to the second row, and multiply by $$-4$$ and add it to the third row to obtain:

$$U_1=\begin{pmatrix}2&1&1\\0&1&1\\0&3&5\end{pmatrix}$$

Next, multiply the second row by $$-3$$ and add it to the third row to obtain:

$$U=\begin{pmatrix}2&1&1\\0&1&1\\0&0&2\end{pmatrix}$$

Multiplying the inverses of the elementary matrices used here gives:

$$L=\begin{pmatrix}1&0&0\\2&1&0\\4&3&1\end{pmatrix}$$

and we can verify that $$A=LU$$.

</div>

However, (mainly for small matrices) applying Gaussian elimination every time to determine whether a matrix is invertible can sometimes be inefficient. The determinant, which we will examine in the next post, tells us whether a given $$n\times n$$ matrix is invertible or not. However, (especially for complex matrices) one of the easiest ways to compute the determinant is still Gaussian elimination. ([§Existence and Uniqueness of the Determinant, ⁋Proposition 8](/en/math/linear_algebra/existence_and_uniqueness_of_determinant#prop8))

---

**References**

**[Lee]** 이인석, *선형대수와 군*, 서울대학교 출판문화원, 2005.

---
