---
title: "Deformation Theory and the Cotangent Complex"
description: "We explain why Kähler differentials are insufficient by examining deformations and obstructions along square-zero extensions. After computing how the naive and full cotangent complexes measure deformations of affine algebras, we assemble local scheme deformations and gluing data via the local-to-global spectral sequence."
excerpt: "Square-zero extensions, first-order deformations, obstructions, and limitations of Kähler differentials"

categories: [Math / Scheme Theory]
permalink: /en/math/scheme_theory/deformation_theory
sidebar:
  nav: "scheme_theory-en"

date: 2026-09-03

weight: 22
translated_at: 2026-11-06T15:15:06+00:00
translation_source: antigravity-gemini-3.8-flash-high
---
## Naive Cotangent Complex

According to [§Smooth and Étale Morphisms, ⁋Theorem 15](/en/math/scheme_theory/smooth_and_etale_morphisms#thm15){: data-lid="pnsu5" }, a morphism of schemes $\varphi:X\rightarrow S$ that is locally of finite presentation is smooth if and only if for every affine $S$-scheme $T=\Spec R$ and every square-zero subscheme $T_0=\Spec R_0$, there always exists a lifting $\varrho:T\rightarrow X$ extending any $S$-morphism $\varrho_0:T_0\rightarrow X$ to $T$. Here, that $T_0$ is a *square-zero subscheme* of $T$ means that $T_0\hookrightarrow T$ is defined by a square-zero ideal sheaf $\mathcal{I}\subseteq\mathcal{O}_T$, and viewing this in the affine setting

$$S=\Spec A,\qquad X=\Spec C,\qquad\text{$C$ an $A$-algebra locally of finite presentation}$$

the closed embedding $T_0\hookrightarrow T$ corresponds to a square-zero extension

$$0\rightarrow\mathfrak{b}\rightarrow R\overset{q}{\rightarrow} R_0\rightarrow0\tag{$\ast$}$$

by a square-zero ideal $\mathfrak{b}\subseteq R$, and the $S$-morphism $\varrho_0$ corresponds to an $A$-algebra homomorphism $\rho_0:C\rightarrow R_0$. That is, in this situation, the smoothness of $\phi: A\rightarrow C$ was equivalent to the condition that for every square-zero extension ($\ast$) and every $\rho_0: C\rightarrow R_0$, there always exists a lifting $\rho: C\rightarrow R$.
 
Now since $C$ is an $A$-algebra locally of finite presentation, there exist a polynomial algebra $B=A[\x_1,\ldots,\x_n]$ and a finitely generated ideal $\mathfrak{a}$ of $B$ such that $C=B/\mathfrak{a}$. Consider the composition

$$\overline{\rho}_0:B\rightarrow C\overset{\rho_0}{\rightarrow}R_0$$

of the natural projection $\pi:B\twoheadrightarrow C$ and $\rho_0$. Then since $q$ is surjective, for each variable $\x_i$ we can choose $r_i\in R$ satisfying $q(r_i)=\overline{\rho}_0(\x_i)$, and by [\[Algebraic Structures\] §Algebras, ⁋Proposition 8](/en/math/algebraic_structures/algebras#prop8){: data-lid="7rl2f" }, the assignment $\x_i\mapsto r_i$ uniquely defines an $A$-algebra homomorphism $\widetilde{\rho}: B\rightarrow R$. This satisfies $q\circ \widetilde{\rho}=\overline{\rho}_0$, where each choice of $r_i$ has freedom by $\ker q=\mathfrak{b}$. 

What we originally seek is a lifting $\rho:C\rightarrow R$ from $C$. If the chosen $\widetilde{\rho}$ satisfies $\widetilde{\rho}(\mathfrak{a})=0$, then $\widetilde{\rho}$ directly factors through $C=B/\mathfrak{a}$ to induce the desired lifting $\rho$, but that is not all. As seen above, the definition of $\widetilde{\rho}$ has indeterminacy up to the lifts of the variables, so another choice of $\widetilde{\rho}$ might yield $\widetilde{\rho}(\mathfrak{a})=0$. Therefore, to determine the failure of this lifting, we must compute a quantity that is independent of the choice of $\widetilde{\rho}$.

To this end, let us first rewrite what it means for $\widetilde{\rho}(\mathfrak{a})=0$ to hold for a fixed $\widetilde{\rho}$. First, for any $f\in \mathfrak{a}$,

$$q(\widetilde{\rho}(f))=\overline{\rho}_0(f)=\rho_0(\pi(f))=\rho_0(0)=0$$

so the inclusion $\widetilde{\rho}(\mathfrak{a})\subseteq \ker q=\mathfrak{b}$ is clear. Moreover, for any $f,g\in \mathfrak{a}$,

$$\widetilde{\rho}(fg)=\widetilde{\rho}(f)\widetilde{\rho}(g)\in\mathfrak{b}^2=0$$

so the map

$$\delta: \mathfrak{a}/\mathfrak{a}^2\rightarrow \mathfrak{b};\qquad \bar{f}\mapsto \widetilde{\rho}(f)$$

is well-defined. Furthermore, the $\delta$ obtained this way is a $C$-linear map. Here, regarding $\mathfrak{a}$ as a $B$-module, the ideal $\mathfrak{a}$ of $B$ acts on $\mathfrak{a}/\mathfrak{a}^2$ by $0$, so it is endowed with a $C=B/\mathfrak{a}$-module structure; as for $\mathfrak{b}$, since $\mathfrak{b}^2=0$, the $R$-module structure on $\mathfrak{b}$ gives an $R_0=R/\mathfrak{b}$-module structure, which is viewed as a $C$-module via $\rho_0$. That is, for a fixed $\widetilde{\rho}$, the condition $\widetilde{\rho}(\mathfrak{a})=0$ is precisely equivalent to the $C$-linear map $\delta\in\Hom_C(\mathfrak{a}/\mathfrak{a}^2, \mathfrak{b})$ defined in this manner being $0$. 

Based on this, we can quantify the variation when changing the choice of $\widetilde{\rho}$. Let $\widetilde{\rho}$ and $\widetilde{\rho}'$ be two lifts of $\overline{\rho}_0$. Then from the equality $q\circ\widetilde{\rho}=q\circ\widetilde{\rho}'$, their difference $D=\widetilde{\rho}'-\widetilde{\rho}$ is an $A$-linear map from $B$ to $\ker q=\mathfrak{b}$. But

$$D(fg)=\widetilde{\rho}'(f)\widetilde{\rho}'(g)-\widetilde{\rho}(f)\widetilde{\rho}(g)=\left(\widetilde{\rho}(f)+D(f)\right)\left(\widetilde{\rho}(g)+D(g)\right)-\widetilde{\rho}(f)\widetilde{\rho}(g)=\widetilde{\rho}(f)D(g)+D(f)\widetilde{\rho}(g)+D(f)D(g)$$

and since $D(f),D(g)\in\mathfrak{b}$ and $\mathfrak{b}^2=0$, the last term $D(f)D(g)$ vanishes. Meanwhile, the $R$-module structure on $\mathfrak{b}$ is given via $q: R\rightarrow R_0$, so

$$\widetilde{\rho}(f)D(g)=q(\widetilde{\rho}(f))\cdot D(g)=\overline{\rho}_0(f)\cdot D(g)$$

holds, and hence the remaining two terms in the above expression can be written as the actions $f\cdot D(g)$ and $D(f)\cdot g$ when viewing $\mathfrak{b}$ as a $B$-module via $\overline{\rho}_0$. That is, $D$ satisfies the Leibniz rule

$$D(fg)=f\cdot D(g)+g\cdot D(f)$$

and is therefore an $A$-derivation. Conversely, for any $D\in \Der_A(B, \mathfrak{b})$, the map $\widetilde{\rho}+D$ is also an $A$-algebra homomorphism satisfying $q\circ(\widetilde{\rho}+D)=\overline{\rho}_0$, so the freedom in choosing a lift of $\overline{\rho}_0$ is captured precisely in $\Der_A(B,\mathfrak{b})=\Hom_C(\Omega_{B/A}\otimes_BC,\mathfrak{b})$.

If we let $h:\Omega_{B/A}\otimes_BC\rightarrow\mathfrak{b}$ be the $C$-linear map corresponding to $D=\widetilde{\rho}'-\widetilde{\rho}\in\Der_A(B,\mathfrak{b})$ above, then for any $f\in\mathfrak{a}$, it is given by

$$\delta'(\bar{f})-\delta(\bar{f})=D(f)=h(\dd{f}\otimes1)=h(\bar{d}(\bar{f}))$$

Here, $\bar{d}: \mathfrak{a}/\mathfrak{a}^2\rightarrow\Omega_{B/A}\otimes_BC$ is the conormal morphism of [§Differentials and Cotangent Sheaves, ⁋Proposition 2](/en/math/scheme_theory/sheaf_of_differentials#prop2){: data-lid="r4obf" }, and we see that $\delta'-\delta$ belongs to the image of $\bar{d}^\ast$. More importantly, the existence of a choice that annihilates $\mathfrak{a}$ is now equivalent to the existence of some $h:\Omega_{B/A}\otimes_BC\rightarrow \mathfrak{b}$ such that $\delta+\bar{d}^\ast(h)=0$, that is, $\delta$ belongs to the image of $\bar{d}^\ast$. Thus, to verify this, it suffices to examine $\delta$ in the class

$$[\delta]\in\coker\left(\Hom_C(\Omega_{B/A}\otimes_BC,\mathfrak{b})\overset{\bar{d}^{\ast}}{\rightarrow}\Hom_C(\mathfrak{a}/\mathfrak{a}^2,\mathfrak{b})\right)$$

which does not depend on the choice of $\widetilde{\rho}$ since the difference $\delta'-\delta=\bar{d}^\ast(h)$ between different lifts belongs to $\im\bar{d}^\ast$. 

More generally, this is the first cohomology of the complex $\Hom_C(\NL_{C/A}, \mathfrak{b})$ obtained by dualizing the complex

$$\NL_{C/A}=\left[\mathfrak{a}/\mathfrak{a}^2\overset{\bar{d}}{\rightarrow}\Omega_{B/A}\otimes_BC\right]$$

into $\mathfrak{b}$, so the obstruction space measuring the lifting problem for the square-zero extension ($\ast$) with kernel $\mathfrak{b}$ is $H^1(\Hom_C(\NL_{C/A}, \mathfrak{b}))$, and if this vanishes for all $\mathfrak{b}$, then $A\rightarrow C$ is smooth. Based on this formalization, looking back at the proof of [§Smooth and Étale Morphisms, ⁋Theorem 15](/en/math/scheme_theory/smooth_and_etale_morphisms#thm15){: data-lid="6hgti" }, what was done in that proof was settling this already at the stage of the naive cotangent complex by showing that the conormal sequence is split exact. 

We name the objects that have appeared so far as follows.

::: Definition 1
For an $A$-algebra $C$ and, over $A$, a polynomial algebra $B$ giving a presentation $C=B/\mathfrak{a}$, we call the above complex

$$\NL_{C/A}=\Bigl[\at{1}{\mathfrak{a}/\mathfrak{a}^2}\overset{\bar{d}}{\rightarrow}\at{0}{\Omega_{B/A}\otimes_BC}\Bigr]$$

the *naive cotangent complex* of $C$, and write its homology as

$$H_1(\NL_{C/A})=\ker\bar{d},\qquad H_0(\NL_{C/A})=\coker\bar{d}$$

respectively. Also, for a $C$-module $M$, we write the cohomology of the cochain complex dualized by $M$,

$$\Hom_C(\NL_{C/A},M):\quad \at{0}{\Hom_C(\Omega_{B/A}\otimes_BC,M)}\overset{\bar{d}^\ast}{\rightarrow}\at{1}{\Hom_C(\mathfrak{a}/\mathfrak{a}^2,M)}$$

as

$$T^0(C/A,M)=\ker\bar{d}^\ast,\qquad T^1(C/A,M)=\coker\bar{d}^\ast$$

:::

These objects are already familiar to us. First, reading the conormal exact sequence of [§Differentials and Cotangent Sheaves, ⁋Proposition 2](/en/math/scheme_theory/sheaf_of_differentials#prop2){: data-lid="2n5wj" } in degree $0$, we obtain

$$H_0(\NL_{C/A})\cong\Omega_{C/A}$$

Moreover, in this case $H_0$ and $H_1$ do not depend on the choice of presentation $C=B/\mathfrak{a}$. In the case of $T^0$, since a degree $0$ cocycle, by annihilating $\mathfrak{a}$, descends to $C=B/\mathfrak{a}$ as a derivation $B\rightarrow M$, we immediately have $T^0(C/A,M)\cong\Der_A(C,M)\cong\Hom_C(\Omega_{C/A},M)$. Finally, since $T^1$ is by definition the cokernel where $[\delta]$ lies, it is obtained simply by replacing $\mathfrak{b}$ by $M$ in the obstruction space obtained earlier.  

## Naive Cotangent Complex and Smoothness

In [§Smooth and Étale Morphisms, ⁋Proposition 8](/en/math/scheme_theory/smooth_and_etale_morphisms#prop8){: data-lid="34xje" }, smoothness appeared as the splitting of the conormal sequence, and in the introduction to this post we saw that the obstruction to lifting lies in $T^1$. These two descriptions are connected as follows.

::: Proposition 2
A finitely presented $A$-algebra $C$ is smooth over $A$ if and only if

$$H_1(\NL_{C/A})=0,\qquad \Omega_{C/A}\text{ is a finitely generated projective }C\text{-module}$$

holds. This is also equivalent to $T^1(C/A,M)=0$ for all $C$-modules $M$.
:::
::: Proof
If $C$ is smooth, by [§Smooth and Étale Morphisms, ⁋Proposition 8](/en/math/scheme_theory/smooth_and_etale_morphisms#prop8){: data-lid="odapy" }, the conormal sequence

$$0\rightarrow\mathfrak{a}/\mathfrak{a}^2\overset{\bar{d}}{\rightarrow}\Omega_{B/A}\otimes_BC\rightarrow\Omega_{C/A}\rightarrow0$$

is a split short exact sequence. Therefore, $H_1(\NL_{C/A})=\ker\bar{d}=0$, and since $\Omega_{C/A}$ is a direct summand of the finitely generated free module $\Omega_{B/A}\otimes_BC$, it is finitely generated projective.

Now suppose that $H_1(\NL_{C/A})=0$ and $\Omega_{C/A}$ is projective. The conormal sequence for a presentation $C=B/\mathfrak{a}$

$$\mathfrak{a}/\mathfrak{a}^2\overset{\bar{d}}{\rightarrow}\Omega_{B/A}\otimes_BC\rightarrow\Omega_{C/A}\rightarrow0$$

is always right exact ([§Differentials and Cotangent Sheaves, ⁋Proposition 2](/en/math/scheme_theory/sheaf_of_differentials#prop2){: data-lid="1fipr" }), and since the condition $H_1(\NL_{C/A})=\ker\bar{d}=0$ is given, we obtain a short exact sequence by appending $0$ to the left. Furthermore, since $\Omega_{C/A}$ is projective, the surjection $\Omega_{B/A}\otimes_BC\rightarrow\Omega_{C/A}$ splits ([\[Multilinear Algebra\] §Projective, Injective, and Flat Modules, ⁋Proposition 4](/en/math/multilinear_algebra/various_modules#prop4){: data-lid="dqrmi" }). Thus, by [§Smooth and Étale Morphisms, ⁋Proposition 8](/en/math/scheme_theory/smooth_and_etale_morphisms#prop8){: data-lid="sj7py" }, $C$ is smooth over $A$.

Finally, we show that smoothness is equivalent to $T^1(C/A,M)=0$ for all $C$-modules $M$. First, if $C$ is smooth, then from the splitting obtained above there exists a retraction $r:\Omega_{B/A}\otimes_BC\rightarrow\mathfrak{a}/\mathfrak{a}^2$ such that $r\circ\bar{d}=\id$. Now for any $C$-module $M$ and any $\delta:\mathfrak{a}/\mathfrak{a}^2\rightarrow M$, setting $h=\delta\circ r$ gives $h\circ\bar{d}=\delta$, so $\bar{d}^\ast$ is surjective and $T^1(C/A,M)=0$. Conversely, suppose that $T^1(C/A,M)=0$ for all $M$. Then for any lifting problem in the introduction, $[\delta]\in T^1(C/A,\mathfrak{b})$ is $0$, so a lifting exists. Since $C$ is finitely presented, by [§Smooth and Étale Morphisms, ⁋Theorem 15](/en/math/scheme_theory/smooth_and_etale_morphisms#thm15){: data-lid="71hn7" }, $C$ is smooth over $A$.
:::

In particular, if $C$ is smooth, from the splitting obtained in the proof above there is a splitting of the naive cotangent complex

$$\NL_{C/A}\cong \Bigl[\at{1}{\mathfrak{a}/\mathfrak{a}^2}\overset{\id}{\rightarrow}\at{0}{\mathfrak{a}/\mathfrak{a}^2}\Bigr]\oplus\Bigl[\at{1}{0}\rightarrow\at{0}{\Omega_{C/A}}\Bigr].$$

That is, denoting the projection onto the second summand by $p$, there is a short exact sequence

$$0\rightarrow\ker p\rightarrow\NL_{C/A}\overset{p}{\rightarrow}[0\rightarrow\Omega_{C/A}]\rightarrow0,$$

and since

$$\ker p\cong\Bigl[\mathfrak{a}/\mathfrak{a}^2\overset{\id}{\rightarrow}\mathfrak{a}/\mathfrak{a}^2\Bigr],$$

we have $H_n(\ker p)=0$ for all $n$. Applying [\[Homological Algebra\] §Long Exact Sequences, ⁋Theorem 1](/en/math/homological_algebra/long_exact_sequence#thm1){: data-lid="wwnua" } to the short exact sequence above, $H_n(p)$ is an isomorphism in all degrees, so $p$ becomes a quasi-isomorphism from $\NL_{C/A}$ to the projective module $\Omega_{C/A}$ in degree $0$. That is, in this case, looking only at $\Omega_{C/A}$ suffices to compute the difference of liftings $T^0(C/A,M)=\Hom_C(\Omega_{C/A},M)$, and the obstruction space $T^1$ obstructing the existence of a lifting always vanishes.

However, for a general $C$, one must first examine the kernel of the conormal morphism and whether its image is a direct summand. Since $\Omega_{C/A}$ is the cokernel of this morphism, directly addressing these two conditions essentially requires $\NL_{C/A}$, which retains the preceding term and the morphism. A representative instance of this situation is the case of complete intersections (lci). ([§Complete Intersections, ⁋Definition 1](/en/math/scheme_theory/complete_intersections#def1){: data-lid="cd9vj" }) In a general non-lci setting, one may need to examine the full cotangent complex to perform similar computations, but in the lci case, the naive cotangent complex is quasi-isomorphic to the full cotangent complex. From this viewpoint, lci can be thought of as a representative case where the necessary cotangent data can be read directly from the naive cotangent complex.

To see a concrete situation, let $B=A[\x_1,\ldots,\x_n]$ and $C=B/\mathfrak{a}$, and suppose that $\mathfrak{a}=(f_1,\ldots,f_r)$ is generated by a $B$-regular sequence. The $C$-linear morphism

$$C^r\rightarrow\mathfrak{a}/\mathfrak{a}^2,\qquad e_j\mapsto\bar{f}_j$$

sending the class of each $f_j$ is an isomorphism by [§Complete Intersections, ⁋Proposition 5](/en/math/scheme_theory/complete_intersections#prop5){: data-lid="6laqx" } and its proof, so in this case the naive cotangent complex is given via the Jacobian by

$$\NL_{C/A}\cong\left[C^r\overset{\bar{d}}{\rightarrow}C^n\right],\qquad\bar{d}(e_j)=\sum_i\overline{\frac{\partial f_j}{\partial\x_i}}\dd{\x_i},$$

and both terms are finitely generated free (hence finitely generated projective) $C$-modules. In a general lci situation, the morphism between these two free modules remains, but in the smooth situation examined above, the additional condition that $\bar{d}$ is a split injection reduces the complex to a single projective module in degree $0$.

## First-Order Deformation Theory

Previously, we saw how the naive cotangent complex records the infinitesimal lifting property of smoothness. This complex also plays a central role in deformation theory.

The geometric starting point of deformation theory is to fix an $A$-scheme $X_0$ and look for a family $\pi:X\rightarrow T$ over a pointed $A$-scheme $(T,\t_0)$ equipped with a section $\t_0:\Spec A\rightarrow T$, together with an identification $X\times_T\Spec A\cong X_0$ of the central fiber. Viewing a morphism of schemes $\pi:X\rightarrow T$ as a family parameterized by $T$ as in [§Morphisms of Schemes, ⁋Example 10](/en/math/scheme_theory/morphism_of_schemes#ex10){: data-lid="dohnh" }, this means considering a family of schemes varying over $T$ whose fiber along the section $\t_0$ is given by $X_0$. For this perspective, it is reasonable to require that $\pi$ be flat ([§Flat Morphisms](/en/math/scheme_theory/flat_morphisms){: data-lid="bjqez" }), and under this assumption, we view and compare the fibers as the varying forms of a single object $X_0$.

As the simplest example, consider a node $X_0=\Spec\bigl(A[\x,\y]/(\x\y)\bigr)$ where two lines intersect at the origin. The simplest way to deform this is to change the equation $\x\y=0$ to $\x\y=\t$ and consider the family

$$\pi:X=\Spec\bigl(A[\t,\x,\y]/(\x\y-\t)\bigr)\rightarrow\Spec A[\t].$$

This has $X_0$ as its fiber at $\t=0$, and on the open set where $\t$ is inverted, both $\x$ and $\y$ become invertible, forming a smooth family. Moreover, by the relation $\x\y=\t$, every monomial can be uniquely reduced to one of $\t^n$, $\t^n\x^i$, or $\t^n\y^j$, so this coordinate ring is a free $A[\t]$-module with basis $\{1\}\cup\{\x^i\mid i\geq1\}\cup\{\y^j\mid j\geq1\}$. Therefore, $\pi$ is flat. That is, by examining this family, we can see how the singularity at the origin of $X_0$ disappears along the parameter $\t$.

The first step in finding deformations of a general scheme $X_0$ is to inspect the infinitesimal directions at the central section $\t_0$ of the base one by one. Setting $A[\epsilon]=A[\t]/(\t^2)$, an $A$-relative tangent direction of $(T,\t_0)$ is represented by an $A$-morphism $\Spec A[\epsilon]\rightarrow T$ that restricts to $\t_0$ at $\t=0$ ([§Smooth and Étale Morphisms, §§Infinitesimal lifting criterion](/en/math/scheme_theory/smooth_and_etale_morphisms#infinitesimal-lifting-criterion){: data-lid="5bh3o" }). Pulling back $\pi:X\rightarrow T$ along this yields a family over $\Spec A[\epsilon]$, which intuitively records how $X_0$ varies up to first order along that tangent direction.

In practice, however, neither the parameter scheme $T$ nor the family $\pi:X\rightarrow T$ over it is given in advance, and finding them is the very beginning of the problem. What we are given initially is only the structure morphism $X_0\rightarrow S$ arising from $X_0$ being an $S$-scheme. To this end, the strategy we adopt is to define the parameter scheme by widening the base $S$ in *all possible directions*. Here, the process of infinitesimally thickening the base is precisely given by square-zero extensions, and simultaneously with the parameter space, we define the fibers lying over the base $S$ thickened through this process.

::: Definition 3
For a flat $A$-algebra $C$ and an arbitrary square-zero extension of $A$

$$0\rightarrow \mathfrak{b}\rightarrow A'\rightarrow A\rightarrow0$$

we define the following. 

1. A *deformation* of $C$ over $A'$ means a pair $(C',\iota)$ satisfying the following two conditions:
   - $C'$ is an $A'$-algebra that is flat over $A'$.
   - $\iota:C'\otimes_{A'}A\xrightarrow{\sim} C$ is an $A$-algebra isomorphism.

   {% diagram Math/Scheme_Theory/Deformation_Theory-1.svg width="5.60em" alt="deformation of algebra" %}

2. Two deformations $(C',\iota)$ and $(C'',\iota')$ being *isomorphic* means that the equality $\iota'\circ(\psi\otimes\id_A)=\iota$ is satisfied by an $A'$-algebra isomorphism $\psi:C'\rightarrow C''$.

   {% diagram Math/Scheme_Theory/Deformation_Theory-2.svg width="10.55em" alt="isomorphism of deformations" %}

In particular, a deformation in the case $A'=A[\epsilon]=A[\t]/(\t^2)$ is called a *first-order deformation* of $C$ over $A$.
:::

In general, given an arbitrary square-zero extension 

$$0\rightarrow \mathfrak{b}\rightarrow A'\rightarrow A\rightarrow0$$

and an $A$-algebra $C$ with a deformation $(C',\iota)$, applying $-\otimes_{A'}C'$ to it gives the exact sequence

$$0\rightarrow \mathfrak{b}\otimes_A C\rightarrow C'\overset{\bar{\iota}}{\rightarrow} C\rightarrow0$$

Here $\bar{\iota}$ is the composition of the quotient $C'\rightarrow C'\otimes_{A'}A$ and $\iota$; since $\mathfrak{b}\otimes_{A'} C'\cong \mathfrak{b}\otimes_A(A\otimes_{A'} C')\cong \mathfrak{b}\otimes_A C$ and $\mathfrak{b}^2=0$, the ideal $\mathfrak{b}\otimes_A C$ is a square-zero ideal of $C'$, and thus this exact sequence is a square-zero extension of $C$. 

More generally, we can treat this classification problem for an arbitrary $A$-algebra $C$ and $C$-module $M$. Considering the following (square-zero) extensions

$$0\rightarrow M\rightarrow E\overset{p}{\rightarrow} C\rightarrow0$$

they form a category $\Ext_{\Alg{A}}(C,M)=\operatorname{Exal}_A(C,M)$ having the following commutative diagrams as morphisms:

{% diagram Math/Scheme_Theory/Deformation_Theory-3.svg width="18.74em" alt="morphism of extensions" %}

where these morphisms are all isomorphisms by [\[Homological Algebra\] §Diagram chasing, ⁋Corollary 3](/en/math/homological_algebra/diagram_chasing#cor3){: data-lid="mj4ii" }. That is, this category is a groupoid, and the isomorphism classes of square-zero extensions are partitioned according to whether a morphism exists between their objects. In fact, suppose an arbitrary datum

$$0\rightarrow M\rightarrow E\overset{p}{\rightarrow} C\rightarrow0$$

in the above category is given. If we represent $C$ using a polynomial ring $B$ by a presentation $B/\mathfrak{a}$ and choose a lift $B\rightarrow E$, then by exactly the same principle as the lifting calculation just before [Definition 1](#def1){: data-lid="x4ncd" }, a class $[\delta_E]\in T^1(C/A,M)$ corresponds to it, which is well-defined since it does not depend on the chosen lift $B\rightarrow E$.

Moreover, this correspondence also works in the opposite direction. Specifically, given a representative of a class $[\delta]\in T^1(C/A,M)$, namely a $C$-linear map $\delta:\mathfrak{a}/\mathfrak{a}^2\rightarrow M$, if we define in the trivial extension $B\oplus M$ the ideal

$$\mathfrak{a}_\delta=\{(f,-\delta(\bar{f}))\in B\oplus M\mid f\in\mathfrak{a}\}$$

then the quotient algebra $E_\delta=(B\oplus M)/\mathfrak{a}_\delta$ defines, via the natural morphisms $m\mapsto\overline{(0,m)}$ and $\overline{(b,m)}\mapsto b+\mathfrak{a}$, a square-zero extension of $C$ by $M$. One can verify that this construction determines an isomorphism class independently of the choice of representative $\delta$ and gives the inverse of the previous correspondence. That is, the above correspondence is a one-to-one correspondence between the collection of isomorphism classes of square-zero extensions of $C$ by $M$, namely $\pi_0(\operatorname{Exal}_A(C,M))$, and $T^1(C/A,M)$, under which the split extension corresponds to $0$. In other words, $T^1(C/A,M)$ is the space that classifies square-zero extensions of $C$ by $M$.

Looking back at the lifting problem in the introduction from this perspective, we can first define, via the pullback of the given data $q:R\rightarrow R_0$ and $\rho_0:C\rightarrow R_0$, the following extension

$$E=R\times_{R_0}C=\{(r,c)\in R\times C\mid q(r)=\rho_0(c)\}$$

which, via the projection $p:E\rightarrow C$, defines a square-zero extension of $C$ by $\mathfrak{b}$

$$0\rightarrow\mathfrak{b}\rightarrow E\overset{p}{\rightarrow}C\rightarrow0$$

Here, that $\rho_0$ admits a lifting $\rho:C\rightarrow R$ is equivalent to $s(c)=(\rho(c),c)$ giving a section of $p$ as an $A$-algebra, that is, to this extension being split; for this reason, we see that $[\delta]$ mapping to $0$ is equivalent to the existence of a lifting of $\rho_0$.

As seen earlier, the process of finding a deformation of a scheme $X_0$ is the task of infinitesimally thickening the base $S=\Spec A$ through square-zero extensions while defining the fiber over it at the same time, and the first-order deformation we have just examined corresponds to the case where this extension of the base is given by the simplest case of dual numbers $A[\epsilon]$. We must now see in which directions the fiber $X_0=\Spec C$ lying over it thickens to form a flat family $X=\Spec C'$.

Let us examine this in the language of concrete equations. In our setting, $X$ is an $S$-scheme locally of finite presentation, so in this affine case, $C$ can be represented using a polynomial ring $B=A[\x_1,\ldots,\x_n]$ and a finitely generated ideal $\mathfrak{a}=(f_1,\ldots,f_m)$ as the quotient $C=B/\mathfrak{a}$. Then, in $B[\epsilon]=A[\epsilon][\x_1,\ldots,\x_n]$, the coordinates $\x_i$ in the fiber direction and the $\epsilon$ direction are naturally separated; here, candidates for extending each equation $f_j\in B$ that defined the fiber around the central fiber are of the form $F_j=f_j+\epsilon g_j$, and the family deformed by these candidates will be given by $C'=B[\epsilon]/(F_1,\ldots,F_m)$. At this point, the only condition is that the family obtained in this way must actually be a flat family.

::: Proposition 4
In the situation above, suppose that $C$ is flat over $A$. Then $C'$ is flat over $A[\epsilon]$ if and only if for every relation $(a_1,\ldots,a_m)$ of $(f_1,\ldots,f_m)$, that is, $(a_j)\in B^m$ such that $\sum_ja_jf_j=0$, we have

$$\sum_{j}a_jg_j\in \mathfrak{a}$$

When this condition holds, the original relation $(a_j)$ lifts to a relation of $(F_1,\ldots,F_m)$.
:::
::: Proof
Since $C$ is flat over $A$, the flatness of $C'$ over $A[\epsilon]$ is equivalent to the exactness of the sequence given by multiplication by $\epsilon$ and reduction

$$0\rightarrow C\overset{\epsilon}{\rightarrow}C'\rightarrow C\rightarrow0$$

that is, to $C'$ being a square-zero extension of $C$ by $C$. Here, since $\ker(C'\rightarrow C)$ is $\bigl(\epsilon B[\epsilon]+(F_1,\ldots,F_m)\bigr)/(F_1,\ldots,F_m)$, under $\epsilon B[\epsilon]\cong B$ this kernel becomes

$$\ker(C'\rightarrow C)\cong\epsilon B[\epsilon]\big/\bigl(\epsilon B[\epsilon]\cap(F_1,\ldots,F_m)\bigr)$$

so the exactness of the sequence above is equivalent to $\epsilon B[\epsilon]\cap(F_1,\ldots,F_m)=\epsilon\mathfrak{a}$. Now to compute this intersection, if we write an element of $(F_1,\ldots,F_m)$ for $a_j,b_j\in B$ as

$$\sum_j(a_j+\epsilon b_j)F_j=\sum_ja_jf_j+\epsilon\Bigl(\sum_ja_jg_j+\sum_jb_jf_j\Bigr)$$

then this belongs to $\epsilon B[\epsilon]$ if and only if $\sum_ja_jf_j=0$, that is, $(a_j)$ is a relation of $(f_1,\ldots,f_m)$. At this time, since $\sum_jb_jf_j$ runs through the entirety of $\mathfrak{a}$, the intersection $\epsilon B[\epsilon]\cap(F_1,\ldots,F_m)$ is $\epsilon$ times the ideal generated together by $\mathfrak{a}$ and the values $\sum_ja_jg_j$ of the relations; thus, this being equal to $\epsilon\mathfrak{a}$ is equivalent to $\sum_ja_jg_j\in\mathfrak{a}$ for every relation $(a_j)$. Finally, under this condition, if we set $\sum_ja_jg_j=\sum_jc_jf_j$ ($c_j\in B$), then for $A_j=a_j-\epsilon c_j$ we have

$$\sum_jA_jF_j=\sum_ja_jf_j+\epsilon\Bigl(\sum_ja_jg_j-\sum_jc_jf_j\Bigr)=0$$

so the original relation $(a_j)$ lifts.
:::

The proof of this proposition shows how a flat family is obtained in a first-order deformation: given relations defining the central fiber, that is,

$$\sum a_jf_j=0$$

when we perturb them via $F_j=f_j+\epsilon g_j$, in the resulting expression

$$\sum a_j(f_j+\epsilon g_j)=\epsilon\sum a_j g_j$$

the term $\sum a_jg_j$ is absorbed into $\mathfrak{a}$, so we can rewrite it back as an equation $\sum a_jg_j=\sum c_jf_j$ in the $f_j$; substituting this back into the original expression, for $A_j=a_j-\epsilon c_j$ the relation

$$\sum_j A_j F_j=0$$

holds, which gives the equations in the thickening.

If this condition holds, the assignment $\bar{f}_j\mapsto\bar{g}_j$ well-defines a $C$-module homomorphism

$$\varphi:\mathfrak{a}/\mathfrak{a}^2\rightarrow C$$

and conversely, any $\varphi\in\Hom_C(\mathfrak{a}/\mathfrak{a}^2,C)$ gives a first-order deformation by choosing $g_j\in B$ such that $\varphi(\bar{f}_j)=\bar{g}_j$. That is, the set of data consisting of a first-order deformation together with a lift of the presentation $B\twoheadrightarrow C$ to $B\rightarrow C'$ naturally corresponds to $\Hom_C(\mathfrak{a}/\mathfrak{a}^2,C)$; this reinterprets the homomorphism $\delta\in\Hom_C(\mathfrak{a}/\mathfrak{a}^2,\mathfrak{b})$ obtained from the extension data in the introduction in the language of equations when $\mathfrak{b}=C$.

It now remains to filter out which of these give trivial deformations. In the case of first-order deformations, a deformation isomorphic to $C'=C[\epsilon]$ is called *trivial*. The simplest among these is when all $g_j=0$ so that $F_j=f_j$, which merely copies and extends the equations defining the central fiber in the $\epsilon$-direction without any deformation.

However, even if $g_j\neq0$ and the equations appear to be deformed, there are cases where the deformation is actually trivial. Choose a derivation $\theta\in\Der_A(B,C)$ and pick representatives $\widetilde{\theta}(\x_i)\in B$ of each $\theta(\x_i)\in C$. This choice uniquely determines an $A$-derivation $\widetilde{\theta}:B\rightarrow B$ satisfying $\pi\circ\widetilde{\theta}=\theta$. Now, applying the coordinate change $\x_i\mapsto\x_i+\epsilon\widetilde{\theta}(\x_i)$ of $B[\epsilon]$ to the original equations $f_j$, they are transformed into

$$f_j+\epsilon\sum_i\widetilde{\theta}(\x_i)\frac{\partial f_j}{\partial\x_i}=f_j+\epsilon\widetilde{\theta}(f_j)$$

Therefore, the equations $F_j=f_j+\epsilon g_j$ obtained by choosing $g_j=\widetilde{\theta}(f_j)\in B$ arise from a coordinate change of the ambient space, and the family they define is isomorphic to the original trivial family $C'=C[\epsilon]$. Here, since $\bar{g}_j=\theta(f_j)\in C$, the corresponding $\varphi$ is given by $\bar{f}_j\mapsto\theta(f_j)$. Generalizing this, trivial deformations are obtained precisely when $\varphi$ comes from a derivation, that is, when it belongs to the image of the composition

$$\Der_A(B,C)=\Hom_C(\Omega_{B/A}\otimes_BC,C)\overset{\bar{d}^\ast}{\rightarrow}\Hom_C(\mathfrak{a}/\mathfrak{a}^2,C)$$

which is the same phenomenon as in the calculation just before [Definition 1](#def1){: data-lid="peajb" }, where the freedom of choosing a lift $\widetilde{\rho}$ was contained in $\Der_A(B,\mathfrak{b})$.

We now assemble what we have obtained in this section into a single classification theorem.

::: Theorem 5
For a finitely presented $A$-algebra $C=B/\mathfrak{a}$, the exact sequence

$$0\rightarrow T^0(C/A,C)\rightarrow\Der_A(B,C)\overset{\bar{d}^\ast}{\rightarrow}\Hom_C(\mathfrak{a}/\mathfrak{a}^2,C)\rightarrow T^1(C/A,C)\rightarrow0$$

holds, where each term has the following interpretation in deformation theory:
1. $\Hom_C(\mathfrak{a}/\mathfrak{a}^2,C)$ classifies the data of a first-order deformation of $C$ together with a lift of the presentation $B\twoheadrightarrow C$ to $B\rightarrow C'$.
2. Since two deformations are isomorphic if and only if their difference lies in the space of trivial deformations $\im\bar{d}^\ast$, the set of first-order deformations up to isomorphism is in natural bijection with the quotient
$$\Hom_C(\mathfrak{a}/\mathfrak{a}^2,C)\big/\im\bar{d}^\ast=T^1(C/A,C)$$
Under this bijection, the trivial deformation corresponds to $0\in T^1$.
3. The infinitesimal automorphism group of any deformation $C'$ is isomorphic to the stabilizer of coordinate changes, $\ker\bar{d}^\ast$, namely $T^0(C/A,C)=\Der_A(C,C)$.
:::

::: Example 6 (Nodal curve)
Let us rigorously compute the node $\x\y=0$ examined earlier. Let $B=A[\x,\y]$, $f(\x,\y)=\x\y$, $\mathfrak{a}=(f)$, and let $C=B/\mathfrak{a}$, $X_0=\Spec C$. In this case, a first-order deformation is given, for some $g\in B$, by

$$F=f+\epsilon g\in B[\epsilon],\qquad C'=B[\epsilon]/(F)$$

. Intuitively, $\Spec C'$ extends $\Spec A$ in the infinitesimal direction, and extends $X_0$ along the fat point $\Spec A'=\Spec A[\epsilon]$ defined along this direction; the information on how it is extended is contained in the choice of $g$. More specifically, we saw in [Theorem 5](#thm5){: data-lid="059xx" } that the following $C$-linear map

$$\varphi:\mathfrak{a}/\mathfrak{a}^2\rightarrow C,\qquad \bar{f}\mapsto\bar{g}$$

induced by this choice precisely carries all the information about the first-order deformation. That is, the choice of $g$ determines the deformation. 

For example, if we choose $g=\x$, then

$$F=\x\y+\epsilon\x=\x(\y+\epsilon)$$

so this transforms the original equation $f=\x\y$ by the coordinate change $\y\mapsto\y+\epsilon$. Since this coordinate change restricts to the identity at $\epsilon=0$ and induces $C[\epsilon]\cong C'$, $g=\x$ defines a trivial deformation.

{% diagram Math/Scheme_Theory/Deformation_Theory-4.svg width="12.56em" alt="trivial deformation of node" %}

More generally, according to [Theorem 5](#thm5){: data-lid="l61ff" }, a trivial deformation is one that comes from an infinitesimal coordinate transformation of the ambient space $B[\epsilon]$, that is, when $\varphi\in\im\bar{d}^\ast$. As we saw right before [Theorem 5](#thm5){: data-lid="33mif" }, such a coordinate transformation is determined by a derivation $\theta\in\Der_A(B,C)$, and specifically we defined the deformation on each equation via the value $\theta(f_j)$. In our example, $B=A[\x,\y]$ is a polynomial ring, so any derivation $\theta\in\Der_A(B,C)$ is uniquely determined by the values on the two variables

$$\theta(\x)=a,\qquad \theta(\y)=b\qquad(a,b\in C)$$

and the variation it gives to the equation $f=\x\y$ is given by

$$\theta(f)=\theta(\x\y)=\theta(\x)\y+\x\theta(\y)=a\y+b\x\tag{$\ast\ast$}$$

. Then $\bar{d}^\ast(\theta)$ is defined by sending the (unique) basis $\bar{f}$ of $\mathfrak{a}/\mathfrak{a}^2$ to this value $\theta(f)\in C$, and hence we see that $\varphi$ belonging to $\im \bar{d}^\ast$ is equivalent to $\bar{g}$ being of the form ($\ast\ast$). In particular, the case $g=\x$ examined earlier corresponds to $a=0$ and $b=1$. 

Conversely, choosing $\bar{g}$ not in this image yields a nontrivial deformation, and from the above calculation we see that a $g$ with a nonzero constant term is such an element. For instance, choosing $g=-1$, we obtain

$$F=\x\y-\epsilon,\qquad C'=A[\epsilon][\x,\y]/(\x\y-\epsilon),\qquad X'=\Spec C'$$

. This corresponds to $-1\in T^1(C/A,C)\cong A$, so it is nontrivial whenever $A\neq0$.

{% diagram Math/Scheme_Theory/Deformation_Theory-5.svg width="12.56em" alt="smoothing of node" %}

The reason why the latter case is a nontrivial deformation can also be obtained from an intuitive calculation as follows. The origin of the nodal curve $X_0=\Spec C$ is given by the ring homomorphism sending both $\x$ and $\y$ to $0$. In a trivial deformation, this ring homomorphism extends to $C[\epsilon]\rightarrow A[\epsilon]$, but in the case of the above

$$C'=A[\epsilon][\x,\y]/(\x\y-\epsilon)$$

, if there were an $A[\epsilon]$-algebra homomorphism $C'\rightarrow A[\epsilon]$ extending $\x,\y\mapsto 0$, it must be of the form $\x\mapsto \epsilon u$, $\y\mapsto \epsilon v$; however, for such a map,

$$\x\y\mapsto (\epsilon u)(\epsilon v)=0$$

so it does not factor through the ideal $\x\y-\epsilon$ of $A[\epsilon,\x,\y]$. That is, among the $A[\epsilon]$-algebra homomorphisms from $C'$ to $A'=A[\epsilon]$, none extends the homomorphism corresponding to the origin, which is an algebraic explanation of the phenomenon seen above where the hyperbolas miss the origin. 
:::

## Obstructions to Deformation and Higher-Order Deformation Theory

So far, we have constructed first-order deformations of an $A$-algebra $C$ and classified their isomorphism classes by $T^1(C/A,C)$. Now our interest is in lifting a given first-order deformation to a deformation of higher order. 

Here, the role of higher-order terms can be understood as the problem of moving a point inside a space. For example, on the circle $\x^2+\y^2=1$ over the real numbers, to move the point $(1,0)$ with velocity $(0,1)$, to first order we may set $\x=1$, $\y=\t$. The problem is that substituting this in yields $\x^2+\y^2-1=\t^2$, so this direction satisfies the equation over $\mathbb{R}[\t]/(\t^2)$, but no longer over $\mathbb{R}[\t]/(\t^3)$. Intuitively, this is because the moment it moves in the $(0,1)$ direction, the point leaves the circle; to stay on the circle, the path must curve to the left while maintaining the initial velocity, and the higher-order terms play this role. Indeed, if we correct it by $\x=1-\t^2/2$, $\y=\t$, then

$$\left(1-\frac{\t^2}{2}\right)^2+\t^2-1=\frac{\t^4}{4}$$

so it satisfies the equation up to second order. This correction term determines the acceleration without changing the initial velocity, and in general, the Taylor expansion of $\x=\sqrt{1-\t^2}$, $\y=\t$ at $\t=0$ gives a correction satisfying the equation to all orders.

The following is an example where such a correction is impossible.

::: Example 7 (Point on a node)
In [Example 6](#ex6){: data-lid="dx6hj" }, we deformed the node $C=A[\x,\y]/(\x\y)$ itself. This time, let us move its origin $\x,\y\mapsto0$ via the lifting problem just before [Definition 1](#def1){: data-lid="0r607" }. At first order, since $(a\t)(b\t)=0$, for any $a,b\in A$, the map $\x\mapsto a\t$, $\y\mapsto b\t$ defines $C\rightarrow A[\t]/(\t^2)$.

When we fix the curve and move only the point, for its lift to $A[\t]/(\t^3)$ given by $\x\mapsto a\t+a'\t^2$, $\y\mapsto b\t+b'\t^2$, we have

$$\x\y\mapsto(a\t+a'\t^2)(b\t+b'\t^2)\equiv ab\t^2\pmod{\t^3}$$

. The corrections $a',b'$ do not appear in the coefficient of $\t^2$, because the coefficients $\x,\y$ of $\bar{d}(\overline{\x\y})=\y\dd{\x}+\x\dd{\y}$ act as $0$ on $\mathfrak{b}=(\t^2)$, so that $\bar{d}^\ast=0$. Therefore, the obstruction is $ab\in T^1(C/A,\mathfrak{b})\cong A$, and the velocity $(a,b)$ extends to second order if and only if $ab=0$.

Now let us also move the curve along with the family $\x\y=\s$. This is the problem of moving the origin of $\widetilde{C}=A[\s,\x,\y]/(\x\y-\s)$, and setting $\s\mapsto c\t+c'\t^2$ yields

$$\x\y-\s\mapsto-c\t+(ab-c')\t^2\pmod{\t^3}$$

. If $c\neq0$ at first order, the curve becomes $\x\y=c\t$, namely the nontrivial deformation in [Example 6](#ex6){: data-lid="o3v5z" }, and as we saw there, there is no point on it extending the origin. Therefore, $c=0$ is forced at first order. However, at second order, choosing $c'=ab$ makes the error vanish. Indeed, a new term $-\dd{\s}$ appears in $\bar{d}(\overline{\x\y-\s})$, so that $\bar{d}^\ast$ becomes surjective and $T^1(\widetilde{C}/A,\mathfrak{b})=0$.

In other words, while the corrections $a',b'$ cannot alter the error $ab\t^2$ on a fixed curve, the second-order deformation $c'\t^2$ of the curve cancels it directly. For example, $(\x,\y)=(\t,\t)$ does not extend to second order on $\x\y=0$, nor can it lie on the hyperbola $\x\y=c\t$ smoothed out at first order; however, it lies at all orders on the hyperbola $\x\y=\t^2$ smoothed out at second order.
:::

Now, to study the problem of extending deformations of $C$ itself, let us return to the presentation

$$C=B/\mathfrak{a},\qquad B=A[\x_1,\ldots,\x_n],\qquad \mathfrak{a}=(f_1,\ldots,f_m)$$

fixed earlier. Then the equations for a first-order deformation were those of the form

$$F_j=f_j+\t g_j\in B[\t]/(\t^2)$$

for $g_j$ satisfying the flatness condition; to lift this by one higher order, we must choose $h_j\in B$ to construct

$$F_j^{(2)}=f_j+\t g_j+\t^2h_j\in B[\t]/(\t^3)$$

. The essential requirement here is that we must choose the $h_j$ so that the algebra defined in this way,

$$C^{(2)}=\bigl(B[\t]/(\t^3)\bigr)/(F_1^{(2)},\ldots,F_m^{(2)})$$

, is flat over $A[\t]/(\t^3)$, and this condition can be computed as follows.

Recall that in [Proposition 4](#prop4){: data-lid="a75je" }, flatness appeared as the condition of simultaneously lifting the relations between the original equations. Specifically, given a relation $\sum_j a_jf_j=0$ between the equations defining $C$, when we lift them to

$$F_j=f_j+\epsilon g_j$$

, in the equation

$$\sum_j a_j(f_j+\epsilon g_j)=\epsilon\sum_j a_j g_j$$

, if we could rewrite $\sum_j a_jg_j$ in terms of the $f_j$ as $\sum_j a_jg_j=\sum_j c_jf_j$, then by shifting this error to the $a_j$ and defining $A_j=a_j-\epsilon c_j$, we could make $\sum_j A_j F_j=0$ hold.

If we replace $\epsilon$ by $\t$ in the proof of [Proposition 4](#prop4){: data-lid="5adhy" } and repeat the same ideal-theoretic computation in $B[\t]/(\t^{n+1})$, flatness at each step similarly manifests as the condition that relations are simultaneously lifted. Therefore, to extend this to second order, we must choose suitable $d_j\in B$ to construct the coefficients of the relation

$$A_j^{(2)}=a_j-\t c_j+\t^2d_j\in B[\t]/(\t^3)$$

; to find the condition this must satisfy, we actually expand the product of the two expressions in $B[\t]/(\t^3)$ to examine

$$\begin{aligned}\sum_j A_j^{(2)}F_j^{(2)}&=\sum_j(a_j-\t c_j+\t^2d_j)(f_j+\t g_j+\t^2h_j)\\
&=\sum_j a_jf_j+\t\Bigl(\sum_j a_jg_j-\sum_j c_jf_j\Bigr)+\t^2\Bigl(\sum_j a_jh_j-\sum_j c_jg_j+\sum_j d_jf_j\Bigr)\end{aligned}$$

. In this expression, the $\t^0$ term on the right-hand side is $0$ because it is the original relation, and the $\t^1$ term is $0$ because it was already chosen to satisfy flatness at first order. Now, in order for this to be $0$ in $B[\t]/(\t^3)$, what remains is the $\t^2$ term; since $\sum_j d_jf_j\in\mathfrak{a}$, this condition appears as the congruence

$$\sum_j a_jh_j\equiv\sum_j c_jg_j\pmod{\mathfrak{a}}$$

. The issue is that the right-hand side of this congruence is a value already determined to satisfy the first-order deformation, which in general may not be $0$; for this reason, it is in general impossible to choose the $h_j$ such that the above congruence is satisfied *whenever* relations $(a_1, \ldots, a_m)$ are given. This is where it differs from first-order deformations: in a first-order deformation, since the right-hand side of the congruence

$$\sum_j a_j g_j\equiv 0\pmod{\mathfrak{a}}$$

was $0$, satisfying this equation itself was always possible at the very least by setting all $g_j$ to $0$ to take the trivial deformation. However, once a nontrivial first-order deformation is already given, the right-hand side forms a fixed nonzero residual term, so it can no longer be satisfied by a choice like $h_j=0$. The algebraic record of this failure, which persists without being canceled even after allowing all possible corrections $h_j$, is precisely the *obstruction class*.

Earlier, we saw that the information about first-order deformations is contained in the cohomologies $T^0$ and $T^1$ of the naive cotangent complex. A natural question then is what space this obstruction class lives in. However, since the information obtainable from the naive cotangent complex is essentially only $T^0$ and $T^1$, to obtain information about second-order terms, we need an object with more terms than the naive cotangent complex.

To this end, let us examine the role of the relations appearing in the preceding calculation in detail. First, a *relation* among the equations $f_1, \ldots, f_m$ defining $C$, which we have already used multiple times, is an $m$-tuple of coefficients $(a_1, \ldots, a_m)\in B^m$ satisfying $\sum_j a_jf_j=0$; formally, these are the elements of the kernel $\Rel$ of the surjection

$$B^m\rightarrow\mathfrak{a};\qquad e_j\mapsto f_j$$

. A *trivial relation* among these equations refers to the trivial relations that these equations must satisfy by the commutativity of $B$, such as the equation $f_if_j-f_jf_i=0$. As an element of $B^m$, this corresponds to the element $f_ie_j-f_je_i\in\Rel$ whose $j$-th component is $f_i$, whose $i$-th component is $-f_j$, and whose remaining components are $0$; let $\TrivRel\subseteq\Rel$ be the submodule generated by such elements. Since these trivial relations always hold by the commutativity of $B$, they play no role in producing obstructions. Therefore, it suffices to consider the quotient module $\Rel/\TrivRel$ obtained by removing them from $\Rel$.

::: Definition 8
For a finitely presented $A$-algebra $C=B/\mathfrak{a}$, the *Lichtenbaum–Schlessinger complex* $\operatorname{LS}_{C/A}$ is defined by

$$\operatorname{LS}_{C/A}=\Bigl[\at{2}{\Rel/\TrivRel}\overset{d_2}{\rightarrow}\at{1}{B^m\otimes_BC}\overset{d_1}{\rightarrow}\at{0}{\Omega_{B/A}\otimes_BC}\Bigr]$$

with the differential given by

$$d_2\bigl(\overline{(a_1,\ldots,a_m)}\bigr)=\sum_j\overline{a_j}e_j,\qquad d_1(e_j)=\dd{f_j}\otimes1$$

For each $i=0,1,2$, the functor

$$T^i(C/A,M)=H^i\bigl(\Hom_C(\operatorname{LS}_{C/A},M)\bigr)$$

is called the *Lichtenbaum–Schlessinger functor* of $C$.
:::

It is not difficult to see that $T^0$ and $T^1$ in this definition are precisely the same as those defined in [Definition 1](#def1){: data-lid="3ydkr" }, and our claim is that the obstruction class is a class living in $T^2$. For a first-order deformation $\xi$, if we choose $c_j\in B$ satisfying $\sum_ja_jg_j=\sum_jc_jf_j$ for each relation $(a_1,\ldots,a_m)\in\Rel$ as in the previous calculation, we obtain

$$\eta(a_1,\ldots, a_m)=\overline{\sum_jc_jg_j}\in C$$

Here, the difference from another choice of $c_j$ is again an element of $\Rel$, and by the flatness condition on $g_j$, this difference becomes $0$ in $C$ and vanishes on $\TrivRel$. Thus, this gives a well-defined $C$-linear map $\eta: \Rel/\TrivRel\rightarrow C$, so we can define its class as $\ob(\xi)=[\eta]\in T^2(C/A,C)$. Moreover, $\ob(\xi)$ depends neither on the choice of $g_j$ nor on the choice of the presentation $C=B/\mathfrak{a}$, and is therefore an invariant of $\xi$ alone.

As seen in the previous calculation, the condition for the existence of a second-order deformation over $A[\t]/(\t^3)$ was that for every relation $a$, the congruence

$$\sum_jc_jg_j\equiv\sum_ja_jh_j\pmod{\mathfrak{a}}$$

be satisfied by some $h_j\in B$. However, the coboundary formed by $h=(\bar{h}_1,\ldots,\bar{h}_m)\in\Hom_C(B^m\otimes_BC,C)$ along the differential $d_2$ takes the right-hand side as its value at $a$. Therefore, the existence of such $h_j$ is precisely equivalent to $\eta$ being a coboundary, that is, $[\eta]=0\in T^2(C/A,C)$, and it is precisely then that a second-order deformation exists. That is, the following holds.

::: Theorem 9
For a first-order deformation $\xi\in T^1(C/A,C)$, the existence of an extension to a flat deformation over $A[\t]/(\t^3)$ is equivalent to $\ob(\xi)=0$.
:::

For a general square-zero extension $0\rightarrow \mathfrak{b}\rightarrow R'\rightarrow R\rightarrow0$ as well, by repeating the same calculation where, instead of powers of $\t$, one perturbs along $\mathfrak{b}$, we obtain the obstruction class, and when an extension exists, applying the argument of [Theorem 5](#thm5){: data-lid="mmtec" } to the difference between two extensions shows that their isomorphism classes form a torsor over $T^1$.

The calculations up to this point generalize to the more general full cotangent complex. To this end, instead of presenting the $A$-algebra $C$ once as a quotient of a polynomial algebra, we choose a free simplicial resolution by polynomial $A$-algebras

$$P_\bullet\overset{\sim}{\rightarrow}C$$

and take the Kähler differentials in each degree. The resulting simplicial $C$-module

$$\LL_{C/A}=\Omega_{P_\bullet/A}\otimes_{P_\bullet}C$$

viewed as a chain complex is the *cotangent complex* of $C$ over $A$. Here, as with the preceding two complexes, we write $\LL_{C/A}$ in homological degrees, and when viewing this in the derived category under cohomological conventions, it is read as $(\LL_{C/A})^{-i}=(\LL_{C/A})_i$. Therefore, the homological truncation $\tau_{\leq r}$ below corresponds to $\tau_{\geq-r}$ in cohomological notation. In this post, we do not use the explicit construction of free simplicial resolutions, but use only the properties regarding truncations and deformations that follow from this definition. The essential property of $\LL_{C/A}$ defined in this way is that it generalizes the two complexes defined earlier, which appear as truncations of $\LL_{C/A}$:

$$\tau_{\leq1}\LL_{C/A}\simeq\NL_{C/A},\qquad \tau_{\leq2}\LL_{C/A}\simeq\operatorname{LS}_{C/A}$$

Therefore, if for any $C$-module $M$ we set

$$T^i(C/A,M)=\Ext^i_C(\LL_{C/A},M)$$

then $T^0$ represents infinitesimal automorphisms, $T^1$ represents first-order deformations and the difference between choices when an extension exists ([Theorem 5](#thm5){: data-lid="5kmzi" }), and $T^2$ controls obstructions to extensions ([Theorem 9](#thm9){: data-lid="gqa0w" }). Now, applying the smoothness criterion of [Proposition 2](#prop2){: data-lid="h13ib" } to the full cotangent complex, we obtain the following conclusion for all degrees of deformation.

::: Proposition 10
If $C$ is smooth over $A$, then for every $C$-module $M$,

$$T^i(C/A,M)=0\qquad(i>0)$$

holds. In particular, the problem of deforming $C$ along a square-zero extension has a solution without obstruction, and its isomorphism class is unique. In the case of a first-order deformation, this class is that of the trivial deformation, and the infinitesimal automorphisms of each deformation are classified by $T^0(C/A,C)=\Der_A(C,C)$.
:::
::: Proof
For smooth $C$, the cotangent complex $\LL_{C/A}$ is quasi-isomorphic in degree $0$ to $\Omega_{C/A}$, and since this module is projective, for all $i>0$ we have

$$T^i(C/A,M)=\Ext^i_C(\LL_{C/A},M)=\Ext^i_C(\Omega_{C/A},M)=0$$
:::

As we have seen earlier, for an affine lci $A$-algebra $C$, the cotangent complex $\LL_{C/A}$ is quasi-isomorphic to the naive cotangent complex consisting of two projective modules, so $T^i(C/A,M)=0$ holds for all $i\geq2$. Therefore, the obstructions at each step vanish and we can continue extending a first-order deformation to a formal deformation; in such cases, we say that it is *unobstructed* in the sense that there is no obstruction class. For a general non-lci algebra, higher homology of $\LL_{C/A}$ may remain; among these, the Lichtenbaum–Schlessinger complex displays up to degree $2$, which is needed for classical deformations and obstructions, while the full cotangent complex preserves the higher relations beyond that.

## General Deformation Theory

So far, we have treated deformations of affine schemes. In the computation immediately following [Definition 3](#def3){: data-lid="d6dgx" }, we saw that if we deform $C$ along an arbitrary square-zero extension

$$0\rightarrow M\rightarrow A'\rightarrow A\rightarrow0$$

the reduction of the deformation $C'$ to the central fiber gives a square-zero extension

$$0\rightarrow M_C\rightarrow C'\rightarrow C\rightarrow0$$

whose kernel is identified with the $C$-module $M_C=M\otimes_AC$. Therefore, the problem of finding a deformation of $C$ over $A'$ was converted into the problem of finding a square-zero extension by $M_C$ of $C$, denoted $C'$, that is compatible with the extension of the base.

That the existence of such an extension is manifested as an *obstruction class* was the content of the previous section. Concretely, if we choose a presentation $C=B/(f_1,\ldots,f_m)$ and, over $A'$, candidate lifts $F_j$ of the equations, then collecting the errors in the direction of the kernel left by the lifts of each relation $\sum_ja_jf_j=0$ yields a $C$-linear map

$$\eta:\Rel/\TrivRel\rightarrow M_C$$

and here, changing the choices of presentation and lifts alters $\eta$ by a coboundary, so its class $[\eta]\in T^2(C/A,M_C)$ was well-defined. This class is precisely the obstruction class, and we know that $[\eta]=0$ is equivalent to the existence of such a square-zero extension $C'$. From this perspective, the earlier [Theorem 9](#thm9){: data-lid="orkga" } was the result in the special case of lifting a first-order deformation $\xi$ to second order. Then, once the obstruction vanishes, the isomorphism classes of deformations form a torsor over $T^1(C/A,M_C)$, and the infinitesimal automorphisms of each deformation are classified by $T^0(C/A,M_C)$.

Now, what remains is to elevate this computation to general schemes. For this, we must first fix a square-zero thickening of the base, construct a flat family on each affine piece, and then choose isomorphisms identifying these families on the overlaps of pairs of pieces. Finally, these isomorphisms must satisfy the cocycle condition on triple overlaps in order to yield a deformation of schemes. Moreover, the cotangent complex must also be computed on each affine piece and glued compatibly with restriction. In this section, rather than carrying out this entire process anew, we clarify which data and obstructions appear at which levels and summarize how they are assembled into a single global $\Ext$.

First, the simplest direction is to extend the initially given base space $S$ from an affine scheme to a general scheme. For a quasi-coherent module $\mathcal{I}$ on $S$, if we endow $\mathcal{O}_S\oplus\mathcal{I}$ with the multiplication

$$(a,u)(b,v)=(ab,av+bu)$$

then, with $\mathcal{I}^2=0$, this becomes an $\mathcal{O}_S$-algebra. Then the relative spectrum $S[\mathcal{I}]=\rSpec_S(\mathcal{O}_S\oplus\mathcal{I})$ associated to this is a split square-zero thickening of $S$, and in particular, when $\mathcal{I}=\mathcal{O}_S$, we write this as $S[\epsilon]$. If $S=\Spec A$, this coincides with $\Spec(A[\epsilon])$ used earlier; more generally, given a square-zero ideal sheaf $\mathcal{I}=\ker(\mathcal{O}_{S'}\rightarrow\mathcal{O}_S)$, the closed embedding $S\hookrightarrow S'$ defined by it can be used as a thickening of the base.

::: Definition 11
Given a flat morphism $f:X_0\rightarrow S$ and a square-zero ideal sheaf $\mathcal{I}$ defining a closed embedding $i:S\hookrightarrow S'$, a *deformation* of $X_0$ over $S'$ is a flat $S'$-scheme $X$ together with an $S$-isomorphism

$$\iota:X\times_{S'}S\xrightarrow{\sim}X_0$$

, given as a pair $(X,\iota)$. Two deformations $(X,\iota)$ and $(X',\iota')$ are *isomorphic* when $\iota'\circ(\psi\times_{S'}S)=\iota$ for some $S'$-isomorphism $\psi:X\rightarrow X'$. In particular, a deformation in the case where $S'=S[\epsilon]$ is called a *first-order deformation* of $X_0$ over $S$.
:::

This is nothing more than rewriting [Definition 3](#def3){: data-lid="jsfdd" } using the infinitesimal thickenings for general schemes described above. Indeed, since a square-zero thickening does not change the underlying topological space, $S$ and $S'$ have the same open sets; in particular, for an affine open $V=\Spec A\subseteq S$, the corresponding subset $V'\subseteq S'$ is also affine, and writing $V'=\Spec A'$, the map $A'\twoheadrightarrow A$ is a square-zero extension. That is, intuitively, an infinitesimal thickening of $S$ can be thought of as performing compatible infinitesimal thickenings on each affine piece and then gluing them together. Similarly, the underlying space of a deformation $X$ is the same as the central fiber $X_0$, so that $U\subseteq X_0$ directly determines an open set of $X$; thanks to this, the flatness of the deformation and the central fiber condition can be checked on affine open sets, and on each affine piece this reduces to the case of [Definition 3](#def3){: data-lid="x7z35" }. In particular, if we denote an affine open over $V'=\Spec A'$ by $U'=\Spec C'\subseteq X$ and set $I=\ker(A'\rightarrow A)$, then since $C'$ is flat over $A'$, tensoring $0\rightarrow I\rightarrow A'\rightarrow A\rightarrow0$ with $C'$ yields the sequence

$$0\rightarrow I\otimes_{A'}C'\rightarrow C'\rightarrow C'/IC'\rightarrow0$$

which is exact; moreover, since $I^2=0$, we have $I\otimes_{A'}C'\cong I\otimes_A(C'/IC')$, so that the ideal sheaf of $X_0\hookrightarrow X$ is identified with $\mathcal{G}=f^\ast\mathcal{I}$. In the globally affine case, if we set $S=\Spec A$, $X_0=\Spec C$, and $\mathcal{I}=\widetilde{M}$, then

$$\mathcal{G}=f^\ast\mathcal{I}\cong\widetilde{M\otimes_A C}=\widetilde{M_C}$$

, so $\mathcal{G}$ is obtained by sheafifying the coefficient module $M_C$ from the earlier affine case. In particular, in a first-order deformation, $M=A$, so $\mathcal{G}=\mathcal{O}_{X_0}$.

Now choose an affine open cover $X_0=\bigcup_iU_i$ of $X_0$. By the discussion above, we can construct a deformation $U_i'$ on each $U_i$, but the problem of gluing them together still remains. First, on the overlap $U_{ij}=U_i\cap U_j$, we must choose an isomorphism

$$\varphi_{ij}:U_i'\vert_{U_{ij}}\xrightarrow{\sim}U_j'\vert_{U_{ij}}$$

which is an $S'$-isomorphism restricting to the identity map on the central fiber, and on the triple overlap $U_{ijk}$, the condition $\varphi_{jk}\circ\varphi_{ij}=\varphi_{ik}$ must hold. Then, under these conditions, the $U_i'$ glue together into a single scheme $X$, and each structure morphism also glues to $X\rightarrow S'$; since flatness is a local condition on the source and the base, the morphism obtained this way is flat. That is, we can obtain a deformation through this process. Conversely, it is clear that every deformation gives rise to such data.

What simultaneously controls these three pieces of data (namely, the local deformations on the affine pieces, the isomorphisms on the overlaps of two pieces, and the cocycle condition on the triple overlaps) is the cotangent complex. To this end, we must first transfer the complex defined in the affine setting to schemes. First, in the affine case, we know that if $U=\Spec C\subseteq X_0$ and $V=\Spec A\subseteq S$ satisfy $f(U)\subseteq V$, then by sheafifying each term and differential of $\LL_{C/A}$, we obtain a complex consisting of quasi-coherent $\mathcal{O}_U$-modules and morphisms between them.

The issue lies in that the naive model of the cotangent complex defined on each of these affine pieces depends on the presentation of $C$, and in the process of extending this to a general cotangent complex, the choice of a resolution also enters. For this reason, these complexes are not termwise identical on each overlap, but are identified only via the canonical quasi-isomorphism

$$\widetilde{\LL_{C/A}}\xrightarrow{\sim}\LL_{X_0/S}\vert_U$$

. That is, the rigorous gluing takes place in the derived category $D(\mathcal{O}_{X_0})$ ([\[Homological Algebra\] §Derived Categories, ⁋Definition 2](/en/math/homological_algebra/derived_categories#def2){: data-lid="983qj" }), and we write the result as $\LL_{X_0/S}$.

Now, since $\LL_{X_0/S}$ is an object of the derived category, on $X_0$, taking a quasi-coherent module $\mathcal{G}$ as coefficients, the degree $i$ data is computed by the formula

$$\Hom_{D(\mathcal{O}_{X_0})}(\LL_{X_0/S},\mathcal{G}[i])\cong H^i\bigl(R\Hom_{\mathcal{O}_{X_0}}(\LL_{X_0/S},\mathcal{G})\bigr)=\Ext^i_{\mathcal{O}_{X_0}}(\LL_{X_0/S},\mathcal{G})$$

. Here, the single complex $R\Hom_{\mathcal{O}_{X_0}}(\LL_{X_0/S},\mathcal{G})$ encapsulates the coefficient data across all degrees simultaneously, and the shift $\mathcal{G}[i]$ is notation for interpreting its $i$-th cohomology as a morphism set in the derived category ([\[Homological Algebra\] §Derived Categories, ⁋Proposition 10](/en/math/homological_algebra/derived_categories#prop10){: data-lid="bz5fv" }). We denote this by

$$T^i(X_0/S,\mathcal{G})=\Ext^i_{\mathcal{O}_{X_0}}(\LL_{X_0/S},\mathcal{G}),\qquad T^i(X_0/S)=T^i(X_0/S,\mathcal{O}_{X_0})$$

. The following theorem then summarizes what we observed for affine schemes into a unified statement.

::: Theorem 12 (Deformation theorem)
Let $f:X_0\rightarrow S$ be a flat, separated morphism locally of finite presentation, suppose that on $S$, a square-zero ideal sheaf $\mathcal{I}$ defines an extension $S\hookrightarrow S'$, and let $\mathcal{G}=f^\ast\mathcal{I}$. Then there exists a canonical obstruction class

$$\ob(X_0/S')\in T^2(X_0/S,\mathcal{G})$$

such that the existence of a deformation over $S'$ is equivalent to $\ob(X_0/S')=0$. In this case, the isomorphism classes of deformations form a torsor under $T^1(X_0/S,\mathcal{G})$, and the infinitesimal automorphisms of each deformation are classified by $T^0(X_0/S,\mathcal{G})$.
:::

In particular, when $S'=S[\epsilon]$, the isomorphism classes of first-order deformations are naturally in one-to-one correspondence with $T^1(X_0/S)$, with the trivial deformation corresponding to $0$.

Since the invariants $T^i(X_0/S)$ obtained in [Theorem 12](#thm12){: data-lid="z7f7e" } above are defined as the global $\Ext$ of the cotangent complex, to read off information directly on each affine piece, we must look at the *sheaf Ext*

$$\sExt^q_{\mathcal{O}_{X_0}}(\mathcal{F},\mathcal{G})=R^q\sHom_{\mathcal{O}_{X_0}}(\mathcal{F},\mathcal{G})$$

This is the sheafification of the presheaf associating to each open set $U$ the module $\Ext^q_{\mathcal{O}_U}(\mathcal{F}\vert_U,\mathcal{G}\vert_U)$. In particular, for $\mathcal{K}=\LL_{X_0/S}$, the sheaf

$$\mathcal{T}_{X_0/S}^q=\sExt^q_{\mathcal{O}_{X_0}}(\LL_{X_0/S},\mathcal{O}_{X_0})$$

gives, on an affine open $U=\Spec C$, the isomorphism $\mathcal{T}_{X_0/S}^q(U)\cong T^q(C/A,C)$, directly recovering the $T^i$ treated in the preceding sections.

Now, to relate the two, let us apply [\[Sheaf Theory\] §Derived Category of Sheaves and Derived Functors, ⁋Corollary 11](/en/math/sheaf_theory/derived_category_of_sheaves#cor11){: data-lid="dndnd" } to $\mathcal{G}=\mathcal{O}_{X_0}$ and the truncation $\mathcal{K}=\tau_{\leq2}\LL_{X_0/S}$ of the cotangent complex. Since $\mathcal{K}$ is a bounded complex with terms only in homological degrees $0,1,2$, that is, cohomological degrees $-2,-1,0$, it is an object of $D^+(\mathcal{O}_{X_0})$; and since the first term of the triangle $\tau_{\geq3}\LL_{X_0/S}\rightarrow\LL_{X_0/S}\rightarrow\mathcal{K}$ contributes only in degrees $3$ and higher to $\Ext$, for $i\leq2$ the complex $\mathcal{K}$ directly computes $T^i(X_0/S)$ and $\mathcal{T}^i_{X_0/S}$. Also, since $\LL_{X_0/S}$ is concentrated in non-negative homological degrees, for $q<0$ we have $\mathcal{T}_{X_0/S}^q=0$, and therefore this becomes a first quadrant spectral sequence

$$E_2^{p,q}=H^p(X_0,\mathcal{T}_{X_0/S}^q)\Rightarrow T^{p+q}(X_0/S)$$

Reading off the low-degree terms of this spectral sequence yields the following.

::: Theorem 13 (Local-to-global exact sequence)
Let $X_0$ be a scheme that is flat, separated, and locally of finite presentation over $S$. Then the exact sequence

$$0\rightarrow H^1(X_0,\mathcal{T}_{X_0/S}^0)\rightarrow T^1(X_0/S)\rightarrow H^0(X_0,\mathcal{T}_{X_0/S}^1)\overset{d_2}{\rightarrow}H^2(X_0,\mathcal{T}_{X_0/S}^0)\rightarrow T^2(X_0/S)$$

holds.
:::
::: Proof
By [\[Homological Algebra\] §Spectral Sequences, ⁋Proposition 10](/en/math/homological_algebra/spectral_sequences#prop10){: data-lid="e2vso" }, the filtration of $T^1(X_0/S)$ given by convergence yields the short exact sequence $0\rightarrow E_\infty^{1,0}\rightarrow T^1(X_0/S)\rightarrow E_\infty^{0,1}\rightarrow0$. By the first-quadrant condition, $E_\infty^{1,0}=E_2^{1,0}$ and $E_\infty^{0,1}=\ker(d_2:E_2^{0,1}\rightarrow E_2^{2,0})$. On the other hand, in total degree $2$, we have $E_\infty^{2,0}=E_2^{2,0}/\im d_2$, which is isomorphic to the first term $F^2T^2(X_0/S)\subseteq T^2(X_0/S)$ of the convergence filtration. Splicing these together and substituting $E_2^{p,q}=H^p(X_0,\mathcal{T}_{X_0/S}^q)$, we obtain the given exact sequence.
:::

Each term of the five-term exact sequence above corresponds in an exact one-to-one manner to the three kinds of data examined earlier. First, the canonical morphism $T^1(X_0/S)\rightarrow H^0(X_0,\mathcal{T}_{X_0/S}^1)$ in the middle forgets the gluing data of a global deformation and retains only the local deformation classes on each affine piece. Therefore, its codomain $H^0(X_0,\mathcal{T}_{X_0/S}^1)$ is the collection of local deformation classes on each piece whose restrictions to the overlaps are compatible with each other.

The kernel of this morphism on the left, $H^1(X_0,\mathcal{T}_{X_0/S}^0)$, classifies the *locally trivial deformations* that are trivial on each affine piece but obtained by twisting the gluing isomorphisms on the overlaps by infinitesimal automorphisms $\mathcal{T}_{X_0/S}^0$. Conversely, the differential $d_2:H^0(X_0,\mathcal{T}_{X_0/S}^1)\rightarrow H^2(X_0,\mathcal{T}_{X_0/S}^0)$ is the obstruction determining whether the cocycle condition holds on triple overlaps once representatives of compatible local deformations and overlap isomorphisms are chosen. That is, only the local classes with $d_2=0$ can finally be glued into a genuine scheme deformation $T^1(X_0/S)$.

Moreover, in degree $0$, since $E_2^{0,0}=E_\infty^{0,0}$, there is a natural isomorphism $T^0(X_0/S)\cong H^0(X_0,\mathcal{T}_{X_0/S}^0)$, which shows that global infinitesimal automorphisms consist precisely of global sections of the local automorphisms on each piece.

::: Corollary 14
If $X_0$ is smooth over $S$, then for all $i$,

$$T^i(X_0/S)\cong H^i(X_0,\mathcal{T}_{X_0/S})$$

holds. In particular, the isomorphism classes of first-order deformations are classified by $H^1(X_0,\mathcal{T}_{X_0/S})$.
:::
::: Proof
In the smooth case, $\LL_{X_0/S}\simeq\Omega_{X_0/S}$, and since $\Omega_{X_0/S}$ is locally free, we have $\mathcal{T}_{X_0/S}^q=0$ for $q>0$ and $\mathcal{T}_{X_0/S}^0=\sHom_{\mathcal{O}_{X_0}}(\Omega_{X_0/S},\mathcal{O}_{X_0})=\mathcal{T}_{X_0/S}$. Therefore, the spectral sequence of [Theorem 13](#thm13){: data-lid="51og8" } degenerates to the single row $q=0$.
:::

---

**References**

**[Har]** R. Hartshorne, *Deformation theory*, Graduate Texts in Mathematics 257, Springer, 2010.  
**[Ill]** L. Illusie, *Complexe cotangent et déformations I, II*, Lecture Notes in Mathematics 239, 283, Springer, 1971--1972.  
**[Stacks]** The Stacks project authors, *The Stacks project*, [stacks.math.columbia.edu](https://stacks.math.columbia.edu).
