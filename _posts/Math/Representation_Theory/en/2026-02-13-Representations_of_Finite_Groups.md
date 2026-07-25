---
title: "Representation Theory of Finite Groups"
description: "This post introduces the notion of a representation of a finite group via its action on a vector space, and covers the fundamental concepts of representation theory such as invariant subspaces and irreducible representations."
excerpt: "Representation of finite groups and irreducible decomposition"

categories: [Math / Representation Theory]
permalink: /en/math/representation_theory/representations_of_finite_groups
sidebar: 
    nav: "representation_theory-en"

date: 2026-02-13
weight: 1
translated_at: 2026-07-14T01:30:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-07-14T01:30:02+00:00
---
One common strategy when dealing with mathematical objects of complicated structure is to observe how they act on simpler ones. In this category, we study representation theory, and among its branches, the representation theory of finite groups.

## Basic Notions of Representation Theory

We begin with the following definition.

::: Definition 1
For any finite group $G$, a *representation* of $G$ is a finite-dimensional vector space $V$ together with a function

$$\rho: G\times V \rightarrow V$$

satisfying the conditions of a group action, such that each $\rho(g,-)$ is a linear map.
:::

In general, the ground field $\mathbb{K}$ can be replaced by an arbitrary ring $A$ without issue, but for our discussion it suffices to fix $\mathbb{K}=\mathbb{C}$. Let us also keep in mind that we are mainly considering the case where $V$ is a *finite-dimensional* vector space serving as the representation space. This too can be generalized to infinite-dimensional vector spaces, but doing so requires standard methods such as endowing $V$ with a topological vector space structure.

The above definition can be thought of concisely as being given a homomorphism $G\rightarrow\Aut(V)$. Through a slight abuse of notation, we sometimes write $\rho(g,-): V\rightarrow V$ simply as $\rho(g)\in \Aut(V)$, and further abbreviate by writing $g\cdot v$ instead of $\rho(g)v$. As this notation suggests, we regard $V$ as a $G$-module, and from this viewpoint (with scalar multiplication implicitly understood) we also simply call $V$ a representation of $G$.

Fix a finite group $G$, and let two representations $V,W$ be given. Then a *morphism* from $V$ to $W$ is given by the following diagram:

{% diagram Math/Representation_Theory/Representations_of_Finite_Groups-1.svg width="10.05em" alt="G-equivariant_maps" %}

Expressed as an equation, this can simply be written as

$$L(g\cdot v)=g\cdot L(v)\qquad\text{for all $g\in G$ and $v\in V$}$$

On the other hand, borrowing the language of linear algebra applied to $V$, we can make the following definition.

::: Definition 2
For a representation $G\times V\rightarrow V$ of a group $G$, we define the following.

1. A subspace $W$ of $V$ is called *$G$-invariant* if for any $g\in G$ and any $w\in W$, we always have $g\cdot w\in W$.
2. For any $G$-invariant subspace $W$, the representation $G\times W\rightarrow W$ is called a *subrepresentation* of $V$.
3. If $V$ is not the zero representation and the only subrepresentations of $V$ are the trivial ones, namely $V$ itself and $G\times\{0\}\rightarrow\{0\}$, then $V$ is called an *irreducible representation*.
:::

From the same perspective, for arbitrary representations $V,W$ we can define $V\oplus W$, $V\otimes W$, etc., using the operations on their underlying vector spaces. One subtle point to watch in the next definition is that, unlike in [Definition 2](#def2) above, for $V\otimes W$ etc. a *natural* $G$-action may not exist; therefore we explicitly define a $G$-action on each vector space.

::: Definition 3
For $G$-representations $V, W$, we define new $G$-representations via the following $G$-actions.

1. Direct sum $V\oplus W$; $G$-action $g\cdot(v,w)=(g\cdot v,g\cdot w)$
2. Tensor product $V\otimes W$; $G$-action $g\cdot(v\otimes w)=(g\cdot v)\otimes (g\cdot w)$, and from this the exterior powers $\bigwedge^k V$, symmetric powers $\Sym^k V$ and the $G$-actions on them
3. $\Hom_\mathbb{C}(V,W)$; $G$-action $(g\cdot f)(v)=g\cdot f(g^{-1}\cdot v)$
4. The *dual representation* $V^\ast$ obtained by setting $W=\mathbb{C}$ in 3
5. The *conjugate representation* $\overline{V}$ obtained by replacing scalar multiplication with its conjugate (same $G$-action)
:::

## Category $\lMod{\mathbb{C}[G]}$

In [Definition 3](#def3) above, the definitions of the tensor product and $\Hom$ may look somewhat artificial; to understand them, the language of group algebras is useful. ([\[Algebraic Structures\] §Algebras, ⁋Definition 5](/en/math/algebraic_structures/algebras#def5)) To briefly review, as a set $\mathbb{C}[G]$ was the collection of functions from $G$ to $\mathbb{C}$. For each $x\in G$, defining $\delta_x:G\rightarrow \mathbb{C}$ by

$$\delta_x(y)=\begin{cases}1&\text{if $y=x$}\\0&\text{otherwise}\end{cases}$$

any $\varphi\in\mathbb{C}[G]$ can be written as

$$\phi=\sum_{x\in G}\phi(x)\delta_x$$

so the $\delta_x$ form a basis of $\mathbb{C}[G]$. What distinguishes the $\mathbb{C}[G]$ we deal with from merely being the ring of functions from $G$ to $\mathbb{C}$ is the multiplication defined on it. Instead of defining the product of two functions $\phi,\psi$ by

$$(\phi\psi)(x)=\phi(x)\psi(x), \qquad \text{for all $x\in G$}$$

multiplication on this space is given by the convolution product

$$(\phi\ast \psi)(x)=\sum_{y\in G}\phi(y)\psi(y^{-1}x)$$

If we identify the delta function $\delta_x$ with $x\in G$ as above, then the identity

$$\left(\sum_{x\in G}\phi(x)\cdot x\right)\left(\sum_{y\in G} \psi(y)\cdot y\right)=\sum_{x,y\in G} \phi(x)\psi(y) \cdot(xy)=\sum_{z\in G}\left(\sum_{x\in G} \phi(x)\psi(x^{-1}z)\right)\cdot z$$

holds, so choosing this multiplication is natural. For example, the product of $\delta_x$ and $\delta_y$ is $0$, but their convolution is $\delta_{xy}$; in order for expressions such as the following, which are involved in the group action,

$$(\delta_x\ast \delta_y)\cdot v=\delta_x\cdot(\delta_y\ast v)$$

to make sense, this choice is inevitable.

For any $G$-representation $\rho:G\rightarrow \Aut(V)$, the formula

$$\widetilde{\rho}\left(\sum_{x\in G} \phi_x x, v\right)= \sum_{x\in G} \phi_x\rho(x)v$$

gives a $\mathbb{C}[G]$-module structure on $V$. Conversely, given any $\mathbb{C}[G]$-module $V$, we obtain a $G$-representation from the way each $x\in G$ acts on $V$.

::: Proposition 4
The above correspondences yield a categorical equivalence

$$\Rep_\mathbb{C}(G)\cong \lMod{\mathbb{C}[G]}$$
:::

That is, what we called a $G$-module can also be thought of, strictly speaking, as having only looked at the action induced from a $\mathbb{C}[G]$-module structure when $G\hookrightarrow \mathbb{C}[G]$ is given.

Indeed, most of what we discussed above can be explained by this categorical equivalence. For example, for any $G$-representation $V$, a subrepresentation of $V$ is a $G$-submodule of $V$ (more precisely, a $\mathbb{C}[G]$-submodule). Also, the tensor product of [Definition 3](#def3) is reasonable: in general, for a $\mathbb{K}$-algebra $A$ equipped with a coproduct $\Delta:A\rightarrow A\otimes A$ and two $A$-modules $M,N$, to define their tensor product one must use $\Delta$ via

$$A\otimes (M\otimes N)\rightarrow (A\otimes A)\otimes (M\otimes N)\rightarrow (A\otimes M)\otimes (A\otimes N)\rightarrow M\otimes N$$

and the coproduct $A\rightarrow A\otimes A$ used here in the case of $\mathbb{C}[G]$ is

$$\mathbb{C}[G]\rightarrow \mathbb{C}[G]\otimes \mathbb{C}[G]$$

Similarly, the $\Hom$ defined in [Definition 3](#def3) is adjoint to this $\otimes$, and it is for this reason that the $G$-actions in [Definition 3](#def3), which look somewhat artificial, arise.

In particular, since subrepresentations of $G$ and $\mathbb{C}[G]$-submodules are the same thing, $V$ being an irreducible representation is equivalent to $V$ being a *simple* $\mathbb{C}[G]$-module.

## Maschke's Theorem

We have now roughly surveyed the basic notions needed for representations of finite groups. Before beginning the main discussion, for any representation $V$ let us consider the following subspace:

$$V^G=\{v\in V\mid g\cdot v=v\text{ for all $g\in G$}\}$$

This space consists of vectors fixed by the $G$-action; while it is indeed a $G$-invariant space, what we want to observe is that the obvious projection map

$$p: V\rightarrow V^G;\qquad v\mapsto \frac{1}{\lvert G\rvert}\sum_{g\in G}g\cdot v$$

exists. In particular, the idea contained in this projection map—namely, averaging over all the actions of $G$ to obtain a $G$-invariant object—is of central importance.

::: Definition 5
A Hermitian inner product $\langle-,-\rangle$ on a $G$-representation $V$ is called *$G$-invariant* if for any $g\in G$ and $u,v\in V$,

$$\langle g\cdot u,g\cdot v\rangle=\langle u,v\rangle$$

holds. A representation equipped with a $G$-invariant inner product is called a *unitary representation*.
:::

If such a $G$-invariant inner product is given, then for any $g\in G$, $\rho(g)\in \Aut(V)$ is a unitary operator. To see this, suppose a $G$-invariant inner product $\langle -,-\rangle$ is given; then for any $g\in G$,

$$\langle v,w\rangle=\langle \rho(g) v,\rho(g) w\rangle=\langle \rho(g)^\dagger \rho(g)v,w\rangle$$

holds for *all* $v,w\in V$.

On the other hand, any finite-dimensional $G$-module $V$ admits a $G$-invariant inner product. This can be proved using the idea mentioned above.

::: Proposition 6
Any representation $V$ admits a $G$-invariant inner product. That is, every representation is a unitary representation.
:::
::: Proof
For any Hermitian inner product $\langle -,- \rangle$ on $V$, define a new inner product $\langle\kern-1.5pt\langle-,-\rangle\kern-1.5pt\rangle$ by

$$\langle\kern-1.5pt\langle u,v\rangle\kern-1.5pt\rangle = \frac{1}{\lvert G\rvert }\sum_{g \in G} \langle g\cdot u, g\cdot v \rangle$$

Then for any $h\in G$,

$$\langle\kern-1.5pt\langle h\cdot u, h\cdot v\rangle\kern-1.5pt\rangle = \frac{1}{\lvert G\rvert }\sum_{g \in G} \langle gh\cdot u, gh\cdot v \rangle = \langle\kern-1.5pt\langle u, v\rangle\kern-1.5pt\rangle$$

so this inner product is $G$-invariant.
:::

In any case, the central theorem of this section follows from the above proposition.

::: Corollary 7 (Maschke)
For any finite-dimensional $G$-representation $V$ and any $G$-invariant subspace $W$, there exists a $G$-invariant subspace $W'$ such that $V = W \oplus W'$. Therefore, inductively, any finite-dimensional $G$-representation decomposes into a direct sum of irreducible representations.
:::
::: Proof
Taking $W'$ to be the orthogonal complement of $W$, then $W'$ is also a $G$-invariant subspace and $V = W \oplus W'$ holds.
:::

Earlier we examined the categorical equivalence

$$\Rep_\mathbb{C}(G)\cong \lMod{\mathbb{C}[G]}$$

What [Corollary 7](#cor7) asserts, then, is that any finite-dimensional $G$-representation $V$ is always a *semisimple* $\mathbb{C}[G]$-module ([\[Ring Theory\] §Semisimple module, ⁋Definition 1](/en/math/ring_theory/semisimple_modules#def1)). Therefore, viewing $\mathbb{C}[G]$ itself as the regular representation, it is a semisimple module by [Corollary 7](#cor7), hence an Artinian semisimple ring, and by [\[Ring Theory\] §Artin-Wedderburn Theorem, ⁋Theorem 11](/en/math/ring_theory/artin_wedderburn#thm11) we know that a decomposition into simple modules

$$\mathbb{C}[G]\cong \bigoplus_{i=1}^r \Mat_{n_i}(\mathbb{C})\tag{1}$$

exists.

## Schur Orthogonality

In the next post we will give representation-theoretic meaning to the decomposition (1). As preparation for this, we prove the following lemma.

::: Lemma 8 (Schur)
Let a (compact) group $G$ and irreducible $G$-modules $V,W$ be given. Then the following hold.

1. Any $G$-map $V\rightarrow W$ is either the zero map or an isomorphism.
2. Any $G$-automorphism $f\in \Aut_G(V)$ is of the form $f(v)=\lambda v$.
3. The space of $G$-maps $\Hom_G(V,W)$ is either $\mathbb{C}$ or $0$.
:::
::: Proof
1. A $G$-map is a $\mathbb{C}[G]$-module homomorphism, and an irreducible $G$-module is a simple $\mathbb{C}[G]$-module, so this is a special case of [\[Ring Theory\] §Division ring, ⁋Lemma 10](/en/math/ring_theory/division_rings#lem10).
2. Since $f$ is a $\mathbb{C}$-linear map before being a $G$-linear map, $f$ has an eigenvalue $\lambda$. Letting $V_\lambda$ be the eigenspace of this eigenvalue, for any $w\in V_\lambda$ and $g\in G$ we have $f(g\cdot w)=g\cdot f(w)=\lambda(g\cdot w)$, so $V_\lambda$ is a nonzero $G$-submodule of $V$. Since $V$ is irreducible, $V_\lambda=V$, and hence $f=\lambda\id_V$.
3. If $V\not\cong W$ then $\Hom_G(V,W)=0$ by 1. If $V\cong W$ then $\Hom_G(V,W)\cong\End_G(V)$, and since any nonzero $f\in\End_G(V)$ is of the form $\lambda\id_V$ by 2, we have $\End_G(V)=\mathbb{C}\id_V\cong\mathbb{C}$.
:::

Using this, we obtain the following proposition.

::: Proposition 9
In the above situation, the function

$$d=\bigoplus_{W\in\Irr(G, \mathbb{C})} d_W:\bigoplus_{W\in \Irr(G, \mathbb{C})}\Hom_G(W,V)\otimes_\mathbb{C}W\rightarrow V$$

is an isomorphism.
:::
::: Proof
By [Corollary 7](#cor7) there exists an irreducible decomposition $V=\bigoplus_j V_j$, and thus we obtain

$$\Hom_G(W, V)=\Hom_G\left(W, \bigoplus V_j\right)\cong \bigoplus \Hom_G(W, V_j) $$

By [Lemma 8](#lem8) each term is $1$-dimensional when $V_j\cong W$ and $0$ otherwise, so choosing an isomorphism $u_j:W\rightarrow V_j$ for each $j$ with $V_j\cong W$ gives a basis of $\Hom_G(W,V)$. Then $d_W$ is the direct sum of isomorphisms sending each $\mathbb{C}u_j\otimes_\mathbb{C}W$ onto $V_j$ via $u_j$, so it is an isomorphism onto $\bigoplus_{V_j\cong W}V_j$, and taking the direct sum over all isomorphism classes gives all of $\bigoplus_jV_j=V$, so $d$ is an isomorphism.
:::

Although written in a complicated way, the above $d$ simply counts how many copies of each irreducible $G$-module $W$ (or its isomorphism class) appear inside $V$, so the following definition is natural.

::: Definition 10
The image of $W\in\Irr(G, \mathbb{C})$ under the above function is called the *$W$-isotypical summand* of $V$, and $\Hom_G(W, V)$ is called the *multiplicity* of $W$.
:::

This definition agrees with the general theory. The image of $d_W$ is the subspace generated by the simple submodules of $V$ isomorphic to $W$, so it is exactly the $W$-isotypic component of [\[Ring Theory\] §Semisimple module, ⁋Definition 7](/en/math/ring_theory/semisimple_modules#def7), and by [the same post, ⁋Proposition 8](/en/math/ring_theory/semisimple_modules#prop8) this decomposition is canonical, independent of the choice of irreducible decomposition.

Uniqueness of the representation also follows now from [\[Ring Theory\] §Semisimple module, ⁋Proposition 9](/en/math/ring_theory/semisimple_modules#prop9). That is, we know that given any representation $V$, it can be written in the form of the decomposition

$$V=V_1^{\oplus r_1}\oplus\cdots\oplus V_k^{\oplus r_k}$$

where the isomorphism classes of the factors and their multiplicities are uniquely determined.
