---
title: "Locally Compact Spaces and One-Point Compactification"
description: "We define locally compact spaces and their properties, construct the one-point compactification and establish its universality, and show that every LCH space is completely regular."
excerpt: "Locally compact Hausdorff spaces, one-point compactification, and complete regularity"

categories: [Math / Topology]
permalink: /en/math/topology/locally_compact_spaces
sidebar:
    nav: "topology-en"

date: 2024-12-15
weight: 16
---

## Locally Compact Spaces

Compactness is among the strongest properties a topological space can have, yet many spaces we actually deal with are not compact. Euclidean space $\mathbb{R}^n$ is not compact because it is unbounded, and topological manifolds, which we will discuss later, also only resemble Euclidean space locally and need not be compact globally. Nevertheless, these spaces behave like compact spaces in a neighborhood of each point. We extract this local property so that we can revive compact-space arguments locally even when global compactness is absent. Furthermore, we will see that adding just a single point to such a space yields a compact space.

We formalize this local condition of compactness around each point as follows.

::: Definition 1
A topological space $X$ is *locally compact* at a point $x\in X$ if there exists a compact neighborhood of $x$ in $X$. When $X$ is locally compact at every point, we call $X$ a *locally compact space*. A space that is locally compact and Hausdorff is abbreviated as an *LCH space*.
:::

Here, a neighborhood of $x$ means a subset containing an open set that contains $x$, so a compact neighborhood need not be open. For example, in $\mathbb{R}$ the closed interval $[-1,1]$ is a compact neighborhood of $0$ but is not open. Thus the definition requires only the weak form of the existence of a single compact neighborhood, but if the space is Hausdorff, this condition can be restated in a much more convenient form.

::: Proposition 2
For a point $x$ in a Hausdorff space $X$, the following two conditions are equivalent.

1. $X$ is locally compact at $x$.
2. For any open neighborhood $V$ of $x$, there exists an open set $W$ such that $x\in W$, $\cl(W)\subseteq V$, and $\cl(W)$ is compact.
:::
::: Proof
If the second condition holds, taking $V=X$ gives a compact set $\cl(W)$ containing the open set $W$ that contains $x$, which forms a compact neighborhood of $x$; thus the second condition implies the first.

Conversely, suppose $X$ is locally compact at $x$ and let an open neighborhood $V$ of $x$ be given. Take a compact neighborhood $K$ of $x$ and let $U=\interior(K)$; then $U$ is an open set containing $x$ with $U\subseteq K$. We may now replace $V$ by $V\cap U$ and assume from the outset that $V\subseteq U\subseteq K$, since obtaining the conclusion for a smaller $V$ implies it for the original $V$.

$K$ is a compact Hausdorff space and hence is regular. ([§Compact Spaces, ⁋Lemma 6](/en/math/topology/compact_spaces#lem6){: data-relation="required" }) Meanwhile $V\subseteq K$ is an open set in $X$ and thus also open in the subspace $K$, so $K\setminus V$ is a closed set in $K$ not containing $x$. Applying regularity of $K$ to the point $x$ and the closed set $K\setminus V$, we obtain two disjoint open sets $P\ni x$ and $Q\supseteq K\setminus V$ in $K$. Since $P\subseteq K\setminus Q\subseteq V$ and $K\setminus Q$ is closed in $K$, we have $\cl_K(P)\subseteq K\setminus Q\subseteq V$.

Now let $W=P\cap U$. $P$ is open in $K$ and $U$ is open in $X$ with $U\subseteq K$, so $W$ is open in $X$ and $x\in W$. Since $W\subseteq U\subseteq K$ and $K$ is closed in $X$ ([§Compact Spaces, ⁋Corollary 5](/en/math/topology/compact_spaces#cor5){: data-relation="required" }), we have $\cl(W)\subseteq K$. Therefore $\cl(W)=\cl(W)\cap K=\cl_K(W)\subseteq\cl_K(P)\subseteq V$. Finally, $\cl(W)$ is a closed subset of the compact set $K$ and hence is compact. ([§Compact Spaces, ⁋Lemma 3](/en/math/topology/compact_spaces#lem3){: data-relation="required" }) Thus the second condition holds.
:::

The second condition of [Proposition 2](#prop2){: data-relation="required" } can be read as saying that in an LCH space, each point has a neighborhood basis consisting of open sets with compact closure. This will be used repeatedly whenever we unfold local arguments, and it also plays a key role in determining the Hausdorff property of the one-point compactification. Moreover, from this property it follows immediately that any LCH space is regular: given a point $x$ and a closed set $C$ not containing $x$, applying the second condition to $V=X\setminus C$ yields $W$ and $X\setminus\cl(W)$ separating $x$ and $C$.

The most basic example is that Euclidean space $\mathbb{R}^n$ is LCH. For any point $x$, the closed ball $\{y:\lVert y-x\rVert\leq 1\}$ is compact by the Heine–Borel theorem and contains the open ball, so it forms a compact neighborhood of $x$, and we already know that $\mathbb{R}^n$ is Hausdorff. Similarly, any discrete space is also LCH, since for each point $x$ the singleton $\{x\}$ is an open finite set and hence a compact neighborhood, and a discrete space is Hausdorff. A slightly less obvious example is a topological manifold.

::: Example 3
A Hausdorff space in which each point has an open neighborhood homeomorphic to an open subset of $\mathbb{R}^n$ is an LCH space. A topological manifold, which we will define later, is precisely such a space. Indeed, for each point $x$ of such a space $M$, take an open neighborhood $U$ homeomorphic to an open subset of $\mathbb{R}^n$; then since the point corresponding to $x$ under this homeomorphism has a compact neighborhood in $\mathbb{R}^n$ (because $\mathbb{R}^n$ is LCH), pulling this back to $U$ gives a compact neighborhood of $x$.
:::

The condition of being locally compact may appear very weak at first glance, but it is by no means automatic. The following is a representative example of a space that is not locally compact.

::: Example 4
The rational number space $\mathbb{Q}$ is not locally compact at any point as a subspace of $\mathbb{R}$. By symmetry, it suffices to show this at $0$. Suppose for contradiction that there exists a compact neighborhood $K\subseteq\mathbb{Q}$ of $0$. Then $K$ contains an open set containing $0$, so for some $\delta>0$ we have $\mathbb{Q}\cap(-\delta,\delta)\subseteq K$, and fixing $0<r<\delta$ we have $\mathbb{Q}\cap[-r,r]\subseteq K$.

Compactness is an intrinsic property independent of the ambient space in which a subspace sits, so $K$ is also compact as a subspace of $\mathbb{R}$, and since $\mathbb{R}$ is Hausdorff, $K$ is closed in $\mathbb{R}$. ([§Compact Spaces, ⁋Corollary 5](/en/math/topology/compact_spaces#cor5){: data-relation="required" }) However, the closure of $\mathbb{Q}\cap[-r,r]$ in $\mathbb{R}$ is the entire interval $[-r,r]$, so since $K$ is closed and contains $\mathbb{Q}\cap[-r,r]$, we obtain $[-r,r]\subseteq K$. This contradicts the fact that $K\subseteq\mathbb{Q}$ while $[-r,r]$ contains irrational numbers.
:::

Local compactness is inherited by suitable subspaces, but not by arbitrary subspaces, only by those that are open or closed.

::: Proposition 5
Open subspaces and closed subspaces of an LCH space are both LCH spaces.
:::
::: Proof
Since subspaces of a Hausdorff space are again Hausdorff, we only need to verify local compactness.

First, let $A\subseteq X$ be an open set and let $x\in A$ be given. Since $A$ is an open neighborhood of $x$ in $X$, by the second condition of [Proposition 2](#prop2){: data-relation="required" } there exists an open set $W$ in $X$ such that $x\in W$ and $\cl_X(W)\subseteq A$ with $\cl_X(W)$ compact. Since $\cl_X(W)\subseteq A$, the closure $\cl_A(W)$ in $A$ equals $\cl_X(W)$, which is compact and contains the open set $W$ in $A$; thus it is a compact neighborhood of $x$ in $A$.

Now let $A\subseteq X$ be a closed set and let $x\in A$ be given. Take a compact neighborhood $K$ of $x$ in $X$ and choose an open set $U\subseteq K$ in $X$ containing $x$. Then $K\cap A$ is a closed subset of the compact set $K$ and hence is compact ([§Compact Spaces, ⁋Lemma 3](/en/math/topology/compact_spaces#lem3){: data-relation="required" }), and $U\cap A$ is an open set in $A$ containing $x$ and contained in $K\cap A$; thus $K\cap A$ is a compact neighborhood of $x$ in $A$.
:::

## Construction of the One-Point Compactification

The most economical way to make a non-compact space compact is to fill in the missing part with a single point. Intuitively, this is like gathering all points escaping to both ends of $\mathbb{R}$ into a single point at infinity to form a circle. We explicitly formalize this compactification for an arbitrary topological space, show that it yields a compact space, and then determine when this construction yields a Hausdorff space.

::: Definition 6
Let a topological space $X$ be given. Write a new point not belonging to $X$ as $\infty$ and consider the set $X^+=X\cup\{\infty\}$. Among the subsets of $X^+$, we declare the following two kinds to be open: first, open sets $U$ of $X$; second, for subsets $C$ of $X$ that are compact and closed, the sets $X^+\setminus C$. The topological space $X^+$ obtained in this way is called the *one-point compactification* of $X$, or the *Alexandroff compactification*.
:::

We must verify that this declaration actually satisfies the axioms of a topology from [§Open Sets, ⁋Definition 1](/en/math/topology/open_sets#def1){: data-relation="required" }. The empty set is an open set of $X$, so it belongs to the first kind, and the empty set is compact and closed, so $X^+=X^+\setminus\emptyset$ belongs to the second kind. For the intersection of two open sets, we distinguish three cases. The intersection of two sets of the first kind is an open set of $X$. The intersection of two sets of the second kind is $(X^+\setminus C)\cap(X^+\setminus D)=X^+\setminus(C\cup D)$, and since $C\cup D$ is a compact closed set, it again belongs to the second kind. The intersection of different kinds is $U\cap(X^+\setminus C)=U\cap(X\setminus C)$, and since $C$ is closed, $X\setminus C$ is open, so this is an open set of $X$, that is, of the first kind. For arbitrary unions, similarly, the union of sets of the first kind is open, the union of sets of the second kind $\bigcup_\alpha(X^+\setminus C_\alpha)=X^+\setminus\bigcap_\alpha C_\alpha$ is of the second kind since $\bigcap_\alpha C_\alpha$ is a closed subset of some $C_\alpha$ and hence compact ([§Compact Spaces, ⁋Lemma 3](/en/math/topology/compact_spaces#lem3){: data-relation="required" }), and a mixed union is $U\cup(X^+\setminus C)=X^+\setminus(C\cap(X\setminus U))$ where $C\cap(X\setminus U)$ is a compact closed set, so it is of the second kind.

We first organize how $X$ sits inside $X^+$ under this topology.

::: Proposition 7
The inclusion map $X\hookrightarrow X^+$ is an open embedding, that is, a homeomorphism placing $X$ as an open subspace of $X^+$. Moreover, $X$ is dense in $X^+$ if and only if $X$ is not compact.
:::
::: Proof
$X$ is an open set of $X$, so it is an open set of $X^+$ by the first kind. Intersecting an open set of $X^+$ with $X$, for a set $U$ of the first kind we have $U\cap X=U$, and for a set $X^+\setminus C$ of the second kind we have $(X^+\setminus C)\cap X=X\setminus C$; both are open sets of $X$, and conversely any open set of $X$ is an open set of $X^+$ as a set of the first kind. Therefore the subspace topology on $X$ coincides with the original topology, and the inclusion map is a homeomorphism onto an open subspace.

$\{\infty\}=X^+\setminus X$ is the complement of the open set $X$, so it is closed. That $X$ is dense means $\infty\in\cl(X)$, which is equivalent to every open neighborhood of $\infty$ meeting $X$. An open set containing $\infty$ must be of the second kind $X^+\setminus C$, and this meets $X$ if and only if $X\setminus C\neq\emptyset$, that is, $C\neq X$. Therefore the necessary and sufficient condition for $X$ not to be dense is that $C=X$ for some compact closed set $C$, that is, that $X$ itself is compact.
:::

When $X$ is compact, $X$ itself is compact and closed, so $\{\infty\}=X^+\setminus X$ becomes an open set and $\infty$ is an isolated point. In this case $X^+$ is nothing more than $X$ with an isolated point attached, which is not interesting. The one-point compactification plays its intended role when $X$ is not compact; in this case $\infty$ serves as the limit point of all directions escaping outside $X$.

::: Theorem 8
For any topological space $X$, $X^+$ is compact.
:::
::: Proof
Let an arbitrary open covering $(O_i)_{i\in I}$ of $X^+$ be given. There exists at least one open set $O_j$ covering $\infty$, which must be of the second kind, so we can write $O_j=X^+\setminus C$ for a compact closed subset $C$ of $X$. The remaining $(O_i)_{i\neq j}$ must cover $C\subseteq X^+\setminus O_j$, and each $O_i\cap X$ is an open set of $X$, so $(O_i\cap X)_{i\neq j}$ is an open covering of $C$ in $X$. Since $C$ is compact, we can choose a finite $J\subseteq I\setminus\{j\}$ such that $C\subseteq\bigcup_{i\in J}(O_i\cap X)\subseteq\bigcup_{i\in J}O_i$. ([§Compact Spaces, ⁋Proposition 2](/en/math/topology/compact_spaces#prop2){: data-relation="required" }) Then $(O_i)_{i\in J\cup\{j\}}$ is a finite subcover of $X^+$.
:::

## Hausdorff Criterion and Universality

The one-point compactification yields a compact space for any space, but whether the result is again Hausdorff is a separate problem. For example, $\mathbb{Q}^+$ is compact but not Hausdorff. The following theorem reveals that the condition for $X^+$ to be Hausdorff is exactly the local compactness defined above.

::: Theorem 9
For a topological space $X$, $X^+$ is a Hausdorff space if and only if $X$ is an LCH space.
:::
::: Proof
First, suppose $X^+$ is Hausdorff. The subspace $X$ is Hausdorff since it is a subspace of a Hausdorff space. To show local compactness, fix $x\in X$; by the Hausdorff property of $X^+$ there exist disjoint open sets $U\ni x$ and $W\ni\infty$ separating $x$ and $\infty$. Since $W$ contains $\infty$, it is of the second kind, and thus $W=X^+\setminus C$ for a compact closed subset $C$ of $X$. From $U\cap W=\emptyset$ we have $U\subseteq C$, and $U$ does not contain $\infty$ so it is an open set contained in $X$. Therefore $C$ is a compact set containing the open set $U$ that contains $x$, that is, a compact neighborhood of $x$, and $X$ is locally compact at $x$.

Conversely, suppose $X$ is LCH. We must separate two distinct points of $X^+$. If both points lie in $X$, then since $X$ is Hausdorff we obtain disjoint open sets separating them in $X$, and these are also open in $X^+$ as sets of the first kind. The remaining case is when one point is $x\in X$ and the other is $\infty$. Since $X$ is Hausdorff, by [Proposition 2](#prop2){: data-relation="required" } there exists an open neighborhood $U$ of $x$ such that $K=\cl(U)$ is compact. Since $X$ is Hausdorff, $K$ is closed ([§Compact Spaces, ⁋Corollary 5](/en/math/topology/compact_spaces#cor5){: data-relation="required" }), and therefore $X^+\setminus K$ is an open set of the second kind containing $\infty$. Since $U\subseteq K$, the sets $U$ and $X^+\setminus K$ are disjoint and separate $x$ and $\infty$.
:::

Combining [Theorem 8](#thm8){: data-relation="required" } and [Theorem 9](#thm9){: data-relation="required" }, when $X$ is an LCH space, $X^+$ becomes a compact Hausdorff space and by [Proposition 7](#prop7){: data-relation="required" } $X$ is embedded in it as an open subspace. In particular, if $X$ is not compact, this embedding is dense. This is the existence part of Alexandroff's theorem: any LCH space can be embedded as a dense open subspace of some compact Hausdorff space. What remains is that such a compactification is essentially unique, which is formalized by the following universality property.

::: Theorem 10
Let an LCH space $X$ be given. If a compact Hausdorff space $Y$, a point $p\in Y$, and a homeomorphism $\varphi:X\rightarrow Y\setminus\{p\}$ are given, then there exists a unique homeomorphism $h:X^+\rightarrow Y$ such that $h=\varphi$ on $X$ and $h(\infty)=p$.
:::
::: Proof
Identifying $X$ and $Y\setminus\{p\}$ via $\varphi$, we regard $X$ as a subset of $Y$. Since $Y$ is Hausdorff, $\{p\}$ is a closed set of $Y$, and therefore $X=Y\setminus\{p\}$ is an open subspace of $Y$. That is, the topology of $X$ coincides with the subspace topology induced from $Y$.

We now show that the open sets of $Y$ correspond exactly to the open sets of $X^+$. If an open set $O$ of $Y$ does not contain $p$, then $O\subseteq X$ and since $X$ is an open subspace of $Y$, $O$ is an open set of $X$, that is, of the first kind. Conversely, an open set of $X$ is open in $Y$ since $X$ is open in $Y$. On the other hand, if an open set $O$ of $Y$ contains $p$, then $Y\setminus O$ is a closed subset of the compact space $Y$ and hence is compact ([§Compact Spaces, ⁋Lemma 3](/en/math/topology/compact_spaces#lem3){: data-relation="required" }), and $Y\setminus O\subseteq X$ and is closed in $Y$ so also closed in $X$. Therefore $O=X^+\setminus(Y\setminus O)$ is the complement of a compact closed subset of $X$, that is, of the second kind. Conversely, for a compact closed subset $C$ of $X$, since $C$ is also compact in $Y$ and $Y$ is Hausdorff, it is closed ([§Compact Spaces, ⁋Corollary 5](/en/math/topology/compact_spaces#cor5){: data-relation="required" }), so $Y\setminus C$ is an open set of $Y$ containing $p$.

Therefore the correspondence $h:X^+\rightarrow Y$ identifying $p$ with $\infty$ sends open sets to open sets and vice versa, bijectively, and hence is a homeomorphism. Since $h$ must agree with $\varphi$ on $X$ and send $\infty$ to $p$, it is unique.
:::

[Theorem 10](#thm10){: data-relation="weak" } says that for an LCH space $X$, there is only one way to add a point to make a compact Hausdorff space, up to homeomorphism. This is the uniqueness part of Alexandroff's theorem expressed in the language of universality. Thanks to this uniqueness, we can treat $X^+$ independently of its concrete construction, and in actual calculations we may choose any convenient compact Hausdorff model and identify it with $X^+$.

{% diagram Math/Topology/Locally_Compact_Spaces-1.svg width="6.23em" alt="Universality of the one-point compactification" %}

::: Remark 11
The one-point compactification is characterized as the smallest among Hausdorff compactifications. A *Hausdorff compactification* of a non-compact LCH space $X$ is a compact Hausdorff space containing $X$ as a dense subspace; from any such compactification, collapsing all points outside $X$ into a single point yields a unique continuous surjection onto $X^+$. The proof of this fact requires the observation that if an LCH space is densely embedded in a Hausdorff space, it is always an open subspace; the detailed argument follows standard literature. **[Mun]** At the opposite extreme is the *Stone–Čech compactification*, the largest Hausdorff compactification that a completely regular space can have, but this requires a separate construction so we only mention its name here.
:::

## Examples of One-Point Compactifications

The most familiar example is that the one-point compactification of Euclidean space becomes a sphere.

::: Example 12
Consider the north pole $N=(0,\ldots,0,1)$ of the $n$-sphere $S^n=\{x\in\mathbb{R}^{n+1}:\lVert x\rVert=1\}$. The stereographic projection

$$\sigma:S^n\setminus\{N\}\rightarrow\mathbb{R}^n,\qquad \sigma(x_1,\ldots,x_{n+1})=\frac{1}{1-x_{n+1}}(x_1,\ldots,x_n)$$

is well known to be a homeomorphism between $S^n\setminus\{N\}$ and $\mathbb{R}^n$. Since $S^n$ is a closed bounded subset of $\mathbb{R}^{n+1}$, it is compact by the Heine–Borel theorem, and it is Hausdorff as a subspace. Therefore $S^n$ is a compact Hausdorff space, and removing the single point $N$ yields a space homeomorphic to $\mathbb{R}^n$; thus by [Theorem 10](#thm10){: data-relation="required" } there is a unique homeomorphism

$$(\mathbb{R}^n)^+\cong S^n$$

and the point at infinity $\infty$ corresponds to the north pole $N$. In particular, $(\mathbb{R})^+$ is the circle $S^1$.
:::

The one-point compactification of a discrete space gives a very concrete picture of a convergent sequence.

::: Example 13
Endow the set of natural numbers $\mathbb{N}=\{1,2,3,\ldots\}$ with the discrete topology. This is LCH as a discrete space, so by [Theorem 9](#thm9){: data-relation="required" } $\mathbb{N}^+$ is a compact Hausdorff space. In a discrete space, the only compact subsets are finite sets, so an open neighborhood of $\infty$ in $\mathbb{N}^+$ is the complement of a finite set, that is, a cofinite set containing $\infty$. This means precisely that a sequence in $\mathbb{N}$ converges to $\infty$ if and only if it eventually leaves any finite set.

This space is realized by a familiar subset of the real numbers. Consider the function

$$f:\mathbb{N}^+\rightarrow\mathbb{R},\qquad f(n)=\frac1n\quad(n\in\mathbb{N}),\qquad f(\infty)=0$$

Then $f$ is a bijection between $\mathbb{N}^+$ and $\{0\}\cup\{1/n\mid n\geq 1\}$. Each $n\in\mathbb{N}$ is an isolated point in $\mathbb{N}^+$ and its image $1/n$ is also an isolated point in $\{0\}\cup\{1/n\}$, and since the cofinite neighborhoods of $\infty$ map to neighborhoods of $0$, $f$ is continuous. Since the domain is compact and the codomain is Hausdorff, by [§Compact Spaces, ⁋Proposition 9](/en/math/topology/compact_spaces#prop9){: data-relation="required" } $f$ is a homeomorphism. That is, $\mathbb{N}^+$ is homeomorphic to a convergent sequence with one limit point.
:::

## Complete Regularity

The one-point compactification is not merely an existential tool; it is also used to characterize intrinsic properties of LCH spaces. A compact Hausdorff space is normal, so ([§Compact Spaces, ⁋Proposition 7](/en/math/topology/compact_spaces#prop7){: data-relation="required" }) it has abundant continuous functions via Urysohn's lemma, and we show that this property is inherited by LCH spaces through open subspaces.

::: Corollary 14
Any LCH space is completely regular. Therefore any LCH space is a Tychonoff space. ([§Hausdorff Spaces, ⁋Definition 3](/en/math/topology/Hausdorff_spaces#def3){: data-relation="weak" })
:::
::: Proof
We first show that any compact Hausdorff space $Y$ is completely regular. Let a point $p\in Y$ and a closed set $C\subseteq Y$ not containing $p$ be given. Since $Y$ is Hausdorff, it is $T_1$ and thus $\{p\}$ is a closed set; $\{p\}$ and $C$ are two disjoint closed sets. Since $Y$ is normal, ([§Compact Spaces, ⁋Proposition 7](/en/math/topology/compact_spaces#prop7){: data-relation="required" }) by Urysohn's lemma there exists a continuous function $g:Y\rightarrow[0,1]$ taking the value $0$ on $\{p\}$ and $1$ on $C$. ([§Urysohn's Lemma and Tietze Extension Theorem, ⁋Theorem 2](/en/math/topology/urysohn_and_tietze#thm2)) This means precisely that $p$ and $C$ can be separated by a continuous function, so $Y$ is completely regular.

Now let $X$ be LCH. By [Theorem 8](#thm8){: data-relation="required" } and [Theorem 9](#thm9){: data-relation="required" }, $X^+$ is a compact Hausdorff space and hence completely regular as shown above. By [Proposition 7](#prop7){: data-relation="required" }, $X$ is a subspace of $X^+$. We show that complete regularity is inherited by subspaces. Let $x\in X$ and a closed set $C$ of $X$ not containing $x$ be given; by the property of closed sets in a subspace, there exists a closed set $C'$ of $X^+$ such that $C=C'\cap X$. Since $x\in X$ and $x\notin C$, we have $x\notin C'$, and since $X^+$ is completely regular, there exists a continuous function $g:X^+\rightarrow[0,1]$ such that $g(x)=0$ and $g$ takes the value $1$ on $C'$. The restriction $g\vert_X$ to $X$ is a continuous function separating $x$ and $C\subseteq C'$, so $X$ is completely regular. Finally, $X$ is Hausdorff and hence $T_0$, so $X$ is a Tychonoff space.
:::

[Corollary 14](#cor14){: data-relation="weak" } guarantees that on an LCH space, we can always obtain a continuous function separating two distinct points or a point and a closed set. This is a fundamental fact indicating how well-behaved locally compact spaces are as analytic objects, and it serves as the starting point for various constructions that patch together locally defined data into global ones using continuous functions.

---

**References**

**[Mun]** J. R. Munkres, *Topology*, 2nd ed., Prentice Hall, 2000.

**[Wil]** S. Willard, *General Topology*, Addison-Wesley, 1970.

**[Kel]** J. L. Kelley, *General Topology*, Springer, 1975.

