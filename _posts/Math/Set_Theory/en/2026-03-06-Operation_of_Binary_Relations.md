---
title: "Operations on Binary Relations"
description: "We define the inverse and composition of binary relations, prove properties of the inverse and the associativity of composition, and discuss a proposition about the inverse of the composition of two binary relations."
excerpt: "Inverse and Composition of Binary Relations"

categories: [Math / Set Theory]
permalink: /en/math/set_theory/operation_of_binary_relations


sidebar: 
    nav: "set_theory-en"

date: 2022-11-22
last_modified_at: 2022-11-22

weight: 4
translated_at: 2026-06-02T19:00:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-02T19:00:02+00:00
---
We now define the inverse of a binary relation, and the composition of binary relations.

## Inverse of Binary Relations

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> Let $$R$$ be a binary relation. Then the binary relation consisting of all $$(y,x)$$ such that $$(x,y)\in R$$ is called the *inverse* of $$R$$, and is denoted by $$R^{-1}$$. Also, the set $$R^{-1}(X)$$ is called the *preimage* of $$X$$. If $$R^{-1}=R$$, then $$R$$ is said to be *symmetric*.

</div>

Explicitly, $$R^{-1}$$ is the set for which the formula

$$(x,y)\in R\iff (y,x)\in R^{-1}$$

holds. 

The set $$R^{-1}(X)$$ can be viewed either as the preimage of $$X$$ under the binary relation $$R$$, or as the image of $$X$$ under the inverse relation $$R^{-1}$$. However, by the definition of $$R^{-1}$$, whichever viewpoint we adopt yields the same set, so there is no danger of confusion.

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> The inverse of $$R^{-1}$$ is $$R$$. Moreover, $$\pr_1R^{-1}=\pr_2R$$ and $$\pr_2R^{-1}=\pr_1R$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

The first claim is immediate from the formula

$$(x,y)\in R\iff (y,x)\in R^{-1}\iff (x,y)\in (R^{-1})^{-1}$$ 

For the second claim, suppose $$x\in\pr_1R^{-1}$$. Then there exists some $$y$$ such that $$(x,y)\in R^{-1}$$. Since $$(y,x)\in R$$, we have $$x\in\pr_2R$$. Reversing this argument proves that $$\pr_2R\subset\pr_1R^{-1}$$.

For the remaining equality $$\pr_2R^{-1}=\pr_1R$$, it suffices to replace $$R$$ by $$R^{-1}$$ in the claim just proved.   

</details>

For given sets $$A,B$$, the product $$A\times B$$ was the largest binary relation having $$A$$ as source and $$B$$ as target. Thus, from the two equalities

$$\pr_1(A\times B)^{-1}=\pr_2(A\times B)=B,\qquad \pr_2(A\times B)^{-1}=\pr_1(A\times B)=A$$

we obtain $$(A\times B)^{-1}\subseteq B\times A$$. Conversely, if $$(y,x)\in B\times A$$, then $$x\in A$$ and $$y\in B$$, so $$(x,y)\in A\times B$$, and therefore $$(y,x)\in (A\times B)^{-1}$$; hence $$(A\times B)^{-1}=B\times A$$.

## Composition of Binary Relations

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> Let $$R_1$$ and $$R_2$$ be binary relations. The *composition* $$R_2\circ R_1$$ of these two binary relations is the set of ordered pairs $$(x,z)$$ for which there exists a $$y$$ such that $$(x,y)\in R_1$$ and $$(y,z)\in R_2$$.

</div>

It is natural to ask what relationship this composition of binary relations bears to the inverse defined above.

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4**</ins> Let $$R_1$$, $$R_2$$ be binary relations. Then the inverse of $$R_2\circ R_1$$ is $$R_2^{-1}\circ R_1^{-1}$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

$$(z,x)\in (R_2\circ R_1)^{-1}$$ is equivalent to $$(x,z)\in R_2\circ R_1$$. This in turn is equivalent to <phrase>the existence of some $y$ such that $(x,y)\in R_1$ and $(y,z)\in R_2$</phrase>. Any $$y$$ satisfying this condition also satisfies <phrase>$(y,x)\in R_1^{-1}$ and $(z,y)\in R_2^{-1}$</phrase>, so by the definition of composition we have $$(z,x)\in R_2^{-1}\circ R_1^{-1}$$. The reverse direction can be shown in the same way.

</details>

Moreover, composition of binary relations satisfies the associative law.

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> Composition of binary relations is associative. That is, for any three binary relations $$R_1,R_2,R_3$$, 

$$(R_3\circ R_2)\circ R_1=R_3\circ(R_2\circ R_1)$$

holds.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

It suffices to show that for any $$(x,w)$$, being an element of $$(R_3\circ R_2)\circ R_1$$ is equivalent to being an element of $$R_3\circ(R_2\circ R_1)$$.  

First, $$(x,w)\in (R_3\circ R_2)\circ R_1$$ is equivalent to <phrase>the existence of some $y$ such that $(x,y)\in R_1$ and $(y,w)\in R_3\circ R_2$</phrase>. But the latter condition is again equivalent to <phrase>the existence of some $z$ such that $(y,z)\in R_2$ and $(z,w)\in R_3$</phrase>, so this condition is equivalent to <phrase>$(x,z)\in R_2\circ R_1$ and $(z,w)\in R_3$</phrase>. Therefore this is equivalent to <phrase>$(x,w)\in R_3\circ(R_2\circ R_1)$</phrase>.

</details>

Thus we may write this common result $$(R_3\circ R_2)\circ R_1=R_3\circ(R_2\circ R_1)$$ without parentheses as $$R_3\circ R_2\circ R_1$$, with no ambiguity. 

The remaining propositions describe how the image of a set behaves under the inverse and composition of binary relations defined above.

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6**</ins> Let $$R_1$$, $$R_2$$ be binary relations and let $$A$$ be a set. Then

$$(R_2\circ R_1)(A)=R_2(R_1(A))$$

holds.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

We proceed as in the preceding proposition. 

For any $$z$$, the statement $$z\in (R_2\circ R_1)(A)$$ is equivalent to <phrase>the existence of some $x\in X$ such that $(x,z)\in R_2\circ R_1$</phrase>. But this is again equivalent to <phrase>the existence of some $y$ such that $(x,y)\in R_1$ and $(y,z)\in R_2$</phrase>. Since $$y\in R_1(A)$$, we have $$z\in R_2(R_1(A))$$. Reversing this logic yields the reverse inclusion.

</details>

<div class="proposition" markdown="1">

<ins id="prop7">**Proposition 7**</ins> Let $$(R,A,B)$$ be a binary relation, and let $$X\subseteq A$$, $$Y\subseteq B$$. Then 

1. $$R^{-1}(R(X))\supset X\cap\pr_1R$$  
2. $$R(R^{-1}(Y))\supset Y\cap\pr_2R$$  

hold, respectively.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Before beginning the proof proper, we observe that since the two formulas above must hold for <em>all</em> $$R$$, they must also hold when $$R^{-1}$$ is substituted for $$R$$. Therefore, once we prove 1, then 2 follows immediately from [Proposition 2](#prop2).  

Now let $$x\in X\cap\pr_1R$$. Then since $$x\in\pr_1R$$, there exists some $$y$$ such that $$(x,y)\in R$$, and because $$x\in X$$, this $$y$$ satisfies $$y\in R(X)$$. Since $$(y,x)\in R^{-1}$$, we have $$x\in R^{-1}(R(X))$$.

</details>

<div class="proposition" markdown="1">

<ins id="prop8">**Proposition 8**</ins> Let $$R_1$$, $$R_2$$ be binary relations. Then the following two formulas hold:

$$ \pr_1(R_2\circ R_1)=R_1^{-1}(\pr_1R_2),\quad \pr_2(R_2\circ R_1)=R_2(\pr_2R_1).$$

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

This is immediate from the following chain of equivalences:

$$\begin{aligned}
    x\in\pr_1(R_2\circ R_1)&\iff \exists z\big((x,z)\in R_2\circ R_1\big)\\
    &\iff\exists y,z\big(((x,y)\in R_1)\wedge((y,z)\in R_2)\big)\\
    &\iff\exists y\big(((x,y)\in R_1)\wedge(y\in\pr_1R_2)\big)\\
    &\iff x\in R_1^{-1}(\pr_1 R_2).
\end{aligned}$$

The second formula can be shown similarly.

</details>

Finally, we introduce a special binary relation.

<div class="definition" markdown="1">

<ins id="def9">**Definition 9**</ins> For a set $$A$$, $$\Delta_A$$ denotes the binary relation

$$\Delta_A=\{(x,x)\mid x\in A\}$$

This is called the *diagonal* of $$A\times A$$.

</div>

By definition $$\pr_1\Delta_A=\pr_2\Delta_A=A$$, so we may regard this as the binary relation

$$\left(\Delta_A,A,A\right)$$

In the next post we will show that this relation is a function; it is called the *identity function* on the set $$A$$. For a binary relation $$R_1$$ having $$A$$ as source, or a binary relation $$R_2$$ having $$A$$ as target, the two formulas

$$R_1\circ\Delta_A=R_1,\qquad \Delta_A\circ R_2=R_2$$

always hold, so it is not unnatural to call $$(\Delta_A,A,A)$$ the identity function.

---
**References**

**[Bou]** N. Bourbaki, *Theory of Sets*. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---
