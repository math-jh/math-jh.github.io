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
translated_at: 2026-07-13T20:30:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-07-13T20:30:02+00:00
---
In the previous post, we defined the fundamental group $\pi_1(X)$ and examined some of its basic properties. The following lemma is then almost obvious from the definitions.

::: Lemma 1
For a path-connected space $X$, the following are all equivalent.

1. Any two paths $p,q$ sharing endpoints are always path homotopic.
2. Any loop $f:S^1 \rightarrow X$ is always null-homotopic.
3. For any loop $f:S^1 \rightarrow X$, there exists a continuous map $\widetilde{f}:D^2 \rightarrow X$ whose restriction to the boundary $S^1$ of its domain is $f$.
4. $\pi_1(X)=0$.
:::
::: Proof
That the first, second, and last conditions are equivalent is obvious by considering the loop $p\ast\bar{q}$ for two paths $p,q$. Thus it suffices to show that the third condition is equivalent to these.

First, assuming the first condition, for any loop $f:S^1 \rightarrow X$ there exists a homotopy $(f_t)$ with $f_1=f$ and $f_0$ the constant map at a fixed point $x_0$. Then the formula

$$\widetilde{f}(\mathrm{x})=\begin{cases}f_{\lvert\mathrm{x}\rvert}(\mathrm{x}/\lvert\mathrm{x}\rvert)&\text{if $\lvert\mathrm{x}\rvert\neq 0$}\\ x_0&\text{if $\lvert\mathrm{x}\rvert=0$}\end{cases}$$

is the continuous function required by the third condition. Conversely, assuming the third condition, for any given loop $f$, setting $f_t(\mathrm{x})=\widetilde{f}(t\mathrm{x})$ gives a homotopy from $f_1=f$ to the constant map.
:::

::: Definition 2
If the equivalent conditions of [Lemma 1](#lem1) hold, we call a path-connected $X$ a *simply connected space*.
:::

## Covering Spaces

For the remainder of the post, we assume all spaces are path-connected for convenience. To compute the fundamental group of a space that is not simply connected, several methods are needed; one of the most basic and essential is the use of covering spaces.

::: Definition 3
For a continuous surjection $p:E \rightarrow B$, an open set $U$ of $B$ is *evenly covered* by $p$ if $p^{-1}(U)$ is a union of disjoint open sets of $E$, each homeomorphic to $U$. If for every $x\in B$ there exists an open neighborhood $U$ of $x$ that is evenly covered by $p$, we call $p$ a *covering map* and $E$ a *covering space*.
:::

The definition is somewhat involved, but it is convenient to keep the following picture in mind.

![S1_covering](/assets/images/Math/Algebraic_Topology/Covering_Spaces-1.svg){:style="width:26em" class="invert" .align-center}

This depicts the covering map

$$p:\mathbb{R}\rightarrow S^1;\quad t\mapsto (\cos 2\pi t, \sin 2\pi t)$$

and we know that it satisfies the condition of [Definition 3](#def3). On the other hand, in general, it is easy to prove that covering maps behave well with respect to subspaces and product spaces as follows.

::: Proposition 4
The following hold.

1. For a covering map $p:E \rightarrow B$ and a subspace $A$ of $B$, the restriction $p\vert_{p^{-1}(A)}:p^{-1}(A) \rightarrow A$ is a covering map.
2. For two covering maps $p_1:E_1 \rightarrow B_1$ and $p_2:E_2\rightarrow B_2$, the product $p_1\times p_2:E_1\times E_2 \rightarrow B_1\times B_2$ is a covering map.
:::

## Fundamental Theorems of Covering Spaces

Using the functoriality of the fundamental groupoid $\Pi_1:\Top \rightarrow \Grpd$, any continuous map $p:E \rightarrow B$ defines the groupoid homomorphism

$$\Pi_1(f):\Pi_1(E) \rightarrow \Pi_1(B)$$

In particular, for any $y_0, y_1\in E$, the homomorphism

$$\Hom_{\Pi_1(E))}(y_0, y_1)\rightarrow \Hom_{\Pi_1(B)}(p(y_0), p(y_1))\tag{$\ast$}$$

is well-defined. If $B$ is path-connected and $p(y_0)=p(y_1)$, this becomes a (groupoid) homomorphism into the fundamental group $\pi_1(B)$. If $E$ contains all information about the fundamental group (or groupoid) of $B$, then at least this homomorphism must be surjective.

::: Definition 5
Fix a continuous map $p:E\rightarrow B$. For any continuous map $f:X \rightarrow B$, a *lifting* of $f$ with respect to $p$ is a map $\widetilde{f}:X\rightarrow E$ satisfying $p\circ\widetilde{f}=f$.
:::

The reason for introducing this definition is of course that when $X=I$ and thus $f$ is a path in $B$, if a lifting of $f$ with respect to $p$ exists then it lies in the preimage of $f$ under the homomorphism ($\ast$). Our claim is then that if $p$ is a covering map, such a lifting always exists.

::: Lemma 6
Consider a covering map $p:E \rightarrow B$ and any point $y_0$ in $E$. Then for any path $\alpha:I \rightarrow B$ starting at $x_0=p(y_0)$, there exists a unique lifting $\widetilde{\alpha}:I \rightarrow E$ starting at $y_0$.
:::
::: Proof
First, since $p$ is a covering map, there exists an open covering $(U_i)$ of $B$ such that each $U_i$ is evenly covered by $p$. Now $(\alpha^{-1}(U_i))$ is an open covering of $I$, so there exists a finite subcover. Using the Lebesgue number lemma, we can find a subdivision of $I$

$$0=s_0<s_1<\cdots<s_n=1$$

such that $\alpha([s_i,s_{i+1}])$ lies inside some $U$. Define $\widetilde{\alpha}(0)=y_0$, and to define $\widetilde{\alpha}$ inductively, assume that $\widetilde{\alpha}$ is defined for $0\leq s\leq s_i$ and define it on $[s_i,s_{i+1}]$. By the choice of the $s_i$, the image $\alpha([s_i,s_{i+1}])$ lies in an open set $U$ that is evenly covered by $p$. Thus we can write $p^{-1}(U)$ as a disjoint union $\coprod_{j\in J}V_j$ of open sets, each homeomorphic to $U$. For the unique $V_j$ with $\widetilde{\alpha}(s_i)\in V_j$, we define $\widetilde{\alpha}$ by

$$\widetilde{\alpha}(s)=(p\vert_{V_j})^{-1}(\alpha(s))$$

For uniqueness, since $[s_i,s_{i+1}]$ is connected and the component containing $\alpha(s_i)$ is determined inductively step by step, this is obvious.
:::

The proof may seem somewhat technical, but the key idea is that any path starting at $x_0\in B$ will, for at least a short time, lie in an open neighborhood $U$ of $x_0$ that is evenly covered by $p$; by definition, $p^{-1}(U)$ is a union of disjoint open subsets of $E$ homeomorphic to $U$, so once we know which of these the starting point belongs to, the component in which the path stays during this short time is determined (by connectedness). The Lebesgue number lemma is used only to show that this process is finite.

Now look again at the groupoid homomorphism ($\ast$). By [Lemma 6](#lem6), for a covering space $p:E \rightarrow B$, given any $x_0,x_1\in B$ and a path $\alpha$ between them, a choice of $y_0\in p^{-1}(x_0)$ determines $y_1\in p^{-1}(x_1)$ and $\widetilde{\alpha}\in \Hom_{\Pi_1(E)}(y_0,y_1)$. A natural question is then whether, for $\alpha'$ path-homotopic to $\alpha$, the same choice of $y_0$ yields the same $y_1$ and homotopy class. If $p$ is a covering map, the answer is also positive.

::: Lemma 7
Consider a covering map $p:E \rightarrow B$ and any point $y_0$ in $E$, and let $p(y_0)=x_0$. Then for any continuous map $F:I\times I \rightarrow B$ satisfying $F(0,0)=x_0$, there exists a unique lifting $\widetilde{F}:I\times I \rightarrow E$ with $\widetilde{F}(0,0)=y_0$. Moreover, if $F$ is a path homotopy then $\widetilde{F}$ is also a path homotopy.
:::

The proof of this is essentially no different from that of [Lemma 6](#lem6), so we omit it. What is important is that by this lemma, for a covering space $p:E \rightarrow B$ and a path class $[\alpha]\in\Hom_{\Pi_1(B)}(x_0,x_1)$, a choice of $y_0\in p^{-1}(x_0)$ uniquely determines a path class $[\widetilde{\alpha}]\in \Hom_{\Pi_1(E)}(y_0,y_1)$ in $E$.

Now consider again the fundamental groupoid $\Pi_1(B)$ and fix a covering map $p:E \rightarrow B$. By the evenly covered condition, for each $x\in B$ the set $p^{-1}(x)$ is discrete. For any path class $[\alpha]\in\Hom_{\Pi_1(B)}(x_0,x_1)$, choosing $y_0\in p^{-1}(x_0)$ defines a unique path class $[\widetilde{\alpha}]$ by [Lemma 7](#lem7), and thus defines $y_1\in p^{-1}(x_1)$. That is, $[\alpha]$ defines a function $p^{-1}(x_0)\rightarrow p^{-1}(x_1)$.

::: Definition 8
In the situation above, we call the function $p^{-1}(x_0)\rightarrow p^{-1}(x_1)$ the *transport map* and denote it by $T_{[\alpha]}$.
:::

The transport map is bijective. Indeed, given any $y_1\in p^{-1}(x_1)$, we can use the path class $[\overline{\alpha}]\in\Hom_{\Pi_1(B)}(x_1,x_0)$ to find a path starting at $y_1$ and ending at some element $y_0$ in $p^{-1}(x_0)$, and this process is unique by [Lemma 7](#lem7). Similarly, by the uniqueness of liftings, we know that this correspondence preserves path concatenation. That is, the assignment sending $x\in \Pi_1(B)$ to $p^{-1}(x)$ and $[\alpha]\in\Hom_{\Pi_1(B)}(x_0,x_1)$ to $T_{[\alpha]}:p^{-1}(x_0)\rightarrow p^{-1}(x_1)$ is functorial.

::: Definition 9
We call the functor $\Pi_1(B) \rightarrow \Set$ defined above the *monodromy functor* defined by $p$ and denote it by $M_p$.
:::

For a fixed base space $B$, we define the category $\Cov(B)$ of covering spaces of $B$ in the obvious way. Explicitly, the objects of this category are covering maps $p:E\rightarrow B$, and a morphism between them is the following commutative diagram

![morphism_of_covering_spaces](/assets/images/Math/Algebraic_Topology/Covering_Spaces-2.svg){:style="width:6.75em" class="invert" .align-center}

Through this, we see that assigning to each $p\in \Cov(B)$ its monodromy functor $M_p$ defines a functor

$$M:\Cov(B) \rightarrow \Fun(\Pi_1(B),\Set)$$

and the main result of this post is that this is an equivalence between the two categories. To show this, we must begin with the functoriality of the above correspondence, and there is much to prove, but ultimately the most essential point is that given any functor $\Pi_1(B)\rightarrow \Set$, we can construct a covering space $E \rightarrow B$ from it. For this, suppose any functor $F:\Pi_1(B) \rightarrow \Set$ is given; tracing the monodromy functor backwards, it is obvious how to construct $p:E\rightarrow B$ as a function between sets. For each $x\in \Pi_1(B)$, the set $F(x)$ will correspond to the fiber of $p$ at $x$, so we set the projection

$$p:E=\coprod_{x\in B}F(x) \rightarrow B$$

The problem is to endow $E$ with a topology that makes this a covering space. If such a topology exists, there should be an open neighborhood $U$ of $x$ and a homeomorphism between $p^{-1}(U)$ and $U\times F(x)$. Thinking of the familiar $\mathbb{R}\rightarrow S^1$, this is intuitively obvious: $p^{-1}(U)$ is a disjoint union of sets homeomorphic to $U$, so any element of $p^{-1}(U)$ is determined by which of these sets it belongs to ($F(x)$) and which point of that set it is ($U$). We will construct a bijection $\phi:p^{-1}(U) \rightarrow U\times F(x)$ and use this to define a topology on $p^{-1}(U)$. Then showing that these $\phi$ agree on overlaps, and thus that these bijections give an appropriate topology on $E$ satisfying the desired properties, is routine; the key of the proof is the part defining $\phi$.

From the form of $p$ defined above, we know that $p^{-1}(U)$ is the collection of $F(x')$ for $x'\in U$. Then the first coordinate of $\phi(x')$ should of course be $x'$ itself, and the second coordinate should be an element of $F(x)$ connected to $x'$ by a path, by the transport map. But for this, the information must be in $\Pi_1(B)$, so we need

1. $U$ to be path-connected so that a path class $[\alpha]\in \Hom_{\Pi_1(B)}(x,x')$ always exists connecting $x$ and $x'$, and
2. such a path class to be uniquely determined.

The first condition is simply that $B$ is locally path-connected. The second condition is somewhat more subtle: two paths in $U$ sharing endpoints must define the same path class *in $B$*. This is a weaker condition than being locally simply connected.

::: Definition 10
A topological space $X$ is *semi-locally simply connected* if for every $x\in X$ there exists an open neighborhood $U$ such that any loop in $U$ is contractible in $X$.
:::

Then for the above argument to work, we see that the space $B$ must satisfy the two conditions of being locally path-connected and semi-locally simply connected in addition to the path-connectedness we assumed earlier. Combining the above discussion, we obtain the following result.

::: Theorem 11 (Fundamental theorem of covering spaces)
For a path-connected, locally path-connected, semi-locally simply connected space $B$, there exists an equivalence

$$M:\Cov(B) \rightarrow \Fun(\Pi_1(B), \Set)$$

between the two categories.
:::

For example, any path-connected topological manifold always satisfies these conditions.

Now we must examine what $\Fun(\Pi_1(B), \Set)$ is. More generally, let us consider what a functor $\mathscr{G}\rightarrow \Set$ is for any groupoid $\mathscr{G}$. By definition, this consists of

- a set $S_G$ corresponding to each object $G\in \mathscr{G}$,
- a bijection $S_G \rightarrow S_H$ corresponding to each (iso)morphism $G \rightarrow H$ of $\mathscr{G}$.

This alone still does not reveal what a functor $\mathscr{G}\rightarrow \Set$ is, so let us consider the special case where $\mathscr{G}$ has only one object $\ast$ and thus all morphisms of $\mathscr{G}$ are automorphisms of $\ast$. That is, $\mathscr{G}$ is a group. Under this assumption, a functor $\mathscr{G}\rightarrow \Set$ is the following data:

- a set $S$ corresponding to the unique object of $\mathscr{G}$,
- a bijection $g\cdot-: S\rightarrow S$ corresponding to each automorphism $g:\ast \rightarrow \ast$.

That is, as one might guess from the notation, this information is exactly a group action of $\mathscr{G}$, and $\Fun(\mathscr{G},\Set)$ is exactly the collection of $\mathscr{G}$-sets, with morphisms being $\mathscr{G}$-equivariant maps. For a general groupoid $\mathscr{G}$, it is simply several groups acting separately on several sets, but isomorphic objects $G,H$ of $\mathscr{G}$ must act in the same way on their respective (isomorphic) sets $S_G$ and $S_H$.

But since the space $B$ is path-connected, the fundamental groupoid $\Pi_1(B)$ is a connected groupoid, and thus $\Pi_1(B)$ is equivalent as a category to the group $\pi_1(B,x)$ for any $x\in B$. That is, a groupoid action of $\Pi_1(B)$ is nothing more than a group action of $\pi_1(B,x)$ replicated along the isomorphisms of the groupoid $\Pi_1(B)$. Therefore, the information contained in [Theorem 11](#thm11) above is essentially contained in the skeleton. Thus let us consider

$$\sk(M):\sk(\Cov(B))\rightarrow \sk(\Fun(\Pi_1(X), \Set))$$

This is an equivalence that takes isomorphism classes of covering spaces and outputs the monodromy functor $M_p$ up to natural isomorphism. That is, $\Pi_1(X)$-sets up to isomorphism. In general, since

$$\sk(\Fun(\Pi_1(X),\Set))\simeq\Fun(\sk(\Pi_1(X)), \Set)$$

using again that $X$ is path-connected, we know that there exists a categorical equivalence taking isomorphism classes of covering spaces and outputting a $\pi_1(X,x)$-set.

But thinking of [\[Algebraic Structures\] §Group Actions, ⁋Theorem 14](/en/math/algebraic_structures/group_actions#thm14) and its proof, given any $G$-set $E$ we can decompose $E$ into orbits of $G$, and the $G$-action restricted to each of these orbits is transitive; these are isomorphic to $G/H$ with the canonical $G$-action for an appropriate subgroup $H$ of $G$. Therefore, if we only consider transitive group actions, by the definition of the monodromy functor this means considering only *connected* covers in the target. That is, we have the equivalence

$$\left\{\text{isomorphism classes of covering spaces of $B$}\right\}\simeq \left\{\text{transitive $\pi_1(B,x)$-sets}\right\}$$

and again, considering the skeleton category classifying transitive $\pi_1(B,x)$-sets up to isomorphism, we finally obtain the equivalence

$$\left\{\text{isomorphism classes of covering spaces of $B$}\right\}\simeq \left\{\text{conjugacy classes of subgroups of $\pi_1(B,x)$}\right\}$$

Now looking at each of these categories, they are just partially ordered sets ([\[Category Theory\] §Categories, ⁋Example 3](/en/math/category_theory/categories#ex3)), and we know that this equivalence is an isomorphism of posets. That is, we obtain the following result.

::: Corollary 12 (Fundamental theorem of covering spaces, classical version)
For a path-connected, locally path-connected, semi-locally simply connected space $B$, there exists a Galois correspondence between the set of isomorphism classes of connected covering spaces and the conjugacy classes of subgroups of $\pi_1(B)$.
:::

Explicitly, given a covering space $p:E \rightarrow B$, a subgroup is defined via $\pi_1(p):\pi_1(E)\rightarrow \pi_1(B)$, and since two transitive $G$-sets $X\cong G/H$ and $Y\cong G/K$ are isomorphic if and only if $H$ and $K$ are conjugate, we obtain the above result. On the other hand, if instead of conjugacy classes of subgroups of $\pi_1(B,x)$ we consider the subgroups themselves, this amounts to choosing one representative among isomorphic covering spaces, which is exactly the same as fixing a base point of $B$ and considering *pointed* covering maps $p:(E, y)\rightarrow (B,x)$ to view their isomorphism classes separately. That is, we have the Galois correspondence

$$\left\{\text{isomorphism classes of \textit{pointed} covering spaces of $B$}\right\}\simeq \left\{\text{subgroups of $\pi_1(B,x)$}\right\}$$

Putting this in a more familiar form, for any $H\leq \pi_1(B,x)$ we can construct the corresponding covering space $E_H$, and then for the automorphism group $\Aut(E_H/B)$ of $E_H$,

$$\Aut(E_H/B)\cong N_G(H)/H$$

holds. We call this the *Deck transformation group* of $E_H$. More generally, automorphisms of covering spaces (obtained by choosing different elements of the fiber $p^{-1}(x)$) correspond to taking inner automorphisms of subgroups of $\pi_1(B,x)$, and we call these *Deck transformations*.

On the other hand, in the poset of subgroups (or their conjugacy classes) of $\pi_1(B,x)$, there exists a minimal element $\left\{e\right\}$. Then by the above Galois correspondence, there corresponds to this a *universal cover* $\widetilde{B}$. The Deck transformation group of this covering space is isomorphic to $\pi_1(B,x)$, and $\widetilde{B}$ is simply connected.

## Seifert-van Kampen Theorem

For nice spaces that we know, we can sometimes compute the fundamental group or homology from the definition, but in most cases computing from the definition is excessively complicated or nearly impossible. Our idea is to represent a large space by smaller spaces in order to compute its fundamental group.

The simplest such method is the case where a space $X$ is expressed as the union of two open sets $X=U\cup V$. Then by [\[Topology\] §Presheaves, ⁋Lemma 1](/en/math/topology/presheaves#lem1), we know that the following diagram

![union_as_colimit](/assets/images/Math/Algebraic_Topology/Covering_Spaces-3.svg){:style="width:7.54em" class="invert" .align-center}

is a colimit diagram. In this case, our goal is to represent $\Pi_1(X)$ using $\Pi_1(U)$, $\Pi_1(V)$, and $\Pi_1(U\cap V)$ by applying the fundamental groupoid functor $\Pi_1$ to this diagram. On the other hand, [\[Topology\] §Presheaves, ⁋Lemma 1](/en/math/topology/presheaves#lem1) tells us that for any open covering $(U_i)$, the following diagram

![general_union_colimit](/assets/images/Math/Algebraic_Topology/Covering_Spaces-4.svg){:style="width:8.27em" class="invert" .align-center}

is a colimit diagram. Our claim is that if the fundamental groupoids of $(U_i)$ and their finite intersections are all known, then we can compute the fundamental groupoid of $\Pi_1(X)$ from them.

::: Theorem 13 (Seifert-van Kampen)
Given a path-connected open cover $\mathcal{O}=(U_i)$ of a topological space $X$, assume that the finite intersections of elements of $\mathcal{O}$ again belong to $\mathcal{O}$. Then the colimit of the $\mathcal{O}$-shaped diagram $\Pi_1:\mathcal{O}\rightarrow\Grpd$ exists and is isomorphic to $\Pi_1(X)$.
:::
::: Proof
That is, for any groupoid $\mathscr{G}\in\Grpd$ and any cocone $\lambda:\Pi_1\vert_\mathcal{O}\Rightarrow \mathscr{G}$, we must show that there exists a $\widetilde{\lambda}$ that agrees with $\lambda$ on each $U\in \mathcal{O}$. Of course, for any $x\in X$, we find a $U$ satisfying $x\in U$ and then define $\widetilde{\lambda}(x)$ to be this value $\lambda_U(x)$, since $\lambda_U$ is defined there. That this is independent of the choice of $U$ is obvious from the fact that for any $U_1,U_2$ containing $x$, $\lambda_{U_1}(x)$ and $\lambda_{U_2}(x)$ must both have the same value as $\lambda_{U_1\cap U_2}(x)$. For morphisms, we can define them similarly: for any path $f$ completely contained in some $U\in \mathcal{O}$, this definition is well-defined for the same reason as above, and what we need to show uniquely is how to define it when the path does not belong to a single $U\in \mathcal{O}$. But in this case, we just use path concatenation. We need to show that this is always defined and well-defined.
:::

Now, just as when we obtained [Corollary 12](#cor12) above, applying this theorem to a single object and thus replacing $\Grpd$ with $\Grp$, and using that the colimit in $\Grp$ is the free product, we obtain the following result.

::: Corollary 14 (Seifert-van Kampen theorem, classical version)
Suppose a topological space $X$ is the union of two connected open subsets $U,V$, and $U\cap V$ is connected. Then the following diagram

![van_Kampen](/assets/images/Math/Algebraic_Topology/Covering_Spaces-5.svg){:style="width:18.89em" class="invert" .align-center}

is a pushout diagram, and the resulting map $\pi_1(U)\ast_{\pi_1(U\cap V)}\pi_1(V)\rightarrow \pi_1(X)$ is an isomorphism.
:::

---

**References**

[Hat] A. Hatcher, *Algebraic Topology*. Cambridge University Press, 2022.  
[May] J. P. May, *A concise course in algebraic topology*.  
[Mun] James Munkres, *Topology*. Prentice Hall, 2000.  
[Tao] Terence Tao, [van Kampen's theorem via covering spaces](https://terrytao.wordpress.com/2012/10/28/van-kampens-theorem-via-covering-spaces/).

---
