---

title: "ZFC axioms"
excerpt: "Axioms of the set theory"

lang: en
categories: [Math / Set Theory]
permalink: /en/math/set_theory/zfc_axioms
header:
    overlay_image: /assets/images/Set_theory/ZFC_axioms.png
    overlay_filter: 0.5
sidebar: 
    nav: "set-en"

date: 2021-06-02
last_modified_at: 2022-04-04
weight: 1

---

## Russell's paradox

One of the remarkable events in 20th century mathematics is the emergence of the axiomatic set theory. The naive set theory played an important role in laying the foundation for mathematics, but the informal nature of the theory made many contradictions, including the *Russell's paradox*.

<div class="example" markdown="1">

<ins id="ex1">**Example 1 (Russell's paradox)**</ins> Let $\mathcal{S}$ be the set consists of all $x$ satisfying $x\not\in x$. Then precisely the one of the following holds; either $\mathcal{S}\in\mathcal{S}$ or $\mathcal{S}\not\in\mathcal{S}$. 

- First assume that $\mathcal{S}\in\mathcal{S}$. Then by the defining property $x\not\in x$ of $\mathcal{S}$, we must have $\mathcal{S}\not\in\mathcal{S}$, contradicting the assumption that $\mathcal{S}\in\mathcal{S}$.
- So it must be the case that $\mathcal{S}\not\in\mathcal{S}$. This also yields a contradiction; since $\mathcal{S}$ then satisfies the property $x\not\in x$, it must be an element of itself.

</div>

In the view of modern mathematics, this kind of the paradox appears since we are defining sets in an ambiguous manner. These days, we introduce the notion of *axiomatic systems*, a collection of mathematical sentences that are believed to be true. The theory of sets therefore depends on the choice of the axiomatic system, but the most famous one is the ZFC, named after mathematicians Ernst Zermelo and Abraham Fraenkel. The letter $C$ stands for *choice*, which we introduce later. 

## The ZFC axioms

The statement $p\implies q$ is always true if $p$ is false. Thus any statement about the sets would be vacuously true if there is no set at all. We therefore introduce the following axiom.

<div class="misc" markdown="1">

**The axiom of existence.** There is a set with no element.

</div>

We would likely to call the set an *empty set*, but in mathematics, we should always see that the object is uniquely (in some sense) determined before giving it a name. The following axiom tells us when the two sets are the same.

<div class="misc" markdown="1">

**The axiom of extensionality.** If every element of $A$ is an element of $B$ and every element of $B$ is also an element of $A$, then two sets are the same.

</div>

From the extensionality we can prove that the set with no element is unique.

<div class="proposition" markdown="1">

<ins id="pp2">**Proposition 2**</ins> There is at most one set with no element.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Let $A$, $B$ be sets with no element. Then two statements

$$(x\in A)\implies (x\in B),\qquad (x\in B)\implies (x\in A)$$

are both true. Therefore the axiom of extensionality applies to complete the proof.

</details>

Therefore, we can now define the *empty set*, which we denote by $\emptyset$. 

The Russell's paradox arose because of the following assumption.

> (Unrestricted comprehension schema) Let $P$ be a statement. Then there exists a set $B$ such that $x\in B$ iff $P(x)$ true.

To prevent such a failure, our theory now *restrict* the above schema as follows.

<div class="misc" markdown="1">

**The axiom schema of comprehension.** Let $A$ be a set, and $P$ be a statement. Then there exists a set $B$ such that $x\in B$ iff both $P(x)$ and $x\in A$ hold. 

</div>

The word *schema* means that the above statement is not a single statement; instead, it is the collection of axioms, which are determined by choosing a statement $P$. 

We first observe that such a set $B$ is uniquely determined. Indeed, if $B'$ is another set satisfying the above condition, then we have

$$x\in B'\iff ((x\in A)\wedge P(x))\iff x\in B$$

so $B=B'$ by the extensionality axiom. Thus it make sense to name such a set and denote by $\\{x\in A:P(x)\\}$. 

Anyway, the comprehension schema avoids the Russell-like paradox as follows.

<div class="example" markdown="1">

<ins id="ex3">**Example 3**</ins> Let $A$ be a set and $P$ the property $x\not\in x$. By the axiom schema of comprehension, we can construct the set

$$B=\{x\in A:P(x)\}$$

and this set does not make any problem this case. First assume $B\in B$. Then by definition of $B$, we have $(B\not\in B)\wedge (B\in A)$; in particular $B\not\in B$ so we get a contradiction this case. The case $B\not\in B$ is not problematic, however. If $B\not\in B$ then we get *either* $B\not\in A$ *or* $B\in B$. It must follows that $B\not\in A$. 

</div>

The same argument as [Example 1](#ex1) now does not make any problem; instead it proves $B\not\in A$. This also shows the following:

<div class="example" markdown="1">

<ins id="ex4">**Example 4**</ins> The universal set does not exist. If $U$ is such a set, then $V=\\{x\in U:x\not\in x\\}$ is a set that does not belong to $U$.

</div>

In practice, the comprehension schema can be used to construct certain sets. (Of course this can be done by unrestricted comprehension schema, either.)

<div class="example" markdown="1">

<ins id="ex5">**Example 5**</ins> Let $A,B$ be sets and $P(x):x\in B$ a statement. Then the following set

$$\{x\in A:P(x)\}$$

is the set of $x$ that belongs to both $A$ and $B$. The above set is uniquely defined, and is called the *intersection* of $A$ and $B$. (Notation: $A\cap B$)

</div>

<div class="example" markdown="1">

<ins id="ex6">**Example 6**</ins> Let $A,B$ be sets and $Q(x):x\not\in B$ a statement. Then the following set

$$\{x\in A:Q(x)\}$$

is the set of $x$ that is in $A$ but not in $A$. The set is called the *relative complement* of $B$ in $A$ and is denoted by $A\setminus B$.

</div>
<div class="remark" markdown="1">

<ins id="rmk1">**Remark**</ins> The *absolute complement* $A^c$ does not make sense in the axiomatic point of view; it presumes the existence of the universal set, which does not exist. However, in many part of mathematics, the "universal" set $X$, which contains all the elements under study, is fixed and therefore the notation $A^c$ is often used to denote the set $X\setminus A$. 

</div>

So far we have introduced three axioms, but the only set we have is $\emptyset$. Its existence is guaranteed by the axiom of existence, but one cannot make sets other than $\emptyset$ using the comprehension schema. We therefore introduce three more axioms that would be useful in constructing the larger sets.

<div class="misc" markdown="1">

**The axiom of pair.** For an arbitrary set $A,B$ given, there exists a set $C$ such that $x\in C$ iff $x\in A$ or $x\in B$ hold.

</div>

One can easily prove that such a set $C$ is uniquely determined; such set will be denoted by $\\{A,B\\}$. And as an exercise one can also prove that the set $\\{\emptyset,\emptyset\\}$ is same as the set $\\{\emptyset\\}$ (extensionality), and that $\\{\emptyset\\}$ is different from $\emptyset$ (since $\emptyset\not\in\emptyset$).  

However, the above construction is not strong enough. For instance, any set obtained from the axiom of pair would be a singleton or a set with two element. Therefore we also introduce:

<div class="misc" markdown="1">

**The axiom of union.** For any set $\mathcal{S}$ there exists a set $U$ such that $x\in U$ iff $x\in A$ for some $A\in\mathcal{S}$.

</div>

This uniquely determined set is called the *union* of $\mathcal{S}$ and denoted by $\bigcap\mathcal{S}$. Make sure you keep your feet on the ground by apply the above axiom to the set $\mathcal{S}=\\{A,B\\}$.

There are more ZFC axioms, but we end this article by introducing the axiom of power set; the others would be introduced later.

<div class="misc" markdown="1">

**The axiom of power set.** For any set $S$, there exists a set $\mathcal{P}$ such that $X\in \mathcal{P}$ iff $X\subset S$.

</div>

The set $\mathcal{P}$ is called the *power set* of $S$ and is denoted by $\mathcal{P}(S)$.
