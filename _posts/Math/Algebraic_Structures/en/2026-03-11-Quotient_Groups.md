---
title: "Quotient Groups"
description: "We construct the quotient group of a group using normal subgroups and equivalence relations. When the equivalence relation is compatible with the group operation, the quotient set inherits a natural group structure."
excerpt: "Normal subgroups and quotient groups"

categories: [Math / Algebraic Structures]
permalink: /en/math/algebraic_structures/quotient_groups
sidebar: 
    nav: "algebraic_structures-en"

date: 2022-11-30
weight: 5
translated_at: 2026-08-15T05:46:23+00:00
translation_source: kimi-cli
---
We previously proved in [§Algebraic Structures, §§Quotient Structures](/en/math/algebraic_structures/algebraic_structures#quotient-structures) that when an equivalence relation $R$ is compatible with the operation of a magma $A$, the quotient set $A/R$ can be endowed with a natural magma structure; moreover, at the end of [§Semigroups, Monoids, and Groups](/en/math/algebraic_structures/groups) we saw that if $A$ is a group, then the magma $A/R$ constructed in this way is also a group. This group $A/R$ is called a *quotient group*.

## Normal Subgroups

On the other hand, from [[Set Theory] §Equivalence Relations](/en/math/set_theory/equivalence_relations) we know that the following two are equivalent:

Giving an equivalence relation $R$ on a set $G$ $\iff$ Choosing a partition $(G_i)_{i\in I}$ of the set $G$
{: .text-center}

Therefore, we can ask what the condition that $R$ be compatible with the operation of $G$ means on the right-hand side.

First, assume that $R$ is compatible with the operation of $G$. Then each element of $G/R$ forms a partition of $G$, and in particular the set containing the identity is exactly $[e]$.

::: Proposition 1
For a quotient group $G/R$, the set $[e]$ is a subgroup of $G$.
:::
::: Proof
Let $a,b\in [e]$. That is, $a\sim e\sim b$. Since $R$ is compatible with the operation of $G$, multiplying both sides of $a\sim b$ on the right by $b^{-1}$ gives $ab^{-1}\sim e$. Thus $ab^{-1}\in[e]$, so by [§Semigroups, Monoids, and Groups, ⁋Proposition 15](/en/math/algebraic_structures/groups#prop15) we know that $[e]$ is a subgroup.
:::

Conversely, suppose an arbitrary subgroup $H$ of $G$ is given. Replacing $[e]$ by $H$ in the above proof, we can define the following relation.

$$a\sim_{\tiny r}b\iff ab^{-1}\in H$$

It is easy to see that $\sim_{\tiny r}$ defined in this way is an equivalence relation. In order to define a quotient group via this, this equivalence relation must be compatible with the operation of $G$. Let arbitrary $a,b,c\in G$ be given. First, if $a\sim_{\tiny r}b$ holds, then

$$(ac)(bc)^{-1}=acc^{-1}b^{-1}=ab^{-1}\in H$$

so $ac\sim_{\tiny r} bc$ holds. That is, $\sim_{\tiny r}$ is right compatible with the operation of $G$. However,

$$(ca)(cb)^{-1}=cab^{-1}c^{-1}$$

so in general $\sim_{\tiny r}$ need not be left compatible with the operation of $G$. But if for every $x\in H$ we have $cxc^{-1}\in H$ for all $c\in G$, then the right-hand side becomes an element of $H$, and thus $\sim_{\tiny r}$ defines a compatible equivalence relation on $G$.

::: Remark {#rmk}
Instead of the equivalence relation $\sim_r$, if we define the relation

$$a\sim_{\tiny l} b\iff a^{-1}b\in H$$

then $\sim_{\tiny l}$ is left compatible, and since

$$(ac)^{-1}(bc)=c^{-1}(a^{-1}b)c$$

it is not right compatible. For this relation to be right compatible, $c^{-1}xc\in H$ must hold for arbitrary $c\in G$ and arbitrary $x\in H$, which is the same condition obtained above.
:::

::: Definition 2
A subgroup $H$ of a group $G$ is called a *normal subgroup* if for every $g\in G$ and every $h\in H$, we always have $ghg^{-1}\in H$.
:::

On the other hand, since $g$ can be chosen arbitrarily, one can show that $H$ being a normal subgroup is equivalent to $gHg^{-1}=H$ holding for every $g$. By the above discussion, given a normal subgroup $H$ of $G$, we obtain the corresponding quotient group. This quotient group is denoted $G/H$.

From [Proposition 1](#prop1), for any $a\in [e]$ the identity

$$a\sim e\implies gag^{-1}\sim geg^{-1}=e$$

shows that $[e]$ is a normal subgroup. Also, when we set $H=[e]$, the corresponding $\sim_{\tiny r}$ is exactly the same as the original equivalence relation $\sim$, so $G/H$ and $G/R$ coincide. Conversely, for $\sim_{\tiny r}$ defined from an arbitrary normal subgroup $H$, $G/H=G/{\sim_{\tiny r}}$ also holds. From this we know that giving a compatible equivalence relation on $G$ is the same as choosing a normal subgroup of $G$.

## Cosets

Now consider a group $G$ and an arbitrary subgroup $H$. Even if $H$ is not normal, the relations $\sim_{\tiny r}$ and $\sim_{\tiny l}$ obtained above are still equivalence relations, so we can examine what the quotient sets $G/{\sim_{\tiny r}}$ and $G/{\sim_{\tiny l}}$ look like.

First, let us consider the elements of $G/{\sim_{\tiny r}}$. For arbitrary $a\in G$ and its equivalence class $[a]_{\tiny r}$,

$$x\in [a]_{\tiny r}\iff x\sim_{\tiny r} a\iff xa^{-1}\in H$$

Thus, defining the set $Ha$ by the formula

$$Ha:=\{ha\mid h\in H\}$$

we have $[a]_{\tiny r}=Ha$. Similarly, for $G/{\sim_{\tiny l}}$ we have $[a]_{\tiny l}=aH$. Of course, if the operation of $G$ were written as addition, these would conventionally be denoted $H+a$ and $a+H$ respectively.

::: Definition 3
The two sets $Ha$ and $aH$ defined above are called a *right coset* and a *left coset*, respectively.
:::

Therefore, given an arbitrary subgroup $H$ of $G$, the two equivalence relations $\sim_{\tiny r}$ and $\sim_{\tiny l}$ partition $G$ into right cosets and left cosets, respectively. In this case, the quotient set of $G$ by $\sim_{\tiny r}$ is denoted $H\setminus G$, and the quotient set of $G$ by $\sim_{\tiny l}$ is denoted $G/H$.[^1] In general $Ha\neq aH$, but one can easily verify that the necessary and sufficient condition for $Ha=aH$ to hold for every $a\in G$ is that $H$ is normal.

Moreover, for any $a\in G$ the maps

$${a\cdot}: H\rightarrow aH;\quad h\mapsto ah,\qquad {a^{-1}\cdot}: aH\rightarrow H;\quad ah\mapsto h$$

are inverses of each other, so all right cosets and left cosets have the same cardinality as $H$. Also, defining a function $H\setminus G\rightarrow G/H$ by the formula

$$Ha\mapsto a^{-1}H$$

one can easily check that this function is bijective. That is, $\lvert H\setminus G\rvert=\lvert G/H\rvert$.

::: Definition 4
For a group $G$ and a subgroup $H$, the *index* $[G:H]$ of $H$ is defined to be $\lvert G/H\rvert$.
:::

From the structure of $G/H$ examined above and the size of each element of $G/H$, the following proposition is obvious.

::: Proposition 5 (Lagrange)
For a group $G$ and a subgroup $H$, the identity $\lvert G\rvert=[G:H]\lvert H\rvert$ holds.
:::

This proposition holds even when $G$ or $H$ is infinite, but in the special case when they are finite, we obtain the result that <phrase>for any subgroup $H$ of a group $G$, the order $\lvert H\rvert$ divides the order $\lvert G\rvert$</phrase>.

---

**References**

**[Bou]** Bourbaki, N. Algebra I. *Elements of Mathematics*. Springer. 1998.  

---

[^1]: The notation for right cosets conflicts with that for set difference, but since right cosets will not be used much, we shall not introduce a separate notation.
