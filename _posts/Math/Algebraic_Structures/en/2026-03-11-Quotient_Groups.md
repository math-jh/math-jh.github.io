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

date: 2022-11-30
last_modified_at: 2022-11-30
weight: 5
translated_at: 2026-05-26T03:30:02+00:00
translation_source: kimi-cli
---
Previously, in [§Algebraic Structures, §§Quotient Structures](/en/math/algebraic_structures/algebraic_structures#quotient-structures), we proved that when an equivalence relation $$R$$ is compatible with the operation of a magma $$A$$, the quotient set $$A/R$$ can be given a magma structure in a natural way. Moreover, at the end of [§Semigroups, Monoids, and Groups](/en/math/algebraic_structures/groups), we saw that when $$A$$ is a group, the magma $$A/R$$ constructed in this way is also a group. This group $$A/R$$ is called a *quotient group*.

## Normal Subgroups

Meanwhile, from [[Set Theory] §Equivalence Relations, ⁋Proposition 7](/en/math/set_theory/equivalence_relations#prop7), we know that the following two are equivalent:

Giving an equivalence relation $$R$$ on a set $$G$$ $$\iff$$ Choosing a partition $$(G_i)_{i\in I}$$ of $$G$$
{: .text-center}

Therefore, we can consider what requiring the equivalence relation $$R$$ to be compatible with the operation of $$G$$ means on the right-hand side.

First, assume that $$R$$ is compatible with the operation of $$G$$. Then each element of $$G/R$$ forms a partition of $$G$$, and in particular, the set containing the identity element is uniquely $$[e]$$.

<div class="proposition" markdown="1">

<ins id="prop1">**Proposition 1**</ins> For the quotient group $$G/R$$, $$[e]$$ is a subgroup of $$G$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Let $$a,b\in [e]$$. That is, $$a\sim e\sim b$$. Now since $$R$$ is compatible with the operation of $$G$$, multiplying both sides of $$a\sim b$$ on the right by $$b^{-1}$$ yields $$ab^{-1}\sim e$$. Thus $$ab^{-1}\in[e]$$, and by [§Semigroups, Monoids, and Groups, ⁋Proposition 15](/en/math/algebraic_structures/groups#prop15), we know that $$[e]$$ is a subgroup.

</details>

Conversely, suppose an arbitrary subgroup $$H$$ of $$G$$ is given. Replacing $$[e]$$ with $$H$$ in the above proof, we can define the following relation:

$$a\sim_{\tiny r}b\iff ab^{-1}\in H$$

It is easy to show that $$\sim_{\tiny r}$$ defined in this way is an equivalence relation. To define a quotient group through this, this equivalence relation must be compatible with the operation of $$G$$. Let arbitrary $$a,b,c\in G$$ be given. First, if $$a\sim_{\tiny r}b$$ holds, then

$$(ac)(bc)^{-1}=acc^{-1}b^{-1}=ab^{-1}\in H$$

so $$ac\sim_{\tiny r} bc$$ holds. That is, $$\sim_{\tiny r}$$ is right compatible with the operation of $$G$$. However,

$$(ca)(cb)^{-1}=cab^{-1}c^{-1}$$

so $$\sim_{\tiny r}$$ is not necessarily left compatible with the operation of $$G$$ in general. But if for arbitrary $$x\in H$$, $$cxc^{-1}\in H$$ holds for all $$c\in G$$, then the right-hand side becomes an element of $$H$$, and thus $$\sim_{\tiny r}$$ defines a compatible equivalence relation on $$G$$.

<div class="remark" markdown="1">

<ins id="rmk1">**Remark**</ins> If instead of the equivalence relation $$\sim_r$$ we define the following relation

$$a\sim_{\tiny l} b\iff a^{-1}b\in H$$

then $$\sim_{\tiny l}$$ is left compatible, and since

$$(ac)^{-1}(bc)=c^{-1}(a^{-1}b)c$$

it is not right compatible. For this relation to be right compatible, $$c^{-1}xc\in H$$ must hold for arbitrary $$c\in G$$ and arbitrary $$x\in H$$, which is the same condition obtained above.

</div>

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> A subgroup $$H$$ of a group $$G$$ is called a *normal subgroup* if for arbitrary $$g\in G$$ and arbitrary $$h\in H$$, $$ghg^{-1}\in H$$ always holds.

</div>

Meanwhile, since $$g$$ can be chosen arbitrarily, we can show that $$H$$ being a normal subgroup is equivalent to $$gHg^{-1}=H$$ holding for arbitrary $$g$$. By the above discussion, when a normal subgroup $$H$$ of $$G$$ is given, we can obtain the corresponding quotient group. The resulting quotient group is denoted by $$G/H$$.

From [Proposition 1](#prop1), for arbitrary $$a\in [e]$$, the following

$$a\sim e\implies gag^{-1}\sim geg^{-1}=e$$

shows that $$[e]$$ is a normal subgroup. Also, when we set $$H=[e]$$, the corresponding $$\sim_{\tiny r}$$ is exactly the same as the original equivalence relation $$\sim$$, so $$G/H$$ and $$G/R$$ are equal. Conversely, for $$\sim_{\tiny r}$$ defined from an arbitrary normal subgroup $$H$$, $$G/H=G/{\sim_{\tiny r}}$$ also holds. From this, we know that giving a compatible equivalence relation on $$G$$ is the same as choosing a normal subgroup of $$G$$.

## Cosets

Now consider a group $$G$$ and an arbitrary subgroup $$H$$. Even if $$H$$ is not normal, $$\sim_{\tiny r}$$ and $$\sim_{\tiny l}$$ obtained from the above discussion are still equivalence relations, so we can examine what the *quotient sets* $$G/{\sim_{\tiny r}}$$ and $$G/{\sim_{\tiny l}}$$ look like.

First, consider the elements of $$G/{\sim_{\tiny r}}$$. For arbitrary $$a\in G$$ and its equivalence class $$[a]_{\tiny r}$$, we know that

$$x\in [a]_{\tiny r}\iff x\sim_{\tiny r} a\iff xa^{-1}\in H$$

Therefore, if we define the set $$Ha$$ by the following formula

$$Ha:=\{ha\mid h\in H\}$$

then $$[a]_{\tiny r}=Ha$$ holds. Similarly, for $$G/{\sim_{\tiny l}}$$, $$[a]_{\tiny l}=aH$$ holds. Of course, if the operation of $$G$$ were written as addition, these would conventionally be denoted as $$H+a$$ and $$a+H$$ respectively.

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> The two sets $$Ha$$ and $$aH$$ defined above are called a *right coset* and a *left coset*, respectively.

</div>

Thus, when an arbitrary subgroup $$H$$ of $$G$$ is given, the two equivalence relations $$\sim_{\tiny r}$$ and $$\sim_{\tiny l}$$ partition $$G$$ into right cosets and left cosets, respectively. In this case, the quotient set of $$G$$ by $$\sim_{\tiny r}$$ is denoted $$H\setminus G$$, and the quotient set of $$G$$ by $$\sim_{\tiny l}$$ is denoted $$G/H$$.[^1] Although $$Ha\neq aH$$ in general, it is easy to verify that $$Ha=aH$$ holds if and only if $$H$$ is normal.

Moreover, for arbitrary $$a\in G$$,

$${a\cdot}: H\rightarrow aH;\quad h\mapsto ah,\qquad {a^{-1}\cdot}: aH\rightarrow H;\quad ah\mapsto h$$

are inverses of each other, so we can see that both right cosets and left cosets have the same cardinality as $$H$$. Also, defining a function $$H\setminus G\rightarrow G/H$$ by the formula

$$Ha\mapsto a^{-1}H$$

it is easy to verify that this function is bijective. That is, $$\lvert H\setminus G\rvert=\lvert G/H\rvert$$.

<div class="definition" markdown="1">

<ins id="def4">**Definition 4**</ins> For a group $$G$$ and a subgroup $$H$$, the *index* $$[G:H]$$ of $$H$$ is defined as $$\lvert G/H\rvert$$.

</div>

From the structure of $$G/H$$ examined above and the size of each element of $$G/H$$, the following proposition is obvious.

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5 (Lagrange)**</ins> For a group $$G$$ and a subgroup $$H$$, $$\lvert G\rvert=[G:H]\lvert H\rvert$$ holds.

</div>

This proposition holds even when $$G$$ or $$H$$ is infinite, but particularly when they are finite, we obtain the result that for any subgroup $$H$$ of a group $$G$$, $$\lvert H\rvert$$ is a divisor of $$\lvert G\rvert$$.



---

**References**

**[Bou]** Bourbaki, N. Algebra I. *Elements of Mathematics*. Springer. 1998.  

---

[^1]: The notation for right cosets overlaps with that for set difference, but since there will not be many occasions to use right cosets, we will not introduce a separate notation.
