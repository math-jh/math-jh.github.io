---
title: "스킴 사상의 성질들"
description: "스킴 사상의 주요 성질들을 정의하고, 준옹골사상과 준분리사상의 개념 및 기본 성질을 소개한 뒤 rational map과 birational map을 정의한다."
excerpt: "Affine, finite, finite type 등 scheme morphism의 기본 성질과 rational map"

categories: [Math / Scheme Theory]
permalink: /ko/math/scheme_theory/properties_of_scheme_morphisms
sidebar: 
    nav: "scheme_theory-ko"

date: 2025-02-21
weight: 9
---

앞선 글에서 우리는 scheme morphism을 이해하는 몇 가지 관점을 살펴보았다. 이번 글에서 우리는 본격적으로 scheme morphism이 갖는 성질들을 정의한다. 우선 이들이 공유하는 다음 성질을 정의한다.

::: 정의 1
Scheme morphism의 성질 $P$가 *local on target*이라는 것은 다음 두 조건이 성립하는 것이다. 
1. 만일 scheme morphism $\varphi:X \rightarrow Y$가 $P$를 만족할 경우, $Y$의 임의의 open subscheme $V$에 대하여 scheme morphism $\varphi\vert_{\varphi^{-1}(V)}: \varphi^{-1}(V) \rightarrow V$ 또한 $P$를 만족한다. 
2. 만일 scheme morphism $\varphi:X \rightarrow Y$에 대하여, $Y$의 open covering $\{V_j\}$가 존재하여 $\varphi\vert_{\varphi^{-1}(V_j)}: \varphi^{-1}(V_j) \rightarrow V_j$가 모두 $P$를 만족한다면 $\varphi$ 또한 그러하다. 
:::

Scheme은 affine scheme으로부터 만들어진다. Scheme morphism의 성질 $P$가 local on target이라면, scheme morphism $\varphi:X \rightarrow Y$의 target $Y$를 $\Spec B$로 가정하여도 되고, 그럼 adjoint

$$\Hom_\Sch(X, \Spec B)\cong \Hom_\cRing(B, \Gamma(X, \mathcal{O}_X))$$

를 통해 우리는 언제나 target이 affine인 경우로 환원할 수 있다. 

## 준옹골사상과 준분리사상

::: 정의 2
Scheme morphism $\varphi: X \rightarrow Y$가 *quasi-compact<sub>준옹골</sub>*이라는 것은 임의의 affine open subset $V\subseteq Y$가 주어질 때마다 $\varphi^{-1}(V)$가 quasi-compact인 것이다. 
:::

::: 명제 3
Scheme morphism $\varphi: X \rightarrow Y$가 quasi-compact인 것은 $Y$의 임의의 quasi-compact open subset의 preimage가 quasi-compact인 것과 동치이다. 
:::
::: 증명
임의의 affine scheme은 quasi-compact이므로 ([§스펙트럼, ⁋보조정리 12](/ko/math/scheme_theory/spectrums#lem12)) 주어진 조건이 [정의 2](#def2)의 조건을 함의하는 것은 당연하다.

거꾸로 quasi-compact morphism $\varphi: X \rightarrow Y$가 주어졌다 하자. 이제 $Y$의 임의의 quasi-compact open subset $V$가 주어졌다 하면, $V$를 덮는 유한히 많은 affine open subset들의 covering $\{V_j\}$가 존재하며 이들의 preimage $\varphi^{-1}(V_j)$는 모두 quasi-compact이다. 이제 

$$\varphi^{-1}(V)=\varphi^{-1}\left(\bigcup_{j\in J} V_j\right)=\bigcup_{j\in J}\varphi^{-1}(V_j)$$

이고 quasi-compact set의 유한한 합집합은 다시 quasi-compact이므로 원하는 결과를 얻는다. 
:::

그럼 [명제 3](#prop3)의 동치로부터, 임의의 quasi-compact morphism의 합성은 다시 quasi-compact임을 안다. 뿐만 아니라 다음이 성립한다.

::: 명제 4
Noetherian scheme $X$에 대하여, scheme morphism $\varphi: X \rightarrow Y$는 항상 quasi-compact이다. 
:::
::: 증명
임의의 affine open subset $V\subseteq Y$가 주어졌다 하고, $\varphi^{-1}(V)$가 quasi-compact임을 보여야 한다. 그런데 [\[위상수학\] §차원, ⁋명제 12](/ko/math/topology/dimension#prop12)와 [\[위상수학\] §차원, ⁋명제 13](/ko/math/topology/dimension#prop13)의 첫째 결과로부터 Noetherian인 위상공간의 임의의 부분공간은 quasi-compact이다.
:::

비슷하게 우리는 quasi-separated morphism을 정의한다. 이를 위해서는 quasi-separated scheme을 먼저 정의해야 한다.

::: 정의 5
Scheme $X$가 *quasi-separated<sub>준분리</sub>*인 것은 $X$의 임의의 두 quasi-compact open subset의 교집합이 다시 quasi-compact인 것이다. Scheme morphism $\varphi: X \rightarrow Y$가 *quasi-separated*인 것은 임의의 affine open set $V\subseteq Y$에 대하여, $\varphi^{-1}(V)$가 quasi-separated인 것이다. 
:::

그럼 다음이 성립한다.

::: 명제 6
Locally Noetherian scheme은 항상 quasi-separated이다. 
:::
::: 증명
Locally Noetherian scheme $X$의 임의의 두 affine open subset $V_1=\Spec B_1, V_2=\Spec B_2$가 주어졌다 하고 $V_1\cap V_2$가 quasi-compact임을 보여야 한다. 

우선 $X$가 locally Noetherian이므로, $X$를 Noetherian ring들의 spectrum $U_i=\Spec A_i$들로 덮을 수 있다. 이제 각각의 $i$에 대하여, [§스킴의 위상구조, ⁋보조정리 11](/ko/math/scheme_theory/topology_of_schemes#lem11)에 의하여 $U_i\cap V_1$을 Noetherian ring들의 spectrum $\Spec (A_i)_g$들로 덮을 수 있다. 이들을 모두 모으면 $V_1$을 Noetherian ring들의 spectrum들로 덮을 수 있으며, [§스펙트럼, ⁋보조정리 12](/ko/math/scheme_theory/spectrums#lem12)에 의해 $V_1=\Spec B_1$은 유한히 많은 Noetherian ring들의 spectrum으로 덮인다. 따라서 [§스킴의 위상구조, ⁋보조정리 13](/ko/math/scheme_theory/topology_of_schemes#lem13)에 의해 $B_1$은 Noetherian ring이고 따라서 $V_1=\Spec B_1$은 Noetherian이다. 다시  [\[위상수학\] §차원, ⁋명제 12](/ko/math/topology/dimension#prop12)와 [\[위상수학\] §차원, ⁋명제 13](/ko/math/topology/dimension#prop13)의 첫째 결과로부터 Noetherian인 위상공간의 임의의 부분공간은 quasi-compact이므로, 특히 $V_1\cap V_2$ 또한 quasi-compact이다. 같은 논리로 $X$의 임의의 affine open은 Noetherian이며, quasi-compact open은 유한 개의 affine open의 합집합이므로 역시 Noetherian이다. Noetherian 위상공간의 부분공간은 quasi-compact이므로 임의의 두 quasi-compact open의 교집합 또한 quasi-compact이고, 따라서 [정의 5](#def5)에 의하여 $X$는 quasi-separated이다. 
:::

그럼 quasi-compactness와 quasi-separatedness는 [정의 1](#def1)의 성질을 만족할 뿐만 아니라, 다음 명제에서 확인할 수 있듯이 *affine-local on target*이다. ([§스킴의 위상구조, ⁋정의 9](/ko/math/scheme_theory/topology_of_schemes#def9))

::: 명제 7
Scheme morphism $\varphi: X \rightarrow Y$에 대하여 다음이 성립한다.

1. 만일 $Y$의 affine open covering $\{V_j\}$가 존재하여 각각의 $\varphi^{-1}(V_j)$가 quasi-compact라면, $\varphi$는 quasi-compact이다. 
2. 만일 $Y$의 affine open covering $\{V_j\}$가 존재하여 각각의 $\varphi^{-1}(V_j)$가 quasi-separated라면, $\varphi$는 quasi-separated이다. 
:::
::: 증명
1. $Y$의 임의의 affine open subset $V$가 주어졌다 하자. 그럼 [§스킴의 위상구조, ⁋보조정리 11](/ko/math/scheme_theory/topology_of_schemes#lem11)에 의하여 $V$와 $V_j$ 각각에서 principal open set이 되는 열린집합들로 $V\cap V_j$를 덮을 수 있고, 이를 모든 $j$에 대해 고려한 후 $V$의 quasi-compactness를 사용하면 이러한 것들 중 유한히 많은 것만 택할 수 있다. 이를 $V=\bigcup W_l$이라 하자.   
    한편 각각의 $l$에 대하여 $W_l$을 principal open subset으로 갖는 $V_{j(l)}$을 택하면, $\varphi^{-1}(V_{j(l)})$는 quasi-compact이므로, 이를 유한히 많은 affine open subset들 $U_{j(l)k}$들로 덮을 수 있고, 이제 $\varphi^{-1}(W_l)\cap U_{j(l)k}$는 [§스펙트럼, ⁋명제 8](/ko/math/scheme_theory/spectrums#prop8)에 의해 $U_{j(l)k}$의 principal open set이므로 $\varphi^{-1}(W_l)$ 각각을 affine open set들의 유한한 합집합으로 표현할 수 있고, 따라서 $\varphi^{-1}(V)$도 affine open set들의 유한한 합집합으로 표현할 수 있다. 이제 quasi-compact space의 유한한 합집합은 quasi-compact이므로 원하는 결과를 얻는다.
2. 우선 scheme $Z$가 quasi-separated인 것은 $Z$의 임의의 두 affine open subset의 교집합이 quasi-compact인 것과 동치이다. Affine scheme은 quasi-compact이므로 한쪽 방향은 자명하고, 거꾸로 $Z$의 임의의 quasi-compact open subset은 유한히 많은 affine open subset의 합집합이므로 두 quasi-compact open subset의 교집합은 유한히 많은 affine끼리의 교집합의 합집합이 되어 quasi-compact이기 때문이다.     
    이제 첫째 결과의 증명에서와 같이 $V$의 유한한 covering $V=\bigcup_{l=1}^n W_l$을 택하여 각각의 $W_l$이 $V$에서도, 적당한 $V_{j(l)}$에서도 principal open subset이 되도록 하자. $\varphi^{-1}(V)$의 두 affine open subset $U_1,U_2$가 주어졌다 하면
    
    $$U_1\cap U_2=\bigcup_{l=1}^n\left(U_1\cap \varphi^{-1}(W_l)\right)\cap\left(U_2\cap \varphi^{-1}(W_l)\right)$$
    
    이다. 여기에서 $W_l$이 $V$의 principal open subset이므로 $U_1\cap \varphi^{-1}(W_l)$은 affine scheme $U_1$ 위에서 $W_l$을 정의하는 함수의 pullback이 정의하는 principal open set이고 ([§스펙트럼, ⁋명제 8](/ko/math/scheme_theory/spectrums#prop8)) 따라서 affine이며, $U_2$에 대해서도 마찬가지이다. 그런데 이들은 모두 $\varphi^{-1}(W_l)\subseteq \varphi^{-1}(V_{j(l)})$의 affine open subset이고 $\varphi^{-1}(V_{j(l)})$이 quasi-separated이므로, 위의 판정법에 의하여 각각의 교집합은 quasi-compact이다. 이상에서 $U_1\cap U_2$는 유한히 많은 quasi-compact set의 합집합이므로 quasi-compact이고, 다시 위의 판정법에 의하여 $\varphi^{-1}(V)$는 quasi-separated이다. 
:::

## 아핀사상

우리는 adjoint

$$\Hom_\Sch(X, \Spec B)\cong\Hom_\cRing (B, \Gamma(X, \mathcal{O}_X))$$

에서, 특별히 $X=\Spec A$인 경우 

$$\Hom_\Sch(\Spec A,\Spec B)\cong\Hom_\cRing (B, A)$$

가 성립하는 것을 안다. ([§아핀스킴, ⁋명제 11](/ko/math/scheme_theory/affine_schemes#prop11)) 따라서, 위와 같이 affine-local on target인 scheme morphism의 성질을 살펴볼 때에는, $Y$의 임의의 affine open subset $V\cong\Spec B$에 대하여 $U=\varphi^{-1}(V)$도 $X$의 open subscheme $U\cong \Spec A$이고, 따라서 $\varphi\vert_U: U \rightarrow V$가 affine scheme들 사이의 morphism이 되어 이 성질을 ring homomorphism 

$$(\varphi\vert_U)^\sharp(V): \mathcal{O}_V(V) \rightarrow \mathcal{O}_U(U)$$

으로부터 얻어낼 수 있으면 좋을 것이다. 그러나 물론 임의의 scheme morphism $\varphi: X \rightarrow Y$에 대하여, $Y$의 affine open subset의 preimage가 affine이 되지는 않는다. ([§스킴, ⁋예시 8](/ko/math/scheme_theory/schemes#ex8))

::: 정의 8
Scheme morphism $\varphi: X \rightarrow Y$가 *affine<sub>아핀</sub>*이라는 것은 $Y$의 임의의 affine open subset $V$에 대하여 $\varphi^{-1}(V)$가 $X$의 affine open subset인 것이다. 
:::

그럼 affine morphism의 합성이 affine인 것은 자명하다. 뿐만 아니라 이 성질은 [정의 1](#def1)의 성질 또한 만족하며, 그 증명은 다음 명제에서 한다. 

::: 명제 9
Scheme morphism $\varphi:X \rightarrow Y$에 대하여, 만일 $Y$의 affine open covering $\{V_j\}$가 존재하여 각각의 $\varphi^{-1}(V_j)$가 affine라면, $\varphi$는 affine이다. 
:::
::: 증명
$Y$의 affine open subset $\Spec B$에 대한 성질 $P$를 "$\varphi^{-1}(\Spec B)$가 $X$의 affine open subset이다"로 정의하자. 그럼 $\varphi$가 affine이라는 것은 $Y$의 임의의 affine open subset이 $P$를 만족하는 것이고 주어진 가정은 $Y$의 어떤 affine open covering이 $P$를 만족한다는 것이므로, [§스킴의 위상구조, ⁋보조정리 12](/ko/math/scheme_theory/topology_of_schemes#lem12)의 둘째 조건과 셋째 조건 사이의 동치에 의하여 $P$가 [§스킴의 위상구조, ⁋정의 9](/ko/math/scheme_theory/topology_of_schemes#def9)의 의미에서 affine-local property임을 보이면 충분하다. 이하에서 sheaf morphism $\varphi^\sharp: \mathcal{O}_Y \rightarrow \varphi_\ast \mathcal{O}_X$의 열린집합 $V$에서의 성분을 $\varphi^\sharp(V): \mathcal{O}_Y(V) \rightarrow \mathcal{O}_X(\varphi^{-1}(V))$로 적는다.

우선 [§스킴의 위상구조, ⁋정의 9](/ko/math/scheme_theory/topology_of_schemes#def9)의 첫째 조건을 확인하자. $\varphi^{-1}(\Spec B)$가 affine open subset $\Spec A$라 하면 [§아핀스킴, ⁋명제 11](/ko/math/scheme_theory/affine_schemes#prop11)에 의하여 $\Spec A \rightarrow \Spec B$는 적당한 ring homomorphism $\phi: B \rightarrow A$에 대해 $\Spec\phi$의 꼴이고, [§스펙트럼, ⁋명제 8](/ko/math/scheme_theory/spectrums#prop8)의 증명에서 얻어진 식

$$(\Spec\phi)^{-1}(D(f))=D(\phi(f))$$

으로부터 임의의 $f\in B$에 대하여 $\varphi^{-1}(\Spec B_f)=D(\phi(f))\cong\Spec A_{\phi(f)}$이므로 $\Spec B_f$ 또한 $P$를 만족한다.

이제 둘째 조건을 확인해야 한다. 즉 $B=(f_1,\ldots, f_r)$이고 각각의 $U_i=\varphi^{-1}(D(f_i))$가 affine이라 가정한 후, $U=\varphi^{-1}(\Spec B)$가 affine임을 보여야 한다. 편의상 $R=\Gamma(U, \mathcal{O}_X)$라 하고 $f_i$의 $\varphi^\sharp(\Spec B): B \rightarrow R$에 의한 image를 $g_i\in R$이라 하자. 또, $g\in \Gamma(U, \mathcal{O}_X)$에 대하여 $g$의 stalk이 $\mathcal{O}_{X,x}$의 maximal ideal에 속하지 <em-ko>않는</em-ko> 점 $x$들의 집합을 $U_g$로 적자. 그럼 $U$의 임의의 affine open subset $\Spec A$에 대하여 $U_g\cap \Spec A=D(g\vert_{\Spec A})$인 것이 정의에 의해 자명하고, 특히 $U_g$는 열린집합이다. 

다음의 세 가지를 관찰한다. 첫째로, $B=(f_1,\ldots, f_r)$이므로 $\Spec B=\bigcup_{i=1}^rD(f_i)$이고 따라서 $\{U_i\}_{i=1}^r$은 $U$의 유한한 affine open covering이다. 뿐만 아니라 $1=\sum_{i=1}^rb_if_i$인 $b_i\in B$를 택하여 $\varphi^\sharp(\Spec B)$를 취하면 $g_1,\ldots, g_r$이 $R$의 unit ideal을 생성함을 안다. 둘째로, $\varphi$가 locally ringed space들 사이의 morphism이므로 각각의 $x\in U$에서 $\varphi^\sharp_x:\mathcal{O}_{Y,\varphi(x)} \rightarrow \mathcal{O}_{X,x}$는 local homomorphism이고, 따라서 $\varphi(x)\in D(f_i)$인 것과 $x\in U_{g_i}$인 것이 동치이므로 $U_i=U_{g_i}$이다. 셋째로, $U_i\cong \Spec A_i$라 하고 $\Spec A_i \rightarrow \Spec B_{f_i}$에 대응되는 ring homomorphism을 $\phi_i$라 하면 $D(f_j)\cap D(f_i)$는 $\Spec B_{f_i}$의 principal open set이므로 위와 같이 [§스펙트럼, ⁋명제 8](/ko/math/scheme_theory/spectrums#prop8)을 적용하여 $U_i\cap U_j$가 $\Spec A_i$의 principal open set, 특히 affine임을 안다.

이제 각각의 $i$에 대하여 canonical map $R_{g_i} \rightarrow \Gamma(U_{g_i}, \mathcal{O}_X)$이 isomorphism임을 보인다. $U$의 open covering $\{U_j\}_{j=1}^r$에 대한 [\[위상수학\] §층, ⁋정의 1](/ko/math/topology/sheaves#def1)의 두 조건은 다음의 exact sequence

$$0 \rightarrow R \rightarrow \bigoplus_{j=1}^r \mathcal{O}_X(U_j) \rightarrow \bigoplus_{j,k=1}^r \mathcal{O}_X(U_j\cap U_k)$$

가 존재한다는 것과 같다. 여기에서 둘째 함수는 $(s_j)_j\mapsto (s_j\vert_{U_j\cap U_k}-s_k\vert_{U_j\cap U_k})_{j,k}$이다. 이는 $R$-module들의 exact sequence이고 direct sum이 유한하므로, [\[가환대수학\] §국소화의 성질들, ⁋명제 2](/ko/math/commutative_algebra/properties_of_localization#prop2)에 의하여 $g_i$에서 localize하여도 exactness가 보존되어 다음의 exact sequence

$$0 \rightarrow R_{g_i} \rightarrow \bigoplus_{j=1}^r \mathcal{O}_X(U_j)_{g_i} \rightarrow \bigoplus_{j,k=1}^r \mathcal{O}_X(U_j\cap U_k)_{g_i}$$

를 얻는다. (여기에서 $\mathcal{O}_X(U_j)$의 localization은 $g_i$의 $U_j$로의 restriction에서의 localization을 뜻한다.) 한편 $U_j$와 $U_j\cap U_k$는 모두 affine이고 affine scheme $\Spec A$와 $a\in A$에 대하여 $\mathcal{O}_{\Spec A}(D(a))=A_a$이므로 ([§스킴, ⁋보조정리 2](/ko/math/scheme_theory/schemes#lem2)) 위에서 관찰한 $U_g\cap \Spec A=D(g\vert_{\Spec A})$로부터

$$\mathcal{O}_X(U_j)_{g_i}=\mathcal{O}_X(U_j\cap U_{g_i}),\qquad \mathcal{O}_X(U_j\cap U_k)_{g_i}=\mathcal{O}_X(U_j\cap U_k\cap U_{g_i})$$

를 얻는다. 그런데 이렇게 얻어진 exact sequence는 정확히 $U_{g_i}$의 open covering $\{U_j\cap U_{g_i}\}_{j=1}^r$에 대한 sheaf 조건이 주는 exact sequence이므로, $R_{g_i}$와 $\Gamma(U_{g_i}, \mathcal{O}_X)$는 모두 같은 함수의 kernel이 되어 canonical map $R_{g_i} \rightarrow \Gamma(U_{g_i}, \mathcal{O}_X)$은 isomorphism이다.

마지막으로 [§아핀스킴, ⁋정리 13](/ko/math/scheme_theory/affine_schemes#thm13)의 adjunction

$$\Hom_\Sch(U, \Spec R)\cong \Hom_\cRing(R, \Gamma(U, \mathcal{O}_X))$$

에서 $\id_R$에 대응되는 scheme morphism $\psi: U \rightarrow \Spec R$을 생각하자. $\psi$ 또한 locally ringed space들 사이의 morphism이므로 각각의 $x\in U$에서 $\psi^\sharp_x$는 local homomorphism이고, 합성 $R \rightarrow \mathcal{O}_{\Spec R, \psi(x)} \rightarrow \mathcal{O}_{X,x}$가 canonical map $R=\Gamma(U, \mathcal{O}_X) \rightarrow \mathcal{O}_{X,x}$이므로 $\psi(x)$는 이 canonical map에 의한 $\mathcal{O}_{X,x}$의 maximal ideal의 preimage이다. 따라서

$$\psi^{-1}(D(g_i))=U_{g_i}=U_i$$

이고, $\psi\vert_{U_i}: U_i \rightarrow D(g_i)\cong \Spec R_{g_i}$는 affine scheme들 사이의 morphism으로서 방금 얻은 isomorphism $R_{g_i}\cong \Gamma(U_i, \mathcal{O}_X)$에 대응되므로 [§아핀스킴, ⁋명제 11](/ko/math/scheme_theory/affine_schemes#prop11)에 의하여 isomorphism이다. 이제 $g_i$들이 $R$의 unit ideal을 생성하므로 $\{D(g_i)\}$는 $\Spec R$을 덮고 $\{U_i\}$는 $U$를 덮으므로, $\psi$는 isomorphism이다. 즉 $U\cong\Spec R$은 affine이다. 
:::

## 유한사상, 정수형사상과 유한형사상

::: 정의 10
Scheme morphism $\varphi:X \rightarrow Y$가 *finite<sub>유한</sub>*인 것은 $\varphi$가 affine이고, $Y$의 임의의 affine open subset $V$에 대하여, ring homomorphism

$$(\varphi\vert_{\varphi^{-1}(V)})^\sharp(V): \mathcal{O}_V(V) \rightarrow \mathcal{O}_{\varphi^{-1}(V)}(\varphi^{-1}(V))$$

이 finite ring homomorphism인 것이다. ([\[가환대수학\] §정수적 확장, ⁋정의 3](/ko/math/commutative_algebra/integral_extension#def3))
:::

이해를 돕기 위해 affine open subset $V\subseteq Y$를 $\Spec B$라 쓰자. 그럼 $\varphi$가 affine이라는 가정으로부터 $U=\varphi^{-1}(V)$는 $X$의 affine open subset이고 따라서 $U\cong\Spec A$이도록 하는 $A$가 존재한다. 이러한 identification을 통해, scheme morphism $\varphi\vert_U: U \rightarrow V$는 spectrum 사이의 morphism $\Spec A \rightarrow \Spec B$와 같은 것이고, 이제 $\varphi$가 finite이라는 것은 이 morphism에 해당하는 ring homomorphism $B \rightarrow A$가 finite인 것이다. 비슷하게 다음을 정의한다.

::: 정의 11
Scheme morphism $\varphi:X \rightarrow Y$가 *integral<sub>정수형</sub>*인 것은 $\varphi$가 affine이고, $Y$의 임의의 affine open subset $V$에 대하여, ring homomorphism

$$(\varphi\vert_{\varphi^{-1}(V)})^\sharp(V): \mathcal{O}_V(V) \rightarrow \mathcal{O}_{\varphi^{-1}(V)}(\varphi^{-1}(V))$$

이 integral ring homomorphism인 것이다. ([\[가환대수학\] §정수적 확장, ⁋정의 3](/ko/math/commutative_algebra/integral_extension#def3)) 
:::

이제 그 정의로부터 finite morphism과 integral morphism이 합성에 대해 닫혀있다는 것을 안다. 또, 이들이 [§스킴의 위상구조, ⁋정의 9](/ko/math/scheme_theory/topology_of_schemes#def9)의 affine-local property 조건을 만족하는 것은 [명제 9](#prop9)와 [\[가환대수학\] §정수적 확장, ⁋명제 14](/ko/math/commutative_algebra/integral_extension#prop14), [\[가환대수학\] §정수적 확장, ⁋명제 15](/ko/math/commutative_algebra/integral_extension#prop15)로부터 알 수 있으므로 이들은 모두 affine-local on target이다. 

우리는 [\[가환대수학\] §정수적 확장, ⁋보조정리 4](/ko/math/commutative_algebra/integral_extension#lem4)에 의해 임의의 finite morphism은 integral인 것을 안다. 이제 이 보조정리를 완전하게 대수기하의 언어로 서술하기 위해서는 finite type morphism을 정의해야 한다. 

::: 정의 12
Scheme morphism $\varphi:X \rightarrow Y$가 *locally of finite type<sub>국소적으로 유한형</sub>*인 것은 $Y$의 임의의 affine open subset $V$와 $\varphi^{-1}(V)$의 임의의 affine open subset $U$에 대하여, 

$$(\varphi\vert_{U})^\sharp(V): \mathcal{O}_V(V) \rightarrow \mathcal{O}_U(U)$$

이 finite type인 것이다. ([\[가환대수학\] §정수적 확장, ⁋정의 3](/ko/math/commutative_algebra/integral_extension#def3)) 
:::

역시 위와 마찬가지로, $V\cong \Spec B$라 하고 $U\cong\Spec A\subseteq \varphi^{-1}(V)$라 하자. 그럼 scheme morphism $\varphi\vert_U: U \rightarrow V$를 $\Spec A \rightarrow \Spec B$로 볼 수 있고, 이에 대응하는 ring homomorphism $B \rightarrow A$가 finite type일 것을 요구하는 것이다.

[정의 12](#def12)는 $\varphi^{-1}(V)$의 <em-ko>모든</em-ko> affine open subset을 양화하므로, 이를 확인하기 위해서는 하나의 affine open covering만으로 충분해야 한다는 것을 따로 보여야 한다. 이는 다음 보조정리의 내용이다.

::: 보조정리 13
Scheme morphism $\varphi: W \rightarrow \Spec B$가 주어졌다 하고, $W$의 affine open covering $\{\Spec A_i\}$가 존재하여 각각의 $B \rightarrow A_i$가 finite type이라 하자. 그럼 $W$의 <em-ko>임의의</em-ko> affine open subset $U$에 대하여 $B \rightarrow \mathcal{O}_W(U)$ 또한 finite type이다. 
:::
::: 증명
$W$의 affine open subset $\Spec R$에 대한 성질 $Q$를 

> $B \rightarrow R$이 finite type이다.

로 정의하고, $Q$가 [§스킴의 위상구조, ⁋정의 9](/ko/math/scheme_theory/topology_of_schemes#def9)의 affine-local property임을 보이자. 그럼 주어진 covering $\{\Spec A_i\}$가 $Q$를 만족하므로 [§스킴의 위상구조, ⁋보조정리 12](/ko/math/scheme_theory/topology_of_schemes#lem12)의 둘째 조건으로부터 원하는 결과를 얻는다.

첫째 조건은 $B \rightarrow R$이 finite type일 때 $R$의 generator들에 $1/h$를 추가하면 $R_h$가 $B$-algebra로서 finitely generated가 되므로 자명하다. 둘째 조건을 위해 $R=(h_1,\ldots, h_m)$이고 각각의 $B \rightarrow R_{h_t}$가 finite type이라 하자. 각각의 $t$에 대하여 $R_{h_t}$를 $B$-algebra로서 생성하는 유한집합을 택한 후 분모를 없애면, $R$의 원소들 $x_{t1},\ldots, x_{tn_t}$가 존재하여 $R_{h_t}$가 $x_{tk}/1$들과 $1/h_t$에 의해 $B$-algebra로서 생성되도록 할 수 있다. 또 $1=\sum_{t=1}^ma_th_t$인 $a_t\in R$을 택하자. 이제 유한집합 $\{h_t\}\cup\{a_t\}\cup\{x_{tk}\}$가 생성하는 $R$의 $B$-subalgebra를 $R'$이라 하면 $R'$은 finite type $B$-algebra이므로 $R'=R$임을 보이면 충분하다. 임의의 $x\in R$에 대하여, $R_{h_t}$에서 $x/1$은 $x_{tk}/1$들과 $1/h_t$의 $B$-계수 다항식이므로 적당한 $r_t\in R'$과 $n_t\geq 0$에 대하여 $x/1=r_t/h_t^{n_t}$이고, 따라서 적당한 $N_t$에 대하여 $R$에서 $h_t^{N_t}(h_t^{n_t}x-r_t)=0$, 곧 $h_t^{N_t+n_t}x=h_t^{N_t}r_t\in R'$이다. $t$가 유한개이므로 공통의 $M$을 택하여 모든 $t$에 대해 $h_t^Mx\in R'$이도록 할 수 있다. 한편 $1=\sum_ta_th_t$에서 $a_t,h_t\in R'$이므로 $h_1,\ldots, h_m$은 $R'$의 unit ideal을 생성하고, 이 식의 양변을 충분히 큰 거듭제곱하면 $h_1^M,\ldots, h_m^M$ 또한 $R'$의 unit ideal을 생성함을 안다. 즉 $1=\sum_tc_th_t^M$인 $c_t\in R'$이 존재하고 따라서

$$x=\sum_{t=1}^mc_t(h_t^Mx)\in R'$$

이다. 
:::

그럼 finite type morphism은 다음과 같이 정의된다.

::: 정의 14
Scheme morphism $\varphi:X \rightarrow Y$가 *morphism of finite type<sub>유한형사상</sub>*이라는 것은 $\varphi$가 quasi-compact morphism locally of finite type인 것이다. 
:::

정의로부터 morphism locally of finite type은 affine-local on target임이 명확하다. 또, quasi-compact morphism은 [명제 7](#prop7)로부터 affine-local on target이므로 finite type morphism 또한 affine-local on target이다. 

그럼 [\[가환대수학\] §정수적 확장, ⁋보조정리 4](/ko/math/commutative_algebra/integral_extension#lem4)에 의해 다음이 성립한다.

::: 명제 15
Scheme morphism $\varphi:X \rightarrow Y$가 finite인 것은 $\varphi$가 integral morphism (locally) of finite type인 것과 동치이다. 
:::
::: 증명
우선 $\varphi$가 finite이라 하자. 임의의 affine open subset $V=\Spec B\subseteq Y$에 대하여 $\varphi^{-1}(V)=\Spec A$이고 $B \rightarrow A$가 finite이므로, [\[가환대수학\] §정수적 확장, ⁋보조정리 4](/ko/math/commutative_algebra/integral_extension#lem4)에 의하여 이는 integral이고 특히 finite type이다. 즉 $\varphi$는 integral이며, $\{\varphi^{-1}(V)\}$ 자신을 affine open covering으로 삼아 [보조정리 13](#lem13)을 적용하면 $\varphi^{-1}(V)$의 <em-ko>모든</em-ko> affine open subset $U$에 대해서도 $B \rightarrow \mathcal{O}_X(U)$가 finite type이므로 $\varphi$는 locally of finite type이다. 반대쪽 방향은 우선 $\varphi$가 integral이라는 가정으로부터 임의의 affine open subset $V\subseteq Y$에 대하여 $\varphi^{-1}(V)$가 $X$의 affine open subset임을 알고, 이렇게 얻어진 ring map에 [\[가환대수학\] §정수적 확장, ⁋보조정리 4](/ko/math/commutative_algebra/integral_extension#lem4)를 적용하면 된다. 
:::

위의 명제에서 $\varphi$는 integral morphism이므로 affine morphism이고, 따라서 quasi-compact morphism이므로 ([§스펙트럼, ⁋보조정리 12](/ko/math/scheme_theory/spectrums#lem12)) $\varphi$가 finite type이든, locally finite type이든 똑같은 가정이 된다. 

::: 예시 16
이번 절에서 살펴본 morphism들의 예시를 살펴보자. Affine scheme들의 세상에서 이는 그저 [\[가환대수학\] §정수적 확장, ⁋정의 3](/ko/math/commutative_algebra/integral_extension#def3)의 예시들을 보는 것에 지나지 않는다. 이번 예시의 목적은 이들에 기하학적인 직관을 부여하는 것이다.

우선 algebraically closed field $\mathbb{K}$에 대하여, ring map $\iota:\mathbb{K}[\x] \rightarrow \mathbb{K}[\x,\y]$를 생각하면 $\mathbb{K}[\x,\y]$는 $\mathbb{K}[\x]$-algebra로서 하나의 원소 $\y$에 의해 생성되므로 finite type ring homomorphism이지만, $\mathbb{K}[\x]$-module로서는 유한하게 생성되지 않으므로 finite ring homomorphism은 아니다. 

이제 이에 대응되는 scheme morphism $\Spec\iota: \Spec \mathbb{K}[\x,\y] \rightarrow\Spec \mathbb{K}[\x]$를 생각하자. 이는 임의의 prime ideal $\mathfrak{p}\subseteq \mathbb{K}[\x,\y]$를 받아 $\mathbb{K}[\x]$의 prime ideal $\mathfrak{p}\cap \mathbb{K}[\x]$를 내놓는 함수이다. 이는 기하적으로는 affine plane $\mathbb{A}^2_\mathbb{K}$의 점 $(x,y)$를 affine line $\mathbb{A}^1_\mathbb{K}$의 점 $x$에 대응시키는 함수이다. 

{% diagram Math/Scheme_Theory/Properties_of_Scheme_Morphisms-1.svg width="28.04em" alt="finite_type_morphism" %}

이와 관련된 finite morphism의 예시로는 위의 ring homomorphism $\iota:\mathbb{K}[\x]\rightarrow \mathbb{K}[\x,\y]$에 projection map $\pi:\mathbb{K}[\x,\y] \rightarrow \mathbb{K}[\x,\y]/(\x-\y^2)$을 합성한 것이 있다. 그럼 $\mathbb{K}[\x,\y]/(\x-\y^2)$은 $\mathbb{K}[\x]$-module로서 $1$과 $\y$에 의해 생성되므로 $\phi:\mathbb{K}[\x] \rightarrow \mathbb{K}[\x,\y]/(\x-\y^2)$은 finite ring homomorphism이다. 

한편 우리는 ring homomorphism $\pi:A \rightarrow A/\mathfrak{a}$는 기하적으로 $\mathfrak{a}$가 정의하는 닫힌집합의 inclusion에 해당하는 것을 안다. 따라서 합성

$$\phi: \mathbb{K}[\x] \rightarrow \mathbb{K}[\x,\y] \rightarrow \mathbb{K}[\x,\y]/(\x-\y^2)$$

이 정의하는 scheme morphism

$$\Spec\phi: \Spec \frac{\mathbb{K}[\x,\y]}{(\x-\y^2)}\rightarrow \Spec \mathbb{K}[\x,\y] \rightarrow \Spec\mathbb{K}[\x]$$

은 기하적으로 $\x=\y^2$의 zero set $Z(\x-\y^2)$에서 $x$축으로의 projection으로 볼 수 있다.

{% diagram Math/Scheme_Theory/Properties_of_Scheme_Morphisms-2.svg width="25.72em" alt="finite_morphism" %}

이 두 예시의 기하학적인 차이는 꽤나 명확하다. 첫 번째 예시의 경우, target의 한 점에서의 fiber가 무한집합인 반면 두 번째 예시의 경우 한 점에서의 fiber가 유한집합이다. 대수적으로 이는 target $\mathbb{A}_\mathbb{K}^1$의 임의의 점 $\mathfrak{p}=(\x-a)$를 가져왔을 때, 임의의 $\mathfrak{q}_b=(\x-a, \y-b)\in \mathbb{A}_\mathbb{K}^2$는 $(\Spec\iota)(\mathfrak{q}_b)=\mathfrak{p}$를 만족하는 반면, 두 번째 예시에서는 $\y^2=\x$가 성립해야 하므로 $b^2=a$인 $b$만이 가능하고, 따라서 $(\Spec\phi)(\mathfrak{q})=\mathfrak{p}$를 만족하는 점은 많아야 두 개, 즉 $\mathfrak{q}_+=(\x-a, \y-\sqrt{a})$와 $\mathfrak{q}_-=(\x-a, \y+\sqrt{a})$뿐이다. 이들이 서로 다른 두 점이 되는 것은 $\operatorname{char}\mathbb{K}\neq 2$이고 $a\neq 0$일 때인데, $a=0$이면 두 점이 하나로 겹치고, $\operatorname{char}\mathbb{K}=2$일 때는 $\y^2-a=(\y-\sqrt{a})^2$이므로 모든 $a$에 대하여 fiber가 한 점이기 때문이다. 

이와 같이, finite type morphism은 기하적으로는 fiber가 유한차원인 것과 관련이 있고, finite morphism은 fiber가 유한집합인 것과 관련이 있다. 
:::

아직은 위의 [예시 16](#ex16)과 같은 상황에서 scheme morphism의 fiber를 계산하기 위해서는 그때그때 상황에 맞추어 우직하게 계산을 해 나가는 수밖에 없지만, 나중에 fiber product를 계산하고 나면 조금 더 정형화된 방식을 사용할 수 있게 된다. 그 때를 위해 다음을 정의한다.

::: 정의 17
Scheme morphism $\varphi: X \rightarrow Y$가 *quasi-finite<sub>준유한</sub>*인 것은 $\varphi$가 morphism of finite type이고 임의의 $y\in Y$에 대하여 집합 $\varphi^{-1}(y)$가 항상 유한집합인 것이다. 
:::

그럼 [예시 16](#ex16)에서의 finite morphism에 대한 기하학적 직관은 항상 참이다. 즉, 임의의 finite morphism은 항상 quasi-finite이다. 이는 지금 당장 증명하는 것도 가능하지만, fiber product를 정의하고 난 후로 미룬다. 

마지막으로 다음을 정의한다. 

::: 정의 18
Scheme morphism $\varphi: X \rightarrow Y$가 *locally of finite presentation<sub>국소유한표시사상</sub>*이라는 것은 $Y$의 임의의 affine open subset $V\cong \Spec B$가 주어질 때마다, $\varphi^{-1}(V)$의 covering $\varphi^{-1}(V)=\bigcup \Spec A_i$가 존재하여 $B \rightarrow A_i$가 모두 finitely presented인 것이다. 만일 scheme morphism $\varphi:X \rightarrow Y$가 quasi-compact, quasi-separated, locally of finite presentation이라면 $\varphi$가 *morphism of finite presentation<sub>유한표시사상</sub>*이라 부른다. 
:::

대부분의 경우 우리는 모든 scheme들이 locally Noetherian인 경우를 생각하고, 이 경우 이 개념은 새로운 것이 아니다. 실제로 $B$가 Noetherian ring이고 $B \rightarrow A$가 finite type이면 $A\cong B[\x_1,\ldots, \x_n]/\mathfrak{a}$로 쓸 수 있는데, [\[가환대수학\] §기본 개념들, ⁋정리 12](/ko/math/commutative_algebra/basic_notions#thm12)에 의하여 $B[\x_1,\ldots, \x_n]$이 Noetherian이므로 $\mathfrak{a}$가 finitely generated이고 따라서 $B \rightarrow A$는 finitely presented이다. 또 locally Noetherian scheme은 quasi-separated이므로 ([명제 6](#prop6)), morphism of finite presentation을 요구하는 것과 morphism of finite type을 요구하는 것 사이의 차이 또한 사라진다. 

## 유리사상

[§스킴의 대수구조, ⁋정의 12](/ko/math/scheme_theory/algebra_of_schemes#def12)에서 우리는 scheme $X$ 위의 유리함수를 정의역 $U$와 그 위의 함수 $f\in \Gamma(U, \mathcal{O}_X)$가 이루는 pair의 equivalence class로 정의하였다. 한편, $U$를 그 자체로 locally ringed space로 보면 [§아핀스킴, ⁋정리 13](/ko/math/scheme_theory/affine_schemes#thm13)의 adjunction에 의해

$$\Hom_\LRS(U, \Spec \mathbb{Z}[\x])\cong \Hom_{\cRing}(\mathbb{Z}[\x], \Gamma(U,\mathcal{O}_X))$$

를 얻고, 여기에서 우변의 ring homomorphism $\mathbb{Z}[\x]\rightarrow \Gamma(U, \mathcal{O}_X)$는 $\x$의 image에 의해 정확하게 결정되므로 우변은 추가적인 isomorphism

$$\Hom_{\cRing}(\mathbb{Z}[\x], \Gamma(U,\mathcal{O}_X))\cong \Gamma(U, \mathcal{O}_X)$$

으로 연결해줄 수 있다. 즉, $U$ 위의 함수 $f$를 주는 것은 scheme morphism $U \rightarrow \Spec \mathbb{Z}[\x]=\mathbb{A}^1_\mathbb{Z}$를 주는 것과 같은 데이터이다. 

한편 우리는 scheme morphism을 정의함으로서 이제 base scheme을 $\Spec \mathbb{Z}$ 대신 일반적인 $\Spec A$로 택할 수도 있으므로, 이 논증을 반복하면 유리함수는 $U$ 위에서 정의된, target을 $\Spec A[\x]$로 갖는 morphism으로 생각할 수 있다. 이를 정확히 적기 위해서는 어떤 열린집합을 정의역으로 허용할 것인지와, 서로 다른 정의역 위의 두 morphism을 언제 같은 것으로 볼 것인지를 정해야 한다. 우선 image가 target 안의 작은 닫힌집합에 갇히지 않는 morphism에 이름을 붙인다.

::: 정의 19
Scheme morphism $\varphi: X \rightarrow Y$가 *dominant*라는 것은 $\varphi$의 image가 $Y$에서 dense인 것, 곧 $\cl(\varphi(X))=Y$인 것이다. 
:::

Surjective morphism은 언제나 dominant이지만 그 역은 성립하지 않는다. 가령 field가 아닌 integral domain $A$에 대하여 $\Spec \Frac A \rightarrow \Spec A$의 image는 generic point $(0)$ 하나뿐이지만, [§스펙트럼, ⁋정의 7](/ko/math/scheme_theory/spectrums#def7) 직후에 살펴본 대로 $(0)$을 포함하는 $\Spec A$의 닫힌집합은 $\Spec A$ 자신뿐이므로 이 morphism은 dominant이다. Affine scheme들 사이에서 dominance는 다음과 같이 순수하게 대수적으로 읽힌다.

::: 명제 20
Ring homomorphism $\phi: B \rightarrow A$와 그에 해당하는 scheme morphism $\varphi=\Spec \phi:\Spec A \rightarrow \Spec B$에 대하여 다음의 식

$$\cl\left(\varphi(\Spec A)\right)=Z(\ker\phi)$$

이 성립한다. 따라서 $\varphi$가 dominant인 것은 $\ker\phi\subseteq \mathfrak{N}(B)$인 것과 동치이다.
:::
::: 증명
[§스펙트럼, ⁋명제 14](/ko/math/scheme_theory/spectrums#prop14)의 둘째 결과에 의하여 임의의 $T\subseteq \Spec B$에 대하여 $\cl(T)=Z(I(T))$이므로, $T=\varphi(\Spec A)$에 대하여 $I(T)$를 계산하면 충분하다. $T$의 원소는 정확히 $\phi^{-1}(\mathfrak{q})$의 꼴이므로 다음의 식

$$I(T)=\bigcap_{\mathfrak{q}\in \Spec A}\phi^{-1}(\mathfrak{q})=\phi^{-1}\left(\bigcap_{\mathfrak{q}\in \Spec A}\mathfrak{q}\right)$$

을 얻는다. 한편 [§스펙트럼, ⁋명제 14](/ko/math/scheme_theory/spectrums#prop14)의 첫째 결과를 $S=\{0\}$에 적용하면 $A$의 모든 prime ideal의 교집합이 $\sqrt{(0)}=\mathfrak{N}(A)$인 것을 알고, 임의의 $b\in B$에 대하여 $\phi(b)$가 nilpotent인 것과 $b^n\in\ker\phi$인 $n$이 존재하는 것이 동치이므로 

$$I(T)=\phi^{-1}(\mathfrak{N}(A))=\sqrt{\ker\phi}$$

이다. 이제 항등식 $Z(I(Z(S)))=Z(S)$에 다시 [§스펙트럼, ⁋명제 14](/ko/math/scheme_theory/spectrums#prop14)의 첫째 결과를 적용하면 $Z(\sqrt{\ker\phi})=Z(\ker\phi)$이므로 원하는 식을 얻는다.

마지막 주장은, $Z(\ker\phi)=\Spec B$인 것이 $\ker\phi$가 $B$의 모든 prime ideal에 포함되는 것, 곧 위와 같은 이유로 $\ker\phi\subseteq \mathfrak{N}(B)$인 것과 동치이기 때문에 성립한다.
:::

특히 $B$가 reduced ring이면 $\Spec\phi$가 dominant인 것은 $\phi$가 injective인 것과 같다. 가령 [예시 16](#ex16)에서 본 $\iota: \mathbb{K}[\x] \rightarrow \mathbb{K}[\x,\y]$는 injective이므로 $\Spec\iota$는 dominant이며, ideal $\mathfrak{a}\subseteq B$에 대한 quotient map이 정의하는 morphism $\Spec B/\mathfrak{a} \rightarrow \Spec B$가 dominant인 것은 $\mathfrak{a}\subseteq \mathfrak{N}(B)$인 것, 곧 $\mathfrak{a}$가 정의하는 닫힌집합이 $\Spec B$ 전체인 것이다.

이제 정의역으로 삼을 열린집합을 정한다. 유리함수의 경우와 마찬가지로 정의역은 $X$ 안에서 충분히 커야 하며, 이를 위상적으로 적은 것이 dense 조건이다. 위의 논증에서 짐작할 수 있듯, reduced scheme에서는 이 조건만으로 함수의 정보가 보존된다.

::: 보조정리 21
Reduced scheme $X$와 dense open subset $U$에 대하여, restriction map $\Gamma(X, \mathcal{O}_X) \rightarrow \Gamma(U, \mathcal{O}_X)$는 injective이다. 
:::
::: 증명
$s\in \Gamma(X, \mathcal{O}_X)$가 $s\vert_U=0$을 만족한다 하고, $X$의 임의의 affine open subset $\Spec A$를 택한 후 편의상 $s$의 $\Spec A$로의 restriction을 다시 $s\in A$로 적자. 그럼 $X$가 reduced이므로 $A$는 reduced ring이고 ([§스킴의 대수구조, ⁋정의 1](/ko/math/scheme_theory/algebra_of_schemes#def1)), $\Spec A$의 공집합이 아닌 임의의 열린집합은 $X$의 열린집합이기도 하여 $U$와 만나므로 $U\cap \Spec A$는 $\Spec A$에서 dense이다. 

이제 임의의 $\mathfrak{p}\in U\cap \Spec A$에 대하여 $s$의 stalk $\mathcal{O}_{X,\mathfrak{p}}=A_\mathfrak{p}$에서의 germ이 $0$이므로 $ts=0$인 $t\in A\setminus \mathfrak{p}$가 존재하고, $\mathfrak{p}$가 prime ideal이므로 이로부터 $s\in \mathfrak{p}$를 얻는다. 곧 $U\cap \Spec A\subseteq Z(s)$인데 $Z(s)$가 닫힌집합이고 $U\cap \Spec A$가 dense이므로 $Z(s)=\Spec A$, 즉 $s$는 $A$의 모든 prime ideal에 속한다. 따라서 [§스펙트럼, ⁋명제 14](/ko/math/scheme_theory/spectrums#prop14)의 첫째 결과에 의하여 $s\in \mathfrak{N}(A)=0$이다. 이것이 $X$의 임의의 affine open subset에 대하여 성립하므로 $s=0$이다. 
:::

이 보조정리에서 reduced라는 가정은 뺄 수 없다. [§스킴의 대수구조, ⁋예시 11](/ko/math/scheme_theory/algebra_of_schemes#ex11)의 $X=\Spec \mathbb{K}[\x_1,\x_2]/(\x_2^2,\x_1\x_2)$의 경우 nilradical이 prime ideal $(\x_2)$이므로 $X$는 irreducible이고 ([§스킴의 대수구조, ⁋보조정리 3](/ko/math/scheme_theory/algebra_of_schemes#lem3)), 따라서 공집합이 아닌 열린집합 $D(\x_1)$은 dense이다. 그러나 $\x_1\x_2=0$에서 $\x_1$을 가역으로 만들면 $\x_2\vert_{D(\x_1)}=0$이 되어, $0$이 아닌 함수가 dense open subset 위에서 사라진다. [§스킴의 대수구조, ⁋정의 12](/ko/math/scheme_theory/algebra_of_schemes#def12)가 유리함수의 정의역에 associated point를 <em-ko>모두</em-ko> 담을 것을 요구한 것이 정확히 이를 막기 위한 것이었다.

한편, rational map의 정의역 $U$가 가질 수 있는 조건은 크게 두 가지가 있다. 하나는 고전적인 algebraic geometry에서와 마찬가지로 $U$를 dense open subset으로 잡는 것이고 ([\[대수다양체\] §유리사상, ⁋정의 5](/ko/math/algebraic_varieties/rational_maps#def5)), 다른 하나는 rational map을 [§스킴의 대수구조, ⁋정의 12](/ko/math/scheme_theory/algebra_of_schemes#def12)의 일반화로 보아 associated point를 모두 포함한다는 조건을 걸어주는 것이다. 위에서 살펴보았듯, non-reduced scheme에 대해서는 일반적으로 dense open subset임을 요구하는 것이 associated point들을 모두 포함하는 것을 요구하는 것보다는 약한 조건이지만, locally Noetherian reduced scheme의 경우 이 두 조건은 일치한다. 이를 확인하기 위해서는 우선 $X$의 임의의 irreducible component $C$가 generic point를 갖는다는 것을 보인 후 ($C$와 만나는 affine open subset $\Spec A$에 [§스펙트럼, ⁋명제 16](/ko/math/scheme_theory/spectrums#prop16)을 적용하여 얻어진 점을 $X$에서 closure를 취해주면 된다) 이로부터 $X$의 열린집합이 dense인 것은 그것이 $X$의 모든 irreducible component의 generic point를 포함하는 것과 동치임을 이끌어내면 된다. 그럼 reduced ring $A$에 대해서는 $\Spec A$의 associated point가 언제나 minimal prime ideal, 즉 irreducible component의 generic point이고, 거꾸로 [§스킴의 대수구조, §§동반소아이디얼](/ko/math/scheme_theory/algebra_of_schemes#동반소아이디얼)에서 Noetherian ring의 minimal prime ideal이 언제나 associated prime ideal인 것은 이미 확인하였으므로 이 두 조건이 일치하게 된다. 

::: 정의 22
Scheme $X$에서 scheme $Y$로의 *rational map<sub>유리사상</sub>*은 $X$에서 dense인 열린집합 $U$와 scheme morphism $\alpha: U \rightarrow Y$가 이루는 pair $(U,\alpha)$들의 equivalence class이다. 여기에서 두 pair $(U,\alpha)$와 $(V,\beta)$가 동치라는 것은 $U\cap V$에 포함되면서 $X$에서 dense인 열린집합 $W$가 존재하여 $\alpha\vert_W=\beta\vert_W$인 것이다. 
:::

Rational map은 $\varphi: X \dashrightarrow Y$와 같이 점선 arrow로 적으며, 점선은 $\varphi$가 $X$의 모든 점에서 정의되지 않을 수 있음을 나타낸다. 위의 정의가 실제로 동치관계인 것은 두 dense open subset의 교집합이 다시 dense open subset이 되기 때문으로, 이는 고전적으로 두 representative의 $U\cap V$ 전체에서의 일치를 요구했던 것에 비하면 약한 조건이지만 ([\[대수다양체\] §유리사상, ⁋정의 5](/ko/math/algebraic_varieties/rational_maps#def5)), $X$가 reduced이고 $Y=\Spec B$가 affine이면 둘은 같아진다. 두 morphism $\alpha,\beta: U\cap V \rightarrow Y$는 [§아핀스킴, ⁋정리 13](/ko/math/scheme_theory/affine_schemes#thm13)에 의하여 ring homomorphism $B \rightarrow \Gamma(U\cap V, \mathcal{O}_X)$에 대응되고, $U\cap V$가 reduced scheme이며 $W$가 그 안에서 dense이므로 [보조정리 21](#lem21)에 의하여 $\Gamma(U\cap V, \mathcal{O}_X) \rightarrow \Gamma(W, \mathcal{O}_X)$가 injective이기 때문이다.

Rational map $\varphi: X \dashrightarrow Y$가 *dominant*라는 것은 그 representative $(U,\alpha)$가 [정의 19](#def19)의 의미에서 dominant morphism인 것이다. 이는 representative의 선택에 의존하지 않는데, $W\subseteq U$가 $X$에서 dense인 열린집합이면 $W$는 $U$에서도 dense이고 $\alpha$가 연속함수이므로 $\cl(\alpha(U))=\cl(\alpha(W))$가 성립하기 때문이다. Dominant rational map이 중요한 이유는 두 rational map $\varphi: X\dashrightarrow Y$와 $\psi: Y \dashrightarrow Z$를 합성할 때 드러난다. 두 rational map의 representative $(U,\alpha)$와 $(V,\beta)$를 택하자. 그럼 이들의 합성 $\beta\circ \alpha$의 실제 정의역은 $\alpha$가 나중 함수의 정의역 안으로 들어가는 부분 $\alpha^{-1}(V)$이므로, 이 함수가 rational map을 정의하기 위해서는 $\alpha^{-1}(V)$가 $X$에서 dense여야 한다. 그럼 자연스럽게 요구할 수 있는 조건은 $\alpha$의 dominance로, 이를 요구하면 $\alpha(U)$가 $V$와 반드시 만나므로 $\alpha^{-1}(V)$가 공집합이 되지는 않는다. 그러나 scheme의 세상에서는 이 조건 역시 다소 불충분하다. 가령 $X$를 $\mathbb{A}^1_\mathbb{K}$와 $\Spec\mathbb{K}$의 disjoint union으로, $Y=\mathbb{A}^1_\mathbb{K}$로 두고 $\alpha$를 첫째 성분에서는 항등사상, 둘째 성분에서는 closed point $p$로 보내는 morphism으로 두면 $\alpha$는 dominant이지만, $V=Y\setminus \{p\}$에 대하여 $\alpha^{-1}(V)$는 첫째 성분의 $\mathbb{A}^1_\mathbb{K}\setminus\{p\}$뿐이어서 $X$의 공집합이 아닌 열린집합인 둘째 성분과 만나지 않는다. 이는 $X$가 여러 조각으로 갈라져 있어서 생기는 문제로, 만일 $X$가 irreducible이면 공집합이 아닌 열린집합이 모두 dense이므로 이런 문제가 사라진다. 또 [보조정리 21](#lem21) 직후의 반례에서 $X$가 reduced인 것이 필요하다는 것을 이미 살펴보았으므로, 우리는 편의상 $X,Y$가 모두 integral scheme인 경우를 생각하기로 한다. ([§스킴의 대수구조, ⁋명제 4](/ko/math/scheme_theory/algebra_of_schemes#prop4)) 그럼 이 경우 dominant rational map $\varphi: X\dashrightarrow Y$와 임의의 rational map $\psi: Y \dashrightarrow Z$의 합성 $\psi\circ\varphi$가 representative $(\alpha^{-1}(V), \beta\circ \alpha)$로 잘 정의되며, 어렵지 않게 이것이 representative의 선택에 의존하지 않음을 보일 수 있다.

::: 정의 23
Integral scheme $X, Y$ 사이의 dominant rational map $\varphi: X \dashrightarrow Y$가 *birational map<sub>쌍유리 사상</sub>*이라는 것은 dominant rational map $\psi: Y \dashrightarrow X$가 존재하여 $\psi\circ\varphi$와 $\varphi\circ\psi$가 각각 $\id_X$와 $\id_Y$가 정의하는 rational map과 같은 것이다. 두 integral scheme $X, Y$가 *birationally equivalent<sub>쌍유리 동치</sub>*라는 것은 이러한 birational map $\varphi: X\dashrightarrow Y$가 존재하는 것이다. 
:::

Isomorphism이 두 scheme이 완전히 같은 구조를 갖는다는 뜻이라면, birational equivalence는 두 scheme이 dense인 열린집합 위에서 같은 구조를 갖는다는 뜻이다. 이를 정확히 적은 것이 다음 명제이다.

::: 명제 24
Integral scheme $X, Y$ 사이의 dominant rational map $\varphi: X \dashrightarrow Y$에 대하여 다음 두 조건이 동치이다.

1. $\varphi$는 birational map이다. 
2. $X$의 공집합이 아닌 열린집합 $\widetilde U$와 $Y$의 공집합이 아닌 열린집합 $\widetilde V$가 존재하여, isomorphism $\widetilde U \rightarrow \widetilde V$가 $\varphi$의 representative가 된다. 
:::
::: 증명
우선 $\varphi$가 birational map이라 하고, $\varphi$의 representative $(U,\alpha)$와 그 역할을 하는 $\psi$의 representative $(V,\beta)$를 택하자. 그럼 $\psi\circ\varphi=\id_X$로부터 $X$의 공집합이 아닌 열린집합 $W_1\subseteq \alpha^{-1}(V)$가 존재하여 $(\beta\circ \alpha)\vert_{W_1}=\id_{W_1}$이고, $\varphi\circ\psi=\id_Y$로부터 $Y$의 공집합이 아닌 열린집합 $W_2\subseteq \beta^{-1}(U)$가 존재하여 $(\alpha\circ \beta)\vert_{W_2}=\id_{W_2}$이다. 이제

$$\widetilde U=W_1\cap \alpha^{-1}(W_2),\qquad \widetilde V=W_2\cap \beta^{-1}(W_1)$$

으로 두자. $W_1$이 $U$에서 dense이고 $\varphi$가 dominant이므로 $\cl(\alpha(W_1))=\cl(\alpha(U))=Y$이고, 따라서 공집합이 아닌 열린집합 $W_2$는 $\alpha(W_1)$과 만나 $\widetilde U\neq\emptyset$이다. 

$\widetilde U$의 점 $x$에 대하여 $\alpha(x)\in W_2$이고, $x\in W_1$이므로 $\beta(\alpha(x))=x\in W_1$, 곧 $\alpha(x)\in \beta^{-1}(W_1)$이다. 따라서 $\alpha(\widetilde U)\subseteq \widetilde V$이며, 같은 방식으로 $\widetilde V$의 점 $y$에 대하여 $\beta(y)\in W_1$이고 $\alpha(\beta(y))=y\in W_2$이므로 $\beta(\widetilde V)\subseteq \widetilde U$이다. 이렇게 얻어진 두 morphism $\alpha\vert_{\widetilde U}: \widetilde U \rightarrow \widetilde V$와 $\beta\vert_{\widetilde V}: \widetilde V \rightarrow \widetilde U$는 $\widetilde U\subseteq W_1$과 $\widetilde V\subseteq W_2$에 의하여 그 합성이 각각 항등사상이 되므로 $\alpha\vert_{\widetilde U}$는 isomorphism이고, $\widetilde U$가 $X$에서 dense이므로 $(\widetilde U, \alpha\vert_{\widetilde U})$는 $\varphi$의 representative이다. 

거꾸로 isomorphism $\alpha: \widetilde U \rightarrow \widetilde V$가 $\varphi$의 representative라 하고 그 역사상을 $\beta: \widetilde V \rightarrow \widetilde U$라 하자. 그럼 $\widetilde V$가 $Y$에서 dense이므로 $\beta$와 open subset의 포함사상 $\widetilde U \hookrightarrow X$의 합성은 rational map $\psi: Y \dashrightarrow X$를 정의하며, $\beta$가 surjective이므로 $\psi$는 dominant이다. 또 $\psi\circ\varphi$는 $\widetilde U$ 위에서 $\beta\circ \alpha=\id_{\widetilde U}$이고 $\varphi\circ\psi$는 $\widetilde V$ 위에서 $\alpha\circ \beta=\id_{\widetilde V}$이므로, 이 둘은 각각 $\id_X$와 $\id_Y$가 정의하는 rational map과 같다. 
:::

Integral scheme $X$가 locally Noetherian이면 [§스킴의 대수구조, ⁋정의 12](/ko/math/scheme_theory/algebra_of_schemes#def12)의 유리함수의 정의역은 정확히 $X$의 공집합이 아닌 열린집합이 된다. 실제로 $X$의 공집합이 아닌 affine open subset $\Spec A$에 대하여 $A$는 integral domain이므로 ([§스킴의 대수구조, ⁋정의 1](/ko/math/scheme_theory/algebra_of_schemes#def1)) $0$이 아닌 원소의 annihilator는 언제나 $(0)$이고, 따라서 $\Spec A$의 associated point는 $(0)$ 하나뿐이다. 곧 $X$의 associated point는 generic point $\eta$ 하나뿐이므로, 정의역이 모든 associated point를 담아야 한다는 조건은 정의역이 공집합이 아니라는 조건과 같아진다. 이렇게 얻어진 유리함수들의 모임 $K(X)$가 $\mathcal{O}_{X,\eta}\cong\Frac A$와 일치하여 field가 되는 것은 이미 확인하였으며 ([§스킴의 대수구조, §§유리함수](/ko/math/scheme_theory/algebra_of_schemes#유리함수)), 이를 $X$의 *function field*라 부른다.

::: 따름정리 25
Birationally equivalent한 두 integral locally Noetherian scheme $X, Y$에 대하여 $K(X)\cong K(Y)$가 성립한다. 
:::
::: 증명
[명제 24](#prop24)에 의하여 isomorphism $\alpha: \widetilde U \rightarrow \widetilde V$를 representative로 갖는 birational map이 존재한다. $X$의 generic point $\eta_X$는 공집합이 아닌 열린집합 $\widetilde U$에 속하고 stalk은 open subscheme으로 제한하여도 변하지 않으므로 $K(X)=\mathcal{O}_{X,\eta_X}=\mathcal{O}_{\widetilde U, \eta_X}$이고, 같은 이유로 $K(Y)=\mathcal{O}_{\widetilde V, \eta_Y}$이다. 한편 $\widetilde V$가 $Y$의 공집합이 아닌 열린집합이므로 그 generic point는 $\eta_Y$이고, $\alpha$가 isomorphism이므로 $\alpha(\eta_X)=\eta_Y$이다. 따라서 $\alpha$가 유도하는 stalk 사이의 isomorphism이 $K(X)\cong K(Y)$를 준다. 
:::

즉 birational equivalence는 function field를 보존한다. Variety의 경우에는 그 역 또한 성립하는 것을 [\[대수다양체\] §유리사상, ⁋명제 10](/ko/math/algebraic_varieties/rational_maps#prop10)에서 확인하였다. 

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic geometry*. Graduate texts in mathematics. Springer, 1977.  
**[Vak]** R. Vakil, *The rising sea: Foundation of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/).
