---
title: "Quotient Spaces"
description: "This post explains how to introduce the quotient space topology on a set equipped with an equivalence relation, and summarizes the basic structure of quotient spaces along with the locally closed property of subspaces."
excerpt: "Properties of Subspaces"

categories: [Math / Topology]
permalink: /en/math/topology/quotient_spaces
sidebar: 
    nav: "topology-en"

date: 2022-11-17
last_modified_at: 2022-11-17
weight: 10
translated_at: 2026-06-03T04:30:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-03T04:30:02+00:00
---
Now we examine how to define a topology on a quotient set. ([[Set Theory] §Equivalence Relations, ⁋Definition 6](/en/math/set_theory/equivalence_relations#def6))

## Locally closed subspace

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> Let $$X$$ be a topological space. A subset $$A$$ is called *locally closed* at $$x\in A$$ if there exists a neighborhood $$V$$ of $$x$$ in $$X$$ such that $$A\cap V$$ is closed in $$V$$. If $$A$$ is locally closed at every $$x\in A$$, then we call $$A$$ itself locally closed.

</div>

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> For a topological space $$X$$ and a subset $$A$$, the following are all equivalent.

1. $$A$$ is locally closed in $$X$$.
2. $$A$$ is the intersection of an open set and a closed set in $$X$$.
3. $$A$$ is open in its closure $$\cl A$$ (in $$X$$).

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, suppose $$A$$ is locally closed, and for each $$x\in A$$ let $$V_x$$ be an open neighborhood of $$x$$ in $$X$$ satisfying the condition of [Definition 1](#def1). Then $$U=\bigcup_{x\in A} V_x$$ is an open set. Also, by applying [§Subspaces, ⁋Proposition 6](/en/math/topology/subspaces#prop6), we see that $$A$$ is closed in $$U$$. Thus $$A=U\cap C$$ for some closed set $$C$$ in $$X$$, so the second condition holds.

Now suppose $$A=U\cap C$$ holds for an open set $$U$$ and a closed set $$C$$ in $$X$$. Then $$\cl A\subseteq C$$, so

$$A\subseteq U\cap\cl A\subseteq U\cap C=A$$

holds, and in particular $$A=U\cap\cl A$$. From this we see that $$A$$ is open in $$\cl A$$.

Finally, if there exists an open set $$U$$ in $$X$$ satisfying $$A=U\cap\cl A$$, then $$A$$ is closed in $$U$$ and hence locally closed.

</details>

In particular, from condition 2, if a continuous function $$f:X\rightarrow Y$$ and a locally closed subset $$B$$ of $$Y$$ are given, then $$f^{-1}(B)$$ is also locally closed in $$X$$.

## Quotient Spaces

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> Let a topological space $$X$$ be given, and let $$R$$ be an equivalence relation on the set $$X$$. Then the *quotient space* of $$X$$ by $$R$$ means the space $$X/R$$ equipped with the final topology defined by the canonical projection $$p:X\rightarrow X/R$$.

</div>

By [§Initial and Final Topology, ⁋Proposition 5](/en/math/topology/initial_and_final_topology#prop5), the open sets in $$X/R$$ are exactly those sets $$U$$ such that $$p^{-1}(U)$$ is open in $$X$$.[^1] Rewriting this in the language of [[Set Theory] §Examples of Equivalence Relations, ⁋Definition 5](/en/math/set_theory/examples_of_equivalence#def5), we can verify that the open sets on $$X/R$$ correspond bijectively to the open sets of $$X$$ that are *saturated* with respect to $$R$$.

Meanwhile, by [§Initial and Final Topology, ⁋Proposition 6](/en/math/topology/initial_and_final_topology#prop6), the following holds.

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4**</ins> Let a topological space $$X$$, a quotient space $$X/R$$, and the canonical projection $$p:X\rightarrow X/R$$ be given. For any topological space $$Y$$, a function $$f:X/R\rightarrow Y$$ is continuous if and only if $$f\circ p$$ is a continuous function from $$X$$ to $$Y$$.

</div>

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> Consider a topological space $$X$$ and two equivalence relations $$R,S$$ defined on $$X$$. If $$S$$ is a finer equivalence relation than $$R$$, then the bijection $$(X/S)/(R/S)\rightarrow X/R$$ is a homeomorphism for the equivalence relation $$R/S$$ defined on $$X/S$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

That $$(X/S)/(R/S)\rightarrow X/R$$ is a bijection was already shown in [[Set Theory] §Examples of Equivalence Relations, ⁋Definition 8](/en/math/set_theory/examples_of_equivalence#def8). By [Proposition 4](#prop4), the continuity of this function is equivalent to the continuity of $$X/S\rightarrow X/R$$, and the continuity of this function in turn follows from the continuity of $$X\rightarrow X/R$$.

Similarly, the continuity of $$X/R\rightarrow(X/S)/(R/S)$$ is obtained from the continuity of $$X\rightarrow(X/S)/(R/S)$$, and this function is the composition of two continuous functions

$$X\longrightarrow X/S\longrightarrow (X/S)/(R/S)$$

so it is continuous.

</details>

Meanwhile, let topological spaces $$X,Y$$ and a continuous function $$f:X\rightarrow Y$$ be given, and consider the equivalence relation $$R$$ defined by $$f$$. ([[Set Theory] §Equivalence Relations, ⁋Definition 5](/en/math/set_theory/equivalence_relations#def5)) Then we may consider the canonical decomposition of $$f$$

$$X\overset{p}{\longrightarrow}X/R\overset{\bar{f}}{\longrightarrow}f(X)\overset{i}{\longrightarrow}Y$$

Now if we give $$f(X)$$ the subspace topology, it is immediate from [Proposition 4](#prop4) and [§Initial and Final Topology, ⁋Proposition 3](/en/math/topology/initial_and_final_topology#prop3) that $$\bar{f}$$ is continuous. Also, by the definition of the canonical decomposition, $$\bar{f}$$ is a bijection. In general $$\bar{f}$$ need not be a homeomorphism ([§Continuous Functions, ⁋Example 5](/en/math/topology/continuous_functions#ex5)), but the following holds.

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6**</ins> For the above diagram, the following are equivalent.

1. $$\bar{f}$$ is a homeomorphism from $$X/R$$ onto $$f(X)$$.
2. For an open set $$U\subseteq X$$ saturated with respect to $$R$$, $$f(U)$$ is open in $$f(X)$$.
3. For a closed set $$C\subseteq X$$ saturated with respect to $$R$$, $$f(C)$$ is closed in $$f(X)$$.

</div>

This is obvious because the second or third condition exactly means that $$\bar{f}^{-1}$$ is also continuous.

Meanwhile, in the same situation as above, suppose there exists a *continuous* section $$s:Y\rightarrow X$$ of $$f$$. Then $$f$$ is surjective, so $$i=\id_Y$$. Now both $$\bar{f}$$ and $$p\circ s$$ are continuous, and

$$\bar{f}\circ(p\circ s)=f\circ s=\id_Y$$

and composing $$\bar{f}^{-1}$$ on the left and $$\bar{f}$$ on the right of the above equation, respectively, we obtain

$$(p\circ s)\circ\bar{f}=\id_{X/R}$$

Therefore, in this case $$\bar{f}$$ is a homeomorphism.

## Quotient Spaces and Subspaces

Now consider a topological space $$X$$, a subset $$A$$, and an equivalence relation $$R$$ given on $$X$$. Letting $$p:X\rightarrow X/R$$ be the canonical projection, the canonical decomposition of $$p\vert_A:A\rightarrow X/R$$

$$A\overset{q}{\longrightarrow}A/(R|_A)\overset{\overline{(p|_A)}}{\longrightarrow} f(A)\overset{j}{\longrightarrow}X/R$$

is defined, and by the same argument as above $$\overline{(p\vert_A)}$$ is a continuous bijection. The following proposition is also almost obvious.

<div class="proposition" markdown="1">

<ins id="prop7">**Proposition 7**</ins> In the above decomposition, the following are all equivalent.

1. $$\overline{(p\vert_A)}$$ is a homeomorphism.
2. An open set $$U\subseteq A$$ that is $$R\vert_A$$-saturated is the intersection of an open set in $$X$$ that is $$R$$-saturated with $$A$$.
3. A closed set $$C\subseteq A$$ that is $$R\vert_A$$-saturated is the intersection of a closed set in $$X$$ that is $$R$$-saturated with $$A$$.

</div>




[^1]: Just as in [§Subspaces], **[Mun]** takes this as the definition of the quotient topology.
