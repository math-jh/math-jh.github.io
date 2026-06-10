---
title: "Sum of Sets"
description: "This post defines the concepts of covers and partitions of a set, and discusses the refinement relation of covers, images under surjective functions, and the existence conditions for partitions."
excerpt: "Sum (disjoint union) of a family of sets"

categories: [Math / Set Theory]
permalink: /en/math/set_theory/sum_of_sets
sidebar: 
    nav: "set_theory-en"

date: 2021-08-15
last_modified_at: 2022-11-25
weight: 9
translated_at: 2026-06-02T12:30:01+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-02T12:30:01+00:00
---
## Covering

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> A family $$(A_i)_{i\in I}$$ is a *covering* of a set $$A$$ if $$A=\bigcup_{i\in I} A_i$$. For two coverings $$(A_i)_{i\in I}$$ and $$(A'_j)_{j\in J}$$ of $$A$$, we say that $$(A'_j)_{j\in J}$$ is *finer* than $$(A_i)_{i\in I}$$ if for every $$j\in J$$, there exists $$i\in I$$ such that $$A'_j\subseteq A_i$$.

</div>

Let a covering $$(A_i)_{i\in I}$$ of a set $$A$$ be given. Then for any function $$f:B \rightarrow A$$, the family $$(f^{-1}(A_i))_{i\in I}$$ of subsets of $$B$$ is a covering of $$B$$. We call this the preimage of $$(A_i)$$ under $$f$$. For any function $$g:A\rightarrow C$$, the family $$(g(A_i))_{i\in I}$$ of subsets of $$C$$ need not be a covering of $$C$$, but if $$g$$ is surjective then these sets do cover $$C$$. We call this the image of $$(A_i)$$ under the surjection $$g$$. 

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> Consider a set $$A$$ with its covering $$(A_i)_{i\in I}$$, and pick an arbitrary set $$B$$.

1. Suppose functions $$f,g:A\rightarrow B$$ satisfy $$f\vert_{A_i}=g\vert_{A_i}$$ for every $$i\in I$$. Then $$f=g$$. 
2. If a family of functions $$(f_i:A_i\rightarrow B)_{i\in I}$$ satisfies the condition
    
    $$f_i\vert_{A_i\cap A_j}=f_j\vert_{A_i\cap A_j}$$

    then there exists a function $$f:A\rightarrow B$$ extending all the $$f_i$$.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

To prove the first claim, let an arbitrary $$x\in A$$ be given. Since $$(A_i)_{i\in I}$$ covers $$A$$, there exists some $$i\in I$$ such that $$x\in A_i$$. Now

$$f(x)=(f\vert_{A_i})(x)=(g\vert_{A_i})(x)=g(x)$$

and thus the first claim holds.

For the second claim, use the given functions $$f_i=(F_i,A_i,B)$$ to form $$F=\bigcup F_i$$, and consider the new triple $$f=(F,A,B)$$. Then $$\pr_1F=A$$ is obvious, so to show that $$f$$ is a function it suffices to prove that for any $$x\in A$$, there is a unique $$y$$ such that $$(x,y)\in F$$.

Suppose $$y,y'\in B$$ satisfy $$(x,y)\in F$$ and $$(x,y')\in F$$. Then there exist $$i,j$$ such that $$(x,y)\in F_i$$ and $$(x,y')\in F_j$$. Now 

$$y=(f_i)(x)=(f_i\vert_{A_i\cap A_j})(x)=(f_j\vert_{A_i\cap A_j})(x)=(f_j)(x)=y'$$

and thus the second claim also holds.

</details>

It is obvious from the first claim that a function $$f$$ satisfying condition 2 of the above proposition is unique. Also, if in particular $$A_i\cap A_j=\emptyset$$ for all $$i,j$$, then the hypothesis of the second claim is always satisfied. We define this as follows.

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> Sets $$A$$ and $$B$$ are *disjoint* if $$A\cap B=\emptyset$$. More generally, a family $$(A_i)_{i\in I}$$ is *pairwise disjoint* if for any $$i, j\in I$$ with $$i\neq j$$, we have $$A_i\cap A_j=\emptyset$$.

</div>

<div class="definition" markdown="1">

<ins id="def4">**Definition 4**</ins> A *partition* of a set $$A$$ is a pairwise disjoint covering of $$A$$.

</div>

In general, since $$\emptyset$$ plays no role among the members of this family, when we speak of a partition we assume that no member is empty.

## Sum of Sets

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> Let $$(A_i)_{i\in I}$$ be a family of sets. Then there exists a set $$S$$ such that 

- $$S$$ is the union of a pairwise disjoint family $$(S_i)_{i\in I}$$, and 
- for every $$i\in I$$ there exists a bijection from $$A_i$$ to $$S_i$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

For each $$i\in I$$, let $$S_i$$ be the set of all pairs $$(x, i)$$ with $$x\in A_i$$. Then $$(S_i)_{i\in I}$$ is pairwise disjoint. Also, for each $$i$$, the map $$x\mapsto (x,i)$$ is a bijection from $$A_i$$ to $$S_i$$. Therefore $$S=\bigcup_{i\in I} S_i$$ satisfies the required conditions.

</details>

<div class="definition" markdown="1">

<ins id="def6">**Definition 6**</ins> A set $$S$$ satisfying the above conditions is called the *sum* of the family $$(A_i)_{i\in I}$$, and is denoted by $$\sum_{i\in I} A_i$$.

</div>

This set is sometimes called the *disjoint union*, and is also written as $$\bigsqcup_{i\in I} A_i$$. The following proposition shows that this name is quite reasonable.

<div class="proposition" markdown="1">

<ins id="prop7">**Proposition 7**</ins> Consider a pairwise disjoint family $$(A_i)_{i\in I}$$. Let $$A$$ be their union and $$S$$ their sum. Then there exists a bijection between $$A$$ and $$S$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

If $$f_i:A_i\rightarrow S_i$$ are bijections satisfying the conditions of [Proposition 5](#prop5), then by [Proposition 2](#prop2) we can extend $$(f_i)_{i\in I}$$ to $$\bigcup_{i\in I} A_i=A$$.

</details>

The intuition for why this is called the sum of sets will appear later. ([§Operations on Cardinals, ⁋Definition 1](/en/math/set_theory/operation_of_cardinals#def1))

## Universal property

There is something we did not mention in [Definition 6](#def6). The sum $$X$$ of a family of sets $$(A_i)$$ is not unique. There are infinitely many sets satisfying the conditions of [Proposition 5](#prop5). For example, in the proof of that proposition we took $$S$$ to be the set of pairs $$(x,i)$$, but one can see that taking the set of pairs $$(i,x)$$ also satisfies the definition of sum. Therefore, strictly speaking, writing the sum of the $$A_i$$ as $$\sum A_i$$ is not a well-defined expression.

First, let us examine the *universal property* of the sum as follows.

<div class="proposition" markdown="1">

<ins id="thm8">**Theorem 8 (Universal property of sum)**</ins> Let a family of sets $$(A_i)$$, a set $$S$$ as defined in [Proposition 5](#prop5), and injections $$\iota_i:A_i\rightarrow S$$ be given. Then, whenever another set $$B$$ and maps $$f_i:A_i\rightarrow B$$ are given, there exists a unique $$f:S\rightarrow B$$ such that $$f_i=f\circ\iota_i$$. 

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, let us show that such a function $$f$$ is unique (if it exists). For this, it suffices to show that for any $$x\in S$$, its function value $$f(x)$$ is always uniquely determined. Since $$S$$ is the union of a pairwise disjoint family $$(S_i)$$, there exists a unique $$i\in I$$ such that $$x\in S_i$$. Then since $$\iota_i:A_i\rightarrow S_i$$ is a bijection, there again exists a unique element $$x_i$$ of $$A_i$$ such that $$\iota_i(x_i)=x$$. Now,

$$f(x)=f(\iota_i(x_i))=(f\circ\iota_i)(x_i)=f_i(x_i)$$

so the function value $$f(x)$$ at $$x$$ must equal $$f_i(x_i)$$, and therefore $$f$$ is uniquely determined.

Now, taking a hint from the uniqueness proof, let us show the existence of the function $$f$$. Define $$f(x)$$ to be $$f_i(x_i)$$ as in the above equation, and prove that $$f$$ is actually a function. For instance, with this definition $$f$$ will be defined for all elements of $$S$$, and moreover a single $$x$$ is assigned exactly one function value as discussed above.

</details>

In many cases the set $$S$$ appearing in the proof of [Proposition 5](#prop5) is defined to be the sum of the $$A_i$$, but in fact this is putting the cart before the horse. The reason we think of $$S$$ as the sum of the $$A_i$$ in many areas is not because the set $$S$$ itself has any special meaning, but because of notational convenience. The properties of the sum do not come from the set $$S$$, but from the universal property above.

Therefore, we could simply define it as follows from the start.

<div class="definition" markdown="1">

<ins id="def6-1">**Definition 6$$'$$**</ins> The *sum* of a given family of sets $$(A_i)$$ is a set $$\sum A_i$$ together with maps $$\iota_i:A_i\rightarrow \sum A_i$$ satisfying the following condition:
 
> Whenever a set $$B$$ and maps $$f_i:A_i\rightarrow B$$ are given, there exists a unique function $$f:\sum A_i\rightarrow B$$ such that $$f_i=f\circ\iota_i$$.

![universal_property_of_sum](/assets/images/Math/Set_Theory/Sum_of_Sets-1.png){:style="width:12em" class="invert" .align-center}

</div>

Of course, to use this as a definition we must show that at least one object satisfying the universal property exists. And [Theorem 8](#thm8) does exactly that. 

We mentioned earlier that the set $$\sum A_i$$ is not well-defined in the strict sense. But even if such a set itself is not well-defined, if several such sets are given then there exists a bijection between them. This situation is called *unique up to bijection*. From [Definition 6$$'$$](#def6-1) one can show that the sum of sets is unique up to bijection. 

<div class="proposition" markdown="1">

<ins id="cor9">**Corollary 9**</ins> For a family of sets $$(A_i)$$, the sum $$\sum A_i$$ is unique up to bijection.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Let two sums $$S$$ and $$S'$$ be given, and let $$\iota_i$$ and $$\iota_i'$$ be the injections from $$A_i$$ into $$S$$ and $$S'$$ respectively. First, for the functions $$\iota_i':A_i\rightarrow S'$$, applying the universal property of $$S$$ yields a unique $$\phi':S\rightarrow S'$$ such that $$\iota_i'=\phi'\circ\iota_i$$. Similarly, applying the universal property of $$S'$$ to the functions $$\iota_i$$ yields a unique $$\phi:S'\rightarrow S$$ such that $$\iota_i=\phi\circ\iota_i'$$. Then

$$\iota_i'=\phi'\circ\iota_i=\phi'\circ(\phi\circ\iota_i')=(\phi'\circ\phi)\circ\iota_i'$$

On the other hand, apply the universal property of $$S'$$ to the functions $$\iota_i':A_i\rightarrow S'$$ this time. Then there exists a unique function $$\psi:S'\rightarrow S'$$ satisfying $$\iota_i'=\psi\circ\iota_i'$$. This is obviously satisfied by $$\psi=\id_{S'}$$, so by uniqueness every function $$\psi$$ satisfying this equation equals $$\id_{S'}$$. Therefore $$\phi'\circ\phi=\id_{S'}$$, and since $$\id_{S'}$$ is bijective, $$\phi'$$ is surjective and $$\phi$$ is injective. ([§Retraction and Section, ⁋Proposition 3](/en/math/set_theory/retraction_and_section#prop3))

Likewise, one can show that $$\phi\circ\phi'=\id_S$$, which implies that $$\phi$$ is surjective and $$\phi'$$ is injective. Thus they are both bijections, so there exists a bijection between $$S$$ and $$S'$$. 

</details>


---
**References**

**[Bou]** N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---
