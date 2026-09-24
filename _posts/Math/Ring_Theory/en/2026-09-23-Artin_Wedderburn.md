---
title: "Artin-Wedderburn Theorem"
description: "We define a semisimple ring as a ring that is semisimple as a module over itself and show that this is equivalent to every module being semisimple. After analyzing module structures, opposite rings, and endomorphism rings of matrix rings, we prove the Artin-Wedderburn theorem on the unique decomposition of semisimple rings into finite products of matrix rings over division rings."
excerpt: "Structure theorem for semisimple rings and unique decomposition into matrix rings"

categories: [Math / Ring Theory]
permalink: /en/math/ring_theory/artin_wedderburn
sidebar: 
    nav: "ring_theory-en"

date: 2026-09-23

weight: 8
translated_at: 2026-09-23T15:15:06+00:00
translation_source: antigravity-gemini-3.8-flash-high
---
[§Semisimple Modules](/en/math/ring_theory/semisimple_modules){: data-lid="bkiu1" } discussed modules that decompose into direct sums of simple modules. One of the most interesting applications is a *semisimple ring*, which is a ring $A$ that is a semisimple module when regarded as a module over itself; the key result of this post is that such a ring decomposes into a product of finitely many matrix rings.

In this post as well, a ring is assumed to have an identity, and commutativity is not assumed unless specified otherwise. Furthermore, an $A$-module is always understood to mean a left $A$-module.

## Semisimple Rings

::: Definition 1
If a ring $A$ is semisimple as a left $A$-module over itself, then $A$ is called a *semisimple ring*.
:::

Since the submodules of the left $A$-module $A$ are precisely the left ideals of $A$, this definition is simply [§Semisimple Modules, ⁋Definition 2](/en/math/ring_theory/semisimple_modules#def2){: data-lid="apyw2" } applied to $M=A$. Meanwhile, the following holds.

::: Proposition 2
For a ring $A$, $A$ is a semisimple ring if and only if every left $A$-module is semisimple.
:::
::: Proof
If every left $A$-module is semisimple, then in particular the left $A$-module $A$ is semisimple. Thus, it suffices to show the converse. Suppose $A$ is a semisimple ring. Any left $A$-module $M$ is a quotient of some free module $A^{(I)}$ ([\[Multilinear Algebra\] §Bases, ⁋Proposition 2](/en/math/multilinear_algebra/basis_of_free_modules#prop2){: data-lid="451t5" }), and since $A$ is semisimple, $A^{(I)}$ is also a semisimple $A$-module by [§Semisimple Modules, ⁋Theorem 5](/en/math/ring_theory/semisimple_modules#thm5){: data-lid="sgjq3" }, so its quotient is also semisimple ([§Semisimple Modules, ⁋Corollary 6](/en/math/ring_theory/semisimple_modules#cor6){: data-lid="cx5wl" }).
:::

In addition, the following holds.

::: Proposition 3
If $A$ is a semisimple ring, then $A$ is a direct sum of finitely many simple left ideals.
:::
::: Proof
Let $A=\bigoplus_{i\in I}\mathfrak{a}_i$ be a direct sum of simple left ideals. Viewing the identity $1$ as an element of this direct sum decomposition, only on a *finite* index set $J\subseteq I$ can the identity be non-$0$. Now for any $a\in A$, we have $a=a\cdot 1\in\sum_{i\in J}\mathfrak{a}_i$, and therefore $A=\bigoplus_{i\in J}\mathfrak{a}_i$.
:::

## Matrix Rings over Division Rings

First, we define the following.

::: Definition 4
For a ring $A$, the ring defined on the same abelian group as $A$ with multiplication given by $a\ast^\op b=ba$ is called the *opposite ring* of $A$, and is denoted by $A^\op$.
:::

Directly from the definition, $(A^\op)^\op=A$, and a right $A$-module is the same as a left $A^\op$-module. Also, if $D$ is a division ring, then the inverse of any nonzero element serves as its inverse in $D^\op$ as well, so $D^\op$ is also a division ring.

::: Proposition 5
Let $D$ be a division ring and $n\geq 1$. If we endow the space of column vectors $D^n$ with the left $\Mat_n(D)$-module structure given by matrix multiplication, the following hold:

1. $D^n$ is a simple $\Mat_n(D)$-module.
2. For the left ideal of matrices whose entries outside the $k$-th column are $0$,
    
    $$C_k=\left\{\begin{pmatrix}0&\cdots&a_{1k}&\cdots&0\\\vdots&\ddots&\vdots&\ddots&\vdots\\0&\cdots&a_{nk}&\cdots&0\end{pmatrix}\middle\vert a_{1k},\ldots,a_{nk}\in D\right\}$$
    
    there exists a direct sum decomposition $\Mat_n(D)=\bigoplus_{k=1}^nC_k$, where each $C_k$ is, as a $\Mat_n(D)$-module, isomorphic to $D^n$. In particular, $\Mat_n(D)$ is a semisimple ring.
:::
::: Proof
First, for the second statement, partitioning matrices by columns gives $\Mat_n(D)=\bigoplus_kC_k$; that $C_k$ is a left ideal can be verified by a simple computation, and that $C_k\rightarrow D^n$ is a module isomorphism is also clear.

Now let us show the first statement. Choose $0\neq v\in D^n$ and any $w\in D^n$. If we choose a component with $v_k\neq 0$, say $k$, and define the matrix $A$ by $A_{ik}=w_iv_k^{-1}$ and the remaining entries by $0$, then

$$(Av)_i=A_{ik}v_k=w_iv_k^{-1}v_k=w_i$$

hence $Av=w$. That is, any element other than $0$ generates the whole of $D^n$, so $D^n$ is simple. Now from the second statement, since $\Mat_n(D)$ is a direct sum of simple modules, $\Mat_n(D)$ is a semisimple ring.
:::

Furthermore, the following holds.

::: Proposition 6
In the setting of [Proposition 5](#prop5){: data-lid="dx93u" }, $\End_{\Mat_n(D)}(D^n)\cong D^\op$.
:::
::: Proof
For any $d\in D$, consider the map $\rho_d(v)=vd$ that multiplies each component of a column vector by $d$ on the right. Then for any matrix $A$,

$$(A(vd))_i=\sum_jA_{ij}(v_jd)=(Av)_id$$

so $\rho_d$ is a module endomorphism. Furthermore, from the identity

$$\rho_d\circ\rho_{d'}(v)=vd'd=\rho_{d'd}(v)$$

the assignment $d\mapsto\rho_d$ defines a ring homomorphism $D^\op\rightarrow\End_{\Mat_n(D)}(D^n)$, and since $\rho_d$ sends the first standard column vector $e_1$ to $e_1d$, it is clearly injective.

It remains to show that this map is surjective. Let $\varphi$ be an arbitrary endomorphism and let $E_{ij}$ be the matrix units. Since $E_{11}e_1=e_1$, we have

$$E_{11}\varphi(e_1)=\varphi(E_{11}e_1)=\varphi(e_1)$$

and since the left-hand side is the vector retaining only the first component of $\varphi(e_1)$, we have $\varphi(e_1)=e_1d$ for some $d\in D$. Now for any $v\in D^n$, let the matrix whose $(i,1)$-entry is $v_i$ and whose other entries are $0$ be $A_i$. Then $v=\sum_iA_ie_1$, so

$$\varphi(v)=\sum_iA_i\varphi(e_1)=\sum_iA_i(e_1d)=vd=\rho_d(v)$$

holds. Therefore, $\varphi=\rho_d$, and the correspondence is surjective.
:::

As mentioned earlier, the goal of this post is to show that any semisimple ring decomposes into a product of finitely many matrix rings, and the two propositions above provide the basic properties of matrix rings for this purpose. Now we must examine the properties of rings and their endomorphisms.

::: Lemma 7
For any ring $A$, we have $\End_A(A)\cong A^\op$.
:::
::: Proof
If we define $\Phi:\End_A(A)\rightarrow A^\op$ by $\Phi(f)=f(1)$, it is easy to show that this is a ring homomorphism into $A^\op$. Conversely, for any $a\in A$, the right multiplication $x\mapsto xa$ is a left module endomorphism, and since this correspondence gives the inverse of $\Phi$, it follows that $\Phi$ is an isomorphism.
:::

Our next observation concerns linear operators on semisimple modules. Intuitively, this states that the simple modules comprising a semisimple module cannot mix (unless they are of the same type), and the proof naturally uses [§Division Rings, ⁋Lemma 10](/en/math/ring_theory/division_rings#lem10){: data-lid="rdgn9" }.

::: Lemma 8
Let $S_1,\ldots,S_k$ be pairwise non-isomorphic simple modules and let $n_1,\ldots,n_k\geq 1$. For $M=\bigoplus_{i=1}^kS_i^{n_i}$,

$$\End_A(M)\cong\prod_{i=1}^k\Mat_{n_i}\big(\End_A(S_i)\big)$$

holds.
:::
::: Proof
Let $\iota_{i,a}$ and $\pi_{i,a}$ denote the inclusion and projection for the direct sum summands, respectively. For an endomorphism $\varphi$, the component $\pi_{i,a}\circ\varphi\circ\iota_{j,b}$ is a homomorphism from $S_j$ to $S_i$; if $i\neq j$, by [§Division Rings, ⁋Lemma 10](/en/math/ring_theory/division_rings#lem10){: data-lid="wccwq" } it must be $0$. Therefore, $\varphi$ is uniquely given, for each $i$, by the data of the matrices $\varphi^{(i)}=(\pi_{i,a}\circ\varphi\circ\iota_{i,b})_{a,b}\in\Mat_{n_i}(\End_A(S_i))$.

We must verify that this correspondence is a ring isomorphism; that is, we must show that it preserves addition and multiplication. The additive part is clear, and for multiplication, since $\sum_{j,b}\iota_{j,b}\circ\pi_{j,b}=\id_M$, we have

$$\pi_{i,a}\circ(\varphi\circ\psi)\circ\iota_{i,c}=\sum_{b}(\pi_{i,a}\circ\varphi\circ\iota_{i,b})\circ(\pi_{i,b}\circ\psi\circ\iota_{i,c})$$

which is precisely the $(a,c)$-entry of the matrix product.
:::

In addition, the following holds.

::: Lemma 9
For any ring $A$, the transpose gives an isomorphism $\Mat_n(A)^\op\cong\Mat_n(A^\op)$.
:::
::: Proof
$T(X)=X^t$ is an additive bijection and preserves the identity matrix. For the multiplication in $\Mat_n(A)^\op$ given by $X\ast^\op Y=YX$,

$$T(X\ast^\op Y)_{ij}=(YX)_{ji}=\sum_k Y_{jk}X_{ki}$$

and the product in $\Mat_n(A^\op)$ is

$$\big(T(X)T(Y)\big)_{ij}=\sum_k(X^t)_{ik}\ast^\op(Y^t)_{kj}=\sum_k(Y^t)_{kj}(X^t)_{ik}=\sum_k Y_{jk}X_{ki}$$

so they coincide.
:::

The final ingredient is the module theory of product rings.

::: Proposition 10
Let $A=A_1\times\cdots\times A_k$, and let $e_i\in A$ be the element whose $i$-th component is $1$ and other components are $0$.

1. $\{e_1,\ldots,e_k\}$ is a complete set of central orthogonal idempotents, and any left $A$-module $M$ decomposes as $M=\bigoplus_ie_iM$. Each $e_iM$ is a module on which $A$ acts via the $i$-th component, making it an $A_i$-module, and its $A$-submodules coincide with its $A_i$-submodules. In particular, the simple left $A$-modules are precisely those obtained by taking, for some $i$, a simple left $A_i$-module and, via the action of the $i$-th component, viewing it as an $A$-module.
2. If each $A_i$ is a semisimple ring, then $A$ is also a semisimple ring.
:::
::: Proof
1. That the $e_i$ form a complete set of central orthogonal idempotents can be checked directly by componentwise calculation. ([§Central Idempotents and Ring Decomposition, ⁋Theorem 5](/en/math/ring_theory/idempotents#thm5){: data-lid="e0b4o" }) Then, from the equations
    
    $$1=\sum e_i,\qquad e_ie_j=\delta_{ij}e_i$$
    
    we know that $M=\bigoplus_i e_iM$, and by centrality, on $e_iM$ only the $i$-th component $A_i$ acts while the other components act as $0$, so for $e_iM$, the $A$-submodules and $A_i$-submodules are identical. In particular, if $M\neq 0$ is simple, exactly one factor in this decomposition is nonzero, so for $M$ to be a simple left $A$-module is equivalent to $M$ being, for some $i$, a simple $A_i$-module.

2. If each $A_i$ is a semisimple ring, then $A_i$ is a direct sum of simple left ideals, so $A\cong\bigoplus_i A_i$ is also a direct sum of simple left ideals, and thus is a semisimple ring.
:::

## Artin-Wedderburn Theorem

Now all the ingredients are ready.

::: Theorem 11 (Artin-Wedderburn)
For a ring $A$, the following are equivalent.

1. $A$ is a semisimple ring.
2. For some division rings $D_1,\ldots,D_k$ and natural numbers $n_1,\ldots,n_k$,
    
    $$A\cong\Mat_{n_1}(D_1)\times\cdots\times\Mat_{n_k}(D_k)$$
    
    holds.

Moreover, the data $k$ and $(n_i,D_i)$ constituting this decomposition of the semisimple ring are unique up to permutation and isomorphism.
:::
::: Proof
That the second condition implies the first follows from the fact that each factor is a semisimple ring by [Proposition 5](#prop5){: data-lid="aw3ne" }, which immediately yields the claim from the second result of [Proposition 10](#prop10){: data-lid="l9ws8" }.

Now assume the first condition and show the second condition. First, by [Proposition 3](#prop3){: data-lid="jyozf" }, $A$ is a direct sum of finitely many simple left ideals. Grouping the factors by isomorphism class, for pairwise non-isomorphic simple modules $S_1,\ldots,S_k$ and natural numbers $n_i\geq 1$, we have $A\cong\bigoplus_iS_i^{n_i}$ as left modules. Setting $C_i=\End_A(S_i)$, this is a division ring by [§Division Rings, ⁋Lemma 10](/en/math/ring_theory/division_rings#lem10){: data-lid="uauah" }, and by [Lemma 7](#lem7){: data-lid="reb59" } and [Lemma 8](#lem8){: data-lid="m01xr" },

$$A^\op\cong\End_A(A)\cong\prod_{i=1}^k\Mat_{n_i}(C_i)$$

holds. Taking $(-)^\op$ on both sides, by [Lemma 9](#lem9){: data-lid="2hk1d" } we obtain

$$A\cong\prod_{i=1}^k\Mat_{n_i}(C_i)^\op\cong\prod_{i=1}^k\Mat_{n_i}(C_i^\op)$$

and since $D_i=C_i^\op$ is a division ring, we obtain the desired decomposition.

Now suppose that an arbitrary decomposition $A\cong\prod_{j=1}^l\Mat_{m_j}(E_j)$ satisfying these properties is given, and let us show uniqueness. This essentially traces the above construction in reverse: first, on $W_j=E_j^{m_j}$, $A$ acts via matrix multiplication through the $j$-th component $\Mat_{m_j}(E_j)$ while the remaining components act as $0$, giving it the structure of a left $A$-module. Then by [Proposition 5](#prop5){: data-lid="qlrxy" }, each $W_j$ is simple and the $j$-th factor is isomorphic to $W_j^{m_j}$, so $A\cong\bigoplus_jW_j^{m_j}$ as left modules, and by the first result of [Proposition 10](#prop10){: data-lid="yl0q8" }, the $W_j$ belong to different components and are thus pairwise non-isomorphic. Then by [§Semisimple Modules, ⁋Proposition 10](/en/math/ring_theory/semisimple_modules#prop10){: data-lid="wprdz" }, one sees that the two decompositions $\bigoplus_iS_i^{n_i}\cong\bigoplus_jW_j^{m_j}$ give the same data, and finally, by the first result of [Proposition 10](#prop10){: data-lid="c9hgr" } we have $\End_A(W_i)=\End_{\Mat_{m_i}(E_i)}(E_i^{m_i})$, and by [Proposition 6](#prop6){: data-lid="wlly1" } this is isomorphic to $E_i^\op$, so

$$E_i\cong\End_A(W_i)^\op\cong\End_A(S_i)^\op=C_i^\op=D_i$$

holds.
:::

Intuitively, this theorem can be understood as a kind of block diagonalization: the action of a semisimple ring splits into mutually non-interacting blocks, and on each block it acts like a matrix ring over a division ring. The module theory over a semisimple ring $A$ is then particularly simple.

::: Corollary 12
Let $A\cong\prod_{i=1}^k\Mat_{n_i}(D_i)$ be a semisimple ring. Then, up to isomorphism, the simple left $A$-modules consist precisely of the $V_i=D_i^{n_i}$, and any left $A$-module is a direct sum of summands isomorphic to them.
:::
::: Proof
By [Proposition 2](#prop2){: data-lid="c2mpv" }, every $A$-module is semisimple, so it can be expressed as a direct sum of simple $A$-modules, and by [Proposition 5](#prop5){: data-lid="pg0b4" } and [Proposition 10](#prop10){: data-lid="zkbod" }, each $V_i$ is simple. 

Conversely, suppose an arbitrary simple $A$-module $M$ is given. For $0\neq x\in M$, since $M=Ax$, there exists a surjection $A\rightarrow M$, and considering the left module decomposition $A\cong\bigoplus_iV_i^{n_i}$ obtained from the second result of [Proposition 5](#prop5){: data-lid="npt9u" }, this surjection is nonzero on some direct summand of $A$, namely $V_i$. Then there exists a nonzero homomorphism $V_i\rightarrow M$ between simple modules, so by [§Division Rings, ⁋Lemma 10](/en/math/ring_theory/division_rings#lem10){: data-lid="aib2j" }, $M\cong V_i$.
:::

Meanwhile, although [Definition 1](#def1){: data-lid="dw004" } was given in terms of left module structures, defining it via right modules yields the same rings. Since a right $A$-module is equivalent to a left $A^\op$-module, $A$ being right semisimple means that $A^\op$ is a semisimple ring. But if $A$ is a semisimple ring, applying [Lemma 9](#lem9){: data-lid="t2e0p" } to the decomposition in [Theorem 11](#thm11){: data-lid="gy0gw" } shows that $A^\op\cong\prod_i\Mat_{n_i}(D_i^\op)$ is also a product of matrix rings and thus a semisimple ring, and the converse holds similarly. Therefore, the notion of a semisimple ring is independent of the choice of handedness.

---

**References**

**[DF]** D. S. Dummit and R. M. Foote, *Abstract algebra*, 3rd ed., Wiley, 2004.  
**[Rot]** J. J. Rotman, *An introduction to homological algebra*, 2nd ed., Universitext, Springer, 2009.
