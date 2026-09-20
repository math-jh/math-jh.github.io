---
title: "Direct Product, Direct Sum, and Tensor Product of Algebras"
description: "This covers the algebra structures naturally endowed on the direct product, direct sum, and tensor product of algebras over a commutative ring, along with their properties."
excerpt: "Product, direct sum, and tensor product structures of algebras"

categories: [Math / Algebraic Structures]
permalink: /en/math/algebraic_structures/operations_of_algebras
sidebar: 
    nav: "algebraic_structures-en"

date: 2024-10-07
weight: 302
translated_at: 2026-09-19T15:15:04+00:00
translation_source: antigravity-gemini-3.8-flash-high
last_polished_at: 2026-09-20T03:15:04+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
We examined operations on modules in [§Direct Products, Direct Sums, and Tensor Products of Modules](/en/math/algebraic_structures/operations_of_modules){: data-relation="required" reviewed="" }, and operations on rings in [§Products, Coproducts, and Tensor Products of Rings](/en/math/algebraic_structures/operations_of_rings){: data-relation="weak" reviewed="" }. Since an $A$-algebra is a structure obtained by adding a bilinear multiplication on an $A$-module ([§Algebras, ⁋Definition 1](/en/math/algebraic_structures/algebras#def1){: data-relation="required" reviewed="" }), the subject of this post is to check whether multiplication carries over well to the operations defined at the module level. As in [§Algebras](/en/math/algebraic_structures/algebras){: data-relation="weak" }, $A$ is always a commutative ring.

## Direct Products and Direct Sums of Algebras

Let a family of $A$-algebras $(E_i)_{i\in I}$ be given. Then we can first consider the $A$-module direct product $\prod_{i\in I}E_i$, and it is natural to define componentwise multiplication on it.

::: Proposition 1
For a family of $A$-algebras $(E_i)_{i\in I}$, if multiplication is defined on the $A$-module $\prod_{i\in I}E_i$ by the formula

$$(x_i)_{i\in I}(y_i)_{i\in I}=(x_iy_i)_{i\in I}$$

then $\prod_{i\in I}E_i$ becomes an $A$-algebra. Moreover, if all $E_i$ are associative (resp. commutative, unital), then so is $\prod_{i\in I}E_i$.
:::
::: Proof
We must show that the above multiplication is $A$-bilinear. For arbitrary $\alpha\in A$ and $x=(x_i),y=(y_i),z=(z_i)\in\prod E_i$, since the multiplication of $E_i$ is $A$-bilinear in each component, we have

$$\bigl((\alpha x+y)z\bigr)_i=(\alpha x_i+y_i)z_i=\alpha(x_iz_i)+y_iz_i=\bigl(\alpha(xz)+yz\bigr)_i$$

and similarly for the second variable. Associativity and commutativity are checked componentwise, and if all $E_i$ have an identity element $1_{E_i}$, then $(1_{E_i})_{i\in I}$ is the identity element of $\prod E_i$.
:::

We name this as follows.

::: Definition 2
The $A$-algebra $\prod_{i\in I}E_i$ equipped with the multiplication defined in [Proposition 1](#prop1){: data-relation="required" reviewed="" } is called the *direct product* of the $E_i$. The canonical projections $\pr_i:\prod E_i \rightarrow E_i$ are all $A$-algebra homomorphisms.
:::

Then the direct product defined in this way is the product in the category of $A$-algebras; that is, the following universal property holds.

::: Proposition 3
Let an $A$-algebra $F$ and $A$-algebra homomorphisms $u_i:F \rightarrow E_i$ be given. Then, satisfying $\pr_i\circ u=u_i$ for all $i$, there exists a unique $A$-algebra homomorphism $u:F \rightarrow \prod_{i\in I}E_i$.
:::
::: Proof
By the universal property of the product at the level of $A$-modules ([§Direct Products, Direct Sums, and Tensor Products of Modules, ⁋Theorem 1](/en/math/algebraic_structures/operations_of_modules#thm1){: data-relation="required" reviewed="" }), there exists a unique $A$-linear map $u:F \rightarrow\prod E_i$, that is, $u(x)=(u_i(x))_{i\in I}$, satisfying the condition. This preserves multiplication because each $u_i$ preserves multiplication, from which

$$u(xy)=(u_i(xy))_{i\in I}=(u_i(x)u_i(y))_{i\in I}=u(x)u(y)$$

follows.
:::

Meanwhile, as we did for other algebraic structures, we can consider the finitely supported elements in the direct product.

::: Proposition 4
The $A$-module direct sum $\bigoplus_{i\in I}E_i$ is a two-sided ideal of the direct product $\prod_{i\in I}E_i$. In particular, if $I$ is finite, then $\bigoplus_{i\in I}E_i=\prod_{i\in I}E_i$.
:::
::: Proof
That $\bigoplus E_i$ is a submodule of $\prod E_i$ holds by definition, so we only need to check the absorption condition. For any $x=(x_i)\in\bigoplus E_i$ and $\alpha=(\alpha_i)\in\prod E_i$, in the componentwise product $\alpha x=(\alpha_ix_i)$, the $i$-th component is not $0$ only if $x_i\neq 0$, so the support of $\alpha x$ is contained in the support of $x$. Since this is a finite set, $\alpha x\in\bigoplus E_i$, and the same holds for $x\alpha$. Finally, if $I$ is finite, the finitely supported condition holds automatically, so the two sets coincide.
:::

::: Definition 5
The (possibly non-unital) $A$-algebra $\bigoplus_{i\in I}E_i$ obtained by restricting the multiplication of the direct product is called the *direct sum* of the $E_i$.
:::

Note that this is *not* the coproduct in the category of $A$-algebras. First, even in the general sense of [§Algebras, ⁋Definition 1](/en/math/algebraic_structures/algebras#def1){: data-relation="weak" }, the canonical injections $\iota_j:E_j\hookrightarrow\bigoplus E_i$ preserve addition, scalar multiplication, and multiplication, but these data do not satisfy the universal property. For example, consider the situation where $E_1=E_2=A$, and each

$$f_i: E_i\rightarrow A$$

is given by $\id_A$. For $E_1\oplus E_2$ to be a coproduct, the diagram

{% diagram Math/Algebraic_Structures/Operations_of_Algebras-1.svg width="13.63em" alt="coproduct" %}

must commute for some $f: E_1\oplus E_2\rightarrow A$. However, for any $(a,b)\in E_1\oplus E_2$, we must have

$$f\bigl((a,b)\bigr)=f\bigl((a,0)+(0,b)\bigr)=f\bigl((a,0)\bigr)+f\bigl((0,b)\bigr)=(f\circ\iota_1)(a)+(f\circ\iota_2)(b)=a+b$$

but except when $ad+bc$ is $0$, in general the two calculations

$$f\bigl((a,b)(c,d)\bigr)=ac+bd,\qquad f(a,b)f(c,d)=(a+b)(c+d)$$

do not coincide. Therefore, in general, $f$ does not preserve multiplication.

On the other hand, in the category of associative unital $A$-algebras and unital homomorphisms, $\Alg{A}$, there is also an issue with the canonical injections. If $I$ is a finite set and each $E_i$ is unital, the identity element of $\bigoplus E_i=\prod E_i$ is $(1_{E_i})_{i\in I}$, so in general $\iota_j$ does not preserve the identity element. Moreover, if $I$ is an infinite set and every $E_i$ is nonzero, then no element of $\bigoplus E_i$ can act as an identity on all components, so $\bigoplus E_i$ does not have an identity element.

## Tensor Product of Algebras

In the category of commutative associative unital $A$-algebras, it is the tensor product that gives the correct notion of coproduct. Fundamentally, this is obtained by suitably defining a multiplication on the $A$-module $E\otimes_AE'$ ([§Direct Products, Direct Sums, and Tensor Products of Modules, ⁋Proposition 8](/en/math/algebraic_structures/operations_of_modules#prop8){: data-relation="required" reviewed="" }) to form an $A$-algebra, and the multiplication we desire is given by the formula

$$(x\otimes x')(y\otimes y')=xy\otimes x'y'\tag{1}$$

However, since an element of $E\otimes_AE'$ is not in general uniquely expressed as a sum of elements of the form $x\otimes x'$, we must first check whether this formula gives a well-defined $A$-bilinear map.

::: Proposition 6
For two $A$-algebras $E,E'$, there exists, satisfying equation $(1)$, a unique $A$-bilinear map $\mu:(E\otimes_AE')\times(E\otimes_AE') \rightarrow E\otimes_AE'$.
:::
::: Proof
First, fix $(y,y')\in E\times E'$. Then the function

$$E\times E' \rightarrow E\otimes_AE';\qquad (x,x')\mapsto xy\otimes x'y'$$

is, since the multiplications on $E,E'$ are $A$-linear in each variable, $A$-bilinear, and thus, by the universal property of [§Direct Products, Direct Sums, and Tensor Products of Modules, ⁋Proposition 8](/en/math/algebraic_structures/operations_of_modules#prop8){: data-relation="required" reviewed="" }, induces, such that $x\otimes x'\mapsto xy\otimes x'y'$, a unique $A$-linear map $m_{(y,y')}:E\otimes_AE' \rightarrow E\otimes_AE'$.

Now consider the assignment $(y,y')\mapsto m_{(y,y')}$; this is a function from $E\times E'$ to $\End_{\lMod{A}}(E\otimes_AE')$, which is again $A$-bilinear by the bilinearity of multiplication. For instance, since

$$m_{(\alpha y+z,y')}(x\otimes x')=x(\alpha y+z)\otimes x'y'=\alpha(xy\otimes x'y')+xz\otimes x'y'=\bigl(\alpha m_{(y,y')}+m_{(z,y')}\bigr)(x\otimes x')$$

holds on the generators, we have $m_{(\alpha y+z,y')}=\alpha m_{(y,y')}+m_{(z,y')}$. Therefore, applying the universal property once more, we obtain, such that $y\otimes y'\mapsto m_{(y,y')}$, an $A$-linear map $\tilde{m}:E\otimes_AE' \rightarrow \End_{\lMod{A}}(E\otimes_AE')$. Now, if we define

$$\mu(s,t)=\tilde{m}(t)(s)$$

then $\mu$ is $A$-linear in each variable, and satisfies equation $(1)$ on the generators. Uniqueness is clear from the fact that $E\otimes_AE'$ is generated by elements of the form $x\otimes x'$.
:::

::: Definition 7
For two $A$-algebras $E,E'$, the $A$-algebra $E\otimes_AE'$ equipped with the multiplication from [Proposition 6](#prop6){: data-relation="required" reviewed="" } is called the *tensor product* of $E$ and $E'$.
:::

As with direct products, the tensor product inherits the properties of both algebras. For instance, if $E,E'$ are both associative, then since

$$\bigl((x\otimes x')(y\otimes y')\bigr)(z\otimes z')=(xy)z\otimes (x'y')z'=x(yz)\otimes x'(y'z')=(x\otimes x')\bigl((y\otimes y')(z\otimes z')\bigr)$$

holds on the generators, $E\otimes_AE'$ is also associative, and in the same way, if $E,E'$ are commutative, then $E\otimes_AE'$ is also commutative. Also, if $E,E'$ are unital, then $1_E\otimes 1_{E'}$ is the identity element of $E\otimes_AE'$. In particular, if $E,E'$ are unital, two unital $A$-algebra homomorphisms

$$\iota:E \rightarrow E\otimes_AE';\quad x\mapsto x\otimes 1_{E'},\qquad \iota':E' \rightarrow E\otimes_AE';\quad x'\mapsto 1_E\otimes x'$$

are defined, and their images commute with each other. That is, $(x\otimes 1)(1\otimes x')=x\otimes x'=(1\otimes x')(x\otimes 1)$.

As we initially introduced, the tensor product is the coproduct in $\cAlg{A}$. The following theorem explains this.

::: Theorem 8
Let commutative associative unital $A$-algebras $E,E',F$ and unital $A$-algebra homomorphisms $u:E \rightarrow F$ and $u':E' \rightarrow F$ be given. Then, satisfying $w\circ\iota=u$ and $w\circ\iota'=u'$, there exists a unique unital $A$-algebra homomorphism $w:E\otimes_AE' \rightarrow F$.
:::
::: Proof
If we define a function $E\times E' \rightarrow F$ by $(x,x')\mapsto u(x)u'(x')$, this is $A$-bilinear, so satisfying $w(x\otimes x')=u(x)u'(x')$, there exists a unique $A$-linear map $w:E\otimes_AE' \rightarrow F$. To see that $w$ preserves multiplication, it suffices to check on generators:

$$w\bigl((x\otimes x')(y\otimes y')\bigr)=w(xy\otimes x'y')=u(xy)u'(x'y')=u(x)u(y)u'(x')u'(y')=u(x)u'(x')u(y)u'(y')=w(x\otimes x')w(y\otimes y')$$

where the fourth equality uses the assumption that $F$ is associative and commutative. Moreover, $w(1_E\otimes 1_{E'})=u(1_E)u'(1_{E'})=1_F$, and $w\circ\iota=u$ and $w\circ\iota'=u'$ are clear from the definition.

We show uniqueness. If $w'$ satisfies the same condition, then for any generator,

$$w'(x\otimes x')=w'\bigl((x\otimes 1_{E'})(1_E\otimes x')\bigr)=w'(\iota(x))w'(\iota'(x'))=u(x)u'(x')=w(x\otimes x')$$

and thus $w'=w$.
:::

That is, $E\otimes_AE'$ is, in $\cAlg{A}$, the coproduct of $E$ and $E'$. However, inspecting the proof of the theorem above, the commutativity of $F$ is used only to swap the order of $u(x)$ and $u'(x')$, so the condition actually needed instead of commutativity is merely that $u(E)$ and $u'(E')$ commute with each other. Thus we obtain the following more general claim.

> Let $E,E'$ be unital $A$-algebras, and let $F$ be an associative unital $A$-algebra. If the images of the two unital $A$-algebra homomorphisms $u:E\rightarrow F$ and $u':E'\rightarrow F$ commute with each other, then, satisfying $w\circ\iota=u$ and $w\circ\iota'=u'$, there exists a unique unital $A$-algebra homomorphism $w:E\otimes_AE'\rightarrow F$.

::: Example 9
The tensor product of polynomial algebras is the polynomial algebra obtained by combining the variables. That is,

$$A[\x]\otimes_AA[\y]\cong A[\x,\y]$$

holds. This follows from the fact that the functor $A[-]:\Set \rightarrow \cAlg{A}$ we examined in [§Algebras, ⁋Proposition 8](/en/math/algebraic_structures/algebras#prop8){: data-relation="required" reviewed="" } is a left adjoint. Since a left adjoint preserves colimits, it sends the coproduct of one-point sets (in sets) $\{\x\}\sqcup\{\y\}=\{\x,\y\}$ to the coproduct in $\cAlg{A}$, which by [Theorem 8](#thm8){: data-relation="required" reviewed="" } is precisely the tensor product. Of course, that the above isomorphism is defined by the two formulas

$$\x\otimes 1\mapsto \x,\qquad 1\otimes \y\mapsto \y$$

can also be directly verified.
:::

---

**References**

**[Bou]** Bourbaki, N. Algebra I. *Elements of Mathematics*. Springer. 1998.  

---
