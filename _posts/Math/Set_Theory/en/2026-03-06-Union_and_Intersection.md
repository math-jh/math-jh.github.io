---
title: "Union and Intersection"
description: "This post rigorously defines the union and intersection of a family of sets within the ZFC axiomatic system, and proves a property of the intersection using surjective functions."
excerpt: "Union and intersection of sets"

categories: [Math / Set Theory]
permalink: /en/math/set_theory/union_and_intersection
sidebar: 
    nav: "set_theory-en"

date: 2021-08-15
weight: 8
translated_at: 2026-06-02T13:00:03+00:00
translation_source: kimi-cli
last_polished_at: 2026-11-01T19:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
## Family of sets

Let an index set $I$ and a set of sets $\mathcal{S}$ be given. Then a function $f=(F,I,\mathcal{S})$ from $I$ to $\mathcal{S}$ assigns to each $i\in I$ an element of $\mathcal{S}$, i.e., a set. We previously agreed to write this as $(f_i)_{i\in I}$, but to maintain the convention of writing sets with capital letters, we shall write it as $(F_i)_{i\in I}$.

Suppose every set in a family $(A_i)_{i\in I}$ is a subset of some set $A$. Then we may take the target $\mathcal{S}$ of this function to be $\mathcal{P}(A)$. When we wish to regard the sets $A_i$ as subsets of $A$ in this way, we express $(A_i)_{i\in I}$ as a *family of subsets of the set $A$*.

## Union and intersection

In [§ZFC Axioms](/en/math/set_theory/zfc_axioms){: data-lid="lumof" }, we accepted as an axiom that unions exist. The following notation is used somewhat more frequently than the notation we employed when introducing that axiom.

::: Definition 1
Let $(A_i)_{i\in I}$ be a family of sets. Then, collecting all elements belonging to at least one $A_i$, the set of all such $x$ is called the *union* of this family, and is written $\bigcup_{i\in I}A_i$.
:::

That is, the union is given by the logical formula

$$\exists i(i\in I\wedge x\in A_i)$$

as the set of $x$ satisfying it. Therefore, if $I=\emptyset$, then $\bigcup_{i\in I} A_i=\emptyset$. It is not difficult to verify that, for $(A_i)_{i\in I}$, the union does not depend on the target $\mathcal{S}$.

::: Definition 2
Let $(A_i)_{i\in I}$ be a family of sets, and suppose $I$ is not empty. Then, collecting all elements belonging to every $A_i$, the set of all such $x$ is called the *intersection* of this family, and is written $\bigcap_{i\in I}A_i$.
:::

The intersection is given by the logical formula

$$\forall i(i\in I\implies x\in A_i)$$

as the collection of $x$ satisfying it. If $I=\emptyset$, then $i\in I$ is false, so the entire statement is true regardless of $x$, and $\bigcap_{i\in\emptyset} A_i$ would have to be the universal set, which is a contradiction. ([§ZFC Axioms, ⁋Example 4](/en/math/set_theory/zfc_axioms#ex4){: data-lid="qcd9n" }) If, for $(A_i)_{i\in I}$, we specify the target $\mathcal{S}$ appropriately, we can define the intersection while avoiding this contradiction.

::: Definition 3
Let a family of sets $(A_i)_{i\in I}$ be a family of subsets of a set $A$. Then, among elements of $A$ that simultaneously belong to every $A_i$, the set of all such $x$ is called the *intersection* of this family, and is written $\bigcap_{i\in I}A_i$.
:::

This time, even if $I=\emptyset$, the condition becomes

$$(x\in A)\wedge (\forall i(i\in I\implies x\in A_i))$$

so that $\bigcap_{i\in I} A_i=A$. Henceforth, in all propositions, whenever we take the intersection of a family of sets, we assume either that $I$ is nonempty or that the given family is a family of subsets of some set.

::: Proposition 4
Consider a family of sets $(A_i)_{i\in I}$ and a surjective function $f:K\rightarrow I$. Then the following two equalities

$$\bigcup_{k\in K}A_{f(k)}=\bigcup_{i\in I}A_i,\qquad \bigcap_{k\in K}A_{f(k)}=\bigcap_{i\in I}A_i$$

hold.
:::

::: Proof
First, let $x\in\bigcup_{i\in I} A_i$. That is, for some $i_0\in I$ we have $x\in A_{i_0}$. But since $f$ is a surjective function, there exists some $k_0\in K$ such that $i_0=f(k_0)$, and therefore $x\in A_{f(k_0)}$, so $x\in\bigcup_{k\in K}A_{f(k)}$.  

Conversely, if $x\in\bigcup_{k\in K}A_{f(k)}$ holds, then for some $k_0\in K$ we have $x\in A_{f(k_0)}$. But since $f(k_0)\in I$, $A_{f(k_0)}$ is one of the sets constituting $(A_i)_{i\in I}$, and therefore $x\in \bigcup_{i\in I} A_{i}$.

We must now show the second equality. First, let $x\in\bigcap_{i\in I}A_i$. Then for every $i\in I$ we have $x\in A_i$. Since for any $k_0\in K$ we have $f(k_0)\in I$, for every $k\in K$ we have $x\in A_{f(k)}$, and therefore $x\in \bigcap_{k\in K}A_{f(k)}$.  
Conversely, if for every $k\in K$ we have $x\in A_{f(k)}$, then since $f$ is surjective, for every $i\in I$ we also have $x\in A_i$.
:::

In particular, suppose $(A_k)_{k\in K}$ satisfies that for any $k,k'\in K$, $A_k=A_{k'}$. If we choose any $k_0\in K$, let $I=\{k_0\}$, and apply the proposition above to the surjective function $f:K\rightarrow I$, then since for every $k$ we have $A_k=A_{k_0}=A_{f(k)}$,

$$\bigcup_{k\in K} A_k=\bigcup_{k\in K} A_{f(k)}=\bigcup_{i\in I}A_i=A_{k_0},\qquad \bigcap_{k\in K}A_k=\bigcap_{k\in K}A_{f(k)}=\bigcap_{i\in I}A_i=A_{k_0}$$

holds.

Let us now examine a few more properties of unions and intersections. If two families $(A_i)_{i\in I}$ and $(B_i)_{i\in I}$ with the same index set are given, and $B_i\subseteq A_i$ holds for every $i\in I$, then

$$\bigcup_{i\in I} B_i\subseteq\bigcup_{i\in I} A_i,\qquad \bigcap_{i\in I} B_i\subseteq\bigcap_{i\in I} A_i$$

is obvious. Also, for a given family $(A_i)_{i\in I}$ and a subset of $I$, $J$,

$$\bigcup_{j\in J}A_j\subseteq\bigcup_{i\in I} A_i,\qquad\bigcap_{j\in J}A_j\supset\bigcap_{i\in I} A_i$$

is almost obvious. 

## Associativity

The operations on sets are associative.

::: Proposition 5
 Let $(A_i)_{i\in I}$ be a family of sets, and suppose the index set $I$ is the union of a family $(J_k)_{k\in K}$. Then

$$\bigcup_{i\in I} A_i=\bigcup_{k\in K}\left(\bigcup_{j\in J_k} A_j\right),\quad \bigcap_{i\in I}A_i=\bigcap_{k\in K}\left(\bigcap_{j\in J_k} A_j\right)$$

holds.
:::
::: Proof
First, let us show the equality for unions. If $x\in \bigcup_{i\in I}A_i$, then for some $i_0\in I$ we have $x\in A_{i_0}$. Now, since $I=\bigcup_{k\in K} J_k$, there exists some $k_0$ such that $i_0\in J_{k_0}$. Then, since

$$A_{i_0}=\bigcup_{i\in \{i_0\}}A_i\subseteq\bigcup_{j\in J_{k_0}} A_j=\bigcup_{k\in\left\{k_0\right\}}\left(\bigcup_{i\in J_k} A_i\right)\subseteq \bigcup_{k\in K}\left(\bigcup_{j\in J_k} A_j\right)$$

we have $x\in A_{i_0}\subseteq \bigcup_{k\in K}\left(\bigcup_{j\in J_k} A_j\right)$.  

Conversely, if $x\in \bigcup_{k\in K}\left(\bigcup_{j\in J_k} A_j\right)$, then for some $k_0\in K$ we have $x\in \bigcup_{j\in J_{k_0}}A_j$, and thus for some $i_0\in J_{k_0}$ we have $x\in A_{i_0}$. Now since $i_0\in I$, we have $x\in\bigcup_{i\in I} A_i$. 

Similarly, the second equality can also be shown. If $x\in\bigcap_{i\in I} A_i$, then for every $i\in I$ we have $x\in A_i$. Since for any $k\in K$ we have $J_{k}\subseteq I$, the statement that the above holds for every $i\in I$ also means that for every $j\in J_{k}$ we have $x\in A_j$. Since this holds for an arbitrarily chosen $k$, this means precisely that $x\in\bigcap_{k\in K}\left(\bigcap_{j\in J_{k}}A_j\right)$. Conversely, if $x\in\bigcap_{k\in K}\left(\bigcap_{j\in J_{k}}A_j\right)$ and $i\in I$, then since $I=\bigcup_{k\in K} J_k$, for some $k\in K$ we have $i\in J_k$, and therefore $x\in A_i$. That is, $x\in\bigcap_{i\in I}A_i$.
:::

## Image of a union or intersection

We may also consider the image of a union or intersection as follows.

::: Proposition 6
 Let $(A_i)_{i\in I}$ be a family of subsets of a set $A$, and let $(R,A,B)$ be a binary relation. Then

$$R\left(\bigcup_{i\in I} A_i\right)=\bigcup_{i\in I}R(A_i),\quad R\left(\bigcap_{i\in I} A_i\right)\subseteq\bigcap_{i\in I}R(A_i)$$

hold.
:::
::: Proof
First, let us show the first equality. If $y\in R\left(\bigcup_{i\in I}A_i\right)$, then there exists some $x\in \bigcup_{i\in I}A_i$ such that $(x,y)\in R$. Now if $x\in A_j$, then $y\in R(A_j)$, so $y\in\bigcup_{i\in I}R\left(A_i\right)$ holds. Conversely, if $y\in \bigcup_{i\in I}R\left(A_i\right)$, then $y\in R\left(A_j\right)$ for some $j$, so there exists some $x\in A_j$ such that $(x,y)\in R$. Therefore, $y\in R\left(\bigcup_{i\in I} A_i\right)$ holds.

For the second formula, it suffices to show only one direction. Suppose $y\in R\left(\bigcap_{i\in I}A_i\right)$. Then there exists some $x\in\bigcap_{i\in I}A_i$ such that $(x,y)\in R$. Since $x$ belongs to every $A_i$, we know that $y\in R(A_i)$ holds for all $i\in I$. That is, $y\in \bigcap_{i\in I}R\left(A_i\right)$.
:::

The reverse inclusion in the second formula of the proposition above does not hold in general, but if $R$ is the inverse relation of a function, then equality holds.

::: Proposition 7
 Let $f:A\rightarrow B$ be a function, and let $(B_i)_{i\in I}$ be a family of subsets of $B$. Then
  
  $$f^{-1}\left(\bigcap_{i\in I} B_i\right)=\bigcap_{i\in I} f^{-1}(B_i)$$

holds. 
:::

::: Proof
Since one inclusion was proved in the more general case, it suffices to prove only the reverse inclusion.

Suppose an arbitrary $x\in\bigcap_{i\in I} f^{-1}(B_i)$ is given. Then $x\in f^{-1}(B_i)$ for every $i$. That is, for every $i$ there exists $y_i\in B_i$ such that $(x,y_i)\in F$. However, since $f$ is a function, such a $y_i$ is unique. Letting this common value be $y$, we have $y\in B_i$ for all $i\in I$, and thus $y\in\bigcap_{i\in I} B_i$; therefore, from $f(x)=y$, we obtain $x\in f^{-1}\left(\bigcap_{i\in I} B_i\right)$.
:::

## De Morgan's laws

::: Proposition 8 (De Morgan's law)
For a set $A$ and a family $(A_i)_{i\in I}$ of its subsets, 
  
$$A\setminus \left(\bigcup_{i\in I}A_i\right)=\bigcap_{i\in I}(A\setminus A_i),\quad A\setminus\left(\bigcap_{i\in I} A_i\right)=\bigcup_{i\in I} (A\setminus A_i)$$

hold.
:::

::: Proof
To show the first equality, suppose first that $x\in A\setminus\left(\bigcup_{i\in I} A_i\right)$. Then $x\in A$ and $x\not\in\left(\bigcup_{i\in I} A_i\right)$. Hence $x\not\in A_i$ for all $i$, so $x\in (A\setminus A_i)$ holds for all $i$. That is, $x\in\bigcap_{i\in I}(A\setminus A_i)$.  
Conversely, if $x\in\bigcap_{i\in I} (A\setminus A_i)$, then for any $i\in I$ we have $x\in A\setminus A_i$, and therefore $x\not\in A_i$ for all $i\in I$. Now since $x\not\in\bigcup_{i\in I} A_i$, we have $x\in A\setminus\bigcup_{i\in I} A_i$.

The second equality is obvious from the first, since the equality $A\setminus(A\setminus X)=X$ holds for all $X\subseteq A$.
:::


---
**References**

**[Bou]** N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---
