---
title: "Smooth and Étale Morphisms"
description: "Smoothness of a morphism of schemes is defined as being finitely presented, flat, and having all geometric fibers regular, and is shown to be equivalent to the cotangent sheaf being locally free of rank equal to the relative dimension. The hard direction passes through the local structure theorem that smooth morphisms are cut out locally by equations whose Jacobian has maximal rank. Unramified morphisms are characterized by the diagonal being an open embedding, and étale morphisms are introduced as smooth unramified morphisms of relative dimension zero, with standard étale models, the Jacobian criterion, and the infinitesimal lifting criterion over square-zero extensions."
excerpt: "Smooth, unramified, and étale morphisms; Jacobian and infinitesimal lifting criteria"

categories: [Math / Scheme Theory]
permalink: /en/math/scheme_theory/smooth_and_etale_morphisms
sidebar: 
    nav: "scheme_theory-en"

date: 2026-08-11
weight: 21
translated_at: 2026-08-28T00:15:05+00:00
translation_source: kimi-cli
last_polished_at: 2026-08-28T00:15:05+00:00
revising: true
---
We have seen that the exact sequences coming from the cotangent sheaf are essentially only *right* exact (the exact sequences following [§Kähler Differentials and Cotangent Sheaves, ⁋Proposition 6](/en/math/scheme_theory/sheaf_of_differentials#prop6)). To prevent this loss of information, we must impose a special condition on the morphism, and this is the motivation for smooth morphisms. The opposite extreme is the case where $\Omega_{X/S}$ vanishes entirely; we call such a morphism *unramified*. Finally, we define *étale* morphisms, which are the smooth unramified morphisms.

Throughout this article, we take as a standing assumption that all morphisms are *locally of finite presentation*. Over a locally Noetherian base (which covers most cases of interest), this coincides with being locally of finite type, so intuitively there is no harm in thinking of it that way.

## Smooth Morphisms

A smooth morphism is a morphism whose fibers form a uniformly regular family over the base. The simplest way to define it would be to require that for each point $s\in S$, the fiber $X_s=X\times_S\Spec\kappa(s)$ has no singular points. In other words, at every point the tangent directions must not exceed the dimension of the fiber; translated into algebraic language at that point, this becomes the condition that equality hold in the inequality $\dim A\leq \dim_{A/\mathfrak{m}}\mathfrak{m}/\mathfrak{m}^2$ for a Noetherian local ring $(A, \mathfrak{m})$, i.e. that $A$ be a regular local ring. ([\[Commutative Algebra\] §Krull Dimension, ⁋Definition 12](/en/math/commutative_algebra/Krull_dimension#def12))

The problem is that for this to be a property of the family, it must behave well under base change, and in general it does not. That is, explicitly requiring regularity at each point of the fiber $X_s$ as above is fragile under base change, and it is known that one should instead consider the *geometric fiber* $X\times_S\Spec\overline{\kappa(s)}$, obtained by extending coefficients to the algebraic closure $\overline{\kappa(s)}$ of the field $\kappa(s)$. However, the proof of this fact is not particularly elementary, so we will use it only as motivation and introduce the following definition directly.

::: Definition 1
A scheme morphism $\varphi:X \rightarrow S$, locally of finite presentation, is *smooth* if the following two conditions hold.

1. $\varphi$ is flat. ([§Flat Morphisms, ⁋Definition 1](/en/math/scheme_theory/flat_morphisms#def1))
2. For every $s\in S$, with the algebraic closure $\overline{\kappa(s)}$ of the residue field $\kappa(s)$ and the canonical morphism $\overline{s}:\Spec\overline{\kappa(s)} \rightarrow S$ it induces, the geometric fiber

   $$X_{\overline{s}}=X\times_S\Spec\overline{\kappa(s)}$$

   is a *regular scheme*. That is, all of its local rings are regular local rings. ([\[Commutative Algebra\] §Krull Dimension, ⁋Definition 12](/en/math/commutative_algebra/Krull_dimension#def12))
:::

In the definition above, the two conditions control different directions: flatness guarantees that the fibers vary continuously along the base without jumps in dimension ([§Flat Morphisms, ⁋Proposition 17](/en/math/scheme_theory/flat_morphisms#prop17)), while the regularity of the geometric fibers guarantees that each fiber itself has no singular points.

The canonical morphism in the definition is given by the composite

$$\Spec \overline{\kappa(s)}\rightarrow \Spec \kappa(s)\rightarrow S$$

so the condition above is stronger than a condition on $X_s$ itself. Concretely, $X_{\overline{s}} \rightarrow X_s$ is the projection obtained from the cartesian square

{% diagram Math/Scheme_Theory/Smooth_and_Etale_Morphisms-1.svg width="12.38em" alt="base change" %}

by base changing $X_s$ along $\Spec\overline{\kappa(s)} \rightarrow \Spec\kappa(s)$, and the fiber of this morphism over $x\in X_s$ is

$$\Spec\kappa(x)\times_{\Spec \kappa(s)}\Spec \overline{\kappa(s)}=\Spec\bigl(\kappa(x)\otimes_{\kappa(s)}\overline{\kappa(s)}\bigr)$$

and since both $\kappa(x)$ and $\overline{\kappa(s)}$ are nonzero vector spaces over $\kappa(s)$, their tensor product is also nonzero, so this fiber is nonempty. Then, since the fiber coincides with the set-theoretic preimage ([§Fiber Products, ⁋Lemma 13](/en/math/scheme_theory/fiber_products#lem13)), $X_{\overline{s}}\rightarrow X_s$ is surjective. In other words, the geometric fiber loses none of the points of $X_s$ and merely enlarges the coefficients, so requiring regularity on it subsumes a requirement at every point of $X_s$.

Meanwhile, smooth morphisms can also be characterized by the local freeness of the cotangent sheaf, and this is the most important characterization of smooth morphisms. To this end, let us first define, for a scheme $Y$ and a point $y\in Y$, the *local dimension* $\dim_yY$ of $Y$ at $y$ as the supremum of the dimensions of the irreducible components containing $y$. Then by definition the total dimension of $Y$ is the supremum of these, and if $Y$ is irreducible then every point lies in the unique irreducible component, so $\dim_yY=\dim Y$ holds. More generally, the same holds for an *equidimensional* scheme, in which all irreducible components have the same dimension. This notion is nothing new; it is merely a language for handling two components of different dimensions in the union of a plane and a line, $Y=V(\x\z,\y\z)\subseteq\mathbb{A}^3_\mathbb{K}$. If $Y$ is of finite type over a field, then at a closed point $z$ we have $\dim\mathcal{O}_{Y,z}=\dim_zY$ by [\[Commutative Algebra\] §Noether Normalization, ⁋Theorem 4](/en/math/commutative_algebra/noether_normalization#thm4).

Among the smoothness conditions, everything except flatness is given on the geometric fiber, so to transfer it to a condition on $X$ we must first check what can be transferred. For the local ring $(\mathcal{O}_{X_{\overline{s}}, \overline{x}}, \mathfrak{m}_{\overline{x}})$ to be regular means, by definition, that the equality

$$\dim_{\kappa(\overline{x})}\mathfrak{m}_{\overline{x}}/\mathfrak{m}_{\overline{x}}^2=\dim \mathcal{O}_{X_{\overline{s}},\overline{x}}\tag{$\ast$}$$

holds. ([\[Commutative Algebra\] §Krull Dimension, ⁋Definition 12](/en/math/commutative_algebra/Krull_dimension#def12)) Meanwhile, immediately after [§Kähler Differentials and Cotangent Sheaves, ⁋Definition 8](/en/math/scheme_theory/sheaf_of_differentials#def8), we saw that for a $\mathbb{K}$-point $\overline{x}$, the $\mathfrak{m}/\mathfrak{m}^2$ on the left-hand side is $\Omega_{X_{\overline{s}}/\mathbb{K}}\otimes\kappa(\overline{x})$, and in our situation $\mathbb{K}=\overline{\kappa(s)}$ is algebraically closed, so every closed point is a $\mathbb{K}$-point and satisfies this premise. Also, we have already seen that the right-hand side equals $\dim_{\overline{x}} X_{\overline{s}}$, so what we want is a statement of the following form.

::: Lemma 2
Let $\varphi:X \rightarrow S$ be a morphism locally of finite presentation, let $x\in X$, $s=\varphi(x)$, put $\mathbb{K}=\overline{\kappa(s)}$, and consider the geometric fiber $X_{\overline{s}}$. Then for any point $\overline{x}\in X_{\overline{s}}$ lying over $x$,

$$\dim_{\kappa(\overline{x})}\bigl(\Omega_{X_{\overline{s}}/\mathbb{K}}\otimes \kappa(\overline{x})\bigr)=\dim_{\kappa(x)}\bigl(\Omega_{X/S}\otimes \kappa(x)\bigr),\qquad \dim_{\overline{x}}X_{\overline{s}}=\dim_xX_s$$

holds.
:::
::: Proof
Since the cotangent sheaf commutes with base change ([§Kähler Differentials and Cotangent Sheaves, ⁋Proposition 5](/en/math/scheme_theory/sheaf_of_differentials#prop5)), in the pullback diagram

{% diagram Math/Scheme_Theory/Smooth_and_Etale_Morphisms-2.svg width="8.18em" alt="pullback" %}

given by the geometric fiber, $\Omega_{X_{\overline{s}}/\mathbb{K}}$ is the pullback $\pi^\ast\Omega_{X/S}$ along $\pi$. Taking the fiber at a point is the pullback along the canonical morphism defined by that point, and the composite of $\overline{x}:\Spec\kappa(\overline{x}) \rightarrow X_{\overline{s}}$ with $\pi$ is the canonical morphism $\Spec\kappa(\overline{x}) \rightarrow \Spec\kappa(x) \rightarrow X$ defined by $x$ and the field extension $\kappa(x)\hookrightarrow \kappa(\overline{x})$, so by the functoriality of pullback,

$$\Omega_{X_{\overline{s}}/\mathbb{K}}\otimes \kappa(\overline{x})=\overline{x}^\ast\pi^\ast\Omega_{X/S}=\bigl(\Omega_{X/S}\otimes \kappa(x)\bigr)\otimes_{\kappa(x)}\kappa(\overline{x})$$

On the other hand, the right-hand side is nothing but the $\kappa(x)$-vector space $\Omega_{X/S}\otimes \kappa(x)$ with scalars extended to $\kappa(\overline{x})$, so the dimensions are equal as well, and this is the first equality.

We prove the second equality. First, since $\Spec\mathbb{K} \rightarrow \Spec\kappa(s)$ given by an algebraic extension is an integral morphism, a property preserved under base change, $X_{\overline{s}} \rightarrow X_s$ is an integral, surjective morphism. Then a component of $X_{\overline{s}}$ containing $\overline{x}$ gives a dominant integral morphism onto the closure of its image, so by [§Dimension, ⁋Proposition 5](/en/math/scheme_theory/dimension#prop5) it has the same dimension as that closure, and since this closure is contained in some component containing $x$, it is clear that $\dim_{\overline{x}}X_{\overline{s}}\leq\dim_xX_s$. For the opposite direction, take a component $W$ of $X_s$ containing $x$ with its reduced structure; then $\overline{x}$ belongs to the base change $W_\mathbb{K}=W\times_{\Spec\kappa(s)}\Spec\mathbb{K}$. Writing $W=\Spec A$, $A$ is a domain and $A\otimes_{\kappa(s)}\mathbb{K}$ is a free $A$-module, so if a minimal prime $\mathfrak{q}$ satisfied $\mathfrak{q}\cap A\neq 0$, then by [\[Commutative Algebra\] §System of Parameters, ⁋Lemma 8](/en/math/commutative_algebra/system_of_parameters#lem8) we could find a prime lying over $0$ inside $\mathfrak{q}$, contradicting minimality. That is, each component of $W_\mathbb{K}$ lies over the generic point of $W$, and this gives a dominant integral morphism, so by [§Dimension, ⁋Proposition 5](/en/math/scheme_theory/dimension#prop5) it has the same dimension as $W$. Meanwhile, a component of $W_\mathbb{K}$ containing $\overline{x}$ is contained in some component of $X_{\overline{s}}$ containing $\overline{x}$, so $\dim_{\overline{x}}X_{\overline{s}}\geq \dim W$, and taking the supremum over all components of $X_s$ containing $x$ yields $\dim_{\overline{x}}X_{\overline{s}}\geq\dim_xX_s$. From this we obtain the desired equality $\dim_{\overline{x}}X_{\overline{s}}=\dim_xX_s$.
:::

From this, under the same hypotheses, the equality ($\ast$) can be understood as the condition

$$\dim_{\kappa(x)}\bigl(\Omega_{X/S}\otimes \kappa(x)\bigr)=\dim_xX_s$$

on the point $x$ of $X$. Here, if $\Omega_{X/S}$ is locally free, the fiber dimension above equals the rank, so this condition can be rephrased as saying that the rank coincides with the local dimension of the fiber. Through this lemma, smoothness can be read off from the local freeness of the cotangent sheaf.

::: Proposition 3
Suppose a morphism $\varphi:X \rightarrow S$, locally of finite presentation, is flat, $\Omega_{X/S}$ is a locally free sheaf, and at each $x\in X$ its rank equals the local dimension $\dim_xX_s$ of the fiber over $s=\varphi(x)$. Then $\varphi$ is smooth.
:::
::: Proof
Since $\varphi$ is flat, it suffices to show that for each $s\in S$ the geometric fiber $X_{\overline{s}}$ is regular. Put $\mathbb{K}=\overline{\kappa(s)}$.

First we verify the given claim at a closed point $z$ of $X_{\overline{s}}$. Since $X_{\overline{s}}$ is locally of finite presentation over the algebraically closed field $\mathbb{K}$ ([§Fiber Products, ⁋Proposition 16](/en/math/scheme_theory/fiber_products#prop16)), we can choose an affine open subset $\Spec\bigl(\mathbb{K}[\x_1,\ldots, \x_n]/\mathfrak{a}\bigr)$ containing $z$, and since the ideal corresponding to $z$ is maximal, by [\[Commutative Algebra\] §The Nullstellensatz, ⁋Lemma 5](/en/math/commutative_algebra/nullstellensatz#lem5) it is the image of $(\x_1-a_1,\ldots, \x_n-a_n)$ for some $a\in \mathbb{K}^n$, and hence $\kappa(z)=\mathbb{K}$. That is, $z$ is a $\mathbb{K}$-point, and immediately after [§Kähler Differentials and Cotangent Sheaves, ⁋Definition 8](/en/math/scheme_theory/sheaf_of_differentials#def8) we verified that for such a point,

$$\Omega_{X_{\overline{s}}/\mathbb{K}}\otimes\kappa(z)\cong\mathfrak{m}_z/\mathfrak{m}_z^2$$

holds.

Now let $x$ be the image of $z$ in $X_s$. Since $\Omega_{X/S}$ is locally free, its fiber dimension at $x$ equals its rank, and by assumption this value in turn equals $\dim_x X_s$, so [Lemma 2](#lem2) gives that the dimension of the left-hand side also equals this value, and hence $\dim_xX_s=\dim_zX_{\overline{s}}$. Meanwhile, since $z$ is a closed point, $\dim_zX_{\overline{s}}=\dim\mathcal{O}_{X_{\overline{s}},z}$, and therefore we obtain

$$\dim_{\kappa(z)}\mathfrak{m}_z/\mathfrak{m}_z^2=\dim \mathcal{O}_{X_{\overline{s}},z}$$

To be a regular local ring, it must be a Noetherian local ring whose maximal ideal is generated by $\dim$ many elements ([\[Commutative Algebra\] §Krull Dimension, ⁋Definition 12](/en/math/commutative_algebra/Krull_dimension#def12)), and by [\[Commutative Algebra\] §Integral Extensions, ⁋Lemma 8](/en/math/commutative_algebra/integral_extension#lem8) this is equivalent to the equality above, so $\mathcal{O}_{X_{\overline{s}},z}$ is a regular local ring.

Now for an arbitrary point $\overline{x}\in X_{\overline{s}}$, choose a closed point $z$ inside $\cl(\overline{x})$ (by [§Dimension, ⁋Proposition 11](/en/math/scheme_theory/dimension#prop11), a nonempty locally closed subset always contains a closed point); then every open neighborhood of $z$ contains $\overline{x}$, so $\mathcal{O}_{X_{\overline{s}},\overline{x}}$ is a localization of $\mathcal{O}_{X_{\overline{s}},z}$. Since a localization of a regular local ring is regular ([\[Commutative Algebra\] §Homological Criterion for Regularity, ⁋Corollary 4](/en/math/commutative_algebra/homological_criterion_for_regularity#cor4)), $\mathcal{O}_{X_{\overline{s}},\overline{x}}$ is also a regular local ring, and hence $X_{\overline{s}}$ is a regular scheme.
:::

Under the conditions of [Proposition 3](#prop3), the rank of $\Omega_{X/S}$ is called the *relative dimension* of $\varphi$. Intuitively, what it measures is the dimension of the tangent space of $\varphi$ in the fiber direction. That is, since the fiber of the relative tangent bundle $\Omega_{X/S}^\vee$ at $x$ is precisely the Zariski tangent space of $X_s$ at $x$ ([§Kähler Differentials and Cotangent Sheaves, ⁋Definition 8](/en/math/scheme_theory/sheaf_of_differentials#def8)), saying that the relative dimension is $r$ means that this tangent space is $r$-dimensional at each point.

Now, for any scheme morphism $\varphi: X \rightarrow S$ locally of finite presentation, we know that locally it can be rewritten in the form

$$\Spec\bigl(A[\x_1,\ldots, \x_n]/(f_1,\ldots, f_r)\bigr)\rightarrow \Spec A$$

The next theorem shows that in such a situation, if the rank of the Jacobian matrix at $x\in X$ matches the number $r$ of equations defining $X$, then $\varphi$ is a smooth morphism of relative dimension $n-r$ on some neighborhood of $x$.

::: Theorem 4 (Jacobian criterion)
Over $S=\Spec A$, let

$$X=\Spec\bigl(A[\x_1,\ldots, \x_n]/(f_1,\ldots, f_r)\bigr)$$

and let $x\in X$ be a point. If at $x$ the Jacobian matrix

$$J=\Bigl(\frac{\partial f_i}{\partial \x_j}\Bigr)_{\substack{1\leq i\leq r\\ 1\leq j\leq n}}$$

has rank $r$ over $\kappa(x)$, then $\varphi:X \rightarrow S$ is a smooth morphism of relative dimension $n-r$ on some open neighborhood of $x$.
:::
::: Proof
By [Proposition 3](#prop3), what we must show is that on some neighborhood of $x$, $\varphi$ is flat, $\Omega_{X/S}$ is a locally free sheaf of rank $n-r$, and at each point of that neighborhood the fiber has local dimension $n-r$. First we factor $\varphi$ as in the following diagram:

{% diagram Math/Scheme_Theory/Smooth_and_Etale_Morphisms-3.svg width="5.94em" alt="factorization" %}

Here $\mathbb{A}_S^n \rightarrow S$ is the canonical structure map, and the horizontal $X\hookrightarrow \mathbb{A}_S^n$ is the closed embedding placing $X$ as the closed subscheme defined by $(f_1,\ldots, f_r)$. Now setting

$$B=A[\x_1,\ldots, \x_n],\qquad \mathfrak{a}=(f_1,\ldots, f_r), \qquad C=B/\mathfrak{a}$$

we have $\mathbb{A}^n_S=\Spec B$ and $X=\Spec C$. Then by [§Kähler Differentials and Cotangent Sheaves, ⁋Proposition 2](/en/math/scheme_theory/sheaf_of_differentials#prop2) there is an exact sequence

$$\mathfrak{a}/\mathfrak{a}^2 \overset{\bar{d}}{\longrightarrow} \Omega_{B/A}\otimes_BC \longrightarrow \Omega_{C/A} \longrightarrow 0$$

and here, by [§Kähler Differentials and Cotangent Sheaves, ⁋Proposition 9](/en/math/scheme_theory/sheaf_of_differentials#prop9), $\Omega_{B/A}$ is a free $B$-module of rank $n$ with basis $\dd{\x_1},\ldots, \dd{\x_n}$, so $\Omega_{B/A}\otimes_BC$ is a free $C$-module of rank $n$ with these as a basis. Under this canonical basis, $\bar{d}$ can be written as

$$\bar{d}: \mathfrak{a}/ \mathfrak{a}^2\rightarrow \Omega_{B/A}\otimes_BC;\qquad f_i+\mathfrak{a}^2\mapsto \dd{f_i}=\sum_j\frac{\partial f_i}{\partial \x_j}\dd{\x_j}$$

Then the Jacobian matrix given in the claim is the transpose of the matrix representing, with respect to the bases $e_i$ and $\dd{\x_j}$, the map obtained by composing $\bar{d}$ with the surjective $C$-module homomorphism

$$\pi: C^{\oplus r} \rightarrow \mathfrak{a}/\mathfrak{a}^2;\qquad e_i\mapsto f_i+\mathfrak{a}^2$$

namely

$$\bar{d}\circ\pi: C^{\oplus r}\rightarrow \mathfrak{a}/\mathfrak{a}^2\rightarrow \Omega_{B/A}\otimes_BC;\qquad e_i\mapsto \sum_j\frac{\partial f_i}{\partial \x_j}\dd{\x_j}$$

and each of its entries is a function on $X$.

Now by hypothesis $J$ has full rank, so there exist indices $j_1,\ldots, j_r$ such that the $r\times r$ minor $\Delta_{j_1,\ldots,j_r}$ formed by those columns is nonzero at $x$. If we let $\pr_{j_1,\ldots,j_r}$ denote the projection from $\Omega_{B/A}\otimes_BC$ onto the subspace generated by these $\dd{\x_{j_k}}$ among its basis elements, then by the matrix representation above, the matrix representing

$$\pr_{j_1,\ldots,j_r}\circ\bar{d}\circ\pi: C^{\oplus r}\rightarrow\mathfrak{a}/\mathfrak{a}^2\rightarrow \Omega_{B/A}\otimes_BC\rightarrow C^{\oplus r}$$

with respect to the $e_i$ is given as the transpose of the $r\times r$ matrix defining $\Delta_{j_1,\ldots,j_r}$. Hence, adjoining the inverse of this minor $\Delta=\Delta_{j_1,\ldots,j_r}$, the map

$$(\pr_{j_1,\ldots,j_r}\circ\bar{d}\circ\pi)_\Delta: C_\Delta^{\oplus r}\rightarrow C_\Delta^{\oplus r}$$

becomes an automorphism ([\[Multilinear Algebra\] §Determinants, ⁋Corollary 3](/en/math/multilinear_algebra/determinants#cor3)). Therefore $\pi_\Delta$ must be an injective $C_\Delta$-module homomorphism; since $\pi$ was already a surjection, $\pi_\Delta$ is a $C_\Delta$-module isomorphism, and from this we know that $(\mathfrak{a}/\mathfrak{a}^2)_\Delta$ is a free $C_\Delta$-module of rank $r$. Meanwhile,

$$\bigl((\pr_{j_1,\ldots,j_r}\circ\bar{d}\circ\pi)_\Delta^{-1}\circ \pr_{j_1,\ldots, j_r}\bigr)\circ(\bar{d}\circ\pi)_\Delta=\id_{C_\Delta^{\oplus r}}$$

so composing with $\pi_\Delta$ and $\pi_\Delta^{-1}$ before and after, we get

$$\left(\pi_\Delta\circ (\pr_{j_1,\ldots,j_r}\circ\bar{d}\circ\pi)_\Delta^{-1}\circ \pr_{j_1,\ldots, j_r}\right)\circ\bar{d}_\Delta=\id_{(\mathfrak{a}/\mathfrak{a}^2)_\Delta}$$

which shows that $\bar{d}_\Delta$ is a split injection. In general, by [\[Multilinear Algebra\] §Exact Sequences, ⁋Proposition 10](/en/math/multilinear_algebra/exact_sequences#prop10), the cokernel of a split injection $\bar{d}_\Delta$ is given by the kernel of its retraction; here both $\pi_\Delta$ and $(\pr_{j_1,\ldots,j_r}\circ\bar{d}\circ\pi)_\Delta^{-1}$ are isomorphisms, so this is precisely the kernel of $(\pr_{j_1,\ldots,j_r})_\Delta$, that is, the free submodule of rank $n-r$ generated by those $\dd{\x_j}$ with $j\notin\{j_1,\ldots, j_r\}$. Since the tensor product preserves cokernels, this must be exactly $\Omega_{C/A}\otimes_CC_\Delta$, and therefore $\Omega_{C/A}$ is a locally free sheaf of rank $n-r$ on $D(\Delta)=\Spec C_\Delta$.

Now, to apply [Proposition 3](#prop3), we must show that $\varphi$ is flat on some open neighborhood of $x$ and that at each point of that neighborhood the fiber has local dimension $n-r$. We first show the flatness of $\varphi$. For this we must first carry out a reduction to the case where $A$ is Noetherian. This is possible because the information we need is contained not in all of $A$ but in the $\mathbb{Z}$-subalgebra $A_0$ generated inside $A$ by the coefficients of $f_1,\ldots, f_r$. By [\[Commutative Algebra\] §Basic Notions, ⁋Corollary 13](/en/math/commutative_algebra/basic_notions#cor13), $A_0$ is Noetherian, and setting $C_0=A_0[\x_1,\ldots, \x_n]/(f_1,\ldots, f_r)$ we have $C=C_0\otimes_{A_0}A$. By the definition of $A_0$, $J$ can also be regarded as a matrix over $C_0$, and hence so can its minor $\Delta$. If we let $x_0$ be the image of the point $x$ in question in $\Spec C_0$, the corresponding prime ideal is the preimage of the prime ideal corresponding to $x$, so $\Delta$ is still nonzero at $x_0$, and hence $J$ still has full rank $r$ at $x_0$. In other words, we can carry all the conditions of the problem over to $X_0$, $S_0$, and if under this hypothesis we can show the flatness of $\varphi_0: X_0\rightarrow S_0$, then since flatness is preserved under base change we can recover the flatness of $\varphi$.

Accordingly, suppose $A$ was Noetherian from the start. For an arbitrary point $x$ of $X$ and its image $s=\varphi(x)$, regard $x$ as a point of $\mathbb{A}_S^n=\Spec B$, let $\mathfrak{p}$ be the corresponding prime ideal of $B$, and let $\mathfrak{q}$ be the prime ideal of $A$ corresponding to $s$; then by the definition of the structure map, $\mathfrak{q}=\mathfrak{p}\cap A$. Our goal is to apply [\[Commutative Algebra\] §Flatness and Localization, ⁋Corollary 4](/en/math/commutative_algebra/local_criterion_for_flatness#cor4) to the *Noetherian* local ring $(A_\mathfrak{q}, \mathfrak{q}A_\mathfrak{q})$, the local *Noetherian* algebra $(B_\mathfrak{p}, \mathfrak{p}B_\mathfrak{p})$ over it, and $B_\mathfrak{p}$ regarded as a module over itself together with the elements $f_1,\ldots, f_r$ of $\mathfrak{p}B_\mathfrak{p}$. Geometrically, this can be viewed as follows. First, $A_\mathfrak{q}$ is the local ring $\mathcal{O}_{S, s}$ at $s=\varphi(x)$, and likewise $B_\mathfrak{p}$ is the local ring $\mathcal{O}_{\mathbb{A}_S^n, x}$ at $x\in X\subset \mathbb{A}_S^n$, whose maximal ideal $\mathfrak{p}B_\mathfrak{p}$ consists of the functions vanishing at $x$. Meanwhile, $\mathfrak{q}B_\mathfrak{p}$ is the ideal generated by pulling back, along $\varphi$, the functions on $S$ vanishing at $s$, and the quotient $B_\mathfrak{p}/\mathfrak{q}B_\mathfrak{p}$ by it is the local ring at $x$ of the fiber over $s$. In this picture, since $x$ is a point of the zero set $X$ cut out by $f_1,\ldots, f_r$, all the $f_i$ belong to $\mathfrak{p}B_\mathfrak{p}$, and the claim of the corollary is then that if $B_\mathfrak{p}$ is a flat $A_\mathfrak{q}$-module and these $f_i$ form a regular sequence in $B_\mathfrak{p}/\mathfrak{q}B_\mathfrak{p}$, then they form a regular sequence in the original $B_\mathfrak{p}$ as well, and the local ring at $x$ of the zero set they cut out is flat over $A_\mathfrak{q}$.

First, since $B$ is a free $A$-module, it is immediate that $B_\mathfrak{p}$ is a flat $A_\mathfrak{q}$-module. Hence all we must show is that the images of $f_1,\ldots, f_r$ form a regular sequence in $R=B_\mathfrak{p}/\mathfrak{q}B_\mathfrak{p}$. For convenience, let us write $\mathfrak{m}$ for the maximal ideal of $R$.

First, in $B/\mathfrak{q}B=(A/\mathfrak{q})[\x_1,\ldots, \x_n]$ the nonzero elements of $A/\mathfrak{q}$ all lie outside $\mathfrak{p}$, so $R$ is the localization of $\kappa(\mathfrak{q})[\x_1,\ldots, \x_n]$ at the prime ideal induced by $\mathfrak{p}$; since this polynomial ring is a regular ring by [\[Commutative Algebra\] §Homological Criterion for Regularity, ⁋Corollary 6](/en/math/commutative_algebra/homological_criterion_for_regularity#cor6), $R$ is a regular local ring with residue field $\kappa(\mathfrak{p})=\kappa(x)$ ([\[Commutative Algebra\] §Krull Dimension, ⁋Definition 12](/en/math/commutative_algebra/Krull_dimension#def12)). Now letting $\bar{f}_i$ denote the image of $f_i$ in $R$, we have $\bar{f}_i\in\mathfrak{m}$, and since $R$ is a regular local ring, $\mathfrak{m}$ is generated by $\dim R$ elements; by [\[Commutative Algebra\] §Regular Local Rings, ⁋Corollary 3](/en/math/commutative_algebra/regular_local_rings#cor3), we know that such generators give a regular sequence. Therefore we will construct a regular system of parameters containing $\bar{f}_1,\ldots, \bar{f}_r$ and then conclude using the fact that an initial segment of a regular sequence is again a regular sequence.

Now we must produce $\dim R$ generators of $\mathfrak{m}$; for this it suffices instead to find elements generating $\mathfrak{m}/\mathfrak{m}^2$ as a $\kappa(\mathfrak{p})$-vector space ([\[Commutative Algebra\] §Integral Extensions, ⁋Lemma 8](/en/math/commutative_algebra/integral_extension#lem8)). Applying [§Kähler Differentials and Cotangent Sheaves, ⁋Proposition 2](/en/math/scheme_theory/sheaf_of_differentials#prop2) to the $\kappa(\mathfrak{q})$-algebra $R$ and its ideal $\mathfrak{m}$, we obtain the conormal exact sequence

$$\mathfrak{m}/\mathfrak{m}^2\longrightarrow\Omega_{R/\kappa(\mathfrak{q})}\otimes_R\kappa(\mathfrak{p})\longrightarrow \Omega_{\kappa(\mathfrak{p})/\kappa(\mathfrak{q})}\longrightarrow 0$$

whose first morphism is given by $u+\mathfrak{m}^2\mapsto\dd{u}$. Meanwhile, since $R$ is a localization of $\kappa(\mathfrak{q})[\x_1,\ldots, \x_n]$, by [\[Commutative Algebra\] §Differentials, ⁋Proposition 7](/en/math/commutative_algebra/differentials#prop7) and [§Kähler Differentials and Cotangent Sheaves, ⁋Proposition 9](/en/math/scheme_theory/sheaf_of_differentials#prop9), $\Omega_{R/\kappa(\mathfrak{q})}$ is a free $R$-module with basis $\dd{\x_1},\ldots, \dd{\x_n}$; hence, writing $u(\mathfrak{p})$ for the image of $u\in R$ in $\kappa(\mathfrak{p})$, this morphism is the $\kappa(\mathfrak{p})$-linear map

$$\mathfrak{m}/\mathfrak{m}^2 \longrightarrow \kappa(\mathfrak{p})^{\oplus n};\qquad u\mapsto \sum_j\frac{\partial u}{\partial \x_j}(\mathfrak{p})\dd{\x_j}$$

In particular, this map sends the class of $\bar{f}_i$ to the $i$-th row of $J$, and since by the Jacobian hypothesis these images are linearly independent vectors, the classes of the $\bar{f}_i$ are linearly independent as well. Hence completing a basis from these classes to a basis of $\mathfrak{m}/\mathfrak{m}^2$ yields the desired basis of $\mathfrak{m}$, and by the preceding arguments $f_1,\ldots, f_r$ form a regular sequence in $B_\mathfrak{p}$ and the quotient $C_\mathfrak{p}=B_\mathfrak{p}/\mathfrak{a}B_\mathfrak{p}$ is flat over $A_\mathfrak{q}$. That is, $\varphi$ is flat at $x$ ([§Flat Morphisms, ⁋Definition 1](/en/math/scheme_theory/flat_morphisms#def1)), and therefore, by [§Flat Morphisms, ⁋Theorem 20](/en/math/scheme_theory/flat_morphisms#thm20), $\varphi$ is flat on some open neighborhood of $x$.

Letting $U$ be the intersection of this open neighborhood with the $D(\Delta)$ obtained earlier, on it $\varphi$ is flat and $\Omega_{C/A}$ is locally free of rank $n-r$. Therefore, the last piece we must show to apply [Proposition 3](#prop3) is that at each point of $U$ the fiber has local dimension $n-r$. This is obtained by repeating the fiber argument above at other points of $U$. For a point $y$ of $U$ and $s'=\varphi(y)$, let $\eta$ be the generic point of the component of the fiber $X_{s'}$ passing through $y$; then $\Delta$ is invertible also at $\eta$, so $J$ has rank $r$, and by the same argument the classes of $\bar{f}_1,\ldots, \bar{f}_r$ are linearly independent inside $\mathfrak{m}_\eta/\mathfrak{m}_\eta^2$ of the regular local ring $\mathcal{O}_{\mathbb{A}^n_{\kappa(s')},\eta}$. Thus $\dim\mathcal{O}_{\mathbb{A}^n_{\kappa(s')},\eta}$, the codimension of that component, is at least $r$, and since $\eta$ is a minimal prime containing $(\bar{f}_1,\ldots, \bar{f}_r)$, [\[Commutative Algebra\] §Krull Dimension, ⁋Theorem 7](/en/math/commutative_algebra/Krull_dimension#thm7) gives the reverse inequality, so the codimension is exactly $r$; by the dimension formula ([\[Commutative Algebra\] §Noether Normalization, ⁋Theorem 4](/en/math/commutative_algebra/noether_normalization#thm4)) the component has dimension $n-r$. Hence at each point of $U$ the local dimension of the fiber coincides with the rank, and by [Proposition 3](#prop3), $\varphi$ is a smooth morphism of relative dimension $n-r$.
:::

The essential content of this proof is all contained in the diagram

{% diagram Math/Scheme_Theory/Smooth_and_Etale_Morphisms-3.svg width="5.94em" alt="factorization" %}

and counting dimensions along it makes the role of each piece clearer. Namely, we view $X\rightarrow S$ as the closed subscheme of the relative affine space $\mathbb{A}^n_S \rightarrow S$ cut out by the equations $f_1,\ldots, f_r$, where the hypothesis that the Jacobian has rank $r$ guarantees that these $r$ conditions do not overlap with one another. The remaining $n-r$ dimensions are then at once the rank of $\Omega_{X/S}$ (the quotient of the free module of rank $n$ generated by $\dd{\x_1},\ldots, \dd{\x_n}$ by the linearly independent $\dd{f_1},\ldots, \dd{f_r}$) and the dimension of the fiber cut at codimension $r$; the condition required by [Proposition 3](#prop3) is precisely that these two values agree.

The proof also gave, along the way, that $f_1,\ldots, f_r$ form a regular sequence in $\mathcal{O}_{\mathbb{A}^n_S,x}$, which means that $X\hookrightarrow \mathbb{A}^n_S$ is a complete intersection of codimension $r$ near $x$ ([§Complete Intersections, ⁋Definition 1](/en/math/scheme_theory/complete_intersections#def1)). In the next section we will show that an arbitrary smooth morphism is locally written in the form of [Theorem 4](#thm4) ([Theorem 6](#thm6)), from which it follows that a smooth morphism always locally has the shape of such a complete intersection.

## Local Structure of Smooth Morphisms

[Theorem 4](#thm4) gives smoothness when a presentation by equations satisfying the Jacobian condition is given; conversely, we can show that any smooth morphism is always locally of this form. We begin with the following situation, where the base is a field. In this case the smoothness condition is given by the regularity of the geometric fiber alone, so what remains is only to translate that regularity into the rank of a Jacobian.

::: Lemma 5
For a field $\mathbb{K}$, its algebraic closure $\overline{\mathbb{K}}$, and polynomials $g_1,\ldots, g_m\in \mathbb{K}[\x_1,\ldots, \x_n]$, let

$$X=\Spec\bigl(\mathbb{K}[\x_1,\ldots, \x_n]/(g_1,\ldots, g_m)\bigr)$$

and suppose that the base change $X_{\overline{\mathbb{K}}}=X\times_{\Spec\mathbb{K}}\Spec\overline{\mathbb{K}}$ is a regular scheme. Then for any $x\in X$, there exist $c=n-\dim_xX$ indices $i_1,\ldots, i_c$ and $h\in \mathbb{K}[\x_1,\ldots, \x_n]$ such that $x\in D(h)$, such that over $D(h)$ the scheme $X$ coincides with the closed subscheme of $\mathbb{A}^n_\mathbb{K}$ defined by $g_{i_1},\ldots, g_{i_c}$, and such that some $c\times c$ minor $\Delta$ of the Jacobian $(\partial g_{i_k}/\partial \x_j)$ is invertible over $D(h)$.
:::
::: Proof
With notation as in the proof of [Theorem 4](#thm4) above, write $\mathfrak{a}=(g_1,\ldots, g_m)$ and regard $X_{\overline{\mathbb{K}}}$ as the closed subscheme of $\mathbb{A}^n_{\overline{\mathbb{K}}}$ defined by $\mathfrak{a}\overline{\mathbb{K}}[\x_1,\ldots, \x_n]$. From the proof of [Lemma 2](#lem2) we know that $X_{\overline{\mathbb{K}}} \rightarrow X$ is surjective, so for any given $x$ we may choose a point $\overline{x}\in X_{\overline{\mathbb{K}}}$ lying over it.

By assumption the local rings of $X_{\overline{\mathbb{K}}}$ are regular, hence in particular domains ([\[Commutative Algebra\] §Regular Local Rings, ⁋Corollary 1](/en/math/commutative_algebra/regular_local_rings#cor1)); thus each point belongs to a unique irreducible component, and the local dimension equals the dimension of the component containing it. Let $Z$ be the component containing $\overline{x}$ and $d=\dim Z$ its dimension. Considering the closure $\cl(\overline{x})$ of $\overline{x}$ in $X_{\overline{\mathbb{K}}}$, this is a closed subset contained in $Z$, and by the second result of [§Dimension, ⁋Proposition 11](/en/math/scheme_theory/dimension#prop11) it contains a closed point $z$ of $X_{\overline{\mathbb{K}}}$. Then by [\[Commutative Algebra\] §Noether Normalization, ⁋Theorem 4](/en/math/commutative_algebra/noether_normalization#thm4) we have $\dim\mathcal{O}_{X_{\overline{\mathbb{K}}},z}=d$, and since $\overline{\mathbb{K}}$ is algebraically closed, by [\[Commutative Algebra\] §The Nullstellensatz, ⁋Lemma 5](/en/math/commutative_algebra/nullstellensatz#lem5) the maximal ideal corresponding to $z$ is the image of $(\x_1-a_1,\ldots, \x_n-a_n)$ for some $a\in \overline{\mathbb{K}}^n$; in particular $\kappa(z)=\overline{\mathbb{K}}$.

Now let us compute the rank of the Jacobian at $z$. Considering the conormal exact sequence of the closed embedding $X_{\overline{\mathbb{K}}}\hookrightarrow \mathbb{A}^n_{\overline{\mathbb{K}}}$, the middle term is a free module of rank $n$ with basis $\dd{\x_1},\ldots, \dd{\x_n}$, and since the defining ideal is generated by $g_1,\ldots, g_m$, the image of the first morphism $\bar{d}$ is generated by the elements $\dd{g_i}=\sum_j(\partial g_i/\partial \x_j)\dd{\x_j}$. Pulling this sequence down to $\kappa(z)$ yields

$$\Omega_{X_{\overline{\mathbb{K}}}/\overline{\mathbb{K}}}\otimes\kappa(z)\cong\coker\bigl(\kappa(z)^{\oplus m} \longrightarrow \kappa(z)^{\oplus n}\bigr)$$

where the right-hand morphism is the transpose of the Jacobian $J=(\partial g_i/\partial \x_j)$ evaluated at $z$. On the other hand, since $z$ is a $\overline{\mathbb{K}}$-point, the left-hand side is $\mathfrak{m}_z/\mathfrak{m}_z^2$ (immediately after [§Kähler Differentials and Cotangent Sheaves, ⁋Definition 8](/en/math/scheme_theory/sheaf_of_differentials#def8)), and since $\mathcal{O}_{X_{\overline{\mathbb{K}}},z}$ is a regular local ring, its dimension is $\dim\mathcal{O}_{X_{\overline{\mathbb{K}}},z}=d$ ([\[Commutative Algebra\] §Krull Dimension, ⁋Definition 12](/en/math/commutative_algebra/Krull_dimension#def12)). Hence $\rank J(z)=n-d$, and writing this value as $c$, there exists a nonzero $c\times c$ minor $\Delta\in \mathbb{K}[\x_1,\ldots, \x_n]$ of $J(z)$. Let $i_1,\ldots, i_c$ be the indices defining it, and set $f_k=g_{i_k}$. Writing $\mathfrak{a}'=(f_1,\ldots, f_c)$ and setting $X'=\Spec\bigl(\mathbb{K}[\x_1,\ldots, \x_n]/\mathfrak{a}'\bigr)$, we have $\mathfrak{a}'\subseteq \mathfrak{a}$, so $X$ is a closed subscheme of $X'$, and our claim is that this inclusion is an equality near $x$.

We first verify the claim in the local ring at $z$. Let $R=\mathcal{O}_{\mathbb{A}^n_{\overline{\mathbb{K}}},z}$ be the localization of $\overline{\mathbb{K}}[\x_1,\ldots, \x_n]$ at the maximal ideal corresponding to $z$; this is a regular local ring of dimension $n$ with residue field $\overline{\mathbb{K}}$. Since $X_{\overline{\mathbb{K}}}$ and $X'_{\overline{\mathbb{K}}}$ are the closed subschemes cut out inside $\mathbb{A}^n_{\overline{\mathbb{K}}}$ by $\mathfrak{a}$ and $\mathfrak{a}'$ respectively, their local rings at $z$ are the quotients of $R$ by these two ideals:

$$\mathcal{O}_{X_{\overline{\mathbb{K}}},z}=R/\mathfrak{a}R,\qquad R'=\mathcal{O}_{X'_{\overline{\mathbb{K}}},z}=R/\mathfrak{a}'R$$

and what we will show at $z$ is that these two ideals coincide, i.e. $\mathfrak{a}R=\mathfrak{a}'R$. As in the proof of [Theorem 4](#thm4), the condition $\Delta(z)\neq 0$ implies that the classes of $f_1,\ldots, f_c$ are linearly independent in $\mathfrak{m}_R/\mathfrak{m}_R^2$, and hence $\mathfrak{m}_R$ is generated by these together with $n-c$ other elements. Then the maximal ideal of $R'$ is generated by $n-c$ elements, so by [\[Commutative Algebra\] §Krull Dimension, ⁋Theorem 7](/en/math/commutative_algebra/Krull_dimension#thm7) we have $\dim R'\leq n-c=d$. But $\mathcal{O}_{X_{\overline{\mathbb{K}}},z}$ is a quotient of $R'$ and has dimension $d$, so $\dim R'\geq d$, and therefore $\dim R'=d$. That is, the maximal ideal of $R'$ is generated by $\dim R'$ elements, so $R'$ is a regular local ring ([\[Commutative Algebra\] §Krull Dimension, ⁋Definition 12](/en/math/commutative_algebra/Krull_dimension#def12)), and in particular a domain. Now suppose, contrary to the conclusion, that the kernel $\mathfrak{b}=\mathfrak{a}R/\mathfrak{a}'R$ of the surjection $R' \rightarrow \mathcal{O}_{X_{\overline{\mathbb{K}}},z}$ is nonzero. The prime ideals of $R'/\mathfrak{b}$ are the prime ideals of $R'$ containing $\mathfrak{b}$, and every such chain starts at a minimal prime over $\mathfrak{b}$; hence there exists a minimal prime $\mathfrak{p}$ over $\mathfrak{b}$ such that $\dim R'/\mathfrak{b}=\dim R'/\mathfrak{p}$. But $\mathfrak{b}\subseteq\mathfrak{p}$, and $\mathfrak{b}\neq 0$ by assumption, so $\mathfrak{p}\neq 0$. On the other hand, since $R'$ is a domain, $0$ is also a prime ideal of $R'$, and therefore one may prepend $0\subsetneq\mathfrak{p}$ to a chain in $R'/\mathfrak{p}$ of length $\dim R'/\mathfrak{p}$, obtaining $\dim R'\geq \dim R'/\mathfrak{p}+1$. That is, $\dim\mathcal{O}_{X_{\overline{\mathbb{K}}},z}<\dim R'=d$, a contradiction, so we must have $\mathfrak{b}=0$, and the claim at $z$ follows. Meanwhile, $\mathfrak{b}$ is the stalk at $z$ of the ideal sheaf of $X_{\overline{\mathbb{K}}}\subseteq X'_{\overline{\mathbb{K}}}$, and since this sheaf is generated by the images of $g_1,\ldots, g_m$ and is therefore of finite type, from $\mathfrak{b}=0$ we obtain that this sheaf actually vanishes over some open neighborhood of $z$. Since $z\in \cl(\overline{x})$ by construction, this neighborhood contains $\overline{x}$.

Finally we descend to $\mathbb{K}$. Let $\mathcal{J}$ be the ideal sheaf of $X\subseteq X'$; since $\mathbb{K} \rightarrow \overline{\mathbb{K}}$ is flat, the base change of $\mathcal{J}$ to $\overline{\mathbb{K}}$ is the ideal sheaf of $X_{\overline{\mathbb{K}}}\subseteq X'_{\overline{\mathbb{K}}}$, and therefore $\mathcal{J}_x\otimes_{\mathcal{O}_{X',x}}\mathcal{O}_{X'_{\overline{\mathbb{K}}},\overline{x}}=0$. But $\mathcal{O}_{X',x} \rightarrow \mathcal{O}_{X'_{\overline{\mathbb{K}}},\overline{x}}$ is a flat local homomorphism, so by [§Flat Morphisms, ⁋Lemma 15](/en/math/scheme_theory/flat_morphisms#lem15) it sends no nonzero module to zero, i.e. $\mathcal{J}_x=0$. Since $\mathcal{J}$ is also of finite type, it vanishes over some principal open neighborhood of $x$. Meanwhile $D(\Delta)$ is an open set containing $z$, hence contains $\overline{x}$, and since $\kappa(x)\hookrightarrow\kappa(\overline{x})$ we have $\Delta(x)\neq 0$. Then taking $D(h)$ to be the intersection of the previous principal open with $D(\Delta)$, all the desired properties hold. Finally, applying [Lemma 2](#lem2) to $S=\Spec\mathbb{K}$ gives $d=\dim_{\overline{x}}X_{\overline{\mathbb{K}}}=\dim_xX$, so $c=n-\dim_xX$.
:::

When the base is a general scheme, this presentation is obtained over the fiber and then lifted in the direction of the base; the flatness assumption is what is needed in this process.

::: Theorem 6 (Local structure)
For a smooth morphism $\varphi:X \rightarrow S$ and points $x\in X$, $s=\varphi(x)$, there exist an affine open neighborhood $\Spec A$ of $s$ and an open neighborhood of $x$ lying over it which is isomorphic, as an $S$-scheme, to

$$\Spec\Bigl(\bigl(A[\x_1,\ldots, \x_n]/(f_1,\ldots, f_c)\bigr)_g\Bigr)$$

Here some $c\times c$ minor of the Jacobian $(\partial f_i/\partial \x_j)$ is invertible in this ring, and $c=n-\dim_xX_s$.
:::
::: Proof
Since the problem is local, we may assume that $S=\Spec A$ and that $x$ lies in an affine open $\Spec C$. Also, since $\varphi$ is locally of finite presentation, we may write $C=A[\x_1,\ldots, \x_n]/(u_1,\ldots, u_m)$. Let $\mathfrak{a}=(u_1,\ldots, u_m)$ be the ideal in this presentation.

The fiber $X_s$ is the quotient of $\kappa(s)[\x_1,\ldots, \x_n]$ by the images $\overline{u}_i$ of the $u_i$, and since $\varphi$ is smooth, its base change $X_{\overline{s}}$ is regular. We can therefore apply [Lemma 5](#lem5) to $\mathbb{K}=\kappa(s)$ and $\overline{u}_1,\ldots, \overline{u}_m$; as a result, there exist $c=n-\dim_xX_s$ indices $i_1,\ldots, i_c$ such that over some open neighborhood of $x$ the fiber $X_s$ coincides with the closed subscheme defined by $\overline{u}_{i_1},\ldots, \overline{u}_{i_c}$, and such that the $c\times c$ minor given by these indices is invertible over it. As in the construction in [Lemma 5](#lem5), set $f_k=u_{i_k}$ and let $\Delta$ be that minor computed in $A[\x_1,\ldots, \x_n]$. Since the image of $\Delta$ in $\kappa(s)$ is nonzero at $x$, we have $\Delta(x)\neq 0$. Now setting $X'=\Spec\bigl(A[\x_1,\ldots, \x_n]/(f_1,\ldots, f_c)\bigr)$, we have $(f_1,\ldots, f_c)\subseteq \mathfrak{a}$, so $X$ is a closed subscheme of $X'$, and its ideal sheaf $\mathcal{I}$ is generated by the images of $u_1,\ldots, u_m$, hence of finite type. We show that $\mathcal{I}_x=0$.

Consider the exact sequence of $\mathcal{O}_{S,s}$-modules

$$0 \rightarrow \mathcal{I}_x \rightarrow \mathcal{O}_{X',x} \rightarrow \mathcal{O}_{X,x} \rightarrow 0$$

Since $\varphi$ is flat, $\mathcal{O}_{X,x}$ is a flat $\mathcal{O}_{S,s}$-module ([§Flat Morphisms, ⁋Definition 1](/en/math/scheme_theory/flat_morphisms#def1)); in particular $\mathfrak{m}_s\otimes_{\mathcal{O}_{S,s}}\mathcal{O}_{X,x} \rightarrow \mathcal{O}_{X,x}$ is injective, so by [\[Commutative Algebra\] §Flatness, ⁋Proposition 1](/en/math/commutative_algebra/flatness#prop1) we have $\Tor_1^{\mathcal{O}_{S,s}}(\kappa(s), \mathcal{O}_{X,x})=0$. Therefore applying $-\otimes_{\mathcal{O}_{S,s}}\kappa(s)$ to the above sequence is still exact on the left; in particular, $\mathcal{I}_x/\mathfrak{m}_s\mathcal{I}_x$ equals the kernel of $\mathcal{O}_{X'_s,x} \rightarrow \mathcal{O}_{X_s,x}$. But by [Lemma 5](#lem5) we have $X_s=X'_s$ near $x$, so this kernel is zero, and hence $\mathcal{I}_x=\mathfrak{m}_s\mathcal{I}_x$. Now since $\mathfrak{m}_s\mathcal{O}_{X',x}\subseteq\mathfrak{m}_x$ and $\mathcal{I}_x$ is finitely generated, by [\[Commutative Algebra\] §Integral Extensions, ⁋Lemma 8](/en/math/commutative_algebra/integral_extension#lem8) we have $\mathcal{I}_x=0$. Then, since $\mathcal{I}$ is of finite type, $\mathcal{I}$ vanishes over some open neighborhood of $x$; choosing a principal open $D(g_1)$ inside that neighborhood, $X$ and $X'$ coincide over $D(g_1)$. Setting $g=\Delta g_1$ gives the desired presentation.
:::

The converse direction of [Proposition 3](#prop3) now follows, completing the characterization of smooth morphisms via the cotangent sheaf.

::: Theorem 7
For a morphism $\varphi:X \rightarrow S$ locally of finite presentation, the following are equivalent.

1. $\varphi$ is smooth.
2. $\varphi$ is flat, $\Omega_{X/S}$ is a locally free sheaf, and at each $x\in X$ its rank equals the local dimension $\dim_xX_s$ of the fiber over $s=\varphi(x)$.
:::
::: Proof
That the second condition implies the first is [Proposition 3](#prop3).

Conversely, suppose $\varphi$ is smooth. Flatness is already part of [Definition 1](#def1). Fix a point $x\in X$ and $s=\varphi(x)$; by [Theorem 6](#thm6), over some open neighborhood of $x$ the scheme $X$ is a localization of $A[\x_1,\ldots, \x_n]/(f_1,\ldots, f_c)$, some $c\times c$ minor of the Jacobian is invertible over it, and $c=n-\dim_xX_s$. Then the argument in the proof of [Theorem 4](#thm4) that obtained local freeness from the conormal exact sequence applies verbatim, so over that neighborhood $\Omega_{X/S}$ is a locally free sheaf of rank $n-c$. That is, its rank is $\dim_xX_s$.
:::

Meanwhile, what was actually used in the proof of [Theorem 4](#thm4) was the fact that the left morphism of the conormal exact sequence is not merely injective but a split injection. This property is not a coincidence attached to the chosen presentation by equations but is equivalent to smoothness itself.

::: Proposition 8
Suppose we are given a closed embedding $X\hookrightarrow \mathbb{A}^n_S$ over $S=\Spec A$, and let $B=A[\x_1,\ldots, \x_n]$, let $\mathfrak{a}\subseteq B$ be its defining ideal, and set $C=B/\mathfrak{a}$. Then $\varphi:X \rightarrow S$ is smooth if and only if the conormal exact sequence ([§Kähler Differentials and Cotangent Sheaves, ⁋Proposition 2](/en/math/scheme_theory/sheaf_of_differentials#prop2)) is exact and split on the left as well, i.e.

$$0 \longrightarrow \mathfrak{a}/\mathfrak{a}^2 \overset{\bar{d}}{\longrightarrow} \Omega_{B/A}\otimes_BC \longrightarrow \Omega_{C/A} \longrightarrow 0$$

is a split short exact sequence. In this case $\mathfrak{a}/\mathfrak{a}^2$ and $\Omega_{C/A}$ are both finitely generated projective $C$-modules.
:::
::: Proof
First suppose $\varphi$ is smooth. By [Theorem 7](#thm7), $\Omega_{C/A}$ is locally free and finitely presented, hence a projective $C$-module, so the surjection on the right splits. What remains is to show that $\bar{d}$ is injective. For this, first observe that the splitting above gives $\Omega_{B/A}\otimes_BC\cong \Omega_{C/A}\oplus \im\bar{d}$, so $\im\bar{d}$, being a direct summand of a free module, is projective, and hence the surjection $\mathfrak{a}/\mathfrak{a}^2 \rightarrow \im\bar{d}$ also splits, giving

$$\mathfrak{a}/\mathfrak{a}^2\cong\ker\bar{d}\oplus\im\bar{d}$$

Now fix a point $x\in X$ and $s=\varphi(x)$, $d=\dim_xX_s$, and let $\mathfrak{q}\subseteq C$ be the prime corresponding to $x$ and $\mathfrak{p}$ its preimage in $B$. By [Theorem 7](#thm7), the rank of $\Omega_{C/A}$ at $x$ is $d$, so the dimension of $\im\bar{d}\otimes_C\kappa(x)$ is $n-d$; on the other hand, since $\mathfrak{a}\subseteq\mathfrak{p}$ implies $\mathfrak{a}^2\subseteq\mathfrak{p}\mathfrak{a}$, we have $(\mathfrak{a}/\mathfrak{a}^2)\otimes_C\kappa(x)=\mathfrak{a}\otimes_B\kappa(x)$. Thus descending the above decomposition to $\kappa(x)$ yields

$$\dim_{\kappa(x)}\mathfrak{a}\otimes_B\kappa(x)=\dim_{\kappa(x)}\ker\bar{d}\otimes_C\kappa(x)+(n-d)$$

The left-hand side is computed on the fiber. Since $\varphi$ is flat, $C$ is a flat $A$-module, so $\Tor_1^A(C, \kappa(s))=0$, and hence applying $-\otimes_A\kappa(s)$ to $0 \rightarrow \mathfrak{a} \rightarrow B \rightarrow C \rightarrow 0$ remains exact on the left as well. Since $B$ is free over $A$, we have $B\otimes_A\kappa(s)=\kappa(s)[\x_1,\ldots, \x_n]$, which means that $\mathfrak{a}\otimes_A\kappa(s)$ equals the ideal $\overline{\mathfrak{a}}$ defining the fiber $X_s$ inside it. Thus $\mathfrak{a}\otimes_B\kappa(x)=\overline{\mathfrak{a}}\otimes\kappa(x)$, and since $\varphi$ is smooth so that its geometric fibers are regular, by [Lemma 5](#lem5) the ideal $\overline{\mathfrak{a}}$ is generated by $n-d$ elements near $x$. That is, the left-hand side is at most $n-d$, and by the equality above $\ker\bar{d}\otimes_C\kappa(x)=0$. Since $\varphi$ is locally of finite presentation, $\mathfrak{a}$ is finitely generated, so $\ker\bar{d}$ is also finitely generated, and by [\[Commutative Algebra\] §Integral Extensions, ⁋Lemma 8](/en/math/commutative_algebra/integral_extension#lem8) we have $(\ker\bar{d})_\mathfrak{q}=0$. Since $x$ was arbitrary, $\bar{d}$ is injective.

Conversely, suppose the above sequence is split short exact. Then $\mathfrak{a}/\mathfrak{a}^2$ and $\Omega_{C/A}$ are both direct summands of the free module $\Omega_{B/A}\otimes_BC$ of rank $n$, hence finitely generated projective. Let $\mathfrak{q}\subseteq C$ be the prime corresponding to a point $x\in X$ and $\mathfrak{p}\subseteq B$ its preimage, and let $c$ be the rank of the free module $(\mathfrak{a}/\mathfrak{a}^2)_{\mathfrak{q}}$. If we choose its basis to consist of the classes of elements $f_1,\ldots, f_c$ of $\mathfrak{a}$, then $\mathfrak{a}_{\mathfrak{p}}=(f_1,\ldots, f_c)_{\mathfrak{p}}+\mathfrak{a}_{\mathfrak{p}}^2$, and since $\varphi$ is locally of finite presentation, $\mathfrak{a}$ is finitely generated, so by [\[Commutative Algebra\] §Integral Extensions, ⁋Lemma 8](/en/math/commutative_algebra/integral_extension#lem8) we have $\mathfrak{a}_{\mathfrak{p}}=(f_1,\ldots, f_c)_{\mathfrak{p}}$. Then for some $g\notin\mathfrak{p}$ we have $\mathfrak{a}_g=(f_1,\ldots, f_c)_g$, so near $x$ the scheme $X$ coincides with $X'=\Spec\bigl(B/(f_1,\ldots, f_c)\bigr)$ as an open subscheme. On the other hand, a split injection remains injective after any base change, so $\bar{d}\otimes\kappa(x)$ is injective, and the matrix representing it with respect to the bases $\bar{f}_1,\ldots, \bar{f}_c$ and $\dd{\x_1},\ldots, \dd{\x_n}$ is the transpose of the Jacobian $(\partial f_i/\partial \x_j)$ computed at $x$, so its rank is $c$. Therefore, by [Theorem 4](#thm4), $X' \rightarrow S$ is smooth on some neighborhood of $x$, and since $X$ and $X'$ coincide on that neighborhood, $\varphi$ is smooth at $x$. Since $x$ was arbitrary, $\varphi$ is smooth.
:::

Over an affine base one can always choose such a closed embedding, and smoothness is a local property, so the above criterion applies locally to an arbitrary $\varphi$. On the other hand, injectivity of $\bar{d}$ alone does not imply smoothness. For instance, in $C=\mathbb{K}[\x,\y]/(\x\y)$, the ideal $\mathfrak{a}=(\x\y)$ is generated by a nonzerodivisor, so $\mathfrak{a}/\mathfrak{a}^2$ is a free module of rank $1$, and any element killing $\bar{d}(\overline{\x\y})=\y \dd{\x}+\x \dd{\y}$ lies in $(\x)\cap(\y)=0$, so $\bar{d}$ is injective. However, at the origin the descent of $\bar{d}$ to the residue field vanishes, so its image fails to be a direct summand; indeed, $X$ is singular at the origin.

Thus smoothness can fail in two ways: $\bar{d}$ may fail to be injective, or its image may fail to be a direct summand even when it is injective. The former is recorded by $H_1(\operatorname{NL}_{C/A})=\ker\bar{d}$, while the latter appears as the failure of $\Omega_{C/A}$ to be projective. The naive cotangent complex extends $\Omega$ to the left so as to retain both conditions, and the cotangent complex continues this construction through all degrees.

## Unramified Morphisms

In [Theorem 4](#thm4), the condition that the Jacobian has full rank says that the differential of the morphism $\mathbb{A}^n_S \rightarrow \mathbb{A}^r_S$ defined by $f_1,\ldots, f_r$ is surjective in the fiber direction; recalling that in [\[Manifolds\] §Implicit Function Theorem, ⁋Corollary 4](/en/math/manifolds/implicit_function_theorem#cor4), whenever the level set of a function consists of such points it forms an embedded submanifold of codimension $r$, one can think of [Theorem 4](#thm4) as parametrizing this fact in the base direction. Thus, intuitively, a smooth morphism can be thought of as the algebraic counterpart of a submersion. Similarly, one can consider the algebraic counterpart of an immersion, which is called an *unramified morphism*. In differential geometry an immersion is a smooth map whose differential is injective, and in algebraic language this translates into the condition that $\Omega_{X/S}$ is $0$. Thus an unramified morphism can be thought of as a morphism having no infinitesimal directions in which to move along the fibers.

::: Definition 9
A morphism of schemes $\varphi:X \rightarrow S$, locally of finite presentation, is *unramified* if $\Omega_{X/S}=0$.
:::

By definition, this condition can be computed directly on affine charts. ([§Kähler Differentials and Cotangent Sheaves, ⁋Definition 4](/en/math/scheme_theory/sheaf_of_differentials#def4)) In particular, if $S=\Spec A$ and $X=\Spec B$, then $\Omega_{X/S}=\widetilde{\Omega_{B/A}}$, so $\varphi$ is unramified if and only if the Kähler differential module $\Omega_{B/A}$ vanishes. The standard example is a finite degree separable field extension ([\[Field Theory\] §Separable Extensions, ⁋Definition 8](/en/math/field_theory/separable_extensions#def8)) $\mathbb{K} \subseteq \mathbb{L}$: by definition $\Omega_{\mathbb{L}/\mathbb{K}}=0$, so $\Spec \mathbb{L} \rightarrow \Spec \mathbb{K}$ is unramified. In the same vein, a standard counterexample also arises: considering the inseparable extension $\mathbb{L}=\mathbb{K}(t^{1/p})$ defined over a field of characteristic $p$, we have $\Omega_{\mathbb{L}/\mathbb{K}}\neq 0$, so it is not unramified. ([\[Field Theory\] §Separable Extensions, ⁋Example 4](/en/math/field_theory/separable_extensions#ex4)) This example makes the intuition for unramified morphisms explained above more transparent: in this inseparable extension, $\Spec\mathbb{L}$ is topologically a single point, but after geometric base change a nontrivial thickening remains, so the infinitesimal directions do not disappear and it fails to be unramified.

This condition can be expressed, independently of coordinates, through the diagonal morphism: since the cotangent sheaf itself is defined as the conormal of the diagonal, its vanishing is directly tied to the diagonal being an open embedding.

::: Proposition 10
For a morphism $\varphi:X \rightarrow S$, locally of finite presentation, the following are equivalent.

1. $\varphi$ is unramified.
2. The diagonal morphism $\Delta_\varphi:X \rightarrow X\times_SX$ is an open embedding.
:::
::: Proof

First suppose $\varphi$ is an unramified morphism. In general $\Delta_\varphi$ is always a closed embedding into some open subscheme, so $\Delta_\varphi$ being an open embedding is equivalent to its closed embedding component being an isomorphism, i.e. to the ideal sheaf $\mathcal{I}$ of its image being zero. Since the problem is local over affines, let $S=\Spec A$ and $X=\Spec B$. Then $X\times_SX=\Spec(B\otimes_AB)$ and $\Delta_\varphi$ comes from the multiplication $\mu:B\otimes_AB \rightarrow B$. Setting $\mathfrak{a}=\ker\mu$, we have $\mathfrak{a}/\mathfrak{a}^2\cong \Omega_{B/A}$ (the proof of [§Kähler Differentials and Cotangent Sheaves, ⁋Proposition 6](/en/math/scheme_theory/sheaf_of_differentials#prop6)), so under the unramified assumption, $\mathfrak{a}=\mathfrak{a}^2$ holds. On the other hand, since $B$ is of finite presentation over $A$, $\mathfrak{a}$ is finitely generated over $B\otimes_AB$, and now by [\[Commutative Algebra\] §Integral Extensions, ⁋Lemma 8](/en/math/commutative_algebra/integral_extension#lem8), if $\mathfrak{a}=\mathfrak{a}^2$ then there exists $e\in \mathfrak{a}$ such that $e^2=e$ and $\mathfrak{a}=(e)$. Then $1-e$ is an idempotent trivializing the image of $\mu$, so the image of $\Delta_\varphi$ is realized as a clopen subscheme lying over $D(1-e)$. Hence $\Delta_\varphi$ is an open embedding.

Conversely, suppose $\Delta_\varphi$ is an open embedding. In the same affine situation, take a prime $\mathfrak{P}$ containing $\mathfrak{a}$; then the surjection $(B\otimes_AB)_\mathfrak{P} \rightarrow \bigl((B\otimes_AB)/\mathfrak{a}\bigr)_\mathfrak{P}$ given by the closed embedding is at the same time the isomorphism given by the open embedding, so $\mathfrak{a}_\mathfrak{P}=0$; and at a prime not containing $\mathfrak{a}$, the localization $\mathfrak{a}_\mathfrak{P}$ is the whole ring, so in either case $(\mathfrak{a}/\mathfrak{a}^2)_\mathfrak{P}=0$. Therefore $\mathfrak{a}/\mathfrak{a}^2=0$, i.e. $\Omega_{B/A}=0$, and $\varphi$ is unramified.
:::

For a point $x\in X$ and $s=\varphi(x)$, consider the fiber $X_s=X\times_S\Spec\kappa(s)$. Since the cotangent sheaf commutes with base change, $\Omega_{X_s/\kappa(s)}$ is the pullback of $\Omega_{X/S}$ to $X_s$, which is zero by the unramified assumption. Hence the fiber morphism $X_s\rightarrow\Spec\kappa(s)$ is also unramified. Since the points of an unramified morphism, locally of finite presentation, over a field are isolated points whose residue fields are finite separable extensions, $x$ is an isolated point whose residue field is a finite separable extension $\kappa(x)$ of $\kappa(s)$.

## Étale Morphisms

In differential geometry, a submersion with discrete fibers, i.e. a submersion of relative dimension $0$, defined a local diffeomorphism. ([\[Manifolds\] §Submanifolds and the Inverse Function Theorem, ⁋Theorem 4](/en/math/manifolds/submanifolds#thm4)) Its algebraic counterpart, then, is what one obtains by requiring the smoothness and unramified conditions simultaneously.

::: Definition 11
A morphism $\varphi:X \rightarrow S$, locally of finite presentation, is *étale* if $\varphi$ is smooth and unramified.
:::

For a smooth morphism, $\Omega_{X/S}$ is a locally free sheaf whose rank equals the relative dimension ([Theorem 7](#thm7)), while for an unramified morphism $\Omega_{X/S}=0$ ([Definition 9](#def9)); so when both conditions hold, the relative dimension is $0$. Thus an étale morphism is a smooth morphism of relative dimension $0$, and it is equivalently characterized as follows.

::: Proposition 12
For a morphism $\varphi:X \rightarrow S$, locally of finite presentation, the following are equivalent.

1. $\varphi$ is étale.
2. $\varphi$ is flat and unramified.
:::
::: Proof
That the first condition implies the second is immediate, so it suffices to prove the converse. That is, assume $\varphi$ is flat and unramified, and let us show that its geometric fibers are regular.

First, by the unramified assumption $\Omega_{X/S}=0$, and hence, as we saw above, $\Omega_{X_{\overline{s}}/\mathbb{K}}=0$ also holds over any geometric fiber $X_{\overline{s}}$. Now $X_{\overline{s}}$ is locally of finite presentation over the algebraically closed field $\mathbb{K}=\overline{\kappa(s)}$, so a closed point $z$ of it is a $\mathbb{K}$-point, and therefore $\mathfrak{m}_z/\mathfrak{m}_z^2\cong\Omega_{X_{\overline{s}}/\mathbb{K}}\otimes\kappa(z)=0$. Then by [\[Commutative Algebra\] §Integral Extensions, ⁋Lemma 8](/en/math/commutative_algebra/integral_extension#lem8) we have $\mathfrak{m}_z=0$, so $\mathcal{O}_{X_{\overline{s}},z}=\mathbb{K}$ is a field. On the other hand, if we choose an affine open neighborhood $U$ of $z$ in $X_{\overline{s}}$, then $U$ is Noetherian, and since $\mathcal{O}_{U,z}$ is also a field, the only irreducible component containing $z$ is $\{z\}$. Since $U$ has only finitely many other irreducible components, $\{z\}$ is open in $U$, and hence in $X_{\overline{s}}$. On the other hand, in the proof of [Proposition 3](#prop3) we checked that every nonempty closed subset always contains a closed point, so every point of the fiber must be a closed point. That is, $X_{\overline{s}}$ is a disjoint union of copies of $\Spec\mathbb{K}$, which is a reduced scheme of local dimension $0$, hence regular. Therefore $\varphi$ is flat with regular geometric fibers, so it is smooth, and since $\Omega_{X/S}=0$ it is unramified, i.e. étale.
:::

In the previous section we claimed that an unramified morphism has $0$-dimensional fiber directions, and the computation in the above proof supports this. On the other hand, like [Theorem 6](#thm6), étale morphisms also admit the following standard form.

::: Theorem 13
For a morphism $\varphi:X\rightarrow S$, locally of finite presentation, $\varphi$ is étale if and only if, for every $x\in X$, over an affine open set of $X$ containing $x$ and an affine open set of $S$ containing $\varphi(x)$, one can write $\varphi$ in the form of a *standard étale* morphism of the following shape.

$$\Spec\bigl((A[t]/(f))_g\bigr)\longrightarrow\Spec A$$

Here $f\in A[t]$ is monic, $g\in A[t]/(f)$, and the image of $f'$ is invertible in $(A[t]/(f))_g$.
:::

However, unlike the proof of [Theorem 6](#thm6), the proof of this theorem is somewhat technical, so we omit it. Another important point is that the derivative condition here is the algebraic expression of the separability condition that $f=0$ has no multiple roots; from this one can see that the inseparable example above is not an étale morphism.

::: Example 14
As we saw above, for a finite separable field extension $\mathbb{K}\subseteq\mathbb{L}$, the map $\Spec\mathbb{L}\rightarrow\Spec\mathbb{K}$ is étale. This is because by the primitive element theorem we can write $\mathbb{L}=\mathbb{K}[t]/(f)$, and since $f$ is separable, $f'$ is invertible in $\mathbb{L}$. ([\[Field Theory\] §Separable Extensions, ⁋Definition 8](/en/math/field_theory/separable_extensions#def8)) On the other hand, the inseparable extension given by $\mathbb{K}=\mathbb{F}_p(t)$ and $\mathbb{L}=\mathbb{F}_p(t^{1/p})$ is not an étale morphism. The minimal polynomial of the adjoined element $u=t^{1/p}$ is $\x^p-t$, whose derivative is $0$ and hence cannot be invertible.

In both situations $\Spec \mathbb{L}\rightarrow \Spec \mathbb{K}$ is a morphism from one point to one point, but the picture changes completely once we pass to the geometric fiber. In the first case $f$ splits completely into distinct linear factors, so the geometric fiber decomposes into these roots, whereas in the second case $f$ factors as $(\x-u)^p$ over the algebraic closure of $\mathbb{K}$, so the roots coalesce into a multiple root. Through this we recover the earlier intuition that the unramified condition fails because of a nontrivial thickening.
:::

## Infinitesimal Lifting Criterion

We now turn to the *infinitesimal lifting criterion* for these notions. Conceptually, this has the same shape as the valuative criteria for separatedness and properness treated in [§Valuation Rings](/en/math/scheme_theory/valuative_criteria). To detect separatedness and properness of a morphism, we first took as a test diagram the map $\Spec K\rightarrow\Spec A$ arising from a discrete valuation ring $A$ and its fraction field $K$. Intuitively, $\Spec K$ is the germ of a curve with its central point removed, $\Spec A$ is the object retaining both the central point and the germ data, and extending $\Spec K\rightarrow X$ to $\Spec A\rightarrow X$ amounts to filling in the missing center.

Likewise, for smoothness and unramifiedness (and hence for étaleness) there exists a characterization of this sort. The geometric intuition comes from [\[Manifolds\] §Implicit Function Theorem, ⁋Theorem 3](/en/math/manifolds/implicit_function_theorem#thm3), which asserts that the zero set of $F:\mathbb{R}^{m-n}_s\times\mathbb{R}^n_r\rightarrow\mathbb{R}^n$ is locally diffeomorphic, near a point where the Jacobian in the $r$ directions is invertible, to the graph of $r=g(s)$. If we set $S=\mathbb{R}^{m-n}$ and $X=F^{-1}(0)$, then $X\rightarrow S$ is the projection from this graph to the first factor, and $X$ itself is locally a graph over $S$.

Intuitively, the implicit function theorem says that at a solution with $F(s_0,r_0)=0$, even after perturbing $s_0$ slightly to $s=s_0+\epsilon$, one can uniquely adjust $r$ so that $F(s,r)=0$ continues to hold, and this adjustment rule is exactly what defines the function $r=g(s)$. It is helpful to separate the two hypotheses that make this work: the *existence* of the adjusted $r$ for every nearby $s$ says that the projection from the graph to the first factor is a submersion, and the *uniqueness* of that $r$ says that this projection is an immersion. In our setting, smoothness corresponds to being a submersion and being unramified corresponds to being an immersion, so this characterization will yield, respectively, the existence and the uniqueness of liftings defined using suitable test schemes.

The test scheme corresponding to this should therefore be an object carrying such first-order deformations. When the defining ideal $\mathcal{J}$ of a closed embedding $T_0\hookrightarrow T$ satisfies $\mathcal{J}^2=0$, we call it a *square-zero extension*. The most basic example, for a field $\mathbb{K}$, is

$$\Spec\mathbb{K}\hookrightarrow\Spec\mathbb{K}[\epsilon]/(\epsilon^2).$$

At the level of rings this comes from the ring homomorphism defined by $a+b\epsilon\mapsto a$. The two schemes are both a single point as underlying topological spaces, but the one on the right has a first-order infinitesimal thickening of $\mathbb{K}$ in the $\varepsilon$ direction adjoined, and the reason it carries only first-order information is that $\epsilon^2=0$. Similarly, in the general definition above, if we write $T=\Spec R$ and $T_0=\Spec R_0$ algebraically, this translates into the situation where the kernel $\mathfrak{b}$ of the surjection $R\rightarrow R_0$ satisfies $\mathfrak{b}^2=0$; in particular, because of this condition every second-order term obtained by multiplying two correction terms in $\mathfrak{b}$ vanishes.

For example, suppose $\ch \mathbb{K}\neq 2$, take the above $\Spec \mathbb{K}\hookrightarrow \Spec \mathbb{K}[\epsilon]/(\epsilon^2)$ as the test scheme $T_0\rightarrow T$, and suppose we are given the
$S=\Spec \mathbb{K}[\y]$-scheme $X=\mathbb{A}^2_\mathbb{K}$. The criterion we will introduce takes the form of the following diagram

{% diagram Math/Scheme_Theory/Smooth_and_Etale_Morphisms-4.svg width="14.67em" alt="concrete lifting" %}

Since every scheme appearing here is affine, this diagram comes, after reversing the arrows, from the diagram of $\mathbb{K}$-algebra homomorphisms

{% diagram Math/Scheme_Theory/Smooth_and_Etale_Morphisms-5.svg width="11.90em" alt="ring level lifting" %}

and the scheme morphisms can be defined through these ring homomorphisms. The map $\mathbb{K}[\epsilon]/(\epsilon^2)\rightarrow \mathbb{K}$ is the same one we saw above, and the rest are defined by

$$\mathbb{K}[\y]\rightarrow \mathbb{K}[\x_1,\x_2];\quad \y\mapsto \x_1^2+\x_2^2,\qquad \mathbb{K}[\x_1,\x_2]\rightarrow \mathbb{K};\quad \x_i\mapsto a_i,\qquad \mathbb{K}[\y]\rightarrow \mathbb{K}[\epsilon]/(\epsilon^2); \quad \y\mapsto y_0+c\epsilon.$$

For the commutativity of the diagram, the constants $y_0, a_1, a_2$ must satisfy the equation $y_0=a_1^2+a_2^2$.

Now, for the above $\varphi:\mathbb{A}^2_\mathbb{K}\rightarrow\mathbb{A}^1_\mathbb{K}$, setting

$$F(\y,\x_1,\x_2)=\x_1^2+\x_2^2-\y,$$

the graph given by $(\id_X,\varphi)$ identifies $X$ with the zero set $Z(F)$ inside $\mathbb{A}^2_S=S\times_\mathbb{K} \mathbb{A}_\mathbb{K}^2$, and under this identification $\varphi$ becomes the projection $Z(F)\rightarrow S$ to the first factor. Then the form of the implicit function theorem we want becomes the problem of finding a rule which, starting from a point $\varrho_0:\Spec \mathbb{K}\rightarrow Z(F)$ of $Z(F)$, that is $(y_0, a_1, a_2)$, and applying the first-order deformation $y_0+c\epsilon$, keeps us inside $Z(F)$. This is exactly the problem of the lifting $\varrho:T\rightarrow X$, and at the ring level it is the task of finding a map sending

$$\x_i\mapsto a_i+b_i\epsilon.$$

Together with the previously fixed $\y\mapsto y_0+c\epsilon$, this first defines a $T$-point of the ambient space $\mathbb{A}^2_S$ over $S$. The condition for this to be a lifting is precisely the condition, required by the implicit function theorem, that it factor through the closed subscheme $Z(F)\cong X$, and for this the equation

$$F(y_0+c\epsilon,a_1+b_1\epsilon,a_2+b_2\epsilon)=0$$

must hold. Under our assumptions $\epsilon^2=0$ and $y_0=a_1^2+a_2^2$, this is equivalent to

$$2a_1b_1+2a_2b_2=c,$$

and wherever $a_1\neq 0$ or $a_2\neq 0$ one can actually solve this and obtain the lifting. On the other hand, at $(a_1,a_2)=(0,0)$ the linear equation above becomes $0=c$, so a base change with $c\neq0$ cannot be lifted, and this reflects the fact that the fiber $\x_1^2+\x_2^2=0$ is singular at this point.

Writing the discussion so far in a general setting, we obtain the following criterion.

::: Theorem 15 (Infinitesimal lifting criterion)
Suppose we are given a morphism $\varphi:X \rightarrow S$ locally of finite presentation. For every affine $S$-scheme $T$, every square-zero closed subscheme $T_0\hookrightarrow T$ in it, and every $S$-morphism $\varrho_0:T_0 \rightarrow X$, consider the following diagram

{% diagram Math/Scheme_Theory/Smooth_and_Etale_Morphisms-6.svg width="6.05em" alt="lifting diagram" %}

1. $\varphi$ is smooth if and only if a lifting $\varrho$ exists for every such $(T_0, T, \varrho_0)$.
2. $\varphi$ is unramified if and only if there is at most one lifting $\varrho$ for every such $(T_0, T, \varrho_0)$.
3. $\varphi$ is étale if and only if there exists exactly one lifting $\varrho$ for every such $(T_0, T, \varrho_0)$.
:::
::: Proof
First, write $T=\Spec R$, $T_0=\Spec R_0$, let $q:R\rightarrow R_0$ be the quotient map, and let $\mathfrak{b}$ be its kernel. Then, since $T_0$ is a square-zero extension, we have $\mathfrak{b}^2=0$. Meanwhile, since the problem is affine-local, we may write $S=\Spec A$ and $X=\Spec C$, and then $\varrho_0$ corresponds to an $A$-algebra homomorphism $\rho_0: C \rightarrow R_0$. Now if $\varrho$ is a lifting of $\varrho_0$, this condition translates at the level of ring homomorphisms into $\rho_0=q\circ\rho$. Therefore, if $\varrho$ and $\varrho'$ are two liftings of $\varrho_0$, the equation

$$q\circ\rho=\rho_0=q\circ\rho'$$

must hold, and hence the image of $D=\rho-\rho'$ lands in $\ker q=\mathfrak{b}$. Because $\mathfrak{b}^2=0$, the map $D:C\rightarrow\mathfrak{b}$ becomes an $A$-derivation. For arbitrary $c, c'\in C$,

$$D(cc')=\rho(c)\rho(c')-\rho'(c)\rho'(c')=\rho(c)D(c')+D(c)\rho'(c')\equiv \rho_0(c)D(c')+D(c)\rho_0(c')\pmod{\mathfrak{b}^2},$$

and since $\mathfrak{b}^2=0$ this is exactly the Leibniz rule. Therefore the difference of two liftings is in bijection with the elements of $\Der_A(C, \mathfrak{b})\cong \Hom_C(\Omega_{C/A}, \mathfrak{b})$.

Now if $\varphi$ is unramified then $\Omega_{C/A}=0$, so $\Hom_C(\Omega_{C/A}, \mathfrak{b})=0$, and hence the difference of two liftings is always zero, yielding the uniqueness of the lifting. Conversely, suppose a lifting is always at most one. Then we can define the trivial extension $C\oplus\Omega_{C/A}$, having $\Omega_{C/A}$ as a square-zero ideal. The multiplication on it is given by

$$(c,\omega)(c',\omega')=(cc',c\omega'+c'\omega),$$

and one can check that $T_0=\Spec C\hookrightarrow T=\Spec(C\oplus\Omega_{C/A})$ is indeed a square-zero extension. In this situation, the ring maps $c\mapsto(c,0)$ and $c\mapsto(c,\dd{c})$ both give liftings of $\id_X$, and since they must agree by assumption, the universal derivation must be zero, hence $\Omega_{C/A}=0$, which shows that $\varphi$ is unramified.

Now let us prove the statement on smoothness. As in the earlier proofs, write $C=B/\mathfrak{a}$ with $B=A[\x_1,\ldots,\x_n]$. Then, by the universal property of [\[Algebraic Structures\] §Algebras, ⁋Proposition 8](/en/math/algebraic_structures/algebras#prop8), we can choose an $A$-algebra homomorphism $\widetilde{\rho}:B\rightarrow R$ lifting $B\twoheadrightarrow C\overset{\rho_0}{\longrightarrow}R_0$ along $q$. Since $(q\circ\widetilde{\rho})(\mathfrak{a})=0$, its image lands in $\mathfrak{b}$, and moreover

$$\widetilde{\rho}(\mathfrak{a}^2)=\widetilde{\rho}(\mathfrak{a})^2\subseteq \mathfrak{b}^2=0,$$

so it induces a $C$-linear map

$$\delta:\mathfrak{a}/\mathfrak{a}^2\rightarrow\mathfrak{b}.$$

Here, $\widetilde{\rho}$ factors through $C=B/\mathfrak{a}$ if and only if $\widetilde{\rho}(\mathfrak{a})=0$, that is, $\delta=0$; thus $\delta$ records the obstruction to the lift satisfying the defining equations of $X$. Therefore the problem of obtaining the desired lifting turns into the problem of correcting $\widetilde{\rho}$ by a $\mathfrak{b}$-valued derivation so as to kill $\delta$. By smoothness and [Proposition 8](#prop8), the conormal sequence

$$0\longrightarrow\mathfrak{a}/\mathfrak{a}^2\overset{\bar{d}}{\longrightarrow}\Omega_{B/A}\otimes_BC\longrightarrow\Omega_{C/A}\longrightarrow0$$

is a split short exact sequence. Hence there exists a $C$-linear retraction $r:\Omega_{B/A}\otimes_BC\rightarrow\mathfrak{a}/\mathfrak{a}^2$ satisfying $r\circ\bar{d}=\id$, and using it we set $h=-\delta\circ r$; then $h:\Omega_{B/A}\otimes_BC\rightarrow\mathfrak{b}$ satisfies $h\circ\bar{d}=-\delta$. Now by [\[Commutative Algebra\] §Differentials, ⁋Lemma 2](/en/math/commutative_algebra/differentials#lem2), $h$ corresponds to an $A$-derivation $d:B\rightarrow\mathfrak{b}$, and $\widetilde{\rho}+d:B\rightarrow R$ is again an $A$-algebra homomorphism. This map vanishes on $\mathfrak{a}$ since $\delta+h\circ\bar{d}=0$, so it factors through $C$, and the resulting $\rho:C\rightarrow R$ is a lifting of $\rho_0$.

Conversely, suppose liftings exist for every square-zero extension. The kernel of the quotient $\pi:B/\mathfrak{a}^2\twoheadrightarrow C$ is $\mathfrak{a}/\mathfrak{a}^2$, whose square is zero, so $T_0=X=\Spec C\hookrightarrow T=\Spec(B/\mathfrak{a}^2)$ is a square-zero extension. Applying this to $\varrho_0=\id_X$, we obtain in the opposite direction an $A$-algebra section $\sigma:C\rightarrow B/\mathfrak{a}^2$ of $\pi$. Now the difference of $B\twoheadrightarrow B/\mathfrak{a}^2$ and $B\twoheadrightarrow C\overset{\sigma}{\longrightarrow}B/\mathfrak{a}^2$ is an $\mathfrak{a}/\mathfrak{a}^2$-valued $A$-derivation, and hence it induces a $C$-linear map

$$r:\Omega_{B/A}\otimes_BC\longrightarrow\mathfrak{a}/\mathfrak{a}^2.$$

For $f\in\mathfrak{a}$, the value of this derivation is the class of $f$ in $\mathfrak{a}/\mathfrak{a}^2$, so $r\circ\bar{d}=\id_{\mathfrak{a}/\mathfrak{a}^2}$. That is, the leftmost morphism of the conormal sequence is a split injection, and by [Proposition 8](#prop8), $\varphi$ is smooth.
:::

All three conditions are stable under base change and composition. The base change of a smooth morphism is again smooth, the composition of smooth morphisms is smooth, and the same holds for unramified and étale. This is because the lifting criterion above is expressed purely in terms of properties of morphism diagrams, and is therefore preserved as-is under base change and composition.

Meanwhile, as we saw in the proof above, the cotangent sheaf directly measures the difference of two lifts, that is, uniqueness, whereas the existence of liftings requires the splitting of the conormal sequence; the object that systematically records such more general obstructions is the notion of the cotangent complex.

---

**References**

**[Har]** R. Hartshorne, *Algebraic geometry*. Graduate Texts in Mathematics. Springer, 1977.  
**[Vak]** R. Vakil, *The rising sea: Foundations of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/).
