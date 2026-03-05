---
title: "아핀 토릭 다양체"
excerpt: "토릭 기하학의 시작점, 아핀 토릭 다양체의 정의와 기본 성질"

categories: [Math / Toric Geometry]
permalink: /ko/math/toric_geometry/affine_toric_varieties

header:
    overlay_image: /assets/images/Math/Toric_Geometry/affine_toric_varieties.png
    overlay_filter: 0.5

sidebar:
    nav: "toric_geometry-ko"

date: 2026-03-05
last_modified_at: 2026-03-05
weight: 1
---

## 토릭 다양체의 동기

토릭 기하학(toric geometry)은 대수적 다양체의 특별한 클래스인 **토릭 다양체(toric varieties)**를 연구하는 분야입니다. 토릭 다양체는 대수적 기하학과 볼록 기하학(convex geometry) 사이의 놀라운 연결을 제공하며, 많은 대수기하학적 문제를 조합론적인 문제로 바꾸어 해결할 수 있게 합니다.

우리는 먼저 가장 간단한 형태인 **아핀 토릭 다양체(affine toric varieties)**부터 시작합니다.

## 아핀 토릭 다양체의 정의

### 콘과 세미그룹

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> $\mathbb{R}^n$의 부분집합 $\sigma$가 다음 조건을 만족할 때 **유리 다면체 콘(rational polyhedral cone)**이라 한다:

1. $\sigma$는 $\mathbb{Q}$-선형 결합에 대해 닫혀 있다: $u, v \in \sigma$, $\lambda, \mu \in \mathbb{Q}_{\ge 0}$이면 $\lambda u + \mu v \in \sigma$
2. $\sigma$는 유한 개의 벡터 $v_1, \ldots, v_s \in \mathbb{Z}^n$의 음이 아닌 조합으로 생성된다:
   $$\sigma = \mathbb{Q}_{\ge 0} v_1 + \cdots + \mathbb{Q}_{\ge 0} v_s$$

</div>

콘 $\sigma$가 주어지면, 우리는 이에 대응하는 **쌍대 콘(dual cone)**을 정의할 수 있다:

$$\sigma^\vee = \{ u \in \mathbb{R}^n \mid \langle u, v \rangle \ge 0 \text{ for all } v \in \sigma \}$$

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> 콘 $\sigma$에 대해, **세미그룹(semigroup)** $S_\sigma$를 다음과 같이 정의한다:

$$S_\sigma = \sigma^\vee \cap \mathbb{Z}^n$$

이 세미그룹의 **세미그룹 대수(semigroup algebra)**는 다음과 같다:

$$\mathbb{C}[S_\sigma] = \mathbb{C}[x^u \mid u \in S_\sigma]$$

여기서 $x^u = x_1^{u_1} \cdots x_n^{u_n}$이다.

</div>

### 아핀 토릭 다양체

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> 유리 다면체 콘 $\sigma \subseteq \mathbb{R}^n$에 대해, **아핀 토릭 다양체(affine toric variety)** $U_\sigma$를 다음과 같이 정의한다:

$$U_\sigma = \operatorname{Spec}(\mathbb{C}[S_\sigma])$$

</div>

<div class="example" markdown="1">

<ins id="ex1">**예시 1**</ins> $\sigma = \{0\}$인 경우, $\sigma^\vee = \mathbb{R}^n$이므로 $S_\sigma = \mathbb{Z}^n$이다. 따라서:

$$\mathbb{C}[S_\sigma] = \mathbb{C}[x_1^{\pm 1}, \ldots, x_n^{\pm 1}] = \mathbb{C}[x_1, \ldots, x_n, x_1^{-1}, \ldots, x_n^{-1}]$$

이것은 **대수적 토러스(algebraic torus)** $(\mathbb{C}^\ast)^n$의 좌표환에 해당한다.

</div>

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins> $\sigma = \mathbb{Q}_{\ge 0} \cdot e_1 \subseteq \mathbb{R}^2$인 경우 (여기서 $e_1 = (1, 0)$):

$$\sigma^\vee = \{(u_1, u_2) \in \mathbb{R}^2 \mid u_1 \ge 0\}$$

따라서 $S_\sigma = \{(u_1, u_2) \in \mathbb{Z}^2 \mid u_1 \ge 0\}$이고:

$$\mathbb{C}[S_\sigma] = \mathbb{C}[x_1, x_2, x_2^{-1}]$$

이것은 $\mathbb{C} \times \mathbb{C}^\ast$의 좌표환에 해당한다.

</div>

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> $\sigma = \mathbb{Q}_{\ge 0} e_1 + \mathbb{Q}_{\ge 0} e_2 \subseteq \mathbb{R}^2$인 경우:

$$\sigma^\vee = \mathbb{Q}_{\ge 0} e_1 + \mathbb{Q}_{\ge 0} e_2$$

따라서 $S_\sigma = \mathbb{Z}_{\ge 0}^2$이고:

$$\mathbb{C}[S_\sigma] = \mathbb{C}[x_1, x_2]$$

이것은 **아핀 평면(affine plane)** $\mathbb{C}^2$의 좌표환에 해당한다.

</div>

## 토러스 작용

아핀 토릭 다양체의 중요한 성질 중 하나는 대수적 토러스의 자연스러운 작용이다.

<div class="proposition" markdown="1">

<ins id="prop1">**명제 1**</ins> 아핀 토릭 다양체 $U_\sigma$ 위에 대수적 토러스 $T = (\mathbb{C}^\ast)^n$이 다음과 같이 작용한다:

$$t \cdot (x^u)_{u \in S_\sigma} = (t^u x^u)_{u \in S_\sigma}$$

여기서 $t = (t_1, \ldots, t_n) \in T$이고 $t^u = t_1^{u_1} \cdots t_n^{u_n}$이다.

</div>

이 작용은 $U_\sigma$ 안에 **열린 조밀한(dense open)** 토러스 궤도(orbit)를 가진다. 이 궤도는 정확히 토러스 $T$ 자체이다.

## 기본 성질

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> 아핀 토릭 다양체 $U_\sigma$에 대해 다음이 성립한다:

1. $U_\sigma$는 **정규(normal)** 다양체이다.
2. $U_\sigma$는 **기약(irreducible)**이다.
3. $U_\sigma$의 차원은 $\sigma$가 포함된 $\mathbb{Q}$-선형 부분공간의 여차원과 같다.

</div>

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> 콘 $\sigma$가 **강한 정초(strongly convex)**일 때 (즉, $\sigma \cap (-\sigma) = \{0\}$), $U_\sigma$는 차원 $n$의 아핀 토릭 다양체이다.

</div>

---

## 다음 단계

아핀 토릭 다양체는 토릭 기하학의 가장 기초적인 구성 요소입니다. 다음 글에서는 여러 개의 콘을 조합하여 더 일반적인 **토릭 다양체(toric varieties)**를 구성하는 방법을 살펴볼 것입니다. 이를 위해 **팬(fan)**의 개념이 필요합니다.

---

**참고문헌**

**[Fulton]** William Fulton, *Introduction to Toric Varieties*, Annals of Mathematics Studies, Princeton University Press, 1993.  
**[CLS]** David Cox, John Little, Hal Schenck, *Toric Varieties*, Graduate Studies in Mathematics, American Mathematical Society, 2011.  
