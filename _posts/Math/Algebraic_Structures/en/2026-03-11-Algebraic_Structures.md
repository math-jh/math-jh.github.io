---
title: "Algebraic Structures"
description: "We define magmas, the algebraic structures obtained by adding a binary operation to a set, and explore the properties of associativity and commutativity."
excerpt: "Binary operations defined on a set"

categories: [Math / Algebraic Structures]
permalink: /en/math/algebraic_structures/algebraic_structures
sidebar: 
    nav: "algebraic_structures-en"

date: 2021-09-02
weight: 1
translated_at: 2026-08-16T09:15:05+00:00
translation_source: kimi-cli
last_polished_at: 2026-08-16T09:15:05+00:00
---
In the [Algebraic Structures](/en/algebraic_structures) category, we define groups and rings and explore their basic properties. These are obtained by endowing a set with the structure of a binary operation: a group by adding one operation, and a ring by adding two. If we further equip these with an action of a ring, we obtain modules and algebras. Galois theory and tensor algebra, among others, have been placed in separate categories.

## Binary Operations

In this post, we examine the *magma*, an algebraic structure equipped with a single binary operation. This structure carries too little information to be of much use on its own, yet whenever we define a new algebraic structure, we will find ourselves returning to the notions of substructures, quotient structures, and the like introduced here.

::: Definition 1
For a nonempty set $A$, a function $\star$ from $A\times A$ to $A$ is called a *binary operation*. A set equipped with a binary operation is called a *magma*.
:::

The value of the binary operation $\star$ at $(x,y)$ is written $x\star y$. Since a magma is a structure comprising not only the set $A$ but also the operation defined on it, we usually denote a magma by $(A,\star)$, specifying both the set and the operation, except when the context makes this unnecessary.

::: Example 2
For any set $X$, both $(\mathcal{P}(X),\cup)$ and $(\mathcal{P}(X),\cap)$ are magmas.

The operation $x-y$ on $\mathbb{Z}$ is also a binary operation, so $(\mathbb{Z}, -)$ is a magma as well.
:::

For the two magmas $(\mathcal{P}(X),\cup)$ and $(\mathcal{P}(X),\cap)$, the identities

$$A\cup(B\cup C)=(A\cup B)\cup C,\qquad A\cap(B\cap C)=(A\cap B)\cap C$$

hold for all $A,B,C\in\mathcal{P}(X)$. On the other hand,

$$4-(1-2)=5\neq 1=(4-1)-2$$

so this property fails in $(\mathbb{N},-)$.

::: Definition 3
For a magma $(A,\star)$, if the identity

$$x\star(y\star z)=(x\star y)\star z$$

holds for all $x$, $y$, $z\in A$, then we say that $\star$ is *associative*, and we call the magma $A$ an *associative magma*.
:::

If $\star$ is associative, then the expression $x\star y\star z$ is unambiguous, since computing it in either of the two ways yields

$$(x\star y)\star z=x\star(y\star z).$$

In diagrammatic terms, this means that the following diagram

{% diagram Math/Algebraic_Structures/Algebraic_Structures-1.svg width="11.89em" alt="associativity" %}

commutes. Meanwhile, the operations above differ in another respect.

::: Definition 4
For a magma $(A, \star)$, if the identity

$$x\star y=y\star x$$

holds for all $x,y\in A$, then we say that $\star$ is *commutative*, and we call the magma $A$ a *commutative magma*.
:::

The commutativity law means that the following diagram

{% diagram Math/Algebraic_Structures/Algebraic_Structures-2.svg width="13.94em" alt="commutativity" %}

commutes. Here, $\sigma$ is the function defined by $(x,y)\mapsto (y,x)$.

In general, the commutativity law may fail even when the associativity law holds, and conversely, the associativity law may fail even when the commutativity law holds.

::: Example 5
Consider a family of magmas $(A_i, \star_i)_{i\in I}$. Then

$$\prod_{i\in I} (A_i\times A_i)\cong\left(\prod_{i\in I} A_i\right)\times\left(\prod_{i\in I}A_i\right)$$

so ([[Set Theory] §Properties of Products, ⁋Proposition 3](/en/math/set_theory/property_of_products#prop3)), the function

$$\prod_{i\in I}\star_i:\prod_{i\in I} (A_i\times A_i) \rightarrow \prod_{i\in I} A_i$$

can be regarded as a function from $\left(\prod_{i\in I} A_i\right)\times\left(\prod_{i\in I}A_i\right)$ to $\prod_{i\in I}A_i$. ([[Set Theory] §Properties of Products, ⁋Definition 4](/en/math/set_theory/property_of_products#def4)) Thus $\prod A_i$ carries a magma structure with respect to $\star=\prod\star_i$. The magma $(\prod A_i, \star)$ obtained in this way is called the *product magma*.

Taking the product of the two diagrams above over all $i\in I$, we see that if all the $\star_i$ are commutative, or all associative, then $\star$ is as well.
:::

## Homomorphisms and Substructures

Let two magmas $A$, $A'$ be given. As sets, there is a function $f:A\rightarrow A'$ between them, but since these are not mere sets (they are algebraic structures equipped with a binary operation), it is natural to require that the function preserve the binary operation as well.

::: Definition 6
A function $f:A\rightarrow A'$ between two magmas $(A,\star)$, $(A',\star')$ satisfying the identity

$$f(x\star y)=f(x)\star'f(y)$$

for all $x$, $y\in A$ is called a *homomorphism*, or a *magma homomorphism* when emphasis is needed. If there exists another homomorphism $g:A'\rightarrow A$ such that

$$g\circ f=\id_A,\qquad f\circ g=\id_{A'}$$

then we say that $f$ and $g$ are *inverses* of each other, and we call $f$ and $g$ *isomorphisms*. In this case, we say that $A$ and $A'$ are *isomorphic*, and write $A\cong A'$.
:::

It is not difficult to see that a bijective magma homomorphism is a magma isomorphism. Moreover, the following holds.

::: Proposition 7
For magma homomorphisms $f:A_1\rightarrow A_2$, $g:A_2\rightarrow A_3$, the composition $g\circ f$ is a magma homomorphism.
:::
::: Proof
For any $x,y\in A_1$,

$$(g\circ f)(x\star_1 y)=g(f(x\star_1y))=g(f(x)\star_2f(y))=g(f(x))\star_3g(f(y))=(g\circ f)(x)\star_3(g\circ f)(y)$$

holds.
:::

Thus there exists a cartesian monoidal category $\Magma$ whose objects are magmas and whose morphisms are magma homomorphisms. ([[Category Theory] §Monoidal Categories, ⁋Definition 3](/en/math/category_theory/monoidal_categories#def3))

In algebra, the image of $f$ is usually written $\im f$ rather than $f(A)$. Pick arbitrary $w,z\in\im f$. Then there exist $x,y\in A$ such that $w=f(x)$ and $z=f(y)$. Now

$$w\star'z=f(x)\star'f(y)=f(x\star y)$$

and since $x\star y\in A$, we have $w\star'z\in\im f$.

We define a subset of a magma that is closed under the operation as follows.

::: Definition 8
For a magma $(A,\star)$, if a subset $S$ of $A$ is closed under $\star$, then we call $S$ a *submagma* of $A$.
:::

Then for a magma $(A,\star)$ and a family of submagmas $(S_i)_{i\in I}$, it is immediate that the intersection $S=\bigcap S_i$ is also a submagma: given arbitrary $a,b\in S$, we have $a,b\in S_i$ for all $i$, hence $a\star b\in S_i$, and therefore $a\star b\in S$.

## Quotient Structures

Since equivalence relations exist on sets, we can define equivalence relations on magmas as well. However, as with functions, not all equivalence relations are of interest to us.

Let $A$ be a magma and $R$ an equivalence relation. Suppose $x\equiv x'\pmod{R}$ and $y\equiv y'\pmod{R}$. Since $x$ and $x'$, and likewise $y$ and $y'$, are regarded as the same element under $R$, it is reasonable to expect the identity

$$x\star y\equiv x'\star y'\pmod{R}$$

to hold. But if no condition is imposed on $R$, there is no reason for this identity to hold. Thus we define the following additional condition.

::: Definition 9
Suppose an equivalence relation $R$ is defined on a magma $(A,\star)$. If for all $a\in A$,

$$x\equiv x'\implies a\star x\equiv a\star x'$$

holds, then we say that $R$ is *left compatible* with $\star$. Similarly, if

$$x\equiv x'\implies x\star a\equiv x'\star a$$

holds for all $a$, then we say that $R$ is *right compatible* with $\star$. An equivalence relation that is both left compatible and right compatible is simply called *compatible*.
:::

Of course, in the above identities, $\equiv$ always denotes the relation $R$.

If $R$ is an equivalence relation, then as a set the *quotient set* $A/R$ is well defined, as we have already seen in set theory. ([[Set Theory] §Equivalence Relations, ⁋Definition 4](/en/math/set_theory/equivalence_relations#def4)) The most natural attempt to define an operation $\tiny\char"2606$ on the set $A/R$ is

$$[x]\mathbin{\tiny\char"2606}[y]=[x\star y].$$

However, for this expression to be meaningful, the value of $[x]\mathbin{\tiny\char"2606}[y]$ must be well defined even if we choose a representative $x'$ of the equivalence class $[x]$ instead of $x$. That is, the identity

$$[x\star y]=[x]\mathbin{\tiny\char"2606}[y]=[x'\star y]$$

must hold. This identity can be rewritten as

$$x'\star y\equiv x\star y\pmod R$$

and according to the preceding definition, this is precisely the condition that $R$ be *right* compatible with the operation. By the same logic, since the value of the operation $\mathbin{\tiny\char"2606}$ must not change under the choice of representative for $[y]$, $R$ must also be *left* compatible with the operation.

Summarizing this, we obtain the following definition.

::: Definition 10
Let $R$ be an equivalence relation on a magma $(A,\star)$ compatible with $\star$. The magma $(A/R,\mathbin{\tiny\char"2606})$ obtained as above is called a *quotient magma*.
:::

It is easy to check that if $\star$ satisfies the associativity or commutativity law, then $\mathbin{\tiny\char"2606}$ does as well. In the above construction, we used distinct notations $\star$ and $\mathbin{\tiny\char"2606}$ for clarity, but since they are easily distinguished from context, it is customary to denote the operation in a quotient magma also by $\star$.

---

**References**

**[Bou]** Bourbaki, N. Algebra I. *Elements of Mathematics*. Springer. 1998.  

---
