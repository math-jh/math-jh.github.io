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

### 격자와 콘

토릭 기하학에서 기본이 되는 것은 **격자(lattice)**입니다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> **격자(lattice)** $N$은 $\mathbb{Z}^n$과 동형인 아벨 군이다. 즉, $N \cong \mathbb{Z}^n$이다. 

**쌍대 격자(dual lattice)** $M$은 $N$에서 $\mathbb{Z}$로의 준동형사상들의 그룹이다:

$$M = \operatorname{Hom}(N, \mathbb{Z})$$

$M$과 $N$ 사이의 **쌍대 페어링(dual pairing)** $\langle \cdot, \cdot \rangle: M \times N \to \mathbb{Z}$는 자연스럽게 정의된다.

</div>

우리는 종종 $N_{\mathbb{R}} = N \otimes_{\mathbb{Z}} \mathbb{R}$과 $M_{\mathbb{R}} = M \otimes_{\mathbb{Z}} \mathbb{R}$을 생각할 것이다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> $N_{\mathbb{R}}$의 부분집합 $\sigma$가 다음 조건을 만족할 때 **강한 정초 유리 다면체 콘(strongly convex rational polyhedral cone)**이라 한다:

1. $\sigma$는 원점을 꼭짓점으로 하는 콘이다: $\lambda v \in \sigma$ for all $v \in \sigma$, $\lambda \ge 0$
2. $\sigma$는 유한 개의 벡터 $v_1, \ldots, v_s \in N$의 음이 아닌 실수 조합으로 생성된다:
   $$\sigma = \mathbb{R}_{\ge 0} v_1 + \cdots + \mathbb{R}_{\ge 0} v_s$$
3. $\sigma$는 **강한 정초(strongly convex)**이다: $\sigma \cap (-\sigma) = \{0\}$

</div>

조건 3은 콘이 원점을 통과하는 직선을 포함하지 않는다는 것을 의미한다.

### 콘의 면

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> 콘 $\sigma$의 **면(face)** $\tau$는 다음과 같이 얻어진다:

$$\tau = \sigma \cap u^{\perp} = \{ v \in \sigma \mid \langle u, v \rangle = 0 \}$$

여기서 $u \in \sigma^\vee$이다. $\tau$가 $\sigma$의 면일 때 $\tau \prec \sigma$라고 쓴다.

</div>

### 세미그룹과 쌍대 콘

콘 $\sigma$가 주어지면, 우리는 이에 대응하는 **쌍대 콘(dual cone)**을 정의할 수 있다:

$$\sigma^\vee = \{ u \in M_{\mathbb{R}} \mid \langle u, v \rangle \ge 0 \text{ for all } v \in \sigma \}$$

콘 $\sigma$가 주어지면, 우리는 이에 대응하는 **쌍대 콘(dual cone)**을 정의할 수 있다:

$$\sigma^\vee = \{ u \in \mathbb{R}^n \mid \langle u, v \rangle \ge 0 \text{ for all } v \in \sigma \}$$

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> 콘 $\sigma$에 대해, **세미그룹(semigroup)** $S_\sigma$를 다음과 같이 정의한다:

$$S_\sigma = \sigma^\vee \cap M$$

이 세미그룹의 **세미그룹 대수(semigroup algebra)**는 다음과 같다:

$$\mathbb{C}[S_\sigma] = \mathbb{C}[\chi^u \mid u \in S_\sigma]$$

여기서 $\chi^u$는 문자(character)로, $M$의 원소 $u$에 대응되는 단항식이다.

</div>

### 아핀 토릭 다양체

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> 강한 정초 유리 다면체 콘 $\sigma \subseteq N_{\mathbb{R}}$에 대해, **아핀 토릭 다양체(affine toric variety)** $U_\sigma$를 다음과 같이 정의한다:

$$U_\sigma = \operatorname{Spec}(\mathbb{C}[S_\sigma])$$

</div>

<div class="example" markdown="1">

<ins id="ex1">**예시 1**</ins> $\sigma = \{0\}$인 경우, $\sigma^\vee = M_{\mathbb{R}}$이므로 $S_\sigma = M$이다. 따라서:

$$\mathbb{C}[S_\sigma] = \mathbb{C}[M] = \mathbb{C}[\chi^{\pm e_1^\ast}, \ldots, \chi^{\pm e_n^\ast}]$$

이것은 **대수적 토러스(algebraic torus)** $T_N = N \otimes_{\mathbb{Z}} \mathbb{C}^\ast \cong (\mathbb{C}^\ast)^n$의 좌표환에 해당한다.

</div>

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins> $N = \mathbb{Z}^2$에서 $\sigma$가 $e_1$과 $e_2$로 생성되는 경우:

$$\sigma^\vee = \mathbb{R}_{\ge 0} e_1^\ast + \mathbb{R}_{\ge 0} e_2^\ast$$

따라서 $S_\sigma = \mathbb{Z}_{\ge 0}^2$이고:

$$\mathbb{C}[S_\sigma] = \mathbb{C}[\chi^{e_1^\ast}, \chi^{e_2^\ast}] = \mathbb{C}[X, Y]$$

이것은 **아핀 평면(affine plane)** $\mathbb{C}^2$의 좌표환에 해당한다.

</div>

<div class="example" markdown="1">

<ins id="ex3">**예시 3 (이차 원뿔)**</ins> $N = \mathbb{Z}^2$에서 $\sigma$가 $e_2$와 $2e_1 - e_2$로 생성되는 경우를 생각하자.

$$\sigma^\vee \cap M$$의 생성원은 $e_1^\ast$, $e_1^\ast + e_2^\ast$, $e_1^\ast + 2e_2^\ast$이다. 따라서:

$$\mathbb{C}[S_\sigma] = \mathbb{C}[\chi^{e_1^\ast}, \chi^{e_1^\ast + e_2^\ast}, \chi^{e_1^\ast + 2e_2^\ast}] = \mathbb{C}[X, XY, XY^2]$$

이것을 $U = X$, $V = XY$, $W = XY^2$로 두면, $V^2 = UW$이므로:

$$\mathbb{C}[S_\sigma] \cong \mathbb{C}[U, V, W] / (V^2 - UW)$$

따라서 $U_\sigma$는 **이차 원뿔(quadric cone)**이다. 이것은 $\mathbb{C}^2$에서 원점에서의 blow-up와 관련이 있다.

</div>

## 토러스 작용

아핀 토릭 다양체의 중요한 성질 중 하나는 대수적 토러스의 자연스러운 작용이다.

<div class="proposition" markdown="1">

<ins id="prop1">**명제 1**</ins> 아핀 토릭 다양체 $U_\sigma$ 위에 대수적 토러스 $T_N = N \otimes_{\mathbb{Z}} \mathbb{C}^\ast$가 다음과 같이 작용한다:

$$t \cdot \chi^u = \chi^u(t) \cdot \chi^u$$

여기서 $t \in T_N$이고 $\chi^u(t)$는 문자 $\chi^u$의 $t$에서의 값이다.

</div>

이 작용은 $U_\sigma$ 안에 **열린 조밀한(dense open)** 토러스 궤도(orbit)를 가진다. 이 궤도는 정확히 토러스 $T_N$ 자체이다.

## 면과 열린 부분집합

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> $\tau$가 $\sigma$의 면일 때, $U_\tau$는 $U_\sigma$의 **주 열린 부분집합(principal open subset)**이다. 구체적으로, $u \in S_\sigma$를 $\tau = \sigma \cap u^{\perp}$를 만족하는 것으로 선택하면:

$$U_\tau = \{ x \in U_\sigma \mid \chi^u(x) \neq 0 \}$$

</div>

이 명제는 작은 콘이 더 작은 열린 집합에 대응된다는 것을 보여준다. 이것이 바로 $N$에서의 기하학이 $M$에서의 기하학보다 선호되는 이유이다.

## 기본 성질

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> 아핀 토릭 다양체 $U_\sigma$에 대해 다음이 성립한다:

1. $U_\sigma$는 **정규(normal)** 다양체이다.
2. $U_\sigma$는 **기약(irreducible)**이다.
3. $U_\sigma$의 차원은 $n$이다 (여기서 $N \cong \mathbb{Z}^n$).

</div>

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> 모든 아핀 토릭 다양체 $U_\sigma$는 토러스 $T_N$을 열린 조밀한 부분집합으로 포함한다.

</div>

---

## 다음 단계

아핀 토릭 다양체는 토릭 기하학의 가장 기초적인 구성 요소입니다. 다음 글에서는 여러 개의 콘을 조합하여 더 일반적인 **토릭 다양체(toric varieties)**를 구성하는 방법을 살펴볼 것입니다. 이를 위해 **팬(fan)**의 개념이 필요합니다.

---

**참고문헌**

**[Fulton]** William Fulton, *Introduction to Toric Varieties*, Annals of Mathematics Studies, Princeton University Press, 1993.  
**[CLS]** David Cox, John Little, Hal Schenck, *Toric Varieties*, Graduate Studies in Mathematics, American Mathematical Society, 2011.  
