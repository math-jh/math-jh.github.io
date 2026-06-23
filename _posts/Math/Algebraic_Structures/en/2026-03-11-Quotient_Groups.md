---
title: "Quotient Groups"
description: "We construct the quotient group from a normal subgroup and its equivalence relation. When the equivalence relation is compatible with the group operation, the quotient set inherits a natural group structure."
excerpt: "Normal subgroups and quotient groups"

categories: [Math / Algebraic Structures]
permalink: /en/math/algebraic_structures/quotient_groups
sidebar: 
    nav: "algebraic_structures-en"

date: 2022-11-30
weight: 5

drift_needed: true
translated_at: 2026-06-23T11:30:37+00:00
translation_source: kimi-cli
---
In [§Algebraic Structures, §§Quotient Structures](/en/math/algebraic_structures/algebraic_structures#몫구조), we proved that when an equivalence relation $$R$$ is compatible with the operation of a magma $$A$$, the quotient set $$A/R$$ can be given a magma structure in a natural way; moreover, at the end of [§Semigroups, Monoids, and Groups](/en/math/algebraic_structures/groups), we saw that if $$A$$ is a group, then the magma $$A/R$$ constructed in this way is also a group. In this case, the group $$A/R$$ is called a *quotient group*.

## Normal Subgroups

On the other hand, from [\[Set Theory\] §Equivalence Relations](/en/math/set_theory/equivalence_relations) we know that the following two things are equivalent:

Giving an equivalence relation $$R$$ on a set $$G$$ $$\iff$$ Choosing a partition $$(G_i)_{i\in I}$$ of the set $$G$$
{: .text-center}

Therefore, we can consider what the requirement that the equivalence relation $$R$$ be compatible with the operation of $$G$$ means on the right-hand side.

First, assume that $$R$$ is compatible with the operation of $$G$$. Then each element of $$G/R$$ forms a partition of $$G$$, and in particular the set containing the identity element is only $$[e]$$.

<div class="proposition" markdown="1">

<ins id="prop1">**Proposition 1**</ins> For the quotient group $$G/R$$, $$[e]$$ is a subgroup of $$G$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Let $$a,b\in [e]$$. That is, $$a\sim e\sim b$$. Since $$R$$ is compatible with the operation of $$G$$, multiplying both sides of $$a\sim b$$ on the right by $$b^{-1}$$ yields $$ab^{-1}\sim e$$. Thus $$ab^{-1}\in[e]$$, so by [§Semigroups, Monoids, and Groups, ⁋Proposition 15](/en/math/algebraic_structures/groups#prop15) we know that $$[e]$$ is a subgroup.

</details>

Conversely, suppose an arbitrary subgroup $$H$$ of $$G$$ is given. Replacing $$[e]$$ with $$H$$ in the above proof, we can define the following relation:

$$a\sim_{\tiny r}b\iff ab^{-1}\in H$$

It is easy to show that $$\sim_{\tiny r}$$ defined in this way is an equivalence relation. Through this, to define a quotient group, this equivalence relation must be compatible with the operation of $$G$$. Let arbitrary $$a,b,c\in G$$ be given. First, if $$a\sim_{\tiny r}b$$ holds,

$$(ac)(bc)^{-1}=acc^{-1}b^{-1}=ab^{-1}\in H$$

so $$ac\sim_{\tiny r} bc$$ holds. That is, $$\sim_{\tiny r}$$ is right compatible with the operation of $$G$$. However,

$$(ca)(cb)^{-1}=cab^{-1}c^{-1}$$

so in general $$\sim_{\tiny r}$$ need not be left compatible with the operation of $$G$$. But if for arbitrary $$x\in H$$, $$cxc^{-1}\in H$$ holds for all $$c\in G$$, then the right-hand side becomes an element of $$H$$, and thus $$\sim_{\tiny r}$$ defines a compatible equivalence relation on $$G$$.

<div class="remark" markdown="1">

**Remark**</ins> If instead of the equivalence relation $$\sim_r$$ we had defined the relation

$$a\sim_{\tiny l} b\iff a^{-1}b\in H$$

then $$\sim_{\tiny l}$$ would be left compatible, and since

$$(ac)^{-1}(bc)=c^{-1}(a^{-1}b)c$$

it is not right compatible. For this relation to be right compatible, $$c^{-1}xc\in H$$ must hold for arbitrary $$c\in G$$ and arbitrary $$x\in H$$, which is the same condition obtained above.

</div>

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> A subgroup $$H$$ of a group $$G$$ is called a *normal subgroup* if for arbitrary $$g\in G$$ and arbitrary $$h\in H$$, $$ghg^{-1}\in H$$ always holds.

</div>

On the other hand, since $$g$$ can be chosen arbitrarily, one can show that $$H$$ being a normal subgroup is equivalent to $$gHg^{-1}=H$$ holding for arbitrary $$g$$. By the above discussion, when a normal subgroup $$H$$ of $$G$$ is given, we can obtain the corresponding quotient group. The resulting quotient group is then written as $$G/H$$.

From [Proposition 1](#prop1), for arbitrary $$a\in [e]$$ the following formula

$$a\sim e\implies gag^{-1}\sim geg^{-1}=e$$

shows that $$[e]$$ is a normal subgroup. Also, when $$H=[e]$$, the corresponding $$\sim_{\tiny r}$$ is exactly the same as the original equivalence relation $$\sim$$, so $$G/H$$ and $$G/R$$ are equal. Conversely, for $$\sim_{\tiny r}$$ defined from an arbitrary normal subgroup $$H$$, $$G/H=G/{\sim_{\tiny r}}$$ also holds. From this we know that giving a compatible equivalence relation on $$G$$ is the same as choosing a normal subgroup of $$G$$.

## Cosets

Now consider a group $$G$$ and an arbitrary subgroup $$H$$. Even if $$H$$ is not normal, the $$\sim_{\tiny r}$$ and $$\sim_{\tiny l}$$ obtained from the above discussion are still equivalence relations, so we can examine what the quotient sets $$G/{\sim_{\tiny r}}$$ and $$G/{\sim_{\tiny l}}$$ look like.

First, consider the elements of $$G/{\sim_{\tiny r}}$$. For arbitrary $$a\in G$$ and its equivalence class $$[a]_{\tiny r}$$, we know that

$$x\in [a]_{\tiny r}\iff x\sim_{\tiny r} a\iff xa^{-1}\in H$$

Thus, defining the set $$Ha$$ by the formula

$$Ha:=\{ha\mid h\in H\}$$

we have $$[a]_{\tiny r}=Ha$$. Similarly, for $$G/{\sim_{\tiny l}}$$ we have $$[a]_{\tiny l}=aH$$. Of course, if the operation of $$G$$ were written as addition, these would conventionally be written as $$H+a$$ and $$a+H$$ respectively.

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> The two sets $$Ha$$ and $$aH$$ defined above are called the *right coset* and *left coset* respectively.

</div>

Thus, when an arbitrary subgroup $$H$$ of $$G$$ is given, the two equivalence relations $$\sim_{\tiny r}$$ and $$\sim_{\tiny l}$$ partition $$G$$ into right cosets and left cosets respectively. In this case, the quotient set of $$G$$ by $$\sim_{\tiny r}$$ is written as $$H\setminus G$$, and the quotient set of $$G$$ by $$\sim_{\tiny l}$$ is written as $$G/H$$.[^1] In general $$Ha\neq aH$$, but in fact it is easy to check that the necessary and sufficient condition for $$Ha=aH$$ to hold is that $$H$$ is normal.

Moreover, for arbitrary $$a\in G$$,

$${a\cdot}: H\rightarrow aH;\quad h\mapsto ah,\qquad {a^{-1}\cdot}: aH\rightarrow H;\quad ah\mapsto h$$

are inverse functions of each other, so we can see that all right cosets and left cosets have the same cardinality as $$H$$. Also, defining a function $$H\setminus G\rightarrow G/H$$ by the formula

$$Ha\mapsto a^{-1}H$$

it is easy to check that this function is bijective. That is, $$\lvert H\setminus G\rvert=\lvert G/H\rvert$$.

<div class="definition" markdown="1">

<ins id="def4">**Definition 4**</ins> For a group $$G$$ and a subgroup $$H$$, we define the *index* $$[G:H]$$ of $$H$$ as $$\lvert G/H\rvert$$.

</div>

From the structure of $$G/H$$ examined above and the size of each element of $$G/H$$, the following proposition is obvious.

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5 (Lagrange)**</ins> For a group $$G$$ and a subgroup $$H$$, $$\lvert G\rvert=[G:H]\lvert H\rvert$$ holds.

</div>

This proposition also holds when $$G$$ or $$H$$ is infinite, but in particular when they are finite, we obtain the result that <phrase>for any subgroup $$H$$ of a group $$G$$, $$\lvert H\rvert$$ divides $$\lvert G\rvert$$</phrase>.

---

**References**

**[Bou]** Bourbaki, N. Algebra I. *Elements of Mathematics*. Springer. 1998.  

---

[^1]: The notation for right cosets conflicts with set difference notation, but since there will not be much occasion to use right cosets, we shall not introduce a separate notation.
