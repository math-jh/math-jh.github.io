---

title: "Algebraic Structures"
excerpt: "Binary operations defined on sets"

categories: [Math / Algebraic Structures]
permalink: /en/math/algebraic_structures/algebraic_structures
header:
    overlay_image: /assets/images/Math/Algebraic_Structures/Algebraic_structures.png
    overlay_filter: 0.5
sidebar:
    nav: "algebraic_structures-en"

date: 2026-03-11
last_modified_at: 2026-03-11
weight: 1

---

In the [Algebraic Structures](/en/algebraic_structures) category, we define groups and rings and explore their fundamental properties. These structures are obtained by adding binary operation structures to sets: groups arise from adding a single operation, while rings arise from adding two operations. By additionally equipping rings with actions, we obtain modules and algebras. Topics such as Galois theory and tensor algebra are treated in separate categories.

## Binary Operations

In this post, we examine *magmas*, which are algebraic structures equipped with a single binary operation. Although this structure contains too little information to be of much use in practice, whenever we define new algebraic structures in what follows, we will consider notions such as substructures and quotient structures that we introduce here.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> For a set $$A$$, a function $$\star$$ from $$A\times A$$ to $$A$$ is called a *binary operation*. A set equipped with a binary operation is called a *magma*.

</div>

The value $$\star(x,y)$$ of a binary operation $$\star$$ is abbreviated as $$x\ast y$$. Since a magma is a structure that includes not only the set $$A$$ but also the operation defined on it, we denote a magma as $$(A,\star)$$, explicitly indicating both the operation and the set, except when the context makes it clear.

<div class="example" markdown="1">

<ins id="ex2">**Example 2**</ins> For any set $$X$$, both $$(\mathcal{P}(X),\cup)$$ and $$(\mathcal{P}(X),\cap)$$ are magmas.

The operation $$x-y$$ defined on $$\mathbb{N}$$ is also a binary operation, so $$(\mathbb{N}, -)$$ is a magma as well.

</div>

In both magmas $$(\mathcal{P}(X),\cup)$$ and $$(\mathcal{P}(X),\cap)$$, the following equations

$$A\cup(B\cup C)=(A\cup B)\cup C,\qquad A\cap(B\cap C)=(A\cap B)\cap C$$

hold for all $$A,B,C\in\mathcal{P}(X)$$. On the other hand, since

$$4-(1-2)=5\neq 1=(4-1)-2$$

this property does not hold in $$(\mathbb{N},-)$$.

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> For a magma $$(A,\star)$$, if the equation

$$x\star(y\star z)=(x\star y)\star z$$

always holds for any $$x$$, $$y$$, $$z\in A$$, we say that $$\star$$ is *associative*, and the magma $$A$$ is called an *associative magma*.

</div>

If $$\star$$ is associative, then even when we compute the expression $$x\star y\star z$$ in two different ways, we obtain

$$(x\star y)\star z=x\star(y\star z)$$

so $$x\star y\star z$$ has an unambiguous meaning. In terms of diagrams, this means that the following diagram

![associativity](/assets/images/Math/Algebraic_Structures/Algebraic_structures-1.png){:style="width:11em" class="invert" .align-center}

commutes. Meanwhile, the previous operations exhibit another difference.

<div class="definition" markdown="1">

<ins id="def4">**Definition 4**</ins> For a magma $$(A, \star)$$, if the equation

$$x\star y=y\star x$$

always holds for any $$x,y\in A$$, we say that $$\star$$ is *commutative*, and the magma $$A$$ is called a *commutative magma*.

</div>

Commutativity means that the following diagram

![commutativity](/assets/images/Math/Algebraic_Structures/Algebraic_structures-2.png){:style="width:13em" class="invert" .align-center}

commutes. Here, $$\sigma$$ is the function defined by $$(x,y)\mapsto (y,x)$$.

In general, commutativity does not imply associativity, and conversely, associativity does not imply commutativity.

<div class="example" markdown="1">

<ins id="ex5">**Example 5**</ins> Consider a family of magmas $$(A_i, \star_i)_{i\in I}$$. Since

$$\prod_{i\in I} (A_i\times A_i)\cong\left(\prod_{i\in I} A_i\right)\times\left(\prod_{i\in I}A_i\right)$$

([[\[Set Theory\] §Properties of Product Sets, ⁋Proposition 3](/en/math/set_theory/property_of_products#prop3)), we can regard the function

$$\prod_{i\in I}\star_i:\prod_{i\in I} (A_i\times A_i) \rightarrow \prod_{i\in I} A_i$$

as a function from $$\left(\prod_{i\in I} A_i\right)\times\left(\prod_{i\in I}A_i\right)$$ to $$\left(\prod_{i\in I} A_i\right)\times\left(\prod_{i\in I}A_i\right)$$. ([[\[Set Theory\] §Properties of Product Sets, ⁋Definition 4](/en/math/set_theory/property_of_products#def4)) Thus $$\prod A_i$$ has a magma structure with respect to $$\star=\prod\star_i$$. The magma $$(\prod A_i, \star)$$ obtained in this way is called the *product magma*.

By taking the product of the two diagrams above for all $$i\in I$$, we see that if all $$\star_i$$ are commutative or all are associative, then $$\star$$ inherits the same property.

</div>

## Homomorphisms and Substructures

Let two magmas $$A$$ and $$A'$$ be given. As sets, there exist functions $$f:A\rightarrow A'$$ between them, but since these are not merely sets but algebraic structures with binary operations, it is natural for functions to preserve the binary operations.

<div class="definition" markdown="1">

<ins id="def6">**Definition 6**</ins> A function $$f:A\rightarrow A'$$ between two magmas $$(A,\star)$$ and $$(A',\star')$$ is called a *homomorphism* if it satisfies the equation

$$f(x\star y)=f(x)\star'f(y)$$

for all $$x$$, $$y\in A$$. When emphasis is needed, we call it a *magma homomorphism*. If there exists another homomorphism $$g:A'\rightarrow A$$ such that

$$g\circ f=\id_A,\qquad f\circ g=\id_{A'}$$

holds, then $$f$$ and $$g$$ are called *inverses* of each other, and $$f$$ and $$g$$ are called *isomorphisms*. In this case, $$A$$ and $$A'$$ are said to be *isomorphic*, denoted by $$A\cong A'$$.

</div>

It is not difficult to see that a bijective magma homomorphism is a magma isomorphism. Moreover, the following holds.

<div class="proposition" markdown="1">

<ins id="prop7">**Proposition 7**</ins> For magma homomorphisms $$f:A_1\rightarrow A_2$$ and $$g:A_2\rightarrow A_3$$, the composition $$g\circ f$$ is a magma homomorphism.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

For any $$x,y\in A_1$$,

$$(g\circ f)(x\star_1 y)=g(f(x\star_1y))=g(f(x)\star_2f(y))=g(f(x))\star_3g(f(y))=(g\circ f)(x)\star_3(g\circ f)(y)$$

holds.

</details>

Therefore, there exists a cartesian monoidal category $$\Magma$$ whose objects are magmas and whose morphisms are magma homomorphisms.

In algebra, it is customary to write the image of $$f$$ as $$\im f$$ rather than $$f(A)$$. Let us choose arbitrary $$w,z\in\im f$$. Then there exist $$x,y\in A$$ such that $$w=f(x)$$ and $$z=f(y)$$. Now

$$w\star'z=f(x)\star'f(y)=f(x\star y)$$

and since $$x\star y\in A$$, we have $$w\star'z\in\im f$$.

A subset of a magma that is closed under the operation in this manner is defined as follows.

<div class="definition" markdown="1">

<ins id="def8">**Definition 8**</ins> For a magma $$(A,\star)$$, if some subset $$S$$ of $$A$$ is closed under $$\star$$, then $$S$$ is called a *submagma* of $$A$$.

</div>

Thus, for a magma $$(A,\star)$$ and a family of submagmas $$(S_i)_{i\in I}$$, it is clear that the intersection $$S=\bigcap S_i$$ is also a submagma. If we choose arbitrary $$a,b\in S$$, then from the fact that $$a,b\in S_i$$ for all $$i$$, we obtain $$a\star b\in S_i$$, and therefore $$a\star b\in S$$.

## Quotient Structures

Since equivalence relations exist on sets, we can also define equivalence relations on magmas. However, just as with functions, not all equivalence relations are of interest to us.

Consider a magma $$A$$ and an equivalence relation $$R$$. Suppose $$x\equiv x'\pmod{R}$$ and $$y\equiv y'\pmod{R}$$ hold. Since $$x$$ and $$x'$$, as well as $$y$$ and $$y'$$, are treated as the same elements by $$R$$, it is reasonable to expect the equation

$$x\star y\equiv x'\star y'\pmod{R}$$

to hold. However, without any conditions on $$R$$, there is no reason for this equation to hold. Therefore, we define the following additional condition.

<div class="definition" markdown="1">

<ins id="def9">**Definition 9**</ins> Let an equivalence relation $$R$$ be defined on a magma $$(A,\star)$$. If for any $$a\in A$$,

$$x\equiv x'\implies a\star x\equiv a\star x'$$

holds, we say that $$R$$ is *left compatible* with $$\star$$. Similarly, if

$$x\equiv x'\implies x\star a\equiv x'\star a$$

holds for all $$a$$, we say that $$R$$ is *right compatible* with $$\star$$. An equivalence relation that is both left and right compatible is simply called *compatible*.
</div>

Of course, in the above equations, $$\equiv$$ always refers to the relation $$R$$.

If $$R$$ is an equivalence relation, we have already seen in set theory that the *quotient set* $$A/R$$ is well-defined. ([[\[Set Theory\] §Equivalence Relations, ⁋Definition 4](/en/math/set_theory/equivalence_relations#def4)) The most natural attempt to define an operation $$\tiny\char\"2606$$ on the set $$A/R$$ is

$$[x]\mathbin{\tiny\char"2606}[y]=[x\star y]$$

However, for this equation to be meaningful, the value of $$[x]\mathbin{\tiny\char\"2606}[y]$$ must be well-defined even if we choose a representative $$x'$$ instead of $$x$$ for the equivalence class $$[x]$$. That is, the equation

$$[x\star y]=[x]\mathbin{\tiny\char"2606}[y]=[x'\star y]$$

must hold. This equation can be rewritten as

$$x'\star y\equiv x\star y\mod R$$

which, according to the previous definition, means precisely that $$R$$ must be *right* compatible with the operation. Similarly, since the value of the operation $$\mathbin{\tiny\char\"2606}$$ must not change with the choice of representative for $$[y]$$, $$R$$ must be *left* compatible with the operation.

Summarizing this, we obtain the following definition.

<div class="definition" markdown="1">

<ins id="def10">**Definition 10**</ins> Let an equivalence relation $$R$$ compatible with $$\star$$ be given on a magma $$(A,\star)$$. The magma $$(A/R,\mathbin{\tiny\char"2606})$$ obtained as above is called the *quotient magma*.

</div>

It is easy to verify that if $$\star$$ is associative or commutative, then $$\mathbin{\tiny\char"2606}$$ inherits the same property. In the above construction, we distinguished between $$\star$$ and $$\mathbin{\tiny\char"2606}$$ by using different notations, but since they are easily distinguishable from context, it is customary to denote the operation in the quotient magma also by $$\star$$.

---

**References**

**[Bou]** Bourbaki, N. Algebra I. *Elements of Mathematics*. Springer. 1998.

---
