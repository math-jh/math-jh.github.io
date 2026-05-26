---
title: "Representation Theory of Finite Groups"
excerpt: "Definition of representations of finite groups and irreducible decomposition"

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
translated_at: 2026-05-26T21:30:02+00:00
translation_source: kimi-cli
---
One good strategy for dealing with a mathematical object whose structure is complicated is to see how it acts on other, simpler objects. In this category we study representation theory, and in particular the representation theory of finite groups.

## Basic Concepts of Representation Theory

Let us begin with the following definition.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> For an arbitrary finite group $$G$$, a *representation* of $$G$$ is given by a finite-dimensional vector space $$V$$ and a function

$$\rho: G\times V \rightarrow V$$

satisfying the conditions of a group action such that each $$\rho(g,-)$$ is a linear map.

</div>

In general the ground field $$\mathbb{K}$$ could be replaced by an arbitrary ring $$A$$ without any problem, but for our discussion it suffices to fix $$\mathbb{K}=\mathbb{C}$$. Also, keep in mind that we mainly consider the case where $$V$$ is a *finite-dimensional* vector space as the representation space. This too can be generalized to infinite-dimensional vector spaces, but for that one needs standard methods such as endowing $$V$$ with a topological vector space structure.

The above definition can be thought of briefly as a given map $$G\rightarrow\Aut(V)$$. By a slight abuse of notation we sometimes write $$\rho(g,-): V\rightarrow V$$ simply as $$\rho(g)\in \Aut(V)$$, and further abbreviate the notation by writing $$g\cdot v$$ instead of $$\rho(g)v$$. As this notation suggests, we think of $$V$$ as a $$G$$-module, and from this point of view (with scalar multiplication implicitly given) we simply call $$V$$ a representation of $$G$$.

Fix a finite group $$G$$, and suppose two representations $$V,W$$ are given. Then a *morphism* from $$V$$ to $$W$$ is given by the following diagram:

![G-equivariant_maps](/assets/images/Math/Representation_Theory/Representations_of_Finite_Groups-1.png){:style="width:10em" class="invert" .align-center}

In formula, this can simply be written as

$$L(g\cdot v)=g\cdot L(v)\qquad\text{for all $g\in G$ and $v\in V$}$$

On the other hand, borrowing the language of linear algebra applied to $$V$$, we can make the following definition.

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> For a representation $$G\times V\rightarrow V$$ of a group $$G$$, we define the following.

1. A subspace $$W$$ of $$V$$ is called *$$G$$-invariant* if for every $$g\in G$$ and every $$w\in W$$, we always have $$g\cdot w\in W$$.
2. For any $$G$$-invariant subspace $$W$$, the representation $$G\times W\rightarrow W$$ is called a *subrepresentation* of $$V$$.
3. If $$V$$ is not the zero representation and the only subrepresentations of $$V$$ are the trivial ones, namely itself and $$G\times\{0\}\rightarrow\{0\}$$, then $$V$$ is called an *irreducible representation*.

</div>

From the same point of view we can define, for arbitrary representations $$V,W$$, the objects $$V\oplus W$$, $$V\otimes W$$, etc., using the operations on their underlying vector spaces. One thing to be slightly careful about in the next definition is that, unlike in [Definition 2](#def2) above, there may not be a *natural* $$G$$-action on $$V\otimes W$$, etc.; therefore we explicitly define a $$G$$-action on each vector space.

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> For $$G$$-representations $$V, W$$, we define new $$G$$-representations via the following $$G$$-actions.

1. Direct sum $$V\oplus W$$; $$G$$-action $$g\cdot(v,w)=(g\cdot v,g\cdot w)$$
2. Tensor product $$V\otimes W$$; $$G$$-action $$g\cdot(v\otimes w)=(g\cdot v)\otimes (g\cdot w)$$, and from this the exterior power $$\bigwedge^k V$$, symmetric power $$\operatorname{Sym}^k V$$, and the $$G$$-actions on them
3. $$\Hom_\mathbb{C}(V,W)$$; $$G$$-action $$(g\cdot f)(v)=g\cdot f(g^{-1}\cdot v)$$
4. The *dual representation* $$V^\ast$$ obtained from 3 by setting $$W=\mathbb{C}$$
5. The *conjugate representation* $$\overline{V}$$ obtained by replacing scalar multiplication with its conjugate (same $$G$$-action)

</div>

## Category $$\lMod{\mathbb{C}[G]}$$

In [Definition 3] above, the definitions of tensor product and $$\Hom$$ may look somewhat artificial; to investigate this, the language of group algebras is useful. ([\[Algebraic Structures\] §Algebras, ⁋Definition 5](/en/math/algebraic_structures/algebras#def5)) To briefly review, as a set $$\mathbb{C}[G]$$ was the collection of functions from $$G$$ to $$\mathbb{C}$$. For each $$x\in G$$, defining $$\delta_x:G\rightarrow \mathbb{C}$$ by

$$\delta_x(y)=\begin{cases}1&\text{if $y=x$}\\0&\text{otherwise}\end{cases}$$

any $$\varphi\in\mathbb{C}[G]$$ can be written as

$$\phi=\sum_{x\in G}\phi(x)\delta_x$$

so the $$\delta_x$$ form a basis of $$\mathbb{C}[G]$$. The part where $$\mathbb{C}[G]$$ is not simply the ring of functions from $$G$$ to $$\mathbb{C}$$ lies in the multiplication defined on it. Instead of defining the product of two functions $$\phi,\psi$$ by

$$(\phi\psi)(x)=\phi(x)\psi(x), \qquad \text{for all $x\in G$}$$

multiplication on this space is given by the convolution product

$$(\phi\ast \psi)(x)=\sum_{y\in G}\phi(y)\psi(y^{-1}x)$$

If we identify the delta function $$\delta_x$$ with $$x\in G$$, then the identity

$$\left(\sum_{x\in G}\phi(x)\cdot x\right)\left(\sum_{y\in G} \psi(y)\cdot y\right)=\sum_{x,y\in G} \phi(x)\psi(y) \cdot(xy)=\sum_{z\in G}\left(\sum_{x\in G} \phi(x)\psi(x^{-1}z)\right)\cdot z$$

holds, so this choice of multiplication is natural. For example, the product of $$\delta_x$$ and $$\delta_y$$ is $$0$$, but their convolution is $$\delta_{xy}$$; for expressions such as

$$(\delta_x\ast \delta_y)\cdot v=\delta_x\cdot(\delta_y\ast v)$$

which are involved in the group action to make sense, this choice is inevitable.

For any $$G$$-representation $$\rho:G\rightarrow \Aut(V)$$, the formula

$$\widetilde{\rho}\left(\sum_{x\in G} \phi_x x, v\right)= \sum_{x\in G} \phi_x\rho(x)v$$

gives a $$\mathbb{C}[G]$$-module structure on $$V$$. Conversely, given any $$\mathbb{C}[G]$$-module $$V$$, we can obtain a $$G$$-representation by the way each $$x\in G$$ acts on $$V$$.

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4**</ins> The above correspondences give a categorical equivalence

$$\Rep_\mathbb{C}(G)\cong \lMod{\mathbb{C}[G]}$$

</div>

That is, what we called a $$G$$-module can be thought of, strictly speaking, as looking only at the action coming from $$G\hookrightarrow \mathbb{C}[G]$$ in a $$\mathbb{C}[G]$$-module structure.

In fact, most of what we discussed above can be explained by this categorical equivalence. For example, for any $$G$$-representation $$V$$, a subrepresentation of $$V$$ is a $$G$$-submodule of $$V$$ (more precisely, a $$\mathbb{C}[G]$$-submodule). Also, the tensor product in [Definition 3](#def3) is plausible: in general, for a $$\mathbb{K}$$-algebra $$A$$ with a given coproduct $$\Delta:A\rightarrow A\otimes A$$ and two $$A$$-modules $$M,N$$, to define their tensor product one must use $$\Delta$$ via

$$A\otimes (M\otimes N)\rightarrow (A\otimes A)\otimes (M\otimes N)\rightarrow (A\otimes M)\otimes (A\otimes N)\rightarrow M\otimes N$$

and the coproduct $$A\rightarrow A\otimes A$$ used here, in the case of $$\mathbb{C}[G]$$, is

$$\mathbb{C}[G]\rightarrow \mathbb{C}[G]\otimes \mathbb{C}[G]$$

Likewise, the $$\Hom$$ defined in [Definition 3](#def3) is adjoint to this $$\otimes$$, and for this reason the somewhat artificial-looking $$G$$-actions in [Definition 3](#def3) appear.

In particular, since subrepresentations of $$G$$ and $$\mathbb{C}[G]$$-submodules are the same thing, $$V$$ being an irreducible representation is equivalent to $$V$$ being a *simple* $$\mathbb{C}[G]$$-module.

## Maschke's Theorem

We have now roughly surveyed the basic concepts needed for representations of finite groups. Before beginning the main story, for an arbitrary representation $$V$$ consider the following subspace:

$$V^G=\{v\in V\mid g\cdot v=v\text{ for all $g\in G$}\}$$

This space is the space of vectors fixed by the $$G$$-action; although it is also a $$G$$-invariant space, what we want to observe is that the obvious projection map

$$p: V\rightarrow V^G;\qquad v\mapsto \frac{1}{\lvert G\rvert}\sum_{g\in G}g\cdot v$$

exists. In particular, the idea contained in this projection map — namely, the idea of averaging over all actions of $$G$$ to obtain a $$G$$-invariant object — is used importantly.

<div class="definition" markdown="1">

<ins id="def5">**Definition 5**</ins> A Hermitian inner product $$\langle-,-\rangle$$ on a $$G$$-representation $$V$$ is called *$$G$$-invariant* if for every $$g\in G$$ and $$u,v\in V$$,

$$\langle g\cdot u,g\cdot v\rangle=\langle u,v\rangle$$

holds. A representation possessing a $$G$$-invariant inner product is called a *unitary representation*.

</div>

If such a $$G$$-invariant inner product is given, then for every $$g\in G$$, $$\rho(g)\in \Aut(V)$$ is a unitary operator. To see this, suppose a $$G$$-invariant inner product $$\langle -,-\rangle$$ is given; then for every $$g\in G$$,

$$\langle v,w\rangle=\langle \rho(g) v,\rho(g) w\rangle=\langle \rho(g)^\dagger \rho(g)v,w\rangle$$

holds for all $$v,w\in V$$.

On the other hand, a finite-dimensional $$G$$-module $$V$$ admits a $$G$$-invariant inner product. This can be proved using the idea mentioned above.

<div class="proposition" markdown="1">
 
<ins id="prop6">**Proposition 6**</ins> Every representation $$V$$ admits a $$G$$-invariant inner product. That is, every representation is a unitary representation.
 
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

<ins id="cor7">**Corollary 7 (Maschke)**</ins> For any finite-dimensional $$G$$-representation $$V$$ and $$G$$-invariant subspace $$W$$, there exists a suitable $$G$$-invariant subspace $$W'$$ such that $$V = W \oplus W'$$. Therefore, inductively, any finite-dimensional $$G$$-representation decomposes as a direct sum of irreducible representations.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Taking $$W'$$ to be the orthogonal complement of $$W$$, then $$W'$$ is also a $$G$$-invariant subspace and $$V = W \oplus W'$$ holds.

</details>

Earlier we examined the categorical equivalence

$$\Rep_\mathbb{C}(G)\cong \lMod{\mathbb{C}[G]}$$

Then what [Corollary 7](#cor7) asserts is that any finite-dimensional $$G$$-representation $$V$$ is always a *semisimple* $$\mathbb{C}[G]$$-module. Therefore $$\mathbb{C}[G]$$ itself becomes an Artinian semisimple ring ([semisimple](##ref##)), and hence by the Artin-Wedderburn theorem ([artin-wedderburn](##ref##)) we know that a decomposition into simple modules

$$\mathbb{C}[G]\cong \bigoplus_{i=1}^r \Mat_{n_i}(\mathbb{C})\tag{1}$$

exists.

## Schur Orthogonality

In the next post we give a representation-theoretic meaning to the decomposition (1). As preparation for this, we prove the following lemma.

<div class="proposition" markdown="1">

<ins id="lem8">**Lemma 8 (Schur)**</ins> Let a (compact) group $$G$$ and irreducible $$G$$-modules $$V,W$$ be given. Then the following hold.

1. Any $$G$$-map $$V\rightarrow W$$ is either the zero map or an isomorphism.
2. Any $$G$$-automorphism $$f\in \Aut_G(V)$$ is of the form $$f(v)=\lambda v$$.
3. The space of $$G$$-maps $$\Hom_G(V,W)$$ is either $$\mathbb{C}$$ or $$0$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

1. This is obvious by considering the kernel and image.
2. The given $$f$$ is a $$\mathbb{C}$$-linear map before being a $$G$$-linear map, so $$f$$ has an eigenvalue $$\lambda$$. Now let $$W$$ be the eigenspace corresponding to this eigenvalue; it suffices to show that this is in fact a $$G$$-submodule.
3. This is obvious from the two propositions above.

</details>

Using this we obtain the following proposition.

<div class="proposition" markdown="1">

<ins id="prop9">**Proposition 9**</ins> In the same situation as above, the function

$$d=\bigoplus_{W\in\Irr(G, \mathbb{C})} d_W:\bigoplus_{W\in \Irr(G, \mathbb{C})}\Hom_G(W,V)\otimes_\mathbb{C}W\rightarrow V$$

is an isomorphism.

</div>

The proof of this is obvious from the identity

$$\Hom_G(W, V)=\Hom_G\left(W, \bigoplus V_j\right)\cong \bigoplus \Hom_G(W, V_j) $$

and [Lemma 8](#lem8), since $$V$$ has an irreducible decomposition $$V=\bigoplus V_j$$. That is, although we have written it in a complicated way, the above $$d$$ simply counts how many copies of each irreducible $$G$$-module $$W$$ (or rather, its isomorphism class) appear inside $$V$$; therefore the following definition is natural.

<div class="definition" markdown="1">

<ins id="def10">**Definition 10**</ins> The image of $$W\in\Irr(G, \mathbb{C})$$ under the above function is called the *$$W$$-isotypical summand* of $$V$$, and $$\Hom_G(W, V)$$ is called the *multiplicity* of $$W$$.

</div>

With a small leap of faith, one can also be convinced that such a decomposition is unique. That is, we know that any representation $$V$$ can be written in the form of the decomposition

$$V=V_1^{\oplus r_1}\oplus\cdots\oplus V_k^{\oplus r_k}$$
