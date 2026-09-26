---
title: "Fiber Products"
description: "This post covers the definition and universal property of fiber products between schemes and proves their existence for affine schemes."
excerpt: "Definition and existence of fiber products in the category of S-schemes"

categories: [Math / Scheme Theory]
permalink: /en/math/scheme_theory/fiber_products
sidebar: 
    nav: "scheme_theory-en"

date: 2025-03-08
weight: 12
translated_at: 2026-09-26T19:15:06+00:00
translation_source: antigravity-gemini-3.8-flash-high
---
One of the things we promised when introducing schemes was the fiber product. Since this is the product on $\Sch_{/S}$, we needed to define $S$-schemes (and scheme morphisms) for this purpose. Having completed the preparations, we now define the fiber product. 

## Definition and Existence of Fiber Products

In [§Morphisms of Schemes, ⁋Definition 3](/en/math/scheme_theory/morphism_of_schemes#def3){: data-lid="rnkqe" }, we agreed to call a scheme morphism $X \rightarrow S$ an *$S$-scheme*. In this post, we will define the product in the category $\Sch_{/S}$. 

::: Definition 1
We denote the fiber product of two scheme morphisms $\varphi_X:X \rightarrow S$ and $\varphi_Y:Y \rightarrow S$ by $X\times_SY$. ([\[Category Theory\] §Limits, ⁋Example 8](/en/math/category_theory/limits#ex8){: data-lid="rrznl" })
:::

That is, $X\times_SY$ satisfies the following property:

> The diagram
> 
> {% diagram Math/Scheme_Theory/Fiber_Products-1.svg width="9.32em" alt="fiber_diagram" %}
> 
> commutes. Moreover, whenever the condition $\varphi_Y\circ\psi_Y=\varphi_X\circ\psi_X$ is satisfied by any given $\psi_X:Z \rightarrow X$ and $\psi_Y:Z \rightarrow Y$, there exists a unique $\psi:Z \rightarrow X\times_SY$ such that $\psi_X=\rho_X\circ\psi$ and $\psi_Y=\rho_Y\circ\psi$.
> 
> {% diagram Math/Scheme_Theory/Fiber_Products-2.svg width="13.72em" alt="universal_product" %}

Therefore, there exists a canonical morphism from $X\times_SY$ to $S$, and from this we can view $X\times_SY$ as an $S$-scheme. Furthermore, from this perspective, it is clear from the definition that $X\times_SY$ is also the product in $\Sch_{/S}$.

After [§Morphisms of Schemes, ⁋Example 4](/en/math/scheme_theory/morphism_of_schemes#ex4){: data-lid="qctzu" }, we saw that any scheme $X$ can always be regarded as a $\mathbb{Z}$-scheme in a unique way. Therefore, assuming that the fiber product $X\times_SY$ satisfying [Definition 1](#def1){: data-lid="nz2tv" } always exists, we know that for any two schemes $X, Y$, the fiber product $X\times_{\Spec \mathbb{Z}}Y$ gives the product of $X$ and $Y$. 

Since [Definition 1](#def1){: data-lid="1nq1f" } does not guarantee anything about the existence of the fiber product $X\times_SY$, for this to be a genuine definition, we must separately prove the existence of $X\times_SY$. ([Theorem 8](#thm8){: data-lid="lvxz7" }) However, the existence of fiber products specifically in $\AffSch$ is almost trivial, and this will be the starting point of our proof.

::: Lemma 2
Suppose we are given morphisms $\Spec A \rightarrow \Spec C$ and $\Spec B \rightarrow\Spec C$ between affine schemes. Then

$$\Spec A\times_{\Spec C}\Spec B\cong\Spec (A\otimes_C B)$$

holds.
:::
::: Proof
Using $\AffSch\cong\cRing^\op$, we convert $\Spec A \rightarrow \Spec C$ and $\Spec B \rightarrow \Spec C$ into $C \rightarrow A$ and $C \rightarrow B$, and then compare the universal property of [\[Algebraic Structures\] §Direct Product, Direct Sum, and Tensor Product of Algebras, ⁋Theorem 8](/en/math/algebraic_structures/operations_of_algebras#thm8){: data-lid="sje3o" } with the universal property of the fiber product. That this comparison holds not only for affine schemes but also when taking an arbitrary scheme $T$ as a test object is because by [§Affine Scheme, ⁋Theorem 13](/en/math/scheme_theory/affine_schemes#thm13){: data-lid="y9wc9" }, for any ring $R$, we have $\Hom_\Sch(T, \Spec R)\cong \Hom_\cRing(R, \Gamma(T))$.
:::

Now, to show that fiber products exist for general schemes, it suffices to show, based on the result for affine schemes examined in [Lemma 2](#lem2){: data-lid="ophvg" }, that we can glue them together properly. 

First, for $Z$, given an open subscheme $U$, if we write it in the form $\iota:U \rightarrow Z$ using the inclusion morphism, the following lemma is almost a tautology. 

::: Lemma 3
Suppose we are given a scheme morphism $\varphi: Y \rightarrow Z$ and an open subscheme of $Z$, $\iota: U \rightarrow Z$. Then the diagram

{% diagram Math/Scheme_Theory/Fiber_Products-3.svg width="8.22em" alt="open_subscheme" %}

is a fiber diagram.
:::
::: Proof
$\varphi^{-1}(U)$ satisfies the universal property of the fiber product. 
:::

Now, by using this slightly, we can prove the following lemma.

::: Lemma 4
Suppose we are given affine schemes $X, Y, Z$ and an open subscheme $Y'\hookrightarrow Y$ of $Y$. Then, for $X\rightarrow Z$ and $Y'\hookrightarrow Y \rightarrow Z$, the fiber product $X\times_ZY'$ exists.
:::
::: Proof
First, from [Lemma 2](#lem2){: data-lid="qjfbm" }, we know that the following fiber diagram 

{% diagram frozen/635a8f80/Math/Scheme_Theory/Fiber_Products-4.svg width="9.32em" alt="open_fiber_product-1" %}

exists. Now, considering the following data

{% diagram frozen/635a8f80/Math/Scheme_Theory/Fiber_Products-5.svg width="8.55em" alt="open_fiber_product-2" %}

we can verify from [Lemma 3](#lem3){: data-lid="oi087" } that the open subscheme of $X\times_ZY$ given by $\rho_Y^{-1}(Y')$ is a fiber product. Now, in general, in the following diagram

{% diagram frozen/635a8f80/Math/Scheme_Theory/Fiber_Products-6.svg width="8.55em" alt="magic_square" %}

if the two smaller squares are fiber diagrams, then the outer large square is also a fiber diagram, which gives the desired result. 
:::

Using this, we can now show that the fiber product of an affine scheme and an arbitrary scheme exists.

::: Lemma 5
For affine schemes $X, Z$ and an arbitrary scheme $Y$, the fiber product of $X\rightarrow Z$ and $Y \rightarrow Z$, denoted $X\times_ZY$, exists.
:::
::: Proof
To this end, let us cover $Y$ by affine open subsets $Y_i$. Then from [Lemma 2](#lem2){: data-lid="7oosl" } we know that the $X\times_ZY_i$ exist. Also, since $Y_{ij}=Y_i\cap Y_j$ is an open subscheme of the affine scheme $Y_i$, $X\times_Z Y_{ij}$ also exists by [Lemma 4](#lem4){: data-lid="rtja6" }. 

Meanwhile, from the proof of [Lemma 4](#lem4){: data-lid="2vf31" }, we see that each $X\times_ZY_{ij}$ is an open subscheme of $X\times_ZY_i$ and $X\times_ZY_j$, respectively. Since it is easy to verify that these data satisfy the conditions of [§Schemes, ⁋Lemma 9](/en/math/scheme_theory/schemes#lem9){: data-lid="8yjcz" }, we can glue them to construct a scheme $X\times_ZY$. That this satisfies the universal property of the fiber product is verified as follows. Suppose a scheme $W$ and morphisms $\alpha: W \rightarrow X$, $\beta: W \rightarrow Y$ agree over $Z$, and let $W_i=\beta^{-1}(Y_i)$. Then restricting $\beta$ to $W_i$ defines $W_i \rightarrow Y_i$, so from the universal property of $X\times_ZY_i$ we obtain a unique morphism $\sigma_i: W_i \rightarrow X\times_ZY_i$. Now on $W_i\cap W_j=\beta^{-1}(Y_{ij})$, both $\sigma_i$ and $\sigma_j$ are equal to the unique morphism given by the universal property of $X\times_ZY_{ij}$ and hence agree; therefore, by [§Morphisms of Schemes, ⁋Proposition 1](/en/math/scheme_theory/morphism_of_schemes#prop1){: data-lid="crwa5" }, they glue into a unique morphism $\sigma: W \rightarrow X\times_ZY$. Here, one should note that rather than restricting the codomain to $Y_i$, we restrict the domain to $W_i$, because there is no reason for the image of $\beta$ to be contained in $Y_i$. 
:::

In this lemma, the assumption that $X$ is an affine scheme was used only to show that $X\times_ZY_i$ exists. Therefore, given two arbitrary schemes $X,Y$, an affine scheme $Z$, and scheme morphisms $X \rightarrow Z$ and $Y \rightarrow Z$, we can choose an affine open cover of $Y$, denoted $\{Y_i\}$, and apply [Lemma 5](#lem5){: data-lid="8gdic" } with the roles of the two factors swapped. That is, since $Y_i$ and $Z$ are affine, $Y_i\times_ZX$ exists, and since the fiber product is symmetric with respect to the order of the two factors, $X\times_ZY_i$ exists. Moreover, since $Y_{ij}$ is an open subscheme of $Y_i$, in the same way as in the proof of [Lemma 4](#lem4){: data-lid="ufis7" }, $X\times_ZY_{ij}$ exists, which is an open subscheme of $X\times_ZY_i$ and $X\times_ZY_j$. Therefore, repeating verbatim the gluing argument in the proof of [Lemma 5](#lem5){: data-lid="rb3cb" }, we obtain the following.

::: Lemma 6
For an affine scheme $Z$, arbitrary schemes $X,Y$, and scheme morphisms $X \rightarrow Z$, $Y \rightarrow Z$, the fiber product $X\times_ZY$ exists. 
:::

Now, finally, we need to extend $Z$ to an arbitrary scheme. First, the following holds.

::: Lemma 7
Let $X,Y,Z$ be schemes, and suppose we are given scheme morphisms $\varphi_X:X \rightarrow Z$, $\varphi_Y:Y \rightarrow Z$ and a monomorphism $\iota: Z \rightarrow Z'$ into an affine scheme $Z'$. For instance, this includes the cases where $\iota$ is an open embedding or a closed embedding. In the latter case, if two morphisms $\alpha,\beta: T \rightarrow Z$ satisfy $\iota\circ \alpha=\iota\circ \beta$, then since $\iota$ is injective, $\alpha=\beta$ as continuous maps, and for each $t\in T$, $\iota^\sharp$ induces a surjection between stalks $\mathcal{O}_{Z',\iota(\alpha(t))} \rightarrow \mathcal{O}_{Z,\alpha(t)}$ ([§Closed Subschemes, ⁋Definition 2](/en/math/scheme_theory/closed_subschemes#def2){: data-lid="17l8f" }), so $\alpha^\sharp$ and $\beta^\sharp$ are determined by the composition and are equal to each other. Then the fiber product $X\times_{Z'}Y$ of $\iota\circ\varphi_X$ and $\iota\circ\varphi_Y$ satisfies the universal property of $X\times_ZY$, and therefore $X\times_ZY$ exists.  
:::
::: Proof
Since $Z'$ is affine, $X\times_{Z'}Y$ exists. Now let any scheme $T$ and morphisms $\alpha:T \rightarrow X$, $\beta:T \rightarrow Y$ be given. The condition required in the universal property of $X\times_ZY$ is $\varphi_X\circ \alpha=\varphi_Y\circ \beta$, and that of $X\times_{Z'}Y$ is $\iota\circ\varphi_X\circ \alpha=\iota\circ\varphi_Y\circ \beta$; since $\iota$ is a monomorphism, these two conditions are equivalent. Therefore, both fiber products satisfy the same universal property, and by uniqueness, $X\times_{Z'}Y$ plays the role of $X\times_ZY$.

On the other hand, without assumptions on $\iota$, this does not hold. For example, if we take the structure morphism $\iota:Z \rightarrow \Spec k$ of a $k$-scheme and equip $X=Y=Z=\mathbb{A}^1_k$ with identity morphisms, then $X\times_ZY=\mathbb{A}^1_k$, but $X\times_{\Spec k}Y=\mathbb{A}^2_k$.
:::

Now, using the lemma above, for arbitrary $X,Y,Z$ and scheme morphisms $\varphi_X:X \rightarrow Z$, $\varphi_Y: Y \rightarrow Z$, if we cover $Z$ by an affine open cover $\{Z_i\}$, then for $\varphi_X\vert^{Z_i}:\varphi_X^{-1}(Z_i) \rightarrow Z_i$ and $\varphi_Y\vert^{Z_i}:\varphi_Y^{-1}(Z_i) \rightarrow Z_i$, writing $X_i=\varphi_X^{-1}(Z_i)$ and $Y_i=\varphi_Y^{-1}(Z_i)$, we know that the fiber product $X_i\times_{Z_i}Y_i$ exists. Now, since the intersection $Z_{ij}=Z_i\cap Z_j$ is an open subset of $Z_i$, by [Lemma 7](#lem7){: data-lid="m4dv9" } the fiber products of $\varphi_X\vert^{Z_{ij}}$ and $\varphi_Y\vert^{Z_{ij}}$ also exist, and these are open subschemes of $X_i\times_{Z_i}Y_i$ and $X_j\times_{Z_j}Y_j$. Therefore, just as in the proof of [Lemma 5](#lem5){: data-lid="ky7tv" }, if we show that these data satisfy the conditions of [§Schemes, ⁋Lemma 9](/en/math/scheme_theory/schemes#lem9){: data-lid="avziv" }, we obtain the following theorem.

::: Theorem 8
For any schemes $X,Y,Z$ and scheme morphisms $X \rightarrow Z$, $Y \rightarrow Z$, the fiber product $X\times_ZY$ exists.
:::
::: Proof
What is required for the gluing is that inside the two pieces $X_i\times_{Z_i}Y_i$ and $X_j\times_{Z_j}Y_j$, the open subsets corresponding to the fiber product over $Z_{ij}$ are canonically identified, and that these identifications satisfy the cocycle condition on triple intersections. However, since both open subsets satisfy the universal property of the fiber product of $\varphi_X\vert^{Z_{ij}}$ and $\varphi_Y\vert^{Z_{ij}}$, the identification between them is uniquely determined, and the three identifications obtained on the triple intersection are also the unique morphisms given by the universal property of the fiber product over $Z_{ijk}=Z_i\cap Z_j\cap Z_k$, so the composition of any two of them equals the third and the cocycle condition holds. Therefore, by [§Schemes, ⁋Lemma 9](/en/math/scheme_theory/schemes#lem9){: data-lid="eabnf" }, they glue together into a single scheme.

That the scheme obtained in this way satisfies the universal property follows as in the proof of [Lemma 5](#lem5){: data-lid="vmve1" }. That is, if morphisms $\alpha: W \rightarrow X$, $\beta: W \rightarrow Y$ agree over $Z$, we set $W_i=(\varphi_X\circ \alpha)^{-1}(Z_i)$, obtain a unique morphism from each $W_i$ to $X_i\times_{Z_i}Y_i$, verify agreement on overlaps via the uniqueness of the universal property as above, and glue them together.
:::

## Interpretation of the Fiber Product

Just as there are multiple ways to interpret scheme morphisms, there are also multiple ways to understand fiber products. 

Earlier, we agreed to think of a scheme morphism $X \rightarrow S$ as a family parametrized by $S$ ([§Morphisms of Schemes, ⁋Example 10](/en/math/scheme_theory/morphism_of_schemes#ex10){: data-lid="i27fa" }), and from this perspective, $S$ can be considered the base of the family $X$. Now suppose we are given an arbitrary $S$-family $X \rightarrow S$ and a scheme morphism $S' \rightarrow S$; then via the fiber product we obtain a new $S'$-family $X\times_SS' \rightarrow S'$. From this point of view, we often call the fiber product a *base change* as well.

::: Example 9
If we restrict our attention to affine schemes, the fact that $\Spec B$ is a $C$-scheme means that a scheme morphism $\Spec B \rightarrow \Spec C$ is given, which in turn is equivalent to being given a ring homomorphism $C \rightarrow B$, which is again equivalent to saying that $B$ is a $C$-algebra. 

Now suppose in addition that a scheme morphism $\Spec A \rightarrow \Spec C$ is given, and let us examine what the base change above yields. By [Lemma 2](#lem2){: data-lid="uqgno" }, we see that what is obtained in this way is

$$\Spec A\times_{\Spec C}\Spec B=\Spec(A\otimes_CB) \rightarrow \Spec A$$

that is, the ring homomorphism $A \rightarrow A\otimes_CB$. In other words, base change (in the case of affine schemes) is nothing other than [\[Algebraic Structures\] §Change of Scalars, ⁋Definition 3](/en/math/algebraic_structures/change_of_base_ring#def3){: data-lid="30e79" }. 
:::

In particular, for the $B$-algebra $B[\x_1,\ldots,\x_n]$ and any ring homomorphism $B \rightarrow A$, from the fact that the identity

$$A\otimes_BB[\x_1,\ldots,\x_n]\cong A[\x_1,\ldots, \x_n]$$

holds, we see that the following diagram

{% diagram Math/Scheme_Theory/Fiber_Products-7.svg width="20.67em" alt="adding_extra_variables" %}

is a fiber diagram. 

While this perspective is important, the geometric intuition here is not immediately apparent right now. To this end, let us consider in particular the case where $S' \rightarrow S$ is an embedding. 

First, for an arbitrarily given $S$-family $X \rightarrow S$ and an open embedding $S' \rightarrow S$, [Lemma 3](#lem3){: data-lid="dzn7l" } shows that the $S'$-family $X\times_SS' \rightarrow S'$ is obtained simply by restricting the base of $X \rightarrow S$ to $S'$. If we further assume that $X \rightarrow S$ is also an open embedding, we see that $X\times_SS'$ is the intersection (in $S$) of $X$ and $S'$. 

The above argument also holds in the case of closed embeddings. For this, we need to show the following lemma corresponding to [Lemma 3](#lem3){: data-lid="ia3dt" }.

::: Lemma 10
For a ring homomorphism $\phi: B \rightarrow A$ and any ideal of $B$, $\mathfrak{b}$, an isomorphism 

$$A/\phi(\mathfrak{b})A\cong A \otimes_B(B/\mathfrak{b})$$

exists. 
:::
::: Proof
Applying $\otimes_BA$ to the following exact sequence obtained from the ideal $\mathfrak{b}$

$$\mathfrak{b} \rightarrow B \rightarrow B/\mathfrak{b} \rightarrow 0$$

we obtain the following exact sequence

$$A\otimes_B \mathfrak{b} \rightarrow A\otimes_BB \rightarrow A\otimes_B (B/\mathfrak{b}) \rightarrow 0$$

and since the image of $A\otimes_B \mathfrak{b}$ in $A\otimes_BB\cong A$ is $\phi(\mathfrak{b})A$, we obtain the desired result.
:::

Now, since any closed embedding locally always comes from $B \rightarrow B/\mathfrak{b}$, the above discussion can be applied to closed embeddings in the same way. In particular, the intersection of two closed embeddings is well-defined.

::: Example 11
Consider two closed subschemes of $Z=\Spec\mathbb{K}[\x,\y]$,

$$X=\Spec \mathbb{K}[\x,\y]/(\y)=\Spec \mathbb{K}[\x],\qquad Y=\Spec \mathbb{K}[\x,\y]/(\x)=\Spec \mathbb{K}[\y]$$

Then $X$ and $Y$ correspond, in $Z=\mathbb{A}^2_\mathbb{K}$, to the $\x$-axis and the $\y$-axis, respectively, and their closed embeddings are given by the projections

$$\mathbb{K}[\x,\y] \rightarrow \mathbb{K}[\x],\qquad \mathbb{K}[\x,\y] \rightarrow \mathbb{K}[\y]$$

Now, by [Lemma 2](#lem2){: data-lid="ihx1v" }, we can see that $X\times_ZY$ is given by

$$\Spec\left(\frac{\mathbb{K}[\x,\y]}{(\y)}\otimes_{\mathbb{K}[\x,\y]} \frac{\mathbb{K}[\x,\y]}{(\x)}\right)\cong \Spec \mathbb{K}[\x,\y]/(\x,\y)\cong\Spec \mathbb{K}$$

which corresponds precisely to the origin, the intersection of the $\x$-axis and the $\y$-axis.

This time, let us replace $Y$ in the calculation above with the following closed subscheme:

$$Y=\Spec \mathbb{K}[\x,\y]/(\y-\x^2)$$

The intersection of $\y=\x^2$ and the $\x$-axis is likewise the origin, but since there is a multiple root this time, the scheme structure should be given differently from the above. Indeed, repeating the calculation shows that $X\times_ZY$ is given by

$$\Spec\left(\frac{\mathbb{K}[\x,\y]}{(\y)}\otimes_{\mathbb{K}[\x,\y]}\frac{\mathbb{K}[\x,\y]}{(\y-\x^2)}\right)\cong\Spec \mathbb{K}[\x,\y]/(\y,\y-\x^2)\cong\Spec \mathbb{K}[\x]/(\x^2)$$

:::

From this perspective, for a scheme morphism $\varphi:X \rightarrow Y$ and $y_0\in Y$, we can also see how to define the fiber $\varphi^{-1}(y_0)$. After constructing a morphism from a scheme containing only $y_0$ to $Y$, we take the fiber product of this morphism and $\varphi$. Here, we must be careful that we cannot take the embedding by viewing the one-point set $\{y_0\}$ as a subspace of $Y$. This is because if $y_0$ is not a closed point, $\{y_0\}$ is generally not even a locally closed subset of $Y$. For example, this is true of the generic point of $\mathbb{A}^2$.

Now, to construct $\Spec\kappa(y) \rightarrow Y$, consider, at $y$, the residue field $\kappa(y)$. Then $\Spec\kappa(y)$ is always a one-point set. Moreover, for $y$ in $Y$, consider an affine open subset $V=\Spec B$ containing it, and suppose that $y$ corresponds to the prime ideal $\mathfrak{q}_y$. Then the canonical morphism

$$B \rightarrow B_{\mathfrak{q}_y} \rightarrow B_{\mathfrak{q}_y}/\mathfrak{q}_y B_{\mathfrak{q}_y} =\kappa(\mathfrak{q}_y)=\kappa(y)$$

defines $\Spec\kappa(y)\rightarrow \Spec B$, and in $\Spec \kappa(y)$, the (unique) point $(0)$ is mapped to $\mathfrak{q}_y$ via this morphism. Therefore, we make the following definition.

::: Definition 12
For a scheme morphism $\varphi: X \rightarrow Y$, at a point in $Y$, $y\in Y$, we define the *fiber* by

$$\varphi^{-1}(y)=X\times_Y\Spec \kappa(y)$$

If $Y$ is irreducible, the fiber at the generic point of $Y$ is called the *generic fiber*.
:::

This definition uses the same notation as the preimage of a continuous function, and in fact the two objects coincide as topological spaces.

::: Lemma 13
For a scheme morphism $\varphi: X \rightarrow Y$ and $y\in Y$, the projection $X\times_Y\Spec\kappa(y) \rightarrow X$ is a homeomorphism onto the preimage $\{x\in X\mid \varphi(x)=y\}$ as a set.
:::
::: Proof
Since forming the fiber product in the same manner as in the proof of [Lemma 4](#lem4){: data-lid="f3kga" } is compatible with restricting $X$ and $Y$ to open subsets, by choosing an affine open subset with $y\in V=\Spec B$, say $V$, and covering $\varphi^{-1}(V)$ by affine open subsets $\Spec A$, it suffices to show only the case where $X=\Spec A$ and $Y=\Spec B$. Here, let the prime ideal corresponding to $y$ be $\mathfrak{q}$, and let $\phi: B \rightarrow A$ be the ring homomorphism corresponding to $\varphi$.

By [Lemma 2](#lem2){: data-lid="rmh2e" }, $X\times_Y\Spec \kappa(\mathfrak{q})=\Spec (A\otimes_B\kappa(\mathfrak{q}))$. Meanwhile, since $\kappa(\mathfrak{q})=B_\mathfrak{q}/\mathfrak{q}B_\mathfrak{q}$, if we set $S=\phi(B\setminus \mathfrak{q})$, then

$$A\otimes_B\kappa(\mathfrak{q})\cong (S^{-1}A)/\mathfrak{q}(S^{-1}A)$$

Then, applying [§The Spectrum, ⁋Proposition 9](/en/math/scheme_theory/spectrums#prop9){: data-lid="vryc4" } twice, $\Spec (A\otimes_B\kappa(\mathfrak{q})) \rightarrow \Spec A$ is a homeomorphism onto its image, and this image is the collection of prime ideals not meeting $S$ and containing $\mathfrak{q}(S^{-1}A)$, that is, those satisfying both $\phi^{-1}(\mathfrak{p})\subseteq \mathfrak{q}$ and $\mathfrak{q}\subseteq \phi^{-1}(\mathfrak{p})$ among $\mathfrak{p}\in \Spec A$. This is precisely the collection of points such that $(\Spec\phi)(\mathfrak{p})=\mathfrak{q}$.
:::

::: Example 14
For $\operatorname{char}\mathbb{K}\neq 2$ and an algebraically closed field $\mathbb{K}$, define a ring homomorphism $\mathbb{K}[\x] \rightarrow \mathbb{K}[\y]$ by the formula $\x \mapsto \y^2$, and consider the scheme morphism $\varphi: \Spec \mathbb{K}[\y] \rightarrow \Spec \mathbb{K}[\x]$ obtained from it. Then the residue field of $\Spec\mathbb{K}[\x]$ at any point $(\x-a)$ is

$$\Frac(\mathbb{K}[\x]/(\x-a))=\mathbb{K}[\x]/(\x-a).$$

Now for any $a\in \mathbb{K}$,

$$\varphi^{-1}((\x-a))=\Spec \mathbb{K}[\y]\times_{\Spec \mathbb{K}[\x]}\Spec \mathbb{K}[\x]/(\x-a)\cong \Spec(\mathbb{K}[\y]\otimes_{\mathbb{K}[\x]}\mathbb{K}[\x]/(\x-a))=\Spec \mathbb{K}[\y]/(\y^2-a),$$

and thus if $a=0$, then $\varphi^{-1}((\x))\cong\Spec \mathbb{K}[\y]/(\y^2)$, and if $a\neq 0$, from the assumptions that $\mathbb{K}$ is algebraically closed and $\operatorname{char}\mathbb{K}\neq 2$, we have

$$\Spec \mathbb{K}[\y]/(\y^2-a)\cong \Spec \mathbb{K}[\y]/(\y-\sqrt{a})\coprod \Spec \mathbb{K}[\y]/(\y+\sqrt{a}).$$

On the other hand, for the generic point of $\mathbb{K}[\x]$, namely $(0)$, since $\kappa((0))=\mathbb{K}(\x)$, we have

$$\varphi^{-1}((0))=\Spec \mathbb{K}[\y]\times_{\Spec \mathbb{K}[\x]}\Spec \mathbb{K}(\x)\cong \Spec\mathbb{K}(\y).$$
:::

The example above is one we have already examined in [§Properties of Scheme Morphisms, ⁋Example 16](/en/math/scheme_theory/properties_of_scheme_morphisms#ex16){: data-lid="7b57a" }. In that example, we claimed that a finite morphism is always quasi-finite, and we can now prove this.

::: Proposition 15
A finite morphism $\varphi: X \rightarrow Y$ is a quasi-finite morphism. 
:::
::: Proof
First, by [§Properties of Scheme Morphisms, ⁋Proposition 15](/en/math/scheme_theory/properties_of_scheme_morphisms#prop15){: data-lid="m36sx" }, a finite morphism is integral and locally of finite type, and since an integral morphism is affine, it is quasi-compact, so $\varphi$ is a morphism of finite type. Thus, it suffices to show that the fibers are finite sets. By [Lemma 13](#lem13){: data-lid="sc18m" }, the points of the set $\varphi^{-1}(y)$ correspond bijectively to the points of the scheme $X\times_Y\Spec\kappa(y)$, so it is enough to count the number of points in the latter. Then it suffices to show the claim for the affine case. That is, it is sufficient to show that for any finite ring homomorphism $\phi: B \rightarrow A$ and any prime ideal of $B$, say $\mathfrak{q}$, the algebra $A\otimes_B\kappa(\mathfrak{q})$ has only finitely many prime ideals. Since $\phi$ is finite, $A\otimes_B\kappa(\mathfrak{q})$ is a finite $\kappa(\mathfrak{q})$-algebra and hence Artinian. By [\[Commutative Algebra\] §The Jordan-Hölder Theorem, ⁋Corollary 6](/en/math/commutative_algebra/Jordan-Holder_theorem#cor6){: data-lid="vqwf6" }, $0$ is a product of finitely many maximal ideals, so any prime ideal must be equal to one of them, which yields the desired result.
:::

From the examples and propositions above, we can make an important observation: properties satisfied by $X \rightarrow S$ often carry over to the base change along any $S' \rightarrow S$, namely $X\times_SS' \rightarrow S'$. Of course, this is not true for all properties. For instance, being dominant is not preserved: $\Spec \mathbb{K}(\t) \rightarrow \Spec \mathbb{K}[\t]$ is a dominant morphism to the generic point, but base changing along $\t=0$ yields a morphism from the empty set to a single point. However, most properties we are interested in are closed under base change.

::: Proposition 16
If a morphism of schemes $\varphi:X \rightarrow Z$ is quasi-compact (resp. quasi-separated, affine, finite, integral, locally of finite type, of finite type, locally of finite presentation, of finite presentation, quasi-finite, surjective), then for any morphism of schemes $Y \rightarrow Z$, the base change of $\varphi$, $X\times_ZY \rightarrow Y$, also has the respective property.
:::
::: Proof
Let us first make a reduction common to all properties. We choose an affine open covering of $Z$ by open sets $\Spec A$, and for each $\Spec A$, cover its preimage under $Y \rightarrow Z$ by affine open subsets $\Spec C$; the $\Spec C$ obtained in this way form an affine open covering of $Y$. Now let $\rho_Y: X\times_ZY \rightarrow Y$ be the projection. From the fact used in the proofs of [Lemma 3](#lem3){: data-lid="hc8vx" } and [Lemma 4](#lem4){: data-lid="1zq0j" } that "if two small squares are fiber diagrams, then the outer large rectangle is also a fiber diagram," we obtain

$$\rho_Y^{-1}(\Spec C)\cong X\times_Z\Spec C\cong \varphi^{-1}(\Spec A)\times_{\Spec A}\Spec C$$

Therefore, writing $X_A=\varphi^{-1}(\Spec A)$ and $W=X_A\times_{\Spec A}\Spec C$, studying the base change $\rho_Y$ over $\Spec C$ is equivalent to studying the base change of $X_A \rightarrow \Spec A$ along $\Spec C \rightarrow \Spec A$, namely $W \rightarrow \Spec C$. Moreover, for the same reason, for any affine open subset of $X_A$, say $\Spec B$, its preimage under the projection $\rho: W \rightarrow X_A$ satisfies, by [Lemma 2](#lem2){: data-lid="e1gzt" },

$$\rho^{-1}(\Spec B)\cong \Spec B\times_{\Spec A}\Spec C\cong \Spec (B\otimes_AC)$$

and thus whenever an affine open covering of $X_A$, $\{\Spec B_i\}$, is given, $\{\Spec (B_i\otimes_AC)\}$ becomes an affine open covering of $W$. That is, every problem reduces to a question about the ring homomorphism $C \rightarrow B\otimes_AC$. We now examine each of the properties.

First, suppose that $\varphi$ is affine. Then $X_A$ is an affine scheme $\Spec B$, and thus $\rho_Y^{-1}(\Spec C)=W\cong\Spec (B\otimes_AC)$ is affine; by the affine open covering of $Y$, $\{\Spec C\}$, and [§Properties of Scheme Morphisms, ⁋Proposition 9](/en/math/scheme_theory/properties_of_scheme_morphisms#prop9){: data-lid="zbsru" }, $\rho_Y$ is affine.

Suppose that $\varphi$ is quasi-compact. Then $X_A$ is quasi-compact, so it is covered by finitely many affine open subsets $\Spec B_1,\ldots, \Spec B_n$, and thus $W$ is covered by finitely many affine open subsets $\Spec (B_i\otimes_AC)$, making it quasi-compact. Now by the first result of [§Properties of Scheme Morphisms, ⁋Proposition 7](/en/math/scheme_theory/properties_of_scheme_morphisms#prop7){: data-lid="5om77" }, $\rho_Y$ is quasi-compact.

Suppose that $\varphi$ is quasi-separated. Then $X_A$ is a quasi-separated scheme. If we choose an affine open covering of $X_A$, $\{\Spec B_i\}$, then $\{W_i=\Spec (B_i\otimes_AC)\}$ is an affine open covering of $W$, and since $\Spec B_i\cap \Spec B_j$ is quasi-compact, we can write it as the union of finitely many principal open sets of $\Spec B_i$, $D(h_1),\ldots, D(h_s)$ ([§The Spectrum, ⁋Lemma 11](/en/math/scheme_theory/spectrums#lem11){: data-lid="ih6ij" }), so

$$W_i\cap W_j=\rho^{-1}(\Spec B_i\cap \Spec B_j)=\bigcup_{t=1}^s\Spec \bigl((B_i)_{h_t}\otimes_AC\bigr)$$

is a union of finitely many affine open subsets, hence quasi-compact. Now let us show in general that if a scheme $W$ has the property that the $W_i\cap W_j$ are all quasi-compact for an affine open covering $\{W_i\}$, then $W$ is quasi-separated. Since any quasi-compact open subset of $W$ is a union of finitely many affine open subsets, it suffices to show that for any two affine open subsets of $W$, $P,Q$, the intersection $P\cap Q$ is quasi-compact. By [§The Topology of Schemes, ⁋Lemma 11](/en/math/scheme_theory/topology_of_schemes#lem11){: data-lid="7yezt" } and the quasi-compactness of $P,Q$, each of $P$ and $Q$ is covered by finitely many open sets that are principal open sets in both itself and some $W_i$; thus, in the end it suffices to show that for a principal open set of $W_i$, $D(f)$, and a principal open set of $W_j$, $D(g)$, the intersection $D(f)\cap D(g)$ is quasi-compact. However, $D(f)\cap D(g)\subseteq W_i\cap W_j$, and since $W_i\cap W_j$ is quasi-compact, it can be written as the union of finitely many principal open sets of $W_i$, $D(h_1),\ldots, D(h_s)$, and therefore

$$D(f)\cap D(g)=\bigcup_{t=1}^s\bigl(D(fh_t)\cap D(g)\bigr)$$

holds. Here, each $D(fh_t)$ is an affine open subset contained in $W_i\cap W_j$; viewing this as an affine open subset of $W_j$, $D(fh_t)\cap D(g)$ is the principal open set defined by the restriction of $g$ on the affine scheme $D(fh_t)$ ([§The Spectrum, ⁋Proposition 8](/en/math/scheme_theory/spectrums#prop8){: data-lid="fj5jp" }), and is thus affine. That is, $D(f)\cap D(g)$ is a union of finitely many affine open subsets and hence is quasi-compact. From the above, $W$ is quasi-separated, and by the second result of [§Properties of Scheme Morphisms, ⁋Proposition 7](/en/math/scheme_theory/properties_of_scheme_morphisms#prop7){: data-lid="s6w4b" }, $\rho_Y$ is quasi-separated.

Suppose that $\varphi$ is integral (resp. finite). Then since $\varphi$ is affine, $X_A=\Spec B$ and $A \rightarrow B$ is integral (resp. finite). Therefore $\rho_Y^{-1}(\Spec C)=\Spec (B\otimes_AC)$, and by [\[Commutative Algebra\] §Integral Extensions, ⁋Proposition 14](/en/math/commutative_algebra/integral_extension#prop14){: data-lid="g66ia" }, $C \rightarrow B\otimes_AC$ is also integral (resp. finite). That these two properties are affine-local on the target was established right after [§Properties of Scheme Morphisms, ⁋Definition 11](/en/math/scheme_theory/properties_of_scheme_morphisms#def11){: data-lid="1e1y0" }, so checking them on the affine open covering of $Y$, $\{\Spec C\}$, is sufficient.

Suppose that $\varphi$ is locally of finite type. If we choose an affine open covering of $X_A$, $\{\Spec B_i\}$, then each $A \rightarrow B_i$ is of finite type, and if elements generating $B_i$ as an $A$-algebra are $x_1,\ldots, x_n$, then $B_i\otimes_AC$ is generated as a $C$-algebra by $x_1\otimes 1,\ldots, x_n\otimes 1$, so $C \rightarrow B_i\otimes_AC$ is also of finite type. Now we must obtain the same conclusion for *all* affine open subsets of $W$, which follows by applying [§Properties of Scheme Morphisms, ⁋Lemma 13](/en/math/scheme_theory/properties_of_scheme_morphisms#lem13){: data-lid="rue4s" } to the affine open covering $\{\Spec (B_i\otimes_AC)\}$ we just constructed. That is, $\rho_Y$ is locally of finite type. Moreover, since a morphism of finite type is a morphism that is both quasi-compact and locally of finite type, combining this with the quasi-compact case above shows that being of finite type is also preserved under base change.

Suppose that $\varphi$ is locally of finite presentation. The condition of [§Properties of Scheme Morphisms, ⁋Definition 18](/en/math/scheme_theory/properties_of_scheme_morphisms#def18){: data-lid="qorha" } is a condition on *some* affine open covering of the preimage, so this case is rather simpler. By hypothesis, there exists an affine open covering of $X_A$, $\{\Spec B_i\}$, such that each $B_i$ is of the form

$$B_i\cong A[\x_1,\ldots, \x_n]/(f_1,\ldots, f_m)$$

and then, from the isomorphism $C\otimes_AA[\x_1,\ldots, \x_n]\cong C[\x_1,\ldots, \x_n]$ observed after [Example 9](#ex9){: data-lid="55k7v" } and [Lemma 10](#lem10){: data-lid="rc4jf" },

$$B_i\otimes_AC\cong C[\x_1,\ldots, \x_n]/(\bar{f}_1,\ldots, \bar{f}_m)$$

we have that (where $\bar{f}_k$ is obtained by sending the coefficients of $f_k$ into $C$) $C \rightarrow B_i\otimes_AC$ is also finitely presented. That is, the affine open covering of $W$, $\{\Spec (B_i\otimes_AC)\}$, witnesses the required condition over $\Spec C$. That this property is affine-local on the target is obtained by applying [§The Topology of Schemes, ⁋Lemma 12](/en/math/scheme_theory/topology_of_schemes#lem12){: data-lid="nfdk0" } to the property that $\varphi^{-1}(\Spec B)$ has, with each $B \rightarrow R_i$ being finitely presented, an affine open covering $\{\Spec R_i\}$. Indeed, the first condition of [§The Topology of Schemes, ⁋Definition 9](/en/math/scheme_theory/topology_of_schemes#def9){: data-lid="oo009" } is obtained from the fact that $\varphi^{-1}(D(f))$ is covered by the $\Spec (R_i)_f$ and $(R_i)_f\cong R_i\otimes_BB_f$ is a base change of a finitely presented homomorphism, while the second condition is obtained from the fact that $B \rightarrow B_f\cong B[\y]/(f\y-1)$ is finitely presented and that the composition of finitely presented homomorphisms is again finitely presented. Finally, a morphism of finite presentation is a morphism that is quasi-compact, quasi-separated, and locally of finite presentation, so combining this with the preceding results shows that this property is also preserved under base change.

Now, for the remaining two properties, let us compute the fibers. For $y\in Y$ and its image $z\in Z$, since $\mathcal{O}_{Z,z} \rightarrow \mathcal{O}_{Y,y}$ is a local homomorphism, $\Spec \kappa(y) \rightarrow Y \rightarrow Z$ factors through $\Spec\kappa(z) \rightarrow Z$, and hence by composing fiber diagrams as above, we obtain by [Definition 12](#def12){: data-lid="xzuvg" }

$$\rho_Y^{-1}(y)=(X\times_ZY)\times_Y\Spec \kappa(y)\cong X\times_Z\Spec \kappa(y)\cong \varphi^{-1}(z)\times_{\Spec \kappa(z)}\Spec \kappa(y)$$

Moreover, by [Lemma 3](#lem3){: data-lid="7gm6b" }, for an affine open subset of $\varphi^{-1}(z)$, $\Spec R$, the set $\Spec (R\otimes_{\kappa(z)}\kappa(y))$ is an open subset of $\rho_Y^{-1}(y)$, and these cover $\rho_Y^{-1}(y)$.

Suppose that $\varphi$ is surjective. First, we check that $\varphi^{-1}(z)$ is not empty. We pick a point satisfying $\varphi(x)=z$, $x\in X$, and choose an affine open subset containing $x$ that is mapped by $\varphi$ into $\Spec A$, say $\Spec B\subseteq X$, along with the corresponding ring homomorphism $\phi:A \rightarrow B$. Letting the prime ideals corresponding to $x$ and $z$ be $\mathfrak{q}\subseteq B$ and $\mathfrak{p}\subseteq A$, respectively, we have $\phi^{-1}(\mathfrak{q})=\mathfrak{p}$ and from [Lemma 10](#lem10){: data-lid="xkfkk" } and the properties of localization,

$$B\otimes_A\kappa(\mathfrak{p})\cong (B/\mathfrak{p}B)_\mathfrak{p}$$

and so $\mathfrak{q}$ defines a prime ideal of this ring. That is, $\varphi^{-1}(z)\neq\emptyset$. Now if we choose a nonempty affine open subset of $\varphi^{-1}(z)$, $\Spec R$, then $R$ is a non-$0$ $\kappa(z)$-algebra, and since $\kappa(y)$ is a non-$0$ $\kappa(z)$-vector space, we have $R\otimes_{\kappa(z)}\kappa(y)\neq 0$. Since a non-$0$ ring always has a prime ideal, $\Spec (R\otimes_{\kappa(z)}\kappa(y))\neq\emptyset$, and therefore $\rho_Y^{-1}(y)\neq\emptyset$. Since $y$ was arbitrary, $\rho_Y$ is surjective.

Finally, suppose that $\varphi$ is quasi-finite. Since $\varphi$ is of finite type, as seen above $\rho_Y$ is also of finite type, and thus it suffices to show that the fibers of $\rho_Y$ are all finite sets. Since $\varphi$ is quasi-compact, applying the preservation of quasi-compactness under base change to $\Spec \kappa(z) \rightarrow Z$ shows that $\varphi^{-1}(z)$ is quasi-compact, so it can be covered by finitely many affine open subsets $\Spec R_1,\ldots, \Spec R_n$. Likewise, since $\varphi$ is locally of finite type, each $R_l$ is a finite type $\kappa(z)$-algebra, and by hypothesis each $\Spec R_l$ is a finite set.

Now let us show that a finite type $\mathbb{K}$-algebra $R$ having only finitely many prime ideals is always a finite-dimensional $\mathbb{K}$-vector space. First, we show that every prime ideal of $R$, $\mathfrak{p}$, is maximal. If there exists a prime ideal strictly containing $\mathfrak{p}$, then $d=\dim R/\mathfrak{p}\geq 1$, and by [\[Commutative Algebra\] §Noether Normalization, ⁋Theorem 1](/en/math/commutative_algebra/noether_normalization#thm1){: data-lid="mvmye" }, $R/\mathfrak{p}$ contains the polynomial ring $\mathbb{K}[\x_1,\ldots, \x_d]$ as a subring and is a finitely generated module over it, in particular an integral extension. However, since $d\geq 1$, $\mathbb{K}[\x_1,\ldots, \x_d]$ has infinitely many prime ideals generated by distinct irreducible polynomials of $\mathbb{K}[\x_1]$, and by [\[Commutative Algebra\] §Integral Extensions and Ideals, ⁋Proposition 1](/en/math/commutative_algebra/lying_over_and_going_up#prop1){: data-lid="msjgq" }, a prime ideal of $R/\mathfrak{p}$ lies over each of these, which contradicts the hypothesis that $R$ has only finitely many prime ideals. Therefore, all prime ideals of $R$ are maximal, and since $R$ is Noetherian by [\[Commutative Algebra\] §Basic Notions, ⁋Theorem 12](/en/math/commutative_algebra/basic_notions#thm12){: data-lid="9qiuu" }, by [\[Commutative Algebra\] §The Jordan-Hölder Theorem, ⁋Theorem 4](/en/math/commutative_algebra/Jordan-Holder_theorem#thm4){: data-lid="tzmqi" } $R$ has finite length as an $R$-module. Here, the composition factors are all of the form $R/\mathfrak{m}$, and since a field is a Jacobson ring, by [\[Commutative Algebra\] §The Nullstellensatz, ⁋Theorem 4](/en/math/commutative_algebra/nullstellensatz#thm4){: data-lid="v3wbe" }, $R/\mathfrak{m}$ is a finite extension of $\mathbb{K}$. Therefore $R$ is a finite-dimensional $\mathbb{K}$-vector space.

Then each $R_l$ is a finite-dimensional $\kappa(z)$-vector space, so $R_l\otimes_{\kappa(z)}\kappa(y)$ is also a finite-dimensional $\kappa(y)$-vector space, and thus becomes an Artinian ring, having only finitely many prime ideals for the same reason as above ([\[Commutative Algebra\] §The Jordan-Hölder Theorem, ⁋Corollary 6](/en/math/commutative_algebra/Jordan-Holder_theorem#cor6){: data-lid="tuefi" }). Now $\rho_Y^{-1}(y)$ is covered by finitely many $\Spec (R_l\otimes_{\kappa(z)}\kappa(y))$ and is therefore a finite set, and from this we see that $\rho_Y$ is quasi-finite.
:::

---

**References**

**[Har]** R. Hartshorne, *Algebraic geometry*. Graduate texts in mathematics. Springer, 1977.  
**[Vak]** R. Vakil, *The rising sea: Foundation of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/).
