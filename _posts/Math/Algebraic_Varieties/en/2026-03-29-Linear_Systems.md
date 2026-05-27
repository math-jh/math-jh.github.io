---
title: "Linear Systems"
excerpt: "Complete linear systems, base loci, and ampleness"

categories: [Math / Algebraic Varieties]
permalink: /en/math/algebraic_varieties/linear_systems
sidebar:
    nav: "algebraic_varieties-en"

header:
    overlay_image: /assets/images/Math/Algebraic_Varieties/Linear_Systems.png
    overlay_filter: 0.5

date: 2026-03-29
last_modified_at: 2026-05-04
weight: 10
translated_at: 2026-05-28T11:36:15+00:00
translation_source: kimi-cli
last_polished_at: 2026-05-26T00:00:04+00:00
---
Previously, we defined a (Weil) divisor on a variety $$X$$ in [§Divisors, ⁋Definition 1](/en/math/algebraic_varieties/divisors#def1). By the definition of the Zariski topology, a divisor can essentially be viewed as the zero set of some *function* on $$X$$, with the orders of these zeros recorded; to make this well defined even in cases such as $$\mathbb{P}^n$$, we generalized *functions* to *sections of a suitable line bundle*.

On the other hand, since divisors allow negative coefficients, this "zero set" may in fact contain poles—zeros of negative order. In such cases, we may instead seek an *effective* divisor linearly equivalent to the given one and study its properties. ([§Divisors, ⁋Definition 7](/en/math/algebraic_varieties/divisors#def7))

For ease of exposition we discussed only Weil divisors above, but the same argument applies to Cartier divisors, yielding the following definition.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> A Weil divisor $$D=\sum n_i D_i$$ on a variety $$X$$ is *effective* if $$n_i \geq 0$$ for all $$i$$. A Cartier divisor $$\{(U_i, f_i)\}$$ is *effective* if $$f_i$$ is regular on $$U_i$$ for all $$i$$.

</div>

Our goal, then, is to determine whether the linear equivalence class of a divisor $$D$$ contains any effective divisors. To this end, consider the line bundle $$\mathcal{L}=\mathcal{O}_X(D)$$ determined by $$D$$. ([§Line Bundles and Vector Bundles, ⁋Definition 17](/en/math/algebraic_varieties/line_bundles#def17)) Every nonzero global section $$s\in \Gamma(X, \mathcal{L})$$ of $$\mathcal{L}$$ has no poles, so it defines an effective divisor $$\divisor(s)$$; one checks that this differs from the original $$D$$ only by a trivialization, hence is linearly equivalent to $$D$$. Thus, to find an effective divisor linearly equivalent to $$D$$, it suffices to examine the nonzero global sections of $$\mathcal{O}_X(D)$$. However, $$\divisor(s)$$ depends not on $$s$$ itself but only on its nonzero scalar multiples; consequently, the object of interest is not $$\Gamma(X, \mathcal{L})$$ itself but its projectivization.

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> For a line bundle $$\mathcal{L}$$ on a variety $$X$$, the *complete linear system* of $$\mathcal{L}$$ is the projectivization of the space of global sections $$\Gamma(X, \mathcal{L})$$:

$$\lvert \mathcal{L} \rvert = \mathbb{P}(\Gamma(X, \mathcal{L})).$$

A *linear system* for $$\mathcal{L}$$ is a nonempty projective subspace of $$\lvert \mathcal{L} \rvert$$. That is, it is of the form $$\mathbb{P}(V) \subseteq \lvert \mathcal{L} \rvert$$ for some subspace $$V \subseteq \Gamma(X, \mathcal{L})$$.

</div>

## Linear Systems on Projective Space

By the calculations following [§Line Bundles and Vector Bundles, ⁋Example 12](/en/math/algebraic_varieties/line_bundles#ex12), we saw that $$\Gamma(\mathbb{P}^n, \mathcal{O}_{\mathbb{P}^n}(d))$$ is isomorphic to the space $$\mathbb{K}[\x_0, \ldots, \x_n]_d$$ of homogeneous polynomials of degree $$d$$. Since each element of this space defines a degree-$$d$$ hypersurface in $$\mathbb{P}^n$$, we may interpret the complete linear system

$$\lvert \mathcal{O}_{\mathbb{P}^n}(d)\rvert=\mathbb{P}(\Gamma(\mathbb{P}^n, \mathcal{O}_{\mathbb{P}^n}(d)))\cong \mathbb{P}(\mathbb{K}[\x_0,\ldots, \x_n]_d)\cong \mathbb{P}^{\binom{n+d}{d} - 1}$$

geometrically as a family of degree-$$d$$ hypersurfaces in $$\mathbb{P}^n$$.

<div class="example" markdown="1">

<ins id="ex3">**Example 3**</ins> For convenience, fix $$n=2$$. Then the family of degree-$$1$$ hypersurfaces—that is, lines in $$\mathbb{P}^2$$—is isomorphic to $$\mathbb{P}^2$$ itself. More precisely,

$$\lvert \mathcal{O}_{\mathbb{P}^2}(1)\rvert\cong \mathbb{P}(\mathbb{K}[\x_0,\x_1,\x_2]_1)\cong \mathbb{P}^{\binom{3}{1}-1}=\mathbb{P}^2,$$

and a point $$[a_0:a_1:a_2]$$ on the right-hand side corresponds to the line $$Z(a_0\x_0+a_1\x_1+a_2\x_2)$$ in $$\mathbb{P}^2$$.

For a more involved geometric example, consider a one-dimensional subspace (that is, a one-dimensional linear system) inside the complete linear system

$$\lvert \mathcal{O}_{\mathbb{P}^2}(2)\rvert\cong \mathbb{P}(\mathbb{K}[\x_0,\x_1,\x_2]_2)\cong \mathbb{P}^{\binom{3}{2}-1}=\mathbb{P}^5$$

defined by the line bundle $$\mathcal{O}_{\mathbb{P}^2}(2)$$ on $$\mathbb{P}^2$$. A typical instance is a *pencil* of two conics. Let $$C_1=Z(F_1)$$ and $$C_2=Z(F_2)$$ be two distinct conics in $$\mathbb{P}^2$$. Then their linear combination

$$Z(\lambda F_1+\mu F_2)$$

is another degree-$$2$$ curve in $$\mathbb{P}^2$$, and by definition all these conics pass through $$C_1\cap C_2$$. Here the point $$[\lambda:\mu]\in \mathbb{P}^1$$ parametrizes these conics.

For a concrete example, consider the two conics

$$C_1: Z((\x_0-2\x_2)^2+\x_1^2-9\x_2^2),\qquad C_2: Z((\x_0+2\x_2)^2+\x_1^2-9\x_2^2)$$

in $$\mathbb{P}^2$$. These equations appear complicated, but upon restriction to $$U_2$$ they become the equations of two circles

$$(\x-2)^2+\y^2=9,\qquad (\x+2)^2+\y^2=9.$$

On $$U_2$$ they meet at $$(x,y)=(0,\pm\sqrt{5})$$, computed directly from the two equations above, while outside $$U_2$$—that is, on the *line at infinity* of $$U_2$$[^1]—they meet at the two points $$[1:i:0]$$ and $$[1:-i:0]$$. The pencil $$Z(\lambda F_1+\mu F_2)$$ is then the family of conics passing through these four points of $$C_1\cap C_2$$.

Meanwhile, a general degree-$$2$$ homogeneous polynomial has the form

$$F(\x_0,\x_1,\x_2) = a_{00}\x_0^2 + a_{11}\x_1^2 + a_{22}\x_2^2 + a_{01}\x_0\x_1 + a_{02}\x_0\x_2 + a_{12}\x_1\x_2,$$

which is precisely why $$\Gamma(X, \mathcal{O}(2))$$ is a $$6$$-dimensional space. If we impose the additional condition that the curve pass through the four-point set $$C_1\cap C_2$$ computed above, each of the four points imposes one independent constraint, eliminating one parameter each, leaving $$2$$ parameters. More explicitly, the four conditions

$$0=F(0,\sqrt{5},1)=5a_{11}+a_{22}+\sqrt{5}a_{12}$$
$$0=F(0,-\sqrt{5},1)=5a_{11}+a_{22}-\sqrt{5}a_{12}$$
$$0=F(1,i,0)=a_{00}-a_{11}+ia_{01}$$
$$0=F(1,-i,0)=a_{00}-a_{11}-ia_{01}$$

force $$a_{12}=0$$, $$a_{01}=0$$, $$5a_{11}=-a_{22}$$, and $$a_{00}=a_{11}$$, so the only free variables are $$a_{00}$$ and $$a_{02}$$. Thus this family of conics forms a $$2$$-dimensional subspace $$V\subseteq\Gamma(X,\mathcal{O}(2))$$, and its projectivization is the $$\mathbb{P}^1$$ parametrized by $$[\lambda:\mu]$$.

![pencil_of_circles](/assets/images/Math/Algebraic_Varieties/Linear_Systems-1.png){:style="width:40em" class="invert" .align-center}

</div>

Of course, [Definition 2](#def2) applies equally to any variety, whether $$X$$ is projective space or a quasi-projective variety. The reason we worked through [Example 3](#ex3) in such detail, however, is that for any quasi-projective variety $$X\subseteq \mathbb{P}^n$$, if $$D$$ comes from some $$\mathcal{O}_{\mathbb{P}^n}(d)$$ then the language of homogeneous polynomials carries over unchanged. In this case the restriction map

$$\Gamma(\mathbb{P}^n, \mathcal{O}_{\mathbb{P}^n}(d)) \to \Gamma(X, \mathcal{O}_{\mathbb{P}^n}(d)\vert_X)$$

sends a homogeneous polynomial $$F \in \mathbb{K}[\x_0, \ldots, \x_n]_d$$ to a section on $$X$$, and its kernel is the degree-$$d$$ homogeneous part $$I(X)_d$$ of $$I(X)$$. Hence

$$\Gamma(X, \mathcal{O}_{\mathbb{P}^n}(d)\vert_X) \cong \mathbb{K}[\x_0, \ldots, \x_n]_d / I(X)_d,$$

so the same calculations as in $$\mathbb{P}^n$$ are available. In particular, since $$F - G \in I(X)$$ defines the same intersection, the parameter space becomes $$\mathbb{P}(V/(V \cap I(X)))$$.

## Base Locus

In the remainder of this post, given a linear system $$L=\mathbb{P}(V)$$ on $$X$$ and a basis $$F_0,\ldots,F_r$$ of $$V$$, we define the embedding

$$\varphi_L:X\rightarrow \mathbb{P}^r;\qquad x\mapsto [F_0(x):\cdots:F_r(x)]$$

using these data.

Of course, this is not always possible. For instance, in [Example 3](#ex3), if we choose the two basis elements

$$F_1(\x_0,\x_1,\x_2)=\x_0^2+\x_1^2-5\x_2^2, \qquad F_2(\x_0,\x_1,\x_2)=\x_0\x_2$$

corresponding to $$(a_{00},a_{02})=(1,0)$$ and $$(0,1)$$, this "embedding" becomes

$$\mathbb{P}^2\rightarrow \mathbb{P}^1;\qquad [\x_0,\x_1,\x_2]\mapsto [\x_0^2+\x_1^2-5\x_2^2:\x_0\x_2].$$

Since this is a map from $$\mathbb{P}^2$$ to the smaller space $$\mathbb{P}^1$$, we immediately sense that something is wrong; indeed, there is a locus where the two functions $$F_1$$ and $$F_2$$ vanish simultaneously.

The above embedding $$\varphi_L$$ does depend on the choice of basis of $$V$$, but many properties of $$\varphi_L$$ do not. For example, the set of points of $$X$$ where all basis elements vanish is independent of the choice of basis, as we have just seen.

To describe this rigorously, we define the *support* of a Weil divisor $$D = \sum n_i D_i$$ as $$\operatorname{Supp}(D) = \bigcup_{n_i \neq 0} D_i$$; that is, the support is the union of the prime divisors appearing with nonzero coefficient in $$D$$. With this, the following is well defined.

<div class="definition" markdown="1">

<ins id="def4">**Definition 4**</ins> The *base locus* $$\operatorname{Bs}(L)$$ of a linear system $$L \subseteq \lvert \mathcal{L} \rvert$$ is the closed subset common to all elements of $$L$$. Specifically, when $$L = \mathbb{P}(V)$$ with $$V \subseteq \Gamma(X, \mathcal{L})$$,

$$\operatorname{Bs}(L) = \bigcap_{s \in V \setminus \{0\}} \operatorname{Supp}(\operatorname{div}(s)),$$

where $$\operatorname{div}(s)$$ is the zero divisor of the section $$s$$.

</div>

In particular, for hypersurface computations in $$\mathbb{P}^n$$, when $$V \subseteq \mathbb{K}[\x_0, \ldots, \x_n]_d$$ this coincides with $$\operatorname{Bs}(L) = \bigcap_{[F] \in L} Z(F)$$. The definition we were aiming for is then the following.

<div class="definition" markdown="1">

<ins id="def5">**Definition 5**</ins> $$L$$ is *basepoint-free* if $$\operatorname{Bs}(L) = \emptyset$$. Equivalently, for every point $$p \in X$$ there exists an element of $$L$$ not passing through $$p$$.

</div>

The key property of a basepoint-free linear system is the following. If $$L=\mathbb{P}(V)$$ is basepoint-free, then a basis $$F_0,\ldots,F_r$$ of $$V$$ satisfies $$\bigcap Z(F_i)\cap X=\emptyset$$, and we obtain a well-defined regular map

$$\varphi_L:X\to\mathbb{P}^r,\quad p\mapsto[F_0(p):\cdots:F_r(p)].$$

Our original interest in linear systems was to find effective divisors linearly equivalent to a given divisor $$D$$; the following proposition gives a direct answer.

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6**</ins> In the situation above, a hyperplane $$H$$ in $$\mathbb{P}^r$$ defines an effective divisor belonging to $$\lvert L\rvert$$.

</div>

To verify this, one checks that for a hyperplane $$H: a_0\x_0+\cdots+a_r\x_r=0$$ in $$\mathbb{P}^r$$, the preimage $$\varphi_L^{-1}(H)$$ coincides with the zero set of the global section

$$\sigma=a_0F_0+\cdots+a_rF_r\in V,$$

that is, with $$\divisor(\sigma)$$. Let us examine a more concrete example.

<div class="example" markdown="1">

<ins id="ex7">**Example 7**</ins> Consider again the two examples in $$\mathbb{P}^n$$ from [Example 3](#ex3). First, take the complete linear system

$$\lvert \mathcal{O}_{\mathbb{P}^2}(1)\rvert=\mathbb{P}(\mathbb{K}[\x_0,\x_1,\x_2]_1).$$

Choosing $$\x_0,\x_1,\x_2$$ as a basis of the vector space $$\mathbb{K}[\x_0,\x_1,\x_2]_1$$, there is no point of $$\mathbb{P}^2$$ where all three vanish simultaneously, so this system is basepoint-free. The map $$\varphi_L$$ determined by this choice of basis is simply the identity.

For the pencil of two conics, as we saw above, the base locus is nonempty. Indeed, the base locus consists of the four intersection points of $$C_1\cap C_2$$ already examined in [Example 3](#ex3); geometrically, every member of the pencil shares exactly these four points, which matches the definition of the base locus.

</div>

The preceding example gives an intuitive explanation for the term "basepoint," but since $$\varphi_L$$ is the identity, [Proposition 6](#prop6) is not particularly illuminating. Let us look at a more nontrivial example.

<div class="example" markdown="1">

<ins id="ex8">**Example 8**</ins> For $$d \ge 1$$ on $$\mathbb{P}^1$$, the map defined by the complete linear system $$\lvert \mathcal{O}_{\mathbb{P}^1}(d) \rvert$$ is

$$\nu_d: \mathbb{P}^1 \to \mathbb{P}^d, \quad [s : t] \mapsto [s^d : s^{d-1}t : \cdots : t^d].$$

This shows that the Veronese embedding examined in [§Projective Varieties, ⁋Example 16](/en/math/algebraic_varieties/projective_varieties#ex16) can be recovered in the language of complete linear systems.

For example, for the hyperplane $$H_0: \x_0 = 0$$ in $$\mathbb{P}^d$$,

$$\nu_d^{-1}(H_0) = \{[s:t] \in \mathbb{P}^1 \mid s^d = 0\},$$

so scheme-theoretically this is the effective divisor $$d\cdot[0:1]$$, giving multiplicity $$d$$ to the point $$[0:1]$$. As another example, for the hyperplane $$H_1: \x_0 - \x_d = 0$$,

$$\nu_d^{-1}(H_1) = \{[s:t] \in \mathbb{P}^1 \mid s^d - t^d = 0\},$$

and since $$s^d - t^d$$ factors into a product of $$d$$ distinct linear factors (for instance, if $$\mathbb{K}=\mathbb{C}$$ then $$s^d-t^d=\prod_{k=0}^{d-1}(s-\zeta^k t)$$), the preimage $$\nu_d^{-1}(H_1)$$ is an effective divisor consisting of $$d$$ distinct points on $$\mathbb{P}^1$$. In either case, these preimages are degree-$$d$$ effective divisors belonging to $$\lvert \mathcal{O}_{\mathbb{P}^1}(d)\rvert$$.

</div>

## Ample Line Bundles

Although we are assuming that every variety is quasi-projective, varieties can in general be defined more abstractly. This approach has both advantages and disadvantages: the benefit is greater flexibility, while the cost is that embedding a variety into projective space is no longer automatic.

For example, in our present language, to regard $$\mathbb{P}^1\times \mathbb{P}^1$$ as a (quasi-projective) variety we must embed it into some projective space. ([§Projective Varieties, ⁋Example 16](/en/math/algebraic_varieties/projective_varieties#ex16)) Conversely, if the definition of a variety does not assume the existence of an ambient projective space, then $$\mathbb{P}^1\times \mathbb{P}^1$$ is automatically a variety without our having to exhibit an embedding; but it becomes unclear whether an arbitrary variety embeds into projective space at all.

Nevertheless, even on an abstract variety we can define line bundles, linear systems, and the like. In particular, using [Proposition 6](#prop6) we can construct a suitable map to projective space. The importance of the following definition should be understood in this context.

<div class="definition" markdown="1">

<ins id="def9">**Definition 9**</ins> A line bundle $$\mathcal{L}$$ (or the corresponding linear system $$\lvert \mathcal{L} \rvert$$) is *very ample* if the regular map $$\varphi_{\mathcal{L}}: X \to \mathbb{P}(\Gamma(X, \mathcal{L}))$$ defined by the complete linear system $$\lvert \mathcal{L} \rvert = \mathbb{P}(\Gamma(X, \mathcal{L}))$$ is a closed embedding.

</div>

For this to be well defined, $$\varphi_L$$ must be independent of the choice of basis, and this is easily verified.

The crucial point in the definition of very ample is that the map is not merely a morphism but a *closed* embedding. That is, even in the world of abstract varieties we can use this to define a projective variety, and moreover, with a very ample line bundle $$\mathcal{L}$$ we can express $$X$$ in explicit coordinates inside this ambient projective space.

We know that $$\mathcal{O}_{\mathbb{P}^n}(1)$$ is very ample, whereas $$\mathcal{O}_{\mathbb{P}^n}(-1)$$ is not. As we saw in [§Line Bundles and Vector Bundles, ⁋Example 12](/en/math/algebraic_varieties/line_bundles#ex12), the reason is that for $$\mathcal{O}_{\mathbb{P}^n}(-1)$$, the twisting of the fibers over the base prevents sections from crossing the zero section, so no nonzero global sections exist. By contrast, the twist in $$\mathcal{O}_{\mathbb{P}^n}(1)$$ permits this, thereby giving rise to global sections.

This example is rather simple, but if we had a space more complicated than $$\mathbb{P}^n$$ whose complexity could not be resolved by the twist of a single line bundle alone (even in the correct direction), we could keep adding more twist until it is. From this intuition we make the following definition.

<div class="definition" markdown="1">

<ins id="def10">**Definition 10**</ins> $$\mathcal{L}$$ is *ample* if $$\mathcal{L}^{\otimes m}$$ is very ample for some $$m > 0$$.

</div>

To appreciate the usefulness of this definition we should consider a space possessing a line bundle that is ample but not very ample, but it is still somewhat premature to introduce such a space. Once we do encounter such a space, however, ampleness will demonstrate its full worth.

---

**References**

**[Har]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.

---

[^1]: We have already analyzed the *line at infinity* of $$\mathbb{P}^2$$ and its geometric intuition in [§Projective Varieties, ⁋Example 11](/en/math/algebraic_varieties/projective_varieties#ex11).
