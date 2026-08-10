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
translated_at: 2026-07-27T02:15:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-07-27T02:15:02+00:00
---
## Algebraic Varieties

Posts in the [Algebraic Varieties](/en/algebraic_varieties/) category followed the basic framework of classical algebraic geometry. That is, the theory of affine varieties—defined as subsets of affine space $\mathbb{A}_\mathbb{K}^n$ over an algebraically closed field $\mathbb{K}$—and of projective varieties obtained by gluing these together appropriately, has yielded rich results in many directions. In particular, the correspondence between the coordinate ring of a variety and the ideal defined by the variety ([\[Algebraic Varieties\] §Affine Varieties, ⁋Proposition 18](/en/math/algebraic_varieties/affine_varieties#prop18)) is a representative example showing the deep connection between geometry and algebra.

A scheme is a systematically constructed space designed to overcome what these varieties miss. Before developing scheme theory, this post aims to examine the respects in which it extends varieties and what new geometric intuition it provides, so as to grasp the big picture in advance.

To this end, let us briefly recall the setting of algebraic varieties. The objects of departure are the *affine variety* from [\[Algebraic Varieties\] §Affine Varieties, ⁋Definition 2](/en/math/algebraic_varieties/affine_varieties#def2) and the *projective variety* from [\[Algebraic Varieties\] §Projective Varieties, ⁋Definition 3](/en/math/algebraic_varieties/projective_varieties#def3), which were defined respectively as irreducible algebraic subsets of affine space $\mathbb{A}_\mathbb{K}^n$ and projective space $\mathbb{P}_\mathbb{K}^n$ over an algebraically closed field $\mathbb{K}$. More important was that these could be understood as locally ringed spaces $(V,\mathcal{O}_V)$ equipped with the sheaf $\mathcal{O}_V$ of regular functions defined on them.

In this world, every point was a closed point. That is, a point on $\mathbb{A}_\mathbb{K}^2$ was completely determined by the maximal ideal $(\x-a, \y-b)\subseteq \mathbb{K}[\x,\y]$ corresponding to the coordinates $(a,b)\in \mathbb{K}^2$. While this may be called geometrically intuitive, it is not a particularly favorable environment for developing theory; for example, if we consider the line $V(\y)$ and the parabola $V(\y-\x^2)$ on $\mathbb{A}_\mathbb{K}^2$, the fact that they meet at the point $(0,0)$ is readily visible in classical algebraic varieties, but the fact that the intersection degree is not $1$ is invisible.

::: Example 1
Let us examine how schemes encode the degree of such an intersection. First, consider the case where the intersection has degree $1$: in $\mathbb{A}_\mathbb{K}^2$, we look at the intersection of the two curves $V(\y-\x)$ and $V(\y)$. From the classical algebraic variety point of view, this is indistinguishable from the situation discussed above. That is, these two lines meet at a single point $V(\x,\y)=\{(0,0)\}$.

To see how the intersection point of these two lines differs from the example above, it suffices to look at the ideals defining them. Namely,

$$(\y-\x)+(\y)=(\x,\y),\qquad (\y-\x^2)+(\y)=(\x^2,\y)$$

so, unlike the first case, in the second case there remains a nilpotent element $\bar{\x}$ in $\mathbb{K}[\x,\y]/(\x^2, \y)$. In fact,

$$\frac{\mathbb{K}[\x,\y]}{(\x^2,\y)} \cong \frac{\mathbb{K}[\epsilon]}{(\epsilon^2)}$$

holds, and the dimension of this ring as a $\mathbb{K}$-vector space is $2$. This dimension is precisely the heart of the scheme-theoretic intersection, which reflects the intersection multiplicity as a coefficient.
:::

This was in fact anticipated to some extent by [\[Algebraic Varieties\] §Affine Varieties, ⁋Theorem 10](/en/math/algebraic_varieties/affine_varieties#thm10): since the points of a classical variety are defined only by radical ideals, all nilpotent elements are discarded, and as a result all infinitesimal information must be thrown away. The key idea of schemes is to preserve and retain all of this information that was previously discarded.

::: Example 2
Consider the ring $\mathbb{K}[\epsilon]/(\epsilon^2)$ examined above. Since this ring has a single prime ideal $(\epsilon)$, in classical algebraic geometry this space looks like a single point, and this remains true in the world of schemes as well.

What is crucially different is that in the world of schemes, functions defined on this space are more refined. To see this refinement properly, we must understand this space not as a mere single point, but as a point with an extra tangent direction attached. That is, $\Spec \mathbb{K}[\epsilon]/(\epsilon^2)$ is a *fat point* obtained by attaching an infinitesimal direction $\epsilon$ to a point; whereas an ordinary point $\Spec \mathbb{K}$ only remembers the value at the point, this space also carries information about the tangent direction at that point.

From this perspective, a regular function—that is, an element $a+b\epsilon$ of $\mathbb{K}[\epsilon]/(\epsilon^2)$—simultaneously encodes two pieces of information. The coefficient $a$ is the function value (in the usual sense) at the point, and $b$ is the coordinate indicating how the function changes along that tangent direction—in other words, the first-order differential information at that point. Thus, even if two functions have the same value $a$ at the point, they are different functions if $b$ differs. For instance, $a+b\epsilon$ and $a+b'\epsilon$ (with $b\ne b'$) have the same value at the same point, but since their behavior in the tangent direction differs, they are distinguished as regular functions on this space. Two functions are equal only when not only the value $a$ but also the tangent coordinate $b$ coincide—that is, only when they share both the value and the first derivative at the point. Viewing a point with the thickness of a tangent direction attached in this way is the essence of a *fat point*, and the fact that this thickness remains is the key to capturing infinitesimal information, including intersection multiplicities.
:::

Another fundamental limitation of classical varieties is that base change, or fiber product, is not natural. This already appears in seemingly trivial situations: for example, even the fact that the product of two projective spaces $\mathbb{P}^n\times \mathbb{P}^m$ is a projective variety had to be shown by hand, using the Segre embedding to embed it into a (larger) projective space. The need for additional machinery just to handle the product of the simplest spaces is evidence that we have not been working in such a favorable world.

## Scheme

Scheme theory was born to resolve all of these problems. A scheme is a kind of locally ringed space whose geometric object is not merely a set of points, but also includes the structure of the local ring sitting above each point.

More concretely, above we examined the limitation that classical varieties view points only as maximal ideals and take radicals to discard all nilpotents, and we saw that if we keep these alive by viewing them as fat points, no information is lost. A scheme is the systematic organization of this correction throughout the entire theory: here we take points to be all prime ideals, not just maximal ideals, and we place a local ring above each point, defining functions as its sections.

One of the most counterintuitive consequences that emerges is the existence of generic points. For example, in $\Spec \mathbb{K}[\x,\y]$, besides the closed points $(\x-a,\y-b)$, there also exist non-closed points such as $(\x)$, $(\y)$, and $(0)$. Among these, when the closure $\overline{\{\mathfrak{p}\}}=Z(\mathfrak{p})$ of some point $\mathfrak{p}\in\Spec A$ becomes an irreducible closed subset, we call $\mathfrak{p}$ the *generic point* of that irreducible closed subset; and if $A$ is an integral domain, then $(0)$ becomes the generic point of the entire $\Spec A$.

::: Example 3
Consider $\Spec \mathbb{Z}[\x]$. This scheme corresponds to the line $\mathbb{A}_{\mathbb{Z}}^1$ defined over $\mathbb{Z}$. In this example we examine some points of this space.

First, $(0)$ is the generic point of the whole space. $(\x)$ is the generic point of the $x$-axis, capturing the universal property of the line $x=0$ on every fiber. $(p)$ is the generic point of the vertical fiber corresponding to the prime $p$, and $(p,\x)$ is the closed point that is the origin on that fiber. In this way, non-closed points are essential for capturing the universal and relative properties of a geometric object.
:::

That is, intuitively, a generic point represents the irreducible subvariety that a prime ideal used to define in the classical setting **as a single point**, and the closure of that point recovers the original subvariety.

The fact that schemes allow nilpotents was already seen in the fat point of [Example 2](#ex2). In general, a scheme can retain nilpotents in its structure sheaf, thereby geometrically realizing a *non-reduced* structure, and it is this flexibility that justifies the intuition regarding multiplicity and infinitesimal deformation seen earlier.

## Relative geometry and functor of points

Up to now, the coordinate rings of the varieties we have dealt with were all $\mathbb{K}$-algebras. Being a $\mathbb{K}$-algebra means that a ring homomorphism $\mathbb{K}\rightarrow A$ is given, and since $\Spec$ is contravariant this is the same as giving a morphism $\Spec A\rightarrow\Spec\mathbb{K}$. Thus our varieties were naturally schemes over $\Spec\mathbb{K}$.

In the world of schemes we replace this base $\Spec\mathbb{K}$ by an arbitrary scheme $S$, and naturally work with *$S$-schemes*, i.e. schemes equipped with a structure morphism $X\rightarrow S$. Under this *relative viewpoint* one can discuss families over an arbitrary base, and even the product, which was troublesome above, is neatly defined as the fiber product $X\times_S Y$ over the base; the product above was merely the case $S=\Spec \mathbb{K}$.

On the other hand this perspective also dovetails with [\[Category Theory\] §Representable Functors, ⁋Theorem 4](/en/math/category_theory/representable_functors#thm4): if we view a scheme $X$ not as a set of points but via its *functor of points* $h_X$, understanding the scheme as the functor receiving morphisms from all other schemes

$$h_X:(\Sch_{/S})^{\op}\rightarrow\Set,\qquad h_X(T)=\Hom_S(T,X)$$

then this theorem shows that $h_X$ completely determines the scheme $X$ without loss, and from this perspective a scheme can also be understood as a contravariant functor defined on the category $\Sch_{/S}$ of $S$-schemes.

A $\mathbb{K}$-rational point on a classical variety $V$ was understood simply as a set of coordinates $(a_1,\dotsc,a_n)$ with values in $\mathbb{K}$. In the language of schemes this corresponds to a morphism $\Spec \mathbb{K}\rightarrow V$. The functor of points extends this viewpoint by defining a $T$-valued point of $V$ as a morphism from an arbitrary scheme $T$.

::: Example 4
The set of $\mathbb{K}$-rational points of a classical variety $V\subseteq\mathbb{A}_\mathbb{K}^n$ is $V(\mathbb{K})=\Hom_\mathbb{K}(\Spec \mathbb{K},V)$. This corresponds to evaluating the functor of points $h_V$ at the base scheme $T=\Spec \mathbb{K}$, i.e., $h_V(\Spec \mathbb{K})$. However, substituting $T=\Spec \mathbb{K}[\epsilon]/(\epsilon^2)$ makes $h_V(T)$ parameterize the tangent vectors to $V$ at its $\mathbb{K}$-points.
:::

In particular, for the projective line $\mathbb{P}_\mathbb{K}^1$, we can see clearly how infinitesimal structure is revealed through the functor of points. Since $\mathbb{P}_\mathbb{K}^1$ is itself a scheme with homogeneous coordinates, for any $\mathbb{K}$-algebra $R$ the set $\mathbb{P}_\mathbb{K}^1(R)$ is defined as the points on the projective line over $R$.

::: Example 5
Let $T=\Spec \mathbb{K}[\epsilon]/(\epsilon^2)$. Considering the $T$-valued points of $\mathbb{P}_\mathbb{K}^1$, that is, morphisms $T\rightarrow\mathbb{P}_\mathbb{K}^1$, these simultaneously determine a point $P$ on $\mathbb{P}_\mathbb{K}^1$ and a tangent vector at that point. Specifically, the point $P$ is obtained by composing the closed immersion $\Spec \mathbb{K}\hookrightarrow T$ with $T\rightarrow\mathbb{P}_\mathbb{K}^1$, and the remaining information becomes an element of the Zariski tangent space at $P$. Thus the $\mathbb{K}[\epsilon]/(\epsilon^2)$-points of $\mathbb{P}_\mathbb{K}^1$ are in bijection with the points constituting the tangent bundle of $\mathbb{P}_\mathbb{K}^1$.
:::

The functor of points serves as a bridge between geometric intuition and categorical formalism by allowing us to understand a scheme as a representable functor.

This post is not one that establishes rigorous definitions or major theorems, but rather a preview of several broad themes in scheme theory that will be covered in this category going forward, written to supplement the intuition that might be missed by the rigorous tools needed in subsequent posts. From the next post onward, we will once again develop scheme theory based on rigorous mathematical content.

---

**References**

**[Har]** R. Hartshorne, *Algebraic geometry*, Springer, 1977.
