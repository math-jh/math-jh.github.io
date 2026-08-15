---
title: "Direct Product, Direct Sum, and Tensor Product of Algebras"
description: "This post covers the natural algebra structures on the direct product, direct sum, and tensor product of algebras over a commutative ring, along with their basic properties."
excerpt: "Product, direct sum, and tensor product structures of algebras"

categories: [Math / Algebraic Structures]
permalink: /en/math/algebraic_structures/operations_of_algebras
sidebar: 
    nav: "algebraic_structures-en"

date: 2024-10-07
weight: 302
translated_at: 2026-08-15T13:17:41+00:00
translation_source: kimi-cli
---
We examined operations on modules in [§Direct Products, Direct Sums, and Tensor Products of Modules](/en/math/algebraic_structures/operations_of_modules), and operations on rings in [§Products, Coproducts, and Tensor Products of Rings](/en/math/algebraic_structures/operations_of_rings). Since an $A$-algebra is a structure obtained by adding a bilinear multiplication on top of an $A$-module ([§Algebras, ⁋Definition 1](/en/math/algebraic_structures/algebras#def1)), the content of this post is to verify that the multiplication behaves well under the operations defined at the module level. As in [§Algebras](/en/math/algebraic_structures/algebras), $A$ is always a commutative ring.

## Direct Products and Direct Sums of Algebras

Let a family $(E_i)_{i\in I}$ of $A$-algebras be given. Then we can first consider the direct product $\prod_{i\in I}E_i$ as an $A$-module, and it is natural to equip it with componentwise multiplication.

::: Proposition 1
For a family $(E_i)_{i\in I}$ of $A$-algebras, if we define multiplication on the $A$-module $\prod_{i\in I}E_i$ by the formula

$$(x_i)_{i\in I}(y_i)_{i\in I}=(x_iy_i)_{i\in I}$$

then $\prod_{i\in I}E_i$ becomes an $A$-algebra. Moreover, if all $E_i$ are associative (resp. commutative, unital), then so is $\prod_{i\in I}E_i$.
:::
::: Proof
We must show that the above multiplication is $A$-bilinear. For arbitrary $\alpha\in A$ and $x=(x_i),y=(y_i),z=(z_i)\in\prod E_i$, since the multiplication on each $E_i$ is $A$-bilinear, we have

$$\bigl((\alpha x+y)z\bigr)_i=(\alpha x_i+y_i)z_i=\alpha(x_iz_i)+y_iz_i=\bigl(\alpha(xz)+yz\bigr)_i$$

and similarly for the second variable. Associativity and commutativity are checked componentwise, and if all $E_i$ have identity elements $1_{E_i}$, then $(1_{E_i})_{i\in I}$ is the identity element of $\prod E_i$.
:::

We name this as follows.

::: Definition 2
The $A$-algebra $\prod_{i\in I}E_i$ equipped with the multiplication defined in [Proposition 1](#prop1) is called the *direct product* of the $E_i$. The canonical projections $\pr_i:\prod E_i \rightarrow E_i$ are all $A$-algebra homomorphisms.
:::

Then this direct product is the product in the category of $A$-algebras; that is, the following universal property holds.

::: Proposition 3
Let an arbitrary $A$-algebra $F$ and $A$-algebra homomorphisms $u_i:F \rightarrow E_i$ be given. Then there exists a unique $A$-algebra homomorphism $u:F \rightarrow \prod_{i\in I}E_i$ such that $\pr_i\circ u=u_i$ holds for all $i$.
:::
::: Proof
By the universal property of the product at the level of $A$-modules ([§Direct Products, Direct Sums, and Tensor Products of Modules, ⁋Theorem 1](/en/math/algebraic_structures/operations_of_modules#thm1)), there exists a unique $A$-linear map $u:F \rightarrow\prod E_i$, namely $u(x)=(u_i(x))_{i\in I}$, satisfying the condition. That this preserves multiplication follows from the fact that each $u_i$ preserves multiplication:

$$u(xy)=(u_i(xy))_{i\in I}=(u_i(x)u_i(y))_{i\in I}=u(x)u(y)$$
:::

On the other hand, as we did with other algebraic structures, we can consider finitely supported elements inside the direct product.

::: Proposition 4
The $A$-module direct sum $\bigoplus_{i\in I}E_i$ is a two-sided ideal of the direct product $\prod_{i\in I}E_i$. In particular, if $I$ is a finite set, then $\bigoplus_{i\in I}E_i=\prod_{i\in I}E_i$.
:::
::: Proof
That $\bigoplus E_i$ is a submodule of $\prod E_i$ is by definition, so we only need to check the absorption condition. For arbitrary $x=(x_i)\in\bigoplus E_i$ and $\alpha=(\alpha_i)\in\prod E_i$, the $i$-th component of the componentwise product $\alpha x=(\alpha_ix_i)$ can be nonzero only if $x_i\neq 0$, so the support of $\alpha x$ is contained in the support of $x$. This is a finite set, so $\alpha x\in\bigoplus E_i$, and the same holds for $x\alpha$. Finally, if $I$ is a finite set, the finitely supported condition holds automatically, so the two sets coincide.
:::

::: Definition 5
The (possibly non-unital) $A$-algebra $\bigoplus_{i\in I}E_i$ obtained by restricting the multiplication of the direct product is called the *direct sum* of the $E_i$.
:::

What must be noted is that this is *not* the coproduct in the category of $A$-algebras. First, even in the general sense of [§Algebras, ⁋Definition 1](/en/math/algebraic_structures/algebras#def1), the canonical injection $\iota_j:E_j\hookrightarrow\bigoplus E_i$ preserves addition, scalar multiplication, and multiplication, but these data do not satisfy the universal property. For example, consider the situation where $E_1=E_2=A$ and

$$f_i: E_i\rightarrow A$$

are each given as $\id_A$. For $E_1\oplus E_2$ to be a coproduct, there must exist $f: E_1\oplus E_2\rightarrow A$ making the following diagram

{% diagram Math/Algebraic_Structures/Operations_of_Algebras-1.svg width="13.63em" alt="coproduct" %}

commute. However, for arbitrary $(a,b)\in E_1\oplus E_2$, we must have

$$f\bigl((a,b)\bigr)=f\bigl((a,0)+(0,b)\bigr)=f\bigl((a,0)\bigr)+f\bigl((0,b)\bigr)=(f\circ\iota_1)(a)+(f\circ\iota_2)(b)=a+b$$

yet the following two computations

$$f\bigl((a,b)(c,d)\bigr)=ac+bd\neq (a+b)(c+d)=f(a,b)f(c,d)$$

show that $f$ cannot preserve multiplication.

Moreover, under our convention that $A$-algebras and their homomorphisms are always unital, the situation is even worse. The $\iota_j$ do not send $1_{E_j}$ to the identity element of $\bigoplus E_i$, so they are not $A$-algebra homomorphisms to begin with, and if $I$ is an infinite set and all $E_i$ are nonzero, then by [Proposition 4](#prop4), $\bigoplus E_i$ is a proper ideal of $\prod E_i$ and thus has no identity element.

## Tensor Products of Algebras

The notion that gives the correct coproduct in the category of commutative $A$-algebras is the tensor product. Basically, this is the $A$-algebra obtained by appropriately defining multiplication on the $A$-module $E\otimes_AE'$ ([§Direct Products, Direct Sums, and Tensor Products of Modules, ⁋Proposition 8](/en/math/algebraic_structures/operations_of_modules#prop8)), and the multiplication we want is given by the formula

$$(x\otimes x')(y\otimes y')=xy\otimes x'y'\tag{1}$$

However, since elements of $E\otimes_AE'$ are not in general uniquely expressed as sums of elements of the form $x\otimes x'$, we must first verify that this formula gives a well-defined $A$-bilinear map.

::: Proposition 6
For two $A$-algebras $E,E'$, there exists a unique $A$-bilinear map $\mu:(E\otimes_AE')\times(E\otimes_AE') \rightarrow E\otimes_AE'$ satisfying equation $(1)$.
:::
::: Proof
First, fix $(y,y')\in E\times E'$. Then the map

$$E\times E' \rightarrow E\otimes_AE';\qquad (x,x')\mapsto xy\otimes x'y'$$

is $A$-bilinear since the multiplication on $E,E'$ is $A$-linear in each variable, and therefore by the universal property of [§Direct Products, Direct Sums, and Tensor Products of Modules, ⁋Proposition 8](/en/math/algebraic_structures/operations_of_modules#prop8), it induces a unique $A$-linear map $m_{(y,y')}:E\otimes_AE' \rightarrow E\otimes_AE'$ such that $x\otimes x'\mapsto xy\otimes x'y'$.

Now consider the correspondence $(y,y')\mapsto m_{(y,y')}$. This is a map from $E\times E'$ to $\End_{\lMod{A}}(E\otimes_AE')$, and again by the bilinearity of multiplication, it is $A$-bilinear. For example,

$$m_{(\alpha y+z,y')}(x\otimes x')=x(\alpha y+z)\otimes x'y'=\alpha(xy\otimes x'y')+xz\otimes x'y'=\bigl(\alpha m_{(y,y')}+m_{(z,y')}\bigr)(x\otimes x')$$

holds on generators, so $m_{(\alpha y+z,y')}=\alpha m_{(y,y')}+m_{(z,y')}$. Thus applying the universal property once more, we obtain an $A$-linear map $\tilde{m}:E\otimes_AE' \rightarrow \End_{\lMod{A}}(E\otimes_AE')$ such that $y\otimes y'\mapsto m_{(y,y')}$. Now defining

$$\mu(s,t)=\tilde{m}(t)(s)$$

we see that $\mu$ is $A$-linear in each variable and satisfies equation $(1)$ on generators. Uniqueness is obvious from the fact that $E\otimes_AE'$ is generated by elements of the form $x\otimes x'$.
:::

::: Definition 7
For two $A$-algebras $E,E'$, the $A$-algebra $E\otimes_AE'$ equipped with the multiplication from [Proposition 6](#prop6) is called the *tensor product* of $E$ and $E'$.
:::

As with the direct product, the tensor product inherits the properties of the two algebras. For example, if $E,E'$ are both associative, then on generators we have

$$\bigl((x\otimes x')(y\otimes y')\bigr)(z\otimes z')=(xy)z\otimes (x'y')z'=x(yz)\otimes x'(y'z')=(x\otimes x')\bigl((y\otimes y')(z\otimes z')\bigr)$$

so $E\otimes_AE'$ is also associative, and similarly if $E,E'$ are commutative then $E\otimes_AE'$ is also commutative. Also, if $E,E'$ are unital, then $1_E\otimes 1_{E'}$ is the identity element of $E\otimes_AE'$. In particular, if $E,E'$ are associative unital, then the two $A$-algebra homomorphisms

$$\iota:E \rightarrow E\otimes_AE';\quad x\mapsto x\otimes 1_{E'},\qquad \iota':E' \rightarrow E\otimes_AE';\quad x'\mapsto 1_E\otimes x'$$

are defined, and their images commute with each other. That is, $(x\otimes 1)(1\otimes x')=x\otimes x'=(1\otimes x')(x\otimes 1)$.

As we introduced initially, the tensor product becomes the coproduct in the category of commutative $A$-algebras. The following theorem explains this.

::: Theorem 8
Let commutative $A$-algebras $E,E'$ and an arbitrary commutative $A$-algebra $F$, and $A$-algebra homomorphisms $u:E \rightarrow F$, $u':E' \rightarrow F$ preserving identity elements be given. Then there exists a unique $A$-algebra homomorphism $w:E\otimes_AE' \rightarrow F$ satisfying $w\circ\iota=u$, $w\circ\iota'=u'$.
:::
::: Proof
Define the map $E\times E' \rightarrow F$ by $(x,x')\mapsto u(x)u'(x')$; this is $A$-bilinear, so there exists a unique $A$-linear map $w:E\otimes_AE' \rightarrow F$ such that $w(x\otimes x')=u(x)u'(x')$. That $w$ preserves multiplication is sufficient to check on generators:

$$w\bigl((x\otimes x')(y\otimes y')\bigr)=w(xy\otimes x'y')=u(xy)u'(x'y')=u(x)u(y)u'(x')u'(y')=u(x)u'(x')u(y)u'(y')=w(x\otimes x')w(y\otimes y')$$

where the fourth equality uses the assumption that $F$ is commutative. Also $w(1_E\otimes 1_{E'})=u(1_E)u'(1_{E'})=1_F$, and $w\circ\iota=u$ and $w\circ\iota'=u'$ are obvious from the definition.

Let us show uniqueness. If $w'$ satisfies the same conditions, then for arbitrary generators

$$w'(x\otimes x')=w'\bigl((x\otimes 1_{E'})(1_E\otimes x')\bigr)=w'(\iota(x))w'(\iota'(x'))=u(x)u'(x')=w(x\otimes x')$$

so $w'=w$.
:::

Thus, $E\otimes_AE'$ is the coproduct of $E$ and $E'$ in the category of commutative $A$-algebras.

::: Example 9
The tensor product of polynomial algebras is the polynomial algebra with the variables combined. That is,

$$A[\x]\otimes_AA[\y]\cong A[\x,\y]$$

holds. This follows from the fact that the functor $A[-]:\Set \rightarrow \cAlg{A}$ examined in [§Algebras, ⁋Proposition 8](/en/math/algebraic_structures/algebras#prop8) is a left adjoint. Since left adjoints preserve colimits, it sends the coproduct $\{\x\}\sqcup\{\y\}=\{\x,\y\}$ of one-point sets (in $\Set$) to the coproduct in $\cAlg{A}$, and by [Theorem 8](#thm8), this is exactly the tensor product. Of course, one can also directly verify the two isomorphisms $\x\otimes 1\mapsto \x$, $1\otimes \y\mapsto \y$.
:::

---

**References**

**[Bou]** Bourbaki, N. Algebra I. *Elements of Mathematics*. Springer. 1998.  

---
