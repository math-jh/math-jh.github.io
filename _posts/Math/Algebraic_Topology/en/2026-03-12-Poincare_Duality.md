---
title: "Poincaré Duality"
description: "We define Poincaré duality, a geometric duality between homology and cohomology on connected topological manifolds, through orientation sheaves and examine its structure."
excerpt: "Duality between homology and cohomology via orientation sheaves and fundamental classes"

categories: [Math / Algebraic Topology]
permalink: /en/math/algebraic_topology/Poincare_duality
sidebar: 
    nav: "algebraic_topology-en"

date: 2025-09-23
weight: 12
translated_at: 2026-08-18T16:15:05+00:00
translation_source: kimi-cli
last_polished_at: 2026-08-18T16:15:05+00:00
---
In this post we discuss Poincaré duality, a beautiful theorem of algebraic topology. As mentioned in the previous post, Poincaré duality exhibits a duality between homology and cohomology. The case of [§Cohomology, ⁋Theorem 5](/en/math/algebraic_topology/cohomology#thm5), which we have already examined, was somewhat expected when $C^\bullet(X;A)$ was defined as the dual of $C_\bullet(X;A)$, but Poincaré duality carries a deeper geometric meaning.

## Orientation Sheaf

To define Poincaré duality, we must first define the notion of orientation. This is a concept defined on a topological manifold ([§Topological Manifolds, ⁋Definition 2](/en/math/algebraic_topology/topological_manifolds#def2)); in this post, unless stated otherwise, we assume every manifold is *connected*.

Given any topological manifold $M$ of dimension $m$ and an open set $U$, the assignment

$$U\mapsto H_m(M, M\setminus U;\mathbb{Z})\tag{1}$$

carries a natural restriction map

$$H_m(M, M\setminus V;\mathbb{Z})\rightarrow H_m(M,M\setminus U;\mathbb{Z})$$

for every $U\subseteq V$, and hence forms a presheaf.

::: Definition 1
The sheafification of the assignment (1) is called the *orientation sheaf* and is denoted $\or_M$. ([\[Topology\] §Sheaves, ⁋Definition 5](/en/math/topology/sheaves#def5))
:::

Then for any $x\in M$ and any open neighborhood $U$ of $x$, there is a canonical map

$$H_m(M,M\setminus U;\mathbb{Z})\rightarrow H_m(M,M\setminus\{x\};\mathbb{Z}).$$

These are compatible with the restriction maps above, and therefore induce a map of direct limits

$$\or_{M,x}=\varinjlim_{x\in U} H_m(M,M\setminus U;\mathbb{Z})\rightarrow H_m(M,M\setminus \{x\};\mathbb{Z})$$

that is well defined.

By definition, an element of $H_m(M,M\setminus\{x\};\mathbb{Z})$ is represented by an $m$-simplex $\sigma:\Delta^m \rightarrow M$ whose boundary does not meet $x$; then we can choose a sufficiently small neighborhood $U$ of $x$ so that this boundary does not meet $U$ either. On the other hand, if two homology classes $\alpha_U\in H_m(M,M\setminus U;\mathbb{Z})$ and $\alpha_V\in H_m(M,M\setminus V;\mathbb{Z})$ represent the same element in $H_m(M,M\setminus \{x\};\mathbb{Z})$, we can likewise find a sufficiently small open neighborhood $W$ of $x$ meeting neither boundary, and then $\alpha_U$ and $\alpha_V$ must agree in $H_m(M,M\setminus W;\mathbb{Z})$. Thus the map

$$\varinjlim_{x\in U}H_m(M,M\setminus U;\mathbb{Z})\rightarrow H_m(M,M\setminus \{x\};\mathbb{Z})$$

is an isomorphism. Moreover, by [§Computing Homology, ⁋Theorem 2](/en/math/algebraic_topology/computation_of_homology#thm2),

$$H_m(M,M\setminus\{x\};\mathbb{Z})\cong H_m(U,U\setminus\{x\};\mathbb{Z})\cong H_m(\mathbb{R}^m, \mathbb{R}^m\setminus\{0\};\mathbb{Z}),$$

and since $\mathbb{R}^m\setminus\{0\}$ deformation retracts onto $S^{m-1}$, the long exact sequence of relative homology shows that the right-hand side is isomorphic to $\mathbb{Z}$. One can also verify that this sheaf is locally constant: for every $x\in M$ there exists a suitable open neighborhood $U$ such that $\or_M\vert_U$ is a constant sheaf. ([\[Topology\] §Sheaves, ⁋Example 9](/en/math/topology/sheaves#ex9))

::: Definition 2
The relative homology group $H_m(M, M\setminus \{x\};\mathbb{Z})$ is called the *local homology group* at $x\in M$.
:::

## Constant Sheaves, Covering Spaces, and Orientation-Generator Sheaves

To examine the orientation sheaf $\or_M$ defined above in more detail, we need to look more closely at constant and locally constant sheaves. First, consider an arbitrary abelian group $A$ equipped with the discrete topology, regarded as a topological space. Then the projection $X\times A \rightarrow X$ is a trivial covering space, and the sheaf of sections of this covering map is precisely the constant sheaf $\underline{A}$. Conversely, given a constant sheaf $\underline{A}$, one can check that its étale space $\Spe(\underline{A})$ is the covering space $X\times A \rightarrow X$. ([\[Topology\] §Presheaves](/en/math/topology/presheaves)) Thus a locally constant sheaf is nothing more than a sheaf whose étale space is a covering space.

Intuitively, $H_m(M,M\setminus\{x\};\mathbb{Z})\cong \mathbb{Z}$ records how many times an $m$-simplex $\sigma:\Delta^m\rightarrow M$ having $x$ in its interior covers $x$. On the other hand, $\Delta^m$ can be given a sign depending on how an ordering is assigned to its vertices; then via this isomorphism, when we assign an element of $\mathbb{Z}$ to such $m$-simplices, the sign difference between two $m$-simplices can be interpreted as either their sources $\Delta^m$ being assigned opposite orientations, or, fixing the orientation of $\Delta^m$, the two simplex maps specifying different directions. In other words, $H_m(M,M\setminus\{x\};\mathbb{Z})$ encodes information about the orientation at the point $x$.

Then a natural question is whether, for every point $x\in M$, we can choose an orientation so that these orientations patch together to yield a global orientation on $M$. For this we first need a reference copy of $\mathbb{Z}$. Fix a constant sheaf $\underline{\mathbb{Z}}$ on $M$. ([\[Topology\] §Sheaves, ⁋Example 9](/en/math/topology/sheaves#ex9)) Then for each $x\in M$, its stalk $\underline{\mathbb{Z}}_x$ can be thought of as having the generator $1$ chosen in a consistent manner, and thus choosing an isomorphism

$$\Iso_\mathbb{Z}(H_m(M, M\setminus\{x\}), \underline{\mathbb{Z}}_x)$$

for each $x$ amounts to choosing, at each $x$, whether $M$ is positively or negatively oriented.

::: Definition 3
For a topological manifold $M$ of dimension $m$, a *local orientation* at a point $x$ is given by choosing an element of $\Iso_\mathbb{Z}(H_m(M,M\setminus\{x\}), \underline{\mathbb{Z}}_x)$.
:::

What matters here is not picking local orientations arbitrarily at each point, but choosing them so that the selections fit together locally. To this end, for each open set $U$ define

$$\omega_M(U)=\{s\in \or_M(U)\mid s_x \text{ generates } \or_{M,x} \text{ for all } x\in U\},$$

with the restriction map inherited from $\or_M$. At each $x\in M$, the stalk $\or_{M,x}$ is $H_m(M,M\setminus\{x\};\mathbb{Z})\cong\mathbb{Z}$, so choosing its generator is the same as choosing a local orientation in the sense of [Definition 3](#def3), i.e., an isomorphism $H_m(M,M\setminus\{x\};\mathbb{Z})\rightarrow \underline{\mathbb{Z}}_x$. Since whether a germ is a generator is a condition checked pointwise, the gluing procedure for sections of $\or_M$ works just as well, and hence $\omega_M$ is a subsheaf of $\or_M$. Moreover, on an open neighborhood $U$ where $\or_M\vert_U$ is a constant sheaf, sections of $\or_M$ are given by locally constant functions, so a germ that is a generator at $x$ remains a generator on a sufficiently small neighborhood of $x$; consequently, the stalk $\omega_{M,x}$ of $\omega_M$ at $x$ is the set of generators of $\or_{M,x}$, namely $\{\pm 1\}$. ([\[Topology\] §Presheaves, ⁋Definition 9](/en/math/topology/presheaves#def9))

This $\omega_M$ is called the *orientation-generator sheaf* of $M$. When the orientation of the constant sheaf $\underline{\mathbb{Z}}$ is fixed and its generator $1$ is chosen, this sheaf records, at each $x$, whether the isomorphism $H_m(M,M\setminus\{x\};\mathbb{Z})\rightarrow\underline{\mathbb{Z}}_x$ sends $1$ to $1$ or to $-1$, by examining which choice arises from a local section of $\or_M$. Then, on a neighborhood $U$ as above, $\omega_M\vert_U$ is the constant sheaf on $\{\pm 1\}$, so $\omega_M$ is also locally constant; therefore its étale space $\Spe(\omega_M)$ is a covering space of $M$ with two-element fibers.

::: Definition 4
The étale space $\Spe(\omega_M)$ defined above is called the *orientation double cover* of $M$, and a global section $M \rightarrow \Spe(\omega_M)$ is called a *global orientation*. We say $M$ is *orientable* if a global orientation exists.
:::

As its name suggests, $\Spe(\omega_M)$ is a covering space of $M$; moreover, for any $x\in M$, taking a chart $U$ of $x$, the preimage $p^{-1}(U)$ under the canonical projection $p:\Spe(\omega_M)\rightarrow M$ splits into two disjoint open subsets each homeomorphic to $U$.

::: Example 5
For instance, consider the orientation double cover $p:\Spe(\omega_{S^1})\rightarrow S^1$ of $S^1$. For any point $x\in S^1$, its preimage $p^{-1}(x)$ consists of two points $(x,+)$ and $(x,-)$, and the same holds for any chart $U$ containing $x$, so $p^{-1}(U)$ splits into two open subsets $U^+,U^-$.

{% diagram Math/Algebraic_Topology/Poincare_Duality-1.svg width="45%" alt="Orientation_cover_of_S1" %}

Now, if we cover $S^1$ by such charts and glue them together preserving orientation, we obtain a double cover with two components as follows.

{% diagram Math/Algebraic_Topology/Poincare_Duality-2.svg width="45%" alt="Orientation_cover_of_S1_glued" %}

However, not every double cover is trivial. For example, if in the above cover of $S^1$ we cross-glue the upper and lower components, we obtain a double cover with a single component; a similar phenomenon occurs for the orientation double cover of a non-orientable manifold.

To observe this, consider the orientation cover of the Möbius strip $M$. Just as for $S^1$, for any point $x\in M$ the fiber $p^{-1}(x)$ consists of two points $(x,+)$ and $(x,-)$, and this is true for every point of $M$.

{% diagram Math/Algebraic_Topology/Poincare_Duality-3.svg width="40%" alt="orientation_cover_of_M" %}

But attempting to glue these together over all of $M$ runs into a problem: if we glue the two covers shown in this figure while respecting orientation, proceeding counterclockwise, then upon returning to $x$ the points $(x,+)$ and $(x,-)$ have been interchanged, so we must cross-glue the upper and lower components. The resulting double cover of $M$ is homeomorphic to a cylinder.
:::

By definition, $M$ is orientable if and only if $\omega_M$ admits a global section, which is equivalent to $\Spe(\omega_M)$ being a trivial covering space, which in turn is equivalent to $\omega_M$ being a constant sheaf. Applying [§Covering Spaces, ⁋Corollary 12 (Fundamental theorem of covering spaces, classical version)](/en/math/algebraic_topology/covering_spaces#cor12), we obtain the following proposition.

::: Proposition 6
For a (connected) topological manifold $M$, the following are equivalent.

1. $M$ is orientable.
2. $\Spe(\omega_M)$ has two components.
3. The monodromy action of $\pi_1(M)$ on $\Spe(\omega_M)$ is trivial.
:::

However, since we have already extended homology and cohomology from $\mathbb{Z}$-modules to general $A$-modules, the above argument can also be extended to a general $A$-module. To this end, first consider the relative homology version of [§Cohomology, ⁋Proposition 1](/en/math/algebraic_topology/cohomology#prop1); observe that there is a (non-canonical) isomorphism

$$H_k(M, M\setminus\{x\};A)\cong H_k(M,M\setminus\{x\})\otimes_\mathbb{Z}A\oplus\Tor_1^\mathbb{Z}(H_{k-1}(M, M\setminus\{x\}), A).$$

Since $H_k(M,M\setminus \{x\})$ is trivial for $k\neq m$, from this isomorphism we obtain

$$H_m(M,M\setminus \{x\};A)\cong H_m(M,M\setminus\{x\})\otimes_\mathbb{Z}A\cong A.$$

Hence the above argument remains valid if we replace every occurrence of $\mathbb{Z}$ by $A$; in particular, we obtain the notion of $A$-orientations via the presheaf

$$\omega_M^A(U)=\prod_{x\in U}\Iso_A(H_m(M,M\setminus\{x\};A), \underline{A}_x)$$

and the global $A$-orientation defined from it. The resulting $A$-orientation sheaf $\omega_M^A$ is nothing other than $\or_M\otimes A$.

To derive a result analogous to [Proposition 6](#prop6) from this definition, let us revisit [§Covering Spaces, ⁋Theorem 11](/en/math/algebraic_topology/covering_spaces#thm11). For each covering space $p:E \rightarrow M$, we considered the $\pi_1(M,x)$-action on the fiber $p^{-1}(x)$ defined by the monodromy functor, which was the same as giving a group homomorphism $\pi_1(M,x)\rightarrow \Aut(p^{-1}(x))$. Then for the covering space $p:\Spe(\omega_M)\rightarrow M$, we must examine how the $\pi_1(M,x)$-action is defined: the fiber $p^{-1}(x)$ is determined by the automorphisms of the stalk $\mathbb{Z}$,

$$\Iso_\mathbb{Z}(\mathbb{Z},\mathbb{Z})\cong \mathbb{Z}^\times\cong \{\pm 1\},$$

and thus the $\pi_1(M,x)$-action can be identified precisely with a group homomorphism $\pi_1(M,x)\rightarrow \mathbb{Z}^\times$. Now, $A$-module isomorphisms from $A$ to $A$ correspond exactly to elements of the unit group $A^\times$, so this ultimately amounts to examining a group homomorphism $\pi_1(M,x)\rightarrow A^\times$. That is, [Proposition 6](#prop6) generalizes as follows.

::: Proposition 7
For a (connected) topological manifold $M$, the following are equivalent.

1. $M$ is $A$-orientable.
2. $\Spe(\omega_M^A)$ is the trivial covering $M\times \lvert A^\times\rvert$.
3. The monodromy representation $\pi_1(M)\rightarrow A^\times$ is trivial.
:::

The most notable case of this generalization is $A=\mathbb{Z}/2$. In this case, the only unit of $A$ is $-1=1$, so there is a unique way to specify an orientation, and hence every manifold is always $\mathbb{Z}/2$-orientable.

## Fundamental Class

We now examine the existence of a global ($A$-)orientation. That is, given local orientations $s_x$ for all $x\in M$, we ask whether there exists a global section $s:M\rightarrow \Spe(\omega_M^A)$ such that $s(x)=(x,s_x)$.

On the other hand, we know that via the canonical homomorphism

$$H_m(M; A)\rightarrow H_m(M,M\setminus\{x\};A)\tag{2}$$

any top homology class $\alpha\in H_m(M;A)$ defines an element $\alpha_x\in H_m(M,M\setminus\{x\};A)$ in the local homology group. Then one natural question is whether, regarding the given local orientations $s_x$ at each $x\in M$ as elements of $A^\times$ and hence as elements of $H_m(M,M\setminus\{x\};A)$, there exists $\alpha\in H_m(M;A)$ whose image in $H_m(M,M\setminus\{x\};A)$ equals $s_x$ for every $x\in M$.

The two paragraphs above illustrate the shape of Poincaré duality. A global section $s:M \rightarrow \Spe(\omega_M^A)$ is essentially a function defined over all of $M$, corresponding to the notion of $0$th cohomology. On the other hand, $\alpha\in H_m(M;A)$ is an element of $m$th homology. Poincaré duality states that these two notions are equivalent, and, more generally, it exhibits a duality between $k$th cohomology and $(m-k)$th homology.

For the remainder of this post, our task splits into two main parts.

1. Show that a lift of the canonical homomorphism (2) defines a global orientation, and conversely.
2. Define the language of *sheaf cohomology* that can express the existence of a global orientation $M \rightarrow \Spe(\omega_M^A)$.

The core content of Poincaré duality lies entirely in the first step; the second step is closer to learning a language that expresses this result elegantly. Therefore we begin with the first step, which is obtained via the following lemma.

::: Lemma 8
Fix a topological manifold $M$ of dimension $m$. For any compact subset $C$ of $M$, the following hold.

1. Given any section $s:M \rightarrow \Spe(\omega_M^A)$, there exists a unique homology class
    
    $$\alpha_C\in H_m(M,M\setminus C;A)$$

    such that for every $x\in C$, the image of $\alpha_C$ under the canonical homomorphism

    $$H_m(M,M\setminus C;A)\rightarrow H_m(M,M\setminus\{x\};A)$$

    is $s_x$.
2. For all $i>m$, we have $H_i(M, M\setminus C;A)=0$.
:::
::: Proof
First, we show that if the statement holds for arbitrary compact sets $C_1,C_2$ and their intersection $C_1\cap C_2$, then it also holds for $C_1\cup C_2$. From the Mayer–Vietoris sequence

$$\cdots \rightarrow H_k(M,M\setminus (C_1\cup C_2); A)\rightarrow H_k(M,M\setminus C_1;A)\oplus H_k(M,M\setminus C_2;A)\rightarrow H_k(M, M\setminus (C_1\cap C_2);A)\rightarrow\cdots\tag{3}$$

for $k>m$, the inductive hypothesis gives

$$H_k(M,M\setminus C_1;A)=H_k(M,M\setminus C_2;A)=H_k(M,M\setminus(C_1\cap C_2);A)=0,$$

so $H_k(M,M\setminus (C_1\cup C_2);A)$ must also be $0$, which yields the second claim.

To prove the first claim, suppose a section $s:M \rightarrow \Spe(\omega_M^A)$ is given. By the inductive hypothesis, lifts exist for $C_1$, $C_2$, and $C_1\cap C_2$, so we must glue these together to produce a class $\alpha_{C_1\cup C_2}$ for $C_1\cup C_2$. By the uniqueness of $\alpha_{C_1}$, $\alpha_{C_2}$, and $\alpha_{C_1\cap C_2}$, both $\alpha_{C_1}$ and $\alpha_{C_2}$ must map to the same element from $\alpha_{C_1\cap C_2}$; hence, considering the element

$$(\alpha_{C_1},-\alpha_{C_2})\in H_m(M,M\setminus C_1;A)\oplus H_m(M,M\setminus C_2;A)$$

in (3), this element lies in the kernel of the map $H_m(M,M\setminus C_1;A)\oplus H_m(M,M\setminus C_2;A)\rightarrow H_m(M, M\setminus (C_1\cap C_2);A)$, and therefore we can pick an element of $H_m(M,M\setminus (C_1\cup C_2);A)$. Uniqueness follows from the injectivity of

$$0=H_{m+1}(M,M\setminus (C_1\cap C_2);A)\rightarrow H_m(M,M\setminus (C_1\cup C_2))\rightarrow H_m(M,M\setminus C_1;A)\oplus H_m(M,M\setminus C_2;A).$$

For the base case of the induction, it suffices to consider $M=\mathbb{R}^m$ with $C$ a convex compact subset. Covering an arbitrary compact set in any manifold $M$ by Euclidean charts and using compactness, we may assume $M=\mathbb{R}^m$; and inside $\mathbb{R}^m$ it is enough to look at finite unions $K$ of closed balls containing $C$. For the maps induced by the inclusions $\mathbb{R}^m\setminus K\subseteq\mathbb{R}^m\setminus C$, we have

$$\varinjlim_{K\supseteq C}H_i(\mathbb{R}^m,\mathbb{R}^m\setminus K;A)\cong H_i(\mathbb{R}^m,\mathbb{R}^m\setminus C;A).$$

Indeed, these maps are induced by the inclusions $\mathbb{R}^m\setminus K\hookrightarrow \mathbb{R}^m\setminus C$, i.e. by $C\hookrightarrow K$, so for this to be an isomorphism the maps induced by each $C\hookrightarrow K$ must be isomorphisms. Since singular chains are always compact by definition, this always holds. Then in this base case both spaces $\mathbb{R}^m\setminus C$ and $\mathbb{R}^m\setminus \{x\}$ deformation retract onto the same space $S^{m-1}$, giving the isomorphism, and the proof is complete.
:::

In this proof, compactness is essential for the inductive construction of $\alpha$ via the Mayer–Vietoris sequence to terminate in finitely many steps. If compactness is dropped, Poincaré duality takes a somewhat different form, and the language of sheaf cohomology is what is needed to express it in a unified formula.

At any rate, by [Lemma 8](#lem8) above, if $M$ is a compact topological manifold of dimension $m$, then taking $C=M$ yields the following theorem.

::: Theorem 9
Let $M$ be a compact connected topological manifold of dimension $m$. Then for every global orientation $s:M \rightarrow \Spe(\omega_M^A)$, there exists a unique class $[M]\in H_m(M;A)$ whose image under the canonical homomorphism (2) coincides with $s_x$.
:::

Then by [Lemma 8](#lem8), $H_m(M;A)$ is the free $A$-module of rank 1 generated by $[M]$, and different choices of global orientation correspond to different choices of generator of $H_m(M;A)$.

::: Definition 10
We call the class $[M]$ defined in [Theorem 9](#thm9) above the *fundamental class* of $M$ determined by the global orientation $s$.
:::

Moreover, if a homology class $[M]$ satisfying the condition of [Theorem 9](#thm9) exists, then it gives rise to a global section $s:M \rightarrow \Spe(\omega_M^A)$.

## Poincaré Duality

We can now prove Poincaré's theorem when the given manifold is $A$-orientable. To this end, consider the cap product homomorphism

$$-\frown -: H^p(M;A)\otimes_A H_m(M;A) \rightarrow H_{m-p}(M;A).$$

Since $H_m(M;A)\cong A$, this homomorphism may be regarded as an $A$-module homomorphism from $H^p(M;A)$ to $H_{m-p}(M;A)$. In particular, introducing a generator $[M]$ of $H_m(M;A)$, this becomes the homomorphism

$$-\frown [M]: H^p(M;A)\rightarrow H_{m-p}(M;A).$$

::: Theorem 11
For an $A$-orientable compact manifold $M$ of dimension $m$ and its fundamental class $[M]$, the above homomorphism

$$-\frown [M]: H^p(M;A)\rightarrow H_{m-p}(M;A)$$

is an isomorphism.
:::

The proof again proceeds by induction using the Mayer–Vietoris sequence, just as in the proof of [Lemma 8](#lem8). The difference, however, is that in [Lemma 8](#lem8) the claim concerned a compact subset $C$, so compactness could be used actively, whereas now the claim is about $M$ itself. Thus, for instance, if a chart $U$ of $M$ is given, it is not compact, so a simple inductive approach does not work. For this we make the following definition.

::: Definition 12
A cochain $\varphi\in C^p(M;A)$ is said to be *compactly supported* if there exists a compact set $K\subseteq M$ such that $\varphi(\sigma)=0$ for every simplex lying in $M\setminus K$. The $p$-th cohomology of the cochain complex of compactly supported cochains is called the $p$-th *compactly supported cohomology*, denoted $H_c^p(M;A)$.
:::

Then we have the identity

$$H_c^p(M;A)\cong \varinjlim_{\text{\scriptsize$K$ compact}}H^p(M,M\setminus K;A).$$

For each compact set $K$, the canonical map

$$H^p(M,M\setminus K;A)\rightarrow H_c^p(M;A)$$

exists, and it is compatible with the directed system on the right-hand side, so the homomorphism

$$\varinjlim_{\text{\scriptsize$K$ compact}}H^p(M,M\setminus K;A)\rightarrow H_c^p(M;A)$$

is well defined. That this is actually an isomorphism can be checked at the cochain level. Intuitively, the $K$'s are the supports of cochains, and since a finite union of compact sets is again compact, their collection forms a directed system; taking the direct limit, i.e. the union, is an exact functor, so it commutes with taking cohomology. In particular, for any compact manifold $M$ we have $H_c^p(M;A)\cong H^p(M;A)$, and hence the desired result follows from the next lemma.

::: Lemma 13
For any $A$-orientable $m$-manifold $M$, the isomorphism

$$H_c^p(M;A)\cong H_{m-p}(M;A)$$

holds for all $p$.
:::
::: Proof
To establish this, we must first define the isomorphism. For this, for any compact subset $K$, consider the cap product

$$H^p(M,M\setminus K;A)\times H_m(M,M\setminus K;A)\rightarrow H_{m-p}(M;A).$$

Then by [Lemma 8](#lem8), for each point $x$ we can find a homology class

$$s_K\in H_m(M,M\setminus K;A)$$

that matches the orientation $s_x$ of $M$ when restricted to $x$. Our claim is that the cap product homomorphisms

$$-\frown s_K: H^p(M,M\setminus K;A) \rightarrow H_{m-p}(M;A)$$

constructed from these $s_K$ satisfy the compatibility condition for the direct system, and therefore define a homomorphism $H_c^p(M;A)\rightarrow H_{m-p}(M;A)$. To verify this, suppose another compact subset $K'$ containing $K$ and the inclusion $i:K\rightarrow K'$ are given. Then for any $\alpha\in H^p(M,M\setminus K;A)$,

$$i^\ast\alpha\frown s_{K'}=\alpha\frown i_\ast s_{K'}$$

holds by [§Cup Product, ⁋Proposition 6](/en/math/algebraic_topology/cup_products#prop6), and by the uniqueness in [Lemma 8](#lem8) we have $i_\ast s_{K'}=s_K$, so we see that this defines the homomorphism $H_c^p(M;A)\rightarrow H_{m-p}(M;A)$ well.

Our claim is that this homomorphism $D_M:H_c^p(M;A)\rightarrow H_{m-p}(M;A)$ is an isomorphism, and to show this we use induction via the Mayer–Vietoris sequence, just as in the proof of [Lemma 8](#lem8).

The base step of the induction is the case $M=\mathbb{R}^m$. In this case, we know that for any ball $B\subseteq \mathbb{R}^m$, the orientation $s_B$ of $B$ gives

$$H_m(\mathbb{R}^m, \mathbb{R}^m\setminus B;A)\cong A,$$

and from [§Cohomology, ⁋Proposition 3](/en/math/algebraic_topology/cohomology#prop3) we have $H^m(\mathbb{R}^m,\mathbb{R}^m\setminus B;A)\cong A$; at this point, the element $\alpha_B$ corresponding to the dual basis of the orientation of $B$ satisfies

$$\langle 1\smile \alpha_B, s_B\rangle=\langle 1,\alpha_B\frown s_B\rangle,$$

so we know that $\alpha_B\frown s_B$ corresponds to a generator of $H_0(\mathbb{R}^m)\cong A$, and therefore

$$H^p(\mathbb{R}^m,\mathbb{R}^m\setminus B;A)\cong H_{m-p}(\mathbb{R}^m;A)$$

holds for all $p$. (For $p\neq m$ this is the zero map between zero modules, hence an isomorphism.) Now, increasing the radius of $B$ to cover all of $\mathbb{R}^m$, we obtain a directed system and see that $H_c^p(M)\rightarrow H_{m-p}(M)$ is an isomorphism.

For the next step, suppose there exist two open subsets $U,V$ of $M$ such that $M=U\cup V$ and the given statement holds for $U$, $V$, and $U\cap V$. Then for each compact subset $K\subseteq U$, $L\subseteq V$, consider the relative Mayer–Vietoris sequence

$$\cdots\rightarrow H^k(M,M\setminus(K\cap L);A)\rightarrow H^k(M,M\setminus K;A)\oplus H^k(M,M\setminus L;A)\rightarrow H^k(M,M\setminus(K\cup L);A)\rightarrow \cdots$$

and after excision and taking the limit, we obtain the following diagram

{% diagram Math/Algebraic_Topology/Poincare_Duality-4.svg width="39.02em" alt="MVseq_duality" %}

In this diagram, the square involving the connecting homomorphism may fail to commute up to sign, so it is only commutative when signs are ignored; however, signs are not needed to apply [\[Homological Algebra\] §Diagram chasing, ⁋Corollary 2 (The five lemma)](/en/math/homological_algebra/diagram_chasing#cor2), so the inductive step completes the induction.

However, since we do not assume $M$ is compact, a little extra argument is needed. First, suppose $M$ is the union of a nested family of open subsets

$$U_1\subseteq U_2\subseteq\cdots$$

and that the given statement holds for each of them. Then any compact subset of $M$ must be contained in some $U_i$, and from this we obtain the isomorphisms

$$H_c^p(M)=\varinjlim_i H^p_c(U_i),\qquad H_{m-p}(M)=\varinjlim_i H_{m-p}(U_i).$$

Since by assumption the maps $H^p_c(U_i)\rightarrow H_{m-p}(U_i)$ are all isomorphisms, we obtain the desired result.

Now consider the case where $M$ is an open subset of $\mathbb{R}^m$. Then we can first cover $M$ by countably many convex open subsets (i.e. open balls) $U_1,U_2,\ldots$ homeomorphic to $\mathbb{R}^m$, and since any convex open subset is homeomorphic to $\mathbb{R}^m$, we saw in the base step above that the theorem's isomorphism holds for each of them. Also, the intersection of two convex sets is again convex, so by the above induction the conclusion holds for $U_1\cup U_2$ as well. To show next that the conclusion holds for $U_1\cup U_2\cup U_3$, we must verify that the intersection

$$(U_1\cup U_2)\cap U_3=(U_1\cap U_3)\cup (U_2\cap U_3)$$

satisfies the given condition; here $U_1\cap U_3$, $U_2\cap U_3$, and $U_1\cap U_2\cap U_3$ are all convex open subsets of $\mathbb{R}^m$, so they satisfy the given condition. Similarly, we see that each of

$$U_1,\quad U_1\cup U_2, \quad U_1\cup U_2\cup U_3,\quad \cdots$$

satisfies the conclusion. Therefore, applying the preceding (infinite) induction to the sequence of nested open subsets

$$U_1\subseteq U_1\cup U_2\subseteq U_1\cup U_2\cup U_3\cdots$$

yields the desired result.

Finally, if $M$ is an arbitrary manifold, using second countability we cover $M$ by countably many Euclidean charts and run the same argument as above.
:::

In particular, from the proof, if $M$ itself were compact, then the duality map $D_M$ would have been exactly the cap product with the fundamental class $[M]$.

## Twisted Poincaré Duality

When $M$ is not $A$-orientable, the main reason [Theorem 11](#thm11) fails is that, fundamentally, $\omega_M^A$ fails to be a constant sheaf and is only locally constant. In the language of covering spaces, this can be thought of as the monodromy action acting nontrivially on the stalk $A$, so that after going "once around" the stalk $A$ becomes twisted upon returning. Since this twist is an automorphism of $A$, it was enough for us to consider elements of the unit group $A^\times$ of $A$.

To account for this twist in duality, we now define *homology with local coefficients*.

::: Definition 14
A locally constant sheaf $\mathcal{L}$ defined on $M$ is called a *local coefficient system*. 
:::

Let $L$ be the stalk of a local system $\mathcal{L}$. Then by [§Covering Spaces, ⁋Theorem 11](/en/math/algebraic_topology/covering_spaces#thm11), we know that for any path $\alpha:[0,1]\rightarrow M$, there exists an isomorphism $\mathcal{L}_{\alpha(0)}\rightarrow \mathcal{L}_{\alpha(1)}$ between stalks. This is nothing other than the isomorphism obtained by lifting the path $\alpha$ in the covering space $\Spe(\mathcal{L})\rightarrow M$. That is, we obtain the following functor

$$\Pi_1(M)\rightarrow \Ab; \qquad x\mapsto \mathcal{L}_x$$

Then fixing a point $e_0=(1,0,\ldots,0)$ of $\Delta^k$, we define $C_\bullet(M,\mathcal{L})$ by the formula

$$C_k(M,\mathcal{L})=\bigoplus_{\sigma:\Delta^k\rightarrow M}\mathcal{L}_{\sigma(e_0)}$$

After all, $\mathcal{L}_x\cong L$ for each $x$, but the key point of this definition is that the $L$ at each point may differ via a nontrivial automorphism. Then the differential map of this chain complex is defined, for a singular $k$-simplex $\sigma:\Delta^k \rightarrow M$ and a coefficient $a\in \mathcal{L}_{\sigma(e_0)}$, by

$$\partial_k(a\sigma)=\sum_{i=0}^k(-1)^i\mathcal{L}_{\sigma_i}(a) (\sigma\vert_{[v_0,\ldots, \hat{v}_i,\ldots,v_k]})$$

Here $\mathcal{L}_{\sigma_i}$ is obtained by applying the functor $\Pi_1(M) \rightarrow \Ab$ to the path in $M$ obtained by sending the edge joining the first vertex $\sigma(e_0)$ of the original simplex and the first vertex of the $i$-th face. In nice situations like ours, we know that using the universal cover $\widetilde{M}$ of $M$, the monodromy action (i.e., Deck transformation) on it, and the monodromy representation $\pi_1(M)\rightarrow \Aut(A)$, the chain complex

$$C(\widetilde{M})\otimes_{\mathbb{Z}[\pi_1(M)]} A$$

gives the same homology group as the one above.

This may be seen as somewhat of an excessive generalization, but to describe the non-orientable version of Poincaré duality we will in any case take the local coefficient system $\mathcal{L}$ to be the constant sheaf $\underline{A}$. However, through this generalization we can also generalize the cohomology part, and this generalization makes Poincaré duality somewhat more transparent.

For any topological space $X$ and a sheaf $\mathcal{F}$ defined on it, the global section functor 

$$\Gamma(X,-):\Sh(X;\mathcal{A})\rightarrow \mathcal{A}$$

is a left exact functor, so its right derived functors exist. To compute these directly, one uses the Godement resolution, which is defined as follows.

Consider a topological space $X$ and a sheaf $\mathcal{F}$ defined on it, and consider the étalé space $\Spe(\mathcal{F})$. We know that $\mathcal{F}$ is precisely the sheaf of continuous sections of $\Spe(\mathcal{F})\rightarrow X$. Now for any open set $U$, define

$$\mathcal{G}_0(U)=\prod_{x\in U}\mathcal{F}_x$$

That is, $\mathcal{G}_0$ is the sheaf of set-theoretic sections of $\Spe(\mathcal{F})\rightarrow X$ (not necessarily continuous). Our idea is that the cases where functions defined locally fail to glue into a function are pushed into the quotient sheaf $\mathcal{Q}$ via the inclusion $\mathcal{F}\rightarrow \mathcal{G}_0$ in the following sequence

$$0 \rightarrow \mathcal{F}\rightarrow \mathcal{G}_0 \rightarrow \mathcal{Q}\rightarrow 0$$

Then for the sheaf $\mathcal{Q}$ as well, we can similarly construct a sheaf defined by

$$\mathcal{G}_1(U)=\prod_{x\in U}\mathcal{Q}_x$$

and this defines the following *Godement resolution*

$$0 \rightarrow \mathcal{F}\rightarrow \mathcal{G}_0 \rightarrow \mathcal{G}_1\rightarrow \cdots$$

Intuitively, this repeatedly captures the part preventing $\Spe(\mathcal{F})$ from having a global section into $\mathcal{Q}$, and then the part preventing $\mathcal{Q}$ from having a global section into $\mathcal{Q}'$, and so on. This resolution $\mathcal{G}_\bullet$ is not an injective resolution, but each sheaf is a flabby (flasque) sheaf, so we can compute the right derived functors $R^i\Gamma$ of the global section functor via it.

::: Definition 15
For a topological space $X$ and a sheaf $\mathcal{F}$ defined on it, the $k$-th cohomology of the sequence of global sections of the Godement resolution

$$0 \rightarrow \mathcal{G}_0(X)\rightarrow \mathcal{G}_1(X)\rightarrow \cdots$$

is denoted

$$H^k(X; \mathcal{F})$$

and is called *sheaf cohomology*.
:::

For more details on this, see [\[Algebraic Varieties\] §Sheaf Cohomology, ⁋Definition 1](/en/math/algebraic_varieties/sheaf_cohomology#def1). Now if $M$ is compact, Poincaré duality generalizes to the following isomorphism

$$H^k(M;\mathcal{L})\cong H_{m-k}(M;\omega_M^A\otimes \mathcal{L})$$

To return to the original Poincaré duality, we first take $\mathcal{L}$ to be the constant sheaf $\underline{A}$. Then in nice cases such as manifolds, it is known that sheaf cohomology $H^k(M;\underline{A})$ and singular cohomology $H^k(M;A)$ are isomorphic, so we obtain the following isomorphism

$$H^k(M;A)\cong H_{m-k}(M;\omega_M^A)$$

Furthermore, if $M$ is $A$-orientable, then $\omega_M^A$ also becomes a constant sheaf, and from this we can recover the classical Poincaré duality

$$H^k(M;A)\cong H_{m-k}(M;A)$$

## Poincaré Duality and Cup Product

So far we have used the cup product on the cohomology ring and the cap product defined from it without hesitation. However, if someone asks *what* the cup product is, it would be difficult to answer. The answer is simple.

> The cup product is the Poincaré dual of intersection.

To explain precisely what this means requires at least as much effort as we have invested so far. However, to see intuitively what this means, the following example will probably suffice.

::: Example 16
Consider the torus $T^2=S^1\times S^1$. Then from the Künneth formula we know that the cohomology of $T^2$ is

$$H^0(T^2;\mathbb{Z})\cong \mathbb{Z}, \quad H^1(T^2;\mathbb{Z})\cong \mathbb{Z}^2,\quad H^2(T^2;\mathbb{Z})\cong \mathbb{Z}$$

The only non-trivial product in this cohomology ring is the product of two generators $\alpha,\beta$ of $H^1(T^2;\mathbb{Z})$. By [§Cohomology, ⁋Proposition 3](/en/math/algebraic_topology/cohomology#prop3), these correspond to the duals of two circles on $T^2$. Then taking their cup product gives a generator of $H^2(T^2;\mathbb{Z})$, which is immediate from the definition of cup product or algebraically from

$$H^2(T^2;\mathbb{Z})=H^1(S^1;\mathbb{Z})\otimes H^1(S^1;\mathbb{Z})\cong \mathbb{Z}\otimes \mathbb{Z}\cong \mathbb{Z}$$

being generated by $\alpha\otimes \beta$.

At this point, the reason the cup product of these does not appear as a constant multiple other than $\pm 1$ of $\alpha\times \beta$ is geometrically as follows. Letting $a,b$ be the homology classes corresponding to $\alpha,\beta$, the intersection of $a$ and $b$ meets at only one point, as shown in the following figure.

{% diagram Math/Algebraic_Topology/Poincare_Duality-5.svg width="30%" alt="Torus_intersection" %}

Here, classifying how the two curves meet and assigning one as positive direction and the other as negative direction is the same as giving an orientation of $T^2$.

Then under this geometric interpretation, how can we explain that $\alpha^2=0$? If we compute the intersection $a\cap a$ literally, this becomes $a$ again. The reason this computation gets tangled is that the two cycles (in this case, two copies of $a$) are not in *general position*. Roughly, given any two lines in $\mathbb{R}^2$, they will generally meet at one point (except when they are parallel, including the coincident case), and the notion of general position generalizes this.

Now consider curves on $T^2$ whose homology class is $a$. Then they will most likely not meet each other, and if they do (again excluding the non-general position case of tangency), they will meet in the following shape

{% diagram Math/Algebraic_Topology/Poincare_Duality-6.svg width="40%" alt="intersections_on_torus" %}

At first glance this seems to produce two intersection points, but in the figure above the two intersections have opposite signs; that is, for example taking the line as the first vector and the curve as the second vector and computing the cross product, one will give a vector pointing outward and the other a vector pointing inward, so the signs are opposite. Thus the two intersection points cancel and their intersection becomes $0$, and therefore $\alpha\smile\alpha=0$.
:::

--- 

**References**

**[Hat]** A. Hatcher, *Algebraic Topology*. Cambridge University Press, 2022.  
**[May]** J. P. May, *A concise course in algebraic topology*.

---
