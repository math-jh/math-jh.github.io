---
title: "Fundamental Theorem of Galois Theory"
description: "This post proves the Fundamental Theorem of Galois Theory and discusses the correspondence between intermediate fields of a Galois extension and closed subgroups of the Galois group."
excerpt: "Galois correspondence between subgroups and intermediate fields"

categories: [Math / Field Theory]
permalink: /en/math/field_theory/fundamental_theorem_of_galois_theory
sidebar: 
    nav: "field_theory-en"

date: 2025-06-27
weight: 10
translated_at: 2026-09-07T07:15:04+00:00
translation_source: antigravity-gemini-3.8-flash-high
---
## Statement and Applications of the Fundamental Theorem

We now finally prove the fundamental theorem of Galois theory. We begin by stating it and examining its consequences before proceeding to the proof.

::: Theorem 1
For a field $\mathbb{K}$, consider a Galois extension $\mathbb{L}/\mathbb{K}$ and its Galois group $\Gamma=\Gal(\mathbb{L}/\mathbb{K})$. Let $\Ext(\mathbb{L}/\mathbb{K})$ be the collection of subextensions of $\mathbb{L}$, and let $\SubGrp_{\cl}(\Gamma)$ be the collection of closed subgroups of $\Gamma$. Then the two functions between $\Ext(\mathbb{L}/\mathbb{K})$ and $\SubGrp_{\cl}(\Gamma)$,

$$k:\SubGrp_{\cl}(\Gamma)\rightarrow\Ext(\mathbb{L}/\mathbb{K});\qquad G\mapsto k(G)\text{ the field of invariants of $G$}$$

and 

$$g:\Ext(\mathbb{L}/\mathbb{K})\rightarrow\SubGrp_{\cl}(\Gamma);\qquad \mathbb{M}\mapsto g(\mathbb{M})\text{ the group of $\mathbb{M}$-automorphisms of $\mathbb{L}$}$$

are inverses of each other. 
:::

In general, if $\mathbb{L}/\mathbb{K}$ is an infinite degree Galois extension, the condition of being a *closed* subgroup in the theorem above is an essential statement; however, if $\mathbb{L}/\mathbb{K}$ is a finite degree Galois extension, then as seen in [§Properties of Galois Groups, ⁋Example 1](/en/math/field_theory/properties_of_galois_extensions#ex1), $\Gal(\mathbb{L}/\mathbb{K})$ is a discrete space, and therefore every subgroup is closed, so in this case [Theorem 1](#thm1) recovers the classical fundamental theorem of Galois theory as a correspondence between subextensions and subgroups.

::: Proposition 2
For a finite degree Galois extension $\mathbb{L}/\mathbb{K}$, we have $\lvert\Gal(\mathbb{L}/\mathbb{K})\rvert=[\mathbb{L}:\mathbb{K}]$.
:::
::: Proof
Our claim is that the set of automorphisms of $\mathbb{L}$ over $\mathbb{K}$ is in one-to-one correspondence precisely with the homomorphisms from $\mathbb{L}$ to $\overline{\mathbb{K}}$ over $\mathbb{K}$. First, given an automorphism of $\mathbb{L}$ over $\mathbb{K}$, composing it with the inclusion from $\mathbb{L}$ into $\overline{\mathbb{K}}$ gives a $\mathbb{K}$-homomorphism $\mathbb{L} \rightarrow \overline{\mathbb{K}}$. Conversely, suppose a $\mathbb{K}$-homomorphism $u:\mathbb{L} \rightarrow \overline{\mathbb{K}}$ is given. Since $\mathbb{L}/\mathbb{K}$ is quasi-Galois, by the fourth condition of [§Galois Extensions, ⁋Proposition 5](/en/math/field_theory/galois_extension#prop5), the image of $u$ is contained in $\mathbb{L}$, and thus $u$ can be viewed as an endomorphism of $\mathbb{L}$ over $\mathbb{K}$. A field homomorphism is always injective, and since $\mathbb{L}/\mathbb{K}$ is of finite degree, an injective $\mathbb{K}$-linear endomorphism is surjective ([\[Linear Algebra\] §Isomorphisms, ⁋Theorem 7](/en/math/linear_algebra/isomorphic_vector_spaces#thm7)). That is, $u$ is an automorphism of $\mathbb{L}$ over $\mathbb{K}$, and one can easily verify that these correspondences are inverses of each other.

Therefore, $\lvert\Gal(\mathbb{L}/\mathbb{K})\rvert$ is the number of homomorphisms from $\mathbb{L}$ into $\overline{\mathbb{K}}$ over $\mathbb{K}$, which is the separable degree $[\mathbb{L}:\mathbb{K}]_s$ ([§Étale Algebras, ⁋Definition 10](/en/math/field_theory/etale_algebras#def10)). Since $\mathbb{L}/\mathbb{K}$ is a finite degree separable extension, it is an étale algebra ([§Separable Extensions, ⁋Definition 8](/en/math/field_theory/separable_extensions#def8)), and thus by [§Étale Algebras, ⁋Proposition 13](/en/math/field_theory/etale_algebras#prop13), this value equals $[\mathbb{L}:\mathbb{K}]$.
:::

We now examine concrete applications of [Theorem 1](#thm1). First, we consider the following simplest example.

::: Example 3
Let $\mathbb{L}=\mathbb{Q}(\sqrt{2},\sqrt{3})$. Since this is the splitting field of the polynomial $(\x^2-2)(\x^2-3)\in\mathbb{Q}[\x]$, it is quasi-Galois by the last condition of [§Galois Extensions, ⁋Proposition 5](/en/math/field_theory/galois_extension#prop5). On the other hand, since every algebraic extension of $\mathbb{Q}$ is separable by [§Fields, ⁋Proposition 18](/en/math/field_theory/fields#prop18) ([§Separable Extensions, ⁋Proposition 9](/en/math/field_theory/separable_extensions#prop9)), $\mathbb{L}/\mathbb{Q}$ is a Galois extension by the second condition of [§Galois Extensions, ⁋Theorem 8](/en/math/field_theory/galois_extension#thm8).

First, $\sqrt{3}\not\in\mathbb{Q}(\sqrt{2})$. Indeed, if $\sqrt{3}=a+b\sqrt{2}$, squaring both sides yields $3=a^2+2b^2+2ab\sqrt{2}$; since $\sqrt{2}$ is irrational, we must have $ab=0$, but $b=0$ implies that $\sqrt{3}$ is rational, and $a=0$ implies that $\sqrt{3/2}$ is rational, both of which are contradictions. Therefore, $\mathbb{L}/\mathbb{Q}$ has $\mathbb{Q}(\sqrt{2})$ as an intermediate field, so $[\mathbb{L}:\mathbb{Q}]=[\mathbb{L}:\mathbb{Q}(\sqrt{2})][\mathbb{Q}(\sqrt{2}):\mathbb{Q}]=4$, and by [Proposition 2](#prop2), $\lvert\Gal(\mathbb{L}/\mathbb{Q})\rvert=4$.

Meanwhile, since $\mathbb{L}$ is generated by the roots of $f=(\x^2-2)(\x^2-3)$, by the discussion following [§Galois Extensions, ⁋Definition 12](/en/math/field_theory/galois_extension#def12), we obtain an injective homomorphism given by permutations of these roots

$$\Gal(\mathbb{L}/\mathbb{Q})\rightarrow S_4$$

and considering the irreducible factors of $f$, namely $\x^2-2$ and $x^2-3$, the image is contained in the product of the symmetric groups of the solution sets $\{\pm\sqrt{2}\}$ and $\{\pm\sqrt{3}\}$. That is, the image lands in $S_2\times S_2\subset S_4$, and counting the number of elements shows that this is an isomorphism.

Specifically, since the three non-identity elements in $S_2\times S_2$ all have order $2$, the only non-trivial proper subgroups are the three generated by each of them; on the $\Gal(\mathbb{L}/\mathbb{Q})$ side, these are the subgroups generated respectively by the automorphism changing only the sign of $\sqrt{3}$, $\sigma$, the automorphism changing only the sign of $\sqrt{2}$, $\tau$, and $\sigma\tau$. From the tower $\mathbb{L}/\mathbb{Q}(\sqrt{2})/\mathbb{Q}$ above, $\{1,\sqrt{2},\sqrt{3},\sqrt{6}\}$ is a basis of $\mathbb{L}$ over $\mathbb{Q}$, so for $x=a+b\sqrt{2}+c\sqrt{3}+d\sqrt{6}$, we have

$$\sigma(x)=a+b\sqrt{2}-c\sqrt{3}-d\sqrt{6},\qquad \tau(x)=a-b\sqrt{2}+c\sqrt{3}-d\sqrt{6},\qquad \sigma\tau(x)=a-b\sqrt{2}-c\sqrt{3}+d\sqrt{6}$$

and thus the fixed fields of the three subgroups are $\mathbb{Q}(\sqrt{2})$, $\mathbb{Q}(\sqrt{3})$, and $\mathbb{Q}(\sqrt{6})$, respectively. By [Theorem 1](#thm1), these are all the non-trivial subextensions of $\mathbb{L}$.
:::

In the previous example, the Galois group was abelian, so every subgroup was normal. The following is the smallest example where this is not the case.

::: Example 4
First, let $\alpha=\sqrt[3]{2}$, $\omega=e^{2\pi i/3}$, and let $\mathbb{L}=\mathbb{Q}(\alpha,\omega)$. Then $\alpha$ is a root of $\x^3-2$ and $\omega$ is a root of $\x^2+\x+1$. Also, if we only adjoin $\alpha$, the field $\mathbb{Q}(\alpha)$ *cannot* be a splitting field of $\x^3-2$, but if we adjoin $\omega$ as well, since the three roots of $\x^3-2$ are $\alpha$, $\omega\alpha$, and $\omega^2\alpha$, the field $\mathbb{L}=\mathbb{Q}(\alpha,\omega)$ becomes a splitting field of $\x^3-2$. Furthermore, for the same reason as in the previous example, $\mathbb{L}/\mathbb{Q}$ is a Galois extension. 

Since $\x^3-2$ is a cubic polynomial with no rational roots, it is irreducible over $\mathbb{Q}$, and thus $[\mathbb{Q}(\alpha):\mathbb{Q}]=3$. Since $\mathbb{Q}(\alpha)$ is contained in $\mathbb{R}$ and does not contain $\omega$, over $\mathbb{Q}(\alpha)$ the minimal polynomial of $\omega$ is $\x^2+\x+1$. That is, $[\mathbb{L}:\mathbb{Q}]=6$, and by [Proposition 2](#prop2), $\lvert\Gal(\mathbb{L}/\mathbb{Q})\rvert=6$. On the other hand, since $\omega=(\omega\alpha)/\alpha$, the field $\mathbb{L}$ is generated precisely by the roots of $\x^3-2$, and hence, as in the discussion following [§Galois Extensions, ⁋Definition 12](/en/math/field_theory/galois_extension#def12), we obtain an injective homomorphism $\Gal(\mathbb{L}/\mathbb{Q})\rightarrow S_3$ given by permutations of the roots. Since both sides have six elements, this is an isomorphism.

Earlier in [Example 3](#ex3), the way elements of $\Gal(\mathbb{L}/\mathbb{Q})$ act on the set of roots was fairly obvious, but the action in this example is slightly more complicated. 

Now let us examine what the elements of $S_3$ do to the three roots under this isomorphism. An element of order $3$ permutes the three roots cyclically; for instance, with $\alpha\mapsto\omega\alpha\mapsto\omega^2\alpha\mapsto\alpha$, the element $\sigma$ satisfies $\sigma(\omega)=\sigma(\omega\alpha)/\sigma(\alpha)=\omega^2\alpha/(\omega\alpha)=\omega$, so $\sigma$ fixes $\omega$. An element of order $2$ swaps two roots and fixes the remaining one; for example, the automorphism given by complex conjugation fixes the real number $\alpha$ and swaps $\omega\alpha$ and $\omega^2\alpha$. Therefore, the nontrivial proper subgroups of $S_3$ are one subgroup formed by elements of order $3$, $A_3$, and, for each $i$, the subgroup fixing $\omega^i\alpha$, giving three subgroups of order $2$.

Then, by [Theorem 1](#thm1), these four subgroups correspond to all nontrivial subextensions of $\mathbb{L}$. For each subgroup $H$, the extension $\mathbb{L}/k(H)$ is a Galois extension and its Galois group is $H$ ([Lemma 7](#lem7)), so by [Proposition 2](#prop2) we have $[\mathbb{L}:k(H)]=\lvert H\rvert$; thus, to $A_3$ corresponds a subextension of degree $2$, and to the remaining three correspond subextensions of degree $3$.

We can identify these from the fixed elements determined above. Since the elements of $A_3$ fix $\omega$, the fixed field $k(A_3)$ contains $\mathbb{Q}(\omega)$, and since the minimal polynomial of $\omega$ is $\x^2+\x+1$, over $\mathbb{Q}$ both have degree $2$, and therefore they are equal. Similarly, for the subgroup fixing $\omega^i\alpha$ of order $2$, the fixed field contains $\mathbb{Q}(\omega^i\alpha)$, and since $\omega^i\alpha$ is a root of the irreducible polynomial $\x^3-2$, both have degree $3$, and thus they are equal as well.

On the other hand, a field containing two distinct roots of $\x^3-2$ contains their ratio, which is $\omega$ or $\omega^2$, and hence contains $\omega$ either way, becoming all of $\mathbb{L}$. Thus, the three fields above of degree $3$ are distinct and each contains only one root of $\x^3-2$; therefore, they do not satisfy the second condition of [§Galois Extensions, ⁋Proposition 5](/en/math/field_theory/galois_extension#prop5) and are not quasi-Galois extensions of $\mathbb{Q}$. Nevertheless, they are mapped to one another by elements of $\Gal(\mathbb{L}/\mathbb{Q})$."
:::

Now, let us examine an example showing why the closed condition appearing in the statement of [Theorem 1](#thm1) is necessary. When the Galois group is infinite, not all subgroups, but only the closed ones among them, correspond to subextensions.

::: Example 5
Fix a prime $p$ and consider the algebraic closure $\overline{\mathbb{F}}_p$ of $\mathbb{F}_p$. Since $\mathbb{F}_p$ is a finite set, it is perfect ([§Fields, ⁋Proposition 18](/en/math/field_theory/fields#prop18)), and hence all its algebraic extensions are separable ([§Separable Extensions, ⁋Proposition 9](/en/math/field_theory/separable_extensions#prop9)). Meanwhile, $\overline{\mathbb{F}}_p$ is the splitting field of all non-constant polynomials in $\mathbb{F}_p[\x]$, so by the fifth condition of [§Galois Extensions, ⁋Proposition 5](/en/math/field_theory/galois_extension#prop5), it is quasi-Galois; that is, $\overline{\mathbb{F}}_p/\mathbb{F}_p$ is a Galois extension. Let us denote its Galois group by $\Gamma$.

Since $\overline{\mathbb{F}}_p$ is also perfect ([§Separable Degree, ⁋Corollary 3](/en/math/field_theory/separable_degree#cor3)), the Frobenius endomorphism $\varphi:x\mapsto x^p$ is an automorphism of $\overline{\mathbb{F}}_p$, and since the elements of $\mathbb{F}_p$ are roots of $\x^p-\x$, we have $\varphi\in\Gamma$. Conversely, $\varphi(x)=x$ means that $x$ is a root of $\x^p-\x$, but this polynomial has at most $p$ roots, and the $p$ elements of $\mathbb{F}_p$ are already all roots. Therefore, for the subgroup $H$ generated by $\varphi$,

$$k(H)=\mathbb{F}_p=k(\Gamma)$$

holds. Thus, as long as $H\neq\Gamma$, the map $k$ is not injective on the set of all subgroups.

To verify this, for each $n\geq1$, let $\mathbb{F}_{p^n}$ be the set of roots of $\x^{p^n}-\x$ in $\overline{\mathbb{F}}_p$. Since this is the collection of elements fixed by $\varphi^n$, it is a subfield, and because the derivative of $\x^{p^n}-\x$ is $-1$, it has no multiple roots ([\[Ring Theory\] §Polynomial Rings, ⁋Proposition 11](/en/math/ring_theory/polynomial_rings#prop11)), so it has exactly $p^n$ elements. Then $\mathbb{F}_{p^n}$ has dimension $n$ as an $\mathbb{F}_p$-vector space, so $[\mathbb{F}_{p^n}:\mathbb{F}_p]=n$; since it is the splitting field of $\x^{p^n}-\x$, it is quasi-Galois, and as seen above, it is separable, so $\mathbb{F}_{p^n}/\mathbb{F}_p$ is a finite degree Galois extension. On the other hand, if $\varphi^d$ is the identity map on $\mathbb{F}_{p^n}$, then all $p^n$ elements are roots of $\x^{p^d}-\x$, so $n\leq d$. Hence the order of $\varphi\vert_{\mathbb{F}_{p^n}}$ is exactly $n$, and by [Proposition 2](#prop2),

$$\Gal(\mathbb{F}_{p^n}/\mathbb{F}_p)=\langle\varphi\vert_{\mathbb{F}_{p^n}}\rangle\cong\mathbb{Z}/n\mathbb{Z}$$

where the last isomorphism sends $\varphi\vert_{\mathbb{F}_{p^n}}$ to $1$.

Now, when $m\mid n$, since $x^{p^m}=x$ implies $x^{p^{n}}=x$, we have $\mathbb{F}_{p^m}\subseteq\mathbb{F}_{p^n}$, and in particular $\mathbb{F}_{p^m}$ and $\mathbb{F}_{p^n}$ are always both contained in $\mathbb{F}_{p^{mn}}$. Also, for any $x\in\overline{\mathbb{F}}_p$, if we set $d=[\mathbb{F}_p(x):\mathbb{F}_p]$, then $\mathbb{F}_p(x)$ is a field with $p^d$ elements, and since the order of its group of units is $p^d-1$ ([\[Algebraic Structures\] §Quotient Groups, ⁋Proposition 5](/en/math/algebraic_structures/quotient_groups#prop5)), we have $x^{p^d-1}=1$ when $x\neq0$. Combined with the case $x=0$, we always have $x^{p^d}=x$, that is, $x\in\mathbb{F}_{p^d}$. Thus $\overline{\mathbb{F}}_p$ is the union of the $\mathbb{F}_{p^n}$, and applying [§Properties of Galois Groups, ⁋Proposition 5](/en/math/field_theory/properties_of_galois_extensions#prop5) to this family, the map induced by the restrictions

$$\Gamma\cong\varprojlim_n\Gal(\mathbb{F}_{p^n}/\mathbb{F}_p)\cong\varprojlim_n\mathbb{Z}/n\mathbb{Z}$$

is an isomorphism of topological groups. Here the inverse limit on the right is with respect to the reduction maps for $m\mid n$, and $\varphi^k$ corresponds to the element given in each component by the residue class of $k$.

Now write each natural number $n$ as $n=2^am$ ($m$ odd), and let $c_n\in\mathbb{Z}/n\mathbb{Z}$ be the unique residue class such that $c_n\equiv0\pmod{2^a}$ and $c_n\equiv1\pmod m$. If $n'\mid n$, then $a'$ and $m'$ of $n'=2^{a'}m'$ satisfy $a'\leq a$ and $m'\mid m$ respectively, so the remainder of $c_n$ divided by $n'$ is $c_{n'}$, and thus $(c_n)_n$ is an element of the inverse limit above. If this corresponded to some $\varphi^k$, then from the components with $n=2^a$ we would have $2^a\mid k$ for all $a$, which implies $k=0$, but the component with $n=3$ requires $k\equiv1\pmod 3$, which is impossible. That is, $(c_n)_n$ is an element of $\Gamma$ that does not belong to $H$ cultural.

Meanwhile, the closure $\overline{H}$ of $H$ is again a subgroup, and from $H\subseteq\overline{H}\subseteq\Gamma$, since $k(\overline{H})$ lies between $k(\Gamma)=\mathbb{F}_p$ and $k(H)=\mathbb{F}_p$, we have $k(\overline{H})=\mathbb{F}_p$. Then applying [Theorem 1](#thm1) to the closed subgroup $\overline{H}$, we obtain $\overline{H}=g(\mathbb{F}_p)=\Gamma$. That is, $H$ is a dense but not closed subgroup of $\Gamma$.
:::

The second part of the fundamental theorem tells us what normal subgroups correspond to under this correspondence.

::: Corollary 6
In the setting of [Theorem 1](#thm1), a closed subgroup $H\in\SubGrp_{\cl}(\Gamma)$ is a normal subgroup of $\Gal(\mathbb{L}/\mathbb{K})$ if and only if $\mathbb{M}=k(H)$ is a Galois extension of $\mathbb{K}$. In this case, the restriction induces a group isomorphism

$$\Gal(\mathbb{L}/\mathbb{K})/H\cong \Gal(\mathbb{M}/\mathbb{K})$$
:::
::: Proof
We begin with a simple computation. For any closed subgroup $H$ and $\sigma\in\Gal(\mathbb{L}/\mathbb{K})$, an element $x\in \mathbb{L}$ is fixed by every element of $\sigma H\sigma^{-1}$ if and only if $\sigma^{-1}(x)$ is fixed by every element of $H$, so

$$\mathbb{L}^{\sigma H\sigma^{-1}}=\sigma(\mathbb{L}^H)=\sigma(\mathbb{M})\tag{$\ast$}$$

holds.

Now assume that $H$ is a normal subgroup. Then by $(\ast)$, for any $\sigma\in\Gal(\mathbb{L}/\mathbb{K})$ we have $\sigma(\mathbb{M})=\mathbb{M}$, so the restriction $\rho:\Gal(\mathbb{L}/\mathbb{K}) \rightarrow \Aut_\mathbb{K}(\mathbb{M})$ is well-defined. If an element of $\mathbb{M}$, $x$, is fixed by every element in the image of $\rho$, then $x$ is fixed by all of $\Gal(\mathbb{L}/\mathbb{K})$, and since $\mathbb{L}/\mathbb{K}$ is Galois, $x\in \mathbb{K}$. In particular, the invariants of the group of all automorphisms of $\mathbb{M}$ over $\mathbb{K}$ are contained in $\mathbb{K}$, and thus by the first condition of [§Galois Extensions, ⁋Theorem 8](/en/math/field_theory/galois_extension#thm8), $\mathbb{M}/\mathbb{K}$ is a Galois extension.

Conversely, suppose that $\mathbb{M}/\mathbb{K}$ is a Galois extension. Then in particular $\mathbb{M}/\mathbb{K}$ is quasi-Galois, so by [§Galois Extensions, ⁋Proposition 5](/en/math/field_theory/galois_extension#prop5), any $\sigma\in \Gal(\mathbb{L}/\mathbb{K})$ satisfies $\sigma(\mathbb{M})=\mathbb{M}$. Then by $(\ast)$ and the correspondence of [Theorem 1](#thm1),

$$\sigma H\sigma^{-1}=g\bigl(\sigma(\mathbb{M})\bigr)=g(\mathbb{M})=H$$

holds, so $H$ is a normal subgroup. Here, $\sigma H\sigma^{-1}$ is closed because conjugation is a homeomorphism of a topological group.

Finally, we verify the isomorphism. When $\mathbb{M}/\mathbb{K}$ is Galois, the restriction defined above is a group homomorphism $\rho:\Gal(\mathbb{L}/\mathbb{K}) \rightarrow \Gal(\mathbb{M}/\mathbb{K})$, and its kernel is the set of elements fixing $\mathbb{M}$, that is, $g(\mathbb{M})=g(k(H))=H$. Meanwhile, the fact that $\rho$ is surjective is as in [§Galois Extensions, ⁋Proposition 13](/en/math/field_theory/galois_extension#prop13). This is because any $\tau\in\Gal(\mathbb{M}/\mathbb{K})$ extends to an automorphism of $\overline{\mathbb{K}}$ over $\mathbb{K}$ by [§Galois Extensions, ⁋Proposition 1](/en/math/field_theory/galois_extension#prop1), and since $\mathbb{L}/\mathbb{K}$ is quasi-Galois, restricting this extension to $\mathbb{L}$ yields an extension of $\tau$ in $\Gal(\mathbb{L}/\mathbb{K})$. Therefore, by the first isomorphism theorem, $\Gal(\mathbb{L}/\mathbb{K})/H\cong\Gal(\mathbb{M}/\mathbb{K})$.
:::

The three subgroups of order $2$ in [Example 4](#ex4) are conjugate to each other and thus not normal, and indeed the corresponding subfields $\mathbb{Q}(\omega^i\alpha)$ were not Galois extensions of $\mathbb{Q}$. On the other hand, $A_3$ is a normal subgroup, and $\mathbb{Q}(\omega)$ is the splitting field of $\x^2+\x+1$ and hence a Galois extension of $\mathbb{Q}$; in this case, the isomorphism of [Corollary 6](#cor6) is $S_3/A_3\cong\Gal(\mathbb{Q}(\omega)/\mathbb{Q})$.

## Proof of the Fundamental Theorem

We prove [Theorem 1](#thm1) in two steps as follows.

::: Lemma 7
For any subextension $\mathbb{M}\in \Ext(\mathbb{L}/\mathbb{K})$, the extension $\mathbb{L}/\mathbb{M}$ is also a Galois extension. Viewing an $\mathbb{M}$-automorphism as a $\mathbb{K}$-automorphism so that we regard the Galois group $\Gal(\mathbb{L}/\mathbb{M})$ as a subgroup of $\Gal(\mathbb{L}/\mathbb{K})$, this is a *closed* subgroup of $\Gal(\mathbb{L}/\mathbb{K})$, and therefore $g$ is well-defined.
:::
::: Proof
First, we show that $\mathbb{L}/\mathbb{M}$ is a Galois extension. Since $\mathbb{L}/\mathbb{K}$ is algebraic, $\mathbb{L}/\mathbb{M}$ is also algebraic. For any $x\in \mathbb{L}$, let the minimal polynomial of $x$ over $\mathbb{K}$ be $f$, and let the minimal polynomial over $\mathbb{M}$ be $g$. Since $f$ is also an element of $\mathbb{M}[\x]$ and $f(x)=0$, $g$ divides $f$ ([§Algebraic Extensions, ⁋Theorem 15](/en/math/field_theory/algebraic_extensions#thm15)). However, since $\mathbb{L}/\mathbb{K}$ is Galois, by the third condition of [§Galois Extensions, ⁋Theorem 8](/en/math/field_theory/galois_extension#thm8), $f$ splits in $\mathbb{L}[\x]$ into a product of distinct linear factors, and hence so does its divisor $g$. That is, $\mathbb{L}/\mathbb{M}$ satisfies the third condition of the same theorem and is therefore a Galois extension.

Now we show that $\Gal(\mathbb{L}/\mathbb{M})$ is closed. As sets,

$$\Gal(\mathbb{L}/\mathbb{M})=\left\{\sigma\in \Gal(\mathbb{L}/\mathbb{K})\mid \text{$\sigma(x)=x$ for all $x\in \mathbb{M}$}\right\}=\bigcap_{x\in \mathbb{M}}\left\{\sigma\mid \sigma(x)=x\right\}$$

holds. However, in the notation for the subbase examined in [§Properties of Galois Groups](/en/math/field_theory/properties_of_galois_extensions), $\{\sigma\mid\sigma(x)=x\}=U_{x,x}\cap\Gal(\mathbb{L}/\mathbb{K})$ is an open set, and its complement is also an open set as the union of the open sets $U_{x,y}$ ($y\neq x$), so these are all clopen. Therefore, $\Gal(\mathbb{L}/\mathbb{M})$ is an intersection of closed sets and thus closed, and that it is a subgroup is clear.
:::

The following lemma is commonly known as *Artin's lemma*, and provides the key counting argument in the proof of [Theorem 1](#thm1).

::: Lemma 8 (Artin)
Let a field $\mathbb{N}$ be given, and let a finite group of automorphisms of $\mathbb{N}$, denoted $H$, be given. If we denote the field of invariants of $H$ by $\mathbb{N}^H$, then $[\mathbb{N}:\mathbb{N}^H]\leq \lvert H\rvert$ holds.
:::
::: Proof
Let $\lvert H\rvert=m$ and write $H=\{\sigma_1,\ldots,\sigma_m\}$, where $\sigma_1=\id_\mathbb{N}$. Suppose, to the contrary, that over $\mathbb{N}^H$ there exist linearly independent elements $x_1,\ldots,x_{m+1}\in \mathbb{N}$.

Consider the following system of homogeneous linear equations

$$\sum_{j=1}^{m+1}\sigma_i(x_j)c_j=0,\qquad i=1,\ldots,m$$

over $\mathbb{N}$ in the unknowns $c_1,\ldots,c_{m+1}$. Since this system has $m$ equations and $m+1$ unknowns, it has a non-trivial solution. Indeed, otherwise, the assignment $(c_j)\mapsto \bigl(\sum_j \sigma_i(x_j)c_j\bigr)_i$ defines a linear map $\mathbb{N}^{m+1} \rightarrow \mathbb{N}^m$ that is injective, and then the image of the standard basis of $\mathbb{N}^{m+1}$ consists, in $\mathbb{N}^m$, of $m+1$ linearly independent elements. Since there exists a basis of $\mathbb{N}^m$ containing these ([\[Linear Algebra\] §Dimension of Vector Spaces, ⁋Proposition 5](/en/math/linear_algebra/dimension#prop5)), $\mathbb{N}^m$ would have a basis of size at least $m+1$, which contradicts [\[Linear Algebra\] §Dimension of Vector Spaces, ⁋Theorem 1](/en/math/linear_algebra/dimension#thm1).

Now, among the non-trivial solutions, choose a solution having the minimal number of non-$0$ components, say $(c_1,\ldots,c_{m+1})$, and rearrange the indices so that $c_1,\ldots,c_r\neq 0$ and $c_{r+1}=\cdots=c_{m+1}=0$. By multiplying the entire solution by $c_r^{-1}$, we may normalize so that $c_r=1$. First, $r\geq 2$, because if $r=1$, the equation corresponding to $\sigma_1=\id_\mathbb{N}$ becomes $x_1c_1=0$, which implies $c_1=0$.

Applying any $\tau\in H$ to each equation, we obtain

$$\sum_{j=1}^{m+1}(\tau\sigma_i)(x_j)\tau(c_j)=0,\qquad i=1,\ldots,m$$

and as $i$ ranges from $1$ to $m$, the elements $\tau\sigma_i$ run through all of $H$, so $(\tau(c_j))_j$ is also a solution to the same system. Hence $(c_j-\tau(c_j))_j$ is also a solution; the $r$-th component of this solution is $c_r-\tau(1)=1-1=0$, and the components from the $(r+1)$-th onward are all $0$, so the number of non-$0$ components is strictly less than $r$. Then by the minimality of $(c_j)$, this solution must be the trivial solution, which means that for all $j$ and all $\tau\in H$, we have $\tau(c_j)=c_j$. In other words, $c_j\in \mathbb{N}^H$.

Then the equation corresponding to $\sigma_1=\id_\mathbb{N}$, namely $\sum_{j}x_jc_j=0$, becomes a non-trivial linear combination among $x_1,\ldots,x_{m+1}$ over $\mathbb{N}^H$, contradicting the assumption that they are linearly independent over $\mathbb{N}^H$.
:::

We can now prove [Theorem 1](#thm1).

::: Proof (Theorem 1)
By [Lemma 7](#lem7), $g$ is well-defined, and for $k$, since every element of $G$ fixes $\mathbb{K}$, the field of invariants $k(G)$ contains $\mathbb{K}$ and is a subfield of $\mathbb{L}$, that is, an element of $\Ext(\mathbb{L}/\mathbb{K})$.

First, we show that $k\circ g=\id_{\Ext(\mathbb{L}/\mathbb{K})}$. For any $\mathbb{M}\in\Ext(\mathbb{L}/\mathbb{K})$, by [Lemma 7](#lem7), $\mathbb{L}/\mathbb{M}$ is a Galois extension, and therefore by the first condition of [§Galois Extensions, ⁋Theorem 8](/en/math/field_theory/galois_extension#thm8), the $\Gal(\mathbb{L}/\mathbb{M})$-invariant elements are all elements of $\mathbb{M}$. Conversely, it is clear that the elements of $\mathbb{M}$ are fixed by $\Gal(\mathbb{L}/\mathbb{M})$, so $k(g(\mathbb{M}))=\mathbb{M}$.

Now we must show that $g\circ k=\id_{\SubGrp_{\cl}(\Gamma)}$. For a closed subgroup $G\in\SubGrp_{\cl}(\Gamma)$, let $\mathbb{M}=k(G)$ and set $G'=g(\mathbb{M})=\Gal(\mathbb{L}/\mathbb{M})$. By definition, the elements of $G$ fix $\mathbb{M}$, so $G\subseteq G'$. Our claim is that $G$ is dense in $G'$.

To this end, let $\sigma\in G'$ be given, along with a basic neighborhood of $\sigma$ in $\Gal(\mathbb{L}/\mathbb{K})$, denoted $U_{\mathbb{M}_0}(\sigma)$, where $\mathbb{M}_0$ is a finite subextension of $\mathbb{L}/\mathbb{K}$. Then $\mathbb{M}(\mathbb{M}_0)$ is a finite degree extension of $\mathbb{M}$, so applying [§Galois Extensions, ⁋Proposition 11](/en/math/field_theory/galois_extension#prop11) to the Galois extension $\mathbb{L}/\mathbb{M}$, there exists, containing $\mathbb{M}(\mathbb{M}_0)$, a finite degree Galois subextension $\mathbb{N}/\mathbb{M}$.

Since $\mathbb{N}/\mathbb{M}$ is quasi-Galois, by [§Galois Extensions, ⁋Proposition 5](/en/math/field_theory/galois_extension#prop5), any $\tau\in \Gal(\mathbb{L}/\mathbb{M})$ maps $\mathbb{N}$ into $\mathbb{N}$, and thus the restriction homomorphism

$$\rho:\Gal(\mathbb{L}/\mathbb{M}) \rightarrow \Gal(\mathbb{N}/\mathbb{M});\qquad \tau\mapsto \tau\vert_\mathbb{N}$$

is well-defined. If we set $H=\rho(G)$, then $H$ is a finite group consisting of automorphisms of $\mathbb{N}$. Now calculating $\mathbb{N}^H$, an element $x\in \mathbb{N}$ is fixed by every element of $H$ if and only if it is fixed by every element of $G$, which is equivalent to $x\in k(G)=\mathbb{M}$. That is, $\mathbb{N}^H=\mathbb{M}$, and by [Lemma 8](#lem8),

$$[\mathbb{N}:\mathbb{M}]\leq \lvert H\rvert$$

holds. On the other hand, since $\mathbb{N}/\mathbb{M}$ is a finite degree Galois extension, by [Proposition 2](#prop2) we have $\lvert\Gal(\mathbb{N}/\mathbb{M})\rvert=[\mathbb{N}:\mathbb{M}]$. Therefore,

$$\lvert H\rvert\leq \lvert\Gal(\mathbb{N}/\mathbb{M})\rvert=[\mathbb{N}:\mathbb{M}]\leq \lvert H\rvert$$

and since $H\subseteq \Gal(\mathbb{N}/\mathbb{M})$ are finite sets of the same size, $H=\Gal(\mathbb{N}/\mathbb{M})$.

In particular, since $\sigma\vert_\mathbb{N}\in \Gal(\mathbb{N}/\mathbb{M})=\rho(G)$, there exists, with $\tau\vert_\mathbb{N}=\sigma\vert_\mathbb{N}$, an element $\tau\in G$. Then since $\mathbb{M}_0\subseteq \mathbb{N}$, we have $\tau\in U_{\mathbb{M}_0}(\sigma)$; that is, every basic neighborhood of $\sigma$ meets $G$. Therefore $G$ is dense in $G'$, and from the assumption that $G$ is closed, $G=G'$.
:::

---

**References**

**[Bou]** N. Bourbaki. *Algebra II: Chapters 4–7*. Springer, 2003.

---
