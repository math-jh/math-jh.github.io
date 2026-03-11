---

title: "Change of Base Ring"
excerpt: ""

categories: [Math / Algebraic Structures]
permalink: /en/math/algebraic_structures/change_of_base_ring
header:
    overlay_image: /assets/images/Math/Algebraic_Structures/Change_of_base_ring.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_structures-en"

date: 2026-03-11
last_modified_at: 2026-03-11
weight: 203

---

In this article, we examine methods to convert $$A$$-modules to $$B$$-modules or vice versa via a ring homomorphism $$\phi:A \rightarrow B$$. Therefore, since abbreviating scalar multiplication and operations as before could cause confusion, we will denote multiplication maps as before by omitting $$\cdot$$, and denote actions by $$\cdot$$ (or $$\cdot_A$$ and $$\cdot_B$$).

## Restriction of Scalars

Let a $$B$$-module $$\rho_N:B\otimes N \rightarrow N$$ be given. Then considering the composition

![restriction_of_scalars](/assets/images/Math/Algebraic_Structures/Change_of_base_ring-1.png){:style="width:14em" class="invert" .align-center}

the map $$\phi^\ast\rho_N:A\otimes N \rightarrow N$$ satisfies all the conditions that an action must satisfy, and thus defines an $$A$$-module structure on $$N$$. Moreover, considering the diagram

![restriction_of_scalars_functoriality](/assets/images/Math/Algebraic_Structures/Change_of_base_ring-2.png){:style="width:16em" class="invert" .align-center}

we see that this correspondence of $$A$$-modules is functorial.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> For a ring homomorphism $$\phi:A \rightarrow B$$, the functor defined as above is denoted by $$\phi^\ast: \lMod{B} \rightarrow \lMod{A}$$ and called the *restriction of scalars*.

</div>

That is, this is simply defining the action of $$A$$ on $$N$$ by using a given $$B$$-module $$\rho_N: B\otimes N \rightarrow N$$:

$$\alpha\cdot_A y:=\phi(\alpha)\cdot_B y$$

Consider in particular the case $$N=B$$. As sets, $$\phi^\ast B$$ and $$B$$ are identical, so we can verify the relationship between the original ring homomorphism $$\phi:A \rightarrow B$$ and the action of $$\phi^\ast B$$; in this case, we can verify that $$\phi$$ becomes an $$A$$-linear map.

<div class="example" markdown="1">

<ins id="ex2">**Example 2**</ins> The forgetful functor $$U: \lMod{B} \rightarrow\Ab$$ is induced by the (unique) ring homomorphism $$\mathbb{Z}\rightarrow B$$.

</div>

## Extension of Scalars

We will now define two functors from $$\lMod{A}$$ to $$\lMod{B}$$. For convenience, fix an $$A$$-module $$M$$.

Consider the tensor product $$\phi^\ast B\otimes_AM$$ of the two $$A$$-modules $$\phi^\ast B$$ and $$M$$. On this, we can define an action $$\cdot_B$$ of $$B$$ by the formula

$$\beta'\cdot_B(\beta\otimes_A x)=(\beta'\beta)\otimes_A x$$

That this is indeed an action can be obtained through straightforward calculation, or can be thought of as obtained from the composition

$$B\otimes_\mathbb{Z}(\phi^\ast B\otimes_AM)\cong (B\otimes_\mathbb{Z}\phi^\ast B)\otimes_AM \overset{\mu_B}{\longrightarrow} \phi^\ast B\otimes_AM$$[^1]. Also, for any $$A$$-linear map $$u:M \rightarrow M'$$, we can verify that $$\id_{\phi^\ast B}\otimes_A u$$ defines a $$B$$-linear map between the two $$B$$-modules thus defined.

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> The functor $$\phi^\ast B\otimes_A-:\lMod{A} \rightarrow \lMod{B}$$ defined above is simply denoted by $$\phi_!$$ and called the *extension of scalars*.

</div>

## Coextension of Scalars

As before, fix an $$A$$-module $$M$$. This time, we consider homomorphisms between the two $$A$$-modules $$\phi^\ast B$$ and $$M$$. Define a $$B$$-module structure on the abelian group

$$\Hom_A(\phi^\ast B,M)$$

by

$$\beta\cdot g: (\beta'\mapsto g(\beta'\beta))$$

For any $$\alpha\in A$$ and any $$\beta'\in \phi^\ast B$$,

$$(\beta\cdot g)(\alpha\cdot \beta')=g(\phi(\alpha)\beta'\beta)=g(\alpha\cdot(\beta'\beta))=\alpha\cdot g(\beta'\beta)=\alpha\cdot (\beta\cdot g)(\beta')$$

so $$\beta\cdot g$$ is also an $$A$$-linear map. Through some calculation, we can verify that this is also functorial, and thus the following is defined.

<div class="definition" markdown="1">

<ins id="def4">**Definition 4**</ins> The functor $$\Hom_A(\phi^\ast B,-): \lMod{A} \rightarrow \lMod{B}$$ is called the *coextension of scalars* and denoted by $$\phi_\ast$$.

</div>

## Adjoint Functors

There are certain adjoint relationships among the three functors defined above. First, we show the following lemma.

<div class="proposition" markdown="1">

<ins id="lem5">**Lemma 5**</ins> For a right $$B$$-module $$N_1$$ and a left $$B$$-module $$N_2$$, consider the two abelian groups $$\phi^\ast N_1\otimes_A \phi^\ast N_2$$ and $$N_1\otimes_B N_2$$. Then there exists a unique bilinear map $$\Phi:\phi^\ast N_1\otimes_A \phi^\ast N_2 \rightarrow N_1\otimes_BN_2$$ such that any $$y_1\otimes_A y_2\in \phi^\ast N_1\otimes_A\phi^\ast N_2$$ is sent to $$y_1\otimes_B y_2\in N_1\otimes_BN_2$$.

If $$A$$ is a commutative ring, then $$\Phi$$ becomes an $$A$$-linear map $$\phi^\ast N_1\otimes_A\phi^\ast N_2 \rightarrow\phi^\ast(N_1\otimes_BN_2)$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Define the function from $$\phi^\ast N_1\times\phi^\ast N_2$$ to $$N_1\otimes_B N_2$$ by $$(y_1,y_2)\mapsto y_1\otimes_B y_2$$, and show that this behaves well with respect to the scalar multiplication of $$A$$. Since the scalar multiplication of $$A$$ on $$\phi^\ast N_1,\phi^\ast N_2$$ is defined as a $$B$$-action via $$\phi(\alpha)$$, for any $$\alpha\in A$$,

$$(\alpha\cdot_A y_1,y_2)=(\phi(\alpha)\cdot_B y_1, y_2)\mapsto (\phi(\alpha)\cdot_B y_1)\otimes_B y_2=y_1\otimes_B(\phi(\alpha)\cdot_B y_1)$$

holds, and therefore $$(\alpha\cdot_A y_1,y_2)$$ and $$y_1,\alpha\cdot_Ay_2$$ are sent to the same element, so the proof is complete by the universal property of tensor products.

</details>

The following propositions can be proved in the general case, but for convenience, we assume that $$A, B$$ are both commutative rings.

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> An adjunction $$\phi_!\dashv\phi^\ast$$ exists.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Fix arbitrary $$A$$-module $$M$$ and $$B$$-module $$N$$. First, for any $$v\in\Hom_B(\phi_!M,N)$$, the composition of functions

![Adjointness-1](/assets/images/Math/Algebraic_Structures/Change_of_base_ring-3.png){:style="width:21em" class="invert" .align-center}

gives a function $$M \rightarrow N$$. Here, $$M \rightarrow A\otimes_AM \rightarrow \phi^\ast B\otimes_AM$$ is a composition of $$A$$-linear maps, and $$v:\phi^\ast B\otimes M \rightarrow N$$ is a $$B$$-linear map. First, for any $$\alpha\in A$$ and $$x\in M$$, looking at the composition of $$A$$-linear maps,

$$\alpha\cdot_Ax\mapsto \alpha\otimes_A x\mapsto \phi(\alpha)\otimes_A x$$

and for the $$B$$-linear map $$f$$, using

$$\phi(\alpha)\otimes_A x=(\phi(\alpha)1)\otimes_A x=\phi(\alpha)\cdot_B(1\otimes_A x)$$

we have

$$v(\phi(\alpha)\otimes_A x)=v(\phi(\alpha)\cdot_B(1\otimes_A x))=\phi(\alpha)\cdot_B v(1\otimes_A x)$$

That is, regarding $$N$$ as an $$A$$-module through restriction of scalars, we see that the above composition is an $$A$$-linear map.

Conversely, let any $$u\in\Hom_A(M, \phi^\ast N)$$ be given. Then the composition

![Adjointness-2](/assets/images/Math/Algebraic_Structures/Change_of_base_ring-4.png){:style="width:28em" class="invert" .align-center}

gives a function $$\phi_!M \rightarrow N$$. For any $$\beta'\in B$$ and $$\beta\otimes_A x\in \phi^\ast B\otimes_AM$$,

$$\Phi(\id_{\phi^\ast B}\otimes_A u(\beta'\cdot_B(\beta\otimes_Ax)))=\Phi((\beta'\beta)\otimes_Ax)=(\beta'\beta)\otimes_B x$$

and this is sent to $$(\beta'\beta)\cdot_Bx=\beta'\cdot_B(\beta\cdot_Bx)$$ via $$B\otimes_BN\cong N$$. That is, the function defined above is a $$B$$-linear map.

We can now verify that the two functions defined above are inverses of each other, and moreover, that they define a natural equivalence.

</details>

Also, the following adjoint pair can be proved in a similar way.

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6**</ins> An adjunction $$\phi^\ast\dashv\phi_\ast$$ exists.

</div>

Thus $$\phi^\ast:\lMod{B} \rightarrow\lMod{A}$$ is both a left adjoint and a right adjoint, and therefore commutes with all limits and colimits.

[^1]: Strictly speaking, to make the first isomorphism in this formula meaningful, we need to use the fact that $$B$$ is an $$(A,\mathbb{Z})$$-bimodule.

