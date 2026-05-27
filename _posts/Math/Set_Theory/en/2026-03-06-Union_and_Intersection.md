---
title: "Union and Intersection"
excerpt: "Union and intersection of sets"

categories: [Math / Set Theory]
permalink: /en/math/set_theory/union_and_intersection
header:
    overlay_image: /assets/images/Math/Set_Theory/Union_and_Intersection.png
    overlay_filter: 0.5
sidebar: 
    nav: "set_theory-en"

date: 2021-08-15
last_modified_at: 2022-11-24
weight: 8
translated_at: 2026-05-27T00:30:03+00:00
translation_source: kimi-cli
---
## Family of sets

Let an index set $$I$$ and a set of sets $$\mathcal{S}$$ be given. Then a function $$f=(F,I,\mathcal{S})$$ from $$I$$ to $$\mathcal{S}$$ assigns to each $$i\in I$$ an element of $$\mathcal{S}$$, i.e., a set. Previously we agreed to write this as $$(f_i)_{i\in I}$$, but to maintain the convention of writing sets with capital letters, we shall write it as $$(F_i)_{i\in I}$$.

Suppose every set in the family $$(A_i)_{i\in I}$$ is a subset of some set $$A$$. Then we may take the target $$\mathcal{S}$$ of this function to be $$\mathcal{P}(A)$$. When we wish to regard the sets $$A_i$$ as subsets of $$A$$ in this way, we say that $$(A_i)_{i\in I}$$ is a *family of subsets of the set $$A$$*.

## Union and intersection

In [§ZFC Axioms](/en/math/set_theory/zfc_axioms) we accepted as an axiom that unions exist. The following notation is used somewhat more frequently than the notation we employed when introducing that axiom.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> Let $$(A_i)_{i\in I}$$ be a family of sets. Then the set of all $$x$$ that <phrase>belong to at least one $$A_i$$</phrase> is called the *union* of this family, and is written $$\bigcup_{i\in I}A_i$$.

</div>

Thus the union is the set of all $$x$$ satisfying the logical formula

$$\exists i(i\in I\wedge x\in A_i)$$

Hence if $$I=\emptyset$$, then $$\bigcup_{i\in I} A_i=\emptyset$$. It is not difficult to verify that the union does not depend on the target $$\mathcal{S}$$ of $$(A_i)_{i\in I}$$.

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> Let $$(A_i)_{i\in I}$$ be a family of sets, and suppose $$I$$ is not empty. Then the set of all $$x$$ that <phrase>belong to every $$A_i$$</phrase> is called the *intersection* of this family, and is written $$\bigcap_{i\in I}A_i$$.

</div>

The intersection is the collection of all $$x$$ satisfying the logical formula

$$\forall i(i\in I\implies x\in A_i)$$

If $$I=\emptyset$$, then $$i\in I$$ is false, so the entire statement is true regardless of $$x$$, and $$\bigcap_{i\in\emptyset} A_i$$ would have to be the universal set, which is a contradiction. ([§ZFC Axioms, ⁋Example 4](/en/math/set_theory/zfc_axioms#ex4)) If we specify the target $$\mathcal{S}$$ of $$(A_i)_{i\in I}$$ appropriately, we can define the intersection while avoiding this contradiction.

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> Let $$(A_i)_{i\in I}$$ be a family of subsets of a set $$A$$. Then the set of all $$x$$ that <phrase>are elements of $$A$$ and simultaneously belong to every $$A_i$$</phrase> is called the *intersection* of this family, and is written $$\bigcap_{i\in I}A_i$$.

</div>

This time, even if $$I=\emptyset$$, the condition becomes

$$(x\in A)\wedge (\forall i(i\in I\implies x\in A_i))$$

so that $$\bigcap_{i\in I} A_i=A$$. Henceforth, whenever we take the intersection of a family of sets in any proposition, we assume either that $$I$$ is nonempty or that the given family is a family of subsets of some set.

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4**</ins> Consider a family of sets $$(A_i)_{i\in I}$$ and a surjective function $$f:K\rightarrow I$$. Then the two equalities

$$\bigcup_{k\in K}A_{f(k)}=\bigcup_{i\in I}A_i,\qquad \bigcap_{k\in K}A_{f(k)}=\bigcap_{i\in I}A_i$$

hold.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

First suppose $$x\in\bigcup_{i\in I} A_i$$. That is, for some $$i_0\in I$$ we have $$x\in A_{i_0}$$. Since $$f$$ is surjective, there exists some $$k_0\in K$$ such that $$i_0=f(k_0)$$, and therefore $$x\in A_{f(k_0)}$$, so $$x\in\bigcup_{k\in K}A_{f(k)}$$.

Conversely, if $$x\in\bigcup_{k\in K}A_{f(k)}$$ holds, then for some $$k_0\in K$$ we have $$x\in A_{f(k_0)}$$. Since $$f(k_0)\in I$$, the set $$A_{f(k_0)}$$ is one of the sets constituting $$(A_i)_{i\in I}$$, and therefore $$x\in \bigcup_{i\in I} A_{i}$$.

We must now show the second equality. First suppose $$x\in\bigcap_{i\in I}A_i$$. Then $$x\in A_i$$ for every $$i\in I$$. For arbitrary $$k_0\in K$$ we have $$f(k_0)\in I$$, so $$x\in A_{f(k)}$$ for every $$k\in K$$, and therefore $$x\in \bigcap_{k\in K}A_{f(k)}$$.
Conversely, if $$x\in A_{f(k)}$$ for every $$k\in K$$, then since $$f$$ is surjective, $$x\in A_{f(k)}$$ also holds for every $$i\in I$$.

</details>

In particular, suppose $$(A_k)_{k\in K}$$ satisfies $$A_k=A_{k'}$$ for arbitrary $$k,k'\in K$$. Choose any $$k_0\in K$$, let $$I=\{k_0\}$$, and apply the above proposition to the surjective function $$f:K\rightarrow I$$; then since $$A_k=A_{k_0}=A_{f(k)}$$ for every $$k$$,

$$\bigcup_{k\in K} A_k=\bigcup_{k\in K} A_{f(k)}=\bigcup_{i\in I}A_i=A_{k_0},\qquad \bigcap_{k\in K}A_k=\bigcap_{k\in K}A_{f(k)}=\bigcap_{i\in I}A_i=A_{k_0}$$

hold.

Let us now examine a few more properties of unions and intersections. If two families $$(A_i)_{i\in I}$$ and $$(B_i)_{i\in I}$$ with the same index set are given, and $$B_i\subseteq A_i$$ holds for every $$i\in I$$, then

$$\bigcup_{i\in I} B_i\subset\bigcup_{i\in I} A_i,\qquad \bigcap_{i\in I} B_i\subset\bigcap_{i\in I} A_i$$

is obvious. Also, for a given family $$(A_i)_{i\in I}$$ and a subset $$J$$ of $$I$$,

$$\bigcup_{j\in J}A_j\subset\bigcup_{i\in I} A_i,\qquad\bigcap_{j\in J}A_j\supset\bigcap_{i\in I} A_i$$

is almost obvious.

## Associativity

The operations on sets satisfy associativity.

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins>  Let $$(A_i)_{i\in I}$$ be a family of sets, and suppose the index set $$I$$ is the union of a family $$(J_k)_{k\in K}$$. Then

$$\bigcup_{i\in I} A_i=\bigcup_{k\in K}\left(\bigcup_{j\in J_k} A_j\right),\quad \bigcap_{i\in I}A_i=\bigcap_{k\in K}\left(\bigcap_{j\in J_k} A_j\right)$$

hold.
</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Let us first prove the equality for unions. If $$x\in \bigcup_{i\in I}A_i$$, then for some $$i_0\in I$$ we have $$x\in A_{i_0}$$. Since $$I=\bigcup_{k\in K} J_k$$, there exists some $$k_0$$ such that $$i_0\in J_{k_0}$$. Then

$$A_{i_0}=\bigcup_{i\in \{i_0\}}A_i\subset\bigcup_{j\in J_{k_0}} A_j=\bigcup_{k\in\left\{k_0\right\}}\left(\bigcup_{i\in J_k} A_i\right)\subseteq \bigcup_{k\in K}\left(\bigcup_{j\in J_k} A_j\right)$$

so $$x\in A_{i_0}\subseteq \bigcup_{k\in K}\left(\bigcup_{j\in J_k} A_j\right)$$.

Conversely, if $$x\in \bigcup_{k\in K}\left(\bigcup_{j\in J_k} A_j\right)$$, then for some $$k_0\in K$$ we have $$x\in \bigcup_{j\in J_{k_0}}A_j$$, and thus for some $$i_0\in J_{k_0}$$ we have $$x\in A_{i_0}$$. Since $$i_0\in I$$, we obtain $$x\in\bigcup_{i\in I} A_i$$.

The second equality can be proved similarly. If $$x\in\bigcap_{i\in I} A_i$$, then $$x\in A_i$$ for every $$i\in I$$. For arbitrary $$k\in K$$ we have $$J_{k}\subseteq I$$, so the statement that the above holds for every $$i\in I$$ is equivalent to the statement that $$x\in A_j$$ holds for every $$j\in J_{k}$$. Since this holds for arbitrarily chosen $$k$$, this means exactly that $$x\in\bigcap_{k\in K}\left(\bigcap_{j\in J_{k}}A_j\right)$$.

</details>

## Image of a union or intersection

We may also consider the image of a union or intersection as follows.

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6**</ins>  Let $$(A_i)_{i\in I}$$ be a family of subsets of a set $$A$$, and let $$(R,A,B)$$ be a binary relation. Then

$$R\left(\bigcup_{i\in I} A_i\right)=\bigcup_{i\in I}R(A_i),\quad R\left(\bigcap_{i\in I} A_i\right)\subset\bigcap_{i\in I}R(A_i)$$

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Let us first prove the first equality. If $$y\in R\left(\bigcup_{i\in I}A_i\right)$$, then there exists suitable $$x\in \bigcup_{i\in I}A_i$$ such that $$(x,y)\in R$$. Now if $$x\in A_j$$, then $$y\in R(A_j)$$, so $$y\in\bigcup_{i\in I}R\left(A_i\right)$$ holds. Conversely, if $$y\in \bigcup_{i\in I}R\left(A_i\right)$$, then for some $$j$$ we have $$y\in R\left(A_j\right)$$, so there exists suitable $$x\in A_j$$ such that $$(x,y)\in R$$. Therefore $$y\in R\left(\bigcup_{i\in I} A_i\right)$$ holds.

For the second equality it suffices to show one inclusion. Suppose $$y\in R\left(\bigcap_{i\in I}A_i\right)$$. Then there exists some $$x\in\bigcap_{i\in I}A_i$$ such that $$(x,y)\in R$$. Since $$x$$ belongs to every $$A_i$$, we know that $$(x,y)\in R(A_i)$$ holds for every $$A_i$$. That is, $$y\in \bigcap_{i\in I}R\left(A_i\right)$$.

</details>

The reverse inclusion in the second equality of the above proposition does not hold in general, but if $$R$$ is the inverse relation of a function, then equality holds.

<div class="proposition" markdown="1">

<ins id="prop7">**Proposition 7**</ins>  Let $$f:A\rightarrow B$$ be a function, and let $$(B_i)_{i\in I}$$ be a family of subsets of $$B$$. Then
  
  $$f^{-1}\left(\bigcap_{i\in I} B_i\right)=\bigcap_{i\in I} f^{-1}(B_i)$$

holds. 
</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

One inclusion was proved in the more general case, so it suffices to prove the reverse inclusion.

Suppose arbitrary $$x\in\bigcap_{i\in I} f^{-1}(B_i)$$ is given. Then $$x\in f^{-1}(B_i)$$ for every $$i$$. That is, for every $$i$$ there exists $$y_i\in B_i$$ such that $$(x,y_i)\in F$$. Since $$f$$ is a function, such $$y_i$$ is unique. Let this common value be $$y$$; then $$y\in B_i$$ for every $$i\in I$$, so $$y\in\bigcap_{i\in I} B_i$$, and therefore from $$f(x)=y$$ we obtain $$x\in f^{-1}\left(\bigcap_{i\in I} B_i\right)$$.

</details>

## De Morgan's laws

<div class="proposition" markdown="1">

<ins id="prop8">**Proposition 8 (De Morgan's law)**</ins> For a family $$(A_i)_{i\in I}$$ of subsets of a set $$A$$,
  
$$A\setminus \left(\bigcup_{i\in I}A_i\right)=\bigcap_{i\in I}(A\setminus A_i),\quad A\setminus\left(\bigcap_{i\in I} A_i\right)=\bigcup_{i\in I} (A\setminus A_i)$$

hold.
</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

To prove the first equality, suppose first $$x\in A\setminus\left(\bigcup_{i\in I} A_i\right)$$. Then $$x\in A$$ and $$x\not\in\left(\bigcup_{i\in I} A_i\right)$$. Hence $$x\not\in A_i$$ for every $$i$$, so $$x\in (A\setminus A_i)$$ holds for every $$i$$. That is, $$x\in\bigcap_{i\in I}(A\setminus A_i)$$.
Conversely, if $$x\in\bigcap_{i\in I} (A\setminus A_i)$$, then for arbitrary $$i\in I$$ we have $$x\in A\setminus A_i$$, and therefore $$x\not\in A_i$$ for every $$i\in I$$. Now since $$x\not\in\bigcup_{i\in I} A_i$$, we have $$x\in A\setminus\bigcup_{i\in I} A_i$$.

The second equality is obvious from the first, since the equality $$A\setminus(A\setminus X)=X$$ holds for every $$X\subseteq A$$.

</details>


---
**References**

**[Bou]** N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---
