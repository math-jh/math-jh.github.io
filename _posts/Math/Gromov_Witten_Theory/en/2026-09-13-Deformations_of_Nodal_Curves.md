---
title: "Deformations of Nodal Curves"
description: "We examine the complete computation of the local-to-global exact sequence in deformation theory for nodal curves, confirming that the local deformation sheaf is a one-dimensional skyscraper sheaf at each node whose generator smooths the singularity by perturbing the defining equation. We then show that deformations and infinitesimal automorphisms, even in the presence of marked points, are computed using vector fields on the normalization, leading to a short exact sequence for projective curves where the Riemann-Roch theorem yields a dimension difference of three g minus three plus n."
excerpt: "Node smoothing, the local deformation sheaf, and the count 3g-3+n"

categories: [Math / Gromov-Witten Theory]
permalink: /en/math/gromov-witten_theory/deformations_of_nodal_curves
sidebar: 
    nav: "gromov-witten_theory-en"

date: 2026-09-13
weight: 1
translated_at: 2026-09-19T19:15:05+00:00
translation_source: antigravity-gemini-3.8-flash-high
---
In Gromov--Witten theory, we deal with stable maps into a target space $X$, $\mu: C\rightarrow X$. Here, the domain of $\mu$, $C$, is a nodal curve with additional special points chosen. For this reason, this category begins with posts treating these nodal curves. More specifically, we will compute how these nodal curves deform and what automorphisms they have.

A representative, and essentially unique, example of a nodal curve is $\x\y=0$. This is the union of the two coordinate axes $\{\x=0\}$ and $\{\y=0\}$, and the point where they meet, namely the origin, is called a *node* or *nodal point*. One of the key properties is that these nodes are singular points ([\[Algebraic Varieties\] §Tangent Spaces and Smoothness, ⁋Example 7](/en/math/algebraic_varieties/tangent_spaces_and_smoothness#ex7){: data-lid="qnd3m" data-relation="weak" }). When dealing with a space where singular points exist, an effective strategy is to consider a deformation having it as the central fiber and whose nearby fibers are all smooth. As we saw in [\[Schemes\] §Deformation Theory and the Cotangent Complex, ⁋Example 6](/en/math/scheme_theory/deformation_theory#ex6){: data-lid="nwt79" data-relation="required" }, by taking $\x\y=0$ and introducing a parameter $\t$ to change it to $\x\y=\t$, we were able to obtain such a deformation.

More generally, when the only singular points of a curve $C$ are nodes, that is, when every singular point is étale-locally of the form $\x\y=0$, we call it a *nodal curve*. All schemes appearing in this post, including these nodal curves, are assumed to be separated and of finite type over an algebraically closed field $\mathbb{K}$. Intuitively, setting $\mathbb{K}=\mathbb{C}$ and thinking of most schemes as varieties (except when fat points are needed) is generally harmless.

## Prestable Curves and Normalization

First, we make the following definition.

::: Definition 1
For a connected projective nodal curve $C$, each of the distinct smooth points $p_1,\ldots,p_n$ is called a *marked point* of $C$. A pair $(C,p_1,\ldots,p_n)$ equipped with such marked points is called a *prestable curve* with $n$ marked points and of genus $g=h^1(C,\mathcal{O}_C)$.
:::

That is, a prestable curve is nothing more than a nodal curve on which several additional points are chosen so that they do not overlap with the nodes.

Given a nodal curve, there is a way to separate the two branches joined at each node. This is the application of the normalization defined in the discussion immediately following [\[Schemes\] §Dimension, ⁋Proposition 5](/en/math/scheme_theory/dimension#prop5){: data-lid="o8zf6" data-relation="weak" } to nodal curves; in this concrete setting, the *normalization* of $C$ means a smooth projective curve $\widetilde{C}$ and a finite morphism $\nu:\widetilde{C}\rightarrow C$ that is an isomorphism outside the nodes and has exactly two points lying over each node.

{% diagram Math/Gromov_Witten_Theory/Deformations_of_Nodal_Curves-1.svg width="7.37em" alt="normalization separates the two branches of a node" %}

As in the diagram above, in the local model at a node, this replaces $Z(\x\y)$ with the disjoint union of the two lines $\mathbb{A}^1_\x$ and $\mathbb{A}^1_\y$, and at the ring level, this is given by the inclusion

$$A=\mathbb{K}[\x,\y]/(\x\y)\rightarrow \widetilde{A}=\mathbb{K}[\x]\times\mathbb{K}[\y];\qquad f(\x,\y)\mapsto (f(\x,0), f(0,\y))$$

Here, looking at the two expressions $f(\x,0)$ and $f(0,\y)$, we see that their constant terms $c$ must be equal; conversely, given such a pair $(f(\x),g(\y))$, viewing $f+g-c$ in $\mathbb{K}[\x,\y]/(\x\y)$ gives the preimage under this inclusion. That is, the image of this inclusion is precisely the collection of pairs whose two components have the same constant term. Therefore, defining $\widetilde{A}\rightarrow \mathbb{K}$ by $(f,g)\mapsto f(0)-g(0)$, the short exact sequence

$$0 \rightarrow A \rightarrow \widetilde{A}\rightarrow \mathbb{K}\rightarrow 0$$

exists. Sheafifying this, outside the nodes $\nu$ is an isomorphism, and the above calculation at $p$ shows that the cokernel is $\kappa(p)=\mathbb{K}$, so we obtain

$$0\rightarrow\mathcal{O}_C\rightarrow\nu_\ast\mathcal{O}_{\widetilde C}\rightarrow\kappa(p)\rightarrow0$$

For a general nodal curve, the normalization carries out this process at all nodes simultaneously, and therefore in this case we obtain the following short exact sequence

$$0\rightarrow\mathcal{O}_C\rightarrow\nu_\ast\mathcal{O}_{\widetilde C}\rightarrow\bigoplus_{p\in\Sing C}\kappa(p)\rightarrow0$$

Now suppose that $C$ has $d$ nodes and $c$ irreducible components, and that the genus of each component of $\widetilde C$ is $g_1,\ldots,g_c$. Since $\nu$ is an affine morphism, by [\[Schemes\] §Sheaf Cohomology of Schemes, ⁋Corollary 4](/en/math/scheme_theory/sheaf_cohomology_of_schemes#cor4){: data-lid="prlmv" data-relation="required" } we have $H^i(C,\nu_\ast\mathcal{G})=H^i(\widetilde C,\mathcal{G})$. Therefore, from the short exact sequence above, we obtain

$$\rchi(C,\nu_\ast\mathcal{O}_{\widetilde C})=\rchi(C,\mathcal{O}_C)+\sum_{p\in\Sing C}\rchi(C,\kappa(p))$$

and since each $\kappa(p)$ is a skyscraper sheaf with global sections $\mathbb{K}$ and vanishing higher cohomology, the last sum is $d$. Summarizing this yields the following proposition.

::: Proposition 2
If the normalization of a nodal curve $C$ with $d$ nodes and $c$ irreducible components consists of components of genera $g_1,\ldots, g_c$, then

$$g=\sum_{j=1}^c g_j+d-c+1$$

holds.
:::

## Deformations of Semistable Curves

We now consider the deformation theory of nodal curves. Let $T_p^1$ denote the first-order local deformation space at a node $p$. In [\[Schemes\] §Deformation Theory and the Cotangent Complex, ⁋Example 6](/en/math/scheme_theory/deformation_theory#ex6){: data-relation="required"}, we have already computed that $T_p^1\cong\mathbb{K}$ for the affine node $Z(\x\y)$, and that its generator can be represented by $\x\y-\epsilon$. Since every node has this local model while the local deformation of a smooth point is trivial, we obtain the following.

::: Proposition 3
At each node $p$ of a nodal curve $C$, the space $T_p^1$ of first-order local deformations is $1$-dimensional.
:::

The geometric meaning of this one dimension can be represented by the family $\x\y=\t$.

{% diagram Math/Gromov_Witten_Theory/Deformations_of_Nodal_Curves-2.svg width="51.68em" alt="the local fibers xy=t over the deformation space" %}

On the other hand, a prestable curve is a nodal curve $C$ equipped with marked points $p_1,\ldots,p_n$ on its smooth locus. Therefore, if we add marked points to the picture above, they move together as the curve deforms, defining sections passing through each $p_i$. Since the marked points cannot coincide with one another, these sections are disjoint; thus, a first-order deformation of a prestable curve is given by the data of a deformation of the underlying curve together with these marked sections. Here, an isomorphism between such data is an isomorphism of families over $\Spec\mathbb{K}[\epsilon]$ that restricts to the identity on the central fiber and sends each marked section to the corresponding marked section. We write the $\mathbb{K}$-vector space of these isomorphism classes as $T^1(C,p_\bullet)$. This applies the $T^1$ from [\[Schemes\] §Deformation Theory and the Cotangent Complex, ⁋Theorem 11](/en/math/scheme_theory/deformation_theory#thm11){: data-lid="fqff9" data-relation="required" } to marked curves; in the same way, we write the $\mathbb{K}$-vector space of infinitesimal automorphisms preserving all marked sections as $T^0(C,p_\bullet)$.

Since $T^0(C,p_\bullet)$ and $T^1(C,p_\bullet)$ are determined by the additional conditions imposed by the newly added marked points on the underlying nodal curve, it is reasonable to consider these two conditions separately. First, for $T^1$, we have already seen above that $T_p^1$ arises only at the nodes, and by definition, marked points are placed only at smooth points, so they do not affect this. That is, $T_p^1$ computed at a node remains the same for prestable curves as well.

What the newly added marked points affect is $T^0$, where an infinitesimal automorphism must preserve the marked sections. Locally, on a function $f$ on $C$, an automorphism $\Phi$ must be of the form

$$\Phi(f)=f+\epsilon v(f)$$

and for this to preserve multiplication, $v(fg)=fv(g)+gv(f)$ must hold. That is, $v$ is a derivation of $\mathcal{O}_C$ over $\mathbb{K}$, and conversely, such a derivation always defines an automorphism in the manner above. Now, the part where a prestable curve has different infinitesimal automorphisms from a nodal curve is in the neighborhood of the marked sections as mentioned above, so let us examine this near each marked point $p_i$. Suppose that $p_i$ is locally given by $\z=0$. By [\[Schemes\] §Smooth and Étale Morphisms, ⁋Theorem 7](/en/math/scheme_theory/smooth_and_etale_morphisms#thm7){: data-lid="x011e" data-relation="required" }, $\Omega_{C/\mathbb K}$ is a locally free sheaf of rank $1$ in this neighborhood with $\dd{\z}$ as a local basis; thus, by the universal property of differentials, any derivation is determined by the image of $\dd{\z}$, namely $v(\z)$. The corresponding automorphism is given by

$$\z\mapsto\z+\epsilon v(\z)$$

and since we chose $\z=0$ so that it (locally) represents the marked section, for this to be preserved $v(\z)$ must vanish at the marked point. That is, we must have $v(\z)\in(\z)$. Now, setting $\Sigma=p_1+\cdots+p_n$, its ideal sheaf is $\mathcal{I}_\Sigma=\mathcal{O}_C(-\Sigma)$, so the sheaf of derivations satisfying this condition is

$$\sHom(\Omega_{C/\mathbb{K}},\mathcal{I}_\Sigma)=\mathcal{T}_{C/\mathbb{K}}\otimes\mathcal{I}_\Sigma=\mathcal{T}_{C/\mathbb{K}}(-\Sigma)$$

and this computes the infinitesimal automorphisms of the marked curve.

Now what remains is the calculation of $\mathcal{T}_{C/\mathbb{K}}=\sHom(\Omega_{C/\mathbb{K}}, \mathcal{O}_C)$. For this, we choose the local model $R=\mathbb K[\x,\y]/(\x\y)$ and examine derivations on it. Any derivation $v$ is determined by its values on the generators, $a=v(\x)$ and $b=v(\y)$, and as in the computation of [\[Schemes\] §Deformation Theory and the Cotangent Complex, ⁋Example 6](/en/math/scheme_theory/deformation_theory#ex6){: data-relation="required" }, in order to preserve the relation $\x\y=0$, we must have

$$0=v(\x\y)=\y a+\x b$$

Here, $\y a=-\x b$ belongs simultaneously to $(\y)$ and $(\x)$, and in $R$, since $(\x)\cap(\y)=0$, we have $\y a=\x b=0$. Furthermore, because $\ann(\y)=(\x)$ and $\ann(\x)=(\y)$, we obtain $a\in\x\mathbb K[\x]$ and $b\in\y\mathbb K[\y]$.

Geometrically, this reflects the situation where two branches are separated in the normalization of $R$. That is, if we write the normalization of $R$ as $\widetilde R=\mathbb K[\x]\oplus\mathbb K[\y]$, the above $a$ and $b$ become derivations on each branch of the normalization, and are functions that vanish at the respective origins.

Now, looking at this on the entire nodal curve, in the normalization $\nu:\widetilde C\rightarrow C$, if we let the two preimages of a node $p$ be $p',p''$, these are derivations vanishing at $p'$ and $p''$ respectively, and since $\nu$ is an isomorphism outside the nodes, these local identifications glue canonically. Therefore, if we let $D$ be the divisor collecting the two preimages of all nodes, this computation is summarized as follows.

::: Proposition 4
For a nodal curve $C$, its normalization $\nu:\widetilde{C}\rightarrow C$, and on $\widetilde{C}$ the divisor $D$ consisting of the preimages of the nodes,

$$\mathcal{T}_{C/\mathbb{K}}\cong\nu_\ast\bigl(\mathcal{T}_{\widetilde{C}/\mathbb{K}}(-D)\bigr)$$

holds. Likewise, if $\widetilde{\Sigma}$ denotes the preimage of the marked points, then $\mathcal{T}_{C/\mathbb{K}}(-\Sigma)\cong\nu_\ast(\mathcal{T}_{\widetilde{C}/\mathbb{K}}(-D-\widetilde{\Sigma}))$.
:::

In fact, the second isomorphism is obtained by adding the vanishing condition at the marked points to the first isomorphism. Therefore, taking global sections yields

$$T^0(C,p_\bullet)\cong H^0\bigl(C,\nu_\ast\mathcal T_{\widetilde C/\mathbb K}(-D-\widetilde\Sigma)\bigr)=H^0\bigl(\widetilde C,\mathcal T_{\widetilde C/\mathbb K}(-D-\widetilde\Sigma)\bigr)$$

where the last equality follows from $H^0(C,\nu_\ast\mathcal F)=H^0(\widetilde C,\mathcal F)$ by the definition of pushforward. That is, infinitesimal automorphisms are computed as derivations on the normalization that vanish at all preimages of the nodes and at the marked points.

Under the standard deformation-theoretic interpretation, this calculation can be viewed as finding the tangent space to the automorphism group of a nodal curve, or more generally a prestable curve. ([\[Schemes\] §Deformation Theory and the Cotangent Complex, ⁋Theorem 5](/en/math/scheme_theory/deformation_theory#thm5){: data-lid="u7v2l" data-relation="required" }) Letting this automorphism group be $G=\Aut(C,p_\bullet)$ and its identity element be $e$, the elements of the tangent space $T_eG$ at the identity are the $\mathbb K[\epsilon]$-valued points $\Spec\mathbb K[\epsilon]\rightarrow G$ whose closed point maps to the identity. ([\[Schemes\] §From Varieties to Schemes, ⁋Example 4](/en/math/scheme_theory/from_varieties_to_schemes#ex4){: data-lid="jhbqv" data-relation="required" }) Intuitively, this can be thought of as a family of automorphisms that restrict to the identity map on the central fiber, from which we obtain the identification 

$$T_eG\cong T^0(C,p_\bullet)\cong H^0\bigl(\widetilde C,\mathcal T_{\widetilde C/\mathbb K}(-D-\widetilde\Sigma)\bigr)$$

From the calculation above, we know that any automorphism is locally written in the form $f\mapsto f+\epsilon v(f)$, and since the derivation $v$ represents a vector field on the smooth curve $\widetilde C$, this expression can be interpreted as saying that the directions in which automorphisms move infinitesimally from the identity appear as vector fields on the normalization.

## Dimension Calculation

Since the deformation space $T^1(C,p_\bullet)$ represents the directions of moving from the single point given by the marked prestable curve $(C,p_\bullet)$ to neighboring points, it plays the role of a tangent space when viewed in the space parameterizing these prestable curves. Here, the degrees of freedom of infinitesimal automorphisms $T^0(C,p_\bullet)$ representing the same point must be subtracted, and our goal is to compute this difference. 

To this end, we need a cohomology vanishing result for prestable curves; for this, take a projective embedding $C\subseteq\mathbb P^N$, and disjoint from $C$, choose a codimension $2$ linear subspace $\Lambda=H_1\cap H_2$. Then $U_i=C\setminus H_i$ is affine and $U_1\cup U_2=C$, so computing the sheaf cohomology on $C$ of any quasi-coherent sheaf $\mathcal{F}$ via Čech cohomology shows that $H^i(C, \mathcal{F})=0$ holds in degree $2$ and above. Using this, we can show the following. 

::: Theorem 5
For an $n$-pointed prestable curve $(C, p_\bullet)$, letting the set of nodes of $C$ be $\Sing C$, the exact sequence

$$0 \rightarrow H^1\bigl(C, \mathcal{T}_{C/\mathbb{K}}(-\Sigma)\bigr) \rightarrow T^1(C, p_\bullet) \rightarrow \bigoplus_{p\in\Sing C}\mathbb{K} \rightarrow 0$$

holds, and moreover $T^0(C, p_\bullet)=H^0(C, \mathcal{T}_{C/\mathbb{K}}(-\Sigma))$.
:::
::: Proof
As computed earlier, the marked points add the twist $(-\Sigma)$ to the automorphism sheaf, but do not change the local deformation spaces $T_p^1$ of the nodes. Therefore, from [\[Schemes\] §Deformation Theory and the Cotangent Complex, ⁋Theorem 12](/en/math/scheme_theory/deformation_theory#thm12){: data-lid="940xu" data-relation="required" }, we obtain

$$0\rightarrow H^1\bigl(C,\mathcal{T}_{C/\mathbb{K}}(-\Sigma)\bigr)\rightarrow T^1(C,p_\bullet)\rightarrow\bigoplus_{p\in\Sing C}T_p^1\rightarrow H^2\bigl(C,\mathcal{T}_{C/\mathbb{K}}(-\Sigma)\bigr)$$

where the last term is $0$ by the vanishing above. In addition, since $T_p^1\cong\mathbb K$ by [Proposition 3](#prop3){: data-lid="8ouk8" data-relation="required" }, we obtain the desired short exact sequence. The last assertion follows by looking at the degree $0$ part of this long exact sequence.
:::

Intuitively, this exact sequence splits the deformations of a prestable curve into two layers. The left term corresponds to the degrees of freedom in deforming the components of the normalization and the positions of the node preimages and marked points on them while preserving the local models of all nodes, whereas the right term corresponds to the degrees of freedom in choosing which nodes to smooth. Then our key claim is as follows.

::: Corollary 6
For a prestable curve $(C, p_\bullet)$ of genus $g$ with $n$ marked points,

$$\dim T^1(C, p_\bullet)-\dim T^0(C, p_\bullet)=3g-3+n$$

holds.
:::
::: Proof
For convenience of notation, we write $\mathcal{H}=\mathcal{T}_{C/\mathbb{K}}(-\Sigma)$, and let $d$ be the number of nodes of $C$. Then by [Theorem 5](#thm5){: data-lid="c3l1e" data-relation="required" },

$$\dim T^1=h^1(\mathcal{H})+d,\qquad \dim T^0=h^0(\mathcal{H})$$

so the desired value is $d-\rchi(C, \mathcal{H})$. Now by [Proposition 4](#prop4){: data-lid="arwum" data-relation="required" } and [\[Schemes\] §Sheaf Cohomology of Schemes, ⁋Corollary 4](/en/math/scheme_theory/sheaf_cohomology_of_schemes#cor4){: data-lid="tpsgt" data-relation="required" },

$$\rchi(C, \mathcal{H})=\rchi\bigl(\widetilde{C}, \mathcal{T}_{\widetilde{C}/\mathbb{K}}(-D-\widetilde{\Sigma})\bigr)$$

holds.

Let us compute the right-hand side of the above equality component by component. Applying [\[Algebraic Varieties\] §The Riemann–Roch Theorem for Curves, ⁋Proposition 3](/en/math/algebraic_varieties/riemann_roch_theorem#prop3){: data-lid="khrzv" data-relation="required" } to the canonical divisor $K_{\widetilde C_j}$ of the component $\widetilde C_j$ of genus $g_j$, we obtain $\deg\omega_{\widetilde C_j}=2g_j-2$. Therefore, $\mathcal T_{\widetilde C_j/\mathbb K}\cong\omega_{\widetilde C_j}^\vee$ is a line bundle of degree $2-2g_j$. If $s_j$ denotes the number of points of $D+\widetilde\Sigma$ lying on it, the degree of the twisted line bundle is $2-2g_j-s_j$, and by the same proposition,

$$\rchi\bigl(\widetilde{C}_j, \mathcal{T}_{\widetilde{C}_j/\mathbb{K}}(-D-\widetilde{\Sigma})\bigr)=(2-2g_j-s_j)+1-g_j=3-3g_j-s_j$$

holds. Now since each node gives two preimages and each marked point gives one, we have $\sum_js_j=2d+n$, and hence for the $c$ components,

$$\rchi(C, \mathcal{H})=\sum_{j=1}^c(3-3g_j-s_j)=3c-3\sum_jg_j-2d-n$$

holds. Substituting $\sum_jg_j=g-d+c-1$ given by [Proposition 2](#prop2){: data-lid="b8s52" data-relation="required" } into this,

$$\rchi(C, \mathcal{H})=3c-3(g-d+c-1)-2d-n=-3g+d+3-n$$

we obtain the desired result.
:::

The key point of this calculation is that the right-hand side does not depend on $d$ and $c$. Creating one more node increases the local deformations by one, but the degrees of freedom for gluing decrease by the same amount, so the difference between the two dimensions is determined solely by the topological data $g$ and $n$ of the curve. This result plays an important role in the next post when computing the dimension of the moduli of stable maps.

---

**References**

**[HKK+]** K. Hori, S. Katz, A. Klemm, R. Pandharipande, R. Thomas, C. Vafa, R. Vakil, E. Zaslow, *Mirror Symmetry*, Clay Mathematics Monographs **1**, AMS, 2003.
