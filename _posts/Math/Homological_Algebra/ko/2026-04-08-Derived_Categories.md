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

date: 2026-04-08
last_modified_at: 2026-04-08
weight: 8
published: false

---

우리는 [§유도함자, ⁋정의 4](/ko/math/homological_algebra/derived_functors#def4)에서 exact하지 않은 functor $$F$$에 대해 projective resolution을 이용하여 left derived functor $$L_iF$$를 정의하였다. Right exact functor $$F$$를 다룰 때, 우리는 대상 $$A$$의 projective resolution $$P_\bullet$$을 선택하고 $$F(P_\bullet)$$의 homology를 취함으로써 손실된 정보를 보충하였다. 그러나 이 접근에는 본질적인 한계가 있다.

첫째, derived functor $$L_iF$$는 각 차수 $$i$$마다 따로따로 정의된다. Vanishing이 여러 차수에서 동시에 발생하며, 이들을 개별적으로 추적하는 것은 비효율적이다. 둘째, 우리는 실제로는 대상 하나가 아니라 **complex 전체**를 functor에 입력하고 싶은 상황을 자주 만난다. Cohomology를 계산할 때 우리는 이미 암묵적으로 이를 한다. 대상 $$A$$의 cohomology를 계산하기 위해 injective resolution $$0 \to A \to I^0 \to I^1 \to \cdots$$을 만들고, 각 $$I^i$$에 functor를 적용한 뒤 전체 complex의 homology를 취한다. 즉 우리의 관심 대상은 개별 대상이 아니라 complex 그 자체에 있다.

Derived category는 이러한 동기에서 생겨난다. Complex 전체를 하나의 대상으로 취급하고, cohomology를 보존하는 사상인 quasi-isomorphism을 강제로 invert한 category를 구성함으로써, derived functor를 단일 functor로 통합할 수 있다.

## Complex와 cohomology

Chain complex와 cochain complex, 그리고 homology와 cohomology는 [§사슬호몰로지, ⁋정의 1](/ko/math/homological_algebra/homology#def1)에서 정의되었다.

Complex라는 개념은 이미 익숙하다. 대상 $$A$$의 injective resolution $$0 \to A \to I^0 \to I^1 \to \cdots$$도 cochain complex이다. 이 complex의 cohomology는 $$H^0(I^\bullet) = A$$이고 $$i \geq 1$$에 대해서는 $$H^i(I^\bullet) = 0$$이다. 즉 resolution은 $$A$$를 유일하게 남기고 나머지 차수의 cohomology를 모두 $$0$$으로 만드는 complex이다. 마찬가지로 projective resolution도 chain complex로 이해할 수 있다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 두 cochain complex $$A^\bullet$$, $$B^\bullet$$ 사이의 사상 $$f \colon A^\bullet \to B^\bullet$$이 모든 차수 $$i$$에서 유도된 사상 $$H^i(f) \colon H^i(A^\bullet) \to H^i(B^\bullet)$$가 isomorphism이면, $$f$$를 *quasi-isomorphism*이라 부른다.

</div>

Quasi-isomorphism은 cohomology의 관점에서 본질적으로 isomorphism과 같다. 두 complex의 cohomology group이 모두 같다면, 우리가 관심을 갖는 정보는 동일하다. 그러나 category의 구조상 quasi-isomorphism의 역사상이 존재하지 않을 수 있다. 예를 들어 어떤 complex가 다른 complex의 resolution일 때, resolution에서 원래 complex로 돌아가는 사상은 일반적으로 존재하지 않는다. 이 문제를 해결하기 위해 quasi-isomorphism을 강제로 invert하여 얻은 category가 derived category이다.

## Homotopy Category

Derived category를 정의하기 위해, 우선 complex 사이의 사상을 cohomology 정보에 의해 분류하는 category를 구성한다. 여기서 $$\Ch(\mathcal{A})$$는 $$\mathcal{A}$$-valued cochain complex들과 chain map들로 이루어진 category이다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> 두 complex 사상 $$f, g \colon A^\bullet \to B^\bullet$$이 *chain homotopic*이라는 것은 degree $$+1$$의 사상 $$h \colon A^\bullet \to B^\bullet[-1]$$가 존재하여 모든 $$i$$에 대해

$$f^i - g^i = d_B^{i-1} \circ h^i + h^{i+1} \circ d_A^i$$

이 성립하는 것이다. 이를 $$f \sim g$$로 쓴다.

</div>

Chain homotopy는 동치관계이다. 반사성은 $$h = 0$$으로, 대칭성은 $$-h$$로, 추이성은 합으로 확인된다. Chain homotopic인 사상은 cohomology에 대해 같은 유도 사상을 갖는다. 실제로 $$f \sim g$$이면 $$H^i(f) = H^i(g)$$가 모든 $$i$$에 대해 성립한다. 따라서 quasi-isomorphism의 문제를 다루기 전에, chain homotopic한 사상을 동일시하는 것이 자연스럽다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> Abelian category $$\mathcal{A}$$의 *homotopy category* $$\mathbf{K}(\mathcal{A})$$는 $$\Ch(\mathcal{A})$$에서 chain homotopic인 사상들을 동일시하여 얻은 quotient category이다. 즉

$$\operatorname{Hom}_{\mathbf{K}(\mathcal{A})}(A^\bullet, B^\bullet) = \operatorname{Hom}_{\Ch(\mathcal{A})}(A^\bullet, B^\bullet) / \{f \sim g\}.$$

</div>

$$\mathbf{K}(\mathcal{A})$$는 additive category이며, shift functor $$[n]$$이 $$\Ch(\mathcal{A})$$에서 $$\mathbf{K}(\mathcal{A})$$로 descend한다. 또한 mapping cone도 homotopy category에서 잘 정의되어, $$\mathbf{K}(\mathcal{A})$$는 triangulated category의 구조를 갖는다. Quasi-isomorphism은 $$\mathbf{K}(\mathcal{A})$$에서 일반적으로 isomorphism이 아니다. $$\mathbf{K}(\mathcal{A})$$에서 quasi-isomorphism을 invert한 category가 바로 derived category이다.

## Derived Category의 정의

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> Abelian category $$\mathcal{A}$$의 *derived category* $$D(\mathcal{A})$$는 homotopy category $$\mathbf{K}(\mathcal{A})$$에서 quasi-isomorphism의 모임 $$S$$에 대한 Verdier quotient $$\mathbf{K}(\mathcal{A})/S$$이다.

</div>

이 정의가 의미를 갖기 위해서는 $$S$$가 *multiplicative system*이어야 한다. $$S$$는 다음 조건을 만족한다. 첫째, 항등사상이 $$S$$에 속하고, $$S$$의 원소들의 합성은 다시 $$S$$에 속한다. 둘째, Ore condition이 성립한다: $$s \in S$$와 임의의 사상 $$f$$가 주어졌을 때, commute하는 diagram

$$\begin{CD} A @>f>> B \\ @VsVV @V\exists{t}VV \\ A' @>>g> B' \end{CD}$$

에서 $$t \in S$$인 lift $$(g, t)$$가 존재한다. 이 조건은 roof diagram의 합성을 정의하는 데 필수적이다. Ore condition의 증명은 표준적이나 다소 기술적이므로 여기서는 생략한다 ([Wei, 10.3] 참조).

$$D(\mathcal{A})$$의 사상은 roof diagram $$A \xleftarrow{s} B \xrightarrow{f} C$$ ($$s \in S$$)의 동치류로 정의된다. 두 roof $$A \xleftarrow{s_1} B_1 \xrightarrow{f_1} C$$과 $$A \xleftarrow{s_2} B_2 \xrightarrow{f_2} C$$는, Ore condition을 사용하여 얻은 commute하는 diagram에서 두 경로가 동일한 사상을 줄 때 동치로 간주한다. Roof의 합성도 Ore condition의 lift를 사용하여 정의된다.

Canonical functor $$Q \colon \mathbf{K}(\mathcal{A}) \to D(\mathcal{A})$$는 $$S$$의 원소들을 isomorphism으로 보내며, triangulated functor이다. Verdier quotient의 기본 성질에 의해 $$D(\mathcal{A})$$도 triangulated category가 된다. 구체적으로, $$\mathbf{K}(\mathcal{A})$$의 distinguished triangle을 $$Q$$로 보낸 삼각형은 $$D(\mathcal{A})$$에서 distinguished triangle이다.

이것의 가장 중요한 결과는 **resolution으로 대체할 수 있다**는 점이다. 대상 $$A$$와 그 injective resolution $$A \to I^\bullet$$ 사이에는 quasi-isomorphism이 존재하므로, derived category에서 $$A = A[0]$$과 $$I^\bullet$$은 isomorphism이다. 따라서 $$A$$를 직접 다루는 대신 $$I^\bullet$$을 다루어도 결과가 같다. 마찬가지로 projective resolution $$P_\bullet \to A$$도 $$A[0]$$와 quasi-isomorphic하다. Derived category에서는 injective resolution과 projective resolution 모두 $$A[0]$$와 isomorphic한 대상이다.

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> Complex $$A^\bullet \in D(\mathcal{A})$$가 *bounded below*이라는 것은 $$H^i(A^\bullet) = 0$$인 $$i$$가 아래로 유계인 것이다, 즉 충분히 작은 $$n$$에 대해 $$i < n$$이면 $$H^i(A^\bullet) = 0$$인 것이다. Bounded below complex들로 이루어진 full subcategory를 $$D^+(\mathcal{A})$$로 쓴다. 비슷하게 bounded above ($$H^i = 0$$ for $$i \gg 0$$)인 complex들의 category를 $$D^-(\mathcal{A})$$, bounded (양쪽에서 유계)인 complex들의 category를 $$D^b(\mathcal{A})$$로 쓴다.

</div>

$$D^+(\mathcal{A})$$는 injective resolution을 사용한 작업에 자연스러운 무대이며, $$D^-(\mathcal{A})$$는 projective resolution에 자연스럽다. 대부분의 응용에서는 bounded derived category $$D^b(\mathcal{A})$$가 주요 무대가 된다.

## Shift Functor

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> $$D(\mathcal{A})$$ 위의 *shift functor* $$[n] \colon D(\mathcal{A}) \to D(\mathcal{A})$$는 complex $$A^\bullet$$을 $$n$$칸 이동시키는 것이다. 구체적으로 $$(A[n])^i = A^{i+n}$$이고, 미분 사상은 $$(d_{A[n]})^i = (-1)^n d_A^{i+n}$$으로 정의한다.

</div>

Shift functor는 derived category의 기본 연산이다. Cohomology에 대해서는

$$H^i(A[n]) = H^{i+n}(A)$$

가 성립한다. 이는 $$d_{A[n]}$$의 정의에서 $$(-1)^n$$ 인자가 cohomology 계산에 영향을 주지 않기 때문이다. 예를 들어, 대상 $$A$$를 $$A[0]$$으로 볼 때, $$A[n]$$은 $$n$$번째 차수에 $$A$$가 있고 나머지는 $$0$$인 complex이다. 따라서 $$H^{-n}(A[n]) = A$$이고 다른 차수에서의 cohomology는 $$0$$이다.

Shift functor는 derived adjunction 등에서 차수의 정합성을 맞추는 역할을 한다.

## Derived Functor

Derived functor를 정의하기 전에, complex 수준의 resolution 개념을 도입한다.

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> Complex $$P \in \mathbf{K}(\mathcal{A})$$가 *$$K$$-projective*라는 것은, 임의의 quasi-isomorphism $$s \colon A \to B$$ in $$\mathbf{K}(\mathcal{A})$$에 대해 유도된 사상

$$\operatorname{Hom}_{\mathbf{K}(\mathcal{A})}(B, P) \xrightarrow{s^*} \operatorname{Hom}_{\mathbf{K}(\mathcal{A})}(A, P)$$

이 isomorphism인 것이다. 즉 $$P$$는 $$\mathbf{K}(\mathcal{A})$$에서 Hom functor $$\operatorname{Hom}(-, P)$$를 quasi-isomorphism에 대해 invariant하게 만드는 complex이다.

</div>

$$K$$-projective complex는 projective resolution의 complex 버전이다. 대상 $$A$$의 projective resolution $$P_\bullet \to A$$는 $$K$$-projective complex이며, 임의의 projective complex도 $$K$$-projective이다.

<div class="definition" markdown="1">

<ins id="def8">**정의 8**</ins> Complex $$I \in \mathbf{K}(\mathcal{A})$$가 *$$K$$-injective*라는 것은, 임의의 quasi-isomorphism $$s \colon A \to B$$에 대해 유도된 사상

$$\operatorname{Hom}_{\mathbf{K}(\mathcal{A})}(I, A) \xrightarrow{s_*} \operatorname{Hom}_{\mathbf{K}(\mathcal{A})}(I, B)$$

이 isomorphism인 것이다.

</div>

$$K$$-injective complex는 injective resolution의 complex 버전이다. Injective complex는 $$K$$-injective이며, 임의의 bounded below complex는 Spaltenstein (1988)의 결과에 의해 $$K$$-injective resolution을 갖는다. 이 결과는 unbounded complex에서 derived functor를 정의하는 데 필수적이다.

---

Derived category에서 exact하지 않은 functor를 다루는 표준적인 방법은 derived functor이다. 우리는 이미 [§유도함자](/ko/math/homological_algebra/derived_functors)에서 대상 하나에 대한 derived functor를 정의하였으나, derived category에서는 이를 complex 전체로 확장하여 단일 functor로 통합할 수 있다.

<div class="definition" markdown="1">

<ins id="def9">**정의 9**</ins> Additive functor $$F \colon \mathcal{A} \to \mathcal{B}$$가 주어졌다고 하자.

1. $$F$$가 left exact이고 $$\mathcal{A}$$가 enough injective를 갖는다고 하자. $$A^\bullet \in D^+(\mathcal{A})$$의 *right derived functor*는 $$R F(A^\bullet) = F(I^\bullet)$$로 정의한다. 여기서 $$A^\bullet \to I^\bullet$$은 $$K$$-injective resolution이다.
2. $$F$$가 right exact이고 $$\mathcal{A}$$가 enough projective를 갖는다고 하자. $$A^\bullet \in D^-(\mathcal{A})$$의 *left derived functor*는 $$L F(A^\bullet) = F(P_\bullet)$$로 정의한다. 여기서 $$P_\bullet \to A^\bullet$$은 $$K$$-projective resolution이다.

</div>

$$K$$-injective resolution과 $$K$$-projective resolution은 일반적인 injective resolution과 projective resolution의 complex 버전이다. 대상 하나의 경우에는 기존의 resolution과 일치한다.

Derived functor가 정의가 잘 되어 있는지 확인하려면 resolution의 선택에 의존하지 않아야 한다. Quasi-isomorphism $$s \colon A^\bullet \to B^\bullet$$이 주어졌을 때, resolution을 선택하여 $$F(I_A^\bullet)$$과 $$F(I_B^\bullet)$$을 얻으면, $$F$$가 적절한 resolution 위에서 작용하므로 이들 사이에 quasi-isomorphism이 유도되어 derived category에서 동일한 대상을 나타낸다.

대상 하나에 대한 derived functor와의 관계는 다음과 같다. $$A \in \mathcal{A}$$를 $$A[0] \in D(\mathcal{A})$$로 보면,

$$H^i(R F(A[0])) = (R^i F)(A)$$

이 성립한다. 즉 $$R F$$는 $$R^i F$$를 모든 차수에서 동시에 포착하는 complex 수준의 functor이다. 비슷하게 $$H_i(L F(A[0])) = (L_i F)(A)$$이다.

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10**</ins> $$R F$$와 $$L F$$는 derived category에서의 functor이다. 즉 quasi-isomorphism을 보내 quasi-isomorphism으로 보낸다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

Quasi-isomorphism $$s \colon A^\bullet \to B^\bullet$$이 주어졌다고 하자. $$A^\bullet \to I^\bullet$$, $$B^\bullet \to J^\bullet$$을 각각 $$K$$-injective resolution이라 하자. $$K$$-injective resolution의 lifting property에 의해, quasi-isomorphism $$s$$는 $$I^\bullet$$과 $$J^\bullet$$ 사이의 사상 $$\tilde{s} \colon I^\bullet \to J^\bullet$$으로 유일하게 (homotopy까지) 확장된다. 따라서 $$F(\tilde{s}) \colon F(I^\bullet) \to F(J^\bullet)$$을 얻는다. $$K$$-injective resolution 위에서 $$F$$를 적용한 것이므로 $$F(\tilde{s})$$는 quasi-isomorphism이며, 따라서 $$D(\mathcal{B})$$에서 $$R F(A^\bullet) \cong R F(B^\bullet)$$이다. Left derived functor에 대해서도 비슷하다.

</details>

구체적인 예로서, $$\mathcal{A}$$ 위에서의 Hom functor $$\operatorname{Hom}(-, B)$$는 contravariant left exact functor이므로 이를 derived하여 complex 수준의 derived Hom을 얻을 수 있다. $$\mathbf{R}\operatorname{Hom}$$을 정의하면, $$\mathbf{R}\operatorname{Hom}(A, B)$$의 cohomology는 $$\operatorname{Ext}^i(A, B)$$와 일치한다.

<div class="proposition" markdown="1">

<ins id="prop11">**명제 11**</ins> $$\mathcal{A}$$가 enough injective를 갖는 abelian category라고 하자. 그럼 모든 $$A, B \in \mathcal{A}$$에 대해

$$H^{i}(\mathbf{R}\operatorname{Hom}(A, B)) \cong \operatorname{Ext}^i(A, B)$$

이 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$\mathbf{R}\operatorname{Hom}(A, B)$$를 정확히 정의하자. $$A$$를 $$A[0] \in D(\mathcal{A})$$로 보고, projective resolution $$P_\bullet \to A$$를 선택한다. $$P_\bullet$$은 $$K$$-projective complex이므로

$$\mathbf{R}\operatorname{Hom}(A, B) = \operatorname{Hom}(P_\bullet, B)$$

로 정의한다. 여기서 우변은 complex $$\operatorname{Hom}(P_\bullet, B)$$를 나타낸다. $$P_\bullet \to A$$가 resolution이므로 [§Ext와 Tor](/ko/math/homological_algebra/ext_and_tor)의 정의에 의해 $$H^i(\operatorname{Hom}(P_\bullet, B)) = \operatorname{Ext}^i(A, B)$$이다.

더 정교하게, $$B$$에도 injective resolution $$B \to I^\bullet$$을 취하면 $$\operatorname{Hom}(P_\bullet, I^\bullet)$$은 이중 복합체를 이루며, 그 total complex가 $$\mathbf{R}\operatorname{Hom}(A, B)$$를 준다. 그러나 $$P_\bullet$$이 $$K$$-projective이므로 한쪽만 resolution을 취해도 cohomology에는 영향을 주지 않는다.

</details>

비슷하게 tensor product의 left derived functor $$L(A \otimes B) = A \otimes^L B$$를 정의할 수 있으며, $$\operatorname{Tor}_i(A, B) = H^{-i}(A \otimes^L B)$$가 성립한다.

## Triangulated Category

Derived category $$D(\mathcal{A})$$는 단순한 category가 아니라 *triangulated category*의 구조를 갖는다. 이 구조는 abelian category에서 short exact sequence가 하던 역할을 derived category에서 대신한다.

<div class="definition" markdown="1">

<ins id="def12">**정의 12**</ins> *Triangulated category*는 다음 구조를 갖춘 additive category $$(\mathcal{T}, [1], \mathcal{S})$$이다.

1. *Shift functor* $$[1] \colon \mathcal{T} \to \mathcal{T}$$: 자기 동형사상이며, $$[0] = \operatorname{id}$$이고 $$[n+1] = [1] \circ [n]$$이다.
2. *Distinguished triangle*들의 모임 $$\mathcal{S}$$: 각 distinguished triangle은

$$A \overset{f}{\to} B \overset{g}{\to} C \overset{h}{\to} A[1]$$

의 형태를 갖는다. 이 모임은 다음 공리를 만족한다.
    - (TR1) Isomorphism은 distinguished triangle을 보낸다. 모든 사상 $$f \colon A \to B$$에 대해 distinguished triangle $$A \to B \to C \to A[1]$$가 존재한다. 또한 $$A \overset{\operatorname{id}}{\to} A \to 0 \to A[1]$$은 distinguished triangle이다.
    - (TR2) $$A \to B \to C \to A[1]$$이 distinguished triangle이면 $$B \to C \to A[1] \to B[1]$$도 distinguished triangle이다.
    - (TR3) 두 distinguished triangle이 주어졌을 때, 사상들 $$(u, v, w)$$에 의한 morphism이 commute하면, $$w$$를 포함하는 확장이 존재한다.
    - (TR4) Octahedral axiom: 합성 $$B \xrightarrow{g} C \xrightarrow{h} D$$이 주어졌을 때, 이와 연관된 octahedron을 이루는 세 개의 distinguished triangle이 존재한다.

</div>

<div class="definition" markdown="1">

<ins id="def13">**정의 13**</ins> 두 cochain complex $$A^\bullet$$, $$B^\bullet$$ 사이의 사상 $$f \colon A^\bullet \to B^\bullet$$이 주어졌을 때, *mapping cone* $$C(f)^\bullet$$은 차수별로 $$C(f)^i = B^i \oplus A^{i+1}$$이고, 미분 사상이

$$(b, a) \mapsto (d_B b + f(a), -d_A a)$$

으로 주어지는 cochain complex이다.

</div>

Mapping cone은 사상 $$f$$가 "얼마나 isomorphism에서 벗어나는지"를 측정하는 도구이다. $$C(f)^\bullet$$의 cohomology를 계산해보자. 정의에 의해 $$H^i(C(f))$$는 $$d_B b + f(a) = 0$$이고 $$d_A a = 0$$인 쌍 $$(b, a) \in B^i \oplus A^{i+1}$$을, $$(d_B b' + f(a'), -d_A a')$$ 형태의 원소들로 나눈 것이다.

<div class="proposition" markdown="1">

<ins id="prop14">**명제 14**</ins> 사상 $$f \colon A^\bullet \to B^\bullet$$이 quasi-isomorphism인 것과 $$H^i(C(f)) = 0$$이 모든 $$i$$에 대해 성립하는 것은 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$f$$에 대해 cohomology long exact sequence

$$\cdots \to H^i(A) \overset{H^i(f)}{\to} H^i(B) \to H^i(C(f)) \to H^{i+1}(A) \overset{H^{i+1}(f)}{\to} H^{i+1}(B) \to \cdots$$

이 성립한다. 이것은 standard construction이며, $$C(f)$$의 정의로부터 직접 확인할 수 있다. $$f$$가 quasi-isomorphism이면 $$H^i(f)$$가 모든 $$i$$에서 isomorphism이므로, five lemma에 의해 $$H^i(C(f)) = 0$$이다. 역으로 $$H^i(C(f)) = 0$$이면 위 long exact sequence에서 $$H^i(f)$$가 isomorphism임을 직접 읽을 수 있다.

</details>

Distinguished triangle의 직관은 short exact sequence의 "derived version"이라는 것이다. Abelian category에서 short exact sequence $$0 \to A' \xrightarrow{f} A \xrightarrow{g} A'' \to 0$$이 있으면, $$f$$를 complex 사이의 사상 $$A'[0] \to A[0]$$로 볼 수 있고, 이때 $$C(f)$$는 $$A''[0]$$과 quasi-isomorphic하다. 즉 short exact sequence는 derived category에서 distinguished triangle

$$A'[0] \overset{f}{\to} A[0] \to A''[0] \to A'[1]$$

으로 나타난다. 일반적인 사상 $$f$$에 대해서는, $$f$$가 isomorphism에서 벗어나는 정도가 $$C(f)$$의 cohomology로 측정되며, cohomology long exact sequence가 자연스럽게 나타난다.

Derived category $$D(\mathcal{A})$$에서 distinguished triangle은 complex 사이의 사상 $$f$$와 그 mapping cone $$C(f)$$로부터 얻어진 삼각형

$$A \overset{f}{\to} B \overset{g}{\to} C(f) \overset{h}{\to} A[1]$$

들로 구성된다. 여기서 $$g \colon B^i \to C(f)^i = B^i \oplus A^{i+1}$$는 $$b \mapsto (b, 0)$$이고, $$h \colon C(f)^i \to A[1]^i = A^{i+1}$$는 $$(b, a) \mapsto a$$이다.

Triangulated 구조의 중요성은 derived functor가 exact functor처럼 "triangles을 triangles으로 보낸다"는 성질에 있다.

<div class="proposition" markdown="1">

<ins id="prop15">**명제 15**</ins> $$R F \colon D^+(\mathcal{A}) \to D^+(\mathcal{B})$$는 triangulated functor이다. 즉 distinguished triangle

$$A \to B \to C \to A[1]$$

이 주어지면

$$R F(A) \to R F(B) \to R F(C) \to R F(A)[1]$$

도 distinguished triangle이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$A \to B$$를 사상으로 보고, 이들의 $$K$$-injective resolution들을 각각 $$I_A^\bullet$$, $$I_B^\bullet$$이라 하자. $$K$$-injective resolution의 lifting property에 의해, 사상 $$A \to B$$는 $$I_A^\bullet \to I_B^\bullet$$로 확장된다. $$C = C(f)$$의 $$K$$-injective resolution $$I_C^\bullet$$을 취하면, $$I_A^\bullet \to I_B^\bullet \to I_C^\bullet \to I_A^\bullet[1]$$은 $$K$$-injective complex들 사이의 distinguished triangle이며, $$F$$를 적용한 뒤 $$D(\mathcal{B})$$에서 보면 원하는 distinguished triangle을 얻는다. $$K$$-injective resolution들 사이의 사상에 대해 mapping cone도 다시 $$K$$-injective가 되므로, 이 diagram이 commute함을 알 수 있다.

</details>

## Derived Adjunction

Category theory에서 adjunction은 두 functor 사이의 가장 중요한 관계 중 하나이다. Derived category에서도 adjunction이 성립하며, 이를 *derived adjunction*이라 부른다.

<div class="proposition" markdown="1">

<ins id="prop16">**명제 16**</ins> Abelian category $$\mathcal{A}, \mathcal{B}$$ 사이의 additive functor들 $$F \colon \mathcal{A} \to \mathcal{B}$$ (right exact), $$G \colon \mathcal{B} \to \mathcal{A}$$ (left exact)가 adjoint pair $$F \dashv G$$를 이룬다고 하자. 그럼 derived category에서

$$L F \colon D^-(\mathcal{A}) \to D^-(\mathcal{B}), \qquad R G \colon D^+(\mathcal{B}) \to D^+(\mathcal{A})$$

는 adjoint pair $$L F \dashv R G$$를 이룬다. 즉 모든 $$A^\bullet \in D^-(\mathcal{A})$$, $$B^\bullet \in D^+(\mathcal{B})$$에 대해

$$\operatorname{Hom}_{D(\mathcal{B})}(L F(A^\bullet), B^\bullet) \cong \operatorname{Hom}_{D(\mathcal{A})}(A^\bullet, R G(B^\bullet))$$

이 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$A^\bullet$$의 $$K$$-projective resolution $$P_\bullet$$과 $$B^\bullet$$의 $$K$$-injective resolution $$I^\bullet$$을 선택하자. $$P_\bullet$$은 $$K$$-projective이므로 $$\operatorname{Hom}_{D(\mathcal{B})}(F(P_\bullet), I^\bullet)$$의 계산에서 $$F(P_\bullet)$$을 resolution로 대체할 수 있다. 원래의 adjunction $$F \dashv G$$에 의해, complex 수준에서

$$\operatorname{Hom}_{\Ch(\mathcal{B})}(F(P_\bullet), I^\bullet) \cong \operatorname{Hom}_{\Ch(\mathcal{A})}(P_\bullet, G(I^\bullet))$$

이 성립한다. 이 동형은 각 차수별 adjunction $$\operatorname{Hom}_\mathcal{B}(F(P^n), I^m) \cong \operatorname{Hom}_\mathcal{A}(P^n, G(I^m))$$을 모아서 complex 수준으로 얻은 것이다. $$P_\bullet$$이 $$K$$-projective이고 $$I^\bullet$$이 $$K$$-injective이므로, 좌변은 $$\operatorname{Hom}_{\mathbf{K}(\mathcal{B})}(F(P_\bullet), I^\bullet) = \operatorname{Hom}_{D(\mathcal{B})}(L F(A^\bullet), B^\bullet)$$로, 우변은 $$\operatorname{Hom}_{\mathbf{K}(\mathcal{A})}(P_\bullet, G(I^\bullet)) = \operatorname{Hom}_{D(\mathcal{A})}(A^\bullet, R G(B^\bullet))$$로 환원된다.

</details>

이 결과는 derived category에서 functor의 adjunction 관계가 "derived version"으로 자연스럽게 보존된다는 것을 보여준다. 가장 대표적인 예는 tensor product와 Hom의 adjunction이다. $$\mathcal{A}$$가 enough projective를 갖는다고 하자. Tensor product $$-\otimes B$$는 right exact이고 $$\operatorname{Hom}(B, -)$$는 left exact이며, [\[다중선형대수학\] §Hom과 텐서곱](/ko/math/multilinear_algebra/hom_and_tensor)에서 본 adjunction

$$\operatorname{Hom}(A \otimes B, C) \cong \operatorname{Hom}(A, \operatorname{Hom}(B, C))$$

의 derived version으로

$$\operatorname{Hom}_{D(\mathcal{A})}(A \otimes^L B, C) \cong \operatorname{Hom}_{D(\mathcal{A})}(A, \mathbf{R}\operatorname{Hom}(B, C))$$

를 얻는다.

Derived adjunction은 algebraic geometry에서 특히 중요하다. Geometric morphism $$f \colon X \to Y$$에 대해 triple adjunction

$$L f^* \dashv R f_* \dashv f^!$$

이 성립한다. 여기서 $$f^!$$는 derived category에서만 자연스럽게 정의되는 functor로, Grothendieck duality의 핵심이다. 이에 대해서는 algebraic geometry 쪽 글에서 다룬다.

---

**참고문헌**

**[GM]** S. I. Gelfand, Y. I. Manin, *Methods of homological algebra*, Springer, 2003.
**[Ver]** J.-L. Verdier, *Des catégories dérivées des catégories abéliennes*, Astérisque **239** (1996).
**[Wei]** C. A. Weibel, *An introduction to homological algebra*, Cambridge University Press, 1994.