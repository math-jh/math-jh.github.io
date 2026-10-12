---
title: "Solvability by Radicals"
description: "After examining the structure of roots of unity and cyclic extensions, we prove Galois's theorem that a polynomial is solvable by radicals if and only if its Galois group is solvable."
excerpt: "Solvability by radicals and solvable Galois group"

categories: [Math / Field Theory]
permalink: /en/math/field_theory/solvability_by_radicals
sidebar: 
    nav: "field_theory-en"

date: 2026-06-11
weight: 11
translated_at: 2026-10-12T19:15:05+00:00
translation_source: antigravity-gemini-3.8-flash-high
last_polished_at: 2026-10-12T23:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
The overarching philosophy of Galois theory is that, given a polynomial needed for an algebraic extension, one constructs a group via the action that permutes the roots of this polynomial and thereby classifies extensions; how this philosophy actually works was finally completed in [§Fundamental Theorem of Galois Theory](/en/math/field_theory/fundamental_theorem_of_galois_theory){: data-lid="9x9hd" }. In this post, we now examine the historical starting point of this theory, namely the unsolvability of degree $5$ polynomial equations. 

In this post, we assume that all fields have characteristic $0$. Then, since the characteristic exponent is $1$, the Frobenius endomorphism is the identity, so every field is perfect, and therefore every algebraic extension is separable by [§Separable Extensions, ⁋Proposition 9](/en/math/field_theory/separable_extensions#prop9){: data-lid="36i5d" }. In particular, any quasi-Galois extension is a Galois extension. This assumption allows us to avoid separate discussions concerning separability required in characteristic $p$, highlighting the purpose of our post more clearly. 

## Roots of Unity

The first ingredient for dealing with radicals is roots of unity. First, let us examine the following general lemma.

::: Lemma 1
Any finite subgroup $G$ of the multiplicative group $\mathbb{K}^\times$ of a field $\mathbb{K}$ is a cyclic group.
:::
::: Proof
First, we show that there exists an element whose order is the least common multiple of the orders of the elements of $G$. For this, it suffices to show that for $x,y\in G$ of respective orders $r,s$, there exists an element of order $n=\lcm(r,s)$, and then repeat this for all elements. 

First, consider a prime power $p^e$ appearing in the prime factorization of $n$. Then $p^e$ divides $r$ or divides $s$. That is, one of $x^{r/p^e}$ or $y^{s/p^e}$ is well-defined, and such an element is an element of order $p^e$. Therefore, it suffices to show that only in the case where $r,s$ are coprime so that $n=rs$, there exists an element of order $n$, and our claim is that the product $xy$ of these two elements is such an element. Indeed, since $G$ is abelian, it is clear that the order of $xy$ divides $rs$, and conversely, for any $k$ satisfying $(xy)^k=e$, we have

$$x^k=y^{-k}\in \langle x\rangle \cap \langle y\rangle$$

and by [\[Algebraic Structures\] §Quotient Groups, ⁋Proposition 5](/en/math/algebraic_structures/quotient_groups#prop5){: data-lid="7jjc3" }, the order of this intersection divides both $r$ and $s$, which are coprime, so it is $1$. That is, $x^k=y^k=e$, and since both $r,s$ divide $k$, $n=rs$ divides $k$, and therefore the order of $xy$ is $n$.

From this, every element of $G$ must satisfy $x^n=1$, so it is a root of the polynomial $\x^n-1$. Since a polynomial of degree $n$ over a field has at most $n$ roots ([\[Ring Theory\] §Polynomial Rings, ⁋Proposition 9](/en/math/ring_theory/polynomial_rings#prop9){: data-lid="9ta6g" }), $\lvert G\rvert\leq n$. On the other hand, for the element $a$ of order $n$ found above, $\langle a\rangle$ is a subgroup of $G$ having $n$ elements, so $G=\langle a\rangle$, and from this we obtain the desired claim. 
:::

::: Definition 2
For a field $\mathbb{K}$ and a natural number $n\geq1$, we denote the collection of roots in $\overline{\mathbb{K}}$ of the polynomial $\x^n-1$ by $\mu_n$ and call its elements *$n$-th roots of unity*. A generator of the group $\mu_n$ is called a *primitive $n$-th root of unity*.
:::

Then it is clear that $\mu_n$ is a subgroup of $\overline{\mathbb{K}}^\times$, and the derivative of $\x^n-1$ is $n\x^{n-1}$; since the characteristic is $0$, these two have no common root. Therefore, by [\[Ring Theory\] §Polynomial Rings, ⁋Proposition 11](/en/math/ring_theory/polynomial_rings#prop11){: data-lid="cxa1d" }, $\x^n-1$ has no multiple roots, and thus by [Lemma 1](#lem1){: data-lid="yaj29" }, it forms a cyclic group of order $n$. If we fix a generator of $\mu_n$, say $\zeta$, the primitive roots are the elements written, with $\gcd(a,n)=1$, in the form $\zeta^a$.

::: Proposition 3
For a primitive $n$-th root of unity $\zeta$, $\mathbb{K}(\zeta)/\mathbb{K}$ is a finite degree Galois extension and its Galois group is isomorphic to a subgroup of the abelian group $(\mathbb{Z}/n\mathbb{Z})^\times$.
:::
::: Proof
Since $\mu_n=\langle\zeta\rangle$, $\mathbb{K}(\zeta)$ contains all roots of $\x^n-1$, and is therefore the splitting field of $\x^n-1$. Then by [§Galois Extensions, ⁋Proposition 5](/en/math/field_theory/galois_extension#prop5){: data-lid="gw8c8" }, $\mathbb{K}(\zeta)/\mathbb{K}$ is quasi-Galois, and thus under the characteristic $0$ assumption it is Galois. Moreover, since it is generated by a single algebraic element, it is clear that it is a finite degree extension.

Now for any $\sigma\in\Gal(\mathbb{K}(\zeta)/\mathbb{K})$, $\sigma$ maps elements of $\mu_n$ to elements of $\mu_n$. Thus $\sigma\vert_{\mu_n}$ is an automorphism of $\mu_n$, and since $\sigma(\zeta)$ must also be a generator of $\mu_n$, that is, a primitive root, for an integer coprime to $n$, say $a_\sigma$, we can write $\sigma(\zeta)=\zeta^{a_\sigma}$. Now, that this assignment $\sigma\mapsto a_\sigma$ defines a group homomorphism

$$\Gal(\mathbb{K}(\zeta)/\mathbb{K}) \rightarrow (\mathbb{Z}/n\mathbb{Z})^\times$$

is clear from $(\sigma\tau)(\zeta)=\sigma(\zeta^{a_\tau})=\zeta^{a_\sigma a_\tau}$, and since $\mathbb{K}(\zeta)$ is generated by $\zeta$, $\sigma$ is completely determined by $\sigma(\zeta)$, so this homomorphism is injective.
:::

## Cyclic Extensions and Roots

A finite degree Galois extension whose Galois group is a cyclic group is called a *cyclic extension*. In general, adjoining a root $\alpha$ ($\alpha^n=a\in\mathbb{K}$) to a field does not immediately make the extension a Galois extension. For example, in [§Fundamental Theorem of Galois Theory, ⁋Example 4](/en/math/field_theory/fundamental_theorem_of_galois_theory#ex4){: data-lid="2e2al" }, we saw that adjoining to $\mathbb{Q}$ the element $\sqrt[3]{2}$ gives $\mathbb{Q}(\sqrt[3]{2})$, which fails to be a Galois extension because it does not contain the other conjugates $\omega\sqrt[3]{2}, \omega^2\sqrt[3]{2}$.

However, we can prove that this failure is solely due to roots of unity. That is, if the base field already contains enough primitive roots of unity, then adjoining roots and cyclic extensions become equivalent. In this section, we fix a natural number $n$, and assume that $\mathbb{K}$ contains a primitive $n$-th root of unity $\zeta$.

::: Proposition 4
For any element $a\in\mathbb{K}^\times$ and any $\alpha$ satisfying $\alpha^n=a$ with $\alpha\in\overline{\mathbb{K}}$, $\mathbb{K}(\alpha)/\mathbb{K}$ is a finite degree Galois extension, and its Galois group is a cyclic group of order dividing $n$.
:::
::: Proof
First, we can verify by direct substitution that the following elements

$$\alpha,\zeta\alpha,\ldots,\zeta^{n-1}\alpha$$

are roots of the polynomial $\x^n-a$, and since they are all distinct, they are precisely all the roots of this polynomial. Also, since $\zeta\in\mathbb{K}$ by assumption, they all belong to $\mathbb{K}(\alpha)$. That is, $\mathbb{K}(\alpha)$ is the splitting field of $\x^n-a$, and as in the proof of [Proposition 3](#prop3){: data-lid="4q873" }, it is a finite degree Galois extension.

Now for any $\sigma\in\Gal(\mathbb{K}(\alpha)/\mathbb{K})$, $\sigma(\alpha)$ is also a root of $\x^n-a$, so $\sigma(\alpha)/\alpha\in\mu_n$. Considering the correspondence $\sigma\mapsto\sigma(\alpha)/\alpha$, since $\mu_n\subseteq\mathbb{K}$ is fixed by $\sigma$, we have

$$(\sigma\tau)(\alpha)/\alpha=\sigma\bigl(\tau(\alpha)/\alpha\bigr)\cdot\sigma(\alpha)/\alpha=\bigl(\tau(\alpha)/\alpha\bigr)\bigl(\sigma(\alpha)/\alpha\bigr)$$

and this defines a group homomorphism $\Gal(\mathbb{K}(\alpha)/\mathbb{K}) \rightarrow \mu_n$, which is injective because $\sigma$ is determined by $\sigma(\alpha)$. Therefore, the Galois group is isomorphic to a subgroup of the cyclic group $\mu_n$, and by [\[Algebraic Structures\] §Quotient Groups, ⁋Proposition 5](/en/math/algebraic_structures/quotient_groups#prop5){: data-lid="8wqa7" }, its order divides $n$.
:::

Conversely, every cyclic extension is necessarily generated in this way by an appropriate radical. Here as well, we fix $n$, and for a primitive $n$th root of unity $\zeta$, we assume that $\zeta\in \mathbb{K}$.

::: Proposition 5
For a degree-$n$ cyclic extension $\mathbb{L}/\mathbb{K}$, there exists some $\alpha\in\mathbb{L}$ such that $\mathbb{L}=\mathbb{K}(\alpha)$ and $\alpha^n\in\mathbb{K}$.
:::
::: Proof
Since $\Gal(\mathbb{L}/\mathbb{K})$ is a cyclic group, there exists a generator $\sigma$. Meanwhile, by [§Fundamental Theorem of Galois Theory, ⁋Proposition 2](/en/math/field_theory/fundamental_theorem_of_galois_theory#prop2){: data-lid="b81g3" }, we have $\lvert\Gal(\mathbb{L}/\mathbb{K})\rvert=[\mathbb{L}:\mathbb{K}]=n$, and thus $\id,\sigma,\sigma^2,\ldots,\sigma^{n-1}$ are distinct homomorphisms from $\mathbb{L}$ to $\mathbb{L}$. By [§Étale Algebras, ⁋Corollary 3](/en/math/field_theory/etale_algebras#cor3){: data-lid="x94nv" }, these are linearly independent in the $\mathbb{L}$-vector space, so the linear combination

$$\id+\zeta\sigma+\zeta^2\sigma^2+\cdots+\zeta^{n-1}\sigma^{n-1}$$

is not the zero map. That is, for some $x\in\mathbb{L}$, we have

$$\alpha=x+\zeta\sigma(x)+\zeta^2\sigma^2(x)+\cdots+\zeta^{n-1}\sigma^{n-1}(x)\neq0$$

Now, since $\zeta\in\mathbb{K}$ is fixed by $\sigma$ and $\sigma^n=\id$, we obtain

$$\sigma(\alpha)=\sigma(x)+\zeta\sigma^2(x)+\cdots+\zeta^{n-1}x=\zeta^{-1}\bigl(\zeta\sigma(x)+\zeta^2\sigma^2(x)+\cdots+\zeta^{n-1}\sigma^{n-1}(x)+x\bigr)=\zeta^{-1}\alpha$$

Therefore, $\sigma(\alpha^n)=\zeta^{-n}\alpha^n=\alpha^n$, and since $\alpha^n$ is fixed by all of $\Gal(\mathbb{L}/\mathbb{K})=\langle\sigma\rangle$, the fact that $\mathbb{L}/\mathbb{K}$ is Galois implies that $\alpha^n\in\mathbb{K}$. ([§Galois Extensions, ⁋Definition 9](/en/math/field_theory/galois_extension#def9){: data-lid="jp7ty" })

Finally, since the $\sigma^i(\alpha)=\zeta^{-i}\alpha$ are $n$ distinct elements, $\alpha$ has, over $\mathbb{K}$, at least $n$ conjugates, and thus $[\mathbb{K}(\alpha):\mathbb{K}]\geq n$. Since $\mathbb{K}(\alpha)\subseteq\mathbb{L}$ and $[\mathbb{L}:\mathbb{K}]=n$, we have $\mathbb{L}=\mathbb{K}(\alpha)$.
:::

## Solvability by Radicals

Now we show that there is no formula for the roots of equations of degree 5 or higher. Here, a formula for the roots means expressing the solutions of an equation using radicals and the four basic arithmetic operations; to formulate this in our language, we define as follows. 

::: Definition 6
A chain of fields

$$\mathbb{K}=\mathbb{K}_0\subseteq\mathbb{K}_1\subseteq\cdots\subseteq\mathbb{K}_r$$

is a *radical tower* if for each $i$, there exist some $\alpha_i\in\mathbb{K}_{i+1}$ and a natural number $n_i\geq1$ such that $\mathbb{K}_{i+1}=\mathbb{K}_i(\alpha_i)$ and $\alpha_i^{n_i}\in\mathbb{K}_i$. A polynomial $f\in\mathbb{K}[\x]$ is *solvable by radicals* if there exists a radical tower such that the splitting field of $f$, $\mathbb{L}_f$, is contained in $\mathbb{K}_r$.
:::

By definition, when passing from $\mathbb{K}_i$ to $\mathbb{K}_{i+1}$, we adjoin, for $\alpha_i^{n_i}\in \mathbb{K}_i$, the element corresponding to its $n_i$-th root, $\alpha_i$. Therefore, that $f$ is solvable by radicals means that all roots of $f$ can be expressed starting from the elements of $\mathbb{K}$ by applying the four basic arithmetic operations and taking roots finitely many times.

Then the following holds.

::: Theorem 7 (Galois)
For a characteristic $0$ field $\mathbb{K}$, a polynomial $f\in\mathbb{K}[\x]$, and the splitting field of $f$, $\mathbb{L}_f$, the following are equivalent.

1. $f$ is solvable by radicals.
2. $\Gal(\mathbb{L}_f/\mathbb{K})$ is a solvable group. ([\[Group Theory\] §Series of Groups, ⁋Definition 11](/en/math/group_theory/series_of_groups#def11){: data-lid="e4s3k" })
:::
::: Proof
First, the splitting field of $f$, $\mathbb{L}_f$, is generated by the finitely many roots of $f$, so it is a finite degree extension. In addition, $\mathbb{L}_f/\mathbb{K}$ is quasi-Galois as a splitting field ([§Galois Extensions, ⁋Proposition 5](/en/math/field_theory/galois_extension#prop5){: data-lid="lm39p" }), and is separable by the assumption of characteristic $0$, so it is a Galois extension.

We first assume the second condition and show the first condition. Suppose that $\Gal(\mathbb{L}_f/\mathbb{K})$ is solvable, and for $n=\lvert\Gal(\mathbb{L}_f/\mathbb{K})\rvert$, choose a primitive $n$-th root of unity $\zeta$, and set $\mathbb{K}'=\mathbb{K}(\zeta)$ and $\mathbb{L}'=\mathbb{L}_f(\zeta)$. Then $\mathbb{L}'$ is the splitting field over $\mathbb{K}'$ of $f$, so $\mathbb{L}'/\mathbb{K}'$ is also a finite degree Galois extension.

Our claim is that $\Gal(\mathbb{L}'/\mathbb{K}')$ is also solvable. For any $\sigma\in\Gal(\mathbb{L}'/\mathbb{K}')$, $\sigma$ fixes $\mathbb{K}$, and since $\mathbb{L}_f/\mathbb{K}$ is quasi-Galois, by the fourth condition of [§Galois Extensions, ⁋Proposition 5](/en/math/field_theory/galois_extension#prop5){: data-lid="1vm97" }, we have $\sigma(\mathbb{L}_f)=\mathbb{L}_f$. Thus the restriction homomorphism 

$$\Gal(\mathbb{L}'/\mathbb{K}') \rightarrow \Gal(\mathbb{L}_f/\mathbb{K});\qquad \sigma\mapsto \sigma\vert_{\mathbb{L}_f}$$

is well-defined. On the other hand, if $\sigma\in\Gal(\mathbb{L}'/\mathbb{K}')$ fixes $\mathbb{L}_f$, it also fixes $\zeta\in\mathbb{K}'$ and hence fixes the whole field $\mathbb{L}'=\mathbb{K}'(\mathbb{L}_f)$. That is, the restriction above is injective, and therefore $\Gal(\mathbb{L}'/\mathbb{K}')$ is isomorphic to a subgroup of the solvable group $\Gal(\mathbb{L}_f/\mathbb{K})$, so it is solvable by [\[Group Theory\] §Series of Groups, ⁋Proposition 13](/en/math/group_theory/series_of_groups#prop13){: data-lid="9iftl" }.

Now, by [\[Group Theory\] §Series of Groups, ⁋Proposition 14](/en/math/group_theory/series_of_groups#prop14){: data-lid="dvshf" }, there exists a series with all quotients cyclic:

$$\Gal(\mathbb{L}'/\mathbb{K}')=H_0\supseteq\cdots\supseteq H_r=\{e\}$$

Here, since $\mathbb{L}'/\mathbb{K}'$ is a finite degree Galois extension, $\Gal(\mathbb{L}'/\mathbb{K}')$ is a discrete group and every subgroup is closed, so by [§Fundamental Theorem of Galois Theory, ⁋Theorem 1](/en/math/field_theory/fundamental_theorem_of_galois_theory#thm1){: data-lid="m85w7" }, there exists a chain of their fixed fields

$$\mathbb{K}'=\mathbb{F}_0\subseteq\mathbb{F}_1\subseteq\cdots\subseteq\mathbb{F}_r=\mathbb{L}',\qquad \mathbb{F}_i=\mathbb{L}'^{H_i}$$

For each $i$, by [§Fundamental Theorem of Galois Theory, ⁋Lemma 7](/en/math/field_theory/fundamental_theorem_of_galois_theory#lem7){: data-lid="3caot" }, $\mathbb{L}'/\mathbb{F}_{i-1}$ is a Galois extension and its Galois group is $H_{i-1}$, and since $H_i$ is a normal subgroup of $H_{i-1}$, by [§Fundamental Theorem of Galois Theory, ⁋Corollary 6](/en/math/field_theory/fundamental_theorem_of_galois_theory#cor6){: data-lid="no8c3" }, $\mathbb{F}_i/\mathbb{F}_{i-1}$ is a Galois extension and

$$\Gal(\mathbb{F}_i/\mathbb{F}_{i-1})\cong H_{i-1}/H_i$$

is a cyclic group. Letting its order be $d_i$, by [\[Algebraic Structures\] §Quotient Groups, ⁋Proposition 5](/en/math/algebraic_structures/quotient_groups#prop5){: data-lid="30g6y" }, $d_i$ divides $\lvert\Gal(\mathbb{L}'/\mathbb{K}')\rvert$, and in turn $\lvert\Gal(\mathbb{L}'/\mathbb{K}')\rvert$ divides $n$. Then, whenever $x^{d_i}=1$, the element $x$ also satisfies $x^n=1$, so $\mu_{d_i}\subseteq\mu_n=\langle\zeta\rangle\subseteq\mathbb{K}'\subseteq\mathbb{F}_{i-1}$, and in particular, a generator of $\mu_{d_i}$, that is, a primitive $d_i$-th root of unity belongs to $\mathbb{F}_{i-1}$. Therefore, by [Proposition 5](#prop5){: data-lid="i7qfu" }, we have $\mathbb{F}_i=\mathbb{F}_{i-1}(\alpha_i)$ with $\alpha_i^{d_i}\in\mathbb{F}_{i-1}$ for some $\alpha_i$. Also, since $\mathbb{F}_0=\mathbb{K}(\zeta)$ and $\zeta^n=1\in\mathbb{K}$, satisfying $\mathbb{L}_f\subseteq\mathbb{L}'$, we obtain a radical tower $\mathbb{K}\subseteq\mathbb{F}_0\subseteq\cdots\subseteq\mathbb{F}_r=\mathbb{L}'$.

Conversely, assume the first condition and show the second condition. Suppose that a radical tower 

$$\mathbb{K}=\mathbb{K}_0\subseteq\cdots\subseteq\mathbb{K}_r$$

satisfies $\mathbb{L}_f\subseteq\mathbb{K}_r$, and is given by $\mathbb{K}_{i+1}=\mathbb{K}_i(\alpha_i)$ with $\alpha_i^{n_i}\in\mathbb{K}_i$. Then, setting $n=n_0n_1\cdots n_{r-1}$, we can choose a primitive $n$-th root of unity $\zeta$.

To translate this into the second condition, we need to transfer this sequence to a sequence of subgroups of the Galois group. For this, we use [§Fundamental Theorem of Galois Theory, ⁋Corollary 6](/en/math/field_theory/fundamental_theorem_of_galois_theory#cor6){: data-lid="k19ue" } and [\[Group Theory\] §Series of Groups, ⁋Proposition 12](/en/math/group_theory/series_of_groups#prop12){: data-lid="yf1pq" }, but as it stands, $\mathbb{K}_r$ need not be a Galois extension of $\mathbb{K}$, each step $\mathbb{K}_{i+1}/\mathbb{K}_i$ need not be Galois either, and even if it were Galois, its Galois group need not be abelian, so we cannot apply them directly in this current state.

To resolve this, first set $\mathbb{E}=\mathbb{K}_r(\zeta)$. Since $\mathbb{E}/\mathbb{K}$ is a finite degree extension, from $\mathbb{E}$ to $\overline{\mathbb{K}}$, there are as many $\mathbb{K}$-homomorphisms as the separable degree $[\mathbb{E}:\mathbb{K}]_s$, and in particular, there are finitely many. ([§Étale Algebras, ⁋Definition 10](/en/math/field_theory/etale_algebras#def10){: data-lid="bnpwu" }) Let these be $u_1=\id,u_2,\ldots,u_s$, and define

$$\mathbb{N}=\mathbb{K}\bigl(u_1(\mathbb{E})\cup\cdots\cup u_s(\mathbb{E})\bigr)$$

On $\overline{\mathbb{K}}$, for any $\mathbb{K}$-automorphism $v$, since the maps $v\circ u_j$ from $\mathbb{E}$ to $\overline{\mathbb{K}}$ are also $\mathbb{K}$-homomorphisms, $v$ permutes the $u_j(\mathbb{E})$, and therefore $v(\mathbb{N})=\mathbb{N}$. That is, by [§Galois Extensions, ⁋Proposition 5](/en/math/field_theory/galois_extension#prop5){: data-lid="v0jwu" }, $\mathbb{N}/\mathbb{K}$ is quasi-Galois, and since the characteristic is $0$, it is a finite degree Galois extension.

Now each $u_j(\mathbb{E})$ is generated over $\mathbb{K}$ by $u_j(\zeta),u_j(\alpha_0),\ldots,u_j(\alpha_{r-1})$, and since $u_j(\zeta)^n=u_j(\zeta^n)=1$, we have $u_j(\zeta)\in\mu_n=\langle\zeta\rangle$. Therefore, $\mathbb{N}$ is obtained from $\mathbb{K}(\zeta)$ by adjoining all elements $u_j(\alpha_i)$. That is, setting $\mathbb{T}_0=\mathbb{K}$ and $\mathbb{T}_1=\mathbb{K}(\zeta)$, if we adjoin them one by one in the order

$$u_1(\alpha_0),\ldots,u_1(\alpha_{r-1}),\quad u_2(\alpha_0),\ldots,u_2(\alpha_{r-1}),\quad\ldots,\quad u_s(\alpha_0),\ldots,u_s(\alpha_{r-1})$$

we obtain the tower

$$\mathbb{K}=\mathbb{T}_0\subseteq\mathbb{T}_1\subseteq\cdots\subseteq\mathbb{T}_{rs+1}=\mathbb{N}$$

Then the element adjoined at each step is a radical. In the first step this is trivial since $\zeta^n=1\in\mathbb{K}$, and for $k\geq1$, if we set $\mathbb{T}_{k+1}=\mathbb{T}_k(u_j(\alpha_i))$, this is because $u_j(\zeta)\in\mathbb{T}_1$ and 

$$u_j(\alpha_i)^{n_i}=u_j(\alpha_i^{n_i})\in u_j(\mathbb{K}_i(\zeta))=\mathbb{K}\bigl(u_j(\zeta),u_j(\alpha_0),\ldots,u_j(\alpha_{i-1})\bigr)\subseteq\mathbb{T}_k$$

hold. Now since $\mathbb{N}/\mathbb{K}$ is Galois, for each $k$, $G_k=\Gal(\mathbb{N}/\mathbb{T}_k)$ is defined ([§Fundamental Theorem of Galois Theory, ⁋Lemma 7](/en/math/field_theory/fundamental_theorem_of_galois_theory#lem7){: data-lid="0tkg8" }), and we obtain a decreasing sequence

$$\Gal(\mathbb{N}/\mathbb{K})=G_0\supseteq G_1\supseteq\cdots\supseteq G_{rs+1}=\{e\}$$

Each step $\mathbb{T}_{k+1}/\mathbb{T}_k$ is an abelian Galois extension. For the first step $\mathbb{K}(\zeta)/\mathbb{K}$, this follows from [Proposition 3](#prop3){: data-lid="39zr0" }, and for $k\geq1$, if $\mathbb{T}_{k+1}=\mathbb{T}_k(u_j(\alpha_i))$, then since $n_i$ divides $n$, we have $\mu_{n_i}\subseteq\mu_n\subseteq\mathbb{T}_1\subseteq\mathbb{T}_k$, so $\mathbb{T}_k$ contains a primitive $n_i$-th root of unity; thus the case $\alpha_i=0$ is trivial, and otherwise $\mathbb{T}_{k+1}/\mathbb{T}_k$ is a cyclic extension by [Proposition 4](#prop4){: data-lid="gfsnj" }. Therefore, by [§Fundamental Theorem of Galois Theory, ⁋Corollary 6](/en/math/field_theory/fundamental_theorem_of_galois_theory#cor6){: data-lid="jn7cx" } and [\[Group Theory\] §Series of Groups, ⁋Proposition 12](/en/math/group_theory/series_of_groups#prop12){: data-lid="ril7l" }, $\Gal(\mathbb{N}/\mathbb{K})$ is a solvable group. Finally, since 

$$\mathbb{L}_f\subseteq\mathbb{K}_r\subseteq\mathbb{E}=u_1(\mathbb{E})\subseteq\mathbb{N}$$

and $\mathbb{L}_f/\mathbb{K}$ is Galois, by [§Galois Extensions, ⁋Proposition 13](/en/math/field_theory/galois_extension#prop13){: data-lid="joes0" } the restriction $\Gal(\mathbb{N}/\mathbb{K}) \rightarrow \Gal(\mathbb{L}_f/\mathbb{K})$ is surjective. That is, $\Gal(\mathbb{L}_f/\mathbb{K})$ is a quotient of a solvable group, and hence is solvable by [\[Group Theory\] §Series of Groups, ⁋Proposition 13](/en/math/group_theory/series_of_groups#prop13){: data-lid="56hfy" }.
:::

Then the fact that there is no formula for the roots of polynomials of degree $5$ or higher now follows, for $n\geq 5$, from the structure of $S_n$.

::: Corollary 8 (Abel–Ruffini)
For general polynomials of degree $5$ or higher, there is no formula for the roots expressible in radicals.
:::
::: Proof
[\[Group Theory\] §Symmetric Groups, ⁋Example 13](/en/math/group_theory/symmetric_groups#ex13){: data-lid="r3hh4" }
:::

---

**References**

**[Bou]** N. Bourbaki. *Algebra II: Chapters 4–7*. Springer, 2003.  
**[Lan]** S. Lang. *Algebra*. Graduate texts in mathematics. Springer, 2002.

---
