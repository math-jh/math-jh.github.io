---
title: "선형계"
excerpt: "Complete linear systems, base loci, and ampleness"

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/linear_systems
sidebar:
    nav: "algebraic_geometry-ko"

header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Linear_Systems.png
    overlay_filter: 0.5

date: 2026-03-15
last_modified_at: 2026-03-15
weight: 10

published: false
---

앞서 우리는 [§인자, ⁋정의 1](/ko/math/algebraic_geometry/divisors#def1)에서 variety $$X$$의 (Weil) divisor를 정의하였다. Zariski topology의 정의에 의하여, 이는 기본적으로 $$X$$ 위에 정의된 어떤 <em-ko>함수</em-ko>의 zero set에, 이 zero의 order를 더한 것으로 생각할 수 있으며, 이를 $$\mathbb{P}^n$$과 같은 경우에도 잘 정의하기 위해 우리는 <em-ko>함수</em-ko>를 <em-ko>적당한 line bundle의 section</em-ko>으로 일반화했다. 

한편, divisor는 음수 계수 또한 허용하므로 이 zero set은 zero set이 아니라, 음수 order의 zero, 즉 pole이 될 수도 있다. 이런 경우 우리는 주어진 divisor와 linearly equivalent한 *effective* divisor를 찾은 후, 이 성질을 탐구할 수 있다. ([§인자, ⁋정의 7](/ko/math/algebraic_geometry/divisors#def7)) 

위에서 우리는 서술의 편의상 Weil divisor에 대한 논의만 하였지만, Cartier divisor에 대해서도 비슷한 논증을 할 수 있으며, 그 결과로 나오는 정의는 다음과 같다. 

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Variety $$X$$ 위에 정의된 Weil divisor $$D=\sum n_i D_i$$가 *effective*라는 것은 모든 $$i$$에 대해 $$n_i\geq 0$$인 것이다. Cartier divisor $$\{(U_i, f_i)\}$$가 *effective*라는 것은 모든 $$i$$에 대해 $$f_i$$가 $$U_i$$ 위에서 regular인 것이다. 

</div>

그렇다면 우리의 목적은 divisor $$D$$의 divisor class 안에서 어떠한 effective divisor가 존재하는지 살펴보는 것이다. 이를 위해 divisor $$D$$가 정의하는 line bundle $$\mathcal{L}=\mathcal{O}_X(D)$$를 생각하자. ([§선다발과 벡터다발, ⁋정의 17](/ko/math/algebraic_geometry/line_bundles#def17)) 우리는 $$\mathcal{L}$$의 각각의 nonzero global section $$s\in H^0(X, \mathcal{L})$$는 pole이 없으므로 effective divisor $$\divisor(s)$$를 정의하며, 이는 원래의 $$D$$와 trivialization만큼만 차이나는 것을 확인할 수 있으므로 $$D$$와 linearly equivalent하다. 즉 $$D$$와 linearly equivalent한 effective divisor를 찾기 위해선 $$\mathcal{O}_X(D)$$의 nonzero global section을 보면 된다. 다만 주의할 사항은 $$\divisor(s)$$는 $$s$$ 자체가 아니라 $$s$$의 nonzero multiple에 의존한다는 것으로, 이때문에 우리가 관심을 가져야할 대상은 $$H^0(X, \mathcal{L})$$ 자체가 아니라 그 projectivization이다. 

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> Variety $$X$$ 위의 line bundle $$\mathcal{L}$$에 대하여, $$\mathcal{L}$$의 *complete linear system*은 $$\mathcal{L}$$의 global section space $$H^0(X, \mathcal{L})$$의 projectivization

$$\lvert \mathcal{L} \rvert = \mathbb{P}(H^0(X, \mathcal{L}))$$

이다. $$\mathcal{L}$$에 대한 *linear system*은 $$\lvert \mathcal{L} \rvert$$의 nonempty projective subspace이다. 즉, 부분벡터공간 $$V \subseteq H^0(X, \mathcal{L})$$에 대해 $$\mathbb{P}(V) \subseteq \lvert \mathcal{L} \rvert$$의 꼴이다.

</div>


## Projective space의 complete linear system

앞서 [§선다발과 벡터다발, ⁋예시 12](/ko/math/algebraic_geometry/line_bundles#ex12) 이후의 계산에 의해 $$H^0(\mathbb{P}^n, \mathcal{O}_{\mathbb{P}^n}(d))$$가 차수 $$d$$의 동차다항식들의 공간 $$\mathbb{K}[\x_0, \ldots, \x_n]_d$$와 동형임을 보았다. 이 



따라서 ([§선다발과 벡터다발, ⁋명제 19](/ko/math/algebraic_geometry/line_bundles#prop19))의 맥락에서, divisor $$dH$$에 대응하는 line bundle $$\mathcal{O}_{\mathbb{P}^n}(d)$$의 complete linear system은 다음과 같다.

$$\lvert \mathcal{O}_{\mathbb{P}^n}(d) \rvert = \mathbb{P}(H^0(\mathbb{P}^n, \mathcal{O}_{\mathbb{P}^n}(d))) \cong \mathbb{P}(\mathbb{K}[\x_0, \ldots, \x_n]_d) \cong \mathbb{P}^{\binom{n+d}{d} - 1}$$

이것은 "차수 $$d$$의 hypersurface들의 family"의 정확한 정의이다. ([§사영다양체](/ko/math/algebraic_geometry/projective_varieties))에서 보았듯, $$\mathbb{P}^n$$의 Zariski topology는 homogeneous polynomial의 zero set으로 정의되며, $$\mathbb{K}[\x_0, \ldots, \x_n]_d$$는 차수 $$d$$의 homogeneous polynomial들의 $$\mathbb{K}$$-벡터공간이다. $$\mathbb{P}^n$$에서 차수 $$d$$의 hypersurface는 원소 $$F \in \mathbb{K}[\x_0, \ldots, \x_n]_d \setminus \{0\}$$의 zero set $$Z(F)$$로 나타내어진다.

이제 우리는 다음 관찰을 한다. 스칼라 $$\lambda \in \mathbb{K}^\ast$$에 대해 $$Z(\lambda F) = Z(F)$$. 즉, nonzero scalar multiple들은 같은 hypersurface를 정의한다. 따라서 "차수 $$d$$의 hypersurface"들은 projective space $$\mathbb{P}(\mathbb{K}[\x_0, \ldots, \x_n]_d)$$의 한 점으로 나타내어진다. $$\dim \mathbb{K}[\x_0, \ldots, \x_n]_d = \binom{n+d}{d}$$이므로, 이 projective space의 차원은 $$\binom{n+d}{d} - 1$$이다.

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> **$$\mathbb{P}^2$$의 직선 family**: $$n = 2$$, $$d = 1$$인 경우, $$\mathbb{K}[\x_0, \x_1, \x_2]_1$$의 기저는 $$\{\x_0, \x_1, \x_2\}$$이다. 따라서 차수 1의 hypersurface (직선)들의 family는 $$\mathbb{P}^2$$와 동형이다. 한 점 $$[a_0 : a_1 : a_2] \in \mathbb{P}^2$$는 직선 $$Z(a_0 \x_0 + a_1 \x_1 + a_2 \x_2)$$에 대응된다.

</div>

## Linear System의 구체적 예시

<div class="example" markdown="1">

<ins id="ex4">**예시 4**</ins> **$$\mathbb{P}^2$$의 conic pencil**: 두 conic $$C_1 = Z(F_1)$$, $$C_2 = Z(F_2)$$의 *pencil*은

$$\{Z(\lambda F_1 + \mu F_2)\}_{[\lambda:\mu] \in \mathbb{P}^1}$$

이다. 이는 $$\lvert \mathcal{O}_{\mathbb{P}^2}(2) \rvert$$의 1차원 subspace이다. Pencil의 각 원소는 차수 2의 plane curve이며, 이들은 모두 $$C_1 \cap C_2$$를 지난다. $$\dim \mathbb{K}[\x_0, \x_1, \x_2]_2 = 6$$이므로 $$\lvert \mathcal{O}_{\mathbb{P}^2}(2) \rvert \cong \mathbb{P}^5$$이고, pencil은 이 $$\mathbb{P}^5$$의 1차원 부분공간이다.

</div>

## Quasiprojective Variety 위의 Linear System

이제 quasiprojective variety $$X \subseteq \mathbb{P}^n$$ 위에서의 linear system을 정의한다. $$\mathbb{P}^n$$의 linear system $$\mathbb{P}(V)$$에 대해, 각 $$F \in V$$는 $$X$$와의 교차 $$X \cap Z(F)$$를 정의한다. 이것이 $$X$$ 위의 linear system의 기하학적 내용이다.

Quasiprojective variety $$X \subseteq \mathbb{P}^n$$ 위에서, 부분벡터공간 $$V \subseteq \mathbb{K}[\x_0, \ldots, \x_n]_d$$가 정의하는 *linear system*은 [정의 2](#def2)의 특수한 경우로, $$\mathbb{P}(V)$$의 각 원소 $$[F]$$가 $$X$$ 위의 교차 $$X \cap Z(F)$$에 대응되는 family이다.

이때 $$X$$ 위에서 두 다항식 $$F, G$$가 같은 교차를 정의하는 것은 $$F \equiv G \pmod{I(X)}$$일 때, 즉 $$F - G$$가 $$X$$의 defining ideal $$I(X)$$에 속할 때이다. 따라서 $$X$$ 위에서의 실제 parameter space는 $$\mathbb{P}(V / (V \cap I(X)))$$이다.

<div class="example" markdown="1">

<ins id="ex5">**예시 5**</ins> **$$\mathbb{P}^1$$ 위의 점들의 family**: $$\mathbb{P}^1$$에서 차수 1의 hypersurface는 점 한 개이다. $$\mathbb{K}[\x_0, \x_1]_1$$의 기저는 $$\{\x_0, \x_1\}$$이고, $$\lvert \mathcal{O}_{\mathbb{P}^1}(1) \rvert \cong \mathbb{P}^1$$이다. 한 점 $$[a : b] \in \mathbb{P}^1$$은 $$\mathbb{P}^1$$의 점 $$Z(a \x_0 + b \x_1) = [b : -a]$$에 대응된다.

</div>

## Base Locus

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> Linear system $$L \subseteq \lvert \mathcal{L} \rvert$$의 *base locus* $$\operatorname{Bs}(L)$$는 $$L$$의 모든 원소가 공유하는 closed subset이다. 구체적으로, $$L = \mathbb{P}(V)$$에서 $$V \subseteq H^0(X, \mathcal{L})$$일 때,

$$\operatorname{Bs}(L) = \bigcap_{s \in V \setminus \{0\}} \operatorname{Supp}(\operatorname{div}(s))$$

여기서 $$\operatorname{div}(s)$$는 section $$s$$의 zero divisor이다. $$\mathbb{P}^n$$의 hypersurface 계산에서는 $$V \subseteq \mathbb{K}[\x_0, \ldots, \x_n]_d$$에 대해 $$\operatorname{Bs}(L) = \bigcap_{[F] \in L} Z(F)$$와 동일하다.

</div>

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> $$L$$이 *basepoint-free*라는 것은 $$\operatorname{Bs}(L) = \emptyset$$인 것이다. 즉, 임의의 점 $$p \in X$$에서 $$p$$를 지나지 않는 $$L$$의 원소가 항상 존재한다.

</div>

<div class="example" markdown="1">

<ins id="ex8">**예시 8**</ins> **$$\mathbb{P}^n$$의 hyperplane system**: $$\lvert \mathcal{O}_{\mathbb{P}^n}(1) \rvert = \mathbb{P}(\mathbb{K}[\x_0, \ldots, \x_n]_1)$$는 basepoint-free이다. 임의의 점 $$p = [p_0 : \cdots : p_n] \in \mathbb{P}^n$$에 대해, $$p$$를 지나지 않는 hyperplane $$Z(\x_i)$$ (단, $$p_i \ne 0$$인 $$i$$를 택함)이 존재하기 때문이다. 즉, $$p \notin \operatorname{Bs}(\lvert \mathcal{O}_{\mathbb{P}^n}(1) \rvert)$$이다.

</div>

<div class="example" markdown="1">

<ins id="ex9">**예시 9**</ins> **Pencil의 base locus**: [예시 4](#ex4)의 conic pencil의 base locus는 $$C_1 \cap C_2$$이다. Bézout's theorem ([§Bézout 정리](/ko/math/algebraic_geometry/bezout_theorem))에 의해, $$\mathbb{P}^2$$에서 두 conic의 교차는 (중복도를 포함하여) 4개의 점으로 구성된다.

</div>

## Basepoint-Free Linear System이 정의하는 사상

Basepoint-free linear system의 핵심 성질은, 이것이 다양체에서 사영공간으로의 사상을 자연스럽게 정의한다는 것이다.

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10**</ins> Quasiprojective variety $$X \subseteq \mathbb{P}^n$$ 위의 basepoint-free linear system $$L = \mathbb{P}(V)$$에서, $$V$$의 기저 $$F_0, \ldots, F_r \in \mathbb{K}[\x_0, \ldots, \x_n]_d$$가 다음 조건을 만족한다고 하자:

$$\bigcap_{i=0}^r Z(F_i) \cap X = \emptyset$$

그러면 $$V$$는 $$X$$에서 사영공간으로의 정칙사상

$$\varphi_L: X \to \mathbb{P}^r, \quad p \mapsto [F_0(p) : \cdots : F_r(p)]$$

을 정의한다. 여기서 $$F_i(p)$$는 $$F_i$$의 $$p$$에서의 값을 나타낸다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

우선 $$\varphi_L$$이 well-defined임을 보여야 한다. $$p \in X$$일 때, $$p \in \operatorname{Bs}(L) = \emptyset$$이므로 어떤 $$i$$에 대해 $$F_i(p) \ne 0$$이다. 따라서 $$[F_0(p) : \cdots : F_r(p)]$$는 $$\mathbb{P}^r$$의 정상적인 점이다.

다음으로 $$\varphi_L$$이 정칙사상임을 보이자. $$X$$의 affine open cover $$U_\alpha = X \cap (\mathbb{P}^n \setminus Z(\x_\alpha))$$를 생각하자. 여기서 $$\x_\alpha$$는 $$\mathbb{P}^n$$의 standard homogeneous coordinate이다. 각 $$U_\alpha$$에서 $$\x_\alpha \ne 0$$이므로, $$F_i / \x_\alpha^d$$는 $$U_\alpha$$에서 정의되는 regular function이다. $$\varphi_L$$의 $$j$$번째 좌표는 이 regular function들의 비율로 나타나므로, $$\varphi_L$$은 $$U_\alpha$$에서 정칙사상이다.

</details>

<div class="example" markdown="1">

<ins id="ex11">**예시 11**</ins> **Rational normal curve**: $$\mathbb{P}^1$$에서 $$d \ge 1$$일 때, $$\lvert \mathcal{O}_{\mathbb{P}^1}(d) \rvert$$의 complete linear system이 정의하는 사상은 *Veronese 사상* 또는 *rational normal curve*이라 불린다.

$$\nu_d: \mathbb{P}^1 \to \mathbb{P}^d, \quad [s : t] \mapsto [s^d : s^{d-1}t : \cdots : t^d]$$

이 사상의 image는 $$\mathbb{P}^d$$에서 degree $$d$$의 *rational normal curve*이다. $$d = 2$$일 때는 $$\mathbb{P}^2$$의 conic, $$d = 3$$일 때는 $$\mathbb{P}^3$$의 twisted cubic이다.

</div>

## Very Ample과 Ample

<div class="definition" markdown="1">

<ins id="def12">**정의 12**</ins> Line bundle $$\mathcal{L}$$ (또는 대응하는 linear system $$\lvert \mathcal{L} \rvert$$)이 *very ample*이라는 것은, complete linear system $$\lvert \mathcal{L} \rvert = \mathbb{P}(H^0(X, \mathcal{L}))$$이 정의하는 사상 $$\varphi_{\mathcal{L}}: X \to \mathbb{P}(H^0(X, \mathcal{L}))$$이 closed embedding인 것이다.

</div>

<div class="definition" markdown="1">

<ins id="def13">**정의 13**</ins> $$\mathcal{L}$$이 *ample*이라는 것은 어떤 $$m > 0$$에 대해 $$\mathcal{L}^{\otimes m}$$이 very ample인 것이다.

</div>

<div class="proposition" markdown="1">

<ins id="prop14">**명제 14**</ins> Very ample line bundle은 항상 basepoint-free이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$\varphi_{\mathcal{L}}: X \hookrightarrow \mathbb{P}^r$$이 embedding이면 모든 점에서 정의된다. $$\varphi_{\mathcal{L}}(p) = [s_0(p) : \cdots : s_r(p)]$$ (여기서 $$s_0, \ldots, s_r$$은 $$H^0(X, \mathcal{L})$$의 기저)이므로, 각 $$p \in X$$에 대해 어떤 $$i$$가 $$s_i(p) \ne 0$$이다. 따라서 $$\operatorname{Bs}(\lvert \mathcal{L} \rvert) = \emptyset$$이다.

</details>

<div class="example" markdown="1">

<ins id="ex15">**예시 15**</ins> **$$\mathcal{O}_{\mathbb{P}^n}(1)$$은 very ample**: $$\lvert \mathcal{O}_{\mathbb{P}^n}(1) \rvert = \mathbb{P}(\mathbb{K}[\x_0, \ldots, \x_n]_1)$$는 identity embedding $$\mathbb{P}^n \hookrightarrow \mathbb{P}^n$$을 정의한다. $$F_i = \x_i$$로 놓으면 $$\varphi_L([x_0 : \cdots : x_n]) = [x_0 : \cdots : x_n]$$이다.

</div>

<div class="example" markdown="1">

<ins id="ex16">**예시 16**</ins> **$$\mathcal{O}_{\mathbb{P}^n}(d)$$도 very ample**: $$d > 0$$이면 $$\lvert \mathcal{O}_{\mathbb{P}^n}(d) \rvert$$는 *Veronese embedding*

$$\nu_d: \mathbb{P}^n \hookrightarrow \mathbb{P}^N, \quad [x_0 : \cdots : x_n] \mapsto [x_0^{a_0} \cdots x_n^{a_n} \text{ (모든 차수 } d \text{의 monomial, } \sum a_i = d)]$$

을 정의한다. 여기서 $$N = \binom{n+d}{d} - 1$$이다. 이 사상은 $$\mathbb{P}^n$$을 $$\mathbb{P}^N$$의 smooth degree $$d$$의 subvariety로 embedding한다.

</div>

Very ample의 정의에서 핵심은 사상이 단순한 morphism이 아니라 **closed embedding**이라는 점이다. Closed embedding $$X \hookrightarrow \mathbb{P}^r$$이 주어지면, $$X$$는 $$\mathbb{P}^r$$ 위의 어떤 homogeneous ideal의 zero set으로 실현되며, 따라서 $$X$$의 모든 기하학적 정보가 사영공간 안에서 읽어낼 수 있게 된다. 실제로 projective variety의 본질적 정의는 "어떤 사영공간의 closed subvariety"인 것이며, [§사영다양체](/ko/math/algebraic_geometry/projective_varieties)에서 다루었듯 quasi-projective variety와의 구별도 여기에 있다. 이 관점에서, $$\mathcal{L}$$이 very ample이라는 것은 $$\mathcal{L}$$ 자체가 $$X$$를 사영공간에 넣는 "좌표"를 제공한다는 의미를 갖는다.

Ample line bundle은 대수기하학에서 가장 중요한 개념 중 하나이다. 정의 13은 "충분히 큰 거듭제곱이 very ample"이라는 형태로만 ample을 규정하지만, 이 정의는 다음과 같은 깊은 결과들과 연결된다. 첫째, $$\mathcal{L}$$이 ample이면 충분히 큰 $$m$$에 대해 complete linear system $$\lvert \mathcal{L}^{\otimes m} \rvert$$가 basepoint-free이고 매우 자유로운 (sufficiently ample) section들을 제공하며, 이를 통해 $$X$$ 위의 임의의 coherent sheaf에 대해 Serre's vanishing theorem $$H^i(X, \mathcal{F} \otimes \mathcal{L}^{\otimes m}) = 0$$ (for $$m \gg 0$$, $$i > 0$$)이 성립한다. 둘째, $$\mathcal{L}$$이 ample이면 $$\lvert \mathcal{L}^{\otimes m} \rvert$$는 매우 다양한 effective divisor를 parameterize하며, $$X$$의 인자 이론에서 기본적인 역할을 수행한다. 셋째, projective variety의 분류론에서 ample (또는 그 일반화인 nef, big) line bundle의 존재 여부는 variety의 기하학적 성질을 결정하는 핵심 정보이다.

Complex geometry와의 연결에서, **Kodaira embedding 정리**는 다음을 assertion한다. Compact complex manifold $$X$$ 위의 line bundle $$\mathcal{L}$$에 대해, $$\mathcal{L}$$이 positive curvature를 갖는 Hermitian metric을 인정하는 것 (complex-analytic positivity)은 $$\mathcal{L}$$이 ample인 것과 동치이다. 대수기하학적으로는, smooth projective variety $$X$$ 위의 line bundle $$\mathcal{L}$$이 ample인 것과 $$\mathcal{L}^{\otimes m}$$이 very ample인 것은 정의 13에 의해 동치이다. Kodaira embedding 정리의 본질은 이 대수적 조건이 해석적 조건 — positive curvature를 갖는 Hermitian metric의 존재 — 과 동치라는 점에 있다. 증명의 핵심 아이디어는, ample line bundle의 section들이 $$X$$를 사영공간에 embed하기에 충분하다는 점과, 이 embedding의 image가 사실 대수적 variety라는 것을 보이는 데 있다. (증명은 생략한다.)

이 글 전체의 narrative를 정리하자. 우리는 divisor에서 출발하여, 이를 line bundle의 section으로 reinterpret하고, linear system의 개념을 통해 section들의 family를 parameterize하였다. Base locus의 관념은 linear system이 사영공간으로의 사상을 정의할 수 있는지의 여부를 결정하며, basepoint-free linear system은 자연스럽게 morphism $$\varphi_L$$를 부여한다. 이 morphism이 closed embedding이 되는 조건이 바로 very ample의 정의이고, 충분한 거듭제곱에서 이 조건을 만족하는 것이 ample의 정의이다. 따라서

$$\text{Ample} \subseteq \text{Very ample} \subseteq \text{Basepoint-free}$$

라는 포함 관계를 얻으며, 가장 강한 조건인 ample line bundle은 사영다양체의 구조를 사영공간 안에서 이해하는 데 필요한 핵심 도구이다. Projective variety는 정의상 어떤 사영공간의 closed subvariety이므로, 결국 모든 projective variety는 어떤 ample line bundle을 가지며, 그 ample line bundle을 통해 variety의 인자 이론, 기하학, 그리고 분류를 연구할 수 있다.

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.
