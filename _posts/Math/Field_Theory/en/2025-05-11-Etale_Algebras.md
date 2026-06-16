---
title: "Étale Algebras"
description: "We discuss properties of extension degree in field extensions, proving the isomorphism of vector spaces via the Hom-tensor adjunction and properties of free subsets of algebras."
excerpt: "The definition of étale algebras over a field and a characterization via diagonalizability"

categories: [Math / Field Theory]
permalink: /en/math/field_theory/etale_algebras
sidebar: 
    nav: "field_theory-en"

date: 2025-05-11
weight: 5
translated_at: 2026-05-31T05:00:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-05-31T05:00:04+00:00
---
Fix a $$\mathbb{K}$$-algebra $$A$$ and a field extension $$\mathbb{L}/\mathbb{K}$$. Then the collection $$\Hom_\mathbb{K}(A, \mathbb{L})$$ of $$\mathbb{K}$$-linear maps between $$\mathbb{K}$$-vector spaces is itself a $$\mathbb{K}$$-vector space, and via the isomorphism

$$\Hom_\mathbb{K}(A,\mathbb{L})\cong\Hom_\mathbb{K}(A, \mathbb{K}\otimes_\mathbb{K}\mathbb{L})\cong\Hom_\mathbb{K}(A, \mathbb{K})\otimes_\mathbb{K}\mathbb{L}=A^\ast\otimes_\mathbb{K}\mathbb{L}$$

it can also be regarded as an $$\mathbb{L}$$-vector space. ([\[Multilinear Algebra\] §Hom and the Tensor Product, ⁋Proposition 3](/en/math/multilinear_algebra/hom_and_tensor#prop3))

Rearranging the above construction slightly, consider the dual $$(A_{(\mathbb{L})})^\ast$$ of $$A_{(\mathbb{L})}=\mathbb{L}\otimes_\mathbb{K}A$$ (as an $$\mathbb{L}$$-vector space). Then by the Hom-tensor adjunction

$$(A_{(\mathbb{L})})^\ast=\Hom_\mathbb{L}(\mathbb{L}\otimes_\mathbb{K}A, \mathbb{L})\cong\Hom_\mathbb{K}(A, \Hom_\mathbb{L}(\mathbb{L}, \mathbb{L}))\cong\Hom_\mathbb{K}(A, \mathbb{L})$$

we obtain an isomorphism of $$\mathbb{L}$$-vector spaces

$$(A_{(\mathbb{L})})^\ast=\Hom_\mathbb{L}(A_{(\mathbb{L})}, \mathbb{L})\cong\Hom_\mathbb{K}(A,\mathbb{L})\cong A^\ast\otimes_\mathbb{K}\mathbb{L}.$$

In particular, if $$A$$ is finite-dimensional as a $$\mathbb{K}$$-vector space then $$A^\ast$$ is a $$\mathbb{K}$$-vector space of the same dimension, and therefore $$A_{(\mathbb{L})}$$ and $$A_{(\mathbb{L})}^\ast$$ are also $$\mathbb{L}$$-vector spaces of the same dimension. Thus we obtain the formula

$$[A_{(\mathbb{L})}:\mathbb{L}]=\dim_\mathbb{L}A_{(\mathbb{L})}=\dim_\mathbb{L} (A_{(\mathbb{L})})^\ast=\dim_\mathbb{K}A=[A:\mathbb{K}].$$

From this we extract the following key ideas of this post.

1. The extension degree $$[A:\mathbb{K}]$$ behaves well under base change.
2. To compute the extension degree $$[A:\mathbb{K}]$$ it suffices to take any extension $$\mathbb{L}/\mathbb{K}$$ and compute the dimension of $$\Hom_\mathbb{K}(A,\mathbb{L})$$.

The following theorem is related to the second idea, and will help us compute the dimension of $$\Hom_\mathbb{K}(A,\mathbb{L})$$, which is the object of our interest.

<div class="proposition" markdown="1">

<ins id="thm1">**Theorem 1**</ins> Let an extension $$\mathbb{L}/\mathbb{K}$$ be given and fix a $$\mathbb{K}$$-algebra $$A$$. Then $$\Hom_{\Alg{\mathbb{K}}}(A,\mathbb{L})$$ is a free subset of the $$\mathbb{L}$$-vector space $$\Hom_\mathbb{K}(A, \mathbb{L})$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

In other words, it suffices to show that every finite subset $$\{u_1,\ldots, u_n\}$$ of $$\Hom_{\Alg{\mathbb{K}}}(A, \mathbb{L})$$ is linearly independent. We argue by induction on $$n$$. The case $$n=0$$ is trivial, so assume $$n \geq 1$$.

Suppose elements $$\alpha_1,\ldots,\alpha_n$$ of $$\mathbb{L}$$ satisfy

$$\sum_{i=1}^{n} \alpha_i u_i = 0$$

for $$u_1,\ldots, u_n\in\Hom_{\Alg{\mathbb{K}}}(A, \mathbb{L})$$. Then for $$x,y\in A$$ the computation

$$\sum_{i=1}^{n-1} \alpha_i([u_i(x) - u_n(x)) u_i(y) = \sum_{i=1}^{n} \alpha_i u_i(xy) - u_n(x) \sum_{i=1}^{n} \alpha_i u_i(y) = 0$$

gives

$$\sum_{i=1}^{n-1} \alpha_i(u_i(x) - u_n(x)) u_i = 0.$$

By the inductive hypothesis, the coefficients $$\alpha_i(u_i(x)-u_n(x))$$ must all vanish. Since $$u_1,\ldots, u_n$$ are distinct, for this to hold identically regardless of the value of $$x$$ we must have $$\alpha_i=0$$ for all $$i=1,\ldots, n-1$$. Substituting this back into the original equation shows that $$\alpha_n$$ must also be $$0$$.

</details>

This theorem itself is not so surprising: for instance, given $$\Hom_\mathbb{K}(\mathbb{K},\mathbb{K})$$ and its subset $$\Hom_{\Alg{\mathbb{K}}}(\mathbb{K},\mathbb{K})$$, for any $$\lambda\in \mathbb{K}$$ the map

$$x\mapsto \lambda x$$

is always $$\mathbb{K}$$-linear, but for it to be a $$\mathbb{K}$$-algebra homomorphism the identity $$\lambda(xy)=\lambda(x)\lambda(y)$$ must hold, which forces $$\lambda^2=\lambda$$; hence $$\Hom_{\Alg{\mathbb{K}}}(\mathbb{K},\mathbb{K})$$ consists of the single element $$\id$$.

In any case, from the above theorem we obtain the inequality

$$\lvert\Hom_{\Alg{\mathbb{K}}}(A, \mathbb{L})\rvert\leq \dim_\mathbb{L}\Hom_\mathbb{K}(A,L)=[A:\mathbb{K}].$$

In particular we obtain the following two corollaries.

<div class="proposition" markdown="1">

<ins id="cor2">**Corollary 2**</ins> Fix a monoid $$\Gamma$$ and a field $$\mathbb{L}$$, and let $$X$$ be the set of homomorphisms from $$\Gamma$$ to $$\mathbb{L}^\times$$. Then $$X$$ is a free subset of the $$\mathbb{L}$$-vector space $$L^\Gamma$$ of functions from $$\Gamma$$ to $$\mathbb{L}$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Consider the monoid algebra $$A=L\Gamma$$ and its canonical basis $$(e_\gamma)_{\gamma\in\Gamma}$$.

Then by a generalization of [\[Algebraic Structures\] §Algebras, ⁋Proposition 6](/en/math/algebraic_structures/algebras#prop6) there is a bijection between $$X$$ and $$\Hom_\mathbb{L}(A,\mathbb{L})$$, so the claim follows immediately from [Theorem 1](#thm1).

</details>

<div class="proposition" markdown="1">

<ins id="cor3">**Corollary 3 (Dedekind)**</ins> For two extensions $$\mathbb{L}/\mathbb{K}$$ and $$\mathbb{M}/\mathbb{K}$$, the set of morphisms from $$\mathbb{M}$$ to $$\mathbb{L}$$ is free as an $$\mathbb{L}$$-vector space. In particular, if $$\mathbb{M}/\mathbb{K}$$ is a finite degree extension then this set has at most $$[\mathbb{M}:\mathbb{K}]$$ elements.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Set $$A=\mathbb{M}$$ and apply [Theorem 1](#thm1). The second assertion is clear because $$\Hom_\mathbb{K}(\mathbb{M},\mathbb{L})$$ is an $$\mathbb{L}$$-vector space of dimension $$[\mathbb{M}:\mathbb{K}]$$.

</details>

Furthermore, if $$\mathbb{K}$$ is infinite then these maps are also *algebraically independent*.

<div class="proposition" markdown="1">

<ins id="thm4">**Theorem 4**</ins> Let an infinite field $$\mathbb{K}$$ and an extension $$\mathbb{L}/\mathbb{K}$$ be given, and fix a $$\mathbb{K}$$-algebra $$A$$. If for $$\mathbb{K}$$-algebra homomorphisms $$u_1,\ldots, u_n:A \rightarrow \mathbb{L}$$ a polynomial $$f\in \mathbb{L}[\x_1,\ldots, \x_n]$$ satisfies $$f(u_1,\ldots, u_n)=0$$ identically, then $$f=0$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Let $$B$$ be the subset of $$\mathbb{L}^n$$ consisting of elements of the form $$(u_1(x), \dots, u_n(x))$$. Then by [Theorem 1](#thm1) we know that there do not exist $$\alpha_1,\ldots, \alpha_n$$ satisfying

$$\sum_{i=1}^n\alpha_i u_i(x)=0$$

for all $$x\in A$$. In other words, if we define the bilinear pairing $$B\times \mathbb{L}^n \rightarrow \mathbb{L}$$ by

$$\bigl((u_1(x),\cdots, u_n(x)), (\alpha_1,\ldots, \alpha_n)\bigr) \mapsto \sum_{i=1}^n \alpha_iu_i(x)$$

then the induced map $$\mathbb{L}^n\rightarrow B^\ast$$ is injective, and hence $$B$$ must generate $$\mathbb{L}$$. Therefore there exist $$a_j\in A$$ such that the $$n\times n$$ matrix $$(u_i(a_j))$$ is invertible.

Now define the polynomial $$g \in \mathbb{L}[\y_1,\ldots, \y_n]$$ by

$$g(\y_1, \ldots, \y_n) = f\left( \sum_{j=1}^n u_1(a_j)y_j, \ldots, \sum_{j=1}^n u_n(a_j)\y'_j \right).$$

Substituting arbitrary elements $$y_i\in \mathbb{K}$$ and setting $$x=\sum_{i=1}^n a_iy_i$$, we have

$$g(y_1, \dots, y_n) = f(u_1(x), \dots, u_n(x)) = 0,$$

and by the hypothesis on $$f$$ we know that $$g(y_1,\ldots, y_n)=0$$. Since $$\mathbb{K}$$ is infinite, $$g$$ must be identically $$0$$; letting $$(v_{ij})$$ be the inverse matrix of $$(u_i(a_j))$$, we have

$$f(\x_1,\ldots, \x_n)=g\left(\sum_{j=1}^n b_{1j}\x_j, \dots, \sum_{j=1}^n b_{nj}\x_j \right)$$

and therefore $$f$$ is also identically $$0$$.

</details>

## Étale Algebras

<div class="definition" markdown="1">

<ins id="def5">**Definition 5**</ins> A $$\mathbb{K}$$-algebra $$A$$ is called *diagonalizable* if there exists a suitable $$n\geq 0$$ and a $$\mathbb{K}$$-algebra isomorphism $$A\cong \mathbb{K}^n$$. If there exists an extension $$\mathbb{L}/\mathbb{K}$$ such that for some $$n\geq 0$$ there is an $$\mathbb{L}$$-algebra isomorphism $$A_{(\mathbb{L})}\cong \mathbb{L}^n$$, we say that this extension *diagonalizes* $$A$$. If there exists a suitable extension $$\mathbb{L}/\mathbb{K}$$ that diagonalizes $$A$$, we call $$A$$ an *étale algebra*.

</div>

A diagonalizable algebra is useful in that its extension degree $$[A:\mathbb{K}]$$ is well defined. Using the first key idea explained at the beginning of this post, we can say that an étale algebra is just as useful.

We begin with the following characterization of diagonalizable algebras.

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6**</ins> For a $$\mathbb{K}$$-algebra $$A$$ of finite degree $$n$$, the following are all equivalent.

1. $$A$$ is diagonalizable.
2. There exists a suitable basis $$(e_1,\ldots, e_n)$$ of $$A$$ such that $$e_i^2=e_i$$ and $$e_ie_j=0$$.
3. The $$\mathbb{K}$$-algebra homomorphisms from $$A$$ to $$\mathbb{K}$$ generate $$A^\ast$$.
4. Every $$A$$-module decomposes as a direct sum of submodules that are one-dimensional over $$\mathbb{K}$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

The equivalence of the first two conditions follows immediately from the multiplication structure on $$\mathbb{K}^n$$. On the other hand, the $$n$$ projections from $$\mathbb{K}^n$$ to $$\mathbb{K}$$ are $$\mathbb{K}$$-algebra homomorphisms, so these conditions imply the third.

Conversely, assume that the third condition holds and choose a basis $$u_1,\ldots, u_n$$ of $$A^\ast$$. Then one can show that the map $$x\mapsto (u_i(x))$$ is a $$\mathbb{K}$$-algebra isomorphism from $$A$$ to $$\mathbb{K}^n$$, and hence the first three conditions are all equivalent.

It remains to show the equivalence of the fourth condition. For this, assume that the second condition holds and pick any $$A$$-module $$M$$. Considering the $$A$$-endomorphism of $$M$$ defined by $$x\mapsto e_ix$$, we see that $$M$$ is the direct sum of the $$e_iM$$, which yields the fourth condition. Conversely, assuming the fourth condition, we can in particular write $$A$$ itself as an internal direct sum of one-dimensional $$\mathbb{K}$$-vector spaces, and one checks that the resulting basis satisfies the condition of the second equivalence.

</details>

In particular, the fourth condition provides some justification for calling $$A$$ *diagonalizable*. The next corollary tells us when the set $$\Hom_{\Alg{\mathbb{K}}}(A, \mathbb{L})$$ of [Theorem 1](#thm1) becomes a *basis*.

<div class="proposition" markdown="1">

<ins id="cor7">**Corollary 7**</ins> Consider a field extension $$\mathbb{L}/\mathbb{K}$$ and the collection $$\Hom_{\Alg{\mathbb{K}}}(A, \mathbb{L})$$ of $$\mathbb{K}$$-algebra homomorphisms $$A \rightarrow \mathbb{L}$$. Then equality holds in the inequality

$$\lvert \Hom_{\Alg{\mathbb{K}}}(A, \mathbb{L})\rvert \leq [A:\mathbb{K}]$$

if and only if $$A$$ is diagonalized by $$\mathbb{L}$$, and in this case $$\Hom_{\Alg{\mathbb{K}}}(A, \mathbb{L})$$ forms a basis of $$\Hom_\mathbb{K}(A,\mathbb{L})$$.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>  

We already know that $$\dim_\mathbb{L}\Hom_\mathbb{K}(A,\mathbb{L})=\dim_\mathbb{K}A$$, and by [Theorem 1](#thm1) we know that $$\Hom_{\Alg{\mathbb{K}}}(A, \mathbb{L})$$ is a free subset of $$\Hom_\mathbb{K}(A,\mathbb{L})$$. Hence the inequality in the claim is obvious, and equality holds only when $$\Hom_{\Alg{\mathbb{K}}}(A, \mathbb{L})$$ is a basis of $$\Hom_\mathbb{K}(A,\mathbb{L})$$.

On the other hand, the $$\mathbb{L}$$-vector space isomorphism $$\Hom_\mathbb{K}(A,\mathbb{L}) \rightarrow (A_{(\mathbb{L})})^\ast$$ sends the subset $$\Hom_\Alg{\mathbb{K}}(A, \mathbb{L})$$ to the set $$\Hom_\Alg{\mathbb{K}}(A_{(\mathbb{L})}, \mathbb{L})$$ of algebra homomorphisms $$A_{(\mathbb{L})} \rightarrow \mathbb{L}$$. Now by the third equivalent condition of [Proposition 6](#prop6), the fact that this set $$\Hom_\Alg{\mathbb{K}}(A_{(\mathbb{L})}, \mathbb{L})$$ generates $$(A_{(\mathbb{L})})^\ast$$ is equivalent to $$A$$ being diagonalized by $$\mathbb{L}$$, which gives the desired result.

</details>

Thus, if $$A$$ is an étale algebra then the extension degree of $$A$$ over $$\mathbb{K}$$ equals the number of elements of $$\Hom_{\Alg{\mathbb{K}}} (A, \mathbb{L})$$; carefully unwinding the proof one sees that what we are actually computing is $$[A_{(\mathbb{L})}:\mathbb{L}]$$ for an extension $$\mathbb{L}/\mathbb{K}$$ that diagonalizes $$A$$. From this point of view the following holds.

<div class="proposition" markdown="1">

<ins id="prop8">**Proposition 8**</ins> For a $$\mathbb{K}$$-algebra $$A$$, the following are all equivalent.

1. $$A$$ is étale.  
2. There exists a finite degree extension that diagonalizes $$A$$.  
3. $$\overline{\mathbb{K}}/\mathbb{K}$$ diagonalizes $$A$$.
</div>

<details class="proof" markdown="1">
<summary>Proof</summary>  

First assume condition 1, let $$n=[A:\mathbb{K}]$$, and suppose that $$\mathbb{L}/\mathbb{K}$$ diagonalizes $$A$$. Then by [Corollary 7](#cor7) the set $$\Hom_{\Alg{\mathbb{K}}}(A, \mathbb{L})$$ has size $$n$$. On the other hand, for any $$u\in \Hom_{\Alg{\mathbb{K}}}(A, \mathbb{L})$$ it is obvious that $$[u(A):\mathbb{K}]\leq n$$; hence the subextension $$\mathbb{L}'$$ of $$\mathbb{L}$$ generated by the images of the elements of $$\Hom_{\Alg{\mathbb{K}}}(A, \mathbb{L})$$ is of finite degree over $$\mathbb{K}$$. Since there are now $$n$$ distinct homomorphisms from $$A$$ to $$\mathbb{L}'$$, [Corollary 7](#cor7) again implies that $$\mathbb{L}'$$ diagonalizes $$A$$.

That condition 2 implies condition 3 follows immediately from the fact that any finite degree extension $$\mathbb{L}/\mathbb{K}$$ can be viewed as a subextension of $$\overline{\mathbb{K}}$$, and that condition 3 implies condition 1 is simply by definition.

</details>

The finiteness in the next proposition justifies the name étale.

<div class="proposition" markdown="1">

<ins id="prop9">**Proposition 9**</ins> An étale $$\mathbb{K}$$-algebra $$A$$ has only finitely many subalgebras and ideals. Moreover, any extension that diagonalizes $$A$$ also diagonalizes every subalgebra and quotient algebra of $$A$$; consequently every subalgebra and every quotient algebra of $$A$$ is étale.
</div>

<details class="proof" markdown="1">
<summary>Proof</summary>  

It suffices to show that $$\mathbb{K}^n$$ has only finitely many subalgebras and ideals, and that their subalgebras and quotient algebras are diagonalizable.

Let $$(e_1, \dots, e_n)$$ be the canonical basis of $$\mathbb{K}^n$$, and for a subalgebra $$A$$ of $$\mathbb{K}^n$$ let $$v_1,\ldots, v_n$$ be the restrictions to $$A$$ of the projection maps $$\mathbb{K}^n \rightarrow \mathbb{K}$$. Then the intersection of their kernels is $$0$$, so the $$v_i$$ generate $$A^\ast$$ (as a $$\mathbb{K}$$-vector space) and hence $$A$$ is diagonalizable.

Therefore every subalgebra of $$A$$ is also diagonalizable, and so for any given subalgebra of $$A$$ we must be able to find a basis satisfying the second condition of [Proposition 6](#prop6). Now the idempotents of $$\mathbb{K}^n$$ are exactly those of the form $$e_I=\sum_{i\in I} e_i$$ for subsets $$I\subseteq\{1,\ldots, n\}$$, and they satisfy $$e_Ie_J=e_{I\cap J}$$. Hence the pairs of idempotents satisfying the second condition are at most as many as the number of partitions of $$\{1,\ldots, n\}$$, and therefore any subalgebra of $$A$$ is one of only finitely many.

Similarly, letting $$\mathfrak{a}_I$$ be the $$\mathbb{K}$$-subspace spanned by $$(e_i)_{i\in I}$$, we can show the finiteness of ideals and the diagonalizability of $$\mathbb{K}^n/\mathfrak{a}_I$$ again by [Proposition 6](#prop6).

</details>

## Separable Degree

Before looking further into the properties of étale algebras, let us introduce a useful concept. In the discussion so far the set $$\Hom_{\Alg{\mathbb{K}}}(A, \mathbb{L})$$ that first appeared in [Theorem 1](#thm1) has played an important role. Now fix a commutative $$\mathbb{K}$$-algebra $$A$$ of finite degree, and for any extension $$\mathbb{L}/\mathbb{K}$$ define a natural number $$h(\mathbb{L})=\lvert \Hom_{\Alg{\mathbb{K}}}(A,\mathbb{L})\rvert$$. Then we know the inequality

$$h(\mathbb{L})\leq [A:\mathbb{K}]=n$$

always holds. Moreover, considering the third condition of [Proposition 8](#prop8), if there exists an $$\mathbb{L}$$ that makes the above inequality an equality then $$h(\overline{\mathbb{K}})$$ must also make it an equality. Motivated by this we make the following definition.

<div class="definition" markdown="1">

<ins id="def10">**Definition 10**</ins> We define the natural number $$h(\overline{\mathbb{K}})$$ to be the *separable degree* of $$A$$ and write it as $$[A:\mathbb{K}]_s$$.

</div>

Of course, for this to be well defined this value must not depend on the choice of $$\overline{\mathbb{K}}$$. This is a consequence of the following lemma.

<div class="proposition" markdown="1">

<ins id="lem11">**Lemma 11**</ins> Fix any algebraic closure $$\Omega$$ of $$\mathbb{K}$$. Then for any extension $$\mathbb{L}/\mathbb{K}$$, we have $$h(\mathbb{L})\leq h(\Omega)$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Let $$\mathbb{L}'$$ be the algebraic closure of $$\mathbb{K}$$ in $$\mathbb{L}$$. Then for any homomorphism $$u:A \rightarrow \mathbb{L}$$ we have

$$[u(A):\mathbb{K}]\leq n$$

That is, $$u(A)$$ is an algebraic extension and hence is contained in $$\mathbb{L}'$$. From this we see that $$h(\mathbb{L}')=h(\mathbb{L})$$ must hold.

On the other hand, by [§Algebraic Closures, ⁋Proposition 11](/en/math/field_theory/algebraically_closed_extensions#prop11) $$\mathbb{L}'$$ is isomorphic to a suitable subextension of $$\Omega$$, and therefore

$$h(\mathbb{L})=h(\mathbb{L}')\leq h(\Omega)$$

</details>

Hence, if $$\mathbb{L}$$ is algebraically closed we can interchange the roles of $$\mathbb{L}$$ and $$\Omega$$, so equality must hold; consequently [Definition 10](#def10) is well defined. The following are basic properties of this notion.

<div class="proposition" markdown="1">

<ins id="prop12">**Proposition 12**</ins> The following hold.

1. For any finite degree $$\mathbb{K}$$-algebras $$A,B$$, we have $$[A\otimes_\mathbb{K}B:\mathbb{K}]_s=[A:\mathbb{K}]_s[B:\mathbb{K}]_s$$.
2. For any extension $$\mathbb{K}'/\mathbb{K}$$ and any $$\mathbb{K}$$-algebra $$A$$, we have $$[A_{(\mathbb{K}')}:\mathbb{K}']_s=[A:\mathbb{K}]_s$$.
3. For any finite degree extension $$\mathbb{K}'/\mathbb{K}$$ and any $$\mathbb{K}'$$-algebra $$A'$$, we have $$[A':\mathbb{K}]_s=[A':\mathbb{K}']_s[\mathbb{K}':\mathbb{K}]_s$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

1. Fix an algebraic closure $$\mathbb{L}$$ of $$\mathbb{K}$$ and consider the three sets
    
    $$\Hom_\Alg{\mathbb{K}}(A, \mathbb{L}),\qquad \Hom_\Alg{\mathbb{K}}(B, \mathbb{L}),\qquad \Hom_\Alg{\mathbb{K}}(A\otimes_\mathbb{K}B, \mathbb{L})$$

    Then the claim follows immediately from the fact that the map

    $$\Hom_\Alg{\mathbb{K}}(A,\mathbb{L})\times \Hom_\Alg{\mathbb{K}}(B, \mathbb{L}) \rightarrow \Hom_\Alg{\mathbb{K}}(A\otimes_\mathbb{K}B,\mathbb{L}); \quad (u,v)\mapsto u\otimes v$$

    is a bijection.
2. Let $$\mathbb{L}$$ be an algebraic closure of $$\mathbb{K}'$$. Then the morphism
    
    $$\bar{u}(x) = u(1 \otimes x) \quad (x \in A)$$
    
    defines a bijection between the set of $$\mathbb{K}'$$-algebra homomorphisms $$u$$ and the set of $$\mathbb{K}$$-algebra homomorphisms $$\bar{u}$$. Hence the equality holds.
3. Similarly, let $$\mathbb{L}$$ be an algebraic closure of $$\mathbb{K}'$$. Consider the two sets $$\Hom_{\Alg{\mathbb{K}}}(\mathbb{K}', \mathbb{L})$$ and $$\Hom_\Alg{\mathbb{K}}(A', \mathbb{L})$$. For each $$u\in\Hom_{\Alg{\mathbb{K}}}(\mathbb{K}', \mathbb{L})$$ consider the set
    
    $$\Hom_\Alg{\mathbb{K}}(A', \mathbb{L})_u=\left\{v\in \Hom_{\Alg{\mathbb{K}}}(A', \mathbb{L})\mid\text{$v(x\cdot 1)=u(x)$ for all $x\in \mathbb{K}'$}\right\}$$

    These induce the partition 

    $$\Hom_\Alg{\mathbb{K}}(A', \mathbb{L})=\bigsqcup_{u\in \Hom_\Alg{\mathbb{K}}(\mathbb{K}', \mathbb{L})} \Hom_\Alg{\mathbb{K}}(A', \mathbb{L})_u$$

    Now for each fixed $$u$$, since $$\mathbb{L}$$ is an algebraic closure of $$\mathbb{K}'$$, the above set $$\Hom_\Alg{\mathbb{K}}(A', \mathbb{L})_u$$ has size $$[A':\mathbb{K}']$$ by definition. From this we obtain the desired equality.

</details>

In this language [Corollary 7](#cor7) translates as follows.

<div class="proposition" markdown="1">

<ins id="prop13">**Proposition 13**</ins> For a finite degree commutative $$\mathbb{K}$$-algebra $$A$$, we have $$[A:\mathbb{K}]_s\leq [A:\mathbb{K}]$$, and equality holds when $$A$$ is an étale algebra.

</div>

In particular, combining this with [Proposition 12](#prop12) we obtain the following corollary.

<div class="proposition" markdown="1">

<ins id="cor14">**Corollary 14**</ins> The following hold.

1. For any two commutative $$\mathbb{K}$$-algebras $$A,B$$, the tensor product $$A\otimes_\mathbb{K}B$$ is étale if and only if each of them is étale.
2. For any extension $$\mathbb{K}'/\mathbb{K}$$, a $$\mathbb{K}$$-algebra $$A$$ is étale if and only if $$A_{(\mathbb{K}')}$$ is étale.
3. For any extension $$\mathbb{K}'/\mathbb{K}$$ and any $$\mathbb{K}'$$-algebra $$A'$$, $$A'$$ is étale over $$\mathbb{K}$$ if and only if $$A'$$ is étale over $$\mathbb{K}'$$ and $$\mathbb{K}'$$ is étale over $$\mathbb{K}$$.

</div>
