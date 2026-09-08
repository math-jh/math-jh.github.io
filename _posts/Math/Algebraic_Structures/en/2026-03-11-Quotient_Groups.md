---
title: "Quotient Groups"
description: "This covers the process of constructing quotient groups using normal subgroups and equivalence relations of a group. It shows that when the equivalence relation is compatible with the group operation, a natural group structure is given on the quotient set."
excerpt: "Normal subgroups and quotient groups"

categories: [Math / Algebraic Structures]
permalink: /en/math/algebraic_structures/quotient_groups
sidebar: 
    nav: "algebraic_structures-en"

date: 2022-11-30
weight: 5
translated_at: 2026-08-16T11:45:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-09-07T15:15:05+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
We previously proved in [§Algebraic Structures, §§Quotient Structures](/en/math/algebraic_structures/algebraic_structures#quotient-structures){: data-relation="required" } that when an equivalence relation $R$ is compatible with the operation of a magma $A$, the quotient set $A/R$ can be endowed with a magma structure in a natural way; moreover, at the end of [§Semigroups, Monoids, and Groups](/en/math/algebraic_structures/groups){: data-relation="required" }, we saw that when $A$ is a group, the magma $A/R$ constructed in this way also becomes a group. In this case, the group $A/R$ is called a *quotient group*.

## Normal Subgroups

Meanwhile, through [[Set Theory] §Equivalence Relations](/en/math/set_theory/equivalence_relations), we know that the following two are equivalent:

Giving a set $G$ an equivalence relation $R \iff$ Choosing for the set $G$ a partition $(G_i)_{i\in I}$
{: .text-center}

Therefore, we can consider what requiring the equivalence relation $R$ to be compatible with the operation of $G$ means on the right-hand side.

First, assume that $R$ is compatible with the operation of $G$. Then the elements of $G/R$ form a partition of $G$, and in particular, the only set among them containing the identity is $[e]$.

::: Proposition 1
For a quotient group $G/R$, $[e]$ is a subgroup of $G$.
:::
::: Proof
Let $a,b\in [e]$. That is, $a\sim e\sim b$. Since $R$ is compatible with the operation of $G$, multiplying both sides of $a\sim b$ on the right by $b^{-1}$ gives $ab^{-1}\sim e$. That is, $ab^{-1}\in[e]$, so by [§Semigroups, Monoids, and Groups, ⁋Proposition 15](/en/math/algebraic_structures/groups#prop15){: data-relation="required" } we know that $[e]$ is a subgroup.
:::

Conversely, for $G$, suppose an arbitrary subgroup $H$ is given. Replacing $[e]$ in the above proof with $H$, we can define the following relation.

$$a\sim_{\tiny r}b\iff ab^{-1}\in H$$

It is easy to show that $\sim_{\tiny r}$ defined in this way is an equivalence relation. In order to define a quotient group through this, this equivalence relation must be compatible with the operation of $G$. Suppose arbitrary $a,b,c\in G$ are given. First, if $a\sim_{\tiny r}b$ holds, then

$$(ac)(bc)^{-1}=acc^{-1}b^{-1}=ab^{-1}\in H$$

so $ac\sim_{\tiny r} bc$ holds. That is, $\sim_{\tiny r}$ is right compatible with the operation of $G$. However, since

$$(ca)(cb)^{-1}=cab^{-1}c^{-1}$$

in general $\sim_{\tiny r}$ need not be left compatible with the operation of $G$. But if for every $x\in H$, $cxc^{-1}\in H$ holds for all $c\in G$, then the right-hand side will be an element of $H$, and thus $\sim_{\tiny r}$ defines a compatible equivalence relation on $G$.

::: Remark {#rmk}
If instead of the equivalence relation $\sim_r$ we had defined the relation

$$a\sim_{\tiny l} b\iff a^{-1}b\in H$$

then $\sim_{\tiny l}$ is left compatible, and since

$$(ac)^{-1}(bc)=c^{-1}(a^{-1}b)c$$

it is not right compatible. In order for this relation to be right compatible, for every $c\in G$ and every $x\in H$, $c^{-1}xc\in H$ must hold, which is the same as the condition obtained above.
:::

::: Definition 2
For a group $G$, a subgroup $H$ is called a *normal subgroup* if for every $g\in G$ and every $h\in H$, $ghg^{-1}\in H$ always holds.
:::

Meanwhile, since $g$ can be chosen arbitrarily, one can show that $H$ being a normal subgroup is equivalent to having, for every $g$, $gHg^{-1}=H$. By the above discussion, for $G$, given a normal subgroup $H$, we obtain the corresponding quotient group. This quotient group is denoted $G/H$.

From [Proposition 1](#prop1){: data-relation="required" }, for any $a\in [e]$, from the formula

$$a\sim e\implies gag^{-1}\sim geg^{-1}=e$$

we know that $[e]$ is a normal subgroup. Also, when setting $H=[e]$, the corresponding $\sim_{\tiny r}$ is exactly identical to the original equivalence relation $\sim$, so $G/H$ and $G/R$ are equal to each other. Conversely, for any normal subgroup $H$, the relation $\sim_{\tiny r}$ defined from it also satisfies $G/H=G/{\sim_{\tiny r}}$. From this, we know that giving a compatible equivalence relation on $G$ is equivalent to choosing a normal subgroup of $G$.

## Cosets

Now consider a group $G$ and an arbitrary subgroup $H$. Even if $H$ is not normal, $\sim_{\tiny r}$ and $\sim_{\tiny l}$ obtained in the discussion above are nonetheless equivalence relations, so we can examine what the quotient sets $G/{\sim_{\tiny r}}$ and $G/{\sim_{\tiny l}}$ look like.

First, let us consider the elements of $G/{\sim_{\tiny r}}$. For any $a\in G$ and its equivalence class $[a]_{\tiny r}$, we know that

$$x\in [a]_{\tiny r}\iff x\sim_{\tiny r} a\iff xa^{-1}\in H$$

holds. Therefore, defining the set $Ha$ by the formula

$$Ha:=\{ha\mid h\in H\}$$

we have $[a]_{\tiny r}=Ha$. Similarly, for $G/{\sim_{\tiny l}}$, we have $[a]_{\tiny l}=aH$. Of course, if the operation of $G$ were written additively, it is customary to denote these by $H+a$ and $a+H$, respectively.

::: Definition 3
The two sets $Ha$ and $aH$ defined above are called a *right coset* and a *left coset*, respectively.
:::

Therefore, for $G$, given an arbitrary subgroup $H$, the two equivalence relations $\sim_{\tiny r}$ and $\sim_{\tiny l}$ partition $G$ into right cosets and left cosets, respectively. In this case, with respect to $\sim_{\tiny r}$, the quotient set of $G$ is denoted $H\setminus G$, and with respect to $\sim_{\tiny l}$, the quotient set of $G$ is denoted $G/H$.[^1] In general, $Ha\neq aH$, but one can easily verify that for any $a\in G$, the necessary and sufficient condition for $Ha=aH$ to hold is that $H$ is normal.

Moreover, for any $a\in G$, the maps

$${a\cdot}: H\rightarrow aH;\quad h\mapsto ah,\qquad {a^{-1}\cdot}: aH\rightarrow H;\quad ah\mapsto h$$

are inverses of each other, so all right cosets and left cosets have the same cardinality as $H$. Also, defining a function $H\setminus G\rightarrow G/H$ by the formula

$$Ha\mapsto a^{-1}H$$

one can easily check that this function is bijective. That is, $\lvert H\setminus G\rvert=\lvert G/H\rvert$.

::: Definition 4
For a group $G$ and a subgroup $H$, the *index* of $H$, denoted $[G:H]$, is defined to be $\lvert G/H\rvert$.
:::

From the structure of $G/H$ examined above and the size of each element of $G/H$, the following proposition is obvious.

::: Proposition 5 (Lagrange)
For a group $G$ and a subgroup $H$, $\lvert G\rvert=[G:H]\lvert H\rvert$ holds.
:::

This proposition holds even when $G$ or $H$ is an infinite set, but especially when they are finite, we obtain the result that <phrase>for a group $G$ and any subgroup $H$, $\lvert H\rvert$ is a divisor of $\lvert G\rvert$</phrase>.

---

**References**

**[Bou]** Bourbaki, N. Algebra I. *Elements of Mathematics*. Springer. 1998.  

---

[^1]: The notation for right cosets conflicts with that for set difference, but since right cosets will not be used much, we shall not introduce a separate notation.
