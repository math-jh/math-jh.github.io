---

title: "Unions and Intersections"
excerpt: "Unions and intersections of sets"

categories: [Math / Set Theory]
permalink: /en/math/set_theory/union_and_intersection
header:
    overlay_image: /assets/images/Math/Set_Theory/Union_and_intersection.png
    overlay_filter: 0.5
sidebar: 
    nav: "set_theory-en"

date: 2026-03-06
last_modified_at: 2026-03-06
weight: 8

---

## Family of Sets

Let an index set $$I$$ and a set of sets $$\mathcal{S}$$ be given. Then a function $$f=(F,I,\mathcal{S})$$ from $$I$$ to $$\mathcal{S}$$ assigns to each $$i\in I$$ an element of $$\mathcal{S}$$, that is, a set. We previously agreed to write this as $$(f_i)_{i\in I}$$, but to maintain the convention of denoting sets with capital letters, we will instead write $$(F_i)_{i\in I}$$.

Suppose all sets in the family $$(A_i)_{i\in I}$$ are subsets of some set $$A$$. Then we can take the target of this function $$\mathcal{S}$$ to be $$\mathcal{P}(A)$$. When we wish to view the sets $$A_i$$ as subsets of $$A$$, we express $$(A_i)_{i\in I}$$ as a *family of subsets of set $$A$$*.

## Unions and Intersections

In [§ZFC Axioms](/en/math/set_theory/zfc_axioms), we accepted as an axiom that unions exist. The following notation is more commonly used than the one introduced when we adopted this axiom.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> Let $$(A_i)_{i\in I}$$ be a family of sets. The *union* of this family is the set consisting of <phrase>all $x$ that belong to at least one $A_i$</phrase>, denoted by $$\bigcup_{i\in I}A_i$$.

</div>

In other words, the union is the set of $$x$$ satisfying the logical formula

$$\exists i(i\in I\wedge x\in A_i).$$

Thus if $$I=\emptyset$$, then $$\bigcup_{i\in I} A_i=\emptyset$$. It is not difficult to verify that the union does not depend on the target $$\mathcal{S}$$ of $$(A_i)_{i\in I}$$.

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> Let $$(A_i)_{i\in I}$$ be a family of sets with $$I$$ non-empty. The *intersection* of this family is the set of <phrase>all $x$ that belong to every $A_i$</phrase>, denoted by $$\bigcap_{i\in I}A_i$$.

</div>

The intersection is the collection of $$x$$ satisfying the logical formula

$$\forall i(i\in I\implies x\in A_i).$$

If $$I=\emptyset$$, then $$i\in I$$ becomes false, making the entire statement true regardless of $$x$$, which would imply that $$\bigcap_{i\in\emptyset} A_i$$ must be the universal set—a contradiction. ([§ZFC Axioms, ⁋Example 4](/en/math/set_theory/zfc_axioms#ex4)) By carefully choosing the target $$\mathcal{S}$$ of $$(A_i)_{i\in I}$$, we can avoid this contradiction and define the intersection.

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> Let $$(A_i)_{i\in I}$$ be a family of subsets of a set $$A$$. The *intersection* of this family is the set of <phrase>all $x$ in $A$ that also belong to every $A_i$</phrase>, denoted by $$\bigcap_{i\in I}A_i$$.

</div>

Now, even if $$I=\emptyset$$, the condition becomes

$$(x\in A)\wedge (\forall i(i\in I\implies x\in A_i))$$

so $$\bigcap_{i\in I} A_i=A$$. In all subsequent propositions, whenever we take the intersection of a family of sets, we will assume that either $$I$$ is non-empty or the given family is a family of subsets of some set.

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4**</ins> Consider a family of sets $$(A_i)_{i\in I}$$ and a surjective function $$f:K\rightarrow I$$. Then the following two equations hold:

$$\bigcup_{k\in K}A_{f(k)}=\bigcup_{i\in I}A_i,\qquad \bigcap_{k\in K}A_{f(k)}=\bigcap_{i\in I}A_i$$

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

First, let $$x\in\bigcup_{i\in I} A_i$$. That is, $$x\in A_{i_0}$$ for some $$i_0\in I$$. Since $$f$$ is surjective, there exists $$k_0\in K$$ such that $$i_0=f(k_0)$$, and thus $$x\in A_{f(k_0)}$$, so $$x\in\bigcup_{k\in K}A_{f(k)}$$.

Conversely, if $$x\in\bigcup_{k\in K}A_{f(k)}$$ holds, then $$x\in A_{f(k_0)}$$ for some $$k_0\in K$$. Since $$f(k_0)\in I$$, the set $$A_{f(k_0)}$$ is one of the sets constituting $$(A_i)_{i\in I}$$, and therefore $$x\in \bigcup_{i\in I} A_{i}$$.

Now we must prove the second equation. Let $$x\in\bigcap_{i\in I}A_i$$. Then $$x\in A_i$$ for all $$i\in I$$. For any $$k_0\in K$$, we have $$f(k_0)\in I$$, so $$x\in A_{f(k)}$$ for all $$k\in K$$, and thus $$x\in \bigcap_{k\in K}A_{f(k)}$$.  
Conversely, if $$x\in A_{f(k)}$$ for all $$k\in K$$, then since $$f$$ is surjective, $$x\in A_{f(k)}$$ holds for all $$i\in I$$ as well.

</details>

In particular, suppose $$(A_k)_{k\in K}$$ satisfies $$A_k=A_{k'}$$ for any $$k,k'\in K$$. Choose any $$k_0\in K$$, let $$I=\{k_0\}$$, and apply the above proposition to the surjective function $$f:K\rightarrow I$$. Since $$A_k=A_{k_0}=A_{f(k)}$$ for all $$k$$, we obtain

$$\bigcup_{k\in K} A_k=\bigcup_{k\in K} A_{f(k)}=\bigcup_{i\in I}A_i=A_{k_0},\qquad \bigcap_{k\in K}A_k=\bigcap_{k\in K}A_{f(k)}=\bigcap_{i\in I}A_i=A_{k_0}.$$

Now let us examine further properties of unions and intersections. If two families $$(A_i)_{i\in I}$$ and $$(B_i)_{i\in I}$$ with the same index are given, and $$B_i\subseteq A_i$$ holds for all $$i\in I$$, then

$$\bigcup_{i\in I} B_i\subset\bigcup_{i\in I} A_i,\qquad \bigcap_{i\in I} B_i\subset\bigcap_{i\in I} A_i$$

is immediate. Also, for a given family $$(A_i)_{i\in I}$$ and a subset $$J$$ of $$I$$,

$$\bigcup_{j\in J}A_j\subset\bigcup_{i\in I} A_i,\qquad\bigcap_{j\in J}A_j\supset\bigcap_{i\in I} A_i$$

is also almost immediate.

## Associativity

Set operations satisfy the associative law.

<div class="proposition" markdown="1">

<ins id="def5">**Proposition 5**</ins> Let $$(A_i)_{i\in I}$$ be a family of sets, and suppose the index set $$I$$ is the union of a family $$(J_k)_{k\in K}$$. Then

$$\bigcup_{i\in I} A_i=\bigcup_{k\in K}\left(\bigcup_{j\in J_k} A_j\right),\quad \bigcap_{i\in I}A_i=\bigcap_{k\in K}\left(\bigcap_{j\in J_k} A_j\right)$$

hold.
</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Let us first prove the equation regarding unions. If $$x\in \bigcup_{i\in I}A_i$$, then $$x\in A_{i_0}$$ for some $$i_0\in I$$. Since $$I=\bigcup_{k\in K} J_k$$, there exists $$k_0$$ such that $$i_0\in J_{k_0}$$. Then

$$A_{i_0}=\bigcup_{i\in \{i_0\}}A_i\subset\bigcup_{j\in J_{k_0}} A_j=\bigcup_{k\in\left\{k_0\right\}}\left(\bigcup_{i\in J_k} A_i\right)\subseteq \bigcup_{k\in K}\left(\bigcup_{j\in J_k} A_j\right)$$

so $$x\in A_{i_0}\subseteq \bigcup_{k\in K}\left(\bigcup_{j\in J_k} A_j\right)$$.

Conversely, if $$x\in \bigcup_{k\in K}\left(\bigcup_{j\in J_k} A_j\right)$$, then $$x\in \bigcup_{j\in J_{k_0}}A_j$$ for some $$k_0\in K$$, and thus $$x\in A_{i_0}$$ for some $$i_0\in J_{k_0}$$. Since $$i_0\in I$$, we have $$x\in\bigcup_{i\in I} A_i$$.

The second equation can be proved similarly. If $$x\in\bigcap_{i\in I} A_i$$, then $$x\in A_i$$ for all $$i\in I$$. Since $$J_{k}\subseteq I$$ for any $$k\in K$$, the statement that the above formula holds for all $$i\in I$$ also means that $$x\in A_j$$ holds for all $$j\in J_{k}$$. Since this holds for arbitrarily chosen $$k$$, this precisely means $$x\in\bigcap_{k\in K}\left(\bigcap_{j\in J_{k}}A_j\right)$$.

</details>

## Images of Unions and Intersections

We can also consider the image of a union or intersection as follows.

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6**</ins> Let $$(A_i)_{i\in I}$$ be a family of subsets of a set $$A$$, and let $$(R,A,B)$$ be a binary relation. Then

$$R\left(\bigcup_{i\in I} A_i\right)=\bigcup_{i\in I}R(A_i),\quad R\left(\bigcap_{i\in I} A_i\right)\subset\bigcap_{i\in I}R(A_i)$$

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Let us first prove the first equation. If $$y\in R\left(\bigcup_{i\in I}A_i\right)$$, then there exists $$x\in \bigcup_{i\in I}A_i$$ such that $$(x,y)\in R$$. If $$x\in A_j$$, then $$y\in R(A_j)$$, so $$y\in\bigcup_{i\in I}R\left(A_i\right)$$. Conversely, if $$y\in \bigcup_{i\in I}R\left(A_i\right)$$, then $$y\in R\left(A_j\right)$$ for some $$j$$, so there exists $$x\in A_j$$ such that $$(x,y)\in R$$. Thus $$y\in R\left(\bigcup_{i\in I} A_i\right)$$.

For the second equation, we only need to prove one direction. Let $$y\in R\left(\bigcap_{i\in I}A_i\right)$$. Then there exists $$x\in\bigcap_{i\in I}A_i$$ such that $$(x,y)\in R$$. Since $$x$$ belongs to all $$A_i$$, we know that $$(x,y)\in R(A_i)$$ holds for all $$A_i$$. That is, $$y\in \bigcap_{i\in I}R\left(A_i\right)$$.

</details>

The reverse inclusion in the second equation of the above proposition does not generally hold, but if $$R$$ is the inverse relation of a function, then equality holds.

<div class="proposition" markdown="1">

<ins id="prop7">**Proposition 7**</ins> Let $$f:A\rightarrow B$$ be a function and $$(B_i)_{i\in I}$$ be a family of subsets of $$B$$. Then
  
  $$f^{-1}\left(\bigcap_{i\in I} B_i\right)=\bigcap_{i\in I} f^{-1}(B_i)$$

holds.
</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

Since one inclusion was proved in the more general case, we only need to prove the reverse inclusion.

Let $$x\in\bigcap_{i\in I} f^{-1}(B_i)$$ be arbitrary. Then $$x\in f^{-1}(B_i)$$ for all $$i$$. That is, for all $$i$$, there exists $$y_i\in B_i$$ such that $$(x,y_i)\in F$$. Since $$f$$ is a function, such $$y_i$$ is unique. Let $$y$$ denote this common value. Then $$y\in B_i$$ for all $$i\in I$$, so $$y\in\bigcap_{i\in I} B_i$$, and from $$f(x)=y$$, we have $$x\in f^{-1}\left(\bigcap_{i\in I} B_i\right)$$.

</details>

## De Morgan's Laws

<div class="proposition" markdown="1">

<ins id="prop8">**Proposition 8 (De Morgan's law)**</ins> For a family $$(A_i)_{i\in I}$$ of subsets of a set $$A$$,
  
$$A\setminus \left(\bigcup_{i\in I}A_i\right)=\bigcap_{i\in I}(A\setminus A_i),\quad A\setminus\left(\bigcap_{i\in I} A_i\right)=\bigcup_{i\in I} (A\setminus A_i)$$

hold.
</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

To prove the first equation, let $$x\in A\setminus\left(\bigcup_{i\in I} A_i\right)$$. Then $$x\in A$$ and $$x\not\in\left(\bigcup_{i\in I} A_i\right)$$. Therefore $$x\not\in A_i$$ for all $$i$$, so $$x\in (A\setminus A_i)$$ holds for all $$i$$. That is, $$x\in\bigcap_{i\in I}(A\setminus A_i)$$.  
Conversely, if $$x\in\bigcap_{i\in I} (A\setminus A_i)$$, then $$x\in A\setminus A_i$$ for all $$i\in I$$, and thus $$x\not\in A_i$$ for all $$i\in I$$. Now $$x\not\in\bigcup_{i\in I} A_i$$, so $$x\in A\setminus\bigcup_{i\in I} A_i$$.

The second equation follows immediately from the first, since the equality $$A\setminus(A\setminus X)=X$$ holds for all $$X\subseteq A$$.

</details>


---
**References**

**[Bou]** N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---
