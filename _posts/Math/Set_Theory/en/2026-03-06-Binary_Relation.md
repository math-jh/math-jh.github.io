---
title: "Binary Relations"
excerpt: "The definition of binary relations"

categories: [Math / Set Theory]
permalink: /en/math/set_theory/binary_relation

header:
    overlay_image: /assets/images/Math/Set_Theory/Binary_Relation.png
    overlay_filter: 0.5

sidebar: 
    nav: "set_theory-en"

date: 2021-08-14
last_modified_at: 2022-11-22

weight: 3
translated_at: 2026-05-23T17:00:03+00:00
translation_source: kimi-cli
---
## Binary Relations

We begin with the definition. The following definition is nothing special; it merely gives a name to the *set of ordered pairs* that appeared in [§Ordered Pairs](/en/math/set_theory/ordered_pair#ordered-pairs) when explaining the motivation for introducing ordered pairs.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> A set $$R$$ is called a *binary relation* if every element of $$R$$ is an ordered pair.[^1]

</div>

Therefore, equality ($$=$$) defined between all sets can no longer be called a binary relation.

<div class="example" markdown="1">

<ins id="ex2">**Example 2**</ins> If $$=$$ were a binary relation between sets, then the set representing it

$$E=\{(A,A)\mid\text{$A$ any set}\}$$

would exist. That is, $$E$$ would have to be the product of two universal sets.

</div>

If the product of two universal sets existed, then by the following proposition a universal set would also have to exist, which contradicts [§ZFC Axioms, ⁋Example 4](/en/math/set_theory/zfc_axioms#ex4). Hence $$=$$ defined between all sets cannot be a binary relation.

<div class="proposition" markdown="1">

<ins id="prop3">**Proposition 3**</ins> Let $$R$$ be a binary relation. Then there exist unique sets $$A$$ and $$B$$ such that

<ul>
<li> <phrase>$x\in A$</phrase> is equivalent to <phrase>there exists some $y$ such that $(x,y)\in R$</phrase>, and</li>
<li> <phrase>$y\in B$</phrase> is equivalent to <phrase>there exists some $x$ such that $(x,y)\in R$</phrase>.</li>
</ul>

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Let $$R$$ be a binary relation and consider $$\bigcup(\bigcup R)$$. By computation we see that $$(x,y)\in R\implies x,y\in\bigcup(\bigcup R))$$. If we define $$P$$ by

> $$P(t)$$: there exists some $$s$$ such that $$(s,t)\in R$$.

then we obtain the set

$$A=\left\{x\mid\left(x\in\bigcup\left(\bigcup R\right)\right)\wedge P(x)\right\}$$

Thus the first claim holds, and similarly, defining the property $$Q$$ by

> $$Q(s)$$: there exists some $$t$$ such that $$(s,t)\in R$$.

we obtain the set $$B$$.

</details>

As in [§Ordered Pairs, ⁋Definition 7](/en/math/set_theory/ordered_pair#def7), we call these the first and second *projections*, and write them as $$\pr_1R$$ and $$\pr_2R$$.

Occasionally it is necessary to make explicit which sets the first and second components of a binary relation belong to. For this purpose, a binary relation $$R$$ satisfying $$\pr_1R\subseteq A$$ and $$\pr_2R\subseteq B$$ for given sets $$A$$ and $$B$$ is sometimes regarded as a triple $$(R,A,B)$$. In this case, we call $$A$$ the *source* of $$R$$ and $$B$$ the *target* of $$R$$, and in such a situation we regard $$(R,A,B)$$ and $$(R,A',B')$$ as distinct even for the same set $$R$$.

<div class="remark" markdown="1">

<ins id="rmk1">**Remark**</ins> Let $$R$$ be a binary relation satisfying the above conditions $$\pr_1R\subseteq A$$ and $$\pr_2R\subseteq B$$. By [§Ordered Pairs, ⁋Proposition 9](/en/math/set_theory/ordered_pair#prop9),

$$R\subseteq \pr_1 R\times\pr_2R\subseteq A\times B$$

so the Cartesian product $$A\times B$$ may be said to be the largest binary relation with source $$A$$ and target $$B$$.

</div>

## Domain and Image of Binary Relations

<div class="definition" markdown="1">

<ins id="def5">**Definition 5**</ins> Consider a binary relation $$(R,A,B)$$ and a subset $$A'\subseteq A$$. Then we call the <phrase>set of all elements related to elements of $A'$ by $R$</phrase> the *image* of $$A'$$ under $$R$$, and denote it by $$R(A')$$.

</div>

Writing out the above definition as a formula gives

$$R(A')=\bigcup_{x\in A'} \{y\in B\mid(x,y)\in R\}$$

Strictly speaking, the set $$\{y\in B\mid(x,y)\in R\}$$ on the right-hand side, if the target $$B$$ of the binary relation $$R$$ were not given,

$$\{y\mid(x,y)\in R\}$$

would take a form like this; unlike the preceding set whose existence is guaranteed by the comprehension schema, this set might not exist.

We must always be wary of such issues when studying set theory. However, our purpose is not to study set theory for its own sake but to prove propositions that are useful elsewhere, so from now on we will gloss over such minor descriptive matters without much thought.

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6**</ins> Let $$R$$ be a binary relation, and consider any set $$A$$ and its subset $$X$$. Then $$R(X)\subseteq R(A)$$.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

Let $$y\in R(X)$$. Then there exists some $$x\in X$$ such that $$(x,y)\in R(X)$$. Since $$X\subseteq A$$, we have $$x\in A$$, and therefore $$y\in R(A)$$.

</details>

By the above proposition, for any $$A$$ we have

$$R(A)=\pr_2\{z\in R\mid\text{$\pr_1z\in A$}\}\subset\pr_2R$$

and therefore $$R(A)\subset\pr_2R$$ holds. In particular, if $$A=\emptyset$$ then $$R(A)=\emptyset$$, and more generally if $$A\cap\pr_1R=\emptyset$$ then $$R(A)=\emptyset$$.

If $$A=\{x\}$$ for some $$x$$, then we may think of $$R(A)$$ as the value of $$R$$ at $$x$$, much like a function value.

<div class="definition" markdown="1">

<ins id="def7">**Definition 7**</ins> For a binary relation $$R$$, the set $$R(\{x\})$$ is called the *section* of $$R$$ at $$x$$.

</div>

This set is sometimes written as $$R(x)$$, as if it were the function value of $$R$$ at $$x$$. This *function value* is not unique, and thus $$R(x)$$ may contain several elements.

---

**References**

**[HJJ]** K. Hrbacek, T.J. Jeck, and T. Jech. *Introduction to Set Theory*. Lecture Notes in Pure and Applied Mathematics. M. Dekker, 1978.  
**[Bou]** N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---

[^1]: In **[Bou]**, such a set is called a *graph*, and a distinction is made between binary relations that have a graph and those that do not. This is not a very common definition, so we follow **[HJJ]** and use the above definition as it stands. In this case, the definition of the word *relation* becomes somewhat ambiguous, but we will pass over this without giving a separate definition.
