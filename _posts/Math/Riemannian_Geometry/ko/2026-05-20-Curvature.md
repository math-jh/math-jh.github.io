---
title: "리만 곡률"
description: "평행 운반의 경로 의존성을 점별로 측정하는 리만 곡률 텐서를 정의하고, 구면 위 측지 삼각형 예시를 통해 곡률 텐서가 홀로노미를 어떻게 지배하는지 살펴본다."
excerpt: "Parallel transport의 path-dependence를 측정하는 Riemann 곡률 텐서"

categories: [Math / Riemannian Geometry]
permalink: /ko/math/riemannian_geometry/curvature
header:
    overlay_image: /assets/images/Math/Riemannian_Geometry/Curvature.png
    overlay_filter: 0.5
sidebar: 
    nav: "riemannian_geometry-ko"

date: 2026-05-20
last_modified_at: 2026-05-20
weight: 4
published: false

---

[§레비-치비타 접속, §§평행 운반](/ko/math/riemannian_geometry/Levi-Civita_connection#def7)에서 우리는 Riemannian manifold $$(M, g)$$ 위에서 곡선 $$\gamma$$를 따라 vector를 *상수처럼* 옮기는 parallel transport $$P_\gamma$$를 정의했다. 그러나 일반적으로 같은 두 점 $$p, q$$ 사이를 잇는 두 곡선 $$\gamma_1, \gamma_2$$에 대해 $$P_{\gamma_1} \ne P_{\gamma_2}$$일 수 있다. 즉 어떤 길을 따라 vector를 옮기느냐에 따라 도착한 vector가 달라진다. 이 *path-dependence*를 점별 정보로 측정하는 텐서가 *Riemann 곡률 텐서*이다.

## 평행 운반의 path-dependence

먼저 path-dependence가 실제로 일어나는 가장 표준적인 예시를 살펴보자.

<div class="example" markdown="1">

<ins id="ex1">**예시 1**</ins> 표준 round metric을 갖춘 2차원 구면 $$S^2 \subset \mathbb{R}^3$$를 생각하고, 다음의 세 곡선으로 이루어진 *측지 삼각형* $$\gamma$$를 보자.

1. 적도 위의 점 $$p_0 = (1, 0, 0)$$에서 출발해 0° 자오선을 따라 북극 $$N = (0, 0, 1)$$으로 가는 곡선 $$\gamma_1$$.
2. 북극에서 90° 자오선을 따라 적도 위의 점 $$p_1 = (0, 1, 0)$$으로 내려오는 곡선 $$\gamma_2$$.
3. 적도를 따라 $$p_1$$에서 $$p_0$$로 돌아오는 곡선 $$\gamma_3$$.

출발점 $$p_0$$에서 적도 방향의 단위 vector $$v = (0, 1, 0) \in T_{p_0} S^2$$을 잡고 이를 $$\gamma$$를 따라 평행 운반하자.

- $$\gamma_1$$ (0° 자오선, 측지선): $$v$$는 매 순간 곡선 $$\gamma_1$$에 *수직*이므로 평행 운반 동안 적도 방향을 유지하며, 북극에서는 90° 자오선 방향의 vector $$(0, 1, 0)$$이 된다.
- $$\gamma_2$$ (90° 자오선, 측지선): 위에서 도착한 vector는 $$\gamma_2$$에 *수직*이므로 평행 운반 동안 그 수직 방향을 유지하며, $$p_1$$에서는 $$(-1, 0, 0)$$이 된다.
- $$\gamma_3$$ (적도, 측지선): 위에서 도착한 vector는 $$\gamma_3$$의 방향과 *평행*이며 (음의 방향), 평행 운반 동안 그 평행성을 유지하므로 $$p_0$$로 돌아왔을 때 여전히 $$(-1, 0, 0)$$이다.

결국 닫힌 곡선 $$\gamma_1 \cdot \gamma_2 \cdot \gamma_3$$를 따라 한 바퀴 평행 운반한 결과 초기 vector $$(0, 1, 0)$$은 $$(-1, 0, 0)$$으로, 즉 *90° 회전된* vector로 돌아온다. 

이를 다른 식으로 해석하면, $$p_0$$에서 $$p_1$$로 가는 *두 가지 path* — $$\gamma_1 \cdot \gamma_2$$로 가는 길과 $$\gamma_3$$ (의 역)으로 가는 길 — 의 parallel transport가 일치하지 않는다는 것이다. 

</div>

위 예시에서 닫힌 곡선이 둘러싸는 면적은 $$S^2$$ 전체 면적 $$4\pi$$의 $$1/8$$인 $$\pi/2$$이며, 정확히 이만큼이 회전 각도 (radian)와 일치한다. 이는 우연이 아니며, 다음에 정의할 곡률 텐서를 곡선이 둘러싸는 면적 위에서 적분한 값이 정확히 holonomy를 통제한다는 *Gauss-Bonnet*의 국소 버전의 결과이다.

## 리만 곡률 텐서

위 예시에서처럼 작은 *닫힌 곡선* (loop)를 따라 평행 운반했을 때 vector가 얼마나 회전하는지를 *무한소* 수준에서 측정하는 자료가 곡률 텐서이다. 이를 형식적으로 정의하면 다음과 같다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> Manifold $$M$$ 위의 tangent bundle $$TM$$ 위의 connection $$\nabla$$가 주어졌다 하자. $$\nabla$$의 *Riemann 곡률 텐서<sub>Riemann curvature tensor</sub>* $$R$$은 다음의 식

$$R(X, Y) Z := \nabla_X \nabla_Y Z - \nabla_Y \nabla_X Z - \nabla_{[X, Y]} Z$$

으로 정의되는 함수 $$R : \mathfrak{X}(M)^{\times 3} \to \mathfrak{X}(M)$$이다.

</div>

정의에서 $$\nabla_{[X, Y]} Z$$항이 왜 등장하는지는 다음 명제가 보여준다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> [정의 2](#def2)의 $$R$$은 세 인수 모두에 대해 $$C^\infty(M)$$-linear이다. 따라서 $$R$$은 실제로 $$M$$ 위의 $$(1, 3)$$-tensor field이며, 그 값 $$R(X, Y)Z$$의 점 $$p$$에서의 값은 $$X_p, Y_p, Z_p$$에만 의존한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$R(X, Y)$$가 $$Z$$에 대해 $$C^\infty$$-linear임을 보이는 게 비자명하다. 라이프니츠 법칙으로 풀어 쓰면

$$\begin{aligned}
\nabla_X \nabla_Y (fZ) &= \nabla_X(f \nabla_Y Z + (Yf) Z) \\
&= f \nabla_X \nabla_Y Z + (Xf)(\nabla_Y Z) + (Yf)(\nabla_X Z) + X(Yf) Z
\end{aligned}$$

이고 $$\nabla_Y \nabla_X(fZ)$$도 비슷한 식으로 풀면, 차를 취했을 때 $$X, Y$$의 미분 결과들이 $$X(Yf) - Y(Xf) = [X, Y] f$$로 정리되어

$$\nabla_X \nabla_Y(fZ) - \nabla_Y \nabla_X(fZ) = f(\nabla_X \nabla_Y Z - \nabla_Y \nabla_X Z) + ([X, Y]f) Z$$

이다. 한편 $$\nabla_{[X, Y]}(fZ) = f \nabla_{[X, Y]} Z + ([X, Y] f) Z$$이므로 그 차

$$R(X, Y)(fZ) = f \cdot R(X, Y) Z$$

가 되어 $$Z$$에 대한 $$C^\infty$$-linearity를 얻는다. $$X, Y$$에 대한 $$C^\infty$$-linearity는 비슷한 방식으로 (혹은 $$R(X, Y)Z = -R(Y, X)Z$$ 대칭과 결합해) 확인된다.

</details>

[정의 2](#def2)의 $$\nabla_{[X, Y]} Z$$항이 정확히 위 증명에서 $$[X, Y]f$$를 통해 등장하는 $$Z$$에 대한 비-$$C^\infty$$-linearity를 *상쇄*시키는 역할을 한다. 만약 이 항이 없다면 $$\nabla_X \nabla_Y - \nabla_Y \nabla_X$$는 점별 정보만으로 결정되지 않는 자료가 되고, "$$X, Y$$가 펼치는 작은 평행사변형 loop 위의 holonomy"라는 점별 정보로서의 의미가 사라진다.

## Path-dependence와의 관계

[예시 1](#ex1)의 직관에 맞춰, 곡률 텐서를 작은 loop 위의 평행 운반 holonomy의 *무한소 generator*로 해석할 수 있다. 정확한 진술은 다음과 같다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> 점 $$p \in M$$과 두 vector $$X_p, Y_p \in T_p M$$에 대해, $$\epsilon \to 0$$의 극한에서 다음이 성립한다. $$X_p, Y_p$$가 펼치는 (적절한 좌표계에서의) 면적 $$\epsilon^2$$의 작은 평행사변형 loop $$\partial D_\epsilon$$를 따른 parallel transport $$P_{\partial D_\epsilon} : T_p M \to T_p M$$는 임의의 $$Z_p \in T_p M$$에 대해

$$P_{\partial D_\epsilon}(Z_p) = Z_p - \epsilon^2 R(X_p, Y_p) Z_p + O(\epsilon^3)$$

을 만족한다. 즉 $$R(X_p, Y_p)$$는 $$X_p, Y_p$$ 방향의 무한소 loop holonomy의 *generator* (의 음수배)이다.

</div>

증명은 평행 운반 ODE를 $$\epsilon$$에 대해 두 단계 전개하는 표준적인 계산이며 [Lee, Theorem 7.3] 등에 자세히 다루어져 있다. 더 큰 disk $$D$$에 대해서는 *non-abelian Stokes* 형태로

$$P_{\partial D} \approx \exp\left(-\int_D R\right) \in \GL(T_p M)$$

이라는 근사식이 성립하는데, 우변의 적분은 $$R$$을 $$T_p M$$ 위의 endomorphism-valued $$2$$-form으로 본 것이다. $$R$$이 다음 절의 antisymmetry로 인해 자연스럽게 $$\End(TM)$$-값을 갖는 2-form으로 다루어진다는 사실이 이러한 표현의 배경이다.

## 곡률 텐서의 대칭성

곡률 텐서는 정의로부터 첫 두 인수에 대해 antisymmetric이며, Riemannian (즉 metric-compatible) 접속의 경우 추가로 더 강한 대칭성들을 만족한다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> $$(M, g)$$의 Levi-Civita 접속의 곡률 텐서 $$R$$은 다음 대칭성들을 만족한다.

1. $$R(X, Y) Z = -R(Y, X) Z$$. (정의로부터)
2. $$\langle R(X, Y) Z, W\rangle = -\langle R(X, Y) W, Z\rangle$$. (metric-compatibility로부터)
3. $$\langle R(X, Y) Z, W\rangle = \langle R(Z, W) X, Y\rangle$$. (pair 교환 대칭)
4. (제1 Bianchi 항등식) $$R(X, Y) Z + R(Y, Z) X + R(Z, X) Y = 0$$. (torsion-freeness로부터)

</div>

이 대칭성들로 인해 metric으로 lower index $$R_{ijkl} := \langle R(\partial_i, \partial_j) \partial_k, \partial_l\rangle$$로 보면, $$R_{ijkl}$$은 $$ij$$ pair에 대해 antisymmetric, $$kl$$ pair에 대해 antisymmetric, $$(ij, kl)$$ pair 교환에 대해 symmetric이며, $$R_{ijkl} + R_{ikjl} + R_{iljk} = 0$$이 성립하는 $$(0, 4)$$-tensor가 된다. 이 대칭성을 갖는 $$(0, 4)$$-tensor의 모듈러스 공간의 차원은 $$n = \dim M$$에 대해 $$n^2(n^2 - 1)/12$$로 계산되며 ($$n = 2$$일 때 1차원, $$n = 3$$일 때 6차원, $$n = 4$$일 때 20차원), 이것이 Riemannian 기하학에서의 *국소* 기하 정보의 자유도이다.

## 평탄 접속과 path-independence

[정의 2](#def2)의 $$R$$이 항등적으로 $$0$$이 되는 가장 중요한 경우를 따로 정의해 두자.

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> Connection $$\nabla$$의 곡률 텐서가 $$R \equiv 0$$일 때 $$\nabla$$를 *flat<sub>평탄</sub>* connection이라 부른다.

</div>

[명제 4](#prop4)의 직접적 결과로, flat connection 하에서는 모든 단순 연결 (simply connected) 영역 안에서 parallel transport가 *path-independent*가 된다. 즉 임의의 두 점 $$p, q$$와 그 사이의 두 곡선 $$\gamma_1, \gamma_2$$가 homotopic이면 $$P_{\gamma_1} = P_{\gamma_2}$$이다. 이는 모든 $$T_p M$$이 canonical하게 한 fixed vector space와 동일시되도록 하며, 적절한 좌표계 $$(t^1, \ldots, t^n)$$에서 $$\nabla$$가 단순 partial derivative로 환원되는 *flat coordinate*가 (국소적으로) 존재한다는 결과로 이어진다.

---

**참고문헌**

**[Lee]** John M. Lee. *Introduction to Riemannian Manifolds*, Graduate texts in mathematics, Springer, 2019

---
