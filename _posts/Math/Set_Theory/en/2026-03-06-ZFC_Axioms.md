---
title: "ZFC Axioms"
description: "We examine how Cantor's naive set theory leads to paradoxes like Russell's paradox, and introduce key axioms of ZFC such as the axiom of existence and the axiom of extensionality proposed to resolve them."
excerpt: "The axioms of set theory"

categories: [Math / Set Theory]
permalink: /en/math/set_theory/zfc_axioms
header:
    overlay_image: /assets/images/Math/Set_Theory/ZFC_Axioms.png
    overlay_filter: 0.5
sidebar: 
    nav: "set_theory-en"

date: 2021-08-07
weight: 1
translated_at: 2026-06-02T09:30:03+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-02T09:30:03+00:00
---
## Historical Background

It would be no exaggeration to say that set theory, as the foundation of the mathematics we study, began with Cantor in the 19th century. Cantor's naive set theory can be summarized by the following principle:

> For any property $$P$$, there exists a set $$Y=\{x\mid P(x)\}$$ of all elements satisfying $$P$$.

However, mathematicians discovered that this approach leads to various contradictions.

<div class="example" markdown="1">

<ins id="ex1">**Example 1 (Russell's Paradox)**</ins> Define the set $$\mathcal{S}$$ to be the collection of all $$x$$ satisfying $$x\not\in x$$. Then $$\mathcal{S}$$ is either an element of itself or not.

- Suppose $$\mathcal{S}$$ is an element of itself. Then $$\mathcal{S}$$ must also satisfy its defining property ($$x\not\in x$$), so $$\mathcal{S}\not\in\mathcal{S}$$. This contradicts the assumption that $$\mathcal{S}\in\mathcal{S}$$; hence $$\mathcal{S}$$ cannot be an element of itself.
- Therefore $$\mathcal{S}$$ must not be an element of itself; that is, $$\mathcal{S}\not\in\mathcal{S}$$. Yet this too is a contradiction. Since $$\mathcal{S}$$ is the collection of all elements satisfying $$x\not\in x$$, and $$\mathcal{S}$$ satisfies this property, it must belong to $$\mathcal{S}$$.

Thus, whether $$\mathcal{S}$$ is an element of itself or not, a contradiction arises in either case. This is called *Russell's paradox*.

</div>

To prevent such paradoxes, sets must be defined by rigorous methods rather than simply as <em-ko>collections of elements</em-ko>. The framework that accomplishes this is axiomatic set theory.

The posts in the [Set Theory](/en/set_theory) category are not intended as an introduction to axiomatic set theory, but as a starting topic for these posts, a brief overview of the ZFC axiom system—the most widely used system—seems a good choice.

## ZFC Axioms

If no sets existed at all, then any proposition we write about sets would be true. This is because the logical formula $$P\implies Q$$ is always true when $$P$$ is false, regardless of the truth value of $$Q$$. Therefore, our first axiom asserts that at least one set exists in this world.

<div class="misc" markdown="1">

**The Axiom of Existence.** There exists a set with no elements.
  
</div>

To give this <em-ko>set with no elements</em-ko> the name "empty set," we must first show that this set is unique. The following axiom justifies this.

<div class="misc" markdown="1">

**The Axiom of Extensionality.** For two sets $$A,B$$, if every element of $$A$$ is an element of $$B$$ and every element of $$B$$ is an element of $$A$$, then the two sets are equal.

</div>

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> There exists at most one set with no elements.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Let $$A$$ and $$B$$ be sets with no elements. Then both statements

$$((x\in A)\implies (x\in B)),\qquad ((x\in B)\implies (x\in A))$$

are true. Therefore, by the axiom of extensionality, $$A=B$$. 

</details>

Since the axiom of existence tells us that at least one such set exists, both the existence and uniqueness of a <em-ko>set with no elements</em-ko> are guaranteed. We now call this set the *empty set* and denote it by $$\emptyset$$.

The following axiom is worth remembering in particular because it prevents [Example 1](#ex1).

<div class="misc" markdown="1">

**The Axiom Schema of Comprehension.** Given any set $$A$$ and any proposition $$P$$, there exists a set $$B$$ such that <phrase>$$x\in B$$</phrase> and <phrase>$$x\in A$$ and $$P(x)$$</phrase> are equivalent.

</div>

From a formal standpoint, the above axiom asserts that a certain property holds for every proposition $$P$$. Since expressing this in first-order logic as a single statement is impossible, we regard it as a collection of axioms rather than a single axiom, and call it the axiom *schema* of comprehension.

The set $$B$$ defined by the comprehension schema is unique. If $$B'$$ is another set satisfying this condition, then

$$x\in B'\iff ((x\in A)\wedge P(x))\iff x\in B$$

and thus $$B=B'$$. It is appropriate to denote such a set by $$\{x\in A\mid P(x)\}$$.

<div class="example" markdown="1">

<ins id="ex3">**Example 3**</ins> What created the contradiction in naive set theory was the following assumption:

> Let $$P$$ be a proposition about $$x$$. Then there exists a set $$B$$ such that <phrase>$$x\in B$$</phrase> and <phrase>$$P(x)$$</phrase> are equivalent.

Now, according to the comprehension schema introduced above, unlike in [Example 1](#ex1), we cannot directly define $$\mathcal{S}=\{x\mid x\not\in x\}$$; we can only define

$$B=\{x\in A\mid x\not\in x\}$$

for an already existing set $$A$$. But unlike the set $$\mathcal{S}$$, this set creates no contradiction whatsoever. 

- If $$B\in B$$, then by definition $$B\not\in B$$ and $$B\in A$$, which is a contradiction. 
- If $$B\not\in B$$, then $$B\not\in A$$ **or** $$B\in B$$. 

In the second case, if $$B\in B$$ then we obtain a contradiction, so necessarily $$B\not\in A$$, and through this the contradiction of Russell's paradox is prevented.

</div>

<div class="example" markdown="1">

<ins id="ex4">**Example 4**</ins> The above example shows that when a set $$A$$ is given, there always exists a set $$B$$ not belonging to $$A$$. In particular, the <em-ko>set of all sets</em-ko>, that is, a universal set does not exist.  

</div>

By choosing the proposition $$P$$ appropriately, we can construct various familiar sets from the comprehension schema. That these are unique is obvious from extensionality.

<div class="example" markdown="1">

<ins id="ex5">**Example 5**</ins> For any sets $$A$$ and $$B$$, let the property $$P$$ concerning $$x$$ be given by $$x\in B$$. Then the set

$$\{x\in A\mid P(x)\}$$

is the collection of elements belonging to both $$A$$ and $$B$$. We call this set the *intersection* of $$A$$ and $$B$$, denoted $$A\cap B$$.

</div>

<div class="example" markdown="1">

<ins id="ex6">**Example 6**</ins> Now, given two sets $$A$$ and $$B$$, let the property $$Q$$ concerning $$x$$ be given by $$x\not\in B$$. Then the set

$$\{x\in A\mid Q(x)\}$$

is the collection of elements belonging to $$A$$ but not to $$B$$. We call this the *difference* of $$B$$ from $$A$$, denoted $$A\setminus B$$.

</div>

Alternatively, $$A\setminus B$$ is also called the *complement* of $$B$$ relative to $$A$$.[^1] 

If the existence of sets other than the empty set is not guaranteed, the above two examples are of little use. The following axioms provide methods for constructing non-empty sets.

<div class="misc" markdown="1">

**The Axiom of Pair.** For any sets $$A$$ and $$B$$, there exists a set $$C$$ such that <phrase>$$x\in C$$</phrase> and <phrase>$$x=A$$ or $$x=B$$</phrase> are equivalent.

</div>

Again, this set is unique by extensionality and is denoted $$\{A,B\}$$. Now taking $$A=B=\emptyset$$, from

$$x\in \{\emptyset\}\iff x=\emptyset\iff (x=\emptyset)\wedge(x=\emptyset)\iff x\in \{\emptyset,\emptyset\}$$

we obtain $$\{\emptyset, \emptyset\}=\{\emptyset\}$$. Also, since $$\emptyset\not\in \emptyset$$, we have $$\emptyset\neq\{\emptyset\}$$. 

<div class="misc" markdown="1">

**The Axiom of Union.** For any set $$\mathcal{S}$$, there exists a set $$U$$ such that <phrase>$$x\in U$$</phrase> and <phrase>$$x\in A$$ for some $$A\in\mathcal{S}$$</phrase> are equivalent.

</div>

For example, if $$\mathcal{S}=\{A,B\}$$, then we can verify that $$U$$ becomes the set of <phrase>elements satisfying $$x\in A$$ or $$x\in B$$</phrase>, that is, $$A\cup B$$. This is sometimes written as $$\bigcup\mathcal{S}$$.

<div class="misc" markdown="1">

**The Axiom of Power Set.** For any set $$S$$, there exists a set $$\mathcal{P}$$ such that <phrase>$$X\in \mathcal{P}$$</phrase> and <phrase>$$X\subseteq S$$</phrase> are equivalent.

</div>

This set is called the *power set* of $$S$$ and is denoted $$\mathcal{P}(S)$$. 

The ZFC axiom system includes several additional axioms beyond these, which will be introduced as needed.

---
**References**

**[HJJ]** K. Hrbacek, T.J. Jeck, and T. Jech. *Introduction to Set Theory*. Lecture Notes in Pure and Applied Mathematics. M. Dekker, 1978.  
**[Bou]** N. Bourbaki. *Elements of the History of Mathematics*. Springer, 2013  
Wikipedia, [Naive set theory](https://en.wikipedia.org/wiki/Naive_set_theory), [Set-theoretic definition of natural numbers](https://en.wikipedia.org/wiki/Set-theoretic_definition_of_natural_numbers).

---

[^1]: In axiomatic set theory, simply the "complement of $$B$$" does not exist. This is because its definition would require a universal set.
