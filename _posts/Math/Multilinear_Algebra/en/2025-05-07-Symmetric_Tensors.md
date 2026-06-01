---
title: "Symmetric Tensors"
description: "We define symmetric tensors and symmetric powers via group actions on modules over group rings, and discuss the properties of relative traces and the invariance of tensor products under subgroup actions."
excerpt: "The action of the symmetric group, symmetric tensors, and symmetric powers"

categories: [Math / Multilinear Algebra]
permalink: /en/math/multilinear_algebra/symmetric_tensors
header:
    overlay_image: /assets/images/Math/Multilinear_Algebra/Symmetric_Tensors.png
    overlay_filter: 0.5
sidebar: 
    nav: "multilinear_algebra-en"

date: 2025-05-07
last_modified_at: 2025-05-07
weight: 201
translated_at: 2026-06-01T20:00:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-01T20:00:02+00:00
---
Given any group $$H$$ and ring $$A$$, we defined the group ring $$AH$$. ([\[Algebraic Structures\] §Algebras, ⁋Definition 5](/en/math/algebraic_structures/algebras#def5)) Now fix an $$AH$$-module $$M$$, and define $$M^H$$ as the set

$$M^H=\left\{x\in M\mid \text{$hx=x$ for all $h\in H$}\right\}$$

where $$hx$$ is, of course, defined by viewing $$h$$ as an element of $$AH$$ via $$h\mapsto \delta_h$$ and then using the $$AH$$-module structure. Then $$M^H$$ is an $$A$$-submodule of $$M$$, but if the group $$H$$ is not commutative, it is generally not an $$AH$$-submodule. Also, if a subgroup $$G$$ of $$H$$ is given, it is obvious that $$M^H\leq M^G$$.

Now let $$x\in M^G$$ and $$h\in H$$ be given, and let $$\bar{h}=hG$$ be an element of $$H/G$$. Then since it is obvious that

$$\bar{h}x=(hG)x=\left\{hx\right\}$$

by a slight abuse of notation we may treat $$hx$$ and $$\bar{h}x$$ as the same. Then for any $$h'\in H$$, the formula

$$h'(\bar{h}x)=(h'\bar{h})x$$

holds.

Now assume that $$[H:G]$$ is finite. Then $$H/G$$ is a finite set, and so the sum

$$\sum_{\bar{h}\in H/G}\bar{h}x$$

is well defined. Moreover this sum is an element of $$M^H$$, because for any $$h'\in H$$,

$$h'\left( \sum_{\bar{h}\in H/G}\bar{h}x\right)=\sum_{\bar{h}\in H/G}(h'\bar{h})x=\sum_{\bar{z}\in H/G}\bar{z}x$$

holds.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> In the above situation, define $$\tr_{H/G}:M^G \rightarrow M^H$$ by the formula

$$\tr_{H/G}(x)=\sum_{\bar{h}\in H/G} \bar{h}x$$

and call it the *relative trace*.

</div>

Then the following holds.

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> The following hold.

1. For any $$x\in M^G$$ and $$h\in H$$, we have $$hx\in M^{hGh^{-1}}$$ and the formula $$\tr_{H/hGh^{-1}}(hx)=\tr_{H/G}(x)$$ holds.
2. For subgroups $$F\leq G\leq H$$, we have $$\tr_{H/G}\circ\tr_{G/F}=\tr_{H/F}$$.
3. For any $$x\in M^H$$, we have $$\tr_{H/G}(x)=[H:G].x$$.

</div>

## Symmetric Tensors

Now we begin the main definitions. First, for any $$A$$-module $$M$$, we can define an $$S_n$$-action on the $$n$$-th tensor power $$\T^n(M)$$ by the formula

$$\sigma(x_1\otimes x_2\otimes \cdots\otimes x_n)=x_{\sigma^{-1}(1)}\otimes \cdots\otimes x_{\sigma^{-1}(n)}$$

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> In the above situation, elements $$z\in \T^nM$$ satisfying

$$\sigma z=z\qquad\text{for all $\sigma\in S_n$}$$

are called $$n$$th *symmetric tensors*, and their set $$\Sym^n(M)$$ is called the $$n$$-th *symmetric power*. Their (graded) direct sum is written as

$$\Sym(M)=\bigoplus_{d=0}^\infty \Sym^d(M)$$

</div>

$$\Sym(M)$$ must be distinguished from the symmetric algebra $$\S(M)$$ defined earlier, but in good cases we can show that the two are isomorphic.

First let us define the product of two symmetric tensors. In general, given any two symmetric tensors

$$x=x_1\otimes x_2\otimes \cdots\otimes x_p,\qquad y=y_1\otimes y_2\otimes \cdots\otimes y_q$$

their product as tensors

$$x\otimes y=x_1\otimes x_2\otimes \cdots\otimes x_p\otimes y_1\otimes y_2\otimes \cdots\otimes y_q$$

need not be a symmetric tensor. Simply consider an element that interchanges the positions of an $$x_i$$ and a $$y_j$$ in the above form to see that it may fail to satisfy the symmetric tensor condition.

Instead, a product of the above form is invariant under the action of the subgroup $$S_p\times S_q$$ of $$S_{p+q}$$. Therefore, defining

$$xy=\tr_{S_{p+q}/S_p\times S_q}(x\otimes y)$$

we have $$xy\in M^{S_{p+q}}$$ and its value is

$$\sum_{\bar{\sigma}\in S_{p+q}/(S_p\times S_q)} \bar{\sigma}(x\otimes y)$$

. On the other hand, let $$S_{p,q}$$ be the subset of $$S_{p+q}$$ consisting of those $$\sigma$$ satisfying

$$\sigma(1)<\sigma(2)< \cdots < \sigma(p), \qquad \sigma(p+1)<\sigma(p+2)<\cdots< \sigma(p+q)$$

; then it is not hard to find a bijection between $$S_{p+q}/S_p\times S_q$$ and $$S_{p,q}$$. This is quite natural, because elements of $$S_p\times S_q$$ are those that fix the image of the automorphism and then permute freely within it, whereas elements of $$S_{p,q}$$ are, conversely, those that choose the image of the automorphism freely but fix the permutation within it. Therefore the above formula can again be written as

$$xy=\sum_{\sigma\in S_{p,q}}\sigma(x\otimes y)$$

.

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4**</ins> For any $$A$$-module $$M$$, the following hold.

1. $$\Sym(M)$$ becomes an associative, commutative unital $$A$$-algebra under the multiplication defined above.
2. For positive integers $$p_1,\ldots, p_n$$, the formula
    
    $$x_1x_2\cdots x_n=\tr_{S_{p_1+\cdots+p_n}/S_{p_1}\times\cdots\times S_{p_n}}(x_1\otimes \cdots\otimes x_n)$$

    holds.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Let us prove the second claim first. We proceed by induction. The case $$n=2$$ is the definition, so assume inductively that

$$x_2\cdots x_n=\tr_{S_{p_2+\dots+p_n}/(S_{p_2}\times\cdots\times S_{p_n})}(x_2 \otimes \dots \otimes x_n)$$

holds. Now consider the tower of subgroups of $$S_{p_1+\cdots+p_n}$$

$$S_{p_1+\cdots+p_n}\geq S_{p_1}\times S_{p_2+\cdots p_n}\geq \left\{\id_{p_1}\right\}\times S_{p_2+\cdots+p_n}$$

Then by [Proposition 2](#prop2),

$$\tr_{S_{p_1+\cdots +p_n}/S_{p_2+\cdots +p_n}}(x_1\otimes\cdots\otimes x_n)=\tr_{S_{p_1+\cdots+p_n}/(S_{p_1}\times S_{p_2+\cdots+p_n})}\circ\tr_{(S_{p_1}\times S_{p_2+\cdots+p_n})/S_{p_2+\cdots+p_n}}(x_1\otimes\cdots\otimes x_n)$$

holds. Computing the right-hand side, by the above inclusion we have

$$\tr_{(S_{p_1}\times S_{p_2+\cdots+p_n})/S_{p_2+\cdots+p_n}}(x_1\otimes\cdots\otimes x_n)=x_1\otimes\tr_{S_{p_2+\cdots+p_n}/(S_{p_2}\times\cdots\times S_{p_n})}(x_2\otimes\cdots\otimes x_n)=x_1\otimes (x_2\cdots x_n)$$

and therefore

$$\tr_{S_{p_1+\cdots +p_n}/S_{p_2+\cdots +p_n}}(x_1\otimes\cdots\otimes x_n)=\tr_{S_{p_1+\cdots+p_n}/(S_{p_1}\times S_{p_2+\cdots+p_n})}(x_1\otimes (x_2\cdots x_n))=x_1(x_2\cdots x_n)$$

holds. If we had started with the tower of subgroups

$$S_{p_1+\cdots+p_n}\geq S_{p_1+\cdots p_{n-1}}\times S_{p_n}\geq S_{p_1+\cdots p_{n-1}}\times 1$$

we would obtain

$$\tr_{S_{p_1+\cdots +p_n}/S_{p_2+\cdots +p_n}}(x_1\otimes\cdots\otimes x_n)=(x_1\cdots x_{n-1})x_n$$

and in particular for $$n=3$$ this shows the associativity of $$\Sym(M)$$. For commutativity, using a $$\sigma\in S_{p_1+p_2}$$ that arranges the first $$p_1$$ elements and the last $$p_2$$ elements among the $$p_1+p_2$$ elements in the form

$$\underbrace{p_2+1,\cdots p_2+p_1}_\text{\scriptsize$p_1$ elements},\qquad \underbrace{1,\ldots, p_2}_\text{\scriptsize$p_2$ elements}$$

and applying the first result of [Proposition 2](#prop2) suffices. The unit is of course $$1\in \Sym^0(M)$$.

</details>

For any $$x\in M$$ and $$k\in \mathbb{N}$$, define

$$\gamma_k(x)=\underbrace{x\otimes\cdots\otimes x}_\text{\scriptsize $k$ times}$$

. Then using the above proposition we obtain the following corollary.

<div class="proposition" markdown="1">

<ins id="cor5">**Corollary 5**</ins> The following hold.

1. The product $$x^k$$ of $$x$$ defined in [Proposition 4](#prop4) equals $$k!\gamma_k(x)$$. 
2. For any $$x_1,\ldots, x_n\in M$$,
    
    $$\gamma_p(x_1+\cdots+x_n)=\sum_{p_1+\cdots+p_n=p}\gamma_{p_1}(x_1)\cdots\gamma_{p_n}(x_n)$$

    holds. 
3. For any $$x_1,\ldots, x_n\in M$$, let $$p=p_1+\cdots+p_n$$. Then letting $$\mathscr{P}$$ be the set of ordered tuples $$(P_1,\ldots, P_n)$$ of partitions of $$\{1,\ldots, p\}$$ such that

    $$\mathscr{P}=\left\{(P_1,\ldots, P_n)\bigg| \bigcup_{k=1}^n P_k=\{1,\ldots, p\}, P_i\cap P_j=\emptyset\right\}$$

    and for each $$P\in\mathscr{P}$$ defining a function $$\phi:\{1,\ldots, p\} \rightarrow \{1,\ldots, n\}$$ such that $$i\in P_{\phi(i)}$$, we have

    $$\gamma_{p_1}(x_1)\cdots\gamma_{p_n}(x_n)=\sum_{P\in \mathscr{P}}x_{\phi(1)}\otimes \cdots \otimes x_{\phi(p)}$$

    . 
4. For any $$x\in M$$ and natural numbers $$p,q$$, the formula
    
    $$\gamma_p(x)\gamma_q(x)=\frac{(p+q)!}{p!q!}\gamma_{p+q}(x)$$

    holds.
5. Let $$x_1,\ldots, x_n\in M$$ be given, and for any subset $$H\subseteq \{1,\ldots, n\}$$ let $$x_H=\sum_{i\in H}x_i$$. Then the formula
    
    $$(-1)^nx_1x_2\cdots x_n=\sum_{H\subset\{1,\ldots, n\}}(-1)^{\lvert H\rvert}\gamma_n(x_H)$$

    holds. 

</div>

As in the general tensor algebra, we are particularly interested in the case where $$M$$ is a free $$A$$-module. First let us prove the following lemma.

<div class="proposition" markdown="1">

<ins id="lem6">**Lemma 6**</ins> For a finite group $$H$$ and a left $$AH$$-module $$N$$, suppose that an $$H$$-invariant $$A$$-basis $$B$$ of $$N$$ is given, and consider the quotient set $$\Omega=B/H$$ for this action. Then the following hold.

1. If for each $$\omega\in \Omega$$ we define $$y_\omega=\sum_{b\in\omega}b$$, then $$(y_\omega)_{\omega\in \Omega}$$ is an $$A$$-basis of $$N^H$$. 
2. A basis of a supplementary submodule of $$N^H$$ in $$N$$ is given by the union $$B'=\bigcup_{\omega\in\Omega} \omega'$$ of the sets $$\omega'=\omega\setminus \{z_\omega\}$$, each obtained from $$\omega\in\Omega$$ by removing one element.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, gathering all the $$y_\omega$$ and the elements of $$B'$$ merely replaces one element $$z_\omega$$ from each $$\omega$$ with $$y_\omega$$, so by elementary linear algebra we know that this is an $$A$$-basis of $$N$$. That is, defining

$$N_1=\sum_{\omega\in\Omega} Ay_\omega,\qquad N_2=\sum_{b'\in B'}Ab'$$

we have $$N=N_1\oplus N_2$$.

Now we must show that $$N_1=N^H$$. By assumption $$N_1\subset N^H$$ is obvious. On the other hand, for any $$y\in N^H$$, writing $$y$$ as a linear combination $$y=\sum \alpha_b b$$ in the $$A$$-basis $$B$$, we know that $$\alpha_{bh}=\alpha_b$$ must hold for all $$b\in B$$ and all $$h\in H$$. From this it follows that $$y\in N_1$$.

</details>

Then using this we can prove the following proposition.

<div class="proposition" markdown="1">

<ins id="prop7">**Proposition 7**</ins> Suppose that $$M$$ is a free $$A$$-module and $$(e_i)_{i \in I}$$ is a basis of $$M$$.

1. For each $$\nu\in\mathbb{N}^{(I)}$$, the elements $$e_\nu=\prod_{i\in I}\gamma_{\nu_i}(e_i)$$ form an $$A$$-basis of $$\Sym(M)$$.
2. For any $$k$$, $$\Sym^k(M)$$ is an $$A$$-direct factor of $$\T^kM$$. 

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

1. This follows from the second formula of [Corollary 5](#cor5).
2. For each $$k$$, set $$H=S_k$$ and $$N=\T^kM$$ and apply [Lemma 6](#lem6). 

</details>

## Functoriality

For an $$A$$-module homomorphism $$u: M \rightarrow N$$,

$$\T(u)\vert_{\Sym(M)}:\Sym(M) \rightarrow \Sym(N)$$

is well defined. We write $$\T(u)\vert_{\Sym(M)}$$ simply as $$\Sym(u)$$. Then we know that $$\Sym$$ becomes a functor, and moreover from the corresponding properties in [§Tensor Algebras](/en/math/multilinear_algebra/tensor_algebras) we know that the natural isomorphism

$$\bigotimes_{i\in I}\Sym(M_i)\rightarrow \Sym\left(\bigoplus_{i\in I} M_i\right)$$

exists. Then defining $$u: M\oplus M \rightarrow M$$ by $$(x,y)\mapsto x+y$$, we know that the composition

$$\Sym(M)\otimes\Sym(M) \rightarrow \Sym(M\oplus M)\overset{\Sym(u)}{\longrightarrow} \Sym(M)$$

sends $$x\otimes y$$ to $$xy$$.

## Symmetric Algebra and Symmetric Tensors

Consider the canonical injections $$i: M \rightarrow \T(M)$$ and $$j: M \rightarrow \Sym(M)$$. Then by [§Tensor Algebras, ⁋Proposition 2](/en/math/multilinear_algebra/tensor_algebras#prop2), there exists a unique $$\mathbb{N}$$-graded $$A$$-algebra homomorphism $$s: \T(M)\rightarrow \Sym(M)$$ such that $$j=s\circ i$$. Then this is the identity on $$\T^0(M)=\Sym^0(M)$$, and considering how multiplication is defined in $$\T(M)$$ and $$\Sym(M)$$, we see that $$s:\T(M) \rightarrow \Sym(M)$$ is exactly the *symmetrization*

$$s:\T(M)\rightarrow \Sym(M);\qquad x\mapsto \sum_{\sigma\in S_n}\sigma x$$

. One thing to be careful about is that even if $$x\in\Sym^k(M)\subseteq \T^k(M)$$, $$s(x)$$ is not $$x$$ itself but $$k!.x$$.

<div class="remark" markdown="1">

<ins id="rmk1">**Remark**</ins> For the above reason, some references define the symmetric product from the beginning as

$$xy=\frac{1}{p!q!}\tr_{S_{p+q}/(S_p\times S_q)}(x\otimes y)$$

. The advantage of doing so is that one no longer needs to worry about such coefficients, but for the above notation to make sense there must be a $$\mathbb{Q}$$-vector space structure on $$\T(M)$$ from the start.

In general, any $$A$$-module has a $$\mathbb{Z}$$-module structure (so expressions such as $$k!.x$$ are well defined regardless of $$A$$), but a natural $$\mathbb{Q}$$-action does not exist, so we shall stick with the original definition.

</div>

For the symmetrization map $$s:\T(M) \rightarrow \Sym(M)$$ obtained in this way, by [§Tensor Algebras, ⁋Proposition 6](/en/math/multilinear_algebra/tensor_algebras#prop6) we obtain an $$\bar{s}: \S(M) \rightarrow \Sym(M)$$ satisfying

$$s=\bar{s}\circ p$$

, and it is not hard to check that this is indeed a graded homomorphism. Here $$p: \T(M) \rightarrow \S(M)$$ is the canonical projection.

On the other hand, $$\bar{s}$$ also has a map in the opposite direction

$$t: \Sym(M)\hookrightarrow \T(M)\overset{p}{\longrightarrow}\S(M)$$

, and our claim is that in many cases these two maps can be regarded as (almost) inverses of each other.

<div class="proposition" markdown="1">

<ins id="prop8">**Proposition 8**</ins> The following hold.

1. If $$x\in \S^n(M)$$, then $$(t\circ\bar{s})(x)=n!.x$$.
2. If $$x\in \Sym^n(M)$$, then $$(\bar{s}\circ t)(x)=n!.x$$. 

</div>

The proof of this is a simple calculation.

For reasons similar to what we saw in [Remark](#rmk1) above, if $$A$$ is a $$\mathbb{Q}$$-algebra (as well as a $$\mathbb{Z}$$-algebra), then $$x\mapsto n!.x$$ is a bijection, and thus we can check that the $$\bar{s}: \S(M) \rightarrow \Sym(M)$$ defined above is an isomorphism.

## Polynomial Mappings

On the other hand, the symmetric algebra $$\S(M)$$ could be thought of as a representation of symmetric $$n$$-linear maps; considering $$\Sym(M)$$ together with [Proposition 8](#prop8) above, we obtain the following proposition.

<div class="proposition" markdown="1">

<ins id="prop9">**Proposition 9**</ins> Let two $$A$$-modules $$M,N$$, a natural number $$n$$, and $$u: M \rightarrow N$$ be given. If $$M$$ is a free $$A$$-module, then the following are all equivalent.

1. There exists an $$n$$-linear map $$v: M^n \rightarrow N$$ satisfying $$u(x)=v(x,\ldots, x)$$.
2. There exists a linear map $$w: \Sym(M) \rightarrow N$$ satisfying $$u(x)=w(\gamma_n(x))$$.
3. There exist a basis $$(e_i)_{i\in I}$$ of $$M$$ and an $$(\mathbb{N}^{(I)})_n$$-indexed family $$(y_\nu)$$ such that
    
    $$u\left(\sum_{i\in I}\lambda_i e_i\right)=\sum_{\nu\in(\mathbb{N}^{(I)})_n}\lambda^\nu y_\nu$$

    . 
4. For every basis $$(e_i)_{i\in I}$$ of $$M$$, one can find a family $$(y_\nu)$$ satisfying the formula in condition 3.

</div>

Then maps $$u: M \rightarrow N$$ satisfying these equivalent conditions are called degree $$n$$ *homogeneous polynomial mappings*, and their set is written as $$\Poly^n(M,N)$$. The first and second conditions of the above proposition induce surjections onto $$\Poly^n(M,N)$$ from the set of $$n$$-linear maps from $$M$$ to $$N$$ and from $$\Hom_A(\Sym^n(M), N)$$, respectively, while the third and fourth conditions justify the name *polynomial mapping*.

<div class="example" markdown="1">

<ins id="ex10">**Example 10**</ins> Let a free $$A$$-module $$A^{(I)}$$ and a polynomial $$u\in N[\x_i]_{i\in I}$$ be given. Then the formula

$$(x_i)_{i\in I} \mapsto u(x_i)\in N$$

is a homogeneous polynomial mapping of $$A$$-modules, and its degree is $$n$$.

</div>

It is not hard to show that the composition of two polynomial mappings is again a homogeneous mapping.

<div class="proposition" markdown="1">

<ins id="prop11">**Proposition 11**</ins> Assume all the conditions of [Proposition 9](#prop9) and additionally assume that $$y\mapsto n!.y$$ is an automorphism of $$N$$. Then for any $$u\in\Poly^n(M,N)$$, there exists a *unique* symmetric $$n$$-linear map $$v:M^n \rightarrow N$$ satisfying

$$u(x)=v(x,\ldots, x)$$

. Moreover, for any $$x_1,\ldots, x_n\in M$$, explicitly

$$v(x_1,\ldots, x_n)=\frac{1}{n!}\sum_{H\subseteq \{1,\ldots, n\}}(-1)^{\lvert H\rvert}u\left(\sum_{i\in H} x_i\right)$$

holds.

</div>

This follows from [Corollary 5](#cor5). Combining this with the observation in [Remark](#rmk1), we obtain the following result.

<div class="proposition" markdown="1">

<ins id="prop12">**Proposition 12**</ins> Assume the situation of [Proposition 9](#prop9), and consider the canonical homomorphism $$\Hom_A(\Sym^n(M), N) \rightarrow \Poly^n(M,N)$$. Then the following hold.

1. If $$A$$ is an infinite integral domain and $$N$$ is torsion-free, then this homomorphism is an isomorphism.
2. If $$y\mapsto n!.y$$ is an injective endomorphism from $$N$$ to $$N$$, then this homomorphism is an isomorphism.

</div>

## Symmetric Functions

On the other hand, we know that when $$M$$ is a finitely generated free $$A$$-module, $$\S(M)$$ is isomorphic to the polynomial algebra $$A[\x_1,\ldots, \x_n]$$. Let us examine this situation in a little more detail.

First, for a natural number $$n$$ and $$\sigma\in S_n$$, we can define an endomorphism of the polynomial ring $$A[\x_1,\ldots, \x_n]$$ by the formula

$$\x_i\mapsto \x_{\sigma(i)}$$

. Then the set of invariants for this action

$$A[\x_1,\ldots, \x_n]^{S_n}=\{p\in A[\x_1,\ldots, \x_n]\mid \sigma\cdot p=p\}$$

can be considered. First we can check that they are generated as an $$A$$-algebra by the elements

$$s_k=\sum_{\substack{H\subset \{1,\ldots, n\}\\\lvert H\rvert=k}}\prod_{i\in H} \x_i$$

. Explicitly,

$$s_0=1,\quad s_1=\sum_{i=1}^n \x_i,\quad s_2=\sum_{1\leq i< j\leq n} \x_i\x_j,\quad \cdots \quad s_n=\x_1\cdots\x_n$$

. Then by induction we can show that the $$s_i$$ are algebraically independent over $$A$$. That is, there is no nonzero $$u\in A[\x_0,\ldots, \x_n]$$ satisfying

$$u(s_0,\ldots, s_n)=0$$

. Also, one can check that the monomials $$\x^\nu$$ satisfying

$$\x^\nu=\x_1^{\nu(1)}\cdots\x_n^{\nu(n)},\qquad 0\leq\nu(i)< i$$

generate $$A[\x_1,\ldots, \x_n]$$ as an $$A[\x_1,\ldots, \x_n]^{S_n}$$-module. A useful formula in this process is the following identity in the polynomial ring $$A[\x_1,\ldots, \x_n, T_1, T_2]$$:

$$\prod_{i=1}^n(T_1+\x_iT_2)=\sum_{k=0}^n T_1^{n-k}T_2^k s_k$$

, which in particular gives the two formulas

$$\prod_{i=1}^n(1+\x_iT)=\sum_{k=0}^n s_kT^k,\qquad \prod_{i=1}^n(\x-\x_i)=\sum_{k=0}^n(-1)^{n-k}s_{n-k}\x^k$$

. Thinking of the second formula as a property similar to the relation between roots and coefficients, for any polynomial

$$f(\x)=\x^n+a_{n-1}\x^{n-1}+\cdots +a_1\x +a_0$$

we can consider the $$A$$-algebra

$$E_f=A[\x_1,\ldots,\x_n]/\mathfrak{a},\qquad \mathfrak{a}=(s_k+(-1)^{k+1}a_k)$$

; then $$f$$, upon extending coefficients from $$A$$ to $$E_f$$, factors completely into a product of linear terms. Moreover $$E_f$$ is universal among $$A$$-algebras with this property, which can be written precisely as follows.

<div class="proposition" markdown="1">

<ins id="prop13">**Proposition 13**</ins> Let arbitrary commutative rings $$A,B$$ be given, and fix a ring homomorphism $$\rho: A \rightarrow B$$ and elements $$\xi_1,\ldots, \xi_n$$ of $$B$$. If in $$B[\x]$$ the formula

$$\rho(f)(\x)=\prod_{i=1}^n (\x-\xi_i)$$

holds, then there exists a unique ring homomorphism $$u: E_f \rightarrow B$$ such that $$\rho(a)=u(a\cdot 1)$$ and $$u(\x_i)=\xi_i$$.

</div>
