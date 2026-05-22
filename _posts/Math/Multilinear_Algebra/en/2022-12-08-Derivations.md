---
title: "Derivations"
excerpt: "Differential module"

categories: [Math / Multilinear Algebra]
permalink: /en/math/multilinear_algebra/derivations
header:
    overlay_image: /assets/images/Math/Multilinear_Algebra/Derivations.png
    overlay_filter: 0.5
sidebar: 
    nav: "multilinear_algebra-en"

date: 2022-12-12
last_modified_at: 2024-10-16
weight: 120
translated_at: 2026-05-22T00:00:01+00:00
translation_source: kimi-cli
---
## Definition of a Derivation

We now introduce the notion of a derivation. To be more precise, what we will consider is the concept of differential forms, and to treat this we need a graded algebra. Henceforth we denote by $$\Delta$$ the abelian group that provides the grading structure of the graded algebra.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> For an abelian group $$(\Delta, +, 0)$$, suppose a function $$\varepsilon : \Delta \times \Delta \to \{ \pm 1 \}$$ satisfies the following three conditions.

- $$\varepsilon(\alpha + \alpha', \beta) = \varepsilon(\alpha, \beta)\varepsilon(\alpha', \beta)$$  
- $$\varepsilon(\alpha, \beta + \beta') = \varepsilon(\alpha, \beta)\varepsilon(\alpha, \beta')$$  
- $$\varepsilon(\beta, \alpha) = \varepsilon(\alpha, \beta)$$

In this case, we call $$\varepsilon$$ a *commutation factor*.

</div>

Then in particular $$\varepsilon(2.\alpha, \beta) = \varepsilon(\alpha, 2.\beta) = 1$$.

The example of most interest to us is the case $$\Delta=\mathbb{Z}$$. In this case, by [Definition 1](#def1), $$\varepsilon$$ is completely determined by its value at $$\varepsilon(1,1)$$, and hence the commutation factors defined on $$\Delta=\mathbb{Z}$$ are only

$$\varepsilon(p,q)=1,\qquad \varepsilon(p,q)=(-1)^{pq}$$

These two. The commutation factor will appear as the sign that arises when we interchange the order of elements of degree $$p$$ and degree $$q$$ in a product.

Now let $$A$$ be a commutative ring, let $$E$$, $$E'$$, $$E''$$, $$F$$, $$F''$$ be $$\Delta$$-graded $$A$$-modules, and let

$$\mu: E \times E' \to E'', \qquad \lambda_1: F \times E' \to F', \qquad \lambda_2: E \times F' \to F''$$

be $$A$$-bilinear maps, and consider the $$A$$-linear maps they induce

$$E \otimes_A E' \to E'', \qquad F \otimes_A E' \to F'', \qquad E \otimes_A F' \to F''$$

and assume that these three $$A$$-linear maps are all degree $$0$$ graded homomorphisms. These correspond to multiplication operations, and we will simply write, for instance, the image of $$x\otimes x'$$ in $$E''$$ as $$xx'$$. Since the element $$x\otimes x'$$ in $$E\otimes_A E'$$ lies in degree $$\degree(x)+\degree(x')$$, under the above assumption $$xx'$$ lies in the degree $$\degree(x)+\degree(x')$$ component of $$E''$$.

We now define the following.

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> In addition to the above situation, suppose a commutation factor $$\varepsilon: \Delta \times \Delta \to \{ \pm 1 \}$$ is given. Then a triple $$d: E \rightarrow F$$, $$d': E' \rightarrow F'$$, $$d'': E'' \rightarrow F''$$ of degree $$\delta$$ graded $$A$$-module homomorphisms satisfying the condition

$$d''(xx') = (dx)x' + \varepsilon(\delta, \deg(x))x(d'x')$$

is called a degree $$\delta$$ *$$(A, \varepsilon)$$-derivation* (or simply an *$$\varepsilon$$-derivation*) from $$(E, E', E'')$$ to $$(F, F', F'')$$. If $$\varepsilon$$ is always $$1$$, so that $$\varepsilon$$ can be omitted from the above formula, we simply call $$(d,d',d'')$$ a *derivation*.

</div>

To avoid confusion in the above definition, it is helpful to check where each term belongs; for example, the term $$(dx)x'$$ on the right-hand side is the element of $$F''$$ obtained by multiplying $$dx\in F$$ and $$x'\in E'$$ via $$\lambda_1$$. However, in practice we are interested in the following two special cases.

1. $$E=F$$, $$E'=F'$$, $$E''=F''$$, and the three bilinear maps $$ \mu, \lambda_1, \lambda_2 $$ are all the same.
2. $$E=E'=E''$$, $$F=F'=F''$$, so that $$E$$ becomes a *graded* algebra via $$\mu:E\otimes_A E \rightarrow E$$, and

    $$\lambda_1: F \otimes_A E \to F, \qquad \lambda_2: E \otimes_A F \to F$$

    In this case, we call a single $$d:E \rightarrow F$$ satisfying the formula

    $$d(xy)=(dx)y+\varepsilon(\delta, \deg(x))x(dy)$$

    an $$\varepsilon$$-derivation from $$E$$ to $$F$$.

Taking the second case as motivation, we sometimes abuse notation and write all of $$d, d', d''$$ with the same symbol $$d$$; then the formula in [Definition 2](#def2) becomes

$$d(xx')=(dx)x'+\varepsilon(\delta,\deg(x))x (dx)$$

and this abuse of notation will not cause confusion in most cases we treat.

The situation that arises most frequently is when both of the above cases hold, i.e., $$E=E'=E''=F=F'=F''$$ and $$\lambda_1, \lambda_2$$ are multiplication in $$E$$, and the derivation is a single graded endomorphism $$d: E \rightarrow E$$. Then the $$\varepsilon$$-derivation can be regarded as a map from $$A$$ to $$A$$, so in this case we simply call it an $$\varepsilon$$-derivation of $$A$$.

Meanwhile, we noted earlier that the case $$\Delta=\mathbb{Z}$$ is our main interest; considering the non-trivial commutation factor $$\varepsilon(p,q)=(-1)^{pq}$$ in this case, we know that any even-degree $$\varepsilon$$-derivation can always ignore the effect of $$\varepsilon$$. In the odd-degree case, for any homogeneous element $$x\in E$$ the following formula

$$d(xx')=(dx)x'+(-1)^{\deg x}x(dx')$$

holds. In this case we call $$d$$ an *anti-derivation*.

## Differential Forms

To see how the preceding discussion can be applied, let us look at a simple example. Here $$\mathbb{K}$$ is a field and $$E=\mathbb{K}[\x_1,\ldots, \x_n]$$ is a polynomial algebra.

First, since a degree $$0$$ derivation can always ignore the commutation factor, if we regard $$E$$ as a non-graded $$\mathbb{K}$$-algebra and consider a derivation from $$E$$ to $$E$$, then $$\varepsilon$$ does not appear. Now, for each $$i$$, if we define $$\partial_i:E \rightarrow E$$ as the partial derivative $$\partial/\partial \x_i$$, then the Leibniz rule implies that the equality in [Definition 2](#def2) is satisfied.

Next, let us see an example of a graded algebra. For the polynomial algebra $$E$$ defined as above, let $$M$$ be the free $$A$$-module generated by the elements

$$d\x_1,d\x_2,\ldots, d\x_n$$

and consider the exterior algebra $$\bigwedge(M)$$; then this exterior algebra is a $$\mathbb{Z}$$-graded $$E$$-algebra given by

$$\bigwedge(M)=\bigoplus_{d=0}^n{\bigwedge}^d(M)$$

where $$\bigwedge^0(M)=A$$ and for each $$k$$, $$\bigwedge^k(M)$$ is the free $$E$$-module generated by elements of the form

$$d\x_J=d\x_{j_1}\wedge d\x_{j_2}\wedge\cdots\wedge d\x_{j_k},\qquad j_1<\cdots< j_k$$

([\[Multilinear Algebra\] §Tensor Algebras, ⁋Proposition 13](/en/math/multilinear_algebra/tensor_algebras#prop13)). Now, for each basis element

$$f\; d\x_{j_1}\wedge d\x_{j_2}\wedge\cdots\wedge d\x_{j_d}\in {\bigwedge}^k(M)$$

the formula

$$d(f\; d\x_{j_1}\wedge d\x_{j_2}\wedge\cdots\wedge d\x_{j_k})=\sum_{i=1}^n\frac{\partial f}{\partial \x_i}d\x_i\wedge d\x_{j_1}\wedge d\x_{j_2}\wedge\cdots\wedge d\x_{j_k}\in{\bigwedge}^{k+1}(M)$$

defines a map which extends to $$d: \bigwedge M \rightarrow \bigwedge M$$. Then $$d$$ becomes an antiderivation of degree $$1$$ on $$\bigwedge(M)$$.

## Bracket

Meanwhile, assume that the first of the two cases above holds. Then $$d=(d,d',d'')$$ can be regarded as a map from $$(E,E',E'')$$ to itself, so we may also consider the composition of $$\varepsilon$$-derivations. However, looking at the formula in [Definition 2](#def2) in general, for any two $$\varepsilon$$-derivations $$d_1,d_2$$ of degrees $$\delta_1, \delta_2$$ and any $$x\in E$$, $$x'\in E'$$,

$$\begin{aligned}(d_2\circ d_1)(xx')&=d_2((d_1x)x'+\varepsilon(\delta_1, \deg(x))x(d_1'x'))\\&=(d_2d_1x)x'+\varepsilon(\delta_2,\deg(d_1x))(d_1x)(d_2'x')+\varepsilon(\delta_1, \deg(x))(d_2x)(d_1'x')+\varepsilon(\delta_1, \deg(x))\varepsilon(\delta_2, \deg(x))x(d_2' d_1'x')\end{aligned}$$

so in general the composition of $$\varepsilon$$-derivations is not an $$\varepsilon$$-derivation. That is, in general, if we consider the category of triples of $$\Delta$$-graded $$A$$-modules and the endomorphism algebra of a fixed triple $$(E,E',E'')$$

$$\End_{\bgr_\Delta \Alg{A}^3}(E, E', E'')$$

then the collection of $$\varepsilon$$-derivations does not define a subalgebra of this endomorphism algebra. However, examining the above computation, it is also clear what kind of product must be defined on this algebra so that the collection of $$\varepsilon$$-derivations becomes closed. In other words, if we eliminate the two middle terms among the four terms on the right-hand side, then $$d_2d_1$$ would become an $$\varepsilon$$-derivation of degree $$\delta_1+\delta_2$$.

To achieve this, we first define, in the most general setting, for an arbitrary $$\Delta$$-graded algebra $$G$$ and a fixed commutation factor $$\varepsilon$$, the *$$\varepsilon$$-bracket* of two homogeneous elements $$x,y$$ of $$G$$ by the formula

$$[x,y]_\varepsilon=xy-\varepsilon(\deg(x),\deg(y))yx$$

Then through this we can define the $$\varepsilon$$-bracket in $$G=\End_{\bgr_\Delta \Alg{A}^3}(E, E', E'')$$.

<div class="proposition" markdown="1">

<ins id="prop3">**Proposition 3**</ins> Let $$d_1, d_2$$ be $$\varepsilon$$-derivations on $$(E, E', E'')$$. If their degrees are $$\delta_1, \delta_2$$, then their $$\varepsilon$$-bracket

$$[d_1, d_2]_\varepsilon = d_1 \circ d_2 - \varepsilon_{\delta_1, \delta_2} \, d_2 \circ d_1$$

is another $$\varepsilon$$-derivation of degree $$\delta_1 + \delta_2$$. In particular, if $$d$$ is an $$\varepsilon$$-derivation of degree $$\delta$$ and $$\varepsilon_{\delta, \delta} = -1$$, then $$d^2 = d \circ d$$ is a derivation.

</div>

The proof of this is obvious from the expansion of $$(d_2\circ d_1)(xx')$$ computed above.

Then, restricting especially to the case $$\Delta=\mathbb{Z}$$, the above proposition yields the following corollary.

<div class="proposition" markdown="1">

<ins id="prop4">**Corollary 4**</ins> Let $$\Delta = \mathbb{Z}$$. Then the following hold.

1. The square of an antiderivation is a derivation.  
2. The bracket of two derivations is a derivation.  
3. The bracket of an antiderivation and an even-degree derivation is an antiderivation.  
4. If $$d_1$$ and $$d_2$$ are antiderivations, then $$d_1 d_2 + d_2 d_1$$ is a derivation.

</div>

Meanwhile, considering the partial derivatives defined on the polynomial algebra, they satisfy $$\partial_i\partial_j=\partial_j\partial_i$$ for any $$i,j$$. Now, writing $$D=\partial_i+\partial_j$$ as with general differential operators and considering $$D^2$$, we can expand it as

$$D^2=(\partial_i+\partial_j)^2=\partial_i^2+\partial_i\partial_j+\partial_j\partial_i+\partial_j^2$$

and since $$\partial_i$$ and $$\partial_j$$ commute, this can be written more simply as

$$D^2=\partial_i^2+2\partial_i\partial_j+\partial_j^2$$

The following proposition generalizes this further.

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> Under the above assumptions and notation, suppose a polynomial $$F \in A[\x_1, \dots, \x_k]$$ in the indeterminates $$T_1, \dots, T_n, T_1', \dots, T_n'$$ is given. That is, $$F(T)$$ and $$F(T')$$ denote

$$F(T) = F(T_1, \dots, T_n), \qquad F(T') = F(T_1', \dots, T_n')$$

respectively. Similarly, define

$$F(T + T') = F(T_1 + T_1', \dots, T_n + T_n')$$

Now, if a polynomial $$P$$ satisfies the formula

$$P(T + T') = \sum_i Q_i(T) R_i(T')$$

then for any $$x\in E$$, $$x\'\in E'$$ the formula

$$P(D)(x x') = \sum_i (Q_i(D) x)(R_i(D) x')$$

holds.

</div>

## Derivations of $$A$$-Algebras

We now examine the second of the two special cases discussed after [Definition 2](#def2). That is, let $$E$$ be a $$\Delta$$-graded $$A$$-algebra, $$F$$ a graded $$A$$-module, and suppose two multiplications $$E\otimes_AF \rightarrow F$$ and $$F\otimes_AE \rightarrow F$$ are given.

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6**</ins> For an $$\varepsilon$$-derivation $$d:E \to F$$ of degree $$\delta$$, the kernel $$\ker(d)$$ is a graded subalgebra of $$E$$, and if $$E$$ has a unity then $$1 \in \ker(d)$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, since it is obvious that $$\ker(d)$$ is an $$A$$-submodule of $$E$$, it suffices to show that $$\ker(d)$$ is closed under multiplication. For any homogeneous $$x, y \in \ker(d)$$,

$$d(xy) = (dx)y + \varepsilon(\delta, \deg(x))x(dy) = 0$$

we have $$xy \in \ker(d)$$. Hence $$\ker(d)$$ is a graded subalgebra.

Now, if $$E$$ has a unity, then $$1$$ has degree $$0$$, so

$$d(1) = d(1 \cdot 1) = (d1) \cdot 1 + \varepsilon_{\delta, 0} \cdot 1 \cdot (d1) = d1 + d1 = 2d1$$

and thus we see that $$d(1) = 0$$.

</details>

Therefore, if $$d_1,d_2$$ are $$\varepsilon$$-derivations of degree $$\delta$$ from $$E$$ to $$F$$ and they agree on the generators of $$E$$ as an $$A$$-algebra, then $$d_1=d_2$$. Meanwhile, the following holds for inverses.

<div class="proposition" markdown="1">

<ins id="prop7">**Proposition 7**</ins> Let $$E$$ be a unital $$\Delta$$-graded $$A$$-algebra and let $$d:E \to F$$ be an $$\varepsilon$$-derivation of degree $$\delta$$. If $$x$$ is an invertible homogeneous element of $$E$$, then for its inverse $$x^{-1}$$ the following formula

$$d(x^{-1}) = -\varepsilon_{\delta, \deg(x)} x^{-1}(d(x))x^{-1}
= -\varepsilon_{\delta, \deg(x)} (d(x)) x^{-2}$$

holds.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

By [Proposition 5](#prop5), $$d(1) = 0$$, so

$$0 = d(xx^{-1}) = d(x))x^{-1} + \varepsilon_{\delta, \deg(x)}x(d(x^{-1})$$

Multiplying both sides on the left by $$x^{-1}$$,

$$0 = x^{-1}(d(x))x^{-1} + \varepsilon_{\delta, \deg(x)} d(x^{-1})$$

and rearranging,

$$d(x^{-1}) = -\varepsilon_{\delta, \deg(x)} x^{-1}(d(x))x^{-1}.
$$

we obtain the first equality. Moreover, using that the degree of $$x^{-1}$$ is $$-\deg(x)$$ and computing $$d(x^{-1}x)$$, we obtain the second equality.

</details>

<div class="proposition" markdown="1">

<ins id="prop8">**Proposition 8**</ins> Let $$E$$ be an $$A$$-algebra that is an integral domain, and consider its field of fractions $$K=\Frac E$$. Regarding any $$K$$-vector space $$F$$ as an $$E$$-module and considering an $$A$$-derivation $$d:E \rightarrow F$$, then $$d$$ extends uniquely to an $$A$$-derivation from $$K$$ to $$F$$.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

Suppose an arbitrary derivation $$d:E \rightarrow f$$ is given, and assume that an extension $$\bar{d}$$ of $$d$$ to $$K$$ exists. Then applying [Proposition 7](#prop7), the following formula

$$\bar{d}(u/v) = v^{-1} d(u) - v^{-2} u\, d(v)$$

must hold, and therefore if $$\bar{d}$$ exists its expression is unique.

Let us show that this definition does not depend on the choice of representation $$u/v$$. That is, even when $$u/v = u'/v'$$,

$$v^{-1} d(u) - v^{-2} u\, d(v) = v'^{-1} d(u') - v'^{-2} u'\, d(v')$$

must hold.

Set $$uv' = u'v$$. Applying $$d$$ to both sides,

$$v' d(u) + u\, d(v') = v\, d(u') + u'\, d(v)$$

and multiplying both sides by $$vv'$$,

$$v v' d(u) - u\, v\, d(v') = v v' d(u') - u'\, v'\, d(v)$$

we obtain, upon rearrangement,

$$v' d(u) - v^{-1} u\, d(v) = v' d(u') - v'^{-1} u'\, d(v')$$

holds. Thus the definition is well defined independent of the expression of the element $$u/v$$. Now, that $$\bar{d}$$ actually satisfies the conditions of an $$A$$-derivation from $$K$$ to $$F$$ is a straightforward computation.

</details>

In the next proposition, for notational convenience, define

$$Z_\varepsilon=\{a\in A\mid \text{$xa_d=\varepsilon(\deg(a),\deg(x))a_dx$ for all homogeneous component $a_d$ of $a$ and for all homogeneous $x\in E$.}\}$$

for any $$\varepsilon$$-derivation $$d:A \rightarrow E$$ of degree $$\delta$$.

<div class="proposition" markdown="1">

<ins id="prop9">**Proposition 9**</ins> Let $$A$$ be a unital graded associative $$A$$-algebra and let $$E$$ be a graded $$(A, A)$$-bimodule. Now let $$d: A \to E$$ be an $$\varepsilon$$-derivation of degree $$\delta$$, and let $$a$$ be a homogeneous element of degree $$\alpha$$ of $$Z_\varepsilon$$. Then the morphism

$$x \mapsto a (d x)$$

is an $$\varepsilon$$-derivation of degree $$\delta + \alpha$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Denoting the given morphism by $$d'$$, this morphism is obviously $$A$$-linear. To show that $$d'$$ is an $$\varepsilon$$-derivation, for any homogeneous element $$x$$ of degree $$\delta'$$ and any $$y\in A$$,

$$\begin{aligned}d'(xy)&=a(dx)y+\varepsilon(\delta, \delta')a(x(dy))\\&=a(dx)y+\varepsilon(\delta, \delta')\varepsilon(\alpha,\delta')xa(dy)\\&=(d'x)y+\varepsilon(\delta+\alpha,\delta')x(d'y)\end{aligned}$$

and therefore $$d'$$ becomes an $$\varepsilon$$-derivation of degree $$\delta + \alpha$$.

</details>

Meanwhile, if $$E$$ is a $$\Delta$$-graded (associative) $$A$$-algebra equipped with an $$\varepsilon$$-bracket, then there exists a natural $$\varepsilon$$-derivation on it.

<div class="definition" markdown="1">

<ins id="def10">**Definition 10**</ins> For a homogeneous element $$z\in E$$ of a graded $$A$$-algebra, we write the morphism

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

1. Suppose $$d$$ is an $$\varepsilon$$-derivation of degree $$\delta$$ and let $$\zeta = \deg(z)$$. Now set $$f = [d, \ad(z)]_\varepsilon$$; then for every homogeneous element $$x \in A$$ of degree $$\xi$$,

    $$\begin{aligned}f(x)&=d(z x - \varepsilon(\zeta, \xi) x z) - \varepsilon(\delta, \zeta) (z (dx) - \varepsilon(\zeta, \delta+\xi) (dx) z) \\&= d(z x) - \varepsilon(\zeta, \xi) d(x z) - \varepsilon(\delta, \zeta) z (dx) + \varepsilon(\zeta,2.\delta+\xi) d(x) z \\&=(dz)x+\varepsilon(\delta, \zeta)z(dx)-\varepsilon(\zeta,\xi)((dx)z+\varepsilon(\delta, \xi)x(dz))- \varepsilon(\delta, \zeta) z (dx) + \varepsilon(\zeta,2.\delta+\xi) (dx) z\\&=(dz)x+\varepsilon(\delta,\zeta)z(dx)-\varepsilon(\zeta,\xi)(dx)z-\varepsilon(\delta+\zeta,\xi)x(dz)-\varepsilon(\delta,\zeta)z (dx)+\varepsilon(\zeta,\xi)(dx)z\\&=(dz)x-\varepsilon(\delta+\zeta,\xi)x(dz)=[dz,x]_\varepsilon=\ad_\varepsilon(dz)(x)\end{aligned}$$

    thus we obtain the desired result.
2. For every homogeneous element $$x \in A$$ of degree $$\xi$$ and homogeneous element $$y \in A$$ of degree $$\eta$$,
    
    $$\begin{aligned}\ad(z)(x y) &= z(x y) - \varepsilon(\zeta, \xi + \eta)(x y) z \\&= (z x) y - \varepsilon(\zeta, \xi) x z y + \varepsilon(\zeta, \xi) x z y - \varepsilon(\zeta, \xi + \eta) x y z \\&= (ax-\varepsilon(\zeta,\xi xz)y+\varepsilon(zeta,\xi)x(ay-\varepsilon(\zeta,\eta)ya)\\&=\ad(z)(x) \cdot y + \varepsilon(\zeta, \xi) x \cdot \ad(z)(y)\end{aligned}$$

    holds.

</details>

Therefore, if $$E$$ is an associative graded $$A$$-algebra, then through [Definition 10](#def10) any homogeneous element of $$E$$ defines an $$\varepsilon$$-derivation from $$E$$ to itself, and we call this an *inner $$\varepsilon$$-derivation*.

When this holds, substituting an inner $$\varepsilon$$-derivation for $$d$$ in the above formula yields the following corollary.

<div class="proposition" markdown="1">

<ins id="cor12">**Corollary 12**</ins> For two homogeneous elements $$x,y$$ of an associative graded algebra $$E$$, the formula

$${[\ad_\varepsilon(x), \ad_\varepsilon(y)]_\varepsilon = \ad_\varepsilon([x,y]_\varepsilon)}$$

always holds.

</div>

Moreover, since the equality in the above corollary can be obtained by verifying it for any homogeneous $$z\in E$$, if $$x,y,z$$ are homogeneous elements of degrees $$\xi,\eta,\zeta$$ respectively, then the formula

$${\varepsilon}_{\xi, \zeta} [[x, [y,z]_{\varepsilon}]_{\varepsilon} + \varepsilon_{\eta,\xi} [y, [z,x]_{\varepsilon}]_{\varepsilon} + \varepsilon_{\zeta,\eta} [z, [x,y]_{\varepsilon}]_{\varepsilon} = 0$$

holds, and we call this the *Jacobi identity*.
