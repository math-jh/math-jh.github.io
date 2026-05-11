---
title: "교차곱"
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

[§저우 군](/ko/math/algebraic_varieties/chow_groups)에서 우리는 Chow group $$\CH^\ast(X)$$를 정의하였다. 우리는 해당 글의 말미에서 여기에 intersection product를 정의하여 ring구조를 줄 수 있다고 주장했었는데, 이번 글에서는 이를 정의하고 성질들을 살펴본다. 

다음 정의는 한 점 $$p$$ 근방에서 두 variety $$V,W$$의 intersection이 무엇인지 보여준다. 정의에 의해 이는 점 $$p$$ 근방에서 일어나는 일이므로, affine chart를 택한 후 ambient space를 $$\mathbb{A}^n$$으로 두고 정의해도 충분하다. 

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 아핀공간 $$\mathbb{A}^n$$의 점 $$p$$에서 두 variety $$V, W$$의 *intersection multiplicity<sub>교차 중복도</sub>* $$i_p(V, W)$$를 다음의 식

$$i_p(V, W) = \dim_{\mathbb{K}} \mathcal{O}_{\mathbb{A}^n, p} / (I(V) + I(W))$$

으로 정의한다. 

</div>

정의에 의해 $$V$$와 $$W$$는 점 $$p$$ 근방에서 $$I(V), I(W)$$의 원소들 각각의 공통 zero set으로 나타난다. 그럼 점 $$p$$가 이들 두 subvariety에 공통적으로 포함되기 위해서는 $$I(V)$$와 $$I(W)$$의 원소들 모두의 zero set으로 나타나야 하므로, 이를 위해 ideal sum $$I(V)+I(W)$$을 생각하게 된다. 일반적으로 ambient space에 비하여 $$V,W$$가 너무 작으면 이들은 일반적으로 만나지 않으므로 위의 식이 잘 정의되지 않는다. 즉, 우리는 $$\dim V+\dim W=n$$이 성립할 때만 위의 식을 사용한다. 일반적으로, 임의의 두 subvariety가 서로 만날 때 그 intersection의 예상 차원은 $$\dim V + \dim W -n$$이며, 이것이 점으로 나오기 위해서는 반드시 $$\dim V+\dim W=n$$이어야 함을 안다. 

일반적으로 이 정의는 local complete intersection의 경우에 적용되고, singular한 상황에서는 다음의 *Tor formula*

$$i_p(V, W) = \sum_{i \ge 0} (-1)^i \dim_{\mathbb{K}} \Tor_i^{R}\bigl(R/I(V),\ R/I(W)\bigr)$$

가 이를 정의해준다. 위의 식은 $$i = 0$$ 항에 해당한다. 이 글에서 우리는 단순한 경우만 살펴보므로 위의 [정의 1](#def1)로 충분하다. 

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins> $$\mathbb{A}^2$$에서 $$V=\{ \y = 0\}$$과 $$W=\{\y = \x^2\}$$가 원점에서 만난다. 각 곡선을 정의하는 ideal은 $$I(V) = (\y)$$, $$I(W) = (\y - \x^2)$$이다. 정의를 따라 원점에서의 local ring에 대한 quotient를 계산하면 

$$\mathcal{O}_{\mathbb{A}^2, 0} / (\y, \y - \x^2) = \mathcal{O}_{\mathbb{A}^2, 0} / (\y, \x^2)$$

이며, 이 quotient는 basis $$\{1, \x\}$$를 갖는 2차원 $$\mathbb{K}$$-vector space이다. 따라서 $$i_0(V, W) = 2$$이다. 이는 곡선 $$W$$가 $$V$$ 위에서 $$\x=0$$에서 order 2로 접한다는 사실과 일치한다. 더 일반적으로 $$V=\{ \y = 0\}$$과 $$W=\{\y = \x^n\}$$에 대하여 $$i_0(V, W) = n$$이다.

</div>

위의 경우는 $$2$$차원에서 두 $$1$$차원 subvariety가 만나는 예시로, 우리는 이미 [§곡면에서의 리만-로흐 정리, ⁋정의 1](/ko/math/algebraic_varieties/riemann_roch_surfaces#def1)에서 이를 간략하게 소개한 바 있다. 해당 글에서 우리는 transversal intersection의 개념을 소개했는데, 이를 공식적으로 정의하자.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> 두 variety $$V, W \subseteq \mathbb{A}^n$$이 점 $$p \in V \cap W$$에서 *transversely intersect*한다는 것은 tangent space의 합이 전체 공간을 채우는 것이다.

</div>

그럼 다음 두 명제는 [§곡면에서의 리만-로흐 정리, ⁋명제 2](/ko/math/algebraic_varieties/riemann_roch_surfaces#prop2)의 자연스러운 일반화이다. 

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> Intersection multiplicity는 다음의 조건을 만족한다. 

1. 임의의 $$p$$와 $$V,W$$에 대하여, $$0\leq i_p(V,W)<\infty$$가 항상 성립하며, $$i_p(V,W)=0$$은 $$p\not\in V\cap W$$일 때 성립한다.
2. $$V,W$$가 $$p$$에서 transversally intersect하는 것은 $$i_p(V,W)=1$$인 것과 동치이다. 
3. $$i_p$$는 [§곡면에서의 리만-로흐 정리, ⁋명제 2](/ko/math/algebraic_varieties/riemann_roch_surfaces#prop2)의 모든 조건을 만족한다. 

</div>

## Intersection Product의 정의

지금까지의 정의는 엄밀히 말하면 Chow group에서의 intersection product의 모든 성질을 사용할 수 있도록 하는 것은 아니다. 가령 $$3$$차원 공간에서 두 평면은 일반적으로 한 직선에서 만나겠지만 우리는 두 부분공간의 교집합이 $$0$$차원인 경우만 다루고 있으므로 이를 설명할 수 없다. 따라서 다음을 우선 정의한다. 

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> Variety $$X$$의 두 subvariety $$V,W$$에 대하여, 다음 식

$$\codim(V \cap W) = \codim V + \codim W$$

이 성립한다면 $$V,W$$가 *properly intersect*한다고 말한다.

</div>

특히 [정의 1](#def1)은 $$\codim (V\cap W)=n$$인 특수한 경우이다. 이제 우리는 만일 위의 등식이 $$V,W$$의 모든 component에 대해 성립한다면 이를 사용하여 다음의 식

$$V \cdot W = \sum_{T \subseteq V \cap W} i_T(V, W) \, [T]$$

으로 정의할 수 있다. 여기서 $$i_T(V, W)$$는 component $$T$$에서의 intersection multiplicity로, [정의 1](#def1)의 점에서의 multiplicity를 component $$T$$로 자연스럽게 확장한 값이다. $$T$$가 점 $$p$$라면 $$i_T(V, W) = i_p(V, W)$$이고, 일반적으로는 $$T$$ 위의 일반적인 점에서 두 variety가 만나는 정도를 측정한 값으로, generic point에서의 intersection multiplicity로 엄밀하게 정의할 수 있다. 그럼 다음은 intersection multiplicity의 성질들을 intersection product로 올려둔 것이다. 

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> Smooth irreducible variety $$X$$ 위에서 codimension $$k$$, $$l$$의 두 cycle $$Z, W$$에 대하여, 위의 식으로부터 *intersection product* 

$$Z \cdot W \in \CH^{k+l}(X)$$

가 잘 정의된다. 뿐만 아니라, 이는 다음의 성질들을 만족한다. 

를 정의할 수 있다. 

1. *Symmetry.* $$Z \cdot W = W \cdot Z$$가 성립한다.
2. *Bilinearity.* $$(aZ_1 + bZ_2) \cdot W = a(Z_1 \cdot W) + b(Z_2 \cdot W)$$가 성립한다. 
3. *Associativity*. $$(Z_1 \cdot Z_2) \cdot Z_3 = Z_1 \cdot (Z_2 \cdot Z_3)$$가 성립한다. 

</div>

그럼 다음 정의는 앞선 글에서부터 예견되었던 것이다. 

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> Intersection product에 의해 $$\CH^\ast(X) = \bigoplus_k \CH^k(X)$$는 *graded ring*이 된다. 이를 *Chow ring*이라 부른다.

</div>

## Moving Lemma

이제 우리의 유일한 문제는 임의의 두 class가 주어졌을 때, 이들이 차원 조건을 만족한다 해도 두 cycle이 실제로 좋게 만나는지는 알 수 없다. 가령 현재 상태에서 우리는 특정한 class의 self-intersection을 정의할 수 없다. 이를 위해서는 더 일반적으로, 임의의 두 cycle이 주어졌을 때 하나를 rational equivalence 안에서 이동시켜 $$W$$와 properly intersect하도록 해 주어야 한다. 이를 보장하는 정리가 다음의 *moving lemma*이다.

<div class="proposition" markdown="1">

<ins id="lem8">**보조정리 8 (Moving Lemma)**</ins> Smooth quasi-projective variety $$X$$와 cycle $$Z \in \CH^k(X)$$, 그리고 임의의 cycle $$W \in \CH^l(X)$$에 대해, $$Z' \sim_{\text{rat}} Z$$이고 $$Z'$$과 $$W$$가 properly intersect하는 $$Z'$$가 존재한다.

</div>

핵심 아이디어는 다음과 같다. $$Z$$를 구성하는 irreducible component $$V_i$$마다, $$V_i$$를 포함하는 충분히 "일반적인" hypersurface $$H_i$$로 자르고, $$V_i \cap H_1 \cap \cdots \cap H_s$$와 같은 형태의 cycle을 취한다. 이때 "일반적"이라는 것은 $$H_i$$가 $$W$$와 generic한 위치에서 만나도록 선택한다는 것으로, 이렇게 하면 차원이 적절히 떨어져 proper intersection을 이룬다. ([§선형계, ⁋정의 5](/ko/math/algebraic_varieties/linear_systems#def5))에서 보았듯 basepoint-free linear system을 사용하면 이러한 "일반적인" 이동을 regular map으로 실현할 수 있으며, 이 과정이 rational equivalence를 보존함을 보이는 것이 증명의 핵심이다.

그럼 우리는 위의 보조정리를 사용하여 $$Z$$를 $$Z'$$로 옮겨준 후, 다음의 식

$$Z \cdot W := Z' \cdot W = \sum_{T \subset Z' \cap W} i_T(Z', W) [T]$$

으로 intersection을 정의한다. 

## Deformation to Normal Cone

Moving lemma는 두 class가 주어졌을 때, 이를 perturb하여 intersection을 계산한다는 점에서 우리의 직관을 현실화한다. 그러나 이 접근은 quasi-projectivity라는 가정에 의존하며, 이를 일반적인 세팅으로 확장하기 위해서는 *deformation to normal cone*을 해야 한다. 

핵심적인 관찰은 다음과 같다. 우선 [§접공간과 매끄러움, ⁋정의 13](/ko/math/algebraic_varieties/tangent_spaces_and_smoothness#def9)에서 tangent cone을 정의했던 것을 기억하자. 이는 singular point에서의 국소적 구조를 이해하는 도구였으며, 이를 일반화하여 우리는 closed embedding $$i: Y \hookrightarrow X$$에 대해 $$Y$$의 $$X$$ 안에서의 *normal cone* $$C_{Y/X}$$를 정의할 수 있다. 만일 $$X$$가 $$Y$$를 따라 smooth하다면 normal cone은 normal bundle $$N_{Y/X}$$가 되지만, 일반적으로는 cone 구조를 가진다.

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9 (Deformation to Normal Cone)**</ins> Closed embedding $$i: Y \hookrightarrow X$$에 대해, $$\mathbb{A}^1$$을 매개변수로 하는 family $$M \to \mathbb{A}^1$$을 구성할 수 있다. 구체적으로, $$t \neq 0$$에서의 fiber $$M_t$$는 $$X$$ 자신이며, $$t = 0$$에서의 fiber $$M_0$$는 normal cone $$C_{Y/X}$$이다. 이 family의 존재는 intersection product의 well-definedness를 이 family에 대한 pushforward/pullback의 호환성으로 환원시킨다.

</div>

<details class="proof" markdown="1">
<summary>증명 (스케치)</summary>

구성은 blow-up을 사용한다. 먼저 $$X \times \mathbb{A}^1$$ 안에서 $$Y \times \{0\}$$를 따라 blow-up하여 $$\widetilde{M} = \Bl_{Y \times \{0\}}(X \times \mathbb{A}^1)$$을 얻고, 그 후 $$X \times \{0\}$$의 proper transform을 제거하여 $$M = \widetilde{M} \setminus \widetilde{X \times \{0\}}$$로 정의한다. 이 blow-up의 exceptional divisor는 $$\mathbb{P}(C_{Y/X} \oplus \mathcal{O}_Y)$$이며, proper transform을 제거하면 $$t=0$$ fiber에서 정확히 normal cone $$C_{Y/X}$$가 남는다. $$t \neq 0$$에서는 blow-up이 isomorphism이므로 fiber가 $$X$$ 그대로이다. 따라서 $$M \to \mathbb{A}^1$$은 $$t=1$$에서의 $$X$$를 $$t=0$$에서의 $$C_{Y/X}$$로 연결하는 deformation을 제공한다. Chow group에서 $$M$$ 위의 specialization map $$\sigma: \CH^\ast(X) \to \CH^\ast(C_{Y/X})$$을 정의할 수 있고, normal cone이 vector bundle 구조를 가질 때 (즉 regular embedding의 경우) Thom isomorphism에 의해 $$\CH^\ast(C_{Y/X}) \cong \CH^\ast(Y)$$가 되어 intersection product의 well-definedness가 확립된다.

</details>

이 방법의 아이디어는 $$X$$를 연속적으로 변형하여 $$Y$$의 normal cone으로 수축시키는 것이다. 기하적으로, $$t=1$$에서는 원래 공간 $$X$$를 보고, $$t$$가 $$0$$으로 갈수록 $$X$$가 $$Y$$를 따라 점점 더 "펴지면서" 결국 $$t=0$$에서는 $$Y$$를 따라 벌어진 normal cone이 된다. ([§유리사상, ⁋예시 8](/ko/math/algebraic_varieties/rational_maps#ex8))의 blow-up이 한 점을 $$\mathbb{P}^1$$로 펼쳐 놓는 변형이었다면, deformation to normal cone은 이를 더 일반적인 embedding에 대해 수행하는 것이다.

## 예시들

Intersection product의 성질을 구체적인 예시들을 통해 확인해 보자.

<div class="example" markdown="1">

<ins id="ex10">**예시 10 ($$\mathbb{P}^n$$)**</ins> $$\CH^\ast(\mathbb{P}^n) \cong \mathbb{Z}[H] / (H^{n+1})$$이다. 여기서 $$H = [\text{hyperplane}] \in \CH^1(\mathbb{P}^n)$$로, $$H^k$$는 $$k$$-codimensional linear subspace의 class와 같다. Degree $$d$$ hypersurface $$V(f)$$에 대해서는 $$[V(f)] = dH$$이다. 이 결과는 ([§인자, ⁋예시 11](/ko/math/algebraic_varieties/divisors#ex7))에서 $$\Cl(\mathbb{P}^n) \cong \mathbb{Z}$$임을 이미 보였으므로 자연스러운 것이다. Picard group $$\Pic(\mathbb{P}^n) \cong \CH^1(\mathbb{P}^n) \cong \mathbb{Z}$$에 intersection product를 더하면, $$H \cdot H = H^2$$, $$H \cdot H^2 = H^3$$, ...의 곱셈이 추가되어 Chow ring이 완성된다.

$$H^k$$는 $$k$$-codimensional linear subspace의 class와 같다. Degree $$d$$ hypersurface $$V(f)$$에 대해서는 $$[V(f)] = dH$$이다. 이 결과는 ([§인자, ⁋예시 11](/ko/math/algebraic_varieties/divisors#ex7))에서 $$\Cl(\mathbb{P}^n) \cong \mathbb{Z}$$임을 이미 보였으므로 자연스러운 것이다. Picard group $$\Pic(\mathbb{P}^n) \cong \CH^1(\mathbb{P}^n) \cong \mathbb{Z}$$에 intersection product를 더하면, $$H \cdot H = H^2$$, $$H \cdot H^2 = H^3$$, ...의 곱셈이 추가되어 Chow ring이 완성된다.

</div>

<div class="example" markdown="1">

<ins id="ex11">**예시 11 (Surface)**</ins> Surface $$S$$ 위의 두 curve $$C, D$$에 대해:

$$[C] \cdot [D] = \sum_{p \in C \cap D} i_p(C, D) [p] \in \CH^2(S)$$

이다. 일반적인 surface의 경우 $$\CH^2(S)$$의 구조는 단순하지 않다. Zero-cycles modulo rational equivalence는 degree map $$\deg: \CH^2(S) \to \mathbb{Z}$$에 의해 $$\mathbb{Z}$$으로 가는 surjection을 갖지만, 그 kernel은 일반적으로 비자명이다. 가령 $$p_g(S) > 0$$인 surface에서는 Mumford의 정리에 의해 $$\CH^2(S)$$가 "infinite dimensional"이 된다. 따라서 교차 수 $$C \cdot D = \sum_{p \in C \cap D} i_p(C, D)$$는 degree map의 image로서 정수값을 얻지만, $$\CH^2(S)$$ 자체는 $$\mathbb{Z}$$이 아닐 수 있다.

그러나 $$\mathbb{P}^2$$에서는 상황이 단순하다. $$\CH^\ast(\mathbb{P}^2) = \mathbb{Z}[H]/(H^3)$$이므로 $$\CH^2(\mathbb{P}^2) \cong \mathbb{Z}$$이고, 교차 수가 완전히 결정된다. Chow ring에서 conic의 class는 $$[X] = 2H$$이고 직선의 class는 $$[L] = H$$이므로, $$[X] \cdot [L] = 2H \cdot H = 2H^2 = 2[\text{point}]$$이다.

</div>

<div class="example" markdown="1">

<ins id="ex12">**예시 12 ($$\mathbb{P}^1 \times \mathbb{P}^1$$)**</ins> ([§유리사상, ⁋예시 11](/ko/math/algebraic_varieties/rational_maps#ex7))에서 $$\mathbb{P}^1 \times \mathbb{P}^1$$과 quadric surface $$Q = V(\x\y - \z\w)$$가 birationally equivalent (실은 isomorphic)임을 보았다. $$\mathbb{P}^1 \times \mathbb{P}^1$$의 Chow ring은

$$\CH^\ast(\mathbb{P}^1 \times \mathbb{P}^1) \cong \mathbb{Z}[H_1, H_2] / (H_1^2, H_2^2)$$

이다. 여기서 $$H_1 = [\mathbb{P}^1 \times \{p\}]$$, $$H_2 = [\{p\} \times \mathbb{P}^1]$$이다. Bidegree $$(a, b)$$의 curve $$C$$에 대해 $$[C] = aH_1 + bH_2$$이며, 따라서 두 curve $$C = aH_1 + bH_2$$, $$C' = a'H_1 + b'H_2$$의 교차 수는

$$C \cdot C' = (aH_1 + bH_2)(a'H_1 + b'H_2) = ab' H_1 H_2 + a'b H_1 H_2 = (ab' + a'b) H_1 H_2$$

으로 계산된다. $$H_1 H_2 = [\text{point}]$$이므로 교차 수는 $$ab' + a'b$$이다. 이는 곡선의 bidegree로부터 교차 수를 직접 계산할 수 있음을 보여준다.

</div>

<div class="example" markdown="1">

<ins id="ex13">**예시 13 (Segre embedding과 교차)**</ins> ([§사영다양체, ⁋예시 16](/ko/math/algebraic_varieties/projective_varieties#ex8))의 Segre embedding $$\sigma: \mathbb{P}^1 \times \mathbb{P}^1 \to \mathbb{P}^3$$를 생각하자. 이 embedding의 image는 quadric surface $$Q = V(\x_0\x_3 - \x_1\x_2)$$이다. ([§선다발과 벡터다발, ⁋명제 20](/ko/math/algebraic_varieties/line_bundles#prop16))에 의해 pullback $$\sigma^\ast \mathcal{O}_{\mathbb{P}^3}(1)$$은 $$\mathbb{P}^1 \times \mathbb{P}^1$$ 위의 line bundle이며, 실제로 $$\sigma^\ast \mathcal{O}_{\mathbb{P}^3}(1) \cong \mathcal{O}_{\mathbb{P}^1 \times \mathbb{P}^1}(1,1)$$이다. 이는 Chow ring 수준에서도 확인할 수 있다. $$\mathbb{P}^3$$에서 hyperplane class $$H_{\mathbb{P}^3}$$를 pullback하면 $$H_1 + H_2$$를 얻고, 이는 bidegree $$(1,1)$$에 해당한다.

이를 통해 $$\mathbb{P}^3$$에서의 교차 계산을 $$\mathbb{P}^1 \times \mathbb{P}^1$$으로 옮겨 수행할 수 있다. 가령 $$\mathbb{P}^3$$에서 두 개의 hyperplane section $$H_1 \cap H_2 \cap Q$$의 교차는, $$\mathbb{P}^1 \times \mathbb{P}^1$$에서 $$(H_1 + H_2)^2 = 2H_1 H_2$$로 계산된다. 즉, 두 hyperplane과 quadric surface의 교차는 $$2$$개의 점으로, 이는 $$Q \cong \mathbb{P}^1 \times \mathbb{P}^1$$에서 두 개의 bidegree $$(1,1)$$ curve가 만나는 것과 같다.

</div>

## 선다발과의 교차

<div class="proposition" markdown="1">

<ins id="prop14">**명제 14**</ins> Line bundle $$L$$과 cycle $$Z \in \CH_k(X)$$에 대해 $$c_1(L) \cap Z \in \CH_{k-1}(X)$$가 well-defined되어 있다. 여기서 **first Chern class** $$c_1(L) \in \CH^1(X)$$는 line bundle $$L$$에 대응하는 divisor class이며, $$L$$이 Cartier divisor $$D$$에 의해 주어지면 $$c_1(L) = [D] \in \CH^1(X)$$이다. 이 대응은 ([§인자](/ko/math/algebraic_varieties/divisors))와 ([§선다발과 벡터다발](/ko/math/algebraic_varieties/line_bundles))에서 다룬 Cartier divisor와 line bundle 사이의 동치관계에 근거한다. 구체적으로 $$L = \mathcal{O}(D)$$, $$D = \sum n_i V_i$$일 때 $$D$$와 $$Z$$가 properly intersect하면 $$c_1(L) \cap Z = \sum n_i \cdot (V_i \cdot Z)$$로 정의되며, proper intersection이 아닌 경우 moving lemma나 deformation to normal cone을 사용한다.

</div>

<details class="proof" markdown="1">
<summary>증명 (스케치)</summary>

Well-definedness의 핵심은 $$c_1(L) \cap Z$$가 $$L$$의 rational section의 선택에 의존하지 않는다는 것이다. $$L$$의 두 rational section $$s_1, s_2$$를 생각하면 $$\divisor(s_1) - \divisor(s_2) = \divisor(s_1/s_2)$$이고, $$s_1/s_2 \in \mathbb{K}(X)^\ast$$는 rational function이다. 따라서 $$[\divisor(s_1)] - [\divisor(s_2)] = 0 \in \CH^1(X)$$이며, 이는 $$c_1(L)$$가 divisor의 선택과 무관함을 보인다. Cap product의 호환성, 즉 $$c_1(L_1 \otimes L_2) = c_1(L_1) + c_1(L_2)$$는 tensor product에 대응하는 divisor의 덧셈으로부터 바로 따른다.

</details>

<div class="proposition" markdown="1">

<ins id="prop15">**명제 15**</ins> $$L = \mathcal{O}(D)$$이면:

$$c_1(L) \cap [X] = [D] \in \CH^1(X)$$

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$c_1(L)$$의 정의에 의해, $$L = \mathcal{O}(D)$$에 대해 $$c_1(L) = [D] \in \CH^1(X)$$이다. 기본 class $$[X] \in \CH^0(X)$$에 대한 cap product $$c_1(L) \cap [X]$$는 intersection product $$[D] \cdot [X]$$와 같다. $$[X] \in \CH^0(X)$$가 항등원이므로 $$[D] \cdot [X] = [D]$$이다.

</details>

## 사상 공식

<div class="proposition" markdown="1">

<ins id="prop16">**명제 16 (Projection Formula)**</ins> Proper morphism $$f: X \to Y$$와 $$\alpha \in \CH^\ast(X)$$, $$\beta \in \CH^\ast(Y)$$에 대해 $$f_\ast(\alpha \cdot f^\ast \beta) = f_\ast(\alpha) \cdot \beta$$가 성립한다.

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
