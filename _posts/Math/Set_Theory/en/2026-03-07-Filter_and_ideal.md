---

title: "Filters, Ideals, and Galois Connections"
excerpt: "Filter and ideal"

categories: [Math / Set Theory]
permalink: /en/math/set_theory/filter_and_ideal
header:
    overlay_image: /assets/images/Math/Set_Theory/Filter_and_ideal.png
    overlay_filter: 0.5
sidebar: 
    nav: "set_theory-en"

date: 2026-03-07
last_modified_at: 2026-03-07
weight: 18

---

This article gathers topics that are scattered throughout **[Bou]** along with some topics not covered there, combining them into a single post.

## Filter and Ideal

First, let us define the following two concepts.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> For an ordered set $$A$$, a subset $$X\subseteq A$$ is a *lower set* (resp. *upper set*) if whenever $$y\in A$$ satisfies $$y\leq x$$ (resp. $$x\leq y$$) for some $$x\in X$$, then $$y\in X$$.

A non-empty right directed lower set is called an *ideal*, and a non-empty left directed upper set is called a *filter*.

</div>

The set $$E$$ itself is both a filter and an ideal. Filters and ideals distinct from $$E$$ are called proper.

<div class="example" markdown="1">

<ins id="ex2">**Example 2**</ins> Let an ordered set $$A$$ be given. For any $$x\in A$$, the *downward closure*[^1]

$$\downarrow x=\{y\in A\mid y\leq x\}$$

is an ideal of $$A$$. Such an ideal is called a *principal ideal*.

Similarly, the *upward closure*

$$\uparrow x=\{y\in A\mid y\geq x\}$$

is a filter of $$A$$, and such a filter is called a *principal filter*.

</div>

We are mostly interested in cases where $$A$$ is a lattice. In this case, ([§Directed Sets, ⁋Definition 4](/en/math/set_theory/directed_set#def4))

- A non-empty lower set $$I$$ is an ideal if and only if for any $$x,y\in I$$, we have $$x\vee y\in I$$.
- A non-empty upper set $$F$$ is a filter if and only if for any $$x,y\in F$$, we have $$x\wedge y\in F$$.

<div class="example" markdown="1">

<ins id="ex3">**Example 3**</ins> Let a set $$A$$ be given. When the natural order relation $$\subseteq$$ is given to $$\mathcal{P}(A)$$, it becomes a lattice, and in particular, for any $$X,Y\in\mathcal{P}(A)$$,

$$X\vee Y=X\cup Y,\qquad X\wedge Y=X\cap Y$$

holds. In $$\mathcal{P}(A)$$, the two operations $$\vee$$ and $$\wedge$$ additionally satisfy the following distributive laws:

$$X\vee(Y\wedge Z)=(X\vee Y)\wedge(X\vee Z),\qquad X\wedge(Y\vee Z)=(X\wedge Y)\vee(X\wedge Z)$$

</div>

<div class="definition" markdown="1">

<ins id="def4">**Definition 4**</ins> Let a lattice $$A$$ be given, and let $$I$$ and $$F$$ be a proper ideal and a proper filter of $$E$$, respectively. $$I$$ is a *prime ideal* if for any $$x,y\in A$$, if $$x\wedge y\in I$$, then either $$x\in I$$ or $$y\in I$$ holds. Similarly, $$F$$ is a *prime filter* if for any $$x,y\in A$$, if $$x\vee y\in F$$, then either $$x\in F$$ or $$y\in F$$ holds. ([\[Algebraic Structures\] §Field of Fractions, ⁋Proposition 8](/en/math/algebraic_structures/field_of_fractions#prop8))

</div>

Alternatively, defining $$I$$ to be a prime ideal by requiring that $$A\setminus I$$ be a filter yields an equivalent definition.

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> Let a lattice $$A$$ be given in which the distributive law between the two operations $$\vee$$ and $$\wedge$$ holds. Then every maximal ideal is a prime ideal, and every maximal filter is a prime filter.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Let $$I$$ be a maximal ideal, and suppose $$x\wedge y\in I$$. Assume, for contradiction, that $$x,y\not\in I$$. Define a new set $$J$$ as the set of all $$z$$ such that $$x\wedge z\in I$$.

1. If $$z_1,z_2\in J$$, then $$x\wedge (z_1\vee z_2)=(x\wedge z_1)\vee(x\wedge z_2)\in I$$ holds, so $$z_1\vee z_2\in J$$.
2. If $$z\in J$$ and $$z'\leq z$$, then $$z'\in J$$. Since $$(x\wedge z')\vee (x\wedge z)=x\wedge (z'\vee z)=x\wedge z$$, we have $$x\wedge z'\leq x\wedge z$$, and since $$x\wedge z\in I$$, we must have $$x\wedge z'$$ also be an element of $$I$$.
3. In particular, it is clear that $$x\not\in J$$ and $$y\in J$$.

Therefore, $$J$$ is a proper ideal strictly containing $$I$$, which contradicts the maximality of $$I$$. Similarly, we can show that every maximal filter is prime.

</details>


Maximal filters are also called *ultrafilters*.


For two ordered sets $$A,B$$, consider an increasing function $$f:A\rightarrow B$$. Also, let $$Y$$ be any lower set of $$B$$ and let $$X=f^{-1}(Y)$$. If for some $$y\in A$$ there exists $$x\in X$$ such that $$y\leq x$$, then $$f(y)\leq f(x)$$, and since $$Y$$ is a lower set, $$f(y)\in Y$$ holds, so $$y\in X$$. That is, the preimage of a lower set is also a lower set.

## Galois Connection

The Galois connection we are about to introduce, as the name suggests, originates from Galois theory on field extensions. However, it can be abstracted as a relation between two ordered sets, and this abstraction proves useful in many areas.

<div class="definition" markdown="1">

<ins id="def6">**Definition 6**</ins> Let two ordered sets $$A$$ and $$B$$ be given.

1. Let two increasing functions $$F:A\rightarrow B$$ and $$G:B\rightarrow A$$ satisfy the condition

    $$F(a)\leq b\iff a\leq G(b)$$

    for all $$a\in A$$ and $$b\in B$$. Then $$F$$ is called the *lower adjoint* of $$G$$, $$G$$ is called the *upper adjoint* of $$F$$, and the pair $$(F,G)$$ is called a *monotone Galois connection* between $$A$$ and $$B$$.
2. Let two decreasing functions $$F:A\rightarrow B$$ and $$G:B\rightarrow A$$ satisfy the condition

    $$b\leq F(a)\iff a\leq G(b)$$

    for all $$a\in A$$ and $$b\in B$$. Then $$F$$ and $$G$$ are each called a *polarity*, and the pair $$(F,G)$$ is called an *antitone Galois connection* between $$A$$ and $$B$$.
</div>

In either case, the function $$G\circ F:A\rightarrow A$$ always satisfies $$a\leq G(F(a))$$. For a monotone Galois connection,

$$a\leq G(F(a))\iff F(a)\leq F(a)$$

where the latter is always true, and similarly for an antitone Galois connection. On the other hand, $$F\circ G$$ depends on whether the Galois connection is monotone or antitone. For a monotone Galois connection,

$$F(G(b))\leq b\iff G(b)\leq G(b)$$

where the latter is always true, so $$F(G(b))\leq b$$ holds. For an antitone Galois connection,

$$b\leq F(G(b))\iff G(b)\leq G(b)$$

so $$b\leq F(G(b))$$ always holds.

Meanwhile, $$G\circ F$$ and $$F\circ G$$ are compositions of two increasing functions or two decreasing functions, so in either case, they must be increasing functions.

In the remainder of this article, for convenience, we will abbreviate $$G\circ F$$ and $$F\circ G$$ as $$GF$$ and $$FG$$, respectively.

<div class="proposition" markdown="1">

<ins id="prop7">**Proposition 7**</ins> Let two ordered sets $$A,B$$ be given with a monotone Galois connection $$F:A\rightarrow B$$ and $$G:B\rightarrow A$$ between them. For any $$y\in B$$, $$GFG(y)=G(y)$$ always holds.

If these form an antitone Galois connection, then for all $$x\in A$$ and $$y\in B$$, both $$GFG(y)=G(y)$$ and $$FGF(x)=F(x)$$ hold.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, substituting $$a=G(y)$$ into $$a\leq GF(a)$$ gives $$G(y)\leq GFG(y)$$. On the other hand, we have shown that $$FG$$ satisfies $$FG(b)\leq b$$ for all $$b\in B$$, and since $$G$$ is an increasing function, we also obtain $$GFG(y)\leq G(y)$$. Therefore, $$GFG(y)=G(y)$$ holds.

On the other hand, in the case where the pair $$(F,G)$$ is an antitone Galois connection, $$G(y)\leq GFG(y)$$ can be shown in the same way as above. Also, since $$b\leq FG(b)$$ always holds for all $$b\in B$$, and $$G$$ is a decreasing function, $$G(y)\geq GFG(y)$$ again holds, so $$GFG(y)=G(y)$$. The equality $$FGF(x)=F(x)$$ is easily proved by swapping the roles of $$F$$ and $$G$$.

</details>

The following definition is used not only in topology but also importantly in lattice theory.

<div class="definition" markdown="1">

<ins id="def8">**Definition 8**</ins> For an ordered set $$A$$, a function $$f:A\rightarrow A$$ is a *closure operator* if the following three conditions are all satisfied:

1. For all $$x\in A$$, $$x\leq f(x)$$ holds.
2. For all $$x\in A$$, $$f(x)=f(f(x))$$.
3. If $$x\leq y$$, then $$f(x)\leq f(y)$$.

In this case, $$x$$ is *closed* if $$f(x)=x$$.

</div>

Let us fix an antitone Galois connection. From the result $$GFG(y)=G(y)$$ in [Proposition 7](#prop7), substituting $$y=F(x)$$ for any $$x\in A$$ gives

$$GFGF(x)=GF(x)$$

Thus the function $$GF$$ satisfies all the conditions above and is therefore a closure operator. Similarly, in an antitone Galois connection, $$FG$$ also becomes a closure operator.

By definition, $$x$$ and $$y$$ being closed with respect to $$GF$$ and $$FG$$ respectively means that $$GF(x)=x$$ and $$FG(y)=y$$ hold. From [Proposition 7](#prop7), we know that all elements in the images of $$F$$ and $$G$$ are closed. Conversely, if an arbitrary element $$x$$ is closed with respect to $$GF$$, then from $$GF(x)=x$$ we know that $$x$$ belongs to the image of $$G$$, and a similar statement for $$FG$$ can also be proved.

Through this process, for a Galois connection between ordered sets $$A$$ and $$B$$, we can construct collections $$A'\subseteq A$$ and $$B'\subseteq B$$ of closed subsets, and the restrictions of $$F$$ and $$G$$ to these collections are well-defined. Moreover, these $$F\vert_{A'}$$ and $$G\vert_{B'}$$ are bijections and become *anti-isomorphisms*. These are specifically called *Galois correspondences*.


---
**References**

**[Bou]** N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.
**[Wikipedia]** [Galois connection](https://en.wikipedia.org/wiki/Galois_connection)

---

[^1]: An upper set is also called an *upward closed set*, and a lower set is also called a *downward closed set*.
