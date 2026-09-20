---
title: "Covering Spaces"
description: "This post defines simply connected spaces and the notions of covering spaces and covering maps. It introduces basic methods for computing fundamental groups through the property of being evenly covered."
excerpt: "Equivalent conditions for simply connected spaces, covering spaces, and Seifert-van Kampen theorem"

categories: [Math / Algebraic Topology]
permalink: /en/math/algebraic_topology/covering_spaces
sidebar: 
    nav: "algebraic_topology-en"

date: 2025-07-27
weight: 4
translated_at: 2026-08-18T13:45:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-09-20T07:15:04+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
In the previous post, we defined the fundamental group $\pi_1(X)$ and examined some of its basic properties. The following lemma is then almost immediate from the definitions.

::: Lemma 1
For a path-connected space $X$, the following are equivalent.

1. Any two paths $p,q$ with common endpoints are always path homotopic.
2. Every loop $f:S^1 \rightarrow X$ is always null-homotopic.
3. For every loop $f:S^1 \rightarrow X$, there exists a continuous map $\widetilde{f}:D^2 \rightarrow X$ such that the restriction of $\widetilde{f}$ to the boundary $S^1$ of its domain is $f$.
4. $\pi_1(X)=0$.
:::
::: Proof
That the first, second, and last conditions are equivalent is clear by considering, for two paths $p,q$, the loop $p\ast\bar{q}$. Thus it suffices to show that the third condition is equivalent to these.

First, assuming the first condition, for any loop $f:S^1 \rightarrow X$ there exists a homotopy $(f_t)$ such that $f_1=f$ and $f_0$ is the constant map to a fixed point $x_0$. Then one sees that the formula

$$\widetilde{f}(\mathrm{x})=\begin{cases}f_{\lvert\mathrm{x}\rvert}(\mathrm{x}/\lvert\mathrm{x}\rvert)&\text{if $\lvert\mathrm{x}\rvert\neq 0$}\\ x_0&\text{if $\lvert\mathrm{x}\rvert=0$}\end{cases}$$

is the continuous function required by the third condition. Conversely, assuming the third condition, for any given loop $f$, setting $f_t(\mathrm{x})=\widetilde{f}(t\mathrm{x})$ defines a homotopy from $f_1=f$ to the constant map.
:::

::: Definition 2
If the equivalent conditions of [Lemma 1](#lem1){: data-relation="required" reviewed="" } hold, we call a path-connected $X$ a *simply connected space*.
:::

## Covering Spaces

For the rest of this post, for convenience we consider only path-connected spaces. Computing the fundamental group of a space that is not simply connected requires several methods; one of the most basic and essential is the use of covering spaces.

::: Definition 3
For a continuous map $p:E \rightarrow B$, an open subset of $B$, $U$, is said to be *evenly covered* by $p$ if $p^{-1}(U)$ can be written as a disjoint union of open subsets of $E$, $\coprod_j V_j$, such that each $p\vert_{V_j}:V_j\rightarrow U$ is a homeomorphism. If for every $x\in B$, there exists, evenly covered by $p$, a suitable open neighborhood $U$, then we call $p$ a *covering map* and $E$ a *covering space*.
:::

Although the definition is somewhat involved, in essence it is helpful to keep the following picture in mind.

{% diagram Math/Algebraic_Topology/Covering_Spaces-1.svg width="26em" alt="S1_covering" %}

This depicts the covering map

$$p:\mathbb{R}\rightarrow S^1;\quad t\mapsto (\cos 2\pi t, \sin 2\pi t)$$

and we know that it satisfies the condition of [Definition 3](#def3){: data-relation="required" reviewed="" }. Meanwhile, in general, one can easily prove that covering maps behave well with respect to subspaces and products, as follows.

::: Proposition 4
The following hold.

1. For a covering map $p:E \rightarrow B$ and a subspace of $B$, $A$, $p\vert_{p^{-1}(A)}:p^{-1}(A) \rightarrow A$ is a covering map.
2. For two covering maps $p_1:E_1 \rightarrow B_1$ and $p_2:E_2\rightarrow B_2$, $p_1\times p_2:E_1\times E_2 \rightarrow B_1\times B_2$ is a covering map.
:::
::: Proof
1. For any $x\in A$, choose, evenly covered by $p$, an open neighborhood of $x$, $U\subseteq B$, and write $p^{-1}(U)=\coprod_j V_j$. Then $U\cap A$ is an open set of $A$, and the equation

    $$p^{-1}(U\cap A)=\coprod_j \left(V_j\cap p^{-1}(A)\right)$$

    holds, and each $V_j\cap p^{-1}(A) \rightarrow U\cap A$ is the restriction of the homeomorphism $p\vert_{V_j}$ to a subspace, hence again a homeomorphism.
2. Similarly, for any $(x_1,x_2)\in B_1\times B_2$, choose evenly covered open neighborhoods $U_1,U_2$ and write $p_i^{-1}(U_i)=\coprod_j V^i_j$. Then the equation

    $$(p_1\times p_2)^{-1}(U_1\times U_2)=\coprod_{j,k}V^1_j\times V^2_k$$

    holds, and the restriction of $p_1\times p_2$ to each $V^1_j\times V^2_k$ is the product of two homeomorphisms, hence again a homeomorphism.
:::

## Fundamental Theorem of Covering Spaces

By the functoriality of the fundamental groupoid $\Pi_1:\Top \rightarrow \Grpd$, any continuous map $p:E \rightarrow B$ defines the following groupoid homomorphism:

$$\Pi_1(p):\Pi_1(E) \rightarrow \Pi_1(B)$$

In particular, for any $y_0, y_1\in E$, the following map

$$\Hom_{\Pi_1(E)}(y_0, y_1)\rightarrow \Hom_{\Pi_1(B)}(p(y_0), p(y_1))\tag{$\ast$}$$

is well-defined. If $p(y_0)=p(y_1)=x$, then the codomain of ($\ast$) is the fundamental group $\pi_1(B,x)$, and in particular, when $y_0=y_1$, ($\ast$) becomes the group homomorphism $\pi_1(E,y_0)\rightarrow \pi_1(B,x)$.

::: Definition 5
Fix a continuous map $p:E\rightarrow B$. Then for any continuous map $f:X \rightarrow B$, a *lifting* of $f$ with respect to $p$ means a map satisfying the equation $p\circ\widetilde{f}=f$, namely $\widetilde{f}:X\rightarrow E$.
:::

The reason for considering this definition is of course that when $X=I$ and thus $f$ is a path in $B$, if a lifting of $f$ with respect to $p$ exists, it belongs to the preimage of $f$ under the homomorphism ($\ast$). Our claim, then, is that if $p$ is a covering map, such a lifting always exists.

::: Lemma 6
Consider a covering map $p:E \rightarrow B$ and an arbitrary point of $E$, $y_0$. Then whenever any path starting at $x_0=p(y_0)$, $\alpha:I \rightarrow B$, is given, there exists a unique lifting starting at $y_0$, $\widetilde{\alpha}:I \rightarrow E$. 
:::
::: Proof
First, from the assumption that $p$ is a covering map, there exists an open covering of $B$, $(U_i)$, such that each $U_i$ is evenly covered by $p$. Now, since $(\alpha^{-1}(U_i))$ is an open covering of $I$, there exists a finite subcover covering $I$. Now, using the Lebesgue number lemma, we can find a subdivision of $I$, 

$$0=s_0<s_1<\cdots<s_n=1$$

such that $\alpha([s_i,s_{i+1}])$ is contained in $U$. Now define $\widetilde{\alpha}(0)=y_0$, and to define $\widetilde{\alpha}$ inductively, assume that for $0\leq s\leq s_i$, $\widetilde{\alpha}$ is defined, and on $[s_i,s_{i+1}]$ let us define $\widetilde{\alpha}$. First, by the choice of the $s_i$, $\alpha([s_i,s_{i+1}])$ is contained in an open set evenly covered by $p$, namely $U$. Therefore, we can write $p^{-1}(U)$ as a disjoint union of open sets homeomorphic to $U$, $\coprod_{j\in J}V_j$. Now, with $\widetilde{\alpha}(s_i)\in V_j$, for this $V_j$, it suffices to define $\widetilde{\alpha}$ by the following formula:

$$\widetilde{\alpha}(s)=(p\vert_{V_j})^{-1}(\alpha(s))$$

As for uniqueness, since $[s_i,s_{i+1}]$ is connected and inductively the component containing $\widetilde{\alpha}(s_i)$ is determined step by step, it is trivial. 
:::

The proof may appear somewhat technical, but the key idea is that any path starting at $x_0\in B$ will, at least for a short time, be contained in an open neighborhood evenly covered by $p$ of $x_0$, namely $U$, and by definition $p^{-1}(U)$ is a union of disjoint open subsets homeomorphic to $U$ in $E$; thus, knowing only which of these the starting point belongs to determines (by connectedness) which component the path stays in during this short time. The Lebesgue number lemma was used only to show that this process is finite. 

Let us look again at the groupoid homomorphism ($\ast$). By [Lemma 6](#lem6){: data-relation="required" reviewed="" }, in a covering space $p:E \rightarrow B$, given any $x_0,x_1\in B$ and a path $\alpha$ having these as endpoints, a choice of $y_0\in p^{-1}(x_0)$ determines $y_1\in p^{-1}(x_1)$ and $\widetilde{\alpha}\in \Hom_{\Pi_1(E)}(y_0,y_1)$. Then the natural question would be whether, for a path that is path-homotopic to $\alpha$, $\alpha'$, the same choice of $y_0$ gives the same $y_1$ and homotopy type. If $p$ is a covering map, the answer to this is also affirmative. 

::: Lemma 7
Consider a covering map $p:E \rightarrow B$ and an arbitrary point of $E$, $y_0$, and let $p(y_0)=x_0$. Then whenever a continuous function satisfying $F(0,0)=x_0$, $F:I\times I \rightarrow B$, is given, there exists a unique lifting satisfying $\widetilde{F}(0,0)=y_0$, $\widetilde{F}:I\times I \rightarrow E$. Furthermore, if $F$ is a path homotopy, then $\widetilde{F}$ is also a path homotopy.  
:::

The proof of this is essentially no different from [Lemma 6](#lem6){: data-relation="required" reviewed="" }, so we omit it. What is important is that, by the path homotopy given by this lemma, given a covering space $p:E \rightarrow B$ and a path class $[\alpha]\in\Hom_{\Pi_1(B)}(x_0,x_1)$, a choice of $y_0\in p^{-1}(x_0)$ uniquely determines a path class of $E$, $[\widetilde{\alpha}]\in \Hom_{\Pi_1(E)}(y_0,y_1)$. 

Now consider the fundamental groupoid $\Pi_1(B)$ again and fix a covering map $p:E \rightarrow B$. Then, by the evenly covered condition, for each $x\in B$, $p^{-1}(x)$ is a discrete set. At this time, for any path class $[\alpha]\in\Hom_{\Pi_1(B)}(x_0,x_1)$, if we choose $y_0\in p^{-1}(x_0)$, [Lemma 7](#lem7){: data-relation="required" reviewed="" } defines a unique path class $[\widetilde{\alpha}]$, and thus defines $y_1\in p^{-1}(x_1)$. That is, $[\alpha]$ defines a function $p^{-1}(x_0)\rightarrow p^{-1}(x_1)$.

::: Definition 8
In the situation above, we call the function $p^{-1}(x_0)\rightarrow p^{-1}(x_1)$ the *transport map* and denote it by $T_{[\alpha]}$. 
:::

The transport map is bijective. First, this is because, given any $y_1\in p^{-1}(x_1)$, we can use the path class $[\overline{\alpha}]\in\Hom_{\Pi_1(B)}(x_1,x_0)$ to find a path starting at $y_1$ and ending in $p^{-1}(x_0)$ at some element $y_0$, and this process is unique by [Lemma 7](#lem7){: data-relation="required" reviewed="" }. Similarly, by the uniqueness of liftings, we know that this correspondence preserves path concatenation well. That is, the assignment sending $x\in \Pi_1(B)$ to $p^{-1}(x)$ and $[\alpha]\in\Hom_{\Pi_1(B)}(x_0,x_1)$ to $T_{[\alpha]}:p^{-1}(x_0)\rightarrow p^{-1}(x_1)$ is functorial. 

::: Definition 9
We call the functor $\Pi_1(B) \rightarrow \Set$ defined above the *monodromy functor* defined by $p$, and denote it by $M_p$. 
:::

For a fixed base space $B$, we define in the obvious way, for covering spaces of $B$, the category $\Cov(B)$. Explicitly, the objects of this category are covering maps $p:E\rightarrow B$, and a morphism between them is the following commutative diagram:

{% diagram Math/Algebraic_Topology/Covering_Spaces-2.svg width="6.75em" alt="morphism_of_covering_spaces" %}

Through this, we see that assigning to each $p\in \Cov(B)$ the monodromy functor $M_p$ defines a functor

$$M:\Cov(B) \rightarrow \Fun(\Pi_1(B),\Set)$$

and the main result of this post is that this is an equivalence between the two categories. To show this, beginning with the functoriality of the correspondence above, there is much to show, but ultimately the most essential part is that given any functor $\Pi_1(B)\rightarrow \Set$, we construct from it a covering space $E \rightarrow B$. To this end, given any functor $F:\Pi_1(B) \rightarrow \Set$, tracing backward along the monodromy functor above makes it obvious how to construct $p:E\rightarrow B$ *as a function between sets*. For each $x\in \Pi_1(B)$, since $F(x)$ will correspond, at $x$, to the fiber of $p$, we can take the projection

$$p:E=\coprod_{x\in B}F(x) \rightarrow B$$

The problem is to endow $E$ with a topology that makes this a covering space. If such a topology exists, there must exist, for $x$, an open neighborhood $U$ such that there is a homeomorphism between $p^{-1}(U)$ and $U\times F(x)$. Thinking of the familiar $\mathbb{R}\rightarrow S^1$, this is intuitively clear, since $p^{-1}(U)$ is a disjoint union of sets homeomorphic to $U$, and therefore any element of $p^{-1}(U)$ is determined by which of these sets it lies in ($F(x)$), and which point of that set it is ($U$). We will conversely construct a bijection $\phi:p^{-1}(U) \rightarrow U\times F(x)$ and use it to define a topology on $p^{-1}(U)$. Then showing that these $\phi$ define the same function on overlaps, and thus that these bijections give a suitable topology on $E$ that satisfies our desired properties, is pure routine; the heart of the proof lies in defining $\phi$. 

From the form of $p$ defined above, we know that $p^{-1}(U)$ is, for points satisfying $x'\in U$ among the $x'$, the collection of $F(x')$. Then for $e\in F(x')$, the first coordinate of $\phi(e)$ should of course be $x'$ itself, and the second coordinate, considering the transport map, should be, connected by a path to $x'$, an element of $F(x)$. However, since this information must be contained in $\Pi_1(B)$ for this purpose, we know that

1. $U$ must be path-connected so that between $x$ and $x'$, a path class $[\alpha]\in \Hom_{\Pi_1(B)}(x,x')$ always exists, and
2. such a path class must be uniquely determined. 

The first condition is simply that $B$ be locally path-connected. The second condition is more subtle: two paths in $U$ sharing endpoints need only define the same path class *in $B$*. This is a weaker condition than locally simply connected.

::: Definition 10
A topological space $X$ is *semi-locally simply connected* if for every $x\in X$ there exists an open neighborhood $U$ such that every loop in $U$ is contractible in $X$.
:::

Then we see that for the above argument to hold, the space $B$ must satisfy, in addition to the previously assumed path-connectedness condition, the two conditions of being locally path-connected and semi-locally simply connected. Now, combining the discussion above, we obtain the following result.

::: Theorem 11 (Fundamental theorem of covering spaces)
For a path-connected, locally path-connected, semi-locally simply connected space $B$, there exists an equivalence

$$M:\Cov(B) \rightarrow \Fun(\Pi_1(B), \Set)$$

between the two categories.
:::

For example, any path-connected topological manifold always satisfies the above conditions.

We now need to examine what $\Fun(\Pi_1(B), \Set)$ is. More generally, for an arbitrary groupoid $\mathcal{G}$, let us consider what a functor $\mathcal{G}\rightarrow \Set$ is. By definition, this consists of

- for each object of $\mathcal{G}$, $G\in \mathcal{G}$, a corresponding set $S_G$,
- for each (iso)morphism of $\mathcal{G}$, $G \rightarrow H$, a corresponding bijection $S_G \rightarrow S_H$.

Since this alone still does not make clear what a functor $\mathcal{G}\rightarrow \Set$ is, let us specifically look at the situation where $\mathcal{G}$ has only one object $\ast$, and therefore all morphisms of $\mathcal{G}$ become automorphisms of $\ast$. That is, $\mathcal{G}$ is a group. Then under this assumption, a functor $\mathcal{G}\rightarrow \Set$ is the following data:

- for the unique object of $\mathcal{G}$, a corresponding set $S$,
- for each automorphism $g:\ast \rightarrow \ast$, a corresponding bijection $g\cdot-: S\rightarrow S$.

That is, as can be guessed from the notation, this information is precisely an action of the group $\mathcal{G}$, and $\Fun(\mathcal{G},\Set)$ is precisely the collection of $\mathcal{G}$-sets, and morphisms between them are $\mathcal{G}$-equivariant maps. For a general groupoid $\mathcal{G}$, it is simply that several groups act separately on several sets, but two isomorphic objects of $\mathcal{G}$, $G,H$, must act in the same way on their respective (isomorphic) sets $S_G$ and $S_H$.

However, since the space $B$ is path-connected, the fundamental groupoid $\Pi_1(B)$ is a connected groupoid; therefore, $\Pi_1(B)$ is, for any $x\in B$, equivalent as a category to the group $\pi_1(B,x)$. That is, a groupoid action of $\Pi_1(B)$ is nothing more than replicating the group action of the group $\pi_1(B,x)$ along isomorphisms in the groupoid $\Pi_1(B)$. Therefore, the information contained in [Theorem 11](#thm11){: data-relation="required" reviewed="" } above is essentially contained in the skeleton. Thus, let us consider
  
$$\sk(M):\sk(\Cov(B))\rightarrow \sk(\Fun(\Pi_1(B), \ Set))$$

This is an equivalence that takes an isomorphism class of covering spaces and yields the monodromy functor $M_p$ up to natural isomorphism; that is, $\Pi_1(B)$-sets up to isomorphism. In general, since

$$\sk(\Fun(\Pi_1(B),\Set))\simeq\Fun(\sk(\Pi_1(B)), \Set)$$

using again here that $B$ is path-connected, we know that there exists a categorical equivalence that takes an isomorphism class of covering spaces and yields a $\pi_1(B,x)$-set.

However, considering [\[Algebraic Structures\] §Group Action, ⁋Theorem 14](/en/math/algebraic_structures/group_actions#thm14){: data-relation="required" reviewed="" } and its proof, given any $G$-set $E$, we can decompose $E$ into orbits of $G$, and then the $G$-action restricted to each of these orbits is transitive, and for a suitable subgroup of $G$, $H$, endowed with the canonical $G$-action, $G/H$ is isomorphic to each of these. Therefore, if we decide to consider only transitive group actions, by the definition of the monodromy functor this amounts to considering only *connected* covers on the target side. That is, there exists the following equivalence

$$\left\{\text{isomorphism classes of connected covering spaces of $B$}\right\}\simeq \left\{\text{transitive $\pi_1(B,x)$-sets}\right\}$$

and considering again the skeleton category classifying transitive $\pi_1(B,x)$-sets up to isomorphism, we finally obtain the following equivalence

$$\left\{\text{isomorphism classes of connected covering spaces of $B$}\right\}\simeq \left\{\text{conjugacy classes of subgroups of $\pi_1(B,x)$}\right\}$$

Now, if we order each of these by the relation that there exists a morphism from one to the other, they are merely partially ordered sets ([\[Category Theory\] §Category, ⁋Example 3](/en/math/category_theory/categories#ex3){: data-relation="weak" reviewed="" }), and we know that this equivalence is an isomorphism between posets. That is, we obtain the following result.

::: Corollary 12 (Fundamental theorem of covering spaces, classical version)
For a path-connected, locally path-connected, semi-locally simply connected space $B$, there exists a Galois correspondence between the set of isomorphism classes of connected covering spaces and the conjugacy classes of subgroups of $\pi_1(B)$. 
:::

Explicitly, given a covering space $p:E \rightarrow B$, a subgroup is defined via $\pi_1(p):\pi_1(E)\rightarrow \pi_1(B)$, and since two transitive $G$-sets $X\cong G/H$ and $Y\cong G/K$ being isomorphic is equivalent to $H$ and $K$ being conjugate to each other, we obtain the result above. On the other hand, if instead of the conjugacy classes of subgroups of $\pi_1(B,x)$ we consider the explicit subgroups themselves, this amounts to choosing one of the isomorphic covering spaces, which is precisely the same as fixing a base point of $B$ and then considering *pointed* covering maps $p:(E, y)\rightarrow (B,x)$ to view the elements of these isomorphism classes separately. That is, the following Galois correspondence

$$\left\{\text{isomorphism classes of connected \textit{pointed} covering spaces of $B$}\right\}\simeq \left\{\text{subgroups of $\pi_1(B,x)$}\right\}$$

exists. Putting this into a slightly more familiar form, for any $H\leq \pi_1(B,x)$ we can construct the corresponding covering space $E_H$, and then for $E_H$'s automorphism group $\Aut(E_H/B)$,

$$\Aut(E_H/B)\cong N_{\pi_1(B,x)}(H)/H$$

holds. We call this the *Deck transformation group* of $E_H$, and its elements *Deck transformations*.

Meanwhile, in the poset of subgroups (or their conjugacy classes) of $\pi_1(B,x)$, there exists a minimal element $\left\{e\right\}$. Then by the Galois correspondence above, there exists a corresponding *universal cover* $\widetilde{B}$. The Deck transformation group of this covering space is isomorphic to $\pi_1(B,x)$, and $\widetilde{B}$ is simply connected.

## Seifert–van Kampen Theorem

For nice spaces that we know, we can compute the fundamental group or homology from the definition, but in most cases computing this from the definition is excessively complicated or nearly impossible. Our idea is to express a large space in terms of smaller spaces to compute its fundamental group. 

The simplest among these methods would be the case where a space $X$ is expressed as the union $X=U\cup V$ of two open sets. Then by [\[Topology\] §Presheaves, ⁋Lemma 1](/en/math/topology/presheaves#lem1){: data-relation="required" reviewed="" }, we know that the following diagram 

{% diagram Math/Algebraic_Topology/Covering_Spaces-3.svg width="7.54em" alt="union_as_colimit" %}

is a colimit diagram. In this case, our goal will be to apply the fundamental groupoid functor $\Pi_1$ to this diagram to express $\Pi_1(X)$ using $\Pi_1(U)$, $\Pi_1(V)$, and $\Pi_1(U\cap V)$. Meanwhile, by [\[Topology\] §Presheaves, ⁋Lemma 1](/en/math/topology/presheaves#lem1){: data-relation="required" reviewed="" }, we know that for any open covering $(U_i)$, the following diagram 
  
{% diagram Math/Algebraic_Topology/Covering_Spaces-4.svg width="17.30em" alt="general_union_colimit" %}

is a colimit diagram. Our claim is that if the fundamental groupoids of $(U_i)$ and of their finite intersections are all known, then from these we can compute the fundamental groupoid $\Pi_1(X)$.

::: Theorem 13 (Seifert–van Kampen)
For a topological space $X$, let an open cover $\mathcal{O}=(U_i)$ be given, and assume that every finite intersection of elements of $\mathcal{O}$ again belongs to $\mathcal{O}$. Then the colimit of the $\mathcal{O}$-shaped diagram $\Pi_1:\mathcal{O}\rightarrow\Grpd$ exists and is isomorphic to $\Pi_1(X)$. 
:::
::: Proof
That is, it suffices to show that for any groupoid $\mathcal{G}\in\Grpd$ and any cocone $\lambda:\Pi_1\vert_\mathcal{O}\Rightarrow \mathcal{G}$, so that for each $U\in \mathcal{O}$, $\widetilde{\lambda}$ and $\lambda_U$ are equal, there exists a unique $\widetilde{\lambda}:\Pi_1(X)\rightarrow \mathcal{G}$. Naturally, for each $x\in X$, after finding that $x\in U$ for some $U$, since on $U$, $\lambda_U$ is defined, we can define $\widetilde{\lambda}(x)$ to be this value $\lambda_U(x)$. Meanwhile, we can make a similar definition for morphisms: for a path completely contained in some $U\in \mathcal{O}$, say $f$, this definition is well-defined for the same reason as above, and the only thing that remains to be shown is how it should be defined when the path does not belong to a single $U\in \mathcal{O}$. But in that case we can simply use concatenation of paths. We only need to show that this is always defined and well-defined. 
:::

Now, just as when we derived [Corollary 12](#cor12){: data-relation="weak" reviewed="" } above, we apply this theorem to a single object, thus replace $\Grpd$ by $\Grp$, and use the fact that pushouts in $\Grp$ are amalgamated free products to obtain the following result. 

::: Corollary 14 (Seifert–van Kampen theorem, classical version)
Suppose a topological space $X$ is expressed as the union of two path-connected open subsets $U,V$, and assume that $U\cap V$ is nonempty and path-connected. Then the following diagram

{% diagram Math/Algebraic_Topology/Covering_Spaces-5.svg width="18.89em" alt="van_Kampen" %}

is a pushout diagram, and the resulting map $\pi_1(U)\ast_{\pi_1(U\cap V)}\pi_1(V)\rightarrow \pi_1(X)$ is an isomorphism. 
:::

--- 

**References**

**[Hat]** A. Hatcher, *Algebraic Topology*. Cambridge University Press, 2022.  
**[May]** J. P. May, *A concise course in algebraic topology*.  
**[Mun]** James Munkres, *Topology*. Prentice Hall, 2000.  
**[Tao]** Terence Tao, [van Kampen's theorem via covering spaces](https://terrytao.wordpress.com/2012/10/28/van-kampens-theorem-via-covering-spaces/).

---
