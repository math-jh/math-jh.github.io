---
title: "ZFC Axioms"
excerpt: "The axioms of set theory"

categories: [Math / Set Theory]
permalink: /en/math/set_theory/zfc_axioms
header:
    overlay_image: /assets/images/Math/Set_Theory/ZFC_axioms.png
    overlay_filter: 0.5
sidebar:
    nav: "set_theory-en"

date: 2026-03-06
weight: 1

---

## Historical Background

It is no exaggeration to say that set theory as the foundation of mathematics began with Cantor in the 19th century. Cantor's naive set theory can be summarized by the following philosophy:

> For any property $P$, there exists a set $Y=\\{x\mid P(x)\\}$ consisting of all elements satisfying $P$.

However, mathematicians discovered that this approach leads to various contradictions.

<div class="example" markdown="1">

<ins id="ex1">**Example 1 (Russell's Paradox)**</ins> Consider the collection $\mathcal{S}$of all $x$ such that $x\not\in x$. Then $\mathcal{S}$ is either an element of itself or not.

- Suppose $\mathcal{S}$ is an element of itself. Then $\mathcal{S}$ must satisfy the defining property ($x\not\in x$), so $\mathcal{S}\not\in\mathcal{S}$. This contradicts the assumption that $\mathcal{S}\in\mathcal{S}$, so $\mathcal{S}$ cannot be an element of itself.
- Therefore, $\mathcal{S}\not\in\mathcal{S}$. But this is also a contradiction. Since $\mathcal{S}$ is the collection of all elements satisfying $x\not\in x$, and $\mathcal{S}$ satisfies this, it must belong to $\mathcal{S}$.

Thus, whether $\mathcal{S}$ is an element of itself or not, a contradiction arises. This is called *Russell's paradox*.

</div>

To prevent such paradoxes, sets must be defined rigorously rather than simply as "collections of elements." The framework for this is axiomatic set theory.

The posts in the [Set Theory](/en/set_theory) category are not intended to introduce axiomatic set theory per se, but as a starting topic, it seems appropriate to briefly introduce the ZFC axiom system, which is the most widely used.

## ZFC Axioms

If sets did not exist at all, then any statement we make about sets would be true. This is because the logical formula $P\implies Q$ is always true when $P$ is false, regardless of the truth value of $Q$. Therefore, our first axiom states that at least one set exists.

<div class="misc" markdown="1">

**The Axiom of Existence.** There exists a set with no elements.

</div>

To call this "set with no elements" the empty set, we must first show it is unique. The following axiom justifies this.

<div class="misc" markdown="1">

**The Axiom of Extensionality.** For two sets $A,B$, if every element of $A$ is an element of $B$ and every element of $B$ is an element of $A$, then the two sets are equal.

</div>

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> There exists at most one set with no elements.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Let $A$ and $B$ be sets with no elements. Then both statements

$$((x\in A)\implies (x\in B)),\qquad ((x\in B)\implies (x\in A))$$

are true. Therefore, by the axiom of extensionality, $A=B$.

</details>

Since the axiom of existence tells us that at least one such set exists, both the existence and uniqueness of a "set with no elements" are guaranteed. We now call this set the *empty set* and denote it by $\emptyset$.

The following axiom is worth remembering as it prevents [Example 1](#ex1).

<div class="misc" markdown="1">

**The Axiom Schema of Comprehension.** Given any set $A$ and any proposition $P$, there exists a set $B$ such that $x\in B$ is equivalent to ($x\in A$ and $P(x)$).

</div>

Formally, the above axiom asserts that a certain property holds for all propositions $P$. Since this cannot be expressed in first-order logic as a single axiom, we think of it as a collection of axioms rather than a single axiom, hence the term axiom *schema* of comprehension.

The set $B$ defined by the comprehension schema is unique. If $B'$ is another set satisfying this condition, then

$$x\in B'\iff ((x\in A)\wedge P(x))\iff x\in B$$

and thus $B=B'$. It is appropriate to denote such a set as $\\{x\in A\mid P(x)\\}$.

<div class="example" markdown="1">

<ins id="ex3">**Example 3**</ins> What caused the contradiction in naive set theory was the following assumption:

> Let $P$ be a proposition about $x$. Then there exists a set $B$ such that $x\in B$ is equivalent to $P(x)$.

According to the newly introduced comprehension schema, unlike [Example 1](#ex1), we cannot directly define $\mathcal{S}=\\{x\mid x\not\in x\\}$, but can only define

$$B=\{x\in A\mid x\not\in x\}$$

for an already existing set $A$. Unlike the set $\mathcal{S}$, this set creates no contradiction.

- If $B\in B$, then by definition $B\not\in B$ and $B\in A$, which is a contradiction.
- If $B\not\in B$, then $B\not\in A$ **or** $B\in B$.

In the second case, if $B\in B$ then we have a contradiction, so necessarily $B\not\in A$. This prevents the contradiction seen in Russell's paradox.

</div>

<div class="example" markdown="1">

<ins id="ex4">**Example 4**</ins> The above example shows that given any set $A$, there always exists a set $B$ not belonging to $A$. In particular, the "set of all sets," i.e., a universal set, does not exist.

</div>

By choosing the proposition $P$ appropriately, we can construct various familiar sets from the comprehension schema. Their uniqueness follows trivially from extensionality.

<div class="example" markdown="1">

<ins id="ex5">**Example 5**</ins> For any sets $A$ and $B$, let the property $P$ about $x$ be given by $x\in B$. Then the set

$$\{x\in A\mid P(x)\}$$

is the collection of elements belonging to both $A$ and $B$. We call this set the *intersection* of $A$ and $B$, denoted $A\cap B$.

</div>

<div class="example" markdown="1">

<ins id="ex6">**Example 6**</ins> Now for two given sets $A$ and $B$, let the property $Q$ about $x$ be given by $x\not\in B$. Then the set

$$\{x\in A\mid Q(x)\}$$

is the collection of elements belonging to $A$ but not to $B$. We call this the *difference* of $B$ from $A$, denoted $A\setminus B$.

</div>

Alternatively, $A\setminus B$ is also called the *complement* of $B$ relative to $A$.[^1]

If the existence of sets other than the empty set is not guaranteed, the above two examples are of little use. The following axioms provide ways to construct non-empty sets.

<div class="misc" markdown="1">

**The Axiom of Pair.** For any sets $A$ and $B$, there exists a set $C$ such that $x\in C$ is equivalent to ($x=A$ or $x=B$).

</div>

Again, this set is unique by extensionality and is denoted $\{A,B\}$. Now taking $A=B=\emptyset$, from

$$x\in \{\emptyset\}\iff x=\emptyset\iff (x=\emptyset)\wedge(x=\emptyset)\iff x\in \{\emptyset,\emptyset\}$$

we obtain $\\{\emptyset, \emptyset\\}=\\{\emptyset\\}$. Also, since $\emptyset\not\in \emptyset$, we have $\emptyset\neq\\{\emptyset\\}$.

<div class="misc" markdown="1">

**The Axiom of Union.** For any set $\mathcal{S}$, there exists a set $U$ such that $x\in U$ is equivalent to ($x\in A$ for some $A\in\mathcal{S}$).

</div>

For example, if $\mathcal{S}=\\{A,B\\}$, then $U$ is the set of elements satisfying ($x\in A$ or $x\in B$), i.e., $A\cup B$. This is sometimes written as $\bigcup\mathcal{S}$.

<div class="misc" markdown="1">

**The Axiom of Power Set.** For any set $S$, there exists a set $\mathcal{P}$ such that $X\in \mathcal{P}$ is equivalent to $X\subseteq S$.

</div>

This set is called the *power set* of $S$ and is denoted $\mathcal{P}(S)$.

The ZFC axiom system includes several other axioms beyond these, but we will introduce them as needed.

---
**References**

**[HJJ]** K. Hrbacek, T.J. Jeck, and T. Jech. *Introduction to Set Theory*. Lecture Notes in Pure and Applied Mathematics. M. Dekker, 1978.  
**[Bou]** N. Bourbaki. *Elements of the History of Mathematics*. Springer, 2013  
Wikipedia, [Naive set theory](https://en.wikipedia.org/wiki/Naive_set_theory), [Set-theoretic definition of natural numbers](https://en.wikipedia.org/wiki/Set-theoretic_definition_of_natural_numbers).

---

[^1]: In axiomatic set theory, simply the "complement of $B$" does not exist, since defining it requires a universal set.
