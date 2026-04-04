---
title: "Intersection Multiplicity"
excerpt: "Intersection multiplicity and Bezout's theorem for curves"

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/intersection_multiplicity
sidebar: 
    nav: "algebraic_geometry-ko"

header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Intersection_Multiplicity.png
    overlay_filter: 0.5

date: 2026-03-15
last_modified_at: 2026-03-15
weight: 18
published: false
---

## 도입

([§차원, ⁋예시 14](/ko/math/algebraic_geometry/dimension#ex14))에서 우리는 두 variety의 교집합의 차원에 대한 부등식을 살펴보았다. 이제 우리는 교집합이 "얼마나 복잡하게" 일어나는지를 정량화하고자 한다. 

평면 $$\mathbb{A}^2$$에서 두 곡선 $$V: y = 0$$과 $$W_1: y = x$$이 원점에서 만난다고 하자. 또 다른 곡선 $$W_2: y = x^2$$ 역시 원점에서 $$V$$와 만난다. 두 경우 모두 교집합은 원점 하나이지만, 그 만나는 방식은 본질적으로 다르다. $$V$$와 $$W_1$$은 원점에서 "가로지르듯" 교차하는 반면, $$V$$와 $$W_2$$는 원점에서 접한다. 이러한 차이를 수치화하기 위해 우리는 *intersection multiplicity*를 정의한다.

핵심적인 관찰은 $$V, W$$를 정의하는 방정식들이 점 $$p$$ 근방에서 얼마나 "깊게" 얽혀있는지를 측정하면 된다는 것이다. 구체적으로 $$V$$를 정의하는 ideal $$I(V)$$와 $$W$$를 정의하는 ideal $$I(W)$$를 점 $$p$$에서의 local ring $$\mathcal{O}_{\mathbb{A}^n, p}$$에서 생각할 때, quotient $$\mathcal{O}_{\mathbb{A}^n, p}/(I(V)+I(W))$$의 $$\mathbb{K}$$-dimension이 클수록 두 variety가 $$p$$에서 더 복잡하게 교차함을 의미한다.

## 정의

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Affine space $$\mathbb{A}^n$$의 점 $$p$$에서 두 variety $$V, W$$의 *intersection multiplicity<sub>교차 중복도</sub>* $$i_p(V, W)$$를 다음과 같이 정의한다:

$$i_p(V, W) = \dim_{\mathbb{K}} \mathcal{O}_{\mathbb{A}^n, p} / (I(V) + I(W))$$

여기서 $$\mathcal{O}_{\mathbb{A}^n, p}$$는 $$p$$에서의 local ring이다. ([\[가환대수학\] §국소화, ⁋정의 1](/ko/math/commutative_algebra/localization#def1)) 이 정의는 $$\dim V + \dim W = n$$, 즉 $$V$$와 $$W$$가 *complementary dimension*을 가지는 경우에 국한하여 사용한다. 이 조건 하에서 $$V \cap W$$는 $$p$$ 근방에서 zero-dimensional이며, [명제 5](#prop5)에서 보이듯 $$i_p(V, W)$$는 유한하다.

</div>

이 정의가 성립하려면 $$\mathcal{O}_{\mathbb{A}^n, p}/(I(V)+I(W))$$가 유한 차원 $$\mathbb{K}$$-vector space여야 한다. 이 조건은 [명제 5](#prop5)에서 다룬다.

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins> $$\mathbb{A}^2$$에서 $$V: y = 0$$과 $$W: y = x^2$$가 원점에서 만난다. 각 곡선을 정의하는 ideal은 $$I(V) = (y)$$, $$I(W) = (y - x^2)$$이다. 원점에서의 local ring에 대한 quotient를 계산하면 $$\mathcal{O}_{\mathbb{A}^2, 0} / (y, y - x^2) = \mathcal{O}_{\mathbb{A}^2, 0} / (y, x^2)$$이며, 이 quotient는 basis $$\{1, x\}$$를 갖는 2차원 $$\mathbb{K}$$-vector space이다. 따라서 $$i_0(V, W) = 2$$이다. 이는 곡선 $$W$$가 $$V$$ 위에서 $$x=0$$에서 order 2로 접한다는 사실과 일치한다.

</div>

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> $$\mathbb{A}^2$$에서 $$V: y = 0$$과 $$W: y = x^3$$이 원점에서 만난다.

$$\mathcal{O}_{\mathbb{A}^2, 0} / (y, x^3)$$은 basis $$\{1, x, x^2\}$$를 갖는 3차원 $$\mathbb{K}$$-vector space이다.

따라서 $$i_0(V, W) = 3$$이다. 마찬가지로 일반적으로 $$V: y = 0$$과 $$W: y = x^n$$에 대하여 $$i_0(V, W) = n$$이다.

</div>

## 기본 성질

Intersection multiplicity을 기하학적으로 의미있게 만들기 위해서는 그것이 *횡단 교차*라는 개념과 어떤 관계에 있는지를 밝혀야 한다.

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> 두 variety $$V, W \subseteq \mathbb{A}^n$$이 점 $$p \in V \cap W$$에서 *transversely intersect<sub>횡단 교차</sub>*한다는 것은 tangent space의 합이 전체 공간을 채우는 것이다:

$$T_p V + T_p W = \mathbb{A}^n$$

Tangent space $$T_p V$$의 정의는 ([§접공간과 매끄러움, ⁋정의 1](/ko/math/algebraic_geometry/tangent_spaces_and_smoothness#def1))를 참조하라.

</div>

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> Intersection multiplicity은 항상 음이 아닌 정수로 정의되며, $$p \notin V \cap W$$이면 $$i_p(V, W) = 0$$이다. $$V, W$$가 $$p$$에서 transversely intersect하면 ([정의 4](#def4)) $$i_p(V, W) = 1$$이다. 또한 $$i_p(V, W) = i_p(W, V)$$가 성립한다(symmetry). 마지막으로 $$\dim V + \dim W = n$$이면 $$i_p(V, W) < \infty$$이다.

*증명.* $$R = \mathcal{O}_{\mathbb{A}^n, p}$$, $$\mathfrak{a} = I(V)R$$, $$\mathfrak{b} = I(W)R$$라 하자.

먼저 음이 아닌 정수임을 보이자. $$i_p(V, W)$$는 vector space의 dimension이므로 자명히 $$\geq 0$$이다. $$p \notin V \cap W$$이면 $$p \notin V$$이거나 $$p \notin W$$이다. 만일 $$p \notin V$$이면 $$I(V)$$의 어떤 원소 $$f$$가 $$p$$에서 $$0$$이 아니고, 따라서 $$R$$에서 invertible이다. 즉 $$\mathfrak{a} + \mathfrak{b} = R$$이 되어 $$R/(\mathfrak{a} + \mathfrak{b}) = 0$$이고 $$i_p(V, W) = 0$$이다.

다음으로 횡단 교차의 경우를 보이자. $$V, W$$가 $$p$$에서 transversely intersect하면 $$T_p V + T_p W = \mathbb{A}^n$$이다. Ambient space $$\mathbb{A}^n$$의 cotangent space는 $$\mathfrak{m}_p/\mathfrak{m}_p^2$$이고, $$V$$의 tangent space는 몫 공간 $$\mathfrak{m}_p/\mathfrak{m}_p^2 \twoheadrightarrow \mathfrak{m}_p/(\mathfrak{a}+\mathfrak{m}_p^2)$$의 쌍대이다. 즉 $$T_p V = (\mathfrak{m}_p/(\mathfrak{a}+\mathfrak{m}_p^2))^*$$이고, 마찬가지로 $$T_p W = (\mathfrak{m}_p/(\mathfrak{b}+\mathfrak{m}_p^2))^*$$이다.

$$T_p V$$와 $$T_p W$$는 각각 $$T_p \mathbb{A}^n = (\mathfrak{m}_p/\mathfrak{m}_p^2)^*$$의 부분공간이다. $$T_p V$$의 annihilator는 $$\mathfrak{a}/(\mathfrak{a} \cap \mathfrak{m}_p^2) \cong (\mathfrak{a}+\mathfrak{m}_p^2)/\mathfrak{m}_p^2 \subseteq \mathfrak{m}_p/\mathfrak{m}_p^2$$이고, $$T_p W$$의 annihilator는 $$(\mathfrak{b}+\mathfrak{m}_p^2)/\mathfrak{m}_p^2$$이다. $$T_p V + T_p W = T_p \mathbb{A}^n$$이면 두 annihilator의 교집합이 0이고, 이것은 $$\mathfrak{a}+\mathfrak{b}$$의 $$\mathfrak{m}_p/\mathfrak{m}_p^2$$에서의 image가 전체 $$\mathfrak{m}_p/\mathfrak{m}_p^2$$임을 의미한다. 따라서 $$\mathfrak{a}+\mathfrak{b}+\mathfrak{m}_p^2 = \mathfrak{m}_p$$이고, Nakayama의 보조정리에 의해 $$\mathfrak{a}+\mathfrak{b}=\mathfrak{m}_p$$이다. 결과적으로 $$R/(\mathfrak{a}+\mathfrak{b})=R/\mathfrak{m}_p\cong\mathbb{K}$$이므로 $$i_p(V, W) = 1$$이다.

Symmetry는 $$\mathfrak{a} + \mathfrak{b} = \mathfrak{b} + \mathfrak{a}$$이므로 $$R/(\mathfrak{a} + \mathfrak{b}) \cong R/(\mathfrak{b} + \mathfrak{a})$$에서 자명하게 성립한다.

마지막으로 유한성을 보이자. $$R = \mathcal{O}_{\mathbb{A}^n, p}$$는 Krull dimension $$n$$의 regular local ring이다. $$\dim V = \dim(R/\mathfrak{a})$$, $$\dim W = \dim(R/\mathfrak{b})$$이다. dimension inequality ([§차원, ⁋예시 14](/ko/math/algebraic_geometry/dimension#ex14))에 의하여
$$\dim(R/(\mathfrak{a} + \mathfrak{b})) \geq \dim(R/\mathfrak{a}) + \dim(R/\mathfrak{b}) - \dim R = \dim V + \dim W - n$$
이고, $$\dim V + \dim W = n$$이므로 $$\dim(R/(\mathfrak{a} + \mathfrak{b})) \geq 0$$이다. 한편 $$\mathfrak{a} + \mathfrak{b} \subseteq \mathfrak{m}_p$$이므로 $$R/(\mathfrak{a} + \mathfrak{b})$$의 모든 prime ideal은 $$\mathfrak{m}_p/(\mathfrak{a} + \mathfrak{b})$$에 포함된다. 즉 $$R/(\mathfrak{a} + \mathfrak{b})$$는 유일한 prime ideal $$\mathfrak{m}_p/(\mathfrak{a} + \mathfrak{b})$$를 갖는 local ring이며, 이는 $$\mathfrak{a} + \mathfrak{b}$$가 $$\mathfrak{m}_p$$-primary ideal임을 의미한다. 따라서 $$\dim(R/(\mathfrak{a} + \mathfrak{b})) \leq 0$$이고, 앞의 부등식과 합쳐 $$\dim(R/(\mathfrak{a} + \mathfrak{b})) = 0$$이다. Krull dimension $$0$$의 Noetherian local ring은 Artinian이고 ([\[가환대수학\] §크룰 차원, ⁋따름정리 3](/ko/math/commutative_algebra/Krull_dimension#cor3)), Artinian local ring은 유한 길이를 가지므로 유한 차원 $$\mathbb{K}$$-vector space이다. 특히 $$\dim_{\mathbb{K}} R/(\mathfrak{a} + \mathfrak{b}) < \infty$$이다. ∎

</div>

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6 (Additivity)**</ins> $$\dim V + \dim W = n$$이고, $$V = V_1 \cup V_2$$이며 $$V_1$$, $$V_2$$가 $$p$$를 포함하는 공통 irreducible component를 갖지 않으면:

$$i_p(V, W) = i_p(V_1, W) + i_p(V_2, W)$$

*증명.* $$R = \mathcal{O}_{\mathbb{A}^n, p}$$, $$I_1 = I(V_1)R$$, $$I_2 = I(V_2)R$$, $$J = I(W)R$$라 하자. $$V = V_1 \cup V_2$$이므로 $$I(V) = I_1 \cap I_2$$이다.

$$\bar{R} = R/J$$, $$\bar{I}_1 = (I_1 + J)/J$$, $$\bar{I}_2 = (I_2 + J)/J$$라 두면 표준적인 short exact sequence
$$0 \to \bar{R}/(\bar{I}_1 \cap \bar{I}_2) \to \bar{R}/\bar{I}_1 \oplus \bar{R}/\bar{I}_2 \to \bar{R}/(\bar{I}_1 + \bar{I}_2) \to 0$$
이 존재한다. 여기서 첫 사상은 $$\bar{a} \mapsto (\bar{a}, -\bar{a})$$, 둘째 사상은 $$(\bar{a}, \bar{b}) \mapsto \overline{a - b}$$이며, exactness는 직접 확인할 수 있다. $$\mathbb{K}$$-dimension을 비교하면
$$i_p(V, W) + \dim_{\mathbb{K}} R/(I_1 + I_2 + J) = i_p(V_1, W) + i_p(V_2, W)$$
이다.

이제 $$\dim_{\mathbb{K}} R/(I_1 + I_2 + J) = 0$$임을 보이자. $$V_1$$과 $$V_2$$가 $$p$$를 포함하는 공통 irreducible component를 갖지 않으므로, $$V_1 \cap V_2$$의 $$p$$를 포함하는 component들의 차원은 $$\dim V$$보다 엄격히 작다. ([§차원, ⁋예시 14](/ko/math/algebraic_geometry/dimension#ex14))의 부등식에 의하면
$$\dim_p(V_1 \cap V_2 \cap W) \geq \dim_p(V_1 \cap V_2) + \dim_p W - n$$
이다. 여기서 $$\dim_p(V_1 \cap V_2) < \dim V$$이고 $$\dim V + \dim W = n$$이므로 우변이 음수이다. 그런데 차원은 항상 $$\geq -1$$이다(공집합의 차원을 $$-1$$로 정의하면). 따라서 부등식 $$\dim_p(V_1 \cap V_2 \cap W) < 0$$을 만족하는 것은 $$V_1 \cap V_2 \cap W$$가 $$p$$ 근방에서 빈 집합인 경우뿐이다. 즉 $$p \notin V_1 \cap V_2 \cap W$$이고, [명제 5](#prop5)의 첫 번째 주장에 의하여 $$\dim_{\mathbb{K}} R/(I_1 + I_2 + J) = 0$$이다. 결과적으로
$$i_p(V, W) = i_p(V_1, W) + i_p(V_2, W)$$
이다. ∎

</div>

## Projective case

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> $$\mathbb{P}^n$$의 점 $$p$$에서 두 variety $$V, W$$의 intersection multiplicity를 affine chart에서의 값으로 정의한다. $$p$$를 포함하는 임의의 affine chart $$U \cong \mathbb{A}^n$$을 선택하고, $$V \cap U$$, $$W \cap U$$의 affine intersection multiplicity를 취한다. 이 값은 affine chart의 선택과 무관하다.

</div>

이 값이 chart의 선택과 무관한 이유는 간단하다. $$U_1, U_2$$가 $$p$$를 포함하는 두 affine chart라면, $$U_1 \cap U_2$$는 $$p$$를 포함하는 열린집합이고, local ring $$\mathcal{O}_{\mathbb{P}^n, p}$$는 $$U_1$$, $$U_2$$ 모두에서의 local ring과 자연스럽게 동형이다. Intersection multiplicity의 정의가 $$p$$에서의 local ring만에 의존하므로, chart의 선택에 영향받지 않는다.

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8 (Bézout 정리, $$\mathbb{P}^2$$의 경우)**</ins> $$\mathbb{P}^2$$에서 degree $$m$$, $$n$$의 두 curve $$C, D$$가 공통 성분을 갖지 않으면:

$$\sum_{p \in C \cap D} i_p(C, D) = mn$$

여기서 curve의 degree $$\deg(C)$$는 $$C$$를 정의하는 homogeneous polynomial의 차수이다.

*증명 sketch.* 핵심 아이디어는 resultant를 사용하는 것이다. $$C$$를 정의하는 homogeneous polynomial $$F$$와 $$D$$를 정의하는 homogeneous polynomial $$G$$에 대해, $$F$$와 $$G$$의 resultant $$\operatorname{Res}(F, G)$$를 생각하면 이것이 정확히 교차점들의 multiplicity 곱들을 인자로 갖는다. Hilbert polynomial을 사용한 degree 계산과 결합하면 총합이 $$mn$$임을 보일 수 있다. 자세한 증명은 ([§Bézout's Theorem](/ko/math/algebraic_geometry/bezout_theorem))에서 다룬다.

</div>

<div class="example" markdown="1">

<ins id="ex9">**예시 9**</ins> 원 $$C: x^2 + y^2 = z^2$$과 직선 $$L: y = z$$을 $$\mathbb{P}^2$$에서 생각하자.

$$y = z$$를 $$x^2 + y^2 = z^2$$에 대입하면 $$x^2 = 0$$을 얻는다. 따라서 $$C \cap L$$은 한 점 $$[0:1:1]$$에서 multiplicity 2로 만난다.

한편 $$\deg C = 2$$, $$\deg L = 1$$이므로 Bézout 정리에 의해 교차점들의 multiplicity 합은 $$2 \times 1 = 2$$이어야 하며, 이는 위의 계산과 일치한다.

</div>

## Bézout 정리의 일반화

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10**</ins> $$\mathbb{P}^n$$에서 두 variety $$V, W \subseteq \mathbb{P}^n$$에 대하여, $$\dim V + \dim W = n$$이고 $$V \cap W$$가 유한집합이면:

$$\sum_{p \in V \cap W} i_p(V, W) = \deg(V) \cdot \deg(W)$$

여기서 projective variety $$V$$의 degree $$\deg(V)$$는 generic hyperplane $$\dim V$$개의 교차으로 얻어지는 0차원 variety에서 각 점의 intersection multiplicity의 합으로 정의된다. 즉, 일반적인 위치에 있는 hyperplane $$H_1, \ldots, H_{\dim V}$$에 대하여 $$\deg(V) = \sum_{p \in V \cap H_1 \cap \cdots \cap H_{\dim V}} i_p(V, H_1 \cap \cdots \cap H_{\dim V})$$이다. 이 값은 Hilbert polynomial의 최고차항 계수에 $$\dim(V)!$$를 곱한 것과 일치한다.

*증명 sketch.* Bézout 정리의 일반 형태이다. $$V, W$$를 각각 $$\deg(V)$$, $$\deg(W)$$개의 hyperplane의 intersection으로 근사한 뒤, additivity와 induction으로 증명한다. 자세한 증명은 ([§Bézout's Theorem](/ko/math/algebraic_geometry/bezout_theorem))에서 다룬다.

</div>

## 접공간과의 관계

<div class="proposition" markdown="1">

<ins id="prop11">**명제 11**</ins> $$V, W$$가 $$p$$에서 smooth하면:

$$i_p(V, W) = 1 \iff T_p V + T_p W = \mathbb{A}^n$$

즉, tangent space가 transversely intersect하면 ([정의 4](#def4)) multiplicity 1이다.

*증명.* $$R = \mathcal{O}_{\mathbb{A}^n, p}$$, $$\mathfrak{a} = I(V)R$$, $$\mathfrak{b} = I(W)R$$라 하자. $$V, W$$가 $$p$$에서 smooth하므로 $$\dim T_p V = \dim V$$, $$\dim T_p W = \dim W$$이다.

$$\Rightarrow$$ 방향: $$i_p(V, W) = 1$$이면 $$R/(\mathfrak{a} + \mathfrak{b}) \cong \mathbb{K}$$이므로 $$\mathfrak{a} + \mathfrak{b} = \mathfrak{m}_p$$이다. 따라서 $$\mathfrak{m}_p/\mathfrak{m}_p^2$$에서 $$\mathfrak{a}$$의 image와 $$\mathfrak{b}$$의 image의 합이 $$\mathfrak{m}_p/\mathfrak{m}_p^2$$ 전체이다. $$V$$의 tangent space는 $$T_p V = (\mathfrak{m}_p/(\mathfrak{a} + \mathfrak{m}_p^2))^*$$이고 $$T_p \mathbb{A}^n = (\mathfrak{m}_p/\mathfrak{m}_p^2)^*$$이며, 포함 $$T_p V \hookrightarrow T_p \mathbb{A}^n$$은 surjection $$\mathfrak{m}_p/\mathfrak{m}_p^2 \twoheadrightarrow \mathfrak{m}_p/(\mathfrak{a} + \mathfrak{m}_p^2)$$의 쌍대이다. $$T_p V \subseteq T_p \mathbb{A}^n$$의 annihilator는 $$(\mathfrak{a} + \mathfrak{m}_p^2)/\mathfrak{m}_p^2 \subseteq \mathfrak{m}_p/\mathfrak{m}_p^2$$이고, 마찬가지로 $$T_p W \subseteq T_p \mathbb{A}^n$$의 annihilator는 $$(\mathfrak{b} + \mathfrak{m}_p^2)/\mathfrak{m}_p^2$$이다. $$\mathfrak{a} + \mathfrak{b} + \mathfrak{m}_p^2 = \mathfrak{m}_p$$이므로 두 annihilator의 합이 $$\mathfrak{m}_p/\mathfrak{m}_p^2$$ 전체이고, 쌍대에서 $$T_p V + T_p W = T_p \mathbb{A}^n$$을 얻는다.

$$\Leftarrow$$ 방향: $$T_p V + T_p W = \mathbb{A}^n$$이면 [명제 5](#prop5)의 횡단 교차 증명과 동일한 논증에 의해 $$i_p(V, W) = 1$$이다. ∎

</div>

<div class="example" markdown="1">

<ins id="ex12">**예시 12**</ins> $$V: y = 0$$과 $$W: y = x^2$$의 경우 원점에서의 tangent space를 계산해보자. $$V$$의 원점에서의 tangent space는 $$T_0 V = \{(v_1, 0)\} \cong \mathbb{K}$$이고, $$W$$의 tangent space는 $$T_0 W = \{(v_1, 0)\} \cong \mathbb{K}$$이다. 따라서 $$T_0 V + T_0 W = \mathbb{K} \neq \mathbb{K}^2$$이고, [명제 11](#prop11)에 의해 $$i_0(V, W) > 1$$이다. 실제로 [예시 2](#ex2)에서 확인했듯 $$i_0(V, W) = 2$$이다.

</div>

<div class="example" markdown="1">

<ins id="ex13">**예시 13**</ins> $$V: y = 0$$과 $$W: y = x$$의 경우 $$T_0 V = \{(v_1, 0)\}$$, $$T_0 W = \{(v_1, v_1)\}$$이므로 $$T_0 V + T_0 W = \mathbb{K}^2$$이다. 따라서 [명제 11](#prop11)에 의해 $$i_0(V, W) = 1$$이다. 이를 직접 확인하면 $$\mathcal{O}_{\mathbb{A}^2,0}/(y, y-x) = \mathcal{O}_{\mathbb{A}^2,0}/(y,x) \cong \mathbb{K}$$로 1차원 vector space가 된다.

</div>

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[Ful]** W. Fulton, *Intersection Theory*, Springer, 1984.
