---
title: "Poincaré Duality"
description: "We define Poincaré duality, a geometric duality between homology and cohomology on connected topological manifolds, using orientation sheaves, and examine its structure."
excerpt: "Duality between homology and cohomology via orientation sheaves and fundamental classes"

categories: [Math / Algebraic Topology]
permalink: /en/math/algebraic_topology/Poincare_duality
sidebar: 
    nav: "algebraic_topology-en"

date: 2025-09-23
weight: 9
translated_at: 2026-07-11T05:30:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-07-11T05:30:02+00:00
---
In this post we discuss Poincaré duality, a beautiful theorem of algebraic topology. As mentioned in the previous post, Poincaré duality exhibits a duality between homology and cohomology. The case of [§Cohomology, ⁋Theorem 5](/en/math/algebraic_topology/cohomology#thm5) that we have already seen was, to some extent, an expected result when we defined $C^\bullet(X;A)$ as the dual of $C_\bullet(X;A)$, but Poincaré duality carries a more genuinely geometric meaning.

## Orientation Sheaf

To define Poincaré duality, we must first define the notion of orientation. This is a concept defined on a topological manifold ([§Topological Manifolds, ⁋Definition 2](/en/math/algebraic_topology/topological_manifolds#def2)), and in this post we assume that any manifold is *connected* unless stated otherwise.

Given any topological manifold $M$ of dimension $m$ and an open set $U$, the correspondence

$$U\mapsto H_m(M, M\setminus U;\mathbb{Z})$$

is a presheaf because for any $U\subseteq V$ we have a natural restriction map

$$H_m(M, M\setminus V;\mathbb{Z})\rightarrow H_m(M,M\setminus U;\mathbb{Z})\tag{1}$$

::: Definition 1
The sheafification of the correspondence (1) is called the *orientation sheaf* and is denoted by $\or_M$. ([\[Topology\] §Sheaves, ⁋Definition 5](/en/math/topology/sheaves#def5))
:::

Then for any $x\in M$ and any open neighborhood $U$ of $x$, there is a canonical map

$$H_m(M,M\setminus U;\mathbb{Z})\rightarrow H_m(M,M\setminus\{x\};\mathbb{Z})$$

These behave well with respect to the restriction maps above, and hence the map of direct limits

$$\or_{M,x}=\varinjlim_{x\in U} H_m(M,M\setminus U;\mathbb{Z})\rightarrow H_m(M,M\setminus \{x\};\mathbb{Z})$$

is well-defined.

By definition, an element of $H_m(M,M\setminus\{x\};\mathbb{Z})$ is an $m$-simplex $\sigma:\Delta^m \rightarrow M$ whose boundary does not meet $x$; then we can choose a sufficiently small neighborhood $U$ of $x$ so that this boundary does not meet $U$. On the other hand, if two homology classes $\alpha_U\in H_m(M,M\setminus U;\mathbb{Z})$ and $\alpha_V\in H_m(M,M\setminus V;\mathbb{Z})$ represent the same element in $H_m(M,M\setminus \{x\};\mathbb{Z})$, then similarly we can find a sufficiently small open neighborhood $W$ of $x$ that meets neither boundary, and then $\alpha_U$ and $\alpha_V$ must be the same element in $H_m(M,M\setminus W;\mathbb{Z})$. Thus the map

$$\varinjlim_{x\in U}H_m(M,M\setminus U;\mathbb{Z})\rightarrow H_m(M,M\setminus \{x\};\mathbb{Z})$$

is an isomorphism. Meanwhile, by [§Computation of Homology, ⁋Theorem 2](/en/math/algebraic_topology/computation_of_homology#thm2),

$$H_m(M,M\setminus\{x\};\mathbb{Z})\cong H_m(U,U\setminus\{x\};\mathbb{Z})\cong H_m(\mathbb{R}^m, \mathbb{R}^m\setminus\{0\};\mathbb{Z})$$

and since $\mathbb{R}^m\setminus\{0\}$ deformation retracts onto $S^{m-1}$, the relative homology long exact sequence shows that the right-hand side of the above is isomorphic to $\mathbb{Z}$; we can also verify that this sheaf is locally constant. That is, for any given $x\in M$ there exists a suitable open neighborhood $U$ such that $\or_M\vert_U$ is a constant sheaf. ([\[Topology\] §Sheaves, ⁋Example 9](/en/math/topology/sheaves#ex9))

::: Definition 2
The relative homology group $H_m(M, M\setminus \{x\};\mathbb{Z})$ is called the *local homology group* of $M$ at $x$.
:::

## Constant Sheaves, Covering Spaces, and the Orientation-Generator Sheaf

To examine the orientation sheaf $\or_M$ defined above in more detail, we need to look more closely at constant sheaves and locally constant sheaves. First, consider an arbitrary abelian group $A$, give it the discrete topology, and regard it as a topological space. Then the projection map $X\times A \rightarrow X$ between topological spaces is a trivial covering space, and the sheaf of sections of this covering map is precisely the constant sheaf $\underline{A}$. Conversely, given a constant sheaf $\underline{A}$, we can verify that its étale space $\Spe(\underline{A})$ becomes the covering space $X\times A \rightarrow X$. ([\[Topology\] §Presheaves](/en/math/topology/presheaves)) Thus a locally constant sheaf is nothing more than a sheaf whose étale space is a covering space.

Intuitively, $H_m(M,M\setminus\{x\};\mathbb{Z})\cong \mathbb{Z}$ tells us how many times an $m$-simplex $\sigma:\Delta^m\rightarrow M$ containing $x$ in its interior covers $x$. On the other hand, $\Delta^m$ can be given a sign depending on how an ordering is assigned to its vertices; then through this isomorphism, when we assign an element of $\mathbb{Z}$ to such $m$-simplices, the sign difference between two $m$-simplices can be thought of as either the source $\Delta^m$ being given opposite orientations, or, fixing the orientation of $\Delta^m$, the two simplex maps specifying different directions. That is, $H_m(M,M\setminus\{x\};\mathbb{Z})$ carries information about the orientation at the point $x$.

Then a natural question is whether, for every point $x\in M$, we can choose an orientation so that these orientations can be glued together to match a global orientation on $M$. For this we first need a copy of $\mathbb{Z}$ to serve as a reference. To this end, fix a constant sheaf $\underline{\mathbb{Z}}$ on $M$. ([\[Topology\] §Presheaves, ⁋Example 6](/en/math/topology/presheaves#ex6)) Then for each $x\in M$, its stalk $\underline{\mathbb{Z}}_x$ can be thought of as having the generator $1$ chosen in a consistent manner, and thus choosing an isomorphism

$$\Iso_\mathbb{Z}(H_m(M, M\setminus\{x\}), \underline{\mathbb{Z}}_x)$$

for each $x$ is the same as choosing, at each $x$, whether $M$ is positively or negatively oriented.

::: Definition 3
For a topological manifold $M$ of dimension $m$, a *local orientation* at a point $x$ is given by choosing an element of $\Iso_\mathbb{Z}(H_m(M,M\setminus\{x\}), \underline{\mathbb{Z}}_x)$.
:::

Now for each open set $U$ define

$$\omega_M^\pre(U)=\prod_{x\in U}\Iso_\mathbb{Z}(H_m(M,M\setminus\{x\}), \underline{\mathbb{Z}}_x)$$

and whenever $U\subseteq V$, define $\rho_{VU}:\omega_M^\pre(V)\rightarrow \omega_M^\pre(U)$ to be the canonical projection. ([\[Set Theory\] §Properties of Products, ⁋Definition 1](/en/math/set_theory/property_of_products#def1)) Then $\omega_M^\pre$ becomes a presheaf on $M$ ([\[Topology\] §Presheaves, ⁋Definition 4](/en/math/topology/presheaves#def4)), and for each $p\in M$ the stalk $\omega_{M,x}^\pre$ of $\omega_M^\pre$ at the point $x$ is $\{\pm 1\}$. ([\[Topology\] §Presheaves, ⁋Definition 9](/en/math/topology/presheaves#def9))

We call the sheafification $\omega_M$ of $\omega_M^\pre$ the *orientation-generator sheaf* of $M$. This amounts to, once the generator $1$ of the fixed constant sheaf $\underline{\mathbb{Z}}$ is fixed, examining whether the isomorphism $H_m(M,M\setminus\{x\};\mathbb{Z})$ sends $1$ to $1$ or to $-1$; through this, $\omega_M$ can be viewed as a subsheaf of $\or_M$. Then since $\omega_M$ is a locally constant sheaf, its étale space $\Spe(\omega_M)$ is a covering space of $M$ and each fiber consists of two elements.

::: Definition 4
The étale space $\Spe(\omega_M)$ defined above is called the *orientation double cover* of $M$, and a global section $M \rightarrow \Spe(\omega_M)$ is called a *global orientation*. We say $M$ is *orientable* if a global orientation exists.
:::

Then, as its name suggests, $\Spe(\omega_M)$ is a covering space of $M$, and moreover for any $x\in M$, if we consider a chart $U$ of $x$, the preimage $p^{-1}(U)$ of $U$ under the canonical projection $p:\Spe(\omega_M)\rightarrow M$ is represented as two disjoint open subsets each homeomorphic to $U$.

::: Example 5
For example, consider the orientation double cover $p:\Spe(\omega_{S^1})\rightarrow S^1$ of $S^1$. For any point $x\in S^1$, the preimage $p^{-1}(x)$ under $p$ consists of two points $(x,+)$ and $(x,-)$, and the same holds for a chart $U$ containing $x$, so $p^{-1}(U)$ splits into two open subsets $U^+,U^-$.

{% diagram Math/Algebraic_Topology/Poincare_Duality-1.svg width="45%" alt="Orientation_cover_of_S1" %}

Now if we cover $S^1$ with such charts, and glue the orientations together as they are where the charts overlap, these become a double cover with two components as follows.

{% diagram Math/Algebraic_Topology/Poincare_Duality-2.svg width="45%" alt="Orientation_cover_of_S1_glued" %}

However, not every double cover is trivial. For example, if in the above cover of $S^1$ we cross-glue the upper and lower components, we obtain a double cover with one component, and a similar thing happens for the orientation double cover of a non-orientable manifold.

To observe this, consider the orientation cover of the Möbius strip $M$. As with $S^1$, for any point $x\in M$, the preimage $p^{-1}(x)$ consists of two points $(x,+)$ and $(x,-)$, and the same holds for any point of $M$.

{% diagram Math/Algebraic_Topology/Poincare_Duality-3.svg width="40%" alt="orientation_cover_of_M" %}

However, if we try to glue these to cover all of $M$, a problem arises: if we glue the two sheets shown in this picture counterclockwise while keeping track of orientation, when we return to $x$ the points $(x,+)$ and $(x,-)$ have swapped, so we must cross-glue the upper and lower components. The resulting double cover of $M$ is homeomorphic to a cylinder.
:::

By definition, for $M$ to be orientable there must exist a global section of $\omega_M$, which is equivalent to $\Spe(\omega_M)$ being a trivial covering space, which in turn is equivalent to $\omega_M$ being a constant sheaf. Applying [§Covering Spaces, ⁋Corollary 12 (Fundamental theorem of covering spaces, classical version)](/en/math/algebraic_topology/covering_spaces#cor12) to this, we obtain the following proposition.

::: Proposition 6
For a (connected) topological manifold $M$, the following are equivalent.

1. $M$ is orientable.
2. $\Spe(\omega_M)$ has two components.
3. The monodromy action of $\pi_1(M)$ on $\Spe(\omega_M)$ is trivial.
:::

Now, when we dealt with homology and cohomology we already extended from $\mathbb{Z}$-modules to general $A$-modules, so the above argument can also be extended to a general $A$-module. For this, first considering the relative homology version of [\[Algebraic Topology\] §Cohomology, ⁋Proposition 1](/en/math/algebraic_topology/cohomology#prop1), observe that the following (non-canonical) isomorphism exists:

$$H_k(M, M\setminus\{x\};A)\cong H_k(M,M\setminus\{x\})\otimes_\mathbb{Z}A\oplus\Tor_1^\mathbb{Z}(H_{k-1}(M, M\setminus\{x\}), A)$$

However, since $H_k(M,M\setminus \{x\})$ is always the trivial group when $k\neq m$, from this isomorphism we know that

$$H_m(M,M\setminus \{x\};A)\cong H_m(M,M\setminus\{x\})\otimes_\mathbb{Z}A\cong A$$

Thus the above argument still makes sense if we replace all occurrences of $\mathbb{Z}$ with $A$, and in particular we will obtain the presheaf of $A$-orientations

$$\omega_M^A(U)=\prod_{x\in U}\Iso_A(H_m(M,M\setminus\{x\};A), \underline{A}_x)$$

and from this the notion of a global $A$-orientation. The $A$-orientation sheaf $\omega_M^A$ obtained this way is nothing other than $\omega_M\otimes A$.

To derive a result analogous to [Proposition 6](#prop6) from this definition, let us revisit [§Covering Spaces, ⁋Theorem 11](/en/math/algebraic_topology/covering_spaces#thm11). For each covering space $p:E \rightarrow M$, we considered the $\pi_1(M,x)$-action on the fiber $p^{-1}(x)$ defined by the monodromy functor, which was the same as considering a group homomorphism $\pi_1(M,x)\rightarrow \Aut(p^{-1}(x))$. Then we must examine how the $\pi_1(M,x)$-action is defined for the covering space $p:\Spe(\omega_M)\rightarrow M$; in this case the fiber $p^{-1}(x)$ is defined from the automorphism group of the stalk $\mathbb{Z}$

$$\Iso_\mathbb{Z}(\mathbb{Z},\mathbb{Z})\cong \mathbb{Z}^\times\cong \{\pm 1\}$$

and thus the $\pi_1(M,x)$-action can be thought of precisely as a group homomorphism $\pi_1(M,x)\rightarrow \mathbb{Z}^\times$. Then since an $A$-module isomorphism from $A$ to $A$ corresponds exactly to an element of the unit group $A^\times$ of $A$, this is the same as examining a group homomorphism $\pi_1(M,x)\rightarrow A^\times$. That is, [Proposition 6](#prop6) can be generalized as follows.

::: Proposition 7
For a (connected) topological manifold $M$, the following are equivalent.

1. $M$ is $A$-orientable.
2. $\Spe(\omega_M^A)$ is the trivial covering $M\times \lvert A^\times\rvert$.
3. The monodromy representation $\pi_1(M)\rightarrow A^\times$ is trivial.
:::

The most notable case of this generalization is when $A=\mathbb{Z}/2$. In this case, since the only unit of $A$ is $-1=1$, there is a unique way to specify orientation, and hence any manifold is always $\mathbb{Z}/2$-orientable.

## Fundamental Class

Now we examine the existence of a global ($A$-)orientation. That is, given local orientations $s_x$ for all $x\in X$, we will investigate whether there exists a suitable global section $s:M\rightarrow \Spe(\omega_M^A)$ such that $s(x)=(x,s_x)$.

On the other hand, we know that through the following canonical homomorphism

$$H_m(M; A)\rightarrow H_m(M,M\setminus\{x\};A)\tag{1}$$

any top homology class $\alpha\in H_m(M;A)$ defines an element $\alpha_x\in H_m(M,M\setminus\{x\};A)$ of the local homology group. Then one natural question is whether, viewing the given local orientations $s_x$ for each $x\in S_x$ as elements of $A^\times$ and treating them as elements of $H_m(M,M\setminus\{x\};A)$, there exists an $\alpha$ such that the image of $\alpha\in H_m(M;A)$ in $H_m(M,M\setminus\{x\};A)$ is $s_x$ for all $x\in X$.

The two paragraphs above illustrate what form Poincaré duality takes. A global section $s:M \rightarrow \Spe(\omega_M^A)$ is essentially a function defined over all of $M$, a concept corresponding to $0$th cohomology. On the other hand, $\alpha\in H_m(M;A)$ is an element of $m$th homology. Poincaré duality shows that these two concepts are equivalent, and more generally, it exhibits a duality between $k$th cohomology and $(n-k)$th homology.

What remains for us to do in the rest of this post is roughly two things.

1. Show that a lifting of the canonical homomorphism (1) defines a global orientation, and conversely.
2. Define the *sheaf cohomology* in which a global orientation $M \rightarrow \Spe(\omega_M^A)$ exists.

The essential content of Poincaré duality is all contained in the first step, and the second step is closer to learning the language that can express this wisely. Therefore we begin with the first step. This is obtained by the following lemma.

::: Lemma 8
Fix a topological manifold $M$ of dimension $m$. For any compact subset $C$ of $M$, the following hold.

1. Given any section $s:M \rightarrow \Spe(\omega_M^A)$, there exists a unique homology class

    $$\alpha_C\in H_m(M,M\setminus C;A)$$

    such that for every $x\in C$, the image of $\alpha_C$ under the canonical homomorphism

    $$H_m(M,M\setminus C;A)\rightarrow H_m(M,M\setminus\{x\};A)$$

    is $s_x$.
2. For all $i>m$, $H_i(M, M\setminus C;A)=0$.
:::
::: Proof
First, let us show that if the statement holds for arbitrary compact sets $C_1,C_2$ and their intersection $C_1\cap C_2$, then it also holds for $C_1\cup C_2$. From the Mayer–Vietoris sequence

$$\cdots \rightarrow H_k(M,M\setminus (C_1\cup C_2); A)\rightarrow H_k(M,M\setminus C_1;A)\oplus H_k(M,M\setminus C_2;A)\rightarrow H_k(M, M\setminus (C_1\cap C_2);A)\rightarrow\cdots\tag{2}$$

for $k>m$, by the inductive hypothesis

$$H_k(M,M\setminus C_1;A)=H_k(M,M\setminus C_2;A)=H_k(M,M\setminus(C_1\cap C_2);A)=0$$

so $H_k(M,M\setminus (C_1\cup C_2);A)$ must also be $0$, and from this the second claim follows.

To show the first claim, suppose a section $s:M \rightarrow \Spe(\omega_M^A)$ is given. By the inductive hypothesis, liftings exist for $C_1,C_2,C_1\cap C_2$, so we must glue these to produce a class $\alpha_{C_1\cup C_2}$ for $C_1\cup C_2$. By the uniqueness of $\alpha_{C_1},\alpha_{C_2},\alpha_{C_1\cap C_2}$, both $\alpha_{C_1}$ and $\alpha_{C_2}$ must restrict to the same element as $\alpha_{C_1\cap C_2}$, so considering the element

$$(\alpha_{C_1},-\alpha_{C_2})\in H_m(M,M\setminus C_1;A)\oplus H_m(M,M\setminus C_2;A)$$

in (2), this element lies in the kernel of $H_m(M,M\setminus C_1;A)\oplus H_m(M,M\setminus C_2;A)\rightarrow H_m(M, M\setminus (C_1\cap C_2);A)$, and hence we can choose an element of $H_m(M,M\setminus (C_1\cup C_2);A)$; uniqueness comes from the injectivity of

$$0=H_{m+1}(M,M\setminus (C_1\cap C_2);A)\rightarrow H_m(M,M\setminus (C_1\cup C_2))\rightarrow H_m(M,M\setminus C_1;A)\oplus H_m(M,M\setminus C_2;A)$$

For the base step of the induction, it suffices to consider the case $M=\mathbb{R}^m$ and $A$ a convex compact subset. This is because any compact set of an arbitrary manifold $M$ can be covered by Euclidean charts, and using compactness we may assume $M=\mathbb{R}^m$; using the basis of open balls in $\mathbb{R}^m$ and again compactness, we may additionally assume that $A$ is convex. Then in this step, both spaces $\mathbb{R}^m\setminus A$ and $\mathbb{R}^m\setminus \{x\}$ deformation retract onto the same space $S^{m-1}$, so we obtain an isomorphism, and the proof is complete.
:::

In this proof, compactness is absolutely necessary so that the inductive construction of $\alpha$ using the Mayer–Vietoris sequence terminates in finitely many steps. If compactness is dropped, Poincaré duality takes a somewhat different form, and to express this in a unified formula we need the language of sheaf cohomology.

In any case, by [Lemma 8](#lem8) above, if $M$ is a compact topological manifold of dimension $m$, then setting $C=M$ we obtain the following theorem.

::: Theorem 9
Let $M$ be a compact connected topological manifold of dimension $m$. Then given an orientation sheaf $\omega_M^A$, there exists a unique class $[M]\in H_m(M;A)$ such that the image of $[M]$ under the canonical homomorphism (1) coincides with $s_x$.
:::

Then by [Lemma 8](#lem8), $H_m(M;A)$ is a free $A$-module of rank 1 generated by $[M]$, and different choices of global orientation correspond to different choices of generator of $H_m(M;A)$.

::: Definition 10
The $[M]$ defined in [Theorem 9](#thm9) above is called the *fundamental class* of $M$ determined by the global orientation $s$.
:::

Moreover, if a homology class $[M]$ satisfying the conditions of [Theorem 9](#thm9) exists, we know that a global section $s:M \rightarrow \Spe(\omega_M^A)$ is given from it.

## Poincaré Duality

We can now prove the Poincaré theorem when the given manifold is $A$-orientable. For this, consider the following cap product homomorphism

$$-\frown -: H^p(M;A)\otimes_A H_m(M;A) \rightarrow H_{m-p}(M;A)$$

Since $H_m(M;A)\cong A$, this homomorphism can be thought of as an $A$-module homomorphism from $H^p(M;A)$ to $H_{m-p}(M;A)$. In particular, introducing the generator $[M]$ of $H_m(M;A)$, this becomes the homomorphism

$$-\frown [M]: H^p(M;A)\rightarrow H_{m-p}(M;A)$$

::: Theorem 11
For an $A$-orientable compact manifold $M$ of dimension $m$ and its fundamental class $[M]$, the above homomorphism

$$-\frown [M]: H^p(M;A)\rightarrow H_{m-p}(M;A)$$

is an isomorphism.
:::

The proof of this also proceeds by induction using the Mayer–Vietoris sequence, just as in the proof of [Lemma 8](#lem8). However, a somewhat different point is that in [Lemma 8](#lem8) the claim was about a compact subset $C$, so compactness could be used aggressively, whereas this time the claim is about $M$ itself, so for example if a chart $U$ of $M$ is given, this is not compact and a simple inductive approach does not work. For this we define the following.

::: Definition 12
A cochain $\varphi\in C^p(M;A)$ is said to be *compactly supported* if there exists a compact set $K\subseteq M$ such that $\varphi(\sigma)=0$ holds for all simplices contained in $M\setminus K$. The $i$th homology of the cochain complex of compactly supported cochains is called the $p$th *compactly supported cohomology* and is denoted by $H_c^p(M;A)$.
:::

Then the following formula

$$H_c^p(M;A)\cong \varinjlim_{\text{\scriptsize$K$ compact}}H^p(M,M\setminus K;A)$$

holds intuitively obviously and the proof is clear. For each compact set $K$,

$$H^p(M,M\setminus K;A)\rightarrow H_c^p(M;A)$$

exists canonically, and this is compatible with the directed system on the right-hand side, so the homomorphism

$$\varinjlim_{\text{\scriptsize$K$ compact}}H^p(M,M\setminus K;A)\rightarrow H_c^p(M;A)$$

is well-defined. That this is an isomorphism can be shown directly. In particular, for any compact manifold $M$, $H_c^p(M,A)\cong H^p(M;A)$ holds, and hence the desired result follows from the following lemma.

::: Lemma 13
For any $A$-orientable $m$-manifold $M$, the isomorphism

$$H_c^p(M;A)\cong H_{m-p}(M;A)$$

holds for all $p$.
:::
::: Proof
To do this, we must first define the isomorphism. For this, for any compact subset $K$ consider the cap product

$$H^p(M,M\setminus K;A)\times H_m(M,M\setminus K;A)\rightarrow H_{m-p}(M;A)$$

Then by [Lemma 8](#lem8), we can find a homology class

$$s_K\in H_m(M,M\setminus K;A)$$

that matches the orientation of $M$ at each point $x$ when restricted to $x$. Our claim is that the cap product homomorphisms

$$-\frown s_K: H^p(M,M\setminus K;A) \rightarrow H_{m-p}(M;A)$$

made from such $s_K$ satisfy compatibility with respect to the direct system, and hence define a homomorphism $H_c^p(M;A)\rightarrow H_{m-p}(M;A)$. To verify this, suppose another compact subset $K'$ containing $K$ and the inclusion $i:K\rightarrow K'$ are given. Then for any $\alpha\in H^p(M,M\setminus K;A)$,

$$i^\ast\alpha\frown s_{K'}=\alpha\frown i_\ast s_{K'}$$

holds by [§Cup Product, ⁋Proposition 6 (Projection formula)](/en/math/algebraic_topology/cup_products#prop6), and by the uniqueness in [Lemma 8](#lem8), $i_\ast s_{K'}=s_K$, so we know that this defines the homomorphism $H_c^p(M;A)\rightarrow H_{n-p}(M;A)$ well.

Our claim is that this homomorphism $D_M:H_c^p(M;A)\rightarrow H_{n-p}(M;A)$ is an isomorphism, and to show this we use induction via the Mayer–Vietoris sequence, just as in the proof of [Lemma 8](#lem8).

The base step of the induction is the case $M=\mathbb{R}^m$. In this case, we know that for any ball $B\subseteq \mathbb{R}^m$, the orientation $s_B$ of $B$ gives

$$H_m(\mathbb{R}^m, \mathbb{R}^m\setminus B;A)\cong A$$

and from [§Cohomology, ⁋Proposition 3](/en/math/algebraic_topology/cohomology#prop3) we have $H^m(\mathbb{R}^m,\mathbb{R}^m\setminus B;A)\cong A$; at this time, the element $\alpha_B$ corresponding to the dual basis of the orientation of $B$ satisfies the following formula

$$\langle 1\smile \alpha_B, s_B\rangle=\langle 1,\alpha_B\frown s_B\rangle$$

so we know that $\alpha_B\frown s_B$ corresponds to the generator of $H_0(\mathbb{R}^m)\cong A$, and hence

$$H^p(\mathbb{R}^m,\mathbb{R}^m\setminus B;A)\cong H_{m-p}(\mathbb{R}^m;A)$$

holds for all $p$. (For $p\neq m$, this is the zero map between zero modules, so it is an isomorphism.) Now if we increase the radius of $B$ and construct a directed system covering all of $\mathbb{R}^m$, we know that $H_c^p(M)\rightarrow H_{m-p}(M)$ is an isomorphism.

For the next step, suppose there exist two open sets $U,V$ of $M$ such that $M=U\cup V$ and the given statement holds for $U,V,U\cap V$. Then for each compact subset $K\subseteq U$, $L\subseteq V$, considering the relative Mayer–Vietoris sequence

$$\cdots\rightarrow H^k(M,M\setminus(K\cap L);A)\rightarrow H^k(M,M\setminus K;A)\oplus H^k(M,M\setminus L;A)\rightarrow H^k(M,M\setminus(K\cup L);A)\rightarrow \cdots$$

and then applying excision and taking limits, we obtain the following commutative diagram

{% diagram Math/Algebraic_Topology/Poincare_Duality-4.svg width="38.08em" alt="MVseq_duality" %}

and the induction is completed by the inductive process and [\[Homological Algebra\] §Diagram chasing, ⁋Corollary 2 (The five lemma)](/en/math/homological_algebra/diagram_chasing#cor2).

However, since we do not assume that $M$ is compact, a slight additional argument is needed. First, suppose $M$ is the union of a nested family of open subsets

$$U_1\subseteq U_2\subseteq\cdots$$

and the given statement holds for each of them. Then any compact subset of $M$ must be contained in some $U_i$, and from this we obtain the following isomorphisms

$$H_c^p(M)=\varinjlim_i H^p_c(U_i),\qquad H_{m-p}(M)=\varinjlim_i H_{m-p}(U_i)$$

By assumption, the $H^p_c(U_i)\rightarrow H_{m-p}(U_i)$ are all isomorphisms, so we obtain the desired result.

Now consider the case where $M$ is an open subset of $\mathbb{R}^m$. Then we can first cover $M$ with countably many convex open subsets (i.e., open balls) $U_1,U_2,\ldots$ homeomorphic to $\mathbb{R}^m$, and since any convex open subset is homeomorphic to $\mathbb{R}^m$, we saw in the base step above that the theorem's isomorphism holds for each of them. Also, the intersection of two convex sets is again convex, so by the above induction the conclusion also holds for $U_1\cup U_2$. To next show that the conclusion holds for $U_1\cup U_2\cup U_3$, we must show that the following intersection

$$(U_1\cup U_2)\cap U_3=(U_1\cap U_3)\cup (U_2\cap U_3)$$

satisfies the given condition; here $U_1\cap U_3$, $U_2\cap U_3$, and $U_1\cap U_2\cap U_3$ are all convex open subsets of $\mathbb{R}^m$ satisfying the given condition. In a similar way, we know that each of

$$U_1,\quad U_1\cup U_2, \quad U_1\cup U_2\cup U_3,\quad \cdots$$

satisfies the conclusion. Therefore, applying the preceding (infinite) induction to the sequence of nested open subsets

$$U_1\subseteq U_1\cup U_2\subseteq U_1\cup U_2\cup U_3\cdots$$

we obtain the desired result.

Finally, if $M$ is an arbitrary manifold, using second countability we cover $M$ with countably many Euclidean charts and proceed with the same argument as above.
:::

In particular, in the proof, if $M$ itself had been compact, the duality map $D_M$ would have been exactly the cap product with the fundamental class $[M]$.

## Twisted Poincaré Duality

When $M$ is not $A$-orientable, the main reason [Theorem 11](#thm11) fails is fundamentally that $\or_M^A$ fails to be a constant sheaf and is only locally constant. In the language of covering spaces, this can be thought of as the monodromy action acting nontrivially on the stalk $A$, so that when we "go around once" the stalk $A$ gets twisted and glued back to itself. Since this twist is an automorphism of $A$, it was sufficient for us to consider the bijection of the unit group $A^\times$ of $A$ to see this.

To incorporate this twist into the duality, we now define *homology with local coefficients*.

::: Definition 14
A locally constant sheaf $\mathcal{L}$ defined on $M$ is called a *local coefficient system*.
:::

Let the stalk of the local system $\mathcal{L}$ be $L$. Then by [§Covering Spaces, ⁋Theorem 11](/en/math/algebraic_topology/covering_spaces#thm11), we know that for any path $\alpha:[0,1]\rightarrow M$, there exists an isomorphism $\mathcal{L}_{\alpha(0)}\rightarrow \mathcal{L}_{\alpha(1)}$ between stalks. This is nothing other than the isomorphism obtained by lifting the path $\alpha$ in the covering space $\Spe(\mathcal{L})\rightarrow M$. That is, we obtain the following functor

$$\Pi_1(M)\rightarrow \Ab; \qquad x\mapsto \mathcal{L}_x$$

Then fixing a point $e_0=(1,0,\ldots,0)$ of $\Delta^k$, we define $C_\bullet(M,\mathcal{L})$ by the formula

$$C_\bullet(M,\mathcal{L})=\bigoplus_{\sigma:\Delta^k\rightarrow M}\mathcal{L}_{\sigma(e_0)}$$

After all, for each $x$ we have $\mathcal{L}_x\cong L$, but the key point of this definition is that the $L$ at each point can differ via nontrivial automorphisms. Then the differential map of this chain complex is defined, for a singular $k$-simplex $\sigma:\Delta^k \rightarrow M$ and a coefficient $a\in \mathcal{L}_{\sigma(e_0)}$, by

$$\partial_k(a\sigma)=\sum_{i=0}^k(-1)^k\mathcal{L}_{\sigma_k}(a) (\sigma\vert_{[v_0,\ldots, \hat{v}_i,\ldots,v_k]})$$

Here $\mathcal{L}_{\sigma_k}$ is obtained by applying the functor $\Pi_1(M) \rightarrow \Ab$ to the path in $M$ obtained by sending the edge joining the first vertex $\sigma(e_0)$ of the original simplex and the first vertex of the $k$th face. In nice cases such as our situation, we know that using the universal cover $\widetilde{M}$ of $M$ and the monodromy action (i.e., Deck transformation) on it, and the monodromy representation $\pi_1(X)\rightarrow \Aut(A)$, the chain complex

$$C(\widetilde{M})\otimes_{\mathbb{Z}[\pi_1(X)]} A$$

gives the same homology group as the above homology group.

This may be seen as somewhat excessive a generalization, because to describe the non-orientable version of Poincaré duality we will anyway set the local coefficient system $\mathcal{L}$ to be the constant sheaf $\underline{A}$. However, through this generalization we can also generalize the cohomology part, and this generalization makes Poincaré duality slightly more transparent.

For any topological space $X$ and a sheaf $\mathcal{F}$ defined on it, the global section functor

$$\Gamma(X,-):\Sh(X;\mathcal{A})\rightarrow \mathcal{A}$$

is a left exact functor, so its right derived functor exists. To compute this directly, we use the Godement resolution, which is defined as follows.

Consider a topological space $X$ and a sheaf $\mathcal{F}$ defined on it, and consider the étalé space $\Spe(\mathcal{F})$. We know that $\mathcal{F}$ is exactly the sheaf of continuous sections of $\Spe(\mathcal{F})\rightarrow X$. Now for any open set $U$ define

$$\mathcal{G}_0(U)=\prod_{x\in U}\mathcal{F}_x$$

That is, $\mathcal{G}_0$ is the sheaf of set-theoretic sections (not necessarily continuous) of $\Spe(\mathcal{F})\rightarrow X$. Our idea is to push into the quotient sheaf $\mathcal{Q}$ the cases where locally defined functions do not glue to a function, via the following sequence induced by the inclusion $\mathcal{F}\rightarrow \mathcal{G}_0$:

$$0 \rightarrow \mathcal{F}\rightarrow \mathcal{G}_0 \rightarrow \mathcal{Q}\rightarrow 0$$

Then for the sheaf $\mathcal{Q}$ as well, we can similarly make a sheaf defined by

$$\mathcal{G}_1(U)=\prod_{x\in U}\mathcal{Q}_x$$

and this defines the following *Godement resolution*

$$0 \rightarrow \mathcal{F}\rightarrow \mathcal{G}_0 \rightarrow \mathcal{G}_1\rightarrow \cdots$$

Intuitively, this repeatedly puts into $\mathcal{Q}$ the part that prevents global sections of $\Spe(\mathcal{F})$ from existing, and then into $\mathcal{Q}'$ the part that prevents global sections of $\mathcal{Q}$ from existing, and so on. This resolution $\mathcal{G}_\bullet$ is not an injective resolution, but because each sheaf is a flabby (flasque) sheaf, we can compute the right derived functors $R^i\Gamma$ of the global section functor through it.

::: Definition 15
For a topological space $X$ and a sheaf $\mathcal{F}$ defined on it, the $k$th homology of the sequence of global sections of the Godement resolution

$$0 \rightarrow \mathcal{F}(X)\rightarrow \mathcal{G}_0(X)\rightarrow \mathcal{G}_1(X)\rightarrow \cdots$$

is denoted by

$$H^k(X; \mathcal{F})$$

and is called *sheaf cohomology*.
:::

For more details on this, see [\[Algebraic Varieties\] §Sheaf Cohomology, ⁋Definition 1](/en/math/algebraic_varieties/sheaf_cohomology#def1). Poincaré duality is now generalized to the following isomorphism

$$H^k(M;\mathcal{L})\cong H_{m-k}(M;\or_M^A\otimes \mathcal{L})$$

To return to the original Poincaré duality from this, we first set $\mathcal{L}$ to the constant sheaf $\underline{A}$. Then in nice cases such as manifolds, it is known that sheaf cohomology $H^k(M;\underline{A})$ is isomorphic to singular cohomology $H^k(M;A)$, so we obtain the following isomorphism

$$H^k(M;A)\cong H_{m-k}(M;\or_M^A)$$

Additionally, if $M$ is $A$-orientable, then $\or_M^A$ also becomes a constant sheaf, and from this we can recover the classical Poincaré duality

$$H^k(M;A)\cong H_{m-k}(M;A)$$

## Poincaré Duality and Cup Product

Until now we have used the cup product on the cohomology ring and the cap product defined from it without hesitation. However, if someone asks *what* the cup product is, it would be difficult to answer. The answer is simple.

> The cup product is the Poincaré dual of intersection.

To explain precisely what this means would require at least as much additional effort as we have invested so far. However, examining what this means intuitively is probably sufficient with the following example.

::: Example 16
Consider the torus $T^2=S^1\times S^1$. Then from the Künneth formula we know that the cohomology of $T^2$ is

$$H^0(T^2;\mathbb{Z})\cong \mathbb{Z}, \quad H^1(T^2;\mathbb{Z})\cong \mathbb{Z}^2,\quad H^2(T^2;\mathbb{Z})$$

In this cohomology ring, the only non-trivial product is that of the two generators $\alpha,\beta$ of $H^1(T^2;\mathbb{Z})$. By [§Cohomology, ⁋Proposition 3](/en/math/algebraic_topology/cohomology#prop3), these correspond to the duals of the two circles of $T^2$. Then their cup product becomes the generator of $H^2(T^2;\mathbb{Z})$, which follows directly from the definition of cup product or algebraically from

$$H^2(T^2;\mathbb{Z})=H^1(T^2;\mathbb{Z})\otimes H^1(T^2;\mathbb{Z})\cong \mathbb{Z}\otimes \mathbb{Z}\cong \mathbb{Z}$$

being generated by $\alpha\otimes \beta$.

At this point, the reason why their cup product is not a non-unit constant multiple of $\alpha\times \beta$ is geometrically as follows. Letting $a,b$ be the homology classes corresponding to $\alpha,\beta$, the intersection of $a$ and $b$ meets at only one point, as shown in the following figure.

{% diagram Math/Algebraic_Topology/Poincare_Duality-5.svg width="30%" alt="Torus_intersection" %}

Here, classifying how the two curves meet and assigning one a positive direction and the other a negative direction is the same as giving an orientation of $T^2$.

Then under this geometric interpretation, how can we explain that $\alpha^2=0$? If we literally compute the intersection $a\cap a$, this becomes $a$ again. The reason this calculation gets tangled is that the two cycles (in this case, two copies of $a$) are not in *general position*. Roughly, if two arbitrary lines in $\mathbb{R}^2$ are given, they will generally meet at one point (except when they are parallel, including coincident); the notion of general position is a generalization of this.

Now consider curves on $T^2$ in the homology class $a$. Then they are likely not to meet each other, and if they do meet (excluding again the case of tangency, which is not general position), they will meet in the following shape

{% diagram Math/Algebraic_Topology/Poincare_Duality-6.svg width="40%" alt="intersections_on_torus" %}

At first glance this seems to produce two intersection points, but in the above figure the two intersection points have different signs; that is, for example, taking the line as the first vector and the curve as the second vector and computing the cross product, one would give a vector pointing outward and the other inward, so the signs are opposite. Thus the two intersection points cancel and their intersection becomes $0$, and hence $\alpha\smile\alpha=0$.
:::

--- 

**References**

[Hat] A. Hatcher, *Algebraic Topology*. Cambridge University Press, 2022.  
[May] J. P. May, *A concise course in algebraic topology*.
