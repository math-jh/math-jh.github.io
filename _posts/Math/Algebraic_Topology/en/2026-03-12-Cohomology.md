---
title: "Cohomology"
excerpt: "The definition of cohomology and the universal coefficient theorem"

categories: [Math / Algebraic Topology]
permalink: /en/math/algebraic_topology/cohomology
header:
    overlay_image: /assets/images/Math/Algebraic_Topology/Cohomology.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_topology-en"

date: 2025-09-07
last_modified_at: 2025-09-07
weight: 6
translated_at: 2026-05-27T08:30:02+00:00
translation_source: kimi-cli
---
Cohomology, as its name suggests, can be regarded as the dual concept to homology. However, if the $k$th cohomology $H^k(X)$ of a space $X$ were simply the dual of the $k$th homology $H_k(X)$, there would be no need to consider it separately.

In fact, cohomology provides a more refined invariant than homology: for instance, a natural product structure is defined on cohomology, and even if two spaces have the same homology, they are not homotopic if this product structure differs. In this post we define cohomology and examine its basic properties.

## Universal Coefficient Theorem for Homology

Before beginning our discussion in earnest, we first review homology with coefficients, which we treated after [§Computation of Homology, ⁋Definition 6 (Eilenberg–Steenrod axioms)](/en/math/algebraic_topology/computation_of_homology#def6). We saw that when defining simplicial homology or singular homology, by taking the tensor product with an abelian group $A$ instead of the chain groups $C_\bullet(X)$ or $C_\bullet^\Delta(X)$, we obtain chain complexes

$$C_\bullet(X;A):=C_\bullet(X)\otimes_\mathbb{Z}A,\qquad C_\bullet^\Delta(X;A):=C_\bullet^\Delta(X)\otimes_\mathbb{Z}A$$

and that their homology groups define the homologies

$$H_k(X;A),\qquad H_k^\Delta(X;A)$$

To compute these in practice, one might ask whether $H_k(X;A)$ or $H_k^\Delta(X;A)$ can be expressed in terms of $H_k(X)\otimes_\mathbb{Z}A$ or $H_k^\Delta(X)\otimes_\mathbb{Z}A$; however, since the tensor product is right-exact but not left-exact in general, this would be too much to hope for, and we need an additional measurement of the information lost by tensoring.

To this end, consider a chain complex $C_\bullet$ of free abelian groups and the short exact sequence in $\Ch_{\geq 0}(\Ab)$

$$0 \rightarrow Z_\bullet \rightarrow C_\bullet \rightarrow B_{\bullet-1}\rightarrow 0\tag{1}$$

Here $Z_k=\ker(\partial:C_k \rightarrow C_{k-1})$ and $B_{k-1}=\im(\partial:C_k \rightarrow C_{k-1})$, the first map is the inclusion, and the second is the boundary map $\partial$.

Since $Z_{k}$ and $B_{k-1}$ are subgroups of the free abelian groups $C_k,C_{k-1}$, they are free, and therefore by [##ref##](third_term_projective_splits) this short exact sequence is a split exact sequence; hence for any abelian group $A$, the sequence

$$0 \rightarrow Z_\bullet\otimes_\mathbb{Z}A \rightarrow C_\bullet\otimes_\mathbb{Z}A \rightarrow B_{\bullet-1}\otimes_\mathbb{Z}A\rightarrow 0$$

is also a splitting short exact sequence. ([##ref](splitting_tensor_splits)) Writing these out gives a commutative diagram of the form

![snake_lemma](/assets/images/Math/Algebraic_Topology/Cohomology-1.png){:style="width:32em" class="invert" .align-center}

and thus by [\[Homological Algebra\] §The Long Exact Sequence, ⁋Theorem 1 (The long exact sequence)](/en/math/homological_algebra/long_exact_sequence#thm1) we obtain the long exact sequence

$$\cdots B_k\otimes_\mathbb{Z}A\overset{\delta_k}{\longrightarrow}Z_k\otimes_\mathbb{Z}A\rightarrow H_k(C\otimes A)\rightarrow B_{k-1}\otimes_\mathbb{Z}A\overset{\delta_{k-1}}{\longrightarrow} Z_{k-1}\otimes_\mathbb{Z}A\rightarrow\cdots\tag{2}$$

To extract information from this exact sequence, we must examine the connecting maps $\delta$. Tracing through the definition, $\delta_k:B_k\otimes_\mathbb{Z}A\rightarrow Z_k\otimes_\mathbb{Z}A$ is exactly $-\otimes \id_A$ applied to the inclusion homomorphism $i_k:B_k \rightarrow Z_k$, so consider the short exact sequence

$$0 \rightarrow B_k\overset{i_k}{\longrightarrow} Z_k \overset{p_k}{\longrightarrow}H_k(C)\rightarrow 0$$

Since $B_k$, $Z_k$, and $0$ are all free abelian groups, this can be viewed as a free resolution of $H_k(C_\bullet)$, and therefore by definition we can fit $\delta_k$ into the exact sequence

$$0 \rightarrow \Tor_1^\mathbb{Z}(H_k(C))\rightarrow B_k\otimes_\mathbb{Z}A\overset{\delta_k}{\longrightarrow} Z_k\otimes_\mathbb{Z}A\rightarrow H_k\otimes_\mathbb{Z}A\rightarrow 0$$

That is, we have the isomorphisms

$$\ker\delta_{k-1}\cong \Tor_1^\mathbb{Z}(H_{k-1}(C), A),\qquad \coker\delta_k\cong H_k(C)\otimes_\mathbb{Z} A$$

and substituting these into (2) yields the short exact sequence

$$0 \rightarrow H_k(C)\otimes_\mathbb{Z}A\rightarrow H_k(C;A)\rightarrow \Tor_1^\mathbb{Z}(H_{k-1}(C), A)\rightarrow 0$$

On the other hand, since (1) is a splitting short exact sequence, we can choose a retraction $r_k:C_k \rightarrow Z_k$. ([\[Multilinear Algebra\] §Exact Sequences, ⁋Proposition 10](/en/math/multilinear_algebra/exact_sequences#prop10)) Then, with this choice, $(p_k\circ r_k)\otimes \id_A$ induces the map $H_k(C;A)\rightarrow H_k(C)\otimes_\mathbb{Z} A$ in homology, and this is a retraction of the map $H_k(C)\otimes_\mathbb{Z}A\rightarrow H_k(C;A)$ above. Thus we obtain the following.

<div class="proposition" markdown="1">

<ins id="prop1">**Proposition 1 (Universal coefficient theorem for homology)**</ins> For any topological space $X$ and abelian group $A$, there exists a short exact sequence

$$0 \rightarrow H_k(X)\otimes_\mathbb{Z}A\rightarrow H_k(X;A)\rightarrow \Tor_1^\mathbb{Z}(H_{k-1}(X), A)\rightarrow 0$$

Moreover, this sequence splits (non-canonically), and therefore yields the (non-canonical) isomorphism

$$H_k(X;A)\cong \left(H_k(X)\otimes_\mathbb{Z}A\right)\oplus \Tor_1^\mathbb{Z}(H_{k-1}(X), A)$$

</div>


## Definition of Cohomology and Universal Coefficient Theorem

Just as in [§Computation of Homology, ⁋Definition 6 (Eilenberg–Steenrod axioms)](/en/math/algebraic_topology/computation_of_homology#def6), we define the Eilenberg-Steenrod axioms for cohomology, and a contravariant functor with connecting morphisms satisfying them can be called a cohomology theory. Writing this out explicitly gives the following.

<div class="definition" markdown="1">

<ins id="def2">**Definition 2 (Eilenberg-Steenrod axioms)**</ins> For contravariant functors $H^k$ from the category of pairs of topological spaces to the category of abelian groups, together with natural transformations

$$\delta: H^k(X) \rightarrow H^{k+1}(X,A)$$

the *Eilenberg-Steenrod axioms* are the following conditions.

- (Homotopy) If two maps $(X,A) \rightarrow (Y,B)$ are homotopic, then the two induced homomorphisms $H^k(Y,B) \rightarrow H^k(X,A)$ are equal.
- (Excision) For $(X,A,Z)$ satisfying the conditions of [§Computation of Homology, ⁋Theorem 2 (Excision theorem)](/en/math/algebraic_topology/computation_of_homology#thm2), the inclusion $(X\setminus Z, A\setminus Z)\hookrightarrow (X,A)$ induces an isomorphism.
- (Dimension) For the one-point space $\ast$, $H^k(\ast)=0$ for all $k>0$.
- (Additivity) If $X=\coprod X_\alpha$, then $H^k(X)\cong\bigoplus H^k(X_\alpha)$.
- (Exactness) For each pair $(X,A)$, the two inclusions $(A,\emptyset) \hookrightarrow (X,\emptyset)$ and $(X,\emptyset)\hookrightarrow (X,A)$ fit into the long exact sequence

    $$\cdots \rightarrow H^k(X,A)\rightarrow H^k(X) \rightarrow H^k(A) \rightarrow H^{k+1}(X,A)\rightarrow \cdots$$

</div>

To show the existence of a cohomology theory satisfying these conditions, just as in [§Homology](/en/math/algebraic_topology/homology), we consider the chain complex of singular simplices of a topological space $X$

$$C_\bullet(X):\qquad\cdots \rightarrow C_{k+1}(X)\rightarrow C_k(X) \rightarrow C_{k-1}(X)\rightarrow \cdots$$

Fixing an abelian group $A$ as the coefficient group, we can consider the dual chain complex

$$(C^\vee)^\bullet(X;A):\qquad\cdots \leftarrow \Hom_\mathbb{Z}(C_{k+1}(X), A)\leftarrow\Hom_\mathbb{Z}(C_k(X),A)\leftarrow\Hom_\mathbb{Z}(C_{k-1}(X),A)\leftarrow\cdots$$

By [\[Algebraic Structures\] §Direct Products, Direct Sums, and Tensor Products of Modules, ⁋Theorem 6](/en/math/algebraic_structures/operations_of_modules#thm6), this can be written as

$$\qquad \cdots\leftarrow\Hom_A(C_{k+1}(X;A),A)\leftarrow \Hom_A(C_k(X;A),A)\leftarrow \Hom_A(C_{k-1}(X;A),A)\leftarrow\cdots$$

so it can be thought of as the dual of the chain complex $C_\bullet(X;A)$. We then define the $k$th homology of this chain complex $(C^\vee)^\bullet(X;A)$ as

$$H^k(X;A):=H_k(C^\vee)$$

and call this the *$k$th cohomology* of $X$. The reason for using superscripts on $H$ and $C^\vee$ to denote the index is that, in contrast to homology, the long exact sequence is formed in the direction of increasing indices; henceforth, when there is no risk of confusion, we will write $(C^\vee)^\bullet(X;A)$ as $C^\bullet(X;A)$.

We must now examine the relationship between $H^k(X;A)$ and $H_k(X)$ thus defined. As stated at the beginning of this post, it is not true that $H^k(X;A)\cong H_k(X)^\ast$ in general. However, by an argument similar to the proof of [Proposition 1](#prop1) above, we obtain the following proposition.

<div class="proposition" markdown="1">

<ins id="prop3">**Proposition 3 (Universal coefficient theorem for cohomology)**</ins> For any topological space $X$ and abelian group $A$, there exists a short exact sequence

$$0\rightarrow\Ext_\mathbb{Z}^1(H_{k-1}(X), A)\rightarrow H^k(X;A)\rightarrow \Hom_\mathbb{Z}(H_k(X),A)\rightarrow 0$$

Moreover, this sequence splits (non-canonically), and therefore yields the (non-canonical) isomorphism

$$H^k(X;A)\cong \Hom_\mathbb{Z}(H_k(X),A)\oplus \Ext^1_\mathbb{Z}(H_{k-1}(X),A)$$

</div>

Roughly speaking, this can be thought of as translating [Proposition 1](#prop1) via [\[Algebraic Structures\] §Abelian Groups, ⁋Theorem 15](/en/math/algebraic_structures/abelian_groups#thm15).

## de Rham Cohomology

Associating a chain complex $C_\bullet(X)$ to a topological space $X$ can be said to transfer information about the subspaces of $X$ into algebraic terms. When defining cohomology, we apply $\Hom_\mathbb{Z}(-,A)$ to $C_\bullet(X)$ and then take the homology of the resulting cochain complex; here

$$C^k(X;A)=\Hom_\mathbb{Z}(C_k(X), A)$$

and an arbitrary element of this can be thought of as a function assigning an element of $A$ to each element of $C_k(X)$ (that is, to each $k$-chain). Thus cohomology can essentially be said to study functions defined on a space.

More concretely, for any $c\in C_k(X)$ and $\varphi\in C^k(X;A)$, we know that the following canonical pairing exists:

$$C_k(X)\times C^k(X;A)\rightarrow A;\qquad (c,\varphi)\mapsto \varphi(c)\in A$$

If we write $\partial$ for the boundary map of $C_\bullet(X)$ and $\delta$ for the coboundary map of $C^\bullet(X;A)$ induced by it, then for any $c\in C_{k+1}(X)$ and $\varphi\in C^k(X;A)$ the identity

$$\langle \partial c, \varphi\rangle=\langle c, \delta\varphi\rangle$$

holds, and from this we know that these induce a pairing at the homology and cohomology level

$$H_k(X)\times H^k(X;A)\rightarrow A$$

For example, to look at de Rham cohomology, consider the $\mathbb{R}$-vector spaces of differential $k$-forms

$$\Omega^k(\mathbb{R}^n)=\{\text{$k$-forms on $\mathbb{R}^n$}\}$$

Here the coboundary map $\Omega^k(\mathbb{R}^n)\rightarrow \Omega^{k+1}(\mathbb{R}^n)$ is given by the exterior derivative, and a differential $k$-form outputs a number via integration when given a $k$-dimensional subset. Also, closed $k$-forms are given by the kernel of this coboundary, and exact $k$-forms by its image.

For example, consider the differential $2$-form on $\mathbb{R}^3$

$$\omega=dx\wedge dy$$

A $2$-dimensional subset of $\mathbb{R}^3$ is given by a map from a (unit) rectangle in $\mathbb{R}^2$ to $\mathbb{R}^3$, and through this we know what it means to apply $\omega$ to a $2$-dimensional subset.

For example, given the set

$$S = \{ (x, y, 0) \mid 0 \leq x \leq 1,\, 0 \leq y \leq 1 \}$$

the value of $\omega$ on this set is simply computed as

$$\int_S \omega = \int_{x=0}^{1} \int_{y=0}^{1} 1\,dy\,dx = 1$$

As another example, if the surface

$$\Sigma = \{ (x, y, z) \mid x^2 + y^2 + z^2 = 1,\ z \geq 0 \}$$

is given, we first parametrize it as a map from $[0,\pi/2]\times[0,2\pi]$ to $\Sigma$ using spherical coordinates

$$x = \sin \phi \cos \theta,\qquad y = \sin \phi \sin \theta,\qquad z = \cos \phi$$

and then using $dx \wedge dy = \sin \phi \cos \phi\, d\phi \wedge d\theta$ we can compute the integral as

$$\begin{align*}
\int_{\Sigma} \omega
&= \int_{0}^{2\pi} \int_{0}^{\pi/2} \sin \phi \cos \phi\, d\phi \, d\theta = \int_{0}^{2\pi} d\theta \int_{0}^{\pi/2} \sin \phi \cos \phi\, d\phi \\
&= 2\pi \times \frac{1}{2} \int_{0}^{\pi/2} \sin(2\phi) d\phi = 2\pi \times \frac{1}{2} \left[ -\frac{1}{2} \cos(2\phi) \right]_{0}^{\pi/2} \\
&= 2\pi \times \frac{1}{2} \left( -\frac{1}{2} [\cos(\pi) - \cos(0)] \right) = 2\pi \times \frac{1}{2} \left( -\frac{1}{2}(-1 - 1) \right) = 2\pi \times \frac{1}{2} \times 1 \\
&= \pi
\end{align*}$$

Thus the differential $2$-form $\omega$ can be thought of as a function that takes $2$-dimensional subsets such as $S$ or $\Sigma$ and outputs a number.

Now by the Poincaré lemma, we know that any closed $k$-form on $\mathbb{R}^n$ is always the exterior derivative of a suitable $(k-1)$-form. Therefore for any $k>0$

$$H^k_\dR(\mathbb{R}^n)=0$$

and for $k=0$, the functions whose derivative is $0$ are exactly the constant functions, so

$$H^0_\dR(\mathbb{R}^n)=\mathbb{R}$$

The de Rham cohomology defined in this way also satisfies all the conditions of [Definition 2](#def2), and therefore by the uniqueness of cohomology theory (and the fact that any singular chain can be approximated by a smooth chain), we can verify that singular cohomology with $\mathbb{R}$ coefficients and de Rham cohomology coincide. The computation above is then nothing but translating the computation of [§Homology, ⁋Proposition 11](/en/math/algebraic_topology/homology#prop11) into $\mathbb{R}$-valued cohomology via [Proposition 3](#prop3).
 
## Coefficients of (Co)homology

The de Rham cohomology examined above is an example of a cohomology theory whose coefficient group is not $\mathbb{Z}$. Unlike singular or simplicial cohomology theory, de Rham cohomology naturally has $\mathbb{R}$ as its coefficient group by definition.
  
Such a cohomology theory has nice properties: for example, since $\mathbb{R}$ is a torsion-free abelian group, $\Tor_1^\mathbb{Z}(A,\mathbb{R})=0$ holds for any abelian group $A$, and therefore by [Proposition 1](#prop1) we know that the isomorphism

$$H_k(X;\mathbb{R})\cong H_k(X)\otimes_\mathbb{Z}\mathbb{R}$$

holds. Moreover, since $\mathbb{R}$ is an injective $\mathbb{Z}$-module, $\Ext_\mathbb{Z}^1(A,\mathbb{R})=0$ holds for any abelian group $A$, and therefore this time [Proposition 3](#prop3) gives the isomorphism

$$H^k(X;\mathbb{R})\cong \Hom_\mathbb{Z}(H_k(X),\mathbb{R})$$

Thus examining this kind of homology and cohomology becomes another topic of interest. Recalling the chain complexes used to define $H_k(X;A)$ and $H^k(X;A)$, we know that the two chain complexes

$$C_\bullet(X;A):=C_\bullet(X)\otimes_\mathbb{Z}A,\qquad C_\bullet^\Delta(X;A):=C_\bullet^\Delta(X)\otimes_\mathbb{Z}A$$

are chain complexes of $A$-modules if $A$ is a ring, and the $C^\bullet(X;A)$ defined above is also such. Therefore taking homology or cohomology of these yields $A$-modules as well.

On the other hand, we know that if $A$ is a principal ideal domain, then any submodule of a free $A$-module is again a free $A$-module. Looking back at the proof of [Proposition 1](#prop1), we used the fact that since $\mathbb{Z}$ is a principal ideal domain, any submodule of a free $\mathbb{Z}$-module (that is, a free abelian group) is again a free $\mathbb{Z}$-module; based on this, we can generalize the preceding two propositions as follows.

<div class="proposition" markdown="1">

<ins id="thm4">**Theorem 4 (Universal coefficient theorem for homology, general version)**</ins> For a principal ideal domain $A$, a chain complex $C_\bullet$ of free $A$-modules, and any $A$-module $M$, there exists a short exact sequence

$$0 \rightarrow H_k(C)\otimes_AM\rightarrow H_k(C\otimes_AM)\rightarrow \Tor_1^A(H_{k-1}(C), A)\rightarrow 0$$

Moreover, this sequence splits (non-canonically), and therefore yields the (non-canonical) isomorphism

$$H_k(C\otimes_AM)\cong \left(H_k(C)\otimes_AM\right)\oplus \Tor_1^A(H_{k-1}(C), M)$$

</div>

<div class="proposition" markdown="1">

<ins id="thm5">**Theorem 5 (Universal coefficient theorem for cohomology, general version)**</ins> For a principal ideal domain $A$, a chain complex $C_\bullet$ of free $A$-modules, and any $A$-module $M$, there exists a short exact sequence

$$0\rightarrow\Ext_A^1(H_{k-1}(C), M)\rightarrow H_k(\Hom_A(C,M))\rightarrow \Hom_A(H_k(C),M)\rightarrow 0$$

Moreover, this sequence splits (non-canonically), and therefore yields the (non-canonical) isomorphism

$$H_k(\Hom_A(C,M))\cong \Hom_A(H_k(C),M)\oplus \Ext^1_A(H_{k-1}(C),M)$$

</div>

## Mayer-Vietoris Sequence

Meanwhile, among the axioms of [Definition 2](#def2), the excision axiom allows us to compute the cohomology of a large space from the cohomology of small spaces. The following proposition is the cohomology version of [\[Algebraic Topology\] §Computation of Homology, ⁋Proposition 7](/en/math/algebraic_topology/computation_of_homology#prop7), and its proof is obtained by repeating the process from [\[Algebraic Topology\] §Computation of Homology, ⁋Definition 6](/en/math/algebraic_topology/computation_of_homology#def6) to [\[Algebraic Topology\] §Computation of Homology, ⁋Proposition 7](/en/math/algebraic_topology/computation_of_homology#prop7), starting from [Definition 2](#def2).

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6 (Mayer-Vietoris sequence)**</ins> Let a topological space $X$ be expressed as the union $X=U\cup V$ of two open sets, and consider a cohomology theory $H$ defined on it. Then there exists a long exact sequence

$$\cdots \to H^{n}(X) \xrightarrow{(i^*, j^*)} H^{n}(U) \oplus H^{n}(V) \xrightarrow{k^* - l^*} H^{n}(U \cap V) \xrightarrow{\delta} H^{n+1}(X) \to \cdots$$

where $i^\ast, j^\ast, k^\ast, l^\ast$ are the maps induced by the inclusions

$$i:U\rightarrow X,\quad j:V\rightarrow X,\quad k:U\cap V\rightarrow U,\quad l:U\cap V \rightarrow V$$

</div>

## Tensor Product of Chain Complexes

Using the Mayer-Vietoris sequence, we can compute the homology or cohomology of a large space from those of its small subspaces. On the other hand, we can also multiply two spaces $X,Y$ to create a larger space $X\times Y$, and the Künneth formula helps us compute the homology and cohomology of such product spaces. To this end, we must first define the tensor product of two chain complexes $C_\bullet$, $D_\bullet$.

<div class="definition" markdown="1">

<ins id="def7">**Definition 7**</ins> Let $A$ be a ring and $C_\bullet,D_\bullet$ be chain complexes of $A$-modules. Their *tensor product* $(C\otimes D)_\bullet$ is defined for each $k$ by

$$(C\otimes D)_k=\bigoplus_{p+q=k}C_p\otimes_A D_q$$

and the differential is defined on homogeneous elements by

$$\partial(x,y)=(\partial^Cx,y)+(-1)^{\deg(x)}(x,\partial^Dy)$$

and then extended linearly.

</div>

That is, $(C\otimes D)_\bullet$ can be regarded as the total complex of a double complex whose $(p,q)$-component is $C_p\otimes D_q$, with horizontal differential $\partial^C\otimes\id_D$ and vertical differential $\id_C\otimes \partial^D$. ([§Homology, ⁋Definition 5](/en/math/homological_algebra/homology#def5))

The algebraic content of the Künneth formula is contained in the following lemma.

<div class="proposition" markdown="1">

<ins id="lem8">**Lemma 8**</ins> Let $A$ be a principal ideal domain and $C_\bullet$, $D_\bullet$ be chain complexes of $A$-modules, and suppose $C_\bullet$ is a chain complex of free $A$-modules. Then for any $k$ there exists a short exact sequence

$$0 \rightarrow \bigoplus_{p+q=k}H_p(C)\otimes_AH_q(D)\rightarrow H_k(C\otimes D)\rightarrow \bigoplus_{p+q=k-1}\Tor_1^A(H_p(C),H_q(D))\rightarrow 0$$

Moreover, this short exact sequence splits (non-canonically), and therefore there exists an isomorphism

$$H_k(C\otimes D)\cong \left( \bigoplus_{p+q=k}H_p(C)\otimes_AH_q(D)\right)\oplus \left(\bigoplus_{p+q=k-1}\Tor_1^A(H_p(C),H_q(D)) \right)$$

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, consider the short exact sequence

$$0 \rightarrow Z_p(C) \rightarrow C_p\rightarrow B_{p-1}(C)\rightarrow 0$$

Since $B_{p-1}(C)$ and $Z_p(C)$ are submodules of the free $A$-modules $C_{p-1},C_p$ and $A$ is a principal ideal domain, they are again free $A$-modules. Therefore, tensoring this short exact sequence with $D_q$ yields the short exact sequence

$$0\rightarrow Z_p(C)\otimes D_q \rightarrow C_p\otimes D_q \rightarrow B_{p-1}(C)\otimes D_q\rightarrow 0$$

From the definition of the chain complex $(C\otimes D)_\bullet$, considering such short exact sequences for all $(p,q)$ with $p+q=k$ and taking their direct sum gives the short exact sequence

$$0 \rightarrow (Z(C)\otimes D)_k \rightarrow (C\otimes D)_k \rightarrow (B(C)\otimes D)_{k-1}\rightarrow 0$$

Now considering the long exact sequence of homologies from this short exact sequence, we obtain

$$\cdots \rightarrow H_{k}(B(C)\otimes D)\overset{\delta_k}{\longrightarrow} H_{k}(Z(C)\otimes D)\rightarrow H_{k}(C\otimes D)\rightarrow H_{k-1}(B(C)\otimes D)\overset{\delta_{k-1}}{\longrightarrow} H_{k-1}(Z(C)\otimes D)\rightarrow \cdots$$

In particular, centering on $H_k(C\otimes D)$, we obtain the short exact sequence

$$0 \rightarrow \coker\delta_k\rightarrow H_k(C\otimes D)\rightarrow \ker\delta_{k-1}\rightarrow 0 \tag{$\ast$}$$

To examine $\coker\delta_k$ and $\ker\delta_{k-1}$, consider the short exact sequence

$$0 \rightarrow B_\bullet(C)\rightarrow Z_\bullet(C)\rightarrow H_\bullet(C)\rightarrow 0$$

and the exact sequence obtained by taking the tensor product with $H_\bullet(D)$:

$$0 \rightarrow \Tor_1^A(H(C), H(D))_\bullet\rightarrow (B(C)\otimes H(D))_\bullet\rightarrow (Z(C) \otimes H(D))_\bullet \rightarrow (H(C)\otimes H(D))_\bullet \rightarrow 0$$

Here the first term $0$ comes from the fact that $Z_\bullet(C)$ consists of free modules. On the other hand, since free modules are flat, taking the tensor product with a free module commutes with taking homology, and therefore in the above sequence we know that

$$(B(C)\otimes H(D))_\bullet\cong H_\bullet(B(C)\otimes D)\qquad (Z(C)\otimes H(D))_\bullet \cong H_\bullet(Z(C)\otimes D)$$

The map $(B(C)\otimes H(D))_\bullet \rightarrow (Z(C)\otimes H(D))_\bullet$ is obtained from the inclusion $B_\bullet(C)\rightarrow Z_\bullet(C)$, and after the above identification it is the same map as $\delta_\bullet$. Therefore we obtain

$$\coker \delta_k\cong (H(C)\otimes H(D))_k,\qquad \ker \delta_{k-1}\cong \Tor_1^A(H(C),H(D))_{k-1}$$

As for the claim about splitting, since

$$0 \rightarrow Z_\bullet(C)\rightarrow C_\bullet \rightarrow B_{\bullet-1}(C) \rightarrow 0$$

is a split exact sequence, a section $B_{\bullet-1}(C)\rightarrow C_\bullet$ induces a splitting of ($\ast$).

</details>

## Eilenberg-Zilber Theorem and Künneth Formula

Keeping the result of [Lemma 8](#lem8) in mind, what we need to do is clear. Given two topological spaces $X,Y$ and their corresponding chain complexes $C_\bullet(X),C_\bullet(Y)$, we examine the relationship between the homology $H_\bullet(X\times Y)$ of the product space $X\times Y$ and the tensor product $(H(X)\otimes H(Y))_\bullet$ of the two chain complexes $H_\bullet(X)$, $H_\bullet(Y)$. The following theorem shows that these two algebraic objects are the same.

<div class="proposition" markdown="1">

<ins id="thm9">**Theorem 9 (Eilenberg-Zilber)**</ins> For two topological spaces $X,Y$ and the chain complexes $C_\bullet(X),C_\bullet(Y)$, and $C_\bullet(X\times Y)$ obtained from them, there exists a chain homotopy equivalence between the two chain complexes $(C(X)\otimes C(Y))_\bullet$ and $C_\bullet(X\times Y)$, and therefore

$$H_\bullet(C(X\times Y))\cong H_\bullet(C(X)\otimes C(Y))$$

holds.

</div>

This is generally proved using the [acyclic models theorem](https://en.wikipedia.org/wiki/Acyclic_model), but since the acyclic models theorem is in fact closer to a generalization of the Eilenberg-Zilber theorem, using it to prove this result feels like overkill. However, since proving the Eilenberg-Zilber theorem directly is quite tedious, we will only examine the two maps that appear in its proof:

$$\AW:C_\bullet(X\times Y) \rightarrow (C(X)\otimes C(Y))_\bullet,\qquad \EZ:(C(X)\otimes C(Y))_\bullet \rightarrow C_\bullet(X\times Y)$$

We will write the proof of the acyclic models theorem in a separate post so as not to break the flow.

First, the Alexander-Whitney map $\AW:C_\bullet(X\times Y) \rightarrow (C(X)\otimes C(Y))_\bullet$ is obtained by sending an arbitrary $k$-simplex $\sigma:\Delta^k \rightarrow X\times Y$ to

$$\sum_p (\pi_X\circ \sigma\vert_{[v_0,\ldots,v_p]})\otimes (\pi_Y\circ \sigma\vert_{[v_p,\ldots v_k]})\in \bigoplus_{p+q=k}C_p(X)\otimes C_q(Y)$$

If $X=Y$, this would be the map making $C(X)$ into a (differential graded counital coassociative) coalgebra via $C(X)\rightarrow C(X)\otimes C(X)$, and for this reason it will reappear in the next post.

The Eilenberg-Zilber map $\EZ:(C(X)\otimes C(Y))_\bullet \rightarrow C_\bullet(X\times Y)$ is defined on simple tensors by the formula

$$\EZ(\sigma\otimes\tau)=\sum_{\substack{\alpha_1<\cdots <\alpha_p\\\beta_1<\cdots <\beta_q}}\sgn(\alpha_1,\ldots,\alpha_p,\beta_1,\ldots,\beta_q)(\sigma\circ s_{\alpha_p}\cdots s_{\alpha_1})\times(\tau\circ s_{\beta_q}\cdots s_{\beta_1})$$

Although this looks complicated as a formula, it is nothing but the $h_n$ function appearing in the proof of [§Homotopy, ⁋Proposition 6](/en/math/algebraic_topology/homotopy#prop6), that is, the method of decomposing the prism $\Delta^p\times \Delta^q$ into simplices. Then the result of [Theorem 9](#thm9) follows from the two identities

$$\AW\circ\EZ=\id_{(C(X)\otimes C(Y))_\bullet},\qquad \EZ\circ \AW\simeq \id_{C_\bullet(X\times Y)}$$

Therefore, combining [Lemma 8](#lem8) with [Theorem 9](#thm9) yields the following result.

<div class="proposition" markdown="1">

<ins id="cor10">**Corollary 10 (Künneth)**</ins> Fix topological spaces $X,Y$. Then for their product space $X\times Y$ and a principal ideal domain $A$, there exists a short exact sequence

$$0 \rightarrow \bigoplus_{p+q=k}H_p(X;A)\otimes_AH_q(Y;A)\rightarrow H_k(X\times Y;A)\rightarrow \bigoplus_{p+q=k-1}\Tor_1^A(H_p(X;A),H_q(Y;A))\rightarrow 0$$

Moreover, this short exact sequence splits (non-canonically), and therefore there exists an isomorphism

$$H_k(X\times Y;A)\cong \left( \bigoplus_{p+q=k}H_p(X;A)\otimes_AH_q(Y;A)\right)\oplus \left(\bigoplus_{p+q=k-1}\Tor_1^A(H_p(X;A),H_q(Y;A)) \right)$$

</div>

Of course, using this result together with [Theorem 5](#thm5), one can obtain the cohomology version of the Künneth formula.

--- 

**References**

[Hat] A. Hatcher, *Algebraic Topology*. Cambridge University Press, 2022.  
[May] J. P. May, *A concise course in algebraic topology*.

---

[^1]: Of course, we would like this pairing to give a homomorphism from $H^k(X;A)$ to $\Hom(H_k(X),A)$, but as we know from [Proposition 3](#prop3), the situation is not so simple and an $\Ext$ term containing hidden torsion must appear.
