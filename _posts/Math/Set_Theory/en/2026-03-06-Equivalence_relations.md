---

title: "Equivalence Relations"
excerpt: "Definition and properties of equivalence relations"

categories: [Math / Set Theory]
permalink: /en/math/set_theory/equivalence_relations
header:
    overlay_image: /assets/images/Math/Set_Theory/Equivalence_relations.png
    overlay_filter: 0.5
sidebar: 
    nav: "set_theory-en"

date: 2026-03-06
last_modified_at: 2026-03-06
weight: 12

---

We now turn our attention to equivalence relations.

## Definition of Equivalence Relations

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> A binary relation $$(R,A,A)$$ is *symmetric* if $$x\mathrel{R}y$$ implies $$y\mathrel{R}x$$. If

$$(x\mathrel{R}y)\wedge(y\mathrel{R}z)\implies  x\mathrel{R}z$$

holds, then it is called *transitive*. Finally, if $$x\mathrel{R}x$$ for all $$x$$, then $$R$$ is *reflexive* on $$A$$. A relation $$R$$ that is reflexive, symmetric, and transitive is called an *equivalence relation*.
</div>

Hereafter, when $$R$$ is an equivalence relation, we will use $$x\sim_{\tiny R}y$$. When there is no risk of confusion, we may also write $$x\sim y$$ or $$x\equiv y$$.

<div class="example" markdown="1">

<ins id="ex2">**Example 2**</ins> On a given set $$A$$, the relation <phrase>$$x=y$$</phrase> is an equivalence relation on $$A$$, and in this case $$R$$ is the same as the set $$\Delta_A$$. On the other hand, the relation <phrase>$$x\in A$$ and $$y\in A$$</phrase> can easily be verified to also be an equivalence relation on $$A$$. The set representing this relation is exactly $$A\times A$$.

Consider any equivalence relation $$R$$ on a set $$A$$. Since $$R$$ is reflexive, $$\Delta_A\subseteq R$$, and the inclusion $$R\subseteq A\times A$$ is clear. Thus the first of the two examples above is the smallest equivalence relation that can be defined on $$A$$, and the second is the largest.

</div>

This can be summarized as follows.

<div class="proposition" markdown="1">

<ins id="prop3">**Proposition 3**</ins> A binary relation $$(R,A,A)$$ is an equivalence relation if and only if the following three conditions hold:

$$\pr_1R=A,\qquad R=R^{-1},\qquad R\circ R=R$$

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, assume $$R$$ is an equivalence relation.
- Since $$(x,x)\in R$$ for all $$x\in A$$, $$\pr_1R=A$$ holds.
- Also, since $$R$$ is symmetric, $$x\sim_\tiny{R} y\iff y\sim_\tiny{R}x$$ holds, and thus from
    
    $$(x,y)\in R\iff (y,x)\in R\iff (x,y)\in R^{-1}\tag{1}$$

    we obtain $$R=R^{-1}$$.
- Finally, we need to show $$R\circ R=R$$. First, let $$(x,y)\in R$$ be arbitrary. Since $$R$$ is reflexive, $$(x,x)\in R$$, and from $$(x,x)\in R$$ and $$(x,y)\in R$$, we see that $$(x,y)\in R\circ R$$. Conversely, let $$(x,y)\in R\circ R$$ be arbitrary. Then there exists $$z\in A$$ such that $$(x,z)\in R$$ and $$(z,y)\in R$$. By transitivity of $$R$$, $$(x,y)\in R$$ holds.

Now suppose a binary relation $$R$$ satisfying the three given conditions is provided.

- From $$R=R^{-1}$$, by reversing the logic in equation (1), we see that $$R$$ is symmetric.
- Assume $$x\mathrel{R}y$$ and $$y\mathrel{R}z$$ hold. Then $$(x,z)\in R\circ R=R$$, so $$R$$ is transitive.
- Finally, from $$\pr_1R=A$$, we know there exists $$y\in A$$ such that $$(x,y)\in R$$. Now since $$R$$ is symmetric, $$y\mathrel{R}x$$ also holds, and by transitivity, $$(x\mathrel{R}y)\wedge(y\mathrel{R}x)\implies x\mathrel{R}x$$ holds. That is, $$R$$ is reflexive.

</details>

In this post, we will explore the fundamental properties of equivalence relations, and in the next post, we will examine equivalence relations that appear in various contexts.

## Equivalence Relations and Partitions

<div class="definition" markdown="1">

<ins id="def4">**Definition 4**</ins> Consider an equivalence relation $$(R,A,A)$$. For any $$x\in A$$, the section $$R(x)$$ at $$x$$ is called the *equivalence class* of $$x$$ under $$R$$. The collection of such equivalence classes is called the *quotient set* of $$R$$, denoted by $$A/R$$.

</div>

By definition, $$R(x)$$ is the collection of elements that are considered equivalent to $$x$$ under the equivalence relation $$R$$. In many cases, the equivalence class containing $$x$$ is written as $$[x]_R$$. When there is no risk of confusion, their set $$A/R$$ may also be denoted as $$A/\mathord{\sim}$$.

![Quotient_set](/assets/images/Math/Set_Theory/Equivalence_relations-1.png){:style="width:600px" class="invert" .align-center}

<cap>Set $$A$$ (left), equivalence relation $$R$$ defined on it (center), and quotient set $$A/R$$ (right). Each element of $$A/R$$ is an equivalence class $$[x]_R$$ from the middle figure.</cap>

<div class="example" markdown="1">

<ins id="ex5">**Example 5**</ins> We have already seen that <phrase>$$x=y$$</phrase> on a set $$A$$ is an equivalence relation. In this relation, the equivalence class of $$x$$ is the set $$\{x\}$$. On the other hand, in the same example, <phrase>$$x\in A$$ and $$y\in A$$</phrase> was also an equivalence relation, in which case the equivalence class of $$x$$ is the entire set $$A$$.

In [Example 2](#ex2), we said $$\Delta_A$$ is the *smallest* and $$A\times A$$ is the *largest*, but rather than comparing set inclusions, it is more common to say that $$\Delta_A$$ is the *finest* equivalence relation and $$A\times A$$ is the *coarsest* equivalence relation, following this perspective. ([§Sum of Sets, ⁋Definition 1](/en/math/set_theory/sum_of_sets#def1))

</div>

<div class="proposition" markdown="1">

<ins id="lem6">**Lemma 6**</ins> For an equivalence relation $$(R,A,A)$$, define $$p:A\rightarrow A/R$$ by $$x\mapsto [x]_R$$. Then $$p$$ is a function, and $$x\sim_{\tiny R} y$$ is equivalent to $$p(x)=p(y)$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

It is not difficult to show that $$p$$ as defined above is indeed a function. Here we only prove the equivalence.

First, assume $$x\sim_{\tiny R} y$$. From $$y\in [x]_R=R(x)$$, we have $$\{y\}\subseteq R(x)$$, and thus by [§Operations on Binary Relations, ⁋Proposition 6](/en/math/set_theory/operation_of_binary_relations#prop6) and [Proposition 3](#prop3),

$$R(y)\subseteq R(R(x))=(R\circ R)(x)=R(x)$$

holds. Since $$R$$ is an equivalence relation, we can swap the roles of $$x$$ and $$y$$, and thus $$R(x)=R(y)$$ holds.

Conversely, if $$[x]_R=[y]_R$$, then from $$x\in [x]_R=[y]_R$$, we obtain $$y\sim_{\tiny R} x$$, and thus the lemma holds.

</details>

The function $$p$$ above is called the canonical projection. Since the subset $$[x]_R\subseteq A$$ is the preimage under $$p$$ of the element $$[x]_R\in A/R$$, we see that equivalence classes are pairwise disjoint. In other words, an equivalence relation $$(R,A,A)$$ induces a partition of $$A$$.

The following proposition shows that the converse also holds.

<div class="proposition" markdown="1">

<ins id="prop7">**Proposition 7**</ins> Let $$(A_i)_{i\in I}$$ be a partition of $$A$$. Then the relation

> there exists some $$i$$ such that $$x,y\in A_i$$

is an equivalence relation on $$x$$ and $$y$$.
</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

Let us denote the above relation by $$R$$.

- It is clear that $$R$$ is reflexive on $$A$$.
- If $$x$$ and $$y$$ belong to the same set, then $$y$$ and $$x$$ also belong to the same set, so $$x\mathrel{R}y$$ implies $$y\mathrel{R}x$$. Thus $$R$$ is symmetric.
- Finally, if $$x\mathrel{R}y$$ and $$y\mathrel{R}z$$, then $$x,y\in A_i$$ and $$y,z\in A_j$$. Since $$y\in A_i\cap A_j$$ and $$(A_i)_{i\in I}$$ is a partition, $$i=j$$. Thus $$x,z\in A_i$$, and the proposition holds.

</details>



---
**References**

**[Bou]** N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---
