---
title: "Separable Degree"
description: "We introduce the notion of separable degree and examine the relationship between purely inseparable extensions and separable extensions in algebraic extensions over a field of characteristic p through the conditions of etale algebras."
excerpt: "Decomposition of separable and inseparable degrees"

categories: [Math / Field Theory]
permalink: /en/math/field_theory/separable_degree
sidebar: 
    nav: "field_theory-en"

date: 2025-05-17
weight: 7
translated_at: 2026-06-26T18:00:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-10-08T19:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
## Purely Inseparable Extensions

The least separable extension we can think of is, of course, a $p$-radical extension. For this reason, a $p$-radical extension is often called a *purely inseparable extension*. In this post, we first examine the relationship between $p$-radical extensions and separable extensions, and then describe it using the separable degree.

First, let us prove the following lemma.

::: Lemma 1
For a field $\mathbb{K}$ of characteristic $p\neq 0$, a finite degree commutative $\mathbb{K}$-algebra $A$ is étale if and only if $A=\mathbb{K}[A^p]$. Moreover, in this case, if $(a_i)$ is a $\mathbb{K}$-basis of $A$, then so is $(a_i^p)$.
:::
::: Proof
Consider an algebraic closure $\overline{\mathbb{K}}$ of $\mathbb{K}$. Then for any $u,v\in \Hom_\Alg{\mathbb{K}}(A, \overline{\mathbb{K}})$, if the restrictions of $u,v$ to the subalgebra $\mathbb{K}[A^p]$ are equal, then the identity

$$u(x)^p=u(x^p)=v(x^p)=v(x)^p$$

holds for all $x\in A$, so by definition we know that the inequality

$$[A:\mathbb{K}]_s\leq[\mathbb{K}[A^p]:\mathbb{K}]_s$$

holds. If $A$ is an étale $\mathbb{K}$-algebra, then by the inequality and its equality condition in [§Étale Algebras, ⁋Proposition 13](/en/math/field_theory/etale_algebras#prop13){: data-lid="5nugq" }, we have

$$[A:\mathbb{K}]=[A:\mathbb{K}]_s\leq[\mathbb{K}[A^p]:\mathbb{K}]_s\leq [\mathbb{K}[A^p]:\mathbb{K}]$$

and since $\mathbb{K}[A^p]\subseteq A$ trivially holds in general, we obtain $A=\mathbb{K}[A^p]$.

Conversely, assume that $A=\mathbb{K}[A^p]$ and let us show that $A$ is étale. For this, it suffices to prove the latter condition. Assuming that $(a_i)$ is a $\mathbb{K}$-basis of $A$, the fact that the $(a_i^p)$ generate $\mathbb{K}[A^p]$ as a $\mathbb{K}$-vector space follows from [§Fields, ⁋Proposition 12](/en/math/field_theory/fields#prop12){: data-lid="khen1" }, and then the given assumption $A=\mathbb{K}[A^p]$ implies that the $(a_i^p)$ also generate $A$.

Now, to use the result of [§Separable Extensions, ⁋Theorem 7](/en/math/field_theory/separable_extensions#thm7){: data-lid="zz4m0" }, let us show that $\overline{\mathbb{K}}\otimes_\mathbb{K}A$ is reduced. If we assume that $u^2=0$ for some $u\in\overline{\mathbb{K}}\otimes_\mathbb{K}A$, then $u^p=0$, and from this, if we write $u=\sum \lambda_i\otimes a_i$, then

$$0=u^p=\sum_{i\in I} (\lambda_i\otimes a_i)^p=\sum_{i\in I} \lambda_i^p\otimes a_i^p$$

and thus each $\lambda_i^p$ must be $0$. Since $\overline{\mathbb{K}}$ is (of course) reduced, all the $\lambda_i$ must be $0$, and hence $u=0$, from which we obtain the desired result.
:::

::: Proposition 2
Let $p$ be the characteristic exponent of a field $\mathbb{K}$, and consider an algebraic extension $\mathbb{L}/\mathbb{K}$. Also let $\mathbb{L}=\mathbb{K}(S)$ for a subset $S$. If $\mathbb{L}/\mathbb{K}$ is separable, then for any $n\geq 0$, $\mathbb{L}=\mathbb{K}(S^{p^n})$ holds. Conversely, if $\mathbb{L}/\mathbb{K}$ is a finite degree extension and $\mathbb{L}=\mathbb{K}(S^p)$, then $\mathbb{L}/\mathbb{K}$ is separable.
:::
::: Proof
As always, there is nothing to prove when $p=1$. Thus it suffices to consider only the case $p\neq 1$.

First, assuming $\mathbb{L}=\mathbb{K}(S)$, we have

$$\mathbb{K}(\mathbb{L}^p)=\mathbb{K}(\mathbb{K}(S)^p)=\mathbb{K}(\mathbb{K}^p(S^p))=\mathbb{K}(S^p)$$

so $\mathbb{K}(S^p)=\mathbb{K}(\mathbb{L}^p)=\mathbb{K}[\mathbb{L}^p]$ holds. First, applying [Lemma 1](#lem1){: data-lid="ueoyf" } above to $A=\mathbb{L}$, the case where $\mathbb{L}/\mathbb{K}$ is a finite degree extension is immediate, since this is equivalent to $\mathbb{L}$ being an étale $\mathbb{K}$-algebra. Now even when $\mathbb{L}/\mathbb{K}$ is of infinite degree, any finite degree subextension of $\mathbb{L}/\mathbb{K}$, $\mathbb{L}'/\mathbb{K}$, is separable, so by the preceding discussion,

$$\mathbb{L}'=\mathbb{K}[(\mathbb{L}')^p]\subseteq \mathbb{K}[\mathbb{L}^p]$$

holds, and since $\mathbb{K}[\mathbb{L}^p]$ is the union of the $\mathbb{L}'/\mathbb{K}$, we obtain the desired equality. The equality for arbitrary $n$ follows by a simple induction.
:::

From this we obtain the following two corollaries.

::: Corollary 3
Any algebraic extension of a perfect field $\mathbb{K}$ is perfect.
:::

The proof of this is almost obvious from [Proposition 2](#prop2){: data-lid="dsu0p" }.

Moreover, the following holds.

::: Corollary 4
For a field $\mathbb{K}$, its algebraic closure $\overline{\mathbb{K}}$, and the perfect closure $\mathbb{K}^{p^{-\infty}}$ inside it, a subextension of $\overline{\mathbb{K}}/\mathbb{K}$, $\mathbb{L}/\mathbb{K}$, is separable if and only if $\mathbb{L}$ is linearly disjoint from $\mathbb{K}^{p^{-\infty}}$.
:::
::: Proof
As always, it suffices to consider the situation where $\mathbb{L}/\mathbb{K}$ is of finite degree. Given a basis of $\mathbb{L}/\mathbb{K}$, $(x_i)$, the condition that $\mathbb{L}$ is linearly disjoint from $\mathbb{K}^{p^{-\infty}}$ is equivalent to $(x_i)$ being free over every $\mathbb{K}^{p^{-n}}$, which means that for any family $(a_i)$ and any $n$,

$$\sum x_i a_i^{p^{-n}}=0\implies a_i=0$$

must always hold. Now taking the $p^n$-th power of both sides, we see from this that the $x_i^{p^n}$ must be free, and therefore they must define a basis of $\mathbb{L}$; the converse also holds. Considering dimensions, this is equivalent to $\mathbb{L}=\mathbb{K}(\mathbb{L}^p)$, so we obtain the desired result from [Proposition 2](#prop2){: data-lid="6x0us" }.
:::

## Separable Closure

On the other hand, just as with algebraic closures or perfect closures, we can also define the separable closure. Then, just as the perfect closure in [§Fields, ⁋Theorem 15](/en/math/field_theory/fields#thm15){: data-lid="3h8km" } is the relative perfect closure with respect to the algebraic closure, it is natural to first define the relative separable closure, and then define the relative separable closure inside an algebraic closure as the (absolute) separable closure.

::: Proposition 5
For a field extension $\mathbb{L}/\mathbb{K}$, let $\mathbb{L}_s$ be the set of elements that are algebraic and separable over $\mathbb{K}$. Then $\mathbb{L}_s$ is a subextension of $\mathbb{L}/\mathbb{K}$, and moreover, it is the largest separable algebraic extension contained in $\mathbb{L}$.
:::
::: Proof
First, since every element of a separable extension is separable ([§Separable Extensions, ⁋Proposition 12](/en/math/field_theory/separable_extensions#prop12){: data-lid="8kpyo" }), any separable subextension of $\mathbb{L}$ is always contained in $\mathbb{L}_s$. Conversely, an algebraic extension generated solely by separable elements is likewise separable by [§Separable Extensions, ⁋Proposition 12](/en/math/field_theory/separable_extensions#prop12){: data-lid="r1ury" }, so $\mathbb{K}(\mathbb{L}_s)$ is itself a separable extension, and again by the claim above, $\mathbb{K}(\mathbb{L}_s)\subseteq \mathbb{L}_s$ holds. That is, $\mathbb{K}(\mathbb{L}_s)=\mathbb{L}_s$ holds, so $\mathbb{L}_s$ itself is a subextension of $\mathbb{L}/\mathbb{K}$; combining this with the maximality observed above, we obtain that $\mathbb{L}_s$ is the largest separable subextension.
:::

As mentioned above, we call $\mathbb{L}_s$ the *relative separable algebraic closure* (in $\mathbb{L}/\mathbb{K}$).

The central result of this post is that any algebraic extension always splits completely into a separable part (corresponding to the relative separable closure) and an inseparable part. This can be verified as follows.

::: Theorem 6
For an algebraic extension $\mathbb{L}/\mathbb{K}$ and $\mathbb{L}_s$ defined in [Proposition 5](#prop5){: data-lid="4gpoh" }, the following hold.

1. $\mathbb{L}/\mathbb{L}_s$ is a $p$-radical extension.
2. For a subextension $\mathbb{M}/\mathbb{K}$, suppose that $\mathbb{L}/\mathbb{M}$ is $p$-radical. Then $\mathbb{M}$ contains $\mathbb{L}_s$.
3. $\mathbb{L}_s$ is the unique subextension of $\mathbb{L}$ that is separable over $\mathbb{K}$ and such that $\mathbb{L}$ is $p$-radical over it.
:::
::: Proof
First, for the first claim, the case $\ch(\mathbb{K})=0$ is trivial, so let us consider the case $\ch(\mathbb{K})=p>0$. Now, considering $x\in \mathbb{L}$ and its minimal polynomial $f$, there exists some $m\geq 0$ such that $f\in\mathbb{K}[\x^{p^m}]$ but $f\not\in \mathbb{K}[\x^{p^{m+1}}]$, and in this case we can choose a polynomial $g$ such that $f(\x)=g(\x^{p^m})$. Since $f$ is irreducible, so is $g$, and therefore $g$ is, over $\mathbb{K}$, the minimal polynomial of $x^{p^m}$. Now, from the last equivalent condition of [§Separable Extensions, ⁋Proposition 10](/en/math/field_theory/separable_extensions#prop10){: data-lid="tvjln" }, $g$ is separable, and therefore $x^{p^m}$ belongs to $\mathbb{L}_s$. Thus $x$ is a $p$-radical extension in $\mathbb{L}/\mathbb{L}_s$, and from this we obtain the desired result.

On the other hand, suppose given a subextension $\mathbb{M}/\mathbb{K}$ satisfying the second assumption, and let $x\in \mathbb{L}_s$. Then $x$ is separable over $\mathbb{K}$, and hence also separable over $\mathbb{M}$. However, since $\mathbb{L}/\mathbb{M}$ is $p$-radical, $x$ is, over $\mathbb{M}$, $p$-radical. Again, from the last equivalent condition of [§Separable Extensions, ⁋Proposition 10](/en/math/field_theory/separable_extensions#prop10){: data-lid="ic8mg" }, the minimal polynomial of $x$ over $\mathbb{M}$ must not belong to $\mathbb{M}[\x^p]$, but at the same time, from the condition that $x$ is $p$-radical, for $x$ of height $e$, $\x^{p^e}-x^{p^e}$ must be the minimal polynomial of $x$. Therefore $e=0$, and since $\x-x$ must be the minimal polynomial of $x$, we must have $x\in \mathbb{M}$.

The last claim is obtained by combining the maximality in [Proposition 5](#prop5){: data-lid="2767h" } and the second claim above.
:::

Then, since an algebraic extension being separable is stable under base change, if two subextensions $\mathbb{L}/\mathbb{K}$, $\mathbb{K}'/\mathbb{K}$ of some extension are given, then for the relative separable closure in $\mathbb{L}$ of $\mathbb{K}$, $\mathbb{L}_s$, one can verify that $\mathbb{K}'(\mathbb{L}_s)$ is the relative separable closure of $\mathbb{K}'$ in $\mathbb{K}'(\mathbb{L})$. Also, from the uniqueness of the relative separable closure, for a finite degree extension $\mathbb{L}/\mathbb{K}$, one can verify that the formula

$$\mathbb{L}_s=\bigcap_{n\geq 0} \mathbb{K}(\mathbb{L}^{p^n})$$

holds.

It is clear how to define the (absolute) separable algebraic closure.

::: Definition 7
A field $\mathbb{K}$ is *separably closed* if every separable algebraic extension of $\mathbb{K}$ is trivial. For a field $\mathbb{K}$, if an extension $\mathbb{L}$ is separable algebraic and at the same time $\mathbb{L}$ is separably closed, then this is called a *separable algebraic closure* of $\mathbb{K}$.
:::

Then, since any separable algebraic extension is algebraic, an algebraically closed field is always separably closed. Conversely, since any algebraic extension of a *perfect* field $\mathbb{K}$ is separable, a separably closed perfect field is algebraically closed.

Then the following holds.

::: Proposition 8
Fix an algebraic closure $\overline{\mathbb{K}}$ of a field $\mathbb{K}$. 

1. The relative separable algebraic closure $\overline{\mathbb{K}}_s$ in $\overline{\mathbb{K}}$ is a separable closure of $\mathbb{K}$. 
2. The separable algebraic closure of $\mathbb{K}$ is uniquely determined up to isomorphism.
:::
::: Proof
1. $\overline{\mathbb{K}}_s$ is separable by [Proposition 5](#prop5){: data-lid="ubmb1" }, and since it is a subextension of the algebraic closure $\overline{\mathbb{K}}$, it is algebraic. Therefore, for the claim, it suffices to show that given any separable algebraic extension $\mathbb{L}/\overline{\mathbb{K}}_s$, $\mathbb{L}$ is a trivial extension of $\overline{\mathbb{K}}_s$. First, since the extension $\mathbb{L}/\overline{\mathbb{K}}_s$ is algebraic, there exists a $\overline{\mathbb{K}}_s$-homomorphism $u:\mathbb{L}\rightarrow\overline{\mathbb{K}}$ ([§Algebraic Closure, ⁋Theorem 5](/en/math/field_theory/algebraically_closed_extensions#thm5){: data-lid="lil5u" }), and its image $u(\mathbb{L})$ is separable algebraic by [§Separable Extensions, ⁋Proposition 15](/en/math/field_theory/separable_extensions#prop15){: data-lid="s9k68" }, so $u(\mathbb{L})=\overline{\mathbb{K}}_s$ holds. 
2. Similarly, one can use [§Algebraic Closure, ⁋Theorem 5](/en/math/field_theory/algebraically_closed_extensions#thm5){: data-lid="xpakq" }. 
:::

From this, we see that the separable algebraic closure is the smallest separably closed algebraic extension. That is, if $\mathbb{L}/\mathbb{K}$ is a separable algebraic closure of $\mathbb{K}$, and for a field extension $\mathbb{M}/\mathbb{K}$ the field $\mathbb{M}$ is separably closed, then there exists a morphism $\mathbb{L}\rightarrow\mathbb{M}$. 

## Separable Degree

By [Theorem 6](#thm6){: data-lid="xalgl" }, any finite degree extension $\mathbb{L}/\mathbb{K}$ can be split into a separable part and a non-separable part, and written as $\mathbb{L}/\mathbb{L}_s/\mathbb{K}$.

::: Proposition 9
In the above situation, $[\mathbb{L}:\mathbb{K}]_s=[\mathbb{L}_s:\mathbb{K}]$.
:::
::: Proof
By definition, $[\mathbb{L}:\mathbb{K}]_s$ is defined, with respect to $\mathbb{K}$'s algebraic closure $\overline{\mathbb{K}}$, as the number of homomorphisms from $\mathbb{L}$ to $\overline{\mathbb{K}}$ that are $\mathbb{K}$-algebra homomorphisms. However, $\overline{\mathbb{K}}$ is an algebraically closed field and hence a perfect field, so by [§Purely Inseparable Extensions, ⁋Proposition 6](/en/math/field_theory/purely_inseparable_extensions#prop6){: data-lid="em96f" }, whenever any $\mathbb{K}$-algebra homomorphism $\mathbb{L} \rightarrow \overline{\mathbb{K}}$ is given, restricting it to $\mathbb{L}_s$ defines $\mathbb{L}_s\rightarrow \overline{\mathbb{K}}$, and conversely, whenever a $\mathbb{K}$-algebra homomorphism $\mathbb{L}_s \rightarrow \overline{\mathbb{K}}$ is given, one can extend it to $\mathbb{L}$ to obtain a unique $\mathbb{L}\rightarrow\overline{\mathbb{K}}$. From this we obtain the equality

$$[\mathbb{L}:\mathbb{K}]_s=[\mathbb{L}_s:\mathbb{K}]_s$$

On the other hand, since $\mathbb{L}_s/\mathbb{K}$ is a finite degree separable extension, it is an étale algebra, and therefore by [§Étale Algebras, ⁋Proposition 13](/en/math/field_theory/etale_algebras#prop13){: data-lid="wc9fi" } we have $[\mathbb{L}_s:\mathbb{K}]_s=[\mathbb{L}_s:\mathbb{K}]$, yielding the desired result.
:::

Therefore it is justified to call $[\mathbb{L}:\mathbb{K}]_s$ the *separable degree*. Moreover, from the formula

$$[\mathbb{L}:\mathbb{K}]=[\mathbb{L}:\mathbb{L}_s][\mathbb{L}_s:\mathbb{K}]=[\mathbb{L}:\mathbb{K}]_s[\mathbb{L}:\mathbb{L}_s]$$

we can define the *inseparable degree* of the extension $\mathbb{L}/\mathbb{K}$ as $[\mathbb{L}:\mathbb{K}]_i=[\mathbb{L}:\mathbb{L}_s]$.

If $\ch\mathbb{K}=0$, then $[\mathbb{L}:\mathbb{K}]_i=1$ always holds, and if $\ch\mathbb{K}=p$, then $[\mathbb{L}:\mathbb{K}]_i$ is always a power of $p$. ([Theorem 6](#thm6){: data-lid="9ye69" }) However, since there are plenty of polynomials that do not define a $p$-radical extension and have degree $p^e$, there is no way to determine the value of $[\mathbb{L}:\mathbb{K}]_i$ from (say) $[\mathbb{L}:\mathbb{K}]$ alone.

Nevertheless, the following still holds.

::: Proposition 10
Fix an extension $\Omega/\mathbb{K}$, and consider two finite degree subextensions of $\Omega$, $\mathbb{L}/\mathbb{K}$, $\mathbb{M}/\mathbb{K}$. The following hold.

1. If $\mathbb{L}\subseteq \mathbb{M}$, then $[\mathbb{M}:\mathbb{K}]_s=[\mathbb{M}:\mathbb{L}]_s[\mathbb{L}:\mathbb{K}]_s$ and $[\mathbb{M}:\mathbb{K}]_i=[\mathbb{M}:\mathbb{L}]_i[\mathbb{L}:\mathbb{K}]_i$.
2. For any subextension of $\Omega$, $\mathbb{K}'$, the following formulas
    
    $$[\mathbb{K}'(\mathbb{L}):\mathbb{K}']_s\leq [\mathbb{L}:\mathbb{K}]_s,\qquad [\mathbb{K}'(\mathbb{L}):\mathbb{K}']_i\leq [\mathbb{L}:\mathbb{K}]_i$$

    hold, and equality holds when $\mathbb{K}'$ and $\mathbb{L}$ are linearly disjoint.
3. The two inequalities
    
    $$[\mathbb{K}(\mathbb{L}\cup \mathbb{M}):\mathbb{K}]_s\leq [\mathbb{L}:\mathbb{K}]_s[\mathbb{M}:\mathbb{K}]_s,\qquad [\mathbb{K}(\mathbb{L}\cup \mathbb{M}):\mathbb{K}]_i\leq [\mathbb{L}:\mathbb{K}]_i[\mathbb{M}:\mathbb{K}]_i$$

    hold, and equality holds when $\mathbb{L},\mathbb{M}$ are linearly disjoint.
:::

The proofs of these are almost tautological; for example, the first result follows from [§Algebraic Extensions, ⁋Proposition 2](/en/math/field_theory/algebraic_extensions#prop2){: data-lid="u4rqg" } and [§Étale Algebras, ⁋Proposition 12](/en/math/field_theory/etale_algebras#prop12){: data-lid="41nc1" }. As for the remaining results, since analogous results hold respectively for the extension degree and the separable degree, they hold naturally for the inseparable degree as well.

---

**References**

**[Bou]** N. Bourbaki. *Algebra II: Chapters 4–7*. Springer, 2003.
