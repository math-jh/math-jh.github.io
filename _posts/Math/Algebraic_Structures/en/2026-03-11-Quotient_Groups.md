---

title: "Quotient Groups"
excerpt: "Normal subgroups and quotient groups"

categories: [Math / Algebraic Structures]
permalink: /en/math/algebraic_structures/quotient_groups
header:
    overlay_image: /assets/images/Math/Algebraic_Structures/Quotient_groups.png
    overlay_filter: 0.5
sidebar:
    nav: "algebraic_structures-en"

date: 2026-03-11
last_modified_at: 2026-03-11
weight: 5

---

In [§Algebraic Structures, §§Quotient Structures](/en/math/algebraic_structures/algebraic_structures#quotient-structures), we proved that when an equivalence relation $$R$$ is compatible with the operation of a magma $$A$$, the quotient set $$A/R$$ can be naturally equipped with a magma structure. Moreover, at the end of [§Semigroups, Monoids, Groups](/en/math/algebraic_structures/groups), we saw that if $$A$$ is a group, the magma $$A/R$$ constructed in this way is also a group. In this case, the group $$A/R$$ is called a *quotient group*.

## Normal Subgroups

On the other hand, from [\[Set Theory\] §Equivalence Relations, ⁋Proposition 7](/en/math/set_theory/equivalence_relations#prop7), we know that the following two notions are equivalent.

Giving an equivalence relation $$R$$ on a set $$G$$ $$\iff$$ Choosing a partition $$(G_i)_{i\in I}$$ of the set $$G$$
{: .text-center}

Therefore, we can consider what requiring the equivalence relation $$R$$ to be compatible with the operation of $$G$$ means on the right-hand side.

First, assume that $$R$$ is compatible with the operation of $$G$$. Then the elements of $$G/R$$ form a partition of $$G$$, and in particular, the set containing the identity element is exactly $$[e]$$.

<div class="proposition" markdown="1">

<ins id="prop1">**Proposition 1**</ins> For a quotient group $$G/R$$, $$[e]$$ is a subgroup of $$G$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Let $$a,b\in [e]$$. That is, $$a\sim e\sim b$$. Since $$R$$ is compatible with the operation of $$G$$, multiplying both sides of $$a\sim b$$ on the right by $$b^{-1}$$ yields $$ab^{-1}\sim e$$. Thus $$ab^{-1}\in[e]$$, and by [§Semigroups, Monoids, Groups, ⁋Proposition 15](/en/math/algebraic_structures/groups#prop15), $$[e]$$ is a subgroup.

</details>

Conversely, suppose an arbitrary subgroup $$H$$ of $$G$$ is given. Replacing $$[e]$$ with $$H$$ in the above proof, we can define the following relation.

$$a\sim_{\tiny r}b\iff ab^{-1}\in H$$

It is easy to show that $$\sim_{\tiny r}$$ defined in this way is an equivalence relation. To define a quotient group using this, this equivalence relation must be compatible with the operation of $$G$$. Let arbitrary $$a,b,c\in G$$ be given. First, if $$a\sim_{\tiny r}b$$ holds, then

$$(ac)(bc)^{-1}=acc^{-1}b^{-1}=ab^{-1}\in H$$

so $$ac\sim_{\tiny r} bc$$ holds. That is, $$\sim_{\tiny r}$$ is right compatible with the operation of $$G$$. However, since

$$(ca)(cb)^{-1}=cab^{-1}c^{-1}$$

in general, $$\sim_{\tiny r}$$ need not be left compatible with the operation of $$G$$. But if for any $$x\in H$$, $$cxc^{-1}\in H$$ holds for all $$c\in G$$, then the right-hand side becomes an element of $$H$$, and thus $$\sim_{\tiny r}$$ defines a compatible equivalence relation on $$G$$.

<div class="remark" markdown="1">

<ins id="rmk1">**Remark**</ins> If instead of the equivalence relation $$\sim_r$$, we had defined the relation

$$a\sim_{\tiny l} b\iff a^{-1}b\in H$$

then $$\sim_{\tiny l}$$ is left compatible, and since

$$(ac)^{-1}(bc)=c^{-1}(a^{-1}b)c$$

it is not right compatible. For this relation to be right compatible, $$c^{-1}xc\in H$$ must hold for all $$c\in G$$ and all $$x\in H$$, which is the same condition obtained above.

</div>

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> A subgroup $$H$$ of a group $$G$$ is a *normal subgroup* if for any $$g\in G$$ and any $$h\in H$$, $$ghg^{-1}\in H$$ always holds.

</div>

On the other hand, since $$g$$ can be chosen arbitrarily, we can show that $$H$$ being a normal subgroup is equivalent to $$gHg^{-1}=H$$ holding for any $$g$$. From the above discussion, when a normal subgroup $$H$$ of $$G$$ is given, we can obtain the corresponding quotient group. The quotient group obtained in this case is denoted by $$G/H$$.

In [Proposition 1](#prop1), from the equation

$$a\sim e\implies gag^{-1}\sim geg^{-1}=e$$

for any $$a\in [e]$$, we see that $$[e]$$ is a normal subgroup. Also, when setting $$H=[e]$$, the corresponding $$\sim_{\tiny r}$$ is exactly the original equivalence relation $$\sim$$, so $$G/H$$ and $$G/R$$ are equal. Conversely, for any normal subgroup $$H$$, $$G/H=G/{\sim_{\tiny r}}$$ also holds. From this, we see that giving a compatible equivalence relation on $$G$$ is the same as choosing a normal subgroup of $$G$$.

## Cosets

Now consider a group $$G$$ and an arbitrary subgroup $$H$$. Even if $$H$$ is not normal, the $$\sim_{\tiny r}$$ and $$\sim_{\tiny l}$$ obtained from the above discussion are still equivalence relations, so we can examine what the *quotient sets* $$G/{\sim_{\tiny r}}$$ and $$G/{\sim_{\tiny l}}$$ look like.

First, let us consider the elements of $$G/{\sim_{\tiny r}}$$. For any $$a\in G$$ and its equivalence class $$[a]_{\tiny r}$$,

$$x\in [a]_{\tiny r}\iff x\sim_{\tiny r} a\iff xa^{-1}\in H$$

is observed. Therefore, defining the set $$Ha$$ by

$$Ha:=\{ha\mid h\in H\}$$

we have $$[a]_{\tiny r}=Ha$$. Similarly, for $$G/{\sim_{\tiny l}}$$, we have $$[a]_{\tiny l}=aH$$. Of course, if the operation of $$G$$ is written as addition, it is customary to write these as $$H+a$$ and $$a+H$$, respectively.

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> The two sets $$Ha$$ and $$aH$$ defined above are called the *right coset* and *left coset*, respectively.

</div>

Thus, when any subgroup $$H$$ of $$G$$ is given, the two equivalence relations $$\sim_{\tiny r}$$ and $$\sim_{\tiny l}$$ partition $$G$$ into right cosets and left cosets, respectively. In this case, the quotient set of $$G$$ by $$\sim_{\tiny r}$$ is denoted by $$H\setminus G$$, and the quotient set of $$G$$ by $$\sim_{\tiny l}$$ is denoted by $$G/H$$.[^1] In general, $$Ha\neq aH$$, but it is easy to verify that the necessary and sufficient condition for $$Ha=aH$$ is that $$H$$ is normal.

Moreover, for any $$a\in G$$,

$${a\cdot}: H\rightarrow aH;\quad h\mapsto ah,\qquad {a^{-1}\cdot}: aH\rightarrow H;\quad ah\mapsto h$$

are inverses of each other, so we see that right cosets and left cosets all have the same cardinality as $$H$$. Also, defining a function $$H\setminus G\rightarrow G/H$$ by

$$Ha\mapsto a^{-1}H$$

it is easy to verify that this function is a bijection. That is, $$\lvert H\setminus G\rvert=\lvert G/H\rvert$$.

<div class="definition" markdown="1">

<ins id="def4">**Definition 4**</ins> For a group $$G$$ and a subgroup $$H$$, the *index* $$[G:H]$$ of $$H$$ is defined as $$\lvert G/H\rvert$$.

</div>

From the structure of $$G/H$$ examined above and the size of each element of $$G/H$$, the following proposition is immediate.

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5 (Lagrange)**</ins> For a group $$G$$ and a subgroup $$H$$, $$\lvert G\rvert=[G:H]\lvert H\rvert$$ holds.

</div>

This proposition holds even when $$G$$ or $$H$$ is infinite, but particularly when they are finite, we obtain the result that for any subgroup $$H$$ of a finite group $$G$$, $$\lvert H\rvert$$ divides $$\lvert G\rvert$$.



---

**References**

**[Bou]** Bourbaki, N. Algebra I. *Elements of Mathematics*. Springer. 1998.

---

[^1]: The notation for right cosets coincides with the notation for set difference, but since we will not use right cosets often, we will not introduce a separate notation.
