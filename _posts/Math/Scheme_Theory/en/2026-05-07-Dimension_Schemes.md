---
title: "Dimension"
description: "We define the dimension of a scheme using Krull dimension and examine its relationship with dimension in commutative algebra. Properties of finite and integral morphisms are also covered."
excerpt: "Definition of scheme dimension and relation to Krull dimension of local rings"

categories: [Math / Scheme Theory]
permalink: /en/math/scheme_theory/dimension
sidebar: 
    nav: "scheme_theory-en"

date: 2025-03-14
weight: 13
translated_at: 2026-09-06T11:15:05+00:00
translation_source: antigravity-gemini-3.8-flash-high
---
## Dimension of Schemes

Now we define the dimension of a scheme.

::: Definition 1
The *dimension* of a scheme $X$ is defined as the Krull dimension of the topological space $X$. ([\[Topology\] §Dimension, ⁋Definition 10](/en/math/topology/dimension#def10){: data-relation="required" })
:::

Then from the Galois correspondence in [§The Spectrum, ⁋Proposition 16](/en/math/scheme_theory/spectrums#prop16){: data-relation="required" }, we see that the dimension of $\Spec A$ as a scheme is equal to the dimension of $A$ as a ring. ([\[Commutative Algebra\] §Krull Dimension, ⁋Definition 1](/en/math/commutative_algebra/Krull_dimension#def1){: data-relation="required" }) Moreover, since by definition one can show that $\Spec A$ and $\Spec A/\mathfrak{N}(A)$ are homeomorphic, $\dim A=\dim A/\mathfrak{N}(A)$ holds. That is, reducedness does not affect the dimension. 

On the other hand, for the same reason as in [\[Topology\] §Dimension, ⁋Proposition 15](/en/math/topology/dimension#prop15){: data-relation="required" }, the following holds.

::: Proposition 2
For any scheme $X$ and integer $n\geq 0$, $\dim X=n$ if and only if there exists an affine open covering $(U_i)$ of $X$ such that $\dim U_i\leq n$ for all $U_i$, with equality holding for at least one $i$. 
:::
::: Proof
In any chain of irreducible closed subsets of $X$

$$Y_0\subsetneq Y_1\subsetneq\cdots\subsetneq Y_r$$

the generic point $\eta_0$ of the smallest term $Y_0$ is a point of $X$, so it belongs to some $U_i$ by the covering $(U_i)$. Then every term of the chain meets $U_i$, so considering the inclusion-preserving bijection in [\[Topology\] §Dimension, ⁋Proposition 15](/en/math/topology/dimension#prop15){: data-relation="required" }, this corresponds to a chain of the same length in $U_i$. Conversely, any chain in $U_i$ is lifted by taking closures in $X$, so $\dim X\geq\dim U_i$, and therefore $\dim X=\sup_i\dim U_i$, which is equivalent to the condition of the proposition.
:::

What the proof actually gave is $\dim X=\sup_i\dim U_i$, and without the assumption that $\dim X$ is finite, there might not exist an $i$ for which equality holds. For example, $X=\coprod_{d\geq 0}\mathbb{A}^d_\mathbb{K}$ is infinite-dimensional, but each affine open subset meets only finitely many components and thus is finite-dimensional.

Meanwhile, in [§Properties of Scheme Morphisms, ⁋Proposition 15](/en/math/scheme_theory/properties_of_scheme_morphisms#prop15){: data-relation="weak" }, we observed that a finite morphism is an integral morphism of finite type, and in [§Fiber Products, ⁋Proposition 15](/en/math/scheme_theory/fiber_products#prop15){: data-relation="weak" }, that any finite morphism is quasi-finite. In general, there exist morphisms that are integral but not of finite type, and therefore we cannot yet discuss the fibers of an integral morphism.

::: Example 3
For example, consider the algebraic closure $\overline{\mathbb{Q}}$ of $\mathbb{Q}$. Any element of $\overline{\mathbb{Q}}$ is algebraic over $\mathbb{Q}$ and thus integral, so $\mathbb{Q} \rightarrow \overline{\mathbb{Q}}$ is an integral extension, from which the scheme morphism $\varphi:\Spec \overline{\mathbb{Q}} \rightarrow \Spec \mathbb{Q}$ is also an integral morphism.

Now, base-changing $\varphi$ by $\Spec\overline{\mathbb{Q}}\rightarrow\Spec\mathbb{Q}$, we obtain the following pullback diagram

{% diagram Math/Scheme_Theory/Dimension_Schemes-1.svg width="13.60em" alt="pullback" %}

where the left vertical map

$$\Spec(\overline{\mathbb{Q}}\otimes_\mathbb{Q}\overline{\mathbb{Q}})\rightarrow \ Spec \overline{\mathbb{Q}}$$

is also integral by [§Fiber Products, ⁋Proposition 16](/en/math/scheme_theory/fiber_products#prop16){: data-relation="required" }. 

To examine this map, let us look specifically at the ring homomorphism $\overline{\mathbb{Q}}\rightarrow \overline{\mathbb{Q}}\otimes_\mathbb{Q}\overline{\mathbb{Q}}$. Viewing a section of the above morphism between schemes is equivalent to viewing a retraction of this map, which comes from the surjective ring homomorphism

$$\overline{\mathbb{Q}}\otimes_\mathbb{Q}\overline{\mathbb{Q}}\rightarrow\overline{\mathbb{Q}},\qquad a\otimes b\mapsto a\sigma(b)$$

for any $\sigma\in\Gal(\overline{\mathbb{Q}}/\mathbb{Q})$. Specifically, the kernel $\mathfrak{p}_\sigma$ of this ring homomorphism is a maximal ideal and hence defines a point of $\Spec(\overline{\mathbb{Q}}\otimes_\mathbb{Q}\overline{\mathbb{Q}})$. If $\sigma\neq\tau$, then choosing $b\in\overline{\mathbb{Q}}$ such that $\sigma(b)\neq\tau(b)$, we have $1\otimes b-\sigma(b)\otimes 1\in\mathfrak{p}_\sigma$ but not in $\mathfrak{p}_\tau$, so $\mathfrak{p}_\sigma\neq\mathfrak{p}_\tau$. Therefore, $\Spec(\overline{\mathbb{Q}}\otimes_\mathbb{Q}\overline{\mathbb{Q}})$ has at least as many points as $\Gal(\overline{\mathbb{Q}}/\mathbb{Q})$, that is, infinitely many points, and $\Spec(\overline{\mathbb{Q}}\otimes_\mathbb{Q}\overline{\mathbb{Q}})\rightarrow\Spec\overline{\mathbb{Q}}$ is not a quasi-finite morphism, hence not a finite morphism.
:::

Or as a simpler example, let us consider $\Spec \mathbb{C}\rightarrow \Spec \mathbb{R}$. Since both $\mathbb{R}$ and $\mathbb{C}$ are fields, $\Spec\mathbb{C}$ and $\Spec\mathbb{R}$ are each a single point, so this map itself is a trivial map from a point to a point. However, if we pull this back by $\Spec \mathbb{C}\rightarrow \Spec \mathbb{R}$ to form a map similar to the above example,

$$\Spec(\mathbb{C}\otimes_\mathbb{R} \mathbb{C}) \rightarrow \Spec \mathbb{C}$$

then $\mathbb{C}\otimes_\mathbb{R}\mathbb{C}$ is no longer a field. Indeed, since $\Spec\mathbb{C}=\Spec\mathbb{R}[\x]/(\x^2+1)$, 

$$\mathbb{C}\otimes_\mathbb{R} \mathbb{C}\cong \mathbb{C}\otimes_\mathbb{R} \frac{\mathbb{R}[\x]}{(\x^2+1)}\cong \frac{\mathbb{C}[\x]}{(\x^2+1)}$$

and $\x^2+1$ factors over $\mathbb{C}$ as the product of two linear polynomials $\x^2+1=(\x-i)(\x+i)$. Since $(\x-i)$ and $(\x+i)$ are comaximal, by [\[Ring Theory\] §Chinese Remainder Theorem, ⁋Proposition 6](/en/math/ring_theory/chinese_remainder_theorem#prop6){: data-relation="required" } we have 

$$\frac{\mathbb{C}[\x]}{((\x-i)(\x+i))}\cong\frac{\mathbb{C}[\x]}{(\x-i)}\times\frac{\mathbb{C}[\x]}{(\x+i)}\cong\mathbb{C}\times\mathbb{C}$$

Thinking in the language of the Galois group examined in the example above, this occurs because the two factors $\mathbb{C}[\x]/(\x-i)$ and $\mathbb{C}[\x]/(\x+i)$ in the decomposition correspond precisely to the automorphisms of $\mathbb{C}\rightarrow \mathbb{C}$ fixing $\mathbb{R}$, that is, the two elements of $\Gal(\mathbb{C}/\mathbb{R})$; the same thing happens for $\mathbb{Q}\rightarrow \overline{\mathbb{Q}}$ in [Example 3](#ex3){: data-relation="weak" }. The only difference is that since $\Gal(\overline{\mathbb{Q}}/\mathbb{Q})$ is infinite, the fiber has infinitely many points rather than two. 

Nevertheless, this example hints at some kind of finiteness for the fibers of an integral morphism; for instance, since $\Gal(\overline{\mathbb{Q}}/\mathbb{Q})$ is a profinite group ([\[Field Theory\] §Properties of Galois Groups, ⁋Proposition 5](/en/math/field_theory/properties_of_galois_extensions#prop5){: data-relation="weak" }), it is $0$-dimensional. This is a fact that holds for any integral morphism as well.

::: Proposition 4
Any non-empty fiber of an integral morphism $\varphi: X \rightarrow Y$ is always $0$-dimensional. 
:::
::: Proof
By definition, the fiber over a point in $Y$, denoted $y$, is given, via the residue field $\kappa(y)$ ([§Schemes, ⁋Definition 5](/en/math/scheme_theory/schemes#def5){: data-relation="required" }), by the base change along the inclusion map $\Spec \kappa(y) \rightarrow Y$ of $\varphi$:

$$\varphi^{-1}(y)=X\times_Y\Spec \kappa(y)$$

and since integral morphisms are preserved under base change ([§Fiber Products, ⁋Proposition 16](/en/math/scheme_theory/fiber_products#prop16){: data-relation="required" }),

$$\varphi^{-1}(y)=X\times_Y\Spec \kappa(y) \rightarrow \Spec \kappa(y)$$

is an integral morphism. Since an integral morphism is by definition an affine morphism, it suffices to show that for an integral morphism $\Spec B \rightarrow \Spec \kappa(y)$, we have $\dim \Spec B=\dim B=0$. That is, for any integral extension $\kappa(y) \rightarrow B$, we must show that no chain of prime ideals of $B$

$$\mathfrak{q}_1\subsetneq \mathfrak{q}_2$$

can exist. This is a consequence of [\[Commutative Algebra\] §Integral Extensions and Ideals, ⁋Corollary 4](/en/math/commutative_algebra/lying_over_and_going_up#cor4){: data-relation="required" }. 
:::

Geometrically, this proposition shows that each fiber of an integral morphism does not have positive dimension. 

[\[Commutative Algebra\] §Integral Extensions and Ideals, ⁋Corollary 4](/en/math/commutative_algebra/lying_over_and_going_up#cor4){: data-relation="required" }, used in the proof of the proposition above, also holds for any integral extension $A\hookrightarrow B$. By this, contracting a chain of prime ideals of $B$ to $A$ remains strict, so $\dim B\leq\dim A$, and conversely, by lying over and going up from [\[Commutative Algebra\] §Integral Extensions and Ideals, ⁋Proposition 1](/en/math/commutative_algebra/lying_over_and_going_up#prop1){: data-relation="required" }, a chain of prime ideals of $A$ can be lifted to $B$, so $\dim A\leq\dim B$. Therefore, more generally, the following holds.

::: Proposition 5
For any integral extension $\phi:A \hookrightarrow B$,

$$\dim\Spec A=\dim\Spec B$$

always holds. 
:::

In particular, for any integral domain $A$ and its normalization $\tilde{A}$, since the extension $A\hookrightarrow\tilde{A}$ is integral, by [Proposition 5](#prop5){: data-relation="weak" } we have $\dim\Spec\tilde{A}=\dim\Spec A$. Here, the normalization $\tilde{A}$ is the extension of $A$ to be integrally closed in its field of fractions $\Frac(A)$, that is, the extension obtained by adjoining all elements of $\Frac(A)$ that are integral over $A$ to $A$ ([\[Commutative Algebra\] §Integral Extensions, ⁋Definition 3](/en/math/commutative_algebra/integral_extension#def3){: data-relation="weak" }). By definition, $A\subseteq\tilde{A}\subseteq\Frac(A)$, so $\Frac(\tilde{A})=\Frac(A)$; that is, normalization preserves the function field of $A$.

::: Example 6
In the discussion above, we have seen that normalization preserves the function field. Geometrically, when $A$ is the coordinate ring of an affine variety over $\mathbb{K}$, this means that the two spaces obtained by normalization are birational ([\[Algebraic Varieties\] §Rational Maps, ⁋Proposition 10](/en/math/algebraic_varieties/rational_maps#prop10){: data-relation="weak" }). That is, outside of certain negligible loci, the normalization is identical to the original space. 

Where the normalization actually differs is the locus where $A$ is not integrally closed, namely the non-normal locus. This is contained in the singular locus, but in general they are not equal. For example, the quadric cone $\mathbb{K}[\x,\y,\z]/(\x\y-\z^2)$ is a $2$-dimensional domain singular at the origin, but since it is normal, the normalization is the identity map and the singular point remains as it is. However, in the case of curves, that is, in dimension $1$, a normal local ring is precisely a regular local ring, so the non-normal locus coincides with the singular locus. As a typical example, let us look at the cusp in [\[Algebraic Varieties\] §Tangent Spaces and Smoothness, ⁋Example 7](/en/math/algebraic_varieties/tangent_spaces_and_smoothness#ex7){: data-relation="weak" }:

$$A=\mathbb{K}[\x,\y]/(\y^2-\x^3)\cong\mathbb{K}[t^2,t^3]$$

. To find the field of fractions of $A$, using $t=\y/\x$ shows that $\Frac(A)=\mathbb{K}(t)$; here the element $t\in\Frac(A)$ satisfies $t^2=\x\in A$, so it is integral over $A$. Therefore, the extension obtained by adjoining $t$,

$$A[t]=\mathbb{K}[t^2,t^3,t]=\mathbb{K}[t]$$

is an integral extension of $A$, and since $A[t]$ is a UFD, it is integrally closed by [\[Commutative Algebra\] §Integral Extensions, ⁋Proposition 9](/en/math/commutative_algebra/integral_extension#prop9){: data-relation="required" }, so this is precisely the normalization $\tilde{A}$. 

Now let us examine what this means geometrically. We must first examine the map between the spaces induced by the above integral extension $A\rightarrow A[t]$,

$$\Spec A[t]\rightarrow \Spec A$$

. First, looking at the singular point of the curve $\Spec A$, namely the origin $\mathfrak{m}=(t^2,t^3)\in\Spec A$, the fiber of the above map at this point is given by the following pullback diagram

{% diagram Math/Scheme_Theory/Dimension_Schemes-2.svg width="17.35em" alt="cusp-fiber" %}

that is, by the following scheme

$$\Spec(A[t]\otimes_A A/\mathfrak{m})=\Spec(A[t]/(t^2,t^3))=\Spec(A[t]/(t^2))$$

. That is, the fiber itself is a single point, but the scheme structure given on it is non-reduced; on the other hand, the origin of $\Spec A$, namely $\Spec A/\mathfrak{m}$, is a reduced single point as the spectrum of a field, so the above fiber cannot be equal to this point. In contrast, on the open set $D(\x)$ away from the origin, $\x=t^2$ becomes invertible, so $t=t^3\cdot(t^2)^{-1}$ is contained in it, and

$$A[\x^{-1}]=\tilde{A}[\x^{-1}]$$

so that the two schemes are completely identical outside the origin. 

To examine what happens at the origin more algebraically, let us look at the local rings. First, the preimage of the origin of $\Spec A$, which is $\mathfrak{m}$, is by definition a prime ideal containing $\mathfrak{m}$ in $A[t]$, and the prime ideal containing $\mathfrak{m}A[t]=(t^2)$ is the radical $(t)$ of this ideal. Then the local ring of $A[t]$ at the origin $(t)$ is

$$A[t]_{(t)}=\mathbb{K}[t]_{(t)}$$

whereas the local ring at the origin of the original curve $\Spec A$ is

$$A_{\mathfrak{m}}=\mathbb{K}[t^2,t^3]_{(t^2, t^3)}$$

. Comparing these reveals algebraically what normalization does at the origin. Even though $A_{\mathfrak{m}}$ is a $1$-dimensional local ring, its maximal ideal cannot be generated by a single element and requires the two elements $t^2$ and $t^3$, so it is not a regular local ring ([\[Commutative Algebra\] §Krull Dimension, ⁋Definition 12](/en/math/commutative_algebra/Krull_dimension#def12){: data-relation="required" }). Indeed, $\mathfrak{m}/\mathfrak{m}^2$ is spanned by the images of $t^2$ and $t^3$ as a $2$-dimensional vector space, which is the same phenomenon as the tangent space at the origin of the cusp being computed as $2$-dimensional (strictly greater than the dimension of the curve) in [\[Algebraic Varieties\] §Tangent Spaces and Smoothness, ⁋Example 7](/en/math/algebraic_varieties/tangent_spaces_and_smoothness#ex7){: data-relation="weak" }. On the other hand, the local ring $A[t]_{(t)}=\mathbb{K}[t]_{(t)}$ of the normalization is a regular local ring whose maximal ideal is generated by the single element $t$. In other words, the normalization straightens out the cusp by replacing the singular local ring $A_{\mathfrak{m}}$ with the regular local ring $A[t]_{(t)}$.
:::

For any integral scheme $X$, we can define the normalization in the same way. Cover $X$ by affine opens $\Spec A_i$. Since $X$ is integral, it has a unique generic point $\xi$, and this point corresponds in each $\Spec A_i$ to the minimal prime of the domain $A_i$, namely $(0)$, so that its stalk is $\Frac(A_i)$. Since the stalk $\mathcal{O}_{X,\xi}$ is the same regardless of which affine open it is computed on, all $\Frac(A_i)$ coincide with a single common function field $K(X)$ ([§Properties of Scheme Morphisms, §§Rational Maps](/en/math/scheme_theory/properties_of_scheme_morphisms#rational-maps){: data-relation="weak" }), and on each piece we can take the normalization of $A_i$ in $K(X)$, namely $\tilde{A}_i$. Since normalization commutes with localization ([\[Commutative Algebra\] §Integral Extensions, ⁋Proposition 12](/en/math/commutative_algebra/integral_extension#prop12){: data-relation="required" }), the restrictions of each $\Spec\tilde{A}_i$ to the overlap $\Spec A_i\cap\Spec A_j$ agree with each other, and therefore they glue together into a single scheme $\tilde{X}$ to define the normalization morphism $\tilde{X}\rightarrow X$. This morphism is an integral morphism since $A_i\hookrightarrow\tilde{A}_i$ is an integral extension affine-locally, and since $\dim\Spec\tilde{A}_i=\dim\Spec A_i$ on each piece by [Proposition 5](#prop5){: data-relation="required" }, we obtain $\dim\tilde{X}=\dim X$ from the proof of [Proposition 2](#prop2){: data-relation="required" }. 

We now define codimension. 

::: Definition 7
For a topological space $X$ and an irreducible subset $Y$, we define the *codimension* of $Y$ in $X$, denoted by $\codim_XY$, to be the supremum of the lengths of strictly descending chains of irreducible closed subsets of $X$,

$$Z_n\supsetneq Z_{n-1}\supsetneq\cdots\supsetneq Z_0=\cl_X(Y)$$

. 
:::

Then we can see that for a ring $A$, the codimension of a prime ideal $\mathfrak{p}$ is equal to the codimension in $\Spec A$ of the point $\mathfrak{p}$ ([\[Commutative Algebra\] §Krull Dimension, ⁋Definition 2](/en/math/commutative_algebra/Krull_dimension#def2){: data-relation="required" }).

::: Proposition 8
For $X$, an irreducible closed subset $Y$, and the generic point of $Y$, denoted by $\eta$, the identity $\codim_X Y=\dim \mathcal{O}_{X,\eta}$ holds.
:::
::: Proof
Since $Y$ has generic point $\eta$, by definition $\codim_XY$ and $\codim_X\{\eta\}$ are equal. Now, around $\eta$, choose an arbitrary affine open subset $U\cong\Spec A$, and suppose that under this isomorphism, $\eta\in U$ corresponds to $\mathfrak{p}_\eta\in \Spec A$. Then from [\[Topology\] §Dimension, ⁋Proposition 15](/en/math/topology/dimension#prop15){: data-relation="required" }, we know that there is a one-to-one correspondence between irreducible closed subsets intersecting $U$ in $X$ and irreducible closed subsets of $U$. That is, $\codim_X\{\eta\}=\codim_U \mathfrak{p}_\eta$. Now from [§The Spectrum, ⁋Proposition 16](/en/math/scheme_theory/spectrums#prop16){: data-relation="required" }, we obtain the desired result. 
:::

More generally, after defining codimension in [\[Commutative Algebra\] §Krull Dimension, ⁋Definition 2](/en/math/commutative_algebra/Krull_dimension#def2){: data-relation="required" }, we proved the inequality

$$\dim \mathfrak{a}+\codim \mathfrak{a}\leq \dim A$$

; if we use [\[Topology\] §Dimension, ⁋Proposition 15](/en/math/topology/dimension#prop15){: data-relation="required" } instead of [\[Commutative Algebra\] §Localization, ⁋Proposition 8](/en/math/commutative_algebra/localization#prop8){: data-relation="required" } used there, we can verify that for a scheme $X$ and an irreducible closed subset of $X$, say $Y$, the following inequality

$$\dim Y+\codim_XY\leq \dim X$$

holds. However, similarly, equality does not hold in general. 

## Noether Normalization

Now we prove the following important result.

::: Theorem 9 (Noether normalization lemma)
Suppose we are given any field $\mathbb{K}$ and a finitely generated $\mathbb{K}$-algebra $A$. If $A$ is an integral domain and 

$$\trdeg_\mathbb{K}\Frac(A)=n$$

then in $A$ there exist elements $x_1,\ldots, x_n$ that are algebraically independent and such that $A$ is a finite $\mathbb{K}[x_1,\ldots, x_n]$-module. 
:::
::: Proof
From the assumption that $A$ is a finitely generated $\mathbb{K}$-algebra, we can write

$$A=\mathbb{K}[y_1,\ldots, y_m]/\mathfrak{p}$$

Then, since the images of these $y_1,\ldots, y_m$ in $\Frac(A)$, as a field extension of $\mathbb{K}$, generate $\Frac(A)$, we must have $m\geq n$. 

Now if $m=n$, the images of the $y_i$ form a transcendence basis of $\Frac(A)$ and so in particular are algebraically independent, whence $\mathfrak{p}=0$, that is, $A=\mathbb{K}[y_1,\ldots, y_n]$. Indeed, any nonzero element of $\mathfrak{p}$ would give a nontrivial algebraic relation among the $y_i$, which would make the transcendence degree strictly less than $n$. That is, in this case the $y_i$ are precisely the desired elements, so there is nothing further to prove. To prove the given claim, suppose now that $m>n$, and assume that whenever $n\leq k< m$, the theorem holds for $k$. Then from the assumption $m>n$, the elements $y_1,\ldots, y_m$ are algebraically dependent. That is, satisfying the equation

$$f(y_1,\ldots, y_m)=0$$

there exists a polynomial over $\mathbb{K}$ in $m$ variables,

$$f(\x_1,\ldots, \x_m)=\sum \alpha_{d_1d_2\cdots d_m}\x_1^{d_1}\cdots\x_m^{d_m}\in \mathbb{K}[\x_1,\ldots, \x_m]\tag{$\ast$}$$

Now, for integers $r_1,\ldots, r_{m-1}$, by the equations

$$z_1=y_1-y_m^{r_1},\quad z_2=y_2-y_m^{r_2},\quad\ldots\quad,\quad z_{m-1}=y_{m-1}-y_m^{r_{m-1}}$$

we define the elements $z_1,\ldots, z_{m-1}$. Then by definition,

$$f(z_1+y_m^{r_1},\ldots, z_{m-1}+y_m^{r_{m-1}}, y_m)=0\tag{$\ast\ast$}$$

holds. Now, in equation ($\ast$), into each constituent monomial of $f$, $\alpha_{d_1d_2\cdots d_m}\x_1^{d_1}\cdots\x_m^{d_m}$, substituting

$$\x_1=z_1+y_m^{r_1},\quad \ldots\quad,\quad \x_{m-1}=z_{m-1}+y_m^{r_{m-1}},\quad \x_m=y_m$$

and expanding, the result will be a power of $y_m$ with constant coefficient,

$$\alpha_{d_1d_2\cdots d_m}y_m^{r_1d_1+\cdots+r_{m-1}d_{m-1}+d_m}$$

together with other terms containing $z_k$. Now, from $f$, taking the maximum of the exponents $d_j$ that actually appear, let $r$ be a strictly greater integer and set $r_i=r^i$. Then for each distinct monomial of $f$, the exponent

$$r_1d_1+\cdots+r_{m-1}d_{m-1}+d_m=d_m+d_1r+\cdots+d_{m-1}r^{m-1}$$

takes a distinct value by the uniqueness of base-$r$ expansions, so among the terms of this form, exactly one remains as the highest-degree term. Since its coefficient is an element of $\mathbb{K}$ not equal to $0$, we can divide both sides by it, and thus the equality ($\ast\ast$) above shows that $y_m$ is integrally dependent over $z_1,\ldots, z_{m-1}$.

Meanwhile, with $z_1,\ldots, z_{m-1}$ generating inside $A$ the $\mathbb{K}$-subalgebra $A'$, that is, viewing ($\ast\ast$) as a single-variable polynomial in $y_m$, consider the subring of $A$ containing its coefficients, the $\mathbb{K}$-subalgebra $A'$. By the argument above, $A$ is a finite $A'$-module, and since $\Frac(A)$ is an algebraic extension of $\Frac(A')$, we have $\trdeg_\mathbb{K}\Frac(A')=n$. Then since $A'$ is an integral domain generated by $m-1$ elements, the induction hypothesis implies the existence of $x_1,\ldots, x_n\in A'$ satisfying the desired conditions, and since $A'$ is a finite $\mathbb{K}[x_1,\ldots, x_n]$-module, $A$ is also a finite $\mathbb{K}[x_1,\ldots, x_n]$-module.
:::

Geometrically, setting $A=\mathbb{K}[y_1,\ldots, y_m]/\mathfrak{p}$ is equivalent to saying that $\Spec A$ is an integral closed subscheme of the affine space $\mathbb{A}^m_\mathbb{K}$, so the finite ring homomorphism $\mathbb{K}[x_1,\ldots, x_n] \rightarrow \mathbb{K}[y_1,\ldots, y_m]/\mathfrak{p}$ obtained as a result of the above theorem is geometrically equivalent to finding a finite scheme morphism $\Spec A \rightarrow \Spec \mathbb{K}[x_1,\ldots, x_n]$. Now since the finite extension $\mathbb{K}[x_1,\ldots, x_n] \rightarrow A$ is an integral extension, [Proposition 5](#prop5){: data-relation="required" } gives $\dim A=\dim \mathbb{K}[x_1,\ldots, x_n]$, and thus by [\[Commutative Algebra\] §System of Parameters, ⁋Corollary 11](/en/math/commutative_algebra/system_of_parameters#cor11){: data-relation="required" } we obtain the following result.

::: Proposition 10
Let $\mathbb{K}$ be any field, and let $A$ be a finitely generated $\mathbb{K}$-algebra. If $A$ is an integral domain, then $\dim\Spec A=\trdeg_\mathbb{K} \Frac(A)$ holds. 
:::

Translating [Proposition 10](#prop10){: data-relation="required" } into the language of points tells us what the closed points of a scheme locally of finite type over $\mathbb{K}$ are, and how many such points there are.

::: Proposition 11
Over a field $\mathbb{K}$, for a scheme $X$ locally of finite type, the following hold:

1. A point $x\in X$ is a closed point if and only if $\kappa(x)$ is a finite extension of $\mathbb{K}$.
2. Any non-empty locally closed subset of $X$ contains a closed point of $X$, and hence the closed points are dense in it.
:::
::: Proof
First, we observe that in $X$, for any affine open subset $\Spec S$, $S$ is a finitely generated $\mathbb{K}$-algebra. ([§Properties of Scheme Morphisms, ⁋Lemma 13](/en/math/scheme_theory/properties_of_scheme_morphisms#lem13){: data-relation="required" })

For one direction of the first claim, suppose that $\kappa(x)$ is a finite extension of $\mathbb{K}$, and choose an affine open neighborhood of $x$, $\Spec S$, and the prime ideal corresponding to $x$, $\mathfrak{q}$. Then $S/\mathfrak{q}$ is an integral domain with fraction field $\kappa(x)$ and a finitely generated $\mathbb{K}$-algebra, so by [Proposition 10](#prop10){: data-relation="required" } we have $\dim S/\mathfrak{q}=\trdeg_\mathbb{K}\kappa(x)=0$; and since an integral domain of dimension $0$ is a field, $\mathfrak{q}$ is a maximal ideal, so $x$ is a closed point of $\Spec S$. Now if we choose $y\in\cl(\{x\})$, then any affine open subset containing $y$ also contains $x$, so applying the above argument to one such subset yields $y=x$, and thus $x$ is a closed point of $X$. Conversely, if $x$ is a closed point of $X$, then in an affine open neighborhood of $x$, $\Spec S$, the subset $\{x\}$ is closed, so the corresponding prime ideal is a maximal ideal; and since a field is a Jacobson ring because its unique prime ideal $(0)$ is maximal, by [\[Commutative Algebra\] §The Nullstellensatz, ⁋Theorem 4](/en/math/commutative_algebra/nullstellensatz#thm4){: data-relation="required" }, $\kappa(x)$ is a finite extension of $\mathbb{K}$.

For the second claim, let us write a non-empty locally closed subset as $U\cap C$. If we choose, contained in $U$, an affine open subset $\Spec S$ containing a point of this set, then $C$ is still closed in it, so $(U\cap C)\cap \Spec S$ is, for some ideal $I$, the set $V(I)$; and since this is non-empty, containing $I$ there exists a maximal ideal $\mathfrak{m}$. Then the point given by $\mathfrak{m}$ belongs to $U\cap C$, and since its residue field is a finite extension of $\mathbb{K}$ ([\[Commutative Algebra\] §The Nullstellensatz, ⁋Theorem 4](/en/math/commutative_algebra/nullstellensatz#thm4){: data-relation="required" }), it is a closed point of $X$ by the first claim. Finally, any non-empty relatively open subset of $U\cap C$ is again a locally closed subset of $X$, so the same argument yields a closed point in it, and therefore the closed points are dense in $U\cap C$.
:::

The most crucial results used in the claims above are, of course, those of [\[Commutative Algebra\] §Integral Extensions and Ideals](/en/math/commutative_algebra/lying_over_and_going_up){: data-relation="weak" }. Meanwhile, using the dimension formula [\[Commutative Algebra\] §Noether Normalization, ⁋Theorem 4](/en/math/commutative_algebra/noether_normalization#thm4){: data-relation="required" }, we obtain the following.

::: Proposition 12
Let a field $\mathbb{K}$ and a finitely generated $\mathbb{K}$-algebra $A$ be given. If $A$ is an integral domain and $f\in A$ is a nonzero non-unit, then $\dim A/(f)=\dim A-1$.
:::
::: Proof
Containing $(f)$, choose a minimal prime of $A$, denoted $\mathfrak{p}$. By [\[Commutative Algebra\] §Krull Dimension, ⁋Theorem 6](/en/math/commutative_algebra/Krull_dimension#thm6){: data-relation="required" }, $\operatorname{ht}\mathfrak{p}\leq 1$, and since $A$ is a domain and $f\neq 0$, from $(0)\subsetneq\mathfrak{p}$ we have $\operatorname{ht}\mathfrak{p}\geq 1$. Thus $\operatorname{ht}\mathfrak{p}=1$, and by the dimension formula ([\[Commutative Algebra\] §Noether Normalization, ⁋Theorem 4](/en/math/commutative_algebra/noether_normalization#thm4){: data-relation="required" }), $\dim A/\mathfrak{p}=\dim A-1$. Now $\dim A/(f)$ is given by the maximum over the minimal primes of $(f)$, denoted $\mathfrak{p}$, of $\dim A/\mathfrak{p}$; since every minimal prime has height $1$ as above, these values are all $\dim A-1$, and therefore $\dim A/(f)=\dim A-1$.
:::

## Principal ideal theorem

Earlier, for an affine integral $\mathbb{K}$-scheme $X=\Spec A$ of finite type, we saw that given in $A$ a nonzero non-unit $f$, the closed subscheme $Z(f)$ defined by it has dimension one less than that of $X$. While this is certainly a useful result, we can also examine the result in a more general setting as follows.

::: Proposition 13
Given a locally Noetherian scheme $X$, and on $X$ a function $f$, every irreducible component of $Z(f)$ has codimension $0$ or codimension $1$.
:::
::: Proof
Let $W$ be an irreducible component of $Z(f)$, and let $w$ be the generic point of $W$. Now, choosing around $w$ an affine open subset $U\cong\Spec A$, since $X$ is locally Noetherian we may take $A$ to be a Noetherian ring, and suppose under this isomorphism $w$ corresponds to $\mathfrak{p}\in\Spec A$. By the correspondence in [\[Topology\] §Dimension, ⁋Proposition 15](/en/math/topology/dimension#prop15){: data-relation="required" }, $W\cap U$ is an irreducible component of $Z(f\vert_U)$, so $\mathfrak{p}$ is a minimal prime ideal containing the principal ideal generated by $f\vert_U\in A$. Therefore, by [\[Commutative Algebra\] §Krull Dimension, ⁋Theorem 6](/en/math/commutative_algebra/Krull_dimension#thm6){: data-relation="required" }, $\codim\mathfrak{p}\leq 1$.

Meanwhile, since the stalk depends only on open neighborhoods of $w$, we have $\mathcal{O}_{U,w}=\mathcal{O}_{X,w}$, and since $W$ and $W\cap U$ are irreducible closed subsets of $X$ and $U$ respectively, both having $w$ as their generic point, applying [Proposition 8](#prop8){: data-relation="required" } twice yields

$$\codim_XW=\dim\mathcal{O}_{X,w}=\dim\mathcal{O}_{U,w}=\codim_U(W\cap U)$$

Now, since in $\Spec A$ the codimension of the point $\mathfrak{p}$ equals that in the ring $A$, namely $\codim\mathfrak{p}$ ([\[Commutative Algebra\] §Krull Dimension, ⁋Definition 2](/en/math/commutative_algebra/Krull_dimension#def2){: data-relation="required" }), we ultimately have $\codim_XW=\codim\mathfrak{p}\leq 1$.
:::

That $\codim_XW=0$ is equivalent to $W$ being an irreducible component of $X$ itself, that is, to $f$ vanishing identically on that component. Therefore, if $f$ does not vanish identically on any irreducible component of $X$, every component of $Z(f)$ has codimension exactly $1$, which is the role played in [Proposition 12](#prop12){: data-relation="weak" } by the assumptions that $A$ is an integral domain and $f$ is nonzero.

---

**References**

**[AM]** M. F. Atiyah and I. G. Macdonald, *Introduction to commutative algebra*, Addison-Wesley, 1969.  
**[Vak]** R. Vakil, *The rising sea: Foundation of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/).
