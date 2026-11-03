---
title: "Filters, Ideals, and Galois Connections"
description: "We define the notions of filters and ideals in ordered sets and lattices, and examine the properties of principal filters, principal ideals, and prime ideals."
excerpt: "Filters and ideals"

categories: [Math / Set Theory]
permalink: /en/math/set_theory/filter_and_ideal
sidebar: 
    nav: "set_theory-en"

date: 2022-05-01
weight: 18
translated_at: 2026-06-02T18:30:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-11-03T19:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
This article gathers topics scattered throughout **[Bou]** along with topics not covered there, combining them into a single post.

## Filter and ideal

First, we define the following two concepts.

::: Definition 1
For an ordered set $A$, a subset $X\subseteq A$ is a *lower set* (resp. *upper set*) if whenever $y\in A$ satisfies $y\leq x$ (resp. $x\leq y$) for some $x\in X$, then $y\in X$.

A nonempty right directed lower set is called an *ideal*, and a nonempty left directed upper set is called a *filter*.
:::

If $A$ is nonempty, right directed, and left directed, then $A$ itself is both a filter and an ideal. Filters and ideals other than $A$ are called proper.

::: Example 2
Let an ordered set $A$ be given. For any $x\in A$, the *downward closure*[^1] of $x$

$$\downarrow x=\{y\in A\mid y\leq x\}$$

is an ideal of $A$. Such an ideal is called a *principal ideal*.

Of course, similarly, the *upward closure* of $x$

$$\uparrow x=\{y\in A\mid y\geq x\}$$

is a filter of $A$, and such a filter is called a *principal filter*.
:::

We are mostly interested in the case where $A$ is a lattice. In this case, ([§Directed Sets, ⁋Definition 4](/en/math/set_theory/directed_set#def4){: data-lid="hmj9a" })

- A nonempty lower set $I$ is an ideal if and only if $x\vee y\in I$ for all $x,y\in I$.
- A nonempty upper set $F$ is a filter if and only if $x\wedge y\in F$ for all $x,y\in F$.

::: Example 3
Let a set $A$ be given. Then endowing $\mathcal{P}(A)$ with the natural order relation $\subseteq$ makes $\mathcal{P}(A)$ a lattice, and in particular, for any $X,Y\in\mathcal{P}(A)$,

$$X\vee Y=X\cup Y,\qquad X\wedge Y=X\cap Y$$

holds. In $\mathcal{P}(A)$, the two operations $\vee$ and $\wedge$ additionally satisfy the following distributive laws:

$$X\vee(Y\wedge Z)=(X\vee Y)\wedge(X\vee Z),\qquad X\wedge(Y\vee Z)=(X\wedge Y)\vee(X\wedge Z)$$
:::

::: Definition 4
Let a lattice $A$ be given, and let $I$ and $F$ be a proper ideal and a proper filter of $A$, respectively. $I$ is a *prime ideal* if for any $x,y\in A$, whenever $x\wedge y\in I$, then either $x\in I$ or $y\in I$. Similarly, $F$ is a *prime filter* if for any $x,y\in A$, whenever $x\vee y\in F$, then either $x\in F$ or $y\in F$. ([\[Algebraic Structures\] §Field of Fractions, ⁋Proposition 9](/en/math/algebraic_structures/field_of_fractions#prop9){: data-lid="545p8" })
:::

Equivalently, one may define $I$ to be a prime ideal by requiring that $A\setminus I$ be a filter.

::: Proposition 5
Let a lattice $A$ be given in which the distributive law between the two operations $\vee$ and $\wedge$ holds. Then every maximal ideal is a prime ideal, and every maximal filter is a prime filter.
:::
::: Proof
For a maximal ideal $I$, let $x\wedge y\in I$. Assume, for contradiction, that $x,y\not\in I$, and let $J$ be the set of all $z$ such that $x\wedge z\in I$.

1. If $z_1,z_2\in J$, then $x\wedge (z_1\vee z_2)=(x\wedge z_1)\vee(x\wedge z_2)\in I$, so $z_1\vee z_2\in J$.
2. If $z\in J$ and $z'\leq z$, then $z'\in J$. This is because $(x\wedge z')\vee (x\wedge z)=x\wedge (z'\vee z)=x\wedge z$ implies $x\wedge z'\leq x\wedge z$, and since $x\wedge z\in I$, $x\wedge z'$ must also be an element of $I$.
3. For any $z\in I$, since $x\wedge z\leq z$ and $I$ is a lower set, $x\wedge z\in I$, that is, $z\in J$. Therefore, $I\subseteq J$. In particular, it is clear that $x\not\in J$ and $y\in J$.

Therefore, $J$ is a proper ideal strictly containing $I$, which contradicts the maximality of $I$. Similarly, one can show that every maximal filter is prime.
:::


In particular, a maximal filter is also called an *ultrafilter*.


For two ordered sets $A,B$, consider an increasing function $f:A\rightarrow B$. Also, let any lower set $Y$ of $B$ be given, and let $X=f^{-1}(Y)$. If for some $y\in A$ there exists $x\in X$ such that $y\leq x$, then $f(y)\leq f(x)$, and since $Y$ is a lower set, $f(y)\in Y$, so $y\in X$. That is, the preimage $X$ of a lower set is also a lower set.

## Galois connection

The Galois connection we are about to introduce, as its name suggests, originates from Galois theory for field extensions. However, it can be abstracted as a relation between two ordered sets, and this abstraction proves useful in many areas.

::: Definition 6
Let two ordered sets $A,B$ be given. 

1. Suppose two increasing functions $F:A\rightarrow B$ and $G:B\rightarrow A$ satisfy, for any $a\in A$ and $b\in B$, the condition

    $$F(a)\leq b\iff a\leq G(b)$$

    Then $F$ is called the *lower adjoint* of $G$, $G$ is called the *upper adjoint* of $F$, and the pair $(F,G)$ is called a *monotone Galois connection* between $A$ and $B$.
2. Suppose two decreasing functions $F:A\rightarrow B$ and $G:B\rightarrow A$ satisfy, for any $a\in A$ and $b\in B$, the condition

    $$b\leq F(a)\iff a\leq G(b)$$

    Then $F$ and $G$ are each called a *polarity* of the other, and the pair $(F,G)$ is called an *antitone Galois connection* between $A$ and $B$.
:::

In either case, the function $G\circ F:A\rightarrow A$ always satisfies $a\leq G(F(a))$. First, for a monotone Galois connection,

$$a\leq G(F(a))\iff F(a)\leq F(a)$$

and the latter is always true; the same holds for an antitone Galois connection. On the other hand, $F\circ G$ depends on whether it is monotone or antitone; for a monotone Galois connection,

$$F(G(b))\leq b\iff G(b)\leq G(b)$$

and since the latter is always true, $F(G(b))\leq b$ holds, while for an antitone Galois connection,

$$b\leq F(G(b))\iff G(b)\leq G(b)$$

so $b\leq F(G(b))$ always holds. 

Meanwhile, $G\circ F$ and $F\circ G$ are compositions of two increasing functions or of two decreasing functions, so in either case they must be increasing functions.

In the remainder of this post, for convenience, we shall abbreviate $G\circ F$ and $F\circ G$ as $GF$ and $FG$, respectively.

::: Proposition 7
Let two ordered sets $A,B$ and a monotone Galois connection $F:A\rightarrow B$, $G:B\rightarrow A$ between them be given. For any $y\in B$, $GFG(y)=G(y)$ always holds. 

If they are an antitone Galois connection, then for any $x\in A$ and $y\in B$, both $GFG(y)=G(y)$ and $FGF(x)=F(x)$ hold.
:::
::: Proof
First, in $a\leq GF(a)$, substituting $a=G(y)$ yields $G(y)\leq GFG(y)$. Meanwhile, we have shown that $FG$ satisfies, for any $b\in B$, $FG(b)\leq b$, and since $G$ is an increasing function, we also obtain $GFG(y)\leq G(y)$. Therefore, $GFG(y)=G(y)$ holds.

On the other hand, if the pair $(F,G)$ is an antitone Galois connection, the fact that $G(y)\leq GFG(y)$ can be shown in the same manner as above. Also, for any $b\in B$, $b\leq FG(b)$ always holds, and since $G$ is a decreasing function, $G(y)\geq GFG(y)$ holds again, so $GFG(y)=G(y)$. $FGF(x)=F(x)$ is easily proved by interchanging the roles of $F$ and $G$.
:::

The following definition is used just as importantly in lattice theory as in topology.

::: Definition 8
For an ordered set $A$, a function $f:A\rightarrow A$ is a *closure operator* if all three of the following conditions are satisfied:

1. For all $x\in A$, $x\leq f(x)$.
2. For all $x\in A$, $f(x)=f(f(x))$.
3. If $x\leq y$, then $f(x)\leq f(y)$.

In this case, $x$ is *closed* if $f(x)=x$.
:::

Fix an antitone Galois connection. From the result $GFG(y)=G(y)$ in [Proposition 7](#prop7){: data-lid="fyrn5" }, substituting $y=F(x)$ for any $x\in A$,

$$GFGF(x)=GF(x)$$

holds. Thus the function $GF$ satisfies all the conditions above and is therefore a closure operator. Similarly, in an antitone Galois connection, $FG$ is also a closure operator.

By definition, that $x,y$ are closed with respect to $GF$ and $FG$, respectively, means that $GF(x)=x$ and $FG(y)=y$ hold, respectively. From [Proposition 7](#prop7){: data-lid="3b7ns" }, we know that all elements in the images of $F$ and $G$ are closed. Conversely, if an arbitrary element $x$ is closed with respect to $GF$, from $GF(x)=x$ we know that $x$ belongs to the image of $G$, and similarly the statement for $FG$ can also be proved.

Through this process, for a Galois connection between ordered sets $A,B$, we can construct the collections $A'\subseteq A$, $B'\subseteq B$ of closed elements, and the restrictions of $F$ and $G$ to these collections are well-defined. Moreover, these $F\vert_{A'}$ and $G\vert_{B'}$ are bijections and are *anti-isomorphisms*. These are specifically called *Galois correspondences*.


---
**References**

**[Bou]** N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.  
**[Wikipedia]** [Galois connection](https://en.wikipedia.org/wiki/Galois_connection)

---

[^1]: An upper set is also called an *upward closed set*, and a lower set is also called a *downward closed set*.
