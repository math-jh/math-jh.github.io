---
title: "Linear Systems"
description: "We define the effectiveness conditions for Weil and Cartier divisors, and explain how to obtain linearly equivalent effective divisors via nonzero global sections of the associated line bundle."
excerpt: "Complete linear systems, base loci, and ampleness"

categories: [Math / Algebraic Varieties]
permalink: /en/math/algebraic_varieties/linear_systems
sidebar:
    nav: "algebraic_varieties-en"

date: 2026-03-29
weight: 11
translated_at: 2026-08-16T00:48:25+00:00
translation_source: kimi-cli
---
Previously, we defined a (Weil) divisor on a variety $X$ in [§Divisors, ⁋Definition 1](/en/math/algebraic_varieties/divisors#def1). By the definition of the Zariski topology, this can essentially be thought of as the zero set of some *function* on $X$, weighted by the orders of these zeros; and to make this well-defined even for cases such as $\mathbb{P}^n$, we generalized the notion of a *function* to a *section of a suitable line bundle*.

On the other hand, since divisors allow negative coefficients, this zero set need not be a zero set at all. It can be a pole, i.e., a zero of negative order. In such cases, we may find an *effective* divisor linearly equivalent to the given divisor and then investigate this property. ([§Divisors, ⁋Definition 7](/en/math/algebraic_varieties/divisors#def7))

For convenience of exposition, we have discussed only Weil divisors above, but a similar argument applies to Cartier divisors, and the resulting definition is as follows.

::: Definition 1
A Weil divisor $D=\sum n_i D_i$ on a variety $X$ is called *effective* if $n_i\geq 0$ for all $i$. A Cartier divisor $\{(U_i, f_i)\}$ is *effective* if $f_i$ is regular on $U_i$ for all $i$.
:::

Our goal, then, is to examine whether there exists any effective divisor in the divisor class of $D$. To this end, consider the line bundle $\mathcal{L}=\mathcal{O}_X(D)$ defined by $D$. ([§Line Bundles and Vector Bundles, ⁋Definition 17](/en/math/algebraic_varieties/line_bundles#def17)) Each nonzero global section $s\in \Gamma(X, \mathcal{L})$ of $\mathcal{L}$ has no poles, so it defines an effective divisor $\divisor(s)$, and one can check that this differs from the original $D$ only by a trivialization, hence is linearly equivalent to $D$. Thus, to find an effective divisor linearly equivalent to $D$, it suffices to look at the nonzero global sections of $\mathcal{O}_X(D)$. One cautionary point is that $\divisor(s)$ does not depend on nonzero scalar multiples of $s$; therefore, the object of interest is not $\Gamma(X, \mathcal{L})$ itself but rather its projectivization.

::: Definition 2
For a line bundle $\mathcal{L}$ on a variety $X$, the *complete linear system* of $\mathcal{L}$ is the projectivization of the global section space $\Gamma(X, \mathcal{L})$:

$$\lvert \mathcal{L} \rvert = \mathbb{P}(\Gamma(X, \mathcal{L})).$$

A *linear system* for $\mathcal{L}$ is a nonempty projective subspace of $\lvert \mathcal{L} \rvert$. That is, for a subspace $V \subseteq \Gamma(X, \mathcal{L})$, it is of the form $\mathbb{P}(V) \subseteq \lvert \mathcal{L} \rvert$.
:::

## Linear Systems on Projective Space

From the calculations following [§Line Bundles and Vector Bundles, ⁋Example 16](/en/math/algebraic_varieties/line_bundles#ex16), we saw that $\Gamma(\mathbb{P}^n, \mathcal{O}_{\mathbb{P}^n}(d))$ is isomorphic to the space of homogeneous polynomials of degree $d$, denoted $\mathbb{K}[\x_0, \ldots, \x_n]_d$. Since each element of this space defines a degree $d$ hypersurface in $\mathbb{P}^n$, we can geometrically understand the complete linear system of $\mathcal{O}_{\mathbb{P}^n}(d)$

$$\lvert \mathcal{O}_{\mathbb{P}^n}(d)\rvert=\mathbb{P}(\Gamma(\mathbb{P}^n, \mathcal{O}_{\mathbb{P}^n}(d)))\cong \mathbb{P}(\mathbb{K}[\x_0,\ldots, \x_n]_d)\cong \mathbb{P}^{\binom{n+d}{d} - 1}$$

as a family of degree $d$ hypersurfaces in $\mathbb{P}^n$.

::: Example 3
For convenience, fix $n=2$. Then the family of degree $1$ hypersurfaces, i.e., lines in $\mathbb{P}^2$, is isomorphic to $\mathbb{P}^2$ itself. More precisely,

$$\lvert \mathcal{O}_{\mathbb{P}^2}(1)\rvert\cong \mathbb{P}(\mathbb{K}[\x_0,\x_1,\x_2]_1)\cong \mathbb{P}^{\binom{3}{1}-1}=\mathbb{P}^2$$

where a point $[a_0:a_1:a_2]$ on the right-hand side $\mathbb{P}^2$ defines the line $Z(a_0\x_0+a_1\x_1+a_2\x_2)$ in $\mathbb{P}^2$.

For a more complicated and geometric example, consider the complete linear system defined by the line bundle $\mathcal{O}_{\mathbb{P}^2}(2)$ on $\mathbb{P}^2$:

$$\lvert \mathcal{O}_{\mathbb{P}^2}(2)\rvert\cong \mathbb{P}(\mathbb{K}[\x_0,\x_1,\x_2]_2)\cong \mathbb{P}^{\binom{4}{2}-1}=\mathbb{P}^5.$$

We consider a one-dimensional subspace (i.e., a $1$-dimensional linear system) of this. A typical example is a *pencil* of two conics. Consider two conics $C_1=Z(F_1)$, $C_2=Z(F_2)$ defined in $\mathbb{P}^2$. Then, provided $C_1$ and $C_2$ are not the same conic, their linear combination

$$Z(\lambda F_1+\mu F_2)$$

is another degree $2$ curve in $\mathbb{P}^2$, and by definition all these conics pass through $C_1\cap C_2$. Here, the point $[\lambda:\mu]\in \mathbb{P}^1$ parametrizes these conics.

For a more concrete example, consider the two conics in $\mathbb{P}^2$

$$C_1: Z((\x_0-2\x_2)^2+\x_1^2-9\x_2^2),\qquad C_2: Z((\x_0+2\x_2)^2+\x_1^2-9\x_2^2).$$

These expressions look complicated as they stand, but restricted to $U_2$ they become the equations of two circles

$$(\x-2)^2+\y^2=9,\qquad (\x+2)^2+\y^2=9.$$

On $U_2$, these meet at $(x,y)=(0,\pm\sqrt{5})$ computed from the two equations above, and outside $U_2$ (that is, on the *line at infinity*[^1] of $\mathbb{P}^2$) they meet at the two points $[1:i:0]$, $[1: -i:0]$. The above pencil $Z(\lambda F_1+\mu F_2)$ is then the family of conics passing through this intersection $C_1\cap C_2$.

On the other hand, a general degree $2$ homogeneous polynomial has the form

$$F(\x_0,\x_1,\x_2) = a_{00}\x_0^2 + a_{11}\x_1^2 + a_{22}\x_2^2 + a_{01}\x_0\x_1 + a_{02}\x_0\x_2 + a_{12}\x_1\x_2,$$

and this is exactly why $\Gamma(\mathbb{P}^2, \mathcal{O}_{\mathbb{P}^2}(2))$ is a $6$-dimensional space. If we impose the additional condition of passing through the four-point set $C_1\cap C_2$ computed above, each of these four points imposes one constraint, eliminating one parameter each, so we know that the parameters needed to express this are $2$. More concretely, the following four conditions

$$0=F(0,\sqrt{5},1)=5a_{11}+a_{22}+\sqrt{5}a_{12}$$

$$0=F(0,-\sqrt{5},1)=5a_{11}+a_{22}-\sqrt{5}a_{12}$$

$$0=F(1,i,0)=a_{00}-a_{11}+ia_{01}$$

$$0=F(1,-i,0)=a_{00}-a_{11}-ia_{01}$$

force $a_{12}=0$, $a_{01}=0$, $5a_{11}=-a_{22}$, $a_{00}=a_{11}$, so the actual variables are the two $a_{00}$, $a_{02}$. That is, this family of conics forms a $2$-dimensional subspace $V$ of $\Gamma(\mathbb{P}^2,\mathcal{O}_{\mathbb{P}^2}(2))$, and its projectivization becomes the $\mathbb{P}^1$ represented by $[\lambda:\mu]$.

{% diagram Math/Algebraic_Varieties/Linear_Systems-1.svg width="40em" alt="pencil_of_circles" %}
:::

Of course, [Definition 2](#def2) applies equally to any variety, whether $X$ is projective space or a quasi-projective variety. However, the reason we went to such lengths with [Example 3](#ex3) above is that for any quasi-projective variety $X\subseteq \mathbb{P}^n$, if $D$ comes from some $\mathcal{O}_{\mathbb{P}^n}(d)$, we can use the language of homogeneous polynomials directly. That is, in this case the restriction map

$$\Gamma(\mathbb{P}^n, \mathcal{O}_{\mathbb{P}^n}(d)) \rightarrow \Gamma(X, \mathcal{O}_{\mathbb{P}^n}(d)\vert_X)$$

sends a homogeneous polynomial $F \in \mathbb{K}[\x_0, \ldots, \x_n]_d$ to a section on $X$, and its kernel is the degree $d$ homogeneous part $I(X)_d$ of $I(X)$. Therefore, if this restriction map is surjective, then

$$\Gamma(X, \mathcal{O}_{\mathbb{P}^n}(d)\vert_X) \cong \mathbb{K}[\x_0, \ldots, \x_n]_d / I(X)_d,$$

so essentially the same calculations as in $\mathbb{P}^n$ are possible. In fact, it is known that this surjectivity holds when $d$ is sufficiently large. In particular, since $F - G \in I(X)$ defines the same intersection, the parameter space becomes $\mathbb{P}(V/(V \cap I(X)))$.

## Base Locus

In what follows, given a linear system $L=\mathbb{P}(V)$ on $X$ and a basis $F_0,\ldots, F_r$ of $V$, we use this to define the embedding

$$\varphi_L:X\rightarrow \mathbb{P}^r;\qquad x\mapsto [F_0(x):\cdots:F_r(x)].$$

Of course, this is not always possible. For instance, in [Example 3](#ex3), if we choose the following two bases corresponding to $(a_{00},a_{02})=(1,0), (0,1)$:

$$G_1(\x_0,\x_1,\x_2)=\x_0^2+\x_1^2-5\x_2^2, \qquad G_2(\x_0,\x_1,\x_2)=\x_0\x_2,$$

then this "embedding" becomes

$$\mathbb{P}^2\rightarrow \mathbb{P}^1;\qquad [\x_0:\x_1:\x_2]\mapsto [\x_0^2+\x_1^2-5\x_2^2:\x_0\x_2].$$

This is a map from $\mathbb{P}^2$ to the smaller space $\mathbb{P}^1$, so we already know something is wrong, and this is because there exists a locus where the two functions $G_1,G_2$ vanish simultaneously.

In fact, the embedding $\varphi_L$ depends on the choice of basis of $V$, but many properties of $\varphi_L$ do not. For example, as above, the points of $X$ where all basis elements vanish do not depend on the choice of basis.

To describe this rigorously, we define the *support* of a Weil divisor $D = \sum n_i D_i$ as $\operatorname{Supp}(D) = \bigcup_{n_i \neq 0} D_i$. That is, the support is the union of the prime divisors with nonzero coefficient in the divisor. Using this, the following is well-defined.

::: Definition 4
The *base locus* $\operatorname{Bs}(L)$ of a linear system $L \subseteq \lvert \mathcal{L} \rvert$ is the closed subset shared by all elements of $L$. Specifically, when $L = \mathbb{P}(V)$ with $V \subseteq \Gamma(X, \mathcal{L})$,

$$\operatorname{Bs}(L) = \bigcap_{s \in V \setminus \{0\}} \operatorname{Supp}(\divisor(s)),$$

where $\divisor(s)$ is the zero divisor of the section $s$.
:::

In particular, for calculations of hypersurfaces in $\mathbb{P}^n$, this coincides with $\operatorname{Bs}(L) = \bigcap_{[F] \in L} Z(F)$ for $V \subseteq \mathbb{K}[\x_0, \ldots, \x_n]_d$. Then the definition we wanted is as follows.

::: Definition 5
$L$ is called *basepoint-free* if $\operatorname{Bs}(L) = \emptyset$. That is, for any point $p \in X$, there always exists an element of $L$ not passing through $p$.
:::

The key property of a basepoint-free linear system is as follows. If $L=\mathbb{P}(V)$ is basepoint-free, then a basis $F_0,\ldots,F_r$ of $V$ satisfies $\bigcap Z(F_i)\cap X=\emptyset$, so using this we can define the following regular map:

$$\varphi_L:X\rightarrow\mathbb{P}^r,\quad p\mapsto[F_0(p):\cdots:F_r(p)].$$

Our original interest in linear systems was to find effective divisors linearly equivalent to a given divisor $D$, and the following proposition gives a direct answer to this.

::: Proposition 6
In the above situation, a hyperplane $H$ of $\mathbb{P}^r$ defines an effective divisor belonging to $L$.
:::

To verify this, for a hyperplane $H: a_0\x_0+\cdots+a_r\x_r=0$ in $\mathbb{P}^r$, one checks that $\varphi_L^{-1}(H)$ coincides with the zero set of the global section

$$\sigma=a_0F_0+\cdots+a_rF_r\in V,$$

i.e., with $\divisor(\sigma)$. Let us look at a more concrete example.

::: Example 7
Consider the two examples in $\mathbb{P}^2$ from [Example 3](#ex3). First, consider the complete linear system

$$\lvert \mathcal{O}_{\mathbb{P}^2}(1)\rvert=\mathbb{P}(\mathbb{K}[\x_0,\x_1,\x_2]_1).$$

If we choose the basis $\x_0,\x_1,\x_2$ of the vector space $\mathbb{K}[\x_0,\x_1,\x_2]_1$, then since there is no point of $\mathbb{P}^2$ where $\x_0,\x_1,\x_2$ all vanish simultaneously, this is basepoint-free. The $\varphi_L$ defined by this choice of basis is simply the identity.

In the case of the two conics, as we saw above, the base locus is not empty. In fact, the base locus is the four intersection points of $C_1\cap C_2$ already examined in [Example 3](#ex3), and geometrically each element of the pencil shares exactly these four intersection points of $C_1\cap C_2$, which matches the definition of base locus.
:::

The above example intuitively shows the origin of the name "basepoint," but since $\varphi_L$ is the identity, [Proposition 6](#prop6) does not have much meaning in this case. Let us look at a more non-trivial example.

::: Example 8
On $\mathbb{P}^1$ for $d \ge 1$, the map defined by the complete linear system $\lvert \mathcal{O}_{\mathbb{P}^1}(d) \rvert$ is

$$\nu_d: \mathbb{P}^1 \rightarrow \mathbb{P}^d, \quad [s : t] \mapsto [s^d : s^{d-1}t : \cdots : t^d].$$

This shows that the Veronese embedding examined in [§Projective Varieties, ⁋Example 16](/en/math/algebraic_varieties/projective_varieties#ex16) can be recovered in the language of complete linear systems.

For example, considering the hyperplane $H_0: \x_0 = 0$ in $\mathbb{P}^d$,

$$\nu_d^{-1}(H_0) = \{[s:t] \in \mathbb{P}^1 \mid s^d = 0\},$$

so scheme-theoretically this becomes the effective divisor $d\cdot[0:1]$ giving multiplicity $d$ at the point $[0:1]$. As another example, for the hyperplane $H_1: \x_0 - \x_d = 0$,

$$\nu_d^{-1}(H_1) = \{[s:t] \in \mathbb{P}^1 \mid s^d - t^d = 0\},$$

and if $\operatorname{char}\mathbb{K}\nmid d$, then $s^d - t^d$ factors into a product of $d$ distinct linear factors (for instance, if $\mathbb{K}=\mathbb{C}$, then $s^d-t^d=\prod_{k=0}^{d-1}(s-\zeta^k t)$), so $\nu_d^{-1}(H_1)$ is an effective divisor consisting of $d$ distinct points on $\mathbb{P}^1$. In any case, these preimages are degree $d$ effective divisors belonging to $\lvert \mathcal{O}_{\mathbb{P}^1}(d)\rvert$.
:::

## Ample Line Bundles

Although we are assuming that every variety is quasi-projective, in general a variety can be defined more abstractly. This approach has its pros and cons: the advantage is that our discussion becomes more flexible, and what we give up is that embedding a variety is no longer trivial.

For example, in our language, to say that $\mathbb{P}^1\times \mathbb{P}^1$ is a (quasi-projective) variety, we must embed it into some projective space. ([§Projective Varieties, ⁋Example 16](/en/math/algebraic_varieties/projective_varieties#ex16)) Instead, if we do not assume the existence of an ambient projective space in the definition of a variety, then $\mathbb{P}^1\times \mathbb{P}^1$ automatically becomes a variety without our having to show this, but it is unclear whether a general variety embeds into projective space.

However, even for abstract varieties, we can define line bundles, linear systems, and so on. Then in particular, using [Proposition 6](#prop6), we can define a suitable map to projective space. The importance of the following definition should be understood in this context.

::: Definition 9
A line bundle $\mathcal{L}$ (or the corresponding linear system $\lvert \mathcal{L} \rvert$) is called *very ample* if the regular map $\varphi_{\mathcal{L}}: X \rightarrow \mathbb{P}(\Gamma(X, \mathcal{L})^\ast)$ defined by the complete linear system $\lvert \mathcal{L} \rvert = \mathbb{P}(\Gamma(X, \mathcal{L}))$ is a closed embedding.
:::

Here, the target is the projectivization of the dual of $\Gamma(X, \mathcal{L})$ rather than its projectivization, because as seen in [Proposition 6](#prop6), the elements of the linear system correspond to hyperplanes in the target. Choosing a basis $s_0,\ldots,s_r$ of $\Gamma(X, \mathcal{L})$ and taking the dual basis as coordinates gives $\mathbb{P}(\Gamma(X, \mathcal{L})^\ast)\cong \mathbb{P}^r$, and in these coordinates $\varphi_{\mathcal{L}}$ is given by $x\mapsto [s_0(x):\cdots:s_r(x)]$. Since $\varphi_L$ differs from this by only an automorphism of $\mathbb{P}^r$ depending on the choice of basis, whether it is a closed embedding does not depend on the choice of basis.

The key point in the definition of very ample is that the map is not merely a morphism but a *closed* embedding. That is, as explained above, even in the world of abstract varieties, we can use this to define projective varieties, and moreover, using a very ample line bundle $\mathcal{L}$, we can represent $X$ with explicit coordinates in this ambient projective space.

We know that $\mathcal{O}_{\mathbb{P}^n}(1)$ is very ample, but $\mathcal{O}_{\mathbb{P}^n}(-1)$ is not. As examined in [§Line Bundles and Vector Bundles, ⁋Example 16](/en/math/algebraic_varieties/line_bundles#ex16), this is because the twisting direction of $\mathcal{O}_{\mathbb{P}^n}(-1)$ as the fiber moves along the base does not allow sections to cross the zero section, so no global sections exist. On the other hand, the twist possessed by $\mathcal{O}_{\mathbb{P}^n}(1)$ allows this, thereby ensuring the existence of global sections.

This example is overly simple, but if there were a space more complicated than $\mathbb{P}^n$ whose complexity could not be resolved by the twisting of a particular line bundle (even in the right direction), we could imagine adding more and more twists until it is resolved. From this imagination, we define the following.

::: Definition 10
$\mathcal{L}$ is called *ample* if there exists some $m > 0$ such that $\mathcal{L}^{\otimes m}$ is very ample.
:::

To see the usefulness of this definition, we should think of a space possessing a line bundle that is ample but not very ample, but it is still somewhat premature to introduce such a space. Before long, however, we will deal with such a space, and ampleness will then prove its worth in earnest.

---

**References**

**[Hart]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.

---

[^1]: We have already analyzed the *line at infinity* of $\mathbb{P}^2$ and its geometric intuition in [§Projective Varieties, ⁋Example 11](/en/math/algebraic_varieties/projective_varieties#ex11).
