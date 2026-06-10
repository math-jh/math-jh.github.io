---
title: "Binary Relations"
description: "Defines a binary relation as a set of ordered pairs, and discusses the existence conditions of the two sets that constitute the relation along with the concepts of projection, source, and target."
excerpt: "The definition of binary relations"

categories: [Math / Set Theory]
permalink: /en/math/set_theory/binary_relation


sidebar: 
    nav: "set_theory-en"

date: 2021-08-14
last_modified_at: 2022-11-22

weight: 3
translated_at: 2026-06-02T10:30:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-02T10:30:02+00:00
---
## Binary Relations

We begin with the definition. The following definition is nothing special; it merely gives a name to the *set of ordered pairs* that appeared in [§Ordered Pairs](/en/math/set_theory/ordered_pair#ordered-pairs) when we explained the motivation for introducing ordered pairs.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> A set $$R$$ is called a *binary relation* if every element of $$R$$ is an ordered pair.[^1]

</div>

Thus, equality ($$=$$) defined between all sets can no longer be called a binary relation.

<div class="example" markdown="1">

<ins id="ex2">**Example 2**</ins> If $$=$$ were a binary relation between sets, then the set representing it

$$E=\{(A,A)\mid\text{$A$ any set}\}$$

would exist. That is, $$E$$ would have to be the product of two universal sets.

</div>

If the product of two universal sets existed, then by the following proposition a universal set would also have to exist, which contradicts [§ZFC Axioms, ⁋Example 4](/en/math/set_theory/zfc_axioms#ex4). Therefore, the $$=$$ defined between all sets cannot be a binary relation.

<div class="proposition" markdown="1">

<ins id="prop3">**Proposition 3**</ins> Let $$R$$ be a binary relation. Then there exist unique sets $$A$$ and $$B$$ such that

<ul>
<li> <phrase>$x\in A$</phrase> is equivalent to <phrase>there exists some $y$ with $(x,y)\in R$</phrase>, and</li>
<li> <phrase>$y\in B$</phrase> is equivalent to <phrase>there exists some $x$ with $(x,y)\in R$</phrase>.</li>
</ul>

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Let $$R$$ be a binary relation and consider $$\bigcup(\bigcup R)$$. By calculation, we see that $$(x,y)\in R\implies x,y\in\bigcup(\bigcup R))$$. Define $$P$$ by

> $$P(t)$$: there exists some $$s$$ such that $$(s,t)\in R$$.

Then we obtain the set

$$A=\left\{x\mid\left(x\in\bigcup\left(\bigcup R\right)\right)\wedge P(x)\right\}.$$

Thus the first claim holds, and similarly defining the property $$Q$$ by

> $$Q(s)$$: there exists some $$t$$ such that $$(s,t)\in R$$.

we obtain the set $$B$$.

</details>

As in [§Ordered Pairs, ⁋Definition 7](/en/math/set_theory/ordered_pair#def7), we call these the first and second *projections* of $$R$$, and write them as $$\pr_1R$$ and $$\pr_2R$$.

Occasionally, we need to specify which sets the first and second components of a binary relation belong to. For this purpose, given two sets $$A,B$$ and a binary relation $$R$$ with $$\pr_1R\subseteq A$$ and $$\pr_2R\subseteq B$$, we sometimes regard $$R$$ as the triple $$(R,A,B)$$. In this case, we call $$A$$ the *source* of $$R$$ and $$B$$ the *target* of $$R$$, and under this convention we regard $$(R,A,B)$$ and $$(R,A',B')$$ as distinct even for the same set $$R$$.

<div class="remark" markdown="1">

**Remark**</ins> Suppose a binary relation $$R$$ satisfying the above conditions $$\pr_1R\subseteq A$$, $$\pr_2R\subseteq B$$ is given. By [§Ordered Pairs, ⁋Proposition 9](/en/math/set_theory/ordered_pair#prop9),

$$R\subseteq \pr_1 R\times\pr_2R\subseteq A\times B$$

so the Cartesian product $$A\times B$$ can be said to be the largest binary relation with source $$A$$ and target $$B$$.

</div>

## Domain and Image of a Binary Relation

<div class="definition" markdown="1">

<ins id="def4">**Definition 4**</ins> Consider a binary relation $$(R,A,B)$$ and a subset $$A'\subseteq A$$. Then the set of <phrase>all elements related by $R$ to elements of $A'$</phrase> is called the *image* of $$A'$$ under $$R$$, and is denoted $$R(A')$$.

</div>

Writing out the above definition as a formula, we have

$$R(A')=\bigcup_{x\in A'} \{y\in B\mid(x,y)\in R\}.$$

Strictly speaking, the set $$\{y\in B\mid(x,y)\in R\}$$ on the right-hand side, if the target $$B$$ of the binary relation $$R$$ is not given, becomes

$$\{y\mid(x,y)\in R\}$$

and unlike the above set whose existence is guaranteed by the comprehension schema, this set may not exist.

This kind of issue is something we must always be careful about when studying set theory. However, since our goal is not to study set theory itself but to prove propositions that will be useful elsewhere, we will pass over this level of minor technical issues without much thought from now on.

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> Let $$R$$ be a binary relation, and consider any set $$A$$ and its subset $$X$$. Then $$R(X)\subseteq R(A)$$ holds.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

Let $$y\in R(X)$$. Then there exists some $$x\in X$$ such that $$(x,y)\in R$$. Since $$X\subseteq A$$, we have $$x\in A$$, and thus $$y\in R(A)$$.

</details>

By the above proposition, for any $$A$$ we have

$$R(A)=\pr_2\{z\in R\mid\text{$\pr_1z\in A$}\}\subset\pr_2R$$

and therefore $$R(A)\subset\pr_2R$$ holds. In particular, if $$A=\emptyset$$ then $$R(A)=\emptyset$$, and more generally if $$A\cap\pr_1R=\emptyset$$ then $$R(A)=\emptyset$$.

If for some $$x$$ we have $$A=\{x\}$$, we can think of $$R(A)$$ as something like the value of $$R$$ at $$x$$.

<div class="definition" markdown="1">

<ins id="def6">**Definition 6**</ins> For a binary relation $$R$$, the set $$R(\{x\})$$ is called the *section* of $$R$$ at $$x$$.

</div>

This set is sometimes written as $$R(x)$$, as if it were the value of $$R$$ at $$x$$. This *value* is not unique, and therefore $$R(x)$$ may contain more than one element.

---
**References**

**[HJJ]** K. Hrbacek, T.J. Jeck, and T. Jech. *Introduction to Set Theory*. Lecture Notes in Pure and Applied Mathematics. M. Dekker, 1978.  
**[Bou]** N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---

[^1]: In **[Bou]**, such a set is called a *graph*, and binary relations are distinguished into those that have a graph and those that do not. This is not a very common definition, so we follow **[HJJ]** and use the above definition as is. In this case, the definition of the word "relation" becomes somewhat ambiguous, but we pass over this without further definition.
