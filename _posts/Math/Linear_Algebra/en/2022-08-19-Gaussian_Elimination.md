---
title: "Gaussian Elimination"
description: "We explore how to compute the inverse of a matrix using Gaussian elimination and prove the equivalent conditions for an invertible matrix. Based on the relationship between matrices and linear transformations, we analyze the equivalence relation determined by rank."
excerpt: "Gaussian elimination and inverse matrices"

categories: [Math / Linear Algebra]
permalink: /en/math/linear_algebra/Gaussian_elimination
sidebar: 
    nav: "linear_algebra-en"


date: 2022-08-19
last_modified_at: 2022-08-19

weight: 12
translated_at: 2026-06-01T00:30:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-01T00:30:04+00:00
---
In the previous post, we saw that linear maps between vector spaces are essentially the same as matrices. From this perspective, if two $$m\times n$$ matrices $$A, B$$ satisfy

$$B=PAQ\tag{1}$$

for suitable invertible matrices $$P, Q$$, one might be tempted to regard $$A$$ and $$B$$ as essentially the same matrix. Yet if we allow complete freedom in choosing bases for the vector spaces $$V, W$$ on which $$L_A, L_B: V\rightarrow W$$ act, we saw that any two matrices of the same rank must be treated as identical. This is why in [§Fundamental Theorem of Linear Algebra, ⁋Definition 8](/en/math/linear_algebra/ftla#def8) we were forced to define a finer equivalence relation. Roughly speaking, if the only information retained in matrix $$A$$ in equation (1) is its rank, then the remaining information is encoded in $$P$$ and $$Q$$—that is, in the *linear operators* from $$V$$ to $$V$$ and from $$W$$ to $$W$$. Fixing a basis of $$V$$ (or $$W$$) to examine these operators makes the equivalence relation quite natural. Henceforth, our discussion proceeds with a fixed vector space $$V$$ and basis $$\mathcal{B}$$; in other words, we focus on $$n\times n$$ matrices. A powerful tool for this purpose is the determinant, which we shall define in the next post.

Meanwhile, we proved that any invertible matrix must be square, using the trace ([§Matrices, ⁋Definition 7](/en/math/linear_algebra/matrices#def7)). Now that we know matrices and linear maps are the same, this result is immediate from [§Isomorphisms, ⁋Corollary 4](/en/math/linear_algebra/isomorphic_vector_spaces#cor4). However, we have not yet examined how to compute an inverse matrix. The method is simple enough that we could have presented it right after [§Matrices](/en/math/linear_algebra/matrices), but now that we have begun a serious study of $$n\times n$$ matrices, we briefly introduce it here.

First, we prove a simple lemma.

<div class="proposition" markdown="1">

<ins id="lem1">**Lemma 1**</ins> For a matrix $$A\in\Mat_n(\mathbb{K})$$, the following three conditions are equivalent.

1. $$A$$ is invertible.
2. There exists $$B\in\Mat_n(\mathbb{K})$$ such that $$AB=I$$.
3. There exists $$B\in\Mat_n(\mathbb{K})$$ such that $$BA=I$$.

Moreover, if either (2) or (3) holds, then $$B=A^{-1}$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

That (1) implies each of (2) and (3) is obvious, so it suffices to prove the converses.

First, assume there exists $$B\in\Mat_n(\mathbb{K})$$ with $$AB=I$$. By the fundamental theorem of linear algebra,

$$L_A\circ L_B=\id_{\mathbb{K}^n}$$

Since $$\id_{\mathbb{K}^n}$$ is bijective, $$L_A:\mathbb{K}^n\rightarrow \mathbb{K}^n$$ is surjective. ([\[Set Theory\] §Retraction and Section, ⁋Proposition 3](/en/math/set_theory/retraction_and_section#prop3)) Therefore, from the rank-nullity theorem ([§Isomorphisms, ⁋Theorem 7](/en/math/linear_algebra/isomorphic_vector_spaces#thm7))

$$\rank L_A+\nullity L_A=\dim \mathbb{K}^n=n$$

we obtain $$\nullity L_A=0$$. Thus $$L_A$$ is injective as well, hence bijective, and so $$A$$ is invertible. Multiplying both sides of $$AB=I$$ on the left by $$A^{-1}$$ yields $$B=A^{-1}$$.

The implication from (3) to (1) is proved similarly.

</details>

Of course, regarding matrices and linear maps as identical, this is obvious because the inverse function satisfies the same property.

Now let an arbitrary invertible $$n\times n$$ matrix $$B$$ be given. Regarding $$B$$ as a linear map $$\mathbb{K}^n\rightarrow\mathbb{K}^n$$, it is completely determined by where it sends the basis $$e_1,\ldots, e_n$$ of $$\mathbb{K}^n$$. Consequently, to compute $$A^{-1}$$ it suffices to know where $$A^{-1}$$ sends each basis vector $$e_i$$. Denoting this vector by $$v_i$$, the matrix $$A^{-1}$$ is given by $$(v_1\mid v_2\mid\cdots\mid v_n)$$, where each $$v_i$$ satisfies

$$v_i=A^{-1}e_i\iff Av_i=e_i\tag{2}$$

## Gauss–Jordan Elimination

Consider the system of linear equations

$$\begin{aligned}a_{11}x_{1}+a_{12}x_2+\cdots+a_{1n}x_n&=b_1\\a_{21}x_1+a_{22}x_2+\cdots+a_{2n}x_n&=b_2\\\hspace{10pt}\vdots&\\a_{mn}x_1+a_{m2}x_2+\cdots+a_{mn}x_n&=b_m\end{aligned}\tag{3}$$

By [§Matrices, ⁋Definition 2](/en/math/linear_algebra/matrices#def2), this system can be written using the matrices

$$A=\begin{pmatrix}a_{11}&a_{12}&\cdots&a_{1n}\\a_{21}&a_{22}&\cdots&a_{2n}\\\vdots&\vdots&\ddots&\vdots\\a_{m1}&a_{m2}&\cdots&a_{mn}\end{pmatrix},\quad x=\begin{pmatrix}x_1\\x_2\\\vdots\\x_n\end{pmatrix},\quad b=\begin{pmatrix}b_1\\b_2\\\vdots\\b_m\end{pmatrix}$$

as $$Ax=b$$. If $$m=n$$ and $$A$$ is invertible, the solution is uniquely determined by

$$x=A^{-1}b\iff Ax=b$$

which is precisely the equation we need for computing the inverse. If $$m\neq n$$ or $$A$$ is not invertible, the system may have no solution or infinitely many. We now examine *Gaussian elimination*, which remains useful in these cases.

Suppose there exists an integer $$1\leq i\leq n$$ such that $$a_{ji}=0$$ for all $$j$$ among the coefficients of (3). Then if

$$x_1=c_1,\quad x_2=c_2,\quad \ldots,\quad x_i=c_i,\quad\ldots,\quad x_n=c_n$$

is one solution of (3), the tuple obtained by replacing $$x_i$$ with an arbitrary $$d_i$$,

$$x_1=c_1,\quad x_2=c_2,\quad\ldots,\quad x_i=d_i,\quad\ldots,\quad x_n=c_n$$

is also a solution. Hence if all $$a_{ij}$$ are zero, then (3) has every vector in $$\mathbb{K}^n$$ as a solution when $$b$$ is the zero vector, and no solution otherwise. To exclude such trivial cases, we assume that at least one $$a_{ij}$$ is nonzero.

Define $$k$$ to be <phrase>the smallest integer for which there exists $$1\leq j\leq m$$ with $$a_{jk}\neq 0$$</phrase>, and for this fixed $$k$$ choose the smallest $$j$$ satisfying $$a_{jk}\neq 0$$. Moving the $$j$$-th equation to the top,

$$\begin{aligned}a_{j1}x_{1}+a_{j2}x_2+\cdots+a_{jn}x_n&=b_j\\a_{11}x_1+a_{12}x_2+\cdots+a_{1n}x_n&=b_1\\\hspace{10pt}\vdots&\\a_{mn}x_1+a_{m2}x_2+\cdots+a_{mn}x_n&=b_m\end{aligned}$$

the definition of $$a_{jk}$$ ensures that $$a_{j1},a_{j2},\ldots, a_{j,(k-1)}$$ and all coefficients below them are zero. For each equation

$$a_{i1}x_1+a_{i2}x_2+\cdots+a_{in}x_n=b_i$$

multiply the first equation by $$-a_{ik}/a_{jk}$$ and add:

$$\left(a_{i1}-\frac{a_{ik}}{a_{jk}}a_{j1}\right)x_1+\left(a_{i2}-\frac{a_{ik}}{a_{jk}}a_{j2}\right)x_2+\cdots+\left(a_{ik}-\frac{a_{ik}}{a_{jk}}a_{jk}\right)x_k+\cdots+\left(a_{in}-\frac{a_{ik}}{a_{jk}}a_{jn}\right)x_n=b_i-\frac{a_{ik}}{a_{jk}}b_k$$

The coefficients of $$x_1,\ldots, x_{k-1}$$ were already zero, and this operation makes the coefficient of $$x_k$$ zero as well. Thus after this process, the coefficients of $$x_1,\ldots, x_{k-1}$$ are all zero, and among the coefficients of $$x_k$$ only the first row has a nonzero entry.

Repeating this process for the $$n-1$$ equations from the second row to the last, then for the $$n-2$$ equations from the third row to the last, and so on until the last row, we arrive at a system satisfying the following two conditions (*).

1. Any equation all of whose coefficients are zero appears at the very bottom.
2. For any equation not identically zero, its first nonzero coefficient lies strictly to the right of the first nonzero coefficient in the equation above it.


<div class="example" markdown="1">

<ins id="ex2">**Example 2**</ins> The following system satisfies the two conditions above.

$$\begin{aligned}x_1+2x_2+4x_3+3x_4&=2\\\phantom{x_1+}3x_2\phantom{+2x_3}+6x_4&=3\\\phantom{x_1+2x_2+}x_3+5x_4&=1\end{aligned}$$

With a little further manipulation we can read off the solution immediately. Call the first nonzero coefficient in each equation the *leading coefficient*. In the system above, the leading coefficients are 1 (coefficient of $$x_1$$ in the first equation), 3 (coefficient of $$x_2$$ in the second), and 1 (coefficient of $$x_3$$ in the third).

Now eliminate all coefficients above each leading coefficient. That is, we must eliminate $$4x_3$$ above the leading coefficient of the last equation, and $$2x_2$$ above that of the second. To do this, multiply the last equation by 4 and subtract from the first, and multiply the second equation by $$2/3$$ and subtract from the first. Multiplying the second equation by $$1/3$$ to simplify, we obtain

$$\begin{aligned}x_1\phantom{+2x_2+4x_3}-21x_4&=-4\\\phantom{x_1+}x_2\phantom{+2x_3}+\phantom{1}2x_4&=1\\\phantom{x_1+2x_2+}x_3+\phantom{1}5x_4&=1\end{aligned}$$

From this, the general solution of the system is

$$x_1=-4+21x_4,\quad x_2=1-2x_4,\quad x_3=1-5x_4$$

</div>

The procedure described above for solving systems of linear equations is called *Gaussian elimination* or *Gauss–Jordan elimination*.

## Elementary Row Operations and Gaussian Elimination

The system (3) could be expressed compactly as $$Ax=b$$. Gaussian elimination shows that $$A$$ and $$b$$ can be transformed so that the system becomes $$A'x=b'$$, where $$A'$$ satisfies conditions (*).

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> For a given matrix $$A$$, an *elementary row operation* is one of the following three operations.

1. Interchanging two rows,
2. Multiplying a row by a nonzero constant,
3. Adding a multiple of one row to another row.

</div>

[Example 2](#ex2), which we examined in detail, concerned manipulating a system to satisfy (*) and then writing it in a specific form; however, it should be noted that the calculations examined earlier were also essentially obtained from elementary row operations (the corresponding equation manipulations).

We also make the following definition.

<div class="definition" markdown="1">

<ins id="def4">**Definition 4**</ins> Let an $$m\times n$$ matrix $$A$$ be given. If for each $$1\leq i\leq m$$ the integer $$j_0(i)=\min\{j\leq n\mid a_{ij}\neq 0\}$$ is well defined, we call $$a_{i,j_0(i)}$$ the *leading coefficient* of the $$i$$-th row. If furthermore

1. whenever $$a_{i1}=a_{i2}=\cdots=a_{in}=0$$, we have $$a_{k1}=a_{k2}=\cdots=a_{kn}=0$$ for all $$k>i$$;
2. whenever $$i<i'$$ and both $$j_0(i), j_0(i')$$ are well defined, we have $$j_0(i)<j_0(i')$$;

then $$A$$ is called a *row echelon matrix* (REF). If in addition

1. $$a_{i, j_0(i)}=1$$ for all $$i$$, and
2. $$a_{i', j_0(i)}=0$$ for all $$i'\neq i$$,

then $$A$$ is called a *reduced row echelon matrix* (RREF).

</div>

Summarizing the discussion of the preceding section, Gaussian elimination is the process of transforming a matrix $$A$$ into row echelon form, or further into reduced row echelon form, by elementary row operations. In general, the row echelon form of a given matrix need not be unique, but the reduced row echelon form is uniquely determined. We omit the proof of this uniqueness, as we shall have no occasion to use it.

Returning to the system (3): interchanging equations, multiplying both sides by a constant, or adding a multiple of one equation to another are familiar operations from the very first encounter with linear systems. Yet when the same system is written as $$Ax=b$$, it is not immediately obvious why elementary row operations applied to $$A$$ affect $$b$$ in the same way. Let an arbitrary $$m\times n$$ matrix be given, and consider several $$m\times m$$ matrices.

First, $$E_{i,j}$$ is the matrix obtained from the $$m\times m$$ identity matrix $$I$$ by interchanging the $$i$$-th and $$j$$-th rows. For example, $$E_{1,2}$$ is

$$E_{1,2}=\begin{pmatrix}0&1&0&\cdots&0\\1&0&0&\cdots&0\\ 0&0&1&\cdots&0\\\vdots&\vdots&\vdots&\ddots&\vdots\\ 0&0&0&\cdots&1\end{pmatrix}$$

Next, $$E'_{i,r}$$ is the matrix obtained by multiplying the $$i$$-th row of $$I$$ by $$r$$. For example, $$E'_{1,r}$$ is

$$E'_{1,r}=\begin{pmatrix}r&0&0&\cdots&0\\0&1&0&\cdots&0\\ 0&0&1&\cdots&0\\\vdots&\vdots&\vdots&\ddots&\vdots\\ 0&0&0&\cdots&1\end{pmatrix}$$

Finally, $$E''_{i,j,r}$$ is the matrix obtained by replacing the $$(j,i)$$-entry of $$I$$ with $$r$$. For example, $$E''_{1,2,r}$$ is

$$E''_{1,2,r}=\begin{pmatrix}1&0&0&\cdots&0\\r&1&0&\cdots&0\\ 0&0&1&\cdots&0\\\vdots&\vdots&\vdots&\ddots&\vdots\\ 0&0&0&\cdots&1\end{pmatrix}$$

These are collectively called *elementary matrices*. Computing $$E_{ij}A$$, $$E'_{i,r}A$$, and $$E''_{i,j,r}A$$, one easily verifies that

1. $$E_{ij}A$$ is the matrix obtained by interchanging the $$i$$-th and $$j$$-th rows of $$A$$;
2. $$E'_{i,r}A$$ is the matrix obtained by multiplying the $$i$$-th row of $$A$$ by $$r$$;
3. $$E''_{i,j,r}A$$ is the matrix obtained by adding $$r$$ times the $$i$$-th row to the $$j$$-th row of $$A$$.

Thus performing an elementary row operation on $$A$$ is equivalent to multiplying on the left by the corresponding elementary matrix $$E$$; and applying this manipulation to the system $$Ax=b$$ yields $$(EA)x=(Eb)$$.

All elementary matrices are invertible. This is clear because applying the "inverse" elementary row operation to a matrix recovers the original matrix.

## Augmented Matrix

Given an arbitrary system of linear equations, we can manipulate it to find its solution. As observed at the beginning of this post, finding the inverse of an invertible $$n\times n$$ matrix amounts to solving $$n$$ systems of linear equations, so by repeating the above method $$n$$ times for equation (2), we can obtain the inverse matrix. The augmented matrix, introduced next, serves purely for notational and computational convenience.

The basic idea is that during Gaussian elimination the columns never mix; this is obvious from the definition of matrix multiplication once elementary row operations are viewed as multiplication by elementary matrices. Moreover, since the right-hand side undergoes exactly the same operations as the left-hand side, we can append the constants to the matrix and perform all computations at once.

<div class="example" markdown="1">

<ins id="ex5">**Example 5**</ins> Take the system from [Example 2](#ex2):

$$\begin{aligned}x_1+2x_2+4x_3+3x_4&=2\\\phantom{x_1+}3x_2\phantom{+2x_3}+6x_4&=3\\\phantom{x_1+2x_2+}x_3+5x_4&=1\end{aligned}$$

From this system we form the *augmented matrix*

$$\begin{pmatrix} 1&2&4&3&2\\ 0&3&0&6&3\\ 0&0&1&5&1\end{pmatrix}$$

The rightmost column corresponds to the right-hand side, and the remaining columns to the coefficients. Applying the operations from [Example 2](#ex2): first, subtract 4 times the last row from the first:

$$\begin{pmatrix}1&2&0&-17&-2\\ 0&3&0&6&3\\0&0&1&5&1\end{pmatrix}$$

Next, multiply the second row by $$2/3$$ and subtract from the first:

$$\begin{pmatrix}1&0&0&-21&-4\\0&3&0&6&3\\0&0&1&5&1\end{pmatrix}$$

Finally, multiply the second row by $$1/3$$:

$$\begin{pmatrix}1&0&0&-21&-4\\0&1&0&2&1\\0&0&1&5&1\end{pmatrix}$$

Restoring the system from this augmented matrix yields exactly what we obtained in [Example 2](#ex2):

$$\begin{aligned}x_1\phantom{+2x_2+4x_3}-21x_4&=-4\\\phantom{x_1+}x_2\phantom{+2x_3}+\phantom{1}2x_4&=1\\\phantom{x_1+2x_2+}x_3+\phantom{1}5x_4&=1\end{aligned}$$

</div>

The example just examined is essentially no different from the calculation in [Example 2](#ex2), even in convenience. A meaningful difference arises when the augmented matrix is used to find an inverse. For this, consider the case where the matrix $$A$$ defining (3) is an invertible $$n\times n$$ matrix. First, the following lemma is obvious.

<div class="proposition" markdown="1">

<ins id="lem6">**Lemma 6**</ins> Every $$n\times n$$ reduced row echelon matrix is either the identity matrix or has a column of all zeros.

</div>

As noted earlier, elementary matrices are all invertible, and we can recover the original matrix from its reduced row echelon form by multiplying, in order, by the inverses of the elementary matrices used. Hence if an $$n\times n$$ matrix has a column of all zeros, it is not invertible, and neither was the original matrix. Equivalently, the reduced row echelon form of an invertible $$n\times n$$ matrix is the identity matrix.

Now, given an arbitrary invertible $$n\times n$$ matrix, we can solve the $$n$$ systems $$Av_i=e_i$$ simultaneously using the augmented matrix. Augmenting $$e_1,\ldots, e_n$$ all at once gives the $$n\times 2n$$ matrix $$(A\mid I_n)$$; converting this to reduced row echelon form makes the right-hand $$n\times n$$ block the inverse of the original matrix.

<div class="example" markdown="1">

<ins id="ex7">**Example 7**</ins> Let us find the inverse of

$$A=\begin{pmatrix}1&2&4\\ 0&3&0\\ 0&0&1\end{pmatrix}$$

The augmented matrix is

$$(A\mid I_3)=\begin{pmatrix}1&2&4&1&0&0\\0&3&0&0&1&0\\ 0&0&1&0&0&1\end{pmatrix}$$

Subtracting 4 times the last row from the first:

$$\begin{pmatrix}1&2&0&1&0&-4\\ 0&3&0&0&1&0\\0&0&1&0&0&1\end{pmatrix}$$

Multiplying the second row by $$2/3$$ and subtracting from the first:

$$\begin{pmatrix}1&0&0&1&-2/3&-4\\0&3&0&0&1&0\\0&0&1&0&0&1\end{pmatrix}$$

Finally, multiplying the second row by $$1/3$$:

$$\begin{pmatrix}1&0&0&1&-2/3&-4\\0&1&0&0&1/3&0\\0&0&1&0&0&1\end{pmatrix}$$

Thus the inverse of $$A$$ is

$$A^{-1}=\begin{pmatrix}1&-2/3&-4\\0&1/3&0\\0&0&1\end{pmatrix}$$

</div>

However, applying Gaussian elimination every time to test invertibility—especially for small matrices—can be inefficient. The determinant, which we shall examine in the next post, provides a criterion for invertibility. Yet even for determinants, one of the easiest computational methods—especially for complicated matrices—remains Gaussian elimination. ([§Existence and Uniqueness of the Determinant, ⁋Proposition 9](/en/math/linear_algebra/existence_and_uniqueness_of_determinant#prop9))

---

**References**

**[Lee]** 이인석, *선형대수와 군*, 서울대학교 출판문화원, 2005.

---
