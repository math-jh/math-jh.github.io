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
last_modified_at: 2026-03-22
weight: 6

---

기하학에서 차원은 가장 기본적인 불변량 중 하나이다. 대수기하학에서도 차원은 마찬가지로 중요하며, 이를 정의하는 여러 가지 동등한 방법이 존재한다. 이 글에서 우리는 variety의 차원을 정의하는 여러 방법을 살펴본다. 

## 위상공간으로서의 차원

Algebraic variety는 이미 위상공간이므로, [§차원, ⁋정의 10](/ko/math/topology/dimension#def10)을 사용하여 $$X$$의 차원을 irreducible closed subset들의 strictly descending chain의 length의 supremum으로 정의할 수 있다. 

<div class="example" markdown="1">

<ins id="ex1">**예시 1**</ins> $$\mathbb{A}^1$$에서 닫힌집합들은 $$\mathbb{A}^1$$ 전체와 유한집합들뿐이다. 따라서 가장 긴 chain은 $$\mathbb{A}^1 \supsetneq \{p\} \supsetneq \emptyset$$이며, 이는 length $$2$$ chain이므로 $$\mathbb{A}^1$$은 이 정의에 따르면 $$1$$차원이 된다.

</div>

이 정의는 순수하게 위상적인 관점에서 차원을 정의한다는 장점이 있다. 그러나 실제로 계산을 위해서는 irreducible closed subset들의 chain을 모두 알아야하므로 그렇게 효율적이지는 않다. 

## Affine variety의 차원

한편 우리는 이미 algebraic variety와 그 위에 정의된 함수들 사이의 관계가 아주 긴밀하다는 것을 알고 있다. 그렇다면, algebraic variety 위의 함수들의 대수구조가 차원에 대한 정보를 담고있다고 하여도 그렇게 놀라운 일은 아닐 것이다. 이러한 관점을 통해 접근하려면 그 coordinate ring $$\mathbb{K}[X]$$가 깔끔하게 주어지는 *affine* variety의 경우를 보는 것이 좋을 것이다. 

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> Affine variety $$X$$의 차원은 coordinate ring $$\mathbb{K}[X]$$의 Krull dimension과 같다. ([\[가환대수학\] §차원, ⁋정의 1](/ko/math/commutative_algebra/Krull_dimension#def1))

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

[§아핀다양체, ⁋명제 12](/ko/math/algebraic_geometry/affine_varieties#prop12)로부터 affine variety의 irreducible closed subset과 $$\mathbb{K}[X]$$의 prime ideal 사이의 일대일대응이 존재한다. 

</details>
<div class="proposition" markdown="1">

<ins id="cor3">**따름정리 3**</ins> $$\dim \mathbb{A}^n = n$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

[\[가환대수학\] §매개계, ⁋정리 10](/ko/math/commutative_algebra/system_of_parameters#cor10)

</details>

한편, 우리는 임의의 prime ideal $$\mathfrak{p}\subset \mathbb{K}[\x_1,\ldots, \x_n]$$에 대하여 다음의 식

$$\dim \mathbb{K}[\x_1,\ldots, \x_n]/\mathfrak{p}+\codim \mathfrak{p}=\dim \mathbb{K}[\x_1,\ldots, \x_n]=n\tag{$\ast$}$$

이 성립하는 것을 안다. ([\[가환대수학\] §정칙국소환, ⁋명제 4](/ko/math/commutative_algebra/regular_local_rings#prop4)) 여기서 codimension $$\mathfrak{p}$$는 [\[가환대수학\] §차원, ⁋정의 2](/ko/math/commutative_algebra/Krull_dimension#def2)에서 정의된 것으로, $$\mathfrak{p}$$에 포함되는 prime ideal들의 chain의 길이의 supremum이며, 기하적으로는 $$X=Z(\mathfrak{p})$$를 포함하는 $$\mathbb{A}^n$$의 closed subvariety들의 chain의 길이의 supremum이다. 기하적으로 우리는 $$\dim \mathbb{K}[\x_1,\ldots, \x_n]/\mathfrak{p}$$이 $$Z(\mathfrak{p})$$의 차원인 것을 알고 있으므로, 이를 통해 ($\ast$)에 기하적인 의미를 부여할 수 있다. 

## Projective variety의 차원

문제는 projective variety로 넘어가면서부터 발생한다. $$\mathbb{P}^n$$의 global function은 오직 상수함수들 뿐이었음을 기억하자. 이러한 상황에서 projective variety의 차원을 정의하기 위해서는 affine chart를 잡으면 된다. 즉 $$X\subset \mathbb{P}^n$$이 주어졌을 때, $$\mathbb{P}^n$$의 affine open chart $$U_i$$를 택한 후, $$X_i=X\cap U_i$$의 affine variety로서의 차원을 생각하면 된다. 그러나 이 정의를 위해서는 임의의 열린집합의 차원이 원래 variety의 차원과 같다는 것을 보여야하므로 아직은 이를 정의로 택할 수 없다. 그 대신 우리는 $$X$$의 *affine cone* $$C(X)$$를 이용한다.

Projective variety $$X\subseteq \mathbb{P}^n$$에 대하여, affine cone $$C(X)\subseteq \mathbb{A}^{n+1}$$은 $$X$$를 정의하는 homogeneous ideal을 $$\mathbb{K}[\x_0,\ldots, \x_n]$$의 ideal로 봤을 때 이것이 정의하는 $$\mathbb{A}^{n+1}$$의 affine variety이다. 즉 $$X$$가 정의하는 homogeneous ideal $$I(X)$$에 대하여, ring $$S(X)$$를

$$S(X)=\mathbb{K}[\x_0,\ldots, \x_n]/I(X)$$

으로 정의하면 이것이 affine cone의 coordinate ring이 되는 것이다. Projective variety의 차원을 계산하기 위해 핵심적인 것은 다음의 결과이다. 

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> Projective variety $$X \subseteq \mathbb{P}^n$$에 대하여 $$\dim X = \dim S(X) - 1$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

우선 $$X$$의 irreducible closed subset chain $$X = X_0 \supsetneq \cdots \supsetneq X_r \neq \emptyset$$를 생각하자. 각 $$X_i$$에 대응하는 graded prime ideal $$\mathfrak{p}_i = I(X_i)$$들은 $$S(X)$$에서의 chain이며, 이 때 우리는 원점에 해당하는 ideal $$\mathfrak{m}=(\x_0,\ldots, \x_n)$$을 끼워넣어

$$\mathfrak{p}_0 \supsetneq \cdots \supsetneq \mathfrak{p}_r \supsetneq \mathfrak{m}$$

을 만들 수 있다. 이로부터 $$\dim S(X) \ge \dim X+ 1$$여야 함을 안다.

이제 반대방향 부등식을 보여야한다. $$S(X)$$에서 $$\mathfrak{m}$$으로 끝나는 maximal chain $$\mathfrak{p}_0 \supsetneq \cdots \supsetneq \mathfrak{p}_s = \mathfrak{m}$$을 생각하자. [\[가환대수학\] §차원, ⁋명제 10](/ko/math/commutative_algebra/Krull_dimension#prop10)에 의해 $$\mathfrak{m}$$을 포함하는 각 $$\mathfrak{p}_i$$는 homogeneous이므로, 각 $$\mathfrak{p}_i$$에 대응되는 projective subvariety $$Y_i$$를 얻을 수 있다.

$$Y_0 \supsetneq \cdots \supsetneq Y_{s-1} \neq \emptyset$$

은 $$X$$의 chain이다. 따라서 $$\dim X \ge \dim S(X) - 1$$이고 증명이 완료된다.

</details>

따라서 $$\dim C(X) = \dim X + 1$$이다. 특히 다음을 얻는다. 

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> $$\dim \mathbb{P}^n = n$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$\mathbb{P}^n$$의 cone은 $$\mathbb{A}^{n+1}$$이고 $$\dim \mathbb{A}^{n+1} = n+1$$이므로 $$\dim \mathbb{P}^n = (n+1) - 1 = n$$이다.

</details>

## 초곡면의 차원

Hypersurface는 단일 다항식의 zero set으로 정의되는 다양체이다. 이들의 차원은 쉽게 계산되는데, 이는 "하나의 방정식 = 하나의 제약 = 차원 1 감소"라는 직관을 formalize한 것이다 ([명제 6](#prop6)의 증명 참조).

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> Irreducible 다항식 $$f \in \mathbb{K}[\x_1, \ldots, \x_n]$$에 대해, irreducible 초곡면 $$V(f) \subset \mathbb{A}^n$$의 차원은 $$n - 1$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$V(f)$$의 coordinate ring은 $$\mathbb{K}[\x_1, \ldots, \x_n]/(f)$$이다. $$f$$가 irreducible 다항식이므로 $$(f)$$는 prime ideal이다. 이제 $$\mathbb{K}[\x_1, \ldots, \x_n]$$에서 $$(f)$$의 *height*—prime ideal $$(f)$$의 height는 $$(f)$$를 포함하는 prime ideal들의 strictly decreasing chain의 최대 길이를 의미한다—가 1임을 보이자. $$(0) \subsetneq (f)$$는 길이 1의 chain이므로 $$\operatorname{ht}(f) \ge 1$$이다. 반면, UFD ([§정역, ⁋정의 16](/ko/math/ring_theory/integral_domains#def16))인 $$\mathbb{K}[\x_1, \ldots, \x_n]$$에서 height가 1인 prime ideal은 모두 principal prime ideal이므로, $$(f)$$ 사이에 다른 prime ideal이 존재할 수 없다. 따라서 $$\operatorname{ht}(f) = 1$$이고,

$$\dim \mathbb{K}[\x_1, \ldots, \x_n]/(f) = \dim \mathbb{K}[\x_1, \ldots, \x_n] - \operatorname{ht}(f) = n - 1$$

이다. 일반적으로 regular local ring $$R$$과 prime ideal $$\mathfrak{p}$$에 대하여 $$\dim R/\mathfrak{p} = \dim R - \operatorname{ht}(\mathfrak{p})$$가 성립한다. ([\[가환대수학\] §정칙국소환, ⁋명제 4](/ko/math/commutative_algebra/regular_local_rings#prop4))

</details>

이 명제는 위에서 설명한 "하나의 방정식 = 차원 1 감소" 직관을 formalize한 것이다. 예를 들어 $$\mathbb{A}^3$$에서 평면 $$V(\x)$$는 2차원이고, 곡선 $$V(\x, \y)$$는 1차원이다. 이는 "codimension 1" hypersurface가 "일반적인" hypersurface임을 보여준다.

## 함수체를 통한 차원

차원을 정의하는 또 다른 방법은 함수체를 사용하는 것이다. 함수체 $$\mathbb{K}(X)$$는 다양체의 generic point에서의 정보를 담고 있으며, birational ([§유리사상, ⁋정의 9](/ko/math/algebraic_geometry/rational_maps#def9)) invariant이므로 분류에 유용하다. birationally equivalent한 두 다양체는 같은 함수체를 가지므로 같은 차원을 갖는다. 함수체가 얼마나 "자유로운지"를 측정하는 것이 바로 차원이다.

먼저 *transcendence degree*를 정의하자: field 확대 $$L/K$$에서, $$L$$의 원소들 $$\{t_1, \ldots, t_r\}$$가 $$K$$ 위에서 *algebraically independent*라는 것은 $$t_1, \ldots, t_r$$에 대한 어떤 비영다항식 $$f \in K[\t_1, \ldots, \t_r]$$에 대해서도 $$f(t_1, \ldots, t_r) \ne 0$$인 것을 의미한다. $$L/K$$의 *transcendence degree*는 $$K$$ 위에서 algebraically independent인 원소들의 최대 개수이다.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> Irreducible 다양체 $$X$$의 차원은 함수체 $$\mathbb{K}(X)$$의 $$\mathbb{K}$$ 위에서의 transcendence degree와 같다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$\mathbb{K}(X) = \operatorname{Frac}(\mathbb{K}[X])$$는 적분역 $$\mathbb{K}[X]$$의 분수체(fraction field)이고, finitely generated $$\mathbb{K}$$-algebra의 Krull dimension은 그 fraction field의 transcendence degree와 같다. 구체적으로, $$\mathbb{K}[X] = \mathbb{K}[y_1, \ldots, y_m]/I$$로 쓰면, $$\mathbb{K}(X)$$는 $$\mathbb{K}$$ 위에서 $$\dim X$$개의 algebraically independent 원소를 갖는다. 이들 $$t_1, \ldots, t_{\dim X}$$을 찾으면 $$\mathbb{K}(X)$$는 $$\mathbb{K}(t_1, \ldots, t_{\dim X})$$의 유한 확대가 된다. 이 사실의 증명은 **[Hart]** Chapter I, Theorem 1.8A를 참고하라.

</details>

이 정의의 장점은 birational ([§유리사상, ⁋정의 9](/ko/math/algebraic_geometry/rational_maps#def9)) invariant라는 것이다. 즉, birationally equivalent한 두 다양체는 같은 차원을 갖는다. 함수체가 birational equivalence를 판별하는 핵심 도구이기 때문이다. Transcendence degree는 함수체의 "자유도"를 측정하며, 이것이 바로 차원이다.

<div class="example" markdown="1">

<ins id="ex8">**예시 8**</ins> 함수체를 통한 차원 계산의 예시들이다.

1. $$\mathbb{K}(\mathbb{A}^n) = \mathbb{K}(x_1, \ldots, x_n)$$이고, $$x_1, \ldots, x_n$$은 $$\mathbb{K}$$ 위에서 대수적 독립이므로 $$\dim \mathbb{A}^n = n$$이다. 이는 $$\mathbb{A}^n$$이 $$n$$개의 "자유로운" 좌표를 가짐을 보여준다.
2. $$\mathbb{K}(V(\y - \x^2)) = \mathbb{K}(x)$$이고, $$x$$는 $$\mathbb{K}$$ 위에서 대수적 독립이므로 $$\dim V(\y - \x^2) = 1$$이다. 이는 parabola가 곡선이라는 직관과 일치한다.
3. $$\mathbb{K}(\mathbb{P}^n) = \mathbb{K}(\x_1/\x_0, \ldots, \x_n/\x_0)$$이고, $$\x_1/\x_0, \ldots, \x_n/\x_0$$는 $$\mathbb{K}$$ 위에서 대수적 독립이므로 $$\dim \mathbb{P}^n = n$$이다. 이는 projective space가 affine space와 birationally equivalent함을 반영한다.

</div>

## 차원의 기본 성질

차원의 가장 기본적인 성질은 진부분집합의 차원이 더 작다는 것이다. 이는 "더 작은" 다양체가 "더 낮은" 차원을 갖는다는 직관을 formalize한다.

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> Irreducible 다양체 $$Y \subsetneq X$$에 대해 $$\dim Y < \dim X$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$Y$$의 닫힌집합들의 최대 chain $$Y = Y_0 \supsetneq Y_1 \supsetneq \cdots \supsetneq Y_n \neq \emptyset$$을 생각하자. $$Y \subsetneq X$$이고 $$X$$는 irreducible이므로 $$Y$$는 $$X$$의 닫힌진부분집합이다. 따라서 $$X \supsetneq Y = Y_0 \supsetneq Y_1 \supsetneq \cdots \supsetneq Y_n$$은 $$X$$의 닫힌집합 chain이고, 그 길이는 $$n+1$$이다. 즉 $$\dim X \ge n + 1 > n = \dim Y$$이다.

</details>

이 명제는 irreducible 다양체의 진부분집합이 항상 더 낮은 차원을 갖는다는 것을 보여준다. 이는 "부분집합 = 더 작은 = 더 낮은 차원"이라는 직관과 일치한다.

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10**</ins> Irreducible 다양체 $$X$$와 regular map ([§준사영다양체, ⁋정의 7](/ko/math/algebraic_geometry/quasi_projective_varieties#def7)) $$\varphi: X \to Y$$에 대해 다음이 성립한다.

1. $$\dim \varphi(X) \le \dim X$$
2. 만약 $$\varphi$$가 dominant ([§유리사상, ⁋정의 8](/ko/math/algebraic_geometry/rational_maps#def8))이면 (즉, $$\overline{\varphi(X)} = Y$$), $$\dim Y \le \dim X$$
3. 만약 $$\varphi$$가 finite이면 (즉, 모든 좌표함수의 pullback이 integral dependence를 만족하는 것), $$\dim \varphi(X) = \dim X$$

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

1. $$\varphi(X)$$의 닫힌집합들의 chain $$Z_0 \supsetneq Z_1 \supsetneq \cdots \supsetneq Z_n$$을 생각하자. 그럼 $$\varphi^{-1}(Z_0) \supsetneq \varphi^{-1}(Z_1) \supsetneq \cdots \supsetneq \varphi^{-1}(Z_n)$$은 $$X$$의 닫힌집합들의 chain이다. $$\varphi^{-1}(Z_i) \ne \varphi^{-1}(Z_{i+1})$$인 것은 $$\varphi$$가 $$\varphi(X)$$ 위로 전사이고, $$Z_i \supsetneq Z_{i+1}$$에서 원상이 달라지기 때문이다. 따라서 $$\dim X \ge n = \dim \varphi(X)$$이다.

2. $$\varphi$$가 dominant이면 $$\overline{\varphi(X)} = Y$$이다. 이제 $$\mathbb{K}(Y)$$가 $$\mathbb{K}(X)$$의 subfield로 embedding됨을 보이자. $$\varphi$$는 rational map으로서 pullback $$\varphi^\ast: \mathbb{K}(Y) \to \mathbb{K}(X)$$를 정의한다: $$\varphi^\ast(g) = g \circ \varphi$$. $$\varphi$$가 dominant이므로 $$\varphi^\ast$$는 injective이다. 따라서 $$\operatorname{tr.deg}_{\mathbb{K}} \mathbb{K}(Y) \le \operatorname{tr.deg}_{\mathbb{K}} \mathbb{K}(X)$$이고, transcendence degree에 의해 $$\dim Y \le \dim X$$이다.

3. $$\varphi$$가 finite이면, 모든 $$p \in \varphi(X)$$에 대하여 $$\varphi^{-1}(p)$$는 유한집합이다. $$\varphi$$는 주어진 point에서 유한 many-to-one 이므로, coordinate ring level에서 $$\mathbb{K}[X]$$는 $$\mathbb{K}[\varphi(X)]$$-module로서 유한 생성이다. 따라서 $$\mathbb{K}(X)$$는 $$\mathbb{K}(\varphi(X))$$의 유한 확대이고, transcendence degree가 같다. 즉, $$\dim \varphi(X) = \dim X$$이다.

</details>

이 명제는 regular map이 차원을 "줄이거나 유지"할 수 있지만 "증가"시킬 수 없음을 보여준다. Dominant map은 차원을 유지하거나 줄일 수 있고, finite map은 차원을 정확히 유지한다.

<div class="example" markdown="1">

<ins id="ex11">**예시 11**</ins> **Linear subspace**: $$\mathbb{A}^n$$의 $$k$$차원 선형부분공간 $$L$$은 $$\dim L = k$$이다. 이는 $$L \cong \mathbb{A}^k$$이기 때문이다. 마찬가지로 $$\mathbb{P}^n$$의 $$k$$차원 선형부분공간 $$L$$은 $$\dim L = k$$이다. 이는 linear subspace가 "가장 간단한" $$k$$차원 다양체임을 보여준다.

</div>

<div class="example" markdown="1">

<ins id="ex12">**예시 12**</ins> **Intersection**: irreducible 다양체 $$X, Y \subseteq \mathbb{A}^n$$에 대해, 일반적으로

$$\dim(X \cap Y) \ge \dim X + \dim Y - n$$

이다. 이를 *dimension inequality*라 부른다. 등호가 성립하는 경우 (즉, $$X$$와 $$Y$$가 "일반적인 위치"에 있는 경우)를 *proper intersection*이라 부른다. 예를 들어 $$\mathbb{A}^3$$에서 두 평면의 교차는 직선이고, $$2 + 2 - 3 = 1$$이므로 proper intersection이다. 이는 intersection theory의 기본적인 결과이다.

</div>

---

**참고문헌**

**[Har]** J. Harris, *Algebraic Geometry: A First Course*, Springer, 1992.  
**[Hart]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.  
**[AM]** M. F. Atiyah and I. G. Macdonald, *Introduction to Commutative Algebra*, Addison-Wesley, 1969.
.
.
