---
title: "레비-치비타 접속"
description: "리만 계량과 호환되는 metric connection을 정의하고, Levi-Civita 접속의 존재와 유일성을 증명한 뒤 병렬 이송까지 다룬다."
excerpt: "리만 다양체 위의 metric-compatible torsion-free connection"

categories: [Math / Riemannian Geometry]
permalink: /ko/math/riemannian_geometry/Levi-Civita_connection
sidebar: 
    nav: "riemannian_geometry-ko"

date: 2022-12-27
weight: 3
published: false
---

[§접속](/ko/math/riemannian_geometry/connection)에서 우리는 임의의 vector bundle 위에 connection이 항상 존재한다는 것을 살펴봤지만, 그러한 connection은 일반적으로 유일하지 않다. 한편 manifold 위에 추가로 non-degenerate symmetric bilinear 자료 — 즉 (pseudo-)Riemannian metric — 이 주어지면 그것으로부터 자연스럽게 *canonical*한 connection을 하나 골라낼 수 있는데, 이 글에서는 이러한 connection — *Levi-Civita 접속* — 을 정의하고 그 존재와 유일성을 보인 뒤, 이를 통해 *parallel transport*까지 도달한다.

## 리만 계량과의 호환성

(Pseudo-)Riemannian manifold $$(M, g)$$의 tangent bundle 위의 connection $$\nabla$$가 주어졌을 때, $$\nabla$$와 $$g$$를 호환되도록 만드는 가장 자연스러운 조건은 두 vector field의 pairing이 한 vector field에 의해 미분될 때 다음의 라이프니츠 법칙을 만족하는 것이다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> (Pseudo-)Riemannian manifold $$(M, g)$$ 위의 tangent bundle $$TM$$ 위의 connection $$\nabla$$가 $$g$$와 *compatible<sub>호환된다</sub>*는 것은 임의의 vector field $$X, Y, Z \in \mathfrak{X}(M)$$에 대해 다음의 식

$$X\langle Y, Z\rangle = \langle \nabla_X Y, Z\rangle + \langle Y, \nabla_X Z\rangle$$

이 성립하는 것이다. 이러한 $$\nabla$$를 *metric connection<sub>리만 접속</sub>*이라 부른다.

</div>

위 호환성 조건은 $$g$$를 $$(0, 2)$$-tensor field로 보고 [§접속, §§Tensor field 위에서의 공변미분](/ko/math/riemannian_geometry/connection#tensor-field-위에서의-공변미분)을 따라 그 covariant derivative $$\nabla g$$를 계산했을 때 얻는 깔끔한 형태로 다시 표현된다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> (Pseudo-)Riemannian manifold $$(M, g)$$ 위의 connection $$\nabla$$에 대해, 다음의 세 조건이 동치이다.

1. $$\nabla$$는 $$g$$와 compatible이다. 즉 [정의 1](#def1)의 식이 성립한다.
2. $$\nabla g = 0$$이다. 즉 $$g$$를 $$(0, 2)$$-tensor field로 보았을 때 그 covariant derivative가 항등적으로 $$0$$이다.
3. 임의의 곡선 $$\gamma : I \to M$$과 그 위의 parallel vector field $$V, W$$에 대해 함수 $$t \mapsto \langle V(t), W(t)\rangle$$이 상수이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

(1) ⟺ (2): $$(\nabla_X g)(Y, Z) = X(g(Y, Z)) - g(\nabla_X Y, Z) - g(Y, \nabla_X Z)$$이므로, 정의 1의 식은 $$\nabla_X g = 0$$이 모든 $$X$$에 대해 성립한다는 것과 동치이다.

(1) ⟹ (3): [정의 8](#def8)에서 parallel vector field $$V$$는 $$\nabla_{\dot\gamma} V = 0$$을 만족하는 것으로 정의될 것이다. 곡선 $$\gamma$$를 따라 $$f(t) := \langle V(t), W(t)\rangle$$이라 하면 $$\dot{f}(t) = \dot\gamma\langle V, W\rangle = \langle \nabla_{\dot\gamma} V, W\rangle + \langle V, \nabla_{\dot\gamma} W\rangle = 0$$.

(3) ⟹ (1): 점 $$p \in M$$에서 임의의 vector $$X_p, Y_p, Z_p$$를 잡고, $$Y, Z$$를 $$X_p$$ 방향의 적당한 곡선을 따라 parallel transport해 vector field로 확장하면 그 곡선 위에서 $$\langle Y, Z\rangle$$이 상수이므로 양변의 미분으로부터 (1)의 식을 얻는다.

</details>

## 비틀림

Metric과의 호환성만으로는 connection이 유일하게 결정되지 않는다. 유일성을 위해 부과되는 또 하나의 자연스러운 조건이 *torsion-freeness*이다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> Manifold $$M$$ 위의 tangent bundle $$TM$$ 위의 connection $$\nabla$$의 *torsion<sub>비틀림</sub>*은 다음의 식

$$T(X, Y) := \nabla_X Y - \nabla_Y X - [X, Y]$$

로 정의된 $$\mathfrak{X}(M) \times \mathfrak{X}(M) \to \mathfrak{X}(M)$$ 함수이다. 만일 $$T \equiv 0$$이면 $$\nabla$$를 *torsion-free<sub>비틀림 없는</sub>* connection이라 부른다.

</div>

직접 계산으로부터 $$T$$는 $$X, Y$$ 둘 다에 대해 $$C^\infty$$-bilinear이며, antisymmetric 즉 $$T(X, Y) = -T(Y, X)$$이다. 따라서 $$T$$는 $$(1, 2)$$-tensor field로, 정의에 등장하는 vector field들의 *국소적인* 정보가 아닌 점별 정보만으로 결정되는 자료가 된다.

기하학적으로 $$T = 0$$ 조건은 connection coefficient $$\Gamma_{ij}^k$$가 $$i, j$$ 두 인덱스에 대해 대칭이라는 것과 동치이다. 실제로 local coordinate $$(x^i)$$에서 $$E_i = \partial/\partial x^i$$를 잡으면 $$[E_i, E_j] = 0$$이므로

$$T(E_i, E_j) = \nabla_{E_i} E_j - \nabla_{E_j} E_i = (\Gamma_{ij}^k - \Gamma_{ji}^k) E_k$$

가 되어 $$T = 0 \iff \Gamma_{ij}^k = \Gamma_{ji}^k$$를 얻는다.

## 리만 기하학의 기본 정리

이제 우리는 (pseudo-)Riemannian manifold 위에 metric-compatible torsion-free connection이 유일하게 존재한다는 것을 보인다. 이것이 *리만 기하학의 기본 정리<sub>fundamental theorem of Riemannian geometry</sub>*이다.

<div class="proposition" markdown="1">

<ins id="thm4">**정리 4 (리만 기하학의 기본 정리)**</ins> Pseudo-Riemannian manifold $$(M, g)$$ 위에 metric과 compatible하고 torsion-free인 connection $$\nabla$$이 유일하게 존재한다. 이 connection을 $$g$$의 *Levi-Civita 접속<sub>Levi-Civita connection</sub>*이라 부른다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

먼저 유일성을 보이기 위해, 그러한 $$\nabla$$가 존재한다 가정하고 임의의 vector field $$X, Y, Z$$에 대해 metric-compatibility를 세 번 적용하면

$$\begin{aligned}
X\langle Y, Z\rangle &= \langle \nabla_X Y, Z\rangle + \langle Y, \nabla_X Z\rangle \\
Y\langle Z, X\rangle &= \langle \nabla_Y Z, X\rangle + \langle Z, \nabla_Y X\rangle \\
Z\langle X, Y\rangle &= \langle \nabla_Z X, Y\rangle + \langle X, \nabla_Z Y\rangle
\end{aligned}$$

가 모두 성립한다. 첫째 둘째 식의 합에서 셋째 식을 빼고 torsion-free 조건 $$\nabla_X Y - \nabla_Y X = [X, Y]$$ 등을 정리하면 다음의 *Koszul 공식*

$$2 \langle \nabla_X Y, Z\rangle = X\langle Y, Z\rangle + Y\langle Z, X\rangle - Z\langle X, Y\rangle - \langle X, [Y, Z]\rangle + \langle Y, [Z, X]\rangle + \langle Z, [X, Y]\rangle \tag{$\ast$}$$

을 얻는다. 우변은 $$X, Y$$에만 의존하지 않고 $$Z$$에 대해서는 $$C^\infty$$-linear이므로 $$\nabla_X Y$$가 좌변에 의해 유일하게 결정된다 — 이는 $$\nabla$$의 유일성을 보장한다.

존재성을 위해서는 식 ($$\ast$$)의 우변을 $$Z$$에 대한 covector로 보고 metric duality로 vector field $$\nabla_X Y$$를 정의하면 된다. 이렇게 정의된 $$\nabla$$가 connection의 조건과 metric compatibility, torsion-freeness를 모두 만족한다는 것은 단순한 계산으로 확인된다.

</details>

위 정리의 증명 과정에서 등장한 식 ($$\ast$$)을 다시 명제로 정리해 두자.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5 (Koszul 공식)**</ins> Pseudo-Riemannian manifold $$(M, g)$$의 Levi-Civita 접속 $$\nabla$$는 다음의 식

$$2\langle \nabla_X Y, Z\rangle = X\langle Y, Z\rangle + Y\langle Z, X\rangle - Z\langle X, Y\rangle - \langle X, [Y, Z]\rangle + \langle Y, [Z, X]\rangle + \langle Z, [X, Y]\rangle$$

으로 metric으로부터 명시적으로 표현된다.

</div>

## 크리스토펠 기호

Koszul 공식은 local coordinate에서 connection coefficient를 metric으로부터 직접 계산할 수 있게 해 준다. Local coordinate $$(x^i)$$에서 $$E_i = \partial/\partial x^i$$를 잡으면 $$[E_i, E_j] = 0$$이므로 [명제 5](#prop5)에 $$X = E_i, Y = E_j, Z = E_k$$를 대입하면

$$2\langle \nabla_{E_i} E_j, E_k\rangle = E_i g_{jk} + E_j g_{ki} - E_k g_{ij}$$

가 된다. 따라서 metric $$(g_{ij})$$의 역행렬 $$(g^{ij})$$에 대해 $$\nabla_{E_i} E_j = \Gamma_{ij}^k E_k$$의 *Christoffel 기호* $$\Gamma_{ij}^k$$는 다음과 같이 명시적으로 표현된다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> Pseudo-Riemannian manifold $$(M, g)$$의 Levi-Civita 접속의 connection coefficient는 local coordinate $$(x^i)$$에서

$$\Gamma_{ij}^k = \frac{1}{2} \sum_{l=1}^n g^{kl} \left(\frac{\partial g_{jl}}{\partial x^i} + \frac{\partial g_{il}}{\partial x^j} - \frac{\partial g_{ij}}{\partial x^l}\right)$$

로 주어진다. 이를 *Christoffel 기호<sub>Christoffel symbols</sub>*라 부른다.

</div>

Christoffel 기호는 인덱스 $$i, j$$에 대해 대칭이며 ($$\Gamma_{ij}^k = \Gamma_{ji}^k$$), 이는 [정의 3](#def3) 직후의 관찰과 일치하는 결과이다.

<div class="example" markdown="1">

<ins id="ex7">**예시 7**</ins> 유클리드 공간 $$\mathbb{R}^n$$에 standard metric $$g_{ij} = \delta_{ij}$$를 주면 모든 $$\Gamma_{ij}^k = 0$$이며, Levi-Civita 접속은 표준적인 component별 미분

$$\nabla_X Y = \sum_{k=1}^n X(Y^k) \frac{\partial}{\partial x^k}$$

으로 환원된다.

</div>

## 평행 운반

Connection이 있는 임의의 vector bundle 위에서는 곡선을 따라 vector를 *상수처럼* 옮기는 자료 — *parallel transport* — 가 정의된다.

<div class="definition" markdown="1">

<ins id="def8">**정의 8**</ins> Manifold $$M$$ 위의 tangent bundle $$TM$$ 위의 connection $$\nabla$$와 smooth 곡선 $$\gamma : I \to M$$이 주어졌다 하자. $$\gamma$$ 위의 vector field $$V : I \to TM$$ (즉 $$V(t) \in T_{\gamma(t)} M$$인 smooth 함수)이 다음의 식

$$\nabla_{\dot\gamma(t)} V = 0$$

을 모든 $$t \in I$$에서 만족할 때, $$V$$를 $$\gamma$$ 위의 *parallel<sub>평행</sub>* vector field라 부른다. 주어진 초기값 $$V(t_0) = v_0 \in T_{\gamma(t_0)} M$$에 대해 위 조건을 만족하는 유일한 parallel vector field가 존재하며 (다음 명제), 이를 통해 정의된 선형 isomorphism

$$P_\gamma^{t_0, t_1} : T_{\gamma(t_0)} M \to T_{\gamma(t_1)} M, \qquad v_0 \mapsto V(t_1)$$

을 $$\gamma$$를 따른 *parallel transport<sub>평행 운반</sub>*라 부른다.

</div>

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> [정의 8](#def8)의 parallel transport는 well-defined이다. 즉 임의의 초기값 $$v_0 \in T_{\gamma(t_0)} M$$에 대해 [정의 8](#def8)의 식과 초기값 조건을 동시에 만족하는 parallel vector field $$V$$가 유일하게 존재한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

곡선 $$\gamma$$의 image 위에 local coordinate $$(x^i)$$를 잡고 $$V = \sum_k V^k(t)\, \partial/\partial x^k$$로 표현하면, $$\nabla_{\dot\gamma} V = 0$$ 조건은 

$$\dot V^k(t) + \sum_{i, j} \Gamma_{ij}^k(\gamma(t))\, \dot\gamma^i(t)\, V^j(t) = 0, \qquad k = 1, \ldots, n$$

이라는 $$n$$개의 일계 선형 ODE 시스템과 동치가 된다. 초기값 $$V^k(t_0)$$가 주어지면 ODE의 표준 이론에 의해 유일한 해가 존재한다.

</details>

Metric-compatible 접속이라는 추가 가정이 들어가면, 더 강한 성질이 따른다.

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10**</ins> $$(M, g)$$의 Levi-Civita 접속 $$\nabla$$에 대해, parallel transport $$P_\gamma^{t_0, t_1} : T_{\gamma(t_0)} M \to T_{\gamma(t_1)} M$$은 *isometry*이다. 즉 임의의 $$v, w \in T_{\gamma(t_0)} M$$에 대해

$$\langle P_\gamma^{t_0, t_1}(v), P_\gamma^{t_0, t_1}(w)\rangle = \langle v, w\rangle$$

이 성립한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$V, W$$를 $$\gamma$$ 위의 parallel vector field로 잡고 $$f(t) := \langle V(t), W(t)\rangle$$을 보면 [명제 2](#prop2)의 (3)에서 $$f$$는 상수이다.

</details>

Parallel transport는 임의의 곡선 $$\gamma$$에 대해 정의되지만, 일반적으로 두 끝점 $$p = \gamma(t_0), q = \gamma(t_1)$$ 사이에 여러 곡선이 존재하는 경우 곡선마다 다른 isomorphism $$P_\gamma^{t_0, t_1}$$이 얻어진다. 이 *path-dependence*가 어떻게 측정되는지를 다루는 자료가 [§리만 곡률](/ko/math/riemannian_geometry/curvature)에서 정의되는 *Riemann 곡률 텐서*이다.

---

**참고문헌**

**[Lee]** John M. Lee. *Introduction to Riemannian Manifolds*, Graduate texts in mathematics, Springer, 2019

---
