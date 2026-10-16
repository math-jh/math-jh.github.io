---
title: "Gaussian Elimination"
description: "We examine the process of finding the inverse of a matrix using Gaussian elimination and prove equivalent conditions for invertible matrices. Based on the relationship between matrices and linear maps, we analyze the equivalence relation determined by rank."
excerpt: "Gaussian elimination and inverse matrices"

categories: [Math / Linear Algebra]
permalink: /en/math/linear_algebra/Gaussian_elimination
sidebar: 
    nav: "linear_algebra-en"


date: 2022-08-19

weight: 12
translated_at: 2026-06-25T12:30:03+00:00
translation_source: kimi-cli
last_polished_at: 2026-10-16T07:15:07+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
In the previous post, we learned that linear maps between vector spaces are essentially identical to matrices. From this perspective, if two $m\times n$ matrices $A,B$ satisfy, for two suitable invertible matrices $P,Q$, the equation

$$B=PAQ\tag{1}$$

then we might want to regard these matrices $A,B$ as essentially the same matrix; however, we saw that for these matrices $L_A, L_B: V\rightarrow W$, if we allow complete freedom in choosing the bases of the two vector spaces $V,W$ on which they act, any two matrices of the same rank must all be treated as the same matrix. For this reason, in [§Fundamental Theorem of Linear Algebra, ⁋Definition 8](/en/math/linear_algebra/ftla#def8){: data-lid="tfpmi" }, we had to define a finer equivalence relation than this. Roughly speaking, if the only information contained in the matrix $A$ in equation (1) above is the rank of $A$, then the remaining information will be contained in the matrices $P,Q$ (that is, in the *linear operators* from $V$ to $V$, or from $W$ to $W$), and if we think of fixing a single basis of $V$ (or $W$) in order to examine them, this equivalence relation is not so unnatural. Accordingly, for the time being, our discussion will proceed with a vector space $V$ and a basis $\mathcal{B}$ fixed. In other words, we will examine $n\times n$ matrices. A powerful tool for this is the determinant, which we will define in the next post.

Meanwhile, we proved using the trace of a matrix that for an arbitrary matrix $A$ to be invertible, this matrix must necessarily be a square matrix ([§Matrices, ⁋Definition 6](/en/math/linear_algebra/matrices#def6){: data-lid="7uqd9" }), and now that we know matrices and linear maps are the same, this result is obvious by [§Isomorphisms, ⁋Proposition 5](/en/math/linear_algebra/isomorphic_vector_spaces#prop5){: data-lid="hn2bn" }. However, we have not yet examined how to compute this inverse matrix. Because this method is simple, we could have examined it right after [§Matrices](/en/math/linear_algebra/matrices){: data-lid="gs9hn" }, but now that we have begun to examine $n\times n$ matrices in earnest, we will briefly introduce this procedure.

First, let us show the following simple lemma.

::: Lemma 1
For a matrix $A\in\Mat_n(\mathbb{K})$, the following three conditions are all equivalent.

1. $A$ is invertible.
2. There exists a suitable $B\in\Mat_n(\mathbb{K})$ such that $AB=I$.
3. There exists a suitable $B\in\Mat_n(\mathbb{K})$ such that $BA=I$.

Moreover, if the second or third condition holds, then $B=A^{-1}$.
:::
::: Proof
That the first condition implies each of the second and third is obvious, so it suffices to show the converse directions.

First, assume that there exists a suitable $B\in\Mat_n(\mathbb{K})$ such that $AB=I$ holds. Then by the fundamental theorem of linear algebra,

$$L_A\circ L_B=\id_{\mathbb{K}^n}$$

holds. Now, from the fact that $\id_{\mathbb{K}^n}$ is bijective, we know that $L_A:\mathbb{K}^n\rightarrow \mathbb{K}^n$ is surjective. ([\[Set Theory\] §Retraction and Section, ⁋Proposition 3](/en/math/set_theory/retraction_and_section#prop3){: data-lid="c8um4" }) Therefore, from the following equation ([§Isomorphisms, ⁋Theorem 7](/en/math/linear_algebra/isomorphic_vector_spaces#thm7){: data-lid="f57r3" })

$$\rank L_A+\nullity L_A=\dim \mathbb{K}^n=n$$

we know that $\nullity L_A=0$. That is, $L_A$ is also injective, and thus $L_A$ is bijective and the matrix $A$ is invertible. Now, multiplying both sides of the equation $AB=I$ on the left by $A^{-1}$, we obtain $B=A^{-1}$.

Similarly, one can prove that the third condition implies the first condition.
:::

Of course, once again considering that matrices and linear maps are the same, this is obvious because the inverse of a function satisfies the same property.

Now, let an arbitrary $n\times n$ invertible matrix $A$ be given. Thinking of $A$ as a linear map from $\mathbb{K}^n$ to $\mathbb{K}^n$, $A$ is completely determined by where it sends the basis $e_1,\ldots, e_n$ of $\mathbb{K}^n$. Therefore, to compute the matrix $A^{-1}$, it suffices to know where $A^{-1}$ sends the basis elements $e_i$. If we denote this value by the vector $v_i$, then the matrix $A^{-1}$ will be given by $(v_1\mid v_2\mid\cdots\mid v_n)$, where each $v_i$ is defined by the following equation:

$$v_i=A^{-1}e_i\iff Av_i=e_i\tag{2}$$

## Gauss-Jordan Elimination

Now, suppose that the following system of linear equations

$$\begin{aligned}a_{11}x_{1}+a_{12}x_2+\cdots+a_{1n}x_n&=b_1\\a_{21}x_1+a_{22}x_2+\cdots+a_{2n}x_n&=b_2\\\hspace{10pt}\vdots&\\a_{m1}x_1+a_{m2}x_2+\cdots+a_{mn}x_n&=b_m\end{aligned}\tag{3}$$

is given. Then by [§Matrices, ⁋Definition 1](/en/math/linear_algebra/matrices#def1){: data-lid="tgs86" }, in terms of the following matrices

$$A=\begin{pmatrix}a_{11}&a_{12}&\cdots&a_{1n}\\a_{21}&a_{22}&\cdots&a_{2n}\\\vdots&\vdots&\ddots&\vdots\\a_{m1}&a_{m2}&\cdots&a_{mn}\end{pmatrix},\quad x=\begin{pmatrix}x_1\\x_2\\\vdots\\x_n\end{pmatrix},\quad b=\begin{pmatrix}b_1\\b_2\\\vdots\\b_m\end{pmatrix}$$

the system above can be written as $Ax=b$. If $m=n$ and the inverse of the matrix $A$ exists, then the solution to this system of equations is uniquely determined through the following equation

$$x=A^{-1}b\iff Ax=b$$

and this is precisely the equation we need to find the inverse matrix. If $m\neq n$ or the inverse of $A$ does not exist, a solution to the system of linear equations above may not exist, or there may be infinitely many. We examine *Gaussian elimination*, which can be usefully applied even in this case.

Suppose that among the coefficients of equation (3), the condition $a_{ji}=0$ for all $j$ holds for some $1\leq i\leq n$. In this case, if

$$x_1=c_1,\quad x_2=c_2,\quad \ldots,\quad x_i=c_i,\quad\ldots,\quad x_n=c_n$$

is a solution to equation (3), then the following tuple obtained by changing the value of $x_i$ to an arbitrary $d_i$,

$$x_1=c_1,\quad x_2=c_2,\quad\ldots,\quad x_i=d_i,\quad\ldots,\quad x_n=c_n$$

is also a solution to equation (3). Therefore, if all $a_{ij}$ are $0$, then if $b$ is the zero vector, equation (3) has every tuple in $\mathbb{K}^n$ as a solution, and otherwise no solution exists. To avoid such trivial cases, we assume that at least one $a_{ij}$ is not 0.

Now, define the integer $k$ as the smallest among the integers for which $a_{jk}\neq 0$ for some $1\leq j\leq m$, and for this fixed $k$, among those satisfying $a_{jk}\neq 0$, choose the smallest integer $j$. Now, if we move the $j$-th equation

$$a_{j1}x_1+a_{j2}x_2+\cdots+a_{jk}x_k+\cdots+a_{jn}x_n=b_j$$

to the very top of the system and write

$$\begin{aligned}a_{j1}x_{1}+a_{j2}x_2+\cdots+a_{jn}x_n&=b_j\\a_{11}x_1+a_{12}x_2+\cdots+a_{1n}x_n&=b_1\\\hspace{10pt}\vdots&\\a_{m1}x_1+a_{m2}x_2+\cdots+a_{mn}x_n&=b_m\end{aligned}$$

then by the definition of $a_{jk}$, the coefficients $a_{j1},a_{j2},\ldots, a_{j,(k-1)}$ and the coefficients below them must all be $0$. Now, for each equation

$$a_{i1}x_1+a_{i2}x_2+\cdots+a_{in}x_n=b_i$$

multiplying the first equation by $-a_{ik}/a_{jk}$ and adding it yields

$$\left(a_{i1}-\frac{a_{ik}}{a_{jk}}a_{j1}\right)x_1+\left(a_{i2}-\frac{a_{ik}}{a_{jk}}a_{j2}\right)x_2+\cdots+\left(a_{ik}-\frac{a_{ik}}{a_{jk}}a_{jk}\right)x_k+\cdots+\left(a_{in}-\frac{a_{ik}}{a_{jk}}a_{jn}\right)x_n=b_i-\frac{a_{ik}}{a_{jk}}b_j$$

In the equation above, the coefficients of $x_1,\ldots, x_{k-1}$ were originally all 0, and through the operation just performed, the coefficient of $x_k$ also becomes 0. That is, after going through this process, the coefficients of $x_1,\ldots, x_{k-1}$ are all 0, and among the coefficients of $x_k$, a nonzero one exists only in the first row.

Now, we repeat this process for the $m-1$ equations from the second row to the last row, and again repeat this process for the $m-2$ equations from the third row to the last row. Continuing this until reaching the last row, equation (3) above finally satisfies the following two conditions (\*):

1. If there is an equation in which all coefficients are 0, this equation is located at the very bottom of the system of equations.
2. For each equation in which not all coefficients are 0, the first nonzero coefficient appearing in this equation lies to the right of the coefficient satisfying this property in the equation above it.

::: Example 2
The following system of equations satisfies the above two conditions.

$$\begin{aligned}x_1+2x_2+4x_3+3x_4&=2\\\phantom{x_1+}3x_2\phantom{+2x_3}+6x_4&=3\\\phantom{x_1+2x_2+}x_3+5x_4&=1\end{aligned}$$

With a little additional manipulation, we can immediately find the solution to the system of equations from this system. Let us call the first nonzero coefficient in each equation the *leading coefficient*. Taking the above system as an example, the leading coefficient of the first equation is 1, the coefficient of $x_1$; the leading coefficient of the second equation is 3, the coefficient of $x_2$; and the leading coefficient of the last equation is 1, the coefficient of $x_3$.

Now, for each row, we eliminate all coefficients above the leading coefficient. That is, we must eliminate the term $4x_3$ above the leading coefficient of the last equation, and the term $2x_2$ above the leading coefficient of the second equation. To do this, we multiply the last equation by 4 and subtract it from the first equation, and multiply the second equation by $2/3$ and subtract it from the first equation. Also, to make the equations cleaner, if we multiply both sides of the second equation by $1/3$, the result is as follows.

$$\begin{aligned}x_1\phantom{+2x_2+4x_3}-21x_4&=-4\\\phantom{x_1+}x_2\phantom{+2x_3}+\phantom{1}2x_4&=1\\\phantom{x_1+2x_2+}x_3+\phantom{1}5x_4&=1\end{aligned}$$

From this, we can see that the general solution to the above system of equations is

$$x_1=-4+21x_4,\quad x_2=1-2x_4,\quad x_3=1-5x_4$$
:::

The method of solving a system of equations through the process described so far is called *Gaussian elimination* or *Gauss-Jordan elimination*.

## Elementary Row Operations and Gaussian Elimination

The system of equations (3) given initially could be expressed simply as $Ax=b$ using matrices. Gaussian elimination shows that by appropriately changing the matrices $A$ and $b$, we can write this equation as $A'x=b'$, where the matrix $A'$ can be chosen to satisfy the two conditions (\*).

::: Definition 3
For a given matrix $A$, an *elementary row operation (ERO)* refers to the following three operations:

1. Interchanging two entire rows vertically,
2. Multiplying a row by a nonzero constant,
3. Adding a multiple of one row to another row.
:::

Although [Example 2](#ex2){: data-lid="jh5b2" }, which we examined in detail, was about appropriately manipulating a system of linear equations so that it satisfies condition (\*) and then writing it in a specific way, it is worth noting that the calculations examined before that are also essentially obtained from (the manipulations of equations corresponding to) elementary row operations.

Also, we define the following.

::: Definition 4
Let an $m\times n$ matrix $A$ be given. For any $1\leq i\leq m$, if the integer $j_0(i)=\min\{j\leq n\mid a_{ij}\neq 0\}$ is well-defined, we call $a_{i,j_0(i)}$ the *leading coefficient* of the $i$-th row. Additionally, if the following two conditions

1. If $a_{i1}, a_{i2},\ldots, a_{in}=0$, then for all $k$ satisfying $i < k$, $a_{k1}, a_{k2},\ldots, a_{kn}=0$.
2. If $i < i'$ and both integers $j_0(i), j_0(i')$ are well-defined, then necessarily $j_0(i) < j_0(i')$.

are satisfied, we call the matrix $A$ a *row echelon matrix*. If additionally

1. $a_{i, j_0(i)}$ is always 1, and
2. for all $i'\neq i$, $a_{i', j_0(i)}=0$,

then we call $A$ a *reduced row echelon matrix*.
:::

Therefore, synthesizing the discussion from the previous section, Gaussian elimination can be described as the process of producing a row echelon matrix, or even further a reduced row echelon matrix, from a matrix $A$ through elementary row operations. In general, there can be several row echelon forms obtained from a given matrix $A$, but it is a well-known fact that the reduced row echelon matrix is necessarily uniquely determined. Since we will have no occasion to use this uniqueness, we do not prove it.

Let us return again to the system of equations (3). Changing the order of the equations, multiplying both sides of each equation by a constant, and adding a multiple of each equation to another equation are familiar solution methods from when we first encountered systems of equations, so they are not strange. However, if we write the same equations as $Ax=b$ using matrices, it is not clear why the elementary row operations applied to $A$ affect $b$ in the same way. Now suppose an arbitrary $m\times n$ matrix is given, and let us consider several $m\times m$ matrices.

First, $E_{i,j}$ is the matrix obtained from the $m\times m$ identity matrix $I$ by swapping the $i$-th and $j$-th rows. For example, $E_{1,2}$ is the following matrix:

$$E_{1,2}=\begin{pmatrix}0&1&0&\cdots&0\\1&0&0&\cdots&0\\ 0&0&1&\cdots&0\\\vdots&\vdots&\vdots&\ddots&\vdots\\ 0&0&0&\cdots&1\end{pmatrix}$$

Meanwhile, $E'_{i,r}$ is the matrix obtained from the $m\times m$ identity matrix $I$ by multiplying the $i$-th row by a non-$0$ constant $r$. For example, $E'_{1,r}$ is the following matrix:

$$E'_{1,r}=\begin{pmatrix}r&0&0&\cdots&0\\0&1&0&\cdots&0\\ 0&0&1&\cdots&0\\\vdots&\vdots&\vdots&\ddots&\vdots\\ 0&0&0&\cdots&1\end{pmatrix}$$

Finally, $E''_{i,j,r}$ is the matrix obtained from the $m\times m$ identity matrix $I$ by changing the entry in row $j$ and column $i$ to $r$. For example, $E''_{1,2,r}$ is the following matrix:

$$E''_{1,2,r}=\begin{pmatrix}1&0&0&\cdots&0\\r&1&0&\cdots&0\\ 0&0&1&\cdots&0\\\vdots&\vdots&\vdots&\ddots&\vdots\\ 0&0&0&\cdots&1\end{pmatrix}$$

These are also collectively called *elementary matrices*. Now, if we compute $E_{ij}A$, $E'_{i,r}A$, and $E''_{i,j,r}A$ respectively:

1. $E_{ij}A$ is the matrix obtained from $A$ by swapping the $i$-th row and the $j$-th row,
2. $E'_{i,r}A$ is the matrix obtained from $A$ by multiplying the $i$-th row by the constant $r$, and
3. $E''_{i,j,r}A$ is the matrix obtained from $A$ by adding to the $j$-th row the ($i$-th row)$\times r$,

as one can easily verify. That is, performing an elementary row operation on a matrix $A$ is the same as multiplying by the matrix $E_{ij}$, $E_{i,r}'$, or $E_{i,j,r}''$ defined above, and applying the above manipulations to the system of equations $Ax=b$ is the same as multiplying both sides on the left by the corresponding elementary matrix $E$ to obtain $(EA)x=(Eb)$.

All elementary matrices $E$ are invertible matrices. This is obvious from the fact that, to a matrix on which the elementary row operation corresponding to an elementary matrix has been performed, one can apply an elementary row operation again to obtain the original matrix.

## Augmented Matrix

Now, when an arbitrary system of linear equations is given, we can manipulate the system to find its solution. As we saw at the beginning of this post, finding the inverse of an arbitrary $n\times n$ invertible matrix is nothing more than solving $n$ systems of linear equations, so if we repeat equation (2), which is needed to find the inverse matrix, $n$ times according to the method introduced above, we can also find the inverse matrix. The augmented matrix introduced from now on is needed only for notational convenience and the computational convenience that follows from it.

The basic idea is that when performing Gaussian elimination, the columns do not mix with each other, which can also be said to be obvious from the definition of matrix multiplication if we think of elementary row operations as multiplication by the elementary matrices examined above. Moreover, when performing Gaussian elimination, since the right-hand side where the constants reside undergoes the same operations as the left-hand side, we can append the entries of the right-hand side to the matrix and compute everything at once.

::: Example 5
Let us use the system of equations given in [Example 2](#ex2){: data-lid="cgq0t" } as it is:

$$\begin{aligned}x_1+2x_2+4x_3+3x_4&=2\\\phantom{x_1+}3x_2\phantom{+2x_3}+6x_4&=3\\\phantom{x_1+2x_2+}x_3+5x_4&=1\end{aligned}$$

From this system of equations, we consider the following *augmented matrix*:

$$\begin{pmatrix} 1&2&4&3&2\\ 0&3&0&6&3\\ 0&0&1&5&1\end{pmatrix}$$

The rightmost column of this matrix corresponds to the right-hand side of the system of equations, and the rest corresponds to the coefficients in front of the variables of the system of equations. Now, let us apply the exact same operations as in [Example 2](#ex2){: data-lid="ookai" } to this matrix. First, subtracting 4 times the last row from the first row gives the following matrix:

$$\begin{pmatrix}1&2&0&-17&-2\\ 0&3&0&6&3\\0&0&1&5&1\end{pmatrix}$$

Now, subtracting $2/3$ times the second row from the first row gives the following matrix:

$$\begin{pmatrix}1&0&0&-21&-4\\0&3&0&6&3\\0&0&1&5&1\end{pmatrix}$$

and multiplying the second row by $1/3$ gives:

$$\begin{pmatrix}1&0&0&-21&-4\\0&1&0&2&1\\0&0&1&5&1\end{pmatrix}$$

Restoring the system of equations from this augmented matrix, we see that this is exactly what we obtained in [Example 2](#ex2){: data-lid="31ihf" }:

$$\begin{aligned}x_1\phantom{+2x_2+4x_3}-21x_4&=-4\\\phantom{x_1+}x_2\phantom{+2x_3}+\phantom{1}2x_4&=1\\\phantom{x_1+2x_2+}x_3+\phantom{1}5x_4&=1\end{aligned}$$
:::

The example just examined is essentially no different from the calculation in [Example 2](#ex2){: data-lid="joj2h" } (even in terms of convenience). A meaningful difference is obtained when finding the inverse matrix by using an augmented matrix. For this, let us consider the case where the matrix $A$ defining the system of equations (3) is an $n\times n$ invertible matrix. First, the following lemma is obvious.

::: Lemma 6
Any $n\times n$ reduced row echelon matrix is either the identity matrix or has a row consisting only of $0$s.
:::

As mentioned earlier, all elementary matrices are invertible, and we can restore the original matrix by multiplying the reduced row echelon form of the given matrix by the inverses of the elementary row operations we performed, in order. That is, if some $n\times n$ matrix has a row consisting only of $0$s, then this matrix is not invertible, and therefore the original matrix cannot be invertible. In other words, the reduced row echelon form of an $n\times n$ invertible matrix is the identity matrix.

Now, when an arbitrary $n\times n$ invertible matrix is given, we can solve the $n$ systems of equations $Av_i=e_i$ all at once using an augmented matrix. That is, if we append $e_1,\ldots, e_n$ all at once to form the $n\times 2n$ matrix $(A\mid I_n)$ and convert this to reduced row echelon form, the rear $n\times n$ matrix will be the inverse of the original matrix.

::: Example 7
Let us find the inverse of the following matrix:

$$A=\begin{pmatrix}1&2&4\\ 0&3&0\\ 0&0&1\end{pmatrix}$$

The augmented matrix is

$$(A\mid I_3)=\begin{pmatrix}1&2&4&1&0&0\\0&3&0&0&1&0\\ 0&0&1&0&0&1\end{pmatrix}$$

and first, subtracting 4 times the last row from the first row gives the following matrix:

$$\begin{pmatrix}1&2&0&1&0&-4\\ 0&3&0&0&1&0\\0&0&1&0&0&1\end{pmatrix}$$

Now, subtracting $2/3$ times the second row from the first row gives the following matrix:

$$\begin{pmatrix}1&0&0&1&-2/3&-4\\0&3&0&0&1&0\\0&0&1&0&0&1\end{pmatrix}$$

and finally, multiplying the second row by $1/3$ gives:

$$\begin{pmatrix}1&0&0&1&-2/3&-4\\0&1&0&0&1/3&0\\0&0&1&0&0&1\end{pmatrix}$$

That is, the inverse of the given matrix $A$ is

$$A^{-1}=\begin{pmatrix}1&-2/3&-4\\0&1/3&0\\0&0&1\end{pmatrix}$$
:::

## LU Decomposition

Earlier, we examined Gaussian elimination from the perspective of elementary row operations. Now, if we organize the same process in terms of matrix multiplication, we can see that a matrix for which elimination can be carried out without row exchanges can be decomposed into the product of two triangular matrices.

::: Definition 8
For a square matrix $A$, when it is decomposed as $A=LU$, if $L$ is a lower triangular matrix with all diagonal entries equal to $1$ and $U$ is an upper triangular matrix, we call this an *LU decomposition* of $A$.
:::

Consider a matrix for which Gaussian elimination can be performed without row exchanges and without multiplying an entire row by a constant. That is, suppose that using only the elementary row operation of "adding a multiple of an upper row to a lower row," we can obtain an upper triangular matrix $U$. If the elementary matrices used in this process are $E_1,E_2,\ldots,E_k$ in order, then

$$E_k\cdots E_2E_1A=U$$

holds. Here, each $E_i$ is an elementary matrix in the form of a lower triangular matrix with diagonal entries equal to $1$, so its inverse $E_i^{-1}$ is also a lower triangular matrix with diagonal entries equal to $1$, and their product also maintains the same form. Therefore, we can write

$$A=(E_1^{-1}\cdots E_k^{-1})U$$

and setting $L=E_1^{-1}\cdots E_k^{-1}$ gives $A=LU$.

Of course, to perform Gaussian elimination in this way, the entry to be used as the pivot at each step must not be $0$. That is, an LU decomposition exists only when this condition is satisfied. The following summarizes this result.

::: Theorem 9
For a square matrix $A$, the following hold.

1. If Gaussian elimination can be performed without row exchanges and without multiplying a row by a constant, then $A$ has an LU decomposition.
2. If $A$ is invertible and both $A=LU$ and $A=L'U'$ are LU decompositions in which the diagonal entries of $L,L'$ are $1$, then $L=L'$ and $U=U'$.
:::
::: Proof
Existence is obvious from the above discussion. Let us show uniqueness. Suppose $LU=L'U'$. Since $L$ and $L'$ are lower triangular matrices with diagonal entries equal to $1$, they are invertible, and by the assumption that $A$ is invertible, $U=L^{-1}A$ is also invertible. Therefore, we obtain

$$(L')^{-1}L=U'(U)^{-1}$$

The left-hand side is the product of two lower triangular matrices and is therefore a lower triangular matrix, while the right-hand side is the product of two upper triangular matrices and is therefore an upper triangular matrix. Thus, both sides are diagonal matrices. Moreover, since the diagonal entries of $L$ and $(L')^{-1}$ are all $1$, the diagonal entries of the left-hand side are also all $1$. That is, both sides are the identity matrix, and we obtain $L=L'$, $U=U'$.
:::

The usefulness of LU decomposition is prominent when solving a system of linear equations $Ax=b$. Once decomposed as $A=LU$, the equation $Ax=b$ can be written as $L(Ux)=b$, and we solve this by separating it into

$$Ly=b,\qquad Ux=y$$

Since each equation is a system of linear equations for a lower triangular or upper triangular matrix, the solution can be found simply by substituting in turn.

::: Example 10
Consider the matrix

$$A=\begin{pmatrix}2&1&1\\4&3&3\\8&7&9\end{pmatrix}$$

Multiplying the first row by $-2$ and adding it to the second row, and multiplying it by $-4$ and adding it to the third row, we obtain

$$U_1=\begin{pmatrix}2&1&1\\0&1&1\\0&3&5\end{pmatrix}$$

Next, multiplying the second row by $-3$ and adding it to the third row gives

$$U=\begin{pmatrix}2&1&1\\0&1&1\\0&0&2\end{pmatrix}$$

Multiplying the inverses of the elementary matrices used here yields

$$L=\begin{pmatrix}1&0&0\\2&1&0\\4&3&1\end{pmatrix}$$

from which we can verify that $A=LU$.
:::

However, (mainly for small matrices) applying Gaussian elimination every time to determine whether a matrix is invertible can sometimes be inefficient. The determinant, which we will examine in the next post, provides a way to determine whether a given $n\times n$ matrix is invertible or not. However, (especially for complicated matrices) one of the easiest ways to compute the determinant is still Gaussian elimination. ([§Existence and Uniqueness of the Determinant, ⁋Proposition 8](/en/math/linear_algebra/existence_and_uniqueness_of_determinant#prop8){: data-lid="9pxst" })

---

**References**

**[Goc]** M.S. Gockenbach, *Finite-dimensional linear algebra*, Discrete Mathematics and its applications, Taylor&Francis, 2011.

---
