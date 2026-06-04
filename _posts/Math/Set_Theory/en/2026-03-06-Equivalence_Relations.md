---
title: "Equivalence Relations"
description: "This post covers the definition and basic properties of equivalence relations that satisfy symmetry, transitivity, and reflexivity. It examines examples of equivalence relations on sets and proves the three conditions required for a binary relation to become an equivalence relation."
excerpt: "The definition and properties of equivalence relations"

categories: [Math / Set Theory]
permalink: /en/math/set_theory/equivalence_relations
sidebar: 
    nav: "set_theory-en"

date: 2021-08-22
last_modified_at: 2022-11-26
weight: 12
translated_at: 2026-06-02T14:00:01+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-02T14:00:01+00:00
---
Now we look at equivalence relations.

## Definition of Equivalence Relations

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> A binary relation $$(R,A,A)$$ is called *symmetric* if $$x\mathrel{R}y$$ implies $$y\mathrel{R}x$$. If

$$(x\mathrel{R}y)\wedge(y\mathrel{R}z)\implies  x\mathrel{R}z$$

holds, we call it *transitive*. Finally, if $$x\mathrel{R}x$$ for all $$x$$, we say that $$R$$ is *reflexive* on $$A$$. A relation $$R$$ that is reflexive, symmetric, and transitive is called an *equivalence relation*.
</div>

If $$R$$ is an equivalence relation, we will use the notation $$x\sim_{\tiny R}y$$. When there is no risk of confusion, we also write $$x\sim y$$ or $$x\equiv y$$.

<div class="example" markdown="1">

<ins id="ex2">**Example 2**</ins> On a given set $$A$$, the relation <phrase>$x=y$</phrase> is an equivalence relation on $$A$$, and in this case $$R$$ equals the set $$\Delta_A$$. On the other hand, one can easily check that the relation <phrase>$x\in A$ and $y\in A$</phrase> is also an equivalence relation on $$A$$. The set representing this relation is exactly $$A\times A$$.

Consider an arbitrary equivalence relation $$R$$ on a set $$A$$. Since $$R$$ is reflexive, $$\Delta_A\subseteq R$$, and the inclusion $$R\subseteq A\times A$$ is obvious. Thus, among the two examples above, the first is the smallest equivalence relation that can be defined on $$A$$, and the second is the largest.

</div>

This can be summarized as follows.

<div class="proposition" markdown="1">

<ins id="prop3">**Proposition 3**</ins> A binary relation $$(R,A,A)$$ is an equivalence relation if and only if the following three conditions hold:

$$\pr_1R=A,\qquad R=R^{-1},\qquad R\circ R=R$$

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, assume that $$R$$ is an equivalence relation.  
- Since $$(x,x)\in R$$ for all $$x\in A$$, we have $$\pr_1R=A$$.  
- Also, since $$R$$ is symmetric, $$x\sim_\tiny{R} y\iff y\sim_\tiny{R}x$$ holds, and therefore

    $$(x,y)\in R\iff (y,x)\in R\iff (x,y)\in R^{-1}\tag{1}$$

    from which $$R=R^{-1}$$ follows. 
- Finally, we show that $$R\circ R=R$$. First, let $$(x,y)\in R$$ be given. Since $$R$$ is reflexive, $$(x,x)\in R$$, and thus from $$(x,x)\in R$$ and $$(x,y)\in R$$ we know that $$(x,y)\in R\circ R$$ holds. Conversely, let $$(x,y)\in R\circ R$$ be given. Then there exists some $$z\in A$$ such that $$(x,z)\in R$$ and $$(z,y)\in R$$. By the transitivity of $$R$$, we have $$(x,y)\in R$$.

Now suppose that $$R$$ is a binary relation satisfying the three given conditions.

- From $$R=R^{-1}$$, we see that $$R$$ is symmetric by reversing the logic of equation (1).
- Assume that $$x\mathrel{R}y$$ and $$y\mathrel{R}z$$ hold. Then $$(x,z)\in R\circ R=R$$, so we see that $$R$$ is transitive.
- Finally, from $$\pr_1R=A$$ we know that for each $$x$$ there exists some $$y\in A$$ such that $$(x,y)\in R$$. Since $$R$$ is symmetric, $$y\mathrel{R}x$$ also holds, and by transitivity $$(x\mathrel{R}y)\wedge(y\mathrel{R}x)\implies x\mathrel{R}x$$ holds. That is, $$R$$ is reflexive.

</details>

In this post we examine the fundamental properties of equivalence relations, and in the next post we will look at equivalence relations arising in various situations.

## Equivalence Relations and Partitions

<div class="definition" markdown="1">

<ins id="def4">**Definition 4**</ins> Consider an equivalence relation $$(R,A,A)$$. For any $$x\in A$$, the section $$R(x)$$ at $$x$$ is called the *equivalence class* of $$x$$ modulo $$R$$. The collection of such equivalence classes is called the *quotient set* of $$R$$, and is denoted by $$A/R$$.

</div>

By definition, $$R(x)$$ is the set of elements that are regarded as equivalent to $$x$$ under the equivalence relation $$R$$. In many cases, the equivalence class containing $$x$$ is written as $$[x]_R$$. When there is no risk of confusion, the set of these classes $$A/R$$ is also written as $$A/\mathord{\sim}$$.

![Quotient_set](/assets/images/Math/Set_Theory/Equivalence_Relations-1.png){:style="width:600px" class="invert" .align-center}

<cap>The set $A$ (left), the equivalence relation $R$ defined on it (center), and the quotient set $A/R$ (right). Each element of $A/R$ is the equivalence class $[x]_R$ in the middle diagram.</cap>

<div class="example" markdown="1">

<ins id="ex5">**Example 5**</ins> We have already seen that <phrase>$x=y$</phrase> is an equivalence relation on a set $$A$$. In this relation, the equivalence class of $$x$$ is the set $$\{x\}$$. In the same example, <phrase>$x\in A$ and $y\in A$</phrase> was also an equivalence relation, and in this case the equivalence class of $$x$$ becomes the whole set $$A$$.

In the preceding [Example 2](#ex2) we said that $$\Delta_A$$ is the <em-ko>smallest</em-ko> and $$A\times A$$ is the <em-ko>largest</em-ko>; however, rather than comparing them by set inclusion, it is more common to say that $$\Delta_A$$ is the *finest* equivalence relation and $$A\times A$$ is the *coarsest* equivalence relation from the above point of view. ([§Sum of Sets, ⁋Definition 1](/en/math/set_theory/sum_of_sets#def1))

</div>

<div class="proposition" markdown="1">

<ins id="lem6">**Lemma 6**</ins> For an equivalence relation $$(R,A,A)$$, define $$p:A\rightarrow A/R$$ by $$x\mapsto [x]_R$$. Then $$p$$ is a function, and $$x\sim_{\tiny R} y$$ is equivalent to $$p(x)=p(y)$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, it is not difficult to show that the map $$p$$ defined by the above formula is indeed a function. Here we only prove the equivalence of the two statements.

First, assume that $$x\sim_{\tiny R} y$$. Then from $$y\in [x]_R=R(x)$$ we have $$\{y\}\subseteq R(x)$$, and therefore by [§Operations on Binary Relations, ⁋Proposition 6](/en/math/set_theory/operation_of_binary_relations#prop6) and [Proposition 3](#prop3)

$$R(y)\subseteq R(R(x))=(R\circ R)(x)=R(x)$$

holds. Since $$R$$ is an equivalence relation, we may interchange the roles of $$x$$ and $$y$$, and thus $$R(x)=R(y)$$ holds.

Conversely, if $$[x]_R=[y]_R$$, then from $$x\in [x]_R=[y]_R$$ we obtain $$y\sim_{\tiny R} x$$, and therefore the lemma holds.

</details>

The above function $$p$$ is called the canonical projection. Then the subset $$[x]_R\subseteq A$$ of $$A$$ is the preimage of the element $$[x]_R\in A/R$$ of the quotient set under the function $$p$$, so we know that the equivalence classes are pairwise disjoint. That is, the equivalence relation $$(R,A,A)$$ induces a partition of $$A$$.

The following proposition shows that the converse also holds.

<div class="proposition" markdown="1">

<ins id="prop7">**Proposition 7**</ins> Let $$(A_i)_{i\in I}$$ be a partition of $$A$$. Then

> there exists some $$i$$ such that $$x,y\in A_i$$

is an equivalence relation on $$A$$.
</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

Write the above relation as $$R$$.

- That $$R$$ is reflexive on $$A$$ is obvious. 
- If $$x$$ and $$y$$ belong to the same set, then $$y$$ and $$x$$ also belong to the same set, so if $$x\mathrel{R}y$$ then $$y\mathrel{R}x$$. That is, $$R$$ is symmetric. 
- Finally, if $$x\mathrel{R}y$$ and $$y\mathrel{R}z$$, then $$x,y\in A_i$$ and $$y,z\in A_j$$. Since $$y\in A_i\cap A_j$$ and $$(A_i)_{i\in I}$$ is a partition, we have $$i=j$$. Therefore $$x,z\in A_i$$, and the proposition holds.

</details>



---
**References**

**[Bou]** N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---
