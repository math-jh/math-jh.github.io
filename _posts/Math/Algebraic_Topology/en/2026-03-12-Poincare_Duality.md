---
title: "Poincaré Duality"
excerpt: "Duality between homology and cohomology via orientation sheaves and fundamental classes"

categories: [Math / Algebraic Topology]
permalink: /en/math/algebraic_topology/Poincare_duality
sidebar: 
    nav: "algebraic_topology-en"

date: 2026-03-12
last_modified_at: 2026-03-12
weight: 9
translated_at: 2026-05-29T02:00:58+00:00
translation_source: kimi-cli
last_polished_at: 2026-05-25T18:00:04+00:00
---
In this post we discuss Poincaré duality, one of the most beautiful theorems of algebraic topology. As mentioned previously, Poincaré duality reveals a duality between homology and cohomology. The universal coefficient theorem ([§Cohomology, ⁋Theorem 5](/en/math/algebraic_topology/cohomology#thm5)) gave a result that was more or less expected once we defined $$C^\bullet(X;A)$$ as the dual of $$C_\bullet(X;A)$$; Poincaré duality, by contrast, carries a far more geometric meaning.

## Orientation Sheaf

To define Poincaré duality we must first define the notion of orientation. This is a concept defined on a topological manifold ([§Topological Manifolds, ⁋Definition 2](/en/math/algebraic_topology/topological_manifolds#def2)); throughout this post, unless stated otherwise, we assume every manifold is *connected*.

Let $$M$$ be a topological manifold of dimension $$m$$ and let $$U$$ be an open set. The correspondence

$$U\mapsto H_m(M, M\setminus U;\mathbb{Z})$$

is a presheaf, since for any $$U\subseteq V$$ there is a natural restriction map

$$H_m(M, M\setminus V;\mathbb{Z})\rightarrow H_m(M,M\setminus U;\mathbb{Z})\tag{1}$$

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> The sheafification ([\[Topology\] §Sheaves, ⁋Definition 5](/en/math/topology/sheaves#def5)) of the correspondence (1) is called the *orientation sheaf* and is denoted by $$\or_M$$.

</div>

For any $$x\in M$$ and any open neighborhood $$U$$ of $$x$$, the canonical map

$$H_m(M,M\setminus U;\mathbb{Z})\rightarrow H_m(M,M\setminus\{x\};\mathbb{Z})$$

exists. These maps are compatible with the restriction maps above, and hence the direct-limit map

$$\or_{M,x}=\varinjlim_{x\in U} H_m(M,M\setminus U;\mathbb{Z})\rightarrow H_m(M,M\setminus \{x\};\mathbb{Z})$$

is well-defined.

By definition, an element of $$H_m(M,M\setminus\{x\};\mathbb{Z})$$ is represented by an $$m$$-simplex $$\sigma:\Delta^m \rightarrow M$$ whose boundary avoids $$x$$, and we can choose a sufficiently small neighborhood $$U$$ of $$x$$ so that this boundary avoids $$U$$ as well. Conversely, if two homology classes $$\alpha_U\in H_m(M,M\setminus U;\mathbb{Z})$$ and $$\alpha_V\in H_m(M,M\setminus V;\mathbb{Z})$$ become the same element in $$H_m(M,M\setminus \{x\};\mathbb{Z})$$, then we can likewise find a sufficiently small open neighborhood $$W$$ of $$x$$ avoiding the boundaries of both elements, and then $$\alpha_U$$ and $$\alpha_V$$ must coincide in $$H_m(M,M\setminus W;\mathbb{Z})$$. Thus the map

$$\varinjlim_{x\in U}H_m(M,M\setminus U;\mathbb{Z})\rightarrow H_m(M,M\setminus \{x\};\mathbb{Z})$$

is an isomorphism. Moreover, by [§Computation of Homology, ⁋Theorem 2](/en/math/algebraic_topology/computation_of_homology#thm2),

$$H_m(M,M\setminus\{x\};\mathbb{Z})\cong H_m(U,U\setminus\{x\};\mathbb{Z})\cong H_m(\mathbb{R}^m, \mathbb{R}^m\setminus\{0\};\mathbb{Z})$$

and since $$\mathbb{R}^m\setminus\{0\}$$ deformation retracts onto $$S^{m-1}$$, the relative homology long exact sequence shows that the right-hand side is isomorphic to $$\mathbb{Z}$$. One also verifies that this sheaf is locally constant: for every $$x\in M$$ there exists an open neighborhood $$U$$ such that $$\or_M\vert_U$$ is a constant sheaf. ([\[Topology\] §Sheaves, ⁋Example 9](/en/math/topology/sheaves#ex9))

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> The relative homology group $$H_m(M, M\setminus \{x\};\mathbb{Z})$$ is called the *local homology group* of $$M$$ at $$x$$.

</div>

## Constant Sheaves, Covering Spaces, and the Orientation-Generator Sheaf

To examine the orientation sheaf $$\or_M$$ in more detail, we need a closer look at constant and locally constant sheaves. First, consider an arbitrary abelian group $$A$$ equipped with the discrete topology, regarded as a topological space. The projection $$X\times A \rightarrow X$$ is then a trivial covering space, and the sheaf of sections of this covering map is precisely the constant sheaf $$\underline{A}$$. Conversely, given a constant sheaf $$\underline{A}$$, one verifies that its étale space $$\Spe(\underline{A})$$ is the covering space $$X\times A \rightarrow X$$. ([\[Topology\] §Presheaves, ⁋Definition 9](/en/math/topology/presheaves#def9)) Hence a locally constant sheaf is nothing more than a sheaf whose étale space is a covering space.

Intuitively, the isomorphism $$H_m(M,M\setminus\{x\};\mathbb{Z})\cong \mathbb{Z}$$ records how many times an $$m$$-simplex $$\sigma:\Delta^m\rightarrow M$$ containing $$x$$ in its interior covers $$x$$. Since $$\Delta^m$$ can be assigned a sign according to the ordering of its vertices, and through this isomorphism we may associate elements of $$\mathbb{Z}$$ to such $$m$$-simplices, the sign difference between two $$m$$-simplices can be interpreted either as their common source $$\Delta^m$$ being oppositely oriented, or, with the orientation of $$\Delta^m$$ fixed, as the two simplex maps specifying opposite directions. Thus $$H_m(M,M\setminus\{x\};\mathbb{Z})$$ encodes the orientation at the point $$x$$.

A natural question arises: can we assign an orientation to every point $$x\in M$$ in such a way that these orientations patch together to yield a global orientation on $$M$$? To do so we first need a reference copy of $$\mathbb{Z}$$; fix a constant sheaf $$\underline{\mathbb{Z}}$$ on $$M$$. ([\[Topology\] §Presheaves, ⁋Example 6](/en/math/topology/presheaves#ex6)) For each $$x\in M$$ we may think of the stalk $$\underline{\mathbb{Z}}_x$$ as having its generator $$1$$ chosen in a consistent manner, and therefore choosing an isomorphism

$$\Iso_\mathbb{Z}(H_m(M, M\setminus\{x\}), \underline{\mathbb{Z}}_x)$$

for each $$x$$ is equivalent to choosing whether $$M$$ is positively or negatively oriented at $$x$$.

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> For a topological manifold $$M$$ of dimension $$m$$, a *local orientation* at a point $$x$$ is given by choosing an element of $$\Iso_\mathbb{Z}(H_m(M,M\setminus\{x\}), \underline{\mathbb{Z}}_x)$$.

</div>

Now define, for each open set $$U$$,

$$\omega_M^\pre(U)=\prod_{x\in U}\Iso_\mathbb{Z}(H_m(M,M\setminus\{x\}), \underline{\mathbb{Z}}_x)$$

and for each $$U\subseteq V$$, define $$\rho_{VU}:\omega_M^\pre(V)\rightarrow \omega_M^\pre(U)$$ to be the canonical projection. ([\[Set Theory\] §Properties of Products, ⁋Definition 1](/en/math/set_theory/property_of_products#def1)) Then $$\omega_M^\pre$$ is a presheaf on $$M$$ ([\[Topology\] §Presheaves, ⁋Definition 4](/en/math/topology/presheaves#def4)), and for each $$p\in M$$ the stalk $$\omega_{M,x}^\pre$$ at the point $$x$$ is $$\{\pm 1\}$$. ([\[Topology\] §Presheaves, ⁋Definition 9](/en/math/topology/presheaves#def9))

The sheafification $$\omega_M$$ of $$\omega_M^\pre$$ is called the *orientation-generator sheaf* of $$M$$. Fixing the generator $$1$$ of the oriented constant sheaf $$\underline{\mathbb{Z}}$$, this sheaf records whether the isomorphism $$H_m(M,M\setminus\{x\};\mathbb{Z})\cong\mathbb{Z}$$ sends $$1$$ to $$1$$ or to $$-1$$; through this observation $$\omega_M$$ may be viewed as a subsheaf of $$\or_M$$. Since $$\omega_M$$ is locally constant, its étale space $$\Spe(\omega_M)$$ is a covering space of $$M$$ whose every fiber consists of two points.

<div class="definition" markdown="1">

<ins id="def4">**Definition 4**</ins> The étale space $$\Spe(\omega_M)$$ defined above is called the *orientation double cover* of $$M$$, and a global section $$M \rightarrow \Spe(\omega_M)$$ is called a *global orientation*. The manifold $$M$$ is *orientable* if a global orientation exists.

</div>

As its name indicates, $$\Spe(\omega_M)$$ is a covering space of $$M$$; moreover, for any $$x\in M$$, taking a chart $$U$$ about $$x$$, the preimage $$p^{-1}(U)$$ under the canonical projection $$p:\Spe(\omega_M)\rightarrow M$$ splits into two disjoint open subsets each homeomorphic to $$U$$.

<div class="example" markdown="1">

<ins id="ex5">**Example 5**</ins> Consider the orientation double cover $$p:\Spe(\omega_{S^1})\rightarrow S^1$$ of the circle. For any point $$x\in S^1$$, the fiber $$p^{-1}(x)$$ consists of two points $$(x,+)$$ and $$(x,-)$$; the same holds for any chart $$U$$ containing $$x$$, so $$p^{-1}(U)$$ decomposes into two open subsets $$U^+,U^-$$.

![Orientation_cover_of_S1](/assets/images/Math/Algebraic_Topology/Poincare_Duality-1.svg){:style="width:45%" class="invert" .align-center}

Covering $$S^1$$ by such charts and gluing the orientations where they overlap, we obtain a double cover with two components as shown below.

![Orientation_cover_of_S1_glued](/assets/images/Math/Algebraic_Topology/Poincare_Duality-2.svg){:style="width:45%" class="invert" .align-center}

However, not every double cover is trivial. For instance, if we cross-glue the top and bottom components of the above cover of $$S^1$$, we obtain a double cover with a single component; the same phenomenon occurs for the orientation double cover of a non-orientable manifold.

To see this, consider the orientation cover of the Möbius strip $$M$$. As with $$S^1$$, for any point $$x\in M$$ the fiber $$p^{-1}(x)$$ consists of two points $$(x,+)$$ and $$(x,-)$$, and the same is true at every point of $$M$$.

![orientation_cover_of_M](/assets/images/Math/Algebraic_Topology/Poincare_Duality-3.svg){:style="width:40%" class="invert" .align-center}

Yet when we attempt to glue these together over all of $$M$$, a problem arises. Proceeding counterclockwise around the strip while respecting orientations, by the time we return to $$x$$ the labels $$(x,+)$$ and $$(x,-)$$ have been interchanged, forcing us to cross-glue the top and bottom components. The resulting double cover of $$M$$ is homeomorphic to a cylinder.

</div>

By definition, $$M$$ is orientable if and only if $$\omega_M$$ admits a global section, which is equivalent to $$\Spe(\omega_M)$$ being a trivial covering space, and in turn equivalent to $$\omega_M$$ being a constant sheaf. Applying [§Covering Spaces, ⁋Corollary 12](/en/math/algebraic_topology/covering_spaces#cor12) yields the following proposition.

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6**</ins> For a (connected) topological manifold $$M$$, the following are equivalent:

1. $$M$$ is orientable.
2. $$\Spe(\omega_M)$$ has two components.
3. The monodromy action of $$\pi_1(M)$$ on $$\Spe(\omega_M)$$ is trivial.

</div>

Since we have already extended homology and cohomology from $$\mathbb{Z}$$-modules to general $$A$$-modules, the preceding argument can be carried out for arbitrary $$A$$ as well. To this end, consider the relative-homology version of [\[Algebraic Topology\] §Cohomology, ⁋Proposition 1](/en/math/algebraic_topology/cohomology#prop1) and observe that there is a (non-canonical) isomorphism

$$H_k(M, M\setminus\{x\};A)\cong H_k(M,M\setminus\{x\})\otimes_\mathbb{Z}A\oplus\Tor_1^\mathbb{Z}(H_{k-1}(M, M\setminus\{x\}), A)$$

Since $$H_k(M,M\setminus \{x\})$$ is trivial whenever $$k\neq m$$, this isomorphism gives

$$H_m(M,M\setminus \{x\};A)\cong H_m(M,M\setminus\{x\})\otimes_\mathbb{Z}A\cong A$$

Hence replacing every occurrence of $$\mathbb{Z}$$ in the above discussion by $$A$$ remains valid. In particular we obtain the presheaf of $$A$$-orientations

$$\omega_M^A(U)=\prod_{x\in U}\Iso_A(H_m(M,M\setminus\{x\};A), \underline{A}_x)$$

and from it the notion of a global $$A$$-orientation. The resulting $$A$$-orientation sheaf $$\omega_M^A$$ is simply $$\omega_M\otimes A$$.

To derive a result analogous to [Proposition 6](#prop6) for this definition, we revisit [§Covering Spaces, ⁋Theorem 11](/en/math/algebraic_topology/covering_spaces#thm11). For each covering space $$p:E \rightarrow M$$ we considered the $$\pi_1(M,x)$$-action on the fiber $$p^{-1}(x)$$ defined by the monodromy functor, which is the same as a group homomorphism $$\pi_1(M,x)\rightarrow \Aut(p^{-1}(x))$$. For the covering space $$p:\Spe(\omega_M)\rightarrow M$$, the fiber $$p^{-1}(x)$$ is defined by the automorphisms of the stalk $$\mathbb{Z}$$,

$$\Iso_\mathbb{Z}(\mathbb{Z},\mathbb{Z})\cong \mathbb{Z}^\times\cong \{\pm 1\}$$

so the $$\pi_1(M,x)$$-action is precisely a group homomorphism $$\pi_1(M,x)\rightarrow \mathbb{Z}^\times$$. Since an $$A$$-module isomorphism from $$A$$ to $$A$$ corresponds exactly to an element of the unit group $$A^\times$$, the same construction yields a group homomorphism $$\pi_1(M,x)\rightarrow A^\times$$. Thus [Proposition 6](#prop6) generalizes as follows.

<div class="proposition" markdown="1">

<ins id="prop7">**Proposition 7**</ins>  For a (connected) topological manifold $$M$$, the following are equivalent:

1. $$M$$ is $$A$$-orientable.
2. $$\Spe(\omega_M^A)$$ is the trivial covering $$M\times \lvert A^\times\rvert$$.
3. The monodromy representation $$\pi_1(M)\rightarrow A^\times$$ is trivial.

</div>

The most striking case of this generalization is $$A=\mathbb{Z}/2$$. Here the only unit of $$A$$ is $$-1=1$$, so there is a unique way to specify an orientation, and consequently every manifold is automatically $$\mathbb{Z}/2$$-orientable.

## Fundamental Class

We now turn to the existence of global ($$A$$-)orientations. That is, given local orientations $$s_x$$ for all $$x\in X$$, we ask whether there exists a global section $$s:M\rightarrow \Spe(\omega_M^A)$$ with $$s(x)=(x,s_x)$$.

On the other hand, via the canonical homomorphism

$$H_m(M; A)\rightarrow H_m(M,M\setminus\{x\};A)\tag{1}$$

every top homology class $$\alpha\in H_m(M;A)$$ defines an element $$\alpha_x\in H_m(M,M\setminus\{x\};A)$$ in the local homology group. A natural question is then: regarding the given local orientations $$s_x$$ as elements of $$A^\times$$ and hence of $$H_m(M,M\setminus\{x\};A)$$, does there exist a class $$\alpha\in H_m(M;A)$$ whose image in $$H_m(M,M\setminus\{x\};A)$$ equals $$s_x$$ for every $$x\in X$$?

These two paragraphs illustrate the form that Poincaré duality takes. A global section $$s:M \rightarrow \Spe(\omega_M^A)$$ is essentially a function defined on all of $$M$$, corresponding to the notion of $$0$$-th cohomology. By contrast, $$\alpha\in H_m(M;A)$$ is an element of the $$m$$-th homology. Poincaré duality asserts the equivalence of these two notions, and more generally establishes a duality between the $$k$$-th cohomology and the $$(m-k)$$-th homology.

What remains in this post falls largely into two steps.

1. Show that a lift of the canonical homomorphism (1) defines a global orientation, and conversely.
2. Define the *sheaf cohomology* in which a global orientation $$M \rightarrow \Spe(\omega_M^A)$$ lives.

The heart of Poincaré duality lies entirely in the first step; the second is more a matter of learning the language that expresses it cleanly. We therefore begin with the first step, which is furnished by the following lemma.

<div class="proposition" markdown="1">

<ins id="lem8">**Lemma 8**</ins> Fix a topological manifold $$M$$ of dimension $$m$$. For any compact subset $$C$$ of $$M$$, the following hold.

1. Given any section $$s:M \rightarrow \Spe(\omega_M^A)$$, there exists a unique homology class
    
    $$\alpha_C\in H_m(M,M\setminus C;A)$$

    such that for every $$x\in C$$, the image of $$\alpha_C$$ under the canonical homomorphism

    $$H_m(M,M\setminus C;A)\rightarrow H_m(M,M\setminus\{x\};A)$$

    equals $$s_x$$.
2. $$H_i(M, M\setminus C;A)=0$$ for all $$i>m$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First we show that if the proposition holds for arbitrary compact sets $$C_1,C_2$$ and their intersection $$C_1\cap C_2$$, then it also holds for $$C_1\cup C_2$$. From the Mayer–Vietoris sequence

$$\cdots \rightarrow H_k(M,M\setminus (C_1\cup C_2); A)\rightarrow H_k(M,M\setminus C_1;A)\oplus H_k(M,M\setminus C_2;A)\rightarrow H_k(M, M\setminus (C_1\cap C_2);A)\rightarrow\cdots\tag{2}$$

the inductive hypothesis gives

$$H_k(M,M\setminus C_1;A)=H_k(M,M\setminus C_2;A)=H_k(M,M\setminus(C_1\cap C_2);A)=0$$

for $$k>m$$, forcing $$H_k(M,M\setminus (C_1\cup C_2);A)=0$$ as well; this establishes the second claim.

For the first claim, suppose a section $$s:M \rightarrow \Spe(\omega_M^A)$$ is given. By the inductive hypothesis there are unique lifts over $$C_1,C_2,C_1\cap C_2$$, and we must patch these to a class $$\alpha_{C_1\cup C_2}$$. Uniqueness forces $$\alpha_{C_1}$$ and $$\alpha_{C_2}$$ to agree over $$C_1\cap C_2$$, so the element

$$(\alpha_{C_1},-\alpha_{C_2})\in H_m(M,M\setminus C_1;A)\oplus H_m(M,M\setminus C_2;A)$$

lies in the kernel of the map to $$H_m(M, M\setminus (C_1\cap C_2);A)$$. Hence it lifts to $$H_m(M,M\setminus (C_1\cup C_2);A)$$, and uniqueness follows from the injectivity of

$$0=H_{m+1}(M,M\setminus (C_1\cap C_2);A)\rightarrow H_m(M,M\setminus (C_1\cup C_2))\rightarrow H_m(M,M\setminus C_1;A)\oplus H_m(M,M\setminus C_2;A)$$

For the base case of the induction it suffices to consider $$M=\mathbb{R}^m$$ with $$A$$ a convex compact subset. Indeed, any compact set in an arbitrary manifold $$M$$ can be covered by Euclidean charts, and compactness reduces us to $$M=\mathbb{R}^m$$; using a basis of open balls and compactness again, we may further assume $$A$$ is convex. In this situation both $$\mathbb{R}^m\setminus A$$ and $$\mathbb{R}^m\setminus \{x\}$$ deformation retract onto $$S^{m-1}$$, yielding the required isomorphism and completing the proof.

</details>

In this proof compactness is essential: it guarantees that the inductive construction of $$\alpha$$ via the Mayer–Vietoris sequence terminates in finitely many steps. When compactness is dropped, Poincaré duality assumes a somewhat different form, and to capture both cases in a single statement one must introduce the language of sheaf cohomology.

In any case, by [Lemma 8](#lem8), if $$M$$ is a compact topological manifold of dimension $$m$$, setting $$C=M$$ yields the following theorem.

<div class="proposition" markdown="1">

<ins id="thm9">**Theorem 9**</ins> Let $$M$$ be a compact connected topological manifold of dimension $$m$$. Then for any orientation sheaf $$\omega_M^A$$, there exists a unique class $$[M]\in H_m(M;A)$$ whose image under the canonical homomorphism (1) coincides with $$s_x$$.

</div>

By [Lemma 8](#lem8), $$H_m(M;A)$$ is the free $$A$$-module of rank $$1$$ generated by $$[M]$$, and distinct choices of global orientation correspond to distinct choices of generator of $$H_m(M;A)$$.

<div class="definition" markdown="1">

<ins id="def10">**Definition 10**</ins> The class $$[M]$$ defined in [Theorem 9](#thm9) is called the *fundamental class* of $$M$$ determined by the global orientation $$s$$.

</div>

Moreover, if a homology class $$[M]$$ satisfying the conditions of [Theorem 9](#thm9) exists, it in turn determines a global section $$s:M \rightarrow \Spe(\omega_M^A)$$.

## Poincaré Duality

We are now in position to prove Poincaré's theorem for an $$A$$-orientable manifold. Consider the cap product homomorphism

$$-\frown -: H^p(M;A)\otimes_A H_m(M;A) \rightarrow H_{m-p}(M;A)$$

Since $$H_m(M;A)\cong A$$, this homomorphism may be viewed as an $$A$$-module homomorphism from $$H^p(M;A)$$ to $$H_{m-p}(M;A)$$. In particular, fixing the generator $$[M]$$ of $$H_m(M;A)$$, we obtain the homomorphism

$$-\frown [M]: H^p(M;A)\rightarrow H_{m-p}(M;A)$$

<div class="proposition" markdown="1">

<ins id="thm11">**Theorem 11**</ins> For an $$A$$-orientable compact manifold $$M$$ of dimension $$m$$ and its fundamental class $$[M]$$, the homomorphism

$$-\frown [M]: H^p(M;A)\rightarrow H_{m-p}(M;A)$$

is an isomorphism.

</div>

The proof again proceeds by induction using the Mayer–Vietoris sequence, much as for [Lemma 8](#lem8). The difference is that [Lemma 8](#lem8) concerned compact subsets $$C$$, so compactness could be exploited directly, whereas here the statement is about $$M$$ itself. If a chart $$U$$ of $$M$$ is given, it need not be compact, so a naive inductive approach fails. To remedy this we make the following definition.

<div class="definition" markdown="1">

<ins id="def12">**Definition 12**</ins> A cochain $$\varphi\in C^p(M;A)$$ is *compactly supported* if there exists a compact set $$K\subseteq M$$ such that $$\varphi(\sigma)=0$$ for every simplex contained in $$M\setminus K$$. The $$p$$-th *compactly supported cohomology* $$H_c^p(M;A)$$ is the $$p$$-th cohomology of the cochain complex of compactly supported cochains.

</div>

The identity

$$H_c^p(M;A)\cong \varinjlim_{\text{\scriptsize$K$ compact}}H^p(M,M\setminus K;A)$$

is intuitively clear and straightforward to verify. For each compact set $$K$$ the canonical map

$$H^p(M,M\setminus K;A)\rightarrow H_c^p(M;A)$$

is compatible with the directed system on the right, yielding a well-defined homomorphism

$$\varinjlim_{\text{\scriptsize$K$ compact}}H^p(M,M\setminus K;A)\rightarrow H_c^p(M;A)$$

that one checks directly is an isomorphism. In particular, for any compact manifold $$M$$ we have $$H_c^p(M,A)\cong H^p(M;A)$$, so the desired result follows from the next lemma.

<div class="proposition" markdown="1">

<ins id="lem13">**Lemma 13**</ins> For any $$A$$-orientable $$m$$-manifold $$M$$, the isomorphism

$$H_c^p(M;A)\cong H_{m-p}(M;A)$$

holds for all $$p$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

We must first define the isomorphism. For any compact subset $$K$$, consider the cap product

$$H^p(M,M\setminus K;A)\times H_m(M,M\setminus K;A)\rightarrow H_{m-p}(M;A)$$

By [Lemma 8](#lem8), for each point $$x$$ we can find a homology class

$$s_K\in H_m(M,M\setminus K;A)$$

restricting to the orientation of $$M$$ at $$x$$. Our claim is that the cap product homomorphisms

$$-\frown s_K: H^p(M,M\setminus K;A) \rightarrow H_{m-p}(M;A)$$

are compatible with the direct system, and therefore define a homomorphism $$H_c^p(M;A)\rightarrow H_{m-p}(M;A)$$. To verify this, let $$K'$$ be another compact subset containing $$K$$ and let $$i:K\rightarrow K'$$ be the inclusion. Then for any $$\alpha\in H^p(M,M\setminus K;A)$$,

$$i^\ast\alpha\frown s_{K'}=\alpha\frown i_\ast s_{K'}$$

by the projection formula ([§Cup Product, ⁋Proposition 6 (Projection formula)](/en/math/algebraic_topology/cup_products#prop6)), and uniqueness in [Lemma 8](#lem8) gives $$i_\ast s_{K'}=s_K$$. Hence we obtain a well-defined homomorphism $$H_c^p(M;A)\rightarrow H_{m-p}(M;A)$$.

We claim that this homomorphism $$D_M:H_c^p(M;A)\rightarrow H_{m-p}(M;A)$$ is an isomorphism. The proof again uses induction via the Mayer–Vietoris sequence, as in [Lemma 8](#lem8).

The base case is $$M=\mathbb{R}^m$$. For any ball $$B\subseteq \mathbb{R}^m$$, the orientation $$s_B$$ of $$B$$ yields

$$H_m(\mathbb{R}^m, \mathbb{R}^m\setminus B;A)\cong A$$

and by [§Cohomology, ⁋Proposition 3](/en/math/algebraic_topology/cohomology#prop3) we have $$H^m(\mathbb{R}^m,\mathbb{R}^m\setminus B;A)\cong A$$. The element $$\alpha_B$$ corresponding to the dual basis of the orientation of $$B$$ satisfies

$$\langle 1\smile \alpha_B, s_B\rangle=\langle 1,\alpha_B\frown s_B\rangle$$

so $$\alpha_B\frown s_B$$ corresponds to the generator of $$H_0(\mathbb{R}^m)\cong A$$. Consequently

$$H^p(\mathbb{R}^m,\mathbb{R}^m\setminus B;A)\cong H_{m-p}(\mathbb{R}^m;A)$$

for all $$p$$. (When $$p\neq m$$ both sides are zero modules, so the zero map is an isomorphism.) Enlarging the radius of $$B$$ and passing to the directed system covering all of $$\mathbb{R}^m$$, we conclude that $$H_c^p(M)\rightarrow H_{m-p}(M)$$ is an isomorphism.

For the inductive step, suppose $$M=U\cup V$$ with open sets $$U,V$$ for which the proposition holds, as well as for $$U\cap V$$. For compact subsets $$K\subset U$$, $$L\subset V$$, consider the relative Mayer–Vietoris sequence

$$\cdots\rightarrow H^k(M,M\setminus(K\cap L);A)\rightarrow H^k(M,M\setminus K;A)\oplus H^k(M,M\setminus L;A)\rightarrow H^k(M,M\setminus(K\cup L);A)\rightarrow \cdots$$

After excision and passage to the limit we obtain the commutative diagram

![MVseq_duality](/assets/images/Math/Algebraic_Topology/Poincare_Duality-4.svg){:style="width:38.08em" class="invert" .align-center}

and the induction is completed by the inductive hypothesis and [\[Homological Algebra\] §Diagram chasing, ⁋Corollary 2 (The five lemma)](/en/math/homological_algebra/diagram_chasing#cor2).

Since $$M$$ need not be compact, an additional argument is required. Suppose $$M$$ is the union of a nested family of open subsets

$$U_1\subset U_2\subset\cdots$$

and that the proposition holds for each $$U_i$$. Any compact subset of $$M$$ is contained in some $$U_i$$, whence

$$H_c^p(M)=\varinjlim_i H^p_c(U_i),\qquad H_{m-p}(M)=\varinjlim_i H_{m-p}(U_i)$$

By hypothesis the maps $$H^p_c(U_i)\rightarrow H_{m-p}(U_i)$$ are all isomorphisms, yielding the desired result.

Now suppose $$M$$ is an open subset of $$\mathbb{R}^m$$. We can cover $$M$$ by countably many convex open subsets (i.e. open balls) $$U_1,U_2,\ldots$$, each homeomorphic to $$\mathbb{R}^m$$; the base step above gives the theorem's isomorphism for each of them. The intersection of two convex sets is again convex, so by induction the conclusion holds for $$U_1\cup U_2$$. To extend to $$U_1\cup U_2\cup U_3$$ we use

$$(U_1\cup U_2)\cap U_3=(U_1\cap U_3)\cup (U_2\cap U_3)$$

where $$U_1\cap U_3$$, $$U_2\cap U_3$$, and $$U_1\cap U_2\cap U_3$$ are all convex open subsets of $$\mathbb{R}^m$$, hence satisfy the hypothesis. Proceeding in this way, each of

$$U_1,\quad U_1\cup U_2, \quad U_1\cup U_2\cup U_3,\quad \cdots$$

satisfies the conclusion. Applying the preceding (infinite) induction to the nested sequence

$$U_1\subset U_1\cup U_2\subset U_1\cup U_2\cup U_3\cdots$$

yields the result.

Finally, for an arbitrary manifold $$M$$, second countability allows us to cover $$M$$ by countably many Euclidean charts and apply the same argument.

</details>

In particular, if $$M$$ is compact, the duality map $$D_M$$ is precisely the cap product with the fundamental class $$[M]$$.

## Twisted Poincaré Duality

When $$M$$ is not $$A$$-orientable, the principal reason [Theorem 11](#thm11) fails is that $$\or_M^A$$ is not a constant sheaf but merely locally constant. In the language of covering spaces, the monodromy action is nontrivial on the stalk $$A$$: traversing a loop twists the stalk before reattaching it. This twist is an automorphism of $$A$$, so it suffices to consider the action on the unit group $$A^\times$$.

To incorporate this twist into the duality, we define *homology with local coefficients*.

<div class="definition" markdown="1">

<ins id="def14">**Definition 14**</ins> A locally constant sheaf $$\mathscr{L}$$ on $$M$$ is called a *local coefficient system*.

</div>

Let $$L$$ be the stalk of a local system $$\mathscr{L}$$. By [§Covering Spaces, ⁋Theorem 11](/en/math/algebraic_topology/covering_spaces#thm11), every path $$\alpha:[0,1]\rightarrow M$$ induces an isomorphism $$\mathscr{L}_{\alpha(0)}\rightarrow \mathscr{L}_{\alpha(1)}$$ between stalks. This is simply the isomorphism obtained by lifting the path $$\alpha$$ in the covering space $$\Spe(\mathscr{L})\rightarrow M$$. Hence we obtain a functor

$$\Pi_1(M)\rightarrow \Ab; \qquad x\mapsto \mathscr{L}_x$$

Fixing the vertex $$e_0=(1,0,\ldots,0)$$ of $$\Delta^k$$, we define

$$C_\bullet(M,\mathscr{L})=\bigoplus_{\sigma:\Delta^k\rightarrow M}\mathscr{L}_{\sigma(e_0)}$$

Although $$\mathscr{L}_x\cong L$$ for each $$x$$, the essential feature of this definition is that the copies of $$L$$ at different points may differ by nontrivial automorphisms. The differential of this chain complex is defined, for a singular $$k$$-simplex $$\sigma:\Delta^k \rightarrow M$$ and coefficient $$a\in \mathscr{L}_{\sigma(e_0)}$$, by

$$\partial_k(a\sigma)=\sum_{i=0}^k(-1)^k\mathscr{L}_{\sigma_k}(a) (\sigma\vert_{[v_0,\ldots, \hat{v}_i,\ldots,v_k]})$$

Here $$\mathscr{L}_{\sigma_k}$$ is obtained by applying the functor $$\Pi_1(M) \rightarrow \Ab$$ to the path in $$M$$ given by the edge joining the first vertex $$\sigma(e_0)$$ of the original simplex to the first vertex of the $$i$$-th face. In favorable situations such as ours, one may instead use the universal cover $$\widetilde{M}$$, the monodromy action (i.e. Deck transformations) upon it, and the monodromy representation $$\pi_1(X)\rightarrow \Aut(A)$$ to form the chain complex

$$C(\widetilde{M})\otimes_{\mathbb{Z}[\pi_1(X)]} A$$

which yields the same homology group as above.

This may seem an excessive level of generality, for to state the non-orientable version of Poincaré duality we shall ultimately take the local coefficient system $$\mathscr{L}$$ to be the constant sheaf $$\underline{A}$$. Yet this generalization also permits a parallel extension on the cohomology side, and that extension renders Poincaré duality more transparent.

For any topological space $$X$$ and sheaf $$\mathscr{F}$$ on it, the global section functor

$$\Gamma(X,-):\Sh(X,\mathcal{A})\rightarrow \mathcal{A}$$

is left exact, hence admits right derived functors. To compute these directly one uses the Godement resolution, defined as follows.

Given a topological space $$X$$ and a sheaf $$\mathscr{F}$$ on it, consider the étalé space $$\Spe(\mathscr{F})$$. We know that $$\mathscr{F}$$ is precisely the sheaf of continuous sections of $$\Spe(\mathscr{F})\rightarrow X$$. For any open set $$U$$, define

$$\mathscr{G}_0(U)=\prod_{x\in U}\mathscr{F}_x$$

Thus $$\mathscr{G}_0$$ is the sheaf of set-theoretic (not necessarily continuous) sections of $$\Spe(\mathscr{F})\rightarrow X$$. The idea is to push into the quotient sheaf $$\mathscr{Q}$$ the obstructions to piecing together local sections into global ones, via the sequence induced by the inclusion $$\mathscr{F}\rightarrow \mathscr{G}_0$$:

$$0 \rightarrow \mathscr{F}\rightarrow \mathscr{G}_0 \rightarrow \mathscr{Q}\rightarrow 0$$

Repeating the construction for $$\mathscr{Q}$$ by setting

$$\mathscr{G}_1(U)=\prod_{x\in U}\mathscr{Q}_x$$

we obtain the *Godement resolution*

$$0 \rightarrow \mathscr{F}\rightarrow \mathscr{G}_0 \rightarrow \mathscr{G}_1\rightarrow \cdots$$

Intuitively, this repeatedly isolates in successive quotients whatever prevents the existence of global sections. The resolution $$\mathscr{G}_\bullet$$ is not an injective resolution, but each $$\mathscr{G}_i$$ is a flabby (flasque) sheaf, so the right derived functors $$R^i\Gamma$$ of the global section functor can be computed from it.

<div class="definition" markdown="1">

<ins id="def15">**Definition 15**</ins> For a topological space $$X$$ and a sheaf $$\mathscr{F}$$ on it, the $$k$$-th cohomology of the complex of global sections of the Godement resolution

$$0 \rightarrow \mathscr{F}(X)\rightarrow \mathscr{G}_0(X)\rightarrow \mathscr{G}_1(X)\rightarrow \cdots$$

is denoted by

$$H^k(X; \mathscr{F})$$

and is called the *sheaf cohomology* of $$X$$ with coefficients in $$\mathscr{F}$$.

</div>

Further details can be found in [\[Algebraic Geometry\] §Sheaf Cohomology, ⁋Definition 1](/en/math/algebraic_varieties/sheaf_cohomology#def1). Poincaré duality now generalizes to the isomorphism

$$H^k(M;\mathscr{L})\cong H_{m-k}(M;\or_M^A\otimes \mathscr{L})$$

To recover the original Poincaré duality, set $$\mathscr{L}$$ to be the constant sheaf $$\underline{A}$$. For nice spaces such as manifolds, sheaf cohomology $$H^k(M;\underline{A})$$ is isomorphic to singular cohomology $$H^k(M;A)$$, whence

$$H^k(M;A)\cong H_{m-k}(M;\or_M^A)$$

If in addition $$M$$ is $$A$$-orientable, then $$\or_M^A$$ is also constant, and we recover the classical Poincaré duality

$$H^k(M;A)\cong H_{m-k}(M;A)$$

## Poincaré Duality and the Cup Product

Thus far we have used the cup product on the cohomology ring, and the cap product derived from it, without hesitation. Yet if someone asks *what* the cup product is, the answer is awkward. The answer is simple:

> The cup product is the Poincaré dual of intersection.

To make this statement rigorous would require at least as much effort as we have already expended. To grasp its intuitive meaning, however, the following example suffices.

<div class="example" markdown="1">

<ins id="ex16">**Example 16**</ins> Consider the torus $$T^2=S^1\times S^1$$. By the Künneth formula, the cohomology of $$T^2$$ is

$$H^0(T^2;\mathbb{Z})\cong \mathbb{Z}, \quad H^1(T^2;\mathbb{Z})\cong \mathbb{Z}^2,\quad H^2(T^2;\mathbb{Z})$$

The only non-trivial product in this cohomology ring is the product of the two generators $$\alpha,\beta$$ of $$H^1(T^2;\mathbb{Z})$$. By [§Cohomology, ⁋Proposition 3](/en/math/algebraic_topology/cohomology#prop3), these correspond to the duals of the two standard circle factors of $$T^2$$. Their cup product is a generator of $$H^2(T^2;\mathbb{Z})$$, which is immediate from the definition of cup product or from the algebraic fact that

$$H^2(T^2;\mathbb{Z})=H^1(T^2;\mathbb{Z})\otimes H^1(T^2;\mathbb{Z})\cong \mathbb{Z}\otimes \mathbb{Z}\cong \mathbb{Z}$$

is generated by $$\alpha\otimes \beta$$.

Geometrically, the reason this cup product is $$\pm 1$$ times the generator rather than some other constant multiple is the following. Let $$a,b$$ be the homology classes dual to $$\alpha,\beta$$; then $$a$$ and $$b$$ intersect transversely in a single point, as shown below.

![Torus_intersection](/assets/images/Math/Algebraic_Topology/Poincare_Duality-5.svg){:style="width:30%" class="invert" .align-center}

Classifying how the two curves meet and assigning one a positive and the other a negative direction is precisely what it means to specify an orientation of $$T^2$$.

How then does this geometric picture explain that $$\alpha^2=0$$? A literal computation of $$a\cap a$$ would yield $$a$$ again. The difficulty is that two copies of the cycle $$a$$ are not in *general position*. Roughly, two lines in $$\mathbb{R}^2$$ generally meet in one point unless they are parallel (including coincidence); the notion of general position extends this idea.

Consider curves in $$T^2$$ representing the homology class $$a$$. They can typically be chosen disjoint; if they do meet (excluding tangencies, which violate general position), the intersection looks as follows.

![intersections_on_torus](/assets/images/Math/Algebraic_Topology/Poincare_Duality-6.png){:style="width:40%" class="invert" .align-center}

At first sight there appear to be two intersection points, but their signs are opposite: taking the cross product with the line as first vector and the curve as second, one points outward and the other inward. The two intersections therefore cancel, giving intersection number zero, and hence $$\alpha\smile\alpha=0$$.

</div>

--- 

**References**

[Hat] A. Hatcher, *Algebraic Topology*. Cambridge University Press, 2022.  
[May] J. P. May, *A concise course in algebraic topology*.

---
