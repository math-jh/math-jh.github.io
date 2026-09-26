---
title: "Perfect Obstruction Theory"
description: "This post addresses the problem of recovering a cycle of the expected dimension on a moduli space of stable maps whose actual dimension exceeds its virtual dimension. Starting from the local model of the zero locus of a vector bundle section, it connects Behrend-Fantechi perfect obstruction theory and the intrinsic normal cone to the construction of the virtual fundamental class."
excerpt: "Perfect obstruction theory, virtual fundamental class, intrinsic normal cone, localized Euler class"

categories: [Math / Gromov-Witten Theory]
permalink: /en/math/gromov-witten_theory/perfect_obstruction_theory
sidebar: 
    nav: "gromov-witten_theory-en"

date: 2026-09-18

weight: 4
translated_at: 2026-09-21T11:15:05+00:00
translation_source: antigravity-gemini-3.8-flash-high
---
In algebraic geometry, the local geometry of a space is understood through the relationship between the tangent space at a point and the equations cutting out the space within it. At a typical smooth point, a neighborhood of the point has the same dimension as the tangent space, but at a singular point, the tangent space (namely the $1$st-order differential) fails to fully reconstruct the space, so that the tangent space plays the role of a space larger than the actual space. For this reason, in such places, higher-order terms of degree $2$ or higher must cut down the tangent space to determine the original space. If these higher-order equations act as $r$ independent constraints, the expected dimension is smaller than the dimension of the tangent space by $r$, but if the equations become mutually dependent or ineffective, they cannot cut down the dimension as expected, so the actual dimension may exceed this expectation.

For example, inside $\mathbb{A}^3$, consider the space defined by the two equations $\x\y=0$ and $\x\z=0$, namely $X=Z(\x\y,\x\z)$. Since it is defined by two equations, the dimension we expect is $3-2=1$, but if we actually plot this, it is the union of the locus satisfying $\x=0$, namely the $\y\z$-plane, and the locus where $\y,\z$ are simultaneously $0$, namely the $\x$-axis. In this picture, along the $\x$-axis part, the two equations function fully among the three variables to reduce the dimension, making it a $1$-dimensional space, but on the $\y\z$-plane, these equations only cut down the dimension by one, so the actual dimension is inflated by one above the expected dimension. Moreover, at the origin where these two components meet, the order-$1$ derivatives of the equations all vanish to $0$, so that even the dimension of the tangent space becomes $3$.

The virtual dimension we calculated in [§Moduli Space of Stable Maps, ⁋Proposition 4](/en/math/gromov-witten_theory/moduli_of_stable_maps#prop4){: data-lid="31q1v" } was precisely the *correct* dimension capturing this intuition. In the moduli of stable maps, the tangent space is the direction in which the stable map moves, that is, the deformation space of the stable map, and that $T^2$ plays the role of the equations cutting it out was the meaning of the definition

$$\vdim=\dim T^1(C,p_\bullet,\mu)-\dim T^2(C,p_\bullet,\mu)$$

In that proposition, we already saw that this virtual dimension does not depend on the choice of the stable map and is determined at every point solely by $g,n,\beta$, but for the reasons examined above, there is no guarantee that this becomes the actual dimension. That is, as $\dim T^1$ and $\dim T^2$ vary respectively, only their difference is held constant, and in this process, situations like the above naturally occur frequently.

Meanwhile, if we read the actual dimension of the moduli space $\dim\overline{\mathcal{M}}_{g,n}(X,\beta)$ as the local dimension at a point, it is less than or equal to the dimension of the tangent space at that point $\dim T^1$, and although introducing $\dim T^2$ was intended to serve as a correction term to capture this defect, it did not measure the actual defect. The actual difference can be written as

$$\dim\overline{\mathcal{M}}_{g,n}(X,\beta)-\vdim=\dim T^2-\bigl(\dim T^1-\dim\overline{\mathcal{M}}_{g,n}(X,\beta)\bigr)$$

where $\dim T^1-\dim\overline{\mathcal{M}}_{g,n}(X,\beta)$ is always nonnegative, and if this number kills the dimension of $\dim T^2$, the virtual dimension and the actual dimension coincide. In this situation, if the dimension of $T^2$ is $0$, the value of $\dim T^1-\dim\overline{\mathcal{M}}_{g,n}(X,\beta)$ is forced to be $0$, and the defect above is also $0$, so the moduli space is smooth. However, even if $T^2$ survives, if $\dim T^1-\dim\overline{\mathcal{M}}_{g,n}(X,\beta)$ completely cancels it, the two dimensions still agree.

To see this in an actual moduli space, let $X$ be a smooth projective variety, $\dim X=d$, and choose $\beta=0$, $g=1$, and $n\geq1$. A stable map $\mu:C\rightarrow X$ of class $0$ is a constant map sending each component to a single point; since the domain must be a stable curve by stability, the remaining data consists only of an $n$-pointed genus $1$ stable curve and the value $\mu(C)\in X$ recording where this curve is sent. Therefore,

$$\overline{\mathcal{M}}_{1,n}(X,0)\cong\overline{\mathcal{M}}_{1,n}\times X$$

and its dimension is $(3\cdot1-3+n)+d=n+d$. This is different from $\vdim=0+(d-3)(1-1)+n=n$ given by the virtual dimension formula above, and our claim is that this indeed arises from the computation examined above. For a constant map, $\mu^\ast T_X=\mathcal{O}_C\otimes T_{X,\mu(C)}$ is a trivial bundle, so

$$H^1(C,\mu^\ast T_X)=H^1(C,\mathcal{O}_C)\otimes T_{X,\mu(C)}$$

and, for $g=1$, since $\dim H^1(C,\mathcal{O}_C)=1$, this space is $d$-dimensional. Furthermore, since $\dd{\mu}=0$ for a constant map, we have $T^2\cong H^1(C,\mu^\ast T_X)$, and since the moduli space itself is smooth, the defect term $\dim T^1-\dim\overline{\mathcal{M}}_{1,n}(X,0)$ is also $0$. Therefore, the excess $\dim\overline{\mathcal{M}}_{1,n}(X,0)-\vdim$ manifests precisely as $\dim T^2=d$ without any cancellation by the defect term.

The goal of this post is to construct, even when the dimensions do not match in this way, the *virtual fundamental class*

$$[\overline{\mathcal{M}}_{g,n}(X,\beta)]^\vir\in A_{\vdim}(\overline{\mathcal{M}}_{g,n}(X,\beta))$$

which is a class of the expected dimension that makes integration possible; following [BF], this can be obtained from data called a *perfect obstruction theory*.

## Zero Locus of a Vector Bundle

Now we lift the language above to a more geometric setting. To this end, we lift $T^1$, which plays the role of the ambient space, to a smooth variety $X$, and $T^2$ to a vector bundle $E$ over it; in this setting, the equation of the obstruction becomes a section $s\in \Gamma(X, E)$ of this bundle, so that our moduli space becomes the common locus defined by the locus of sections on such a smooth variety $X$.

We therefore briefly review this situation. On a smooth variety $X$, suppose we are given a rank $r$ vector bundle $E$ and a section $s\in\Gamma(X,E)$, and let

$$Z(s)=\{x\in X\mid s(x)=0\}$$

be its zero locus. If $s$ intersects the zero section transversally, then $Z(s)$ is a smooth subvariety of the expected codimension $r$, and its fundamental class coincides with the Euler class $e(E)\cap[X]$. If the section $s$ does not intersect transversally so that the codimension of $Z(s)$ is less than $r$, its fundamental class $[Z(s)]$ is not a class of the expected dimension; nevertheless, in this model, a class on $X$, namely $e(E)\cap[X]$, exists, and we can bring it to a cycle on $Z(s)$ via the Gysin map. Since the normal cone $C_{Z(s)/X}$ is naturally included as a closed subcone of $E\vert_{Z(s)}$, with respect to the zero section $0_E: Z(s)\hookrightarrow E\vert_{Z(s)}$, applying the Gysin map $0_E^!$ to the cone allows us to define a class on $Z(s)$ of the correct expected dimension $\dim X-r$

$$e(E,s)=0_E^![C_{Z(s)/X}]\in A_{\dim X-r}(Z(s))$$

which is called the *localized Euler class*. Intuitively, this can be understood as algebraically recording, without actually perturbing it, the class that would have been obtained had the non-transversal section $s$ been perturbed appropriately.

::: Example 1
Consider $X=\mathbb{P}^2$ and $E=\mathcal{O}(1)^{\oplus2}$. Then the section $s=(\ell_1,\ell_2)$ is given by two linear forms, so in the diagram above, $Z(s)$ has expected dimension $0$. In fact, this is a single point given by the intersection of two lines, and the degree of its class is

$$\int_{\mathbb{P}^2}e(E)=\int_{\mathbb{P}^2}c_1(\mathcal{O}(1))^2=1$$

. However, if we choose a non-transversal section, say $s\equiv0$ in the extreme case, then $Z(s)=\mathbb{P}^2$ becomes the entire space, so the actual dimension exceeds the expected dimension by $2$. Nevertheless, the class obtained by pushing the localized Euler class forward to $X$ is determined solely by the bundle and not by the section, and

$$e(E)\cap[\mathbb{P}^2]=c_2(\mathcal{O}(1)^{\oplus2})\cap[\mathbb{P}^2]$$

still yields a point class of degree $1$. ([\[Algebraic Varieties\] §Intersection Product, ⁋Example 11](/en/math/algebraic_varieties/intersection_product#ex11){: data-lid="9kgj4" })
:::

To accommodate the deformation space $T^1$ and the obstruction space $T^2$, we have constructed such a smooth variety $X$ and vector bundle $E$, and our goal in this section is to make this precise. For a fixed $x\in X$, the vector space containing all directions perturbing it is the tangent space to $X$, denoted by $T_{X,x}$, and the fiber $E_x$ at each point becomes the obstruction space.

Meanwhile, given a point of $Z(s)$, say $x$, the condition that perturbing this point still keeps it inside $Z(s)$ is precisely what determines the deformation directions of $Z(s)$. That is, in the direction of a tangent vector $v\in T_{X,x}$, for an infinitesimal displacement $x+\epsilon v$, we have

$$s(x+\epsilon v)=s(x)+\epsilon\dd{s}(v)=\epsilon\dd{s}(v)$$

, so the condition that this first-order variation $\dd{s}(v)=0$ must be satisfied for the result to remain inside $Z(s)$. Therefore, the kernel of $\dd{s}$, namely $\ker(\dd{s})$, constitutes the actual tangent space and deformation directions of $Z(s)$; conversely, the remaining directions in $E_x$ not filled by the image of $\dd{s}$, that is, the cokernel $\coker(\dd{s})$, are the directions that cannot be controlled to keep the section at $0$, and this is precisely the actual obstruction space of $Z(s)$.

To summarize, the local deformation and obstruction data of $Z(s)$ are entirely encoded in the complex in the tangent direction, where its differential $\dd{s}$ connects the tangent space $T^1$ and the obstruction space $T^2$:

$$\Bigl[\at{0}{T_X\vert_{Z(s)}}\xrightarrow{\ \dd{s}\ }\at{1}{E\vert_{Z(s)}}\Bigr]$$

As we conventionally work in the cotangent direction in algebraic geometry, dualizing this complex to write it as a complex situated in degrees $-1$ and $0$, we obtain

$$E^\bullet=\Bigl[\at{-1}{E^\vee\vert_{Z(s)}}\xrightarrow{\ (\dd{s})^\vee\ }\at{0}{\Omega_X\vert_{Z(s)}}\Bigr]$$

. Now, applying $R\Hom(-,\mathcal{O}_{Z(s)})$ to this complex to recover the original tangent direction, the $0$th cohomology and $1$st cohomology

$$h^0((E^\bullet)^\vee)=\ker(\dd{s}),\qquad h^1((E^\bullet)^\vee)=\coker(T_X\vert_{Z(s)}\rightarrow E\vert_{Z(s)})$$

give the actual tangent space and obstruction space.

The crucial observation is that, even if the tangent space is inflated beyond expectation as in [Example 1](#ex1){: data-lid="fkmo8" }, the obstruction also increases by the same amount, so their difference

$$\dim h^0((E^\bullet)^\vee)-\dim h^1((E^\bullet)^\vee)=\dim X-\rank E$$

is always preserved as the virtual dimension $\vdim$. That is, however poorly the actual moduli space behaves, the Gysin map defined above always yields a virtual class of exactly dimension $\dim X-\rank E$, that is, of the correct dimension.

## Perfect obstruction theory

Now it is clear how the above discussion should be applied. That is, a general stack $M$ has a cotangent complex $\LL_M$, and we only need to consider the truncation $\tau_{\geq -1}\LL_M$ where deformations and obstructions are captured. ([\[Schemes\] §Deformation Theory and the Cotangent Complex, §§Obstructions to Deformation and Higher-Order Deformation Theory](/en/math/scheme_theory/deformation_theory#obstructions-to-deformation-and-higher-order-deformation-theory){: data-lid="0fpnl" }) Now, if étale-locally $M$ is represented as a closed subscheme of a smooth variety $X$ with ideal sheaf $\mathcal{I}$, this truncation takes the form

$$\tau_{\geq-1}\LL_M=\Bigl[\at{-1}{\mathcal{I}/\mathcal{I}^2}\xrightarrow{\ \dd{\ }}\at{0}{\Omega_X\vert_M}\Bigr]$$

. The problem is that on a general $M$, the sheaf $\mathcal{I}/\mathcal{I}^2$ is not a vector bundle, so we cannot define a zero section or a Gysin map from $\tau_{\geq-1}\LL_M$ alone. For this reason, we must consider a two-term complex of actual vector bundles that can encode all this information, and this is precisely the following definition.

::: Definition 2 (Behrend–Fantechi)
Let $M$ be a Deligne–Mumford stack. A *perfect obstruction theory* on $M$ is a pair consisting of a complex locally quasi-isomorphic to a two-term complex of vector bundles $[E^{-1}\rightarrow E^0]$, namely $E^\bullet$, and a morphism

$$\phi:E^\bullet\longrightarrow\tau_{\geq-1}\LL_M$$

such that $h^0(\phi)$ is an isomorphism and $h^{-1}(\phi)$ is a surjection.
:::

In this definition, first, that $h^0(\phi)$ is an isomorphism means that the term of $E^\bullet$ in degree $0$ precisely reproduces the deformations of $M$. The part requiring modification was where $\mathcal{I}/\mathcal{I}^2$ originally belonged, namely the degree $-1$ term; here, that $h^{-1}(\phi)$ is a surjection means that the term of $E^\bullet$ in degree $-1$ governs the obstructions of $M$ *without omission*. That is, having more obstructions on the side of $E^\bullet$ than actually exist is permitted, but missing even one is not; this structure gives the leeway to extract a class of the expected dimension.

From the complex constructed via $Z(s)\hookrightarrow X$ examined above,

$$E^\bullet=\Bigl[\at{-1}{E^\vee\vert_{Z(s)}}\xrightarrow{\ (\dd{s})^\vee\ }\at{0}{\Omega_X\vert_{Z(s)}}\Bigr]$$

to the truncation

$$\tau_{\geq-1}\LL_{Z(s)}=[\at{-1}{\mathcal{I}/\mathcal{I}^2}\rightarrow\at{0}{\Omega_X\vert_{Z(s)}}]$$

the morphism $\phi:E^\bullet\rightarrow\tau_{\geq-1}\LL_{Z(s)}$ is given by the following diagram:

{% diagram Math/Gromov_Witten_Theory/Perfect_Obstruction_Theory-1.svg width="10.88em" alt="morphism from the local complex to the truncated cotangent complex" %}

In particular, in degree $-1$, it is defined by descending the pairing with the section $s$, $s^\vee:E^\vee\rightarrow\mathcal{O}_X$, to $\mathcal{I}/\mathcal{I}^2$. Since the image of $s^\vee$ is precisely $\mathcal{I}$, this is a surjection, so this complex indeed becomes a perfect obstruction theory.

Now, from such a given perfect obstruction theory, we define the virtual fundamental class. In ordinary intersection theory, given a closed embedding $Z(s)\hookrightarrow X$, deformation to the normal cone deforms $X$ to the normal cone $C_{Z(s)/X}$, allowing us to define the intersection product and the Gysin map. ([\[Algebraic Varieties\] §Intersection Product, ⁋Proposition 9](/en/math/algebraic_varieties/intersection_product#prop9){: data-lid="7fg7b" }) The key result of [BF] is the construction of the *intrinsic normal cone* $\mathfrak{c}_M=[C_{Z(s)/X}/T_X\vert_{Z(s)}]$, which can be obtained intrinsically without an explicit embedding being given; the perfect obstruction theory $\phi$ above realizes this as a closed embedding into the vector bundle stack $\mathfrak{E}=h^1/h^0((E^\bullet)^\vee)$:

$$\mathfrak{c}_M\hookrightarrow\mathfrak{E}=[E_1/E_0]$$

Here, $E_i=(E^{-i})^\vee$. Thanks to this, just as in ordinary intersection theory, using the Gysin pullback with respect to the zero section of $\mathfrak{E}$, we can define the virtual class

$$[M]^\vir=0^!_{E^\bullet}[\mathfrak{c}_M]\in A_{\rank E^\bullet}(M)$$

Its properties are as follows.

::: Proposition 3
For a Deligne–Mumford stack $M$ equipped with a perfect obstruction theory $\phi:E^\bullet\rightarrow\tau_{\geq-1}\LL_M$, the virtual class $[M]^\vir=0^!_{E^\bullet}[\mathfrak{c}_M]$ satisfies the following:

1. $[M]^\vir$ is a cycle of virtual dimension $\vdim=\rank E^\bullet=\rank E^0-\rank E^{-1}$.
2. If $M$ is given as the fiber of a flat family and $\phi$ is compatible with a perfect obstruction theory on the family, then $[M]^\vir$ is the Gysin pullback of the virtual class of the family to the fiber. In particular, $[M]^\vir$ is invariant under deformation within the family.
3. If $h^1((E^\bullet)^\vee)=0$, then $M$ is smooth and $[M]^\vir=[M]$ is the ordinary fundamental class.
:::

## Virtual Fundamental Class of Stable Maps

We now construct a perfect obstruction theory on the moduli stack of stable maps $M=\overline{\mathcal{M}}_{g,n}(X,\beta)$. For this purpose, from the target $X$, we import its tangent space $T_X$ using

$$\pi:\mathcal{C}\rightarrow M,\qquad\mu:\mathcal{C}\rightarrow X$$

That is, after pulling back $T_X$ via $\mu$, we push it down again via $R\pi_\ast$ to obtain $R\pi_\ast\mu^\ast T_X$. Since the dimension of curves is $1$, the higher direct images $R^i\pi_\ast$ survive only for $i=0,1$; thus this complex is a two-term complex concentrated in degrees $0$ and $1$, and at each point its cohomology recovers $H^0(C,\mu^\ast T_X)$ and $H^1(C,\mu^\ast T_X)$.

Therefore, the dual of $R\pi_\ast\mu^\ast T_X$ obtained above, $E^\bullet=(R\pi_\ast\mu^\ast T_X)^\vee$, is a complex of amplitude $[-1,0]$ and serves as a candidate for the desired perfect obstruction theory. However, since this data fixes the domain curve $(C,p_\bullet)$ and deforms only the map $\mu$, it forms a relative perfect obstruction theory for the morphism to the moduli stack of prestable curves $\mathfrak{M}_{g,n}$, $q:M\rightarrow\mathfrak{M}_{g,n}$. What helps us here is that the base stack $\mathfrak{M}_{g,n}$ is smooth; intuitively, this is because there is no obstruction when smoothing a node. That is, $\mathfrak{M}_{g,n}$ already has a (genuine) fundamental class even without a perfect obstruction theory, and we can bring this over using the relative perfect obstruction theory.

::: Proposition 4 (Behrend)
For $M=\overline{\mathcal{M}}_{g,n}(X,\beta)$ and the forgetful morphism $q:M\rightarrow\mathfrak{M}_{g,n}$, the complex $E^\bullet=(R\pi_\ast\mu^\ast T_X)^\vee$ above forms, with respect to $q$, a relative perfect obstruction theory $\phi:E^\bullet\rightarrow\LL_{M/\mathfrak{M}_{g,n}}$. This induces on $M$ an (absolute) perfect obstruction theory $(E')^\bullet\rightarrow\tau_{\geq-1}\LL_M$, and the virtual class of $M$ obtained from this, $[M]^\vir$, has dimension equal to the virtual dimension

$$\vdim=\int_\beta c_1(T_X)+(\dim X-3)(1-g)+n$$
:::

The strategy of proof for this is to first use $T_X$ on the target side to construct the relative complex $(R\pi_\ast\mu^\ast T_X)^\vee$, and together with the base stack $\mathfrak{M}_{g,n}$ to which the domain curves belong, construct the distinguished triangle

$$q^\ast\LL_{\mathfrak{M}_{g,n}}\rightarrow (E')^\bullet\rightarrow E^\bullet\rightarrow q^\ast\LL_{\mathfrak{M}_{g,n}}[1]$$

between the two. Here, the smoothness of the base ensures that $q^\ast\LL_{\mathfrak{M}_{g,n}}$ has no negative degree terms, and the fact that $M$ is a Deligne–Mumford stack eliminates the degree $1$ term containing infinitesimal automorphisms of curves; together, these keep the amplitude of $(E')^\bullet$ in $[-1,0]$, making it a perfect obstruction theory.

::: Example 5
When $X$ is convex, for every genus $0$ stable map we have $H^1(C,\mu^\ast T_X)=0$ ([§Moduli Space of Stable Maps, ⁋Proposition 5](/en/math/gromov-witten_theory/moduli_of_stable_maps#prop5){: data-lid="c4h5h" }), so the obstruction space is $h^1((E^\bullet)^\vee)=R^1\pi_\ast\mu^\ast T_X=0$. Now, for the same reason as discussed above, the smoothness of $\mathfrak{M}_{0,n}$ implies that the absolute obstruction also vanishes, $h^1(((E')^\bullet)^\vee)=0$, so by part (3) of [Proposition 3](#prop3){: data-lid="vrq63" },

$$[\overline{\mathcal{M}}_{0,n}(X,\beta)]^\vir=[\overline{\mathcal{M}}_{0,n}(X,\beta)]$$

and the virtual class coincides with the usual fundamental class. The cases $X=\mathbb{P}^r$, Grassmannians, and general flag varieties $G/P$ all fall into this situation, where genus $0$ curve counting agrees with integration against the (genuine) fundamental class of the smooth moduli, justifying the computations in the previous post.
:::

In [§Gromov-Witten Invariants, ⁋Definition 1](/en/math/gromov-witten_theory/gromov-witten_invariants#def1){: data-lid="gt4df" }, we only gave the definition in the case where the fundamental class $[\overline{\mathcal{M}}_{0,n}(X,\beta)]$ exists, but by simply replacing this fundamental class with the virtual fundamental class, we can define for an arbitrary smooth projective target $X$ the genus $0$ Gromov-Witten invariants without the convexity assumption; that these two definitions coincide under the convexity assumption is immediate from [Example 5](#ex5){: data-lid="bt6x3" } above. Then, under this definition, we can verify that the virtual class behaves well under forgetful morphisms and gluing morphisms, so the string, divisor, and splitting axioms as well as the WDVV relations in [§Gromov-Witten Invariants, §§Axioms of Gromov–Witten Invariants](/en/math/gromov-witten_theory/gromov-witten_invariants#axioms-of-gromovwitten-invariants){: data-lid="huqbc" } also hold verbatim once the corresponding integrals are interpreted as integrals against the virtual class.

::: Example 6
As the opposite extreme, we conclude by examining the moduli space of constant maps $\overline{\mathcal{M}}_{1,n}(X,0)\cong\overline{\mathcal{M}}_{1,n}\times X$ discussed in the introduction. Since our claim in the introduction was that the obstruction survives in its entirety, let us now recompute this in rigorous language.

Let the two projections be $p_1:\overline{\mathcal{M}}_{1,n}\times X\rightarrow\overline{\mathcal{M}}_{1,n}$ and $p_2:\overline{\mathcal{M}}_{1,n}\times X\rightarrow X$, respectively. For a constant map, every point on the curve is mapped to the same point of $X$, so the universal evaluation map $\mu:\mathcal{C}\rightarrow X$ factors as the composition of the projection $p_2$ and the universal curve $\pi:\mathcal{C}\rightarrow M$,

$$\mu=p_2\circ\pi$$

Therefore, the pullback of the target tangent bundle is $\mu^\ast T_X\cong\pi^\ast p_2^\ast T_X$, and pushing this down to $M$ yields, by the projection formula,

$$R^1\pi_\ast\mu^\ast T_X\cong(R^1\pi_\ast\mathcal{O}_{\mathcal{C}})\otimes p_2^\ast T_X$$

Here, over $\overline{\mathcal{M}}_{1,n}$, for the genus $1$ universal curve, applying Serre duality $H^1(C,\mathcal{O}_C)\cong H^0(C,\omega_C)^\vee$ in families shows that $R^1\pi_\ast\mathcal{O}_{\mathcal{C}}$ is isomorphic to the rank $1$ bundle $p_1^\ast(\pi_\ast\omega_{\mathcal{C}})^\vee$. Therefore, the obstruction bundle is

$$h^1(((E')^\bullet)^\vee)\cong R^1\pi_\ast\mu^\ast T_X\cong p_1^\ast(\pi_\ast\omega_{\mathcal{C}})^\vee\otimes p_2^\ast T_X$$

Indeed, at each point $((C,p_\bullet),x)$, the pullback by the constant map $\mu$ trivializes as $\mu^\ast T_X\cong\mathcal{O}_C\otimes T_x X$, so the obstruction space at this point becomes

$$H^1(C,\mu^\ast T_X)\cong H^1(C,\mathcal{O}_C)\otimes T_x X$$

Since $C$ is a genus $1$ curve, we have $\dim H^1(C,\mathcal{O}_C)=1$, and hence the rank of this bundle is $\dim X=d$, which coincides precisely with the difference between the actual dimension $\dim(\overline{\mathcal{M}}_{1,n}\times X)=n+d$ and the virtual dimension $\vdim=n$ of the moduli, namely the excess dimension $d$. Meanwhile, since the moduli stack of prestable curves $\mathfrak{M}_{1,n}$ is smooth, the (open) substack $\overline{\mathcal{M}}_{1,n}$ obtained by imposing the open condition of stability is also smooth; using in addition the smoothness of the target $X$, the entire moduli stack $\overline{\mathcal{M}}_{1,n}\times X$ is smooth. Now, since the obstruction $h^1(((E')^\bullet)^\vee)$ defined on this stack is also a vector bundle, the local model with $s\equiv0$ from [Example 1](#ex1){: data-lid="1f2tf" } applies directly, so that

$$[\overline{\mathcal{M}}_{1,n}(X,0)]^\vir=e(p_1^\ast(\pi_\ast\omega_{\mathcal{C}})^\vee\otimes p_2^\ast T_X)\cap[\overline{\mathcal{M}}_{1,n}\times X]$$

On the $(n+d)$-dimensional space, we recover a class of dimension $n$ via the cap product with the Euler class, effectively reenacting the situation of [Example 1](#ex1){: data-lid="m97nc" } where $s\equiv0$ in the moduli of stable maps.
:::

---

**References**

**[BF]** K. Behrend, B. Fantechi, *The intrinsic normal cone*, Invent. Math. **128** (1997)  
**[B]** K. Behrend, *Gromov–Witten invariants in algebraic geometry*, Invent. Math. **127** (1997)  
