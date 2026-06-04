---
title: "Algebraic Structures"
description: "We define magmas, the algebraic structures obtained by adding a binary operation to a set, and explore the properties of associativity and commutativity."
excerpt: "Binary operations defined on sets"

categories: [Math / Algebraic Structures]
permalink: /en/math/algebraic_structures/algebraic_structures
sidebar: 
    nav: "algebraic_structures-en"

date: 2021-09-02
last_modified_at: 2022-11-29
weight: 1
translated_at: 2026-05-29T16:30:03+00:00
translation_source: kimi-cli
last_polished_at: 2026-05-29T16:30:03+00:00
---
In the [Algebraic Structures](/en/algebraic_structures) category, we define groups and rings and explore their basic properties. These are obtained by adding the structure of a binary operation to a set: a group is obtained by adding one operation, and a ring by adding two. If we additionally equip these with an action of a ring, we obtain modules and algebras. Galois theory and tensor algebra, among others, have been separated into their own categories, distinct from these algebraic structures.

## Binary Operations

In this post, we examine the *magma*, an algebraic structure equipped with a single binary operation. This structure carries too little information to be of much use going forward, but every time we define a new algebraic structure, we will find ourselves considering substructures and quotient structures as defined in this post.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> Given a set $$A$$, a function $$\star$$ from $$A\times A$$ to $$A$$ is called a *binary operation*. A set equipped with a binary operation is called a *magma*.

</div>

The value of the binary operation $$\star$$ at $$(x,y)$$ is abbreviated as $$x\ast y$$. Since a magma is a structure that includes not only the set $$A$$ but also the operation defined on it, we usually denote a magma as $$(A,\star)$$, including both the set and the operation, except when the context makes it clear.

<div class="example" markdown="1">

<ins id="ex2">**Example 2**</ins> For any set $$X$$, both $$(\mathcal{P}(X),\cup)$$ and $$(\mathcal{P}(X),\cap)$$ are magmas.

The operation $$x-y$$ defined on $$\mathbb{N}$$ is also a binary operation, so $$(\mathbb{N}, -)$$ is a magma as well.

</div>

For the two magmas $$(\mathcal{P}(X),\cup)$$ and $$\mathcal{P}(X),\cap)$$, the identities

$$A\cup(B\cup C)=(A\cup B)\cup C,\qquad A\cap(B\cap C)=(A\cap B)\cap C$$

hold for all $$A,B,C\in\mathcal{P}(X)$$. On the other hand, since

$$4-(1-2)=5\neq 1=(4-1)-2$$

this property does not hold in $$(\mathbb{N},-)$$.

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> For a magma $$(A,\star)$$, if the identity

$$x\star(y\star z)=(x\star y)\star z$$

holds for all $$x$$, $$y$$, $$z\in A$$, then we say that $$\star$$ is *associative*, and we call the magma $$A$$ an *associative magma*.

</div>

If $$\star$$ is associative, then computing the expression $$x\star y\star z$$ in either way yields

$$(x\star y)\star z=x\star(y\star z)$$

so $$x\star y\star z$$ has an unambiguous meaning. In terms of diagrams, this means the following diagram

![associativity](/assets/images/Math/Algebraic_Structures/Algebraic_Structures-1.png){:style="width:11em" class="invert" .align-center}

commutes. Meanwhile, the preceding operations have another point of difference.

<div class="definition" markdown="1">

<ins id="def4">**Definition 4**</ins> For a magma $$(A, \star)$$, if the identity

$$x\star y=y\star x$$

holds for all $$x,y\in A$$, then we say that $$\star$$ is *commutative*, and we call the magma $$A$$ a *commutative magma*.

</div>

Commutativity means that the following diagram

![commutativity](/assets/images/Math/Algebraic_Structures/Algebraic_Structures-2.png){:style="width:13em" class="invert" .align-center}

commutes. Here, $$\sigma$$ is the function defined by $$(x,y)\mapsto (y,x)$$.

In general, commutativity may hold without associativity, and conversely associativity may hold without commutativity.

<div class="example" markdown="1">

<ins id="ex5">**Example 5**</ins> Consider a family of magmas $$(A_i, \star_i)_{i\in I}$$. Then

$$\prod_{i\in I} (A_i\times A_i)\cong\left(\prod_{i\in I} A_i\right)\times\left(\prod_{i\in I}A_i\right)$$

so ([\[Set Theory\] §Properties of Products, ⁋Proposition 3](/en/math/set_theory/property_of_products#prop3)), the function

$$\prod_{i\in I}\star_i:\prod_{i\in I} (A_i\times A_i) \rightarrow \prod_{i\in I} A_i$$

can be viewed as a function from $$\left(\prod_{i\in I} A_i\right)\times\left(\prod_{i\in I}A_i\right)$$ to $$\left(\prod_{i\in I} A_i\right)\times\left(\prod_{i\in I}A_i\right)$$. ([\[Set Theory\] §Properties of Products, ⁋Definition 4](/en/math/set_theory/property_of_products#def4)) Thus $$\prod A_i$$ has a magma structure with respect to $$\star=\prod\star_i$$. The magma $$(\prod A_i, \star)$$ obtained in this way is called the *product magma*.

Taking the product of the above two diagrams over all $$i\in I$$, we can see that if all the $$\star_i$$ satisfy the commutative law, or all satisfy the associative law, then $$\star$$ does as well.

</div>

## Homomorphisms and Substructures

Let two magmas $$A$$ and $$A'$$ be given. As sets, there exists a function $$f:A\rightarrow A'$$ between them, but since these are not mere sets but algebraic structures equipped with a binary operation, it is natural to require that the function also preserve the binary operation.

<div class="definition" markdown="1">

<ins id="def6">**Definition 6**</ins> A function $$f:A\rightarrow A'$$ between two magmas $$(A,\star)$$ and $$(A',\star')$$ satisfying the identity

$$f(x\star y)=f(x)\star'f(y)$$

for all $$x$$, $$y\in A$$ is called a *homomorphism*, or a *magma homomorphism* when emphasis is needed. If there exists another homomorphism $$g:A'\rightarrow A$$ such that

$$g\circ f=\id_A,\qquad f\circ g=\id_{A'}$$

holds, then we say that $$f$$ and $$g$$ are *inverses* of each other, and call $$f$$ and $$g$$ *isomorphisms*. In this case, we say that $$A$$ and $$A'$$ are *isomorphic*, and denote this by $$A\cong A'$$.

</div>

It is not difficult to see that a bijective magma homomorphism is a magma isomorphism. Also, the following holds.

<div class="proposition" markdown="1">

<ins id="prop7">**Proposition 7**</ins> For magma homomorphisms $$f:A_1\rightarrow A_2$$ and $$g:A_2\rightarrow A_3$$, the composition $$g\circ f$$ is a magma homomorphism.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

For any $$x,y\in A_1$$,

$$(g\circ f)(x\star_1 y)=g(f(x\star_1y))=g(f(x)\star_2f(y))=g(f(x))\star_3g(f(y))=(g\circ f)(x)\star_3(g\circ f)(y)$$

holds.

</details>

Thus, there exists a cartesian monoidal category $$\Magma$$ whose objects are magmas and whose morphisms are magma homomorphisms.

In algebra, it is customary to write the image of $$f$$ as $$\im f$$ rather than $$f(A)$$. Choose arbitrary $$w,z\in\im f$$. Then there exist some $$x,y\in A$$ such that $$w=f(x)$$ and $$z=f(y)$$. Now

$$w\star'z=f(x)\star'f(y)=f(x\star y)$$

and since $$x\star y\in A$$, we have $$w\star'z\in\im f$$.

In this way, we define a subset of a magma that is closed under the operation as follows.

<div class="definition" markdown="1">

<ins id="def8">**Definition 8**</ins> For a magma $$(A,\star)$$, if some subset $$S$$ of $$A$$ is closed under $$\star$$, then we call $$S$$ a *submagma* of $$A$$.

</div>

Then for a magma $$(A,\star)$$ and a family of submagmas $$(S_i)_{i\in I}$$, it is obvious that the intersection $$S=\bigcap S_i$$ is also a submagma. For if we choose arbitrary $$a,b\in S$$, then since $$a,b\in S_i$$ for all $$i$$, we obtain $$a\star b\in S_i$$, and therefore $$a\star b\in S$$.

## Quotient Structures

Since equivalence relations exist on sets, we can also define equivalence relations on magmas. However, as with functions, not all equivalence relations are of interest to us.

Let a magma $$A$$ and an equivalence relation $$R$$ be given, and suppose that $$x\equiv x'\pmod{R}$$ and $$y\equiv y'\pmod{R}$$ hold. Since $$x$$ and $$x'$$, and $$y$$ and $$y'$$, are being treated as the same element by $$R$$, it is reasonable to expect the identity

$$x\star y\equiv x'\star y'\pmod{R}$$

to hold. But if no condition is imposed on $$R$$, there is no reason for this identity to hold. Therefore, we additionally define the following condition.

<div class="definition" markdown="1">

<ins id="def9">**Definition 9**</ins> Suppose an equivalence relation $$R$$ is defined on a magma $$(A,\star)$$. If for any $$a\in A$$,

$$x\equiv x'\implies a\star x\equiv a\star x'$$

holds, then we say that $$R$$ is *left compatible* with $$\star$$. Similarly, if

$$x\equiv x'\implies x\star a\equiv x'\star a$$

holds for all $$a$$, then we say that $$R$$ is *right compatible* with $$\star$$. An equivalence relation that is both left compatible and right compatible is simply said to be *compatible*.
</div>

Of course, in the above expressions, $$\equiv$$ always denotes the relation $$R$$.

If $$R$$ is an equivalence relation, we have already seen in set theory that the *quotient set* $$A/R$$ is well defined as a set. ([\[Set Theory\] §Equivalence Relations, ⁋Definition 4](/en/math/set_theory/equivalence_relations#def4)) The most natural attempt to define an operation $$\tiny\char"2606$$ on the set $$A/R$$ is

$$[x]\mathbin{\tiny\char"2606}[y]=[x\star y]$$

However, for this expression to be meaningful, the value of $$[x]\mathbin{\tiny\char"2606}[y]$$ must be well defined even if we choose a representative $$x'$$ of the equivalence class $$[x]$$ instead of $$x$$. That is, the identity

$$[x\star y]=[x]\mathbin{\tiny\char"2606}[y]=[x'\star y]$$

must hold. This identity can be rewritten as

$$x'\star y\equiv x\star y\mod R$$

and following the preceding definition, this is exactly the condition that $$R$$ be *right* compatible with the operation. By the same logic, since the value of the operation $$\mathbin{\tiny\char"2606}$$ must not change under the choice of representative for $$[y]$$, $$R$$ must also be *left* compatible with the operation.

Summarizing this, we obtain the following definition.

<div class="definition" markdown="1">

<ins id="def10">**Definition 10**</ins> Let a magma $$(A,\star)$$ be given with an equivalence relation $$R$$ compatible with $$\star$$. The magma $$(A/R,\mathbin{\tiny\char"2606})$$ obtained as above is called the *quotient magma*.

</div>

If $$\star$$ is associative or commutative, it is easy to verify that $$\mathbin{\tiny\char"2606}$$ is as well. In the above construction, we used different notations $$\star$$ and $$\mathbin{\tiny\char"2606}$$ for distinction, but since they are easily distinguished from context, it is customary to denote the operation in the quotient magma also by $$\star$$.

---

**References**

**[Bou]** Bourbaki, N. Algebra I. *Elements of Mathematics*. Springer. 1998.
