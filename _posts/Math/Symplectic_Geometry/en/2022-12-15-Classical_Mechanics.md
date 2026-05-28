---
title: "Classical Mechanics"
excerpt: "Classical mechanics and phase space"

categories: [Math / Symplectic Geometry]
permalink: /en/math/symplectic_geometry/classical_mechanics
header:
    overlay_image: /assets/images/Math/Symplectic_Geometry/Classical_Mechanics.png
    overlay_filter: 0.5
sidebar: 
    nav: "symplectic_geometry-en"

date: 2022-12-15
last_modified_at: 2022-12-15
weight: 1
translated_at: 2026-05-28T11:36:15+00:00
translation_source: kimi-cli
---
In this post we examine the historical (physical) background that led to the introduction of symplectic manifolds, which are studied in symplectic geometry. As a mathematician, I have compiled bits and pieces picked up here and there, so there may be some physical inaccuracies.

## Conservation of Energy

Physics, and especially mechanics, has various formulas describing the motion of objects. For example, Newton's law of motion $$F=ma$$ is a formula that even those who have not studied physics would know.

One fact that became clear to physicists in the 19th century is that rather than such formulas determining the motion of an object, a single function determines the motion. In a sense, this fact is somewhat related to the *law of energy conservation* as well.

To examine this, consider a *phase space* with one axis representing the position of an object and the other representing its momentum. For example, the phase space corresponding to a 1-dimensional space is a 2-dimensional space consisting of one position axis and one momentum axis, and in general, the phase space of an $$n$$-dimensional space is a $$2n$$-dimensional space consisting of $$n$$-dimensional position coordinates and $$n$$-dimensional momentum coordinates.

![phase_space](/assets/images/Math/Symplectic_Geometry/Classical_Mechanics-1.png){:style="width:268.8px" class="invert" .align-center}

In this situation, kinetic energy $$K=\frac{1}{2}mv^2$$ or potential energy $$P=mgh$$, etc., are physical quantities that can be described by position and velocity coordinates, excluding the constants $$m$$, $$g$$. That is, these energies are functions from phase space to $$\mathbb{R}$$. Then the law of conservation of energy means that when the motion of an object is described in phase space, its trajectory must be completely contained in a level surface of the energy function.

For example, consider the motion of an object in one dimension with no force acting on it. That is, since the energy of this object consists only of kinetic energy, we may consider the energy function $$E:\mathbb{R}^2\rightarrow\mathbb{R}$$ as $$E(x,v)=v^2$$. Then the level surfaces of $$E$$ are line segments drawn parallel to the position axis.

![kinetic_energy](/assets/images/Math/Symplectic_Geometry/Classical_Mechanics-2.png){:style="width:268.8px" class="invert" .align-center}

By the law of conservation of energy, an object starting at a point in phase space cannot leave this level surface no matter how much time passes. Interpreting this physically, when no external force acts on the object, its acceleration is zero.

The law of conservation of mechanical energy that we learn in high school generally means that the sum of kinetic energy and potential energy does not change. If we draw a similar picture as above, the level surfaces of the energy function are roughly as follows.

![mechanical_energy](/assets/images/Math/Symplectic_Geometry/Classical_Mechanics-3.png){:style="width:240.3px" class="invert" .align-center}

Likewise, by the law of conservation of energy, the motion of the object must always lie on the level surface of this energy.

Finally, consider the motion of an object attached to a spring. By Hooke's law, the potential energy imparted to the object by the spring is given by $$\frac{1}{2}kx^2$$. Since the kinetic energy of the object is $$\frac{1}{2}mv^2$$, we define the energy function $$E$$ as $$E(x,v)=\frac{1}{2}kx^2+\frac{1}{2}mv^2$$. If we plot this in phase space, an elliptical shape appears as follows.

![harmonic_oscillator](/assets/images/Math/Symplectic_Geometry/Classical_Mechanics-4.png){:style="width:391.35px" class="invert" .align-center}

This suggests that the motion of the object will be periodic.

The above picture makes sense when the dimension in which the object moves is 1, but even if the object moves in 2 dimensions, the phase space becomes 4-dimensional, and thus the energy level surface becomes 3-dimensional, so additional tools are needed to explain which curve the object actually follows within it.

## Principle of Least Action

What plays an important role in this process is the following *principle of least action*.

> When an object moves from $$x_0$$ to $$x_1$$, it follows the extremum $$z(t)=(x(t),y(t))$$ ($$t_0\leq t\leq t_1$$) of the following *action*.
> 
> $$\mathcal{A}_H(z)=\int_{t_0}^{t_1}\langle y,\dot{x}\rangle-H(z)\mathop{dt}$$

In this formula, the newly introduced $$H$$ denotes the *Hamiltonian*, and in what follows we may simply think of it as energy. This principle holds locally even when $$H$$ depends on time, in which case we simply write $$H_t$$ instead of $$H$$. It is very well known how such problems are treated mathematically.

<div class="proposition" markdown="1">

<ins id="prop1">**Proposition 1**</ins> A path $$z(t)=(x(t),y(t))$$ ($$t_0\leq t\leq t_1$$) in phase space is an extremum of $$\mathcal{A}_H$$ among paths satisfying the boundary conditions $$x(t_0)=x_0$$, $$x(t_1)=x_1$$ if and only if $$z$$ satisfies the following *Hamilton's equations*

$$\dot{x}=\frac{\partial H_t}{\partial y},\quad \dot{y}=-\frac{\partial H_t}{\partial x}$$

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

To prove this, suppose we are given a 1-parameter family of paths $$(z_s)=(x_s,y_s)$$ satisfying the boundary conditions $$x_s(t_0)=x_0$$, $$x_s(t_1)=x_1$$, and let $$z_0=z$$. Then

$$\begin{aligned}\frac{\partial}{\partial s}\bigg|_{s=0}\mathcal{A}_H(z_s)&=\frac{\partial}{\partial s}\bigg|_{s=0}\int_{t_0}^{t_1}\langle y_s,\dot{x}_s\rangle-H_t(x_s,y_s)\mathop{dt}\\&=\int_{t_0}^{t_1}\frac{\partial}{\partial s}\bigg|_{s=0}\left(\langle y_s,\dot{x}_s\rangle-H_t(x_s,y_s)\right)\mathop{dt}\\&=\int_{t_0}^{t_1}\bigl\langle\partial_s y_s|_0,\dot{x}\bigr\rangle+\bigl\langle y,\partial_s\dot{x}|_0\bigr\rangle-\bigl\langle\partial_sx_s|_0,\partial_x H_t\bigr\rangle-\bigl\langle\partial_sy_s|_0,\partial_yH_t\bigr\rangle\mathop{dt}\end{aligned}$$

. Now integration by parts

$$\int_{t_0}^{t_1}\langle y,\partial_s\dot{x}_s|_0\rangle\mathop{dt}=\bigl[\langle y,\partial_sx_s|_0\rangle\bigr]_{t_0}^{t_1}-\int_{t_0}^{t_1}\langle\dot{y},\partial_sx_s|_0\rangle\mathop{dt}$$

gives that the first term on the right-hand side vanishes by the boundary conditions $$x_s(t_0)=x_0$$, $$x_s(t_1)=x_1$$. Substituting this into the previous equation and rearranging,

$$\frac{\partial}{\partial s}\bigg|_{s=0}\mathcal{A}_H(z)=\int_{t_0}^{t_1}\langle\partial_sy_s|_0,\dot{x}-\partial_yH_t\rangle\mathop{dt}-\int_{t_0}^{t_1}\langle\partial_sx_s|_0,\dot{y}+\partial_xH_t\rangle\mathop{dt}$$

and since $$\partial_sx_s\vert_0$$ and $$\partial_sy_s\vert_0$$ can vary arbitrarily, $$z$$ being an extremum of $$\mathcal{A}_H$$ is equivalent to the two equations

$$\dot{x}-\partial_yH_t=0,\qquad\dot{y}+\partial_xH_t=0$$

holding.

</details>

Consider the (linear) complex structure[^1] $$J_0\in\End(\mathbb{R}^{2n})$$ defined on the vector space $$\mathbb{R}^{2n}$$. With respect to the basis $$\{x_1,\ldots, x_n,y_1,\ldots, y_n\}$$, this linear map is given by the following matrix

$$J_0=\begin{pmatrix}0&-I\\I&0\end{pmatrix}$$

. This means multiplication by the imaginary unit $$i$$ when we identify $$\mathbb{R}^{2n}$$ with $$\mathbb{C}^n$$ via $$z_j:=x_j+iy_j$$. If we think of $$\mathbb{R}^{2n}$$ as a manifold and $$T_p\mathbb{R}^{2n}\cong\mathbb{R}^{2n}$$ as the tangent space at each point $$p\in\mathbb{R}^{2n}$$, then $$J_0$$ can be regarded as an element of $$\End(T\mathbb{R}^{2n})$$ defined by the formulas

$$J_0\left(\frac{\partial}{\partial x^j}\bigg|_p\right)=\frac{\partial}{\partial y^j}\bigg|_p,\qquad J_0\left(\frac{\partial}{\partial y^j}\bigg|_p\right)=-\frac{\partial}{\partial x^j}\bigg|_p\tag{1}$$

. Now

$$\nabla H=\begin{pmatrix}\partial H/\partial x\\ \partial H/\partial y\end{pmatrix}$$

, so Hamilton's equations can be written simply as

$$\dot{z}=-J_0\nabla H(z)$$

. Intuitively, the gradient $$\nabla H$$ points in the direction of greatest change of $$H$$, that is, in the direction perpendicular to the level surfaces of $$H$$, so we can think of $$\dot{z}$$ as being obtained by rotating this again by 90 degrees via $$J_0$$ to make it parallel to the level surfaces of $$H$$.

Therefore, finding the path along which the object actually moves in phase space, that is, finding $$z$$, is exactly the same as finding the integral flow of the following *Hamiltonian vector field*

$$X_H=-J_0\nabla H(z)$$

, and we know that this is always possible. ([\[Manifolds\] §Vector Fields, ⁋Theorem 6](/en/math/manifold/vector_fields#thm6))

## Symplectic Form

To summarize the above process, the Hamiltonian $$H$$ describes the motion of the object through the formula

$$dH=\langle-J_0\nabla H(z), -\rangle$$

. Now define a $$2$$-form on $$\mathbb{R}^{2n}$$ by

$$\omega_0(-,-):=\langle J_0-, -\rangle$$

. Then the above formula can be written, analogously to the definition of the gradient of a function $$f$$ via $$df=\langle\nabla f,-\rangle$$, as

$$dH=\omega_0(X_H, -)$$

. We call $$\omega_0$$ the *canonical symplectic form* defined on $$\mathbb{R}^{2n}$$, and from this point of view $$X_H$$ is sometimes called the *symplectic gradient*.

In the standard coordinate system of $$\mathbb{R}^{2n}$$,

$$\langle-,-\rangle=\sum_{j=1}^n dx^j\otimes dx^j+\sum_{j=1}^n dy^j\otimes dy^j$$

so using equation (1) we can compute $$\omega_0$$ on the basis vectors $$\partial/\partial x^j,\partial/\partial y^j$$. For example,

$$(\omega_0)_p\left(\frac{\partial}{\partial x^j}\bigg|_p,\frac{\partial}{\partial y^k}\bigg|_p\right)=\left\langle\frac{\partial}{\partial y^j}\bigg|_p,\frac{\partial}{\partial y^k}\bigg|_p\right\rangle_p=\delta_{jk}$$

, and computing the remaining basis vectors as well, we find that $$\omega_0$$ is expressed in standard coordinates as

$$\omega_0=\sum_{j=1}^n dx^j\wedge dy^j$$

. 

Before long we will see that the above discussion remains valid when we replace $$\mathbb{R}^{2n}$$ with an arbitrary manifold $$M$$ and cotangent bundle $$T^\ast M$$, Riemannian metric $$g$$, and almost complex structure $$J$$.

---

**References**

**[MS]** D. Mcduff and D. Salamon. *Introduction to symplectic topology*. Oxford graduate texts in mathematics. Oxford University Press, 2017.

---

[^1]: A *linear complex structure* defined on a vector space $$V$$ means an endomorphism $$J\in\End(V)$$ satisfying $$J^2=-\id$$. When such a $$J$$ is given, one can verify that $$V$$ acquires the structure of a $$\mathbb{C}$$-vector space via the formula $$(a+bi)\cdot v:=av+bJv$$.
