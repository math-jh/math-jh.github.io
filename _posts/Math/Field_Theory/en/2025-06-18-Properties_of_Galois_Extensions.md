---
title: "Properties of Galois Groups"
description: "This post explains how to equip Galois groups with a topological structure, and describes the correspondence between the lattice of subgroups and the lattice of intermediate extensions."
excerpt: "Structure of infinite Galois groups with the Krull topology"

categories: [Math / Field Theory]
permalink: /en/math/field_theory/properties_of_galois_extensions
sidebar: 
    nav: "field_theory-en"

date: 2025-06-18
last_modified_at: 2025-06-18
weight: 9
translated_at: 2026-06-11T06:30:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-11T06:30:02+00:00
---
We have previously defined Galois extensions and Galois groups. The central result of Galois theory is that for a field extension $$\mathbb{L}/\mathbb{K}$$, there exists an order-preserving bijection between the lattice of subgroups of the Galois group $$\Gal(\mathbb{L}/\mathbb{K})$$ and the lattice of Galois subextensions of $$\mathbb{L}/\mathbb{K}$$. Many treatments discuss this result only when $$\Gal(\mathbb{L}/\mathbb{K})$$ is finite, but we shall also cover the infinite case, and to do so we must endow $$\Gal(\mathbb{L}/\mathbb{K})$$ with an appropriate topology.

## Topology of the Galois Group

Let $$\mathbb{L}/\mathbb{K}$$ be a Galois extension, and let $$\Gal(\mathbb{L}/\mathbb{K})$$ denote its Galois group. Since the Galois group is a collection of functions from $$\mathbb{L}$$ to $$\mathbb{L}$$, if we equip the set of all such functions $$\Fun(\mathbb{L},\mathbb{L})=\mathbb{L}^\mathbb{L}$$ with a topology, then we can induce a topology on $$\Gal(\mathbb{L}/\mathbb{K})$$ as a subset of this set. ([[Topology] §Subspaces, ⁋Definition 1](/en/math/topology/subspaces#def1))

To this end, we give $$\mathbb{L}$$ the discrete topology. ([[Topology] §Open Sets, ⁋Example 2](/en/math/topology/open_sets#ex2)) From the results of [[Topology] §Product Spaces](/en/math/topology/product_spaces), we know that a subbase for this set consists of sets of the form

$$U_{x,y}=\left\{\sigma\mid\sigma(x)=y \right\}$$

so if we give $$\Gal(\mathbb{L}/\mathbb{K})$$ the subspace topology, then for any $$\sigma\in\Gal(\mathbb{L}/\mathbb{K})$$, the collection of sets of the form

$$U_{x_1,\ldots,x_n}=\left\{\tau\in\Gal(\mathbb{L}/\mathbb{K})\mid \text{$\tau(x_i)=\sigma(x_i)$ for all $i$}\right\}$$

forms a local base at $$\sigma$$. ([[Topology] §Bases of Topological Spaces, ⁋Definition 4](/en/math/topology/topological_bases#def4))

On the other hand, the functions satisfying the above condition are precisely those that agree with $$\sigma$$ when restricted to a finite subextension $$\mathbb{M}=\mathbb{L}(x_1,\ldots,x_n )$$ of $$\mathbb{L}$$; conversely, any finite subextension $$\mathbb{M}/\mathbb{K}$$ defines an element of the local base at $$\sigma$$ in this manner. That is, letting $$\Lambda$$ be the collection of *finite* subextensions of $$\mathbb{L}/\mathbb{K}$$, and for any $$\mathbb{M}/\mathbb{K}\in \Lambda$$ and any $$\sigma\in \Gal(\mathbb{L}/\mathbb{K})$$, defining the subset $$U_\mathbb{M}(\sigma)$$ of $$\Gal(\mathbb{L}/\mathbb{K})$$ by the formula

$$U_\mathbb{M}(\sigma)=\left\{\tau\in \Gal(\mathbb{L}/\mathbb{K})\mid \sigma\vert_\mathbb{M}=\tau\vert_\mathbb{M}\right\}$$

this set becomes an element of the local base at $$\sigma$$, and the collection $$(U_\mathbb{M}(\sigma))_{\sigma\in\Lambda}$$ is exactly the local base at $$\sigma$$.

<div class="example" markdown="1">

<ins id="ex1">**Example 1**</ins> Let us consider the special case where $$\mathbb{L}/\mathbb{K}$$ is a finite degree Galois extension. Then from the discussion following [§Galois Extensions, ⁋Definition 12](/en/math/field_theory/galois_extension#def12), we know that $$\Gal(\mathbb{L}/\mathbb{K})$$ is a finite set. On the other hand, from the local base above, since $$\mathbb{L}/\mathbb{K}$$ is of finite degree, $$\mathbb{L}/\mathbb{K}$$ is already an element of $$\Lambda$$, and therefore

$$U_\mathbb{L}(\sigma)=\left\{\tau\in\Gal(\mathbb{L}/\mathbb{K})\mid \sigma\vert_\mathbb{L}=\tau\vert_\mathbb{L}\right\}=\left\{\sigma\right\}$$

so in this case $$\Gal(\mathbb{L}/\mathbb{K})$$ carries the discrete topology.

</div>

Moreover, the topological space $$\Gal(\mathbb{L}/\mathbb{K})$$ defined above is originally a group under composition of $$\mathbb{K}$$-automorphisms, and it is not difficult to show that composition of functions is compatible with this topological structure.

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> The $$\Gal(\mathbb{L}/\mathbb{K})$$ defined above is a topological group.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

That is, we must show that the two homomorphisms

$$\Gal(\mathbb{L}/\mathbb{K})\times\Gal(\mathbb{L}/\mathbb{K})\rightarrow\Gal(\mathbb{L}/\mathbb{K});\quad (\sigma,\sigma')\mapsto \sigma\sigma',\qquad \Gal(\mathbb{L}/\mathbb{K})\rightarrow\Gal(\mathbb{L}/\mathbb{K});\quad \sigma\mapsto \sigma^{-1}$$

are continuous. First, considering an arbitrary element $$U_\mathbb{M}(\sigma\sigma')$$ of the local base at $$\sigma\sigma'$$, by definition

$$U_\mathbb{M}(\sigma\sigma')=\left\{\tau\in\Gal(\mathbb{L}/\mathbb{K})\mid \tau\vert_\mathbb{M}=\sigma\sigma'\vert_\mathbb{M}\right\}$$

and thus for obvious reasons the open set $$U_\mathbb{M}(\sigma)\times U_\mathbb{M}(\sigma')$$ in $$\Gal(\mathbb{L}/\mathbb{K})\times\Gal(\mathbb{L}/\mathbb{K})$$ is contained in the preimage of the above set, so the multiplication map is continuous.

Similarly, the local base element $$U_\mathbb{M}(\sigma^{-1})$$ at $$\sigma^{-1}$$ is given by the formula

$$U_\mathbb{M}(\sigma^{-1})=\left\{\tau\in\Gal(\mathbb{L}/\mathbb{K})\mid \tau\vert_\mathbb{M}=\sigma^{-1}\vert_\mathbb{M}\right\}$$

and considering the local base element $$U_\mathbb{M}(\sigma)$$ at $$\sigma$$, this set is contained in the preimage of the above set.

</details>

In particular, the local base at any $$\sigma$$ is obtained by translating the local base at the identity $$\id_\mathbb{L}$$ via the translation map. That is, for any $$\sigma\in \Gal(\mathbb{L}/\mathbb{K})$$, the formula

$$U_\mathbb{M}(\sigma)=U_\mathbb{M}(\id_\mathbb{L})\sigma=\sigma U_\mathbb{M}(\id_\mathbb{L})$$

holds. From this we know that it suffices to consider only the set

$$U_\mathbb{M}(\id_\mathbb{L})=\left\{\tau\in \Gal(\mathbb{L}/\mathbb{K})\mid \tau\vert_\mathbb{M}=\id_\mathbb{M}\right\}$$

instead of the above sets. Then

$$U_\mathbb{M}(\id_\mathbb{L})\subseteq U_\mathbb{N}(\id_\mathbb{L})\iff \mathbb{M}\supseteq \mathbb{N}$$

and from the notation above, as a set we know that

$$U_\mathbb{M}(\id_\mathbb{L})=\Gal(\mathbb{L}/\mathbb{M})$$

Here, the inclusion on the right is simply obtained by viewing an $$\mathbb{M}$$-automorphism as a $$\mathbb{K}$$-automorphism, and moreover we know that the topology defined on $$\Gal(\mathbb{L}/\mathbb{M})$$ is exactly the same as that on $$U_\mathbb{M}(\id_\mathbb{L})$$.

Now considering the collection $$\Lambda'$$ of finite degree *Galois* extensions, by [§Galois Extensions, ⁋Proposition 11](/en/math/field_theory/galois_extension#prop11) we know that this is a cofinal subset of $$\Lambda$$. That is, $$(U_\mathbb{M}(\id_\mathbb{L}))_{\mathbb{M}\in\Lambda}$$ is also a local base at $$\id_\mathbb{L}$$. Then for any $$\mathbb{M}\in \Lambda'$$, considering the restriction homomorphism $$\rho:\Gal(\mathbb{L}/\mathbb{K})\rightarrow\Gal(\mathbb{M}/\mathbb{K})$$ examined in [§Galois Extensions, ⁋Proposition 13](/en/math/field_theory/galois_extension#prop13), since any finite degree subextension of $$\mathbb{M}$$ is also a finite degree subextension of $$\mathbb{L}$$, this restriction homomorphism is continuous with respect to the topology defined above. In this situation, $$\rho$$ is a continuous function from $$\Gal(\mathbb{L}/\mathbb{K})$$ to the finite discrete space $$\Gal(\mathbb{M}/\mathbb{K})$$ ([Example 1](#ex1)), so $$\ker\rho$$ is a closed subgroup of $$\Gal(\mathbb{L}/\mathbb{K})$$. However, by definition

$$\sigma\in\ker\rho\iff \sigma\vert_\mathbb{M}=\id\vert_\mathbb{M}\iff\sigma\in U_\mathbb{M}(\id_\mathbb{L})$$

so each $$U_\mathbb{M}(\id_\mathbb{L})$$ is clopen. On the other hand, any clopen set can always be written as a union of connected components, and therefore any non-empty intersection of clopen sets must contain a connected component. However, the following holds.

<div class="proposition" markdown="1">

<ins id="prop3">**Proposition 3**</ins> In the above situation, the formula

$$\{\id_\mathbb{L}\}=\bigcap_{\mathbb{M}\in \Lambda'}U_\mathbb{M}(\id_\mathbb{L})$$

holds.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Let an arbitrary $$\sigma\in \Gal(\mathbb{L}/\mathbb{K})$$ be given. If $$\sigma\neq\id_\mathbb{L}$$, then there exists $$x\in \mathbb{L}$$ such that $$\sigma(x)\neq x$$. Then taking $$\mathbb{M}=\mathbb{K}(x)$$, we have $$\sigma\not\in U_\mathbb{M}(\id_\mathbb{L})$$. Now, as examined earlier, since $$\Lambda'$$ is a cofinal subset of $$\Lambda$$, we obtain the desired result.

</details>

Therefore, by the result of this proposition, the connected component containing $$\id_\mathbb{L}$$ is $$\left\{\id_\mathbb{L}\right\}$$, and from this we know that $$\Gal(\mathbb{L}/\mathbb{K})$$ is a totally disconnected space. ([[Topology] §Connected Spaces, ⁋Definition 7](/en/math/topology/connected_spaces#def7)) Moreover, the following holds.

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4**</ins> $$\Gal(\mathbb{L}/\mathbb{K})$$ is compact.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, for each $$x\in \mathbb{L}$$, since $$\mathbb{L}/\mathbb{K}$$ is an algebraic extension, $$x$$ is algebraic, and therefore there are only finitely many elements conjugate to $$x$$. ([§Galois Extensions, ⁋Proposition 3](/en/math/field_theory/galois_extension#prop3)) In other words, considering

$$\Gal(\mathbb{L}/\mathbb{K})\hookrightarrow \prod_{x\in \mathbb{L}}\mathbb{L}\overset{\pr_x}{\longrightarrow}\mathbb{L};\qquad \sigma\mapsto \sigma(x)$$

the image of this function is a finite set. Therefore $$\Gal(\mathbb{L}/\mathbb{K})$$ is a subset of a product of finite sets, and since finite sets are compact, this product is also compact. ([[Topology] §Compactness, ⁋Theorem 2](/en/math/topology/compactness#thm2)) Thus proving the given proposition is equivalent to showing that $$\Gal(\mathbb{L}/\mathbb{K})$$ is closed in $$\mathbb{L}^\mathbb{L}$$.

Suppose a function $$u$$ lies in the closure of $$\Gal(\mathbb{L}/\mathbb{K})$$ in $$\mathbb{L}^\mathbb{L}$$. If $$u$$ is not an element of $$\Gal(\mathbb{L}/\mathbb{K})$$, then either $$u$$ is not a field homomorphism or $$u$$ does not fix $$\mathbb{K}$$. Adopting the first assumption, suppose there exist $$x,y\in\mathbb{L}$$ such that $$u(x+y)\neq u(x)+u(y)$$. Then the set

$$\left\{f\in \mathbb{L}^\mathbb{L}\mid f(x)=u(x),f(y)=u(y),f(x+y)=u(x+y)\right\}$$

is a basic open set in $$\mathbb{L}^\mathbb{L}$$, hence open, and moreover contains $$u$$. That is, this set is an open neighborhood of $$u$$. However, from the assumption

$$f(x+y)=u(x+y)\neq u(x)+u(y)=f(x)+f(y)$$

so these $$f$$ are also not field homomorphisms. That is, the above open neighborhood does not meet $$\Gal(\mathbb{L}/\mathbb{K})$$, which contradicts the assumption that $$u$$ lies in the closure of $$\Gal(\mathbb{L}/\mathbb{K})$$. By similar logic all other cases can also be excluded, and from this we can prove that $$\Gal(\mathbb{L}/\mathbb{K})$$ is closed in $$\mathbb{L}^\mathbb{L}$$.

</details>

On the other hand, let $$\mathbb{L}/\mathbb{K}$$ be a Galois extension, and let $$\mathbb{L}_i/\mathbb{K}$$ be Galois subextensions of this extension satisfying $$\mathbb{L}=\bigcup_{i\in I}\mathbb{L}_i$$. Then we endow this with the partial order

$$i\leq j \iff \mathbb{L}_i\subset \mathbb{L}_j$$

and under this partial order we can define the following restriction maps

$$\rho_{ij}:\Gal(\mathbb{L}_j/\mathbb{K}) \rightarrow \Gal(\mathbb{L}_i/\mathbb{K})\qquad \text{whenever $i\leq j$}$$

These are continuous homomorphisms, and therefore their inverse limit

$$\varprojlim_{i\in I}\Gal(\mathbb{L}_i/\mathbb{K})$$

and the canonical morphisms $$\rho_i:\varprojlim \Gal(\mathbb{L}_i/\mathbb{K})\rightarrow\Gal(\mathbb{L}_i/\mathbb{K})$$ exist.

On the other hand, considering the restriction maps

$$\lambda_i:\Gal(\mathbb{L}/\mathbb{K})\rightarrow\Gal(\mathbb{L}_i/\mathbb{K})$$

since these satisfy $$\lambda_i=\rho_{ij}\circ\lambda_j$$, the continuous homomorphism $$\lambda:\Gal(\mathbb{L}/\mathbb{K})\rightarrow\varprojlim\Gal(\mathbb{L}_i/\mathbb{K})$$ induced by them exists.

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> The $$\lambda$$ defined above is an isomorphism of topological groups.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

By [Proposition 3](#prop3), each $$\Gal(\mathbb{L}_i/\mathbb{K})$$ is Hausdorff, and since products and subspaces of Hausdorff spaces are again Hausdorff, their inverse limit $$\varprojlim \Gal(\mathbb{L}_i/\mathbb{K})$$ is also Hausdorff. On the other hand, since $$\Gal(\mathbb{L}/\mathbb{K})$$ is compact by [Proposition 4](#prop4), by [[Topology] §Compact Spaces, ⁋Proposition 9](/en/math/topology/compact_spaces#prop9) it suffices to show that $$\lambda$$ is bijective, which is almost obvious from $$\mathbb{L}= \bigcup \mathbb{L}_i$$.

</details>

In particular, this proposition applies well to the family $$\Lambda'$$.

## Galois Cohomology

The Galois group is not merely a group, but a group acting on $$\mathbb{L}$$, and in particular on the multiplicative group $$\mathbb{L}^\times$$. The standard tool for extracting the arithmetic information encoded in this action is *Galois cohomology*, and to close this article we examine the classical theorem at its origin, Hilbert's Theorem 90. In this section $$\mathbb{L}/\mathbb{K}$$ is a finite degree Galois extension and $$G=\Gal(\mathbb{L}/\mathbb{K})$$.

<div class="definition" markdown="1">

<ins id="def6">**Definition 6**</ins> A function $$\varphi:G \rightarrow \mathbb{L}^\times$$ is called a *1-cocycle* if for any $$\sigma,\tau\in G$$ the formula

$$\varphi(\sigma\tau)=\varphi(\sigma)\cdot\sigma\bigl(\varphi(\tau)\bigr)$$

holds. In particular, a 1-cocycle of the form $$\varphi(\sigma)=\sigma(c)/c$$ for some $$c\in\mathbb{L}^\times$$ is called a *1-coboundary*.

</div>

First, verifying that a 1-coboundary is indeed a 1-cocycle, we have

$$\varphi(\sigma)\cdot\sigma(\varphi(\tau))=\frac{\sigma(c)}{c}\cdot\sigma\left(\frac{\tau(c)}{c}\right)=\frac{\sigma(c)}{c}\cdot\frac{\sigma\tau(c)}{\sigma(c)}=\frac{\sigma\tau(c)}{c}=\varphi(\sigma\tau)$$

Also, since the 1-cocycles form an abelian group under pointwise multiplication and the 1-coboundaries form a subgroup thereof, we can consider the quotient group, which we denote by $$H^1(G,\mathbb{L}^\times)$$. Hilbert's Theorem 90 is the somewhat deflating but extremely useful theorem that this group contains no information whatsoever.

<div class="proposition" markdown="1">

<ins id="thm7">**Theorem 7 (Hilbert 90)**</ins> For a finite degree Galois extension $$\mathbb{L}/\mathbb{K}$$, every 1-cocycle $$\varphi:G \rightarrow \mathbb{L}^\times$$ is a 1-coboundary. That is, $$H^1(G,\mathbb{L}^\times)$$ is trivial.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Since the elements of $$G$$ are distinct homomorphisms from $$\mathbb{L}$$ to $$\mathbb{L}$$, by Dedekind's theorem in [§Étale Algebras, ⁋Corollary 3](/en/math/field_theory/etale_algebras#cor3), they are linearly independent over the $$\mathbb{L}$$-vector space. Since the values of $$\varphi$$ are all non-zero, the linear combination

$$\sum_{\tau\in G}\varphi(\tau)\,\tau$$

is not the zero map, and therefore for some $$x\in\mathbb{L}$$

$$b=\sum_{\tau\in G}\varphi(\tau)\,\tau(x)\neq0$$

Now for any $$\sigma\in G$$, rewriting the cocycle condition as $$\sigma(\varphi(\tau))=\varphi(\sigma)^{-1}\varphi(\sigma\tau)$$ and computing, we have

$$\sigma(b)=\sum_{\tau\in G}\sigma(\varphi(\tau))\,\sigma\tau(x)=\varphi(\sigma)^{-1}\sum_{\tau\in G}\varphi(\sigma\tau)\,\sigma\tau(x)=\varphi(\sigma)^{-1}b$$

The last equality holds because as $$\tau$$ ranges over all of $$G$$, so does $$\sigma\tau$$. Therefore taking $$c=b^{-1}$$

$$\varphi(\sigma)=\frac{b}{\sigma(b)}=\frac{\sigma(c)}{c}$$

so $$\varphi$$ is a 1-coboundary.

</details>

The classical form of Hilbert 90 concerns cyclic extensions. Let $$G=\langle\sigma\rangle$$ be a cyclic group of order $$n$$, and define the *norm* of $$x\in\mathbb{L}$$ by

$$N_{\mathbb{L}/\mathbb{K}}(x)=\prod_{i=0}^{n-1}\sigma^i(x)$$

Applying $$\sigma$$ merely permutes the factors, so $$N_{\mathbb{L}/\mathbb{K}}(x)$$ is $$G$$-invariant, and since $$\mathbb{L}/\mathbb{K}$$ is Galois, by [§Galois Extensions, ⁋Theorem 8](/en/math/field_theory/galois_extension#thm8) we have $$N_{\mathbb{L}/\mathbb{K}}(x)\in\mathbb{K}$$.

<div class="proposition" markdown="1">

<ins id="cor8">**Corollary 8**</ins> Let $$\mathbb{L}/\mathbb{K}$$ be a finite degree Galois extension and let $$G=\Gal(\mathbb{L}/\mathbb{K})=\langle\sigma\rangle$$ be cyclic. Then for $$x\in\mathbb{L}^\times$$, the following are equivalent.

1. $$N_{\mathbb{L}/\mathbb{K}}(x)=1$$.
2. There exists $$y\in\mathbb{L}^\times$$ such that $$x=\sigma(y)/y$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, assuming the second condition,

$$N_{\mathbb{L}/\mathbb{K}}\bigl(\sigma(y)/y\bigr)=\prod_{i=0}^{n-1}\frac{\sigma^{i+1}(y)}{\sigma^i(y)}=\frac{\sigma^n(y)}{y}=1$$

The middle equality is telescoping and the last equality follows from $$\sigma^n=\id_\mathbb{L}$$.

Conversely, assume $$N_{\mathbb{L}/\mathbb{K}}(x)=1$$. Define the function $$\varphi:G \rightarrow \mathbb{L}^\times$$ by

$$\varphi(\sigma^i)=\prod_{k=0}^{i-1}\sigma^k(x)\qquad(0\leq i\leq n-1)$$

where for $$i=0$$ the empty product gives $$\varphi(\id)=1$$. Let us verify that this is a 1-cocycle. For $$0\leq a,b\leq n-1$$,

$$\varphi(\sigma^a)\cdot\sigma^a\bigl(\varphi(\sigma^b)\bigr)=\prod_{k=0}^{a-1}\sigma^k(x)\cdot\prod_{k=0}^{b-1}\sigma^{a+k}(x)=\prod_{k=0}^{a+b-1}\sigma^k(x)$$

If $$a+b\leq n-1$$, then by definition this is $$\varphi(\sigma^{a+b})=\varphi(\sigma^a\sigma^b)$$. If $$a+b\geq n$$, then since $$\sigma^k=\sigma^{k-n}$$ ($$k\geq n$$),

$$\prod_{k=0}^{a+b-1}\sigma^k(x)=\prod_{k=0}^{n-1}\sigma^k(x)\cdot\prod_{k=n}^{a+b-1}\sigma^k(x)=N_{\mathbb{L}/\mathbb{K}}(x)\cdot\prod_{k=0}^{a+b-n-1}\sigma^k(x)=\varphi(\sigma^{a+b-n})$$

and since $$\sigma^a\sigma^b=\sigma^{a+b-n}$$, the cocycle condition again holds. The assumption $$N_{\mathbb{L}/\mathbb{K}}(x)=1$$ was used in the last equality.

Now by [Theorem 7](#thm7), $$\varphi$$ is a 1-coboundary. That is, for some $$c\in\mathbb{L}^\times$$ we have $$\varphi(\sigma^i)=\sigma^i(c)/c$$, and in particular for $$i=1$$

$$x=\varphi(\sigma)=\frac{\sigma(c)}{c}$$

so taking $$y=c$$ suffices.

</details>

<div class="remark" markdown="1">

<ins id="rmk9">**Remark 9**</ins> The 1-cocycle of [Definition 6](#def6) is the crossed homomorphism discussed in [[Homological Algebra] §Group Cohomology](/en/math/homological_algebra/group_cohomology), translated into multiplicative notation. That is, viewing $$\mathbb{L}^\times$$ as a $$G$$-module, $$H^1(G,\mathbb{L}^\times)$$ is the group cohomology $$H^1$$, [Theorem 7](#thm7) is the assertion that this vanishes, and [Corollary 8](#cor8) is obtained by combining this with the cohomology computation for cyclic groups. On the other hand, when $$\mathbb{L}/\mathbb{K}$$ is an infinite degree Galois extension, one must use cocycles that are continuous with respect to the Krull topology defined in this article to obtain the correct theory, which is another reason we took care to construct the topological structure in this article. The additive version—that is, the vanishing of $$H^1(G,\mathbb{L})$$ when $$\mathbb{L}$$ is viewed as an additive group—also holds; this is related to the normal basis theorem, so we shall cover it when needed later.

</div>

---

**References**

**[Bou]** N. Bourbaki. *Algebra II: Chapters 4–7*. Springer, 2003.  
**[Ser]** J.-P. Serre. *Local Fields*. Graduate texts in mathematics. Springer, 1979.

---
