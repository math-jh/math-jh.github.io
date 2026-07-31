---
title: "Division Rings"
description: "A division ring is defined as a ring in which every nonzero element is a unit, and it is shown that such a ring has no zero divisors. Wedderburn's little theorem, which states that every finite division ring is a field, is proved using the class equation and cyclotomic polynomials, followed by a direct verification that the quaternions form a noncommutative division ring. Schur's lemma is then presented to show that the endomorphism ring of a simple module is a division ring."
excerpt: "Division rings, quaternions, Wedderburn's little theorem, and Schur's lemma"

categories: [Math / Ring Theory]
permalink: /en/math/ring_theory/division_rings
sidebar: 
    nav: "ring_theory-en"

date: 2026-06-20

weight: 5
translated_at: 2026-07-30T20:45:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-07-30T20:45:02+00:00
---
In this post we study in earnest rings in which every nonzero element has a multiplicative inverse, i.e. *division rings*.

Unless otherwise stated, a ring is always assumed to have an identity $1\neq 0$, and a division ring is *not* assumed to be commutative.

## Division Rings and Zero Divisors

The definition of a division ring has already been given, but we restate it to begin this post. ([[Algebraic Structures] §Field of Fractions, ⁋Definition 3](/en/math/algebraic_structures/field_of_fractions#def3))

::: Definition 1
A ring $D\neq 0$ is called a *division ring* or *skew field* if every nonzero element of $D$ has a two-sided multiplicative inverse. A commutative division ring is called a *field*.
:::

We have already verified in [§Units and Zero Divisors, ⁋Definition 1](/en/math/ring_theory/units_and_zero_divisors#def1) that the unit group $D^\times$ is a group under multiplication, and by definition $D^\times=D\setminus\{0\}$ in a division ring, so this is a group under multiplication. We call this group the *multiplicative group* of $D$.

The first property of a division ring is as follows.

::: Proposition 2
A division ring $D$ has no zero divisors. That is, if $ab=0$ then $a=0$ or $b=0$. In particular, every field is an integral domain.
:::
::: Proof
Let $a,b\in D$ with $ab=0$ and $a\neq 0$. Since $D$ is a division ring, $a$ has an inverse $a^{-1}$, and multiplying both sides on the left by $a^{-1}$ gives

$$b=1\cdot b=(a^{-1}a)b=a^{-1}(ab)=a^{-1}\cdot 0=0$$

Thus if $a\neq 0$ then $b=0$, which means that $a=0$ or $b=0$ whenever $ab=0$. Hence $D$ has no nonzero zero divisors. If $D$ is a field, then it is additionally commutative and $0\neq 1$, so it is an integral domain ([[Algebraic Structures] §Field of Fractions, ⁋Definition 5](/en/math/algebraic_structures/field_of_fractions#def5)).
:::

## Wedderburn's Little Theorem

The above [Proposition 2](#prop2) can in fact be obtained immediately from [§Units and Zero Divisors, ⁋Proposition 4](/en/math/ring_theory/units_and_zero_divisors#prop4), since in a division ring every nonzero element is a unit, so there is no possibility of a nonzero zero divisor existing. However, the converse is not generally true; for instance, $\mathbb{Z}$ is such an example, as we already observed right after the above proposition.

Moreover, in that post we already examined a partial converse of the above [Proposition 2](#prop2), namely that for *finite* rings, an integral domain is always a field. ([§Units and Zero Divisors, ⁋Corollary 6](/en/math/ring_theory/units_and_zero_divisors#cor6)) The proof of this corollary does not essentially use the commutativity of the ring, yet commutativity was assumed in that corollary because there simply do not exist any finite non-commutative zero-divisor-free rings when commutativity is dropped.

To examine this phenomenon, we first organize properties of the center $Z(D)$ of a division ring $D$. This is a commutative subring of $D$ ([[Algebraic Structures] §Definition of a Ring, ⁋Definition 8](/en/math/algebraic_structures/rings#def8)), and moreover it is a field. This is because any nonzero $z\in Z(D)$ has an inverse $z^{-1}$ in $D$, and for any $x\in D$ we have

$$z^{-1}x=z^{-1}xzz^{-1}=z^{-1}zxz^{-1}=xz^{-1}$$

so $z^{-1}\in Z(D)$. Hence if $D$ is finite, then $Z(D)$ is a finite field, and letting $q$ be its number of elements, we have $q\geq 2$.

Still assuming finiteness, if we view $D$ as a vector space over $Z(D)$, then for $n=\dim_{Z(D)} D$ we have $|D|=q^n$. More generally, any sub-division ring $D'$ of $D$ containing $Z(D)$ is also a vector space over $Z(D)$, so its number of elements is of the form $q^d$, and if $D$ is an $m$-dimensional vector space over $D'$ then from $q^n=(q^d)^m$ we obtain $d\mid n$. By a similar reasoning, we need the following cyclotomic polynomial to prove the main result of this section.

::: Definition 3
For a positive integer $n$, the *$n$th cyclotomic polynomial* $\Phi_n(\x)$ is defined by

$$\Phi_n(\x)=\prod_{\substack{1\leq m\leq n\\ \gcd(m,n)=1}}\bigl(\x-\zeta^m\bigr),\qquad \zeta=e^{2\pi i/n}$$

That is, $\Phi_n(\x)$ is the monic polynomial whose roots are the primitive $n$th roots of unity.
:::

We use two basic properties of cyclotomic polynomials. First, every root of $\x^n-1$ is a primitive $d$th root of unity for some $d\mid n$, so

$$\x^n-1=\prod_{d\mid n}\Phi_d(\x)$$

holds, and therefore by performing the division from [§Polynomial Rings, ⁋Proposition 5](/en/math/ring_theory/polynomial_rings#prop5) inside $\mathbb{Z}[\x]$, we inductively know that each $\Phi_d(\x)$ has integer coefficients. Second, for a proper divisor $d$ of $n$,

$$\x^n-1=(\x^d-1)\cdot\prod_{e\mid n\text{ but }e\nmid d}\Phi_e(\x)$$

contains the factor $\Phi_n(\x)$ on the right-hand side, so $\Phi_n(\x)$ divides $(\x^n-1)/(\x^d-1)$ in $\mathbb{Z}[\x]$. In particular, substituting an integer $q$ into these integer polynomials, we know that $\Phi_n(q)$ divides both $q^n-1$ and $(q^n-1)/(q^d-1)$ as integers.

Finally, we isolate one analytic inequality that we will need.

::: Proposition 4
For integers $q\geq 2$ and $n\geq 2$, we have $|\Phi_n(q)|>q-1$.
:::
::: Proof
Substituting $q$ into the cyclotomic polynomial, by [Definition 3](#def3) we have

$$\Phi_n(q)=\prod_{\substack{1\leq m\leq n\\ \gcd(m,n)=1}}(q-\zeta^m)$$

We estimate the absolute value of each factor from below. Writing $\zeta=\cos\theta+i\sin\theta$ ($\theta\neq 0$), we have

$$|q-\zeta^m|^2=(q-\cos m\theta)^2+\sin^2 m\theta=q^2-2q\cos m\theta+1$$

and therefore

$$|q-\zeta^m|^2-(q-1)^2=q^2-2q\cos m\theta+1-(q^2-2q+1)=2q(1-\cos m\theta)\geq 0$$

For every primitive root $\zeta^m$ we have $|q-\zeta^m|\geq q-1\geq 1$, and in particular

$$|\Phi_n(q)|=\prod_{\substack{1\leq m\leq n\\ \gcd(m,n)=1}}|q-\zeta^m|\geq|q-\zeta|\geq q-1$$

For the last inequality, using $\zeta\neq 1$, i.e. $\cos\theta\neq 1$, this inequality is strict, and we obtain the strict inequality of the proposition.
:::

We now prove the theorem.

::: Theorem 5 (Wedderburn)
Every finite division ring is a field. That is, every finite division ring is commutative.
:::
::: Proof
Let $D$ be a finite division ring and $Z=Z(D)$ its center. As we saw above, $Z$ is a finite field; letting $q\geq 2$ be its number of elements, $D$ is a finite-dimensional vector space over $Z$ with $|D|=q^n$ elements. Our claim is that $n=1$, so that $D=Z$ is commutative.

To this end, we write the class equation of the multiplicative group $D^\times=D\setminus\{0\}$. ([[Algebraic Structures] §Group Actions, ⁋Theorem 14](/en/math/algebraic_structures/group_actions#thm14)) The class equation of $D^\times$ for the conjugation action from [[Algebraic Structures] §Group Actions, ⁋Proposition 9](/en/math/algebraic_structures/group_actions#prop9) is

$$|D^\times|=|Z(D^\times)|+\sum_{x}\bigl[D^\times:C_{D^\times}(x)\bigr]$$

where $C_{D^\times}(x)$ is the centralizer of $x$ defined right after [[Algebraic Structures] §Group Actions, ⁋Definition 12](/en/math/algebraic_structures/group_actions#def12), and the sum is over all representatives not belonging to $Z(D^\times)$. Also, since $Z(D^\times)=Z^\times=Z\setminus\{0\}$, we have $|Z(D^\times)|=q-1$.

Now for each $x\in D^\times$, the set $C_D(x)=\{y\in D\mid xy=yx\}$ is a sub-division ring of $D$ containing $Z$. In this case we have seen that $C_D(x)$ is a $Z$-vector space, and since $|Z|=q$, we have $|C_D(x)|=q^{d(x)}$ for some $d(x)$. Also, since $D$ is a vector space over $C_D(x)$, we have $d(x)\mid n$. Since $C_{D^\times}(x)=C_D(x)\setminus\{0\}$, we have

$$\bigl[D^\times:C_{D^\times}(x)\bigr]=\frac{q^n-1}{q^{d(x)}-1}$$

and for this to be an integer we must have $d(x)\mid n$. If $x$ is not in the center, then $C_D(x)\neq D$, so $d(x)<n$. Hence the class equation takes the form

$$q^n-1=(q-1)+\sum_{x}\frac{q^n-1}{q^{d(x)}-1}\tag{$\ast$}$$

where each $d(x)$ in the sum is a proper divisor of $n$.

Now assume $n\geq 2$ and derive a contradiction. The cyclotomic polynomial $\Phi_n(\x)$ divides $q^n-1$, and for each proper divisor $d=d(x)<n$, it also divides $\frac{q^n-1}{q^d-1}$. Therefore, from $(\ast)$ above, $\Phi_n(q)$ must also divide $q-1$. That is, $\Phi_n(q)\mid q-1$ and $q-1\geq 1$, so $|\Phi_n(q)|\leq q-1$. However, by [Proposition 4](#prop4), if $n\geq 2$ then $|\Phi_n(q)|>q-1$, a contradiction.
:::

The first consequence of this theorem is to reconfirm the result about finite integral domains.

::: Corollary 6
Let $A$ be a finite ring with $0\neq 1$. If $A$ has no nonzero zero-divisors, then $A$ is a field.
:::
::: Proof
Let $A$ be a finite ring with no zero divisors other than $0$. For any nonzero $a\in A$, consider the left multiplication morphism $\lambda_a:A\rightarrow A$, $\lambda_a(x)=ax$. If $ax=ay$, then $a(x-y)=0$, and since $a$ is not a zero divisor, $x=y$, i.e. $\lambda_a$ is injective. Since $A$ is finite, $\lambda_a$ is surjective, and there exists $v$ with $av=1$. Applying the same argument to right multiplication, there exists $w$ with $wa=1$, and $w=w(av)=(wa)v=v$, so $v$ is a two-sided inverse of $a$. Thus every nonzero element is a unit and $A$ is a division ring. A finite division ring is a field by [Theorem 5](#thm5).
:::

What makes this essentially different from [§Units and Zero Divisors, ⁋Corollary 6](/en/math/ring_theory/units_and_zero_divisors#cor6) is that we do not assume the commutativity of $A$. If we had assumed commutativity from the outset, then [Theorem 5](#thm5) would not have been needed to prove this corollary. The power of this theorem lies in achieving the same result using only finiteness, without commutativity.

## Quaternions

By [Theorem 5](#thm5), a non-commutative division ring must necessarily be infinite, so we must look for examples among infinite rings. The most classical one is the space of *quaternions* defined by Hamilton, which is a 4-dimensional vector space over the real field $\mathbb{R}$ equipped with a multiplication.

::: Definition 7
The *quaternion algebra* $\mathbb{H}$ is the 4-dimensional vector space over $\mathbb{R}$ with basis $1,i,j,k$, whose elements are of the form

$$q=a+bi+cj+dk\qquad(a,b,c,d\in\mathbb{R})$$

and whose multiplication is defined by extending $\mathbb{R}$-bilinearly from the identity $1$ and the relations

$$i^2=j^2=k^2=-1,\qquad ij=k,\quad jk=i,\quad ki=j,\qquad ji=-k,\quad kj=-i,\quad ik=-j$$

on the basis elements.
:::

That this multiplication is associative does not follow merely from extending the relations bilinearly, so this must be checked separately. The simplest method is to realize $\mathbb{H}$ inside the ring of $2\times 2$ complex matrices $\Mat_2(\mathbb{C})$. For a given quaternion $q=a+bi+cj+dk$, set $z=a+bi$, $w=c+di$ and define the $\mathbb{R}$-linear map $\varphi:\mathbb{H}\rightarrow\Mat_2(\mathbb{C})$ by

$$\varphi(q)=\begin{pmatrix}z&w\\ -\bar w&\bar z\end{pmatrix}$$

Then the images of the basis elements are

$$\varphi(1)=I,\qquad\varphi(i)=\begin{pmatrix}i&0\\ 0&-i\end{pmatrix},\qquad\varphi(j)=\begin{pmatrix}0&1\\ -1&0\end{pmatrix},\qquad\varphi(k)=\begin{pmatrix}0&i\\ i&0\end{pmatrix}$$

and that these four matrices satisfy all the relations of [Definition 7](#def7) is verified by direct computation. Since both sides are bilinear in $q,q'$, it follows that $\varphi(qq')=\varphi(q)\varphi(q')$ for all quaternions, and since the four matrices above are linearly independent over $\mathbb{R}$, $\varphi$ is injective. Thus the associativity of multiplication in $\Mat_2(\mathbb{C})$ carries over to $\mathbb{H}$, and $\mathbb{H}$ becomes a ring isomorphic to the subring $\varphi(\mathbb{H})\subseteq\Mat_2(\mathbb{C})$. On the other hand, the determinant of this matrix

$$|z|^2+|w|^2=a^2+b^2+c^2+d^2$$

defines the norm of the quaternion.

::: Definition 8
For a quaternion $q=a+bi+cj+dk$, its *conjugate* is defined by

$$\bar q=a-bi-cj-dk$$

and its *norm* is defined by

$$N(q)=q\bar q$$
:::

For any quaternion $q=a+bi+cj+dk$, multiplying by the conjugate $\bar q$ indeed yields, by the relations of [Definition 7](#def7), cancellation of all coefficients of the $i,j,k$ terms, giving

$$N(q)=q\bar q=a^2+b^2+c^2+d^2\in\mathbb{R}$$

In particular, $N(q)=0$ is equivalent to $a=b=c=d=0$, i.e. $q=0$.

Another property of the norm is that it preserves multiplication. Indeed, it is easily verified that the conjugate satisfies $\overline{q_1q_2}=\bar q_2\bar q_1$, and using this we obtain

$$N(q_1q_2)=q_1q_2\overline{q_1q_2}=q_1q_2\bar q_2\bar q_1=q_1N(q_2)\bar q_1=N(q_2)q_1\bar q_1=N(q_1)N(q_2)$$

Writing this multiplicativity in coordinates gives

$$(a_1^2+b_1^2+c_1^2+d_1^2)(a_2^2+b_2^2+c_2^2+d_2^2)=(\cdots)^2+(\cdots)^2+(\cdots)^2+(\cdots)^2$$

which is Euler's [four-square identity](https://en.wikipedia.org/wiki/Euler%27s_four-square_identity). In any case, what is important for us is that we can use this to prove that $\mathbb{H}$ is a division ring.

::: Proposition 9
The quaternion algebra $\mathbb{H}$ is a noncommutative division ring.
:::
::: Proof
That $\mathbb{H}$ is a ring with $1\neq 0$ was verified above, and its noncommutativity is obvious from $ij=k\neq -k=ji$. It remains to show that every nonzero $q\in\mathbb{H}$ has a two-sided multiplicative inverse.

Let $q=a+bi+cj+dk\neq 0$. We have seen above that $N(q)=a^2+b^2+c^2+d^2$ is a positive real number. This can be viewed as an element of $\mathbb{H}$, and moreover it commutes with every element of $\mathbb{H}$. The same holds for the inverse $N(q)^{-1}$ of $N(q)$, and therefore

$$q\cdot\bigl(N(q)^{-1}\bar q\bigr)=N(q)^{-1}(q\bar q)=N(q)^{-1}N(q)=1$$

and similarly

$$\bigl(N(q)^{-1}\bar q\bigr)\cdot q=N(q)^{-1}(\bar q q)=N(q)^{-1}N(q)=1$$

can be verified. That is, $q^{-1}=N(q)^{-1}\bar q$ is a two-sided inverse of $q$, yielding the desired claim.
:::

## Endomorphism Rings of Simple Modules

Division rings are useful when dealing with endomorphisms of modules. A nonzero module $M$ over a ring $A$ is called a *simple module* if $M$ has no submodules other than $0$ and itself. For convenience we fix $M$ as a left module. Then the following holds.

::: Lemma 10 (Schur)
For simple modules $M,N$ over a ring $A$, the following hold.

1. Any $A$-module homomorphism $f:M\rightarrow N$ is either the zero map or an isomorphism.
2. In particular, the endomorphism ring $\End_A(M)$ of a simple module $M$ is a division ring.
:::
::: Proof
Let $f:M\rightarrow N$ be a nonzero $A$-module homomorphism. The kernel $\ker f$ is a submodule of $M$, and since $f\neq 0$, we have $\ker f\neq M$. Since $M$ is simple, $\ker f=0$, i.e. $f$ is injective. Also $\im f$ is a nonzero submodule of $N$, and since $N$ is simple, $\im f=N$, i.e. $f$ is surjective. Hence $f$ is an isomorphism. This establishes the first result.

Now consider the case $M=N$. Then $\End_A(M)$ is a ring with composition of morphisms as multiplication and the identity map $\id_M$ as identity. Since $M$ is nonzero, $\id_M\neq 0$, i.e. this ring is not zero. By the first result, any nonzero $f\in\End_A(M)$ is an isomorphism, and its inverse $f^{-1}$ is also an $A$-module homomorphism, hence an element of $\End_A(M)$. Moreover $f\circ f^{-1}=f^{-1}\circ f=\id_M$, so $f$ is a unit. That is, every nonzero element is a unit, and $\End_A(M)$ is a division ring.
:::

This lemma supplies division rings in abundance in the form of endomorphism rings of simple modules. Conversely, viewing a division ring itself as a vector space over a smaller field, it is represented by matrices inside the ring of linear endomorphisms over that field, and the matrix representation of the quaternions $\mathbb{H}$ written by hand right after [Definition 7](#def7) is also obtained in this way. Considering the subfield $\mathbb{C}=\mathbb{R}+\mathbb{R}i$ of $\mathbb{H}$ and viewing $\mathbb{H}$ as a $\mathbb{C}$-vector space by left multiplication, a quaternion $q=a+bi+cj+dk$ can be written uniquely as

$$q=z+wj$$

for $z=a+bi$, $w=c+di$, so $\{1,j\}$ is a basis of this vector space and $\dim_{\mathbb{C}}\mathbb{H}=2$. Now considering right multiplication $\rho_q(x)=xq$ for each $q\in\mathbb{H}$, we have

$$\rho_q(ux)=uxq=u\rho_q(x)\qquad(u\in\mathbb{C})$$

so $\rho_q$ is a $\mathbb{C}$-linear map, i.e. an element of $\End_{\mathbb{C}}(\mathbb{H})$, and if $\rho_q=0$ then $q=\rho_q(1)=0$, so $q\mapsto\rho_q$ is injective. By associativity, $\rho_{qq'}=\rho_{q'}\circ\rho_q$, so this correspondence reverses the order of multiplication, but if we write coordinates as row vectors and represent a $\mathbb{C}$-linear map by a matrix $M_q$ acting by right multiplication, the order is reversed once more, so

$$\mathbb{H}\rightarrow\Mat_2(\mathbb{C});\quad q\mapsto M_q$$

is an injective ring homomorphism. Here the two rows of $M_q$ are the coordinates of $\rho_q(1)$ and $\rho_q(j)$, and using from the relations of [Definition 7](#def7) that $ji=-ij$, so that $ju=\bar uj$ holds for any $u\in\mathbb{C}$, we obtain from $\rho_q(1)=q=z+wj$ and

$$\rho_q(j)=jq=jz+jwj=\bar zj+\bar wj^2=-\bar w+\bar zj$$

that

$$M_q=\begin{pmatrix}z&w\\ -\bar w&\bar z\end{pmatrix}$$

This is the matrix representation written above, and its determinant $|z|^2+|w|^2$ is precisely the norm $N(q)$, so the fact that $M_q$ is invertible for nonzero $q$ is the same content as what [Proposition 9](#prop9) showed.

---

**References**

**[DF]** D. S. Dummit and R. M. Foote, *Abstract algebra*, 3rd ed., Wiley, 2004.  
**[Her]** I. N. Herstein, *Noncommutative rings*, Carus Mathematical Monographs 15, Mathematical Association of America, 1968.  
**[Lam]** T. Y. Lam, *A first course in noncommutative rings*, 2nd ed., Graduate Texts in Mathematics 131, Springer, 2001.
