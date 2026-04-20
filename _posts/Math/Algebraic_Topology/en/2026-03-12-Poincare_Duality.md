---

title: "Poincaré Duality"
excerpt: ""

categories: [Math / Algebraic Topology]
permalink: /en/math/algebraic_topology/Poincare_duality
header:
    overlay_image: /assets/images/Math/Algebraic_Topology/Poincare_duality.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_topology-en"

date: 2026-03-12
last_modified_at: 2026-03-12
weight: 9

---

In this post, we discuss Poincaré duality, one of the beautiful theorems of algebraic topology. As mentioned in the previous post, Poincaré duality reveals a duality between homology and cohomology. While the universal coefficient theorem ([§Cohomology, ⁋Theorem 5](/en/math/algebraic_topology/cohomology#thm65)) was somewhat expected when we defined $$C^\bullet(X;A)$$ as the dual of $$C_\bullet(X;A)$$, Poincaré duality has a more geometric significance.

## Orientation Sheaf

To define Poincaré duality, we first need to define the notion of orientation. This is a concept defined on topological manifolds ([§Topological Manifolds, ⁋Definition 2](/en/math/algebraic_topology/topological_manifolds#def2)), and in this post, unless otherwise stated, we assume that any manifold is *connected*.

Consider an arbitrary topological manifold $$M$$ of dimension $$m$$ and an open set $$U$$. The correspondence

$$U\mapsto H_m(M, M\setminus U;\mathbb{Z})$$

is a presheaf since for any $$U\subseteq V$$, there is a natural restriction map

$$H_m(M, M\setminus V;\mathbb{Z})\rightarrow H_m(M,M\setminus U;\mathbb{Z})\tag{1}$$

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> The sheafification ([\[Topology\] §Sheaves, ⁋Definition 5](/en/math/topology/sheaves#def5)) of the correspondence (1) is called the *orientation sheaf* and is denoted by $$\or_M$$.

</div>

Then for any $$x\in M$$ and any open neighborhood $$U$$ of $$x$$, the following canonical map

$$H_m(M,M\setminus U;\mathbb{Z})\rightarrow H_m(M,M\setminus\{x\};\mathbb{Z})$$

exists. These maps behave well with respect to the restriction maps above, and thus the direct limit map

$$\or_{M,x}=\varinjlim_{x\in U} H_m(M,M\setminus U;\mathbb{Z})\rightarrow H_m(M,M\setminus \{x\};\mathbb{Z})$$

is well-defined.

By definition, an element of $$H_m(M,M\setminus\{x\};\mathbb{Z})$$ is an $$m$$-simplex $$\sigma:\Delta^m \rightarrow M$$ whose boundary does not meet $$x$$, and we can choose a sufficiently small neighborhood $$U$$ of $$x$$ such that this boundary does not meet $$U$$. On the other hand, if two homology classes $$\alpha_U\in H_m(M,M\setminus U;\mathbb{Z})$$, $$\alpha_V\in H_m(M,M\setminus V;\mathbb{Z})$$ are the same element in $$H_m(M,M\setminus \{x\};\mathbb{Z})$$, then similarly we can find a sufficiently small open neighborhood $$W$$ of $$x$$ that does not meet the boundaries of either element, and then $$\alpha_U$$ and $$\alpha_V$$ must be the same element in $$H_m(M,M\setminus W;\mathbb{Z})$$. That is, the above function

$$\varinjlim_{x\in U}H_m(M,M\setminus U;\mathbb{Z})\rightarrow H_m(M,M\setminus \{x\};\mathbb{Z})$$

is an isomorphism. Moreover, by [§Computation of Homology, ⁋Theorem 2](/en/math/algebraic_topology/computation_of_homology#thm2),

$$H_m(M,M\setminus\{x\};\mathbb{Z})\cong H_m(U,U\setminus\{x\};\mathbb{Z})\cong H_m(\mathbb{R}^m, \mathbb{R}^m\setminus\{0\};\mathbb{Z})$$

and since $$\mathbb{R}^m\setminus\{0\}$$ deformation retracts to $$S^{m-1}$$, by the relative homology long exact sequence, the right-hand side is isomorphic to $$\mathbb{Z}$$, and we can also verify that this sheaf is a locally constant sheaf. That is, for any $$x\in M$$, there exists an open neighborhood $$U$$ such that $$\or_M\vert_U$$ is a constant sheaf. ([\[Topology\] §Sheaves, ⁋Example 9](/en/math/topology/sheaves#ex9))

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> The relative homology group $$H_m(M, M\setminus \{x\};\mathbb{Z})$$ is called the *local homology group* of $$M$$ at $$x$$.

</div>

## Constant Sheaves and Covering Spaces, Orientation-Generator Sheaf

To examine the orientation sheaf $$\or_M$$ defined above in more detail, we need to look more carefully at constant sheaves and locally constant sheaves. First, consider an arbitrary abelian group $$A$$, and give it the discrete topology to regard it as a topological space. Then the projection map $$X\times A \rightarrow X$$ between topological spaces is a trivial covering space, and the sheaf of sections of this covering map is precisely the constant sheaf $$\underline{A}$$. Conversely, given a constant sheaf $$\underline{A}$$, we can verify that the étale space $$\Spe(\underline{A})$$ becomes the covering space $$X\times A \rightarrow X$$. ([\[Topology\] §Presheaves, ⁋Definition 9](/en/math/topology/presheaves#def9)) Thus, a locally constant sheaf is simply a sheaf whose étale space is a covering space.

Intuitively, $$H_m(M,M\setminus\{x\};\mathbb{Z})\cong \mathbb{Z}$$ tells us how many times an $$m$$-simplex $$\sigma:\Delta^m\rightarrow M$$ containing $$x$$ in its interior covers $$x$$. Since $$\Delta^m$$ can be given a sign depending on how its vertices are ordered, and through this isomorphism we can associate elements of $$\mathbb{Z}$$ to these $$m$$-simplices, the sign difference between two $$m$$-simplices can be thought of as the source $$\Delta^m$$ of the two simplices being ordered in opposite directions, or when the sign of $$\Delta^m$$ is fixed, the two simplex maps specifying different directions. Thus $$H_m(M,M\setminus\{x\};\mathbb{Z})$$ contains information about the orientation at the point $$x$$.

A natural question then arises: can we assign an orientation to every point $$x\in M$$ in a way that these orientations can be pieced together to match a global orientation on $$M$$? To do this, we first need a $$\mathbb{Z}$$ to serve as a reference. For this purpose, let us fix a constant sheaf $$\underline{\mathbb{Z}}$$ on $$M$$. ([\[Topology\] §Presheaves, ⁋Example 6](/en/math/topology/presheaves#ex6)) Then for each $$x\in M$$, we can think of its stalk $$\underline{\mathbb{Z}}_x$$ as having a generator $$1$$ chosen in a consistent way, and thus for each $$x$$, choosing an isomorphism

$$\Iso_\mathbb{Z}(H_m(M, M\setminus\{x\}), \underline{\mathbb{Z}}_x)$$

is equivalent to choosing whether $$M$$ has a positive or negative orientation at each $$x$$.

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> For a topological manifold $$M$$ of dimension $$m$$, a *local orientation* at a point $$x$$ is given by choosing an element of $$\Iso_\mathbb{Z}(H_m(M,M\setminus\{x\}), \underline{\mathbb{Z}}_x)$$.

</div>

Now for each open set $$U$$, define

$$\omega_M^\pre(U)=\prod_{x\in U}\Iso_\mathbb{Z}(H_m(M,M\setminus\{x\}), \underline{\mathbb{Z}}_x)$$

and for each $$U\subseteq V$$, define $$\rho_{VU}:\omega_M^\pre(V)\rightarrow \omega_M^\pre(U)$$ as the canonical projection. ([\[Set Theory\] §Properties of Product Sets, ⁋Definition 1](/en/math/set_theory/property_of_products#def1)) Then $$\omega_M^\pre$$ becomes a presheaf defined on $$M$$ ([\[Topology\] §Presheaves, ⁋Definition 4](/en/math/topology/presheaves#def4)), and for each $$p\in M$$, the stalk $$\omega_{M,x}^\pre$$ of $$\omega_M^\pre$$ at the point $$x$$ is $$\{\pm 1\}$$. ([\[Topology\] §Presheaves, ⁋Definition 9](/en/math/topology/presheaves#def9))

The sheafification $$\omega_M$$ of $$\omega_M^\pre$$ is called the *orientation-generator sheaf* of $$M$$. This involves examining, when the generator $$1$$ of the constant sheaf $$\underline{\mathbb{Z}}$$ with fixed orientation is fixed, whether the isomorphism $$H_m(M,M\setminus\{x\};\mathbb{Z})$$ maps $$1$$ to $$1$$ or to $$-1$$, and through this $$\omega_M$$ can be viewed as a subsheaf of $$\or_M$$. Since $$\omega_M$$ is a locally constant sheaf, its étale space $$\Spe(\omega_M)$$ is a covering space of $$M$$ with each fiber consisting of two elements.

<div class="definition" markdown="1">

<ins id="def4">**Definition 4**</ins> The étale space $$\Spe(\omega_M)$$ defined above is called the *orientation double cover* of $$M$$, and a global section $$M \rightarrow \Spe(\omega_M)$$ is called a *global orientation*. $$M$$ is *orientable* if a global orientation exists.

</div>

As the name suggests, $$\Spe(\omega_M)$$ is a covering space of $$M$$, and moreover, for any $$x\in M$$, considering a chart $$U$$ of $$x$$, the preimage $$p^{-1}(U)$$ under the canonical projection $$p:\Spe(\omega_M)\rightarrow M$$ consists of two disjoint open subsets each homeomorphic to $$U$$.

<div class="example" markdown="1">

<ins id="ex5">**Example 5**</ins> For example, consider the orientation double cover $$p:\Spe(\omega_{S^1})\rightarrow S^1$$ of $$S^1$$. The preimage $$p^{-1}(x)$$ of any point $$x\in S^1$$ under $$p$$ consists of two points $$(p,+)$$ and $$(p,-)$$, and the same holds for a chart $$U$$ containing $$x$$, so $$p^{-1}(U)$$ is divided into two open subsets $$U^+,U^-$$.

![Orientation_cover_of_S1](/assets/images/Math/Algebraic_Topology/Poincare_duality-1.png){:style="width:45%" class="invert" .align-center}

Now if we cover $$S^1$$ with such covers and glue the orientations together where the charts overlap, we obtain a double cover with two components as follows.

![Orientation_cover_of_S1_glued](/assets/images/Math/Algebraic_Topology/Poincare_duality-2.png){:style="width:45%" class="invert" .align-center}

However, not every double cover is a trivial cover. For example, if we glue the top and bottom components of the above cover of $$S^1$$ in a crossed manner, we obtain a double cover with one component, and a similar thing happens with the orientation double cover of a non-orientable manifold.

To observe this, consider the orientation cover of the Möbius strip $$M$$. As with $$S^1$$, for any point $$x\in M$$, $$p^{-1}(x)$$ consists of two points $$(x,+)$$ and $$(x,-)$$, and the same holds for any point of $$M$$.

![orientation_cover_of_M](/assets/images/Math/Algebraic_Topology/Poincare_duality-3.png){:style="width:40%" class="invert" .align-center}

However, when we try to glue this together to cover all of $$M$$, a problem arises. If we glue the two covers shown in this figure, proceeding counterclockwise while considering the orientation, when we return to $$x$$, $$(x,+)$$ and $$(x,-)$$ are swapped, so we must glue the top and bottom components in a crossed manner. The double cover of $$M$$ created this way becomes homeomorphic to a cylinder.

</div>

By definition, $$M$$ is orientable if and only if a global section of $$\omega_M$$ exists, which is equivalent to $$\Spe(\omega_M)$$ being a trivial covering space, which is again equivalent to $$\omega_M$$ being a constant sheaf. Applying [§Covering Spaces, ⁋Corollary 12](/en/math/algebraic_topology/covering_spaces#cor12) here, we obtain the following proposition.

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6**</ins> For a (connected) topological manifold $$M$$, the following are equivalent:

1. $$M$$ is orientable.
2. $$\Spe(\omega_M)$$ has two components.
3. The monodromy action of $$\pi_1(M)$$ acts trivially on $$\Spe(\omega_M)$$.

</div>

However, since we have already dealt with not only $$\mathbb{Z}$$-modules but also general $$A$$-modules when discussing homology and cohomology, the above argument can also be extended to general $$A$$-modules. For this purpose, first consider the relative homology version of [\[Algebraic Topology\] §Cohomology, ⁋Proposition 1](/en/math/algebraic_topology/cohomology#prop1), and observe that the following (non-canonical) isomorphism

$$H_k(M, M\setminus\{x\};A)\cong H_k(M,M\setminus\{x\})\otimes_\mathbb{Z}A\oplus\Tor_1^\mathbb{Z}(H_{k-1}(M, M\setminus\{x\}), A)$$

exists. However, since $$H_k(M,M\setminus \{x\})$$ is always a trivial group when $$k\neq m$$, from this isomorphism we know that

$$H_m(M,M\setminus \{x\};A)\cong H_m(M,M\setminus\{x\})\otimes_\mathbb{Z}A\cong A$$

Therefore, replacing all instances of $$\mathbb{Z}$$ in the above argument with $$A$$ will still make sense, and in particular, we obtain the presheaf of $$A$$-orientations

$$\omega_M^A(U)=\prod_{x\in U}\Iso_A(H_m(M,M\setminus\{x\};A), \underline{A}_x)$$

and the concept of global $$A$$-orientation defined from it. The resulting $$A$$-orientation sheaf $$\omega_M^A$$ is nothing but $$\omega_M\otimes A$$.

To derive a result like [Proposition 6](#prop6) from this definition, let us revisit [§Covering Spaces, ⁋Theorem 11](/en/math/algebraic_topology/covering_spaces#thm11). For each covering space $$p:E \rightarrow M$$, we considered the $$\pi_1(M,x)$$-action defined by the monodromy functor on the fiber $$p^{-1}(x)$$, which is equivalent to considering a group homomorphism $$\pi_1(M,x)\rightarrow \Aut(p^{-1}(x))$$. We then need to examine how the $$\pi_1(M,x)$$-action is defined for the covering space $$p:\Spe(\omega_M)\rightarrow M$$, where the fiber $$p^{-1}(x)$$ is defined from the automorphisms of the stalk $$\mathbb{Z}$$

$$\Iso_\mathbb{Z}(\mathbb{Z},\mathbb{Z})\cong \mathbb{Z}^\times\cong \{\pm 1\}$$

and thus the $$\pi_1(M,x)$$-action can be thought of precisely as a group homomorphism $$\pi_1(M,x)\rightarrow \mathbb{Z}^\times$$. Since an $$A$$-module isomorphism from $$A$$ to $$A$$ corresponds exactly to an element of the unit group $$A^\times$$ of $$A$$, this is ultimately equivalent to examining a group homomorphism $$\pi_1(M,x)\rightarrow A^\times$$. Thus [Proposition 6](#prop6) can be generalized as follows.

<div class="proposition" markdown="1">

<ins id="prop7">**Proposition 7**</ins>  For a (connected) topological manifold $$M$$, the following are equivalent:

1. $$M$$ is $$A$$-orientable.
2. $$\Spe(\omega_M^A)$$ is the trivial covering $$M\times \lvert A^\times\rvert$$.
3. The monodromy representation $$\pi_1(M)\rightarrow A^\times$$ is trivial.

</div>

The most noteworthy case in this generalization is when $$A=\mathbb{Z}/2$$. In this case, the only unit of $$A$$ is $$-1=1$$, so there is a unique way to specify an orientation, and thus any manifold is always $$\mathbb{Z}/2$$-orientable.

## Fundamental Class

We now examine the existence of global ($$A$$-)orientations. That is, when local orientations $$s_x$$ are given for all $$x\in X$$, we investigate whether there exists a global section $$s:M\rightarrow \Spe(\omega_M^A)$$ such that $$s(x)=(x,s_x)$$.

On the other hand, we know that through the following canonical homomorphism

$$H_m(M; A)\rightarrow H_m(M,M\setminus\{x\};A)\tag{1}$$

any top homology class $$\alpha\in H_m(M;A)$$ defines an element $$\alpha_x\in H_m(M,M\setminus\{x\};A)$$ of the local homology group. A natural question then is whether, when given local orientations $$s_x$$ for each $$x\in S_x$$ viewed as elements of $$A^\times$$ and treated as elements of $$H_m(M,M\setminus\{x\};A)$$, there exists an $$\alpha\in H_m(M;A)$$ whose image in $$H_m(M,M\setminus\{x\};A)$$ under the canonical map equals $$s_x$$ for all $$x\in X$$.

The above two paragraphs show what form Poincaré duality takes. A global section $$s:M \rightarrow \Spe(\omega_M^A)$$ is essentially a function defined on all of $$M$$, corresponding to the 0-th cohomology. On the other hand, $$\alpha\in H_m(M;A)$$ is an element of the $$m$$-th homology. Poincaré duality shows that these two concepts are equivalent, and more generally, shows a duality between the $$k$$-th cohomology and the $$(n-k)$$-th homology.

What we need to do in the remainder of this post is largely twofold:

1. Show that the lifting of the canonical homomorphism (1) defines a global orientation, and conversely.
2. Define the *sheaf cohomology* for which a global orientation $$M \rightarrow \Spe(\omega_M^A)$$ exists.

The core content of Poincaré duality is all contained in the first step, while the second step is closer to learning a language that can express this wisely. Therefore, we start with the first step. This is obtained by the following lemma.

<div class="proposition" markdown="1">

<ins id="lem8">**Lemma 8**</ins> Fix a topological manifold $$M$$ of dimension $$m$$. For any compact subset $$C$$ of $$M$$, the following holds:

1. For any given section $$s:M \rightarrow \Spe(\omega_M^A)$$, there exists a unique homology class
    
    $$\alpha_C\in H_m(M,M\setminus C;A)$$

    such that for any $$x\in C$$, the image of $$\alpha_C$$ under the canonical homomorphism

    $$H_m(M,M\setminus C;A)\rightarrow H_m(M,M\setminus\{x\};A)$$

    equals $$s_x$$.
2. For all $$i>n$$, $$H_i(M, M\setminus C;A)=0$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, let us show that if this proposition holds for arbitrary compact sets $$C_1,C_2$$ and their intersection $$C_1\cap C_2$$, then it also holds for $$C_1\cup C_2$$. From the Mayer-Vietoris sequence

$$\cdots \rightarrow H_k(M,M\setminus (C_1\cup C_2); A)\rightarrow H_k(M,M\setminus C_1;A)\oplus H_k(M,M\setminus C_2;A)\rightarrow H_k(M, M\setminus (C_1\cap C_2);A)\rightarrow\cdots\tag{2}$$

for $$k>m$$, by the inductive hypothesis,

$$H_k(M,M\setminus C_1;A)=H_k(M,M\setminus C_2;A)=H_k(M,M\setminus(C_1\cap C_2);A)=0$$

so $$H_k(M,M\setminus (C_1\cup C_2);A)$$ must also be $$0$$, from which the second claim follows.

To show the first claim, suppose a section $$s:M \rightarrow \Spe(\omega_M^A)$$ is given. By the inductive hypothesis, these can be lifted for $$C_1,C_2,C_1\cap C_2$$, so we need to piece these together to create a class $$\alpha_{C_1\cup C_2}$$ for $$C_1\cup C_2$$. By the uniqueness of $$\alpha_{C_1},\alpha_{C_2},\alpha_{C_1\cap C_2}$$, both $$\alpha_{C_1}$$ and $$\alpha_{C_2}$$ must become the same element at $$\alpha_{C_1\cap C_2}$$, so in (2), considering the element

$$(\alpha_{C_1},-\alpha_{C_2})\in H_m(M,M\setminus C_1;A)\oplus H_m(M,M\setminus C_2;A)$$

this element belongs to the kernel of $$H_m(M,M\setminus C_1;A)\oplus H_m(M,M\setminus C_2;A)\rightarrow H_m(M, M\setminus (C_1\cap C_2);A)$$, and thus we can choose an element of $$H_m(M,M\setminus (C_1\cup C_2);A)$$, and uniqueness follows from the injectivity of

$$0=H_{m+1}(M,M\setminus (C_1\cap C_2);A)\rightarrow H_m(M,M\setminus (C_1\cup C_2))\rightarrow H_m(M,M\setminus C_1;A)\oplus H_m(M,M\setminus C_2;A)$$

For the base case of the induction, it suffices to consider the case where $$M=\mathbb{R}^m$$ and $$A$$ is a convex compact subset. This is because for a compact set of an arbitrary manifold $$M$$, after covering it with Euclidean charts and using compactness, we can assume $$M=\mathbb{R}^m$$, and by using a basis of open balls of $$\mathbb{R}^m$$ and using compactness again, we can additionally assume $$A$$ is convex. Then in this step, both spaces $$\mathbb{R}^m\setminus A$$ and $$\mathbb{R}^m\setminus \{x\}$$ deformation retract to the same space $$S^{m-1}$$, giving an isomorphism, and the proof is complete.

</details>

In this proof, compactness is absolutely necessary to ensure that the inductive process terminates in finitely many steps when constructing $$\alpha$$ inductively using the Mayer-Vietoris sequence. Indeed, when compactness is absent, Poincaré duality takes a somewhat different form, and to express this in a unified formula, we need to introduce the language of sheaf cohomology.

In any case, by [Lemma 8](#lem8) above, if $$M$$ is a compact topological manifold of dimension $$m$$, setting $$C=M$$ yields the following theorem.

<div class="proposition" markdown="1">

<ins id="thm9">**Theorem 9**</ins> Let $$M$$ be a compact connected topological manifold of dimension $$m$$. Then for any orientation sheaf $$\omega_M^A$$, there exists a unique class $$[M]\in H_m(M;A)$$ such that the image of $$[M]$$ under the canonical homomorphism (1) coincides with $$s_x$$.

</div>

Then by [Lemma 8](#lem8), $$H_m(M;A)$$ is a free $$A$$-module of rank 1 generated by $$[M]$$, and different choices of global orientation correspond to different choices of generators of $$H_m(M;A)$$.

<div class="definition" markdown="1">

<ins id="def10">**Definition 10**</ins> The $$[M]$$ defined in [Theorem 9](#thm9) above is called the *fundamental class* of $$M$$ defined by the global orientation $$s$$.

</div>

Moreover, if a homology class $$[M]$$ satisfying the conditions of [Theorem 9](#thm9) exists, we know that this gives rise to a global section $$s:M \rightarrow \Spe(\omega_M^A)$$.

## Poincaré Duality

We can now prove Poincaré's theorem for an $$A$$-orientable manifold. For this, consider the cap product homomorphism

$$-\frown -: H^p(M;A)\otimes_A H_m(M;A) \rightarrow H_{m-p}(M;A)$$

Since $$H_m(M;A)\cong A$$, this homomorphism can be thought of as an $$A$$-module homomorphism from $$H^p(M;A)$$ to $$H_{m-p}(M;A)$$. In particular, introducing the generator $$[M]$$ of $$H_m(M;A)$$, this becomes the homomorphism

$$-\frown [M]: H^p(M;A)\rightarrow H_{m-p}(M;A)$$

<div class="proposition" markdown="1">

<ins id="thm11">**Theorem 11**</ins> For an $$A$$-orientable compact manifold $$M$$ of dimension $$m$$ and its fundamental class $$[M]$$, the above homomorphism

$$-\frown [M]: H^p(M;A)\rightarrow H_{m-p}(M;A)$$

is an isomorphism.

</div>

The proof of this also proceeds by induction using the Mayer-Vietoris sequence, similar to the proof of [Lemma 8](#lem8). However, a somewhat different point is that while [Lemma 8](#lem8) was a statement about compact subsets $$C$$, so compactness could be used actively, this time the statement is about $$M$$ itself, so for example, if a chart $$U$$ of $$M$$ is given, it is not compact, so a simple inductive approach is not possible. For this, we define the following.

<div class="definition" markdown="1">

<ins id="def12">**Definition 12**</ins> A cochain $$\varphi\in C^p(M;A)$$ is *compactly supported* if there exists a compact set $$K\subseteq M$$ such that $$\varphi(\sigma)=0$$ holds for all simplices contained in $$M\setminus K$$. The $$i$$-th homology of the cochain complex of compactly supported cochains is called the $$p$$-th *compactly supported cohomology* and is denoted by $$H_c^p(M;A)$$.

</div>

Then the following equation

$$H_c^p(M;A)\cong \varinjlim_{\text{\scriptsize$K$ compact}}H^p(M,M\setminus K;A)$$

is intuitively obvious and the proof is clear. For each compact set $$K$$,

$$H^p(M,M\setminus K;A)\rightarrow H_c^p(M;A)$$

exists canonically, and this is compatible with the directed system on the right-hand side, so the homomorphism

$$\varinjlim_{\text{\scriptsize$K$ compact}}H^p(M,M\setminus K;A)\rightarrow H_c^p(M;A)$$

is well-defined. That this is an isomorphism can be shown directly. In particular, for any compact manifold $$M$$, $$H_c^p(M,A)\cong H^p(M;A)$$ holds, so the desired result follows from the lemma below.

<div class="proposition" markdown="1">

<ins id="lem13">**Lemma 13**</ins> For any $$A$$-orientable $$m$$-manifold $$M$$, the following isomorphism

$$H_c^p(M;A)\cong H_{m-p}(M;A)$$

holds for all $$p$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

For this, we first need to define the isomorphism. For this purpose, for any compact subset $$K$$, consider the cap product

$$H^p(M,M\setminus K;A)\times H_m(M,M\setminus K;A)\rightarrow H_{m-p}(M;A)$$

Then by [Lemma 8](#lem8), we can find a homology class

$$s_K\in H_m(M,M\setminus K;A)$$

that matches the orientation $$x$$ of $$M$$ when restricted to each point $$x$$. Our claim is that the cap product homomorphism made from these $$s_K$$'s

$$-\frown s_K: H^p(M,M\setminus K;A) \rightarrow H_{m-p}(M;A)$$

satisfies compatibility with respect to the direct system, and thus defines a homomorphism $$H_c^p(M;A)\rightarrow H_{m-p}(M;A)$$. To verify this, suppose another compact subset $$K'$$ containing $$K$$ and the inclusion $$i:K\rightarrow K'$$ are given. Then for any $$\alpha\in H^p(M,M\setminus K;A)$$,

$$i^\ast\alpha\frown s_{K'}=\alpha\frown i_\ast s_{K'}$$

holds by the projection formula ([§Cup Products, ⁋Proposition 6](/en/math/algebraic_topology/cup_products#prop6)), and by the uniqueness in [Lemma 8](#lem8), $$i_\ast s_{K'}=s_K$$, so we know that this well-defines a homomorphism $$H_c^p(M;A)\rightarrow H_{n-p}(M;A)$$.

Our claim is that this homomorphism $$D_M:H_c^p(M;A)\rightarrow H_{n-p}(M;A)$$ is an isomorphism, and to show this, we use induction with the Mayer-Vietoris sequence as in the proof of [Lemma 8](#lem8).

The base step of the induction is when $$M=\mathbb{R}^m$$. In this case, for any ball $$B\subseteq \mathbb{R}^m$$, we know that the orientation $$s_B$$ of $$B$$ gives

$$H_m(\mathbb{R}^m, \mathbb{R}^m\setminus B;A)\cong A$$

and from [§Cohomology, ⁋Proposition 3](/en/math/algebraic_topology/cohomology#prop3), $$H^m(\mathbb{R}^m,\mathbb{R}^m\setminus B;A)\cong A$$, where the $$\alpha_B$$ corresponding to the dual basis of the orientation of $$B$$ satisfies

$$\langle 1\smile \alpha_B, s_B\rangle=\langle 1,\alpha_B\frown s_B\rangle$$

so $$\alpha_B\frown s_B$$ corresponds to the generator of $$H_0(\mathbb{R}^m)\cong A$$, and thus

$$H^p(\mathbb{R}^m,\mathbb{R}^m\setminus B;A)\cong H_{m-p}(\mathbb{R}^m;A)$$

holds for all $$p$$. (For $$p\neq m$$, it is an isomorphism between zero modules, hence a zero map.) Now by increasing the radius of $$B$$ and constructing a directed system covering all of $$\mathbb{R}^m$$, we know that $$H_c^p(M)\rightarrow H_{m-p}(M)$$ is an isomorphism.

Now for the next step, suppose there exist open sets $$U,V$$ of $$M$$ such that $$M=U\cap V$$ and the given proposition holds for $$U,V,U\cap V$$. Then for each compact subset $$K\subset U$$, $$L\subset V$$, consider the relative Mayer-Vietoris sequence

$$\cdots\rightarrow H^k(M,M\setminus(K\cap L);A)\rightarrow H^k(M,M\setminus K;A)\oplus H^k(M,M\setminus L;A)\rightarrow H^k(M,M\setminus(K\cup L);A)\rightarrow \cdots$$

then after excision and taking the limit, we obtain the following commutative diagram

![MVseq_duality](/assets/images/Math/Algebraic_Topology/Poincare_duality-4.png){:style="width:36em" class="invert" .align-center}

and the induction is completed from the inductive process and [\[Homological Algebra\] §Diagram Chasing, ⁋Corollary 2](/en/math/homological_algebra/diagram_chasing#cor2).

However, since there is no assumption that $$M$$ is compact, we need to add some argument. First, suppose $$M$$ is the union of a nested family of open subsets

$$U_1\subset U_2\subset\cdots$$

and the given proposition holds for each of them. Then any compact subset of $$M$$ must be contained in some $$U_i$$, from which we obtain the following isomorphisms

$$H_c^p(M)=\varinjlim_i H^p_c(U_i),\qquad H_{m-p}(M)=\varinjlim_i H_{m-p}(U_i)$$

By the assumption, $$H^p_c(U_i)\rightarrow H_{m-p}(U_i)$$ are all isomorphisms, so we obtain the desired result.

Now consider the case when $$M$$ is an open subset of $$\mathbb{R}^m$$. Then we can first cover $$M$$ with countably many convex open subsets (i.e., open balls) $$U_1,U_2,\ldots$$ each homeomorphic to $$\mathbb{R}^m$$, and since any convex open subset is homeomorphic to $$\mathbb{R}^m$$, we showed in the base step above that the isomorphism of the theorem holds for each of them. Also, the intersection of two convex sets is again a convex set, so by the above induction, the conclusion also holds for $$U_1\cup U_2$$. Next, to show that the conclusion holds for $$U_1\cup U_2\cup U_3$$, we need to show that the intersection

$$(U_1\cup U_2)\cap U_3=(U_1\cap U_3)\cup (U_2\cap U_3)$$

satisfies the given condition, where $$U_1\cap U_3$$, $$U_2\cap U_3$$, and $$U_1\cap U_2\cap U_3$$ are all convex open subsets of $$\mathbb{R}^m$$, satisfying the given condition. Similarly, we know that each of

$$U_1,\quad U_1\cup U_2, \quad U_1\cup U_2\cup U_3,\quad \cdots$$

satisfies the conclusion. Therefore, applying the preceding (infinite) induction to the sequence of nested open subsets

$$U_1\subset U_1\cup U_2\subset U_1\cup U_2\cup U_3\cdots$$

yields the desired result.

Finally, when $$M$$ is an arbitrary manifold, we can use second countability to cover $$M$$ with countable Euclidean charts and go through the same argument as above.

</details>

In particular, in the proof, if $$M$$ were compact, the duality map $$D_M$$ would be exactly the cap product with the fundamental class $$[M]$$.

## Twisted Poincaré Duality

When $$M$$ is not $$A$$-orientable, the main reason [Theorem 11](#thm11) fails is fundamentally because $$\or_M^A$$ fails to be a constant sheaf and is only locally constant. In terms of covering spaces, this means that the monodromy action acts nontrivially on the stalk $$A$$, so when we go "one full circle" and return, the stalk $$A$$ gets twisted and attached. Since this twist is an automorphism of $$A$$, it suffices to consider a bijection of the unit group $$A^\times$$ of $$A$$.

To consider this twist together in the duality, we define *homology with local coefficient*.

<div class="definition" markdown="1">

<ins id="def14">**Definition 14**</ins> A locally constant sheaf $$\mathscr{L}$$ defined on $$M$$ is called a *local coefficient system*.

</div>

Let the stalk of a local system $$\mathscr{L}$$ be $$L$$. Then by [§Covering Spaces, ⁋Theorem 11](/en/math/algebraic_topology/covering_spaces#thm11), we know that for any path $$\alpha:[0,1]\rightarrow M$$, there exists an isomorphism $$\mathscr{L}_{\alpha(0)}\rightarrow \mathscr{L}_{\alpha(1)}$$ between the stalks. This is simply the isomorphism obtained by lifting the path $$\alpha$$ in the covering space $$\Spe(\mathscr{L})\rightarrow M$$. That is, we obtain the following functor

$$\Pi_1(M)\rightarrow \Ab; \qquad x\mapsto \mathscr{L}_x$$

Then fixing a point $$e_0=(1,0,\ldots,0)$$ of $$\Delta^k$$, we define $$C_\bullet(M,\mathscr{L})$$ by

$$C_\bullet(M,\mathscr{L})=\bigoplus_{\sigma:\Delta^k\rightarrow M}\mathscr{L}_{\sigma(e_0)}$$

While $$\mathscr{L}_x\cong L$$ for each $$x$$, the key point of this definition is that the $$L$$ at each point can change through nontrivial automorphisms. The differential map of this chain complex is defined for a singular $$k$$-simplex $$\sigma:\Delta^k \rightarrow M$$ and coefficient $$a\in \mathscr{L}_{\sigma(e_0)}$$ by

$$\partial_k(a\sigma)=\sum_{i=0}^k(-1)^k\mathscr{L}_{\sigma_k}(a) (\sigma|_{[v_0,\ldots, \hat{v}_i,\ldots,v_k]})$$

Here $$\mathscr{L}_{\sigma_k}$$ is obtained by applying the functor $$\Pi_1(M) \rightarrow \Ab$$ to the path in $$M$$ obtained by sending the edge connecting the first vertex $$\sigma(e_0)$$ of the original simplex and the first vertex of the $$k$$-th face. In good situations like ours, we know that using the universal cover $$\widetilde{M}$$ of $$M$$, the monodromy action acting on it (i.e., Deck transformation), and the monodromy representation $$\pi_1(X)\rightarrow \Aut(A)$$, the chain complex obtained by considering

$$C(\widetilde{M})\otimes_{\mathbb{Z}[\pi_1(X)]} A$$

gives the same homology group as the above homology group.

This may seem like an excessive generalization, since to state the non-orientable version of Poincaré duality, we would set the local coefficient system $$\mathscr{L}$$ to be the constant sheaf $$\underline{A}$$. However, through this generalization, we can also generalize the cohomology part, and this generalization makes Poincaré duality more transparent.

For any topological space $$X$$ and sheaf $$\mathscr{F}$$ defined on it, the global section functor

$$\Gamma(X,-):\Sh(X,\mathcal{A})\rightarrow \mathcal{A}$$

is a left exact functor, so its right derived functor exists. To compute this directly, we use the Godement resolution, defined as follows.

Consider a topological space $$X$$ and a sheaf $$\mathscr{F}$$ defined on it, and consider the étalé space $$\Spe(\mathscr{F})$$. We know that $$\mathscr{F}$$ is precisely the sheaf of continuous sections of $$\Spe(\mathscr{F})\rightarrow X$$. Now for any open set $$U$$, define

$$\mathscr{G}_0(U)=\prod_{x\in U}\mathscr{F}_x$$

That is, $$\mathscr{G}_0$$ is the sheaf of set-theoretic (not necessarily continuous) sections of $$\Spe(\mathscr{F})\rightarrow X$$. Our idea is to put into the quotient sheaf $$\mathscr{Q}$$ the parts where locally defined functions fail to become functions when pieced together, through the following sequence induced by the inclusion $$\mathscr{F}\rightarrow \mathscr{G}_0$$

$$0 \rightarrow \mathscr{F}\rightarrow \mathscr{G}_0 \rightarrow \mathscr{Q}\rightarrow 0$$

Then for the sheaf $$\mathscr{Q}$$ as well, we can create a sheaf defined by

$$\mathscr{G}_1(U)=\prod_{x\in U}\mathscr{Q}_x$$

and this defines the following *Godement resolution*

$$0 \rightarrow \mathscr{F}\rightarrow \mathscr{G}_0 \rightarrow \mathscr{G}_1\rightarrow \cdots$$

Intuitively, this repeatedly puts into $$\mathscr{Q}$$ the parts that prevent the existence of global sections of $$\Spe(\mathscr{F})$$, then into $$\mathscr{Q}'$$ the parts that prevent the existence of global sections of $$\mathscr{Q}$$, and so on. This resolution $$\mathscr{G}_\bullet$$ is not an injective resolution, but since each sheaf is a flabby (flasque) sheaf, we can compute the right derived functors $$R^i\Gamma$$ of the global section functor through it.

<div class="definition" markdown="1">

<ins id="def14">**Definition 14**</ins> For a topological space $$X$$ and a sheaf $$\mathscr{F}$$ defined on it, the $$k$$-th homology of the sequence of global sections of the Godement resolution

$$0 \rightarrow \mathscr{F}(X)\rightarrow \mathscr{G}_0(X)\rightarrow \mathscr{G}_1(X)\rightarrow \cdots$$

is denoted by

$$H^k(X; \mathscr{F})$$

and is called the *sheaf cohomology*.

</div>

Now Poincaré duality is generalized to the following isomorphism

$$H^k(M;\mathscr{L})\cong H_{m-k}(M;\or_M^A\otimes \mathscr{L})$$

To return to the original Poincaré duality from this, first set $$\mathscr{L}$$ to be the constant sheaf $$\underline{A}$$. Then for nice spaces like manifolds, it is known that sheaf cohomology $$H^k(M;\underline{A})$$ and singular cohomology $$H^k(M;A)$$ are isomorphic, so we obtain the isomorphism

$$H^k(M;A)\cong H_{m-k}(M;\or_M^A)$$

Additionally, if $$M$$ is $$A$$-orientable, $$\or_M^A$$ also becomes a constant sheaf, from which we can recover the classical Poincaré duality

$$H^k(M;A)\cong H_{m-k}(M;A)$$

## Poincaré Duality and Cup Product

So far, we have freely used the cup product on the cohomology ring and the cap product defined from it. However, if someone asks *what* the cup product is, it would be difficult to answer. The answer is simple:

> Cup product is the Poincaré dual of intersection.

To explain rigorously what this means would require at least as much additional effort as we have put in so far. However, to understand intuitively what this means, the following example is probably sufficient.

<div class="example" markdown="1">

<ins id="ex15">**Example 15**</ins> Consider the torus $$T^2=S^1\times S^1$$. From the Künneth formula, we know that the cohomology of $$T^2$$ is

$$H^0(T^2;\mathbb{Z})\cong \mathbb{Z}, \quad H^1(T^2;\mathbb{Z})\cong \mathbb{Z}^2,\quad H^2(T^2;\mathbb{Z})$$

The only non-trivial product in this cohomology ring is the product of the two generators $$\alpha,\beta$$ of $$H^1(T^2;\mathbb{Z})$$. According to [§Cohomology, ⁋Proposition 3](/en/math/algebraic_topology/cohomology#prop3), these correspond to the duals of two circles of $$T^2$$. Taking their cup product gives a generator of $$H^2(T^2;\mathbb{Z})$$, which follows immediately from the definition of cup product or algebraically since

$$H^2(T^2;\mathbb{Z})=H^1(T^2;\mathbb{Z})\otimes H^1(T^2;\mathbb{Z})\cong \mathbb{Z}\otimes \mathbb{Z}\cong \mathbb{Z}$$

is generated by $$\alpha\otimes \beta$$.

At this point, the reason why their cup product does not appear as a constant multiple other than $$\pm 1$$ times $$\alpha\times \beta$$ is geometrically as follows. If we denote the homology classes corresponding to $$\alpha$$, $$\beta$$ by $$a,b$$, the intersection of $$a$$ and $$b$$ meets at only one point as shown in the following figure.

![Torus_intersection](/assets/images/Math/Algebraic_Topology/Poincare_duality-5.png){:style="width:30%" class="invert" .align-center}

At this point, classifying how the two curves meet and designating one as positive and one as negative direction is equivalent to giving an orientation of $$T^2$$.

Then, under this geometric interpretation, how can we explain that $$\alpha^2=0$$? If we literally compute the intersection $$a\cap a$$, it becomes $$a$$ again. The reason this computation gets tangled is that two cycles (in this case, two copies of $$a$$) are not in *general position*. Roughly speaking, if two lines in $$\mathbb{R}^2$$ are given, they generally meet at one point except when they are parallel (including the case where they coincide), and the concept of general position generalizes this.

Now consider curves in $$T^2$$ with homology class $$a$$. These are likely not to meet each other, and if they do meet (excluding the case of tangency, which is not general position), they will meet in the following pattern

![intersections_on_torus](/assets/images/Math/Algebraic_Topology/Poincare_duality-6.png){:style="width:40%" class="invert" .align-center}

At first glance, this seems to create two intersection points, but in the figure above, the two intersection points have opposite signs. That is, if we take the cross product with the line as the first vector and the curve as the second vector, one will give a vector pointing outward and the other pointing inward, hence opposite signs. Thus the two intersection points cancel out, and the intersection becomes $$0$$, so $$\alpha\smile\alpha=0$$.

</div>

--- 

**References**

[Hat] A. Hatcher, *Algebraic Topology*. Cambridge University Press, 2022.  
[May] J. P. May, *A concise course in algebraic topology*.

---
