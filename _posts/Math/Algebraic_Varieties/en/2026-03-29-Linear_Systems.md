---
title: "Linear Systems"
description: "We define the effectiveness conditions for Weil and Cartier divisors, and explain how to obtain linearly equivalent effective divisors from the nonzero global sections of the line bundle defined by a divisor."
excerpt: "Complete linear systems, base loci, and ampleness"

categories: [Math / Algebraic Varieties]
permalink: /en/math/algebraic_varieties/linear_systems
sidebar:
    nav: "algebraic_varieties-en"

date: 2026-03-29
weight: 11
translated_at: 2026-08-17T12:15:04+00:00
translation_source: kimi-cli
---
Previously, we defined a (Weil) divisor on a variety $X$ in [§Divisors, ⁋Definition 1](/en/math/algebraic_varieties/divisors#def1). By the definition of the Zariski topology, this can essentially be thought of as the zero set of some *function* defined on $X$, with the orders of these zeros added in, and to make this well defined even in cases such as $\mathbb{P}^n$, we generalized the *function* to a *section of a suitable line bundle*.

On the other hand, since divisors also allow negative coefficients, this zero set need not be a zero set at all; a zero of negative order, i.e., a pole, is also possible. In such cases, we can find an *effective* divisor linearly equivalent to the given divisor and then investigate this property. ([§Divisors, ⁋Definition 7](/en/math/algebraic_varieties/divisors#def7))

For convenience of exposition, we have discussed only Weil divisors above, but a similar argument can be made for Cartier divisors, and the resulting definition is as follows.

::: Definition 1
A Weil divisor $D=\sum n_i D_i$ defined on a variety $X$ is said to be *effective* if $n_i\geq 0$ for all $i$. A Cartier divisor $\{(U_i, f_i)\}$ is said to be *effective* if $f_i$ is regular on $U_i$ for all $i$.
:::

Our goal, then, is to examine whether any effective divisor exists in the divisor class of a divisor $D$. To this end, consider the line bundle $\mathcal{L}=\mathcal{O}_X(D)$ defined by $D$. ([§Line Bundles and Vector Bundles, ⁋Definition 17](/en/math/algebraic_varieties/line_bundles#def17)) Each nonzero global section $s\in \Gamma(X, \mathcal{L})$ of $\mathcal{L}$ has no poles, so it defines an effective divisor $\divisor(s)$, and we can check that this differs from the original $D$ only by a trivialization, so it is linearly equivalent to $D$. In other words, to find an effective divisor linearly equivalent to $D$, it suffices to look at the nonzero global sections of $\mathcal{O}_X(D)$. However, one must be careful: $\divisor(s)$ does not depend on a nonzero scalar multiple of $s$, and for this reason, the object of interest is not $\Gamma(X, \mathcal{L})$ itself but rather its projectivization.

::: Definition 2
For a line bundle $\mathcal{L}$ on a variety $X$, the *complete linear system* of $\mathcal{L}$ is the projectivization of the global section space $\Gamma(X, \mathcal{L})$ of $\mathcal{L}$,

$$\lvert \mathcal{L} \rvert = \mathbb{P}(\Gamma(X, \mathcal{L})).$$

A *linear system* for $\mathcal{L}$ is a nonempty projective subspace of $\lvert \mathcal{L} \rvert$. That is, for a subspace $V \subseteq \Gamma(X, \mathcal{L})$, it is of the form $\mathbb{P}(V) \subseteq \lvert \mathcal{L} \rvert$.
:::

## Linear systems on projective space

By the calculations following [§Line Bundles and Vector Bundles, ⁋Example 16](/en/math/algebraic_varieties/line_bundles#ex16), we saw that $\Gamma(\mathbb{P}^n, \mathcal{O}_{\mathbb{P}^n}(d))$ is isomorphic to the space of homogeneous polynomials of degree $d$, $\mathbb{K}[\x_0, \ldots, \x_n]_d$. Since each element of this space defines a degree $d$ hypersurface in $\mathbb{P}^n$, we can understand the complete linear system of $\mathcal{O}_{\mathbb{P}^n}(d)$

$$\lvert \mathcal{O}_{\mathbb{P}^n}(d)\rvert=\mathbb{P}(\Gamma(\mathbb{P}^n, \mathcal{O}_{\mathbb{P}^n}(d)))\cong \mathbb{P}(\mathbb{K}[\x_0,\ldots, \x_n]_d)\cong \mathbb{P}^{\binom{n+d}{d} - 1}$$

geometrically as a family of degree $d$ hypersurfaces in $\mathbb{P}^n$.

::: Example 3
For convenience, fix $n=2$. Then the family of degree $1$ hypersurfaces, i.e., lines in $\mathbb{P}^2$, is isomorphic to $\mathbb{P}^2$ itself. More precisely,

$$\lvert \mathcal{O}_{\mathbb{P}^2}(1)\rvert\cong \mathbb{P}(\mathbb{K}[\x_0,\x_1,\x_2]_1)\cong \mathbb{P}^{\binom{3}{1}-1}=\mathbb{P}^2,$$

and a point $[a_0:a_1:a_2]$ on the right-hand side $\mathbb{P}^2$ defines a line $Z(a_0\x_0+a_1\x_1+a_2\x_2)$ in $\mathbb{P}^2$.

For a slightly more complicated and geometric example, consider the complete linear system defined by the line bundle $\mathcal{O}_{\mathbb{P}^2}(2)$ on $\mathbb{P}^2$:

$$\lvert \mathcal{O}_{\mathbb{P}^2}(2)\rvert\cong \mathbb{P}(\mathbb{K}[\x_0,\x_1,\x_2]_2)\cong \mathbb{P}^{\binom{4}{2}-1}=\mathbb{P}^5.$$

We consider a $1$-dimensional subspace (i.e., a $1$-dimensional linear system) of this. A typical example is the *pencil* of two conics. Consider two conics $C_1=Z(F_1)$, $C_2=Z(F_2)$ defined in $\mathbb{P}^2$. Then, as long as $C_1$ and $C_2$ are not the same conic, their linear combination

$$Z(\lambda F_1+\mu F_2)$$

is another degree $2$ curve in $\mathbb{P}^2$, and by definition all these conics pass through $C_1\cap C_2$. Here, the point $[\lambda:\mu]\in \mathbb{P}^1$ parametrizes these conics.

For a more concrete example, consider the two conics in $\mathbb{P}^2$

$$C_1: Z((\x_0-2\x_2)^2+\x_1^2-9\x_2^2),\qquad C_2: Z((\x_0+2\x_2)^2+\x_1^2-9\x_2^2).$$

These expressions look complicated as they are, but when restricted to $U_2$, they become the equations of two circles

$$(\x-2)^2+\y^2=9,\qquad (\x+2)^2+\y^2=9.$$

On $U_2$, these meet at $(x,y)=(0,\pm\sqrt{5})$, computed from the two equations above, and outside $U_2$ (that is, on the *line at infinity*[^1] of $\mathbb{P}^2$) they meet at the two points $[1:i:0]$, $[1: -i:0]$. The pencil $Z(\lambda F_1+\mu F_2)$ above is then the collection of conics passing through this intersection $C_1\cap C_2$.

On the other hand, a general degree $2$ homogeneous polynomial is of the form

$$F(\x_0,\x_1,\x_2) = a_{00}\x_0^2 + a_{11}\x_1^2 + a_{22}\x_2^2 + a_{01}\x_0\x_1 + a_{02}\x_0\x_2 + a_{12}\x_1\x_2,$$

and this is exactly why $\Gamma(\mathbb{P}^2, \mathcal{O}_{\mathbb{P}^2}(2))$ is a $6$-dimensional space. On the other hand, if we add the condition that the set of four points $C_1\cap C_2$ computed above must be passed through, then each of these four points imposes one constraint, eliminating one parameter each, so we know that there are $2$ parameters needed to express this. More specifically, the following four conditions

$$0=F(0,\sqrt{5},1)=5a_{11}+a_{22}+\sqrt{5}a_{12}$$

$$0=F(0,-\sqrt{5},1)=5a_{11}+a_{22}-\sqrt{5}a_{12}$$

$$0=F(1,i,0)=a_{00}-a_{11}+ia_{01}$$

$$0=F(1,-i,0)=a_{00}-a_{11}-ia_{01}$$

force $a_{12}=0$, $a_{01}=0$, $5a_{11}=-a_{22}$, $a_{00}=a_{11}$, so the actual variables are the two $a_{00}$, $a_{02}$. That is, this collection of conics will form a $2$-dimensional subspace $V$ of $\Gamma(\mathbb{P}^2,\mathcal{O}_{\mathbb{P}^2}(2))$, and projectivizing this gives the $\mathbb{P}^1$ represented by $[\lambda:\mu]$.

{% diagram Math/Algebraic_Varieties/Linear_Systems-1.svg width="40em" alt="pencil_of_circles" %}
:::

Of course, [Definition 2](#def2) applies equally to any variety, whether $X$ is projective space or a quasi-projective variety. However, the reason we went to such lengths in computing [Example 3](#ex3) above is that for any quasi-projective variety $X\subseteq \mathbb{P}^n$, if $D$ comes from some $\mathcal{O}_{\mathbb{P}^n}(d)$, then the language of homogeneous polynomials can be used as is. That is, in this case the restriction map

$$\Gamma(\mathbb{P}^n, \mathcal{O}_{\mathbb{P}^n}(d)) \rightarrow \Gamma(X, \mathcal{O}_{\mathbb{P}^n}(d)\vert_X)$$

sends a homogeneous polynomial $F \in \mathbb{K}[\x_0, \ldots, \x_n]_d$ to a section on $X$, and its kernel is the degree $d$ homogeneous part $I(X)_d$ of $I(X)$. Therefore, if this restriction map is surjective, then

$$\Gamma(X, \mathcal{O}_{\mathbb{P}^n}(d)\vert_X) \cong \mathbb{K}[\x_0, \ldots, \x_n]_d / I(X)_d,$$

and essentially the same calculations as in $\mathbb{P}^n$ are possible. In fact, it is known that this surjectivity holds when $d$ is sufficiently large. In particular, since $F - G \in I(X)$ defines the same intersection, the parameter space becomes $\mathbb{P}(V/(V \cap I(X)))$.

## Base Locus

In the remainder of this post, given a linear system $L=\mathbb{P}(V)$ on $X$ and a basis $F_0,\ldots, F_r$ of $V$, we use this to define the embedding

$$\varphi_L:X\rightarrow \mathbb{P}^r;\qquad x\mapsto [F_0(x):\cdots:F_r(x)].$$

Of course, this is not always possible. For example, in [Example 3](#ex3), if we choose the following two bases corresponding to $(a_{00},a_{02})=(1,0), (0,1)$:

$$G_1(\x_0,\x_1,\x_2)=\x_0^2+\x_1^2-5\x_2^2, \qquad G_2(\x_0,\x_1,\x_2)=\x_0\x_2,$$

then this "embedding" becomes

$$\mathbb{P}^2\rightarrow \mathbb{P}^1;\qquad [\x_0:\x_1:\x_2]\mapsto [\x_0^2+\x_1^2-5\x_2^2:\x_0\x_2].$$

We already know that something is wrong because this is a map from $\mathbb{P}^2$ to the smaller space $\mathbb{P}^1$, and this is because there exists a locus where the two functions $G_1,G_2$ vanish simultaneously.

The embedding $\varphi_L$ above actually depends on the choice of basis of $V$, but many properties that $\varphi_L$ possesses do not. For example, as just mentioned, the points of $X$ where all bases vanish do not depend on the choice of basis.

To describe this rigorously, we define the *support* of a Weil divisor $D = \sum n_i D_i$ as $\operatorname{Supp}(D) = \bigcup_{n_i \neq 0} D_i$. That is, the support is the union of the prime divisors with nonzero coefficient in the divisor. Using this, the following is well defined.

::: Definition 4
The *base locus* $\operatorname{Bs}(L)$ of a linear system $L \subseteq \lvert \mathcal{L} \rvert$ is the closed subset shared by all elements of $L$. Specifically, when $L = \mathbb{P}(V)$ with $V \subseteq \Gamma(X, \mathcal{L})$,

$$\operatorname{Bs}(L) = \bigcap_{s \in V \setminus \{0\}} \operatorname{Supp}(\divisor(s)),$$

where $\divisor(s)$ is the zero divisor of the section $s$.
:::

In particular, in the calculation of hypersurfaces in $\mathbb{P}^n$, for $V \subseteq \mathbb{K}[\x_0, \ldots, \x_n]_d$, this is the same as $\operatorname{Bs}(L) = \bigcap_{[F] \in L} Z(F)$. Then the definition we wanted to make is the following.

::: Definition 5
$L$ is said to be *basepoint-free* if $\operatorname{Bs}(L) = \emptyset$. That is, for any point $p \in X$, there always exists an element of $L$ not passing through $p$.
:::

The key property of a basepoint-free linear system is as follows. If $L=\mathbb{P}(V)$ is basepoint-free, then a basis $F_0,\ldots,F_r$ of $V$ satisfies $\bigcap Z(F_i)\cap X=\emptyset$, so using this we can define the following regular map:

$$\varphi_L:X\rightarrow\mathbb{P}^r,\quad p\mapsto[F_0(p):\cdots:F_r(p)].$$

Our original interest in linear systems was to find, for a given divisor $D$, an effective divisor linearly equivalent to $D$, and the following proposition gives a direct answer to this.

::: Proposition 6
In the above situation, a hyperplane $H$ of $\mathbb{P}^r$ defines an effective divisor belonging to $L$.
:::

To verify this, it suffices to check that for a hyperplane $H: a_0\x_0+\cdots+a_r\x_r=0$ in $\mathbb{P}^r$, the preimage $\varphi_L^{-1}(H)$ coincides with the zero set of the global section

$$\sigma=a_0F_0+\cdots+a_rF_r\in V,$$

that is, with $\divisor(\sigma)$. Let us look at a more concrete example.

::: Example 7
Let us examine the two examples of $\mathbb{P}^2$ from [Example 3](#ex3). First, consider the complete linear system

$$\lvert \mathcal{O}_{\mathbb{P}^2}(1)\rvert=\mathbb{P}(\mathbb{K}[\x_0,\x_1,\x_2]_1).$$

Choosing the basis $\x_0,\x_1,\x_2$ for the vector space $\mathbb{K}[\x_0,\x_1,\x_2]_1$, there is no point in $\mathbb{P}^2$ where $\x_0,\x_1,\x_2$ all vanish simultaneously, so this is basepoint-free. The $\varphi_L$ defined by this choice of basis is simply the identity.

In the case of the base locus of the two conics, as we saw above, the base locus is not empty. In fact, the base locus is the four intersection points of $C_1\cap C_2$ already examined in [Example 3](#ex3), and geometrically, since each element of the pencil shares exactly these four intersection points of $C_1\cap C_2$, this matches the definition of the base locus.
:::

The above example intuitively shows the origin of the name basepoint, but since $\varphi_L$ is the identity, [Proposition 6](#prop6) does not actually have much meaning. Let us look at a more non-trivial example.

::: Example 8
For $d \ge 1$ on $\mathbb{P}^1$, the map defined by the complete linear system $\lvert \mathcal{O}_{\mathbb{P}^1}(d) \rvert$ is

$$\nu_d: \mathbb{P}^1 \rightarrow \mathbb{P}^d, \quad [s : t] \mapsto [s^d : s^{d-1}t : \cdots : t^d].$$

This shows that the Veronese embedding examined in [§Projective Varieties, ⁋Example 16](/en/math/algebraic_varieties/projective_varieties#ex16) can be recovered in the language of complete linear systems.

For example, considering the hyperplane $H_0: \x_0 = 0$ in $\mathbb{P}^d$,

$$\nu_d^{-1}(H_0) = \{[s:t] \in \mathbb{P}^1 \mid s^d = 0\},$$

so scheme-theoretically this becomes the effective divisor $d\cdot[0:1]$ giving multiplicity $d$ at the point $[0:1]$. As another example, for the hyperplane $H_1: \x_0 - \x_d = 0$,

$$\nu_d^{-1}(H_1) = \{[s:t] \in \mathbb{P}^1 \mid s^d - t^d = 0\},$$

and if $\operatorname{char}\mathbb{K}\nmid d$, then $s^d - t^d$ factors into a product of $d$ distinct linear factors (for example, if $\mathbb{K}=\mathbb{C}$, then $s^d-t^d=\prod_{k=0}^{d-1}(s-\zeta^k t)$), so $\nu_d^{-1}(H_1)$ is an effective divisor consisting of $d$ distinct points on $\mathbb{P}^1$. In any case, these preimages are degree $d$ effective divisors belonging to $\lvert \mathcal{O}_{\mathbb{P}^1}(d)\rvert$.
:::

## Ample line bundle

Although we are assuming that every variety is quasi-projective, varieties can generally be defined more abstractly. This approach has its pros and cons: the good point is that our discussion becomes more flexible, and what we give up is that embedding a variety is no longer trivial.

For example, in our language, to say that $\mathbb{P}^1\times \mathbb{P}^1$ is a (quasi-projective) variety, we must embed it into some projective space. ([§Projective Varieties, ⁋Example 16](/en/math/algebraic_varieties/projective_varieties#ex16)) Instead, if we do not assume the existence of an ambient projective space in the definition of a variety, then $\mathbb{P}^1\times \mathbb{P}^1$ automatically becomes a variety without our having to show this, but it is unclear whether a general variety embeds into projective space.

However, even on an abstract variety, we can define line bundles, linear systems, and so on. Then in particular, using [Proposition 6](#prop6), we can define a suitable map to projective space. The importance of the following definition should be understood in this context.

::: Definition 9
A line bundle $\mathcal{L}$ (or the corresponding linear system $\lvert \mathcal{L} \rvert$) is said to be *very ample* if the regular map $\varphi_{\mathcal{L}}: X \rightarrow \mathbb{P}(\Gamma(X, \mathcal{L})^\ast)$ defined by the complete linear system $\lvert \mathcal{L} \rvert = \mathbb{P}(\Gamma(X, \mathcal{L}))$ is a closed embedding.
:::

Here, the reason the target is the projectivization of the dual of $\Gamma(X, \mathcal{L})$, rather than the projectivization of $\Gamma(X, \mathcal{L})$ itself, is that, as we saw in [Proposition 6](#prop6), the elements of the linear system correspond to the hyperplanes of the target. Choosing a basis $s_0,\ldots,s_r$ of $\Gamma(X, \mathcal{L})$ and taking the dual basis as coordinates, we get $\mathbb{P}(\Gamma(X, \mathcal{L})^\ast)\cong \mathbb{P}^r$, and in these coordinates $\varphi_{\mathcal{L}}$ is given by $x\mapsto [s_0(x):\cdots:s_r(x)]$. Since $\varphi_L$ differs by an automorphism of $\mathbb{P}^r$ depending on the choice of basis, whether this is a closed embedding does not depend on the choice of basis.

The key point in the definition of very ample is that the map is not merely a morphism but a *closed* embedding. That is, as explained above, even in the world of abstract varieties, we can use this to define a projective variety, and moreover, using a very ample line bundle $\mathcal{L}$, we can express $X$ in explicit coordinates in this ambient projective space.

We know that $\mathcal{O}_{\mathbb{P}^n}(1)$ is very ample, but $\mathcal{O}_{\mathbb{P}^n}(-1)$ is not. As examined in [§Line Bundles and Vector Bundles, ⁋Example 16](/en/math/algebraic_varieties/line_bundles#ex16), this is because the twisting direction of $\mathcal{O}_{\mathbb{P}^n}(-1)$ as the fiber moves along the base does not allow sections to cross the zero section, so no global sections exist. On the other hand, the twisting of $\mathcal{O}_{\mathbb{P}^n}(1)$ allows this, giving rise to global sections.

This example is too simple, but if there is a space more complicated than $\mathbb{P}^n$ whose complexity cannot be resolved by the twisting of a particular line bundle alone (even if in the right direction), we can imagine adding more and more twisting until it is resolved. From this imagination, we define the following.

::: Definition 10
$\mathcal{L}$ is said to be *ample* if there exists some $m > 0$ such that $\mathcal{L}^{\otimes m}$ is very ample.
:::

To see the usefulness of this definition, one should think of a space having a line bundle that is ample but not very ample, but it is still somewhat premature to introduce such a space. However, before long we will deal with such a space, and ampleness will then prove its full worth.

## General elements

An element of a linear system is a nonzero section modulo scalar multiplication ([Definition 2](#def2)), and what each element actually gives us is the zero locus of that section. Then it is natural to ask what kind of space this zero locus looks like. Looking again at the pencil of [Example 3](#ex3), this is generated by $G_1=\x_0^2+\x_1^2-5\x_2^2$ and $G_2=\x_0\x_2$, so its elements are the conics $Z(\lambda G_1+\mu G_2)$. The determinant of the symmetric matrix corresponding to this quadratic form is $-\lambda(20\lambda^2+\mu^2)/4$, and a conic is singular exactly when this value is $0$, so the bad elements are only when $[\lambda:\mu]$ is one of the three points $[0:1]$, $[1:\pm 2\sqrt{5}i]$. For example, the element with $\lambda=0$ splits into two lines $Z(\x_0)$ and $Z(\x_2)$ and has a singular point at their intersection. All other elements are smooth conics, and what we want to know is the property that *almost all* elements have in this way.

If $\mathcal{L}$ is very ample, this question translates into a question about hyperplanes. Through $\varphi_{\mathcal{L}}$, $X$ becomes a closed subvariety of $\mathbb{P}^N = \mathbb{P}(\Gamma(X,\mathcal{L})^\ast)$, and by [Proposition 6](#prop6), the elements of $\lvert \mathcal{L}\rvert$ are exactly the traces $X\cap H$ of hyperplanes $H\subseteq \mathbb{P}^N$ on $X$. That is, $\lvert \mathcal{L}\rvert$ is identified with the dual projective space $(\mathbb{P}^N)^\ast$, and so our question becomes one of how a general hyperplane cuts $X$. The answer to this is the following theorem.

::: Proposition 11 (Bertini's theorem)
For a projective variety $X\subseteq \mathbb{P}^N$, there exists a dense open subset $U$ of the dual projective space $(\mathbb{P}^N)^\ast$ such that for every $H\in U$, the following hold.

1. The singular points of $X\cap H$ are all singular points of $X$. In particular, if $X$ is smooth, then $X\cap H$ is also smooth.
2. If $\dim X\geq 2$, then $X\cap H$ is irreducible.
:::

The first result intuitively means the following. For $H$ to create a singular point of $X\cap H$ at a smooth point $x$ of $X$ is the same as $H$ being tangent to $X$ at $x$, and if we let $n=\dim X$, then the hyperplanes tangent at a fixed $x$ form a subspace of dimension $(N-n-1)$ inside $(\mathbb{P}^N)^\ast$, so even collecting these over all $x\in X$, the dimension is at most $N-1$. That is, the hyperplanes tangent to $X$ somewhere cannot fill the $N$-dimensional $(\mathbb{P}^N)^\ast$, and the remainder is the dense open subset we seek. To make this rigorous, one must actually measure the dimension of the incidence variety formed by collecting such $H$, and the irreducibility of the second result is a deeper fact, so we will take both results without proof.

Henceforth, we will call an element belonging to some dense open subset of a linear system a "general element" of that linear system. Then, translating the above proposition back into the original language, we obtain the following.

::: Corollary 12
For a smooth projective variety $X$ and a very ample line bundle $\mathcal{L}$, a general element of the complete linear system $\lvert \mathcal{L}\rvert$ is smooth, and if $\dim X\geq 2$, it is irreducible.
:::

::: Proof
By [Definition 9](#def9), $\varphi_{\mathcal{L}}$ is a closed embedding, so we can view $X$ as a closed subvariety of $\mathbb{P}^N$, and by [Proposition 6](#prop6), under this identification the elements of $\lvert \mathcal{L}\rvert$ are of the form $X\cap H$ for a hyperplane $H$. Applying [Proposition 11](#prop11) to this gives the result.
:::

---

**References**

**[Hart]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.

---

[^1]: The *line at infinity* of $\mathbb{P}^2$ and its geometric intuition have already been analyzed in [§Projective Varieties, ⁋Example 11](/en/math/algebraic_varieties/projective_varieties#ex11).
