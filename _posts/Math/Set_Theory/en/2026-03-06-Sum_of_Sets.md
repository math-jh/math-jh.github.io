---
title: "Sum of Sets"
description: "This post defines the concepts of covers and partitions of a set, and discusses the refinement relation of covers, images under surjective functions, and the existence conditions for partitions."
excerpt: "Sum of sets (disjoint union)"

categories: [Math / Set Theory]
permalink: /en/math/set_theory/sum_of_sets
sidebar: 
    nav: "set_theory-en"

date: 2021-08-15
weight: 9
translated_at: 2026-06-02T12:30:01+00:00
translation_source: kimi-cli
last_polished_at: 2026-11-01T15:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
## Covering

::: Definition 1
That a family $(A_i)_{i\in I}$ is a *covering* of a set $A$ means that $A=\bigcup_{i\in I} A_i$. For two coverings of $A$, $(A_i)_{i\in I}$ and $(A'_j)_{j\in J}$, that $(A'_j)_{j\in J}$ is *finer* than $(A_i)_{i\in I}$ means that for any $j\in J$, $A'_j\subseteq A_i$ holds for some $i\in I$.
:::

Suppose that for a set $A$, a covering $(A_i)_{i\in I}$ is given. Then for any function $f:B \rightarrow A$, the family of subsets of $B$, $(f^{-1}(A_i))_{i\in I}$, is a covering of $B$. We call this the preimage of $(A_i)$ under $f$. For any function $g:A\rightarrow C$, the family of subsets of $C$, $(g(A_i))_{i\in I}$, need not be a covering of $C$, but if $g$ is a surjection, these cover $C$. We call this the image under the surjection $g$ of $(A_i)$. 


::: Proposition 2
Consider a set $A$ and its covering $(A_i)_{i\in I}$, and choose an arbitrary set $B$.

1. Suppose functions $f,g:A\rightarrow B$ satisfy, whenever any $i\in I$ is given, $f\vert_{A_i}=g\vert_{A_i}$. Then $f=g$. 
2. If a family of functions $(f_i:A_i\rightarrow B)_{i\in I}$ satisfies the condition
    
    $$f_i\vert_{A_i\cap A_j}=f_j\vert_{A_i\cap A_j}$$

    then there exists, extending all $f_i$, a function $f:A\rightarrow B$.
:::

::: Proof
First, to show the first claim, suppose that an arbitrary $x\in A$ is given. Since $(A_i)_{i\in I}$ covers $A$, there exists some $i\in I$ such that $x\in A_i$. Now, since

$$f(x)=(f\vert_{A_i})(x)=(g\vert_{A_i})(x)=g(x)$$

the first claim holds.

For the second claim, using the given functions $f_i=(F_i,A_i,B)$, form $F=\bigcup F_i$, and consider the new triple $f=(F,A,B)$. Then $\pr_1F=A$ is obvious, and thus to show that $f$ is a function, it suffices to show that for any $x\in A$, $(x,y)\in F$ is true for a unique $y$.

Suppose $y,y'\in B$ satisfy $(x,y)\in F$ and $(x,y')\in F$. Then $(x,y)\in F_i$ and $(x,y')\in F_j$ hold for some $i,j$, respectively. Now, since 

$$y=(f_i)(x)=(f_i\vert_{A_i\cap A_j})(x)=(f_j\vert_{A_i\cap A_j})(x)=(f_j)(x)=y'$$

the second claim also holds.
:::

It is obvious by the first claim that the function $f$ satisfying part 2 of the above proposition is unique. Also, if in particular $A_i\cap A_j=\emptyset$ holds whenever $i\neq j$ for all $i,j$, the premise of the second claim is always satisfied. We define this as follows.

::: Definition 3
Sets $A$ and $B$ are *disjoint* if $A\cap B=\emptyset$. More generally, $(A_i)_{i\in I}$ is *pairwise disjoint* if for any $i, j\in I$, $i\neq j$ implies $A_i\cap A_j=\emptyset$.
:::

::: Definition 4
A *partition* of a set $A$ is a pairwise disjoint covering of $A$.
:::

In general, since $\emptyset$ plays no role among the members of this family, when we speak of a partition we assume that all members are non-empty. 

## Sum of Sets

::: Proposition 5
Let $(A_i)_{i\in I}$ be a family of sets. Then there exists a set $S$ such that 

- $S$ is the union of a pairwise disjoint family $(S_i)_{i\in I}$, and 
- for every $i\in I$, there exists a bijection from $A_i$ to $S_i$.
:::
::: Proof
Let $S_i$ be the set formed by taking, for each $x\in A_i$, the pair $(x, i)$. Then $(S_i)_{i\in I}$ is pairwise disjoint. Also, for each $i$, the map $x\mapsto (x,i)$ is a bijection from $A_i$ to $S_i$. Therefore $S=\bigcup_{i\in I} S_i$ satisfies the given conditions.
:::

::: Definition 6
The set $S$ satisfying the above conditions is called the *sum* of the family $(A_i)_{i\in I}$, and is denoted by $\sum_{i\in I} A_i$.
:::

This set is often called the *disjoint union*, and is also written as $\bigsqcup_{i\in I} A_i$. In view of the following proposition, this name also seems quite plausible.

::: Proposition 7
Consider a pairwise disjoint family $(A_i)_{i\in I}$. Let $A$ be their union and $S$ their sum. Then there exists a bijection between $A$ and $S$.
:::
::: Proof
If $f_i:A_i\rightarrow S_i$ are bijections satisfying the conditions of [Proposition 5](#prop5){: data-lid="ci10x" }, then by [Proposition 2](#prop2){: data-lid="badww" } we can extend $(f_i)_{i\in I}$ to $\bigcup_{i\in I} A_i=A$. The function $f:A\rightarrow S$ obtained in this way is injective because each $x\in A$ belongs to a unique $A_i$, $(S_i)_{i\in I}$ is pairwise disjoint, and each $f_i$ is injective; and it is surjective because $S=\bigcup_{i\in I} S_i$ and each $f_i$ is surjective onto $S_i$.
:::

The intuition for why this is called the sum of sets will appear later. ([§Operations on Cardinals, ⁋Definition 1](/en/math/set_theory/operation_of_cardinals#def1){: data-lid="4w61m" })

## Universal property

There is something we did not mention in [Definition 6](#def6){: data-lid="3dyzo" }. The sum $S$ of a family of sets $(A_i)$ is not unique. There are infinitely many sets satisfying the conditions of [Proposition 5](#prop5){: data-lid="tv6c6" }. For example, in the proof of that proposition we took $S$ to be the set of pairs $(x,i)$, but one can see that taking the set of pairs $(i,x)$ also satisfies the definition of sum. Therefore, strictly speaking, writing the sum of the $A_i$ as $\sum A_i$ is not a well-defined expression.

First, let us examine the *universal property* of the sum as follows.

::: Theorem 8 (Universal property of sum)
Let a family of sets $(A_i)$, the set $S$ defined in [Proposition 5](#prop5){: data-lid="42b2o" }, and, obtained by composing the bijections $A_i\rightarrow S_i$ of the same proposition with the inclusion relations $S_i\subseteq S$, the functions $\iota_i:A_i\rightarrow S$ be given. Then, whenever another set $B$ and maps $f_i:A_i\rightarrow B$ are given, there exists a unique corresponding $f:S\rightarrow B$ such that $f_i=f\circ\iota_i$ holds. 
:::
::: Proof
First, let us show that such a function $f$ is unique (if it exists). For this, it suffices to show that for any $x\in S$, its function value $f(x)$ is always uniquely determined. Since $S$ is the union of the pairwise disjoint family $(S_i)$, there exists a unique $i\in I$ such that $x\in S_i$. Then since $\iota_i:A_i\rightarrow S_i$ is a bijection, there again exists a unique element $x_i$ of $A_i$ such that $\iota_i(x_i)=x$. Now,

$$f(x)=f(\iota_i(x_i))=(f\circ\iota_i)(x_i)=f_i(x_i)$$

so at $x$, the function value $f(x)$ must equal $f_i(x_i)$, and therefore $f$ is uniquely determined.

Now, taking a hint from the uniqueness proof, let us show the existence of the function $f$. It suffices to *define* $f(x)$ to be $f_i(x_i)$ as in the above equation, and prove that $f$ is actually a function. For instance, with this definition $f$ will be defined for all elements of $S$, and a single $x$ specifies only one function value as discussed above.
:::


In many cases the set $S$ appearing in the proof of [Proposition 5](#prop5){: data-lid="cm7az" } is defined to be the sum of the $A_i$, but in fact this definition puts the cart before the horse. The reason we think of $S$ as the sum of the $A_i$ in many areas is not because the set $S$ itself has any special meaning, but because of notational convenience. The properties of the sum do not come from the set $S$, but from the universal property above.

Therefore, we could simply define it as follows from the start.

::: definition Definition 6$'$ {#def6-1}
The *sum* of a given family of sets $(A_i)$ is, satisfying the following condition:
 
> Whenever an arbitrary set $B$ and $f_i:A_i\rightarrow B$ are given, there exists a unique function $f:\sum A_i\rightarrow B$ such that $f_i=f\circ\iota_i$ holds.

{% diagram Math/Set_Theory/Sum_of_Sets-1.svg width="13.49em" alt="universal_property_of_sum" %}

a collection of a set $\sum A_i$ and maps $\iota_i:A_i\rightarrow \sum A_i$.
:::

Of course, to use this as a definition we must show that at least one object satisfying the universal property exists. And [Theorem 8](#thm8){: data-lid="jqxjl" } plays exactly that role. 

We mentioned earlier that the set $\sum A_i$ is not well-defined in the strict sense. But even if such a set itself is not well-defined, if several such sets are given then there exists a bijection between them. This situation is called *unique up to bijection*. From [Definition 6$'$](#def6-1){: data-lid="3tabr" } one can show that the sum of sets is unique up to bijection.

::: Corollary 9
For a family of sets $(A_i)$, the sum $\sum A_i$ is unique up to bijection.
:::
::: Proof
Let two sums $S$ and $S'$ be given, and let $\iota_i$ and $\iota_i'$ be the functions from $A_i$ into $S$ and $S'$, respectively. First, for the functions $\iota_i':A_i\rightarrow S'$, applying the universal property of $S$ yields a unique $\phi':S\rightarrow S'$ such that $\iota_i'=\phi'\circ\iota_i$. Similarly, applying the universal property of $S'$ to the functions $\iota_i$, once again there exists a unique $\phi:S'\rightarrow S$ such that $\iota_i=\phi\circ\iota_i'$. Then

$$\iota_i'=\phi'\circ\iota_i=\phi'\circ(\phi\circ\iota_i')=(\phi'\circ\phi)\circ\iota_i'$$

On the other hand, let us apply the universal property of $S'$ to the functions $\iota_i':A_i\rightarrow S'$ this time. Then there exists a unique function $\psi:S'\rightarrow S'$ satisfying $\iota_i'=\psi\circ\iota_i'$. Since this equation is obviously satisfied by $\psi=\id_{S'}$, by uniqueness every function $\psi$ satisfying this equation equals $\id_{S'}$. Therefore $\phi'\circ\phi=\id_{S'}$, and since $\id_{S'}$ is bijective, $\phi'$ is surjective and $\phi$ is injective. ([§Retraction and Section, ⁋Proposition 3](/en/math/set_theory/retraction_and_section#prop3){: data-lid="dc4gm" })

Likewise, one can show that $\phi\circ\phi'=\id_S$, which implies that $\phi$ is surjective and $\phi'$ is injective. That is, since each of them is a bijection, there exists a bijection between $S$ and $S'$. 
:::


---
**References**

**[Bou]** N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---
