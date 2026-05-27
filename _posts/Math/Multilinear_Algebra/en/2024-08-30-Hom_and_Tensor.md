---title: "Hom and the Tensor Product"
excerpt: "Adjunction and exactness of the Hom functor and the tensor product"

categories: [Math / Multilinear Algebra]
permalink: /en/math/multilinear_algebra/hom_and_tensor
header:
    overlay_image: /assets/images/Math/Multilinear_Algebra/Hom_and_Tensor.png
    overlay_filter: 0.5
sidebar: 
    nav: "multilinear_algebra-en"

date: 2024-08-30
last_modified_at: 2024-09-23
weight: 5
translated_at: 2026-05-28T11:36:15+00:00
translation_source: kimi-cli
---
In this post we take a closer look at $$\Hom$$ and the tensor product.

## Hom functor

Previously we saw that $$\Hom_{\lMod{A}}(-,N)$$ and $$\Hom_\lMod{A}(M,-)$$ are left exact functors, and we called the modules $$M$$ and $$N$$ that make them exact functors *projective* and *injective* modules, respectively. The following two propositions go in a somewhat different direction, showing that any *splitting* exact sequence remains an exact sequence after applying $$\Hom$$.

<div class="proposition" markdown="1">

<ins id="prop1">**Proposition 1**</ins> Given a splitting exact sequence

$$0 \longrightarrow M \overset{u}{\longrightarrow} L \overset{v}{\longrightarrow} N \rightarrow 0$$

and any $$A$$-module $$K$$, the induced sequence

$$0 \rightarrow \Hom_\lMod{A}(N,K) \rightarrow\Hom_\lMod{A}(L,K) \rightarrow\Hom_\lMod{A}(M,K) \rightarrow 0$$

is a splitting exact sequence. Conversely, if the above sequence is exact for any $$K$$, then the original exact sequence is a splitting exact sequence.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

That the given exact sequence $$0 \rightarrow M \rightarrow L \rightarrow N \rightarrow 0$$ splits is equivalent to the existence of a suitable retraction $$r:L \rightarrow M$$. ([§Exact Sequences, ⁋Proposition 10](/en/math/multilinear_algebra/exact_sequences#prop10)) Now consider

$$\Hom_\lMod{A}(r, \id_K):\Hom_\lMod{A}(M,K) \rightarrow\Hom_\lMod{A}(L,K)$$

From the identity $$r\circ u=\id_M$$ we know that $$\Hom_\lMod{A}(r,\id_K)$$ has a section, and applying [§Exact Sequences, ⁋Proposition 10](/en/math/multilinear_algebra/exact_sequences#prop10) again shows that the second sequence splits.

For the converse, set $$K=M$$ and consider the short exact sequence

$$0 \rightarrow \Hom_\lMod{A}(N,M) \rightarrow \Hom_\lMod{A}(L,M) \rightarrow\Hom_\lMod{A}(M,M) \rightarrow 0$$

Then there exists a suitable $$f\in\Hom_\lMod{A}(L,M)$$ such that $$f\circ u=\id_M$$, so applying [§Exact Sequences, ⁋Proposition 10](/en/math/multilinear_algebra/exact_sequences#prop10) again completes the proof.

</details>

Similarly, the following holds.

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> Given a splitting exact sequence

$$0 \longrightarrow M \overset{u}{\longrightarrow} L \overset{v}{\longrightarrow} N \rightarrow 0$$

and any $$A$$-module $$K$$, the induced sequence

$$0 \rightarrow \Hom_\lMod{A}(K,M) \rightarrow\Hom_\lMod{A}(K,L) \rightarrow\Hom_\lMod{A}(K,N) \rightarrow 0$$

is a splitting exact sequence. Conversely, if the above sequence is exact for any $$K$$, then the original exact sequence is a splitting exact sequence.

</div>

## Homomorphism $$M^\ast\otimes_AN \rightarrow \Hom_{\rMod{A}}(M,N)$$

For convenience, assume that $$A$$ is a commutative ring. Then $$\lMod{A}=\rMod{A}$$, so there is no need to distinguish whether an arbitrary $$A$$-module is a left or right $$A$$-module. In this case, for aesthetic reasons when writing subscripts, we fix $$\rMod{A}$$ as our notation. Now let three $$A$$-modules $$M,N,L$$ be given. Then we can construct the following $$A$$-module homomorphism

$$\nu:\Hom_{\rMod{A}}(M,L)\otimes_A N \rightarrow\Hom_{\rMod{A}}(M,L\otimes_AN)$$

More generally, if $$A,B$$ are rings (not necessarily commutative), $$M$$ is a left $$A$$-module, $$N$$ is a left $$B$$-module, and $$L$$ is an $$(A,B)$$-bimodule, then we can construct the following $$\mathbb{Z}$$-module homomorphism

$$\Hom_{\lMod{A}}(M,L)\otimes_AN \rightarrow \Hom_{\lMod{A}}(M, L\otimes_BN)$$

([\[Bou\] II.4.2]())

First, for any $$u\in\Hom_{\rMod{A}}(M,L)$$ and any $$y\in N$$, the formula

$$x\mapsto u(x)\otimes_Ay$$

defines an $$A$$-linear map from $$M$$ to $$L\otimes_AN$$, and then we can see that the above function sending $$(u,y)\in\Hom_{\rMod{A}}(M,L)\times N$$ to an element of $$\Hom_{\rMod{A}}(M, L\otimes_AB)$$ is $$A$$-balanced. Therefore the above $$A$$-linear map $$\nu$$ is induced.

<div class="proposition" markdown="1">

<ins id="prop3">**Proposition 3**</ins> For $$\nu$$ defined as above, the following hold.

1. If $$N$$ is a projective $$A$$-module, then $$\nu$$ is injective. Also, if $$N$$ is finitely generated projective, then $$\nu$$ is bijective.
2. If $$M$$ is a finitely generated projective $$A$$-module, then $$\nu$$ is bijective.

</div>

In particular, if $$L=A$$, we obtain the following corollary.

<div class="proposition" markdown="1">

<ins id="cor4">**Corollary 4**</ins> Let two arbitrary $$A$$-modules $$M,N$$ be given. If either $$M$$ or $$N$$ is a finitely generated projective $$A$$-module, then there is an isomorphism

$$M^\ast \otimes_AN\cong \Hom_{\rMod{A}}(M,N)$$

</div>

Also, setting $$N=\Hom_{\rMod{A}}(M', L')$$, we obtain the following corollary.

<div class="proposition" markdown="1">

<ins id="cor5">**Corollary 5**</ins> There exists the following $$A$$-linear map

$$\Hom_\rMod{A}(M,L)\otimes_A\Hom_\rMod{A}(M',L') \rightarrow \Hom_\rMod{A}(M\otimes M', L\otimes L')$$

and this is an isomorphism if one of the following pairs

$$(M,M'),\quad (M,L),\quad (M',L')$$

is a finitely generated projective $$A$$-module.

</div>

## Trace

We still assume that $$A$$ is a commutative ring. Then for any $$A$$-module $$M$$,

$$M^\ast\times M \rightarrow A;\qquad (\xi,x) \mapsto \langle x, \xi\rangle$$

is $$A$$-balanced. Therefore this function induces the following $$A$$-linear map

$$\tau: M^\ast\otimes_A M \rightarrow A$$

Now if $$M$$ is a finitely generated projective $$A$$-module, then by [Corollary 4](#cor4) we can identify the left-hand side with $$\End_\rMod{A}(M)=\Hom_\rMod{A}(M,M)$$, and thus a unique $$A$$-linear map from $$\End_\rMod{A}(M)$$ to $$A$$ is defined.

<div class="definition" markdown="1">

<ins id="def6">**Definition 6**</ins> The map defined as above is called the *trace map* and is denoted by $$\tr$$.

</div>

Let an arbitrary $$u\in\End_\rMod{A}(M)$$ be given. After identifying $$\End_\rMod{A}(M)$$ with $$M^\ast\otimes_AM$$, we can choose finitely many $$\xi_i\in M^\ast, x_i\in M$$ and write this as the sum

$$\sum_i \xi_i\otimes_A x_i\tag{1}$$

and the fact that this element corresponds to $$u$$ by [Corollary 4](#cor4) means that the formula

$$u(x)=\sum_i\langle x,\xi_i\rangle x_i\qquad\text{for all $x\in M$}\tag{2}$$

holds. Then by the definition of the trace map,

$$\tr(u)=\sum_i\langle x_i,\xi_i\rangle$$

In general there may be infinitely many pairs $$\xi_i\in M^\ast, x_i\in M$$ satisfying (2), but this is because there are infinitely many ways to represent an element of $$M^\ast\otimes_AM$$ as in (1), and in any case $$\tau:M^\ast\otimes_AM \rightarrow A$$ is well-defined, so $$\tr$$ does not depend on this choice.

Moreover, one can check that $$\tr$$ is an $$A$$-linear map, and furthermore the following holds.

<div class="proposition" markdown="1">

<ins id="prop7">**Proposition 7**</ins> For any two finitely generated projective $$A$$-modules $$M,N$$ and $$A$$-linear maps $$u:M \rightarrow N$$, $$v:N \rightarrow M$$ between them,

$$\tr(u\circ v)=\tr(v\circ u)$$

</div>
