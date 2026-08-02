---
title: "Purely Inseparable Extensions"
description: "In a field extension with characteristic exponent p, we define p-radical elements and their height, and determine their minimal polynomials. We then discuss the existence and uniqueness of p-radical closures and perfect closures."
excerpt: "Definition and role of p-radical extensions in Galois theory"

categories: [Math / Field Theory]
permalink: /en/math/field_theory/purely_inseparable_extensions
sidebar: 
    nav: "field_theory-en"

date: 2025-05-15
weight: 4
translated_at: 2026-08-02T18:15:03+00:00
translation_source: kimi-cli
last_polished_at: 2026-08-02T18:15:03+00:00
---
Let us examine the overarching theme of Galois theory through a very simple example. Consider the degree $4$ extension $\mathbb{Q}(\sqrt{2}, \sqrt{3})$ of $\mathbb{Q}$: the newly adjoined elements $\sqrt{2}$ and $\sqrt{3}$ arise from their minimal polynomials over $\mathbb{Q}$,

$$\x^2-2,\qquad \x^2-3.$$

However, each of these polynomials has two roots, $\pm\sqrt{2}$ and $\pm\sqrt{3}$, and there is no algebraic way to distinguish these roots within $\mathbb{Q}$. Thus, if we consider the action that permutes these roots (or equivalently, the $\mathbb{Q}$-automorphisms of $\mathbb{Q}(\sqrt{2},\sqrt{3})$), namely the permutation group $S_2\times S_2$, this is a subgroup of $S_4$.

In this manner, whenever a polynomial is given we can define an appropriate Galois group, and the philosophy of Galois theory is that studying these groups allows us to classify extensions of $\mathbb{Q}$.

Yet, following this philosophy, if a minimal polynomial has a repeated root then defining a permutation action becomes rather awkward. This is a mere coincidence over $\mathbb{Q}$, but in some situations this can actually occur.

::: remark {#rmk}
Every field appearing in this post has characteristic exponent $p$.
:::

## Purely Inseparable Extensions

::: Definition 1
For a field extension $\mathbb{L}/\mathbb{K}$, an element $x\in \mathbb{L}$ is called *$p$-radical* if there exists some $m\geq 0$ such that $x^{p^m}\in \mathbb{K}$. The smallest such $m$ is called the *height* of $x$.
:::

If $p=1$, the above definition is essentially meaningless, and the same holds for the rest of the content in this post. In other words, the content of this post is essentially all about fields of characteristic $p$.

::: Proposition 2
Fix a field extension $\mathbb{L}/\mathbb{K}$ and a $p$-radical element $x\in \mathbb{L}$ of height $e$. Then for $a=x^{p^e}\in \mathbb{K}$, the minimal polynomial of $x$ is given by

$$\x^{p^e}-a\in \mathbb{K}[\x].$$

Hence $[\mathbb{K}(x):\mathbb{K}]=p^e$.
:::

We agreed to write the image of the Frobenius endomorphism $\Frob_p:\mathbb{K}\rightarrow \mathbb{K}$ as $\mathbb{K}^p$. Then the above claim follows from the next lemma.

::: Lemma 3
Assume that an element $a$ of a field $\mathbb{K}$ satisfies $a\not\in \mathbb{K}^p$. Then for any $e\geq 0$, the polynomial $f(\x)=\x^{p^e}-a$ is irreducible in $\mathbb{K}[\x]$.
:::
::: Proof
If $p=1$, then $\mathbb{K}^p=\mathbb{K}$, so no $a$ satisfying the assumption exists. Thus it suffices to consider the case where $p$ is prime. Also, if $e=0$, then $f$ is linear and trivially irreducible, so it suffices to consider $e\geq 1$.

Choose a root $\alpha$ of $f$ in $\overline{\mathbb{K}}$, so that $\alpha^{p^e}=a$. Then applying the Frobenius endomorphism of [§Fields, ⁋Theorem 10](/en/math/field_theory/fields#thm10) repeatedly to the characteristic $p$ ring $\overline{\mathbb{K}}[\x]$ yields

$$f(\x)=\x^{p^e}-\alpha^{p^e}=(\x-\alpha)^{p^e}.$$

On the other hand, if $\alpha^{p^m}\in \mathbb{K}$ for some $m<e$, then $a=(\alpha^{p^m})^{p^{e-m}}\in \mathbb{K}^p$, contradicting the assumption; therefore any $m$ with $\alpha^{p^m}\in\mathbb{K}$ must satisfy $m\geq e$.

Now let $g\in \mathbb{K}[\x]$ be a monic factor of $f$ of degree at least one. Then in $\overline{\mathbb{K}}[\x]$, $g$ is a monic factor of $(\x-\alpha)^{p^e}$, so it must be of the form $g=(\x-\alpha)^d$ for some $0< d\leq p^e$. Write $d=p^cu$, where $u$ is a positive integer coprime to $p$. Then again by [§Fields, ⁋Theorem 10](/en/math/field_theory/fields#thm10),

$$g=\bigl((\x-\alpha)^{p^c}\bigr)^u=(\x^{p^c}-\alpha^{p^c})^u,$$

and expanding this, the coefficient of $\x^{p^c(u-1)}$ is $-u\alpha^{p^c}$. Since $g\in\mathbb{K}[\x]$, we have $-u\alpha^{p^c}\in \mathbb{K}$; but $p$ does not divide $u$, so $u\cdot 1$ is invertible in $\mathbb{K}$, and hence $\alpha^{p^c}\in \mathbb{K}$. Then by the preceding paragraph we must have $c\geq e$, and therefore $d\geq p^c\geq p^e$, so $d=p^e$, i.e. $g=f$. Thus $f$ has no monic factor of degree at least one other than itself, which means $f$ is irreducible.
:::

Assuming this, the proof of [Proposition 2](#prop2) is also easily obtained.

::: Proof (Proposition 2)
If $e=0$, then $x=a\in \mathbb{K}$, so the minimal polynomial of $x$ is $\x-a$, i.e. $\x^{p^0}-a$, and $[\mathbb{K}(x):\mathbb{K}]=1=p^0$.

Now suppose $e\geq 1$, and assume that $a=b^p$ for some $b\in\mathbb{K}$. Then $(x^{p^{e-1}})^p=x^{p^e}=a=b^p$, but since the Frobenius endomorphism is always injective in a field, we get $x^{p^{e-1}}=b\in \mathbb{K}$, contradicting the minimality of $e$. Hence $a\not\in \mathbb{K}^p$, and by [Lemma 3](#lem3), $\x^{p^e}-a$ is irreducible. This is a monic polynomial having $x$ as a root, so it is the minimal polynomial of $x$, and since its degree is $p^e$, we have $[\mathbb{K}(x):\mathbb{K}]=p^e$.
:::

The following definition would have been natural even immediately after [Definition 1](#def1).

::: Definition 4
A field extension $\mathbb{L}/\mathbb{K}$ is called *$p$-radical* if every element of $\mathbb{L}$ is $p$-radical. If there exists an integer $e$ such that $x^{p^e}\in \mathbb{K}$ holds for <em>every</em> element $x\in \mathbb{L}$, then the smallest such $e$ is called the *height* of $\mathbb{L}$.
:::

Thus the height of $\mathbb{L}/\mathbb{K}$, if defined, can be thought of as the maximum of the heights of the elements of $\mathbb{L}$. Also, by [Proposition 2](#prop2), any $p$-radical extension is naturally an algebraic extension.

If the Frobenius endomorphism $\Frob_p:A\rightarrow A$ is a bijection, we called $A$ a *perfect ring*. ([§Fields, ⁋Definition 13](/en/math/field_theory/fields#def13)) Therefore, if $\mathbb{K}$ were a perfect field, then $\mathbb{K}^p=\mathbb{K}$, so any $p$-radical extension of a perfect field must be the field itself. Moreover, it is obvious from the definition that the compositum of $p$-radical extensions is $p$-radical. The following proposition concerns the existence of a (relative) $p$-radical closure.

::: Proposition 5
Fix a field extension $\mathbb{L}/\mathbb{K}$, and for each $n\geq 0$ define

$$\mathbb{L}_n=\{x\in \mathbb{L}\mid\text{$x$ is $p$-radical of height $\leq n$}\}.$$

Then the union $\mathbb{L}_\infty$ of the increasing sequence $\mathbb{L}_n$ is the largest $p$-radical subextension of $\mathbb{L}$ containing $\mathbb{K}$.
:::

::: Proof
That $\mathbb{L}_n\subseteq \mathbb{L}_{n+1}$ is obvious from the definition. Let us show that $\mathbb{L}_\infty$ is a subfield. If $x,y\in \mathbb{L}_\infty$, then we can choose $N$ so that $x^{p^N},y^{p^N}\in \mathbb{K}$, and from the Frobenius endomorphism of [§Fields, ⁋Theorem 10](/en/math/field_theory/fields#thm10),

$$(x\pm y)^{p^N}=x^{p^N}\pm y^{p^N}\in \mathbb{K},\qquad (xy)^{p^N}=x^{p^N}y^{p^N}\in\mathbb{K},$$

and if $x\neq 0$, then $(x^{-1})^{p^N}=(x^{p^N})^{-1}\in \mathbb{K}$. Thus $\mathbb{L}_\infty$ is a subfield of $\mathbb{L}$ containing $\mathbb{K}=\mathbb{L}_0$, and since every element of it is $p$-radical, $\mathbb{L}_\infty/\mathbb{K}$ is a $p$-radical extension. Finally, if $\mathbb{M}/\mathbb{K}$ is any $p$-radical subextension of $\mathbb{L}$, then any element $x\in \mathbb{M}$ has finite height $n$, so $x\in \mathbb{L}_n\subseteq\mathbb{L}_\infty$. That is, $\mathbb{L}_\infty$ is the largest.
:::

In [§Algebraic Closures](/en/math/field_theory/algebraically_closed_extensions) we saw that every field $\mathbb{K}$ has an algebraic closure $\overline{\mathbb{K}}$. Hence in [Proposition 5](#prop5) we may take $\mathbb{L}=\overline{\mathbb{K}}$. Then $\overline{\mathbb{K}}$ is a perfect field, and moreover we know that for each $n$, $\overline{\mathbb{K}}_n$ is exactly $\mathbb{K}^{1/p^n}$. Let us write the (relative) $p$-radical closure in this situation as $\mathbb{K}^{1/p^\infty}$. This is the same thing as the perfect closure of $\mathbb{K}$ defined in [§Fields, ⁋Definition 14](/en/math/field_theory/fields#def14) and whose existence was shown in [§Fields, ⁋Theorem 15](/en/math/field_theory/fields#thm15). If $\mathbb{K}$ is imperfect, i.e. $\mathbb{K}\neq \mathbb{K}^p$, then the above ascending sequence is strictly increasing, and therefore $\mathbb{K}^{1/p^\infty}/\mathbb{K}$ becomes an extension of infinite degree.

On the other hand, the following holds.

::: Proposition 6
Let $\mathbb{L}/\mathbb{K}$ be a $p$-radical extension, and suppose a homomorphism $u$ from $\mathbb{K}$ to some perfect field $\mathbb{F}$ is given. Then there exists a unique homomorphism $v:\mathbb{L} \rightarrow \mathbb{F}$ extending $u$.
:::
::: Proof
Since $\mathbb{F}$ is perfect, the Frobenius endomorphism $\Frob_p:\mathbb{F} \rightarrow \mathbb{F}$ is bijective, and therefore for any $b\in \mathbb{F}$ and $m\geq 0$ there exists a unique $\xi\in \mathbb{F}$ satisfying $\xi^{p^m}=b$.

Now let $x\in \mathbb{L}$ be a $p$-radical element of height $m$; then $x^{p^m}\in \mathbb{K}$, and define $v(x)$ to be the unique $\xi\in\mathbb{F}$ satisfying $\xi^{p^m}=u(x^{p^m})$. This definition does not depend on the choice of $m$. Indeed, for $n\geq m$ we also have $x^{p^n}\in \mathbb{K}$, and the $\xi$ defined above satisfies

$$\xi^{p^n}=(\xi^{p^m})^{p^{n-m}}=u(x^{p^m})^{p^{n-m}}=u\bigl((x^{p^m})^{p^{n-m}}\bigr)=u(x^{p^n}),$$

so it coincides with the element defined using $n$.

Let us show that $v$ is a homomorphism. If the heights of $x,y\in \mathbb{L}$ are both at most $N$, then

$$\bigl(v(x)+v(y)\bigr)^{p^N}=v(x)^{p^N}+v(y)^{p^N}=u(x^{p^N})+u(y^{p^N})=u\bigl((x+y)^{p^N}\bigr)=v(x+y)^{p^N},$$

and since Frobenius is injective in $\mathbb{F}$, we have $v(x+y)=v(x)+v(y)$. The same argument works for multiplication. Also, for elements of height $0$, i.e. elements of $\mathbb{K}$, we have $v=u$, so $v$ extends $u$; in particular $v(1)=u(1)$.

Finally, let us show uniqueness. If $w:\mathbb{L} \rightarrow \mathbb{F}$ is a homomorphism extending $u$, then for any $x\in \mathbb{L}$ of height $m$,

$$w(x)^{p^m}=w(x^{p^m})=u(x^{p^m}),$$

so by the uniqueness of $p^m$-th roots in $\mathbb{F}$, we have $w(x)=v(x)$.
:::

Hence the following holds.

::: Corollary 7
A field extension $\mathbb{L}/\mathbb{K}$ is the perfect closure of $\mathbb{K}$ if and only if $\mathbb{L}$ is a $p$-radical extension of $\mathbb{K}$ and $\mathbb{L}$ is a perfect field.
:::
::: Proof
Since the perfect closure is defined by a universal property and is uniquely determined up to $\mathbb{K}$-isomorphism, it suffices to verify the necessity for $\mathbb{K}^{1/p^\infty}$. By construction, every element of $\mathbb{K}^{1/p^\infty}$ has finite height, so $\mathbb{K}^{1/p^\infty}/\mathbb{K}$ is a $p$-radical extension. Also, if $x\in \mathbb{K}^{1/p^\infty}$, then since $\overline{\mathbb{K}}$ is algebraically closed there exists $y\in \overline{\mathbb{K}}$ with $y^p=x$; if $x^{p^n}\in \mathbb{K}$, then $y^{p^{n+1}}=x^{p^n}\in \mathbb{K}$, so $y\in \mathbb{K}^{1/p^\infty}$. That is, Frobenius is surjective on $\mathbb{K}^{1/p^\infty}$, and since Frobenius is always injective in a field, $\mathbb{K}^{1/p^\infty}$ is perfect.

Conversely, suppose $\mathbb{L}/\mathbb{K}$ is $p$-radical and $\mathbb{L}$ is perfect. Applying [Proposition 6](#prop6) to the inclusion $u:\mathbb{K}\hookrightarrow \mathbb{K}^{1/p^\infty}$ yields a $\mathbb{K}$-homomorphism $v:\mathbb{L} \rightarrow \mathbb{K}^{1/p^\infty}$. First, $v(\mathbb{L})$ is a perfect field: given $v(x)\in v(\mathbb{L})$, the fact that $\mathbb{L}$ is perfect yields $z\in \mathbb{L}$ with $x=z^p$, and then $v(x)=v(z)^p$. On the other hand, any element $t\in \mathbb{K}^{1/p^\infty}$ satisfies $t^{p^n}\in \mathbb{K}\subseteq v(\mathbb{L})$ for some $n$, and since $v(\mathbb{L})$ is perfect there exists $\xi\in v(\mathbb{L})$ with $\xi^{p^n}=t^{p^n}$. But Frobenius is injective in a field, so $t=\xi\in v(\mathbb{L})$. That is, $v$ is surjective, and since a nonzero homomorphism between fields is injective ([§Fields, ⁋Proposition 2](/en/math/field_theory/fields#prop2)), $v$ is a $\mathbb{K}$-isomorphism. Therefore $\mathbb{L}$ is the perfect closure of $\mathbb{K}$.
:::

From this, the uniqueness of the perfect closure also follows.

::: Proposition 8
Let $\mathbb{M}_1$, $\mathbb{M}_2$ be two perfect closures of a field $\mathbb{K}$, i.e. two fields that are perfect and $p$-radical extensions of $\mathbb{K}$. Then there exists a unique $\mathbb{K}$-isomorphism $\mathbb{M}_1 \rightarrow \mathbb{M}_2$.
:::
::: Proof
Applying [Proposition 6](#prop6) to the inclusion $\mathbb{K}\hookrightarrow \mathbb{M}_2$ yields a unique $\mathbb{K}$-homomorphism $v:\mathbb{M}_1 \rightarrow \mathbb{M}_2$, and interchanging the roles of $\mathbb{M}_1$ and $\mathbb{M}_2$ yields a unique $\mathbb{K}$-homomorphism $w:\mathbb{M}_2 \rightarrow \mathbb{M}_1$. Then the composition $w\circ v:\mathbb{M}_1 \rightarrow \mathbb{M}_1$ is a homomorphism extending the inclusion $\mathbb{K}\hookrightarrow\mathbb{M}_1$, and since $\id_{\mathbb{M}_1}$ also does so, the uniqueness in [Proposition 6](#prop6) gives $w\circ v=\id_{\mathbb{M}_1}$. For the same reason $v\circ w=\id_{\mathbb{M}_2}$, so $v$ is an isomorphism, and its uniqueness was already observed.
:::

We close this post by presenting the counterexample mentioned in the introduction.

::: Example 9
Consider the field $\mathbb{K}=\mathbb{F}_p(t)$. Since the elements of $\mathbb{F}_p$ are fixed by the Frobenius endomorphism, we have $\mathbb{K}^p=\mathbb{F}_p(t^p)$, and hence $t\not\in \mathbb{K}^p$. Then the polynomial $f(\x)=\x^p-t\in \mathbb{K}[\x]$ is irreducible by [Lemma 3](#lem3), so $\mathbb{L}=\mathbb{K}[\x]/(\x^p-t)$ is an extension of $\mathbb{K}$. If we let $\alpha$ be the residue class of $\x$, then $\alpha^p=t\in\mathbb{K}$ and $\alpha\not\in \mathbb{K}$, so $\alpha$ is a $p$-radical element of height $1$, and therefore $\mathbb{L}/\mathbb{K}$ is a $p$-radical extension and the minimal polynomial of $\alpha$ is $f(\x)$. ([Proposition 2](#prop2)) Differentiating this gives $Df=p\x^{p-1}=0$, so by [\[Ring Theory\] §Polynomial Rings, ⁋Proposition 11](/en/math/ring_theory/polynomial_rings#prop11) we know that $\alpha$ is a multiple root of $f$. In fact, by [§Fields, ⁋Theorem 10](/en/math/field_theory/fields#thm10) we have $(\x-\alpha)^p=\x^p-\alpha^p=\x^p-t$, so $\alpha$ has multiplicity $p$.
:::

In the next post and the one after that, we will see how such cases are excluded from the discussion.

---

**References**

**[Bou]** N. Bourbaki. *Algebra II: Chapters 4–7*. Springer, 2003.
