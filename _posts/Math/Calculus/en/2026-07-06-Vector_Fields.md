---
title: "Vector Fields"
description: "We introduce vector fields that assign a vector to each point in space, and define gradient fields, conservative fields, and potentials. We define divergence and curl, examine their meaning, and show that the curl of a gradient is zero, the divergence of a curl is zero, and that conservative fields are irrotational."
excerpt: "Vector fields, gradient and conservative fields, potentials, divergence and curl, differential identities"

categories: [Math / Calculus]
permalink: /en/math/calculus/vector_fields
sidebar: 
    nav: "calculus-en"

date: 2026-07-06
weight: 16
translated_at: 2026-08-19T11:45:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-10-01T11:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
What we ultimately want to treat is the calculus of general functions $\mathbb{R}^m\rightarrow\mathbb{R}^n$. We prepared for this first by raising the dimension of the codomain in [§Curves and Vector-Valued Functions](/en/math/calculus/vector_functions){: data-lid="glm3l" }, and then the dimension of the domain after [§Functions of Several Variables and Partial Derivatives](/en/math/calculus/partial_derivatives){: data-lid="q8s28" }. Now we combine both directions into one and begin the general case where both the domain and codomain are multidimensional. In particular, $\mathbb{R}^n\rightarrow\mathbb{R}^n$, where the domain and codomain have the same dimension, is the most natural object; then this function takes an $n$-dimensional vector and outputs an $n$-dimensional vector. 

## Vector Fields

However, in practice, since the cross product, one of the powerful operations at our disposal, is defined only in $3$ dimensions, we will conduct most of our discussion in $3$ dimensions, and in its subspace, $2$ dimensions. In any case, the following definitions make sense in general dimensions as well. 

::: Definition 1
A function on a domain $D \subseteq \mathbb{R}^n$ that assigns to each point $\mathbf{x}$ a vector $\mathbf{F}(\mathbf{x}) \in \mathbb{R}^n$, $\mathbf{F}\colon D \rightarrow \mathbb{R}^n$, is called a *vector field*. In the plane we write $\mathbf{F}(x,y) = (P(x,y), Q(x,y))$, and in space $\mathbf{F}(x,y,z) = (P, Q, R)$; if each component $P, Q, R$ is $C^1$, we call $\mathbf{F}$ a $C^1$ vector field.
:::

A vector field is most intuitively visualized as a picture of arrows attached to each point, originating from that point. For instance, in fluid flow, representing the velocity at each point forms a vector field. We already know one such object. ([§Functions of Several Variables and Partial Derivatives, ⁋Definition 2](/en/math/calculus/partial_derivatives#def2){: data-lid="8byij" })

::: Definition 2
For a $C^1$ scalar field $f$, the vector field given by the gradient $\nabla f = (\partial f/\partial x_1, \ldots, \partial f/\partial x_n)$ is called the *gradient field* of $f$. If, for some scalar field $f$, a vector field can be written as $\mathbf{F} = \nabla f$, the vector field $\mathbf{F}$ is called a *conservative field*, and that $f$ is called a *potential* of $\mathbf{F}$.
:::

## Divergence and Curl

On the other hand, since not every vector field is a conservative field, determining whether a given $\mathbf{F}$ is the gradient of some $f$ becomes a central problem. The operations used for this determination are given in the following definition; in particular, because defining $\curl$ requires the cross product, we inevitably have to come down to $3$ dimensions. 

::: Definition 3
The *divergence* of a $C^1$ vector field $\mathbf{F} = (P, Q, R)$ is the scalar field

$$\divergence \mathbf{F} = \nabla \cdot \mathbf{F} = \frac{\partial P}{\partial x} + \frac{\partial Q}{\partial y} + \frac{\partial R}{\partial z}$$

and the *curl* is the vector field

$$\curl \mathbf{F} = \nabla \times \mathbf{F} = \left(\frac{\partial R}{\partial y} - \frac{\partial Q}{\partial z},\ \frac{\partial P}{\partial z} - \frac{\partial R}{\partial x},\ \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\right)$$

A plane vector field $\mathbf{F} = (P, Q)$ is viewed as independent of $z$ in the form $(P, Q, 0)$, so $\curl \mathbf{F} = (0, 0, \partial Q/\partial x - \partial P/\partial y)$, and this last component is called the curl of the plane vector field. 
:::

The two notations $\nabla\cdot \mathbf{F}$ and $\nabla \times \mathbf{F}$ above are formal, viewing $\nabla = (\partial_x, \partial_y, \partial_z)$ as a vector and taking the dot and cross products.

::: Example 4
The radially extending $\mathbf{F}(x,y,z) = (x, y, z)$ has $\divergence \mathbf{F} = 1 + 1 + 1 = 3$, which is positive everywhere. Intuitively, this calculation tells us that this vector field points *outward* at every point. On the other hand, $\curl \mathbf{F} = 0$. This can be understood as meaning that $\mathbf{F}$ has no rotational component whatsoever and consists purely of an outward component.

As a contrasting example, $\mathbf{G}(x,y,z) = (-y, x, 0)$ rotating around the $z$-axis has $\divergence \mathbf{G} = 0$, but $\curl \mathbf{G} = (0, 0, 2)$, showing that it is a vector field rotating about the $z$-axis.
:::

Now let us see how these determine whether a given vector field is conservative. For this, we first need the following.

::: Proposition 5
For a $C^2$ function $f$ and a $C^2$ vector field $\mathbf{F}$,

$$\curl(\nabla f) = 0, \qquad \divergence(\curl \mathbf{F}) = 0$$

:::

::: Proof
The first component of the curl of $\nabla f = (f_x, f_y, f_z)$ is $\partial_y f_z - \partial_z f_y = f_{zy} - f_{yz}$, which is $0$ by [§Functions of Several Variables and Partial Derivatives, ⁋Theorem 7](/en/math/calculus/partial_derivatives#thm7){: data-lid="e0214" }, and the remaining two components are $0$ for the same reason. Also, the divergence of $\curl \mathbf{F} = (R_y - Q_z,\ P_z - R_x,\ Q_x - P_y)$ groups as

$$\partial_x(R_y - Q_z) + \partial_y(P_z - R_x) + \partial_z(Q_x - P_y) = (R_{yx} - R_{xy}) + (P_{zy} - P_{yz}) + (Q_{xz} - Q_{zx})$$

and applying [§Functions of Several Variables and Partial Derivatives, ⁋Theorem 7](/en/math/calculus/partial_derivatives#thm7){: data-lid="o06o9" } to each parenthesis again shows that it is $0$.
:::

The first identity gives a necessary condition for determining whether a vector field is conservative. This is because if $\mathbf{F} = \nabla f$, then $\curl \mathbf{F} = \curl(\nabla f) = 0$, so a vector field whose curl is not $0$ can never be conservative. That is, the following holds.

::: Proposition 6
A conservative field is irrotational. That is, if a $C^1$ vector field $\mathbf{F}$ is conservative, then $\curl \mathbf{F} = 0$. For a plane vector field $\mathbf{F} = (P, Q)$, this is equivalent to $\partial Q/\partial x = \partial P/\partial y$.
:::

However, this condition is only a necessary condition, and the converse does not hold. The interesting point is that this converse depends on the shape of the domain: if the domain has no "holes," then the converse also holds, but if there are holes, there exist vector fields that are irrotational and yet not conservative.

::: Example 7
Consider $\mathbf{F} = (2xy,\ x^2 + z,\ y)$. Computing its curl,

$$\curl \mathbf{F} = (\partial_y y - \partial_z(x^2+z),\ \partial_z(2xy) - \partial_x y,\ \partial_x(x^2+z) - \partial_y(2xy)) = (1 - 1,\ 0,\ 2x - 2x) = 0$$

so it may be conservative. Therefore, let us see whether we can find an $f$ satisfying $\mathbf{F}=\nabla f$.

Such an $f$ must first satisfy $f_x = 2xy$ by the first component, so it must take the form $f = x^2 y + g(y, z)$. Now differentiating this with respect to $y$ gives $f_y = x^2 + g_y$, and if $\mathbf{F}$ were conservative, this value would have to match the second component $x^2 + z$ of $\mathbf{F}$, so $g_y = z$, that is, $g = yz + h(z)$. Now finally, substituting this back into $f$, differentiating with respect to $z$, and matching coefficients, we must have $f_z = y + h'(z) = y$, so $h' = 0$. Thus $f = x^2 y + yz$ can serve as a potential, and indeed $\mathbf{F} = \nabla f$ holds.
:::

---

**References**

**[Ste]** J. Stewart, *Calculus*, 8th ed., Cengage Learning, 2016.  
**[Kim]** 김홍종, *미적분학 1·2*, 제3개정판, 서울대학교출판문화원, 2020.
