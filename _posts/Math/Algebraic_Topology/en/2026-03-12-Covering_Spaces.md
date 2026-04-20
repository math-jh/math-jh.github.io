---

title: "Covering Spaces"
excerpt: ""

categories: [Math / Algebraic Topology]
permalink: /en/math/algebraic_topology/covering_spaces
header:
    overlay_image: /assets/images/Math/Algebraic_Topology/Covering_spaces.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_topology-en"

date: 2026-03-12
last_modified_at: 2026-03-12
weight: 4

---

In the previous post, we defined the fundamental group $$\pi_1(X)$$ and explored its basic properties. Then the following lemma is almost trivial from the definitions.

<div class="proposition" markdown="1">

<ins id="lem1">**Lemma 1**</ins> For a path-connected space $$X$$, the following are all equivalent.

1. Any two paths $$p,q$$ sharing endpoints are always path homotopic.
2. Any loop $$f:S^1 \rightarrow X$$ is always null-homotopic.
3. For any loop $$f:S^1 \rightarrow X$$, there exists a continuous map $$\widetilde{f}:D^2 \rightarrow X$$ such that the restriction of $$\widetilde{f}$$ to its boundary $$S^1$$ is $$f$$.
4. $$\pi_1(X)=0$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

That the first condition, second condition, and last condition are equivalent is trivial by considering the loop $$p\ast\bar{q}$$ for two paths $$p,q$$. Therefore, it suffices to show that the third condition is equivalent to these.

First, assuming the first condition, for any loop $$f:S^1 \rightarrow X$$, there exists a homotopy $$(f_t)$$ such that $$f_1=f$$ and $$f_0$$ is a constant map to a fixed point $$x_0$$. Then the formula

$$\widetilde{f}(\mathrm{x})=\begin{cases}f_{\lvert\mathrm{x}\rvert}(\mathrm{x}/\lvert\mathrm{x}\rvert)&\text{if $\lvert\mathrm{x}\rvert\neq 0$}\\ x_0&\text{if $\lvert\mathrm{x}\rvert=0$}\end{cases}$$

gives the continuous function required by the third condition. Conversely, assuming the third condition, given any loop $$f$$, setting $$f_t(\mathrm{x})=\widetilde{f}(t\mathrm{x})$$ gives a homotopy from $$f_1=f$$ to a constant map.

</details>

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> If the equivalent conditions of [Lemma 1](#lem1) hold, we call a path-connected $$X$$ a *simply connected space*.

</div>

## Covering Spaces

In what follows, we will only consider path-connected spaces for convenience. To compute the fundamental group of spaces that are not simply connected, several methods are needed, and one of the most fundamental and essential methods is to use covering spaces.

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> For a continuous surjection $$p:E \rightarrow B$$, an open set $$U$$ of $$B$$ is said to be *evenly covered* by $$p$$ if $$p^{-1}(U)$$ can be written as a union of disjoint open sets of $$E$$, each homeomorphic to $$U$$. If for every $$x\in B$$ there exists an open neighborhood $$U$$ that is evenly covered by $$p$$, then $$p$$ is called a *covering map* and $$E$$ is called a *covering space*.

</div>

The definition may seem somewhat complex, but essentially it is convenient to keep the following picture in mind.

![S1_covering](/assets/images/Math/Algebraic_Topology/Covering_spaces-1.png){:style="width:26em" class="invert" .align-center}

This represents the covering map

$$p:\mathbb{R}\rightarrow S^1;\quad t\mapsto (\cos 2\pi t, \sin 2\pi t)$$

and we know that it satisfies the conditions of [Definition 2](#def2). On the other hand, in general, it is easy to prove that covering maps behave well with respect to subspaces and product spaces.

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4**</ins> The following hold.

1. For a covering map $$p:E \rightarrow B$$ and a subspace $$A$$ of $$B$$, $$p\vert_{p^{-1}(A)}:p^{-1}(A) \rightarrow A$$ is a covering map.
2. For two covering maps $$p_1:E_1 \rightarrow B_1$$, $$p_2:E_2\rightarrow B_2$$, $$p_1\times p_2:E_1\times E_2 \rightarrow B_1\times B_2$$ is a covering map.

</div>

## Fundamental Theorem of Covering Spaces

Using the functoriality of the fundamental groupoid $$\Pi_1:\Top \rightarrow \Grpd$$, any continuous function $$p:E \rightarrow B$$ defines the following groupoid homomorphism

$$\Pi_1(f):\Pi_1(E) \rightarrow \Pi_1(B)$$

In particular, for any $$y_0, y_1\in E$$, the following homomorphism

$$\Hom_{\Pi_1(E))}(y_0, y_1)\rightarrow \Hom_{\Pi_1(B)}(p(y_0), p(y_1))\tag{$\ast$}$$

is well-defined. If $$B$$ is path-connected and $$p(y_0)=p(y_1)$$, this becomes a (groupoid) homomorphism to the fundamental group $$\pi_1(B)$$. If $$E$$ contains all the information about the fundamental group (or groupoid) of $$B$$, then at least this homomorphism should be surjective.

<div class="definition" markdown="1">

<ins id="def5">**Definition 5**</ins> Fix a continuous map $$p:E\rightarrow B$$. Then for any continuous map $$f:X \rightarrow B$$, a *lifting* of $$f$$ with respect to $$p$$ is a map $$\widetilde{f}:X\rightarrow E$$ satisfying the equation $$p\circ\widetilde{f}=f$$.

</div>

The reason for considering such a definition is naturally that when $$X=I$$ and thus $$f$$ is a path into $$B$$, if a lifting of $$f$$ with respect to $$p$$ exists, then it belongs to the preimage of $$f$$ under the homomorphism ($$\ast$$). Our claim is then that if $$p$$ is a covering space, such a lifting always exists.

<div class="proposition" markdown="1">

<ins id="lem6">**Lemma 6**</ins> Consider a covering map $$p:E \rightarrow B$$ and any point $$y_0$$ of $$E$$. Then whenever a path $$\alpha:I \rightarrow B$$ starting at $$x_0=p(y_0)$$ is given, there exists a unique lifting $$\widetilde{\alpha}:I \rightarrow E$$ starting at $$y_0$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, from the assumption that $$p$$ is a covering space, we can take an open covering $$(U_i)$$ of $$B$$ such that each $$U_i$$ is evenly covered by $$p$$. Now $$(\alpha^{-1}(U_i))$$ is an open covering of $$I$$, so there exists a finite subcover covering $$I$$. Using [##ref##](Lebesgue_number_lemma), we can find a subdivision of $$I$$

$$0=s_0<s_1<\cdots<s_n=1$$

such that $$\alpha([s_i,s_{i+1}])$$ lies inside some $$U$$. Now define $$\widetilde{\alpha}(0)=y_0$$, and to define $$\widetilde{\alpha}$$ inductively, assume $$\widetilde{\alpha}$$ is defined for $$0\leq s\leq s_i$$ and define $$\widetilde{\alpha}$$ on $$[s_i,s_{i+1}]$$. First, by the choice of $$s_i$$, $$\alpha([s_i,s_{i+1}])$$ lies in an open set $$U$$ that is evenly covered by $$p$$. Therefore, we can write $$p^{-1}(U)$$ as a disjoint union $$\coprod_{j\in J}V_j$$ of open sets each homeomorphic to $$U$$. Now for the $$V_j$$ such that $$\widetilde{\alpha}(s_i)\in V_j$$, we can define $$\widetilde{\alpha}$$ by the formula

$$\widetilde{\alpha}(s)=(p\vert_{V_j})^{-1}(\alpha(s))$$

For uniqueness, since $$[s_i,s_{i+1}]$$ is connected and the component containing $$\alpha(s_i)$$ is determined inductively, it is trivial.

</details>

The proof may appear somewhat technical, but the key idea is that any path starting at $$x_0\in B$$ will lie inside an open neighborhood $$U$$ of $$x_0$$ that is evenly covered by $$p$$ at least for a short time, and by definition, $$p^{-1}(U)$$ is a union of disjoint open subsets of $$E$$ each homeomorphic to $$U$$, so once we know which component the starting point belongs to, the component where the path stays during this short time is determined (by connectedness). The Lebesgue number lemma is only used to show that this process is finite.

Let us return to the groupoid homomorphism ($$\ast$$). By [Lemma 6](#lem6), for a covering space $$p:E \rightarrow B$$, given any $$x_0,x_1\in B$$ and a path $$\alpha$$ with these as endpoints, the choice of $$y_0\in p^{-1}(x_0)$$ determines $$y_1\in p^{-1}(x_1)$$ and $$\widetilde{\alpha}\in \Hom_{\Pi_1(E)}(y_0,y_1)$$. A natural question then is whether for $$\alpha'$$ that is path-homotopic to $$\alpha$$, the same choice of $$y_0$$ gives the same $$y_1$$ and homotopy type. If $$p$$ is a covering space, the answer to this is also affirmative.

<div class="proposition" markdown="1">

<ins id="lem7">**Lemma 7**</ins> Consider a covering map $$p:E \rightarrow B$$ and any point $$y_0$$ of $$E$$, and let $$p(y_0)=x_0$$. Then whenever a continuous function $$F:I\times I \rightarrow B$$ satisfying $$F(0,0)=x_0$$ is given, there exists a unique lifting $$\widetilde{F}:I\times I \rightarrow E$$ satisfying $$\widetilde{F}(0,0)=y_0$$. Moreover, if $$F$$ is a path homotopy, then $$\widetilde{F}$$ is also a path homotopy.  

</div>

The proof of this is essentially no different from [Lemma 6](#lem6), so we omit it. What is important is that by the path homotopy given by this lemma, given a covering space $$p:E \rightarrow B$$ and a path class $$[\alpha]\in\Hom_{\Pi_1(B)}(x_0,x_1)$$, the choice of $$y_0\in p^{-1}(x_0)$$ uniquely determines the path class $$[\widetilde{\alpha}]\in \Hom_{\Pi_1(E)}(y_0,y_1)$$.

Now let us consider the fundamental groupoid $$\Pi_1(B)$$ again and fix a covering map $$p:E \rightarrow B$$. Then by the evenly covered condition, for each $$x\in B$$, $$p^{-1}(x)$$ is a discrete set. In this case, for any path class $$[\alpha]\in\Hom_{\Pi_1(B)}(x_0,x_1)$$, if we choose $$y_0\in p^{-1}(x_0)$$, then [Lemma 7](#lem7) defines a unique path class $$[\widetilde{\alpha}]$$, and thus defines $$y_1\in p^{-1}(x)$$. That is, $$[\alpha]$$ defines a function $$p^{-1}(x_0)\rightarrow p^{-1}(x_1)$$.

<div class="definition" markdown="1">

<ins id="def8">**Definition 8**</ins> In the above situation, the function $$p^{-1}(x_0)\rightarrow p^{-1}(x_1)$$ is called the *transport map* and is denoted by $$T_{[\alpha]}$$.

</div>

The transport map is bijective. This is because, first, if any $$y_1\in p^{-1}(x_1)$$ is given, we can use the path class $$[\overline{\alpha}]\in\Hom_{\Pi_1(B)}(x_1,x_0)$$ to find a path starting at $$y_1$$ and ending at some element $$y_0$$ of $$p^{-1}(x_0)$$, and this process is unique by [Lemma 7](#lem7). Similarly, by the uniqueness of liftings, we know that this correspondence preserves concatenation of paths well. That is, the correspondence sending $$x\in \Pi_1(B)$$ to $$p^{-1}(x)$$ and $$[\alpha]\in\Hom_{\Pi_1(B)}(x_0,x_1)$$ to $$T_{[\alpha]}:p^{-1}(x_0)\rightarrow p^{-1}(x_1)$$ is functorial.

<div class="definition" markdown="1">

<ins id="def9">**Definition 9**</ins> The functor $$\Pi_1(B) \rightarrow \Set$$ defined above is called the *monodromy functor* defined by $$p$$ and is denoted by $$M_p$$.

</div>

For a fixed base space $$B$$, we define the category $$\Cov(B)$$ of covering spaces of $$B$$ in a trivial manner. Explicitly, the objects of this category are covering maps $$p:E\rightarrow B$$, and morphisms between them are the following commutative diagram 

![morphism_of_covering_spaces](/assets/images/Math/Algebraic_Topology/Covering_spaces-2.png){:style="width:8em" class="invert" .align-center}

Through this, we see that associating each $$p\in \Cov(B)$$ with the monodromy functor $$M_p$$ defines a functor

$$M:\Cov(B) \rightarrow \Fun(\Pi_1(B),\Set)$$

and the main result of this post is that this is an equivalence between the two categories. To show this, starting from the functoriality of the above correspondence, there is much to prove, but ultimately the most essential content is constructing a covering space $$E \rightarrow B$$ from any given functor $$\Pi_1(B)\rightarrow \Set$$. To do this, suppose any functor $$F:\Pi_1(B) \rightarrow \Set$$ is given. Following the monodromy functor backward, it is obvious how to construct $$p:E\rightarrow B$$ *as a function between sets*. For each $$x\in \Pi_1(B)$$, $$F(x)$$ will correspond to the fiber of $$p$$ at $$x$$, so we can take the projection

$$p:E=\coprod_{x\in B}F(x) \rightarrow B$$

The problem is to give a topology on $$E$$ that makes this a covering space. If such a topology exists, there should be an open neighborhood $$U$$ of $$x$$ such that a homeomorphism exists between $$p^{-1}(U)$$ and $$U\times F(x)$$. Thinking of the familiar $$\mathbb{R}\rightarrow S^1$$, this is intuitively obvious: $$p^{-1}(U)$$ is a disjoint union of sets homeomorphic to $$U$$, and thus any element of $$p^{-1}(U)$$ is determined by which of these sets it belongs to ($$F(x)$$) and which point in that set it is ($$U$$). We will conversely construct a bijection $$\phi:p^{-1}(U) \rightarrow U\times F(x)$$ and use it to define a topology on $$p^{-1}(U)$$. Then where these $$\phi$$ overlap, they define the same function, so showing that these bijections give an appropriate topology on $$E$$ and that it satisfies our desired properties is simple labor, and the core of the proof is defining $$\phi$$.

By the form of $$p$$ defined above, we know that $$p^{-1}(U)$$ is the collection of $$F(x')$$ for $$x'$$ satisfying $$x'\in U$$. Then the first coordinate of $$\phi(x')$$ should naturally be $$x'$$ itself, and the second coordinate, considering the transport map, should be an element of $$F(x)$$ connected to $$x'$$ by a path. But for this, this information must be contained in $$\Pi_1(B)$$, so we need:

1. $$U$$ to be path-connected so that a path class $$[\alpha]\in \Hom_{\Pi_1(B)}(x,x')$$ connecting $$x$$ and $$x'$$ always exists, and
2. Such a path class to be uniquely determined.

The first condition is simply that $$B$$ is locally path-connected. The second condition is a bit more subtle: it suffices if two paths sharing endpoints *in $$B$$* define the same path class. This is a weaker condition than locally simply connected.

<div class="definition" markdown="1">

<ins id="def10">**Definition 10**</ins> A topological space $$X$$ is *semi-locally simply connected* if for every $$x\in X$$, there exists an open neighborhood $$U$$ such that any loop in $$U$$ is contractible in $$X$$.

</div>

Thus for the above argument to hold, we see that in addition to the path-connected condition previously assumed, the space $$B$$ must satisfy two conditions: locally path-connected and semi-locally simply connected. Now summarizing the above discussion, we obtain the following result.

<div class="proposition" markdown="1">

<ins id="thm11">**Theorem 11 (Fundamental theorem of covering spaces)**</ins> For a path-connected, locally path-connected, semi-locally simply connected space $$B$$, there exists an equivalence between the two categories

$$M:\Cov(B) \rightarrow \Fun(\Pi_1(B), \Set)$$

</div>

For example, any path-connected topological manifold always satisfies the above conditions.

Now we need to examine what $$\Fun(\Pi_1(B), \Set)$$ is. More generally, let us consider what a functor $$\mathscr{G}\rightarrow \Set$$ is for any groupoid $$\mathscr{G}$$. By definition, this consists of

- A set $$S_G$$ corresponding to each object $$G\in \mathscr{G}$$,
- A bijection $$S_G \rightarrow S_H$$ corresponding to each (iso)morphism $$G \rightarrow H$$ of $$\mathscr{G}$$.

This alone still does not show what a functor $$\mathscr{G}\rightarrow \Set$$ is, so let us consider the special case where $$\mathscr{G}$$ has only one object $$\ast$$ and thus all morphisms of $$\mathscr{G}$$ become automorphisms of $$\ast$$. That is, $$\mathscr{G}$$ is a group. Then under this assumption, a functor $$\mathscr{G}\rightarrow \Set$$ is the following data:

- A set $$S$$ corresponding to the unique object of $$\mathscr{G}$$,
- A bijection $$g\cdot-: S\rightarrow S$$ corresponding to each automorphism $$g:\ast \rightarrow \ast$$.

That is, as one might guess from the notation, this information is exactly an action of the group $$\mathscr{G}$$, and $$\Fun(\mathscr{G},\Set)$$ is exactly the collection of $$\mathscr{G}$$-sets and morphisms between them are $$\mathscr{G}$$-equivariant maps. For a general groupoid $$\mathscr{G}$$, it is just that several groups act on several sets separately, but isomorphic objects $$G,H$$ of $$\mathscr{G}$$ must act on their respective (isomorphic) sets $$S_G$$ and $$S_H$$ in the same way.

But since the space $$B$$ is path-connected, the fundamental groupoid $$\Pi_1(B)$$ is a connected groupoid, and thus $$\Pi_1(B)$$ is equivalent as a category to the group $$\pi_1(B,x)$$ for any $$x\in B$$. That is, the groupoid action of $$\Pi_1(B)$$ is nothing more than copying the group action of the group $$\pi_1(B,x)$$ along isomorphisms in the groupoid $$\Pi_1(B)$$. Therefore, the information contained in [Theorem 11](#thm11) above is essentially contained in a skeleton. Thus consider

$$\sk(M):\sk(\Cov(B))\rightarrow \sk(\Fun(\Pi_1(X), \Set))$$

This is an equivalence that takes isomorphism classes of covering spaces and produces the monodromy functor $$M_p$$ up to natural isomorphism. That is, $$\Pi_1(X)$$-sets up to isomorphism. In general,

$$\sk(\Fun(\Pi_1(X),\Set))\simeq\Fun(\sk(\Pi_1(X)), \Set)$$

so, using again that $$X$$ is path-connected, we see that there exists a categorical equivalence that takes isomorphism classes of covering spaces and produces a $$\pi_1(X,x)$$-set.

But considering [\[Algebraic Structures\] §Group Actions, ⁋Theorem 14](/en/math/algebraic_structures/group_actions#thm14) and its proof, given any $$G$$-set $$E$$, we can decompose $$E$$ into orbits of $$G$$, and then when restricted to each of these orbits, the $$G$$-action is transitive and they are isomorphic to $$G/N$$ for some normal subgroup $$N$$ of $$G$$ with the canonical $$G$$-action. Therefore, if we only consider transitive group actions, by the definition of the monodromy functor, this corresponds to considering only *connected* covers on the target side. Thus the following equivalence

$$\left\{\text{isomorphism classes of covering spaces of $B$}\right\}\simeq \left\{\text{transitive $\pi_1(B,x)$-sets}\right\}$$

exists, and again considering the skeleton category classifying transitive $$\pi_1(B,x)$$-sets up to isomorphism, we finally obtain the following equivalence

$$\left\{\text{isomorphism classes of covering spaces of $B$}\right\}\simeq \left\{\text{conjugacy classes of subgroups of $\pi_1(B,x)$}\right\}$$

Now examining each of these categories, they are just partially ordered sets ([\[Category Theory\] §Categories, ⁋Example 3](/en/math/category_theory/categories#ex3)) and this equivalence is an isomorphism between posets. Thus we obtain the following result.

<div class="proposition" markdown="1">

<ins id="cor12">**Corollary 12 (Fundamental theorem of covering spaces, classical version)**</ins> For a path-connected, locally path-connected, semi-locally simply connected space $$B$$, there exists a Galois correspondence between the set of isomorphism classes of connected covering spaces and the conjugacy classes of subgroups of $$\pi_1(B)$$.

</div>

Explicitly, given a covering space $$p:E \rightarrow B$$, a subgroup is defined through $$\pi_1(p):\pi_1(E)\rightarrow \pi_1(B)$$, and since two transitive $$G$$-sets $$X\cong G/H$$ and $$Y\cong G/K$$ are isomorphic if and only if $$H$$ and $$K$$ are conjugate to each other, we obtain the above result. On the other hand, if instead of conjugacy classes of subgroups of $$\pi_1(B,x)$$ we consider explicit subgroups themselves, this amounts to choosing one among isomorphic covering spaces, which is exactly fixing a base point of $$B$$ and then considering *pointed* covering maps $$p:(E, y)\rightarrow (B,x)$$ and examining each element of these isomorphism classes separately. That is, the following Galois correspondence

$$\left\{\text{isomorphism classes of \textit{pointed} covering spaces of $B$}\right\}\simeq \left\{\text{subgroups of $\pi_1(B,x)$}\right\}$$

exists. To express this in a more familiar form, for any $$H\leq \pi_1(B,x)$$, we can construct the corresponding covering space $$E_H$$, and then for the automorphism group $$\Aut(E_H/B)$$ of $$E_H$$,

$$\Aut(E_H/B)\cong N_G(H)/H$$

holds. This is called the *Deck transformation group* of $$E_H$$. More generally, automorphisms of covering spaces (obtained by choosing different elements of the fiber $$p^{-1}(x)$$) correspond to taking inner automorphisms of subgroups of $$\pi_1(B,x)$$, and we call this a *Deck transformation*.

On the other hand, the poset of conjugacy classes of subgroups of $$\pi_1(B,x)$$ has a minimal element $$\left\{e\right\}$$. Then by the above Galois correspondence, there exists a corresponding *universal cover* $$\widetilde{B}$$. The Deck transformation group of this covering space is isomorphic to $$\pi_1(B,x)$$, and

## Seifert-van Kampen Theorem

While we can compute the fundamental group or homology from the definition for nice spaces that we know, in most cases computing them from the definition is excessively complicated or nearly impossible. Our idea is to compute the fundamental group of a large space by representing it in terms of smaller spaces.

The simplest of such methods is the case where a space $$X$$ can be expressed as a union of two open sets $$X=U\cup V$$. Then by [\[Topology\] §Presheaves, ⁋Lemma 1](/en/math/topology/presheaves#lem1), we know that the following diagram 

![union_as_colimit](/assets/images/Math/Algebraic_Topology/Covering_spaces-3.png){:style="width:8em" class="invert" .align-center}

is a colimit diagram. In this case, our goal is to apply the fundamental groupoid functor $$\Pi_1$$ to this diagram and represent $$\Pi_1(X)$$ in terms of $$\Pi_1(U)$$, $$\Pi_1(V)$$, and $$\Pi_1(U\cap V)$$. On the other hand, [\[Topology\] §Presheaves, ⁋Lemma 1](/en/math/topology/presheaves#lem1) tells us that for any open covering $$(U_i)$$, the following diagram 

![general_union_colimit](/assets/images/Math/Algebraic_Topology/Covering_spaces-4.png){:style="width:8em" class="invert" .align-center}

is a colimit diagram. Our claim is that if the fundamental groupoids of $$(U_i)$$ and their finite intersections are all known, we can compute the fundamental groupoid of $$\Pi_1(X)$$ from them.

<div class="proposition" markdown="1">

<ins id="thm13">**Theorem 13 (Seifert-van Kampen)**</ins> Let a path-connected open cover $$\mathcal{O}=(U_i)$$ of a topological space $$X$$ be given, and assume that finite intersections of elements of $$\mathcal{O}$$ belong to $$\mathcal{O}$$. Then the colimit of the $$\mathcal{O}$$-shaped diagram $$\Pi_1:\mathcal{O}\rightarrow\Grpd$$ exists and is isomorphic to $$\Pi_1(X)$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

That is, we need to show that for any groupoid $$\mathscr{G}\in\Grpd$$ and any cocone $$\lambda:\Pi_1\vert_\mathcal{O}\Rightarrow \mathscr{G}$$, there exists $$\widetilde{\lambda}$$ such that for each $$U\in \mathcal{O}$$, $$\widetilde{\lambda}$$ equals $$\lambda$$. Naturally, for each $$x\in X$$, we find a $$U$$ satisfying $$x\in U$$, and since $$\lambda_U$$ is defined on it, we can define $$\widetilde{\lambda}(x)$$ as this value $$\lambda_U(x)$$. That this is independent of the choice of $$U$$ follows trivially from the fact that for any $$U_1,U_2$$ containing $$x$$, both $$\lambda_{U_1}(x)$$ and $$\lambda_{U_2}(x)$$ must equal $$\lambda_{U_1\cap U_2}(x)$$. Similarly, we can define morphisms in a similar way; for a path $$f$$ that is completely contained in some $$U\in \mathcal{O}$$, this definition is well-defined for the same reason as above, and what remains to be shown uniquely is how to define it when a path does not belong to a single $$U\in \mathcal{O}$$. But in this case, we can just consider the concatenation of paths. We need to show that this is always defined and well-defined.

</details>

Now, just as when we obtained [Corollary 12](#cor12) above, if we apply this theorem only at a single object, and thus replace $$\Grpd$$ with $$\Grp$$ and use that the colimit in $$\Grp$$ is the free product, we obtain the following result.

<div class="proposition" markdown="1">

<ins id="cor14">**Corollary 14 (Seifert-van Kampen theorem, classical version)**</ins> Suppose a topological space $$X$$ is expressed as a union of two connected open subsets $$U,V$$, and let $$U\cap V$$ be connected. Then the following diagram

![van_Kampen](/assets/images/Math/Algebraic_Topology/Covering_spaces-5.png){:style="width:20em" class="invert" .align-center}

is a pushout diagram and the resulting $$\pi_1(U)\ast_{\pi_1(U\cap V)}\pi_1(V)\rightarrow \pi_1(X)$$ is an isomorphism.

</div>

## Hurewicz Theorem

Homology groups have a simpler structure than the fundamental group. For example, $$\pi_1(X)$$ does not need to be an abelian group in general, but $$H_1(X)$$ is an abelian group by definition. However, as we saw in [§Homology, ⁋Example 8](/en/math/algebraic_topology/homology#ex8), elements of $$H_1(X)$$ can also be thought of as a kind of loops, so it is natural to expect a relationship between them.

<div class="proposition" markdown="1">

<ins id="thm15">**Theorem 15 (Hurewicz)**</ins> Fix a path-connected space $$X$$. Then for each $$n$$, there exists a group homomorphism  

$$h_n:\pi_n(X) \rightarrow H_n(X)$$

In particular, for $$n=1$$, $$h_1$$ is surjective and $$\ker h_1$$ becomes the commutator subgroup $$[\pi_1(X),\pi_1(X)]$$ of $$\pi_1(X)$$, so by the first isomorphism theorem,

$$H_1(X)\cong \pi_1(X)/\ker h_1=\pi_1(X)/[\pi_1(X),\pi_1(X)]=\pi_1(X)^\ab$$

holds. More generally, if $$\pi_i(X)=0$$ for all $$i< n$$, then $$h_n$$ is an isomorphism and $$h_{n+1}$$ is surjective.

</div>

The Hurewicz homomorphism $$h_n$$ is given by $$f_\ast([S^n])$$ when any $$f:S^n \rightarrow X$$ is given. Here $$[S^n]$$ is a generator of $$H_n(S^n)\cong \mathbb{Z}$$.



--- 

**References**

[Hat] A. Hatcher, *Algebraic Topology*. Cambridge University Press, 2022.  
[May] J. P. May, *A concise course in algebraic topology*.  
[Mun] James Munkres, *Topology*. Prentice Hall, 2000.  
[Tao] Terence Tao, [van Kampen's theorem via covering spaces](https://terrytao.wordpress.com/2012/10/28/van-kampens-theorem-via-covering-spaces/).

---
