---
title: "Dimension"
description: "We define the dimension of a scheme in terms of Krull dimension and examine its relationship with commutative-algebraic notions of dimension. Properties of finite and integral morphisms are discussed together."
excerpt: "The definition of scheme dimension and its relation to Krull dimension of local rings"

categories: [Math / Scheme Theory]
permalink: /en/math/scheme_theory/dimension
drift_needed: true
sidebar: 
    nav: "scheme_theory-en"

date: 2025-03-14
weight: 16
translated_at: 2026-06-26T05:01:02+00:00
translation_source: kimi-cli
---
## Dimension of Schemes

We now define the dimension of a scheme.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> The *dimension* of a scheme $$X$$ is defined as the Krull dimension of the topological space $$X$$. ([[Topology] §Dimension, ⁋Definition 10](/en/math/topology/dimension#def10))

</div>

Then, by the Galois correspondence of [§Spectrums, ⁋Proposition 16](/en/math/scheme_theory/spectrums#prop16), we know that the dimension of $$\Spec A$$ as a scheme equals the dimension of $$A$$ as a ring. ([[Commutative Algebra] §Dimension, ⁋Definition 1](/en/math/commutative_algebra/Krull_dimension#def1)) Moreover, by definition, one can show that $$\Spec A$$ and $$\Spec A/\mathfrak{N}(A)$$ are homeomorphic, so $$\dim A=\dim A/\mathfrak{N}(A)$$ holds. That is, reducedness does not affect dimension.

On the other hand, by the same reasoning as in [[Topology] §Dimension, ⁋Proposition 13](/en/math/topology/dimension#prop13), the following holds.

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> For an arbitrary scheme $$X$$, the condition $$\dim X=n$$ is equivalent to the existence of an affine open covering $$(U_i)$$ of $$X$$ such that $$\dim U_i\leq n$$ for all $$U_i$$, with equality holding for at least one $$i$$.

</div>

Meanwhile, we saw in [§Properties of Scheme Morphisms, ⁋Proposition 14](/en/math/scheme_theory/properties_of_scheme_morphisms#prop14) that a finite morphism is an integral morphism of finite type, and in [§Fiber Products, ⁋Proposition 14](/en/math/scheme_theory/fiber_products#prop14) that any finite morphism is quasi-finite. In general, there exist integral morphisms that are not of finite type, so we cannot yet say anything about the fibers of integral morphisms.

<div class="example" markdown="1">

<ins id="ex3">**Example 3**</ins> For example, consider the algebraic closure $$\overline{\mathbb{Q}}$$ of $$\mathbb{Q}$$. Then $$\mathbb{Q} \rightarrow \overline{\mathbb{Q}}$$ is integral, so the scheme morphism $$\Spec \overline{\mathbb{Q}} \rightarrow \Spec \mathbb{Q}$$ is integral.

On the other hand, by [§Fiber Products, ⁋Proposition 15](/en/math/scheme_theory/fiber_products#prop15), integral morphisms are preserved under base change, so the base change of $$\Spec \overline{\mathbb{Q}} \rightarrow \Spec \mathbb{Q}$$ via $$\Spec \overline{\mathbb{Q}} \rightarrow \Spec \mathbb{Q}$$, namely $$\Spec \overline{\mathbb{Q}}\otimes_\mathbb{Q}\overline{\mathbb{Q}} \rightarrow \Spec \overline{\mathbb{Q}}$$, is also integral. However, the prime ideals of $$\overline{\mathbb{Q}}\otimes \overline{\mathbb{Q}}$$ are in bijection with $$\Gal(\overline{\mathbb{Q}}/\mathbb{Q})$$, so $$\Spec\overline{\mathbb{Q}}\otimes \overline{\mathbb{Q}}$$ is an infinite set, and thus $$\Spec \overline{\mathbb{Q}}\otimes_\mathbb{Q}\overline{\mathbb{Q}} \rightarrow \Spec \overline{\mathbb{Q}}$$ is not a quasi-finite morphism, hence not a finite morphism.

</div>

However, the following holds.

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4**</ins> Any fiber of an integral morphism $$\varphi: X \rightarrow Y$$ is always of dimension $$0$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

By definition, the fiber at a point $$y$$ of $$Y$$ is given by the base change of $$\varphi$$ along the inclusion map $$\Spec \kappa(y) \rightarrow Y$$:

$$\varphi^{-1}(y)=X\times_Y\Spec \kappa(y)$$

Since integral morphisms are preserved under base change,

$$\varphi^{-1}(y)=X\times_Y\Spec \kappa(y) \rightarrow \Spec \kappa(y)$$

is an integral morphism, and by definition an integral morphism is an affine morphism. Thus it suffices to show that for any integral morphism $$\Spec B \rightarrow \Spec \mathbb{K}$$, we have $$\dim \Spec B=\dim B=0$$. That is, we must show that for any integral extension $$\mathbb{K} \rightarrow B$$, there cannot exist a chain of prime ideals of $$B$$

$$\mathfrak{q}_1\subsetneq \mathfrak{q}_2$$

This is a consequence of [[Commutative Algebra] §Integral Extensions and Ideals, ⁋Corollary 4](/en/math/commutative_algebra/lying_over_and_going_up#cor4).

</details>

Since [[Commutative Algebra] §Integral Extensions and Ideals, ⁋Corollary 4](/en/math/commutative_algebra/lying_over_and_going_up#cor4) used in the proof of the above proposition also holds for any integral extension $$A\hookrightarrow B$$, more generally the following holds.

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> For any integral extension $$\phi:A \rightarrow B$$,

$$\dim\Spec A=\dim\Spec B$$

always holds.

</div>

In particular, for any integral domain $$A$$ and its normalization $$\tilde{A}$$, the dimensions of $$\Spec \tilde{A}$$ and $$\Spec A$$ are always equal. This holds more generally for the normalization of a scheme, but the normalization of schemes will be treated in a separate post later.

<div class="definition" markdown="1">

<ins id="def6">**Definition 6**</ins> For an irreducible subset $$Y$$ of a topological space $$X$$, the *codimension* of $$Y$$ in $$X$$, denoted $$\codim_XY$$, is defined as the supremum of the lengths of strictly descending chains of irreducible closed subsets of $$X$$

$$A_n\supsetneq A_{n-1}\supsetneq\cdots\supsetneq A_0=\cl_X(Y)$$

</div>

Then one can verify that the codimension of a prime ideal $$\mathfrak{p}$$ of a ring $$A$$ ([[Commutative Algebra] §Dimension, ⁋Definition 2](/en/math/commutative_algebra/Krull_dimension#def2)) equals the codimension of the point $$\mathfrak{p}$$ in $$\Spec A$$.

<div class="proposition" markdown="1">

<ins id="prop7">**Proposition 7**</ins> For an irreducible closed subset $$Y$$ of $$X$$ and its generic point $$y$$, we have $$\codim Y=\dim \mathcal{O}_{X, y}$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Since $$Y$$ has generic point $$y$$, by definition $$\codim_XY$$ equals $$\codim_X\{y\}$$. Now choose any affine open subset $$U\cong\Spec A$$ containing $$y$$, and let $$y\in U$$ correspond to $$\mathfrak{p}_y\in \Spec A$$ under this isomorphism. Then by [[Topology] §Dimension, ⁋Proposition 14](/en/math/topology/dimension#prop14), we know that there is a bijection between the irreducible closed subsets of $$X$$ meeting $$U$$ and the irreducible closed subsets of $$U$$. That is, $$\codim_X\{y\}=\codim_U \mathfrak{p}_y$$. Now we obtain the desired result from [§Spectrums, ⁋Proposition 16](/en/math/scheme_theory/spectrums#prop16).

</details>

More generally, after defining codimension in [[Commutative Algebra] §Dimension, ⁋Definition 2](/en/math/commutative_algebra/Krull_dimension#def2), we proved the inequality

$$\dim \mathfrak{a}+\codim \mathfrak{a}\leq \dim A$$

Using [[Topology] §Dimension, ⁋Proposition 14](/en/math/topology/dimension#prop14) in place of [[Commutative Algebra] §Localization, ⁋Proposition 8](/en/math/commutative_algebra/localization#prop8) used there, one can verify that for a scheme $$X$$ and an irreducible closed subset $$Y$$ of $$X$$, the following inequality holds:

$$\dim Y+\codim_XY\leq \dim X$$

However, as before, equality does not hold in general.

## Noether Normalization

We now show the following important result.

<div class="proposition" markdown="1">

<ins id="thm8">**Theorem 8 (Noether normalization lemma)**</ins> Let $$\mathbb{K}$$ be an arbitrary field and $$A$$ a finitely generated $$\mathbb{K}$$-algebra. If $$A$$ is an integral domain and

$$\trdeg_\mathbb{K}\Frac(A)=n$$

then there exist elements $$x_1,\ldots, x_n$$ of $$A$$ that are algebraically independent and such that $$A$$ is a finite $$\mathbb{K}[x_1,\ldots, x_n]$$-module.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

From the assumption that $$A$$ is a finitely generated $$\mathbb{K}$$-algebra, we can write

$$A=\mathbb{K}[y_1,\ldots, y_m]/\mathfrak{p}$$

Then the images of $$y_1,\ldots, y_m$$ in $$\Frac(A)$$ generate $$\Frac(A)$$ as a field extension of $$\mathbb{K}$$, so we must have $$m\geq n$$.

Now if $$m=n$$, then the $$y_i$$ are exactly the desired elements, and there is nothing more to prove. To prove the given statement, assume $$m>n$$ and suppose the theorem holds for any $$k$$ with $$n\leq k< m$$. Then by the assumption $$m>n$$, the elements $$y_1,\ldots, y_m$$ are algebraically dependent. That is, there exists an $$m$$-variable polynomial over $$\mathbb{K}$$

$$f(\x_1,\ldots, \x_m)=\sum \alpha_{d_1d_2\cdots d_m}\x_1^{d_1}\cdots\x_m^{d_m}\in \mathbb{K}[\x_1,\ldots, \x_m]\tag{$\ast$}$$

satisfying

$$f(y_1,\ldots, y_m)=0$$

Now for integers $$r_1,\ldots, r_{m-1}$$, define elements $$z_1,\ldots, z_{m-1}$$ by

$$z_1=y_1-y_m^{r_1},\quad z_2=y_2-y_m^{r_2},\quad\ldots\quad,\quad z_{m-1}=y_{m-1}-y_m^{r_{m-1}}$$

Then by definition

$$f(z_1+y_m^{r_1},\ldots, z_{m-1}+y_m^{r_{m-1}}, y_m)=0\tag{$\ast\ast$}$$

holds. Now substitute

$$\x_1=z_1+y_m^{r_1},\quad \ldots\quad,\quad \x_{m-1}=z_{m-1}+y_m^{r_{m-1}},\quad \x_m=y_m$$

into each monomial $$\alpha_{d_1d_2\cdots d_m}\x_1^{d_1}\cdots\x_m^{d_m}$$ constituting $$f$$ in ($$\ast$$) and expand. The result will be a power of $$y_m$$ with constant coefficient

$$\alpha_{d_1d_2\cdots d_m}y_m^{r_1d_1+\cdots+r_{m-1}d_{m-1}+d_m}$$

and other terms involving $$z_k$$. Now if we choose $$r_1,\ldots, r_{m-1}$$ sufficiently large, we can make such a term the leading term, and thus the above equation ($$\ast\ast$$) shows that $$y_m$$ is integrally dependent on $$z_1,\ldots, z_{m-1}$$. On the other hand, for the $$\mathbb{K}$$-subalgebra $$A'$$ of $$A$$ generated by $$z_1,\ldots, z_{m-1}$$, that is, the $$\mathbb{K}$$-subalgebra $$A'$$ of $$A$$ where the coefficients exist when ($$\ast\ast$$) is viewed as a polynomial in $$y_m$$, the inductive hypothesis gives elements $$x_1,\ldots, x_n\in A$$ satisfying the desired condition. Now $$A$$ is a finite $$A'$$-module by the above argument, and $$A'$$ is a finite $$\mathbb{K}[x_1,\ldots, x_n]$$-module by the inductive hypothesis, so we obtain the desired result.

</details>

Geometrically, setting $$A=\mathbb{K}[y_1,\ldots, y_m]/\mathfrak{p}$$ means that $$\Spec A$$ is an integral closed subscheme of the affine space $$\mathbb{A}^m_\mathbb{K}$$, so the finite ring homomorphism $$\mathbb{K}[x_1,\ldots, x_n] \rightarrow \mathbb{K}[y_1,\ldots, y_m]/\mathfrak{p}$$ obtained from the above theorem corresponds geometrically to finding a finite scheme morphism $$\Spec A \rightarrow \Spec \mathbb{K}[x_1,\ldots, x_n]$$. Now since the finite extension $$\mathbb{K}[x_1,\ldots, x_n] \rightarrow A$$ is an integral extension, by [Proposition 5](#prop5) we have $$\dim A=\dim \mathbb{K}[x_1,\ldots, x_n]$$, and thus by [[Commutative Algebra] §System of Parameters, ⁋Corollary 11](/en/math/commutative_algebra/system_of_parameters#cor11) we obtain the following result.

<div class="proposition" markdown="1">

<ins id="prop9">**Proposition 9**</ins> Let $$\mathbb{K}$$ be an arbitrary field and $$A$$ a finitely generated $$\mathbb{K}$$-algebra. If $$A$$ is an integral domain, then $$\dim\Spec A=\trdeg_\mathbb{K} \Frac(A)$$ holds.

</div>

The most important results used in the above statements are of course those from [[Commutative Algebra] §Integral Extensions and Ideals](/en/math/commutative_algebra/lying_over_and_going_up). As a classical result paired with this, there is the *going-down theorem*, which holds for integral extensions over normal domains (**[AM]**). Using this, we obtain the following.

<div class="proposition" markdown="1">

<ins id="prop10">**Proposition 10**</ins> Let $$\mathbb{K}$$ be an arbitrary field and $$A$$ a finitely generated $$\mathbb{K}$$-algebra. If $$A$$ is an integral domain and $$f\in A$$ is a non-unit, then $$\dim A/(f)=\dim A-1$$ holds.

</div>

## Principal Ideal Theorem

Earlier we saw that for any affine integral $$\mathbb{K}$$-scheme $$X=\Spec A$$, the closed subscheme $$Z(f)$$ defined by a non-unit $$f$$ of $$A$$ has dimension one less than that of $$A$$. This is clearly a useful result, but we can examine the result in the following more general case as well.

<div class="proposition" markdown="1">

<ins id="prop11">**Proposition 11**</ins> For a locally noetherian scheme $$X$$ and a function $$f$$ on $$X$$, each irreducible component of $$Z(f)$$ has codimension $$0$$ or codimension $$1$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

[[Commutative Algebra] §Dimension, ⁋Theorem 6](/en/math/commutative_algebra/Krull_dimension#thm6)

</details>

---

**References**

**[AM]** M. F. Atiyah and I. G. Macdonald, *Introduction to commutative algebra*, Addison-Wesley, 1969.
