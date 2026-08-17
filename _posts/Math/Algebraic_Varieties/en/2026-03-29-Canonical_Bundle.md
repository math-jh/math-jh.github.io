---
title: "Canonical Line Bundle"
description: "We examine the canonical line bundle defined as the top exterior power of the cotangent bundle, and understand the geometric structure on smooth algebraic varieties through the relationship between vector bundles and coherent sheaves."
excerpt: "Canonical bundle and canonical divisor"

categories: [Math / Algebraic Varieties]
permalink: /en/math/algebraic_varieties/canonical_bundle
sidebar:
    nav: "algebraic_varieties-en"

date: 2026-03-29
weight: 12
translated_at: 2026-08-17T11:48:12+00:00
translation_source: kimi-cli
---
In [§Linear Systems](/en/math/algebraic_varieties/linear_systems), we saw that a basepoint-free complete linear system of a line bundle can be used to embed a variety into projective space, and when this defines a closed embedding, such a line bundle is called *very ample*.

Despite the significant geometric influence that line bundles exert, we have not yet properly examined how to define a line bundle on an arbitrary variety in general. If $X$ is a *smooth* variety, we can consider the cotangent bundle $\Omega_X^1$ defined on it via [§Line Bundles and Vector Bundles, ⁋Example 24](/en/math/algebraic_varieties/line_bundles#ex24), and by taking its top exterior power we obtain the *canonical bundle* $\omega_X$. The goal of this post is to study this bundle $\omega_X$.

## Vector Bundles and Quasi-Coherent Sheaves

As mentioned above, to define $\omega_X$ we start from the cotangent bundle $\Omega_X^1$. We have already seen that this is the bundle of differential forms on $X$. Let us verify that this aligns with differentiation in the algebraic setting. ([[Commutative Algebra] §Differentials, ⁋Definition 3](/en/math/commutative_algebra/differentials#def3)) For this, we need to examine the process of transferring an $A$-module $M$ to a vector bundle over $X$, given an affine variety $X$ with coordinate ring $A$ and an $A$-module $M$.

Our basic philosophy, using [§Affine Varieties](/en/math/algebraic_varieties/affine_varieties), is that a homomorphism between coordinate *rings* can be transferred to a morphism between varieties in the opposite direction, and thus we can obtain a bundle over $X$. However, the problem is that $M$ is not a ring. That is, multiplication is not defined on $M$. Yet, according to [[Multilinear Algebra] §Tensor Algebras, ⁋Definition 5](/en/math/multilinear_algebra/tensor_algebras#def5), we can consider the symmetric algebra $\S(M)$, which forcibly introduces a (commutative) multiplication on $M$.

However, there is a problem in applying this directly. Recall that our goal is to view $M$ as a vector bundle over $X$. Roughly speaking, our goal is to attach $M$ nicely over each point of $X$, and according to [§Affine Varieties](/en/math/algebraic_varieties/affine_varieties), if $M$ appears in the world of varieties (as fibers), then the coordinate ring defining it should be its coordinate functions. That is, we must use $M^\vee$ instead of $M$, and therefore we consider $\S_A(M^\vee)$ rather than $\S_A(M)$. Then this is an $A$-algebra, so we obtain a map of coordinate rings $A\rightarrow \S_A(M^\vee)$, and applying [§Affine Varieties](/en/math/algebraic_varieties/affine_varieties) to this gives a morphism from some variety $V(M)$ to $X$.

Let us verify that this morphism actually carries a vector bundle structure over $X$. A point $x\in X$ corresponds to a maximal ideal $\mathfrak{m}_x$ of the coordinate ring $A$, and thus the set-theoretic fiber $V(M)_x = \pi^{-1}(x)$ over $x$ in $V(M) \rightarrow X$ consists of the maximal ideals of $\S_A(M^\vee)$ containing $\mathfrak{m}_x\cdot \S_A(M^\vee)$.

Algebraically, to obtain the coordinate ring defining this fiber, we must first think about what functions are defined on it. Now, the functions contained in the maximal ideal $\mathfrak{m}_x$ defining $x\in X$ all vanish at $x$, so it is reasonable to think of functions defined on this fiber as $A/\mathfrak{m}_x$-valued functions. We call this field $\kappa(x)=A/\mathfrak{m}_x$ the *residue field* at $x$, and thus in general $\kappa(x)$ is an algebraic extension of $\mathbb{K}$. ([[Commutative Algebra] §Nullstellensatz, ⁋Theorem 4](/en/math/commutative_algebra/nullstellensatz#thm4)) Since we usually consider the case where $\mathbb{K}$ is an algebraically closed field, we may simply think of $\kappa(x)$ as $\mathbb{K}$.

Now, from the above discussion, we know that we should consider the collection of $\kappa(x)$-valued functions on $\S_A(M^\vee)$, namely $\S_A(M^\vee)\otimes_A\kappa(x)$. Then, from the fact that symmetric algebra commutes with tensor product, we obtain the identity

$$\S_A(M^\vee)\otimes_A\kappa(x)=\S_{\kappa(x)} (M^\vee\otimes_A\kappa(x))=\S_{\kappa(x)}(M_x^\vee)$$

where on the right-hand side $M_x = M \otimes_A \kappa(x)$, and the tensor products appearing here can be thought of, roughly as explained above, as viewing all objects as $\mathbb{K}$-vector spaces (more precisely, $\kappa(x)$-vector spaces).

Now $\S_{\kappa(x)}(M_x^\vee)$ is a polynomial algebra with coefficients in $\kappa(x)$ and with linear terms given by the elements of $M_x^\vee$, and thus the fiber $V(M)_x$ consists of points having the elements of $M_x^\vee$ as coordinate functions, so these points can be thought of as the double dual of $M_x$. Now if $M$ is a finitely generated $A$-module, the canonical isomorphism $M_x\cong M_x^{\vee\vee}$ exists, and from this we can understand each fiber $V(M)_x$ as the $\kappa(x)$-vector space $M_x$.

If $M$ is finitely generated projective, that is, a locally free $A$-module, then through additional computation we can verify that this data satisfies the locally trivial condition, and thereby we can confirm that we may think of this as a vector bundle over $X$.

On the other hand, showing that this vector bundle is locally trivial is essentially the same as examining it in the language of sheaves. We have not used the language of sheaves much for geometric intuition, but roughly speaking, it is as follows.

As above, given an affine variety $X$ with coordinate ring $A$ and an $A$-module $M$, we define the sheaf $\widetilde{M}$ over $X$ on a basic open set $U=D(f)$ by the formula

$$\widetilde{M}(U)=M\otimes_A \mathcal{O}_X(U)$$

This is basically the same context as introducing $\kappa(x)$ above, and although we have not computed it in detail, when showing the local triviality of $V(M)$ we would have base changed using the structure sheaf in this manner. Then in particular for all of $X$ we have

$$\widetilde{M}(X)=M\otimes_A A=M$$

so that $M$ becomes the global section space of $\widetilde{M}$.

These two definitions are merely expressing the same object in different geometric languages. That is, for an affine variety $X$ with coordinate ring $A$ and a finitely generated projective $A$-module $M$, the total space corresponding to $\widetilde{M}$ is precisely $V(M)$, and the section sheaf of $V(M)$ is $\widetilde{M}$.

In general, compared to concrete geometric language, the advantage of sheaf language is that it can be applied in more general situations. For example, we define the following. ([[Commutative Algebra] §Basic Notions, ⁋Definition 8](/en/math/commutative_algebra/basic_notions#def8))

::: Definition 1
An $\mathcal{O}_X$-module $\mathcal{F}$ on a general variety $X$ is called a *quasi-coherent sheaf* if there exists an affine open cover $\{U_i\}$ of $X$ and $A_i=\mathcal{O}_X(U_i)$-modules $M_i$ for each such that $\mathcal{F}\vert_{U_i}\cong \widetilde{M_i}$. If each $M_i$ is a finitely generated $A_i$-module, then $\mathcal{F}$ is called a *coherent sheaf*.
:::

When dealing with quasi-coherent sheaves in general, one must be careful because different $M$'s may be attached on each affine cover, but when restricted to the affine case, $M\mapsto \widetilde{M}$ defines a categorical equivalence from $\lMod{A}$ to $\QCoh(X)$. This can be verified by checking that for any quasi-coherent sheaf $\mathcal{F}$, $\widetilde{\Gamma(X,\mathcal{F})}$ recovers $\mathcal{F}$ itself. That is, our slogan is: in the affine case, a quasi-coherent sheaf is an $A$-module, and a coherent sheaf is a finitely generated $A$-module.

From this perspective, a vector bundle can be thought of as a very special case of a (quasi-)coherent sheaf. Or conversely, when thinking of these (quasi-)coherent sheaves, one may think of them as very general forms of vector bundles. Specifically, a coherent sheaf can be thought of as an extension of the category of (finite rank) vector bundles so that it is closed under the operations of an abelian category, namely kernels, images, cokernels, etc., and intuitively it can be thought of as a vector bundle whose fiber dimension may vary from point to point. A quasi-coherent sheaf is what remains after removing the finite rank condition.

Since the coordinate ring of a variety is Noetherian, by [[Commutative Algebra] §Basic Notions, ⁋Proposition 9](/en/math/commutative_algebra/basic_notions#prop9) the coherent condition and the finitely generated condition coincide even on a singular variety, and thus the above slogan holds just as well in geometric situations. However, one somewhat cautionary point from the above intuition is that how close a coherent sheaf is to a vector bundle depends on the geometry of $X$. Any coherent sheaf on a smooth variety admits a locally free resolution of finite length, but this is not the case on a singular variety.

## Canonical Bundle

We are now ready to define the canonical bundle. For this, we must first introduce the cotangent bundle on a variety, and the following definition is what we already saw in [§Line Bundles and Vector Bundles, ⁋Example 24](/en/math/algebraic_varieties/line_bundles#ex24), but we introduce it again for completeness.

::: Definition 2
The *cotangent bundle* $\Omega_X^1$ of a smooth variety $X$ is the dual vector bundle of the tangent bundle $\mathcal{T}_X$.
:::

Then the construction we examined in the previous section is for the following.

::: Proposition 3
For a smooth affine variety $X$ with coordinate ring $A$, $\Omega_X^1$ is the vector bundle corresponding to $\widetilde{\Omega_{A/\mathbb{K}}}$. ([[Commutative Algebra] §Differentials, ⁋Definition 3](/en/math/commutative_algebra/differentials#def3))
:::

::: Proof
For this, it will be convenient to rewrite the previously defined tangent bundle and cotangent bundle in the language of sheaves. First, let us define the tangent sheaf $\mathcal{T}_X$. For an open subset $U$ of $X$, we define the sheaf given by the collection of $\mathbb{K}$-derivations $\Der_\mathbb{K}(\mathcal{O}_X(U),\mathcal{O}_X(U))$ on $\mathcal{O}_X(U)$ as the tangent sheaf.

Our main tool is the universal property of Kähler differentials. ([[Commutative Algebra] §Differentials, ⁋Lemma 2](/en/math/commutative_algebra/differentials#lem2)) That is, for any $A$-module $N$, let us use the natural isomorphism

$$\Der_\mathbb{K}(A,N)\cong\Hom_A(\Omega_{A/\mathbb{K}},N)$$

Then, by the fact that $\widetilde{(-)}$ is a categorical equivalence and the above natural isomorphism,

$$\Hom_{\mathcal{O}_X}(\widetilde{\Omega_{A/\mathbb{K}}},\widetilde{N})\cong\Hom_A(\Omega_{A/\mathbb{K}},N)\cong\Der_\mathbb{K}(A,N)$$

holds. Moreover, if we think of the sheaf of derivations, the last term $\Der_\mathbb{K}(A,N)$ is again $\Der_\mathbb{K}(\mathcal{O}_X, \widetilde{N})$, so the identity

$$\Hom_{\mathcal{O}_X}(\widetilde{\Omega_{A/\mathbb{K}}}, \widetilde{N})\cong \Der_\mathbb{K}(\mathcal{O}_X, \widetilde{N})$$

holds. In particular, for the case $N=A$, that is, $\widetilde{N}=\mathcal{O}_X$, we have

$$\Hom_{\mathcal{O}_X}(\widetilde{\Omega_{A/\mathbb{K}}}, \mathcal{O}_X)\cong\Der_\mathbb{K}(\mathcal{O}_X, \mathcal{O}_X)\cong \mathcal{T}_X$$

On the other hand, from the fact that $\Omega_{A/\mathbb{K}}$ is a finitely generated projective $A$-module, we know that $\widetilde{\Omega_{A/\mathbb{K}}^\vee}\cong \widetilde{\Omega_{A/\mathbb{K}}}^\vee$, and therefore

$$\widetilde{\Omega_{A/\mathbb{K}}}^\vee\cong \widetilde{\Omega_{A/\mathbb{K}}^\vee}\cong \widetilde{\Der_\mathbb{K}(A,A)}\cong \mathcal{T}_X$$

so the desired claim holds.
:::

This result shows that the cotangent bundle is represented by differential $1$-forms, just as we imagine.

::: Example 4
The cotangent bundle of $\mathbb{A}^n$ is $\Omega_{\mathbb{A}^n}^1 \cong \mathcal{O}_{\mathbb{A}^n}^{\oplus n}$. Algebraically, if we fix the coordinate ring $\mathbb{K}[\x_1, \ldots, \x_n]$ of $\mathbb{A}^n$, then the Kähler differentials of this $\mathbb{K}$-algebra form the free module $\bigoplus_{i=1}^n \mathbb{K}[\x_1, \ldots, \x_n]  \dd{\x_i}$, so this result aligns well with our intuition.
:::

On the other hand, for any smooth variety $X$ of dimension $n$ and its cotangent bundle $\Omega_X^1$, since each fiber of $\Omega_X^1$ is $n$-dimensional, we know that taking its $n$-fold exterior product yields a line bundle. ([§Line Bundles and Vector Bundles, ⁋Example 24](/en/math/algebraic_varieties/line_bundles#ex24))

::: Definition 5
The *canonical line bundle* $\omega_X$ of a smooth variety $X$ of dimension $n$ is defined as the top exterior power of the cotangent bundle

$$\omega_X = \bigwedge\nolimits^{n} \Omega_X^1$$
:::

We call a global section $s\in \Gamma(X, \omega_X)$ of the canonical bundle $\omega_X$ a *regular $n$-form* on $X$. These are $n$-forms of the form $f\dd{\x_1} \wedge \cdots \wedge \dd{\x_n}$ for a regular function $f$, when we pick a trivializing open set $U$ of $\omega_X$ and identify it with the cotangent bundle over affine space as in [Example 4](#ex4).

On the other hand, from the correspondence between line bundles and divisor classes, we can define the following.

::: Definition 6
The divisor class corresponding to the canonical bundle $\omega_X$ is called the *canonical divisor* and denoted by $K_X$. That is, $\omega_X \cong \mathcal{O}_X(K_X)$.
:::

Since we use [§Line Bundles and Vector Bundles, ⁋Proposition 19](/en/math/algebraic_varieties/line_bundles#prop19) for this, note that $K_X$ is defined only as a divisor class.

## Canonical Bundle of $\mathbb{P}^n$

As in previous posts, the most familiar example for us is that of $\mathbb{P}^n$. Intuitively, if we unpack the quotient

$$\mathbb{P}^n=(\mathbb{A}^{n+1}\setminus\{0\})/\mathbb{K}^\times$$

defining $\mathbb{P}^n$, the $\mathbb{K}^\times$-action is in the direction radiating from the origin, that is, the direction defined by the Euler vector field, and from the perspective of $\mathbb{P}^n$ this is merely a trivial line bundle. Then the tangent space of $\mathbb{P}^n$ corresponds to the remaining part after quotienting the directions of $\mathbb{A}^{n+1}$, that is, the linear forms, by this trivial line bundle. That is, there exists the following short exact sequence corresponding to the tangent bundle

$$0 \rightarrow \mathcal{O}_{\mathbb{P}^{n}}\rightarrow \mathcal{O}_{\mathbb{P}^n}(1)^{\oplus (n+1)}\rightarrow T_{\mathbb{P}^n}\rightarrow 0$$

and taking the dual of this yields the following.

::: Proposition 7 (Euler Exact Sequence)
There exists an exact sequence of vector bundles over $\mathbb{P}^n$

$$0 \rightarrow \Omega_{\mathbb{P}^n}^1 \rightarrow \mathcal{O}_{\mathbb{P}^n}(-1)^{\oplus(n+1)} \rightarrow \mathcal{O}_{\mathbb{P}^n} \rightarrow 0$$
:::

To compute the canonical bundle of $\mathbb{P}^n$ from this, we must take the top exterior power of this exact sequence. More generally, suppose we are given a short exact sequence

$$0\rightarrow E\rightarrow F\rightarrow L\rightarrow 0$$

where $E$ is a vector bundle of rank $r$ and $L$ is a vector bundle of rank $1$. Taking $\bigwedge\nolimits^{r+1}(-)$ of this sequence, from the fact that determinant is compatible with tensor product, we know that

$$\det(F)\cong \det(E)\otimes \det(L)$$

Now let us apply this to the Euler exact sequence of [Proposition 7](#prop7). Since $E=\Omega_{\mathbb{P}^n}^1$ has rank $n$, $F=\mathcal{O}_{\mathbb{P}^n}(-1)^{\oplus(n+1)}$ has rank $n+1$, and $L=\mathcal{O}_{\mathbb{P}^n}$ has rank $1$, we have

$$\det(\mathcal{O}_{\mathbb{P}^n}(-1)^{\oplus(n+1)})\cong \det(\Omega_{\mathbb{P}^n}^1)\otimes \det(\mathcal{O}_{\mathbb{P}^n})$$

On the right-hand side, $\det(\mathcal{O}_{\mathbb{P}^n})\cong \mathcal{O}_{\mathbb{P}^n}$, and the left-hand side is $\mathcal{O}_{\mathbb{P}^n}(-1)^{\otimes(n+1)}\cong \mathcal{O}_{\mathbb{P}^n}(-n-1)$, so we obtain

$$\omega_{\mathbb{P}^n}=\det(\Omega_{\mathbb{P}^n}^1)\cong \mathcal{O}_{\mathbb{P}^n}(-n-1)$$

At this point, the canonical divisor is given by $K_{\mathbb{P}^n}=-(n+1)H$. From this computation and [§Line Bundles and Vector Bundles, ⁋Example 16](/en/math/algebraic_varieties/line_bundles#ex16), we know that $\omega_{\mathbb{P}^n}$ has no regular sections.

::: Example 8
We can also verify the above computation from the perspective of transition functions of $n$-forms. On the standard open cover $U_i = \{\x_i \neq 0\}$ of $\mathbb{P}^n$, setting affine coordinates $\y_j^{(i)} = \x_j / \x_i$ ($j \neq i$), we can consider the $n$-form on $U_i$

$$\dd{\y_0}^{(i)} \wedge \cdots \wedge \widehat{\dd{\y_i}^{(i)}} \wedge \cdots \wedge \dd{\y_n}^{(i)}$$

On $U_i \cap U_j$, since $\y_k^{(j)} = \x_k / \x_j = (\x_k / \x_i) / (\x_j / \x_i) = \y_k^{(i)} / \y_j^{(i)}$, writing $t = \y_j^{(i)}$ for convenience, for $k \neq i, j$ we have

$$\dd{\y_k}^{(j)} = \dd{(\y_k^{(i)} / t)} = \frac{t \dd{\y_k}^{(i)} - \y_k^{(i)}  \dd{t}}{t^2}$$

On the other hand, the case $k=i$ is not included in the above computation, and in this case $\y_i^{(j)} = \x_i / \x_j = 1/t$, so

$$\dd{\y_i}^{(j)} = -t^{-2}\dd{t}$$

Now computing the $n$-form $\bigwedge_{k \neq j} \dd{\y_k}^{(j)}$ on $U_j$, since this exterior product contains the factor with $k=i$ and this is a multiple of $\dd{t}$, the terms with $\dd{t}$ in the remaining factors all cancel, leaving only $t^{-1}\dd{\y_k}^{(i)}$. Thus from the $n-1$ factors with $k \neq i, j$ we get $t^{-(n-1)}$, and from the factor with $k=i$ we get $-t^{-2}\dd{t} = -t^{-2}\dd{\y_j}^{(i)}$, and rearranging these, the $n$-form on $U_j$ transforms on $U_i \cap U_j$ as

$$\bigwedge_{k \neq j} \dd{\y_k}^{(j)} = (-1)^{i+j}(\y_j^{(i)})^{-(n+1)} \cdot \bigwedge_{k \neq i} \dd{\y_k}^{(i)}$$

Here $(-1)^{i+j}$ is the sign arising from gathering the sign of the factor with $k=i$ and rearranging the factors in order, and this can be absorbed by multiplying the $n$-form on each $U_i$ by $(-1)^i$, so it is safe to ignore.

Then the $n$-forms on $U_i$ have the frame $\alpha_i = \bigwedge_{k \neq i} \dd{\y_k}^{(i)}$, and the above computation says that the relation between the two frames is $\alpha_j = c_{ij}\alpha_i$ with $c_{ij} = (\y_j^{(i)})^{-(n+1)} = (\x_j / \x_i)^{-(n+1)}$. Now writing a section as $s = f_i\alpha_i = f_j\alpha_j$, we have $f_i = c_{ij}f_j$, so by the convention of [§Line Bundles and Vector Bundles, ⁋Example 12](/en/math/algebraic_varieties/line_bundles#ex12), the transition function between the trivialized functions is its inverse $g_{ij} = c_{ij}^{-1} = (\x_i / \x_j)^{-(n+1)}$. This matches the transition function of $\mathcal{O}_{\mathbb{P}^n}(-n-1)$.
:::

## Adjunction Formula

In many cases, we are interested in varieties obtained from $\mathbb{P}^n$ through sufficiently many polynomials. Intuitively, this is obtained by successively considering smooth divisors $D$ of a smooth variety $X$. The following *adjunction formula* tells us how to compute the canonical line bundle of $D$ from that of $X$ in such cases.

For this, recall for a smooth variety $X$ and a smooth divisor $D$ the ideal sheaf $\mathcal{I}_D=\mathcal{O}_X(-D)$ satisfying the short exact sequence

$$0\rightarrow \mathcal{I}_D\rightarrow \mathcal{O}_X\rightarrow \mathcal{O}_D\rightarrow 0$$

([§Line Bundles and Vector Bundles, ⁋Definition 17](/en/math/algebraic_varieties/line_bundles#def17)) Then from this we can compute that the first-order approximation of $\mathcal{I}_D$ is given by

$$\mathcal{I}_D/\mathcal{I}_D^2=\mathcal{I}_D\otimes_{\mathcal{O}_X}\mathcal{O}_D=\mathcal{O}_X(-D)\vert_D$$

On the other hand, let us compute the tangent sheaves $\mathcal{T}_X=\Der(\mathcal{O}_X)$ and $\mathcal{T}_D=\Der(\mathcal{O}_D)$ of $X$ and $D$ respectively. Then there exists a natural inclusion $\mathcal{T}_D\rightarrow \mathcal{T}_X\vert_D$, and we define its cokernel as the *normal sheaf* $\mathcal{N}_{D/X}$. That is, there exists the following short exact sequence

$$0\rightarrow \mathcal{T}_D\rightarrow \mathcal{T}_X\vert_D\rightarrow \mathcal{N}_{D/X}\rightarrow 0$$

Then we can verify that the dual of this normal bundle $\mathcal{N}_{D/X}$ is precisely $\mathcal{I}_D/\mathcal{I}_D^2$. For this reason we call this the *conormal sheaf*, and concretely this is obtained by verifying the dual of the above short exact sequence,

$$0 \rightarrow \mathcal{I}_D/\mathcal{I}_D^2\rightarrow \Omega_X^1\vert_D\rightarrow \Omega_D^1\rightarrow 0$$

where the first arrow is given by $f\mapsto \dd{f}$. Taking the top exterior power of this short exact sequence yields the following.

::: Proposition 9
(Adjunction Formula) For a smooth divisor $D$ of a smooth variety $X$,

$$\omega_D \cong (\omega_X \otimes \mathcal{O}_X(D))\vert_D$$

holds.
:::

From this, the claim for the canonical divisor also follows immediately. In any case, the content of this proposition is that restricting the canonical bundle $\omega_X$ of the ambient variety $X$, twisted by the line bundle $\mathcal{O}_X(D)$, to $D$ yields the canonical bundle $\omega_D$ of the subvariety $D$. In simple terms, differential forms on $D$ are obtained by adding normal direction information to the differential forms of the ambient space.

The following example shows a concrete computation using this.

::: Example 10
Let $C \subseteq \mathbb{P}^2$ be a smooth curve of degree $d$. By the adjunction formula,

$$\omega_C \cong \omega_{\mathbb{P}^2}\vert_C \otimes \mathcal{O}_{\mathbb{P}^2}(C)\vert_C \cong \mathcal{O}_{\mathbb{P}^2}(-3)\vert_C \otimes \mathcal{O}_{\mathbb{P}^2}(d)\vert_C \cong \mathcal{O}_C(d-3)$$

Thus $K_C \sim (d-3)H\vert_C$, and since the degree of $H\vert_C$ is $d$, we have $\deg K_C = d(d-3)$.

On the other hand, in classical algebraic geometry it is well known that the genus of a plane curve (that is, a projective curve in $\mathbb{P}^2$) is given from its degree by

$$g=\frac{(d-1)(d-2)}{2}$$

([Degree-genus formula](https://en.wikipedia.org/wiki/Genus%E2%80%93degree_formula)) From this we can verify that

$$\deg K_C=d(d-3)=(d-1)(d-2)-2=2g-2$$

holds.
:::

The degree-genus formula is in fact a special case of the Riemann-Roch theorem, which we will examine later, and in that post we will derive both the result $\deg K_C=2g-2$ of the above computation and the degree-genus formula.

## Canonical Divisor of a Blow-up

In [§Rational Maps, ⁋Example 12](/en/math/algebraic_varieties/rational_maps#ex12), we examined the blow-up of $\mathbb{A}^2$ at a point $0$. We now generalize this example further and examine how the canonical divisor behaves in this general setting.

For a smooth variety $X$ and a smooth subvariety $Z$ of codimension $r$, the blow-up of $X$ along $Z$ is given by the birational morphism

$$\pi:\widetilde{X}\rightarrow X$$

where $\pi$ is an isomorphism away from the fiber over $Z$, and the fiber over $Z$ is the *exceptional divisor*

$$E=\mathbb{P}(\mathcal{N}_{Z/X})$$

Here $\mathcal{N}_{Z/X}$ is the normal bundle of $Z$ in $X$, and $\mathbb{P}(\mathcal{N}_{Z/X})$ means the projective bundle obtained by projectivizing the vector space corresponding to the fiber at each point of $Z$. This is the analogue of what we did in [§Rational Maps, ⁋Example 12](/en/math/algebraic_varieties/rational_maps#ex12), where the exceptional divisor corresponding to the fiber over a point $0$ was attached by projectivizing the directions *coming into* this point from outside it.

Now restricting $\pi:\widetilde{X}\rightarrow X$ to $E$, let us consider

$$\pi\vert_E: E\rightarrow Z$$

For notational convenience, we abbreviate this as $\pi_E$. Now thinking of the tangent bundle of $E$, we can divide it into the horizontal direction $(\pi\vert_E)^\ast T_Z$ coming from the base space $Z$ and the relative tangent bundle direction $T_{E/Z}$ perpendicular to it. That is, we obtain the following short exact sequence

$$0 \rightarrow T_{E/Z} \rightarrow T_E \rightarrow \pi_E^\ast T_Z \rightarrow 0\tag{$\ast$}$$

On the other hand, by assumption $Z$ had codimension $r$, so $\mathcal{N}_{Z/X}$ has rank $r$ and thus each fiber of $E$ is $\mathbb{P}^{r-1}$. Generalizing [Proposition 7](#prop7), we obtain the following.

::: Proposition 11 (Relative Euler Sequence)
For any vector bundle $V\rightarrow B$ and projectivized vector bundle $\pi: \mathbb{P}(V)\rightarrow B$, there exists a short exact sequence

$$0\rightarrow \mathcal{O}\rightarrow \pi^\ast V\otimes \mathcal{O}(1)\rightarrow T_{\mathbb{P}(V)/B}\rightarrow 0$$
:::
::: Proof
By definition, each point $[v]\in \mathbb{P}(V)$ is a one-dimensional subspace on a fiber of $V$. Now, just as in $\mathbb{P}^n$, $\mathcal{O}_{\mathbb{P}(V)}(-1)$ is the line bundle collecting these lines, and from this we obtain the tautological exact sequence

$$0\rightarrow \mathcal{O}(-1)\rightarrow \pi^\ast V\rightarrow \mathcal{Q}\rightarrow 0$$

and since tensoring an exact sequence with a line bundle preserves exactness,

$$0 \rightarrow \mathcal{O}\rightarrow \mathcal{O}(1)\otimes \pi^\ast V \rightarrow \mathcal{Q}\otimes\mathcal{O}(1)\rightarrow 0$$

holds. Now examining the part

$$\mathcal{Q}\otimes \mathcal{O}(1)\cong \Hom(\mathcal{O}(-1),\mathcal{Q})$$

we have already seen in the proof of [Proposition 7](#prop7) that viewing how a line in $\mathbb{P}^n$ maps to some quotient is precisely the tangent space, so similarly

$$\Hom(\mathcal{O}(-1),\mathcal{Q})\cong T_{\mathbb{P}(V)/B}$$

is obtained, and from this we obtain the *relative* Euler sequence

$$0\rightarrow \mathcal{O}\rightarrow \pi^\ast V\otimes \mathcal{O}(1)\rightarrow T_{\mathbb{P}(V)/B}\rightarrow 0$$
:::

Thus returning to our situation, we obtain the following exact sequence

$$0\rightarrow \mathcal{O}_E\rightarrow (\pi\vert_E)^\ast \mathcal{N}_{Z/X}\otimes \mathcal{O}_E(1)\rightarrow T_{E/Z}\rightarrow 0\tag{$\ast\ast$}$$

::: Proposition 12 (Canonical Bundle of a Blow-up)
For the blow-up $\pi: \widetilde{X} \rightarrow X$ of a smooth variety $X$ along a smooth subvariety $Z$ of codimension $r$, letting $E$ be the exceptional divisor,

$$K_{\widetilde{X}} = \pi^\ast K_X + (r-1)E$$

holds.
:::

::: Proof
First, by the adjunction formula on $\widetilde{X}$,

$$K_E = (K_{\widetilde{X}} + E)\vert_E$$

Now since $\widetilde{X} \setminus E$ and $X \setminus Z$ are isomorphic, the difference between $K_{\widetilde{X}}$ and $\pi^\ast K_X$ can only occur on $E$. Thus there exists an integer $a$ such that we can write

$$K_{\widetilde{X}} = \pi^\ast K_X + aE$$

and we must show that $a=r-1$.

Restricting the above identity to $E$ gives

$$K_{\widetilde{X}}\vert_E = (\pi^\ast K_X)\vert_E + aE\vert_E$$

Here $(\pi^\ast K_X)\vert_E = \pi_E^\ast(K_X\vert_Z)$, and by the adjunction formula for $Z \subseteq X$,

$$K_X\vert_Z = K_Z \otimes \det(\mathcal{N}_{Z/X})^{-1}$$

so we obtain

$$(\pi^\ast K_X)\vert_E = \pi_E^\ast K_Z \otimes \pi_E^\ast \det(\mathcal{N}_{Z/X})^{-1}$$

Also, since $E\vert_E = \mathcal{O}_E(-1)$,

$$K_{\widetilde{X}}\vert_E = \pi_E^\ast K_Z \otimes \pi_E^\ast \det(\mathcal{N}_{Z/X})^{-1} \otimes \mathcal{O}_E(-a)$$

Therefore,

$$(K_{\widetilde{X}} + E)\vert_E = \pi_E^\ast K_Z \otimes \pi_E^\ast \det(\mathcal{N}_{Z/X})^{-1} \otimes \mathcal{O}_E(-a-1)$$

On the other hand, from ($\ast$) and ($\ast\ast$), taking determinants we obtain the following two identities

$$\det(T_E) = \det(T_{E/Z}) \otimes \pi_E^\ast \det(T_Z),\qquad \det(T_{E/Z}) = \pi_E^\ast \det(\mathcal{N}_{Z/X}) \otimes \mathcal{O}_E(r)$$

From the second identity, we can explicitly obtain the relative canonical bundle as

$$\omega_{E/Z} = \det(T_{E/Z})^{-1} = \pi_E^\ast \det(\mathcal{N}_{Z/X})^{-1} \otimes \mathcal{O}_E(-r)$$

and substituting this back into the first identity, we know that

$$K_E = \det(T_E)^{-1} = \omega_{E/Z} \otimes \pi_E^\ast K_Z = \pi_E^\ast K_Z \otimes \pi_E^\ast \det(\mathcal{N}_{Z/X})^{-1} \otimes \mathcal{O}_E(-r)$$

Comparing these two expressions, we obtain $-a-1 = -r$, that is, $a = r-1$.
:::

Let us examine the following concrete case.

::: Example 13 (Blow-up of $\mathbb{A}^2$ at a Point)
Consider the blow-up of $X = \mathbb{A}^2$ at the origin $Z = \{0\}$. Since $K_{\mathbb{A}^2} = 0$ and the codimension of $Z$ is $r = 2$, by [Proposition 12](#prop12),

$$K_{\widetilde{\mathbb{A}^2}} = E$$

That is, we see that the exceptional divisor $E$ plays the role of the canonical divisor.
:::

---

**References**

**[Hart]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977. (II.8. Differentials; III.7. The Dualizing Sheaf)
