---
title: "Differential Modules"
excerpt: "Differential modules with derivations on graded algebras"

categories: [Math / Multilinear Algebra]
permalink: /en/math/multilinear_algebra/differential_modules
header:
    overlay_image: /assets/images/Math/Multilinear_Algebra/Differential_Modules.png
    overlay_filter: 0.5
sidebar: 
    nav: "multilinear_algebra-en"

date: 2025-04-18
last_modified_at: 2025-04-18
weight: 121
translated_at: 2026-05-22T06:30:01+00:00
translation_source: kimi-cli
---
Now we define differential modules. For this we need a simple lemma; first consider the second case assumed in [§Derivations, ⁋Definition 2](/en/math/multilinear_algebra/derivations#def2). That is, we consider a commutative ring $$A$$, a $$\Delta$$-graded $$A$$-algebra $$E$$, a graded $$A$$-module $$F$$, and an $$\varepsilon$$-derivation $$d:E \rightarrow F$$.

## Functoriality of Derivations

In addition to the above assumptions, we assume that every algebra appearing in this section is unital associative, and all algebra homomorphisms are unital.

<div class="proposition" markdown="1">

<ins id="prop1">**Proposition 1**</ins> Let two associative unital graded $$A$$-algebras $$E,F$$ be given, let $$M$$ be an $$(E,E)$$-bimodule, and let $$N$$ be a graded $$(F,F)$$-bimodule. Then for a graded $$A$$-algebra homomorphism $$\rho: E \rightarrow F$$ and a degree $$0$$ graded $$E$$-homomorphism $$\theta: M \rightarrow N$$ of $$E$$-bimodules defined by $$\rho$$, the following hold.

1. For any $$\varepsilon$$-derivation $$d': F \rightarrow N$$, the composition $$d'\circ\rho: E \rightarrow \rho^\ast N$$ is also an $$\varepsilon$$-derivation of the same degree.
2. For any $$\varepsilon$$-derivation $$d: E \rightarrow M$$, the composition $$\theta\circ d: E \rightarrow \rho^\ast N$$ is also an $$\varepsilon$$-derivation of the same degree.

</div>

The proof of this is immediate from the definition of $$\rho^\ast$$. Meanwhile, in this situation we can also give $$F$$ an $$(E,E)$$-bimodule structure. Then it is natural to ask when $$d':F \rightarrow N$$ is also (left/right) $$E$$-linear.

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> Assume the situation of [Proposition 1](#prop1), and let an $$\varepsilon$$-derivation $$d': F \rightarrow N$$ be given. Then $$d'$$ is left (resp. right) $$E$$-linear if and only if $$d'$$ vanishes identically on the subalgebra $$\rho(E)$$ of $$F$$.

</div>

Now define $$\Der_A(F, N)$$ to be the set of $$A$$-derivations from $$F$$ to $$N$$. Then the set of derivations satisfying the condition of [Proposition 2](#prop2) and becoming $$E$$-linear is the same as the set of derivations vanishing identically on $$\rho(E)$$, so this set forms an $$A$$-submodule of $$\Der_A(F, N)$$. We denote this by $$\Der_E(F,N)$$.

In addition, let three graded $$A$$-algebras $$E,F,G$$ be given, and let graded $$A$$-algebra homomorphisms $$\rho: A \rightarrow B$$, $$\sigma: B \rightarrow C$$ be given. Then for any graded $$A$$-algebra $$H$$, the sequence

$$0 \rightarrow \Der_F(G, H) \rightarrow \Der_E(G,H) \rightarrow \Der_E(F, H)$$

is exact for the following three $$A$$-modules

$$\Der_E(F, \rho_\ast H),\qquad \Der_F(G,H),\qquad\Der_E(G, H).$$

For any $$\Delta$$-graded $$A$$-module $$M$$ and any $$\delta\in \Delta$$, define $$M[\delta]$$ by the formula

$$(M[\delta])_\mu=M_{\delta+\mu}$$

Since the $$\Delta$$-graded $$A$$-algebra $$E\oplus M[\delta]$$ exists, we can now give $$E\oplus M[\delta]$$ a graded $$A$$-algebra structure using the following formula for homogeneous elements $$x\in E$$ and the resulting elements $$(x,y), (x',y')$$ of $$E\oplus M[\delta]$$:

$$(x,y)(x',y')=(xx', xy+\varepsilon(\delta, \deg x)xy')$$

In this case, we call the projection map $$\epsilon: E\oplus M[\delta] \rightarrow E$$ the *augmentation map*, and we know that this is a graded $$A$$-algebra homomorphism.

Now if a degree $$0$$ graded $$A$$-linear map $$g:E \rightarrow E\oplus M[\delta]$$ satisfies $$\epsilon\circ g=\id_A$$, then by definition we know that it must be of the form $$x\mapsto (x,f(x))$$ for some degree $$\delta$$ graded $$A$$-linear map $$f:E \rightarrow M$$, and conversely any degree $$\delta$$ $$A$$-linear map $$f$$ defines a $$g$$ satisfying the above condition.

Then the following proposition is also a consequence of a simple calculation.

<div class="proposition" markdown="1">

<ins id="prop3">**Proposition 3**</ins> A graded $$K$$-linear map $$f: A \to E$$ of degree $$\delta$$ is an $$\varepsilon$$-derivation if and only if the map $$x \mapsto (x, f(x))$$ is a graded $$K$$-algebra homomorphism from $$A$$ to $$A \oplus E[\delta]$$.

</div>

On the other hand, for the next section we also need to examine when the graded $$A$$-algebra $$E\oplus M[\delta]$$ defined above is associative and unital.

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4**</ins> In the above situation, $$E \oplus M[\delta]$$ is an associative unital algebra if and only if $$E$$ is associative unital and the two maps $$(a, x) \mapsto a \cdot x$$ and $$(a, x) \mapsto x \cdot a$$ define an $$(A, A)$$-bimodule structure on $$M$$. In this case, $$E \oplus M[\delta]$$ has unity $$(1, 0)$$.

</div>

## Tensor Algebras and Derivations

The exterior algebra, which appeared as an important example in the previous post, is obtained from the following more general setting.

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> Let $$A$$ be a commutative ring and $$M$$ an $$A$$-module, let $$B$$ be one of $$\T(M)$$, $$\S(M)$$, or $$\bigwedge(M)$$, and let $$E$$ be a $$(B,B)$$-bimodule. Assume that a derivation $$d_0: A \rightarrow E$$ and an abelian group homomorphism $$d_1: M \rightarrow E$$ satisfy the condition

$$d_1(ax)=ad_1(x)+d_0(a)x.$$

If $$B=\S(M)$$, additionally assume the condition

$$xd_1(y)+d_1(x)y=yd_1(x)+d_1(y)x,$$

and if $$B=\bigwedge(M)$$, additionally assume the condition

$$xd_1(x)+d_1(x)x=0.$$

Then regarding $$B$$ as a $$\mathbb{Z}$$-algebra, there exists a unique $$A$$-derivation $$d: B \rightarrow E$$ satisfying $$d\vert_A = d_0$$ and $$d\vert_M = d_1$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First define multiplication on the abelian group $$B \oplus E$$ by the formula

$$(b, t)(b', t') = (bb', bt' + b't)$$

and regard this as an associative $$\mathbb{Z}$$-algebra. Then via the canonical injection $$t\mapsto (0,t)$$ we can identify $$E$$ with a two-sided ideal of the $$\mathbb{Z}$$-algebra $$B\oplus E$$, and in this case $$E^2=0$$.

On the other hand, defining $$h_0: B \to B \oplus E$$ by $$h_0(a) = (a, d_0(a))$$, this is a (unital) ring homomorphism by [Proposition 3](#prop3), and via this $$B \oplus E$$ becomes an $$A$$-algebra. Now after giving $$B\oplus E$$ such an $$A$$-module structure, consider the function $$h_1: M \rightarrow B\oplus E$$ defined by $$h_1(x) = (x, d_1(x))$$. Then by the given conditions the formula

$$h_1(ax) = h_0(a) h_1(x)$$

holds, so $$h_1$$ is an $$A$$-linear map from $$M$$ to $$B$$. Therefore, using the given assumptions and the universal property of $$T(M)$$, $$S(M)$$, or $$\bigwedge(M)$$, we obtain a unique $$A$$-algebra homomorphism $$h:B \rightarrow B\oplus E$$ satisfying $$h\vert_M=h_1$$. Meanwhile, we can easily check that composing $$h$$ with the augmentation map $$B\oplus E \rightarrow B$$ yields $$\id_B$$, so again by [Proposition 3](#prop3) there exists a unique $$\varepsilon$$-derivation $$d:B \rightarrow E$$ such that $$h(b)=(b,d(b))$$, and from this we obtain the desired result.

</details>

## Universal Property

In this section we assume that every algebra is associative unital, and all algebra homomorphisms are unital.

For any $$A$$-algebra $$E$$, the tensor product $$E\otimes_AE$$ has an $$(E,E)$$-bimodule structure by multiplying elements of $$E$$ on both sides. Considering the multiplication map

$$m: E\otimes_AE \rightarrow E$$

of $$E$$, it is obvious that $$m$$ preserves this $$(E,E)$$-bimodule structure. Therefore we can consider the kernel $$\mathfrak{I}$$ of $$m$$, which is a sub-$$(E,E)$$-bimodule of $$E\otimes_AE$$. Then the following lemma is a simple calculation.

<div class="proposition" markdown="1">

<ins id="lem6">**Lemma 6**</ins> The map $$\delta_E: x \mapsto x \otimes 1 - 1 \otimes x$$ is an $$A$$-derivation from $$E$$ to $$\mathfrak{I}$$. Moreover, $$\mathfrak{I}$$ is generated as a left $$A$$-module by the image of $$\delta_E$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

The first claim follows from the following calculation:

$$(xy)\otimes 1-1\otimes(xy)=(x\otimes 1-1\otimes x)y+x(y\otimes 1-1\otimes y).$$

Now let an arbitrary element $$\sum_i x_i\otimes y_i$$ of $$\mathfrak{I}$$ be given. That is, $$\sum_i x_iy_i=0$$. Then from this we obtain the formula

$$\sum_i x_i\otimes y_i=\sum_i \left(x_i(1\otimes y_i)-(x_iy_i)\otimes 1\right)=\sum_i x_i(1\otimes y_i-y_i\otimes 1),$$

so the second claim is also immediate.

</details>

From this we now obtain the following universal property.

<div class="proposition" markdown="1">

<ins id="prop7">**Proposition 7**</ins> The map $$\delta_E$$ obtained in [Lemma 6](#lem6) satisfies the following universal property.

> For every $$(E,E)$$-bimodule $$M$$ and every $$A$$-derivation $$d: E \to M$$, there exists a unique $$(E,E)$$-bimodule homomorphism $$f: \mathfrak{I} \to M$$ such that $$d=f\circ\delta_E$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, by [Proposition 1](#prop1) we know that for every $$(E, E)$$-bimodule homomorphism $$f: \mathfrak{I} \to M$$, the composition $$f \circ \delta_E$$ is an $$A$$-derivation from $$E$$ to $$M$$.

On the other hand, for uniqueness, from the definition of $$\delta_E$$ we know that we must have

$$f(x \otimes 1 - 1 \otimes x) = dx,$$

and since by [Lemma 6](#lem6) $$\mathfrak{I}$$ is generated by the image of $$\delta_E$$, any $$f$$ satisfying the given condition must be unique if it exists. Moreover, using the calculation from the preceding lemma, we know that for any $$\sum x_i y_i\in \mathfrak{I}$$ the formula

$$f\left( \sum_i x_i \otimes y_i \right) = \sum_i x_i  f(1 \otimes y_i - y_i \otimes 1) = - \sum_i x_i  dy_i$$

must necessarily hold. Therefore, to show existence we must verify that this defines an $$(E,E)$$-bimodule homomorphism. For this, first note that the map $$(x, y) \mapsto -x \cdot dy$$ is an $$A$$-bilinear map from $$E$$ to $$M$$, so from this we know that the $$A$$-bilinear map $$g: E \otimes E \to M$$ defined by $$g(x \otimes y) = -x \cdot dy$$ is well-defined. Then its restriction to $$\mathfrak{I}$$ equals $$f$$, and it now suffices to show that this restriction preserves the $$E$$-bimodule structure, which is a simple calculation.

</details>

By the above proposition we obtain a canonical $$A$$-module isomorphism

$$\Hom_{(E, E)}(\mathfrak{I}, M) \rightarrow \Der_A(E, M).$$

That is, we can think of the $$(E,E)$$-bimodule $$\mathfrak{I}$$ as representing the $$A$$-derivations from $$E$$ to $$M$$.

If moreover $$E$$ is a *commutative* $$A$$-algebra, then we can find a representation of the derivations from $$E$$ to $$M$$ in $$\lMod{E}$$.

First consider $$E\otimes_AE$$. In the preceding argument, the $$(E,E)$$-bimodule structure on $$E\otimes_AE$$ was given by the formula

$$x(u\otimes v)y=(xu)\otimes(vy).$$

If $$E$$ is commutative as in our present assumption, then $$E\otimes_AE$$ is a (commutative) ring, and from the formula

$$x(u\otimes v)y=(xu)\otimes(vy)=(x\otimes y)(u\otimes v)$$

we see that this bimodule structure is in fact the same as the ring structure of $$E\otimes_AE$$. Therefore $$\mathfrak{I}$$ is an ideal of $$E\otimes_AE$$.

Now let us assume a better situation. That is, suppose now that $$E$$ is a *commutative* $$A$$-algebra. Then any $$E$$-module $$M$$ can be viewed as an $$(E,E)$$-bimodule. On the other hand, the $$(E,E)$$-bimodule structure on $$E\otimes_AE$$ appearing above is given, in this case, by the multiplication of $$E\otimes_AE$$; hence $$\mathfrak{I}$$, which was a sub-$$(E,E)$$-bimodule of $$E\otimes_AE$$, is now an ideal of $$E\otimes_AE$$. Moreover, since the multiplication map $$m$$ of the ring is surjective, we obtain the canonical isomorphism

$$(E\otimes_AE)/\mathfrak{I}\cong E.$$

Meanwhile, any $$E$$-module $$M$$ can be regarded as an $$(E,E)$$-bimodule by viewing its action as both a left and a right action. On the other hand, if we view the $$E$$-module $$M$$ as an $$E\otimes_AE$$-module $$M$$ via the multiplication map $$m:E\otimes_AE \rightarrow E$$, then from the adjunction

$$\Hom_{(E,E)}(\mathfrak{I}, M) \rightarrow \Hom_{E\otimes_AE}(\mathfrak{I}, M)$$

we obtain the isomorphisms

$$\Hom_{E\otimes_AE}(\mathfrak{I}, M)\cong \Hom_{(E,E)}(\mathfrak{I}, M)\cong\Der_A(E, M).$$

Now we further show that

$$\Hom_E(\mathfrak{I}/\mathfrak{I}^2, M)\cong \Hom_{E\otimes_AE}(\mathfrak{I}, M)\cong \Hom_{(E,E)}(\mathfrak{I}, M)\cong\Der_A(E, M).$$

First, for any $$z\in M$$ and any generator $$1\otimes x-x\otimes1$$ of $$\mathfrak{I}$$, view $$\mathfrak{I}$$ as an $$E\otimes_AE$$-module as above. Then the commutativity of $$E$$ gives the formula

$$(1\otimes x-x\otimes1)z=0,$$

so $$\mathfrak{I}M=0$$. Therefore $$\mathfrak{I}$$ lies in the annihilator of the $$E\otimes_AE$$-module $$M$$, and hence we can regard $$M$$ as an $$(E\otimes_AE)/\mathfrak{I}$$-module. On the other hand, rewriting the $$A$$-module $$\mathfrak{I}$$ via the formula

$$((E\otimes_AE)/\mathfrak{I})\otimes_A\mathfrak{I}\cong\mathfrak{I}/\mathfrak{I}^2,$$

we obtain the desired claim. That is, the following holds.

<div class="proposition" markdown="1">

<ins id="prop8">**Proposition 8**</ins> Consider a commutative $$A$$-algebra $$E$$, the multiplication map $$m:E\otimes_AE \rightarrow E$$, and the kernel $$\mathfrak{I}$$ of $$m$$. Then give $$\mathfrak{I}/\mathfrak{I}^2$$ an $$E$$-module structure via the canonical isomorphism

$$(E\otimes_AE)/\mathfrak{I}\cong E.$$

On the other hand, defining $$\delta_{E/A}: E \rightarrow \mathfrak{I}/\mathfrak{I}^2$$ by the formula

$$x\mapsto (x\otimes 1-1\otimes x)+\mathfrak{I}^2,$$

$$\delta_{E/A}$$ is an $$A$$-derivation and satisfies the following universal property.

> For any $$E$$-module $$M$$ and any $$A$$-derivation $$D:E \rightarrow M$$, there exists a unique $$A$$-linear map $$g:\mathfrak{I}/\mathfrak{I}^2 \rightarrow M$$ such that $$D=g\circ\delta_{E/A}$$.

</div>

<div class="definition" markdown="1">

<ins id="def9">**Definition 9**</ins> The $$E$$-module $$\mathfrak{I}/\mathfrak{I}^2$$ is called the module of *$$A$$-differentials* (or the ($$E$$-)module of differentials), and is denoted by $$\Omega_{A}(E)$$ or $$\Omega_{E/A}$$. Also, we write $$\delta_{E/A}(x)$$ as $$d_{E/A}(x)$$, and when there is no danger of confusion we simply write this as $$dx$$. For each $$x \in E$$, we call $$d_{E/A}(x)$$ the *differential* of $$x$$.

</div>

Therefore, we obtain the canonical isomorphism

$$\Hom_E(\Omega_{E/A}, N)\cong\Der_A(E, N).$$

<div class="example" markdown="1">

<ins id="ex10">**Example 10**</ins> Let $$A$$ be a commutative ring and $$M$$ an $$A$$-module. Then the symmetric algebra $$\S(M)$$ is a commutative $$A$$-algebra. Therefore, for any $$\S(M)$$-module $$N$$ and any $$A$$-derivation $$D:\S(M)\rightarrow N$$, there exists a unique $$A$$-linear map $$g:\Omega_{\S(M)/A}\rightarrow N$$ such that the formula

$$D=g\circ d_{\S(M)/A}$$

holds.

Meanwhile, given any $$A$$-derivation $$D:\S(M)\rightarrow L$$, we can verify through [Proposition 5](#prop5) that its restriction $$D\vert_M$$ to $$M$$ is an $$A$$-module homomorphism from $$M$$ to $$L$$, and that this correspondence $$D\mapsto D\vert_M$$ is in fact an $$\S(M)$$-module isomorphism. On the other hand, since $$L$$ is an $$\S(M)$$-module, by [[Algebraic Structures] §Change of Base Ring, ⁋Proposition 5](/en/math/algebraic_structures/change_of_base_ring#prop5) we have

$$\Hom_{\S(M)}(M\otimes_A\S(M),L)\cong\Hom_A(M,L),$$

so combining these, we see that any $$A$$-derivation $$D:\S(M)\rightarrow N$$ can be written in the form $$D=h\circ D_0$$, where $$D_0$$ is the $$A$$-derivation obtained by extending the canonical homomorphism

$$M\rightarrow M\otimes_A\S(M);\qquad x\mapsto x\otimes1,$$

and $$h\in \Hom_{\S(M)}(M\otimes_A\S(M),L)$$ is suitable.

By a simple calculation, the $$A$$-linear map $$\Omega_{\S(M)/A}\rightarrow M\otimes_A\S(M)$$ obtained in the first calculation when $$N=M\otimes_A\S(M)$$, and the $$h$$ obtained in the second calculation when $$L=\Omega_A(\S(M))$$, are inverses of each other; hence we know that the isomorphism

$$\Omega_{\S(M)/A}\cong M\otimes_A\S(M)$$

holds, and moreover, if we write this isomorphism as $$\omega:M\otimes_A\S(M)\rightarrow\Omega_{\S(M)/A}$$, then for any $$x\in M$$ we know that $$\omega(x\otimes1)=d_{\S(M)/A}(x)=dx$$.

In particular, if $$M$$ is a free $$A$$-module of finite rank $$n$$, then $$\S(M)$$ can be identified with the polynomial algebra $$A[\x_1,\ldots, \x_n]$$, and under this identification the $$d\x_i$$ are <em-ko>really</em-ko> the images of the $$\x_i$$ under $$d=d_{\S(M)/A}$$; moreover, if the image of a polynomial $$p\in A[\x_1,\ldots, \x_n]$$ under $$d$$ is expressed as a linear combination of the basis elements $$d\x_i$$ of $$\Omega_{\S(M)/A}$$, then the coefficients attached to them are precisely the $$i$$-th partial derivatives $$\partial p/\partial \x_i$$ of $$p$$.

</div>

Now let us prove properties of $$\Omega_{E/A}$$. From now on, every ring is commutative, every algebra is associative, commutative, and unital, and every algebra homomorphism is unital.

<div class="proposition" markdown="1">

<ins id="prop11">**Proposition 11**</ins> Suppose the following commutative diagram is given, and regard $$E$$ and $$E'$$ as $$A$$- and $$A'$$-algebras via the vertical maps.

![change_of_base_ring-1](/assets/images/Math/Multilinear_Algebra/Differential_Modules-1.png){:style="width:6.8em" class="invert" .align-center}

Then there exists a unique $$A$$-linear map

$$\nu: \Omega_{E/A} \rightarrow \Omega_{E'/A'}$$

making the following diagram commute:

![change_of_base_ring-2](/assets/images/Math/Multilinear_Algebra/Differential_Modules-2.png){:style="width:10em" class="invert" .align-center}

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

The proof of this is nothing but an appropriate use of the other universal properties employed in proving [Proposition 8](#prop8).

</details>

From this we see that if we regard $$\Omega$$ as the correspondence taking an $$A$$-algebra $$A \rightarrow E$$ to the module of its differentials $$\Omega_A(E)$$, then $$\Omega$$ also possesses functoriality.

On the other hand, since $$\Omega_{A'}(E')$$ is an $$A'$$-module, by [[Algebraic Structures] §Change of Base Ring, ⁋Proposition 5](/en/math/algebraic_structures/change_of_base_ring#prop5) we obtain from [Proposition 11](#prop11) the following $$A'$$-linear map:

$$\Omega_0(u):\Omega_A(E)\otimes_E E'\rightarrow\Omega_{A'}(E').$$

Denoting by $$i_E$$ the canonical morphism $$\Omega_A(E)\rightarrow \Omega_A(E)\otimes_EE'$$, we know that $$\Omega(u)=\Omega_0(u)\circ i_E$$.

Considering the isomorphism

$$\Hom_E(\Omega_A(E), M)\cong\Der_A(E, M)$$

given by the universal property of [Proposition 8](#prop8), we obtain the following commutative diagram:

![change_of_base_ring-3](/assets/images/Math/Multilinear_Algebra/Differential_Modules-3.png){:style="width:28em" class="invert" .align-center}

Here the right-hand vertical map is the composite of the above isomorphism and the isomorphism of [[Algebraic Structures] §Change of Base Ring, ⁋Proposition 5](/en/math/algebraic_structures/change_of_base_ring#prop5),

$$\Hom_{E'}(\Omega_A(E)\otimes_EE', N) \rightarrow \Hom_E(\Omega_A(E), N)\rightarrow\Der_A(E, N),$$

and the bottom horizontal map is

$$\Der_{A'}(E', N) \rightarrow \Der_A(E, N);\qquad D\mapsto D\circ u$$

obtained from the functoriality of $$\Der$$.

<div class="proposition" markdown="1">

<ins id="prop12">**Proposition 12**</ins> Suppose $$E' = E \otimes_AA'$$, and let $$\eta : A \to E'$$ and $$u : E \to E'$$ be the canonical morphisms. Then the $$A'$$-linear map

$$\Omega_0(u) : \Omega_{E/A}\otimes_EE'\rightarrow\Omega_{E'/A'}$$

is an isomorphism.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, since the vertical maps are all isomorphisms, if we show that $$C(u)$$ is an isomorphism then we know that for any $$N$$,

$$\Hom_{E'}(\Omega_{E'/A'} , N) \rightarrow \Hom_{E'}(\Omega_{E/A}\otimes_AE',N)$$

is an isomorphism. That is, the sequence

$$0\rightarrow\Hom_{E'}(\Omega_{E'/A'} , N) \rightarrow \Hom_{E'}(\Omega_{E/A}\otimes_AE',N)\rightarrow 0$$

is exact for any $$N$$. Now since $$\Hom$$ is a left exact functor ([§Projective, Injective, and Flat Modules, ⁋Proposition 2](/en/math/multilinear_algebra/various_modules#prop2)), the exactness of the above sequence for all $$N$$ is equivalent to the exactness of the sequence

$$0 \rightarrow\Omega_{E/A}\otimes_EE'\rightarrow\Omega_{E'/A'}\rightarrow 0.$$

Therefore, to prove the claim it suffices to show that $$C(u)$$ is bijective.

First,

$$\Hom(u, \id_N):\Hom_{A'}(E\otimes_AA', N) \rightarrow \Hom_A(E, N)$$

is an isomorphism, and since $$C(u)$$ is nothing but its restriction to $$\Der_{A'}(E', N)$$, it is obvious that $$C(u)$$ is injective. That $$C(u)$$ is surjective can also be proved without difficulty.

</details>

In particular, consider the case where $$\rho:A \rightarrow A'$$ is $$\id_A: A\rightarrow A'$$, so that $$u:E\rightarrow E'$$ is an $$A$$-algebra homomorphism. Then through the above process $$u$$ induces an $$E'$$-linear homomorphism

$$\Omega_0(u): \Omega_{E/A}\otimes_AE'\rightarrow\Omega_{E'/A}.$$

On the other hand, if we regard $$E'$$ as an $$E$$-algebra via $$E\rightarrow E'$$, then the derivation $$d_{E'/E}: E' \rightarrow\Omega_{E'/E}$$ obtained here is also an $$A$$-derivation; hence by the universal property of $$\Omega_{E'/A}$$ there exists a factorization

$$E'\overset{d_{E'/A}}{\longrightarrow}\Omega_{E'/A}\overset{\Omega_u}{\longrightarrow}\Omega_{E'/E}.$$

Then again by the universal property there exists the following commutative diagram:

![change_of_base_ring-4](/assets/images/Math/Multilinear_Algebra/Differential_Modules-4.png){:style="width:24em" class="invert" .align-center}

Now we introduce two exact sequences that are frequently used.

<div class="proposition" markdown="1">

<ins id="prop13">**Proposition 13**</ins> The sequence of $$E'$$-modules

$$\Omega_A(E)\otimes_EE'\overset{\Omega_0(u)}{\longrightarrow}\Omega_{E'/A}\overset{\Omega_u}{\longrightarrow}\Omega_{E'/E}\longrightarrow0$$

is exact.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Again from the fact that $$\Hom$$ is a left exact functor ([§Projective, Injective, and Flat Modules, ⁋Proposition 2](/en/math/multilinear_algebra/various_modules#prop2)), it suffices to show that the sequence

$$0 \rightarrow \Hom_{E'}(\Omega_{E'/E},N) \rightarrow \Hom_{E'}(\Omega_{E'/A}, N) \rightarrow \Hom_{E'}(\Omega_{E/A}\otimes_EE',N)$$

is exact for any $$E'$$-module $$N$$. However, using the commutative diagrams employed before and after [Proposition 12](#prop12), we can convert this into the sequence of modules of derivations

$$0 \rightarrow \Der_E(E', N) \rightarrow \Der_A(E', N) \rightarrow \Der_A(E, N),$$

and we showed immediately after [Proposition 2](#prop2) that this is exact.

</details>

Now consider in particular the case where $$u:E \rightarrow E'$$ is surjective, so that for $$\mathfrak{I}=\ker u$$ we have an isomorphism $$E'\cong E/\mathfrak{I}$$. Denote by $$d'$$ the restriction of the canonical derivation $$d=d_{E/A}$$ to $$\mathfrak{I}$$,

$$\mathfrak{I}\overset{d\vert_{\mathfrak{I}}}{\longrightarrow}\Omega_{E/A}\overset{i_E}{\longrightarrow}\Omega_{E/A}\otimes_EE'.$$

Then for any $$x,y\in \mathfrak{I}$$,

$$d'(xy)=d(xy)\otimes1=dy\otimes u(x)+dx\otimes u(y)=0,$$

so the following $$E$$-linear map

$$\overline{d}:\mathfrak{I}/\mathfrak{I}^2\rightarrow\Omega_{E/A}\otimes_EE'$$

is well-defined. Moreover, since $$\mathfrak{I}$$ annihilates $$\mathfrak{I}/\mathfrak{I}^2$$, $$\overline{d}$$ is an $$E'=E/\mathfrak{I}$$-linear map.

<div class="proposition" markdown="1">

<ins id="prop14">**Proposition 14**</ins> In the above situation, the sequence of $$E'$$-linear maps

$$\mathfrak{I}/\mathfrak{I}^2\overset{\overline{d}}{\longrightarrow}\Omega_{E/A}\otimes_EE'\overset{\Omega_0(u)}{\longrightarrow}\Omega_{E'/A}\longrightarrow0$$

is exact.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Using the notation of the preceding argument, we can identify $$\Omega_{E/A}\otimes_EE'$$ with $$\Omega_{E/A}/\mathfrak{I}\Omega_{E/A}$$. Then under this identification, the image of $$\overline{d}$$ becomes the image of $$d(\mathfrak{I})\subset\Omega_{E/A}$$ in the quotient module $$\Omega_{E/A}/\mathfrak{I}\Omega_{E/A}$$. Therefore, taking the $$A$$-submodule $$I$$ of $$\Omega_{E/A}$$ to be that generated by $$\mathfrak{I}\Omega_{E/A}$$ and $$d(\mathfrak{I})$$, we obtain the isomorphism

$$\frac{\Omega_{E/A}\otimes_EE'}{\im(\overline{d})}\cong\frac{\Omega_{E/A}}{I},$$

and through this we obtain the desired result.

</details>
