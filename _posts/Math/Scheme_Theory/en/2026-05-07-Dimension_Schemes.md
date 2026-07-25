---
title: "Dimension"
description: "We define the dimension of a scheme via Krull dimension and examine its relationship with commutative-algebraic dimension. The properties of finite morphisms and integral morphisms are discussed together."
excerpt: "Definition of scheme dimension and its relation to Krull dimension of local rings"

categories: [Math / Scheme Theory]
permalink: /en/math/scheme_theory/dimension
sidebar: 
    nav: "scheme_theory-en"

date: 2025-03-14
weight: 13
translated_at: 2026-07-21T22:45:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-07-21T22:45:02+00:00
---
## Dimension of Schemes

Now we define the dimension of a scheme.

::: Definition 1
The *dimension* of a scheme $X$ is defined as the Krull dimension of the topological space $X$. ([[Topology] §Dimension, ⁋Definition 10](/en/math/topology/dimension#def10))
:::

Then from the Galois correspondence of [[Spectrums] ⁋Proposition 16](/en/math/scheme_theory/spectrums#prop16), we know that the dimension of $\Spec A$ as a scheme equals the dimension of $A$ as a ring. ([[Commutative Algebra] §Dimension, ⁋Definition 1](/en/math/commutative_algebra/Krull_dimension#def1)) Moreover, by definition one can show that $\Spec A$ and $\Spec A/\mathfrak{N}(A)$ are homeomorphic, so $\dim A=\dim A/\mathfrak{N}(A)$. That is, reducedness does not affect dimension.

On the other hand, by the same reasoning as [[Topology] §Dimension, ⁋Proposition 15](/en/math/topology/dimension#prop15), the following holds.

::: Proposition 2
For any scheme $X$, the condition $\dim X=n$ is equivalent to the existence of an affine open covering $(U_i)$ of $X$ such that $\dim U_i\leq n$ for all $i$, with equality for at least one $i$.
:::
::: Proof
Given any chain of irreducible closed subsets of $X$

$$Y_0\subsetneq Y_1\subsetneq\cdots\subsetneq Y_r$$

the generic point $y_0$ of the smallest term $Y_0$ is a point of $X$, so it belongs to some $U_i$ in the covering $(U_i)$. Then every term of the chain meets $U_i$, so by the inclusion-preserving bijection of [[Topology] §Dimension, ⁋Proposition 15](/en/math/topology/dimension#prop15), it corresponds to a chain of the same length inside $U_i$. Conversely, any chain in $U_i$ lifts to $X$ by taking closures, so $\dim X\geq\dim U_i$, and therefore $\dim X=\sup_i\dim U_i$, which is equivalent to the condition in the proposition.
:::

On the other hand, we saw in [[Properties of Scheme Morphisms] ⁋Proposition 14](/en/math/scheme_theory/properties_of_scheme_morphisms#prop14) that a finite morphism is an integral morphism of finite type, and in [[Fiber Products] ⁋Proposition 14](/en/math/scheme_theory/fiber_products#prop14) that any finite morphism is quasi-finite. In general, there exist morphisms that are integral but not of finite type, so we have not yet been able to say anything about the fibers of integral morphisms.

::: Example 3
For example, consider an algebraic closure $\overline{\mathbb{Q}}$ of $\mathbb{Q}$. Every element of $\overline{\mathbb{Q}}$ is algebraic over $\mathbb{Q}$, hence integral, and therefore $\mathbb{Q} \rightarrow \overline{\mathbb{Q}}$ is an integral extension; consequently the scheme morphism $\varphi:\Spec \overline{\mathbb{Q}} \rightarrow \Spec \mathbb{Q}$ is also an integral morphism.

Now base change $\varphi$ along $\Spec\overline{\mathbb{Q}}\rightarrow\Spec\mathbb{Q}$ to obtain the following pullback diagram

{% diagram Math/Scheme_Theory/Dimension_Schemes-1.svg width="13.60em" alt="pullback" %}

The left-hand vertical map

$$\Spec(\overline{\mathbb{Q}}\otimes_\mathbb{Q}\overline{\mathbb{Q}})\rightarrow \Spec \overline{\mathbb{Q}}$$

is also integral by [[Fiber Products] ⁋Proposition 15](/en/math/scheme_theory/fiber_products#prop15).

To examine this map, let us look concretely at the ring homomorphism $\overline{\mathbb{Q}}\rightarrow \overline{\mathbb{Q}}\otimes_\mathbb{Q}\overline{\mathbb{Q}}$. Finding a section of the above map of schemes is the same as finding a retraction of this homomorphism, which arises from the following surjective ring homomorphism

$$\overline{\mathbb{Q}}\otimes_\mathbb{Q}\overline{\mathbb{Q}}\rightarrow\overline{\mathbb{Q}},\qquad a\otimes b\mapsto a\sigma(b)$$

Specifically, the kernel $\mathfrak{p}_\sigma$ of this ring homomorphism is a maximal ideal, hence defines a point of $\Spec(\overline{\mathbb{Q}}\otimes_\mathbb{Q}\overline{\mathbb{Q}})$, and if $\sigma\neq\tau$ then choosing $b\in\overline{\mathbb{Q}}$ with $\sigma(b)\neq\tau(b)$, we have $1\otimes b-\sigma(b)\otimes 1\in\mathfrak{p}_\sigma$ but this element does not belong to $\mathfrak{p}_\tau$, so $\mathfrak{p}_\sigma\neq\mathfrak{p}_\tau$. Therefore $\Spec(\overline{\mathbb{Q}}\otimes_\mathbb{Q}\overline{\mathbb{Q}})$ has at least as many points as $\Gal(\overline{\mathbb{Q}}/\mathbb{Q})$, that is, infinitely many, and $\Spec(\overline{\mathbb{Q}}\otimes_\mathbb{Q}\overline{\mathbb{Q}})\rightarrow\Spec\overline{\mathbb{Q}}$ is not a quasi-finite morphism, hence not a finite morphism.
:::

Or consider the simpler example $\Spec \mathbb{C}\rightarrow \Spec \mathbb{R}$. Since $\mathbb{R}$ and $\mathbb{C}$ are both fields, $\Spec\mathbb{C}$ and $\Spec\mathbb{R}$ each consist of a single point, so this map itself is trivially a map from one point to one point. However, pulling it back along $\Spec \mathbb{C}\rightarrow \Spec \mathbb{R}$ yields a map analogous to the one above,

$$\Spec(\mathbb{C}\otimes_\mathbb{R} \mathbb{C}) \rightarrow \Spec \mathbb{C}$$

and $\mathbb{C}\otimes_\mathbb{R}\mathbb{C}$ is no longer a field. Indeed, since $\Spec\mathbb{C}=\Spec\mathbb{R}[\x]/(\x^2+1)$,

$$\mathbb{C}\otimes_\mathbb{R} \mathbb{C}\cong \mathbb{C}\otimes_\mathbb{R} \frac{\mathbb{R}[\x]}{(\x^2+1)}\cong \frac{\mathbb{C}[\x]}{(\x^2+1)}$$

and $\x^2+1$ factors over $\mathbb{C}$ as a product of two linear factors $\x^2+1=(\x-i)(\x+i)$; since $(\x-i)$ and $(\x+i)$ are comaximal, by [[Ring Theory] §Chinese Remainder Theorem, ⁋Proposition 6](/en/math/ring_theory/chinese_remainder_theorem#prop6)

$$\frac{\mathbb{C}[\x]}{((\x-i)(\x+i))}\cong\frac{\mathbb{C}[\x]}{(\x-i)}\times\frac{\mathbb{C}[\x]}{(\x+i)}\cong\mathbb{C}\times\mathbb{C}$$

Thinking in the language of Galois groups as in the example above, this decomposition arises because the two factors $\mathbb{C}[\x]/(\x-i)$ and $\mathbb{C}[\x]/(\x+i)$ correspond precisely to the automorphisms $\mathbb{C}\rightarrow \mathbb{C}$ fixing $\mathbb{R}$, that is, the two elements of $\Gal(\mathbb{C}/\mathbb{R})$, and the same phenomenon occurs in [Example 3](#ex3) for $\mathbb{Q}\rightarrow \overline{\mathbb{Q}}$. The only difference is that $\Gal(\overline{\mathbb{Q}}/\mathbb{Q})$ is infinite, so the fiber has infinitely many points rather than two.

Nevertheless, this example suggests some kind of finiteness for the fibers of an integral morphism; for instance, $\Gal(\overline{\mathbb{Q}}/\mathbb{Q})$ is a profinite group, hence ([[Field Theory] §Properties of Galois Groups, ⁋Proposition 5](/en/math/field_theory/properties_of_galois_extensions#prop5)) $0$-dimensional. This is a fact that holds for any integral morphism.

::: Proposition 4
Every fiber of an integral morphism $\varphi: X \rightarrow Y$ is $0$-dimensional.
:::
::: Proof
By definition, the fiber over a point $y\in Y$ is given by the base change of $\varphi$ along the inclusion map $\Spec \kappa(y) \rightarrow Y$ for the residue field $\kappa(y)$ from [[Schemes] ⁋Definition 5](/en/math/scheme_theory/schemes#def5):

$$\varphi^{-1}(y)=X\times_Y\Spec \kappa(y)$$

Since integral morphisms are preserved under base change ([[Fiber Products] ⁋Proposition 15](/en/math/scheme_theory/fiber_products#prop15)),

$$\varphi^{-1}(y)=X\times_Y\Spec \kappa(y) \rightarrow \Spec \kappa(y)$$

is an integral morphism, and since an integral morphism is affine by definition, it suffices to show that $\dim \Spec B=\dim B=0$ for an integral morphism $\Spec B \rightarrow \Spec \kappa(y)$. That is, we must show that for any integral extension $\kappa(y) \rightarrow B$, there cannot exist a chain of prime ideals of $B$

$$\mathfrak{q}_1\subsetneq \mathfrak{q}_2$$

This follows from [[Commutative Algebra] §Integral Extensions and Ideals, ⁋Corollary 4](/en/math/commutative_algebra/lying_over_and_going_up#cor4).
:::

Geometrically, this proposition shows that no fiber of an integral morphism has positive dimension.

The [[Commutative Algebra] §Integral Extensions and Ideals, ⁋Corollary 4](/en/math/commutative_algebra/lying_over_and_going_up#cor4) used in the proof above also holds for any integral extension $A\hookrightarrow B$. By this, contracting a chain of prime ideals of $B$ to $A$ remains strict, so $\dim B\leq\dim A$; conversely, by lying over and going up in [[Commutative Algebra] §Integral Extensions and Ideals, ⁋Proposition 1](/en/math/commutative_algebra/lying_over_and_going_up#prop1), a chain of prime ideals of $A$ lifts to $B$, so $\dim A\leq\dim B$. Therefore, more generally, the following holds.

::: Proposition 5
For any integral extension $\phi:A \rightarrow B$,

$$\dim\Spec A=\dim\Spec B$$

always holds.
:::

In particular, for any integral domain $A$ and its normalization $\tilde{A}$, since the extension $A\hookrightarrow\tilde{A}$ is integral, [Proposition 5](#prop5) gives $\dim\Spec\tilde{A}=\dim\Spec A$. Here the normalization $\tilde{A}$ is the extension obtained by enlarging $A$ until it becomes integrally closed in its field of fractions $\Frac(A)$, that is, by adjoining to $A$ all elements of $\Frac(A)$ that are integral over $A$. ([[Commutative Algebra] §Integral Extension, ⁋Definition 3](/en/math/commutative_algebra/integral_extension#def3)) By definition $A\subseteq\tilde{A}\subseteq\Frac(A)$, so $\Frac(\tilde{A})=\Frac(A)$; that is, normalization preserves the function field of $A$.

::: Example 6
In the discussion above we saw that normalization preserves the function field. Geometrically, when $A$ is the coordinate ring of an affine variety over $\mathbb{K}$, this means that the space obtained by normalization is birational to the original. ([[Algebraic Varieties] §Rational Maps, ⁋Proposition 10](/en/math/algebraic_varieties/rational_maps#prop10)) That is, normalization agrees with the original space outside a certain locus small enough to be negligible.

Moreover, normalization makes this locus precisely the singular points. As a representative example, consider the cusp from [[Algebraic Varieties] §Tangent Spaces and Smoothness, ⁋Example 7](/en/math/algebraic_varieties/tangent_spaces_and_smoothness#ex7):

$$A=\mathbb{K}[\x,\y]/(\y^2-\x^3)\cong\mathbb{K}[t^2,t^3]$$

To see the field of fractions of $A$, we use $t=\y/\x$ to check that $\Frac(A)=\mathbb{K}(t)$; then the element $t\in\Frac(A)$ satisfies $t^2=\x\in A$, so it is integral over $A$. Hence the extension obtained by adjoining $t$,

$$A[t]=\mathbb{K}[t^2,t^3,t]=\mathbb{K}[t]$$

is an integral extension of $A$, and since $A[t]$ is a UFD, it is integrally closed by [[Commutative Algebra] §Integral Extension, ⁋Proposition 9](/en/math/commutative_algebra/integral_extension#prop9); thus this is precisely the normalization $\tilde{A}$.

Now let us see geometrically what this means. We first examine the map between spaces induced by the integral extension $A\rightarrow A[t]$:

$$\Spec A[t]\rightarrow \Spec A$$

Consider the origin $\mathfrak{m}=(t^2,t^3)\in\Spec A$, which is the singular point of the curve $\Spec A$. The fiber of the above map over this point is given by the following pullback diagram

{% diagram Math/Scheme_Theory/Dimension_Schemes-2.svg width="17.35em" alt="cusp-fiber" %}

that is, by the map

$$\Spec(A[t]\otimes_A A/\mathfrak{m})=\Spec(A[t]/(t^2,t^3))=\Spec(A[t]/(t^2))$$

Thus the fiber itself is a single point, but the scheme structure on it is non-reduced, whereas the origin $\Spec A/\mathfrak{m}$ of $\Spec A$ is a reduced single point, being the spectrum of a field; hence the above fiber cannot coincide with this point. On the other hand, on the open subset $D(\x)$ with the origin removed, $\x=t^2$ becomes invertible, so $t=t^3\cdot(t^2)^{-1}$ enters and

$$A[\x^{-1}]=\tilde{A}[\x^{-1}]$$

so the two schemes agree completely away from the origin.

To examine what happens at the origin more algebraically, let us look at the local rings. First, the preimage of the origin $\mathfrak{m}$ of $\Spec A$ is, by definition, the prime ideals of $A[t]$ containing $\mathfrak{m}$; the prime ideals containing $\mathfrak{m}A[t]=(t^2)$ are exactly those containing the radical $(t)$. Then the local ring of $A[t]$ at the origin $(t)$ is

$$A[t]_{(t)}=\mathbb{K}[t]_{(t)}$$

whereas the local ring at the origin of the original curve $\Spec A$ is

$$A_{\mathfrak{m}}=\mathbb{K}[t^2,t^3]_{(t^2, t^3)}$$

Comparing these reveals algebraically what normalization does at the origin. Although $A_{\mathfrak{m}}$ is a $1$-dimensional local ring, its maximal ideal cannot be generated by a single element and requires the two elements $t^2$ and $t^3$, so it is not a regular local ring. ([[Commutative Algebra] §Dimension, ⁋Definition 12](/en/math/commutative_algebra/Krull_dimension#def12)) Indeed $\mathfrak{m}/\mathfrak{m}^2$ is a $2$-dimensional vector space generated by the images of $t^2$ and $t^3$, which is the same phenomenon as the tangent space at the origin of the cusp being computed as $2$-dimensional, larger than the dimension of the curve, in [[Algebraic Varieties] §Tangent Spaces and Smoothness, ⁋Example 7](/en/math/algebraic_varieties/tangent_spaces_and_smoothness#ex7). On the other hand, the local ring $A[t]_{(t)}=\mathbb{K}[t]_{(t)}$ of the normalization is a regular local ring whose maximal ideal is generated by the single element $t$. That is, normalization replaces the singular local ring $A_{\mathfrak{m}}$ by the regular local ring $A[t]_{(t)}$, thereby resolving the cusp.
:::

For any integral scheme $X$, normalization can be defined in the same way. Cover $X$ by affine opens $\Spec A_i$. Since $X$ is integral, it has a unique generic point $x$, and this point corresponds in each $\Spec A_i$ to the minimal prime $(0)$ of the domain $A_i$, so its stalk is $\Frac(A_i)$. Since the stalk $\mathcal{O}_{X,x}$ is the same no matter which affine open we compute it in, all $\Frac(A_i)$ agree in a common function field $K(X)$ ([[Algebra of Schemes] §§Rational Functions](/en/math/scheme_theory/algebra_of_schemes#유리함수)), and we can take the normalization $\tilde{A}_i$ of $A_i$ inside $K(X)$ on each piece. Since normalization commutes with localization ([[Commutative Algebra] §Integral Extension, ⁋Proposition 12](/en/math/commutative_algebra/integral_extension#prop12)), the restrictions of each $\Spec\tilde{A}_i$ to the overlaps $\Spec A_i\cap\Spec A_j$ agree, and therefore they glue together into a single scheme $\tilde{X}$ defining the normalization morphism $\tilde{X}\rightarrow X$. This morphism is integral since $A_i\hookrightarrow\tilde{A}_i$ is an integral extension affine-locally, and by [Proposition 5](#prop5) we have $\dim\Spec\tilde{A}_i=\dim\Spec A_i$ on each piece, so from [Proposition 2](#prop2) we obtain $\dim\tilde{X}=\dim X$.

Now we define codimension.

::: Definition 7
For an irreducible subset $Y$ of a topological space $X$, the *codimension* $\codim_XY$ of $Y$ in $X$ is defined as the supremum of the lengths of strictly descending chains of irreducible closed subsets of $X$

$$Z_n\supsetneq Z_{n-1}\supsetneq\cdots\supsetneq Z_0=\cl_X(Y)$$
:::

Then one can check that the codimension of a prime ideal $\mathfrak{p}$ of a ring $A$ equals the codimension of the point $\mathfrak{p}$ in $\Spec A$. ([[Commutative Algebra] §Dimension, ⁋Definition 2](/en/math/commutative_algebra/Krull_dimension#def2))

::: Proposition 8
For an irreducible closed subset $Y$ of $X$ and its generic point $y$, $\codim_X Y=\dim \mathcal{O}_{X,y}$ holds.
:::
::: Proof
Since $Y$ has generic point $y$, by definition $\codim_XY$ equals $\codim_X\{y\}$. Now choose any affine open subset $U\cong\Spec A$ containing $y$, and suppose that under this isomorphism $y\in U$ corresponds to $\mathfrak{p}_y\in \Spec A$. Then from [[Topology] §Dimension, ⁋Proposition 15](/en/math/topology/dimension#prop15) we know that there is a one-to-one correspondence between irreducible closed subsets of $X$ meeting $U$ and irreducible closed subsets of $U$. That is, $\codim_X\{y\}=\codim_U \mathfrak{p}_y$. Now we obtain the desired result from [[Spectrums] ⁋Proposition 16](/en/math/scheme_theory/spectrums#prop16).
:::

More generally, in [[Commutative Algebra] §Dimension, ⁋Definition 2](/en/math/commutative_algebra/Krull_dimension#def2) we defined codimension and then proved the inequality

$$\dim \mathfrak{a}+\codim \mathfrak{a}\leq \dim A$$

and using [[Topology] §Dimension, ⁋Proposition 15](/en/math/topology/dimension#prop15) in place of [[Commutative Algebra] §Localization, ⁋Proposition 8](/en/math/commutative_algebra/localization#prop8) used there, one can check that for a scheme $X$ and an irreducible closed subset $Y$ of $X$, the inequality

$$\dim Y+\codim_XY\leq \dim X$$

holds. However, as before, equality does not hold in general.

## Noether Normalization

Now we prove the following important result.

::: Theorem 9 (Noether normalization lemma)
Let $\mathbb{K}$ be an arbitrary field and $A$ a finitely generated $\mathbb{K}$-algebra. If $A$ is an integral domain and

$$\trdeg_\mathbb{K}\Frac(A)=n$$

then there exist suitable elements $x_1,\ldots, x_n$ of $A$ that are algebraically independent and such that $A$ is a finite $\mathbb{K}[x_1,\ldots, x_n]$-module.
:::
::: Proof
From the assumption that $A$ is a finitely generated $\mathbb{K}$-algebra, we can write

$$A=\mathbb{K}[y_1,\ldots, y_m]/\mathfrak{p}$$

Then the images of $y_1,\ldots, y_m$ in $\Frac(A)$ generate $\Frac(A)$ as a field extension of $\mathbb{K}$, so we must have $m\geq n$.

Now if $m=n$, the $y_i$ are exactly the desired elements, so there is nothing more to prove. Assume $m>n$ for the induction, and suppose the theorem holds for any $k$ with $n\leq k< m$. Then from the assumption $m>n$, the elements $y_1,\ldots, y_m$ are algebraically dependent. That is, there exists an $m$-variable polynomial with coefficients in $\mathbb{K}$

$$f(\x_1,\ldots, \x_m)=\sum \alpha_{d_1d_2\cdots d_m}\x_1^{d_1}\cdots\x_m^{d_m}\in \mathbb{K}[\x_1,\ldots, \x_m]\tag{$\ast$}$$

satisfying

$$f(y_1,\ldots, y_m)=0$$

Now for integers $r_1,\ldots, r_{m-1}$, define elements $z_1,\ldots, z_{m-1}$ by

$$z_1=y_1-y_m^{r_1},\quad z_2=y_2-y_m^{r_2},\quad\ldots\quad,\quad z_{m-1}=y_{m-1}-y_m^{r_{m-1}}$$

Then by definition

$$f(z_1+y_m^{r_1},\ldots, z_{m-1}+y_m^{r_{m-1}}, y_m)=0\tag{$\ast\ast$}$$

holds. Substituting

$$\x_1=z_1+y_m^{r_1},\quad \ldots\quad,\quad \x_{m-1}=z_{m-1}+y_m^{r_{m-1}},\quad \x_m=y_m$$

into each monomial $\alpha_{d_1d_2\cdots d_m}\x_1^{d_1}\cdots\x_m^{d_m}$ comprising $f$ in ($\ast$) and expanding, the result is a power of $y_m$ with constant coefficient

$$\alpha_{d_1d_2\cdots d_m}y_m^{r_1d_1+\cdots+r_{m-1}d_{m-1}+d_m}$$

together with other terms involving the $z_k$. Now choose an integer $r$ larger than the maximum of the exponents $d_j$ actually appearing in $f$ and set $r_i=r^i$; then the exponents

$$r_1d_1+\cdots+r_{m-1}d_{m-1}+d_m=d_m+d_1r+\cdots+d_{m-1}r^{m-1}$$

take distinct values for different monomials of $f$ by the uniqueness of base-$r$ expansion, so exactly one such term survives as the leading term. Its coefficient is a nonzero element of $\mathbb{K}$, so we may divide both sides by it, and therefore the equality ($\ast\ast$) shows that $y_m$ is integrally dependent on $z_1,\ldots, z_{m-1}$.

On the other hand, let $A'$ be the $\mathbb{K}$-subalgebra of $A$ generated by $z_1,\ldots, z_{m-1}$, that is, the $\mathbb{K}$-subalgebra of $A$ containing the coefficients when ($\ast\ast$) is viewed as a polynomial in $y_m$. By the above argument $A$ is a finite $A'$-module, and therefore $\Frac(A)$ is an algebraic extension of $\Frac(A')$, so $\trdeg_\mathbb{K}\Frac(A')=n$. Then $A'$ is an integral domain generated by $m-1$ elements, so by the induction hypothesis there exist $x_1,\ldots, x_n\in A'$ satisfying the desired condition, and since $A'$ is a finite $\mathbb{K}[x_1,\ldots, x_n]$-module, $A$ is also a finite $\mathbb{K}[x_1,\ldots, x_n]$-module.
:::

Geometrically, setting $A=\mathbb{K}[y_1,\ldots, y_m]/\mathfrak{p}$ means that $\Spec A$ is an integral closed subscheme of affine space $\mathbb{A}^m_\mathbb{K}$, so the finite ring homomorphism $\mathbb{K}[x_1,\ldots, x_n] \rightarrow \mathbb{K}[y_1,\ldots, y_m]/\mathfrak{p}$ obtained from the above theorem corresponds geometrically to finding a finite scheme morphism $\Spec A \rightarrow \Spec \mathbb{K}[x_1,\ldots, x_n]$. Since the finite extension $\mathbb{K}[x_1,\ldots, x_n] \rightarrow A$ is an integral extension, by [Proposition 5](#prop5) we have $\dim A=\dim \mathbb{K}[x_1,\ldots, x_n]$, so by [[Commutative Algebra] §System of Parameters, ⁋Corollary 11](/en/math/commutative_algebra/system_of_parameters#cor11) we obtain the following result.

::: Proposition 10
Let $\mathbb{K}$ be an arbitrary field and $A$ a finitely generated $\mathbb{K}$-algebra. If $A$ is an integral domain, then $\dim\Spec A=\trdeg_\mathbb{K} \Frac(A)$ holds.
:::

The results most crucially used above are of course those of [[Commutative Algebra] §Integral Extensions and Ideals](/en/math/commutative_algebra/lying_over_and_going_up). On the other hand, using the dimension formula [[Commutative Algebra] §Noether Normalization, ⁋Theorem 4](/en/math/commutative_algebra/noether_normalization#thm4), we obtain the following.

::: Proposition 11
Let $\mathbb{K}$ be an arbitrary field and $A$ a finitely generated $\mathbb{K}$-algebra. If $A$ is an integral domain and $f\in A$ is a nonzero non-unit, then $\dim A/(f)=\dim A-1$ holds.
:::
::: Proof
Choose a minimal prime $\mathfrak{p}$ of $A$ containing $(f)$. By [[Commutative Algebra] §Dimension, ⁋Theorem 6](/en/math/commutative_algebra/Krull_dimension#thm6) we have $\operatorname{ht}\mathfrak{p}\leq 1$, and since $A$ is a domain and $f\neq 0$, from $(0)\subsetneq\mathfrak{p}$ we have $\operatorname{ht}\mathfrak{p}\geq 1$. Therefore $\operatorname{ht}\mathfrak{p}=1$, and by the dimension formula [[Commutative Algebra] §Noether Normalization, ⁋Theorem 4](/en/math/commutative_algebra/noether_normalization#thm4) we have $\dim A/\mathfrak{p}=\dim A-1$. Now $\dim A/(f)$ is given as the maximum of $\dim A/\mathfrak{p}$ over the minimal primes $\mathfrak{p}$ of $(f)$, and since all minimal primes have height $1$ as above, all these values are $\dim A-1$, and therefore $\dim A/(f)=\dim A-1$.
:::

## Principal Ideal Theorem

Earlier we saw that for a finite type affine integral $\mathbb{K}$-scheme $X=\Spec A$, the closed subscheme $Z(f)$ defined by a nonzero non-unit $f\in A$ has dimension one less than $X$. This is clearly a useful result, but we can also examine its consequences in more general cases as follows.

::: Proposition 12
For a locally Noetherian scheme $X$ and a function $f$ on $X$, every irreducible component of $Z(f)$ has codimension $0$ or $1$.
:::
::: Proof
Let $W$ be an irreducible component of $Z(f)$ and $w$ the generic point of $W$. Choose an affine open subset $U\cong\Spec A$ containing $w$; since $X$ is locally Noetherian we may take $A$ to be a Noetherian ring, and suppose that under this isomorphism $w$ corresponds to $\mathfrak{p}\in\Spec A$. By the correspondence of [[Topology] §Dimension, ⁋Proposition 15](/en/math/topology/dimension#prop15), $W\cap U$ is an irreducible component of $Z(f\vert_U)$, so $\mathfrak{p}$ is a minimal prime ideal containing the principal ideal generated by $f\vert_U\in A$. Therefore by [[Commutative Algebra] §Dimension, ⁋Theorem 6](/en/math/commutative_algebra/Krull_dimension#thm6) we have $\codim\mathfrak{p}\leq 1$.

On the other hand, since the stalk depends only on an open neighborhood of $w$, we have $\mathcal{O}_{U,w}=\mathcal{O}_{X,w}$, and since $W$ and $W\cap U$ are irreducible closed subsets of $X$ and $U$ respectively both having $w$ as generic point, applying [Proposition 8](#prop8) twice gives

$$\codim_XW=\dim\mathcal{O}_{X,w}=\dim\mathcal{O}_{U,w}=\codim_U(W\cap U)$$

Now since the codimension of the point $\mathfrak{p}$ in $\Spec A$ equals $\codim\mathfrak{p}$ in the ring $A$ ([[Commutative Algebra] §Dimension, ⁋Definition 2](/en/math/commutative_algebra/Krull_dimension#def2)), we eventually obtain $\codim_XW=\codim\mathfrak{p}\leq 1$.
:::

That $\codim_XW=0$ means that $W$ is an irreducible component of $X$ itself, that is, $f$ vanishes identically on that component. Therefore if $f$ does not vanish identically on any irreducible component of $X$, then every component of $Z(f)$ has codimension exactly $1$, and this is the role played by the assumptions in [Proposition 11](#prop11) that $A$ is an integral domain and $f$ is nonzero.

---

**References**

**[AM]** M. F. Atiyah and I. G. Macdonald, *Introduction to commutative algebra*, Addison-Wesley, 1969.
