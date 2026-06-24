---
title: "Poincaré Duality"
description: "We define Poincaré duality, a geometric duality between homology and cohomology on connected topological manifolds, through orientation sheaves and examine its structure."
excerpt: "Duality between homology and cohomology via orientation sheaves and fundamental classes"

categories: [Math / Algebraic Topology]
permalink: /en/math/algebraic_topology/Poincare_duality
sidebar: 
    nav: "algebraic_topology-en"

date: 2025-09-23
weight: 9
translated_at: 2026-06-24T03:30:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-24T03:30:02+00:00
---
In this post, we discuss Poincaré duality, a beautiful theorem of algebraic topology. As mentioned in the previous post, Poincaré duality exhibits a duality between homology and cohomology. The universal coefficient theorem we have already examined ([§Cohomology, ⁋Theorem 5](/en/math/algebraic_topology/cohomology#thm5)) was a somewhat predictable result when $C^\bullet(X;A)$ is defined as the dual of $C_\bullet(X;A)$, but Poincaré duality carries a deeper geometric meaning.

## Orientation Sheaf

To define Poincaré duality, we must first define the notion of orientation. This is a concept defined on a topological manifold ([§Topological Manifolds, ⁋Definition 2](/en/math/algebraic_topology/topological_manifolds#def2)); in this post, unless stated otherwise, we assume every manifold is *connected*.

Given any topological manifold $M$ of dimension $m$ and an open set $U$, the correspondence

$$U\mapsto H_m(M, M\setminus U;\mathbb{Z})$$

is a presheaf, because for any $U\subseteq V$ there is a natural restriction map

$$H_m(M, M\setminus V;\mathbb{Z})\rightarrow H_m(M,M\setminus U;\mathbb{Z})\tag{1}$$

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> The sheafification ([\[Topology\] §Sheaves, ⁋Definition 5](/en/math/topology/sheaves#def5)) of the correspondence (1) is called the *orientation sheaf* and denoted by $\or_M$.

</div>

Then for any $x\in M$ and any open neighborhood $U$ of $x$, there is a canonical map

$$H_m(M,M\setminus U;\mathbb{Z})\rightarrow H_m(M,M\setminus\{x\};\mathbb{Z})$$

These are compatible with the restriction maps above, and thus the map of direct limits

$$\or_{M,x}=\varinjlim_{x\in U} H_m(M,M\setminus U;\mathbb{Z})\rightarrow H_m(M,M\setminus \{x\};\mathbb{Z})$$

is well-defined.

By definition, an element of $H_m(M,M\setminus\{x\};\mathbb{Z})$ consists of $m$-simplices $\sigma:\Delta^m \rightarrow M$ whose boundary does not meet $x$, and we can choose a sufficiently small neighborhood $U$ of $x$ so that this boundary does not meet $U$. On the other hand, if two homology classes $\alpha_U\in H_m(M,M\setminus U;\mathbb{Z})$ and $\alpha_V\in H_m(M,M\setminus V;\mathbb{Z})$ represent the same element in $H_m(M,M\setminus \{x\};\mathbb{Z})$, then similarly we can find a sufficiently small open neighborhood $W$ of $x$ that meets the boundary of neither element, and then $\alpha_U$ and $\alpha_V$ must be the same element in $H_m(M,M\setminus W;\mathbb{Z})$. That is, the map

$$\varinjlim_{x\in U}H_m(M,M\setminus U;\mathbb{Z})\rightarrow H_m(M,M\setminus \{x\};\mathbb{Z})$$

is an isomorphism. Meanwhile, by [§Computation of Homology, ⁋Theorem 2](/en/math/algebraic_topology/computation_of_homology#thm2),

$$H_m(M,M\setminus\{x\};\mathbb{Z})\cong H_m(U,U\setminus\{x\};\mathbb{Z})\cong H_m(\mathbb{R}^m, \mathbb{R}^m\setminus\{0\};\mathbb{Z})$$

and since $\mathbb{R}^m\setminus\{0\}$ deformation retracts onto $S^{m-1}$, the relative homology long exact sequence shows that the right-hand side is isomorphic to $\mathbb{Z}$; we can also verify that this sheaf is locally constant. That is, for any given $x\in M$, there exists a suitable open neighborhood $U$ such that $\or_M\vert_U$ is a constant sheaf. ([\[Topology\] §Sheaves, ⁋Example 9](/en/math/topology/sheaves#ex9))

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> The relative homology group $H_m(M, M\setminus \{x\};\mathbb{Z})$ is called the *local homology group* of $M$ at $x$.

</div>

## Constant Sheaves and Covering Spaces, Orientation-Generator Sheaf

To examine the orientation sheaf $\or_M$ defined above in more detail, we need to look more closely at constant and locally constant sheaves. First, consider an arbitrary abelian group $A$, give it the discrete topology, and regard it as a topological space. Then the projection map $X\times A \rightarrow X$ is a trivial covering space, and the sheaf of sections of this covering map is precisely the constant sheaf $\underline{A}$. Conversely, given a constant sheaf $\underline{A}$, we can verify that its étale space $\Spe(\underline{A})$ is the covering space $X\times A \rightarrow X$. ([\[Topology\] §Presheaves](/en/math/topology/presheaves)) Thus a locally constant sheaf is nothing but a sheaf whose étale space is a covering space.

Intuitively, $H_m(M,M\setminus\{x\};\mathbb{Z})\cong \mathbb{Z}$ tells us how many times an $m$-simplex $\sigma:\Delta^m\rightarrow M$ containing $x$ in its interior covers $x$. Meanwhile, $\Delta^m$ can be given a sign depending on how its vertices are ordered, and through this isomorphism, when we assign elements of $\mathbb{Z}$ to such $m$-simplices, the sign difference between two $m$-simplices can be thought of as either the source $\Delta^m$ of the two $m$-simplices being given opposite orientations, or, with the sign of $\Delta^m$ fixed, the two simplex maps specifying different orientations. That is, $H_m(M,M\setminus\{x\};\mathbb{Z})$ contains information about the orientation at the point $x$.

A natural question is then whether, for every point $x\in M$, we can choose an orientation so that these orientations glue together to match a global orientation on $M$. For this, we first need a reference copy of $\mathbb{Z}$. To this end, fix a constant sheaf $\underline{\mathbb{Z}}$ on $M$. ([\[Topology\] §Presheaves, ⁋Example 6](/en/math/topology/presheaves#ex6)) Then for each $x\in M$, its stalk $\underline{\mathbb{Z}}_x$ can be thought of as having the generator $1$ chosen in a consistent manner, and thus choosing an isomorphism

$$\Iso_\mathbb{Z}(H_m(M, M\setminus\{x\}), \underline{\mathbb{Z}}_x)$$

for each $x$ is the same as choosing, for each $x$, whether $M$ is positively or negatively oriented at $x$.

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> For a topological manifold $M$ of dimension $m$, a *local orientation* at a point $x$ is given by choosing an element of $\Iso_\mathbb{Z}(H_m(M,M\setminus\{x\}), \underline{\mathbb{Z}}_x)$.

</div>

Now for each open set $U$, define

$$\omega_M^\pre(U)=\prod_{x\in U}\Iso_\mathbb{Z}(H_m(M,M\setminus\{x\}), \underline{\mathbb{Z}}_x)$$

and whenever $U\subseteq V$, define $\rho_{VU}:\omega_M^\pre(V)\rightarrow \omega_M^\pre(U)$ as the canonical projection. ([\[Set Theory\] §Properties of Products, ⁋Definition 1](/en/math/set_theory/property_of_products#def1)) Then $\omega_M^\pre$ becomes a presheaf on $M$ ([\[Topology\] §Presheaves, ⁋Definition 4](/en/math/topology/presheaves#def4)), and for each $p\in M$, the stalk $\omega_{M,x}^\pre$ of $\omega_M^\pre$ at $x$ is $\{\pm 1\}$. ([\[Topology\] §Presheaves, ⁋Definition 9](/en/math/topology/presheaves#def9))

The sheafification $\omega_M$ of $\omega_M^\pre$ is called the *orientation-generator sheaf* of $M$. Concretely, with a fixed generator $1$ of the constant sheaf $\underline{\mathbb{Z}}$ with a fixed orientation, one examines whether the isomorphism $H_m(M,M\setminus\{x\};\mathbb{Z})$ sends $1$ to $1$ or to $-1$; through this, $\omega_M$ can be viewed as a subsheaf of $\or_M$. Since $\omega_M$ is a locally constant sheaf, its étale space $\Spe(\omega_M)$ is a covering space of $M$ and each fiber consists of two elements.

<div class="definition" markdown="1">

<ins id="def4">**Definition 4**</ins> The étale space $\Spe(\omega_M)$ defined above is called the *orientation double cover* of $M$, and a global section $M \rightarrow \Spe(\omega_M)$ is called a *global orientation*. We say $M$ is *orientable* if a global orientation exists.

</div>

Then, as its name suggests, $\Spe(\omega_M)$ is a covering space of $M$, and moreover, for any $x\in M$, if we take a chart $U$ of $x$, the preimage $p^{-1}(U)$ of $U$ under the canonical projection $p:\Spe(\omega_M)\rightarrow M$ is the disjoint union of two open subsets, each homeomorphic to $U$.

<div class="example" markdown="1">

<ins id="ex5">**Example 5**</ins> Consider, for example, the orientation double cover $p:\Spe(\omega_{S^1})\rightarrow S^1$ of $S^1$. For any point $x\in S^1$, its preimage $p^{-1}(x)$ consists of two points $(x,+)$ and $(x,-)$, and the same holds for a chart $U$ containing $x$, so $p^{-1}(U)$ splits into two open subsets $U^+,U^-$.

![Orientation_cover_of_S1](/assets/images/Math/Algebraic_Topology/Poincare_Duality-1.svg){:style="width:45%" class="invert" .align-center}

If we cover $S^1$ with such charts and glue the orientations as they are at the overlaps, we obtain a double cover with two components as follows.

![Orientation_cover_of_S1_glued](/assets/images/Math/Algebraic_Topology/Poincare_Duality-2.svg){:style="width:45%" class="invert" .align-center}

However, not every double cover is trivial. For example, if in the above cover of $S^1$ we cross and glue the upper and lower components, we obtain a double cover with one component, and a similar phenomenon occurs in the orientation double cover of a non-orientable manifold.

To see this, consider the orientation cover of the Möbius strip $M$. As with $S^1$, for any point $x\in M$, $p^{-1}(x)$ consists of two points $(x,+)$ and $(x,-)$, and the same holds for any point of $M$.

![orientation_cover_of_M](/assets/images/Math/Algebraic_Topology/Poincare_Duality-3.svg){:style="width:40%" class="invert" .align-center}

However, if we try to glue these together to cover all of $M$, a problem arises: if we glue the two sheets shown in this figure in a counterclockwise direction, taking orientation into account, when we return to $x$, $(x,+)$ and $(x,-)$ have been swapped, so we must cross and glue the upper and lower components. The double cover of $M$ constructed in this way is homeomorphic to a cylinder.

</div>

By definition, for $M$ to be orientable, a global section of $\omega_M$ must exist, which is equivalent to $\Spe(\omega_M)$ being a trivial covering space, which in turn is equivalent to $\omega_M$ being a constant sheaf. Applying [§Covering Spaces, ⁋Corollary 12 (Fundamental theorem of covering spaces, classical version)](/en/math/algebraic_topology/covering_spaces#cor12) to this, we obtain the following proposition.

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6**</ins> For a (connected) topological manifold $M$, the following are equivalent.

1. $M$ is orientable.
2. $\Spe(\omega_M)$ has two components.
3. The monodromy action of $\pi_1(M)$ on $\Spe(\omega_M)$ is trivial.

</div>

Since we have already dealt with homology and cohomology not only over $\mathbb{Z}$-modules but also over general $A$-modules, the above argument can be extended to a general $A$-module. For this, first considering the relative homology version of [\[Algebraic Topology\] §Cohomology, ⁋Proposition 1](/en/math/algebraic_topology/cohomology#prop1), observe that the following (non-canonical) isomorphism exists:

$$H_k(M, M\setminus\{x\};A)\cong H_k(M,M\setminus\{x\})\otimes_\mathbb{Z}A\oplus\Tor_1^\mathbb{Z}(H_{k-1}(M, M\setminus\{x\}), A)$$

However, since $H_k(M,M\setminus \{x\})$ is always the trivial group when $k\neq m$, from this isomorphism we know

$$H_m(M,M\setminus \{x\};A)\cong H_m(M,M\setminus\{x\})\otimes_\mathbb{Z}A\cong A$$

Therefore, we could replace all the $\mathbb{Z}$ appearing in the above argument with $A$, and in particular we obtain the concept of a global $A$-orientation defined from the presheaf of $A$-orientations

$$\omega_M^A(U)=\prod_{x\in U}\Iso_A(H_m(M,M\setminus\{x\};A), \underline{A}_x)$$

The $A$-orientation sheaf $\omega_M^A$ obtained in this way is nothing but $\omega_M\otimes A$.

To derive a result analogous to [Proposition 6](#prop6) from this definition, let us revisit [§Covering Spaces, ⁋Theorem 11](/en/math/algebraic_topology/covering_spaces#thm11). For each covering space $p:E \rightarrow M$, we considered the $\pi_1(M,x)$-action defined by the monodromy functor on the fiber $p^{-1}(x)$, which was the same as considering a group homomorphism $\pi_1(M,x)\rightarrow \Aut(p^{-1}(x))$. Then for the covering space $p:\Spe(\omega_M)\rightarrow M$, we must examine how the $\pi_1(M,x)$-action is defined: the fiber $p^{-1}(x)$ is defined from the automorphism group of the stalk $\mathbb{Z}$

$$\Iso_\mathbb{Z}(\mathbb{Z},\mathbb{Z})\cong \mathbb{Z}^\times\cong \{\pm 1\}$$

and thus the $\pi_1(M,x)$-action can be thought of precisely as a group homomorphism $\pi_1(M,x)\rightarrow \mathbb{Z}^\times$. Since an $A$-module isomorphism from $A$ to $A$ corresponds exactly to an element of the unit group $A^\times$ of $A$, this is ultimately the same as examining a group homomorphism $\pi_1(M,x)\rightarrow A^\times$. That is, [Proposition 6](#prop6) can be generalized as follows.

<div class="proposition" markdown="1">

<ins id="prop7">**Proposition 7**</ins> For a (connected) topological manifold $M$, the following are equivalent.

1. $M$ is $A$-orientable.
2. $\Spe(\omega_M^A)$ is the trivial covering $M\times \lvert A^\times\rvert$.
3. The monodromy representation $\pi_1(M)\rightarrow A^\times$ is trivial.

</div>

The most notable case of this generalization is when $A=\mathbb{Z}/2$. In this case, the only unit of $A$ is $-1=1$, so the way to specify an orientation is unique, and thus any manifold is always $\mathbb{Z}/2$-orientable.

## Fundamental Class

Now we examine the existence of a global ($A$-)orientation. That is, given local orientations $s_x$ for all $x\in X$, we ask whether there exists a suitable global section $s:M\rightarrow \Spe(\omega_M^A)$ such that $s(x)=(x,s_x)$.

On the other hand, we know that through the canonical homomorphism

$$H_m(M; A)\rightarrow H_m(M,M\setminus\{x\};A)\tag{1}$$

any top homology class $\alpha\in H_m(M;A)$ defines an element $\alpha_x\in H_m(M,M\setminus\{x\};A)$ of the local homology group. Then one natural question is: when we regard the given local orientations $s_x$ for each $x\in S_x$ as elements of $A^\times$ and treat them as elements of $H_m(M,M\setminus\{x\};A)$, does there exist an $\alpha$ such that the image of $\alpha\in H_m(M;A)$ in $H_m(M,M\setminus\{x\};A)$ is $s_x$ for all $x\in X$.

The two paragraphs above illustrate the form that Poincaré duality takes. A global section $s:M \rightarrow \Spe(\omega_M^A)$ is essentially a function defined over all of $M$, corresponding to the notion of $0$th cohomology. On the other hand, $\alpha\in H_m(M;A)$ is an element of $m$th homology. Poincaré duality shows that these two notions are equivalent, and more generally, it exhibits a duality between $k$th cohomology and $(n-k)$th homology.

What remains for us to do in the rest of this post is essentially two things.

1. We show that a lifting of the canonical homomorphism (1) defines a global orientation, and conversely.
2. We define the *sheaf cohomology* in which a global orientation $M \rightarrow \Spe(\omega_M^A)$ exists.

The core content of Poincaré duality is all contained in the first step; the second step is closer to learning a language that can express this wisely. Therefore, we begin with the first step. This is obtained from the following lemma.

<div class="proposition" markdown="1">

<ins id="lem8">**Lemma 8**</ins> Fix a topological manifold $M$ of dimension $m$. For any compact subset $C$ of $M$, the following hold.

1. Given any section $s:M \rightarrow \Spe(\omega_M^A)$, there exists a unique homology class

    $$\alpha_C\in H_m(M,M\setminus C;A)$$

    such that for any $x\in C$, the image of $\alpha_C$ under the canonical homomorphism

    $$H_m(M,M\setminus C;A)\rightarrow H_m(M,M\setminus\{x\};A)$$

    is $s_x$.
2. For all $i>m$, $H_i(M, M\setminus C;A)=0$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, let us show that if the proposition holds for arbitrary compact sets $C_1,C_2$ and their intersection $C_1\cap C_2$, then it also holds for $C_1\cup C_2$. From the Mayer-Vietoris sequence

$$\cdots \rightarrow H_k(M,M\setminus (C_1\cup C_2); A)\rightarrow H_k(M,M\setminus C_1;A)\oplus H_k(M,M\setminus C_2;A)\rightarrow H_k(M, M\setminus (C_1\cap C_2);A)\rightarrow\cdots\tag{2}$$

for $k>m$, by the inductive hypothesis

$$H_k(M,M\setminus C_1;A)=H_k(M,M\setminus C_2;A)=H_k(M,M\setminus(C_1\cap C_2);A)=0$$

so $H_k(M,M\setminus (C_1\cup C_2);A)$ must also be $0$, and from this the second claim holds.

To show the first claim, suppose a section $s:M \rightarrow \Spe(\omega_M^A)$ is given. By the inductive hypothesis, liftings exist for $C_1,C_2,C_1\cap C_2$, so we must glue these to produce a class $\alpha_{C_1\cup C_2}$ for $C_1\cup C_2$. By the uniqueness of $\alpha_{C_1},\alpha_{C_2},\alpha_{C_1\cap C_2}$, both $\alpha_{C_1}$ and $\alpha_{C_2}$ must map to the same element from $\alpha_{C_1\cap C_2}$, so considering the element

$$(\alpha_{C_1},-\alpha_{C_2})\in H_m(M,M\setminus C_1;A)\oplus H_m(M,M\setminus C_2;A)$$

in (2), this element lies in the kernel of $H_m(M,M\setminus C_1;A)\oplus H_m(M,M\setminus C_2;A)\rightarrow H_m(M, M\setminus (C_1\cap C_2);A)$, and thus we can choose an element of $H_m(M,M\setminus (C_1\cup C_2);A)$; uniqueness comes from the injectivity of

$$0=H_{m+1}(M,M\setminus (C_1\cap C_2);A)\rightarrow H_m(M,M\setminus (C_1\cup C_2))\rightarrow H_m(M,M\setminus C_1;A)\oplus H_m(M,M\setminus C_2;A)$$

For the base step of the induction, it suffices to consider the case where $M=\mathbb{R}^m$ and $A$ is a convex compact subset. After covering an arbitrary compact set of any manifold $M$ with Euclidean charts, using compactness we may assume $M=\mathbb{R}^m$, and using the basis of open balls in $\mathbb{R}^m$ and again compactness, we may additionally assume $A$ is convex. Then at this step both spaces $\mathbb{R}^m\setminus A$ and $\mathbb{R}^m\setminus \{x\}$ deformation retract onto the same space $S^{m-1}$, so we obtain an isomorphism, and the proof is complete.

</details>

In this proof, compactness is absolutely necessary for the inductive construction of $\alpha$ using the Mayer-Vietoris sequence to terminate in finitely many steps. Indeed, if compactness is omitted, Poincaré duality takes a somewhat different form, and to express this in a unified formula we must introduce the language of sheaf cohomology.

In any case, by [Lemma 8](#lem8) above, if $M$ is a compact topological manifold of dimension $m$, then setting $C=M$ we obtain the following theorem.

<div class="proposition" markdown="1">

<ins id="thm9">**Theorem 9**</ins> Let $M$ be a compact connected topological manifold of dimension $m$. Then for each orientation sheaf $\omega_M^A$, there exists a unique class $[M]\in H_m(M;A)$ such that the image of $[M]$ under the canonical homomorphism (1) coincides with $s_x$.

</div>

Then by [Lemma 8](#lem8), $H_m(M;A)$ is a free $A$-module of rank 1 generated by $[M]$, and different choices of global orientation correspond to different choices of generators of $H_m(M;A)$.

<div class="definition" markdown="1">

<ins id="def10">**Definition 10**</ins> The class $[M]$ defined in [Theorem 9](#thm9) above is called the *fundamental class* of $M$ determined by the global orientation $s$.

</div>

Moreover, if a homology class $[M]$ satisfying the conditions of [Theorem 9](#thm9) exists, we know that a global section $s:M \rightarrow \Spe(\omega_M^A)$ is given from it.

## Poincaré Duality

Now we can prove the Poincaré theorem when the given manifold is $A$-orientable. For this, consider the cap product homomorphism

$$-\frown -: H^p(M;A)\otimes_A H_m(M;A) \rightarrow H_{m-p}(M;A)$$

Since $H_m(M;A)\cong A$, this homomorphism can be regarded as an $A$-module homomorphism from $H^p(M;A)$ to $H_{m-p}(M;A)$. In particular, introducing the generator $[M]$ of $H_m(M;A)$, this becomes the homomorphism

$$-\frown [M]: H^p(M;A)\rightarrow H_{m-p}(M;A)$$

<div class="proposition" markdown="1">

<ins id="thm11">**Theorem 11**</ins> For an $A$-orientable compact manifold $M$ of dimension $m$ and its fundamental class $[M]$, the above homomorphism

$$-\frown [M]: H^p(M;A)\rightarrow H_{m-p}(M;A)$$

is an isomorphism.

</div>

The proof of this also proceeds by induction using the Mayer-Vietoris sequence, just as in the proof of [Lemma 8](#lem8). However, there is a somewhat different point: in [Lemma 8](#lem8), the claim concerned a compact subset $C$, so compactness could be used aggressively, but this time the claim is about $M$ itself, so for example, if a chart $U$ of $M$ is given, this is not compact, and a simple inductive approach is not possible. For this, we define the following.

<div class="definition" markdown="1">

<ins id="def12">**Definition 12**</ins> A cochain $\varphi\in C^p(M;A)$ is said to be *compactly supported* if there exists a compact set $K\subseteq M$ such that $\varphi(\sigma)=0$ for all simplices contained in $M\setminus K$. We call the $i$th homology of the cochain complex of compactly supported cochains the $p$th *compactly supported cohomology* and denote it by $H_c^p(M;A)$.

</div>

Then the formula

$$H_c^p(M;A)\cong \varinjlim_{\text{\scriptsize$K$ compact}}H^p(M,M\setminus K;A)$$

is intuitively obvious and the proof is clear. For each compact set $K$,

$$H^p(M,M\setminus K;A)\rightarrow H_c^p(M;A)$$

exists canonically, and because this is compatible with the directed system on the right-hand side, the homomorphism

$$\varinjlim_{\text{\scriptsize$K$ compact}}H^p(M,M\setminus K;A)\rightarrow H_c^p(M;A)$$

is well-defined. That this is an isomorphism can be shown directly. In particular, for any compact manifold $M$, $H_c^p(M,A)\cong H^p(M;A)$ holds, and thus the desired result follows from the following lemma.

<div class="proposition" markdown="1">

<ins id="lem13">**Lemma 13**</ins> For any $A$-orientable $m$-manifold $M$, the isomorphism

$$H_c^p(M;A)\cong H_{m-p}(M;A)$$

holds for all $p$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

To do this, we must first define the isomorphism. For this, for any compact subset $K$, consider the cap product

$$H^p(M,M\setminus K;A)\times H_m(M,M\setminus K;A)\rightarrow H_{m-p}(M;A)$$

Then by [Lemma 8](#lem8), we can find a homology class

$$s_K\in H_m(M,M\setminus K;A)$$

that matches the orientation of $M$ when restricted to each point $x$. Our claim is that the cap product homomorphisms

$$-\frown s_K: H^p(M,M\setminus K;A) \rightarrow H_{m-p}(M;A)$$

made from such $s_K$ satisfy compatibility for the direct system, and thus define a homomorphism $H_c^p(M;A)\rightarrow H_{m-p}(M;A)$. To verify this, suppose another compact subset $K'$ containing $K$ and the inclusion $i:K\rightarrow K'$ are given. Then for any $\alpha\in H^p(M,M\setminus K;A)$,

$$i^\ast\alpha\frown s_{K'}=\alpha\frown i_\ast s_{K'}$$

holds by the projection formula ([§Cup Products, ⁋Proposition 6](/en/math/algebraic_topology/cup_products#prop6)), and by the uniqueness in [Lemma 8](#lem8), $i_\ast s_{K'}=s_K$, so we know that this defines the homomorphism $H_c^p(M;A)\rightarrow H_{n-p}(M;A)$ well.

Our claim is that this homomorphism $D_M:H_c^p(M;A)\rightarrow H_{n-p}(M;A)$ is an isomorphism, and to show this we use induction via the Mayer-Vietoris sequence as in the proof of [Lemma 8](#lem8).

The base step of the induction is the case $M=\mathbb{R}^m$. In this case, we know that for any ball $B\subseteq \mathbb{R}^m$, the orientation $s_B$ of $B$ gives

$$H_m(\mathbb{R}^m, \mathbb{R}^m\setminus B;A)\cong A$$

and from [§Cohomology, ⁋Proposition 3](/en/math/algebraic_topology/cohomology#prop3), $H^m(\mathbb{R}^m,\mathbb{R}^m\setminus B;A)\cong A$, and at this time the $\alpha_B$ corresponding to the dual basis of the orientation of $B$ satisfies the formula

$$\langle 1\smile \alpha_B, s_B\rangle=\langle 1,\alpha_B\frown s_B\rangle$$

so we know that $\alpha_B\frown s_B$ corresponds to the generator of $H_0(\mathbb{R}^m)\cong A$, and thus

$$H^p(\mathbb{R}^m,\mathbb{R}^m\setminus B;A)\cong H_{m-p}(\mathbb{R}^m;A)$$

holds for all $p$. (The case $p\neq m$ is an isomorphism between zero modules, i.e., a zero map.) Now by increasing the radius of $B$ and constructing a directed system covering all of $\mathbb{R}^m$, we know that $H_c^p(M)\rightarrow H_{m-p}(M)$ is an isomorphism.

For the next step, suppose there exist two open sets $U,V$ of $M$ such that $M=U\cap V$ and the given proposition holds for $U,V,U\cap V$. Then for each compact subset $K\subset U$, $L\subset V$, considering the relative Mayer-Vietoris sequence

$$\cdots\rightarrow H^k(M,M\setminus(K\cap L);A)\rightarrow H^k(M,M\setminus K;A)\oplus H^k(M,M\setminus L;A)\rightarrow H^k(M,M\setminus(K\cup L);A)\rightarrow \cdots$$

and then applying excision and taking limits, we obtain the following commutative diagram

![MVseq_duality](/assets/images/Math/Algebraic_Topology/Poincare_Duality-4.svg){:style="width:38.08em" class="invert" .align-center}

and the induction is completed by the inductive process and [\[Homological Algebra\] §Diagram Chasing, ⁋Corollary 2 (The five lemma)](/en/math/homological_algebra/diagram_chasing#cor2).

However, since there is no assumption that $M$ is compact, a slight additional argument is needed. First, suppose $M$ is the union of a nested family of open subsets

$$U_1\subset U_2\subset\cdots$$

and the given proposition holds for each of them. Then any compact subset of $M$ must be contained in some $U_i$, and from this we obtain the isomorphisms

$$H_c^p(M)=\varinjlim_i H^p_c(U_i),\qquad H_{m-p}(M)=\varinjlim_i H_{m-p}(U_i)$$

By assumption, the $H^p_c(U_i)\rightarrow H_{m-p}(U_i)$ are all isomorphisms, so we obtain the desired result.

Now consider the case where $M$ is an open subset of $\mathbb{R}^m$. Then first we can cover $M$ with countably many convex open subsets (i.e., open balls) $U_1,U_2,\ldots$ homeomorphic to $\mathbb{R}^m$, and since any convex open subset is homeomorphic to $\mathbb{R}^m$, we saw in the base step above that the theorem's isomorphism holds for each of them. Also, since the intersection of two convex sets is again convex, by the induction above, the conclusion also holds for $U_1\cup U_2$. To show that the conclusion holds next for $U_1\cup U_2\cup U_3$, we must show that the following intersection

$$(U_1\cup U_2)\cap U_3=(U_1\cap U_3)\cup (U_2\cap U_3)$$

satisfies the given condition, but at this time $U_1\cap U_3$, $U_2\cap U_3$, and $U_1\cap U_2\cap U_3$ are all convex open subsets of $\mathbb{R}^m$ satisfying the given condition. In a similar manner, we know that each of

$$U_1,\quad U_1\cup U_2, \quad U_1\cup U_2\cup U_3,\quad \cdots$$

satisfies the conclusion. Therefore, applying the preceding (infinite) induction to the sequence of nested open subsets

$$U_1\subset U_1\cup U_2\subset U_1\cup U_2\cup U_3\cdots$$

we obtain the desired result.

Finally, for the case where $M$ is an arbitrary manifold, using second countability, cover $M$ with countably many Euclidean charts and proceed with the same argument as above.

</details>

In particular, in the proof, if $M$ were itself compact, the duality map $D_M$ would have been exactly the cap product with the fundamental class $[M]$.

## Twisted Poincaré Duality

When $M$ is not $A$-orientable, the main reason [Theorem 11](#thm11) fails is that, fundamentally, $\or_M^A$ fails to be a constant sheaf and is only locally constant. In the language of covering spaces, this can be thought of as the monodromy action acting nontrivially on the stalk $A$, so that when we go "around once," the stalk $A$ gets twisted back onto itself. This twist is an automorphism of $A$, so to see this, it sufficed to consider the bijection of the unit group $A^\times$ of $A$.

Now to incorporate this twist into the duality, we define *homology with local coefficients*.

<div class="definition" markdown="1">

<ins id="def14">**Definition 14**</ins> A locally constant sheaf $\mathscr{L}$ defined on $M$ is called a *local coefficient system*.

</div>

Let the stalk of the local system $\mathscr{L}$ be $L$. Then by [§Covering Spaces, ⁋Theorem 11](/en/math/algebraic_topology/covering_spaces#thm11), we know that for any path $\alpha:[0,1]\rightarrow M$, there exists an isomorphism between stalks $\mathscr{L}_{\alpha(0)}\rightarrow \mathscr{L}_{\alpha(1)}$. This is nothing but the isomorphism obtained by lifting the path $\alpha$ in the covering space $\Spe(\mathscr{L})\rightarrow M$. That is, we obtain the following functor

$$\Pi_1(M)\rightarrow \Ab; \qquad x\mapsto \mathscr{L}_x$$

Then fixing one point $e_0=(1,0,\ldots,0)$ of $\Delta^k$, we define $C_\bullet(M,\mathscr{L})$ by

$$C_\bullet(M,\mathscr{L})=\bigoplus_{\sigma:\Delta^k\rightarrow M}\mathscr{L}_{\sigma(e_0)}$$

After all, for each $x$, $\mathscr{L}_x\cong L$, but the key point of this definition is that the $L$ at each point can differ through nontrivial automorphisms. Then the differential map of this chain complex is defined, for a singular $k$-simplex $\sigma:\Delta^k \rightarrow M$ and a coefficient $a\in \mathscr{L}_{\sigma(e_0)}$, by

$$\partial_k(a\sigma)=\sum_{i=0}^k(-1)^k\mathscr{L}_{\sigma_k}(a) (\sigma\vert_{[v_0,\ldots, \hat{v}_i,\ldots,v_k]})$$

Here, $\mathscr{L}_{\sigma_k}$ is obtained by applying the functor $\Pi_1(M) \rightarrow \Ab$ to the path obtained by sending to $M$ the edge connecting the first vertex $\sigma(e_0)$ of the original simplex and the first vertex of the $k$th face. In good cases like our situation, we can also consider the chain complex obtained by constructing

$$C(\widetilde{M})\otimes_{\mathbb{Z}[\pi_1(X)]} A$$

using the universal cover $\widetilde{M}$ of $M$ and the monodromy action (i.e., Deck transformation) on it, and the monodromy representation $\pi_1(X)\rightarrow \Aut(A)$, and we know that this gives the same homology group as the above.

This may be seen as somewhat excessive generalization, because to describe the non-orientable version of Poincaré duality we will set the local coefficient system $\mathscr{L}$ to the constant sheaf $\underline{A}$ anyway. However, through this generalization we can also generalize the cohomology part, and this generalization makes Poincaré duality slightly more transparent.

For any topological space $X$ and a sheaf $\mathscr{F}$ defined on it, the global section functor

$$\Gamma(X,-):\Sh(X,\mathcal{A})\rightarrow \mathcal{A}$$

is left exact, so its right derived functor exists. To compute this directly, we use the Godement resolution, which is defined as follows.

Consider a topological space $X$ and a sheaf $\mathscr{F}$ defined on it, and the étalé space $\Spe(\mathscr{F})$. We know that $\mathscr{F}$ is exactly the sheaf of continuous sections of $\Spe(\mathscr{F})\rightarrow X$. Now for any open set $U$, define

$$\mathscr{G}_0(U)=\prod_{x\in U}\mathscr{F}_x$$

That is, $\mathscr{G}_0$ is the sheaf of set-theoretic sections (not necessarily continuous) of $\Spe(\mathscr{F})\rightarrow X$. Our idea is that, when locally defined functions fail to glue together to form a function, we push this failure into the quotient sheaf $\mathscr{Q}$ via the inclusion $\mathscr{F}\rightarrow \mathscr{G}_0$ through the sequence

$$0 \rightarrow \mathscr{F}\rightarrow \mathscr{G}_0 \rightarrow \mathscr{Q}\rightarrow 0$$

Then for the sheaf $\mathscr{Q}$ as well, we can similarly define a sheaf

$$\mathscr{G}_1(U)=\prod_{x\in U}\mathscr{Q}_x$$

and this defines the *Godement resolution*

$$0 \rightarrow \mathscr{F}\rightarrow \mathscr{G}_0 \rightarrow \mathscr{G}_1\rightarrow \cdots$$

Intuitively, this repeatedly puts the part that prevents $\Spe(\mathscr{F})$ from having a global section into $\mathscr{Q}$, and then the part that prevents $\mathscr{Q}$ from having a global section into $\mathscr{Q}'$, and so on. This resolution $\mathscr{G}_\bullet$ is not an injective resolution, but because each sheaf is flabby (flasque), we can compute the right derived functors $R^i\Gamma$ of the global section functor through it.

<div class="definition" markdown="1">

<ins id="def15">**Definition 15**</ins> For a topological space $X$ and a sheaf $\mathscr{F}$ defined on it, the $k$th homology of the sequence of global sections of the Godement resolution

$$0 \rightarrow \mathscr{F}(X)\rightarrow \mathscr{G}_0(X)\rightarrow \mathscr{G}_1(X)\rightarrow \cdots$$

is denoted

$$H^k(X; \mathscr{F})$$

and called *sheaf cohomology*.

</div>

For more details on this, see [\[Algebraic Varieties\] §Sheaf Cohomology, ⁋Definition 1](/en/math/algebraic_varieties/sheaf_cohomology#def1). Now Poincaré duality is generalized to the isomorphism

$$H^k(M;\mathscr{L})\cong H_{m-k}(M;\or_M^A\otimes \mathscr{L})$$

To return to the original Poincaré duality from this, we first set $\mathscr{L}$ to the constant sheaf $\underline{A}$. Then in good cases like manifolds, it is known that sheaf cohomology $H^k(M;\underline{A})$ and singular cohomology $H^k(M;A)$ are isomorphic, so we obtain the isomorphism

$$H^k(M;A)\cong H_{m-k}(M;\or_M^A)$$

Additionally, if $M$ is $A$-orientable, then $\or_M^A$ also becomes a constant sheaf, so from this we can recover the classical Poincaré duality

$$H^k(M;A)\cong H_{m-k}(M;A)$$

## Poincaré Duality and Cup Product

Until now, we have used the cup product on the cohomology ring and the cap product defined from it without hesitation. However, if someone asks what the cup product *is*, it would be difficult to answer. The answer is simple.

> Cup product is the Poincaré dual of intersection.

To explain precisely what this means requires at least as much effort as we have invested so far. However, examining what this means intuitively is probably sufficient with the following example.

<div class="example" markdown="1">

<ins id="ex16">**Example 16**</ins> Consider the torus $T^2=S^1\times S^1$. From the Künneth formula, we know that the cohomology of $T^2$ is

$$H^0(T^2;\mathbb{Z})\cong \mathbb{Z}, \quad H^1(T^2;\mathbb{Z})\cong \mathbb{Z}^2,\quad H^2(T^2;\mathbb{Z})$$

In this cohomology ring, the only non-trivial product is the product of the two generators $\alpha,\beta$ of $H^1(T^2;\mathbb{Z})$. By [§Cohomology, ⁋Proposition 3](/en/math/algebraic_topology/cohomology#prop3), these correspond to the duals of the two circles of $T^2$. Then taking their cup product gives the generator of $H^2(T^2;\mathbb{Z})$, which follows directly from the definition of cup product or algebraically from

$$H^2(T^2;\mathbb{Z})=H^1(T^2;\mathbb{Z})\otimes H^1(T^2;\mathbb{Z})\cong \mathbb{Z}\otimes \mathbb{Z}\cong \mathbb{Z}$$

being generated by $\alpha\otimes \beta$.

At this time, the reason why the cup product of these is not a constant multiple other than $\pm 1$ of $\alpha\times \beta$ is geometrically as follows. Let the homology classes corresponding to $\alpha$, $\beta$ be $a,b$; then $a$ and $b$ intersect at only one point, as shown in the following figure.

![Torus_intersection](/assets/images/Math/Algebraic_Topology/Poincare_Duality-5.svg){:style="width:30%" class="invert" .align-center}

At this time, classifying how the two curves meet and defining one as positive direction and one as negative direction is the same as giving an orientation of $T^2$.

Then under this geometric interpretation, how can we explain that $\alpha^2=0$? If we literally compute the intersection $a\cap a$, this becomes $a$ again. The reason this calculation gets tangled is that the two cycles (in this case, two copies of $a$) are not in *general position*. Roughly, if two arbitrary lines in $\mathbb{R}^2$ are given, they will generally meet at one point (except when they are parallel, including the case of coincidence), and the concept of general position is a generalization of this.

Now consider curves in $T^2$ whose homology class is $a$. Then they are likely not to meet each other, and if they do meet (excluding again the case of general position, i.e., tangency), they will meet in the following shape

![intersections_on_torus](/assets/images/Math/Algebraic_Topology/Poincare_Duality-6.svg){:style="width:40%" class="invert" .align-center}

At first glance, this seems to create two intersection points, but in the above figure, the two intersection points have different signs; that is, for example, if we take the line as the first vector and the curve as the second vector and take the cross product, one will give a vector pointing outward and the other a vector pointing inward, and thus the signs are opposite. Thus the two intersection points cancel each other out, so their intersection becomes $0$, and therefore $\alpha\smile\alpha=0$.

</div>

--- 

**References**

[Hat] A. Hatcher, *Algebraic Topology*. Cambridge University Press, 2022.  
[May] J. P. May, *A concise course in algebraic topology*.

---
