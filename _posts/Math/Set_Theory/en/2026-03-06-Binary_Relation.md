---
title: "Binary Relations"
description: "Defines a binary relation as a set of ordered pairs, and discusses the existence conditions of the two sets that constitute the relation along with the concepts of projection, source, and target."
excerpt: "The definition of binary relations"

categories: [Math / Set Theory]
permalink: /en/math/set_theory/binary_relation


sidebar: 
    nav: "set_theory-en"

date: 2021-08-14

weight: 3
translated_at: 2026-06-02T10:30:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-10-31T23:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
## Binary Relations

We begin with the definition. The following definition is nothing special; it merely gives a name to the *set of ordered pairs* that appeared in [§Ordered Pairs](/en/math/set_theory/ordered_pair#ordered-pairs){: data-lid="v0g57" } when we explained the motivation for introducing ordered pairs.

::: Definition 1
A set $R$ is called a *binary relation* if every element of $R$ is an ordered pair.[^1]
:::

Thus, equality ($=$) defined between sets as follows can no longer be called a binary relation.

::: Example 2
If $=$ were a binary relation between sets, then the set representing it

$$E=\{(A,A)\mid\text{$A$ any set}\}$$

would exist.
:::

If such an $E$ exists, then by the following proposition a universal set must also exist, which contradicts [§ZFC Axioms, ⁋Example 4](/en/math/set_theory/zfc_axioms#ex4){: data-lid="zvv91" }. Therefore, $=$ defined between all sets cannot be a binary relation.

::: Proposition 3
Let $R$ be a binary relation. Then there exist unique sets $A$, $B$ such that

<ul>
<li> $x\in A$ is equivalent to the existence of some $y$ such that $(x,y)\in R$, and</li>
<li> $y\in B$ is equivalent to the existence of some $x$ such that $(x,y)\in R$.</li>
</ul>
:::
::: Proof
Let $R$ be a binary relation and consider $\bigcup(\bigcup R)$. By calculation, we see that $(x,y)\in R\implies x,y\in\bigcup(\bigcup R)$. If we define $P$ by

> $P(s)$: there exists some $t$ such that $(s,t)\in R$.

we obtain the following set

$$A=\left\{x\mid\left(x\in\bigcup\left(\bigcup R\right)\right)\wedge P(x)\right\}$$

Thus the first claim holds, and similarly defining the property $Q$ by

> $Q(t)$: there exists some $s$ such that $(s,t)\in R$.

we obtain the set $B$. Also, since any two sets satisfying each of the above conditions have the same elements, by extensionality such $A$ and $B$ are unique.
:::

Just as in [§Ordered Pairs, ⁋Definition 7](/en/math/set_theory/ordered_pair#def7){: data-lid="97c39" }, we call these the first and second *projections*, respectively, and write them as $\pr_1R$ and $\pr_2R$.

Occasionally, one needs to make clear which sets the first and second components of a binary relation belong to. For this purpose, given two sets $A,B$, and satisfying $\pr_1R\subseteq A$, $\pr_2R\subseteq B$, a binary relation $R$ is also considered as a triple $(R,A,B)$. In this case, we call $A$ the *source* of $R$ and $B$ the *target* of $R$, and in such situations, even for the same set $R$, we consider $(R,A,B)$ and $(R,A',B')$ to be different.

::: remark Remark {#rmk}
Suppose that, satisfying the above conditions $\pr_1R\subseteq A$, $\pr_2R\subseteq B$, a binary relation $R$ is given. By [§Ordered Pairs, ⁋Proposition 9](/en/math/set_theory/ordered_pair#prop9){: data-lid="f7fdx" },

$$R\subseteq \pr_1 R\times\pr_2R\subseteq A\times B$$

and thus the cartesian product $A\times B$ can be said to be the largest among binary relations with source $A$ and target $B$.
:::

## Domain and Image of a Binary Relation

::: Definition 4
Consider a binary relation $(R,A,B)$ and a subset $A'\subseteq A$. Then the set of all elements related by $R$ to elements of $A'$ is called the *image* under $R$ of $A'$, and is denoted by $R(A')$.
:::

Writing out the above definition as a formula, we have

$$R(A')=\bigcup_{x\in A'} \{y\in B\mid(x,y)\in R\}$$

Strictly speaking, the set $\{y\in B\mid(x,y)\in R\}$ on the right-hand side, if for the binary relation $R$ the target $B$ is not given, takes a form such as

$$\{y\mid(x,y)\in R\}$$

and, unlike the set above, the bounding set required by the comprehension schema does not appear in the notation.

This kind of issue is something we must always be careful about when studying set theory. However, since our purpose is not to study set theory, but to prove propositions that will be useful elsewhere, from now on we will pass over such minor expository issues without much thought.

::: Proposition 5
Let $R$ be a binary relation, and consider any set $A$ and its subset $X$. Then $R(X)\subseteq R(A)$ holds.
:::

::: Proof
Let $y\in R(X)$. Then there exists some $x\in X$ such that $(x,y)\in R$. Now since $X\subseteq A$, we have $x\in A$, and thus $y\in R(A)$.
:::

By the above proposition, for any $A$ we have 

$$R(A)=\pr_2\{z\in R\mid\text{$\pr_1z\in A$}\}\subseteq\pr_2R$$

and therefore $R(A)\subseteq\pr_2R$ holds. In particular, if $A=\emptyset$ then $R(A)=\emptyset$, and more generally if $A\cap\pr_1R=\emptyset$ then $R(A)=\emptyset$. 

If for some $x$ we have $A=\{x\}$, we can think of $R(A)$ as if it were the value at $x$ of $R$. 

::: Definition 6
For a binary relation $R$, the set $R(\{x\})$ is called the *section* at $x$ of $R$.
:::

As if it were the value at $x$ of $R$, this set is also written as $R(x)$. This *value* is not unique, and therefore $R(x)$ may also contain more than one element.

---
**References**

**[HJJ]** K. Hrbacek, T.J. Jeck, and T. Jech. *Introduction to Set Theory*. Lecture Notes in Pure and Applied Mathematics. M. Dekker, 1978.  
**[Bou]** N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---

[^1]: In **[Bou]**, such a set is called a *graph*, and binary relations are distinguished into those that have a graph and those that do not. This is not a very common definition, so we follow **[HJJ]** and use the above definition as is. In this case, the definition of the word "relation" becomes somewhat ambiguous, but we pass over this without further definition.
