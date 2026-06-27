---
title: "Minimal Polynomial"
description: "We define the operation of evaluating a polynomial at a matrix and prove the Cayley-Hamilton theorem using the primary decomposition theorem. We then introduce the minimal polynomial, show that it divides the characteristic polynomial, and discuss criteria for diagonalizability. Finally, we construct the Jordan-Chevalley decomposition, which splits an operator into its diagonalizable and nilpotent parts."
excerpt: "Cayley-Hamilton theorem and minimal polynomial"

categories: [Math / Linear Algebra]
permalink: /en/math/linear_algebra/minimal_polynomial
sidebar: 
    nav: "linear_algebra-en"


date: 2026-06-28

weight: 18
translated_at: 2026-06-27T19:00:02+00:00
translation_source: kimi-cli
---
Through the Jordan canonical form, we decomposed an arbitrary linear operator into Jordan blocks on generalized eigenspaces. This structure is also useful for examining the relationship between polynomials and linear operators. In this post, we define the operation of substituting a polynomial into a matrix, and through this we cover the Cayley–Hamilton theorem and the minimal polynomial.

## Polynomials in Matrices

Since powers of matrices, scalar multiplication, and addition are all well defined, substituting a polynomial into a matrix is also naturally defined. In this post, $$\mathbb{K}[\x]$$ denotes the space of (finite-degree) polynomials defined in [§Subspaces, ⁋Example 5](/en/math/linear_algebra/subspaces#ex5).

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> For an $$n\times n$$ matrix $$A$$ and a polynomial $$p(\x)=\sum_{i=0}^d a_i\x^i\in\mathbb{K}[\x]$$, we define the matrix obtained by *evaluating* $$p$$ at $$A$$ by the formula

$$p(A)=\sum_{i=0}^d a_iA^i=a_dA^d+\cdots+a_1A+a_0I$$

Here we adopt the convention $$A^0=I$$. The same definition applies to a linear operator $$L:V\rightarrow V$$, giving $$p(L)$$.

</div>

This evaluation transfers addition and multiplication of polynomials to that of matrices. In particular, the following proposition is frequently used in the discussion below.

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> For an $$n\times n$$ matrix $$A$$ and any two polynomials $$p,q\in\mathbb{K}[\x]$$, the following two identities hold:

$$(p+q)(A)=p(A)+q(A),\qquad (pq)(A)=p(A)q(A)$$

In particular, $$p(A)$$ and $$q(A)$$ commute.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

The identity for addition is obvious from the definition. For multiplication, write $$p(\x)=\sum_i a_i\x^i$$ and $$q(\x)=\sum_j b_j\x^j$$; then the coefficient of $$\x^k$$ in $$pq$$ is $$\sum_{i+j=k}a_ib_j$$, so

$$(pq)(A)=\sum_k\left(\sum_{i+j=k}a_ib_j\right)A^k=\sum_{i,j}a_ib_jA^{i+j}=\left(\sum_i a_iA^i\right)\left(\sum_j b_jA^j\right)=p(A)q(A)$$

Here we used that $$A^iA^j=A^{i+j}=A^jA^i$$. Finally, since polynomial multiplication is commutative, $$p(A)q(A)=(pq)(A)=(qp)(A)=q(A)p(A)$$.

</details>

## Cayley–Hamilton Theorem

We now prove the remarkable fact that substituting any matrix into its characteristic polynomial always yields the zero matrix. Before that, let us note the (obvious) fact that the nilpotency index of a nilpotent operator cannot exceed the dimension of the space.

<div class="proposition" markdown="1">

<ins id="lem3">**Lemma 3**</ins> For a nilpotent operator $$N:V\rightarrow V$$ defined on an $$m$$-dimensional vector space $$V$$, we have $$N^m=0$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

By [§Jordan Canonical Form, ⁋Lemma 1](/en/math/linear_algebra/Jordan_canonical_form#lem1), there exists a filtration

$$0=\ker N^0\subsetneq\ker N^1\subsetneq\cdots\subsetneq\ker N^k=\ker N^{k+1}=\cdots$$

where $$k$$ is the nilpotency index of $$N$$. Since $$N$$ is nilpotent, $$\ker N^k=V$$ for some integer, and because all the inclusions are strict,

$$0=\dim\ker N^0<\dim\ker N^1<\cdots<\dim\ker N^k=m$$

so the dimension increases by at least $$1$$ at each step. Therefore $$k\leq m$$, and in particular $$N^m=0$$.

</details>

Then we can prove the following.

<div class="proposition" markdown="1">

<ins id="thm4">**Theorem 4 (Cayley–Hamilton)**</ins> For any linear operator $$A:V\rightarrow V$$ defined on a finite-dimensional vector space $$V$$ and its characteristic polynomial $$p_A$$, we have $$p_A(A)=0$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Assume $$\mathbb{K}$$ is algebraically closed. By [§Jordan Canonical Form, ⁋Theorem 6](/en/math/linear_algebra/Jordan_canonical_form#thm6), letting $$\lambda_1,\ldots,\lambda_r$$ be the distinct eigenvalues of $$A$$, we have a decomposition

$$V=G_{\lambda_1}(A)\oplus\cdots\oplus G_{\lambda_r}(A)$$

Then by the results of [§Jordan Canonical Form](/en/math/linear_algebra/Jordan_canonical_form), for each $$\lambda=\lambda_i$$ the operator $$(A-\lambda I)\vert_{G_\lambda(A)}$$ is nilpotent on $$G_\lambda(A)$$, its dimension is $$\dim G_\lambda(A)=d_\lambda$$, where $$d_\lambda$$ is the algebraic multiplicity of $$\lambda$$. Therefore by [Lemma 3](#lem3),

$$(A-\lambda I)^{d_\lambda}v=0\qquad\text{for all $v\in G_\lambda(A)$}$$

Now since $$p_A(\x)=\prod_{i=1}^r(\x-\lambda_i)^{d_{\lambda_i}}$$, for any $$v\in G_\lambda(A)$$, using from [Proposition 2](#prop2) that the factors commute, we have

$$p_A(A)v=\left(\prod_{\mu\neq\lambda}(A-\mu I)^{d_\mu}\right)(A-\lambda I)^{d_\lambda}v=0$$

Since $$V$$ is the direct sum of the $$G_\lambda(A)$$, we have $$p_A(A)v=0$$ for any $$v\in V$$, and thus $$p_A(A)=0$$.

</details>

We have only considered the case where $$\mathbb{K}$$ is an algebraically closed field; if it is not, we may take any algebraically closed field $$\mathbb{L}$$ containing $$\mathbb{K}$$ (for example, $$\mathbb{C}$$ for $$\mathbb{R}$$), and regard $$p$$ as a polynomial over $$\mathbb{L}$$. In this case, the characteristic polynomial of $$A$$ is still $$p_A$$ over $$\mathbb{L}$$, so by the proof above we likewise obtain $$p_A(A)=0$$, and since all coefficients of this polynomial belong to $$\mathbb{K}$$, this equality also holds over $$\mathbb{K}$$. However, showing the existence of such an $$\mathbb{L}$$ is difficult at our present level, so we have briefly explained this outside the proof. In any case, intuitively the Cayley–Hamilton theorem says that because the characteristic polynomial contains all eigenvalues of $$A$$ with sufficiently high multiplicity, substituting $$A$$ annihilates even the nilpotent part on each generalized eigenspace.

## Minimal Polynomial

The Cayley–Hamilton theorem shows that there always exists a nonzero polynomial $$p$$ satisfying $$p(A)=0$$. Let us name the simplest such polynomial.

<div class="definition" markdown="1">

<ins id="def5">**Definition 5**</ins> For an $$n\times n$$ matrix $$A$$, among the monic polynomials satisfying $$p(A)=0$$, the one of smallest degree is called the *minimal polynomial* of $$A$$ and is denoted $$m_A$$.

</div>

By [Theorem 4](#thm4), we have $$p_A(A)=0$$, and dividing $$p_A$$ by its leading coefficient yields a monic polynomial, so the monic polynomial of smallest degree in the above definition certainly exists. The following proposition shows that this minimal polynomial is unique and divides every polynomial that annihilates $$A$$.

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6**</ins> For an $$n\times n$$ matrix $$A$$, if a polynomial $$p$$ satisfies $$p(A)=0$$, then $$m_A\mid p$$. In particular, the minimal polynomial of $$A$$ is unique, and $$m_A\mid p_A$$ holds.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

By the division algorithm for polynomials, there exist polynomials $$q,r$$ such that $$p=qm_A+r$$ and either $$r=0$$ or $$\deg r<\deg m_A$$. By [Proposition 2](#prop2),

$$r(A)=p(A)-q(A)m_A(A)=0-q(A)\cdot 0=0$$

If $$r\neq 0$$, then dividing $$r$$ by its leading coefficient would yield a monic polynomial of degree less than $$m_A$$ that annihilates $$A$$, contradicting the minimality of $$m_A$$. Therefore $$r=0$$ and $$m_A\mid p$$.

To show uniqueness, suppose $$m_A'$$ also satisfies the condition for a minimal polynomial. Then by the argument above, $$m_A\mid m_A'$$ and $$m_A'\mid m_A$$, and since both are monic polynomials of the same degree, $$m_A=m_A'$$. Finally, from [Theorem 4](#thm4) we have $$p_A(A)=0$$, so $$m_A\mid p_A$$.

</details>

The roots of the minimal polynomial coincide exactly with the roots of the characteristic polynomial. That is, the degree may be smaller, but the only way degrees drop is by lowering multiplicities at repeated eigenvalues, so no eigenvalue is lost in this process.

<div class="proposition" markdown="1">

<ins id="prop7">**Proposition 7**</ins> For an $$n\times n$$ matrix $$A$$, the set of roots of $$m_A$$ equals the set of eigenvalues of $$A$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, for any polynomial $$p$$, eigenvalue $$\lambda$$, and corresponding eigenvector $$v$$, we have $$A^iv=\lambda^iv$$, so $$p(A)v=p(\lambda)v$$. Now if $$\lambda$$ is an eigenvalue of $$A$$ and $$v\neq 0$$ is a corresponding eigenvector, then

$$0=m_A(A)v=m_A(\lambda)v$$

and since $$v\neq 0$$, we have $$m_A(\lambda)=0$$. Thus every eigenvalue is a root of $$m_A$$. Conversely, if $$\lambda$$ is a root of $$m_A$$, then from $$m_A\mid p_A$$ in [Proposition 6](#prop6), $$\lambda$$ is a root of $$p_A$$, i.e., an eigenvalue of $$A$$.

</details>

Now using the Jordan canonical form, we can determine the exact form of the minimal polynomial. In the following theorem, $$e_\lambda$$ denotes the nilpotency index of the nilpotent operator $$(A-\lambda I)\vert_{G_\lambda(A)}$$ on the generalized eigenspace $$G_\lambda(A)$$, i.e., the size of the largest Jordan block corresponding to $$\lambda$$.

<div class="proposition" markdown="1">

<ins id="thm8">**Theorem 8**</ins> Assume $$\mathbb{K}$$ is algebraically closed. Let $$\lambda_1,\ldots,\lambda_r$$ be the distinct eigenvalues of an $$n\times n$$ matrix $$A$$. Then the identity

$$m_A(\x)=\prod_{i=1}^r(\x-\lambda_i)^{e_{\lambda_i}}$$

holds.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Fix $$\lambda=\lambda_i$$ and let $$e_\lambda$$ be the nilpotency index of $$N_\lambda=(A-\lambda I)\vert_{G_\lambda(A)}$$. Expanding an arbitrary monic polynomial $$p$$ about $$\lambda$$ as

$$p(\x)=\sum_{j\geq 0}c_j(\x-\lambda)^j$$

then on $$G_\lambda(A)$$ we have $$(A-\lambda I)\vert_{G_\lambda(A)}=N_\lambda$$, so by [Proposition 2](#prop2)

$$p(A)\vert_{G_\lambda(A)}=\sum_{j\geq 0}c_jN_\lambda^j=\sum_{j=0}^{e_\lambda-1}c_jN_\lambda^j$$

The last equality follows from $$N_\lambda^j=0$$ for $$j\geq e_\lambda$$. On the other hand, since $$N_\lambda^{e_\lambda-1}\neq 0$$, there exists $$w\in G_\lambda(A)$$ with $$N_\lambda^{e_\lambda-1}w\neq 0$$, and by [§Jordan Canonical Form, ⁋Lemma 8](/en/math/linear_algebra/Jordan_canonical_form#lem8), the vectors $$w, N_\lambda w,\ldots, N_\lambda^{e_\lambda-1}w$$ are linearly independent. Therefore $$\sum_{j=0}^{e_\lambda-1}c_jN_\lambda^jw=0$$ only if $$c_0=\cdots=c_{e_\lambda-1}=0$$, and consequently

$$p(A)\vert_{G_\lambda(A)}=0\iff (\x-\lambda)^{e_\lambda}\mid p$$

Now from the decomposition $$V=\bigoplus_i G_{\lambda_i}(A)$$ in [§Jordan Canonical Form, ⁋Theorem 6](/en/math/linear_algebra/Jordan_canonical_form#thm6), $$p(A)=0$$ is equivalent to $$p(A)\vert_{G_{\lambda_i}(A)}=0$$ for all $$i$$, which is in turn equivalent to $$(\x-\lambda_i)^{e_{\lambda_i}}\mid p$$ for all $$i$$, i.e., $$\prod_i(\x-\lambda_i)^{e_{\lambda_i}}\mid p$$. Among such monic polynomials, the one of smallest degree is $$\prod_i(\x-\lambda_i)^{e_{\lambda_i}}$$ itself, so this is precisely $$m_A$$.

</details>

In particular, the minimal polynomial gives a concise criterion for diagonalizability.

<div class="proposition" markdown="1">

<ins id="cor9">**Corollary 9**</ins> Assume $$\mathbb{K}$$ is algebraically closed. An $$n\times n$$ matrix $$A$$ is diagonalizable if and only if $$m_A$$ is a product of distinct linear factors, i.e., of the form

$$m_A(\x)=\prod_{i=1}^r(\x-\lambda_i)$$

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

$$A$$ is diagonalizable if and only if for every eigenvalue $$\lambda$$ we have $$\ker(A-\lambda I)^2=\ker(A-\lambda I)$$, i.e., $$G_\lambda(A)=\ker(A-\lambda I)$$. ([§Eigenspace Decomposition, ⁋Proposition 12](/en/math/linear_algebra/eigenspace_decomposition#prop12)) This is equivalent to $$N_\lambda=0$$, i.e., $$e_\lambda=1$$, for every $$\lambda$$. By [Theorem 8](#thm8), this is equivalent to $$m_A$$ being a product of distinct linear factors.

</details>

<div class="example" markdown="1">

<ins id="ex10">**Example 10**</ins> Consider the matrix from [§Jordan Canonical Form, ⁋Example 2](/en/math/linear_algebra/Jordan_canonical_form#ex2)

$$A=\begin{pmatrix}1&1&1\\0&1&1\\0&0&1\end{pmatrix}$$

The characteristic polynomial of this matrix is $$(\x-1)^3$$, and for the unique eigenvalue $$1$$ we have $$(A-I)^2\neq 0$$ but $$(A-I)^3=0$$, so $$e_1=3$$. Therefore $$m_A(\x)=(\x-1)^3=p_A(\x)$$, and since this is a power of a linear factor, $$A$$ is not diagonalizable by [Corollary 9](#cor9). On the other hand, for the matrix

$$B=\begin{pmatrix}0&1\\1&0\end{pmatrix}$$

the characteristic polynomial is $$\x^2-1=(\x-1)(\x+1)$$, and since $$B^2=I$$, we have $$(B-I)(B+I)=B^2-I=0$$. Thus $$m_B(\x)=(\x-1)(\x+1)$$, which is a product of two distinct linear factors, so $$B$$ is diagonalizable by [Corollary 9](#cor9). That is, what determines diagonalizability is not the characteristic polynomial but whether the minimal polynomial has repeated factors; in the case of $$A$$, $$m_A=(\x-1)^3$$ retains a repeated factor and fails to diagonalize.

</div>

## Jordan–Chevalley Decomposition

In the discussion so far, the Jordan form has been the central tool and motivation. On the other hand, thinking of each Jordan block, it splits into two pieces: a diagonal part containing the eigenvalue and a nilpotent part appearing as super-diagonal entries. We close this post by applying our discussion so far to extend this decomposition to the whole space.

First, let us observe three facts needed for the uniqueness of the decomposition.

1. The only operator that is simultaneously diagonalizable and nilpotent is $$0$$. Such an operator is nilpotent, so all its eigenvalues are $$0$$, and being diagonalizable, in a suitable basis it equals a diagonal matrix all of whose diagonal entries are $$0$$.
2. The difference of two commuting diagonalizable operators is again diagonalizable. By [§Eigenspace Decomposition, ⁋Proposition 10](/en/math/linear_algebra/eigenspace_decomposition#prop10), two commuting diagonalizable operators are simultaneously diagonalizable, so in a common eigenbasis both operators are diagonal and their difference is also diagonal in the same basis.
3. The difference of two commuting nilpotent operators $$N,M$$ is again nilpotent. If $$N^a=M^b=0$$, then since $$N,M$$ commute, the binomial theorem gives $$(N-M)^{a+b}=0$$.

<div class="proposition" markdown="1">

<ins id="thm11">**Theorem 11 (Jordan–Chevalley Decomposition)**</ins> Assume $$\mathbb{K}$$ is algebraically closed. For any linear operator $$A:V\rightarrow V$$, there exist uniquely a diagonalizable operator $$A_s$$ and a nilpotent operator $$A_n$$ satisfying

$$A=A_s+A_n,\qquad A_sA_n=A_nA_s.$$

Moreover, $$A_s$$ and $$A_n$$ are expressed as polynomials in $$A$$ with zero constant term. We call $$A_s$$ the diagonalizable part and $$A_n$$ the nilpotent part of $$A$$.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

First we show existence. By [§Jordan Canonical Form, ⁋Theorem 6](/en/math/linear_algebra/Jordan_canonical_form#thm6), for the distinct eigenvalues $$\lambda_1,\ldots,\lambda_r$$ of $$A$$ we have a decomposition

$$V=G_{\lambda_1}(A)\oplus\cdots\oplus G_{\lambda_r}(A)$$

and as in [Theorem 8](#thm8), letting $$e_i$$ be the nilpotency index of $$(A-\lambda_iI)\vert_{G_{\lambda_i}(A)}$$, we have $$(A-\lambda_iI)^{e_i}=0$$ on $$G_{\lambda_i}(A)$$ and

$$m_A(\x)=\prod_{i=1}^r(\x-\lambda_i)^{e_i}$$

On each $$G_{\lambda_i}(A)$$, $$A$$ is the sum of the scalar $$\lambda_iI$$ and the nilpotent operator $$A-\lambda_iI$$; assembling these over the whole space, we define $$A_s$$ to be $$\lambda_iI$$ on each $$G_{\lambda_i}(A)$$ and $$A_n=A-A_s$$. Then $$A_s$$ is diagonalizable, $$A_n$$ is nilpotent, and since $$A_s$$ is scalar on each piece, they commute, yielding the decomposition $$A=A_s+A_n$$.

Thus the heart of the claim is the remaining part, especially that they are expressed as polynomials. This starts from the fact that for distinct $$\lambda_i$$, the polynomials $$(\x-\lambda_i)^{e_i}$$ are pairwise coprime, so there exists a polynomial $$p$$ satisfying all the congruences

$$p(\x)\equiv\lambda_i\pmod{(\x-\lambda_i)^{e_i}}\quad(i=1,\ldots,r),\qquad p(\x)\equiv 0\pmod{\x}$$

This is a generalization of the Chinese remainder theorem; its precise statement and proof will be treated separately in ring theory. Accepting this, for each $$i$$ the polynomial $$p(\x)-\lambda_i$$ is divisible by $$(\x-\lambda_i)^{e_i}$$, so using that $$(A-\lambda_iI)^{e_i}=0$$ on $$G_{\lambda_i}(A)$$, we obtain from [Proposition 2](#prop2) that $$p(A)-\lambda_iI=0$$, i.e., $$p(A)=\lambda_iI=A_s$$. Therefore $$A_s=p(A)$$, and since $$p(0)=0$$, $$p$$ has no constant term; moreover $$A_n=A-p(A)=q(A)$$ (with $$q(\x)=\x-p(\x)$$) is also a polynomial in $$A$$ with no constant term.

Finally, to show uniqueness, suppose $$A=S+N$$ satisfies the same conditions, i.e., $$S$$ diagonalizable, $$N$$ nilpotent, $$SN=NS$$. Then $$S$$ and $$N$$ commute with $$S+N=A$$, hence also commute with $$A_s=p(A)$$ and $$A_n=q(A)$$, which are polynomials in $$A$$. From $$A=A_s+A_n=S+N$$ we have

$$A_s-S=N-A_n$$

On the left-hand side, $$A_s$$ and $$S$$ are commuting diagonalizable operators, so their difference is diagonalizable; on the right-hand side, $$N$$ and $$A_n$$ are commuting nilpotent operators, so their difference is nilpotent. Therefore $$A_s-S$$ is simultaneously diagonalizable and nilpotent, hence $$0$$, and consequently $$A_s=S$$, $$A_n=N$$.

</details>

The key content of this theorem, as can be seen from its proof, is that the two parts $$A_s$$ and $$A_n$$ of the decomposition are polynomials in $$A$$. That is, while their construction follows almost directly from the Jordan canonical form, the fact that they are expressed as polynomials in $$A$$ is the most nontrivial aspect and also the most useful. For example, the following holds.

<div class="proposition" markdown="1">

<ins id="cor12">**Corollary 12**</ins> $$A_s$$ and $$A_n$$ commute with every operator $$B$$ that commutes with $$A$$. In particular, $$A$$-invariant subspaces are also $$A_s$$-invariant and $$A_n$$-invariant.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

By [Theorem 11](#thm11), $$A_s=p(A)$$ and $$A_n=q(A)$$ are polynomials in $$A$$. If $$AB=BA$$, then $$A^iB=BA^i$$, so $$p(A)B=Bp(A)$$ and $$q(A)B=Bq(A)$$. Also, if $$W$$ is $$A$$-invariant, i.e., $$A(W)\subseteq W$$, then $$A^i(W)\subseteq W$$ for all $$i$$, so $$p(A)(W)\subseteq W$$, i.e., $$A_s(W)\subseteq W$$, and similarly $$A_n(W)\subseteq W$$.

</details>

<div class="example" markdown="1">

<ins id="ex13">**Example 13**</ins> Consider the matrix

$$A=\begin{pmatrix}2&1&0\\0&2&0\\0&0&3\end{pmatrix}$$

The generalized eigenspace for eigenvalue $$2$$ is the 2-dimensional space spanned by $$e_1,e_2$$, on which the nilpotency index of $$A-2I$$ is $$2$$; the generalized eigenspace for eigenvalue $$3$$ is spanned by $$e_3$$. Setting $$p(\x)=\x^2-4\x+6$$, we have $$p(2)=2$$, $$p'(2)=0$$, $$p(3)=3$$, so $$p$$ satisfies the congruences $$p\equiv 2\pmod{(\x-2)^2}$$, $$p\equiv 3\pmod{\x-3}$$ of [Theorem 11](#thm11), and

$$A_s=p(A)=A^2-4A+6I=\begin{pmatrix}2&0&0\\0&2&0\\0&0&3\end{pmatrix},\qquad A_n=A-A_s=\begin{pmatrix}0&1&0\\0&0&0\\0&0&0\end{pmatrix}$$

Here $$A_s$$ is diagonalizable, $$A_n$$ is nilpotent, the two operators commute, and $$A=A_s+A_n$$.

</div>

---

**References**

**[Goc]** M.S. Gockenbach, *Finite-dimensional linear algebra*, Discrete Mathematics and its applications, Taylor&Francis, 2011.  
**[Lee]** 이인석, *선형대수와 군*, 서울대학교 출판문화원, 2005.

---
