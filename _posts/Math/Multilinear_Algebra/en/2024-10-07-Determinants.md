---
title: "Determinants"
description: "We define the determinant on a free module and prove its basic properties. We cover the multiplication formula, invertibility, and its relationship with the invertibility of linear maps on free modules with a finite basis."
excerpt: "Determinant of an endomorphism of a free module and its basic properties"

categories: [Math / Multilinear Algebra]
permalink: /en/math/multilinear_algebra/determinants
sidebar: 
    nav: "multilinear_algebra-en"

date: 2024-10-07
weight: 11
translated_at: 2026-06-01T18:30:06+00:00
translation_source: kimi-cli
last_polished_at: 2026-10-24T15:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
## Determinant

In the previous post, we verified that for any free $A$-module $M$, if $M$ has a basis $(e_i)_{i\in I}$, then the elements $e_J$ of the form

$$e_J=e_{j_1}\wedge e_{j_2}\wedge\cdots\wedge e_{j_k},\qquad j_1<\cdots < j_k, \quad J=\{j_1,\ldots, j_k\}$$

constitute a basis of $\bigwedge(M)$. ([§Tensor Algebra, ⁋Proposition 13](/en/math/multilinear_algebra/tensor_algebras#prop13){: data-lid="2tgfs" }) In particular, if we collect the subsets satisfying $\lvert J\rvert=n$, these $J$ form a basis of $\bigwedge^n(M)$.

Now suppose $M$ has a finite basis $e_1,\ldots, e_n$. Then the basis of $\bigwedge^n(M)$ consists of only the single element $e_1\wedge\cdots\wedge e_n$. On the other hand, for any $u\in\End_\rMod{A}(M)$, the functoriality of $\bigwedge$ induces $\bigwedge^n(u):\bigwedge^n(M)\rightarrow\bigwedge^n(M)$, and from the discussion above, this linear map must be written in the form $x\mapsto \alpha x$.

::: Definition 1
Suppose a free $A$-module $M$ has a finite basis $e_1,\ldots, e_n$. Then for any $u\in\End_\rMod{A}(M)$, the element $\alpha\in A$ obtained from the discussion above is called the *determinant* of $u$ and is denoted $\det u$.
:::

Then the following proposition is immediate from the definition.

::: Proposition 2
The following hold.

1. For any $u,v\in\End_\rMod{A}(M)$, we have $\det(u\circ v)=(\det u)(\det v)$.
2. $\det(\id_M)=1$.
3. For any $u\in\Aut_\rMod{A}(M)$, $\det u$ has a multiplicative inverse in $A$, and its value is equal to $\det(u)^{-1}=\det(u^{-1})$.
:::

::: Corollary 3
For a finite-dimensional free $A$-module $M$ and $u\in\End_\rMod{A}(M)$, the following are equivalent.

1. $u$ is bijective.
2. $\det u$ is invertible in $A$.
:::
::: Proof
It suffices to assume condition 2 and show condition 1. For this, define $x_i=u(e_i)$ to obtain

$$x_1\wedge \cdots\wedge x_n=\det(u) e_1\wedge\cdots\wedge e_n$$

and then multiply both sides by $\det(u)^{-1}$ and consider the change of basis obtained from that equation.
:::

If we fix a free $A$-module $M$ and its basis $e_1,\ldots, e_n$, then for any elements of $M$, $x_1,\ldots, x_n$, there exists $\alpha$ such that

$$x_1\wedge \cdots\wedge x_n=\alpha e_1\wedge\cdots\wedge e_n$$

and we write this as $\det(x_1,\ldots, x_n)$. To actually compute this value, one expresses each $x_i$ as a linear combination of $e_1,\ldots, e_n$ and then simplifies everything using $e_i\wedge e_i=0$ and $e_i\wedge e_j=-e_j\wedge e_i$. In the case $A=\mathbb{K}$, this was already examined in [\[Linear Algebra\] §Existence and Uniqueness of the Determinant](/en/math/linear_algebra/existence_and_uniqueness_of_determinant#lem2){: data-lid="15kx7" }. To explain in a little more detail, when any $X\in\Mat_n(A)$ is written using column vectors as $X=(x_1,\ldots, x_n)$, then for the unique endomorphism satisfying $u(e_i)=x_i$, $u\in\End_\rMod{A}(M)$, $\det(u)$ is well-defined, and comparing this with the formula from the proof of [Corollary 3](#cor3){: data-lid="drqhn" }, we have $\det (x_1,\ldots, x_n)=\det(u)$. From this, one can formulate a matrix version of [Proposition 2](#prop2){: data-lid="ovhgw" }, and the process of computing it is precisely [\[Linear Algebra\] §Existence and Uniqueness of the Determinant](/en/math/linear_algebra/existence_and_uniqueness_of_determinant#lem2){: data-lid="5o46g" }. In particular, from this we see that $\det(u^\ast)=\det(u)$.

## Minors of a Matrix

Meanwhile, among the methods for computing determinants, there was [\[Linear Algebra\] §Existence and Uniqueness of the Determinant, ⁋Theorem 12](/en/math/linear_algebra/existence_and_uniqueness_of_determinant#thm12){: data-lid="kgoj2" } using Laplace expansion; we will not repeat this computation itself as it has already been covered, but we can generalize the $\det A^{(i,j)}$ that appeared there.

To this end, suppose an arbitrary $X=(\xi_{ij})\in\Mat_{I\times J}$ is given. If we fix a total ordering defined on $I$ and $J$, then whenever finite subsets $H\subseteq I$ and $K\subseteq J$ are given, a total order is also given to the indices of the submatrix $X_{H,K}=(\xi_{i,j})_{i\in H,j\in K}$ formed by them. In particular, consider the case where $\lvert H\rvert=\lvert K\rvert$. Then the following lemma is obvious.

::: Lemma 4
Suppose a free $A$-module $M$ is given with a basis $(e_i)_{i\in I}$, and fix a total ordering on $I$. Also, for any natural number $p$, consider the basis of $\bigwedge^p(M)$

$$(e_J=e_{j_1}\wedge\cdots\wedge e_{j_p})_{\lvert J\rvert=p}$$

In $M$, given any $p$ elements $x_1,\ldots, x_p$, write them in the form

$$x_j=\sum_{i\in I} \xi_{ij}e_i$$

and define the matrix $X=(\xi_{ij})_{(i,j)\in I\times p}\in\Mat_{I\times p}(A)$. Then the formula

$$x_1\wedge x_2\wedge\cdots\wedge x_p=\sum_{\lvert J\rvert=p}\det X_{J,\{1,\ldots, p\}}e_J$$

holds.
:::

::: Proposition 5
Suppose two free $A$-modules $M,N$ and their finite bases $(e_i)_{1\leq i\leq m}$, $(f_j)_{1\leq j\leq n}$ are respectively given, and let the matrix representation of an $A$-linear map $u:M\rightarrow N$ with respect to these bases be $X$. Now, for any natural number less than or equal to $\min(m,n)$, denoted by $p$, the matrix representation of $\bigwedge^p(u):\bigwedge^p(M) \rightarrow\bigwedge^p(N)$ with respect to the bases $(e_I)_{\lvert I\rvert=p}$ and $(f_J)_{\lvert J\rvert=p}$ is given by $(\det(X_{J,I}))$.
:::
::: Proof
In the given situation, arrange the elements of $I$ in increasing order as $i_1<\cdots< i_p$. Then by the definition of $\bigwedge^p(u)$,

$${\bigwedge}^p(u)(e_I)=u(e_{i_1})\wedge\cdots\wedge u(e_{i_p})$$

so it suffices to apply the preceding lemma.
:::

::: Corollary 6
Suppose a free $A$-module $M$ has a finite basis $(e_i)_{1\leq i\leq n}$. Then for any $u\in\End_\rMod{A}(M)$ and $\alpha,\beta\in A$, we obtain the following formula:

$$\det(\alpha\cdot\id_M+\beta u)=\sum_{k=0}^n\tr\left({\bigwedge}^k(u)\right)\alpha^{n-k}\beta^k$$
:::
::: Proof
The left-hand side arises from reducing the following wedge product:

$$(\alpha e_1+\beta u(e_1))\wedge\cdots\wedge(\alpha e_n+\beta u(e_n))$$

to a multiple of $e_1\wedge\cdots\wedge e_n$. Expanding the above expression completely, this is equal to the sum obtained by: for an integer satisfying $0\leq p\leq n$, $p$, a subset satisfying $\lvert P\rvert=p$ of $\{1,\ldots, n\}$, $P$, and the formula

$$x_i=\begin{cases}u(e_i)&\text{if $i\in P$}\\e_i&\text{otherwise}\end{cases}$$

defining the elements $x_i$, for the element of $\bigwedge^n(M)$ defined by $x_P=x_1\wedge\cdots\wedge x_n$, summing all the terms $\alpha^{n-p}\beta^p x_P$.

To simplify $x_P$ of the above form, let $\{1,\ldots, n\}\setminus P=Q$, and arrange the elements of $P,Q$ respectively in increasing order as

$$P=\{i_1< i_2<\cdots< i_p\},\qquad Q=\{j_1< j_2<\cdots < j_{n-p}\}$$

Then, reordering the elements of $P$ and the elements of $Q$ respectively, we can write

$$x_P=\gamma_{P,Q}e_{j_1}\wedge\cdots\wedge e_{j_{n-p}}\wedge u(e_{i_1})\wedge\cdots\wedge u(e_{i_p})$$

Here $\gamma_{P,Q}$ is the sign arising from reordering them, given concretely by the following formula:

$$\gamma_{P,Q}=(-1)^{\lvert S\rvert},\qquad S=\{(i,j)\in P\times Q\mid i< j\}$$

Then by the definition of $X$ and [Lemma 4](#lem4){: data-lid="vgovz" }, since

$$u(e_{i_1})\wedge\cdots\wedge u(e_{i_p})=\sum_{\lvert I\rvert=p}\det(X_{I,P})e_I$$

substituting this yields

$$x_P=\gamma_{P,Q}\sum_{\lvert I\rvert=p}\det X_{I,P} e_Q\wedge e_I$$

However, since $\lvert I\rvert=p$ and $\lvert Q\rvert=n-p$, unless $I=P$ they always share an overlapping $e_i$, and therefore the above expression can be written as

$$x_P=\det (X_{P,P} )e_1\wedge e_2\wedge\cdots\wedge e_n$$

By [Proposition 5](#prop5){: data-lid="j25m6" }, for a fixed $p$, the sum over all subsets satisfying $\lvert P\rvert=p$, $P$, of $\det(X_{P,P})$ is $\tr\left(\bigwedge^p(u)\right)$, and thus the proof is complete.
:::

In particular, setting $\alpha=\beta=1$ yields $\tr(\bigwedge(u))=\det(\id_M+u)$.

## Characteristic Polynomial

We now define the characteristic polynomial.

Considering the polynomial algebra $A[\x]$ and the canonical inclusion $\iota: A \hookrightarrow A[\x]$, through extension of scalars, on $\iota_!M=A[\x]\otimes_A M$ an $A[\x]$-module structure is defined. ([\[Algebraic Structures\] §Change of Scalars, ⁋Definition 3](/en/math/algebraic_structures/change_of_base_ring#def3){: data-lid="qq5fc" }) Moreover, whenever any $u\in\End_\rMod{A}(M)$ is given, $\iota_!u\in\End_\rMod{A[\x]}(\iota_!M)$ is also defined.

For any $u\in\End_\rMod{A}(M)$, let us introduce the notation

$$u^k=\underbrace{u\circ\cdots\circ u}_\text{$k$ times}$$

Then for any $p\in A[\x]$, we can regard $p(u)$ as an element of $\End_\rMod{A}(M)$, and in this case, for any $p,q\in A[\x]$,

$$(pq)(u)=p(u)\circ q(u)=q(u)\circ p(u)$$

holds. Therefore, defining on $M$ an $A[\x]$-action by the following formula:

$$p\bullet x=p(u)(x)$$

endows $M$ with an $A[\x]$-module structure. That is, by the scalar multiplication just defined,

$$\rho: A[\x]\otimes_A M \rightarrow M;\qquad p\otimes_A x\mapsto p\bullet x\tag{1}$$

is defined, and this is $A$-linear. Moreover, $\rho$ is an $A[\x]$-linear map. This is because for any $p\in A[\x]$ and $q\otimes x\in \iota_!M$,

$$\rho(p(q\otimes_Ax))=\rho((pq)\otimes_Ax)=(pq)\bullet x=(pq)(u)(x)=p(u)(q(u)x)=p\bullet\rho(q\otimes_Ax)$$

holds.

To avoid confusion, let us denote $M$, regarded as an $A[\x]$-module, by $M_u$. Now viewing $u$ as a function from $M_u$ to $M_u$, the formula

$$u(p\bullet x)=u(p(u)(x))=(\x p)\bullet x=(p\x)\bullet x=p\bullet(u(x))$$

holds, so $u$ becomes an $A[\x]$-module endomorphism. Then from the above formula and (1), we know that

$$\rho\circ(\iota_!u)=u\circ\rho$$

holds.

::: Proposition 7
In the above situation, define the $A[\x]$-endomorphism $\psi=\x-\iota_!u$ by the formula

$$\psi(p\otimes_Ax)=(\x p)\otimes_Ax -p\otimes_A u(x)$$

Then the following sequence of $A[\x]$-modules

$$\iota_!M\overset{\psi}{\rightarrow}\iota_!M\overset{\rho}{\rightarrow}M_u\rightarrow 0$$

is exact.
:::
::: Proof
It suffices to show that $\ker\rho\subseteq \im\psi$. Let $z\in\ker\rho$ be arbitrary. Then by decomposing $z$ into a sum of elements of the form $p\otimes_A x$, further decomposing the $p$'s into linear combinations of $1,\x,\x^2,\ldots$, and rewriting the sum according to the $\x^k$'s, we can write

$$z=\sum_k \x^k\otimes_A x_k,\qquad x_k\in M$$

Then from the condition $z\in\ker\rho$, we obtain

$$\rho(z)=\sum_k u^k(x_k)=0$$

Now since $\sum 1\otimes u^k(x_k)=0$, from this we obtain

$$z=\sum_k (\x^k\otimes_A x_k-1\otimes_A u^k(x_k))=\sum_k (\x^k-\iota_!u^k)(1\otimes x_k)$$

and since in $\iota_!M=A[\x]\otimes_A M$ the element $\x$ acts on the $A[\x]$ part and $\iota_!u$ acts on $M$, their multiplications commute. That is, the above expression can be written as

$$\sum_k (\x-\iota_!u)\circ\left(\sum_{j=0}^{k-1} \x^j (\iota_!u)^{k-j-1}\right)(1\otimes_A x_k)$$

which completes the proof.
:::

On the other hand, considering the determinant of $\psi$, from [Corollary 6](#cor6){: data-lid="xhn59" } we obtain

$$\det (\x-\iota_!u)=\sum_{k=0}^n (-1)^k\tr\left({\bigwedge}^k(\iota_!u)\right)\x^{n-k}$$

Meanwhile, since $u$'s matrix representation $[u]_\mathcal{B}^\mathcal{B}$ is equal, with respect to $\iota_!M$'s $A[\x]$-basis $\mathcal{B}'=(1\otimes e_i)_{1\leq i\leq n}$, to $\iota_!u$'s matrix representation $[\iota_!u]_{\mathcal{B}'}^{\mathcal{B}'}$, the above formula can be written as

$$\det (\x-\iota_!u)=\sum_{k=0}^n (-1)^k\tr\left({\bigwedge}^k(u)\right)\x^{n-k}$$

::: Definition 8
The polynomial $\det(\x-\iota_!u)$ defined above is called the *characteristic polynomial* of $u$ and is denoted by $\chi_u(\x)$.
:::

Then from the preceding formula, we see that in the characteristic polynomial the coefficient of $\x^n$ is $1$, the coefficient of $\x^{n-1}$ is $-\tr(u)$, and the constant term is $(-1)^n\det(u)$.

::: Proposition 9 (Cayley-Hamilton)
$\chi_u(u)=0$.
:::
::: Proof
What we must show is that for any $x\in M$, $\chi_u(u)(x)=0$. Meanwhile, using equation (1), $\chi_u(u)(x)$ is equal to $\rho(\chi_u(\x)\otimes_Ax)$. Now, we have

$$\chi_u(\x)\otimes_Ax=\chi_u(\x)(1\otimes_Ax)=\det(\x-\iota_!u)(1\otimes_Ax)$$

However, considering the Laplace expansion, for any matrix $X$ and $X$'s cofactor $Y$ we have $XY^t=(\det X)I$; hence there exists a suitable $v\in\End_\rMod{A[\x]}(\iota_!M)$ such that we can write

$$\det(\x-\iota_!u)(1\otimes_Ax)=(\x-\iota_!u)(v(1\otimes_A x))$$

and therefore we obtain the desired result by [Proposition 7](#prop7){: data-lid="6lztw" }.
:::

---

**References**

**[Bou]** Bourbaki, N. Algebra I. *Elements of Mathematics*. Springer. 1998.
