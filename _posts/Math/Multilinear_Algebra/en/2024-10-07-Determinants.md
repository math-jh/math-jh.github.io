---
title: "Determinants"
description: "We define the determinant over a free commutative group and prove its basic properties. We cover the multiplicative formula, invertibility, and the relationship with the invertibility of linear maps on finite-dimensional free commutative groups."
excerpt: "The determinant of an endomorphism of a free module and its basic properties"

categories: [Math / Multilinear Algebra]
permalink: /en/math/multilinear_algebra/determinants
sidebar: 
    nav: "multilinear_algebra-en"

date: 2024-10-07
weight: 11
translated_at: 2026-06-01T18:30:06+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-01T18:30:06+00:00
---
## Determinant

In the previous post, we verified that for any free $$A$$-module $$M$$ with a basis $$(e_i)_{i\in I}$$, the elements $$e_J$$ of the form

$$e_J=e_{j_1}\wedge e_{j_2}\wedge\cdots\wedge e_{j_k},\qquad j_1<\cdots < j_k, \quad J=\{j_1,\ldots, j_k\}$$

constitute a basis of $$\bigwedge(M)$$. In particular, collecting all $$J$$ with $$\lvert J\rvert=n$$ yields a basis of $$\bigwedge^n(M)$$.

Now suppose $$M$$ has a finite basis $$e_1,\ldots, e_n$$. Then $$\bigwedge^n(M)$$ has a basis consisting of the single element $$e_1\wedge\cdots\wedge e_n$$. On the other hand, for any $$u\in\End_\rMod{A}(M)$$, the functoriality of $$\bigwedge$$ induces $$\bigwedge^n(u):\bigwedge^n(M)\rightarrow\bigwedge^n(M)$$, and by the discussion above this linear map must be of the form $$x\mapsto \alpha x$$.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> Suppose a free $$A$$-module $$M$$ has a basis $$(e_i)_{i\in I}$$. Then for any $$u:M \rightarrow M$$, the scalar $$\alpha\in A$$ obtained from the above discussion is called the *determinant* of $$u$$ and is denoted $$\det u$$.

</div>

The following proposition is then immediate from the definition.

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> The following hold.

1. For any $$u,v\in\End_\rMod{A}(M)$$, we have $$\det(u\circ v)=(\det u)(\det v)$$.
2. $$\det(\id_M)=1$$.
3. For any $$u\in\Aut_\rMod{A}(M)$$, the element $$\det u$$ is invertible in $$A$$ and satisfies $$\det(u)^{-1}=\det(u^{-1})$$.

</div>

<div class="proposition" markdown="1">

<ins id="cor3">**Corollary 3**</ins> For a finite free $$A$$-module $$M$$ and $$u\in\End_\rMod{A}(M)$$, the following are equivalent.

1. $$u$$ is bijective.
2. $$\det u$$ is invertible in $$A$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

It suffices to show that condition 2 implies condition 1. To do this, define $$x_i=u(e_i)$$ to obtain

$$x_1\wedge \cdots\wedge x_n=\det(u) e_1\wedge\cdots\wedge e_n,$$

then multiply both sides by $$\det(u)^{-1}$$ and consider the change of basis arising from this equation.

</details>

Fixing a free $$A$$-module $$M$$ and its basis $$e_1,\ldots, e_n$$, for any elements $$x_1,\ldots, x_n$$ of $$M$$ there exists a scalar $$\alpha$$ such that

$$x_1\wedge \cdots\wedge x_n=\alpha e_1\wedge\cdots\wedge e_n,$$

and we write this as $$\det(x_1,\ldots, x_n)$$. To compute this value explicitly, one expresses each $$x_i$$ as a linear combination of $$e_1,\ldots, e_n$$ and then simplifies using $$e_i\wedge e_i=0$$ and $$e_i\wedge e_j=-e_j\wedge e_i$$. In the case $$A=\mathbb{K}$$, this was already examined in [\[Linear Algebra\] §Existence and Uniqueness of the Determinant](/en/math/linear_algebra/existence_and_uniqueness_of_determinant#lem2). More precisely, for any $$X\in\Mat_n(A)$$, writing $$X=(x_1,\ldots, x_n)$$ using column vectors, there is a unique $$u\in\End_\rMod{A}(M)$$ satisfying $$u(e_i)=x_i$$, and $$\det(u)$$ is well-defined; comparing this with the expression appearing in the proof of [Corollary 3](#cor3), we see that $$\det (x_1,\ldots, x_n)=\det(u)$$. From this we obtain a matrix version of [Proposition 2](#prop2), and the process of computing it is exactly [\[Linear Algebra\] §Existence and Uniqueness of the Determinant](/en/math/linear_algebra/existence_and_uniqueness_of_determinant#lem2). In particular, we obtain $$\det(u^\ast)=\det(u)$$.

## Minors of a Matrix

Among methods for computing determinants, there is Laplace expansion, which was discussed in [\[Linear Algebra\] §Existence and Uniqueness of the Determinant, ⁋Theorem 12](/en/math/linear_algebra/existence_and_uniqueness_of_determinant#thm12). We will not repeat that computation since it was already covered, but we can generalize the $$\det A^{(i,j)}$$ that appeared there.

To this end, suppose we are given an arbitrary $$X=(\xi_{ij})\in\Mat_{I\times J}$$. Fixing a total ordering on $$I$$ and $$J$$, whenever finite subsets $$H\subseteq I$$ and $$K\subseteq J$$ are given, the submatrix $$X_{H,K}=(\xi_{i,j})_{i\in H,j\in K}$$ also inherits a total order on its indices. In particular, consider the case where $$\lvert H\rvert=\lvert K\rvert$$. Then the following lemma is obvious.

<div class="proposition" markdown="1">

<ins id="lem4">**Lemma 4**</ins> Suppose a basis $$(e_i)_{i\in I}$$ of a free $$A$$-module $$M$$ is given, and fix a total ordering on $$I$$. Also, for any natural number $$p$$, consider the basis of $$\bigwedge^p(M)$$

$$(e_J=e_{j_1}\wedge\cdots\wedge e_{j_p})_{\lvert J\rvert=p}.$$

Given any $$p$$ elements $$x_1,\ldots, x_p$$ of $$M$$, write them in the form

$$x_j=\sum_{i\in I} \xi_{ij}e_i$$

and define the matrix $$X=(\xi_{ij})_{(i,j)\in I\times p}\in\Mat_{I\times p}(A)$$. Then the formula

$$x_1\wedge x_2\wedge\cdots\wedge x_p=\sum_{\lvert J\rvert=p}\det X_{I,J}e_J$$

holds.

</div>

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> Suppose two free $$A$$-modules $$M,N$$ and their finite bases $$(e_i)_{1\leq i\leq m}$$, $$(f_j)_{1\leq j\leq n}$$ are respectively given. Now for a natural number $$p$$ less than $$\min(m,n)$$, the matrix representation of $$\bigwedge^p(u):\bigwedge^p(M) \rightarrow\bigwedge^p(N)$$ with respect to the bases $$(e_I)_{\lvert I\rvert=p}$$ and $$(f_J)_{\lvert J\rvert=p}$$ is given by $$(\det(X_{J,I}))$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

In the given situation, arrange the elements of $$I$$ in increasing order as $$i_1<\cdots< i_p$$. Then by the definition of $$\bigwedge^p(u)$$,

$${\bigwedge}^p(u)=u(e_{i_1})\wedge\cdots\wedge u(e_{i_p}),$$

so it suffices to apply the preceding lemma.

</details>

<div class="proposition" markdown="1">

<ins id="cor6">**Corollary 6**</ins> Suppose a free $$A$$-module $$M$$ has a finite basis $$(e_i)_{1\leq i\leq n}$$. Then for any $$u\in\End_\rMod{A}(M)$$ and $$\alpha,\beta\in A$$ we obtain the formula

$$\det(\alpha\cdot\id_M+\beta u)=\sum_{k\geq 0}\tr\left({\bigwedge}^k(u)\right)\alpha^{n-k}\beta^k.$$

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

The left-hand side arises from expressing the wedge product

$$(\alpha e_1+\beta u(e_1))\wedge\cdots\wedge(\alpha e_n+\beta u(e_n))$$

as a multiple of $$e_1\wedge\cdots\wedge e_n$$. Expanding the above expression completely, it equals the sum of the terms $$\alpha^{n-p}\beta^p x_P$$ over integers $$p$$ with $$0\leq p\leq n$$ and subsets $$P\subseteq\{1,\ldots, n\}$$ with $$\lvert P\rvert=p$$, where $$x_P=x_1\wedge\cdots\wedge x_n$$ is the element of $$\bigwedge^n(M)$$ defined by

$$x_i=\begin{cases}u(e_i)&\text{if $i\in P$}\\e_i&\text{otherwise.}\end{cases}$$

To simplify $$x_P$$ of the above form, put $$\{1,\ldots, n\}\setminus P=Q$$ and arrange the elements of $$P$$ and $$Q$$ in increasing order as

$$P=\{i_1< i_2<\cdots< i_p\},\qquad Q=\{j_1< j_2<\cdots < j_{n-p}\}.$$

Then by reordering the factors we can write

$$x_P=\gamma_{P,Q}e_{j_1}\wedge\cdots\wedge e_{j_{n-p}}\wedge u(e_{i_1})\wedge\cdots u(e_{i_{n-p}}).$$

Here $$\gamma_{P,Q}$$ is the sign arising from this reordering, given concretely by the formula

$$\gamma_{P,Q}=(-1)^{\lvert A\rvert},\qquad A=\{(p,q)\in P\times Q\mid p>q\}.$$

Then by the definition of $$X$$ and [Lemma 4](#lem4),

$$u(e_{i_1})\wedge\cdots\wedge u(e_{i_p})=\sum_{\lvert I\rvert=p}\det(X_{I,Q})e_Q,$$

and substituting this gives

$$x_P=\gamma_{P,Q}\sum_{\lvert I\rvert=p}\det X_{I,P} e_Q\wedge e_I.$$

However, since $$\lvert I\rvert=p$$ and $$\lvert Q\rvert=n-p$$, unless $$I=P$$ they always share a common $$e_i$$, and therefore the above expression reduces to

$$x_P=\det (X_{P,P} )e_1\wedge e_2\wedge\cdots\wedge e_n.$$

By [Proposition 5](#prop5), for a fixed $$p$$, the sum of $$\det(X_{p,p})$$ over all $$P$$ satisfying $$\lvert P\rvert=p$$ equals $$\tr\left(\bigwedge^k(u)\right)$$, and thus the proof is complete.

</details>

In particular, setting $$\alpha=\beta=1$$ gives $$\tr(\bigwedge(u))=\det(\id_M+u)$$.

## Characteristic Polynomial

We now define the characteristic polynomial.

Consider the polynomial algebra $$A[\x]$$ and the canonical inclusion $$\iota: A \hookrightarrow A[\x]$$. By extension of scalars, this defines an $$A[\x]$$-module structure on $$\iota_!M=A[\x]\otimes_A M$$. ([\[Algebraic Structures\] §Change of Base Ring, ⁋Definition 3](/en/math/algebraic_structures/change_of_base_ring#def3)) Moreover, whenever $$u\in\End_\rMod{A}(M)$$ is given, $$\iota_!u\in\End_\rMod{A[\x]}(\iota_!M)$$ is also defined.

For any $$u\in\End_\rMod{A}(M)$$, let us introduce the notation

$$u^k=\underbrace{u\circ\cdots\circ u}_\text{$k$ times}.$$

Then for any $$p\in A[\x]$$ we can regard $$p(u)$$ as an element of $$\End_\rMod{A}(M)$$, and in this case for any $$p,q\in A[\x]$$ we have

$$(pq)(u)=p(u)\circ q(u)=q(u)\circ p(u).$$

Therefore, defining an $$A[\x]$$-action on $$M$$ by the formula

$$p\bullet x=p(u)(x)$$

gives $$M$$ an $$A[\x]$$-module structure. That is, via the scalar multiplication just defined,

$$\rho: A[\x]\otimes_A M \rightarrow M;\qquad p\otimes_A x\mapsto p\bullet x\tag{1}$$

is defined and is $$A$$-linear. Moreover, $$\rho$$ is an $$A[\x]$$-linear map, because for any $$p\in A[\x]$$ and $$q\otimes x\in \iota_!M$$,

$$\rho(p(q\otimes_Ax))=\rho((pq)\otimes_Ax)=(pq)\bullet x=(pq)(u)(x)=p(u)(q(u)x)=p\bullet\rho(q\otimes_Ax).$$

To avoid confusion, let us write $$M_u$$ for $$M$$ regarded as an $$A[\x]$$-module. Now viewing $$u$$ as a map from $$M_u$$ to $$M_u$$, the formula

$$u(p\bullet x)=u(p(u)(x))=(\x p)\bullet x=(p\x)\bullet x=p\bullet(u(x))$$

holds, so $$u$$ becomes an $$A[\x]$$-module endomorphism. Then from the above formula and (1) we know that

$$\rho\circ(\iota_!u)=u\circ\rho$$

holds.

<div class="proposition" markdown="1">

<ins id="prop7">**Proposition 7**</ins> In the above situation, define the $$A[\x]$$-endomorphism $$\psi=\x-\iota_!u$$ by the formula

$$\psi(p\otimes_Ax)=(\x p)\otimes_Ax -p\otimes_A u(x).$$

Then the sequence of $$A[\x]$$-modules

$$\iota_!M\overset{\psi}{\longrightarrow}\iota_!M\overset{\rho}{\longrightarrow}M_u\longrightarrow 0$$

is exact.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

It suffices to show that $$\ker\rho\subseteq \im\psi$$. Let $$z\in\ker\rho$$ be arbitrary. Then by decomposing $$z$$ into a sum of elements of the form $$p\otimes_A x$$, and further decomposing the $$p$$'s into linear combinations of $$1,\x,\x^2,\ldots$$ and regrouping according to the $$\x^k$$'s, we can write

$$z=\sum_k \x^k\otimes_A x_k,\qquad x_k\in M.$$

Then the condition $$z\in\ker\rho$$ yields

$$\rho(z)=\sum_k u^k(x_k)=0.$$

Now since $$\sum 1\otimes u^k(x_k)=0$$, we obtain

$$z=\sum_k (\x^k\otimes_A x_k-1\otimes_A u^k(x_k))=\sum_k (\x^k-\iota_!u^k)(1\otimes x_k),$$

and since in $$\iota_!M=A[\x]\otimes_A M$$ the element $$\x$$ acts on the $$A[\x]$$ factor and $$\iota_!u$$ acts on $$M$$, these multiplications commute. That is, the above expression can be written as

$$\sum_k (\x-\iota_!u)\circ\left(\sum_{j=0}^{k-1} \x^j (\iota_!u)^{k-j-1}\right),$$

which completes the proof.

</details>

On the other hand, considering the determinant of $$\psi$$, from [Corollary 6](#cor6) we obtain

$$\det (\x-\iota_!u)=\sum_{k=0}^n (-1)^k\tr\left({\bigwedge}^k(\iota_!u)\right)\x^{n-k}.$$

Moreover, the matrix representation $$[u]_\mathcal{B}^\mathcal{B}$$ of $$u$$ equals the matrix representation $$[\iota_!u]_{\mathcal{B}'}^{\mathcal{B}''}$$ of $$\iota_!u$$ with respect to the $$A[\x]$$-basis $$\mathcal{B}'=(1\otimes e_i)_{1\leq i\leq n}$$ of $$M[\x]$$, so the above formula can be written as

$$\det (\x-\iota_!u)=\sum_{k=0}^n (-1)^k\tr\left({\bigwedge}^k(u)\right)\x^{n-k}.$$

<div class="definition" markdown="1">

<ins id="def8">**Definition 8**</ins> The polynomial $$\det(\x-\iota_!u)$$ defined above is called the *characteristic polynomial* of $$u$$ and is denoted $$\chi_u(\x)$$.

</div>

Then from the preceding formula, we see that in the characteristic polynomial the coefficient of $$\x^n$$ is $$1$$, the coefficient of $$\x^{n-1}$$ is $$-\tr(u)$$, and the constant term is $$(-1)^n\det(u)$$.

<div class="proposition" markdown="1">

<ins id="prop9">**Proposition 9 (Cayley–Hamilton)**</ins> $$\chi_u(u)=0$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

We need to show that $$\chi_u(u)(x)=0$$ for every $$x\in M$$. Now using equation (1), $$\chi_u(u)(x)$$ equals $$\rho(\chi_u(\x)\otimes_Ax)$$. Observe that

$$\chi_u(\x)\otimes_Ax=\chi_u(\x)(1\otimes_Ax)=\det(\x-\iota_!u)(1\otimes_Ax).$$

But thinking of Laplace expansion, for any matrix $$X$$ and its cofactor matrix $$Y$$ we have $$XY^t=(\det X)I$$; hence there exists a suitable $$v\in\End_\rMod{A[\x]}(\iota_!M)$$ such that

$$\det(\x-\iota_!u)(1\otimes_Ax)=(\x-\iota_!u)(v(1\otimes_A x)),$$

and therefore we obtain the desired result by [Proposition 7](#prop7).

</details>
