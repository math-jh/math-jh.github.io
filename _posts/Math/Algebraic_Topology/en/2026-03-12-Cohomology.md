---
title: "Cohomology"
description: "We define cohomology, the dual concept of homology, and show through the cohomology ring with a natural multiplicative structure that spaces with the same homology can be topologically distinct."
excerpt: "Definition of cohomology and the universal coefficient theorem"

categories: [Math / Algebraic Topology]
permalink: /en/math/algebraic_topology/cohomology
sidebar: 
    nav: "algebraic_topology-en"

date: 2025-09-07
weight: 9
translated_at: 2026-08-18T14:45:05+00:00
translation_source: kimi-cli
last_polished_at: 2026-09-20T15:15:04+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
As its name suggests, cohomology can be said to be a concept corresponding to the dual of homology. However, if for a space $X$, the $k$th cohomology $H^k(X)$ were simply the dual of the $k$th homology $H_k(X)$, there would be no need to consider it separately.

In fact, cohomology provides a more refined invariant than homology: for instance, a natural product structure is defined on cohomology, and even if spaces have the same homology, they are not homotopic if this product structure differs. In this post, we examine the definition and basic properties of cohomology. 

## The Universal Coefficient Theorem for Homology

Before beginning the discussion in earnest, we first look at homology with coefficients, which was treated after [§Computation of Homology, ⁋Definition 6](/en/math/algebraic_topology/computation_of_homology#def6){: data-lid="071az" data-relation="weak" reviewed="" }. We have seen that when defining simplicial homology or singular homology, instead of the chain groups $C_\bullet(X)$ or $C_\bullet^\Delta(X)$, by taking the tensor product with an abelian group $A$ we obtain the chain complexes

$$C_\bullet(X;A):=C_\bullet(X)\otimes_\mathbb{Z}A,\qquad C_\bullet^\Delta(X;A):=C_\bullet^\Delta(X)\otimes_\mathbb{Z}A$$

and can then define the homologies 

$$H_k(X;A),\qquad H_k^\Delta(X;A)$$

as their homology groups. To compute these in practice, we would additionally need to examine whether $H_k(X;A)$ or $H_k^\Delta(X;A)$ comes out in a form such as $H_k(X)\otimes_\mathbb{Z}A$ or $H_k^\Delta(X)\otimes_\mathbb{Z}A$; however, since the tensor product is in general right-exact but not left-exact, this would be an excessive expectation, and we will need to additionally measure the information lost by taking the tensor. 

To this end, consider a chain complex $C_\bullet$ consisting of free abelian groups, and consider the short exact sequence in $\Ch_{\geq 0}(\Ab)$

$$0 \rightarrow Z_\bullet \rightarrow C_\bullet \rightarrow B_{\bullet-1}\rightarrow 0\tag{1}$$

Here, $Z_k=\ker(\partial:C_k \rightarrow C_{k-1})$ and $B_{k-1}=\im(\partial:C_k \rightarrow C_{k-1})$, and the first map in the sequence above is the inclusion, and the second map is the boundary map $\partial$. 

Here, $Z_{k}$ and $B_{k-1}$ are subgroups of the free abelian groups $C_k,C_{k-1}$, respectively, and are thus free; in particular, since the third term $B_{k-1}$ is free, specifying a preimage for each element of its basis gives a section $B_{k-1}\rightarrow C_k$. That is, this short exact sequence is a split exact sequence, and thus for any abelian group $A$, the following sequence

$$0 \rightarrow Z_\bullet\otimes_\mathbb{Z}A \rightarrow C_\bullet\otimes_\mathbb{Z}A \rightarrow B_{\bullet-1}\otimes_\mathbb{Z}A\rightarrow 0$$

is also a split short exact sequence. This is because the splitting gives a direct sum decomposition $C_\bullet\cong Z_\bullet\oplus B_{\bullet-1}$, and since the tensor product commutes with direct sums, this decomposition is preserved as is even after $\otimes_\mathbb{Z}A$. At this point, writing these out, it is of the form of the following commutative diagram 

{% diagram Math/Algebraic_Topology/Cohomology-1.svg width="31.09em" alt="snake_lemma" %}

and therefore, by [\[Homological Algebra\] §Long Exact Sequences, ⁋Theorem 1](/en/math/homological_algebra/long_exact_sequence#thm1){: data-lid="8v7n3" data-relation="required" reviewed="" }, we obtain the following long exact sequence

$$\cdots \rightarrow B_k\otimes_\mathbb{Z}A\overset{\delta_k}{\longrightarrow}Z_k\otimes_\mathbb{Z}A\rightarrow H_k(C\otimes A)\rightarrow B_{k-1}\otimes_\mathbb{Z}A\overset{\delta_{k-1}}{\longrightarrow} Z_{k-1}\otimes_\mathbb{Z}A\rightarrow\cdots\tag{2}$$

Now, in order to extract information from this exact sequence, we need to examine the connecting maps $\delta$. Following the definition, $\delta_k:B_k\otimes_\mathbb{Z}A\rightarrow Z_k\otimes_\mathbb{Z}A$ is precisely the inclusion homomorphism $i_k:B_k \rightarrow Z_k$ with $-\otimes \id_A$ applied, so let us consider the following short exact sequence

$$0 \rightarrow B_k\overset{i_k}{\longrightarrow} Z_k \overset{p_k}{\longrightarrow}H_k(C)\rightarrow 0$$

Then, since $B_k$, $Z_k$, and $0$ are all free abelian groups, this can be seen as a free resolution of $H_k(C_\bullet)$, and therefore by definition we can place $\delta_k$ into the following exact sequence

$$0 \rightarrow \Tor_1^\mathbb{Z}(H_k(C), A)\rightarrow B_k\otimes_\mathbb{Z}A\overset{\delta_k}{\longrightarrow} Z_k\otimes_\mathbb{Z}A\rightarrow H_k(C)\otimes_\mathbb{Z}A\rightarrow 0$$

That is, the isomorphisms

$$\ker\delta_{k-1}\cong \Tor_1^\mathbb{Z}(H_{k-1}(C), A),\qquad \coker\delta_k\cong H_k(C)\otimes_\mathbb{Z} A$$

exist, and substituting these into (2) yields the short exact sequence

$$0 \rightarrow H_k(C)\otimes_\mathbb{Z}A\rightarrow H_k(C;A)\rightarrow \Tor_1^\mathbb{Z}(H_{k-1}(C), A)\rightarrow 0$$

Meanwhile, since (1) is a split short exact sequence, we can choose a retraction $r_k:C_k \rightarrow Z_k$. ([\[Multilinear Algebra\] §Exact Sequences, ⁋Proposition 10](/en/math/multilinear_algebra/exact_sequences#prop10){: data-lid="p6arh" data-relation="required" reviewed="" }) Then under this choice, $(p_k\circ r_k)\otimes \id_A$ induces a map $H_k(C;A)\rightarrow H_k(C)\otimes_\mathbb{Z} A$ on homology, and we see that this is a retraction of $H_k(C)\otimes_\mathbb{Z}A\rightarrow H_k(C;A)$ above. That is, we obtain the following.

::: Proposition 1 (Universal coefficient theorem for homology)
For any topological space $X$ and abelian group $A$, there exists the following short exact sequence:

$$0 \rightarrow H_k(X)\otimes_\mathbb{Z}A\rightarrow H_k(X;A)\rightarrow \Tor_1^\mathbb{Z}(H_{k-1}(X), A)\rightarrow 0$$

Moreover, this sequence splits (non-canonically), and therefore gives the following (non-canonical) isomorphism:

$$H_k(X;A)\cong \left(H_k(X)\otimes_\mathbb{Z}A\right)\oplus \Tor_1^\mathbb{Z}(H_{k-1}(X), A)$$
:::


## Definition of Cohomology and the Universal Coefficient Theorem

Just as in [§Computation of Homology, ⁋Definition 6](/en/math/algebraic_topology/computation_of_homology#def6){: data-lid="5a8ej" data-relation="weak" reviewed="" }, we can define the Eilenberg-Steenrod axioms for cohomology, and call a contravariant functor and connecting morphisms satisfying them cohomology. Written explicitly, this is as follows.

::: Definition 2 (Eilenberg-Steenrod axioms)
For contravariant functors $H^k$ from the category of pairs of topological spaces to the category of abelian groups, and natural transformations between them

$$\delta: H^k(A) \rightarrow H^{k+1}(X,A)$$

the *Eilenberg-Steenrod axioms* refer to the following axioms:

- (Homotopy) If two homotopic maps $(X,A) \rightarrow (Y,B)$ are given, the two homomorphisms $H^k(Y,B) \rightarrow H^k(X,A)$ they induce are also identical.
- (Excision) For $(X,A,Z)$ satisfying the conditions of [§Computation of Homology, ⁋Theorem 2](/en/math/algebraic_topology/computation_of_homology#thm2){: data-lid="opm3m" data-relation="required" reviewed="" }, $(X\setminus Z, A\setminus Z)\hookrightarrow (X,A)$ induces an isomorphism.
- (Dimension) For a one-point space $\ast$, $H^k(\ast)=0$ holds for all $k>0$.
- (Additivity) If $X=\coprod X_\alpha$, then $H^k(X)\cong\prod H^k(X_\alpha)$.
- (Exactness) Each pair $(X,A)$ and the two inclusions $(A,\emptyset) \hookrightarrow (X,\emptyset)$ and $(X,\emptyset)\hookrightarrow (X,A)$ fit into the following long exact sequence:
    
    $$\cdots \rightarrow H^k(X,A)\rightarrow H^k(X) \rightarrow H^k(A) \rightarrow H^{k+1}(X,A)\rightarrow \cdots$$
:::

To show the existence of a cohomology theory satisfying these conditions, just as in [§Homology](/en/math/algebraic_topology/homology){: data-lid="zp566" data-relation="required" reviewed="" }, let us consider the chain complex of singular simplices of a topological space $X$,

$$C_\bullet(X):\qquad\cdots \rightarrow C_{k+1}(X)\rightarrow C_k(X) \rightarrow C_{k-1}(X)\rightarrow \cdots$$

Fixing an abelian group $A$ to be used as the coefficient group, we can consider the following chain complex corresponding to the dual of this chain complex:

$$(C^\vee)^\bullet(X;A):\qquad\cdots \leftarrow \Hom_\mathbb{Z}(C_{k+1}(X), A)\leftarrow\Hom_\mathbb{Z}(C_k(X),A)\leftarrow\Hom_\mathbb{Z}(C_{k-1}(X),A)\leftarrow\cdots$$

If $A$ is a commutative ring, ([\[Algebraic Structures\] §Definition of a Ring, ⁋Definition 1](/en/math/algebraic_structures/rings#def1){: data-lid="8ua52" data-relation="weak" reviewed="" }) the adjunction of [\[Algebraic Structures\] §Change of Scalars, ⁋Proposition 6](/en/math/algebraic_structures/change_of_base_ring#prop6){: data-lid="w1xzz" data-relation="required" reviewed="" } for the ring homomorphism $\mathbb{Z}\rightarrow A$ gives an isomorphism $\Hom_A(M\otimes_\mathbb{Z}A,N)\cong\Hom_\mathbb{Z}(M,N)$ for any abelian group $M$ and $A$-module $N$. Therefore, in this case, the above chain complex can be regarded as

$$\qquad \cdots\leftarrow\Hom_A(C_{k+1}(X;A),A)\leftarrow \ Hom_A(C_k(X;A),A)\leftarrow \Hom_A(C_{k-1}(X;A),A)\leftarrow\cdots$$

and hence can be considered as corresponding to the dual of the chain complex $C_\bullet(X;A)$. We then write the $k$th homology of this chain complex $(C^\vee)^\bullet(X;A)$ as

$$H^k(X;A):=H_k(C^\vee)$$

and call it the *$k$th cohomology* of $X$. The reason for denoting the index using superscripts on $H$ and $C^\vee$ is that, contrary to homology, the long exact sequence is formed in the direction of increasing index; hereafter, when there is no danger of confusion, let us write $C^\bullet(X;A)$ for $(C^\vee)^\bullet(X)$.

We must now examine what relationship exists between $H^k(X;A)$ thus defined and $H_k(X)$. As stated at the beginning of this post, it is not simply the case that $H^k(X;A)\cong H_k(X)^\ast$ holds. However, in a manner similar to the proof of [Proposition 1](#prop1){: data-relation="required" reviewed="" } above, we can obtain the following proposition.

::: Proposition 3 (Universal coefficient theorem for cohomology)
For any topological space $X$ and abelian group $A$, there exists the following short exact sequence:

$$0\rightarrow\Ext_\mathbb{Z}^1(H_{k-1}(X), A)\rightarrow H^k(X;A)\rightarrow \Hom_\mathbb{Z}(H_k(X),A)\rightarrow 0$$

Moreover, this sequence splits (non-canonically), and therefore gives the following (non-canonical) isomorphism:

$$H^k(X;A)\cong \Hom_\mathbb{Z}(H_k(X),A)\oplus \Ext^1_\mathbb{Z}(H_{k-1}(X),A)$$
:::

Roughly speaking, this may be thought of as translating [Proposition 1](#prop1){: data-relation="weak" reviewed="" } via [\[Algebraic Structures\] §Abelian Groups, ⁋Theorem 15](/en/math/algebraic_structures/abelian_groups#thm15){: data-lid="qfrxz" data-relation="weak" reviewed="" }.

## de Rham Cohomology

Associating to a topological space $X$ a chain complex $C_\bullet(X)$ can be viewed as algebraically transferring information about the subspaces of $X$. In defining cohomology, to $C_\bullet(X)$ we apply $\Hom_\mathbb{Z}(-,A)$ and then define the homology of this cochain complex; here, any element of

$$C^k(X;A)=\Hom_\mathbb{Z}(C_k(X), A)$$

can be thought of as a function that assigns to each element of $C_k(X)$ (that is, each $k$-chain) an element of $A$. That is, cohomology can essentially be said to be looking at functions defined on the space.

More concretely, for any $c\in C_k(X)$ and $\varphi\in C^k(X;A)$, we know that the canonical pairing

$$C_k(X)\times C^k(X;A)\rightarrow A;\qquad (c,\varphi)\mapsto \varphi(c)\in A$$

exists; and if we denote the boundary map of $C_\bullet(X)$ by $\partial$ and the resulting coboundary map of $C^\bullet(X;A)$ by $\delta$, we know that for any $c\in C_{k+1}(X)$ and $\varphi\in C^k(X;A)$, the equation

$$\langle \partial c, \varphi\rangle=\langle c, \delta\varphi\rangle$$

holds, from which we know that these give a pairing

$$H_k(X)\times H^k(X;A)\rightarrow A$$

at the level of homology and cohomology.[^1]

For example, to see de Rham cohomology, consider the spaces of differential $k$-forms, which are $\mathbb{R}$-vector spaces

$$\Omega^k(\mathbb{R}^n)=\{\text{$k$-forms on $\mathbb{R}^n$}\}$$

Here the coboundary map $\Omega^k(\mathbb{R}^n)\rightarrow \Omega^{k+1}(\mathbb{R}^n)$ is given by the exterior derivative, and a differential $k$-form, when given a $k$-dimensional subset, produces a corresponding number via integration. Also, closed $k$-forms are given by the kernel of this coboundary, and exact $k$-forms are given by the image of this coboundary.

For instance, on $\mathbb{R}^3$, consider the differential $2$-form

$$\omega=\dd{x}\wedge \dd{y}$$

In $\mathbb{R}^3$, a $2$-dimensional subset is given by a function from a (unit) rectangle in $\mathbb{R}^2$ to $\mathbb{R}^3$, and through this we know what it means to apply to a $2$-dimensional subset $\omega$.

For example, suppose the following set

$$S = \{ (x, y, 0) \mid 0 \leq x \leq 1, 0 \leq y \leq 1 \}$$

is given. Then the value of $\omega$ on this set is simply computed as

$$\int_S \omega = \int_{x=0}^{1} \int_{y=0}^{1} 1\dd{y}\dd{x} = 1$$

As another example, if the surface

$$\Sigma = \{ (x, y, z) \mid x^2 + y^2 + z^2 = 1,\ z \geq 0 \}$$

is given, we first use spherical coordinates

$$x = \sin \phi \cos \theta,\qquad y = \sin \phi \sin \theta,\qquad z = \cos \phi$$

to parametrize this as a function from $[0,\pi/2]\times[0,2\pi]$ to $\Sigma$, and then, using $\dd{x} \wedge \dd{y} = \sin \phi \cos \phi\dd{\phi} \wedge \dd{\theta}$, we can compute the integral in the following manner:

$$\begin{align*}
\int_{\Sigma} \omega
&= \int_{0}^{2\pi} \int_{0}^{\pi/2} \sin \phi \cos \phi\dd{\phi} \dd{\theta} = \int_{0}^{2\pi} \dd{\theta} \int_{0}^{\pi/2} \sin \phi \cos \phi\dd{\phi} \\
&= 2\pi \times \frac{1}{2} \int_{0}^{\pi/2} \sin(2\phi) \dd{\phi} = 2\pi \times \frac{1}{2} \left[ -\frac{1}{2} \cos(2\phi) \right]_{0}^{\pi/2} \\
&= 2\pi \times \frac{1}{2} \left( -\frac{1}{2} [\cos(\pi) - \cos(0)] \right) = 2\pi \times \frac{1}{2} \left( -\frac{1}{2}(-1 - 1) \right) = 2\pi \times \frac{1}{2} \times 1 \\
&= \pi
\end{align*}$$

Then the differential $2$-form $\omega$ can be thought of as a function that, in this manner, takes a 2-dimensional subset such as $S$ or $\Sigma$ and outputs a number.

Now, by the Poincaré lemma, we know that for any $k>0$, on $\mathbb{R}^n$ closed $k$-forms always arise as the exterior derivative of a suitable $k-1$-form. Hence for any $k>0$,

$$H^k_\dR(\mathbb{R}^n)=0$$

and in the case $k=0$, since the functions that become $0$ when differentiated are precisely the constant functions,

$$H^0_\dR(\mathbb{R}^n)=\mathbb{R}$$

The de Rham cohomology defined in this manner also satisfies all the conditions of [Definition 2](#def2){: data-lid="0nylx" data-relation="required" reviewed="" } on the category of pairs of smooth manifolds; therefore, by the uniqueness of cohomology theories and the fact that any singular chain can be approximated by a smooth chain, we can verify that singular cohomology with $\mathbb{R}$ coefficients and de Rham cohomology coincide. The computation above is then nothing more than translating the computation of [§Homology, ⁋Proposition 11](/en/math/algebraic_topology/homology#prop11){: data-lid="3t7fb" data-relation="weak" reviewed="" } via [Proposition 3](#prop3){: data-lid="c7afp" data-relation="weak" reviewed="" } into $\mathbb{R}$-valued cohomology.
 
## Coefficients of (Co)homology

The de Rham cohomology examined above is an example of a cohomology theory whose coefficient group is not $\mathbb{Z}$. Unlike singular cohomology or simplicial cohomology theory, for de Rham cohomology it is natural by definition that the coefficient group is $\mathbb{R}$.
  
Such cohomology theories have good properties: for instance, since $\mathbb{R}$ is a torsion-free abelian group, $\Tor_1^\mathbb{Z}(A,\mathbb{R})=0$ holds for any abelian group $A$, and hence by [Proposition 1](#prop1){: data-relation="required" reviewed="" } we know that the following isomorphism

$$H_k(X;\mathbb{R})\cong H_k(X)\otimes_\mathbb{Z}\mathbb{R}$$

holds. Furthermore, since $\mathbb{R}$ is an injective $\mathbb{Z}$-module, $\Ext_\mathbb{Z}^1(A,\mathbb{R})=0$ holds for any abelian group $A$, and thus this time [Proposition 3](#prop3){: data-lid="iqix3" data-relation="required" reviewed="" } gives the following isomorphism:

$$H^k(X;\mathbb{R})\cong \Hom_\mathbb{Z}(H_k(X),\mathbb{R})$$

Then studying homology and cohomology of this kind will be another point of interest. To this end, recalling the chain complexes used when defining $H_k(X;A)$ and $H^k(X;A)$, we know that the two chain complexes

$$C_\bullet(X;A):=C_\bullet(X)\otimes_\mathbb{Z}A,\qquad C_\bullet^\Delta(X;A):=C_\bullet^\Delta(X)\otimes_\mathbb{Z}A$$

are, if $A$ were a ring, chain complexes of $A$-modules, and the previously defined $C^\bullet(X;A)$ is also such. Therefore, taking homology or cohomology of these, the result will also be an $A$-module.

Meanwhile, we know that if $A$ is a principal ideal domain, any submodule of a free $A$-module is again a free $A$-module. Looking back at the proof of [Proposition 1](#prop1){: data-relation="required" reviewed="" }, it made use of the fact that, since $\mathbb{Z}$ is a principal ideal domain, a submodule of a free $\mathbb{Z}$-module (that is, a free abelian group) is again a free $\mathbb{Z}$-module, and based on this, we can generalize the preceding two propositions as follows.

::: Theorem 4 (Universal coefficient theorem for homology, general version)
For a principal ideal domain $A$, a chain complex of free $A$-modules $C_\bullet$, and an arbitrary $A$-module $M$, there exists the following short exact sequence:

$$0 \rightarrow H_k(C)\otimes_AM\rightarrow H_k(C\otimes_AM)\rightarrow \Tor_1^A(H_{k-1}(C), M)\rightarrow 0$$

Moreover, this sequence splits (non-canonically), and therefore gives the following (non-canonical) isomorphism:

$$H_k(C\otimes_AM)\cong \left(H_k(C)\otimes_AM\right)\oplus \Tor_1^A(H_{k-1}(C), M)$$
:::

::: Theorem 5 (Universal coefficient theorem for cohomology, general version)
For a principal ideal domain $A$, a chain complex of free $A$-modules $C_\bullet$, and an arbitrary $A$-module $M$, there exists the following short exact sequence:

$$0\rightarrow\Ext_A^1(H_{k-1}(C), M)\rightarrow H_k(\Hom_A(C,M))\rightarrow \Hom_A(H_k(C),M)\rightarrow 0$$

Moreover, this sequence splits (non-canonically), and therefore gives the following (non-canonical) isomorphism:

$$H_k(\Hom_A(C,M))\cong \Hom_A(H_k(C),M)\oplus \Ext^1_A(H_{k-1}(C),M)$$
:::

## The Mayer-Vietoris Sequence

Meanwhile, among the axioms of [Definition 2](#def2){: data-relation="required" reviewed="" }, the excision axiom allows us to compute the cohomology of a large space from that of smaller ones. The following proposition is the cohomology version of [\[Algebraic Topology\] §Computation of Homology, ⁋Proposition 7](/en/math/algebraic_topology/computation_of_homology#prop7){: data-relation="required" reviewed="" }, and its proof is obtained by repeating the passage from [\[Algebraic Topology\] §Computation of Homology, ⁋Definition 6](/en/math/algebraic_topology/computation_of_homology#def6){: data-lid="dvoei" data-relation="required" reviewed="" } to [\[Algebraic Topology\] §Computation of Homology, ⁋Proposition 7](/en/math/algebraic_topology/computation_of_homology#prop7){: data-relation="required" reviewed="" }, starting from [Definition 2](#def2){: data-relation="required" reviewed="" }.

::: Proposition 6 (Mayer-Vietoris sequence)
Suppose a topological space $X$ is expressed as the union $X=U\cup V$ of two open sets, and consider a cohomology theory $H$ defined on it. Then there exists a long exact sequence

$$\cdots \rightarrow H^{n}(X) \xrightarrow{(i^\ast, j^\ast)} H^{n}(U) \oplus H^{n}(V) \xrightarrow{k^\ast - l^\ast} H^{n}(U \cap V) \xrightarrow{\delta} H^{n+1}(X) \rightarrow \cdots$$

where $i^\ast, j^\ast, k^\ast, l^\ast$ are the maps induced by the inclusions

$$i:U\rightarrow X,\quad j:V\rightarrow X,\quad k:U\cap V\rightarrow U,\quad l:U\cap V \rightarrow V$$

respectively.
:::

## Tensor Product of Chain Complexes

Using the Mayer-Vietoris sequence, we can compute the homology or cohomology of a large space from the homology or cohomology of its small subspaces. Meanwhile, we can also multiply two spaces $X,Y$ to form a larger space $X\times Y$, and the Künneth formula helps compute the homology and cohomology of such product spaces. To this end, given two chain complexes $C_\bullet$, $D_\bullet$, we must first define their tensor product.

::: Definition 7
Let a ring $A$ and chain complexes of $A$-modules $C_\bullet,D_\bullet$ be given. Then their *tensor product* $(C\otimes D)_\bullet$ is defined for each $k$ by

$$(C\otimes D)_k=\bigoplus_{p+q=k}C_p\otimes_A D_q$$

and the differential is defined on homogeneous elements by

$$\partial(x\otimes y)=\partial^Cx\otimes y+(-1)^{\deg(x)}x\otimes\partial^Dy$$

and then obtained by extending linearly.
:::

That is, $(C\otimes D)_\bullet$ can be regarded as the total complex of the double complex whose $(p,q)$-component is $C_p\otimes D_q$, with horizontal differential $\partial^C\otimes\id_D$ and vertical differential $\id_C\otimes \partial^D$. ([§Homology, ⁋Definition 5](/en/math/homological_algebra/homology#def5){: data-lid="rlunk" data-relation="weak" reviewed="" })

Then the algebraic content of the Künneth formula is contained in the following lemma.

::: Lemma 8
Suppose given a principal ideal domain $A$ and $A$-module chain complexes $C_\bullet$, $D_\bullet$, and let $C_\bullet$ be a chain complex of free $A$-modules. Then for any $k$, there exists a short exact sequence

$$0 \rightarrow \bigoplus_{p+q=k}H_p(C)\otimes_AH_q(D)\rightarrow H_k(C\otimes D)\rightarrow \bigoplus_{p+q=k-1}\Tor_1^A(H_p(C),H_q(D))\rightarrow 0$$

Moreover, this short exact sequence splits (non-canonically), and therefore there exists an isomorphism

$$H_k(C\otimes D)\cong \left( \bigoplus_{p+q=k}H_p(C)\otimes_AH_q(D)\right)\oplus \left(\bigoplus_{p+q=k-1}\Tor_1^A(H_p(C),H_q(D)) \right)$$
:::
::: Proof
First, consider the short exact sequence

$$0 \rightarrow Z_p(C) \rightarrow C_p\rightarrow B_{p-1}(C)\rightarrow 0$$

Since $B_{p-1}(C)$ and $Z_p(C)$ are submodules of the free $A$-modules $C_{p-1},C_p$, and $A$ is a principal ideal domain, they are again free $A$-modules. Therefore, tensoring this short exact sequence with $D_q$ yields the short exact sequence

$$0\rightarrow Z_p(C)\otimes D_q \rightarrow C_p\otimes D_q \rightarrow B_{p-1}(C)\otimes D_q\rightarrow 0$$

From the definition of the chain complex $(C\otimes D)_\bullet$, considering such short exact sequences with $p+q=k$ over all $(p,q)$ and then taking their direct sum, we obtain the short exact sequence

$$0 \rightarrow (Z(C)\otimes D)_k \rightarrow (C\otimes D)_k \rightarrow (B(C)\otimes D)_{k-1}\rightarrow 0$$

Now, considering the long exact sequence in homology from this short exact sequence, we can obtain

$$\cdots \rightarrow H_{k}(B(C)\otimes D)\overset{\delta_k}{\longrightarrow} H_{k}(Z(C)\otimes D)\rightarrow H_{k}(C\otimes D)\rightarrow H_{k-1}(B(C)\otimes D)\overset{\delta_{k-1}}{\longrightarrow} H_{k-1}(Z(C)\otimes D)\rightarrow \cdots$$

In particular, relative to $H_k(C\otimes D)$, we obtain the short exact sequence

$$0 \rightarrow \coker\delta_k\rightarrow H_k(C\otimes D)\rightarrow \ker\delta_{k-1}\rightarrow 0 \tag{$\ast$}$$

Now, to examine $\coker\delta_k$ and $\ker\delta_{k-1}$, consider the short exact sequence

$$0 \rightarrow B_\bullet(C)\rightarrow Z_\bullet(C)\rightarrow H_\bullet(C)\rightarrow 0$$

and consider the following exact sequence obtained by taking the tensor product with $H_\bullet(D)$:

$$0 \rightarrow \Tor_1^A(H(C), H(D))_\bullet\rightarrow (B(C)\otimes H(D))_\bullet\rightarrow (Z(C) \otimes H(D))_\bullet \rightarrow (H(C)\otimes H(D))_\bullet \rightarrow 0$$

Here, the leading $0$ comes from the fact that $Z_\bullet(C)$ consists of free modules. On the other hand, since free modules are flat, taking the tensor product with a free module commutes with taking homology, and hence in the above sequence we have

$$(B(C)\otimes H(D))_\bullet\cong H_\bullet(B(C)\otimes D)\qquad (Z(C)\otimes H(D))_\bullet \cong H_\bullet(Z(C)\otimes D)$$

At this point, $(B(C)\otimes H(D))_\bullet \rightarrow (Z(C)\otimes H(D))_\bullet$ is obtained from the inclusion $B_\bullet(C)\rightarrow Z_\bullet(C)$, and under the above identifications we see that it is the same map as $\delta_\bullet$. Therefore, we obtain

$$\coker \delta_k\cong (H(C)\otimes H(D))_k,\qquad \ker \delta_{k-1}\cong \Tor_1^A(H(C),H(D))_{k-1}$$

As for the claim regarding the splitting, since

$$0 \rightarrow Z_\bullet(C)\rightarrow C_\bullet \rightarrow B_{\bullet-1}(C) \rightarrow 0$$

is a split exact sequence, a section $B_{\bullet-1}(C)\rightarrow C_\bullet$ induces a splitting of ($\ast$).
:::

## The Eilenberg-Zilber Theorem and the Künneth Formula

Bearing in mind the result of [Lemma 8](#lem8){: data-relation="required" reviewed="" }, what we have to do is clear. Given two topological spaces $X,Y$ and their corresponding chain complexes $C_\bullet(X),C_\bullet(Y)$, it is to examine the relationship between the homology $H_\bullet(X\times Y)$ of the product space $X\times Y$ and, for the two chain complexes $H_\bullet(X)$, $H_\bullet(Y)$, their tensor product $(H(X)\otimes H(Y))_\bullet$. The following theorem shows that these two algebraic objects are the same.

::: Theorem 9 (Eilenberg-Zilber)
For two topological spaces $X,Y$ and the chain complexes $C_\bullet(X),C_\bullet(Y)$, and $C_\bullet(X\times Y)$ obtained from them, there exists a chain homotopy equivalence between the two chain complexes $(C(X)\otimes C(Y))_\bullet$ and $C_\bullet(X\times Y)$, and therefore 

$$H_\bullet(C(X\times Y))\cong H_\bullet(C(X)\otimes C(Y))$$

holds.
:::

This is usually proved using the [acyclic models theorem](https://en.wikipedia.org/wiki/Acyclic_model), but in fact the acyclic models theorem is closer to a generalization of the Eilenberg-Zilber theorem, so proving it via the acyclic models theorem feels somewhat excessive. However, directly proving the Eilenberg-Zilber theorem is rather tedious, so we will only examine the two maps

$$\AW:C_\bullet(X\times Y) \rightarrow (C(X)\otimes C(Y))_\bullet,\qquad \EZ:(C(X)\otimes C(Y))_\bullet \rightarrow C_\bullet(X\times Y)$$

appearing in this proof. The proof of the acyclic models theorem is recorded in a separate post so as not to break the flow.

First, the Alexander-Whitney map $\AW:C_\bullet(X\times Y) \rightarrow (C(X)\otimes C(Y))_\bullet$ is obtained by sending an arbitrary $k$-simplex $\sigma:\Delta^k \rightarrow X\times Y$ to 

$$\sum_p (\pi_X\circ \sigma\vert_{[v_0,\ldots,v_p]})\otimes (\pi_Y\circ \sigma\vert_{[v_p,\ldots v_k]})\in \bigoplus_{p+q=k}C_p(X)\otimes C_q(Y)$$

If $X=Y$, this would be a map making $C(X)$ into a (differential graded counital coassociative) coalgebra via $C(X)\rightarrow C(X)\otimes C(X)$, and for this reason it will reappear in the next post.

The Eilenberg-Zilber map $\EZ:(C(X)\otimes C(Y))_\bullet \rightarrow C_\bullet(X\times Y)$ is defined on simple tensors by the formula

$$\EZ(\sigma\otimes\tau)=\sum_{\substack{\alpha_1<\cdots <\alpha_p,\quad \beta_1<\cdots <\beta_q\\ \{\alpha_1,\ldots,\alpha_p\}\sqcup\{\beta_1,\ldots,\beta_q\}=\{0,1,\ldots,p+q-1\}}}\sgn(\alpha_1,\ldots,\alpha_p,\beta_1,\ldots,\beta_q)(\sigma\circ s_{\beta_q}\cdots s_{\beta_1})\times(\tau\circ s_{\alpha_p}\cdots s_{\alpha_1})$$

and although this looks complicated as a formula, it merely represents the function $h_n$ appearing in the proof of [§Homotopy, ⁋Proposition 6](/en/math/algebraic_topology/homotopy#prop6){: data-lid="m90xp" data-relation="weak" reviewed="" }, that is, the method of decomposing the prism $\Delta^p\times \Delta^q$ into simplices. Then the result of [Theorem 9](#thm9){: data-relation="required" reviewed="" } follows from the two identities

$$\AW\circ\EZ=\id_{(C(X)\otimes C(Y))_\bullet},\qquad \EZ\circ \AW\simeq \id_{C_\bullet(X\times Y)}$$

Since the chain homotopy equivalence of [Theorem 9](#thm9){: data-relation="required" reviewed="" } is between free complexes, it persists after applying $\otimes_\mathbb{Z}A$, and from this we obtain $C_\bullet(X\times Y)\otimes_\mathbb{Z}A\simeq (C(X)\otimes C(Y))_\bullet\otimes_\mathbb{Z}A\cong C_\bullet(X;A)\otimes_AC_\bullet(Y;A)$. Therefore, combining [Lemma 8](#lem8){: data-relation="required" reviewed="" } with [Theorem 9](#thm9){: data-relation="required" reviewed="" }, we obtain the following result.

::: Corollary 10 (Künneth)
Fix topological spaces $X,Y$. Then for their product space $X\times Y$ and a principal ideal domain $A$, there exists a short exact sequence

$$0 \rightarrow \bigoplus_{p+q=k}H_p(X;A)\otimes_AH_q(Y;A)\rightarrow H_k(X\times Y;A)\rightarrow \bigoplus_{p+q=k-1}\Tor_1^A(H_p(X;A),H_q(Y;A))\rightarrow 0$$

Moreover, this short exact sequence splits (non-canonically), and therefore there exists an isomorphism

$$H_k(X\times Y;A)\cong \left( \bigoplus_{p+q=k}H_p(X;A)\otimes_AH_q(Y;A)\right)\oplus \left(\bigoplus_{p+q=k-1}\Tor_1^A(H_p(X;A),H_q(Y;A)) \right)$$
:::

Of course, using this result together with [Theorem 5](#thm5){: data-lid="w18l1" data-relation="weak" reviewed="" }, one can obtain the cohomology version of the Künneth formula.

--- 

**References**

**[Hat]** A. Hatcher, *Algebraic Topology*. Cambridge University Press, 2022.  
**[May]** J. P. May, *A concise course in algebraic topology*.

---

[^1]: Of course, we would hope that this pairing gives a homomorphism from $H^k(X;A)$ to $\Hom(H_k(X),A)$, but the situation is not so simple, and we know from [Proposition 3](#prop3){: data-lid="7yee4" data-relation="weak" reviewed="" } that an $\Ext$ term containing hidden torsion must appear.
