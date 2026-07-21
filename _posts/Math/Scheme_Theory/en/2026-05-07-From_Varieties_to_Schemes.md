---
title: "From Varieties to Schemes"
description: "We examine the limitations of classical algebraic varieties, particularly their inability to capture intersection multiplicities and nilpotent information, and explain how Grothendieck's theory of schemes naturally extends this framework."
excerpt: "From varieties to schemes"
categories: [Math / Scheme Theory]
permalink: /en/math/scheme_theory/from_varieties_to_schemes
sidebar: 
    nav: "scheme_theory-en"
date: 2026-05-07
weight: 1
translated_at: 2026-07-12T00:30:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-07-12T00:30:02+00:00
---
## Algebraic Varieties

In the posts on [algebraic varieties](/en/algebraic_varieties/), we have followed the classical framework of algebraic geometry. That is, affine varieties defined as subsets of affine space $\mathbb{A}_\mathbb{K}^n$ over an algebraically closed field $\mathbb{K}$, and projective varieties obtained by gluing these together, have yielded rich results in many directions. In particular, the correspondence between the coordinate ring of a variety and the ideal it defines ([\[Algebraic Varieties\] §Affine Varieties, ⁋Proposition 18](/en/math/algebraic_varieties/affine_varieties#prop18)) is a representative example showing the deep connection between geometry and algebra.

A scheme is a systematically constructed space designed to overcome what these varieties miss. Before developing scheme theory, this post aims to grasp the big picture by examining in what dimensions it extends varieties and what new geometric intuition it provides.

To this end, let us briefly recall the setting in algebraic varieties. The objects we start from are the *affine variety* of [\[Algebraic Varieties\] §Affine Varieties, ⁋Definition 2](/en/math/algebraic_varieties/affine_varieties#def2) and the *projective variety* of [\[Algebraic Varieties\] §Projective Varieties, ⁋Definition 3](/en/math/algebraic_varieties/projective_varieties#def3), which were defined as irreducible algebraic subsets of affine space $\mathbb{A}_\mathbb{K}^n$ and projective space $\mathbb{P}_\mathbb{K}^n$ over an algebraically closed field $\mathbb{K}$, respectively. More importantly, they could be understood as locally ringed spaces $(V,\mathcal{O}_V)$ equipped with the sheaf $\mathcal{O}_V$ of regular functions defined on them.

In this world, every point was a closed point. That is, a point on $\mathbb{A}_\mathbb{K}^2$ was completely determined by the maximal ideal $(\x-a, \y-b)\subseteq \mathbb{K}[\x,\y]$ corresponding to the coordinates $(a,b)\in \mathbb{K}^2$. This may be intuitively plausible from a geometric perspective, but it is not a very favorable environment for developing theory; for example, if we consider the line $V(\y)$ and the parabola $V(\y-\x^2)$ on $\mathbb{A}_\mathbb{K}^2$, the fact that they meet at the point $(0,0)$ is clearly visible in classical algebraic varieties, but the fact that the intersection multiplicity is not $1$ is completely invisible.

::: Example 1
Let us see how schemes capture the degree of such an intersection. First, consider the case where the intersection has multiplicity $1$: the intersection of the two curves $V(\y-\x)$ and $V(\y)$ on $\mathbb{A}_\mathbb{K}^2$. From the classical algebraic variety perspective, this is indistinguishable from the situation examined above. That is, these two lines meet at a single point $V(\x,\y)=\{(0,0)\}$.

To see how this intersection differs from the example above, we look at the ideals defining them. Namely,

$$(\y-\x)+(\y)=(\x,\y),\qquad (\y-\x^2)+(\y)=(\x^2,\y)$$

so, unlike the first case, in the second case there remains a nilpotent element $\bar{\x}$ in the coordinate ring $\mathbb{K}[\x,\y]$ of $\mathbb{A}_\mathbb{K}^2$. In fact,

$$\frac{\mathbb{K}[\x,\y]}{(\x^2,\y)} \cong \frac{\mathbb{K}[\epsilon]}{(\epsilon^2)}$$

holds, and the dimension of this ring as a $\mathbb{K}$-vector space is $2$. This dimension is precisely the core of the scheme-theoretic intersection, which reflects the intersection multiplicity as a coefficient.
:::

This was in fact anticipated to some extent from [\[Algebraic Varieties\] §Affine Varieties, ⁋Theorem 10](/en/math/algebraic_varieties/affine_varieties#thm10), because points of a classical variety are defined only by radical ideals, so all nilpotent elements are discarded, and as a result all infinitesimal information must be lost. The key idea of schemes is to preserve all this discarded information exactly as it is.

::: Example 2
Consider the ring $\mathbb{K}[\epsilon]/(\epsilon^2)$ examined above. This ring has a single prime ideal $(\epsilon)$, so in classical algebraic geometry this space looks like a space consisting of a single point, and this is indeed the same in the world of schemes.

What is crucially different is that in the world of schemes, the functions defined on this space are more refined. To see this refinement properly, we must understand this space not as a single point but as a point with a <em>tangent direction</em> attached to it. That is, $\Spec \mathbb{K}[\epsilon]/(\epsilon^2)$ is a *fat point* obtained by attaching an infinitesimal direction $\epsilon$ to a point; whereas an ordinary point $\Spec \mathbb{K}$ remembers only the value at the point, this space also carries the information of the tangent direction at that point.

From this perspective, a regular function, that is, an element $a+b\epsilon$ of $\mathbb{K}[\epsilon]/(\epsilon^2)$, carries two pieces of information simultaneously. The coefficient $a$ is the (usual) function value at that point, and $b$ is the coordinate indicating how the function changes along that tangent direction, in other words the first-order differential information at that point. Thus, even if two functions have the same value $a$ at that point, they are different functions if $b$ differs. For instance, $a+b\epsilon$ and $a+b'\epsilon$ ($b\ne b'$) have the same value at the same point but different behavior in the tangent direction, so they are distinguished as regular functions on this space. Two functions become equal only when both the value $a$ and the tangent coordinate $b$ agree, that is, when they share both the value and the first-order derivative at the point. Viewing a point with the thickness of a tangent direction attached in this way is the essence of a *fat point*, and the fact that this thickness remains is the key to capturing infinitesimal information such as intersection multiplicity.
:::

Another fundamental limitation of classical varieties is that base change, or fiber product, is not natural. This already shows up in seemingly trivial places; for instance, even the fact that the product of two projective spaces $\mathbb{P}^n\times \mathbb{P}^m$ is a projective variety required us to manually embed it into a (larger) projective space using the Segre embedding. The fact that even the product of the simplest spaces requires additional machinery to define is evidence that we have not been working in such a good world.

## Schemes

Scheme theory was born to solve all these problems. A scheme is a kind of locally ringed space whose geometric object is not merely a set of points but also includes the structure of the local ring sitting above each point.

Specifically, above we examined the limitation that classical varieties view points only as maximal ideals and take radical ideals to discard all nilpotents, and we saw that if we preserve them and view them as fat points, no information is lost. A scheme is this modification systematized throughout; here we take points to be <em>all prime ideals</em>, not maximal ideals, and define functions as sections of the local ring placed above each point.

One of the most counterintuitive consequences is the existence of generic points. For example, in $\Spec \mathbb{K}[\x,\y]$ there exist non-closed points such as $(\x)$, $(\y)$, and $(0)$ in addition to the closed points $(\x-a,\y-b)$. Among these, when the closure $\overline{\{\mathfrak{p}\}}=V(\mathfrak{p})$ of a point $\mathfrak{p}\in\Spec A$ becomes an irreducible component, we call $\mathfrak{p}$ the *generic point* of that component, and if $A$ is an integral domain then $(0)$ becomes the generic point of the entire $\Spec A$.

::: Example 3
Consider $\Spec \mathbb{Z}[\x]$. This scheme corresponds to the line $\mathbb{A}_{\mathbb{Z}}^1$ defined over $\mathbb{Z}$. The points of this space are classified as follows. First, $(0)$ is the generic point of the whole space. $(\x)$ is the generic point of the $x$-axis, carrying the universal property of the line $x=0$ on every fiber. $(p)$ is the generic point of the vertical fiber corresponding to the prime $p$, and $(p,\x)$ is the closed point that is the origin on that fiber. In this way, non-closed points are essential for capturing universal and relative properties of geometric objects.
:::

That is, intuitively, a generic point is a single point that **represents** the irreducible subvariety that a prime ideal defined in the classical setting, and the closure of that point recovers the original subvariety.

The fact that schemes allow nilpotents was already seen in the fat point of [Example 2](#ex2). In general, a scheme can retain nilpotents in its structure sheaf, thereby realizing a *non-reduced* structure geometrically, and it is thanks to this flexibility that the intuition of multiplicity and infinitesimal deformation seen above is justified.

## Relative geometry and the functor of points

The coordinate rings of the varieties we have dealt with so far were all $\mathbb{K}$-algebras. Being a $\mathbb{K}$-algebra means that a ring homomorphism $\mathbb{K}\rightarrow A$ is given, and since $\Spec$ is contravariant, this is the same as giving a morphism $\Spec A\rightarrow\Spec\mathbb{K}$. That is, our varieties were naturally schemes over $\Spec\mathbb{K}$.

In the world of schemes, we replace this base $\Spec\mathbb{K}$ by an arbitrary scheme $S$, and naturally deal with *$S$-schemes* equipped with a structure morphism $X\rightarrow S$. Under this *relative viewpoint*, we can discuss families over an arbitrary base, and even the product that was troublesome above is cleanly defined as the fiber product $X\times_S Y$ over the base; the product above is merely the case $S=\Spec \mathbb{K}$.

On the other hand, this perspective also dovetails with [\[Category Theory\] §Representable Functors, ⁋Theorem 3](/en/math/category_theory/representable_functors#thm3): if we view a scheme $X$ not as a set of points but as its *functor of points* $h_X$, understanding a scheme as the functor

$$h_X:(\Sch_{/S})^{\op}\rightarrow\Set,\qquad h_X(T)=\Hom_S(T,X)$$

that receives morphisms from all other schemes, this theorem shows that $h_X$ completely determines the scheme $X$ without loss, and from this perspective a scheme can also be understood as a contravariant functor defined on the category $\Sch_{/S}$ of $S$-schemes.

A $\mathbb{K}$-rational point on a classical variety $V$ was understood simply as the set of coordinates $(a_1,\dotsc,a_n)$ taking values in $\mathbb{K}$. In the language of schemes, this corresponds to a morphism $\Spec \mathbb{K}\rightarrow V$. The functor of points extends this perspective by defining a $T$-valued point of $V$ as a morphism from an arbitrary scheme $T$.

::: Example 4
The set of $\mathbb{K}$-rational points of a classical variety $V\subseteq\mathbb{A}_\mathbb{K}^n$ is $V(\mathbb{K})=\Hom_\mathbb{K}(\Spec \mathbb{K},V)$. This corresponds to the value of the functor of points $h_V$ evaluated at the base scheme $T=\Spec \mathbb{K}$, namely $h_V(\Spec \mathbb{K})$. However, if we substitute $T=\Spec \mathbb{K}[\epsilon]/(\epsilon^2)$, then $h_V(T)$ parameterizes the points on the tangent bundle of $V$, providing rich geometric information invisible from classical $\mathbb{K}$-rational points alone.
:::

In particular, for the projective line $\mathbb{P}_\mathbb{K}^1$, we can see clearly how infinitesimal structure is revealed through the functor of points. $\mathbb{P}_\mathbb{K}^1$ is itself a scheme with a homogeneous coordinate, so for any $\mathbb{K}$-algebra $R$, $\mathbb{P}_\mathbb{K}^1(R)$ is defined as the points on the projective line over $R$.

::: Example 5
Let $T=\Spec \mathbb{K}[\epsilon]/(\epsilon^2)$. Considering the $T$-valued points of $\mathbb{P}_\mathbb{K}^1$, that is, morphisms $T\rightarrow\mathbb{P}_\mathbb{K}^1$, these simultaneously determine a point $P$ on $\mathbb{P}_\mathbb{K}^1$ and a tangent vector at that point. Specifically, the point $P$ is obtained by composing the closed immersion $\Spec \mathbb{K}\hookrightarrow T$ with $T\rightarrow\mathbb{P}_\mathbb{K}^1$, and the remaining information becomes an element of the Zariski tangent space at $P$. Therefore, the $\mathbb{K}[\epsilon]/(\epsilon^2)$-points of $\mathbb{P}_\mathbb{K}^1$ are in one-to-one correspondence with the points constituting the tangent bundle of $\mathbb{P}_\mathbb{K}^1$.
:::

The functor of points thus serves as a bridge between geometric intuition and categorical formalism, by enabling us to understand schemes as representable functors.

This post is not one that establishes rigorous definitions or important theorems, but rather a preview of some of the big themes of scheme theory that we will cover in this category, written in advance to supplement the intuition that the rigorous tools in the posts to follow might miss. From the next post onward, we will again develop scheme theory based on rigorous mathematical content.

---

**References**

**[Har]** R. Hartshorne, *Algebraic geometry*, Springer, 1977.
