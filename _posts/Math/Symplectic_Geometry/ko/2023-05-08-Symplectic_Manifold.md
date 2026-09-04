---
title: "사교다양체"
description: "다양체 위에 정의된 사교형식의 개념을 통해 사교다양체의 정의를 다룬다. 짝수차원에서만 존재하는 사교다양체의 기본 성질과 구조를 소개한다."
excerpt: "Symplectic manifold의 정의와 성질들"

categories: [Math / Symplectic Geometry]
permalink: /ko/math/symplectic_geometry/symplectic_manifold
sidebar: 
    nav: "symplectic_geometry-ko"

date: 2023-05-08
weight: 3

---

**[MS]**에서는 symplectic vector space를 소개한 후, 시간을 좀 더 들여서 Maslov class를 소개하는 등등의 일을 한다. 우리는 이를 나중에 Floer theory를 다루며 필요할 때 소개하기로 하고, **[Cd]**를 따라 우선 symplectic manifold를 정의한다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Manifold $$M$$ 위에 정의된 *symplectic form<sub>사교형식</sub>* $$\omega$$는 $$d\omega=0$$이고 모든 $$p\in M$$에 대하여 $$\omega_p:T_pM\times T_pM\rightarrow \mathbb{R}$$이 linear symplectic form이도록 하는 differential $$2$$-form을 뜻한다. 이 때 $$(M,\omega)$$를 *symplectic manifold<sub>사교다양체</sub>*라 부른다. 

</div>

Symplectic manifold $$(M,\omega)$$에 대하여, 벡터공간 $$T_pM$$에는 linear symplectic form $$\omega_p$$가 주어져 있으므로 $$\dim T_pM$$은 짝수이고, 따라서 $$M$$ 또한 짝수차원이어야 한다. 