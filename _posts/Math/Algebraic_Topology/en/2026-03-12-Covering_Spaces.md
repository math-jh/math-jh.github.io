---
title: "Covering Spaces"
description: "This post defines simply connected spaces and the concepts of covering spaces and covering maps. It introduces fundamental methods for computing fundamental groups through the properties of evenly covered neighborhoods."
excerpt: "Equivalent conditions for simply connected spaces, covering spaces, and the Seifert-van Kampen theorem"

categories: [Math / Algebraic Topology]
permalink: /en/math/algebraic_topology/covering_spaces
sidebar: 
    nav: "algebraic_topology-en"

date: 2025-07-27
weight: 4
translated_at: 2026-06-24T02:00:03+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-24T02:00:03+00:00
---
In the previous post, we defined the fundamental group $$\pi_1(X)$$ and examined some of its basic properties. The following lemma is then almost immediate from the definitions.

<div class="proposition" markdown="1">

<ins id="lem1">**Lemma 1**</ins> For a path-connected space $$X$$, the following are equivalent.

1. Any two paths $$p,q$$ with the same endpoints are always path homotopic.
2. Every loop $$f:S^1 \rightarrow X$$ is null-homotopic.
3. For every loop $$f:S^1 \rightarrow X$$, there exists a continuous map $$\widetilde{f}:D^2 \rightarrow X$$ whose restriction to the boundary $$S^1$$ is $$f$$.
4. $$\pi_1(X)=0$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

The equivalence of the first, second, and last conditions is obvious by considering the loop $$p\ast\bar{q}$$ for two paths $$p,q$$. Thus it suffices to show that the third condition is equivalent to these.

First, assume the first condition. For any loop $$f:S^1 \rightarrow X$$, there exists a homotopy $$(f_t)$$ with $$f_1=f$$ and $$f_0$$ the constant map to a fixed point $$x_0$$. Then the formula

$$\widetilde{f}(\mathrm{x})=\begin{cases}f_{\lvert\mathrm{x}\rvert}(\mathrm{x}/\lvert\mathrm{x}\rvert)&\text{if $\lvert\mathrm{x}\rvert\neq 0$}\\ x_0&\text{if $\lvert\mathrm{x}\rvert=0$}\end{cases}$$

defines the continuous map required by the third condition. Conversely, assuming the third condition, for any loop $$f$$, setting $$f_t(\mathrm{x})=\widetilde{f}(t\mathrm{x})$$ yields a homotopy from $$f_1=f$$ to the constant map.

</details>

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> If the equivalent conditions of [Lemma 1](#lem1) hold, a path-connected space $$X$$ is called a *simply connected space*.

</div>

## Covering Spaces

For the remainder of this post, we consider only path-connected spaces for convenience. Computing the fundamental group of a non-simply-connected space requires several methods; one of the most basic and essential is the use of covering spaces.

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> For a continuous surjection $$p:E \rightarrow B$$, an open subset $$U$$ of $$B$$ is said to be *evenly covered* by $$p$$ if $$p^{-1}(U)$$ is a union of disjoint open subsets of $$E$$, each homeomorphic to $$U$$. If every $$x\in B$$ has an open neighborhood $$U$$ that is evenly covered by $$p$$, then $$p$$ is called a *covering map* and $$E$$ a *covering space*.

</div>

The definition may appear somewhat complicated, but it is essentially captured by the following picture.

![S1_covering](/assets/images/Math/Algebraic_Topology/Covering_Spaces-1.svg){:style="width:26em" class="invert" .align-center}

This depicts the covering map

$$p:\mathbb{R}\rightarrow S^1;\quad t\mapsto (\cos 2\pi t, \sin 2\pi t)$$

and we know that it satisfies the conditions of [Definition 3](#def3). In general, covering maps behave well with respect to subspaces and product spaces, as one can easily verify.

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4**</ins> The following hold.

1. For a covering map $$p:E \rightarrow B$$ and a subspace $$A$$ of $$B$$, the restriction $$p\vert_{p^{-1}(A)}:p^{-1}(A) \rightarrow A$$ is a covering map.
2. For two covering maps $$p_1:E_1 \rightarrow B_1$$ and $$p_2:E_2\rightarrow B_2$$, the product $$p_1\times p_2:E_1\times E_2 \rightarrow B_1\times B_2$$ is a covering map.

</div>

## Fundamental Theorems of Covering Spaces

By the functoriality of the fundamental groupoid $$\Pi_1:\Top \rightarrow \Grpd$$, any continuous map $$p:E \rightarrow B$$ defines a groupoid homomorphism

$$\Pi_1(f):\Pi_1(E) \rightarrow \Pi_1(B)$$

In particular, for any $$y_0, y_1\in E$$, the homomorphism

$$\Hom_{\Pi_1(E))}(y_0, y_1)\rightarrow \Hom_{\Pi_1(B)}(p(y_0), p(y_1))\tag{$\ast$}$$

is well defined. If $$B$$ is path-connected and $$p(y_0)=p(y_1)$$, this becomes a (groupoid) homomorphism into the fundamental group $$\pi_1(B)$$. If $$E$$ carries all the information about the fundamental group (or groupoid) of $$B$$, then at least this homomorphism should be surjective.

<div class="definition" markdown="1">

<ins id="def5">**Definition 5**</ins> Fix a continuous map $$p:E\rightarrow B$$. For any continuous map $$f:X \rightarrow B$$, a *lifting* of $$f$$ with respect to $$p$$ is a map $$\widetilde{f}:X\rightarrow E$$ satisfying $$p\circ\widetilde{f}=f$$.

</div>

The point of this definition is that when $$X=I$$, so that $$f$$ is a path in $$B$$, a lifting of $$f$$ with respect to $$p$$—if it exists—lies in the preimage of $$f$$ under the homomorphism ($$\ast$$). Our claim is that such a lifting always exists when $$p$$ is a covering map.

<div class="proposition" markdown="1">

<ins id="lem6">**Lemma 6**</ins> Let $$p:E \rightarrow B$$ be a covering map and let $$y_0$$ be an arbitrary point of $$E$$. Then for every path $$\alpha:I \rightarrow B$$ starting at $$x_0=p(y_0)$$, there exists a unique lifting $$\widetilde{\alpha}:I \rightarrow E$$ starting at $$y_0$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, since $$p$$ is a covering map, there exists an open cover $$(U_i)$$ of $$B$$ such that each $$U_i$$ is evenly covered by $$p$$. Then $$(\alpha^{-1}(U_i))$$ is an open cover of $$I$$, so it admits a finite subcover. By the Lebesgue number lemma, we can find a subdivision of $$I$$

$$0=s_0<s_1<\cdots<s_n=1$$

such that each $$\alpha([s_i,s_{i+1}])$$ lies in some $$U$$. Set $$\widetilde{\alpha}(0)=y_0$$, and assume inductively that $$\widetilde{\alpha}$$ is defined for $$0\leq s\leq s_i$$; we define it on $$[s_i,s_{i+1}]$$. By the choice of the $$s_i$$, the image $$\alpha([s_i,s_{i+1}])$$ lies in an open set $$U$$ evenly covered by $$p$$. Thus we can write $$p^{-1}(U)$$ as a disjoint union $$\coprod_{j\in J}V_j$$ of open sets homeomorphic to $$U$$. For the unique $$V_j$$ containing $$\widetilde{\alpha}(s_i)$$, we define

$$\widetilde{\alpha}(s)=(p\vert_{V_j})^{-1}(\alpha(s))$$

Uniqueness follows because each $$[s_i,s_{i+1}]$$ is connected, so the component containing $$\alpha(s_i)$$ is determined inductively at each step.

</details>

The proof may appear somewhat technical, but the key idea is transparent: any path starting at $$x_0\in B$$ remains in some evenly covered neighborhood $$U$$ of $$x_0$$ for at least a short time, and by definition $$p^{-1}(U)$$ is a union of disjoint open subsets of $$E$$ homeomorphic to $$U$$; knowing which of these contains the starting point determines, by connectedness, the component in which the path stays during this short interval. The Lebesgue number lemma is used only to ensure that this process terminates after finitely many steps.

Returning to the groupoid homomorphism ($$\ast$$), [Lemma 6](#lem6) implies that for a covering space $$p:E \rightarrow B$$, given any $$x_0,x_1\in B$$ and a path $$\alpha$$ between them, a choice of $$y_0\in p^{-1}(x_0)$$ determines $$y_1\in p^{-1}(x_1)$$ and $$\widetilde{\alpha}\in \Hom_{\Pi_1(E)}(y_0,y_1)$$. The natural question is whether, for $$\alpha'$$ path-homotopic to $$\alpha$$, the same choice of $$y_0$$ yields the same $$y_1$$ and the same homotopy class. The answer is affirmative when $$p$$ is a covering map.

<div class="proposition" markdown="1">

<ins id="lem7">**Lemma 7**</ins> Let $$p:E \rightarrow B$$ be a covering map and let $$y_0$$ be an arbitrary point of $$E$$; set $$p(y_0)=x_0$$. Then for every continuous map $$F:I\times I \rightarrow B$$ with $$F(0,0)=x_0$$, there exists a unique lifting $$\widetilde{F}:I\times I \rightarrow E$$ with $$\widetilde{F}(0,0)=y_0$$. Moreover, if $$F$$ is a path homotopy, then so is $$\widetilde{F}$$.

</div>

The proof is essentially identical to that of [Lemma 6](#lem6), so we omit it. What matters is that by this lemma, path homotopy classes are preserved: for a covering space $$p:E \rightarrow B$$ and a path class $$[\alpha]\in\Hom_{\Pi_1(B)}(x_0,x_1)$$, a choice of $$y_0\in p^{-1}(x_0)$$ uniquely determines a path class $$[\widetilde{\alpha}]\in \Hom_{\Pi_1(E)}(y_0,y_1)$$ in $$E$$.

Now consider again the fundamental groupoid $$\Pi_1(B)$$ and fix a covering map $$p:E \rightarrow B$$. By the evenly covered condition, the fiber $$p^{-1}(x)$$ over each $$x\in B$$ is a discrete set. Then for any path class $$[\alpha]\in\Hom_{\Pi_1(B)}(x_0,x_1)$$, choosing $$y_0\in p^{-1}(x_0)$$ defines a unique path class $$[\widetilde{\alpha}]$$ by [Lemma 7](#lem7), and hence a unique $$y_1\in p^{-1}(x_1)$$. In other words, $$[\alpha]$$ defines a function $$p^{-1}(x_0)\rightarrow p^{-1}(x_1)$$.

<div class="definition" markdown="1">

<ins id="def8">**Definition 8**</ins> In the above situation, the function $$p^{-1}(x_0)\rightarrow p^{-1}(x_1)$$ is called the *transport map* and is denoted by $$T_{[\alpha]}$$.

</div>

The transport map is bijective. Indeed, given any $$y_1\in p^{-1}(x_1)$$, we can use the path class $$[\overline{\alpha}]\in\Hom_{\Pi_1(B)}(x_1,x_0)$$ to find a path starting at $$y_1$$ and ending at some element $$y_0\in p^{-1}(x_0)$$, and this process is unique by [Lemma 7](#lem7). Similarly, by the uniqueness of liftings, this correspondence respects path concatenation. That is, the assignment sending $$x\in \Pi_1(B)$$ to $$p^{-1}(x)$$ and $$[\alpha]\in\Hom_{\Pi_1(B)}(x_0,x_1)$$ to $$T_{[\alpha]}:p^{-1}(x_0)\rightarrow p^{-1}(x_1)$$ is functorial.

<div class="definition" markdown="1">

<ins id="def9">**Definition 9**</ins> The functor $$\Pi_1(B) \rightarrow \Set$$ defined above is called the *monodromy functor* defined by $$p$$ and is denoted by $$M_p$$.

</div>

For a fixed base space $$B$$, we define in the obvious way the category $$\Cov(B)$$ of covering spaces of $$B$$. Explicitly, the objects of this category are covering maps $$p:E\rightarrow B$$, and a morphism between these is a commutative diagram

![morphism_of_covering_spaces](/assets/images/Math/Algebraic_Topology/Covering_Spaces-2.svg){:style="width:6.75em" class="invert" .align-center}

Through this, assigning to each $$p\in \Cov(B)$$ its monodromy functor $$M_p$$ defines a functor

$$M:\Cov(B) \rightarrow \Fun(\Pi_1(B),\Set)$$

and the main result of this post is that this is an equivalence of categories. To prove this, one must verify much starting from the functoriality of the above correspondence, but ultimately the most essential step is that given any functor $$\Pi_1(B)\rightarrow \Set$$, one can construct a covering space $$E \rightarrow B$$ from it. To this end, given any functor $$F:\Pi_1(B) \rightarrow \Set$$, tracing the monodromy functor backwards makes it obvious how to define $$p:E\rightarrow B$$ as a function between sets: for each $$x\in \Pi_1(B)$$, the set $$F(x)$$ will correspond to the fiber of $$p$$ over $$x$$, so we set the projection to be

$$p:E=\coprod_{x\in B}F(x) \rightarrow B$$

The problem is to endow $$E$$ with a topology making this a covering space. If such a topology exists, then for each $$x$$ there should be an open neighborhood $$U$$ such that $$p^{-1}(U)$$ is homeomorphic to $$U\times F(x)$. For the familiar example $$\mathbb{R}\rightarrow S^1$$, this is intuitively clear: $$p^{-1}(U)$$ is a disjoint union of copies of $$U$$, so any element of $$p^{-1}(U)$$ is determined by which copy it lies in ($$F(x)$$) and which point of that copy ($$U$$). We will conversely construct a bijection $$\phi:p^{-1}(U) \rightarrow U\times F(x)$$ and use it to define a topology on $$p^{-1}(U)$$. Showing that these $$\phi$$ agree on overlaps, and hence that the bijections assemble into a suitable topology on $$E$$ with the desired properties, is routine; the crux of the proof is the definition of $$\phi$$.

By the form of $$p$$ defined above, we know that $$p^{-1}(U)$$ is the collection of $$F(x')$$ for $$x'\in U$$. Then the first coordinate of $$\phi(x')$$ should of course be $$x'$$ itself, and the second coordinate should be an element of $$F(x)$$ connected to $$x'$$ by a path, as suggested by the transport map. However, for this to be information contained in $$\Pi_1(B)$$, we need

1. $$U$$ to be path-connected, so that a path class $$[\alpha]\in \Hom_{\Pi_1(B)}(x,x')$$ always exists between $$x$$ and $$x'$$, and
2. such a path class to be uniquely determined.

The first condition is simply that $$B$$ be locally path-connected. The second is more subtle: two paths in $$U$$ with the same endpoints must define the same path class *in $$B$$*. This is a weaker condition than being locally simply connected.

<div class="definition" markdown="1">

<ins id="def10">**Definition 10**</ins> A topological space $$X$$ is *semi-locally simply connected* if every $$x\in X$$ has an open neighborhood $$U$$ such that every loop in $$U$$ is contractible in $$X$$.

</div>

For the above argument to hold, we see that $$B$$ must satisfy, in addition to the previously assumed path-connectedness, the two conditions of being locally path-connected and semi-locally simply connected. Combining the above discussion, we obtain the following result.

<div class="proposition" markdown="1">

<ins id="thm11">**Theorem 11 (Fundamental theorem of covering spaces)**</ins> For a path-connected, locally path-connected, semi-locally simply connected space $$B$$, there exists an equivalence

$$M:\Cov(B) \rightarrow \Fun(\Pi_1(B), \Set)$$

between the two categories.

</div>

For example, any path-connected topological manifold always satisfies these conditions.

We must now examine what $$\Fun(\Pi_1(B), \Set)$$ is. More generally, consider what a functor $$\mathscr{G}\rightarrow \Set$$ is for an arbitrary groupoid $$\mathscr{G}$$. By definition, this consists of

- a set $$S_G$$ corresponding to each object $$G\in \mathscr{G}$$,
- a bijection $$S_G \rightarrow S_H$$ corresponding to each (iso)morphism $$G \rightarrow H$$ in $$\mathscr{G}$$.

This alone does not yet reveal the nature of a functor $$\mathscr{G}\rightarrow \Set$$, so consider the special case where $$\mathscr{G}$$ has only one object $$\ast$$, so that all morphisms of $$\mathscr{G}$$ are automorphisms of $$\ast$$—that is, $$\mathscr{G}$$ is a group. Under this assumption, a functor $$\mathscr{G}\rightarrow \Set$$ is the following data:

- a set $$S$$ corresponding to the unique object of $$\mathscr{G}$$,
- a bijection $$g\cdot-: S\rightarrow S$$ corresponding to each automorphism $$g:\ast \rightarrow \ast$$.

That is, as the notation suggests, this is precisely a group action of $$\mathscr{G}$$; $$\Fun(\mathscr{G},\Set)$$ is exactly the collection of $$\mathscr{G}$$-sets, with morphisms the $$\mathscr{G}$$-equivariant maps. For a general groupoid $$\mathscr{G}$$, this is simply several groups acting separately on several sets, with the requirement that isomorphic objects $$G,H$$ of $$\mathscr{G}$$ act in the same way on their respective (isomorphic) sets $$S_G$$ and $$S_H$$.

Since $$B$$ is path-connected, the fundamental groupoid $$\Pi_1(B)$$ is a connected groupoid, and hence equivalent as a category to the group $$\pi_1(B,x)$$ for any $$x\in B$$. Thus a groupoid action of $$\Pi_1(B)$$ is nothing but a group action of $$\pi_1(B,x)$$ replicated along the isomorphisms in $$\Pi_1(B)$$. Consequently, the information in [Theorem 11](#thm11) is essentially contained in the skeleton. Let us therefore consider

$$\sk(M):\sk(\Cov(B))\rightarrow \sk(\Fun(\Pi_1(X), \Set))$$

This is an equivalence taking isomorphism classes of covering spaces to the monodromy functor $$M_p$$ up to natural isomorphism—that is, to $$\Pi_1(X)$$-sets up to isomorphism. In general, since

$$\sk(\Fun(\Pi_1(X),\Set))\simeq\Fun(\sk(\Pi_1(X)), \Set)$$

and using again that $$X$$ is path-connected, we know that there exists a categorical equivalence taking isomorphism classes of covering spaces to a $$\pi_1(X,x)$$-set.

Now, recalling [\[Algebraic Structures\] §Group Actions, ⁋Theorem 14](/en/math/algebraic_structures/group_actions#thm14) and its proof, given any $$G$$-set $$E$$ we can decompose $$E$$ into orbits of $$G$$; the restriction of the action to each orbit is transitive, and these are isomorphic to $$G/H$$ with the canonical $$G$$-action for a suitable subgroup $$H$$ of $$G$$. Thus, if we restrict attention to transitive group actions, the definition of the monodromy functor implies that on the target side this corresponds to considering only *connected* covers. That is, we have an equivalence

$$\left\{\text{isomorphism classes of covering spaces of $B$}\right\}\simeq \left\{\text{transitive $\pi_1(B,x)$-sets}\right\}$$

and considering the skeleton category of transitive $$\pi_1(B,x)$$-sets up to isomorphism, we finally obtain the equivalence

$$\left\{\text{isomorphism classes of covering spaces of $B$}\right\}\simeq \left\{\text{conjugacy classes of subgroups of $\pi_1(B,x)$}\right\}$$

Now, each of these categories is nothing but a partially ordered set ([\[Category Theory\] §Categories, ⁋Example 3](/en/math/category_theory/categories#ex3)), and this equivalence is an isomorphism of posets. Hence we obtain the following result.

<div class="proposition" markdown="1">

<ins id="cor12">**Corollary 12 (Fundamental theorem of covering spaces, classical version)**</ins> For a path-connected, locally path-connected, semi-locally simply connected space $$B$$, there exists a Galois correspondence between the set of isomorphism classes of connected covering spaces and the conjugacy classes of subgroups of $$\pi_1(B)$$.

</div>

Explicitly, given a covering space $$p:E \rightarrow B$$, a subgroup is defined via $$\pi_1(p):\pi_1(E)\rightarrow \pi_1(B)$$, and two transitive $$G$$-sets $$X\cong G/H$$ and $$Y\cong G/K$$ are isomorphic if and only if $$H$$ and $$K$$ are conjugate, which yields the above result. On the other hand, if instead of conjugacy classes of subgroups of $$\pi_1(B,x)$$ we consider the subgroups themselves, this corresponds to choosing one representative from each isomorphism class of covering spaces; this is exactly the same as fixing a base point of $$B$$ and considering *pointed* covering maps $$p:(E, y)\rightarrow (B,x)$$, viewing the elements of their isomorphism classes separately. That is, we have a Galois correspondence

$$\left\{\text{isomorphism classes of \textit{pointed} covering spaces of $B$}\right\}\simeq \left\{\text{subgroups of $\pi_1(B,x)$}\right\}$$

Putting this in a more familiar form, for any $$H\leq \pi_1(B,x)$$ we can construct the corresponding covering space $$E_H$$, and then for the automorphism group $$\Aut(E_H/B)$$ of $$E_H$$,

$$\Aut(E_H/B)\cong N_G(H)/H$$

holds. This is called the *Deck transformation group* of $$E_H$$. More generally, automorphisms of covering spaces (obtained by choosing different elements of the fiber $$p^{-1}(x)$$) correspond to taking inner automorphisms of subgroups of $$\pi_1(B,x)$$; these are called *Deck transformations*.

On the other hand, the poset of subgroups (or conjugacy classes of subgroups) of $$\pi_1(B,x)$$ has a minimal element $$\left\{e\right\}$$. By the above Galois correspondence, this corresponds to a *universal cover* $$\widetilde{B}$$. The Deck transformation group of this covering space is isomorphic to $$\pi_1(B,x)$$, and

## Seifert–van Kampen Theorem

While the familiar well-behaved spaces may sometimes have fundamental group or homology computable directly from the definition, in most cases such a computation is excessively complicated or nearly impossible. Our idea is to decompose a large space into smaller pieces in order to compute its fundamental group.

The simplest such method is the case where a space $$X$$ is the union of two open sets $$X=U\cup V$$. Then by [\[Topology\] §Presheaves, ⁋Lemma 1](/en/math/topology/presheaves#lem1), the diagram

![union_as_colimit](/assets/images/Math/Algebraic_Topology/Covering_Spaces-3.svg){:style="width:7.54em" class="invert" .align-center}

is a colimit diagram. In this case, we aim to describe $$\Pi_1(X)$$ in terms of $$\Pi_1(U)$$, $$\Pi_1(V)$$, and $$\Pi_1(U\cap V)$$ by applying the fundamental groupoid functor $$\Pi_1$$ to this diagram. On the other hand, [\[Topology\] §Presheaves, ⁋Lemma 1](/en/math/topology/presheaves#lem1) also tells us that for any open covering $$(U_i)$$, the diagram

![general_union_colimit](/assets/images/Math/Algebraic_Topology/Covering_Spaces-4.svg){:style="width:8.27em" class="invert" .align-center}

is a colimit diagram. Our claim is that if the fundamental groupoids of the $$(U_i)$$ and their finite intersections are all known, then we can compute the fundamental groupoid of $$\Pi_1(X)$$ from these.

<div class="proposition" markdown="1">

<ins id="thm13">**Theorem 13 (Seifert–van Kampen)**</ins> Let $$X$$ be a topological space with a path-connected open cover $$\mathcal{O}=(U_i)$$, and assume that finite intersections of elements of $$\mathcal{O}$$ again belong to $$\mathcal{O}$$. Then the colimit of the $$\mathcal{O}$$-shaped diagram $$\Pi_1:\mathcal{O}\rightarrow\Grpd$$ exists and is isomorphic to $$\Pi_1(X)$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

That is, for any groupoid $$\mathscr{G}\in\Grpd$$ and any cocone $$\lambda:\Pi_1\vert_\mathcal{O}\Rightarrow \mathscr{G}$$, we must show that there exists a $$\widetilde{\lambda}$$ such that for each $$U\in \mathcal{O}$$, $$\widetilde{\lambda}$$ and $$\lambda$$ agree. Naturally, for any $$x\in X$$ we find a $$U$$ with $$x\in U$$; since $$\lambda_U$$ is defined on this $$U$$, we set $$\widetilde{\lambda}(x)=\lambda_U(x)$$. That this is independent of the choice of $$U$$ is obvious, because for any $$U_1,U_2$$ containing $$x$$, both $$\lambda_{U_1}(x)$$ and $$\lambda_{U_2}(x)$$ must agree with $$\lambda_{U_1\cap U_2}(x)$$. For morphisms we can define them similarly: for any path $$f$$ completely contained in some $$U\in \mathcal{O}$$, this definition is well-defined for the same reason, and the only thing that remains to be shown is how to define it when the path does not lie in a single $$U\in \mathcal{O}$$. But in this case we simply use concatenation of paths. We must show that this is always defined and well-defined.

</details>

Now, just as when we obtained [Corollary 12](#cor12) above, applying this theorem to a single object and thus replacing $$\Grpd$$ with $$\Grp$$, and using that the colimit in $$\Grp$$ is the free product, we obtain the following result.

<div class="proposition" markdown="1">

<ins id="cor14">**Corollary 14 (Seifert–van Kampen theorem, classical version)**</ins> Let a topological space $$X$$ be the union of two connected open subsets $$U,V$$, and let $$U\cap V$$ be connected. Then the diagram

![van_Kampen](/assets/images/Math/Algebraic_Topology/Covering_Spaces-5.svg){:style="width:18.89em" class="invert" .align-center}

is a pushout diagram, and the resulting map $$\pi_1(U)\ast_{\pi_1(U\cap V)}\pi_1(V)\rightarrow \pi_1(X)$$ is an isomorphism.

</div>

## Hurewicz Theorem

Homology groups have a simpler structure than the fundamental group. For example, $$\pi_1(X)$$ need not be abelian in general, but $$H_1(X)$$ is abelian by definition. However, as we saw in [§Homology, ⁋Example 8](/en/math/algebraic_topology/homology#ex8), the elements of $$H_1(X)$$ can also be thought of as a kind of loop, so a relationship between them is to be expected.

<div class="proposition" markdown="1">

<ins id="thm15">**Theorem 15 (Hurewicz)**</ins> Fix a path-connected space $$X$$. Then for each $$n$$, there exists a group homomorphism

$$h_n:\pi_n(X) \rightarrow H_n(X)$$

In particular, for $$n=1$$, $$h_1$$ is surjective and $$\ker h_1$$ is the commutator subgroup $$[\pi_1(X),\pi_1(X)]$$ of $$\pi_1(X)$$, so by the first isomorphism theorem

$$H_1(X)\cong \pi_1(X)/\ker h_1=\pi_1(X)/[\pi_1(X),\pi_1(X)]=\pi_1(X)^\ab$$

More generally, if $$\pi_i(X)=0$$ for all $$i< n$$, then $$h_n$$ is an isomorphism and $$h_{n+1}$$ is surjective.

</div>

The Hurewicz homomorphism $$h_n$$ is given by $$f_\ast([S^n])$$ for any $$f:S^n \rightarrow X$$. Here $$[S^n]$$ is the generator of $$H_n(S^n)\cong \mathbb{Z}$$.

---

**References**

[Hat] A. Hatcher, *Algebraic Topology*. Cambridge University Press, 2022.  
[May] J. P. May, *A concise course in algebraic topology*.  
[Mun] James Munkres, *Topology*. Prentice Hall, 2000.  
[Tao] Terence Tao, [van Kampen's theorem via covering spaces](https://terrytao.wordpress.com/2012/10/28/van-kampens-theorem-via-covering-spaces/).
