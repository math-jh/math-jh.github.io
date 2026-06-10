---
title: "Quotient Groups"
description: "We construct quotient groups using normal subgroups and equivalence relations. We show that when an equivalence relation is compatible with the group operation, a natural group structure arises on the quotient set."
excerpt: "Normal subgroups and quotient groups"

categories: [Math / Algebraic Structures]
permalink: /en/math/algebraic_structures/quotient_groups
sidebar: 
    nav: "algebraic_structures-en"

date: 2022-11-30
last_modified_at: 2022-11-30
weight: 5
translated_at: 2026-05-29T17:30:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-05-29T17:30:04+00:00
---
Previously, in [§Algebraic Structures, §§Quotient Structures](/en/math/algebraic_structures/algebraic_structures#quotient-structures), we proved that when an equivalence relation $$R$$ is compatible with the operation of a magma $$A$$, the quotient set $$A/R$$ can be given a magma structure in a natural way. Moreover, at the end of [§Semigroups, Monoids, and Groups](/en/math/algebraic_structures/groups), we saw that when $$A$$ is a group, the magma $$A/R$$ constructed in this way is again a group. This group $$A/R$$ is called a *quotient group*.

## Normal Subgroups

Meanwhile, from [[Set Theory] §Equivalence Relations, ⁋Proposition 7](/en/math/set_theory/equivalence_relations#prop7), we know that the following two are equivalent:

Giving an equivalence relation $$R$$ on a set $$G$$ $$\iff$$ Choosing a partition $$(G_i)_{i\in I}$$ of $$G$$
{: .text-center}

Thus, we may ask what it means on the right-hand side to require that the equivalence relation $$R$$ be compatible with the operation of $$G$$.

First, suppose that $$R$$ is compatible with the operation of $$G$$. Then each element of $$G/R$$ constitutes a block of the partition of $$G$$, and in particular, the block containing the identity element is precisely $$[e]$$.

<div class="proposition" markdown="1">

<ins id="prop1">**Proposition 1**</ins> For a quotient group $$G/R$$, the equivalence class $$[e]$$ is a subgroup of $$G$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Let $$a,b\in [e]$$. That is, $$a\sim e\sim b$$. Since $$R$$ is compatible with the operation of $$G$$, multiplying both sides of $$a\sim b$$ on the right by $$b^{-1}$$ yields $$ab^{-1}\sim e$$. Thus $$ab^{-1}\in[e]$$, and by [§Semigroups, Monoids, and Groups, ⁋Proposition 15](/en/math/algebraic_structures/groups#prop15), we conclude that $$[e]$$ is a subgroup.

</details>

Conversely, suppose an arbitrary subgroup $$H$$ of $$G$$ is given. Replacing $$[e]$$ with $$H$$ in the argument above, we can define the following relation:

$$a\sim_{\tiny r}b\iff ab^{-1}\in H$$

It is easy to verify that $$\sim_{\tiny r}$$ defined in this way is an equivalence relation. To obtain a quotient group from this, the equivalence relation must be compatible with the operation of $$G$$. Let arbitrary $$a,b,c\in G$$ be given. First, if $$a\sim_{\tiny r}b$$, then

$$(ac)(bc)^{-1}=acc^{-1}b^{-1}=ab^{-1}\in H$$

so $$ac\sim_{\tiny r} bc$$. That is, $$\sim_{\tiny r}$$ is right compatible with the operation of $$G$$. However,

$$(ca)(cb)^{-1}=cab^{-1}c^{-1}$$

so $$\sim_{\tiny r}$$ need not be left compatible in general. Yet if $$cxc^{-1}\in H$$ for every $$x\in H$$ and every $$c\in G$$, then the right-hand side above lies in $$H$$, and hence $$\sim_{\tiny r}$$ defines a compatible equivalence relation on $$G$$.

<div class="remark" markdown="1">

**Remark**</ins> If instead of the equivalence relation $$\sim_r$$ we define

$$a\sim_{\tiny l} b\iff a^{-1}b\in H$$

then $$\sim_{\tiny l}$$ is left compatible, and since

$$(ac)^{-1}(bc)=c^{-1}(a^{-1}b)c$$

it is not right compatible. For this relation to be right compatible, $$c^{-1}xc\in H$$ must hold for arbitrary $$c\in G$$ and arbitrary $$x\in H$$, which is the same condition obtained above.

</div>

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> A subgroup $$H$$ of a group $$G$$ is called a *normal subgroup* if for every $$g\in G$$ and every $$h\in H$$, we have $$ghg^{-1}\in H$$.

</div>

Since $$g$$ can be chosen arbitrarily, one can show that $$H$$ being normal is equivalent to $$gHg^{-1}=H$$ for every $$g$$. By the discussion above, given a normal subgroup $$H$$ of $$G$$, we obtain the corresponding quotient group, which is denoted by $$G/H$$.

From [Proposition 1](#prop1), for any $$a\in [e]$$ we have

$$a\sim e\implies gag^{-1}\sim geg^{-1}=e$$

and thus $$[e]$$ is a normal subgroup. Moreover, if we set $$H=[e]$$, the corresponding $$\sim_{\tiny r}$$ coincides exactly with the original equivalence relation $$\sim$$, so $$G/H$$ and $$G/R$$ are the same. Conversely, for $$\sim_{\tiny r}$$ defined from an arbitrary normal subgroup $$H$$, we also have $$G/H=G/{\sim_{\tiny r}}$$. Hence giving a compatible equivalence relation on $$G$$ is equivalent to choosing a normal subgroup of $$G$$.

## Cosets

Now consider a group $$G$$ and an arbitrary subgroup $$H$$. Even if $$H$$ is not normal, the relations $$\sim_{\tiny r}$$ and $$\sim_{\tiny l}$$ obtained above are still equivalence relations, so we may examine what the *quotient sets* $$G/{\sim_{\tiny r}}$$ and $$G/{\sim_{\tiny l}}$$ look like.

First, consider the elements of $$G/{\sim_{\tiny r}}$$. For arbitrary $$a\in G$$ and its equivalence class $$[a]_{\tiny r}$$, we have

$$x\in [a]_{\tiny r}\iff x\sim_{\tiny r} a\iff xa^{-1}\in H$$

Therefore, defining the set $$Ha$$ by

$$Ha:=\{ha\mid h\in H\}$$

we obtain $$[a]_{\tiny r}=Ha$$. Similarly, for $$G/{\sim_{\tiny l}}$$ we have $$[a]_{\tiny l}=aH$$. Of course, if the operation of $$G$$ is written additively, these are conventionally denoted $$H+a$$ and $$a+H$$, respectively.

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> The two sets $$Ha$$ and $$aH$$ defined above are called a *right coset* and a *left coset*, respectively.

</div>

Thus, given an arbitrary subgroup $$H$$ of $$G$$, the two equivalence relations $$\sim_{\tiny r}$$ and $$\sim_{\tiny l}$$ partition $$G$$ into right cosets and left cosets, respectively. The quotient set of $$G$$ by $$\sim_{\tiny r}$$ is denoted $$H\setminus G$$, and the quotient set of $$G$$ by $$\sim_{\tiny l}$$ is denoted $$G/H$$.[^1] Although $$Ha\neq aH$$ in general, it is easy to check that $$Ha=aH$$ if and only if $$H$$ is normal.

Moreover, for arbitrary $$a\in G$$, the maps

$${a\cdot}: H\rightarrow aH;\quad h\mapsto ah,\qquad {a^{-1}\cdot}: aH\rightarrow H;\quad ah\mapsto h$$

are inverses of each other, so both right cosets and left cosets have the same cardinality as $$H$$. Also, defining a function $$H\setminus G\rightarrow G/H$$ by

$$Ha\mapsto a^{-1}H$$

it is easy to verify that this function is bijective. Hence $$\lvert H\setminus G\rvert=\lvert G/H\rvert$$.

<div class="definition" markdown="1">

<ins id="def4">**Definition 4**</ins> For a group $$G$$ and a subgroup $$H$$, the *index* $$[G:H]$$ of $$H$$ is defined as $$\lvert G/H\rvert$$.

</div>

From the structure of $$G/H$$ examined above and the size of each element of $$G/H$$, the following proposition is immediate.

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5 (Lagrange)**</ins> For a group $$G$$ and a subgroup $$H$$, we have $$\lvert G\rvert=[G:H]\lvert H\rvert$$.

</div>

This proposition remains valid even when $$G$$ or $$H$$ is infinite, but in the finite case it yields the familiar result that the order of any subgroup $$H$$ of a finite group $$G$$ divides the order of $$G$$.



---

**References**

**[Bou]** Bourbaki, N. Algebra I. *Elements of Mathematics*. Springer. 1998.  

---

[^1]: The notation for right cosets conflicts with that for set difference, but since right cosets will rarely be used, we do not introduce a separate notation.
