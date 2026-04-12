---

title: "유도카테고리"
excerpt: ""

categories: [Math / Homological Algebra]
permalink: /ko/math/homological_algebra/derived_categories
header:
    overlay_image: /assets/images/Math/Homological_Algebra/Derived_Categories.png
    overlay_filter: 0.5
sidebar: 
    nav: "homological_algebra-ko"

date: 2026-04-13
last_modified_at: 2026-04-13
weight: 8
published: false

---

우리는 [§유도함자](/ko/math/homological_algebra/derived_functors)에서 exact하지 않은 functor가 주어졌을 때 이를 해결하는 방법을 살펴보았다. 구체적으로, 우리는 어떠한 left (resp. right) exact functor $$F$$가 주어졌을 때, 대상 $$A$$의 injective (resp. projective) resolution을 택하고 그 resolution의 cohomology (resp. homology)를 취하여 right (resp. left) derived functor를 정의했다. 

주목할 것은 이 과정에서 injective resolution과 projective resolution의 선택은 (co)homology 레벨에서는 영향을 주지 않지만, 구체적인 chain complex 레벨에서는 이들 선택이 자연스럽지 않다는 것이다. 이제 우리는 이를 개념적으로 좀 더 보완하여 언어를 다듬는 작업을 한다. 구체적으로, 우리는 chain complex들을 우리의 대상으로 생각하고, quasi-isomorphic한 chain complex들을 처음부터 같은 것으로 취급하여 이러한 문제를 해결할 것이다. 즉, 우리가 활동하는 영역을 abelian category $$\mathcal{A}$$가 아니라, $$\mathcal{A}$$의 chain complex들로 이루어진 category $$\Ch(\mathcal{A})$$가 우선적인 관심의 대상이 된다.

## Derived Category의 정의

그러나 $$\Ch(\mathcal{A})$$ 자체는 우리의 관심의 대상은 아니다. 우리는 앞서 설명했듯 $$\Ch(\mathcal{A})$$에서 quasi-isomorphism을 모두 같은 것으로 봐야 하므로 이에 대한 quotient 또한 생각해야 한다. 또, 그 이전에 chain homotopic한 chain map들은 모두 같은 것이므로 다음과 같은 정의를 내려야 한다. 

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Abelian category $$\mathcal{A}$$의 *homotopy category* $$K(\mathcal{A})$$는 $$\Ch(\mathcal{A})$$에서 chain homotopic인 사상들을 동일시하여 얻은 quotient category이다. 즉 chain homotopy relation $$\sim$$에 대하여

$$\Hom_{K(\mathcal{A})}(A^\bullet, B^\bullet) = \Hom_{\Ch(\mathcal{A})}(A^\bullet, B^\bullet) /{\sim}$$

이다. 

</div>

그럼 우리는 $$K(\mathcal{A})$$이 additive category인 것을 확인할 수 있다. 한편, 우리는 quasi-isomorphism이 일반적으로 $$K(\mathcal{A})$$에서 isomorphism이 아닌 것은 이미 [§긴 완전열, ⁋정의 4](/ko/math/homological_algebra/long_exact_sequence#def4)에서 확인하였다. 따라서 quasi-isomorphic한 chain complex (up to chain homotopy)을 같은 것으로 보기 위해서 우리는 반드시 quasi-isomorphism의 inverse를 강제로 만들어주어야 한다. 

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> Abelian category $$\mathcal{A}$$의 *derived category* $$D(\mathcal{A})$$는 homotopy category $$K(\mathcal{A})$$에서 quasi-isomorphism의 모임 $$S$$에 대한 Verdier quotient $$K(\mathcal{A})/S$$이다.

</div>

우리는 이 정의를 아주 엄밀하게 다루지는 않지만, 이는 기본적으로 [\[대수적 구조\] §분수체, ⁋정의 2](/ko/math/algebraic_structures/field_of_fractions#def2)의 구성과 다르지 않다. 다른 점은 대상들이 non-commutative하다는 것으로, 이것만 주의하면 우리는 $$K(\mathcal{A})$$의 "localization" $$D(\mathcal{A})$$를 얻어낼 수 있다. 

조금 더 구체적으로, $$D(\mathcal{A})$$의 morphism을 설명할 때 우리는 종종 roof diagram을 설명한다. $$X$$에서 $$Y$$로의 $$D(\mathcal{A})$$에서의 morphism은 다음의 diagram

$$X\overset{s}{\longrightarrow} X'\overset{f}{\longrightarrow}Y$$

으로 표현되며, 여기서 $$s$$는 quasi-isomorphism이고, $$f$$는 chain map이다. 즉, $$D(\mathcal{A})$$ 안에서, $$X$$에서 $$Y$$로의 map은 실제 map이 아니라, $$X$$의 quasi-isomorphism class에 속하는 $$X'$$에서 $$Y$$로의 chain map (정확히는 up to chain homotopy)인 것으로 생각할 수 있다. 이 과정에서 우리는 실제로 chain map으로서 존재하지는 않을 수도 있는 $$s^{-1}$$을 추가하게 되어 위의 설명에서의 "localization" analogue가 생기게 되는 것이다. 

사상은 roof diagram 

$$A \xleftarrow{s} B \xrightarrow{f} C,\qquad s \in S$$

의 equivalence class로 정의된다. 여기서 $$s \in S$$는 invert될 quasi-isomorphism이고, $$f$$가 우리가 실제로 정의하고자 하는 사상이다. 이 때 두 roof 

$$A \xleftarrow{s_1} B_1 \xrightarrow{f_1} C, \qquad A \xleftarrow{s_2} B_2 \xrightarrow{f_2} C$$

가 equivalent한 것은 roof 

$$B_1 \xleftarrow{s'} B_3 \xrightarrow{f'} B_2,\qquad s \in S$$

가 존재하여 이로부터 얻어지는 $$A\leftarrow B_3\rightarrow C$$이 roof인 것이다. 

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> Complex $$A^\bullet \in D(\mathcal{A})$$가 *bounded below*이라는 것은 $$H^i(A^\bullet) = 0$$인 $$i$$가 아래로 유계인 것이다, 즉 충분히 작은 $$n$$에 대해 $$i < n$$이면 $$H^i(A^\bullet) = 0$$인 것이다. Bounded below complex들로 이루어진 full subcategory를 $$D^+(\mathcal{A})$$로 쓴다. 비슷하게 bounded above ($$H^i = 0$$ for $$i \gg 0$$)인 complex들의 category를 $$D^-(\mathcal{A})$$, bounded (양쪽에서 유계)인 complex들의 category를 $$D^b(\mathcal{A})$$로 쓴다.

</div>

$$D^+(\mathcal{A})$$는 injective resolution을 사용한 작업에 자연스러운 무대이며, $$D^-(\mathcal{A})$$는 projective resolution에 자연스럽다. 대부분의 응용에서는 bounded derived category $$D^b(\mathcal{A})$$가 주요 무대가 된다.

## Shift Functor

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> $$D(\mathcal{A})$$ 위의 *shift functor* $$[n] \colon D(\mathcal{A}) \to D(\mathcal{A})$$는 complex $$A^\bullet$$을 $$n$$칸 이동시키는 것이다. 구체적으로 $$(A[n])^i = A^{i+n}$$이고, 미분 사상은 $$(d_{A[n]})^i = (-1)^n d_A^{i+n}$$으로 정의한다.

</div>

Shift functor는 derived category의 기본 연산이다. Cohomology에 대해서는

$$H^i(A[n]) = H^{i+n}(A)$$

가 성립한다. 이는 $$d_{A[n]}$$의 정의에서 $$(-1)^n$$ 인자가 cohomology 계산에 영향을 주지 않기 때문이다. 예를 들어, 대상 $$A$$를 $$A[0]$$으로 볼 때, $$A[n]$$은 $$-n$$번째 차수에 $$A$$가 있고 나머지는 $$0$$인 complex이다. 따라서 $$H^{-n}(A[n]) = A$$이고 다른 차수에서의 cohomology는 $$0$$이다.

Shift functor는 derived adjunction 등에서 차수의 정합성을 맞추는 역할을 한다.


## Derived Functor

Derived functor를 정의하기 전에, complex 수준의 resolution 개념을 도입한다.

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> Complex $$P \in K(\mathcal{A})$$가 *$$K$$-projective*라는 것은, 임의의 quasi-isomorphism $$s \colon A \to B$$ in $$K(\mathcal{A})$$에 대해 유도된 사상

$$\Hom_{K(\mathcal{A})}(B, P) \xrightarrow{s^*} \Hom_{K(\mathcal{A})}(A, P)$$

이 isomorphism인 것이다. 즉 $$P$$는 $$K(\mathcal{A})$$에서 Hom functor $$\Hom(-, P)$$를 quasi-isomorphism에 대해 invariant하게 만드는 complex이다.

</div>

$$K$$-projective complex는 projective resolution의 complex 버전이다. 대상 $$A$$의 projective resolution $$P_\bullet \to A$$는 $$K$$-projective complex이며, 임의의 projective complex도 $$K$$-projective이다.

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> Complex $$I \in K(\mathcal{A})$$가 *$$K$$-injective*라는 것은, 임의의 quasi-isomorphism $$s \colon A \to B$$에 대해 유도된 사상

$$\Hom_{K(\mathcal{A})}(I, A) \xrightarrow{s_*} \Hom_{K(\mathcal{A})}(I, B)$$

이 isomorphism인 것이다.

</div>

$$K$$-injective complex는 injective resolution의 complex 버전이다. Injective complex는 $$K$$-injective이며, bounded below complex에 대해 이러한 resolution이 존재하는 것은 잘 알려져 있다. 이 결과는 unbounded complex에서 derived functor를 정의하는 데 필수적이다.


Derived category에서 exact하지 않은 functor를 다루는 표준적인 방법은 derived functor이다.

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> Additive functor $$F \colon \mathcal{A} \to \mathcal{B}$$가 주어졌다고 하자.

1. $$F$$가 left exact이고 $$\mathcal{A}$$가 enough injective를 갖는다고 하자. $$A^\bullet \in D^+(\mathcal{A})$$의 *right derived functor*는 $$R F(A^\bullet) = F(I^\bullet)$$로 정의한다. 여기서 $$A^\bullet \to I^\bullet$$은 $$K$$-injective resolution이다.
2. $$F$$가 right exact이고 $$\mathcal{A}$$가 enough projective를 갖는다고 하자. $$A^\bullet \in D^-(\mathcal{A})$$의 *left derived functor*는 $$L F(A^\bullet) = F(P_\bullet)$$로 정의한다. 여기서 $$P_\bullet \to A^\bullet$$은 $$K$$-projective resolution이다.

</div>

대상 하나에 대한 derived functor와의 관계는 다음과 같다. $$A \in \mathcal{A}$$를 $$A[0] \in D(\mathcal{A})$$로 보면,

$$H^i(R F(A[0])) = (R^i F)(A)$$

이 성립한다. 즉 $$R F$$는 $$R^i F$$를 모든 차수에서 동시에 포착하는 complex 수준의 functor이다. 비슷하게 $$H_i(L F(A[0])) = (L_i F)(A)$$이다.

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> $$R F$$와 $$L F$$는 derived category에서의 functor이다. 즉 quasi-isomorphism을 보내 quasi-isomorphism으로 보낸다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

Quasi-isomorphism $$s \colon A^\bullet \to B^\bullet$$이 주어졌다고 하자. $$A^\bullet \to I^\bullet$$, $$B^\bullet \to J^\bullet$$을 각각 $$K$$-injective resolution이라 하자. $$K$$-injective resolution의 lifting property에 의해, quasi-isomorphism $$s$$는 $$I^\bullet$$과 $$J^\bullet$$ 사이의 사상 $$\tilde{s} \colon I^\bullet \to J^\bullet$$으로 유일하게 (homotopy까지) 확장된다. 따라서 $$F(\tilde{s}) \colon F(I^\bullet) \to F(J^\bullet)$$을 얻는다. $$K$$-injective resolution 위에서 $$F$$를 적용한 것이므로 $$F(\tilde{s})$$는 quasi-isomorphism이며, 따라서 $$D(\mathcal{B})$$에서 $$R F(A^\bullet) \cong R F(B^\bullet)$$이다. Left derived functor에 대해서도 비슷하다.

</details>

구체적인 예로서, $$\mathcal{A}$$ 위에서의 Hom functor $$\Hom(-, B)$$는 contravariant left exact functor이므로 이를 derived하여 complex 수준의 derived Hom을 얻을 수 있다. $$\mathbf{R}\Hom$$을 정의하면, $$\mathbf{R}\Hom(A, B)$$의 cohomology는 $$\Ext^i(A, B)$$와 일치한다.

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10**</ins> $$\mathcal{A}$$가 enough injective를 갖는 abelian category라고 하자. 그럼 모든 $$A, B \in \mathcal{A}$$에 대해

$$H^{i}(\mathbf{R}\Hom(A, B)) \cong \Ext^i(A, B)$$

이 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$\mathbf{R}\Hom(A, B)$$를 정확히 정의하자. $$A$$를 $$A[0] \in D(\mathcal{A})$$로 보고, projective resolution $$P_\bullet \to A$$를 선택한다. $$P_\bullet$$은 $$K$$-projective complex이므로

$$\mathbf{R}\Hom(A, B) = \Hom(P_\bullet, B)$$

로 정의한다. 여기서 우변은 complex $$\Hom(P_\bullet, B)$$를 나타낸다. $$P_\bullet \to A$$가 resolution이므로 [§Ext와 Tor](/ko/math/homological_algebra/ext_and_tor)의 정의에 의해 $$H^i(\Hom(P_\bullet, B)) = \Ext^i(A, B)$$이다.

더 정교하게, $$B$$에도 injective resolution $$B \to I^\bullet$$을 취하면 $$\Hom(P_\bullet, I^\bullet)$$은 이중 복합체를 이루며, 그 total complex가 $$\mathbf{R}\Hom(A, B)$$를 준다. 그러나 $$P_\bullet$$이 $$K$$-projective이므로 한쪽만 resolution을 취해도 cohomology에는 영향을 주지 않는다.

</details>

비슷하게 tensor product의 left derived functor $$L(A \otimes B) = A \otimes^L B$$를 정의할 수 있으며, $$\Tor_i(A, B) = H^{-i}(A \otimes^L B)$$가 성립한다.

## Triangulated Category

Derived category $$D(\mathcal{A})$$는 단순한 category가 아니라 *triangulated category*의 구조를 갖는다. 이 구조는 abelian category에서 short exact sequence가 하던 역할을 derived category에서 대신한다.

<div class="definition" markdown="1">

<ins id="def8">**정의 8**</ins> *Triangulated category*는 다음 구조를 갖춘 additive category $$(\mathcal{T}, [1], \mathcal{S})$$이다.

1. *Shift functor* $$[1] \colon \mathcal{T} \to \mathcal{T}$$: 자기 동형사상이며, $$[0] = \id$$이고 $$[n+1] = [1] \circ [n]$$이다.
2. *Distinguished triangle*들의 모임 $$\mathcal{S}$$: 각 distinguished triangle은

$$A \overset{f}{\to} B \overset{g}{\to} C \overset{h}{\to} A[1]$$

의 형태를 갖는다. 이 모임은 다음 공리를 만족한다.
    - (TR1) Isomorphism은 distinguished triangle을 보낸다. 모든 사상 $$f \colon A \to B$$에 대해 distinguished triangle $$A \to B \to C \to A[1]$$가 존재한다. 또한 $$A \overset{\id}{\to} A \to 0 \to A[1]$$은 distinguished triangle이다.
    - (TR2) $$A \to B \to C \to A[1]$$이 distinguished triangle이면 $$B \to C \to A[1] \to B[1]$$도 distinguished triangle이다.
    - (TR3) 두 distinguished triangle이 주어졌을 때, 사상들 $$(u, v, w)$$에 의한 morphism이 commute하면, $$w$$를 포함하는 확장이 존재한다.
    - (TR4) Octahedral axiom: 합성 $$B \xrightarrow{g} C \xrightarrow{h} D$$이 주어졌을 때, 이와 연관된 octahedron을 이루는 세 개의 distinguished triangle이 존재한다.

</div>

[§긴 완전열, ⁋정의 8](/ko/math/homological_algebra/long_exact_sequence#def6)에서 chain complex에 대해 정의한 mapping cone을 cochain complex로 다시 쓰면 다음과 같다. 두 cochain complex $$A^\bullet$$, $$B^\bullet$$ 사이의 사상 $$f \colon A^\bullet \to B^\bullet$$이 주어졌을 때, *mapping cone* $$C(f)^\bullet$$은 차수별로 $$C(f)^i = B^i \oplus A^{i+1}$$이고, 미분 사상이 $$(b, a) \mapsto (d_B b + f(a), -d_A a)$$로 주어지는 cochain complex이다.

Mapping cone은 사상 $$f$$가 "얼마나 isomorphism에서 벗어나는지"를 측정하는 도구이다 ([§긴 완전열, ⁋정의 8](/ko/math/homological_algebra/long_exact_sequence#def6) 참고). $$C(f)^\bullet$$의 cohomology를 계산해보자. 정의에 의해 $$H^i(C(f))$$는 $$d_B b + f(a) = 0$$이고 $$d_A a = 0$$인 쌍 $$(b, a) \in B^i \oplus A^{i+1}$$을, $$(d_B b' + f(a'), -d_A a')$$ 형태의 원소들로 나눈 것이다.

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> 사상 $$f \colon A^\bullet \to B^\bullet$$이 quasi-isomorphism인 것과 $$H^i(C(f)) = 0$$이 모든 $$i$$에 대해 성립하는 것은 동치이다. 이는 [§긴 완전열, ⁋따름정리 9](/ko/math/homological_algebra/long_exact_sequence#cor9)의 cochain 버전이다.

</div>

[§긴 완전열, ⁋따름정리 9](/ko/math/homological_algebra/long_exact_sequence#cor9)의 증명에서는 homology long exact sequence와 five lemma를 사용하였는데, cochain complex에 대해서도 동일한 논증이 적용된다.

Distinguished triangle의 직관은 short exact sequence의 "derived version"이라는 것이다. Abelian category에서 short exact sequence $$0 \to A' \xrightarrow{f} A \xrightarrow{g} A'' \to 0$$이 있으면, $$f$$를 complex 사이의 사상 $$A'[0] \to A[0]$$로 볼 수 있고, 이때 $$C(f)$$는 $$A''[0]$$과 quasi-isomorphic하다. 즉 short exact sequence는 derived category에서 distinguished triangle

$$A'[0] \overset{f}{\to} A[0] \to A''[0] \to A'[1]$$

으로 나타난다. 일반적인 사상 $$f$$에 대해서는, $$f$$가 isomorphism에서 벗어나는 정도가 $$C(f)$$의 cohomology로 측정되며, cohomology long exact sequence가 자연스럽게 나타난다.

Derived category $$D(\mathcal{A})$$에서 distinguished triangle은 complex 사이의 사상 $$f$$와 그 mapping cone $$C(f)$$로부터 얻어진 삼각형

$$A \overset{f}{\to} B \overset{g}{\to} C(f) \overset{h}{\to} A[1]$$

들로 구성된다. 여기서 $$g \colon B^i \to C(f)^i = B^i \oplus A^{i+1}$$는 $$b \mapsto (b, 0)$$이고, $$h \colon C(f)^i \to A[1]^i = A^{i+1}$$는 $$(b, a) \mapsto a$$이다.

<div class="proposition" markdown="1">

<ins id="prop11">**명제 11**</ins> $$R F \colon D^+(\mathcal{A}) \to D^+(\mathcal{B})$$는 triangulated functor이다. 즉 distinguished triangle

$$A \to B \to C \to A[1]$$

이 주어지면

$$R F(A) \to R F(B) \to R F(C) \to R F(A)[1]$$

도 distinguished triangle이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$A \to B$$를 사상으로 보고, 이들의 $$K$$-injective resolution들을 각각 $$I_A^\bullet$$, $$I_B^\bullet$$이라 하자. $$K$$-injective resolution의 lifting property에 의해, 사상 $$A \to B$$는 $$I_A^\bullet \to I_B^\bullet$$로 확장된다. $$C = C(f)$$의 $$K$$-injective resolution $$I_C^\bullet$$을 취하면, $$I_A^\bullet \to I_B^\bullet \to I_C^\bullet \to I_A^\bullet[1]$$은 $$K$$-injective complex들 사이의 distinguished triangle이며, $$F$$를 적용한 뒤 $$D(\mathcal{B})$$에서 보면 원하는 distinguished triangle을 얻는다. Bounded below $$K$$-injective complex들은 $$K(\mathcal{A})$$의 삼각 부분 범주를 이루므로, mapping cone도 $$K$$-injective가 되고 이 diagram이 commute함을 알 수 있다.

</details>

## Derived Adjunction

Category theory에서 adjunction은 두 functor 사이의 가장 중요한 관계 중 하나이다. Derived category에서도 adjunction이 성립하며, 이를 *derived adjunction*이라 부른다.

<div class="proposition" markdown="1">

<ins id="prop12">**명제 12**</ins> Abelian category $$\mathcal{A}, \mathcal{B}$$ 사이의 additive functor들 $$F \colon \mathcal{A} \to \mathcal{B}$$ (right exact), $$G \colon \mathcal{B} \to \mathcal{A}$$ (left exact)가 adjoint pair $$F \dashv G$$를 이룬다고 하자. 그럼 derived category에서

$$L F \colon D^-(\mathcal{A}) \to D^-(\mathcal{B}), \qquad R G \colon D^+(\mathcal{B}) \to D^+(\mathcal{A})$$

는 adjoint pair $$L F \dashv R G$$를 이룬다. 즉 모든 $$A^\bullet \in D^-(\mathcal{A})$$, $$B^\bullet \in D^+(\mathcal{B})$$에 대해

$$\Hom_{D(\mathcal{B})}(L F(A^\bullet), B^\bullet) \cong \Hom_{D(\mathcal{A})}(A^\bullet, R G(B^\bullet))$$

이 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$A^\bullet$$의 $$K$$-projective resolution $$P_\bullet$$과 $$B^\bullet$$의 $$K$$-injective resolution $$I^\bullet$$을 선택하자. $$P_\bullet$$은 $$K$$-projective이므로 $$\Hom_{D(\mathcal{B})}(F(P_\bullet), I^\bullet)$$의 계산에서 $$F(P_\bullet)$$을 resolution로 대체할 수 있다. 원래의 adjunction $$F \dashv G$$에 의해, complex 수준에서

$$\Hom_{\Ch(\mathcal{B})}(F(P_\bullet), I^\bullet) \cong \Hom_{\Ch(\mathcal{A})}(P_\bullet, G(I^\bullet))$$

이 성립한다. 이 동형은 각 차수별 adjunction $$\Hom_\mathcal{B}(F(P^n), I^m) \cong \Hom_\mathcal{A}(P^n, G(I^m))$$을 모아서 complex 수준으로 얻은 것이다. $$P_\bullet$$이 $$K$$-projective이고 $$I^\bullet$$이 $$K$$-injective이므로, 좌변은 $$\Hom_{K(\mathcal{B})}(F(P_\bullet), I^\bullet) = \Hom_{D(\mathcal{B})}(L F(A^\bullet), B^\bullet)$$로, 우변은 $$\Hom_{K(\mathcal{A})}(P_\bullet, G(I^\bullet)) = \Hom_{D(\mathcal{A})}(A^\bullet, R G(B^\bullet))$$로 환원된다.

</details>

가장 대표적인 예는 tensor product와 Hom의 adjunction이다. $$\mathcal{A}$$가 enough projective를 갖는다고 하자. Tensor product $$-\otimes B$$는 right exact이고 $$\Hom(B, -)$$는 left exact이며, [\[다중선형대수학\] §Hom과 텐서곱](/ko/math/multilinear_algebra/hom_and_tensor)에서 본 adjunction

$$\Hom(A \otimes B, C) \cong \Hom(A, \Hom(B, C))$$

의 derived version으로

$$\Hom_{D(\mathcal{A})}(A \otimes^L B, C) \cong \Hom_{D(\mathcal{A})}(A, \mathbf{R}\Hom(B, C))$$

를 얻는다.

Derived adjunction은 algebraic geometry에서 특히 중요하다. Geometric morphism $$f \colon X \to Y$$에 대해 triple adjunction

$$L f^* \dashv R f_* \dashv f^!$$

이 성립한다. 여기서 $$f^!$$는 derived category에서만 자연스럽게 정의되는 functor로, Grothendieck duality의 핵심이다. 이에 대해서는 algebraic geometry 쪽 글에서 다룬다.

---

**참고문헌**

**[GM]** S. I. Gelfand, Y. I. Manin, *Methods of homological algebra*, Springer, 2003.
**[Ver]** J.-L. Verdier, *Des catégories dérivées des catégories abéliennes*, Astérisque **239** (1996).
**[Wei]** C. A. Weibel, *An introduction to homological algebra*, Cambridge University Press, 1994.