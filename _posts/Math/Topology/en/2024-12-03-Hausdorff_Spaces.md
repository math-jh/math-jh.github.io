---
title: "Hausdorff Spaces"
description: "We define the convergence of sequences in topological spaces and examine the space structure where the uniqueness of limits is guaranteed by the Hausdorff separation axiom."
excerpt: "Convergence of sequences and the Hausdorff axiom"

categories: [Math / Topology]
permalink: /en/math/topology/Hausdorff_spaces
sidebar: 
    nav: "topology-en"

date: 2024-12-03
weight: 13
translated_at: 2026-06-03T07:30:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-11-10T03:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
Now we define Hausdorff spaces. Before doing so, we first define the following.

## Convergence of Sequences

::: Definition 1
For a topological space $X$, a function $\mathbb{N} \rightarrow X$ is called a *sequence* of points in $X$, and is denoted by $(x_n)_{n\geq 1}$. That a sequence $(x_n)_{n\geq 1}$ *converges* to $x\in X$ means that for $x$, whenever any neighborhood $U$ is given, there exists an $N\in \mathbb{N}$ such that the statement 

$$n\geq N\implies x_n\in U$$

is true. 
:::

This differs from the $\epsilon$-$N$ definition of sequence convergence already treated in calculus and elsewhere only in that, to represent points close to $x$, instead of an $\epsilon$-ball, an open set $U$ is used. Naturally, if a sequence $(x_n)$ converges to $x$, one would like to write this as $\lim_{n \rightarrow\infty}x_n$, but from the following example we can see that this notation is not even well-defined. 

::: Example 2
Let us endow any set $X$ with the trivial topology and consider $X$ as a topological space. Then any sequence in $X$ converges to every point of $X$. 
:::

## Separation Axioms

The reason a phenomenon like [Example 2](#ex2){: data-lid="xys2v" } above occurs is, intuitively, that the topology defined on $X$ is not strong enough to separate the points of $X$. We may define various kinds of *separation axioms* according to the degree to which points are separated in a topological space, and classify spaces satisfying each of them. To this end, let us fix some terminology.

- In a topological space $X$, two points $x,y$ are distinct if $x\neq y$. 
- In a topological space $X$, two points $x,y$ are *topologically distinguishable* if $\mathcal{N}(x)\neq \mathcal{N}(y)$.[^1] ([§Open Sets, §§Neighborhood filter](/en/math/topology/open_sets#neighborhood-filter){: data-lid="2wcja" })
- In a topological space $X$, two subsets $A,B$ are *separated* if $A,B$ each have a neighborhood disjoint from the other.
- In a topological space $X$, two subsets $A,B$ are *separated by neighborhoods* if they have disjoint neighborhoods.
- In a topological space $X$, two subsets $A,B$ are *separated by closed neighborhoods* if they have disjoint closed neighborhoods.
- In a topological space $X$, two subsets $A,B$ are *separated by continuous functions* if there exists a continuous function $f:X \rightarrow \mathbb{R}$ such that $A\subseteq f^{-1}(\{0\})$ and $B\subseteq f^{-1}(\{1\})$. 
- In a topological space $X$, two subsets $A,B$ are *precisely separated by continuous functions* if there exists a continuous function $f:X \rightarrow \mathbb{R}$ such that $A= f^{-1}(\{0\})$ and $B= f^{-1}(\{1\})$. 

The conditions above are listed in order of strength. That is, two subsets precisely separated by continuous functions are separated by continuous functions; two subsets separated by continuous functions are separated by closed neighborhoods; two subsets separated by closed neighborhoods are separated by neighborhoods; two subsets separated by neighborhoods are separated; two separated points are topologically distinguishable; and all topologically distinguishable points are distinct.

Now we define the following.

::: Definition 3
For a topological space $X$, we define the following.

1. $X$ is a *$T_0$-space*, or a *Kolmogorov space*, if any two distinct points $x,y$ are topologically distinguishable.
2. $X$ is an *$R_0$-space* if any two topologically distinguishable points are separated.
3. $X$ is a *$T_1$-space*, or a *Fréchet space*, if any two distinct points are separated. Thus, $X$ is $T_1$ if and only if $X$ is $T_0$ and $R_0$.
4. $X$ is an *$R_1$-space* if any two topologically distinguishable points are separated by neighborhoods. Hence every $R_1$-space is an $R_0$-space.
5. $X$ is a *$T_2$-space*, or a *Hausdorff space*, if any two distinct points are separated by neighborhoods. Thus, $X$ is $T_2$ if and only if $X$ is $T_0$ and $R_1$, and every $T_2$-space is $T_1$. 
6. $X$ is a *$T_{2\frac{1}{2}}$-space*, or a *Urysohn space*, if any two distinct points are separated by closed neighborhoods. Hence every $T_{2\frac{1}{2}}$-space is $T_2$. 
7. $X$ is a *completely $T_2$-space*, or a *completely Hausdorff space*, if any two distinct points are separated by continuous functions.
8. $X$ is a *regular space* if any point $x\in X$ and any closed set $A\subseteq X$ not containing $x$ are always separated by neighborhoods.
9. $X$ is a *$T_3$-space*, or a *regular Hausdorff space*, if $X$ is $T_0$ and regular. Every $T_3$-space is $T_{2\frac{1}{2}}$. 
10. $X$ is a *completely regular space* if any point $x\in X$ and any closed set $A\subseteq X$ not containing $x$ are always separated by continuous functions.
11. $X$ is a *completely $T_3$-space*, or a *Tychonoff space*, if $X$ is $T_0$ and completely regular. Thus if $X$ is completely $T_3$, then it is completely Hausdorff and regular Hausdorff; it is therefore also called a *completely regular Hausdorff space*.
12. $X$ is a *normal space* if any two disjoint closed subsets are separated by neighborhoods. 
13. $X$ is a *normal regular space* if $X$ is normal and $R_0$. Thus if $X$ is normal regular, then $X$ is completely regular. 
14. $X$ is a *$T_4$-space*, or a *normal Hausdorff space*, if $X$ is $T_1$ and normal. Every $T_1$-space is $R_0$, so every $T_4$-space is normal regular, and hence completely regular. Meanwhile, every $T_1$-space is a $T_0$-space, so from this we see that every $T_4$-space is completely $T_3$.
15. $X$ is a *completely normal space* if any two separated subsets are separated by neighborhoods. Then every completely normal space is normal.
16. $X$ is a *completely $T_4$-space* if $X$ is completely normal and $T_1$. Hence every completely $T_4$-space is $T_4$.
17. $X$ is a *perfectly normal space* if any two disjoint closed subsets are precisely separated by continuous functions.
18. $X$ is a *perfectly $T_4$-space* if $X$ is perfectly normal and $T_0$. 
:::

## Hausdorff Spaces

One of the notions of particular importance in [Definition 3](#def3){: data-lid="sjled" } is that of a Hausdorff space. Here our intuition holds well. 

::: Proposition 4
For any sequence $(x_n)$ in a Hausdorff space $X$, there exists at most one point to which $(x_n)$ converges.
:::
::: Proof
Suppose for contradiction that $(x_n)$ converges to two points $x,y$. Then, for $x$ and $y$, we can choose disjoint open neighborhoods $U,V$, respectively. From the assumption that $(x_n)$ converges to $x$ and $y$ respectively, there exist $M,N$ such that

$$m\geq M \implies x_m\in U,\qquad n\geq N\implies x_n\in V$$

so letting $K=\max(M,N)$, $x_K$ must belong to both $U$ and $V$ simultaneously, which is a contradiction.
:::

Meanwhile, the following lemma is also useful for showing that $X$ is Hausdorff.

::: Lemma 5
A topological space $X$ is a Hausdorff space if and only if the subset

$$\Delta_X=\{(x,x)\mid x\in X\}$$

of $X\times X$ is closed.
:::
::: Proof
First, assume $X$ is Hausdorff. Then for any $(x,y)\not\in\Delta_X$, since $x\neq y$, we can choose disjoint open neighborhoods of $x$ and $y$, denoted $U,V$. Then $U\times V$ is an open set containing $(x,y)$ and disjoint from $\Delta_X$. 

Conversely, if $\Delta_X$ is a closed set of $X\times X$, then whenever $x\neq y$ for any $x,y\in X$, we have $(x,y)\not\in\Delta_X$, and thus there exists an open neighborhood disjoint from $\Delta_X$ of $(x,y)$; considering the base of the product topology, there exists an open set of the form $U\times V$ contained in it. 
:::

More generally, by the same argument one can show that $X$ being a Hausdorff space is equivalent to the condition that, for any index set $I$, the diagonal in $X^I=\prod_{i\in I}X$,

$$\Delta_X=\{(x_i)_{i\in I}\mid\text{$x_i=x$ for all $i$, where $x\in X$}\}$$

is a closed set. From [Lemma 5](#lem5){: data-lid="tqzuv" }, the following holds.

::: Corollary 6
For continuous functions $f,g:X \rightarrow Y$, if $Y$ is Hausdorff then the set

$$E=\{x\in X\mid f(x)=g(x)\}$$

is a closed set of $X$.
:::
::: Proof
Considering the continuous function from $X$ to $Y\times Y$ given by $x\mapsto (f(x), g(x))$, the given set is the preimage under this continuous function of the closed set in $Y\times Y$, $\Delta_Y$. 
:::

::: Corollary 7
For a continuous function $f:X \rightarrow Y$, if $Y$ is Hausdorff then the set

$$\graph(f)=\{(x,f(x))\mid x\in X\}$$

is a closed set of $X\times Y$.
:::
::: Proof
It suffices to consider the two continuous functions from $X\times Y$ to $Y$,

$$(x,y)\mapsto f(x),\quad (x,y)\mapsto y$$

and apply [Corollary 6](#cor6){: data-lid="9tl6q" }. 
:::

## Subspaces and Products of Hausdorff Spaces

For any Hausdorff space $X$, it is easily verified that a subspace of $X$, $A$, is also Hausdorff. This is because, given any distinct $x,y\in A$, if we choose their disjoint open neighborhoods in $X$, $U,V$, then $U\cap A, V\cap A$ become disjoint open neighborhoods in $A$ of $x,y$. On the other hand, the product of Hausdorff spaces is also Hausdorff.

::: Proposition 8
For nonempty $X_i$, that $X=\prod_{i\in I}X_i$ is Hausdorff is equivalent to each of the $X_i$ being Hausdorff. 
:::
::: Proof
First, suppose the $X_i$ are Hausdorff and distinct $x,y\in X$ are given. Then there exists an index such that $x_i\neq y_i$, namely $i$, and inside this $X_i$, let us choose for $x_i$ and $y_i$ separating open neighborhoods $U,V$. Then, with only the $i$th components being respectively $U,V$ and the remaining $j$th components being $X_j$, considering the base of $X=\prod X_i$, these separate $x,y$. 

Conversely, if $X$ is Hausdorff, then for arbitrarily chosen elements of $X_j$, $x_j$, 

$$\prod_{j\in I} A_j,\qquad A_j=\begin{cases}X_i&i=j\\\{x_j\}&\text{otherwise}\end{cases}$$

$\prod A_j$ defined by this is homeomorphic to $X_i$ as a subset of $X$. 
:::

## Quotient Spaces of Hausdorff Spaces

In general, for a Hausdorff space $X$, the quotient space $X/R$ is not necessarily a Hausdorff space. Moreover, a necessary and sufficient condition for $X/R$ to be Hausdorff can also be easily seen: since open sets in $X/R$ correspond bijectively to $R$-saturated open sets in $X$, for $X/R$ to be Hausdorff is equivalent to the existence, for $x,y\in X$ belonging to different equivalence classes, of two disjoint $R$-saturated open sets separating them. In particular, the following holds.

::: Proposition 9
For a continuous function $f:X \rightarrow Y$, if $Y$ is Hausdorff, then with respect to the equivalence relation

$$x\sim y\iff f(x)=f(y)$$

the quotient space $X/{\sim}$ is Hausdorff.
:::

---

**References**

**[Bou]** N. Bourbaki, <i>General Topology</i>. Elements of mathematics. Springer, 1995.

---

[^1]: This is equivalent to saying that the collections of open sets containing $x$ and $y$ respectively are not the same.
