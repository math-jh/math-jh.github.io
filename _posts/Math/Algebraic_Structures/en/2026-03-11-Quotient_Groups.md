---
title: "Quotient Groups"
excerpt: "Normal subgroups and quotient groups"

categories: [Math / Algebraic Structures]
permalink: /en/math/algebraic_structures/quotient_groups
header:
    overlay_image: /assets/images/Math/Algebraic_Structures/Quotient_Groups.png
    overlay_filter: 0.5
sidebar:
    nav: "algebraic_structures-en"

date: 2026-03-11
last_modified_at: 2026-03-11
weight: 5
translated_at: 2026-05-24T12:30:03+00:00
translation_source: kimi-cli
last_polished_at: 2026-05-24T12:30:03+00:00
---
In [§Algebraic Structures, §§Quotient Structures](/en/math/algebraic_structures/algebraic_structures#quotient-structures), we proved that if an equivalence relation $$R$$ is compatible with the operation of a magma $$A$$, then the quotient set $$A/R$$ can be naturally endowed with a magma structure. Moreover, at the end of [§Semigroups, Monoids, Groups](/en/math/algebraic_structures/groups), we saw that when $$A$$ is a group, the magma $$A/R$$ constructed in this way is also a group. In this case, the group $$A/R$$ is called a *quotient group*.

## Normal Subgroups

Now, from [[Set Theory] §Equivalence Relations, ⁋Proposition 7](/en/math/set_theory/equivalence_relations#prop7), we know that the following two notions are equivalent.

A set $$G$$ equipped with an equivalence relation $$R$$ $$\iff$$ a set $$G$$ partitioned into subsets $$(G_i)_{i\in I}$$
{: .text-center}

Thus, we may ask what requiring the equivalence relation $$R$$ to be compatible with the operation of $$G$$ means in terms of the partition.

First, suppose that $$R$$ is compatible with the operation of $$G$$. Then the elements of $$G/R$$ form a partition of $$G$$, and in particular, the set containing the identity element is exactly $$[e]$$.

<div class="proposition" markdown="1">

<ins id="prop1">**Proposition 1**</ins> For the quotient group $$G/R$$, $$[e]$$ is a subgroup of $$G$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Let $$a,b\in [e]$$. That is, $$a\sim e\sim b$$. Since $$R$$ is compatible with the operation of $$G$$, multiplying both sides of $$a\sim b$$ on the right by $$b^{-1}$$ gives $$ab^{-1}\sim e$$. Thus $$ab^{-1}\in[e]$$, so by [§Semigroups, Monoids, Groups, ⁋Proposition 15](/en/math/algebraic_structures/groups#prop15) we see that $$[e]$$ is a subgroup.

</details>

Conversely, let $$G$$ be a group and let $$H$$ be an arbitrary subgroup. Replacing $$[e]$$ with $$H$$ in the above proof, we can define the following relation.

$$a\sim_{\tiny r}b\iff ab^{-1}\in H$$

It is easy to verify that $$\sim_{\tiny r}$$ defined in this way is an equivalence relation. To define a quotient group from this, we need this equivalence relation to be compatible with the operation of $$G$$. Take arbitrary $$a,b,c\in G$$. First, if $$a\sim_{\tiny r}b$$ holds, then

$$(ac)(bc)^{-1}=acc^{-1}b^{-1}=ab^{-1}\in H$$

so $$ac\sim_{\tiny r} bc$$. That is, $$\sim_{\tiny r}$$ is right compatible with the operation of $$G$$. However,

$$(ca)(cb)^{-1}=cab^{-1}c^{-1}$$

so $$\sim_{\tiny r}$$ need not be left compatible with the operation of $$G$$ in general. But if for any $$x\in H$$, $$cxc^{-1}\in H$$ holds for all $$c\in G$$, then the right-hand side becomes an element of $$H$$, and thus $$\sim_{\tiny r}$$ defines a compatible equivalence relation on $$G$$.

<div class="remark" markdown="1">

<ins id="rmk1">**Remark**</ins> If instead of the equivalence relation $$\sim_r$$, we had defined the relation

$$a\sim_{\tiny l} b\iff a^{-1}b\in H$$

then $$\sim_{\tiny l}$$ is left compatible, and since

$$(ac)^{-1}(bc)=c^{-1}(a^{-1}b)c$$

it is not right compatible. For this relation to be right compatible, for all $$c\in G$$ and all $$x\in H$$ we must have $$c^{-1}xc\in H$$, which is the same condition obtained above.

</div>

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> For a group $$G$$, a subgroup $$H$$ is called a *normal subgroup* if for any $$g\in G$$ and any $$h\in H$$, we have $$ghg^{-1}\in H$$.

</div>

Now, since $$g$$ can be chosen arbitrarily, we can show that $$H$$ being a normal subgroup is equivalent to the statement that for any $$g$$, $$gHg^{-1}=H$$. From the above discussion, when $$G$$ has a normal subgroup $$H$$, we obtain the corresponding quotient group. We denote this quotient group by $$G/H$$.

In [Proposition 1](#prop1), for any $$a\in [e]$$ the implication

$$a\sim e\implies gag^{-1}\sim geg^{-1}=e$$

shows that $$[e]$$ is a normal subgroup. Moreover, setting $$H=[e]$$, the corresponding $$\sim_{\tiny r}$$ coincides exactly with the original equivalence relation $$\sim$$, so $$G/H$$ and $$G/R$$ are equal. Conversely, for any normal subgroup $$H$$ and the corresponding $$\sim_{\tiny r}$$, we also have $$G/H=G/{\sim_{\tiny r}}$$. Thus, giving a compatible equivalence relation on $$G$$ is equivalent to choosing a normal subgroup of $$G$$.

## Cosets

Now consider a group $$G$$ and an arbitrary subgroup $$H$$. Even if $$H$$ is not normal, the relations $$\sim_{\tiny r}$$ and $$\sim_{\tiny l}$$ obtained above are still equivalence relations, so we may examine what the *quotient sets* $$G/{\sim_{\tiny r}}$$ and $$G/{\sim_{\tiny l}}$$ look like.

First, let us consider the elements of $$G/{\sim_{\tiny r}}$$. For any $$a\in G$$ and its equivalence class $$[a]_{\tiny r}$$, we have

$$x\in [a]_{\tiny r}\iff x\sim_{\tiny r} a\iff xa^{-1}\in H$$

Thus, defining the set $$Ha$$ by

$$Ha:=\{ha\mid h\in H\}$$

we obtain $$[a]_{\tiny r}=Ha$$. Similarly, for $$G/{\sim_{\tiny l}}$$, we have $$[a]_{\tiny l}=aH$$. Of course, if the operation of $$G$$ is written additively, it is customary to denote these by $$H+a$$ and $$a+H$$, respectively.

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> The two sets $$Ha$$ and $$aH$$ defined above are called the *right coset* and *left coset*, respectively.

</div>

Thus, given a group $$G$$ and any subgroup $$H$$ thereof, the two equivalence relations $$\sim_{\tiny r}$$ and $$\sim_{\tiny l}$$ partition $$G$$ into right cosets and left cosets, respectively. In this case, the quotient set induced by $$\sim_{\tiny r}$$ on $$G$$ is denoted $$H\setminus G$$, and the quotient set induced by $$\sim_{\tiny l}$$ on $$G$$ is denoted $$G/H$$.[^1] In general $$Ha\neq aH$$, but it is easy to verify that $$Ha=aH$$ if and only if $$H$$ is normal.

Moreover, for any $$a\in G$$, the maps

$${a\cdot}: H\rightarrow aH;\quad h\mapsto ah,\qquad {a^{-1}\cdot}: aH\rightarrow H;\quad ah\mapsto h$$

are inverses of each other, so we see that all right cosets and left cosets have the same cardinality as $$H$$. Also, defining a function $$H\setminus G\rightarrow G/H$$ by

$$Ha\mapsto a^{-1}H$$

one easily verifies that this function is bijective. That is, $$\lvert H\setminus G\rvert=\lvert G/H\rvert$$.

<div class="definition" markdown="1">

<ins id="def4">**Definition 4**</ins> For a group $$G$$ and a subgroup $$H$$, we define the *index* of $$H$$, denoted $$[G:H]$$, to be $$\lvert G/H\rvert$$.

</div>

From the structure of $$G/H$$ examined above and the size of each element of $$G/H$$, the following proposition is immediate.

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5 (Lagrange)**</ins> For a group $$G$$ and a subgroup $$H$$, we have $$\lvert G\rvert=[G:H]\lvert H\rvert$$.

</div>

This proposition holds even when $$G$$ or $$H$$ is infinite, but in the special case where they are finite, we obtain the result that for any subgroup $H$ of $G$, the order $\lvert H\rvert$ divides $\lvert G\rvert$.



---

**References**

**[Bou]** Bourbaki, N. Algebra I. *Elements of Mathematics*. Springer. 1998.

---

[^1]: The notation for right cosets coincides with the notation for set difference, but since we will not use right cosets often, we will not introduce a separate notation.
