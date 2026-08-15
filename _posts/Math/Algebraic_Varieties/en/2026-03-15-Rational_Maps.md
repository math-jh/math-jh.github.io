---
title: "Rational Maps"
description: "Rational maps generalize regular maps by studying functions defined on most points of an algebraic variety. We examine the equivalence classes of rational functions and the structure of function fields."
excerpt: "Rational maps and birational equivalence"

categories: [Math / Algebraic Varieties]
permalink: /en/math/algebraic_varieties/rational_maps
sidebar: 
    nav: "algebraic_varieties-en"

date: 2026-03-15
weight: 4
translated_at: 2026-08-15T21:17:36+00:00
translation_source: kimi-cli
---
In [§Quasi-Projective Varieties, ⁋Definition 7](/en/math/algebraic_varieties/quasi_projective_varieties#def7) we defined a regular map between quasi-projective varieties as a function that is defined at every point of its domain. Above all, it is a function defined at every point of its domain, so even if it is written in rational form on $D(f)$ as in [§Affine Varieties, ⁋Definition 14](/en/math/algebraic_varieties/affine_varieties#def14), the only thing that can appear in the denominator is a power of $f$, and therefore it is defined at every point.

However, many kinds of functions are still given in a form that is not a regular map. For example, $(x, y) \mapsto [x : y]$ is not a regular map because it is not defined at the origin, but it looks like a sufficiently natural function. In this post, we examine *rational maps*, which are functions defined at *most points*.

## Rational Functions

Just as when we defined regular maps, we first define the notion of a rational function before defining a rational map.

::: Definition 1
A *rational function* on a variety $X$ is a pair $(U,f)$ consisting of a nonempty open subset $U$ of $X$ and a regular function $f:U \rightarrow \mathbb{K}$ defined on it. Two rational functions $(U,f)$, $(V,g)$ are equivalent if they agree on $U\cap V$.
:::

The intuition behind this is as follows. In the Zariski topology, closed sets are small and open sets are large. Thus a rational function is a function that is not defined on a small set, but is defined at most of the remaining points. For instance, one may essentially think of open sets in the Zariski topology as sets of the form $D(g)$, and the regular functions $f/g$ defined on them are now what we regard as functions. ([§Affine Varieties, ⁋Definition 14](/en/math/algebraic_varieties/affine_varieties#def14)) Of course, this function is not defined at points where $g$ is zero, but that is precisely why we consider functions defined on an open set $U$, and in any case the points where $g$ is zero are small from the perspective of the whole space.

We denote the set of equivalence classes of all rational functions on $X$ by $\mathbb{K}(X)$. The sum and product of two rational functions are defined on the intersection of their domains of definition, and the inverse of a nonzero rational function is defined at the points where that function is nonzero. Therefore $\mathbb{K}(X)$ becomes a field, which we call the *function field*.

::: Proposition 2
For an affine variety $X$, we have $\mathbb{K}(X)=\Frac\mathbb{K}[X]$.
:::

The essential part of this proposition is showing that an arbitrary regular function $f:U\rightarrow \mathbb{K}$ defined on an arbitrary open set $U$ can actually be expressed in fractional form; in any case, $U$ can be written as a union of $D(g_i)$ ([§Affine Varieties, ⁋Proposition 6](/en/math/algebraic_varieties/affine_varieties#prop6)), and since the coordinate ring of $D(g_i)\cap X$ is $\mathbb{K}[X]_{g_i}$, the regular function on it takes the form of a rational expression with a power of $g_i$ in the denominator, so the proof is not difficult.

What is important is that this proposition provides a practical method for computing rational functions. For example, the coordinate ring of $X = V(\y - \x^2)$ is $\mathbb{K}[\x, \y]/(\y - \x^2) \cong \mathbb{K}[\x]$, and therefore $\mathbb{K}(X) = \Frac(\mathbb{K}[\x]) = \mathbb{K}(\x)$.

::: Proposition 3
For a variety $X$ and a nonempty open set $U$, we have $\mathbb{K}(U) = \mathbb{K}(X)$.
:::
::: Proof
First, it is obvious that the inclusion $\iota: U \hookrightarrow X$ induces an embedding $\iota^\ast: \mathbb{K}(X)\rightarrow \mathbb{K}(U)$ of function fields. Since any nonzero field homomorphism is an inclusion, it suffices to show that $\iota^\ast$ is surjective. ([\[Field Theory\] §Fields, ⁋Proposition 2](/en/math/field_theory/fields#prop2))

Now for any $f \in \mathbb{K}(U)$, $f$ is a regular function on some nonempty open subset $V$ of $U$, and then since this $V$ is also an open set of $X$, the pair $(V,f)$ belongs to $\mathbb{K}(X)$.
:::
::: Example 4
Considering the function field $\mathbb{K}(\mathbb{P}^n)$ of $\mathbb{P}^n$, by [Proposition 3](#prop3) it suffices to compute the function field on the open set $U_0$ of $\mathbb{P}^n$. However, since $U_0$ is an affine variety, by [Proposition 2](#prop2) it equals the fraction field of $\mathbb{K}[U_0]$, and therefore the function field of $\mathbb{P}^n$ is the field $\mathbb{K}(\t_1,\ldots, \t_n)$ generated by $n$ indeterminates.

Concretely, this is obtained by writing an element of $\mathbb{P}^n$ as $[x_0:\cdots: x_n]$ and letting $\t_i=\x_i/\x_0$ where $\x_i$ is the coordinate function reading off the $i$-th coordinate. If we had chosen a different open set $U_j$, then rational functions of a similar form would have been defined via $\t_i=\x_i/\x_j$, and thus we know that in general rational functions on $\mathbb{P}^n$ are represented as ratios $F/G$ of homogeneous polynomials of the same degree.
:::

## Rational Maps

Now, thinking about how we defined a regular map from a regular function, it is obvious how a rational map should be defined from a rational function.

::: Definition 5
A *rational map* between two varieties $X, Y$ is a pair $(U,\varphi)$ consisting of a nonempty open subset $U$ of $X$ and a regular map $\varphi: U \rightarrow Y$ defined on it.
:::

As before, two rational maps $\varphi: U \rightarrow Y$ and $\psi: V \rightarrow Y$ are regarded as the same if they agree on $U \cap V$. A rational map is usually denoted $\varphi: X \dashrightarrow Y$, where the dashed arrow indicates that it *may not be defined at every point*. The points where it is not defined are called *base points*.

On the other hand, for a rational map $\varphi:U\rightarrow Y$, we can consider rational maps equivalent to $(U,\varphi)$. Then if we take the union of the domains of all these rational maps, we obtain the *largest* open set on which $\varphi$ can be defined.

::: Definition 6
For a rational map $\varphi: X\dashrightarrow Y$, we denote the open set obtained by the above process by $\dom(\varphi)$.
:::

::: Example 7
One of the typical examples of a rational map is the projection from a point. For instance, considering the line $\{\x_2=0\}$ in $\mathbb{P}^2$, this can be thought of as a projective line $\mathbb{P}^1$ inside $\mathbb{P}^2$. Now the point $[0:0:1]$ is a point not on this line, and the equation of the line joining this point and an arbitrary point $[x_0:x_1:x_2]$ is

$$x_1\x_0-x_0\x_1=0$$

Then the point where this line meets the above $\mathbb{P}^1$ is exactly $[x_0:x_1:0]$, and thus the following projection

$$[x_0:x_1:x_2]\mapsto [x_0:x_1]$$

is obtained in this manner.
:::

## Birational Equivalence

If an isomorphism of regular maps means that two varieties have exactly the same structure, then birational equivalence means that two varieties have roughly the same structure. Many geometric properties are preserved not only between isomorphic varieties but also between birationally equivalent varieties.

::: Definition 8
A rational map $\varphi: X \dashrightarrow Y$ is called *dominant* if the image of $\varphi$ is dense in $Y$. That is, $\overline{\varphi(\dom(\varphi))} = Y$ holds.
:::

The reason the dominant condition is needed is that the composition of rational maps is not generally defined. For two rational maps $\varphi: X\dashrightarrow Y$ and $\psi: Y \dashrightarrow Z$, if the image of $\varphi$ does not meet $\dom(\psi)$, then there is no way to define $\psi\circ \varphi$ at all. However, if $\varphi$ is dominant, then $\varphi(\dom(\varphi))$ is dense in $Y$, so it must meet the nonempty open set $\dom(\psi)$, and therefore $W=\varphi^{-1}(\dom(\psi))$ becomes a nonempty open subset of $\dom(\varphi)$ on which $\psi\circ\varphi$ is defined as a regular map. We can also check that this $\psi\circ\varphi$ is again dominant. Since $X$ is irreducible, $W$ is dense in $\dom(\varphi)$, and $\varphi^{-1}(\overline{\varphi(W)})$ is a closed subset of $\dom(\varphi)$ containing $W$, so $\varphi(\dom(\varphi))\subseteq \overline{\varphi(W)}$, that is, $\overline{\varphi(W)}=Y$. Then $\varphi(W)$ is also dense in $\dom(\psi)$, so applying the same argument once more to $\psi$ and $\varphi(W)$, we obtain $\overline{\psi(\varphi(W))}=Z$. Henceforth we consider composition only for dominant rational maps.

::: Definition 9
A dominant rational map $\varphi: X \dashrightarrow Y$ is called a *birational map* if there exists another dominant rational map $\psi: Y \dashrightarrow X$ such that $\psi \circ \varphi = \id_X$ and $\varphi \circ \psi = \id_Y$ hold (where defined). Two varieties $X, Y$ are called *birationally equivalent* if there exists a birational map between them.
:::

Two birationally equivalent varieties are isomorphic "at most points." Concretely, as shown in the following proposition, there exist isomorphic open subsets of the two varieties. This shows that birational equivalence is weaker than isomorphism but still a strong relationship.

::: Proposition 10
For two varieties $X, Y$, the following are equivalent.

1. $X$ and $Y$ are birationally equivalent.
2. A $\mathbb{K}$-algebra isomorphism $\mathbb{K}(X) \cong \mathbb{K}(Y)$ holds.
3. There exist nonempty isomorphic open subsets of $X$ and $Y$.
:::
::: Proof
First, suppose $X, Y$ are birationally equivalent. Then considering the domain $\dom(\varphi)$ of the birational map $\varphi: X\dashrightarrow Y$, there exists a $\mathbb{K}$-algebra homomorphism $\varphi^\ast: \mathbb{K}(Y)\rightarrow \mathbb{K}(\dom(\varphi))$ of function fields induced by $\varphi$. Similarly, the birational inverse $\psi: Y\dashrightarrow X$ of $\varphi$ defines $\psi^\ast: \mathbb{K}(X)\rightarrow \mathbb{K}(\dom(\psi))$. Now by [Proposition 3](#prop3), we have $\mathbb{K}(\dom(\varphi))=\mathbb{K}(X)$ and $\mathbb{K}(\dom(\psi))=\mathbb{K}(Y)$, so using this we know from $\psi\circ\varphi=\id_X$ and $\varphi\circ\psi=\id_Y$ that $\varphi^\ast$ and $\psi^\ast$ are inverses of each other, and therefore $\mathbb{K}(X)\cong \mathbb{K}(Y)$.

Now suppose a $\mathbb{K}$-algebra isomorphism $\Phi: \mathbb{K}(X) \rightarrow \mathbb{K}(Y)$ is given. For any affine open subset $U \subseteq X$, the coordinate ring $\mathbb{K}[U]$ is a finitely generated $\mathbb{K}$-subalgebra of $\mathbb{K}(X)$. Now choosing an affine open subset $V\subseteq Y$ such that the images under $\Phi$ of all its generators are regular, we have $\Phi(\mathbb{K}[U])\subseteq \mathbb{K}[V]$, and on the other hand using $\Phi^{-1}$ in a similar way we obtain a nonzero $f\in \mathbb{K}[U]$ satisfying $\Phi^{-1}(\mathbb{K}[V])\subseteq \mathbb{K}[U]_f$. Now letting $h=\Phi(f)$, since $\Phi(1/f)=1/h$, from the above two inclusions we obtain $\Phi(\mathbb{K}[U]_f)\subseteq \mathbb{K}[V]_h$ and $\Phi^{-1}(\mathbb{K}[V]_h)\subseteq \mathbb{K}[U]_f$, and therefore $\Phi$ restricts to an isomorphism between $\mathbb{K}[U]_f$ and $\mathbb{K}[V]_h$. But these are respectively the coordinate rings of the affine varieties $D(f)\cap U$ and $D(h)\cap V$ ([§Affine Varieties, ⁋Proposition 7](/en/math/algebraic_varieties/affine_varieties#prop7)), so by [§Affine Varieties, ⁋Proposition 18](/en/math/algebraic_varieties/affine_varieties#prop18) these two open sets are isomorphic.

That the last condition implies the first is obvious by [Proposition 3](#prop3).
:::

This theorem shows that to determine birational equivalence, it suffices to look at the function field.

::: Example 11
Let us compute the function fields of $\mathbb{P}^1 \times \mathbb{P}^1$ and of the quadric surface $Q = V(\x\y - \z\w)$ in $\mathbb{P}^3$.

First, for $\mathbb{P}^1 \times \mathbb{P}^1$, by [Proposition 3](#prop3) it suffices to compute on the product open set $U_0 \times U_0$ of each factor. The function field of the first factor $\mathbb{P}^1$ is $\mathbb{K}(\t_1)$ as we saw in [Example 4](#ex4), and similarly the second factor is $\mathbb{K}(\t_2)$. Then through this we know that their function field is given by $\mathbb{K}(\t_1,\t_2)$.

Now consider the quadric surface $Q = V(\x\y - \z\w) \subseteq \mathbb{P}^3$. Similarly, by [Proposition 3](#prop3) it suffices to compute on the affine patch $\{\w \ne 0\}$. On this patch, letting $\x' = \x/\w$, $\y' = \y/\w$, $\z' = \z/\w$, the equation $\x\y - \z\w = 0$ becomes $\x'\y' - \z' = 0$. Therefore $\z' = \x'\y'$, and the coordinate ring of this patch is $\mathbb{K}[\x', \y', \z']/(\x'\y' - \z') \cong \mathbb{K}[\x', \y']$. By [Proposition 2](#prop2), we have $\mathbb{K}(Q) = \Frac(\mathbb{K}[\x', \y']) = \mathbb{K}(\x', \y') \cong \mathbb{K}(\t_1, \t_2)$.

Therefore, since $\mathbb{K}(\mathbb{P}^1 \times \mathbb{P}^1) \cong \mathbb{K}(Q) \cong \mathbb{K}(\t_1, \t_2)$, the two varieties are birationally equivalent by [Proposition 10](#prop10). In fact, the image of the Segre embedding $\mathbb{P}^1 \times \mathbb{P}^1 \rightarrow \mathbb{P}^3$, $([x : y], [u : v]) \mapsto [xu : xv : yu : yv]$ discussed in [§Projective Varieties, ⁋Example 16](/en/math/algebraic_varieties/projective_varieties#ex16) is exactly the quadric $V(\x\w - \y\z)$, which becomes $Q$ upon swapping $\y$ and $\w$. That is, in this case the birational equivalence actually realizes an isomorphism. This example shows that birational equivalence is weaker than isomorphism, but includes isomorphism.
:::

## Blow-up

A rational map has the limitation that it is not defined at base points. A representative tool for resolving this limitation is the *blow-up*. The motivation for this is the function $(x,y)\mapsto [x:y]$ that we first examined. This function takes a point $(x,y)$ in $\mathbb{A}^2$ and gives the slope of the line joining this point and the origin $(0,0)\in \mathbb{A}^2$, and the reason this is not defined at the origin is that two distinct points are needed to define a line. In such a case, we would usually fix the origin $(0,0)$ and let the other point $(x,y)$ approach $(0,0)$ to compute the limit value, but in this case there are infinitely many directions approaching $(0,0)$, so the limit is not well defined.

The idea of blow-up is simple: record all directions approaching $(0,0)$ separately.

::: Example 12
Consider the following variety

$$\Bl_{(0,0)} \mathbb{A}^2 = \{((x, y), [u : v]) \in \mathbb{A}^2 \times \mathbb{P}^1 \mid xv = yu\}$$

This set is a closed subvariety of $\mathbb{A}^2 \times \mathbb{P}^1$. The condition $xv = yu$ means that the point $(x, y)$ and the line $[u : v]$ are in the *same direction*. That is,

- For a point $(x,y)$ in $\mathbb{A}^2$ other than the origin, the point $[u:v]$ in $\mathbb{P}^1$ is uniquely determined by the condition $xv=yu$, and through this the point of $\Bl_{(0,0)}\mathbb{A}^2$ is uniquely determined.
- At the origin $(0,0)$ of $\mathbb{A}^2$, any point of $\mathbb{P}^1$ can exist.

{% diagram Math/Algebraic_Varieties/Rational_Maps-1.png width="32em" alt="Blowup" %}
<cap markdown="1">[Hart] p.29. Fig. 3.</cap>

Concretely, defining the projection $\pi_1: \Bl_{(0,0)} \mathbb{A}^2 \rightarrow \mathbb{A}^2$ by $\pi_1((x, y), [u : v]) = (x, y)$, the preimage of every point other than the origin is a single point, and the preimage of the origin is $\mathbb{P}^1$. This is called the *exceptional divisor*.

From this, since the two varieties $\mathbb{A}^2$ and $\Bl_{(0,0)}\mathbb{A}^2$ are isomorphic on the rest of the plane excluding the origin, $\pi_1$ is a birational map.

Now consider the rational map $\varphi: \mathbb{A}^2 \dashrightarrow \mathbb{P}^1$, $(x, y) \mapsto [x : y]$ mentioned earlier. This is not defined at the origin $(0, 0)$, but from the perspective of the blow-up $\Bl_{(0,0)} \mathbb{A}^2$, this is nothing but the projection $\pr_2$ to the $\mathbb{P}^1$ factor, and in particular this is a regular map. In this way we can resolve base points where a birational map is not defined.
:::

---

**References**

**[Hart]** R. Hartshorne, *Algebraic Geometry*, Springer, 1977.  
**[Har]** J. Harris, *Algebraic Geometry: A First Course*, Springer, 1992.  
**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.
