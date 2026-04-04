---
title: "층 코호몰로지"
excerpt: "Sheaf cohomology and its applications"

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/sheaf_cohomology
sidebar:
    nav: "algebraic_geometry-ko"

header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Sheaf_Cohomology.png
    overlay_filter: 0.5

date: 2026-03-15
last_modified_at: 2026-04-05
weight: 12
---

우리는 지금까지 기하적 직관을 위해 주로 line bundle의 언어를 사용하였으나, [§표준선다발, ⁋정의 1](/ko/math/algebraic_geometry/canonical_bundle#def1) 직후에 살펴보았듯 line bundle의 section sheaf를 생각하면 이는 근본적으로는 sheaf의 언어로 바꾸어 쓸 수 있다. 이번 글에서 우리는 sheaf cohomology의 개념을 정의한다. 


가령 [§선다발과 벡터다발](/ko/math/algebraic_geometry/line_bundles)에서 우리는 line bundle $$\mathcal{L}$$의 global section space $$\Gamma(X, \mathcal{L})$$을 정의하였다. 특히 [는 이 차원이 complete linear system의 dimension, 나아가 variety의 projective embedding을 결정하는 핵심적 역할을 한다는 것을 살펴보았다. 

## Derived Functor로서의 정의

Sheaf가 위상공간의 모든 정보들을 체계적으로 기술할 수 있는 도구임에 반해, 지금까지의 이야기에서 sheaf가 전면으로 등장한 것은 [§선형계](/ko/math/algebraic_geometry/linear_systems)에서 global section space $$\Gamma(X, \mathcal{L})$$이 complete linear system의 projective embedding을 결정한다는 것을 살펴볼 때 뿐이었다. 

그러나 global section만이 우리의 관심사라면, 굳이 sheaf를 생각할 필요 없이 global section functor만 생각했어도 될 것이다. 실제로 global section functor는 sheaf가 갖고 있는 정보를 모두 담고 있는 것이 아니다. 예를 들어 global section functor

$$\Gamma(X, -): \QCoh(X) \to \Vect_\mathbb{K}; \qquad \mathcal{F} \mapsto \mathcal{F}(X)$$

를 생각하자. 우리가 [§표준선다발, ⁋정의 1](/ko/math/algebraic_geometry/canonical_bundle#def1)에서 quasi-coherent sheaf를 정의할 때의 motivation은 vector bundle들의 category $$\Bun(X)$$가 abelian category가 아니므로, kernel과 cokernel을 추가하는 더 넓은 category를 생각하는 것이었고, 그러한 관점에서 $$\QCoh(X)$$가 abelian category가 된다는 것은 놀라운 일은 아니다. [^1]

만일 $$\Gamma(X,-)$$가 어떠한 정보도 잃어버리지 않는다면, 이 functor는 exact functor여야 할 것이다. 즉, (quasi-coherent) sheaf들의 short exact sequence

$$0 \to \mathcal{F}' \to \mathcal{F} \to \mathcal{F}'' \to 0$$

가 주어졌을 때, 이를 $$\Gamma(X,-)$$를 타고 옮긴 것 또한 short exact sequence가 되어야 할 것이다. 그러나 이 functor는 left exact functor밖에 되지 않는다. 즉, 

$$0 \to \Gamma(X, \mathcal{F}') \to \Gamma(X, \mathcal{F}) \to \Gamma(X, \mathcal{F}'')$$

의 exactness는 보장되지만 surjection

$$\Gamma(X, \mathcal{F}) \to \Gamma(X, \mathcal{F}'') \to 0$$

은 일반적으로 보장되지 않는다. 구체적인 예시를 위해 Euler sequence

$$0 \to \Omega^1_{\mathbb{P}^n} \to \mathcal{O}_{\mathbb{P}^n}(-1)^{\oplus(n+1)} \to \mathcal{O}_{\mathbb{P}^n} \to 0$$

를 생각하자. ([§표준선다발, ⁋명제 7](/ko/math/algebraic_geometry/canonical_bundle#prop7)) 이 short exact sequence에 $$\Gamma(\mathbb{P}^n, -)$$를 적용하면

$$0 \to \Gamma(\mathbb{P}^n, \Omega^1_{\mathbb{P}^n}) \to \Gamma(\mathbb{P}^n, \mathcal{O}_{\mathbb{P}^n}(-1)^{\oplus(n+1)}) \to \Gamma(\mathbb{P}^n, \mathcal{O}_{\mathbb{P}^n})$$

를 얻는다. 그런데 [§선다발과 벡터다발, ⁋예시 16](/ko/math/algebraic_geometry/line_bundles#ex16)에서 살펴본 것처럼 $$\mathcal{O}_{\mathbb{P}^n}(-1)$$의 global section은 0뿐이므로

$$\Gamma(\mathbb{P}^n, \mathcal{O}_{\mathbb{P}^n}(-1)^{\oplus(n+1)}) = 0$$

이지만, $$\Gamma(\mathbb{P}^n, \mathcal{O}_{\mathbb{P}^n})=\mathbb{K}$$이므로 오른쪽 부분의 surjectivity가 성립할 수 없다. 

이를 해결하기 위한 표준적인 방법은 right derived functor를 생각하는 것이다. ([\[호몰로지 대수학\] §유도함자, ⁋정의 9](/ko/math/homological_algebra/derived_functors#def9)). 구체적으로, $$\QCoh(X)$$에는 충분한 injective object가 존재하는 것을 보일 수 있으므로 임의의 quasi-coherent sheaf $$\mathcal{F}$$는 항상 injective resolution $$\mathcal{I}^\bullet$$을 가지고, 이로부터 다음의 

$$0 \to \Gamma(X, \mathcal{I}^0) \to \Gamma(X, \mathcal{I}^1) \to \Gamma(X, \mathcal{I}^2) \to \cdots$$

를 통해 다음의 sheaf cohomology를 정의할 수 있다. 

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Variety $$X$$ 위의 quasi-coherent sheaf $$\mathcal{F}$$에 대하여, $$i$$번째 *sheaf cohomology* $$H^i(X, \mathcal{F})$$를

$$H^i(X, \mathcal{F}) = \frac{\ker(\Gamma(X, \mathcal{I}^i) \to \Gamma(X, \mathcal{I}^{i+1}))}{\operatorname{im}(\Gamma(X, \mathcal{I}^{i-1}) \to \Gamma(X, \mathcal{I}^i))}$$

으로 정의한다. 여기서 $$\mathcal{I}^\bullet$$은 $$\mathcal{F}$$의 injective resolution이다.

</div>

이것이 $$\mathcal{I}^\bullet$$의 선택에 무관한 것 등등은 모두 homological algebra의 표준적인 논증으로부터 따라온다.

우리는 앞서 global section space $$\Gamma(X, \mathcal{L})$$을 소개하며 이 공간의 또 다른 대중적인 표기 중 하나가 $$H^0(X, \mathcal{L})$$이라고 하였는데, 이 표기법이 바로 위의 정의로부터 정당화됨을 안다. 

다음 명제 또한 homological algebra로부터 바로 따라나오는 표준적인 명제이다. 

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> Sheaf의 short exact sequence

$$0 \to \mathcal{F}' \to \mathcal{F} \to \mathcal{F}'' \to 0$$

에 대하여, 긴 완전열

$$0 \to H^0(X, \mathcal{F}') \to H^0(X, \mathcal{F}) \to H^0(X, \mathcal{F}'') \xrightarrow{\delta} H^1(X, \mathcal{F}') \to \cdots$$

이 존재한다. 여기서 $$\delta$$는 *connecting homomorphism*이다.

</div>

## Čech Cohomology

[정의 1](#def1)는 sheaf cohomology의 정의로서는 엄밀하지만, injective resolution을 명시적으로 구성하는 것은 일반적으로 매우 어렵다. 따라서 실제 계산에서는 다른 관점에서 cohomology를 정의하는 Čech approach를 사용한다. 

직관적으로 Čech cohomology $$\check{H}^i(X, \mathcal{F})$$는 국소적인 정보의 gluing의 실패를 측정하는 도구이다. 즉, $$\check{H}^0(X, \mathcal{F})$$는 정확하게 global section space이며, $$\check{H}^1(X, \mathcal{F})$$는 local section들을 붙여서 global section을 얻어내는 과정이 얼마나 실패하는지를 알려준다. 이를 엄밀하게 정의하기 위해 다음부터 시작한다. 

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> 위상공간 $$X$$의 open cover $$\mathcal{U} = \{U_i\}_{i \in I}$$와 sheaf $$\mathcal{F}$$가 주어졌다 하고, $$I$$ 위의 total order $$<$$를 임의로 고정하자. 그럼 *Čech complex<sub>체흐 복합체</sub>* $$C^\bullet(\mathcal{U}, \mathcal{F})$$는 다음과 같이 정의된다. 

$$\check{C}^p(\mathcal{U}, \mathcal{F}) = \prod_{i_0 < \cdots < i_p} \mathcal{F}(U_{i_0} \cap \cdots \cap U_{i_p})$$

이 때, *coboundary map* $$d: \check{C}^p \to \check{C}^{p+1}$$은 다음의 식

$$(d\alpha)_{i_0 \cdots i_{p+1}} = \sum_{k=0}^{p+1} (-1)^k \alpha_{i_0 \cdots \hat{i_k} \cdots i_{p+1}}\vert_{U_{i_0 \cdots i_{p+1}}}$$

으로 정의된다. 여기서 $$\hat{i_k}$$는 index $$i_k$$를 생략한다는 의미이다.

</div>

이 정의가 잘 정의되기 위해서는, 즉, $$\check{C}^\bullet(\mathcal{U}, \mathcal{F})$$이 실제로 complex가 되기 위해서는 coboundary map이 실제로 coboundary map이 되어야 한다. 즉 $$d^2=0$$이어야 한다. 이는 위의 식을 전개해보면 부호 차이로부터 직접 확인할 수 있다. 결론적으로 $$\check{C}^\bullet(\mathcal{U}, \mathcal{F})$$는 cochain complex이며, 따라서 다음을 정의할 수 있다. 

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> *Čech cohomology<sub>체흐 코호몰로지</sub>* $$\check{H}^p(\mathcal{U}, \mathcal{F})$$를 Čech complex의 cohomology

$$\check{H}^p(\mathcal{U}, \mathcal{F}) = H^p(C^\bullet(\mathcal{U}, \mathcal{F}))$$

로 정의한다. 

</div>

Coboundary map의 직관적 의미를 낮은 차원의 경우로 이해할 수 있다. 이 직관을 $$p = 0, 1$$의 낮은 차원에서 확인해보자.

<div class="example" markdown="1">

<ins id="ex5">**예시 5** ($$p = 0$$)</ins> Čech complex의 정의에 의하여 $$C^0(\mathcal{U}, \mathcal{F}) = \prod_i \mathcal{F}(U_i)$$이고, $$C^0$$에서 $$C^1$$로의 coboundary map은

$$(ds)_{ij} = s_j\vert_{U_i \cap U_j} - s_i\vert_{U_i \cap U_j}$$

이다. 따라서

$$\check{H}^0(\mathcal{U}, \mathcal{F}) = \ker(d: C^0 \to C^1) = \{(s_i) \in \prod_i \mathcal{F}(U_i) : s_i\vert_{U_i \cap U_j} = s_j\vert_{U_i \cap U_j} \text{ for all } i, j\}$$

이다. Sheaf의 gluing condition ([\[위상수학\] §층, ⁋정의 1](/ko/math/topology/sheaves#def1))에 의해 이러한 section들의 family는 정확히 $$X$$ 전체 위에서의 section, 즉 $$\Gamma(X, \mathcal{F})$$와 일치한다. 즉, $$\check{H}^0(\mathcal{U}, \mathcal{F}) = H^0(X, \mathcal{F})$$이며 이는 open cover의 선택과 무관하다.

</div>

<div class="example" markdown="1">

<ins id="ex6">**예시 6** ($$p = 1$$)</ins> 1-cochain은 각 $$U_i \cap U_j$$ 위의 section $$s_{ij} \in \mathcal{F}(U_i \cap U_j)$$들의 모임이며, 1-cocycle은 cocycle condition

$$s_{ij} + s_{jk} = s_{ik} \quad\text{on } U_i \cap U_j \cap U_k$$

을 만족하는 것들이다. 한편 1-coboundary는 0-cochain $$(t_i)$$로부터 유도되는 것, 즉 $$s_{ij} = t_j\vert_{U_i \cap U_j} - t_i\vert_{U_i \cap U_j}$$의 꼴이다.

따라서 $$\check{H}^1(\mathcal{U}, \mathcal{F})$$는 "각각의 overlap 위에서 section이 주어져 있고, 세 개 이상의 열린집합이 겹치는 곳에서는 이 section들이 compatible하지만, 이를 하나의 전역 section으로 이어붙일 수는 없는" 데이터들의 모임을 coboundary에 의한 동치관계로 나눈 것이다. 이는 $$\mathcal{F}$$의 torsor (또는 principal homogeneous space)를 분류한다. 예를 들어, 만약 $$\mathcal{F} = \mathcal{O}_X$$라면 $$\check{H}^1(\mathcal{U}, \mathcal{O}_X)$$는 $$X$$의 위상이 만들어내는 "함수의 이음새 불일치"를 측정하는 양이다. 이것이 바로 도입부에서 말한 "local section의 gluing 실패"의 구체적인 예시이다.

</div>

지금까지 우리는 하나의 open cover $$\mathcal{U}$$에 대하여 Čech cohomology $$\check{H}^p(\mathcal{U}, \mathcal{F})$$를 정의하였다. 그러나 일반적으로 서로 다른 open cover는 서로 다른 Čech cohomology를 줄 수 있다. 가령 하나의 열린집합 $$U_0 = X$$으로 이루어진 cover에서는 모든 교집합이 $$X$$이므로 $$\check{H}^p$$가 $$p = 0$$에서만 0이 아닌 값을 갖는다. 더 조밀한 cover를 사용할수록 더 많은 위상적 정보를 포착할 수 있으므로, 우리는 open cover들 사이의 관계를 규명하고 모든 open cover에 대한 정보를 종합할 필요가 있다.

Open cover $$\mathcal{V} = \{V_j\}$$가 $$\mathcal{U} = \{U_i\}$$의 *refinement*라는 것은 각 $$j$$에 대해 $$V_j \subseteq U_{\tau(j)}$$인 함수 $$\tau: J \to I$$가 존재하는 것이다. Refinement $$\mathcal{V} \preceq \mathcal{U}$$에 대하여 natural map $$\check{H}^p(\mathcal{U}, \mathcal{F}) \to \check{H}^p(\mathcal{V}, \mathcal{F})$$가 존재한다.

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> *Čech cohomology of $$X$$*를 모든 open cover에 대한 direct limit으로 정의한다:

$$\check{H}^p(X, \mathcal{F}) = \varinjlim_{\mathcal{U}} \check{H}^p(\mathcal{U}, \mathcal{F})$$

</div>

Direct limit을 취하는 것은 open cover를 점점 더 조밀하게 만들면서 cohomology 정보를 "모두 합친다"는 의미이다. Refinement 관계는 cohomology 사이의 map을 유도하므로, 이들로 이루어진 directed system의 direct limit을 취할 수 있다. 특히 이 direct limit은 $$p = 0$$에서는 $$H^0(X, \mathcal{F})$$와 일치한다. 왜냐하면 임의의 open cover에 대해 $$\check{H}^0(\mathcal{U}, \mathcal{F}) = \Gamma(X, \mathcal{F})$$이므로 direct limit도 같은 값이 되기 때문이다.

## Čech와 Sheaf Cohomology의 비교

일반적으로 [정의 7](#def7)의 $$\check{H}^p(X, \mathcal{F})$$와 [정의 1](#def1)의 $$H^p(X, \mathcal{F})$$는 동형이라고 보장되지 않는다. 그러나 다행히 대수기하학에서 등장하는 대부분의 sheaf에 대해서는 둘이 일치하며, 이 절에서는 그 조건을 규명한다.

<div class="definition" markdown="1">

<ins id="def8">**정의 8** (Acyclic)</ins> Sheaf $$\mathcal{F}$$가 *acyclic*이라는 것은 모든 $$i > 0$$에 대해 $$H^i(X, \mathcal{F}) = 0$$인 것이다. 

</div>

예를 들어 *flasque sheaf*, 즉 임의의 열린집합 $$V \subseteq U$$에 대해 제한 사상 $$\mathcal{F}(U) \to \mathcal{F}(V)$$가 surjective인 sheaf는 acyclic이다. Injective sheaf 역시 항상 flasque이므로 acyclic이다. 대수기하학에서 특히 중요한 것은 quasi-coherent sheaf가 아핀다양체 위에서 acyclic이라는 사실이다.

<div class="proposition" markdown="1">

<ins id="thm9">**정리 9** (Leray)</ins> Open cover $$\mathcal{U} = \{U_i\}$$에 대해 모든 유한 교집합 $$U_{i_0 \cdots i_p}$$에서 $$\mathcal{F}$$가 acyclic (즉 $$H^{>0}(U_{i_0 \cdots i_p}, \mathcal{F}) = 0$$)이면:

$$\check{H}^p(\mathcal{U}, \mathcal{F}) \cong H^p(X, \mathcal{F})$$

이 때, natural map $$\check{H}^p(\mathcal{U}, \mathcal{F}) \to H^p(X, \mathcal{F})$$이 isomorphism이 된다.

</div>

이 정리는 $$\mathcal{F}$$의 injective resolution $$\mathcal{I}^\bullet$$을 이용하여 double complex $$C^{p,q} = \check{C}^p(\mathcal{U}, \mathcal{I}^q)$$를 구성한 뒤, 두 방향의 filtration으로부터 얻어지는 spectral sequence argument로 증명된다. Natural map $$\check{H}^p(X, \mathcal{F}) \to H^p(X, \mathcal{F})$$는 항상 존재하며 $$p = 0, 1$$에서는 isomorphism이지만, $$p \geq 2$$에서는 일반적으로 isomorphism이 아니다. Leray 정리는 acyclic cover라는 조건 하에서 이 natural map이 모든 차수에서 isomorphism이 됨을 보장한다.

<div class="proposition" markdown="1">

<ins id="cor10">**따름정리 10**</ins> Separated variety $$X$$ 위의 quasi-coherent sheaf $$\mathcal{F}$$와 affine open cover $$\mathcal{U}$$에 대해:

$$\check{H}^p(\mathcal{U}, \mathcal{F}) \cong H^p(X, \mathcal{F})$$

</div>

아핀다양체 $$U$$ 위에서 quasi-coherent sheaf $$\mathcal{F} = \widetilde{M}$$의 cohomology는 모두 0이므로(즉 $$H^i(U, \mathcal{F}) = 0$$ for $$i > 0$$), [정리 9](#thm9)의 acyclic 조건을 확인하려면 affine open cover의 모든 유한 교집합이 다시 아핀다양체이면 충분하다. Separated variety에서는 두 affine 열린집합의 교집합이 다시 affine이며(이는 diagonal $$\Delta_X \hookrightarrow X \times X$$가 closed immersion이라는 사실과 동치이다), 따라서 임의의 유한 개의 affine 열린집합의 교집합도 inductively affine이 되어 acyclic 조건이 자동으로 충족된다. 이 사실은 대수기하학에서 Čech cohomology가 sheaf cohomology의 실질적인 계산 도구로 널리 사용되는 이유이다.

## 예시: $$S^1$$ 위의 Constant Sheaf

지금까지의 이론을 구체적인 계산 예시로 확인해보자. 가장 고전적인 예시는 circle $$S^1$$ 위에서의 constant sheaf $$\underline{\mathbb{Z}}$$의 Čech cohomology를 계산하는 것이다. 이 예시는 Čech complex의 작동 방식을 직접적으로 보여주며, 그 결과가 우리의 위상적 직관과 일치한다는 것을 확인할 수 있다.

<div class="example" markdown="1">

<ins id="ex11">**예시 11** ($$S^1$$ 위의 constant sheaf)</ins> Circle $$S^1$$을 두 개의 열린 호 $$U_1, U_2$$로 cover하자. $$U_1 \cap U_2$$는 두 개의 연결성분 $$V_1, V_2$$를 갖는다.

Constant sheaf $$\underline{\mathbb{Z}}$$에 대해 Čech complex를 계산하자. 먼저 $$C^0 = \mathcal{F}(U_1) \times \mathcal{F}(U_2) = \mathbb{Z} \times \mathbb{Z}$$이다. $$C^1 = \mathcal{F}(U_1 \cap U_2) = \mathcal{F}(V_1) \times \mathcal{F}(V_2) = \mathbb{Z} \times \mathbb{Z}$$이다. Coboundary map $$d: C^0 \to C^1$$은

$$d(s_1, s_2) = s_2\vert_{U_1 \cap U_2} - s_1\vert_{U_1 \cap U_2} = (s_2 - s_1, s_2 - s_1)$$

이다(여기서 $$V_1, V_2$$ 각각에서 $$s_2 - s_1$$의 값이 같은 이유는 $$U_1, U_2$$가 각각 연결되어 있어 constant sheaf의 section이 각각 하나의 정수로 결정되기 때문이다).

이제 각 cohomology group을 계산한다.

- *$$\check{H}^0(\mathcal{U}, \underline{\mathbb{Z}})$$*: $$\ker(d) = \{(s_1, s_2) : s_1 = s_2\} \cong \mathbb{Z}$$. 이것은 $$S^1$$ 전체 위에서의 상수함수이며, $$\Gamma(S^1, \underline{\mathbb{Z}}) \cong \mathbb{Z}$$와 일치한다.

- *$$\check{H}^1(\mathcal{U}, \underline{\mathbb{Z}})$$*: Cover가 2개의 열린집합으로 이루어져 있어 세 개 이상의 열린집합이 겹치는 곳이 존재하지 않으므로, cocycle condition이 vacuous하게 만족되어 모든 1-cochain이 자동으로 cocycle이다. 따라서 1-cocycle은 $$(a, b) \in \mathbb{Z} \times \mathbb{Z}$$이다. Coboundary는 $$d(s_1, s_2) = (s_2 - s_1, s_2 - s_1)$$의 꼴이므로, cocycle $$(a, b)$$와 $$(a', b')$$이 같은 cohomology class에 속할 필요충분조건은 $$a - a' = b - b'$$인 것이다. 따라서 invariant는 차이 $$a - b \in \mathbb{Z}$$이고, $$\check{H}^1(\mathcal{U}, \underline{\mathbb{Z}}) \cong \mathbb{Z}$$이다.

이 결과 $$\check{H}^1(S^1, \mathbb{Z}) \cong \mathbb{Z}$$는 $$S^1$$의 "빈 구멍"이 하나 있다는 위상적 사실을 cohomology가 정확히 포착하고 있음을 보여준다. 일반적으로 $$H^1(S^1, \mathbb{Z}) \cong \mathbb{Z}$$와 일치한다.

</div>

## Application: Line Bundle의 분류

앞서 우리는 line bundle이 transition function $$g_{ij} \in \mathcal{O}_X^\ast(U_i \cap U_j)$$들로 결정된다는 것을 보았다 ([§선다발과 벡터다발, ⁋명제 2](/ko/math/algebraic_geometry/line_bundles#prop2)). Transition function들은 cocycle condition $$g_{ij}g_{jk} = g_{ik}$$을 만족하는데, 이는 multiplicative notation으로 쓴 Čech 1-cocycle condition에 정확히 해당한다. 또한 line bundle의 isomorphism은 각 $$U_i$$ 위에서의 함수 $$h_i \in \mathcal{O}_X^\ast(U_i)$$에 의해 $$g_{ij} \mapsto h_i g_{ij} h_j^{-1}$$로 transition function이 변하는 것이므로, 이 역시 Čech 1-coboundary에 의한 동치관계와 일치한다. 즉, line bundle의 isomorphism class는 $$\check{H}^1(X, \mathcal{O}_X^\ast)$$의 원소와 자연스럽게 대응된다.

이 관찰을 엄밀하게 정리하면 다음을 얻는다. 여기서 주의할 점은 $$\mathcal{O}_X^\ast$$가 곱셈적 구조를 갖는 sheaf of (abelian) groups이므로, Čech cohomology에서 coboundary 관계가 덧셈적이 아닌 곱셈적으로 표현된다는 것이다. 구체적으로 1-coboundary는 $$(g_{ij}) = (h_i \cdot h_j^{-1})$$의 꼴이다.

<div class="proposition" markdown="1">

<ins id="prop12">**명제 12**</ins> $$\check{H}^1(X, \mathcal{O}_X^\ast) \cong \operatorname{Pic}(X)$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

우선 $$\check{H}^1(X, \mathcal{O}_X^\ast)$$에서 $$\operatorname{Pic}(X)$$로의 map을 정의한다. Čech 1-cocycle $$(g_{ij}) \in \check{Z}^1(\mathcal{U}, \mathcal{O}_X^\ast)$$가 주어지면, 이를 transition function으로 하는 line bundle $$\mathcal{L}$$을 구성한다. 구체적으로, 각 $$U_i$$ 위에서는 trivial bundle $$U_i \times \mathbb{A}^1$$을 잡고, $$U_i \cap U_j$$ 위에서는 $$(p, t) \mapsto (p, g_{ij}(p)t)$$으로 접착한다. Cocycle condition $$g_{ij}g_{jk} = g_{ik}$$에 의해 이 접착이 consistent하므로 well-defined line bundle이 얻어진다.

Coboundary에 의해 동치인 두 cocycle $$g_{ij}^{\mathcal{L}} = h_i g_{ij}^{\mathcal{M}} h_j^{-1}$$이 주어지면, 대응하는 두 line bundle 사이의 isomorphism을 $$\varphi_i: \mathcal{L}\vert_{U_i} \to \mathcal{M}\vert_{U_i}$$, $$v \mapsto h_i^{-1} v$$로 정의한다. 그러면 $$\varphi_i$$와 $$\varphi_j$$가 $$U_i \cap U_j$$에서 compatible임은

$$g_{ij}^{\mathcal{M}} \cdot \varphi_j(v) = g_{ij}^{\mathcal{M}} h_j^{-1} v = h_i^{-1} (h_i g_{ij}^{\mathcal{M}} h_j^{-1}) v = h_i^{-1} g_{ij}^{\mathcal{L}} v = \varphi_i(g_{ij}^{\mathcal{L}} v)$$

에서 확인된다. 따라서 map $$\check{H}^1(\mathcal{U}, \mathcal{O}_X^\ast) \to \operatorname{Pic}(X)$$가 well-defined이다.

역으로, 임의의 line bundle $$\mathcal{L}$$은 ([§선다발과 벡터다발, ⁋정의 1](/ko/math/algebraic_geometry/line_bundles#def1))에 의해 적당한 open cover $$\mathcal{U}$$ 위에서 transition function $$g_{ij}$$로 표현되며, 이는 Čech 1-cocycle을 이룬다. Line bundle isomorphism은 정확히 coboundary에 의한 동치관계에 해당하므로, 이 map의 kernel은 coboundary들이다. 따라서 $$\check{H}^1(\mathcal{U}, \mathcal{O}_X^\ast) \to \operatorname{Pic}(X)$$는 injective이다.

Direct limit을 취하면 $$\check{H}^1(X, \mathcal{O}_X^\ast) \cong \operatorname{Pic}(X)$$를 얻는다.

</details>

이 명제는 line bundle의 기하학적 분류 문제가 cohomology의 대수적 계산 문제로 번역됨을 보여준다. 가령 $$\operatorname{Pic}(X)$$의 원소를 찾는 문제는 이제 $$\mathcal{O}_X^\ast$$-valued Čech 1-cocycle을 분류하는 문제가 되며, 이는 구체적인 계산이 가능한 형태이다. $$\mathbb{P}^n$$ 위의 line bundle $$\mathcal{O}(k)$$의 cohomology 계산은 ([§Cohomology of Line Bundles on $$\mathbb{P}^n$$](/ko/math/algebraic_geometry/cohomology_of_line_bundles))에서 상세히 다룬다.

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.  
**[God]** R. Godement, *Topologie algébrique et théorie des faisceaux*, Hermann, 1958.

---

[^1]: 더 일반적으로, [[\[위상수학\] §층, §층들의 가환범주](/ko/math/topology/sheaves#층들의-가환범주)에서 살펴보았듯 임의의 위상공간 $$X$$ 위에 정의된 sheaf들의 category $$\Sh(X)$$는 abelian category를 이룬다.