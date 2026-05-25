---
title: "Dimension"
excerpt: "Definitions of covering dimension and Krull dimension for algebraic geometry"

categories: [Math / Topology]
permalink: /en/math/topology/dimension
header:
    overlay_image: /assets/images/Math/Topology/Dimension.png
    overlay_filter: 0.5
sidebar: 
    nav: "topology-en"

date: 2024-12-15
last_modified_at: 2024-12-15
weight: 19
translated_at: 2026-05-23T08:30:01+00:00
translation_source: kimi-cli
---
In this post we define the dimension of a topological space. First we define the dimension in common use, and then we separately define the notion of dimension used in [algebraic geometry](/en/algebraic_varieties/).

## Covering dimension

For convenience, following **[Mun]** we define the dimension only for compact spaces in this section. The basic idea is to measure how many times a point of $$X$$ is covered by open sets; of course, since $$X$$ is covered by just the single open set $$X$$, we must define this using arbitrary open coverings, and if we give an open covering haphazardly we can cover a single point by as many open sets as we wish, so we must guarantee some kind of minimality.

First we define the following.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> A family $$(U_i)_{i\in I}$$ of subsets of $$X$$ is said to have *order* $$m+1$$ if no point of $$X$$ belongs to $$m+1$$ or more of the $$U_i$$, and some point of $$X$$ belongs to exactly $$m+1$$ of the $$U_i$$.

</div>

Then we can define the dimension of a space $$X$$ as follows.

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> A space $$X$$ is called *finite dimensional* if there exists an $$m$$ such that, for every open covering $$(U_i)_{i\in I}$$, there always exists an open refinement $$(V_j)_{j\in J}$$ of $$(U_i)$$ of order $$m+1$$. We define the smallest such $$m$$ to be the *dimension* of $$X$$, and write $$\dim X$$.

</div>

One somewhat noteworthy point is that topological spaces can look quite strange, as in the figure below, and in this case we have defined the dimension of this topological space to be the larger of the dimensions of the two components.

img

Meanwhile, there are several properties we expect of dimension, and some of them are as follows.

<div class="proposition" markdown="1">

<ins id="prop3">**Proposition 3**</ins> If $$X$$ is a finite dimensional topological space and $$Y$$ is a closed subspace of $$X$$, then $$Y$$ is also finite dimensional and $$\dim Y\leq\dim X$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Suppose $$X$$ is a $$d$$-dimensional topological space and let $$\{V_j\}$$ be an arbitrary open covering of $$Y$$. Then for each $$V_j$$ there exists an open subset $$U_j$$ of $$X$$ such that $$V_j=U_j\cap Y$$. Now $$X$$ can be covered by the $$U_j$$ and $$X\setminus Y$$. Then there exists a refinement of this covering of order $$\leq d+1$$, and intersecting it again with $$Y$$ yields a refinement of $$\{V_j\}$$ of order $$\leq d+1$$.

</details>

The following proposition is a more mathematically refined version of the caveat mentioned after [Definition 2](#def2).

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4**</ins> If there exist two finite dimensional closed subspaces $$Y,Z$$ of a topological space $$X$$ such that $$X=Y\cup Z$$, then $$\dim X=\max(\dim Y,\dim Z)$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>



</details>

And of course we wish that $$\mathbb{R}^n$$ has dimension $$n$$. However, showing this is not easy, basically because at present it is even hard to show that $$\mathbb{R}^n$$ and $$\mathbb{R}^m$$ are not homeomorphic. Instead, the following weaker proposition can be easily seen from the definition.

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> Any compact subspace of $$\mathbb{R}^n$$ is always at most $$n$$-dimensional.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>



</details>

## Krull dimension

On the other hand, we will define the notion of dimension used in algebraic geometry; since the spaces of interest in algebraic geometry are equipped with a topological structure different from the usual one, this definition is somewhat non-intuitive. In particular, $$\mathbb{R}^n$$ with its ordinary topology is always $$0$$-dimensional. However, it is nevertheless true that this definition can be phrased in the language of topology, so we record it here as well.

<div class="definition" markdown="1">

<ins id="def6">**Definition 6**</ins> A topological space $$X$$ is called *irreducible* if there do not exist proper closed subsets $$A,B$$ of $$X$$ such that $$X=A\cup B$$.

</div>

Then the following are all equivalent.

<div class="proposition" markdown="1">

<ins id="prop7">**Proposition 7**</ins> For a topological space $$X$$, the following are all equivalent.

1. $$X$$ is irreducible.
2. For any nonempty open sets $$U,V$$ of $$X$$, $$U\cap V\neq\emptyset$$.
3. For any nonempty open set $$U$$ of $$X$$, $$\cl U=X$$.
4. Every open set of $$X$$ is connected.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

The equivalence of the first and second conditions is obvious by considering complements, and the equivalence of the second and third conditions is obvious by considering $$X\setminus \cl U$$ and $$U$$. Finally, the second and fourth conditions are equivalent by definition.

</details>

In particular, an irreducible space is not Hausdorff. Because of the last equivalence in the above proposition, an irreducible space is also called a *hyperconnected space*. In a similar vein, the following holds. (See: [§Connected Spaces, ⁋Proposition 3](/en/math/topology/connected_spaces#prop3))

<div class="proposition" markdown="1">

<ins id="prop8">**Proposition 8**</ins> Suppose $$X$$ is a union of irreducible open subsets

$$X=\bigcup_{i\in I} U_i$$

and that $$U_i\cap U_j\neq \emptyset$$ holds for all $$i,j$$. Then $$X$$ is irreducible.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Let arbitrary open sets $$V, W$$ be given; we show that $$V\cap W\neq\emptyset$$. Then by the given assumption there first exist $$i,j$$ satisfying $$U_i\cap V\neq\emptyset$$ and $$U_j\cap W\neq\emptyset$$. Now by the third condition of [Proposition 7](#prop7) and [§Subspaces, ⁋Proposition 5](/en/math/topology/subspaces#prop5), $$U_i$$ is also irreducible, so the two nonempty subsets $$U_i\cap V$$ and $$U_i\cap U_j$$ of $$U_i$$ must have a nonempty intersection. That is,

$$(U_i\cap V)\cap (U_i\cap U_j)=U_i\cap U_j\cap V\neq\emptyset$$

and, viewing $$U_i\cap U_j\cap V$$ as a nonempty subset of $$U_j$$, likewise from the irreducibility of $$U_j$$ we obtain the formula

$$(U_i\cap U_j\cap V)\cap (U_j\cap W)=U_i\cap U_j\cap V\cap W\neq\emptyset$$

and in particular $$V\cap W\neq\emptyset$$.

</details>

Just as with connected components, we can define the following.

<div class="definition" markdown="1">

<ins id="def9">**Definition 9**</ins> For a subset $$A$$ of a topological space $$X$$, the *irreducible component* containing $$A$$ means the largest irreducible subset containing $$A$$.

</div>

Then by an argument similar to [§Connected Spaces, ⁋Proposition 2](/en/math/topology/connected_spaces), one can show that the closure of an irreducible set is irreducible, so an irreducible component is necessarily a closed subset.

<div class="definition" markdown="1">

<ins id="def10">**Definition 10**</ins> For a topological space $$X$$, we define the *length* of a strictly descending chain of irreducible closed subsets of $$X$$

$$A_n\supsetneq\cdots\supsetneq A_0$$

to be $$n$$. Then we define the *Krull dimension* of $$X$$ by the formula

$$\dim X=\sup\{\text{length of strictly descending chains of irreducible closed subsets}\}$$

If there exists a strictly descending chain of infinite length, we define $$\dim X=\infty$$, and if $$X=\emptyset$$ we define $$\dim X=-\infty$$.

</div>

Then the Krull dimension of $$X$$ is always finite in the following situation. In particular, in a Hausdorff space only singletons are irreducible subsets, so the Krull dimension of a Hausdorff space is $$0$$.

<div class="definition" markdown="1">

<ins id="def11">**Definition 11**</ins> A topological space $$X$$ is called *noetherian* if, whenever a chain of closed sets

$$A_1\supseteq A_2\supseteq\cdots$$

is given, there exists an $$n$$ such that $$A_n=A_{n+1}=\cdots$$.

</div>

The Noetherian condition gives a strong finiteness condition. For instance, the following holds.

<div class="proposition" markdown="1">

<ins id="prop12">**Proposition 12**</ins> A Noetherian space is compact.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Assume a Noetherian space $$X$$ and an open covering $$\{U_i\}_{i\in I}$$ of $$X$$ are given. Then we can define

$$\mathcal{C}=\left\{\bigcup_{j\in J} U_j:\text{$J$ finite subset of $I$}\right\}.$$

Now if we consider any totally ordered subset of $$\mathcal{C}$$, this is equivalent to a descending chain of closed sets formed by their complements, and therefore by the assumption that $$X$$ is noetherian this must eventually stop. That is, $$\mathcal{C}$$ satisfies the condition of [[Set Theory] §Axiom of Choice, ⁋Theorem 4](/en/math/set_theory/axiom_of_choice#thm4) and hence $$\mathcal{C}$$ has a maximal element $$U\in \mathcal{C}$$. If $$X\neq U$$, we can choose a $$U_j$$ containing $$x\in X\setminus U$$, and then $$U\cap U_j$$ is an element of $$\mathcal{C}$$ that strictly contains $$U$$, contradicting the maximality of $$U$$. Therefore $$U=X$$ and we obtain the desired result.

</details>

Additionally, the following holds for Noetherian spaces.

<div class="proposition" markdown="1">

<ins id="prop13">**Proposition 13**</ins> For a Noetherian topological space $$X$$, the following hold.

1. Any subspace of $$X$$ is noetherian.
2. $$X$$ has finitely many irreducible components.
3. Each irreducible component of $$X$$ contains a nonempty open set of $$X$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

1. Let an arbitrary subspace $$Y$$ of $$X$$ be given, and suppose a descending chain of closed sets of $$Y$$
    
    $$A_1\supseteq A_2\supseteq \cdots$$

    is given. Then there exist closed sets $$A_i'$$ of $$X$$ satisfying $$A_i=A_i'\cap Y$$. Now if we let $$B_i=A_1'\cap\cdots\cap A_i'$$, then $$B_i\cap Y=A_i$$ and the $$B_i$$ form a descending chain of closed sets of $$X$$.
2. Let $$\mathcal{C}$$ be the collection of closed sets of $$X$$ that cannot be expressed as a union of finitely many irreducible components. Then it suffices to show that $$\mathcal{C}=\emptyset$$. Assuming for contradiction that $$\mathcal{C}$$ is not empty, by the same method as in the proof of [Proposition 12](#prop12) we know that $$\mathcal{C}$$ has a minimal element $$A$$. Now since $$A$$ is not irreducible, it can be written as $$A=B_1\cup B_2$$ for two closed sets $$B_1,B_2$$, and by the assumption that $$B_1,B_2\not\in \mathcal{C}$$ each of them has finitely many irreducible components. Through a brief calculation we can use these irreducible decompositions to find a finite irreducible decomposition of $$A=B_1\cup B_2$$, which is a contradiction; hence $$\mathcal{C}=\emptyset$$.
3. Suppose $$X=A_1\cup\cdots\cup A_n$$ is an irreducible decomposition; then considering $$X\setminus (A_2\cup\cdots\cup A_n)$$, this set is a nonempty open set of $$X$$ contained in $$A_1$$.

</details>

Then if $$X$$ is noetherian, there exists an irreducible decomposition of $$X$$

$$X=\bigcup_{i=1}^r X_i$$

and the $$X_i$$ are all closed sets; since the complement of each $$X_i$$ is also a finite union of closed sets, each $$X_i$$ is also an open set.

<div class="proposition" markdown="1">

<ins id="prop14">**Proposition 14**</ins> For a topological space $$X$$ and an open set $$U$$, there exists a one-to-one correspondence between the irreducible closed subsets of $$X$$ meeting $$U$$ and the irreducible closed subsets of $$U$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, suppose an irreducible subspace $$Z$$ of $$X$$ satisfying $$U\cap Z\neq\emptyset$$ is given; we must show that any two nonempty open subsets of $$Z\cap U$$ are not disjoint. Since any subset of $$Z\cap U$$ is of the form $$V_1\cap U$$, $$V_2\cap U$$ for open sets $$V_1, V_2$$ of $$Z$$, from the formula

$$(V_1\cap U)\cap (V_2\cap U)=(V_1\cap V_2)\cap U$$

if $$(V_1\cap U)\cap(V_2\cap U)\neq\emptyset$$ then $$V_1\cap V_2\neq\emptyset$$, contradicting the assumption that $$Z$$ is irreducible.

Conversely, suppose an irreducible closed subset $$Y\subseteq U$$ of $$U$$ is given; then the closure of $$Y$$ is also irreducible, so $$\cl_X(Y)$$ is an irreducible subset of $$X$$ meeting $$U$$. That is, from this we obtain two maps

$$\{\text{irreducible closes subset of $X$ meeting $U$}\}\rightarrow \{\text{irreducible closed subset of $U$}\};\qquad Z\mapsto Z\cap U$$

and

$$\{\text{irreducible closed subset of $U$}\} \rightarrow \{\text{irreducible closes subset of $X$ meeting $U$}\};\qquad Y\mapsto \cl_X(Y)$$

and we can verify that these are mutually inverse bijections.

</details>

Moreover, since the two maps in the above proof are inclusion-preserving, there exists a one-to-one correspondence between the irreducible components of $$X$$ meeting $$U$$ and the irreducible components of $$U$$.

We now show the following proposition.

<div class="proposition" markdown="1">

<ins id="prop15">**Proposition 15**</ins> If there exist two finite dimensional closed subspaces $$Y,Z$$ of a topological space $$X$$ such that $$X=Y\cup Z$$, then their Krull dimensions also satisfy the formula $$\dim X=\max(\dim Y,\dim Z)$$.

</div>
