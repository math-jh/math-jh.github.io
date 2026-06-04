---
title: "Properties of Galois Groups"
description: "This post explains how to endow a Galois group with a topology, and describes the correspondence between the lattice of subgroups and the lattice of intermediate extensions."
excerpt: "The structure of infinite Galois groups with the Krull topology"

categories: [Math / Field Theory]
permalink: /en/math/field_theory/properties_of_galois_extensions
sidebar: 
    nav: "field_theory-en"

date: 2025-06-18
last_modified_at: 2025-06-18
weight: 9
translated_at: 2026-05-31T08:00:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-05-31T08:00:04+00:00
---
We previously defined Galois extensions and Galois groups. The central result of Galois theory is that for a field extension $$\mathbb{L}/\mathbb{K}$$, there exists an order-preserving bijection between the lattice of subgroups of the Galois group $$\Gal(\mathbb{L}/\mathbb{K})$$ and the lattice of Galois subextensions of $$\mathbb{L}/\mathbb{K}$$. Many treatments of this result consider only the case where $$\Gal(\mathbb{L}/\mathbb{K})$$ is finite, but since we will also treat the infinite case, we must endow $$\Gal(\mathbb{L}/\mathbb{K})$$ with an appropriate topological structure.

## The Topological Structure of Galois Groups

Let a Galois extension $$\mathbb{L}/\mathbb{K}$$ be given, and let $$\Gal(\mathbb{L}/\mathbb{K})$$ be its Galois group. Since the Galois group is, after all, a collection of functions from $$\mathbb{L}$$ to $$\mathbb{L}$$, if we endow the set of all such functions $$\Fun(\mathbb{L},\mathbb{L})=\mathbb{L}^\mathbb{L}$$ with a topological structure, we can give $$\Gal(\mathbb{L}/\mathbb{K})$$ the subspace topology as a subset of this set. ([\[Topology\] §Subspaces, ⁋Definition 1](/en/math/topology/subspaces#def1))

To this end, we endow $$\mathbb{L}$$ with the discrete topology. ([\[Topology\] §Open Sets, ⁋Example 2](/en/math/topology/open_sets#ex2)) From the results of [\[Topology\] §Product Spaces](/en/math/topology/product_spaces), we know that a subbase for this set consists of sets of the form

$$U_{x,y}=\left\{\sigma\mid\sigma(x)=y \right\}$$

and so, giving $$\Gal(\mathbb{L}/\mathbb{K})$$ the subspace topology, we know that for any $$\sigma\in\Gal(\mathbb{L}/\mathbb{K})$$ the collection of sets of the form

$$U_{x_1,\ldots,x_n}=\left\{\tau\in\Gal(\mathbb{L}/\mathbb{K})\mid \text{$\tau(x_i)=\sigma(x_i)$ for all $i$}\right\}$$

constitutes a local base at $$\sigma$$. ([\[Topology\] §Bases of a Topological Space, ⁋Definition 4](/en/math/topology/topological_bases#def4))

Meanwhile, the functions satisfying the above condition are precisely those that agree with $$\sigma$$ when restricted to the finite subextension $$\mathbb{M}=\mathbb{L}(x_1,\ldots,x_n)$$ of $$\mathbb{L}$$; conversely, any finite subextension $$\mathbb{M}/\mathbb{K}$$ defines an element of the local base at $$\sigma$$ in this manner. That is, letting $$\Lambda$$ denote the collection of *finite* subextensions of $$\mathbb{L}/\mathbb{K}$$, and for any $$\mathbb{M}/\mathbb{K}\in \Lambda$$ and any $$\sigma\in \Gal(\mathbb{L}/\mathbb{K})$$ defining the subset $$U_\mathbb{M}(\sigma)$$ of $$\Gal(\mathbb{L}/\mathbb{K})$$ by

$$U_\mathbb{M}(\sigma)=\left\{\tau\in \Gal(\mathbb{L}/\mathbb{K})\mid \sigma\vert_\mathbb{M}=\tau\vert_\mathbb{M}\right\}$$

this set becomes an element of the local base at $$\sigma$$, and the collection $$(U_\mathbb{M}(\sigma))_{\mathbb{M}\in\Lambda}$$ is precisely the local base at $$\sigma$$.
  
<div class="example" markdown="1">

<ins id="ex1">**Example 1**</ins> In particular, consider the case where $$\mathbb{L}/\mathbb{K}$$ is a finite degree Galois extension. Then from the discussion following [§Galois Extensions, ⁋Definition 12](/en/math/field_theory/galois_extension#def12), we know that $$\Gal(\mathbb{L}/\mathbb{K})$$ is a finite set. Meanwhile, from the local base described above, since $$\mathbb{L}/\mathbb{K}$$ is of finite degree, $$\mathbb{L}/\mathbb{K}$$ itself is already an element of $$\Lambda$$ and therefore

$$U_\mathbb{L}(\sigma)=\left\{\tau\in\Gal(\mathbb{L}/\mathbb{K})\mid \sigma\vert_\mathbb{L}=\tau\vert_\mathbb{L}\right\}=\left\{\sigma\right\}$$

so in this case $$\Gal(\mathbb{L}/\mathbb{K})$$ carries the discrete topology. 

</div>

Meanwhile, the topological space $$\Gal(\mathbb{L}/\mathbb{K})$$ defined above is originally a group under composition of $$\mathbb{K}$$-automorphisms, and it is not difficult to show that composition is compatible with this topological structure.
  
<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> $$\Gal(\mathbb{L}/\mathbb{K})$$ defined above is a topological group. 

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

That is, we must show that the two maps

$$\Gal(\mathbb{L}/\mathbb{K})\times\Gal(\mathbb{L}/\mathbb{K})\rightarrow\Gal(\mathbb{L}/\mathbb{K});\quad (\sigma,\sigma')\mapsto \sigma\sigma',\qquad \Gal(\mathbb{L}/\mathbb{K})\rightarrow\Gal(\mathbb{L}/\mathbb{K});\quad \sigma\mapsto \sigma^{-1}$$

are continuous. First, taking any element $$U_\mathbb{M}(\sigma\sigma')$$ of the local base at $$\sigma\sigma'$$, by definition

$$U_\mathbb{M}(\sigma\sigma')=\left\{\tau\in\Gal(\mathbb{L}/\mathbb{K})\mid \tau\vert_\mathbb{M}=\sigma\sigma'\vert_\mathbb{M}\right\}$$

and therefore the open set $$U_\mathbb{M}(\sigma)\times U_\mathbb{M}(\sigma')$$ in $$\Gal(\mathbb{L}/\mathbb{K})\times\Gal(\mathbb{L}/\mathbb{K})$$ is contained in the preimage of the above set; thus the multiplication map is continuous. 

Similarly, the local base element $$U_\mathbb{M}(\sigma^{-1})$$ at $$\sigma^{-1}$$ is given by

$$U_\mathbb{M}(\sigma^{-1})=\left\{\tau\in\Gal(\mathbb{L}/\mathbb{K})\mid \tau\vert_\mathbb{M}=\sigma^{-1}\vert_\mathbb{M}\right\}$$

and considering the local base element $$U_\mathbb{M}(\sigma)$$ at $$\sigma$$, this set is contained in the preimage of the above set. 

</details>

In particular, the local base at any $$\sigma$$ is obtained by translating the local base at the identity $$\id_\mathbb{L}$$ along the translation map. That is, for any $$\sigma\in \Gal(\mathbb{L}/\mathbb{K})$$ the identity

$$U_\mathbb{M}(\sigma)=U_\mathbb{M}(\id_\mathbb{L})\sigma=\sigma U_\mathbb{M}(\id_\mathbb{L})$$

holds. From this we know that instead of the above sets, we need only consider

$$U_\mathbb{M}(\id_\mathbb{L})=\left\{\tau\in \Gal(\mathbb{L}/\mathbb{K})\mid \tau\vert_\mathbb{M}=\id_\mathbb{M}\right\}$$

Then

$$U_\mathbb{M}(\id_\mathbb{L})\subseteq U_\mathbb{N}(\id_\mathbb{L})\iff \mathbb{M}\supseteq \mathbb{N}$$

and from the above notation we know that as sets

$$U_\mathbb{M}(\id_\mathbb{L})=\Gal(\mathbb{L}/\mathbb{M})$$

The inclusion on the right is simply obtained by viewing an $$\mathbb{M}$$-automorphism as a $$\mathbb{K}$$-automorphism, and moreover we know that the topological structure defined on $$\Gal(\mathbb{L}/\mathbb{M})$$ coincides exactly with that of $$U_\mathbb{M}(\id_\mathbb{L})$$.

Now, letting $$\Lambda'$$ denote the collection of finite degree *Galois* extensions, by [§Galois Extensions, ⁋Proposition 11](/en/math/field_theory/galois_extension#prop11) we know that this is a cofinal subset of $$\Lambda$$. That is, $$(U_\mathbb{M}(\id_\mathbb{L}))_{\mathbb{M}\in\Lambda'}$$ is also a local base at $$\id_\mathbb{L}$$. Then for any $$\mathbb{M}\in \Lambda'$$, considering the restriction homomorphism $$\rho:\Gal(\mathbb{L}/\mathbb{K})\rightarrow\Gal(\mathbb{M}/\mathbb{K})$$ examined in [§Galois Extensions, ⁋Proposition 13](/en/math/field_theory/galois_extension#prop13), since any finite degree subextension of $$\mathbb{M}$$ is also a finite degree subextension of $$\mathbb{L}$$, this restriction homomorphism is continuous with respect to the topological structure defined above. In this situation, since $$\rho$$ is a continuous function from $$\Gal(\mathbb{L}/\mathbb{K})$$ to the finite discrete space $$\Gal(\mathbb{M}/\mathbb{K})$$ ([Example 1](#ex1)), $$\ker\rho$$ is a closed subgroup of $$\Gal(\mathbb{L}/\mathbb{K})$$. However, by definition

$$\sigma\in\ker\rho\iff \sigma\vert_\mathbb{M}=\id\vert_\mathbb{M}\iff\sigma\in U_\mathbb{M}(\id_\mathbb{L})$$

so each $$U_\mathbb{M}(\id_\mathbb{L})$$ is clopen. Meanwhile, any clopen set can always be written as a union of connected components, and therefore any nonempty intersection of clopen sets must contain a connected component. However, the following holds.

<div class="proposition" markdown="1">

<ins id="prop3">**Proposition 3**</ins> In the above situation the identity

$$\{\id_\mathbb{L}\}=\bigcap_{\mathbb{M}\in \Lambda'}U_\mathbb{M}(\id_\mathbb{L})$$

holds.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Let any $$\sigma\in \Gal(\mathbb{L}/\mathbb{K})$$ be given. If $$\sigma\neq\id_\mathbb{L}$$, then there exists $$x\in \mathbb{L}$$ such that $$\sigma(x)\neq x$$. Then taking $$\mathbb{M}=\mathbb{K}(x)$$, we have $$\sigma\not\in U_\mathbb{M}(\id_\mathbb{L})$$. Now, as we saw earlier, since $$\Lambda'$$ is a cofinal subset of $$\Lambda$$, we obtain the desired result.

</details>

Therefore, by this proposition the connected component containing $$\id_\mathbb{L}$$ is $$\left\{\id_\mathbb{L}\right\}$$, and from this we know that $$\Gal(\mathbb{L}/\mathbb{K})$$ is a totally disconnected space. ([\[Topology\] §Connected Spaces, ⁋Definition 7](/en/math/topology/connected_spaces#def7)) Moreover, the following holds.

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4**</ins> $$\Gal(\mathbb{L}/\mathbb{K})$$ is compact. 

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, for each $$x\in \mathbb{L}$$, since $$\mathbb{L}/\mathbb{K}$$ is an algebraic extension, $$x$$ is algebraic, and therefore there are only finitely many elements conjugate to $$x$$. ([§Galois Extensions, ⁋Proposition 3](/en/math/field_theory/galois_extension#prop3)) In other words, considering

$$\Gal(\mathbb{L}/\mathbb{K})\hookrightarrow \prod_{x\in \mathbb{L}}\mathbb{L}\overset{\pr_x}{\longrightarrow}\mathbb{L};\qquad \sigma\mapsto \sigma(x)$$

the image of this function is a finite set. Therefore $$\Gal(\mathbb{L}/\mathbb{K})$$ is a subset of a product of finite sets, and since finite sets are compact, this product is also compact. ([\[Topology\] §Compactness, ⁋Theorem 2](/en/math/topology/compactness#thm2)) Thus proving the given proposition amounts to showing that $$\Gal(\mathbb{L}/\mathbb{K})$$ is closed in $$\mathbb{L}^\mathbb{L}$$.

Suppose a function $$u$$ belongs to the closure of $$\Gal(\mathbb{L}/\mathbb{K})$$ in $$\mathbb{L}^\mathbb{L}$$. If $$u$$ is not an element of $$\Gal(\mathbb{L}/\mathbb{K})$$, then either $$u$$ is not a field homomorphism or $$u$$ does not fix $$\mathbb{K}$$. Adopting the first assumption, suppose there exist $$x,y\in\mathbb{L}$$ such that $$u(x+y)\neq u(x)+u(y)$$. Then the set

$$\left\{f\in \mathbb{L}^\mathbb{L}\mid f(x)=u(x),f(y)=u(y),f(x+y)=u(x+y)\right\}$$

is a basic open set in $$\mathbb{L}^\mathbb{L}$$, hence open, and moreover contains $$u$$. That is, this set is an open neighborhood of $$u$$. However, by assumption

$$f(x+y)=u(x+y)\neq u(x)+u(y)=f(x)+f(y)$$

so these $$f$$ are also not field homomorphisms. That is, the above open neighborhood does not meet $$\Gal(\mathbb{L}/\mathbb{K})$$, which contradicts the assumption that $$u$$ belongs to the closure of $$\Gal(\mathbb{L}/\mathbb{K})$$. By similar logic all other cases can also be excluded, and from this we can prove that $$\Gal(\mathbb{L}/\mathbb{K})$$ is closed in $$\mathbb{L}^\mathbb{L}$$.

</details>

Meanwhile, let $$\mathbb{L}/\mathbb{K}$$ be a Galois extension, and let $$\mathbb{L}_i/\mathbb{K}$$ be Galois subextensions of this extension satisfying $$\mathbb{L}=\bigcup_{i\in I}\mathbb{L}_i$$. Then we impose the partial order

$$i\leq j \iff \mathbb{L}_i\subset \mathbb{L}_j$$

and under this partial order we can define the following restriction maps

$$\rho_{ij}:\Gal(\mathbb{L}_j/\mathbb{K}) \rightarrow \Gal(\mathbb{L}_i/\mathbb{K})\qquad \text{whenever $i\leq j$}$$

These are continuous homomorphisms, and therefore their inverse limit

$$\varprojlim_{i\in I}\Gal(\mathbb{L}_i/\mathbb{K})$$

and the canonical morphisms $$\rho_i:\varprojlim \Gal(\mathbb{L}_i/\mathbb{K})\rightarrow\Gal(\mathbb{L}_i/\mathbb{K})$$ exist. 

Meanwhile, considering the restriction maps

$$\lambda_i:\Gal(\mathbb{L}/\mathbb{K})\rightarrow\Gal(\mathbb{L}_i/\mathbb{K})$$

these satisfy $$\lambda_i=\rho_{ij}\circ\lambda_j$$, so there exists a continuous homomorphism $$\lambda:\Gal(\mathbb{L}/\mathbb{K})\rightarrow\varprojlim\Gal(\mathbb{L}_i/\mathbb{K})$$ induced by them. 

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> The $$\lambda$$ defined above is an isomorphism of topological groups. 

</div >
<details class="proof" markdown="1">
<summary>Proof</summary>

By [Proposition 3](#prop3), $$\Gal(\mathbb{L}_i/\mathbb{K})$$ is Hausdorff, and since products and subspaces of Hausdorff spaces are again Hausdorff, their inverse limit $$\varprojlim \Gal(\mathbb{L}_i/\mathbb{K})$$ is also Hausdorff. Meanwhile, since $$\Gal(\mathbb{L}/\mathbb{K})$$ is compact by [Proposition 4](#prop4), by [\[Topology\] §Compact Spaces, ⁋Proposition 9](/en/math/topology/compact_spaces#prop9) it suffices to show that $$\lambda$$ is bijective, which is almost obvious from $$\mathbb{L}= \bigcup \mathbb{L}_i$$.

</details>

In particular, this proposition applies well to the family $$\Lambda'$$.

## Galois Cohomology
