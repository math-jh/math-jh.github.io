---
title: "From Varieties to Schemes"
excerpt: "Classical algebraic variety에서 scheme으로의 자연스러운 전환"
categories: [Math / Algebraic_Geometry]
permalink: /ko/math/algebraic_geometry/from_varieties_to_schemes
sidebar: { nav: "algebraic_geometry-ko" }
header: { overlay_image: /assets/images/Math/Algebraic_Geometry/From_Varieties_to_Schemes.png, overlay_filter: 0.5 }
date: 2026-05-07
last_modified_at: 2026-05-07
weight: 0
---

## Introduction

우리는 지금까지 classical algebraic geometry의 기본적인 틀을 따라가며, affine space 위에서 다항식의 공통 영점으로 정의되는 <em-ko>아핀다양체</em-ko>와 이들의 동차 다항식 버전인 <em-ko>사영다양체</em-ko>를 살펴 보았다. 이러한 대상들은 algebraically closed field 위에서 정의되며, Zariski topology와 regular function을 통해 기하학적 성질을 기술하는 전통적인 방식이었다. Classical framework은 직관적이고 많은 구체적인 예시를 제공하지만, 동시에 몇 가지 근본적인 질문을 던지게 한다. 예를 들어, 두 곡선이 한 점에서 접할 때 그 교차 정도를 어떻게 정확히 측정할 것인가, 혹은 infinitesimal한 정보를 기하학적으로 어떻게 포착할 것인가 하는 문제들이 그것이다. 이러한 질문들에 대한 자연스러운 해답을 찾는 과정에서 Grothendieck의 scheme theory가 등장하며, 이는 classical algebraic variety의 개념을 훨씬 더 넓은 맥락으로 확장시킨다.

본 글에서는 classical variety의 개념이 갖는 한계들을 구체적으로 살펴 보고, 이것이 scheme theory의 동기가 되는 과정을 직관적으로 설명한다. 우리의 목표는 scheme의 정의를 엄밀하게 전개하는 것이 아니라, variety에서 scheme으로 넘어가는 사고방식의 전환을 자연스럽게 느끼는 데 있다.

## Classical variety의 한계

Classical algebraic geometry에서는 주로 algebraically closed field $k$ 위에서 정의된 affine variety나 projective variety를 다룬다. 이러한 대상들은 직관적이고 계산하기에도 용이하지만, 몇 가지 본질적인 제약을 안고 있다. 그중 첫 번째는 <em-ko>generic point</em-ko>의 부재이다.

<div class="example" markdown="1">

<ins id="ex1">**예시 1**</ins> Affine plane $$\mathbb{A}^2$$ 위에서 직선 $$V(\y - \x)$$과 $$\x$$-축 $$V(\y)$$를 생각하자. 이들은 원점에서 교차하며, 이 교차의 multiplicity는 $$1$$이다. 반면에 포물선 $$V(\y - \x^2)$$과 $$\x$$-축 $$V(\y)$$의 교차는 원점에서 multiplicity $$2$$로 일어난다. Classical framework에서는 이 multiplicity를 local ring $$\mathcal{O}_{(0,0)}/(\y - \x^2, \y)$$의 길이로 계산해야 하며, 이는 직접적인 기하학적 직관과 다소 거리가 있는 대수적 계산에 의존한다. Scheme theory에서는 이 교차를 단순한 점의 집합이 아닌, generic point를 포함하는 보다 풍부한 공간 위에서 본다. 이로 인해 multiplicity가 공간의 내재적 구조로 자연스럽게 드러난다.

</div>

Generic point는 irreducible closed subset에 대응하는 점으로, classical variety에서는 등장하지 않는다. 예를 들어 $$\mathbb{A}^2$$의 원점 $$(0,0)$$은 maximal ideal $$(\x, \y)$$에 대응하지만, 직선 $$V(\y)$$ 자체를 나타내는 점, 즉 generic point는 prime ideal $$(\y)$$에 대응한다. Classical variety에서는 오직 closed point, 즉 $k$-rational point만을 다루므로, 이러한 generic point가 가지는 기하학적 정보를 놓치게 된다.

두 번째 한계는 <em-ko>nilpotent</em-ko>의 부재이다. Classical variety에서는 coordinate ring이 reduced ring이어야 하므로 nilpotent element를 허용하지 않는다. 이는 infinitesimal한 정보를 기하학적으로 표현하는 것을 불가능하게 만든다.

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins> Ring $k[\epsilon]/(\epsilon^2)$ 위에서 정의되는 $$\Spec k[\epsilon]/(\epsilon^2)$$를 생각하자. 이것은 단일한 점을 지니지만, 그 structure sheaf $$\mathcal{O}$$에는 nilpotent element $$\epsilon$$이 존재한다. 따라서 이 scheme은 일반적인 점보다 두꺼운, 소위 <em-ko>길이 2의 점</em-ko>으로 불린다. Classical variety의 범주에서는 이러한 대상은 절대로 나타날 수 없으며, 이는 곧 tangent vector나 infinitesimal deformation 같은 개념을 pure하게 기하학적으로 다루기 어렵게 만든다.

</div>

예를 들어, 어떤 variety 위의 점에서의 tangent space를 classical하게 정의하려면 해당 점 근방의 함수들의 미분을 고려해야 한다. 그러나 scheme theory에서는 $$\Spec k[\epsilon]/(\epsilon^2)$$로부터의 사상들을 통해 tangent vector를 직접적으로 parameterize할 수 있으며, 이는 기하학과 대수의 결합을 훨씬 더 자연스럽게 만든다.

세 번째로, classical variety는 base field에 강하게 의존한다. 예를 들어 정수 계수 다항식으로 정의된 variety를 생각할 때, 이를 여러 field에서 reduction mod $p$ 하거나 field extension을 취하는 과정은 classical framework에서 깔끔하게 다뤄지지 않는다. Variety의 정의가 특정 algebraically closed field에 묶여 있기 때문이다.

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> $$\Spec \mathbb{Z}[\x]$$를 생각하자. 이 scheme은 모든 소수 $p$에 대해 $$\mathbb{F}_p$$ 위의 fiber를 자연스럽게 지닌다. 즉, morphism $$\Spec \mathbb{Z}[\x] \to \Spec \mathbb{Z}$$라는 상대적 구조를 통해, 각 소수 위에서의 기하학적 상황을 하나의 대상 안에서 통합적으로 파악할 수 있다. Classical variety에서는 이러한 relative viewpoint를 갖추기 어렵다.

</div>

이러한 세 가지 한계는 모두 classical algebraic geometry의 기본적인 전제, 즉 기하학적 대상이 algebraically closed field 위의 점들의 집합으로 이핼되어야 한다는 관점에서 비롯된다. Scheme theory는 바로 이 전제를 해체함으로써 보다 유연하고 강력한 기구를 제공한다.

## Varieties as schemes

Classical variety가 scheme의 특수한 경우에 불과하다는 사실은 scheme theory를 배우는 데 있어 중요한 직관을 준다. 구체적으로, affine variety $V \subset \mathbb{A}^n$에 대해 그 coordinate ring $A = k[\x_1, \ldots, \x_n]/I(V)$를 생각하면 $$\Spec A$$가 대응하는 affine scheme이 된다. 여기서 $I(V)$는 $V$를 정의하는 ideal이며, classical setting에서는 이것이 radical ideal이므로 $A$는 reduced ring이다.

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> Affine scheme $$\Spec A$$는 commutative ring $A$의 prime ideal들의 집합 위에 Zariski topology를 부여하고, structure sheaf $$\mathcal{O}_{\Spec A}$$를 정의하여 얻어진 locally ringed space이다.

</div>

Projective variety에 대해서도 유사한 대응이 존재한다. Homogeneous coordinate ring $S = k[\x_0, \ldots, \x_n]/I$에 대해, $$\Proj S$$가 대응하는 projective scheme이 된다. Classical variety에서 projective variety는 homogeneous coordinate ring의 maximal homogeneous ideal들을 제외한 homogeneous prime ideal들에 대응했으므로, $$\Proj$$ construction은 이를 자연스럽게 확장한다.

이제 classical variety가 scheme의 범주에서 어떤 위치를 차지하는지 명확히 할 수 있다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> Algebraically closed field $k$ 위의 classical variety, 즉 reduced이고 irreducible이며 separated인 finite type $k$-scheme은 classical algebraic geometry에서 다루는 variety와 동일한 범주를 형성한다.

</div>

<details class="proof" markdown="1">

<summary>증명</summary>

Classical variety $V$에 대해 coordinate ring $A$를 대응시키는 functor는 affine case에서 fully faithful하다. Projective case에서는 homogeneous coordinate ring을 통해 유사한 대응이 성립한다. Reduced와 irreducible 조건은 classical variety가 nilpotent를 갖지 않으며 single irreducible component를 가짐을 보장하고, separated 조건은 Hausdorff 성질의 적절한 확장이며, finite type 조건은 $A$가 finitely generated $k$-algebra임을 의미한다. 이들 조건 하에서 classical variety와 해당 scheme 사이의 category equivalence가 성립한다.

</details>

Classical framework의 핵심 개념들도 scheme theory 내에서 그대로 해석된다. Zariski topology는 $$\Spec A$$ 위에서 natural하게 정의되며, regular function은 structure sheaf $$\mathcal{O}_X$$의 section으로, rational map은 function field를 통하지 않고도 morphism of schemes의 개념으로 자연스럽게 확장된다.

## New features of schemes

Scheme theory가 classical variety를 포함하면서도 어떤 새로운 특징들을 가져오는지 살펴 보자.

가장 먼저 눈에 띄는 것은 <em-ko>non-closed point</em-ko>의 존재이다. $$\Spec \mathbb{Z}[\x]$$를 생각하면, $(0)$은 $$\mathbb{Z}[\x]$$의 prime ideal이므로 $$\Spec \mathbb{Z}[\x]$$의 점이 된다. 이 점은 closed point가 아니며, 대신 전체 공간의 generic point에 대응한다. 마찬가지로 $$\Spec k[\x, \y]$$에서 $$(\x)$$는 $$\y$$-축의 generic point로, 해당 irreducible closed subset에 대응하는 점이다. 이러한 점들은 classical variety에서는 보이지 않았던, 공간의 전체적인 구조를 포착하는 정보를 담고 있다.

<div class="example" markdown="1">

<ins id="ex6">**예시 6**</ins> $$\Spec k[\x, \y]$$에서 $$(\x)$$는 $V(\x)$$, 즉 $$\y$$-축의 generic point이다. 이 점을 포함함으로써 우리는 $$\y$$-축 전체를 하나의 점으로 압축하여 볼 수 있으며, 이는 intersection theory나 divisor theory에서 필수적인 역할을 한다.

</div>

다음으로, structure sheaf $$\mathcal{O}_X$$가 nilpotent section을 가질 수 있다는 점이 중요하다. 이는 scheme이 단순한 점의 집합이 아니라, 각 점에 local ring을 덧붙인 풍부한 구조를 가짐을 의미한다.

<div class="example" markdown="1">

<ins id="ex7">**예시 7**</ins> $$\Spec k[\x, \y]/(\y^2)$$를 생각하자. 이 scheme의 기저 공간은 $$\x$$-축 $V(\y)$$와 동일하지만, structure sheaf에는 $$\y$$라는 nilpotent element가 남아 있다. 이는 $$\x$$-축에 대한 infinitesimal thickening, 즉 근방의 첫 번째 order 정보를 담고 있으며, deformation theory에서 핵심적인 역할을 한다.

</div>

마지막으로, scheme theory는 <em-ko>relative viewpoint</em-ko>를 자연스럽게 채택한다. Scheme $X$를 단순히 absolute object로 보는 대신, base scheme $S$ 위의 scheme $X \to S$로 보는 관점이다. 이는 classical variety가 특정 field 위에서만 정의되는 반면, scheme은 임의의 ring 위에서 정의될 수 있음을 반영한다.

<div class="definition" markdown="1">

<ins id="def8">**정의 8**</ins> $S$-scheme은 morphism $X \to S$를 데이터로 하는 scheme $X$를 의미한다. 특히 $S = \Spec \mathbb{Z}$인 경우를 absolute scheme이라 부른다.

</div>

Relative viewpoint는 base change를 자연스러운 개념으로 만든다. 예를 들어 $X \to \Spec \mathbb{Z}$가 주어지면, 임의의 ring homomorphism $$\mathbb{Z} \to R$$에 대해 fiber product $X \times_{\Spec \mathbb{Z}} \Spec R$를 취함으로써, $R$ 위에서의 해당 scheme의 모습을 쉽게 얻을 수 있다.

## Functor of points

Scheme을 이해하는 또 다른 중요한 관점은 <em-ko>functor of points</em-ko>이다. Scheme $X$를 하나의 공간으로 보는 대신, 다음과 같은 functor로 볼 수 있다.

<div class="definition" markdown="1">

<ins id="def9">**정의 9**</ins> Scheme $X$에 대해, functor $h_X: \Sch^{\op} \to \Set$를 $h_X(S) = \Hom(S, X)$로 정의한다. 이를 $X$의 functor of points라 부른다.

</div>

Classical variety에서는 주로 $k$-rational point $X(k) = \Hom(\Spec k, X)$만을 고려했다. 이는 affine variety의 경우 coordinate ring에서 $k$로의 homomorphism에 대응하며, 구체적인 좌표를 가진 점들의 집합이다. 그러나 functor of points는 모든 scheme $S$에 대해 $S$-point 집합 $X(S)$를 고려함으로써 훨씬 더 풍부한 정보를 담는다.

<div class="example" markdown="1">

<ins id="ex10">**예시 10**</ins> $$\mathbb{P}^1$$의 $k[\epsilon]/(\epsilon^2)$-points를 생각하자. 이들은 $$\Hom(\Spec k[\epsilon]/(\epsilon^2), \mathbb{P}^1)$$에 대응하며, $$\mathbb{P}^1$$ 위의 한 점과 해당 점에서의 tangent vector의 쌍을 parameterize한다. 다시 말해, $$\mathbb{P}^1(k[\epsilon]/(\epsilon^2))$$는 $$\mathbb{P}^1$$의 tangent bundle의 정보를 담고 있다.

</div>

이 관점이 특히 자연스러운 이유는, scheme이 본질적으로 임의의 ring 위에서의 다항식 방정식의 해를 나타내는 대상이기 때문이다. 예를 들어 affine scheme $$\Spec \mathbb{Z}[\x_1, \ldots, \x_n]/(f_1, \ldots, f_m)$$의 $R$-points는 정확히 ring $R$ 위에서 방정식들 $f_1 = \cdots = f_m = 0$을 만족시키는 해들의 집합과 일치한다.

<div class="proposition" markdown="1">

<ins id="prop11">**명제 11**</ins> Affine scheme $X = \Spec A$에 대해, 임의의 scheme $S = \Spec R$에 대한 $X$의 $S$-point 집합 $X(S)$는 ring homomorphism들의 집합 $$\Hom(A, R)$$과 자연스럽게 일치한다.

</div>

<details class="proof" markdown="1">

<summary>증명</summary>

Affine scheme 사이의 morphism $$\Spec R \to \Spec A$$는 ring homomorphism $A \to R$과 반대 방향으로 일대일 대응한다. 이는 affine scheme의 기본적인 성질이며, 따라서 $X(S) = \Hom(\Spec R, \Spec A) \cong \Hom(A, R)$가 성립한다.

</details>

Functor of points는 Yoneda lemma에 의해 scheme $X$ 자체를 완전히 결정짓는다. 즉, $X$와 $Y$가 동일한 functor of points를 가진다면, 이들은 isomorphic하다. 이는 scheme이 공간으로서의 구조보다는, 다른 대상들로부터 받아오는 사상들의 집합으로서 더 자연스럽게 이핼될 수 있음을 보여준다.

## Conclusion

우리는 classical algebraic variety가 가진 세 가지 본질적인 한계, 즉 generic point의 부재, nilpotent의 부재, 그리고 base field에 대한 강한 의존성을 살펴 보았다. 이러한 한계들은 모두 classical framework이 기하학적 대상을 단순한 점의 집합으로 본다는 관점에서 비롯되며, scheme theory는 바로 이 관점을 해체함으로써 더 넓은 세계를 열어준다. Affine variety는 $$\Spec$$을 통해, projective variety는 $$\Proj$$를 통해 자연스럽게 scheme으로 확장되며, classical variety는 reduced, irreducible, separated scheme of finite type으로 특징지어진다. Non-closed point와 nilpotent section의 도입은 기하학적 대상에 풍부한 계층적 구조를 부여하고, relative viewpoint와 functor of points는 기하학을 임의의 ring 위에서의 방정식의 해로 보는 보편적 관점을 제공한다.

이제 다음 글에서는 scheme theory의 가장 기본적인 building block인 <em-ko>spectrum</em-ko>, 즉 $$\Spec A$$의 정의와 성질을 본격적으로 전개할 것이다. $$\Spec A$$ 위의 Zariski topology와 structure sheaf를 구성하고, 이것이 어떻게 locally ringed space를 형성하는지를 살펴 봄으로써, scheme theory의 엄밀한 기초를 다질 것이다.

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic geometry*, Springer, 1977.

**[EH]** D. Eisenbud and J. Harris, *The Geometry of Schemes*, Springer, 2000.
