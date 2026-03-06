---

title: "Sum of Sets"
excerpt: "Sum of Sets (Disjoint Union)"

categories: [Math / Set Theory]
permalink: /en/math/set_theory/sum_of_sets
header:
    overlay_image: /assets/images/Math/Set_Theory/Sum_of_sets.png
    overlay_filter: 0.5
sidebar: 
    nav: "set_theory-en"

date: 2026-03-06
last_modified_at: 2026-03-06
weight: 9

---

## Covering

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> A family $(A\_i)\_{i\in I}$ is a *covering* of a set $A$ if $A=\bigcup\_{i\in I} A\_i$. Given two coverings $(A\_i)\_{i\in I}$ and $(A'\_j)\_{j\in J}$ of $A$, the covering $(A'_j)\_{j\in J}$ is *finer* than $(A_i)\_{i\in I}$ if for every $j\in J$, there exists $i\in I$ such that $A'\_j\subseteq A\_i$.

</div>

Let $(A\_i)\_{i\in I}$ be a covering of a set $A$. For any function $f:B \rightarrow A$, the family $(f^{-1}(A\_i))\_{i\in I}$ of subsets of $B$ is a covering of $B$. This is called the *preimage* of $(A\_i)$ under $f$. For any function $g:A\rightarrow C$, the family $(g(A\_i))\_{i\in I}$ of subsets of $C$ need not be a covering of $C$, but if $g$ is surjective, then these sets cover $C$. This is called the *image* of $(A\_i)$ under the surjection $g$.


<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins>  Let $A$ be a set with covering $(A_i)\_{i\in I}$, and let $B$ be any set.

1. Suppose functions $f,g:A\rightarrow B$ satisfy $f\|_{A\_i}=g\|_{A\_i}$ for every $i\in I$. Then $f=g$.
2. Let $(f\_i:A\_i\rightarrow B)\_{i\in I}$ be a family of functions satisfying the condition
    
    $$f_i|_{A_i\cap A_j}=f_j|_{A_i\cap A_j}$$

    Then there exists a function $f:A\rightarrow B$ extending all $f_i$.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

For the first claim, let $x\in A$ be given. Since $(A_i)\_{i\in I}$ covers $A$, there exists $i\in I$ with $x\in A_i$. Then

$$f(x)=(f|_{A_i})(x)=(g|_{A_i})(x)=g(x)$$

which establishes the first claim.

For the second claim, using the given functions $f\_i=(F\_i,A\_i,B)$, form $F=\bigcup F\_i$ and consider the triple $f=(F,A,B)$. Clearly $\pr\_1F=A$, so to show that $f$ is a function, it suffices to prove that for any $x\in A$, there is a unique $y$ such that $(x,y)\in F$.

Let $y,y'\in B$ satisfy $(x,y)\in F$ and $(x,y')\in F$. Then there exist $i$ and $j$ such that $(x,y)\in F\_i$ and $(x,y')\in F\_j$. Now

$$y=(f_i)(x)=(f_i|_{A_i\cap A_j})(x)=(f_j|_{A_i\cap A_j})(x)=(f_j)(x)=y'$$

so the second claim is also established.

</details>

By the first claim, the function $f$ satisfying the condition in part 2 is necessarily unique. Moreover, if $A\_i\cap A\_j=\emptyset$ for all $i,j$, then the hypothesis of part 2 is automatically satisfied. We make the following definition.

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> Sets $A$ and $B$ are *disjoint* if $A\cap B=\emptyset$. More generally, a family $(A_i)\_{i\in I}$ is *pairwise disjoint* if for any $i, j\in I$ with $i\neq j$, we have $A_i\cap A_j=\emptyset$.

</div>

<div class="definition" markdown="1">

<ins id="def4">**Definition 4**</ins> A *partition* of a set $A$ is a pairwise disjoint covering of $A$.

</div>

In general, the empty set plays no role among the members of such a family, so when we speak of a partition, we assume that no member is empty.

## Sum of Sets

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> Let $(A_i)\_{i\in I}$ be a family of sets. Then there exists a set $S$ such that:

- $S$ is the union of a pairwise disjoint family $(S\_i)\_{i\in I}$, and
- for every $i\in I$, there exists a bijection from $A_i$ to $S_i$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Let $S_i$ be <phrase>the set of all $(x, i)$ satisfying $x\in A_i$</phrase>. Then $(S_i)\_{i\in I}$ is pairwise disjoint. For each $i$, the map $x\mapsto (x,i)$ is a bijection from $A_i$ to $S_i$. Hence $S=\bigcup\_{i\in I} S_i$ satisfies the required conditions.

</details>

<div class="definition" markdown="1">

<ins id="def6">**Definition 6**</ins> A set $S$ satisfying the conditions above is called the *sum* of the family $(A_i)\_{i\in I}$ and is denoted by $\sum\_{i\in I} A_i$.

</div>

This set is often called the *disjoint union* and denoted by $\bigsqcup_{i\in I} A_i$. The following proposition shows that this terminology is apt.

<div class="proposition" markdown="1">

<ins id="prop7">**Proposition 7**</ins> Let $(A_i)\_{i\in I}$ be a pairwise disjoint family. If $A$ denotes their union and $S$ their sum, then there exists a bijection between $A$ and $S$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

If $f_i:A_i\rightarrow S_i$ are the bijections satisfying the condition of [Proposition 5](#prop5), then by [Proposition 2](#prop2), the family $(f_i)\_{i\in I}$ extends to a bijection from $\bigcup\_{i\in I} A_i=A$.

</details>

The intuition for calling this the sum of sets will emerge later. ([§Cardinals, ⁋Definition 6](/en/math/set_theory/cardinals#def6))

## Universal Property

There is a point we have not yet mentioned regarding [Definition 6](#def6). The sum $X$ of a family of sets $(A_i)$ is not unique: infinitely many sets satisfy the conditions of [Proposition 5](#prop5). For instance, in the proof of that proposition, we took $S$ to be the set of pairs $(x,i)$, but we could equally well have taken the set of pairs $(i,x)$. Strictly speaking, then, the notation $\sum A_i$ for the sum of the $A_i$ is not well-defined.

Let us first examine the *universal property* of the sum.

<div class="proposition" markdown="1">

<ins id="thm8">**Theorem 8 (Universal property of sum)**</ins> Let $(A_i)$ be a family of sets, let $S$ be the set defined in [Proposition 5](#prop5), and let $\iota_i:A_i\rightarrow S$ be the injections. Given another set $B$ and functions $f_i:A_i\rightarrow B$, there exists a unique function $f:S\rightarrow B$ such that $f_i=f\circ\iota_i$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

We first show that such a function $f$, if it exists, is unique. It suffices to show that for any $x\in S$, the value $f(x)$ is uniquely determined. Since $S$ is the union of a pairwise disjoint family $(S_i)$, there exists a unique $i\in I$ with $x\in S_i$. As $\iota_i:A_i\rightarrow S_i$ is a bijection, there exists a unique $x_i\in A_i$ with $\iota_i(x_i)=x$. Now

$$f(x)=f(\iota_i(x_i))=(f\circ\iota_i)(x_i)=f_i(x_i)$$

so the value $f(x)$ at $x$ must equal $f_i(x_i)$, and hence $f$ is uniquely determined.

For existence, taking a cue from the uniqueness proof, we *define* $f(x)$ to be $f_i(x_i)$ as above, and verify that $f$ is indeed a function. With this definition, $f$ is defined on all elements of $S$, and each $x$ is assigned exactly one value, as argued above.

</details>


In many contexts, the set $S$ from the proof of [Proposition 5](#prop5) is taken as the definition of the sum of the $A_i$, but this is actually putting the cart before the horse. The reason we regard $S$ as the sum of the $A_i$ in many fields is notational convenience, not because the set $S$ itself has special significance. The properties of the sum do not derive from the set $S$, but from the universal property above.

Thus we might instead adopt the following definition from the start.

<div class="definition" markdown="1">

<ins id="def6-1">**Definition 6$'$**</ins> The *sum* of a given family of sets $(A_i)$ is a set $\sum A_i$ together with injections $\iota_i:A_i\rightarrow \sum A_i$ satisfying the following condition:
 
> For any set $B$ and functions $f_i:A_i\rightarrow B$, there exists a unique function $f:\sum A_i\rightarrow B$ such that $f_i=f\circ\iota_i$.

![universal_property_of_sum](/assets/images/Math/Set_Theory/Sum_of_sets-1.png){:style="width:12em" class="invert" .align-center}

</div>

To use this as a definition, we must of course show that at least one object satisfying the universal property exists. [Theorem 8](#thm8) provides precisely this.

We mentioned earlier that the set $\sum A_i$ is not strictly well-defined. However, even though such a set is not uniquely defined, any two such sets are in bijection. We say that such an object is *unique up to bijection*. From [Definition 6$'$](#def6-1), we can show that the sum of sets is unique up to bijection.

<div class="proposition" markdown="1">

<ins id="cor9">**Corollary 9**</ins> For a family of sets $(A_i)$, the sum $\sum A_i$ is unique up to bijection.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Suppose two sums $S$ and $S'$ are given, with injections $\iota_i$ and $\iota_i'$ from $A_i$ to $S$ and $S'$ respectively. Applying the universal property of $S$ to the functions $\iota_i':A_i\rightarrow Y$, we obtain a unique $\phi':S\rightarrow S'$ such that $\iota_i'=\phi'\circ\iota_i$. Similarly, applying the universal property of $S'$ to the functions $\iota_i$, we obtain a unique $\phi:S'\rightarrow S$ such that $\iota_i=\phi\circ\iota_i'$. Then

$$\iota_i'=\phi'\circ\iota_i=\phi'\circ(\phi\circ\iota_i')=(\phi'\circ\phi)\circ\iota_i'$$

Now apply the universal property of $S'$ to the functions $\iota_i':A_i\rightarrow S'$. There exists a unique function $\psi:S'\rightarrow S'$ such that $\iota_i'=\psi\circ\iota_i'$. This is of course satisfied by $\psi=\id\_{S'}$, so by uniqueness, any such $\psi$ equals $\id\_{S'}$. Hence $\phi'\circ\phi=\id\_{S'}$, and since $\id\_{S'}$ is a bijection, $\phi'$ is surjective and $\phi$ is injective. ([§Retraction and Section, ⁋Proposition 3](/en/math/set_theory/retraction_and_section#prop3))

Similarly, we can show that $\phi\circ\phi'=\id\_S$, from which it follows that $\phi$ is surjective and $\phi'$ is injective. Thus each is a bijection, and there exists a bijection between $S$ and $S'$.

</details>


---
**References**

**[Bou]** N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---
