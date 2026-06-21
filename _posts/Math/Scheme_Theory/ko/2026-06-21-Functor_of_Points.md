---
title: "점함자"
description: "스킴을 그 점함자로 바라보는 관점을 Yoneda 보조정리와 representable functor의 언어로 정리하고, 아핀공간·사영공간·Grassmannian·group scheme 등 주요 함자들을 살펴본다."
excerpt: "Functor of points, Yoneda embedding, representability, group schemes"

categories: [Math / Scheme Theory]
permalink: /ko/math/scheme_theory/functor_of_points
sidebar: 
    nav: "scheme_theory-ko"

date: 2026-06-21
weight: 21

published: false
---

우리는 [§스킴 사이의 사상, ⁋정의 6](/ko/math/scheme_theory/morphism_of_schemes#def6)에서 scheme morphism $$f: T \rightarrow X$$를 $$X$$의 *$$T$$-point*라 불렀고, $$T=\Spec A$$인 경우 이를 $$A$$-point라 불렀다. 또 [§스킴 사이의 사상, ⁋예시 7](/ko/math/scheme_theory/morphism_of_schemes#ex7)에서 algebraically closed field $$\mathbb{K}$$ 위의 affine space $$\mathbb{A}^n_\mathbb{K}$$의 $$\mathbb{K}$$-point들이 정확히 고전적인 의미에서의 $$n$$-tuple $$(x_1,\ldots, x_n)$$들과 일대일대응한다는 것을 보았다. 이번 글의 목표는 이 관찰을 하나의 체계로 정립하는 것이다. 핵심은 scheme $$X$$를 위상공간과 structure sheaf로 이루어진 데이터로 보는 대신, 모든 가능한 test scheme $$T$$에 대하여 $$X$$의 $$T$$-point들이 어떻게 모여있는가, 즉 functor

$$h_X=\Hom_\Sch(-,X): \Sch^\op \rightarrow \Set$$

로 보는 것이다. 우리는 이 함자가 $$X$$를 isomorphism까지 완전히 결정한다는 것을 Yoneda 보조정리를 통해 확인하고, 이러한 함자적 관점이 affine space, projective space, Grassmannian, group scheme 등을 다룰 때 어떻게 자연스러운 언어를 제공하는지를 살펴본다.

## 점함자

[§스킴 사이의 사상, ⁋정의 9](/ko/math/scheme_theory/morphism_of_schemes#def9)에서 우리는 이미 functor of points를 도입하였다. 편의상 그 정의를 여기에 다시 적되, 앞으로 사용할 표기를 함께 고정한다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Scheme $$X$$의 *functor of points<sub>점함자</sub>*는 contravariant functor

$$h_X=\Hom_\Sch(-,X):\Sch^\op \rightarrow \Set$$

으로 정의된다. 각각의 scheme $$T$$에 대하여 $$h_X(T)=\Hom_\Sch(T,X)$$를 $$X$$의 *$$T$$-points<sub>$$T$$-점</sub>*들의 집합이라 부르고 $$X(T)$$로 적는다. 또, scheme morphism $$g: T' \rightarrow T$$에 대하여 $$h_X(g): X(T) \rightarrow X(T')$$는 합성

$$h_X(g)(f)=f\circ g$$

으로 주어진다. 특히 $$T=\Spec R$$인 경우 $$X(\Spec R)$$을 간단히 $$X(R)$$로 적고, $$R$$-point들의 집합이라 부른다.

</div>

집합 $$X(T)=\Hom_\Sch(T,X)$$의 원소를 *$$T$$-valued point*라고도 부른다. $$T$$를 변화시키며 scheme $$X$$를 관찰하는 이 관점에서, $$T$$는 일종의 측정 도구의 역할을 한다. 가장 단순한 test scheme은 한 점 $$\Spec \mathbb{K}$$이며, 이 경우 $$X(\mathbb{K})$$는 [§스킴 사이의 사상, ⁋예시 7](/ko/math/scheme_theory/morphism_of_schemes#ex7)에서 살펴본 고전적인 점들을 회복한다. 그러나 $$T$$로 더 큰 scheme을 사용하면 고전적인 점만으로는 보이지 않던 정보까지 함께 관찰할 수 있다.

함자성에 대해 부연하자면, scheme morphism $$g: T' \rightarrow T$$가 주어졌을 때 $$X(T)$$의 원소 $$f: T \rightarrow X$$를 $$f\circ g: T' \rightarrow X$$로 보내는 사상은 $$X$$의 $$T$$-point를 $$g$$를 따라 $$T'$$-point로 끌어당기는 것으로 이해할 수 있다. 특히 $$T'=\Spec R'$$, $$T=\Spec R$$이 affine scheme이고 $$g$$가 ring homomorphism $$\varphi: R \rightarrow R'$$로부터 온 경우, $$X(R) \rightarrow X(R')$$은 "$$R$$ 위에서 정의된 점을 $$\varphi$$를 통해 $$R'$$ 위로 옮기는" 사상이다.

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins> Scheme morphism $$\varphi: X \rightarrow Y$$가 주어졌다 하자. 그럼 각각의 test scheme $$T$$에 대하여, 합성

$$h_\varphi(T): X(T) \rightarrow Y(T);\qquad f\mapsto \varphi\circ f$$

은 well-defined map이며, 임의의 $$g: T' \rightarrow T$$에 대하여 $$h_\varphi(T')\circ h_X(g)=h_Y(g)\circ h_\varphi(T)$$가 성립한다. 즉 $$\varphi$$는 natural transformation $$h_\varphi: h_X \rightarrow h_Y$$를 유도한다. 이로부터 $$X\mapsto h_X$$가 functor

$$h_{(-)}:\Sch \rightarrow \operatorname{Fun}(\Sch^\op, \Set)$$

를 정의한다는 것을 안다. 

</div>

[예시 2](#ex2)에서 얻어진 functor $$h_{(-)}$$는 임의의 category에 대해 정의되는 Yoneda embedding의 특수한 경우이며, 이것이 점함자 관점이 가지는 힘의 원천이다. 다음 절에서 우리는 이 함자가 충실충만하다는 것을 확인한다.

## Yoneda 보조정리와 representability

점함자 관점이 유용하려면, scheme $$X$$에 대한 모든 정보가 함자 $$h_X$$에 담겨 있어야 한다. 이를 보장하는 것이 Yoneda 보조정리이다. 이는 임의의 locally small category $$\mathcal{C}$$에 대하여 성립하는 순수하게 범주론적인 사실이므로, 여기에서는 $$\mathcal{C}=\Sch$$인 경우로 진술한다. 

<div class="proposition" markdown="1">

<ins id="thm3">**정리 3** (Yoneda)</ins> Scheme $$X$$와 임의의 functor $$F:\Sch^\op \rightarrow \Set$$가 주어졌다 하자. 그럼 natural transformation들의 모임과 집합 $$F(X)$$ 사이에 자연스러운 일대일대응

$$\operatorname{Nat}(h_X, F)\cong F(X)$$

이 존재한다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

Natural transformation $$\eta: h_X \rightarrow F$$가 주어졌다 하면, 성분 $$\eta_X: h_X(X)=\Hom_\Sch(X,X) \rightarrow F(X)$$이 존재하고, 여기에 $$\id_X\in h_X(X)$$를 대입하여 원소 $$\eta_X(\id_X)\in F(X)$$를 얻는다. 이로써 사상

$$\Phi: \operatorname{Nat}(h_X, F) \rightarrow F(X);\qquad \eta\mapsto \eta_X(\id_X)$$

이 정의된다. 거꾸로 원소 $$\xi\in F(X)$$가 주어졌다 하면, 각각의 test scheme $$T$$와 $$f\in h_X(T)=\Hom_\Sch(T,X)$$에 대하여

$$\eta^\xi_T(f)=F(f)(\xi)\in F(T)$$

으로 $$\eta^\xi_T: h_X(T) \rightarrow F(T)$$를 정의한다. 여기에서 $$F(f): F(X) \rightarrow F(T)$$는 $$F$$가 contravariant이므로 morphism $$f: T \rightarrow X$$로부터 얻어진 것이다. 이것이 natural transformation임을 보이려면, 임의의 $$g: T' \rightarrow T$$에 대하여 $$\eta^\xi_{T'}\circ h_X(g)=F(g)\circ \eta^\xi_T$$를 확인하면 되는데, $$f\in h_X(T)$$에 대하여

$$\eta^\xi_{T'}(h_X(g)(f))=\eta^\xi_{T'}(f\circ g)=F(f\circ g)(\xi)=F(g)(F(f)(\xi))=F(g)(\eta^\xi_T(f))$$

이 functoriality $$F(f\circ g)=F(g)\circ F(f)$$로부터 성립한다. 이로써 사상

$$\Psi: F(X) \rightarrow \operatorname{Nat}(h_X, F);\qquad \xi\mapsto \eta^\xi$$

이 정의된다. 마지막으로 $$\Phi$$와 $$\Psi$$가 서로 역사상임을 확인한다. 한편으로 $$\Phi(\Psi(\xi))=\eta^\xi_X(\id_X)=F(\id_X)(\xi)=\xi$$이다. 다른 한편으로 임의의 $$\eta$$에 대하여 $$\xi=\Phi(\eta)=\eta_X(\id_X)$$라 두면, 임의의 $$f: T \rightarrow X$$에 대하여 $$\eta$$의 naturality로부터 정사각형

$$F(f)\circ \eta_X=\eta_T\circ h_X(f)$$

이 성립하고, 양변을 $$\id_X$$에 적용하면

$$\eta_T(f)=\eta_T(h_X(f)(\id_X))=F(f)(\eta_X(\id_X))=F(f)(\xi)=\eta^\xi_T(f)$$

이므로 $$\eta=\eta^\xi=\Psi(\Phi(\eta))$$를 얻는다. 

</details>

[정리 3](#thm3)에서 $$F$$로 다른 점함자 $$h_Y$$를 택하면 곧바로 다음을 얻는다. 

<div class="proposition" markdown="1">

<ins id="cor4">**따름정리 4**</ins> 임의의 scheme $$X, Y$$에 대하여, [예시 2](#ex2)의 사상은 일대일대응

$$\Hom_\Sch(X,Y)\cong \operatorname{Nat}(h_X, h_Y)$$

을 준다. 따라서 functor $$h_{(-)}:\Sch \rightarrow \operatorname{Fun}(\Sch^\op, \Set)$$은 fully faithful이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[정리 3](#thm3)에서 $$F=h_Y$$로 두면 $$\operatorname{Nat}(h_X, h_Y)\cong h_Y(X)=\Hom_\Sch(X,Y)$$를 얻는다. 이 대응을 추적하면, natural transformation $$\eta$$에 대응하는 원소는 $$\eta_X(\id_X)\in \Hom_\Sch(X,Y)$$, 즉 scheme morphism $$\psi=\eta_X(\id_X)$$이고, 거꾸로 $$\psi: X \rightarrow Y$$에 대응하는 natural transformation은 $$\eta^\psi_T(f)=h_Y(f)(\psi)=\psi\circ f$$, 즉 [예시 2](#ex2)에서 정의한 $$h_\psi$$와 정확히 일치한다. 

</details>

[따름정리 4](#cor4)는 점함자 관점의 근본적인 정당화이다. Functor $$h_{(-)}$$가 fully faithful이므로, 두 scheme $$X, Y$$가 isomorphic인 것과 그 점함자 $$h_X, h_Y$$가 자연동형인 것이 동치이다. 따라서 $$X$$는 그 점함자 $$h_X$$에 의해 isomorphism까지 유일하게 결정되며, scheme 사이의 morphism은 점함자 사이의 natural transformation과 정확히 같은 데이터이다. 이로써 우리는 scheme을 다룰 때 그 점함자만을 가지고 작업할 수 있게 된다. 

이제 거꾸로, 주어진 함자가 어떤 scheme의 점함자로 나타나는지를 묻는 것이 자연스럽다. 

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> Functor $$F:\Sch^\op \rightarrow \Set$$가 *representable<sub>표현가능</sub>*하다는 것은, scheme $$X$$와 자연동형 $$F\cong h_X$$이 존재하는 것이다. 이 때 $$X$$를 $$F$$의 *representing object*라 부른다. 

</div>

[따름정리 4](#cor4)에 의하여, representing object는 (존재한다면) isomorphism까지 유일하게 결정된다. 따라서 어떤 기하학적 대상을 구성하고자 할 때, 그 대상이 가져야 할 $$T$$-point들의 집합 $$F(T)$$를 먼저 함자적으로 기술한 뒤, 이 $$F$$가 representable임을 보이는 전략을 취할 수 있다. 실제로 moduli problem들은 거의 항상 이러한 형태로 제기된다. 이 절의 마지막으로, representability를 [정리 3](#thm3)의 언어로 다시 풀어 쓴 universal element의 관점을 기록해둔다. 

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> Functor $$F:\Sch^\op \rightarrow \Set$$가 scheme $$X$$에 의해 representable인 것은, $$F(X)$$의 원소 $$\xi$$가 존재하여 다음 *universal property*를 만족하는 것과 동치이다: 임의의 scheme $$T$$와 원소 $$\zeta\in F(T)$$에 대하여, $$F(f)(\xi)=\zeta$$를 만족하는 morphism $$f: T \rightarrow X$$가 유일하게 존재한다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[정리 3](#thm3)의 일대일대응 $$\Psi: F(X)\cong \operatorname{Nat}(h_X, F)$$에서, 원소 $$\xi\in F(X)$$에 대응하는 natural transformation은 $$\eta^\xi_T(f)=F(f)(\xi)$$이다. 그럼 $$\eta^\xi$$가 자연동형인 것, 즉 각각의 성분 $$\eta^\xi_T: h_X(T) \rightarrow F(T)$$이 전단사인 것은 다음과 같이 풀린다. $$\eta^\xi_T$$가 전사인 것은 임의의 $$\zeta\in F(T)$$에 대하여 $$F(f)(\xi)=\zeta$$인 $$f$$가 존재하는 것이고, $$\eta^\xi_T$$가 단사인 것은 그러한 $$f$$가 유일한 것이다. 즉 $$\eta^\xi$$가 자연동형인 것은 $$\xi$$가 진술된 universal property를 만족하는 것과 정확히 같다. 한편 $$F$$가 representable인 것은 어떤 자연동형 $$h_X\cong F$$이 존재하는 것인데, $$\Psi$$가 전단사이므로 이는 위와 같은 $$\xi$$가 존재하는 것과 동치이다. 

</details>

[명제 6](#prop6)의 $$\xi\in F(X)$$를 $$F$$의 *universal element*라 부른다. 직관적으로 $$\xi$$는 $$X$$ 자신 위에서 정의된 가장 일반적인 $$F$$-데이터이며, 다른 모든 $$T$$ 위의 $$F$$-데이터는 이를 유일한 morphism $$T \rightarrow X$$로 끌어당겨 얻어진다. 

## 함자로 본 affine space와 사영공간

이제 구체적인 scheme들의 점함자를 계산하여, 함자적 기술이 어떻게 그 scheme의 기하학을 직접 드러내는지를 살펴본다. 가장 기본적인 예는 affine line $$\mathbb{A}^1$$이다. 

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> $$\mathbb{Z}$$ 위의 affine line $$\mathbb{A}^1=\Spec \mathbb{Z}[\x]$$에 대하여, 임의의 scheme $$T$$의 점들의 집합은

$$\mathbb{A}^1(T)\cong \Gamma(T, \mathcal{O}_T)=\mathcal{O}_T(T)$$

로 주어지며, 이 대응은 $$T$$에 대해 자연스럽다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[§아핀스킴, ⁋정리 13](/ko/math/scheme_theory/affine_schemes#thm13)에서 살펴본 adjunction

$$\Hom_\Sch(T, \Spec A)\cong \Hom_\cRing(A, \Gamma(T, \mathcal{O}_T))$$

에서 $$A=\mathbb{Z}[\x]$$로 두자. Ring $$\mathbb{Z}[\x]$$는 $$\cRing$$에서 free object이므로, ring homomorphism $$\mathbb{Z}[\x] \rightarrow \Gamma(T, \mathcal{O}_T)$$은 생성원 $$\x$$의 image $$\x\mapsto a$$를 자유롭게 정하는 것과 같고, 이는 정확히 원소 $$a\in \Gamma(T, \mathcal{O}_T)$$를 하나 고르는 것이다. 따라서

$$\mathbb{A}^1(T)=\Hom_\Sch(T, \Spec \mathbb{Z}[\x])\cong \Hom_\cRing(\mathbb{Z}[\x], \Gamma(T, \mathcal{O}_T))\cong \Gamma(T, \mathcal{O}_T)$$

이다. 자연스러움은 임의의 $$g: T' \rightarrow T$$에 대하여 restriction map $$\Gamma(T, \mathcal{O}_T) \rightarrow \Gamma(T', \mathcal{O}_{T'})$$이 위의 대응과 commute한다는 것으로, adjunction의 자연스러움으로부터 따라온다. 

</details>

[명제 7](#prop7)은 affine line의 $$T$$-point가 정확히 $$T$$ 위의 전역 정칙함수 하나라는 것을 말한다. 이 관점에서 $$\mathbb{A}^1$$은 "함수를 측정하는" scheme이다. 이를 $$n$$개의 생성원으로 일반화하면 다음을 얻는다. 

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> $$\mathbb{Z}$$ 위의 affine $$n$$-space $$\mathbb{A}^n=\Spec \mathbb{Z}[\x_1,\ldots, \x_n]$$에 대하여, 자연스러운 일대일대응

$$\mathbb{A}^n(T)\cong \Gamma(T, \mathcal{O}_T)^n$$

이 존재한다. 즉 $$\mathbb{A}^n$$의 $$T$$-point는 $$T$$ 위의 정칙함수 $$n$$개의 순서쌍이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[명제 7](#prop7)의 증명과 동일하게, free ring $$\mathbb{Z}[\x_1,\ldots, \x_n]$$에서 나가는 ring homomorphism은 각 생성원 $$\x_i$$의 image $$a_i\in \Gamma(T, \mathcal{O}_T)$$를 자유롭게 정하는 것이므로

$$\mathbb{A}^n(T)\cong \Hom_\cRing(\mathbb{Z}[\x_1,\ldots, \x_n], \Gamma(T, \mathcal{O}_T))\cong \Gamma(T, \mathcal{O}_T)^n$$

을 얻는다. 

</details>

특별히 $$T=\Spec R$$인 경우 $$\mathbb{A}^n(R)\cong R^n$$이며, 이는 고전적인 직관과 정확히 일치한다. 즉 affine $$n$$-space의 $$R$$-point는 $$R$$의 원소 $$n$$개로 이루어진 좌표이다. 한편 $$T$$가 affine이 아닌 경우에는 $$\Gamma(T,\mathcal{O}_T)$$이 더 풍부할 수 있으므로, $$\mathbb{A}^n(T)$$ 역시 고전적인 좌표보다 더 많은 정보를 담는다. 

곱셈에 대한 가역원만을 추출하면 다음 함자를 얻는다. 

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> $$\mathbb{G}_m=\Spec \mathbb{Z}[\x, \x^{-1}]$$에 대하여, 자연스러운 일대일대응

$$\mathbb{G}_m(T)\cong \Gamma(T, \mathcal{O}_T)^\times$$

이 존재한다. 여기에서 $$\Gamma(T, \mathcal{O}_T)^\times$$은 ring $$\Gamma(T, \mathcal{O}_T)$$의 가역원들의 group이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$\mathbb{Z}[\x, \x^{-1}]=\mathbb{Z}[\x]_\x$$이므로, ring homomorphism $$\mathbb{Z}[\x, \x^{-1}] \rightarrow \Gamma(T, \mathcal{O}_T)$$은 $$\x$$의 image $$a$$가 가역인 것들과 일대일대응한다. 실제로 localization의 universal property에 의하여 $$\mathbb{Z}[\x]_\x$$에서 나가는 ring homomorphism은 $$\x$$의 image를 가역원으로 보내는 $$\mathbb{Z}[\x] \rightarrow \Gamma(T, \mathcal{O}_T)$$들과 정확히 대응하고, [명제 7](#prop7)에서 본 것처럼 이는 가역원 $$a\in \Gamma(T, \mathcal{O}_T)^\times$$를 하나 고르는 것이다. 

</details>

이제 affine이 아닌 scheme의 대표적인 예로 사영공간 $$\mathbb{P}^n$$의 점함자를 살펴보자. 고전적으로 $$\mathbb{P}^n$$의 점은 동차좌표 $$[x_0:\cdots:x_n]$$, 즉 영이 아닌 $$(n+1)$$-tuple을 전체 scaling으로 동일시한 것이다. 이미 [§스킴 사이의 사상, ⁋예시 5](/ko/math/scheme_theory/morphism_of_schemes#ex5)에서 우리는 ring $$A$$ 위의 scheme $$X$$와 함수 $$f_0,\ldots, f_n\in \Gamma(X, \mathcal{O}_X)$$이 적절한 조건을 만족할 때 morphism $$X \rightarrow \mathbb{P}^n_A$$이 얻어지는 것을 보았다. 함자적 관점은 이 구성을 정확한 표현으로 만든다. 우선 직선다발을 다루어야 하므로, 다음을 약속한다. 

<div class="definition" markdown="1">

<ins id="def10">**정의 10**</ins> Scheme $$T$$ 위의 *line bundle<sub>직선다발</sub>* $$\mathcal{L}$$은 rank $$1$$의 locally free $$\mathcal{O}_T$$-module이다. Line bundle $$\mathcal{L}$$의 절단 $$s_0,\ldots, s_n\in \Gamma(T, \mathcal{L})$$이 $$\mathcal{L}$$을 *globally generate<sub>전역생성</sub>*한다는 것은, 각각의 점 $$t\in T$$에서 stalk $$\mathcal{L}_t$$이 germ $$(s_0)_t,\ldots, (s_n)_t$$로 $$\mathcal{O}_{T,t}$$-module로서 생성되는 것이다. 두 데이터 $$(\mathcal{L}, s_0,\ldots, s_n)$$과 $$(\mathcal{L}', s_0',\ldots, s_n')$$이 *isomorphic*하다는 것은, $$\mathcal{O}_T$$-module isomorphism $$\psi:\mathcal{L} \rightarrow \mathcal{L}'$$이 존재하여 각각의 $$i$$에 대하여 $$\psi(s_i)=s_i'$$인 것이다. 

</div>

직선다발과 그 생성절단의 isomorphism 개념을 위와 같이 약속하면, $$\mathbb{P}^n$$의 점함자는 다음과 같이 깔끔하게 기술된다. 

<div class="proposition" markdown="1">

<ins id="thm11">**정리 11**</ins> $$\mathbb{Z}$$ 위의 projective space $$\mathbb{P}^n=\Proj \mathbb{Z}[\x_0,\ldots, \x_n]$$에 대하여, $$\mathbb{P}^n(T)$$는 $$T$$ 위의 line bundle $$\mathcal{L}$$과 이를 globally generate하는 절단 $$s_0,\ldots, s_n\in \Gamma(T, \mathcal{L})$$의 데이터 $$(\mathcal{L}, s_0,\ldots, s_n)$$들의 isomorphism class와 자연스럽게 일대일대응한다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

Morphism $$f: T \rightarrow \mathbb{P}^n$$이 주어졌다 하자. $$\mathbb{P}^n$$ 위의 twisting sheaf $$\mathcal{O}_{\mathbb{P}^n}(1)$$은 line bundle이고 그 전역절단들 $$\x_0,\ldots, \x_n$$은 $$\mathcal{O}_{\mathbb{P}^n}(1)$$을 globally generate하므로, pullback을 취하여 $$T$$ 위의 line bundle $$\mathcal{L}=f^\ast \mathcal{O}_{\mathbb{P}^n}(1)$$과 절단 $$s_i=f^\ast \x_i$$를 얻는다. Pullback이 globally generate되는 성질을 보존하므로 $$(\mathcal{L}, s_0,\ldots, s_n)$$은 위의 데이터를 이룬다. 

거꾸로 $$T$$ 위의 line bundle $$\mathcal{L}$$과 이를 globally generate하는 절단 $$s_0,\ldots, s_n$$이 주어졌다 하자. 각각의 $$i$$에 대하여 $$s_i$$가 생성하는 곳 $$T_{s_i}=\{t\in T\mid (s_i)_t \text{ generates } \mathcal{L}_t\}$$는 열린집합이고, 절단들이 $$\mathcal{L}$$을 globally generate하므로 $$\{T_{s_i}\}_{i=0}^n$$은 $$T$$의 열린덮개를 이룬다. $$T_{s_i}$$ 위에서는 $$s_i$$가 $$\mathcal{L}\vert_{T_{s_i}}$$의 자명화를 주므로, 각 $$j$$에 대하여 $$s_j/s_i\in \Gamma(T_{s_i}, \mathcal{O}_T)$$가 잘 정의된다. 이로써 [§스킴 사이의 사상, ⁋예시 5](/ko/math/scheme_theory/morphism_of_schemes#ex5)와 같은 방식으로 $$T_{s_i} \rightarrow D_+(\x_i)$$를 정의하고, 교집합 위에서의 gluing condition을 확인하여 morphism $$f: T \rightarrow \mathbb{P}^n$$을 얻는다. 

이 두 구성이 서로 역이라는 것과 isomorphic한 데이터가 같은 morphism을 준다는 것은, $$(\mathcal{L}, s_0,\ldots, s_n)$$ 전체를 $$\mathcal{O}_T$$-module isomorphism으로 옮겨도 $$s_j/s_i$$들이 변하지 않으므로 같은 gluing 데이터를 준다는 사실로부터 확인된다. 자연스러움은 $$g: T' \rightarrow T$$에 대하여 위의 데이터를 pullback하는 것과 morphism을 합성하는 것이 일치한다는 것이다. 

</details>

[정리 11](#thm11)은 사영공간의 함자적 본질을 보여준다. $$\mathbb{P}^n$$은 더 이상 affine scheme들을 붙인 결과로서 다루어지지 않고, "line bundle 하나와 그것을 생성하는 절단 $$n+1$$개"라는 단일한 데이터를 분류하는 대상으로 나타난다. 특별히 $$T=\Spec \mathbb{K}$$가 한 점이고 $$\mathbb{K}$$가 field인 경우, $$\mathbb{K}$$ 위의 line bundle은 자명하므로 데이터는 $$0$$이 아닌 $$(n+1)$$-tuple $$(s_0,\ldots, s_n)\in \mathbb{K}^{n+1}$$을 전체 scaling $$\mathbb{K}^\times$$으로 나눈 것과 같고, 이는 정확히 고전적인 동차좌표 $$[s_0:\cdots:s_n]$$이다. 즉 line bundle의 등장은 동차좌표의 전체 scaling 모호성을 함자적으로 정확하게 포착한 것이다. 

이 관점은 Grassmannian으로 자연스럽게 확장된다. 

<div class="example" markdown="1">

<ins id="ex12">**예시 12**</ins> $$\mathbb{Z}$$ 위의 Grassmannian $$\Gr(k,n)$$은 다음 함자를 representable하게 만드는 scheme으로 정의할 수 있다. 각각의 $$T$$에 대하여, $$\Gr(k,n)(T)$$를 자명한 다발 $$\mathcal{O}_T^n$$의 rank $$k$$ locally free 몫다발들

$$\mathcal{O}_T^n \twoheadrightarrow \mathcal{Q},\qquad \mathcal{Q}\text{ is locally free of rank } k$$

의 isomorphism class들의 집합으로 둔다. 여기에서 두 몫다발 $$\mathcal{O}_T^n\twoheadrightarrow \mathcal{Q}$$와 $$\mathcal{O}_T^n\twoheadrightarrow \mathcal{Q}'$$이 isomorphic하다는 것은, 두 몫사상을 commute하게 하는 $$\mathcal{O}_T$$-module isomorphism $$\mathcal{Q}\cong \mathcal{Q}'$$이 존재하는 것이다. $$T=\Spec \mathbb{K}$$가 field 위의 한 점인 경우, rank $$k$$ 몫공간 $$\mathbb{K}^n\twoheadrightarrow Q$$은 그 kernel인 $$\mathbb{K}^n$$의 $$(n-k)$$차원 부분공간과 일대일대응하므로, $$\Gr(k,n)(\mathbb{K})$$는 $$\mathbb{K}^n$$의 $$(n-k)$$차원 부분공간들의 집합, 즉 고전적인 Grassmannian과 일치한다. $$k=1$$인 경우, 곧 rank $$1$$ 몫다발을 분류하는 경우 [정리 11](#thm11)의 사영공간 $$\mathbb{P}^{n-1}$$로 환원된다. 

</div>

[예시 12](#ex12)에서 몫다발을 사용하는 것은 [정리 11](#thm11)에서 line bundle과 그 생성절단을 사용한 것의 직접적인 일반화이다. 실제로 자명한 다발의 rank $$1$$ 몫다발 $$\mathcal{O}_T^{n}\twoheadrightarrow \mathcal{L}$$을 주는 것은, $$\mathcal{L}$$의 생성절단 $$n$$개를 주는 것과 같다. 이러한 함자적 정의가 representable임을 보이는 것이 moduli theory의 출발점이며, 그 증명은 Grassmannian을 affine chart들로 덮어 [명제 6](#prop6)의 universal element를 구성하는 방식으로 이루어진다. 

## 함자로 본 올곱

점함자 관점은 [§올곱, ⁋정의 1](/ko/math/scheme_theory/fiber_products#def1)에서 정의한 fiber product와 잘 맞아떨어진다. Fiber product $$X\times_S Y$$의 universal property는, 임의의 test scheme $$T$$에 대하여 그 $$T$$-point들이 어떻게 결정되는지를 함자 수준에서 곧바로 말해준다. 

<div class="proposition" markdown="1">

<ins id="prop13">**명제 13**</ins> Scheme morphism $$X \rightarrow S$$와 $$Y \rightarrow S$$가 주어졌다 하자. 그럼 임의의 scheme $$T$$에 대하여, 자연스러운 일대일대응

$$(X\times_S Y)(T)\cong X(T)\times_{S(T)} Y(T)$$

이 존재한다. 우변은 집합들의 fiber product, 즉 $$X(T)\times Y(T)$$에서 $$X(T) \rightarrow S(T)$$와 $$Y(T) \rightarrow S(T)$$가 같은 값을 주는 순서쌍들의 집합이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[§올곱, ⁋정의 1](/ko/math/scheme_theory/fiber_products#def1)의 universal property는, $$T$$로부터 $$X\times_S Y$$로의 morphism이 $$\psi_X: T \rightarrow X$$와 $$\psi_Y: T \rightarrow Y$$로서 $$S$$로의 합성이 일치하는, 즉 $$X(T) \rightarrow S(T)$$와 $$Y(T) \rightarrow S(T)$$를 통해 $$\psi_X$$와 $$\psi_Y$$가 같은 $$S$$-point로 가는 순서쌍과 유일하게 대응한다는 것을 정확히 말한다. 이를 집합의 언어로 적으면 

$$(X\times_S Y)(T)\cong \{(\psi_X, \psi_Y)\in X(T)\times Y(T)\mid \psi_X, \psi_Y \text{ map to the same element of } S(T)\}=X(T)\times_{S(T)} Y(T)$$

이다. 자연스러움은 $$g: T' \rightarrow T$$에 대하여 양변의 끌어당김이 일치한다는 것으로, universal property의 자연스러움으로부터 따라온다. 

</details>

[명제 13](#prop13)은 fiber product를 함자 수준에서 "점별로 fiber product를 취하는" 연산으로 해석하게 해준다. 이 관점에서 fiber product의 존재성 증명 ([§올곱, ⁋정리 8](/ko/math/scheme_theory/fiber_products#thm8))은, 점별로 자명하게 정의되는 함자 $$T\mapsto X(T)\times_{S(T)} Y(T)$$가 representable임을 보이는 일로 재해석된다. 특히 product $$X\times Y=X\times_{\Spec \mathbb{Z}} Y$$의 경우에는 단순히 $$(X\times Y)(T)\cong X(T)\times Y(T)$$이 된다. 

## Group scheme

함자적 관점이 가장 빛을 발하는 곳 중 하나는 group scheme이다. 고전적으로 algebraic group은 group 구조를 가진 variety로서, 곱셈과 역원이 morphism인 것으로 정의된다. ([§대수적 군, ⁋정의 1](/ko/math/scheme_theory/algebraic_groups#def1)) 이를 scheme의 세계로 옮기는 가장 깔끔한 방법은, 각각의 test scheme 위에서 그 점들이 group을 이루도록 요구하는 것이다. 

<div class="definition" markdown="1">

<ins id="def14">**정의 14**</ins> Scheme $$S$$ 위의 *group scheme<sub>군 스킴</sub>*은, $$S$$-scheme $$G$$로서 그 점함자가 group으로 값을 갖는 함자로 lift되는 것이다. 즉 functor

$$h_G:(\Sch_{/S})^\op \rightarrow \mathbf{Grp}$$

이 존재하여, 망각함자 $$\mathbf{Grp} \rightarrow \Set$$과 합성하면 $$\Hom_{\Sch_{/S}}(-, G)$$이 되는 것이다. 풀어 말하면, 각각의 $$S$$-scheme $$T$$에 대하여 $$G(T)$$에 group 구조가 주어지고, 임의의 morphism $$T' \rightarrow T$$가 유도하는 $$G(T) \rightarrow G(T')$$이 group homomorphism인 것이다. 

</div>

[정의 14](#def14)는 group scheme을 "함자적으로 group인 scheme"으로 규정한다. 이것이 곱셈, 역원, 항등원 morphism으로 주어지는 고전적인 정의와 동치임은 Yoneda 보조정리로부터 따라온다. 실제로 [따름정리 4](#cor4)에 의하여 $$\mathbf{Grp}$$-값 lift를 주는 것은, group의 공리를 표현하는 가환 도식을 만족하는 morphism

$$m: G\times_S G \rightarrow G,\qquad i: G \rightarrow G,\qquad e: S \rightarrow G$$

들을 주는 것과 같다. 여기에서 $$m, i, e$$는 각각 $$T$$-point 수준에서의 곱셈, 역원, 항등원을 [명제 13](#prop13)을 통해 표현한 것이다. 함자적 정의의 장점은, group의 공리를 직접 가환 도식으로 적는 대신 각 $$G(T)$$가 통상적인 의미에서 group이라는 것만 확인하면 된다는 데 있다. 

<div class="example" markdown="1">

<ins id="ex15">**예시 15**</ins> 다음은 $$\mathbb{Z}$$ 위의 대표적인 group scheme들이다. 

1. *Additive group<sub>덧셈군</sub>* $$\mathbb{G}_a=\Spec \mathbb{Z}[\x]=\mathbb{A}^1$$. [명제 8](#prop8)에 의하여 $$\mathbb{G}_a(T)\cong \Gamma(T, \mathcal{O}_T)$$이며, 여기에 ring $$\Gamma(T, \mathcal{O}_T)$$의 덧셈을 주면 group이 된다. 임의의 ring homomorphism은 덧셈을 보존하므로 함자성이 성립하고, $$\mathbb{G}_a$$는 group scheme이다. 

2. *Multiplicative group<sub>곱셈군</sub>* $$\mathbb{G}_m=\Spec \mathbb{Z}[\x, \x^{-1}]$$. [명제 9](#prop9)에 의하여 $$\mathbb{G}_m(T)\cong \Gamma(T, \mathcal{O}_T)^\times$$이며, 여기에 가역원들의 곱셈을 주면 group이 된다. 

3. *$$n$$-th roots of unity* $$\mu_n=\Spec \mathbb{Z}[\x]/(\x^n-1)$$. 그럼 $$\mu_n(T)\cong \{a\in \Gamma(T, \mathcal{O}_T)^\times\mid a^n=1\}$$이며, 이는 $$\mathbb{G}_m(T)$$의 부분group이다. 따라서 $$\mu_n$$은 $$\mathbb{G}_m$$의 closed subgroup scheme이다. 

4. *General linear group* $$\GL_n$$. 각각의 ring $$R$$에 대하여 $$\GL_n(R)$$을 $$R$$ 성분의 가역행렬들의 group으로 두면, 이는 

$$\GL_n=\Spec \mathbb{Z}[\x_{11},\ldots, \x_{nn}, \det{}^{-1}]$$

으로 representable한 group scheme이 된다. 여기에서 $$\det$$은 행렬 $$(\x_{ij})$$의 determinant이며, 이를 가역으로 만든 localization을 취한 것이다. 

</div>

[예시 15](#ex15)의 각 경우에서 group 구조는 test scheme $$T$$에 대해 점별로 통상적인 대수 구조를 주는 것만으로 정의되었으며, 별도의 가환 도식을 그릴 필요가 없었다. 특히 $$\mu_n$$의 경우, $$\mathbb{Z}[\x]/(\x^n-1)$$이 $$n$$이 base ring에서 가역이 아닐 때에는 reduced가 아닐 수 있으므로, 이는 고전적인 variety의 언어로는 잘 포착되지 않는 nilpotent를 가진 group scheme의 예이다. 이러한 대상까지 자연스럽게 다룰 수 있다는 점이 함자적 관점과 scheme 언어의 강점이다. 

마지막으로, 위의 모든 구성은 base scheme $$S$$를 고정한 상대적인 상황으로 일반화된다. 즉 임의의 함자 $$F:(\Sch_{/S})^\op \rightarrow \Set$$을 다룰 수 있으며, 이 경우 representability는 $$S$$-scheme의 존재로 묻게 된다. Affine space, 사영공간, Grassmannian, group scheme의 함자적 정의는 모두 $$\Spec \mathbb{Z}$$ 위에서 주어졌으므로, 임의의 base $$S$$ 위로 base change ([§올곱, ⁋예시 9](/ko/math/scheme_theory/fiber_products#ex9))하여 상대적인 버전 $$\mathbb{A}^n_S, \mathbb{P}^n_S, \Gr(k,n)_S, \GL_{n,S}$$를 얻는다. 점함자의 언어에서 이는 단지 test scheme을 $$\Sch_{/S}$$로 제한하는 것에 해당하며, 따라서 절대적인 경우와 상대적인 경우가 하나의 틀 안에서 통일적으로 다루어진다. 

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic geometry*. Graduate texts in mathematics. Springer, 1977.  
**[Vak]** R. Vakil, *The rising sea: Foundations of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/).  
**[GD]** A. Grothendieck, J. Dieudonné, *Éléments de géométrie algébrique I*. Springer, 1971.  
**[Mum]** D. Mumford, *The red book of varieties and schemes*. Lecture notes in mathematics. Springer, 1999.  
**[EH]** D. Eisenbud, J. Harris, *The geometry of schemes*. Graduate texts in mathematics. Springer, 2000.  

---
