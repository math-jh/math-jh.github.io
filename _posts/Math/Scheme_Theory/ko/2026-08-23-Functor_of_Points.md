---
title: "점함자"
description: "스킴을 그 점함자로 바라보는 관점을 Yoneda 보조정리와 representable functor의 언어로 정리하고, 아핀공간·사영공간·Grassmannian·올곱 등 주요 함자들을 살펴본다."
excerpt: "Functor of points, Yoneda embedding, representability, fiber products"

categories: [Math / Scheme Theory]
permalink: /ko/math/scheme_theory/functor_of_points
sidebar: 
    nav: "scheme_theory-ko"

date: 2026-08-23
weight: 22
drift_needed: true
---

이제 우리는 스킴의 언어를 더 확장하기 위한 준비를 시작한다. 이를 위해서는 [§스킴 사이의 사상, ⁋정의 6](/ko/math/scheme_theory/morphism_of_schemes#def6)에서 살펴보았던 functor of points 관점이 필요하다. 이는 [§스킴 사이의 사상, ⁋정의 9](/ko/math/scheme_theory/morphism_of_schemes#def9)에서 이미 정의했던 것으로, scheme $X$를 살펴보기 위해 모든 가능한 test scheme $T$에 대하여 $X$의 $T$-point들의 모임을 보는 것이다. 즉, 다음의 functor

$$h_X=\Hom_\Sch(-,X): \Sch^\op \rightarrow \Set$$

를 생각하는 것이다. 우리의 첫째 목표는 이 functor가 $X$를 isomorphism까지 완전히 결정한다는 것을 Yoneda 보조정리를 통해 확인하고, 이러한 functorial한 관점이 affine space, projective space, Grassmannian, fiber product 등을 다룰 때 어떻게 자연스러운 언어를 제공하는지를 살펴본다.

본격적인 논의를 시작하기 전에 표기를 고정하자. 각각의 scheme $T$에 대하여 $h_X(T)=\Hom_\Sch(T,X)$를 $X(T)$로 적으며, scheme morphism $\tau: T' \rightarrow T$에 대하여 $h_X(\tau): X(T) \rightarrow X(T')$은 합성 $h_X(\tau)(\psi)=\psi\circ \tau$을 의미한다. 특히 $T=\Spec A$인 경우 $X(\Spec A)$를 간단히 $X(A)$로 적으며, 위에서 정의했던 것과 같이 집합 $X(T)$의 원소를 *$T$-valued point*라고도 부른다. 그럼 이 이름 하에서 $X(\tau)$는 $X$의 $T$-point를 $\tau$를 따라 $T'$-point로 끌어당기는 것과 같다. 

한편 functoriality는 $X$ 방향에도 존재한다. Scheme morphism $\varphi: X\rightarrow Y$가 주어졌을 때, 고정된 test scheme $T$에 대하여 합성

$$h_\varphi(T): X(T) \rightarrow Y(T);\qquad \psi\mapsto \varphi\circ \psi$$

은 잘 정의되며, 뿐만 아니라 임의의 $\tau: T' \rightarrow T$에 대하여 $h_\varphi(T')\circ h_X(\tau)=h_Y(\tau)\circ h_\varphi(T)$가 성립한다. 즉 $\varphi$는 natural transformation $h_\varphi: h_X \rightarrow h_Y$를 유도하고, 이로부터 $X\mapsto h_X$가 functor

$$h_{(-)}:\Sch \rightarrow \Fun(\Sch^\op, \Set)$$

를 정의한다는 것을 안다. 이 관점은 $\Sch_{/S}$로 우리의 관심의 대상을 바꾸어도 그대로 성립하지만, 이번 글에서는 편의상 $\Sch$에서 모든 일을 진행하기로 한다. 

## Yoneda 보조정리와 representability

이제 우리는 $X$가 정의하는 functor of points $h_X$가 실제로 $X$에 대한 충분한 scheme-theoretic 정보를 가지고 있다는 것을 보인다. 이는 기본적으로 범주론에서 이미 다룬 것으로, 여기서는 간단한 리뷰만 진행하기로 한다. 

Functor of points 관점의 범주론적 기초는 당연히 Yoneda 보조정리와 representability로, [\[범주론\] §표현가능한 함자, ⁋정리 4](/ko/math/category_theory/representable_functors#thm4)를 $\mathcal{A}=\Sch$에 적용하면 functor $h_{(-)}:\Sch \rightarrow \Fun(\Sch^\op, \Set)$이 fully faithful functor임을 안다. 이는 scheme $X$가 $h_X$에 의해 up to isomorphism으로 유일하게 결정되고, scheme morphism은 functor of points 사이의 natural transformation과 정확히 같은 데이터임을 보여준다.

위에서 살펴봤듯, scheme morphism $\varphi:X\rightarrow Y$가 주어지면, $T$-point $\psi:T\rightarrow X$를 합성 $\varphi\circ\psi:T\rightarrow Y$로 보낼 수 있다. 이러한 방식으로 $\varphi$는 모든 test scheme에 걸쳐 호환되는 map $X(T)\rightarrow Y(T)$들을 준다. 핵심적인 관찰은 이것이 거꾸로도 작동한다는 것이다. 이러한 호환되는 map들의 모임 $\alpha_T:X(T)\rightarrow Y(T)$가 주어졌다고 하자. $\alpha_X$가 identity morphism $\id_X:X\rightarrow X$에 보내는 원소 $\alpha_X(\id_X)$는 $Y$의 $X$-point, 곧 scheme morphism $f:X\rightarrow Y$이다. Naturality에 의하여 임의의 $\psi:T\rightarrow X$에 대하여 $\alpha_T(\psi)=f\circ\psi$가 성립하므로, 나머지 모든 $T$-point에서의 map은 $f$와의 합성으로 강제된다. 즉 functor of points 사이의 natural transformation은 하나의 scheme morphism과 정확히 같은 데이터이다.

그렇다면 presheaf $F:\Sch^\op\rightarrow\Set$이 실제로 어떤 scheme의 functor of points로 나타나기 위한 조건은 $F$가 representable functor인 것이다. ([\[범주론\] §표현가능한 함자, ⁋정의 1](/ko/math/category_theory/representable_functors#def1)) Isomorphism $F\cong h_X$가 주어지면 $X$ 위에는 $h_X(X)$의 $\id_X$에 대응하는 universal element가 주어지며, 임의의 scheme morphism $f:T\rightarrow X$는 이를 $T$ 위로 pullback하여 $F(T)$의 원소를 준다. 이는 [\[대수적 위상수학\] §분류공간, ⁋정리 8](/ko/math/algebraic_topology/classifying_spaces#thm8)에서 classifying map $f:B\rightarrow \B G$가 universal bundle을 pullback하여 $B$ 위의 principal $G$-bundle을 주는 것과 같은 방식이지만, 차이는 여기서는 homotopy class 대신 실제 scheme morphism $f:T\rightarrow X$ 자체가 나타난다는 것이다.

## Functor로 본 affine space와 projective space

이제 우리는 이 관점으로 우리가 이미 알고 있는 기하학적 대상들을 살펴본다. 그 시작점은 당연히 affine space와 projective space이다. 

::: 명제 1
$\mathbb{Z}$ 위의 affine line $\mathbb{A}^1=\Spec \mathbb{Z}[\x]$와 임의의 scheme $T$에 대하여, $\mathbb{A}^1$의 $T$-point들의 집합은

$$\mathbb{A}^1(T)\cong \Gamma(T, \mathcal{O}_T)=\mathcal{O}_T(T)$$

로 주어지며, 이 대응은 $T$에 대해 natural하다. 
:::
::: 증명
[§아핀스킴, ⁋정리 13](/ko/math/scheme_theory/affine_schemes#thm13)에서 살펴본 adjunction

$$\Hom_\Sch(T, \Spec A)\cong \Hom_\cRing(A, \Gamma(T, \mathcal{O}_T))$$

에서 $A=\mathbb{Z}[\x]$로 두자. Ring $\mathbb{Z}[\x]$는 $\cRing$에서 free object이므로, ring homomorphism $\mathbb{Z}[\x] \rightarrow \Gamma(T, \mathcal{O}_T)$은 generator $\x$의 image $\x\mapsto a$를 자유롭게 정하는 것과 같고, 이는 정확히 원소 $a\in \Gamma(T, \mathcal{O}_T)$를 하나 고르는 것이다. 따라서

$$\mathbb{A}^1(T)=\Hom_\Sch(T, \Spec \mathbb{Z}[\x])\cong \Hom_\cRing(\mathbb{Z}[\x], \Gamma(T, \mathcal{O}_T))\cong \Gamma(T, \mathcal{O}_T)$$

이다. 이 대응의 naturality는 임의의 $\tau: T' \rightarrow T$에 대하여 restriction map $\Gamma(T, \mathcal{O}_T) \rightarrow \Gamma(T', \mathcal{O}_{T'})$이 위의 대응과 commute한다는 것으로, adjunction의 naturality로부터 따라온다. 
:::

이전 절에서 도입한 언어를 도입하자면, $\mathbb{A}^1$은 global section functor $T\mapsto\Gamma(T,\mathcal{O}_T)$를 represent하는 것이다. 이 때 universal element는 $h_{\mathbb{A}^1}(\mathbb{A}^1)=\Hom_\Sch(\mathbb{A}^1,\mathbb{A}^1)$ 안에서 identity morphism $\id_{\mathbb{A}^1}$에 대응되는 것으로, 위의 [명제 1](#prop1)의 대응을 쫓아가보면 이는 $\Gamma(\mathbb{A}^1,\mathcal{O}_{\mathbb{A}^1})=\mathbb{Z}[\x]$ 안의 $\x$에 대응한다는 것을 안다. 

이제 임의의 scheme morphism $f:T\rightarrow\mathbb{A}^1$는 pullback map $f^\ast:\Gamma(\mathbb{A}^1,\mathcal{O}_{\mathbb{A}^1})\rightarrow\Gamma(T,\mathcal{O}_T)$을 통해 $T$ 위에 정의된 (global) regular function $f^\ast \x$를 정의한다. 거꾸로, 임의의 global regular function $a\in\Gamma(T,\mathcal{O}_T)$가 주어지면 $\x\mapsto a$로 정해지는 ring homomorphism $\mathbb{Z}[\x]\rightarrow\Gamma(T,\mathcal{O}_T)$가 있고, 바로 이 선택이 유일한 scheme morphism $f:T\rightarrow\mathbb{A}^1$를 주며 이러한 $f$는 $f^\ast\x=a$를 만족한다. 이를 $n$개의 generator로 일반화하면 다음을 얻는다. 

::: 명제 2
$\mathbb{Z}$ 위의 affine $n$-space $\mathbb{A}^n=\Spec \mathbb{Z}[\x_1,\ldots, \x_n]$에 대하여, 자연스러운 일대일대응

$$\mathbb{A}^n(T)\cong \Gamma(T, \mathcal{O}_T)^n$$

이 존재한다. 즉 $\mathbb{A}^n$의 $T$-point는 $T$ 위의 regular function $n$개의 순서쌍이다. 
:::
::: 증명
[명제 1](#prop1)의 증명과 동일하게, free ring $\mathbb{Z}[\x_1,\ldots, \x_n]$에서 나가는 ring homomorphism은 각 generator $\x_i$의 image $a_i\in \Gamma(T, \mathcal{O}_T)$를 자유롭게 정하는 것이므로

$$\mathbb{A}^n(T)\cong \Hom_\cRing(\mathbb{Z}[\x_1,\ldots, \x_n], \Gamma(T, \mathcal{O}_T))\cong \Gamma(T, \mathcal{O}_T)^n$$

을 얻는다. 
:::

특별히 $T=\Spec A$인 경우 $\mathbb{A}^n(A)\cong A^n$이며, 이는 고전적인 직관과 정확히 일치한다. 즉 affine $n$-space의 $A$-point는 $A$의 원소 $n$개로 이루어진 좌표이다. 더 일반적으로 만일 $T$가 affine이 아닌 경우에는 $\Gamma(T,\mathcal{O}_T)$이 더 풍부할 수 있으므로, $\mathbb{A}^n(T)$ 역시 고전적인 좌표보다 더 많은 정보를 담는다. 한편 global section functor에서 곱셈에 대한 가역원만을 추출하면 다음 functor를 얻는다. 

::: 명제 3
$\mathbb{G}_m=\Spec \mathbb{Z}[\t, \t^{-1}]$에 대하여, 자연스러운 일대일대응

$$\mathbb{G}_m(T)\cong \Gamma(T, \mathcal{O}_T)^\times$$

이 존재한다. 여기에서 $\Gamma(T, \mathcal{O}_T)^\times$은 ring $\Gamma(T, \mathcal{O}_T)$의 가역원들의 group이다. 
:::
::: 증명
$\mathbb{Z}[\t, \t^{-1}]=\mathbb{Z}[\t]_\t$이므로, ring homomorphism $\mathbb{Z}[\t, \t^{-1}] \rightarrow \Gamma(T, \mathcal{O}_T)$은 $\t$의 image $a$가 가역인 것들과 일대일대응한다. 실제로 localization의 universal property에 의하여 $\mathbb{Z}[\t]_\t$에서 나가는 ring homomorphism은 $\t$의 image를 가역원으로 보내는 $\mathbb{Z}[\t] \rightarrow \Gamma(T, \mathcal{O}_T)$들과 정확히 대응하고, [명제 1](#prop1)에서 본 것처럼 이는 가역원 $a\in \Gamma(T, \mathcal{O}_T)^\times$를 하나 고르는 것이다. 
:::

이를 사용하면 affine space로부터 projective space를 얻어낼 수 있다. 이를 위해 $\mathbb{A}^{n+1}$에서 원점을 제거한 open subscheme $U$를 생각하자. 먼저 scheme morphism

$$\mu:\mathbb{G}_m\times\mathbb{A}^{n+1}\rightarrow\mathbb{A}^{n+1}$$

을 다음의 식

$$\mathbb{Z}[\x_0,\ldots,\x_n]\rightarrow\mathbb{Z}[\t,\t^{-1},\x_0,\ldots,\x_n];\qquad \x_i\mapsto\t\x_i$$

으로 정의한다. 그럼 이는 $\mathbb{G}_m$의 scalar multiplication action이며 $U$ 위에도 제한된다. 고전적으로 projective space는 이 action에 대한 몫 $U/\mathbb{G}_m$으로 생각되었다.

이를 $T$-point들에서 살펴보면, [명제 3](#prop3)에 의하여 $\mathbb{G}_m(T)=\Gamma(T,\mathcal{O}_T)^\times$이므로, 위 action은 $T$-point에서 가역함수 $u$가 tuple $(a_0,\ldots,a_n)\in U(T)$에

$$u\cdot(a_0,\ldots,a_n)=(ua_0,\ldots,ua_n)$$

로 작용하는 것으로 생각할 수 있다. 여기서 각각의 $a_i$들은 $T$ 위에 정의된 함수들로서, $T$의 임의의 점 $t$에서의 tuple $(a_0(t),\ldots, a_n(t))$이 영벡터가 되지 않아야 한다. 

자연스러운 기대는 $\mathbb{P}^n(T)=U(T)/\mathbb{G}_m(T)$일 것이지만, 이것이 성립하지는 않는다. 실제로 이러한 tuple $(a_0,\ldots, a_n)\in U(T)$에 대하여, 

$$T_i=\{t\in T\mid \text{$a_i(t)$ invertible}\}$$

이 $T$의 open subscheme들이 되며, $T_i$ 위에서는 비율 $a_j/a_i$가 항상 정의되므로 다음의 식

$$\mathbb{Z}[\x_0/\x_i,\ldots, \x_n/\x_i]\rightarrow \Gamma(T_i, \mathcal{O}_T);\qquad \x_j/\x_i\mapsto a_j/a_i$$

을 통해 각각의 morphism $T_i\rightarrow D_+(\x_i)$이 정의되며, 이들은 교집합 위에서 일치하여 하나의 morphism $T\rightarrow\mathbb{P}^n$으로 붙는다. 뿐만 아니라 $\mathbb{G}_m(T)$-action은 비율 $a_j/a_i$를 바꾸지는 않으므로, 대응 $U(T)/\mathbb{G}_m(T)\rightarrow\mathbb{P}^n(T)$이 얻어진다는 사실 자체는 자연스럽다.

문제는 이 대응이 일반적으로 전사가 아니라는 것으로, 그 이유는 $\psi: T \rightarrow \mathbb{P}^n$의 image가 $\mathbb{P}^n$의 여러 chart에 걸쳐 있을 때 homogeneous coordinate를 고르는 방식이 chart마다 달라질 수 있기 때문이다. 구체적으로 morphism $\psi:T\rightarrow\mathbb{P}^n$이 주어지면 $V_i=\psi^{-1}(D_+(\x_i))$들이 $T$의 open cover를 이루고, 각각의 $V_i$ 위에서는 $i$번째 coordinate가 $1$이 되도록 맞춘 tuple

$$a^{(i)}=(\psi^\ast(\x_0/\x_i),\ldots, \psi^\ast(\x_n/\x_i))\in U(V_i)$$

이 정의되며 서로 다른 두 chart를 연결하는 transition relation은

$$a^{(i)}=\psi^\ast(\x_j/\x_i)\cdot a^{(j)}$$

로 주어진다. 문제는 이 때의 factor $\psi^\ast(\x_j/\x_i)$는 $V_i\cap V_j$ 위에서만 정의된 가역함수인 반면, 위에서 $T_i$들을 붙일 때 고려했던 factor는 $\mathbb{G}_m(T)$, 즉 global scaling factor에서 왔다는 것이다. 따라서 단순히 $\mathbb{P}^n(T)=U(T)/\mathbb{G}_m(T)$라 생각하면 이러한 $T$-point들을 놓치게 된다. 

한편 우리는 마침 이러한 경우마다 국소적으로 scaling factor를 담을 수 있는 방법을 잘 알고 있다. 즉 $T$ 위에 정의된 line bundle을 생각하면 된다. 이렇게 얻어지는 line bundle $\mathcal{L}$ 위에서 국소적인 tuple들의 coordinate는 global section $n+1$개 $s_0,\ldots, s_n\in \Gamma(T, \mathcal{L})$으로 합쳐지고, $a^{(i)}$의 $i$번째 coordinate가 $1$이었다는 것은 $V_i$ 위에서 $s_i$가 $\mathcal{L}$을 생성한다는 뜻이 된다. 이 때 우리는 이 비율을 잘 정의하기 위해 다음의 조건을 요구하여야 한다. 

::: 정의 4
Scheme $T$ 위의 line bundle $\mathcal{L}$의 *globally generating sections<sub>전역생성단면</sub>* $s_0,\ldots, s_n\in \Gamma(T, \mathcal{L})$이라는 것은, 각각의 점 $t\in T$에서 stalk $\mathcal{L}_t$이 germ $(s_0)_t,\ldots, (s_n)_t$로 $\mathcal{O}_{T,t}$-module로서 생성되는 것이다. 두 데이터 $(\mathcal{L}, s_0,\ldots, s_n)$과 $(\mathcal{L}', s_0',\ldots, s_n')$이 *isomorphic*하다는 것은, $\mathcal{O}_T$-module isomorphism $\theta:\mathcal{L} \rightarrow \mathcal{L}'$이 존재하여 각각의 $i$에 대하여 $\theta(s_i)=s_i'$인 것이다. 
:::

이 isomorphism 조건이 homogeneous coordinate의 scaling을 기록한다. 특히 $\mathcal{L}=\mathcal{O}_T$인 경우, $\mathcal{O}_T$의 automorphism은 가역함수 $u\in\Gamma(T,\mathcal{O}_T)^\times$를 곱하는 것뿐이다. 따라서 $(\mathcal{O}_T,s_0,\ldots,s_n)$와 $(\mathcal{O}_T,us_0,\ldots,us_n)$은 isomorphic한 data이다.

그럼 이 정의 하에서 $\mathbb{P}^n$의 functor of points는 다음과 같이 깔끔하게 기술된다. 

::: 정리 5
$\mathbb{Z}$ 위의 projective space $\mathbb{P}^n=\Proj \mathbb{Z}[\x_0,\ldots, \x_n]$에 대하여, $\mathbb{P}^n(T)$는 $T$ 위의 line bundle $\mathcal{L}$과 그 globally generating sections $s_0,\ldots, s_n\in \Gamma(T, \mathcal{L})$의 데이터 $(\mathcal{L}, s_0,\ldots, s_n)$들의 isomorphism class와 자연스럽게 일대일대응한다. 
:::
::: 증명
Morphism $\psi: T \rightarrow \mathbb{P}^n$이 주어졌다 하자. $\mathbb{P}^n$ 위의 twisting sheaf $\mathcal{O}_{\mathbb{P}^n}(1)$은 line bundle이고 그 global sections $\x_0,\ldots, \x_n$은 globally generating sections이므로, pullback을 취하여 $T$ 위의 line bundle $\mathcal{L}=\psi^\ast \mathcal{O}_{\mathbb{P}^n}(1)$과 sections $s_i=\psi^\ast \x_i$를 얻는다. Pullback이 globally generating sections인 성질을 보존하므로 $(\mathcal{L}, s_0,\ldots, s_n)$은 위의 데이터를 이룬다. 

거꾸로 $T$ 위의 line bundle $\mathcal{L}$과 그 globally generating sections $s_0,\ldots, s_n$이 주어졌다 하자. 각각의 $i$에 대하여 section $s_i$가 생성하는 곳 $T_{s_i}=\{t\in T\mid (s_i)_t \text{ generates } \mathcal{L}_t\}$는 열린집합이고, sections가 $\mathcal{L}$을 globally generate하므로 $\{T_{s_i}\}_{i=0}^n$은 $T$의 open cover를 이룬다. $T_{s_i}$ 위에서는 $s_i$가 $\mathcal{L}\vert_{T_{s_i}}$의 trivialization을 주므로, 각 $j$에 대하여 $s_j/s_i\in \Gamma(T_{s_i}, \mathcal{O}_T)$가 잘 정의된다. 이로써 [§스킴 사이의 사상, ⁋예시 5](/ko/math/scheme_theory/morphism_of_schemes#ex5)와 같은 방식으로 $T_{s_i} \rightarrow D_+(\x_i)$를 정의하고, 교집합 위에서의 gluing condition을 확인하여 morphism $\psi: T \rightarrow \mathbb{P}^n$을 얻는다. 

이 두 구성이 서로 역이라는 것과 isomorphic한 데이터가 같은 morphism을 준다는 것은, $(\mathcal{L}, s_0,\ldots, s_n)$ 전체를 $\mathcal{O}_T$-module isomorphism으로 옮겨도 $s_j/s_i$들이 변하지 않으므로 같은 gluing 데이터를 준다는 사실로부터 확인된다. 자연스러움은 $\tau: T' \rightarrow T$에 대하여 위의 데이터를 pullback하는 것과 morphism을 합성하는 것이 일치한다는 것이다. 
:::

구체적으로 [§다양체에서 스킴으로, ⁋예시 5](/ko/math/scheme_theory/from_varieties_to_schemes#ex5)에서 살펴본 $\mathbb{P}^n_\mathbb{K}$의 $\mathbb{K}[\epsilon]/(\epsilon^2)$-point를 이 언어로 다시 살펴보자. 이는 one-point space이므로 그 위의 line bundle은 trivial line bundle 뿐이며, 따라서 trivialization을 하나 고정하면 $\Gamma(T,\mathcal{L})\cong\Gamma(T,\mathcal{O}_T)=A$이므로 이 위의 line bundle의 section을 고르는 것은 $A$의 원소를 고르는 것과 같다. 한편 이들이 globally generating이라는 조건은, $\Spec A$의 유일한 점에서 stalk이 $A$ 자신이므로, 어떤 $a_i$가 가역이라는 조건이 되어 정확히 $(a_0,\ldots, a_n)\in U(A)$라는 조건이 된다. 

이제 [정리 5](#thm5)가 어떻게 작동하는지 보기 위해 그 isomorphism class를 살펴보면, $\mathcal{O}_T$의 automorphism은 이제 $A^\times$의 원소를 곱하는 것뿐이므로 두 tuple이 같은 $A$-point를 주는 것은 서로 $A^\times$배인 것과 동치이다. 따라서

$$\mathbb{P}^n(A)=U(A)/A^\times$$

이며, 여기서 $U(A)$는 각 좌표가 $A$인 $(n+1)$-tuple $(a_0, \ldots, a_n)$ 중 적어도 한 좌표가 가역인 것이고 $A^\times$는 모든 성분에 $A^\times$의 원소를 곱하는 것으로 얻어진다. 

이제 $V=\mathbb{K}^{n+1}$이라 하고, $U(A)$의 원소를 $a=b+\epsilon c$의 형태로 쓰자. 그럼 다음 대응

$$\widetilde{\rho}: U(A)\rightarrow \mathbb{P}^n(\mathbb{K});\qquad b+\epsilon c\mapsto [b]$$

을 생각할 수 있다. 직관적으로 이는 tangent vector 방향은 잊어버리고 그 base point만 기억하는 함수이다. 원소 $u=\lambda+\epsilon\mu\in A^\times$를 $\lambda\in\mathbb{K}^\times$, $\mu\in\mathbb{K}$로 쓰면 $U(A)$ 위의 $A^\times$ action은

$$u(b+\epsilon c)=\lambda b+\epsilon(\lambda c+\mu b)$$

이므로 이러한 $\widetilde{\rho}$는 $\rho: \mathbb{P}^n(A)\rightarrow \mathbb{P}^n(\mathbb{K})$으로 떨어진다. 

이렇게 얻은 $\rho$는 실제로 ring homomorphism 

$$q:A\rightarrow\mathbb{K};\qquad \epsilon\mapsto0$$

으로부터 functorial하게 유도되는 map이다. 즉, 이 ring homomorphism에 대응하는 morphism을 $\iota:\Spec\mathbb{K}\rightarrow\Spec A$라 하면, $\rho$는 $A$-point $\psi:\Spec A\rightarrow\mathbb{P}^n$을 합성 $\psi\circ\iota$로 보낸다는 것을 확인할 수 있으며, 이것이 위에서 정의한 $\rho$와 정확히 일치하는 것을 확인할 수 있다.

따라서 $\rho^{-1}(\ell)$은 $\Spec\mathbb{K}\rightarrow\Spec A$를 따라 restriction했을 때 $\ell$이 되는 $A$-point들의 집합이다. 이를 직접 계산해보자. 우선 class $[b+\epsilon c]\in\rho^{-1}(\ell)$을 하나 택하면 $\ell=\mathbb{K}b\subseteq V$이고, 이 $A$-point로부터 $\mathbb{K}$-linear map

$$\phi:\ell\rightarrow V/\ell,\qquad \phi(b)=c+\ell$$

을 정의할 수 있다. 이는 representative의 선택에 의존하지 않는다. 실제로 앞선 계산을 활용하면, $b+\epsilon c$와 같은 class에 속하는 $\lambda b+\epsilon(\lambda c+\mu b)$의 경우, $\phi$를 통해 $\lambda b$가 옮겨지는 값은

$$(\lambda c+\mu b)+\ell=\lambda(c+\ell)$$

이 되기 때문이다. 거꾸로 일차원 부분공간 $\ell\subseteq V$와 linear map $\phi:\ell\rightarrow V/\ell$이 주어졌다고 하자. 영벡터가 아닌 $b\in\ell$을 택하고 $\phi(b)$의 lift $c\in V$를 택하면 $b+\epsilon c\in U(A)$를 얻는다. 이는 우선 $b$의 lift에 의존하지 않는 것으로, 만일 다른 lift $c'=c+\mu b$를 택하면 

$$b+\epsilon c'=(1+\epsilon\mu)(b+\epsilon c)$$

가 되어 이는 같은 $A^\times$-class에 속한다. 비슷하게 basis $b'=\lambda b$와 그 lift $c'=\lambda c+\mu b$를 택하면 

$$b'+\epsilon c'=(\lambda+\epsilon\mu)(b+\epsilon c)$$

이므로, 어떠한 선택에도 의존하지 않는 $A^\times$-class가 주어진다. 이는 위의 구성과 역과정인 것을 확인할 수 있으며, 따라서 다음의 isomorphism

$$\mathbb{P}^n(A)\cong\{(\ell,\phi)\mid \ell\in \mathbb{P}^n(\mathbb{K}),\ \phi\in \Hom_\mathbb{K}(\ell, V/\ell)\}$$

을 얻는다. 즉 $\mathbb{P}^n(A)$는 $\mathbb{P}^n$의 모든 점들에서의 tangent vector들을 모아둔 것이 되며, $\rho$는 그중 base point만 남기므로 $\rho^{-1}(\ell)$은 $\mathbb{P}^n$의 $\ell$에서의 tangent space $T_\ell\mathbb{P}^n$을 준다. 더 일반적으로 임의의 $\mathbb{K}$-scheme $X$에 대하여 $X(A)$는 모든 $\mathbb{K}$-point에서의 tangent space들을 모은 집합이다.

::: 예시 6
이제 우리는 위에서 살펴본 projective space가 정의하는 functor를 구체적으로 살펴본다. 우선 $\mathbb{P}^n(T)$를 나타내는 $\mathcal{L}$과 globally generating sections $s_0,\ldots, s_n$은 다음의 surjection

$$\mathcal{O}_T^{\oplus n+1}\twoheadrightarrow \mathcal{L};\qquad e_i\mapsto s_i$$

으로 다시 쓸 수 있다. 이제 이러한 surjection들 사이의 isomorphism을 다음의 diagram

{% diagram Math/Scheme_Theory/Functor_of_Points-1.svg width="11.42em" alt="isomorphic_surjections" %}

으로 정의하고, $T\in\Sch$를 받아 이러한 isomorphism class를 대응시키는 functor $F_{n+1}$을 생각하자. 이 때 functoriality는 morphism의 단계에서는, $\tau:T'\rightarrow T$를 통해 surjection을 pullback하여 

$$\mathcal{O}_{T'}^{\oplus n+1}\twoheadrightarrow\tau^\ast\mathcal{L}$$

을 정의하는 방식으로 주어진다. 즉,  이 대응은 contravariant functor

$$F_{n+1}:\Sch^\op\rightarrow\Set$$

를 정의한다. 이 관점에서 [정리 5](#thm5)는 모든 scheme $T$에 대하여 natural한 일대일대응

$$\mathbb{P}^n(T)\cong F_{n+1}(T)$$

이 존재한다는 것이며, projective space $\mathbb{P}^n$이 이 functor를 represent한다. [\[범주론\] §표현가능한 함자, ⁋정리 4](/ko/math/category_theory/representable_functors#thm4)에 의하여 $\id_{\mathbb{P}^n}$에 대응하는 universal element는 $\mathbb{P}^n$ 위의 quotient bundle

$$\mathcal{O}_{\mathbb{P}^n}^{\oplus n+1}\twoheadrightarrow\mathcal{O}_{\mathbb{P}^n}(1)$$

이고, 임의의 $T$-point는 이 universal quotient를 $T$ 위로 pullback하여 rank $1$ quotient를 얻는다.

Grassmannian은 위 functor에서 rank $1$ target을 rank $k$ target으로 바꾸어 얻는다. 즉 정수 $0<k<n$에 대하여 scheme $T$에 집합

$$F_{k,n}(T)=\left\{\mathcal{O}_T^n\twoheadrightarrow\mathcal{Q}\mid \mathcal{Q}\text{ is locally free of rank }k\right\}\big/\cong$$

를 대응시키고, morphism $\tau:T'\rightarrow T$에는 pullback을 대응시킨다. 이 contravariant functor를 represent하는 scheme을 $\Gr(k,n)$이라 하므로, 모든 scheme $T$에 대하여 natural한 일대일대응

$$\Gr(k,n)(T)\cong F_{k,n}(T)$$

이 존재한다.

$T=\Spec\mathbb{K}$인 경우 $F_{k,n}(T)$의 원소는 rank $k$ quotient space $\mathbb{K}^n\twoheadrightarrow Q$이다. 이는 kernel인 $(n-k)$차원 부분공간 $\bar S\subseteq\mathbb{K}^n$에 의하여 유일하게 결정되므로, $\Gr(k,n)(\mathbb{K})$는 이러한 부분공간들의 집합과 일치한다. 부분공간을 직접 분류하는 [\[대수다양체\] §그라스만 다양체, ⁋정의 1](/ko/math/algebraic_varieties/grassmannians#def1)의 관례에서는 이 집합을 $\Gr(n-k,n)$으로 표기한다. 특히 $k=1$이면 rank $1$ quotient를 분류하므로 [정리 5](#thm5)의 $\mathbb{P}^{n-1}$을 회복한다.

:::

이러한 functorial한 정의가 representable함을 보이는 것이 moduli theory의 출발점이며, Grassmannian의 경우에는 quotient bundle이 standard affine chart들 위에서 행렬의 data로 표현된다는 사실을 이용하여 representing scheme과 universal quotient를 구성할 수 있다.

## Functor로 본 올곱

Functor of points 관점은 [§올곱, ⁋정의 1](/ko/math/scheme_theory/fiber_products#def1)에서 정의한 fiber product와 잘 맞아떨어진다. Fiber product $X\times_S Y$의 universal property는, 임의의 test scheme $T$에 대하여 그 $T$-point들이 어떻게 결정되는지를 functor 수준에서 곧바로 말해준다. 

::: 명제 7
Scheme morphism $X \rightarrow S$와 $Y \rightarrow S$가 주어졌다 하자. 그럼 임의의 scheme $T$에 대하여, 자연스러운 일대일대응

$$(X\times_S Y)(T)\cong X(T)\times_{S(T)} Y(T)$$

이 존재한다. 여기서 우변은 $\Set$에서의 fiber product, 즉 $X(T)\times Y(T)$에서 $X(T) \rightarrow S(T)$와 $Y(T) \rightarrow S(T)$가 같은 값을 주는 순서쌍들의 집합이다. 
:::
::: 증명
[§올곱, ⁋정의 1](/ko/math/scheme_theory/fiber_products#def1)의 universal property는, $T$로부터 $X\times_S Y$로의 morphism이 $\psi_X: T \rightarrow X$와 $\psi_Y: T \rightarrow Y$로서 $S$로의 합성이 일치하는, 즉 $X(T) \rightarrow S(T)$와 $Y(T) \rightarrow S(T)$를 통해 $\psi_X$와 $\psi_Y$가 같은 $S$-point로 가는 순서쌍과 유일하게 대응한다는 것을 의미한다
. 이를 집합의 언어로 적으면 

$$(X\times_S Y)(T)\cong \{(\psi_X, \psi_Y)\in X(T)\times Y(T)\mid \psi_X, \psi_Y \text{ map to the same element of } S(T)\}=X(T)\times_{S(T)} Y(T)$$

이다. Naturality는 $\tau: T' \rightarrow T$에 대하여 양변의 pullback이 일치한다는 것으로, universal property의 naturality으로부터 따라온다. 
:::

[명제 7](#prop7)은 fiber product를 functor 수준에서 <em-ko>점별로</em-ko> fiber product를 취하는 연산으로 해석하게 해준다. 이 관점에서 [§올곱, ⁋정리 8](/ko/math/scheme_theory/fiber_products#thm8)의 존재성 증명은, 점별로 자명하게 정의되는 functor $T\mapsto X(T)\times_{S(T)} Y(T)$가 representable임을 보이는 일로 재해석된다. 특히 product $X\times Y=X\times_{\Spec \mathbb{Z}} Y$의 경우에는 단순히 $(X\times Y)(T)\cong X(T)\times Y(T)$이 된다. 

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic geometry*. Graduate texts in mathematics. Springer, 1977.  
**[Vak]** R. Vakil, *The rising sea: Foundations of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/).  

---
