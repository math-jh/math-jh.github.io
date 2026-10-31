---
title: "Jordan Canonical Form"
description: "We introduce the notion of generalized eigenspaces for non-diagonalizable linear operators and explain how to obtain the Jordan canonical form by compensating for the dimension deficiency of eigenspaces through filtrations."
excerpt: "Constructing the Jordan canonical form via generalized eigenspace decomposition"

categories: [Math / Linear Algebra]
permalink: /en/math/linear_algebra/Jordan_canonical_form
sidebar: 
    nav: "linear_algebra-en"

date: 2026-01-21
weight: 17
translated_at: 2026-06-24T09:00:03+00:00
translation_source: kimi-cli
last_polished_at: 2026-10-17T19:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
## Generalized Eigenspaces

Previously, we saw that whenever a diagonalizable operator $A$ is given, we can decompose the given space into eigenspaces on which $A$ acts like scalar multiplication. However, as examined in [§Eigenspace Decomposition, ⁋Proposition 6](/en/math/linear_algebra/eigenspace_decomposition#prop6){: data-lid="b8nee" }, even if we assume $\mathbb{K}$ is an algebraically closed field (and, as we examined after that proposition, we will always assume this), not every linear operator is always diagonalizable. 

The second condition of [§Eigenspace Decomposition, ⁋Proposition 6](/en/math/linear_algebra/eigenspace_decomposition#prop6){: data-lid="zwl6p" } fails when $A$ has some eigenvalue $\lambda$ for which the geometric multiplicity of $\lambda$ is less than the algebraic multiplicity of $\lambda$. ([§Eigenspace Decomposition, ⁋Proposition 5](/en/math/linear_algebra/eigenspace_decomposition#prop5){: data-lid="hkefb" }) In other words, intuitively, the following vector space

$$E_\lambda(A)=\ker(A-\lambda I)$$

is <em>too small</em>. The following lemma gives a clue for resolving this. 

::: Lemma 1
On a finite-dimensional vector space $V$, let an arbitrary linear operator $L:V\rightarrow V$ defined on it be given. For notational convenience, let $L^0=\id_V$. Then the following filtration

$$0=\ker L^0\subsetneq \ker L^1\subsetneq \ker L^2\subsetneq \cdots \subsetneq \ker L^{k-1}\subsetneq \ker L^k=\ker L^{k+1}$$

exists. 
:::
::: Proof
First, for any $i$, if $v\in \ker L^{i}$ holds, then

$$L^{i+1}v=L(L^iv)=L(0)=0$$

so $\ker L^i\subseteq \ker L^{i+1}$ is obvious. On the other hand, since $V$ is finite-dimensional, this filtration must eventually stop increasing. What we need to show is that if $\ker L^k=\ker L^{k+1}$, then <em>all</em> subsequent terms are equal to $\ker L^k$. For this, let $k$ be the smallest integer satisfying $\ker L^k=\ker L^{k+1}$. Here, if $i<k$, then by the minimality of $k$ we have $\ker L^i\neq \ker L^{i+1}$, so it also follows that the inclusions in the filtration above are strict. Then by definition $\ker L^k=\ker L^{k+1}$, and using this as the base step, we can inductively show that $\ker L^k=\ker L^{k+j}$ holds for all $j$. That is, assuming that $\ker L^k=\ker L^{k+j}$ holds, let us show that $\ker L^k=\ker L^{k+j+1}$. For this, it suffices to show that $\ker L^{k+j+1}\subseteq \ker L^k$. Now for any $v\in \ker L^{k+j+1}$, since we know that $Lv\in \ker L^{k+j}=\ker L^k$, from the following calculation

$$L^{k+1}v=L^k(Lv)=0\implies v\in \ker L^{k+1}$$

and the base step $\ker L^k=\ker L^{k+1}$, we obtain the desired result. 
:::

Our key observation is that although the eigenspace $E_\lambda(A)$ has insufficient dimension, if we apply [Lemma 1](#lem1){: data-lid="8t70t" } to $L=A-\lambda I$ and enlarge this space, we eventually obtain the "correct dimension." 

::: Example 2
Consider the following matrix

$$A=\begin{pmatrix}1&1&1\\0&1&1\\0&0&1\end{pmatrix}$$

In a previous post, we saw that although the characteristic polynomial of this matrix is $(\x-1)^3=0$ (that is, the algebraic multiplicity of the unique eigenvalue $1$ is $3$), the corresponding eigenspace $E_1(A)$ is the space spanned by the vector $(1,0,0)$, a $1$-dimensional space. 

Now let us apply the above lemma to the linear operator

$$A-1I=\begin{pmatrix}0&1&1\\0&0&1\\0&0&0\end{pmatrix}$$

As mentioned, 

$$\ker (A-I)=\span \{(1,0,0)\}$$

However, carrying out calculations for higher powers,

$$(A-I)^2=\begin{pmatrix}0&0&1\\0&0&0\\0&0&0\end{pmatrix}$$

so

$$\ker(A-I)^2=\span \{(1,0,0), (0,1,0)\}$$

and

$$(A-I)^3=\begin{pmatrix}0&0&0\\0&0&0\\0&0&0\end{pmatrix}$$

so we see that

$$\ker (A-I)^3=\span \{(1,0,0), (0,1,0), (0,0,1)\}$$
:::

Though calling it intuition is perhaps a bit grandiose, at least in the case of this example we can verify that the observation mentioned above holds well. Now let us introduce the following definition for the main discussion.

::: Definition 3
On a finite-dimensional vector space $V$, given a linear operator $A$ and, for $A$, an eigenvalue $\lambda$, we define the *generalized eigenspace* of $A$ for $\lambda$ by the formula

$$G_\lambda(A)=\left\{v\in V\mid (A-\lambda I)^kv=0\text{ for some $k\geq 0$}\right\}$$
:::

Then from [Lemma 1](#lem1){: data-lid="tlklp" } we obtain the following.

::: Corollary 4
For a finite-dimensional vector space $V$, a linear operator $A:V\rightarrow V$ defined on it, and its eigenvalue $\lambda$, there exists a suitable positive integer $k$ such that $G_\lambda(A)=\ker(A-\lambda I)^k$.
:::
::: Proof
If we apply [Lemma 1](#lem1){: data-lid="9itkd" } to the linear operator $A-\lambda I$,

$$\ker(A-\lambda I)^k=\ker(A-\lambda I)^{k+1}=\cdots$$

holds for some $k$. On the other hand, whenever $v\in G_\lambda(A)$ is given, by definition the equation

$$(A-\lambda I)^lv=0$$

holds for some $l$. However, if we set $k'=\max (k,l)$, then from $k'\geq l$ we see that

$$(A-\lambda I)^{k'}v =0$$

That is, $v\in\ker (A-\lambda I)^{k'}$. But by the definition of $k$, we have $\ker(A-\lambda I)^k=\ker(A-\lambda I)^{k'}$, and from this $v\in \ker (A-\lambda I)^k$. ($k'$ depends on $v$, but $k$ does not.) Since the inclusion $\ker (A-\lambda I)^k\subseteq G_\lambda(A)$ is obvious, we obtain the desired result.
:::

Intuitively, generalized eigenspaces are spaces containing not only genuine eigenvectors, but also vectors that, under repeated application of the linear operator $(A-\lambda I)$, eventually become $0$.

## Primary Decomposition Theorem

Before introducing the main result, let us briefly summarize the proof of [§Eigenspace Decomposition, ⁋Proposition 12](/en/math/linear_algebra/eigenspace_decomposition#prop12){: data-lid="kim1o" }. To show the diagonalizability of $A$, we assumed that for a fixed eigenvalue $\lambda$ the equation

$$\ker(A-\lambda I)=\ker(A-\lambda I)^2$$

holds, and then, since by [§Eigenspace Decomposition, ⁋Lemma 11](/en/math/linear_algebra/eigenspace_decomposition#lem11){: data-lid="2pmmg" }

$$\ker (A-\lambda I)\cap \im (A-\lambda I)=\{0\}$$

we saw that $V$ can necessarily be expressed in the form $V=\ker (A-\lambda I)\oplus \im(A-\lambda I)$. Then $\im (A-\lambda I)$ becomes $A$-invariant, so we can view $A$ as a linear operator on this space, and at that time (since by [§Eigenspace Decomposition, ⁋Proposition 4](/en/math/linear_algebra/eigenspace_decomposition#prop4){: data-lid="hvvsf" }, $E_\lambda(A)\cap E_\mu(A)=\{0\}$) the eigenvalue--eigenvector pairs match up, so repeating this inductively to obtain the eigenspace decomposition was the gist of the proof.

Now, thinking about how to utilize [Definition 3](#def3){: data-lid="g9sea" } from the above perspective, we know that for an arbitrary linear operator $L$, whenever

$$\ker L^k=\ker L^{k+1}=\cdots$$

holds for $k$, the equation

$$\ker L^k=\ker L^{2k}$$

holds. In other words, for $L^k:V \rightarrow V$, the premise of [§Eigenspace Decomposition, ⁋Lemma 11](/en/math/linear_algebra/eigenspace_decomposition#lem11){: data-lid="acd14" } is satisfied. Applying this to $L=A-\lambda I$, we obtain the first step of induction---that is, the direct sum decomposition $V=\ker (A-\lambda I)^k \oplus \im (A-\lambda I)^k$. As in the proof of [§Eigenspace Decomposition, ⁋Proposition 12](/en/math/linear_algebra/eigenspace_decomposition#prop12){: data-lid="3ilra" }, let us write this as

$$V=G_\lambda(A)\oplus W_\lambda(A)$$

Then it is obvious that $W_\lambda(A)$ is $A$-invariant and therefore $A\vert_{W_\lambda(A)}$ defines a linear operator $A\vert_{W_\lambda(A)}:W_\lambda(A)\rightarrow W_\lambda(A)$. The part that requires some care is the following lemma.

::: Lemma 5
For a finite-dimensional vector space $V$, a linear operator $A:V\rightarrow V$ defined on it, and two distinct eigenvalues of $A$, $\lambda, \mu$, we have $G_\lambda(A)\cap G_\mu(A)=\{0\}$.
:::
::: Proof
First, assume that $v\in G_{\lambda}(A)\cap G_{\mu}(A)$ and $v\neq 0$. From [Corollary 4](#cor4){: data-lid="ssaoz" }, the following two equations

$$G_{\lambda}(A)=\ker(A-\lambda I)^{k},\qquad G_{\mu}(A)=\ker(A-\mu I)^{l}$$

hold for some integers $k, l$. 

Now, let the integer $p$ be, among those satisfying $(A-\lambda I)^{m}v=0$, the smallest $m$. Then from the equation

$$(A-\lambda I)^{p}v=0\implies A(A-\lambda I)^{p-1}v=\lambda(A-\lambda I)^{p-1}v$$

we see that $w=(A-\lambda I)^{p-1}v\neq 0$ is an eigenvector of $A$ corresponding to the eigenvalue $\lambda$. On the other hand, since $v\in G_{\mu}(A)$, we have $(A-\mu I)^{l}v=0$, and since $(A-\lambda I)$ and $(A-\mu I)$ commute,

$$(A-\mu I)^{l}w=(A-\mu I)^{l}(A-\lambda I)^{p-1}v=(A-\lambda I)^{p-1}(A-\mu I)^{l}v=0$$

holds. That is, since $w\in G_{\mu}(A)$, $w$ is an eigenvector corresponding to the eigenvalue $\lambda$ and at the same time a vector belonging to $G_{\mu}(A)$. 

Let us show that this is impossible. First, since $w\in G_{\mu}(A)$, by definition $(A-\mu I)^{m}w=0$ holds for some integer $m$. (For instance, we saw above that $m=l$ satisfies this.) If we let the smallest among the integers $m$ satisfying this condition be $q$, then by minimality $w'=(A-\mu I)^{q-1}w\neq 0$, and since

$$0=(A-\mu I)^{q}w=(A-\mu I)w'$$

, $w'$ is an eigenvector corresponding to the eigenvalue $\mu$. On the other hand, since $w$ is an eigenvector corresponding to the eigenvalue $\lambda$, from the equation

$$Aw'=A(A-\mu I)^{q-1}w=(A-\mu I)^{q-1}Aw=(A-\mu I)^{q-1}\lambda w=\lambda (A-\mu I)^{q-1}w=\lambda w'$$

we see that $w'$ is also an eigenvector corresponding to $\lambda$. This contradicts [§Eigenspace Decomposition, ⁋Proposition 4](/en/math/linear_algebra/eigenspace_decomposition#prop4){: data-lid="kmp8q" }, so by contradiction we see that $G_{\lambda}(A)\cap G_{\mu}(A)=\{0\}$. 
:::

Therefore, considering the preceding decomposition

$$V=G_\lambda(A)\oplus W_\lambda(A)$$

and the restricted linear operator $A\vert_{W_\lambda(A)}: W_\lambda(A)\rightarrow W_\lambda(A)$, the eigenvalues of this linear operator are precisely those eigenvalues of $A$ other than $\lambda$. Indeed, if $\mu\neq \lambda$ is an eigenvalue of $A$, then for $v\in E_\mu(A)$ we have $(A-\lambda I)^kv=(\mu-\lambda)^kv$, so $v=(A-\lambda I)^k\left((\mu-\lambda)^{-k}v\right)\in \im (A-\lambda I)^k=W_\lambda(A)$, and hence $\mu$ is an eigenvalue of $A\vert_{W_\lambda(A)}$. Furthermore, since $G_\mu(A)$ is $A$-invariant and a suitable power of $A-\mu I$ is $0$ on it, $A-\lambda I=(\mu-\lambda)I+(A-\mu I)$ is invertible on $G_\mu(A)$. Therefore, $G_\mu(A)=(A-\lambda I)^k(G_\mu(A))\subseteq\im(A-\lambda I)^k=W_\lambda(A)$, and the generalized eigenspace of $A\vert_{W_\lambda(A)}$ for $\mu$ is equal to $G_\mu(A)$. That is, induction works, and thus the following holds.

::: Theorem 6 (First Decomposition Theorem)
On a finite-dimensional vector space $V$, for a linear operator $A:V\rightarrow V$, let all eigenvalues of $A$ be $\lambda_1,\ldots,\lambda_m$. Then the following direct sum decomposition

$$V=G_{\lambda_1}(A)\oplus G_{\lambda_2}(A)\oplus\cdots\oplus G_{\lambda_m}(A)$$

holds. 
:::

## Jordan Canonical Form

Now for each $\lambda$, we need to compute the dimension of $G_\lambda(A)$. Let a linear operator $A:V \rightarrow V$ be given, and let its characteristic polynomial

$$p_A(\x)=\prod_{\lambda\in\sigma(A)}(\x-\lambda)^{d_\lambda}$$

be given. Here $d_\lambda$ is the algebraic multiplicity of $\lambda$, and $\sum d_\lambda$ equals the degree of $p_A$, which is $\dim V$. However, from the above decomposition we obtain the formula

$$p_A(\x)=\prod_{\lambda\in\sigma(A)} p_{G_\lambda(A)}(\x)$$

([§Existence and Uniqueness of the Determinant, ⁋Corollary 10](/en/math/linear_algebra/existence_and_uniqueness_of_determinant#cor10){: data-lid="z93i9" }) Since we verified in [Lemma 5](#lem5){: data-lid="nzyj6" } that when restricted to $G_\lambda(A)$, $A$ has only $\lambda$ as an eigenvalue, each $p_{G_\lambda(A)}(\x)$ must have only $\x-\lambda$ as a factor. Therefore, for the two expressions above to be equal, we know that $p_{G_\lambda(A)}(\x)$ must be a polynomial of degree exactly $d_\lambda$

$$p_{G_\lambda(A)}(\x)=(\x-\lambda)^{d_\lambda}$$

and from this we know that $\dim G_\lambda(A)=d_\lambda$. 

Thus, up to this point we have verified that for an arbitrary linear operator $A:V \rightarrow V$, the decomposition

$$V=\bigoplus_{\lambda\in\sigma(A)}G_\lambda(A)$$

holds, and furthermore, for each $\lambda$, $\dim G_\lambda(A)$ matches the dimension we expect, that is, in the characteristic polynomial of $A$, the algebraic multiplicity of $\lambda$. Then what remains for us is to find a suitable basis of $V$ and represent an arbitrary matrix in a form similar to [§Eigenspace Decomposition, ⁋Proposition 7](/en/math/linear_algebra/eigenspace_decomposition#prop7){: data-lid="kcdc1" }. 

A useful fact here is that for a linear operator $A:V\rightarrow V$ and any eigenvalue $\lambda\in \sigma(A)$, when restricted to the generalized eigenspace $G_\lambda(A)$, the linear operator

$$N_\lambda:=(A-\lambda I)\vert_{G_\lambda(A)}: G_\lambda(A)\rightarrow G_\lambda(A)$$

is a nilpotent operator. 

::: Definition 7
On a vector space $V$, a linear operator $N:V \rightarrow V$ is called *nilpotent* if there exists an integer $k$ such that $N^k=0$. The smallest such $k$ is called the *(nilpotency) index* of $N$. 
:::

That is, if we can find the canonical form of an arbitrary nilpotent operator, then we will also be able to represent the entire matrix $A$ in canonical form. 

Let an index-$k$ nilpotent operator $N: V\rightarrow V$ be given. Then there exists some $v\in V$ such that $N^{k-1}v\neq 0$. Using this vector, we can also show that the inclusions in [Lemma 1](#lem1){: data-lid="5he7w" } are strict, because $N^{k-i}v\in \ker N^i$ but $N^{k-i}v\not\in\ker N^{i-1}$. In other words, $v, Nv, \ldots, N^{k-1}v$ are all distinct elements. More generally, the following holds.

::: Lemma 8
Suppose that on a vector space $V$, a linear operator $N: V\rightarrow V$ and a vector $v$ satisfy $N^kv=0$ and $N^{k-1}v\neq 0$. Then the following vectors

$$v, \quad Nv, \quad\cdots,\quad N^{k-1}v$$

are linearly independent. 
:::
::: Proof
Assume that the following equation

$$a_0v+a_1 Nv+\cdots +a_{k-1}N^{k-1}v=0$$

holds. Applying $N^{k-1}$ to both sides, from $N^kv=0$ we know that $a_0N^{k-1}v=0$. But since $N^{k-1}v\neq 0$ by assumption, necessarily $a_0=0$, and thus

$$a_1Nv+\cdots +a_{k-1}N^{k-1}v=0$$

Applying $N^{k-2}$ to both sides again, we obtain $a_1=0$, and repeating this yields the desired result. 
:::

That is, the $k$ vectors $v, Nv, \ldots, N^{k-1}v$ form, in $V$, a basis of the $k$-dimensional subspace (a subspace of this form is called the *cyclic subspace* defined by $v$), $U$. The reason this particular basis is interesting is that if we express $N\vert_U$ as a matrix with respect to this basis $N^{k-1}v, \ldots, Nv, v$, it becomes

$$\begin{pmatrix}0&1&0&\cdots&0\\ 0&0&1&\cdots&0\\\vdots&\vdots&\vdots&\ddots&\vdots\\ 0&0&0&\cdots&1\\ 0&0&0&\cdots&0\end{pmatrix}\tag{1}$$

Our idea is to take this as the canonical form of a nilpotent operator. 

That is, given an arbitrary vector space $V$ and a nilpotent operator $N$ defined on it, our task is to represent this as a direct sum of cyclic subspaces. 

::: Theorem 9 (Cyclic Decomposition Theorem, or Second Decomposition Theorem)
For an arbitrary finite-dimensional vector space $V$ and a nilpotent operator $N: V\rightarrow V$ defined on it, there exists a decomposition into cyclic subspaces

$$V=U_1\oplus \cdots\oplus U_e$$
:::

The proof of this theorem is as follows. Let the nilpotency index of $N$ be $k_1$, and choose, such that $N^{k_1}v_1=0$ but $N^{k_1-1}v_1\neq 0$, a vector $v_1$. Consider the cyclic subspace defined by this vector:

$$U_1=\span (N^{k_1-1}v_1, \cdots, Nv_1, v_1)$$

If $U_1=V$, there is nothing more to prove. Otherwise, so that $V=U_1\oplus W_1$, we find an *$N$-invariant* subspace $W_1$. Since it is obvious that $N$ is also nilpotent on $W_1$, we can take the nilpotency index of $N\vert_{W_1}$ to be $k_2$, and such that $N^{k_2}v_2=0$ but $N^{k_2-1}v_2\neq 0$, choose a vector $v_2$. Now we obtain the following cyclic subspace again:

$$U_2=\span (N^{k_2-1}v_2, \cdots, Nv_2, v_2)$$

and by repeating the process of obtaining a complement of $U_2$ that is $N$-invariant, we obtain the desired decomposition. 

The most crucial part of this proof is that for $U$, we can choose a complement $W$ to be $N$-invariant. 

::: Lemma 10
Consider an arbitrary vector space $V$ and an index-$k$ nilpotent operator $N$ defined on it, and choose, satisfying $N^{k-1}v\neq 0$, a vector $v$. Then for the cyclic subspace generated by $v$

$$U=\span(v, Nv, \ldots, N^{k-1}v)$$

there exists, such that $V=U\oplus W$, an $N$-invariant space $W$. 
:::

The proof of this can be done by induction on the nilpotency index of $N$, but since the proof is somewhat tedious, we omit it. 

In any case, after going through this process, we know that an arbitrary nilpotent operator $N$ can be represented as a direct sum of the form (1) above (that is, block diagonal matrices with the above matrices on the diagonal). Since $N$ arose on the generalized eigenspace $G_\lambda(A)$ from the nilpotent operator $A-\lambda I$, we define the following.

::: Definition 11
The *Jordan block* of size $k$, $J_k(\lambda)$, is defined as the following $k\times k$ matrix

$$J_k(\lambda)=\begin{pmatrix}\lambda&1&0&\cdots&0\\0&\lambda&1&\cdots&0\\\vdots&\vdots&\ddots&\ddots&\vdots\\0&0&\cdots&\lambda&1\\0&0&\cdots&0&\lambda\end{pmatrix}$$
:::

Then combining [Theorem 6](#thm6){: data-lid="vro9x" } and [Theorem 9](#thm9){: data-lid="uxmzd" }, we obtain the following theorem.

::: Theorem 12 (Jordan canonical form)
For an arbitrary linear operator $A:V\rightarrow V$ defined on a finite-dimensional vector space $V$, by choosing a suitable basis of $V$, the matrix representation of $A$ takes the following form:

$$J=\begin{pmatrix}J_{k_1}(\lambda_1)&0&\cdots&0\\0&J_{k_2}(\lambda_2)&\cdots&0\\\vdots&\vdots&\ddots&\vdots\\0&0&\cdots&J_{k_m}(\lambda_m)\end{pmatrix}$$

where each $J_{k_i}(\lambda_i)$ is a Jordan block. A matrix of this form is called the *Jordan canonical form* of $A$.
:::

::: Example 13
Let us find the Jordan canonical form of the matrix

$$A=\begin{pmatrix}1&1&1\\0&1&1\\0&0&1\end{pmatrix}$$

from [Example 2](#ex2){: data-lid="yr2k6" }. The unique eigenvalue of $A$ is $\lambda=1$, and we have already computed that

$$A-I=\begin{pmatrix}0&1&1\\0&0&1\\0&0&0\end{pmatrix}$$

and

$$\ker(A-I)=\span\{(1,0,0)\},\quad \ker(A-I)^2=\span\{(1,0,0),(0,1,0)\},\quad \ker(A-I)^3=\mathbb{R}^3$$

That is, applying [Theorem 6](#thm6){: data-lid="9suiv" } to $A$ simply gives $V=G_1(A)$. 

Now we need to apply [Theorem 9](#thm9){: data-lid="2ab5v" } on $G_1(A)$. As seen earlier, $(A-I)^3=0$ but $(A-I)^2\neq 0$, and we know that $v=(0,0,1)$ actually satisfies $(A-I)^2 v\neq 0$. Then

$$v_1=(A-I)^2v=(1,0,0),\qquad v_2=(A-I)v=(1,1,0),\qquad v_3=v=(0,0,1)$$

and these span $G_1(A)$. Now taking $\mathcal{B}=(v_1, v_2, v_3)$ as a basis of $V$ and representing $A$:

$$Av_1 = A\begin{pmatrix}1\\0\\0\end{pmatrix} = \begin{pmatrix}1\\0\\0\end{pmatrix} = v_1$$

$$Av_2 = A\begin{pmatrix}1\\1\\0\end{pmatrix} = \begin{pmatrix}2\\1\\0\end{pmatrix} = v_1 + v_2$$

$$Av_3 = A\begin{pmatrix}0\\0\\1\end{pmatrix} = \begin{pmatrix}1\\1\\1\end{pmatrix} = v_2 + v_3$$

Therefore, the matrix representation of $A$ with respect to the basis $\mathcal{B}$ is

$$[A]_{\mathcal{B}} = \begin{pmatrix}1&1&0\\0&1&1\\0&0&1\end{pmatrix} = J_3(1)$$

yielding a Jordan canonical form consisting of a single Jordan block of size 3.
:::

The uniqueness of the Jordan canonical form follows from the fact that the sizes of the Jordan blocks are determined by $\dim\ker N^k-\dim\ker N^{k-1}$. Since this is independent of the choice of basis, the Jordan canonical form is uniquely determined up to the order of the Jordan blocks.

## Rational Canonical Form

The Jordan canonical form directly contains the eigenvalue $\lambda$ in each block and therefore depends on the assumption that $\mathbb{K}$ is algebraically closed. There is a canonical form that encodes the same information without explicitly specifying eigenvalues, using only the coefficients of polynomials; its basic unit is the companion matrix.

::: Definition 14
For a monic polynomial $p(\x)=\x^d+c_{d-1}\x^{d-1}+\cdots+c_1\x+c_0$, its *companion matrix* $C(p)$ is defined as the following $d\times d$ matrix:

$$C(p)=\begin{pmatrix}0&0&\cdots&0&-c_0\\1&0&\cdots&0&-c_1\\0&1&\cdots&0&-c_2\\\vdots&\vdots&\ddots&\vdots&\vdots\\0&0&\cdots&1&-c_{d-1}\end{pmatrix}$$
:::

An operator $T:V\rightarrow V$ is said to be *cyclic* if there exists a suitable $v\in V$ such that $\{v,Tv,\ldots,T^{d-1}v\}$ ($d=\dim V$) is a basis of $V$; such a $v$ is called a cyclic vector.

::: Proposition 15
With a cyclic vector $v$, a dimension $d$ operator $T:V\rightarrow V$ has minimal polynomial $p$ of degree $d$, and with respect to the cyclic basis $\{v,Tv,\ldots,T^{d-1}v\}$, the matrix representation of $T$ is $C(p)$. In particular, the Jordan block $J_k(\lambda)$ of [Definition 11](#def11){: data-lid="dxeiz" } is similar to the companion matrix of $(\x-\lambda)^k$.
:::
::: Proof
Since $\{v,Tv,\ldots,T^{d-1}v\}$ is linearly independent, expressing $T^dv$ as their linear combination

$$T^dv=-(c_0v+c_1Tv+\cdots+c_{d-1}T^{d-1}v)$$

and defining $p(\x)=\x^d+c_{d-1}\x^{d-1}+\cdots+c_0$ with these coefficients, we have $p(T)v=0$. Then for arbitrary $T^iv$, we have $p(T)T^iv=T^ip(T)v=0$, and since these generate $V$, $p(T)=0$. On the other hand, for a polynomial of degree less than $d$ that is not $0$, $q$, since $q(T)v$ is a nontrivial linear combination of $\{v,\ldots,T^{d-1}v\}$, it is not $0$; therefore $p$ is the minimal polynomial of $T$. In this basis, $T$ acts as $T^iv\mapsto T^{i+1}v$ ($i<d-1$), and $T^{d-1}v$ acts by the above formula, so its matrix representation is exactly $C(p)$.

In the case of $J_k(\lambda)$, since $N=J_k(\lambda)-\lambda I$ is a nilpotent of index $k$, choosing a vector with $N^{k-1}v\neq 0$, say $v$, by [Lemma 8](#lem8){: data-lid="04k8g" }, $\{v,Nv,\ldots,N^{k-1}v\}$ is a basis. Since $J_k(\lambda)=\lambda I+N$, $\{v,J_k(\lambda)v,\ldots,J_k(\lambda)^{k-1}v\}$ also generates the same space, so $v$ is a cyclic vector, and since the minimal polynomial of $J_k(\lambda)$ is $(\x-\lambda)^k$, by the above result $J_k(\lambda)$ is similar to the companion matrix of $(\x-\lambda)^k$.
:::

That these do not actually become the same matrix is because the two bases are taken as powers of different operators. While the basis giving the companion matrix of [Definition 14](#def14){: data-lid="pjzpy" } is $\{v, Tv, \ldots, T^{d-1}v\}$, the basis giving the Jordan block is, with respect to $N=T-\lambda I$, $\{N^{k-1}v, \ldots, Nv, v\}$, and the only case explained by a difference in ordering convention is when $\lambda=0$, so that the two become the same basis in reverse order. However, both of these canonical forms are deeply rooted, and aligning either one with the other would break this standard, so we settle for only such a brief remark. Then, more generally, we obtain the following.

::: Theorem 16 (Rational Canonical Form)
For an arbitrary linear operator $A$ defined on a finite-dimensional vector space over an algebraically closed field, by choosing a suitable basis of $V$, the matrix representation of $A$ becomes a block diagonal of companion matrices

$$\begin{pmatrix}C(p_1)&&\\&\ddots&\\&&C(p_r)\end{pmatrix},\qquad p_i=(\x-\lambda_i)^{k_i}$$

where each $(\x-\lambda_i)^{k_i}$ is the *elementary divisor* corresponding to $A$'s Jordan block $J_{k_i}(\lambda_i)$.
:::
::: Proof
By [Theorem 12](#thm12){: data-lid="l7u21" }, $A$ is similar to a direct sum of Jordan blocks $J_{k_i}(\lambda_i)$, and by [Proposition 15](#prop15){: data-lid="lviva" }, each $J_{k_i}(\lambda_i)$ is similar to $C((\x-\lambda_i)^{k_i})$, so collecting these gives the desired block diagonal form.
:::

Needless to say, the true usefulness of the rational canonical form lies in the fact that it can be applied even when $\mathbb{K}$ is <em>not</em> algebraically closed. In keeping with the flow of the exposition, the proof above used the Jordan form to obtain the companion form of the elementary divisors $(\x-\lambda_i)^{k_i}$, but even when eigenvalues do not exist in $\mathbb{K}$, an arbitrary operator is standardized into companion matrices of *invariant factors* $p_1\mid p_2\mid\cdots\mid p_r$ ($p_r$ being the minimal polynomial) through the irreducible factorization of the minimal polynomial and cyclic decomposition. This general form follows from the structure theorem for $\mathbb{K}[\x]$-modules, and gives a canonical form defined entirely over $\mathbb{K}$ without mentioning eigenvalues at all.

---

**References**

**[Goc]** M.S. Gockenbach, *Finite-dimensional linear algebra*, Discrete Mathematics and its applications, Taylor&Francis, 2011.  
**[Lee]** 이인석, *선형대수와 군*, 서울대학교 출판문화원, 2005.

---

[^1]: That for $U_1$, the complement $W_1$ can be made $N$-invariant is the most nontrivial part of this proof, and this must be shown directly by induction.
