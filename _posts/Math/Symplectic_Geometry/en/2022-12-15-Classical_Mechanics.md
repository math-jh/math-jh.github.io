---
title: "Classical Mechanics"
description: "This post explores the physical background of symplectic geometry through the law of conservation of energy and phase space. It summarizes how symplectic manifolds emerged from nineteenth-century physics."
excerpt: "Classical mechanics and phase space"

categories: [Math / Symplectic Geometry]
permalink: /en/math/symplectic_geometry/classical_mechanics
sidebar: 
    nav: "symplectic_geometry-en"

date: 2022-12-15
weight: 1
translated_at: 2026-06-02T23:00:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-11-07T03:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
In this post, we examine the historical (physical) background behind the introduction of symplectic manifolds studied in symplectic geometry. As a student of mathematics, this is a compilation of things picked up here and there, so there may be a few physical errors.

## Conservation of Energy

In physics, especially in mechanics, there are various formulas describing the motion of objects. For example, Newton's law of motion $F=ma$ is likely a formula that everyone knows, even those who have not studied physics.

One fact that became clear to physicists in the 19th century is that it is not these formulas that determine the motion of an object, but rather a single function that determines the motion of an object. In a sense, this fact can also be said to be somewhat related to the *law of conservation of energy*.

To examine this, consider a *phase space* where one axis represents the position of an object and the other axis represents the momentum of the object. For example, the phase space corresponding to a 1-dimensional space will be a 2-dimensional space consisting of one position axis and one momentum axis, and in general, the phase space of an $n$-dimensional space, consisting of $n$-dimensional position coordinates and $n$-dimensional momentum coordinates, will be a $2n$-dimensional space.

{% diagram Math/Symplectic_Geometry/Classical_Mechanics-1.svg width="13.13em" alt="phase_space" %}

In this situation, kinetic energy $K=\frac{1}{2}mv^2$ or potential energy $P=mgh$, etc., become physical quantities that can be described through position and velocity coordinates, aside from the constants $m$ and $g$. That is, these energies are functions from phase space to $\mathbb{R}$. Then the law of conservation of energy means that when the motion of an object is described in phase space, its trajectory must be completely contained within a level set of the energy function.

For example, consider the motion of an object in one dimension on which no force acts. That is, since the only energy this object has is kinetic energy, we may think of the energy function $E:\mathbb{R}^2\rightarrow\mathbb{R}$ as $E(x,v)=v^2$. Then the level sets of $E$ are line segments drawn parallel to the position axis.

{% diagram Math/Symplectic_Geometry/Classical_Mechanics-2.svg width="13.13em" alt="kinetic_energy" %}

According to the law of conservation of energy, an object whose starting point is a point in phase space cannot leave this level set, no matter how much time elapses. Physically, this can be interpreted as the acceleration of the object being 0 when no external force acts.

The law of conservation of mechanical energy learned in high school generally means that the sum of kinetic energy and potential energy does not change. Drawing a picture similarly to the above, the level sets of the energy function are roughly as follows.

{% diagram Math/Symplectic_Geometry/Classical_Mechanics-3.svg width="12.02em" alt="mechanical_energy" %}

Likewise, according to the law of conservation of energy, the motion of the object must always lie on this level set of energy.

Finally, consider the motion of an object attached to a spring. According to Hooke's law, the potential energy imparted to the object by the spring is given by $\frac{1}{2}kx^2$. Since the kinetic energy of the object is $\frac{1}{2}mv^2$, it suffices to define the energy function $E$ by $E(x,v)=\frac{1}{2}kx^2+\frac{1}{2}mv^2$. Plotting this in phase space yields an elliptical shape as follows.

{% diagram Math/Symplectic_Geometry/Classical_Mechanics-4.svg width="19.81em" alt="harmonic_oscillator" %}

This suggests that the motion of the object will be periodic.

The picture above makes sense when the dimension in which the object moves is 1 dimension, but even if the dimension in which the object moves is just 2 dimensions, the phase space becomes 4-dimensional, and hence the energy level set becomes 3-dimensional; therefore, additional tools are needed to explain along which curve the object actually moves within it.

## Principle of Least Action

What plays an important role in this process is the following *principle of least action*.

> When an object moves from $x_0$ to $x_1$, this object moves along the extremum $z(t)=(x(t),y(t))$ ($t_0\leq t\leq t_1$) of the following *action*.
> 
> $\mathcal{A}_H(z)=\int_{t_0}^{t_1}\langle y,\dot{x}\rangle-H(z)\dd{t}$

The $H$ newly introduced in the formula denotes the *Hamiltonian*, and in what follows, we may simply think of it as energy. This principle holds locally even when $H$ depends on time; in that case, one can simply replace $H$ by $H_t$. How to handle such problems mathematically is very well known.

::: Proposition 1
For a path $z(t)=(x(t),y(t))$ ($t_0\leq t\leq t_1$) in phase space, being, among paths satisfying the position conditions $x(t_0)=x_0$, $x(t_1)=x_1$, an extremum of $\mathcal{A}_H$ is equivalent to $z$ satisfying the following *Hamilton's equation*:

$$\dot{x}=\frac{\partial H_t}{\partial y},\quad \dot{y}=-\frac{\partial H_t}{\partial x}$$
:::
::: Proof
To prove this, suppose that a 1-parameter family of paths satisfying the position conditions $x_s(t_0)=x_0$, $x_s(t_1)=x_1$, $(z_s)=(x_s,y_s)$, is given, and let $z_0=z$. Then

$$\begin{aligned}\frac{\partial}{\partial s}\bigg\vert_{s=0}\mathcal{A}_H(z_s)&=\frac{\partial}{\partial s}\bigg\vert_{s=0}\int_{t_0}^{t_1}\langle y_s,\dot{x}_s\rangle-H_t(x_s,y_s)\dd{t}\\&=\int_{t_0}^{t_1}\frac{\partial}{\partial s}\bigg\vert_{s=0}\left(\langle y_s,\dot{x}_s\rangle-H_t(x_s,y_s)\right)\dd{t}\\&=\int_{t_0}^{t_1}\bigl\langle\partial_s y_s\vert_0,\dot{x}\bigr\rangle+\bigl\langle y,\partial_s\dot{x}_s\vert_0\bigr\rangle-\bigl\langle\partial_sx_s\vert_0,\partial_x H_t\bigr\rangle-\bigl\langle\partial_sy_s\vert_0,\partial_yH_t\bigr\rangle\dd{t}\end{aligned}$$

Now, considering integration by parts:

$$\int_{t_0}^{t_1}\langle y,\partial_s\dot{x}_s\vert_0\rangle\dd{t}=\bigl[\langle y,\partial_sx_s\vert_0\rangle\bigr]_{t_0}^{t_1}-\int_{t_0}^{t_1}\langle\dot{y},\partial_sx_s\vert_0\rangle\dd{t}$$

from the position conditions $x_s(t_0)=x_0$, $x_s(t_1)=x_1$, the first term on the right-hand side becomes $0$. Substituting this into the preceding equation and rearranging,

$$\frac{\partial}{\partial s}\bigg\vert_{s=0}\mathcal{A}_H(z_s)=\int_{t_0}^{t_1}\langle\partial_sy_s\vert_0,\dot{x}-\partial_yH_t\rangle\dd{t}-\int_{t_0}^{t_1}\langle\partial_sx_s\vert_0,\dot{y}+\partial_xH_t\rangle\dd{t}$$

and since $\partial_sx_s\vert_0$ and $\partial_sy_s\vert_0$ can vary arbitrarily, that $z$ is an extremum of $\mathcal{A}_H$ is equivalent to the two equations

$$\dot{x}-\partial_yH_t=0,\qquad\dot{y}+\partial_xH_t=0$$

holding.
:::

On the vector space $\mathbb{R}^{2n}$, consider the (linear) complex structure[^1] $J_0\in\End(\mathbb{R}^{2n})$. With respect to the basis $\{x_1,\ldots, x_n,y_1,\ldots, y_n\}$, this linear map is given by the matrix

$$J_0=\begin{pmatrix}0&-I\\I&0\end{pmatrix}$$

When we identify $\mathbb{R}^{2n}$ through $z_j:=x_j+iy_j$ with $\mathbb{C}^n$, this represents multiplication by the imaginary unit $i$. If we regard $\mathbb{R}^{2n}$ as a manifold and at each point $p\in\mathbb{R}^{2n}$ consider $T_p\mathbb{R}^{2n}\cong\mathbb{R}^{2n}$ as the tangent space, $J_0$ can be regarded, via the following equations

$$J_0\left(\frac{\partial}{\partial x^j}\bigg\vert_p\right)=\frac{\partial}{\partial y^j}\bigg\vert_p,\qquad J_0\left(\frac{\partial}{\partial y^j}\bigg\vert_p\right)=-\frac{\partial}{\partial x^j}\bigg\vert_p\tag{1}$$

as an element of $\End(T\mathbb{R}^{2n})$. Now, since

$$\nabla H=\begin{pmatrix}\partial H/\partial x\\ \partial H/\partial y\end{pmatrix}$$

Hamilton's equation can simply be written as the following equation:

$$\dot{z}=-J_0\nabla H(z)$$

Intuitively, since the gradient $\nabla H$ points in the direction of greatest change of $H$, namely the direction perpendicular to the level surfaces of $H$, rotating this again by 90 degrees via $J_0$ to make it parallel to the level surfaces of $H$ can be thought of as $\dot{z}$.

Therefore, finding the path along which the object actually moves in phase space, namely $z$, is precisely the same as the problem of finding the integral flow of the following *Hamiltonian vector field*

$$X_H=-J_0\nabla H(z)$$

and we know that this is always possible. ([\[Manifolds\] §Vector Fields, ⁋Theorem 6](/en/math/manifolds/vector_fields#thm6){: data-lid="no604" })

## Symplectic form

To summarize the above process, the Hamiltonian $H$ describes the motion of the object through the equation

$$\dd{H}=\langle-J_0\nabla H(z), -\rangle$$

Now, if we define on $\mathbb{R}^{2n}$ a $2$-form

$$\omega_0(-,-):=\langle J_0-, -\rangle$$

the equation above can be written, similarly to how for a function $f$ the gradient $\nabla f$ defines $\dd{f}=\langle \nabla f,-\rangle$, as

$$\dd{H}=\omega_0(X_H, -)$$

$\omega_0$ is called the *canonical symplectic form* defined on $\mathbb{R}^{2n}$, and from this perspective, $X_H$ is also called the *symplectic gradient*.

In the standard coordinates of $\mathbb{R}^{2n}$,

$$\langle-,-\rangle=\sum_{j=1}^n \dd{x}^j\otimes \dd{x}^j+\sum_{j=1}^n \dd{y}^j\otimes \dd{y}^j$$

so using equation (1), one can compute $\omega_0$ on each of the basis elements $\partial/\partial x^j,\partial/\partial y^j$. For example,

$$(\omega_0)_p\left(\frac{\partial}{\partial x^j}\bigg\vert_p,\frac{\partial}{\partial y^k}\bigg\vert_p\right)=\left\langle\frac{\partial}{\partial y^j}\bigg\vert_p,\frac{\partial}{\partial y^k}\bigg\vert_p\right\rangle_p=\delta_{jk}$$

and calculating for the remaining basis elements as well, one can verify that in standard coordinates $\omega_0$ appears as

$$\omega_0=\sum_{j=1}^n \dd{x}^j\wedge \dd{y}^j$$

Before long, we will see that the discussion so far remains valid even if we replace the setting with an arbitrary manifold $M$, cotangent bundle $T^\ast M$, Riemannian metric $g$, and almost complex structure $J$.

---

**References**

**[MS]** D. Mcduff and D. Salamon. *Introduction to symplectic topology*. Oxford graduate texts in mathematics. Oxford University Press, 2017.

---

[^1]: A *linear complex structure* defined on a vector space $V$ refers to an element satisfying $J^2=-\id$, namely $J\in\End(V)$. When such a $J$ is given, one can verify via the formula $(a+bi)\cdot v:=av+bJv$ that $V$ has the structure of a $\mathbb{C}$-vector space.
