---
title: "Group Action"
description: "We examine how monoids and groups act on sets, covering the definitions of left and right actions and explaining the relationship between the two actions via the opposite magma."
excerpt: "Group action"

categories: [Math / Algebraic Structures]
permalink: /en/math/algebraic_structures/group_actions
sidebar: 
    nav: "algebraic_structures-en"

date: 2023-02-14
weight: 11
translated_at: 2026-08-16T13:45:05+00:00
translation_source: kimi-cli
last_polished_at: 2026-09-08T11:15:05+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
One effective strategy when dealing with complex algebraic structures is to study how a given algebraic object acts on other algebraic objects, rather than analyzing the structure directly. We are particularly interested in group actions; as always, we first consider the slightly more general case of a monoid acting on a set.

## Monoid acting on a set

::: Definition 1
Fix a monoidal category $(\mathcal{A},\otimes, I)$ and a monoid object $(A,\cdot, 1)$ in $\mathcal{A}$. A morphism $\rho: A\otimes E\rightarrow E$ is called a *left action* of $A$ defined on an object $E\in\obj(\mathcal{A})$ if the following two diagrams both commute.

{% diagram Math/Algebraic_Structures/Group_Actions-1.svg width="31.84em" alt="left_module" %}

Here $I\otimes E \rightarrow E$ is the left unitor. We write this situation as $A\circlearrowright E$.

Similarly, a morphism $\rho: E\otimes A\rightarrow E$ is called a *right action* of $A$ defined on an object $E\in\obj(\mathcal{A})$ if the following two diagrams both commute.

{% diagram Math/Algebraic_Structures/Group_Actions-2.svg width="31.84em" alt="right_module" %}

Likewise $E\otimes I \rightarrow E$ is the right unitor. We write this situation as $E \circlearrowleft A$.
:::

Fix a monoid object $(M,\cdot,1)$ in the monoidal category $(\Set,\times, I)$. Then through this we can consider a left action of $M$ defined on an arbitrary set $E$. Swapping the order of factors as $M\times E\cong E\times M$ and applying [\[Set Theory\] §Product of Sets, ⁋Proposition 4](/en/math/set_theory/product_of_sets#prop4){: data-relation="required" } yields

$$\Hom_\Set(M\times E,E)\cong\Hom_\Set(M,\Hom_\Set(E,E))\cong\Hom_\Set(M, \End(E))$$

so any left action defines a function $M \rightarrow \End(E)$. The commutativity of the two diagrams in [Definition 1](#def1){: data-relation="required" } is then equivalent to this function being a monoid homomorphism.

In other words, saying that $M$ acts on $E$ from the left means that for arbitrary $\alpha,\beta\in M$ and $x\in E$, the identities

$$(\alpha\beta)\cdot x=\alpha\cdot(\beta\cdot x),\qquad e\cdot x=x$$

hold.

In general, we consider the case where a given object acts on another from the left as above, but sometimes acting from the right is also natural. By the following definition, these are in fact the same.

::: Definition 2
For an arbitrary magma $(M,\ast)$, the *opposite magma* $(M^\op,\ast^\op)$ of $M$ is the magma defined as follows.

1. As a set, $M^\op=M$.
2. For arbitrary $x,y\in M^\op$, $x\ast^\op y$ is defined to be $y\ast x$.
:::

Then one verifies that a right $M$-action is the same as a left $M^\op$-action. Rewriting this, we have

$$x\cdot(\beta\alpha)=(x\cdot\beta)\cdot\alpha,\qquad x\cdot e=x$$

In this way, left actions and right actions differ only in notation and essentially have the same meaning. Therefore, when developing the general theory in what follows, we assume that every action is a left action.

::: Example 3
Suppose a monoid $M$ acts on a set $E$. Then there is a natural $M$-action on $\mathcal{P}(E)$ as well. For arbitrary $\alpha\in M$ and $A\in \mathcal{P}(E)$, define $\alpha\cdot A$ by

$$\alpha\cdot A=\{\alpha\cdot a\mid a\in A\}$$

Then

$$(\alpha\beta)\cdot A=\{(\alpha\beta)\cdot a\mid a\in A\}=\{\alpha\cdot(\beta\cdot a)\mid a\in A\}=\alpha\cdot\{\beta\cdot a\mid a\in A\}=\alpha\cdot(\beta\cdot A)$$

and $e\cdot A=\{e\cdot a\mid a\in A\}=A$, so this defines an $M$-action on $\mathcal{P}(E)$.
:::

For convenience of discussion, we make the following definition.

::: Definition 4
When a monoid $M$ defines a left action on a set $E$, we call $E$ together with this action a (left) $M$-set.
:::

## $M$-set homomorphism

::: Definition 5
Suppose a monoid $M$ is fixed, and let $E,E'$ be $M$-sets. A function $f:E\rightarrow E'$ is called an *$M$-set homomorphism* if for all $x\in E$ and $\alpha\in M$,

$$f(\alpha\cdot x)=\alpha\cdot f(x)$$

holds.
:::

It is easy to verify that the composition of $M$-set homomorphisms is an $M$-set homomorphism, and that the identity function is an $M$-set homomorphism. That is, the collection of (left) $M$-sets forms a category, which we denote by $\lset{M}$.

Fix an arbitrary monoid homomorphism $\phi:M \rightarrow M'$. Then for any $M'$-set $E$, we can regard $E$ as an $M$-set via the composition

$$M\overset{\phi}{\longrightarrow}M'\overset{\rho}{\longrightarrow}\End(E)$$

Let us write the action defined in this way as $\phi^\ast\rho$. Then explicitly, $\phi^\ast\rho$ is the action defined by

$$(\phi^\ast\rho)(\alpha)(x)=\rho(\phi(\alpha))(x)$$

for arbitrary $\alpha\in M$ and $x\in E$. Now suppose two $M'$-actions $\rho:M' \rightarrow \End(E)$ and $\rho':M' \rightarrow \End(E')$ are given, and an $M'$-set homomorphism $f:E \rightarrow E'$ between them is given. Then for arbitrary $\alpha\in M$ and $x\in E$,

$$f((\phi^\ast\rho)(\alpha)(x))=f(\rho(\phi(\alpha))(x))=\rho'(\phi(\alpha))(f(x))=(\phi^\ast\rho')(\alpha)(f(x))$$

holds. That is, any monoid homomorphism $\phi:M \rightarrow M'$ defines a functor from $\lset{M'}$ to $\lset{M}$. In particular, if $\iota$ is the inclusion of a submonoid, this is the restriction of a monoid action.

On the other hand, if $(E_i)$ is a collection of $M$-sets, then defining an action of $M$ on their product $\prod E_i$ via the formula

$$\alpha\cdot(x_i)_{i\in I}=(\alpha\cdot x_i)_{i\in I}$$

again yields an $M$-set. Similarly, if a subset $F$ of an $M$-set $E$ satisfies

$$x\in F\implies \alpha\cdot x\in F\text{ for all $\alpha\in M$}$$

then $F$ is called an $M$-subset. Also, if an equivalence relation $\sim$ defined on an $M$-set is compatible with the action of $M$, that is, if

$$x\sim y\implies\alpha\cdot x\sim\alpha\cdot y$$

always holds, then $E/\mathnormal{\sim}$ naturally carries the structure of an $M$-set.

## Stabilizer, fixer

::: Definition 6
Let an $M$-set $E$ and its subset $A$ be given.
- The *stabilizer* of $A$ means the set satisfying $\alpha A\subseteq A$ of elements $\alpha$, denoted $\stab (A)$.
- The *strict stabilizer* of $A$ means the set satisfying $\alpha A=A$ of elements $\alpha$, denoted $\Stab(A)$.
- The *fixer* of $A$ means, for all $a\in A$, the set satisfying $\alpha a=a$ of elements $\alpha$, denoted $\Fix(A)$.
:::

For any subset $A$, $\Fix(A)\subseteq \Stab(A)\subseteq \stab(A)$ holds. Also, it is obvious that $e\in\Fix(A)$.

::: Proposition 7
For an $M$-set $E$ and its subset $A$, $\stab(A)$, $\Stab (A)$, and $\Fix(A)$ are submonoids of $M$.
:::
::: Proof
It suffices to show that these sets are closed under the operation. If $\alpha,\beta\in\stab(A)$, then from

$$(\alpha\beta)A=\alpha(\beta A)\subseteq \alpha A\subseteq A$$

we see that $\alpha\beta\in \stab(A)$. Similarly, if $\alpha,\beta\in\Stab(A)$, then

$$(\alpha\beta)A=\alpha(\beta A)=\alpha A=A$$

so $\alpha\beta\in \Stab(A)$ and the claim holds. Finally, if $\alpha,\beta\in\Fix(A)$, then for any $a\in A$,

$$(\alpha\beta)a=\alpha(\beta a)=\alpha a=a$$

so $\alpha\beta\in \Fix(A)$.
:::

::: Corollary 8
Let a group $G$ be given. For a $G$-set $E$ and its subset $A$, $\Stab (A)$ and $\Fix(A)$ are subgroups of $G$, and in particular $\Fix(A)$ is a normal subgroup of $\Stab(A)$.
:::
::: Proof
For the first claim, it suffices to show that the given sets are closed under inverses, which is clear from the fact that for any $\alpha\in\Stab(A)$, the equation

$$A=(\alpha^{-1}\alpha)A=\alpha^{-1}(\alpha A)=\alpha^{-1}A$$

holds, and for any $\alpha\in\Fix(A)$ and $a\in A$,

$$a=(\alpha^{-1}\alpha)a=\alpha^{-1}(\alpha a)=\alpha^{-1}a$$

holds. For the second claim, suppose arbitrary $\alpha\in\Fix(A)$ and $\beta\in\Stab(A)$ are given; if for any $a\in A$ we compute $(\beta\alpha\beta^{-1})a$, then

$$(\beta\alpha\beta^{-1})a=\beta(\alpha(\beta^{-1}a))=\beta\beta^{-1}a=a$$

so $\beta\alpha\beta^{-1}\in\Fix(A)$, and the claim holds.
:::

When a group $G$ acts on a set $E$, for any $x\in E$, since $g^{-1}\cdot(g\cdot x)=(g^{-1}g)\cdot x=x$, $\rho_{g^{-1}}$ is the inverse function of $\rho_g$. Therefore $\rho_g$ is necessarily bijective, from which $\im\rho\subseteq \Aut(E)$ always holds.

## Inner automorphisms

We now consider the case where the set $E$ is given additional structure. For instance, suppose $E$ also has a monoid structure and a given monoid $M$ acts on $E$; then the $M$-action is given by a monoid homomorphism $M \rightarrow\End(E)=\End_\Mon(E)$.

In particular, consider the case where a group $G$ acts on itself. If a homomorphism $\rho:G\rightarrow\End(G)=\End_\Grp(G)$ is given, then since a bijective group homomorphism is always a group isomorphism ([§Algebraic Structures, ⁋Definition 6](/en/math/algebraic_structures/algebraic_structures#def6){: data-relation="weak" }), we know that if $G$ acts on itself, this must necessarily take the form of a group homomorphism $G \rightarrow \Aut(G)$.

Among group actions defined on a group itself, the following example in particular is worth keeping in mind.

::: Proposition 9
For a group $G$ and any element $g$, if we define $\rho_g\in\Aut(G)$ by the equation

$$\rho_g(x)=gxg^{-1}$$

then the correspondence $\rho:g\mapsto \rho_g$ is a group homomorphism.
:::
::: Proof
From the fact that for any $x,y\in G$,

$$\rho_g(xy)=g(xy)g^{-1}=(gxg^{-1})(gyg^{-1})=\rho_g(x)\rho_g(y)$$

holds, we see that $\rho_g$ is a group homomorphism.

On the other hand, for any $g,h\in G$ and $x\in G$,

$$\rho_{gh}(x)=(gh)x(gh)^{-1}=g(hxh^{-1})g^{-1}=(\rho_g\circ\rho_h)(x)$$

so $\rho_{gh}=\rho_g\circ\rho_h$. In particular, substituting $h=g^{-1}$ gives $\rho_g\circ\rho_{g^{-1}}=\rho_e=\id_G$, so each $\rho_g$ is bijective, and therefore $\im\rho\subseteq\Aut(G)$ holds. That is, $\rho:g\mapsto \rho_g$ is a group homomorphism from $G$ to $\Aut(G)$.
:::

::: Definition 10
Let a group $G$ be given. We call the automorphism $\rho_g$ of [Proposition 9](#prop9){: data-relation="required" } the *inner automorphism* defined by $g$, and denote the collection of these by $\Inn(G)$.
:::

::: Proposition 11
For a group $G$, the collection $\Inn(G)$ of inner automorphisms is a normal subgroup of $\Aut(G)$.
:::
::: Proof
Since $\Inn(G)$ is the image of the group homomorphism $\rho:G\rightarrow\Aut(G)$, it is obvious that it is a subgroup of $\Aut(G)$; thus it suffices to show that $\Inn(G)$ is a *normal* subgroup.

Choose an arbitrary $f\in\Aut(G)$, and fix $g\in G$ arbitrarily. We must show that $f\circ\rho_g\circ f^{-1}\in \Inn(G)$. This is obvious since for any $x\in G$,

$$(f\circ\rho_g\circ f^{-1})(x)=f(gf^{-1}(x)g^{-1})=f(g)xf(g^{-1})=\rho_{f(g)}(x)$$

holds.
:::

On the other hand, $\rho:G\rightarrow\Inn(G)$ is surjective, and therefore by [§Group Isomorphisms, ⁋Theorem 2](/en/math/algebraic_structures/isomorphism_theorems#thm2){: data-relation="required" },

$$G/\ker\rho\cong\Inn(G)$$

holds. $\ker\rho$ also has a special name.

::: Definition 12
For a group $G$ and the group homomorphism $\rho:G\rightarrow\Inn(G)$ defined in [Proposition 9](#prop9){: data-relation="required" }, we call $\ker\rho$ the *center* of $G$ and denote it by $Z(G)$.
:::

By definition,

$$g\in\ker\rho\iff\rho_g=\id_G\iff gxg^{-1}=x\quad\text{for all $x\in G$}$$

holds, so in the situation where $G$ acts on itself by inner automorphisms, the fixer $\Fix(G)$ is precisely $Z(G)$. More generally, for any subset $A\subseteq G$, we define the fixer of $A$, $\Fix(A)$, to be the *centralizer* of $A$, $C_G(A)$. Similarly, we define the *normalizer* of $A$, $N_G(A)$, to be $\Stab(A)$.

## Orbit-stabilizer theorem

Now we again consider a group action defined on a general set $E$. First, let us define the following.

::: Definition 13
Suppose that on a set $E$, an action of a group $G$ is defined. Then the *orbit* of an element $x\in E$ is given by the following set:

$$G\cdot x=\{g\cdot x\mid g\in G\}$$
:::

Then the following relation defined on $E$,

$$x\sim y\iff G\cdot x=G\cdot y\tag{$\ast$}$$

is an equivalence relation, so the quotient set $E/{\sim}$ is defined, and this is the set of orbits.

::: Theorem 14 (Orbit-stabilizer theorem)
Suppose that on a set $E$, an action of a group $G$ is given. Then the identity

$$\lvert G\cdot x\rvert=[G:\Stab(x)]$$

holds.
:::
::: Proof
If we define a function $p:G \rightarrow G\cdot x$ by $g\mapsto g\cdot x$, then by the definition of $G\cdot x$, this function is surjective. On the other hand, since $p(g_1)=p(g_2)\iff g_1^{-1}g_2\in \Stab(x)$, we obtain the desired result from the canonical decomposition following [\[Set Theory\] §Examples of Equivalence Relations, ⁋Proposition 7](/en/math/set_theory/examples_of_equivalence#prop7){: data-relation="required" }.
:::

Therefore, if $G$ is finite, then by [§Quotient Groups, ⁋Proposition 5](/en/math/algebraic_structures/quotient_groups#prop5){: data-relation="required" } we obtain the identity

$$\lvert G\cdot x\rvert=\frac{\lvert G\rvert}{\lvert\Stab(x)\rvert}\tag{$\ast\ast$}$$

Similarly, suppose $G$ is finite, and $G$ acts on a finite set $E$. If we define $E^g$ as the set of elements fixed by $g$,

$$E^g=\{x\in E\mid g\cdot x=x\}$$

then

$$\sum_{g\in G}\lvert E^g\rvert=\# \{(g, x)\in G\times E\mid g\cdot x=x\}=\sum_{x\in E}\lvert \Stab(x)\rvert$$

holds. Now from ($\ast\ast$), we have

$$\sum_{x\in E}\lvert \Stab(x)\rvert=\sum_{x\in E}\frac{\lvert G\rvert}{\lvert G\cdot x\rvert}$$

On the other hand, considering the quotient set defined from ($\ast$), $E/{\sim}$, the above sum can again be written as

$$\sum_{x\in E}\frac{\lvert G\rvert}{\lvert G\cdot x\rvert}=\lvert G\rvert\sum_{O\in E/{\sim}}\sum_{x\in O}\frac{1}{\lvert O\rvert}=\lvert G\rvert\sum_{O\in E/{\sim}} 1=\lvert G\rvert\lvert E/{\sim}\rvert$$

From this we obtain the following lemma.

::: Lemma 15
Suppose a finite group $G$ acts on a finite set $E$, and let $E/{\sim}$ be the quotient set of $E$ consisting of orbits. Then the identity

$$\lvert E/{\sim}\rvert=\frac{1}{\lvert G\rvert}\sum_{g\in G}\lvert E^g\rvert$$

holds.
:::

---

**References**

**[Bou]** Bourbaki, N. Algebra I. *Elements of Mathematics*. Springer. 1998.  

---
