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

평면 $$\mathbb{A}^2$$에서 두 곡선 $$y = 0$$과 $$y = x^2$$이 원점에서 만난다. 이 두 곡선은 단순히 "만난다"고 말하는 것으로는 충분하지 않다. 원점에서 얼마나 "강하게" 만나는가? $$y = 0$$과 $$y = x$$은 원점에서 단순히 "교차"하지만, $$y = 0$$과 $$y = x^2$$은 원점에서 $$x^2$$만큼의 "접촉"을 갖는다.

이러한 교차의 "복잡도"를 수치화하기 위해, 우리는 variety를 정의하는 ideal의 local ring에서의 quotient dimension을 사용한다. 이는 다음과 같은 직관을 갖는다: $$V, W$$를 정의하는 방정식 $$f_1, \ldots, f_k$$가 local ring $$\mathcal{O}_{\mathbb{A}^n, p}$$에서 생성하는 ideal $$(f_1, \ldots, f_k)$$의 quotient $$\mathcal{O}_{\mathbb{A}^n, p} / (f_1, \ldots, f_k)$$의 dimension이 클수록, 방정식들이 점 $$p$$ 근처에서 더 "깊게" 결합되어 있음을 의미한다. 즉, 두 variety가 $$p$$에서 더 복잡하게 교차함을 반영한다.

**Intersection multiplicity**는 두 variety가 한 점에서 얼마나 "복잡하게" 만나는지를 측정하는 정수이다. 이것은 Bézout's theorem, Chow groups 등의 기초가 된다.

## Definition

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Affine space $$\mathbb{A}^n$$의 점 $$p$$에서 두 variety $$V, W$$의 **intersection multiplicity<sub>교차 중복도</sub>** $$i_p(V, W)$$를 다음과 같이 정의한다:

$$i_p(V, W) = \dim_{\mathbb{K}} \mathcal{O}_{\mathbb{A}^n, p} / (I(V) + I(W))$$

여기서 $$\mathcal{O}_{\mathbb{A}^n, p}$$는 $$p$$에서의 local ring ([\[가환대수학\] §국소화, ⁋정의 1](/ko/math/commutative_algebra/localization#def1))이다.

</div>

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins> $$\mathbb{A}^2$$에서 $$V: y = 0$$과 $$W: y = x^2$$가 원점에서 만난다.

- $$I(V) = (y)$$, $$I(W) = (y - x^2)$$
- $$\mathcal{O}_{\mathbb{A}^2, 0} / (y, y - x^2) = \mathcal{O}_{\mathbb{A}^2, 0} / (y, x^2)$$
- 이것은 basis $$\{1, x\}$$를 갖는 2차원 vector space

따라서 $$i_0(V, W) = 2$$이다.

</div>

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> $$\mathbb{A}^2$$에서 $$V: y = 0$$과 $$W: y = x^3$$이 원점에서 만난다.

$$\mathcal{O}_{\mathbb{A}^2, 0} / (y, x^3)$$은 basis $$\{1, x, x^2\}$$를 갖는 3차원 vector space이다.

따라서 $$i_0(V, W) = 3$$이다.

</div>

## Properties

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> 두 variety $$V, W \subseteq \mathbb{A}^n$$이 점 $$p \in V \cap W$$에서 **transversely intersect<sub>횡단 교차</sub>**한다는 것은 tangent space의 합이 전체 공간을 채우는 것이다:

$$T_p V + T_p W = \mathbb{A}^n$$

Tangent space $$T_p V$$의 정의는 [§Tangent_spaces_and_smoothness](/ko/math/algebraic_geometry/tangent_spaces_and_smoothness)를 참조하라.

</div>

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> Intersection multiplicity의 기본 성질:

1. $$i_p(V, W) \geq 0$$이고, $$p \notin V \cap W$$이면 $$i_p(V, W) = 0$$
2. $$V, W$$가 $$p$$에서 transversely intersect하면 $$i_p(V, W) = 1$$ ([정의 4](#def4))
3. $$i_p(V, W) = i_p(W, V)$$ (symmetry)
4. $$\dim V + \dim W = n$$이면 $$i_p(V, W) < \infty$$

*증명.* $$R = \mathcal{O}_{\mathbb{A}^n, p}$$, $$\mathfrak{a} = I(V)$$, $$\mathfrak{b} = I(W)$$라 하자.

(1) $$i_p(V, W)$$는 vector space의 dimension이므로 자명히 $$\geq 0$$이다. $$p \notin V \cap W$$이면 어떤 $$f \in \mathfrak{a} + \mathfrak{b}$$가 $$p$$에서 $$0$$이 아니고, 따라서 $$R$$에서 invertible이다. 즉 $$\mathfrak{a} + \mathfrak{b} = R$$이 되어 $$R/(\mathfrak{a} + \mathfrak{b}) = 0$$이다.

(2) $$V, W$$가 $$p$$에서 transversely intersect하면 $$T_p V + T_p W = \mathbb{A}^n$$이다. Nakayama의 보조정리에 의해 $$\mathfrak{a} + \mathfrak{b}$$는 $$\mathfrak{m}_p$$-primary이고, $$R/(\mathfrak{a} + \mathfrak{b})$$는 $$\mathbb{K}$$와 동형인 1차원 vector space이다. 따라서 $$i_p(V, W) = 1$$이다.

(3) $$\mathfrak{a} + \mathfrak{b} = \mathfrak{b} + \mathfrak{a}$$이므로 $$R/(\mathfrak{a} + \mathfrak{b}) \cong R/(\mathfrak{b} + \mathfrak{a})$$에서 자명하게 성립한다.

(4) $$\dim V = \dim(R/\mathfrak{a})$$, $$\dim W = \dim(R/\mathfrak{b})$$이다. 가환대수학의 dimension formula에 의해 $$\dim(R/(\mathfrak{a} + \mathfrak{b})) \geq \dim(R/\mathfrak{a}) + \dim(R/\mathfrak{b}) - n = 0$$이고, 등호가 성립한다. 즉 $$R/(\mathfrak{a} + \mathfrak{b})$$는 Krull dimension $$0$$의 local ring이므로 Artinian이고, 따라서 유한 차원 $$\mathbb{K}$$-vector space이다. ∎

</div>

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6 (Additivity)**</ins> $$V = V_1 \cup V_2$$이면:

$$i_p(V, W) = i_p(V_1, W) + i_p(V_2, W)$$

*증명.* $$R = \mathcal{O}_{\mathbb{A}^n, p}$$, $$I_1 = I(V_1)$$, $$I_2 = I(V_2)$$, $$J = I(W)$$라 하자. $$I(V) = I_1 \cap I_2$$에 대해 다음 exact sequence가 존재한다:

$$0 \to R/(I_1 \cap I_2 + J) \to R/(I_1 + J) \oplus R/(I_2 + J) \to R/(I_1 + I_2 + J) \to 0$$

첫 번째 항은 $$R/(I(V) + I(W))$$이므로 dimension이 $$i_p(V, W)$$이다. 만약 $$V_1$$과 $$V_2$$가 $$p$$를 포함하는 공통 irreducible component를 갖지 않으면, $$I_1 + I_2$$는 $$p$$에서 $$\mathfrak{m}_p$$-primary가 되어 $$R/(I_1 + I_2 + J)$$의 dimension은 무시할 수 있거나 $$0$$이 되고, 따라서 $$i_p(V, W) = i_p(V_1, W) + i_p(V_2, W)$$를 얻는다. ∎

</div>

## Projective Case

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> $$\mathbb{P}^n$$의 점 $$p$$에서 두 variety $$V, W$$의 intersection multiplicity를 affine chart에서의 값으로 정의한다. $$p$$를 포함하는 임의의 affine chart $$U \cong \mathbb{A}^n$$을 선택하고, $$V \cap U$$, $$W \cap U$$의 affine intersection multiplicity를 취한다. 이 값은 affine chart의 선택과 무관하다.

왜 무관한가? $$U_1, U_2$$가 $$p$$를 포함하는 두 affine chart라면, $$U_1 \cap U_2$$는 open set이고, local ring $$\mathcal{O}_{\mathbb{P}^n, p}$$는 $$U_1$$, $$U_2$$ 모두에서의 local ring과 자연스럽게 동형이다. Intersection multiplicity의 정의가 $$p$$에서의 local ring만에 의존하므로, chart의 선택에 영향받지 않는다.

</div>

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8 (Bezout for Curves in $$\mathbb{P}^2$$)**</ins> $$\mathbb{P}^2$$에서 degree $$m$$, $$n$$의 두 curve $$C, D$$가 공통 성분을 갖지 않으면:

$$\sum_{p \in C \cap D} i_p(C, D) = mn$$

여기서 curve의 degree $$\deg(C)$$는 $$C$$를 정의하는 homogeneous polynomial의 차수이다.

*증명 sketch.* 핵심 아이디어는 다음과 같다. $$C$$에 대한 resultants와 Hilbert polynomial을 사용하여 교차점의 intersection multiplicity 총합이 $$mn$$임을 보인다. 자세한 증명은 [§Bézout_Theorem](/ko/math/algebraic_geometry/bezout_theorem)에서 다룬다.

</div>

<div class="example" markdown="1">

<ins id="ex9">**예시 9**</ins> Circle $$C: x^2 + y^2 = z^2$$과 line $$L: y = z$$을 $$\mathbb{P}^2$$에서 생각하자.

$$C \cap L$$은 한 점 $$[0:1:1]$$에서 multiplicity 2로 만난다. (Substituting $$y = z$$ into $$x^2 + y^2 = z^2$$ gives $$x^2 = 0$$.)

Check: $$\deg C = 2$$, $$\deg L = 1$$, $$2 \times 1 = 2$$. ✓

</div>

## Dimension Formula

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10**</ins> $$\dim V + \dim W = n$$이고 $$V \cap W$$가 finite set이면:

$$\sum_{p \in V \cap W} i_p(V, W) = \deg(V) \cdot \deg(W)$$

여기서 projective variety $$V$$의 degree $$\deg(V)$$는 generic hyperplane $$H$$와 $$V$$의 교차 $$V \cap H$$의 점 개수 (각 점의 intersection multiplicity 합)로 정의된다. 즉, $$\deg(V) = \sum_{p \in V \cap H} i_p(V, H)$$이다.

*증명 sketch.* Bézout의 theorem의 일반 형태이다. $$V, W$$를 각각 $$\deg(V)$$, $$\deg(W)$$개의 hyperplane의 intersection으로 표현한 뒤, additivity와 induction으로 증명한다. 자세한 증명은 [§Bézout_Theorem](/ko/math/algebraic_geometry/bezout_theorem)에서 다룬다.

</div>

## Local Ring Interpretation

<div class="proposition" markdown="1">

<ins id="prop11">**명제 11**</ins> $$V, W$$가 $$p$$에서 smooth하고 transversely intersect하면 ([정의 4](#def4)):

$$i_p(V, W) = \dim_{\mathbb{K}} \mathcal{O}_{V \cap W, p}$$

즉, intersection multiplicity는 local ring의 dimension이다.

</div>

<div class="example" markdown="1">

<ins id="ex12">**예시 12 (Double point)**</ins> $$V: y = 0$$, $$W: y = x^2$$의 경우:

- $$V \cap W$$는 점 $$p = (0, 0)$$ 하나
- $$\mathcal{O}_{V \cap W, p} = \mathbb{K}[x]_{(x)} / (x^2)$$
- Dimension = 2

따라서 $$i_p(V, W) = 2$$이다.

</div>

## Relation to Tangent Spaces

<div class="proposition" markdown="1">

<ins id="prop13">**명제 13**</ins> $$V, W$$가 $$p$$에서 smooth하면:

$$i_p(V, W) = 1 \iff T_p V + T_p W = \mathbb{A}^n$$

즉, tangent space가 transversely intersect하면 ([정의 4](#def4)) multiplicity 1이다.

*증명.* $$\Rightarrow$$ 방향: $$i_p(V, W) = 1$$이면 $$R/(\mathfrak{a} + \mathfrak{b}) \cong \mathbb{K}$$이므로 $$\mathfrak{m}_p = \mathfrak{a} + \mathfrak{b} + \mathfrak{m}_p^2$$이다. 따라서 $$\mathbb{K}$$-vector space로서 $$\mathfrak{m}_p / \mathfrak{m}_p^2 = (\mathfrak{a} + \mathfrak{b})/\mathfrak{m}_p^2$$. 좌변은 $$\mathbb{A}^n$$의 cotangent space $$\mathfrak{m}_p/\mathfrak{m}_p^2$$이고, 우변은 $$T_p V$$와 $$T_p W$$의 cotangent space의 합이다. 따라서 $$T_p V + T_p W = \mathbb{A}^n$$이다.

$$\Leftarrow$$ 방향: $$T_p V + T_p W = \mathbb{A}^n$$이면 [명제 5](#prop5)(2)에 의해 $$i_p(V, W) = 1$$이다. ∎

</div>

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[Ful]** W. Fulton, *Intersection Theory*, Springer, 1984.
