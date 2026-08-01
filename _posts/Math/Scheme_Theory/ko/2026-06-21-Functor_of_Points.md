---
title: "점함자"
description: "스킴을 그 점함자로 바라보는 관점을 Yoneda 보조정리와 representable functor의 언어로 정리하고, 아핀공간·사영공간·Grassmannian·올곱 등 주요 함자들을 살펴본다."
excerpt: "Functor of points, Yoneda embedding, representability, fiber products"

categories: [Math / Scheme Theory]
permalink: /ko/math/scheme_theory/functor_of_points
sidebar: 
    nav: "scheme_theory-ko"

date: 2026-06-21
weight: 22

published: false
drift_needed: true
---

우리는 [§스킴 사이의 사상, ⁋정의 6](/ko/math/scheme_theory/morphism_of_schemes#def6)에서 scheme morphism $f: T \rightarrow X$를 $X$의 *$T$-point*라 불렀고, $T=\Spec A$인 경우 이를 $A$-point라 불렀다. 또 [§스킴 사이의 사상, ⁋예시 7](/ko/math/scheme_theory/morphism_of_schemes#ex7)에서 algebraically closed field $\mathbb{K}$ 위의 affine space $\mathbb{A}^n_\mathbb{K}$의 $\mathbb{K}$-point들이 정확히 고전적인 의미에서의 $n$-tuple $(x_1,\ldots, x_n)$들과 일대일대응한다는 것을 보았다. 이번 글의 목표는 이 관찰을 하나의 체계로 정립하는 것이다. 핵심은 scheme $X$를 위상공간과 structure sheaf로 이루어진 데이터로 보는 대신, 모든 가능한 test scheme $T$에 대하여 $X$의 $T$-point들이 어떻게 모여있는가, 즉 functor

$$h_X=\Hom_\Sch(-,X): \Sch^\op \rightarrow \Set$$

로 보는 것이다. 이 functor는 [§스킴 사이의 사상, ⁋정의 9](/ko/math/scheme_theory/morphism_of_schemes#def9)에서 $X$의 functor of points라 부르기로 이미 약속하였다. 우리는 이 functor가 $X$를 isomorphism까지 완전히 결정한다는 것을 Yoneda 보조정리를 통해 확인하고, 이러한 functorial한 관점이 affine space, projective space, Grassmannian, fiber product 등을 다룰 때 어떻게 자연스러운 언어를 제공하는지를 살펴본다.

## Functor of points

앞으로 사용할 표기를 여기에서 고정하기로 한다. 각각의 scheme $T$에 대하여 $h_X(T)=\Hom_\Sch(T,X)$를 $X(T)$로 적으며, scheme morphism $g: T' \rightarrow T$에 대하여 $h_X(g): X(T) \rightarrow X(T')$은 합성 $h_X(g)(f)=f\circ g$로 주어진다. 특히 $T=\Spec R$인 경우 $X(\Spec R)$을 간단히 $X(R)$로 적는다. 또 집합 $X(T)$의 원소를 *$T$-valued point*라고도 부른다.

$T$를 변화시키며 scheme $X$를 관찰하는 이 관점에서, $T$는 일종의 측정 도구의 역할을 한다. 가장 단순한 test scheme은 한 점 $\Spec \mathbb{K}$이며, 이 경우 $X(\mathbb{K})$는 [§스킴 사이의 사상, ⁋예시 7](/ko/math/scheme_theory/morphism_of_schemes#ex7)에서 살펴본 고전적인 점들을 회복한다. 그러나 $T$로 더 큰 scheme을 사용하면 고전적인 점만으로는 보이지 않던 정보까지 함께 관찰할 수 있다.

Functoriality에 대해 부연하자면, scheme morphism $g: T' \rightarrow T$가 주어졌을 때 $X(T)$의 원소 $f: T \rightarrow X$를 $f\circ g: T' \rightarrow X$로 보내는 morphism은 $X$의 $T$-point를 $g$를 따라 $T'$-point로 끌어당기는 것으로 이해할 수 있다. 특히 $T'=\Spec R'$, $T=\Spec R$이 affine scheme이고 $g$가 ring homomorphism $\varphi: R \rightarrow R'$로부터 온 경우, $X(R) \rightarrow X(R')$은 "$R$ 위에서 정의된 점을 $\varphi$를 통해 $R'$ 위로 옮기는" morphism이다.

한편 scheme morphism $\varphi: X \rightarrow Y$가 주어졌다 하면, 각각의 test scheme $T$에 대하여 합성

$$h_\varphi(T): X(T) \rightarrow Y(T);\qquad f\mapsto \varphi\circ f$$

은 well-defined map이며, 임의의 $g: T' \rightarrow T$에 대하여 $h_\varphi(T')\circ h_X(g)=h_Y(g)\circ h_\varphi(T)$가 성립한다. 즉 $\varphi$는 natural transformation $h_\varphi: h_X \rightarrow h_Y$를 유도하고, 이로부터 $X\mapsto h_X$가 functor

$$h_{(-)}:\Sch \rightarrow \operatorname{Fun}(\Sch^\op, \Set)$$

를 정의한다는 것을 안다. 이 functor $h_{(-)}$는 임의의 category에 대해 정의되는 Yoneda embedding의 특수한 경우이며, 이것이 functor of points 관점이 가지는 힘의 원천이다. 다음 절에서 우리는 이 functor가 fully faithful하다는 것을 확인한다.

## Yoneda 보조정리와 representability

Functor of points 관점이 유용하려면, scheme $X$에 대한 모든 정보가 functor $h_X$에 담겨 있어야 한다. 이를 보장하는 것이 Yoneda 보조정리이다. 이는 임의의 locally small category $\mathcal{C}$에 대하여 성립하는 순수하게 범주론적인 사실이므로, 여기에서는 $\mathcal{C}=\Sch$인 경우로 진술한다. 

::: 정리 1 (Yoneda)
Scheme $X$와 임의의 functor $F:\Sch^\op \rightarrow \Set$가 주어졌다 하자. 그럼 natural transformation들의 모임과 집합 $F(X)$ 사이에 자연스러운 일대일대응

$$\operatorname{Nat}(h_X, F)\cong F(X)$$

이 존재한다. 
:::
::: 증명
Natural transformation $\eta: h_X \rightarrow F$가 주어졌다 하면, 성분 $\eta_X: h_X(X)=\Hom_\Sch(X,X) \rightarrow F(X)$이 존재하고, 여기에 $\id_X\in h_X(X)$를 대입하여 원소 $\eta_X(\id_X)\in F(X)$를 얻는다. 이로써 morphism

$$\Phi: \operatorname{Nat}(h_X, F) \rightarrow F(X);\qquad \eta\mapsto \eta_X(\id_X)$$

이 정의된다. 거꾸로 원소 $\xi\in F(X)$가 주어졌다 하면, 각각의 test scheme $T$와 $f\in h_X(T)=\Hom_\Sch(T,X)$에 대하여

$$\eta^\xi_T(f)=F(f)(\xi)\in F(T)$$

으로 $\eta^\xi_T: h_X(T) \rightarrow F(T)$를 정의한다. 여기에서 $F(f): F(X) \rightarrow F(T)$는 $F$가 contravariant이므로 morphism $f: T \rightarrow X$로부터 얻어진 것이다. 이것이 natural transformation임을 보이려면, 임의의 $g: T' \rightarrow T$에 대하여 $\eta^\xi_{T'}\circ h_X(g)=F(g)\circ \eta^\xi_T$를 확인하면 되는데, $f\in h_X(T)$에 대하여

$$\eta^\xi_{T'}(h_X(g)(f))=\eta^\xi_{T'}(f\circ g)=F(f\circ g)(\xi)=F(g)(F(f)(\xi))=F(g)(\eta^\xi_T(f))$$

이 functoriality $F(f\circ g)=F(g)\circ F(f)$로부터 성립한다. 이로써 morphism

$$\Psi: F(X) \rightarrow \operatorname{Nat}(h_X, F);\qquad \xi\mapsto \eta^\xi$$

이 정의된다. 마지막으로 $\Phi$와 $\Psi$가 서로 역사상임을 확인한다. 한편으로 $\Phi(\Psi(\xi))=\eta^\xi_X(\id_X)=F(\id_X)(\xi)=\xi$이다. 다른 한편으로 임의의 $\eta$에 대하여 $\xi=\Phi(\eta)=\eta_X(\id_X)$라 두면, 임의의 $f: T \rightarrow X$에 대하여 $\eta$의 naturality로부터 정사각형

$$F(f)\circ \eta_X=\eta_T\circ h_X(f)$$

이 성립하고, 양변을 $\id_X$에 적용하면

$$\eta_T(f)=\eta_T(h_X(f)(\id_X))=F(f)(\eta_X(\id_X))=F(f)(\xi)=\eta^\xi_T(f)$$

이므로 $\eta=\eta^\xi=\Psi(\Phi(\eta))$를 얻는다. 
:::

[정리 1](#thm1)에서 $F$로 다른 functor of points $h_Y$를 택하면 곧바로 다음을 얻는다. 

::: 따름정리 2
임의의 scheme $X, Y$에 대하여, 대응 $\varphi\mapsto h_\varphi$는 일대일대응

$$\Hom_\Sch(X,Y)\cong \operatorname{Nat}(h_X, h_Y)$$

을 준다. 따라서 functor $h_{(-)}:\Sch \rightarrow \operatorname{Fun}(\Sch^\op, \Set)$은 fully faithful이다. 
:::
::: 증명
[정리 1](#thm1)에서 $F=h_Y$로 두면 $\operatorname{Nat}(h_X, h_Y)\cong h_Y(X)=\Hom_\Sch(X,Y)$를 얻는다. 이 대응을 추적하면, natural transformation $\eta$에 대응하는 원소는 $\eta_X(\id_X)\in \Hom_\Sch(X,Y)$, 즉 scheme morphism $\psi=\eta_X(\id_X)$이고, 거꾸로 $\psi: X \rightarrow Y$에 대응하는 natural transformation은 $\eta^\psi_T(f)=h_Y(f)(\psi)=\psi\circ f$, 즉 앞 절에서 정의한 $h_\psi$와 정확히 일치한다. 
:::

[따름정리 2](#cor2)는 functor of points 관점의 근본적인 정당화이다. Functor $h_{(-)}$가 fully faithful이므로, 두 scheme $X, Y$가 isomorphic인 것과 그 functor of points $h_X, h_Y$가 natural isomorphism인 것이 동치이다. 따라서 $X$는 그 functor of points $h_X$에 의해 isomorphism까지 유일하게 결정되며, scheme 사이의 morphism은 functor of points 사이의 natural transformation과 정확히 같은 데이터이다. 이로써 우리는 scheme을 다룰 때 그 functor of points만을 가지고 작업할 수 있게 된다. 

이제 거꾸로, 주어진 functor가 어떤 scheme의 functor of points로 나타나는지를 묻는 것이 자연스럽다. 

::: 정의 3
Functor $F:\Sch^\op \rightarrow \Set$가 *representable<sub>표현가능</sub>*하다는 것은, scheme $X$와 natural isomorphism $F\cong h_X$이 존재하는 것이다. 이 때 $X$를 $F$의 *representing object<sub>표현 대상</sub>*라 부른다. 
:::

[따름정리 2](#cor2)에 의하여, representing object는 (존재한다면) isomorphism까지 유일하게 결정된다. 따라서 어떤 기하학적 대상을 구성하고자 할 때, 그 대상이 가져야 할 $T$-point들의 집합 $F(T)$를 먼저 functorial하게 기술한 뒤, 이 $F$가 representable임을 보이는 전략을 취할 수 있다. 실제로 moduli problem들은 거의 항상 이러한 형태로 제기된다. 이 절의 마지막으로, representability를 [정리 1](#thm1)의 언어로 다시 풀어 쓴 universal element의 관점을 기록해둔다. 

::: 명제 4
Functor $F:\Sch^\op \rightarrow \Set$가 scheme $X$에 의해 representable인 것은, $F(X)$의 원소 $\xi$가 존재하여 다음 *universal property*를 만족하는 것과 동치이다: 임의의 scheme $T$와 원소 $\zeta\in F(T)$에 대하여, $F(f)(\xi)=\zeta$를 만족하는 morphism $f: T \rightarrow X$가 유일하게 존재한다. 
:::
::: 증명
[정리 1](#thm1)의 일대일대응 $\Psi: F(X)\cong \operatorname{Nat}(h_X, F)$에서, 원소 $\xi\in F(X)$에 대응하는 natural transformation은 $\eta^\xi_T(f)=F(f)(\xi)$이다. 그럼 $\eta^\xi$가 natural isomorphism인 것, 즉 각각의 성분 $\eta^\xi_T: h_X(T) \rightarrow F(T)$이 전단사인 것은 다음과 같이 풀린다. $\eta^\xi_T$가 전사인 것은 임의의 $\zeta\in F(T)$에 대하여 $F(f)(\xi)=\zeta$인 $f$가 존재하는 것이고, $\eta^\xi_T$가 단사인 것은 그러한 $f$가 유일한 것이다. 즉 $\eta^\xi$가 natural isomorphism인 것은 $\xi$가 진술된 universal property를 만족하는 것과 정확히 같다. 한편 $F$가 representable인 것은 어떤 natural isomorphism $h_X\cong F$이 존재하는 것인데, $\Psi$가 전단사이므로 이는 위와 같은 $\xi$가 존재하는 것과 동치이다. 
:::

[명제 4](#prop4)의 $\xi\in F(X)$를 $F$의 *universal element*라 부른다. 직관적으로 $\xi$는 $X$ 자신 위에서 정의된 가장 일반적인 $F$-데이터이며, 다른 모든 $T$ 위의 $F$-데이터는 이를 유일한 morphism $T \rightarrow X$로 끌어당겨 얻어진다. 

## Functor로 본 affine space와 projective space

이제 구체적인 scheme들의 functor of points를 계산하여, functorial한 기술이 어떻게 그 scheme의 기하학을 직접 드러내는지를 살펴본다. 가장 기본적인 예는 affine line $\mathbb{A}^1$이다. 

::: 명제 5
$\mathbb{Z}$ 위의 affine line $\mathbb{A}^1=\Spec \mathbb{Z}[\x]$에 대하여, 임의의 scheme $T$의 점들의 집합은

$$\mathbb{A}^1(T)\cong \Gamma(T, \mathcal{O}_T)=\mathcal{O}_T(T)$$

로 주어지며, 이 대응은 $T$에 대해 자연스럽다. 
:::
::: 증명
[§아핀스킴, ⁋정리 13](/ko/math/scheme_theory/affine_schemes#thm13)에서 살펴본 adjunction

$$\Hom_\Sch(T, \Spec A)\cong \Hom_\cRing(A, \Gamma(T, \mathcal{O}_T))$$

에서 $A=\mathbb{Z}[\x]$로 두자. Ring $\mathbb{Z}[\x]$는 $\cRing$에서 free object이므로, ring homomorphism $\mathbb{Z}[\x] \rightarrow \Gamma(T, \mathcal{O}_T)$은 generator $\x$의 image $\x\mapsto a$를 자유롭게 정하는 것과 같고, 이는 정확히 원소 $a\in \Gamma(T, \mathcal{O}_T)$를 하나 고르는 것이다. 따라서

$$\mathbb{A}^1(T)=\Hom_\Sch(T, \Spec \mathbb{Z}[\x])\cong \Hom_\cRing(\mathbb{Z}[\x], \Gamma(T, \mathcal{O}_T))\cong \Gamma(T, \mathcal{O}_T)$$

이다. 자연스러움은 임의의 $g: T' \rightarrow T$에 대하여 restriction map $\Gamma(T, \mathcal{O}_T) \rightarrow \Gamma(T', \mathcal{O}_{T'})$이 위의 대응과 commute한다는 것으로, adjunction의 자연스러움으로부터 따라온다. 
:::

[명제 5](#prop5)는 affine line의 $T$-point가 정확히 $T$ 위의 전역 regular function 하나라는 것을 말한다. 이 관점에서 $\mathbb{A}^1$은 "함수를 측정하는" scheme이다. 이를 $n$개의 generator로 일반화하면 다음을 얻는다. 

::: 명제 6
$\mathbb{Z}$ 위의 affine $n$-space $\mathbb{A}^n=\Spec \mathbb{Z}[\x_1,\ldots, \x_n]$에 대하여, 자연스러운 일대일대응

$$\mathbb{A}^n(T)\cong \Gamma(T, \mathcal{O}_T)^n$$

이 존재한다. 즉 $\mathbb{A}^n$의 $T$-point는 $T$ 위의 regular function $n$개의 순서쌍이다. 
:::
::: 증명
[명제 5](#prop5)의 증명과 동일하게, free ring $\mathbb{Z}[\x_1,\ldots, \x_n]$에서 나가는 ring homomorphism은 각 generator $\x_i$의 image $a_i\in \Gamma(T, \mathcal{O}_T)$를 자유롭게 정하는 것이므로

$$\mathbb{A}^n(T)\cong \Hom_\cRing(\mathbb{Z}[\x_1,\ldots, \x_n], \Gamma(T, \mathcal{O}_T))\cong \Gamma(T, \mathcal{O}_T)^n$$

을 얻는다. 
:::

특별히 $T=\Spec R$인 경우 $\mathbb{A}^n(R)\cong R^n$이며, 이는 고전적인 직관과 정확히 일치한다. 즉 affine $n$-space의 $R$-point는 $R$의 원소 $n$개로 이루어진 좌표이다. 한편 $T$가 affine이 아닌 경우에는 $\Gamma(T,\mathcal{O}_T)$이 더 풍부할 수 있으므로, $\mathbb{A}^n(T)$ 역시 고전적인 좌표보다 더 많은 정보를 담는다. 

곱셈에 대한 가역원만을 추출하면 다음 functor를 얻는다. 

::: 명제 7
$\mathbb{G}_m=\Spec \mathbb{Z}[\x, \x^{-1}]$에 대하여, 자연스러운 일대일대응

$$\mathbb{G}_m(T)\cong \Gamma(T, \mathcal{O}_T)^\times$$

이 존재한다. 여기에서 $\Gamma(T, \mathcal{O}_T)^\times$은 ring $\Gamma(T, \mathcal{O}_T)$의 가역원들의 group이다. 
:::
::: 증명
$\mathbb{Z}[\x, \x^{-1}]=\mathbb{Z}[\x]_\x$이므로, ring homomorphism $\mathbb{Z}[\x, \x^{-1}] \rightarrow \Gamma(T, \mathcal{O}_T)$은 $\x$의 image $a$가 가역인 것들과 일대일대응한다. 실제로 localization의 universal property에 의하여 $\mathbb{Z}[\x]_\x$에서 나가는 ring homomorphism은 $\x$의 image를 가역원으로 보내는 $\mathbb{Z}[\x] \rightarrow \Gamma(T, \mathcal{O}_T)$들과 정확히 대응하고, [명제 5](#prop5)에서 본 것처럼 이는 가역원 $a\in \Gamma(T, \mathcal{O}_T)^\times$를 하나 고르는 것이다. 
:::

이제 affine이 아닌 scheme의 대표적인 예로 projective space $\mathbb{P}^n$의 functor of points를 살펴보자. 고전적으로 $\mathbb{P}^n$의 점은 homogeneous coordinates $[x_0:\cdots:x_n]$, 즉 영이 아닌 $(n+1)$-tuple을 전체 scaling으로 동일시한 것이다. 이미 [§스킴 사이의 사상, ⁋예시 5](/ko/math/scheme_theory/morphism_of_schemes#ex5)에서 우리는 ring $A$ 위의 scheme $X$와 함수 $f_0,\ldots, f_n\in \Gamma(X, \mathcal{O}_X)$이 적절한 조건을 만족할 때 morphism $X \rightarrow \mathbb{P}^n_A$이 얻어지는 것을 보았다. Functorial한 관점은 이 구성을 정확한 표현으로 만든다. 우선 line bundle을 다루어야 한다. Scheme $T$ 위의 rank $1$ locally free $\mathcal{O}_T$-module, 곧 invertible sheaf가 line bundle에 대응한다는 것은 [§준연접층, ⁋정의 12](/ko/math/scheme_theory/quasicoherent_sheaves#def12)에서 확인하였으므로, 여기에서는 그 절단에 관한 다음 개념만을 약속한다. 

::: 정의 8
Scheme $T$ 위의 line bundle $\mathcal{L}$의 절단 $s_0,\ldots, s_n\in \Gamma(T, \mathcal{L})$이 $\mathcal{L}$을 *globally generate<sub>전역생성</sub>*한다는 것은, 각각의 점 $t\in T$에서 stalk $\mathcal{L}_t$이 germ $(s_0)_t,\ldots, (s_n)_t$로 $\mathcal{O}_{T,t}$-module로서 생성되는 것이다. 두 데이터 $(\mathcal{L}, s_0,\ldots, s_n)$과 $(\mathcal{L}', s_0',\ldots, s_n')$이 *isomorphic*하다는 것은, $\mathcal{O}_T$-module isomorphism $\psi:\mathcal{L} \rightarrow \mathcal{L}'$이 존재하여 각각의 $i$에 대하여 $\psi(s_i)=s_i'$인 것이다. 
:::

Line bundle과 그 생성절단의 isomorphism 개념을 위와 같이 약속하면, $\mathbb{P}^n$의 functor of points는 다음과 같이 깔끔하게 기술된다. 

::: 정리 9
$\mathbb{Z}$ 위의 projective space $\mathbb{P}^n=\Proj \mathbb{Z}[\x_0,\ldots, \x_n]$에 대하여, $\mathbb{P}^n(T)$는 $T$ 위의 line bundle $\mathcal{L}$과 이를 globally generate하는 절단 $s_0,\ldots, s_n\in \Gamma(T, \mathcal{L})$의 데이터 $(\mathcal{L}, s_0,\ldots, s_n)$들의 isomorphism class와 자연스럽게 일대일대응한다. 
:::
::: 증명
Morphism $f: T \rightarrow \mathbb{P}^n$이 주어졌다 하자. $\mathbb{P}^n$ 위의 twisting sheaf $\mathcal{O}_{\mathbb{P}^n}(1)$은 line bundle이고 그 전역절단들 $\x_0,\ldots, \x_n$은 $\mathcal{O}_{\mathbb{P}^n}(1)$을 globally generate하므로, pullback을 취하여 $T$ 위의 line bundle $\mathcal{L}=f^\ast \mathcal{O}_{\mathbb{P}^n}(1)$과 절단 $s_i=f^\ast \x_i$를 얻는다. Pullback이 globally generate되는 성질을 보존하므로 $(\mathcal{L}, s_0,\ldots, s_n)$은 위의 데이터를 이룬다. 

거꾸로 $T$ 위의 line bundle $\mathcal{L}$과 이를 globally generate하는 절단 $s_0,\ldots, s_n$이 주어졌다 하자. 각각의 $i$에 대하여 $s_i$가 생성하는 곳 $T_{s_i}=\{t\in T\mid (s_i)_t \text{ generates } \mathcal{L}_t\}$는 열린집합이고, 절단들이 $\mathcal{L}$을 globally generate하므로 $\{T_{s_i}\}_{i=0}^n$은 $T$의 open cover를 이룬다. $T_{s_i}$ 위에서는 $s_i$가 $\mathcal{L}\vert_{T_{s_i}}$의 자명화를 주므로, 각 $j$에 대하여 $s_j/s_i\in \Gamma(T_{s_i}, \mathcal{O}_T)$가 잘 정의된다. 이로써 [§스킴 사이의 사상, ⁋예시 5](/ko/math/scheme_theory/morphism_of_schemes#ex5)와 같은 방식으로 $T_{s_i} \rightarrow D_+(\x_i)$를 정의하고, 교집합 위에서의 gluing condition을 확인하여 morphism $f: T \rightarrow \mathbb{P}^n$을 얻는다. 

이 두 구성이 서로 역이라는 것과 isomorphic한 데이터가 같은 morphism을 준다는 것은, $(\mathcal{L}, s_0,\ldots, s_n)$ 전체를 $\mathcal{O}_T$-module isomorphism으로 옮겨도 $s_j/s_i$들이 변하지 않으므로 같은 gluing 데이터를 준다는 사실로부터 확인된다. 자연스러움은 $g: T' \rightarrow T$에 대하여 위의 데이터를 pullback하는 것과 morphism을 합성하는 것이 일치한다는 것이다. 
:::

[정리 9](#thm9)는 projective space의 functorial한 본질을 보여준다. $\mathbb{P}^n$은 더 이상 affine scheme들을 붙인 결과로서 다루어지지 않고, "line bundle 하나와 그것을 생성하는 절단 $n+1$개"라는 단일한 데이터를 분류하는 대상으로 나타난다. 특별히 $T=\Spec \mathbb{K}$가 한 점이고 $\mathbb{K}$가 field인 경우, $\mathbb{K}$ 위의 line bundle은 자명하므로 데이터는 $0$이 아닌 $(n+1)$-tuple $(s_0,\ldots, s_n)\in \mathbb{K}^{n+1}$을 전체 scaling $\mathbb{K}^\times$으로 나눈 것과 같고, 이는 정확히 고전적인 homogeneous coordinates $[s_0:\cdots:s_n]$이다. 즉 line bundle의 등장은 homogeneous coordinates의 전체 scaling 모호성을 functorial하게 정확하게 포착한 것이다. 

이 관점은 Grassmannian으로 자연스럽게 확장된다. 

::: 예시 10
$\mathbb{Z}$ 위의 Grassmannian $\Gr(k,n)$은 다음 functor를 representable하게 만드는 scheme으로 정의할 수 있다. 각각의 $T$에 대하여, $\Gr(k,n)(T)$를 자명한 다발 $\mathcal{O}_T^n$의 rank $k$ locally free quotient bundle들

$$\mathcal{O}_T^n \twoheadrightarrow \mathcal{Q},\qquad \mathcal{Q}\text{ is locally free of rank } k$$

의 isomorphism class들의 집합으로 둔다. 여기에서 두 quotient bundle $\mathcal{O}_T^n\twoheadrightarrow \mathcal{Q}$와 $\mathcal{O}_T^n\twoheadrightarrow \mathcal{Q}'$이 isomorphic하다는 것은, 두 quotient map을 commute하게 하는 $\mathcal{O}_T$-module isomorphism $\mathcal{Q}\cong \mathcal{Q}'$이 존재하는 것이다. $T=\Spec \mathbb{K}$가 field 위의 한 점인 경우, rank $k$ quotient space $\mathbb{K}^n\twoheadrightarrow Q$은 그 kernel인 $\mathbb{K}^n$의 $(n-k)$차원 부분공간과 일대일대응하므로, $\Gr(k,n)(\mathbb{K})$는 $\mathbb{K}^n$의 $(n-k)$차원 부분공간들의 집합, 즉 고전적인 Grassmannian과 일치한다. $k=1$인 경우, 곧 rank $1$ quotient bundle을 분류하는 경우 [정리 9](#thm9)의 projective space $\mathbb{P}^{n-1}$로 환원된다. 
:::

[예시 10](#ex10)에서 quotient bundle을 사용하는 것은 [정리 9](#thm9)에서 line bundle과 그 생성절단을 사용한 것의 직접적인 일반화이다. 실제로 자명한 다발의 rank $1$ quotient bundle $\mathcal{O}_T^{n}\twoheadrightarrow \mathcal{L}$을 주는 것은, $\mathcal{L}$의 생성절단 $n$개를 주는 것과 같다. 이러한 functorial한 정의가 representable임을 보이는 것이 moduli theory의 출발점이며, 그 증명은 Grassmannian을 affine chart들로 덮어 [명제 4](#prop4)의 universal element를 구성하는 방식으로 이루어진다. 

## Functor로 본 올곱

Functor of points 관점은 [§올곱, ⁋정의 1](/ko/math/scheme_theory/fiber_products#def1)에서 정의한 fiber product와 잘 맞아떨어진다. Fiber product $X\times_S Y$의 universal property는, 임의의 test scheme $T$에 대하여 그 $T$-point들이 어떻게 결정되는지를 functor 수준에서 곧바로 말해준다. 

::: 명제 11
Scheme morphism $X \rightarrow S$와 $Y \rightarrow S$가 주어졌다 하자. 그럼 임의의 scheme $T$에 대하여, 자연스러운 일대일대응

$$(X\times_S Y)(T)\cong X(T)\times_{S(T)} Y(T)$$

이 존재한다. 우변은 집합들의 fiber product, 즉 $X(T)\times Y(T)$에서 $X(T) \rightarrow S(T)$와 $Y(T) \rightarrow S(T)$가 같은 값을 주는 순서쌍들의 집합이다. 
:::
::: 증명
[§올곱, ⁋정의 1](/ko/math/scheme_theory/fiber_products#def1)의 universal property는, $T$로부터 $X\times_S Y$로의 morphism이 $\psi_X: T \rightarrow X$와 $\psi_Y: T \rightarrow Y$로서 $S$로의 합성이 일치하는, 즉 $X(T) \rightarrow S(T)$와 $Y(T) \rightarrow S(T)$를 통해 $\psi_X$와 $\psi_Y$가 같은 $S$-point로 가는 순서쌍과 유일하게 대응한다는 것을 정확히 말한다. 이를 집합의 언어로 적으면 

$$(X\times_S Y)(T)\cong \{(\psi_X, \psi_Y)\in X(T)\times Y(T)\mid \psi_X, \psi_Y \text{ map to the same element of } S(T)\}=X(T)\times_{S(T)} Y(T)$$

이다. 자연스러움은 $g: T' \rightarrow T$에 대하여 양변의 끌어당김이 일치한다는 것으로, universal property의 자연스러움으로부터 따라온다. 
:::

[명제 11](#prop11)은 fiber product를 functor 수준에서 "점별로 fiber product를 취하는" 연산으로 해석하게 해준다. 이 관점에서 [§올곱, ⁋정리 8](/ko/math/scheme_theory/fiber_products#thm8)의 존재성 증명은, 점별로 자명하게 정의되는 functor $T\mapsto X(T)\times_{S(T)} Y(T)$가 representable임을 보이는 일로 재해석된다. 특히 product $X\times Y=X\times_{\Spec \mathbb{Z}} Y$의 경우에는 단순히 $(X\times Y)(T)\cong X(T)\times Y(T)$이 된다. 

마지막으로, 위의 모든 구성은 base scheme $S$를 고정한 상대적인 상황으로 일반화된다. 즉 임의의 functor $F:(\Sch_{/S})^\op \rightarrow \Set$을 다룰 수 있으며, 이 경우 representability는 $S$-scheme의 존재로 묻게 된다. Affine space, projective space, Grassmannian의 functorial한 정의는 모두 $\Spec \mathbb{Z}$ 위에서 주어졌으므로, 임의의 base $S$ 위로 base change하여 상대적인 버전 $\mathbb{A}^n_S, \mathbb{P}^n_S, \Gr(k,n)_S$를 얻는다. ([§올곱, ⁋예시 9](/ko/math/scheme_theory/fiber_products#ex9)) Functor of points의 언어에서 이는 단지 test scheme을 $\Sch_{/S}$로 제한하는 것에 해당하며, 따라서 절대적인 경우와 상대적인 경우가 하나의 틀 안에서 통일적으로 다루어진다. 이 상대적인 틀 위에서 각각의 test scheme $T$마다 $S$-scheme $G$의 점들의 집합 $G(T)$가 group을 이루고 그 구조가 $T$에 대해 자연스럽기를 요구하면 group scheme의 개념을 얻는다. 

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic geometry*. Graduate texts in mathematics. Springer, 1977.  
**[Vak]** R. Vakil, *The rising sea: Foundations of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/).  
**[GD]** A. Grothendieck, J. Dieudonné, *Éléments de géométrie algébrique I*. Springer, 1971.  
**[Mum]** D. Mumford, *The red book of varieties and schemes*. Lecture notes in mathematics. Springer, 1999.  
**[EH]** D. Eisenbud, J. Harris, *The geometry of schemes*. Graduate texts in mathematics. Springer, 2000.

---
