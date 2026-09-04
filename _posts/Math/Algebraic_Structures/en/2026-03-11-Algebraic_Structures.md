---
title: "Algebraic Structures"
description: "We define a magma, an algebraic structure obtained by adding a binary operation to a set, and explore the properties of associativity and commutativity."
excerpt: "Binary operations defined on a set"

categories: [Math / Algebraic Structures]
permalink: /en/math/algebraic_structures/algebraic_structures
sidebar: 
    nav: "algebraic_structures-en"

date: 2021-09-02
weight: 1
translated_at: 2026-08-16T09:15:05+00:00
translation_source: kimi-cli
last_polished_at: 2026-09-04T09:45:04+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
In the [Algebraic Structures](/en/algebraic_structures) category, we define groups and rings and explore their basic properties. These are obtained by adding the structure of a binary operation onto a set: a group by adding one operation, and a ring by adding two. If we additionally give them an action of a ring, we obtain modules and algebras. Besides these algebraic structures, Galois theory and tensor algebra, among others, have been separated into distinct categories.

## Binary Operations

In this post, we examine the *magma*, an algebraic structure equipped with a single binary operation. This structure carries so little information that we will not use it going forward, but whenever we define a new algebraic structure hereafter, we will consider notions such as substructures and quotient structures to be defined in this post.

::: Definition 1
For a nonempty set $A$, a function from $A\times A$ to $A$, $\star$, is called a *binary operation*. A set equipped with a binary operation is called a *magma*.
:::

For a binary operation $\star$, the function value $\star(x,y)$ is abbreviated as $x\star y$. Since a magma is a structure comprising not only the set $A$ but also the operation defined on it, except when clear from context, we specify both the operation and the set as $(A,\star)$ when denoting a magma.

::: Example 2
For any set $X$, both $(\mathcal{P}(X),\cup)$ and $(\mathcal{P}(X),\cap)$ are magmas.

On $\mathbb{Z}$, the operation $x-y$ is also a binary operation, so $(\mathbb{Z}, -)$ is also a magma.
:::

In the two magmas $(\mathcal{P}(X),\cup)$ and $(\mathcal{P}(X),\cap)$, the equations

$$A\cup(B\cup C)=(A\cup B)\cup C,\qquad A\cap(B\cap C)=(A\cap B)\cap C$$

hold for all $A,B,C\in\mathcal{P}(X)$. On the other hand, since

$$4-(1-2)=5\neq 1=(4-1)-2$$

this property does not hold in $(\mathbb{N},-)$.

::: Definition 3
For a magma $(A,\star)$, if for any $x$, $y$, $z\in A$ the equation

$$x\star(y\star z)=(x\star y)\star z$$

always holds, then $\star$ is said to be *associative*, and the magma $A$ is called an *associative magma*.
:::

If $\star$ is associative, even if the expression $x\star y\star z$ is computed in two ways, since

$$(x\star y)\star z=x\star(y\star z)$$

without ambiguity $x\star y\star z$ has a well-defined meaning. Expressed as a diagram, this means that the following diagram

{% diagram Math/Algebraic_Structures/Algebraic_Structures-1.svg width="11.89em" alt="associativity" %}

commutes. Meanwhile, the preceding operations have another difference.

::: Definition 4
For a magma $(A, \star)$, if for any $x,y\in A$ the equation

$$x\star y=y\star x$$

always holds, then $\star$ is said to be *commutative*, and the magma $A$ is called a *commutative magma*.
:::

Commutativity means that the following diagram

{% diagram Math/Algebraic_Structures/Algebraic_Structures-2.svg width="13.94em" alt="commutativity" %}

commutes. Here, $\sigma$ is the function defined by $(x,y)\mapsto (y,x)$.

In general, even if commutativity holds, associativity may fail to hold, and conversely, even if associativity holds, commutativity may fail to hold.

::: Example 5
Consider a family of magmas $(A_i, \star_i)_{i\in I}$. Then, since

$$\prod_{i\in I} (A_i\times A_i)\cong\left(\prod_{i\in I} A_i\right)\times\left(\prod_{i\in I}A_i\right)$$

([\[Set Theory\] §Properties of Products, ⁋Proposition 3](/en/math/set_theory/property_of_products#prop3)), the function

$$\prod_{i\in I}\star_i:\prod_{i\in I} (A_i\times A_i) \rightarrow \prod_{i\in I} A_i$$

can be regarded as a function from $\left(\prod_{i\in I} A_i\right)\times\left(\prod_{i\in I}A_i\right)$ to $\prod_{i\in I}A_i$. ([\[Set Theory\] §Properties of Products, ⁋Definition 4](/en/math/set_theory/property_of_products#def4)) Therefore, $\prod A_i$ has a magma structure with respect to $\star=\prod\star_i$. The magma $(\prod A_i, \star)$ obtained in this way is called the *product magma*.

Taking the product of the above two diagrams over all $i\in I$, we see that if the $\star_i$ are all commutative, or all associative, then $\star$ is as well.
:::

## Homomorphisms and Substructures

Let two magmas $A$, $A'$ be given. As sets, there exists a function $f:A\rightarrow A'$ between them, but since these are not merely sets but algebraic structures with an added binary operation, it is natural that the function also preserve the binary operation.

::: Definition 6
For two magmas $(A,\star)$ and $(A',\star')$, if a function $f:A\rightarrow A'$ satisfies the equation

$$f(x\star y)=f(x)\star'f(y)$$

for all $x$, $y\in A$, then this function $f$ is called a *homomorphism*, or a *magma homomorphism* when emphasis is needed. If there exists another homomorphism $g:A'\rightarrow A$ such that

$$g\circ f=\id_A,\qquad f\circ g=\id_{A'}$$

holds, then $f$ and $g$ are called each other's *inverse*, and $f$ and $g$ are called *isomorphisms*. In this case, $A$ and $A'$ are called *isomorphic*, and denoted by $A\cong A'$.
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

Therefore, there exists a cartesian monoidal category $\Magma$ whose objects are magmas and whose morphisms are magma homomorphisms. ([\[Category Theory\] §Monoidal Categories, ⁋Definition 3](/en/math/category_theory/monoidal_categories#def3))

In algebra, it is customary to write the image of $f$, instead of $f(A)$, as $\im f$. Let us take arbitrary $w,z\in\im f$. Then there exist some $x,y\in A$ such that $w=f(x)$ and $z=f(y)$. Now

$$w\star'z=f(x)\star'f(y)=f(x\star y)$$

and since $x\star y\in A$, we have $w\star'z\in\im f$.

A subset of a magma that is closed under the operation in this way is defined as follows.

::: Definition 8
For a magma $(A,\star)$, if a subset of $A$, $S$, is closed under $\star$, then $S$ is called a *submagma* of $A$.
:::

Then, for a magma $(A,\star)$ and a family of submagmas $(S_i)_{i\in I}$, it is trivial that the intersection $S=\bigcap S_i$ is also a submagma. This is because if we choose arbitrary $a,b\in S$, then from the fact that for all $i$ we have $a,b\in S_i$, we obtain $a\star b\in S_i$, and therefore $a\star b\in S$.

## Quotient Structures

Since equivalence relations exist on sets, we can define equivalence relations on magmas as well. However, as with functions, not all equivalence relations are objects of our interest.

For a magma $A$ and an equivalence relation $R$, suppose that $x\equiv x'\pmod{R}$ and $y\equiv y'\pmod{R}$ hold. Since $x$ and $x'$, and $y$ and $y'$ are treated as the same elements by $R$, it is reasonable to expect the following equation

$$x\star y\equiv x'\star y'\pmod{R}$$

to hold. But if no condition is imposed on $R$, there is no reason for this equation to hold. Therefore, we define the following additional condition.

::: Definition 9
Suppose an equivalence relation $R$ is defined on a magma $(A,\star)$. If for any $a\in A$,

$$x\equiv x'\implies a\star x\equiv a\star x'$$

holds, then $R$ is said to be *left compatible* with $\star$. Similarly, if

$$x\equiv x'\implies x\star a\equiv x'\star a$$

holds for all $a$, then $R$ is said to be *right compatible* with $\star$. An equivalence relation that is both left compatible and right compatible is simply called *compatible*.
:::

Of course, in the above equations, $\equiv$ always means with respect to the relation $R$.

If $R$ is an equivalence relation, we have already seen in set theory that as a set the *quotient set* $A/R$ is well-defined. ([\[Set Theory\] §Equivalence Relations, ⁋Definition 4](/en/math/set_theory/equivalence_relations#def4)) On the set $A/R$, the most natural attempt to define an operation $\tiny\char"2606$ is

$$[x]\mathbin{\tiny\char"2606}[y]=[x\star y].$$

However, for this expression to have meaning, even if we choose for the equivalence class $[x]$, instead of $x$, the representative $x'$, the value of $[x]\mathbin{\tiny\char"2606}[y]$ must be well-defined. That is, the following equation

$$[x\star y]=[x]\mathbin{\tiny\char"2606}[y]=[x'\star y]$$

must hold. This equation can be rewritten as

$$x'\star y\equiv x\star y\pmod R$$

and according to the preceding definition, this means precisely that $R$ must be *right* compatible with the operation. By the same logic, since even under the choice of representative of $[y]$ the value of the operation $\mathbin{\tiny\char"2606}$ must not change, $R$ must be *left* compatible with the operation.

Summarizing this, we obtain the following definition.

::: Definition 10
Suppose that on a magma $(A,\star)$, an equivalence relation compatible with $\star$, $R$, is given. The magma $(A/R,\mathbin{\tiny\char"2606})$ obtained as above is called a *quotient magma*.
:::

It is easy to check that if $\star$ satisfies associativity or commutativity, then $\mathbin{\tiny\char"2606}$ does as well. In the above construction, we denoted $\star$ and $\mathbin{\tiny\char"2606}$ differently for distinction, but since they are easily distinguished from context, it is customary to denote the operation in the quotient magma also as $\star$.

---

**References**

**[Bou]** Bourbaki, N. Algebra I. *Elements of Mathematics*. Springer. 1998.  

---
