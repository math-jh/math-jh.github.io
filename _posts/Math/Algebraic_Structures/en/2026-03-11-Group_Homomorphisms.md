---
title: "Group Homomorphisms"
description: "This post covers the definitions of group homomorphisms and isomorphisms, and shows that a magma homomorphism is an isomorphism if and only if it is bijective. It also examines the property that the equalizer of homomorphisms forms a subgroup."
excerpt: "Definitions and properties of group homomorphisms, their kernels and images"

categories: [Math / Algebraic Structures]
permalink: /en/math/algebraic_structures/group_homomorphisms
sidebar: 
    nav: "algebraic_structures-en"
    
date: 2021-09-08
weight: 4
translated_at: 2026-08-16T09:45:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-09-04T23:15:05+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
For now, we investigate the properties of groups. Therefore, a group homomorphism between groups will simply be called a homomorphism.

From [§Algebraic Structures, ⁋Definition 6](/en/math/algebraic_structures/algebraic_structures#def6), a (group) isomorphism can also be defined, and from this definition and [[Set Theory] §Operations Between Functions, ⁋Proposition 5](/en/math/set_theory/operation_of_functions#prop5), it is obvious that any isomorphism must be a bijection. In many cases, the converse also holds.

::: Proposition 1
A magma homomorphism $f:A\rightarrow A'$ is an isomorphism if and only if $f$ is bijective. 

If $A$ has an identity element $e$ and $f:A\rightarrow A'$ is a bijective homomorphism, then $f(e)$ is the identity element of $A'$, and thus $f^{-1}$ is a magma homomorphism sending the identity element of $A'$ to the identity element of $A$.
:::

::: Proof
It suffices to show the converse direction. Since $f$ is bijective, the inverse function $f^{-1}:A'\rightarrow A$ exists as a function. If $f^{-1}$ is a homomorphism, then by definition $f$ will be an isomorphism.

Choose arbitrary $y, y'\in  A'$. Then since $f$ is bijective, there exist unique $x$, $x'$ such that $f(x)=y$ and $f(x')=y'$. Now

$$f^{-1}(yy')=f^{-1}(f(x)f(x'))=f^{-1}(f(xx'))=xx'=f^{-1}(y)f^{-1}(y')$$

so $f^{-1}$ is a homomorphism, and therefore $f$ is an isomorphism. 

On the other hand, if $f:A\rightarrow A'$ is a bijection, then for any $y\in A'$, $f(x)=y$ holds for a unique $x\in A$. Now

$$y=f(x)=f(xe)=f(x)f(e),\qquad y=f(x)=f(ex)=f(e)f(x)$$

so $f(e)$ is the identity element of $A'$.
:::

## Equalizer of Homomorphisms

The following holds.

::: Proposition 2
Let group homomorphisms $f,g:G \rightarrow H$ be given. Then

$$\Eq(f,g)=\{x\in G\mid f(x)=g(x)\}$$

is a subgroup of $G$.
:::
::: Proof
If $x,y\in \Eq(f,g)$, then by the argument immediately following [§Semigroups, Monoids, and Groups, ⁋Definition 11](/en/math/algebraic_structures/groups#def11), a monoid homomorphism between groups preserves inverses, so

$$f(xy^{-1})=f(x)f(y)^{-1}=g(x)g(y)^{-1}=g(xy^{-1})$$

and thus $xy^{-1}\in\Eq(f,g)$. Also, after [§Semigroups, Monoids, and Groups, ⁋Definition 11](/en/math/algebraic_structures/groups#def11) we observed that a monoid homomorphism between groups preserves the identity element, and since the identity element of $H$ is unique, $\Eq(f,g)$ is nonempty. Therefore, by [§Semigroups, Monoids, and Groups, ⁋Proposition 15](/en/math/algebraic_structures/groups#prop15), we obtain the desired result. 
:::

For $\Eq(f,g)$ defined in this way, the inclusion $i:\Eq(f,g)\rightarrow G$ has the following property.

> If a group homomorphism $j:G' \rightarrow G$ satisfies $f\circ j=g\circ j$, then there exists a unique homomorphism $j': G' \rightarrow \Eq(f,g)$ such that $i\circ j'=j$.

This is because by definition the image of $j$ is contained in $\Eq(f,g)$. Thus any pair of parallel morphisms in $\Grp$ has an equalizer. ([[Category Theory] §Limits, ⁋Example 7](/en/math/category_theory/limits#ex7)) In fact, any pair of parallel morphisms in $\Grp$ also has a coequalizer, but to define this we must first define normal subgroups and quotient groups. 

## Kernel and Image of a Homomorphism

The group $\{e\}$ is a zero object in the category $\Grp$. Therefore, for any groups $G,H$, the zero map $e:G \rightarrow H$ is defined as the composite $G\rightarrow\{e\}\rightarrow H$. 

On the other hand, the condition that a group homomorphism $f$ is injective can be expressed as follows.

::: Proposition 3
A homomorphism $f:G\rightarrow G'$ is injective if and only if $f^{-1}(e')=\{e\}$.
:::
::: Proof
If $f$ is injective, it is obvious that $f^{-1}(e')=\{e\}$.

Conversely, assume that $f^{-1}(e')=\{e\}$. Suppose $f(x)=f(y)$ for $x,y\in G$. Then

$$e'=f(x)f(y)^{-1}=f(xy^{-1})$$

and by assumption $xy^{-1}=e$. From this we know that $x=y$.
:::

For any homomorphism $f:G\rightarrow G'$, the above set $f^{-1}(e')$ indicates how far $f$ is from being injective. This set is called as follows.

::: Definition 4
The *kernel* of a homomorphism $f:G\rightarrow G'$ is defined as the set $f^{-1}(e')$, and is denoted $\ker f$.
:::

Then $f^{-1}(e')$ is not merely a set, but becomes a subgroup of $G$.

::: Proposition 5
For any homomorphism $f:G\rightarrow G'$, $\ker f$ is a subgroup of $G$.
:::
::: Proof
By definition, $\ker f=\Eq(f,e)$.
:::

On the other hand, when any magma homomorphism $f:A\rightarrow A'$ is given, we have verified that its image $\im f$ is a submagma of $A'$. (the calculation before [§Algebraic Structures, ⁋Definition 8](/en/math/algebraic_structures/algebraic_structures#def8)) However, since a submagma of a group need not be a subgroup in general, the following proposition must be proved separately. 

::: Proposition 6
For any homomorphism $f:G\rightarrow G'$, $\im f$ is a subgroup of $G'$.
:::
::: Proof
We already know that $\im f$ is a submagma of $G'$, so by [§Semigroups, Monoids, and Groups, ⁋Proposition 15](/en/math/algebraic_structures/groups#prop15) it suffices to show that $\im f$ is closed under taking inverses. Let $y\in\im f$ and suppose $x\in G$ satisfies $f(x)=y$. Then from

$$f(x^{-1})=f(x)^{-1}=y^{-1}$$

we know that $y^{-1}\in\im f$.
:::


---

**References**

**[Bou]** Bourbaki, N. Algebra I. *Elements of Mathematics*. Springer. 1998.  

---
