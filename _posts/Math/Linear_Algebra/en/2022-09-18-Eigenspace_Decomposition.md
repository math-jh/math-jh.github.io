---
title: "Eigenspace Decomposition"
description: "We discuss the conditions for decomposing a vector space into a direct sum of eigenspaces through definitions and propositions. The role of a basis and necessary and sufficient conditions for a direct sum of subspaces are explained."
excerpt: "Eigenspace decomposition of a vector space"

categories: [Math / Linear Algebra]
permalink: /en/math/linear_algebra/eigenspace_decomposition
drift_needed: true
sidebar: 
    nav: "linear_algebra-en"


date: 2022-09-18

weight: 16
translated_at: 2026-06-26T01:31:46+00:00
translation_source: kimi-cli
---
## Direct Sums of Subspaces

Consider an $$n\times n$$ matrix $$A$$ and one of its eigenvalues $$\lambda$$. By definition, any vector $$v$$ in the eigenspace $$E_\lambda$$ corresponding to $$\lambda$$ must satisfy the equation

$$Av=\lambda v$$

Therefore, when restricted to $$E_\lambda$$, the matrix $$A$$ becomes the very simple object $$v\mapsto \lambda v$$.

More generally, let us think of $$A$$ as a linear map from $$\mathbb{K}^n$$ to $$\mathbb{K}^n$$, and assume that the domain $$\mathbb{K}^n$$ can be covered by the eigenspaces $$E_\lambda$$. That is, suppose

$$\mathbb{K}^n=\span\left(\bigcup_{\lambda\in\sigma(A)}E_\lambda\right)$$

Then for any $$v\in\mathbb{K}^n$$, there exist vectors $$v_\lambda\in E_\lambda$$ such that we can write

$$v=\sum_{\lambda\in\sigma(A)}v_\lambda$$

and therefore

$$Av=A\left(\sum_{\lambda\in\sigma(A)}v_\lambda\right)=\sum_{\lambda\in\sigma(A)}Av_\lambda$$

By the argument above, since $$Av_\lambda=\lambda v_\lambda$$, we obtain the formula

$$Av=\sum_{\lambda\in\sigma(A)}\lambda v_\lambda$$

Of course, for this calculation to make sense, the way of expressing $$v$$ as a sum of the $$v_\lambda$$ must be unique. We define this as follows.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> A $$\mathbb{K}$$-vector space $$V$$ is called the *direct sum* of its subspaces $$(W_i)_{i\in I}$$ if, for any given $$v\in V$$, there exist unique $$(v_i)_{i\in I}$$ such that

$$v=\sum_{i\in I} v_i$$

holds.[^1] We write this as $$V=\bigoplus_{i\in I}W_i$$.

</div>

The easiest nontrivial case is when $$I$$ is a two-element set.

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> For two subspaces $$W_1,W_2$$ of a $$\mathbb{K}$$-vector space $$V$$, the condition $$V=W_1\oplus W_2$$ is equivalent to $$V=W_1+W_2$$ and $$W_1\cap W_2=\{0\}$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, assume $$V=W_1\oplus W_2$$. By definition, $$W_1+W_2\subseteq V$$ is obvious. Conversely, for any $$v\in V$$, there exist $$w_i\in W_i$$ such that $$v=w_1+w_2$$, so $$V\subseteq W_1+W_2$$ also holds. From this we know that $$V=W_1+W_2$$. On the other hand, if $$W_1\cap W_2\neq \{0\}$$, then for a nonzero $$w\in W_1\cap W_2$$,

$$w=0+w=w+0$$

which contradicts the uniqueness in [Definition 1](#def1).

Conversely, suppose $$V=W_1+W_2$$ and $$W_1\cap W_2=\{0\}$$. For any $$v\in V$$, since $$V=W_1+W_2$$, there must exist $$w_1\in W_i$$ such that $$v=w_1+w_2$$. Moreover, this expression is unique. If

$$v=w_1+w_2=w_1'+w_2'$$

then

$$w_1-w_1'=w_2-w_2'$$

The left side is an element of $$W_1$$ and the right side is an element of $$W_2$$, so the condition $$W_1\cap W_2=\{0\}$$ implies $$w_1-w_1'=w_2-w_2'=0$$.

</details>

One direction of the above proposition holds even when $$I$$ has three or more elements. That is, if $$V=\bigoplus_{i\in I}W_i$$, then $$V=\sum_{i\in I}W_i$$ and whenever $$i\neq j$$, we have $$W_i\cap W_j=\{0\}$$, and the proof is the same as above. However, the converse does not generally hold.

For example, let $$V=\mathbb{R}^2$$ and take the two standard basis vectors $$e_1,e_2$$ of $$V$$. If we set $$W_1=\mathbb{R}e_1$$, $$W_2=\mathbb{R}e_2$$, and $$W_3=\mathbb{R}(e_1+e_2)$$, then $$V=W_1+W_2+W_3$$ and whenever $$i\neq j$$ we have $$W_i\cap W_j=\{0\}$$, but $$V\neq W_1\oplus W_2\oplus W_3$$.

This is because the way to represent $$e_1+e_2\in V$$ is not unique, as shown by

$$e_1+e_2=e_1+e_2+0=0+0+(e_1+e_2)$$

As another example, let us choose a basis $$\mathcal{B}=\{x_1,\ldots, x_n\}$$ of $$V$$. If we set $$W_i=\mathbb{K}x_i$$, then the condition that $$\mathcal{B}$$ is a basis exactly coincides with the condition that $$V$$ is the direct sum of the $$W_i$$. More generally, the following holds.

<div class="proposition" markdown="1">

<ins id="prop3">**Proposition 3**</ins> For any $$\mathbb{K}$$-vector space $$V$$ and subspaces $$(W_i)_{i\in I}$$, the condition $$V=\bigoplus_{i\in I} W_i$$ is equivalent to the bases $$\mathcal{B}_i$$ of $$W_i$$ satisfying $$\mathcal{B}_i\cap\mathcal{B}_j=\emptyset$$ whenever $$i\neq j$$, and $$\bigcup_{i\in I}\mathcal{B}_i$$ becoming a basis of $$V$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, assume $$V=\bigoplus W_i$$ and choose bases $$\mathcal{B}_i$$ of the $$W_i$$. If $$\mathcal{B}_i\cap\mathcal{B}_j\neq\emptyset$$, then $$W_i\cap W_j\neq\emptyset$$, which contradicts the discussion after [Proposition 2](#prop2), so we must have $$\mathcal{B}_i\cap\mathcal{B}_j=\emptyset$$. For any $$v\in V$$, from $$V=\bigoplus W_i$$ there exist unique $$w_i$$ satisfying the equation

$$v=\sum_{i\in I} w_i$$

Also, in each $$W_i$$ the $$w_i$$ can be uniquely expressed as linear combinations of elements of $$\mathcal{B}_i$$. From this we can see that $$\bigcup\mathcal{B}_i$$ becomes a basis of $$V$$.

Reversing this argument shows the converse direction as well.

</details>

Thus we can see that $$\dim V=\sum_{i\in I}\dim W_i$$.

## Diagonalization

Now we examine how to decompose $$\mathbb{K}^n$$ into eigenspaces. From the preceding [Proposition 3](#prop3) we know that decomposing the vector space $$\mathbb{K}^n$$ into the eigenspaces $$E_\lambda$$ is the same as collecting bases of the $$E_\lambda$$ to represent a basis of $$\mathbb{K}^n$$. Also, if a nonzero vector $$x_1$$ is an eigenvector corresponding to an eigenvalue $$\lambda_1$$, then for another eigenvalue $$\lambda_2$$,

$$Ax_1=\lambda_1x_1\neq\lambda_2 x_1$$

so we know that $$x_1\not\in E_{\lambda_2}$$. Therefore, no matter how we choose bases of the $$E_\lambda$$, the bases of $$E_{\lambda_1}$$ and $$E_{\lambda_2}$$ never overlap for distinct $$\lambda_1,\lambda_2$$. Moreover, the following holds.

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4**</ins> For any matrix $$A$$, suppose $$x_1,\ldots, x_m$$ are eigenvectors corresponding to distinct eigenvalues $$\lambda_1,\ldots,\lambda_m$$ respectively. Then the set $$\{x_1,\ldots,x_m\}$$ is linearly independent.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Suppose for contradiction that the set $$\{x_1,x_2,\ldots, x_m\}$$ is linearly dependent. That is, there exist scalars $$\alpha_i$$, not all zero, satisfying the equation

$$\alpha_1x_1+\alpha_2x_2+\cdots+\alpha_mx_m=0\tag{1}$$

Now among the $$(\alpha_i)_{1\leq i\leq m}$$ satisfying this, choose a collection with the smallest $$\supp(\alpha_i)$$ and call it $$(\beta_i)_{1\leq i\leq m}$$. That is, if the number of $$i$$ satisfying $$\beta_i\neq0$$ is $$k$$, then no $$(\alpha_i)_{1\leq i\leq m}$$ with fewer than $$k$$ nonzero $$\alpha_i$$ satisfies equation (1) above.

Now since at least two of the $$\beta_i$$ are nonzero, we may assume without loss of generality that $$\beta_m\neq 0$$. Then

$$x_m=\sum_{i=1}^{m-1}\left(-\frac{\beta_i}{\beta_m}\right)x_i$$

For convenience, let us write this as $$x_m=\sum_{i=1}^{m-1}\beta'_ix_i$$. Multiplying both sides by $$A$$,

$$Ax_m=\sum_{i=1}^{m-1}\beta'_i(Ax_i)$$

and since the $$x_m$$ are eigenvectors,

$$\lambda_mx_m=\sum_{i=1}^{m-1}\beta'_i\lambda_i x_i$$

But multiplying both sides of $$x_m=\sum_{i=1}^{m-1}\beta'_ix_i$$ by $$\lambda_m$$ gives

$$\lambda_mx_m=\sum_{i=1}^{m-1}\beta_i'\lambda_mx_i$$

so combining this with the equation obtained above,

$$0=\sum_{i=1}^{m-1}\beta_i'(\lambda_i-\lambda_m)x_i$$

and since $$\beta_i'=-(\beta_i/\beta_m)$$, multiplying both sides by $$\beta_m$$ and rearranging gives

$$0=\sum_{i=1}^{m-1}\beta_i(\lambda_i-\lambda_m)x_i$$

If we define $$(\beta''_i)_{1\leq i\leq n}$$ by the formula

$$\beta_i''=\begin{cases}\beta_i(\lambda_i-\lambda_m)&1\leq i\leq m-1\\0&i=m\end{cases}$$

then the above equation becomes

$$\beta_1''x_1+\beta_2''x_2+\cdots+\beta_m''x_m=0$$

By assumption, $$\lambda_i-\lambda_m\neq 0$$, so for $$1\leq i\leq m-1$$, the condition $$\beta_i''=0$$ is equivalent to $$\beta_i=0$$. Therefore, the number of $$1\leq i\leq m-1$$ satisfying $$\beta_i''\neq 0$$ is $$k-1$$, and since $$\beta_m''=0$$, the size of $$\supp(\beta_i'')_{1\leq i\leq m}$$ is $$k-1$$. This contradicts the minimality of $$(\beta_i)_{1\leq i\leq m}$$, so the set $$\{x_1,x_2,\ldots, x_m\}$$ is linearly independent.

</details>

From this, for any matrix $$A$$ with eigenvalues $$\lambda\in\sigma(A)$$ and corresponding eigenspaces $$E_\lambda$$ with bases $$\mathcal{B}_\lambda$$, we know that $$\mathcal{B}=\bigcup_{\lambda\in\sigma(A)}\mathcal{B}_\lambda$$ becomes a linearly independent subset of $$\mathbb{K}^n$$. However, there is no reason for $$\mathcal{B}$$ to be a basis of $$\mathbb{K}^n$$ in general. For example, looking at [§Characteristic Polynomial, ⁋Example 7](/en/math/linear_algebra/characteristic_polynomial#ex7), when $$\mathbb{K}=\mathbb{R}$$ we have $$\sigma(J)=\emptyset$$, so $$\mathcal{B}=\emptyset$$. Moreover, even if we assume that the characteristic polynomial of $$A$$ has exactly $$n$$ roots, a similar problem can arise; for example, for the matrix

$$A=\begin{pmatrix}1&1&1\\0&1&1\\0&0&1\end{pmatrix}$$

the characteristic polynomial is $$(\mathbf{x}-1)^3=0$$, but we can see that the only eigenvector corresponding to the eigenvalue $$1$$ is $$(1,0,0)$$. In the language introduced in the previous post, the algebraic multiplicity of the eigenvalue $$1$$ is $$3$$, and the geometric multiplicity is $$1$$.

The following proposition shows that the geometric multiplicity of an eigenvalue of a matrix can never exceed its algebraic multiplicity.

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> For an eigenvalue $$\lambda\in\mathbb{K}$$ of an $$n\times n$$ matrix $$A$$, the geometric multiplicity of $$\lambda$$ never exceeds the algebraic multiplicity of $$\lambda$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Let the geometric multiplicity of $$\lambda$$ be $$k$$, and consider $$k$$ linearly independent vectors $$x_1,\ldots, x_k$$ spanning $$E_\lambda(A)$$. To these we can add $$(n-k)$$ vectors $$x_{k+1},\ldots, x_n$$ to form a new basis $$\{x_1,\ldots, x_n\}$$ of $$\mathbb{K}^n$$. Now if we define the matrix $$X$$ by

$$X=(x_1\vert x_2\vert \cdots\vert x_n)$$

then since the columns of $$X$$ are linearly independent, $$X^{-1}$$ exists. Let the rows of $$X^{-1}$$ be $$y_i$$. From the equation $$X^{-1}X=XX^{-1}=I$$,

$$y_i\cdot x_j=\begin{cases}1&i=j\\ 0&i\neq j\end{cases}$$

holds. Therefore, if we set $$A'=X^{-1}AX$$,

$$\begin{aligned}A'&=X^{-1}(AX)=\begin{pmatrix}y_1\\ y_2\\ \vdots\\ y_n\end{pmatrix}(Ax_1\vert Ax_2\vert \cdots\vert Ax_n)\\
&=\begin{pmatrix}y_1\cdot Ax_1&y_1\cdot Ax_2&\cdots& y_1\cdot Ax_k&\cdots&y_1\cdot Ax_n\\ y_2\cdot Ax_1&y_2\cdot Ax_2&\cdots &y_2\cdot Ax_k&\cdots &y_2\cdot Ax_n\\ \vdots&\vdots&\ddots&\vdots&\ddots&\vdots\\ y_k\cdot Ax_1&y_k\cdot Ax_2&\cdots&y_k\cdot Ax_k&\cdots&y_k\cdot Ax_n\\ \vdots&\vdots&\ddots&\vdots&\ddots&\vdots\\ y_n\cdot Ax_1&y_n\cdot Ax_2&\cdots &y_n\cdot Ax_k&\cdots&y_n\cdot Ax_n \end{pmatrix}\\
&=\begin{pmatrix}y_1\cdot (\lambda x_1)&y_1\cdot (\lambda x_2)&\cdots& y_1\cdot (\lambda x_k)&\cdots&y_1\cdot Ax_n\\ y_2\cdot (\lambda x_1)&y_2\cdot (\lambda x_2)&\cdots &y_2\cdot (\lambda x_k)&\cdots &y_2\cdot Ax_n\\ \vdots&\vdots&\ddots&\vdots&\ddots&\vdots\\ y_k\cdot (\lambda x_1)&y_k\cdot (\lambda x_2)&\cdots&y_k\cdot (\lambda x_k)&\cdots&y_k\cdot Ax_n\\ \vdots&\vdots&\ddots&\vdots&\ddots&\vdots\\ y_n\cdot (\lambda x_1)&y_n\cdot (\lambda x_2)&\cdots &y_n\cdot (\lambda x_k)&\cdots&y_n\cdot Ax_n \end{pmatrix}\\
&=\begin{pmatrix}\lambda&0&\cdots& 0&\cdots&y_1\cdot Ax_n\\ 0&\lambda&\cdots &0&\cdots &y_2\cdot Ax_n\\ \vdots&\vdots&\ddots&\vdots&\ddots&\vdots\\ 0&0&\cdots&\lambda&\cdots&y_k\cdot Ax_n\\ \vdots&\vdots&\ddots&\vdots&\ddots&\vdots\\ 0&0&\cdots &0&\cdots&y_n\cdot Ax_n \end{pmatrix}\\
&=\begin{pmatrix}\lambda I_k&B\\ 0&C\end{pmatrix}\end{aligned}$$

Thus, if we write the characteristic polynomial of $$A$$ as $$p_A(\mathbf{x})$$, then by [§Characteristic Polynomial, ⁋Corollary 4](/en/math/linear_algebra/characteristic_polynomial#cor4) we have $$p_A(\mathbf{x})=p_{A'}(\mathbf{x})$$, and therefore

$$p_A(\mathbf{x})=p_{A'}(\mathbf{x})=\det(\mathbf{x}I-A')=(\mathbf{x}-\lambda)^k\det(\mathbf{x}I_{n-k}-C)$$

That is, the algebraic multiplicity of $$\lambda$$ in $$p_A$$ is at least $$k$$.

</details>

Given an $$n\times n$$ matrix $$A$$, if we let $$p_A$$ be the characteristic polynomial of $$A$$, then the sum of the algebraic multiplicities of the eigenvalues $$\lambda$$ cannot exceed $$n$$, the degree of $$p_A$$. Also, for a fixed eigenvalue $$\lambda$$, the above proposition shows that the geometric multiplicity of $$\lambda$$ cannot exceed its algebraic multiplicity. Finally, from the argument after [Proposition 4](#prop4), we can see that in order to decompose $$\mathbb{K}^n$$ into eigenspaces, the sum of the geometric multiplicities of the $$\lambda$$ must equal $$n$$. Putting all this together, we obtain the following proposition.

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6**</ins> For any $$n\times n$$ matrix $$A$$, the necessary and sufficient condition for $$\mathbb{K}^n$$ to be expressible as a direct sum of the eigenspaces of $$A$$ is:

1. The characteristic polynomial of $$A$$ has $$n$$ roots counting multiplicity, and
2. For each eigenvalue, the geometric multiplicity equals the algebraic multiplicity.

</div>

In particular, if $$\mathbb{K}$$ is an algebraically closed field, the first condition is always satisfied, so we only need to consider the second condition.

We assume that the field $$\mathbb{K}$$ is algebraically closed while dealing with diagonalization of matrices. This is purely for convenience; if $$\mathbb{K}$$ is not algebraically closed, we simply consider a field extension obtained by adjoining the roots of the characteristic polynomial of the matrix of interest. ([\[Field Theory\] §Algebraic Extensions](/en/math/field_theory/algebraic_extensions)) This is exactly the same as obtaining $$\mathbb{C}$$ from $$\mathbb{R}$$ by adjoining the imaginary root $$i$$ of the equation $$\x^2+1=0$$, for example.

## Diagonalization of Matrices

We have previously examined how to decompose $$\mathbb{R}^n$$ through the eigenvalues and eigenspaces of an arbitrary $$n\times n$$ matrix $$A$$, and from [Proposition 6](#prop6) we have also learned when such a decomposition is possible. Let us look again at the proof of [Proposition 5](#prop5) that we used to prove this. We added $$n-k$$ arbitrary vectors to a basis $$x_1,\ldots, x_k$$ of $$E_\lambda$$, then defined the matrix $$X=(x_1\mid\cdots\mid x_n)$$ through these, and by calculation showed that

$$XAX^{-1}=\begin{pmatrix}\lambda I_k&B\\0&C\end{pmatrix}$$

has the upper left $$k\times k$$ block matrix as the diagonal matrix $$\lambda I_k$$. However, if $$A$$ satisfies all the conditions of [Proposition 6](#prop6), instead of adding the $$n-k$$ vectors $$x_{k+1},\ldots, x_n$$ arbitrarily, we can choose them so that all $$n$$ vectors $$x_1,\ldots, x_n$$ become bases of the eigenspaces of $$A$$. Then from

$$y_i\cdot x_j=\begin{cases}1&i=j\\0&i\neq j\end{cases}$$

in the proof of [Proposition 5](#prop5), we can see that $$C$$ also becomes a diagonal matrix and $$B$$ becomes the zero matrix. Therefore the following holds.

<div class="proposition" markdown="1">

<ins id="prop7">**Proposition 7**</ins> Consider an $$n\times n$$ matrix $$A$$ satisfying all the conditions of [Proposition 6](#prop6), and let $$x_1,\ldots, x_n$$ be a basis of $$\mathbb{R}^n$$ consisting of bases of the eigenspaces. Let $$Ax_i=\lambda_ix_i$$ and $$X=(x_1\mid\cdots\mid x_n)$$. Then for the diagonal matrix

$$D=\begin{pmatrix}\lambda_1&0&\cdots&0\\ 0&\lambda_2&\cdots&0\\ \vdots&\vdots&\ddots&\vdots\\0&0&\cdots&\lambda_n\end{pmatrix}$$

we have $$A=XDX^{-1}$$.

</div>

Thus we can give a suitable name to a matrix $$A$$ satisfying this condition.

<div class="definition" markdown="1">

<ins id="def8">**Definition 8**</ins> An $$n\times n$$ matrix $$A$$ satisfying all the conditions of [Proposition 6](#prop6) is called *diagonalizable*.

</div>

Alternatively, since [Proposition 6](#prop6) was a necessary and sufficient condition, there is no problem in calling a matrix similar to a diagonal matrix diagonalizable. In other words, any diagonalizable matrix is completely determined by its eigenvalues.

That diagonalizable matrices are conceptually important has been sufficiently examined above. Moreover, diagonalizable matrices are also greatly helpful in terms of computational convenience. For example, if a matrix $$A$$ is diagonalizable with $$A=XDX^{-1}$$, then the powers of $$A$$ are given by $$A^k=XD^kX^{-1}$$, and since the power of a diagonal matrix is merely the diagonal matrix made of the powers of each component, computing powers of $$A$$ becomes a very easy task.

More generally, if matrices $$A_1,\ldots, A_k$$ are diagonalizable through the same matrix $$X$$, that is, if

$$A_i=XD_iX^{-1}$$

then

$$A_1A_2\cdots A_k =XD_1D_2\cdots D_kX^{-1}$$

and since the product of diagonal matrices is merely the diagonal matrix consisting of the products of the diagonal entries, computing $$A_1A_2\cdots A_k$$ may also not be very difficult. We give such a case the following name.

<div class="definition" markdown="1">

<ins id="def9">**Definition 9**</ins> A family of matrices $$\{A_i\}$$ is called *simultaneously diagonalizable* if there exists an invertible matrix $$X$$ such that $$X^{-1}A_iX$$ is a diagonal matrix for every $$i$$.

</div>

If two matrices $$A,B$$ are simultaneously diagonalizable through a fixed matrix $$X$$, then from the equation

$$AB=XD_AX^{-1}XD_BX^{-1}=XD_AD_BX^{-1}=XD_BD_AX^{-1}=BA$$

we know that the two matrices $$A, B$$ commute. The following proposition shows that the converse also holds (for diagonalizable matrices).

<div class="proposition" markdown="1">

<ins id="prop10">**Proposition 10**</ins> If two diagonalizable matrices $$A,B$$ satisfy the condition $$AB=BA$$, then $$A, B$$ are simultaneously diagonalizable.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Essentially, it suffices to show that the two matrices $$A,B$$ give the same eigenspace decomposition. Consider the eigenspace decomposition using $$A$$:

$$V=\bigoplus_{\lambda}E_\lambda(A)$$

Then for any $$v\in E_\lambda(A)$$, from the equation

$$A(Bv)=ABv=BAv=B(\lambda v)=\lambda(Bv)$$

we know that $$Bv\in E_\lambda(A)$$. Now viewing $$B$$ as a linear operator on the vector space $$E_\lambda(A)$$, since the original linear operator $$B$$ was diagonalizable, $$B$$ is also diagonalizable on $$E_\lambda(A)$$, and therefore there exists a basis of $$E_\lambda(A)$$ consisting of eigenvectors of $$B$$. Now any element of $$E_\lambda(A)$$ is an eigenvector of $$A$$ (corresponding to eigenvalue $$\lambda$$), so these are also eigenvectors of $$A$$.

</details>

## Eigenspace Decomposition of Linear Operators

So far we have examined the process of diagonalizing a given matrix, and fundamentally this is the same as decomposing a vector space into eigenspaces when a (diagonalizable) linear operator is given. To prove this we actively used bases of eigenspaces. Describing this without the choice of a basis will be helpful when we examine the Jordan canonical form in the next post.

For a finite-dimensional vector space $$V$$ and a linear operator $$L:V\rightarrow V$$, we have seen that the equation

$$\rank L +\nullity L=\dim V$$

holds. ([§Isomorphic Vector Spaces, ⁋Theorem 7](/en/math/linear_algebra/isomorphic_vector_spaces#thm7)) Here $$\rank L=\dim\im L$$ and $$\nullity L=\dim\ker L$$. However, this does not mean that $$V$$ can be expressed as a direct sum of $$\im L$$ and $$\ker L$$. For example, for the matrix $$A$$ that was the non-diagonalizable example after [Proposition 4](#prop4),

$$A-I=\begin{pmatrix}0&1&1\\0&0&1\\0&0&0\end{pmatrix}$$

the operator defined by this satisfies $$\ker (A-I)\cap \im(A-I)\neq \{0\}$$. However, if only $$\ker L\cap \im L=\{0\}$$ holds, then from [§Dimension of Vector Spaces, ⁋Example 8](/en/math/linear_algebra/dimension#ex8) and [Proposition 2](#prop2) we know that necessarily $$V=\ker L\oplus \im L$$. The following lemma gives a condition equivalent to this.

<div class="proposition" markdown="1">

<ins id="lem11">**Lemma 11**</ins> In the above situation, the condition $$\ker L\cap \im L=\{0\}$$ is equivalent to $$\ker L^2=\ker L$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

With a little thought, we know that $$\ker L^2=\ker L$$ is equivalent to $$\ker L^2\subset \ker L$$. Therefore what we need to show is the equivalence

$$\ker L\cap \im L=\{0\}\iff \ker L^2\subset\ker L$$

First, assume $$\ker L\cap \im L=\{0\}$$ and let $$v\in\ker L^2$$. Then $$0=L^2 v=L(Lv)$$, so $$Lv\in\ker L$$, and therefore by assumption we must have $$Lv=0$$. That is, $$v\in\ker L$$. Conversely, assume $$\ker L^2\subset \ker L$$ and let $$v\in \ker L\cap \im L$$. Then since $$v\in \im L$$, there exists $$w\in V$$ such that $$v=Lw$$. But since $$v\in\ker L$$ as well,

$$0=Lv=L(Lw)=L^2w\implies w\in\ker(L^2)\subset \ker L$$

so $$w\in \ker L$$. That is, $$v=Lw=0$$.

</details>

Returning to the original story, we are particularly interested in the case where $$L$$ is of the form $$A-\lambda I$$ for some linear operator and its eigenvalue. The following proposition uses [Lemma 11](#lem11) to characterize diagonalizability concisely.

<div class="proposition" markdown="1">

<ins id="prop12">**Proposition 12**</ins> A linear operator $$A:V\rightarrow V$$ is diagonalizable if and only if for every eigenvalue $$\lambda\in\sigma(A)$$,

$$\ker(A-\lambda I)^2=\ker(A-\lambda I)$$

holds.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, suppose $$A$$ is diagonalizable. Then $$V=\bigoplus_{\mu\in\sigma(A)} E_\mu(A)$$. For any $$v\in\ker(A-\lambda I)^2$$, we can uniquely write $$v=\sum_{\mu\in\sigma(A)}v_\mu$$, and

$$(A-\lambda I)^2v=\sum_{\mu\in\sigma(A)}(A-\lambda I)^2v_\mu=\sum_{\mu\in\sigma(A)}(\mu-\lambda)^2v_\mu=0$$

By the uniqueness of the eigenspace decomposition, $$(\mu-\lambda)^2v_\mu=0$$ must hold for all $$\mu$$, and when $$\mu\neq\lambda$$ we have $$v_\mu=0$$, so

$$v=v_\lambda\in E_\lambda(A)=\ker(A-\lambda I)$$

Conversely, suppose that for every eigenvalue $$\lambda$$, we have $$\ker(A-\lambda I)^2=\ker(A-\lambda I)$$. From [Lemma 11](#lem11), for each $$\lambda$$,

$$\ker(A-\lambda I)\cap\im(A-\lambda I)=\{0\}$$

and by [§Isomorphic Vector Spaces, ⁋Theorem 7](/en/math/linear_algebra/isomorphic_vector_spaces#thm7),

$$\dim\ker(A-\lambda I)+\dim\im(A-\lambda I)=\dim V$$

so $$V=\ker(A-\lambda I)\oplus\im(A-\lambda I)$$. For convenience, let us write $$\ker(A-\lambda I)=E_\lambda(A)$$ and $$\im (A-\lambda I)=W_\lambda(A)$$. We first know that for any $$v\in W_\lambda(A)$$, if we write $$v=(A-\lambda I)w$$, then from

$$Av=A(A-\lambda I)w=(A-\lambda I)Aw\in W_\lambda(A)$$

we see that $$W_\lambda(A)$$ is an $$A$$-invariant subspace. That is,

$$A\vert_{W_\lambda(A)}: W_\lambda(A) \rightarrow W_\lambda(A)$$

is well-defined. Then from [Proposition 4](#prop4), if $$w\in W_\lambda(A)$$ is an eigenvector of $$A\vert_{W_\lambda(A)}$$ with eigenvalue $$\mu$$, then viewing $$w$$ as an element of $$V$$, it is also an eigenvector of $$A$$ (corresponding to eigenvalue $$\mu$$), and conversely, if an eigenvalue $$\mu\neq \lambda$$ of $$A$$ and its corresponding eigenvector are given, this can be viewed as an eigenvalue-eigenvector pair of $$A\vert_{W_\lambda(A)}$$. Also, for any eigenvalue $$\mu$$ of $$A\vert_{W_\lambda(A)}$$,

$$\ker (A_{W_\lambda(A)}-\mu I)=\ker (A_{W_\lambda(A)}-\mu I)^2$$

also holds on $$W_\lambda(A)$$ for a similar reason. That is, we can repeat this process inductively. On the other hand, since we are assuming that $$\mathbb{K}$$ is algebraically closed, we know that any linear operator $$W \rightarrow W$$ always has an eigenvalue as long as $$W$$ is not $$0$$-dimensional, and from this we know that this induction exactly gives the eigenspace decomposition of $$A$$.

</details>

---

**[Goc]** M.S. Gockenbach, *Finite-dimensional linear algebra*, Discrete Mathematics and its applications, Taylor&Francis, 2011.  
**[Lee]** 이인석, *선형대수와 군*, 서울대학교 출판문화원, 2005.

---

[^1]: Of course, as always, this sum is in fact assumed to be a finite sum. That is, we assume that $$(v_i)_{i\in I}$$ is finitely supported.
