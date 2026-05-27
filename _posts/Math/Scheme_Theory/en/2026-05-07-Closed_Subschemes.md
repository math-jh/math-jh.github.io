---
title: "Closed Subschemes"
excerpt: "Closed subschemes and vanishing schemes defined by ideal sheaves"

categories: [Math / Scheme Theory]
permalink: /en/math/scheme_theory/closed_subschemes
header:
    overlay_image: /assets/images/Math/Algebraic_Varieties/Closed_subschemes.png
    overlay_filter: 0.5
sidebar: 
    nav: "scheme_theory-en"

date: 2025-02-18
last_modified_at: 2025-02-18
weight: 12
translated_at: 2026-05-22T15:00:01+00:00
translation_source: kimi-cli
---
In [§Schemes, ⁋Lemma 2](/en/math/scheme_theory/schemes#lem2) we saw that, for an affine scheme $$\Spec A$$, any element $$f$$ defines an open affine subscheme $$D(f)\cong \Spec A_f$$; in particular, to compare the two structure sheaves, we applied [\[Topology\] §Sheaves, ⁋Lemma 11](/en/math/topology/sheaves#lem11) to the morphism

$$(\Spec\epsilon)^\sharp: \mathscr{O}_{\Spec A} \rightarrow (\Spec \epsilon)_\ast \mathscr{O}_{\Spec A_f}$$

obtained from $$\epsilon: A \rightarrow A_f$$ to get

$$(\Spec\epsilon \vert^{D(f)})^\sharp: \mathscr{O}_{D(f)} \rightarrow (\Spec\epsilon\vert^{D(f)})_\ast \mathscr{O}_{\Spec A_f}$$

and, from the fact that $$\Spec A_f$$ is an open subset of $$\Spec A$$, we could conclude that this is an isomorphism.

On the other hand, by the second result of [§Spectrums, ⁋Proposition 9](/en/math/scheme_theory/spectrums#prop9), given an affine scheme $$\Spec A$$ and an ideal $$\mathfrak{a}$$ of $$A$$, the $$\Spec$$ functor gives

$$\Spec\pi: \Spec A/\mathfrak{a}\rightarrow \Spec A$$

and we know that $$\Spec\pi$$ is injective and its image is the closed set $$Z(\mathfrak{a})$$. In this case as well, considering the canonical decomposition

$$\Spec A/\mathfrak{a}\overset{\Spec\pi\vert^{Z(\mathfrak{a})}}{\longrightarrow} Z(\mathfrak{a}) \overset{\iota}{\longrightarrow}\Spec A$$

just as above, from

$$(\Spec\pi)^\sharp: \mathscr{O}_{\Spec A} \rightarrow (\Spec\pi)_\ast \mathscr{O}_{\Spec A/\mathfrak{a}}$$

we can construct the morphism of sheaves on $$Z(\mathfrak{a})$$

$$\iota^{-1} \mathscr{O}_{\Spec A} \rightarrow (\Spec\pi\vert^{Z(\mathfrak{a})})_\ast \mathscr{O}_{\Spec A/\mathfrak{a}}$$

but we have not defined a scheme structure on $$Z(\mathfrak{a})$$; hence we do not know the relationship between $$\iota^{-1}\mathscr{O}_{\Spec A}$$ and $$\mathscr{O}_{Z(\mathfrak{a})}$$, and there is no guarantee that this is an isomorphism. In fact, it is much more likely not to be an isomorphism, because $$\iota^{-1}\mathscr{O}_{\Spec A}$$ is defined using only the topological data of the closed set $$Z(\mathfrak{a})$$ inside the structure sheaf of $$\Spec A$$, whereas $$(\Spec\pi)_\ast\mathscr{O}_{\Spec A/\mathfrak{a}}$$ also carries the algebraic information of the ring $$A/\mathfrak{a}$$. 


<div class="example" markdown="1">

<ins id="ex1">**Example 1**</ins> For example, fix a field $$\mathbb{K}$$ and consider the affine $$1$$-line $$\mathbb{A}_\mathbb{K}^1=\Spec \mathbb{K}[\x]$$. Then we have the canonical surjections

$$\pi_1:\mathbb{K}[\x] \rightarrow \mathbb{K}[\x]/(\x)\cong \mathbb{K},\qquad \pi_2:\mathbb{K}[\x] \rightarrow \mathbb{K}[\x]/(\x^2)$$

where concretely $$\pi_1$$ and $$\pi_2$$ are defined by $$\x\mapsto 0+(\x)$$ and $$\x\mapsto \x+(\x^2)$$, respectively. 

Since $$\mathbb{K}[\x]/(\x)\cong \mathbb{K}$$, $$\Spec \mathbb{K}[\x]/(\x)$$ has only the single point $$(0)$$. Similarly, $$\Spec \mathbb{K}[\x]/(\x^2)$$ also has only one point. This is because there is a one-to-one correspondence between the prime ideals of $$\mathbb{K}[\x]/(\x^2)$$ and the prime ideals of $$\mathbb{K}[\x]$$ containing $$\x^2$$; since $$\mathbb{K}[\x]$$ is a principal ideal domain, writing a prime ideal of $$\mathbb{K}[\x]$$ as $$(p(\x))$$, for this ideal to contain $$\x^2$$ we must have $$p(\x)$$ divide $$\x^2$$, which forces $$p(\x)=\x$$. 

Thus, considering the scheme morphisms they define,

$$\Spec\pi_1:\Spec \mathbb{K}[\x]/(\x) \rightarrow \Spec \mathbb{K}[\x],\qquad \Spec\pi_2:\Spec \mathbb{K}[\x]/(\x^2) \rightarrow \Spec \mathbb{K}[\x]$$

we see that as a continuous map, $$\Spec\pi_1$$ sends the unique point $$(0)$$ of $$\Spec \mathbb{K}[\x]/(\x)$$ to the point $$(\x)$$ of $$\Spec \mathbb{K}[\x]$$, and $$\Spec\pi_2$$ sends the unique point $$(\x)$$ of $$\Spec \mathbb{K}[\x]/(\x^2)$$ to the point $$(\x)$$ of $$\Spec \mathbb{K}[\x]$$. That is, as continuous maps these define the same function, but of course $$\Spec \mathbb{K}[\x]/(\x)$$ and $$\mathbb{K}[\x]/(\x^2)$$ are not isomorphic as schemes. 

</div>

Naturally, the structure sheaf we want is of the form $$(\Spec\pi)_\ast \mathscr{O}_{\Spec A/\mathfrak{a}}$$, which carries the algebraic information; what relationship this has with $$\iota^{-1}\mathscr{O}_{\Spec A}$$ will be examined at the end of this article.

## Closed Subschemes

As we saw above, our model for closed subschemes is the canonical projection $$\pi: A \rightarrow A/\mathfrak{a}$$ and the scheme morphism it induces,

$$(\Spec \pi, (\Spec\pi)^\sharp): \Spec A/\mathfrak{a} \rightarrow\Spec A$$

Here $$\Spec\pi$$ is an injective continuous map giving a homeomorphism between $$\Spec A/\mathfrak{a}$$ and a closed set of $$\Spec A$$, and $$\Spec\pi^\sharp: \mathscr{O}_{\Spec A} \rightarrow (\Spec\pi)_\ast \mathscr{O}_{\Spec A/\mathfrak{a}}$$ is obtained from [§Affine Schemes, ⁋Proposition 9](/en/math/scheme_theory/affine_schemes#prop9).

The most important property of the ring homomorphism $$\pi: A \rightarrow A/\mathfrak{a}$$ is that $$\pi$$ is surjective. Indeed, for any surjective ring homomorphism $$\phi: A \rightarrow B$$, by the first isomorphism theorem

$$B=\im\phi\cong A/\ker\phi$$

so this property characterizes $$\pi$$ exactly. Furthermore, by [\[Commutative Algebra\] §Properties of Localization, ⁋Proposition 4](/en/math/commutative_algebra/properties_of_localization#prop4), the surjectivity of $$\pi$$ can be checked by looking at whether the localization $$\pi_\mathfrak{p}: A_\mathfrak{p} \rightarrow (A/\mathfrak{a})_{\mathfrak{p}}$$ at each prime ideal $$\mathfrak{p}$$ is surjective. Geometrically, this is the same as looking at the stalk at each point $$\mathfrak{p}$$ of the affine scheme $$\Spec A$$, and so by [\[Topology\] §Sheaves, ⁋Proposition 14](/en/math/topology/sheaves#prop14) it is equivalent to $$(\Spec\pi)^\sharp$$ being surjective. 

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> A scheme morphism $$\iota: Z \rightarrow X$$ is a *closed embedding* if $$\iota$$ is a homeomorphism (as a continuous map) between $$Z$$ and a closed set of $$X$$, and the sheaf morphism $$\iota^\sharp: \mathscr{O}_X \rightarrow \iota_\ast \mathscr{O}_Z$$ is surjective.

</div>

The condition on the continuous map $$\iota$$ is self-evident, and the intuition for $$\iota^\sharp$$ also has a geometric interpretation: the functions on $$Z$$ — more precisely, the functions on $$\iota(Z)$$ — must all be obtained by restricting functions on $$X$$ to $$Z$$. Conversely, given an arbitrary function on $$Z$$, it must be possible to extend it to a function on $$X$$. On the other hand, if $$\iota$$ is an open embedding, then $$\iota^\sharp$$ must be an isomorphism. 

This definition is natural, but it differs slightly in flavor from the properties of scheme morphisms we defined in previous articles. We therefore use (without proof) the following equivalent definition. 

<div class="proposition" markdown="1">

<ins id="prop3">**Proposition 3**</ins> For a scheme morphism $$\varphi: X \rightarrow Y$$, the following two conditions are equivalent.

1. $$\varphi$$ is a closed embedding.
2. $$\varphi$$ is an affine morphism, and for every affine open subset $$V\cong \Spec B$$ of $$Y$$, with preimage $$\varphi^{-1}(V)\cong \Spec A$$, the map $$B \rightarrow A$$ is surjective. 

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

[The equivalence of two definitions of closed subscheme, Vakil's Ex 8.1.K](https://math.stackexchange.com/questions/1720902/the-equivalence-of-two-definitions-of-closed-subscheme-vakils-ex-8-1-k), Stack Exchange.

</details>

Then any closed embedding can locally be regarded as coming from some $$\pi: A \rightarrow A/\mathfrak{a}$$, as we saw above. In particular, if $$Y$$ is an affine scheme $$\Spec B$$, then by the equivalence above, any closed embedding $$\varphi: X \rightarrow Y$$ into $$Y$$ corresponds exactly to some $$B \rightarrow B/\mathfrak{b}$$. 

## Properties of Closed Embeddings

Once we accept [Proposition 3](#prop3), we know that any closed embedding is affine-local on the target, and that closed embeddings are closed under composition. Moreover, the following holds.

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4**</ins> Any closed embedding is a finite morphism.

</div>

This is obvious from the definition, and in light of the geometric intuition for (quasi-)finite morphisms developed in [§Properties of Scheme Morphisms, ⁋Example 15](/en/math/scheme_theory/properties_of_scheme_morphisms#ex15), it is clear that at least a closed embedding must always be quasi-finite, and one can further give a geometric interpretation of why it is also finite. 

<div class="definition" markdown="1">

<ins id="def5">**Definition 5**</ins> For any scheme $$Z$$, a subsheaf $$\mathscr{I}$$ of $$\mathscr{O}_Z$$ is called an *ideal sheaf* of $$Z$$. In particular, for a closed embedding $$\iota: Z \rightarrow X$$, the subsheaf $$\ker\iota^\sharp$$ of $$\mathscr{O}_X$$ is called the ideal sheaf defined by $$\iota$$, denoted $$\mathscr{I}_{Z/X}$$. 

</div>

That is, we have the exact sequence

$$0 \rightarrow \mathscr{I}_{Z/X} \rightarrow \mathscr{O}_X \rightarrow \iota_\ast \mathscr{O}_Z \rightarrow 0$$

Therefore, on any affine open subset $$U=\Spec A$$ of $$X$$,

$$0 \rightarrow \mathscr{I}_{Z/X}(U) \rightarrow \mathscr{O}_X(U)\cong A \rightarrow \iota_\ast \mathscr{O}_Z(U) \rightarrow 0$$

so $$\mathscr{I}_{Z/X}(U)$$ is an ideal of $$A$$, which justifies this name. 

Right after [Proposition 3](#prop3) we saw that closed subschemes of an affine scheme $$Y=\Spec B$$ correspond exactly to ideals of $$B$$. Since any scheme is built by gluing affine schemes, ideals are defined on each affine scheme, and if they satisfy a suitable gluing condition, they define a closed subscheme of the original scheme. 

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6**</ins> Suppose that for each affine open subset $$\Spec A$$ of a scheme $$X$$, an ideal $$\mathscr{I}(A)\subseteq A$$ is given. If for every $$f\in A$$ the map $$A \rightarrow A_f$$ induces an isomorphism $$\mathscr{I}(A_f)\cong \mathscr{I}(A)_f$$, then this data induces a unique closed subscheme $$Z\hookrightarrow X$$. 

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First cover $$X$$ by affine open subsets $$\{\Spec A_i\}$$. Then what we need to show is that for any $$i,j$$, the closed subscheme of $$\Spec A_i$$ defined by the ideal $$\mathscr{I}(A_i)$$ and the closed subscheme of $$\Spec A_j$$ defined by the ideal $$\mathscr{I}(A_j)$$ define the same closed subscheme on the intersection of $$\Spec A_i$$ and $$\Spec A_j$$. 


First, by [§Topology of Schemes, ⁋Lemma 11](/en/math/scheme_theory/topology_of_schemes) we can cover the intersection of $$\Spec A_i$$ and $$\Spec A_j$$ by principal open subsets 

$$\Spec (A_i)_{f_i}\cong\Spec (A_j)_{f_j}$$

Restricting the closed subscheme of $$\Spec A_i$$ defined by $$\mathscr{I}(A_i)$$ to $$D(f_i)\cong\Spec (A_i)_{f_i}$$ gives $$\mathscr{I}(A_i)_{f_i}$$, which by the assumption is isomorphic to $$\mathscr{I}((A_i)_{f_i})$$, and this equals $$\mathscr{I}((A_j)_{f_j})$$, so we can glue these together to form a closed subscheme $$Z$$. 

</details>

Now let an arbitrary scheme $$X$$ and a global section $$s\in \Gamma(X, \mathscr{O}_X)$$ be given. Then for each affine cover $$U\cong\Spec A$$, $$s\vert_U$$ defines an ideal $$\mathscr{I}(A)=(s\vert_U)$$ of $$A$$, and it is obvious that the $$\mathscr{I}(A)$$ defined in this way satisfies the conditions of [Proposition 6](#prop6).

<div class="definition" markdown="1">

<ins id="def7">**Definition 7**</ins> For a scheme $$X$$ and a global section $$s\in \Gamma(X, \mathscr{O}_X)$$ of $$X$$, the scheme $$Z(s)$$ defined as above is called the *vanishing scheme* of $$s$$.

</div>

More generally, it is obvious how to define $$Z(S)$$ for a set $$S$$ of global sections. Hence in particular, when $$X=\Spec A$$ and $$S=\mathfrak{a}$$ is an ideal of $$A$$, it is obvious how to define $$Z(\mathfrak{a})$$: it is obtained by transferring the structure sheaf of the affine scheme $$\Spec A/\mathfrak{a}$$ to the closed set $$Z(\mathfrak{a})$$ via $$\Spec\pi$$. Henceforth, we always regard $$Z(\mathfrak{a})$$ as carrying this scheme structure.

<div class="definition" markdown="1">

<ins id="def8">**Definition 8**</ins> A scheme morphism $$\varphi: X \rightarrow Y$$ is a *locally closed embedding* if there exists some open subscheme $$\iota:Z\hookrightarrow Y$$ of $$Y$$ such that, through the canonical decomposition

$$X\overset{\varphi\vert^Z}{\longrightarrow}Z\overset{\iota}{\longrightarrow} Y$$

$$\varphi\vert^Z$$ is a closed embedding. 

</div>

Then by [Proposition 4](#prop4), we know that any locally closed embedding is always locally of finite type. 

## Images of Scheme Morphisms

We now define the image of a scheme morphism. Naturally, given an arbitrary scheme morphism $$\varphi: X \rightarrow Y$$, we want its image $$\im\varphi$$ to also carry a scheme structure. However, as a subset of the topological space $$Y$$, $$\im\varphi$$ may be neither open nor closed, so defining a structure sheaf on $$\im\varphi$$ using the structure sheaf of $$Y$$ seems out of reach. 

The solution is to define the *scheme-theoretic image* of $$\varphi$$ as the smallest closed subscheme containing the image of $$\varphi$$. To do this, we must first examine what it means for one closed subscheme of $$X$$ to be smaller than another.

<div class="proposition" markdown="1">

<ins id="lem9">**Lemma 9**</ins> Let two closed embeddings $$\iota_1: Z_1 \rightarrow X$$, $$\iota_2: Z_2 \rightarrow X$$ be given. Then the existence of some scheme morphism $$\varphi: Z_1 \rightarrow Z_2$$ satisfying $$\iota_1=\iota_2\circ\varphi$$ is equivalent to $$\mathscr{I}_{Z_2/X}\subseteq \mathscr{I}_{Z_1/X}$$. In this case $$\varphi$$ is a closed embedding. 

</div>

This is because, viewed on an affine open subset $$\Spec A$$, the two closed embeddings correspond respectively to

$$A \rightarrow A/\mathscr{I}_{Z_1/X}(A),\qquad A \rightarrow A/\mathscr{I}_{Z_2/X}(A)$$

and the existence of $$\varphi$$ satisfying the above condition is the same as requiring the ring homomorphism $$A \rightarrow A/ \mathscr{I}_{Z_1/X}(A)$$ to factor through $$A \rightarrow A/ \mathscr{I}_{Z_2/X}(A)$$, which in turn is equivalent to $$\mathscr{I}_{Z_2/X}(A)\subseteq \mathscr{I}_{Z_1/X}(A)$$. 

For two closed subschemes $$Z_1, Z_2$$ of a scheme $$X$$, we regard $$Z_1$$ as a *smaller* closed subscheme than $$Z_2$$ if there exists a closed embedding $$\varphi:Z_1 \rightarrow Z_2$$. 

<div class="definition" markdown="1">

<ins id="def10">**Definition 10**</ins> Let an arbitrary scheme morphism $$\varphi: X \rightarrow Y$$ be given. We say that the image of $$\varphi$$ is *contained* in a closed subscheme $$\iota: Z \rightarrow Y$$ if the composition

$$\mathscr{I}_{Z/Y} \rightarrow \mathscr{O}_Y \rightarrow \varphi_\ast \mathscr{O}_X$$

is $$0$$. In this case, the smallest closed subscheme of $$Y$$ containing the image of $$\varphi$$ is called the *scheme-theoretic image* of $$\varphi$$.

</div>

If in the formula above $$Y$$ is an affine scheme $$\Spec B$$, then a closed subscheme of $$Y$$ is completely determined by an ideal $$\mathfrak{b}$$ of $$B$$. Therefore, in this case the scheme-theoretic image of $$Y$$ is the closed subscheme of $$Y$$ defined by the kernel of $$\mathscr{O}_Y \rightarrow \varphi_\ast \mathscr{O}_X$$. In the more special case where $$X$$ is also an affine scheme, $$\mathscr{O}_Y \rightarrow \varphi_\ast \mathscr{O}_X$$ comes from a ring homomorphism $$\phi$$, so we can carry out an explicit computation.

<div class="example" markdown="1">

<ins id="ex11">**Example 11**</ins> Let us look at a slight variant of the closed embedding example $$\Spec\pi: \Spec \mathbb{K}[\x]/(\x^2) \rightarrow \Spec \mathbb{K}[\x]$$ from [Example 1](#ex1). In this example, for clarity, we write $$\mathbb{K}[\x]/(\x^2)$$ as $$\mathbb{K}[\epsilon]/(\epsilon^2)$$. 

By [\[Algebraic Structures\] §Algebras, ⁋Proposition 8](/en/math/algebraic_structures/algebras#prop8), we know that a $$\mathbb{K}$$-algebra homomorphism $$\phi:\mathbb{K}[\x_1,\ldots, \x_n] \rightarrow \mathbb{K}[\epsilon]/(\epsilon^2)$$ is completely determined by the values of $$\x_i$$. So let $$\phi(\x_i)=a_i+b_i\epsilon$$. If there is some nonzero $$b_i$$, one can show that $$\phi$$ is surjective; thus $$\Spec\phi$$ is a closed embedding and the scheme-theoretic image of $$\Spec\phi$$ is the closed subscheme defined by $$\Spec\phi$$ itself. Writing this out concretely, $$\Spec\phi$$ sends the unique prime ideal $$(\epsilon)$$ of $$\mathbb{K}[\epsilon]/(\epsilon^2)$$ to the prime ideal of $$\Spec \mathbb{K}[\x_1,\ldots, \x_n]$$

$$(\Spec\phi)(\epsilon)=\phi^{-1}(\epsilon)=\left(\frac{\x_1}{b_1}-\frac{a_1}{b_1},\ldots \frac{\x_n}{b_n}-\frac{a_n}{b_n}\right)=(\x_1-a_1,\ldots, \x_n-a_n)$$

That is, as a continuous map, $$\Spec\phi$$ sends the one-point space $$\Spec \mathbb{K}[\epsilon]/(\epsilon^2)$$ to the single point $$(a_1,\ldots, a_n)$$ of $$\mathbb{A}^n$$.

Geometrically, $$\Spec\phi$$ corresponds to the tangent vector $$(b_1,\ldots, b_n)$$ at the point $$(a_1,\ldots, a_n)$$ of $$\mathbb{A}^n$$. This can be verified by noting that the directional derivative of any function $$f\in \mathbb{K}[\x_1,\ldots, \x_n]$$ on $$\mathbb{A}^n$$ at the point $$(a_1,\ldots, a_n)$$ in the direction of the vector $$(b_1,\ldots, b_n)$$ is given exactly by $$\phi(f)$$. More generally, replacing $$\Spec \mathbb{K}[\epsilon]/(\epsilon^2)$$ with $$\Spec \mathbb{K}[\epsilon]/(\epsilon^k)$$, we can see derivatives up to order $$k-1$$. 

</div>

In the example above we assumed that $$X$$ is an affine scheme, but $$\varphi^\sharp:\mathscr{O}_Y \rightarrow \varphi_\ast \mathscr{O}_X$$ is in any case data contained in the scheme morphism $$\varphi$$, so there is nothing new there. The difference appears when we generalize $$Y$$ to an arbitrary scheme: for each affine open subset $$V=\Spec B$$ of $$Y$$, the ideal

$$\mathscr{I}(V):=\ker(\varphi^\sharp(V))\subset B$$

defines a closed subscheme of $$V$$, but whether one can glue these together to form a single closed subscheme defined on all of $$Y$$ is a separate matter. Of course we will use [Proposition 6](#prop6) for this, and this hypothesis is satisfied in particular when $$X$$ is a reduced scheme or $$\varphi$$ is quasi-compact.

<div class="proposition" markdown="1">

<ins id="cor12">**Corollary 12**</ins> Let a scheme morphism $$\varphi: X \rightarrow Y$$ be given. If $$X$$ is reduced or $$\varphi$$ is quasi-compact, then the ideal sheaf $$\mathscr{I}$$ defined above satisfies the conditions of [Proposition 6](#prop6); hence $$\mathscr{I}$$ defines a closed subscheme of $$Y$$, and this is the scheme-theoretic image of $$\varphi$$.

</div>

Under the above assumption, checking the image of $$\varphi$$ on each affine open subset, one sees that the scheme-theoretic image of $$\varphi$$ has the form of a structure sheaf defined on the closure of the image of $$\varphi$$ (as a continuous map). 

Without the assumption of [Corollary 12](#cor12), this does not happen.

<div class="example" markdown="1">

<ins id="ex13">**Example 13**</ins> Define a scheme $$X$$ by

$$X=\coprod_{k\geq 0} \Spec \mathbb{K}[\epsilon]/(\epsilon^k)$$

and let $$Y=\Spec \mathbb{K}[\x]$$. We can define a scheme morphism $$X \rightarrow Y$$ on each component of $$X$$ via $$\x\mapsto \epsilon$$. Then from [Example 11](#ex11) we know that the image of $$X \rightarrow Y$$ (as a continuous map) is the single point $$0\in \mathbb{A}^1$$. 

However, the scheme-theoretic image of the scheme morphism $$\varphi:X \rightarrow Y$$ is not $$0$$. To see this, consider the morphism of structure sheaves $$\varphi^\sharp:\mathscr{O}_Y \rightarrow \varphi_\ast \mathscr{O}_X$$. For an element $$f$$ of $$\mathcal{O}_Y$$ to satisfy $$\varphi^\sharp(f)=0$$, the $$k$$-th order approximation of $$f$$ must be $$0$$ for every $$k$$, which forces $$f=0$$. Hence $$\mathscr{I}_{Z/Y}$$ must be $$0$$, and from this we see that the scheme-theoretic image of $$\varphi$$ is itself.

</div>

## Reduced Scheme Structures on Closed Sets

At the beginning of this article, we were able to define two structure sheaves on any closed set $$Z(\mathfrak{a})$$ of an affine scheme $$\Spec A$$: $$(\Spec\pi)_\ast \mathscr{O}_{\Spec A/\mathfrak{a}}$$ and $$\iota^{-1} \mathscr{O}_{\Spec A}$$. Of these, we chose $$(\Spec\pi)_\ast \mathscr{O}_{\Spec A/ \mathfrak{a}}$$ as the correct scheme structure on $$Z(\mathfrak{a})$$. We now examine $$\iota^{-1} \mathscr{O}_{\Spec A}$$.

More generally, consider an arbitrary scheme $$Y$$ and a closed set $$X$$ of $$Y$$. Then for any open set $$\Spec B$$ of $$Y$$, the closed set $$X\cap \Spec B$$ of $$\Spec B$$ can be written in the form $$Z(\mathfrak{b})$$ for some radical ideal $$\mathfrak{b}$$ of $$B$$, by [§Spectrums, ⁋Theorem 15](/en/math/scheme_theory/spectrums#thm15). 
Moreover, since $$\mathfrak{b}$$ is by definition the largest among the ideals of $$B$$ satisfying $$X\cap \Spec B= Z(\mathfrak{b}')$$, by [Lemma 9](#lem9) it is the smallest closed subscheme structure that can be given to $$X\cap \Spec B$$.

<div class="definition" markdown="1">

<ins id="def14">**Definition 14**</ins> For any closed set $$X$$ of a scheme $$Y$$, the scheme structure on $$X$$ defined above is called the *reduced scheme structure*, and is written $$X^\red$$. 

</div>

In particular, when $$X=Y$$, writing $$\Spec B=Z(0)$$ for any affine subset $$\Spec B$$, we have $$\mathfrak{b}=\sqrt{(0)}$$, so $$B/\sqrt{(0)}$$ becomes a reduced ring. Meanwhile, the sheaf morphism examined above,

$$\iota^{-1}\mathscr{O}_{\Spec A} \rightarrow (\Spec\pi\vert^{Z(\mathfrak{a})})_\ast \mathscr{O}_{\Spec A/\mathfrak{a}}$$

is simply the canonical scheme morphism obtained from [Lemma 9](#lem9).

---
**References**

**[Har]** R. Hartshorne, *Algebraic geometry*. Graduate texts in mathematics. Springer, 1977.  
**[Vak]** R. Vakil, *The rising sea: Foundation of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/).  

---
