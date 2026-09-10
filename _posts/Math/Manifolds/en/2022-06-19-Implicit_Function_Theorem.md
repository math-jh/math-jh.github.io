---
title: "Implicit Function Theorem"
description: "This post discusses the implicit function theorem extended to smooth manifolds. It proves that immersed submanifolds are locally embedded and derives the submersion level set theorem."
excerpt: "Implicit function theorem on smooth manifolds and its consequences"

categories: [Math / Manifolds]
permalink: /en/math/manifolds/implicit_function_theorem
sidebar: 
    nav: "manifolds-en"

date: 2022-06-19
weight: 9
translated_at: 2026-09-06T07:15:05+00:00
translation_source: antigravity-gemini-3.8-flash-high
---
First, we define the following.

::: Definition 1
Let a manifold $M$ and a coordinate system $(U,\varphi)$ be given. Let $\varphi=(x^i)_{i=1}^m$, let $0\leq k\leq m$, and for $p\in \varphi(U)$, the manifold given by the set

$$S=\{q\in U\mid x^i(q)=r^i(p), k+1\leq i\leq m\}$$

endowed with the subspace topology and the coordinate system $(S, (x^j\vert_S)_{j=1}^k)$ is called a *slice* of $(U,\varphi)$.
:::

::: Lemma 2
Let an immersion $F:M\rightarrow N$ between two manifolds be given. Then for each $p\in M$, there exist a coordinate system $(V,\varphi)$ containing $F(p)$ and an open neighborhood $U$ of $p$ such that $F\vert_U$ is injective and $F(U)$ is a slice of $(V,\varphi)$.
:::
::: Proof
Let $\dim M=k$ and $\dim N=n$. Choose, containing $F(p)$, a coordinate system $(V_0,\psi)$, $\psi=(y^i)_{i=1}^n$. Since $\dd{F_p}$ is injective, by [§Submanifolds and the Inverse Function Theorem, ⁋Corollary 10](/en/math/manifolds/submanifolds#cor10){: data-relation="required" }, a suitable subset of the set $\{y^i\circ F\}$ forms, near the point $p$, a coordinate system for $M$. Rearranging the order of coordinates, we may assume that $x^j=y^j\circ F$ ($j=1,\ldots,k$) form, on a suitable open neighborhood of $p$, denoted $U_1$, a coordinate system $(U_1,x)$, $x=(x^j)_{j=1}^k$. Shrinking $U_1$ if necessary, we may assume $F(U_1)\subseteq V_0$.

First, $F\vert_{U_1}$ is injective. If $q,q'\in U_1$ satisfy $F(q)=F(q')$, then for each $j\leq k$ we have $x^j(q)=y^j(F(q))=y^j(F(q'))=x^j(q')$, because $x$ is injective on $U_1$.

Now on $U_1$, let us express $F$ in coordinates. For $j\leq k$, since $y^j\circ F=x^j$, the map $\psi\circ F\circ x^{-1}:x(U_1) \rightarrow \mathbb{R}^n$ has the identity as its first $k$ components; thus there exist $C^\infty$ functions $h^i:x(U_1) \rightarrow \mathbb{R}$ ($i=k+1,\ldots,n$) such that for every $q\in U_1$,

$$\psi(F(q))=\bigl(x^1(q),\ldots,x^k(q),h^{k+1}(x(q)),\ldots,h^n(x(q))\bigr)$$

holds. That is, $F(U_1)$ is, in $\psi$-coordinates, the graph of the function $h=(h^{k+1},\ldots,h^n)$.

Now consider the open subset of $V_0$

$$V'=\left\{q'\in V_0\mid (y^1(q'),\ldots,y^k(q'))\in x(U_1)\right\}$$

then $F(p)\in V'$. On $V'$, define new functions by

$$w^j=y^j\quad (j=1,\ldots,k),\qquad w^i=y^i-h^i(y^1,\ldots,y^k)\quad (i=k+1,\ldots,n)$$

Then at the point $F(p)$,

$$\dd{w}^j=\dd{y}^j\quad(j\leq k),\qquad \dd{w}^i=\dd{y}^i-\sum_{j=1}^k\frac{\partial h^i}{\partial y^j}\dd{y}^j\quad(i>k)$$

so the $\dd{w}^i$ are obtained from the basis $\dd{y}^i$ via a triangular matrix transformation whose diagonal entries are all $1$, and thus are linearly independent. Therefore, by [§Submanifolds and the Inverse Function Theorem, ⁋Corollary 6](/en/math/manifolds/submanifolds#cor6){: data-relation="required" }, on a suitable open neighborhood of $F(p)$, $V\subseteq V'$, $\varphi=(w^1,\ldots,w^n)$ becomes a coordinate system.

Finally, let $U=U_1\cap F^{-1}(V)$. For any $q\in U$ and $i>k$,

$$w^i(F(q))=y^i(F(q))-h^i(x(q))=h^i(x(q))-h^i(x(q))=0$$

Conversely, suppose that $q'\in V$ satisfies, for all $i>k$, that $w^i(q')=0$. Setting $b=(y^1(q'),\ldots,y^k(q'))$, we have $b\in x(U_1)$, and since the point $F(x^{-1}(b))$ has $\psi$-coordinates $(b,h(b))$, which coincide with the coordinates of $q'$ in $\psi$, we have $q'=F(x^{-1}(b))$. In particular, since $q'\in V$, we have $x^{-1}(b)\in U_1\cap F^{-1}(V)=U$, that is, $q'\in F(U)$. In summary,

$$F(U)=\left\{q'\in V\mid \text{$w^i(q')=w^i(F(p))=0$ for $i=k+1,\ldots,n$}\right\}$$

and therefore $F(U)$ is a slice of $(V,\varphi)$.
:::

In the lemma above, it is worth noting that for an open set of $M$, say $U$, $F(U)$ becomes a slice of $(V,\varphi)$. For example, $F(M)\cap V$ does not in general have to be a slice, and this remains true even when $F$ is a submanifold.

{% diagram Math/Manifolds/Implicit_Function_Theorem-1.png width="200px" alt="counterexample" %}

However, if $F$ were an embedding, we could choose $(V,\varphi)$ appropriately so that $F(M)\cap V$ is a slice of $V$. From this perspective, we can summarize the above lemma roughly as

> An immersed submanifold is locally embedded.

## Implicit Function Theorem and Its Consequences

We are now ready to extend the implicit function theorem to differentiable manifolds.

::: Theorem 3 (Implicit function theorem)
Let $U\subseteq\mathbb{R}^{m-n}\times\mathbb{R}^n$ be an open subset, and for distinction, let the coordinates of $\mathbb{R}^{m-n}$ be $s^1,\ldots, s^{m-n}$, and the coordinates of $\mathbb{R}^n$ be $r^1,\ldots, r^n$. Also, let $f:U\rightarrow\mathbb{R}^n$ be $C^\infty$, and suppose that for some point $(s_0,r_0)\in U$, we have $f(s_0,r_0)=0$. If at the point $(s_0,r_0)$, the Jacobian matrix

$$\begin{pmatrix}\partial f^1/\partial s^1&\partial f^1/\partial s^2&\cdots&\partial f^1/\partial s^{m-n}&\partial f^1/\partial r^1&\partial f^1/\partial r^2&\cdots&\partial f^1/\partial r^n\\\partial f^2/\partial s^1&\partial f^2/\partial s^2&\cdots&\partial f^2/\partial s^{m-n}&\partial f^2/\partial r^1&\partial f^2/\partial r^2&\cdots&\partial f^2/\partial r^n\\ \vdots&\vdots&\ddots&\vdots&\vdots&\vdots&\ddots&\vdots\\\partial f^n/\partial s^1&\partial f^n/\partial s^2&\cdots&\partial f^n/\partial s^{m-n}&\partial f^n/\partial r^1&\partial f^n/\partial r^2&\cdots&\partial f^n/\partial r^n\end{pmatrix}$$

has the property that its $n\times n$ submatrix

$$\begin{pmatrix}\partial f^1/\partial r^1&\partial f^1/\partial r^2&\cdots&\partial f^1/\partial r^n\\\partial f^2/\partial r^1&\partial f^2/\partial r^2&\cdots&\partial f^2/\partial r^n\\\vdots&\vdots&\ddots&\vdots\\\partial f^n/\partial r^1&\partial f^n/\partial r^2&\cdots&\partial f^n/\partial r^n\end{pmatrix}$$

is nonsingular, then there exist an open neighborhood of $s_0$, denoted $V$, an open neighborhood of $r_0$, denoted $W$, and a $C^\infty$ function $g:V\rightarrow W$ such that $V\times W\subseteq U$, and for each $(p,q)\in V\times W$,

$$f(p,q)=0\iff q=g(p)$$

is satisfied.
:::

::: Corollary 4 (Submersion level set theorem)
Let $F:M\rightarrow N$ be $C^\infty$, fix $q\in F(M)$, and let $P=F^{-1}(q)$. If for every $p\in P$, the differential $\dd{F_p}:T_pM\rightarrow T_{F(p)}N$ is surjective, then there exists a unique manifold structure defined on $P$ such that the canonical injection $\iota:P\hookrightarrow M$ is a submanifold.

Moreover, in this case $\iota$ is an embedding, and the codimension of $P$, $\dim M-\dim P$, is equal to $\dim N$."
:::
::: Proof
Let $\dim M=m$ and $\dim N=n$. Fix an arbitrary $p\in P$, and choose a coordinate system $(Y,\psi)$, $\psi=(y^j)_{j=1}^n$ containing $q=F(p)$ such that $\psi(q)=0$. Since $\dd{F_p}$ is surjective, by [§Submanifolds and the Inverse Function Theorem, ⁋Corollary 9](/en/math/manifolds/submanifolds#cor9){: data-relation="required" }, there exist functions $x^{n+1},\ldots,x^m$ such that

$$x^1=y^1\circ F,\quad\ldots,\quad x^n=y^n\circ F,\qquad x^{n+1},\quad\ldots,\quad x^m$$

form, on a suitable open neighborhood of $p$, denoted $W$, a coordinate system. Shrinking $W$ if necessary, we may assume $F(W)\subseteq Y$. Then for $w\in W$, having $F(w)=q$ is equivalent, since $\psi$ is injective, to $y^j(F(w))=0$ holding for all $j\leq n$, and therefore

$$P\cap W=\left\{w\in W\mid x^1(w)=\cdots=x^n(w)=0\right\}$$

That is, rearranging the order of coordinates, $P\cap W$ is a slice of the coordinate system $(W,(x^i)_{i=1}^m)$.

Now endow $P$ with the subspace topology of $M$, and to each slice obtained above, assign the function

$$\varphi_p=(x^{n+1},\ldots,x^m)\big\vert_{P\cap W}$$

Since $x=(x^i)_{i=1}^m$ is a homeomorphism from $W$ to the open subset $x(W)\subseteq\mathbb{R}^m$, $\varphi_p$ is a homeomorphism from $P\cap W$ to the open subset $\{a\in\mathbb{R}^{m-n}\mid (0,a)\in x(W)\}$. Moreover, the transition between two charts $(P\cap W,\varphi_p)$ and $(P\cap W',\varphi_{p'})$ is given by

$$\varphi_{p'}\circ\varphi_p^{-1}:a\mapsto \bigl(\text{$x'\circ x^{-1}(0,a)$의 마지막 $m-n$개의 성분}\bigr)$$

which, between two coordinate systems of $M$, is the composition and restriction of $C^\infty$ transition functions, and thus is $C^\infty$. Since $P$ is Hausdorff and second countable as a subspace of $M$, these charts make $P$ into an $(m-n)$-dimensional manifold.

With respect to this structure, $\iota:P\hookrightarrow M$ is of the form $a\mapsto(0,a)$ in coordinates and thus is $C^\infty$, and $\dd{\iota}$ is injective at every point. That is, $\iota$ is an injective immersion and therefore a submanifold, and since $P$ was endowed with the subspace topology from the beginning, it is an embedding. Counting dimensions, the codimension of $P$ is $\dim M-\dim P=m-(m-n)=n=\dim N$.

Finally, the uniqueness of this manifold structure follows from [§Uniqueness of Submanifolds, ⁋Proposition 5](/en/math/manifolds/uniqueness_of_submanifold#prop5){: data-relation="required" }. This is because $(P,\iota)$ has a differential structure that makes it a submanifold of $M$ with respect to the subspace topology, and this structure is the unique manifold structure making $(P,\iota)$ a submanifold of $M$.
:::

The following corollary does not require $\dd{F_p}$ to be surjective, but only that its rank is constant, so it can be used even when the preceding corollary does not apply.

::: Corollary 5 (Constant-rank level set theorem)
Let $F:M\rightarrow N$ be $C^\infty$, and suppose that $\dd{F_p}:T_pM\rightarrow T_{F(p)}N$ has the same rank $r$ at every point $p\in M$. Fixing $q\in F(M)$ and letting $P=F^{-1}(q)$, there exists a unique manifold structure defined on $P$ such that the canonical injection $\iota:P\hookrightarrow M$ is a submanifold.

Moreover, in this case $\iota$ is an embedding, and the codimension of $P$, $\dim M-\dim P$, is equal to $r$.
:::

Using these theorems, we can show that a particular subset of a given manifold $M$ is an embedded submanifold, which typically follows an argument such as the following.

::: Example 6
Consider the function from $\mathbb{R}^{n+1}$ to $\mathbb{R}$ given by

$$f(x)=\lvert x\rvert^2=\sum_{i=1}^{n+1} r^i(x)^2$$

For any point $x\in \mathbb{R}^{n+1}$ and $v\in T_x\mathbb{R}^{n+1}$,

$$\dd{f_x}(v)=v(f)=\sum v^i\frac{\partial f}{\partial r^i}\bigg\vert_{x}=2\sum r^i(x) v^i$$

holds, from which we see that as long as $x$ is not the origin, by adjusting $v$ we can make $\dd{f_x}(v)$ take any real value. That is, since $\dd{f_x}$ is always surjective away from the origin, there exists a unique manifold structure such that $f^{-1}(1)$ is a submanifold of $\mathbb{R}^{n+1}$. By uniqueness, this structure coincides with the manifold structure given to $S^n$, and by [Corollary 4](#cor4){: data-relation="required" } again, we see that this is an embedded submanifold of $\mathbb{R}^{n+1}$.
:::

---

**References**

**[War]** Frank W. Warner. *Foundations of Differentiable Manifolds and Lie Groups*, Graduate texts in mathematics, Springer, 2013  
**[Lee]** John M. Lee. *Introduction to Smooth Manifolds*, Graduate texts in mathematics, Springer, 2012

---
