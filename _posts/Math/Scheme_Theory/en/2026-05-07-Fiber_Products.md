---
title: "Fiber Products"
description: "This post covers the definition and universal property of fiber products of schemes, and proves the existence of fiber products for affine schemes."
excerpt: "Definition and existence of fiber products in the category of S-schemes"

categories: [Math / Scheme Theory]
permalink: /en/math/scheme_theory/fiber_products
sidebar: 
    nav: "scheme_theory-en"

date: 2025-03-08
weight: 12
translated_at: 2026-07-21T22:15:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-07-21T22:15:02+00:00
---
One of the things we promised when introducing schemes was the fiber product, which is the product in $\Sch_{/S}$; to discuss this we had to define $S$-schemes (and scheme morphisms). Now that the preparations are complete, we define the fiber product.

## Definition and Existence of Fiber Products

In [§Morphisms of Schemes, ⁋Definition 3](/en/math/scheme_theory/morphism_of_schemes#def3) we agreed to call a scheme morphism $X \rightarrow S$ an *$S$-scheme*. In this post we define the product in the category $\Sch_{/S}$.

::: Definition 1
The fiber product of two scheme morphisms $\varphi_X:X \rightarrow S$, $\varphi_Y:Y \rightarrow S$ is denoted $X\times_SY$. ([\[Category Theory\] §Limits, ⁋Example 8](/en/math/category_theory/limits#ex8))
:::

Thus $X\times_SY$ satisfies the following property.

> The diagram
> 
> ![fiber_diagram](/assets/images/Math/Scheme_Theory/Fiber_Products-1.svg){:style="width:9.32em" class="invert" .align-center}
> 
> commutes. Moreover, whenever any $\psi_X:Z \rightarrow X$, $\psi_Y:Z \rightarrow Y$ satisfying $\varphi_Y\circ\psi_Y=\varphi_X\circ\psi_X$ are given, there exists a unique $\psi:Z \rightarrow X\times_SY$ such that $\psi_X=\rho_X\circ\psi$ and $\psi_Y=\rho_Y\circ\psi$.
> 
> ![universal_product](/assets/images/Math/Scheme_Theory/Fiber_Products-2.svg){:style="width:13.72em" class="invert" .align-center}

Therefore, there is a canonical morphism from $X\times_SY$ to $S$, and from this we may view $X\times_SY$ as an $S$-scheme. Moreover, from this viewpoint it is obvious from the definition that $X\times_SY$ is also the product in $\Sch_{/S}$.

After [§Morphisms of Schemes, ⁋Example 4](/en/math/scheme_theory/morphism_of_schemes#ex4) we saw that any scheme $X$ can always be regarded as a $\mathbb{Z}$-scheme in a unique way. Thus, assuming that a fiber product $X\times_SY$ satisfying [Definition 1](#def1) always exists, we know that for any two schemes $X, Y$ the fiber product $X\times_{\Spec \mathbb{Z}}Y$ gives the product of $X$ and $Y$.

Since [Definition 1](#def1) does not guarantee the existence of the fiber product $X\times_SY$, for this to be a genuine definition we must separately prove the existence of $X\times_SY$. ([Theorem 8](#thm8)) However, the existence of fiber products in $\AffSch$ is almost obvious, and this will be the starting point of our proof.

::: Lemma 2
Given morphisms of affine schemes $\Spec A \rightarrow \Spec C$, $\Spec B \rightarrow\Spec C$, we have

$$\Spec A\times_{\Spec C}\Spec B\cong\Spec (A\otimes_C B).$$
:::
::: Proof
Via $\AffSch\cong\cRing^\op$ we convert $\Spec A \rightarrow \Spec C$, $\Spec B \rightarrow \Spec C$ into $C \rightarrow A$, $C \rightarrow B$, and compare the universal property of [\[Algebraic Structures\] §Products, Coproducts, and Tensor Products of Algebras, ⁋Theorem 8](/en/math/algebraic_structures/operations_of_algebras#thm8) with the universal property of the fiber product.
:::

Now, to prove the existence of fiber products for general schemes, it suffices to show that we can glue together the affine results examined in [Lemma 2](#lem2).

First, when an open subscheme $U$ of $Z$ is given, writing it in the form $\iota:U \rightarrow Z$ using the inclusion morphism, the following lemma is almost a tautology.

::: Lemma 3
Given a scheme morphism $\varphi: Y \rightarrow Z$ and an open subscheme $\iota: U \rightarrow Z$ of $Z$, the diagram

![open_subscheme](/assets/images/Math/Scheme_Theory/Fiber_Products-3.svg){:style="width:8.22em" class="invert" .align-center}

is a fiber diagram.
:::
::: Proof
$\varphi^{-1}(U)$ satisfies the universal property of the fiber product.
:::

Now, applying this slightly, we can prove the following lemma.

::: Lemma 4
Given affine schemes $X, Y, Z$, and an open subscheme $Y'\hookrightarrow Y$ of $Y$, the fiber product $X\times_ZY'$ of $X\rightarrow Z$ and $Y'\hookrightarrow Y \rightarrow Z$ exists.
:::
::: Proof
First, from [Lemma 2](#lem2) we know that the following fiber diagram

![open_fiber_product-1](/assets/images/Math/Scheme_Theory/Fiber_Products-4.svg){:style="width:9.32em" class="invert" .align-center}

exists. Now consider the data

![open_fiber_product-2](/assets/images/Math/Scheme_Theory/Fiber_Products-5.svg){:style="width:8.55em" class="invert" .align-center}

From [Lemma 3](#lem3) we can verify that the open subscheme $\rho_Y^{-1}(Y')$ of $X\times_ZY$ is the fiber product. Now, in general, if the two small squares in the diagram

![magic_square](/assets/images/Math/Scheme_Theory/Fiber_Products-6.svg){:style="width:8.55em" class="invert" .align-center}

are fiber diagrams, then the outer large square is also a fiber diagram, so we obtain the desired result.
:::

Now using this, we can show that the fiber product of an affine scheme and an arbitrary scheme exists.

::: Lemma 5
For affine schemes $X, Z$ and any scheme $Y$, the fiber product $X\times_ZY$ of $X\rightarrow Z$ and $Y \rightarrow Z$ exists.
:::
::: Proof
To see this, cover $Y$ by affine open subsets $Y_i$. Then we know from [Lemma 2](#lem2) that the $X\times_ZY_i$ exist. Also, since $Y_{ij}=Y_i\cap Y_j$ is an open subscheme of the affine scheme $Y_i$, the fiber product $X\times_Z Y_{ij}$ also exists by [Lemma 4](#lem4).

On the other hand, looking at the proof of [Lemma 4](#lem4), we see that $X\times_ZY_{ij}$ is an open subscheme of both $X\times_ZY_i$ and $X\times_ZY_j$. We can easily check that these data satisfy the conditions of [§Schemes, ⁋Lemma 9](/en/math/scheme_theory/schemes#lem9), so we can glue them to construct the scheme $X\times_ZY$. That this satisfies the universal property of the fiber product can be checked by restricting the codomain of a scheme morphism $W \rightarrow Y$ to the $Y_i$, using the universal property of each $X\times_ZY_i$, and then gluing the scheme morphisms together as in [§Morphisms of Schemes, ⁋Proposition 1](/en/math/scheme_theory/morphism_of_schemes#prop1).
:::

In this lemma, the assumption that $X$ is affine was used only to show that $X\times_ZY_i$ exists. Therefore, if any two schemes $X,Y$ and an affine scheme $Z$ are given, together with scheme morphisms $X \rightarrow Z$ and $Y \rightarrow Z$, we can choose an affine open cover $\{Y_i\}$ of $Y$, then know that $X\times_ZY_i$ exists by [Lemma 5](#lem5), and thus glue them to construct $X\times_ZY$. That is, the following holds.

::: Lemma 6
For an affine scheme $Z$, arbitrary schemes $X,Y$, and scheme morphisms $X \rightarrow Z$, $Y \rightarrow Z$, the fiber product $X\times_ZY$ exists.
:::

Now finally we must extend $Z$ to an arbitrary scheme. First, the following holds.

::: Lemma 7
Given arbitrary schemes $X,Y,Z$, scheme morphisms $\varphi_X:X \rightarrow Z$, $\varphi_Y:Y \rightarrow Z$, and a monomorphism $\iota: Z \rightarrow Z'$ to an affine scheme $Z'$. For instance, this is the case when $\iota$ is an open immersion or a closed embedding. Then the fiber product $X\times_{Z'}Y$ of $\iota\circ\varphi_X$ and $\iota\circ\varphi_Y$ satisfies the universal property of $X\times_ZY$, and therefore $X\times_ZY$ exists.
:::
::: Proof
Since $Z'$ is affine, $X\times_{Z'}Y$ exists. Now let $T$ be an arbitrary scheme and $a:T \rightarrow X$, $b:T \rightarrow Y$ morphisms. The condition required by the universal property of $X\times_ZY$ is $\varphi_X\circ a=\varphi_Y\circ b$, and that of $X\times_{Z'}Y$ is $\iota\circ\varphi_X\circ a=\iota\circ\varphi_Y\circ b$; since $\iota$ is a monomorphism these two conditions are equivalent. Thus the two fiber products satisfy the same universal property, and by uniqueness $X\times_{Z'}Y$ plays the role of $X\times_ZY$.

On the other hand, this does not hold without the assumption on $\iota$. For example, taking the structure morphism $\iota:Z \rightarrow \Spec k$ of a $k$-scheme and giving the identity morphism on $X=Y=Z=\mathbb{A}^1_k$, we have $X\times_ZY=\mathbb{A}^1_k$ but $X\times_{\Spec k}Y=\mathbb{A}^2_k$.
:::

Now, using the above lemma, for arbitrary $X,Y,Z$ and scheme morphisms $\varphi_X:X \rightarrow Z$, $\varphi_Y: Y \rightarrow Z$, if we cover $Z$ by an affine open cover $\{Z_i\}$, then we know that fiber products $X_i\times_{Z_i}Y_i$ exist for $\varphi_X\vert^{Z_i}:\varphi_X^{-1}(Z_i) \rightarrow Z_i$ and $\varphi_Y\vert^{Z_i}:\varphi_Y^{-1}(Z_i) \rightarrow Z_i$. Now the intersection $Z_{ij}=Z_i\cap Z_j$ is an open subset of $Z_i$, so by [Lemma 7](#lem7) the fiber products of $\varphi_X\vert^{Z_{ij}}$ and $\varphi_Y\vert^{Z_{ij}}$ also exist, and these are open subschemes of $X_i\times_{Z_i}Y_i$ and $X_j\times_{Z_j}Y_j$. Therefore, just as in the proof of [Lemma 5](#lem5), if we show that these data satisfy the condition of [§Schemes, ⁋Lemma 9](/en/math/scheme_theory/schemes#lem9), we obtain the following theorem.

::: Theorem 8
For arbitrary schemes $X,Y,Z$ and scheme morphisms $X \rightarrow Z$, $Y \rightarrow Z$, the fiber product $X\times_ZY$ exists.
:::

## Interpretations of the Fiber Product

Just as there are several ways to interpret a scheme morphism, there are several ways to understand the fiber product.

Earlier we agreed to think of a scheme morphism $X \rightarrow S$ as a family parametrized by $S$ ([§Morphisms of Schemes, ⁋Example 10](/en/math/scheme_theory/morphism_of_schemes#ex10)), and from this viewpoint $S$ can be thought of as the base of the family $X$. Now, given any $S$-family $X \rightarrow S$ and a scheme morphism $S' \rightarrow S$, through the fiber product we obtain a new $S'$-family $X\times_SS' \rightarrow S'$. From this viewpoint we often call the fiber product a *base change*.

::: Example 9
Narrowing our scope to affine schemes, saying that $\Spec B$ is a $C$-scheme means that a scheme morphism $\Spec B \rightarrow \Spec C$ is given, which in turn is the same as a ring homomorphism $C \rightarrow B$ being given, which is again the same as saying that $B$ is a $C$-algebra.

Now additionally given a scheme morphism $\Spec A \rightarrow \Spec C$, let us see what the above base change gives; by [Lemma 2](#lem2) we know that what is obtained in this way is

$$\Spec A\times_{\Spec C}\Spec B=\Spec(A\otimes_CB) \rightarrow \Spec A$$

that is, the ring homomorphism $A \rightarrow A\otimes_CB$. In other words, base change is (in the case of affine schemes) nothing but [\[Algebraic Structures\] §Change of Base Ring, ⁋Definition 3](/en/math/algebraic_structures/change_of_base_ring#def3).
:::

In particular, for the $B$-algebra $B[\x_1,\ldots,\x_n]$ and any ring homomorphism $B \rightarrow A$, from the identity

$$A\otimes_BB[\x_1,\ldots,\x_n]\cong A[\x_1,\ldots, \x_n]$$

we know that the following diagram

![adding_extra_variables](/assets/images/Math/Scheme_Theory/Fiber_Products-7.svg){:style="width:20.67em" class="invert" .align-center}

is a fiber diagram.

This viewpoint is important, but for now the geometric intuition here is not very visible. To see this, let us consider the case where $S' \rightarrow S$ is an embedding in particular.

First, for any given $S$-family $X \rightarrow S$ and open embedding $S' \rightarrow S$, [Lemma 3](#lem3) shows that the $S'$-family $X\times_SS' \rightarrow S'$ is simply obtained by restricting the base of $X \rightarrow S$ to $S'$. Moreover, if we additionally assume that $X \rightarrow S$ is also an open embedding, we know that $X\times_SS'$ is the intersection of $X$ and $S'$ (inside $S$).

The above argument also works in the case of a closed embedding. To see this, we need the following lemma corresponding to [Lemma 3](#lem3).

::: Lemma 10
For a ring homomorphism $\phi: B \rightarrow A$ and any ideal $\mathfrak{b}$ of $B$, there exists an isomorphism

$$A/\phi(\mathfrak{b})A\cong A \otimes_B(B/\mathfrak{b}).$$
:::
::: Proof
Applying $\otimes_BA$ to the exact sequence

$$\mathfrak{b} \rightarrow B \rightarrow B/\mathfrak{b} \rightarrow 0$$

obtained from the ideal $\mathfrak{b}$, we get the exact sequence

$$A\otimes_B \mathfrak{b} \rightarrow A\otimes_BB \rightarrow A\otimes_B (B/\mathfrak{b}) \rightarrow 0$$

and since the image of $A\otimes_B \mathfrak{b}$ in $A\otimes_BB\cong A$ is $\phi(\mathfrak{b})A$, we obtain the desired result.
:::

Now any closed embedding is locally always obtained from $B \rightarrow B/\mathfrak{b}$, so the above discussion applies equally to closed embeddings. In particular, the intersection of two closed embeddings is well-defined.

::: Example 11
Consider the two closed subschemes of $Z=\Spec\mathbb{K}[\x,\y]$

$$X=\Spec \mathbb{K}[\x,\y]/(\y)=\Spec \mathbb{K}[\x],\qquad Y=\Spec \mathbb{K}[\x,\y]/(\x)=\Spec \mathbb{K}[\y].$$

Then $X$ and $Y$ correspond to the $\x$-axis and $\y$-axis of $Z=\mathbb{A}^2_\mathbb{K}$ respectively, and their closed embeddings are given by the projections

$$\mathbb{K}[\x,\y] \rightarrow \mathbb{K}[\x],\qquad \mathbb{K}[\x,\y] \rightarrow \mathbb{K}[\y].$$

Now $X\times_ZY$ is, by [Lemma 2](#lem2), given by

$$\Spec\left(\frac{\mathbb{K}[\x,\y]}{(\x)}\otimes_{\mathbb{K}[\x,\y]} \frac{\mathbb{K}[\x,\y]}{(\y)}\right)\cong \Spec \mathbb{K}[\x,\y]/(\x,\y)\cong\Spec \mathbb{K}$$

which we can check corresponds exactly to the origin, the intersection point of the $\x$-axis and $\y$-axis.

Now let us change $Y$ in the above computation to the following closed subscheme

$$Y=\Spec \mathbb{K}[\x,\y]/(\y-\x^2).$$

The intersection of $\y=\x^2$ and the $\x$-axis is again the origin, but this time a multiple root exists so the scheme structure must be given differently. Indeed, repeating the computation, $X\times_ZY$ becomes

$$\Spec\left(\frac{\mathbb{K}[\x,\y]}{(\y)}\otimes_{\mathbb{K}[\x,\y]}\frac{\mathbb{K}[\x,\y]}{(\y-\x^2)}\right)\cong\Spec \mathbb{K}[\x,\y]/(\y,\y-\x^2)\cong\Spec \mathbb{K}[\x]/(\x^2).$$
:::

From this viewpoint we can also see how to define the fiber $\varphi^{-1}(y_0)$ of a scheme morphism $\varphi:X \rightarrow Y$ at $y_0\in Y$. Whether $y_0$ is a closed point or not, viewing it as $\iota:\{y_0\}\hookrightarrow Y$ and taking the fiber product of $\iota$ and $\varphi$ suffices. For this we must describe $\iota$ as a scheme morphism.

To do this, consider the residue field $\kappa(y)$ at $y$. Then $\Spec\kappa(y)$ is always a one-point set. Moreover, taking an affine open subset $V=\Spec B$ of $Y$ containing $y$, and letting $y$ correspond to the prime ideal $\mathfrak{q}_y$, the canonical morphism

$$B \rightarrow B_{\mathfrak{q}_y} \rightarrow B_{\mathfrak{q}_y}/\mathfrak{q}_y B_{\mathfrak{q}_y} =\kappa(\mathfrak{q}_y)=\kappa(y)$$

defines $\Spec\kappa(y)\rightarrow \Spec B$, and the (unique) point $(0)$ of $\Spec \kappa(y)$ is sent to $\mathfrak{q}_y$ via the above morphism. Therefore we define the following.

::: Definition 12
For a scheme morphism $\varphi: X \rightarrow Y$, the *fiber* at a point $y\in Y$ is defined as

$$\varphi^{-1}(y)=X\times_Y\Spec \kappa(y).$$

If $Y$ is irreducible, the fiber at the generic point of $Y$ is called the *generic fiber*.
:::

::: Example 13
For an algebraically closed field $\mathbb{K}$, define the ring homomorphism $\mathbb{K}[\x] \rightarrow \mathbb{K}[\y]$ by $\x \mapsto \y^2$, and consider the scheme morphism $\varphi: \Spec \mathbb{K}[\y] \rightarrow \Spec \mathbb{K}[\x]$ obtained from it. Then the residue field at any point $(\x-a)$ of $\Spec\mathbb{K}[\x]$ is

$$\Frac(\mathbb{K}[\x]/(\x-a))=\mathbb{K}[\x]/(\x-a).$$

Now for any $a\in \mathbb{K}$,

$$\varphi^{-1}((\x-a))=\Spec \mathbb{K}[\y]\times_{\Spec \mathbb{K}[\x]}\Spec \mathbb{K}[\x]/(\x-a)\cong \Spec(\mathbb{K}[\y]\otimes_{\mathbb{K}[\x]}\mathbb{K}[\x]/(\x-a))=\Spec \mathbb{K}[\y]/(\y^2-a)$$

and therefore if $a=0$ then $\varphi^{-1}((\x))\cong\Spec \mathbb{K}[\y]/(\y^2)$, and if $a\neq 0$ then from the assumption that $\mathbb{K}$ is algebraically closed we know

$$\Spec \mathbb{K}[\y]/(\y^2-a)\cong \Spec \mathbb{K}[\y]/(\y-\sqrt{a})\coprod \Spec \mathbb{K}[\y]/(\y+\sqrt{a}).$$

On the other hand, for the generic point $(0)$ of $\mathbb{K}[\x]$ we have $\kappa((0))=\mathbb{K}(\x)$, so

$$\varphi^{-1}((0))=\Spec \mathbb{K}[\y]\times_{\Spec \mathbb{K}[\x]}\Spec \mathbb{K}(\x)\cong \Spec\mathbb{K}(\y).$$
:::

The above example is what we already examined in [§Properties of Scheme Morphisms, ⁋Example 15](/en/math/scheme_theory/properties_of_scheme_morphisms#ex15). In that example we claimed that a finite morphism is always quasi-finite, and now we can prove this.

::: Proposition 14
A finite morphism $\varphi: X \rightarrow Y$ is a quasi-finite morphism.
:::
::: Proof
It suffices to show the affine case. That is, it suffices to show that for any finite ring homomorphism $\phi: B \rightarrow A$ and any prime ideal $\mathfrak{q}$ of $B$, the ring $A\otimes_B\kappa(\mathfrak{q})$ has only finitely many prime ideals. Since $\phi$ is finite, $A\otimes_B\kappa(\mathfrak{q})$ is a finite $\kappa(\mathfrak{q})$-algebra and hence Artinian, from which we obtain the desired result. ([\[Commutative Algebra\] §Jordan-Hölder Theorem, ⁋Theorem 4](/en/math/commutative_algebra/Jordan-Holder_theorem#thm4))
:::

From the above examples and propositions we can make an important observation: if $X \rightarrow S$ satisfies some property $P$ of scheme morphisms, then the base change $X\times_SS' \rightarrow S'$ via any $S' \rightarrow S$ also satisfies it. This is not a coincidence; in fact, most properties we are interested in are closed under base change.

::: Proposition 15
If a scheme morphism $\varphi:X \rightarrow Z$ is quasicompact (resp. quasiseparated, affine, finite, integral, locally of finite type, finite type, locally of finite presentation, finite presentation, quasi-finite, surjective), then the base change $X\times_ZY \rightarrow Y$ of $\varphi$ via any scheme morphism $Y \rightarrow Z$ is also such.
:::
::: Proof
Let us first carry out a reduction common to all properties. Choose the $\Spec A$ forming an affine open covering of $Z$, and for each $\Spec A$ cover the preimage under $Y \rightarrow Z$ by affine open subsets $\Spec C$; the $\Spec C$ obtained in this way then form an affine open covering of $Y$. Now letting the projection be $\rho_Y: X\times_ZY \rightarrow Y$, from the fact used in the proofs of [Lemma 3](#lem3) and [Lemma 4](#lem4) that "if the two small squares are fiber diagrams then the outer large square is also a fiber diagram," we obtain

$$\rho_Y^{-1}(\Spec C)\cong X\times_Z\Spec C\cong \varphi^{-1}(\Spec A)\times_{\Spec A}\Spec C.$$

Thus, writing $X_A=\varphi^{-1}(\Spec A)$ and $W=X_A\times_{\Spec A}\Spec C$, examining the base change $\rho_Y$ over $\Spec C$ is the same as examining the base change $W \rightarrow \Spec C$ of $X_A \rightarrow \Spec A$ along $\Spec C \rightarrow \Spec A$. Moreover, for the same reason, for any affine open subset $\Spec B$ of $X_A$ the preimage under the projection $\rho: W \rightarrow X_A$ is, by [Lemma 2](#lem2),

$$\rho^{-1}(\Spec B)\cong \Spec B\times_{\Spec A}\Spec C\cong \Spec (B\otimes_AC)$$

so whenever an affine open covering $\{\Spec B_i\}$ of $X_A$ is given, $\{\Spec (B_i\otimes_AC)\}$ becomes an affine open covering of $W$. That is, every problem reduces to a problem about the ring homomorphism $C \rightarrow B\otimes_AC$. We now examine each property.

First, suppose $\varphi$ is affine. Then $X_A$ is an affine scheme $\Spec B$, and therefore $\rho_Y^{-1}(\Spec C)=W\cong\Spec (B\otimes_AC)$ is affine, so by the affine open covering $\{\Spec C\}$ of $Y$ and [§Properties of Scheme Morphisms, ⁋Proposition 9](/en/math/scheme_theory/properties_of_scheme_morphisms#prop9), $\rho_Y$ is affine.

Suppose $\varphi$ is quasi-compact. Then $X_A$ is quasi-compact, so it is covered by finitely many affine open subsets $\Spec B_1,\ldots, \Spec B_n$, and therefore $W$ is covered by finitely many affine open subsets $\Spec (B_i\otimes_AC)$ and is quasi-compact. Now by the first result of [§Properties of Scheme Morphisms, ⁋Proposition 7](/en/math/scheme_theory/properties_of_scheme_morphisms#prop7), $\rho_Y$ is quasi-compact.

Suppose $\varphi$ is quasi-separated. Then $X_A$ is a quasi-separated scheme. Choosing an affine open covering $\{\Spec B_i\}$ of $X_A$, $\{W_i=\Spec (B_i\otimes_AC)\}$ is an affine open covering of $W$, and since $\Spec B_i\cap \Spec B_j$ is quasi-compact we can write it as a union of finitely many principal open sets $D(h_1),\ldots, D(h_s)$ of $\Spec B_i$ ([§Spectra, ⁋Lemma 11](/en/math/scheme_theory/spectrums#lem11)), so

$$W_i\cap W_j=\rho^{-1}(\Spec B_i\cap \Spec B_j)=\bigcup_{t=1}^s\Spec \bigl((B_i)_{h_t}\otimes_AC\bigr)$$

is a union of finitely many affine open subsets, hence quasi-compact. Now let us show in general that if a scheme $W$ has an affine open covering $\{W_i\}$ such that all $W_i\cap W_j$ are quasi-compact, then $W$ is quasi-separated. Since any quasi-compact open subset of $W$ is a union of finitely many affine open subsets, it suffices to show that for any two affine open subsets $P,Q$ of $W$, the intersection $P\cap Q$ is quasi-compact. By [§Topology of Schemes, ⁋Lemma 11](/en/math/scheme_theory/topology_of_schemes#lem11) and the quasi-compactness of $P,Q$, the sets $P$ and $Q$ are each covered by finitely many open sets that are principal open in both themselves and some $W_i$, so ultimately it suffices to show that $D(f)\cap D(g)$ is quasi-compact for a principal open set $D(f)$ of $W_i$ and a principal open set $D(g)$ of $W_j$. But $D(f)\cap D(g)\subseteq W_i\cap W_j$ and $W_i\cap W_j$ is quasi-compact, so we can write it as a union of finitely many principal open sets $D(h_1),\ldots, D(h_s)$ of $W_i$, and therefore

$$D(f)\cap D(g)=\bigcup_{t=1}^s\bigl(D(fh_t)\cap D(g)\bigr).$$

Now each $D(fh_t)$ is an affine open subset contained in $W_i\cap W_j$, so viewing it as an affine open subset of $W_j$, the intersection $D(fh_t)\cap D(g)$ is the principal open set defined by the restriction of $g$ on the affine scheme $D(fh_t)$ ([§Spectra, ⁋Proposition 8](/en/math/scheme_theory/spectrums#prop8)) and hence is affine. That is, $D(f)\cap D(g)$ is a union of finitely many affine open subsets, so it is quasi-compact. From the above, $W$ is quasi-separated, and by the second result of [§Properties of Scheme Morphisms, ⁋Proposition 7](/en/math/scheme_theory/properties_of_scheme_morphisms#prop7), $\rho_Y$ is quasi-separated.

Suppose $\varphi$ is integral (resp. finite). Then $\varphi$ is affine, so $X_A=\Spec B$ and $A \rightarrow B$ is integral (resp. finite). Therefore $\rho_Y^{-1}(\Spec C)=\Spec (B\otimes_AC)$, and by [\[Commutative Algebra\] §Integral Extensions, ⁋Proposition 14](/en/math/commutative_algebra/integral_extension#prop14), $C \rightarrow B\otimes_AC$ is also integral (resp. finite). That these two properties are affine-local on target was examined right after [§Properties of Scheme Morphisms, ⁋Definition 11](/en/math/scheme_theory/properties_of_scheme_morphisms#def11), so checking on the affine open covering $\{\Spec C\}$ of $Y$ is sufficient.

Suppose $\varphi$ is locally of finite type. Choosing an affine open covering $\{\Spec B_i\}$ of $X_A$, each $A \rightarrow B_i$ is of finite type, and letting $x_1,\ldots, x_n$ be generators of $B_i$ as an $A$-algebra, $B_i\otimes_AC$ is generated as a $C$-algebra by $x_1\otimes 1,\ldots, x_n\otimes 1$, so $C \rightarrow B_i\otimes_AC$ is also of finite type. Now we must obtain the same conclusion for *all* affine open subsets of $W$; to do this, define the property $Q$ for an affine open subset $\Spec R$ of $W$ as "$C \rightarrow R$ is of finite type," and let us show that $Q$ is an affine-local property in the sense of [§Topology of Schemes, ⁋Definition 9](/en/math/scheme_theory/topology_of_schemes#def9). Then from the affine open covering $\{\Spec (B_i\otimes_AC)\}$ just constructed and [§Topology of Schemes, ⁋Lemma 12](/en/math/scheme_theory/topology_of_schemes#lem12), we obtain the desired conclusion.

The first condition is obvious: if $C \rightarrow R$ is of finite type, then adding $1/h$ to the generators of $R$ makes $R_h$ finitely generated as a $C$-algebra. For the second condition, let $R=(h_1,\ldots, h_m)$ and suppose each $C \rightarrow R_{h_t}$ is of finite type. For each $t$, choose a finite set generating $R_{h_t}$ as a $C$-algebra and then clear denominators; there exist elements $x_{t1},\ldots, x_{tn_t}$ of $R$ such that $R_{h_t}$ is generated as a $C$-algebra by the $x_{tk}/1$ and $1/h_t$. Also choose $a_t\in R$ with $1=\sum_{t=1}^ma_th_t$. Now let $R'$ be the $C$-subalgebra of $R$ generated by the finite set $\{h_t\}\cup\{a_t\}\cup\{x_{tk}\}$; then $R'$ is a finite type $C$-algebra, so it suffices to show $R'=R$. For any $x\in R$, since $x/1$ in $R_{h_t}$ is a polynomial in the $x_{tk}/1$ and $1/h_t$ with coefficients in $C$, for suitable $r_t\in R'$ and $n_t\geq 0$ we have $x/1=r_t/h_t^{n_t}$, and therefore for suitable $N_t$ we have in $R$ that $h_t^{N_t}(h_t^{n_t}x-r_t)=0$, i.e. $h_t^{N_t+n_t}x=h_t^{N_t}r_t\in R'$. Since there are finitely many $t$, we can choose a common $M$ so that $h_t^Mx\in R'$ for all $t$. On the other hand, from $1=\sum_ta_th_t$ with $a_t,h_t\in R'$, the elements $h_1,\ldots, h_m$ generate the unit ideal of $R'$, and raising both sides of this identity to a sufficiently high power we know that $h_1^M,\ldots, h_m^M$ also generate the unit ideal of $R'$. That is, there exist $c_t\in R'$ with $1=\sum_tc_th_t^M$, and therefore

$$x=\sum_{t=1}^mc_t(h_t^Mx)\in R'.$$

From the above, $Q$ is an affine-local property, and since locally of finite type is affine-local on target as examined right after [§Properties of Scheme Morphisms, ⁋Definition 13](/en/math/scheme_theory/properties_of_scheme_morphisms#def13), $\rho_Y$ is locally of finite type. Also, a morphism of finite type is a morphism that is quasi-compact and locally of finite type, so combining with the quasi-compact case above, finite type is also preserved under base change.

Suppose $\varphi$ is locally of finite presentation. The condition of [§Properties of Scheme Morphisms, ⁋Definition 17](/en/math/scheme_theory/properties_of_scheme_morphisms#def17) is a condition on *some* affine open covering of the preimage, so this case is rather simple. By assumption there exists an affine open covering $\{\Spec B_i\}$ of $X_A$ such that each $B_i$ is of the form

$$B_i\cong A[\x_1,\ldots, \x_n]/(f_1,\ldots, f_m)$$

and then from the isomorphism $C\otimes_AA[\x_1,\ldots, \x_n]\cong C[\x_1,\ldots, \x_n]$ examined after [Example 9](#ex9) and from [Lemma 10](#lem10),

$$B_i\otimes_AC\cong C[\x_1,\ldots, \x_n]/(\bar{f}_1,\ldots, \bar{f}_m)$$

(where $\bar{f}_k$ is obtained by sending the coefficients of $f_k$ to $C$), so $C \rightarrow B_i\otimes_AC$ is also finitely presented. That is, the affine open covering $\{\Spec (B_i\otimes_AC)\}$ of $W$ witnesses the required condition over $\Spec C$. That this property is affine-local on target is obtained by applying [§Topology of Schemes, ⁋Lemma 12](/en/math/scheme_theory/topology_of_schemes#lem12) to the property "$\varphi^{-1}(\Spec B)$ has an affine open covering $\{\Spec R_i\}$ such that all $B \rightarrow R_i$ are finitely presented." Indeed, the first condition of [§Topology of Schemes, ⁋Definition 9](/en/math/scheme_theory/topology_of_schemes#def9) follows from the fact that $\varphi^{-1}(D(f))$ is covered by $\Spec (R_i)_f$ and $(R_i)_f\cong R_i\otimes_BB_f$ is a base change of a finitely presented homomorphism; the second condition follows from the fact that $B \rightarrow B_f\cong B[\y]/(f\y-1)$ is finitely presented and the composition of finitely presented homomorphisms is again finitely presented. Finally, a morphism of finite presentation is a morphism that is quasi-compact, quasi-separated, and locally of finite presentation, so combining the previous results this property is also preserved under base change.

Now let us compute fibers for the remaining two properties. For $y\in Y$ and its image $z\in Z$, since $\mathcal{O}_{Z,z} \rightarrow \mathcal{O}_{Y,y}$ is a local homomorphism, $\Spec \kappa(y) \rightarrow Y \rightarrow Z$ factors through $\Spec\kappa(z) \rightarrow Z$, and therefore composing fiber diagrams as above, by [Definition 12](#def12) we obtain

$$\rho_Y^{-1}(y)=(X\times_ZY)\times_Y\Spec \kappa(y)\cong X\times_Z\Spec \kappa(y)\cong \varphi^{-1}(z)\times_{\Spec \kappa(z)}\Spec \kappa(y).$$

Also, by [Lemma 3](#lem3), for an affine open subset $\Spec R$ of $\varphi^{-1}(z)$, the scheme $\Spec (R\otimes_{\kappa(z)}\kappa(y))$ is an open subset of $\rho_Y^{-1}(y)$, and such sets cover $\rho_Y^{-1}(y)$.

Suppose $\varphi$ is surjective. First we check that $\varphi^{-1}(z)$ is nonempty. Choose $x\in X$ with $\varphi(x)=z$, and choose an affine open subset $\Spec B\subseteq X$ containing $x$ that maps into $\Spec A$ under $\varphi$, together with the corresponding ring homomorphism $\phi:A \rightarrow B$. Letting $\mathfrak{q}\subset B$ and $\mathfrak{p}\subset A$ be the prime ideals corresponding to $x$ and $z$ respectively, we have $\phi^{-1}(\mathfrak{q})=\mathfrak{p}$, and by [Lemma 10](#lem10) and properties of localization,

$$B\otimes_A\kappa(\mathfrak{p})\cong (B/\mathfrak{p}B)_\mathfrak{p}$$

so $\mathfrak{q}$ defines a prime ideal of this ring. That is, $\varphi^{-1}(z)\neq\emptyset$. Now choosing a nonempty affine open subset $\Spec R$ of $\varphi^{-1}(z)$, $R$ is a nonzero $\kappa(z)$-algebra, and since $\kappa(y)$ is a nonzero $\kappa(z)$-vector space, $R\otimes_{\kappa(z)}\kappa(y)\neq 0$. A nonzero ring always has a prime ideal, so $\Spec (R\otimes_{\kappa(z)}\kappa(y))\neq\emptyset$, and therefore $\rho_Y^{-1}(y)\neq\emptyset$. Since $y$ was arbitrary, $\rho_Y$ is surjective.

Finally, suppose $\varphi$ is quasi-finite. Since $\varphi$ is of finite type, $\rho_Y$ is also of finite type as seen above, so it suffices to show that all fibers of $\rho_Y$ are finite sets. Since $\varphi$ is quasi-compact, applying preservation of quasi-compactness under base change to $\Spec \kappa(z) \rightarrow Z$, we know that $\varphi^{-1}(z)$ is quasi-compact, and therefore can be covered by finitely many affine open subsets $\Spec R_1,\ldots, \Spec R_n$. Similarly, since $\varphi$ is locally of finite type, each $R_l$ is a finite type $\kappa(z)$-algebra, and by assumption each $\Spec R_l$ is a finite set.

Now let us show that a finite type $\mathbb{K}$-algebra $R$ having only finitely many prime ideals is always a finite-dimensional $\mathbb{K}$-vector space. First we show that any prime ideal $\mathfrak{p}$ of $R$ is maximal. If there exists a prime ideal properly containing $\mathfrak{p}$, then $d=\dim R/\mathfrak{p}\geq 1$, and by [\[Commutative Algebra\] §Noether Normalization, ⁋Theorem 1](/en/math/commutative_algebra/noether_normalization#thm1), $R/\mathfrak{p}$ contains the polynomial ring $\mathbb{K}[\x_1,\ldots, \x_d]$ as a subring and is finitely generated over it, in particular an integral extension. But since $d\geq 1$, $\mathbb{K}[\x_1,\ldots, \x_d]$ has infinitely many prime ideals generated by distinct irreducible polynomials of $\mathbb{K}[\x_1]$, and by [\[Commutative Algebra\] §Lying Over and Going Up, ⁋Proposition 1](/en/math/commutative_algebra/lying_over_and_going_up#prop1) each of these has a prime ideal of $R/\mathfrak{p}$ lying over it, contradicting the assumption that $R$ has only finitely many prime ideals. Therefore all prime ideals of $R$ are maximal, and since $R$ is Noetherian by [\[Commutative Algebra\] §Basic Notions, ⁋Theorem 12](/en/math/commutative_algebra/basic_notions#thm12), by [\[Commutative Algebra\] §Jordan-Hölder Theorem, ⁋Theorem 4](/en/math/commutative_algebra/Jordan-Holder_theorem#thm4) $R$ has finite length as an $R$-module. The composition factors are all of the form $R/\mathfrak{m}$, and since a field is a Jacobson ring, by [\[Commutative Algebra\] §Nullstellensatz, ⁋Theorem 4](/en/math/commutative_algebra/nullstellensatz#thm4) $R/\mathfrak{m}$ is a finite extension of $\mathbb{K}$. Therefore $R$ is a finite-dimensional $\mathbb{K}$-vector space.

Then each $R_l$ is a finite-dimensional $\kappa(z)$-vector space, so $R_l\otimes_{\kappa(z)}\kappa(y)$ is also a finite-dimensional $\kappa(y)$-vector space, and hence becomes an Artinian ring having only finitely many prime ideals. ([\[Commutative Algebra\] §Jordan-Hölder Theorem, ⁋Theorem 4](/en/math/commutative_algebra/Jordan-Holder_theorem#thm4)) Now $\rho_Y^{-1}(y)$ is covered by finitely many $\Spec (R_l\otimes_{\kappa(z)}\kappa(y))$, so it is a finite set, and thus we know that $\rho_Y$ is quasi-finite.
:::
