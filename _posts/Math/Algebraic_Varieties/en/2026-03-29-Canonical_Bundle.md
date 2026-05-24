---
title: "Canonical Bundle"
excerpt: "Canonical Bundle and Canonical Divisor"

categories: [Math / Algebraic Varieties]
permalink: /en/math/algebraic_varieties/canonical_bundle
sidebar:
    nav: "algebraic_varieties-en"

header:
    overlay_image: /assets/images/Math/Algebraic_Varieties/Canonical_Bundle.png
    overlay_filter: 0.5

date: 2026-03-29
last_modified_at: 2026-04-22
weight: 11
translated_at: 2026-05-24T09:30:01+00:00
translation_source: kimi-cli
---
In [§Linear Systems](/en/math/algebraic_varieties/linear_systems) we saw that a line bundle can be used to embed a variety into projective space via its (basepoint-free) complete linear system, and if this defines a closed embedding, such a line bundle is called *very ample*.

Despite the fact that line bundles have considerable influence on our geometry, we have not yet properly examined how to define a line bundle on an arbitrary variety in general. If $$X$$ is a *smooth* variety, using [§Line Bundles and Vector Bundles, ⁋Example 24](/en/math/algebraic_varieties/line_bundles#ex24) we can consider the cotangent bundle $$\Omega_X^1$$ defined on it, and by taking its top exterior power we obtain the *canonical bundle* $$\omega_X$$. Our goal in this post is to examine this bundle $$\omega_X$$.

## Vector Bundles and Quasi-Coherent Sheaves

As mentioned above, to define $$\omega_X$$ we start from the cotangent bundle $$\Omega_X^1$$. We have already seen that this is the bundle of differential forms defined on $$X$$. Let us show that this matches the differential in the algebraic setting. ([[Commutative Algebra] §Differentials, ⁋Definition 3](/en/math/commutative_algebra/differentials#def3)) To do this, we need to examine the process of turning a given $$A$$-module $$M$$ into a vector bundle over $$X$$, where $$X$$ is an arbitrary affine variety with coordinate ring $$A$$.

Our basic philosophy is that using [§Affine Varieties, ⁋Proposition 16](/en/math/algebraic_varieties/affine_varieties#prop16), a homomorphism between coordinate *rings* can be transferred to a morphism in the opposite direction between varieties, and thus we can obtain a bundle defined over $$X$$. However, the problem is that $$M$$ is not a ring. That is, multiplication is not defined on $$M$$. But according to [[Multilinear Algebra] §Tensor Algebras, ⁋Definition 5](/en/math/multilinear_algebra/tensor_algebras#def5), we can consider the symmetric algebra $$\S(M)$$ which forcibly defines a (commutative) multiplication on $$M$$.

Yet there is a problem in applying this immediately. Remember that our goal is to view $$M$$ as a vector bundle defined on $$X$$. Roughly speaking, our goal is to attach $$M$$ nicely over each point of $$X$$, but according to [§Affine Varieties, ⁋Proposition 16](/en/math/algebraic_varieties/affine_varieties#prop16), if $$M$$ appears in the world of varieties (as a fiber), the coordinate ring defining it must consist of its coordinate functions. Thus we must use $$M^\vee$$ instead of $$M$$, and therefore we consider $$\S_A(M^\vee)$$ instead of $$\S_A(M)$$. Then this is an $$A$$-algebra, so we obtain the homomorphism $$A\rightarrow \S_A(M^\vee)$$ between coordinate rings, and applying [§Affine Varieties, ⁋Proposition 16](/en/math/algebraic_varieties/affine_varieties#prop16) to this yields a morphism from some variety $$V(M)$$ to $$X$$.

Let us verify that this morphism actually carries a vector bundle structure over $$X$$. A point $$x\in X$$ corresponds to the maximal ideal $$\mathfrak{m}_x$$ of the coordinate ring $$A$$, and therefore the points of the set-theoretic fiber $$V(M)_x = \pi^{-1}(x)$$ over $$x$$ in $$V(M) \to X$$ are the maximal ideals of $$\S_A(M^\vee)$$ containing $$\mathfrak{m}_x\cdot \S_A(M^\vee)$$.

To obtain algebraically the coordinate ring defining this fiber, we must first think about what functions are defined on it. Now, the functions contained in the maximal ideal $$\mathfrak{m}_x$$ defining $$x\in X$$ all vanish at $$x$$, so it is reasonable to think of the functions defined on this fiber as $$A/\mathfrak{m}_x$$-valued functions. We call this field $$\kappa(x)=A/\mathfrak{m}_x$$ the *residue field* at $$x$$, and thus in general $$\kappa(x)$$ is an algebraic extension of $$\mathbb{K}$$. ([[Commutative Algebra] §Nullstellensatz, ⁋Theorem 4](/en/math/commutative_algebra/nullstellensatz#thm4)) Since we usually consider the case where $$\mathbb{K}$$ is an algebraically closed field, we may simply think of $$\kappa(x)$$ as $$\mathbb{K}$$.

From the above discussion, we know that we must consider the collection of $$\kappa(x)$$-valued functions of $$\S_A(M^\vee)$$, namely $$\S_A(M^\vee)\otimes_A\kappa(x)$$. Then from the fact that the symmetric algebra commutes with tensor products, we obtain the formula

$$\S_A(M^\vee)\otimes_A\kappa(x)=\S_{\kappa(x)} (M^\vee\otimes_A\kappa(x))=\S_{\kappa(x)}(M_x^\vee)$$

where the right-hand side has $$M_x = M \otimes_A \kappa(x)$$, and the tensor products appearing here can be thought of as viewing all objects roughly as $$\mathbb{K}$$-vector spaces (more precisely, as $$\kappa(x)$$-vector spaces), just as explained above.

Now $$\S_{\kappa(x)}(M_x^\vee)$$ is a polynomial algebra with coefficients in $$\kappa(x)$$ having the elements of $$M_x^\vee$$ as its linear terms; then the fiber $$V(M)_x$$ consists of points having these elements of $$M_x^\vee$$ as coordinate functions, and thus these points can be thought of as the double dual of $$M_x$$. Now if $$M$$ is a finitely generated $$A$$-module, the canonical isomorphism $$M_x\cong M_x^{\vee\vee}$$ exists, so we can understand each fiber $$V(M)_x$$ as the $$\kappa(x)$$-vector space $$M_x$$.

Through additional calculation we can verify that this data satisfies the locally trivial condition, and thus we can confirm that when a finitely generated $$A$$-module $$M$$ is given, we can view it as a vector bundle defined over $$X$$.

On the other hand, showing that this vector bundle is locally trivial is essentially the same as examining it in the language of sheaves. We have not used the language of sheaves much for geometric intuition, but roughly speaking it works as follows.

Just as above, when an affine variety $$X$$, its coordinate ring $$A$$, and an $$A$$-module $$M$$ are given, the sheaf $$\widetilde{M}$$ defined on $$X$$ is defined by the formula

$$\widetilde{M}(U)=M\otimes_A \mathcal{O}_X(U)$$

This is basically the same context as introducing $$\kappa(x)$$ above, and although we did not compute in detail, in showing the local triviality of $$V(M)$$ one would have performed base change using the structure sheaf in this way. Then in particular for the whole $$X$$,

$$\widetilde{M}(X)=M\otimes_A A=M$$

we have $$\widetilde{M}(X)=M\otimes_A A=M$$, so that $$M$$ becomes the space of global sections of $$\widetilde{M}$$.

These two definitions are merely expressing the same object in different geometric languages. That is, for an affine variety $$X$$ with coordinate ring $$A$$ and a finitely generated $$A$$-module $$M$$, the étale space of $$\widetilde{M}$$ is precisely $$V(M)$$, and the section sheaf of $$V(M)$$ is $$\widetilde{M}$$.

In general, compared to concrete geometric language, the advantage of the sheaf language is that it can be applied in more general situations. For instance, we define the following. ([[Commutative Algebra] §Basic Notions, ⁋Definition 8](/en/math/commutative_algebra/basic_notions#def8))

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> An $$\mathcal{O}_X$$-module $$\mathcal{F}$$ on a general variety $$X$$ is called a *quasi-coherent sheaf* if there exist an affine open cover $$\{U_i\}$$ of $$X$$ and $$A_i=\mathcal{O}_X(U_i)$$-modules $$M_i$$ such that $$\mathcal{F}\vert_{U_i}\cong \widetilde{M_i}$$. If each $$M_i$$ is a finitely generated $$A_i$$-module, we call $$\mathcal{F}$$ a *coherent sheaf*.

</div>

In general, when dealing with quasi-coherent sheaves one must be careful because different $$M$$'s may be attached on each affine cover, but if we restrict to the affine case, the functor $$M\mapsto \widetilde{M}$$ defines a categorical equivalence from $$\lMod{A}$$ to $$\QCoh(X)$$. It suffices to check that for any quasi-coherent sheaf $$\mathcal{F}$$, $$\widetilde{\Gamma(X,\mathcal{F})}$$ recovers $$\mathcal{F}$$ itself. In other words, our slogan is: in the affine case, a quasi-coherent sheaf is an $$A$$-module, and a coherent sheaf is a finite rank $$A$$-module.

From this point of view, a vector bundle can be thought of as a very special case of a (quasi-)coherent sheaf. Or conversely, when thinking about these (quasi-)coherent sheaves, one may regard them as very general forms of vector bundles. Specifically, a coherent sheaf can be thought of as an extension of the category of (finite rank) vector bundles so that it is closed under the operations of an abelian category, namely kernels, images, cokernels, etc.; intuitively, it can be thought of as a vector bundle whose fiber dimension may vary from point to point. A quasi-coherent sheaf is what remains after dropping even the finite rank condition.

However, one somewhat delicate point in the above intuition is that [[Commutative Algebra] §Basic Notions, ⁋Proposition 9](/en/math/commutative_algebra/basic_notions#prop9) does not fit the geometric situation exactly. For example, any coherent sheaf defined on a smooth variety admits a locally free resolution of finite length, but this is not true on a singular variety.

## Canonical Bundle

We are now ready to define the canonical bundle. To do this we must first introduce the cotangent bundle on a variety, and the following definition was already examined in [§Line Bundles and Vector Bundles, ⁋Example 24](/en/math/algebraic_varieties/line_bundles#ex24), but we present it again for completeness.

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> The *cotangent bundle* $$\Omega_X^1$$ of a smooth variety $$X$$ is the dual vector bundle of the tangent bundle $$\mathcal{T}_X$$.

</div>

Then the construction we examined in the previous section is for the following.

<div class="proposition" markdown="1">

<ins id="prop3">**Proposition 3**</ins> For an affine variety $$X$$ with coordinate ring $$A$$, $$\Omega_X^1$$ is the vector bundle corresponding to $$\widetilde{\Omega}_{A/\mathbb{K}}$$. ([[Commutative Algebra] §Differentials, ⁋Definition 3](/en/math/commutative_algebra/differentials#def3))

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

For this it will be convenient to rewrite the previously defined tangent bundle and cotangent bundle in the language of sheaves. First let us define the tangent sheaf $$\mathcal{T}_X$$. For an open subset $$U$$ of $$X$$, the sheaf defined by the collection of $$\mathbb{K}$$-derivations $$\Der_\mathbb{K}(\mathcal{O}_X(U),\mathcal{O}_X(U))$$ on $$\mathcal{O}_X(U)$$ is called the tangent sheaf.

Our main tool is the universal property of Kähler differentials. ([[Commutative Algebra] §Differentials, ⁋Lemma 2](/en/math/commutative_algebra/differentials#lem2)) That is, for any $$A$$-module $$N$$ there is a natural isomorphism

$$\Der_\mathbb{K}(A,N)\cong\Hom_A(\Omega_{A/\mathbb{K}},N)$$

Let us use this. Then by the fact that $$\widetilde{(-)}$$ is a categorical equivalence and the above natural isomorphism,

$$\Hom_{\mathcal{O}_X}(\widetilde{\Omega_{A/\mathbb{K}}},\widetilde{N})\cong\Hom_A(\Omega_{A/\mathbb{K}},N)\cong\Der_\mathbb{K}(A,N)$$

holds. Moreover, if we think of the sheaf of derivations, the last term $$\Der_\mathbb{K}(A,N)$$ becomes $$\Der_\mathbb{K}(\mathcal{O}_X, \widetilde{N})$$, so the formula

$$\Hom_{\mathcal{O}_X}(\widetilde{\Omega_{A/\mathbb{K}}}, \widetilde{N})\cong \Der_\mathbb{K}(\mathcal{O}_X, \widetilde{N})$$

holds. Considering the special case $$N=A$$, i.e. $$\widetilde{N}=\mathcal{O}_X$$,

$$\Hom_{\mathcal{O}_X}(\widetilde{\Omega_{A/\mathbb{K}}}, \mathcal{O}_X)\cong\Der_\mathbb{K}(\mathcal{O}_X, \mathcal{O}_X)\cong \mathcal{T}_X$$

holds. On the other hand, since $$\Omega_{A/\mathbb{K}}$$ is a finitely generated projective $$A$$-module, we know that $$\widetilde{\Omega_{A/\mathbb{K}}^\vee}\cong \widetilde{\Omega_{A/\mathbb{K}}}^\vee$$, and therefore

$$\widetilde{\Omega_{A/\mathbb{K}}}^\vee\cong \widetilde{\Omega_{A/\mathbb{K}}^\vee}\cong \widetilde{\Der_\mathbb{K}(A,A)}\cong \mathcal{T}_X$$

so the desired claim holds.

</details>

This result shows that the cotangent bundle is represented by differential $$1$$-forms, just as we imagine.

<div class="example" markdown="1">

<ins id="ex4">**Example 4**</ins> The cotangent bundle of $$\mathbb{A}^n$$ is $$\Omega_{\mathbb{A}^n}^1 \cong \mathcal{O}_{\mathbb{A}^n}^{\oplus n}$$. Algebraically, if we fix the coordinate ring $$\mathbb{K}[\x_1, \ldots, \x_n]$$ of $$\mathbb{A}^n$$, then the Kähler differentials of this $$\mathbb{K}$$-algebra are the free module $$\bigoplus_{i=1}^n \mathbb{K}[\x_1, \ldots, \x_n]  d\x_i$$, so this result agrees well with our intuition.

</div>

Meanwhile, for any smooth variety $$X$$ of dimension $$n$$ and its cotangent bundle $$\Omega_X^1$$, we know that each fiber of $$\Omega_X^1$$ is $$n$$-dimensional, so taking its $$n$$-fold exterior product yields a line bundle.

<div class="definition" markdown="1">

<ins id="def5">**Definition 5**</ins> The *canonical line bundle* $$\omega_X$$ of a smooth variety $$X$$ of dimension $$n$$ is defined as the top exterior power of the cotangent bundle,

$$\omega_X = \bigwedge\nolimits^{\!n} \Omega_X^1.$$

</div>

We call a global section $$s\in \Gamma(X, \omega_X)$$ of the canonical bundle a *regular $$n$$-form* on $$X$$. These are the $$n$$-forms of the form $$fd\x_1 \wedge \cdots \wedge d\x_n$$ for a regular function $$f$$, when we pick a trivializing open set $$U$$ of $$\omega_X$$ and identify it with the cotangent bundle over affine space as in [Example 4](#ex4).

On the other hand, from the correspondence between line bundles and divisor classes we can define the following.

<div class="definition" markdown="1">

<ins id="def6">**Definition 6**</ins> The divisor class corresponding to the canonical bundle $$\omega_X$$ is called the *canonical divisor* and denoted $$K_X$$. That is, $$\omega_X \cong \mathcal{O}_X(K_X)$$.

</div>

Since we use [§Line Bundles and Vector Bundles, ⁋Proposition 19](/en/math/algebraic_varieties/line_bundles#prop19) for this, note that $$K_X$$ is defined only as a divisor class.

## The Canonical Bundle of $$\mathbb{P}^n$$

As in previous posts, the most familiar example to us is that of $$\mathbb{P}^n$$. Intuitively, if we unpack the quotient

$$\mathbb{P}^n=(\mathbb{A}^{n+1}\setminus\{0\})/\mathbb{K}^\ast$$

defining $$\mathbb{P}^n$$, the $$\mathbb{K}^\ast$$-action is in the radial direction from the origin, that is, the direction defined by the Euler vector field, and from the viewpoint of $$\mathbb{P}^n$$ this is merely a trivial line bundle. Then the tangent space of $$\mathbb{P}^n$$ corresponds to the directions in $$\mathbb{A}^{n+1}$$, i.e. the degree-one forms, modulo this trivial line bundle. In other words, there is a short exact sequence of tangent bundles

$$0 \rightarrow \mathcal{O}_{\mathbb{P}^{n}}\rightarrow \mathcal{O}_{\mathbb{P}^n}(1)^{\oplus (n+1)}\rightarrow T_{\mathbb{P}^n}\rightarrow 0$$

and taking the dual of this yields the following.

<div class="proposition" markdown="1">

<ins id="prop7">**Proposition 7 (Euler Exact Sequence)**</ins> There is an exact sequence of vector bundles on $$\mathbb{P}^n$$

$$0 \rightarrow \Omega_{\mathbb{P}^n}^1 \rightarrow \mathcal{O}_{\mathbb{P}^n}(-1)^{\oplus(n+1)} \rightarrow \mathcal{O}_{\mathbb{P}^n} \rightarrow 0.$$

</div>

To compute the canonical bundle of $$\mathbb{P}^n$$, we must now take the top exterior power of this exact sequence. More generally, given a short exact sequence

$$0\rightarrow E\rightarrow F\rightarrow L\rightarrow 0$$

suppose that $$E$$ has rank $$r$$ and $$L$$ has rank $$1$$. Applying $$\bigwedge\nolimits^{\!r}(-)$$ to this sequence, we know from the fact that the determinant is compatible with tensor products that

$$\det(F)\cong \det(E)\otimes \det(L)$$

Apply this to the Euler exact sequence of [Proposition 7](#prop7). Since $$E=\Omega_{\mathbb{P}^n}^1$$ has rank $$n$$, $$F=\mathcal{O}_{\mathbb{P}^n}(-1)^{\oplus(n+1)}$$ has rank $$n+1$$, and $$L=\mathcal{O}_{\mathbb{P}^n}$$ has rank $$1$$,

$$\det(\mathcal{O}_{\mathbb{P}^n}(-1)^{\oplus(n+1)})\cong \det(\Omega_{\mathbb{P}^n}^1)\otimes \det(\mathcal{O}_{\mathbb{P}^n})$$

The right-hand side has $$\det(\mathcal{O}_{\mathbb{P}^n})\cong \mathcal{O}_{\mathbb{P}^n}$$, and the left-hand side is $$\mathcal{O}_{\mathbb{P}^n}(-1)^{\otimes(n+1)}\cong \mathcal{O}_{\mathbb{P}^n}(-n-1)$$, so

$$\omega_{\mathbb{P}^n}=\det(\Omega_{\mathbb{P}^n}^1)\cong \mathcal{O}_{\mathbb{P}^n}(-n-1)$$

we obtain $$\omega_{\mathbb{P}^n}=\det(\Omega_{\mathbb{P}^n}^1)\cong \mathcal{O}_{\mathbb{P}^n}(-n-1)$$. The canonical divisor is then given by $$K_{\mathbb{P}^n}=-(n+1)H$$. From this computation and [§Line Bundles and Vector Bundles, ⁋Example 16](/en/math/algebraic_varieties/line_bundles#ex16), we see that $$\omega_{\mathbb{P}^n}$$ has no regular sections.

<div class="example" markdown="1">

<ins id="ex8">**Example 8**</ins> The above computation can also be checked from the viewpoint of transition functions of $$n$$-forms. If we set affine coordinates $$\y_j^{(i)} = \x_j / \x_i$$ ($$j \neq i$$) on the standard open cover $$U_i = \{\x_i \neq 0\}$$ of $$\mathbb{P}^n$$, we can consider the $$n$$-form

$$d \y_1^{(i)} \wedge \cdots \wedge \widehat{d \y_i^{(i)}} \wedge \cdots \wedge d \y_n^{(i)}$$

on $$U_i$$. On $$U_i \cap U_j$$ we have $$\y_k^{(j)} = \x_k / \x_j = (\x_k / \x_i) / (\x_j / \x_i) = \y_k^{(i)} / \y_j^{(i)}$$, so for $$k \neq i, j$$

$$d \y_k^{(j)} = d(\y_k^{(i)} / \y_j^{(i)}) = \frac{\y_j^{(i)} d \y_k^{(i)} - \y_k^{(i)}  d \y_j^{(i)}}{(\y_j^{(i)})^2}.$$

Therefore the $$n$$-form on $$U_j$$ transforms on $$U_i \cap U_j$$ as

$$\bigwedge_{k \neq j} d \y_k^{(j)} = (\y_j^{(i)})^{-(n+1)} \cdot \bigwedge_{k \neq i} d \y_k^{(i)}.$$

Since $$(\y_j^{(i)})^{-(n+1)} = (\x_j / \x_i)^{-(n+1)}$$, we can verify that the transition function is $$g_{ij} = (\x_i / \x_j)^{-(n+1)}$$. This coincides with the transition function of $$\mathcal{O}_{\mathbb{P}^n}(-n-1)$$.

</div>

## Adjunction Formula

In many cases we are interested in varieties obtained from $$\mathbb{P}^n$$ by sufficiently many polynomials. Intuitively this is obtained by successively considering smooth divisors $$D$$ of a smooth variety $$X$$. The following *adjunction formula* tells us how to compute the canonical line bundle of $$D$$ from that of $$X$$ in such cases.

For this, recall for a smooth variety $$X$$ and a smooth divisor $$D$$ the short exact sequence

$$0\rightarrow \mathcal{I}_D\rightarrow \mathcal{O}_X\rightarrow \mathcal{O}_D\rightarrow 0$$

satisfying $$\mathcal{I}_D=\mathcal{O}_X(-D)$$. ([§Line Bundles and Vector Bundles, ⁋Definition 17](/en/math/algebraic_varieties/line_bundles#def17)) Then from this we can compute the first-order approximation of $$\mathcal{I}_D$$ as

$$\mathcal{I}_D/\mathcal{I}_D^2=\mathcal{I}_D\otimes_{\mathcal{O}_X}\mathcal{O}_D=\mathcal{O}_X(-D)\vert_D$$

We can compute that this is given by $$\mathcal{I}_D/\mathcal{I}_D^2=\mathcal{I}_D\otimes_{\mathcal{O}_X}\mathcal{O}_D=\mathcal{O}_X(-D)\vert_D$$. On the other hand, let us compute the tangent sheaves $$\mathcal{T}_X=\Der(\mathcal{O}_X)$$ and $$\mathcal{T}_D=\Der(\mathcal{O}_D)$$ of $$X$$ and $$D$$. Then there is a natural inclusion $$\mathcal{T}_D\rightarrow \mathcal{T}_X\vert_D$$, and we define its cokernel as the *normal sheaf* $$\mathcal{N}_{D/X}$$. That is, there is a short exact sequence

$$0\rightarrow \mathcal{T}_D\rightarrow \mathcal{T}_X\vert_D\rightarrow \mathcal{N}_{D/X}\rightarrow 0$$

Then we can verify that the dual of this normal bundle $$\mathcal{N}_{D/X}$$ is precisely $$\mathcal{I}_D/\mathcal{I}_D^2$$. For this reason we call this the *conormal sheaf*; concretely, this is obtained by checking the dual of the above short exact sequence,

$$0 \rightarrow \mathcal{I}_D/\mathcal{I}_D^2\rightarrow \Omega_X^1\lvert D\rightarrow \Omega_D^1\rightarrow 0$$

where the first arrow is given by $$f\mapsto df$$. Taking the top exterior power of this short exact sequence yields the following.

<div class="proposition" markdown="1">

<ins id="prop9">**Proposition 9**</ins> (Adjunction Formula) For a smooth divisor $$D$$ on a smooth variety $$X$$,

$$\omega_D \cong (\omega_X \otimes \mathcal{O}_X(D))\vert_D.$$

</div>

A statement about the canonical divisor also follows immediately from this. At any rate, the claim contained in this proposition is that if we twist the canonical bundle $$\omega_X$$ of the ambient variety $$X$$ by the normal bundle $$\mathcal{O}_X(D)$$ and then restrict to $$D$$, we obtain the canonical bundle $$\omega_D$$ of the subvariety $$D$$. In simple terms, a differential form on $$D$$ is obtained by adding the information of the normal direction to the differential form on the ambient space.

The next example shows a concrete calculation using this.

<div class="example" markdown="1">

<ins id="ex10">**Example 10**</ins> Let $$C \subset \mathbb{P}^2$$ be a smooth curve of degree $$d$$. By the adjunction formula,

$$\omega_C \cong \omega_{\mathbb{P}^2}\vert_C \otimes \mathcal{O}_{\mathbb{P}^2}(C)\vert_C \cong \mathcal{O}_{\mathbb{P}^2}(-3)\vert_C \otimes \mathcal{O}_{\mathbb{P}^2}(d)\vert_C \cong \mathcal{O}_C(d-3).$$

Therefore $$K_C \sim (d-3)H\vert_C$$, and since the degree of $$H\vert_C$$ is $$d$$, we have $$\deg K_C = d(d-3)$$.

Meanwhile, in classical algebraic geometry it is well known that the genus of a plane curve (i.e. a projective curve in $$\mathbb{P}^2$$) is given from its degree by

$$g=\frac{(d-1)(d-2)}{2}.$$

([Degree-genus formula](https://en.wikipedia.org/wiki/Genus%E2%80%93degree_formula)) From this we can verify that

$$\deg K_C=d(d-3)=(d-1)(d-2)-2=2g-2.$$

</div>

The degree-genus formula is in fact a special case of the Riemann–Roch theorem that we will examine later, and in that post we will derive both the result $$\deg K_C=2g-2$$ of the above computation and the degree-genus formula.

## The Canonical Divisor of a Blow-up

We examined the blow-up of $$\mathbb{A}^2$$ at a point $$0$$ in [§Rational Maps, ⁋Example 12](/en/math/algebraic_varieties/rational_maps#ex12). We now generalize this example further and examine how the canonical divisor behaves in this general setting.

For a smooth variety $$X$$ and a smooth subvariety $$Z$$ of codimension $$r$$, the blow-up of $$X$$ along $$Z$$ is given by the birational morphism

$$\pi:\widetilde{X}\rightarrow X;$$

where $$\pi$$ is an isomorphism away from the fiber over $$Z$$, and the fiber over $$Z$$ is the *exceptional divisor*

$$E=\mathbb{P}(\mathcal{N}_{Z/X})$$

Here $$\mathcal{N}_{Z/X}$$ is the normal bundle of $$Z$$ in $$X$$, and $$\mathbb{P}(\mathcal{N}_{Z/X})$$ denotes the projective bundle obtained by projectivizing the vector space corresponding to the fiber at each point of $$Z$$. This is the analogue of the exceptional divisor over the fiber of a point $$0$$ in [§Rational Maps, ⁋Example 12](/en/math/algebraic_varieties/rational_maps#ex12), where we attached the directions <em>coming into</em> this point from outside by projectivizing them.

Then restricting $$\pi:\widetilde{X}\rightarrow X$$ to $$E$$,

$$\pi\vert_E: E\rightarrow Z$$

let us consider $$\pi\vert_E: E\rightarrow Z$$. Now if we think of the tangent bundle of $$E$$, we can split it into the horizontal directions $$(\pi\vert_E)^\ast T_Z$$ coming from the base space $$Z$$ and the relative tangent bundle directions $$T_{E/Z}$$ perpendicular to them. That is, we obtain the short exact sequence

$$0 \to T_{E/Z} \to T_E \to \pi_E^\ast T_Z \to 0\tag{$\ast$}$$

$$0 \to T_{E/Z} \to T_E \to \pi_E^\ast T_Z \to 0\tag{$\ast$}.$$

On the other hand, since $$Z$$ has codimension $$r$$ by assumption, $$\mathcal{N}_{Z/X}$$ has rank $$r$$, and therefore each fiber of $$E$$ is $$\mathbb{P}^{r-1}$$. Generalizing [Proposition 7](#prop7), we obtain the following.

<div class="proposition" markdown="1">

<ins id="prop11">**Proposition 11 (Relative Euler Sequence)**</ins> For any vector bundle $$V\rightarrow B$$ and projectivized vector bundle $$\pi: \mathbb{P}(V)\rightarrow B$$, there is a short exact sequence

$$0\rightarrow \mathcal{O}\rightarrow \pi^\ast V\otimes \mathcal{O}(1)\rightarrow T_{\mathbb{P}(V)/B}\rightarrow 0.$$

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

By definition each point $$[v]\in \mathbb{P}(V)$$ is a one-dimensional subspace on a fiber of $$V$$. Now just as in $$\mathbb{P}^n$$, $$\mathcal{O}_{\mathbb{P}(V)}(-1)$$ is the line bundle collecting these lines, and from this we obtain the tautological exact sequence

$$0\rightarrow \mathcal{O}(-1)\rightarrow \pi^\ast V\rightarrow \mathcal{Q}\rightarrow 0$$

and since tensoring an exact sequence with a line bundle preserves exactness,

$$0 \rightarrow \mathcal{O}\rightarrow \mathcal{O}(1)\otimes \pi^\ast V \rightarrow \mathcal{Q}\otimes\mathcal{O}(1)\rightarrow 0$$

holds. Now looking at the part 

$$\mathcal{Q}\otimes \mathcal{O}(1)\cong \Hom(\mathcal{O}(-1),\mathcal{Q}),$$

since we already saw in the proof of [Proposition 7](#prop7) that seeing which quotient a line in $$\mathbb{P}^n$$ maps to is precisely the tangent space, we also obtain

$$\Hom(\mathcal{O}(-1),\mathcal{Q})\cong T_{\mathbb{P}(V)/B}$$

and from this we obtain the *relative* Euler sequence

$$0\rightarrow \mathcal{O}\rightarrow \pi^\ast V\otimes \mathcal{O}(1)\rightarrow T_{\mathbb{P}(V)/B}\rightarrow 0.$$

</details>

Returning to our situation, we obtain the exact sequence

$$0\rightarrow \mathcal{O}_E\rightarrow (\pi\vert_E)^\ast \mathcal{N}_{Z/X}\otimes \mathcal{O}_E(1)\rightarrow T_{E/Z}\rightarrow 0\tag{$\ast\ast$}$$

$$0\rightarrow \mathcal{O}_E\rightarrow (\pi\vert_E)^\ast \mathcal{N}_{Z/X}\otimes \mathcal{O}_E(1)\rightarrow T_{E/Z}\rightarrow 0\tag{$\ast\ast$}.$$

<div class="proposition" markdown="1">

<ins id="prop12">**Proposition 12 (Canonical Bundle of a Blow-up)**</ins> For the blow-up $$\pi: \widetilde{X} \to X$$ of a smooth variety $$X$$ along a smooth subvariety $$Z$$ of codimension $$r$$, with exceptional divisor $$E$$,

$$K_{\widetilde{X}} = \pi^\ast K_X + (r-1)E.$$

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

First, by the adjunction formula on $$\widetilde{X}$$,

$$K_E = (K_{\widetilde{X}} + E)\vert_E$$

holds. Since $$\widetilde{X} \setminus E$$ and $$X \setminus Z$$ are isomorphic, the difference between $$K_{\widetilde{X}}$$ and $$\pi^\ast K_X$$ can occur only on $$E$$. Thus there exists an integer $$a$$ such that

$$K_{\widetilde{X}} = \pi^\ast K_X + aE$$

we can write $$K_{\widetilde{X}} = \pi^\ast K_X + aE$$, and we must show that $$a=r-1$$.

Restricting the above equation to $$E$$,

$$K_{\widetilde{X}}\vert_E = (\pi^\ast K_X)\vert_E + aE\vert_E$$

we have $$K_{\widetilde{X}}\vert_E = (\pi^\ast K_X)\vert_E + aE\vert_E$$. Here $$(\pi^\ast K_X)\vert_E = \pi_E^\ast(K_X\vert_Z)$$, and by the adjunction formula for $$Z \subset X$$,

$$K_X\vert_Z = K_Z \otimes \det(\mathcal{N}_{Z/X})^{-1}$$

we have

$$(\pi^\ast K_X)\vert_E = \pi_E^\ast K_Z \otimes \pi_E^\ast \det(\mathcal{N}_{Z/X})^{-1}$$

so we obtain $$(\pi^\ast K_X)\vert_E = \pi_E^\ast K_Z \otimes \pi_E^\ast \det(\mathcal{N}_{Z/X})^{-1}$$. Moreover, since $$E\vert_E = \mathcal{O}_E(-1)$$,

$$K_{\widetilde{X}}\vert_E = \pi_E^\ast K_Z \otimes \pi_E^\ast \det(\mathcal{N}_{Z/X})^{-1} \otimes \mathcal{O}_E(-a)$$

we have $$K_{\widetilde{X}}\vert_E = \pi_E^\ast K_Z \otimes \pi_E^\ast \det(\mathcal{N}_{Z/X})^{-1} \otimes \mathcal{O}_E(-a)$$. Therefore

$$(K_{\widetilde{X}} + E)\vert_E = \pi_E^\ast K_Z \otimes \pi_E^\ast \det(\mathcal{N}_{Z/X})^{-1} \otimes \mathcal{O}_E(-a-1)$$

$$(K_{\widetilde{X}} + E)\vert_E = \pi_E^\ast K_Z \otimes \pi_E^\ast \det(\mathcal{N}_{Z/X})^{-1} \otimes \mathcal{O}_E(-a-1).$$

On the other hand, from ($$\ast$$) and ($$\ast\ast$$), taking determinants we obtain the two equations

$$\det(T_E) = \det(T_{E/Z}) \otimes \pi_E^\ast \det(T_Z),\qquad \det(T_{E/Z}) = \pi_E^\ast \det(\mathcal{N}_{Z/X}) \otimes \mathcal{O}_E(r)$$

From the second equation we explicitly obtain the relative canonical bundle

$$\omega_{E/Z} = \det(T_{E/Z})^{-1} = \pi_E^\ast \det(\mathcal{N}_{Z/X})^{-1} \otimes \mathcal{O}_E(-r)$$

as $$\omega_{E/Z} = \det(T_{E/Z})^{-1} = \pi_E^\ast \det(\mathcal{N}_{Z/X})^{-1} \otimes \mathcal{O}_E(-r)$$, and substituting this back into the first equation gives

$$K_E = \det(T_E)^{-1} = \omega_{E/Z} \otimes \pi_E^\ast K_Z = \pi_E^\ast K_Z \otimes \pi_E^\ast \det(\mathcal{N}_{Z/X})^{-1} \otimes \mathcal{O}_E(-r)$$

$$K_E = \det(T_E)^{-1} = \omega_{E/Z} \otimes \pi_E^\ast K_Z = \pi_E^\ast K_Z \otimes \pi_E^\ast \det(\mathcal{N}_{Z/X})^{-1} \otimes \mathcal{O}_E(-r).$$ Comparing these two expressions, we obtain $$-a-1 = -r$$, i.e. $$a = r-1$$.

</details>

Let us look at a concrete example.

<div class="example" markdown="1">

<ins id="ex13">**Example 13 (Blow-up of $$\mathbb{A}^2$$ at a Point)**</ins> Consider the blow-up of $$X = \mathbb{A}^2$$ at the origin $$Z = \{0\}$$. Since $$K_{\mathbb{A}^2} = 0$$ and the codimension of $$Z$$ is $$r = 2$$, by [Proposition 12](#prop12) we have

$$K_{\widetilde{\mathbb{A}^2}} = E.$$

Since $$K_{\widetilde{\mathbb{A}^2}} = E$$, we see that the exceptional divisor $$E$$ plays the role of the canonical divisor.

</div>

---

**References**

**[Har]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977. (II.8. Differentials; III.7. The Dualizing Sheaf)
