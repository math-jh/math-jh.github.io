---
title: "Cohomology"
description: "We define cohomology, the dual concept to homology, and show that spaces with the same homology can still be topologically distinct by introducing the natural ring structure on cohomology."
excerpt: "Definition of cohomology and the universal coefficient theorem"

categories: [Math / Algebraic Topology]
permalink: /en/math/algebraic_topology/cohomology
sidebar: 
    nav: "algebraic_topology-en"

date: 2025-09-07
weight: 9
translated_at: 2026-08-18T14:45:05+00:00
translation_source: kimi-cli
last_polished_at: 2026-08-18T14:45:05+00:00
---
As its name suggests, cohomology may be regarded as the dual of homology. However, if the $k$th cohomology $H^k(X)$ of a space $X$ were simply the dual of the $k$th homology $H_k(X)$, there would be little reason to consider it separately.

In fact, cohomology provides a more refined invariant than homology: for instance, it carries a natural product structure, and two spaces with the same homology may nevertheless fail to be homotopic if their cohomology rings differ. In this post, we review the definition of cohomology and its basic properties.

## The Universal Coefficient Theorem for Homology

Before diving into the main discussion, we first revisit homology with coefficients, which was treated after [§Computing Homology, ⁋Definition 6](/en/math/algebraic_topology/computation_of_homology#def6). When defining simplicial or singular homology, we considered the chain complexes obtained by taking the tensor product with an abelian group $A$,

$$C_\bullet(X;A):=C_\bullet(X)\otimes_\mathbb{Z}A,\qquad C_\bullet^\Delta(X;A):=C_\bullet^\Delta(X)\otimes_\mathbb{Z}A$$

and defined the homology groups

$$H_k(X;A),\qquad H_k^\Delta(X;A)$$

from these. To compute these in practice, one might hope that $H_k(X;A)$ or $H_k^\Delta(X;A)$ could be expressed simply as $H_k(X)\otimes_\mathbb{Z}A$ or $H_k^\Delta(X)\otimes_\mathbb{Z}A$. However, since the tensor product is right-exact but not left-exact in general, this would be too optimistic; we need an additional measurement of the information lost under tensoring.

To this end, consider a chain complex $C_\bullet$ of free abelian groups and the short exact sequence in $\Ch_{\geq 0}(\Ab)$

$$0 \rightarrow Z_\bullet \rightarrow C_\bullet \rightarrow B_{\bullet-1}\rightarrow 0\tag{1}$$

where $Z_k=\ker(\partial:C_k \rightarrow C_{k-1})$, $B_{k-1}=\im(\partial:C_k \rightarrow C_{k-1})$, the first map is the inclusion, and the second is the boundary map $\partial$.

Since $Z_k$ and $B_{k-1}$ are subgroups of the free abelian groups $C_k$ and $C_{k-1}$, they are themselves free; in particular, because $B_{k-1}$ is free, choosing a preimage for each basis element yields a section $B_{k-1}\rightarrow C_k$. Thus this short exact sequence is split, and hence for any abelian group $A$, the sequence

$$0 \rightarrow Z_\bullet\otimes_\mathbb{Z}A \rightarrow C_\bullet\otimes_\mathbb{Z}A \rightarrow B_{\bullet-1}\otimes_\mathbb{Z}A\rightarrow 0$$

is also split short exact. The splitting gives a direct sum decomposition $C_\bullet\cong Z_\bullet\oplus B_{\bullet-1}$, and since tensor products commute with direct sums, this decomposition persists after applying $\otimes_\mathbb{Z}A$. Unpacking these, we obtain a commutative diagram of the form

{% diagram Math/Algebraic_Topology/Cohomology-1.svg width="31.09em" alt="snake_lemma" %}

and therefore, by [\[Homological Algebra\] §Long Exact Sequence, ⁋Theorem 1](/en/math/homological_algebra/long_exact_sequence#thm1), the long exact sequence

$$\cdots \rightarrow B_k\otimes_\mathbb{Z}A\overset{\delta_k}{\longrightarrow}Z_k\otimes_\mathbb{Z}A\rightarrow H_k(C\otimes A)\rightarrow B_{k-1}\otimes_\mathbb{Z}A\overset{\delta_{k-1}}{\longrightarrow} Z_{k-1}\otimes_\mathbb{Z}A\rightarrow\cdots\tag{2}$$

To extract information from this exact sequence, we examine the connecting maps $\delta$. Tracing through the definition, $\delta_k:B_k\otimes_\mathbb{Z}A\rightarrow Z_k\otimes_\mathbb{Z}A$ is precisely $i_k\otimes\id_A$, where $i_k:B_k\rightarrow Z_k$ is the inclusion homomorphism. Thus, considering the short exact sequence

$$0 \rightarrow B_k\overset{i_k}{\longrightarrow} Z_k \overset{p_k}{\longrightarrow}H_k(C)\rightarrow 0$$

since $B_k$, $Z_k$, and $0$ are all free abelian groups, this may be viewed as a free resolution of $H_k(C_\bullet)$, and by definition we may fit $\delta_k$ into the exact sequence

$$0 \rightarrow \Tor_1^\mathbb{Z}(H_k(C), A)\rightarrow B_k\otimes_\mathbb{Z}A\overset{\delta_k}{\longrightarrow} Z_k\otimes_\mathbb{Z}A\rightarrow H_k(C)\otimes_\mathbb{Z}A\rightarrow 0$$

Hence we have isomorphisms

$$\ker\delta_{k-1}\cong \Tor_1^\mathbb{Z}(H_{k-1}(C), A),\qquad \coker\delta_k\cong H_k(C)\otimes_\mathbb{Z} A$$

and substituting these into (2) yields the short exact sequence

$$0 \rightarrow H_k(C)\otimes_\mathbb{Z}A\rightarrow H_k(C;A)\rightarrow \Tor_1^\mathbb{Z}(H_{k-1}(C), A)\rightarrow 0$$

On the other hand, since (1) is a split short exact sequence, we may choose a retraction $r_k:C_k\rightarrow Z_k$. ([\[Multilinear Algebra\] §Exact Sequences, ⁋Proposition 10](/en/math/multilinear_algebra/exact_sequences#prop10)) With this choice, $(p_k\circ r_k)\otimes\id_A$ induces a map $H_k(C;A)\rightarrow H_k(C)\otimes_\mathbb{Z} A$ on homology, and one checks that this is a retraction of the map $H_k(C)\otimes_\mathbb{Z}A\rightarrow H_k(C;A)$ above. Thus we obtain:

::: Proposition 1 (Universal coefficient theorem for homology)
For any topological space $X$ and abelian group $A$, there exists a short exact sequence

$$0 \rightarrow H_k(X)\otimes_\mathbb{Z}A\rightarrow H_k(X;A)\rightarrow \Tor_1^\mathbb{Z}(H_{k-1}(X), A)\rightarrow 0$$

Moreover, this sequence splits (non-canonically), and therefore we have a (non-canonical) isomorphism

$$H_k(X;A)\cong \left(H_k(X)\otimes_\mathbb{Z}A\right)\oplus \Tor_1^\mathbb{Z}(H_{k-1}(X), A)$$
:::


## Definition of Cohomology and the Universal Coefficient Theorem

Just as in [§Computing Homology, ⁋Definition 6](/en/math/algebraic_topology/computation_of_homology#def6), we define the Eilenberg-Steenrod axioms for cohomology; a contravariant functor together with connecting morphisms satisfying these axioms will be called a cohomology theory. Explicitly, the axioms are as follows.

::: Definition 2 (Eilenberg-Steenrod axioms)
For contravariant functors $H^k$ from the category of pairs of topological spaces to the category of abelian groups, together with natural transformations

$$\delta: H^k(A) \rightarrow H^{k+1}(X,A)$$

the *Eilenberg-Steenrod axioms* are the following:

- (Homotopy) If two maps $(X,A)\rightarrow(Y,B)$ are homotopic, then the induced homomorphisms $H^k(Y,B)\rightarrow H^k(X,A)$ coincide.
- (Excision) For $(X,A,Z)$ satisfying the conditions of [§Computing Homology, ⁋Theorem 2](/en/math/algebraic_topology/computation_of_homology#thm2), the inclusion $(X\setminus Z, A\setminus Z)\hookrightarrow(X,A)$ induces an isomorphism.
- (Dimension) For the one-point space $\ast$, we have $H^k(\ast)=0$ for all $k>0$.
- (Additivity) If $X=\coprod X_\alpha$, then $H^k(X)\cong\prod H^k(X_\alpha)$.
- (Exactness) For each pair $(X,A)$ and the two inclusions $(A,\emptyset)\hookrightarrow(X,\emptyset)$ and $(X,\emptyset)\hookrightarrow(X,A)$, we have the long exact sequence

    $$\cdots \rightarrow H^k(X,A)\rightarrow H^k(X) \rightarrow H^k(A) \rightarrow H^{k+1}(X,A)\rightarrow \cdots$$
:::

To establish the existence of a cohomology theory satisfying these conditions, just as in [§Homology](/en/math/algebraic_topology/homology), we consider the chain complex of singular simplices of a topological space $X$,

$$C_\bullet(X):\qquad\cdots \rightarrow C_{k+1}(X)\rightarrow C_k(X) \rightarrow C_{k-1}(X)\rightarrow \cdots$$

Fixing an abelian group $A$ as the coefficient group, we may form the dual cochain complex

$$(C^\vee)^\bullet(X;A):\qquad\cdots \leftarrow \Hom_\mathbb{Z}(C_{k+1}(X), A)\leftarrow\Hom_\mathbb{Z}(C_k(X),A)\leftarrow\Hom_\mathbb{Z}(C_{k-1}(X),A)\leftarrow\cdots$$

If $A$ is a commutative ring, then the adjunction of [\[Algebraic Structures\] §Change of Scalars, ⁋Proposition 6](/en/math/algebraic_structures/change_of_base_ring#prop6) for the ring homomorphism $\mathbb{Z}\rightarrow A$ gives an isomorphism $\Hom_A(M\otimes_\mathbb{Z}A,N)\cong\Hom_\mathbb{Z}(M,N)$ for any abelian group $M$ and $A$-module $N$. Hence in this case the above cochain complex may be written as

$$\qquad \cdots\leftarrow\Hom_A(C_{k+1}(X;A),A)\leftarrow \Hom_A(C_k(X;A),A)\leftarrow \Hom_A(C_{k-1}(X;A),A)\leftarrow\cdots$$

so it may be regarded as the dual of the chain complex $C_\bullet(X;A)$. We then define the $k$th homology of this cochain complex $(C^\vee)^\bullet(X;A)$ as

$$H^k(X;A):=H_k(C^\vee)$$

and call it the *$k$th cohomology* of $X$. The use of superscripts on $H$ and $C^\vee$ to denote the index is because, in contrast to homology, the long exact sequence runs in the direction of increasing indices; hereafter, when there is no risk of confusion, we shall write $C^\bullet(X;A)$ for $(C^\vee)^\bullet(X;A)$.

We must now examine the relationship between $H^k(X;A)$ and $H_k(X)$ thus defined. As noted at the outset, it is not the case that $H^k(X;A)\cong H_k(X)^\ast$ in general. However, by an argument similar to the proof of [Proposition 1](#prop1) above, we obtain the following proposition.

::: Proposition 3 (Universal coefficient theorem for cohomology)
For any topological space $X$ and abelian group $A$, there exists a short exact sequence

$$0\rightarrow\Ext_\mathbb{Z}^1(H_{k-1}(X), A)\rightarrow H^k(X;A)\rightarrow \Hom_\mathbb{Z}(H_k(X),A)\rightarrow 0$$

Moreover, this sequence splits (non-canonically), and therefore we have a (non-canonical) isomorphism

$$H^k(X;A)\cong \Hom_\mathbb{Z}(H_k(X),A)\oplus \Ext^1_\mathbb{Z}(H_{k-1}(X),A)$$
:::

Roughly speaking, this may be thought of as translating [Proposition 1](#prop1) via [\[Algebraic Structures\] §Abelian Groups, ⁋Theorem 15](/en/math/algebraic_structures/abelian_groups#thm15).

## de Rham Cohomology

Associating a chain complex $C_\bullet(X)$ to a topological space $X$ may be viewed as algebraically encoding information about the subspaces of $X$. In defining cohomology, we apply $\Hom_\mathbb{Z}(-,A)$ to $C_\bullet(X)$ and take the homology of the resulting cochain complex; here

$$C^k(X;A)=\Hom_\mathbb{Z}(C_k(X), A)$$

and an arbitrary element of this group may be thought of as a function assigning an element of $A$ to each element of $C_k(X)$ (that is, to each $k$-chain). Thus cohomology is, in essence, concerned with functions defined on the space.

More concretely, for any $c\in C_k(X)$ and $\varphi\in C^k(X;A)$, we have the canonical pairing

$$C_k(X)\times C^k(X;A)\rightarrow A;\qquad (c,\varphi)\mapsto \varphi(c)\in A$$

and if we denote the boundary map of $C_\bullet(X)$ by $\partial$ and the induced coboundary map of $C^\bullet(X;A)$ by $\delta$, then for any $c\in C_{k+1}(X)$ and $\varphi\in C^k(X;A)$ we have the identity

$$\langle \partial c, \varphi\rangle=\langle c, \delta\varphi\rangle$$

from which we obtain the pairing at the level of homology and cohomology

$$H_k(X)\times H^k(X;A)\rightarrow A$$[^1]

For example, to see de Rham cohomology, consider the $\mathbb{R}$-vector spaces of differential $k$-forms

$$\Omega^k(\mathbb{R}^n)=\{\text{$k$-forms on $\mathbb{R}^n$}\}$$

Here the coboundary map $\Omega^k(\mathbb{R}^n)\rightarrow \Omega^{k+1}(\mathbb{R}^n)$ is given by the exterior derivative, and a differential $k$-form produces a number via integration when a $k$-dimensional subspace is given. Moreover, closed $k$-forms are the kernel of this coboundary, and exact $k$-forms are its image.

For instance, consider the differential $2$-form on $\mathbb{R}^3$

$$\omega=\dd{x}\wedge \dd{y}$$

A $2$-dimensional subspace of $\mathbb{R}^3$ is given by a map from a (unit) rectangle in $\mathbb{R}^2$ into $\mathbb{R}^3$, and through this we know what it means to apply $\omega$ to a $2$-dimensional subspace.

For example, given the set

$$S = \{ (x, y, 0) \mid 0 \leq x \leq 1, 0 \leq y \leq 1 \}$$

the value of $\omega$ on this set is simply computed as

$$\int_S \omega = \int_{x=0}^{1} \int_{y=0}^{1} 1\dd{y}\dd{x} = 1$$

As another example, if the surface

$$\Sigma = \{ (x, y, z) \mid x^2 + y^2 + z^2 = 1,\ z \geq 0 \}$$

is given, we first parametrize it as a map from $[0,\pi/2]\times[0,2\pi]$ to $\Sigma$ using spherical coordinates

$$x = \sin \phi \cos \theta,\qquad y = \sin \phi \sin \theta,\qquad z = \cos \phi$$

and then, using $\dd{x} \wedge \dd{y} = \sin \phi \cos \phi\dd{\phi} \wedge \dd{\theta}$, we compute the integral as

$$\begin{align*}
\int_{\Sigma} \omega
&= \int_{0}^{2\pi} \int_{0}^{\pi/2} \sin \phi \cos \phi\dd{\phi} \dd{\theta} = \int_{0}^{2\pi} \dd{\theta} \int_{0}^{\pi/2} \sin \phi \cos \phi\dd{\phi} \\
&= 2\pi \times \frac{1}{2} \int_{0}^{\pi/2} \sin(2\phi) \dd{\phi} = 2\pi \times \frac{1}{2} \left[ -\frac{1}{2} \cos(2\phi) \right]_{0}^{\pi/2} \\
&= 2\pi \times \frac{1}{2} \left( -\frac{1}{2} [\cos(\pi) - \cos(0)] \right) = 2\pi \times \frac{1}{2} \left( -\frac{1}{2}(-1 - 1) \right) = 2\pi \times \frac{1}{2} \times 1 \\
&= \pi
\end{align*}$$

Thus the differential $2$-form $\omega$ may be thought of as a function that takes a $2$-dimensional subspace such as $S$ or $\Sigma$ and returns a number.

Now, by the Poincaré lemma, we know that for any $k>0$, every closed $k$-form on $\mathbb{R}^n$ is the exterior derivative of some $(k-1)$-form. Hence for any $k>0$,

$$H^k_\dR(\mathbb{R}^n)=0$$

and for $k=0$, the functions with vanishing derivative are exactly the constant functions, so

$$H^0_\dR(\mathbb{R}^n)=\mathbb{R}$$

This de Rham cohomology, defined in this manner, also satisfies all the conditions of [Definition 2](#def2) on the category of pairs of smooth manifolds; therefore, by the uniqueness of cohomology theories and the fact that any singular chain can be approximated by a smooth chain, we may verify that singular cohomology with $\mathbb{R}$ coefficients and de Rham cohomology coincide. The computation above is then nothing more than translating the computation of [§Homology, ⁋Proposition 11](/en/math/algebraic_topology/homology#prop11) into $\mathbb{R}$-valued cohomology via [Proposition 3](#prop3).
 
## Coefficients of (Co)homology

The de Rham cohomology reviewed above is an example of a cohomology theory whose coefficient group is not $\mathbb{Z}$. Unlike singular or simplicial cohomology, de Rham cohomology has $\mathbb{R}$ as its coefficient group by definition.

Such a cohomology theory enjoys nice properties: for instance, since $\mathbb{R}$ is a torsion-free abelian group, $\Tor_1^\mathbb{Z}(A,\mathbb{R})=0$ holds for any abelian group $A$, and hence by [Proposition 1](#prop1) we have the isomorphism

$$H_k(X;\mathbb{R})\cong H_k(X)\otimes_\mathbb{Z}\mathbb{R}$$

Moreover, since $\mathbb{R}$ is an injective $\mathbb{Z}$-module, $\Ext_\mathbb{Z}^1(A,\mathbb{R})=0$ for any abelian group $A$, and thus this time [Proposition 3](#prop3) gives the isomorphism

$$H^k(X;\mathbb{R})\cong \Hom_\mathbb{Z}(H_k(X),\mathbb{R})$$

It is then of separate interest to study homology and cohomology of this kind. Recalling the chain complexes used to define $H_k(X;A)$ and $H^k(X;A)$, we know that if $A$ were a ring, the two chain complexes

$$C_\bullet(X;A):=C_\bullet(X)\otimes_\mathbb{Z}A,\qquad C_\bullet^\Delta(X;A):=C_\bullet^\Delta(X)\otimes_\mathbb{Z}A$$

are chain complexes of $A$-modules, and the previously defined $C^\bullet(X;A)$ is also such. Hence taking homology or cohomology of these yields $A$-modules as well.

On the other hand, we know that if $A$ is a principal ideal domain, then any submodule of a free $A$-module is again a free $A$-module. Re-examining the proof of [Proposition 1](#prop1), we see that it exploited the fact that $\mathbb{Z}$ is a principal ideal domain, so that submodules of free $\mathbb{Z}$-modules (i.e., free abelian groups) are again free $\mathbb{Z}$-modules. Based on this, we may generalize the preceding two propositions as follows.

::: Theorem 4 (Universal coefficient theorem for homology, general version)
Let $A$ be a principal ideal domain, $C_\bullet$ a chain complex of free $A$-modules, and $M$ an arbitrary $A$-module. Then there exists a short exact sequence

$$0 \rightarrow H_k(C)\otimes_AM\rightarrow H_k(C\otimes_AM)\rightarrow \Tor_1^A(H_{k-1}(C), M)\rightarrow 0$$

Moreover, this sequence splits (non-canonically), and therefore we have a (non-canonical) isomorphism

$$H_k(C\otimes_AM)\cong \left(H_k(C)\otimes_AM\right)\oplus \Tor_1^A(H_{k-1}(C), M)$$
:::

::: Theorem 5 (Universal coefficient theorem for cohomology, general version)
Let $A$ be a principal ideal domain, $C_\bullet$ a chain complex of free $A$-modules, and $M$ an arbitrary $A$-module. Then there exists a short exact sequence

$$0\rightarrow\Ext_A^1(H_{k-1}(C), M)\rightarrow H_k(\Hom_A(C,M))\rightarrow \Hom_A(H_k(C),M)\rightarrow 0$$

Moreover, this sequence splits (non-canonically), and therefore we have a (non-canonical) isomorphism

$$H_k(\Hom_A(C,M))\cong \Hom_A(H_k(C),M)\oplus \Ext^1_A(H_{k-1}(C),M)$$
:::

## The Mayer-Vietoris Sequence

Among the axioms of [Definition 2](#def2), the excision axiom allows us to compute the cohomology of a large space from that of smaller ones. The following proposition is the cohomology version of [\[Algebraic Topology\] §Computing Homology, ⁋Proposition 7](/en/math/algebraic_topology/computation_of_homology#prop7), and its proof is obtained by repeating the passage from [\[Algebraic Topology\] §Computing Homology, ⁋Definition 6](/en/math/algebraic_topology/computation_of_homology#def6) to [\[Algebraic Topology\] §Computing Homology, ⁋Proposition 7](/en/math/algebraic_topology/computation_of_homology#prop7), starting from [Definition 2](#def2).

::: Proposition 6 (Mayer-Vietoris sequence)
Suppose a topological space $X$ is expressed as the union $X=U\cup V$ of two open sets, and let $H$ be a cohomology theory defined on $X$. Then there exists a long exact sequence

$$\cdots \rightarrow H^{n}(X) \xrightarrow{(i^\ast, j^\ast)} H^{n}(U) \oplus H^{n}(V) \xrightarrow{k^\ast - l^\ast} H^{n}(U \cap V) \xrightarrow{\delta} H^{n+1}(X) \rightarrow \cdots$$

where $i^\ast, j^\ast, k^\ast, l^\ast$ are the maps induced by the inclusions

$$i:U\rightarrow X,\quad j:V\rightarrow X,\quad k:U\cap V\rightarrow U,\quad l:U\cap V \rightarrow V$$
:::

## Tensor Product of Chain Complexes

The Mayer-Vietoris sequence allows us to compute the homology or cohomology of a large space from those of its small subspaces. On the other hand, we may also form a larger space $X\times Y$ as the product of two spaces $X$ and $Y$; the Künneth formula helps compute the homology and cohomology of such product spaces. To this end, we first define the tensor product of two chain complexes $C_\bullet$ and $D_\bullet$.

::: Definition 7
Let $A$ be a ring and $C_\bullet$, $D_\bullet$ chain complexes of $A$-modules. Their *tensor product* $(C\otimes D)_\bullet$ is defined by

$$(C\otimes D)_k=\bigoplus_{p+q=k}C_p\otimes_A D_q$$

for each $k$, with differential on homogeneous elements given by

$$\partial(x\otimes y)=\partial^Cx\otimes y+(-1)^{\deg(x)}x\otimes\partial^Dy$$

and extended linearly.
:::

That is, $(C\otimes D)_\bullet$ is the total complex of the double complex whose $(p,q)$-entry is $C_p\otimes D_q$, with horizontal differential $\partial^C\otimes\id_D$ and vertical differential $\id_C\otimes\partial^D$. ([§Homology, ⁋Definition 5](/en/math/homological_algebra/homology#def5))

The algebraic content of the Künneth formula is contained in the following lemma.

::: Lemma 8
Let $A$ be a principal ideal domain and $C_\bullet$, $D_\bullet$ chain complexes of $A$-modules, and suppose $C_\bullet$ is a chain complex of free $A$-modules. Then for any $k$, there exists a short exact sequence

$$0 \rightarrow \bigoplus_{p+q=k}H_p(C)\otimes_AH_q(D)\rightarrow H_k(C\otimes D)\rightarrow \bigoplus_{p+q=k-1}\Tor_1^A(H_p(C),H_q(D))\rightarrow 0$$

Moreover, this short exact sequence splits (non-canonically), and therefore there exists an isomorphism

$$H_k(C\otimes D)\cong \left( \bigoplus_{p+q=k}H_p(C)\otimes_AH_q(D)\right)\oplus \left(\bigoplus_{p+q=k-1}\Tor_1^A(H_p(C),H_q(D)) \right)$$
:::
::: Proof
Consider the short exact sequence

$$0 \rightarrow Z_p(C) \rightarrow C_p\rightarrow B_{p-1}(C)\rightarrow 0$$

Since $B_{p-1}(C)$ and $Z_p(C)$ are submodules of the free $A$-modules $C_{p-1}$ and $C_p$, and $A$ is a principal ideal domain, they are again free $A$-modules. Hence tensoring this short exact sequence with $D_q$ yields the short exact sequence

$$0\rightarrow Z_p(C)\otimes D_q \rightarrow C_p\otimes D_q \rightarrow B_{p-1}(C)\otimes D_q\rightarrow 0$$

By the definition of the chain complex $(C\otimes D)_\bullet$, taking the direct sum of such short exact sequences over all $(p,q)$ with $p+q=k$ gives the short exact sequence

$$0 \rightarrow (Z(C)\otimes D)_k \rightarrow (C\otimes D)_k \rightarrow (B(C)\otimes D)_{k-1}\rightarrow 0$$

From this short exact sequence, considering the long exact sequence in homology, we obtain

$$\cdots \rightarrow H_{k}(B(C)\otimes D)\overset{\delta_k}{\longrightarrow} H_{k}(Z(C)\otimes D)\rightarrow H_{k}(C\otimes D)\rightarrow H_{k-1}(B(C)\otimes D)\overset{\delta_{k-1}}{\longrightarrow} H_{k-1}(Z(C)\otimes D)\rightarrow \cdots$$

In particular, relative to $H_k(C\otimes D)$, we obtain the short exact sequence

$$0 \rightarrow \coker\delta_k\rightarrow H_k(C\otimes D)\rightarrow \ker\delta_{k-1}\rightarrow 0 \tag{$\ast$}$$

To examine $\coker\delta_k$ and $\ker\delta_{k-1}$, consider the short exact sequence

$$0 \rightarrow B_\bullet(C)\rightarrow Z_\bullet(C)\rightarrow H_\bullet(C)\rightarrow 0$$

and the exact sequence obtained by taking the tensor product with $H_\bullet(D)$:

$$0 \rightarrow \Tor_1^A(H(C), H(D))_\bullet\rightarrow (B(C)\otimes H(D))_\bullet\rightarrow (Z(C) \otimes H(D))_\bullet \rightarrow (H(C)\otimes H(D))_\bullet \rightarrow 0$$

Here the leading $0$ comes from the fact that $Z_\bullet(C)$ consists of free modules. On the other hand, since free modules are flat, taking the tensor product with a free module commutes with taking homology, and hence in the above sequence we have

$$(B(C)\otimes H(D))_\bullet\cong H_\bullet(B(C)\otimes D)\qquad (Z(C)\otimes H(D))_\bullet \cong H_\bullet(Z(C)\otimes D)$$

The map $(B(C)\otimes H(D))_\bullet\rightarrow(Z(C)\otimes H(D))_\bullet$ is induced by the inclusion $B_\bullet(C)\rightarrow Z_\bullet(C)$, and under the above identifications it corresponds to $\delta_\bullet$. Therefore

$$\coker \delta_k\cong (H(C)\otimes H(D))_k,\qquad \ker \delta_{k-1}\cong \Tor_1^A(H(C),H(D))_{k-1}$$

As for the splitting claim, since

$$0 \rightarrow Z_\bullet(C)\rightarrow C_\bullet \rightarrow B_{\bullet-1}(C) \rightarrow 0$$

is a split exact sequence, a section $B_{\bullet-1}(C)\rightarrow C_\bullet$ induces a splitting of ($\ast$).
:::

## The Eilenberg-Zilber Theorem and the Künneth Formula

Bearing in mind the result of [Lemma 8](#lem8), our task is clear. Given two topological spaces $X,Y$ and their corresponding chain complexes $C_\bullet(X),C_\bullet(Y)$, we examine the relationship between the homology $H_\bullet(X\times Y)$ of the product space $X\times Y$ and the tensor product $(H(X)\otimes H(Y))_\bullet$ of the two chain complexes. The following theorem shows that these two algebraic objects are the same.

::: Theorem 9 (Eilenberg-Zilber)
For two topological spaces $X,Y$ and the chain complexes $C_\bullet(X),C_\bullet(Y)$ and $C_\bullet(X\times Y)$ obtained from them, there exists a chain homotopy equivalence between the two chain complexes $(C(X)\otimes C(Y))_\bullet$ and $C_\bullet(X\times Y)$, and therefore

$$H_\bullet(C(X\times Y))\cong H_\bullet(C(X)\otimes C(Y))$$
:::

This is usually proved using the [acyclic models theorem](https://en.wikipedia.org/wiki/Acyclic_model), but in fact the acyclic models theorem is closer to a generalization of the Eilenberg-Zilber theorem, so proving it via the acyclic models theorem feels somewhat excessive. However, a direct proof of the Eilenberg-Zilber theorem is rather tedious, so we shall only examine the two maps that appear in its proof:

$$\AW:C_\bullet(X\times Y) \rightarrow (C(X)\otimes C(Y))_\bullet,\qquad \EZ:(C(X)\otimes C(Y))_\bullet \rightarrow C_\bullet(X\times Y)$$

We have recorded the proof of the acyclic models theorem in a separate post so as not to break the flow.

First, the Alexander-Whitney map $\AW:C_\bullet(X\times Y)\rightarrow(C(X)\otimes C(Y))_\bullet$ sends an arbitrary $k$-simplex $\sigma:\Delta^k\rightarrow X\times Y$ to

$$\sum_p (\pi_X\circ \sigma\vert_{[v_0,\ldots,v_p]})\otimes (\pi_Y\circ \sigma\vert_{[v_p,\ldots v_k]})\in \bigoplus_{p+q=k}C_p(X)\otimes C_q(Y)$$

If $X=Y$, this becomes a map $C(X)\rightarrow C(X)\otimes C(X)$ making $C(X)$ into a (differential graded counital coassociative) coalgebra, and for this reason it will reappear in the next post.

The Eilenberg-Zilber map $\EZ:(C(X)\otimes C(Y))_\bullet\rightarrow C_\bullet(X\times Y)$ is defined on simple tensors by the formula

$$\EZ(\sigma\otimes\tau)=\sum_{\substack{\alpha_1<\cdots <\alpha_p,\quad \beta_1<\cdots <\beta_q\\ \{\alpha_1,\ldots,\alpha_p\}\sqcup\{\beta_1,\ldots,\beta_q\}=\{0,1,\ldots,p+q-1\}}}\sgn(\alpha_1,\ldots,\alpha_p,\beta_1,\ldots,\beta_q)(\sigma\circ s_{\beta_q}\cdots s_{\beta_1})\times(\tau\circ s_{\alpha_p}\cdots s_{\alpha_1})$$

Although this looks complicated, it is merely the formula describing the decomposition of the prism $\Delta^p\times\Delta^q$ into simplices, i.e., the functions $h_n$ appearing in the proof of [§Homotopy, ⁋Proposition 6](/en/math/algebraic_topology/homotopy#prop6). The conclusion of [Theorem 9](#thm9) then follows from the two identities

$$\AW\circ\EZ=\id_{(C(X)\otimes C(Y))_\bullet},\qquad \EZ\circ \AW\simeq \id_{C_\bullet(X\times Y)}$$

Since the chain homotopy equivalence of [Theorem 9](#thm9) is between free complexes, it persists after applying $\otimes_\mathbb{Z}A$, and from this we obtain $C_\bullet(X\times Y)\otimes_\mathbb{Z}A\simeq (C(X)\otimes C(Y))_\bullet\otimes_\mathbb{Z}A\cong C_\bullet(X;A)\otimes_AC_\bullet(Y;A)$. Therefore, combining [Lemma 8](#lem8) with [Theorem 9](#thm9), we obtain the following result.

::: Corollary 10 (Künneth)
Fix topological spaces $X,Y$. Then for their product space $X\times Y$ and a principal ideal domain $A$, there exists a short exact sequence

$$0 \rightarrow \bigoplus_{p+q=k}H_p(X;A)\otimes_AH_q(Y;A)\rightarrow H_k(X\times Y;A)\rightarrow \bigoplus_{p+q=k-1}\Tor_1^A(H_p(X;A),H_q(Y;A))\rightarrow 0$$

Moreover, this short exact sequence splits (non-canonically), and therefore there exists an isomorphism

$$H_k(X\times Y;A)\cong \left( \bigoplus_{p+q=k}H_p(X;A)\otimes_AH_q(Y;A)\right)\oplus \left(\bigoplus_{p+q=k-1}\Tor_1^A(H_p(X;A),H_q(Y;A)) \right)$$
:::

Of course, using this result together with [Theorem 5](#thm5), one may obtain the cohomology version of the Künneth formula.

--- 

**References**

**[Hat]** A. Hatcher, *Algebraic Topology*. Cambridge University Press, 2022.  
**[May]** J. P. May, *A concise course in algebraic topology*.

---

[^1]: Of course, one would hope that this pairing gives a homomorphism from $H^k(X;A)$ to $\Hom(H_k(X),A)$, but as we know from [Proposition 3](#prop3), the situation is not so simple and an $\Ext$ term containing hidden torsion must appear.
