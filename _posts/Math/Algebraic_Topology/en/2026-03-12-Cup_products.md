---

title: "Cup Product"
excerpt: ""

categories: [Math / Algebraic Topology]
permalink: /en/math/algebraic_topology/cup_products
header:
    overlay_image: /assets/images/Math/Algebraic_Topology/Cup_products.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_topology-en"

date: 2026-03-12
last_modified_at: 2026-03-12
weight: 8

---

When we introduced cohomology earlier, we mentioned that one of the greatest advantages of cohomology is the naturally defined multiplicative structure on it. A natural question then arises: why was this structure not visible in homology? As we will see in this post, once we define this multiplicative structure, it becomes clear that this is essentially because cohomology is a contravariant functor.

## Exterior Product of Cohomology

Fix a commutative ring $$A$$, and let $$C_\bullet,D_\bullet$$ be chain complexes of $$A$$-modules. Consider their dual sequences

$$(C^\vee)^\bullet=\Hom_A(C_\bullet,A),\qquad (D^\vee)^\bullet=\Hom_A(D_\bullet,A)$$

and

$$((C\otimes D)^\vee)^\bullet=\Hom_A((C\otimes D)_\bullet,A)$$

We first define

$$\times:(C^\vee\otimes D^\vee)^\bullet\rightarrow ((C\otimes D)^\vee)^\bullet$$

To do this, we need to map a simple tensor $$\phi\otimes \psi$$ on the left-hand side to a function from $$(C\otimes D)_\bullet$$ to $$A$$, which is again determined by its values on simple tensors in $$(C\otimes D)_\bullet$$. If $$\phi\in (C^\vee)^p,\psi\in (D^\vee)^q$$, then we define this correspondence to be the function given by

$$(\phi\times\psi):(C\otimes D)_\bullet \rightarrow A;\qquad (\alpha\otimes \beta)\mapsto (-1)^{\deg(\alpha)\deg(\beta)}\phi(\alpha)\psi(\beta)$$

exactly on simple tensors $$\alpha\otimes \beta$$ belonging to $$C_p\otimes D_q$$, and zero elsewhere. It is then not difficult to verify that this is a morphism between cochain complexes, and thus $$\times$$ defines a map on cohomology

$$\bar{\times}: H^\bullet(C^\vee\otimes D^\vee)\rightarrow (H(C^\vee)\otimes H(D^\vee))^\bullet\rightarrow H^\bullet((C\otimes D)^\vee)$$

Now suppose we are given $$A$$-valued chains

$$C_\bullet(X;A),\qquad C_\bullet(Y;A)$$

of two topological spaces $$X,Y$$. Setting $$C_\bullet=C_\bullet(X;A), D_\bullet=C_\bullet(Y;A)$$ and applying the above cochain map, we compose this with the map induced by the Alexander-Whitney map $$\AW$$ from [§Cohomology](/en/math/algebraic_topology/cohomology) to obtain the following cochain map

$$(C^\vee(X;A)\otimes C^\vee(Y;A))^\bullet \overset{\times}{\longrightarrow} \Hom_A(C_\bullet(X;A)\otimes C_\bullet(Y;A),A)\overset{\Hom(\AW,A)}{\longrightarrow} \Hom_A(C_\bullet(X\times Y;A),A)=(C^\vee)^\bullet(X\times Y)$$

and passing to the cohomology level, we obtain for each $$(p,q)$$ the following $$A$$-module homomorphism

$${\AW^\ast}\circ{(-\mathbin{\bar{\times}}-)}:H^p(X;A)\otimes_A H^q(Y;A)\rightarrow H^{p+q}(X\times Y;A)$$

When there is no risk of confusion, we will simply denote this by $$\times$$.

## Definition and Basic Properties of the Cup Product

We can now define the cup product.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> For a commutative ring $$A$$ and a topological space $$X$$, the composition

$${\smile}:H^\bullet(X;A)\otimes_A H^\bullet(X;A)\overset{\AW^\ast\circ\bar{\times}}{\longrightarrow}H^\bullet(X\times X)\overset{\Delta^\ast}{\longrightarrow} H^\bullet(X)$$

is called the *cup product* on $$H^\bullet(X;A)$$.

</div>

At this stage, it becomes apparent why the cup product was not explicitly visible in homology. Using the Eilenberg-Zilber map, we could construct

$$H_p(X;A)\otimes_A H_q(X;A)\rightarrow H_{p+q}(X\times X;A)$$

but applying the homology functor to the diagonal map $$\Delta:X\rightarrow X\times X$$ is covariant, so the direction would not match.

Explicitly, for any $$\alpha\in H^p(X;A)$$, $$\beta\in H^q(X;A)$$, the element $$\alpha\smile\beta\in H^{p+q}(X;A)$$ is given on any chain $$\sigma:\Delta^{p+q}\rightarrow X$$ by the formula

$$(\alpha\smile\beta)(\sigma)=(\Delta^\ast\AW^\ast(\alpha\mathbin{\bar{\times}}\beta))(\sigma)=(\alpha\mathbin{\bar{\times}}\beta)(\AW(\Delta(\sigma)))=(-1)^{pq}\alpha(\text{front face of $\sigma$})\beta(\text{back face of $\sigma$})$$

As this explicit calculation shows, in de Rham cohomology, the cup product is quite familiar: it corresponds to the wedge product of differential forms.

As the name suggests, the cup product defines a multiplicative structure on the cohomology ring. However, since $$H^\bullet(X;A)$$ is also a graded ring, we must be careful when discussing the commutativity of multiplication defined on it.

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> Fix a topological space $$X$$ and a commutative ring $$A$$. Then

$$(H^\bullet(X;A), {\smile}, 1)$$

forms a graded-commutative, $$\mathbb{N}$$-graded $$A$$-algebra. Here, $$1\in H^0(X;A)$$ is the cocycle that sends every $$\Delta$$-simplex of $$X$$ to $$1\in A$$.

</div>

In other words, for homogeneous cycles $$\alpha\in H^p(X;A),\beta\in H^q(X;A),\gamma\in H^r(X;A)$$, we have

- (Unit) $$1\smile\alpha=\alpha\smile 1=\alpha$$
- (Associativity) $$(\alpha\smile\beta)\smile\gamma=\alpha\smile(\beta\smile\gamma)$$
- (Graded-commutativity) $$\alpha\smile\beta=(-1)^{pq}\beta\smile\alpha$$

To prove this, naturally, we apply [§Acyclic models theorem, ¶Theorem 3](/en/math/algebraic_topology/acyclic_models_theorem#thm3) to functors from $$\Top^2$$ (or $$\Top^3$$) to $$\Ch_{\geq 0}(\lMod{A})$$.

## Functorial Properties of the Cup Product

The property proved above shows that the objects of the functor $$H^\bullet(-;A)$$, while initially defined as a functor to $$\lMod{A}$$, ultimately arrive at $$\gr_{\mathbb{N}}\Alg{A}$$. It is then natural to ask whether $$H^\bullet(-;A)$$ is a functor from $$\Top$$ to $$\gr_\mathbb{N}\Alg{A}$$.

<div class="proposition" markdown="1">

<ins id="prop3">**Proposition 3**</ins> For any topological spaces $$X,Y$$ and any commutative ring $$A$$,

$$\times: H^*(X;A)\otimes_A H^*(Y;A) \to H^*(X\times Y;A)$$

is a graded $$A$$-algebra homomorphism.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

That is, what we need to show is the commutativity of the following diagram

![functoriality_of_cup_products](/assets/images/Math/Algebraic_Topology/Cup_products-1.png){:style="width:40em" class="invert" .align-center}

For any $$\alpha_1,\alpha_2\in H^\ast(X;A)$$ and any $$\beta_1,\beta_2\in H^\ast(Y;A)$$, we have

$$(\alpha_1\times\beta_1)(\alpha_2\times\beta_2)=\Delta_{X\times Y}^\ast ((\alpha_1\times\beta_1)\times(\alpha_2\times\beta_2))$$

and since the right-hand side is of the form $$\alpha_1\times\beta_1\times\alpha_2\times\beta_2$$, we can regroup it appropriately. That this is a graded homomorphism and preserves $$1$$ is clear.

</details>

Using this, we can also establish the functoriality of the cup product.

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4**</ins> For a continuous map $$f:X \rightarrow Y$$, the map $$f^\ast=H^\bullet(f;A):H^\bullet(Y;A)\rightarrow H^\bullet(X;A)$$ induced by the cohomology functor is a morphism of graded $$A$$-algebras. That is, the following equation

$$f^\ast(\alpha\smile\beta)=(f^\ast\alpha)\smile(f^\ast\beta)$$

holds.

</div>

The proof of this proposition follows from the fact that by [Proposition 3](#prop3), we know the following diagram

![functoriality_1](/assets/images/Math/Algebraic_Topology/Cup_products-2.png){:style="width:20em" class="invert" .align-center}

commutes, so we just need to apply the cohomology functor to the following diagram

![diagonals_and_f](/assets/images/Math/Algebraic_Topology/Cup_products-3.png){:style="width:8em" class="invert" .align-center}

## Cap Product

In the remaining section, we prepare for discussing the duality between homology and cohomology. Of course, we were able to observe this duality in forms such as [\[Algebraic Topology\] §Cohomology, ¶Proposition 3](/en/math/algebraic_topology/cohomology#prop3), but what we will examine now has a somewhat more subtle character.

What we will do now is define an action of the graded ring $$H^\bullet(X;A)$$ on the homology module $$H_\bullet(X;A)$$. Writing this as

$${\frown}:H^\bullet(X;A)\otimes_A H_\bullet(X;A) \rightarrow H_\bullet(X;A)$$

the property we require of $$\frown$$ is the following *adjunction formula*

$$\langle \alpha\smile\beta,\sigma\rangle=\langle \alpha,\beta\frown \sigma\rangle$$

and through this, $$H_\bullet(X;A)$$ acquires an $$H^\bullet(X;A)$$-module structure. Here, $$\langle-,-\rangle$$ is the pairing induced by the Kronecker pairing

$$\langle-,-\rangle: C^\bullet(X;A)\times C_\bullet(X;A) \rightarrow A$$

For this equation to hold, we must have

$$\langle\alpha,\beta\frown \sigma\rangle=\langle\alpha\smile \beta,\sigma\rangle=\sum_i(-1)^{\lvert\beta\rvert\lvert\sigma_i\rangle}\alpha(\sigma_i)\beta(\tau_i)$$

Here, $$\sigma_i$$ and $$\tau_i$$ are the chains that appear when we express $$\sigma$$ as $$\sum \sigma_i\otimes\tau_i$$ via the Alexander-Whitney map. Since this equation must hold for all $$\alpha$$, we must define

$$\beta\frown \sigma=\sum_i(-1)^{\lvert\beta\rvert\lvert\sigma_i\rvert}\beta(\tau_i)\sigma_i$$

<div class="definition" markdown="1">

<ins id="def5">**Definition 5**</ins> The map defined above

$$\frown:H^p(X;A)\otimes H_{p+q}(X;A) \rightarrow H_q(X;A)$$

is called the *cap product*.

</div>

In other words, $$\frown$$ takes a homology chain of degree $$p+q$$ and a cohomology chain of degree $$p$$, computes the Kronecker pairing of the degree $$p$$ portion of the homology chain with the cohomology chain, and then scalar multiplies this constant with the remaining degree $$q$$ homology chain. This may seem like an artificial definition at first, but by the uniqueness of [§Acyclic models theorem, ¶Theorem 3](/en/math/algebraic_topology/acyclic_models_theorem#thm3), it is the only definition that makes sense. Moreover, from this representation, we can see that this is exactly the operation corresponding to the interior product.

The following then holds.

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6 (Projection formula)**</ins> For a continuous map $$f:X \rightarrow Y$$ and $$\alpha\in H^p(X)$$, $$\beta\in H^q(Y)$$, and $$\sigma\in H_{p+q}(X)$$, the following equation

$$f_\ast(f^\ast\beta\frown\sigma)=\beta\frown f_\ast\sigma$$

holds.

</div>

--- 

**References**

[Hat] A. Hatcher, *Algebraic Topology*. Cambridge University Press, 2022.

---
