---
title: "Intersection Product"
excerpt: "The intersection product on Chow groups"

categories: [Math / Algebraic Varieties]
permalink: /ko/math/algebraic_varieties/intersection_product
sidebar: 
    nav: "algebraic_varieties-ko"

header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Intersection_Product.png
    overlay_filter: 0.5

date: 2026-05-11
last_modified_at: 2026-05-11
weight: 20
published: false
---


## 도입

([§저우 군](/ko/math/algebraic_varieties/chow_groups))에서 우리는 Chow group $$\operatorname{CH}^\ast(X)$$를 정의하였다. Chow group은 variety $$X$$ 위의 cycle들을 rational equivalence로 묶은 abelian group으로, 기하학적 대상들을 대수적으로 다룰 수 있게 해 준다. 그러나 Chow group이 단순한 abelian group이 아니라는 것은 이미 여러 예시에서 암시되었다. ([§인자, ⁋정의 7](/ko/math/algebraic_varieties/divisors#def7))에서 정의한 linear equivalence는 Weil divisor들 사이의 관계였고, 이를 ([§선다발과 벡터다발, ⁋명제 19](/ko/math/algebraic_varieties/line_bundles#prop19))에서 Picard group과 연결하였다. Linear equivalence가 divisor class들 사이의 "덧셈" 구조를 준다면, 자연스럽게 떠오르는 질문은 *곱셈* 구조가 존재하는지, 즉 두 cycle을 "곱하여" 새로운 cycle을 얻을 수 있는지이다.

이 질문에 대한 답이 **intersection product**이다. 직관적으로, 두 기하학적 대상이 만나는 방식을 하나의 대상으로 기술하는 연산이다. Surface $$S$$ 위의 두 curve $$C, D$$를 생각하자. ([정의 1](#def1))에서 정의하는 intersection multiplicity $$i_p(C,D)$$를 사용하면 교차 수 $$C \cdot D = \sum_p i_p(C,D)$$를 계산할 수 있다. 이때 핵심적인 관찰은 이 정수가 $$C$$와 $$D$$의 구체적인 *위치*가 아니라 그들이 대표하는 *rational equivalence class*에만 의존한다는 것이다. 즉, $$C$$를 rational equivalence 내에서 적당히 "이동"시켜도 교차 수는 변하지 않는다. 이로부터 두 curve의 intersection은 각 curve 자체보다는 그들이 대표하는 Chow class 사이의 곱셈으로 이해되어야 한다는 것을 안다.

이는 topology에서의 상황과 완전히 같다. Singular homology group $$H_\ast(X)$$는 단순한 abelian group이 아니라 cap product에 의해 **homology ring** 구조를 갖는다. Poincaré dual을 통한 cap product가 homology class 사이의 곱셈을 주듯이, 대수기하학에서는 intersection product가 같은 역할을 한다. 실제로 ([§인자, ⁋예시 11](/ko/math/algebraic_varieties/divisors#ex11))에서 우리는 이미 $$\Cl(\mathbb{P}^n) \cong \mathbb{Z}$$임을 보았고, ([§선다발과 벡터다발, ⁋예시 12](/ko/math/algebraic_varieties/line_bundles#ex12))에서 $$\Pic(\mathbb{P}^n) \cong \mathbb{Z}$$임을 보였으므로, 이제 이들에 곱셈 구조를 주어 Chow *ring*을 완성할 차례이다.

구체적인 예로, $$\mathbb{P}^2$$에서 degree $$d_1$$ curve $$C_1$$과 degree $$d_2$$ curve $$C_2$$를 생각하자. Bézout 정리에 의해 $$C_1 \cdot C_2 = d_1 d_2$$이며, 이 결과는 두 curve의 구체적인 위치에 무관하다. 이는 오직 그들의 Chow class $$d_1[H]$$와 $$d_2[H]$$의 곱 $$d_1 d_2 H^2$$로부터 얻어진다 — 마치 ([§선형계, ⁋예시 3](/ko/math/algebraic_varieties/linear_systems#ex3))에서 degree가 곱해지듯이, intersection product에서는 Chow class가 곱해진다. 본 글은 이러한 곱셈 구조를 일반적인 smooth variety에서 엄밀하게 정의하고, 그 기본 성질들을 살펴 본다. Chow group ([§저우 군](/ko/math/algebraic_varieties/chow_groups)), intersection multiplicity ([정의 1](#def1)), line bundle ([§선다발과 벡터다발](/ko/math/algebraic_varieties/line_bundles))에 대한 기본 지식을 전제로 한다.


## Proper Intersection과 Intersection Multiplicity

## 정의

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Affine space $$\mathbb{A}^n$$의 점 $$p$$에서 두 variety $$V, W$$의 *intersection multiplicity<sub>교차 중복도</sub>* $$i_p(V, W)$$를 다음과 같이 정의한다:

$$i_p(V, W) = \dim_{\mathbb{K}} \mathcal{O}_{\mathbb{A}^n, p} / (I(V) + I(W))$$

여기서 $$\mathcal{O}_{\mathbb{A}^n, p}$$는 $$p$$에서의 local ring이다. ([\[가환대수학\] §국소화, ⁋정의 1](/ko/math/commutative_algebra/localization#def1)) 이 정의는 $$\dim V + \dim W = n$$, 즉 $$V$$와 $$W$$가 *complementary dimension*을 가지는 경우에 국한하여 사용한다. 이 조건 하에서 $$V \cap W$$는 $$p$$ 근방에서 zero-dimensional이며, [명제 5](#prop5)에서 보이듯 $$i_p(V, W)$$는 유한하다.

</div>

이 정의가 성립하려면 $$\mathcal{O}_{\mathbb{A}^n, p}/(I(V)+I(W))$$가 유한 차원 $$\mathbb{K}$$-vector space여야 한다. 이 조건은 [명제 5](#prop5)에서 다룬다.

위 정의는 $$V, W$$가 모두 local complete intersection이거나 (특히 hypersurface인 경우 자동으로 성립) Cohen–Macaulay인 경우에 정확한 교차수를 준다. 보다 일반적인 (singular한) 상황에서는 Serre의 *Tor formula*

$$i_p(V, W) = \sum_{i \ge 0} (-1)^i \dim_{\mathbb{K}} \Tor_i^{R}\bigl(R/I(V),\ R/I(W)\bigr)$$

가 올바른 정의이며, 위 정의는 그 $$i = 0$$ 항에 해당한다. 본 글에서 다루는 평면 곡선이나 hypersurface 사이의 교차에서는 두 정의가 일치하므로 위 단순한 정의로 충분하다. 일반적인 형태의 교차수는 Serre의 Tor formula로 다룬다.

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins> $$\mathbb{A}^2$$에서 $$V: y = 0$$과 $$W: y = x^2$$가 원점에서 만난다. 각 곡선을 정의하는 ideal은 $$I(V) = (y)$$, $$I(W) = (y - x^2)$$이다. 원점에서의 local ring에 대한 quotient를 계산하면 $$\mathcal{O}_{\mathbb{A}^2, 0} / (y, y - x^2) = \mathcal{O}_{\mathbb{A}^2, 0} / (y, x^2)$$이며, 이 quotient는 basis $$\{1, x\}$$를 갖는 2차원 $$\mathbb{K}$$-vector space이다. 따라서 $$i_0(V, W) = 2$$이다. 이는 곡선 $$W$$가 $$V$$ 위에서 $$x=0$$에서 order 2로 접한다는 사실과 일치한다.

</div>

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> $$\mathbb{A}^2$$에서 $$V: y = 0$$과 $$W: y = x^3$$이 원점에서 만난다.

$$\mathcal{O}_{\mathbb{A}^2, 0} / (y, x^3)$$은 basis $$\{1, x, x^2\}$$를 갖는 3차원 $$\mathbb{K}$$-vector space이다.

따라서 $$i_0(V, W) = 3$$이다. 마찬가지로 일반적으로 $$V: y = 0$$과 $$W: y = x^n$$에 대하여 $$i_0(V, W) = n$$이다.

</div>

## 기본 성질

Intersection multiplicity를 기하학적으로 의미있게 만들기 위해서는 그것이 transversal intersection이라는 개념과 어떤 관계에 있는지를 밝혀야 한다.

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> 두 variety $$V, W \subseteq \mathbb{A}^n$$이 점 $$p \in V \cap W$$에서 *transversely intersect<sub>횡단 교차</sub>*한다는 것은 tangent space의 합이 전체 공간을 채우는 것이다:

$$T_p V + T_p W = \mathbb{A}^n$$

Tangent space $$T_p V$$의 정의는 ([§접공간과 매끄러움, ⁋정의 1](/ko/math/algebraic_varieties/tangent_spaces_and_smoothness#def1))를 참조하라.

</div>

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> Intersection multiplicity는 항상 음이 아닌 정수로 정의되며, $$p \notin V \cap W$$이면 $$i_p(V, W) = 0$$이다. $$V, W$$가 $$p$$에서 transversely intersect하면 ([정의 4](#def4)) $$i_p(V, W) = 1$$이다. 또한 $$i_p(V, W) = i_p(W, V)$$가 성립한다 (symmetry). 마지막으로 $$\dim V + \dim W = n$$이면 $$i_p(V, W) < \infty$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$R = \mathcal{O}_{\mathbb{A}^n, p}$$, $$\mathfrak{a} = I(V)R$$, $$\mathfrak{b} = I(W)R$$라 하자.

먼저 명제의 마지막 주장(유한성)을 가정하면 $$i_p(V, W)$$는 유한 차원 vector space의 dimension이므로 음이 아닌 정수이다. $$p \notin V \cap W$$이면 $$p \notin V$$이거나 $$p \notin W$$이다. 만일 $$p \notin V$$이면 $$p$$에서 0이 아닌 $$f \in I(V)$$가 존재하고 (Nullstellensatz 또는 정의에 의해), 이는 local ring $$R$$에서 invertible이다. 즉 $$\mathfrak{a} + \mathfrak{b} = R$$이 되어 $$R/(\mathfrak{a} + \mathfrak{b}) = 0$$이고 $$i_p(V, W) = 0$$이다.

다음으로 횡단 교차의 경우를 보이자. $$V, W$$가 $$p$$에서 transversely intersect하면 $$T_p V + T_p W = \mathbb{A}^n$$이다. Ambient space $$\mathbb{A}^n$$의 cotangent space는 $$\mathfrak{m}_p/\mathfrak{m}_p^2$$이고, $$V$$의 tangent space는 몫 공간 $$\mathfrak{m}_p/\mathfrak{m}_p^2 \twoheadrightarrow \mathfrak{m}_p/(\mathfrak{a}+\mathfrak{m}_p^2)$$의 쌍대이다. 즉 $$T_p V = (\mathfrak{m}_p/(\mathfrak{a}+\mathfrak{m}_p^2))^\ast$$이고, 마찬가지로 $$T_p W = (\mathfrak{m}_p/(\mathfrak{b}+\mathfrak{m}_p^2))^\ast$$이다.

$$T_p V$$와 $$T_p W$$는 각각 $$T_p \mathbb{A}^n = (\mathfrak{m}_p/\mathfrak{m}_p^2)^\ast$$의 부분공간이다. $$T_p V$$의 annihilator는 $$\mathfrak{a}/(\mathfrak{a} \cap \mathfrak{m}_p^2) \cong (\mathfrak{a}+\mathfrak{m}_p^2)/\mathfrak{m}_p^2 \subseteq \mathfrak{m}_p/\mathfrak{m}_p^2$$이고, $$T_p W$$의 annihilator는 $$(\mathfrak{b}+\mathfrak{m}_p^2)/\mathfrak{m}_p^2$$이다. $$T_p V + T_p W = T_p \mathbb{A}^n$$이면 두 annihilator의 교집합이 0이고, 이것은 $$\mathfrak{a}+\mathfrak{b}$$의 $$\mathfrak{m}_p/\mathfrak{m}_p^2$$에서의 image가 전체 $$\mathfrak{m}_p/\mathfrak{m}_p^2$$임을 의미한다. 따라서 $$\mathfrak{a}+\mathfrak{b}+\mathfrak{m}_p^2 = \mathfrak{m}_p$$이고, Nakayama의 보조정리에 의해 $$\mathfrak{a}+\mathfrak{b}=\mathfrak{m}_p$$이다. 결과적으로 $$R/(\mathfrak{a}+\mathfrak{b})=R/\mathfrak{m}_p\cong\mathbb{K}$$이므로 $$i_p(V, W) = 1$$이다.

Symmetry는 $$\mathfrak{a} + \mathfrak{b} = \mathfrak{b} + \mathfrak{a}$$이므로 $$R/(\mathfrak{a} + \mathfrak{b}) \cong R/(\mathfrak{b} + \mathfrak{a})$$에서 즉시 따라온다.

마지막으로 유한성을 보이자. $$R = \mathcal{O}_{\mathbb{A}^n, p}$$는 Krull dimension $$n$$의 regular local ring이다. $$\dim V = \dim(R/\mathfrak{a})$$, $$\dim W = \dim(R/\mathfrak{b})$$이다. dimension inequality ([§차원, ⁋예시 14](/ko/math/algebraic_varieties/dimension#ex14))에 의하여
$$\dim(R/(\mathfrak{a} + \mathfrak{b})) \geq \dim(R/\mathfrak{a}) + \dim(R/\mathfrak{b}) - \dim R = \dim V + \dim W - n$$
이고, $$\dim V + \dim W = n$$이므로 $$\dim(R/(\mathfrak{a} + \mathfrak{b})) \geq 0$$이다. 한편 $$\mathfrak{a} + \mathfrak{b} \subseteq \mathfrak{m}_p$$이므로 $$R/(\mathfrak{a} + \mathfrak{b})$$의 모든 prime ideal은 $$\mathfrak{m}_p/(\mathfrak{a} + \mathfrak{b})$$에 포함된다. 즉 $$R/(\mathfrak{a} + \mathfrak{b})$$는 유일한 prime ideal $$\mathfrak{m}_p/(\mathfrak{a} + \mathfrak{b})$$를 갖는 local ring이며, 이는 $$\mathfrak{a} + \mathfrak{b}$$가 $$\mathfrak{m}_p$$-primary ideal임을 의미한다. 따라서 $$\dim(R/(\mathfrak{a} + \mathfrak{b})) \leq 0$$이고, 앞의 부등식과 합쳐 $$\dim(R/(\mathfrak{a} + \mathfrak{b})) = 0$$이다. Krull dimension $$0$$의 Noetherian local ring은 Artinian이고 ([\[가환대수학\] §차원, ⁋따름정리 3](/ko/math/commutative_algebra/Krull_dimension#cor3)), Artinian local ring은 유한 길이를 가지므로 유한 차원 $$\mathbb{K}$$-vector space이다. 특히 $$\dim_{\mathbb{K}} R/(\mathfrak{a} + \mathfrak{b}) < \infty$$이다.

</details>

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6 (Additivity)**</ins> $$\dim V + \dim W = n$$이고, $$V = V_1 \cup V_2$$이며 $$V_1$$, $$V_2$$가 $$p$$를 포함하는 공통 irreducible component를 갖지 않으면

$$i_p(V, W) = i_p(V_1, W) + i_p(V_2, W)$$

가 성립한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$R = \mathcal{O}_{\mathbb{A}^n, p}$$, $$I_1 = I(V_1)R$$, $$I_2 = I(V_2)R$$, $$J = I(W)R$$라 하자. $$V = V_1 \cup V_2$$이므로 $$I(V) = I_1 \cap I_2$$이다.

$$\bar{R} = R/J$$, $$\bar{I}_1 = (I_1 + J)/J$$, $$\bar{I}_2 = (I_2 + J)/J$$라 두면 표준적인 short exact sequence
$$0 \to \bar{R}/(\bar{I}_1 \cap \bar{I}_2) \to \bar{R}/\bar{I}_1 \oplus \bar{R}/\bar{I}_2 \to \bar{R}/(\bar{I}_1 + \bar{I}_2) \to 0$$
이 존재한다. 여기서 첫 사상은 $$\bar{a} \mapsto (\bar{a}, -\bar{a})$$, 둘째 사상은 $$(\bar{a}, \bar{b}) \mapsto \overline{a - b}$$이며, exactness는 직접 확인할 수 있다. $$\mathbb{K}$$-dimension을 비교하면
$$i_p(V, W) + \dim_{\mathbb{K}} R/(I_1 + I_2 + J) = i_p(V_1, W) + i_p(V_2, W)$$
이다.

이제 $$\dim_{\mathbb{K}} R/(I_1 + I_2 + J) = 0$$임을 보이자. 대우 논증을 이용한다. 만일 $$p \in V_1 \cap V_2 \cap W$$ 근방이라면 ([§차원, ⁋예시 14](/ko/math/algebraic_varieties/dimension#ex14))의 부등식에 의해
$$\dim_p(V_1 \cap V_2 \cap W) \geq \dim_p(V_1 \cap V_2) + \dim_p W - n$$
가 성립한다. 그런데 $$V_1$$과 $$V_2$$가 $$p$$를 포함하는 공통 irreducible component를 갖지 않으므로 $$\dim_p(V_1 \cap V_2) < \dim V$$이고, $$\dim V + \dim W = n$$이므로 우변이 음수가 되어 모순이다. 따라서 $$p \notin V_1 \cap V_2 \cap W$$ 근방이고, [명제 5](#prop5)의 첫 번째 주장에 의하여 $$\dim_{\mathbb{K}} R/(I_1 + I_2 + J) = 0$$이다. 결과적으로
$$i_p(V, W) = i_p(V_1, W) + i_p(V_2, W)$$
이다.

</details>

## Projective case

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> $$\mathbb{P}^n$$의 점 $$p$$에서 두 variety $$V, W$$의 intersection multiplicity를 affine chart에서의 값으로 정의한다. $$p$$를 포함하는 임의의 affine chart $$U \cong \mathbb{A}^n$$을 선택하고, $$V \cap U$$, $$W \cap U$$의 affine intersection multiplicity를 취한다. 이 값은 affine chart의 선택과 무관하다.

</div>

이 값이 chart의 선택과 무관한 이유는 간단하다. $$U_1, U_2$$가 $$p$$를 포함하는 두 affine chart라면, $$U_1 \cap U_2$$는 $$p$$를 포함하는 열린집합이고, local ring $$\mathcal{O}_{\mathbb{P}^n, p}$$는 $$U_1$$, $$U_2$$ 모두에서의 local ring과 자연스럽게 동형이다. Intersection multiplicity의 정의가 $$p$$에서의 local ring만에 의존하므로, chart의 선택에 영향받지 않는다.

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8 (Bézout 정리, $$\mathbb{P}^2$$의 경우)**</ins> $$\mathbb{P}^2$$에서 degree $$m$$, $$n$$의 두 curve $$C, D$$가 공통 성분을 갖지 않으면

$$\sum_{p \in C \cap D} i_p(C, D) = mn$$

이 성립한다. 여기서 curve의 degree $$\deg(C)$$는 $$C$$를 정의하는 homogeneous polynomial의 차수이다.

</div>

<details class="proof" markdown="1">
<summary>증명 (스케치)</summary>

핵심 아이디어는 resultant를 사용하는 것이다. $$C$$를 정의하는 homogeneous polynomial $$F$$와 $$D$$를 정의하는 homogeneous polynomial $$G$$에 대해, $$F$$와 $$G$$의 resultant $$\operatorname{Res}(F, G)$$를 생각하면 이것이 정확히 교차점들의 multiplicity 곱들을 인자로 갖는다. Hilbert polynomial을 사용한 degree 계산과 결합하면 총합이 $$mn$$임을 보일 수 있다. 자세한 증명은 ([§Bézout's Theorem, ⁋명제 2](/ko/math/algebraic_varieties/bezout_theorem#prop2))에서 다룬다.

</details>

<div class="example" markdown="1">

<ins id="ex9">**예시 9**</ins> 원 $$C: x^2 + y^2 = z^2$$과 직선 $$L: y = z$$을 $$\mathbb{P}^2$$에서 생각하자.

$$y = z$$를 $$x^2 + y^2 = z^2$$에 대입하면 $$x^2 = 0$$을 얻는다. 따라서 $$C \cap L$$은 한 점 $$[0:1:1]$$에서 multiplicity 2로 만난다.

한편 $$\deg C = 2$$, $$\deg L = 1$$이므로 Bézout 정리에 의해 교차점들의 multiplicity 합은 $$2 \times 1 = 2$$이어야 하며, 이는 위의 계산과 일치한다.

</div>

## Bézout 정리의 일반화

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10**</ins> $$\mathbb{P}^n$$에서 두 variety $$V, W \subseteq \mathbb{P}^n$$에 대하여, $$\dim V + \dim W = n$$이고 $$V \cap W$$가 유한집합이면

$$\sum_{p \in V \cap W} i_p(V, W) = \deg(V) \cdot \deg(W)$$

이 성립한다. 여기서 projective variety $$V$$의 degree $$\deg(V)$$는 generic hyperplane $$\dim V$$개의 교차로 얻어지는 0차원 variety에서 각 점의 intersection multiplicity의 합으로 정의된다. 즉, 일반적인 위치에 있는 hyperplane $$H_1, \ldots, H_{\dim V}$$에 대하여 $$\deg(V) = \sum_{p \in V \cap H_1 \cap \cdots \cap H_{\dim V}} i_p(V, H_1 \cap \cdots \cap H_{\dim V})$$이다. 이 값은 Hilbert polynomial의 최고차항 계수에 $$\dim(V)!$$를 곱한 것과 일치한다.

</div>

<details class="proof" markdown="1">
<summary>증명 (스케치)</summary>

Bézout 정리의 일반 형태이다. $$V, W$$를 각각 $$\deg(V)$$, $$\deg(W)$$개의 hyperplane의 intersection으로 근사한 뒤, additivity와 induction으로 증명한다. 자세한 증명은 ([§Bézout's Theorem, ⁋명제 1](/ko/math/algebraic_varieties/bezout_theorem#prop1))에서 다룬다.

</details>

## 접공간과의 관계

<div class="proposition" markdown="1">

<ins id="prop11">**명제 11**</ins> $$V, W$$가 $$p$$에서 smooth하면

$$i_p(V, W) = 1 \iff T_p V + T_p W = \mathbb{A}^n$$

이 성립한다. 즉, tangent space가 transversely intersect하면 ([정의 4](#def4)) multiplicity 1이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$R = \mathcal{O}_{\mathbb{A}^n, p}$$, $$\mathfrak{a} = I(V)R$$, $$\mathfrak{b} = I(W)R$$라 하자. $$V, W$$가 $$p$$에서 smooth하므로 $$\dim T_p V = \dim V$$, $$\dim T_p W = \dim W$$이다.

$$\Rightarrow$$ 방향: $$i_p(V, W) = 1$$이면 $$R/(\mathfrak{a} + \mathfrak{b}) \cong \mathbb{K}$$이므로 $$\mathfrak{a} + \mathfrak{b} = \mathfrak{m}_p$$이다. 따라서 $$\mathfrak{m}_p/\mathfrak{m}_p^2$$에서 $$\mathfrak{a}$$의 image와 $$\mathfrak{b}$$의 image의 합이 $$\mathfrak{m}_p/\mathfrak{m}_p^2$$ 전체이다. $$V$$의 tangent space는 $$T_p V = (\mathfrak{m}_p/(\mathfrak{a} + \mathfrak{m}_p^2))^\ast$$이고 $$T_p \mathbb{A}^n = (\mathfrak{m}_p/\mathfrak{m}_p^2)^\ast$$이며, 포함 $$T_p V \hookrightarrow T_p \mathbb{A}^n$$은 surjection $$\mathfrak{m}_p/\mathfrak{m}_p^2 \twoheadrightarrow \mathfrak{m}_p/(\mathfrak{a} + \mathfrak{m}_p^2)$$의 쌍대이다. $$T_p V \subseteq T_p \mathbb{A}^n$$의 annihilator는 $$(\mathfrak{a} + \mathfrak{m}_p^2)/\mathfrak{m}_p^2 \subseteq \mathfrak{m}_p/\mathfrak{m}_p^2$$이고, 마찬가지로 $$T_p W \subseteq T_p \mathbb{A}^n$$의 annihilator는 $$(\mathfrak{b} + \mathfrak{m}_p^2)/\mathfrak{m}_p^2$$이다. $$\mathfrak{a} + \mathfrak{b} + \mathfrak{m}_p^2 = \mathfrak{m}_p$$이므로 두 annihilator의 합이 $$\mathfrak{m}_p/\mathfrak{m}_p^2$$ 전체이고, 쌍대에서 $$T_p V + T_p W = T_p \mathbb{A}^n$$을 얻는다.

$$\Leftarrow$$ 방향: $$T_p V + T_p W = \mathbb{A}^n$$이면 [명제 5](#prop5)의 횡단 교차 증명과 동일한 논증에 의해 $$i_p(V, W) = 1$$이다.

</details>

<div class="example" markdown="1">

<ins id="ex12">**예시 12**</ins> $$V: y = 0$$과 $$W: y = x^2$$의 경우 원점에서의 tangent space를 계산해보자. $$V$$의 원점에서의 tangent space는 $$T_0 V = \{(v_1, 0)\} \cong \mathbb{K}$$이고, $$W$$의 tangent space는 $$T_0 W = \{(v_1, 0)\} \cong \mathbb{K}$$이다. 따라서 $$T_0 V + T_0 W = \mathbb{K} \neq \mathbb{K}^2$$이고, [명제 11](#prop11)에 의해 $$i_0(V, W) > 1$$이다. 실제로 [예시 2](#ex2)에서 확인했듯 $$i_0(V, W) = 2$$이다.

</div>

<div class="example" markdown="1">

<ins id="ex13">**예시 13**</ins> $$V: y = 0$$과 $$W: y = x$$의 경우 $$T_0 V = \{(v_1, 0)\}$$, $$T_0 W = \{(v_1, v_1)\}$$이므로 $$T_0 V + T_0 W = \mathbb{K}^2$$이다. 따라서 [명제 11](#prop11)에 의해 $$i_0(V, W) = 1$$이다. 이를 직접 확인하면 $$\mathcal{O}_{\mathbb{A}^2,0}/(y, y-x) = \mathcal{O}_{\mathbb{A}^2,0}/(y,x) \cong \mathbb{K}$$로 1차원 vector space가 된다.

</div>


## Intersection Product의 정의

이제 proper intersection에서의 계산을 바탕으로, 일반적인 두 cycle에 대해 intersection product를 정의한다. 문제는 일반적으로 두 subvariety가 properly intersect하지 않는다는 것이다. 가령 $$\mathbb{P}^3$$에서 두 surface가 curve를 공유하면, 이 curve의 codimension은 $$1 + 1 = 2$$가 아닌 $$1$$이 되어 proper intersection이 아니다.

<div class="proposition" markdown="1">

<ins id="prop14">**명제 14 (Intersection Product)**</ins> Smooth irreducible variety $$X$$ 위에서 codimension $$k$$, $$l$$의 두 cycle $$Z, W$$의 **intersection product** $$Z \cdot W \in \operatorname{CH}^{k+l}(X)$$를 정의할 수 있다. 이 연산은 교환법칙 $$Z \cdot W = W \cdot Z$$, 결합법칙 $$(Z_1 \cdot Z_2) \cdot Z_3 = Z_1 \cdot (Z_2 \cdot Z_3)$$, 분배법칙 $$Z \cdot (W_1 + W_2) = Z \cdot W_1 + Z \cdot W_2$$을 만족하며, $$[X] \in \operatorname{CH}^0(X)$$가 항등원 역할을 한다.

</div>

<details class="proof" markdown="1">
<summary>증명 (스케치)</summary>

핵심은 정의가 cycle의 rational equivalence class에만 의존한다는 것이다. Quasi-projective variety의 경우 moving lemma([명제 16](#prop16))에 의해 $$Z$$를 rationally equivalent한 $$Z'$$로 이동시켜 $$W$$와 properly intersect하도록 할 수 있으며, 두 이동 $$Z'_1, Z'_2$$가 주어지면 $$Z'_1 - Z'_2 = \divisor(f)$$인 rational function $$f$$가 존재한다. 이때 $$\divisor(f)$$와 $$W$$의 교차가 rational equivalence에서 $$0$$이 됨을 보이면 $$Z'_1 \cdot W = Z'_2 \cdot W$$가 성립한다. 일반적인 scheme의 경우 Fulton의 deformation to normal cone([명제 19](#prop19))을 사용하여 well-definedness를 pushforward-pullback의 호환성으로 환원한다. 교환법칙은 Serre의 Tor formula의 대칭성으로부터, 결합법칙은 세 cycle의 이동이 독립적으로 가능하다는 사실로부터 따른다.

</details>

Intersection product를 정의하는 핵심 아이디어는 주어진 cycle $$Z \in \operatorname{CH}^k(X)$$와 $$W \in \operatorname{CH}^l(X)$$에 대해, $$Z$$를 rational equivalence 내에서 적절히 "이동"시켜 $$Z' \sim_{\text{rat}} Z$$이고 $$Z'$$가 $$W$$와 properly intersect하도록 만드는 것이다. 그러면 $$Z'$$가 $$W$$와 properly intersect하므로 $$Z' \cdot W$$를 직접 계산할 수 있고, 이것을 $$Z \cdot W$$로 정의한다. 이것이 가능하다는 것, 즉 $$Z'$$의 선택에 관계없이 결과가 같다는 것을 보이는 것이 이 절의 핵심 내용이다.

<div class="definition" markdown="1">

<ins id="def15">**정의 15**</ins> Intersection product에 의해 $$\operatorname{CH}^\ast(X) = \bigoplus_k \operatorname{CH}^k(X)$$는 *graded ring*이 된다. 이를 *Chow ring*이라 부른다.

</div>

Chow ring은 ([§선다발과 벡터다발, ⁋정의 9](/ko/math/algebraic_varieties/line_bundles#def9))에서 정의한 Picard group $$\Pic(X) \cong \operatorname{CH}^1(X)$$을 자연스럽게 포함한다. Picard group이 line bundle (즉 codimension 1 cycle)들의 곱셈이 덧셈으로 기록된 group이었다면, Chow ring은 이를 모든 codimension으로 확장하여 곱셈까지 갖춘 구조로 만든 것이다.

## Moving Lemma

Intersection product의 정의가 성립하려면, 임의의 두 cycle $$Z, W$$에 대해 $$Z$$를 rational equivalence 내에서 "이동"시켜 $$W$$와 properly intersect하도록 만들 수 있어야 한다. 이를 보장하는 정리가 **moving lemma**이다.

<div class="proposition" markdown="1">

<ins id="prop16">**명제 16 (Moving Lemma)**</ins> Smooth quasi-projective variety $$X$$와 cycle $$Z \in \operatorname{CH}^k(X)$$, 그리고 임의의 cycle $$W \in \operatorname{CH}^l(X)$$에 대해, $$Z' \sim_{\text{rat}} Z$$이고 $$Z'$$과 $$W$$가 properly intersect하는 $$Z'$$가 존재한다.

</div>

<details class="proof" markdown="1">
<summary>증명 (스케치)</summary>

핵심은 $$Z$$를 구성하는 각 irreducible component $$V_i$$에 대해, $$V_i$$를 rational equivalence 내에서 적절히 이동시킬 수 있다는 것이다. $$V_i$$를 포함하는 충분히 큰 projective space에 포함시킨 뒤, basepoint-free linear system을 사용하여 $$V_i$$를 "일반적인" hypersurface들로 자른다. 구체적으로 $$V_i$$의 cone을 이루는 point들을 충분히 일반적인 hyperplane들로 slicing하면 차원이 $$1$$씩 떨어지며, 이 과정에서 $$W$$와의 교차가 proper가 되도록 hyperplane의 방향을 선택할 수 있다. Basepoint-free 조건에 의해 이 slicing은 regular rational map을 유도하고, 그 graph의 closure가 rational equivalence를 보존하는 deformation을 제공한다. 각 component에 대해 독립적으로 이 과정을 수행하면 원하는 $$Z'$$를 얻는다.

</details>

핵심 아이디어는 다음과 같다. $$Z$$를 구성하는 irreducible component $$V_i$$마다, $$V_i$$를 포함하는 충분히 "일반적인" hypersurface $$H_i$$로 자르고, $$V_i \cap H_1 \cap \cdots \cap H_s$$와 같은 형태의 cycle을 취한다. 이때 "일반적"이라는 것은 $$H_i$$가 $$W$$와 generic한 위치에서 만나도록 선택한다는 것으로, 이렇게 하면 차원이 적절히 떨어져 proper intersection을 이룬다. ([§선형계, ⁋정의 5](/ko/math/algebraic_varieties/linear_systems#def5))에서 보았듯 basepoint-free linear system을 사용하면 이러한 "일반적인" 이동을 regular map으로 실현할 수 있으며, 이 과정이 rational equivalence를 보존함을 보이는 것이 증명의 핵심이다.

<div class="proposition" markdown="1">

<ins id="prop17">**명제 17**</ins> Moving lemma에 의해 intersection product를 다음과 같이 정의할 수 있다. $$Z' \sim_{\text{rat}} Z$$이고 $$Z'$$이 $$W$$와 properly intersect하도록 선택한 뒤,

$$Z \cdot W := Z' \cdot W = \sum_{T \subset Z' \cap W} i_T(Z', W) [T]$$

으로 정의하면, 이 값은 $$Z'$$의 선택과 무관하게 결정된다.

</div>

<details class="proof" markdown="1">
<summary>증명 (스케치)</summary>

이는 [명제 16](#prop16)의 직접적인 따름이다. 두 이동 $$Z'_1, Z'_2$$ 모두 moving lemma로 얻어진 것이므로 $$Z'_1 - Z'_2$$는 $$\divisor(f)$$의 형태이다. $$\divisor(f) \cdot W$$를 계산하면, $$f$$가 rational function이므로 그 graph가 $$\mathbb{P}^1 \times X$$ 위에서 $$W$$와의 교차로 주어지며, $$\mathbb{P}^1$$ 위의 두 점 $$0$$과 $$\infty$$에서의 fiber가 각각 $$Z'_1 \cdot W$$와 $$Z'_2 \cdot W$$에 해당한다. $$\mathbb{P}^1$$의 $$0$$과 $$\infty$$가 rationally equivalent하므로 두 fiber 역시 rationally equivalent하고, 따라서 $$Z'_1 \cdot W = Z'_2 \cdot W \in \operatorname{CH}^\ast(X)$$이다.

</details>

<div class="example" markdown="1">

<ins id="ex18">**예시 18**</ins> $$\mathbb{P}^2$$에서 두 conic $$C_1 = Z(F_1)$$, $$C_2 = Z(F_2)$$가 curve를 공유하는 상황, 즉 proper intersection이 아닌 경우를 생각하자. 예를 들어 $$C_1$$과 $$C_2$$가 한 직선 $$L$$을 공유한다면, $$C_1 \cap C_2$$는 $$L$$과 $$L$$ 밖의 유한 개의 점들로 구성된다. 이때 moving lemma에 의해 $$C_2$$를 $$C_2' \sim_{\text{rat}} C_2$$로 이동시켜 $$C_1$$과 properly intersect하도록 할 수 있다. 기하적으로, $$C_2'$$는 $$C_2$$를 ([§유리사상, ⁋정의 5](/ko/math/algebraic_varieties/rational_maps#def5))의 rational map에 의해 약간 "밀어" 얻은 conic이며, 이것이 $$C_1$$과 $$4$$개의 점에서 (Bézout 정리에 의해) 만나게 된다.

</div>

## Deformation to Normal Cone

Moving lemma는 quasi-projective setting에서 intersection product를 정의하는 고전적 방법이다. 그러나 이 접근은 quasi-projectivity라는 가정에 의존하며, general scheme으로 확장하는 것은 매우 어렵다. 이에 대한 대안이 Fulton이 개발한 **deformation to normal cone**이다.

Fulton의 접근에서 핵심적인 관찰은 다음과 같다. ([§접공간과 매끄러움, ⁋정의 13](/ko/math/algebraic_varieties/tangent_spaces_and_smoothness#def13))에서 우리는 tangent cone을 정의했는데, 이는 singular point에서의 국소적 구조를 이해하는 도구였다. Normal cone은 이를 embedding의 언어로 일반화한 것으로, closed embedding $$i: Y \hookrightarrow X$$에 대해 $$Y$$의 $$X$$ 안에서의 *normal cone* $$C_{Y/X}$$를 정의할 수 있다. 만일 $$X$$가 $$Y$$를 따라 smooth하다면 normal cone은 normal bundle $$N_{Y/X}$$가 되지만, 일반적으로는 cone 구조를 가진다.

<div class="proposition" markdown="1">

<ins id="prop19">**명제 19 (Deformation to Normal Cone)**</ins> Closed embedding $$i: Y \hookrightarrow X$$에 대해, $$\mathbb{A}^1$$을 매개변수로 하는 family $$M \to \mathbb{A}^1$$을 구성할 수 있다. 구체적으로, $$t \neq 0$$에서의 fiber $$M_t$$는 $$X$$ 자신이며, $$t = 0$$에서의 fiber $$M_0$$는 normal cone $$C_{Y/X}$$이다. 이 family의 존재는 intersection product의 well-definedness를 이 family에 대한 pushforward/pullback의 호환성으로 환원시킨다.

</div>

<details class="proof" markdown="1">
<summary>증명 (스케치)</summary>

구성은 blow-up을 사용한다. 먼저 $$X \times \mathbb{A}^1$$ 안에서 $$Y \times \{0\}$$를 따라 blow-up하여 $$\widetilde{M} = \Bl_{Y \times \{0\}}(X \times \mathbb{A}^1)$$을 얻고, 그 후 $$X \times \{0\}$$의 proper transform을 제거하여 $$M = \widetilde{M} \setminus \widetilde{X \times \{0\}}$$로 정의한다. 이 blow-up의 exceptional divisor는 $$\mathbb{P}(C_{Y/X} \oplus \mathcal{O}_Y)$$이며, proper transform을 제거하면 $$t=0$$ fiber에서 정확히 normal cone $$C_{Y/X}$$가 남는다. $$t \neq 0$$에서는 blow-up이 isomorphism이므로 fiber가 $$X$$ 그대로이다. 따라서 $$M \to \mathbb{A}^1$$은 $$t=1$$에서의 $$X$$를 $$t=0$$에서의 $$C_{Y/X}$$로 연결하는 deformation을 제공한다. Chow group에서 $$M$$ 위의 specialization map $$\sigma: \operatorname{CH}^\ast(X) \to \operatorname{CH}^\ast(C_{Y/X})$$을 정의할 수 있고, normal cone이 vector bundle 구조를 가질 때 (즉 regular embedding의 경우) Thom isomorphism에 의해 $$\operatorname{CH}^\ast(C_{Y/X}) \cong \operatorname{CH}^\ast(Y)$$가 되어 intersection product의 well-definedness가 확립된다.

</details>

이 방법의 아이디어는 $$X$$를 연속적으로 변형하여 $$Y$$의 normal cone으로 수축시키는 것이다. 기하적으로, $$t=1$$에서는 원래 공간 $$X$$를 보고, $$t$$가 $$0$$으로 갈수록 $$X$$가 $$Y$$를 따라 점점 더 "펴지면서" 결국 $$t=0$$에서는 $$Y$$를 따라 벌어진 normal cone이 된다. ([§유리사상, ⁋예시 12](/ko/math/algebraic_varieties/rational_maps#ex12))의 blow-up이 한 점을 $$\mathbb{P}^1$$로 펼쳐 놓는 변형이었다면, deformation to normal cone은 이를 더 일반적인 embedding에 대해 수행하는 것이다.

이 접근은 moving lemma와 달리 scheme에 대한 추가 가정 (quasi-projectivity 등)이 필요하지 않아 더 일반적이며, Fulton의 *Intersection Theory*에서 채택한 주요 프레임워크이다. Pullback $$f^\ast$$는 ([§저우 군, ⁋명제 7](/ko/math/algebraic_varieties/chow_groups#prop7)) 및 ([§저우 군, ⁋명제 11](/ko/math/algebraic_varieties/chow_groups#prop11))에서 정의되었다.

## 예시들

Intersection product의 성질을 구체적인 예시들을 통해 확인해 보자.

<div class="example" markdown="1">

<ins id="ex20">**예시 20 ($$\mathbb{P}^n$$)**</ins> $$\operatorname{CH}^\ast(\mathbb{P}^n) \cong \mathbb{Z}[H] / (H^{n+1})$$이다. 여기서 $$H = [\text{hyperplane}] \in \operatorname{CH}^1(\mathbb{P}^n)$$로, $$H^k$$는 $$k$$-codimensional linear subspace의 class와 같다. Degree $$d$$ hypersurface $$V(f)$$에 대해서는 $$[V(f)] = dH$$이다. 이 결과는 ([§인자, ⁋예시 11](/ko/math/algebraic_varieties/divisors#ex11))에서 $$\Cl(\mathbb{P}^n) \cong \mathbb{Z}$$임을 이미 보였으므로 자연스러운 것이다. Picard group $$\Pic(\mathbb{P}^n) \cong \operatorname{CH}^1(\mathbb{P}^n) \cong \mathbb{Z}$$에 intersection product를 더하면, $$H \cdot H = H^2$$, $$H \cdot H^2 = H^3$$, ...의 곱셈이 추가되어 Chow ring이 완성된다.

특히 $$\mathbb{P}^2$$에서 Bézout 정리를 Chow ring의 언어로 번역하면, degree $$d_1$$ curve와 degree $$d_2$$ curve의 교차가 $$d_1 H \cdot d_2 H = d_1 d_2 H^2$$로 계산된다. $$H^2 = [\text{point}]$$이므로 교차 수는 $$d_1 d_2$$가 되고, 이는 두 curve의 구체적인 위치에 무관함을 보여준다. 이것이 [도입](#도입)에서 언급한 "위치가 아니라 class에 의존한다"는 주장의 엄밀한 의미이다.

</div>

<div class="example" markdown="1">

<ins id="ex21">**예시 21 (Surface)**</ins> Surface $$S$$ 위의 두 curve $$C, D$$에 대해:

$$[C] \cdot [D] = \sum_{p \in C \cap D} i_p(C, D) [p] \in \operatorname{CH}^2(S)$$

이다. 일반적인 surface의 경우 $$\operatorname{CH}^2(S)$$의 구조는 단순하지 않다. Zero-cycles modulo rational equivalence는 degree map $$\deg: \operatorname{CH}^2(S) \to \mathbb{Z}$$에 의해 $$\mathbb{Z}$$으로 가는 surjection을 갖지만, 그 kernel은 일반적으로 비자명이다. 가령 $$p_g(S) > 0$$인 surface에서는 Mumford의 정리에 의해 $$\operatorname{CH}^2(S)$$가 "infinite dimensional"이 된다. 따라서 교차 수 $$C \cdot D = \sum_{p \in C \cap D} i_p(C, D)$$는 degree map의 image로서 정수값을 얻지만, $$\operatorname{CH}^2(S)$$ 자체는 $$\mathbb{Z}$$이 아닐 수 있다.

그러나 $$\mathbb{P}^2$$에서는 상황이 단순하다. $$\operatorname{CH}^\ast(\mathbb{P}^2) = \mathbb{Z}[H]/(H^3)$$이므로 $$\operatorname{CH}^2(\mathbb{P}^2) \cong \mathbb{Z}$$이고, 교차 수가 완전히 결정된다. 예를 들어 ([§사영다양체, ⁋예시 11](/ko/math/algebraic_varieties/projective_varieties#ex11))의 conic $$X = Z(\x_0^2 + \x_1^2 - \x_2^2) \subset \mathbb{P}^2$$와 임의의 직선 $$L$$의 교차는, $$L$$이 $$X$$와 properly intersect하면, 항상 $$2$$개의 점 (counted with multiplicity)에서 만난다. Chow ring에서 $$[X] = 2H$$, $$[L] = H$$이므로 $$[X] \cdot [L] = 2H \cdot H = 2H^2 = 2[\text{point}]$$이다.

</div>

<div class="example" markdown="1">

<ins id="ex22">**예시 22 ($$\mathbb{P}^1 \times \mathbb{P}^1$$)**</ins> ([§유리사상, ⁋예시 11](/ko/math/algebraic_varieties/rational_maps#ex11))에서 $$\mathbb{P}^1 \times \mathbb{P}^1$$과 quadric surface $$Q = V(\x\y - \z\w)$$가 birationally equivalent (실은 isomorphic)임을 보았다. $$\mathbb{P}^1 \times \mathbb{P}^1$$의 Chow ring은

$$\operatorname{CH}^\ast(\mathbb{P}^1 \times \mathbb{P}^1) \cong \mathbb{Z}[H_1, H_2] / (H_1^2, H_2^2)$$

이다. 여기서 $$H_1 = [\mathbb{P}^1 \times \{p\}]$$, $$H_2 = [\{p\} \times \mathbb{P}^1]$$이다. Bidegree $$(a, b)$$의 curve $$C$$에 대해 $$[C] = aH_1 + bH_2$$이며, 따라서 두 curve $$C = aH_1 + bH_2$$, $$C' = a'H_1 + b'H_2$$의 교차 수는

$$C \cdot C' = (aH_1 + bH_2)(a'H_1 + b'H_2) = ab' H_1 H_2 + a'b H_1 H_2 = (ab' + a'b) H_1 H_2$$

으로 계산된다. $$H_1 H_2 = [\text{point}]$$이므로 교차 수는 $$ab' + a'b$$이다. 이는 곡선의 bidegree로부터 교차 수를 직접 계산할 수 있음을 보여준다.

</div>

<div class="example" markdown="1">

<ins id="ex23">**예시 23 (Segre embedding과 교차)**</ins> ([§사영다양체, ⁋예시 16](/ko/math/algebraic_varieties/projective_varieties#ex16))의 Segre embedding $$\sigma: \mathbb{P}^1 \times \mathbb{P}^1 \to \mathbb{P}^3$$를 생각하자. 이 embedding의 image는 quadric surface $$Q = V(\x_0\x_3 - \x_1\x_2)$$이다. ([§선다발과 벡터다발, ⁋명제 20](/ko/math/algebraic_varieties/line_bundles#prop20))에 의해 pullback $$\sigma^\ast \mathcal{O}_{\mathbb{P}^3}(1)$$은 $$\mathbb{P}^1 \times \mathbb{P}^1$$ 위의 line bundle이며, 실제로 $$\sigma^\ast \mathcal{O}_{\mathbb{P}^3}(1) \cong \mathcal{O}_{\mathbb{P}^1 \times \mathbb{P}^1}(1,1)$$이다. 이는 Chow ring 수준에서도 확인할 수 있다. $$\mathbb{P}^3$$에서 hyperplane class $$H_{\mathbb{P}^3}$$를 pullback하면 $$H_1 + H_2$$를 얻고, 이는 bidegree $$(1,1)$$에 해당한다.

이를 통해 $$\mathbb{P}^3$$에서의 교차 계산을 $$\mathbb{P}^1 \times \mathbb{P}^1$$으로 옮겨 수행할 수 있다. 가령 $$\mathbb{P}^3$$에서 두 개의 hyperplane section $$H_1 \cap H_2 \cap Q$$의 교차는, $$\mathbb{P}^1 \times \mathbb{P}^1$$에서 $$(H_1 + H_2)^2 = 2H_1 H_2$$로 계산된다. 즉, 두 hyperplane과 quadric surface의 교차는 $$2$$개의 점으로, 이는 $$Q \cong \mathbb{P}^1 \times \mathbb{P}^1$$에서 두 개의 bidegree $$(1,1)$$ curve가 만나는 것과 같다.

</div>

## 선다발과의 교차

<div class="proposition" markdown="1">

<ins id="prop24">**명제 24**</ins> Line bundle $$L$$과 cycle $$Z \in \operatorname{CH}_k(X)$$에 대해 $$c_1(L) \cap Z \in \operatorname{CH}_{k-1}(X)$$가 well-defined되어 있다. 여기서 **first Chern class** $$c_1(L) \in \operatorname{CH}^1(X)$$는 line bundle $$L$$에 대응하는 divisor class이며, $$L$$이 Cartier divisor $$D$$에 의해 주어지면 $$c_1(L) = [D] \in \operatorname{CH}^1(X)$$이다. 이 대응은 ([§인자](/ko/math/algebraic_varieties/divisors))와 ([§선다발과 벡터다발](/ko/math/algebraic_varieties/line_bundles))에서 다룬 Cartier divisor와 line bundle 사이의 동치관계에 근거한다. 구체적으로 $$L = \mathcal{O}(D)$$, $$D = \sum n_i V_i$$일 때 $$D$$와 $$Z$$가 properly intersect하면 $$c_1(L) \cap Z = \sum n_i \cdot (V_i \cdot Z)$$로 정의되며, proper intersection이 아닌 경우 moving lemma나 deformation to normal cone을 사용한다.

</div>

<details class="proof" markdown="1">
<summary>증명 (스케치)</summary>

Well-definedness의 핵심은 $$c_1(L) \cap Z$$가 $$L$$의 rational section의 선택에 의존하지 않는다는 것이다. $$L$$의 두 rational section $$s_1, s_2$$를 생각하면 $$\divisor(s_1) - \divisor(s_2) = \divisor(s_1/s_2)$$이고, $$s_1/s_2 \in \mathbb{K}(X)^\ast$$는 rational function이다. 따라서 $$[\divisor(s_1)] - [\divisor(s_2)] = 0 \in \operatorname{CH}^1(X)$$이며, 이는 $$c_1(L)$$가 divisor의 선택과 무관함을 보인다. Cap product의 호환성, 즉 $$c_1(L_1 \otimes L_2) = c_1(L_1) + c_1(L_2)$$는 tensor product에 대응하는 divisor의 덧셈으로부터 바로 따른다.

</details>

<div class="proposition" markdown="1">

<ins id="prop25">**명제 25**</ins> $$L = \mathcal{O}(D)$$이면:

$$c_1(L) \cap [X] = [D] \in \operatorname{CH}^1(X)$$

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$c_1(L)$$의 정의에 의해, $$L = \mathcal{O}(D)$$에 대해 $$c_1(L) = [D] \in \operatorname{CH}^1(X)$$이다. 기본 class $$[X] \in \operatorname{CH}^0(X)$$에 대한 cap product $$c_1(L) \cap [X]$$는 intersection product $$[D] \cdot [X]$$와 같다. $$[X] \in \operatorname{CH}^0(X)$$가 항등원이므로 $$[D] \cdot [X] = [D]$$이다.

</details>

## 사상 공식

<div class="proposition" markdown="1">

<ins id="prop26">**명제 26 (Projection Formula)**</ins> Proper morphism $$f: X \to Y$$와 $$\alpha \in \operatorname{CH}^\ast(X)$$, $$\beta \in \operatorname{CH}^\ast(Y)$$에 대해 $$f_\ast(\alpha \cdot f^\ast \beta) = f_\ast(\alpha) \cdot \beta$$가 성립한다.

</div>

<details class="proof" markdown="1">
<summary>증명 (스케치)</summary>

먼저 $$f$$가 flat인 경우를 생각하자. 이 경우 flat pullback $$f^\ast$$는 cycle level에서 $$f^\ast[W] = [f^{-1}(W)]$$로 정의되므로, $$\alpha = [V]$$, $$\beta = [W]$$에 대해 $$[V] \cdot f^\ast[W] = [V] \cap [f^{-1}(W)]$$이다. 한편 $$f_\ast(\alpha) \cdot \beta = [f(V)] \cdot [W]$$이며, $$f|_{V \cap f^{-1}(W)}: V \cap f^{-1}(W) \to f(V) \cap W$$가 proper surjective이므로 pushforward가 교차를 보존한다.

일반적인 morphism $$f$$의 경우, pullback $$f^\ast$$는 moving lemma나 deformation to normal cone을 통해 정의된다. 핵심은 intersection product가 rational equivalence와 호환된다는 것이다. $$\alpha = [V]$$를 $$V' \sim_{\text{rat}} V$$로 이동시켜 $$V'$$가 $$f^{-1}(W)$$와 properly intersect하도록 만들면, $$[V'] \cdot [f^{-1}(W)]$$와 $$[f(V')] \cdot [W]$$ 사이의 관계를 pushforward-pullback의 호환성으로 추적할 수 있다. Proper map 하에서의 degree 보존과 rational equivalence의 호환성으로부터 양변이 같음이 따른다.

</details>


---

**참고문헌**

**[Ful]** W. Fulton, *Intersection Theory*, Springer, 1984.
**[Har]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.
