---
title: "Group Actions"
description: "We examine how monoids and groups act on sets, covering the definitions of left and right actions and explaining the relationship between the two via the opposite magma."
excerpt: "Group actions on sets"

categories: [Math / Algebraic Structures]
permalink: /en/math/algebraic_structures/group_actions
sidebar: 
    nav: "algebraic_structures-en"

date: 2023-02-14
weight: 11
translated_at: 2026-08-16T13:45:05+00:00
translation_source: kimi-cli
last_polished_at: 2026-08-16T13:45:05+00:00
---
One effective strategy when dealing with complex algebraic structures is to study how a given algebraic object acts on other algebraic objects, rather than analyzing the structure directly. We are particularly interested in group actions; as always, we begin with the slightly more general case of a monoid acting on a set.

## Monoid acting on a set

::: Definition 1
Fix a monoidal category $(\mathcal{A},\otimes, I)$ and a monoid object $(A,\cdot, 1)$ in $\mathcal{A}$. A morphism $\rho: A\otimes E\rightarrow E$ is called a *left action* of $A$ on an object $E\in\obj(\mathcal{A})$ if the following two diagrams both commute.

{% diagram Math/Algebraic_Structures/Group_Actions-1.svg width="31.84em" alt="left_module" %}

Here $I\otimes E \rightarrow E$ is the left unitor. We write this situation as $A\circlearrowright E$.

Similarly, a morphism $\rho: E\otimes A\rightarrow E$ is called a *right action* of $A$ on an object $E\in\obj(\mathcal{A})$ if the following two diagrams both commute.

{% diagram Math/Algebraic_Structures/Group_Actions-2.svg width="31.84em" alt="right_module" %}

Likewise $E\otimes I \rightarrow E$ is the right unitor. We write this situation as $E \circlearrowleft A$.
:::

Fix a monoid object $(M,\cdot,1)$ in the monoidal category $(\Set,\times, I)$. Then we can consider a left action of $M$ on an arbitrary set $E$. Swapping the factors $M\times E\cong E\times M$ and applying [\[Set Theory\] §Product of Sets, ⁋Proposition 4](/en/math/set_theory/product_of_sets#prop4) yields

$$\Hom_\Set(M\times E,E)\cong\Hom_\Set(M,\Hom_\Set(E,E))\cong\Hom_\Set(M, \End(E))$$

so any left action defines a function $M \rightarrow \End(E)$. The commutativity of the two diagrams in [Definition 1](#def1) is equivalent to this function being a monoid homomorphism.

In other words, saying that $M$ acts on $E$ from the left means that for arbitrary $\alpha,\beta\in M$ and $x\in E$, the identities

$$(\alpha\beta)\cdot x=\alpha\cdot(\beta\cdot x),\qquad e\cdot x=x$$

hold.

In general, we consider the situation where a given object acts on another from the left as above, but sometimes acting from the right is more natural. The following definition shows that these are essentially the same.

::: Definition 2
For an arbitrary magma $(M,\ast)$, the *opposite magma* $(M^\op,\ast^\op)$ of $M$ is the magma defined as follows.

1. As a set, $M^\op=M$.
2. For arbitrary $x,y\in M^\op$, the product $x\ast^\op y$ is defined to be $y\ast x$.
:::

Then one verifies that a right $M$-action is the same as a left $M^\op$-action. Rewriting this, we have

$$x\cdot(\beta\alpha)=(x\cdot\beta)\cdot\alpha,\qquad x\cdot e=x$$

Thus left and right actions differ only in notation and are essentially the same. Therefore, in developing the general theory below, we assume every action is a left action.

::: Example 3
Suppose a monoid $M$ acts on a set $E$. Then there is a natural $M$-action on $\mathcal{P}(E)$ as well. For arbitrary $\alpha\in M$ and $A\in \mathcal{P}(E)$, define $\alpha\cdot A$ by

$$\alpha\cdot A=\{\alpha\cdot a\mid a\in A\}$$

Then

$$(\alpha\beta)\cdot A=\{(\alpha\beta)\cdot a\mid a\in A\}=\{\alpha\cdot(\beta\cdot a)\mid a\in A\}=\alpha\cdot\{\beta\cdot a\mid a\in A\}=\alpha\cdot(\beta\cdot A)$$

and $e\cdot A=\{e\cdot a\mid a\in A\}=A$, so this defines an $M$-action on $\mathcal{P}(E)$.
:::

For convenience, we make the following definition.

::: Definition 4
When a monoid $M$ defines a left action on a set $E$, we call $E$ together with this action a (left) $M$-set.
:::

## $M$-set homomorphism

::: Definition 5
Fix a monoid $M$, and let $E,E'$ be $M$-sets. A function $f:E\rightarrow E'$ is called an *$M$-set homomorphism* if for all $x\in E$ and $\alpha\in M$,

$$f(\alpha\cdot x)=\alpha\cdot f(x)$$

holds.
:::

It is easy to verify that the composition of $M$-set homomorphisms is an $M$-set homomorphism, and that the identity function is an $M$-set homomorphism. Thus the collection of (left) $M$-sets forms a category, which we denote by $\lset{M}$.

Fix an arbitrary monoid homomorphism $\phi:M \rightarrow M'$. Then for any $M'$-set $E$, we can regard $E$ as an $M$-set via the composition

$$M\overset{\phi}{\longrightarrow}M'\overset{\rho}{\longrightarrow}\End(E)$$

Let us write the action defined in this way as $\phi^\ast\rho$. Then explicitly, $\phi^\ast\rho$ is the action defined by

$$(\phi^\ast\rho)(\alpha)(x)=\rho(\phi(\alpha))(x)$$

for arbitrary $\alpha\in M$ and $x\in E$. Now suppose two $M'$-actions $\rho:M' \rightarrow \End(E)$ and $\rho':M' \rightarrow \End(E')$ are given, along with an $M'$-set homomorphism $f:E \rightarrow E'$ between them. Then for arbitrary $\alpha\in M$ and $x\in E$,

$$f((\phi^\ast\rho)(\alpha)(x))=f(\rho(\phi(\alpha))(x))=\rho'(\phi(\alpha))(f(x))=(\phi^\ast\rho')(\alpha)(f(x))$$

holds. That is, any monoid homomorphism $\phi:M \rightarrow M'$ defines a functor from $\lset{M'}$ to $\lset{M}$. In particular, if $\iota$ is the inclusion of a submonoid, this becomes the restriction of a monoid action.

On the other hand, if $(E_i)$ is a collection of $M$-sets, then their product $\prod E_i$ with the $M$-action defined by

$$\alpha\cdot(x_i)_{i\in I}=(\alpha\cdot x_i)_{i\in I}$$

is again an $M$-set. Similarly, if a subset $F$ of an $M$-set $E$ satisfies

$$x\in F\implies \alpha\cdot x\in F\text{ for all $\alpha\in M$}$$

then we call $F$ an $M$-subset. Also, if an equivalence relation $\sim$ on an $M$-set is compatible with the action of $M$, that is, if

$$x\sim y\implies\alpha\cdot x\sim\alpha\cdot y$$

always holds, then $E/\mathnormal{\sim}$ naturally carries the structure of an $M$-set.

## Stabilizer, fixer

::: Definition 6
Let $A$ be a subset of an $M$-set $E$.
- The *stabilizer* of $A$ is the set of $\alpha$ satisfying $\alpha A\subseteq A$, denoted $\stab (A)$.
- The *strict stabilizer* of $A$ is the set of $\alpha$ satisfying $\alpha A=A$, denoted $\Stab(A)$.
- The *fixer* of $A$ is the set of $\alpha$ satisfying $\alpha a=a$ for all $a\in A$, denoted $\Fix(A)$.
:::

For any subset $A$, we have $\Fix(A)\subseteq \Stab(A)\subseteq \stab(A)$. Also, $e\in\Fix(A)$ is obvious.

::: Proposition 7
For an $M$-set $E$ and its subset $A$, the sets $\stab(A)$, $\Stab (A)$, and $\Fix(A)$ are submonoids of $M$.
:::
::: Proof
It suffices to show that these sets are closed under the operation. If $\alpha,\beta\in\stab(A)$, then from

$$(\alpha\beta)A=\alpha(\beta A)\subseteq \alpha A\subseteq A$$

we see that $\alpha\beta\in \stab(A)$. Similarly, if $\alpha,\beta\in\Stab(A)$, then

$$(\alpha\beta)A=\alpha(\beta A)=\alpha A=A$$

so $\alpha\beta\in \Stab(A)$ and the claim holds. Finally, if $\alpha,\beta\in\Fix(A)$, then for arbitrary $a\in A$,

$$(\alpha\beta)a=\alpha(\beta a)=\alpha a=a$$

so $\alpha\beta\in \Fix(A)$.
:::

::: Corollary 8
Let a group $G$ be given. For a $G$-set $E$ and its subset $A$, the sets $\Stab (A)$ and $\Fix(A)$ are subgroups of $G$, and in particular $\Fix(A)$ is a normal subgroup of $\Stab(A)$.
:::
::: Proof
For the first claim, it suffices to show that the given sets are closed under inverses, and this follows from the identities: for arbitrary $\alpha\in\Stab(A)$,

$$A=(\alpha^{-1}\alpha)A=\alpha^{-1}(\alpha A)=\alpha^{-1}A$$

holds, and for arbitrary $\alpha\in\Fix(A)$ and $a\in A$,

$$a=(\alpha^{-1}\alpha)a=\alpha^{-1}(\alpha a)=\alpha^{-1}a$$

holds. For the second claim, given arbitrary $\alpha\in\Fix(A)$ and $\beta\in\Stab(A)$, computing $(\beta\alpha\beta^{-1})a$ for arbitrary $a\in A$ gives

$$(\beta\alpha\beta^{-1})a=\beta(\alpha(\beta^{-1}a))=\beta\beta^{-1}a=a$$

so $\beta\alpha\beta^{-1}\in\Fix(A)$, as desired.
:::

When a group $G$ acts on a set $E$, for any $x\in E$ we have $g^{-1}\cdot(g\cdot x)=(g^{-1}g)\cdot x=x$, so $\rho_{g^{-1}}$ is the inverse function of $\rho_g$. Hence $\rho_g$ is necessarily bijective, and therefore $\im\rho\subseteq \Aut(E)$ always holds.

## Inner automorphisms

We now consider the case where the set $E$ carries additional structure. For instance, suppose $E$ itself has a monoid structure and a given monoid $M$ acts on $E$; then the $M$-action is given by a monoid homomorphism $M \rightarrow\End(E)=\End_\Mon(E)$.

Let us consider in particular the case where a group $G$ acts on itself. If a homomorphism $\rho:G\rightarrow\End(G)=\End_\Grp(G)$ is given, then since a bijective group homomorphism is always a group isomorphism ([§Algebraic Structures, ⁋Definition 6](/en/math/algebraic_structures/algebraic_structures#def6)), we know that if $G$ acts on itself, this must necessarily be represented by a group homomorphism $G \rightarrow \Aut(G)$.

Among group actions on itself, the following example is especially worth remembering.

::: Proposition 9
For any element $g$ of a group $G$, define $\rho_g\in\Aut(G)$ by

$$\rho_g(x)=gxg^{-1}$$

Then the correspondence $\rho:g\mapsto \rho_g$ is a group homomorphism.
:::
::: Proof
For arbitrary $x,y\in G$,

$$\rho_g(xy)=g(xy)g^{-1}=(gxg^{-1})(gyg^{-1})=\rho_g(x)\rho_g(y)$$

holds, so we see that $\rho_g$ is a group homomorphism.

On the other hand, for arbitrary $g,h\in G$ and $x\in G$,

$$\rho_{gh}(x)=(gh)x(gh)^{-1}=g(hxh^{-1})g^{-1}=(\rho_g\circ\rho_h)(x)$$

so $\rho_{gh}=\rho_g\circ\rho_h$. In particular, substituting $h=g^{-1}$ gives $\rho_g\circ\rho_{g^{-1}}=\rho_e=\id_G$, so each $\rho_g$ is bijective, and therefore $\im\rho\subseteq\Aut(G)$ holds. That is, $\rho:g\mapsto \rho_g$ is a group homomorphism from $G$ to $\Aut(G)$.
:::

::: Definition 10
Let a group $G$ be given. We call the automorphism $\rho_g$ from [Proposition 9](#prop9) the *inner automorphism* defined by $g$, and denote the collection of these by $\Inn(G)$.
:::

::: Proposition 11
For a group $G$, the collection $\Inn(G)$ of inner automorphisms is a normal subgroup of $\Aut(G)$.
:::
::: Proof
Since $\Inn(G)$ is the image of the group homomorphism $\rho:G\rightarrow\Aut(G)$, it is obviously a subgroup of $\Aut(G)$; thus it suffices to show that $\Inn(G)$ is a *normal* subgroup.

Choose arbitrary $f\in\Aut(G)$, and fix $g\in G$ arbitrarily. We must show that $f\circ\rho_g\circ f^{-1}\in \Inn(G)$. For arbitrary $x\in G$,

$$(f\circ\rho_g\circ f^{-1})(x)=f(gf^{-1}(x)g^{-1})=f(g)xf(g^{-1})=\rho_{f(g)}(x)$$

so this is obvious.
:::

On the other hand, $\rho:G\rightarrow\Inn(G)$ is surjective, and therefore by [§Group Homomorphisms, ⁋Theorem 2](/en/math/algebraic_structures/isomorphism_theorems#thm2),

$$G/\ker\rho\cong\Inn(G)$$

holds. The kernel $\ker\rho$ also has a special name.

::: Definition 12
For a group $G$ and the group homomorphism $\rho:G\rightarrow\Inn(G)$ defined in [Proposition 9](#prop9), we call $\ker\rho$ the *center* of $G$ and denote it by $Z(G)$.
:::

By definition,

$$g\in\ker\rho\iff\rho_g=\id_G\iff gxg^{-1}=x\quad\text{for all $x\in G$}$$

so the fixer $\Fix(G)$ in the situation where $G$ acts on itself by inner automorphisms is exactly $Z(G)$. More generally, for an arbitrary subset $A\subseteq G$, we define the fixer $\Fix(A)$ of $A$ to be the *centralizer* $C_G(A)$ of $A$. Similarly, we define the *normalizer* $N_G(A)$ of $A$ to be $\Stab(A)$.

## Orbit-stabilizer theorem

We now return to group actions on a general set $E$. First, let us make the following definition.

::: Definition 13
Suppose an action of a group $G$ on a set $E$ is given. Then the *orbit* of an element $x\in E$ is the set

$$G\cdot x=\{g\cdot x\mid g\in G\}$$
:::

Then the relation on $E$ defined by

$$x\sim y\iff G\cdot x=G\cdot y\tag{$\ast$}$$

is an equivalence relation, so the quotient set $E/{\sim}$ is defined, and this is the set of orbits.

::: Theorem 14 (Orbit-stabilizer theorem)
Suppose an action of a group $G$ on a set $E$ is given. Then the identity

$$\lvert G\cdot x\rvert=[G:\Stab(x)]$$

holds.
:::
::: Proof
Define a function $p:G \rightarrow G\cdot x$ by $g\mapsto g\cdot x$; by the definition of $G\cdot x$, this function is surjective. On the other hand, $p(g_1)=p(g_2)\iff g_1^{-1}g_2\in \Stab(x)$, so the desired result follows from the canonical decomposition given after [\[Set Theory\] §Examples of Equivalence Relations, ⁋Proposition 7](/en/math/set_theory/examples_of_equivalence#prop7).
:::

Therefore, if $G$ is finite, then by [§Quotient Groups, ⁋Proposition 5](/en/math/algebraic_structures/quotient_groups#prop5) we obtain the identity

$$\lvert G\cdot x\rvert=\frac{\lvert G\rvert}{\lvert\Stab(x)\rvert}\tag{$\ast\ast$}$$

Likewise, suppose $G$ is finite and acts on a finite set $E$. Define $E^g$ to be the set of elements fixed by $g$,

$$E^g=\{x\in E\mid g\cdot x=x\}$$

then

$$\sum_{g\in G}\lvert E^g\rvert=\# \{(g, x)\in G\times E\mid g\cdot x=x\}=\sum_{x\in E}\lvert \Stab(x)\rvert$$

holds. Now from ($\ast\ast$),

$$\sum_{x\in E}\lvert \Stab(x)\rvert=\sum_{x\in E}\frac{\lvert G\rvert}{\lvert G\cdot x\rvert}$$

On the other hand, considering the quotient set $E/{\sim}$ defined from ($\ast$), the above sum can be rewritten as

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
