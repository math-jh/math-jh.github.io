---
title: "Symmetric Tensors"
description: "We define symmetric tensors and symmetric powers using modules over group rings and group actions, and discuss properties of relative traces and the invariance of tensor products under subgroup actions."
excerpt: "Symmetric group actions, symmetric tensors, and symmetric powers"

categories: [Math / Multilinear Algebra]
permalink: /en/math/multilinear_algebra/symmetric_tensors
sidebar: 
    nav: "multilinear_algebra-en"

date: 2025-05-07
weight: 13
translated_at: 2026-07-14T01:00:03+00:00
translation_source: kimi-cli
last_polished_at: 2026-10-25T03:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
Given any group $H$ and ring $A$, we have defined the group ring $AH$. ([\[Algebraic Structures\] §Algebras, ⁋Definition 5](/en/math/algebraic_structures/algebras#def5){: data-lid="n282q" }) Now fix an $AH$-module $M$, and define $M^H$ as the set

$$M^H=\left\{x\in M\mid \text{$hx=x$ for all $h\in H$}\right\}$$

Here $hx$ is of course defined by viewing $h$ as an element of $AH$ via $h\mapsto \delta_h$, then using the $AH$-module structure. Then $M^H$ is an $A$-submodule of $M$, but if the group $H$ is not commutative, it is generally not an $AH$-submodule. Also, if a subgroup $G$ of $H$ is given, then $M^H\leq M^G$ is obvious. 

Now suppose $x\in M^G$ and $h\in H$ are given, and let $\bar{h}=hG$ be an element of $H/G$. Then, since

$$\bar{h}x=(hG)x=\left\{hx\right\}$$

is obvious, by a slight abuse of notation we may treat $hx$ and $\bar{h}x$ as the same. Then for any $h'\in H$, the equation

$$h'(\bar{h}x)=(h'\bar{h})x$$

holds. 

Now assume that $[H:G]$ is finite. Then $H/G$ is a finite set, so the sum

$$\sum_{\bar{h}\in H/G}\bar{h}x$$

is well-defined. Moreover, this sum is an element of $M^H$, because for any $h'\in H$,

$$h'\left( \sum_{\bar{h}\in H/G}\bar{h}x\right)=\sum_{\bar{h}\in H/G}(h'\bar{h})x=\sum_{\bar{z}\in H/G}\bar{z}x$$

::: Definition 1
In the above situation, we define $\tr_{H/G}:M^G \rightarrow M^H$ by the formula

$$\tr_{H/G}(x)=\sum_{\bar{h}\in H/G} \bar{h}x$$

and call this the *relative trace*. 
:::

Then the following holds. 

::: Proposition 2
The following hold.

1. For any $x\in M^G$ and $h\in H$, we have $hx\in M^{hGh^{-1}}$ and the equation $\tr_{H/hGh^{-1}}(hx)=\tr_{H/G}(x)$ holds. 
2. For subgroups $F\leq G\leq H$ with all relevant indices finite, $\tr_{H/G}\circ\tr_{G/F}=\tr_{H/F}$ holds. 
3. For any $x\in M^H$, $\tr_{H/G}(x)=[H:G].x$ holds. 
:::

## Symmetric Tensors

Now we begin the main definitions. First, for any $A$-module $M$, we can define an $S_n$-action on the $n$-th tensor power $\T^n(M)$ by the formula

$$\sigma(x_1\otimes x_2\otimes \cdots \otimes x_n)=x_{\sigma^{-1}(1)}\otimes \cdots \otimes x_{\sigma^{-1}(n)}$$

::: Definition 3
In the above situation, the elements satisfying

$$\sigma z=z\qquad\text{for all $\sigma\in S_n$}$$

among $z\in \T^nM$ are called $n$th *symmetric tensors*, and their collection $\Sym^n(M)$ is called the $n$-th *symmetric power*. Their (graded) direct sum is written as

$$\Sym(M)=\bigoplus_{d=0}^\infty \Sym^d(M)$$
:::

$\Sym(M)$ must be distinguished from the symmetric algebra $\S(M)$ defined earlier, but in favorable cases we can show that the two are isomorphic.

First, let us define the product of two symmetric tensors. In general, given any two symmetric tensors

$$x=x_1\otimes x_2\otimes \cdots \otimes x_p,\qquad y=y_1\otimes y_2\otimes \cdots \otimes y_q$$

there is no guarantee that their product as tensors

$$x\otimes y=x_1\otimes x_2\otimes \cdots \otimes x_p\otimes y_1\otimes y_2\otimes \cdots \otimes y_q$$

will be a symmetric tensor. This is because, simply considering an element that swaps the positions of $x_i$ and $y_j$ in the above form, it may fail to satisfy the condition of a symmetric tensor.

Instead, a product of the above form is invariant under the action of the subgroup $S_p\times S_q$ of $S_{p+q}$. Therefore, if we define

$$xy=\tr_{S_{p+q}/S_p\times S_q}(x\otimes y)$$

then $xy\in (\T^{p+q}M)^{S_{p+q}}=\Sym^{p+q}(M)$, and its value is

$$\sum_{\bar{\sigma}\in S_{p+q}/(S_p\times S_q)} \bar{\sigma}(x\otimes y)$$

On the other hand, if we let $S_{p,q}$ be the subset satisfying the conditions

$$\sigma(1)<\sigma(2)< \cdots < \sigma(p), \qquad \sigma(p+1)<\sigma(p+2)<\cdots< \sigma(p+q)$$

consisting of those $\sigma$ in $S_{p+q}$, then it is not difficult to find a bijection between $S_{p+q}/S_p\times S_q$ and $S_{p,q}$. This is quite natural, because the elements of $S_p\times S_q$ are those that fix the images of the two blocks and may permute freely within them, while the elements of $S_{p,q}$, conversely, choose the images of the two blocks arbitrarily but fix the permutation within them to a single one. Therefore, the above formula can be rewritten as

$$xy=\sum_{\sigma\in S_{p,q}}\sigma(x\otimes y)$$

::: Proposition 4
For any $A$-module $M$, the following hold.

1. $\Sym(M)$ becomes an associative, commutative unital $A$-algebra under the multiplication defined above. 
2. For positive integers $p_1,\ldots, p_n$ and $x_i\in \Sym^{p_i}(M)$, the formula
    
    $$x_1x_2\cdots x_n=\tr_{S_{p_1+\cdots+p_n}/S_{p_1}\times\cdots\times S_{p_n}}(x_1\otimes \cdots\otimes x_n)$$

    holds.
:::
::: Proof
Let us show the second claim first. We proceed by induction. Since the case $n=2$ is the definition, assume inductively that

$$x_2\cdots x_n=\tr_{S_{p_2+\dots+p_n}/(S_{p_2}\times\cdots\times S_{p_n})}(x_2 \otimes \dots \otimes x_n)$$

holds. Now considering the tower of subgroups of $S_{p_1+\cdots+p_n}$

$$S_{p_1+\cdots+p_n}\geq S_{p_1}\times S_{p_2+\cdots+p_n}\geq \left\{\id_{p_1}\right\}\times S_{p_2+\cdots+p_n}$$

by the result of [Proposition 2](#prop2){: data-lid="pf1re" },

$$\tr_{S_{p_1+\cdots +p_n}/S_{p_2+\cdots +p_n}}(x_1\otimes\cdots\otimes x_n)=\tr_{S_{p_1+\cdots+p_n}/(S_{p_1}\times S_{p_2+\cdots+p_n})}\circ\tr_{(S_{p_1}\times S_{p_2+\cdots+p_n})/S_{p_2+\cdots+p_n}}(x_1\otimes\cdots\otimes x_n)$$

holds. Now computing the right-hand side, by the above inclusions,

$$\tr_{(S_{p_1}\times S_{p_2+\cdots+p_n})/S_{p_2+\cdots+p_n}}(x_1\otimes\cdots\otimes x_n)=x_1\otimes\tr_{S_{p_2+\cdots+p_n}/(S_{p_2}\times\cdots\times S_{p_n})}(x_2\otimes\cdots\otimes x_n)=x_1\otimes (x_2\cdots x_n)$$

and therefore

$$\tr_{S_{p_1+\cdots +p_n}/S_{p_2+\cdots +p_n}}(x_1\otimes\cdots\otimes x_n)=\tr_{S_{p_1+\cdots+p_n}/(S_{p_1}\times S_{p_2+\cdots+p_n})}(x_1\otimes (x_2\cdots x_n))=x_1(x_2\cdots x_n)$$

holds. If we had initially started with the following tower of subgroups

$$S_{p_1+\cdots+p_n}\geq S_{p_1+\cdots+p_{n-1}}\times S_{p_n}\geq S_{p_1+\cdots+p_{n-1}}\times 1$$

we would obtain

$$\tr_{S_{p_1+\cdots +p_n}/S_{p_2+\cdots +p_n}}(x_1\otimes\cdots\otimes x_n)=(x_1\cdots x_{n-1})x_n$$

and in particular, in the case $n=3$, the associativity of $\Sym(M)$ is shown from this. For commutativity, taking $\sigma$ to be the permutation arranging, among the $p_1+p_2$ elements, the first $p_1$ elements and the last $p_2$ elements into the form

$$\underbrace{p_2+1,\cdots p_2+p_1}_\text{\scriptsize$p_1$ elements},\qquad \underbrace{1,\ldots, p_2}_\text{\scriptsize$p_2$ elements}$$

one uses such $\sigma\in S_{p_1+p_2}$ and applies the first result of [Proposition 2](#prop2){: data-lid="whrg3" }. The unit is obviously $1\in \Sym^0(M)$.
:::

For any $x\in M$ and $k\in \mathbb{N}$, define

$$\gamma_k(x)=\underbrace{x\otimes\cdots\otimes x}_\text{\scriptsize $k$ times}$$

Then, computing using the above proposition, we obtain the following corollary.

::: Corollary 5
The following hold. 

1. The product of $x$ defined in [Proposition 4](#prop4){: data-lid="8yg92" }, $x^k$, equals $k!\gamma_k(x)$. 
2. For any $x_1,\ldots, x_n\in M$,
    
    $$\gamma_p(x_1+\cdots+x_n)=\sum_{p_1+\cdots+p_n=p}\gamma_{p_1}(x_1)\cdots\gamma_{p_n}(x_n)$$

    holds. 
3. For any $x_1,\ldots, x_n\in M$, let $p=p_1+\cdots+p_n$. Then, for the set, such that $\{1,\ldots, p\}=P_1\cup\cdots\cup P_n$, of ordered tuples of partitions of the set $\{1,\ldots, p\}$,

    $$\mathcal{P}=\left\{(P_1,\ldots, P_n)\bigg\vert \bigcup_{k=1}^n P_k=\{1,\ldots, p\}, \lvert P_k\rvert=p_k, P_i\cap P_j=\emptyset\text{ for }i\neq j\right\}$$

    and, for each $P\in\mathcal{P}$, for the function defined such that $i\in P_{\phi(i)}$, $\phi:\{1,\ldots, p\} \rightarrow \{1,\ldots, n\}$,

    $$\gamma_{p_1}(x_1)\cdots\gamma_{p_n}(x_n)=\sum_{P\in \mathcal{P}}x_{\phi(1)}\otimes \cdots \otimes x_{\phi(p)}$$

    holds. 
4. For any $x\in M$ and natural numbers $p,q$, the identity
    
    $$\gamma_p(x)\gamma_q(x)=\frac{(p+q)!}{p!q!}\gamma_{p+q}(x)$$

    holds.
5. Suppose any $x_1,\ldots, x_n\in M$ are given, and for any subset $H\subseteq \{1,\ldots, n\}$, let $x_H=\sum_{i\in H}x_i$. Then the identity
    
    $$(-1)^nx_1x_2\cdots x_n=\sum_{H\subseteq\{1,\ldots, n\}}(-1)^{\lvert H\rvert}\gamma_n(x_H)$$

    holds. 
:::

As in general tensor algebra, our interest is especially when $M$ is a free $A$-module. First, let us prove the following lemma.

::: Lemma 6
For a finite group $H$ and a left $AH$-module $N$, suppose that $N$ is given an $H$-invariant $A$-basis $B$, and consider the quotient set $\Omega=B/H$ for this action. Then the following hold. 

1. For each $\omega\in \Omega$, if we define $y_\omega=\sum_{b\in\omega}b$, then $(y_\omega)_{\omega\in \Omega}$ forms for $N^H$ an $A$-basis. 
2. A basis for a supplementary submodule of $N^H$ in $N$ is given by taking, for each $\omega\in\Omega$, the set $\omega'=\omega\setminus \{z_\omega\}$ with one element removed, and taking the union $B'=\bigcup_{\omega\in\Omega} \omega'$. 
:::
::: Proof
First, if we collect all the $y_\omega$ and all elements of $B'$, since this merely replaces in each $\omega$ one element $z_\omega$ with $y_\omega$, by simple linear algebra we know that this forms for $N$ an $A$-basis. That is, if according to the given decomposition we set

$$N_1=\sum_{\omega\in\Omega} Ay_\omega,\qquad N_2=\sum_{b'\in B'}Ab'$$

then $N=N_1\oplus N_2$. 

Now what we must show is $N_1=N^H$. By assumption, $N_1\subseteq N^H$ is obvious. On the other hand, for any $y\in N^H$, if we express $y$ as a linear combination in the $A$-basis $B$ as $y=\sum \alpha_b b$, we know that for all $b\in B$ and all $h\in H$, it must hold that $\alpha_{hb}=\alpha_b$. From this, we must have $y\in N_1$. 
:::

Then using this, we can show the following proposition. 

::: Proposition 7
Suppose $M$ is a free $A$-module and $(e_i)_{i \in I}$ is a basis of $M$.

1. For each $\nu\in\mathbb{N}^{(I)}$, the elements $e_\nu=\prod_{i\in I}\gamma_{\nu_i}(e_i)$ form for $\Sym(M)$ an $A$-basis.
2. For any $k$, $\Sym^k(M)$ is, in $\T^kM$, an $A$-direct factor. 
:::
::: Proof
1. It suffices to use the second equation of [Corollary 5](#cor5){: data-lid="9lo98" }.
2. For each $k$, it suffices to set $H=S_k$, $N=\T^kM$ and apply [Lemma 6](#lem6){: data-lid="aos4n" }. 
:::

## Functoriality

For an $A$-module homomorphism $u: M \rightarrow N$, 

$$\T(u)\vert_{\Sym(M)}:\Sym(M) \rightarrow \Sym(N)$$

is well-defined. We write $\T(u)\vert_{\Sym(M)}$ simply as $\Sym(u)$. Then we know that $\Sym$ becomes a functor, and moreover, from the corresponding properties in [§Tensor Algebra](/en/math/multilinear_algebra/tensor_algebras){: data-lid="qskm9" }, we know that when each $M_i$ is a free $A$-module, the following natural isomorphism 

$$\bigotimes_{i\in I}\Sym(M_i)\rightarrow \Sym\left(\bigoplus_{i\in I} M_i\right)$$

exists. Then defining $u: M\oplus M \rightarrow M$ by $(x,y)\mapsto x+y$, we know that the following composition

$$\Sym(M)\otimes\Sym(M) \rightarrow \Sym(M\oplus M)\overset{\Sym(u)}{\rightarrow} \Sym(M)$$

sends $x\otimes y$ to $xy$. 

## Symmetric Algebra and Symmetric Tensors

Consider the canonical injections $i: M \rightarrow \T(M)$ and $j: M \rightarrow \Sym(M)$. Then by [§Tensor Algebra, ⁋Proposition 2](/en/math/multilinear_algebra/tensor_algebras#prop2){: data-lid="4p4u3" }, there exists a unique $\mathbb{N}$-graded $A$-algebra homomorphism $s: \T(M)\rightarrow \Sym(M)$ such that $j=s\circ i$. Then this is the identity on $\T^0(M)=\Sym^0(M)$, and considering how multiplication is defined in $\T(M)$ and $\Sym(M)$ respectively, we know that $s:\T(M) \rightarrow \Sym(M)$ is precisely the *symmetrization* 

$$s:\T(M)\rightarrow \Sym(M);\qquad x\mapsto \sum_{\sigma\in S_n}\sigma x$$

One thing to be somewhat careful about is that even if $x\in\Sym^k(M)\subseteq \T^k(M)$, $s(x)$ does not output $x$ as is, but rather $k!.x$.

::: Remark 8
For reasons such as the above, some references define the symmetric product from the beginning as

$$xy=\frac{p!q!}{(p+q)!}\tr_{S_{p+q}/(S_p\times S_q)}(x\otimes y)$$

The advantage of doing so is that one no longer needs to worry about coefficients like the above, but for the notation above to make sense, $\T(M)$ must have a $\mathbb{Q}$-vector space structure from the start.

In general, any $A$-module has a $\mathbb{Z}$-module structure (so expressions like $k!.x$ are well-defined regardless of $A$), but since no natural $\mathbb{Q}$-action exists, we choose to keep using the original definition.
:::

For the symmetrization map $s:\T(M) \rightarrow \Sym(M)$ obtained in this way, by [§Tensor Algebra, ⁋Proposition 6](/en/math/multilinear_algebra/tensor_algebras#prop6){: data-lid="c32gr" } we can obtain, satisfying the relation

$$s=\bar{s}\circ p$$

a map $\bar{s}: \S(M) \rightarrow \Sym(M)$, and it is not difficult to check that this is indeed a graded homomorphism. Here $p: \T(M) \rightarrow \S(M)$ is the canonical projection.

On the other hand, $\bar{s}$ also has a map in the opposite direction,

$$t: \Sym(M)\hookrightarrow \T(M)\overset{p}{\rightarrow}\S(M)$$

and our claim is that in many cases these two maps can be thought of as (almost) inverses of each other.

::: Proposition 9
The following hold.

1. If $x\in \S^n(M)$, then $(t\circ\bar{s})(x)=n!.x$.
2. If $x\in \Sym^n(M)$, then $(\bar{s}\circ t)(x)=n!.x$.
:::

The proof of this is a simple computation.

For reasons similar to what we observed in [Remark 8](#rmk8){: data-lid="dxro4" } above, if $A$ is (not only a $\mathbb{Z}$-algebra but) a $\mathbb{Q}$-algebra, then $x\mapsto n!.x$ is a bijection, and thus one can verify that $\bar{s}: \S(M) \rightarrow \Sym(M)$ defined above is an isomorphism.

## Polynomial Mappings

On the other hand, the symmetric algebra $\S(M)$ could be thought of as a representation of symmetric $n$-linear maps; considering $\Sym(M)$ together with it via [Proposition 9](#prop9){: data-lid="7smfc" } above, we obtain the following proposition.

::: Proposition 10
Let two $A$-modules $M,N$, a natural number $n$, and $u: M \rightarrow N$ be given. If $M$ is a free $A$-module, then the following are all equivalent.

1. There exists, satisfying the equation $u(x)=v(x,\ldots, x)$, an $n$-linear map $v: M^n \rightarrow N$.
2. There exists, satisfying the equation $u(x)=w(\gamma_n(x))$, a linear map $w: \Sym^n(M) \rightarrow N$.
3. There exist a basis of $M$, $(e_i)_{i\in I}$, and an $(\mathbb{N}^{(I)})_n$-indexed family $(y_\nu)$ such that
    
    $$u\left(\sum_{i\in I}\lambda_i e_i\right)=\sum_{\nu\in(\mathbb{N}^{(I)})_n}\lambda^\nu y_\nu$$

    holds.
4. For every basis of $M$, $(e_i)_{i\in I}$, a family $(y_\nu)$ satisfying the formula in condition 3 can be found.
:::

We then call maps $u: M \rightarrow N$ satisfying these equivalent conditions degree $n$ *homogeneous polynomial mappings*, and write their collection as $\Poly^n(M,N)$. The first and second conditions of the above proposition respectively induce surjections from the collection of maps from $M$ to $N$ that are $n$-linear onto $\Poly^n(M,N)$, and from $\Hom_A(\Sym^n(M), N)$ onto $\Poly^n(M,N)$; the third and fourth conditions justify this name *polynomial mapping*.

::: Example 11
For an $A$-module $N$, suppose a free $A$-module $A^{(I)}$ is given and fix a degree $n$ homogeneous polynomial $u\in N[\x_i]_{i\in I}$. Then the map

$$(x_i)_{i\in I} \mapsto u(x_i)\in N$$

is a homogeneous polynomial mapping between $A$-modules, and its degree is $n$.
:::

It is not difficult to show that the composition of two polynomial mappings is again a homogeneous mapping.

::: Proposition 12
Assume all the conditions of [Proposition 10](#prop10){: data-lid="7rykx" }, and additionally assume that $y\mapsto n!.y$ is an automorphism of $N$. Then for any $u\in\Poly^n(M,N)$, there exists, satisfying the equation

$$u(x)=v(x,\ldots, x)$$

, a unique symmetric $n$-linear map $v:M^n \rightarrow N$. Moreover, for any $x_1,\ldots, x_n\in M$, explicitly

$$v(x_1,\ldots, x_n)=\frac{1}{n!}\sum_{H\subseteq \{1,\ldots, n\}}(-1)^{n-\lvert H\rvert}u\left(\sum_{i\in H} x_i\right)$$

holds.
:::

This is a consequence that follows from [Corollary 5](#cor5){: data-lid="8g6xk" }. Now combining this with the observation in [Remark 8](#rmk8){: data-lid="lzu75" }, we obtain the following result.

::: Proposition 13
Assume the situation of [Proposition 10](#prop10){: data-lid="3rpqm" }, and consider the canonical homomorphism $\Hom_A(\Sym^n(M), N) \rightarrow \Poly^n(M,N)$. Then the following hold.

1. If $A$ is an infinite integral domain and $N$ is torsion-free, then this homomorphism is an isomorphism.
2. If $y\mapsto n!.y$ is an injective endomorphism from $N$ to $N$, then this homomorphism is an isomorphism.
:::

## Symmetric Functions

On the other hand, when $M$ is a finitely generated free $A$-module, we know that $\S(M)$ is isomorphic to the polynomial algebra $A[\x_1,\ldots, \x_n]$. Let us examine this situation in a bit more detail.

First, for a natural number $n$ and $\sigma\in S_n$, through the formula

$$\x_i\mapsto \x_{\sigma(i)}$$

we can define an endomorphism of the polynomial ring $A[\x_1,\ldots, \x_n]$. Then we can consider the collection of invariants under this action,

$$A[\x_1,\ldots, \x_n]^{S_n}=\{p\in A[\x_1,\ldots, \x_n]\mid \sigma\cdot p=p\}$$

. First, we can verify that, as an $A$-algebra, these are generated by the elements

$$s_k=\sum_{\substack{H\subseteq \{1,\ldots, n\}\\\lvert H\rvert=k}}\prod_{i\in H} \x_i$$

. Explicitly, they are given by

$$s_0=1,\quad s_1=\sum_{i=1}^n \x_i,\quad s_2=\sum_{1\leq i< j\leq n} \x_i\x_j,\quad \cdots \quad s_n=\x_1\cdots\x_n$$

. Then by induction we can show that $s_1,\ldots, s_n$ are algebraically independent over $A$. That is, satisfying the equation

$$u(s_1,\ldots, s_n)=0$$

, there exists no non-$0$ $u\in A[\x_1,\ldots, \x_n]$. Also, satisfying the formula

$$\x^\nu=\x_1^{\nu(1)}\cdots\x_n^{\nu(n)},\qquad 0\leq\nu(i)< i$$

, one can also verify that the monomials $\x^\nu$ generate, as an $A[\x_1,\ldots, \x_n]^{S_n}$-module, $A[\x_1,\ldots, \x_n]$. A useful identity in this process is the following identity holding in the polynomial ring $A[\x_1,\ldots, \x_n, T_1, T_2]$:

$$\prod_{i=1}^n(T_1+\x_iT_2)=\sum_{k=0}^n T_1^{n-k}T_2^ks_k$$

, which in particular gives the two identities

$$\prod_{i=1}^n(1+\x_iT)=\sum_{k=0}^n s_kT^k,\qquad \prod_{i=1}^n(\x-\x_i)=\sum_{k=0}^n(-1)^{n-k}s_{n-k}\x^k$$

. Here, regarding the second identity as a property similar to the relation between roots and coefficients, for any polynomial

$$f(\x)=\x^n+a_{n-1}\x^{n-1}+\cdots +a_1\x +a_0$$

we can consider the following $A$-algebra:

$$E_f=A[\x_1,\ldots,\x_n]/\mathfrak{a},\qquad \mathfrak{a}=(s_k+(-1)^{k+1}a_{n-k})$$

and then, when extending coefficients from $A$ to $E_f$, $f$ factors completely into a product of linear polynomials. Moreover, $E_f$ is the universal object among $A$-algebras having this property; writing this precisely:

::: Proposition 14
Let arbitrary commutative rings $A,B$ be given, and fix a ring homomorphism $\rho: A \rightarrow B$ and elements $\xi_1,\ldots, \xi_n$ of $B$. If in $B[\x]$ the identity

$$\rho(f)(\x)=\prod_{i=1}^n (\x-\xi_i)$$

holds, then there exists a unique ring homomorphism $u: E_f \rightarrow B$ such that $\rho(a)=u(a.1)$ and $u(\x_i)=\xi_i$.
:::

The $s_k$ treated as generators so far are standardly called *elementary symmetric polynomials* $e_k$. Defining other symmetric polynomials that pair with these makes the structure of the ring of symmetric functions much clearer, and they are used centrally in Schubert calculus of Grassmannians and elsewhere.

::: Definition 15
For a natural number $k$, define the degree-$k$ *complete homogeneous symmetric polynomial* $h_k$ by

$$h_k = \sum_{1 \leq i_1 \leq i_2 \leq \cdots \leq i_k \leq n} \x_{i_1} \x_{i_2} \cdots \x_{i_k}.$$

That is, $h_k$ is the sum of all monomials of degree $k$, with $h_0 = 1$, and if $k < 0$, we set $h_k = 0$.
:::

Paired with the elementary symmetric polynomials being generated by $\prod_{i=1}^n (1 + \x_i T) = \sum_{k=0}^n e_k T^k$, the complete homogeneous symmetric polynomials appear via the generating function

$$\prod_{i=1}^n \frac{1}{1 - \x_i T} = \sum_{k \geq 0} h_k T^k.$$

From the fact that the product of the first generating function with $T$ replaced by $-T$, namely $\prod_{i=1}^n (1 - \x_i T)$, and the second generating function is $1$, the relation connecting $e$ and $h$, $\sum_{j=0}^k (-1)^j e_j h_{k-j} = 0$ ($k \geq 1$), follows, and $h_1, \ldots, h_n$, just like $e_1, \ldots, e_n$, also generate the ring of symmetric polynomials $A[\x_1, \ldots, \x_n]^{S_n}$.

::: Definition 16
For a weakly decreasing sequence of non-negative integers $\lambda = (\lambda_1 \geq \lambda_2 \geq \cdots \geq \lambda_n \geq 0)$ (called a *partition*), define the *Schur polynomial* $s_\lambda$ as the ratio of two alternating polynomials

$$s_\lambda(\x_1, \ldots, \x_n) = \frac{\det\bigl(\x_i^{\lambda_j + n - j}\bigr)_{1 \leq i, j \leq n}}{\det\bigl(\x_i^{n - j}\bigr)_{1 \leq i, j \leq n}}.$$

The denominator is the Vandermonde determinant $\prod_{i < j} (\x_i - \x_j)$, and the numerator is also divisible by the same factors, so $s_\lambda$ is a well-defined polynomial and a symmetric polynomial invariant under permutation of variables.
:::

For example, if $\lambda = (0, \ldots, 0)$, then $s_\lambda = 1$, and when there are $n = 2$ variables and $\lambda = (2,1)$, dividing the numerator $\det\begin{pmatrix} \x_1^3 & \x_1 \\ \x_2^3 & \x_2 \end{pmatrix} = \x_1 \x_2 (\x_1^2 - \x_2^2)$ by the Vandermonde $\x_1 - \x_2$ yields $s_{(2,1)} = \x_1 \x_2 (\x_1 + \x_2)$.

::: Remark 17
Schur polynomials are described in several equivalent ways. First, by the *Jacobi–Trudi identity* using $h_k$ from [Definition 15](#def15){: data-lid="vmzkl" },

$$s_\lambda = \det\bigl(h_{\lambda_i - i + j}\bigr)_{1 \leq i, j \leq \ell}$$

(where $\ell$ is the number of parts of $\lambda$ not equal to $0$). Second, viewing $\lambda$ as a *Young diagram* with, in the $i$-th row, $\lambda_i$ boxes stacked left-aligned, and filling those boxes with values from $\{1, \ldots, n\}$ so that they are weakly increasing along each row and strictly increasing along each column, one also writes, over all *semistandard Young tableaux* $T$,

$$s_\lambda = \sum_T \x_1^{m_1(T)} \cdots \x_n^{m_n(T)}$$

(where $m_i(T)$ is the number of cells in $T$ filled with the value $i$). As special cases, for a single row $\lambda = (k)$ we have $s_{(k)} = h_k$, and for a single column $\lambda = (1^k)$ we have $s_{(1^k)} = e_k$. Furthermore, for $\ell(\lambda) \leq n$, the collection of all $s_\lambda$ forms an $A$-basis of the ring of symmetric polynomials, and expanding their product in this basis as

$$s_\lambda s_\mu = \sum_\nu c_{\lambda\mu}^\nu s_\nu$$

the structure constants $c_{\lambda\mu}^\nu$ are called *Littlewood–Richardson numbers*. For proofs of these equivalences and the basis and multiplication rules, see Macdonald, *Symmetric Functions and Hall Polynomials* (Chapter I) or Fulton, *Young Tableaux*.
:::

---

**References**

**[Bou]** Bourbaki, N. Algebra I. *Elements of Mathematics*. Springer. 1998.
