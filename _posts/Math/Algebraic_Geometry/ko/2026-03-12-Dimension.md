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
last_modified_at: 2026-03-15
weight: 6

---

기하학에서 차원은 가장 기본적인 불변량 중 하나이다. 곡선은 1차원, 곡면은 2차원, 입체는 3차원이라는 직관은 우리가 다루는 기하학적 대상의 "크기"를 나타낸다. 대수기하학에서도 차원은 마찬가지로 중요하며, 다행히도 이를 정의하는 여러 가지 동등한 방법이 존재한다. 이 절에서 우리는 대수다양체의 차원을 위상적, 대수적, 그리고 함수체적 관점에서 정의하고, 이들이 모두 일치함을 보일 것이다.

차원의 개념은 단순해 보이지만, 대수기하학에서는 여러 가지로 정의될 수 있다. 위상적으로는 닫힌집합들의 chain으로, 대수적으로는 coordinate ring의 Krull dimension으로, 함수체적으로는 transcendence degree로 정의된다. 이들이 모두 일치한다는 것은 대수기하학의 아름다운 통일성을 보여준다.

## 위상적 차원

가장 직관적인 차원의 정의는 위상적인 것이다. 닫힌집합들의 chain의 길이를 통해 차원을 측정한다. 이는 위상공간의 "복잡도"를 닫힌집합들의 포함 관계를 통해 측정하는 방법이다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 위상공간 $$X$$의 *dimension<sub>차원</sub>* $$\dim X$$는 다음과 같이 정의된다:

- $$\dim \emptyset = -1$$
- $$\dim X \ge n$$인 것은 닫힌집합들의 strictly decreasing chain $$X = X_0 \supsetneq X_1 \supsetneq \cdots \supsetneq X_n \neq \emptyset$$이 존재하는 것이다.
- $$\dim X = n$$인 것은 $$\dim X \ge n$$이고 $$\dim X \ge n+1$$이 아닌 것이다.

</div>

즉, 차원은 닫힌집합들을 통해 얼마나 "깊이" 들어갈 수 있는지를 측정한다. 예를 들어 $$\mathbb{A}^1$$에서는 $$\mathbb{A}^1 \supsetneq \{p\} \supsetneq \emptyset$$이라는 chain이 존재하므로 $$\dim \mathbb{A}^1 \ge 1$$이고, 더 긴 chain은 존재하지 않으므로 $$\dim \mathbb{A}^1 = 1$$이다. 이 정의에서 핵심은 각 단계에서 "진정으로 작아지는" 닫힌집합들의 sequence를 찾는 것이다.

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins> $$\mathbb{A}^1$$에서 닫힌집합들은 $$\mathbb{A}^1$$ 전체와 유한집합들뿐이다. 따라서 가장 긴 chain은 $$\mathbb{A}^1 \supsetneq \{p\} \supsetneq \emptyset$$이며, 이는 길이 2 (= 차원 1)이다. 여기서 길이는 닫힌집합의 개수에서 1을 뺀 것이다. 이는 $$\mathbb{A}^1$$이 "가장 간단한" 1차원 다양체임을 보여준다.

</div>

이 정의의 장점은 순수하게 위상적이라는 것이다. 즉, 다양체의 대수적 구조에 의존하지 않는다. 그러나 이것이 실제로 계산하기 쉽지 않다는 단점이 있다. 다행히도 대수다양체의 경우, 차원을 대수적으로 계산할 수 있는 방법들이 있다. 이는 위상적 정의와 대수적 정의가 일치한다는 것을 의미하며, 대수기하학의 깊은 사실 중 하나이다.

## Coordinate Ring을 통한 차원

기역 아핀다양체 $$X$$의 경우, 차원은 coordinate ring $$\mathbb{K}[X]$$의 Krull dimension과 같다. 이는 닫힌집합들의 chain이 prime ideal들의 chain에 대응된다는 것을 이용한다. 이 대응은 Nullstellensatz에서 $$V$$와 $$I$$ 사이의 Galois connection을 통해 이루어진다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> 기역 아핀다양체 $$X$$의 차원은 coordinate ring $$\mathbb{K}[X]$$의 Krull dimension과 같다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$X$$의 닫힌집합들의 strictly decreasing chain $$X = X_0 \supsetneq X_1 \supsetneq \cdots \supsetneq X_n \neq \emptyset$$을 생각하자. 각 $$X_i$$에 대응하는 ideal $$I(X_i)$$를 생각하면, [§아핀다양체, ⁋명제 6](/ko/math/algebraic_geometry/affine_varieties#prop6)에서 $$X_i \subsetneq X_{i+1}$$일 때 $$I(X_{i+1}) \subsetneq I(X_i)$$임을 안다. 또한 $$X$$가 기역이므로 $$I(X) = (0)$$이고, 각 $$X_i$$가 기역이면 $$I(X_i)$$는 prime ideal이다. 따라서

$$(0) = I(X_0) \subsetneq I(X_1) \subsetneq \cdots \subsetneq I(X_n)$$

은 $$\mathbb{K}[X]$$의 prime ideal들의 chain이다.

역으로, $$\mathbb{K}[X]$$의 prime ideal들의 chain $$(0) = \mathfrak{p}_0 \subsetneq \mathfrak{p}_1 \subsetneq \cdots \subsetneq \mathfrak{p}_n$$이 주어지면, $$V(\mathfrak{p}_i)$$들은 $$X$$의 닫힌집합들의 strictly decreasing chain을 이룬다. 따라서 $$\dim X = \dim \mathbb{K}[X]$$이다.

</details>

이 명제는 차원을 계산하는 구체적인 방법을 제공한다. 예를 들어 $$\mathbb{K}[x_1, \ldots, x_n]$$의 Krull dimension이 $$n$$이라는 사실로부터 $$\dim \mathbb{A}^n = n$$을 얻는다. 이는 대수적 도구 (coordinate ring)를 사용하여 기하적 대상 (다양체)의 성질 (차원)을 계산할 수 있음을 보여준다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> $$\dim \mathbb{A}^n = n$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$\mathbb{K}[\x_1, \ldots, \x_n]$$의 Krull dimension은 $$n$$이다. 이는 chain

$$(0) \subsetneq (\x_1) \subsetneq (\x_1, \x_2) \subsetneq \cdots \subsetneq (\x_1, \ldots, \x_n)$$

이 길이 $$n$$의 prime ideal chain이고, 더 긴 chain이 존재하지 않기 때문이다. 자세한 증명은 [\[가환대수학\] §Krull 차원, ⁋정리 8](/ko/math/commutative_algebra/krull_dimension#thm8)를 참조하라.

</details>

이 결과는 직관적으로 타당하다. $$\mathbb{A}^n$$은 $$n$$개의 독립적인 좌표를 가지며, 각 좌표가 하나의 "자유도"를 제공한다. 따라서 $$n$$개의 좌표는 $$n$$차원을 정의한다.

## 사영다양체의 차원

사영다양체의 차원은 그 cone의 차원을 통해 정의된다. 여기서 cone이란 사영다양체를 affine space로 "역projection"한 것이다. 이는 projective space와 affine space 사이의 기하적 관계를 이용한다.

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> 사영다양체 $$X \subseteq \mathbb{P}^n$$의 *cone* $$\tilde{X} \subseteq \mathbb{A}^{n+1}$$를 다음과 같이 정의한다:

$$\tilde{X} = \{(x_0, \ldots, x_n) \in \mathbb{A}^{n+1} \mid [x_0 : \cdots : x_n] \in X\} \cup \{(0, \ldots, 0)\}$$

</div>

즉, $$\tilde{X}$$는 $$X$$의 각 점 $$[x_0 : \cdots : x_n]$$에 대응하는 모든 homogeneous representatives들의 합집합에 원점을 추가한 것이다. $$\tilde{X}$$는 원점을 지나는 cone이며, $$X = (\tilde{X} \setminus \{0\})/\mathbb{K}^\ast$$로 복원된다. 이 대응은 projective variety를 affine variety로 "lift"하는 방법을 제공한다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> 사영다양체 $$X \subseteq \mathbb{P}^n$$의 차원은 그 cone $$\tilde{X}$$의 차원에서 $$1$$을 뺀 것과 같다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$X$$의 닫힌집합들의 chain $$X = X_0 \supsetneq X_1 \supsetneq \cdots \supsetneq X_n \neq \emptyset$$을 생각하자. 각 $$X_i$$에 대응하는 cone $$\tilde{X}_i$$는 $$\mathbb{A}^{n+1}$$의 닫힌집합이고,

$$\tilde{X} = \tilde{X}_0 \supsetneq \tilde{X}_1 \supsetneq \cdots \supsetneq \tilde{X}_n \supsetneq \{0\}$$

는 $$\tilde{X}$$의 닫힌집합들의 chain이다. 여기서 $$\{0\}$$이 추가된 것은 $$\tilde{X}$$가 원점을 포함하기 때문이다. 따라서 $$\dim \tilde{X} \ge \dim X + 1$$이다.

역으로, $$\tilde{X}$$의 닫힌집합들의 chain $$\tilde{X} = Y_0 \supsetneq Y_1 \supsetneq \cdots \supsetneq Y_m \neq \emptyset$$이 주어지면, 마지막 닫힌집합 $$Y_m$$이 원점을 포함하는지 여부에 따라 두 경우로 나뉜다. 원점을 포함하면 이는 $$X$$의 chain에 대응되고, 그렇지 않으면 더 짧은 chain을 얻을 수 있다. 결과적으로 $$\dim \tilde{X} = \dim X + 1$$이다.

</details>

이 명제는 projective variety의 차원을 affine variety의 차원으로 계산할 수 있게 해준다. Cone의 차원에서 1을 빼는 것은 projective space가 "homogeneous coordinates"를 사용하므로 하나의 자유도가 줄어들기 때문이다.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> $$\dim \mathbb{P}^n = n$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$\mathbb{P}^n$$의 cone은 $$\mathbb{A}^{n+1}$$이고 $$\dim \mathbb{A}^{n+1} = n+1$$이므로 $$\dim \mathbb{P}^n = (n+1) - 1 = n$$이다.

</details>

## 초곡면의 차원

Hypersurface는 단일 다항식의 zero set으로 정의되는 다양체이다. 이들의 차원은 쉽게 계산된다. 이는 "하나의 방정식 = 하나의 제약 = 차원 1 감소"라는 직관을 formalize한다.

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> 기역 다항식 $$f \in \mathbb{K}[\x_1, \ldots, \x_n]$$에 대해, 기역 초곡면 $$V(f) \subset \mathbb{A}^n$$의 차원은 $$n - 1$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$V(f)$$의 coordinate ring은 $$\mathbb{K}[\x_1, \ldots, \x_n]/(f)$$이다. $$f$$가 기역 다항식이므로 $$(f)$$는 prime ideal이고, 그 height는 1이다 (principal prime ideal). 따라서

$$\dim \mathbb{K}[\x_1, \ldots, \x_n]/(f) = \dim \mathbb{K}[\x_1, \ldots, \x_n] - \operatorname{ht}(f) = n - 1$$

이다. 자세한 내용은 [\[가환대수학\] §Krull 차원, ⁋명제 6](/ko/math/commutative_algebra/krull_dimension#prop6)을 참조하라.

</details>

이 명제는 직관적으로 타당하다. $$\mathbb{A}^n$$에서 하나의 방정식 $$f = 0$$을 추가하면 "자유도가 하나 줄어들어" 차원이 1만큼 감소한다. 예를 들어 $$\mathbb{A}^3$$에서 평면 $$V(x)$$는 2차원이고, 곡선 $$V(x, y)$$는 1차원이다. 이는 "codimension 1" hypersurface가 "일반적인" hypersurface임을 보여준다.

## 함수체를 통한 차원

차원을 정의하는 또 다른 방법은 함수체를 사용하는 것이다. 이는 대수기하학에서 매우 자연스러운 관점이다. 함수체는 다양체 위의 "모든 rational function"들의 집합이며, 이것이 얼마나 "자유로운지"를 측정하는 것이 차원이다.

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> 기역 다양체 $$X$$의 차원은 함수체 $$\mathbb{K}(X)$$의 $$\mathbb{K}$$ 위에서의 transcendence degree와 같다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$\mathbb{K}(X) = \operatorname{Frac}(\mathbb{K}[X])$$이고, finitely generated $$\mathbb{K}$$-algebra의 Krull dimension은 그 fraction field의 transcendence degree와 같다. 구체적으로, $$\mathbb{K}[X] = \mathbb{K}[y_1, \ldots, y_m]/I$$로 쓰면, $$\mathbb{K}(X)$$는 $$\mathbb{K}$$ 위에서 $$\dim X$$개의 대수적 독립원을 갖는다. 이들 $$x_1, \ldots, x_{\dim X}$$을 찾으면 $$\mathbb{K}(X)$$는 $$\mathbb{K}(x_1, \ldots, x_{\dim X})$$의 유한확대가 된다.

</details>

이 정의의 장점은 birational invariant라는 것이다. 즉, birationally equivalent한 두 다양체는 같은 차원을 갖는다. 이는 [§유리사상](/ko/math/algebraic_geometry/rational_maps)에서 논의한 것처럼 함수체가 birational equivalence를 판별하는 핵심 도구이기 때문이다. Transcendence degree는 함수체의 "자유도"를 측정하며, 이것이 바로 차원이다.

<div class="example" markdown="1">

<ins id="ex10">**예시 10**</ins> 함수체를 통한 차원 계산의 예시들이다.

1. $$\mathbb{K}(\mathbb{A}^n) = \mathbb{K}(x_1, \ldots, x_n)$$이고, $$x_1, \ldots, x_n$$은 $$\mathbb{K}$$ 위에서 대수적 독립이므로 $$\dim \mathbb{A}^n = n$$이다. 이는 $$\mathbb{A}^n$$이 $$n$$개의 "자유로운" 좌표를 가짐을 보여준다.
2. $$\mathbb{K}(V(\y - \x^2)) = \mathbb{K}(x)$$이고, $$x$$는 $$\mathbb{K}$$ 위에서 대수적 독립이므로 $$\dim V(\y - \x^2) = 1$$이다. 이는 parabola가 곡선이라는 직관과 일치한다.
3. $$\mathbb{K}(\mathbb{P}^n) = \mathbb{K}(x_1/x_0, \ldots, x_n/x_0)$$이고, $$x_1/x_0, \ldots, x_n/x_0$$는 $$\mathbb{K}$$ 위에서 대수적 독립이므로 $$\dim \mathbb{P}^n = n$$이다. 이는 projective space가 affine space와 birationally equivalent함을 반영한다.

</div>

## 차원의 기본 성질

차원의 가장 기본적인 성질은 진부분집합의 차원이 더 작다는 것이다. 이는 "더 작은" 다양체가 "더 낮은" 차원을 갖는다는 직관을 formalize한다.

<div class="proposition" markdown="1">

<ins id="prop11">**명제 11**</ins> 기역 다양체 $$Y \subsetneq X$$에 대해 $$\dim Y < \dim X$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$Y$$의 닫힌집합들의 최대 chain $$Y = Y_0 \supsetneq Y_1 \supsetneq \cdots \supsetneq Y_n \neq \emptyset$$을 생각하자. $$Y \subsetneq X$$이고 $$X$$는 기역이므로 $$Y$$는 $$X$$의 닫힌진부분집합이다. 따라서 $$X \supsetneq Y = Y_0 \supsetneq Y_1 \supsetneq \cdots \supsetneq Y_n$$은 $$X$$의 닫힌집합 chain이고, 그 길이는 $$n+1$$이다. 즉 $$\dim X \ge n + 1 > n = \dim Y$$이다.

</details>

이 명제는 기역 다양체의 진부분집합이 항상 더 낮은 차원을 갖는다는 것을 보여준다. 이는 "부분집합 = 더 작은 = 더 낮은 차원"이라는 직관과 일치한다.

<div class="proposition" markdown="1">

<ins id="prop12">**명제 12**</ins> 기역 다양체 $$X$$와 regular map $$\varphi: X \to Y$$에 대해 다음이 성립한다.

1. $$\dim \varphi(X) \le \dim X$$
2. 만약 $$\varphi$$가 dominant이면 $$\dim Y \le \dim X$$
3. 만약 $$\varphi$$가 finite이면 $$\dim \varphi(X) = \dim X$$

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

1. $$\varphi(X)$$의 닫힌집합들의 chain $$Z_0 \supsetneq Z_1 \supsetneq \cdots \supsetneq Z_n$$을 생각하자. 그럼 $$\varphi^{-1}(Z_0) \supsetneq \varphi^{-1}(Z_1) \supsetneq \cdots \supsetneq \varphi^{-1}(Z_n)$$은 $$X$$의 닫힌집합들의 chain이다. ($$\varphi^{-1}(Z_i) \ne \varphi^{-1}(Z_{i+1})$$인 것은 $$\varphi$$가 surjective onto $$\varphi(X)$$이기 때문이다.) 따라서 $$\dim X \ge n = \dim \varphi(X)$$이다.

2. $$\varphi$$가 dominant이면 $$\overline{\varphi(X)} = Y$$이고, $$\mathbb{K}(Y)$$는 $$\mathbb{K}(X)$$의 subfield로 embedding된다. 따라서 transcendence degree에 의해 $$\dim Y \le \dim X$$이다.

3. Finite map의 경우 fiber가 유한집합이므로, "차원이 보존된다." 구체적으로, $$\mathbb{K}(X)$$가 $$\mathbb{K}(\varphi(X))$$의 유한확대이므로 transcendence degree가 같다.

</details>

이 명제는 regular map이 차원을 "줄이거나 유지"할 수 있지만 "증가"시킬 수 없음을 보여준다. Dominant map은 차원을 유지하거나 줄일 수 있고, finite map은 차원을 정확히 유지한다.

<div class="example" markdown="1">

<ins id="ex13">**예시 13**</ins> **Linear subspace**: $$\mathbb{A}^n$$의 $$k$$차원 선형부분공간 $$L$$은 $$\dim L = k$$이다. 이는 $$L \cong \mathbb{A}^k$$이기 때문이다. 마찬가지로 $$\mathbb{P}^n$$의 $$k$$차원 선형부분공간 $$L$$은 $$\dim L = k$$이다. 이는 linear subspace가 "가장 간단한" $$k$$차원 다양체임을 보여준다.

</div>

<div class="example" markdown="1">

<ins id="ex14">**예시 14**</ins> **Intersection**: 기역 다양체 $$X, Y \subseteq \mathbb{A}^n$$에 대해, 일반적으로

$$\dim(X \cap Y) \ge \dim X + \dim Y - n$$

이다. 이를 *dimension inequality*라 부른다. 등호가 성립하는 경우 (즉, $$X$$와 $$Y$$가 "일반적인 위치"에 있는 경우)를 *proper intersection*이라 부른다. 예를 들어 $$\mathbb{A}^3$$에서 두 평면의 교차는 직선이고, $$2 + 2 - 3 = 1$$이므로 proper intersection이다. 이는 intersection theory의 기본적인 결과이다.

</div>

---

**참고문헌**

**[Har]** J. Harris, *Algebraic Geometry: A First Course*, Springer, 1992.  
**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.  
**[AM]** M. F. Atiyah and I. G. Macdonald, *Introduction to Commutative Algebra*, Addison-Wesley, 1969.
