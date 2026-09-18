---
title: "Deformations of Nodal Curves"
description: "We compute the local-to-global deformation sequence for nodal curves, identifying the skyscraper local deformation sheaves that smooth each node and expressing infinitesimal automorphisms via vector fields on the normalization. For projective curves with marked points, this reduces to a short exact sequence from which the expected moduli dimension is derived via Riemann-Roch."
excerpt: "Node smoothing, local deformation sheaves, and dimension counts"

categories: [Math / Gromov-Witten Theory]
permalink: /en/math/gromov-witten_theory/deformations_of_nodal_curves
sidebar: 
    nav: "gromov-witten_theory-en"

date: 2026-09-13
weight: 1
translated_at: 2026-09-14T07:57:47+00:00
translation_source: antigravity-gemini-3.8-flash-high
---
In Gromov--Witten theory, for a target space $X$, we deal with stable maps $\mu: C\rightarrow X$. Here, the domain of $\mu$, denoted $C$, is a nodal curve with additional special points chosen on it. For this reason, this category begins with articles dealing with these nodal curves. More specifically, we will compute how these nodal curves deform and what automorphisms they have. 

A representative, and essentially the unique, example of a nodal curve is $\x\y=0$. This is the union of the two coordinate axes $\{\x=0\}$ and $\{\y=0\}$, and the point where they meet, namely the origin, is called a *node* or a *nodal point*. One of the key properties is that these nodes are singular points. ([\[Algebraic Varieties\] §Tangent Spaces and Smoothness, ⁋Example 7](/en/math/algebraic_varieties/tangent_spaces_and_smoothness#ex7){: data-relation="weak" }) When dealing with a space where such singular points exist, an effective strategy is to consider a deformation that has this space as the central fiber and whose nearby fibers are all smooth. As seen in [\[Schemes\] §Deformation Theory and the Cotangent Complex, ⁋Example 6](/en/math/scheme_theory/deformation_theory#ex6){: data-relation="required" }, starting from $\x\y=0$ and introducing a parameter $\t$ to change it to $\x\y=\t$, we could obtain such a deformation.

More generally, when the only singular points of a curve $C$ are nodes, that is, when every singular point is étale-locally of the form $\x\y=0$, we call it a *nodal curve*. All schemes appearing in this article, including these nodal curves, are assumed to be separated and of finite type over an algebraically closed field $\mathbb{K}$. Intuitively, one may set $\mathbb{K}=\mathbb{C}$, and it is generally harmless to think of most schemes as varieties (except when fat points are needed).

## Prestable Curves and Normalization

First, we define the following. 

::: Definition 1
For a connected projective nodal curve $C$, each of the distinct smooth points $p_1,\ldots,p_n$ is called a *marked point* of $C$. Such a pair $(C,p_1,\ldots,p_n)$ equipped with marked points is called a *prestable curve* with $n$ marked points of genus $g=h^1(C,\mathcal{O}_C)$.
:::

In other words, a prestable curve is merely a nodal curve on which several additional points are chosen so as not to coincide with the nodes. 

Given a nodal curve, there is a way to separate the two branches meeting at the node. This is the normalization defined in the discussion immediately following [\[Schemes\] §Dimension, ⁋Proposition 5](/en/math/scheme_theory/dimension#prop5){: data-relation="weak" } applied to a nodal curve; in this specific context, the *normalization* of $C$ means a smooth projective curve $\widetilde{C}$ together with a finite morphism $\nu:\widetilde{C}\rightarrow C$ that is an isomorphism away from the nodes and has exactly two points lying over each node. 

{% diagram Math/Gromov_Witten_Theory/Deformations_of_Nodal_Curves-1.svg width="7.37em" alt="normalization separates the two branches of a node" %}

As in the diagram above, in the local model at a node, this amounts to replacing $Z(\x\y)$ with the disjoint union of two lines $\mathbb{A}^1_\x$ and $\mathbb{A}^1_\y$, and at the level of rings, this is given by the inclusion

$$A=\mathbb{K}[\x,\y]/(\x\y)\rightarrow \widetilde{A}=\mathbb{K}[\x]\times\mathbb{K}[\y];\qquad f(\x,\y)\mapsto (f(\x,0), f(0,\y))$$

Here, looking at the two expressions $f(\x,0)$ and $f(0,\y)$, we see that their constant terms $c$ must be equal, and conversely, if such a pair $(f(\x),g(\y))$ is given, viewing $f+g-c$ in $\mathbb{K}[\x,\y]/(\x\y)$ gives the preimage under this inclusion. That is, the image of this inclusion is precisely the collection of pairs whose two components have the same constant term. Therefore, if we define $\widetilde{A}\rightarrow \mathbb{K}$ by $(f,g)\mapsto f(0)-g(0)$, the following short exact sequence

$$0 \rightarrow A \rightarrow \widetilde{A}\rightarrow \mathbb{K}\rightarrow 0$$

exists. Sheafifying this, since $\nu$ is an isomorphism outside the nodes and the above computation at $p$ shows that the cokernel is $\kappa(p)=\mathbb{K}$, we obtain

$$0\rightarrow\mathcal{O}_C\rightarrow\nu_\ast\mathcal{O}_{\widetilde C}\rightarrow\kappa(p)\rightarrow0$$

For a general nodal curve, normalization performs this process at all nodes simultaneously, so in this case we obtain the following short exact sequence

$$0\rightarrow\mathcal{O}_C\rightarrow\nu_\ast\mathcal{O}_{\widetilde C}\rightarrow\bigoplus_{p\in\Sing C}\kappa(p)\rightarrow0$$

Now suppose that $C$ has $d$ nodes and $c$ irreducible components, and that the genera of the components of $\widetilde C$ are $g_1,\ldots,g_c$. Since $\nu$ is an affine morphism, by [\[Schemes\] §Sheaf Cohomology of Schemes, ⁋Corollary 4](/en/math/scheme_theory/sheaf_cohomology_of_schemes#cor4){: data-relation="required" }, we have $H^i(C,\nu_\ast\mathcal{G})=H^i(\widetilde C,\mathcal{G})$. Therefore, from the short exact sequence above, we obtain the relation

$$\rchi(C,\nu_\ast\mathcal{O}_{\widetilde C})=\rchi(C,\mathcal{O}_C)+\sum_{p\in\Sing C}\rchi(C,\kappa(p))$$

where, since each $\kappa(p)$ is a skyscraper sheaf whose space of global sections is $\mathbb{K}$ and whose higher cohomology vanishes, the last sum is $d$. Summarizing this yields the following proposition.

::: Proposition 2
With $d$ nodes and $c$ irreducible components, if the normalization of a nodal curve $C$ consists of components of genus $g_1,\ldots, g_c$, then

$$g=\sum_{j=1}^c g_j+d-c+1$$
:::

## Deformation of Semistable Curves

We now examine the deformation theory of nodal curves. At a node $p$, let $T_p^1$ denote the first-order local deformation space. In [\[Schemes\] §Deformation Theory and the Cotangent Complex, ⁋Example 6](/en/math/scheme_theory/deformation_theory#ex6){: data-relation="required"}, we have already computed that for the affine node $Z(\x\y)$, we have $T_p^1\cong\mathbb{K}$ and its generator can be represented by $\x\y-\epsilon$. While every node has this local model, the local deformation of a smooth point is trivial, so we obtain the following.

::: Proposition 3
At each node $p$ of a nodal curve $C$, the space $T_p^1$ of first-order local deformations is $1$-dimensional.
:::

The geometric meaning of this one dimension can be represented by the family $\x\y=\t$.

{% diagram Math/Gromov_Witten_Theory/Deformations_of_Nodal_Curves-2.svg width="51.68em" alt="the local fibers xy=t over the deformation space" %}

Meanwhile, a prestable curve is a nodal curve $C$ equipped with marked points $p_1,\ldots,p_n$ in its smooth locus. Therefore, if we add marked points to the figure above, they move along as the curve deforms, defining sections passing through each $p_i$. Since the marked points cannot coincide with one another, these sections are disjoint; thus, a first-order deformation of a prestable curve is given by the datum consisting of a deformation of the underlying curve together with these marked sections. Here, an isomorphism between such data is an isomorphism of families over $\Spec\mathbb{K}[\epsilon]$ that is the identity on the central fiber and sends each marked section to the corresponding marked section. We denote the $\mathbb{K}$-vector space of such isomorphism classes by $T^1(C,p_\bullet)$. This is the application of $T^1$ from [\[Schemes\] §Deformation Theory and the Cotangent Complex, ⁋Theorem 11](/en/math/scheme_theory/deformation_theory#thm11){: data-relation="required" } to marked curves, and in the same manner, we denote by $T^0(C,p_\bullet)$ the $\mathbb{K}$-vector space of infinitesimal automorphisms preserving all marked sections.

Since these $T^0(C,p_\bullet)$ and $T^1(C,p_\bullet)$ are determined by the additional conditions imposed on the underlying nodal curve by the newly added marked points, it is reasonable to consider these two conditions separately. First, in the case of $T^1$, we have already seen above that $T_p^1$ arises only at the nodes, and by definition marked points are placed only at smooth points, so they do not affect this. That is, $T_p^1$ computed at the nodes remains the same for prestable curves.

The newly added marked points affect $T^0$, where the infinitesimal automorphisms must preserve the marked sections. Locally, on $C$, for a function $f$, an automorphism $\Phi$ must be of the form

$$\Phi(f)=f+\epsilon v(f)$$

and for this to preserve multiplication, $v(fg)=fv(g)+gv(f)$ must hold. That is, $v$ is a derivation of $\mathcal{O}_C$ over $\mathbb{K}$, and conversely, such a derivation always defines an automorphism by the formula above. Now, the part where a prestable curve has infinitesimal automorphisms differing from those of a nodal curve is in the neighborhood of the marked sections as mentioned above, so let us examine this near each marked point $p_i$. Suppose that $p_i$ is locally given by $\z=0$. By [\[Schemes\] §Smooth and Étale Morphisms, ⁋Theorem 7](/en/math/scheme_theory/smooth_and_etale_morphisms#thm7){: data-relation="required" }, $\Omega_{C/\mathbb K}$ is a locally free sheaf of rank $1$ in this neighborhood and $\dd{\z}$ is a local basis, so by the universal property of differentials, any derivation is determined by the image of $\dd{\z}$, $v(\z)$. The corresponding automorphism is given by

$$\z\mapsto\z+\epsilon v(\z)$$

and since we chose $\z=0$ to represent (locally) the marked section, for this to be preserved, $v(\z)$ must vanish at the marked point. That is, we must have $v(\z)\in(\z)$. Now, setting $\Sigma=p_1+\cdots+p_n$, its ideal sheaf is $\mathcal{I}_\Sigma=\mathcal{O}_C(-\Sigma)$, so the sheaf of derivations satisfying this condition is

$$\sHom(\Omega_{C/\mathbb{K}},\mathcal{I}_\Sigma)=\mathcal{T}_{C/\mathbb{K}}\otimes\mathcal{I}_\Sigma=\mathcal{T}_{C/\mathbb{K}}(-\Sigma)$$

and this computes the infinitesimal automorphisms of the marked curve.

What remains now is the computation of $\mathcal{T}_{C/\mathbb{K}}=\sHom(\Omega_{C/\mathbb{K}}, \mathcal{O}_C)$. For this, we choose the local model $R=\mathbb K[\x,\y]/(\x\y)$ and examine derivations on it. Any derivation $v$ is determined by its values on the generators, $a=v(\x)$ and $b=v(\y)$, and to preserve the relation $\x\y=0$ as in the computation of [\[Schemes\] §Deformation Theory and the Cotangent Complex, ⁋Example 6](/en/math/scheme_theory/deformation_theory#ex6){: data-relation="required" }, the condition

$$0=v(\x\y)=\y a+\x b$$

must hold. Here, $\y a=-\x b$ belongs simultaneously to $(\y)$ and $(\x)$, and in $R$, since $(\x)\cap(\y)=0$, we have $\y a=\x b=0$. Furthermore, since $\ann(\y)=(\x)$ and $\ann(\x)=(\y)$, we have $a\in\x\mathbb K[\x]$ and $b\in\y\mathbb K[\y]$.

Geometrically, this reflects the situation where the two branches are separated in the normalization of $R$. That is, if we write the normalization of $R$ as $\widetilde R=\mathbb K[\x]\oplus\mathbb K[\y]$, then the above $a$ and $b$ become derivations on each branch of the normalization, given by functions that vanish at the respective origins.

Now viewing this on the whole nodal curve, in the normalization $\nu:\widetilde C\rightarrow C$, if we denote the two preimages of a node $p$ by $p',p''$, these are derivations vanishing at $p'$ and $p''$ respectively, and since $\nu$ is an isomorphism outside the nodes, these local identifications glue canonically. Therefore, if we denote by $D$ the divisor formed by both preimages of all nodes, this computation is summarized as follows.

::: Proposition 4
For the normalization $\nu:\widetilde{C}\rightarrow C$ of a nodal curve $C$ and the divisor $D$ on $\widetilde{C}$ consisting of the preimages of the nodes,

$$\mathcal{T}_{C/\mathbb{K}}\cong\nu_\ast\bigl(\mathcal{T}_{\widetilde{C}/\mathbb{K}}(-D)\bigr)$$

holds. Similarly, if $\widetilde{\Sigma}$ denotes the preimage of the marked points, then $\mathcal{T}_{C/\mathbb{K}}(-\Sigma)\cong\nu_\ast(\mathcal{T}_{\widetilde{C}/\mathbb{K}}(-D-\widetilde{\Sigma}))$.
:::

Indeed, the second isomorphism is obtained by adding to the first isomorphism the vanishing condition at the marked points. Therefore, taking global sections yields

$$T^0(C,p_\bullet)\cong H^0\bigl(C,\nu_\ast\mathcal T_{\widetilde C/\mathbb K}(-D-\widetilde\Sigma)\bigr)=H^0\bigl(\widetilde C,\mathcal T_{\widetilde C/\mathbb K}(-D-\widetilde\Sigma)\bigr)$$

Here, the last equality holds because $H^0(C,\nu_\ast\mathcal F)=H^0(\widetilde C,\mathcal F)$ by the definition of pushforward. That is, infinitesimal automorphisms are computed as derivations on the normalization that vanish at all preimages of the nodes and at the marked points.

## Dimension Computation

Since the deformation space $T^1(C,p_\bullet)$ represents the directions of motion from a marked prestable curve $(C,p_\bullet)$ to neighboring points, it plays the role of the tangent space when viewed in the space of these prestable curves. Here, we must subtract the degrees of freedom of infinitesimal automorphisms $T^0(C,p_\bullet)$ representing the same point, and our goal is to compute this difference.

To this end, we need a cohomology vanishing result for prestable curves. For this, choose a projective embedding $C\subseteq\mathbb P^N$ and pick a linear subspace $\Lambda=H_1\cap H_2$ of codimension $2$ disjoint from $C$. Then $U_i=C\setminus H_i$ is affine and $U_1\cup U_2=C$, so computing the sheaf cohomology of an arbitrary quasi-coherent sheaf $\mathcal{F}$ on $C$ via Čech cohomology shows that $H^i(C, \mathcal{F})=0$ holds in degree $2$ and higher. Using this, we can show the following.

::: Theorem 5
For a prestable curve $(C, p_\bullet)$ with $n$ marked points, let $\Sing C$ be the set of nodes of $C$. Then the exact sequence

$$0 \rightarrow H^1\bigl(C, \mathcal{T}_{C/\mathbb{K}}(-\Sigma)\bigr) \rightarrow T^1(C, p_\bullet) \rightarrow \bigoplus_{p\in\Sing C}\mathbb{K} \rightarrow 0$$

holds, and $T^0(C, p_\bullet)=H^0(C, \mathcal{T}_{C/\mathbb{K}}(-\Sigma))$.
:::
::: Proof
As computed earlier, the marked points add the twist $(-\Sigma)$ to the automorphism sheaf, but do not change the local deformation space $T_p^1$ of the nodes. Therefore, from [\[Schemes\] §Deformation Theory and the Cotangent Complex, ⁋Theorem 12](/en/math/scheme_theory/deformation_theory#thm12){: data-relation="required" }, we obtain

$$0\rightarrow H^1\bigl(C,\mathcal{T}_{C/\mathbb{K}}(-\Sigma)\bigr)\rightarrow T^1(C,p_\bullet)\rightarrow\bigoplus_{p\in\Sing C}T_p^1\rightarrow H^2\bigl(C,\mathcal{T}_{C/\mathbb{K}}(-\Sigma)\bigr)$$

where the last term is $0$ by the vanishing above. In addition, since $T_p^1\cong\mathbb K$ by [Proposition 3](#prop3){: data-relation="required" }, we obtain the desired short exact sequence. The last claim follows from examining the degree $0$ part of this long exact sequence.
:::

Intuitively, this exact sequence splits the deformations of a prestable curve into two layers. The left term represents the degrees of freedom in deforming the components of the normalization and the positions of the node preimages and marked points on them while preserving the local models of all nodes, and the right term represents the degrees of freedom in choosing which nodes to smooth. Then our key claim is as follows.

::: Corollary 6
For a prestable curve $(C, p_\bullet)$ of genus $g$ with $n$ marked points,

$$\dim T^1(C, p_\bullet)-\dim T^0(C, p_\bullet)=3g-3+n$$

holds.
:::
::: Proof
For convenience of notation, write $\mathcal{H}=\mathcal{T}_{C/\mathbb{K}}(-\Sigma)$, and let the number of nodes of $C$ be $d$. By [Theorem 5](#thm5){: data-relation="required" },

$$\dim T^1=h^1(\mathcal{H})+d,\qquad \dim T^0=h^0(\mathcal{H})$$

so the desired value is $d-\rchi(C, \mathcal{H})$. Now, by [Proposition 4](#prop4){: data-relation="required" } and [\[Schemes\] §Sheaf Cohomology of Schemes, ⁋Corollary 4](/en/math/scheme_theory/sheaf_cohomology_of_schemes#cor4){: data-relation="required" },

$$\rchi(C, \mathcal{H})=\rchi\bigl(\widetilde{C}, \mathcal{T}_{\widetilde{C}/\mathbb{K}}(-D-\widetilde{\Sigma})\bigr).$$

Let us compute the right-hand side of the above equality for each component. Applying [\[Algebraic Varieties\] §The Riemann–Roch Theorem for Curves, ⁋Proposition 3](/en/math/algebraic_varieties/riemann_roch_theorem#prop3){: data-relation="required" } on a genus $g_j$ component $\widetilde C_j$ to the canonical divisor $K_{\widetilde C_j}$, we obtain $\deg\omega_{\widetilde C_j}=2g_j-2$. Thus $\mathcal T_{\widetilde C_j/\mathbb K}\cong\omega_{\widetilde C_j}^\vee$ is a line bundle of degree $2-2g_j$. Letting the number of points of $D+\widetilde\Sigma$ lying on it be $s_j$, the degree of the twisted line bundle is $2-2g_j-s_j$, and by the same proposition,

$$\rchi\bigl(\widetilde{C}_j, \mathcal{T}_{\widetilde{C}_j/\mathbb{K}}(-D-\widetilde{\Sigma})\bigr)=(2-2g_j-s_j)+1-g_j=3-3g_j-s_j.$$

Now, since each node contributes two preimages and each marked point contributes one, we have $\sum_js_j=2d+n$. Therefore, for the $c$ components,

$$\rchi(C, \mathcal{H})=\sum_{j=1}^c(3-3g_j-s_j)=3c-3\sum_jg_j-2d-n.$$

Substituting $\sum_jg_j=g-d+c-1$ given by [Proposition 2](#prop2){: data-relation="required" } into this yields

$$\rchi(C, \mathcal{H})=3c-3(g-d+c-1)-2d-n=-3g+d+3-n,$$

which gives the desired result.
:::

The key point of this computation is that the right-hand side does not depend on $d$ and $c$. Creating one more node adds one local deformation, but the gluing degrees of freedom decrease by the same amount, so the difference between the two dimensions is determined solely by the topological data $g$ and $n$ of the curve. This result plays an important role in the next post when computing the dimension of the moduli of stable maps.

---

**References**

**[HKK+]** K. Hori, S. Katz, A. Klemm, R. Pandharipande, R. Thomas, C. Vafa, R. Vakil, E. Zaslow, *Mirror Symmetry*, Clay Mathematics Monographs **1**, AMS, 2003.
