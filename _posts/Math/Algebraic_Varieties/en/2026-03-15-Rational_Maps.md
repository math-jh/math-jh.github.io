---
title: "Rational Maps"
description: "Rational maps generalize regular morphisms and deal with functions defined on most points of an algebraic variety. We examine the definition of equivalence classes of rational functions and the structure of function fields."
excerpt: "Rational maps and birational equivalence"

categories: [Math / Algebraic Varieties]
permalink: /en/math/algebraic_varieties/rational_maps
sidebar: 
    nav: "algebraic_varieties-en"

date: 2026-03-15
weight: 4
translated_at: 2026-08-18T19:45:05+00:00
translation_source: kimi-cli
last_polished_at: 2026-09-23T07:15:05+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
In [§Quasi-Projective Varieties, ⁋Definition 7](/en/math/algebraic_varieties/quasi_projective_varieties#def7){: data-lid="54gkl" data-relation="required" }, we defined regular maps, which are functions between quasi-projective varieties. Above all, these are functions defined at every point of their domain; even if they are written in the form of rational expressions on $D(f)$ as in [§Affine Varieties, ⁋Definition 14](/en/math/algebraic_varieties/affine_varieties#def14){: data-lid="noo5h" data-relation="weak" }, they are defined at all points because the only things that can enter the denominator are powers of $f$.

However, many kinds of functions are still given in forms that are not regular maps. For example, $(x, y) \mapsto [x : y]$ is not a regular map because it is not defined at the origin, but it looks like a sufficiently natural function. In this post, we examine *rational maps*, which are functions defined *at most points*.

## Rational Functions

Just as when defining regular maps, we first define the notion of a rational function before defining rational maps.

::: Definition 1
A *rational function* on a variety $X$ means, given in $X$ a nonempty open subset $U$ and a regular function $f:U \rightarrow \mathbb{K}$ defined on it, the pair $(U,f)$. Two rational functions $(U,f)$ and $(V,g)$ are equivalent if they agree on $U\cap V$. 
:::

The intuition for this is as follows. In the Zariski topology, closed sets are small and open sets are large. Therefore, a rational function is a function that is not defined on a small set, but is defined at most other points. For instance, essentially one may think of open sets in the Zariski topology as sets of the form $D(g)$, and we now consider the regular functions $f/g$ defined on them as functions. ([§Affine Varieties, ⁋Definition 14](/en/math/algebraic_varieties/affine_varieties#def14){: data-lid="ltkqt" data-relation="weak" }) Of course, this function is not defined at points where $g$ is $0$, but that is precisely why we consider functions defined on open sets $U$, and in any case, the points where $g$ is $0$ are small when viewed in the whole space.

We denote the set of equivalence classes of all rational functions on $X$ by $K(X)$. The sum and product of two rational functions are defined on the intersection of their domains of definition, and the inverse of a nonzero rational function is defined at points where the function is nonzero. Therefore, $K(X)$ is a field, which we call the *function field*.

::: Proposition 2
For an affine variety $X$, we have $K(X)=\Frac\mathbb{K}[X]$.
:::

The crucial part of this proposition is, for an arbitrary open set $U$ and an arbitrary regular function $f:U\rightarrow \mathbb{K}$ defined on it, actually representing it in fractional form; in any case, $U$ can be represented as a union of $D(g_i)$ ([§Affine Varieties, ⁋Proposition 6](/en/math/algebraic_varieties/affine_varieties#prop6){: data-lid="4s6ud" data-relation="required" }), and since the coordinate ring of $D(g_i)\cap X$ is $\mathbb{K}[X]_{g_i}$, regular functions on it take the form of rational expressions having powers of $g_i$ in the denominator, so the proof is not difficult.

What is important is that this proposition provides a practical way to compute rational functions. For example, the coordinate ring of $X = V(\y - \x^2)$ is $\mathbb{K}[\x, \y]/(\y - \x^2) \cong \mathbb{K}[\x]$, and therefore $K(X) = \Frac(\mathbb{K}[\x]) = \mathbb{K}(\x)$.

::: Proposition 3
For a variety $X$ and a nonempty open subset $U$, we have $K(U) = K(X)$.
:::
::: Proof
First, it is obvious that the inclusion $\iota: U \hookrightarrow X$ induces an embedding $\iota^\ast: K(X)\rightarrow K(U)$ of function fields. Since any nonzero field homomorphism is an inclusion, it suffices for us to show that $\iota^\ast$ is surjective. ([\[Field Theory\] §Fields, ⁋Proposition 2](/en/math/field_theory/fields#prop2){: data-lid="ap7my" data-relation="required" })

However, for any $f \in K(U)$, $f$ is a regular function on some nonempty open subset of $U$, namely $V$, and since this $V$ is also an open subset of $X$, this pair $(V,f)$ belongs to $K(X)$. 
:::

::: Example 4
Considering the function field of $\mathbb{P}^n$, $K(\mathbb{P}^n)$, by [Proposition 3](#prop3){: data-lid="esvis" data-relation="required" } it suffices to compute the function field on the open set in $\mathbb{P}^n$, $U_0$. Since $U_0$ is an affine variety, by [Proposition 2](#prop2){: data-lid="v0veg" data-relation="required" } it equals the fraction field of $\mathbb{K}[U_0]$, and therefore the function field of $\mathbb{P}^n$ is the field generated by $n$ indeterminates, $\mathbb{K}(\t_1,\ldots, \t_n)$.

Concretely, this is obtained by expressing elements of $\mathbb{P}^n$ as $[x_0:\cdots: x_n]$, and, denoting the coordinate function that reads off the $i$-th coordinate by $\x_i$, setting $\t_i=\x_i/\x_0$. If we had chosen a different open set $U_j$, similar rational functions would have been defined via $\t_i=\x_i/\x_j$, and so in general we know that rational functions on $\mathbb{P}^n$ appear in the form of a ratio $F/G$ of homogeneous polynomials of the same degree.
:::

## Rational Maps

Now, recalling how we defined regular maps from regular functions, it is obvious how to define rational maps from rational functions.

::: Definition 5
A *rational map* between two varieties $X, Y$ refers to, given a nonempty open set of $X$, $U$, and a regular map $\varphi: U \rightarrow Y$ defined on it, the pair $(U,\varphi)$.
:::

As before, two rational maps $\varphi: U \rightarrow Y$ and $\psi: V \rightarrow Y$ are regarded as the same if they agree on $U \cap V$. A rational map is usually denoted $\varphi: X \dashrightarrow Y$, where the dashed arrow indicates that *it may not be defined at every point*. The points where it is undefined are called *base points*.

On the other hand, for a rational map $\varphi:U\rightarrow Y$, we may consider rational maps equivalent to $(U,\varphi)$. Then, taking the union of the domains of all these rational maps, we obtain the *largest* open set on which $\varphi$ can be defined.

::: Definition 6
For a rational map $\varphi: X\dashrightarrow Y$, we write $\dom(\varphi)$ for the open set obtained by the above procedure.
:::

::: Example 7
One of the typical examples of a rational map is projection from a point. For instance, if we consider in $\mathbb{P}^2$ the line $\{\x_2=0\}$, this can be viewed, inside $\mathbb{P}^2$, as the projective line $\mathbb{P}^1$. Now, the point $[0:0:1]$ is a point not lying on this line, and the line connecting this point and an arbitrary point $[x_0:x_1:x_2]$ has equation

$$x_1\x_0-x_0\x_1=0$$

Then the point where this line meets the above $\mathbb{P}^1$ is precisely $[x_0:x_1:0]$, and thus the following projection

$$[x_0:x_1:x_2]\mapsto [x_0:x_1]$$

is obtained in this manner.
:::

## Birational Equivalence

If an isomorphism of regular maps means that two varieties have completely the same structure, then birational equivalence means that two varieties have largely the same structure. Many geometric properties are preserved not only between isomorphic varieties but also between birationally equivalent varieties.

::: Definition 8
A rational map $\varphi: X \dashrightarrow Y$ is called *dominant* if the image of $\varphi$ is dense in $Y$. That is, $\overline{\varphi(\dom(\varphi))} = Y$ holds.
:::

The condition of being dominant is needed because the composition of rational maps is not generally defined. For two rational maps $\varphi: X\dashrightarrow Y$ and $\psi: Y \dashrightarrow Z$, if the image of $\varphi$ does not meet $\dom(\psi)$, there is no way at all to define $\psi\circ \varphi$. However, if $\varphi$ is dominant, then $\varphi(\dom(\varphi))$ is dense in $Y$, so it necessarily meets the nonempty open set $\dom(\psi)$, and therefore $W=\varphi^{-1}(\dom(\psi))$ is a nonempty open subset of $\dom(\varphi)$ on which $\psi\circ\varphi$ is defined as a regular map. One can also check that $\psi\circ\varphi$ obtained in this way is again dominant. Since $X$ is irreducible, $W$ is dense in $\dom(\varphi)$, and since $\varphi^{-1}(\overline{\varphi(W)})$ is a closed subset of $\dom(\varphi)$ containing $W$, we have $\varphi(\dom(\varphi))\subseteq \overline{\varphi(W)}$, that is, $\overline{\varphi(W)}=Y$. Then $\varphi(W)$ is dense in $\dom(\psi)$ as well, so applying the same argument once more to $\psi$ and $\varphi(W)$ yields $\overline{\psi(\varphi(W))}=Z$. Henceforth, we consider compositions only for dominant rational maps.

::: Definition 9
A dominant rational map $\varphi: X \dashrightarrow Y$ is called a *birational map* if there exists another dominant rational map $\psi: Y \dashrightarrow X$ such that $\psi \circ \varphi = \id_X$ and $\varphi \circ \psi = \id_Y$ hold (where defined). Two varieties $X, Y$ are called *birationally equivalent* if there exists a birational map between them.
:::

Two birationally equivalent varieties are isomorphic "at most points." Specifically, as shown in the next proposition, there exist isomorphic open subsets of the two varieties. This shows that birational equivalence is weaker than isomorphism but still a strong relationship.

::: Proposition 10
For two varieties $X, Y$, the following are equivalent.

1. $X$ and $Y$ are birationally equivalent.
2. There is a $\mathbb{K}$-algebra isomorphism $K(X) \cong K(Y)$.
3. There exist nonempty isomorphic open subsets of $X$ and $Y$.
:::
::: Proof
First, suppose that $X, Y$ are birationally equivalent. Then, considering the birational map $\varphi: X\dashrightarrow Y$ and its domain $\dom(\varphi)$, $\varphi$ induces a $\mathbb{K}$-algebra homomorphism of function fields $\varphi^\ast: K(Y)\rightarrow K(\dom(\varphi))$. Similarly, the birational inverse of $\varphi$, $\psi: Y\dashrightarrow X$, defines $\psi^\ast: K(X)\rightarrow K(\dom(\psi))$. Now by [Proposition 3](#prop3){: data-lid="yi0pc" data-relation="required" }, since $K(\dom(\varphi))=K(X)$ and $K(\dom(\psi))=K(Y)$, using this we see from $\psi\circ\varphi=\id_X$ and $\varphi\circ\psi=\id_Y$ that $\varphi^\ast$ and $\psi^\ast$ are inverses of each other, and hence $K(X)\cong K(Y)$.

Now suppose that a $\mathbb{K}$-algebra isomorphism $\Phi: K(X) \rightarrow K(Y)$ is given. For any affine open subset of $X$, $U \subseteq X$, the coordinate ring $\mathbb{K}[U]$ is, within $K(X)$, a finitely generated $\mathbb{K}$-subalgebra. Now, ensuring that the images under $\Phi$ of their generators are all regular, if we choose an affine open subset of $Y$, $V\subseteq Y$, then $\Phi(\mathbb{K}[U])\subseteq \mathbb{K}[V]$; meanwhile, using $\Phi^{-1}$ in a similar way, we obtain, satisfying $\Phi^{-1}(\mathbb{K}[V])\subseteq \mathbb{K}[U]_f$, a non-$0$ element $f\in \mathbb{K}[U]$. Now, setting $h=\Phi(f)$, since $\Phi(1/f)=1/h$, from the two inclusions above we get $\Phi(\mathbb{K}[U]_f)\subseteq \mathbb{K}[V]_h$ and $\Phi^{-1}(\mathbb{K}[V]_h)\subseteq \mathbb{K}[U]_f$, and therefore $\Phi$ restricts to an isomorphism between $\mathbb{K}[U]_f$ and $\mathbb{K}[V]_h$. But since these are the coordinate rings of the affine varieties $D(f)\cap U$ and $D(h)\cap V$ respectively ([§Affine Varieties, ⁋Proposition 7](/en/math/algebraic_varieties/affine_varieties#prop7){: data-lid="aottl" data-relation="required" }), by [§Affine Varieties, ⁋Proposition 18](/en/math/algebraic_varieties/affine_varieties#prop18){: data-lid="wbfo9" data-relation="required" } these two open sets are isomorphic.

That the last condition implies the first is obvious by [Proposition 3](#prop3){: data-lid="r5x35" data-relation="required" }.
:::

This theorem shows that to determine birational equivalence it suffices to look at the function field.

::: Example 11
Let us compute the function fields of $\mathbb{P}^1 \times \mathbb{P}^1$ and of the quadric surface in $\mathbb{P}^3$, $Q = V(\x\y - \z\w)$.

First, for $\mathbb{P}^1 \times \mathbb{P}^1$, by [Proposition 3](#prop3){: data-lid="qkk1d" data-relation="required" } it suffices to compute on the product open set $U_0 \times U_0$ of each factor. The function field of the first factor $\mathbb{P}^1$ is $\mathbb{K}(\t_1)$ as we saw in [Example 4](#ex4){: data-lid="9akou" data-relation="required" }, and similarly that of the second factor is $\mathbb{K}(\t_2)$. From this, we see that their function field is given by $\mathbb{K}(\t_1,\t_2)$.

Now consider the quadric surface $Q = V(\x\y - \z\w) \subseteq \mathbb{P}^3$. Similarly, by [Proposition 3](#prop3){: data-lid="7u483" data-relation="required" } it suffices to compute on the affine patch $\{\w \ne 0\}$. On this patch, if we set $\x' = \x/\w$, $\y' = \y/\w$, $\z' = \z/\w$, then the equation $\x\y - \z\w = 0$ becomes $\x'\y' - \z' = 0$. Therefore $\z' = \x'\y'$, and the coordinate ring of this patch is $\mathbb{K}[\x', \y', \z']/(\x'\y' - \z') \cong \mathbb{K}[\x', \y']$. By [Proposition 2](#prop2){: data-lid="v9nzw" data-relation="required" }, $K(Q) = \Frac(\mathbb{K}[\x', \y']) = \mathbb{K}(\x', \y') \cong \mathbb{K}(\t_1, \t_2)$.

Therefore, since $K(\mathbb{P}^1 \times \mathbb{P}^1) \cong K(Q) \cong \mathbb{K}(\t_1, \t_2)$, by [Proposition 10](#prop10){: data-lid="15ff7" data-relation="required" } the two varieties are birationally equivalent. In fact, the image of the Segre embedding $\mathbb{P}^1 \times \mathbb{P}^1 \rightarrow \mathbb{P}^3$, $([x : y], [u : v]) \mapsto [xu : xv : yu : yv]$ discussed in [§Projective Varieties, ⁋Example 16](/en/math/algebraic_varieties/projective_varieties#ex16){: data-lid="b7krq" data-relation="weak" } is exactly $V(\x\w - \y\z)$, which is a quadric that becomes $Q$ upon swapping $\y$ and $\w$. That is, in this case the birational equivalence is actually an isomorphism. This example shows that birational equivalence is weaker than isomorphism, but includes it.
:::

## Blow-up

A rational map has the limitation that it is undefined at base points. A representative tool for resolving this limitation is the *blow-up*. The motivation for this is the very first function we considered, $(x,y)\mapsto [x:y]$. When given a point in $\mathbb{A}^2$, $(x,y)$, this function gives the slope of the line connecting this point and the origin $(0,0)\in \mathbb{A}^2$; the reason it is undefined at the origin is that two distinct points are needed to define a line. In such a case, we would usually fix the origin $(0,0)$ and let the other point $(x,y)$ approach $(0,0)$ to compute the limit, but in this case there are infinitely many directions toward $(0,0)$, so the limit is not well defined.

The idea of blow-up is simple: record all directions toward $(0,0)$ separately.

::: Example 12
Consider the following variety

$$\Bl_{(0,0)} \mathbb{A}^2 = \{((x, y), [u : v]) \in \mathbb{A}^2 \times \mathbb{P}^1 \mid xv = yu\}$$

This set is a closed subvariety of $\mathbb{A}^2 \times \mathbb{P}^1$. The condition $xv = yu$ means that the point $(x, y)$ and the line $[u : v]$ lie in the *same direction*. That is, 

- For a point in $\mathbb{A}^2$ other than the origin, $(x,y)$, the condition $xv=yu$ uniquely determines the point in $\mathbb{P}^1$, $[u:v]$, and through this the point of $\Bl_{(0,0)}\mathbb{A}^2$ is uniquely determined. 
- At the origin of $\mathbb{A}^2$, $(0,0)$, every point of $\mathbb{P}^1$ is possible. 

{% diagram Math/Algebraic_Varieties/Rational_Maps-1.png width="32em" alt="Blowup" %}
<cap markdown="1">[Hart] p.29. Fig. 3.</cap>

Concretely, define the projection $\pi_1: \Bl_{(0,0)} \mathbb{A}^2 \rightarrow \mathbb{A}^2$ by $\pi_1((x, y), [u : v]) = (x, y)$. Then the preimage of every point other than the origin is a single point, while the preimage of the origin is $\mathbb{P}^1$. This is called the *exceptional divisor*.

Hence away from the origin the two varieties $\mathbb{A}^2$ and $\Bl_{(0,0)}\mathbb{A}^2$ are isomorphic, so $\pi_1$ is a birational map. 

Now consider the rational map $\varphi: \mathbb{A}^2 \dashrightarrow \mathbb{P}^1$, $(x, y) \mapsto [x : y]$ mentioned earlier. It is undefined at the origin $(0, 0)$, but from the viewpoint of the blow-up $\Bl_{(0,0)} \mathbb{A}^2$ it is simply the projection to the $\mathbb{P}^1$ factor, $\pr_2$, which in particular is a regular map. In this way we can resolve base points where a birational map is undefined. 
:::

---

**References**

**[Hart]** R. Hartshorne, *Algebraic Geometry*, Springer, 1977.  
**[Har]** J. Harris, *Algebraic Geometry: A First Course*, Springer, 1992.  
**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.
