---
title: "Sheaf Cohomology of Schemes"
description: "We lift sheaf cohomology, introduced on algebraic varieties, to quasi-coherent sheaves on arbitrary schemes, covering its definition as derived functors of the abelian sheaf category and Cech cohomology for affine covers, and showing that the two cohomologies agree on separated schemes via the vanishing theorem for quasi-coherent sheaves on affine schemes. We then recompute the cohomology of O(d) on projective space, prove finiteness and Serre vanishing for coherent sheaves on Noetherian projective schemes, obtain Serre's criterion characterizing ample invertible sheaves by the vanishing of higher cohomology, and introduce the Euler characteristic and Hilbert polynomial to define the degree of a projective subscheme."
excerpt: "Cohomology of quasi-coherent sheaves, Serre vanishing, ampleness criterion, and Hilbert polynomials"

categories: [Math / Scheme Theory]
permalink: /en/math/scheme_theory/sheaf_cohomology_of_schemes
sidebar: 
    nav: "scheme_theory-en"

date: 2026-06-21
weight: 18
translated_at: 2026-08-02T05:45:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-10-29T23:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
In [\[Algebraic Varieties\] §Sheaf Cohomology](/en/math/algebraic_varieties/sheaf_cohomology){: data-lid="43wxo" }, we defined sheaf cohomology on (quasi-projective) varieties via derived functors, and examined how to compute the cohomology of quasi-coherent sheaves through comparison with Čech cohomology and Leray's theorem. Now that we have organized quasi-coherent sheaves in the language of schemes, we can do the same for schemes. The key point is that the quasi-projective hypothesis in the above post was excessive; once we show separatedness and the vanishing theorem for quasi-coherent sheaves on affine schemes, we can prove the same results as in that post.

As with the previous few posts, the goal of this post is to lift the content already treated in [\[Algebraic Varieties\] §Sheaf Cohomology](/en/math/algebraic_varieties/sheaf_cohomology){: data-lid="3yvpf" } to schemes; while we will carry out some calculations directly, our main task will be translating into this language, leaving most of the calculations to those posts.

## Cohomology as a Derived Functor

On a scheme $X$ as well, the category $\Sh(X)$ of sheaves of abelian groups is an abelian category and has enough injectives. Thus we can define the derived functor of the global section functor in the same manner as in [\[Algebraic Varieties\] §Sheaf Cohomology](/en/math/algebraic_varieties/sheaf_cohomology){: data-lid="mokuj" }. Just as there, our primary interest is always quasi-coherent sheaves, but both the definition and the resolution take place inside $\Sh(X)$.

::: Definition 1
For a sheaf $\mathcal{F}$ on a scheme $X$, by taking the right derived functor of the global section functor $\Gamma(X, -):\Sh(X) \rightarrow \Ab$ ([\[Homological Algebra\] §Derived Functors, ⁋Definition 9](/en/math/homological_algebra/derived_functors#def9){: data-lid="9hwny" }), we define the $i$-th *sheaf cohomology* as

$$H^i(X, \mathcal{F})=R^i\Gamma(X, -)(\mathcal{F})=\frac{\ker\bigl(\Gamma(X, \mathcal{I}^i) \rightarrow \Gamma(X, \mathcal{I}^{i+1})\bigr)}{\im\bigl(\Gamma(X, \mathcal{I}^{i-1}) \rightarrow \Gamma(X, \mathcal{I}^i)\bigr)}$$

Here, $0 \rightarrow \mathcal{F} \rightarrow \mathcal{I}^\bullet$ is an injective resolution in $\Sh(X)$.
:::

This definition is nothing more than transferring [\[Algebraic Varieties\] §Sheaf Cohomology, ⁋Definition 1](/en/math/algebraic_varieties/sheaf_cohomology#def1){: data-lid="bdg58" } to an arbitrary scheme, and formal properties, including the fact that this definition is independent of the choice of $\mathcal{I}^\bullet$, all follow from standard arguments in homological algebra. In particular, $H^0(X, \mathcal{F})=\Gamma(X, \mathcal{F})$, and a short exact sequence of sheaves induces a long exact sequence.

Meanwhile, since $\Gamma(X, -)$ is a functor on $\Sh(X)$, $H^i(X, \mathcal{F})$ is initially obtained only as an abelian group; however, when $\mathcal{F}$ is an $\mathcal{O}_X$-module, it acquires a $\Gamma(X, \mathcal{O}_X)$-module structure. For each $a\in\Gamma(X, \mathcal{O}_X)$, multiplication by $a$ is an endomorphism of $\mathcal{F}$ in $\Sh(X)$, so the functoriality of cohomology gives an endomorphism on $H^i(X, \mathcal{F})$, and this assignment preserves multiplication. Adding the fact that $R^i\Gamma(X, -)$ is an additive functor, the map $a\mapsto H^i(m_a)$ also preserves addition, yielding a ring homomorphism $\Gamma(X, \mathcal{O}_X) \rightarrow \End_\mathbb{Z}\bigl(H^i(X, \mathcal{F})\bigr)$, which gives the desired module structure.

::: Proposition 2
For a short exact sequence of sheaves

$$0 \rightarrow \mathcal{F}' \rightarrow \mathcal{F} \rightarrow \mathcal{F}'' \rightarrow 0$$

there exists a long exact sequence

$$0 \rightarrow H^0(X, \mathcal{F}') \rightarrow H^0(X, \mathcal{F}) \rightarrow H^0(X, \mathcal{F}'') \xrightarrow{\delta} H^1(X, \mathcal{F}') \rightarrow H^1(X, \mathcal{F}) \rightarrow \cdots$$
:::
::: Proof
Since $\Gamma(X, -)$ is a left exact functor and $\Sh(X)$ has enough injectives, the long exact sequence of the $\delta$-functor defined by the right derived functors holds directly.
:::

## Cohomology of Affine Schemes

On the other hand, we also introduced Čech cohomology in [\[Algebraic Varieties\] §Sheaf Cohomology](/en/math/algebraic_varieties/sheaf_cohomology){: data-lid="5pgvu" }; this is in fact a definition at the level of topological spaces, so it works on schemes without any modification. As in that post, while the definition of sheaf cohomology in [Definition 1](#def1){: data-lid="rlbuq" } captures its essence precisely, in order to actually use it, one usually passes to Čech cohomology. The result that made this possible was [\[Algebraic Varieties\] §Sheaf Cohomology, ⁋Proposition 12](/en/math/algebraic_varieties/sheaf_cohomology#prop12){: data-lid="fjzpr" }, which stated that the higher cohomology of quasi-coherent sheaves vanishes on affine varieties. The scheme version of this proposition is as follows.

::: Theorem 3 (Serre)
For a Noetherian ring $A$, the affine scheme $X=\Spec A$ defined by it, and a quasi-coherent sheaf $\mathcal{F}=\widetilde{M}$ on it,

$$H^i(X, \mathcal{F})=0 \qquad (i>0)$$

holds.
:::
::: Proof
By [§Quasi-Coherent Sheaves, ⁋Theorem 9](/en/math/scheme_theory/quasicoherent_sheaves#thm9){: data-lid="wzd4l" }, $\QCoh(\Spec A)$ is equivalent to $\rMod{A}$, so $\mathcal{F}=\widetilde{M}$ for some $A$-module $M$. Since $\rMod{A}$ has enough injectives, let us take an injective resolution of $M$

$$0 \rightarrow M \rightarrow I^0 \rightarrow I^1 \rightarrow \cdots$$

Since the associated sheaf functor $\widetilde{(-)}$ is exact ([§Quasi-Coherent Sheaves, ⁋Proposition 6](/en/math/scheme_theory/quasicoherent_sheaves#prop6){: data-lid="zglxv" }),

$$0 \rightarrow \widetilde{M} \rightarrow \widetilde{I^0} \rightarrow \widetilde{I^1} \rightarrow \cdots$$

is a resolution of sheaves on $\Spec A$. Our claim is that each $\widetilde{I^k}$ is $\Gamma(\Spec A, -)$-acyclic; if this holds, then by [\[Algebraic Varieties\] §Sheaf Cohomology, ⁋Proposition 17](/en/math/algebraic_varieties/sheaf_cohomology#prop17){: data-lid="9uyp8" } we obtain

$$H^i(\Spec A, \widetilde{M})\cong H^i\bigl(\Gamma(\Spec A, \widetilde{I^\bullet})\bigr)=H^i(I^\bullet)$$

Here, the second equality follows from the fact that the global sections of the associated sheaf are the original module ([§Quasi-Coherent Sheaves, ⁋Definition 4](/en/math/scheme_theory/quasicoherent_sheaves#def4){: data-lid="n4vfi" }), and since $M \rightarrow I^\bullet$ is a quasi-isomorphism, the cohomology on the right vanishes for all $i>0$. Thus $H^i(\Spec A, \widetilde{M})=0$ ($i>0$).

It remains to show that for an injective $A$-module $I$, the associated sheaf $\widetilde{I}$ is acyclic. To this end, we show that $\widetilde{I}$ is flasque. ([\[Algebraic Varieties\] §Sheaf Cohomology, ⁋Proposition 16](/en/math/algebraic_varieties/sheaf_cohomology#prop16){: data-lid="togdz" }) Since every open subset of $\Spec A$ is of the form $U=\Spec A\setminus Z(\mathfrak{a})$, it suffices to show that for each of them, the restriction $\widetilde{I}(\Spec A)=I\rightarrow\widetilde{I}(U)$ is surjective. There is an exact sequence connecting the sections of a quasi-coherent sheaf with local cohomology

$$I\rightarrow\widetilde{I}(U)\rightarrow H^1_{\mathfrak{a}}(I)\rightarrow 0$$

where $H^i_{\mathfrak{a}}(M)=\varinjlim_n\Ext^i_A(A/\mathfrak{a}^n,M)$. Since $I$ is injective, for all $n$ we have $\Ext^1_A(A/\mathfrak{a}^n,I)=0$, so $H^1_{\mathfrak{a}}(I)=0$, and therefore the above restriction is surjective. Then for any two open subsets $V\subseteq U$, the map $I \rightarrow \widetilde{I}(V)$ factors through $\widetilde{I}(U)$, so $\widetilde{I}(U) \rightarrow \widetilde{I}(V)$ is also surjective, and hence $\widetilde{I}$ is flasque.
:::

The Noetherian hypothesis in [Theorem 3](#thm3){: data-lid="97nig" } is for convenience of proof; in fact the result holds for an arbitrary ring $A$. However, this goes beyond the scope of this post, so we omit the proof and use this general form only in [Corollary 4](#cor4){: data-lid="purjn" } and [Corollary 5](#cor5){: data-lid="qk3lk" } below, and in [Theorem 7](#thm7){: data-lid="vrria" } dealing with projective space over an arbitrary ring.

At any rate, the heart of this theorem is that affine schemes are *simple* spaces from the viewpoint of cohomology. That is, on an affine scheme all information about a quasi-coherent sheaf is contained in $H^0$, i.e., its global section module, and higher cohomology gives no new information. This is the algebraic-geometric phenomenon corresponding to a topological space being contractible from the viewpoint of Čech cohomology.

Passing [Theorem 3](#thm3){: data-lid="y8v8g" } to its relative form gives the following.

::: Corollary 4
For an affine morphism $f:X\rightarrow Y$ and a quasi-coherent sheaf $\mathcal{F}$ on $X$,

$$R^qf_\ast\mathcal{F}=0\qquad(q>0)$$

and for every $i$,

$$H^i(Y,f_\ast\mathcal{F})\cong H^i(X,\mathcal{F})$$

:::
::: Proof
$R^qf_\ast\mathcal{F}$ is the sheafification of the presheaf $V\mapsto H^q(f^{-1}(V),\mathcal{F}\vert_{f^{-1}(V)})$. If $V\subseteq Y$ is affine, then since $f$ is an affine morphism, $f^{-1}(V)$ is also affine, and since $\mathcal{F}\vert_{f^{-1}(V)}$ is a quasi-coherent sheaf, this cohomology vanishes for $q>0$ by [Theorem 3](#thm3){: data-lid="ndyjr" }. Since the affine open subsets form a basis for $Y$, $R^qf_\ast\mathcal{F}=0$. Therefore, in the Leray spectral sequence of [\[Algebraic Varieties\] §Sheaf Cohomology, ⁋Proposition 19](/en/math/algebraic_varieties/sheaf_cohomology#prop19){: data-lid="ayoz9" }, only the row with $q=0$ remains, giving the second isomorphism.
:::

From this we immediately obtain the Leray theorem for affine coverings at the level of schemes. [\[Algebraic Varieties\] §Sheaf Cohomology, ⁋Theorem 11](/en/math/algebraic_varieties/sheaf_cohomology#thm11){: data-lid="lun3p" } states that if $\mathcal{F}$ is acyclic on all finite intersections of the cover $\mathcal{U}$, then $\check{H}^p(\mathcal{U}, \mathcal{F})\cong H^p(X, \mathcal{F})$; since this is a theorem at the level of topological spaces, it applies directly to schemes as well. The only hypothesis to add here is separatedness, the condition that intersections of affines are again affine. ([§Valuation Rings, ⁋Definition 3](/en/math/scheme_theory/valuative_criteria#def3){: data-lid="v66wp" })

::: Corollary 5
For a separated scheme $X$, a quasi-coherent sheaf $\mathcal{F}$ on it, and an affine open cover $\mathcal{U}=\{U_i\}$, for all $p$,

$$\check{H}^p(\mathcal{U}, \mathcal{F})\cong H^p(X, \mathcal{F})$$

holds.
:::
::: Proof
By [\[Algebraic Varieties\] §Sheaf Cohomology, ⁋Theorem 11](/en/math/algebraic_varieties/sheaf_cohomology#thm11){: data-lid="6k1yz" }, it suffices to show that on any finite intersection of $\mathcal{U}$, $U_{i_0}\cap\cdots\cap U_{i_p}$, $\mathcal{F}$ is acyclic. Since $X$ is separated, the diagonal morphism $\Delta:X \rightarrow X\times_{\Spec \mathbb{Z}}X$ is a closed embedding, and therefore, for any two affine open subsets $U_i, U_j$, the intersection $U_i\cap U_j$ is again affine. Indeed, $U_i\cap U_j$ is the fiber product $U_i\times_X U_j$, which is isomorphic to the closed subscheme of the affine scheme $U_i\times_{\Spec \mathbb{Z}}U_j$ given by $\Delta^{-1}(U_i\times U_j)$, hence affine. Repeating the same argument, the finite intersection $U_{i_0}\cap\cdots\cap U_{i_p}$ is also an affine scheme. Then the restriction of $\mathcal{F}$ to this is a quasi-coherent sheaf on an affine scheme, so it is acyclic by [Theorem 3](#thm3){: data-lid="018pe" }, and thus the hypothesis of [\[Algebraic Varieties\] §Sheaf Cohomology, ⁋Theorem 11](/en/math/algebraic_varieties/sheaf_cohomology#thm11){: data-lid="dp5vn" } is satisfied.
:::

Therefore, on a separated scheme, derived functor cohomology is obtained directly by choosing a single affine covering and computing only the Čech complex. A morphism between affine schemes is always separated ([§Valuation Rings, ⁋Lemma 5](/en/math/scheme_theory/valuative_criteria#lem5){: data-lid="3xnxl" }), and projective schemes including $\mathbb{P}^n$ are also separated, so this corollary works for most schemes we actually deal with.

## Line Bundles on Projective Space

We now treat the cohomology of the line bundle $\mathcal{O}(d)$ on projective space at the scheme level, using Čech calculations for an affine covering. Just as we defined projective space over a ring $A$, using the *graded* ring $A[\x_0,\ldots, \x_n]$, as $\mathbb{P}^n_A=\Proj A[\x_0,\ldots, \x_n]$ ([§Projective Space and the Proj Construction, ⁋Definition 1](/en/math/scheme_theory/projective_schemes#def1){: data-lid="e9177" }), we must first define $\mathcal{O}(d)$ in the language of graded modules.

::: Definition 6
Suppose we are given $S_\bullet=A[\x_0,\ldots, \x_n]$ endowed with the standard grading, and let $S(d)$ be the shift of $S_\bullet$ by degree $d$, that is, with degrees given by

$$S(d)_m=S_{d+m}$$

as a graded $S_\bullet$-module. Then, on each chart of the standard affine cover of $\mathbb{P}_A^n=\Proj S_\bullet$,

$$\mathcal{U}=\{D_+(\x_i)=\Spec S_{(\x_i)}\}$$

we consider the localization $S(d)_{\x_i}$ and, viewing its degree $0$ part

$$M_i=\bigl(S(d)_{\x_i}\bigr)_0=\x_i^d\cdot S_{(\x_i)}$$

as an $S_{(\x_i)}$-module, define the associated sheaf $\widetilde{M_i}$; we call the quasi-coherent sheaf on $\mathbb{P}^n_A$ obtained by gluing these via natural identifications on overlaps the *twisting sheaf* $\mathcal{O}(d)$.
:::

In [\[Algebraic Varieties\] §Line Bundles and Vector Bundles, ⁋Example 12](/en/math/algebraic_varieties/line_bundles#ex12){: data-lid="yjpdw" }, for each standard open set where $\x_i\neq 0$, namely $D_+(\x_i)$, we specified a trivialization $\phi_i(s)=s\cdot\x_i^{-d}$, and, taking the transition functions $(\x_i/\x_j)^d$ obtained by comparing the two trivializations on overlaps as data, described $\mathcal{O}(d)$. In this description, the space formed by the sections over $D_+(\x_i)$ was $\x_i^d\cdot\mathcal{O}(D_+(\x_i))$. [Definition 6](#def6){: data-lid="r4i46" } above is a redefinition using this last space itself, directly using, over the coordinate ring of $D_+(\x_i)$, namely $S_{(\x_i)}$, the module $M_i=\x_i^d\cdot S_{(\x_i)}$. That these two data are identical can be verified by using [§Quasi-Coherent Sheaves, ⁋Definition 4](/en/math/scheme_theory/quasicoherent_sheaves#def4){: data-lid="2vj2s" } to check that the sections in [Definition 6](#def6){: data-lid="32cq6" } are precisely given by $\mathcal{O}(d)(D_+(\x_i))=M_i$. Here, shifting the grading to $S(d)$ is a notation to transcribe the part of $S_{\x_i}$ of degree $d$ to the degree $0$ part that each chart adopts as functions.

As we saw in [\[Algebraic Varieties\] §Line Bundles and Vector Bundles, ⁋Example 12](/en/math/algebraic_varieties/line_bundles#ex12){: data-lid="m6702" }, our basic motivation is that while homogeneous polynomials of degree $d$ are needed to express closed subschemes of projective space, they cannot be regarded as actual functions because fundamentally only their zero sets are well-defined, and the function values themselves are not well-defined. One way to resolve this is to take the open set where each coordinate $\x_i$ is not $0$, namely $D_+(\x_i)$, and then divide this polynomial by $\x_i^d$ so that it becomes degree $0$, treating it as a function on this open set. However, this amounts to choosing a non-canonical trivialization for each chart $D_+(\x_i)$, and since these choices differ from chart to chart they are not compatible on overlaps, so they still cannot become global sections of $\mathcal{O}_{\mathbb{P}^n_A}$. Yet if we define $\mathcal{O}(d)$ as above, gathering these *functions* chart by chart gives a global section of this sheaf, and that section is the original polynomial itself. Also, since $M_i$ is generated by $\x_i^d$ as a rank $1$ free $S_{(\x_i)}$-module and the transition functions $(\x_i/\x_j)^d$ are invertible, this sheaf is an invertible sheaf ([§Quasi-Coherent Sheaves, ⁋Definition 12](/en/math/scheme_theory/quasicoherent_sheaves#def12){: data-lid="17r16" }), and thus can also be interpreted as the line bundle $\mathcal{O}(d)$. On the other hand, this way of describing an object by data on each chart and comparisons on overlaps is precisely the material for a Čech complex. Therefore, the gluing of these data is determined exactly by the (Čech) cohomology of $\mathcal{O}(d)$.

::: Theorem 7 (Bott)
The cohomology of the line bundle $\mathcal{O}(d)$ on the projective space $\mathbb{P}^n_A$ over a ring $A$ is given by

$$H^q(\mathbb{P}^n_A, \mathcal{O}(d))=\begin{cases}A[\x_0,\ldots, \x_n]_d & q=0,\ d\geq 0 \\ A[\x_0^{-1},\ldots, \x_n^{-1}]_{-d-n-1} & q=n,\ d\leq -n-1 \\ 0 & \text{otherwise}\end{cases}$$

In particular, for $0<q<n$, it vanishes for all $d$.
:::
::: Proof
Since $\mathbb{P}^n_A$ is a separated scheme, by [Corollary 5](#cor5){: data-lid="uih9d" } the Čech cohomology with respect to the standard affine cover $\mathcal{U}=\{D_+(\x_i)\}$ is the derived functor cohomology. However, this Čech complex is literally the same as the one appearing in the proof of [\[Algebraic Varieties\] §Cohomology of Projective Space, ⁋Proposition 1](/en/math/algebraic_varieties/cohomology_of_projective_spaces#prop1){: data-lid="347fd" }. That is, on each intersection $D_+(\x_{i_0}\cdots\x_{i_p})$, the sections of $\mathcal{O}(d)$ are generated by monomials allowing only $\x_{i_0},\ldots, \x_{i_p}$ in the denominator and of degree $d$,

$$\x_0^{a_0}\cdots\x_n^{a_n}, \qquad \sum_{j=0}^n a_j=d,\quad a_j\geq 0\ \text{for}\ j\not\in\{i_0,\ldots, i_p\}$$

over $A$, and the coboundary map is also given by the same alternating sum formula. The proof there starts from the observation that the coboundary map does not change the exponent vector $a=(a_0,\ldots, a_n)$ of a monomial, and decomposes the Čech complex into subcomplexes for each $a$. Letting $N_{<0}(a)$ denote the set of positions with negative exponents, the above condition means that $\x^a$ being regular on $D_+(\x_{i_0}\cdots\x_{i_p})$ is equivalent to $N_{<0}(a)\subseteq\{i_0,\ldots, i_p\}$, so the subcomplex corresponding to $a$ is the cochain complex of the simplex formed by the subsets of indices containing $N_{<0}(a)$. Then $N_{<0}(a)$ contributes only to $q=0$ when it is empty, only to $q=n$ when it is the entire set, and contributes nothing in between, giving the three cases at once. This argument does not use the assumption that the coefficients form a field at all, using only that each subcomplex consists of free $A$-modules, so reading that proof literally with $A$-coefficients yields the result above.

Finally, the reason the space obtained for $q=n$, $d\leq -n-1$ is written as $A[\x_0^{-1},\ldots, \x_n^{-1}]_{-d-n-1}$ is the same as the explanation right after [\[Algebraic Varieties\] §Cohomology of Projective Space, ⁋Proposition 1](/en/math/algebraic_varieties/cohomology_of_projective_spaces#prop1){: data-lid="7jzn4" }. That is, if for monomials with all exponents at most $-1$ and of degree $d$ we substitute $\y_j=\x_j^{-1}$, they become monomials with all exponents at least $1$ and of degree $\lvert d\rvert$, and removing the common factor $\y_0\cdots\y_n$ from these yields a one-to-one correspondence with the space of "negative degree" monomials of degree $\lvert d\rvert-(n+1)=-d-n-1$.
:::

## Coherent Sheaves on Noetherian Projective Schemes

We now examine more generally the sheaf cohomology of a Noetherian projective scheme $X$ and a coherent sheaf $\mathcal{F}$ on it. There are two key results: one is that each $H^i(X, \mathcal{F})$ is finite-dimensional, and the other is Serre vanishing, which states that twisting $\mathcal{F}$ sufficiently makes higher cohomology vanish.

One of the tools we use for this is the existence of the line bundle $\mathcal{O}_X(1)$ defined on a projective scheme. By definition, a projective scheme $X$ gives a closed embedding $\iota: X\hookrightarrow \mathbb{P}^n$, and using this we can pull back from $\mathbb{P}^n$ the line bundle $\mathcal{O}_{\mathbb{P}^n}(1)$ to define

$$\mathcal{O}_X(1)=\mathcal{O}_{\mathbb{P}^n}(1)\vert_X=\iota^\ast \mathcal{O}_{\mathbb{P}^n}(1)$$

Here, the restrictions of the coordinates $\x_0\vert_X,\ldots, \x_n\vert_X$ globally generate $\mathcal{O}_X(1)$, and the morphism they define is precisely the inclusion $X\hookrightarrow\mathbb{P}^n_\mathbb{K}$, so we may just as well view this line bundle as the embedding itself. That is, $\mathcal{O}_X(1)$ is a very ample invertible sheaf ([§Divisors and Linear Systems, ⁋Definition 17](/en/math/scheme_theory/divisors_and_linear_systems#def17){: data-lid="kzhf5" }), and for any coherent sheaf $\mathcal{F}$ we write $\mathcal{F}(d)=\mathcal{F}\otimes_{\mathcal{O}_X}\mathcal{O}_X(d)$.

The key observation is that cohomology is preserved along the closed embedding $\iota:X\hookrightarrow\mathbb{P}^n$, that is, on $X$, for any quasi-coherent sheaf $\mathcal{F}$, we have

$$H^i(X, \mathcal{F})\cong H^i(\mathbb{P}^n, \iota_\ast\mathcal{F})\tag{$\ast$}$$

This is because the Čech complexes computing both sides are the same complex. Indeed, since a closed embedding is an affine morphism ([§Closed Subschemes, ⁋Proposition 3](/en/math/scheme_theory/closed_subschemes#prop3){: data-lid="3j7fw" }), each $U_i=\iota^{-1}(D_+(\x_i))$ is an affine scheme and $\{U_i\}$ is an affine open cover of $X$. On the other hand, by the definition of pushforward,

$$(\iota_\ast\mathcal{F})(D_+(\x_{i_0}\cdots\x_{i_p}))=\mathcal{F}\bigl(\iota^{-1}(D_+(\x_{i_0})\cap\cdots\cap D_+(\x_{i_p}))\bigr)=\mathcal{F}(U_{i_0}\cap\cdots\cap U_{i_p})$$

and the restriction maps also correspond to each other, so the Čech complex with respect to $\{U_i\}$ of $\mathcal{F}$ and the Čech complex with respect to $\mathcal{U}$ of $\iota_\ast\mathcal{F}$ are the same complex. But since both $X$ and $\mathbb{P}^n$ are projective schemes, they are separated, and $\iota_\ast\mathcal{F}$ is also quasi-coherent ([§Quasi-Coherent Sheaves, ⁋Theorem 16](/en/math/scheme_theory/quasicoherent_sheaves#thm16){: data-lid="3iyb5" }), so by [Corollary 5](#cor5){: data-lid="30nfy" } the cohomology of this single complex computes both sides simultaneously, yielding the isomorphism above.

The two theorems below both start from the fact that a coherent sheaf, when sufficiently twisted, is generated by global sections alone, so we establish this first.

::: Lemma 8
For a coherent sheaf $\mathcal{F}$ on the projective space $\mathbb{P}^n_\mathbb{K}$ over a field $\mathbb{K}$, $\mathcal{F}(d)$ is globally generated for sufficiently large $d\gg 0$.
:::
::: Proof
Let $S_\bullet=\mathbb{K}[\x_0,\ldots, \x_n]$ and consider the graded $S_\bullet$-module

$$\Gamma_\ast(\mathcal{F})=\bigoplus_{m\in\mathbb{Z}}\Gamma(\mathbb{P}^n, \mathcal{F}(m))$$

We first show the equality on each standard affine chart:

$$\Gamma(D_+(\x_j), \mathcal{F})=\Gamma_\ast(\mathcal{F})_{(\x_j)}$$

That is, we must show that every section on $D_+(\x_j)$ comes from a global twisted section, which means that given any section on $D_+(\x_j)$, multiplying by a sufficiently large power of $\x_j$ makes it come from a global section of $\mathbb{P}^n$.

This is obtained by checking chart by chart and then gluing. To shorten notation, write $U_i=D_+(\x_i)$. Fix $s\in\Gamma(U_j, \mathcal{F})$ and look at each $i$. Since $U_i\cap U_j$ is the principal open set in $U_i=\Spec S_{(\x_i)}$ obtained by inverting $\x_j/\x_i$, we obtain from [§Quasi-Coherent Sheaves, ⁋Proposition 5](/en/math/scheme_theory/quasicoherent_sheaves#prop5){: data-lid="d6vgv" } that

$$\Gamma(U_i\cap U_j, \mathcal{F})=\Gamma(U_i, \mathcal{F})_{\x_j/\x_i}$$

That is, $s\vert_{U_i\cap U_j}$ is $t_i\vert_{U_i\cap U_j}$ divided by $(\x_j/\x_i)^{e_i}$ for suitable $e_i\geq0$ and $t_i\in\Gamma(U_i, \mathcal{F})$, and therefore multiplying both sides by $\x_i^{e_i}(\x_j/\x_i)^{e_i}=\x_j^{e_i}$ gives

$$\x_j^{e_i}\cdot s\vert_{U_i\cap U_j}=(\x_i^{e_i}t_i)\vert_{U_i\cap U_j}$$

Then both sides of this equation are sections of $\mathcal{F}(e_i)$, the right side is the restriction of the section $\x_i^{e_i}t_i\in\Gamma(U_i, \mathcal{F}(e_i))$ defined on all of $U_i$, and thus $\x_j^{e_i}s$ extends to $U_i$. Now, since there are finitely many such charts, letting $e=\max e_i$ and setting

$$u_i=\x_j^{e-e_i}\x_i^{e_i}t_i\in\Gamma(U_i, \mathcal{F}(e))$$

we have $u_i\vert_{U_i\cap U_j}=\x_j^es\vert_{U_i\cap U_j}$ for all $i$. It remains to check whether $u_i$ and $u_{i'}$ obtained from two different charts agree on $U_i\cap U_{i'}$, that is, the cocycle condition; their difference is $0$ on $U_i\cap U_{i'}\cap U_j$, and since this open set is also obtained by inverting the ratio of $\x_j$ on $U_i\cap U_{i'}$, by the same localization equality as above a suitable power of $\x_j$ annihilates the difference. Again, since there are finitely many such pairs, taking a sufficiently large common integer $f$, the $\x_j^fu_i$ agree and glue to a single $t\in\Gamma(\mathbb{P}^n, \mathcal{F}(e+f))$, with $t\vert_{U_j}=\x_j^{e+f}s$.

Conversely, suppose $t/\x_j^m$ is $0$ on $U_j$ for $t\in\Gamma(\mathbb{P}^n, \mathcal{F}(m))$. Then for each $i$, the restriction of $t\vert_{U_i}$ to $U_i\cap U_j$ is $0$, so by the localization equality above there exists $q_i$ such that $(\x_j/\x_i)^{q_i}t\vert_{U_i}=0$. Since there are finitely many charts, letting $q=\max q_i$ gives $\x_j^qt=0$, and therefore $t/\x_j^m$ is already $0$ in $\Gamma_\ast(\mathcal{F})_{(\x_j)}$. This establishes the equality above.

Now, since the right-hand side $\Gamma_\ast(\mathcal{F})_{(\x_j)}$ is a finitely generated module over $S_{(\x_j)}$, on each chart its generators can be written in the form

$$m_{jk}/\x_j^{e_{jk}},\qquad m_{jk}\in\Gamma(\mathbb{P}^n, \mathcal{F}(e_{jk}))$$

Since there are finitely many charts and finitely many generators, $d_0=\max_{j,k}e_{jk}$ is well-defined, and then the elements $m_{jk}\x_j^{d_0-e_{jk}}\in\Gamma(\mathbb{P}^n, \mathcal{F}(d_0))$ obtained by multiplying each generator $m_{jk}$ by $\x_j^{d_0-e_{jk}}$ generate the stalks of $\mathcal{F}(d_0)$ on each $D_+(\x_j)$. Since these charts cover $\mathbb{P}^n$, $\mathcal{F}(d_0)$ is globally generated, and if $d\geq d_0$, then $\mathcal{F}(d)=\mathcal{F}(d_0)\otimes\mathcal{O}(d-d_0)$ is also globally generated.
:::

::: Theorem 9
For a Noetherian projective scheme $X$ over a field $\mathbb{K}$ and a coherent sheaf $\mathcal{F}$ on it, each $H^i(X, \mathcal{F})$ is a finite-dimensional $\mathbb{K}$-vector space, and is $0$ for sufficiently large $i$.
:::
::: Proof
By the isomorphism $(\ast)$ above, once we check that the quasi-coherent sheaf $\iota_\ast\mathcal{F}$ ([§Quasi-Coherent Sheaves, ⁋Theorem 16](/en/math/scheme_theory/quasicoherent_sheaves#thm16){: data-lid="hcown" }) is a coherent sheaf on $\mathbb{P}^n$, we may assume $X=\mathbb{P}^n_{\mathbb{K}}$. For this, it suffices to check only the finite type condition affine-locally: since $\iota$ is a closed embedding, on each chart $\iota_\ast\mathcal{F}$ is a finitely generated module over the $A$-algebra $A/I$ viewed as an $A$-module, and because $A \rightarrow A/I$ is surjective, lifting generators over $A/I$ to $A$ shows that the same elements generate over $A$ as well.

Thus, on $\mathbb{P}^n$, it suffices to prove the statement for a coherent sheaf $\mathcal{F}$. First, for sufficiently large cohomological dimension $i>n$, we have $H^i=0$, because $\mathbb{P}^n$ is covered by $n+1$ open sets, so already at the level of the Čech complex these terms are $0$.

We now prove the finiteness of the remaining terms by descending induction on $i$. Since we have already shown above that this is $0$ for large dimensions, it suffices to prove the inductive step. For any coherent sheaf $\mathcal{F}$, by [Lemma 8](#lem8){: data-lid="zl32s" }, for a suitable $d\gg 0$, $\mathcal{F}(d)$ is globally generated, so finitely many global sections give a surjection

$$\mathcal{O}_{\mathbb{P}^n}^{\oplus r} \twoheadrightarrow \mathcal{F}(d)$$

and twisting this by $\mathcal{O}(-d)$ yields $\mathcal{O}(-d)^{\oplus r}\twoheadrightarrow\mathcal{F}$. Since $\mathbb{P}^n$ is Noetherian, on each affine chart a submodule of a finitely generated module is again finitely generated ([\[Commutative Algebra\] §Basic Notions, ⁋Theorem 3](/en/math/commutative_algebra/basic_notions#thm3){: data-lid="edtzn" }), and therefore its kernel $\mathcal{K}$ is also of finite type, hence a coherent sheaf. Then in the long exact sequence of the short exact sequence of coherent sheaves

$$0 \rightarrow \mathcal{K} \rightarrow \mathcal{O}(-d)^{\oplus r} \rightarrow \mathcal{F} \rightarrow 0$$

if we look at

$$H^i(\mathbb{P}^n, \mathcal{O}(-d)^{\oplus r}) \rightarrow H^i(\mathbb{P}^n, \mathcal{F}) \rightarrow H^{i+1}(\mathbb{P}^n, \mathcal{K})$$

the left term is finite-dimensional by [Theorem 7](#thm7){: data-lid="0kuk5" }, and the right term is finite-dimensional by the induction hypothesis, so the middle term $H^i(\mathbb{P}^n, \mathcal{F})$ is also finite-dimensional.
:::

The key argument in the proof above is to twist a coherent sheaf sufficiently to make it globally generated, and then cover it by a free sheaf. From this, the finiteness of cohomology on $\mathbb{P}^n$ propagated along the long exact sequence to give the claim of the theorem. But [Theorem 7](#thm7){: data-lid="fk91z" } shows not only that cohomology is finite-dimensional in every degree, but also that higher-degree cohomology vanishes entirely, so developing the argument in this direction yields the following result.

::: Theorem 10 (Serre Vanishing)
For a Noetherian projective scheme $X$ over a field $\mathbb{K}$ and a coherent sheaf $\mathcal{F}$ on it, for sufficiently large $d\gg 0$,

$$H^i(X, \mathcal{F}(d))=0 \qquad (i>0)$$

holds. Moreover, for such $d$, $\mathcal{F}(d)$ is globally generated.
:::
::: Proof
As in [Theorem 9](#thm9){: data-lid="3uri2" }, by $(\ast)$ we may reduce to the case where $X=\mathbb{P}^n_{\mathbb{K}}$ and $\mathcal{O}_X(1)=\mathcal{O}(1)$. Since the statement involves twisting, the additional equality needed for this is

$$\iota_\ast(\mathcal{F}(d))\cong(\iota_\ast\mathcal{F})(d)$$ 

and since $\mathcal{O}_X(1)=\iota^\ast\mathcal{O}(1)$, this follows immediately from [§Quasi-Coherent Sheaves, ⁋Proposition 17](/en/math/scheme_theory/quasicoherent_sheaves#prop17){: data-lid="kgf0g" }.

Under this reduction, global generation is also carried over. This is because along a closed embedding, at $x\in X$ we have $(\iota_\ast\mathcal{G})_{\iota(x)}=\mathcal{G}_x$ and $\Gamma(\mathbb{P}^n, \iota_\ast\mathcal{G})=\Gamma(X, \mathcal{G})$, so if $(\iota_\ast\mathcal{F})(d)$ is globally generated, then $\mathcal{F}(d)$ is as well. Then [Lemma 8](#lem8){: data-lid="8rh3g" } provides, so that for each $d\geq d_0$ $\mathcal{F}(d)$ is globally generated, a $d_0$, so only the vanishing remains.

Now what remains is the vanishing, which, just as in [Theorem 9](#thm9){: data-lid="93fvo" }, we treat by descending induction on $i$. For $i>n$, from the number of charts we have $H^i=0$, so it suffices to show the induction step. For any $i\geq1$, from the globally generated property we can choose a surjection $\mathcal{O}^{\oplus r}\twoheadrightarrow\mathcal{F}(d_0)$ to obtain the following short exact sequence

$$0 \rightarrow \mathcal{K} \rightarrow \mathcal{O}^{\oplus r} \rightarrow \mathcal{F}(d_0) \rightarrow 0$$

where $\mathcal{K}$ is the kernel of this surjection and is a coherent sheaf for the same reason as in the proof of [Theorem 9](#thm9){: data-lid="v7phl" }. Now twisting this by $\mathcal{O}(d-d_0)$, we have

$$0 \rightarrow \mathcal{K}(d-d_0) \rightarrow \mathcal{O}(d-d_0)^{\oplus r} \rightarrow \mathcal{F}(d) \rightarrow 0$$

and consider the long exact sequence that this gives:

$$H^i(\mathbb{P}^n, \mathcal{O}(d-d_0)^{\oplus r}) \rightarrow H^i(\mathbb{P}^n, \mathcal{F}(d)) \rightarrow H^{i+1}(\mathbb{P}^n, \mathcal{K}(d-d_0))$$

By [Theorem 7](#thm7){: data-lid="k0b9j" }, if $d-d_0\gg0$ and $i>0$, the left-hand term is $0$. The right-hand term comes from applying the induction hypothesis to $\mathcal{K}$, and vanishing at $i+1$ holds for sufficiently large twists. Therefore, if $d$ is large enough to make both of these $0$, the middle term $H^i(\mathbb{P}^n, \mathcal{F}(d))$ vanishes. Now, since $i$ is finite from $1$ to $n$, to simultaneously guarantee vanishing for all $i>0$ we can choose a common $d_1$, and for $d\geq d_1$ we have $H^i(\mathbb{P}^n, \mathcal{F}(d))=0$ ($i>0$).
:::

This transfers the Serre vanishing of [\[Algebraic Varieties\] §Cohomology of Projective Space, ⁋Proposition 7](/en/math/algebraic_varieties/cohomology_of_projective_spaces#prop7){: data-lid="3si0f" } to the scheme level. The global generation obtained alongside this allows us to write any coherent sheaf as a quotient of a finite direct sum of $\mathcal{O}(-d)$'s, and repeating this yields a resolution by such sheaves.

## Cohomological Criterion for Ampleness

On the other hand, the crucial fact used to prove the results in the preceding section was that $\mathcal{O}_X(1)$ comes from an embedding of $X$ into projective space, that is, it is very ample. We already know from [\[Algebraic Varieties\] §Linear Systems, ⁋Definition 10](/en/math/algebraic_varieties/linear_systems#def10){: data-lid="6gv63" } that very ampleness and ampleness are closely related, and hence the (scheme version of) ampleness defined in [§Divisors and Linear Systems](/en/math/scheme_theory/divisors_and_linear_systems){: data-lid="43faj" } will also be related to this. First, the following holds.

::: Corollary 11
Over a field $\mathbb{K}$, on a Noetherian projective scheme $X$, a very ample invertible sheaf $\mathcal{L}$ is ample. ([§Divisors and Linear Systems, ⁋Definition 18](/en/math/scheme_theory/divisors_and_linear_systems#def18){: data-lid="gyrt7" })
:::
::: Proof
Since $\mathcal{L}$ is very ample, finitely many sections globally generating it define a locally closed embedding $\iota:X \rightarrow \mathbb{P}^N_\mathbb{K}$, and $\mathcal{L}\cong\iota^\ast\mathcal{O}(1)$. ([§Divisors and Linear Systems, §§Ample invertible sheaf](/en/math/scheme_theory/divisors_and_linear_systems#ample-invertible-sheaf){: data-lid="17hfi" }) Since $X$ is projective over $\mathbb{K}$, $\iota(X)$ is a closed set ([§Valuation Rings, ⁋Corollary 16](/en/math/scheme_theory/valuative_criteria#cor16){: data-lid="gbzpz" }), and hence $\iota$ is a closed embedding. Then $\mathcal{L}$ can play exactly the same role as $\mathcal{O}_X(1)$ in [Theorem 10](#thm10){: data-lid="ha2g2" }, so for any coherent sheaf $\mathcal{F}$ and all sufficiently large $d$, the sheaf $\mathcal{F}\otimes\mathcal{L}^{\otimes d}$ is globally generated. This is the definition of ampleness.
:::

However, the converse of this corollary does not hold. An ample invertible sheaf may lack enough sections to give an embedding, and to remedy this one must tensor it repeatedly to increase the number of sections. The following theorem tells us that this is always possible.

::: Theorem 12
Over a field $\mathbb{K}$, on a Noetherian projective scheme $X$, for an invertible sheaf $\mathcal{L}$, $\mathcal{L}$ is ample if and only if for some $m>0$, $\mathcal{L}^{\otimes m}$ is very ample.
:::
::: Proof
Suppose $\mathcal{L}^{\otimes m}$ is very ample. By [Corollary 11](#cor11){: data-lid="rs41o" }, $\mathcal{L}^{\otimes m}$ is ample, and by the second result of [§Divisors and Linear Systems, ⁋Proposition 19](/en/math/scheme_theory/divisors_and_linear_systems#prop19){: data-lid="i7n98" }, $\mathcal{L}$ is also ample.

Conversely, suppose $\mathcal{L}$ is ample. We must construct a locally closed embedding defined by global sections of a suitable power of $\mathcal{L}$. By definition, a suitable power of $\mathcal{L}$ is globally generated, and since such sections always give a morphism $X \rightarrow \mathbb{P}^M$, what we actually need to show is that this morphism gives an embedding.

Consider sections globally generating $\mathcal{L}^{\otimes k}$, namely $s_0,\ldots, s_M\in\Gamma(X, \mathcal{L}^{\otimes k})$, and the morphism $\varphi:X \rightarrow \mathbb{P}^M$ they define. This is the morphism pulling back the $\mathbb{P}^M$-coordinates $\x_i$ to $s_i$, from which the preimage of the standard chart $D_+(\x_i)$ is precisely the open set where $s_i$ does not vanish, namely $X_{s_i}$. Since being a closed embedding is a local property on the target, it suffices to show that the morphisms

$$\varphi\vert_{X_{s_i}}: X_{s_i} \rightarrow D_+(\x_i)$$

are closed embeddings. Our claim is that if we choose the above sections very well, then $X_{s_i}$ becomes an affine scheme, so the above closed embedding is a morphism between affine schemes, and thus this determination reduces to the surjectivity of the corresponding ring homomorphism. Here, the coordinate ring of $D_+(\x_i)$ is the polynomial ring generated by the ratios $\x_j/\x_i$, and the ring homomorphism corresponding to $\varphi\vert_{X_{s_i}}$ sends them to $s_j/s_i\in\Gamma(X_{s_i}, \mathcal{O}_X)$, so surjectivity is equivalent to these ratios generating $\Gamma(X_{s_i}, \mathcal{O}_X)$ as a $\mathbb{K}$-algebra.

Therefore, our first goal is to find, among sections globally generating $\mathcal{L}^{\otimes k}$, those for which all $X_{s_i}$ are affine. To this end, for each closed point $x\in X$, we will construct, containing $x$, an affine open set $X_s$. First, choose an open affine neighborhood containing $x$ trivializing $\mathcal{L}$, say $U$. If a suitable section $s$ satisfies $X_s\subseteq U$, the fact that $X_s$ is affine is immediately obtained by regarding $X_s$ as the principal open set in $U$ defined by the function $s$, so the section $s$ we must find is one that is non-vanishing at $x$ and identically zero on $Y=X\setminus U$.

To this end, endow $Y$ with the reduced closed subscheme structure, and consider its ideal sheaf $\mathcal{I}_Y$. Since this is the kernel of $\mathcal{O}_X \rightarrow \iota_\ast\mathcal{O}_Y$, it is quasi-coherent, and on each affine chart $\Spec A$ it corresponds to an ideal of $A$. But since $X$ is Noetherian, so is $A$, and this ideal is finitely generated ([\[Commutative Algebra\] §Basic Notions, ⁋Theorem 3](/en/math/commutative_algebra/basic_notions#thm3){: data-lid="pl8j7" }), so $\mathcal{I}_Y$ is a coherent sheaf. Thus, from the ampleness of $\mathcal{L}$, we know that for some $n>0$, $\mathcal{I}_Y\otimes\mathcal{L}^{\otimes n}$ is globally generated. At this point, since $x\not\in Y$, we have $(\mathcal{I}_Y)_x=\mathcal{O}_{X,x}$, and hence there exists a section not vanishing at $x$, namely $s\in\Gamma(X, \mathcal{I}_Y\otimes\mathcal{L}^{\otimes n})\subseteq\Gamma(X, \mathcal{L}^{\otimes n})$, from which we can choose for each closed point an affine open set $X_s$ containing it. Moreover, since $X$ is of finite type over $\mathbb{K}$, the coordinate ring of each affine chart is a Jacobson ring ([\[Commutative Algebra\] §The Nullstellensatz, ⁋Theorem 4](/en/math/commutative_algebra/nullstellensatz#thm4){: data-lid="7sbm5" }), and therefore every non-empty closed subset of $X$ always contains a closed point of $X$. That is, the union of the above open sets obtained from the closed points is all of $X$ because its complement is a closed set containing no closed point, and since $X$ is quasi-compact, already a finite subcollection $X_{s_1},\ldots, X_{s_q}$ covers $X$. However, these were obtained from sheaves with different exponents, as $s_i\in\Gamma(X, \mathcal{L}^{\otimes n_i})$, so to jointly define a single morphism, we must make them sections of the same sheaf by setting the exponent to their least common multiple $m$, and replace the $s_i$ with $s_i^{m/n_i}$ so that $s_i\in \Gamma(X, \mathcal{L}^{\otimes m})$; and this process is justified since for any $e\geq1$, we have $X_{s^e}=X_s$.

Now, since $X_{s_i}$ is affine and $X$ is of finite type over $\mathbb{K}$, each $B_i=\Gamma(X_{s_i}, \mathcal{O}_X)$ is a finitely generated $\mathbb{K}$-algebra, and we can choose its generators $b_{i1},\ldots, b_{ir_i}$. Now our claim is that, so that

$$b_{ij}=t_{ij}/s_i^N, \qquad t_{ij}\in\Gamma(X, \mathcal{L}^{\otimes mN})$$

holds, there exist a common $N$ and global sections $t_{ij}$ such that $s_1^N,\ldots, s_q^N$ and the $t_{ij}$ globally generate $\mathcal{L}^{\otimes mN}$. If this holds, then among the ratios they give on the chart of $s_i^N$, there is $t_{ij}/s_i^N=b_{ij}$, so the desired surjectivity, namely the fact that $\varphi$ becomes a closed embedding when restricted to affine schemes, will be proved. The charts checked here are only those corresponding to $s_i^N$, but since the $X_{s_i}$ cover $X$, this means that $\varphi$ is a closed embedding into the union of these charts, that is, a locally closed embedding.

To this end, choose for $\mathcal{L}^{\otimes m}$ a trivializing affine open cover $V_1,\ldots, V_p$, and fix a trivialization on each $V_l=\Spec A_l$; then $s_i$ corresponds to a function $g_{il}\in A_l$, and $X_{s_i}\cap V_l=D(g_{il})$. Then the restriction of the functions on $X_{s_i}$, namely $b_{ij}$, to $D(g_{il})$ is an element of $(A_l)_{g_{il}}$, so multiplying by a suitable power of $g_{il}$ makes it an element of $A_l$, and since there are finitely many such exponents for $i$, $j$, and $l$, taking their maximum $N_0$ allows us to ensure that for all $l$, $s_i^{N_0}b_{ij}$ extends on $V_l$ to a section of $\mathcal{L}^{\otimes mN_0}$. Now what remains is to show that these can be glued into a global section $t_{ij}$.

To this end, considering the extensions obtained from the two charts $V_l$ and $V_{l'}$, they agree on $X_{s_i}\cap V_l\cap V_{l'}$, but there is no reason they should agree on the whole of $V_l\cap V_{l'}$. To resolve this, take an affine open cover simultaneously trivializing $\mathcal{L}^{\otimes m}$ and $\mathcal{L}^{\otimes mN_0}$, and let it cover $V_l\cap V_{l'}$. Since $X$ is Noetherian, we may arrange that there are finitely many such affine open sets. Then on such an affine open set $\Spec C$, $s_i$ corresponds to a function $g\in C$, and the difference of the two extensions on $V_l$ and $V_{l'}$ is an element vanishing on $D(g)$, namely $h\in C$. Then in $C_g$ we have $h=0$, so for some exponent $c$ we have $g^ch=0$, which means that multiplying both extensions by $s_i^c$ makes them agree on the whole of $V_l\cap V_{l'}$. Since there are also finitely many such exponents, taking their maximum $c_0$ and setting $N=N_0+c_0$, the chart-wise extensions of $s_i^{N_0}b_{ij}$ multiplied by $s_i^{c_0}$ agree with one another and glue into a single $t_{ij}\in\Gamma(X, \mathcal{L}^{\otimes mN})$; and by construction, the restriction of $t_{ij}$ to $X_{s_i}$ is $s_i^Nb_{ij}$, where the fact that these globally generate $\mathcal{L}^{\otimes mN}$ is already obvious since $X_{s_i}$ cover $X$.
:::

By part 2 of [§Divisors and Linear Systems, ⁋Proposition 19](/en/math/scheme_theory/divisors_and_linear_systems#prop19){: data-lid="0sa6k" }, that $\mathcal{L}$ is ample is equivalent to having, for any $m\geq1$, that $\mathcal{L}^{\otimes m}$ is ample, so [Theorem 12](#thm12){: data-lid="y51eu" } tells us that the difference between the two notions comes only from taking powers. Adding [Theorem 10](#thm10){: data-lid="g0md4" } to this, ampleness can be determined solely by the vanishing of cohomology.

::: Theorem 13 (Serre criterion)
For an invertible sheaf $\mathcal{L}$ on a Noetherian projective scheme $X$ over a field $\mathbb{K}$, the following two conditions are equivalent.

1. $\mathcal{L}$ is ample.
2. For any coherent sheaf $\mathcal{F}$, there exists $n_0$ such that for all $i>0$ and $n\geq n_0$, $H^i(X, \mathcal{F}\otimes_{\mathcal{O}_X}\mathcal{L}^{\otimes n})=0$.
:::
::: Proof
The direction that the first condition implies the second is easy, so let us look at it first. If $\mathcal{L}$ is ample, then by [Theorem 12](#thm12){: data-lid="7pnsh" } there exists $m>0$ such that $\mathcal{L}^{\otimes m}$ is very ample. Then, as in the proof of [Corollary 11](#cor11){: data-lid="d4pc2" }, the embedding defined by $\mathcal{L}^{\otimes m}$ is a closed embedding, so taking $\mathcal{L}^{\otimes m}$ as the twisting sheaf we can apply [Theorem 10](#thm10){: data-lid="b9dmh" }. In particular, applying this to each of the finitely many coherent sheaves

$$\mathcal{F}\otimes\mathcal{L}^{\otimes q},\qquad q=0,1,\ldots, m-1$$

for each $q$ there exist $p_q$ such that for all $p>p_q$,

$$H^i\bigl(X, \mathcal{F}\otimes\mathcal{L}^{\otimes q}\otimes(\mathcal{L}^{\otimes m})^{\otimes p}\bigr)=0 \qquad (i>0).$$

Now setting $n_0=m(\max p_q+1)$, any $n\geq n_0$ satisfies

$$n\geq n_0>m p_q+ q$$

for all $q$, so we obtain the desired result.

Thus the heart of this theorem is to assume the second condition and prove the first. That is, fixing an arbitrary coherent sheaf $\mathcal{F}$, we must show that $\mathcal{F}\otimes\mathcal{L}^{\otimes n}$ is globally generated for all sufficiently large $n$.

First, fix a closed point $x\in X$, and let $\mathcal{I}_x$ be the ideal sheaf obtained by giving $\{x\}$ the reduced closed subscheme structure. That is, $\mathcal{I}_x$ is the kernel of $\mathcal{O}_X \rightarrow \iota_\ast\mathcal{O}_{\{x\}}$ given by the closed embedding $\iota:\{x\} \rightarrow X$ ([§Closed Subschemes, ⁋Definition 5](/en/math/scheme_theory/closed_subschemes#def5){: data-lid="ofc91" }), and since $x$ is a closed point, on any open set $U$ not meeting $\{x\}$ we have $(\iota_\ast\mathcal{O}_{\{x\}})(U)=\mathcal{O}_{\{x\}}(U\cap\{x\})=0$, so cleanly $\mathcal{I}_x=\mathcal{O}_X$ on the open set $X\setminus \{x\}$. Now let $\mathcal{I}_x\mathcal{F}$ be the image of the multiplication map $\mathcal{I}_x\otimes\mathcal{F} \rightarrow \mathcal{F}$; then on each affine chart $\Spec A$, $\mathcal{I}_x$ and $\mathcal{F}$ correspond to an ideal $I\subseteq A$ and a finitely generated $A$-module $M$, and since the associated sheaf functor is exact ([§Quasi-Coherent Sheaves, ⁋Proposition 6](/en/math/scheme_theory/quasicoherent_sheaves#prop6){: data-lid="58hx0" }), $\mathcal{I}_x\mathcal{F}$ is the associated sheaf of the submodule $IM\subseteq M$ on each chart. Here, since $X$ is Noetherian, $IM$ is also finitely generated ([\[Commutative Algebra\] §Basic Notions, ⁋Theorem 3](/en/math/commutative_algebra/basic_notions#thm3){: data-lid="327vv" }), so $\mathcal{I}_x\mathcal{F}$ is a coherent sheaf. We thus obtain a short exact sequence

$$0 \rightarrow \mathcal{I}_x\mathcal{F} \rightarrow \mathcal{F} \rightarrow \mathcal{F}/\mathcal{I}_x\mathcal{F} \rightarrow 0.$$

But from the computation above, we have already seen that $\mathcal{I}_x$ becomes all of $\mathcal{O}_X$ outside $\{x\}$, so the stalk of the last term $\mathcal{F}/\mathcal{I}_x\mathcal{F}$ vanishes away from $x$, and at $x$, since $\mathcal{I}_x$ is the ideal sheaf of the reduced structure, it is precisely the skyscraper sheaf at $x$ with value

$$(\mathcal{F}/\mathcal{I}_x\mathcal{F})_x=\mathcal{F}_x/\mathfrak{m}_x\mathcal{F}_x=\mathcal{F}_x\otimes_{\mathcal{O}_{X,x}}\kappa(x).$$

Now tensoring the above exact sequence with $\mathcal{L}^{\otimes n}$, since this is invertible it is locally isomorphic to $\mathcal{O}_X$, and thus exactness is preserved, so

$$0 \rightarrow \mathcal{I}_x\mathcal{F}\otimes\mathcal{L}^{\otimes n} \rightarrow \mathcal{F}\otimes\mathcal{L}^{\otimes n} \rightarrow (\mathcal{F}/\mathcal{I}_x\mathcal{F})\otimes\mathcal{L}^{\otimes n} \rightarrow 0$$

is also exact, and the last term becomes the skyscraper sheaf at $x$ with value

$$(\mathcal{F}\otimes\mathcal{L}^{\otimes n})_x\otimes_{\mathcal{O}_{X,x}}\kappa(x).$$

Now applying the given hypothesis to the coherent sheaf $\mathcal{I}_x\mathcal{F}$, there exists $n_1$ such that for all $n\geq n_1$, $H^1(X, \mathcal{I}_x\mathcal{F}\otimes\mathcal{L}^{\otimes n})=0$, so a portion of the long exact sequence

$$\Gamma(X, \mathcal{F}\otimes\mathcal{L}^{\otimes n}) \rightarrow (\mathcal{F}\otimes\mathcal{L}^{\otimes n})_x\otimes_{\mathcal{O}_{X,x}}\kappa(x) \rightarrow 0$$

is exact. That is, the global sections of $\mathcal{F}\otimes\mathcal{L}^{\otimes n}$ surject onto the fiber at $x$. From this we obtain global generation in a neighborhood of $x$.

Indeed, the stalk $M=(\mathcal{F}\otimes\mathcal{L}^{\otimes n})_x$ is a finitely generated module over the Noetherian local ring $\mathcal{O}_{X,x}$, and the fiber of the above skyscraper sheaf is $M/\mathfrak{m}_xM$, so we can choose finitely many global sections $s_1,\ldots, s_c$ whose germs generate $M/\mathfrak{m}_xM$, and by the second result of [\[Commutative Algebra\] §Integral Extensions, ⁋Lemma 8](/en/math/commutative_algebra/integral_extension#lem8){: data-lid="w3y3a" } they generate $M$ itself. Then the cokernel $\mathcal{Q}$ of the map $\mathcal{O}_X^{\oplus c} \rightarrow \mathcal{F}\otimes\mathcal{L}^{\otimes n}$ defined by $s_1,\ldots, s_c$ is a coherent sheaf satisfying $\mathcal{Q}_x=0$. Taking an affine open set $\Spec A$ containing $x$, letting $N$ be the finitely generated $A$-module corresponding to $\mathcal{Q}$ on it and $\mathfrak{p}$ the prime ideal corresponding to $x$, since $N_\mathfrak{p}=0$, for each generator of $N$ there exists an element outside $\mathfrak{p}$ annihilating it; since $N$ has finitely many generators, letting $f$ be the product of the elements thus obtained, we have $N_f=0$. Hence $\mathcal{Q}$ vanishes on the open neighborhood $D(f)$ of $x$, which means that $\mathcal{F}\otimes\mathcal{L}^{\otimes n}$ is generated by $s_1,\ldots, s_c$ on $D(f)$.

That is, we have verified that for each closed point $x$ there exists an open neighborhood $D(f)$ such that $\mathcal{F}\otimes\mathcal{L}^{\otimes n}$ is globally generated at each point of $D(f)$. What is somewhat subtle is that the definition of this $D(f)$ varies with $n$, and to finish the proof of the theorem we need a single neighborhood that works simultaneously for all sufficiently large $n$, so before the main argument we must find a way to increase the exponent of $\mathcal{L}$ on a fixed neighborhood. For this, applying the argument so far to $\mathcal{F}=\mathcal{O}_X$, there exists $e\geq1$ such that $\mathcal{L}^{\otimes e}$ and $\mathcal{L}^{\otimes(e+1)}$ are each globally generated on some open neighborhood of $x$, and both are so on the intersection $W$ of the two neighborhoods. Since the tensor product of two globally generated sheaves is again globally generated by the tensors of the stalk generators, for $a,b\geq0$, $\mathcal{L}^{\otimes(ae+b(e+1))}$ is globally generated on $W$. Now, if we let $s$ be the quotient and $b$ the remainder of an integer $k\geq e^2$ divided by $e$, then $s\geq e>b\geq0$, so $a=s-b$ is non-negative and $ae+b(e+1)=se+b=k$; thus on $W$, $\mathcal{L}^{\otimes k}$ is globally generated for all $k\geq e^2$. Returning now to $\mathcal{F}$ itself, if we choose some $n_2\geq n_1$, then $\mathcal{F}\otimes\mathcal{L}^{\otimes n_2}$ is globally generated on some open neighborhood $V$ of $x$, so for all $n\geq n_2+e^2$,

$$\mathcal{F}\otimes\mathcal{L}^{\otimes n}\cong(\mathcal{F}\otimes\mathcal{L}^{\otimes n_2})\otimes\mathcal{L}^{\otimes(n-n_2)}$$

is globally generated on $W\cap V$. Thus, for each closed point $x$ we obtain an open neighborhood $U_x=W\cap V$ and a lower bound $n_x=n_2+e^2$ such that $\mathcal{F}\otimes\mathcal{L}^{\otimes n}$ is globally generated on $U_x$ whenever $n\geq n_x$.

Now it remains to cover $X$ by these neighborhoods; as seen in the proof of [Theorem 12](#thm12){: data-lid="tzhwq" }, since $X$ is of finite type over $\mathbb{K}$, the coordinate ring of each affine chart is a Jacobson ring, so every non-empty closed subset of $X$ always contains a closed point. Therefore, since its complement is a closed set containing no closed points, the union of the $U_x$ is all of $X$, and since $X$ is quasi-compact, finitely many $U_{x_1},\ldots, U_{x_r}$ suffice to cover $X$. Then setting $n_0=\max_jn_{x_j}$, for every $n\geq n_0$ the sheaf $\mathcal{F}\otimes\mathcal{L}^{\otimes n}$ is generated by global sections at every point of $X$, and since $\mathcal{F}$ was an arbitrary coherent sheaf, $\mathcal{L}$ is ample.
:::

A noteworthy fact from the proof is that although what [Theorem 13](#thm13){: data-lid="siiyj" } required as a condition was the vanishing of all $i>0$, in obtaining 1 from 2 what was actually used was only the vanishing of $H^1$; this is because the obstruction to lifting a section of the quotient sheaf to a global section lies in the $H^1$ term of the long exact sequence.

## Euler Characteristic and Hilbert Polynomial

By [Theorem 9](#thm9){: data-lid="gyecm" }, a coherent sheaf on a projective scheme has only finitely many finite-dimensional cohomologies, so we can take the alternating sum of their dimensions.

::: Definition 14
Over a field $\mathbb{K}$, for a Noetherian projective scheme $X$ and a coherent sheaf $\mathcal{F}$ on it, we define the *Euler characteristic* of $\mathcal{F}$ by the formula

$$\rchi(X, \mathcal{F})=\sum_{i\geq 0}(-1)^i\dim_\mathbb{K}H^i(X, \mathcal{F})$$
:::

By [Theorem 9](#thm9){: data-lid="kfevo" }, the right-hand side is a finite sum and each term is finite, so $\rchi(X, \mathcal{F})$ is an integer; when $X$ is clear from context, we abbreviate it as $\rchi(\mathcal{F})$. This carries [\[Algebraic Varieties\] §Cohomology of Projective Space, ⁋Definition 2](/en/math/algebraic_varieties/cohomology_of_projective_spaces#def2){: data-lid="6xhig" } over to schemes. While the individual dimensions $\dim_\mathbb{K}H^i(X, \mathcal{F})$ can jump even under a slight perturbation of the sheaf, their alternating sum is far more stable; the source of this is the following additivity.

::: Proposition 15
Over a field $\mathbb{K}$, the following hold for coherent sheaves on a Noetherian projective scheme $X$.

1. For a short exact sequence $0 \rightarrow \mathcal{F}' \rightarrow \mathcal{F} \rightarrow \mathcal{F}'' \rightarrow 0$, we have $\rchi(\mathcal{F})=\rchi(\mathcal{F}')+\rchi(\mathcal{F}'')$.
2. For a finite exact sequence $0 \rightarrow \mathcal{F}_k \rightarrow \cdots \rightarrow \mathcal{F}_1 \rightarrow \mathcal{F}_0 \rightarrow 0$, we have $\sum_{j=0}^k(-1)^j\rchi(\mathcal{F}_j)=0$.
:::
::: Proof
First consider an exact sequence $0 \rightarrow V_0 \rightarrow V_1 \rightarrow \cdots \rightarrow V_t \rightarrow 0$ of finite-dimensional vector spaces. If we denote the rank of the $j$-th linear map by $r_j$ ($r_{-1}=r_t=0$), exactness gives $\dim V_j=r_{j-1}+r_j$, so in the alternating sum $\sum_j(-1)^j\dim V_j$ adjacent terms cancel each other to give $0$.

For (1), the long exact sequence given by [Proposition 2](#prop2){: data-lid="yriwc" }

$$0 \rightarrow H^0(X, \mathcal{F}') \rightarrow H^0(X, \mathcal{F}) \rightarrow H^0(X, \mathcal{F}'') \rightarrow H^1(X, \mathcal{F}') \rightarrow \cdots$$

consists of finite-dimensional vector spaces by [Theorem 9](#thm9){: data-lid="wg5k2" } and terminates in sufficiently high degree, so it is finite. Applying the observation above, the alternating sum of the cohomology dimensions of the three sheaves is $0$, and rearranging signs gives the desired formula.

For (2), for $j\geq1$ let $\mathcal{Z}_j=\ker(\mathcal{F}_j \rightarrow \mathcal{F}_{j-1})$, and let $\mathcal{Z}_0=\mathcal{F}_0$. Since the kernel of a morphism between coherent sheaves is again a coherent sheaf, each $\mathcal{Z}_j$ is a coherent sheaf; by exactness $\mathcal{Z}_k=0$, and for each $j\geq1$ we obtain a short exact sequence

$$0 \rightarrow \mathcal{Z}_j \rightarrow \mathcal{F}_j \rightarrow \mathcal{Z}_{j-1} \rightarrow 0$$

Applying (1) to this, summing the resulting $\rchi(\mathcal{F}_j)=\rchi(\mathcal{Z}_j)+\rchi(\mathcal{Z}_{j-1})$ with alternating signs causes all intermediate terms to cancel, yielding $\sum_{j=1}^k(-1)^j\rchi(\mathcal{F}_j)=-\rchi(\mathcal{Z}_0)=-\rchi(\mathcal{F}_0)$.
:::

In particular, if a coherent sheaf $\mathcal{F}$ has a finite resolution $0 \rightarrow \mathcal{E}_k \rightarrow \cdots \rightarrow \mathcal{E}_0 \rightarrow \mathcal{F} \rightarrow 0$, then from (2) of [Proposition 15](#prop15){: data-lid="ctund" } we obtain $\rchi(\mathcal{F})=\sum_{j=0}^k(-1)^j\rchi(\mathcal{E}_j)$. This is the standard path for actually computing the Euler characteristic, and its starting point is line bundles on projective space.

::: Corollary 16
For the projective space $\mathbb{P}^n_\mathbb{K}$ over a field $\mathbb{K}$ and any integer $d$,

$$\rchi(\mathbb{P}^n_\mathbb{K}, \mathcal{O}(d))=\binom{n+d}{n}$$

holds. Here $\binom{n+d}{n}$ is read as the value of the polynomial $t(t-1)\cdots(t-n+1)/n!$ at $t=n+d$.
:::
::: Proof
Setting $A=\mathbb{K}$ in [Theorem 7](#thm7){: data-lid="ph85s" }, there are three cases. If $d\geq0$, only $H^0$ survives and its dimension is the number of degree $d$ monomials in $n+1$ variables, $\binom{n+d}{n}$. If $-n\leq d\leq-1$, all cohomology vanishes; in this range $t=n+d$ is an integer between $0$ and $n-1$, so one of the factors in the product $t(t-1)\cdots(t-n+1)$ is $0$, giving $\binom{n+d}{n}=0$. If $d\leq -n-1$, only $H^n$ survives and its dimension is the number of degree $d$ monomials with all exponents negative, $\binom{-d-1}{n}$, so

$$\rchi(\mathbb{P}^n_\mathbb{K}, \mathcal{O}(d))=(-1)^n\binom{-d-1}{n}=\binom{n+d}{n}$$

holds. The last equality follows from $t(t-1)\cdots(t-n+1)=(-1)^n(n-t-1)(n-t-2)\cdots(-t)$ for $t=n+d$.
:::

This value is a polynomial of degree $n$ in $d$, matching the variety version of [\[Algebraic Varieties\] §Cohomology of Projective Space, ⁋Corollary 3](/en/math/algebraic_varieties/cohomology_of_projective_spaces#cor3){: data-lid="e65jg" }. That is, as we twist $\mathcal{O}(d)$, the alternating sum of cohomology follows a single polynomial regardless of the three phases that the individual cohomologies undergo. The following theorem states that this also holds for general coherent sheaves; to state it, we define the *support* of a coherent sheaf $\mathcal{F}$ as $\supp\mathcal{F}=\{x\in X\mid \mathcal{F}_x\neq0\}$. On an affine chart this is the zero set of the annihilator ideal of the corresponding module, hence a closed set.

::: Theorem 17 (Hilbert)
Over a field $\mathbb{K}$, for the projective space $\mathbb{P}^n_\mathbb{K}$, its closed subscheme $X$, and a coherent sheaf $\mathcal{F}$ on it, there exists a unique numerical polynomial $P_\mathcal{F}$ such that ([\[Commutative Algebra\] §Hilbert–Samuel Function, ⁋Definition 1](/en/math/commutative_algebra/hilbert-samuel_function#def1){: data-lid="l3v24" }) for every integer $d$,

$$\rchi(\mathcal{F}(d))=P_\mathcal{F}(d)$$

holds. Moreover, if $\mathcal{F}\neq0$, then the degree of $P_\mathcal{F}$ equals $\dim\supp\mathcal{F}$, and for sufficiently large $d$, we have $P_\mathcal{F}(d)=\dim_\mathbb{K}\Gamma(X, \mathcal{F}(d))$.
:::
::: Proof
The last claim follows immediately from [Theorem 10](#thm10){: data-lid="mpsf6" }: for sufficiently large $d$ we have $H^i(X, \mathcal{F}(d))=0$ ($i>0$), so only $H^0$ remains in the alternating sum. Uniqueness follows from the fact that two distinct polynomials cannot agree at infinitely many integers.

We first reduce to the case $X=\mathbb{P}^n_\mathbb{K}$. For the closed embedding $\iota:X\hookrightarrow\mathbb{P}^n_\mathbb{K}$, combining the isomorphism $(\ast)$ just before [Theorem 9](#thm9){: data-lid="qoq9c" } with the equality $\iota_\ast(\mathcal{F}(d))\cong(\iota_\ast\mathcal{F})(d)$ seen in the proof of [Theorem 10](#thm10){: data-lid="qj82d" }, we have $H^i(X, \mathcal{F}(d))\cong H^i(\mathbb{P}^n, (\iota_\ast\mathcal{F})(d))$; and since $\supp\iota_\ast\mathcal{F}=\iota(\supp\mathcal{F})$, as seen in the proof of [Theorem 9](#thm9){: data-lid="o8jy6" }, we may substitute $\iota_\ast\mathcal{F}$, which is coherent, for $\mathcal{F}$.

Moreover, we may assume that the field $\mathbb{K}$ is *infinite*. Since the conclusion of the theorem is stated solely in terms of the dimensions of cohomology and the dimension of $\supp\mathcal{F}$, to show this it suffices to show that these two invariants are preserved under an extension to an infinite field $\mathbb{K}\hookrightarrow \mathbb{L}$. First, for the dimensions of cohomology, the Čech complex for the standard affine cover is $\check{C}^\bullet(\mathcal{U}, \mathcal{F})\otimes_\mathbb{K}\mathbb{L}$ with only the coefficients changed, and since $-\otimes_\mathbb{K}\mathbb{L}$ is exact, by [Corollary 5](#cor5){: data-lid="kum72" } we have $\dim_\mathbb{L}H^i(\mathbb{P}^n_\mathbb{L}, \mathcal{F}_\mathbb{L}(d))=\dim_\mathbb{K}H^i(\mathbb{P}^n_\mathbb{K}, \mathcal{F}(d))$. For the dimension of the support, we first see that the support itself is compatible with field extension. On each affine chart $\Spec A$, corresponding to $\mathcal{F}$ is a finitely generated module $M$, and if we choose generators $m_1,\ldots, m_r$, then $\ann M$ is the kernel of the map given by $a\mapsto(am_1,\ldots, am_r)$, $A \rightarrow M^{\oplus r}$. ([\[Commutative Algebra\] §Basic Notions, ⁋Definition 1](/en/math/commutative_algebra/basic_notions#def1){: data-lid="vv6fy" }) However, the $m_k\otimes1$ generate $M\otimes_\mathbb{K}\mathbb{L}$ and $-\otimes_\mathbb{K}\mathbb{L}$ preserves kernels, so $\ann(M\otimes_\mathbb{K}\mathbb{L})=(\ann M)\otimes_\mathbb{K}\mathbb{L}$; thus if $\supp\mathcal{F}$ is $\Spec(A/\ann M)$ on each chart, then on each chart $\supp\mathcal{F}_\mathbb{L}$ is given by $\Spec\bigl((A/\ann M)\otimes_\mathbb{K}\mathbb{L}\bigr)$. Now, since the dimension of a finitely generated $\mathbb{K}$-algebra does not change under field extension ([\[Commutative Algebra\] §Noether Normalization, ⁋Proposition 5](/en/math/commutative_algebra/noether_normalization#prop5){: data-lid="piea1" }), these two invariants are preserved, and therefore we may assume from the outset that $\mathbb{K}$ is an infinite field.

Now, the overall structure of the proof is the same dévissage used in the proofs of [Theorem 9](#thm9){: data-lid="w99ne" } and [Theorem 10](#thm10){: data-lid="w2ayd" }: we construct a short exact sequence

$$0 \rightarrow \mathcal{F}(-1) \rightarrow \mathcal{F} \rightarrow \mathcal{F}'' \rightarrow 0\tag{$\ast\ast$}$$

and transfer the desired properties along it. Here, $\mathcal{F}(-1) \rightarrow \mathcal{F}$ is the morphism of multiplication by an element of the homogeneous coordinate ring $S_\bullet=\mathbb{K}[\x_0,\ldots, \x_n]$ of degree $1$, $\ell\in S_1$, and $\mathcal{F}''$ is its cokernel; intuitively, this is the restriction of $\mathcal{F}$ to the hyperplane $V_+(\ell)$, namely the hyperplane section of $\mathcal{F}$. The difference is that, whereas the proofs of the earlier theorems ran induction by covering a coherent sheaf with a free sheaf and computing with the long exact sequence, we run induction on the dimension $r=\dim\supp \mathcal{F}$ of the support using the additivity in [Proposition 15](#prop15){: data-lid="6ho2r" }."

First, for such a short exact sequence to exist, we cannot choose $\ell$ arbitrarily. The issue is the injectivity of $\times \ell$: if $\ell$ belongs to some associated prime of $\mathcal{F}$ (that is, appearing as the annihilator of a non-$0$ section $m$, a prime $\mathfrak{p}=\ann(m)$), then $\ell m=0$ and injectivity fails. Conversely, since all zerodivisors are the union of the associated primes, these are the only obstructions to injectivity. Geometrically, the point $\mathfrak{p}$ lying on the hyperplane $V_+(\ell)$ is precisely $\ell\in\mathfrak{p}$, so this condition is equivalent to saying that $V_+(\ell)$ does not pass through any of the finitely many points given by the associated primes of $\mathcal{F}$. Since among these points are the generic points of each irreducible component of $\supp\mathcal{F}$ ([§Algebraic Structure of Schemes, §§Associated Primes](/en/math/scheme_theory/algebra_of_schemes#associated-primes){: data-lid="5fswh" }), such a hyperplane does not contain any component of $\supp\mathcal{F}$ as a whole and meets each only in a proper subset. Therefore, $\ell$ must avoid all the points given by the associated primes of $\mathcal{F}$; our idea is that while there are only finitely many associated primes, we have arranged $\mathbb{K}$ to be infinite, and we make use of this.

If $\mathcal{F}=0$, then all cohomology vanishes, so the theorem itself is trivial. Thus, assume $\mathcal{F}\neq0$. On each chart $D_+(\x_j)=\Spec S_{(\x_j)}$, the sheaf $\mathcal{F}$ corresponds to a finitely generated module $M_j$ ([§Quasi-Coherent Sheaves, ⁋Theorem 10](/en/math/scheme_theory/quasicoherent_sheaves#thm10){: data-lid="tw0fl" }, [§Quasi-Coherent Sheaves, ⁋Definition 11](/en/math/scheme_theory/quasicoherent_sheaves#def11){: data-lid="3iopp" }), and each $\Ass M_j$ is a finite set. ([\[Commutative Algebra\] §Associated Primes, ⁋Theorem 7](/en/math/commutative_algebra/associated_primes#thm7){: data-lid="m7yvp" }, part 1) Collecting all corresponding points of $\mathbb{P}^n$ yields finitely many points, and each gives a homogeneous prime ideal $\mathfrak{p}_1,\ldots, \mathfrak{p}_t\subseteq S$ not containing the irrelevant ideal. Since $\mathfrak{p}_k$ is homogeneous, if $S_1\subseteq\mathfrak{p}_k$, then $\mathfrak{p}_k$ would contain the irrelevant ideal, so each $\mathfrak{p}_k\cap S_1$ is a proper subspace of $S_1$. On the other hand, since $\mathbb{K}$ is an infinite field, the vector space $S_1$ cannot be the union of finitely many proper subspaces, and therefore, belonging to none of the $\mathfrak{p}_k$, there exists an element $\ell\in S_1$.

While $\ell$ chosen in this way avoids the homogeneous primes of $S$, namely the $\mathfrak{p}_k$, what obstructs the injectivity of the short exact sequence is the associated primes on each chart, so we must transfer this condition to the $S_{(\x_j)}$ side via the correspondence of [§Projective Space and the Proj Construction, ⁋Lemma 8](/en/math/scheme_theory/projective_schemes#lem8){: data-lid="ifzsy" }. Viewing the multiplication-by-$\ell$ morphism $\mathcal{F}(-1) \rightarrow \mathcal{F}$ on the chart $D_+(\x_j)$, it acts on each element of $M_j$ by multiplying by $\ell/\x_j$. Our claim is that this element $\ell/\x_j$ is not a zerodivisor on $M_j$, hence injectivity is guaranteed; for this, we must show that $\ell/\x_j$ does not belong to any associated prime of $M_j$. ([\[Commutative Algebra\] §Associated Primes, ⁋Theorem 7](/en/math/commutative_algebra/associated_primes#thm7){: data-lid="7pp8p" }, part 2) Indeed, each associated prime of $M_j$ is, on the chart $D_+(\x_j)$, given by some $\mathfrak{p}_k$ under this correspondence as the prime $\mathfrak{p}_kS_{\x_j}\cap S_{(\x_j)}$; if $\ell/\x_j$ belonged to such a prime, then $\ell=\x_j\cdot(\ell/\x_j)$ would belong to $\mathfrak{p}_kS_{\x_j}\cap S=\mathfrak{p}_k$, contradicting the choice of $\ell$. Hence this morphism is injective. Letting its cokernel be $\mathcal{F}''$, for each $d$ we obtain a short exact sequence

$$0 \rightarrow \mathcal{F}(d-1) \rightarrow \mathcal{F}(d) \rightarrow \mathcal{F}''(d) \rightarrow 0$$

and $\supp\mathcal{F}''=\supp\mathcal{F}\cap V_+(\ell)$. Indeed, looking at the stalk at a point $\mathfrak{p}$, we have $\mathcal{F}''_\mathfrak{p}=\mathcal{F}_\mathfrak{p}/\ell\mathcal{F}_\mathfrak{p}$; if $\ell\notin\mathfrak{p}$, then $\ell$ is a unit in the local ring so this is $0$, and if $\ell\in\mathfrak{p}$ while $\mathcal{F}_\mathfrak{p}\neq0$, then by part 1 of [\[Commutative Algebra\] §Integral Extensions, ⁋Lemma 8](/en/math/commutative_algebra/integral_extension#lem8){: data-lid="5ltub" } we have $\mathcal{F}_\mathfrak{p}/\ell\mathcal{F}_\mathfrak{p}\neq0$.

Now, as announced, the remainder consists in applying induction on the dimension using the short exact sequence ($\ast\ast$) thus obtained. For this, we must first show that a hyperplane section indeed drops the dimension of the support by exactly one. Since minimal primes are always associated primes, $\ell$ does not vanish identically on any irreducible component of $\supp\mathcal{F}$. Giving each component $Z$ its reduced structure and measuring the dimension of the intersection, since $Z$ is irreducible and of finite type over $\mathbb{K}$, for each chart meeting $Z$, in $Z\cap D_+(\x_j)=\Spec A_j$, the ring $A_j$ is a finitely generated $\mathbb{K}$-algebra that is an integral domain, and its fraction field is the function field of $Z$ independent of the chart. That is, by [§Dimension, ⁋Proposition 10](/en/math/scheme_theory/dimension#prop10){: data-lid="f372n" }, $\dim A_j$ is the same across all charts, and by [§Dimension, ⁋Proposition 2](/en/math/scheme_theory/dimension#prop2){: data-lid="jrlg6" }, this common value is $\dim Z$. If $\dim Z=0$, then $Z$ is a single point and $\ell$ does not vanish on it, so $Z\cap V_+(\ell)=\emptyset$; conversely, if $Z\cap V_+(\ell)= \emptyset$, then necessarily $\dim Z=0$. This is because $Z$ is affine as a closed subscheme of the affine scheme $D_+(\ell)$, and its coordinate ring is a finite-dimensional $\mathbb{K}$-vector space by [Theorem 9](#thm9){: data-lid="cj6rm" } and an integral domain by the integrality of $Z$, hence a field by [\[Field Theory\] §Algebraic Extensions, ⁋Proposition 3](/en/math/field_theory/algebraic_extensions#prop3){: data-lid="b3hip" }. Therefore, if $\dim Z\geq 1$, then $Z\cap V_+(\ell)$ is not empty, and choosing a chart $D_+(\x_j)$ containing a point of this set, $\ell/\x_j\in A_j$ is not $0$ and vanishes at that point so is not a unit either, and hence by [§Dimension, ⁋Proposition 12](/en/math/scheme_theory/dimension#prop12){: data-lid="96m5d" },

$$\dim\bigl(Z\cap V_+(\ell)\cap D_+(\x_j)\bigr)=\dim A_j-1=\dim Z-1$$

holds. Since this value is the same across all charts meeting $Z\cap V_+(\ell)$, by [§Dimension, ⁋Proposition 2](/en/math/scheme_theory/dimension#prop2){: data-lid="7xg7w" } we have $\dim(Z\cap V_+(\ell))=\dim Z-1$. That is, if $r=0$, then every component does not meet $V_+(\ell)$ so $\mathcal{F}''=0$, and if $r\geq1$, then $r-1$ is obtained from the components of dimension $r$, giving $\dim\supp\mathcal{F}''=r-1$.

Now we actually run the induction. First, consider the case $r=0$. In this case, since $\mathcal{F}''=0$, the short exact sequence obtained by twisting ($\ast\ast$) by $d$ yields an isomorphism $\mathcal{F}(d-1)\cong\mathcal{F}(d)$, and thus if we set $g(d)=\rchi(\mathcal{F}(d))$, then $g$ is a constant independent of $d$. If we let this constant be $P$, then $P$ is a numerical polynomial satisfying $\rchi(\mathcal{F}(d))=P(d)$ for all integers $d$. In addition, by [Theorem 10](#thm10){: data-lid="yle5s" }, for sufficiently large $d$, the sheaf $\mathcal{F}(d)$ is globally generated, and since $\mathcal{F}\neq0$, we have $\Gamma(X, \mathcal{F}(d))\neq0$, which immediately implies $P>0$ by the last claim, so $\deg P=0=r$.

Now assume $r\geq1$, and suppose that the theorem holds for the case where the dimension of the support is $r-1$. As seen above, $\dim\supp\mathcal{F}''=r-1$ and in particular $\mathcal{F}''\neq0$, so by the induction hypothesis $\rchi(\mathcal{F}''(d))$ coincides for all $d$ with some numerical polynomial $Q$, and $\deg Q=r-1$. By part 1 of [Proposition 15](#prop15){: data-lid="o8cpl" }, for all integers $d$ we have $g(d)-g(d-1)=Q(d)$, so $g(d+1)-g(d)=Q(d+1)$ is a numerical polynomial, and then by the second result of [\[Commutative Algebra\] §Hilbert–Samuel Function, ⁋Lemma 2](/en/math/commutative_algebra/hilbert-samuel_function#lem2){: data-lid="59vf3" } there exists a numerical polynomial $P$ agreeing with $g$ for sufficiently large $d$. At this point, since $\deg Q=r-1\geq0$ implies $Q\neq0$, we have $\deg P=\deg Q+1=r$. For sufficiently large $d$, we have $P(d+1)-P(d)=g(d+1)-g(d)=Q(d+1)$, so this equality holds also as polynomials; thus, stepping $d$ down one by one, we obtain

$$g(d)=g(d+1)-Q(d+1)=P(d+1)-Q(d+1)=P(d)$$

so $g$ and $P$ agree at all integers.
:::

This polynomial $P_\mathcal{F}$ is called the *Hilbert polynomial* of $\mathcal{F}$. [Corollary 16](#cor16){: data-lid="ryqxu" } is the case $\mathcal{F}=\mathcal{O}_{\mathbb{P}^n}$, where $P_{\mathcal{O}_{\mathbb{P}^n}}(t)=\binom{n+t}{n}$ and its degree is $\dim\mathbb{P}^n=n$. The last claim of [Theorem 17](#thm17){: data-lid="55rnx" } says that for sufficiently large degree, this polynomial measures the dimension of the space of global sections of $\mathcal{F}(d)$; this is where it connects with the classical perspective of introducing the Hilbert polynomial via the Hilbert function of the homogeneous coordinate ring. ([\[Commutative Algebra\] §Hilbert–Samuel Function, ⁋Definition 4](/en/math/commutative_algebra/hilbert-samuel_function#def4){: data-lid="esb2n" }) In particular, when $\mathcal{F}=\mathcal{O}_X$, this polynomial becomes an invariant of $X$ itself.

::: Definition 18
Over a field $\mathbb{K}$, in the projective space $\mathbb{P}^n_\mathbb{K}$, for a non-empty $r$-dimensional closed subscheme $X$, let the leading coefficient of the Hilbert polynomial $P_{\mathcal{O}_X}$ be $a_r$. Then we define the *degree* of $X$ by

$$\deg X=r!\cdot a_r$$

and the *arithmetic genus* of $X$ by $p_a(X)=(-1)^r\bigl(P_{\mathcal{O}_X}(0)-1\bigr)$.
:::

Here, since $\supp\mathcal{O}_X=X$, by [Theorem 17](#thm17){: data-lid="kldo5" }, $P_{\mathcal{O}_X}$ is a polynomial of degree $r$, and for sufficiently large $d$ we have $P_{\mathcal{O}_X}(d)=\dim_\mathbb{K}\Gamma(X, \mathcal{O}_X(d))>0$, so $a_r$ is positive. Moreover, writing a numerical polynomial as an integer linear combination of binomial coefficients (the first result of [\[Commutative Algebra\] §Hilbert–Samuel Function, ⁋Lemma 2](/en/math/commutative_algebra/hilbert-samuel_function#lem2){: data-lid="2fgkq" }), we see that $r!$ times the leading coefficient is an integer. Thus $\deg X$ is a positive integer. On the other hand, since $P_{\mathcal{O}_X}(0)=\rchi(\mathcal{O}_X)$, the arithmetic genus is simply a rewriting of the Euler characteristic of the structure sheaf, and the sign $(-1)^r$ is chosen so that in the case of curves it agrees with the definition $p_a=1-\rchi(\mathcal{O}_X)$ we already know.

The simplest example is projective space itself. From [Corollary 16](#cor16){: data-lid="kwsot" }, $P_{\mathcal{O}_{\mathbb{P}^n}}(t)=\binom{n+t}{n}$, so the leading coefficient is $1/n!$ and therefore $\deg\mathbb{P}^n_\mathbb{K}=1$, and from $P_{\mathcal{O}_{\mathbb{P}^n}}(0)=1$ we have $p_a(\mathbb{P}^n_\mathbb{K})=0$. As a less trivial example, for a positive degree $e$ and a non-zero homogeneous polynomial $f$, let us consider the hypersurface $X=V_+(f)\subseteq\mathbb{P}^n_\mathbb{K}$ defined by it. Since $f$ can, for at most one $j$, be a constant multiple of $\x_j^e$, if $n\geq1$ there must exist, with $f$ not being a constant multiple of $\x_j^e$, a chart $D_+(\x_j)$. On this chart, $X$ is the zero set of the dehomogenization $f/\x_j^e$, and since this element is neither $0$ nor a unit, its zero set is non-empty, and thus $X$ is a non-empty closed subscheme to which [Definition 18](#def18){: data-lid="n5nm9" } applies. Following this through, since $\mathbb{K}[\x_0,\ldots, \x_n]$ is an integral domain, multiplication by $f$ is injective on each chart, and therefore there exists a short exact sequence

$$0 \rightarrow \mathcal{O}_{\mathbb{P}^n}(-e)\overset{\times f}{\rightarrow}\mathcal{O}_{\mathbb{P}^n} \rightarrow \mathcal{O}_X \rightarrow 0$$

and twisting this by $\mathcal{O}(d)$ and applying part 1 of [Proposition 15](#prop15){: data-lid="0fc3w" } and [Corollary 16](#cor16){: data-lid="t1piu" }, we have

$$P_{\mathcal{O}_X}(t)=\binom{n+t}{n}-\binom{n+t-e}{n}$$

On the right-hand side, the $t^n$ term cancels and the coefficient of $t^{n-1}$ remaining is $e/(n-1)!$, so together with $\dim X=n-1$ we obtain $\deg X=e$. That is, the classical fact that the degree of a hypersurface in $\mathbb{P}^n$ is the degree of the defining polynomial is recovered in the language of Hilbert polynomials.

---

**References**

**[Har]** R. Hartshorne, *Algebraic geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[Vak]** R. Vakil, *The rising sea: Foundations of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/).
