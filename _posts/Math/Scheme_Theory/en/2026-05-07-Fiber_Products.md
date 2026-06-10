---
title: "Fiber Products"
description: "This post covers the definition and universal property of fiber products of schemes, and proves the existence of fiber products for affine schemes."
excerpt: "Definition and existence of fiber products in the category of S-schemes"

categories: [Math / Scheme Theory]
permalink: /en/math/scheme_theory/fiber_products
sidebar: 
    nav: "scheme_theory-en"

date: 2025-03-08
last_modified_at: 2025-03-08
weight: 11
translated_at: 2026-06-02T04:00:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-02T04:00:02+00:00
---
## Definition and Existence of Fiber Products

In [§Morphisms of Schemes, ⁋Definition 3](/en/math/scheme_theory/morphism_of_schemes#def3) we agreed to call a scheme morphism $$X \rightarrow S$$ an *$$S$$-scheme*. In this post we define the product in the category $$\Sch_{/S}$$.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> The fiber product of two scheme morphisms $$\varphi_X:X \rightarrow S$$, $$\varphi_Y:Y \rightarrow S$$ is denoted by $$X\times_SY$$. ([\[Category Theory\] §Limits, ⁋Example 8](/en/math/category_theory/limits#ex8))

</div>

That is, $$X\times_SY$$ satisfies the following property.

> The following diagram
> 
> ![fiber_diagram](/assets/images/Math/Algebraic_Varieties/Fiber_products-1.png){:style="width:11em" class="invert" .align-center}
> 
> commutes. Moreover, whenever arbitrary $$\psi_X:Z \rightarrow X$$, $$\psi_Y:Z \rightarrow Y$$ satisfying the equation $$\varphi_Y\circ\psi_Y=\varphi_X\circ\psi_X$$ are given, there exists a unique $$\psi:Z \rightarrow X\times_SY$$ such that $$\psi_X=\rho_X\circ\psi$$ and $$\psi_Y=\rho_Y\circ\psi$$.
> 
> ![universal_product](/assets/images/Math/Algebraic_Varieties/Fiber_products-2.png){:style="width:16em" class="invert" .align-center}

Therefore, there exists a canonical morphism from $$X\times_SY$$ to $$S$$, and from this we may regard $$X\times_SY$$ as an $$S$$-scheme. Moreover, from this perspective it is obvious from the definition that $$X\times_SY$$ is also the product in $$\Sch_{/S}$$.

After [§Morphisms of Schemes, ⁋Example 4](/en/math/scheme_theory/morphism_of_schemes#ex4) we saw that any scheme $$X$$ can always be regarded as a $$\mathbb{Z}$$-scheme in a unique way. Therefore, assuming that a fiber product $$X\times_SY$$ satisfying [Definition 1](#def1) always exists, we know that for any two schemes $$X, Y$$, the fiber product $$X\times_{\Spec \mathbb{Z}}Y$$ gives the product of $$X$$ and $$Y$$.

Since [Definition 1](#def1) does not guarantee anything about the existence of the fiber product $$X\times_SY$$, for this to be a genuine definition we must separately prove the existence of $$X\times_SY$$. ([Theorem 8](#thm8)) However, the existence of fiber products in $$\AffSch$$ is almost obvious, and this will be the starting point of our proof.

<div class="proposition" markdown="1">

<ins id="lem2">**Lemma 2**</ins> Given morphisms $$\Spec A \rightarrow \Spec C$$, $$\Spec B \rightarrow\Spec C$$ between affine schemes, we have

$$\Spec A\times_{\Spec C}\Spec B\cong\Spec (A\otimes_C B).$$

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Using the equivalence $$\AffSch\cong\cRing^\op$$, convert $$\Spec A \rightarrow \Spec C$$, $$\Spec B \rightarrow \Spec C$$ into $$C \rightarrow A$$, $$C \rightarrow B$$, and compare the universal property of [##ref##](tensor_product_of_algebras) with the universal property of the fiber product.

</details>

To show that fiber products exist for general schemes, we now need to show that we can glue together the results for affine schemes from [Lemma 2](#lem2).

First, given an open subscheme $$U$$ of $$Z$$, writing it in the form $$\iota:U \rightarrow Z$$ using the inclusion morphism, the following lemma is almost a tautology.

<div class="proposition" markdown="1">

<ins id="lem3">**Lemma 3**</ins> Given a scheme morphism $$\varphi: Y \rightarrow Z$$ and an open subscheme $$\iota: U \rightarrow Z$$ of $$Z$$, the following diagram

![open_subscheme](/assets/images/Math/Algebraic_Varieties/Fiber_products-3.png){:style="width:8.4em" class="invert" .align-center}

is a fiber diagram.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

$$\varphi^{-1}(U)$$ satisfies the universal property of the fiber product.

</details>

Now, by slightly exploiting this, we can prove the following lemma.

<div class="proposition" markdown="1">

<ins id="lem4">**Lemma 4**</ins> Given affine schemes $$X, Y, Z$$ and an open subscheme $$Y'\hookrightarrow Y$$ of $$Y$$, the fiber product $$X\times_ZY'$$ of $$X\rightarrow Z$$ and $$Y'\hookrightarrow Y \rightarrow Z$$ exists.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, from [Lemma 2](#lem2) we know that the following fiber diagram

![open_fiber_product-1](/assets/images/Math/Algebraic_Varieties/Fiber_products-4.png){:style="width:10.5em" class="invert" .align-center}

exists. Now, considering the following data

![open_fiber_product-2](/assets/images/Math/Algebraic_Varieties/Fiber_products-5.png){:style="width:9em" class="invert" .align-center}

we can verify from [Lemma 3](#lem3) that the open subscheme $$\rho_Y^{-1}(Y')$$ of $$X\times_SY$$ is a fiber product. Now, in general, if the two small squares in the following diagram

![magic_square](/assets/images/Math/Algebraic_Varieties/Fiber_products-6.png){:style="width:10.5em" class="invert" .align-center}

are fiber diagrams, then the outer large square is also a fiber diagram, so we obtain the desired result.

</details>

Now, using this, we can show that the fiber product of an affine scheme and an arbitrary scheme exists.

<div class="proposition" markdown="1">

<ins id="lem5">**Lemma 5**</ins> For affine schemes $$X, Z$$ and an arbitrary scheme $$Y$$, the fiber product $$X\times_ZY$$ of $$X\rightarrow Z$$ and $$Y \rightarrow Z$$ exists.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

For this, cover $$Y$$ by affine open subsets $$Y_i$$. Then from [Lemma 2](#lem2) we know that the $$X\times_ZY_i$$ exist. Also, since $$Y_{ij}=Y_i\cap Y_j$$ is an open subscheme of the affine scheme $$Y_i$$, the fiber product $$X\times_Z Y_{ij}$$ also exists by [Lemma 4](#lem4).

On the other hand, looking at the proof of [Lemma 4](#lem4), we can see that $$X\times_ZY_{ij}$$ is an open subscheme of both $$X\times_ZY_i$$ and $$X\times_ZY_j$$. We can easily verify that these data satisfy the conditions of [§Schemes, ⁋Lemma 9](/en/math/scheme_theory/schemes#lem9), so we can glue them together to form the scheme $$X\times_ZY$$. That this satisfies the universal property of the fiber product can be checked by restricting the codomain of a scheme morphism $$W \rightarrow Y$$ to the $$Y_i$$, using the universal property of each $$X\times_ZY_i$$, and then gluing the scheme morphisms together as in [§Morphisms of Schemes, ⁋Proposition 1](/en/math/scheme_theory/morphism_of_schemes#prop1).

</details>

In this lemma, the assumption that $$X$$ is an affine scheme was used only to show that $$X\times_ZY_i$$ exists. Therefore, given arbitrary schemes $$X,Y$$, an affine scheme $$Z$$, and scheme morphisms $$X \rightarrow Z$$ and $$Y \rightarrow Z$$, we can choose an affine open cover $$\{Y_i\}$$ of $$Y$$, then know that $$X\times_ZY_i$$ exists by [Lemma 5](#lem5), and thus glue them together to form $$X\times_ZY$$. That is, the following holds.

<div class="proposition" markdown="1">

<ins id="lem6">**Lemma 6**</ins> For an affine scheme $$Z$$, arbitrary schemes $$X,Y$$, and scheme morphisms $$X \rightarrow Z$$, $$Y \rightarrow Z$$, the fiber product $$X\times_ZY$$ exists.

</div>

Finally, we must extend $$Z$$ to an arbitrary scheme. First, the following holds.

<div class="proposition" markdown="1">

<ins id="lem7">**Lemma 7**</ins> Given arbitrary schemes $$X,Y,Z$$, scheme morphisms $$\varphi_X:X \rightarrow Z$$, $$\varphi_Y:Y \rightarrow Z$$, and a morphism $$\iota: Z \rightarrow Z'$$ to an affine scheme $$Z'$$, the fiber product $$X\times_{Z'}Y$$ of $$\iota\circ\varphi_X$$ and $$\iota\circ\varphi_Y$$ satisfies the universal property of $$X\times_ZY$$, and therefore $$X\times_ZY$$ exists.

</div>

Now, using the above lemma, for arbitrary $$X,Y,Z$$ and scheme morphisms $$\varphi_X:X \rightarrow Z$$, $$\varphi_Y: Y \rightarrow Z$$, if we cover $$Z$$ by an affine open cover $$\{Z_i\}$$, we know that fiber products $$X_i\times_{Z_i}Y_i$$ exist for $$\varphi_X\vert^{Z_i}:\varphi_X^{-1}(Z_i) \rightarrow Z_i$$ and $$\varphi_Y\vert^{Z_i}:\varphi_Y^{-1}(Z_i) \rightarrow Z_i$$. Now, since the intersection $$Z_{ij}=Z_i\cap Z_j$$ is an open subset of $$Z_i$$, by [Lemma 7](#lem7) the fiber products of $$\varphi_X\vert^{Z_{ij}}$$ and $$\varphi_Y\vert^{Z_{ij}}$$ also exist and are open subschemes of $$X_i\times_{Z_i}Y_i$$ and $$X_j\times_{Z_j}Y_j$$. Therefore, just as in the proof of [Lemma 5](#lem5), if we show that these data satisfy the conditions of [§Schemes, ⁋Lemma 9](/en/math/scheme_theory/schemes#lem9), we obtain the following theorem.

<div class="proposition" markdown="1">

<ins id="thm8">**Theorem 8**</ins> For arbitrary schemes $$X,Y,Z$$ and scheme morphisms $$X \rightarrow Z$$, $$Y \rightarrow Z$$, the fiber product $$X\times_ZY$$ exists.

</div>

## Interpretations of the Fiber Product

Just as there are various ways to interpret a scheme morphism, there are various ways to understand the fiber product.

Earlier, we agreed to think of a scheme morphism $$X \rightarrow S$$ as a family parametrized by $$S$$ ([§Morphisms of Schemes, ⁋Example 10](/en/math/scheme_theory/morphism_of_schemes#ex10)), and from this perspective $$S$$ can be thought of as the base of the family $$X$$. Now, given an arbitrary $$S$$-family $$X \rightarrow S$$ and a scheme morphism $$S' \rightarrow S$$, through the fiber product we obtain a new $$S'$$-family $$X\times_SS' \rightarrow S'$$. From this perspective, we often call the fiber product a *base change*.

<div class="example" markdown="1">

<ins id="ex9">**Example 9**</ins> Narrowing our scope to affine schemes, saying that $$\Spec B$$ is a $$C$$-scheme means that a scheme morphism $$\Spec B \rightarrow \Spec C$$ is given, which in turn is the same as a ring homomorphism $$C \rightarrow B$$ being given, which is again the same as saying that $$B$$ is a $$C$$-algebra.

Now, in addition, given a scheme morphism $$\Spec A \rightarrow \Spec C$$, let us see what the above base change gives. By [Lemma 2](#lem2), we know that what is obtained in this way is

$$\Spec A\times_{\Spec C}\Spec B=\Spec(A\otimes_CB) \rightarrow \Spec A,$$

that is, the ring homomorphism $$A \rightarrow A\otimes_CB$$. In other words, base change is (in the case of affine schemes) nothing other than [\[Algebraic Structures\] §Change of Base Ring, ⁋Definition 3](/en/math/algebraic_structures/change_of_base_ring#def3).

</div>

In particular, for a $$B$$-algebra $$B[\x_1,\ldots,\x_n]$$ and an arbitrary ring homomorphism $$B \rightarrow A$$, from the isomorphism

$$A\otimes_BB[\x_1,\ldots,\x_n]\cong A[\x_1,\ldots, \x_n]$$

we know that the following diagram

![adding_extra_variables](/assets/images/Math/Algebraic_Varieties/Fiber_products-7.png){:style="width:19.4em" class="invert" .align-center}

is a fiber diagram.

This perspective is important, but for now the geometric intuition here is not very visible. To see this, let us consider the case where $$S' \rightarrow S$$ is an embedding in particular.

First, given an arbitrary $$S$$-family $$X \rightarrow S$$ and an open embedding $$S' \rightarrow S$$, [Lemma 3](#lem3) shows that the $$S'$$-family $$X\times_SS' \rightarrow S'$$ is simply obtained by restricting the base of $$X \rightarrow S$$ to $$S'$$. Moreover, if we also assume that $$X \rightarrow S$$ is an open embedding, we know that $$X\times_SS'$$ is the intersection of $$X$$ and $$S'$$ (inside $$S$$).

The above argument also works for closed embeddings. To see this, we need to show the following lemma corresponding to [Lemma 3](#lem3).

<div class="proposition" markdown="1">

<ins id="lem10">**Lemma 10**</ins> For a ring homomorphism $$\phi: B \rightarrow A$$ and an arbitrary ideal $$\mathfrak{b}$$ of $$B$$, there exists an isomorphism

$$A/\phi(\mathfrak{b})A\cong A \otimes_B(B/\mathfrak{b}).$$

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

From the ideal $$\mathfrak{b}$$ we have the following exact sequence

$$\mathfrak{b} \rightarrow B \rightarrow B/\mathfrak{b} \rightarrow 0,$$

and taking $$\otimes_BA$$ gives the following exact sequence

$$A\otimes_B \mathfrak{b} \rightarrow A\otimes_BB \rightarrow A\otimes_B (B/\mathfrak{b}) \rightarrow 0,$$

and since the image of $$A\otimes_B \mathfrak{b}$$ in $$A\otimes_BB\cong A$$ is $$\phi(\mathfrak{b})A$$, we obtain the desired result.

</details>

Now, since any closed embedding locally always comes from some $$B \rightarrow B/\mathfrak{b}$$, we can apply the above discussion to closed embeddings in the same way. In particular, the intersection of two closed embeddings is well-defined.

<div class="example" markdown="1">

<ins id="ex11">**Example 11**</ins> Consider the two closed subschemes of $$Z=\Spec\mathbb{K}[\x,\y]$$

$$X=\Spec \mathbb{K}[\x,\y]/(\y)=\Spec \mathbb{K}[\x],\qquad Y=\Spec \mathbb{K}[\x,\y]/(\x)=\Spec \mathbb{K}[\y].$$

Then $$X$$ and $$Y$$ correspond to the $$\x$$-axis and $$\y$$-axis of $$Z=\mathbb{A}^2_\mathbb{K}$$ respectively, and their closed embeddings are given by the projections

$$\mathbb{K}[\x,\y] \rightarrow \mathbb{K}[\x],\qquad \mathbb{K}[\x,\y] \rightarrow \mathbb{K}[\y].$$

Now $$X\times_ZY$$ is, by [Lemma 2](#lem2),

$$\Spec\left(\frac{\mathbb{K}[\x,\y]}{(\x)}\otimes_{\mathbb{K}[\x,\y]} \frac{\mathbb{K}[\x,\y]}{(\y)}\right)\cong \Spec \mathbb{K}[\x,\y]/(\x,\y)\cong\Spec \mathbb{K},$$

and we can check that this corresponds exactly to the origin, the intersection point of the $$\x$$-axis and the $$\y$$-axis.

Now let us replace $$Y$$ in the above calculation with the following closed subscheme

$$Y=\Spec \mathbb{K}[\x,\y]/(\y-\x^2).$$

The intersection of $$\y=\x^2$$ and the $$\x$$-axis is again the origin, but this time a double root exists, so the scheme structure must be given differently. Indeed, repeating the calculation, $$X\times_ZY$$ becomes

$$\Spec\left(\frac{\mathbb{K}[\x,\y]}{(\y)}\otimes_{\mathbb{K}[\x,\y]}\frac{\mathbb{K}[\x,\y]}{(\y-\x^2)}\right)\cong\Spec \mathbb{K}[\x,\y]/(\y,\y-\x^2)\cong\Spec \mathbb{K}[\x]/(\x^2).$$

</div>

From this perspective, we can also see how to define the fiber $$\varphi^{-1}(y_0)$$ of a scheme morphism $$\varphi:X \rightarrow Y$$ at a point $$y_0\in Y$$. Whether $$y_0$$ is a closed point or not, viewing it as $$\iota:\{y_0\}\hookrightarrow Y$$ and taking the fiber product of $$\iota$$ and $$\varphi$$ suffices. For this, we must describe $$\iota$$ as a scheme morphism.

To do this, consider the residue field $$\kappa(y)$$ at $$y$$. Then $$\Spec\kappa(y)$$ is always a one-point set. Moreover, considering an affine open subset $$V=\Spec B$$ of $$Y$$ containing $$y$$, and letting $$y$$ correspond to the prime ideal $$\mathfrak{q}_y$$, through the canonical morphism

$$B \rightarrow B_{\mathfrak{q}_y} \rightarrow B_{\mathfrak{q}_y}/\mathfrak{q}_y B_{\mathfrak{q}_y} =\kappa(\mathfrak{q}_y)=\kappa(y)$$

the morphism $$\Spec\kappa(y)\rightarrow \Spec B$$ is defined, and the (unique) point $$(0)$$ of $$\Spec \kappa(y)$$ is mapped to $$\mathfrak{q}_y$$ via the above morphism. Therefore, we define the following.

<div class="definition" markdown="1">

<ins id="def12">**Definition 12**</ins> For a scheme morphism $$\varphi: X \rightarrow Y$$, the *fiber* at a point $$y\in Y$$ is defined as

$$\varphi^{-1}(y)=X\times_Y\Spec \kappa(y).$$

If $$Y$$ is irreducible, the fiber at the generic point of $$Y$$ is called the *generic fiber*.

</div>

<div class="example" markdown="1">

<ins id="ex13">**Example 13**</ins> For an algebraically closed field $$\mathbb{K}$$, define the ring homomorphism $$\mathbb{K}[\x] \rightarrow \mathbb{K}[\y]$$ by the formula $$\x \mapsto \y^2$$, and consider the scheme morphism $$\varphi: \Spec \mathbb{K}[\y] \rightarrow \Spec \mathbb{K}[\x]$$ obtained from this. Then the residue field at an arbitrary point $$(\x-a)$$ of $$\Spec\mathbb{K}[\x]$$ is

$$\Frac(\mathbb{K}[\x]/(\x-a))=\mathbb{K}[\x]/(\x-a).$$

Now, for arbitrary $$a\in \mathbb{K}$$,

$$\varphi^{-1}((\x-a))=\Spec \mathbb{K}[\y]\otimes_{\Spec \mathbb{K}[\x]}\Spec \mathbb{K}[\x]/(\x-a)\cong \Spec(\mathbb{K}[\y]\otimes_{\mathbb{K}[\x]}\mathbb{K}[\x]/(\x-a))=\Spec \mathbb{K}[\y]/(\y^2-a),$$

and therefore if $$a=0$$ then $$\varphi^{-1}((\x))\cong\Spec \mathbb{K}[\y]/(\y^2)$$, and if $$a\neq 0$$ then from the assumption that $$\mathbb{K}$$ is algebraically closed we know

$$\Spec \mathbb{K}[\y]/(\y^2-a)\cong \Spec \mathbb{K}[\y]/(\y-\sqrt{a})\coprod \Spec \mathbb{K}[\y]/(\y+\sqrt{a}).$$

On the other hand, for the generic point $$(0)$$ of $$\mathbb{K}[\x]$$ we have $$\kappa((0))=\mathbb{K}(\x)$$, so

$$\varphi^{-1}((0))=\Spec \mathbb{K}[\y]\otimes_{\Spec \mathbb{K}[\x]}\Spec \mathbb{K}(\x)\cong \Spec\mathbb{K}(\y).$$

</div>

The above example is what we already examined in [§Properties of Scheme Morphisms, ⁋Example 15](/en/math/scheme_theory/properties_of_scheme_morphisms#ex15). In that example, we claimed that a finite morphism is always quasi-finite, and now we can prove this.

<div class="proposition" markdown="1">

<ins id="prop14">**Proposition 14**</ins> A finite morphism $$\varphi: X \rightarrow Y$$ is a quasi-finite morphism.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

It suffices to show the affine case. That is, it suffices to show that for an arbitrary finite ring homomorphism $$\phi: B \rightarrow A$$ and a prime ideal $$\mathfrak{q}$$ of $$B$$, the tensor product $$A\otimes_B\kappa(\mathfrak{q})$$ has finitely many prime ideals. Since $$\phi$$ is finite, $$A\otimes_B\kappa(\mathfrak{q})$$ is a finite $$\kappa(\mathfrak{q})$$-algebra and therefore artinian, from which we obtain the desired result. ([\[Ring Theory\] §Chinese Remainder Theorem](/en/math/ring_theory/chinese_remainder_theorem))

</details>

From the above examples and propositions we can make an important observation: if $$X \rightarrow S$$ satisfies some property $$P$$ of scheme morphisms, then the base change $$X\times_SS' \rightarrow S'$$ via arbitrary $$S' \rightarrow S$$ also satisfies it. This is not a coincidence; in fact, most properties we are interested in are closed under base change.

<div class="proposition" markdown="1">

<ins id="prop15">**Proposition 15**</ins> If a scheme morphism $$\varphi:X \rightarrow Z$$ is quasicompact (resp. quasiseparated, affine, finite, integral, locally of finite type, finite type, locally of finite presentation, finite presentation, quasi-finite, surjective), then the base change $$X\times_ZY \rightarrow X$$ of $$\varphi$$ via an arbitrary scheme morphism $$Y \rightarrow Z$$ is also such.

</div>

For instance, for integral morphisms and finite morphisms we proved this in [\[Commutative Algebra\] §Integral Extensions, ⁋Proposition 14](/en/math/commutative_algebra/integral_extension#prop14), and for the other properties the above proposition can be shown without difficulty.
