---
title: "Algebraic Structures"
excerpt: "Binary operations defined on sets"

categories: [Math / Algebraic Structures]
permalink: /en/math/algebraic_structures/algebraic_structures
header:
    overlay_image: /assets/images/Math/Algebraic_Structures/Algebraic_Structures.png
    overlay_filter: 0.5
sidebar:
    nav: "algebraic_structures-en"

date: 2026-03-11
last_modified_at: 2026-03-11
weight: 1
translated_at: 2026-05-24T07:00:03+00:00
translation_source: kimi-cli
last_polished_at: 2026-05-24T07:00:03+00:00
---
In the [Algebraic Structures](/en/algebraic_structures) category, we define groups and rings and investigate their fundamental properties. These structures are obtained by endowing sets with binary operations: a group is obtained by adding one operation, and a ring by adding two. If we further consider actions of rings, we obtain modules and algebras. Outside these algebraic structures, we have separated Galois theory and tensor algebra into separate categories.

## Binary Operations

In this post, we examine *magmas*, algebraic structures equipped with a single binary operation. This structure carries too little information to be of use going forward; however, whenever we define new algebraic structures, we will find ourselves considering the substructures and quotient structures introduced here.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> For a set $$A$$, a function $$\star$$ from $$A\times A$$ to $$A$$ is called a *binary operation*. A set equipped with a binary operation is called a *magma*.

</div>

The value $$\star(x,y)$$ of a binary operation $$\star$$ is abbreviated as $$x\ast y$$. A magma is a structure comprising not only the set $$A$$ but also the operation defined on it, so we denote a magma by $$(A,\star)$$, explicitly indicating both the set and the operation, except when the context makes this clear.

<div class="example" markdown="1">

<ins id="ex2">**Example 2**</ins> For any set $$X$$, both $$(\mathcal{P}(X),\cup)$$ and $$(\mathcal{P}(X),\cap)$$ are magmas.

The operation $$x-y$$ on $$\mathbb{N}$$ is also a binary operation, so $$(\mathbb{N}, -)$$ is a magma as well.

</div>

In both magmas $$(\mathcal{P}(X),\cup)$$ and $$(\mathcal{P}(X),\cap)$$, the equations

$$A\cup(B\cup C)=(A\cup B)\cup C,\qquad A\cap(B\cap C)=(A\cap B)\cap C$$

hold for all $$A,B,C\in\mathcal{P}(X)$$. On the other hand,

$$4-(1-2)=5\neq 1=(4-1)-2$$

so this property fails in $$(\mathbb{N},-)$$.

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> For a magma $$(A,\star)$$, if

$$x\star(y\star z)=(x\star y)\star z$$

holds for all $$x$$, $$y$$, $$z\in A$$, we say that $$\star$$ is *associative*, and we call the magma $$A$$ an *associative magma*.

</div>

If $$\star$$ is associative, then computing $$x\star y\star z$$ in either of the two possible ways yields

$$(x\star y)\star z=x\star(y\star z)$$

so $$x\star y\star z$$ has an unambiguous meaning. Diagrammatically, this means that the following diagram

![associativity](/assets/images/Math/Algebraic_Structures/Algebraic_Structures-1.png){:style="width:11em" class="invert" .align-center}

commutes. The operations above also differ in another respect.

<div class="definition" markdown="1">

<ins id="def4">**Definition 4**</ins> For a magma $$(A, \star)$$, if

$$x\star y=y\star x$$

holds for all $$x,y\in A$$, we say that $$\star$$ is *commutative*, and we call the magma $$A$$ a *commutative magma*.

</div>

Commutativity means that the following diagram

![commutativity](/assets/images/Math/Algebraic_Structures/Algebraic_Structures-2.png){:style="width:13em" class="invert" .align-center}

commutes. Here, $$\sigma$$ is the function defined by $$(x,y)\mapsto (y,x)$$.

In general, commutativity does not imply associativity, nor does associativity imply commutativity.

<div class="example" markdown="1">

<ins id="ex5">**Example 5**</ins> Consider a family of magmas $$(A_i, \star_i)_{i\in I}$$. Since

$$\prod_{i\in I} (A_i\times A_i)\cong\left(\prod_{i\in I} A_i\right)\times\left(\prod_{i\in I}A_i\right)$$

([\[Set Theory\] §Properties of Products, ⁋Proposition 3](/en/math/set_theory/property_of_products#prop3)), we may regard the function

$$\prod_{i\in I}\star_i:\prod_{i\in I} (A_i\times A_i) \rightarrow \prod_{i\in I} A_i$$

as a function from $$\left(\prod_{i\in I} A_i\right)\times\left(\prod_{i\in I}A_i\right)$$ to $$\left(\prod_{i\in I} A_i\right)\times\left(\prod_{i\in I}A_i\right)$$. ([\[Set Theory\] §Properties of Products, ⁋Definition 4](/en/math/set_theory/property_of_products#def4)) Thus $$\prod A_i$$ carries a magma structure with respect to $$\star=\prod\star_i$$. The magma $$(\prod A_i, \star)$$ obtained in this way is called the *product magma*.

Taking the product of the two diagrams above over all $$i\in I$$, we see that if all $$\star_i$$ are commutative, or if all are associative, then $$\star$$ inherits the same property.

</div>

## Homomorphisms and Substructures

Let $$A$$ and $$A'$$ be two magmas. As sets, there are functions $$f:A\rightarrow A'$$ between them, but since they are not merely sets but algebraic structures equipped with binary operations, it is natural to require that functions preserve these operations.

<div class="definition" markdown="1">

<ins id="def6">**Definition 6**</ins> A function $$f:A\rightarrow A'$$ between two magmas $$(A,\star)$$ and $$(A',\star')$$ is called a *homomorphism* if it satisfies

$$f(x\star y)=f(x)\star'f(y)$$

for all $$x$$, $$y\in A$$. When emphasis is needed, we call it a *magma homomorphism*. If there exists another homomorphism $$g:A'\rightarrow A$$ such that

$$g\circ f=\id_A,\qquad f\circ g=\id_{A'}$$

then we call $$f$$ and $$g$$ *inverses* of each other, and we call $$f$$ and $$g$$ *isomorphisms*. In this case, $$A$$ and $$A'$$ are said to be *isomorphic*, denoted $$A\cong A'$$.

</div>

It is not difficult to see that a bijective magma homomorphism is a magma isomorphism. Moreover, the following holds.

<div class="proposition" markdown="1">

<ins id="prop7">**Proposition 7**</ins> Given magma homomorphisms $$f:A_1\rightarrow A_2$$ and $$g:A_2\rightarrow A_3$$, the composition $$g\circ f$$ is a magma homomorphism.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

For any $$x,y\in A_1$$,

$$(g\circ f)(x\star_1 y)=g(f(x\star_1y))=g(f(x)\star_2f(y))=g(f(x))\star_3g(f(y))=(g\circ f)(x)\star_3(g\circ f)(y)$$

holds.

</details>

Therefore, there exists a cartesian monoidal category $$\Magma$$ whose objects are magmas and whose morphisms are magma homomorphisms.

In algebra, it is customary to write the image of $$f$$ as $$\im f$$ rather than $$f(A)$$. Take arbitrary $$w,z\in\im f$$. Then there exist $$x,y\in A$$ such that $$w=f(x)$$ and $$z=f(y)$$. Now

$$w\star'z=f(x)\star'f(y)=f(x\star y)$$

and since $$x\star y\in A$$, we have $$w\star'z\in\im f$$.

We define a subset of a magma closed under the operation in this manner as follows.

<div class="definition" markdown="1">

<ins id="def8">**Definition 8**</ins> For a magma $$(A,\star)$$, if a subset $$S$$ of $$A$$ is closed under $$\star$$, then we call $$S$$ a *submagma* of $$A$$.

</div>

Then, for a magma $$(A,\star)$$ and a family of submagmas $$(S_i)_{i\in I}$$, it is clear that the intersection $$S=\bigcap S_i$$ is also a submagma. Indeed, for any $$a,b\in S$$, we have $$a,b\in S_i$$ for all $$i$$, so $$a\star b\in S_i$$ for all $$i$$, and hence $$a\star b\in S$$.

## Quotient Structures

Just as sets admit equivalence relations, so do magmas. However, not every equivalence relation is of interest to us.

Consider a magma $$A$$ with an equivalence relation $$R$$. Suppose $$x\equiv x'\pmod{R}$$ and $$y\equiv y'\pmod{R}$$. Since $$R$$ identifies $$x$$ with $$x'$$ and $$y$$ with $$y'$$, it is reasonable to expect that

$$x\star y\equiv x'\star y'\pmod{R}$$

holds. Yet without additional conditions on $$R$$, there is no reason for this to be true. Therefore, we impose the following additional condition.

<div class="definition" markdown="1">

<ins id="def9">**Definition 9**</ins> Let $$R$$ be an equivalence relation on a magma $$(A,\star)$$. If for any $$a\in A$$,

$$x\equiv x'\implies a\star x\equiv a\star x'$$

holds, we say that $$R$$ is *left compatible* with $$\star$$. Similarly, if

$$x\equiv x'\implies x\star a\equiv x'\star a$$

holds for all $$a$$, we say that $$R$$ is *right compatible* with $$\star$$. An equivalence relation that is both left and right compatible is simply called *compatible*.
</div>

Of course, in the above equations, $$\equiv$$ always denotes the relation $$R$$.

If $$R$$ is an equivalence relation, we have already seen in set theory that the *quotient set* $$A/R$$ is well-defined. ([\[Set Theory\] §Equivalence Relations, ⁋Definition 4](/en/math/set_theory/equivalence_relations#def4)) The most natural attempt to define an operation $$\tiny\char"2606$$ on $$A/R$$ is

$$[x]\mathbin{\tiny\char"2606}[y]=[x\star y]$$

However, for this expression to be well-defined, the value of $$[x]\mathbin{\tiny\char"2606}[y]$$ must not depend on the choice of representative for $$[x]$$. That is,

$$[x\star y]=[x]\mathbin{\tiny\char"2606}[y]=[x'\star y]$$

must hold whenever $$x\equiv x'$$. This can be rewritten as

$$x'\star y\equiv x\star y\mod R$$

which, by the previous definition, means precisely that $$R$$ must be *right* compatible with the operation. Similarly, since the value of the operation $$\mathbin{\tiny\char"2606}$$ must not change when we choose a different representative for $$[y]$$, $$R$$ must also be *left* compatible with the operation.

Summarizing this, we obtain the following definition.

<div class="definition" markdown="1">

<ins id="def10">**Definition 10**</ins> Let $$R$$ be an equivalence relation on a magma $$(A,\star)$$ that is compatible with $$\star$$. The magma $$(A/R,\mathbin{\tiny\char"2606})$$ obtained above is called the *quotient magma*.

</div>

It is easy to verify that if $$\star$$ is associative or commutative, then $$\mathbin{\tiny\char"2606}$$ inherits the same property. In the above construction, we distinguished between $$\star$$ and $$\mathbin{\tiny\char"2606}$$ by using different notations, but since they are easily distinguished from context, it is customary to denote the operation in the quotient magma also by $$\star$$.

---

**References**

**[Bou]** Bourbaki, N. Algebra I. *Elements of Mathematics*. Springer. 1998.

---
