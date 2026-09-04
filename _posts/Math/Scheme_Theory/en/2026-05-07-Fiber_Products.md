---
title: "Fiber Products"
description: "We define fiber products of schemes and discuss their universal properties, then prove the existence of fiber products for affine schemes."
excerpt: "Definition and existence of fiber products in the category of S-schemes"

categories: [Math / Scheme Theory]
permalink: /en/math/scheme_theory/fiber_products
sidebar: 
    nav: "scheme_theory-en"

date: 2025-03-08
weight: 12
translated_at: 2026-07-27T01:15:03+00:00
translation_source: kimi-cli
last_polished_at: 2026-07-27T01:15:03+00:00
---
One of the things we promised when introducing schemes was the fiber product; since this is the product in $\Sch_{/S}$, we had to define $S$-schemes (and scheme morphisms) in preparation. Now that we are ready, we define the fiber product.

## Definition and Existence of Fiber Products

In [§Morphisms of Schemes, ⁋Definition 3](/en/math/scheme_theory/morphism_of_schemes#def3) we agreed to call a scheme morphism $X \rightarrow S$ an *$S$-scheme*. In this post we define the product in the category $\Sch_{/S}$.

::: Definition 1
The fiber product of two scheme morphisms $\varphi_X:X \rightarrow S$, $\varphi_Y:Y \rightarrow S$ is denoted $X\times_SY$. ([\[Category Theory\] §Limits, ⁋Example 8](/en/math/category_theory/limits#ex8))
:::

That is, $X\times_SY$ satisfies the following property.

> The diagram
> 
> {% diagram Math/Scheme_Theory/Fiber_Products-1.svg width="9.32em" alt="fiber_diagram" %}
> 
> commutes. Moreover, whenever morphisms $\psi_X:Z \rightarrow X$, $\psi_Y:Z \rightarrow Y$ satisfying $\varphi_Y\circ\psi_Y=\varphi_X\circ\psi_X$ are given, there exists a unique $\psi:Z \rightarrow X\times_SY$ such that $\psi_X=\rho_X\circ\psi$ and $\psi_Y=\rho_Y\circ\psi$.
> 
> {% diagram Math/Scheme_Theory/Fiber_Products-2.svg width="13.72em" alt="universal_product" %}

Hence there is a canonical morphism from $X\times_SY$ to $S$, and from this we may view $X\times_SY$ as an $S$-scheme. Moreover, from this viewpoint it is obvious from the definition that $X\times_SY$ is also the product in $\Sch_{/S}$.

After [§Morphisms of Schemes, ⁋Example 4](/en/math/scheme_theory/morphism_of_schemes#ex4) we saw that any scheme $X$ can always be regarded as a $\mathbb{Z}$-scheme in a unique way. Thus, assuming that a fiber product $X\times_SY$ satisfying [Definition 1](#def1) always exists, we know that for any two schemes $X, Y$, the object $X\times_{\Spec \mathbb{Z}}Y$ gives the product of $X$ and $Y$.

Since [Definition 1](#def1) guarantees nothing about the existence of the fiber product $X\times_SY$, for this to be a genuine definition we must separately prove existence. ([Theorem 8](#thm8)) However, the existence of fiber products in $\AffSch$ is almost obvious, and this will be the starting point of our proof.

::: Lemma 2
Given morphisms of affine schemes $\Spec A \rightarrow \Spec C$, $\Spec B \rightarrow\Spec C$, we have

$$\Spec A\times_{\Spec C}\Spec B\cong\Spec (A\otimes_C B).$$
:::
::: Proof
Via $\AffSch\cong\cRing^\op$, convert $\Spec A \rightarrow \Spec C$, $\Spec B \rightarrow \Spec C$ into $C \rightarrow A$, $C \rightarrow B$, and compare the universal property of [\[Algebraic Structures\] §Direct Products, Direct Sums, and Tensor Products of Algebras, ⁋Theorem 8](/en/math/algebraic_structures/operations_of_algebras#thm8) with the universal property of the fiber product.
:::

To show that fiber products exist for general schemes, it now suffices to show that we can glue together the affine results from [Lemma 2](#lem2).

First, when an open subscheme $U$ of $Z$ is given, writing it in the form $\iota:U \rightarrow Z$ using the inclusion morphism, the following lemma is almost a tautology.

::: Lemma 3
Given a scheme morphism $\varphi: Y \rightarrow Z$ and an open subscheme $\iota: U \rightarrow Z$ of $Z$, the diagram

{% diagram Math/Scheme_Theory/Fiber_Products-3.svg width="8.22em" alt="open_subscheme" %}

is a fiber diagram.
:::
::: Proof
$\varphi^{-1}(U)$ satisfies the universal property of the fiber product.
:::

Applying this slightly, we can prove the following lemma.

::: Lemma 4
Given affine schemes $X, Y, Z$, and an open subscheme $Y'\hookrightarrow Y$ of $Y$, the fiber product $X\times_ZY'$ of $X\rightarrow Z$ and $Y'\hookrightarrow Y \rightarrow Z$ exists.
:::
::: Proof
First, from [Lemma 2](#lem2) we know that the following fiber diagram exists:

{% diagram frozen/629e76cc/Math/Scheme_Theory/Fiber_Products-4.svg width="9.32em" alt="open_fiber_product-1" %}

Now, considering the data

{% diagram frozen/629e76cc/Math/Scheme_Theory/Fiber_Products-5.svg width="8.55em" alt="open_fiber_product-2" %}

we can verify from [Lemma 3](#lem3) that the open subscheme $\rho_Y^{-1}(Y')$ of $X\times_ZY$ is the fiber product. In general, if the two small squares in the following diagram

{% diagram frozen/629e76cc/Math/Scheme_Theory/Fiber_Products-6.svg width="8.55em" alt="magic_square" %}

are fiber diagrams, then the outer large square is also a fiber diagram, so we obtain the desired result.
:::

Using this, we can now show that the fiber product of an affine scheme and an arbitrary scheme exists.

::: Lemma 5
For affine schemes $X, Z$ and an arbitrary scheme $Y$, the fiber product $X\times_ZY$ of $X\rightarrow Z$ and $Y \rightarrow Z$ exists.
:::
::: Proof
For this, cover $Y$ by affine open subsets $Y_i$. Then we know from [Lemma 2](#lem2) that the $X\times_ZY_i$ exist. Also, since $Y_{ij}=Y_i\cap Y_j$ is an open subscheme of the affine scheme $Y_i$, the $X\times_Z Y_{ij}$ also exist by [Lemma 4](#lem4).

On the other hand, looking at the proof of [Lemma 4](#lem4), we see that each $X\times_ZY_{ij}$ is an open subscheme of both $X\times_ZY_i$ and $X\times_ZY_j$. It is easy to check that these data satisfy the conditions of [§Schemes, ⁋Lemma 9](/en/math/scheme_theory/schemes#lem9), so we can glue them to obtain a scheme $X\times_ZY$. That this satisfies the universal property of the fiber product is verified as follows. Given a scheme $W$ and morphisms $\alpha: W \rightarrow X$, $\beta: W \rightarrow Y$ agreeing over $Z$, set $W_i=\beta^{-1}(Y_i)$. Then the restriction of $\beta$ to $W_i$ defines $W_i \rightarrow Y_i$, so from the universal property of $X\times_ZY_i$ we obtain a unique morphism $\sigma_i: W_i \rightarrow X\times_ZY_i$. Now on $W_i\cap W_j=\beta^{-1}(Y_{ij})$, both $\sigma_i$ and $\sigma_j$ coincide with the unique morphism given by the universal property of $X\times_ZY_{ij}$, and hence agree; therefore by [§Morphisms of Schemes, ⁋Proposition 1](/en/math/scheme_theory/morphism_of_schemes#prop1) they glue to a unique morphism $\sigma: W \rightarrow X\times_ZY$. Note that here we restrict the domain to $W_i$ rather than the codomain to $Y_i$, because there is no reason for the image of $\beta$ to lie in $Y_i$.
:::

In this lemma, the hypothesis that $X$ is affine was used only to show that $X\times_ZY_i$ exists. Hence, given arbitrary schemes $X,Y$ and an affine scheme $Z$, and scheme morphisms $X \rightarrow Z$ and $Y \rightarrow Z$, we can choose an affine open cover $\{Y_i\}$ of $Y$ and then apply [Lemma 5](#lem5) with the two arguments swapped. That is, since $Y_i$ and $Z$ are affine, $Y_i\times_ZX$ exists, and since the fiber product is symmetric in its two arguments, $X\times_ZY_i$ exists. Also $Y_{ij}$ is an open subscheme of $Y_i$, so $X\times_ZY_{ij}$ exists by [Lemma 4](#lem4) and is an open subscheme of both $X\times_ZY_i$ and $X\times_ZY_j$. Therefore, repeating the gluing argument in the proof of [Lemma 5](#lem5) verbatim, we obtain the following.

::: Lemma 6
For an affine scheme $Z$, arbitrary schemes $X,Y$ and scheme morphisms $X \rightarrow Z$, $Y \rightarrow Z$, the fiber product $X\times_ZY$ exists.
:::

Finally, we must extend $Z$ to an arbitrary scheme. First, the following holds.

::: Lemma 7
Given arbitrary schemes $X,Y,Z$, scheme morphisms $\varphi_X:X \rightarrow Z$, $\varphi_Y:Y \rightarrow Z$ and a monomorphism $\iota: Z \rightarrow Z'$ to an affine scheme $Z'$. For instance, this is the case when $\iota$ is an open immersion or a closed embedding. In the latter case, given two morphisms $\alpha,\beta: T \rightarrow Z$ with $\iota\circ \alpha=\iota\circ \beta$, since $\iota$ is injective we have $\alpha=\beta$ as continuous maps, and at each $t\in T$, $\iota^\sharp$ induces a surjection $\mathcal{O}_{Z',\iota(\alpha(t))} \rightarrow \mathcal{O}_{Z,\alpha(t)}$ on stalks ([§Closed Subschemes, ⁋Definition 2](/en/math/scheme_theory/closed_subschemes#def2)), so $\alpha^\sharp$ and $\beta^\sharp$ are determined by their compositions and hence equal. Then the fiber product $X\times_{Z'}Y$ of $\iota\circ\varphi_X$ and $\iota\circ\varphi_Y$ satisfies the universal property of $X\times_ZY$, and therefore $X\times_ZY$ exists.
:::
::: Proof
Since $Z'$ is affine, $X\times_{Z'}Y$ exists. Now let $T$ be an arbitrary scheme and let morphisms $\alpha:T \rightarrow X$, $\beta:T \rightarrow Y$ be given. The condition required in the universal property of $X\times_ZY$ is $\varphi_X\circ \alpha=\varphi_Y\circ \beta$, while that of $X\times_{Z'}Y$ is $\iota\circ\varphi_X\circ \alpha=\iota\circ\varphi_Y\circ \beta$; since $\iota$ is a monomorphism these two conditions are equivalent. Hence the two fiber products satisfy the same universal property, and by uniqueness $X\times_{Z'}Y$ plays the role of $X\times_ZY$.

On the other hand, without the hypothesis on $\iota$ this does not hold. For example, taking the structure morphism $\iota:Z \rightarrow \Spec k$ of a $k$-scheme and giving identity morphisms on $X=Y=Z=\mathbb{A}^1_k$, we have $X\times_ZY=\mathbb{A}^1_k$ but $X\times_{\Spec k}Y=\mathbb{A}^2_k$.
:::

Now, using the above lemma, for arbitrary $X,Y,Z$ and scheme morphisms $\varphi_X:X \rightarrow Z$, $\varphi_Y: Y \rightarrow Z$, if we cover $Z$ by affine open subsets $\{Z_i\}$, we know that fiber products $X_i\times_{Z_i}Y_i$ exist for $\varphi_X\vert^{Z_i}:\varphi_X^{-1}(Z_i) \rightarrow Z_i$ and $\varphi_Y\vert^{Z_i}:\varphi_Y^{-1}(Z_i) \rightarrow Z_i$. Now the intersection $Z_{ij}=Z_i\cap Z_j$ is an open subset of $Z_i$, so by [Lemma 7](#lem7) the fiber products of $\varphi_X\vert^{Z_{ij}}$ and $\varphi_Y\vert^{Z_{ij}}$ also exist and are open subschemes of both $X_i\times_{Z_i}Y_i$ and $X_j\times_{Z_j}Y_j$. Therefore, just as in the proof of [Lemma 5](#lem5), if we show that these data satisfy the conditions of [§Schemes, ⁋Lemma 9](/en/math/scheme_theory/schemes#lem9), we obtain the following theorem.

::: Theorem 8
For arbitrary schemes $X,Y,Z$ and scheme morphisms $X \rightarrow Z$, $Y \rightarrow Z$, the fiber product $X\times_ZY$ exists.
:::
::: Proof
What is needed for gluing is that the open subsets corresponding to the fiber product over $Z_{ij}$ inside the two pieces $X_i\times_{Z_i}Y_i$ and $X_j\times_{Z_j}Y_j$ are canonically identified, and that these identifications satisfy the cocycle condition on triple intersections. However, since both open subsets satisfy the universal property of the fiber product of $\varphi_X\vert^{Z_{ij}}$ and $\varphi_Y\vert^{Z_{ij}}$, the identification between them is uniquely determined, and the three identifications obtained on the triple intersection are also the unique morphisms given by the universal property of the fiber product over $Z_{ijk}=Z_i\cap Z_j\cap Z_k$; hence the composition of any two of them equals the third, so the cocycle condition holds. Therefore by [§Schemes, ⁋Lemma 9](/en/math/scheme_theory/schemes#lem9) they glue into a single scheme.

That the scheme thus obtained satisfies the universal property is the same as in the proof of [Lemma 5](#lem5). That is, if morphisms $\alpha: W \rightarrow X$, $\beta: W \rightarrow Y$ agree over $Z$, set $W_i=(\varphi_X\circ \alpha)^{-1}(Z_i)$, obtain the unique morphism to $X_i\times_{Z_i}Y_i$ on each $W_i$, and then verify agreement on overlaps by the uniqueness in the universal property as above, and glue.
:::

## Interpretations of the Fiber Product

Just as there are various ways to interpret a scheme morphism, there are various ways to understand the fiber product.

Earlier we agreed to think of a scheme morphism $X \rightarrow S$ as a family parametrized by $S$ ([§Morphisms of Schemes, ⁋Example 10](/en/math/scheme_theory/morphism_of_schemes#ex10)); from this viewpoint $S$ can be thought of as the base of the family $X$. Now, given an arbitrary $S$-family $X \rightarrow S$ and a scheme morphism $S' \rightarrow S$, through the fiber product we obtain a new $S'$-family $X\times_SS' \rightarrow S'$. From this perspective we often call the fiber product a *base change*.

::: Example 9
Narrowing our scope to affine schemes, $\Spec B$ being a $C$-scheme means that a scheme morphism $\Spec B \rightarrow \Spec C$ is given, which in turn is the same as a ring homomorphism $C \rightarrow B$ being given, which is again the same as saying that $B$ is a $C$-algebra.

Now, given in addition a scheme morphism $\Spec A \rightarrow \Spec C$, let us see what the above base change yields; by [Lemma 2](#lem2) we know that what is obtained in this way is

$$\Spec A\times_{\Spec C}\Spec B=\Spec(A\otimes_CB) \rightarrow \Spec A,$$

that is, the ring homomorphism $A \rightarrow A\otimes_CB$. In other words, base change is (in the case of affine schemes) nothing other than [\[Algebraic Structures\] §Change of Base Ring, ⁋Definition 3](/en/math/algebraic_structures/change_of_base_ring#def3).
:::

In particular, for the $B$-algebra $B[\x_1,\ldots,\x_n]$ and an arbitrary ring homomorphism $B \rightarrow A$, from the identity

$$A\otimes_BB[\x_1,\ldots,\x_n]\cong A[\x_1,\ldots, \x_n]$$

we know that the following diagram

{% diagram Math/Scheme_Theory/Fiber_Products-7.svg width="20.67em" alt="adding_extra_variables" %}

is a fiber diagram.

This viewpoint is important, but for the moment the geometric intuition here is not very visible. For this, let us think particularly of the case where $S' \rightarrow S$ is an embedding.

First, for an arbitrarily given $S$-family $X \rightarrow S$ and an open embedding $S' \rightarrow S$, [Lemma 3](#lem3) shows that the $S'$-family $X\times_SS' \rightarrow S'$ is simply obtained by restricting the base of $X \rightarrow S$ to $S'$. Moreover, if we also assume that $X \rightarrow S$ is an open embedding, we know that $X\times_SS'$ is the intersection of $X$ and $S'$ (inside $S$).

The above argument also works in the case of a closed embedding. For this we need the following lemma corresponding to [Lemma 3](#lem3).

::: Lemma 10
For a ring homomorphism $\phi: B \rightarrow A$ and an arbitrary ideal $\mathfrak{b}$ of $B$, there exists an isomorphism

$$A/\phi(\mathfrak{b})A\cong A \otimes_B(B/\mathfrak{b}).$$
:::
::: Proof
From the ideal $\mathfrak{b}$ we have the exact sequence

$$\mathfrak{b} \rightarrow B \rightarrow B/\mathfrak{b} \rightarrow 0,$$

and taking $\otimes_BA$ yields the exact sequence

$$A\otimes_B \mathfrak{b} \rightarrow A\otimes_BB \rightarrow A\otimes_B (B/\mathfrak{b}) \rightarrow 0,$$

and since the image of $A\otimes_B \mathfrak{b}$ in $A\otimes_BB\cong A$ is $\phi(\mathfrak{b})A$, we obtain the desired result.
:::

Now, since an arbitrary closed embedding locally always comes from $B \rightarrow B/\mathfrak{b}$, the above discussion applies equally to closed embeddings. In particular, the intersection of two closed embeddings is well defined.

::: Example 11
Consider the two closed subschemes of $Z=\Spec\mathbb{K}[\x,\y]$

$$X=\Spec \mathbb{K}[\x,\y]/(\y)=\Spec \mathbb{K}[\x],\qquad Y=\Spec \mathbb{K}[\x,\y]/(\x)=\Spec \mathbb{K}[\y].$$

Then $X$ and $Y$ correspond respectively to the $\x$-axis and $\y$-axis of $Z=\mathbb{A}^2_\mathbb{K}$, and their closed embeddings are given by the projections

$$\mathbb{K}[\x,\y] \rightarrow \mathbb{K}[\x],\qquad \mathbb{K}[\x,\y] \rightarrow \mathbb{K}[\y].$$

Now $X\times_ZY$ is, by [Lemma 2](#lem2),

$$\Spec\left(\frac{\mathbb{K}[\x,\y]}{(\x)}\otimes_{\mathbb{K}[\x,\y]} \frac{\mathbb{K}[\x,\y]}{(\y)}\right)\cong \Spec \mathbb{K}[\x,\y]/(\x,\y)\cong\Spec \mathbb{K},$$

which corresponds exactly to the origin, the intersection point of the $\x$-axis and $\y$-axis.

Now let us replace $Y$ in the above computation by the following closed subscheme:

$$Y=\Spec \mathbb{K}[\x,\y]/(\y-\x^2).$$

The intersection of $\y=\x^2$ and the $\x$-axis is again the origin, but this time a double root exists so the scheme structure must be given differently. Indeed, repeating the computation, $X\times_ZY$ becomes

$$\Spec\left(\frac{\mathbb{K}[\x,\y]}{(\y)}\otimes_{\mathbb{K}[\x,\y]}\frac{\mathbb{K}[\x,\y]}{(\y-\x^2)}\right)\cong\Spec \mathbb{K}[\x,\y]/(\y,\y-\x^2)\cong\Spec \mathbb{K}[\x]/(\x^2).$$
:::

From this viewpoint we can also see how to define the fiber $\varphi^{-1}(y_0)$ of a scheme morphism $\varphi:X \rightarrow Y$ at a point $y_0\in Y$. We construct a morphism from a one-point scheme to $Y$ containing only $y_0$, and then take the fiber product of this morphism with $\varphi$. Here we must be careful that we cannot take the one-point set $\{y_0\}$ as a subspace of $Y$ and use an embedding. If $y_0$ is not a closed point, $\{y_0\}$ is generally not even a locally closed subset of $Y$; for instance, the generic point of $\mathbb{A}^2$ is such a case.

Now, to construct $\iota$, consider the residue field $\kappa(y)$ at $y$. Then $\Spec\kappa(y)$ is always a one-point set. Moreover, taking an affine open subset $V=\Spec B$ of $Y$ containing $y$, and letting $y$ correspond to the prime ideal $\mathfrak{q}_y$, through the canonical morphism

$$B \rightarrow B_{\mathfrak{q}_y} \rightarrow B_{\mathfrak{q}_y}/\mathfrak{q}_y B_{\mathfrak{q}_y} =\kappa(\mathfrak{q}_y)=\kappa(y)$$

we define $\Spec\kappa(y)\rightarrow \Spec B$, and the (unique) point $(0)$ of $\Spec \kappa(y)$ is sent to $\mathfrak{q}_y$ via the above morphism. Hence we define the following.

::: Definition 12
For a scheme morphism $\varphi: X \rightarrow Y$, the *fiber* at a point $y\in Y$ is defined by

$$\varphi^{-1}(y)=X\times_Y\Spec \kappa(y).$$

If $Y$ is irreducible, the fiber at the generic point of $Y$ is called the *generic fiber*.
:::

This definition uses the same symbol as the preimage as a continuous map, and indeed the two coincide as topological spaces.

::: Lemma 13
For a scheme morphism $\varphi: X \rightarrow Y$ and $y\in Y$, the projection $X\times_Y\Spec\kappa(y) \rightarrow X$ is a homeomorphism onto the set-theoretic preimage $\{x\in X\mid \varphi(x)=y\}$.
:::
::: Proof
By [Lemma 4](#lem4), forming the fiber product is compatible with restricting $X$ and $Y$ to open subsets, so it suffices to choose an affine open subset $V$ with $y\in V=\Spec B$, cover $\varphi^{-1}(V)$ by affine open subsets $\Spec A$, and treat only the case $X=\Spec A$, $Y=\Spec B$. Let $\mathfrak{q}$ be the prime ideal corresponding to $y$, and let $\phi: B \rightarrow A$ be the ring homomorphism corresponding to $\varphi$.

By [Lemma 2](#lem2) we have $X\times_Y\Spec \kappa(\mathfrak{q})=\Spec (A\otimes_B\kappa(\mathfrak{q}))$. On the other hand, since $\kappa(\mathfrak{q})=B_\mathfrak{q}/\mathfrak{q}B_\mathfrak{q}$, letting $S=\phi(B\setminus \mathfrak{q})$ we have

$$A\otimes_B\kappa(\mathfrak{q})\cong (S^{-1}A)/\mathfrak{q}(S^{-1}A).$$

Then, applying [§The Spectrum, ⁋Proposition 9](/en/math/scheme_theory/spectrums#prop9) twice, $\Spec (A\otimes_B\kappa(\mathfrak{q})) \rightarrow \Spec A$ is a homeomorphism onto its image, and its image is the collection of prime ideals $\mathfrak{p}\in \Spec A$ satisfying both $\phi^{-1}(\mathfrak{p})\subseteq \mathfrak{q}$ and $\mathfrak{q}\subseteq \phi^{-1}(\mathfrak{p})$, that is, exactly the set of points with $(\Spec\phi)(\mathfrak{p})=\mathfrak{q}$.
:::

::: Example 14
For an algebraically closed field $\mathbb{K}$, define the ring homomorphism $\mathbb{K}[\x] \rightarrow \mathbb{K}[\y]$ by $\x \mapsto \y^2$, and consider the resulting scheme morphism $\varphi: \Spec \mathbb{K}[\y] \rightarrow \Spec \mathbb{K}[\x]$. Then the residue field at any point $(\x-a)$ of $\Spec\mathbb{K}[\x]$ is

$$\Frac(\mathbb{K}[\x]/(\x-a))=\mathbb{K}[\x]/(\x-a).$$

Now for arbitrary $a\in \mathbb{K}$,

$$\varphi^{-1}((\x-a))=\Spec \mathbb{K}[\y]\times_{\Spec \mathbb{K}[\x]}\Spec \mathbb{K}[\x]/(\x-a)\cong \Spec(\mathbb{K}[\y]\otimes_{\mathbb{K}[\x]}\mathbb{K}[\x]/(\x-a))=\Spec \mathbb{K}[\y]/(\y^2-a),$$

and therefore if $a=0$ then $\varphi^{-1}((\x))\cong\Spec \mathbb{K}[\y]/(\y^2)$, while if $a\neq 0$ then from the assumption that $\mathbb{K}$ is algebraically closed we know

$$\Spec \mathbb{K}[\y]/(\y^2-a)\cong \Spec \mathbb{K}[\y]/(\y-\sqrt{a})\coprod \Spec \mathbb{K}[\y]/(\y+\sqrt{a}).$$

On the other hand, for the generic point $(0)$ of $\mathbb{K}[\x]$ we have $\kappa((0))=\mathbb{K}(\x)$, so

$$\varphi^{-1}((0))=\Spec \mathbb{K}[\y]\times_{\Spec \mathbb{K}[\x]}\Spec \mathbb{K}(\x)\cong \Spec\mathbb{K}(\y).$$
:::

The above example is what we already examined in [§Properties of Scheme Morphisms, ⁋Example 16](/en/math/scheme_theory/properties_of_scheme_morphisms#ex16). In that example we claimed that a finite morphism is always quasi-finite, and now we can prove this.

::: Proposition 15
A finite morphism $\varphi: X \rightarrow Y$ is a quasi-finite morphism.
:::
::: Proof
By [Lemma 13](#lem13) the points of the set $\varphi^{-1}(y)$ are in one-to-one correspondence with the points of the scheme $X\times_Y\Spec\kappa(y)$, so it suffices to count the latter. Then it suffices to treat the affine case. That is, it suffices to show that for an arbitrary finite ring homomorphism $\phi: B \rightarrow A$ and a prime ideal $\mathfrak{q}$ of $B$, the ring $A\otimes_B\kappa(\mathfrak{q})$ has only finitely many prime ideals. But since $\phi$ is finite, $A\otimes_B\kappa(\mathfrak{q})$ is a finite $\kappa(\mathfrak{q})$-algebra and hence Artinian, from which we obtain the desired result. ([\[Commutative Algebra\] §The Jordan-Hölder Theorem, ⁋Theorem 4](/en/math/commutative_algebra/Jordan-Holder_theorem#thm4))
:::

From the above examples and propositions we can make an important observation: many properties satisfied by $X \rightarrow S$ are also inherited by the base change $X\times_SS' \rightarrow S'$ for arbitrary $S' \rightarrow S$. Of course not all properties are like this. For instance, dominant is not preserved: $\Spec \mathbb{K}(\t) \rightarrow \Spec \mathbb{K}[\t]$ is a dominant morphism to the generic point, but base changing along $\t=0$ yields a morphism from the empty set to a point. However, most properties we care about are closed under base change.

::: Proposition 16
If a scheme morphism $\varphi:X \rightarrow Z$ is quasicompact (resp. quasiseparated, affine, finite, integral, locally of finite type, finite type, locally of finite presentation, finite presentation, quasi-finite, surjective), then the base change $X\times_ZY \rightarrow Y$ of $\varphi$ via an arbitrary scheme morphism $Y \rightarrow Z$ is also such.
:::
::: Proof
Let us first carry out a reduction common to all properties. Choose the $\Spec A$ forming an affine open covering of $Z$, and for each $\Spec A$ cover its preimage under $Y \rightarrow Z$ by affine open subsets $\Spec C$; the $\Spec C$ thus obtained form an affine open covering of $Y$. Now letting the projection be $\rho_Y: X\times_ZY \rightarrow Y$, from the fact used in the proofs of [Lemma 3](#lem3) and [Lemma 4](#lem4) that "if the two small squares are fiber diagrams then the outer large square is also a fiber diagram," we obtain

$$\rho_Y^{-1}(\Spec C)\cong X\times_Z\Spec C\cong \varphi^{-1}(\Spec A)\times_{\Spec A}\Spec C.$$

Hence, writing $X_A=\varphi^{-1}(\Spec A)$ and $W=X_A\times_{\Spec A}\Spec C$, examining the base change $\rho_Y$ over $\Spec C$ is the same as examining the base change $W \rightarrow \Spec C$ of $X_A \rightarrow \Spec A$ along $\Spec C \rightarrow \Spec A$. Moreover, for the same reason, for an arbitrary affine open subset $\Spec B$ of $X_A$, its preimage under the projection $\rho: W \rightarrow X_A$ is by [Lemma 2](#lem2)

$$\rho^{-1}(\Spec B)\cong \Spec B\times_{\Spec A}\Spec C\cong \Spec (B\otimes_AC),$$

so whenever an affine open covering $\{\Spec B_i\}$ of $X_A$ is given, $\{\Spec (B_i\otimes_AC)\}$ becomes an affine open covering of $W$. That is, every problem reduces to a problem about the ring homomorphism $C \rightarrow B\otimes_AC$. We now examine each property.

First, suppose $\varphi$ is affine. Then $X_A$ is an affine scheme $\Spec B$, and hence $\rho_Y^{-1}(\Spec C)=W\cong\Spec (B\otimes_AC)$ is affine; therefore by the affine open covering $\{\Spec C\}$ of $Y$ and [§Properties of Scheme Morphisms, ⁋Proposition 9](/en/math/scheme_theory/properties_of_scheme_morphisms#prop9), $\rho_Y$ is affine.

Suppose $\varphi$ is quasi-compact. Then $X_A$ is quasi-compact, so it is covered by finitely many affine open subsets $\Spec B_1,\ldots, \Spec B_n$, and hence $W$ is covered by finitely many affine open subsets $\Spec (B_i\otimes_AC)$ and is quasi-compact. Now by the first result of [§Properties of Scheme Morphisms, ⁋Proposition 7](/en/math/scheme_theory/properties_of_scheme_morphisms#prop7), $\rho_Y$ is quasi-compact.

Suppose $\varphi$ is quasi-separated. Then $X_A$ is a quasi-separated scheme. Choosing an affine open covering $\{\Spec B_i\}$ of $X_A$, $\{W_i=\Spec (B_i\otimes_AC)\}$ is an affine open covering of $W$, and since $\Spec B_i\cap \Spec B_j$ is quasi-compact it can be written as a union of finitely many principal open sets $D(h_1),\ldots, D(h_s)$ of $\Spec B_i$ ([§The Spectrum, ⁋Lemma 11](/en/math/scheme_theory/spectrums#lem11)), so

$$W_i\cap W_j=\rho^{-1}(\Spec B_i\cap \Spec B_j)=\bigcup_{t=1}^s\Spec \bigl((B_i)_{h_t}\otimes_AC\bigr)$$

is a union of finitely many affine open subsets, hence quasi-compact. Now let us show in general that if a scheme $W$ has an affine open covering $\{W_i\}$ such that all $W_i\cap W_j$ are quasi-compact, then $W$ is quasi-separated. Since an arbitrary quasi-compact open subset of $W$ is a union of finitely many affine open subsets, it suffices to show that for arbitrary two affine open subsets $P,Q$ of $W$, $P\cap Q$ is quasi-compact. By [§The Topological Structure of Schemes, ⁋Lemma 11 (Nike)](/en/math/scheme_theory/topology_of_schemes#lem11) and the quasi-compactness of $P,Q$, both $P$ and $Q$ are covered by finitely many open sets that are principal in both themselves and some $W_i$; hence ultimately it suffices to show that $D(f)\cap D(g)$ is quasi-compact for a principal open set $D(f)$ of $W_i$ and a principal open set $D(g)$ of $W_j$. But $D(f)\cap D(g)\subseteq W_i\cap W_j$ and $W_i\cap W_j$ is quasi-compact, so it can be written as a union of finitely many principal open sets $D(h_1),\ldots, D(h_s)$ of $W_i$, and therefore

$$D(f)\cap D(g)=\bigcup_{t=1}^s\bigl(D(fh_t)\cap D(g)\bigr).$$

Here each $D(fh_t)$ is an affine open subset contained in $W_i\cap W_j$; viewing this as an affine open subset of $W_j$, $D(fh_t)\cap D(g)$ is the principal open set defined by the restriction of $g$ on the affine scheme $D(fh_t)$ ([§The Spectrum, ⁋Proposition 8](/en/math/scheme_theory/spectrums#prop8)), and hence is affine. That is, $D(f)\cap D(g)$ is a union of finitely many affine open subsets, so it is quasi-compact. From the above, $W$ is quasi-separated, and by the second result of [§Properties of Scheme Morphisms, ⁋Proposition 7](/en/math/scheme_theory/properties_of_scheme_morphisms#prop7), $\rho_Y$ is quasi-separated.

Suppose $\varphi$ is integral (resp. finite). Then $\varphi$ is affine, so $X_A=\Spec B$ and $A \rightarrow B$ is integral (resp. finite). Hence $\rho_Y^{-1}(\Spec C)=\Spec (B\otimes_AC)$, and by [\[Commutative Algebra\] §Integral Extensions, ⁋Proposition 14](/en/math/commutative_algebra/integral_extension#prop14), $C \rightarrow B\otimes_AC$ is also integral (resp. finite). That these two properties are affine-local on the target was examined right after [§Properties of Scheme Morphisms, ⁋Definition 11](/en/math/scheme_theory/properties_of_scheme_morphisms#def11), so it suffices to have checked this over the affine open covering $\{\Spec C\}$ of $Y$.

Suppose $\varphi$ is locally of finite type. Choosing an affine open covering $\{\Spec B_i\}$ of $X_A$, each $A \rightarrow B_i$ is of finite type; letting $x_1,\ldots, x_n$ be generators of $B_i$ as an $A$-algebra, $B_i\otimes_AC$ is generated as a $C$-algebra by $x_1\otimes 1,\ldots, x_n\otimes 1$, so $C \rightarrow B_i\otimes_AC$ is also of finite type. Now we must obtain the same conclusion for *every* affine open subset of $W$; this is obtained by applying [§Properties of Scheme Morphisms, ⁋Lemma 13](/en/math/scheme_theory/properties_of_scheme_morphisms#lem13) to the affine open covering $\{\Spec (B_i\otimes_AC)\}$ just constructed. That is, $\rho_Y$ is locally of finite type. Also, a morphism of finite type is a morphism that is quasi-compact and locally of finite type, so combining with the quasi-compact case above, finite type is also preserved under base change.

Suppose $\varphi$ is locally of finite presentation. The condition of [§Properties of Scheme Morphisms, ⁋Definition 18](/en/math/scheme_theory/properties_of_scheme_morphisms#def18) is a condition on *some* affine open covering of the preimage, so this case is rather simpler. By hypothesis there exists an affine open covering $\{\Spec B_i\}$ of $X_A$ such that each $B_i$ has the form

$$B_i\cong A[\x_1,\ldots, \x_n]/(f_1,\ldots, f_m),$$

and then by the isomorphism $C\otimes_AA[\x_1,\ldots, \x_n]\cong C[\x_1,\ldots, \x_n]$ examined after [Example 9](#ex9) and by [Lemma 10](#lem10),

$$B_i\otimes_AC\cong C[\x_1,\ldots, \x_n]/(\bar{f}_1,\ldots, \bar{f}_m)$$

(where $\bar{f}_k$ sends the coefficients of $f_k$ to $C$), so $C \rightarrow B_i\otimes_AC$ is also finitely presented. That is, the affine open covering $\{\Spec (B_i\otimes_AC)\}$ of $W$ witnesses the required condition over $\Spec C$. That this property is affine-local on the target is obtained by applying [§The Topological Structure of Schemes, ⁋Lemma 12](/en/math/scheme_theory/topology_of_schemes#lem12) to the property "$\varphi^{-1}(\Spec B)$ has an affine open covering $\{\Spec R_i\}$ such that all $B \rightarrow R_i$ are finitely presented." Indeed, the first condition of [§The Topological Structure of Schemes, ⁋Definition 9](/en/math/scheme_theory/topology_of_schemes#def9) follows from the fact that $\varphi^{-1}(D(f))$ is covered by $\Spec (R_i)_f$ and $(R_i)_f\cong R_i\otimes_BB_f$ is a base change of a finitely presented homomorphism; the second condition follows from the fact that $B \rightarrow B_f\cong B[\y]/(f\y-1)$ is finitely presented and the composition of finitely presented homomorphisms is again finitely presented. Finally, a morphism of finite presentation is a morphism that is quasi-compact, quasi-separated, and locally of finite presentation, so combining the preceding results this property is also preserved under base change.

Now let us compute fibers for the remaining two properties. For $y\in Y$ and its image $z\in Z$, since $\mathcal{O}_{Z,z} \rightarrow \mathcal{O}_{Y,y}$ is a local homomorphism, $\Spec \kappa(y) \rightarrow Y \rightarrow Z$ factors through $\Spec\kappa(z) \rightarrow Z$; hence, composing fiber diagrams as above, by [Definition 12](#def12) we obtain

$$\rho_Y^{-1}(y)=(X\times_ZY)\times_Y\Spec \kappa(y)\cong X\times_Z\Spec \kappa(y)\cong \varphi^{-1}(z)\times_{\Spec \kappa(z)}\Spec \kappa(y).$$

Also, by [Lemma 3](#lem3), for an affine open subset $\Spec R$ of $\varphi^{-1}(z)$, the scheme $\Spec (R\otimes_{\kappa(z)}\kappa(y))$ is an open subset of $\rho_Y^{-1}(y)$, and such schemes cover $\rho_Y^{-1}(y)$.

Suppose $\varphi$ is surjective. First we verify that $\varphi^{-1}(z)$ is nonempty. Choose $x\in X$ with $\varphi(x)=z$, and choose an affine open subset $\Spec B\subseteq X$ containing $x$ and mapping into $\Spec A$ under $\varphi$, with corresponding ring homomorphism $\phi:A \rightarrow B$. Let $\mathfrak{q}\subseteq B$, $\mathfrak{p}\subseteq A$ be the prime ideals corresponding to $x$ and $z$ respectively; then $\phi^{-1}(\mathfrak{q})=\mathfrak{p}$, and by [Lemma 10](#lem10) and the properties of localization,

$$B\otimes_A\kappa(\mathfrak{p})\cong (B/\mathfrak{p}B)_\mathfrak{p},$$

so $\mathfrak{q}$ defines a prime ideal of this ring. That is, $\varphi^{-1}(z)\neq\emptyset$. Now choosing a nonempty affine open subset $\Spec R$ of $\varphi^{-1}(z)$, $R$ is a nonzero $\kappa(z)$-algebra, and since $\kappa(y)$ is a nonzero $\kappa(z)$-vector space, $R\otimes_{\kappa(z)}\kappa(y)\neq 0$. A nonzero ring always has a prime ideal, so $\Spec (R\otimes_{\kappa(z)}\kappa(y))\neq\emptyset$, and hence $\rho_Y^{-1}(y)\neq\emptyset$. Since $y$ was arbitrary, $\rho_Y$ is surjective.

Finally, suppose $\varphi$ is quasi-finite. Since $\varphi$ is of finite type, $\rho_Y$ is also of finite type as seen above, so it suffices to show that all fibers of $\rho_Y$ are finite sets. Since $\varphi$ is quasi-compact, applying preservation of quasi-compactness under base change to $\Spec \kappa(z) \rightarrow Z$, we know that $\varphi^{-1}(z)$ is quasi-compact, and hence can be covered by finitely many affine open subsets $\Spec R_1,\ldots, \Spec R_n$. Likewise, since $\varphi$ is locally of finite type, each $R_l$ is a finite type $\kappa(z)$-algebra, and by hypothesis each $\Spec R_l$ is a finite set.

Now let us show that a finite type $\mathbb{K}$-algebra $R$ having only finitely many prime ideals is always a finite-dimensional $\mathbb{K}$-vector space. First we show that an arbitrary prime ideal $\mathfrak{p}$ of $R$ is maximal. If there existed a prime ideal properly containing $\mathfrak{p}$, then $d=\dim R/\mathfrak{p}\geq 1$, and by [\[Commutative Algebra\] §Noether Normalization, ⁋Theorem 1](/en/math/commutative_algebra/noether_normalization#thm1), $R/\mathfrak{p}$ contains the polynomial ring $\mathbb{K}[\x_1,\ldots, \x_d]$ as a subring and is finitely generated, hence an integral extension over it. But since $d\geq 1$, $\mathbb{K}[\x_1,\ldots, \x_d]$ has infinitely many prime ideals generated by distinct irreducible polynomials of $\mathbb{K}[\x_1]$, and by [\[Commutative Algebra\] §Integral Extensions and Ideals, ⁋Proposition 1](/en/math/commutative_algebra/lying_over_and_going_up#prop1) above each of these lies a prime ideal of $R/\mathfrak{p}$; this contradicts the hypothesis that $R$ has only finitely many prime ideals. Hence every prime ideal of $R$ is maximal, and by [\[Commutative Algebra\] §Basic Notions, ⁋Theorem 12](/en/math/commutative_algebra/basic_notions#thm12) $R$ is Noetherian, so by [\[Commutative Algebra\] §The Jordan-Hölder Theorem, ⁋Theorem 4](/en/math/commutative_algebra/Jordan-Holder_theorem#thm4) $R$ has finite length as an $R$-module. Here the composition factors are all of the form $R/\mathfrak{m}$; since a field is a Jacobson ring, by [\[Commutative Algebra\] §Nullstellensatz, ⁋Theorem 4](/en/math/commutative_algebra/nullstellensatz#thm4) $R/\mathfrak{m}$ is a finite extension of $\mathbb{K}$. Therefore $R$ is a finite-dimensional $\mathbb{K}$-vector space.

Then each $R_l$ is a finite-dimensional $\kappa(z)$-vector space, so $R_l\otimes_{\kappa(z)}\kappa(y)$ is also a finite-dimensional $\kappa(y)$-vector space, and hence becomes an Artinian ring having only finitely many prime ideals. ([\[Commutative Algebra\] §The Jordan-Hölder Theorem, ⁋Theorem 4](/en/math/commutative_algebra/Jordan-Holder_theorem#thm4)) Now $\rho_Y^{-1}(y)$ is covered by finitely many $\Spec (R_l\otimes_{\kappa(z)}\kappa(y))$, so it is a finite set, and thus we know that $\rho_Y$ is quasi-finite.
:::

---

**References**

**[Har]** R. Hartshorne, *Algebraic geometry*. Graduate texts in mathematics. Springer, 1977.  
**[Vak]** R. Vakil, *The rising sea: Foundation of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/).
