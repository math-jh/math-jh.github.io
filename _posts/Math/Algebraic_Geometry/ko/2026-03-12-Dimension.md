---
title: "차원"
excerpt: "Dimension of algebraic varieties"

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/dimension
sidebar: 
    nav: "algebraic_geometry-ko"

header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Dimension.png
    overlay_filter: 0.5

date: 2026-03-12
last_modified_at: 2026-03-12
weight: 6

---

기하학에서 차원은 가장 기본적인 불변량 중 하나이다. 이 절에서 우리는 대수다양체의 차원을 정의하고 그 기본적인 성질들을 살펴본다.

## 위상적 차원

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 위상공간 $X$의 *dimension<sub>차원</sub>* $\dim X$는 다음 중 최솟값이다:

- $-1$ (if $X = \emptyset$)
- 닫힌집합들의 strictly decreasing chain $X_0 \supsetneq X_1 \supsetneq \cdots \supsetneq X_n \neq \emptyset$의 최대 길이 $n$

</div>

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins> $\mathbb{A}^1$에서 닫힌집합들은 $\mathbb{A}^1$과 유한집합들뿐이므로, $\dim \mathbb{A}^1 = 1$이다.

</div>

## Coordinate Ring을 통한 차원

기약 아핀다양체의 경우, 차원은 coordinate ring을 통해 계산할 수 있다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> 기약 아핀다양체 $X$의 차원은 coordinate ring $\mathbb{K}[X]$의 Krull dimension과 같다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$X$의 닫힌집합들의 chain $X_0 \supsetneq X_1 \supsetneq \cdots \supsetneq X_n$은 $\mathbb{K}[X]$의 prime ideal들의 chain $(0) \subsetneq I(X_1) \subsetneq \cdots \subsetneq I(X_{n-1})$에 대응한다. 역도 성립한다. 따라서 $\dim X = \dim \mathbb{K}[X]$이다.

</details>

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> $\dim \mathbb{A}^n = n$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$\mathbb{K}[\x_1, \ldots, \x_n]$의 Krull dimension은 $n$이다. [\[가환대수학\] §Krull 차원, ⁋정리 8](/ko/math/commutative_algebra/krull_dimension#thm8)를 참조하라.

</details>

## 사영다양체의 차원

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> 사영다양체 $X \subseteq \mathbb{P}^n$의 차원은 $X$의 *cone* $\tilde{X} \subseteq \mathbb{A}^{n+1}$의 차원에서 $1$을 뺀 것과 같다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$\tilde{X}$는 $X$의 homogeneous coordinates들의 합집합으로, 원점을 포함한다. $\tilde{X}$의 닫힌집합 chain은 $X$의 닫힌집합 chain보다 정확히 하나 더 길다 (원점에서 끝나는 chain).

</details>

<div class="corollary" markdown="1">

<ins id="cor6">**따름정리 6**</ins> $\dim \mathbb{P}^n = n$이다.

</div>

## 초곡면의 차원

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> 기약 다항식 $f \in \mathbb{K}[\x_1, \ldots, \x_n]$에 대해 $\dim V(f) = n - 1$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$\mathbb{K}[\x_1, \ldots, \x_n]/(f)$의 Krull dimension은 $n - 1$이다. 이는 $(f)$가 height $1$의 prime ideal이기 때문이다. [\[가환대수학\] §Krull 차원, ⁋명제 6](/ko/math/commutative_algebra/krull_dimension#prop6)을 참조하라.

</details>

## 함수체의 확대 차수

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> 기약 다양체 $X$의 차원은 함수체 $\mathbb{K}(X)$의 $\mathbb{K}$ 위에서의 transcendence degree와 같다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$\mathbb{K}(X) = \text{Frac}(\mathbb{K}[X])$이고, $\mathbb{K}[X]$의 Krull dimension은 transcendence degree와 같다.

</details>

<div class="example" markdown="1">

<ins id="ex9">**예시 9**</ins>

1. $\mathbb{K}(\mathbb{A}^n) = \mathbb{K}(x_1, \ldots, x_n)$이므로 $\dim \mathbb{A}^n = n$
2. $\mathbb{K}(V(y - x^2)) = \mathbb{K}(x)$이므로 $\dim V(y - x^2) = 1$
3. $\mathbb{K}(\mathbb{P}^n) = \mathbb{K}(x_1/x_0, \ldots, x_n/x_0)$이므로 $\dim \mathbb{P}^n = n$

</div>

## 차원의 성질

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10**</ins> 기약 다양체 $Y \subsetneq X$에 대해 $\dim Y < \dim X$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$Y$의 닫힌집합 chain에 $X$를 추가하면 $X$의 더 긴 chain을 얻는다.

</details>

<div class="proposition" markdown="1">

<ins id="prop11">**명제 11**</ins> 기약 다양체 $X$와 regular map $\varphi: X \to Y$에 대해:

1. $\dim \varphi(X) \le \dim X$
2. 만약 $\varphi$가 dominant이면 $\dim Y \le \dim X$

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

1. $\varphi(X)$의 닫힌집합 chain의 preimage는 $X$의 닫힌집합 chain을 준다.
2. $\varphi$가 dominant이면 $\mathbb{K}(Y) \hookrightarrow \mathbb{K}(X)$가 존재하므로 transcendence degree에 의해 $\dim Y \le \dim X$이다.

</details>

---

**참고문헌**

**[Har]** J. Harris, *Algebraic Geometry: A First Course*, Springer, 1992.  
**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.  
**[AM]** M. F. Atiyah and I. G. Macdonald, *Introduction to Commutative Algebra*, Addison-Wesley, 1969.
