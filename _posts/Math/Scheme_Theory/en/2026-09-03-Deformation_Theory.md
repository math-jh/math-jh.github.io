---
title: "Deformation Theory and the Cotangent Complex"
description: "We explain why Kahler differentials are insufficient by examining deformations and obstructions along square-zero extensions. After computing how naive and full cotangent complexes measure deformations of affine algebras, we assemble local deformations of schemes using the local-to-global spectral sequence."
excerpt: "Square-zero extensions, first-order deformations, obstructions, and the cotangent complex"

categories: [Math / Scheme Theory]
permalink: /en/math/scheme_theory/deformation_theory
sidebar:
  nav: "scheme_theory-en"

date: 2026-09-03

weight: 22
translated_at: 2026-09-13T11:15:04+00:00
translation_source: antigravity-gemini-3.8-flash-high
---
## Naive Cotangent Complex

According to [§Smooth and Étale Morphisms, ⁋Theorem 15](/en/math/scheme_theory/smooth_and_etale_morphisms#thm15){: data-relation="required" }, that a morphism of schemes $\varphi:X\rightarrow S$ locally of finite presentation is smooth is equivalent to the condition that for every affine $S$-scheme $T=\Spec R$ and every square-zero subscheme $T_0=\Spec R_0$, to extend any $S$-morphism $\varrho_0:T_0\rightarrow X$ to $T$, a lifting $\varrho:T\rightarrow X$ always exists. Here, that $T_0$ is a *square-zero subscheme* of $T$ means that $T_0\hookrightarrow T$ is defined by a square-zero ideal sheaf $\mathcal{I}\subseteq\mathcal{O}_T$, and if we view this in the affine space setting

$$S=\Spec A,\qquad X=\Spec C,\qquad\text{$C$ an $A$-algebra locally of finite presentation}$$

the closed embedding $T_0\hookrightarrow T$ corresponds to a square-zero extension

$$0\longrightarrow\mathfrak{b}\longrightarrow R\overset{q}{\longrightarrow} R_0\longrightarrow0\tag{$\ast$}$$

by a square-zero ideal $\mathfrak{b}\subseteq R$, and the $S$-morphism $\varrho_0$ corresponds to an $A$-algebra homomorphism $\rho_0:C\rightarrow R_0$. That is, in such a situation, the smoothness of $\phi: A\rightarrow C$ was equivalent to the condition that whenever a square-zero extension ($\ast$) and any $\rho_0: C\rightarrow R_0$ are given, a lifting $\rho: C\rightarrow R$ always exists.
 
Now, since $C$ is an $A$-algebra locally of finite presentation, there exist a polynomial algebra $B=A[\x_1,\ldots,\x_n]$ and a finitely generated ideal $\mathfrak{a}$ of $B$ such that we can write $C=B/\mathfrak{a}$. Consider the composition of the natural projection $\pi:B\twoheadrightarrow C$ and $\rho_0$:

$$\overline{\rho}_0:B\longrightarrow C\overset{\rho_0}{\longrightarrow}R_0$$

Then, since $q$ is surjective, for each variable $\x_i$, to satisfy $q(r_i)=\overline{\rho}_0(\x_i)$ we can choose elements $r_i\in R$, and by [\[Algebraic Structures\] §Algebras, ⁋Proposition 8](/en/math/algebraic_structures/algebras#prop8){: data-relation="required" }, the assignment $\x_i\mapsto r_i$ uniquely defines an $A$-algebra homomorphism $\widetilde{\rho}: B\rightarrow R$. This satisfies $q\circ \widetilde{\rho}=\overline{\rho}_0$, where in the choice of each $r_i$ there is freedom parameterized by $\ker q=\mathfrak{b}$. 

What we originally wish to find is a lifting from $C$, namely $\rho:C\rightarrow R$. If the chosen $\widetilde{\rho}$ satisfies $\widetilde{\rho}(\mathfrak{a})=0$, then $\widetilde{\rho}$ will directly factor through $C=B/\mathfrak{a}$ to induce the desired lifting $\rho$, but that is not all. As observed above, since the definition of $\widetilde{\rho}$ varies by the lifts of each variable, another choice of $\widetilde{\rho}$ might give $\widetilde{\rho}(\mathfrak{a})=0$. Therefore, to determine the failure of this lifting, we must compute a quantity that does not depend on the choice of $\widetilde{\rho}$.

To this end, let us first rewrite what it means, for a fixed $\widetilde{\rho}$, to have $\widetilde{\rho}(\mathfrak{a})=0$. First, for any $f\in \mathfrak{a}$, since

$$q(\widetilde{\rho}(f))=\overline{\rho}_0(f)=\rho_0(\pi(f))=\rho_0(0)=0$$

the inclusion $\widetilde{\rho}(\mathfrak{a})\subseteq \ker q=\mathfrak{b}$ is clear. Moreover, for any $f,g\in \mathfrak{a}$, since

$$\widetilde{\rho}(fg)=\widetilde{\rho}(f)\widetilde{\rho}(g)\in\mathfrak{b}^2=0$$

the map

$$\delta: \mathfrak{a}/\mathfrak{a}^2\rightarrow \mathfrak{b};\qquad \bar{f}\mapsto \widetilde{\rho}(f)$$

is well-defined. Furthermore, $\delta$ obtained in this way becomes a $C$-linear map. Here, on $\mathfrak{a}/\mathfrak{a}^2$, when viewing $\mathfrak{a}$ as a $B$-module, the $B$-ideal $\mathfrak{a}$ acts on it by $0$, so that a $C=B/\mathfrak{a}$-module structure is given; and for $\mathfrak{b}$, since $\mathfrak{b}^2=0$, the structure on $\mathfrak{b}$ as an $R$-module gives an $R_0=R/\mathfrak{b}$-module structure, which is viewed via $\rho_0$ as a $C$-module. That is, for a fixed $\widetilde{\rho}$, having $\widetilde{\rho}(\mathfrak{a})=0$ is precisely equivalent to the $C$-linear map $\delta\in\Hom_C(\mathfrak{a}/\mathfrak{a}^2, \mathfrak{b})$ defined in this manner being $0$. 

Based on this, we can quantify the variation when changing the choice of $\widetilde{\rho}$. Let $\widetilde{\rho}$ and $\widetilde{\rho}'$ be two lifts of $\overline{\rho}_0$. Then from the equality $q\circ\widetilde{\rho}=q\circ\widetilde{\rho}'$, their difference $D=\widetilde{\rho}'-\widetilde{\rho}$ is a map from $B$ to $\ker q=\mathfrak{b}$ that is $A$-linear. However,

$$D(fg)=\widetilde{\rho}'(f)\widetilde{\rho}'(g)-\widetilde{\rho}(f)\widetilde{\rho}(g)=\left(\widetilde{\rho}(f)+D(f)\right)\left(\widetilde{\rho}(g)+D(g)\right)-\widetilde{\rho}(f)\widetilde{\rho}(g)=\widetilde{\rho}(f)D(g)+D(f)\widetilde{\rho}(g)+D(f)D(g)$$

and since $D(f),D(g)\in\mathfrak{b}$ and $\mathfrak{b}^2=0$, the last term $D(f)D(g)$ vanishes. Meanwhile, on $\mathfrak{b}$, the $R$-module structure is given via $q: R\rightarrow R_0$, so

$$\widetilde{\rho}(f)D(g)=q(\widetilde{\rho}(f))\cdot D(g)=\overline{\rho}_0(f)\cdot D(g)$$

holds, and therefore, viewing $\mathfrak{b}$ via $\overline{\rho}_0$ as a $B$-module, the two remaining terms in the above expression can be written as the actions $f\cdot D(g)$ and $D(f)\cdot g$. That is, $D$ satisfies the Leibniz rule

$$D(fg)=f\cdot D(g)+g\cdot D(f)$$

and is therefore an $A$-derivation. Conversely, for any $D\in \Der_A(B, \mathfrak{b})$, $\widetilde{\rho}+D$ is also an $A$-algebra homomorphism and satisfies $q\circ(\widetilde{\rho}+D)=\overline{\rho}_0$, so the freedom in choosing a lift of $\overline{\rho}_0$ is captured precisely by $\Der_A(B,\mathfrak{b})=\Hom_C(\Omega_{B/A}\otimes_BC,\mathfrak{b})$.

If to $D=\widetilde{\rho}'-\widetilde{\rho}\in\Der_A(B,\mathfrak{b})$ above we associate the $C$-linear map $h:\Omega_{B/A}\otimes_BC\rightarrow\mathfrak{b}$, then for any $f\in\mathfrak{a}$, it is given by

$$\delta'(\bar{f})-\delta(\bar{f})=D(f)=h(\dd{f}\otimes1)=h(\bar{d}(\bar{f}))$$

Here $\bar{d}: \mathfrak{a}/\mathfrak{a}^2\rightarrow\Omega_{B/A}\otimes_BC$ is the conormal morphism of [§Kähler Differentials and Cotangent Sheaves, ⁋Proposition 2](/en/math/scheme_theory/sheaf_of_differentials#prop2){: data-relation="required" }, and we see that $\delta'-\delta$ belongs to the image of $\bar{d}^\ast$. More importantly, the existence of a choice that kills $\mathfrak{a}$ is now equivalent to the existence of some $h:\Omega_{B/A}\otimes_BC\rightarrow \mathfrak{b}$ such that $\delta+\bar{d}^\ast(h)=0$, that is, that $\delta$ belongs to the image of $\bar{d}^\ast$. That is, to check this, it suffices to consider $\delta$ in the class

$$[\delta]\in\coker\left(\Hom_C(\Omega_{B/A}\otimes_BC,\mathfrak{b})\overset{\bar{d}^{\ast}}{\longrightarrow}\Hom_C(\mathfrak{a}/\mathfrak{a}^2,\mathfrak{b})\right)$$

and since the difference $\delta'-\delta=\bar{d}^\ast(h)$ between different lifts belongs to $\im\bar{d}^\ast$, this does not depend on the choice of $\widetilde{\rho}$. 

More generally, dualizing the complex

$$\NL_{C/A}=\left[\mathfrak{a}/\mathfrak{a}^2\overset{\bar{d}}{\longrightarrow}\Omega_{B/A}\otimes_BC\right]$$

by $\mathfrak{b}$, this is the first cohomology of the resulting complex $\Hom_C(\NL_{C/A}, \mathfrak{b})$. Hence the obstruction space measuring the lifting problem for the square-zero extension ($\ast$) having this $\mathfrak{b}$ as kernel is $H^1(\Hom_C(\NL_{C/A}, \mathfrak{b}))$, and if for every $\mathfrak{b}$ this becomes $0$, then $A\rightarrow C$ is smooth. Re-examining the proof of [§Smooth and Étale Morphisms, ⁋Theorem 15](/en/math/scheme_theory/smooth_and_etale_morphisms#thm15){: data-relation="weak" } based on this formalism, what was done in that proof was to settle it at the stage of the naive cotangent complex by showing that the conormal sequence is split exact. 

Giving names to the objects that have appeared so far, we have the following.

::: Definition 1
For an $A$-algebra $C$ and a polynomial algebra over $A$, $B$, with a presentation $C=B/\mathfrak{a}$, we call the complex above

$$\NL_{C/A}=\Bigl[\at{1}{\mathfrak{a}/\mathfrak{a}^2}\overset{\bar{d}}{\longrightarrow}\at{0}{\Omega_{B/A}\otimes_BC}\Bigr]$$

the *naive cotangent complex* of $C$, and write its homology groups as

$$H_1(\NL_{C/A})=\ker\bar{d},\qquad H_0(\NL_{C/A})=\coker\bar{d}$$

respectively. Also, for a $C$-module $M$, the cohomology of the cochain complex obtained by dualizing this by $M$,

$$\Hom_C(\NL_{C/A},M):\quad \at{0}{\Hom_C(\Omega_{B/A}\otimes_BC,M)}\overset{\bar{d}^\ast}{\rightarrow}\at{1}{\Hom_C(\mathfrak{a}/\mathfrak{a}^2,M)}$$

is written as

$$T^0(C/A,M)=\ker\bar{d}^\ast,\qquad T^1(C/A,M)=\coker\bar{d}^\ast$$
:::

These objects are already familiar to us. First, reading the conormal exact sequence of [§Kähler Differentials and Cotangent Sheaves, ⁋Proposition 2](/en/math/scheme_theory/sheaf_of_differentials#prop2){: data-relation="required" } at degree $0$, we obtain

$$H_0(\NL_{C/A})\cong\Omega_{C/A}$$

Moreover, in this case $H_0$ and $H_1$ do not depend on the choice of the presentation $C=B/\mathfrak{a}$. In the case of $T^0$, since a degree $0$ cocycle annihilates $\mathfrak{a}$ and descends to $C=B/\mathfrak{a}$ from a derivation $B\rightarrow M$, we immediately have $T^0(C/A,M)\cong\Der_A(C,M)\cong\Hom_C(\Omega_{C/A},M)$. Finally, since $T^1$ is by definition the cokernel where $[\delta]$ lies, it is simply the obstruction space obtained earlier with $\mathfrak{b}$ replaced by $M$.  

## Naive Cotangent Complex and Smoothness

In [§Smooth and Étale Morphisms, ⁋Proposition 8](/en/math/scheme_theory/smooth_and_etale_morphisms#prop8){: data-relation="required" }, smoothness appeared as the splitting of the conormal sequence, and in the introduction of this post we saw that the obstruction to lifting lies in $T^1$. These two descriptions are connected as follows.

::: Proposition 2
A finitely presented $A$-algebra $C$ is smooth over $A$ if and only if

$$H_1(\NL_{C/A})=0,\qquad \Omega_{C/A}\text{ is a finitely generated projective }C\text{-module}$$

holds. This is also equivalent to the condition that for every $C$-module $M$, $T^1(C/A,M)=0$.
:::
::: Proof
If $C$ is smooth, by [§Smooth and Étale Morphisms, ⁋Proposition 8](/en/math/scheme_theory/smooth_and_etale_morphisms#prop8){: data-relation="required" }, the conormal sequence

$$0\longrightarrow\mathfrak{a}/\mathfrak{a}^2\overset{\bar{d}}{\longrightarrow}\Omega_{B/A}\otimes_BC\longrightarrow\Omega_{C/A}\longrightarrow0$$

is a split short exact sequence. Therefore $H_1(\NL_{C/A})=\ker\bar{d}=0$, and since $\Omega_{C/A}$ is a direct summand of the finitely generated free module $\Omega_{B/A}\otimes_BC$, it is finitely generated projective.

Now suppose that $H_1(\NL_{C/A})=0$ and $\Omega_{C/A}$ is projective. The conormal sequence for the presentation $C=B/\mathfrak{a}$

$$\mathfrak{a}/\mathfrak{a}^2\overset{\bar{d}}{\longrightarrow}\Omega_{B/A}\otimes_BC\longrightarrow\Omega_{C/A}\longrightarrow0$$

is always right exact ([§Kähler Differentials and Cotangent Sheaves, ⁋Proposition 2](/en/math/scheme_theory/sheaf_of_differentials#prop2){: data-relation="required" }), and since the condition $H_1(\NL_{C/A})=\ker\bar{d}=0$ is given, we can append $0$ on the left to obtain a short exact sequence. Moreover, since $\Omega_{C/A}$ is projective, the surjection $\Omega_{B/A}\otimes_BC\rightarrow\Omega_{C/A}$ splits ([\[Multilinear Algebra\] §Projective, Injective, and Flat Modules, ⁋Proposition 4](/en/math/multilinear_algebra/various_modules#prop4){: data-relation="required" }). Therefore, by [§Smooth and Étale Morphisms, ⁋Proposition 8](/en/math/scheme_theory/smooth_and_etale_morphisms#prop8){: data-relation="required" }, $C$ is smooth over $A$.

Finally, we show that smoothness is equivalent to the condition that for every $C$-module $M$, $T^1(C/A,M)=0$. First, if $C$ is smooth, then by the splitting obtained above, we have $r\circ\bar{d}=\id$ for some retraction $r:\Omega_{B/A}\otimes_BC\rightarrow\mathfrak{a}/\mathfrak{a}^2$. Now, given any $C$-module $M$ and $\delta:\mathfrak{a}/\mathfrak{a}^2\rightarrow M$, setting $h=\delta\circ r$ yields $h\circ\bar{d}=\delta$, so $\bar{d}^\ast$ is surjective and $T^1(C/A,M)=0$. Conversely, suppose that for all $M$, $T^1(C/A,M)=0$. Then in any lifting problem from the introduction, $[\delta]\in T^1(C/A,\mathfrak{b})$ is $0$, so a lifting exists. Since $C$ is finitely presented, by [§Smooth and Étale Morphisms, ⁋Theorem 15](/en/math/scheme_theory/smooth_and_etale_morphisms#thm15){: data-relation="required" }, $C$ is smooth over $A$ .
:::

In particular, if $C$ is smooth, the splitting obtained in the above proof yields a splitting of the naive cotangent complex

$$\NL_{C/A}\cong \Bigl[\at{1}{\mathfrak{a}/\mathfrak{a}^2}\overset{\id}{\longrightarrow}\at{0}{\mathfrak{a}/\mathfrak{a}^2}\Bigr]\oplus\Bigl[\at{1}{0}\longrightarrow\at{0}{\Omega_{C/A}}\Bigr].$$

That is, if we denote by $p$ the projection onto the second summand, there is a short exact sequence

$$0\longrightarrow\ker p\longrightarrow\NL_{C/A}\overset{p}{\longrightarrow}[0\longrightarrow\Omega_{C/A}]\longrightarrow0,$$

and since

$$\ker p\cong\Bigl[\mathfrak{a}/\mathfrak{a}^2\overset{\id}{\longrightarrow}\mathfrak{a}/\mathfrak{a}^2\Bigr],$$

we have, for all $n$, $H_n(\ker p)=0$. Applying [\[Homological Algebra\] §Long Exact Sequences, ⁋Theorem 1](/en/math/homological_algebra/long_exact_sequence#thm1){: data-relation="required" } to the above short exact sequence, $H_n(p)$ becomes an isomorphism in all degrees, so $p$ is a quasi-isomorphism from $\NL_{C/A}$ to the degree $0$ projective module $\Omega_{C/A}$. That is, in this case, looking only at $\Omega_{C/A}$ suffices to compute the difference between liftings, $T^0(C/A,M)=\Hom_C(\Omega_{C/A},M)$, and the obstruction space $T^1$ preventing the existence of a lifting always vanishes.

However, for a general $C$, we must first examine whether the kernel of the conormal morphism and its image are direct summands. Since $\Omega_{C/A}$ is the cokernel of this morphism, dealing directly with these two conditions essentially requires $\NL_{C/A}$, which retains the preceding term and the morphism. A representative case of this situation is that of an lci ([§Complete Intersections, ⁋Definition 1](/en/math/scheme_theory/complete_intersections#def1){: data-relation="weak" }). In general non-lci situations, we may need to examine the entire cotangent complex to perform similar computations, but for an lci, the naive cotangent complex is quasi-isomorphic to the full cotangent complex. From this perspective, an lci can be viewed as a representative case where the necessary cotangent data can be read off directly from the naive cotangent complex.

To see a concrete situation, set $B=A[\x_1,\ldots,\x_n]$ and $C=B/\mathfrak{a}$, and suppose that $\mathfrak{a}=(f_1,\ldots,f_r)$ is generated by a $B$-regular sequence. The map sending the class of each $f_j$ defines a $C$-linear morphism

$$C^r\longrightarrow\mathfrak{a}/\mathfrak{a}^2,\qquad e_j\longmapsto\bar{f}_j$$

which is an isomorphism by [§Complete Intersections, ⁋Proposition 5](/en/math/scheme_theory/complete_intersections#prop5){: data-relation="required" } and its proof; hence in this case, the naive cotangent complex is given via the Jacobian by

$$\NL_{C/A}\cong\left[C^r\overset{\bar{d}}{\longrightarrow}C^n\right],\qquad\bar{d}(e_j)=\sum_i\overline{\frac{\partial f_j}{\partial\x_i}}\dd{\x_i}$$

and both terms are finitely generated free (hence finitely generated projective) $C$-modules. In a general lci situation, the morphism between these two free modules remains, but in the smooth situation examined above, the condition that $\bar{d}$ is a split injection is added, so that the complex reduces to a single degree $0$ projective module.

## First-Order Deformation Theory

Above, we have seen how the naive cotangent complex records the infinitesimal lifting property of smoothness. This complex also plays a central role in deformation theory.

The geometric starting point of deformation theory is to fix an $A$-scheme $X_0$, and, with a section $\t_0:\Spec A\rightarrow T$ equipping a pointed $A$-scheme $(T,\t_0)$, to look for a family $\pi:X\rightarrow T$ and an identification of the central fiber $X\times_T\Spec A\cong X_0$. As in [§Morphisms of Schemes, ⁋Example 10](/en/math/scheme_theory/morphism_of_schemes#ex10){: data-relation="weak" }, if we view a scheme morphism $\pi:X\rightarrow T$ as a family parameterized by $T$, this means looking at a family of schemes varying over $T$ whose fiber obtained along the section $\t_0$ is given by $X_0$. For this perspective, it is reasonable to require that $\pi$ be flat ([§Flat Morphisms](/en/math/scheme_theory/flat_morphisms){: data-relation="weak" }), and under this assumption, we compare the fibers by viewing them as the variation of a single object $X_0$.

As the simplest example, consider the node $X_0=\Spec\bigl(A[\x,\y]/(\x\y)\bigr)$ where two lines meet at the origin. The simplest way to deform this is to replace the equation $\x\y=0$ with $\x\y=\t$ and consider the family

$$\pi:X=\Spec\bigl(A[\t,\x,\y]/(\x\y-\t)\bigr)\longrightarrow\Spec A[\t].$$

At $\t=0$, this has $X_0$ as its fiber, and over the open set where $\t$ is inverted, both $\x$ and $\y$ become invertible, forming a smooth family. Moreover, by the relation $\x\y=\t$, every monomial can be uniquely reduced to one of $\t^n$, $\t^n\x^i$, or $\t^n\y^j$, so this coordinate ring has $\{1\}\cup\{\x^i\mid i\geq1\}\cup\{\y^j\mid j\geq1\}$ as a basis and is a free $A[\t]$-module. Therefore $\pi$ is flat. In other words, looking at this family allows us to see how the singularity at the origin of $X_0$ disappears along the parameter $\t$.

The first step in finding a deformation of a general scheme $X_0$ is to examine each of the infinitesimal directions at the central section $\t_0$ of the base. Setting $A[\epsilon]=A[\t]/(\t^2)$, a tangent direction of $(T,\t_0)$ relative to $A$ is expressed via its restriction at $\t=0$ to $\t_0$ as an $A$-morphism $\Spec A[\epsilon]\rightarrow T$ ([§Smooth and Étale Morphisms, §§Infinitesimal lifting criterion](/en/math/scheme_theory/smooth_and_etale_morphisms#infinitesimal-lifting-criterion){: data-relation="required" }). Pulling back $\pi:X\rightarrow T$ along this morphism yields a family over $\Spec A[\epsilon]$, which intuitively records how $X_0$ varies to first order along that tangent direction.

In reality, however, this parameter scheme $T$ and the family $\pi:X\rightarrow T$ over it are not given in advance; finding them is the very beginning of the problem. All that is initially given to us is that $X_0$ is an $S$-scheme, with only the structure morphism $X_0\rightarrow S$, and our strategy is to define the parameter scheme by extending the base $S$ in *all possible directions*. The process of infinitesimally thickening the base at each step is precisely given by square-zero extensions, and simultaneously with the parameter space, we define the fibers lying over the base $S$ thickened by this process.

::: Definition 3
Given a flat $A$-algebra $C$ and an arbitrary square-zero extension of $A$

$$0\longrightarrow \mathfrak{b}\longrightarrow A'\longrightarrow A\longrightarrow0$$

we define the following. 

1. A *deformation* of $C$ over $A'$ is a pair $(C',\iota)$ satisfying the following two conditions:
   - $C'$ is an $A'$-algebra that is flat over $A'$.
   - $\iota:C'\otimes_{A'}A\xrightarrow{\sim} C$ is an $A$-algebra isomorphism.

   {% diagram Math/Scheme_Theory/Deformation_Theory-1.svg width="5.60em" alt="deformation of algebra" %}

2. Two deformations $(C',\iota)$ and $(C'',\iota')$ are *isomorphic* if the equality $\iota'\circ(\psi\otimes\id_A)=\iota$ holds for some $A'$-algebra isomorphism $\psi:C'\rightarrow C''$.

   {% diagram Math/Scheme_Theory/Deformation_Theory-2.svg width="10.55em" alt="isomorphism of deformations" %}

In particular, a deformation in the case $A'=A[\epsilon]=A[\t]/(\t^2)$ is called a *first-order deformation* of $C$ over $A$.
:::

In general, given any square-zero extension 

$$0\rightarrow \mathfrak{b}\rightarrow A'\rightarrow A\rightarrow0$$

and, for an $A$-algebra $C$, a deformation $(C',\iota)$, applying $-\otimes_{A'}C'$ yields an exact sequence

$$0\longrightarrow \mathfrak{b}\otimes_A C\longrightarrow C'\overset{\bar{\iota}}{\longrightarrow} C\longrightarrow0$$

Here, $\bar{\iota}$ is the composition of the quotient $C'\rightarrow C'\otimes_{A'}A$ and $\iota$. Since $\mathfrak{b}\otimes_{A'} C'\cong \mathfrak{b}\otimes_A(A\otimes_{A'} C')\cong \mathfrak{b}\otimes_A C$ and $\mathfrak{b}^2=0$, $\mathfrak{b}\otimes_A C$ is a square-zero ideal of $C'$, and therefore this exact sequence is a square-zero extension of $C$. 

More generally, we can treat this classification problem for an arbitrary $A$-algebra $C$ and $C$-module $M$. Considering the following (square-zero) extensions

$$0\longrightarrow M\longrightarrow E\overset{p}{\longrightarrow} C\longrightarrow0$$

these, with morphisms given by the following commutative diagram

{% diagram Math/Scheme_Theory/Deformation_Theory-3.svg width="18.74em" alt="morphism of extensions" %}

form a category $\Ext_{\Alg{A}}(C,M)=\operatorname{Exal}_A(C,M)$, where these morphisms are all isomorphisms by [\[Homological Algebra\] §Diagram chasing, ⁋Corollary 3](/en/math/homological_algebra/diagram_chasing#cor3){: data-relation="required" }. That is, this category is a groupoid, and the isomorphism classes of square-zero extensions are partitioned according to whether a morphism exists between their objects. Indeed, suppose we are given arbitrary data

$$0\longrightarrow M\longrightarrow E\overset{p}{\longrightarrow} C\longrightarrow0$$

in the category above; if we express $C$ via a polynomial ring $B$ as a presentation $B/\mathfrak{a}$ and choose a lift $B\rightarrow E$, then by exactly the same principle as the lifting computation just before [Definition 1](#def1){: data-relation="required" }, a class $[\delta_E]\in T^1(C/A,M)$ corresponds, which is well-defined since it does not depend on the choice of the lift $B\rightarrow E$.

Furthermore, this correspondence also works in the opposite direction. Specifically, given a class $[\delta]\in T^1(C/A,M)$ represented by a $C$-linear map $\delta:\mathfrak{a}/\mathfrak{a}^2\rightarrow M$, if we define inside the trivial extension $B\oplus M$ the ideal

$$\mathfrak{a}_\delta=\{(f,-\delta(\bar{f}))\in B\oplus M\mid f\in\mathfrak{a}\}$$

then the quotient algebra $E_\delta=(B\oplus M)/\mathfrak{a}_\delta$, via the natural morphisms $m\mapsto\overline{(0,m)}$ and $\overline{(b,m)}\mapsto b+\mathfrak{a}$, defines a square-zero extension of $C$ by $M$. One can verify that this construction determines the isomorphism class independently of the choice of the representative $\delta$, and provides the inverse to the preceding correspondence. That is, the above correspondence is a bijection between the collection of isomorphism classes of square-zero extensions of $C$ by $M$, $\pi_0(\operatorname{Exal}_A(C,M))$, and $T^1(C/A,M)$, under which the split extension corresponds to $0$. In other words, $T^1(C/A,M)$ is the space classifying square-zero extensions of $C$ by $M$.

Viewing the lifting problem from the introduction from this perspective, we can first use the pullback of the given data $q:R\rightarrow R_0$ and $\rho_0:C\rightarrow R_0$ to define the extension

$$E=R\times_{R_0}C=\{(r,c)\in R\times C\mid q(r)=\rho_0(c)\}$$

which, via the projection $p:E\rightarrow C$, defines a square-zero extension of $C$ by $\mathfrak{b}$

$$0\longrightarrow\mathfrak{b}\longrightarrow E\overset{p}{\longrightarrow}C\longrightarrow0$$

Here, that $\rho_0$ has a lifting $\rho:C\rightarrow R$ is equivalent to $s(c)=(\rho(c),c)$ being a section of $p$ that is an $A$-algebra homomorphism, that is, to this extension being split; for this reason, we see that $[\delta]$ going to $0$ is equivalent to the existence of a lifting of $\rho_0$.

As seen earlier, the process of finding a deformation of a scheme $X_0$ is the task of infinitesimally thickening the base $S=\Spec A$ via square-zero extensions while simultaneously defining the fiber over it, and the first-order deformation we have just examined corresponds to the case where this extension of the base is given by the simplest dual numbers $A[\epsilon]$. We must now see in which direction the fiber $X_0=\Spec C$ lying over it thickens to form a flat family $X=\Spec C'$.

Let us examine this in the concrete language of equations. In our setting, since $X$ is an $S$-scheme locally of finite presentation, in this affine case $C$ can be represented via a polynomial ring in finitely many variables $B=A[\x_1,\ldots,\x_n]$ and a finitely generated ideal $\mathfrak{a}=(f_1,\ldots,f_m)$ as the quotient $C=B/\mathfrak{a}$. Then, in $B[\epsilon]=A[\epsilon][\x_1,\ldots,\x_n]$, the fiber-direction coordinates $\x_i$ and the $\epsilon$-direction are naturally separated. At this time, candidates for extending each equation $f_j\in B$ that defined the fiber around the central fiber are of the form $F_j=f_j+\epsilon g_j$, and the family deformed by these candidates will be expressed as $C'=B[\epsilon]/(F_1,\ldots,F_m)$. Here, the only condition is that the family obtained in this way must actually be a flat family.

::: Proposition 4
In the situation above, suppose that $C$ is flat over $A$. Then $C'$ is flat over $A[\epsilon]$ if and only if for any relation $(a_1,\ldots,a_m)$ among $(f_1,\ldots,f_m)$, that is, any $(a_j)\in B^m$ such that $\sum_ja_jf_j=0$,

$$\sum_{j}a_jg_j\in \mathfrak{a}$$

holds. When this condition holds, the original relation $(a_j)$ lifts to a relation among $(F_1,\ldots,F_m)$.
:::
::: Proof
Since $C$ is flat over $A$, $C'$ being flat over $A[\epsilon]$ is equivalent to the exactness of the sequence

$$0\longrightarrow C\overset{\epsilon}{\longrightarrow}C'\longrightarrow C\longrightarrow0$$

given by multiplication by $\epsilon$ and reduction, that is, to $C'$ being a square-zero extension of $C$ by $C$. Here, since $\ker(C'\rightarrow C)$ is $\bigl(\epsilon B[\epsilon]+(F_1,\ldots,F_m)\bigr)/(F_1,\ldots,F_m)$, under $\epsilon B[\epsilon]\cong B$ this kernel becomes

$$\ker(C'\rightarrow C)\cong\epsilon B[\epsilon]\big/\bigl(\epsilon B[\epsilon]\cap(F_1,\ldots,F_m)\bigr)$$

so that the sequence above being exact is equivalent to $\epsilon B[\epsilon]\cap(F_1,\ldots,F_m)=\epsilon\mathfrak{a}$. Now, to compute this intersection, writing an element of $(F_1,\ldots,F_m)$ for $a_j,b_j\in B$ as

$$\sum_j(a_j+\epsilon b_j)F_j=\sum_ja_jf_j+\epsilon\Bigl(\sum_ja_jg_j+\sum_jb_jf_j\Bigr)$$

this belongs to $\epsilon B[\epsilon]$ if and only if $\sum_ja_jf_j=0$, that is, $(a_j)$ is a relation among $(f_1,\ldots,f_m)$. At this point, since $\sum_jb_jf_j$ runs over all of $\mathfrak{a}$, the intersection $\epsilon B[\epsilon]\cap(F_1,\ldots,F_m)$ is $\epsilon$ times the ideal generated by $\mathfrak{a}$ together with the values $\sum_ja_jg_j$ of the relations, and therefore this being equal to $\epsilon\mathfrak{a}$ is equivalent to $\sum_ja_jg_j\in\mathfrak{a}$ for every relation $(a_j)$. Finally, under this condition, if we write $\sum_ja_jg_j=\sum_jc_jf_j$ ($c_j\in B$), then for $A_j=a_j-\epsilon c_j$, we have

$$\sum_jA_jF_j=\sum_ja_jf_j+\epsilon\Bigl(\sum_ja_jg_j-\sum_jc_jf_j\Bigr)=0$$

so the original relation $(a_j)$ lifts.
:::

The proof of this proposition illustrates the process by which a flat family is obtained in a first-order deformation. That is, if relations defining the central fiber,

$$\sum a_jf_j=0$$

are given, then upon perturbing them via $F_j=f_j+\epsilon g_j$, the term $\sum a_jg_j$ in the resulting expression

$$\sum a_j(f_j+\epsilon g_j)=\epsilon\sum a_j g_j$$

is absorbed into $\mathfrak{a}$, so that it can be rewritten in terms of the $f_j$ as $\sum a_jg_j=\sum c_jf_j$; substituting this back into the original expression yields, for $A_j=a_j-\epsilon c_j$, the identity

$$\sum_j A_j F_j=0$$

which gives precisely the equations on the thickening.

If this condition holds, the assignment $\bar{f}_j\mapsto\bar{g}_j$ well-defines a $C$-module homomorphism

$$\varphi:\mathfrak{a}/\mathfrak{a}^2\rightarrow C$$

and conversely, any $\varphi\in\Hom_C(\mathfrak{a}/\mathfrak{a}^2,C)$ gives a first-order deformation by choosing $g_j\in B$ such that $\varphi(\bar{f}_j)=\bar{g}_j$. That is, the set of data consisting of a first-order deformation together with a lift $B\rightarrow C'$ of the presentation $B\twoheadrightarrow C$ corresponds naturally to $\Hom_C(\mathfrak{a}/\mathfrak{a}^2,C)$, which reinterprets $\delta\in\Hom_C(\mathfrak{a}/\mathfrak{a}^2,\mathfrak{b})$ obtained from the extension data in the introduction in the language of equations in the case $\mathfrak{b}=C$.

It now remains to filter out which of these give trivial deformations. In the case of first-order deformations, a deformation isomorphic to $C'=C[\epsilon]$ is called *trivial*. The simplest among these is the case where all $g_j=0$ so that $F_j=f_j$, which is nothing more than copying and extending the equations defining the central fiber along the $\epsilon$ direction without any deformation.

However, even if $g_j\neq0$ so that the equations appear to be deformed, they may actually give a trivial deformation. Choose a derivation $\theta\in\Der_A(B,C)$, and choose a representative $\widetilde{\theta}(\x_i)\in B$ for each $\theta(\x_i)\in C$. This choice uniquely determines an $A$-derivation $\widetilde{\theta}:B\rightarrow B$, which satisfies $\pi\circ\widetilde{\theta}=\theta$. Now, applying the coordinate change $\x_i\mapsto\x_i+\epsilon\widetilde{\theta}(\x_i)$ of $B[\epsilon]$ to the original equations $f_j$, they are sent to

$$f_j+\epsilon\sum_i\widetilde{\theta}(\x_i)\frac{\partial f_j}{\partial\x_i}=f_j+\epsilon\widetilde{\theta}(f_j)$$

Therefore, the equations $F_j=f_j+\epsilon g_j$ chosen with $g_j=\widetilde{\theta}(f_j)\in B$ are obtained by a coordinate change of the ambient space, and the family they define is isomorphic to the original trivial family $C'=C[\epsilon]$. Since $\bar{g}_j=\theta(f_j)\in C$ in this case, the corresponding $\varphi$ is given by $\bar{f}_j\mapsto\theta(f_j)$. Generalizing this, trivial deformations are obtained precisely when $\varphi$ comes from a derivation, that is, when it lies in the image of the composition

$$\Der_A(B,C)=\Hom_C(\Omega_{B/A}\otimes_BC,C)\overset{\bar{d}^\ast}{\rightarrow}\Hom_C(\mathfrak{a}/\mathfrak{a}^2,C)$$

which is the same phenomenon as the degree of freedom in choosing the lift $\widetilde{\rho}$ being contained in $\Der_A(B,\mathfrak{b})$ in the calculation immediately preceding [Definition 1](#def1){: data-relation="weak" }.

We now assemble what we have obtained in this section into a single classification theorem.

::: Theorem 5
For a finitely presented $A$-algebra $C=B/\mathfrak{a}$, the exact sequence

$$0\longrightarrow T^0(C/A,C)\longrightarrow\Der_A(B,C)\overset{\bar{d}^\ast}{\longrightarrow}\Hom_C(\mathfrak{a}/\mathfrak{a}^2,C)\longrightarrow T^1(C/A,C)\longrightarrow0$$

holds, and each term has the following meaning in deformation theory.
1. $\Hom_C(\mathfrak{a}/\mathfrak{a}^2,C)$ classifies the data of a first-order deformation of $C$ together with a lift $B\rightarrow C'$ of the presentation $B\twoheadrightarrow C$.
2. Since two deformations are isomorphic if and only if their difference lies in the space $\im\bar{d}^\ast$ of trivial deformations, the set of isomorphism classes of first-order deformations is in natural bijection with the quotient
$$\Hom_C(\mathfrak{a}/\mathfrak{a}^2,C)\big/\im\bar{d}^\ast=T^1(C/A,C)$$
Under this correspondence, the trivial deformation corresponds to $0\in T^1$.
3. The infinitesimal automorphism group of any deformation $C'$ is isomorphic to $\ker\bar{d}^\ast$, the stabilizer of coordinate changes, namely $T^0(C/A,C)=\Der_A(C,C)$.
:::

::: Example 6 (Nodal curve)
Let us rigorously compute the node $\x\y=0$ examined earlier. Let $B=A[\x,\y]$, $f(\x,\y)=\x\y$, $\mathfrak{a}=(f)$, and let $C=B/\mathfrak{a}$, $X_0=\Spec C$. In this case, a first-order deformation is given by

$$F=f+\epsilon g\in B[\epsilon],\qquad C'=B[\epsilon]/(F)$$

for some $g\in B$. Intuitively, $\Spec C'$ is obtained by extending $\Spec A$ in the infinitesimal direction, thickening $X_0$ along the fat point $\Spec A'=\Spec A[\epsilon]$ defined along this direction; the choice of $g$ encodes the information of how it is thickened. More concretely, we saw in [Theorem 5](#thm5){: data-relation="required" } that the resulting $C$-linear map

$$\varphi:\mathfrak{a}/\mathfrak{a}^2\longrightarrow C,\qquad \bar{f}\longmapsto\bar{g}$$

captures precisely all the information about the first-order deformation. That is, the choice of $g$ determines the deformation. 

For example, if we choose $g=\x$, then

$$F=\x\y+\epsilon\x=\x(\y+\epsilon)$$

so this transforms the original equation $f=\x\y$ by the coordinate change $\y\mapsto\y+\epsilon$. Since this coordinate change restricts to the identity at $\epsilon=0$ and induces an isomorphism $C[\epsilon]\cong C'$, the choice $g=\x$ defines a trivial deformation.

{% diagram Math/Scheme_Theory/Deformation_Theory-4.svg width="12.56em" alt="trivial deformation of node" %}

More generally, according to [Theorem 5](#thm5){: data-relation="required" }, a trivial deformation is one that comes from an infinitesimal coordinate change of the ambient space $B[\epsilon]$, that is, the case where $\varphi\in\im\bar{d}^\ast$. As examined just before [Theorem 5](#thm5){: data-relation="required" }, such a coordinate change is determined by a derivation $\theta\in\Der_A(B,C)$, which concretely defined the deformation on each equation via the value $\theta(f_j)$. In our example, since $B=A[\x,\y]$ is a polynomial ring, any derivation $\theta\in\Der_A(B,C)$ is uniquely determined by the values on the two variables

$$\theta(\x)=a,\qquad \theta(\y)=b\qquad(a,b\in C)$$

and the variation it induces on the equation $f=\x\y$ is given by

$$\theta(f)=\theta(\x\y)=\theta(\x)\y+\x\theta(\y)=a\y+b\x\tag{$\ast\ast$}$$

Then $\bar{d}^\ast(\theta)$ is defined by sending the (unique) basis $\bar{f}$ of $\mathfrak{a}/\mathfrak{a}^2$ to this value $\theta(f)\in C$, so we see that $\varphi\in\im \bar{d}^\ast$ is equivalent to $\bar{g}$ being of the form ($\ast\ast$). In particular, the case $g=\x$ examined earlier corresponds to $a=0$ and $b=1$. 

Conversely, choosing $\bar{g}$ not belonging to this image yields a nontrivial deformation, and from the above calculation we see that any $g$ with a nonzero constant term is such an element. For example, choosing $g=-1$, we obtain

$$F=\x\y-\epsilon,\qquad C'=A[\epsilon][\x,\y]/(\x\y-\epsilon),\qquad X'=\Spec C'$$

This corresponds to $-1\in T^1(C/A,C)\cong A$, and is therefore nontrivial when $A\neq0$.

{% diagram Math/Scheme_Theory/Deformation_Theory-5.svg width="12.56em" alt="smoothing of node" %}

The reason why the latter case yields a nontrivial deformation can also be understood from the following intuitive calculation. The origin of the nodal curve $X_0=\Spec C$ is given by the ring homomorphism sending both $\x,\y$ to $0$. In a trivial deformation, this ring homomorphism extends to $C[\epsilon]\rightarrow A[\epsilon]$, but in the case of

$$C'=A[\epsilon][\x,\y]/(\x\y-\epsilon)$$

above, if an $A[\epsilon]$-algebra homomorphism $C'\rightarrow A[\epsilon]$ extending $\x,\y\mapsto 0$ exists, it must be of the form $\x\mapsto \epsilon u$, $\y\mapsto \epsilon v$; however, such a map gives

$$\x\y\mapsto (\epsilon u)(\epsilon v)=0$$

and thus does not factor through the ideal $\x\y-\epsilon$ of $A[\epsilon,\x,\y]$. That is, among the $A[\epsilon]$-algebra homomorphisms from $C'$ to $A'=A[\epsilon]$, none extends the homomorphism corresponding to the origin, which is the algebraic explanation for the phenomenon seen above where the hyperbolas miss the origin. 
:::

## Obstructions to Deformation and Higher-Order Deformation Theory

So far, we have constructed first-order deformations of an $A$-algebra $C$ and classified their isomorphism classes by $T^1(C/A,C)$. Now our interest is in lifting a given first-order deformation to a deformation of higher order. If a one-parameter flat family were already given, we would simply truncate it at the $\t^2, \t^3, \ldots$ terms and examine each order successively; however, as seen in the introduction to the previous section, our goal is to construct such a family, so the situation is not so simple. 

To examine this intuitively, let us return to the presentation fixed earlier:

$$C=B/\mathfrak{a},\qquad B=A[\x_1,\ldots,\x_n],\qquad \mathfrak{a}=(f_1,\ldots,f_m)$$

Then the equations for a first-order deformation were those of the form

$$F_j=f_j+\t g_j\in B[\t]/(\t^2)$$

for $g_j$ satisfying the flatness condition, and to raise this by one order, we must choose $h_j\in B$ and construct

$$F_j^{(2)}=f_j+\t g_j+\t^2h_j\in B[\t]/(\t^3)$$

What is essential here is that we must choose the $h_j$ so that the algebra defined in this way,

$$C^{(2)}=\bigl(B[\t]/(\t^3)\bigr)/(F_1^{(2)},\ldots,F_m^{(2)})$$

is flat over $A[\t]/(\t^3)$, and this condition can be computed as follows. 

Recall that in [Proposition 4](#prop4){: data-relation="required" }, flatness appeared as the condition that relations among the original equations are lifted simultaneously. Concretely, suppose a relation $\sum_j a_jf_j=0$ among the equations defining $C$ is given; when we lift these equations to

$$F_j=f_j+\epsilon g_j$$

then in the equation

$$\sum_j a_j(f_j+\epsilon g_j)=\epsilon\sum_j a_j g_j$$

if we can rewrite $\sum_j a_jg_j$ as an expression in the $f_j$ as $\sum_j a_jg_j=\sum_j c_jf_j$, we could absorb this error into the $a_j$ by defining $A_j=a_j-\epsilon c_j$ to ensure that $\sum_j A_j F_j=0$ holds. 

Replacing $\epsilon$ by $\t$ in the proof of [Proposition 4](#prop4){: data-relation="required" } and repeating the same ideal calculation in $B[\t]/(\t^{n+1})$, flatness at each stage likewise appears as the condition that the relations are lifted together. Therefore, to extend this to second order, we must choose suitable $d_j\in B$ to construct the coefficients of the relation

$$A_j^{(2)}=a_j-\t c_j+\t^2d_j\in B[\t]/(\t^3)$$

and to find the condition they must satisfy, we expand the product of the two expressions in $B[\t]/(\t^3)$:

$$\begin{aligned}\sum_j A_j^{(2)}F_j^{(2)}&=\sum_j(a_j-\t c_j+\t^2d_j)(f_j+\t g_j+\t^2h_j)\\
&=\sum_j a_jf_j+\t\Bigl(\sum_j a_jg_j-\sum_j c_jf_j\Bigr)+\t^2\Bigl(\sum_j a_jh_j-\sum_j c_jg_j+\sum_j d_jf_j\Bigr)\end{aligned}$$

In this expression, the $\t^0$ term on the right-hand side is $0$ because it is the original relation, and the $\t^1$ term is $0$ because it was already chosen to satisfy flatness at first order. Now, for this to become $0$ in $B[\t]/(\t^3)$, what remains is the $\t^2$ term; since $\sum_j d_jf_j\in\mathfrak{a}$, this condition appears as the equation

$$\sum_j a_jh_j\equiv\sum_j c_jg_j\pmod{\mathfrak{a}}$$

The problem is that the right-hand side of this congruence is a value already determined to satisfy the first-order deformation, which in general may not be $0$; because of this, it is in general impossible to choose the $h_j$ so that the above congruence is satisfied *for every given* relation $(a_1, \ldots, a_m)$. This is where it differs from first-order deformations: in a first-order deformation, the right-hand side of the equation

$$\sum_j a_j g_j\equiv 0\pmod{\mathfrak{a}}$$

was $0$, so at the very least, it was always possible to satisfy this equation by setting all $g_j$ to $0$ and choosing the trivial deformation. However, once a nontrivial first-order deformation is given, the right-hand side forms a fixed nonzero residual term, so it can no longer be satisfied by a choice such as $h_j=0$. The algebraic record of this failure, which remains uncancelled even after allowing all possible corrections $h_j$, is precisely the *obstruction class*. 

Earlier, we saw that information about first-order deformations is contained in the cohomology modules $T^0$ and $T^1$ of the naive cotangent complex. A natural question then is what space this obstruction class lives in. However, since the information that can be obtained from the naive cotangent complex is essentially only $T^0$ and $T^1$, to obtain information about the second-order terms we need an object with more terms than the naive cotangent complex. 

To this end, let us examine more concretely the role of the relations appearing in the earlier calculation. First, a *relation* among the equations $f_1, \ldots, f_m$ defining $C$, which we have already used multiple times, is an $m$-tuple of coefficients $(a_1, \ldots, a_m)\in B^m$ satisfying $\sum_j a_jf_j=0$; these are formally elements of the kernel $\Rel$ of the surjection

$$B^m\rightarrow\mathfrak{a};\qquad e_j\mapsto f_j$$

By a *trivial relation* among these equations, we mean a trivial relation that these equations must satisfy by the commutativity of $B$, such as $f_if_j-f_jf_i=0$. As an element of $B^m$, this corresponds to the element $f_ie_j-f_je_i\in\Rel$ whose $j$-th component is $f_i$, whose $i$-th component is $-f_j$, and whose remaining components are $0$. Let $\TrivRel\subseteq\Rel$ be the submodule generated by these elements. Since these trivial relations always hold by the commutativity of $B$, they play no role in creating obstructions. Therefore, we may consider the quotient module $\Rel/\TrivRel$ obtained by removing them from $\Rel$.

::: Definition 7
For a finitely presented $A$-algebra $C=B/\mathfrak{a}$, the *Lichtenbaum–Schlessinger complex* $\operatorname{LS}_{C/A}$ is defined by

$$\operatorname{LS}_{C/A}=\Bigl[\at{2}{\Rel/\TrivRel}\overset{d_2}{\longrightarrow}\at{1}{B^m\otimes_BC}\overset{d_1}{\longrightarrow}\at{0}{\Omega_{B/A}\otimes_BC}\Bigr]$$

with differentials

$$d_2\bigl(\overline{(a_1,\ldots,a_m)}\bigr)=\sum_j\overline{a_j}e_j,\qquad d_1(e_j)=\dd{f_j}\otimes1$$

For each $i=0,1,2$, the functor

$$T^i(C/A,M)=H^i\bigl(\Hom_C(\operatorname{LS}_{C/A},M)\bigr)$$

is called the *Lichtenbaum–Schlessinger functor* of $C$.
:::

It is not difficult to see that $T^0$ and $T^1$ in this definition coincide exactly with those defined in [Definition 1](#def1){: data-relation="required" }, and our claim is that the obstruction class is a class living in $T^2$. For a first-order deformation $\xi$, as in the earlier calculation, for each relation $(a_1,\ldots,a_m)\in\Rel$, choosing elements satisfying $\sum_ja_jg_j=\sum_jc_jf_j$, namely $c_j\in B$, we obtain

$$\eta(a_1,\ldots, a_m)=\overline{\sum_jc_jg_j}\in C$$

Here, the difference with respect to another choice of $c_j$ is again an element of $\Rel$, and by the flatness condition on $g_j$, its image in $C$ is $0$ and it vanishes on $\TrivRel$; thus this yields a well-defined $C$-linear map $\eta: \Rel/\TrivRel\rightarrow C$, and we can define its class as $\ob(\xi)=[\eta]\in T^2(C/A,C)$. Moreover, $\ob(\xi)$ depends neither on the choice of $g_j$ nor on the choice of presentation $C=B/\mathfrak{a}$, and is therefore an invariant of $\xi$ alone.

As seen in the earlier calculation, the condition for the existence of a second-order deformation over $A[\t]/(\t^3)$ was that for every relation $a$, the congruence

$$\sum_jc_jg_j\equiv\sum_ja_jh_j\pmod{\mathfrak{a}}$$

is satisfied by some $h_j\in B$. Now, the right-hand side is the coboundary induced by $h=(\bar{h}_1,\ldots,\bar{h}_m)\in\Hom_C(B^m\otimes_BC,C)$ via the differential $d_2$, evaluated at $a$. Therefore, the existence of such $h_j$ is precisely equivalent to $\eta$ being a coboundary, that is, $[\eta]=0\in T^2(C/A,C)$, and it is precisely in this case that a second-order deformation exists. That is, the following holds.

::: Theorem 8
For a first-order deformation $\xi\in T^1(C/A,C)$, an extension to a flat deformation over $A[\t]/(\t^3)$ exists if and only if $\ob(\xi)=0$.
:::

For a general square-zero extension $0\rightarrow \mathfrak{b}\rightarrow R'\rightarrow R\rightarrow0$, repeating the same calculation by replacing powers of $\t$ with perturbations along $\mathfrak{b}$, we obtain an obstruction class; when an extension exists, applying the argument of [Theorem 5](#thm5){: data-relation="required" } to the difference between two extensions shows that their isomorphism classes form a torsor over $T^1$.

The calculations so far generalize to the more general full cotangent complex. To this end, instead of representing the $A$-algebra $C$ as a quotient of a polynomial algebra once, we choose a free simplicial resolution whose terms are polynomial $A$-algebras,

$$P_\bullet\overset{\sim}{\rightarrow}C$$

and take Kähler differentials in each degree. The resulting simplicial $C$-module

$$\LL_{C/A}=\Omega_{P_\bullet/A}\otimes_{P_\bullet}C$$

viewed as a chain complex, is the *cotangent complex* of $C$ over $A$. Here, as with the two complexes above, we write $\LL_{C/A}$ in homological degrees; when viewing it in the derived category under the cohomological convention, we read this as $(\LL_{C/A})^{-i}=(\LL_{C/A})_i$. Therefore, the homological truncation $\tau_{\leq r}$ below corresponds to $\tau_{\geq-r}$ in cohomological notation. In this post, we do not use the explicit construction of a free simplicial resolution, but only the properties concerning truncations and deformations that follow from this definition. The key property of $\LL_{C/A}$ defined in this way is that it generalizes the two complexes defined earlier, which appear as truncations of $\LL_{C/A}$:

$$\tau_{\leq1}\LL_{C/A}\simeq\NL_{C/A},\qquad \tau_{\leq2}\LL_{C/A}\simeq\operatorname{LS}_{C/A}$$

Therefore, setting, for any $C$-module $M$,

$$T^i(C/A,M)=\Ext^i_C(\LL_{C/A},M)$$

$T^0$ represents infinitesimal automorphisms, $T^1$ represents first-order deformations and the differences between choices of extensions when an extension exists ([Theorem 5](#thm5){: data-relation="weak" }), and $T^2$ controls the obstructions to extensions ([Theorem 8](#thm8){: data-relation="weak" }). Applying the smoothness criterion of [Proposition 2](#prop2){: data-relation="required" } to the full cotangent complex, we now obtain the following conclusion for deformations in all degrees.

::: Proposition 9
If $C$ is smooth over $A$, then for every $C$-module $M$,

$$T^i(C/A,M)=0\qquad(i>0).$$

In particular, the problem of deforming $C$ along a square-zero extension has a solution without obstruction, and its isomorphism class is unique. In the case of a first-order deformation, this class is that of the trivial deformation, and the infinitesimal automorphisms of each deformation are classified by $T^0(C/A,C)=\Der_A(C,C)$.
:::
::: Proof
The cotangent complex $\LL_{C/A}$ of a smooth $C$ is quasi-isomorphic to $\Omega_{C/A}$ in degree $0$, and since this module is projective, for all $i>0$ we have

$$T^i(C/A,M)=\Ext^i_C(\LL_{C/A},M)=\Ext^i_C(\Omega_{C/A},M)=0.$$
:::

As we saw earlier, for an affine lci algebra $C$ over $A$, $\LL_{C/A}$ is quasi-isomorphic to the naive cotangent complex consisting of two projective modules, so $T^i(C/A,M)=0$ holds for all $i\geq2$. Therefore, the obstruction at each step vanishes and we can continuously extend a first-order deformation to a formal deformation; in such cases, we say it is *unobstructed* in the sense that there is no obstruction class. For general non-lci algebras, higher homology of $\LL_{C/A}$ can remain, and the Lichtenbaum–Schlessinger complex displays up to degree $2$, which is needed for classical deformations and obstructions, while the full cotangent complex preserves even higher relations beyond that.

## General Deformation Theory

So far, we have treated deformations of affine schemes. In the computation immediately following [Definition 3](#def3){: data-relation="required" }, we saw that if we deform $C$ along an arbitrary square-zero extension

$$0\rightarrow M\rightarrow A'\rightarrow A\rightarrow0$$

then the reduction of the deformation $C'$ to the central fiber yields a square-zero extension

$$0\rightarrow M_C\rightarrow C'\rightarrow C\rightarrow0$$

whose kernel is identified with the $C$-module $M_C=M\otimes_AC$. Therefore, the problem of finding a deformation of $C$ over $A'$ reduces to finding a square-zero extension $C'$ of $C$ by $M_C$ that is compatible with the extension of the base.

The content of the previous section was that the existence of such an extension is governed by an *obstruction class*. Specifically, choosing a presentation $C=B/(f_1,\ldots,f_m)$ and candidate lifts $F_j$ of the equations over $A'$, we can collect the errors in the direction of the kernel left by the lifts of each relation $\sum_ja_jf_j=0$ to obtain a $C$-linear map

$$\eta:\Rel/\TrivRel\rightarrow M_C$$

where changing the choices of presentation and lifts changes $\eta$ by a coboundary, so that its class $[\eta]\in T^2(C/A,M_C)$ is well-defined. This class is precisely the obstruction class, and we know that $[\eta]=0$ is equivalent to the existence of such a square-zero extension $C'$. From this perspective, the earlier [Theorem 8](#thm8){: data-relation="weak" } was the result for the special case of lifting a first-order deformation $\xi$ to second order. Then, when the obstruction vanishes, the isomorphism classes of deformations form a torsor over $T^1(C/A,M_C)$, and the infinitesimal automorphisms of each deformation are classified by $T^0(C/A,M_C)$.

Now what remains is to lift this computation to general schemes. For this, we must first fix a square-zero thickening of the base, construct a flat family over each affine patch, and then choose isomorphisms identifying these families on the overlap of two patches. Finally, these isomorphisms must satisfy the cocycle condition on triple overlaps in order to yield a single deformation of schemes. Moreover, the cotangent complex must also be computed on each affine patch and glued compatibly with restrictions. Rather than repeating this entire process, in this section we clarify what data and obstructions appear at which levels, and summarize how they assemble into a single global $\Ext$.

First, the simplest direction is to extend the initially given base space $S$ from an affine scheme to a general scheme. For a quasi-coherent module $\mathcal{I}$ on $S$, if we equip $\mathcal{O}_S\oplus\mathcal{I}$ with the multiplication

$$(a,u)(b,v)=(ab,av+bu)$$

then this becomes an $\mathcal{O}_S$-algebra with $\mathcal{I}^2=0$. Then its relative spectrum $S[\mathcal{I}]=\rSpec_S(\mathcal{O}_S\oplus\mathcal{I})$ is a split square-zero thickening of $S$, and in particular, when $\mathcal{I}=\mathcal{O}_S$, we write this as $S[\epsilon]$. If $S=\Spec A$, this coincides with $\Spec(A[\epsilon])$ used earlier, and more generally, a closed embedding $S\hookrightarrow S'$ defined by a square-zero ideal sheaf $\mathcal{I}=\ker(\mathcal{O}_{S'}\rightarrow\mathcal{O}_S)$ can be used as a thickening of the base.

::: Definition 10
For a flat morphism $f:X_0\rightarrow S$ and a square-zero ideal sheaf $\mathcal{I}$ defining a closed embedding $i:S\hookrightarrow S'$, a *deformation* of $X_0$ over $S'$ means a flat $S'$-scheme $X$ and an $S$-isomorphism

$$\iota:X\times_{S'}S\xrightarrow{\sim}X_0$$

, given as a pair $(X,\iota)$. Two deformations $(X,\iota)$ and $(X',\iota')$ are *isomorphic* if the equality $\iota'\circ(\psi\times_{S'}S)=\iota$ holds for some $S'$-isomorphism $\psi:X\rightarrow X'$. In particular, a deformation in the case $S'=S[\epsilon]$ is called a *first-order deformation* of $X_0$ over $S$.
:::

This is merely a rewrite of [Definition 3](#def3){: data-relation="required" } using infinitesimal thickenings for general schemes as explained above. Indeed, since a square-zero thickening does not change the underlying topological space, $S$ and $S'$ have the same open subsets; in particular, corresponding to an affine open $V=\Spec A\subseteq S$, the subset $V'\subseteq S'$ is also affine, and writing $V'=\Spec A'$, the map $A'\twoheadrightarrow A$ is a square-zero extension. That is, intuitively, an infinitesimal thickening of $S$ can be thought of as performing compatible infinitesimal thickenings on each affine piece and then gluing them together. Likewise, the underlying space of the deformation $X$ is the same as the central fiber $X_0$, so $U\subseteq X_0$ directly determines an open set of $X$; thanks to this, the flatness and central fiber conditions of the deformation can be checked on affine open sets, and on each affine piece it reduces to the case of [Definition 3](#def3){: data-relation="required" }. In particular, taking an affine open over $V'=\Spec A'$ to be $U'=\Spec C'\subseteq X$ and setting $I=\ker(A'\rightarrow A)$, since $C'$ is flat over $A'$, tensoring $0\rightarrow I\rightarrow A'\rightarrow A\rightarrow0$ with $C'$ yields the sequence

$$0\longrightarrow I\otimes_{A'}C'\longrightarrow C'\longrightarrow C'/IC'\longrightarrow0$$

, which is exact; furthermore, since $I^2=0$, we have $I\otimes_{A'}C'\cong I\otimes_A(C'/IC')$, so the ideal sheaf of $X_0\hookrightarrow X$ is identified with $\mathcal{G}=f^\ast\mathcal{I}$. When everything is affine, setting $S=\Spec A$, $X_0=\Spec C$, and $\mathcal{I}=\widetilde{M}$, since

$$\mathcal{G}=f^\ast\mathcal{I}\cong\widetilde{M\otimes_A C}=\widetilde{M_C}$$

, $\mathcal{G}$ is obtained by sheafifying the coefficient module $M_C$ of the earlier affine case. In particular, for a first-order deformation, $M=A$, so $\mathcal{G}=\mathcal{O}_{X_0}$.

Now let us take an affine open cover of $X_0$, $X_0=\bigcup_iU_i$. By the discussion above, on each $U_i$ we can construct a deformation $U_i'$, but the problem of gluing them still remains. First, on each overlap $U_{ij}=U_i\cap U_j$, an isomorphism restricting to the identity map of the central fiber,

$$\varphi_{ij}:U_i'\vert_{U_{ij}}\xrightarrow{\sim}U_j'\vert_{U_{ij}}$$

, must be chosen as an $S'$-isomorphism, and on each triple overlap $U_{ijk}$, the condition $\varphi_{jk}\circ\varphi_{ij}=\varphi_{ik}$ must hold. Then, under these conditions, the $U_i'$ glue together into a single scheme $X$, and each structure morphism also glues to $X\rightarrow S'$; since flatness is a local condition on the source and the base, the morphism obtained this way is flat. That is, we obtain a deformation through this process. Conversely, it is clear that every deformation yields such data.

What simultaneously controls these three pieces of data (namely, the local deformations on affine pieces, the isomorphisms on overlaps of two pieces, and the cocycle condition on triple overlaps) is the cotangent complex. To this end, we must first transfer the complex defined in the affine setting to schemes. First, in the affine case, if $U=\Spec C\subseteq X_0$ and $V=\Spec A\subseteq S$ satisfy $f(U)\subseteq V$, we know that by sheafifying each term and differential of $\LL_{C/A}$, we obtain a complex consisting of quasi-coherent $\mathcal{O}_U$-modules and morphisms between them.

The issue is that the model of the naive cotangent complex defined on each of these affine pieces depends on the presentation of $C$, and in the process of extending this to the general cotangent complex, the choice of a resolution also enters. For this reason, these complexes are not termwise identical on each overlap, but are identified only via the canonical quasi-isomorphism

$$\widetilde{\LL_{C/A}}\xrightarrow{\sim}\LL_{X_0/S}\vert_U$$

. That is, the rigorous gluing takes place in the derived category $D(\mathcal{O}_{X_0})$ ([\[Homological Algebra\] §Derived Categories, ⁋Definition 2](/en/math/homological_algebra/derived_categories#def2){: data-relation="required" }), and we denote the resulting object by $\LL_{X_0/S}$.

Now, since $\LL_{X_0/S}$ is an object of the derived category, given on $X_0$ a quasi-coherent module $\mathcal{G}$ as coefficients, the degree $i$ data is computed by the formula

$$\Hom_{D(\mathcal{O}_{X_0})}(\LL_{X_0/S},\mathcal{G}[i])\cong H^i\bigl(R\Hom_{\mathcal{O}_{X_0}}(\LL_{X_0/S},\mathcal{G})\bigr)=\Ext^i_{\mathcal{O}_{X_0}}(\LL_{X_0/S},\mathcal{G})$$

. Here, the single complex $R\Hom_{\mathcal{O}_{X_0}}(\LL_{X_0/S},\mathcal{G})$ contains the coefficient data in all degrees together, and the shift $\mathcal{G}[i]$ is the notation for reading its $i$-th cohomology as a morphism set in the derived category ([\[Homological Algebra\] §Derived Categories, ⁋Proposition 10](/en/math/homological_algebra/derived_categories#prop10){: data-relation="required" }). We write this as

$$T^i(X_0/S,\mathcal{G})=\Ext^i_{\mathcal{O}_{X_0}}(\LL_{X_0/S},\mathcal{G}),\qquad T^i(X_0/S)=T^i(X_0/S,\mathcal{O}_{X_0})$$

. Then the following theorem summarizes what we have seen for affine schemes into a single statement.

::: Theorem 11 (Deformation theorem)
Let $f:X_0\rightarrow S$ be a flat, separated morphism locally of finite presentation, let $S\hookrightarrow S'$ be an extension defined by a square-zero ideal sheaf $\mathcal{I}$ of $S$, and let $\mathcal{G}=f^\ast\mathcal{I}$. Then there exists a canonical obstruction class

$$\ob(X_0/S')\in T^2(X_0/S,\mathcal{G})$$

such that a deformation over $S'$ exists if and only if $\ob(X_0/S')=0$. In this case, the isomorphism classes of deformations form a torsor over $T^1(X_0/S,\mathcal{G})$, and the infinitesimal automorphisms of each deformation are classified by $T^0(X_0/S,\mathcal{G})$.
:::

In particular, when $S'=S[\epsilon]$, the isomorphism classes of first-order deformations are in natural bijection with $T^1(X_0/S)$, where the trivial deformation corresponds to $0$.

Since the invariants $T^i(X_0/S)$ obtained in [Theorem 11](#thm11){: data-relation="required" } above are defined as the global $\Ext$ of the cotangent complex, to read off information directly on each affine piece we must consider the *sheaf Ext*

$$\sExt^q_{\mathcal{O}_{X_0}}(\mathcal{F},\mathcal{G})=R^q\sHom_{\mathcal{O}_{X_0}}(\mathcal{F},\mathcal{G})$$

This is the sheafification of the presheaf associating $\Ext^q_{\mathcal{O}_U}(\mathcal{F}\vert_U,\mathcal{G}\vert_U)$ to each open set $U$. In particular, the sheaf defined for $\mathcal{K}=\LL_{X_0/S}$,

$$\mathcal{T}_{X_0/S}^q=\sExt^q_{\mathcal{O}_{X_0}}(\LL_{X_0/S},\mathcal{O}_{X_0})$$

satisfies $\mathcal{T}_{X_0/S}^q(U)\cong T^q(C/A,C)$ on an affine open $U=\Spec C$, recovering the $T^i$ discussed in the previous sections.

Now, to relate the two, let us apply [\[Sheaf Theory\] §Derived Category of Sheaves and Derived Functors, ⁋Corollary 11](/en/math/sheaf_theory/derived_category_of_sheaves#cor11){: data-relation="required" } to $\mathcal{G}=\mathcal{O}_{X_0}$ and the truncation of the cotangent complex $\mathcal{K}=\tau_{\leq2}\LL_{X_0/S}$. Since $\mathcal{K}$ is a bounded complex with terms only in homological degrees $0,1,2$, that is, cohomological degrees $-2,-1,0$, it is an object of $D^+(\mathcal{O}_{X_0})$, and since the first term of the triangle $\tau_{\geq3}\LL_{X_0/S}\rightarrow\LL_{X_0/S}\rightarrow\mathcal{K}$ contributes to $\Ext$ only in degree $3$ and higher, $\mathcal{K}$ computes $T^i(X_0/S)$ and $\mathcal{T}^i_{X_0/S}$ for $i\leq2$. Furthermore, since $\LL_{X_0/S}$ is concentrated in non-negative homological degrees, $\mathcal{T}_{X_0/S}^q=0$ for $q<0$, and therefore this becomes a first-quadrant spectral sequence

$$E_2^{p,q}=H^p(X_0,\mathcal{T}_{X_0/S}^q)\Longrightarrow T^{p+q}(X_0/S)$$

Reading off the low-degree terms of this spectral sequence yields the following.

::: Theorem 12 (Local-to-global exact sequence)
Let $X_0$ be a scheme that is flat, separated, and locally of finite presentation over $S$. Then the exact sequence

$$0\longrightarrow H^1(X_0,\mathcal{T}_{X_0/S}^0)\longrightarrow T^1(X_0/S)\longrightarrow H^0(X_0,\mathcal{T}_{X_0/S}^1)\overset{d_2}{\longrightarrow}H^2(X_0,\mathcal{T}_{X_0/S}^0)\longrightarrow T^2(X_0/S)$$

holds.
:::
::: Proof
By [\[Homological Algebra\] §Spectral Sequences, ⁋Proposition 10](/en/math/homological_algebra/spectral_sequences#prop10){: data-relation="required" }, the filtration on $T^1(X_0/S)$ given by convergence yields a short exact sequence $0\rightarrow E_\infty^{1,0}\rightarrow T^1(X_0/S)\rightarrow E_\infty^{0,1}\rightarrow0$. By the first quadrant condition, $E_\infty^{1,0}=E_2^{1,0}$ and $E_\infty^{0,1}=\ker(d_2:E_2^{0,1}\rightarrow E_2^{2,0})$. On the other hand, in total degree $2$, we have $E_\infty^{2,0}=E_2^{2,0}/\im d_2$, which is isomorphic to the first term $F^2T^2(X_0/S)\subseteq T^2(X_0/S)$ of the convergence filtration. Splicing these together and substituting $E_2^{p,q}=H^p(X_0,\mathcal{T}_{X_0/S}^q)$, we obtain the given exact sequence.
:::

Each term of the above five-term exact sequence corresponds in an exact one-to-one manner to the three kinds of data examined earlier. First, the canonical morphism $T^1(X_0/S)\rightarrow H^0(X_0,\mathcal{T}_{X_0/S}^1)$ in the middle forgets the gluing data from a global deformation and retains only the local deformation classes on each affine piece. Therefore, its codomain $H^0(X_0,\mathcal{T}_{X_0/S}^1)$ is the collection of local deformation classes on each piece whose restrictions to overlaps are mutually compatible.

The kernel of this morphism on the left, $H^1(X_0,\mathcal{T}_{X_0/S}^0)$, classifies *locally trivial deformations* that are trivial on each affine piece but obtained by twisting the gluing isomorphisms on overlaps by infinitesimal automorphisms $\mathcal{T}_{X_0/S}^0$. Conversely, the differential $d_2:H^0(X_0,\mathcal{T}_{X_0/S}^1)\rightarrow H^2(X_0,\mathcal{T}_{X_0/S}^0)$ is the obstruction determining whether the cocycle condition holds on triple overlaps once representatives of compatible local deformations and overlap isomorphisms are chosen. That is, only those local classes with $d_2=0$ can finally be glued into a single complete scheme deformation in $T^1(X_0/S)$.

Moreover, in degree $0$, since $E_2^{0,0}=E_\infty^{0,0}$, there is a natural isomorphism $T^0(X_0/S)\cong H^0(X_0,\mathcal{T}_{X_0/S}^0)$, showing that a global infinitesimal automorphism consists precisely of global sections of local automorphisms on each piece.

::: Corollary 13
If $X_0$ is smooth over $S$, then for all $i$,

$$T^i(X_0/S)\cong H^i(X_0,\mathcal{T}_{X_0/S})$$

holds. In particular, $H^1(X_0,\mathcal{T}_{X_0/S})$ classifies the isomorphism classes of first-order deformations.
:::
::: Proof
In the smooth case, $\LL_{X_0/S}\simeq\Omega_{X_0/S}$ and $\Omega_{X_0/S}$ is locally free, so $\mathcal{T}_{X_0/S}^q=0$ for $q>0$ and $\mathcal{T}_{X_0/S}^0=\sHom_{\mathcal{O}_{X_0}}(\Omega_{X_0/S},\mathcal{O}_{X_0})=\mathcal{T}_{X_0/S}$. Thus the spectral sequence of [Theorem 12](#thm12){: data-relation="required" } degenerates to the single row $q=0$.
:::

---

**References**

**[Har]** R. Hartshorne, *Deformation theory*, Graduate Texts in Mathematics 257, Springer, 2010.  
**[Ill]** L. Illusie, *Complexe cotangent et déformations I, II*, Lecture Notes in Mathematics 239, 283, Springer, 1971--1972.  
**[Stacks]** The Stacks project authors, *The Stacks project*, [stacks.math.columbia.edu](https://stacks.math.columbia.edu).
