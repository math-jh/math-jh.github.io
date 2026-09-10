---
title: "Dimension"
description: "We define the dimension of a topological space using the order of open coverings. We also discuss the covering dimension of compact spaces and the properties of finite-dimensional topological spaces."
excerpt: "Definitions of covering dimension and Krull dimension for algebraic geometry"

categories: [Math / Topology]
permalink: /en/math/topology/dimension
sidebar: 
    nav: "topology-en"

date: 2024-12-15
weight: 21
translated_at: 2026-09-06T23:15:05+00:00
translation_source: antigravity-gemini-3.8-flash-high
---
In this post, we define the dimension of a topological space. First, we define the dimension commonly used, and then separately define the notion of dimension to be used in [Algebraic Varieties](/en/algebraic_varieties/). 

## Covering dimension

For convenience, following **[Mun]**, in this section we define the dimension of compact spaces only. The basic idea is to measure how many times points of $X$ are covered by open sets. Of course, since $X$ is covered by the single open set $X$ itself, this should be defined using arbitrary open coverings; furthermore, since an arbitrary open covering can cover a single point with as many open sets as desired, we must guarantee some kind of minimality. 

First, we define the following.

::: Definition 1
A family of subsets of $X$, $(U_i)_{i\in I}$, is said to have *order* $m+1$ if no point of $X$ belongs to more than $m+1$ sets $U_i$, and some point of $X$ belongs to exactly $m+1$ sets $U_i$.
:::

Then we can define the dimension of a space $X$ as follows. 

::: Definition 2
A space $X$ is said to be *finite dimensional* if there exists $m$ such that whenever an open covering $(U_i)_{i\in I}$ is given, an open refinement of order at most $m+1$ of $(U_i)$, $(V_j)_{j\in J}$, always exists. The smallest $m$ for which this is possible is defined as the *dimension* of $X$ and is denoted by $\dim X$. 
:::

It is worth noting that a topological space can look quite strange, as in the following figure, and in this case we have defined the dimension of this topological space to be the larger of the dimensions of the two components.

img

Meanwhile, there are several properties we might expect of dimension, some of which are as follows. 

::: Proposition 3
If $X$ is a finite-dimensional topological space and $Y$ is a closed subspace of $X$, then $Y$ is also finite-dimensional and $\dim Y\leq\dim X$.
:::
::: Proof
Let $X$ be a $d$-dimensional topological space, and let an arbitrary open covering of $Y$, $\{V_j\}$, be given. Then for each $V_j$, we have $V_j=U_j\cap Y$ for an open subset of $X$, $U_j$. Now $X$ can be covered by the $U_j$ and $X\setminus Y$. Then there exists a refinement of this covering of order $\leq d+1$, and intersecting this with $Y$ yields a refinement of $\{V_j\}$ of order $\leq d+1$. 
:::

The following proposition refines the remark mentioned after [Definition 2](#def2){: data-relation="required" } more mathematically.

::: Proposition 4
If for a compact space $X$, there exist two finite-dimensional closed subspaces $Y,Z$ such that $X=Y\cup Z$, then $\dim X=\max(\dim Y,\dim Z)$. 
:::
::: Proof
Since $Y,Z$ are closed subspaces, by [Proposition 3](#prop3){: data-relation="required" } we have $\max(\dim Y,\dim Z)\leq \dim X$. Therefore, setting $m=\max(\dim Y,\dim Z)$, it suffices to show that $\dim X\leq m$.

First, observe the following. If a topological space $T$ satisfies $\dim T\leq m$ and a finite open covering of $T$, $(V_1,\ldots,V_k)$, is given, then with each $i$ satisfying $W_i\subseteq V_i$, there exists an open covering of order at most $m+1$, $(W_1,\ldots,W_k)$. Here, some $W_i$ may be empty. Indeed, by the definition of dimension, there exists an open refinement of $(V_i)$ of order $\leq m+1$, $(O_j)_{j\in J}$; for each $j$, to satisfy $O_j\subseteq V_{i(j)}$ we pick an index $i(j)$, and then define

$$W_i=\bigcup_{i(j)=i}O_j$$

It is clear that $(W_i)$ is an open covering that is a shrinking of $(V_i)$, and if a point $x$ belongs to distinct $W_{i_1},\ldots,W_{i_r}$, then $x$ must, for indices satisfying $i(j_1)=i_1,\ldots,i(j_r)=i_r$, belong to distinct $O_{j_1},\ldots,O_{j_r}$, which implies $r\leq m+1$.

Now let an arbitrary open covering of $X$ be given. Since $X$ is compact, we can choose a finite subcovering $(U_1,\ldots,U_k)$, and it suffices to find an open refinement of this covering of order $\leq m+1$.

As a first step, let us handle $Y$. Since $(U_i\cap Y)$ is a finite open covering of $Y$ and $\dim Y\leq m$, by the above observation there exist, with $B_i\subseteq U_i\cap Y$ and of order $\leq m+1$, sets covering $Y$ that are open in $Y$, $(B_i)$. For each $i$, satisfying $\tilde{B}_i\cap Y=B_i$, choose an open subset of $X$, $\tilde{B}_i$; intersecting with $U_i$ if necessary, we may assume that $\tilde{B}_i\subseteq U_i$. Now, if we define

$$W_i=\tilde{B}_i\cup (U_i\setminus Y)$$

then since $Y$ is a closed set, the $W_i$ are open sets and $W_i\subseteq U_i$. Since points of $Y$ belong to some $B_i$ and points outside $Y$ belong to some $U_i\setminus Y$, $(W_i)$ is an open covering of $X$. Finally, for $y\in Y$, since $W_i\cap Y=\tilde{B}_i\cap Y=B_i$, the number of sets with $y$ belonging to $W_i$ is equal to the number of sets with $y$ belonging to $B_i$, which is at most $m+1$.

As a second step, apply the same construction to $Z$ and the covering $(W_i)$. That is, applying the above observation to $(W_i\cap Z)$, we obtain, with $C_i\subseteq W_i\cap Z$ and of order $\leq m+1$, sets covering $Z$ that are open in $Z$, $(C_i)$; after choosing, so that $\tilde{C}_i\subseteq W_i$ and $\tilde{C}_i\cap Z=C_i$, open sets of $X$, $\tilde{C}_i$, we define

$$V_i=\tilde{C}_i\cup(W_i\setminus Z)$$

Then, as in the first step, $(V_i)$ is an open covering of $X$ and $V_i\subseteq W_i\subseteq U_i$, and points of $Z$ belong to at most $m+1$ of the sets $V_i$. Meanwhile, for a point $y$ of $Y$, whenever $y\in V_i$ we have $y\in W_i$, so the number of sets with $y$ belonging to $V_i$ is at most the number of sets $W_i$ controlled in the first step, that is, at most $m+1$. Since $X=Y\cup Z$, $(V_i)$ is an open refinement of the given covering of order $\leq m+1$, and therefore $\dim X\leq m$.
:::

And of course, we would hope that the dimension of $\mathbb{R}^n$ is $n$. However, showing this is not easy, basically because at present it is difficult for us even to show that $\mathbb{R}^n$ and $\mathbb{R}^m$ are not homeomorphic. Instead, the following weaker proposition can be easily shown from the definition.

::: Proposition 5
Any compact subspace of $\mathbb{R}^n$ is always at most $n$-dimensional.
:::
::: Proof
Let $A\subseteq\mathbb{R}^n$ be a compact subspace, and let an arbitrary open covering of $A$ be given. By compactness, we can choose a finite subcovering $(U_1,\ldots,U_k)$.

First, let us show that there exists $\delta>0$ such that any subset of diameter less than $\delta$ in $A$ is contained in some $U_i$. For each $x\in A$, to have $x\in U_{i(x)}$, choose an index $i(x)$, and in $A$, so that the open ball satisfies $B(x,2r_x)\subseteq U_{i(x)}$, choose $r_x>0$. Then $(B(x,r_x))_{x\in A}$ is an open covering of $A$, so finitely many balls $B(x_1,r_{x_1}),\ldots,B(x_l,r_{x_l})$ cover $A$, and we may set $\delta=\min(r_{x_1},\ldots,r_{x_l})$. Indeed, if for a set of diameter $<\delta$, say $S$, a point $y$ belongs to $B(x_j,r_{x_j})$, then by the triangle inequality, $S\subseteq B(x_j,2r_{x_j})\subseteq U_{i(x_j)}$.

Now, we construct an open covering of the whole $\mathbb{R}^n$ with order at most $n+1$ and the diameter of every element bounded by a fixed constant. Consider the unit grid with vertices at the integer points. Here, a *face* refers to a Cartesian product where each component is either a unit interval $[k_i,k_i+1]$ or a single point $\{k_i\}$ ($k_i\in\mathbb{Z}$), and the dimension of a face is the number of components where an interval is used. Let the collection of $d$-dimensional faces be denoted by $\mathcal{F}_d$, and let the union of faces of dimension at most $d$ be $\sk_d$. Then $\sk_n=\mathbb{R}^n$. For each $d=0,1,\ldots,n$, we set $r_d=8^{-(d+1)}$, and for each $F\in\mathcal{F}_d$,

$$U_F=\left\{x\in\mathbb{R}^n\middle\vert \operatorname{dist}(x,F)<2r_d,\quad \operatorname{dist}(x,\sk_{d-1})>r_{d-1}\right\}$$

we define as above. When $d=0$, the second condition is omitted. Since the distance functions are continuous, the sets $U_F$ are open.

Let us show that these cover $\mathbb{R}^n$. For any $x$, among indices satisfying $\operatorname{dist}(x,\sk_d)\leq r_d$, choose the smallest $d$. Since $\operatorname{dist}(x,\sk_n)=0\leq r_n$, such a $d$ exists. Then by the minimality of $d$, when $d>0$ we have $\operatorname{dist}(x,\sk_{d-1})>r_{d-1}$, and since $\operatorname{dist}(x,\sk_d)\leq r_d<2r_d$, we have $\operatorname{dist}(x,F)<2r_d$ for some $F\in\mathcal{F}_d$. That is, $x\in U_F$.

Next, for two distinct faces $F\neq F'\in\mathcal{F}_d$ of the same dimension, let us show that $U_F\cap U_{F'}=\emptyset$. If there exists $x\in U_F\cap U_{F'}$, then satisfying $\lvert x-y\rvert<2r_d$ and $\lvert x-y'\rvert<2r_d$, there exist $y\in F$ and $y'\in F'$, and in particular $\lvert y-y'\rvert<4r_d\leq 1/2$. First, $F\cap F'\neq\emptyset$, because otherwise the intervals of the two faces in some component would be disjoint, and since the distance between disjoint intervals with integer endpoints is at least $1$, this would imply $\lvert y-y'\rvert\geq 1$, a contradiction. In particular, since a contradiction is already obtained for $d=0$, let us assume $d>0$. Then $F\cap F'$ is a face given by the componentwise intersections, and if its dimension were $d$, the unit intervals of the two faces would coincide in the $d$ components where intervals are used and the two points would coincide in the remaining components, yielding $F=F'$; thus the dimension of $F\cap F'$ is at most $d-1$. That is, $F\cap F'\subseteq\sk_{d-1}$.

Now, in each component, for $y_i$, let the closest point in $F_i'$ be $z_i$. If $y_i\in F_i'$, then $z_i=y_i\in F_i\cap F_i'$; otherwise $z_i$ is an endpoint of $F_i'$, and since any point of $F_i\cap F_i'$, relative to $y_i$ and $z_i$, lies beyond $z_i$, the fact that the interval $F_i$ contains both $y_i$ and that point implies $z_i\in F_i\cap F_i'$. Also, since $y_i'\in F_i'$, we have $\lvert z_i-y_i\rvert=\operatorname{dist}(y_i,F_i')\leq\lvert y_i-y_i'\rvert$. Therefore, $z=(z_i)\in F\cap F'\subseteq \sk_{d-1}$ and $\lvert y-z\rvert\leq\lvert y-y'\rvert$, so

$$\operatorname{dist}(x,\sk_{d-1})\leq \lvert x-y\rvert+\lvert y-z\rvert\leq \lvert x-y\rvert+\lvert y-y'\rvert<2r_d+4r_d=6r_d<8r_d=r_{d-1}$$

which contradicts the second condition in $x\in U_F$.

Therefore, for each dimension $d$, each point belongs to at most one $U_F$ ($F\in\mathcal{F}_d$), and since the dimensions range from $0$ to $n$, the order of $(U_F)$ is at most $n+1$. In addition, since each $U_F$ consists of points whose distance from $F$ is less than $2r_d$, its diameter is at most $\operatorname{diam}F+4r_d\leq\sqrt{n}+1/2$.

Finally, we apply scaling. Setting $\lambda=\delta/(\sqrt{n}+1)$ and transferring the covering constructed above via the homeomorphism $x\mapsto\lambda x$, we obtain, with order $\leq n+1$ and each element having diameter $\lambda(\sqrt{n}+1/2)<\delta$, an open covering of $\mathbb{R}^n$, denoted $\mathcal{W}$. Then $(W\cap A)_{W\in\mathcal{W}}$ is an open covering of $A$, its order is still at most $n+1$, and since each element has diameter $<\delta$, it is contained in some $U_i$ by the property of the Lebesgue number found in the first step. That is, this is an open refinement of the given covering of order $\leq n+1$, and therefore $\dim A\leq n$.
:::

## Krull dimension

Meanwhile, we define the notion of dimension used in algebraic geometry; this definition is somewhat counterintuitive because the spaces of interest in algebraic geometry are endowed with topologies different from those one typically considers. In particular, $\mathbb{R}^n$ with the usual topology is always $0$-dimensional. Nevertheless, since it is true that this definition can be given in the language of topology, we record it here on this page.

::: Definition 6
A topological space $X$ is said to be *irreducible* if $X$ is nonempty, and no decomposition $X=A\cup B$ into proper closed subsets of $X$, $A,B$, exists.
:::

Then the following are all equivalent.

::: Proposition 7
For a nonempty topological space $X$, the following are all equivalent:

1. $X$ is irreducible.
2. In $X$, for any nonempty open subsets $U,V$, we have $U\cap V\neq\emptyset$.
3. In $X$, for any nonempty open subset $U$, we have $\cl U=X$.
4. Every open subset of $X$ is connected.
:::
::: Proof
The equivalence of the first and second conditions is clear by considering complements, and the equivalence of the second and third conditions is clear by considering $X\setminus \cl U$ and $U$. Finally, the second and fourth conditions are equivalent by definition.
:::

In particular, an irreducible space is not Hausdorff. Because of the last equivalence in the proposition above, an irreducible space is also called a *hyperconnected space*. In a similar vein, the following holds. (cf. [§Connected Spaces, ⁋Proposition 3](/en/math/topology/connected_spaces#prop3){: data-relation="weak" })

::: Proposition 8
Suppose that a nonempty space $X$ is a union of irreducible open subsets

$$X=\bigcup_{i\in I} U_i$$

and $U_i\cap U_j\neq \emptyset$ holds for all $i,j$. Then $X$ is irreducible.
:::
::: Proof
Suppose two open sets $V, W$ are given, and let us show that $V\cap W\neq\emptyset$. Then from the given hypothesis, first, we have $U_i\cap V\neq\emptyset$ and $U_j\cap W\neq\emptyset$ for some $i,j$. Now since $U_i$ is irreducible, the two nonempty subsets of $U_i$, namely $U_i\cap V$ and $U_i\cap U_j$, must also have a nonempty intersection. That is,

$$(U_i\cap V)\cap (U_i\cap U_j)=U_i\cap U_j\cap V\neq\emptyset$$

and viewing $U_i\cap U_j\cap V$ as a nonempty subset of $U_j$, the irreducibility of $U_j$ likewise yields

$$(U_i\cap U_j\cap V)\cap (U_j\cap W)=U_i\cap U_j\cap V\cap W\neq\emptyset$$

and in particular $V\cap W\neq\emptyset$.
:::

Similarly to connected components, we can define the following.

::: Definition 9
For a subset $A$ of a topological space $X$, an *irreducible component* containing $A$ means a maximal element with respect to inclusion among the irreducible subsets containing $A$.
:::

Given a nonempty totally ordered subset of irreducible subsets containing $A$, their union $Y$ is also irreducible, because if two nonempty open subsets of $Y$ intersect elements $Y_1, Y_2$ of this collection, respectively, and $Y_1\subseteq Y_2$, then the intersections of the two open sets with $Y_2$ are nonempty open subsets of $Y_2$, which intersect each other by the second condition of [Proposition 7](#prop7){: data-relation="required" }. Therefore, if $A$ is irreducible, the empty totally ordered subset has $A$ itself as an upper bound, and thus by [\[Set Theory\] §Axiom of Choice, ⁋Theorem 4](/en/math/set_theory/axiom_of_choice#thm4){: data-relation="required" }, there exists an irreducible component containing $A$. However, unlike connected components, there is no reason for a maximal one to be unique, so there may be multiple irreducible components containing $A$. Meanwhile, by an argument similar to [§Connected Spaces, ⁋Proposition 2](/en/math/topology/connected_spaces#prop2){: data-relation="weak" }, we can show that the closure of an irreducible set is irreducible, so an irreducible component is necessarily a closed subset.

::: Definition 10
For a topological space $X$, for a strictly descending chain of irreducible closed subsets of $X$

$$A_n\supsetneq\cdots\supsetneq A_0$$

we define its *length* to be $n$. Then we define the *Krull dimension* of $X$ by the formula

$$\dim X=\sup\{\text{length of strictly descending chains of irreducible closed subsets}\}$$

If there exists a strictly descending chain of infinite length, we define $\dim X=\infty$, and in the case where $X=\emptyset$, we define $\dim X=-\infty$.
:::

In a Hausdorff space, only singletons are irreducible subsets, so the Krull dimension of a nonempty Hausdorff space is always $0$. Meanwhile, spaces dealt with in algebraic geometry often satisfy the following finiteness condition.

::: Definition 11
A topological space $X$ is *Noetherian* if whenever a chain of arbitrary closed subsets

$$A_1\supseteq A_2\supseteq\cdots$$

is given, there exists some $n$ such that $A_n=A_{n+1}=\cdots$.
:::

This condition does not even guarantee the finiteness of the Krull dimension. For example, if we endow $X=\mathbb{N}$ with the topology whose closed sets are $\emptyset$, $X$, and the finite initial segments $\{1,\ldots,n\}$, then $n$ must decrease in any strictly descending chain of closed subsets, so $X$ is Noetherian. However, each $\{1,\ldots,n\}$ is the closure of $\{n\}$ and thus irreducible, and therefore $\{1\}\subsetneq\{1,2\}\subsetneq\cdots$ gives an arbitrarily long chain, so $\dim X=\infty$.

Also, if $X$ is Noetherian, any nonempty collection of closed subsets of $X$, say $\mathcal{S}$, has a minimal element with respect to inclusion. Indeed, otherwise, for each $A\in\mathcal{S}$, we could satisfy $A\supsetneq A'$ by choosing some $A'\in\mathcal{S}$, and repeating this would yield a descending chain of closed subsets that does not stabilize.

The Noetherian condition gives a strong finiteness property. For instance, the following holds.

::: Proposition 12
A Noetherian space is compact.
:::
::: Proof
Suppose we are given a Noetherian space $X$ and an open covering of $X$, $\{U_i\}_{i\in I}$. Then we can define

$$\mathcal{C}=\left\{\bigcup_{j\in J} U_j\mid\text{$J$ finite subset of $I$}\right\}$$

Now let any totally ordered subset of $\mathcal{C}$, say $\mathcal{D}$, be given. If $\mathcal{D}$ is empty, then corresponding to $J=\emptyset$, the element $\emptyset\in\mathcal{C}$ is an upper bound of $\mathcal{D}$; otherwise, the complements of the elements of $\mathcal{D}$ form a nonempty collection of closed subsets of $X$, and thus have a minimal element as seen above, and since $\mathcal{D}$ is totally ordered, its complement is the largest element in $\mathcal{D}$, in particular an upper bound of $\mathcal{D}$. That is, every totally ordered subset of $\mathcal{C}$ has an upper bound, so by [\[Set Theory\] §Axiom of Choice, ⁋Theorem 4](/en/math/set_theory/axiom_of_choice#thm4){: data-relation="required" }, $\mathcal{C}$ has a maximal element $U\in \mathcal{C}$. If $X\neq U$, we can pick some $x\in X\setminus U$ and take $U_j$ containing it; then $U\cup U_j$ is an element strictly containing $U$ in $\mathcal{C}$, which contradicts the maximality of $U$. Therefore $U=X$, and we obtain the desired result.
:::

Additionally, the following holds for Noetherian spaces.

::: Proposition 13
For a Noetherian topological space $X$, the following hold:

1. Any subspace of $X$ is Noetherian.
2. $X$ has finitely many irreducible components.
3. Each irreducible component of $X$ contains a nonempty open subset of $X$.
:::
::: Proof
1. For any subspace of $X$, say $Y$, suppose a descending chain of closed subsets of $Y$
    
    $$A_1\supseteq A_2\supseteq \cdots$$

    is given. Then we can write $A_i=A_i' \cap Y$ for some closed subsets of $X$, $A_i'$. Now if we set $B_i=A_1'\cap\cdots\cap A_i'$, then $B_i\cap Y=A_i$, and $B_i$ is a descending chain of closed subsets of $X$.
2. Let $\mathcal{C}$ be the collection of closed subsets of $X$ that cannot be expressed as a union of finitely many irreducible closed subsets. Then it suffices to show that $\mathcal{C}=\emptyset$. If we assume to the contrary that $\mathcal{C}$ is nonempty, by the existence of a minimal element seen above, $\mathcal{C}$ has a minimal element $A$. Since the empty set is the union of the empty collection, $A\neq\emptyset$, and if $A$ were irreducible, $A$ itself would be a union of a single element, so $A$ is not irreducible. Therefore, by [Definition 6](#def6){: data-relation="required" }, we can write $A=B_1\cup B_2$ for some proper closed subsets of $A$, $B_1,B_2$, and from the minimality of $A$, we have $B_1,B_2\not\in\mathcal{C}$, so each of these is a union of finitely many irreducible closed subsets; combining the two, $A$ is also such a union, which is a contradiction. That is, $\mathcal{C}=\emptyset$, and in particular, we have $X=A_1\cup\cdots\cup A_n$ for some irreducible closed subsets of $X$, $A_1,\ldots,A_n$. If some $A_i$ is contained in another $A_j$, we may remove it, so assuming from the beginning that there are no inclusion relations among the $A_i$, for any irreducible closed subset of $X$, $B$, the set $B=\bigcup_i (B\cap A_i)$ is a finite union of closed subsets of $B$, so repeatedly applying [Definition 6](#def6){: data-relation="required" }, we have $B\subseteq A_i$ for some $i$. Then an irreducible component of $X$ is, by [Definition 9](#def9){: data-relation="required" }, a maximal irreducible subset, and as seen earlier is a closed subset, so it is contained in some $A_i$; since $A_i$ itself is irreducible, by maximality it is equal to $A_i$. Therefore, the irreducible components of $X$ are at most $n$.
3. Choose $X=A_1\cup\cdots\cup A_n$ obtained in (2) such that there are no inclusion relations among the $A_i$. If $A_1\subseteq A_2\cup\cdots\cup A_n$, then since $A_1=\bigcup_{j\geq 2}(A_1\cap A_j)$, as above we have $A_1\subseteq A_j$ for some $j\geq 2$, contradicting the absence of inclusion relations; therefore $X\setminus (A_2\cup\cdots\cup A_n)$ is contained in $A_1$ and is a nonempty open subset of $X$. Since each irreducible component is equal to some $A_i$, the same argument can be applied to all $i$.
:::

Then, if $X$ is Noetherian, an irreducible decomposition of $X$

$$X=\bigcup_{i=1}^r X_i$$

exists, and the $X_i$ are all closed subsets. However, distinct irreducible components can intersect each other, so $X\setminus X_i$ may be smaller than $\bigcup_{j\neq i}X_j$, and thus there is no reason for $X_i$ to be an open set. Indeed, if $X_i$ is an open set and intersects another component $X_j$, then $X_i\cap X_j$ is a nonempty open subset of $X_j$, and thus by the third condition of [Proposition 7](#prop7){: data-relation="required" } it is dense in $X_j$; since $X_i$ is a closed subset, we have $X_j\subseteq X_i$, and from the maximality of $X_j$ it follows that $X_i=X_j$. That is, $X_i$ is an open set only when $X_i$ does not intersect other components.

Formulating the above fact that any nonempty collection of closed subsets always has a minimal element into an induction principle, we obtain a standard tool for proving properties of closed subsets on a Noetherian space.

::: Proposition 14 (Noetherian induction)
Suppose we are given a Noetherian topological space $X$ and, for closed subsets of $X$, a property $P$. If for any closed subset $Z\subseteq X$, whenever every proper closed subset $Z'\subsetneq Z$ satisfies $P(Z')$, $P(Z)$ also holds, then $P$ holds for all closed subsets of $X$.
:::
::: Proof
Let the family of closed subsets for which $P$ does not hold be $\mathcal{S}$, and suppose for the sake of contradiction that $\mathcal{S}\neq\emptyset$. As seen above, $\mathcal{S}$ has a minimal element $Z_0$. Then, since $Z_0$ is minimal, any proper closed subset $Z'\subsetneq Z_0$ does not belong to $\mathcal{S}$, so $P(Z')$ holds, and therefore by hypothesis $P(Z_0)$ holds. This contradicts $Z_0\in\mathcal{S}$, so $\mathcal{S}=\emptyset$, which means that $P$ holds for all closed subsets of $X$.
:::

This is a topological analogue of strong induction for the natural numbers, where the Noetherian condition, that closed subsets satisfy the descending chain condition, makes the induction possible. In practice, for any closed subset $Z$, we assume that the property holds for its proper closed subsets and show that it holds for $Z$; in particular, the case $Z=X$ is included in the conclusion.

::: Proposition 15
For a topological space $X$ and an open subset $U$, there is a one-to-one correspondence between the subsets meeting $U$ among the irreducible closed subsets of $X$ and the irreducible closed subsets of $U$.
:::
::: Proof
First, assuming $U\cap Z\neq\emptyset$ for an irreducible subspace of $X$, say $Z$, we must show that any two nonempty open subsets of $Z\cap U$ are not disjoint. Since for any open subsets of $Z\cap U$, there exist open subsets of $Z$, say $V_1, V_2$, such that they are of the form $V_1\cap U$, $V_2\cap U$, from the equation

$$(V_1\cap U)\cap (V_2\cap U)=(V_1\cap V_2)\cap U$$

if $(V_1\cap U)\cap(V_2\cap U)\neq\emptyset$, then $V_1\cap V_2\neq\emptyset$, which contradicts the assumption that $Z$ is irreducible. 

Conversely, given in $U$ an irreducible closed subset $Y\subseteq U$, the closure of $Y$ is also irreducible, so that in $X$, the irreducible $\cl_X(Y)$ is a subset meeting $U$ among the irreducible subsets of $X$. Thus, from this we obtain two maps

$$\{\text{irreducible closed subset of $X$ meeting $U$}\}\rightarrow \{\text{irreducible closed subset of $U$}\};\qquad Z\mapsto Z\cap U$$

and 

$$\{\text{irreducible closed subset of $U$}\} \rightarrow \{\text{irreducible closed subset of $X$ meeting $U$}\};\qquad Y\mapsto \cl_X(Y)$$

and we can verify that they are mutual bijections.
:::

Moreover, since the two maps in the above proof are inclusion-preserving, there is a one-to-one correspondence between the components meeting $U$ among the irreducible components of $X$ and the irreducible components of $U$.

We now prove the following proposition.

::: Proposition 16
If for a topological space $X$, there exist two finite-dimensional closed subspaces $Y,Z$ such that $X=Y\cup Z$, then their Krull dimensions also satisfy the relation $\dim X=\max(\dim Y,\dim Z)$.
:::

---

**References**

**[Bou]** N. Bourbaki, <i>General Topology</i>. Elements of mathematics. Springer, 1995.
