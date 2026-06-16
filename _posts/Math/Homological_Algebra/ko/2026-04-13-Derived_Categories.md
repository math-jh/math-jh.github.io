---
title: "유도카테고리"
description: "homotopy category에서 chain homotopic한 사상들을 동일시하고, quasi-isomorphism의 역을 공식적으로 부여하여 정의하는 유도카테고리의 구조를 다룬다."
excerpt: "Chain complex와 quasi-isomorphism을 통한 derived category 구성"

categories: [Math / Homological Algebra]
permalink: /ko/math/homological_algebra/derived_categories
sidebar: 
    nav: "homological_algebra-ko"

date: 2026-04-13
weight: 8

---

우리는 [§유도함자](/ko/math/homological_algebra/derived_functors)에서 exact하지 않은 functor가 주어졌을 때 이를 해결하는 방법을 살펴보았다. 구체적으로, 우리는 어떠한 left (resp. right) exact functor $$F$$가 주어졌을 때, 대상 $$A$$의 injective (resp. projective) resolution을 택하고 그 resolution의 cohomology (resp. homology)를 취하여 right (resp. left) derived functor를 정의했다. 

주목할 것은 이 과정에서 injective resolution과 projective resolution의 선택은 (co)homology 레벨에서는 영향을 주지 않지만, 구체적인 chain complex 레벨에서는 이들 선택이 자연스럽지 않다는 것이다. 이제 우리는 이를 개념적으로 좀 더 보완하여 언어를 다듬는 작업을 한다. 구체적으로, 우리는 chain complex들을 우리의 대상으로 생각하고, quasi-isomorphic한 chain complex들을 처음부터 같은 것으로 취급하여 이러한 문제를 해결할 것이다. 즉, 우리가 활동하는 영역을 abelian category $$\mathcal{A}$$가 아니라, $$\mathcal{A}$$의 chain complex들로 이루어진 category $$\Ch(\mathcal{A})$$가 우선적인 관심의 대상이 된다.

## Derived Category의 정의

그러나 $$\Ch(\mathcal{A})$$ 자체는 우리의 관심의 대상은 아니다. 우리는 앞서 설명했듯 $$\Ch(\mathcal{A})$$에서 quasi-isomorphism을 모두 같은 것으로 봐야 하므로 이에 대한 quotient 또한 생각해야 한다. 또, 그 이전에 chain homotopic한 chain map들은 모두 같은 것이므로 다음과 같은 정의를 내려야 한다. 

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Abelian category $$\mathcal{A}$$의 *homotopy category* $$K(\mathcal{A})$$는 $$\Ch(\mathcal{A})$$에서 chain homotopic인 map들을 동일시하여 얻은 quotient category이다. 즉 chain homotopy relation $$\sim$$에 대하여

$$\Hom_{K(\mathcal{A})}(A^\bullet, B^\bullet) = \Hom_{\Ch(\mathcal{A})}(A^\bullet, B^\bullet) /{\sim}$$

이다. 

</div>

그럼 우리는 $$K(\mathcal{A})$$이 additive category인 것을 확인할 수 있다. 한편, 우리는 quasi-isomorphism이 일반적으로 $$K(\mathcal{A})$$에서 isomorphism이 아닌 것은 이미 [§긴 완전열, ⁋정의 4](/ko/math/homological_algebra/long_exact_sequence#def4)에서 확인하였다. 따라서 quasi-isomorphic한 chain complex (up to chain homotopy)을 같은 것으로 보기 위해서 우리는 반드시 quasi-isomorphism의 inverse를 강제로 만들어주어야 한다. 

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> Abelian category $$\mathcal{A}$$의 *derived category* $$D(\mathcal{A})$$는 homotopy category $$K(\mathcal{A})$$에서 quasi-isomorphism의 모임 $$S$$에 대한 Verdier quotient $$K(\mathcal{A})/S$$이다.

</div>

우리는 이 정의를 아주 엄밀하게 다루지는 않지만, 이는 기본적으로 [\[대수적 구조\] §분수체, ⁋정의 2](/ko/math/algebraic_structures/field_of_fractions#def2)의 구성과 다르지 않다. 다른 점은 대상들이 non-commutative하다는 것으로, 이것만 주의하면 우리는 $$K(\mathcal{A})$$의 "localization" $$D(\mathcal{A})$$를 얻어낼 수 있다.

조금 더 구체적으로, $$D(\mathcal{A})$$의 morphism을 설명할 때 우리는 종종 roof diagram을 사용하여 설명한다. $$X$$에서 $$Y$$로의 $$D(\mathcal{A})$$에서의 morphism은 다음의 diagram

$$X\overset{s}{\longleftarrow} X'\overset{f}{\longrightarrow}Y$$

으로 표현되며, 여기서 $$s$$는 quasi-isomorphism이고, $$f$$는 chain map이다. 즉, $$D(\mathcal{A})$$ 안에서, $$X$$에서 $$Y$$로의 map은 실제 map이 아니라, $$X$$의 quasi-isomorphism class에 속하는 $$X'$$에서 $$Y$$로의 chain map (정확히는 up to chain homotopy)인 것으로 생각할 수 있다. 이 과정에서 우리는 실제로 chain map으로서 존재하지는 않을 수도 있는 $$s^{-1}$$을 추가하게 되어 위의 설명에서의 "localization" analogue가 생기게 되는 것이다.

이러한 관점에서, 어떤 roof들이 서로 equivalent한 roof를 정의하는지 또한 살펴볼 수 있다. 이는 localization 세팅에서는

$$\frac{a}{b}=\frac{ca}{cb}$$

꼴의 equivalence로 나타나는 것이다. 다음의 두 roof들

$$X\overset{s}{\longleftarrow} A\overset{f}{\longrightarrow}Y,\qquad X\overset{t}{\longleftarrow} B\overset{g}{\longrightarrow}Y$$

이 주어졌다고 할 때, 이들 둘이 equivalent하다는 것은 또 다른 object $$C$$와 roof

$$A\overset{u}{\longleftarrow} C\overset{h}B$$

이 존재하여

$$su=th,\qquad fu=gh$$

이 성립하며 $$su=th$$가 quasi-isomorphism인 것이다. 비슷한 방식으로 roof 두 개의 합성도 정의할 수 있으며 (roof diagram 상에서는 두 roof의 공통의 roof를 잡는 것으로 나타난다) 따라서 $$D(\mathcal{A})$$의 morphism을 완전하게 이해할 수 있다.

이제 이 언어가 어떻게 좋은 framework를 구성하는지를 보기 위해, 일상적인 $$\mathcal{A}$$의 원소 $$A$$가 주어졌다 하자. 그럼 우리는 $$A$$를 $$0$$번째 성분에 두고 나머지 성분은 $$0$$으로 고정한 chain complex

$$A[0]:\qquad \cdots\rightarrow 0\rightarrow A\rightarrow 0\rightarrow \cdots$$

을 생각한다. 그럼 우리가 알고 있는 것은 $$A$$의 injective resolution 혹은 $$A$$의 projective resolution이 $$A[0]$$과 quasi-isomorphic하다는 것으로, derived category 레벨에서는 $$A$$의 resolution들이 곧 $$A$$ 그 자체가 된다.

한편 위와 같이 resolution을 생각하면, injective resolution과 projective resolution은 서로 방향이 다르므로 $$D(\mathcal{A})$$를 조금 더 세분화할 수 있다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> Derived category $$D(\mathcal{A})$$의 subcategory들을 정의한다.

1. 충분히 작은 $$n$$에 대하여 그 cohomology $$H^n(A^\bullet)=0$$이 항상 성립하는 complex들을 *bounded below*라 하고, 이들이 이루는 $$D(\mathcal{A})$$의 full subcategory를 $$D^+(\mathcal{A})$$로 적는다.
2. 충분히 큰 $$n$$에 대하여 그 cohomology $$H^n(A^\bullet)=0$$이 항상 성립하는 complex들을 *bounded above*라 하고, 이들이 이루는 $$D(\mathcal{A})$$의 full subcategory를 $$D^-(\mathcal{A})$$로 적는다.
3. Bounded below이면서 bounded above인 complex들을 *bounded*라 하고, 이들이 이루는 $$D(\mathcal{A})$$의 full subcategory를 $$D^b(\mathcal{A})$$로 적는다.

</div>

종종 주어진 complex가 $$0$$ 아닌 (co)homology를 가지는 index의 범위를 *amplitude*라 부른다. 위에서 언급한 것과 같이, $$D^+(\mathcal{A})$$는 injective resolution을 사용한 작업에 자연스러운 무대이며, $$D^-(\mathcal{A})$$는 projective resolution에 자연스럽다. 대부분의 응용에서는 bounded derived category $$D^b(\mathcal{A})$$가 주요 무대가 된다.

한편 우리는 다음을 공식적으로 정의한다.

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> $$D(\mathcal{A})$$ 위의 *shift functor* $$[n]: D(\mathcal{A}) \rightarrow D(\mathcal{A})$$는 complex $$A^\bullet$$을 $$n$$칸 이동시키는 것이다. 구체적으로 $$(A[n])^i = A^{i+n}$$이고, 미분 map은 $$(d_{A[n]})^i = (-1)^n d_A^{i+n}$$으로 정의한다.

</div>
이 때 differential의 sign convention은 [§호몰로지, ⁋정의 5](/ko/math/homological_algebra/homology#def5) 이후에 이미 설명한 바 있다. 그러나 sign이 바뀐 것은 (co)homology에 어떠한 영향도 주지 않으므로 가령 다음의 식

$$H^i(A[n]) = H^{i+n}(A)$$

이 성립한다. 구체적인 예시로, abelian category의 object $$A$$를 $$A[0]$$으로 볼 때, $$A[n]$$은 $$-n$$번째 차수에 $$A$$가 있고 나머지는 $$0$$인 complex이며, 따라서 $$H^{-n}(A[n]) = A$$이고 다른 차수에서의 cohomology는 $$0$$이다.

## Derived Functor

우리는 앞서 derived category가 derived functor를 올바르게 살펴보는 데에 도움을 준다고 하였다. 이를 위해서는 complex 수준에서 resolution의 개념을 도입해야 한다.

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> Complex $$P \in K(\mathcal{A})$$가 *$$K$$-projective*라는 것은, 임의의 quasi-isomorphism $$s: A \rightarrow B$$ in $$K(\mathcal{A})$$에 대해 유도된 map

$$\Hom(s, P):\Hom_{K(\mathcal{A})}(B, P)\rightarrow\Hom_{K(\mathcal{A})}(A, P)$$

이 isomorphism인 것이다.

</div>

즉 $$P$$는 $$K(\mathcal{A})$$에서 Hom functor $$\Hom(-, P)$$를 quasi-isomorphism에 대해 invariant하게 만드는 complex로, 이러한 대상들만이 derived category로 잘 떨어질 것은 자명하다. 물론 다음 또한 정의해야 한다.

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> Complex $$I \in K(\mathcal{A})$$가 *$$K$$-injective*라는 것은, 임의의 quasi-isomorphism $$s : A \rightarrow B$$에 대해 유도된 map

$$\Hom_{K(\mathcal{A})}(I, A) \xrightarrow{s_\ast} \Hom_{K(\mathcal{A})}(I, B)$$

이 isomorphism인 것이다.

</div>

일반적으로, 대상 $$A$$의 resolution은 $$A[0]$$의 $$K$$-resolution이 된다. 또, 어렵지 않게 다음의 명제를 확인할 수 있다.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> 다음이 성립한다.

1. 각 항이 injective이고 bounded below인 chain complex는 $$K$$-injective이다.
2. 각 항이 projective이고 bounded above인 chain complex는 $$K$$-projective이다.

</div>

더 일반적으로, enough injective를 갖는 임의의 abelian category의 homotopy category는 enough $$K$$-injective resolution을 가지며 projective case에 대해서도 마찬가지이다. 이제 우리는 다음을 정의할 준비가 되었다.

<div class="definition" markdown="1">

<ins id="def8">**정의 8**</ins> Additive functor $$F : \mathcal{A} \rightarrow \mathcal{B}$$가 주어졌다고 하자.

1. $$F$$가 left exact이고 $$\mathcal{A}$$가 enough injective를 갖는다고 하자. $$A^\bullet \in D^+(\mathcal{A})$$의 *right derived functor*는 $$R F(A^\bullet) = F(I^\bullet)$$로 정의한다. 여기서 $$A^\bullet \rightarrow I^\bullet$$은 $$K$$-injective resolution이다.
2. $$F$$가 right exact이고 $$\mathcal{A}$$가 enough projective를 갖는다고 하자. $$A^\bullet \in D^-(\mathcal{A})$$의 *left derived functor*는 $$L F(A^\bullet) = F(P_\bullet)$$로 정의한다. 여기서 $$P_\bullet \rightarrow A^\bullet$$은 $$K$$-projective resolution이다.

</div>

우리는 $$K$$-resolution의 존재성을 사용하기 위해 $$A^\bullet$$이 $$D^\pm(\mathcal{A})$$에 각각 속해있을 것을 요구하였지만, 만일 $$K$$-resolution이 명시적으로 주어진다면 굳이 이를 가정할 필요는 없다. 그러나 실제 사용되는 대부분의 경우 $$A^\bullet$$은 우리가 원하는 boundedness를 만족하도록 주어진다. 

특별히 $$A \in \mathcal{A}$$를 $$A[0] \in D(\mathcal{A})$$로 보면,

$$H^i(R F(A[0])) = (R^i F)(A)$$

이 성립하므로 우리는 $$RF$$가 원래의 right derived functor들을 잘 복원하는 것을 안다. 더 직관적으로 말하자면, 이 right derived functor의 모든 정보는 사실상 $$R^iF$$들 각각이 아닌, $$RF$$라는 단일한 derived functor에 들어있는 것이며 이를 "classical"한 세계로 가져오기 위한 도구가 cohomology일 뿐이다. 비슷하게 $$H_i(L F(A[0])) = (L_i F)(A)$$인 것도 자명하다.

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> $$R F$$와 $$L F$$는 derived category에서의 functor이다. 즉 quasi-isomorphism을 quasi-isomorphism으로 보낸다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

Quasi-isomorphism $$s : A^\bullet \rightarrow B^\bullet$$이 주어졌다고 하고, $$A^\bullet \rightarrow I^\bullet$$, $$B^\bullet \rightarrow J^\bullet$$을 각각 $$K$$-injective resolution이라 하자. $$K$$-injective resolution의 lifting property ([정의 6](#def6))에 의해, quasi-isomorphism $$s$$는 $$I^\bullet$$과 $$J^\bullet$$ 사이의 map $$\tilde{s} : I^\bullet \rightarrow J^\bullet$$으로 유일하게 (homotopy까지) 확장된다. 따라서 $$F(\tilde{s}) : F(I^\bullet) \rightarrow F(J^\bullet)$$을 얻는다. $$K$$-injective resolution 위에서 $$F$$를 적용한 것이므로 $$F(\tilde{s})$$는 quasi-isomorphism이며, 따라서 $$D(\mathcal{B})$$에서 $$R F(A^\bullet) \cong R F(B^\bullet)$$이다. Left derived functor에 대해서도 비슷하다.

</details>

구체적인 예로서, $$\mathcal{A}$$ 위에서의 Hom functor $$\Hom(-, B)$$는 contravariant left exact functor이므로 이를 derived하여 complex 수준의 derived Hom $$R\Hom$$을 정의하면, $$R\Hom(A, B)$$의 cohomology는 $$\Ext^i(A, B)$$와 일치한다.

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10**</ins> $$\mathcal{A}$$가 enough injective를 갖는 abelian category라고 하자. 그럼 모든 $$A, B \in \mathcal{A}$$에 대해

$$H^{i}(R\Hom(A, B)) \cong \Ext^i(A, B)$$

이 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$R\Hom(A, B)$$를 정확히 정의하자. $$A$$를 $$A[0] \in D(\mathcal{A})$$로 보고, projective resolution $$P_\bullet \rightarrow A$$를 선택한다. [명제 7](#prop7)에 의하여 $$P_\bullet$$은 $$K$$-projective complex이므로

$$R\Hom(A, B) = \Hom(P_\bullet, B)$$

로 정의한다. 여기서 우변은 complex $$\Hom(P_\bullet, B)$$를 나타낸다. 그럼 $$P_\bullet \rightarrow A$$가 projective resolution이므로 [§Ext와 Tor](/ko/math/homological_algebra/ext_and_tor)의 정의에 의해 $$H^i(\Hom(P_\bullet, B)) = \Ext^i(A, B)$$이다.

</details>

비슷하게 tensor product의 left derived functor $$L(A \otimes B) = A \otimes^L B$$를 정의할 수 있으며, $$\Tor_i(A, B) = H^{-i}(A \otimes^L B)$$가 성립한다.

## Triangulated Category

Derived category $$D(\mathcal{A})$$는 단순한 category가 아니라 *triangulated category*의 구조를 갖는다. 이 구조는 abelian category에서 short exact sequence가 하던 역할을 derived category에서 대신한다.

<div class="definition" markdown="1">

<ins id="def11">**정의 11**</ins> *Triangulated category*는 다음 구조를 갖춘 additive category $$(\mathcal{T}, [1], \mathcal{S})$$이다.

1. *Shift functor* $$[1] : \mathcal{T} \rightarrow \mathcal{T}$$. 여기서 $$[0] = \id$$이고 $$[n+1] = [1] \circ [n]$$이다.
2. *Distinguished triangle*들의 모임 $$\mathcal{S}$$. 각 distinguished triangle은

$$A \overset{f}{\rightarrow} B \overset{g}{\rightarrow} C \overset{h}{\rightarrow} A[1]$$

의 형태를 갖는다. 이 모임은 다음 공리를 만족한다.
- (TR1) 모든 morphism $$f : A \rightarrow B$$에 대해 distinguished triangle $$A \rightarrow B \rightarrow C \rightarrow A[1]$$가 존재한다. 또한 $$A \overset{\id}{\rightarrow} A \rightarrow 0 \rightarrow A[1]$$은 distinguished triangle이다.
- (TR2) $$A \rightarrow B \rightarrow C \rightarrow A[1]$$이 distinguished triangle이면 $$B \rightarrow C \rightarrow A[1] \rightarrow B[1]$$도 distinguished triangle이다.
- (TR3) 두 distinguished triangle이 주어졌을 때, map들 $$(u, v, w)$$에 의한 morphism이 commute하면, $$w$$를 포함하는 확장이 존재한다.
- (TR4) Octahedral axiom: 합성 $$B \overset{g}{\longrightarrow} C \overset{h}{\longrightarrow} D$$이 주어졌을 때, 이와 연관된 octahedron을 이루는 세 개의 distinguished triangle이 존재한다.

</div>

Distinguished triangle의 직관은 short exact sequence의 "derived version"이라는 것이다. Abelian category에서 short exact sequence $$0 \rightarrow A' \overset{f}{\longrightarrow} A \overset{g}{\longrightarrow} A'' \rightarrow 0$$이 있으면, $$f$$를 complex 사이의 map $$A'[0] \rightarrow A[0]$$로 볼 수 있고, 이때 mapping cone $$C(f)$$는 $$A''[0]$$과 quasi-isomorphic하다. ([§긴 완전열, ⁋정의 8](/ko/math/homological_algebra/long_exact_sequence#def8)) 즉 short exact sequence는 derived category에서 distinguished triangle

$$A'[0] \overset{f}{\rightarrow} A[0] \rightarrow A''[0] \rightarrow A'[1]$$

으로 나타난다. 일반적인 map $$f$$에 대해서는, $$f$$가 isomorphism에서 벗어나는 정도가 $$C(f)$$의 cohomology로 측정되며, cohomology long exact sequence가 자연스럽게 나타난다.

Derived category $$D(\mathcal{A})$$에서 distinguished triangle은 complex 사이의 map $$f$$와 그 mapping cone $$C(f)$$로부터 얻어진 삼각형

$$A \overset{f}{\rightarrow} B \overset{g}{\rightarrow} C(f) \overset{h}{\rightarrow} A[1]$$

들로 구성된다. 여기서 $$g : B^i \rightarrow C(f)^i = B^i \oplus A^{i+1}$$는 $$b \mapsto (b, 0)$$이고, $$h : C(f)^i \rightarrow A[1]^i = A^{i+1}$$는 $$(b, a) \mapsto a$$이다.

<div class="proposition" markdown="1">

<ins id="prop12">**명제 12**</ins> $$R F : D^+(\mathcal{A}) \rightarrow D^+(\mathcal{B})$$는 triangulated functor이다. 즉 distinguished triangle

$$A \rightarrow B \rightarrow C \rightarrow A[1]$$

이 주어지면

$$R F(A) \rightarrow R F(B) \rightarrow R F(C) \rightarrow R F(A)[1]$$

도 distinguished triangle이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$A \rightarrow B$$를 map으로 보고, 이들의 $$K$$-injective resolution들을 각각 $$I_A^\bullet$$, $$I_B^\bullet$$이라 하자. $$K$$-injective resolution의 lifting property에 의해, map $$A \rightarrow B$$는 $$I_A^\bullet \rightarrow I_B^\bullet$$로 확장된다. $$C = C(f)$$의 $$K$$-injective resolution $$I_C^\bullet$$을 취하면, $$I_A^\bullet \rightarrow I_B^\bullet \rightarrow I_C^\bullet \rightarrow I_A^\bullet[1]$$은 $$K$$-injective complex들 사이의 distinguished triangle이며, $$F$$를 적용한 뒤 $$D(\mathcal{B})$$에서 보면 원하는 distinguished triangle을 얻는다. Bounded below $$K$$-injective complex들은 $$K(\mathcal{A})$$의 triangulated subcategory를 이루므로, mapping cone도 $$K$$-injective가 되고 이 diagram이 commute함을 알 수 있다.

</details>

## Derived Adjunction

Category theory에서 adjunction은 두 functor 사이의 가장 중요한 관계 중 하나이다. Derived category에서도 adjunction이 성립하며, 이를 *derived adjunction*이라 부른다. Derived adjunction $$L F \dashv R G$$는 일반적인 adjoint 관계를 derived category로 끌어올린 것으로, $$F$$, $$G$$가 exact하지 않아도 resolution을 통해 "올바르게" 계산한 결과끼리 여전히 adjoint 관계를 이룬다. Naive하게 $$F$$나 $$G$$를 적용하면 exactness가 깨져서 잘못된 homology가 나올 수 있지만, derived version을 사용하면 이 문제를 해결하면서 원래의 adjoint 구조도 유지된다.

<div class="proposition" markdown="1">

<ins id="prop13">**명제 13**</ins> Abelian category $$\mathcal{A}, \mathcal{B}$$ 사이의 additive functor들 $$F : \mathcal{A} \rightarrow \mathcal{B}$$ (right exact), $$G : \mathcal{B} \rightarrow \mathcal{A}$$ (left exact)가 adjoint pair $$F \dashv G$$를 이룬다고 하자. 그럼 derived category에서

$$L F : D^-(\mathcal{A}) \rightarrow D^-(\mathcal{B}), \qquad R G : D^+(\mathcal{B}) \rightarrow D^+(\mathcal{A})$$

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

가장 대표적인 예는 tensor product와 Hom의 adjunction이다. [\[다중선형대수학\] §Hom과 텐서곱](/ko/math/multilinear_algebra/hom_and_tensor)에서 본 abelian category $$\mathcal{A}$$ 위의 tensor-Hom adjunction

$$\Hom(A \otimes B, C) \cong \Hom(A, \Hom(B, C))$$

에서, complex $$X, Y, Z$$에 대해 동일한 형태의 isomorphism을 derived category에서도 얻고 싶을 수 있다. 그러나 raw functor $$-\otimes B$$와 $$\Hom(B,-)$$는 quasi-isomorphism을 보존하지 않으므로, 이 adjunction은 naive하게 derived category로 내려오지 않는다. 앞서 derived functor를 정의할 때 projective resolution 또는 injective resolution을 취해야만 $$K(\mathcal{A}) \to D(\mathcal{A})$$로 잘 descend한다는 점을 확인하였는데, 이는 바로 $$-\otimes B$$가 right exact이고 $$\Hom(B,-)$$가 left exact이기 때문이다. Quasi-isomorphism에 대한 localization을 거치면 classical adjoint는 자동으로 살아남지 않으므로, 이 exactness의 부족을 보완하는 derived version이 필요하다.

이를 구체적으로 확인하기 위해 $$R = \mathbb{Z}$$, $$M = \mathbb{Z}/n\mathbb{Z}$$를 생각하자. $$M$$은 flat이 아니므로 tensoring이 exact하지 않다. $$0 \to \mathbb{Z} \xrightarrow{\times n} \mathbb{Z} \to \mathbb{Z}/n\mathbb{Z} \to 0$$에 $$-\otimes M$$을 적용하면 exactness가 깨지며, 구체적으로 $$\Tor_1^\mathbb{Z}(\mathbb{Z}/n\mathbb{Z}, \mathbb{Z}/n\mathbb{Z}) \cong \mathbb{Z}/n\mathbb{Z}$$이 존재하므로 naive adjunction은 기대하는 대로 작동하지 않는다. ([§Ext와 Tor](/ko/math/homological_algebra/ext_and_tor))

이 exactness failure를 해결하기 위해 projective resolution을 사용하여 $$\otimes^L$$와 $$R\Hom$$을 구성하면, [명제 13](#prop13)에 의해 adjunction이 복원된다. 구체적으로 $$A \otimes^L B$$는 $$A$$의 projective resolution에 $$-\otimes B$$를 적용한 것이며, $$R\Hom(B, C)$$는 $$B$$의 projective resolution에 $$\Hom(-, C)$$를 적용한 것이다. 이를 통해

$$\Hom_{D(\mathcal{A})}(A \otimes^L B, C) \cong \Hom_{D(\mathcal{A})}(A, R\Hom(B, C))$$

를 얻는다. Projective resolution을 취하는 과정에서 $$-\otimes B$$가 잃어버렸던 $$\Tor$$ 정보와 $$\Hom(B,-)$$가 잃어버렸던 $$\Ext$$ 정보가 complex의 상위 차원으로 보존되며, chain map의 계산을 통해 양변이 일치함을 확인할 수 있다.

요약하면, abelian category에서의 classical adjunction은 underived level에서 존재하지만 quasi-isomorphism에 대한 localization을 거치면 자동으로 살아남지 않는다. $$-\otimes B$$의 right exactness와 $$\Hom(B,-)$$의 left exactness로 인해 quasi-isomorphism이 보존되지 않으며, 이로 인해 naive adjunction이 깨진다. 이 exactness의 failure는 $$\otimes^L$$와 $$R\Hom$$을 resolution을 통해 구성함으로써 해결되며, [명제 13](#prop13)이 보장하는 derived adjunction이 classical adjunction을 정확하게 대체한다.

---

**참고문헌**

**[GM]** S. I. Gelfand, Y. I. Manin, *Methods of homological algebra*, Springer, 2003.  
**[Ver]** J.-L. Verdier, *Des catégories dérivées des catégories abéliennes*, Astérisque **239** (1996).  
**[Wei]** C. A. Weibel, *An introduction to homological algebra*, Cambridge University Press, 1994.