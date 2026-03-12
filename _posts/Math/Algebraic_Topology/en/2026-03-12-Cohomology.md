---

title: "Cohomology"
excerpt: ""

categories: [Math / Algebraic Topology]
permalink: /en/math/algebraic_topology/cohomology
header:
    overlay_image: /assets/images/Math/Algebraic_Topology/Cohomology.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_topology-en"

date: 2026-03-12
last_modified_at: 2026-03-12
weight: 6

---

Cohomology, as the name suggests, can be described as the dual concept to homology. However, if the $k$-th cohomology $H^k(X)$ of a space $X$ were simply the dual of the $k$-th homology $H_k(X)$, there would be no need to consider it separately.

In fact, cohomology provides a more refined invariant than homology; for instance, a natural multiplication structure can be defined on cohomology, and even for spaces with the same homology, if this multiplicative structure differs, they are not homotopic. In this article, we examine the definition and fundamental properties of cohomology.

## Universal Coefficient Theorem for Homology

Before beginning our main discussion, we first examine homology with coefficients, which we covered after [§Computation of Homology, ⁋Definition 6](/en/math/algebraic_topology/computation_of_homology#def6). When defining simplicial homology or singular homology, we saw that by taking the tensor product with an abelian group $A$ instead of the chain groups $C_\bullet(X)$ or $C_\bullet^\Delta(X)$, we obtain the chain complex

$$C_\bullet(X;A):=C_\bullet(X)\otimes_\mathbb{Z}A,\qquad C_\bullet^\Delta(X;A):=C_\bullet^\Delta(X)\otimes_\mathbb{Z}A$$

and then we can define the homology groups

$$H_k(X;A),\qquad H_k^\Delta(X;A)$$

as the homology groups of these complexes. To compute these practically, we would need to examine whether $H_k(X;A)$ or $H_k^\Delta(X;A)$ takes the form $H_k(X;A)\otimes_\mathbb{Z}A$ or $H_k^\Delta(X;A)\otimes_\mathbb{Z}A$. However, since tensor products are right-exact but not left-exact in general, this would be an excessive expectation, and we need to additionally measure the information lost by taking the tensor product.

For this purpose, consider a chain complex $C_\bullet$ consisting of free abelian groups, and the following short exact sequence in $\Ch_{\geq 0}(\Ab)$

$$0 \rightarrow Z_\bullet \rightarrow C_\bullet \rightarrow B_{\bullet-1}\rightarrow 0\tag{1}$$

Here $Z_k=\ker(\partial:C_k \rightarrow C_{k-1})$ and $B_{k-1}=\im(\partial:C_k \rightarrow C_{k-1})$, and the first map in the above sequence is the inclusion, while the second is the boundary map $\partial$.

At this point, since $Z_{k}$ and $B_{k-1}$ are subgroups of the free abelian groups $C_k,C_{k-1}$ respectively, they are free, and thus by [##ref##](third_term_projective_splits), this short exact sequence is a split exact sequence. Therefore, for any abelian group $A$, the following sequence

$$0 \rightarrow Z_\bullet\otimes_\mathbb{Z}A \rightarrow C_\bullet\otimes_\mathbb{Z}A \rightarrow B_{\bullet-1}\otimes_\mathbb{Z}A\rightarrow 0$$

is also a splitting short exact sequence. ([##ref](splitting_tensor_splits)) When we expand these, we obtain the following commutative diagram

![snake_lemma](/assets/images/Math/Algebraic_Topology/Cohomology-1.png){:style="width:32em" class="invert" .align-center}

and therefore by [[Homological Algebra] §Long Exact Sequences, ⁋Theorem 1](/en/math/homological_algebra/long_exact_sequence#thm1), we obtain the following long exact sequence

$$\cdots B_k\otimes_\mathbb{Z}A\overset{\delta_k}{\longrightarrow}Z_k\otimes_\mathbb{Z}A\rightarrow H_k(C\otimes A)\rightarrow B_{k-1}\otimes_\mathbb{Z}A\overset{\delta_{k-1}}{\longrightarrow} Z_{k-1}\otimes_\mathbb{Z}A\rightarrow\cdots\tag{2}$$

Now to extract information from this exact sequence, we need to examine the connecting maps $\delta$. Following the definition, $\delta_k:B_k\otimes_\mathbb{Z}A\rightarrow Z_k\otimes_\mathbb{Z}A$ is exactly the map obtained by applying $-\otimes \id_A$ to the inclusion homomorphism $i_k:B_k \rightarrow Z_k$. So let us consider the following short exact sequence

$$0 \rightarrow B_k\overset{i_k}{\longrightarrow} Z_k \overset{p_k}{\longrightarrow}H_k(C)\rightarrow 0$$

Then, since $B_k$, $Z_k$, and $0$ are all free abelian groups, this can be viewed as a free resolution of $H_k(C_\bullet)$, and therefore by definition, we can place $\delta_k$ in the following exact sequence

$$0 \rightarrow \Tor_1^\mathbb{Z}(H_k(C))\rightarrow B_k\otimes_\mathbb{Z}A\overset{\delta_k}{\longrightarrow} Z_k\otimes_\mathbb{Z}A\rightarrow H_k\otimes_\mathbb{Z}A\rightarrow 0$$

In other words, the following isomorphisms

$$\ker\delta_{k-1}\cong \Tor_1^\mathbb{Z}(H_{k-1}(C), A),\qquad \coker\delta_k\cong H_k(C)\otimes_\mathbb{Z} A$$

exist, and substituting these into (2) yields the short exact sequence

$$0 \rightarrow H_k(C)\otimes_\mathbb{Z}A\rightarrow H_k(C;A)\rightarrow \Tor_1^\mathbb{Z}(H_{k-1}(C), A)\rightarrow 0$$

On the other hand, since (1) is a splitting short exact sequence, we can choose a retraction $r_k:C_k \rightarrow Z_k$. ([[Multilinear Algebra] §Exact Sequences, ⁋Proposition 10](/en/math/multilinear_algebra/exact_sequences#prop10)) Then under this choice, $(p_k\circ r_k)\otimes \id_A$ induces the map $H_k(C;A)\rightarrow H_k(C)\otimes_\mathbb{Z} A$ in homology, and we know this is a retraction of the above $H_k(C)\otimes_\mathbb{Z}A\rightarrow H_k(C;A)$. Thus we obtain the following.

<div class="proposition" markdown="1">

<ins id="prop1">**Proposition 1 (Universal coefficient theorem for homology)**</ins> For any topological space $X$ and abelian group $A$, the following short exact sequence

$$0 \rightarrow H_k(X)\otimes_\mathbb{Z}A\rightarrow H_k(X;A)\rightarrow \Tor_1^\mathbb{Z}(H_{k-1}(X), A)\rightarrow 0$$

exists. Moreover, this sequence splits (non-canonically) and therefore gives the following (non-canonical) isomorphism

$$H_k(X;A)\cong \left(H_k(X)\otimes_\mathbb{Z}A\right)\oplus \Tor_1^\mathbb{Z}(H_{k-1}(X), A)$$

</div>


## Definition of Cohomology and Universal Coefficient Theorem

As in [§Computation of Homology, ⁋Definition 6](/en/math/algebraic_topology/computation_of_homology#def6), we can define the Eilenberg-Steenrod axioms for cohomology, and contravariant functors and connecting morphisms satisfying these can be called cohomology. Explicitly, they are as follows.

<div class="definition" markdown="1">

<ins id="def2">**Definition 2 (Eilenberg-Steenrod axioms)**</ins> For contravariant functors $H^k$ from the category of pairs of topological spaces to the category of abelian groups, and natural transformations between them

$$\delta: H^k(X) \rightarrow H^{k+1}(X,A)$$

the *Eilenberg-Steenrod axioms* refer to the following axioms.

- (Homotopy) If two homotopic maps $(X,A) \rightarrow (Y,B)$ are given, then the two homomorphisms $H^k(Y,B) \rightarrow H^k(X,A)$ they induce are identical.
- (Excision) For $(X,A,Z)$ satisfying the conditions of [§Computation of Homology, ⁋Theorem 2](/en/math/algebraic_topology/computation_of_homology#thm2), $(X\setminus Z, A\setminus Z)\hookrightarrow (X,A)$ induces an isomorphism.
- (Dimension) For a one-point space $\ast$, $H^k(\ast)=0$ holds for all $k>0$.
- (Additivity) If $X=\coprod X_\alpha$, then $H^k(X)\cong\bigoplus H^k(X_\alpha)$.
- (Exactness) For each pair $(X,A)$ and the two inclusions $(A,\emptyset) \hookrightarrow (X,\emptyset)$ and $(X,\emptyset)\hookrightarrow (X,A)$, they fit into the following long exact sequence
    
    $$\cdots \rightarrow H^k(X,A)\rightarrow H^k(X) \rightarrow H^k(A) \rightarrow H^{k+1}(X,A)\rightarrow \cdots$$

</div>

To demonstrate the existence of a cohomology theory satisfying these conditions, as in [§Homology](/en/math/algebraic_topology/homology), let us consider the chain complex consisting of singular simplices of a topological space $X$

$$C_\bullet(X):\qquad\cdots \rightarrow C_{k+1}(X)\rightarrow C_k(X) \rightarrow C_{k-1}(X)\rightarrow \cdots$$

If we fix an abelian group $A$ to use as the coefficient group, we can consider the following chain complex corresponding to the dual of this chain complex

$$(C^\vee)^\bullet(X;A):\qquad\cdots \leftarrow \Hom_\mathbb{Z}(C_{k+1}(X), A)\leftarrow\Hom_\mathbb{Z}(C_k(X),A)\leftarrow\Hom_\mathbb{Z}(C_{k-1}(X),A)\leftarrow\cdots$$

By [[Algebraic Structures] §Direct Products and Direct Sums, Tensor Products of Modules, ⁋Theorem 6](/en/math/algebraic_structures/operations_of_modules#thm6), this can be viewed as

$$\qquad \cdots\leftarrow\Hom_A(C_{k+1}(X;A),A)\leftarrow \Hom_A(C_k(X;A),A)\leftarrow \Hom_A(C_{k-1}(X;A),A)\leftarrow\cdots$$

so it can be thought of as the dual of the chain complex $C_\bullet(X;A)$. We then denote the $k$-th homology of this chain complex $(C^\vee)^\bullet(X;A)$ as

$$H^k(X;A):=H_k(C^\vee)$$

and call this the *$k$-th cohomology* of $X$. Here, the reason we use superscripts to index $H$ and $C^\vee$ is that, in contrast to homology, the long exact sequence is formed in the direction of increasing index. From now on, when there is no confusion, we will write $(C^\vee)^\bullet(X)$ as $C^\bullet(X;A)$.

Now we need to examine what relationship exists between $H^k(X;A)$ and $H_k(X)$ defined in this way. As mentioned at the beginning of this article, $H^k(X;A)\cong H_k(X)^\ast$ does not hold in general. However, using a method similar to the proof of [Proposition 1](#prop1) above, we can obtain the following proposition.

<div class="proposition" markdown="1">

<ins id="prop3">**Proposition 3 (Universal coefficient theorem for cohomology)**</ins> For any topological space $X$ and abelian group $A$, the following short exact sequence

$$0\rightarrow\Ext_\mathbb{Z}^1(H_{k-1}(X), A)\rightarrow H^k(X;A)\rightarrow \Hom_\mathbb{Z}(H_k(X),A)\rightarrow 0$$

exists. Moreover, this sequence splits (non-canonically) and therefore gives the following (non-canonical) isomorphism

$$H^k(X;A)\cong \Hom_\mathbb{Z}(H_k(X),A)\oplus \Ext^1_\mathbb{Z}(H_{k-1}(X),A)$$

</div>

Roughly speaking, this can be thought of as translating [Proposition 1](#prop1) through [[Algebraic Structures] §Abelian Groups, ⁋Theorem 15](/en/math/algebraic_structures/abelian_groups#thm15).

## de Rham Cohomology

Associating a chain complex $C_\bullet(X)$ to a topological space $X$ can be described as algebraically encoding information about the subspaces of $X$. When defining cohomology, we apply $\Hom_\mathbb{Z}(-,A)$ to $C_\bullet(X)$ and then define the homology of this cochain complex, where

$$C^k(X;A)=\Hom_\mathbb{Z}(C_k(X), A)$$

can be thought of as a function that assigns an element of $A$ to each element of $C_k(X)$ (i.e., to each $k$-chain). In other words, cohomology essentially involves looking at functions defined on the space.

More concretely, for any $c\in C_k(X)$ and $\varphi\in C^k(X;A)$, we know there exists the following canonical pairing

$$C_k(X)\times C^k(X;A)\rightarrow A;\qquad (c,\varphi)\mapsto \varphi(c)\in A$$

and if we denote the boundary map of $C_\bullet(X)$ as $\partial$ and the coboundary map of $C^\bullet(X;A)$ derived from it as $\delta$, then for any $c\in C_{k+1}(X)$ and $\varphi\in C^k(X;A)$, the following equation

$$\langle \partial c, \varphi\rangle=\langle c, \delta\varphi\rangle$$

holds, and from this we know that they give a pairing at the homology and cohomology level

$$H_k(X)\times H^k(X;A)\rightarrow A$$

[^1]

For example, to examine de Rham cohomology, consider the $\mathbb{R}$-vector spaces consisting of differential $k$-forms

$$\Omega^k(\mathbb{R}^n)=\{\text{$k$-forms on $\mathbb{R}^n$}\}$$

Here, the coboundary map $\Omega^k(\mathbb{R}^n)\rightarrow \Omega^{k+1}(\mathbb{R}^n)$ is given by the exterior derivative, and a differential $k$-form, when given a $k$-dimensional subset, produces a corresponding number through integration. Also, closed $k$-forms are given as the kernel of this coboundary, and exact $k$-forms are given as the image of this coboundary.

For instance, consider the differential $2$-form defined on $\mathbb{R}^3$

$$\omega=dx\wedge dy$$

A $2$-dimensional subset of $\mathbb{R}^3$ is given by a function from a (unit) rectangle in $\mathbb{R}^2$ to $\mathbb{R}^3$, and through this we understand what it means to apply $\omega$ to a $2$-dimensional subset.

For example, suppose the following set

$$S = \{ (x, y, 0) \mid 0 \leq x \leq 1,\, 0 \leq y \leq 1 \}$$

is given. Then the value of $\omega$ on this set is simply calculated as

$$\int_S \omega = \int_{x=0}^{1} \int_{y=0}^{1} 1\,dy\,dx = 1$$

As another example, if the surface

$$\Sigma = \{ (x, y, z) \mid x^2 + y^2 + z^2 = 1,\ z \geq 0 \}$$

is given, we first use spherical coordinates

$$x = \sin \phi \cos \theta,\qquad y = \sin \phi \sin \theta,\qquad z = \cos \phi$$

to parametrize it as a function from $[0,\pi/2]\times[0,2\pi]$ to $\Sigma$, and then use $dx \wedge dy = \sin \phi \cos \phi\, d\phi \wedge d\theta$ to calculate

$$\begin{align*}
\int_{\Sigma} \omega
&= \int_{0}^{2\pi} \int_{0}^{\pi/2} \sin \phi \cos \phi\, d\phi \, d\theta = \int_{0}^{2\pi} d\theta \int_{0}^{\pi/2} \sin \phi \cos \phi\, d\phi \\
&= 2\pi \times \frac{1}{2} \int_{0}^{\pi/2} \sin(2\phi) d\phi = 2\pi \times \frac{1}{2} \left[ -\frac{1}{2} \cos(2\phi) \right]_{0}^{\pi/2} \\
&= 2\pi \times \frac{1}{2} \left( -\frac{1}{2} [\cos(\pi) - \cos(0)] \right) = 2\pi \times \frac{1}{2} \left( -\frac{1}{2}(-1 - 1) \right) = 2\pi \times \frac{1}{2} \times 1 \\
&= \pi
\end{align*}$$

Thus, the differential $2$-form $\omega$ can be thought of as a function that takes a $2$-dimensional subset such as $S$ or $\Sigma$ and produces a number.

Now, by the Poincaré lemma, we know that any closed $k$-form on $\mathbb{R}^n$ is always the exterior derivative of some $(k-1)$-form. Therefore, for any $k>0$,

$$H^k_\dR(\mathbb{R}^n)=0$$

and for $k=0$, since functions that become $0$ when differentiated are exactly constant functions,

$$H^0_\dR(\mathbb{R}^n)=\mathbb{R}$$

The de Rham cohomology defined in this way also satisfies all the conditions of [Definition 2](#thm2), and therefore by the uniqueness of cohomology theory (and the fact that any singular chain can be approximated by a smooth chain), we can confirm that singular cohomology with $\mathbb{R}$ coefficients and de Rham cohomology are the same. The above calculation is then nothing more than translating the calculation in [§Homology, ⁋Proposition 11](/en/math/algebraic_topology/homology#prop11) to $\mathbb{R}$-valued cohomology through [Proposition 3](#prop3).
 
## Coefficients of (Co)homology

The de Rham cohomology examined above is an example of a cohomology theory where the coefficient group is not $\mathbb{Z}$. Unlike singular cohomology or simplicial cohomology theory, in de Rham cohomology, it is natural from the definition that the coefficient group is $\mathbb{R}$.
  
Such cohomology theories have good properties; for instance, since $\mathbb{R}$ is a torsion-free abelian group, $\Tor_1^\mathbb{Z}(A,\mathbb{R})=0$ holds for any abelian group $A$, and therefore by [Proposition 1](#prop1), we know the following isomorphism

$$H_k(X;\mathbb{R})\cong H_k(X)\otimes_\mathbb{Z}\mathbb{R}$$

holds. Moreover, since $\mathbb{R}$ is an injective $\mathbb{Z}$-module, $\Ext_\mathbb{Z}^1(A,\mathbb{R})=0$ holds for any abelian group $A$, and therefore [Proposition 3](#prop3) gives the following isomorphism

$$H^k(X;\mathbb{R})\cong \Hom_\mathbb{Z}(H_k(X),\mathbb{R})$$

Then examining such types of homology and cohomology would be another interest. For this purpose, recalling the chain complexes used to define $H_k(X;A)$ and $H^k(X;A)$, we know that the two chain complexes

$$C_\bullet(X;A):=C_\bullet(X)\otimes_\mathbb{Z}A,\qquad C_\bullet^\Delta(X;A):=C_\bullet^\Delta(X)\otimes_\mathbb{Z}A$$

are chain complexes of $A$-modules if $A$ were a ring, and the $C^\bullet(X;A)$ defined earlier is also such. Therefore, taking homology or cohomology of these will also yield $A$-modules as results.

On the other hand, we know that if $A$ is a principal ideal domain, then any submodule of a free $A$-module is again a free $A$-module. Looking back at the proof of [Proposition 1](#prop1), we utilized the fact that since $\mathbb{Z}$ is a principal ideal domain, a submodule of a free $\mathbb{Z}$-module (i.e., free abelian group) is again a free $\mathbb{Z}$-module. Based on this, we can generalize the previous two propositions as follows.

<div class="proposition" markdown="1">

<ins id="thm4">**Theorem 4 (Universal coefficient theorem for homology, general version)**</ins> For a principal ideal domain $A$, a chain complex $C_\bullet$ of free $A$-modules, and an arbitrary $A$-module $M$, the following short exact sequence

$$0 \rightarrow H_k(C)\otimes_AM\rightarrow H_k(C\otimes_AM)\rightarrow \Tor_1^A(H_{k-1}(C), A)\rightarrow 0$$

exists. Moreover, this sequence splits (non-canonically) and therefore gives the following (non-canonical) isomorphism

$$H_k(C\otimes_AM)\cong \left(H_k(C)\otimes_AM\right)\oplus \Tor_1^A(H_{k-1}(C), M)$$

</div>

<div class="proposition" markdown="1">

<ins id="thm65">**Theorem 5 (Universal coefficient theorem for cohomology, general version)**</ins> For a principal ideal domain $A$, a chain complex $C_\bullet$ of free $A$-modules, and an arbitrary $A$-module $M$, the following short exact sequence

$$0\rightarrow\Ext_A^1(H_{k-1}(C), M)\rightarrow H_k(\Hom_A(C,M))\rightarrow \Hom_A(H_k(C),M)\rightarrow 0$$

exists. Moreover, this sequence splits (non-canonically) and therefore gives the following (non-canonical) isomorphism

$$H_k(\Hom_A(C,M))\cong \Hom_A(H_k(C),M)\oplus \Ext^1_A(H_{k-1}(C),M)$$

</div>

## Mayer-Vietoris Sequence

Among the axioms in [Definition 2](#thm2), the excision axiom allows us to compute the cohomology of a large space from the cohomology of smaller spaces. The following proposition is the cohomology version of [[Algebraic Topology] §Computation of Homology, ⁋Proposition 7](/en/math/algebraic_topology/computation_of_homology#prop7), and its proof can be obtained by repeating the process of deriving [[Algebraic Topology] §Computation of Homology, ⁋Proposition 7](/en/math/algebraic_topology/computation_of_homology#prop7) from [[Algebraic Topology] §Computation of Homology, ⁋Definition 6](/en/math/algebraic_topology/computation_of_homology#def6), starting from [Definition 2](#thm2).

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6 (Mayer-Vietoris sequence)**</ins> Suppose a topological space $X$ can be expressed as a union of two open sets $X=U\cap V$, and consider a cohomology theory $H$ defined on it. Then the long exact sequence

$$\cdots \to H^{n}(X) \xrightarrow{(i^*, j^*)} H^{n}(U) \oplus H^{n}(V) \xrightarrow{k^* - l^*} H^{n}(U \cap V) \xrightarrow{\delta} H^{n+1}(X) \to \cdots$$

exists, where $i^\ast, j^\ast, k^\ast, l^\ast$ are the maps induced by the inclusions

$$i:U\rightarrow X,\quad j:V\rightarrow X,\quad k:U\cap V\rightarrow U,\quad l:U\cap V \rightarrow V$$

respectively.

</div>

## Tensor Product of Chain Complexes

Using the Mayer-Vietoris sequence, we can compute the homology or cohomology of a large space from the homology or cohomology of its small subspaces. On the other hand, we can also multiply two spaces $X,Y$ to create a larger space $X\times Y$, and the Künneth formula helps compute the homology and cohomology of such product spaces. For this, we first need to define the tensor product of two given chain complexes $C_\bullet$ and $D_\bullet$.

<div class="definition" markdown="1">

<ins id="def7">**Definition 7**</ins> Let $A$ be a ring and let $C_\bullet,D_\bullet$ be chain complexes of $A$-modules. Their *tensor product* $(C\otimes D)_\bullet$ is defined for each $k$ as

$$(C\otimes D)_k=\bigoplus_{p+q=k}C_p\otimes_A D_q$$

and the differential is defined on homogeneous elements as

$$\partial(x,y)=(\partial^Cx,y)+(-1)^{\deg(x)}(x,\partial^Dy)$$

and then extended linearly.

</div>

In other words, $(C\otimes D)_\bullet$ can be described as the total complex of a double complex whose $(p,q)$ component is $C_p\otimes D_q$, with horizontal differential $\partial^C\otimes\id_D$ and vertical differential $\id_C\otimes \partial^D$. ([##ref##](total_complex))

The algebraic content of the Künneth formula is contained in the following lemma.

<div class="proposition" markdown="1">

<ins id="lem8">**Lemma 8**</ins> Let $A$ be a principal ideal domain and let $C_\bullet$, $D_\bullet$ be chain complexes of $A$-modules, with $C_\bullet$ being a chain complex of free $A$-modules. Then for any $k$, the following short exact sequence

$$0 \rightarrow \bigoplus_{p+q=k}H_p(C)\otimes_AH_q(D)\rightarrow H_k(C\otimes D)\rightarrow \bigoplus_{p+q=k-1}\Tor_1^A(H_p(C),H_q(D))\rightarrow 0$$

exists. Moreover, this short exact sequence splits (non-canonically) and therefore the following isomorphism

$$H_k(C\otimes D)\cong \left( \bigoplus_{p+q=k}H_p(C)\otimes_AH_q(D)\right)\oplus \left(\bigoplus_{p+q=k-1}\Tor_1^A(H_p(C),H_q(D)) \right)$$

exists.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, consider the following short exact sequence

$$0 \rightarrow Z_p(C) \rightarrow C_p\rightarrow B_{p-1}(C)\rightarrow 0$$

Since $B_{p-1}(C)$ and $Z_p(C)$ are submodules of the free $A$-modules $C_{p-1},C_p$ and $A$ is a principal ideal domain, they are again free $A$-modules. Therefore, the following short exact sequence obtained by tensoring $D_q$ with this short exact sequence

$$0\rightarrow Z_p(C)\otimes D_q \rightarrow C_p\otimes D_q \rightarrow B_{p-1}(C)\otimes D_q\rightarrow 0$$

exists. From the definition of the chain complex $(C\otimes D)_\bullet$, considering such short exact sequences for all $(p,q)$ satisfying $p+q=k$ and then taking the direct sum of all of them yields the following short exact sequence

$$0 \rightarrow (Z(C)\otimes D)_k \rightarrow (C\otimes D)_k \rightarrow (B(C)\otimes D)_{k-1}\rightarrow 0$$

Now, considering the long exact sequence of homologies from this short exact sequence, we obtain

$$\cdots \rightarrow H_{k}(B(C)\otimes D)\overset{\delta_k}{\longrightarrow} H_{k}(Z(C)\otimes D)\rightarrow H_{k}(C\otimes D)\rightarrow H_{k-1}(B(C)\otimes D)\overset{\delta_{k-1}}{\longrightarrow} H_{k-1}(Z(C)\otimes D)\rightarrow \cdots$$

In particular, with $H_k(C\otimes D)$ as the reference point, we obtain the following short exact sequence

$$0 \rightarrow \coker\delta_k\rightarrow H_k(C\otimes D)\rightarrow \ker\delta_{k-1}\rightarrow 0 \tag{$\ast$}$$

Now, to examine $\coker\delta_k$ and $\ker\delta_{k-1}$, consider the short exact sequence

$$0 \rightarrow B_\bullet(C)\rightarrow Z_\bullet(C)\rightarrow H_\bullet(C)\rightarrow 0$$

and consider the following exact sequence obtained by tensoring with $H_\bullet(D)$

$$0 \rightarrow \Tor_1^A(H(C), H(D))_\bullet\rightarrow (B(C)\otimes H(D))_\bullet\rightarrow (Z(C) \otimes H(D))_\bullet \rightarrow (H(C)\otimes H(D))_\bullet \rightarrow 0$$

Here, the $0$ in the first term comes from the fact that $Z_\bullet(C)$ consists of free modules. On the other hand, since free modules are flat, taking the tensor product with a free module commutes with taking homology, and therefore in the above sequence we know that

$$(B(C)\otimes H(D))_\bullet\cong H_\bullet(B(C)\otimes D)\qquad (Z(C)\otimes H(D))_\bullet \cong H_\bullet(Z(C)\otimes D)$$

At this point, $(B(C)\otimes H(D))_\bullet \rightarrow (Z(C)\otimes H(D))_\bullet$ is obtained from the inclusion $B_\bullet(C)\rightarrow Z_\bullet(C)$, and through the above identification, we know it is the same map as $\delta_\bullet$. Therefore

$$\coker \delta_k\cong (H(C)\otimes H(D))_k,\qquad \ker \delta_{k-1}\cong \Tor_1^A(H(C),H(D))_{k-1}$$

are obtained. For the claim about splitting, since

$$0 \rightarrow Z_\bullet(C)\rightarrow C_\bullet \rightarrow B_{\bullet-1}(C) \rightarrow 0$$

is a split exact sequence, a splitting of ($\ast$) is induced by a section $B_{\bullet-1}(C)\rightarrow C_\bullet$.

</details>

## Eilenberg-Zilber Theorem and Künneth Formula

Keeping the result of [Lemma 8](#lem8) in mind, what we need to do is clear. When two topological spaces $X,Y$ and their corresponding chain complexes $C_\bullet(X),C_\bullet(Y)$ are given, we need to examine the relationship between the homology $H_\bullet(X\times Y)$ of the product space $X\times Y$ and the tensor product $(H(X)\otimes H(Y))_\bullet$ of the two chain complexes $H_\bullet(X)$ and $H_\bullet(Y)$. The following theorem shows that these two algebraic objects are identical.

<div class="proposition" markdown="1">

<ins id="thm9">**Theorem 9 (Eilenberg-Zilber)**</ins> For two topological spaces $X,Y$ and the chain complexes $C_\bullet(X),C_\bullet(Y)$ obtained from them, and $C_\bullet(X\times Y)$, there exists a chain homotopy equivalence between the two chain complexes $(C(X)\otimes C(Y))_\bullet$ and $C_\bullet(X\times Y)$, and therefore

$$H_\bullet(C(X\times Y))\cong H_\bullet(C(X)\otimes C(Y))$$

holds.

</div>

This is typically proved using the [acyclic models theorem](https://en.wikipedia.org/wiki/Acyclic_model), but the acyclic models theorem is in fact a theorem that is closer to being a generalization of the Eilenberg-Zilber theorem, so proving it using the acyclic models theorem is somewhat excessive. However, directly proving the Eilenberg-Zilber theorem is a rather tedious task, so we will only examine the two maps

$$\AW:C_\bullet(X\times Y) \rightarrow (C(X)\otimes C(Y))_\bullet,\qquad \EZ:(C(X)\otimes C(Y))_\bullet \rightarrow C_\bullet(X\times Y)$$

that appear in this proof process. The proof using the acyclic models theorem will be written in a separate article to avoid disrupting the flow.

First, for the Alexander-Whitney map $\AW:C_\bullet(X\times Y) \rightarrow (C(X)\otimes C(Y))_\bullet$, any $k$-simplex $\sigma:\Delta^k \rightarrow X\times Y$ is sent to

$$\sum_p (\pi_X\circ \sigma\vert_{[v_0,\ldots,v_p]})\otimes (\pi_Y\circ \sigma\vert_{[v_p,\ldots v_k]})\in \bigoplus_{p+q=k}C_p(X)\otimes C_q(Y)$$

If $X=Y$, this would be a map $C(X)\rightarrow C(X)\otimes C(X)$ that makes $C(X)$ into a (differential graded counital coassociative) coalgebra, and for this reason it will appear again in the next article.

The Eilenberg-Zilber map $\EZ:(C(X)\otimes C(Y))_\bullet \rightarrow C_\bullet(X\times Y)$ is defined for simple tensors by the formula

$$\EZ(\sigma\otimes\tau)=\sum_{\substack{\alpha_1<\cdots <\alpha_p\\\beta_1<\cdots <\beta_q}}\sgn(\alpha_1,\ldots,\alpha_p,\beta_1,\ldots,\beta_q)(\sigma\circ s_{\alpha_p}\cdots s_{\alpha_1})\times(\tau\circ s_{\beta_q}\cdots s_{\beta_1})$$

which looks complicated as a formula, but it simply represents the method of decomposing the prism $\Delta^p\times \Delta^q$ into simplices, as in the $h_n$ map that appeared in the proof of [§Homotopy, ⁋Proposition 6](/en/math/algebraic_topology/homotopy#prop6). Then the result of [Theorem 9](#thm9) follows from the two equations

$$\AW\circ\EZ=\id_{(C(X)\otimes C(Y))_\bullet},\qquad \EZ\circ \AW\simeq \id_{C_\bullet(X\times Y)}$$

Therefore, combining [Lemma 8](#lem8) with [Theorem 9](#thm9) yields the following result.

<div class="proposition" markdown="1">

<ins id="cor10">**Corollary 10 (Künneth)**</ins> Fix topological spaces $X,Y$. Then for their product space $X\times Y$ and a principal ideal domain $A$, the following short exact sequence

$$0 \rightarrow \bigoplus_{p+q=k}H_p(X;A)\otimes_AH_q(Y;A)\rightarrow H_k(X\times Y;A)\rightarrow \bigoplus_{p+q=k-1}\Tor_1^A(H_p(X;A),H_q(Y;A))\rightarrow 0$$

exists. Moreover, this short exact sequence splits (non-canonically) and therefore the following isomorphism

$$H_k(X\times Y;A)\cong \left( \bigoplus_{p+q=k}H_p(X;A)\otimes_AH_q(Y;A)\right)\oplus \left(\bigoplus_{p+q=k-1}\Tor_1^A(H_p(X;A),H_q(Y;A)) \right)$$

exists.

</div>

Of course, using this result together with [Theorem 5](#thm5), we can obtain the cohomology version of the Künneth formula.

--- 

**References**

[Hat] A. Hatcher, *Algebraic Topology*. Cambridge University Press, 2022.  
[May] J. P. May, *A concise course in algebraic topology*.

---

[^1]: Of course, we would want this pairing to give a homomorphism from $H^k(X;A)$ to $\Hom(H_k(X),A)$, but the situation is not this simple, and we know from [Proposition 3](#prop3) that an $\Ext$ term containing hidden torsion must appear.
