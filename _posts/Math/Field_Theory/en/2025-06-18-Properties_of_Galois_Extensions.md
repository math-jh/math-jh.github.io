---
title: "Properties of Galois Groups"
description: "This post discusses how to equip a Galois group with a topological structure, and explains the correspondence between the lattice of subgroups and the lattice of subextensions."
excerpt: "Structure of infinite Galois groups with the Krull topology"

categories: [Math / Field Theory]
permalink: /en/math/field_theory/properties_of_galois_extensions
sidebar: 
    nav: "field_theory-en"

date: 2025-06-18
weight: 9
translated_at: 2026-08-09T18:45:05+00:00
translation_source: kimi-cli
last_polished_at: 2026-10-09T03:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
We have previously defined Galois extensions and Galois groups. The central result of Galois theory is that for a Galois extension $\mathbb{L}/\mathbb{K}$, there exists an inclusion-reversing bijection between the lattice of closed subgroups of the Galois group $\Gal(\mathbb{L}/\mathbb{K})$ and the lattice of subextensions of $\mathbb{L}/\mathbb{K}$. In many cases, this result is discussed only when the Galois group $\Gal(\mathbb{L}/\mathbb{K})$ is finite, but we shall also treat the case where $\Gal(\mathbb{L}/\mathbb{K})$ is infinite; for this, we must endow $\Gal(\mathbb{L}/\mathbb{K})$ with an appropriate topology.

## Topology of the Galois Group

Let $\mathbb{L}/\mathbb{K}$ be a Galois extension, and let $\Gal(\mathbb{L}/\mathbb{K})$ be the Galois group of this extension. Since the Galois group is in any case a collection of functions from the set $\mathbb{L}$ to $\mathbb{L}$, if we endow the collection $\Fun(\mathbb{L},\mathbb{L})=\mathbb{L}^\mathbb{L}$ of functions from $\mathbb{L}$ to $\mathbb{L}$ with a topology, we can endow $\Gal(\mathbb{L}/\mathbb{K})$ with a topology as a subset of this set. ([\[Topology\] §Subspaces, ⁋Definition 1](/en/math/topology/subspaces#def1){: data-lid="kk314" })

To this end, let us endow $\mathbb{L}$ with the discrete topology. ([\[Topology\] §Open Sets, ⁋Example 2](/en/math/topology/open_sets#ex2){: data-lid="3oua0" }) Then, by the discussion following [\[Topology\] §Product Spaces, ⁋Definition 1](/en/math/topology/product_spaces#def1){: data-lid="pfywy" }, sets of the form $\pr_x^{-1}(U)$ for the projections $\pr_x:\mathbb{L}^\mathbb{L}\rightarrow\mathbb{L}$ form a subbase of $\mathbb{L}^\mathbb{L}$, and since $\mathbb{L}$ is discrete, restricting $U$ to singletons here still yields a subbase. That is, since we know that a subbase of this set is the collection of sets that can be written in the form

$$U_{x,y}=\left\{\sigma\mid\sigma(x)=y \right\}$$

viewing $\Gal(\mathbb{L}/\mathbb{K})$ as a subspace of this, we know that for any $\sigma\in\Gal(\mathbb{L}/\mathbb{K})$, the collection of sets of the form

$$U_{x_1,\ldots,x_n}(\sigma)=\left\{\tau\in\Gal(\mathbb{L}/\mathbb{K})\mid \text{$\tau(x_i)=\sigma(x_i)$ for all $i$}\right\}$$

is a local base at $\sigma$. ([\[Topology\] §Bases of a Topological Space, ⁋Definition 4](/en/math/topology/topological_bases#def4){: data-lid="okdxw" })

On the other hand, the functions satisfying the above condition are those that agree with $\sigma$ when restricted to the finite subextension $\mathbb{M}=\mathbb{K}(x_1,\ldots,x_n )$ of $\mathbb{L}$, and conversely, any finite subextension $\mathbb{M}/\mathbb{K}$ defines an element of the local base at $\sigma$ in this manner. That is, let $\Ext_{\fin}(\mathbb{L}/\mathbb{K})$ be the collection of *finite* subextensions of the extension $\mathbb{L}/\mathbb{K}$; for any $\mathbb{M}/\mathbb{K}\in \Ext_{\fin}(\mathbb{L}/\mathbb{K})$ and any $\sigma\in \Gal(\mathbb{L}/\mathbb{K})$, if we define the subset $U_\mathbb{M}(\sigma)$ of $\Gal(\mathbb{L}/\mathbb{K})$ by the formula

$$U_\mathbb{M}(\sigma)=\left\{\tau\in \Gal(\mathbb{L}/\mathbb{K})\mid \sigma\vert_\mathbb{M}=\tau\vert_\mathbb{M}\right\}$$

then this set becomes an element of the local base at $\sigma$, and the collection $(U_\mathbb{M}(\sigma))_{\mathbb{M}\in\Ext_{\fin}(\mathbb{L}/\mathbb{K})}$ of these sets is precisely the local base at $\sigma$. The topology on $\Gal(\mathbb{L}/\mathbb{K})$ obtained in this way is called the *Krull topology*.

::: Example 1
In particular, consider the case where $\mathbb{L}/\mathbb{K}$ is a finite degree Galois extension. Then from the discussion following [\[Galois Extension\] §Galois Extensions, ⁋Definition 12](/en/math/field_theory/galois_extension#def12){: data-lid="4hrt0" }, we know that $\Gal(\mathbb{L}/\mathbb{K})$ is a finite set. On the other hand, since $\mathbb{L}/\mathbb{K}$ is of finite degree, $\mathbb{L}/\mathbb{K}$ itself is already an element of $\Ext_{\fin}(\mathbb{L}/\mathbb{K})$, and thus for any $\sigma\in \Gal(\mathbb{L}/\mathbb{K})$,

$$U_\mathbb{L}(\sigma)=\left\{\tau\in\Gal(\mathbb{L}/\mathbb{K})\mid \sigma\vert_\mathbb{L}=\tau\vert_\mathbb{L}\right\}=\left\{\sigma\right\}$$

is an element of the local base at $\sigma$ described above. That is, since the singleton $\left\{\sigma\right\}$ is an open set, in this case $\Gal(\mathbb{L}/\mathbb{K})$ becomes a set equipped with the discrete topology.
:::

Meanwhile, the topological space $\Gal(\mathbb{L}/\mathbb{K})$ defined above is originally a group under composition of $\mathbb{K}$-automorphisms, and it is not difficult to show that the composition of functions is compatible with this topological structure.

::: Proposition 2
$\Gal(\mathbb{L}/\mathbb{K})$ defined above is a topological group.
:::
::: Proof
That is, we must show that the two maps

$$\Gal(\mathbb{L}/\mathbb{K})\times\Gal(\mathbb{L}/\mathbb{K})\rightarrow\Gal(\mathbb{L}/\mathbb{K});\quad (\sigma,\sigma')\mapsto \sigma\sigma',\qquad \Gal(\mathbb{L}/\mathbb{K})\rightarrow\Gal(\mathbb{L}/\mathbb{K});\quad \sigma\mapsto \sigma^{-1}$$

are continuous. First, for $\sigma\sigma'$, if we consider an arbitrary element $U_\mathbb{M}(\sigma\sigma')$ of the local base, by definition

$$U_\mathbb{M}(\sigma\sigma')=\left\{\tau\in\Gal(\mathbb{L}/\mathbb{K})\mid \tau\vert_\mathbb{M}=\sigma\sigma'\vert_\mathbb{M}\right\}$$

holds. Here, since $\sigma'$ is a $\mathbb{K}$-automorphism of $\mathbb{L}$, $\sigma'(\mathbb{M})$ is also a finite subextension of $\mathbb{L}$, and if $\tau\in U_{\sigma'(\mathbb{M})}(\sigma)$ and $\tau'\in U_\mathbb{M}(\sigma')$, then for any $x\in \mathbb{M}$, since $\tau'(x)=\sigma'(x)\in\sigma'(\mathbb{M})$, we have $\tau\tau'(x)=\sigma\sigma'(x)$. That is, the open set $U_{\sigma'(\mathbb{M})}(\sigma)\times U_\mathbb{M}(\sigma')$ in $\Gal(\mathbb{L}/\mathbb{K})\times\Gal(\mathbb{L}/\mathbb{K})$ is contained in the preimage of the above set, and therefore the multiplication map is continuous.

Similarly, for $\sigma^{-1}$, the local base element $U_\mathbb{M}(\sigma^{-1})$ is given by the formula

$$U_\mathbb{M}(\sigma^{-1})=\left\{\tau\in\Gal(\mathbb{L}/\mathbb{K})\mid \tau\vert_\mathbb{M}=\sigma^{-1}\vert_\mathbb{M}\right\}$$

and since $\sigma^{-1}(\mathbb{M})$ is also a finite subextension, we can consider $U_{\sigma^{-1}(\mathbb{M})}(\sigma)$. For any $x\in \mathbb{M}$, since $\sigma^{-1}(x)\in\sigma^{-1}(\mathbb{M})$, if $\tau\in U_{\sigma^{-1}(\mathbb{M})}(\sigma)$, then $\tau(\sigma^{-1}(x))=\sigma(\sigma^{-1}(x))=x$, that is, $\tau^{-1}(x)=\sigma^{-1}(x)$, and therefore this set is contained in the preimage of the above set.
:::

In particular, the local base at any $\sigma$ is given by translating the local base at the identity $\id_\mathbb{L}$ along the left translation map. That is, for any $\sigma\in \Gal(\mathbb{L}/\mathbb{K})$, the equation

$$U_\mathbb{M}(\sigma)=\sigma U_\mathbb{M}(\id_\mathbb{L})$$

holds. From this, we see that it suffices to consider only the set

$$U_\mathbb{M}(\id_\mathbb{L})=\left\{\tau\in \Gal(\mathbb{L}/\mathbb{K})\mid \tau\vert_\mathbb{M}=\id_\mathbb{M}\right\}$$

instead of the sets above. Then by definition,

$$U_\mathbb{M}(\id_\mathbb{L})=\Gal(\mathbb{L}/\mathbb{M})$$

as sets. Here, since the third condition of [§Galois Extensions, ⁋Theorem 8](/en/math/field_theory/galois_extension#thm8){: data-lid="jo2v7" } holds even when replacing $\mathbb{K}$ with $\mathbb{M}$, $\mathbb{L}/\mathbb{M}$ is also a Galois extension, and the inclusion from the group on the right into $\Gal(\mathbb{L}/\mathbb{K})$ is simply obtained by viewing an $\mathbb{M}$-automorphism as a $\mathbb{K}$-automorphism. Moreover, the topological structure of $\Gal(\mathbb{L}/\mathbb{M})$ is the same as the subspace topology that $U_\mathbb{M}(\id_\mathbb{L})$ inherits from $\Gal(\mathbb{L}/\mathbb{K})$. Then by the first condition of the same theorem, since $\mathbb{L}^{\Gal(\mathbb{L}/\mathbb{M})}=\mathbb{M}$,

$$U_\mathbb{M}(\id_\mathbb{L})\subseteq U_\mathbb{N}(\id_\mathbb{L})\iff \mathbb{M}\supseteq \mathbb{N}$$

holds. The right-to-left direction follows immediately from the definition, and the left-to-right direction follows from $\mathbb{N}=\mathbb{L}^{\Gal(\mathbb{L}/\mathbb{N})}\subseteq\mathbb{L}^{\Gal(\mathbb{L}/\mathbb{M})}=\mathbb{M}$.

Now, considering the collection $\Ext_{\fin,\gal}(\mathbb{L}/\mathbb{K})$ of finite degree *Galois* subextensions, by [§Galois Extensions, ⁋Proposition 11](/en/math/field_theory/galois_extension#prop11){: data-lid="pljwz" } we know that this is a cofinal subset of $\Ext_{\fin}(\mathbb{L}/\mathbb{K})$. That is, $(U_\mathbb{M}(\id_\mathbb{L}))_{\mathbb{M}\in\Ext_{\fin,\gal}(\mathbb{L}/\mathbb{K})}$ is also a local base at $\id_\mathbb{L}$. Then for any $\mathbb{M}\in \Ext_{\fin,\gal}(\mathbb{L}/\mathbb{K})$, considering the restriction homomorphism $\rho:\Gal(\mathbb{L}/\mathbb{K})\rightarrow\Gal(\mathbb{M}/\mathbb{K})$ examined in [§Galois Extensions, ⁋Proposition 13](/en/math/field_theory/galois_extension#prop13){: data-lid="72rks" }, since any finite degree subextension of $\mathbb{M}$ is also a finite degree subextension of $\mathbb{L}$, this restriction homomorphism is continuous with respect to the topology defined above. In this situation, since $\rho$ is a continuous map from $\Gal(\mathbb{L}/\mathbb{K})$ to the finite discrete space $\Gal(\mathbb{M}/\mathbb{K})$ ([Example 1](#ex1){: data-lid="ij77y" }), $\ker\rho$ is a closed subgroup of $\Gal(\mathbb{L}/\mathbb{K})$. Now, by definition,

$$\sigma\in\ker\rho\iff \sigma\vert_\mathbb{M}=\id\vert_\mathbb{M}\iff\sigma\in U_\mathbb{M}(\id_\mathbb{L})$$

so each $U_\mathbb{M}(\id_\mathbb{L})$ is clopen. On the other hand, any clopen set can always be written as a union of connected components, and therefore any nonempty intersection of clopen sets must contain a connected component. However, the following holds.

::: Proposition 3
In the above situation, the following equation

$$\{\id_\mathbb{L}\}=\bigcap_{\mathbb{M}\in \Ext_{\fin,\gal}(\mathbb{L}/\mathbb{K})}U_\mathbb{M}(\id_\mathbb{L})$$

holds.
:::
::: Proof
Let $\sigma\in \Gal(\mathbb{L}/\mathbb{K})$ be given. If $\sigma\neq\id_\mathbb{L}$, then there exists $x\in \mathbb{L}$ such that $\sigma(x)\neq x$. Then, taking $\mathbb{M}=\mathbb{K}(x)$, we have $\sigma\not\in U_\mathbb{M}(\id_\mathbb{L})$. Now, as observed earlier, since $\Ext_{\fin,\gal}(\mathbb{L}/\mathbb{K})$ is a cofinal subset of $\Ext_{\fin}(\mathbb{L}/\mathbb{K})$, we obtain the desired result.
:::

Therefore, by the result of this proposition, the connected component containing $\id_\mathbb{L}$ is $\left\{\id_\mathbb{L}\right\}$. On the other hand, by [Proposition 2](#prop2){: data-lid="tbehr" }, left translation by any $\sigma$ is a homeomorphism, so the connected component containing any point is also a singleton, and from this we see that $\Gal(\mathbb{L}/\mathbb{K})$ is a totally disconnected space. ([\[Topology\] §Connected Spaces, ⁋Definition 7](/en/math/topology/connected_spaces#def7){: data-lid="qk2i3" }) Moreover, the following holds.

::: Proposition 4
$\Gal(\mathbb{L}/\mathbb{K})$ is compact.
:::
::: Proof
First, for each $x\in \mathbb{L}$, since $\mathbb{L}/\mathbb{K}$ is an algebraic extension, $x$ is algebraic, and hence there are only finitely many elements conjugate to $x$. ([§Galois Extensions, ⁋Proposition 3](/en/math/field_theory/galois_extension#prop3){: data-lid="gm9dq" }) In other words, if we consider

$$\Gal(\mathbb{L}/\mathbb{K})\hookrightarrow \prod_{x\in \mathbb{L}}\mathbb{L}\overset{\pr_x}{\longrightarrow}\mathbb{L};\qquad \sigma\mapsto \sigma(x)$$

the image of this map is a finite set. Therefore $\Gal(\mathbb{L}/\mathbb{K})$ is a subset of a product of finite sets, and since finite sets are compact, this product is also compact. ([\[Topology\] §Compactness and Convergence of Filters, ⁋Theorem 19 (Tychonoff)](/en/math/topology/filter_convergence#thm19){: data-lid="fa6xx" }) Thus proving the given proposition amounts to showing that $\Gal(\mathbb{L}/\mathbb{K})$ is closed in $\mathbb{L}^\mathbb{L}$.

Suppose a function $u$ belongs to the closure of $\Gal(\mathbb{L}/\mathbb{K})$ in $\mathbb{L}^\mathbb{L}$. First, a field homomorphism $u:\mathbb{L}\rightarrow\mathbb{L}$ fixing $\mathbb{K}$ is always an element of $\Gal(\mathbb{L}/\mathbb{K})$, because $u$ is injective and, for any $x\in \mathbb{L}$, maps the finite set of roots in $\mathbb{L}$ of the minimal polynomial of $x$ to itself and is thus bijective on it, so $x$ belongs to the image of $u$. Therefore, if $u$ is not an element of $\Gal(\mathbb{L}/\mathbb{K})$, then either $u$ is not a field homomorphism or $u$ does not fix $\mathbb{K}$. Adopting the first assumption, suppose for instance that there exist $x,y\in\mathbb{L}$ such that $u(x+y)\neq u(x)+u(y)$. Then the set

$$\left\{f\in \mathbb{L}^\mathbb{L}\mid f(x)=u(x),f(y)=u(y),f(x+y)=u(x+y)\right\}$$

is a basic open set in $\mathbb{L}^\mathbb{L}$ and hence is open, and moreover it contains $u$. That is, this set is an open neighborhood of $u$. However, by assumption

$$f(x+y)=u(x+y)\neq u(x)+u(y)=f(x)+f(y)$$

so these $f$ also fail to be field homomorphisms. That is, the above open neighborhood does not intersect $\Gal(\mathbb{L}/\mathbb{K})$, which contradicts the assumption that $u$ belongs to the closure of $\Gal(\mathbb{L}/\mathbb{K})$. By similar reasoning all other cases can also be ruled out, and from this we can prove that $\Gal(\mathbb{L}/\mathbb{K})$ is closed in $\mathbb{L}^\mathbb{L}$.
:::

Now let $\mathbb{L}/\mathbb{K}$ be a Galois extension, let Galois subextensions $\mathbb{L}_i/\mathbb{K}$ of this extension satisfy $\mathbb{L}=\bigcup_{i\in I}\mathbb{L}_i$, and suppose that for any $i,j\in I$ there exists $k\in I$ such that $\mathbb{L}_i\cup\mathbb{L}_j\subseteq \mathbb{L}_k$. Then we endow this with the partial order

$$i\leq j \iff \mathbb{L}_i\subseteq \mathbb{L}_j$$

and under this partial order we can define the following restriction maps

$$\rho_{ij}:\Gal(\mathbb{L}_j/\mathbb{K}) \rightarrow \Gal(\mathbb{L}_i/\mathbb{K})\qquad \text{whenever $i\leq j$}$$

Then these are continuous homomorphisms, and therefore their inverse limit

$$\varprojlim_{i\in I}\Gal(\mathbb{L}_i/\mathbb{K})=\left\{(\sigma_i)\in\prod_{i\in I}\Gal(\mathbb{L}_i/\mathbb{K})\mid\text{$\rho_{ij}(\sigma_j)=\sigma_i$ whenever $i\leq j$}\right\}$$

and canonical morphisms $\rho_i:\varprojlim \Gal(\mathbb{L}_i/\mathbb{K})\rightarrow\Gal(\mathbb{L}_i/\mathbb{K})$ exist. ([\[Category Theory\] §Limits, ⁋Example 5](/en/math/category_theory/limits#ex5){: data-lid="vherg" })

On the other hand, considering the restriction maps

$$\lambda_i:\Gal(\mathbb{L}/\mathbb{K})\rightarrow\Gal(\mathbb{L}_i/\mathbb{K})$$

they satisfy $\lambda_i=\rho_{ij}\circ\lambda_j$, so there exists an induced continuous homomorphism $\lambda:\Gal(\mathbb{L}/\mathbb{K})\rightarrow\varprojlim\Gal(\mathbb{L}_i/\mathbb{K})$.

::: Proposition 5
The $\lambda$ defined above defines an isomorphism between topological groups.
:::
::: Proof
Each $\Gal(\mathbb{L}_i/\mathbb{K})$ is a subspace of the Hausdorff space $\mathbb{L}_i^{\mathbb{L}_i}$ and hence is Hausdorff, and since products and subspaces of Hausdorff spaces are again Hausdorff, their inverse limit $\varprojlim \Gal(\mathbb{L}_i/\mathbb{K})$ is also Hausdorff. On the other hand, since $\Gal(\mathbb{L}/\mathbb{K})$ is compact by [Proposition 4](#prop4){: data-lid="39hru" }, by [\[Topology\] §Compact Spaces, ⁋Proposition 9](/en/math/topology/compact_spaces#prop9){: data-lid="jimmm" } it suffices to show that $\lambda$ is bijective.

First, if $\lambda(\sigma)$ is the identity, then for any $i$ we have $\sigma\vert_{\mathbb{L}_i}=\id_{\mathbb{L}_i}$, and since $\mathbb{L}=\bigcup_i\mathbb{L}_i$, we have $\sigma=\id_\mathbb{L}$. That is, $\lambda$ is injective. Now let $(\sigma_i)\in\varprojlim\Gal(\mathbb{L}_i/\mathbb{K})$ be given, and for $x\in \mathbb{L}_i$ define $\sigma(x)=\sigma_i(x)$. If $x$ belongs to both $\mathbb{L}_i$ and $\mathbb{L}_j$, then with $\mathbb{L}_i\cup\mathbb{L}_j\subseteq \mathbb{L}_k$ for some $k$, we have $\sigma_i(x)=\rho_{ik}(\sigma_k)(x)=\sigma_k(x)$ and by the same reasoning $\sigma_j(x)=\sigma_k(x)$, so $\sigma$ is well-defined, and any two elements of $\mathbb{L}$ also belong together to a single $\mathbb{L}_k$, so $\sigma$ is a field homomorphism fixing $\mathbb{K}$. On the other hand, since the $\rho_{ij}$ are homomorphisms, $(\sigma_i^{-1})$ is also an element of $\varprojlim\Gal(\mathbb{L}_i/\mathbb{K})$, and the function obtained in the same way is the inverse of $\sigma$. That is, $\sigma\in\Gal(\mathbb{L}/\mathbb{K})$ and $\lambda(\sigma)=(\sigma_i)$, so $\lambda$ is surjective.
:::

In particular, the family of finite degree Galois subextensions $\Ext_{\fin,\gal}(\mathbb{L}/\mathbb{K})$ satisfies the conditions of this proposition. This is because the compositum of two elements of this family is again a finite degree Galois subextension by [§Galois Extensions, ⁋Proposition 10](/en/math/field_theory/galois_extension#prop10){: data-lid="dbv05" }, and in $\mathbb{L}$, any element $x$ belongs to an element containing $\mathbb{K}(x)$ in $\Ext_{\fin,\gal}(\mathbb{L}/\mathbb{K})$. That is, the Galois group of any Galois extension is an inverse limit of finite groups, namely a *profinite group*.

## Galois Cohomology

The Galois group is not merely a group, but a group acting on $\mathbb{L}$, and in particular on the multiplicative group $\mathbb{L}^\times$. The standard tool for extracting the arithmetic information contained in this action is *Galois cohomology*, and to conclude this post, we examine Hilbert's Theorem 90, the classical theorem at its starting point. In this section, $\mathbb{L}/\mathbb{K}$ is a finite degree Galois extension and $G=\Gal(\mathbb{L}/\mathbb{K})$.

::: Definition 6
A function $\varphi:G \rightarrow \mathbb{L}^\times$ is called a *1-cocycle* if for any $\sigma,\tau\in G$ the equation

$$\varphi(\sigma\tau)=\varphi(\sigma)\cdot\sigma\bigl(\varphi(\tau)\bigr)$$

holds. In particular, for some $c\in\mathbb{L}^\times$, a 1-cocycle of the form $\varphi(\sigma)=\sigma(c)/c$ is called a *1-coboundary*.
:::

First, we verify that a 1-coboundary is indeed a 1-cocycle:

$$\varphi(\sigma)\cdot\sigma(\varphi(\tau))=\frac{\sigma(c)}{c}\cdot\sigma\left(\frac{\tau(c)}{c}\right)=\frac{\sigma(c)}{c}\cdot\frac{\sigma\tau(c)}{\sigma(c)}=\frac{\sigma\tau(c)}{c}=\varphi(\sigma\tau)$$

Also, since $\mathbb{L}^\times$ is abelian, the 1-cocycles form an abelian group under pointwise multiplication, and since $c\mapsto(\sigma\mapsto\sigma(c)/c)$ is a group homomorphism, the 1-coboundaries form a subgroup of it. Therefore we can consider the quotient group, which we denote by $H^1(G,\mathbb{L}^\times)$. Hilbert's Theorem 90 states that this group carries no information at all.

::: Theorem 7 (Hilbert 90)
For a finite degree Galois extension $\mathbb{L}/\mathbb{K}$, every 1-cocycle $\varphi:G \rightarrow \mathbb{L}^\times$ is a 1-coboundary. That is, $H^1(G,\mathbb{L}^\times)$ is trivial.
:::
::: Proof
The elements of $G$ are distinct homomorphisms from $\mathbb{L}$ to $\mathbb{L}$, so by [§Étale Algebras, ⁋Corollary 3](/en/math/field_theory/etale_algebras#cor3){: data-lid="kcojb" } they are linearly independent in the $\mathbb{L}$-vector space. Since the values of $\varphi$ are all non-$0$, the linear combination

$$\sum_{\tau\in G}\varphi(\tau)\tau$$

is not the zero map, and therefore for some $x\in\mathbb{L}$ we have

$$b=\sum_{\tau\in G}\varphi(\tau)\tau(x)\neq0$$

Now for any $\sigma\in G$, writing the cocycle condition as $\sigma(\varphi(\tau))=\varphi(\sigma)^{-1}\varphi(\sigma\tau)$, we compute

$$\sigma(b)=\sum_{\tau\in G}\sigma(\varphi(\tau))\sigma\tau(x)=\varphi(\sigma)^{-1}\sum_{\tau\in G}\varphi(\sigma\tau)\sigma\tau(x)=\varphi(\sigma)^{-1}b$$

The last equality holds because as $\tau$ ranges over all of $G$, $\sigma\tau$ also ranges over all of $G$. Therefore, setting $c=b^{-1}$, we have

$$\varphi(\sigma)=\frac{b}{\sigma(b)}=\frac{\sigma(c)}{c}$$

so $\varphi$ is a 1-coboundary.
:::

The classical form of Hilbert 90 concerns cyclic extensions. Let $G=\langle\sigma\rangle$ be a cyclic group of order $n$, and define the *norm* of $x\in\mathbb{L}$ by

$$N_{\mathbb{L}/\mathbb{K}}(x)=\prod_{i=0}^{n-1}\sigma^i(x)$$

Applying $\sigma$ merely permutes the factors, so $N_{\mathbb{L}/\mathbb{K}}(x)$ is $G$-invariant, and since $\mathbb{L}/\mathbb{K}$ is Galois, by [§Galois Extensions, ⁋Theorem 8](/en/math/field_theory/galois_extension#thm8){: data-lid="0c0mf" } we have $N_{\mathbb{L}/\mathbb{K}}(x)\in\mathbb{K}$.

::: Corollary 8
Let $\mathbb{L}/\mathbb{K}$ be a finite degree Galois extension and let $G=\Gal(\mathbb{L}/\mathbb{K})=\langle\sigma\rangle$ be cyclic. Then for $x\in\mathbb{L}^\times$, the following are equivalent.

1. $N_{\mathbb{L}/\mathbb{K}}(x)=1$.
2. There exists $y\in\mathbb{L}^\times$ such that $x=\sigma(y)/y$.
:::
::: Proof
First, assuming the second condition, we have

$$N_{\mathbb{L}/\mathbb{K}}\bigl(\sigma(y)/y\bigr)=\prod_{i=0}^{n-1}\frac{\sigma^{i+1}(y)}{\sigma^i(y)}=\frac{\sigma^n(y)}{y}=1$$

The middle equality is telescoping and the last equality is because $\sigma^n=\id_\mathbb{L}$.

Conversely, assume $N_{\mathbb{L}/\mathbb{K}}(x)=1$. Define the function $\varphi:G \rightarrow \mathbb{L}^\times$ by

$$\varphi(\sigma^i)=\prod_{k=0}^{i-1}\sigma^k(x)\qquad(0\leq i\leq n-1)$$

Here, when $i=0$, the empty product gives $\varphi(\id)=1$. Let us verify that this is a 1-cocycle. For $0\leq a,b\leq n-1$, we have

$$\varphi(\sigma^a)\cdot\sigma^a\bigl(\varphi(\sigma^b)\bigr)=\prod_{k=0}^{a-1}\sigma^k(x)\cdot\prod_{k=0}^{b-1}\sigma^{a+k}(x)=\prod_{k=0}^{a+b-1}\sigma^k(x)$$

If $a+b\leq n-1$, then by definition this is $\varphi(\sigma^{a+b})=\varphi(\sigma^a\sigma^b)$. If $a+b\geq n$, then since $\sigma^k=\sigma^{k-n}$ ($k\geq n$),

$$\prod_{k=0}^{a+b-1}\sigma^k(x)=\prod_{k=0}^{n-1}\sigma^k(x)\cdot\prod_{k=n}^{a+b-1}\sigma^k(x)=N_{\mathbb{L}/\mathbb{K}}(x)\cdot\prod_{k=0}^{a+b-n-1}\sigma^k(x)=\varphi(\sigma^{a+b-n})$$

and since $\sigma^a\sigma^b=\sigma^{a+b-n}$, the cocycle condition holds as well. The assumption $N_{\mathbb{L}/\mathbb{K}}(x)=1$ was used in the last equality.

Now by [Theorem 7](#thm7){: data-lid="85it1" }, $\varphi$ is a 1-coboundary. That is, for some $c\in\mathbb{L}^\times$ we have $\varphi(\sigma^i)=\sigma^i(c)/c$, and in particular for $i=1$,

$$x=\varphi(\sigma)=\frac{\sigma(c)}{c}$$

so we may set $y=c$.
:::

---

**References**

**[Bou]** N. Bourbaki. *Algebra II: Chapters 4–7*. Springer, 2003.  

---
