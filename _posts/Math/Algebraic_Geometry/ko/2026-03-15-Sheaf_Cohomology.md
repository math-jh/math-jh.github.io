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


가령 [§선다발과 벡터다발](/ko/math/algebraic_geometry/line_bundles)에서 우리는 line bundle $$\mathcal{L}$$의 global section space $$\Gamma(X, \mathcal{L})$$을 정의하였다. 특히 [§선형계, ⁋명제 7](/ko/math/algebraic_geometry/linear_systems#prop7)에서는 이 차원이 complete linear system의 dimension, 나아가 variety의 projective embedding을 결정하는 핵심적 역할을 한다는 것을 살펴보았다. 

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

$$H^i(X, \mathcal{F}) = \frac{\ker(\Gamma(X, \mathcal{I}^i) \to \Gamma(X, \mathcal{I}^{i+1}))}{\im(\Gamma(X, \mathcal{I}^{i-1}) \to \Gamma(X, \mathcal{I}^i))}$$

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

$$(d\alpha)_{i_0 \cdots i_{p+1}} = \sum_{k=0}^{p+1} (-1)^k \alpha_{i_0 \cdots \hat{i_k} \cdots i_{p+1}}\vert_{U_{i_0}\cap \cdots \cap U_{i_{p+1}}}$$

으로 정의된다. 여기서 $$\hat{i_k}$$는 index $$i_k$$를 생략한다는 의미이다.

</div>

이 정의가 잘 정의되기 위해서는, 즉, $$\check{C}^\bullet(\mathcal{U}, \mathcal{F})$$이 실제로 complex가 되기 위해서는 coboundary map이 실제로 coboundary map이 되어야 한다. 즉 $$d^2=0$$이어야 한다. 이는 위의 식을 전개해보면 부호 차이로부터 직접 확인할 수 있다. 결론적으로 $$\check{C}^\bullet(\mathcal{U}, \mathcal{F})$$는 cochain complex이며, 따라서 다음을 정의할 수 있다. 

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> *Čech cohomology<sub>체흐 코호몰로지</sub>* $$\check{H}^p(\mathcal{U}, \mathcal{F})$$를 Čech complex의 cohomology

$$\check{H}^p(\mathcal{U}, \mathcal{F}) = H^p(\check{C}^\bullet(\mathcal{U}, \mathcal{F}))$$

로 정의한다. 

</div>

우리는 앞서 Čech cohomology가 gluing의 실패를 측정해주는 도구라 하였는데, 이는 coboundary map에 담겨있다. Coboundary map의 직관적 의미를 낮은 차원 $$p = 0, 1$$에서 확인해보자. 

<div class="example" markdown="1">

<ins id="ex5">**예시 5 ($$p = 0$$)**</ins> Čech complex의 정의에 의하여 $$\check{C}^0(\mathcal{U}, \mathcal{F}) = \prod_i \mathcal{F}(U_i)$$이고, $$\check{C}^0$$에서 $$\check{C}^1$$로의 coboundary map은

$$(ds)_{ij} = s_j\vert_{U_i \cap U_j} - s_i\vert_{U_i \cap U_j}$$

이다. 따라서

$$\check{H}^0(\mathcal{U}, \mathcal{F}) = \ker(d: \check{C}^0 \to \check{C}^1) = \left\{(s_i) \in \prod_i \mathcal{F}(U_i) \mid s_i\vert_{U_i \cap U_j} = s_j\vert_{U_i \cap U_j} \text{ for all } i, j\right\}$$

이다. Sheaf의 gluing condition ([\[위상수학\] §층, ⁋정의 1](/ko/math/topology/sheaves#def1))에 의해 이러한 section들의 family는 정확히 $$X$$ 전체 위에서의 section, 즉 $$\Gamma(X, \mathcal{F})$$와 일치한다. 즉, $$\check{H}^0(\mathcal{U}, \mathcal{F}) = H^0(X, \mathcal{F})$$이며 이는 open cover의 선택과 무관하다.

</div>

우리는 곧 좋은 상황에서는 위와 같이 Čech cohomology와 sheaf cohomology가 항상 같다는 것을 보일 것이다. 지금은 우선 $$p=1$$인 경우 이것이 어떻게 gluing의 failure를 측정하는지를 보자.

<div class="example" markdown="1">

<ins id="ex6">**예시 6 ($$p = 1$$)**</ins> 1-cochain은 각 $$U_i \cap U_j$$ 위의 section $$s_{ij} \in \mathcal{F}(U_i \cap U_j)$$들의 모임이며, 1-cocycle은 cocycle condition

$$s_{ij} + s_{jk} = s_{ik} \quad\text{on } U_i \cap U_j \cap U_k$$

을 만족하는 것들이다. 한편 1-coboundary는 0-cochain $$(t_i)$$로부터 유도되는 것, 즉 $$s_{ij} = t_j\vert_{U_i \cap U_j} - t_i\vert_{U_i \cap U_j}$$의 꼴이다.

따라서 $$\check{H}^1(\mathcal{U}, \mathcal{F})$$의 nontrivial한 원소는 이들 세 데이터 $$s_{ij}, s_{jk}, s_{ik}$$를 붙이려 할 때 나타나는 차이를 반영하는 것이며, 이것이 위에서 언급한 gluing의 failure라 할 수 있다.

</div>

지금까지 우리는 하나의 open cover $$\mathcal{U}$$에 대하여 Čech cohomology $$\check{H}^p(\mathcal{U}, \mathcal{F})$$를 정의하였다. 그러나 일반적으로 서로 다른 open cover는 서로 다른 Čech cohomology를 줄 수 있다. 가령 하나의 열린집합 $$U_0 = X$$으로 이루어진 cover에서는 모든 교집합이 $$X$$이므로 $$\check{H}^p$$가 $$p = 0$$에서만 0이 아닌 값을 갖는다. 더 조밀한 cover를 사용할수록 더 많은 위상적 정보를 포착할 수 있으므로, 우리는 open cover들 사이의 관계를 규명하고 모든 open cover에 대한 정보를 종합할 필요가 있다. 즉, <em-ko>모든</em-ko> open cover들에, refinement를 사용하여 순서관계를 주자. 그럼 refinement $$\mathcal{V} \preceq \mathcal{U}$$에 대하여 natural map $$\check{H}^p(\mathcal{U}, \mathcal{F}) \to \check{H}^p(\mathcal{V}, \mathcal{F})$$가 존재한다는 것이 자명하며, 따라서 모든 open cover들을 index set 삼아 direct system $$\check{H}^p(\mathcal{U}, \mathcal{F})$$을 정의할 수 있다. 이로부터 다음을 정의한다. 

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> *Čech cohomology of $$X$$*를 모든 open cover에 대한 direct limit으로 정의한다:

$$\check{H}^p(X, \mathcal{F}) = \varinjlim_{\mathcal{U}} \check{H}^p(\mathcal{U}, \mathcal{F})$$

</div>

위의 논증을 더 간단히 설명하자면, open cover를 점점 더 세밀하게 잡으며 추가되는 cohomology data를 모두 합쳐 이를 $$\check{H}(X, \mathcal{F})$$로 정의하겠다는 의미이다.

일반적으로 [정의 7](#def7)의 $$\check{H}^p(X, \mathcal{F})$$와 [정의 1](#def1)의 $$H^p(X, \mathcal{F})$$가 isomorphic하다는 것은 보장되지 않지만, 다행히 대수기하학에서 등장하는 대부분의 sheaf에 대해서는 둘이 일치한다. 이 조건을 쓰기 위해 우선 다음을 정의하자. 

<div class="definition" markdown="1">

<ins id="def8">**정의 8**</ins> 위상공간 $$X$$ 위의 sheaf $$\mathcal{F}$$가 *acyclic*이라는 것은 모든 $$i > 0$$에 대해 $$H^i(X, \mathcal{F}) = 0$$인 것이다.

</div>

만일 임의의 열린집합 $$V \subseteq U$$에 대해, restriction map $$\mathcal{F}(U) \to \mathcal{F}(V)$$가 surjective라면 우리는 $$\mathcal{F}$$를 *flasque* sheaf라 부르며, 이는 acyclic sheaf의 대표적인 예시이다. 앞서 말했듯, 대수기하에서 좋은 경우에는 Čech cohomology와 sheaf cohomology가 일치하는데, 이는 다음 정리를 의미한다. 

<div class="proposition" markdown="1">

<ins id="thm9">**정리 9** (Leray)</ins> 위상공간 $$X$$ 위의 sheaf $$\mathcal{F}$$와 open cover $$\mathcal{U} = \{U_i\}$$에 대하여, 모든 유한 교집합 $$U_{i_0 \cdots i_p}$$에서 $$\mathcal{F}$$가 acyclic이면 자연스러운 map

$$\check{H}^p(\mathcal{U}, \mathcal{F}) \to H^p(X, \mathcal{F})$$

이 isomorphism이다. 즉, Čech cohomology가 sheaf cohomology와 일치한다.

</div>

이를 증명하기 위해서는 주어진 sheaf $$\mathcal{F}$$의 injective resolution $$\mathcal{I}^\bullet$$과 이들 각각에 대한 Čech complex $$\check{C}^p(\mathcal{U}, \mathcal{I}^q)$$를 생각하여 double complex를 구성한 후 spectral sequence argument를 사용하면 된다. 중요한 것은 이 acyclic 조건이 생각보다는 널널한 조건이라는 것이다. 

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10**</ins> Affine variety $$X$$ 위의 quasi-coherent sheaf $$\mathcal{F} = \widetilde{M}$$에 대하여, $$H^i(X, \mathcal{F}) = 0$$이 모든 $$i > 0$$에 대해 성립한다.

</div>

이에 대한 증명은, $$X$$의 coordinate ring을 $$A$$라 할 때, $$\lMod{A}$$ 카테고리에서 $$M$$의 injective resolution $$I^\bullet$$을 찾으면 이것이 ($$\QCoh(X)$$에서의 resolution인) $$\widetilde{I^\bullet}$$을 주며, 이 때 injective module이 주는 sheaf는 항상 flasque이고, 따라서 acyclic이기 때문이다. 

이제 임의의 variety $$X$$와 그 위에 정의된 quasi-coherent sheaf $$\mathcal{F}$$를 생각하고, $$\mathcal{F}$$의 affine open cover $$\mathcal{U}$$가 주어졌다 하자. 그럼 이들 데이터가 [정리 9](#thm9)의 전제조건을 만족하기 위해서는 $$\mathcal{U}$$의 임의의 유한한 교집합이 다시 affine이어야 하는 것이다. 만일, diagonal

$$\Delta_X\hookrightarrow X\times X$$

이 $$X\times X$$의 *closed* immersion이라면, 이 조건이 성립하는 것을 보일 수 있으며 이런 경우 $$X$$가 *separated* variety라 부른다. 이는 (그 정의에서 알 수 있듯) Hausdorff 조건의 Zariski topology 버전이라 할 수 있으며 그만큼 합당한 조건이며, 현재 우리의 정의와 같이 quasi-projective variety를 variety라 부른다면 이 조건은 자동으로 충족된다. 즉, 현재 우리의 언어에서 이 논증은 임의의 variety 위에 정의된 quasi-coherent sheaf에 대해서는 Čech cohomology와 sheaf cohomology가 일치한다는 말이 된다.

지금까지의 이론을 구체적인 계산 예시로 확인해보자. 

<div class="example" markdown="1">

<ins id="ex11">**예시 11** ($$S^1$$ 위의 constant sheaf)</ins> Circle $$S^1$$을 두 개의 열린 arc $$U_1, U_2$$로 cover하자. $$U_1 \cap U_2$$는 두 개의 connected component $$V_1, V_2$$를 갖는다.

Constant sheaf $$\underline{\mathbb{Z}}$$에 대해 Čech complex를 계산하자. 먼저 $$C^0 = \mathcal{F}(U_1) \times \mathcal{F}(U_2) = \mathbb{Z} \times \mathbb{Z}$$이다. $$C^1 = \mathcal{F}(U_1 \cap U_2) = \mathcal{F}(V_1) \times \mathcal{F}(V_2) = \mathbb{Z} \times \mathbb{Z}$$이다. Coboundary map $$d: C^0 \to C^1$$은

$$d(s_1, s_2) = s_2\vert_{U_1 \cap U_2} - s_1\vert_{U_1 \cap U_2} = (s_2 - s_1, s_2 - s_1)$$

이다(여기서 $$V_1, V_2$$ 각각에서 $$s_2 - s_1$$의 값이 같은 이유는 $$U_1, U_2$$가 각각 connected이므로 constant sheaf의 section이 각각 하나의 정수로 결정되기 때문이다).

이제 각 cohomology group을 계산한다.

- *$$\check{H}^0(\mathcal{U}, \underline{\mathbb{Z}})$$*: $$\ker(d) = \{(s_1, s_2) : s_1 = s_2\} \cong \mathbb{Z}$$. 이것은 $$S^1$$ 전체 위에서의 상수함수이며, $$\Gamma(S^1, \underline{\mathbb{Z}}) \cong \mathbb{Z}$$와 일치한다.

- *$$\check{H}^1(\mathcal{U}, \underline{\mathbb{Z}})$$*: Cover가 2개의 열린집합으로 이루어져 있어 세 개 이상의 열린집합이 겹치는 곳이 존재하지 않으므로, cocycle condition이 vacuous하게 만족되어 모든 1-cochain이 자동으로 cocycle이다. 따라서 1-cocycle은 $$(a, b) \in \mathbb{Z} \times \mathbb{Z}$$이다. Coboundary는 $$d(s_1, s_2) = (s_2 - s_1, s_2 - s_1)$$의 꼴이므로, cocycle $$(a, b)$$와 $$(a', b')$$이 같은 cohomology class에 속할 필요충분조건은 $$a - a' = b - b'$$인 것이다. 따라서 invariant는 차이 $$a - b \in \mathbb{Z}$$이고, $$\check{H}^1(\mathcal{U}, \underline{\mathbb{Z}}) \cong \mathbb{Z}$$이다.

</div>

## Line Bundle의 Classification

앞서 우리는 line bundle이 transition function $$g_{ij} \in \mathcal{O}_X^\ast(U_i \cap U_j)$$들로 결정된다는 것을 보았다 ([§선다발과 벡터다발, ⁋명제 2](/ko/math/algebraic_geometry/line_bundles#prop2)). Transition function들은 cocycle condition $$g_{ij}g_{jk} = g_{ik}$$을 만족하는데, 이는 multiplicative notation으로 쓴 Čech 1-cocycle condition에 정확히 해당한다. 또한 line bundle의 isomorphism은 각 $$U_i$$ 위에서의 함수 $$h_i \in \mathcal{O}_X^\ast(U_i)$$에 의해 $$g_{ij} \mapsto h_i g_{ij} h_j^{-1}$$로 transition function이 변하는 것이므로, 이 역시 Čech 1-coboundary에 의한 동치관계와 일치한다. 즉, line bundle의 isomorphism class는 $$\check{H}^1(X, \mathcal{O}_X^\ast)$$의 원소와 자연스럽게 대응된다.

이 관찰을 엄밀하게 정리하면 다음을 얻는다. 여기서 주의할 점은 $$\mathcal{O}_X^\ast$$가 곱셈적 구조를 갖는 sheaf of (abelian) groups이므로, Čech cohomology에서 coboundary 관계가 덧셈적이 아닌 곱셈적으로 표현된다는 것이다. 구체적으로 1-coboundary는 $$(g_{ij}) = (h_i \cdot h_j^{-1})$$의 꼴이다.

<div class="proposition" markdown="1">

<ins id="prop12">**명제 12**</ins> $$\check{H}^1(X, \mathcal{O}_X^\ast) \cong \Pic(X)$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

우선 $$\check{H}^1(X, \mathcal{O}_X^\ast)$$에서 $$\Pic(X)$$로의 map을 정의한다. Čech 1-cocycle $$(g_{ij}) \in \check{Z}^1(\mathcal{U}, \mathcal{O}_X^\ast)$$가 주어지면, 이를 transition function으로 하는 line bundle $$\mathcal{L}$$을 구성한다. 구체적으로, 각 $$U_i$$ 위에서는 trivial bundle $$U_i \times \mathbb{A}^1$$을 잡고, $$U_i \cap U_j$$ 위에서는 $$(p, t) \mapsto (p, g_{ij}(p)t)$$으로 접착한다. Cocycle condition $$g_{ij}g_{jk} = g_{ik}$$에 의해 이 접착이 consistent하므로 well-defined line bundle이 얻어진다.

Coboundary에 의해 동치인 두 cocycle $$g_{ij}^{\mathcal{L}} = h_i g_{ij}^{\mathcal{M}} h_j^{-1}$$이 주어지면, 대응하는 두 line bundle 사이의 isomorphism을 $$\varphi_i: \mathcal{L}\vert_{U_i} \to \mathcal{M}\vert_{U_i}$$, $$v \mapsto h_i^{-1} v$$로 정의한다. 그러면 $$\varphi_i$$와 $$\varphi_j$$가 $$U_i \cap U_j$$에서 compatible임은

$$g_{ij}^{\mathcal{M}} \cdot \varphi_j(v) = g_{ij}^{\mathcal{M}} h_j^{-1} v = h_i^{-1} (h_i g_{ij}^{\mathcal{M}} h_j^{-1}) v = h_i^{-1} g_{ij}^{\mathcal{L}} v = \varphi_i(g_{ij}^{\mathcal{L}} v)$$

에서 확인된다. 따라서 map $$\check{H}^1(\mathcal{U}, \mathcal{O}_X^\ast) \to \Pic(X)$$가 well-defined이다.

역으로, 임의의 line bundle $$\mathcal{L}$$은 ([§선다발과 벡터다발, ⁋정의 1](/ko/math/algebraic_geometry/line_bundles#def1))에 의해 적당한 open cover $$\mathcal{U}$$ 위에서 transition function $$g_{ij}$$로 표현되며, 이는 Čech 1-cocycle을 이룬다. Line bundle isomorphism은 정확히 coboundary에 의한 동치관계에 해당하므로, 이 map의 kernel은 coboundary들이다. 따라서 $$\check{H}^1(\mathcal{U}, \mathcal{O}_X^\ast) \to \Pic(X)$$는 injective이다.

Direct limit을 취하면 $$\check{H}^1(X, \mathcal{O}_X^\ast) \cong \Pic(X)$$를 얻는다.

</details>

이 명제는 line bundle의 classification이 cohomology의 계산으로 귀결된다는 것을 보여준다. 즉, $$\Pic(X)$$의 원소를 분류하는 문제는 이제 $$\mathcal{O}_X^\ast$$-valued Čech 1-cocycle을 분류하는 문제가 되며, 이는 어쨌든 [예시 11](#ex11)와 같이 명시적인 계산이 가능하다는 점에서 고무적이다. 다음 글 [§사영공간의 코호몰로지](/ko/math/algebraic_geometry/cohomology_of_projective_spaces)에서 우리는 $$\mathbb{P}^n$$ 위의 line bundle $$\mathcal{O}(d)$$의 cohomology를 계산한다. 

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.  
**[God]** R. Godement, *Topologie algébrique et théorie des faisceaux*, Hermann, 1958.

---

[^1]: 더 일반적으로, [[\[위상수학\] §층, §층들의 가환범주](/ko/math/topology/sheaves#층들의-가환범주)에서 살펴보았듯 임의의 위상공간 $$X$$ 위에 정의된 sheaf들의 category $$\Sh(X)$$는 abelian category를 이룬다.