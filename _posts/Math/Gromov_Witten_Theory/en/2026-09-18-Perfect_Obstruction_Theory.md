---
title: "Perfect Obstruction Theory"
description: "Starting from the local model of the zero locus of a vector bundle section, this post addresses how to construct cycles of the expected dimension on moduli spaces of stable maps whose actual dimension exceeds the virtual dimension. It introduces the virtual fundamental class using Behrend-Fantechi perfect obstruction theory and the intrinsic normal cone."
excerpt: "Perfect obstruction theory, virtual fundamental classes, and intrinsic normal cones"

categories: [Math / Gromov-Witten Theory]
permalink: /en/math/gromov-witten_theory/perfect_obstruction_theory
sidebar: 
    nav: "gromov-witten_theory-en"

date: 2026-09-18

weight: 4
translated_at: 2026-09-19T07:15:05+00:00
translation_source: antigravity-gemini-3.8-flash-high
---
In algebraic geometry, the local geometry of a space is understood through the relationship between the tangent space at a point and the equations that cut out the space within it. At a general smooth point, a neighborhood of the point has the same dimension as the tangent space, but at a singular point, the tangent space, that is, the order-$1$ differential, fails to fully recover the space, so that the tangent space plays the role of a space larger than the actual space. For this reason, in such places, higher-order terms of degree $2$ or higher must cut out the tangent space to determine the original space. If these higher-order equations act as $r$ independent constraints, the expected dimension is $r$ less than the dimension of the tangent space; however, if the equations become mutually dependent or ineffective, they fail to cut down the dimension as much as expected, so the actual dimension can exceed this expectation.

For example, in $\mathbb{A}^3$, consider the space defined by the two equations $\x\y=0$ and $\x\z=0$, denoted by $X=Z(\x\y,\x\z)$. Since this space is defined by two equations, the dimension we expect is $3-2=1$, but if we actually draw it, it is the union of the locus where $\x=0$ holds, namely the $\y\z$-plane, and the locus where $\y,\z$ are simultaneously $0$, namely the $\x$-axis. In this picture, on the $\x$-axis part, the two equations act fully on the three unknowns to cut down the dimension, so it becomes a $1$-dimensional space; however, on the $\y\z$-plane, these equations cut down the dimension by only one, so the actual dimension inflates by one above the expected dimension. Furthermore, at the origin where these two components meet, the order-$1$ derivatives of the equations all become $0$, so that even the dimension of the tangent space becomes $3$.

The virtual dimension we computed in [§Moduli Space of Stable Maps, ⁋Proposition 4](/en/math/gromov-witten_theory/moduli_of_stable_maps#prop4){: data-lid="31q1v" } was precisely the *correct* dimension that captured this intuition. In the moduli space of stable maps, the tangent space is the direction in which stable maps can move, namely the deformation space of stable maps, and $T^2$ plays the role of the equations cutting it out; this was the meaning of the definition

$$\vdim=\dim T^1(C,p_\bullet,\mu)-\dim T^2(C,p_\bullet,\mu)$$

. In that proposition, we have already seen that this virtual dimension does not depend on the choice of the stable map and is determined at every point solely by $g,n,\beta$, but for the same reasons as examined above, there is no guarantee that this is the actual dimension. That is, $\dim T^1$ and $\dim T^2$ each vary while only their difference is maintained, and in this process, situations like the one above naturally occur frequently.

On the other hand, if we read the actual dimension $\dim\overline{\mathcal{M}}_{g,n}(X,\beta)$ of the moduli space as its local dimension at a point, it is less than or equal to the dimension $\dim T^1$ of the tangent space at that point, and although the introduction of $\dim T^2$ was intended as a correction term to capture this defect, it did not measure the actual defect. The part that actually differs can be written as

$$\dim\overline{\mathcal{M}}_{g,n}(X,\beta)-\vdim=\dim T^2-\bigl(\dim T^1-\dim\overline{\mathcal{M}}_{g,n}(X,\beta)\bigr)$$

, where $\dim T^1-\dim\overline{\mathcal{M}}_{g,n}(X,\beta)$ is always non-negative, and if this quantity cancels out the dimension of $\dim T^2$, the virtual dimension and the actual dimension coincide. In this situation, if the dimension of $T^2$ is $0$, the value of $\dim T^1-\dim\overline{\mathcal{M}}_{g,n}(X,\beta)$ is forced to be $0$ and the defect above also becomes $0$, so the moduli space is smooth. However, even if $T^2$ is non-zero, if $\dim T^1-\dim\overline{\mathcal{M}}_{g,n}(X,\beta)$ cancels it out completely, the two dimensions will still match.

To see this in an actual moduli space, let $X$ be a smooth projective variety, $\dim X=d$, and choose $\beta=0$, $g=1$, $n\geq1$. A stable map of class $0$, $\mu:C\rightarrow X$, is a constant map sending each component to a single point, and by stability the domain must be a stable curve, so the remaining data are only an $n$-pointed genus $1$ stable curve and the value $\mu(C)\in X$ specifying where this curve is sent. Therefore,

$$\overline{\mathcal{M}}_{1,n}(X,0)\cong\overline{\mathcal{M}}_{1,n}\times X$$

, and its dimension is $(3\cdot1-3+n)+d=n+d$. This is different from $\vdim=0+(d-3)(1-1)+n=n$ given by the virtual dimension formula above, and our claim is that this indeed comes from the computation we saw above. For a constant map, $\mu^\ast T_X=\mathcal{O}_C\otimes T_{X,\mu(C)}$ is a trivial bundle, so

$$H^1(C,\mu^\ast T_X)=H^1(C,\mathcal{O}_C)\otimes T_{X,\mu(C)}$$

, and since for $g=1$ we have $\dim H^1(C,\mathcal{O}_C)=1$, this space is $d$-dimensional. Furthermore, for a constant map we have $\dd{\mu}=0$, so $T^2\cong H^1(C,\mu^\ast T_X)$, and because the moduli space itself is smooth, the defect term $\dim T^1-\dim\overline{\mathcal{M}}_{1,n}(X,0)$ is also $0$. Therefore, the excess $\dim\overline{\mathcal{M}}_{1,n}(X,0)-\vdim$ appears precisely as $\dim T^2=d$ without being cancelled by the defect term.

The goal of our post is to construct, even when dimensions do not match in this way, the *virtual fundamental class*

$$[\overline{\mathcal{M}}_{g,n}(X,\beta)]^\vir\in A_{\vdim}(\overline{\mathcal{M}}_{g,n}(X,\beta))$$

, which is a class of the expected dimension that enables integration; following [BF], this can be obtained from data called a *perfect obstruction theory*.

## Zero Locus of a Vector Bundle

Now we lift the language above to a more geometric setting. To this end, $T^1$, which serves as the ambient space, is lifted to a smooth variety $X$, and $T^2$ to a vector bundle $E$ over it; here the equations for the obstructions become its section $s\in \Gamma(X, E)$, so that our moduli space becomes the common locus defined on this smooth variety $X$ by the locus of sections.

Therefore, we briefly review this situation. Suppose that on a smooth variety $X$, a rank $r$ vector bundle $E$ and a section $s\in\Gamma(X,E)$ are given, and let

$$Z(s)=\{x\in X\mid s(x)=0\}$$

be its zero locus. If $s$ intersects the zero section transversally, then $Z(s)$ is a smooth subvariety of the expected codimension $r$, and its fundamental class coincides with the Euler class $e(E)\cap[X]$. If the section $s$ does not intersect transversally so that the codimension of $Z(s)$ is strictly less than $r$, then its fundamental class $[Z(s)]$ is not a class of the expected dimension; nevertheless, in this model, on $X$ there exists the class $e(E)\cap[X]$, and we can bring it to a cycle on $Z(s)$ via the Gysin map. Since the normal cone $C_{Z(s)/X}$ is naturally contained as a closed subcone of $E\vert_{Z(s)}$, with respect to the zero section $0_E: Z(s)\hookrightarrow E\vert_{Z(s)}$, applying the Gysin map $0_E^!$ to the cone allows us to define a class on $Z(s)$ of the correct expected dimension $\dim X-r$

$$e(E,s)=0_E^![C_{Z(s)/X}]\in A_{\dim X-r}(Z(s))$$

, which is called the *localized Euler class*. Intuitively, this can be understood as algebraically recording the class that would have appeared had we properly perturbed the non-transversal section $s$, without actually perturbing it.

::: Example 1
Consider $X=\mathbb{P}^2$ and $E=\mathcal{O}(1)^{\oplus2}$. Then the section $s=(\ell_1,\ell_2)$ is given by two linear forms, so in the picture above, $Z(s)$ has expected dimension $0$. In fact, this is a single point, the intersection of two lines, and the degree of its class is

$$\int_{\mathbb{P}^2}e(E)=\int_{\mathbb{P}^2}c_1(\mathcal{O}(1))^2=1$$

. However, if we choose a non-transversal section, for instance the extreme case $s\equiv0$, then $Z(s)=\mathbb{P}^2$ becomes the entire space, so the actual dimension exceeds the expected dimension by $2$. Nevertheless, the pushforward of the localized Euler class to $X$ is determined solely by the bundle, not by the section, and

$$e(E)\cap[\mathbb{P}^2]=c_2(\mathcal{O}(1)^{\oplus2})\cap[\mathbb{P}^2]$$

still yields a point class of degree $1$. ([\[Algebraic Varieties\] §Intersection Product, ⁋Example 11](/en/math/algebraic_varieties/intersection_product#ex11){: data-lid="9kgj4" data-relation="weak" })
:::

To accommodate the deformation space $T^1$ and obstruction space $T^2$, we constructed such a smooth variety $X$ and vector bundle $E$, and our goal in this section is to make this rigorous. For a fixed $x\in X$, the vector space containing all directions in which it can be perturbed is the tangent space to $X$, $T_{X,x}$, and the fiber $E_x$ at each point serves as the obstruction space. 

Meanwhile, on $Z(s)$, given a point $x$, the condition that it must still remain in $Z(s)$ even after being perturbed determines the deformation directions of $Z(s)$. That is, in the direction of a tangent vector $v\in T_{X,x}$, for an infinitesimal displacement $x+\epsilon v$,

$$s(x+\epsilon v)=s(x)+\epsilon\dd{s}(v)=\epsilon\dd{s}(v)$$

holds, so this first-order variation condition $\dd{s}(v)=0$ must be satisfied for the result to remain in $Z(s)$. Therefore, the kernel of $\dd{s}$, $\ker(\dd{s})$, forms the actual tangent space and deformation directions of $Z(s)$. Conversely, the remaining directions in $E_x$ not filled by the image of $\dd{s}$, namely the cokernel $\coker(\dd{s})$, are the directions that cannot be controlled to keep the section $0$, and this constitutes the actual obstruction space of $Z(s)$.

To summarize, the local deformation and obstruction data of $Z(s)$ are encoded in the tangent complex where the differential $\dd{s}$ connects the tangent space $T^1$ and the obstruction $T^2$:

$$\Bigl[\at{0}{T_X\vert_{Z(s)}}\xrightarrow{\ \dd{s}\ }\at{1}{E\vert_{Z(s)}}\Bigr]$$

Conventionally in algebraic geometry, we examine the cotangent direction; dualizing this complex into one situated in degrees $-1$ and $0$ yields

$$E^\bullet=\Bigl[\at{-1}{E^\vee\vert_{Z(s)}}\xrightarrow{\ (\dd{s})^\vee\ }\at{0}{\Omega_X\vert_{Z(s)}}\Bigr]$$

. Now, applying $R\Hom(-,\mathcal{O}_{Z(s)})$ to this complex to recover the original tangent direction, the $0$-th cohomology and $1$-st cohomology

$$h^0((E^\bullet)^\vee)=\ker(\dd{s}),\qquad h^1((E^\bullet)^\vee)=\coker(T_X\vert_{Z(s)}\rightarrow E\vert_{Z(s)})$$

give the actual tangent space and obstruction space. 

The crucial observation is that, even if the tangent space is inflated beyond expectation as in [Example 1](#ex1){: data-lid="fkmo8" data-relation="required" }, the obstruction space also increases by the same amount, so their difference

$$\dim h^0((E^\bullet)^\vee)-\dim h^1((E^\bullet)^\vee)=\dim X-\rank E$$

is always preserved as the virtual dimension $\vdim$. In other words, no matter how badly behaved the actual moduli space is, the Gysin map defined above always produces a virtual class of dimension exactly $\dim X-\rank E$, which is the correct dimension. 

## Perfect obstruction theory

Now it is clear how to apply the discussion above. That is, a general stack $M$ has a cotangent complex $\LL_M$, and we only need to look at the truncation $\tau_{\geq -1}\LL_M$ where deformations and obstructions are captured. ([\[Schemes\] §Deformation Theory and the Cotangent Complex, §§Obstructions to Deformation and Higher-Order Deformation Theory](/en/math/scheme_theory/deformation_theory#obstructions-to-deformation-and-higher-order-deformation-theory){: data-lid="0fpnl" data-relation="weak" }) If étale-locally $M$ is represented as a closed subscheme in a smooth variety $X$, and its ideal sheaf is $\mathcal{I}$, then this truncation takes the form

$$\tau_{\geq-1}\LL_M=\Bigl[\at{-1}{\mathcal{I}/\mathcal{I}^2}\xrightarrow{\ \dd\ }\at{0}{\Omega_X\vert_M}\Bigr]$$

. The problem is that on a general $M$, $\mathcal{I}/\mathcal{I}^2$ is not a vector bundle, so $\tau_{\geq-1}\LL_M$ alone cannot be used to define a zero section or a Gysin map. For this reason, we must consider a two-term complex of actual vector bundles that can encode all of this information, which is precisely the following definition.

::: Definition 2 (Behrend–Fantechi)
Let $M$ be a Deligne–Mumford stack. A *perfect obstruction theory* on $M$ is a pair consisting of a complex locally quasi-isomorphic to a two-term complex of vector bundles $[E^{-1}\rightarrow E^0]$, namely $E^\bullet$, and a morphism

$$\phi:E^\bullet\longrightarrow\tau_{\geq-1}\LL_M$$

such that $h^0(\phi)$ is an isomorphism and $h^{-1}(\phi)$ is a surjection.
:::

In this definition, first, that $h^0(\phi)$ is an isomorphism means that the term of $E^\bullet$ in degree $0$ accurately reproduces the deformations of $M$. The part that required modification was that originally containing $\mathcal{I}/\mathcal{I}^2$, namely the term in degree $-1$; here, that $h^{-1}(\phi)$ is a surjection means that the term of $E^\bullet$ in degree $-1$ governs the obstructions of $M$ *without omission*. That is, having more obstructions on the side of $E^\bullet$ than in reality is permitted, but missing even one is not, and this structure provides the leeway to pick out a class of the expected dimension. 

From the complex constructed by $Z(s)\hookrightarrow X$ examined above,

$$E^\bullet=\Bigl[\at{-1}{E^\vee\vert_{Z(s)}}\xrightarrow{\ (\dd{s})^\vee\ }\at{0}{\Omega_X\vert_{Z(s)}}\Bigr]$$

to the truncation 

$$\tau_{\geq-1}\LL_{Z(s)}=[\at{-1}{\mathcal{I}/\mathcal{I}^2}\rightarrow\at{0}{\Omega_X\vert_{Z(s)}}]$$

the morphism $\phi:E^\bullet\rightarrow\tau_{\geq-1}\LL_{Z(s)}$ is given by the following diagram:

{% diagram Math/Gromov_Witten_Theory/Perfect_Obstruction_Theory-1.svg width="10.88em" alt="morphism from the local complex to the truncated cotangent complex" %}

In particular, in degree $-1$, it is defined by descending the pairing with the section $s$, $s^\vee:E^\vee\rightarrow\mathcal{O}_X$, to $\mathcal{I}/\mathcal{I}^2$; since the image of $s^\vee$ is precisely $\mathcal{I}$, this is a surjection, and thus this complex indeed becomes a perfect obstruction theory. 

Now, from a perfect obstruction theory given in this way, let us define the virtual fundamental class. In ordinary intersection theory, given a closed embedding $Z(s)\hookrightarrow X$, deformation to the normal cone deforms $X$ to the normal cone $C_{Z(s)/X}$, allowing us to define the intersection product and the Gysin map. ([\[Algebraic Varieties\] §Intersection Product, ⁋Proposition 9](/en/math/algebraic_varieties/intersection_product#prop9){: data-lid="7fg7b" data-relation="required" }) The key result of [BF] is the construction of the *intrinsic normal cone* $\mathfrak{c}_M=[C_{Z(s)/X}/T_X\vert_{Z(s)}]$, which can be obtained intrinsically without an explicit embedding being given; the perfect obstruction theory $\phi$ above realizes this as a closed embedding into the vector bundle stack $\mathfrak{E}=h^1/h^0((E^\bullet)^\vee)$:

$$\mathfrak{c}_M\hookrightarrow\mathfrak{E}=[E_1/E_0]$$

Here $E_i=(E^{-i})^\vee$. Thanks to this, just as in ordinary intersection theory, using the Gysin pullback along the zero section of $\mathfrak{E}$, we can define the virtual class

$$[M]^\vir=0^!_{E^\bullet}[\mathfrak{c}_M]\in A_{\rank E^\bullet}(M)$$

Its properties are as follows.

::: Proposition 3
For a perfect obstruction theory $\phi:E^\bullet\rightarrow\tau_{\geq-1}\LL_M$ on a Deligne–Mumford stack $M$, the virtual class $[M]^\vir=0^!_{E^\bullet}[\mathfrak{c}_M]$ satisfies the following:

1. $[M]^\vir$ is a cycle of virtual dimension $\vdim=\rank E^\bullet=\rank E^0-\rank E^{-1}$.
2. If $M$ is given as a fiber of a flat family and $\phi$ is compatible with a perfect obstruction theory over the family, then $[M]^\vir$ is the Gysin pullback of the virtual class of the family to the fiber. In particular, $[M]^\vir$ is invariant under deformations within the family.
3. If $h^1((E^\bullet)^\vee)=0$, then $M$ is smooth and $[M]^\vir=[M]$ is the usual fundamental class.
:::

## Virtual Fundamental Class of Stable Maps

Now let us construct a perfect obstruction theory on the moduli stack $M=\overline{\mathcal{M}}_{g,n}(X,\beta)$ of stable maps. To this end, we bring over the tangent space $T_X$ of the target $X$ using

$$\pi:\mathcal{C}\rightarrow M,\qquad\mu:\mathcal{C}\rightarrow X$$

That is, we pull back $T_X$ via $\mu$ and push it forward via $R\pi_\ast$ to obtain $R\pi_\ast\mu^\ast T_X$. Since the dimension of the curves is $1$, the higher direct images $R^i\pi_\ast$ survive only for $i=0,1$. Hence, this complex is a two-term complex concentrated in degrees $0$ and $1$, and at each point its cohomology recovers $H^0(C,\mu^\ast T_X)$ and $H^1(C,\mu^\ast T_X)$.

Thus, the dual $E^\bullet=(R\pi_\ast\mu^\ast T_X)^\vee$ of $R\pi_\ast\mu^\ast T_X$ obtained above is a complex of amplitude $[-1,0]$, making it a candidate for our desired perfect obstruction theory. However, because this data deforms only the map $\mu$ while fixing the domain curve $(C,p_\bullet)$, it forms a relative perfect obstruction theory with respect to the morphism $q:M\rightarrow\mathfrak{M}_{g,n}$ to the moduli stack $\mathfrak{M}_{g,n}$ of prestable curves. What helps us here is that the base stack $\mathfrak{M}_{g,n}$ is smooth; intuitively, this is because there is no obstruction to smoothing nodes. In other words, $\mathfrak{M}_{g,n}$ already possesses a (genuine) fundamental class even without a perfect obstruction theory, which we can pull back via the relative perfect obstruction theory.

::: Proposition 4 (Behrend)
For $M=\overline{\mathcal{M}}_{g,n}(X,\beta)$ and the forgetful morphism $q:M\rightarrow\mathfrak{M}_{g,n}$, the complex $E^\bullet=(R\pi_\ast\mu^\ast T_X)^\vee$ above forms a relative perfect obstruction theory $\phi:E^\bullet\rightarrow\LL_{M/\mathfrak{M}_{g,n}}$ with respect to $q$. This induces an (absolute) perfect obstruction theory $(E')^\bullet\rightarrow\tau_{\geq-1}\LL_M$ on $M$, and the dimension of the virtual class $[M]^\vir$ of $M$ obtained from this is given by the virtual dimension

$$\vdim=\int_\beta c_1(T_X)+(\dim X-3)(1-g)+n$$

.
:::

The proof strategy is to use the relative complex $(R\pi_\ast\mu^\ast T_X)^\vee$ constructed from $T_X$ on the target side and the base stack $\mathfrak{M}_{g,n}$ to which the domain curves belong, forming the distinguished triangle

$$q^\ast\LL_{\mathfrak{M}_{g,n}}\rightarrow (E')^\bullet\rightarrow E^\bullet\rightarrow q^\ast\LL_{\mathfrak{M}_{g,n}}[1]$$

between them. Here, the smoothness of the base ensures that $q^\ast\LL_{\mathfrak{M}_{g,n}}$ has no terms in negative degrees, and the fact that $M$ is a Deligne–Mumford stack kills the degree $1$ term carrying the infinitesimal automorphisms of the curve; together they keep the amplitude of $(E')^\bullet$ in $[-1,0]$, making it a perfect obstruction theory.

::: Example 5
When $X$ is convex, $H^1(C,\mu^\ast T_X)=0$ for all genus $0$ stable maps ([§Moduli Space of Stable Maps, ⁋Proposition 5](/en/math/gromov-witten_theory/moduli_of_stable_maps#prop5){: data-lid="c4h5h" data-relation="required" }), so the obstruction space is $h^1((E^\bullet)^\vee)=R^1\pi_\ast\mu^\ast T_X=0$. Now, for the same reason discussed above, the smoothness of $\mathfrak{M}_{0,n}$ also implies that the absolute obstruction is $h^1(((E')^\bullet)^\vee)=0$. Thus, by (3) of [Proposition 3](#prop3){: data-lid="vrq63" data-relation="required" },

$$[\overline{\mathcal{M}}_{0,n}(X,\beta)]^\vir=[\overline{\mathcal{M}}_{0,n}(X,\beta)]$$

and the virtual class coincides with the usual fundamental class. $X=\mathbb{P}^r$, Grassmannians, and general flag varieties $G/P$ all fall into this case; here, genus $0$ curve counting reduces to integration against the (genuine) fundamental class of the smooth moduli, which justifies the calculations in the previous post.
:::

::: Example 6
At the other extreme, we conclude this post by examining the moduli space of constant maps $\overline{\mathcal{M}}_{1,n}(X,0)\cong\overline{\mathcal{M}}_{1,n}\times X$ seen in the introduction. Since our claim in the introduction was that the obstruction survives in its entirety, let us now recalculate this in rigorous terms. 

Let the two projections be $p_1:\overline{\mathcal{M}}_{1,n}\times X\rightarrow\overline{\mathcal{M}}_{1,n}$ and $p_2:\overline{\mathcal{M}}_{1,n}\times X\rightarrow X$. For a constant map, all points on the curve are mapped to the same point in $X$, so the universal evaluation map $\mu:\mathcal{C}\rightarrow X$ factors as the composite of the projection $p_2$ and the universal curve $\pi:\mathcal{C}\rightarrow M$:

$$\mu=p_2\circ\pi$$

Therefore, the pullback of the target tangent bundle is $\mu^\ast T_X\cong\pi^\ast p_2^\ast T_X$, and pushing this down to $M$ yields by the projection formula

$$R^1\pi_\ast\mu^\ast T_X\cong(R^1\pi_\ast\mathcal{O}_{\mathcal{C}})\otimes p_2^\ast T_X$$

Applying relative Serre duality $H^1(C,\mathcal{O}_C)\cong H^0(C,\omega_C)^\vee$ to the genus $1$ universal curve over $\overline{\mathcal{M}}_{1,n}$, $R^1\pi_\ast\mathcal{O}_{\mathcal{C}}$ becomes the rank $1$ bundle $p_1^\ast(\pi_\ast\omega_{\mathcal{C}})^\vee$. Thus, the obstruction bundle is

$$h^1(((E')^\bullet)^\vee)\cong R^1\pi_\ast\mu^\ast T_X\cong p_1^\ast(\pi_\ast\omega_{\mathcal{C}})^\vee\otimes p_2^\ast T_X$$

Indeed, at each point $((C,p_\bullet),x)$, the pullback by the constant map $\mu$ trivializes as $\mu^\ast T_X\cong\mathcal{O}_C\otimes T_x X$, so the obstruction space at this point is

$$H^1(C,\mu^\ast T_X)\cong H^1(C,\mathcal{O}_C)\otimes T_x X$$

Since $C$ is a genus $1$ curve, $\dim H^1(C,\mathcal{O}_C)=1$, and hence the rank of this bundle is $\dim X=d$, matching exactly the excess dimension $d$ between the actual dimension $\dim(\overline{\mathcal{M}}_{1,n}\times X)=n+d$ and the virtual dimension $\vdim=n$ of the moduli space. Meanwhile, the moduli stack of prestable curves $\mathfrak{M}_{1,n}$ is smooth and the stability of curves is an open condition, so its open substack $\overline{\mathcal{M}}_{1,n}$ is also smooth, and together with the smoothness of the target $X$, the entire moduli stack $\overline{\mathcal{M}}_{1,n}\times X$ is smooth. Since the obstruction $h^1(((E')^\bullet)^\vee)$ is also a vector bundle, the local model of [Example 1](#ex1){: data-relation="weak" } with $s\equiv0$ applies directly to yield

$$[\overline{\mathcal{M}}_{1,n}(X,0)]^\vir=e(p_1^\ast(\pi_\ast\omega_{\mathcal{C}})^\vee\otimes p_2^\ast T_X)\cap[\overline{\mathcal{M}}_{1,n}\times X]$$

This recovers a class of dimension $n$ by capping with the Euler class on an $(n+d)$-dimensional space, effectively reenacting the situation where $s\equiv0$ from [Example 1](#ex1){: data-relation="weak" } in the moduli space of stable maps.
:::

---

**References**

**[BF]** K. Behrend, B. Fantechi, *The intrinsic normal cone*, Invent. Math. **128** (1997), 45--88.  
**[B]** K. Behrend, *Gromov–Witten invariants in algebraic geometry*, Invent. Math. **127** (1997), 601--617.  
**[LT]** J. Li, G. Tian, *Virtual moduli cycles and Gromov–Witten invariants of algebraic varieties*, J. Amer. Math. Soc. **11** (1998), 119--174.  
**[Sie]** B. Siebert, *Virtual fundamental classes, global normal cones and Fulton's canonical classes*, in *Frobenius Manifolds*, Aspects Math. **E36** (2004), 341--358.
