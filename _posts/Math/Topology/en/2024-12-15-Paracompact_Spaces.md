---
title: "Paracompact Spaces and Partitions of Unity"
description: "We define paracompact spaces, prove their normality, establish the existence of partitions of unity subordinate to open covers via the Shrinking Lemma, and apply them to topological manifolds."
excerpt: "Paracompact spaces, normality, partitions of unity, and topological manifolds"

categories: [Math / Topology]
permalink: /en/math/topology/paracompact_spaces
sidebar:
    nav: "topology-en"

date: 2024-12-15
weight: 17
---

## Bridging Locality and Globality

The objects we wish to handle on a topological space are usually given locally first: continuous functions defined in a neighborhood of each point, sections obtained locally, constructions placed on each coordinate patch. To patch such local data into a single global object, we need a device that smoothly vanishes each piece within its own domain of definition while distributing values so that they do not overlap across the whole space. The standard tool serving this role is the *partition of unity*, and the natural stage on which it exists is the paracompact Hausdorff space we discuss in this article.

Compactness demands that from any open cover we can extract a finite subcover ([§Compact Spaces, ⁋Definition 1](/en/math/topology/compact_spaces#def1)), but most spaces we actually deal with are not compact. Paracompactness weakens compactness appropriately by replacing finiteness with local finiteness, allowing us to revive many arguments that held for compact spaces in a local manner. We introduce this concept, show that paracompact Hausdorff spaces are normal, and then use this as a foundation to prove that a partition of unity subordinate to any open cover can always be constructed.

## Paracompact Spaces

We first name the operation of slicing an open cover into finer pieces so that each piece fits entirely inside some original piece.

::: Definition 1
Let two covers $(U_i)_{i\in I}$ and $(V_j)_{j\in J}$ of a topological space $X$ be given. The latter is called a *refinement* of the former if for every $j\in J$ there exists $i\in I$ such that $V_j\subseteq U_i$. When all elements of a refinement $(V_j)_{j\in J}$ are open sets, we call it an *open refinement*.
:::

A refinement is a much more flexible notion than a subcover. While a subcover merely selects some of the original pieces as they are, a refinement allows freely cutting each piece into smaller ones as long as each resulting piece remains contained in some original piece. Combining this with local finiteness yields a new finiteness condition that can replace compactness. Recall that a family $(A_i)_{i\in I}$ is *locally finite* if every point has a neighborhood meeting only finitely many $A_i$. ([§Interior, Closure, and Boundary, ⁋Definition 3](/en/math/topology/other_concepts#def3))

::: Definition 2
A topological space $X$ is *paracompact* if every open cover of $X$ has a locally finite open refinement.
:::

The definition demands that for any open cover, there exists a locally finite open cover refining it. Compactness demands that any open cover still covers the whole space after discarding all but finitely many sets; a cover consisting of finitely many open sets is itself locally finite, so paracompactness can be read as relaxing the finiteness required by compactness to finiteness in a neighborhood of each point.

::: Proposition 3
Any compact space is paracompact.
:::
::: Proof
Let $X$ be a compact space and let an open cover $(U_i)_{i\in I}$ be given. By compactness there exists a finite $J\subseteq I$ such that $(U_j)_{j\in J}$ still covers $X$. ([§Compact Spaces, ⁋Definition 1](/en/math/topology/compact_spaces#def1)) This finite subcover is an open refinement of the original cover, and a finite family is always locally finite, so ([§Interior, Closure, and Boundary, ⁋Definition 3](/en/math/topology/other_concepts#def3)) it is a locally finite open refinement of $(U_i)_{i\in I}$. Therefore $X$ is paracompact.
:::

That paracompactness is substantially broader than compactness must be verified on non-compact spaces. The following is a representative case, showing that even in Euclidean space, which has no finiteness at all, we can explicitly construct a locally finite refinement.

::: Example 4
Euclidean space $\mathbb{R}^n$ is paracompact. $\mathbb{R}^n$ is not compact because it is unbounded, but we can exhaust the space by open balls centered at the origin with increasing radii and obtain a locally finite refinement.

Let an arbitrary open cover $\mathcal{U}=(U_i)_{i\in I}$ be given. For each integer $k\geq 1$, let $B_k=\{x:\lVert x\rVert<k\}$ be the open ball of radius $k$, and agree that $B_0=B_{-1}=\emptyset$. Then the shells

$$A_k=\cl(B_k)\setminus B_{k-1}=\{x: k-1\leq\lVert x\rVert\leq k\}$$

are closed bounded subsets of $\mathbb{R}^n$ and hence compact by the Heine–Borel theorem, and their union is all of $\mathbb{R}^n$. Meanwhile,

$$O_k=B_{k+1}\setminus\cl(B_{k-2})$$

is an open set satisfying $A_k\subseteq O_k$. Here for $k\geq 3$ we have $O_k=\{x: k-2<\lVert x\rVert<k+1\}$, and for $k=1,2$ since $B_{k-2}=\emptyset$ we have $\cl(B_{k-2})=\emptyset$ so $O_k=B_{k+1}$.

We now treat each compact set $A_k$. Each $x\in A_k$ belongs to some $U_i$, so $x\in U_i\cap O_k$, and such open sets cover $A_k$. Since $A_k$ is compact, we can choose finitely many indices, that is, a finite set $F_k\subseteq I$, such that $(U_i\cap O_k)_{i\in F_k}$ covers $A_k$. ([§Compact Spaces, ⁋Proposition 2](/en/math/topology/compact_spaces#prop2)) Consider the family gathered over all $k\geq 1$:

$$\mathcal{V}=(U_i\cap O_k)_{k\geq 1,i\in F_k}$$

Each element is an open set contained in $U_i$, so $\mathcal{V}$ is an open refinement of $\mathcal{U}$; and since the $A_k$ cover $\mathbb{R}^n$, $\mathcal{V}$ also covers $\mathbb{R}^n$. Finally, we verify that $\mathcal{V}$ is locally finite. For a point $x$, letting $r=\lVert x\rVert$, the neighborhood $B_{r+1}=\{y:\lVert y\rVert<r+1\}$ meets $O_k$ only when $k-2<r+1$, that is, $k<r+3$, so it meets only finitely many $O_k$. For each $k$, the elements of $\mathcal{V}$ are only finitely many ($\lvert F_k\rvert$ many), so $B_{r+1}$ meets only finitely many elements of $\mathcal{V}$. Therefore $\mathcal{V}$ is a locally finite open refinement and $\mathbb{R}^n$ is paracompact.
:::

The argument of this example relies not on any special property of $\mathbb{R}^n$ but only on two properties: local compactness and exhaustion by countably many compact sets. Indeed, the same method shows that any second countable LCH space, and more generally any $\sigma$-compact LCH space, is paracompact. This forms the basis for the paracompactness of topological manifolds, which we will discuss later.

## Normality of Paracompact Hausdorff Spaces

The power of paracompactness is fully revealed when combined with the Hausdorff condition. Just as a compact Hausdorff space is normal ([§Compact Spaces, ⁋Proposition 7](/en/math/topology/compact_spaces#prop7)), we aim to show that a paracompact Hausdorff space is also normal. Once normality is secured, we can obtain abundant continuous functions via Urysohn's lemma, and this becomes the key ingredient for constructing partitions of unity. ([§Urysohn's Lemma and Tietze Extension Theorem, ⁋Theorem 2](/en/math/topology/urysohn_and_tietze#thm2))

The proof repeatedly relies on the following property of locally finite families: in a locally finite family, the closure of a union equals the union of the closures, so the closure operation freely commutes with infinite unions.

::: Lemma 5
Let $(A_i)_{i\in I}$ be a locally finite family of subsets of a topological space $X$. Then

$$\cl\Bigl(\bigcup_{i\in I} A_i\Bigr)=\bigcup_{i\in I}\cl(A_i)$$

holds.
:::
::: Proof
For each $i$, since $A_i\subseteq\bigcup_j A_j$, we have $\cl(A_i)\subseteq\cl(\bigcup_j A_j)$, and therefore $\bigcup_i\cl(A_i)\subseteq\cl(\bigcup_j A_j)$.

For the reverse inclusion, it suffices to show that $\bigcup_i\cl(A_i)$ is a closed set, for then the closure of $\bigcup_i A_i\subseteq\bigcup_i\cl(A_i)$ is also contained in $\bigcup_i\cl(A_i)$. We first observe that the family $(\cl(A_i))_{i\in I}$ is also locally finite. We can choose a neighborhood $V$ of a point $x$ such that $V$ meets only finitely many $A_i$; if we choose $V$ to be open, then whenever $V\cap\cl(A_i)\neq\emptyset$, since $V$ is a neighborhood of a point of $\cl(A_i)$ we have $V\cap A_i\neq\emptyset$. Therefore $V$ meets only finitely many $\cl(A_i)$, and $(\cl(A_i))_{i\in I}$ is also locally finite. This is a locally finite family of closed sets, so their union $\bigcup_i\cl(A_i)$ is closed. ([§Interior, Closure, and Boundary, ⁋Proposition 4](/en/math/topology/other_concepts#prop4))
:::

We first show that a paracompact Hausdorff space is regular. The skeleton of the argument is as follows: to separate a point and a closed set, we use the Hausdorff property to obtain, for each point of the closed set, an open set whose closure avoids the point in question; then we form an open cover from these together with the complement of the closed set, refine it to be locally finite using paracompactness, and control the closure using [Lemma 5](#lem5).

::: Proposition 6
Any paracompact Hausdorff space is a regular space. ([§Hausdorff Spaces, ⁋Definition 3](/en/math/topology/Hausdorff_spaces#def3))
:::
::: Proof
Let $X$ be a paracompact Hausdorff space, and let a point $a\in X$ and a closed set $B\subseteq X$ not containing $a$ be given. For each $b\in B$, since $a\neq b$, by the Hausdorff property of $X$ there exist disjoint open sets $P_b\ni a$ and $U_b\ni b$. Since $U_b\subseteq X\setminus P_b$ and $X\setminus P_b$ is closed, we have $\cl(U_b)\subseteq X\setminus P_b$, and in particular $a\notin\cl(U_b)$.

Adding the open set $X\setminus B$ to the family $(U_b)_{b\in B}$ yields an open cover of $X$. Since $X$ is paracompact, choose a locally finite open refinement $\mathcal{C}$ of this cover. Among the elements of $\mathcal{C}$, let $\mathcal{D}=\{C\in\mathcal{C}\mid C\cap B\neq\emptyset\}$ be those meeting $B$. Each element $C$ of $\mathcal{D}$ is contained in $X\setminus B$ or some $U_b$ by the refinement property; since $C$ meets $B$, it cannot be contained in $X\setminus B$, so it is contained in some $U_b$ and thus $a\notin\cl(C)$. Also, each point of $B$ belongs to some element of $\mathcal{C}$ containing it, and that element meets $B$ so it belongs to $\mathcal{D}$. That is, $\mathcal{D}$ covers $B$.

Let $V=\bigcup\mathcal{D}$; then $V$ is an open set containing $B$. Since $\mathcal{D}$ is a subfamily of the locally finite family $\mathcal{C}$, it is locally finite, and by [Lemma 5](#lem5) we have $\cl(V)=\bigcup_{C\in\mathcal{D}}\cl(C)$. Since each $\cl(C)$ does not contain $a$, we have $a\notin\cl(V)$. Then $W=X\setminus\cl(V)$ is an open set containing $a$ and disjoint from $V\supseteq B$. Therefore $a$ and $B$ are separated by neighborhoods and $X$ is regular.
:::

Expanding the same argument with the point $a$ replaced by a closed set $A$ yields normality. Here we use the regularity just proved instead of the Hausdorff property, to ensure that the closures of the open sets covering each point of $B$ avoid $A$.

::: Theorem 7
Any paracompact Hausdorff space is a normal space. ([§Hausdorff Spaces, ⁋Definition 3](/en/math/topology/Hausdorff_spaces#def3))
:::
::: Proof
Let $X$ be a paracompact Hausdorff space and let two disjoint closed sets $A,B\subseteq X$ be given. By [Proposition 6](#prop6), $X$ is regular. For each $b\in B$, since $b\notin A$, applying regularity to the point $b$ and the closed set $A$ yields disjoint open sets $U_b\ni b$ and $Q_b\supseteq A$. Since $U_b\subseteq X\setminus Q_b$ and $X\setminus Q_b$ is closed, we have $\cl(U_b)\subseteq X\setminus Q_b\subseteq X\setminus A$, that is, $\cl(U_b)\cap A=\emptyset$.

Add the open set $X\setminus B$ to the family $(U_b)_{b\in B}$ to form an open cover, and by paracompactness choose a locally finite open refinement $\mathcal{C}$; let $\mathcal{D}=\{C\in\mathcal{C}\mid C\cap B\neq\emptyset\}$. As in the proof of [Proposition 6](#prop6), each element of $\mathcal{D}$ is contained in some $U_b$ and thus satisfies $\cl(C)\cap A=\emptyset$, and $\mathcal{D}$ covers $B$.

$V=\bigcup\mathcal{D}$ is an open set containing $B$, and since $\mathcal{D}$ is locally finite, by [Lemma 5](#lem5) we have $\cl(V)=\bigcup_{C\in\mathcal{D}}\cl(C)$, which is disjoint from $A$. Therefore $W=X\setminus\cl(V)$ is an open set containing $A$ and disjoint from $V\supseteq B$. Then $V$ and $W$ are disjoint open sets containing $B$ and $A$ respectively, so $X$ is normal.
:::

[Theorem 7](#thm7) is the true generalization of the fact that a compact Hausdorff space is normal. Indeed, by [Proposition 3](#prop3) a compact space is paracompact, so the result that a compact Hausdorff space is normal is recovered as a special case of [Theorem 7](#thm7). With normality secured, we can now always obtain a continuous function separating two disjoint closed sets, and this makes the construction of partitions of unity in the next section possible.

Among the most abundant sources of paracompact spaces are metric spaces. We already know that every metric space is normal ([§Urysohn's Lemma and Tietze Extension Theorem, ⁋Proposition 4](/en/math/topology/urysohn_and_tietze#prop4)), but in fact they are always paracompact as well. This is known as A. H. Stone's theorem.

::: Theorem 8
(Stone) Any metric space is paracompact.
:::
::: Proof
We only sketch the key idea of the proof and leave the details to standard literature. **[Mun]** Let a space $X$ with metric $d$ and an open cover $(U_\alpha)_{\alpha\in J}$ be given. First, using the axiom of choice we impose a well-ordering on the index set $J$. For each integer $n\geq 1$ and each $\alpha$, from the points of $U_\alpha$ we retain only those that are at least $2^{-n}$ away from the boundary and are not already in the corresponding set for some earlier $U_\beta$ in the order, and then take the union of open balls of radius $2^{-n-1}$ centered at these remaining points to define the set $V_{n,\alpha}$. Here the well-ordering on $\alpha$ and the geometrically shrinking radii interact so that the family $(V_{n,\alpha})$ becomes an open cover refining $(U_\alpha)$ and simultaneously locally finite: for each point $x$, looking at the stage $n$ where $x$ is first covered, a neighborhood of radius about $2^{-n-1}$ meets only finitely many $V_{n',\alpha}$. Therefore $X$ is paracompact. This construction is widely known in the form recorded by M. E. Rudin.
:::

## Existence of Partitions of Unity

We now formalize the partition of unity, the tool that patches locally defined data into a global object. The *support* of a continuous function $\phi:X\rightarrow[0,1]$ is defined as $\supp\phi=\cl(\{x\in X\mid\phi(x)\neq 0\})$, which is the smallest closed set containing the region where $\phi$ takes non-zero values.

::: Definition 9
A family $(\phi_i)_{i\in I}$ of continuous functions on a topological space $X$ is called a *partition of unity* if each $\phi_i:X\rightarrow[0,1]$ satisfies the following two conditions.

1. The family $(\supp\phi_i)_{i\in I}$ is locally finite.
2. For every $x\in X$, $\sum_{i\in I}\phi_i(x)=1$ holds.

Furthermore, given an open cover $(U_i)_{i\in I}$ of $X$, a partition of unity $(\phi_i)_{i\in I}$ with the same index set is called *subordinate to* $(U_i)$ if $\supp\phi_i\subseteq U_i$ for all $i$.
:::

The local finiteness in the first condition ensures that the sum $\sum_i\phi_i(x)$ in the second condition reduces to a finite sum in some neighborhood of each point, so it actually makes sense. The subordination condition $\supp\phi_i\subseteq U_i$ means that each $\phi_i$ vanishes not only outside $U_i$ but even near the boundary of $U_i$, so multiplying locally defined data on $U_i$ by $\phi_i$ allows us to extend the product continuously to all of $X$ by filling in $0$ outside $U_i$. This is the principle by which a partition of unity globalizes local constructions.

The key to the existence proof is that normality alone is not sufficient; we need to "shrink" the cover twice so that closed sets still cover the whole space. We first prepare a lemma for this purpose. A family $(U_i)_{i\in I}$ is *point-finite* if each point $x\in X$ belongs to only finitely many $U_i$; a locally finite family is always point-finite.

::: Lemma 10
(Shrinking lemma) Let $(U_\alpha)_{\alpha\in J}$ be a point-finite open cover of a normal space $X$. Then there exists an open cover $(V_\alpha)_{\alpha\in J}$ such that $\cl(V_\alpha)\subseteq U_\alpha$ for all $\alpha$.
:::
::: Proof
Using the axiom of choice, we impose a well-ordering on the index set $J$. We define open sets $V_\alpha$ for each $\alpha\in J$ by transfinite induction, maintaining the following invariant at every stage:

$$(\ast_\alpha)\qquad \{V_\beta\mid\beta<\alpha\}\cup\{U_\beta\mid\beta\geq\alpha\}\ \text{covers}\ X.$$

We first verify that $(\ast_\alpha)$ holds for arbitrary $\alpha$ from point-finiteness. Suppose that for each $\beta<\alpha$, $V_\beta$ has already been defined satisfying $\cl(V_\beta)\subseteq U_\beta$. Given a point $x\in X$, it belongs to only finitely many $U_\gamma$. If among these there is one with $\gamma\geq\alpha$, then $x$ is covered by $U_\gamma$. Otherwise, all $\gamma$ with $x\in U_\gamma$ are less than $\alpha$; let $\gamma_0$ be the largest among them. By the already valid $(\ast_{\gamma_0})$, $x$ is covered by either some $V_\beta$ with $\beta\leq\gamma_0$ or some $U_\beta$ with $\beta>\gamma_0$; but by maximality of $\gamma_0$, if $\beta>\gamma_0$ then $x\notin U_\beta$, so $x$ is covered by some $V_\beta$ with $\beta\leq\gamma_0<\alpha$. In any case, $x$ is covered by the family in $(\ast_\alpha)$, so $(\ast_\alpha)$ holds.

Now, assuming $V_\beta$ has been defined for $\beta<\alpha$, we define $V_\alpha$. The set

$$C_\alpha=X\setminus\Bigl(\bigcup_{\beta<\alpha}V_\beta\cup\bigcup_{\beta>\alpha}U_\beta\Bigr)$$

is closed. By $(\ast_\alpha)$, points outside this complement, that is, points of $C_\alpha$, do not belong to any $V_\beta$ with $\beta<\alpha$ or any $U_\beta$ with $\beta>\alpha$, so they must belong to $U_\alpha$. That is, $C_\alpha\subseteq U_\alpha$. Since $X$ is normal, for the closed set $C_\alpha$ and the open set $U_\alpha$ containing it, there exists an open set $V_\alpha$ such that $C_\alpha\subseteq V_\alpha\subseteq\cl(V_\alpha)\subseteq U_\alpha$. ([§Urysohn's Lemma and Tietze Extension Theorem, ⁋Lemma 1](/en/math/topology/urysohn_and_tietze#lem1)) Then since $C_\alpha\subseteq V_\alpha$, the family $\{V_\beta\mid\beta\leq\alpha\}\cup\{U_\beta\mid\beta>\alpha\}$ covers $X$, continuing the invariant to the next stage.

Finally, we show that the $(V_\alpha)_{\alpha\in J}$ obtained in this way covers $X$. Since the $U_\gamma$ containing a point $x$ are only finitely many, let $\gamma_0$ be the largest index among them; then by $(\ast_{\gamma_0})$ and the maximality of $\gamma_0$, as before, $x$ is covered by some $V_\beta$ with $\beta\leq\gamma_0$. Therefore $(V_\alpha)_{\alpha\in J}$ is an open cover of $X$ satisfying $\cl(V_\alpha)\subseteq U_\alpha$ for each $\alpha$.
:::

Note that point-finiteness was used crucially to maintain the covering property at the limit stages and the final stage of the transfinite induction. With only a well-ordering, there would be a risk that some point is not covered when infinitely many $U_\beta$ are replaced by $V_\beta$ all at once, but the fact that each point belongs to only finitely many pieces pins down the stage at which it is covered to a finite one. We are now ready to prove the main theorem.

::: Theorem 11
For any open cover $(U_\alpha)_{\alpha\in J}$ of a paracompact Hausdorff space $X$, there exists a partition of unity subordinate to $(U_\alpha)$.
:::
::: Proof
The proof consists of four steps. First, we refine the cover to a locally finite one with the same index set; then we shrink this twice to obtain a closed cover; next we construct bump functions for each piece using Urysohn's lemma; and finally we normalize them.

**(1) Precise locally finite refinement.** Since $X$ is paracompact, there exists a locally finite open refinement $(W_\beta)_{\beta\in K}$ of $(U_\alpha)$. By the definition of refinement, for each $\beta$ we can choose $\alpha(\beta)\in J$ such that $W_\beta\subseteq U_{\alpha(\beta)}$. Now for each $\alpha\in J$ define

$$V_\alpha=\bigcup\{W_\beta\mid\alpha(\beta)=\alpha\}$$

(if there is no such $\beta$, set $V_\alpha=\emptyset$). Then $V_\alpha$ is an open set with $V_\alpha\subseteq U_\alpha$, and since the $W_\beta$ cover $X$, $(V_\alpha)_{\alpha\in J}$ also covers $X$. Moreover, if a neighborhood of a point $x$ meets only finitely many $W_\beta$, then it meets only finitely many $V_\alpha$ (since a neighborhood meeting $V_\alpha$ must meet some $W_\beta$ with $\alpha(\beta)=\alpha$), so $(V_\alpha)_{\alpha\in J}$ is locally finite. Thus we have obtained a locally finite open cover with the same index set $J$ satisfying $V_\alpha\subseteq U_\alpha$.

**(2) Two shrinkings.** $X$ is normal by [Theorem 7](#thm7), and the locally finite $(V_\alpha)$ is point-finite. Apply [Lemma 10](#lem10) to $(V_\alpha)$ to obtain an open cover $(P_\alpha)_{\alpha\in J}$ with $\cl(P_\alpha)\subseteq V_\alpha$ for all $\alpha$. Since $P_\alpha\subseteq V_\alpha$, $(P_\alpha)$ is also point-finite, and applying [Lemma 10](#lem10) again to $(P_\alpha)$ yields an open cover $(Q_\alpha)_{\alpha\in J}$ with $\cl(Q_\alpha)\subseteq P_\alpha$ for all $\alpha$. In summary, both covers $(P_\alpha)$ and $(Q_\alpha)$ cover $X$ and satisfy

$$\cl(Q_\alpha)\subseteq P_\alpha\subseteq\cl(P_\alpha)\subseteq V_\alpha\subseteq U_\alpha$$

for all $\alpha$.

**(3) Bump functions.** For each $\alpha$, the sets $\cl(Q_\alpha)$ and $X\setminus P_\alpha$ are two disjoint closed sets. Since $X$ is normal, by Urysohn's lemma there exists a continuous function $\psi_\alpha:X\rightarrow[0,1]$ taking the value $1$ on $\cl(Q_\alpha)$ and $0$ on $X\setminus P_\alpha$. ([§Urysohn's Lemma and Tietze Extension Theorem, ⁋Theorem 2](/en/math/topology/urysohn_and_tietze#thm2)) Then $\{x\mid\psi_\alpha(x)\neq 0\}\subseteq P_\alpha$, so

$$\supp\psi_\alpha=\cl(\{x\mid\psi_\alpha(x)\neq 0\})\subseteq\cl(P_\alpha)\subseteq V_\alpha\subseteq U_\alpha$$

In particular, $(\supp\psi_\alpha)_{\alpha\in J}$ is locally finite since $\supp\psi_\alpha\subseteq V_\alpha$ and $(V_\alpha)$ is locally finite.

**(4) Normalization.** Since the family $(\psi_\alpha)$ has locally finite support, for each point $x$ there is a neighborhood where only finitely many $\psi_\alpha$ are non-zero. On that neighborhood the sum $\psi=\sum_{\alpha\in J}\psi_\alpha$ is a finite sum, and a finite sum of continuous functions is continuous, so $\psi$ is continuous on that neighborhood. Since continuity is a local property, $\psi:X\rightarrow\mathbb{R}$ is a continuous function. Also, since $(Q_\alpha)$ covers $X$, any $x$ belongs to some $Q_\alpha$, and then $\psi_\alpha(x)=1$ on $\cl(Q_\alpha)$, so $\psi(x)\geq 1>0$. Therefore, defining

$$\phi_\alpha=\frac{\psi_\alpha}{\psi}$$

each $\phi_\alpha:X\rightarrow[0,1]$ is a continuous function (since $\psi$ is nowhere zero). Since $\psi>0$, we have $\{x\mid\phi_\alpha(x)\neq 0\}=\{x\mid\psi_\alpha(x)\neq 0\}$, and thus $\supp\phi_\alpha=\supp\psi_\alpha\subseteq U_\alpha$ and $(\supp\phi_\alpha)$ is locally finite. Finally, for each $x$,

$$\sum_{\alpha\in J}\phi_\alpha(x)=\frac{1}{\psi(x)}\sum_{\alpha\in J}\psi_\alpha(x)=\frac{\psi(x)}{\psi(x)}=1$$

Therefore $(\phi_\alpha)_{\alpha\in J}$ is a partition of unity subordinate to $(U_\alpha)$.
:::

::: Remark 12
The converse of [Theorem 11](#thm11) also holds. Let a space $X$ be given such that for any open cover $(U_i)_{i\in I}$ there exists a subordinate partition of unity $(\phi_i)_{i\in I}$. Then the open sets $G_i=\{x\mid\phi_i(x)>0\}$ satisfy $G_i\subseteq\supp\phi_i\subseteq U_i$, so they form an open refinement of $(U_i)$; since $(\supp\phi_i)$ is locally finite, $(G_i)$ is also locally finite; and from $\sum_i\phi_i(x)=1$, for each $x$ there exists $i$ with $\phi_i(x)>0$, so $(G_i)$ covers $X$. Therefore $X$ is paracompact. Together with the Hausdorff condition, this yields the fact that a topological space is paracompact Hausdorff if and only if every open cover admits a subordinate partition of unity.
:::

## Globalizing Local Constructions

Once a partition of unity is available, the standard procedure for patching locally defined data into a global object opens up. In this section we illustrate the principle with the case of continuous functions.

::: Example 13
Let an open cover $(U_\alpha)_{\alpha\in J}$ of a paracompact Hausdorff space $X$ be given, and let continuous functions $f_\alpha:U_\alpha\rightarrow\mathbb{R}$ defined only on each $U_\alpha$ be given. By [Theorem 11](#thm11), choose a partition of unity $(\phi_\alpha)_{\alpha\in J}$ subordinate to $(U_\alpha)$. For each $\alpha$, the product $\phi_\alpha f_\alpha$ is continuous on $U_\alpha$; since $\supp\phi_\alpha\subseteq U_\alpha$ is a closed set of $X$, we can extend this product continuously to all of $X$ by setting it to $0$ outside $U_\alpha$. Writing this extension again as $\phi_\alpha f_\alpha$, since the family $(\supp\phi_\alpha)$ is locally finite,

$$f=\sum_{\alpha\in J}\phi_\alpha f_\alpha$$

reduces to a finite sum in a neighborhood of each point and defines a continuous function on all of $X$. Here $f$ is the global function obtained by averaging the local data $(f_\alpha)$ with the weights of the partition of unity. Conversely, given any continuous function $g$ on $X$, we have $g=\sum_\alpha\phi_\alpha g$, so $g$ is decomposed into pieces $\phi_\alpha g$ on $U_\alpha$.
:::

The stage where this construction is most essentially used is topological manifolds. In this section we define topological manifolds and verify that they always admit the partitions of unity from the previous section. The model for a topological manifold is the familiar Euclidean space $\mathbb{R}^m$, and a topological manifold is a space that locally resembles this model.

## Topological Manifolds

::: Definition 14
A topological space $M$ is *locally Euclidean of dimension $m$* if for every $x\in M$ there exists an open neighborhood $U$ of $x$ such that $U$ is homeomorphic to an open subset of $\mathbb{R}^m$.
:::

The locally Euclidean condition captures the local essence of a topological manifold, but by itself it is too weak; we add two global conditions.

::: Definition 15
A space that is second countable, Hausdorff, and locally Euclidean of dimension $m$ is called a *topological manifold of dimension $m$*.
:::

The reasons for requiring Hausdorff and second countability are revealed in the following theorem. This theorem tells us that in a locally Euclidean space, second countability is essentially the same condition as paracompactness, thereby confirming that a topological manifold sits exactly on the stage of partitions of unity prepared in the previous section.

::: Theorem 16
For a Hausdorff and locally Euclidean topological space $M$, the following are equivalent: $M$ is second countable; and $M$ is paracompact and has countably many connected components. ([§Connected Spaces, ⁋Definition 7](/en/math/topology/connected_spaces#def7))
:::
::: Proof
We only sketch the key idea and follow **[Lee]** for the details. From the locally Euclidean condition, each point has a neighborhood homeomorphic to an open subset of $\mathbb{R}^m$, so the space behaves like a locally compact space at each point. If it is second countable, we can generalize the exhaustion argument of [Example 4](#ex4) to cover $M$ by countably many relatively compact open sets, and from this we obtain a locally finite refinement in the same manner as in [Proposition 3](#prop3), yielding that $M$ is paracompact and has countably many components. Conversely, if $M$ is paracompact and has countably many components, then each component is Lindelöf and hence has a countable base, so $M$ is second countable.
:::

As a direct consequence of this theorem, any topological manifold $M$ is a paracompact Hausdorff space, and therefore by [Theorem 11](#thm11) there exists a partition of unity subordinate to any coordinate cover of $M$. Thanks to this fact, objects defined in the language of Euclidean space on each coordinate patch can be patched together to the whole manifold, and this is the reason why partitions of unity are an essential tool in manifold theory and bundle theory.

---

**References**

**[Mun]** J. R. Munkres, *Topology*, 2nd ed., Prentice Hall, 2000.

**[Wil]** S. Willard, *General Topology*, Addison-Wesley, 1970.

**[Lee]** J. M. Lee, *Introduction to Topological Manifolds*, 2nd ed., Springer, 2011.

