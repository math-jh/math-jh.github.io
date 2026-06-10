---
title: "Derivations"
description: "This post introduces the notion of a differential defined over a graded algebra, developing the sign rule via a commutation factor and the Leibniz rule for products."
excerpt: "Differential module"

categories: [Math / Multilinear Algebra]
permalink: /en/math/multilinear_algebra/derivations
sidebar: 
    nav: "multilinear_algebra-en"

date: 2022-12-12
last_modified_at: 2024-10-16
weight: 120
translated_at: 2026-06-01T14:00:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-01T14:00:04+00:00
---
## Definition

We now introduce the notion of a derivation. More precisely, we consider the concept of a differential form, which requires a graded algebra. Henceforth, we denote the abelian group giving the graded algebra structure by $$\Delta$$.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> Let $$(\Delta, +, 0)$$ be an abelian group, and let a function $$\varepsilon : \Delta \times \Delta \to \{ \pm 1 \}$$ satisfy the following three conditions.

- $$\varepsilon(\alpha + \alpha', \beta) = \varepsilon(\alpha, \beta)\varepsilon(\alpha', \beta)$$  
- $$\varepsilon(\alpha, \beta + \beta') = \varepsilon(\alpha, \beta)\varepsilon(\alpha, \beta')$$  
- $$\varepsilon(\beta, \alpha) = \varepsilon(\alpha, \beta)$$

Then $$\varepsilon$$ is called a *commutation factor*.

</div>

In particular, $$\varepsilon(2.\alpha, \beta) = \varepsilon(\alpha, 2.\beta) = 1$$.

The example of greatest interest is the case $$\Delta=\mathbb{Z}$$. In this case, by [Definition 1](#def1), $$\varepsilon$$ is completely determined by its value at $$\varepsilon(1,1)$$, and thus the only commutation factors defined on $$\Delta=\mathbb{Z}$$ are

$$\varepsilon(p,q)=1,\qquad \varepsilon(p,q)=(-1)^{pq}.$$

The commutation factor will appear as the sign arising when elements of degree $$p$$ and degree $$q$$ are interchanged in a product. 

Now let $$A$$ be a commutative ring, let $$E$$, $$E'$$, $$E''$$, $$F$$, $$F'$$, $$F''$$ be $$\Delta$$-graded $$A$$-modules, and consider $$A$$-bilinear maps

$$\mu: E \times E' \to E'', \qquad \lambda_1: F \times E' \to F', \qquad \lambda_2: E \times F' \to F''$$

and the induced $$A$$-linear maps

$$E \otimes_A E' \to E'', \qquad F \otimes_A E' \to F'', \qquad E \otimes_A F' \to F''$$

and assume that all three of these $$A$$-linear maps are degree $$0$$ graded homomorphisms. These correspond to multiplication operations, and we will write the image of $$x\otimes x'$$ in $$E''$$ simply as $$xx'$$. Since the element $$x\otimes x'$$ in $$E\otimes_A E'$$ lies in degree $$\degree(x)+\degree(x')$$, under the above assumption $$xx'$$ lies in the degree $$\degree(x)+\degree(x')$$ component of $$E''$$.

We now make the following definition.

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> In addition to the above situation, suppose a commutation factor $$\varepsilon: \Delta \times \Delta \to \{ \pm 1 \}$$ is given. Then a degree $$\delta$$ *$$(A, \varepsilon)$$-derivation* or simply an *$$\varepsilon$$-derivation* from $$(E, E', E'')$$ to $$(F, F', F'')$$ is a triple of degree $$\delta$$ graded $$A$$-module homomorphisms $$d: E \rightarrow F$$, $$d': E' \rightarrow F'$$, $$d'': E'' \rightarrow F''$$ satisfying the condition

$$d''(xx') = (dx)x' + \varepsilon(\delta, \deg(x))x(d'x').$$

If $$\varepsilon$$ is always $$1$$, so that $$\varepsilon$$ can be omitted from the above equation, then $$(d,d',d'')$$ is simply called a *derivation*.

</div>

To avoid confusion in the above definition, it is helpful to check where each term belongs; for instance, $$(dx)x'$$ on the right-hand side is the element of $$F''$$ obtained by multiplying $$dx\in F$$ and $$x'\in E'$$ via $$\lambda_1$$. However, in practice we are interested in the following two special cases.

1. $$E=F$$, $$E'=F'$$, $$E''=F''$$, and the three bilinear maps $$\mu, \lambda_1, \lambda_2$$ are all the same.
2. $$E=E'=E''$$, $$F=F'=F''$$, so that $$\mu:E\otimes_A E \rightarrow E$$ makes $$E$$ a *graded* algebra, and

    $$\lambda_1: F \otimes_A E \to F, \qquad \lambda_2: E \otimes_A F \to F.$$

    In this case, a *single* $$d:E \rightarrow F$$ satisfying the equation

    $$d(xy)=(dx)y+\varepsilon(\delta, \deg(x))x(dy)$$

    for all $$x,y\in E$$ is called an $$\varepsilon$$-derivation from $$E$$ to $$F$$.

Motivated by the second case, we sometimes abuse notation and write all of $$d, d', d''$$ with the same symbol $$d$$; then the equation of [Definition 2](#def2) can be written as

$$d(xx')=(dx)x'+\varepsilon(\delta,\deg(x))x (dx),$$

and in most cases we treat, this abuse of notation will not cause confusion.

If both of the above cases hold, so that $$E=E'=E''=F=F'=F''$$ and $$\lambda_1, \lambda_2$$ are multiplication in $$E$$, and the derivation is a single graded endomorphism $$d: E \rightarrow E$$, this is the situation that appears most frequently. Then the $$\varepsilon$$-derivation can be thought of as a map from $$A$$ to $$A$$, and in this case we simply call it an $$\varepsilon$$-derivation of $$A$$.

On the other hand, we said above that the case $$\Delta=\mathbb{Z}$$ is our main interest; in this case, considering the non-trivial commutation factor $$\varepsilon(p,q)=(-1)^{pq}$$, we know that any even-degree $$\varepsilon$$-derivation can always ignore the effect of $$\varepsilon$$. In the odd-degree case, for any homogeneous element $$x\in E$$ the equation

$$d(xx')=(dx)x'+(-1)^{\deg x}x(dx')$$

holds. In this case $$d$$ is called an *anti-derivation*.

## Differential Forms

To see how the discussion so far can be applied, let us briefly look at a simple example. Here $$\mathbb{K}$$ is a field and $$E=\mathbb{K}[\x_1,\ldots, \x_n]$$ is a polynomial algebra.

First, since a degree $$0$$ derivation can always ignore the commutation factor, if we view $$E$$ as a non-graded $$\mathbb{K}$$-algebra and consider a derivation from $$E$$ to $$E$$, then $$\varepsilon$$ does not appear. Now for each $$i$$, defining $$\partial_i:E \rightarrow E$$ to be the partial derivative $$\partial/\partial \x_i$$, the Leibniz rule implies that the equation of [Definition 2](#def2) is satisfied.

Now let us look at an example of a graded algebra. For the polynomial algebra $$E$$ defined as above, let $$M$$ be the free $$A$$-module generated by the elements

$$d\x_1,d\x_2,\ldots, d\x_n$$

and consider the exterior algebra $$\bigwedge(M)$$; this exterior algebra is a $$\mathbb{Z}$$-graded $$E$$-algebra

$$\bigwedge(M)=\bigoplus_{d=0}^n{\bigwedge}^d(M)$$

where $$\bigwedge^0(M)=A$$ and for each $$k$$, $$\bigwedge^k(M)$$ is the free $$E$$-module generated by elements of the form

$$d\x_J=d\x_{j_1}\wedge d\x_{j_2}\wedge\cdots\wedge d\x_{j_k},\qquad j_1<\cdots< j_k$$

([§Tensor Algebras, ⁋Proposition 13](/en/math/multilinear_algebra/tensor_algebras#prop13)). Now for each basis element

$$f\; d\x_{j_1}\wedge d\x_{j_2}\wedge\cdots\wedge d\x_{j_d}\in {\bigwedge}^k(M)$$

define

$$d(f\; d\x_{j_1}\wedge d\x_{j_2}\wedge\cdots\wedge d\x_{j_k})=\sum_{i=1}^n\frac{\partial f}{\partial \x_i}d\x_i\wedge d\x_{j_1}\wedge d\x_{j_2}\wedge\cdots\wedge d\x_{j_k}\in{\bigwedge}^{k+1}(M)$$

and extend this to define $$d: \bigwedge M \rightarrow \bigwedge M$$. Then $$d$$ is an antiderivation of degree $$1$$ on $$\bigwedge(M)$$.

## Bracket

Now assume that the first of the two cases above holds. Then $$d=(d,d',d'')$$ can be thought of as a map from $$(E,E',E'')$$ to itself, so we can also consider the composition of $$\varepsilon$$-derivations. However, looking at the equation in [Definition 2](#def2) in general, for arbitrarily given $$\varepsilon$$-derivations $$d_1,d_2$$ of degrees $$\delta_1$$, $$\delta_2$$ and arbitrary $$x\in E$$, $$x'\in E'$$, we have

$$\begin{aligned}(d_2\circ d_1)(xx')&=d_2((d_1x)x'+\varepsilon(\delta_1, \deg(x))x(d_1'x'))\\&=(d_2d_1x)x'+\varepsilon(\delta_2,\deg(d_1x))(d_1x)(d_2'x')+\varepsilon(\delta_1, \deg(x))(d_2x)(d_1'x')+\varepsilon(\delta_1, \deg(x))\varepsilon(\delta_2, \deg(x))x(d_2' d_1'x')\end{aligned}$$

so in general the composition of $$\varepsilon$$-derivations is not an $$\varepsilon$$-derivation. That is, if we consider the category of triples of $$\Delta$$-graded $$A$$-modules and the endomorphism algebra

$$\End_{\bgr_\Delta \Alg{A}^3}(E, E', E'')$$

of a fixed triple $$(E,E',E'')$$, the collection of $$\varepsilon$$-derivations does not define a subalgebra of this endomorphism algebra. However, looking at the above computation, it is clear what kind of multiplication must be defined on this algebra so that the collection of $$\varepsilon$$-derivations becomes closed: among the four terms on the right-hand side, if the middle two terms are eliminated, then $$d_2d_1$$ would be an $$\varepsilon$$-derivation of degree $$\delta_1+\delta_2$$.

To this end, first consider an arbitrary $$\Delta$$-graded algebra $$G$$ with a fixed commutation factor $$\varepsilon$$; for two homogeneous elements $$x,y$$ of $$G$$, define their *$$\varepsilon$$-bracket* by the formula

$$[x,y]_\varepsilon=xy-\varepsilon(\deg(x),\deg(y))yx.$$

Then through this we can define the $$\varepsilon$$-bracket on $$G=\End_{\bgr_\Delta \Alg{A}^3}(E, E', E'')$$.

<div class="proposition" markdown="1">

<ins id="prop3">**Proposition 3**</ins> Let $$d_1, d_2$$ be $$\varepsilon$$-derivations on $$(E, E', E'')$$, with degrees $$\delta_1$$, $$\delta_2$$ respectively. Then their $$\varepsilon$$-bracket

$$[d_1, d_2]_\varepsilon = d_1 \circ d_2 - \varepsilon_{\delta_1, \delta_2} \, d_2 \circ d_1$$

is another $$\varepsilon$$-derivation of degree $$\delta_1 + \delta_2$$. In particular, if $$d$$ is an $$\varepsilon$$-derivation of degree $$\delta$$ and $$\varepsilon_{\delta, \delta} = -1$$, then $$d^2 = d \circ d$$ is a derivation.

</div>

The proof of this is immediate from the expansion of $$(d_2\circ d_1)(xx')$$ computed above.

Then, restricting to the case $$\Delta=\mathbb{Z}$$, the above proposition yields the following corollary.

<div class="proposition" markdown="1">

<ins id="cor4">**Corollary 4**</ins> Let $$\Delta = \mathbb{Z}$$. Then the following hold.

1. The square of an antiderivation is a derivation.
2. The bracket of two derivations is a derivation.
3. The bracket of an antiderivation and an even-degree derivation is an antiderivation.
4. If $$d_1$$, $$d_2$$ are antiderivations, then $$d_1 d_2 + d_2 d_1$$ is a derivation.

</div>

On the other hand, looking at the partial derivatives defined on a polynomial algebra, they satisfy $$\partial_i\partial_j=\partial_j\partial_i$$ for all $$i,j$$. Now, as with general differential operators, writing $$D=\partial_i+\partial_j$$ and considering $$D^2$$, we can expand this as

$$D^2=(\partial_i+\partial_j)^2=\partial_i^2+\partial_i\partial_j+\partial_j\partial_i+\partial_j^2$$

and since $$\partial_i$$ and $$\partial_j$$ commute, we can also write this more simply as

$$D^2=\partial_i^2+2\partial_i\partial_j+\partial_j^2.$$

The following proposition generalizes this further.

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> Under the above assumptions and notation, suppose a polynomial $$F \in A[\x_1, \dots, \x_k]$$ in indeterminates $$T_1, \dots, T_n, T_1', \dots, T_n'$$ is given. That is, $$F(T)$$, $$F(T')$$ mean

$$F(T) = F(T_1, \dots, T_n), \qquad F(T') = F(T_1', \dots, T_n')$$

respectively. Similarly define

$$F(T + T') = F(T_1 + T_1', \dots, T_n + T_n').$$

Now if a polynomial $$P$$ satisfies the equation

$$P(T + T') = \sum_i Q_i(T) R_i(T')$$

then for any $$x\in E$$, $$x\'\in E'$$ the equation

$$P(D)(x x') = \sum_i (Q_i(D) x)(R_i(D) x')$$

holds.

</div>

## Derivations of $$A$$-Algebras

We now examine the second of the two special cases discussed after [Definition 2](#def2). That is, let $$E$$ be a $$\Delta$$-graded $$A$$-algebra, let $$F$$ be a graded $$A$$-module, and suppose two multiplications $$E\otimes_AF \rightarrow F$$ and $$F\otimes_AE \rightarrow F$$ are given.

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6**</ins> For an $$\varepsilon$$-derivation $$d:E \to F$$ of degree $$\delta$$, $$\ker(d)$$ is a graded subalgebra of $$E$$, and if $$E$$ has a unit then $$1 \in \ker(d)$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, it is obvious that $$\ker(d)$$ is an $$A$$-submodule of $$E$$, so it suffices to show that $$\ker(d)$$ is closed under multiplication. For any homogeneous $$x, y \in \ker(d)$$,

$$d(xy) = (dx)y + \varepsilon(\delta, \deg(x))x(dy) = 0$$

so $$xy \in \ker(d)$$. Therefore $$\ker(d)$$ is a graded subalgebra.

Now if $$E$$ has a unit, then $$1$$ has degree $$0$$, so

$$d(1) = d(1 \cdot 1) = (d1) \cdot 1 + \varepsilon_{\delta, 0} \cdot 1 \cdot (d1) = d1 + d1 = 2d1$$

and thus we obtain $$d(1) = 0$$.

</details>

Therefore, if $$d_1,d_2$$ are degree $$\delta$$ $$\varepsilon$$-derivations from $$E$$ to $$F$$ and they agree on the generators of $$E$$ as an algebra over $$A$$, then $$d_1=d_2$$. On the other hand, the following holds for inverses.

<div class="proposition" markdown="1">

<ins id="prop7">**Proposition 7**</ins> Let $$E$$ be a unital $$\Delta$$-graded $$A$$-algebra, and consider an $$\varepsilon$$-derivation $$d:E \to F$$ of degree $$\delta$$. If $$x$$ is an invertible homogeneous element of $$E$$, then for its inverse $$x^{-1}$$ the equation

$$d(x^{-1}) = -\varepsilon_{\delta, \deg(x)} x^{-1}(d(x))x^{-1}
= -\varepsilon_{\delta, \deg(x)} (d(x)) x^{-2}$$

holds.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

By [Proposition 5](#prop5) we have $$d(1) = 0$$, so

$$0 = d(xx^{-1}) = d(x))x^{-1} + \varepsilon_{\delta, \deg(x)}x(d(x^{-1})$$

Multiplying on the left by $$x^{-1}$$ on both sides gives

$$0 = x^{-1}(d(x))x^{-1} + \varepsilon_{\delta, \deg(x)} d(x^{-1})$$

and rearranging yields

$$d(x^{-1}) = -\varepsilon_{\delta, \deg(x)} x^{-1}(d(x))x^{-1}.
$$

Also, using the fact that the degree of $$x^{-1}$$ is $$-\deg(x)$$ and computing $$d(x^{-1}x)$$ gives the second equation.

</details>

<div class="proposition" markdown="1">

<ins id="prop8">**Proposition 8**</ins> Let $$E$$ be an $$A$$-algebra that is an integral domain, and consider its field of fractions $$K=\Frac E$$. Regarding any $$K$$-vector space $$F$$ as an $$E$$-module, given an $$A$$-derivation $$d:E \rightarrow F$$, $$d$$ extends uniquely to an $$A$$-derivation from $$K$$ to $$F$$.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

Suppose a derivation $$d:E \rightarrow f$$ is given, and suppose an extension $$\bar{d}$$ of $$d$$ to $$K$$ exists. Then by applying [Proposition 7](#prop7) we know that the equation

$$\bar{d}(u/v) = v^{-1} d(u) - v^{-2} u\, d(v)$$

must hold, and thus if $$\bar{d}$$ exists its expression is unique.

Let us show that this definition does not depend on the choice of representation of an element of $$B$$ as $$u/v$$. That is, even when $$u/v = u'/v'$$, we must have

$$v^{-1} d(u) - v^{-2} u\, d(v) = v'^{-1} d(u') - v'^{-2} u'\, d(v').$$

Set $$uv' = u'v$$. Applying $$d$$ to both sides gives

$$v' d(u) + u\, d(v') = v\, d(u') + u'\, d(v)$$

so multiplying both sides by $$vv'$$ yields

$$v v' d(u) - u\, v\, d(v') = v v' d(u') - u'\, v'\, d(v)$$

and rearranging gives

$$v' d(u) - v^{-1} u\, d(v) = v' d(u') - v'^{-1} u'\, d(v').$$

Therefore the definition is well-defined independent of the representation of the element $$u/v$$ of $$F$$. That $$\bar{d}$$ actually satisfies the condition of being an $$A$$-derivation from $$K$$ to $$F$$ is a straightforward computation.

</details>

In the following proposition, for notational convenience, for any degree $$\delta$$ $$\varepsilon$$-derivation $$d:A \rightarrow E$$ define

$$Z_\varepsilon=\{a\in A\mid \text{$xa_d=\varepsilon(\deg(a),\deg(x))a_dx$ for all homogeneous component $a_d$ of $a$ and for all homogeneous $x\in E$.}\}$$

<div class="proposition" markdown="1">

<ins id="prop9">**Proposition 9**</ins> Let $$A$$ be a unital graded associative $$A$$-algebra and let $$E$$ be a graded $$(A, A)$$-bimodule. Now let $$d: A \to E$$ be an $$\varepsilon$$-derivation of degree $$\delta$$, and let $$a$$ be a homogeneous element of $$Z_\varepsilon$$ of degree $$\alpha$$. Then the morphism

$$x \mapsto a (d x)$$

is an $$\varepsilon$$-derivation of degree $$\delta + \alpha$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Denote the given morphism by $$d'$$; this morphism is obviously $$A$$-linear. To show that $$d'$$ is an $$\varepsilon$$-derivation, for any homogeneous element $$x$$ of degree $$\delta'$$ and any $$y\in A$$ we have

$$\begin{aligned}d'(xy)&=a(dx)y+\varepsilon(\delta, \delta')a(x(dy))\\&=a(dx)y+\varepsilon(\delta, \delta')\varepsilon(\alpha,\delta')xa(dy)\\&=(d'x)y+\varepsilon(\delta+\alpha,\delta')x(d'y)\end{aligned}$$

so $$d'$$ is a degree $$\delta + \alpha$$ $$\varepsilon$$-derivation.

</details>

On the other hand, if $$E$$ is a $$\Delta$$-graded (associative) $$A$$-algebra with a given $$\varepsilon$$-bracket, then there is a natural $$\varepsilon$$-derivation on it.

<div class="definition" markdown="1">

<ins id="def10">**Definition 10**</ins> For a homogeneous element $$z\in E$$ of a graded $$A$$-algebra $$E$$, we write the morphism

$$x\mapsto [z,x]_\varepsilon$$

as $$\ad_\varepsilon(z)$$.

</div>

Then the following holds.

<div class="proposition" markdown="1">

<ins id="prop11">**Proposition 11**</ins> Let $$E$$ be a graded $$A$$-algebra.

1. For any $$\varepsilon$$-derivation $$d : E \rightarrow E$$ and every homogeneous element $$z$$ of $$E$$, $${[d, \ad(a)]_\varepsilon = \ad(dz)}$$ holds.
2. If $$A$$ is associative, then $$\ad(z)$$ is an $$\varepsilon$$-derivation of $$A$$, and its degree is $$\deg(z)$$.
</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

1. Suppose $$d$$ is an $$\varepsilon$$-derivation of degree $$\delta$$, and let $$\zeta = \deg(z)$$. Now let $$f = [d, \ad(z)]_\varepsilon$$; then for every homogeneous element $$x \in A$$ of degree $$\xi$$,

    $$\begin{aligned}f(x)&=d(z x - \varepsilon(\zeta, \xi) x z) - \varepsilon(\delta, \zeta) (z (dx) - \varepsilon(\zeta, \delta+\xi) (dx) z) \\&= d(z x) - \varepsilon(\zeta, \xi) d(x z) - \varepsilon(\delta, \zeta) z (dx) + \varepsilon(\zeta,2.\delta+\xi) d(x) z \\&=(dz)x+\varepsilon(\delta, \zeta)z(dx)-\varepsilon(\zeta,\xi)((dx)z+\varepsilon(\delta, \xi)x(dz))- \varepsilon(\delta, \zeta) z (dx) + \varepsilon(\zeta,2.\delta+\xi) (dx) z\\&=(dz)x+\varepsilon(\delta,\zeta)z(dx)-\varepsilon(\zeta,\xi)(dx)z-\varepsilon(\delta+\zeta,\xi)x(dz)-\varepsilon(\delta,\zeta)z (dx)+\varepsilon(\zeta,\xi)(dx)z\\&=(dz)x-\varepsilon(\delta+\zeta,\xi)x(dz)=[dz,x]_\varepsilon=\ad_\varepsilon(dz)(x)\end{aligned}$$

    and thus we obtain the desired result.
2. For every homogeneous element $$x \in A$$ of degree $$\xi$$ and homogeneous element $$y \in A$$ of degree $$\eta$$,

    $$\begin{aligned}\ad(z)(x y) &= z(x y) - \varepsilon(\zeta, \xi + \eta)(x y) z \\&= (z x) y - \varepsilon(\zeta, \xi) x z y + \varepsilon(\zeta, \xi) x z y - \varepsilon(\zeta, \xi + \eta) x y z \\&= (ax-\varepsilon(\zeta,\xi xz)y+\varepsilon(zeta,\xi)x(ay-\varepsilon(\zeta,\eta)ya)\\&=\ad(z)(x) \cdot y + \varepsilon(\zeta, \xi) x \cdot \ad(z)(y)\end{aligned}$$

    as desired.

</details>

Therefore, if $$E$$ is an associative graded $$A$$-algebra, then by [Definition 10](#def10) any homogeneous element of $$E$$ defines an $$\varepsilon$$-derivation from $$E$$ to itself, which we call an *inner $$\varepsilon$$-derivation*.

When this holds, replacing $$d$$ by an inner $$\varepsilon$$-derivation in the above equation yields the following corollary.

<div class="proposition" markdown="1">

<ins id="cor12">**Corollary 12**</ins> For two homogeneous elements $$x,y$$ of an associative graded algebra $$E$$, the equation

$${[\ad_\varepsilon(x), \ad_\varepsilon(y)]_\varepsilon = \ad_\varepsilon([x,y]_\varepsilon)}$$

always holds.

</div>

Moreover, since the equation in the above corollary can be obtained by verifying it for any homogeneous $$z\in E$$, if $$x,y,z$$ are homogeneous elements of degrees $$\xi,\eta,\zeta$$ respectively then the equation

$${\varepsilon}_{\xi, \zeta} [[x, [y,z]_{\varepsilon}]_{\varepsilon} + \varepsilon_{\eta,\xi} [y, [z,x]_{\varepsilon}]_{\varepsilon} + \varepsilon_{\zeta,\eta} [z, [x,y]_{\varepsilon}]_{\varepsilon} = 0$$

holds, and we call this the *Jacobi identity*.
