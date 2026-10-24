---
title: "Differential Modules"
description: "This post covers derivations on graded algebras and their functorial properties, and examines the definition of differential modules and the structure of related exact sequences."
excerpt: "Differential modules with derivations on graded algebras"

categories: [Math / Multilinear Algebra]
permalink: /en/math/multilinear_algebra/differential_modules
sidebar: 
    nav: "multilinear_algebra-en"

date: 2025-04-18
weight: 15
translated_at: 2026-06-01T19:30:01+00:00
translation_source: kimi-cli
last_polished_at: 2026-10-24T23:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
Now we define differential modules. For this we need a simple lemma; first consider the second case assumed after [§Derivations, ⁋Definition 2](/en/math/multilinear_algebra/derivations#def2){: data-lid="tonzh" }. That is, we will consider a commutative ring $A$, a $\Delta$-graded $A$-algebra $E$, a graded $A$-module $F$, and an $\varepsilon$-derivation $d:E \rightarrow F$. 

## Functoriality of Derivations

In addition to the above assumptions, we assume that every algebra appearing in this section is unital associative, and that all algebra homomorphisms are unital. 

::: Proposition 1
Suppose two associative unital graded $A$-algebras $E,F$ are given, and let $M$ be a graded $(E,E)$-bimodule, and $N$ a graded $(F,F)$-bimodule. Then, given a graded $A$-algebra homomorphism $\rho: E \rightarrow F$ and a degree $0$ graded $E$-homomorphism $\theta: M \rightarrow N$ of the $E$-bimodules defined by $\rho$, the following hold:

1. For any $\varepsilon$-derivation $d': F \rightarrow N$, $d'\circ\rho: E \rightarrow \rho^\ast N$ is also an $\varepsilon$-derivation of the same degree. 
2. For any $\varepsilon$-derivation $d: E \rightarrow M$, $\theta\circ d: E \rightarrow \rho^\ast N$ is also an $\varepsilon$-derivation of the same degree.
:::

The proof of this is obvious from the definition of $\rho^\ast$. Meanwhile, in such a situation we can also endow $F$ with an $(E,E)$-bimodule structure. It is then natural to examine when $d':F \rightarrow N$ is also (left/right) $E$-linear. 

::: Proposition 2
Assuming the situation of [Proposition 1](#prop1){: data-lid="u3lh3" }, let an $\varepsilon$-derivation $d': F \rightarrow N$ be given. Then $d'$ is left (resp. right) $E$-linear if and only if $d'$ is, on the subalgebra of $F$, $\rho(E)$, identically $0$. 
:::

Now let us define $\Der_A(F, N)$ to be the collection of derivations from $F$ to $N$ that are $A$-derivations. Then the collection of derivations satisfying the condition of [Proposition 2](#prop2){: data-lid="l73b2" } and becoming $E$-linear coincides with the collection of derivations identically zero on $\rho(E)$, so this collection forms, in $\Der_A(F, N)$, an $A$-submodule. Let us denote this by $\Der_E(F,N)$. 

Furthermore, suppose three graded $A$-algebras $E,F,G$ are given, and graded $A$-algebra homomorphisms $\rho: E \rightarrow F$, $\sigma: F \rightarrow G$ are given. Then for any graded $(G,G)$-bimodule $H$, for the following three $A$-modules

$$\Der_E(F, \sigma^\ast H),\qquad \Der_F(G,H),\qquad\Der_E(G, H)$$

it is obvious that

$$0 \rightarrow \Der_F(G, H) \rightarrow \Der_E(G,H) \rightarrow \Der_E(F, \sigma^\ast H)$$

is exact. 

For any $\Delta$-graded $A$-module $M$ and $\delta\in \Delta$, define $M[\delta]$ by the following formula:

$$(M[\delta])_\mu=M_{\delta+\mu}$$

Then, since the $\Delta$-graded $A$-module $E\oplus M[\delta]$ exists, now for a homogeneous element $x\in E$ and elements of $E\oplus M[\delta]$, $(x,y), (x',y')$, obtained using it, we can use the following formula

$$(x,y)(x',y')=(xx', yx'+\varepsilon(\delta, \deg x)xy')$$

to endow $E\oplus M[\delta]$ with a graded $A$-algebra structure. In this case, we call the projection map $\epsilon: E\oplus M[\delta] \rightarrow E$ the *augmentation map*, and we know that this is a graded $A$-algebra homomorphism. 

Now, if a degree $0$ graded $A$-linear map $g:E \rightarrow E\oplus M[\delta]$ satisfies $\epsilon\circ g=\id_E$, then by definition we know that for some degree $\delta$ graded $A$-linear map $f:E \rightarrow M$ it must be of the form $x\mapsto (x,f(x))$, and conversely, any degree $\delta$ $A$-linear map $f$ defines a $g$ satisfying the above condition. 

Then the following proposition is also the result of a simple calculation.

::: Proposition 3
A graded $A$-linear map $f: E \rightarrow M$ of degree $\delta$ is an $\varepsilon$-derivation if and only if the map $x \mapsto (x, f(x))$ from $E$ to $E \oplus M[\delta]$ is a graded $A$-algebra homomorphism.
:::

Meanwhile, for the next section as well, we need to examine when the graded $A$-algebra $E\oplus M[\delta]$ defined above is associative and unital.

::: Proposition 4
In the above situation, $E \oplus M[\delta]$ is an associative unital algebra if and only if $E$ is associative unital and the two maps $(a, x) \mapsto a \cdot x$ and $(a, x) \mapsto x \cdot a$ define on $M$ an $(E, E)$-bimodule structure. In this case, $E \oplus M[\delta]$ has unity $(1, 0)$.
:::

## Tensor Algebra and Derivations

The exterior algebra, which appeared as an important example in the previous post, is obtained in the following more general setting.

::: Proposition 5
For a commutative ring $A$ and an $A$-module $M$, let $B$ be one of $B=\T(M)$, $\S(M)$, or $\bigwedge(M)$, and let a $(B,B)$-bimodule $E$ be given. Also, suppose that a derivation $d_0: A \rightarrow E$ and an abelian group homomorphism $d_1: M \rightarrow E$ satisfy the following condition:

$$d_1(ax)=ad_1(x)+d_0(a)x$$

If $B=\S(M)$, we additionally assume the following condition:

$$xd_1(y)+d_1(x)y=yd_1(x)+d_1(y)x$$

and if $B=\bigwedge(M)$, we additionally assume the following condition:

$$xd_1(x)+d_1(x)x=0$$

Then, regarding $B$ as a $\mathbb{Z}$-algebra, from $B$ to $E$ there exists a unique derivation $d$ such that $d\vert_A = d_0$ and $d\vert_M = d_1$.
:::
::: Proof
First, define multiplication on the abelian group $B \oplus E$ by the formula

$$(b, t)(b', t') = (bb', bt' + b't)$$

and regard this as an associative $\mathbb{Z}$-algebra. Then via the canonical injection $t\mapsto (0,t)$, we can identify $E$ with a two-sided ideal of the $\mathbb{Z}$-algebra $B\oplus E$, and in this case $E^2=0$.

On the other hand, if we define $h_0: A \rightarrow B \oplus E$ by $h_0(a) = (a, d_0(a))$, this is a (unital) ring homomorphism by [Proposition 3](#prop3){: data-lid="lmyod" }, and via this $B \oplus E$ becomes an $A$-algebra. Now, after endowing $B\oplus E$ with this $A$-module structure, consider the function defined by $h_1(x) = (x, d_1(x))$, namely $h_1: M \rightarrow B\oplus E$. Then by the given condition, the formula

$$h_1(ax) = h_0(a) h_1(x)$$

holds, so $h_1$ from $M$ to $B\oplus E$ is an $A$-linear map. Therefore, using the given assumptions and by the universal property of $\T(M)$, $\S(M)$, or $\bigwedge(M)$, we obtain, satisfying $h\vert_M=h_1$, a unique $A$-algebra homomorphism $h:B \rightarrow B\oplus E$. Meanwhile, we can easily check that composing $h$ with the augmentation map $B\oplus E \rightarrow B$ yields $\id_B$, so again by [Proposition 3](#prop3){: data-lid="azrty" }, there exists, satisfying $h(b)=(b,\dd{(b)})$, a unique derivation $d:B \rightarrow E$, and from this we obtain the desired result.
:::

## Universal property

In this section, every algebra is assumed to be associative unital, and all algebra homomorphisms are assumed to be unital.

For any $A$-algebra $E$, $E\otimes_AE$ has, via multiplication by elements of $E$ on both sides, an $(E,E)$-bimodule structure. Meanwhile, considering the multiplication map of $E$,

$$m: E\otimes_AE \rightarrow E$$

it is obvious that $m$ preserves this $(E,E)$-bimodule structure. Therefore, we can consider the kernel of $m$, $\mathfrak{I}$, which, within $E\otimes_AE$, is a sub-$(E,E)$-bimodule. Then the following lemma is a simple calculation.

::: Lemma 6
The map $\delta_E: x \mapsto x \otimes 1 - 1 \otimes x$ from $E$ to $\mathfrak{I}$ is an $A$-derivation. Moreover, $\mathfrak{I}$ is generated as a left $E$-module by the image of $\delta_E$.
:::
::: Proof
First, the first claim follows because the following calculation

$$(xy)\otimes 1-1\otimes(xy)=(x\otimes 1-1\otimes x)y+x(y\otimes 1-1\otimes y)$$

holds. Now suppose in general that an arbitrary element of $\mathfrak{I}$, $\sum_i x_i\otimes y_i$, is given. That is, $\sum_i x_iy_i=0$. Now from this, since the following formula

$$\sum_i x_i\otimes y_i=\sum_i \left(x_i(1\otimes y_i)-(x_iy_i)\otimes 1\right)=\sum_i x_i(1\otimes y_i-y_i\otimes 1)$$

is obtained, the second claim is also immediate.
:::

From this we now obtain the following universal property.

::: Proposition 7
The $\delta_E$ obtained in [Lemma 6](#lem6){: data-lid="ogpuq" } satisfies the following universal property. 

> For every $(E,E)$-bimodule $M$ and every $A$-derivation $d: E \rightarrow M$, there exists a unique $(E,E)$-bimodule homomorphism $f: \mathfrak{I} \rightarrow M$ such that $d=f\circ\delta_E$. 
:::
::: Proof
First, by [Proposition 1](#prop1){: data-lid="ntesk" } we know that for every $(E, E)$-bimodule homomorphism $f: \mathfrak{I} \rightarrow M$, $f \circ \delta_E$ is an $A$-derivation from $E$ to $M$.

On the other hand, for uniqueness, from the definition of $\delta_E$ we know that

$$f(x \otimes 1 - 1 \otimes x) = \dd{x}$$

must hold, and since by [Lemma 6](#lem6){: data-lid="ip4fi" } $\mathfrak{I}$ is uniquely generated by the image of $\delta_E$, any $f$ satisfying the given condition must be unique if it exists. Additionally, using the calculation in the preceding lemma, we know that for any $\sum x_i \otimes y_i\in \mathfrak{I}$ the formula

$$f\left( \sum_i x_i \otimes y_i \right) = \sum_i x_i  f(1 \otimes y_i - y_i \otimes 1) = - \sum_i x_i  \dd{y_i}$$

must necessarily hold. Therefore, to show existence we must show that this is an $(E,E)$-bimodule homomorphism. For this, since the mapping $(x, y) \mapsto -x \cdot \dd{y}$ is an $A$-bilinear mapping from $E\times E$ to $M$, from this we know that an $A$-linear map $g: E \otimes E \rightarrow M$ is defined by $g(x \otimes y) = -x \cdot \dd{y}$. Now it is sufficient to show that the restriction of this $g$ is $f$ and that this preserves the $E$-bimodule structure, which is a simple calculation. 
:::

By the above proposition, we obtain a canonical $A$-module isomorphism 

$$\Hom_{(E, E)}(\mathfrak{I}, M) \rightarrow \Der_A(E, M)$$

That is, the $(E,E)$-bimodule $\mathfrak{I}$ can be thought of as a representation of the $A$-derivations from $E$ to $M$.

If in addition to this, $E$ is a *commutative* $A$-algebra, then we can find a representation of the derivations from $E$ to $M$ in $\lMod{E}$. 

First consider $E\otimes_AE$. In the preceding argument, the $(E,E)$-bimodule structure defined on $E\otimes_AE$ was given by the formula

$$x(u\otimes v)y=(xu)\otimes(vy)$$

If $E$ were commutative as in our present assumption, then $E\otimes_AE$ is a (commutative) ring, and from the formula

$$x(u\otimes v)y=(xu)\otimes(vy)=(x\otimes y)(u\otimes v)$$

we see that this bimodule structure is in fact the same as the ring structure of $E\otimes_AE$. Therefore $\mathfrak{I}$ is an ideal of $E\otimes_AE$. 

Now let us assume a better situation. That is, suppose this time that $E$ is a *commutative* $A$-algebra. Then any $E$-module $M$ can be viewed as an $(E,E)$-bimodule. Meanwhile, the $(E,E)$-bimodule structure of $E\otimes_AE$ appearing above is, in this case, given by the multiplication of $E\otimes_AE$, and therefore $\mathfrak{I}$, which was a sub-$(E,E)$-bimodule of $E\otimes_AE$, is now an ideal of $E\otimes_AE$. Furthermore, since the multiplication map $m$ of the ring is surjective, we obtain the canonical isomorphism

$$(E\otimes_AE)/\mathfrak{I}\cong E$$

On the other hand, any $E$-module $M$ can be regarded as an $(E,E)$-bimodule by viewing its action as both a left action and a right action. On the other hand, if we view the $E$-module $M$ as an $E\otimes_AE$-module $M$ via the multiplication map $m:E\otimes_AE \rightarrow E$, then from the following adjoint

$$\Hom_{(E,E)}(\mathfrak{I}, M) \rightarrow \Hom_{E\otimes_AE}(\mathfrak{I}, M)$$

we obtain the following isomorphisms

$$\Hom_{E\otimes_AE}(\mathfrak{I}, M)\cong \Hom_{(E,E)}(\mathfrak{I}, M)\cong\Der_A(E, M)$$

Now in addition to this, we further show that 

$$\Hom_E(\mathfrak{I}/\mathfrak{I}^2, M)\cong \Hom_{E\otimes_AE}(\mathfrak{I}, M)\cong \Hom_{(E,E)}(\mathfrak{I}, M)\cong\Der_A(E, M)$$

First, for any $z\in M$ and any generator $1\otimes x-x\otimes1$ of $\mathfrak{I}$, let us view $M$ as an $E\otimes_AE$-module as above. Then the commutativity of $E$ gives the formula

$$(1\otimes x-x\otimes1)z=0$$

so $\mathfrak{I}M=0$. Therefore $\mathfrak{I}$ belongs to the annihilator of the $E\otimes_AE$-module $M$, and hence $M$ can be treated as an $(E\otimes_AE)/\mathfrak{I}$-module. Meanwhile, replacing the $E\otimes_AE$-module $\mathfrak{I}$ accordingly by the formula

$$((E\otimes_AE)/\mathfrak{I})\otimes_{E\otimes_AE}\mathfrak{I}\cong\mathfrak{I}/\mathfrak{I}^2$$

we obtain the desired claim from this. That is, the following holds.

::: Proposition 8
Consider a commutative $A$-algebra $E$, the multiplication map $m:E\otimes_AE \rightarrow E$, and the kernel $\mathfrak{I}$ of $m$. Then via the canonical isomorphism

$$(E\otimes_AE)/\mathfrak{I}\cong E$$

let us endow $\mathfrak{I}/\mathfrak{I}^2$ with an $E$-module structure. 

On the other hand, if we define $\delta_{E/A}: E \rightarrow \mathfrak{I}/\mathfrak{I}^2$ by the formula

$$x\mapsto (x\otimes 1-1\otimes x)+\mathfrak{I}^2$$

then $\delta_{E/A}$ is an $A$-derivation and satisfies the following universal property. 

> For any $E$-module $M$ and any $A$-derivation $D:E \rightarrow M$, there exists a unique $E$-linear map $g:\mathfrak{I}/\mathfrak{I}^2 \rightarrow M$ such that $D=g\circ\delta_{E/A}$. 
:::

::: Definition 9
The $E$-module $\mathfrak{I}/\mathfrak{I}^2$ is called the ($E$-)module of *$A$-differentials*, and is denoted by $\Omega_{A}(E)$ or $\Omega_{E/A}$. Also, we write $\delta_{E/A}(x)$ as $d_{E/A}(x)$, and when there is no danger of confusion we simply write this as $\dd{x}$. For each $x \in E$, we call $d_{E/A}(x)$ the *differential* of $x$.
:::

Therefore, we obtain the canonical isomorphism

$$\Hom_E(\Omega_{E/A}, N)\cong\Der_A(E, N)$$

::: Example 10
Let a commutative ring $A$ and an $A$-module $M$ be given. Then the symmetric algebra $\S(M)$ is a commutative $A$-algebra. Therefore, whenever an $\S(M)$-module $N$ and an $A$-derivation $D:\S(M)\rightarrow N$ are given, for the following formula

$$D=g\circ d_{\S(M)/A}$$

to hold, there exists a unique $\S(M)$-linear map $g:\Omega_{\S(M)/A}\rightarrow N$. 

Meanwhile, when any $A$-derivation $D:\S(M)\rightarrow L$ is given, we can verify through [Proposition 5](#prop5){: data-lid="lt3ji" } that its restriction to $M$, $D\vert_M$, is an $A$-module homomorphism from $M$ to $L$, and that this correspondence $D\mapsto D\vert_M$ is in fact an $\S(M)$-module isomorphism. On the other hand, since $L$ is an $\S(M)$-module, by [\[Algebraic Structures\] §Change of Scalars, ⁋Proposition 6](/en/math/algebraic_structures/change_of_base_ring#prop6){: data-lid="pg8g9" } we have 

$$\Hom_{\S(M)}(M\otimes_A\S(M),L)\cong\Hom_A(M,L)$$

and combining these, we know that for any $A$-derivation $D:\S(M)\rightarrow L$, extending the canonical homomorphism

$$M\rightarrow M\otimes_A\S(M);\qquad x\mapsto x\otimes1$$

yields an $A$-derivation $D_0$ such that, for a suitable $h\in \Hom_{\S(M)}(M\otimes_A\S(M),L)$, $D$ can be written in the form $D=h\circ D_0$. 

By a simple calculation, in the first calculation when $N=M\otimes_A\S(M)$, the obtained $\S(M)$-linear map $\Omega_{\S(M)/A}\rightarrow M\otimes_A\S(M)$ and, in the second calculation when $L=\Omega_A(\S(M))$, the obtained $h$ are inverses of each other; hence we know that the isomorphism

$$\Omega_{\S(M)/A}\cong M\otimes_A\S(M)$$

holds, and moreover, if we write this isomorphism as $\omega:M\otimes_A\S(M)\rightarrow\Omega_{\S(M)/A}$, then for any $x\in M$ we know that $\omega(x\otimes1)=d_{\S(M)/A}(x)=\dd{x}$. 

In particular, if $M$ is a free $A$-module of finite rank $n$, then $\S(M)$ can be identified with the polynomial algebra $A[\x_1,\ldots, \x_n]$, and under this identification the $\dd{\x_i}$ are *really* the images of the $\x_i$ under $d=d_{\S(M)/A}$; moreover, if the image of a polynomial $p\in A[\x_1,\ldots, \x_n]$ under $d$ is expressed as a linear combination of the $\Omega_{\S(M)/A}$ basis elements $\dd{\x_i}$, then the coefficients attached to them are precisely $p$'s $i$-th partial derivatives $\partial p/\partial \x_i$. 
:::

Now let us prove properties of $\Omega_{E/A}$. From now on, every ring is commutative, every algebra is an associative, commutative, unital algebra, and every algebra homomorphism is unital.

::: Proposition 11
Suppose that the following commutative diagram

{% diagram Math/Multilinear_Algebra/Differential_Modules-1.svg width="6.35em" alt="change_of_base_ring-1" %}

is given, and let us regard $E,E'$ as $A,A'$-algebras, respectively, via the vertical maps. Then there exists a unique $A$-linear mapping

$$\nu: \Omega_{E/A} \rightarrow \Omega_{E'/A'}$$

making the following diagram commute:

{% diagram Math/Multilinear_Algebra/Differential_Modules-2.svg width="11.54em" alt="change_of_base_ring-2" %}
:::
::: Proof
The proof is nothing but an appropriate use of the other universal properties employed in proving [Proposition 8](#prop8){: data-lid="5h9gb" }.
:::

From this we see that if we regard $\Omega$ as the correspondence taking an $A$-algebra $A \rightarrow E$ to the module of its differentials $\Omega_A(E)$, then $\Omega$ also possesses functoriality.

On the other hand, since $\Omega_{A'}(E')$ is an $A'$-module, by [\[Algebraic Structures\] §Change of Scalars, ⁋Proposition 6](/en/math/algebraic_structures/change_of_base_ring#prop6){: data-lid="fznhe" } we obtain from [Proposition 11](#prop11){: data-lid="0d3dl" } the following $A'$-linear map

$$\Omega_0(u):\Omega_A(E)\otimes_E E'\rightarrow\Omega_{A'}(E')$$

and if we let $i_E$ be the canonical morphism $\Omega_A(E)\rightarrow \Omega_A(E)\otimes_EE'$, we know that $\Omega(u)=\Omega_0(u)\circ i_E$.

Meanwhile, considering the isomorphism

$$\Hom_E(\Omega_A(E), M)\cong\Der_A(E, M)$$

given by the universal property of [Proposition 8](#prop8){: data-lid="w5u4e" }, we obtain the following commutative diagram:

{% diagram Math/Multilinear_Algebra/Differential_Modules-3.svg width="29.41em" alt="change_of_base_ring-3" %}

Here the vertical map on the right is the composite of the above isomorphism and the isomorphism of [\[Algebraic Structures\] §Change of Scalars, ⁋Proposition 6](/en/math/algebraic_structures/change_of_base_ring#prop6){: data-lid="mrxt7" },

$$\Hom_{E'}(\Omega_A(E)\otimes_EE', N) \rightarrow \Hom_E(\Omega_A(E), N)\rightarrow\Der_A(E, N)$$

and the horizontal map at the bottom is the map obtained from the functoriality of $\Der$:

$$\Der_{A'}(E', N) \rightarrow \Der_A(E, N);\qquad D\mapsto D\circ u$$

which we write as $C(u)$.

::: Proposition 12
Let $E' = E \otimes_AA'$, and let $\eta' : A' \rightarrow E'$ and $u : E \rightarrow E'$ be the canonical morphisms. Then the $A'$-linear map

$$\Omega_0(u) : \Omega_{E/A}\otimes_EE'\rightarrow\Omega_{E'/A'}$$

is an isomorphism.
:::
::: Proof
First, since the vertical maps are all isomorphisms, if we show that $C(u)$ is an isomorphism, we know that for any $N$,

$$\Hom_{E'}(\Omega_{E'/A'} , N) \rightarrow \Hom_{E'}(\Omega_{E/A}\otimes_EE',N)$$

is an isomorphism. That is, the following sequence

$$0\rightarrow\Hom_{E'}(\Omega_{E'/A'} , N) \rightarrow \Hom_{E'}(\Omega_{E/A}\otimes_EE',N)\rightarrow 0$$

is exact for any $N$. Now since $\Hom$ is a left exact functor ([§Projective, Injective, and Flat Modules, ⁋Proposition 2](/en/math/multilinear_algebra/various_modules#prop2){: data-lid="mvd8r" }), that the above sequence is exact for all $N$ is equivalent to the following sequence

$$0 \rightarrow\Omega_{E/A}\otimes_EE'\rightarrow\Omega_{E'/A'}\rightarrow 0$$

being exact. Therefore, to prove the claim it suffices to show that $C(u)$ is bijective.

First,

$$\Hom(u, \id_N):\Hom_{A'}(E\otimes_AA', N) \rightarrow \Hom_A(E, N)$$

is an isomorphism, and since $C(u)$ is nothing but its restriction to $\Der_{A'}(E', N)$, it is obvious that $C(u)$ is injective. That $C(u)$ is surjective can also be proved without difficulty.
:::

In particular, consider the case where $A=A'$ and $\rho:A \rightarrow A'$ is $\id_A$, and therefore $u:E\rightarrow E'$ is an $A$-algebra homomorphism. Then through the above process $u$ induces an $E'$-linear homomorphism

$$\Omega_0(u): \Omega_{E/A}\otimes_EE'\rightarrow\Omega_{E'/A}$$

On the other hand, if we regard $E'$ as an $E$-algebra using $E\rightarrow E'$, then since the derivation $d_{E'/E}: E' \rightarrow\Omega_{E'/E}$ obtained here is also an $A$-derivation, by the universal property of $\Omega_{E'/A}$ there exists the following factorization

$$E'\overset{d_{E'/A}}{\rightarrow}\Omega_{E'/A}\overset{\Omega_u}{\rightarrow}\Omega_{E'/E}$$

Then again by the universal property, there exists the following commutative diagram:

{% diagram Math/Multilinear_Algebra/Differential_Modules-4.svg width="25.13em" alt="change_of_base_ring-4" %}

Now we introduce two frequently used exact sequences.

::: Proposition 13
The sequence of $E'$-modules

$$\Omega_A(E)\otimes_EE'\overset{\Omega_0(u)}{\rightarrow}\Omega_{E'/A}\overset{\Omega_u}{\rightarrow}\Omega_{E'/E}\rightarrow0$$

is exact.
:::
::: Proof
Again from the fact that $\Hom$ is a left exact functor ([§Projective, Injective, and Flat Modules, ⁋Proposition 2](/en/math/multilinear_algebra/various_modules#prop2){: data-lid="54shr" }), it suffices to show that the sequence

$$0 \rightarrow \Hom_{E'}(\Omega_{E'/E},N) \rightarrow \Hom_{E'}(\Omega_{E'/A}, N) \rightarrow \Hom_{E'}(\Omega_{E/A}\otimes_EE',N)$$

is exact for any $E'$-module $N$. However, using the commutative diagrams used before and after [Proposition 12](#prop12){: data-lid="gergw" }, we can convert this into the sequence of modules of derivations

$$0 \rightarrow \Der_E(E', N) \rightarrow \Der_A(E', N) \rightarrow \Der_A(E, N)$$

and we showed immediately after [Proposition 2](#prop2){: data-lid="psha7" } that this is exact.
:::

Now consider in particular the case where $u:E \rightarrow E'$ is surjective, and thus for $\mathfrak{I}=\ker u$ we have an isomorphism $E'\cong E/\mathfrak{I}$. Then, letting $d'$ be the restriction of the canonical derivation $d=d_{E/A}$ to $\mathfrak{I}$

$$\mathfrak{I}\overset{d\vert_{\mathfrak{I}}}{\rightarrow}\Omega_{E/A}\overset{i_E}{\rightarrow}\Omega_{E/A}\otimes_EE'$$

since for any $x,y\in \mathfrak{I}$

$$d'(xy)=\dd{(xy)}\otimes1=\dd{y}\otimes u(x)+\dd{x}\otimes u(y)=0$$

the following $E$-linear map

$$\overline{d}:\mathfrak{I}/\mathfrak{I}^2\rightarrow\Omega_{E/A}\otimes_EE'$$

is well-defined. Moreover, since $\mathfrak{I}$ annihilates $\mathfrak{I}/\mathfrak{I}^2$, $\overline{d}$ is an $E'=E/\mathfrak{I}$-linear map.

::: Proposition 14
In the above situation, the sequence of $E'$-linear maps

$$\mathfrak{I}/\mathfrak{I}^2\overset{\overline{d}}{\rightarrow}\Omega_{E/A}\otimes_EE'\overset{\Omega_0(u)}{\rightarrow}\Omega_{E'/A}\rightarrow0$$

is exact.
:::
::: Proof
In the notation of the preceding argument, we can identify $\Omega_{E/A}\otimes_EE'$ with $\Omega_{E/A}/\mathfrak{I}\Omega_{E/A}$. Then under this identification, the image of $\overline{d}$ becomes the image of $\dd{(\mathfrak{I})}\subseteq\Omega_{E/A}$ in the quotient module $\Omega_{E/A}/\mathfrak{I}\Omega_{E/A}$. Therefore, if we take the $A$-submodule $I$ of $\Omega_{E/A}$ to be the one generated by $\mathfrak{I}\Omega_{E/A}$ and $\dd{(\mathfrak{I})}$, we obtain the isomorphism

$$\frac{\Omega_{E/A}\otimes_EE'}{\im(\overline{d})}\cong\frac{\Omega_{E/A}}{I}$$

and through this we obtain the desired result.
:::

---

**References**

**[Bou]** Bourbaki, N. Algebra I. *Elements of Mathematics*. Springer. 1998.
