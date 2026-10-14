---
title: "Deformations of Nodal Curves"
description: "We present the complete computation of the local-to-global exact sequence in deformation theory for curves with nodes as local models, verifying that the local deformation sheaf is a one-dimensional skyscraper sheaf at each node and that its generator perturbs the equation in the direction of smoothing the node. After showing that deformations and infinitesimal automorphisms, including cases with marked points, are computed as vector fields on the normalization, we see that this breaks into a short exact sequence on projective curves and deduce by Riemann-Roch that the difference between the two dimensions is 3g-3+n."
excerpt: "Node smoothing, the local deformation sheaf, and the count 3g-3+n"

categories: [Math / Gromov-Witten Theory]
permalink: /en/math/gromov-witten_theory/deformations_of_nodal_curves
sidebar: 
    nav: "gromov-witten_theory-en"

date: 2026-09-13
weight: 1
translated_at: 2026-10-13T19:15:06+00:00
translation_source: antigravity-gemini-3.8-flash-high
last_polished_at: 2026-10-14T03:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
In Gromov--Witten theory, we deal with stable maps $\mu: C\rightarrow X$ into a target space $X$. Here, the domain $C$ of $\mu$ is a nodal curve equipped with additionally chosen special points. For this reason, this category begins with a post dealing with these nodal curves. More specifically, we will compute how these nodal curves deform and what automorphisms they have. 

A representative, and essentially the only, example of a nodal curve is $\x\y=0$. This is the union of the two coordinate axes $\{\x=0\}$ and $\{\y=0\}$, and the point where they meet, namely the origin, is called a *node* or *nodal point*. One of the key properties is that these nodes are singular points. ([\[Algebraic Varieties\] §Tangent Spaces and Smoothness, ⁋Example 7](/en/math/algebraic_varieties/tangent_spaces_and_smoothness#ex7){: data-lid="qnd3m" }) When dealing with spaces where such singular points exist, an effective strategy is to consider a deformation having this as the central fiber and whose nearby fibers are all smooth. As seen in [\[Schemes\] §Deformation Theory and the Cotangent Complex, ⁋Example 6](/en/math/scheme_theory/deformation_theory#ex6){: data-lid="nwt79" }, introducing a parameter $\t$ into $\x\y=0$ to turn it into $\x\y=\t$ yielded such a deformation.

More generally, when the singular points of a curve $C$ are only nodes, that is, when every singular point is étale-locally of the form $\x\y=0$, we call it a *nodal curve*. All schemes appearing in this post, including these nodal curves, are assumed to be separated and of finite type over an algebraically closed field $\mathbb{K}$. Intuitively, it is generally harmless to set $\mathbb{K}=\mathbb{C}$ and think of most schemes as varieties (except when fat points are needed).

## Prestable Curves and Normalization

First, we define the following.

::: Definition 1
For a connected projective nodal curve $C$, each of the distinct smooth points $p_1,\ldots,p_n$ is called a *marked point* of $C$. A pair $(C,p_1,\ldots,p_n)$ equipped with marked points in this way is called a *prestable curve* with $n$ marked points and genus $g=h^1(C,\mathcal{O}_C)$.
:::

That is, a prestable curve is nothing more than a nodal curve with several points additionally chosen so as not to overlap with the nodes. 

Given a nodal curve, there is a way to separate the two branches joined at a node. This is the application to nodal curves of the normalization defined in the discussion immediately following [\[Schemes\] §Dimension, ⁋Proposition 5](/en/math/scheme_theory/dimension#prop5){: data-lid="o8zf6" }; in this concrete situation, the *normalization* of $C$ means a smooth projective curve $\widetilde{C}$ and a finite morphism $\nu:\widetilde{C}\rightarrow C$ that is an isomorphism outside the nodes and has exactly two points lying over each node. 

{% diagram Math/Gromov_Witten_Theory/Deformations_of_Nodal_Curves-1.svg width="7.37em" alt="normalization separates the two branches of a node" %}

As in the figure above, in the local model at a node, this replaces $Z(\x\y)$ with the disjoint union of the two affine lines $\mathbb{A}^1_\x$ and $\mathbb{A}^1_\y$, and at the ring level, this is given by the inclusion

$$A=\mathbb{K}[\x,\y]/(\x\y)\rightarrow \widetilde{A}=\mathbb{K}[\x]\times\mathbb{K}[\y];\qquad f(\x,\y)\mapsto (f(\x,0), f(0,\y))$$

Here, looking at the two expressions $f(\x,0)$ and $f(0,\y)$, we see that their constant terms $c$ must be equal; conversely, given such a pair $(f(\x),g(\y))$, viewing $f+g-c$ in $\mathbb{K}[\x,\y]/(\x\y)$ shows that it is the preimage under this inclusion. That is, the image of this inclusion is precisely the collection of pairs whose constant terms in both components coincide. Therefore, defining $\widetilde{A}\rightarrow \mathbb{K}$ by $(f,g)\mapsto f(0)-g(0)$, there is the following short exact sequence

$$0 \rightarrow A \rightarrow \widetilde{A}\rightarrow \mathbb{K}\rightarrow 0$$

Sheafifying this, since $\nu$ is an isomorphism outside the node and the above computation at $p$ shows that the cokernel is $\kappa(p)=\mathbb{K}$, we obtain

$$0\rightarrow\mathcal{O}_C\rightarrow\nu_\ast\mathcal{O}_{\widetilde{C}}\rightarrow\kappa(p)\rightarrow0$$

For a general nodal curve, normalization performs this process simultaneously at all nodes, and therefore in this case we obtain the following short exact sequence

$$0\rightarrow\mathcal{O}_C\rightarrow\nu_\ast\mathcal{O}_{\widetilde{C}}\rightarrow\bigoplus_{p\in\Sing C}\kappa(p)\rightarrow0$$

Now assume that $C$ has $d$ nodes and $c$ irreducible components, and that the genera of the components of $\widetilde{C}$ are $g_1,\ldots,g_c$. Since $\nu$ is an affine morphism, by [\[Schemes\] §Sheaf Cohomology of Schemes, ⁋Corollary 4](/en/math/scheme_theory/sheaf_cohomology_of_schemes#cor4){: data-lid="prlmv" }, we have $H^i(C,\nu_\ast\mathcal{G})=H^i(\widetilde{C},\mathcal{G})$. Therefore, from the short exact sequence above, we obtain the formula

$$\rchi(C,\nu_\ast\mathcal{O}_{\widetilde{C}})=\rchi(C,\mathcal{O}_C)+\sum_{p\in\Sing C}\rchi(C,\kappa(p))$$

where, since each $\kappa(p)$ is a skyscraper sheaf with global sections $\mathbb{K}$ and vanishing higher cohomology, the last sum is $d$. Organizing this yields the following proposition.

::: Proposition 2
If, with $d$ nodes and $c$ irreducible components, the normalization of a connected nodal curve $C$ consists of components of genus $g_1,\ldots, g_c$, then

$$g=\sum_{j=1}^c g_j+d-c+1$$

holds.
:::

Since a projective nodal curve $C$ is étale-locally a hypersurface, it is Cohen–Macaulay, and therefore has a dualizing sheaf $\omega_C$. ([\[Algebraic Varieties\] §Serre Duality, §§Generalizations of Serre Duality](/en/math/algebraic_varieties/serre_duality#generalizations-of-serre-duality){: data-lid="jenro" }) Since this is isomorphic to $\Omega_C$ away from the nodes, it suffices to describe, for each open subset $U\subseteq C$ containing a node, the sections $\omega_C(U)$.

To this end, consider for $C$ its normalization $\nu:\widetilde{C}\rightarrow C$, and for a node $p$, let $p_1,p_2$ be its two preimages under the normalization. In the étale-local model $A=\mathbb{K}[\x,\y]/(\x\y)$ of the node, the sections of $\omega_C$ are those pairs $(\eta_1,\eta_2)$ of rational 1-forms on the two branches that, for some $a\in\mathbb{K}$, $f_1\in\mathbb{K}[\x]$, and $f_2\in\mathbb{K}[\y]$, are given in the form

$$\eta_1=\Bigl(\frac{a}{\x}+f_1(\x)\Bigr)\dd{\x},\qquad\eta_2=\Bigl(-\frac{a}{\y}+f_2(\y)\Bigr)\dd{\y}$$

.

All such pairs can be written uniquely as $(\dd{\x}/\x,-\dd{\y}/\y)$ multiplied by an element of $A$, so $\omega_C$ is a line bundle near the node with this pair as a basis, and when pulled back by $\nu$, the local basis on each branch becomes $\dd{\x}/\x$ and $-\dd{\y}/\y$. Because these form a basis for the line bundle of 1-forms allowing simple poles at the preimages of the nodes, if we let $D$ be the divisor collecting the preimages of the nodes, then

$$\nu^\ast\omega_C\cong\omega_{\widetilde{C}}(D)$$

holds. Here, let $D_j$ be the divisor collecting the points of $D$ on the component $\widetilde{C}_j$, and let $m_j$ be the number of those points. Restricting the above isomorphism to $\widetilde{C}_j$, the line bundle obtained by pulling back $\omega_C$ to this component is isomorphic to $\omega_{\widetilde{C}_j}(D_j)$. The degree of the canonical bundle of the smooth curve $\widetilde{C}_j$ is $2g_j-2$, and twisting by a divisor adds its degree, so

$$\deg\omega_{\widetilde{C}_j}(D_j)=\deg\omega_{\widetilde{C}_j}+\deg D_j=2g_j-2+m_j$$

holds. Since each node has two preimages in the normalization, we have $\sum_{j=1}^c m_j=2d$, and therefore by [Proposition 2](#prop2){: data-lid="lhuop" }, the sum of these degrees is

$$\sum_{j=1}^c(2g_j-2)+2d=2(g-d+c-1)-2c+2d=2g-2$$

Similarly, adding marked points $p_1,\ldots,p_n$, the sum of the degrees of the pullback of $\omega_C(p_1+\cdots+p_n)$ is $2g-2+n$.

## Deformations of Semistable Curves

Now we examine the deformation theory of nodal curves. At a node $p$, write $T_p^1$ for the first-order local deformation space. In [\[Schemes\] §Deformation Theory and the Cotangent Complex, ⁋Example 6](/en/math/scheme_theory/deformation_theory#ex6){: data-lid="y2bip" }, we have already computed that for the affine node $Z(\x\y)$, we have $T_p^1\cong\mathbb{K}$, and its generator can be represented by $\x\y-\epsilon$. Since every node has this local model while the local deformation of a smooth point is trivial, we obtain the following.

::: Proposition 3
At each node $p$ of a nodal curve $C$, the space $T_p^1$ of first-order local deformations is $1$-dimensional.
:::

The geometric meaning of this single dimension can be represented by the family $\x\y=\t$.

{% diagram Math/Gromov_Witten_Theory/Deformations_of_Nodal_Curves-2.svg width="51.68em" alt="the local fibers xy=t over the deformation space" %}

Meanwhile, a prestable curve is a nodal curve $C$ equipped with marked points $p_1,\ldots,p_n$ on its smooth locus. Therefore, if we add marked points to the picture above, they move along as the curve deforms, defining sections passing through each $p_i$. Since the marked points cannot coincide with one another, these sections are disjoint; thus, a first-order deformation of a prestable curve is given by the datum of a deformation of the underlying curve together with these marked sections. Here, an isomorphism between such data is an isomorphism of families over $\Spec\mathbb{K}[\epsilon]$ that is the identity on the central fiber and sends each marked section to the corresponding marked section. We denote the $\mathbb{K}$-vector space of such isomorphism classes by $T^1(C,p_\bullet)$. This is the $T^1$ of [\[Schemes\] §Deformation Theory and the Cotangent Complex, ⁋Theorem 11](/en/math/scheme_theory/deformation_theory#thm11){: data-lid="fqff9" } applied to marked curves; in the same way, we denote the $\mathbb{K}$-vector space of infinitesimal automorphisms preserving all marked sections by $T^0(C,p_\bullet)$. 

Since these $T^0(C,p_\bullet)$ and $T^1(C,p_\bullet)$ are determined by the additional conditions that the newly added marked points impose on the underlying nodal curve, it is reasonable to consider these two conditions separately. First, for deformations, we have already seen above that $T_p^1$ arises only at the nodes, and by definition the marked points lie only on smooth points, so they do not affect this. That is, $T_p^1$ computed at the nodes remains the same for prestable curves. 

What the newly added marked points affect is the automorphism side, where an infinitesimal automorphism must preserve the marked sections. Locally, for a function $f$ on $C$, an automorphism $\Phi$ must be of the form

$$\Phi(f)=f+\epsilon v(f)$$

and for this to preserve multiplication, $v(fg)=fv(g)+gv(f)$ must hold. That is, $v$ is a $\mathbb{K}$-derivation of $\mathcal{O}_C$, and conversely, such a derivation always defines an automorphism by the formula above. Now, the part where a prestable curve has infinitesimal automorphisms differing from those of the nodal curve is near the marked sections, as mentioned above, so let us examine this near each marked point $p_i$. Suppose that $p_i$ is locally given by $\z=0$. By [\[Schemes\] §Smooth and Étale Morphisms, ⁋Theorem 7](/en/math/scheme_theory/smooth_and_etale_morphisms#thm7){: data-lid="x011e" }, $\Omega_{C/\mathbb{K}}$ is a locally free sheaf of rank $1$ in this neighborhood and $\dd{\z}$ is a local basis, so by the universal property of differentials, any derivation is determined by the image $v(\z)$ of $\dd{\z}$. The corresponding automorphism is given by

$$\z\mapsto\z+\epsilon v(\z)$$

and since we chose $\z=0$ to represent (locally) the marked section, for this to be preserved, $v(\z)$ must vanish at the marked point. That is, we must have $v(\z)\in(\z)$. Now, setting $\Sigma=p_1+\cdots+p_n$, its ideal sheaf is $\mathcal{I}_\Sigma=\mathcal{O}_C(-\Sigma)$, so the sheaf of derivations satisfying this condition is

$$\sHom(\Omega_{C/\mathbb{K}},\mathcal{I}_\Sigma)=\mathcal{T}_{C/\mathbb{K}}\otimes\mathcal{I}_\Sigma=\mathcal{T}_{C/\mathbb{K}}(-\Sigma)$$

and this computes the infinitesimal automorphisms of the marked curve. 

Now what remains is the computation of $\mathcal{T}_{C/\mathbb{K}}=\sHom(\Omega_{C/\mathbb{K}}, \mathcal{O}_C)$. For this, we choose the local model $R=\mathbb{K}[\x,\y]/(\x\y)$ and examine derivations on it. Any derivation $v$ is determined by its values on the generators, $a=v(\x)$ and $b=v(\y)$, and as in the computation of [\[Schemes\] §Deformation Theory and the Cotangent Complex, ⁋Example 6](/en/math/scheme_theory/deformation_theory#ex6){: data-lid="7kwur" }, to preserve the relation $\x\y=0$ we must have

$$0=v(\x\y)=\y a+\x b$$

Here, $\y a=-\x b$ belongs to both $(\y)$ and $(\x)$, and in $R$, since $(\x)\cap(\y)=0$, we have $\y a=\x b=0$. Furthermore, because $\ann(\y)=(\x)$ and $\ann(\x)=(\y)$, we have $a\in\x\mathbb{K}[\x]$ and $b\in\y\mathbb{K}[\y]$. 

Geometrically, this reflects the situation where the two branches are separated in the normalization of $R$. That is, if we write the normalization of $R$ as $\widetilde{R}=\mathbb{K}[\x]\oplus\mathbb{K}[\y]$, then $a$ and $b$ above become derivations on each branch of the normalization, and are functions vanishing at their respective origins. 

Now viewing this on the entire nodal curve, if we denote the two preimages of a node $p$ in the normalization $\nu:\widetilde{C}\rightarrow C$ by $p',p''$, these are derivations vanishing at $p'$ and $p''$ respectively, and since $\nu$ is an isomorphism outside the nodes, these local identifications glue canonically. Therefore, if we let $D$ be the divisor consisting of the two preimages of all nodes, this computation is summarized as follows.

::: Proposition 4
For a nodal curve $C$, its normalization $\nu:\widetilde{C}\rightarrow C$, and the divisor $D$ on $\widetilde{C}$ consisting of the preimages of the nodes,

$$\mathcal{T}_{C/\mathbb{K}}\cong\nu_\ast\bigl(\mathcal{T}_{\widetilde{C}/\mathbb{K}}(-D)\bigr)$$

holds. If we denote the preimage of the marked points by $\widetilde{\Sigma}$, then similarly $\mathcal{T}_{C/\mathbb{K}}(-\Sigma)\cong\nu_\ast(\mathcal{T}_{\widetilde{C}/\mathbb{K}}(-D-\widetilde{\Sigma}))$ holds.
:::

Indeed, the second isomorphism is obtained by adding the vanishing condition at the marked points to the first isomorphism. Therefore, taking global sections, we have

$$T^0(C,p_\bullet)\cong H^0\bigl(C,\nu_\ast\mathcal{T}_{\widetilde{C}/\mathbb{K}}(-D-\widetilde{\Sigma})\bigr)=H^0\bigl(\widetilde{C},\mathcal{T}_{\widetilde{C}/\mathbb{K}}(-D-\widetilde{\Sigma})\bigr)$$

Here, the last equality holds because $H^0(C,\nu_\ast\mathcal{F})=H^0(\widetilde{C},\mathcal{F})$ by definition of the pushforward. Thus infinitesimal automorphisms are computed as derivations on the normalization that vanish at all preimages of the nodes and at the marked points.

According to the standard interpretation in deformation theory, this calculation can be interpreted as finding the tangent space of the automorphism group of a nodal curve, or more generally a prestable curve. ([\[Schemes\] §Deformation Theory and the Cotangent Complex, ⁋Theorem 5](/en/math/scheme_theory/deformation_theory#thm5){: data-lid="u7v2l" }) Letting this automorphism group be $G=\Aut(C,p_\bullet)$ and its identity element be $e$, the elements of the tangent space $T_eG$ at the identity are the collection of $\mathbb{K}[\epsilon]$-valued points $\Spec\mathbb{K}[\epsilon]\rightarrow G$ whose closed point maps to the identity. ([\[Schemes\] §From Varieties to Schemes, ⁋Example 4](/en/math/scheme_theory/from_varieties_to_schemes#ex4){: data-lid="jhbqv" }) That is, intuitively, this can be thought of as a family of automorphisms that restricts to the identity map on the central fiber, and from this we obtain the identification

$$T_eG\cong T^0(C,p_\bullet)\cong H^0\bigl(\widetilde{C},\mathcal{T}_{\widetilde{C}/\mathbb{K}}(-D-\widetilde{\Sigma})\bigr)$$

From the calculation above, we know that any automorphism is locally written in the form $f\mapsto f+\epsilon v(f)$; since the derivation $v$ means a vector field on the smooth curve $\widetilde{C}$, this expression can be interpreted as saying that the direction in which an automorphism infinitesimally moves from the identity is represented by a vector field on the normalization.

Let us rephrase the calculations up to this point in the language of [\[Schemes\] §Deformation Theory and the Cotangent Complex, ⁋Theorem 11](/en/math/scheme_theory/deformation_theory#thm11){: data-lid="6chlh" }. Through this, we can glue together the local calculations performed in the preceding propositions into deformations of the entire curve, and even compute $T^2$, where the obstructions to higher-order deformations lie. For convenience of notation, if we set $\LL_C=\LL_{C/\mathbb{K}}$ and $\Omega_C=\Omega_{C/\mathbb{K}}$, then in the absence of marked points, the spaces

$$T^i(C)=\Ext^i_C(\LL_C,\mathcal{O}_C)$$

provided by this theorem for $i=0,1,2$ can be interpreted geometrically as follows.

- $T^1(C)$ measures the isomorphism classes of flat families over $\Spec\mathbb{K}[\epsilon]$ whose central fiber is $C$, namely the first-order deformations of $C$. Here, the trivial deformation $C\times\Spec\mathbb{K}[\epsilon]$ corresponds to $0$.
- $T^0(C)$ measures the automorphisms of the trivial deformation that restrict to the identity on the central fiber, namely the infinitesimal automorphisms of $C$. As seen earlier, these are locally of the form $f\mapsto f+\epsilon v(f)$, so $T^0(C)$ is the space of global vector fields on $C$, and is the tangent space of $\Aut(C)$ at the identity.
- $T^2(C)$ controls the obstruction to extending such deformations to higher-order deformations.

In general, $\LL_C$ is a complex with terms in degree $0$ and above, and for a general singular scheme there is no way to transfer the information contained in this complex to $\Omega_C$. However, in our case of nodal curves, $\LL_C$ is quasi-isomorphic to $\Omega_C$ placed in degree $0$, which, as seen below, stems from the fact that the local model of a node is a hypersurface and is reduced. To verify this, we first define $\LL_C\rightarrow H_0(\LL_C)$. This map is defined only in degree $0$ as the quotient map $(\LL_C)_0\rightarrow H_0(\LL_C)$, and as $0$ in the remaining degrees. One can verify that this map is well-defined independently of the choice of complex representing $\LL_C$. Furthermore, as seen just before [\[Schemes\] §Deformation Theory and the Cotangent Complex, ⁋Proposition 9](/en/math/scheme_theory/deformation_theory#prop9){: data-lid="cj6r9" }, we have $H_0(\LL_C)=\Omega_C$, so this map is a morphism $\LL_C\rightarrow\Omega_C$, which by definition is an isomorphism on $H_0$.

Our claim is that this also satisfies $H_i(\LL_C)=0$ for all $i\geq1$, and since this is a local condition, it suffices to check it in a neighborhood of each point. First, in a neighborhood of a smooth point of $C$, the cotangent complex is quasi-isomorphic to a single locally free sheaf $\Omega_C$ as in the proof of [\[Schemes\] §Deformation Theory and the Cotangent Complex, ⁋Proposition 9](/en/math/scheme_theory/deformation_theory#prop9){: data-lid="xoabf" }, so there is nothing more to show. What could be problematic is near the nodes; étale-locally, $C$ is given by the local model $R=\mathbb{K}[\x,\y]/(\x\y)$, and since the cotangent complex is compatible with pullback by étale morphisms, it suffices to check on $R$. Since this is obtained by cutting out $\mathbb{K}[\x,\y]$ by a single nonzerodivisor, it is a local complete intersection ([\[Schemes\] §Complete Intersections, ⁋Definition 1](/en/math/scheme_theory/complete_intersections#def1){: data-lid="9arnl" }), and hence, as seen in [\[Schemes\] §Deformation Theory and the Cotangent Complex, §§Naive Cotangent Complex and Smoothness](/en/math/scheme_theory/deformation_theory#naive-cotangent-complex-and-smoothness){: data-lid="mc2dh" }, $\LL_R$ is quasi-isomorphic to the naive cotangent complex $\NL_R$ associated with the presentation $\mathbb{K}[\x,\y]\rightarrow R$. Since the conormal module $(\x\y)/(\x\y)^2$ of this presentation is a free $R$-module with the class of $\x\y$ as a basis, substituting $f=\x\y$ into the Jacobian calculation at the corresponding link yields

$$\LL_R\simeq \NL_R\cong\Bigl[\at{1}{R}\overset{\bar{d}}{\rightarrow}\at{0}{R\dd{\x}\oplus R\dd{\y}}\Bigr],\qquad\bar{d}(1)=\y\dd{\x}+\x\dd{\y}$$

Now, all we have to show is that $H_1(\NL_R)=\ker\bar{d}$ is $0$. Indeed, if

$$\bar{d}(c)=c(\y\dd{\x}+\x\dd{\y})=0$$

then since $R\dd{\x}\oplus R\dd{\y}$ is free, we have $c\y=c\x=0$, and as examined earlier,

$$\ann(\y)=(\x),\qquad \ann(\x)=(\y)$$

and since $(\x)\cap(\y)=0$, we have $c=0$. In addition, since $\NL_R$ has terms only in degrees $0$ and $1$, for $i\geq2$ we also have $H_i(\LL_R)=0$. Having thus verified that for $i\geq1$, $H_i(\LL_C)=0$ holds both in a neighborhood of a smooth point and in a neighborhood of a node, $\LL_C\rightarrow\Omega_C$ is a quasi-isomorphism. Meanwhile, since $T^i(C)=\Ext^i_C(\LL_C,\mathcal{O}_C)$ and $\mathcal{T}^q_{C/\mathbb{K}}=\sExt^q(\LL_C,\mathcal{O}_C)$ are originally objects defined in the derived category $D(\mathcal{O}_C)$, we may now replace $\LL_C$ by $\Omega_C$ when computing them. That is,

$$T^i(C)=\Ext^i_C(\Omega_C,\mathcal{O}_C),\qquad\mathcal{T}^q_{C/\mathbb{K}}=\sExt^q(\Omega_C,\mathcal{O}_C)$$

holds. Here, $\mathcal{T}^q_{C/\mathbb{K}}$ is the local data of [\[Schemes\] §Deformation Theory and the Cotangent Complex, ⁋Theorem 12](/en/math/scheme_theory/deformation_theory#thm12){: data-lid="6d3kc" }, and in particular $\mathcal{T}^0_{C/\mathbb{K}}$ is the $\mathcal{T}_{C/\mathbb{K}}$ calculated earlier.

First, since the marked points lie on the smooth locus, $\mathcal{O}_C(\Sigma)$ is a line bundle, and we compute the sheaf Ext of $\Omega_C$ twisted by this, namely $\Omega_C(\Sigma)=\Omega_C\otimes\mathcal{O}_C(\Sigma)$. What we shall show are the equations

$$\sHom(\Omega_C(\Sigma),\mathcal{O}_C)=\mathcal{T}_{C/\mathbb{K}}(-\Sigma),\qquad\sExt^1(\Omega_C(\Sigma),\mathcal{O}_C)=\bigoplus_{p\in\Sing C}T_p^1,\qquad\sExt^q(\Omega_C(\Sigma),\mathcal{O}_C)=0\quad(q\geq2)$$

In a neighborhood of a smooth point, $\Omega_C(\Sigma)=\Omega_C\otimes\mathcal{O}_C(\Sigma)$ is a line bundle, so for $q\geq1$ we have $\sExt^q=0$, and $\sHom$ is its dual $\mathcal{T}_{C/\mathbb{K}}\otimes\mathcal{O}_C(-\Sigma)=\mathcal{T}_{C/\mathbb{K}}(-\Sigma)$, namely the sheaf of infinitesimal automorphisms preserving the marked points. What is problematic is near the nodes; since the marked points do not meet the nodes, we have $\Omega_C(\Sigma)=\Omega_C$ in this neighborhood, and as before, it suffices to compute in the local model $R=\mathbb{K}[\x,\y]/(\x\y)$ the module $\Ext^q_R(\Omega_R,R)$. First, since we showed earlier that $\bar{d}$ is injective,

$$0\rightarrow R\overset{\bar{d}}{\rightarrow}R\dd{\x}\oplus R\dd{\y}\rightarrow\Omega_R\rightarrow0$$

is a free resolution of $\Omega_R$ consisting of two terms, and applying $\Hom_R(-,R)$ to this, we can compute $\Ext^q_R(\Omega_R,R)$ as the cohomology of the complex

$$\at{0}{\Hom_R(R\dd{\x}\oplus R\dd{\y},R)}\overset{\bar{d}^\ast}{\rightarrow}\at{1}{\Hom_R(R,R)}$$

in degree $q$. In particular, for $q\geq 2$, this value becomes $0$, so there is no local obstruction near the nodes either. An element in the left term of the above complex is determined by its values on $\dd{\x}$ and $\dd{\y}$ as $(a,b)$, and an element in the right term by its value on $1$. Since $\bar{d}(1)=\y\dd{\x}+\x\dd{\y}$, we can write $\bar{d}^\ast$ as

$$R^2\rightarrow R,\qquad(a,b)\mapsto a\y+b\x$$

Computing the cohomology directly using this explicit map, the degree $0$ cohomology $\ker\bar{d}^\ast$ consists of the $(a,b)$ satisfying $a\y+b\x=0$, which is identical to the condition $v(\x\y)=\y a+\x b=0$ obtained for the derivation $v$ before [Proposition 4](#prop4){: data-lid="4akca" }; hence we have $\Hom_R(\Omega_R,R)=\Der_\mathbb{K}(R,R)$, and we recover the sheaf $\mathcal{T}_{C/\mathbb{K}}$ of infinitesimal automorphisms in this neighborhood. The degree $1$ cohomology is $\coker\bar{d}^\ast$, and since the image of $\bar{d}^\ast$ is the ideal generated by $\x$ and $\y$, this becomes $R/(\x,\y)=\mathbb{K}$. Since these give a $1$-dimensional space supported at each node, by the identification $\mathcal{T}^1_{C/\mathbb{K}}=\sExt^1(\Omega_C,\mathcal{O}_C)$, we see that this is precisely the deformation space $T_p^1$ of the node. That is, our earlier examination of the effect of the marked points by dividing it into $T^0$ and $T^1$ was in fact computing the sheaf Ext of $\Omega_C(\Sigma)$.

Indeed, $\Omega_C(\Sigma)$ is the object measuring deformations in the presence of marked points. To see this, first consider the short exact sequence

$$0\rightarrow\Omega_C\rightarrow\Omega_C(\Sigma)\rightarrow\bigoplus_{j=1}^n\kappa(p_j)\rightarrow0$$

Applying $\Hom_C(-,\mathcal{O}_C)$ to this, we obtain the long exact sequence

$$0\rightarrow\Ext^0_C(\Omega_C(\Sigma),\mathcal{O}_C)\rightarrow\Ext^0_C(\Omega_C,\mathcal{O}_C)\rightarrow\bigoplus_{j=1}^nT_{p_j}C\rightarrow\Ext^1_C(\Omega_C(\Sigma),\mathcal{O}_C)\rightarrow\Ext^1_C(\Omega_C,\mathcal{O}_C)\rightarrow0$$

and the isomorphism $\Ext^2_C(\Omega_C(\Sigma),\mathcal{O}_C)\cong\Ext^2_C(\Omega_C,\mathcal{O}_C)$. Here, we used the isomorphism

$$\Ext^q_C(\kappa(p_j),\mathcal{O}_C)\cong\begin{cases}T_{p_j}C&q=1\\0&q\neq1\end{cases}$$

On the other hand, if we directly trace the process of forgetting marked points in the language of deformations, we obtain the exact sequence

$$0\rightarrow T^0(C,p_\bullet)\rightarrow T^0(C)\rightarrow\bigoplus_{j=1}^nT_{p_j}C\rightarrow T^1(C,p_\bullet)\rightarrow T^1(C)\rightarrow0$$

Here, $T^0(C)\rightarrow\bigoplus_{j=1}^nT_{p_j}C$ sends a vector field to its values at each $p_j$, $\bigoplus_{j=1}^nT_{p_j}C\rightarrow T^1(C,p_\bullet)$ moves only the marked points while leaving the curve fixed, and $T^1(C,p_\bullet)\rightarrow T^1(C)$ forgets the marked points. Comparing this with the long exact sequence above, we have $T^0(C,p_\bullet)=\Ext^0_C(\Omega_C(\Sigma),\mathcal{O}_C)$ and $T^i(C)=\Ext^i_C(\Omega_C,\mathcal{O}_C)$, and the evaluation maps are also the same; therefore, the remaining two terms $T^1(C,p_\bullet)$ and $\Ext^1_C(\Omega_C(\Sigma),\mathcal{O}_C)$ have the same dimension and are in fact canonically isomorphic. That is, the long exact sequence above expresses the process of forgetting marked points in terms of $\Ext$. Accordingly, from now on we write $T^i(C,p_\bullet)=\Ext^i_C(\Omega_C(\Sigma),\mathcal{O}_C)$ for $i=0,1,2$, and in the case $i=2$, this is equal to $T^2(C)$ by the isomorphism above.

## Dimension Computation

The deformation space $T^1(C,p_\bullet)$ represents the direction of moving from a point $(C,p_\bullet)$ (a marked prestable curve) to neighboring points, and thus plays the role of a tangent space when viewed in the space of these prestable curves. Here, we must subtract the degrees of freedom $T^0(C,p_\bullet)$ of infinitesimal automorphisms representing the same point, and our goal is to compute this difference.

To this end, we need cohomology vanishing for prestable curves; for this purpose, choose a projective embedding $C\subseteq\mathbb{P}^N$ and select a codimension $2$ linear subspace $\Lambda=H_1\cap H_2$ that does not intersect $C$. Then $U_i=C\setminus H_i$ is affine and $U_1\cup U_2=C$; thus, computing on $C$ the sheaf cohomology of any quasi-coherent sheaf $\mathcal{F}$ via Čech cohomology, we know that in degree $2$ and above, $H^i(C, \mathcal{F})=0$ holds. Using this, we can show the following.

::: Theorem 5
For an $n$-pointed prestable curve $(C, p_\bullet)$, if we denote the set of nodes of $C$ by $\Sing C$, the exact sequence

$$0 \rightarrow H^1\bigl(C, \mathcal{T}_{C/\mathbb{K}}(-\Sigma)\bigr) \rightarrow T^1(C, p_\bullet) \rightarrow \bigoplus_{p\in\Sing C}\mathbb{K} \rightarrow 0$$

holds, and moreover $T^0(C, p_\bullet)=H^0(C, \mathcal{T}_{C/\mathbb{K}}(-\Sigma))$.
:::
::: Proof
As computed earlier, the marked points add the twist $(-\Sigma)$ to the automorphism sheaf, but do not change the local deformation space $T_p^1$ of the nodes. Therefore, from [\[Schemes\] §Deformation Theory and the Cotangent Complex, ⁋Theorem 12](/en/math/scheme_theory/deformation_theory#thm12){: data-lid="940xu" }, we obtain

$$0\rightarrow H^1\bigl(C,\mathcal{T}_{C/\mathbb{K}}(-\Sigma)\bigr)\rightarrow T^1(C,p_\bullet)\rightarrow\bigoplus_{p\in\Sing C}T_p^1\rightarrow H^2\bigl(C,\mathcal{T}_{C/\mathbb{K}}(-\Sigma)\bigr)$$

where the last term is $0$ by the vanishing above. Also, by [Proposition 3](#prop3){: data-lid="8ouk8" }, we have $T_p^1\cong\mathbb{K}$, from which we obtain the desired short exact sequence. The last claim follows by considering the degree $0$ part of this long exact sequence.
:::

Intuitively, this exact sequence splits the deformations of a prestable curve into two layers. The left term represents the degrees of freedom in deforming the components of the normalization along with the positions of the node preimages and marked points on them while preserving the local models of all nodes, and the right term represents the degrees of freedom in choosing which nodes to smooth. Then our key claim is as follows.

::: Corollary 6
For an $n$-pointed, genus $g$ prestable curve $(C, p_\bullet)$,

$$\dim T^1(C, p_\bullet)-\dim T^0(C, p_\bullet)=3g-3+n$$

holds.
:::
::: Proof
For convenience of notation, write $\mathcal{H}=\mathcal{T}_{C/\mathbb{K}}(-\Sigma)$, and let the number of nodes of $C$ be $d$. Then by [Theorem 5](#thm5){: data-lid="c3l1e" },

$$\dim T^1=h^1(\mathcal{H})+d,\qquad \dim T^0=h^0(\mathcal{H})$$

so the value to be computed is $d-\rchi(C, \mathcal{H})$. Now by [Proposition 4](#prop4){: data-lid="arwum" } and [\[Schemes\] §Sheaf Cohomology of Schemes, ⁋Corollary 4](/en/math/scheme_theory/sheaf_cohomology_of_schemes#cor4){: data-lid="tpsgt" },

$$\rchi(C, \mathcal{H})=\rchi\bigl(\widetilde{C}, \mathcal{T}_{\widetilde{C}/\mathbb{K}}(-D-\widetilde{\Sigma})\bigr)$$

holds.

Let us compute the right-hand side of the above equality on each component. For a genus $g_j$ component $\widetilde{C}_j$, applying [\[Algebraic Varieties\] §The Riemann–Roch Theorem for Curves, ⁋Proposition 3](/en/math/algebraic_varieties/riemann_roch_theorem#prop3){: data-lid="khrzv" } to its canonical divisor $K_{\widetilde{C}_j}$, we obtain $\deg\omega_{\widetilde{C}_j}=2g_j-2$. Therefore, $\mathcal{T}_{\widetilde{C}_j/\mathbb{K}}\cong\omega_{\widetilde{C}_j}^\vee$ is a line bundle of degree $2-2g_j$. Letting the number of points of $D+\widetilde{\Sigma}$ lying on it be $s_j$, the degree of the twisted line bundle is $2-2g_j-s_j$, and by the same proposition,

$$\rchi\bigl(\widetilde{C}_j, \mathcal{T}_{\widetilde{C}_j/\mathbb{K}}(-D-\widetilde{\Sigma})\bigr)=(2-2g_j-s_j)+1-g_j=3-3g_j-s_j$$

holds. Now, since each node gives two preimages and each marked point gives one, we have $\sum_js_j=2d+n$, and therefore for the $c$ components,

$$\rchi(C, \mathcal{H})=\sum_{j=1}^c(3-3g_j-s_j)=3c-3\sum_jg_j-2d-n$$

holds. Substituting $\sum_jg_j=g-d+c-1$ given by [Proposition 2](#prop2){: data-lid="b8s52" } into this, we obtain

$$\rchi(C, \mathcal{H})=3c-3(g-d+c-1)-2d-n=-3g+d+3-n$$

which gives the desired result.
:::

The crux of this calculation is that the right-hand side does not depend on $d$ and $c$. Creating one more node adds one local deformation, but reduces the gluing degrees of freedom by the same amount, so the difference between the two dimensions is determined solely by the topological data $g$ and $n$ of the curve.

## Vanishing of Obstructions

Earlier, we saw that $T^1(C,p_\bullet)$ plays the role of the tangent space to the space of prestable curves. If the stack is smooth, its dimension is $\dim T^1(C,p_\bullet)-\dim T^0(C,p_\bullet)$. In general, however, moduli spaces are very singular, so we cannot expect this. Therefore, to verify smoothness, let us examine whether a given deformation can continue to be extended over a thicker base. For this purpose, we replace $\mathbb{K}[\epsilon]$ with an algebra whose residue field is $\mathbb{K}$, namely a general local Artin $\mathbb{K}$-algebra $A$.

For a local Artin $\mathbb{K}$-algebra $A$, a *deformation* of $(C,p_\bullet)$ over $A$ is the choice of a flat proper family $\pi_A:\mathcal{C}_A\rightarrow\Spec A$, an identification $\mathcal{C}_A\times_{\Spec A}\Spec\mathbb{K}\cong C$ of the central fiber, and mutually disjoint sections restricting to $p_j$ under this identification, $\sigma_{j,A}:\Spec A\rightarrow\mathcal{C}_A$. The first-order deformation discussed earlier is the special case where $A=\mathbb{K}[\epsilon]$. Extending this along a surjection $A'\rightarrow A$ means finding a deformation over $A'$ such that

$$\mathcal{C}_{A'}\times_{\Spec A'}\Spec A\cong\mathcal{C}_A$$

preserves the identification of the central fiber and the marked sections. In other words, this adds higher-order data while maintaining the deformation already given.

For the surjection $A'\rightarrow A$ given above, let its kernel be $J$, and let the maximal ideal of $A'$ be $\mathfrak{m}$. Since $A'$ is a local Artin ring, we have $\mathfrak{m}^N=0$ for some $N$, and therefore this surjection factors as

$$A'=A'/\mathfrak{m}^NJ\rightarrow\cdots\rightarrow A'/\mathfrak{m}J\rightarrow A'/J=A$$

Since the kernel $\mathfrak{m}^rJ/\mathfrak{m}^{r+1}J$ at each stage is annihilated by the maximal ideal of the source ring, it suffices to show the extension only when $\mathfrak{m}_{A'}I=0$ for the kernel $I$ of the surjection $A'\rightarrow A$. In this case, since $I^2=0$, $A'\rightarrow A$ is a square-zero extension, and therefore we can apply [\[Schemes\] §Deformation Theory and the Cotangent Complex, ⁋Theorem 11](/en/math/scheme_theory/deformation_theory#thm11){: data-lid="cmkkl" }. Then, since the coefficient sheaf is $\mathcal{O}_C\otimes_\mathbb{K}I$ on the central fiber, using flat base change and $L_C\simeq\Omega_C$, this obstruction lies in

$$\ob(\mathcal{C}_A/A')\in\Ext^2_C(\Omega_C,\mathcal{O}_C\otimes_\mathbb{K}I)\cong T^2(C)\otimes_\mathbb{K}I$$

and its being $0$ is equivalent to the existence of an extension. After extending the curve, the marked sections always extend by smoothness near $p_j$, so what we need to show is that $T^2(C)\cong\Ext^2_C(\Omega_C(\Sigma),\mathcal{O}_C)$ is $0$. To verify this, in the spectral sequence given by [\[Sheaf Theory\] §Derived Category of Sheaves and Derived Functors, ⁋Corollary 11](/en/math/sheaf_theory/derived_category_of_sheaves#cor11){: data-lid="r5mnh" },

$$E_2^{p,q}=H^p\bigl(C,\sExt^q(\Omega_C(\Sigma),\mathcal{O}_C)\bigr)\Rightarrow\Ext^{p+q}_C(\Omega_C(\Sigma),\mathcal{O}_C)$$

looking at the total degree $2$ part yields the following.

::: Proposition 7
For a prestable curve with $n$ marked points, $(C,p_\bullet)$, we have $\Ext^2_C(\Omega_C(\Sigma),\mathcal{O}_C)=0$. Therefore, deformations of $(C,p_\bullet)$ are *unobstructed*. 
:::
::: Proof
As seen before [Theorem 5](#thm5){: data-lid="suizo" }, the cohomology of any quasi-coherent sheaf on $C$ vanishes in degree $2$ and above, so 

$$E_2^{2,0}=H^2\bigl(C,\sExt^0(\Omega_C(\Sigma),\mathcal{O}_C)\bigr)=H^2(C,\mathcal{T}_{C/\mathbb{K}}(-\Sigma))=0$$

Also, we verified there that $\sExt^1(\Omega_C(\Sigma),\mathcal{O}_C)$ is a skyscraper sheaf supported at the nodes, so its higher cohomology vanishes and 

$$E_2^{1,1}=H^1\bigl(C,\sExt^1(\Omega_C(\Sigma),\mathcal{O}_C)\bigr)=0$$

and finally, since $\sExt^2(\Omega_C(\Sigma),\mathcal{O}_C)=0$, we have $E_2^{0,2}=0$. Therefore, since all $E_2$ terms of total degree $2$ are $0$, we have $\Ext^2_C(\Omega_C(\Sigma),\mathcal{O}_C)=0$.
:::

Consider the formal neighborhood of the point $[(C,p_\bullet)]$. With residue field $\mathbb{K}$, this is given by a complete local $\mathbb{K}$-algebra $S$; intuitively, $S/\mathfrak{m}_S^{k+1}$ is the $k$-th infinitesimal neighborhood of that point, that is, a point thickened only up to order $k$, and since $S$ is their inverse limit, considering $S$ means taking the limit by successively increasing this to view all orders. Now, if for each $k$, the deformations over $S/\mathfrak{m}_S^{k+1}$ of $(C,p_\bullet)$ of order $k$, $\mathcal{C}_k$, are compatible with this inverse system (that is, if the base change of $\mathcal{C}_{k+1}$ to $S/\mathfrak{m}_S^{k+1}$ is isomorphic as a deformation to $\mathcal{C}_k$), then we call this a *formal deformation* over $S$. For example, if $S=\mathbb{K}[[\t]]$, this is a collection obtained by successively extending families matched by increasing the order with respect to $\t$. If $S$ is a local Artinian $\mathbb{K}$-algebra, then for sufficiently large $k$ we have $S/\mathfrak{m}_S^{k+1}=S$, so a formal deformation over $S$ is simply a deformation over $S$. That is, a deformation over a local Artinian $\mathbb{K}$-algebra is a special case of a formal deformation subject to the finiteness condition of having finite thickness.

Now let us fix, with residue field $\mathbb{K}$, a complete local $\mathbb{K}$-algebra $R$. Then a formal deformation $\mathcal{X}$ defined over it is said to be *versal* if, given any formal deformation, it is determined as a pullback of $\mathcal{X}$. More precisely, given any formal deformation over an algebra with residue field $\mathbb{K}$, an arbitrary complete local $\mathbb{K}$-algebra $S$, this formal deformation can be obtained by pulling back along some local homomorphism $R\rightarrow S$ the deformation $\mathcal{X}$; and we additionally require that in the case $S=\mathbb{K}[\epsilon]$, such a local homomorphism is *uniquely* determined. Intuitively, a local homomorphism $R\rightarrow\mathbb{K}[\epsilon]$ is a tangent vector of $R$, and since deformations over $\mathbb{K}[\epsilon]$ form $T^1(C, p_\bullet)$, this condition identifies the tangent space of $R$ with $T^1(C, p_\bullet)$. 

Then it is known that $(C,p_\bullet)$ has a versal formal deformation. Intuitively, for $N=\dim T^1(C,p_\bullet)$, this is done by taking a basis of $T^1(C,p_\bullet)$ and corresponding coordinates $\s_1,\ldots,\s_N$, starting from a first-order deformation over $\mathbb{K}[[\s_1,\ldots,\s_N]]/(\s_1,\ldots,\s_N)^2$, and extending it order by order. Since the obstruction to extension at each step is controlled by $T^2(C)$ according to [\[Schemes\] §Deformation Theory and the Cotangent Complex, ⁋Theorem 11](/en/math/scheme_theory/deformation_theory#thm11){: data-lid="lqfm6" }, an extension is possible only if we impose relations among $\s_1,\ldots,\s_N$ so that these obstructions vanish. The resulting ring satisfies, for the ideal $J$ generated by these relations,

$$R\cong\mathbb{K}[[\s_1,\ldots,\s_N]]/J\tag{$\ast$}$$

where the number of relations required is at most $\dim T^2(C)$. However, in our case, we have $T^2(C)=0$ by [Proposition 7](#prop7){: data-lid="ctbij" }, so $J=0$ and hence $R\cong\mathbb{K}[[\s_1,\ldots,\s_N]]$. This means that the formal neighborhood of the point $[(C,p_\bullet)]$ is smooth. ([\[Commutative Algebra\] §Regular Local Rings, ⁋Proposition 4](/en/math/commutative_algebra/regular_local_rings#prop4){: data-lid="v5ayc" }, [\[Schemes\] §Smooth and Étale Morphisms, ⁋Definition 1](/en/math/scheme_theory/smooth_and_etale_morphisms#def1){: data-lid="fzprr" }) We call this $R$ the *versal base* of $(C,p_\bullet)$. In particular, if $T^0(C,p_\bullet)=0$, the above local homomorphism is unique not only for $S=\mathbb{K}[\epsilon]$ but for all $S$, and in this case we call the versal formal deformation *universal*. 

## Moduli Stack of Prestable Curves

The calculations so far were carried out in a neighborhood of a single curve $(C,p_\bullet)$, that is, over its versal base. However, since this argument holds for any prestable curve $(C,p_\bullet)$, the moduli of prestable curves will be smooth at every point. To define this moduli space, it suffices to specify the families defined over an arbitrary scheme $T$ ([\[Stacks\] §Moduli Spaces, ⁋Definition 1](/en/math/stacks/moduli_spaces#def1){: data-lid="lvrdq" })

::: Definition 8
Over a scheme $T$, a *prestable curve* of genus $g$ with $n$ marked points is a pair consisting of a flat proper morphism $\pi:\mathcal{C}\rightarrow T$ and sections $\sigma_1,\ldots,\sigma_n:T\rightarrow\mathcal{C}$ such that for each of $T$'s geometric points $\bar{t}$, the fiber $(\mathcal{C}_{\bar{t}},\sigma_1(\bar{t}),\ldots,\sigma_n(\bar{t}))$ is a prestable curve with $n$ marked points of genus $g$. The moduli functor that assigns to each scheme $T$ the groupoid formed by these and the $T$-isomorphisms between them that preserve the sections is denoted by $\mathfrak{M}_{g,n}$.
:::

It is well known that this moduli functor is an algebraic stack locally of finite type, that is, a moduli stack in the sense of [\[Stacks\] §Moduli Spaces, ⁋Definition 6](/en/math/stacks/moduli_spaces#def6){: data-lid="fvex6" }. An object of $\mathfrak{M}_{g,n}$ over $\Spec\mathbb{K}$ is a prestable curve of [Definition 1](#def1){: data-lid="9o4n7" }, its stabilizer is the automorphism group $\Aut(C,p_\bullet)$, and as seen earlier, its tangent space is $T^0(C,p_\bullet)$. In addition, a deformation of $(C,p_\bullet)$ over $A$ is given by an identification of the central fiber with $(C,p_\bullet)$ together with a morphism $\Spec A\rightarrow\mathfrak{M}_{g,n}$. That an algebraic stack is smooth at a point is equivalent to the versal base at that point being a power series ring, and since we showed in the previous section that the versal base of each point $[(C,p_\bullet)]$ is a power series ring, $\mathfrak{M}_{g,n}$ is smooth. Therefore, the following holds.

::: Theorem 9
$\mathfrak{M}_{g,n}$ is a smooth algebraic stack of dimension $3g-3+n$.
:::
::: Proof
As we have seen earlier, $\mathfrak{M}_{g,n}$ is a smooth algebraic stack locally of finite type, so it suffices to show the claim on its dimension. Choose a smooth atlas $W\rightarrow\mathfrak{M}_{g,n}$ around the point representing $(C,p_\bullet)$ and a closed point $w\in W$ lying over this point. At $w$, with the relative dimension of $W\rightarrow\mathfrak{M}_{g,n}$ being $r$, the dimension at this point is given by $\dim_wW-r$. ([\[Stacks\] §Algebraic Stacks, ⁋Definition 6](/en/math/stacks/algebraic_stacks#def6){: data-lid="5ac8a" }) Then, for the point representing $(C,p_\bullet)$, given by $\Spec\mathbb{K}\rightarrow\mathfrak{M}_{g,n}$, the fiber $W_0=W\times_{\mathfrak{M}_{g,n}}\Spec\mathbb{K}$ is a smooth scheme of dimension $r$, and at the point corresponding to $w$ there is an exact sequence of tangent spaces:

$$0\rightarrow T^0(C,p_\bullet)\rightarrow T_wW_0\rightarrow T_wW\rightarrow T^1(C,p_\bullet)\rightarrow0$$

Here, $W_0$ can be regarded as a pair of a point of $W$ and an isomorphism identifying the curve over it with $(C, p_\bullet)$. Then the first map $T^0\rightarrow T_wW_0$ corresponds to altering this identification by an infinitesimal automorphism, the second map is given by the differential of $W_0\rightarrow W$ forgetting the identification, and the third map is the first-order deformation obtained by pulling back the family over $W$ along a tangent vector $\Spec\mathbb{K}[\epsilon]\rightarrow W$ of $W$. Therefore, from this exact sequence we obtain

$$\dim_wW-r=\dim T_wW-\dim T_wW_0=\dim T^1(C,p_\bullet)-\dim T^0(C,p_\bullet)=3g-3+n$$

where the last equality follows from [Corollary 6](#cor6){: data-lid="a0i84" }.
:::

In the proof above, $T^0(C,p_\bullet)$ appeared as the infinitesimal automorphism changing the identification, that is, the tangent space of the stabilizer of the point $[(C,p_\bullet)]$; thus, at points where $T^0(C,p_\bullet)\neq0$, the stabilizer is not unramified, and hence $\mathfrak{M}_{g,n}$ is not, in general, a Deligne–Mumford stack. ([\[Stacks\] §Algebraic Stacks, ⁋Definition 6](/en/math/stacks/algebraic_stacks#def6){: data-lid="z8p7i" })

## Smoothing parameter

We have seen earlier that applying [Proposition 7](#prop7){: data-lid="wetkp" }, the versal base can be written as in ($\ast$) as

$$R\cong\mathbb{K}[[\s_1,\ldots,\s_N]]$$

By definition, each coordinate of $R$ represents a direction of deforming the prestable curve, but writing $\s_1,\ldots, \s_N$ in this way was merely chosen to correspond to a basis of $T^1(C,p_\bullet)$ and carried no geometric meaning.

In this section, we examine these directions in more detail. Specifically, at each node $p$, we define a smoothing parameter $\t_p$ representing the degree to which the node is smoothed out, as in [§§Deformations of Semistable Curves](#deformations-of-semistable-curves){: data-lid="9wb6j" }, and show that they are mutually independent in $R$, so that some of the coordinates $\s_1,\ldots, \s_N$ above can be chosen to be these parameters.

At a node $p$, the complete local ring of $C$ is obtained by completing the local model $\mathbb{K}[\x,\y]/(\x\y)$ of a node seen earlier, and is given by

$$\widehat{\mathcal{O}}_{C,p}\cong\mathbb{K}[[\u,\v]]/(\u\v)$$

Here, $\u$ and $\v$ are coordinates on the branches to which the two preimages of the node in the normalization belong, respectively. Then, as in the definition of deformations discussed previously, over a local Artin $\mathbb{K}$-algebra $A$, a deformation of $\widehat{\mathcal{O}}_{C,p}$ is given by a pair of a flat $A$-algebra $B$ and an identification $B\otimes_A\mathbb{K}\cong\widehat{\mathcal{O}}_{C,p}$ on each fiber. At this point, we know by [Proposition 3](#prop3){: data-lid="p1den" } that the space $T_p^1$ of first-order deformations is $1$-dimensional, and just before that proposition we saw that its elements can be written in the form $\u\v=c\epsilon$.

Now, the versal formal deformation of the node is given by the family over $\mathbb{K}[[\t]]$

$$\mathbb{K}[[\u,\v,\t]]/(\u\v-\t)$$

Indeed, when the residue field is $\mathbb{K}$, over a complete local $\mathbb{K}$-algebra $S$, a formal deformation of $\widehat{\mathcal{O}}_{C,p}$ is given, after a suitable choice of coordinates, for some $f\in\mathfrak{m}_S$ in the form $S[[\u,\v]]/(\u\v-f)$. Such a deformation is cut out by a single equation lifting $\u\v$, because when we organize this equation by degrees in $\mathfrak{m}_S$, the parts of the error terms of the form $\u a+\v b$ at each degree are absorbed by changing coordinates to $\u+b$ and $\v+a$, leaving only the constant term. This repeats at each degree the calculation from [\[Schemes\] §Deformation Theory and the Cotangent Complex, ⁋Example 6](/en/math/scheme_theory/deformation_theory#ex6){: data-lid="orqq8" } showing that a first-order deformation $\u\v=\epsilon h$ was determined solely by $h(0)$. That is, any formal deformation is obtained by pulling back the family above along the local homomorphism $\t\mapsto f$, and if $S=\mathbb{K}[\epsilon]$, this homomorphism $\t\mapsto c\epsilon$ is uniquely determined by the element of $T_p^1$ given by $\u\v=c\epsilon$.

Now, restricting the versal formal deformation of $(C,p_\bullet)$ to a neighborhood of the node $p$ yields a formal deformation of $\widehat{\mathcal{O}}_{C,p}$ over $R$, which by the versality above is the pullback of the versal family of the node by some local homomorphism $\mathbb{K}[[\t]]\rightarrow R$. Let us write the element to which this homomorphism sends $\t$ as $\t_p\in\mathfrak{m}_R$. Then the map between tangent spaces

$$T^1(C,p_\bullet)\rightarrow\bigoplus_{p\in\Sing C}T_p^1$$

is the restriction of deformations to local deformations near each node, so it coincides with the right-hand map in [Theorem 5](#thm5){: data-lid="zx1zj" }, and hence is surjective. That this first-order information extends to the entire versal base is the content of the following proposition.

::: Proposition 10
For a prestable curve with $n$ marked points and $d$ nodes $(C,p_\bullet)$, let $R$ be its versal base and let $N=\dim T^1(C,p_\bullet)$. Then for the elements $\t_p$ ($p\in\Sing C$) above and suitable $\s_1,\ldots,\s_{N-d}\in\mathfrak{m}_R$, we have

$$R=\mathbb{K}[[\{\t_p\}_{p\in\Sing C},\s_1,\ldots,\s_{N-d}]]$$

That is, we can choose the smoothing parameters $\t_p$ for each node as part of the coordinates of the versal base, and in these coordinates, the complete local ring of the versal family near the node $p$ is $R[[\u_p,\v_p]]/(\u_p\v_p-\t_p)$.
:::
::: Proof
The map between tangent spaces $T^1(C,p_\bullet)\rightarrow\bigoplus_pT_p^1$ is dual to the map between cotangent spaces, namely the map sending each $\t_p$ to its class in $\mathfrak{m}_R/\mathfrak{m}_R^2$. Therefore, by [Theorem 5](#thm5){: data-lid="38w02" }, surjectivity of this map is equivalent to saying that the classes of the $\t_p$ are linearly independent in $\mathfrak{m}_R/\mathfrak{m}_R^2$. Choose $\s_1,\ldots,\s_{N-d}\in\mathfrak{m}_R$ extending them to a basis. Since $R$ is a power series ring in $N$ variables, elements whose classes form a basis of $\mathfrak{m}_R/\mathfrak{m}_R^2$ give $N$ elements that can be chosen as variables of $R$. The last assertion follows from the fact that the restriction near the node $p$ is the pullback of the local versal family $\mathbb{K}[[\u,\v,\t]]/(\u\v-\t)$ along $\t\mapsto\t_p$, by definition of $\t_p$.
:::

By [Proposition 10](#prop10){: data-lid="s6m44" }, smoothing the nodes acts independently. Near each node $p$, the versal family is of the form $\u_p\v_p=\t_p$, and outside this node it is smooth like $C$, so the locus where the node $p$ remains a node without being smoothed is precisely defined by $\t_p=0$. Thus, the locus of curves having at least one node is given by

$$\prod_{p\in\Sing C}\t_p=0$$

This is the union of distinct coordinate hyperplanes, namely a normal crossings divisor, whose components correspond bijectively to the nodes of $C$. In particular, the locus where all nodes of $C$ remain, namely $\{\t_p=0\}_{p\in\Sing C}$, has tangent space given by the kernel of the right map in [Theorem 5](#thm5){: data-lid="7y4l8" }, namely $H^1(C,\mathcal{T}_{C/\mathbb{K}}(-\Sigma))$, which agrees with our interpretation after [Theorem 5](#thm5){: data-lid="i6j6b" } of this term as deformations preserving the local models of all nodes.

The results so far concern the versal base $R$. To lift this to the stack, we must pass through a smooth atlas $W\rightarrow\mathfrak{M}_{g,n}$. The issue is that a smooth atlas is a scheme that has *unfolded* the isomorphisms remembered by the stack, so there may be additional directions that do not change the isomorphism class of the curve. Therefore, at the point representing $(C,p_\bullet)$, $w\in W$, $\widehat{\mathcal{O}}_{W,w}$ can be larger than $R$, and whether the $\t_p$ remain as coordinates on $W$ must be checked separately. To this end, looking back at the proof of [Theorem 9](#thm9){: data-lid="iq442" }, the family over $W$ is obtained by versality by pulling back the versal formal deformation along some local homomorphism $R\rightarrow\widehat{\mathcal{O}}_{W,w}$, and since $T_wW\rightarrow T^1(C,p_\bullet)$ is surjective in the exact sequence of that proof, by the same argument as in the proof of [Proposition 10](#prop10){: data-lid="ds93e" }, the variables of $R$ become part of the variables of $\widehat{\mathcal{O}}_{W,w}$. That is, the smoothing parameters $\t_p$ are part of the local coordinates even on the smooth atlas, the locus of curves with nodes in $\mathfrak{M}_{g,n}$ is a normal crossings divisor, and the locus of curves with exactly $k$ nodes has codimension $k$.

What we have examined above concerns versal families, so to actually use this, we must be able to perform computations on an arbitrary family. Over a ring with residue field $\mathbb{K}$, namely a complete local $\mathbb{K}$-algebra $S$, suppose we are given a formal deformation of $(C,p_\bullet)$. Then by versality, this is obtained by pulling back the versal formal deformation along a suitable local homomorphism $\phi:R\rightarrow S$, and the complete local ring at the node $p$ is $S[[\u,\v]]/(\u\v-\phi(\t_p))$. In particular, if a prestable curve over a scheme $T$ has fiber over a closed point $t$ equal to $(C,p_\bullet)$, its completion at $t$ is a formal deformation over $\widehat{\mathcal{O}}_{T,t}$, so we can apply the above result with $S=\widehat{\mathcal{O}}_{T,t}$; thus where the node remains and how it is smoothed is determined solely by the pullback of $\t_p$, which is the function $\phi(\t_p)\in\widehat{\mathcal{O}}_{T,t}$.

Now we examine what the normal bundle of the boundary divisor is. By what we have seen above, the boundary consists of the loci given by $\{\t_p=0\}$. Now looking at directions moving away from here, since $\t_p$ is obtained by pulling back the coordinate of the versal base $\mathbb{K}[[\t]]$ of the node, the normal direction to $\{\t_p=0\}$ in the versal base is identified via $T^1(C,p_\bullet)\rightarrow T_p^1$ with $T_p^1$. That is, moving away from the boundary corresponds to the direction of smoothing the node $p$ to first order. Here, expressing the amount of smoothing the node in $\u\v=c\epsilon$ via the number $c$ depends on coordinates, and in fact, changing coordinates to $\u'=\lambda\u$, $\v'=\mu\v$ causes the same deformation to be written as $\u'\v'=\lambda\mu c\epsilon$. This change cancels out exactly with $\partial_{\u}\otimes\partial_{\v}=\lambda\mu(\partial_{\u'}\otimes\partial_{\v'})$, so sending the deformation $\u\v=c\epsilon$ to $c(\partial_{\u}\otimes\partial_{\v})$ yields a coordinate-independent isomorphism

$$T_p^1\cong T_{p'}\widetilde{C}\otimes T_{p''}\widetilde{C}$$

Even for general coordinates $\u'=\u\alpha(\u)$, $\v'=\v\beta(\v)$, by [\[Schemes\] §Deformation Theory and the Cotangent Complex, ⁋Example 6](/en/math/scheme_theory/deformation_theory#ex6){: data-lid="j127z" }, the first-order deformation is determined solely by the constant terms, so only $\lambda=\alpha(0)$ and $\mu=\beta(0)$ remain, and the situation is the same. That is, the magnitude of smoothing the node can be measured by the tensor product of the tangent vectors of the two branches. Since this isomorphism is canonical, the data obtained at each point of the boundary glue together to give the normal line bundle of the boundary component $\{\t_p=0\}$, and since exchanging the two branches in $\u\v=\t_p$ does not change $\t_p$, this does not depend on the ordering of the two branches either.

Finally, let us look at an example of how automorphisms act on the smoothing directions. An automorphism of $(C,p_\bullet)$, $\sigma$, by sending each first-order deformation $(X,\iota)$ to $(X,\sigma\circ\iota)$, acts on $T^1(C,p_\bullet)$, and that $\sigma$ fixes an element of $T^1$ is equivalent to $\sigma$ extending to the deformation represented by that element.

::: Example 11
Consider two elliptic curves $E_1$ and $E_2$ whose origins $p'$ and $p''$ are glued into a single node $p$ to form a genus $2$ curve $C$, and assume that the characteristic of $\mathbb{K}$ is not $2$. Since the tangent sheaf of an elliptic curve is trivial, by [Proposition 4](#prop4){: data-lid="6wm2c" }, $\mathcal{T}_{C/\mathbb{K}}$ is the pushforward of $\mathcal{O}_{E_1}(-p')\oplus\mathcal{O}_{E_2}(-p'')$, where each term satisfies $h^0=0$ and $h^1=1$. Therefore, by [Theorem 5](#thm5){: data-lid="qqbud" }, $T^0(C)=0$, and $T^1(C)$ consists of deforming $(E_1,p')$ and $(E_2,p'')$ respectively, which accounts for $2$ dimensions, and $T_p^1$ smoothing the node, which accounts for $1$ dimension.

Gluing the inversion of $E_1$, $[-1]$, with the identity map on $E_2$, let $\sigma_1$ be the resulting automorphism. Since a deformation of $(E_1,p')$ is a group scheme with origin $p'$, $[-1]$ extends over it, and therefore $\sigma_1$ acts trivially on the former $2$ dimensions. On the other hand, since $[-1]$ acts on $T_{p'}E_1$ by $-1$, $\sigma_1$ acts on $T_p^1\cong T_{p'}E_1\otimes T_{p''}E_2$ by $-1$. That is, $\sigma_1=\operatorname{diag}(1,1,-1)$, and since for $E_2$ the inversion $\sigma_2$ behaves similarly, $\sigma_1\sigma_2$ acts trivially on $T^1(C)$.
:::

In this example, although $T^0(C)=0$, because $\sigma_1$ interchanges the deformation smoothing the node by $\epsilon$ and the deformation smoothing it by $-\epsilon$, different directions in the versal base yield the same curve. In [Theorem 9](#thm9){: data-lid="o3ctj" }, $\mathfrak{M}_{2,0}$ remembers this redundancy via the stabilizer $\Aut(C)$.

---

**References**

**[HKK+]** K. Hori, S. Katz, A. Klemm, R. Pandharipande, R. Thomas, C. Vafa, R. Vakil, E. Zaslow, *Mirror Symmetry*, Clay Mathematics Monographs **1**, AMS, 2003.
