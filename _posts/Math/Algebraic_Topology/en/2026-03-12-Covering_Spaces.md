---
title: "Covering Spaces"
description: "This post defines simply connected spaces and the notions of covering spaces and covering maps. It also introduces fundamental methods for computing fundamental groups using the properties of evenly covered neighborhoods."
excerpt: "Equivalent conditions for simply connected spaces, covering spaces, and the Seifert-van Kampen theorem"

categories: [Math / Algebraic Topology]
permalink: /en/math/algebraic_topology/covering_spaces
sidebar: 
    nav: "algebraic_topology-en"

date: 2025-07-27
weight: 4
translated_at: 2026-08-18T13:45:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-08-18T13:45:04+00:00
---
In the previous post, we defined the fundamental group $\pi_1(X)$ and examined some of its basic properties. The following lemma is then almost immediate from the definitions.

::: Lemma 1
For a path-connected space $X$, the following are equivalent.

1. Any two paths $p,q$ with common endpoints are path homotopic.
2. Every loop $f:S^1 \rightarrow X$ is null-homotopic.
3. For every loop $f:S^1 \rightarrow X$, there exists a continuous map $\widetilde{f}:D^2 \rightarrow X$ whose restriction to the boundary $S^1$ of its domain is $f$.
4. $\pi_1(X)=0$.
:::
::: Proof
The equivalence of the first, second, and fourth conditions is immediate upon considering the loop $p\ast\bar{q}$ for two paths $p,q$. Thus it suffices to show that the third condition is equivalent to these.

Assuming the first condition, for any loop $f:S^1 \rightarrow X$ there exists a homotopy $(f_t)$ with $f_1=f$ and $f_0$ the constant map at a fixed point $x_0$. Then the formula

$$\widetilde{f}(\mathrm{x})=\begin{cases}f_{\lvert\mathrm{x}\rvert}(\mathrm{x}/\lvert\mathrm{x}\rvert)&\text{if $\lvert\mathrm{x}\rvert\neq 0$}\\ x_0&\text{if $\lvert\mathrm{x}\rvert=0$}\end{cases}$$

gives the continuous function required by the third condition. Conversely, assuming the third condition, for any loop $f$ the assignment $f_t(\mathrm{x})=\widetilde{f}(t\mathrm{x})$ defines a homotopy from $f_1=f$ to the constant map.
:::

::: Definition 2
If the equivalent conditions of [Lemma 1](#lem1) hold, we call a path-connected $X$ a *simply connected space*.
:::

## Covering Spaces

Henceforth, we assume for convenience that all spaces are path-connected. Computing the fundamental group of a space that is not simply connected requires several methods; one of the most basic and essential is the use of covering spaces.

::: Definition 3
For a continuous map $p:E \rightarrow B$, an open subset $U$ of $B$ is said to be *evenly covered* by $p$ if $p^{-1}(U)$ can be written as a disjoint union $\coprod_j V_j$ of open subsets of $E$ such that each restriction $p\vert_{V_j}:V_j\rightarrow U$ is a homeomorphism. If for every $x\in B$ there exists an open neighborhood $U$ of $x$ that is evenly covered by $p$, then we call $p$ a *covering map* and $E$ a *covering space*.
:::

Although the definition is somewhat involved, it is helpful to keep the following picture in mind.

{% diagram Math/Algebraic_Topology/Covering_Spaces-1.svg width="26em" alt="S1_covering" %}

This depicts the covering map

$$p:\mathbb{R}\rightarrow S^1;\quad t\mapsto (\cos 2\pi t, \sin 2\pi t),$$

and we know that it satisfies the condition of [Definition 3](#def3). In general, one can easily prove that covering maps behave well with respect to subspaces and products, as follows.

::: Proposition 4
The following hold.

1. For a covering map $p:E \rightarrow B$ and a subspace $A$ of $B$, the restriction $p\vert_{p^{-1}(A)}:p^{-1}(A) \rightarrow A$ is a covering map.
2. For two covering maps $p_1:E_1 \rightarrow B_1$ and $p_2:E_2\rightarrow B_2$, the product $p_1\times p_2:E_1\times E_2 \rightarrow B_1\times B_2$ is a covering map.
:::
::: Proof
1. For any $x\in A$, choose an open neighborhood $U\subseteq B$ of $x$ evenly covered by $p$ and write $p^{-1}(U)=\coprod_j V_j$. Then $U\cap A$ is open in $A$, and

    $$p^{-1}(U\cap A)=\coprod_j \left(V_j\cap p^{-1}(A)\right)$$

    holds. Each map $V_j\cap p^{-1}(A) \rightarrow U\cap A$ is the restriction of the homeomorphism $p\vert_{V_j}$ to a subspace, hence again a homeomorphism.
2. Similarly, for any $(x_1,x_2)\in B_1\times B_2$, choose evenly covered open neighborhoods $U_1,U_2$ and write $p_i^{-1}(U_i)=\coprod_j V^i_j$. Then

    $$(p_1\times p_2)^{-1}(U_1\times U_2)=\coprod_{j,k}V^1_j\times V^2_k$$

    holds, and the restriction of $p_1\times p_2$ to each $V^1_j\times V^2_k$ is the product of two homeomorphisms, hence again a homeomorphism.
:::

## Fundamental Theorems of Covering Spaces

By the functoriality of the fundamental groupoid $\Pi_1:\Top \rightarrow \Grpd$, any continuous map $p:E \rightarrow B$ defines a groupoid homomorphism

$$\Pi_1(p):\Pi_1(E) \rightarrow \Pi_1(B).$$

In particular, for any $y_0, y_1\in E$, the map

$$\Hom_{\Pi_1(E)}(y_0, y_1)\rightarrow \Hom_{\Pi_1(B)}(p(y_0), p(y_1))\tag{$\ast$}$$

is well defined. If $p(y_0)=p(y_1)=x$, then the codomain of ($\ast$) is the fundamental group $\pi_1(B,x)$, and when $y_0=y_1$, ($\ast$) becomes the group homomorphism $\pi_1(E,y_0)\rightarrow \pi_1(B,x)$. If $E$ carries all the information about the fundamental group (or groupoid) of $B$, then at minimum this map should be surjective.

::: Definition 5
Fix a continuous map $p:E\rightarrow B$. For any continuous map $f:X \rightarrow B$, a *lifting* of $f$ with respect to $p$ is a map $\widetilde{f}:X\rightarrow E$ satisfying $p\circ\widetilde{f}=f$.
:::

The reason for introducing this definition is of course the case $X=I$, where $f$ is a path in $B$: if a lifting of $f$ with respect to $p$ exists, it lies in the preimage of $f$ under the homomorphism ($\ast$). Our claim, then, is that if $p$ is a covering map, such a lifting always exists.

::: Lemma 6
Let $p:E \rightarrow B$ be a covering map and let $y_0$ be any point of $E$. Then for every path $\alpha:I \rightarrow B$ starting at $x_0=p(y_0)$, there exists a unique lifting $\widetilde{\alpha}:I \rightarrow E$ starting at $y_0$.
:::
::: Proof
Since $p$ is a covering map, there exists an open cover $(U_i)$ of $B$ such that each $U_i$ is evenly covered by $p$. Then $(\alpha^{-1}(U_i))$ is an open cover of $I$, so it has a finite subcover. By the Lebesgue number lemma, we can find a subdivision

$$0=s_0<s_1<\cdots<s_n=1$$

of $I$ such that each $\alpha([s_i,s_{i+1}])$ lies in some $U$. Set $\widetilde{\alpha}(0)=y_0$, and assume inductively that $\widetilde{\alpha}$ is defined for $0\leq s\leq s_i$; we define it on $[s_i,s_{i+1}]$. By the choice of the $s_i$, the image $\alpha([s_i,s_{i+1}])$ lies in some open set $U$ evenly covered by $p$. Hence we can write $p^{-1}(U)$ as a disjoint union $\coprod_{j\in J}V_j$ of open sets, each homeomorphic to $U$. For the unique $V_j$ containing $\widetilde{\alpha}(s_i)$, we define

$$\widetilde{\alpha}(s)=(p\vert_{V_j})^{-1}(\alpha(s)).$$

For uniqueness, since $[s_i,s_{i+1}]$ is connected and the component containing $\widetilde{\alpha}(s_i)$ is determined inductively step by step, it is immediate.
:::

The proof may appear somewhat technical, but the key idea is simple: any path starting at $x_0\in B$ remains for a short time inside an open neighborhood $U$ of $x_0$ that is evenly covered by $p$, and by definition $p^{-1}(U)$ is a disjoint union of open subsets of $E$ each homeomorphic to $U$; thus, knowing only which of these contains the starting point determines (by connectedness) which component the path stays in during this short interval. The Lebesgue number lemma is used only to show that this process terminates after finitely many steps.

Returning to the groupoid homomorphism ($\ast$), [Lemma 6](#lem6) implies that for a covering space $p:E \rightarrow B$, given any $x_0,x_1\in B$ and a path $\alpha$ between them, a choice of $y_0\in p^{-1}(x_0)$ determines $y_1\in p^{-1}(x_1)$ and a lift $\widetilde{\alpha}\in \Hom_{\Pi_1(E)}(y_0,y_1)$. The natural question is then whether, for a path $\alpha'$ path-homotopic to $\alpha$, the same choice of $y_0$ yields the same $y_1$ and the same homotopy class. If $p$ is a covering map, the answer is affirmative.

::: Lemma 7
Let $p:E \rightarrow B$ be a covering map and let $y_0$ be any point of $E$; write $p(y_0)=x_0$. Then for every continuous map $F:I\times I \rightarrow B$ with $F(0,0)=x_0$, there exists a unique lifting $\widetilde{F}:I\times I \rightarrow E$ with $\widetilde{F}(0,0)=y_0$. Moreover, if $F$ is a path homotopy, then so is $\widetilde{F}$.
:::

The proof is essentially no different from that of [Lemma 6](#lem6), so we omit it. The important consequence is that, by this lemma, for a covering space $p:E \rightarrow B$ and a path class $[\alpha]\in\Hom_{\Pi_1(B)}(x_0,x_1)$, a choice of $y_0\in p^{-1}(x_0)$ uniquely determines a path class $[\widetilde{\alpha}]\in \Hom_{\Pi_1(E)}(y_0,y_1)$.

Now reconsider the fundamental groupoid $\Pi_1(B)$ and fix a covering map $p:E \rightarrow B$. By the evenly covered condition, for each $x\in B$ the fiber $p^{-1}(x)$ is a discrete set. Hence, for any path class $[\alpha]\in\Hom_{\Pi_1(B)}(x_0,x_1)$, choosing $y_0\in p^{-1}(x_0)$ defines a unique path class $[\widetilde{\alpha}]$ by [Lemma 7](#lem7), and thus defines $y_1\in p^{-1}(x_1)$. In other words, $[\alpha]$ defines a function $p^{-1}(x_0)\rightarrow p^{-1}(x_1)$.

::: Definition 8
In this situation, we call the function $p^{-1}(x_0)\rightarrow p^{-1}(x_1)$ the *transport map* and denote it by $T_{[\alpha]}$.
:::

The transport map is bijective. Indeed, given any $y_1\in p^{-1}(x_1)$, we can use the path class $[\overline{\alpha}]\in\Hom_{\Pi_1(B)}(x_1,x_0)$ to find a path starting at $y_1$ and ending at some element $y_0\in p^{-1}(x_0)$, and this process is unique by [Lemma 7](#lem7). Similarly, by the uniqueness of liftings, this correspondence preserves path concatenation. That is, the assignment sending $x\in \Pi_1(B)$ to $p^{-1}(x)$ and $[\alpha]\in\Hom_{\Pi_1(B)}(x_0,x_1)$ to $T_{[\alpha]}:p^{-1}(x_0)\rightarrow p^{-1}(x_1)$ is functorial.

::: Definition 9
We call the functor $\Pi_1(B) \rightarrow \Set$ defined above the *monodromy functor* defined by $p$, and denote it by $M_p$.
:::

For a fixed base space $B$, we define in the obvious way the category $\Cov(B)$ of covering spaces of $B$. Explicitly, the objects of this category are covering maps $p:E\rightarrow B$, and a morphism between them is a commutative diagram

{% diagram Math/Algebraic_Topology/Covering_Spaces-2.svg width="6.75em" alt="morphism_of_covering_spaces" %}

Through this, we see that assigning to each $p\in \Cov(B)$ its monodromy functor $M_p$ defines a functor

$$M:\Cov(B) \rightarrow \Fun(\Pi_1(B),\Set),$$

and the main result of this post is that this is an equivalence between the two categories. To prove this, we must begin with the functoriality of the above correspondence; there is much to verify, but ultimately the most essential point is that from any functor $\Pi_1(B)\rightarrow \Set$ we can construct a covering space $E \rightarrow B$. To this end, given any functor $F:\Pi_1(B) \rightarrow \Set$, tracing backwards along the monodromy functor makes it obvious how to construct $p:E\rightarrow B$ as a *function between sets*. For each $x\in B$, the set $F(x)$ will correspond to the fiber of $p$ over $x$, so we set

$$p:E=\coprod_{x\in B}F(x) \rightarrow B$$

to be the projection. The problem is to endow $E$ with a topology that makes this a covering space. If such a topology exists, there should be an open neighborhood $U$ of $x$ and a homeomorphism between $p^{-1}(U)$ and $U\times F(x)$. Thinking of the familiar $\mathbb{R}\rightarrow S^1$, this is intuitively clear: $p^{-1}(U)$ is a disjoint union of sets each homeomorphic to $U$, so any element of $p^{-1}(U)$ is determined by which of these sets it lies in ($F(x)$) and which point of that set it is ($U$). We will conversely construct a bijection $\phi:p^{-1}(U) \rightarrow U\times F(x)$ and use it to define a topology on $p^{-1}(U)$. Showing that these $\phi$ agree on overlaps, and hence that these bijections yield a suitable topology on $E$ with the desired properties, is straightforward; the heart of the proof lies in defining $\phi$.

From the form of $p$ defined above, we know that $p^{-1}(U)$ is the collection of $F(x')$ for $x'\in U$. Then for $e\in F(x')$, the first coordinate of $\phi(e)$ should of course be $x'$ itself, and the second coordinate should be an element of $F(x)$ joined to $x'$ by a path, as we see by considering the transport map. But for this to be information contained in $\Pi_1(B)$, we need

1. $U$ to be path-connected, so that a path class $[\alpha]\in \Hom_{\Pi_1(B)}(x,x')$ always exists between $x$ and $x'$, and
2. such a path class to be uniquely determined.

The first condition is simply that $B$ be locally path-connected. The second condition is more subtle: two paths in $U$ with common endpoints must define the same path class *in $B$*. This is a weaker condition than locally simply connected.

::: Definition 10
A topological space $X$ is called *semi-locally simply connected* if for every $x\in X$ there exists an open neighborhood $U$ such that every loop in $U$ is contractible in $X$.
:::

Thus, for the above argument to work, the space $B$ must satisfy, in addition to the path-connectedness assumed from the outset, the two conditions of being locally path-connected and semi-locally simply connected. Combining the preceding discussion, we obtain the following result.

::: Theorem 11 (Fundamental theorem of covering spaces)
For a path-connected, locally path-connected, semi-locally simply connected space $B$, there exists an equivalence

$$M:\Cov(B) \rightarrow \Fun(\Pi_1(B), \Set)$$

between the two categories.
:::

For example, every path-connected topological manifold satisfies these conditions.

We now examine what $\Fun(\Pi_1(B), \Set)$ is. More generally, consider a functor $\mathcal{G}\rightarrow \Set$ for an arbitrary groupoid $\mathcal{G}$. By definition, it consists of

- a set $S_G$ assigned to each object $G\in \mathcal{G}$,
- a bijection $S_G \rightarrow S_H$ assigned to each (iso)morphism $G \rightarrow H$ in $\mathcal{G}$.

This alone does not yet make clear what a functor $\mathcal{G}\rightarrow \Set$ is, so let us consider the special case where $\mathcal{G}$ has only one object $\ast$, so that all morphisms of $\mathcal{G}$ are automorphisms of $\ast$; that is, $\mathcal{G}$ is a group. Under this assumption, a functor $\mathcal{G}\rightarrow \Set$ is the following data:

- a set $S$ assigned to the unique object of $\mathcal{G}$,
- a bijection $g\cdot-: S\rightarrow S$ assigned to each automorphism $g:\ast \rightarrow \ast$.

That is, as the notation suggests, this data is precisely a group action of $\mathcal{G}$, and $\Fun(\mathcal{G},\Set)$ is precisely the collection of $\mathcal{G}$-sets, with morphisms being $\mathcal{G}$-equivariant maps. For a general groupoid $\mathcal{G}$, the picture is simply that of several groups acting separately on several sets, except that two isomorphic objects $G,H$ of $\mathcal{G}$ must act in the same way on their respective (isomorphic) sets $S_G$ and $S_H$.

Since $B$ is path-connected, the fundamental groupoid $\Pi_1(B)$ is a connected groupoid, and hence equivalent as a category to the group $\pi_1(B,x)$ for any $x\in B$. Thus a groupoid action of $\Pi_1(B)$ is nothing more than a group action of $\pi_1(B,x)$ replicated along isomorphisms in $\Pi_1(B)$. Consequently, the information contained in [Theorem 11](#thm11) is essentially carried by the skeleton. Consider, therefore,

$$\sk(M):\sk(\Cov(B))\rightarrow \sk(\Fun(\Pi_1(B), \Set)).$$

This is an equivalence sending an isomorphism class of covering spaces to the monodromy functor $M_p$ up to natural isomorphism, that is, to $\Pi_1(B)$-sets up to isomorphism. In general,

$$\sk(\Fun(\Pi_1(B),\Set))\simeq\Fun(\sk(\Pi_1(B)), \Set),$$

so using again that $B$ is path-connected, we obtain a categorical equivalence between isomorphism classes of covering spaces and $\pi_1(B,x)$-sets.

But recalling [\[Algebraic Structures\] §Group Actions, ⁋Theorem 14](/en/math/algebraic_structures/group_actions#thm14) and its proof, given any $G$-set $E$ we can decompose $E$ into $G$-orbits; the restriction of the $G$-action to each orbit is transitive, and each orbit is isomorphic to $G/H$ with its canonical $G$-action for some subgroup $H$ of $G$. Hence, if we restrict attention to transitive group actions, the definition of the monodromy functor implies that on the target side this corresponds to considering only *connected* covers. That is, we have an equivalence

$$\left\{\text{isomorphism classes of connected covering spaces of $B$}\right\}\simeq \left\{\text{transitive $\pi_1(B,x)$-sets}\right\},$$

and passing again to the skeleton category of transitive $\pi_1(B,x)$-sets up to isomorphism, we finally obtain

$$\left\{\text{isomorphism classes of connected covering spaces of $B$}\right\}\simeq \left\{\text{conjugacy classes of subgroups of $\pi_1(B,x)$}\right\}.$$

If we now order each of these sets by the existence of a morphism from one object to the other, they become merely partially ordered sets ( [\[Category Theory\] §Category, ⁋Example 3](/en/math/category_theory/categories#ex3) ), and the above equivalence is an isomorphism of posets. Hence we obtain the following.

::: Corollary 12 (Fundamental theorem of covering spaces, classical version)
For a path-connected, locally path-connected, semi-locally simply connected space $B$, there exists a Galois correspondence between the set of isomorphism classes of connected covering spaces of $B$ and the conjugacy classes of subgroups of $\pi_1(B)$.
:::

Explicitly, given a covering space $p:E \rightarrow B$, the subgroup is defined via $\pi_1(p):\pi_1(E)\rightarrow \pi_1(B)$; and since two transitive $G$-sets $X\cong G/H$ and $Y\cong G/K$ are isomorphic if and only if $H$ and $K$ are conjugate, we obtain the result above. On the other hand, if we consider the subgroups themselves rather than their conjugacy classes, this corresponds to choosing a representative from each isomorphism class of covering spaces, which is exactly the same as fixing a base point of $B$ and considering *pointed* covering maps $p:(E, y)\rightarrow (B,x)$, viewing the elements of their isomorphism classes separately. That is, we have a Galois correspondence

$$\left\{\text{isomorphism classes of connected \textit{pointed} covering spaces of $B$}\right\}\simeq \left\{\text{subgroups of $\pi_1(B,x)$}\right\}.$$

In a more familiar form, for any $H\leq \pi_1(B,x)$ we can construct the corresponding covering space $E_H$, and then for the automorphism group $\Aut(E_H/B)$ of $E_H$ we have

$$\Aut(E_H/B)\cong N_{\pi_1(B,x)}(H)/H.$$

We call this the *Deck transformation group* of $E_H$, and its elements *Deck transformations*.

Now, the poset of subgroups (or their conjugacy classes) of $\pi_1(B,x)$ has a minimal element $\{e\}$. By the Galois correspondence above, this corresponds to a *universal cover* $\widetilde{B}$. The Deck transformation group of this covering space is isomorphic to $\pi_1(B,x)$, and $\widetilde{B}$ is simply connected.

## Seifert–van Kampen Theorem

For the familiar nice spaces, we can sometimes compute the fundamental group or homology directly from the definition, but in most cases doing so is excessively complicated or nearly impossible. Our idea is to compute the fundamental group of a large space by decomposing it into smaller ones.

The simplest such method is the case where a space $X$ is the union $X=U\cup V$ of two open sets. Then by [\[Topology\] §Presheaves, ⁋Lemma 1](/en/math/topology/presheaves#lem1), the diagram

{% diagram Math/Algebraic_Topology/Covering_Spaces-3.svg width="7.54em" alt="union_as_colimit" %}

is a colimit diagram. In this case, our goal is to express $\Pi_1(X)$ in terms of $\Pi_1(U)$, $\Pi_1(V)$, and $\Pi_1(U\cap V)$ by applying the fundamental groupoid functor $\Pi_1$ to this diagram. On the other hand, by [\[Topology\] §Presheaves, ⁋Lemma 1](/en/math/topology/presheaves#lem1), for any open covering $(U_i)$ the diagram

{% diagram Math/Algebraic_Topology/Covering_Spaces-4.svg width="17.30em" alt="general_union_colimit" %}

is a colimit diagram. Our claim is that if the fundamental groupoids of the $(U_i)$ and of all their finite intersections are known, then we can compute the fundamental groupoid of $\Pi_1(X)$ from them.

::: Theorem 13 (Seifert–van Kampen)
Let $\mathcal{O}=(U_i)$ be an open cover of a topological space $X$, and assume that every finite intersection of elements of $\mathcal{O}$ again belongs to $\mathcal{O}$. Then the colimit of the $\mathcal{O}$-shaped diagram $\Pi_1:\mathcal{O}\rightarrow\Grpd$ exists and is isomorphic to $\Pi_1(X)$.
:::
::: Proof
That is, we must show that for any groupoid $\mathcal{G}\in\Grpd$ and any cocone $\lambda:\Pi_1\vert_\mathcal{O}\Rightarrow \mathcal{G}$, there exists a unique $\widetilde{\lambda}:\Pi_1(X)\rightarrow \mathcal{G}$ that agrees with $\lambda_U$ on each $U\in \mathcal{O}$. Of course, for any $x\in X$ we choose $U$ with $x\in U$, and since $\lambda_U$ is defined on $U$, we set $\widetilde{\lambda}(x)$ to be the value $\lambda_U(x)$. For morphisms we can make a similar definition: for a path $f$ completely contained in some $U\in \mathcal{O}$, this definition is well defined for the same reason as above. The only thing that must be shown unique is how to define it when the path does not lie in a single $U\in \mathcal{O}$. But in that case we simply use concatenation of paths. We must verify that this is always defined and well defined.
:::

Now, just as when we derived [Corollary 12](#cor12) above, we apply this theorem to a single object, replace $\Grpd$ by $\Grp$, and use the fact that pushouts in $\Grp$ are amalgamated free products, to obtain the following.

::: Corollary 14 (Seifert–van Kampen theorem, classical version)
Let a topological space $X$ be the union of two path-connected open subsets $U,V$, and assume that $U\cap V$ is nonempty and path-connected. Then the diagram

{% diagram Math/Algebraic_Topology/Covering_Spaces-5.svg width="18.89em" alt="van_Kampen" %}

is a pushout diagram, and the induced map $\pi_1(U)\ast_{\pi_1(U\cap V)}\pi_1(V)\rightarrow \pi_1(X)$ is an isomorphism.
:::

--- 

**References**

**[Hat]** A. Hatcher, *Algebraic Topology*. Cambridge University Press, 2022.  
**[May]** J. P. May, *A concise course in algebraic topology*.  
**[Mun]** James Munkres, *Topology*. Prentice Hall, 2000.  
**[Tao]** Terence Tao, [van Kampen's theorem via covering spaces](https://terrytao.wordpress.com/2012/10/28/van-kampens-theorem-via-covering-spaces/).

---
