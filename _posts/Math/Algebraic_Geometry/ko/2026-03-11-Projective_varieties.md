---
title: "사영다양체"
excerpt: "Projective varieties and homogeneous coordinates"

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/projective_varieties
sidebar: 
    nav: "algebraic_geometry-ko"

header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Projective_Varieties.png
    overlay_filter: 0.5

date: 2026-03-11
last_modified_at: 2026-03-12
weight: 2

---

[§아핀다양체](/ko/math/algebraic_geometry/affine_varieties)에서 우리는 아핀공간 $\mathbb{A}^n$과 그 위의 다항식으로 정의되는 부분집합들을 살펴보았다. 그러나 아핀공간에는 몇 가지 불편한 점이 있다. 가장 큰 문제는 "무한히 확장"되어 있어 닫힌 곡선과 같은 기하적 대상을 다루기에 적합하지 않다는 것이다. 예를 들어, $\mathbb{A}^1$에서 두 직선 $y = ax$와 $y = bx$ ($a \ne b$)는 항상 원점에서 만나지만, 평행한 두 직선은 만나지 않는다. 이는 기하학적으로 자연스럽지 않다.

사영공간 $\mathbb{P}^n$은 이러한 문제를 해결한다. 사영공간은 아핀공간에 "무한원점들"을 추가하여, 임의의 두 직선이 (평행한 경우 무한원점에서) 만나도록 만든 것이다.

## 사영공간의 정의

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 체 $\mathbb{K}$ 위의 *projective $n$-space<sub>$n$차원 사영공간</sub>* $\mathbb{P}^n_{\mathbb{K}}$를 다음과 같이 정의한다. 집합으로서

$$\mathbb{P}^n = (\mathbb{K}^{n+1} \setminus \{0\}) / \sim$$

이며, 여기서 동치관계 $\sim$은

$$(x_0, \ldots, x_n) \sim (y_0, \ldots, y_n) \iff \text{$x_i = \lambda y_i$ for some $\lambda \in \mathbb{K}^\ast$, for all $i$}$$

으로 주어진다. 혼동의 여지가 없을 때는 $\mathbb{P}^n$으로 적는다.

</div>

동치류 $[(x_0, \ldots, x_n)]$은 보통 $[x_0 : \cdots : x_n]$으로 표기하며, 이를 *homogeneous coordinates<sub>동차좌표</sub>*라 부른다. $x_0, \ldots, x_n$을 *좌표*라 하고, 이들 중 적어도 하나는 $0$이 아니어야 한다. Homogeneous coordinates의 핵심은 좌표들이 *비율*만을 결정한다는 것이다. 즉, $[x_0 : \cdots : x_n] = [\lambda x_0 : \cdots : \lambda x_n]$ for $\lambda \in \mathbb{K}^\ast$이다.

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins> $\mathbb{P}^1$의 점들:

- $[1 : 0]$, $[0 : 1]$, $[1 : 1]$, $[2 : 3]$, $[1 : 2]$, ...
- $[1 : 0]$과 $[2 : 0]$은 같은 점 ($\lambda = 2$)
- $[0 : 1]$은 "무한원점"으로 생각할 수 있음

</div>

## Standard Affine Cover

사영공간 $\mathbb{P}^n$은 $n+1$개의 아핀공간들로 덮을 수 있다. 이는 사영공간을 이해하는 가장 중요한 방법 중 하나이다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> $i = 0, 1, \ldots, n$에 대하여, *$i$번째 standard open set* $U_i$를

$$U_i = \{[x_0 : \cdots : x_n] \in \mathbb{P}^n \mid x_i \ne 0\}$$

으로 정의한다.

</div>

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> 각각의 $U_i$는 아핀공간 $\mathbb{A}^n$과 bijective하다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$U_0$의 경우, map $\varphi_0: U_0 \to \mathbb{A}^n$을

$$\varphi_0([x_0 : x_1 : \cdots : x_n]) = \left(\frac{x_1}{x_0}, \ldots, \frac{x_n}{x_0}\right)$$

으로 정의하자. 역함수 $\psi_0: \mathbb{A}^n \to U_0$는

$$\psi_0(a_1, \ldots, a_n) = [1 : a_1 : \cdots : a_n]$$

이다. 이들이 서로 역함수임은 자명하다. 일반적인 $U_i$도 비슷하게 보인다.

</details>

즉, 우리는 $U_i$를 "좌표 $x_i$가 무한대가 아닌 점들"로 생각할 수 있다. $\mathbb{P}^n = U_0 \cup \cdots \cup U_n$이고, 각 $U_i \cong \mathbb{A}^n$이다. 특히 $\mathbb{P}^n \setminus U_i = V(x_i)$는 "무한원점들"로 이루어진 *hyperplane at infinity*이다.

## Homogeneous Polynomial과 사영다양체

사영공간에서는 *homogeneous polynomial*들만이 well-defined한 zero set을 정의한다.

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> 다항식 $F \in \mathbb{K}[\x_0, \ldots, \x_n]$이 *homogeneous of degree $d$*라는 것은 모든 $\lambda \in \mathbb{K}$에 대해

$$F(\lambda \x_0, \ldots, \lambda \x_n) = \lambda^d F(\x_0, \ldots, \x_n)$$

을 만족하는 것이다.

</div>

Homogeneous polynomial $F$에 대해 $F([x_0 : \cdots : x_n])$은 잘 정의되지 않는다. 그러나 조건 $F(x_0, \ldots, x_n) = 0$은 well-defined이다. 왜냐하면

$$F(\lambda x_0, \ldots, \lambda x_n) = \lambda^d F(x_0, \ldots, x_n) = 0 \iff F(x_0, \ldots, x_n) = 0$$

이기 때문이다.

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> Homogeneous polynomials $F_1, \ldots, F_k \in \mathbb{K}[\x_0, \ldots, \x_n]$에 대하여, *projective variety<sub>사영다양체</sub>* $V(F_1, \ldots, F_k)$를

$$V(F_1, \ldots, F_k) = \{[x_0 : \cdots : x_n] \in \mathbb{P}^n \mid F_1(x) = \cdots = F_k(x) = 0\}$$

으로 정의한다.

</div>

<div class="example" markdown="1">

<ins id="ex7">**예시 7**</ins> $\mathbb{P}^2$에서의 기본적인 사영다양체들:

1. **사영직선**: $V(a_0 \x_0 + a_1 \x_1 + a_2 \x_2)$
2. **원뿔곡선<sub>conic</sub>**: $V(\x_0^2 + \x_1^2 - \x_2^2)$
3. **세 직선의 합집합**: $V(\x_0 \x_1 \x_2)$

</div>

<div class="example" markdown="1">

<ins id="ex8">**예시 8**</ins> **Veronese embedding**: $\mathbb{P}^1 \to \mathbb{P}^2$를

$$[\x : \y] \mapsto [\x^2 : \x\y : \y^2]$$

으로 정의하면, 그 image는 $V(\x_0 \x_2 - \x_1^2)$이다. 이는 conic이다.

</div>

아핀 경우와 마찬가지로, 사영다양체들을 닫힌집합으로 갖는 위상을 *Zariski topology*라 부른다. 특히 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> 다음이 성립한다.

1. $V(0) = \mathbb{P}^n$, $V(1) = \emptyset$
2. $\bigcap_\alpha V(F_\alpha) = V((F_\alpha)_\alpha)$
3. $V(F) \cup V(G) = V(FG)$

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

아핀 경우와 동일하다.

</details>

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10**</ins> $\mathbb{P}^n$은 Zariski 위상에서 quasi-compact이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Standard open cover $\mathbb{P}^n = U_0 \cup \cdots \cup U_n$을 생각하자. 각 $U_i \cong \mathbb{A}^n$은 Zariski 위상에서 quasi-compact이다. 유한개의 quasi-compact 열린집합들의 합집합은 quasi-compact이므로 $\mathbb{P}^n$은 quasi-compact이다.

</details>

## Homogeneous Ideal과 Projective Nullstellensatz

<div class="definition" markdown="1">

<ins id="def11">**정의 11**</ins> Ideal $I \subseteq \mathbb{K}[\x_0, \ldots, \x_n]$이 *homogeneous*라는 것은 $I$가 homogeneous polynomials들로 생성되는 것이다.

</div>

<div class="definition" markdown="1">

<ins id="def12">**정의 12**</ins> 부분집합 $X \subseteq \mathbb{P}^n$의 *homogeneous ideal* $I(X)$를

$$I(X) = \{F \in \mathbb{K}[\x_0, \ldots, \x_n] \mid F \text{ is homogeneous and } F(x) = 0 \text{ for all } x \in X\}$$

으로 정의한다.

</div>

<div class="theorem" markdown="1">

<ins id="thm13">**정리 13**</ins> (Projective Nullstellensatz) $\mathbb{K}$가 대수적으로 닫힌 체이고 $I \subseteq \mathbb{K}[\x_0, \ldots, \x_n]$이 homogeneous ideal이라 하자. 그럼

1. $V(I) = \emptyset \iff I \supseteq (\x_0, \ldots, \x_n)$
2. $I(V(I)) = \sqrt{I}$ (if $V(I) \ne \emptyset$)

</div>

아핀 경우와의 차이점은 $V(I) = \emptyset$이 $I = (1)$을 의미하지 않고, $I$가 *irrelevant ideal* $(\x_0, \ldots, \x_n)$을 포함하는 것을 의미한다는 점이다. 이는 $(\x_0, \ldots, \x_n)$이 $\mathbb{K}^{n+1}$의 원점에 해당하는데, 사영공간의 정의에서 원점은 제외되었기 때문이다.

## 사영다양체와 아핀다양체의 관계

<div class="proposition" markdown="1">

<ins id="prop14">**명제 14**</ins> 사영다양체 $X \subseteq \mathbb{P}^n$과 standard open set $U_i$에 대하여, $X \cap U_i$는 $U_i \cong \mathbb{A}^n$ 위의 아핀다양체이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$U_0$의 경우, $X = V(F_1, \ldots, F_k)$이고 각 $F_j$가 homogeneous of degree $d_j$라 하자. 그럼 $X \cap U_0$는 $\mathbb{A}^n$에서

$$F_j\left(1, \frac{\x_1}{\x_0}, \ldots, \frac{\x_n}{\x_0}\right) = 0, \quad j = 1, \ldots, k$$

을 만족하는 점들이다. 양변에 $\x_0^{d_j}$를 곱하면

$$\x_0^{d_j} F_j\left(1, \frac{\x_1}{\x_0}, \ldots, \frac{\x_n}{\x_0}\right) = F_j(\x_0, \x_1, \ldots, \x_n) = 0$$

이다. 이제 $f_j(\x_1, \ldots, \x_n) = F_j(1, \x_1, \ldots, \x_n)$라 두면, $X \cap U_0 = V(f_1, \ldots, f_k) \subseteq \mathbb{A}^n$이다.

</details>

<div class="example" markdown="1">

<ins id="ex15">**예시 15**</ins> $\mathbb{P}^2$에서 원 $X = V(\x_0^2 + \x_1^2 - \x_2^2)$를 생각하자. 그럼

- $X \cap U_2 = V(\x^2 + \y^2 - 1) \subset \mathbb{A}^2$ (단위원)
- $X \cap U_0 = V(1 + \y^2 - \z^2) \subset \mathbb{A}^2$ (쌍곡선)

</div>

## 사영다양체 사이의 사상

<div class="definition" markdown="1">

<ins id="def16">**정의 16**</ins> 사영다양체 $X \subseteq \mathbb{P}^n$과 $Y \subseteq \mathbb{P}^m$ 사이의 *morphism<sub>사상</sub>* $\varphi: X \to Y$는 각 점 $p \in X$에 대해 다음을 만족하는 함수이다:

적당한 homogeneous polynomials $F_0, \ldots, F_m$ of the same degree가 존재하여

$$\varphi(p) = [F_0(p) : \cdots : F_m(p)]$$

이고, 모든 $p \in X$에 대해 $F_i(p)$들이 동시에 $0$이 아니다.

</div>

<div class="example" markdown="1">

<ins id="ex17">**예시 17**</ins>

1. **항등사상**: $\mathbb{P}^n \to \mathbb{P}^n$, $[\x_0 : \cdots : \x_n] \mapsto [\x_0 : \cdots : \x_n]$
2. **Veronese embedding**: $\mathbb{P}^1 \to \mathbb{P}^2$, $[\x : \y] \mapsto [\x^2 : \x\y : \y^2]$
3. **Segre embedding**: $\mathbb{P}^1 \times \mathbb{P}^1 \to \mathbb{P}^3$, $([\x : \y], [\u : \v]) \mapsto [\x\u : \x\v : \y\u : \y\v]$

</div>

<div class="example" markdown="1">

<ins id="ex18">**예시 18**</ins> **주의**: $\mathbb{P}^1 \to \mathbb{P}^1$, $[\x : \y] \mapsto [\x : \y + 1]$은 *morphism가 아니다*. 왜냐하면 $[0 : -1]$에서 $(\x, \y + 1) = (0, 0)$이 되어 정의되지 않기 때문이다. 대신 이는 *rational map*이다.

</div>

<div class="example" markdown="1">

<ins id="ex19">**예시 19**</ins> **Twisted cubic in $\mathbb{P}^3$**: 

$$C = \{[1 : t : t^2 : t^3] \mid t \in \mathbb{K}\} \cup \{[0 : 0 : 0 : 1]\}$$

이는 세 개의 quadratic polynomials

$$\x_0 \x_2 - \x_1^2, \quad \x_0 \x_3 - \x_1 \x_2, \quad \x_1 \x_3 - \x_2^2$$

의 공통 영점이다. 이 사영다양체는 $\mathbb{P}^1$과 isomorphic하다.

</div>

---

**참고문헌**

**[Har]** J. Harris, *Algebraic Geometry: A First Course*, Springer, 1992.  
**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.  
**[Ful]** W. Fulton, *Algebraic Curves*, 2008. (Available online)
