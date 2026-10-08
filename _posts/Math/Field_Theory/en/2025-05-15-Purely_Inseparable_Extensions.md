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
last_polished_at: 2026-10-08T11:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
Let us examine the overarching theme of Galois theory that we will explore through a very simple example. For instance, considering the degree $4$ extension $\mathbb{Q}(\sqrt{2}, \sqrt{3})$ of $\mathbb{Q}$, the elements $\sqrt{2}$ and $\sqrt{3}$ newly added from $\mathbb{Q}$ arise, respectively, from the minimal polynomials with rational coefficients

$$\x^2-2,\qquad \x^2-3$$

However, looking at each of these two polynomials, they are polynomials having two roots $\pm \sqrt{2}$ and $\pm\sqrt{3}$, respectively, and there is no algebraic way to distinguish them within $\mathbb{Q}$. Therefore, if we consider the action of permuting these roots (or the $\mathbb{Q}$-automorphisms of $\mathbb{Q}(\sqrt{2},\sqrt{3})$), that is, if we consider the permutation group $S_2\times S_2$, this is a subgroup of $S_4$.

In this manner, whenever a polynomial is given, we can define an appropriate Galois group, and the philosophy of Galois theory is that studying them allows us to classify extensions of $\mathbb{Q}$.

However, thinking on the basis of this philosophy, if, for instance, a minimal polynomial has a repeated root, defining a permutation action would become quite awkward. While this is an unfounded worry over $\mathbb{Q}$, in certain cases such a thing can actually happen.

::: remark {#rmk}
Every field appearing in this post has characteristic exponent $p$.
:::

## Purely Inseparable Extensions

::: Definition 1
For a field extension $\mathbb{L}/\mathbb{K}$, an element $x\in \mathbb{L}$ is called *$p$-radical* if there exists some $m\geq 0$ such that $x^{p^m}\in \mathbb{K}$. The smallest such $m$ is called the *height* of $x$.
:::

If $p=1$, the above definition is of little significance, and the same holds for the rest of the content in this post. That is, essentially all the content of this post can be regarded as being about fields of characteristic $p$.

::: Proposition 2
Fix a field extension $\mathbb{L}/\mathbb{K}$ and a $p$-radical element $x\in \mathbb{L}$ of height $e$. Then for $a=x^{p^e}\in \mathbb{K}$, the minimal polynomial of $x$ is given by

$$\x^{p^e}-a\in \mathbb{K}[\x]$$

Hence $[\mathbb{K}(x):\mathbb{K}]=p^e$.
:::

We agreed to denote the image of the Frobenius endomorphism $\Frob_p:\mathbb{K}\rightarrow \mathbb{K}$ by $\mathbb{K}^p$. Then the above claim follows from the following lemma.

::: Lemma 3
Assume that in a field $\mathbb{K}$, an element $a$ satisfies $a\not\in \mathbb{K}^p$. Then for any $e\geq 0$, $f(\x)=\x^{p^e}-a$ is an irreducible polynomial in $\mathbb{K}[\x]$.
:::
::: Proof
If $p=1$, then $\mathbb{K}^p=\mathbb{K}$, so no $a$ satisfying the assumption exists. Thus it suffices to consider only the case where $p$ is prime. Also, if $e=0$, then $f$ is linear and trivially irreducible, so it suffices to consider only the case $e\geq 1$.

In $\overline{\mathbb{K}}$, choose a root of $f$, say $\alpha$; that is, $\alpha^{p^e}=a$. Then applying the Frobenius endomorphism of [§Fields, ⁋Theorem 10](/en/math/field_theory/fields#thm10){: data-lid="f5lhw" } repeatedly to the characteristic $p$ ring $\overline{\mathbb{K}}[\x]$,

$$f(\x)=\x^{p^e}-\alpha^{p^e}=(\x-\alpha)^{p^e}$$

holds. On the other hand, if for some $m<e$ we have $\alpha^{p^m}\in \mathbb{K}$, then $a=(\alpha^{p^m})^{p^{e-m}}\in \mathbb{K}^p$, contradicting the assumption; thus for $\alpha^{p^m}\in\mathbb{K}$ to hold, $m$ must satisfy $m\geq e$.

Now let $g\in \mathbb{K}[\x]$ be a monic factor of $f$ of degree at least one. Then in $\overline{\mathbb{K}}[\x]$, $g$ is a monic factor of $(\x-\alpha)^{p^e}$, so for some $0< d\leq p^e$, it must be of the form $g=(\x-\alpha)^d$. Write $d=p^cu$, where $u$ is a positive integer coprime to $p$. Then again by [§Fields, ⁋Theorem 10](/en/math/field_theory/fields#thm10){: data-lid="zk46j" },

$$g=\bigl((\x-\alpha)^{p^c}\bigr)^u=(\x^{p^c}-\alpha^{p^c})^u$$

and expanding this, the coefficient of $\x^{p^c(u-1)}$ is $-u\alpha^{p^c}$. Since $g\in\mathbb{K}[\x]$, we have $-u\alpha^{p^c}\in \mathbb{K}$; but $p$ does not divide $u$, so $u\cdot 1$ is invertible in $\mathbb{K}$, and hence $\alpha^{p^c}\in \mathbb{K}$. Then by what was seen in the preceding paragraph, we must have $c\geq e$, and therefore $d\geq p^c\geq p^e$, so $d=p^e$, i.e. $g=f$. Therefore $f$ has only itself as a monic factor of degree at least one, which means that $f$ is irreducible.
:::

Assuming this, the proof of [Proposition 2](#prop2){: data-lid="1g6k7" } is also easily obtained.

::: Proof (Proposition 2)
If $e=0$, then $x=a\in \mathbb{K}$, so the minimal polynomial of $x$ is $\x-a$, i.e. $\x^{p^0}-a$, and $[\mathbb{K}(x):\mathbb{K}]=1=p^0$.

Now suppose $e\geq 1$, and assume that for some $b\in\mathbb{K}$, $a=b^p$. Then $(x^{p^{e-1}})^p=x^{p^e}=a=b^p$, but since the Frobenius endomorphism in a field is always injective, we have $x^{p^{e-1}}=b\in \mathbb{K}$, contradicting the minimality of $e$. Therefore $a\not\in \mathbb{K}^p$, and by [Lemma 3](#lem3){: data-lid="5mf0e" }, $\x^{p^e}-a$ is irreducible. Since this is a monic polynomial having $x$ as a root, it is the minimal polynomial of $x$, and since its degree is $p^e$, we have $[\mathbb{K}(x):\mathbb{K}]=p^e$.
:::

The following definition would have been natural even immediately after [Definition 1](#def1){: data-lid="famqy" }.

::: Definition 4
A field extension $\mathbb{L}/\mathbb{K}$ is called *$p$-radical* if every element of $\mathbb{L}$ is $p$-radical. If for $\mathbb{L}$, <em>every</em> element $x$ satisfies $x^{p^e}\in \mathbb{K}$ for some integer $e$, then the smallest such $e$ satisfying this property is called the *height* of $\mathbb{L}$.
:::

That is, the height of $\mathbb{L}/\mathbb{K}$ (if defined) can be thought of as the maximum of the heights of the elements of $\mathbb{L}$. Also, by [Proposition 2](#prop2){: data-lid="t3j9i" }, any $p$-radical extension is naturally an algebraic extension.

If the Frobenius endomorphism $\Frob_p:A\rightarrow A$ is a bijection, we called $A$ a *perfect ring*. ([§Fields, ⁋Definition 13](/en/math/field_theory/fields#def13){: data-lid="lqsbi" }) Therefore, if $\mathbb{K}$ is a perfect field, then $\mathbb{K}^p=\mathbb{K}$, so any $p$-radical extension of a perfect field must be itself. Furthermore, it is obvious from the definition that the compositum of $p$-radical extensions is $p$-radical. The following proposition concerns the existence of a (relative) $p$-radical closure.

::: Proposition 5
Fix a field extension $\mathbb{L}/\mathbb{K}$, and for each $n\geq 0$ define

$$\mathbb{L}_n=\{x\in \mathbb{L}\mid\text{$x$ is $p$-radical of height $\leq n$}\}$$

Then the union of the increasing sequence $\mathbb{L}_n$, $\mathbb{L}_\infty$, is, among the subextensions containing $\mathbb{K}$ in $\mathbb{L}$, the largest $p$-radical subextension.
:::

::: Proof
That $\mathbb{L}_n\subseteq \mathbb{L}_{n+1}$ is obvious from the definition. Let us show that $\mathbb{L}_\infty$ is a subfield. If $x,y\in \mathbb{L}_\infty$, then we can choose $N$ so that $x^{p^N},y^{p^N}\in \mathbb{K}$, and from the Frobenius endomorphism of [§Fields, ⁋Theorem 10](/en/math/field_theory/fields#thm10){: data-lid="d03w8" },

$$(x\pm y)^{p^N}=x^{p^N}\pm y^{p^N}\in \mathbb{K},\qquad (xy)^{p^N}=x^{p^N}y^{p^N}\in\mathbb{K}$$

and if $x\neq 0$, then $(x^{-1})^{p^N}=(x^{p^N})^{-1}\in \mathbb{K}$. Thus $\mathbb{L}_\infty$ contains $\mathbb{K}=\mathbb{L}_0$ and is a subfield of $\mathbb{L}$, and since every element of it is $p$-radical, $\mathbb{L}_\infty/\mathbb{K}$ is a $p$-radical extension. Finally, if $\mathbb{M}/\mathbb{K}$ is any subextension of $\mathbb{L}$ that is $p$-radical, then any element of $\mathbb{M}$, say $x$, has finite height $n$, so $x\in \mathbb{L}_n\subseteq\mathbb{L}_\infty$. That is, $\mathbb{L}_\infty$ is the largest.
:::

In [§Algebraic Closure](/en/math/field_theory/algebraically_closed_extensions){: data-lid="hnzgf" } we saw that every field $\mathbb{K}$ has an algebraic closure $\overline{\mathbb{K}}$. Hence in [Proposition 5](#prop5){: data-lid="hx9dy" } we may take $\mathbb{L}=\overline{\mathbb{K}}$. Then $\overline{\mathbb{K}}$ is a perfect field, and moreover we know that for each $n$, $\overline{\mathbb{K}}_n$ is exactly $\mathbb{K}^{1/p^n}$. Let us write the (relative) $p$-radical closure in this situation as $\mathbb{K}^{1/p^\infty}$. This is the same thing as the perfect closure of $\mathbb{K}$ defined in [§Fields, ⁋Definition 14](/en/math/field_theory/fields#def14){: data-lid="0yhn5" } and whose existence was shown in [§Fields, ⁋Theorem 15](/en/math/field_theory/fields#thm15){: data-lid="z95z3" }. If $\mathbb{K}$ is imperfect, that is, $\mathbb{K}\neq \mathbb{K}^p$, then the above ascending sequence is strictly increasing, and therefore $\mathbb{K}^{1/p^\infty}/\mathbb{K}$ becomes an extension of infinite degree.

On the other hand, the following holds.

::: Proposition 6
Let a field extension $\mathbb{L}/\mathbb{K}$ be a $p$-radical extension, and suppose that from $\mathbb{K}$ to some perfect field $\mathbb{F}$ a homomorphism $u$ is given. Then, extending $u$, there exists a unique homomorphism $v:\mathbb{L} \rightarrow \mathbb{F}$.
:::
::: Proof
Since $\mathbb{F}$ is perfect, the Frobenius endomorphism $\Frob_p:\mathbb{F} \rightarrow \mathbb{F}$ is bijective, and therefore for any $b\in \mathbb{F}$ and $m\geq 0$, there exists, satisfying $\xi^{p^m}=b$, a unique $\xi\in \mathbb{F}$.

Now if $x\in \mathbb{L}$ is a height-$m$ $p$-radical element, then $x^{p^m}\in \mathbb{K}$, and let us define $v(x)$, satisfying $\xi^{p^m}=u(x^{p^m})$, to be the unique $\xi\in\mathbb{F}$. This definition does not depend on the choice of $m$. Indeed, for $n\geq m$ we also have $x^{p^n}\in \mathbb{K}$, and since the $\xi$ defined above satisfies

$$\xi^{p^n}=(\xi^{p^m})^{p^{n-m}}=u(x^{p^m})^{p^{n-m}}=u\bigl((x^{p^m})^{p^{n-m}}\bigr)=u(x^{p^n})$$

it coincides with the element defined using $n$.

Let us show that $v$ is a homomorphism. If the heights of $x,y\in \mathbb{L}$ are both at most $N$, then

$$\bigl(v(x)+v(y)\bigr)^{p^N}=v(x)^{p^N}+v(y)^{p^N}=u(x^{p^N})+u(y^{p^N})=u\bigl((x+y)^{p^N}\bigr)=v(x+y)^{p^N}$$

and since Frobenius is injective on $\mathbb{F}$, we have $v(x+y)=v(x)+v(y)$. The same argument holds for multiplication. Also, for elements of height $0$, i.e., elements of $\mathbb{K}$, we have $v=u$, so $v$ extends $u$; in particular, $v(1)=u(1)$.

Finally, let us show uniqueness. If $w:\mathbb{L} \rightarrow \mathbb{F}$ is a homomorphism extending $u$, then for any height-$m$ $x\in \mathbb{L}$,

$$w(x)^{p^m}=w(x^{p^m})=u(x^{p^m})$$

so by the uniqueness in $\mathbb{F}$ of $p^m$-th roots, we have $w(x)=v(x)$.
:::

Hence the following holds. 

::: Corollary 7
A field extension $\mathbb{L}/\mathbb{K}$ is the perfect closure of $\mathbb{K}$ if and only if $\mathbb{L}$ is an extension of $\mathbb{K}$ that is $p$-radical and $\mathbb{L}$ is a perfect field.
:::
::: Proof
Since the perfect closure is defined by a universal property and is uniquely determined up to $\mathbb{K}$-isomorphism, it suffices to verify the necessity for $\mathbb{K}^{1/p^\infty}$. By construction, every element of $\mathbb{K}^{1/p^\infty}$ has finite height, so $\mathbb{K}^{1/p^\infty}/\mathbb{K}$ is a $p$-radical extension. Also, if $x\in \mathbb{K}^{1/p^\infty}$, then since $\overline{\mathbb{K}}$ is algebraically closed, there exists, satisfying $y^p=x$, an element $y\in \overline{\mathbb{K}}$; if $x^{p^n}\in \mathbb{K}$, then $y^{p^{n+1}}=x^{p^n}\in \mathbb{K}$, so $y\in \mathbb{K}^{1/p^\infty}$. That is, Frobenius is surjective on $\mathbb{K}^{1/p^\infty}$, and since Frobenius is always injective in a field, $\mathbb{K}^{1/p^\infty}$ is perfect.

Conversely, suppose $\mathbb{L}/\mathbb{K}$ is $p$-radical and $\mathbb{L}$ is perfect. Applying [Proposition 6](#prop6){: data-lid="eewk9" } to the inclusion $u:\mathbb{K}\hookrightarrow \mathbb{K}^{1/p^\infty}$ yields a $\mathbb{K}$-homomorphism $v:\mathbb{L} \rightarrow \mathbb{K}^{1/p^\infty}$. First, $v(\mathbb{L})$ is a perfect field: whenever $v(x)\in v(\mathbb{L})$ is given, from the fact that $\mathbb{L}$ is perfect there exists, satisfying $x=z^p$, an element $z\in \mathbb{L}$, and $v(x)=v(z)^p$. On the other hand, any element of $\mathbb{K}^{1/p^\infty}$, say $t$, satisfies for some $n$ the relation $t^{p^n}\in \mathbb{K}\subseteq v(\mathbb{L})$, and since $v(\mathbb{L})$ is perfect, there exists, satisfying $\xi^{p^n}=t^{p^n}$, an element $\xi\in v(\mathbb{L})$. But since Frobenius is injective in a field, $t=\xi\in v(\mathbb{L})$. That is, $v$ is surjective, and since a nonzero homomorphism between fields is injective ([§Fields, ⁋Proposition 2](/en/math/field_theory/fields#prop2){: data-lid="f6ale" }), $v$ is a $\mathbb{K}$-isomorphism. Therefore $\mathbb{L}$ is the perfect closure of $\mathbb{K}$.
:::

From this we also obtain the uniqueness of the perfect closure.

::: Proposition 8
For a field $\mathbb{K}$, suppose two perfect closures $\mathbb{M}_1$, $\mathbb{M}_2$ (that is, two fields that are perfect and, over $\mathbb{K}$, $p$-radical extensions) are given. Then there exists a unique $\mathbb{K}$-isomorphism $\mathbb{M}_1 \rightarrow \mathbb{M}_2$.
:::
::: Proof
Applying [Proposition 6](#prop6){: data-lid="khs2y" } to the inclusion $\mathbb{K}\hookrightarrow \mathbb{M}_2$ yields a unique $\mathbb{K}$-homomorphism $v:\mathbb{M}_1 \rightarrow \mathbb{M}_2$, and interchanging the roles of $\mathbb{M}_1$ and $\mathbb{M}_2$ also yields a unique $\mathbb{K}$-homomorphism $w:\mathbb{M}_2 \rightarrow \mathbb{M}_1$. Then the composition $w\circ v:\mathbb{M}_1 \rightarrow \mathbb{M}_1$ is a homomorphism extending the inclusion $\mathbb{K}\hookrightarrow\mathbb{M}_1$, and since $\id_{\mathbb{M}_1}$ also does so, again by the uniqueness in [Proposition 6](#prop6){: data-lid="u2sar" }, we have $w\circ v=\id_{\mathbb{M}_1}$. For the same reason, $v\circ w=\id_{\mathbb{M}_2}$, so $v$ is an isomorphism, and its uniqueness has already been observed.
:::

We close this post by presenting the counterexample mentioned in the introduction.

::: Example 9
Consider the field $\mathbb{K}=\mathbb{F}_p(t)$. Since the elements of $\mathbb{F}_p$ are fixed by the Frobenius endomorphism, we have $\mathbb{K}^p=\mathbb{F}_p(t^p)$, and hence $t\not\in \mathbb{K}^p$. Then the polynomial $f(\x)=\x^p-t\in \mathbb{K}[\x]$ is irreducible by [Lemma 3](#lem3){: data-lid="im3it" }, so $\mathbb{L}=\mathbb{K}[\x]/(\x^p-t)$ is an extension of $\mathbb{K}$. If we let the residue class of $\x$ be $\alpha$, then $\alpha^p=t\in\mathbb{K}$ and $\alpha\not\in \mathbb{K}$, so $\alpha$ is a height $1$ $p$-radical element, and therefore $\mathbb{L}/\mathbb{K}$ is a $p$-radical extension and the minimal polynomial of $\alpha$ is $f(\x)$. ([Proposition 2](#prop2){: data-lid="b7e39" }) Differentiating this gives $Df=p\x^{p-1}=0$, so by [\[Ring Theory\] §Polynomial Rings, ⁋Proposition 11](/en/math/ring_theory/polynomial_rings#prop11){: data-lid="itccv" } we know that $\alpha$ is a multiple root of $f$. In fact, by [§Fields, ⁋Theorem 10](/en/math/field_theory/fields#thm10){: data-lid="qa1rv" } we have $(\x-\alpha)^p=\x^p-\alpha^p=\x^p-t$, so $\alpha$ has multiplicity $p$.
:::

Now, in the next post and the one after that, we will see how such cases are excluded from the discussion.

---

**References**

**[Bou]** N. Bourbaki. *Algebra II: Chapters 4–7*. Springer, 2003.
