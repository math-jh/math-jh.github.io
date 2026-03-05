---

title: "Binary Relations"
excerpt: "Definition of Binary Relation"

categories: [Math / Set Theory]
permalink: /en/math/set_theory/binary_relation

header:
    overlay_image: /assets/images/Math/Set_Theory/Binary_relation.png
    overlay_filter: 0.5

sidebar: 
    nav: "set_theory-en"

date: 2026-03-06
last_modified_at: 2026-03-06

weight: 3

---

## Binary Relation

Let us begin with the definition. The following definition is nothing particularly special; it simply gives a name to the *set of ordered pairs* that appeared while explaining why ordered pairs need to be introduced in [§Ordered Pair](/en/math/set_theory/ordered_pair#ordered-pair).

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> A set $R$ is called a *binary relation* if every element of $R$ is an ordered pair.[^1]

</div>

Therefore, the equality ($=$) defined between sets can no longer be considered a binary relation.

<div class="example" markdown="1">

<ins id="ex2">**Example 2**</ins> If $=$ between sets were a binary relation, then the set representing it

$$E=\{(A,A)\mid\text{$A$ any set}\}$$

would exist. That is, $E$ would have to be the product of two universal sets.

</div>

If the product of two universal sets exists, then by the following proposition, a universal set must also exist, which contradicts [§ZFC Axioms, ⁋Example 4](/en/math/set_theory/zfc_axioms#ex4). Therefore, $=$ defined between all sets cannot be a binary relation.

<div class="proposition" markdown="1">

<ins id="prop3">**Proposition 3**</ins> Let $R$ be a binary relation. Then there exist unique sets $A$ and $B$ such that:

<ul>
<li> <phrase>$x\in A$</phrase> is equivalent to <phrase>there exists some $y$ such that $(x,y)\in R$</phrase>, and</li>
<li> <phrase>$y\in B$</phrase> is equivalent to <phrase>there exists some $x$ such that $(x,y)\in R$</phrase>.</li>
</ul>

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Let $R$ be a binary relation and consider $\bigcup(\bigcup R)$. Through calculation, we can see that $(x,y)\in R\implies x,y\in\bigcup(\bigcup R))$. Define $P$ as

> $P(t)$: There exists some $s$ such that $(s,t)\in R$.

Then we obtain the following set

$$A=\left\{x\mid\left(x\in\bigcup\left(\bigcup R\right)\right)\wedge P(x)\right\}$$

Thus the first claim holds. Similarly, by defining property $Q$ as

> $Q(s)$: There exists some $t$ such that $(s,t)\in R$.

we obtain set $B$.

</details>

As in [§Ordered Pair, ⁋Definition 7](/en/math/set_theory/ordered_pair#def7), these are called the first and second *projections* respectively, and are written as $\pr_1R$ and $\pr_2R$.

Sometimes it is necessary to clarify which sets the first and second components of a binary relation belong to. For this purpose, given two sets $A,B$ and a binary relation $R$ satisfying $\pr\_1R\subseteq A$ and $\pr\_2R\subseteq B$, we sometimes think of it as a triple $(R,A,B)$. In this case, $A$ is called the *source* of $R$, and $B$ is called the *target* of $R$. In such situations, even for the same set $R$, $(R,A,B)$ and $(R,A',B')$ are considered different.

<div class="remark" markdown="1">

<ins id="rmk1">**Remark**</ins> Let $R$ be a binary relation satisfying the above conditions $\pr\_1R\subseteq A$ and $\pr\_2R\subseteq B$. By [§Ordered Pair, ⁋Proposition 9](/en/math/set_theory/ordered_pair#prop9),

$$R\subseteq \pr_1 R\times\pr_2R\subseteq A\times B$$

Therefore, the Cartesian product $A\times B$ can be said to be the largest among all binary relations having $A$ as source and $B$ as target.

</div>

## Domain and Image of a Binary Relation

<div class="definition" markdown="1">

<ins id="def5">**Definition 5**</ins> Consider a binary relation $(R,A,B)$ and a subset $A'\subseteq A$. Then the *image* of $A'$ under $R$, denoted by $R(A')$, is defined as the set of all elements related to elements of $A'$ by $R$.

</div>

Expressing the above definition as a formula:

$$R(A')=\bigcup_{x\in A'} \{y\in B\mid(x,y)\in R\}$$

Strictly speaking, the set on the right-hand side $\{y\in B\mid(x,y)\in R\}$ would take the form

$$\{y\mid(x,y)\in R\}$$

if the target $B$ of binary relation $R$ is not given. Unlike the set above whose existence is guaranteed by the comprehension schema, this set may not exist.

Such issues must always be kept in mind when studying set theory. However, since our goal is not to study set theory per se, but rather to prove propositions that will be useful elsewhere, we will pass over such minor notational issues without much thought.

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6**</ins> Let $R$ be a binary relation, and consider any set $A$ and its subset $X$. Then $R(X)\subseteq R(A)$ holds.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

Let $y\in R(X)$. Then there exists some $x\in X$ such that $(x,y)\in R(X)$. Now since $X\subseteq A$, we have $x\in A$, and thus $y\in R(A)$.

</details>

By the above proposition, for any $A$,

$$R(A)=\pr_2\{z\in R\mid\text{$\pr_1z\in A$}\}\subset\pr_2R$$

and therefore $R(A)\subset\pr_2R$ holds. In particular, if $A=\emptyset$, then $R(A)=\emptyset$. More generally, if $A\cap\pr_1R=\emptyset$, then $R(A)=\emptyset$.

If $A=\{x\}$ for some $x$, then $R(A)$ can be thought of as the value of $R$ at $x$, similar to a function value.

<div class="definition" markdown="1">

<ins id="def7">**Definition 7**</ins> For a binary relation $R$, the set $R(\{x\})$ is called the *section* of $R$ at $x$.

</div>

This set is sometimes written as $R(x)$, treating it like the value of $R$ at $x$. This *function value* is not unique, and therefore $R(x)$ may have multiple elements.

---
**References**

**[HJJ]** K. Hrbacek, T.J. Jeck, and T. Jech. *Introduction to Set Theory*. Lecture Notes in Pure and Applied Mathematics. M. Dekker, 1978.  
**[Bou]** N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---

[^1]: In **[Bou]**, such a set is called a *graph*, and a distinction is made between binary relations that have graphs and those that do not. Since this is not a common definition, we follow **[HJJ]** and use the above definition as is. In this case, the definition of the word "relation" becomes somewhat ambiguous, but we will not define it separately.
