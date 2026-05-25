---
title: "Covering Spaces"
excerpt: "Equivalent conditions for simply connected, covering spaces, and the Seifert–van Kampen theorem"

categories: [Math / Algebraic Topology]
permalink: /en/math/algebraic_topology/covering_spaces
header:
    overlay_image: /assets/images/Math/Algebraic_Topology/Covering_Spaces.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_topology-en"

date: 2026-03-12
last_modified_at: 2026-03-12
weight: 4
translated_at: 2026-05-25T15:30:03+00:00
translation_source: kimi-cli
last_polished_at: 2026-05-25T15:30:03+00:00
---
In the previous post, we defined the fundamental group $$\pi_1(X)$$ and examined its basic properties. The following lemma is then almost immediate from the definitions.

<div class="proposition" markdown="1">

<ins id="lem1">**Lemma 1**</ins> For a path-connected space $$X$$, the following are equivalent.

1. Any two paths $$p,q$$ sharing endpoints are path homotopic.
2. Every loop $$f:S^1 \rightarrow X$$ is null-homotopic.
3. For every loop $$f:S^1 \rightarrow X$$, there exists a continuous map $$\widetilde{f}:D^2 \rightarrow X$$ whose restriction to the boundary $$S^1$$ is $$f$$.
4. $$\pi_1(X)=0$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

The equivalence of the first, second, and last conditions is immediate by considering the loop $$p\ast\bar{q}$$ for two paths $$p,q$$. Thus it suffices to show that the third condition is equivalent to these.

First, assume the first condition. Then for any loop $$f:S^1 \rightarrow X$$, there exists a homotopy $$(f_t)$$ with $$f_1=f$$ and $$f_0$$ the constant map at a fixed point $$x_0$$. The formula

$$\widetilde{f}(\mathrm{x})=\begin{cases}f_{\lvert\mathrm{x}\rvert}(\mathrm{x}/\lvert\mathrm{x}\rvert)&\text{if $\lvert\mathrm{x}\rvert\neq 0$}\\ x_0&\text{if $\lvert\mathrm{x}\rvert=0$}\end{cases}$$

defines the continuous map required by the third condition. Conversely, assuming the third condition, given any loop $$f$$, setting $$f_t(\mathrm{x})=\widetilde{f}(t\mathrm{x})$$ yields a homotopy from $$f_1=f$$ to a constant map.

</details>

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> If the equivalent conditions of [Lemma 1](#lem1) hold, we call a path-connected $$X$$ a *simply connected space*.

</div>

## Covering Spaces

For the remainder of this post, we assume all spaces are path-connected for convenience. Computing the fundamental group of a space that is not simply connected requires several tools; one of the most fundamental and essential is the use of covering spaces.

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> For a continuous surjection $$p:E \rightarrow B$$, an open set $$U\subseteq B$$ is said to be *evenly covered* by $$p$$ if $$p^{-1}(U)$$ is a disjoint union of open subsets of $$E$$, each homeomorphic to $$U$$ via $$p$$. If every $$x\in B$$ has an open neighborhood that is evenly covered by $$p$$, then $$p$$ is called a *covering map* and $$E$$ is called a *covering space*.

</div>

Although the definition appears somewhat involved, it is helpful to keep the following picture in mind.

![S1_covering](/assets/images/Math/Algebraic_Topology/Covering_Spaces-1.png){:style="width:26em" class="invert" .align-center}

This depicts the covering map

$$p:\mathbb{R}\rightarrow S^1;\quad t\mapsto (\cos 2\pi t, \sin 2\pi t)$$

and one can verify that it satisfies the conditions of [Definition 3](#def3). In general, covering maps behave well with respect to subspaces and product spaces, as is easily proved.

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4**</ins> The following hold.

1. For a covering map $$p:E \rightarrow B$$ and a subspace $$A\subseteq B$$, the restriction $$p\vert_{p^{-1}(A)}:p^{-1}(A) \rightarrow A$$ is a covering map.
2. For covering maps $$p_1:E_1 \rightarrow B_1$$ and $$p_2:E_2\rightarrow B_2$$, the product map $$p_1\times p_2:E_1\times E_2 \rightarrow B_1\times B_2$$ is a covering map.

</div>

## Fundamental Theorem of Covering Spaces

By the functoriality of the fundamental groupoid $$\Pi_1:\Top \rightarrow \Grpd$$, any continuous map $$p:E \rightarrow B$$ induces a groupoid homomorphism

$$\Pi_1(p):\Pi_1(E) \rightarrow \Pi_1(B)$$

In particular, for any $$y_0, y_1\in E$$, the induced map

$$\Hom_{\Pi_1(E))}(y_0, y_1)\rightarrow \Hom_{\Pi_1(B)}(p(y_0), p(y_1))\tag{$\ast$}$$

is well-defined. If $$B$$ is path-connected and $$p(y_0)=p(y_1)$$, this becomes a homomorphism into the fundamental group $$\pi_1(B)$$. If $$E$$ is to carry all the information about the fundamental group (or groupoid) of $$B$$, then at minimum this homomorphism must be surjective.

<div class="definition" markdown="1">

<ins id="def5">**Definition 5**</ins> Fix a continuous map $$p:E\rightarrow B$$. For any continuous map $$f:X \rightarrow B$$, a *lifting* of $$f$$ along $$p$$ is a map $$\widetilde{f}:X\rightarrow E$$ satisfying $$p\circ\widetilde{f}=f$$.

</div>

The point of this definition is that when $$X=I$$, so that $$f$$ is a path in $$B$$, the existence of a lifting of $$f$$ along $$p$$ guarantees that it lies in the preimage of $$f$$ under ($$\ast$$). Our claim is that if $$p$$ is a covering map, such a lifting always exists.

<div class="proposition" markdown="1">

<ins id="lem6">**Lemma 6**</ins> Let $$p:E \rightarrow B$$ be a covering map and let $$y_0\in E$$. Then for every path $$\alpha:I \rightarrow B$$ starting at $$x_0=p(y_0)$$, there exists a unique lifting $$\widetilde{\alpha}:I \rightarrow E$$ starting at $$y_0$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Since $$p$$ is a covering map, we may choose an open cover $$(U_i)$$ of $$B$$ such that each $$U_i$$ is evenly covered by $$p$$. Then $$(\alpha^{-1}(U_i))$$ is an open cover of $$I$$, so it admits a finite subcover. By the [Lebesgue number lemma](Lebesgue_number_lemma), we can find a subdivision

$$0=s_0<s_1<\cdots<s_n=1$$

of $$I$$ such that each $$\alpha([s_i,s_{i+1}])$$ lies in some evenly covered open set $$U$$. Set $$\widetilde{\alpha}(0)=y_0$$, and assume inductively that $$\widetilde{\alpha}$$ has been defined on $$[0,s_i]$$. By the choice of the subdivision, $$\alpha([s_i,s_{i+1}])$$ lies in some open set $$U$$ evenly covered by $$p$$; thus $$p^{-1}(U)$$ is a disjoint union $$\coprod_{j\in J}V_j$$ of open sets, each mapped homeomorphically onto $$U$$ by $$p$$. Let $$V_j$$ be the component containing $$\widetilde{\alpha}(s_i)$$; then define

$$\widetilde{\alpha}(s)=(p\vert_{V_j})^{-1}(\alpha(s))$$

for $$s\in[s_i,s_{i+1}]$$. Uniqueness follows because each interval $$[s_i,s_{i+1}]$$ is connected, so the component containing $$\widetilde{\alpha}(s_i)$$ is determined inductively.

</details>

The proof may appear technical, but the core idea is simple: any path starting at $$x_0\in B$$ remains inside some evenly covered neighborhood $$U$$ of $$x_0$$ for at least a short time, and since $$p^{-1}(U)$$ is a disjoint union of open subsets of $$E$$ each homeomorphic to $$U$$, knowing which component contains the starting point determines, by connectedness, the component in which the path must lie during that short interval. The Lebesgue number lemma is used only to ensure that this process terminates after finitely many steps.

Returning to the groupoid homomorphism ($$\ast$$), [Lemma 6](#lem6) implies that for a covering space $$p:E \rightarrow B$$, given any $$x_0,x_1\in B$$ and a path $$\alpha$$ between them, a choice of $$y_0\in p^{-1}(x_0)$$ determines both $$y_1\in p^{-1}(x_1)$$ and a lift $$\widetilde{\alpha}\in \Hom_{\Pi_1(E)}(y_0,y_1)$$. The natural question is whether, for a path $$\alpha'$$ path-homotopic to $$\alpha$$, the same choice of $$y_0$$ yields the same endpoint $$y_1$$ and the same homotopy class. When $$p$$ is a covering map, the answer is affirmative.

<div class="proposition" markdown="1">

<ins id="lem7">**Lemma 7**</ins> Let $$p:E \rightarrow B$$ be a covering map and let $$y_0\in E$$, with $$p(y_0)=x_0$$. Then for every continuous map $$F:I\times I \rightarrow B$$ satisfying $$F(0,0)=x_0$$, there exists a unique lifting $$\widetilde{F}:I\times I \rightarrow E$$ with $$\widetilde{F}(0,0)=y_0$$. Moreover, if $$F$$ is a path homotopy, then so is $$\widetilde{F}$$.

</div>

The proof is essentially identical to that of [Lemma 6](#lem6), so we omit it. The crucial consequence is that, by this lemma, given a covering space $$p:E \rightarrow B$$ and a path class $$[\alpha]\in\Hom_{\Pi_1(B)}(x_0,x_1)$$, the choice of $$y_0\in p^{-1}(x_0)$$ uniquely determines the path class $$[\widetilde{\alpha}]\in \Hom_{\Pi_1(E)}(y_0,y_1)$$.

Now consider again the fundamental groupoid $$\Pi_1(B)$$ and fix a covering map $$p:E \rightarrow B$$. By the evenly covered condition, $$p^{-1}(x)$$ is a discrete set for each $$x\in B$$. Hence, for any path class $$[\alpha]\in\Hom_{\Pi_1(B)}(x_0,x_1)$$, choosing $$y_0\in p^{-1}(x_0)$$ yields, by [Lemma 7](#lem7), a unique path class $$[\widetilde{\alpha}]$$ and thus a unique endpoint $$y_1\in p^{-1}(x_1)$$. In other words, $$[\alpha]$$ defines a function $$p^{-1}(x_0)\rightarrow p^{-1}(x_1)$$.

<div class="definition" markdown="1">

<ins id="def8">**Definition 8**</ins> In the situation above, the function $$p^{-1}(x_0)\rightarrow p^{-1}(x_1)$$ is called the *transport map* and is denoted $$T_{[\alpha]}$$.

</div>

The transport map is bijective. Indeed, given any $$y_1\in p^{-1}(x_1)$$, we may use the path class $$[\overline{\alpha}]\in\Hom_{\Pi_1(B)}(x_1,x_0)$$ to find a path starting at $$y_1$$ and ending at some $$y_0\in p^{-1}(x_0)$$, and this procedure is unique by [Lemma 7](#lem7). Similarly, uniqueness of liftings implies that this correspondence respects concatenation of paths. Thus the assignment sending each object $$x\in \Pi_1(B)$$ to the set $$p^{-1}(x)$$ and each morphism $$[\alpha]\in\Hom_{\Pi_1(B)}(x_0,x_1)$$ to the transport map $$T_{[\alpha]}:p^{-1}(x_0)\rightarrow p^{-1}(x_1)$$ defines a functor.

<div class="definition" markdown="1">

<ins id="def9">**Definition 9**</ins> The functor $$\Pi_1(B) \rightarrow \Set$$ defined above is called the *monodromy functor* associated to $$p$$ and is denoted $$M_p$$.

</div>

For a fixed base space $$B$$, we define the category $$\Cov(B)$$ of covering spaces over $$B$$ in the evident manner. Explicitly, its objects are covering maps $$p:E\rightarrow B$$, and a morphism from $$p_1:E_1\rightarrow B$$ to $$p_2:E_2\rightarrow B$$ is a continuous map $$f:E_1\rightarrow E_2$$ making the diagram

![morphism_of_covering_spaces](/assets/images/Math/Algebraic_Topology/Covering_Spaces-2.png){:style="width:8em" class="invert" .align-center}

commute. Associating to each $$p\in \Cov(B)$$ its monodromy functor $$M_p$$ then defines a functor

$$M:\Cov(B) \rightarrow \Fun(\Pi_1(B),\Set)$$

and the central result of this post is that this functor is an equivalence of categories. To establish this, one must verify the functoriality of the above correspondence and much more; but the deepest part of the proof is the construction of a covering space $$E \rightarrow B$$ from an arbitrary functor $$\Pi_1(B)\rightarrow \Set$$. Given a functor $$F:\Pi_1(B) \rightarrow \Set$$, reversing the monodromy construction makes it clear how to define $$p:E\rightarrow B$$ *as a function of sets*: for each $$x\in B$$, the set $$F(x)$$ will serve as the fiber over $$x$$, so we set

$$p:E=\coprod_{x\in B}F(x) \rightarrow B$$

to be the projection. The difficulty lies in topologizing $$E$$ so that $$p$$ becomes a covering map. If such a topology exists, then each $$x\in B$$ must have an open neighborhood $$U$$ such that $$p^{-1}(U)$$ is homeomorphic to $$U\times F(x)$$. The familiar example $$\mathbb{R}\rightarrow S^1$$ makes this intuitive: $$p^{-1}(U)$$ is a disjoint union of copies of $$U$$, and an element of $$p^{-1}(U)$$ is determined by which copy it lies in ($$F(x)$$) and which point of that copy it is ($$U$$). We proceed in reverse by constructing, for suitable $$U$$, a bijection $$\phi:p^{-1}(U) \rightarrow U\times F(x)$$ and using it to define a topology on $$p^{-1}(U)$$. Verifying that these bijections agree on overlaps, endow $$E$$ with a well-defined topology, and satisfy the required properties is then routine; the heart of the proof lies in defining $$\phi$$.

From the form of $$p$$ above, we know that $$p^{-1}(U)$$ is the union of the sets $$F(x')$$ for $$x'\in U$$. The first coordinate of $$\phi(x')$$ should evidently be $$x'$$ itself, and the second coordinate, by the transport map, should be an element of $$F(x)$$ joined to $$x'$$ by a path. But for this information to be available in $$\Pi_1(B)$$, we require:

1. $$U$$ to be path-connected, so that a path class $$[\alpha]\in \Hom_{\Pi_1(B)}(x,x')$$ always exists, and
2. such a path class to be uniquely determined.

The first condition is simply that $$B$$ be locally path-connected. The second is more subtle: it suffices that two paths in $$U$$ with common endpoints define the same path class *in $$B$$*. This is a weaker condition than being locally simply connected.

<div class="definition" markdown="1">

<ins id="def10">**Definition 10**</ins> A topological space $$X$$ is *semi-locally simply connected* if every $$x\in X$$ has an open neighborhood $$U$$ such that every loop in $$U$$ is contractible in $$X$$.

</div>

Hence, for the preceding argument to hold, the space $$B$$ must satisfy, in addition to path-connectedness, the two conditions of being locally path-connected and semi-locally simply connected. Synthesizing the above discussion yields the following theorem.

<div class="proposition" markdown="1">

<ins id="thm11">**Theorem 11 (Fundamental theorem of covering spaces)**</ins> For a path-connected, locally path-connected, semi-locally simply connected space $$B$$, there is an equivalence of categories

$$M:\Cov(B) \rightarrow \Fun(\Pi_1(B), \Set)$$

</div>

For instance, every path-connected topological manifold satisfies these conditions.

It remains to understand what $$\Fun(\Pi_1(B), \Set)$$ is. More generally, consider a functor $$\mathscr{G}\rightarrow \Set$$ for an arbitrary groupoid $$\mathscr{G}$$. By definition, such a functor consists of:

- a set $$S_G$$ for each object $$G\in \mathscr{G}$$,
- a bijection $$S_G \rightarrow S_H$$ for each (iso)morphism $$G \rightarrow H$$ in $$\mathscr{G}$$.

This description alone does not fully illuminate the structure, so consider the special case where $$\mathscr{G}$$ has a single object $$\ast$$, so that every morphism of $$\mathscr{G}$$ is an automorphism of $$\ast$$—that is, $$\mathscr{G}$$ is a group. Under this assumption, a functor $$\mathscr{G}\rightarrow \Set$$ amounts to the following data:

- a set $$S$$ corresponding to the unique object of $$\mathscr{G}$$,
- a bijection $$g\cdot-: S\rightarrow S$$ for each automorphism $$g:\ast \rightarrow \ast$$.

Thus, as the notation suggests, this is precisely a group action of $$\mathscr{G}$$; the category $$\Fun(\mathscr{G},\Set)$$ is exactly the category of $$\mathscr{G}$$-sets, with morphisms the $$\mathscr{G}$$-equivariant maps. For a general groupoid $$\mathscr{G}$$, the picture is simply that of several groups acting separately on several sets, with the requirement that isomorphic objects $$G,H$$ of $$\mathscr{G}$$ act on their respective (isomorphic) sets $$S_G$$ and $$S_H$$ in the same manner.

Since $$B$$ is path-connected, the fundamental groupoid $$\Pi_1(B)$$ is a connected groupoid, and hence equivalent as a category to the group $$\pi_1(B,x)$$ for any $$x\in B$$. That is, a groupoid action of $$\Pi_1(B)$$ is nothing more than a group action of $$\pi_1(B,x)$$ propagated along the isomorphisms of $$\Pi_1(B)$$. Consequently, the information contained in [Theorem 11](#thm11) is essentially captured by a skeleton. Consider

$$\sk(M):\sk(\Cov(B))\rightarrow \sk(\Fun(\Pi_1(X), \Set))$$

This is an equivalence sending isomorphism classes of covering spaces to monodromy functors $$M_p$$ up to natural isomorphism—that is, to $$\Pi_1(X)$$-sets up to isomorphism. In general,

$$\sk(\Fun(\Pi_1(X),\Set))\simeq\Fun(\sk(\Pi_1(X)), \Set)$$

so, using again that $$X$$ is path-connected, we obtain a categorical equivalence between isomorphism classes of covering spaces and $$\pi_1(X,x)$$-sets.

Now recall [\[*Algebraic Structures* §Group Actions, ⁋Theorem 14*](/en/math/algebraic_structures/group_actions#thm14) and its proof: given any $$G$$-set $$E$$, we may decompose $$E$$ into $$G$$-orbits, and the restriction of the action to each orbit is transitive; moreover, each such orbit is isomorphic to $$G/N$$ for some normal subgroup $$N$$ of $$G$$, equipped with the canonical $$G$$-action. Hence, if we restrict attention to transitive group actions, the definition of the monodromy functor tells us that on the target side this corresponds to considering only *connected* covers. We thus obtain an equivalence

$$\left\{\text{isomorphism classes of covering spaces of $B$}\right\}\simeq \left\{\text{transitive $\pi_1(B,x)$-sets}\right\}$$

Passing to the skeleton category classifying transitive $$\pi_1(B,x)$$-sets up to isomorphism yields, finally, the equivalence

$$\left\{\text{isomorphism classes of covering spaces of $B$}\right\}\simeq \left\{\text{conjugacy classes of subgroups of $\pi_1(B,x)$}\right\}$$

Examining each of these categories, we find that they are simply partially ordered sets ([\[*Category Theory* §Categories, ⁋Example 3*](/en/math/category_theory/categories#ex3)), and the equivalence is an isomorphism of posets. This gives the following classical statement.

<div class="proposition" markdown="1">

<ins id="cor12">**Corollary 12 (Fundamental theorem of covering spaces, classical version)**</ins> For a path-connected, locally path-connected, semi-locally simply connected space $$B$$, there is a Galois correspondence between the set of isomorphism classes of connected covering spaces of $$B$$ and the set of conjugacy classes of subgroups of $$\pi_1(B)$$.

</div>

Explicitly, a covering space $$p:E \rightarrow B$$ determines a subgroup via $$\pi_1(p):\pi_1(E)\rightarrow \pi_1(B)$$, and two transitive $$G$$-sets $$X\cong G/H$$ and $$Y\cong G/K$$ are isomorphic if and only if $$H$$ and $$K$$ are conjugate, whence the result. On the other hand, if one wishes to work with specific subgroups of $$\pi_1(B,x)$$ rather than their conjugacy classes, this amounts to selecting a representative from each isomorphism class of covering spaces; equivalently, it is the same as fixing a basepoint in $$B$$ and considering *pointed* covering maps $$p:(E, y)\rightarrow (B,x)$, examining their isomorphism classes individually. Thus we have a Galois correspondence

$$\left\{\text{isomorphism classes of \textit{pointed} covering spaces of $B$}\right\}\simeq \left\{\text{subgroups of $\pi_1(B,x)$}\right\}$$

To put this in a more familiar form, for any $$H\leq \pi_1(B,x)$$ we may construct the corresponding covering space $$E_H$$, and the automorphism group $$\Aut(E_H/B)$$ of $$E_H$$ over $$B$$ satisfies

$$\Aut(E_H/B)\cong N_G(H)/H$$

This group is called the *Deck transformation group* of $$E_H$$. More generally, automorphisms of covering spaces (obtained by choosing different elements of the fiber $$p^{-1}(x)$$) correspond to inner automorphisms of subgroups of $$\pi_1(B,x)$$; we call these *Deck transformations*.

Now, the poset of conjugacy classes of subgroups of $$\pi_1(B,x)$$ possesses a minimal element $$\left\{e\right\}$$. By the Galois correspondence above, this corresponds to a *universal cover* $$\widetilde{B}$$. The Deck transformation group of this covering space is isomorphic to $$\pi_1(B,x)$$, and

## Seifert–van Kampen Theorem

For well-behaved spaces, one can in principle compute the fundamental group or homology directly from the definitions, but in most cases such a computation is prohibitively complicated or essentially impossible. Our strategy is to compute the fundamental group of a large space by decomposing it into smaller pieces.

The simplest such decomposition is a union of two open sets: $$X=U\cup V$$. By [\[*Topology* §Presheaves, ⁋Lemma 1*](/en/math/topology/presheaves#lem1), the diagram

![union_as_colimit](/assets/images/Math/Algebraic_Topology/Covering_Spaces-3.png){:style="width:8em" class="invert" .align-center}

is a colimit diagram. Our goal is to apply the fundamental groupoid functor $$\Pi_1$$ to this diagram and express $$\Pi_1(X)$$ in terms of $$\Pi_1(U)$$, $$\Pi_1(V)$$, and $$\Pi_1(U\cap V)$$. More generally, [\[*Topology* §Presheaves, ⁋Lemma 1*](/en/math/topology/presheaves#lem1) implies that for any open cover $$(U_i)$$, the diagram

![general_union_colimit](/assets/images/Math/Algebraic_Topology/Covering_Spaces-4.png){:style="width:8em" class="invert" .align-center}

is a colimit diagram. Our claim is that if the fundamental groupoids of the $$U_i$$ and of all their finite intersections are known, then the fundamental groupoid of $$\Pi_1(X)$$ can be computed from them.

<div class="proposition" markdown="1">

<ins id="thm13">**Theorem 13 (Seifert–van Kampen)**</ins> Let $$X$$ be a topological space with a path-connected open cover $$\mathcal{O}=(U_i)$$, and assume that every finite intersection of members of $$\mathcal{O}$$ belongs to $$\mathcal{O}$$. Then the colimit of the $$\mathcal{O}$$-shaped diagram $$\Pi_1:\mathcal{O}\rightarrow\Grpd$$ exists and is isomorphic to $$\Pi_1(X)$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

We must show that for any groupoid $$\mathscr{G}\in\Grpd$$ and any cocone $$\lambda:\Pi_1\vert_\mathcal{O}\Rightarrow \mathscr{G}$$, there exists a unique morphism $$\widetilde{\lambda}:\Pi_1(X)\rightarrow\mathscr{G}$$ such that $$\widetilde{\lambda}\vert_U=\lambda_U$$ for each $$U\in \mathcal{O}$$. Naturally, for each $$x\in X$$ we choose some $$U\in\mathcal{O}$$ containing $$x$$ and define $$\widetilde{\lambda}(x)=\lambda_U(x)$$. That this is independent of the choice of $$U$$ follows from the fact that for any $$U_1,U_2\in\mathcal{O}$$ containing $$x$$, the values $$\lambda_{U_1}(x)$$ and $$\lambda_{U_2}(x)$$ must both agree with $$\lambda_{U_1\cap U_2}(x)$$. Morphisms are treated similarly: for a path $$f$$ entirely contained in some $$U\in\mathcal{O}$$, the definition is well-defined for the same reason, and the only remaining issue is how to define $$\widetilde{\lambda}$$ on a path that is not contained in a single member of $$\mathcal{O}$$. In this case, one simply subdivides the path and takes the concatenation of the images of the pieces. That this is always defined and well-defined is straightforward to verify.

</details>

As in the derivation of [Corollary 12](#cor12), we now apply this theorem at a single basepoint, thereby replacing $$\Grpd$$ with $$\Grp$$, and use the fact that colimits in $$\Grp$$ are amalgamated free products. This yields the classical statement.

<div class="proposition" markdown="1">

<ins id="cor14">**Corollary 14 (Seifert–van Kampen theorem, classical version)**</ins> Let a topological space $$X$$ be expressed as the union of two connected open subsets $$U,V$$, and suppose $$U\cap V$$ is connected. Then the diagram

![van_Kampen](/assets/images/Math/Algebraic_Topology/Covering_Spaces-5.png){:style="width:20em" class="invert" .align-center}

is a pushout diagram, and the induced map $$\pi_1(U)\ast_{\pi_1(U\cap V)}\pi_1(V)\rightarrow \pi_1(X)$$ is an isomorphism.

</div>

## Hurewicz Theorem

Homology groups are structurally simpler than the fundamental group. For example, $$\pi_1(X)$$ need not be abelian in general, whereas $$H_1(X)$$ is abelian by definition. Nevertheless, as observed in [§Homology, ⁋Example 8](/en/math/algebraic_topology/homology#ex8), elements of $$H_1(X)$$ may be regarded as a kind of loop, so a relationship between the two is to be expected.

<div class="proposition" markdown="1">

<ins id="thm15">**Theorem 15 (Hurewicz)**</ins> Let $$X$$ be a path-connected space. Then for each $$n$$, there is a group homomorphism

$$h_n:\pi_n(X) \rightarrow H_n(X)$$

In particular, for $$n=1$$, the map $$h_1$$ is surjective and its kernel is the commutator subgroup $$[\pi_1(X),\pi_1(X)]$$; hence by the first isomorphism theorem,

$$H_1(X)\cong \pi_1(X)/\ker h_1=\pi_1(X)/[\pi_1(X),\pi_1(X)]=\pi_1(X)^\ab$$

More generally, if $$\pi_i(X)=0$$ for all $$i< n$$, then $$h_n$$ is an isomorphism and $$h_{n+1}$$ is surjective.

</div>

The Hurewicz homomorphism $$h_n$$ is given by $$f_\ast([S^n])$$ for any $$f:S^n \rightarrow X$$. Here $$[S^n]$$ denotes a generator of $$H_n(S^n)\cong \mathbb{Z}$$.



--- 

**References**

[Hat] A. Hatcher, *Algebraic Topology*. Cambridge University Press, 2022.  
[May] J. P. May, *A concise course in algebraic topology*.  
[Mun] James Munkres, *Topology*. Prentice Hall, 2000.  
[Tao] Terence Tao, [van Kampen's theorem via covering spaces](https://terrytao.wordpress.com/2012/10/28/van-kampens-theorem-via-covering-spaces/).

---
