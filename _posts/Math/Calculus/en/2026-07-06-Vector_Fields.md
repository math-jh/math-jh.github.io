---
title: "Vector Fields"
description: "We introduce vector fields, which assign a vector to each point in space, and define gradient fields, conservative fields, and potentials. We define divergence and curl, examine their meanings, and show that curl of a gradient is zero, divergence of a curl is zero, and conservative fields are irrotational."
excerpt: "Vector fields and gradient fields, conservative fields and potentials, divergence and curl, differential identities"

categories: [Math / Calculus]
permalink: /en/math/calculus/vector_fields
sidebar: 
    nav: "calculus-en"

date: 2026-07-06
weight: 16
translated_at: 2026-07-05T22:00:03+00:00
translation_source: kimi-cli
last_polished_at: 2026-07-05T22:00:03+00:00
---
What we ultimately want to study is the calculus of general functions $\mathbb{R}^m\rightarrow\mathbb{R}^n$. We have prepared for this by first raising the dimension of the codomain in [§Curves and Vector-Valued Functions](/en/math/calculus/vector_functions), and then raising the dimension of the domain from [§Multivariable Functions and Partial Derivatives](/en/math/calculus/partial_derivatives) onward. Now we combine both directions and begin the general case in which both the domain and codomain are multidimensional. In particular, the most natural object of interest is the case where the dimensions of the domain and codomain are equal, namely $\mathbb{R}^n\rightarrow\mathbb{R}^n$; such a function takes an $n$-dimensional vector and returns an $n$-dimensional vector.

## Vector Fields

However, because the cross product—one of the powerful operations at our disposal—is defined only in three dimensions, we will for the most part work in three dimensions, and in its subspace of two dimensions. Nevertheless, the following definitions make sense in arbitrary dimensions.

::: Definition 1
A function $\mathbf{F}\colon D \rightarrow \mathbb{R}^n$ that assigns to each point $\mathbf{x}$ in a domain $D \subseteq \mathbb{R}^n$ a vector $\mathbf{F}(\mathbf{x}) \in \mathbb{R}^n$ is called a *vector field*. In the plane we write $\mathbf{F}(x,y) = (P(x,y), Q(x,y))$, and in space $\mathbf{F}(x,y,z) = (P, Q, R)$; if each component $P, Q, R$ is $C^1$, then $\mathbf{F}$ is called a $C^1$ vector field.
:::

A vector field is most intuitively understood as a picture with an arrow emanating from each point. For instance, the flow velocity of a fluid at each point constitutes a vector field. We already know one such object. ([§Multivariable Functions and Partial Derivatives, ⁋Definition 2](/en/math/calculus/partial_derivatives#def2))

::: Definition 2
The vector field given by the gradient $\nabla f = (\partial f/\partial x_1, \ldots, \partial f/\partial x_n)$ of a $C^1$ scalar function $f$ is called the *gradient field* of $f$. A vector field $\mathbf{F}$ that can be written as $\mathbf{F} = \nabla f$ for some scalar function $f$ is called a *conservative field*, and that $f$ is called the *potential* of $\mathbf{F}$.
:::

## Divergence and Curl

On the other hand, not every vector field is conservative, so the central problem becomes determining whether a given $\mathbf{F}$ is the gradient of some $f$. The operations used for this determination are those in the following definition; in particular, because defining $\curl$ requires the cross product, we are inevitably forced down to three dimensions.

::: Definition 3
The *divergence* of a $C^1$ vector field $\mathbf{F} = (P, Q, R)$ is the scalar field

$$\divergence \mathbf{F} = \nabla \cdot \mathbf{F} = \frac{\partial P}{\partial x} + \frac{\partial Q}{\partial y} + \frac{\partial R}{\partial z}$$

and the *curl* is the vector field

$$\curl \mathbf{F} = \nabla \times \mathbf{F} = \left(\frac{\partial R}{\partial y} - \frac{\partial Q}{\partial z},\ \frac{\partial P}{\partial z} - \frac{\partial R}{\partial x},\ \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\right).$$

:::

The two notations $\nabla\cdot \mathbf{F}$ and $\nabla \times \mathbf{F}$ above are formal: we regard $\nabla = (\partial_x, \partial_y, \partial_z)$ as a vector and take the dot and cross products with it.

::: Example 4
The radial vector field $\mathbf{F}(x,y,z) = (x, y, z)$ has $\divergence \mathbf{F} = 1 + 1 + 1 = 3$, which is positive everywhere. Intuitively, this calculation tells us that this vector field is <em>outward</em> at every point. On the other hand, $\curl \mathbf{F} = 0$. This can be interpreted as meaning that $\mathbf{F}$ has no rotational component whatsoever and is composed purely of an outward component.

In contrast, the vector field $\mathbf{G}(x,y,z) = (-y, x, 0)$ rotating around the $z$-axis has $\divergence \mathbf{G} = 0$ but $\curl \mathbf{G} = (0, 0, 2)$, showing that it is a vector field rotating about the $z$-axis.
:::

Now let us see how these operations determine whether a given vector field is conservative. For this we first need the following.

::: Proposition 5
For a $C^2$ function $f$ and a $C^2$ vector field $\mathbf{F}$,

$$\curl(\nabla f) = 0, \qquad \divergence(\curl \mathbf{F}) = 0.$$

:::

::: Proof
The first component of the curl of $\nabla f = (f_x, f_y, f_z)$ is $\partial_y f_z - \partial_z f_y = f_{zy} - f_{yz}$, which is $0$ by [§Multivariable Functions and Partial Derivatives, ⁋Theorem 7](/en/math/calculus/partial_derivatives#thm7), and the remaining two components are $0$ for the same reason. Also, the divergence of $\curl \mathbf{F} = (R_y - Q_z,\ P_z - R_x,\ Q_x - P_y)$ is

$$\partial_x(R_y - Q_z) + \partial_y(P_z - R_x) + \partial_z(Q_x - P_y) = (R_{yx} - R_{xy}) + (P_{zy} - P_{yz}) + (Q_{xz} - Q_{zx})$$

and applying [§Multivariable Functions and Partial Derivatives, ⁋Theorem 7](/en/math/calculus/partial_derivatives#thm7) to each parenthesis again shows that it equals $0$.
:::

The first identity gives a necessary condition for a conservative field. If $\mathbf{F} = \nabla f$, then $\curl \mathbf{F} = \curl(\nabla f) = 0$, so a vector field with nonzero curl can never be conservative. That is, the following holds.

::: Proposition 6
A conservative field is irrotational. That is, if a $C^1$ vector field $\mathbf{F}$ is conservative, then $\curl \mathbf{F} = 0$. For a plane vector field $\mathbf{F} = (P, Q)$, this is equivalent to $\partial Q/\partial x = \partial P/\partial y$.
:::

However, this condition is only necessary, and the converse does not hold in general. The interesting point is that the converse depends on the shape of the domain: if the domain has no "holes," then the converse also holds, but if there are holes, there exist irrotational vector fields that are not conservative.

::: Example 7
Consider $\mathbf{F} = (2xy,\ x^2 + z,\ y)$. Computing its curl,

$$\curl \mathbf{F} = (\partial_y y - \partial_z(x^2+z),\ \partial_z(2xy) - \partial_x y,\ \partial_x(x^2+z) - \partial_y(2xy)) = (1 - 1,\ 0,\ 2x - 2x) = 0$$

so it may be conservative. Let us see whether we can find an $f$ satisfying $\mathbf{F}=\nabla f$.

Such an $f$ must first satisfy $f_x = 2xy$ from the first component, so it must be of the form $f = x^2 y + g(y, z)$. Differentiating this with respect to $y$ gives $f_y = x^2 + g_y$, and if $\mathbf{F}$ were conservative, this must match the second component $x^2 + z$ of $\mathbf{F}$, so $g_y = z$, i.e., $g = yz + h(z)$. Finally, substituting this back into $f$ and differentiating with respect to $z$ and matching coefficients, we need $f_z = y + h'(z) = y$, so $h' = 0$. Therefore $f = x^2 y + yz$ can serve as a potential, and indeed $\mathbf{F} = \nabla f$ holds.
:::
