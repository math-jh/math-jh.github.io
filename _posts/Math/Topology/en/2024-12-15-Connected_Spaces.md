---
title: "Connected Spaces"
description: "This post covers the definition and properties of connected spaces in topology. It proves that connectedness is preserved under continuous functions and that the union of intersecting connected sets is also connected."
excerpt: "Connected spaces, path-connectedness, and connected components"

categories: [Math / Topology]
permalink: /en/math/topology/connected_spaces
sidebar: 
    nav: "topology-en"

date: 2024-12-15
weight: 20
translated_at: 2026-07-21T07:45:01+00:00
translation_source: kimi-cli
last_polished_at: 2026-11-10T19:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
Now we examine one of the important concepts in topology, connectedness.

::: Definition 1
A topological space $X$ is a *connected space* if $X$ cannot be represented as the union of two disjoint nonempty open sets. More generally, for a subset of $X$, $A$ is connected if $A$ equipped with the subspace topology is connected.
:::

That is, a topological space $X$ being disconnected means that there exist two disjoint nonempty open sets $U,V$ such that $X=U\cup V$. In this case, since $U$ and $V$ are complements of each other, they are both open and closed; hence we know that replacing open sets with closed sets in the condition above yields the same concept. On the other hand, for a subset $A\subseteq X$, unpacking the definition of the subspace topology, $A$ being disconnected means that in $X$ there exist two open sets $U,V$ such that

$$A=(U\cap A)\cup (V\cap A),\qquad U\cap V\cap A=\emptyset$$

and both $U\cap A$ and $V\cap A$ are nonempty.

::: Proposition 2
For a connected set $A\subseteq X$, if $A\subseteq B \subseteq \cl(A)$, then $B$ is connected.
:::
::: Proof
In the given situation, since

$$\cl_B(A)=B\cap \cl_X(A)=B$$

$A$ is a dense subset of $B$. ([§Subspaces, ⁋Proposition 5](/en/math/topology/subspaces#prop5){: data-lid="1azsh" }) Now suppose, toward a contradiction, that in $B$ there exist two disjoint open sets $U,V$ such that $U\cup V=B$. Then since $A$ is a dense subset of $B$, $U\cap A, V\cap A$ are both nonempty and $U\cap V\cap A=\emptyset$. This contradicts the assumption that $A$ is connected.
:::

Also, the following proposition is intuitively plausible.

::: Proposition 3
For a family $(A_i)$ of connected sets, if for every $i,j$ we have $A_i\cap A_j\neq\emptyset$, then $A=\bigcup A_i$ is also connected.
:::
::: Proof
Suppose, toward a contradiction, that there exist two open sets $U,V$ such that the two conditions

$$A=(U\cap A)\cup (V\cap A),\qquad U\cap V\cap A=\emptyset$$

hold. First, for any $i$, since $A_i$ is connected, exactly one of the two statements $A_i\subseteq U$ or $A_i\subseteq V$ must hold. On the other hand, if $A_i\subseteq U$ and $A_j\subseteq V$, then

$$A_i\cap A_j\subseteq (U\cap A)\cap (V\cap A)=U\cap V\cap A=\emptyset$$

which is a contradiction; hence the $A_i$ must all simultaneously belong to $U$ or simultaneously belong to $V$. Then we must have $U\cap A=\emptyset$ or $V\cap A=\emptyset$.
:::

## Properties of Connected Sets

Connectedness is a property preserved by continuous functions.

::: Proposition 4
For any continuous function $f:X \rightarrow Y$ and any connected subset of $X$, $A\subseteq X$, $f(A)$ is also connected.
:::
::: Proof
Suppose, toward a contradiction, that $f(A)$ is not connected, and let

$$f(A)=(V_1\cap f(A))\cup (V_2\cap f(A)), \qquad V_1\cap V_2\cap f(A)=\emptyset$$

hold by choosing open sets in $Y$, $V_1,V_2$. Then $f^{-1}(V_1),f^{-1}(V_2)$ are open sets in $X$, and

$$A=(A\cap f^{-1}(V_1))\cup (A\cap f^{-1}(V_2)),\qquad f^{-1}(V_1)\cap f^{-1}(V_2)\cap A=\emptyset$$

holds. Now from the assumption that $A$ is connected, we know that either $V_1\cap f(A)=\emptyset$ or $V_2\cap f(A)=\emptyset$.
:::

From this we obtain the following corollary.

::: Corollary 5
A quotient space of a connected space is connected.
:::
::: Proof
Suppose that on a connected space $X$, an equivalence relation $R$ is given. The canonical projection $p:X \rightarrow X/R$ is a continuous surjection. ([§Quotient Spaces, ⁋Definition 3](/en/math/topology/quotient_spaces#def3){: data-lid="7pbe8" }) Therefore, by [Proposition 4](#prop4){: data-lid="3zh41" }, $X/R=p(X)$ is also connected.
:::

Also, the following holds.

::: Proposition 6
The product of connected spaces is connected. Conversely, if a nonempty product is connected, each of its components is also connected.
:::
::: Proof
For the reverse direction, since $\pr_i$ is surjective if the product is nonempty, we can apply [Proposition 4](#prop4){: data-lid="m7qlj" } to $\pr_i$.

Thus assume each $X_i$ is connected, and suppose toward a contradiction that $X=\prod X_i$ is not connected. If $X=U\cup V$ with $U\cap V=\emptyset$ and $U,V\neq\emptyset$, then setting

$$f(x)=\begin{cases}1&\text{if $x\in U$}\\0&\text{if $x\in V$}\end{cases}$$

the function $f:X \rightarrow \{0,1\}$ defined in this way is continuous. (Here $\{0,1\}$ is the space equipped with the discrete topology.)

Now fix an element $a=(a_i)\in X$, and define $\iota_i: X_i \rightarrow X$ to be the function whose $i$-th component is $x$ and whose remaining components come from $a$. Here, in place of $a$, we can take an arbitrary point of $X$ as a base point to define $\iota_i$ in the same way. Then $\iota_i$ is continuous because each component function is either the identity function or a constant function ([§Product Spaces, ⁋Proposition 2](/en/math/topology/product_spaces#prop2){: data-lid="slta3" }), $f\circ\iota_i$ is a continuous function from $X_i$ to $\{0,1\}$, and from the assumption that $X_i$ is connected, we know that $f\circ\iota_i$ must be a constant function. Therefore, by induction, we know that agreeing with $a$ in all but finitely many components, points of $X$, $x$, must satisfy $f(x)=f(a)$. Since such points form a dense subset of $X$, $f$ must be a constant function on all of $X$, which is a contradiction.
:::

## Connected Components

On the other hand, for a fixed $x\in X$, the collection of connected sets containing $x$ satisfies the hypothesis of [Proposition 3](#prop3){: data-lid="22cxz" }, so the largest connected set containing $x$ makes sense.

::: Definition 7
The *connected component* containing a point of $X$, $x\in X$, is the largest connected subset containing $x$ in $X$. If in $X$, the connected component containing any point $x$ is always $\{x\}$ itself, we call $X$ *totally disconnected*.
:::

By definition, if $X$ is connected, then $X$ has a unique connected component. More generally, any $X$ can be written as the union of its connected components:

$$X=\bigcup_{i\in I} U_i$$

Meanwhile, by [Proposition 2](#prop2){: data-lid="9crha" }, each $U_i$ must be closed. If $I$ is a finite set, we know that the $U_i$ must all be simultaneously open and closed. Of course, this does not apply to infinitely many connected components, but any clopen set in an arbitrary topological space must be represented as a union of connected components. This is because, if this were not the case and some connected component $C$ met a clopen set $A$ while simultaneously meeting the complement of $A$, then $C\cap A$ and $C\setminus A$ would be two open sets partitioning $C$.

Furthermore, the following holds.

::: Proposition 8
On a topological space $X$, define an equivalence relation $\sim$ by

$$x\sim y\iff \text{$x$ and $y$ lie in the same component}$$

Then $X/{\sim}$ is totally disconnected.
:::
::: Proof
Let $p:X \rightarrow X/{\sim}$ be the canonical projection. By the definition of the quotient space, in $X/{\sim}$, a subset $S$ is open if and only if $p^{-1}(S)$ is open in $X$. ([§Quotient Spaces, ⁋Definition 3](/en/math/topology/quotient_spaces#def3){: data-lid="i496s" }) Taking complements, we also see that in $X/{\sim}$, a subset $S$ is closed if and only if $p^{-1}(S)$ is closed in $X$.

Now it suffices to show that in $X/{\sim}$, any connected component $C$ is a singleton. First, we show that $p^{-1}(C)$ is connected. By [Proposition 2](#prop2){: data-lid="5na2j" }, connected components are always closed, so $C$ is closed in $X/{\sim}$, and by the observation above, $p^{-1}(C)$ is closed in $X$. Suppose, toward a contradiction, that $p^{-1}(C)$ is the union of two disjoint nonempty closed sets $Z_1,Z_2$. Since $p^{-1}(C)$ is closed in $X$, $Z_1,Z_2$ are also closed in $X$. ([§Subspaces, ⁋Lemma 3](/en/math/topology/subspaces#lem3){: data-lid="1b669" }) On the other hand, for any $c\in C$, $p^{-1}(c)$ is a connected component of $X$, and since the two sets $Z_1\cap p^{-1}(c)$ and $Z_2\cap p^{-1}(c)$ divide the connected set $p^{-1}(c)$ into two disjoint closed sets, one of them must be empty. That is, each $p^{-1}(c)$ is entirely contained in exactly one of $Z_1$ and $Z_2$. Then, letting the condition $p^{-1}(c)\subseteq Z_1$ define the collection of such $c$ as $C_1$, and $p^{-1}(c)\subseteq Z_2$ define the collection of such $c$ as $C_2$, $C_1,C_2$ are disjoint, $C=C_1\cup C_2$, and $p^{-1}(C_i)=Z_i$. By the observation in the first paragraph, $C_1,C_2$ are both nonempty closed sets in $X/{\sim}$, contradicting that $C$ is connected.

Therefore, $p^{-1}(C)$ is connected, and since $p$ is surjective, it is nonempty. Choose a point $x\in p^{-1}(C)$, and let the connected component of $x$ be $K$. Then $p^{-1}(C)$ is a connected set containing $x$, so $p^{-1}(C)\subseteq K$. Conversely, $p^{-1}(C)$ is a union of equivalence classes of $\sim$, and the equivalence class of $x$ is precisely $K$, so $K\subseteq p^{-1}(C)$. Therefore, $p^{-1}(C)=K$, and since $p$ is surjective, $C=p(p^{-1}(C))=p(K)$ is a single point.
:::

## Locally Connected Spaces

The connectedness we have examined so far was a property of the space as a whole, but in many cases we are interested in whether this property holds around each point as well.

::: Definition 9
A topological space $X$ is called *locally connected* at a point $x\in X$ if, whenever for $x$ any neighborhood $U$ is given, there exists in $U$ a connected neighborhood of $x$. A space that is locally connected at every point is simply called a locally connected space.
:::

Then the following holds.

::: Proposition 10
$X$ is locally connected if and only if every component of every open set in $X$ is open.
:::
::: Proof
First, suppose $X$ is locally connected. Let an open set $U$ and a connected component of $U$, $C$, be given, and choose $x\in C$. Since $U$ is a neighborhood of $x$, by assumption there exists in $U$ a connected neighborhood of $x$, $N$. Then, since $N$ contains $x$ and is a connected subset of $U$, $N\subseteq C$, and since $N$ is a neighborhood of $x$, $C$ is also a neighborhood of $x$. Since $x$ was an arbitrary point of $C$, by [§Open Sets, ⁋Proposition 5](/en/math/topology/open_sets#prop5){: data-lid="vv7qq" } the set $C$ is open.

Conversely, suppose every component of every open set in $X$ is open. Given a point $x\in X$ and a neighborhood of $x$, $U$, by the definition of a neighborhood there exists an open neighborhood of $x$, $V$, such that $V\subseteq U$. Now, let the connected component of $V$ containing $x$ be $C$; then by assumption $C$ is open, and hence $C$ is a connected neighborhood in $U$ of $x$. Therefore $X$ is locally connected.
:::

In particular, if $X$ is locally connected, then the connected components of $X$ itself are all open. Since the complement of each component is the union of the remaining components, in this case the connected components are simultaneously open and closed. This contrasts with the fact that the connected components of a general topological space are merely closed.

## Path-Connected Spaces

Connectedness was defined as a negative condition: no partition of the space into two pieces exists. On the other hand, we can also translate the intuition that a space is one piece in a positive way: it should be possible to connect any two points of the space continuously within the space. Formalizing this yields the following definition.

::: Definition 11
For a topological space $X$, a continuous function $\gamma:[0,1]\rightarrow X$ is called a *path* from $\gamma(0)$ to $\gamma(1)$ in $X$. A space $X$ is called *path-connected* if for any two points $x,y\in X$ there exists a path from $x$ to $y$.
:::

Just as in [Definition 1](#def1){: data-lid="0ffma" }, a subset $A\subseteq X$ being path-connected means that $A$ with the subspace topology is path-connected, which is equivalent to saying that any two points of $A$ can be joined by a path whose image is contained in $A$. For example, if a subset of $\mathbb{R}^n$, $A$, contains the entire line segment joining any two points $x,y\in A$, then $A$ is path-connected, because the parametrization $\gamma(t)=(1-t)x+ty$ of the line segment is continuous since each component function $t\mapsto(1-t)x_i+ty_i$ is continuous ([§Product Spaces, ⁋Proposition 2](/en/math/topology/product_spaces#prop2){: data-lid="qwx7k" }), and restricting the codomain to $A$ preserves continuity. ([§Subspaces, §§Subspaces and Continuous Functions](/en/math/topology/subspaces#subspaces-and-continuous-functions){: data-lid="i33oa" }) In particular, $\mathbb{R}^n$ itself is path-connected.

The relationship between path-connectedness and connectedness goes through the closed interval $[0,1]$, which is the domain of a path. First we show that a closed interval is connected; this relies on the completeness of the real numbers, which states that every nonempty, bounded-above subset of $\mathbb{R}$ always has a supremum. ([\[Set Theory\] §Elements of Ordered Sets, ⁋Definition 6](/en/math/set_theory/elements_in_ordered_set#def6){: data-lid="oppw1" })

::: Lemma 12
For any real numbers $a\leq b$, the closed interval $[a,b]$ is a connected subset of $\mathbb{R}$.
:::
::: Proof
Suppose, toward a contradiction, that there exist in $\mathbb{R}$ two open sets $U,V$ such that

$$[a,b]=(U\cap[a,b])\cup(V\cap[a,b]),\qquad U\cap V\cap[a,b]=\emptyset$$

and both $U\cap[a,b]$ and $V\cap[a,b]$ are nonempty. Without loss of generality assume $b\in V$. The set $U\cap[a,b]$ is nonempty and $b$ is an upper bound, so by the completeness of the real numbers the supremum $s=\sup(U\cap[a,b])$ exists and satisfies $a\leq s\leq b$.

First suppose $s\in U$. Since $b\in V$ and $U\cap V\cap[a,b]=\emptyset$, we have $s\neq b$, i.e. $s<b$. As $U$ is open, for some $\epsilon>0$ the open interval $(s-\epsilon,s+\epsilon)$ is contained in $U$. Then, choosing $s<t<\min(s+\epsilon,b)$, such a $t$ satisfies $t\in U\cap[a,b]$, contradicting that $s$ is an upper bound of $U\cap[a,b]$.

Now suppose $s\in V$. Similarly, for some $\epsilon>0$ we have $(s-\epsilon,s+\epsilon)\subseteq V$. Any $t\in U\cap[a,b]$ satisfies $t\leq s$, and since $U\cap V\cap[a,b]=\emptyset$, we cannot have $t\in(s-\epsilon,s]$, so $t\leq s-\epsilon$. Thus $s-\epsilon$ is also an upper bound of $U\cap[a,b]$, contradicting that $s$ is the least upper bound.

Since $s\in[a,b]\subseteq U\cup V$, one of the two cases must occur, and either yields a contradiction; hence $[a,b]$ is connected.
:::

Then, as in the intuition above, we can show that path-connectedness is a stronger condition than connectedness.

::: Proposition 13
A path-connected space is connected.
:::
::: Proof
Suppose, toward a contradiction, that a path-connected space $X$ is not connected, and for two disjoint nonempty open sets $U,V$, let $X=U\cup V$. If we choose $x\in U$ and $y\in V$ respectively, then by assumption there exists a path from $x$ to $y$, $\gamma:[0,1]\rightarrow X$. By [Lemma 12](#lem12){: data-lid="d6vff" } and [Proposition 4](#prop4){: data-lid="2lpi0" }, $\gamma([0,1])$ is connected. However, $U\cap\gamma([0,1])$ and $V\cap\gamma([0,1])$ contain $x$ and $y$ respectively and are therefore nonempty, and since $\gamma([0,1])\subseteq U\cup V$ and $U\cap V\cap\gamma([0,1])=\emptyset$, this contradicts that $\gamma([0,1])$ is connected.
:::

In particular, $\mathbb{R}^n$ is connected. However, the converse of this proposition does not hold. The following example is a classic instance of a space that is connected but not path-connected.

::: Example 14
Consider the two subsets of the plane $\mathbb{R}^2$

$$S=\{(x,\sin(1/x))\mid 0<x\leq 1\},\qquad T=S\cup(\{0\}\times[-1,1])$$

That is, $T$ is the curve $S$ together with the vertical line segment where the oscillations of $S$ accumulate. We call $T$ the *topologist's sine curve*; we show that $T$ is connected but not path-connected.

First we show that $T$ is connected. Define a function $\phi:(0,1]\rightarrow\mathbb{R}^2$ by $\phi(x)=(x,\sin(1/x))$; since both coordinate functions are continuous, $\phi$ is continuous. ([§Product Spaces, ⁋Proposition 2](/en/math/topology/product_spaces#prop2){: data-lid="tq1f7" }) On the other hand, $(0,1]=\bigcup_{n\geq 1}[1/n,1]$, and each $[1/n,1]$ is connected by [Lemma 12](#lem12){: data-lid="gensu" }; since they all contain $1$, by [Proposition 3](#prop3){: data-lid="o2wd0" }, $(0,1]$ is connected. Therefore $S=\phi((0,1])$ is also connected. ([Proposition 4](#prop4){: data-lid="115ke" })

Next we verify that $\{0\}\times[-1,1]\subseteq\cl(S)$. Given $y\in[-1,1]$, choose, with $\sin\theta_0=y$, some $\theta_0\in[\pi/2,5\pi/2]$; then for each natural number $n$, $x_n=1/(\theta_0+2\pi n)$ belongs to $(0,1]$ and $\sin(1/x_n)=\sin\theta_0=y$, so $(x_n,y)\in S$. Any neighborhood of the point $(0,y)$ contains, for some $\epsilon>0$, the open ball $\{z\in\mathbb{R}^2: \lVert z-(0,y)\rVert<\epsilon\}$; since the distance between $(x_n,y)$ and $(0,y)$ is $x_n$, if we choose $n$ sufficiently large then $x_n<\epsilon$, so this neighborhood must meet $S$. Therefore $(0,y)\in\cl(S)$. ([§Interior, Closure, and Boundary, ⁋Proposition 6](/en/math/topology/other_concepts#prop6){: data-lid="9eihp" }) Then $S\subseteq T\subseteq\cl(S)$, so by [Proposition 2](#prop2){: data-lid="742gw" }, $T$ is connected.

Now we show that $T$ is not path-connected. Suppose, toward a contradiction, that there exists, with $\gamma(0)\in\{0\}\times[-1,1]$ and $\gamma(1)\in S$, a path $\gamma:[0,1]\rightarrow T$. Let the two component functions of $\gamma$ be $u=\pr_1\circ\gamma$ and $v=\pr_2\circ\gamma$; these are continuous as compositions of continuous functions. Among the points of $T$, those with positive first coordinate are precisely the points of $S$, so if $u(t)>0$, at $t$ we have $v(t)=\sin(1/u(t))$.

The set $P=\{t\in[0,1]\mid u(t)>0\}$ contains $1$ so is nonempty, and since $0$ is a lower bound, by the completeness of the real numbers the infimum $t_0=\inf P$ exists. First we verify that $u(t_0)=0$. Since the first coordinate of $\gamma(0)$ is $0$, if $t_0=0$ then immediately $u(t_0)=0$. In the case where $t_0>0$, if $u(t_0)>0$, then by the continuity of $u$, the preimage $u^{-1}((0,\infty))$ contains an open neighborhood of $t_0$, so at a point smaller than $t_0$, say $t$, we have $u(t)>0$, contradicting that $t_0$ is a lower bound of $P$. Therefore $u(t_0)=0$ and $\gamma(t_0)\in\{0\}\times[-1,1]$.

Since $\gamma$ is continuous at $t_0$, for the open ball of radius $1/2$, $B=\{z\in\mathbb{R}^2:\lVert z-\gamma(t_0)\rVert<1/2\}$, the preimage $\gamma^{-1}(B\cap T)$ contains an open neighborhood of $t_0$, and thus there exists $\delta>0$ such that $t\in[t_0,t_0+\delta)$ implies $\lVert\gamma(t)-\gamma(t_0)\rVert<1/2$. On the other hand, since $t_0$ is the infimum of $P$, there exists in $[t_0,t_0+\delta)$ an element of $P$, $t_1$, and since $u(t_0)=0$, we have $t_0<t_1$. Now write $a=u(t_1)>0$. By [Lemma 12](#lem12){: data-lid="kb5tn" } and [Proposition 4](#prop4){: data-lid="yx8e0" }, $u([t_0,t_1])$ is connected. If for some $0<c<a$, the real number $c$ did not belong to $u([t_0,t_1])$, then the two open sets $(-\infty,c)$ and $(c,\infty)$ would partition $u([t_0,t_1])$ and contain $u(t_0)=0$ and $u(t_1)=a$ respectively, so would be nonempty, a contradiction. Therefore $[0,a]\subseteq u([t_0,t_1])$.

Now choose a natural number $k$ sufficiently large that both numbers $2/((4k+1)\pi)$ and $2/((4k-1)\pi)$ lie in $(0,a]$; then with $u(t')=2/((4k+1)\pi)$ and $u(t'')=2/((4k-1)\pi)$, there exist $t',t''\in[t_0,t_1]$. Since the first coordinates are positive, $\gamma(t')$ and $\gamma(t'')$ are points of $S$, and their second coordinates are respectively

$$v(t')=\sin((4k+1)\pi/2)=1,\qquad v(t'')=\sin((4k-1)\pi/2)=-1$$

However, since $t',t''\in[t_0,t_0+\delta)$, by the triangle inequality

$$\lVert\gamma(t')-\gamma(t'')\rVert\leq\lVert\gamma(t')-\gamma(t_0)\rVert+\lVert\gamma(t_0)-\gamma(t'')\rVert<1$$

whereas looking only at the difference of the second coordinates of the two points gives $\lVert\gamma(t')-\gamma(t'')\rVert\geq 2$. This is a contradiction; therefore $T$ is connected but not path-connected.
:::

---

**References**

**[Bou]** N. Bourbaki, <i>General Topology</i>. Elements of mathematics. Springer, 1995.
