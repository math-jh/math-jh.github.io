---

title: "Direct Products, Direct Sums, and Tensor Products of Modules"
excerpt: ""

categories: [Math / Algebraic Structures]
permalink: /en/math/algebraic_structures/operations_of_modules
header:
    overlay_image: /assets/images/Math/Algebraic_Structures/Operations_of_modules.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_structures-en"

date: 2026-03-11
last_modified_at: 2026-03-11
weight: 202

---

## Direct Products and Direct Sums of Modules

The category $$\lMod{A}$$ is a bicomplete category. To show this, we need to construct arbitrary products and coproducts in $$\lMod{A}$$, which amounts to showing that there exist natural $$A$$-actions on the product and coproduct in $$\Ab$$.

Let a family $$(M_i)_{i\in I}$$ of $$A$$-modules be given. Then the action on $$\prod M_i$$ is defined by first defining $$A\otimes\left(\prod M_i\right) \rightarrow M_i$$ through the composition

$$A\otimes\left(\prod_{i\in I}M_i\right)\overset{\id_A\otimes\pr_i}{\longrightarrow} A\otimes M_i \overset{\rho_i}{\longrightarrow} M_i $$

and then using the universal property of products in $$\Ab$$ to construct $$A\otimes\left(\prod M_i\right) \rightarrow \prod M_i$$, and showing that this satisfies the action conditions.

For coproducts, since $$A\otimes-$$ is a left adjoint from $$\Ab$$ to $$\Ab$$, it preserves colimits, and thus the action on $$\bigoplus M_i$$ is defined through

$$A\otimes\left(\bigoplus_{i\in I} M_i\right)\cong\bigoplus_{i\in I}(A\otimes M_i)\overset{\bigoplus \rho_i}{\longrightarrow} \bigoplus_{i\in I}M_i$$

For equalizers and coequalizers, for two module homomorphisms $$u,v:M \rightarrow N$$, we define

$$\Eq(u,v)=\{x\in M\mid u(x)=v(x)\}$$

and

$$\CoEq(u,v)=N/N',\qquad N'=\langle u(x)-v(x)\rangle\rangle$$

Thus, the following holds.

<div class="proposition" markdown="1">

<ins id="thm1">**Theorem 1**</ins> $$\lMod{A}$$ is a bicomplete category, and in particular, the product of a family $$(M_i)$$ of $$A$$-modules is given by their direct product, and the coproduct is given by their direct sum.

</div>

Then direct products preserve kernels and direct sums preserve cokernels. ([\[Category Theory\] §Limits, ⁋Proposition 10](/en/math/category_theory/limits#prop10)) Additionally, these satisfy the following proposition.

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> Let two families $$(M_i)_{i\in I},(N_i)_{i\in I}$$ of $$A$$-modules and linear maps $$u_i: M_i \rightarrow N_i$$ between them be given, and consider the induced functions $$\bigoplus u_i:\bigoplus M_i \rightarrow \bigoplus N_i$$ and $$\prod u_i: \prod M_i \rightarrow \prod N_i$$. Then the following holds:

1. If each $$u_i$$ is surjective, then $$\prod u_i$$ is also surjective, and conversely.
2. If each $$u_i$$ is injective, then $$\bigoplus u_i$$ is also injective, and conversely.

</div>

The proof is obtained by writing $$\prod u_i$$ and $$\bigoplus u_i$$ explicitly in terms of coordinates. In particular, from this proposition, we see that direct products also preserve cokernels and direct sums also preserve kernels.

Earlier, we saw that for any $$M,N\in\lMod{A}$$, the set $$\Hom_{\lMod{A}}(M,N)$$ is an abelian group. It is not difficult to verify that this addition behaves well with respect to composition, and that the category $$\lMod{A}$$ is an additive category with the zero module $$0$$ as its zero object. ([\[Category Theory\] §Abelian Categories, ⁋Definition 1](/en/math/category_theory/abelian_categories#def1))

Moreover, $$\lMod{A}$$ is an abelian category. ([\[Category Theory\] §Abelian Categories, ⁋Definition 7](/en/math/category_theory/abelian_categories#def7)) To verify this, we need to check that any monomorphism $$u:M \rightarrow N$$ is the kernel of its cokernel $$N \rightarrow N/M$$, and any epimorphism $$v:M \rightarrow N$$ is the cokernel of its kernel $$M \rightarrow M/\ker v$$.

## Free Modules

In [§Modules, ⁋Example 5](/en/math/algebraic_structures/modules#ex5), we saw that a ring $$A$$ carries an $$A$$-module structure. Then any $$A$$-module homomorphism $$u:A \rightarrow M$$ is uniquely determined by $$u(1)$$. For any $$\alpha\in A$$,

$$u(\alpha)=u(\alpha\cdot 1)=\alpha\cdot u(1)$$

In other words, the isomorphism

$$\Hom_A(A, M)\cong\Hom_\Set(\ast, U(M))$$

holds. Here $$U:\lMod{A} \rightarrow \Set$$ is the forgetful functor. Thus, $$A$$ can be called a representation of the forgetful functor $$U$$.

On the other hand, since we have verified that $$\lMod{R}$$ has coproducts $$\bigoplus$$, if a left adjoint $$F: \Set \rightarrow \lMod{A}$$ to $$U$$ exists, then the equation

$$F(X)=F\left(\coprod_{x\in X} \{x\}\right)\cong\bigoplus_{x\in X} F(\{x\})$$

must hold, and using the above representation, we see that we should define $$F(X)=\bigoplus_{x\in X}Ax$$. Thus, the following holds.

<div class="proposition" markdown="1">

<ins id="prop3">**Proposition 3**</ins> For the forgetful functor $$U:\lMod{A} \rightarrow\Set$$ and the free functor $$F:\Set \rightarrow\lMod{A}$$ defined above, an adjunction $$F\dashv U$$ exists.

</div>

For any set $$X$$, $$A$$-modules isomorphic to $$F(X)$$ are called *free $$A$$-modules*.

## Tensor Products of Modules

On the other hand, we can also define the tensor product of $$A$$-modules. First, we begin with the following definition.

<div class="definition" markdown="1">

<ins id="def4">**Definition 4**</ins> Let a ring $$A$$, a right $$A$$-module $$M$$, and a left $$A$$-module $$N$$ be given. Then for any abelian group $$L$$, a function $$f:M\times N \rightarrow L$$ is called *$$A$$-balanced* if $$f$$ is bilinear as a function between abelian groups, and additionally the equation

$$f(x\alpha, y)=f(x,\alpha y)$$

holds.

</div>

For fixed $$M\in\obj(\rMod{A}),N\in\obj(\lMod{A})$$, define the set $$\Balan_A(M,N;L)$$ by

$$\Balan_A(M,N;L)=\{\text{$A$-balanced maps from $M\times N$ to $L$}\}$$

Then the following theorem holds.

<div class="proposition" markdown="1">

<ins id="thm5">**Theorem 5**</ins> The functor $$\Balan_A(M,N;-):\lMod{\mathbb{Z}}=\Ab\rightarrow\Set$$ is a representable functor.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Define the subgroup $$M'$$ of the free abelian group $$F(M\times N)$$ by

$$M'=\left\langle (x, y_1+y_2)-(x,y_1)-(x,y_2), (x_1+x_2,y)-(x_1,y)-(x_2,y), (\alpha x,y)-(x,\alpha y)\right\rangle$$

Then by the universal property of free groups, whenever a function $$f:M\times N \rightarrow L$$ is given, there exists a group homomorphism $$\hat{f}:F(M\times N)\rightarrow L$$, and if $$f$$ is $$A$$-balanced, then the kernel of $$\hat{f}$$ contains $$M'$$, so $$\hat{f}$$ defines a group homomorphism from $$F(M\times N)/M'$$ to $$L$$.

The naturality of the isomorphism $$\Balan_A(M,N;L)\cong\Hom_\Ab(F(M\times N)/M',L)$$ requires additional verification, but this is a straightforward computation, so we omit it.

</details>

The representation thus obtained is denoted by $$M\otimes_AN$$. Then the following holds.

<div class="proposition" markdown="1">

<ins id="thm6">**Theorem 6 ($$\otimes\dashv\Hom$$)**</ins> There exists an adjunction

$$\Hom_\mathbb{Z}(M\otimes_A N, L)\cong\Hom_{\rMod{A}}(M,\Hom_\mathbb{Z}(N, L))\cong\Hom_{\lMod{A}}(N,\Hom_\mathbb{Z}(M, L))$$

</div>

Therefore, $$\otimes$$ commutes with colimits, and $$\Hom$$ commutes with limits. In particular, the following isomorphisms between abelian groups

$$M\otimes_A\left(\bigoplus_{i\in I} N_i\right)\cong \bigoplus_{i\in I} M\otimes_AN_i,\qquad \left(\bigoplus_{i\in I} M_i\right)\otimes_A N\cong\bigoplus_{i\in I} M_i\otimes_AN\tag{1}$$

and

$$\Hom_{\lMod{A}}\left(M,\prod_{i\in I} N_i\right)\cong\prod_{i\in I}\Hom_{\lMod{A}}(M, N_i),\qquad \Hom_{\lMod{A}}\left(\bigoplus_{i\in I} M_i, N\right)\cong \prod_{i\in I}\Hom_{\lMod{A}}(M_i,N)\tag{2}$$

are obtained. In particular, when $$A=\mathbb{Z}$$, we recover the contents of [§Abelian Groups, §§Tensor Products](/en/math/algebraic_structures/abelian_groups#텐서곱); the isomorphisms above were not written in that article due to space constraints.

## Tensor Products of Modules over Commutative Rings

The $$M\otimes_A N$$ defined above does not carry an $$A$$-module structure. If we try to define an $$A$$-action on $$M\otimes_A N$$, it would be natural to define the element

$$(x\alpha)\otimes_A y=x\otimes_A(\alpha y)$$

as $$\alpha(x\otimes_Ay)$$, but then computing $$(\alpha\beta)(x\otimes_Ay)$$ would give

$$(x\alpha\beta)\otimes_A y,\qquad x\otimes_A(\alpha\beta y)$$

which would be different elements. This is also why, in the definition of the tensor product, $$M$$ is taken as a right module and $$N$$ as a left module.

If $$M$$ has not only a right $$A$$-module structure but also a compatible left $$B$$-module structure, then $$M$$ is called a $$(B,A)$$-bimodule. That is, for any $$\alpha\in A$$, $$\beta\in B$$, and $$x\in M$$, the equation

$$(\alpha\cdot_A x)\cdot_B\beta=\alpha\cdot_A(x\cdot_B\beta)$$

must hold. Then one can verify that the equation

$$\beta(x\otimes_A y)=(\beta x)\otimes_Ay$$

gives $$M\otimes_AN$$ a left $$B$$-module structure.

We are mostly interested in the case where $$A$$ is a commutative ring. Then any left $$A$$-module is also a right $$A$$-module, and vice versa. Moreover, regarding any left $$A$$-module as a right $$A$$-module, these two structures form an $$(A,A)$$-bimodule structure. Therefore, there exists a natural $$A$$-action on $$M\otimes_AN$$:

$$\alpha(x\otimes_Ay)=(\alpha x)\otimes_Ay=x\otimes_A(\alpha y)$$

This also becomes a representation of an appropriate functor.

<div class="definition" markdown="1">

<ins id="def7">**Definition 7**</ins> Let a commutative ring $$A$$ and three $$A$$-modules $$M,N,L$$ be given. A function $$f:M\times N \rightarrow L$$ is called *$$A$$-bilinear* if $$f$$ is bilinear as a function between abelian groups, and additionally the equation

$$\alpha f(x,y)=f(\alpha x,y)=f(x,\alpha y)$$

holds.

</div>

Define the set $$\Bilin_A(M,N;L)$$ by

$$\Bilin_A(M,N;L)=\{\text{$A$-bilinear maps from $M\times N$ to $L$}\}$$

<div class="proposition" markdown="1">

<ins id="prop8">**Proposition 8**</ins> The functor $$\Bilin_A(M,N;-):\lMod{A}\rightarrow\Set$$ is a representable functor, and its representation is the *$$A$$-module* $$M\otimes_AN$$ defined above.

</div>

On the other hand, if $$A$$ is a general ring, then $$\Hom_{\lMod{A}}(M,M')$$ does not carry an $$A$$-module structure, but if $$A$$ is a commutative ring, then $$\Hom_{\lMod{A}}(M,M')$$ also has an $$A$$-module structure. That is, $$\Hom_A$$ is an internal $$\Hom$$, and thus we can refine the adjunction in [Theorem 6](#thm6) to prove the following.

<div class="proposition" markdown="1">

<ins id="thm9">**Theorem 9**</ins> For a commutative ring $$A$$, there exists an adjunction

$$\Hom_A(M\otimes_AN, L)\cong\Hom_A(M,\Hom_A(N,L))\cong\Hom_A(N,\Hom_A(M,L))$$

</div>

In particular, the isomorphisms (1) and (2) above become isomorphisms between $$A$$-modules. Also, one can verify that $$(\lMod{A},\otimes_A,A)$$ becomes a symmetric monoidal category.
