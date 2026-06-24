---
title: "Linear Systems"
description: "We define effectiveness conditions for Weil and Cartier divisors, and explain how to find linearly equivalent effective divisors using nonzero global sections of the line bundle defined by a divisor."
excerpt: "Complete linear systems, base loci, and ampleness"

categories: [Math / Algebraic Varieties]
permalink: /en/math/algebraic_varieties/linear_systems
sidebar:
    nav: "algebraic_varieties-en"

date: 2026-03-29
weight: 10
translated_at: 2026-06-24T06:00:03+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-24T06:00:03+00:00
---
Previously, we defined a (Weil) divisor on a variety $$X$$ in [§Divisors, ⁋Definition 1](/en/math/algebraic_varieties/divisors#def1). By the definition of the Zariski topology, this can essentially be thought of as the zero set of some function defined on $$X$$, with the orders of these zeros added in; to make this well-defined even in cases such as $$\mathbb{P}^n$$, we generalized the notion of a function to a section of an appropriate line bundle.

On the other hand, since divisors also allow negative coefficients, this zero set is not merely a zero set but may become a pole, i.e., a zero of negative order. In such cases, we can find an *effective* divisor linearly equivalent to the given divisor and then investigate this property. ([§Divisors, ⁋Definition 7](/en/math/algebraic_varieties/divisors#def7))

For convenience of exposition, we have only discussed Weil divisors above, but a similar argument can be made for Cartier divisors, and the resulting definition is as follows.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> A Weil divisor $$D=\sum n_i D_i$$ defined on a variety $$X$$ is called *effective* if $$n_i\geq 0$$ for all $$i$$. A Cartier divisor $$\{(U_i, f_i)\}$$ is called *effective* if $$f_i$$ is regular on $$U_i$$ for all $$i$$.

</div>

Our goal, then, is to examine whether any effective divisor exists in the divisor class of a divisor $$D$$. To this end, consider the line bundle $$\mathcal{L}=\mathcal{O}_X(D)$$ defined by $$D$$. ([§Line Bundles and Vector Bundles, ⁋Definition 17](/en/math/algebraic_varieties/line_bundles#def17)) Each nonzero global section $$s\in \Gamma(X, \mathcal{L})$$ of $$\mathcal{L}$$ has no poles, so it defines an effective divisor $$\divisor(s)$$; we can check that this differs from the original $$D$$ only by a trivialization, so it is linearly equivalent to $$D$$. That is, to find an effective divisor linearly equivalent to $$D$$, it suffices to look at the nonzero global sections of $$\mathcal{O}_X(D)$$. However, one must be careful that $$\divisor(s)$$ depends not on $$s$$ itself but on its nonzero multiples; therefore, the object of interest is not $$\Gamma(X, \mathcal{L})$$ itself but its projectivization.

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> For a line bundle $$\mathcal{L}$$ on a variety $$X$$, the *complete linear system* of $$\mathcal{L}$$ is the projectivization of the global section space $$\Gamma(X, \mathcal{L})$$ of $$\mathcal{L}$$:

$$\lvert \mathcal{L} \rvert = \mathbb{P}(\Gamma(X, \mathcal{L}))$$

A *linear system* for $$\mathcal{L}$$ is a nonempty projective subspace of $$\lvert \mathcal{L} \rvert$$. That is, for a subspace $$V \subseteq \Gamma(X, \mathcal{L})$$, it is of the form $$\mathbb{P}(V) \subseteq \lvert \mathcal{L} \rvert$$.

</div>

## Linear Systems on Projective Space

From the calculations following [§Line Bundles and Vector Bundles, ⁋Example 12](/en/math/algebraic_varieties/line_bundles#ex12), we saw that $$\Gamma(\mathbb{P}^n, \mathcal{O}_{\mathbb{P}^n}(d))$$ is isomorphic to the space of homogeneous polynomials of degree $$d$$, $$\mathbb{K}[\x_0, \ldots, \x_n]_d$$. Since each element of this space defines a degree $$d$$ hypersurface in $$\mathbb{P}^n$$, we can understand the complete linear system of $$\mathcal{O}_{\mathbb{P}^n}(d)$$

$$\lvert \mathcal{O}_{\mathbb{P}^n}(d)\rvert=\mathbb{P}(\Gamma(\mathbb{P}^n, \mathcal{O}_{\mathbb{P}^n}(d)))\cong \mathbb{P}(\mathbb{K}[\x_0,\ldots, \x_n]_d)\cong \mathbb{P}^{\binom{n+d}{d} - 1}$$

geometrically as the family of degree $$d$$ hypersurfaces in $$\mathbb{P}^n$$.

<div class="example" markdown="1">

<ins id="ex3">**Example 3**</ins> For convenience, fix $$n=2$$. Then the family of degree $$1$$ hypersurfaces, i.e., the family of lines in $$\mathbb{P}^2$$, is isomorphic to $$\mathbb{P}^2$$ itself. More precisely,

$$\lvert \mathcal{O}_{\mathbb{P}^2}(1)\rvert\cong \mathbb{P}(\mathbb{K}[\x_0,\x_1,\x_2]_1)\cong \mathbb{P}^{\binom{3}{1}-1}=\mathbb{P}^2$$

and a point $$[a_0:a_1:a_2]$$ on the right-hand side $$\mathbb{P}^2$$ defines a line $$Z(a_0\x_0+a_1\x_1+a_2\x_2)$$ in $$\mathbb{P}^2$$.

For a slightly more involved and geometric example, consider the complete linear system defined by the line bundle $$\mathcal{O}_{\mathbb{P}^2}(2)$$ on $$\mathbb{P}^2$$

$$\lvert \mathcal{O}_{\mathbb{P}^2}(2)\rvert\cong \mathbb{P}(\mathbb{K}[\x_0,\x_1,\x_2]_2)\cong \mathbb{P}^{\binom{3}{2}-1}=\mathbb{P}^5$$

and its 1-dimensional subspace (that is, a 1-dimensional linear system). A typical example is the *pencil* of two conics. Consider two conics $$C_1=Z(F_1)$$, $$C_2=Z(F_2)$$ defined in $$\mathbb{P}^2$$. Then, as long as $$C_1$$ and $$C_2$$ are not the same conic, their linear combination

$$Z(\lambda F_1+\mu F_2)$$

is another degree $$2$$ curve in $$\mathbb{P}^2$$, and by definition all these conics pass through $$C_1\cap C_2$$. Here, the point $$[\lambda:\mu]\in \mathbb{P}^1$$ parametrizes these conics.

For a more concrete example, consider the two conics in $$\mathbb{P}^2$$

$$C_1: Z((\x_0-2\x_2)^2+\x_1^2-9\x_2^2),\qquad C_2: Z((\x_0+2\x_2)^2+\x_1^2-9\x_2^2)$$

These may look complicated as they stand, but when restricted to $$U_2$$ they become the equations of two circles

$$(\x-2)^2+\y^2=9,\qquad (\x+2)^2+\y^2=9$$

On $$U_2$$ they meet at $$(x,y)=(0,\pm\sqrt{5})$$, computed from the two equations above, and outside $$U_2$$—that is, on the <em>line at infinity</em>[^1] of $$U_2$$—they meet at the two points $$[1:i:0]$$, $$[1: -i:0]$$. The pencil $$Z(\lambda F_1+\mu F_2)$$ is then the family of conics passing through this intersection $$C_1\cap C_2$$.

On the other hand, a general degree 2 homogeneous polynomial is of the form

$$F(\x_0,\x_1,\x_2) = a_{00}\x_0^2 + a_{11}\x_1^2 + a_{22}\x_2^2 + a_{01}\x_0\x_1 + a_{02}\x_0\x_2 + a_{12}\x_1\x_2$$

which is exactly why $$\Gamma(X, \mathcal{O}(2))$$ is a 6-dimensional space. If we impose the additional condition that the set of four points $$C_1\cap C_2$$ computed above must be passed through, each of these four points imposes one constraint, eliminating one parameter each, so we know that there are 2 parameters remaining. More concretely, the following four conditions

$$0=F(0,\sqrt{5},1)=5a_{11}+a_{22}+\sqrt{5}a_{12}$$

$$0=F(0,-\sqrt{5},1)=5a_{11}+a_{22}-\sqrt{5}a_{12}$$

$$0=F(1,i,0)=a_{00}-a_{11}+ia_{01}$$

$$0=F(1,-i,0)=a_{00}-a_{11}-ia_{01}$$

force $$a_{12}=0$$, $$a_{01}=0$$, $$5a_{11}=-a_{22}$$, $$a_{00}=a_{11}$$, so the actual variables are the two $$a_{00}$$, $$a_{02}$$. That is, this family of conics forms a 2-dimensional subspace $$V$$ of $$\Gamma(X,\mathcal{O}(2))$$, and its projectivization is the $$\mathbb{P}^1$$ represented by $$[\lambda:\mu]$$.

![pencil_of_circles](/assets/images/Math/Algebraic_Varieties/Linear_Systems-1.svg){:style="width:40em" class="invert" .align-center}

</div>

Of course, [Definition 2](#def2) applies equally to any variety, whether $$X$$ is a projective space or a quasi-projective variety. However, the reason we took such pains to calculate [Example 3](#ex3) above is that for any quasi-projective variety $$X\subseteq \mathbb{P}^n$$, if $$D$$ comes from some $$\mathcal{O}_{\mathbb{P}^n}(d)$$, we can use the language of homogeneous polynomials directly. That is, in this case the restriction map

$$\Gamma(\mathbb{P}^n, \mathcal{O}_{\mathbb{P}^n}(d)) \to \Gamma(X, \mathcal{O}_{\mathbb{P}^n}(d)\vert_X)$$

sends a homogeneous polynomial $$F \in \mathbb{K}[\x_0, \ldots, \x_n]_d$$ to a section on $$X$$, and its kernel is the degree $$d$$ homogeneous part $$I(X)_d$$ of $$I(X)$$. Therefore,

$$\Gamma(X, \mathcal{O}_{\mathbb{P}^n}(d)\vert_X) \cong \mathbb{K}[\x_0, \ldots, \x_n]_d / I(X)_d$$

so essentially the same calculations as in $$\mathbb{P}^n$$ are possible. In particular, since the same intersection is defined when $$F - G \in I(X)$$, the parameter space becomes $$\mathbb{P}(V/(V \cap I(X)))$$.

## Base Locus

In the remainder of this post, given a linear system $$L=\mathbb{P}(V)$$ on $$X$$ and a basis $$F_0,\ldots, F_r$$ of $$V$$, we use this to define the embedding

$$\varphi_L:X\rightarrow \mathbb{P}^r;\qquad x\mapsto [F_0(x):\cdots:F_r(x)]$$

Of course, this is not always possible. For example, in [Example 3](#ex3), if we choose the two basis elements corresponding to $$(a_{00},a_{02})=(1,0), (0,1)$$

$$F_1(\x_0,\x_1,\x_2)=\x_0^2+\x_1^2-5\x_2^2, \qquad F_2(\x_0,\x_1,\x_2)=\x_0\x_2$$

then this "embedding" becomes

$$\mathbb{P}^2\rightarrow \mathbb{P}^1;\qquad [\x_0,\x_1,\x_2]\mapsto [\x_0^2+\x_1^2-5\x_2^2:\x_0\x_2]$$

This is a map from $$\mathbb{P}^2$$ to the smaller space $$\mathbb{P}^1$$, so we know something is wrong somewhere; this is because there exists a locus where the two functions $$F_1,F_2$$ simultaneously vanish.

The embedding $$\varphi_L$$ above actually depends on the choice of basis of $$V$$, but many properties of $$\varphi_L$$ do not. For example, as just mentioned, the points of $$X$$ where all basis elements vanish do not depend on the choice of basis.

To describe this rigorously, we define the *support* of a Weil divisor $$D = \sum n_i D_i$$ as $$\operatorname{Supp}(D) = \bigcup_{n_i \neq 0} D_i$$. That is, the support is the union of the prime divisors whose coefficient in the divisor is nonzero. Using this, the following is well-defined.

<div class="definition" markdown="1">

<ins id="def4">**Definition 4**</ins> The *base locus* $$\operatorname{Bs}(L)$$ of a linear system $$L \subseteq \lvert \mathcal{L} \rvert$$ is the closed subset shared by all elements of $$L$$. Specifically, when $$L = \mathbb{P}(V)$$ with $$V \subseteq \Gamma(X, \mathcal{L})$$,

$$\operatorname{Bs}(L) = \bigcap_{s \in V \setminus \{0\}} \operatorname{Supp}(\operatorname{div}(s))$$

where $$\operatorname{div}(s)$$ is the zero divisor of the section $$s$$.

</div>

Especially in calculations of hypersurfaces in $$\mathbb{P}^n$$, for $$V \subseteq \mathbb{K}[\x_0, \ldots, \x_n]_d$$ this is the same as $$\operatorname{Bs}(L) = \bigcap_{[F] \in L} Z(F)$$. Then the definition we wanted is the following.

<div class="definition" markdown="1">

<ins id="def5">**Definition 5**</ins> $$L$$ is called *basepoint-free* if $$\operatorname{Bs}(L) = \emptyset$$. That is, for any point $$p \in X$$, there always exists an element of $$L$$ not passing through $$p$$.

</div>

The key property of a basepoint-free linear system is as follows. If $$L=\mathbb{P}(V)$$ is basepoint-free, then a basis $$F_0,\ldots,F_r$$ of $$V$$ satisfies $$\bigcap Z(F_i)\cap X=\emptyset$$, so using this we can define the following regular map

$$\varphi_L:X\to\mathbb{P}^r,\quad p\mapsto[F_0(p):\cdots:F_r(p)]$$

Our initial interest in linear systems was to find effective divisors linearly equivalent to a given divisor $$D$$; the following proposition gives a direct answer to this.

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6**</ins> In the above situation, a hyperplane $$H$$ in $$\mathbb{P}^r$$ defines an effective divisor belonging to $$\lvert L\rvert$$.

</div>

To verify this, it suffices to check that for a hyperplane $$H: a_0\x_0+\cdots+a_r\x_r=0$$ in $$\mathbb{P}^r$$, the preimage $$\varphi_L^{-1}(H)$$ coincides with the zero set of the global section

$$\sigma=a_0F_0+\cdots+a_rF_r\in V$$

that is, with $$\divisor(\sigma)$$. Let us look at a more concrete example.

<div class="example" markdown="1">

<ins id="ex7">**Example 7**</ins> Let us examine the two examples of $$\mathbb{P}^n$$ seen in [Example 3](#ex3). First, consider the complete linear system

$$\lvert \mathcal{O}_{\mathbb{P}^2}(1)\rvert=\mathbb{P}(\mathbb{K}[\x_0,\x_1,\x_2]_1)$$

If we choose the basis of the vector space $$\mathbb{K}[\x_0,\x_1,\x_2]_1$$ as $$\x_0,\x_1,\x_2$$, then since there is no point in $$\mathbb{P}^2$$ where $$\x_0,\x_1,\x_2$$ simultaneously vanish, this is basepoint-free. The $$\varphi_L$$ defined by this choice of basis is simply the identity.

In the case of the two conics, as examined above, the base locus is not empty. In fact, the base locus is the four intersection points of $$C_1\cap C_2$$ already examined in [Example 3](#ex3), and geometrically we know that each element of the pencil shares exactly these four intersection points of $$C_1\cap C_2$$, which matches the definition of the base locus.

</div>

The above example intuitively shows the origin of the name "basepoint," but since $$\varphi_L$$ is the identity, [Proposition 6](#prop6) does not have much meaning in fact. Let us look at a more non-trivial example.

<div class="example" markdown="1">

<ins id="ex8">**Example 8**</ins> On $$\mathbb{P}^1$$ for $$d \ge 1$$, the map defined by the complete linear system $$\lvert \mathcal{O}_{\mathbb{P}^1}(d) \rvert$$ is

$$\nu_d: \mathbb{P}^1 \to \mathbb{P}^d, \quad [s : t] \mapsto [s^d : s^{d-1}t : \cdots : t^d]$$

This shows that the Veronese embedding examined in [§Projective Varieties, ⁋Example 16](/en/math/algebraic_varieties/projective_varieties#ex16) can be recovered in the language of complete linear systems.

For example, considering the hyperplane $$H_0: \x_0 = 0$$ in $$\mathbb{P}^d$$,

$$\nu_d^{-1}(H_0) = \{[s:t] \in \mathbb{P}^1 \mid s^d = 0\}$$

so scheme-theoretically this becomes the effective divisor $$d\cdot[0:1]$$ giving multiplicity $$d$$ to the point $$[0:1]$$. As another example, for the hyperplane $$H_1: \x_0 - \x_d = 0$$,

$$\nu_d^{-1}(H_1) = \{[s:t] \in \mathbb{P}^1 \mid s^d - t^d = 0\}$$

and since $$s^d - t^d$$ decomposes into a product of $$d$$ distinct linear factors (for example, if $$\mathbb{K}=\mathbb{C}$$ then $$s^d-t^d=\prod_{k=0}^{d-1}(s-\zeta^k t)$$), $$\nu_d^{-1}(H_1)$$ is an effective divisor consisting of $$d$$ distinct points on $$\mathbb{P}^1$$. In any case, these preimages are degree $$d$$ effective divisors belonging to $$\lvert \mathcal{O}_{\mathbb{P}^1}(d)\rvert$$.

</div>

## Ample Line Bundle

Although we are assuming that every variety is quasi-projective, in general a variety can be defined more abstractly. This approach has its pros and cons: the advantage is that our discussion becomes more flexible, and the price we pay is that embedding a variety is no longer trivial.

For example, in our language, to say that $$\mathbb{P}^1\times \mathbb{P}^1$$ is a (quasi-projective) variety we must necessarily embed it into some projective space. ([§Projective Varieties, ⁋Example 16](/en/math/algebraic_varieties/projective_varieties#ex16)) Instead, if we do not assume the existence of an ambient projective space in the definition of a variety, then $$\mathbb{P}^1\times \mathbb{P}^1$$ is automatically a variety without our having to show this, but it is unclear whether a general variety embeds into a projective space.

However, even on an abstract variety we can define line bundles, linear systems, and so on. Then in particular, using [Proposition 6](#prop6) we can define an appropriate map to projective space. The importance of the following definition should be understood in this context.

<div class="definition" markdown="1">

<ins id="def9">**Definition 9**</ins> A line bundle $$\mathcal{L}$$ (or the corresponding linear system $$\lvert \mathcal{L} \rvert$$) is called *very ample* if the regular map $$\varphi_{\mathcal{L}}: X \to \mathbb{P}(\Gamma(X, \mathcal{L}))$$ defined by the complete linear system $$\lvert \mathcal{L} \rvert = \mathbb{P}(\Gamma(X, \mathcal{L}))$$ is a closed embedding.

</div>

For this to be well-defined, $$\varphi_L$$ must not depend on the choice of basis, and indeed it is easy to check that this is the case.

The key point in the definition of very ample is that the map is not just a morphism but a *closed* embedding. That is, as explained above, even in the world of abstract varieties we can use this to define a projective variety, and with a very ample line bundle $$\mathcal{L}$$ we can represent $$X$$ by explicit coordinates in this ambient projective space.

We know that $$\mathcal{O}_{\mathbb{P}^n}(1)$$ is very ample, but $$\mathcal{O}_{\mathbb{P}^n}(-1)$$ is not. As seen in [§Line Bundles and Vector Bundles, ⁋Example 16](/en/math/algebraic_varieties/line_bundles#ex16), this is because the twisting of $$\mathcal{O}_{\mathbb{P}^n}(-1)$$ does not allow sections to cross the zero section as the base moves, so no global sections exist. On the other hand, the twisting of $$\mathcal{O}_{\mathbb{P}^n}(1)$$ allows this, so global sections do exist.

This example is perhaps too simple, but if there is some space more complicated than $$\mathbb{P}^n$$ and its complexity cannot be resolved by the twisting of a particular line bundle (even in the right direction), we could keep adding more and more twisting until it is resolved. From this idea we define the following.

<div class="definition" markdown="1">

<ins id="def10">**Definition 10**</ins> $$\mathcal{L}$$ is called *ample* if for some $$m > 0$$, $$\mathcal{L}^{\otimes m}$$ is very ample.

</div>

To see the usefulness of this definition, we should think of a space having a line bundle that is ample but not very ample, but it is still somewhat premature to introduce such a space. However, before long we will deal with such a space, and then ampleness will prove its full usefulness.

---

**References**

**[Har]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.

---

[^1]: The <em>line at infinity</em> of $$\mathbb{P}^2$$ and its geometric intuition were already analyzed in [§Projective Varieties, ⁋Example 11](/en/math/algebraic_varieties/projective_varieties#ex11).
