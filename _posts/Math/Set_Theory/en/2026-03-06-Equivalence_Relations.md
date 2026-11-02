---
title: "Equivalence Relations"
description: "This post covers the definition and basic properties of equivalence relations that satisfy symmetry, transitivity, and reflexivity. It examines examples of equivalence relations on sets and three equivalent conditions for a binary relation to be an equivalence relation, along with proofs."
excerpt: "The definition and properties of equivalence relations"

categories: [Math / Set Theory]
permalink: /en/math/set_theory/equivalence_relations
sidebar: 
    nav: "set_theory-en"

date: 2021-08-22
weight: 12
translated_at: 2026-06-02T14:00:01+00:00
translation_source: kimi-cli
last_polished_at: 2026-11-02T07:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
Now we examine equivalence relations.

## Definition of Equivalence Relations

::: Definition 1
A binary relation $(R,A,A)$ is called *symmetric* if $x\mathrel{R}y$ implies that $y\mathrel{R}x$ also holds. If

$$(x\mathrel{R}y)\wedge(y\mathrel{R}z)\implies  x\mathrel{R}z$$

holds, we call it *transitive*. Finally, if for all $x$ we have $x\mathrel{R}x$, then $R$ is said to be *reflexive* on $A$. A relation $R$ that is reflexive, symmetric, and transitive is called an *equivalence relation*.
:::

From now on, when $R$ is an equivalence relation, we will use $x\sim_{\tiny R}y$. When there is no risk of confusion, we also write $x\sim y$ or $x\equiv y$.

::: Example 2
On a given set $A$, the relation $x=y$ is an equivalence relation on $A$, and in this case $R$ equals the set $\Delta_A$. On the other hand, one can easily check that the relation '$x\in A$ and $y\in A$' is also an equivalence relation on $A$. The set representing this relation is exactly $A\times A$.

On a given set $A$, consider an arbitrary equivalence relation $R$. Since $R$ is reflexive, $\Delta_A\subseteq R$, and the inclusion $R\subseteq A\times A$ is obvious. Therefore, of the two examples given above, the first is the smallest equivalence relation that can be defined on $A$, and the second is the largest.
:::

Summarizing this in formulas, we have the following.

::: Proposition 3
A binary relation $(R,A,A)$ is an equivalence relation if and only if the following three conditions hold:

$$\pr_1R=A,\qquad R=R^{-1},\qquad R\circ R=R$$
:::
::: Proof
First, assume that $R$ is an equivalence relation.  
- For all $x\in A$, we have $(x,x)\in R$, and so $\pr_1R=A$ holds.  
- Also, since $R$ is symmetric, $x\sim_{\tiny R} y\iff y\sim_{\tiny R}x$ holds, and therefore
    
    $$(x,y)\in R\iff (y,x)\in R\iff (x,y)\in R^{-1}\tag{1}$$

    from which $R=R^{-1}$ follows. 
- Finally, we must show that $R\circ R=R$. First, let $(x,y)\in R$ be given. Since $R$ is reflexive, $(x,x)\in R$, and thus from $(x,x)\in R$ and $(x,y)\in R$ we know that $(x,y)\in R\circ R$ holds. Conversely, let $(x,y)\in R\circ R$ be given. Then there exists some $z\in A$ such that $(x,z)\in R$ and $(z,y)\in R$. Now by the transitivity of $R$, we have $(x,y)\in R$. 

Now suppose that $R$ is a binary relation satisfying the three given conditions.

- From $R=R^{-1}$, reversing the logic of equation (1) shows that $R$ is symmetric.
- Assume that $x\mathrel{R}y$ and $y\mathrel{R}z$ hold. Then $(x,z)\in R\circ R=R$, so we know that $R$ is transitive.
- Finally, from $\pr_1R=A$, we know that there exists some $y\in A$ such that $(x,y)\in R$. Now since $R$ is symmetric, $y\mathrel{R}x$ also holds, and by transitivity $(x\mathrel{R}y)\wedge(y\mathrel{R}x)\implies x\mathrel{R}x$ holds. That is, $R$ is reflexive.
:::

In this post, we examine the key properties of equivalence relations, and in the next post, we will examine equivalence relations that appear in various situations.

## Equivalence Relations and Partitions

::: Definition 4
Consider an equivalence relation $(R,A,A)$. For any $x\in A$, the section at $x$, $R(x)$, is called in $R$ the *equivalence class* of $x$. The collection of such equivalence classes is called the *quotient set* of $R$, and is denoted by $A/R$.
:::

By definition, $R(x)$ is the set of elements regarded under the equivalence relation $R$ as equivalent to $x$. In many cases, the equivalence class containing $x$ is written as $[x]_R$. When there is no risk of confusion, their set $A/R$ is also denoted by $A/\mathord{\sim}$.

{% diagram Math/Set_Theory/Equivalence_Relations-1.png width="600px" alt="Quotient_set" %}

<cap>The set $A$ (left), the equivalence relation $R$ defined on it (center), and the quotient set $A/R$ (right). Each element of $A/R$ is the equivalence class $[x]_R$ in the middle diagram.</cap>

::: Example 5
We have already seen that on a set $A$, $x=y$ is an equivalence relation. In this relation, the equivalence class of $x$ is the set $\{x\}$. Meanwhile, in the same example, the relation ‘$x\in A$ and $y\in A$’ was also an equivalence relation, in which case the equivalence class of $x$ becomes the whole of $A$. 

In the preceding [Example 2](#ex2){: data-lid="9b85j" } we said that $\Delta_A$ is the *smallest* and $A\times A$ is the *largest*; however, rather than comparing them by set inclusion, it is more common to say that $\Delta_A$ is the *finest* equivalence relation and $A\times A$ is the *coarsest* equivalence relation from the above point of view. ([§Sum of Sets, ⁋Definition 1](/en/math/set_theory/sum_of_sets#def1){: data-lid="b35w2" })
:::

::: Lemma 6
For an equivalence relation $(R,A,A)$, define $p:A\rightarrow A/R$ by $x\mapsto [x]_R$. Then $p$ is a function, and $x\sim_{\tiny R} y$ is equivalent to $p(x)=p(y)$.
:::
::: Proof
First, it is not difficult to show that $p$ defined by the above formula is indeed a function. Here we only show the equivalence.

First, assume that $x\sim_{\tiny R} y$. Then from $y\in [x]_R=R(x)$ we have $\{y\}\subseteq R(x)$, and therefore by [§Binary Relations, ⁋Proposition 5](/en/math/set_theory/binary_relation#prop5){: data-lid="lz312" }, [§Operations on Binary Relations, ⁋Proposition 6](/en/math/set_theory/operation_of_binary_relations#prop6){: data-lid="rgctz" }, and [Proposition 3](#prop3){: data-lid="yynpx" }

$$R(y)\subseteq R(R(x))=(R\circ R)(x)=R(x)$$

holds. Since $R$ is an equivalence relation, we may interchange the roles of $x$ and $y$, and thus $R(x)=R(y)$ holds.

Conversely, if $[x]_R=[y]_R$, then from $x\in [x]_R=[y]_R$ we obtain $y\sim_{\tiny R} x$, and therefore the lemma holds.
:::

The above function $p$ is called the canonical projection. Then the subset of $A$, $[x]_R\subseteq A$, is the preimage of the element $[x]_R\in A/R$ of the quotient set under the function $p$, so we know that the equivalence classes are disjoint. Also, since $R$ is reflexive, any $x\in A$ belongs to $[x]_R$, and therefore the equivalence classes are all nonempty and their union is the whole of $A$. That is, the equivalence relation $(R,A,A)$ induces a partition of $A$. ([§Sum of Sets, ⁋Definition 4](/en/math/set_theory/sum_of_sets#def4){: data-lid="mdpjf" })

The following proposition shows that the converse also holds.

::: Proposition 7
Let $(A_i)_{i\in I}$ be a partition of $A$. Then

> there exists some $i$ such that $x,y\in A_i$

is an equivalence relation with respect to $x$ and $y$.
:::

::: Proof
Write the above relation as $R$. 

- That $R$ is reflexive on $A$ is obvious. 
- If $x$ and $y$ belong to the same set, then $y$ and $x$ also belong to the same set, so if $x\mathrel{R}y$ then $y\mathrel{R}x$. That is, $R$ is symmetric. 
- Finally, if $x\mathrel{R}y$ and $y\mathrel{R}z$, then $x,y\in A_i$ and $y,z\in A_j$. But $y\in A_i\cap A_j$ and $(A_i)_{i\in I}$ is a partition, so $i=j$. Therefore $x,z\in A_i$, and the proposition holds.
:::



---
**References**

**[Bou]** N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---
