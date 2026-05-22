---
title: "Representation Theory of Finite Groups"
excerpt: "Definition of finite group representations and irreducible decomposition"

categories: [Math / Representation Theory]
permalink: /en/math/representation_theory/representations_of_finite_groups
header:
    overlay_image: /assets/images/Math/Representation_Theory/Representations_of_Finite_Groups.png
    overlay_filter: 0.5
sidebar: 
    nav: "representation_theory-en"

date: 2026-02-13
last_modified_at: 2026-02-13
weight: 1
translated_at: 2026-05-22T08:00:01+00:00
translation_source: kimi-cli
---
In general, when dealing with mathematical objects having complicated structure, one good strategy is to observe how the object acts on other, simpler objects. In this category we study representation theory, and in particular the representation theory of finite groups.

## Basic Concepts of Representation Theory

Let us begin with the following definition.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> For an arbitrary finite group $$G$$, a *representation* of $$G$$ consists of a finite-dimensional vector space $$V$$ and a function

$$\rho: G\times V \rightarrow V$$

satisfying the conditions of a group action, such that each $$\rho(g,-)$$ is a linear map.

</div>

In general, there is no problem replacing the ground field $$\mathbb{K}$$ with an arbitrary ring $$A$$, but for our purposes it is enough to fix $$\mathbb{K}=\mathbb{C}$$. Also, recall that we will mainly consider the case where the representation space $$V$$ is *finite-dimensional*. This too can be generalized to infinite-dimensional vector spaces, but doing so requires standard methods such as equipping $$V$$ with a topological vector space structure.

Briefly, the above definition can be thought of as giving a map $$G\rightarrow\Aut(V)$$. By a slight abuse of notation, we sometimes write $$\rho(g,-): V\rightarrow V$$ simply as $$\rho(g)\in \Aut(V)$$, and abbreviate further by writing $$g\cdot v$$ instead of $$\rho(g)v$$. As this notation suggests, we think of $$V$$ as a $$G$$-module, and from this perspective (scalar multiplication being implicitly understood) we also simply call $$V$$ a representation of $$G$$.

Fix a finite group $$G$$, and suppose two representations $$V,W$$ are given. Then a *morphism* from $$V$$ to $$W$$ is given by the following diagram

![G-equivariant_maps](/assets/images/Math/Representation_Theory/Representations_of_Finite_Groups-1.png){:style="width:10em" class="invert" .align-center}

In terms of equations, this can simply be written as

$$L(g\cdot v)=g\cdot L(v)\qquad\text{for all $g\in G$ and $v\in V$}$$

Meanwhile, borrowing the language of linear algebra as applied to $$V$$, we can define the following.

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> For a representation $$G\times V\rightarrow V$$ of a group $$G$$, we define the following.

1. A subspace $$W$$ of $$V$$ is called *$$G$$-invariant* if for every $$g\in G$$ and every $$w\in W$$, we always have $$g\cdot w\in W$$.
2. For any $$G$$-invariant subspace $$W$$, the representation $$G\times W\rightarrow W$$ is called a *subrepresentation* of $$V$$.
3. If $$V$$ is not the zero representation and its only subrepresentations are the trivial ones, namely $$V$$ itself and $$G\times\{0\}\rightarrow\{0\}$$, then $$V$$ is called an *irreducible representation*.

</div>

From the same perspective, for arbitrary representations $$V,W$$, we can define $$V\oplus W$$, $$V\otimes W$$, etc., using the operations on their underlying vector spaces. One subtle point in the following definition is that, unlike [Definition 2](#def2) above, there may not be a natural $$G$$-action on $$V\otimes W$$, etc.; therefore we explicitly define a $$G$$-action on each vector space.

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> For $$G$$-representations $$V, W$$, we define new $$G$$-representations via the following $$G$$-actions.

1. Direct sum $$V\oplus W$$; $$G$$-action $$g\cdot(v,w)=(g\cdot v,g\cdot w)$$
2. Tensor product $$V\otimes W$$; $$G$$-action $$g\cdot(v\otimes w)=(g\cdot v)\otimes (g\cdot w)$$, and from this the exterior powers $$\bigwedge^k V$$, symmetric powers $$\operatorname{Sym}^k V$$ and the $$G$$-actions on them
3. $$\Hom_\mathbb{C}(V,W)$$; $$G$$-action $$(g\cdot f)(v)=g\cdot f(g^{-1}\cdot v)$$
4. The *dual representation* $$V^\ast$$ obtained from 3 by setting $$W=\mathbb{C}$$
5. The *conjugate representation* $$\overline{V}$$ obtained by replacing scalar multiplication with its conjugate (the same $$G$$-action)

</div>

## Category $$\lMod{\mathbb{C}[G]}$$

In [Definition 3](#def3), the definitions of the tensor product and $$\Hom$$ may seem somewhat artificial; to investigate why, the language of group algebras is useful. ([\[Algebraic Structures\] §Algebras, ⁋Definition 5](/en/math/algebraic_structures/algebras#def5)) To briefly review, as a set $$\mathbb{C}[G]$$ is the collection of functions from $$G$$ to $$\mathbb{C}$$. If for each $$x\in G$$ we define $$\delta_x:G\rightarrow \mathbb{C}$$ by

$$\delta_x(y)=\begin{cases}1&\text{if $y=x$}\\0&\text{otherwise}\end{cases}$$

then any $$\varphi\in\mathbb{C}[G]$$ can be written as

$$\phi=\sum_{x\in G}\phi(x)\delta_x$$

so the $$\delta_x$$'s form a basis of $$\mathbb{C}[G]$$. What distinguishes the $$\mathbb{C}[G]$$ we consider from the mere ring of functions from $$G$$ to $$\mathbb{C}$$ is the multiplication defined on it. Instead of defining the product of two functions $$\phi,\psi$$ by

$$(\phi\psi)(x)=\phi(x)\psi(x), \qquad \text{for all $x\in G$}$$

we define multiplication on it by the convolution product

$$(\phi\ast \psi)(x)=\sum_{y\in G}\phi(y)\psi(y^{-1}x)$$

If we identify the above delta functions $$\delta_x$$ with the elements $$x\in G$$, then the formula

$$\left(\sum_{x\in G}\phi(x)\cdot x\right)\left(\sum_{y\in G} \psi(y)\cdot y\right)=\sum_{x,y\in G} \phi(x)\psi(y) \cdot(xy)=\sum_{z\in G}\left(\sum_{x\in G} \phi(x)\psi(x^{-1}z)\right)\cdot z$$

holds, so this choice of multiplication is natural. For example, the product of $$\delta_x$$ and $$\delta_y$$ is $$0$$, but their convolution is $$\delta_{xy}$$; therefore, in order for expressions such as

$$(\delta_x\ast \delta_y)\cdot v=\delta_x\cdot(\delta_y\ast v)$$

which are part of the group action, to make sense, this choice is inevitable.

For any $$G$$-representation $$\rho:G\rightarrow \Aut(V)$$, the formula

$$\widetilde{\rho}\left(\sum_{x\in G} \phi_x x, v\right)= \sum_{x\in G} \phi_x\rho(x)v$$

gives a $$\mathbb{C}[G]$$-module structure on $$V$$. Conversely, given any $$\mathbb{C}[G]$$-module $$V$$, we obtain a $$G$$-representation via the action of each $$x\in G$$ on $$V$$.

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4**</ins> The above correspondences give rise to a categorical equivalence

$$\Rep_\mathbb{C}(G)\cong \lMod{\mathbb{C}[G]}$$

</div>

In other words, what we have been calling a $$G$$-module can be thought of, strictly speaking, as merely observing the action coming from the inclusion $$G\hookrightarrow \mathbb{C}[G]$$ in the $$\mathbb{C}[G]$$-module structure.

In fact, most of what we discussed above can be explained through this categorical equivalence. For example, for any $$G$$-representation $$V$$, a subrepresentation of $$V$$ is a $$G$$-submodule of $$V$$ (more precisely, a $$\mathbb{C}[G]$$-submodule). Also, the tensor product in [Definition 3](#def3) is plausible, because in general, for a $$\mathbb{K}$$-algebra $$A$$ equipped with a coproduct $$\Delta:A\rightarrow A\otimes A$$ and two $$A$$-modules $$M,N$$, to define their tensor product one must use $$\Delta$$ via

$$A\otimes (M\otimes N)\rightarrow (A\otimes A)\otimes (M\otimes N)\rightarrow (A\otimes M)\otimes (A\otimes N)\rightarrow M\otimes N$$

and this is because the coproduct $$A\rightarrow A\otimes A$$ used here is, for $$\mathbb{C}[G]$$, the natural map

$$\mathbb{C}[G]\rightarrow \mathbb{C}[G]\otimes \mathbb{C}[G]$$

Then similarly, the $$\Hom$$ defined in [Definition 3](#def3) stands in an adjunction with this $$\otimes$$, and it is for this reason that the somewhat artificial-looking $$G$$-actions in [Definition 3](#def3) arise.

In particular, since subrepresentations of $$G$$ and $$\mathbb{C}[G]$$-submodules are the same thing, $$V$$ being an irreducible representation is equivalent to $$V$$ being a *simple* $$\mathbb{C}[G]$$-module.

## Maschke's Theorem

We have now roughly surveyed the basic concepts needed for representations of finite groups. Before diving into the main story, consider the following subspace

$$V^G=\{v\in V\mid g\cdot v=v\text{ for all $g\in G$}\}$$

for an arbitrary representation $$V$$. This space is the space of vectors fixed by the $$G$$-action; while it is also a $$G$$-invariant space, what we are more interested in observing is that the obvious projection map

$$p: V\rightarrow V^G;\qquad v\mapsto \frac{1}{\lvert G\rvert}\sum_{g\in G}g\cdot v$$

exists. In particular, the idea contained in this projection map — namely, the idea of summing over all actions of $$G$$ and then averaging to obtain a $$G$$-invariant object — is of great importance.

<div class="definition" markdown="1">

<ins id="def5">**Definition 5**</ins> A Hermitian inner product $$\langle-,-\rangle$$ on a $$G$$-representation $$V$$ is called *$$G$$-invariant* if for every $$g\in G$$ and $$u,v\in V$$,

$$\langle g\cdot u,g\cdot v\rangle=\langle u,v\rangle$$

holds. A representation possessing a $$G$$-invariant inner product is called a *unitary representation*.

</div>

If such a $$G$$-invariant inner product is given, then for any $$g\in G$$, $$\rho(g)\in \Aut(V)$$ is a unitary operator. To see this, suppose a $$G$$-invariant inner product $$\langle -,-\rangle$$ is given, and observe that for any $$g\in G$$,

$$\langle v,w\rangle=\langle \rho(g) v,\rho(g) w\rangle=\langle \rho(g)^\dagger \rho(g)v,w\rangle$$

holds for all $$v,w\in V$$.

On the other hand, any finite-dimensional $$G$$-module $$V$$ admits a $$G$$-invariant inner product. This can be proved using the averaging idea mentioned above.

<div class="proposition" markdown="1">
 
<ins id="prop6">**Proposition 6**</ins> Any representation $$V$$ possesses a $$G$$-invariant inner product. That is, any representation is a unitary representation.
 
</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

For any Hermitian inner product $$\langle -,- \rangle$$ on $$V$$, define a new inner product $$\langle\kern-1.5pt\langle-,-\rangle\kern-1.5pt\rangle$$ by

$$\langle\kern-1.5pt\langle u,v\rangle\kern-1.5pt\rangle = \frac{1}{|G|}\sum_{g \in G} \langle g\cdot u, g\cdot v \rangle$$

Then for any $$h\in G$$,

$$\langle\kern-1.5pt\langle h\cdot u, h\cdot v\rangle\kern-1.5pt\rangle = \frac{1}{|G|}\sum_{g \in G} \langle gh\cdot u, gh\cdot v \rangle = \langle\kern-1.5pt\langle u, v\rangle\kern-1.5pt\rangle$$

so this inner product is $$G$$-invariant.

</details>

At any rate, the central theorem of this section follows from the above proposition.

<div class="proposition" markdown="1">

<ins id="cor7">**Corollary 7 (Maschke)**</ins> For any finite-dimensional $$G$$-representation $$V$$ and any $$G$$-invariant subspace $$W$$, there exists a $$G$$-invariant subspace $$W'$$ such that $$V = W \oplus W'$$. Therefore, by induction, any finite-dimensional $$G$$-representation decomposes as a direct sum of irreducible representations.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Taking $$W'$$ to be the orthogonal complement of $$W$$, we see that $$W'$$ is also a $$G$$-invariant subspace and $$V = W \oplus W'$$ holds.

</details>

Earlier we examined the categorical equivalence

$$\Rep_\mathbb{C}(G)\cong \lMod{\mathbb{C}[G]}$$

Thus what [Corollary 7](#cor7) asserts is that any finite-dimensional $$G$$-representation $$V$$ is always a *semisimple* $$\mathbb{C}[G]$$-module. Therefore $$\mathbb{C}[G]$$ itself is an Artinian semisimple ring ([semisimple](##ref##)), and hence by the Artin-Wedderburn theorem ([artin-wedderburn](##ref##)), a decomposition into simple modules

$$\mathbb{C}[G]\cong \bigoplus_{i=1}^r \Mat_{n_i}(\mathbb{C})\tag{1}$$

exists.

## Schur Orthogonality

In the next post, we give representation-theoretic meaning to the decomposition (1). As preparation, we prove the following lemma.

<div class="proposition" markdown="1">

<ins id="lem8">**Lemma 8 (Schur)**</ins> Let $$G$$ be a (compact) group and let $$V,W$$ be irreducible $$G$$-modules. Then the following hold.

1. Any $$G$$-map $$V\rightarrow W$$ is either zero or an isomorphism.
2. Any $$G$$-automorphism $$f\in \Aut_G(V)$$ is of the form $$f(v)=\lambda v$$.
3. The space of $$G$$-maps $$\Hom_G(V,W)$$ is either $$\mathbb{C}$$ or $$0$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

1. This is obvious by considering the kernel and image.
2. Since the given $$f$$ is a $$\mathbb{C}$$-linear map to begin with, it has an eigenvalue $$\lambda$$. Now let $$W$$ be the eigenspace corresponding to this eigenvalue; then it suffices to show that this is in fact a $$G$$-submodule.
3. This is obvious from the two statements above.

</details>

Using this, we obtain the following proposition.

<div class="proposition" markdown="1">

<ins id="prop9">**Proposition 9**</ins> In the above situation, the map

$$d=\bigoplus_{W\in\Irr(G, \mathbb{C})} d_W:\bigoplus_{W\in \Irr(G, \mathbb{C})}\Hom_G(W,V)\otimes_\mathbb{C}W\rightarrow V$$

is an isomorphism.

</div>

The proof is obvious from the formula

$$\Hom_G(W, V)=\Hom_G\left(W, \bigoplus V_j\right)\cong \bigoplus \Hom_G(W, V_j) $$

and [Lemma 8](#lem8), since $$V$$ has an irreducible decomposition $$V=\bigoplus V_j$$. That is, although written in a complicated way, the above $$d$$ simply counts how many copies of each irreducible $$G$$-module $$W$$ (or rather, its isomorphism class) are contained in $$V$$, and therefore the following definition is natural.

<div class="definition" markdown="1">

<ins id="def10">**Definition 10**</ins> The image of $$W\in\Irr(G, \mathbb{C})$$ under the above map is called the *$$W$$-isotypical summand* of $$V$$, and $$\Hom_G(W, V)$$ is called the *multiplicity* of $$W$$.

</div>

With a little faith, one can also be convinced that such a decomposition is unique. That is, given any representation $$V$$, we know that it can be written in the form of a decomposition

$$V=V_1^{\oplus r_1}\oplus\cdots\oplus V_k^{\oplus r_k}$$
