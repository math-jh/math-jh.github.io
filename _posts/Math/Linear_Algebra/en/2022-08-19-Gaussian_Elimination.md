---
title: "Gaussian Elimination"
excerpt: "Gaussian elimination and inverse matrices"

categories: [Math / Linear Algebra]
permalink: /en/math/linear_algebra/Gaussian_elimination
sidebar: 
    nav: "linear_algebra-en"

header:
    overlay_image: /assets/images/Math/Linear_Algebra/Gaussian_Elimination.png
    overlay_filter: 0.5

date: 2022-08-19
last_modified_at: 2022-08-19

weight: 12
translated_at: 2026-05-23T11:00:02+00:00
translation_source: kimi-cli
---
In the previous post, we saw that linear maps between vector spaces are essentially identical to matrices. From this viewpoint, if two $$m\times n$$ matrices $$A, B$$ satisfy the following equation for suitable invertible matrices $$P, Q$$

$$B=PAQ\tag{1}$$

one might want to think of these matrices $$A, B$$ as essentially the same matrix. However, if we allow complete freedom in choosing the bases of the two vector spaces $$V, W$$ on which these matrices $$L_A, L_B: V\rightarrow W$$ act, we saw that two matrices of the same rank must all be treated as the same matrix. Therefore, in [§Fundamental Theorem of Linear Algebra, ⁋Definition 8](/en/math/linear_algebra/ftla#def8) we had to define a finer equivalence relation. Roughly speaking, if the only information contained in matrix $$A$$ in equation (1) is its rank, then the remaining information is contained in the matrices $$P, Q$$, i.e., in the *linear operators* from $$V$$ to $$V$$ or from $$W$$ to $$W$$. If we fix a basis of $$V$$ (or $$W$$) to examine these, this equivalence relation is not so unnatural. Thus, for the time being, our discussion will proceed with a fixed vector space $$V$$ and basis $$\mathcal{B}$$. In other words, we will examine $$n\times n$$ matrices. A powerful tool for this is the determinant, which we will define in the next post.

Meanwhile, we proved that for any matrix $$A$$ to be invertible it must be a square matrix, using the trace of a matrix ([§Matrices, ⁋Definition 7](/en/math/linear_algebra/matrices#def7)). Now that we know matrices and linear maps are the same, this result is obvious from [§Isomorphic Vector Spaces, ⁋Theorem 4](/en/math/linear_algebra/isomorphic_vector_spaces#cor4). However, we have not yet examined how to compute this inverse matrix. Since this method is simple, we could have examined it right after [§Matrices](/en/math/linear_algebra/matrices), but now that we have begun to seriously study $$n\times n$$ matrices, we briefly introduce this procedure.

First, let us prove the following simple lemma.

<div class="proposition" markdown="1">

<ins id="lem1">**Lemma 1**</ins> For a matrix $$A\in\Mat_n(\mathbb{K})$$, the following three conditions are all equivalent.

1. $$A$$ is invertible.
2. There exists a suitable $$B\in\Mat_n(\mathbb{K})$$ such that $$AB=I$$.
3. There exists a suitable $$B\in\Mat_n(\mathbb{K})$$ such that $$BA=I$$.

Moreover, if the second or third condition holds, then $$B=A^{-1}$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

That the first condition implies each of the second and third is obvious, so it suffices to show the converse.

First, assume there exists a suitable $$B\in\Mat_n(\mathbb{K})$$ such that $$AB=I$$ holds. Then by the fundamental theorem of linear algebra

$$L_A\circ L_B=\id_{\mathbb{K}^n}$$

holds. Now, since $$\id_{\mathbb{K}^n}$$ is a bijection, we know that $$L_A:\mathbb{K}^n\rightarrow \mathbb{K}^n$$ is surjective. ([\[Set Theory\] §Retractions and Sections, ⁋Proposition 3](/en/math/set_theory/retraction_and_section#prop3)) Therefore, from the following equation ([§Isomorphic Vector Spaces, ⁋Theorem 7](/en/math/linear_algebra/isomorphic_vector_spaces#thm7))

$$\rank L_A+\nullity L_A=\dim \mathbb{K}^n=n$$

we know that $$\nullity L_A=0$$. That is, $$L_A$$ is also injective, and thus $$L_A$$ is bijective and the matrix $$A$$ is invertible. Now, multiplying both sides of the equation $$AB=I$$ on the left by $$A^{-1}$$, we obtain $$B=A^{-1}$$.

Similarly, one can prove that the third condition implies the first.

</details>

Of course, thinking again that matrices and linear maps are the same, this is obvious because the inverse function satisfies the same property.

Now suppose an arbitrary invertible $$n\times n$$ matrix $$B$$ is given. Thinking of $$B$$ as a linear map from $$\mathbb{K}^n$$ to $$\mathbb{K}^n$$, $$B$$ is completely determined by where it sends the basis $$e_1,\ldots, e_n$$ of $$\mathbb{K}^n$$. Therefore, to compute the matrix $$A^{-1}$$, it suffices to know where $$A^{-1}$$ sends each basis vector $$e_i$$. Let this vector be $$v_i$$; then the matrix $$A^{-1}$$ is given by $$(v_1\mid v_2\mid\cdots\mid v_n)$$, where each $$v_i$$ is defined by the following equation

$$v_i=A^{-1}e_i\iff Av_i=e_i\tag{2}$$

## Gaussian-Jordan Elimination

Now consider the following system of linear equations

$$\begin{aligned}a_{11}x_{1}+a_{12}x_2+\cdots+a_{1n}x_n&=b_1\\a_{21}x_1+a_{22}x_2+\cdots+a_{2n}x_n&=b_2\\\hspace{10pt}\vdots&\\a_{mn}x_1+a_{m2}x_2+\cdots+a_{mn}x_n&=b_m\end{aligned}\tag{3}$$

Then by [§Matrices, ⁋Definition 2](/en/math/linear_algebra/matrices#def2), the above equation can be written using the following matrices

$$A=\begin{pmatrix}a_{11}&a_{12}&\cdots&a_{1n}\\a_{21}&a_{22}&\cdots&a_{2n}\\\vdots&\vdots&\ddots&\vdots\\a_{m1}&a_{m2}&\cdots&a_{mn}\end{pmatrix},\quad x=\begin{pmatrix}x_1\\x_2\\\vdots\\x_n\end{pmatrix},\quad b=\begin{pmatrix}b_1\\b_2\\\vdots\\b_m\end{pmatrix}$$

as $$Ax=b$$. If $$m=n$$ and the inverse of matrix $$A$$ exists, then the solution of this system of equations is uniquely determined by the following equation

$$x=A^{-1}b\iff Ax=b$$

and this is exactly the equation we need to find the inverse matrix. If $$m\neq n$$ or the inverse of $$A$$ does not exist, the above system of linear equations may have no solution, or infinitely many solutions. We examine *Gaussian elimination*, which is useful even in this case.

Assume there exists an integer $$1\leq i\leq n$$ such that $$a_{ji}=0$$ holds for all $$j$$ among the coefficients of equation (3). In this case, if

$$x_1=c_1,\quad x_2=c_2,\quad \ldots,\quad x_i=c_i,\quad\ldots,\quad x_n=c_n$$

is one solution of equation (3), then the following tuple obtained by changing the value of $$x_i$$ to an arbitrary $$d_i$$

$$x_1=c_1,\quad x_2=c_2,\quad\ldots,\quad x_i=d_i,\quad\ldots,\quad x_n=c_n$$

is also a solution of equation (3). Therefore, if all $$a_{ij}$$ are $$0$$, then if $$b$$ is the zero vector, equation (3) has every tuple in $$\mathbb{K}^n$$ as a solution; otherwise, no solution exists. To avoid such trivial cases, we assume that at least one $$a_{ij}$$ is not zero.

Now define the integer $$k$$ to be <phrase>the smallest integer among those for which there exists $1\leq j\leq m$ such that $a_{jk}\neq 0$</phrase>, and for this fixed $$k$$, choose the smallest integer $$j$$ satisfying $$a_{jk}\neq 0$$. Now the $$j$$-th equation

$$a_{j1}x_1+a_{j2}x_2+\cdots+a_{jk}x_k+\cdots+a_{nk}x_n=b_j$$

is moved to the very top of the system

$$\begin{aligned}a_{j1}x_{1}+a_{j2}x_2+\cdots+a_{jn}x_n&=b_j\\a_{11}x_1+a_{12}x_2+\cdots+a_{1n}x_n&=b_1\\\hspace{10pt}\vdots&\\a_{mn}x_1+a_{m2}x_2+\cdots+a_{mn}x_n&=b_m\end{aligned}$$

then by the definition of $$a_{jk}$$, the coefficients $$a_{j1},a_{j2},\ldots, a_{j,(k-1)}$$ and those below them must all be $$0$$. Now for each equation

$$a_{i1}x_1+a_{i2}x_2+\cdots+a_{in}x_n=b_i$$

we multiply the first equation by $$-a_{ik}/a_{jk}$$ and add it to obtain

$$\left(a_{i1}-\frac{a_{ik}}{a_{jk}}a_{j1}\right)x_1+\left(a_{i2}-\frac{a_{ik}}{a_{jk}}a_{j2}\right)x_2+\cdots+\left(a_{ik}-\frac{a_{ik}}{a_{jk}}a_{jk}\right)x_k+\cdots+\left(a_{in}-\frac{a_{ik}}{a_{jk}}a_{jn}\right)x_n=b_i-\frac{a_{ik}}{a_{jk}}b_k$$

In the above equation, the coefficients of $$x_1,\ldots, x_{k-1}$$ were already all zero, and through the operation just performed, the coefficient of $$x_k$$ also becomes zero. That is, after this process, the coefficients of $$x_1,\ldots, x_{k-1}$$ are all zero, and among the coefficients of $$x_k$$, the only nonzero one lies in the first row.

Now repeat this process for the $$n-1$$ equations from the second row to the last row, and again for the $$n-2$$ equations from the third row to the last row. Continuing this until we reach the last row, equation (3) finally satisfies the following two conditions (\*).

1. If there is an equation all of whose coefficients are zero, it is located at the very bottom of the system.
2. For any equation not all of whose coefficients are zero, the first nonzero coefficient in that equation appears to the right of the first nonzero coefficient in the equation above it.


<div class="example" markdown="1">

<ins id="ex2">**Example 2**</ins> The following system of equations satisfies the two conditions above.

$$\begin{aligned}x_1+2x_2+4x_3+3x_4&=2\\\phantom{x_1+}3x_2\phantom{+2x_3}+6x_4&=3\\\phantom{x_1+2x_2+}x_3+5x_4&=1\end{aligned}$$

With a little additional manipulation, we can immediately obtain the solution of the system from this equation. Let us call the first nonzero coefficient in each equation the *leading coefficient*. For example, in the above system, the leading coefficient of the first equation is the coefficient of $$x_1$$, which is 1; the leading coefficient of the second equation is the coefficient of $$x_2$$, which is 3; and the leading coefficient of the last equation is the coefficient of $$x_3$$, which is 1.

Now eliminate all the coefficients above the leading coefficient in each row. That is, we must eliminate the term $$4x_3$$ above the leading coefficient of the last equation, and the term $$2x_2$$ above the leading coefficient of the second equation. To do this, we multiply the last equation by 4 and subtract it from the first equation, and multiply the second equation by $$2/3$$ and subtract it from the first equation. Also, multiplying both sides of the second equation by $$1/3$$ to simplify, we obtain the following result.

$$\begin{aligned}x_1\phantom{+2x_2+4x_3}-21x_4&=-4\\\phantom{x_1+}x_2\phantom{+2x_3}+\phantom{1}2x_4&=1\\\phantom{x_1+2x_2+}x_3+\phantom{1}5x_4&=1\end{aligned}$$

From this, the general solution of the above system of equations is

$$x_1=-4+21x_4,\quad x_2=1-2x_4,\quad x_3=1-5x_4$$

as can be seen.

</div>

The method of solving a system of equations through the procedure described above is called *Gaussian elimination* or *Gauss-Jordan elimination*.

## Elementary Row Operations and Gaussian Elimination

The system of equations (3) given at the beginning could be simply expressed as $$Ax=b$$ using matrices. Gaussian elimination shows that this matrix $$A$$ and $$b$$ can be suitably transformed so that the system can be written as $$A'x=b'$$, where the matrix $$A'$$ can be chosen to satisfy the two conditions (\*). 

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> For a given matrix $$A$$, an *elementary row operation* refers to the following three operations.

1. exchanging two rows,
2. multiplying a row by a nonzero constant,
3. adding a multiple of one row to another row.

</div>

[Example 2](#ex2), which we examined concretely, concerned manipulating a system of linear equations to satisfy conditions (\*) and then writing it in a specific form; however, it should be noted that the calculations examined before that were also essentially obtained from elementary row operations (the corresponding manipulations of equations).

We also define the following.

<div class="definition" markdown="1">

<ins id="def4">**Definition 4**</ins> Let an $$m\times n$$ matrix $$A$$ be given. If for arbitrary $$1\leq i\leq m$$ the integer $$j_0(i)=\min\{j\leq n\mid a_{ij}\neq 0\}$$ is well-defined, we call $$a_{i,j_0(i)}$$ the *leading coefficient* of the $$i$$-th row. Additionally, if the following two conditions

1. If $$a_{i1}, a_{i2},\ldots, a_{in}=0$$, then for all $$k$$ satisfying $$i < k$$, we have $$a_{k1}, a_{k2},\ldots, a_{kn}=0$$.
2. If $$i < i'$$ and both integers $$j_0(i), j_0(i')$$ are well-defined, then necessarily $$j_0(i) < j_0(i')$$.

are satisfied, the matrix $$A$$ is called a *row echelon matrix* (REF). If additionally

1. $$a_{i, j_0(i)}$$ is always 1, and 
2. for all $$i'\neq i$$, $$M_{i', j_0(i)}=0$$

then $$A$$ is called a *reduced row echelon matrix* (RREF).

</div>

Therefore, summarizing the discussion in the previous section, Gaussian elimination can be said to be the process of making a row echelon matrix, or further a reduced row echelon matrix, from a matrix $$A$$ through elementary row operations. In general, the row echelon form obtained from a given matrix $$A$$ may not be unique, but it is well known that the reduced row echelon form is uniquely determined. We will not prove this uniqueness since we will have no occasion to use it.

Let us return to the system of equations (3). Changing the order of equations, multiplying both sides of an equation by a constant, or adding a multiple of one equation to another are familiar techniques from the first encounter with systems of equations, so they are not strange. However, if we write the same system as $$Ax=b$$ using matrices, it is not clear why the elementary row operations applied to $$A$$ affect $$b$$ in the same way. Now suppose an arbitrary $$m\times n$$ matrix is given, and consider several $$m\times m$$ matrices.

First, $$E_{i,j}$$ is the matrix obtained from the $$m\times m$$ identity matrix $$I$$ by exchanging the $$i$$-th and $$j$$-th rows. For example, $$E_{1,2}$$ is the following matrix

$$E_{1,2}=\begin{pmatrix}0&1&0&\cdots&0\\1&0&0&\cdots&0\\ 0&0&1&\cdots&0\\\vdots&\vdots&\vdots&\ddots&\vdots\\ 0&0&0&\cdots&1\end{pmatrix}$$

Meanwhile, $$E'_{i,r}$$ is the matrix obtained by multiplying the $$i$$-th row of the $$m\times m$$ identity matrix $$I$$ by $$r$$. For example, $$E'_{1,r}$$ is the following matrix

$$E'_{1,r}=\begin{pmatrix}r&0&0&\cdots&0\\0&1&0&\cdots&0\\ 0&0&1&\cdots&0\\\vdots&\vdots&\vdots&\ddots&\vdots\\ 0&0&0&\cdots&1\end{pmatrix}$$

Finally, $$E''_{i,j,r}$$ is the matrix obtained by changing the $$(j,i)$$-entry of the $$m\times m$$ identity matrix $$I$$ to $$r$$. For example, $$E''_{1,2,r}$$ is the following matrix

$$E''_{1,2,r}=\begin{pmatrix}1&0&0&\cdots&0\\r&1&0&\cdots&0\\ 0&0&1&\cdots&0\\\vdots&\vdots&\vdots&\ddots&\vdots\\ 0&0&0&\cdots&1\end{pmatrix}$$

These are collectively called *elementary matrices*. Now, computing $$E_{ij}A$$, $$E'_{i,r}A$$, and $$E''_{i,j,r}A$$ respectively, 

1. $$E_{ij}A$$ is the matrix obtained by exchanging the $$i$$-th and $$j$$-th rows of $$A$$,
2. $$E'_{i,r}A$$ is the matrix obtained by multiplying the $$i$$-th row of $$A$$ by the constant $$r$$,
3. $$E''_{i,j,r}A$$ is the matrix obtained by adding ($$i$$-th row)$$\times r$$ to the $$j$$-th row of $$A$$

can be easily verified. That is, performing an elementary row operation on matrix $$A$$ is the same as multiplying by one of the matrices $$E_{ij}$$, $$E_{i,r}'$$, or $$E_{i,j,r}''$$ defined above; and applying the above manipulation to the system of equations $$Ax=b$$ is the same as multiplying both sides on the left by the corresponding elementary matrix $$E$$ to obtain $$(EA)x=(Eb)$$. 

The elementary matrices $$E$$ are all invertible. This is obvious from the fact that by applying another elementary row operation to a matrix on which an elementary row operation corresponding to an elementary matrix has been performed, we can recover the original matrix.

## Augmented Matrix

Now, when an arbitrary system of linear equations is given, we can manipulate the system to find its solution. As we saw at the beginning of this post, finding the inverse of an arbitrary invertible $$n\times n$$ matrix is nothing more than solving $$n$$ systems of linear equations, so by repeating the method introduced above $$n$$ times for equation (1) needed to find the inverse matrix, we can also obtain the inverse matrix. The augmented matrix introduced from now on is needed only for notational convenience and the resulting computational convenience.

The basic idea is that when performing Gaussian elimination, the columns do not mix with each other; this may be said to be obvious from the definition of matrix multiplication if we think of elementary row operations as multiplication by the elementary matrices examined above. Moreover, when performing Gaussian elimination, the right-hand side containing the constants undergoes the same operations as the left-hand side, so we can add the components of the right-hand side to the matrix and compute everything at once.

<div class="example" markdown="1">

<ins id="ex5">**Example 5**</ins> Using the system of equations given in [Example 2](#ex2)

$$\begin{aligned}x_1+2x_2+4x_3+3x_4&=2\\\phantom{x_1+}3x_2\phantom{+2x_3}+6x_4&=3\\\phantom{x_1+2x_2+}x_3+5x_4&=1\end{aligned}$$

as is. From this system of equations we consider the following *augmented matrix*

$$\begin{pmatrix} 1&2&4&3&2\\ 0&3&0&6&3\\ 0&0&1&5&1\end{pmatrix}$$

The rightmost column of this matrix corresponds to the right-hand side of the system of equations, and the rest correspond to the coefficients of the variables. Now let us apply the operations from [Example 2](#ex2) to this matrix as they are. First, subtracting 4 times the last row from the first row gives the following matrix

$$\begin{pmatrix}1&2&0&-17&-2\\ 0&3&0&6&3\\0&0&1&5&1\end{pmatrix}$$

Now, multiplying the second row by $$2/3$$ and subtracting it from the first row gives the following matrix 

$$\begin{pmatrix}1&0&0&-21&-4\\0&3&0&6&3\\0&0&1&5&1\end{pmatrix}$$

we obtain, and multiplying the second row by $$1/3$$,

$$\begin{pmatrix}1&0&0&-21&-4\\0&1&0&2&1\\0&0&1&5&1\end{pmatrix}$$

is obtained. Restoring the system of equations from this augmented matrix, we see that this is exactly what we obtained in [Example 2](#ex2):

$$\begin{aligned}x_1\phantom{+2x_2+4x_3}-21x_4&=-4\\\phantom{x_1+}x_2\phantom{+2x_3}+\phantom{1}2x_4&=1\\\phantom{x_1+2x_2+}x_3+\phantom{1}5x_4&=1\end{aligned}$$

</div>

The example just examined is essentially no different from the calculation in [Example 2](#ex2) (even in terms of convenience). A meaningful difference is obtained when finding the inverse matrix by using the augmented matrix. For this, consider the case where the matrix $$A$$ defining the system of equations (3) is an invertible $$n\times n$$ matrix. First, the following lemma is obvious.

<div class="proposition" markdown="1">

<ins id="lem6">**Lemma 6**</ins> Any $$n\times n$$ reduced row echelon matrix is either the identity matrix or has a column consisting entirely of zeros. 

</div>

As mentioned earlier, elementary matrices are all invertible, and we can recover the original matrix by multiplying the reduced row echelon form of a given matrix by the inverses of the elementary row operations we performed, in order. That is, if some $$n\times n$$ matrix has a column consisting entirely of zeros, then this matrix is not invertible, and therefore the original matrix cannot be invertible. In other words, the reduced row echelon form of an $$n\times n$$ matrix is the identity matrix.

Now, given an arbitrary invertible $$n\times n$$ matrix, we can solve the $$n$$ systems of equations $$Av_i=e_i$$ at once using the augmented matrix. That is, augmenting $$e_1,\ldots, e_n$$ all at once to form the $$2n\times n$$ matrix $$(A\mid I_n)$$, and then converting this to reduced row echelon form, the rear $$n\times n$$ matrix will become the inverse of the original matrix.

<div class="example" markdown="1">

<ins id="ex7">**Example 7**</ins> Let us find the inverse of the following matrix 

$$A=\begin{pmatrix}1&2&4\\ 0&3&0\\ 0&0&1\end{pmatrix}$$

The augmented matrix is

$$(A\mid I_3)=\begin{pmatrix}1&2&4&1&0&0\\0&3&0&0&1&0\\ 0&0&1&0&0&1\end{pmatrix}$$

and first, subtracting 4 times the last row from the first row gives the following matrix

$$\begin{pmatrix}1&2&0&1&0&-4\\ 0&3&0&0&1&0\\0&0&1&0&0&1\end{pmatrix}$$

Now, multiplying the second row by $$2/3$$ and subtracting it from the first row gives the following matrix 

$$\begin{pmatrix}1&0&0&1&-2/3&-4\\0&3&0&0&1&0\\0&0&1&0&0&1\end{pmatrix}$$

we obtain, and finally multiplying the second row by $$1/3$$,

$$\begin{pmatrix}1&0&0&1&-2/3&-4\\0&1&0&0&1/3&0\\0&0&1&0&0&1\end{pmatrix}$$

is obtained. Thus the inverse of the given matrix $$A$$ is

$$A^{-1}=\begin{pmatrix}1&-2/3&-4\\0&1/3&0\\0&0&1\end{pmatrix}$$

</div>

However, applying Gaussian elimination every time to determine whether a matrix is invertible (especially for small matrices) can sometimes be inefficient. The determinant, which we will examine in the next post, tells us whether a given $$n\times n$$ matrix is invertible or not. However, (especially for complicated matrices) one of the easiest ways to compute the determinant is still Gaussian elimination. ([§Existence and Uniqueness of the Determinant, ⁋Proposition 9](/en/math/linear_algebra/existence_and_uniqueness_of_determinant#prop9))

---

**References**

**[Lee]** 이인석, *선형대수와 군*, 서울대학교 출판문화원, 2005.

---
