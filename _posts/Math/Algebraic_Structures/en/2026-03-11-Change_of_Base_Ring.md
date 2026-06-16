---
title: "Change of Base Ring"
excerpt: "Restriction and extension of scalars via a ring homomorphism"

categories: [Math / Algebraic Structures]
permalink: /en/math/algebraic_structures/change_of_base_ring
sidebar: 
    nav: "algebraic_structures-en"

date: 2026-03-11
weight: 203
translated_at: 2026-05-29T16:03:58+00:00
translation_source: kimi-cli
last_polished_at: 2026-05-24T23:30:03+00:00
---
In this article, we examine how to change an $$A$$-module into a $$B$$-module, or a $$B$$-module into an $$A$$-module, via a ring homomorphism $$\phi:A \rightarrow B$$. Hence, abbreviating scalar multiplication and operations as we did before may lead to confusion; we therefore continue to omit $$\cdot$$ for multiplication maps, and denote actions by $$\cdot$$ (or $$\cdot_A$$ and $$\cdot_B$$).

## Restriction of Scalars

Let a $$B$$-module $$\rho_N:B\otimes N \rightarrow N$$ be given. Then, considering the composition

![restriction_of_scalars](/assets/images/Math/Algebraic_Structures/Change_of_Base_Ring-1.svg){:style="width:14.53em" class="invert" .align-center}

the map $$\phi^\ast\rho_N:A\otimes N \rightarrow N$$ satisfies all the conditions required of an action, and thus defines an $$A$$-module structure on $$N$$. Moreover, considering the diagram

![restriction_of_scalars_functoriality](/assets/images/Math/Algebraic_Structures/Change_of_Base_Ring-2.svg){:style="width:16.59em" class="invert" .align-center}

we see that this assignment of an $$A$$-module is functorial.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> For a ring homomorphism $$\phi:A \rightarrow B$$, the functor defined above is denoted by $$\phi^\ast: \lMod{B} \rightarrow \lMod{A}$$ and called the *restriction of scalars*.

</div>

In other words, given any $$B$$-module $$\rho_N: B\otimes N \rightarrow N$$, we simply define an action of $$A$$ on $$N$$ by the formula

$$\alpha\cdot_A y:=\phi(\alpha)\cdot_B y$$

In particular, consider the case $$N=B$$. Since $$\phi^\ast B$$ and $$B$$ coincide as sets, we can compare the original ring homomorphism $$\phi:A \rightarrow B$$ with the action on $$\phi^\ast B$$; here we find that $$\phi$$ is an $$A$$-linear map.

<div class="example" markdown="1">

<ins id="ex2">**Example 2**</ins> The forgetful functor $$U: \lMod{B} \rightarrow\Ab$$ is induced by the (unique) ring homomorphism $$\mathbb{Z}\rightarrow B$$.

</div>

## Extension of Scalars

We now define two functors from $$\lMod{A}$$ to $$\lMod{B}$$. For convenience, fix an $$A$$-module $$M$$.

Consider the tensor product $$\phi^\ast B\otimes_AM$$ of the two $$A$$-modules $$\phi^\ast B$$ and $$M$$. We define a $$B$$-action $$\cdot_B$$ on it by the formula

$$\beta'\cdot_B(\beta\otimes_A x)=(\beta'\beta)\otimes_A x$$

That this defines an action is readily verified by direct computation, or can be understood as arising from the composition

$$B\otimes_\mathbb{Z}(\phi^\ast B\otimes_AM)\cong (B\otimes_\mathbb{Z}\phi^\ast B)\otimes_AM \overset{\mu_B}{\longrightarrow} \phi^\ast B\otimes_AM$$[^1]. Furthermore, for any $$A$$-linear map $$u:M \rightarrow M'$$, we verify that $$\id_{\phi^\ast B}\otimes_A u$$ is a $$B$$-linear map between the $$B$$-modules defined above.

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> The functor $$\phi^\ast B\otimes_A-:\lMod{A} \rightarrow \lMod{B}$$ defined above is simply denoted by $$\phi_!$$ and called the *extension of scalars*.

</div>

## Coextension of Scalars

As before, fix an $$A$$-module $$M$$. This time we consider homomorphisms between the two $$A$$-modules $$\phi^\ast B$$ and $$M$$. We define a $$B$$-module structure on the abelian group

$$\Hom_A(\phi^\ast B,M)$$

by

$$\beta\cdot g: (\beta'\mapsto g(\beta'\beta))$$

For any $$\alpha\in A$$ and any $$\beta'\in \phi^\ast B$$,

$$(\beta\cdot g)(\alpha\cdot \beta')=g(\phi(\alpha)\beta'\beta)=g(\alpha\cdot(\beta'\beta))=\alpha\cdot g(\beta'\beta)=\alpha\cdot (\beta\cdot g)(\beta')$$

so $$\beta\cdot g$$ is also an $$A$$-linear map. A short calculation shows that this is functorial as well, yielding the following definition.

<div class="definition" markdown="1">

<ins id="def4">**Definition 4**</ins> The functor $$\Hom_A(\phi^\ast B,-): \lMod{A} \rightarrow \lMod{B}$$ is called the *coextension of scalars* and written $$\phi_\ast$$.

</div>

## Adjoint Functors

The three functors defined above are related by certain adjunctions. We first establish the following lemma.

<div class="proposition" markdown="1">

<ins id="lem5">**Lemma 5**</ins> Let $$N_1$$ be a right $$B$$-module and $$N_2$$ a left $$B$$-module, and consider the two abelian groups $$\phi^\ast N_1\otimes_A \phi^\ast N_2$$ and $$N_1\otimes_B N_2$$. Then there is a unique bilinear map $$\Phi:\phi^\ast N_1\otimes_A \phi^\ast N_2 \rightarrow N_1\otimes_BN_2$$ sending each $$y_1\otimes_A y_2\in \phi^\ast N_1\otimes_A\phi^\ast N_2$$ to $$y_1\otimes_B y_2\in N_1\otimes_BN_2$$.

If $$A$$ is a commutative ring, then $$\Phi$$ is an $$A$$-linear map $$\phi^\ast N_1\otimes_A\phi^\ast N_2 \rightarrow\phi^\ast(N_1\otimes_BN_2)$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Define a map $$\phi^\ast N_1\times\phi^\ast N_2 \rightarrow N_1\otimes_B N_2$$ by $$(y_1,y_2)\mapsto y_1\otimes_B y_2$$, and verify that it is balanced with respect to the $$A$$-action. Since the $$A$$-action on $$\phi^\ast N_1,\phi^\ast N_2$$ is given by the $$B$$-action through $$\phi(\alpha)$$, for any $$\alpha\in A$$,

$$(\alpha\cdot_A y_1,y_2)=(\phi(\alpha)\cdot_B y_1, y_2)\mapsto (\phi(\alpha)\cdot_B y_1)\otimes_B y_2=y_1\otimes_B(\phi(\alpha)\cdot_B y_1)$$

holds, and therefore $$(\alpha\cdot_A y_1,y_2)$$ and $$y_1,\alpha\cdot_Ay_2$$ are sent to the same element; the claim follows from the universal property of the tensor product.

</details>

The following propositions hold in the general case as well, but for convenience we assume that $$A$$ and $$B$$ are both commutative rings.

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6**</ins> An adjunction $$\phi_!\dashv\phi^\ast$$ exists.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Fix arbitrary $$A$$-module $$M$$ and $$B$$-module $$N$$. First, for any $$v\in\Hom_B(\phi_!M,N)$$, consider the composition of maps

![Adjointness-1](/assets/images/Math/Algebraic_Structures/Change_of_Base_Ring-3.svg){:style="width:22.24em" class="invert" .align-center}

yields a map $$M \rightarrow N$$. Here $$M \rightarrow A\otimes_AM \rightarrow \phi^\ast B\otimes_AM$$ is a composite of $$A$$-linear maps, while $$v:\phi^\ast B\otimes M \rightarrow N$$ is a $$B$$-linear map.

Now, for any $$\alpha\in A$$ and $$x\in M$$, the composite of the $$A$$-linear maps is

$$\alpha\cdot_Ax\mapsto \alpha\otimes_A x\mapsto \phi(\alpha)\otimes_A x$$

and for the $$B$$-linear map $$v$$, using

$$\phi(\alpha)\otimes_A x=(\phi(\alpha)1)\otimes_A x=\phi(\alpha)\cdot_B(1\otimes_A x)$$

we have

$$v(\phi(\alpha)\otimes_A x)=v(\phi(\alpha)\cdot_B(1\otimes_A x))=\phi(\alpha)\cdot_B v(1\otimes_A x)$$

Thus, viewing $$N$$ as an $$A$$-module via restriction of scalars, we see that the above composition is an $$A$$-linear map.

Conversely, given any $$u\in\Hom_A(M, \phi^\ast N)$$, consider the composition

![Adjointness-2](/assets/images/Math/Algebraic_Structures/Change_of_Base_Ring-4.svg){:style="width:30.40em" class="invert" .align-center}

yields a map $$\phi_!M \rightarrow N$$. Then for any $$\beta'\in B$$ and $$\beta\otimes_A x\in \phi^\ast B\otimes_AM$$,

$$\Phi(\id_{\phi^\ast B}\otimes_A u(\beta'\cdot_B(\beta\otimes_Ax)))=\Phi((\beta'\beta)\otimes_Ax)=(\beta'\beta)\otimes_B x$$

and under the isomorphism $$B\otimes_BN\cong N$$ this corresponds to $$(\beta'\beta)\cdot_Bx=\beta'\cdot_B(\beta\cdot_Bx)$$. Hence the map defined above is $$B$$-linear.

We now verify that the two maps defined above are mutually inverse, and moreover that they define a natural equivalence.

</details>

The following adjoint pair is proved similarly.

<div class="proposition" markdown="1">

<ins id="prop7">**Proposition 7**</ins> An adjunction $$\phi^\ast\dashv\phi_\ast$$ exists.

</div>

Thus $$\phi^\ast:\lMod{B} \rightarrow\lMod{A}$$ is both a left adjoint and a right adjoint, and therefore commutes with all limits and colimits.

[^1]: Strictly speaking, in order for the first isomorphism in this formula to make sense, we must use the fact that $$B$$ is an $$(A,\mathbb{Z})$$-bimodule.
