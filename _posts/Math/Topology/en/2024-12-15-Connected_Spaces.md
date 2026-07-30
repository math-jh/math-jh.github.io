---
title: "Connected Spaces"
description: "This post covers the definition and properties of connected spaces in topology. It proves that connectedness is preserved under continuous functions and that the union of intersecting connected sets is also connected."
excerpt: "Connected spaces, path-connectedness, and connected components"

categories: [Math / Topology]
permalink: /en/math/topology/connected_spaces
sidebar: 
    nav: "topology-en"

date: 2024-12-15
weight: 18
translated_at: 2026-07-21T07:45:01+00:00
translation_source: kimi-cli
last_polished_at: 2026-07-21T07:45:01+00:00
---
Now we examine one of the most important concepts in topology: connectedness.

::: Definition 1
A topological space $X$ is called a *connected space* if $X$ cannot be written as the union of two disjoint nonempty open sets. More generally, a subset $A$ of $X$ is connected if $A$ with the subspace topology is connected.
:::

In other words, a topological space $X$ is disconnected when there exist two disjoint nonempty open sets $U,V$ with $X=U\cup V$. In this case $U$ and $V$ are complements of each other, so they are simultaneously open and closed; hence replacing "open" with "closed" in the above condition yields the same notion. On the other hand, for a subset $A\subseteq X$, unpacking the definition of the subspace topology, $A$ being disconnected means that there exist two open sets $U,V$ in $X$ such that

$$A=(U\cap A)\cup (V\cap A),\qquad U\cap V\cap A=\emptyset$$

and both $U\cap A$ and $V\cap A$ are nonempty.

::: Proposition 2
For a connected set $A\subseteq X$, any $B$ satisfying $A\subseteq B \subseteq \cl(A)$ is connected.
:::
::: Proof
In the given situation,

$$\cl_B(A)=B\cap \cl_X(A)=B$$

so $A$ is a dense subset of $B$. ([§Subspaces, ⁋Proposition 5](/en/math/topology/subspaces#prop5)) Now suppose, toward a contradiction, that there exist two disjoint open sets $U,V$ in $B$ with $U\cup V=B$. Then since $A$ is dense in $B$, both $U\cap A$ and $V\cap A$ are nonempty and $U\cap V\cap A=\emptyset$. This contradicts the assumption that $A$ is connected.
:::

The following proposition is also intuitively plausible.

::: Proposition 3
For a family $(A_i)$ of connected sets, if $A_i\cap A_j\neq\emptyset$ holds for every $i,j$, then $A=\bigcup A_i$ is also connected.
:::
::: Proof
Suppose, toward a contradiction, that there exist two open sets $U,V$ satisfying

$$A=(U\cap A)\cup (V\cap A),\qquad U\cap V\cap A=\emptyset.$$

First, for any $i$, since $A_i$ is connected, exactly one of $A_i\subseteq U$ or $A_i\subseteq V$ must hold. On the other hand, if $A_i\subseteq U$ and $A_j\subseteq V$, then

$$A_i\cap A_j\subseteq (U\cap A)\cap (V\cap A)=U\cap V\cap A=\emptyset$$

which is a contradiction; hence all $A_i$ must lie simultaneously in $U$ or simultaneously in $V$. Therefore either $U\cap A=\emptyset$ or $V\cap A=\emptyset$.
:::

## Properties of Connected Sets

Connectedness is preserved by continuous maps.

::: Proposition 4
For any continuous function $f:X \rightarrow Y$ and any connected subset $A\subseteq X$, the image $f(A)$ is also connected.
:::
::: Proof
Suppose, toward a contradiction, that $f(A)$ is not connected, and choose open sets $V_1,V_2$ in $Y$ such that

$$f(A)=(V_1\cap f(A))\cup (V_2\cap f(A)), \qquad V_1\cap V_2\cap f(A)=\emptyset.$$

Then $f^{-1}(V_1),f^{-1}(V_2)$ are open in $X$, and

$$A=(A\cap f^{-1}(V_1))\cup (A\cap f^{-1}(V_2)),\qquad f^{-1}(V_1)\cap f^{-1}(V_2)\cap A=\emptyset.$$

Since $A$ is connected, we conclude that either $V_1\cap f(A)=\emptyset$ or $V_2\cap f(A)=\emptyset$.
:::

From this we obtain the following corollary.

::: Corollary 5
A quotient space of a connected space is connected.
:::
::: Proof
Let an equivalence relation $R$ be given on a connected space $X$. The canonical projection $p:X \rightarrow X/R$ is a continuous surjection. ([§Quotient Spaces, ⁋Definition 3](/en/math/topology/quotient_spaces#def3)) Therefore by [Proposition 4](#prop4), $X/R=p(X)$ is also connected.
:::

Moreover, the following holds.

::: Proposition 6
The product of connected spaces is connected. Conversely, if a product is connected then each factor is connected.
:::
::: Proof
The reverse direction follows immediately by applying [Proposition 4](#prop4) to the projections $\pr_i$, so there is nothing to prove.

Thus assume each $X_i$ is connected, and suppose toward a contradiction that $X=\prod X_i$ is not connected. If $X=U\cup V$ with $U\cap V=\emptyset$ and $U,V\neq\emptyset$, then the function $f:X \rightarrow \{0,1\}$ defined by

$$f(x)=\begin{cases}1&\text{if $x\in U$}\\0&\text{if $x\in V$}\end{cases}$$

is continuous. (Here $\{0,1\}$ carries the discrete topology.)

Now fix an element $a=(a_i)\in X$, and define $\iota_i: X_i \rightarrow X$ to be the map whose $i$-th coordinate is $x$ and whose remaining coordinates come from $a$. Then $f\circ\iota_i$ is a continuous function from $X_i$ to $\{0,1\}$, and since $X_i$ is connected, $f\circ\iota_i$ must be constant. Hence by induction, points of $X$ all of whose coordinates agree with $a$ except for finitely many must satisfy $f(x)=f(a)$. Such points form a dense subset of $X$, so $f$ must be constant on all of $X$, which is a contradiction.
:::

## Connected Components

On the other hand, for a fixed $x\in X$, the collection of connected sets containing $x$ satisfies the hypothesis of [Proposition 3](#prop3), so it makes sense to speak of the largest connected set containing $x$.

::: Definition 7
The *connected component* containing a point $x\in X$ is the largest connected subset of $X$ containing $x$. If for every point $x$ of $X$ the connected component containing $x$ is always $\{x\}$ itself, we call $X$ *totally disconnected*.
:::

By definition, if $X$ is connected then $X$ has a unique connected component. More generally, any $X$ can be written as the union of its connected components

$$X=\bigcup_{i\in I} U_i.$$

Moreover, by [Proposition 2](#prop2) each $U_i$ must be closed. If $I$ is finite, then the $U_i$ are all simultaneously open and closed. Of course this does not apply when there are infinitely many connected components, but any clopen set in an arbitrary topological space must be a union of connected components. For if some connected component $C$ met a clopen set $A$ and also met its complement, then $C\cap A$ and $C\setminus A$ would be two open sets partitioning $C$.

Furthermore, the following holds.

::: Proposition 8
Define an equivalence relation $\sim$ on a topological space $X$ by

$$x\sim y\iff \text{$x$ and $y$ lie in the same component}.$$

Then $X/{\sim}$ is totally disconnected.
:::
::: Proof
Let $p:X \rightarrow X/{\sim}$ be the canonical projection. By the definition of the quotient space, a subset $S$ of $X/{\sim}$ is open if and only if $p^{-1}(S)$ is open in $X$. ([§Quotient Spaces, ⁋Definition 3](/en/math/topology/quotient_spaces#def3)) Taking complements, we also see that $S$ is closed in $X/{\sim}$ if and only if $p^{-1}(S)$ is closed in $X$.

Now we must show that any connected component $C$ of $X/{\sim}$ is a singleton. First we show that $p^{-1}(C)$ is connected. By [Proposition 2](#prop2), connected components are always closed, so $C$ is closed in $X/{\sim}$, and by the observation above $p^{-1}(C)$ is closed in $X$. Suppose, toward a contradiction, that $p^{-1}(C)$ is the union of two disjoint nonempty closed sets $Z_1,Z_2$. Since $p^{-1}(C)$ is closed in $X$, so are $Z_1,Z_2$. ([§Subspaces, ⁋Lemma 3](/en/math/topology/subspaces#lem3)) On the other hand, for any $c\in C$, the set $p^{-1}(c)$ is a connected component of $X$, and the two sets $Z_1\cap p^{-1}(c)$ and $Z_2\cap p^{-1}(c)$ partition the connected set $p^{-1}(c)$ into disjoint closed sets, so one of them must be empty. That is, each $p^{-1}(c)$ is entirely contained in exactly one of $Z_1$ or $Z_2$. Let $C_1$ be the set of $c$ with $p^{-1}(c)\subseteq Z_1$, and $C_2$ the set of $c$ with $p^{-1}(c)\subseteq Z_2$; then $C_1,C_2$ are disjoint, $C=C_1\cup C_2$, and $p^{-1}(C_i)=Z_i$. By the observation in the first paragraph, $C_1,C_2$ are both nonempty closed sets in $X/{\sim}$, contradicting that $C$ is connected.

Therefore $p^{-1}(C)$ is connected, and since $p$ is surjective it is nonempty. Choose a point $x\in p^{-1}(C)$ and let $K$ be the connected component of $x$. Then $p^{-1}(C)$ is a connected set containing $x$, so $p^{-1}(C)\subseteq K$. Conversely, $p^{-1}(C)$ is a union of equivalence classes of $\sim$, and the equivalence class of $x$ is precisely $K$, so $K\subseteq p^{-1}(C)$. Thus $p^{-1}(C)=K$, and since $p$ is surjective, $C=p(p^{-1}(C))=p(K)$ is a single point.
:::

## Locally Connected Spaces

The connectedness we have examined so far is a global property of a space, but in many cases we are interested in whether this property holds around each point.

::: Definition 9
A topological space $X$ is called *locally connected* at a point $x\in X$ if, whenever a neighborhood $U$ of $x$ is given, there exists a connected neighborhood of $x$ contained in $U$. A space that is locally connected at every point is simply called a locally connected space.
:::

Then the following holds.

::: Proposition 10
$X$ is locally connected if and only if every component of every open set in $X$ is open.
:::
::: Proof
First suppose $X$ is locally connected. Let an open set $U$ and a connected component $C$ of $U$ be given, and choose $x\in C$. Since $U$ is a neighborhood of $x$, by assumption there exists a connected neighborhood $N$ of $x$ contained in $U$. Then $N$ is a connected subset of $U$ containing $x$, so $N\subseteq C$, and since $N$ is a neighborhood of $x$, so is $C$. Since $x$ was an arbitrary point of $C$, by [§Open Sets, ⁋Proposition 5](/en/math/topology/open_sets#prop5) the set $C$ is open.

Conversely, suppose every component of every open set in $X$ is open. Let a point $x\in X$ and a neighborhood $U$ of $x$ be given. By the definition of neighborhood there exists an open neighborhood $V$ of $x$ with $V\subseteq U$. Now let $C$ be the connected component of $V$ containing $x$; then by assumption $C$ is open, and hence $C$ is a connected neighborhood of $x$ contained in $U$. Therefore $X$ is locally connected.
:::

In particular, if $X$ is locally connected then the connected components of $X$ itself are all open. Since the complement of each component is the union of the remaining components, in this case the connected components are simultaneously open and closed. This contrasts with the general situation where connected components of an arbitrary topological space are only guaranteed to be closed.

## Path-Connected Spaces

Connectedness was defined as a negative condition: no partition of the space into two pieces exists. On the other hand, we can also translate the intuition that a space is "one piece" in a positive way: it should be possible to connect any two points of the space continuously within the space. Formalizing this yields the following definition.

::: Definition 11
For a topological space $X$, a continuous function $\gamma:[0,1]\rightarrow X$ is called a *path* in $X$ from $\gamma(0)$ to $\gamma(1)$. A space $X$ is called *path-connected* if for any two points $x,y\in X$ there exists a path from $x$ to $y$.
:::

Just as in [Definition 1](#def1), a subset $A\subseteq X$ being path-connected means that $A$ with the subspace topology is path-connected, which is equivalent to saying that any two points of $A$ can be joined by a path whose image lies in $A$. For example, if a subset $A$ of $\mathbb{R}^n$ contains the entire line segment joining any two points $x,y\in A$, then $A$ is path-connected, because the parametrization $\gamma(t)=(1-t)x+ty$ of the line segment is continuous since each coordinate function $t\mapsto(1-t)x_i+ty_i$ is continuous ([§Product Spaces, ⁋Proposition 2](/en/math/topology/product_spaces#prop2)), and restricting the codomain to $A$ preserves continuity. ([§Subspaces, §§Subspaces and Continuous Functions](/en/math/topology/subspaces#subspaces-and-continuous-functions)) In particular, $\mathbb{R}^n$ itself is path-connected.

The relationship between path-connectedness and connectedness goes through the closed interval $[0,1]$, which is the domain of a path. First we show that a closed interval is connected; this relies on the completeness of the real numbers, which states that every nonempty bounded above subset of $\mathbb{R}$ has a supremum. ([\[Set Theory\] §Elements of Ordered Sets, ⁋Definition 6](/en/math/set_theory/elements_in_ordered_set#def6))

::: Lemma 12
For any real numbers $a\leq b$, the closed interval $[a,b]$ is a connected subset of $\mathbb{R}$.
:::
::: Proof
Suppose, toward a contradiction, that there exist two open sets $U,V$ in $\mathbb{R}$ such that

$$[a,b]=(U\cap[a,b])\cup(V\cap[a,b]),\qquad U\cap V\cap[a,b]=\emptyset$$

and both $U\cap[a,b]$ and $V\cap[a,b]$ are nonempty. Without loss of generality assume $b\in V$. The set $U\cap[a,b]$ is nonempty and bounded above by $b$, so by the completeness of the real numbers the supremum $s=\sup(U\cap[a,b])$ exists and satisfies $a\leq s\leq b$.

First suppose $s\in U$. Since $b\in V$ and $U\cap V\cap[a,b]=\emptyset$, we have $s\neq b$, i.e. $s<b$. As $U$ is open, for some $\epsilon>0$ the open interval $(s-\epsilon,s+\epsilon)$ is contained in $U$. Then choosing $t$ with $s<t<\min(s+\epsilon,b)$ gives $t\in U\cap[a,b]$, contradicting that $s$ is an upper bound of $U\cap[a,b]$.

Now suppose $s\in V$. Similarly, for some $\epsilon>0$ we have $(s-\epsilon,s+\epsilon)\subseteq V$. Any $t\in U\cap[a,b]$ satisfies $t\leq s$, and since $U\cap V\cap[a,b]=\emptyset$, $t$ cannot lie in $(s-\epsilon,s]$, so $t\leq s-\epsilon$. Thus $s-\epsilon$ is also an upper bound of $U\cap[a,b]$, contradicting that $s$ is the least upper bound.

Since $s\in[a,b]\subseteq U\cup V$, one of the two cases must occur, and either yields a contradiction; hence $[a,b]$ is connected.
:::

Then, as our intuition suggested, we can show that path-connectedness is a stronger condition than connectedness.

::: Proposition 13
A path-connected space is connected.
:::
::: Proof
Suppose, toward a contradiction, that a path-connected space $X$ is not connected, and let $X=U\cup V$ for disjoint nonempty open sets $U,V$. Choose $x\in U$ and $y\in V$; then by assumption there exists a path $\gamma:[0,1]\rightarrow X$ from $x$ to $y$. By [Lemma 12](#lem12) and [Proposition 4](#prop4), the image $\gamma([0,1])$ is connected. However, $U\cap\gamma([0,1])$ and $V\cap\gamma([0,1])$ contain $x$ and $y$ respectively so are nonempty, and $\gamma([0,1])\subseteq U\cup V$ with $U\cap V\cap\gamma([0,1])=\emptyset$, contradicting that $\gamma([0,1])$ is connected.
:::

In particular, $\mathbb{R}^n$ is connected. However, the converse of this proposition does not hold. The following example is a classic instance of a space that is connected but not path-connected.

::: Example 14
Consider the two subsets of the plane $\mathbb{R}^2$

$$S=\{(x,\sin(1/x))\mid 0<x\leq 1\},\qquad T=S\cup(\{0\}\times[-1,1]).$$

That is, $T$ is the curve $S$ together with the vertical line segment where the oscillations of $S$ accumulate. We call $T$ the *topologist's sine curve*; we show that $T$ is connected but not path-connected.

First we show that $T$ is connected. Define a function $\phi:(0,1]\rightarrow\mathbb{R}^2$ by $\phi(x)=(x,\sin(1/x))$; since both coordinate functions are continuous, $\phi$ is continuous. ([§Product Spaces, ⁋Proposition 2](/en/math/topology/product_spaces#prop2)) On the other hand, $(0,1]=\bigcup_{n\geq 1}[1/n,1]$, and each $[1/n,1]$ is connected by [Lemma 12](#lem12); since they all contain $1$, by [Proposition 3](#prop3) the interval $(0,1]$ is connected. Therefore $S=\phi((0,1])$ is also connected. ([Proposition 4](#prop4))

Next we verify that $\{0\}\times[-1,1]\subseteq\cl(S)$. Given $y\in[-1,1]$, choose $\theta_0\in[\pi/2,5\pi/2]$ with $\sin\theta_0=y$; then for each natural number $n$, the number $x_n=1/(\theta_0+2\pi n)$ lies in $(0,1]$ and satisfies $\sin(1/x_n)=\sin\theta_0=y$, so $(x_n,y)\in S$. Any neighborhood of the point $(0,y)$ contains an open ball $\{z\in\mathbb{R}^2: \lVert z-(0,y)\rVert<\epsilon\}$ for some $\epsilon>0$, and since the distance between $(x_n,y)$ and $(0,y)$ is $x_n$, choosing $n$ sufficiently large gives $x_n<\epsilon$, so this neighborhood must meet $S$. Therefore $(0,y)\in\cl(S)$. ([§Interior, Closure, and Boundary, ⁋Proposition 6](/en/math/topology/other_concepts#prop6)) Then $S\subseteq T\subseteq\cl(S)$, so by [Proposition 2](#prop2) the set $T$ is connected.

Now we show that $T$ is not path-connected. Suppose, toward a contradiction, that there exists a path $\gamma:[0,1]\rightarrow T$ with $\gamma(0)\in\{0\}\times[-1,1]$ and $\gamma(1)\in S$. Let $u=\pr_1\circ\gamma$ and $v=\pr_2\circ\gamma$ be the two coordinate functions of $\gamma$; these are continuous as compositions of continuous functions. Among the points of $T$, those with positive first coordinate are exactly the points of $S$, so for $t$ with $u(t)>0$ we have $v(t)=\sin(1/u(t))$.

The set $P=\{t\in[0,1]\mid u(t)>0\}$ contains $1$ so is nonempty, and $0$ is a lower bound, so by the completeness of the real numbers the infimum $t_0=\inf P$ exists. First we verify that $u(t_0)=0$. Since the first coordinate of $\gamma(0)$ is $0$, if $t_0=0$ then immediately $u(t_0)=0$. If $t_0>0$, then if $u(t_0)>0$, by continuity of $u$ the preimage $u^{-1}((0,\infty))$ contains an open neighborhood of $t_0$, so $u(t)>0$ for some $t<t_0$, contradicting that $t_0$ is a lower bound of $P$. Therefore $u(t_0)=0$ and $\gamma(t_0)\in\{0\}\times[-1,1]$.

Since $\gamma$ is continuous at $t_0$, for the open ball $B=\{z\in\mathbb{R}^2:\lVert z-\gamma(t_0)\rVert<1/2\}$ of radius $1/2$, the preimage $\gamma^{-1}(B\cap T)$ contains an open neighborhood of $t_0$, so there exists $\delta>0$ such that $t\in[t_0,t_0+\delta)$ implies $\lVert\gamma(t)-\gamma(t_0)\rVert<1/2$. On the other hand, since $t_0$ is the infimum of $P$, there exists an element $t_1$ of $P$ in $[t_0,t_0+\delta)$, and since $u(t_0)=0$ we have $t_0<t_1$. Now write $a=u(t_1)>0$. By [Lemma 12](#lem12) and [Proposition 4](#prop4), the image $u([t_0,t_1])$ is connected. If some real number $c$ with $0<c<a$ did not belong to $u([t_0,t_1])$, then the two open sets $(-\infty,c)$ and $(c,\infty)$ would partition $u([t_0,t_1])$ and contain $u(t_0)=0$ and $u(t_1)=a$ respectively, so would be nonempty, a contradiction. Therefore $[0,a]\subseteq u([t_0,t_1])$.

Now choose a natural number $k$ sufficiently large that both numbers $2/((4k+1)\pi)$ and $2/((4k-1)\pi)$ lie in $(0,a]$; then there exist $t',t''\in[t_0,t_1]$ with $u(t')=2/((4k+1)\pi)$ and $u(t'')=2/((4k-1)\pi)$. Since the first coordinates are positive, $\gamma(t')$ and $\gamma(t'')$ are points of $S$, and their second coordinates are respectively

$$v(t')=\sin((4k+1)\pi/2)=1,\qquad v(t'')=\sin((4k-1)\pi/2)=-1.$$

However, since $t',t''\in[t_0,t_0+\delta)$, the triangle inequality gives

$$\lVert\gamma(t')-\gamma(t'')\rVert\leq\lVert\gamma(t')-\gamma(t_0)\rVert+\lVert\gamma(t_0)-\gamma(t'')\rVert<1$$

whereas looking only at the difference of the second coordinates of the two points gives $\lVert\gamma(t')-\gamma(t'')\rVert\geq 2$. This is a contradiction; therefore $T$ is connected but not path-connected.
:::
