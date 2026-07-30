---
title: "Symmetric Tensors"
description: "We define symmetric tensors and symmetric powers using group actions on modules over group rings, and discuss properties of relative traces and invariance of tensor products under subgroup actions."
excerpt: "Symmetric group actions, symmetric tensors, and symmetric powers"

categories: [Math / Multilinear Algebra]
permalink: /en/math/multilinear_algebra/symmetric_tensors
sidebar: 
    nav: "multilinear_algebra-en"

date: 2025-05-07
weight: 13
translated_at: 2026-07-14T01:00:03+00:00
translation_source: kimi-cli
last_polished_at: 2026-07-14T01:00:03+00:00
---
Given a group $H$ and a ring $A$, we have defined the group ring $AH$. ([[Algebraic Structures] §Algebras, ⁋Definition 5](/en/math/algebraic_structures/algebras#def5)) Now fix an $AH$-module $M$, and define $M^H$ as the set

$$M^H=\left\{x\in M\mid \text{$hx=x$ for all $h\in H$}\right\}.$$

Here $hx$ is of course defined by viewing $h$ as an element of $AH$ via $h\mapsto \delta_h$, then using the $AH$-module structure. Then $M^H$ is an $A$-submodule of $M$, but if $H$ is not commutative, it is generally not an $AH$-submodule. Also, if a subgroup $G$ of $H$ is given, then $M^H\leq M^G$ is obvious.

Now suppose $x\in M^G$ and $h\in H$ are given, and let $\bar{h}=hG$ be an element of $H/G$. Then

$$\bar{h}x=(hG)x=\left\{hx\right\}$$

is obvious, so by a slight abuse of notation we may treat $hx$ and $\bar{h}x$ as the same. Then for any $h'\in H$, the identity

$$h'(\bar{h}x)=(h'\bar{h})x$$

holds.

Now assume that $[H:G]$ is finite. Then $H/G$ is a finite set, so the sum

$$\sum_{\bar{h}\in H/G}\bar{h}x$$

is well-defined. Moreover, this sum is an element of $M^H$, because for any $h'\in H$,

$$h'\left( \sum_{\bar{h}\in H/G}\bar{h}x\right)=\sum_{\bar{h}\in H/G}(h'\bar{h})x=\sum_{\bar{z}\in H/G}\bar{z}x.$$

::: Definition 1
In the above situation, define $\tr_{H/G}:M^G \rightarrow M^H$ by the formula

$$\tr_{H/G}(x)=\sum_{\bar{h}\in H/G} \bar{h}x,$$

and call this the *relative trace*.
:::

Then the following holds.

::: Proposition 2
The following hold.

1. For any $x\in M^G$ and $h\in H$, we have $hx\in M^{hGh^{-1}}$ and the identity $\tr_{H/hGh^{-1}}(hx)=\tr_{H/G}(x)$ holds.
2. For subgroups $F\leq G\leq H$, we have $\tr_{H/G}\circ\tr_{G/F}=\tr_{H/F}$.
3. For any $x\in M^H$, we have $\tr_{H/G}(x)=[H:G].x$.
:::

## Symmetric Tensors

Now we begin the main definitions. First, for any $A$-module $M$, we can define an $S_n$-action on the $n$-th tensor power $\T^n(M)$ by the formula

$$\sigma(x_1\otimes x_2\otimes \cdots\otimes x_n)=x_{\sigma^{-1}(1)}\otimes \cdots\otimes x_{\sigma^{-1}(n)}.$$

::: Definition 3
In the above situation, elements $z\in \T^nM$ satisfying

$$\sigma z=z\qquad\text{for all $\sigma\in S_n$}$$

are called $n$th *symmetric tensors*, and their collection $\Sym^n(M)$ is called the $n$-th *symmetric power*. Their (graded) direct sum is written as

$$\Sym(M)=\bigoplus_{d=0}^\infty \Sym^d(M).$$
:::

$\Sym(M)$ must be distinguished from the symmetric algebra $\S(M)$ defined earlier, but in favorable cases we can show that the two are isomorphic.

First, let us define the product of two symmetric tensors. In general, given two symmetric tensors

$$x=x_1\otimes x_2\otimes \cdots\otimes x_p,\qquad y=y_1\otimes y_2\otimes \cdots\otimes y_q,$$

their product as tensors

$$x\otimes y=x_1\otimes x_2\otimes \cdots\otimes x_p\otimes y_1\otimes y_2\otimes \cdots\otimes y_q$$

is not guaranteed to be a symmetric tensor. Simply consider an element that swaps the positions of some $x_i$ and $y_j$ in the above expression; this may fail to satisfy the symmetric tensor condition.

Instead, the product of the above form is invariant under the action of the subgroup $S_p\times S_q$ of $S_{p+q}$. Therefore, if we define

$$xy=\tr_{S_{p+q}/S_p\times S_q}(x\otimes y)$$

then $xy\in M^{S_{p+q}}$ and its value is

$$\sum_{S_{p+q}/(S_p\times S_q)} \bar{\sigma}(x\otimes y).$$

On the other hand, let $S_{p,q}$ be the subset of $S_{p+q}$ consisting of those $\sigma$ satisfying

$$\sigma(1)<\sigma(2)< \cdots < \sigma(p), \qquad \sigma(p+1)<\sigma(p+2)<\cdots< \sigma(p+q).$$

Then it is not difficult to find a bijection between $S_{p+q}/S_p\times S_q$ and $S_{p,q}$. This is quite natural, because elements of $S_p\times S_q$ are those that fix the image of the automorphism and permute freely within it, while elements of $S_{p,q}$ do the opposite: they freely choose the image of the automorphism but fix the permutation within it. Therefore, the above formula can be rewritten as

$$xy=\sum_{\sigma\in S_{p,q}}\sigma(x\otimes y).$$

::: Proposition 4
For any $A$-module $M$, the following hold.

1. $\Sym(M)$ becomes an associative, commutative unital $A$-algebra under the multiplication defined above.
2. For positive integers $p_1,\ldots, p_n$, the identity
    
    $$x_1x_2\cdots x_n=\tr_{S_{p_1+\cdots+p_n}/S_{p_1}\times\cdots\times S_{p_n}}(x_1\otimes \cdots\otimes x_n)$$

    holds.
:::
::: Proof
Let us show the second claim first. We proceed by induction. For $n=2$ this is the definition, so inductively assume that

$$x_2\cdots x_n=\tr_{S_{p_2+\dots+p_n}/(S_{p_2}\times\cdots\times S_{p_n})}(x_2 \otimes \dots \otimes x_n)$$

holds. Now consider the tower of subgroups of $S_{p_1+\cdots+p_n}$

$$S_{p_1+\cdots+p_n}\geq S_{p_1}\times S_{p_2+\cdots p_n}\geq \left\{\id_{p_1}\right\}\times S_{p_2+\cdots+p_n}.$$

Then by [Proposition 2](#prop2),

$$\tr_{S_{p_1+\cdots +p_n}/S_{p_2+\cdots +p_n}}(x_1\otimes\cdots\otimes x_n)=\tr_{S_{p_1+\cdots+p_n}/(S_{p_1}\times S_{p_2+\cdots+p_n})}\circ\tr_{(S_{p_1}\times S_{p_2+\cdots+p_n})/S_{p_2+\cdots+p_n}}(x_1\otimes\cdots\otimes x_n)$$

holds. Now computing the right-hand side, by the above inclusions,

$$\tr_{(S_{p_1}\times S_{p_2+\cdots+p_n})/S_{p_2+\cdots+p_n}}(x_1\otimes\cdots\otimes x_n)=x_1\otimes\tr_{S_{p_2+\cdots+p_n}/(S_{p_2}\times\cdots\times S_{p_n})}(x_2\otimes\cdots\otimes x_n)=x_1\otimes (x_2\cdots x_n)$$

and therefore

$$\tr_{S_{p_1+\cdots +p_n}/S_{p_2+\cdots +p_n}}(x_1\otimes\cdots\otimes x_n)=\tr_{S_{p_1+\cdots+p_n}/(S_{p_1}\times S_{p_2+\cdots+p_n})}(x_1\otimes (x_2\cdots x_n))=x_1(x_2\cdots x_n)$$

holds. If we had started with the tower of subgroups

$$S_{p_1+\cdots+p_n}\geq S_{p_1+\cdots p_{n-1}}\times S_{p_n}\geq S_{p_1+\cdots p_{n-1}}\times 1,$$

we would have obtained

$$\tr_{S_{p_1+\cdots +p_n}/S_{p_2+\cdots +p_n}}(x_1\otimes\cdots\otimes x_n)=(x_1\cdots x_{n-1})x_n,$$

and in particular for $n=3$ this shows the associativity of $\Sym(M)$. For commutativity, let $\sigma$ be the element of $S_{p_1+p_2}$ that arranges the first $p_1$ elements and the last $p_2$ elements among $p_1+p_2$ elements in the form

$$\underbrace{p_2+1,\cdots p_2+p_1}_\text{\scriptsize$p_1$ elements},\qquad \underbrace{1,\ldots, p_2}_\text{\scriptsize$p_2$ elements}$$

and apply the first result of [Proposition 2](#prop2). The unit is of course $1\in \Sym^0(M)$.
:::

For any $x\in M$ and $k\in \mathbb{N}$, define

$$\gamma_k(x)=\underbrace{x\otimes\cdots\otimes x}_\text{\scriptsize $k$ times}.$$

Then using the above proposition, we obtain the following corollary.

::: Corollary 5
The following hold.

1. The product $x^k$ of $x$ defined in [Proposition 4](#prop4) equals $k!\gamma_k(x)$.
2. For any $x_1,\ldots, x_n\in M$,
    
    $$\gamma_p(x_1+\cdots+x_n)=\sum_{p_1+\cdots+p_n=p}\gamma_{p_1}(x_1)\cdots\gamma_{p_n}(x_n)$$

    holds.
3. For any $x_1,\ldots, x_n\in M$, let $p=p_1+\cdots+p_n$. Let $\mathscr{P}$ be the set of ordered tuples of partitions $\{1,\ldots, p\}=P_1\cup\cdots\cup P_n$ of the set $\{1,\ldots, p\}$,

    $$\mathscr{P}=\left\{(P_1,\ldots, P_n)\bigg\vert \bigcup_{k=1}^n P_k=\{1,\ldots, p\}, P_i\cap P_j=\emptyset\right\}$$

    and for each $P\in\mathscr{P}$ define the function $\phi:\{1,\ldots, p\} \rightarrow \{1,\ldots, n\}$ by $i\in P_{\phi(i)}$. Then

    $$\gamma_{p_1}(x_1)\cdots\gamma_{p_n}(x_n)=\sum_{P\in \mathscr{P}}x_{\phi(1)}\otimes \cdots x_{\phi(p)}$$

    holds.
4. For any $x\in M$ and natural numbers $p,q$, the identity
    
    $$\gamma_p(x)\gamma_q(x)=\frac{(p+q)!}{p!q!}\gamma_{p+q}(x)$$

    holds.
5. Given any $x_1,\ldots, x_n\in M$, and for any subset $H\subseteq \{1,\ldots, n\}$ let $x_H=\sum_{i\in H}x_i$. Then the identity
    
    $$(-1)^nx_1x_2\cdots x_n=\sum_{H\subseteq\{1,\ldots, n\}}(-1)^{\lvert H\rvert}\gamma_n(x_H)$$

    holds.
:::

As in general tensor algebra, our main interest is the case where $M$ is a free $A$-module. First, let us show the following lemma.

::: Lemma 6
For a finite group $H$ and a left $AH$-module $N$, suppose an $H$-invariant $A$-basis $B$ of $N$ is given, and consider the quotient set $\Omega=B/H$ for this action. Then the following hold.

1. For each $\omega\in \Omega$, define $y_\omega=\sum_{b\in\omega}b$; then $(y_\omega)_{\omega\in \Omega}$ is an $A$-basis of $N^H$.
2. A basis for a supplementary submodule of $N^H$ in $N$ is given by the union $B'=\bigcup_{\omega\in\Omega} \omega'$ of the sets $\omega'=\omega\setminus \{z_\omega\}$, where one element is removed from each $\omega\in\Omega$.
:::
::: Proof
First, gathering all the $y_\omega$ and all elements of $B'$, this is merely replacing one element $z_\omega$ of $\omega$ with $y_\omega$, so by simple linear algebra we know this is an $A$-basis of $N$. That is, defining

$$N_1=\sum_{\omega\in\Omega} Ay_\omega,\qquad N_2=\sum_{b'\in B'}Ab'$$

according to the given decomposition, we have $N=N_1\oplus N_2$.

Now what we must show is $N_1=N^H$. By assumption $N_1\subseteq N^H$ is obvious. On the other hand, for any $y\in N^H$, writing $y$ as a linear combination $y=\sum \alpha_b b$ of the $A$-basis $B$, we know that $\alpha_{bh}=\alpha_b$ must hold for all $b\in B$ and all $h\in H$. From this, $y$ must lie in $N_1$.
:::

Then using this, we can show the following proposition.

::: Proposition 7
Suppose $M$ is a free $A$-module and $(e_i)_{i \in I}$ is a basis of $M$.

1. For each $\nu\in\mathbb{N}^{(I)}$, the elements $e_\nu=\prod_{i\in I}\gamma_{\nu_i}(e_i)$ form an $A$-basis of $\Sym(M)$.
2. For any $k$, $\Sym^k(M)$ is an $A$-direct factor of $\T^kM$.
:::
::: Proof
1. Use the second formula of [Corollary 5](#cor5).
2. For each $k$, set $H=S_k$, $N=\T^kM$ and apply [Lemma 6](#lem6).
:::

## Functoriality

For an $A$-module homomorphism $u: M \rightarrow N$,

$$\T(u)\vert_{\Sym(M)}:\Sym(M) \rightarrow \Sym(N)$$

is well-defined. We write $\T(u)\vert_{\Sym(M)}$ simply as $\Sym(u)$. Then we know that $\Sym$ becomes a functor, and moreover from the corresponding properties in [§Tensor Algebra](/en/math/multilinear_algebra/tensor_algebras) we know that the natural isomorphism

$$\bigotimes_{i\in I}\Sym(M_i)\rightarrow \Sym\left(\bigoplus_{i\in I} M_i\right)$$

exists. Then defining $u: M\oplus M \rightarrow M$ by $(x,y)\mapsto x+y$, we know that the composition

$$\Sym(M)\otimes\Sym(M) \rightarrow \Sym(M\oplus M)\overset{\Sym(u)}{\longrightarrow} \Sym(M)$$

sends $x\otimes y$ to $xy$.

## Symmetric Algebra and Symmetric Tensors

Consider the canonical injections $i: M \rightarrow \T(M)$ and $j: M \rightarrow \Sym(M)$. Then by [§Tensor Algebra, ⁋Proposition 2](/en/math/multilinear_algebra/tensor_algebras#prop2), there exists a unique $\mathbb{N}$-graded $A$-algebra homomorphism $s: \T(M)\rightarrow \Sym(M)$ such that $j=s\circ i$. This is the identity on $\T^0(M)=\Sym^0(M)$, and considering how multiplication is defined in $\T(M)$ and $\Sym(M)$ respectively, we know that $s:\T(M) \rightarrow \Sym(M)$ is exactly the *symmetrization*

$$s:\T(M)\rightarrow \Sym(M);\qquad x\mapsto \sum_{\sigma\in S_n}\sigma x.$$

One thing to be somewhat careful about is that even if $x\in\Sym^k(M)\subseteq \T^k(M)$, $s(x)$ does not output $x$ as is, but rather $k!.x$.

::: Remark 8
For the above reason, some references define the symmetric product from the beginning as

$$xy=\frac{1}{p!q!}\tr_{S_{p+q}/(S_p\times S_q)}(x\otimes y).$$

The advantage of doing so is that one no longer needs to worry about such coefficients, but for the above notation to make sense, a $\mathbb{Q}$-vector space structure on $\T(M)$ is needed from the start.

In general, any $A$-module has a $\mathbb{Z}$-module structure (so expressions like $k!.x$ are well-defined regardless of $A$), but a natural $\mathbb{Q}$-action does not exist, so we will stick to the original definition.
:::

For the symmetrization map $s:\T(M) \rightarrow \Sym(M)$ obtained in this way, by [§Tensor Algebra, ⁋Proposition 6](/en/math/multilinear_algebra/tensor_algebras#prop6) we obtain $\bar{s}: \S(M) \rightarrow \Sym(M)$ satisfying

$$s=\bar{s}\circ p,$$

and it is not difficult to check that this is indeed a graded homomorphism. Here $p: \T(M) \rightarrow \S(M)$ is the canonical projection.

On the other hand, $\bar{s}$ also has a map in the opposite direction,

$$t: \Sym(M)\hookrightarrow \T(M)\overset{p}{\longrightarrow}\S(M),$$

and our claim is that in many cases these two maps can be thought of as (almost) inverses of each other.

::: Proposition 9
The following hold.

1. If $x\in \S^n(M)$, then $(t\circ\bar{s})(x)=n!.x$.
2. If $x\in \Sym^n(M)$, then $(\bar{s}\circ t)(x)=n!.x$.
:::

The proof of this is a simple computation.

For a reason similar to what we observed in [Remark 8](#rmk8) above, if $A$ is a $\mathbb{Q}$-algebra (as well as a $\mathbb{Z}$-algebra), then $x\mapsto n!.x$ is a bijection, and thus the $\bar{s}: \S(M) \rightarrow \Sym(M)$ defined above becomes an isomorphism.

## Polynomial Mappings

On the other hand, the symmetric algebra $\S(M)$ could be thought of as a representation of symmetric $n$-linear maps, and thinking of $\Sym(M)$ together via [Proposition 9](#prop9) above, we obtain the following proposition.

::: Proposition 10
Let two $A$-modules $M,N$, a natural number $n$, and $u: M \rightarrow N$ be given. If $M$ is a free $A$-module, then the following are all equivalent.

1. There exists an $n$-linear map $v: M^n \rightarrow N$ satisfying the identity $u(x)=v(x,\ldots, x)$.
2. There exists a linear map $w: \Sym(M) \rightarrow N$ satisfying the identity $u(x)=w(\gamma_n(x))$.
3. There exists a basis $(e_i)_{i\in I}$ of $M$ and a $(\mathbb{N}^{(I)})_n$-indexed family $(y_\nu)$ such that
    
    $$u\left(\sum_{i\in I}\lambda_i e_i\right)=\sum_{\nu\in\mathbb{N}^{(I)})_n}\lambda^\nu y_\nu$$

    holds.
4. For every basis $(e_i)_{i\in I}$ of $M$, a family $(y_\nu)$ satisfying the formula in condition 3 can be found.
:::

We call maps $u: M \rightarrow N$ satisfying these equivalent conditions degree $n$ *homogeneous polynomial mappings*, and write their collection as $\Poly^n(M,N)$. The first and second conditions of the above proposition respectively induce surjections from the collection of $n$-linear maps from $M$ to $N$ onto $\Poly^n(M,N)$, and from $\Hom_A(\Sym^n(M), N)$ onto $\Poly^n(M,N)$; the third and fourth conditions justify the name *polynomial mapping*.

::: Example 11
For an $A$-module $N$, suppose a free $A$-module $A^{(I)}$ is given and fix a polynomial $u\in N[\x_i]_{i\in I}$. Then the map

$$(x_i)_{i\in I} \mapsto u(x_i)\in N$$

is a homogeneous polynomial mapping between $A$-modules, and its degree is $n$.
:::

It is not difficult to show that the composition of two polynomial mappings is again a homogeneous mapping.

::: Proposition 12
Assume all the conditions of [Proposition 10](#prop10), and additionally assume that $y\mapsto n!.y$ is an automorphism of $N$. Then for any $u\in\Poly^n(M,N)$, there exists a *unique* symmetric $n$-linear map $v:M^n \rightarrow N$ satisfying the identity

$$u(x)=v(x,\ldots, x).$$

Moreover, for any $x_1,\ldots, x_n\in M$, explicitly

$$v(x_1,\ldots, x_n)=\frac{1}{n!}\sum_{H\subseteq \{1,\ldots, n\}}(-1)^{\lvert H\rvert}u\left(\sum_{i\in H} x_i\right)$$

holds.
:::

This is a consequence that follows from [Corollary 5](#cor5). Now combining this with the observation in [Remark 8](#rmk8), we obtain the following result.

::: Proposition 13
Assume the situation of [Proposition 10](#prop10), and consider the canonical homomorphism $\Hom_A(\Sym^n(M), N) \rightarrow \Poly^n(M,N)$. Then the following hold.

1. If $A$ is an infinite integral domain and $N$ is torsion-free, then this homomorphism is an isomorphism.
2. If $y\mapsto n!.y$ is an injective endomorphism from $N$ to $N$, then $u$ is an isomorphism.
:::

## Symmetric Functions

On the other hand, when $M$ is a finitely generated free $A$-module, we know that $\S(M)$ is isomorphic to the polynomial algebra $A[\x_1,\ldots, \x_n]$. Let us examine this situation in a bit more detail.

First, for a natural number $n$ and $\sigma\in S_n$, we can define an endomorphism of the polynomial ring $A[\x_1,\ldots, \x_n]$ by the formula

$$\x_i\mapsto \x_{\sigma(i)}.$$

Then we can consider the collection of invariants under this action,

$$A[\x_1,\ldots, \x_n]^{S_n}=\{p\in A[x_1,\ldots, \x_n]\mid \sigma\cdot p=p\}.$$

First, we can verify that these are generated as an $A$-algebra by the elements

$$s_k=\sum_{\substack{H\subseteq \{1,\ldots, n\}\\\lvert H\rvert=k}}\prod_{i\in H} x_i.$$

Explicitly,

$$s_0=1,\quad s_1=\sum_{i=1}^n \x_i,\quad s_2=\sum_{1\leq i< j\leq n} \x_i\x_j,\quad \cdots \quad s_n=\x_1\cdots\x_n.$$

Then by induction we can show that the $s_i$ are algebraically independent over $A$. That is, there is no $u\in A[\x_0,\ldots, \x_n]$ satisfying the identity

$$u(s_0,\ldots, s_n)=0.$$

Also, we can verify that the monomials $\x^\nu$ satisfying

$$\x^\nu=\x_1^{\nu(1)}\cdots\x_n^{\nu(n)},\qquad 0\leq\nu(i)< i$$

generate $A[\x_1,\ldots, \x_n]$ as an $A[\x_1,\ldots, \x_n]^{S_n}$-module. A useful identity in this process is the following identity that holds in the polynomial ring $A[\x_1,\ldots, \x_n, T_1, T_2]$:

$$\prod_{i=1}^n(T_1+\x_iT_2)=\sum_{k=0}^n T_1^{n-k}T_2^ks_k,$$

which in particular gives the two identities

$$\prod_{i=1}^n(1+\x_iT)=\sum_{k=0}^n s_kT^k,\qquad \prod_{i=1}^n(\x-\x_i)=\sum_{k=0}^n(-1)^{n-k}s_{n-k}\x^k.$$

Thinking of the second identity as a property similar to the relationship between roots and coefficients, for any polynomial

$$f(\x)=\x^n+a_{n-1}\x^{n-1}+\cdots +a_1\x +a_0$$

we can consider the $A$-algebra

$$E_f=A[\x_1,\ldots,\x_n]/\mathfrak{a},\qquad \mathfrak{a}=(s_k+(-1)^{k+1}a_k),$$

and then $f$, extending coefficients from $A$ to $E_f$, factors completely into a product of linear terms. Moreover, $E_f$ is the universal object among $A$-algebras with this property; writing this precisely:

::: Proposition 14
Let arbitrary commutative rings $A,B$ be given, and fix a ring homomorphism $\rho: A \rightarrow B$ and elements $\xi_1,\ldots, \xi_n$ of $B$. If the identity

$$\rho(f)(\x)=\prod_{i=1}^n (\x-\xi_i)$$

holds in $B[\x]$, then there exists a unique ring homomorphism $u: E_f \rightarrow B$ such that $\rho(a)=u(a.1)$ and $u(\x_i)=\xi_i$.
:::

The $s_k$ we have treated as generators are standardly called *elementary symmetric polynomials* $e_k$. Defining other symmetric polynomials that pair with these makes the structure of the ring of symmetric functions much clearer, and they are used centrally in Schubert calculus of Grassmannians and elsewhere.

::: Definition 15
For a natural number $k$, define the $k$-th *complete homogeneous symmetric polynomial* $h_k$ by

$$h_k = \sum_{1 \leq i_1 \leq i_2 \leq \cdots \leq i_k \leq n} \x_{i_1} \x_{i_2} \cdots \x_{i_k}.$$

That is, $h_k$ is the sum of all monomials of degree $k$, with $h_0 = 1$, and we agree that $h_k = 0$ for $k < 0$.
:::

Paired with the elementary symmetric polynomial generated by $\prod_{i=1}^n (1 + \x_i T) = \sum_{k=0}^n e_k T^k$, the complete homogeneous symmetric polynomials are represented by the generating function

$$\prod_{i=1}^n \frac{1}{1 - \x_i T} = \sum_{k \geq 0} h_k T^k.$$

From the fact that the product of the two generating functions is $1$, the relation $\sum_{j=0}^k (-1)^j e_j\, h_{k-j} = 0$ ($k \geq 1$) connecting $e$ and $h$ follows, and $h_1, \ldots, h_n$ also generate the ring of symmetric polynomials $A[\x_1, \ldots, \x_n]^{S_n}$, just as $e_1, \ldots, e_n$ do.

::: Definition 16
For a weakly decreasing sequence of non-negative integers $\lambda = (\lambda_1 \geq \lambda_2 \geq \cdots \geq \lambda_n \geq 0)$ — called a *partition* — define the *Schur polynomial* $s_\lambda$ as the ratio of two alternating polynomials

$$s_\lambda(\x_1, \ldots, \x_n) = \frac{\det\bigl(\x_i^{\lambda_j + n - j}\bigr)_{1 \leq i, j \leq n}}{\det\bigl(\x_i^{n - j}\bigr)_{1 \leq i, j \leq n}}.$$

The denominator is the Vandermonde determinant $\prod_{i < j} (\x_i - \x_j)$, and the numerator is also divisible by the same factors, so $s_\lambda$ is a well-defined polynomial and a symmetric polynomial invariant under permutation of variables.
:::

For example, if $\lambda = (0, \ldots, 0)$ then $s_\lambda = 1$, and if there are $n = 2$ variables and $\lambda = (2,1)$, then dividing the numerator $\det\begin{pmatrix} \x_1^3 & \x_1 \\ \x_2^3 & \x_2 \end{pmatrix} = \x_1 \x_2 (\x_1^2 - \x_2^2)$ by the Vandermonde $\x_1 - \x_2$ gives $s_{(2,1)} = \x_1 \x_2 (\x_1 + \x_2)$.

::: Remark 17
Schur polynomials are described in several equivalent ways. First, by the *Jacobi–Trudi identity* using the $h_k$ from [Definition 15](#def15),

$$s_\lambda = \det\bigl(h_{\lambda_i - i + j}\bigr)_{1 \leq i, j \leq \ell}$$

(where $\ell$ is the number of non-zero parts of $\lambda$). Second, viewing $\lambda$ as a *Young diagram* with $\lambda_i$ boxes left-justified in the $i$-th row, and summing over all *semistandard Young tableaux* $T$ filled with values from $\{1, \ldots, n\}$ that are weakly increasing along each row and strictly increasing along each column,

$$s_\lambda = \sum_T \x_1^{m_1(T)} \cdots \x_n^{m_n(T)}$$

(where $m_i(T)$ is the number of times the value $i$ appears in $T$). As special cases, for a single row $\lambda = (k)$ we have $s_{(k)} = h_k$, and for a single column $\lambda = (1^k)$ we have $s_{(1^k)} = e_k$. Moreover, the set of all $s_\lambda$ with $\ell(\lambda) \leq n$ forms an $A$-basis of the ring of symmetric polynomials, and the structure constants

$$s_\lambda\, s_\mu = \sum_\nu c_{\lambda\mu}^\nu\, s_\nu$$

in the expansion of their product in this basis are called *Littlewood–Richardson numbers*. For proofs of these equivalences and the basis/multiplication rules, see Macdonald, *Symmetric Functions and Hall Polynomials* (Chapter I) or Fulton, *Young Tableaux*.
:::

---

**References**

**[Bou]** Bourbaki, N. Algebra I. *Elements of Mathematics*. Springer. 1998.
