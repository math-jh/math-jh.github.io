---
title: "Rational Maps"
excerpt: "Rational maps and birational equivalence"

categories: [Math / Algebraic Varieties]
permalink: /en/math/algebraic_varieties/rational_maps
sidebar: 
    nav: "algebraic_varieties-en"

header:
    overlay_image: /assets/images/Math/Algebraic_Varieties/Rational_Maps.png
    overlay_filter: 0.5

date: 2026-03-15
last_modified_at: 2026-03-15
weight: 4
translated_at: 2026-05-19T04:00:02+00:00
translation_source: kimi-cli
---
In [§Quasi-Projective Varieties, ⁋Definition 7](/en/math/algebraic_varieties/quasi_projective_varieties#def7) we defined regular maps, functions between quasi-projective varieties. Above all, these are functions defined at every point of the domain; even if expressed in rational form over $$D(f)$$ as in [§Affine Varieties, ⁋Definition 13](/en/math/algebraic_varieties/affine_varieties#def13), the only denominators allowed are powers of $$f$$, so they are defined everywhere.

However, many kinds of functions are still given in a form that is not a regular map. For example, $$(x, y) \mapsto [x : y]$$ is not a regular map because it is undefined at the origin, yet it looks like a perfectly natural function. In this post we examine *rational maps*, functions defined <em>at most points</em>.

## Rational Functions

Just as when we defined regular maps, before defining rational maps we first define the notion of a rational function.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> A *rational function* on a variety $$X$$ is a pair $$(U,f)$$ consisting of a nonempty open subset $$U$$ of $$X$$ and a regular function $$f:U \rightarrow \mathbb{K}$$ defined on it. Two rational functions $$(U,f)$$ and $$(V,g)$$ are equivalent if they agree on $$U\cap V$$.

</div>

The intuition is as follows. In the Zariski topology closed sets are small and open sets are large. Thus a rational function is a function that is undefined on a small set but defined at most remaining points. For instance, essentially every open set in the Zariski topology can be thought of as a union of sets of the form $$D(g)$$, and regular functions of the form $$f/g$$ defined on them are now regarded as functions. ([§Affine Varieties, ⁋Definition 13](/en/math/algebraic_varieties/affine_varieties#def13)) Of course this function is undefined at points where $$g$$ vanishes, but that is precisely why we consider functions defined on an open set $$U$$, and in any case the zero locus of $$g$$ is small from the viewpoint of the whole space.

We denote the set of all rational functions on $$X$$ by $$\mathbb{K}(X)$$. The sum and product of two rational functions are defined on the intersection of their domains, and the inverse of a nonzero rational function is defined at points where the function does not vanish. Hence $$\mathbb{K}(X)$$ is a field, which we call the *function field*.

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> For an affine variety $$X$$, we have $$\mathbb{K}(X)=\Frac\mathbb{K}[X]$$.

</div>

The heart of this proposition is representing an arbitrary regular function $$f:U\rightarrow \mathbb{K}$$ defined on an arbitrary open set $$U$$ as a fraction; since $$U$$ can be written as a union of $$D(f)$$'s ([§Affine Varieties, ⁋Proposition 6](/en/math/algebraic_varieties/affine_varieties#prop6)) and a regular function on it has the form of a rational expression whose denominator is a power of $$f$$, the proof is not difficult.

What is important is that this proposition provides a practical way to compute rational functions. For example, the coordinate ring of $$X = V(\y - \x^2)$$ is $$\mathbb{K}[\x, \y]/(\y - \x^2) \cong \mathbb{K}[\x]$$, and therefore $$\mathbb{K}(X) = \operatorname{Frac}(\mathbb{K}[\x]) = \mathbb{K}(\x)$$.

<div class="proposition" markdown="1">

<ins id="prop3">**Proposition 3**</ins> For a variety $$X$$ and a nonempty open subset $$U$$, we have $$\mathbb{K}(U) = \mathbb{K}(X)$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, it is obvious that the inclusion $$\iota: U \hookrightarrow X$$ induces an embedding of function fields $$\iota^\ast: \mathbb{K}(X)\rightarrow \mathbb{K}(U)$$. Since any nonzero field homomorphism is an inclusion, it suffices to show that $$\iota^\ast$$ is surjective. ([\[Field Theory\] §Fields, ⁋Proposition 2](/en/math/field_theory/fields#prop2))

Now for any $$f \in \mathbb{K}(U)$$, the function $$f$$ is a regular function on some nonempty open subset $$V$$ of $$U$$, and then since this $$V$$ is also open in $$X$$, the pair $$(V,f)$$ belongs to $$\mathbb{K}(X)$$. 

</details>
<div class="example" markdown="1">

<ins id="ex4">**Example 4**</ins> 
To determine the function field $$\mathbb{K}(\mathbb{P}^n)$$ of $$\mathbb{P}^n$$, by [Proposition 3](#prop3) it is enough to compute the function field on the open set $$U_0$$ of $$\mathbb{P}^n$$. Since $$U_0$$ is an affine variety, by [Proposition 2](#prop2) this equals the fraction field of $$\mathbb{K}[U_0]$$, and therefore the function field of $$\mathbb{P}^n$$ is the field $$\mathbb{K}(\t_1,\ldots, \t_n)$$ generated by $$n$$ indeterminates. 

Concretely, writing elements of $$\mathbb{P}^n$$ as $$[x_0:\cdots: x_n]$$ and letting $$\x_i$$ be the coordinate function extracting the $$i$$-th coordinate, we obtain this by setting $$\t_i=\x_i/\x_0$$. If we had chosen a different open set $$U_j$$, similar rational functions would be defined by $$\t_i=\x_i/\x_j$$, and thus in general the rational functions on $$\mathbb{P}^n$$ are represented as ratios $$F/G$$ of homogeneous polynomials of the same degree. 

</div>

## Rational Maps

Now if we think about how we defined regular maps from regular functions, it is obvious how rational maps should be defined from rational functions.

<div class="definition" markdown="1">

<ins id="def5">**Definition 5**</ins> A *rational map* between two varieties $$X, Y$$ is a pair $$(U,\varphi)$$ consisting of a nonempty open subset $$U$$ of $$X$$ and a regular map $$\varphi: U \to Y$$ defined on it. 

</div>

As before, two rational maps $$\varphi: U \to Y$$ and $$\psi: V \to Y$$ are regarded as the same if they agree on $$U \cap V$$. A rational map is usually denoted $$\varphi: X \dashrightarrow Y$$, where the dotted arrow indicates that it <em>may not be defined at every point</em>. The points where it is undefined are called its *base points*.

On the other hand, for a rational map $$\varphi:U\rightarrow Y$$ we can consider rational maps equivalent to $$(U,\varphi)$$. Taking the union of the domains of all such rational maps gives the <em>largest</em> open subset on which $$\varphi$$ can be defined.

<div class="definition" markdown="1">

<ins id="def6">**Definition 6**</ins> For a rational map $$\varphi: X\dashrightarrow Y$$, we write $$\dom(\varphi)$$ for the open subset obtained by the above procedure. 

</div>

<div class="example" markdown="1">

<ins id="ex7">**Example 7**</ins> One typical example of a rational map is the projection from a point. For instance, consider the line $$\{\x_2=0\}$$ in $$\mathbb{P}^2$$; this can be regarded as a projective line $$\mathbb{P}^1$$ inside $$\mathbb{P}^2$$. The point $$[0:0:1]$$ does not lie on this line, and the equation of the line joining this point to an arbitrary point $$[x_0:x_1:x_2]$$ is

$$x_1\x_0-x_0\x_1=0$$

Then the intersection of this line with the above $$\mathbb{P}^1$$ is exactly $$[x_0:x_1:0]$$, and therefore the projection

$$[x_0:x_1:x_2]\mapsto [x_0:x_1]$$

is obtained in this way. 

</div>

## Birational Equivalence

If an isomorphism of regular maps means that two varieties have exactly the same structure, birational equivalence means that two varieties have essentially the same structure. Many geometric properties are preserved not only under isomorphic varieties but also between birationally equivalent varieties.

<div class="definition" markdown="1">

<ins id="def8">**Definition 8**</ins> A rational map $$\varphi: X \dashrightarrow Y$$ is called *dominant* if its image is dense in $$Y$$. That is, $$\overline{\varphi(X)} = Y$$ holds.

</div>

<div class="definition" markdown="1">

<ins id="def9">**Definition 9**</ins> A rational map $$\varphi: X \dashrightarrow Y$$ is a *birational map* if there exists another rational map $$\psi: Y \dashrightarrow X$$ such that $$\psi \circ \varphi = \operatorname{id}_X$$ and $$\varphi \circ \psi = \operatorname{id}_Y$$ (wherever they are defined). Two varieties $$X, Y$$ are said to be *birationally equivalent* if there exists a birational map between them.

</div>

Two birationally equivalent varieties are isomorphic "at most points". Specifically, as the following proposition shows, there exist isomorphic open subsets of the two varieties. This shows that birational equivalence is a weaker relation than isomorphism but still a strong one.

<div class="proposition" markdown="1">

<ins id="prop10">**Proposition 10**</ins> For two varieties $$X, Y$$ the following are equivalent.

1. $$X$$ and $$Y$$ are birationally equivalent.
2. $$\mathbb{K}(X) \cong \mathbb{K}(Y)$$ holds.
3. There exist nonempty isomorphic open subsets of $$X$$ and $$Y$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, suppose that $$X, Y$$ are birationally equivalent. Considering the domain $$\dom(\varphi)$$ of the birational map $$\varphi: X\dashrightarrow Y$$, there exists an induced homomorphism of function fields $$\varphi^\ast: \mathbb{K}(Y)\rightarrow \mathbb{K}(\dom(\varphi))$$. Similarly, the birational inverse $$\psi: Y\dashrightarrow X$$ of $$\varphi$$ defines $$\psi^\ast: \mathbb{K}(X)\rightarrow \mathbb{K}(\dom(\psi))$$. Now by [Proposition 3](#prop3) we have $$\mathbb{K}(\dom(\varphi))=\mathbb{K}(X)$$ and $$\mathbb{K}(\dom(\psi))=\mathbb{K}(Y)$$, and using this we see that $$\mathbb{K}(X)\cong \mathbb{K}(Y)$$.

Now suppose a field isomorphism $$\Phi: \mathbb{K}(X) \rightarrow \mathbb{K}(Y)$$ is given. For any affine open subset $$U \subseteq X$$, the coordinate ring $$\mathbb{K}[U]$$ is a finitely generated $$\mathbb{K}$$-subalgebra of $$\mathbb{K}(X)$$. Choose an affine open subset $$V\subseteq Y$$ on which the images of the generators of $$\mathbb{K}[U]$$ under $$\Phi$$ are all regular; this gives a map $$\Phi\vert_{\mathbb{K}[U]}:\mathbb{K}[U]\rightarrow \mathbb{K}[V]$$. On the other hand, in a similar way using $$\Phi^{-1}$$ we can obtain $$\Phi^{-1}\vert_{\mathbb{K}[V]}:\mathbb{K}[V]\rightarrow \mathbb{K}[U']$$, where $$U'\subset U$$. Since $$\Phi$$ is assumed to be an isomorphism, we must have $$\mathbb{K}[U]=\mathbb{K}[U']$$ and $$\mathbb{K}[U]\cong \mathbb{K}[V]$$.

That the last condition implies the first is obvious by [Proposition 3](#prop3). 

</details>

This proposition shows that to determine birational equivalence it suffices to look at the function field.

<div class="example" markdown="1">

<ins id="ex11">**Example 11**</ins> Let us compute the function fields of $$\mathbb{P}^1 \times \mathbb{P}^1$$ and of the quadric surface $$Q = V(\x\y - \z\w)$$ in $$\mathbb{P}^3$$.

First, for $$\mathbb{P}^1 \times \mathbb{P}^1$$, by [Proposition 3](#prop3) it suffices to compute on the product open set $$U_0 \times U_0$$ of the factors. The function field of the first factor $$\mathbb{P}^1$$ is $$\mathbb{K}(\t_1)$$ as we saw in [Example 4](#ex4), and similarly that of the second factor is $$\mathbb{K}(\t_2)$$. Hence the function field of the product is $$\mathbb{K}(\t_1,\t_2)$$.

Now consider the quadric surface $$Q = V(\x\y - \z\w) \subset \mathbb{P}^3$$. Again by [Proposition 3](#prop3) it suffices to compute on the affine patch $$\{\w \ne 0\}$$. On this patch set $$\x' = \x/\w$$, $$\y' = \y/\w$$, $$\z' = \z/\w$$; then the equation $$\x\y - \z\w = 0$$ becomes $$\x'\y' - \z' = 0$$. Hence $$\z' = \x'\y'$$, and the coordinate ring of this patch is $$\mathbb{K}[\x', \y', \z']/(\x'\y' - \z') \cong \mathbb{K}[\x', \y']$$. By [Proposition 2](#prop2) we have $$\mathbb{K}(Q) = \operatorname{Frac}(\mathbb{K}[\x', \y']) = \mathbb{K}(\x', \y') \cong \mathbb{K}(\t_1, \t_2)$$.

Therefore $$\mathbb{K}(\mathbb{P}^1 \times \mathbb{P}^1) \cong \mathbb{K}(Q) \cong \mathbb{K}(\t_1, \t_2)$$, so by [Proposition 10](#prop10) the two varieties are birationally equivalent. In fact, the image of the Segre embedding $$\mathbb{P}^1 \times \mathbb{P}^1 \to \mathbb{P}^3$$, $$([x : y], [u : v]) \mapsto [xu : xv : yu : yv]$$ discussed in [§Projective Varieties, ⁋Example 16](/en/math/algebraic_varieties/projective_varieties#ex16) is exactly $$V(\x\y - \z\w)$$. That is, in this case the birational equivalence is actually an isomorphism. This example shows that birational equivalence is weaker than isomorphism but includes it.

</div>

## Blow-ups

Rational maps have the drawback that they are undefined at base points. A prototypical tool for resolving this is the *blow-up*. The motivation comes from the very first function we looked at, $$(x,y)\mapsto [x:y]$$. This function sends a point $$(x,y)$$ in $$\mathbb{A}^2$$ to the slope of the line joining that point to the origin $$(0,0)\in \mathbb{A}^2$$, and the reason it is undefined at the origin is that defining a line requires two distinct points. In such a situation one usually fixes the origin $$(0,0)$$ and lets the other point $$(x,y)$$ approach it to compute a limit, but in this case there are infinitely many directions toward $$(0,0)$$, so the limit is not well defined.

The idea of a blow-up is simple: record separately all the directions approaching $$(0,0)$$.

<div class="example" markdown="1">

<ins id="ex12">**Example 12**</ins> Consider the variety

$$\Bl_{(0,0)} \mathbb{A}^2 = \{((x, y), [u : v]) \in \mathbb{A}^2 \times \mathbb{P}^1 \mid xv = yu\}$$

This set is a closed subvariety of $$\mathbb{A}^2 \times \mathbb{P}^1$$. The condition $$xv = yu$$ means that the point $$(x, y)$$ and the line $$[u : v]$$ lie in the <em>same direction</em>. That is, 

- For a point $$(x,y)$$ in $$\mathbb{A}^2$$ other than the origin, the condition $$xv=yu$$ determines the point $$[u:v]$$ in $$\mathbb{P}^1$$ uniquely, and thereby the point of $$\Bl_{(0,0)}\mathbb{A}^2$$ is uniquely determined. 
- Over the origin $$(0,0)$$ of $$\mathbb{A}^2$$, every point of $$\mathbb{P}^1$$ can occur. 

![Blowup](/assets/images/Math/Algebraic_Varieties/Rational_Maps-1.png){:style="width:32em" class="invert" .align-center}
<cap markdown="1">[Har1] p.29. Fig. 3.</cap>

Explicitly, define the projection $$\pi_1: \operatorname{Bl}_{(0,0)} \mathbb{A}^2 \to \mathbb{A}^2$$ by $$\pi((x, y), [u : v]) = (x, y)$$; then the preimage of every point other than the origin is a single point, while the preimage of the origin is $$\mathbb{P}^1$$. This is called the *exceptional divisor*.

From this, away from the origin the two varieties $$\mathbb{A}^2$$ and $$\Bl_{(0,0)}\mathbb{A}^2$$ are isomorphic, so $$\pi$$ is a birational map. 

Now consider the rational map $$\varphi: \mathbb{A}^2 \dashrightarrow \mathbb{P}^1$$, $$(x, y) \mapsto [x : y]$$ mentioned earlier. It is undefined at the origin $$(0, 0)$$, but on the blow-up $$\operatorname{Bl}_{(0,0)} \mathbb{A}^2$$ it is nothing more than the projection $$\pr_2$$ onto the $$\mathbb{P}^1$$ factor, which in particular is a regular map. In this way we can resolve a base point at which a rational map is undefined. 

</div>

---

**References**

**[Har1]** R. Hartshorne, *Algebraic Geometry*, Springer, 1977.  
**[Har2]** J. Harris, *Algebraic Geometry: A First Course*, Springer, 1992.  
**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.
