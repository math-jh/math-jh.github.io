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

[§아핀다양체](/ko/math/algebraic_geometry/affine_varieties)에서 우리는 affine space $$\mathbb{A}^n$$과 그 위의 다항식으로 정의되는 부분집합들을 살펴보았다. 그러나 affine space에는 몇 가지 불편한 점이 있다. 가장 큰 문제 중 하나는 일종의 compactness로, 예를 들어 $$\mathbb{A}^2$$에서 두 직선 $$y = ax$$와 $$y = bx$$ ($$a \ne b$$)는 항상 원점에서 만나지만, 평행한 두 직선은 만나지 않는다. 이를 해결하기 위해 우리는 $$\mathbb{A}^n$$의 one-point compactification을 생각할 수 있을 것이며, 이를 대수기하학의 언어로 구현하는 것이 이번 글의 목적이다. 

## 사영공간의 정의

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Field $$\mathbb{K}$$ 위의 *projective $$n$$-space<sub>$$n$$차원 사영공간</sub>* $$\mathbb{P}^n_{\mathbb{K}}$$를 다음과 같이 정의한다. 집합으로서

$$\mathbb{P}^n = (\mathbb{K}^{n+1} \setminus \{0\}) / \sim$$

이며, 여기서 동치관계 $$\sim$$은

$$(x_0, \ldots, x_n) \sim (y_0, \ldots, y_n) \iff \text{$x_i = \lambda y_i$ for some $\lambda \in \mathbb{K}^\ast$, for all $i$}$$

으로 주어진다. 혼동의 여지가 없을 때는 $$\mathbb{P}^n$$으로 적는다.

</div>

동치류 $$[(x_0, \ldots, x_n)]$$은 보통 $$[x_0 : \cdots : x_n]$$으로 표기하며, 이를 *homogeneous coordinates<sub>동차좌표</sub>*라 부른다. $$x_0, \ldots, x_n$$을 *좌표*라 하고, 이들 중 적어도 하나는 $$0$$이 아니어야 한다. Homogeneous coordinates의 핵심은 좌표들이 *비율*만을 결정한다는 것이다. 즉, $$[x_0 : \cdots : x_n] = [\lambda x_0 : \cdots : \lambda x_n]$$ for $$\lambda \in \mathbb{K}^\ast$$이다.

## 동차다항식과 사영공간

이제 우리는 affine case에서와 마찬가지로 $$\mathbb{P}^n$$에 위상구조를 주어야 한다. Projective space에서도 마찬가지로 우리는 다항식들의 zero set으로 닫힌집합을 정의할 것인데, 주의할 점은 $$\mathbb{P}^n$$은 quotient set으로 정의되었으므로 다항식이 잘 정의되지 않는다는 것이다. 즉 임의의 $$F \in \mathbb{K}[x_0, \ldots, x_n]$$에 대하여, $$[x_0 : \cdots : x_n] = [\lambda x_0 : \cdots : \lambda x_n]$$이지만 일반적으로

$$F(x_0, \ldots, x_n)\neq F(\lambda x_0, \ldots, \lambda x_n)$$

이며, 이 evaluation이 임의의 representative에 대해 잘 정의되도록 하는 유일한 다항식은 상수다항식 뿐이다. 

그러나 만일 다항식이 정의하는 zero set에만 관심을 둔다면 이 문제가 해결된다. Homogeneous polynomial $$F$$ of degree $$d$$에 대해서는

$$F(\lambda x_0, \ldots, \lambda x_n) = \lambda^d F(x_0, \ldots, x_n)$$

이므로,

$$F(\lambda x_0, \ldots, \lambda x_n) = 0 \iff F(x_0, \ldots, x_n) = 0$$

이다. 따라서 homogeneous polynomial의 zero set은 projective space에서 잘 정의된다. 

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> 다항식 $$F \in \mathbb{K}[\x_0, \ldots, \x_n]$$이 *homogeneous of degree $$d$$<sub>$d$차 동차다항식</sub>*라는 것은 모든 $$\lambda \in \mathbb{K}$$에 대해

$$F(\lambda \x_0, \ldots, \lambda \x_n) = \lambda^d F(\x_0, \ldots, \x_n)$$

을 만족하는 것이다.

</div>

정의를 복잡하게 해 두긴 했지만, 이는 본질적으로 다항식을 단항식들의 합으로 나타냈을 때, 모든 단항식이 $$d$$차라는 것이다. 그럼 다음을 정의할 수 있다. 

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> Homogeneous polynomials $$F_1, \ldots, F_k \in \mathbb{K}[\x_0, \ldots, \x_n]$$에 대하여, *projective variety<sub>사영다양체</sub>* $$V(F_1, \ldots, F_k)$$를

$$V(F_1, \ldots, F_k) = \{[x_0 : \cdots : x_n] \in \mathbb{P}^n \mid F_1(x) = \cdots = F_k(x) = 0\}$$

으로 정의한다.

</div>

위에서 설명했듯, 각각의 $$F_i$$들이 homogeneous이므로 이것이 잘 정의되는 것을 확인할 수 있다. 그럼 affine case와 마찬가지로 우리는 위상구조를 정의하기 위해 Zariski topology를 사용한다. 이를 위해서는 다음 명제가 필요하다. 

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> 다음이 성립한다.

1. $$V(0) = \mathbb{P}^n$$, $$V(1) = \emptyset$$,
2. $$\bigcap_\alpha V(F_\alpha) = V(\sum F_\alpha)$$,
3. $$V(F) \cup V(G) = V(FG)$$.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

이 증명은 affine case와 완전히 동일하다. 유일한 차이점은 여기서 다루는 다항식들이 모두 homogeneous라는 점이지만, 증명 논리 자체는 동일하다.

첫 번째 주장은 자명하다. 두 번째 주장의 경우, 점 $$[x_0 : \cdots : x_n]$$이 모든 $$V(F_\alpha)$$에 속한다는 것은 모든 $$F_\alpha(x) = 0$$이라는 것이다. 이는 ideal $$(F_\alpha)_\alpha$$의 모든 원소가 $$x$$에서 0이라는 것과 동치이다. 마지막으로 점 $$[x_0 : \cdots : x_n]$$이 $$V(F) \cup V(G)$$에 속한다는 것은 $$F(x) = 0$$ 또는 $$G(x) = 0$$이라는 것이다. Field에서 이는 $$F(x)G(x) = 0$$과 동치이다.


</details>

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> $$\mathbb{P}^n$$은 Zariski 위상에서 quasi-compact이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Standard open cover $$\mathbb{P}^n = U_0 \cup \cdots \cup U_n$$을 생각하자. 각 $$U_i \cong \mathbb{A}^n$$은 Zariski 위상에서 quasi-compact이다. 유한개의 quasi-compact 열린집합들의 합집합은 quasi-compact이므로 $$\mathbb{P}^n$$은 quasi-compact이다.

</details>

그런데 잠깐, 우리는 affine space가 compact하지 않기 때문에 projective space를 도입한다고 했는데, 위의 명제에 따르면 $$\mathbb{A}^n$$은 이미 quasi-compact가 아닌가? 물론 맞는 말이다. Zariski topology에서 $$\mathbb{A}^n$$은 quasi-compact이며, 이는 Zariski 위상이 매우 coarse하기 때문이다 (닫힌집합이 너무 적어서 compact가 되어버린다).

진정한 문제는 compactness가 아니라 **기하학적 성질**에 있다. Affine space에서는:
- 평행한 두 직선이 만나지 않는다
- 닫힌 곡선들이 "무한히 확장"되어 닫힌 곡선으로 남지 않는다

Projective space는 이 문제를 해결한다. 예를 들어 $$\mathbb{P}^2$$에서는 임의의 두 직선이 (평행한 경우 무한원점에서) 반드시 만난다. 이로 인해 닫힌 곡선들이 projective space에서도 닫힌 곡선으로 남고, Bézout의 정리와 같은 강력한 결과들을 얻을 수 있다.

## Homogeneous Ideal과 Projective Nullstellensatz

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> Ideal $$I \subseteq \mathbb{K}[\x_0, \ldots, \x_n]$$이 *homogeneous*라는 것은 $$I$$가 homogeneous polynomials들로 생성되는 것이다.

</div>

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> 부분집합 $$X \subseteq \mathbb{P}^n$$의 *homogeneous ideal* $$I(X)$$를

$$I(X) = \{F \in \mathbb{K}[\x_0, \ldots, \x_n] \mid F \text{ is homogeneous and } F(x) = 0 \text{ for all } x \in X\}$$

으로 정의한다.

</div>

<div class="proposition" markdown="1">

<ins id="thm8">**정리 8**</ins> (Projective Nullstellensatz) Field $$\mathbb{K}$$가 대수적으로 닫힌 체이고 $$I \subseteq \mathbb{K}[\x_0, \ldots, \x_n]$$이 homogeneous ideal이라 하자. 그럼

1. $$V(I) = \emptyset \iff I \supseteq (\x_0, \ldots, \x_n)$$
2. $$I(V(I)) = \sqrt{I}$$ (if $$V(I) \ne \emptyset$$)

</div>

아핀 경우와의 차이점은 $$V(I) = \emptyset$$이 $$I = (1)$$을 의미하지 않고, $$I$$가 *irrelevant ideal* $$(\x_0, \ldots, \x_n)$$을 포함하는 것을 의미한다는 점이다. 이는 $$(\x_0, \ldots, \x_n)$$이 $$\mathbb{K}^{n+1}$$의 원점에 해당하는데, projective space의 정의에서 원점은 제외되었기 때문이다.

## Standard Affine Cover

Projective space $$\mathbb{P}^n$$은 $$n+1$$개의 affine space들로 덮을 수 있다. 이는 projective space를 이해하는 가장 중요한 방법 중 하나이다.

<div class="definition" markdown="1">

<ins id="def9">**정의 9**</ins> $$i = 0, 1, \ldots, n$$에 대하여, *$$i$$번째 standard open set* $$U_i$$를

$$U_i = \{[x_0 : \cdots : x_n] \in \mathbb{P}^n \mid x_i \ne 0\}$$

으로 정의한다.

</div>

각각의 $$U_i$$에 $$\mathbb{P}^n$$으로부터 오는 subspace topology를 주자.

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10**</ins> 각각의 $$U_i$$는 (subspace topology 하에서) affine space $$\mathbb{A}^n$$과 homeomorphic하다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$U_0$$의 경우, map $$\varphi_0: U_0 \to \mathbb{A}^n$$을

$$\varphi_0([x_0 : x_1 : \cdots : x_n]) = \left(\frac{x_1}{x_0}, \ldots, \frac{x_n}{x_0}\right)$$

으로 정의하자. 역함수 $$\psi_0: \mathbb{A}^n \to U_0$$는

$$\psi_0(a_1, \ldots, a_n) = [1 : a_1 : \cdots : a_n]$$

이다. 이들이 서로 inverse이고, $$\varphi_0$$와 $$\psi_0$$ 모두 연속함수임은 자명하다. 일반적인 $$U_i$$도 비슷하게 보인다.

</details>

즉, 우리는 $$U_i$$를 "좌표 $$x_i$$가 무한대가 아닌 점들"로 생각할 수 있다. $$\mathbb{P}^n = U_0 \cup \cdots \cup U_n$$이고, 각 $$U_i \cong \mathbb{A}^n$$이다. 특히 $$\mathbb{P}^n \setminus U_i = V(x_i)$$는 "무한원점들"로 이루어진 *hyperplane at infinity*이다.

<div class="proposition" markdown="1">

<ins id="prop11">**명제 11**</ins> Projective variety $$X \subseteq \mathbb{P}^n$$과 standard open set $$U_i$$에 대하여, $$X \cap U_i$$는 $$U_i \cong \mathbb{A}^n$$ 위의 affine variety이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$U_0$$의 경우, $$X = V(F_1, \ldots, F_k)$$이고 각 $$F_j$$가 homogeneous of degree $$d_j$$라 하자. 그럼 $$X \cap U_0$$는 $$\mathbb{A}^n$$에서

$$F_j\left(1, \frac{\x_1}{\x_0}, \ldots, \frac{\x_n}{\x_0}\right) = 0, \quad j = 1, \ldots, k$$

을 만족하는 점들이다. 양변에 $$\x_0^{d_j}$$를 곱하면

$$\x_0^{d_j} F_j\left(1, \frac{\x_1}{\x_0}, \ldots, \frac{\x_n}{\x_0}\right) = F_j(\x_0, \x_1, \ldots, \x_n) = 0$$

이다. 이제 $$f_j(\x_1, \ldots, \x_n) = F_j(1, \x_1, \ldots, \x_n)$$라 두면, $$X \cap U_0 = V(f_1, \ldots, f_k) \subseteq \mathbb{A}^n$$이다.

</details>

<div class="example" markdown="1">

<ins id="ex12">**예시 12**</ins> $$\mathbb{P}^2$$에서 원 $$X = V(\x_0^2 + \x_1^2 - \x_2^2)$$를 생각하자. 그럼

- $$X \cap U_2 = V(\x^2 + \y^2 - 1) \subset \mathbb{A}^2$$ (단위원)
- $$X \cap U_0 = V(1 + \y^2 - \z^2) \subset \mathbb{A}^2$$ (쌍곡선)

</div>

## 사영다양체 사이의 사상

<div class="definition" markdown="1">

<ins id="def13">**정의 13**</ins> Projective variety $$X \subseteq \mathbb{P}^n$$과 $$Y \subseteq \mathbb{P}^m$$ 사이의 *morphism<sub>사상</sub>* $$\varphi: X \to Y$$는 각 점 $$p \in X$$에 대해 다음을 만족하는 함수이다:

적당한 homogeneous polynomials $$F_0, \ldots, F_m$$ of the same degree가 존재하여

$$\varphi(p) = [F_0(p) : \cdots : F_m(p)]$$

이고, 모든 $$p \in X$$에 대해 $$F_i(p)$$들이 동시에 $$0$$이 아니다.

</div>

<div class="example" markdown="1">

<ins id="ex14">**예시 14**</ins>

1. **항등사상**: $$\mathbb{P}^n \to \mathbb{P}^n$$, $$[\x_0 : \cdots : \x_n] \mapsto [\x_0 : \cdots : \x_n]$$
2. **Veronese embedding**: $$\mathbb{P}^1 \to \mathbb{P}^2$$, $$[\x : \y] \mapsto [\x^2 : \x\y : \y^2]$$
3. **Segre embedding**: $$\mathbb{P}^1 \times \mathbb{P}^1 \to \mathbb{P}^3$$, $$([\x : \y], [\u : \v]) \mapsto [\x\u : \x\v : \y\u : \y\v]$$

</div>

<div class="example" markdown="1">

<ins id="ex15">**예시 15**</ins> **Twisted cubic in $$\mathbb{P}^3$$**: 

$$C = \{[1 : t : t^2 : t^3] \mid t \in \mathbb{K}\} \cup \{[0 : 0 : 0 : 1]\}$$

이는 세 개의 quadratic polynomials

$$\x_0 \x_2 - \x_1^2, \quad \x_0 \x_3 - \x_1 \x_2, \quad \x_1 \x_3 - \x_2^2$$

의 공통 영점이다. 이 사영다양체는 $$\mathbb{P}^1$$과 isomorphic하다.

</div>

---

**참고문헌**

**[Har]** J. Harris, *Algebraic Geometry: A First Course*, Springer, 1992.  
**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.  
**[Ful]** W. Fulton, *Algebraic Curves*, 2008. (Available online)
