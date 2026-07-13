---
title: "Group Homomorphisms"
excerpt: "Definition and properties of group homomorphisms, kernels and images"

categories: [Math / Algebraic Structures]
permalink: /en/math/algebraic_structures/group_homomorphisms
sidebar:
    nav: "algebraic_structures-en"

date: 2026-03-11
weight: 4
translated_at: 2026-05-29T02:00:58+00:00
translation_source: kimi-cli
last_polished_at: 2026-05-24T08:00:03+00:00
---
For the time being, we explore properties of groups. Thus, we will simply refer to group homomorphisms between groups as homomorphisms.

From [§Algebraic Structures, ⁋Definition 6](/en/math/algebraic_structures/algebraic_structures#def6), we can also define (group) isomorphisms, and from this definition and [\[Set Theory\] §Operations on Functions, ⁋Proposition 5](/en/math/set_theory/operation_of_functions#prop5), it is clear that any isomorphism must be a bijection. In many cases, the converse also holds.

::: Proposition 1
A magma homomorphism $f:A\rightarrow A'$ is an isomorphism if and only if $f$ is a bijection.

If $A$ has an identity element $e$ and $f:A\rightarrow A'$ is a bijection, then $f(e)$ is the identity element of $A'$, and consequently $f^{-1}$ is a magma homomorphism that sends the identity element of $A'$ to the identity element of $A$.
:::

::: Proof
It suffices to prove the converse. Since $f$ is a bijection, there exists an inverse function $f^{-1}:G'\rightarrow G$. If $f^{-1}$ is a homomorphism, then by definition $f$ is an isomorphism.

Take arbitrary $y, y'\in  A'$. Since $f$ is a bijection, there exist unique $x$ and $x'$ such that $f(x)=y$ and $f(x')=y'$. Now

$$f^{-1}(yy')=f^{-1}(f(x)f(x'))=f^{-1}(f(xx'))=xx'=f^{-1}(y)f^{-1}(y')$$

so $f^{-1}$ is a homomorphism, and therefore $f$ is an isomorphism.

On the other hand, if $f:A\rightarrow A'$ is a bijection, then for any $y\in A'$, there exists a unique $x\in A$ such that $f(x)=y$. Now

$$y=f(x)=f(xe)=f(x)f(e),\qquad y=f(x)=f(ex)=f(e)f(x)$$

so $f(e)$ is the identity element of $A'$.
:::

## Equalizer of Homomorphisms

The following holds.

::: Proposition 2
Let $f,g:G \rightarrow H$ be group homomorphisms. Then

$$\Eq(f,g)=\{x\in G\mid f(x)=g(x)\}$$

is a subgroup of $G$.
:::
::: Proof
If $x,y\in \Eq(f,g)$, then

$$f(xy^{-1})=f(x)f(y)^{-1}=g(x)g(y)^{-1}=g(xy^{-1})$$

so $xy^{-1}\in\Eq(f,g)$. Therefore, by [§Semigroups, Monoids, and Groups, ⁋Proposition 15](/en/math/algebraic_structures/groups#prop15), we obtain the desired result.
:::

The map $i:\Eq(f,g)\rightarrow G$ defined in this way has the following property.

> If a group homomorphism $j:G' \rightarrow G$ satisfies $f\circ j=g\circ j$, then there exists a unique homomorphism $j': G' \rightarrow G$ such that $i\circ j'=j$.

This is because the image of $j$ is contained in $\Eq(f,g)$ by definition. Thus every morphism in $\Grp$ has an equalizer. ([\[Category Theory\] §Limits, ⁋Example 7](/en/math/category_theory/limits#ex7)) In fact, every morphism in $\Grp$ also has a coequalizer, but to define this, we first need to define normal subgroups and quotient groups.

## Kernel and Image of Homomorphisms

The group $\{e\}$ is a zero object in the category $\Grp$. Therefore, for any groups $G,H$, the zero map $e:G \rightarrow H$ is defined as the composite $G\rightarrow\{e\}\rightarrow H$.

Meanwhile, whether a group homomorphism $f$ is injective can be expressed as follows.

::: Proposition 3
A homomorphism $f:G\rightarrow G'$ is injective if and only if $f^{-1}(e')=\{e\}$.
:::
::: Proof
If $f$ is injective, then it is clear that $f^{-1}(e')=\{e\}$.

Conversely, suppose $f^{-1}(e')=\{e\}$. Let $x,y\in G$ satisfy $f(x)=f(y)$. Then

$$e'=f(x)f(y)^{-1}=f(xy^{-1})$$

and by assumption, $xy^{-1}=e$. Hence $x=y$.
:::

For any homomorphism $f:G\rightarrow G'$, the set $f^{-1}(e')$ above shows how far $f$ is from being injective. This set is named as follows.

::: Definition 4
The *kernel* of a homomorphism $f:G\rightarrow G'$ is defined as the set $f^{-1}(e')$ and denoted by $\ker f$.
:::

Then $f^{-1}(e')$ is not merely a set but a subgroup of $G$.

::: Proposition 5
For any homomorphism $f:G\rightarrow G'$, $\ker f$ is a subgroup of $G$.
:::
::: Proof
By definition, $\ker f=\Eq(f,e)$.
:::

On the other hand, we verified that for any magma homomorphism $f:A\rightarrow A'$, its image $\im f$ is a submagma of $A'$. (See the calculation before [§Algebraic Structures, ⁋Definition 8](/en/math/algebraic_structures/algebraic_structures#def8)) However, a submagma of a group is not necessarily a subgroup in general, so the following proposition requires a separate proof.

::: Proposition 6
For any homomorphism $f:G\rightarrow G'$, $\im f$ is a subgroup of $G'$.
:::
::: Proof
We already know that $\im f$ is a submagma of $G'$, so by [§Semigroups, Monoids, and Groups, ⁋Proposition 15](/en/math/algebraic_structures/groups#prop15), it suffices to show that $\im f$ is closed under taking inverses. Let $y\in\im f$ and suppose $x\in G$ satisfies $f(x)=y$. Then

$$f(x^{-1})=f(x)^{-1}=y^{-1}$$

so $y^{-1}\in\im f$.
:::


---

**References**

**[Bou]** Bourbaki, N. Algebra I. *Elements of Mathematics*. Springer. 1998.

---

[^1]: To avoid cluttered notation, we wrote $$\bar{a}$$ instead of $$a\ker f$$.
