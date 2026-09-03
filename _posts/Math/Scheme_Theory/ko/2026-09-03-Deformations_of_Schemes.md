---
title: "스킴의 변형"
description: "Affine 수준에서 얻은 일차 변형의 분류를 scheme 전체로 붙인다. Smooth한 경우 일차 변형이 tangent sheaf의 첫째 cohomology로 분류됨을 gluing으로 보이고, singularity가 있으면 이 논법이 깨지는 이유를 tangent sheaf의 정보 손실에서 찾는다. Reduced local complete intersection에서 conormal sequence가 왼쪽에서도 exact임을 보여 naive 여접 복합체가 cotangent sheaf의 projective resolution이 됨을 확인하고, 이로써 변형과 obstruction을 Ext로 적는다. 국소-대역 Ext spectral sequence의 다섯 항 완전열이 국소 변형과 접합의 자유도를 분리하며, hypersurface에서 국소 변형이 Tjurina algebra로 계산된다."
excerpt: "First-order deformations of schemes, and why they are governed by Ext of the cotangent sheaf"

categories: [Math / Scheme Theory]
permalink: /ko/math/scheme_theory/deformations_of_schemes
sidebar: 
    nav: "scheme_theory-ko"

date: 2026-09-03
weight: 23

published: false

---

Affine scheme의 변형은 이미 손에 있다. Finitely generated $k$-algebra $B$의 first-order deformation이 $T^1(B/k, B)$과 일대일 대응하고 ([§변형이론과 여접 복합체, ⁋정리 7](/ko/math/scheme_theory/deformation_theory#thm7)), 그것을 더 두꺼운 base 위로 연장하는 데 걸리는 obstruction은 [§변형이론과 여접 복합체, ⁋정리 9](/ko/math/scheme_theory/deformation_theory#thm9)에 의하여 $T^2(B/k, B)$에 놓인다. 남은 일은 이 국소적인 분류를 scheme 전체로 붙이는 것이다.

붙이는 데에는 두 겹의 자유도가 있다. 하나는 각 affine 조각이 스스로 변형되는 자유도이고, 다른 하나는 조각들을 다시 이어 붙이는 방식의 자유도이다. Smooth한 경우에는 첫째 자유도가 통째로 사라져 둘째 것만 남으며, 그 결과가 tangent sheaf의 첫째 cohomology이다. Singularity가 있으면 두 자유도가 함께 살아 있고, 이들을 한 대상 안에서 다루는 올바른 틀이 cotangent sheaf의 $\Ext$이다.

이 글 전체에서 $k$는 algebraically closed field이고, 모든 scheme은 $k$ 위에서 separated이며 finite type이다. 또 $k[\epsilon]=k[t]/(t^2)$로 적는다.

## 스킴의 일차 변형

::: 정의 1
$k$-scheme $X$의 *first-order deformation<sub>일차 변형</sub>*이란 $\Spec k[\epsilon]$ 위에서 flat한 scheme $\mathcal{X}$와 isomorphism

$$\mathcal{X}\times_{\Spec k[\epsilon]}\Spec k\cong X$$

의 짝을 뜻한다. 두 first-order deformation $\mathcal{X}, \mathcal{X}'$이 *isomorphic*이라는 것은 $\Spec k[\epsilon]$ 위에서의 isomorphism $\mathcal{X}\cong\mathcal{X}'$으로서 $X$ 위에 항등사상을 유도하는 것이 존재한다는 것이다. 곱 $X\times_{\Spec k}\Spec k[\epsilon]$에 isomorphic한 변형을 *trivial*하다 부른다.
:::

$\epsilon$이 nilpotent이므로 $\mathcal{X}$와 $X$는 같은 위상공간을 갖고, 두꺼워지는 것은 오직 structure sheaf뿐이다. 따라서 $X$의 열린집합 $U$마다 $\mathcal{X}\vert_U$가 $U$의 first-order deformation을 주며, 이것이 위에서 말한 국소적인 자료이다. Affine $U=\Spec B$에서 이 자료는 정확히 $B$의 first-order deformation이므로 ([§변형이론과 여접 복합체, ⁋정의 3](/ko/math/scheme_theory/deformation_theory#def3)) $T^1(B/k, B)$가 분류한다.

Smooth한 경우 이 국소 자료가 아무것도 주지 않는다는 것을 먼저 확인한다.

::: 명제 2
$X$가 $k$ 위에서 smooth한 affine scheme이면 $X$의 모든 first-order deformation은 trivial하다.
:::
::: 증명
$X=\Spec B$이고 $\mathcal{X}=\Spec B'$이라 하자. $B'$이 $k[\epsilon]$ 위에서 flat하므로 $\times\epsilon: B'/\epsilon B'\rightarrow \epsilon B'$이 isomorphism이고 ([\[가환대수학\] §평탄성, ⁋따름정리 2](/ko/math/commutative_algebra/flatness#cor2)), $B'/\epsilon B'=B$이므로 $k[\epsilon]$-module들의 exact sequence

$$0\longrightarrow B\overset{\times\epsilon}{\longrightarrow}B'\longrightarrow B\longrightarrow0$$

을 얻는다. 특히 $\epsilon B'$은 제곱이 $0$이므로 $\Spec B\hookrightarrow \Spec B'$은 square-zero closed embedding이다.

이제 $\varphi: X\rightarrow \Spec k$가 smooth이고 $\Spec B'$이 affine이므로 [§매끄러운 사상과 에탈 사상, ⁋정리 15](/ko/math/scheme_theory/smooth_and_etale_morphisms#thm15)의 첫째 주장을 $T_0=\Spec B$, $T=\Spec B'$, 그리고 $\varrho_0=\id_X$에 적용할 수 있다. 그럼 $\varrho_0$의 lifting $\varrho:\Spec B'\rightarrow X$가 존재하며, 이는 ring 단계에서 quotient $B'\rightarrow B$와 합성하여 $\id_B$가 되는 $k$-algebra homomorphism $\sigma: B\rightarrow B'$이다.

$\sigma$를 $k[\epsilon]$-algebra homomorphism $\Sigma: B\otimes_kk[\epsilon]\rightarrow B'$으로 확장하자. 이 사상은 위의 exact sequence와 $B\otimes_kk[\epsilon]$에 대한 같은 형태의 exact sequence 사이의 사상을 이루고, 양 끝에서 $\id_B$를 유도한다. 그럼 [\[호몰로지 대수학\] §Diagram chasing, ⁋따름정리 3](/ko/math/homological_algebra/diagram_chasing#cor3)에 의하여 $\Sigma$가 isomorphism이므로, 주어진 변형은 trivial하다.
:::

## Smooth한 경우의 분류

국소 자료가 사라지면 남는 것은 접합의 자유도뿐이다. 두 trivialization의 차이를 재는 것이 derivation이라는 사실이 이미 확보되어 있으므로 ([§매끄러운 사상과 에탈 사상, ⁋정리 15](/ko/math/scheme_theory/smooth_and_etale_morphisms#thm15)의 증명), 그 차이들이 이루는 cocycle이 답을 준다.

::: 정리 3
$X$가 $k$ 위에서 smooth한 scheme이면, $X$의 first-order deformation들의 isomorphism class 집합은 $H^1(X, \mathcal{T}_{X/k})$와 자연스럽게 일대일 대응한다. 이 대응 아래에서 trivial deformation은 $0$에 대응한다.
:::
::: 증명
$X$의 affine open cover $\{U_i\}$를 고정하자. First-order deformation $\mathcal{X}$가 주어지면 [명제 2](#prop2)에 의하여 각 조각 위에서 trivialization

$$\theta_i:\mathcal{X}\vert_{U_i}\overset{\sim}{\longrightarrow}U_i\times_{\Spec k}\Spec k[\epsilon]$$

를 고를 수 있다. 겹치는 곳 $U_{ij}=U_i\cap U_j$ 위에서 $\theta_i\circ\theta_j^{-1}$은 $U_{ij}\times\Spec k[\epsilon]$의 automorphism으로서 $U_{ij}$ 위에 항등사상을 유도한다. $X$가 separated이므로 $U_{ij}$는 affine이고, [§매끄러운 사상과 에탈 사상, ⁋정리 15](/ko/math/scheme_theory/smooth_and_etale_morphisms#thm15)의 증명이 보인 대로 그러한 두 lifting의 차이는 $\Der_k(\mathcal{O}_X(U_{ij}), \mathcal{O}_X(U_{ij}))$의 원소로 정확히 기술되며, 이 module은 $\mathcal{T}_{X/k}(U_{ij})$이다. ([§미분과 여접층, ⁋정의 7](/ko/math/scheme_theory/sheaf_of_differentials#def7) 직후의 계산) 곧 $\theta_i\circ\theta_j^{-1}=\id+\epsilon\vartheta_{ij}$ 꼴이며 $\vartheta_{ij}\in\mathcal{T}_{X/k}(U_{ij})$이다.

세 겹치는 곳에서 $\theta_i\theta_j^{-1}\circ\theta_j\theta_k^{-1}=\theta_i\theta_k^{-1}$이고 $\epsilon^2=0$이므로 $\vartheta_{ij}+\vartheta_{jk}=\vartheta_{ik}$가 성립하여 $(\vartheta_{ij})$는 Čech $1$-cocycle이다. 또 각 $\theta_i$를 $\id+\epsilon\eta_i$로 바꾸면 $\vartheta_{ij}$가 $\eta_i-\eta_j$만큼 달라지므로, cohomology class는 trivialization의 선택에 무관하다. Isomorphic한 두 변형에 대해서는 그 isomorphism으로 trivialization을 옮기면 같은 class를 주므로, 대응 $\mathcal{X}\mapsto[(\vartheta_{ij})]\in H^1(X, \mathcal{T}_{X/k})$가 well-defined하다.

거꾸로 cocycle $(\vartheta_{ij})$가 주어지면 $\id+\epsilon\vartheta_{ij}$를 gluing 자료로 삼아 $U_i\times\Spec k[\epsilon]$들을 이어 붙일 수 있고, cocycle 조건이 정확히 gluing이 성립할 조건이므로 ([\[위상수학\] §층, ⁋명제 8](/ko/math/topology/sheaves#prop8)) 이는 $k[\epsilon]$ 위에서 국소적으로 자명하여 flat한 scheme $\mathcal{X}$를 준다. 두 구성이 서로 역이고, coboundary로 옮겨지는 자료가 정확히 trivialization을 바꾼 것이므로 대응은 전단사이다. Trivial deformation은 모든 $\theta_i$를 주어진 trivialization의 제한으로 택하여 $\vartheta_{ij}=0$을 주므로 $0$에 대응한다.
:::

## 접층이 잃는 정보

$X$에 singularity가 있으면 위의 논법은 첫 걸음에서 깨진다. Affine 조각 자체가 비자명하게 변형되어 $T^1(B/k, B)\neq0$이 되므로, 접합의 자유도만으로는 변형을 다 세지 못하기 때문이다.

더 근본적인 문제는 [정리 3](#thm3)의 답에 등장한 $\mathcal{T}_{X/k}=\sHom_{\mathcal{O}_X}(\Omega_{X/k}, \mathcal{O}_X)$ 자체가 옳은 대상이 아니라는 데 있다. $\Omega_{X/k}$가 locally free가 아닌 곳에서 dual을 취하면 정보가 사라지며, 그 손실은 이미 관찰된 것이다. $A=k[t]$와 $B=k[t, \x, \y]/(\x\y-t)$의 경우 $\Der_A(B, B)$는 $\x\partial/\partial\x-\y\partial/\partial\y$가 생성하는 rank $1$의 free module로 어디에서나 rank가 $1$인 반면, $\Omega_{B/A}$는 원점에서 rank가 $2$로 뛴다. ([§미분과 여접층, ⁋정의 7](/ko/math/scheme_theory/sheaf_of_differentials#def7) 이후의 계산) 곧 $\mathcal{T}$에서 $\Omega$를 되찾을 수 없으며, singularity 근방의 변형 자료는 $\mathcal{T}$가 지워 버린 쪽에 들어 있다.

해결은 dual을 취하는 연산을 그 derived functor로 대체하는 것이다. $\sHom(\Omega_{X/k}, -)$의 derived functor가 $\mathcal{E}xt$이므로 ([\[층론\] §층의 유도 범주와 유도 functor, ⁋정의 7](/ko/math/sheaf_theory/derived_category_of_sheaves#def7)), $\mathcal{T}_{X/k}=\mathcal{E}xt^0(\Omega_{X/k}, \mathcal{O}_X)$은 이 계열의 $0$차 항일 뿐이고 잃어버린 자료는 $\mathcal{E}xt^1$에 남는다. 이것이 실제로 변형이론의 $T^i$와 일치한다는 것이 아래의 내용이다.

## 여접층의 Ext

이 일치는 조건 없이 성립하지는 않으며, naive 여접 복합체가 $\Omega_{X/k}$의 resolution이 되는 경우에 성립한다. 그 조건을 먼저 확인한다.

::: 명제 4
$X$가 codimension $k$의 local complete intersection, 곧 각 점의 어떤 근방에서 $\mathbb{A}^n_k$ 안의 길이 $k$짜리 regular sequence의 vanishing scheme과 isomorphic한 scheme이라 하자. ([§완전교차, ⁋정의 1](/ko/math/scheme_theory/complete_intersections#def1)) $X$가 reduced이고 그 smooth locus가 $X$에서 dense이면, 국소적인 closed embedding $X\vert_U\hookrightarrow V=\mathbb{A}^n_k$와 그 ideal sheaf $\mathcal{I}$에 대하여 sequence

$$0 \rightarrow \mathcal{I}/\mathcal{I}^2 \overset{\bar{d}}{\rightarrow} \Omega_{V/k}\vert_{X\vert_U} \rightarrow \Omega_{X/k}\vert_U \rightarrow 0$$

은 exact이다.
:::
::: 증명
오른쪽 두 항에서의 exactness는 conormal exact sequence이다. ([§미분과 여접층, ⁋명제 2](/ko/math/scheme_theory/sheaf_of_differentials#prop2)) 남은 것은 $\bar d$의 단사성이므로, $\mathcal{K}=\ker\bar d$가 $0$임을 보이면 된다.

먼저 $X$의 smooth locus $W$ 위에서 이를 확인한다. $W$ 위에서 $\Omega_{X/k}$는 rank $\dim X$의 locally free sheaf이고 ([§매끄러운 사상과 에탈 사상, ⁋정의 1](/ko/math/scheme_theory/smooth_and_etale_morphisms#def1)), $\Omega_{V/k}\vert_W$는 rank $n$의 locally free sheaf이다. 그럼 conormal exact sequence의 오른쪽 두 항이 주는 short exact sequence

$$0 \rightarrow \im\bar d \rightarrow \Omega_{V/k}\vert_W \rightarrow \Omega_{X/k}\vert_W \rightarrow 0$$

에서 오른쪽 항이 locally free이므로 이 sequence는 국소적으로 split하고, 따라서 $\im\bar d$는 rank $n-\dim X=k$의 locally free sheaf이다. 한편 $\mathcal{I}/\mathcal{I}^2$ 또한 rank $k$의 locally free sheaf이므로 ([§완전교차, ⁋명제 5](/ko/math/scheme_theory/complete_intersections#prop5)), $\bar d$는 같은 rank의 두 locally free sheaf 사이의 전사이다. 그 kernel은 rank $0$이면서 locally free sheaf의 subsheaf라 torsion이 없으므로 $0$이고, 곧 $\mathcal{K}\vert_W=0$이다.

이제 $W$가 $X$에서 dense이고 $X$가 reduced이므로, locally free sheaf $\mathcal{I}/\mathcal{I}^2$의 section이 $W$ 위에서 소멸하면 그 section은 $0$이다. 실제로 국소적으로 $\mathcal{I}/\mathcal{I}^2\cong\mathcal{O}_X^{\oplus k}$이므로 이는 $\mathcal{O}_X$의 section에 대한 주장으로 환원되고, $X$가 reduced이면 $f\in\mathcal{O}_X(U')$의 vanishing locus가 dense한 열린집합을 포함할 때 그 vanishing locus는 닫혀 있으면서 dense하여 $U'$ 전체이므로 $f$는 모든 local ring의 maximal ideal에 속하고, 곧 nilradical에 속해 $0$이다. 따라서 $\mathcal{K}=0$이다.
:::

::: 명제 5
[명제 4](#prop4)의 가정을 만족하는 $X$와 affine open subset $U=\Spec B\subseteq X$에 대하여, $i=0, 1$에서

$$T^i(B/k, B)\cong\Ext^i_B(\Omega_{B/k}, B)$$

가 성립한다. 따라서 $X$의 국소적인 변형 자료를 모은 층은 $\mathcal{E}xt^i_{\mathcal{O}_X}(\Omega_{X/k}, \mathcal{O}_X)$이다.
:::
::: 증명
$U$를 줄여 $B=P/I$ ($P=k[\x_1,\ldots,\x_n]$)이고 $I$가 길이 $k$의 $P$-regular sequence로 생성된다고 두어도 좋다. Naive 여접 복합체는

$$\operatorname{NL}_{B/k}=\bigl[I/I^2\overset{\bar d}{\longrightarrow}\Omega_{P/k}\otimes_PB\bigr]$$

이고 $T^i(B/k, B)$는 $\Hom_B(\operatorname{NL}_{B/k}, B)$의 cohomology이다. ([§변형이론과 여접 복합체, ⁋정의 5](/ko/math/scheme_theory/deformation_theory#def5))

[명제 4](#prop4)에 의하여 $\bar d$가 단사이므로 이 complex의 homology는 $H_1=0$과 $H_0=\Omega_{B/k}$뿐이고, 곧 augmentation $\operatorname{NL}_{B/k}\rightarrow\Omega_{B/k}$가 quasi-isomorphism이다. 두 항 가운데 $\Omega_{P/k}\otimes_PB$는 $\dd{\x_1},\ldots,\dd{\x_n}$을 기저로 하는 free $B$-module이고 ([\[가환대수학\] §미분, ⁋명제 5](/ko/math/commutative_algebra/differentials#prop5)), $I/I^2$은 rank $k$의 free $B$-module이므로 ([§완전교차, ⁋명제 5](/ko/math/scheme_theory/complete_intersections#prop5)), $\operatorname{NL}_{B/k}$는 $\Omega_{B/k}$의 길이 $1$짜리 free resolution이다. 그러므로 $\Hom_B(\operatorname{NL}_{B/k}, B)$의 cohomology는 정의에 의하여 $\Ext^i_B(\Omega_{B/k}, B)$이다. ([\[호몰로지 대수학\] §Ext와 Tor, ⁋명제 3](/ko/math/homological_algebra/ext_and_tor#prop3))

마지막 주장은 $\Ext$가 affine 위에서 associated sheaf와 교환하고 $\mathcal{E}xt$가 국소적인 대상이라는 것에서 따라온다. ([§준연접층, ⁋정리 7](/ko/math/scheme_theory/quasicoherent_sheaves#thm7))
:::

## 국소와 대역

이제 국소 자료 $\mathcal{E}xt^1$과 접합 자료 $H^1(\mathcal{T}_X)$가 어떻게 하나의 대역적인 $\Ext^1$을 이루는지가 spectral sequence 하나로 정리된다.

::: 정리 6
[명제 4](#prop4)의 가정을 만족하는 $X$에 대하여, exact sequence

$$0 \rightarrow H^1(X, \mathcal{T}_{X/k}) \rightarrow \Ext^1_{\mathcal{O}_X}(\Omega_{X/k}, \mathcal{O}_X) \rightarrow H^0(X, \mathcal{E}xt^1_{\mathcal{O}_X}(\Omega_{X/k}, \mathcal{O}_X)) \overset{d_2}{\rightarrow} H^2(X, \mathcal{T}_{X/k})$$

가 성립한다.
:::
::: 증명
Local-to-global $\Ext$ spectral sequence

$$E_2^{p, q}=H^p(X, \mathcal{E}xt^q_{\mathcal{O}_X}(\Omega_{X/k}, \mathcal{O}_X))\Longrightarrow \Ext^{p+q}_{\mathcal{O}_X}(\Omega_{X/k}, \mathcal{O}_X)$$

를 쓴다. 이는 $\Ext=H^\bullet(R\Gamma\circ R\sHom)$의 합성에 [\[층론\] §층의 유도 범주와 유도 functor, ⁋정리 10](/ko/math/sheaf_theory/derived_category_of_sheaves#thm10)을 적용하여 얻어지는 first quadrant spectral sequence이다.

이제 [\[대수다양체\] §층 코호몰로지, ⁋따름정리 20](/ko/math/algebraic_varieties/sheaf_cohomology#cor20)의 논법을 그대로 옮긴다. 그 증명이 사용한 것은 first quadrant라는 사실과 수렴의 정의뿐이므로 ([\[호몰로지 대수학\] §스펙트럼 열, ⁋명제 6](/ko/math/homological_algebra/spectral_sequences#prop6), [\[호몰로지 대수학\] §스펙트럼 열, ⁋정의 5](/ko/math/homological_algebra/spectral_sequences#def5)), 임의의 first quadrant spectral sequence에 적용된다. 곧 $(1, 0)$으로 드나드는 differential이 모두 $0$이라 $E_\infty^{1, 0}=E_2^{1, 0}$이고, $(0, 1)$에서는 $d_2:E_2^{0, 1}\rightarrow E_2^{2, 0}$만이 비자명할 수 있어 $E_\infty^{0, 1}=\ker d_2$이며, 전체 차수 $1$의 filtration이 두 조각으로 이루어져 있으므로 위의 다섯 항 sequence를 얻는다. 마지막으로 $\mathcal{E}xt^0(\Omega_{X/k}, \mathcal{O}_X)=\sHom(\Omega_{X/k}, \mathcal{O}_X)=\mathcal{T}_{X/k}$이다. ([§미분과 여접층, ⁋정의 7](/ko/math/scheme_theory/sheaf_of_differentials#def7))
:::

왼쪽 항과 오른쪽 항이 앞에서 말한 두 겹의 자유도이다. $H^1(X, \mathcal{T}_{X/k})$은 각 조각을 건드리지 않고 접합만 바꾸어 얻는 변형, 곧 국소적으로 자명한 변형이고, $H^0(X, \mathcal{E}xt^1)$은 각 점에서의 국소 변형을 대역적으로 고른 것이다. 가운데 항은 이 둘을 동시에 담으며, $d_2$는 국소 변형들의 선택이 실제로 하나의 대역적인 변형으로 접합되는지를 재는 obstruction이다.

::: 따름정리 7
$X$가 smooth이면 모든 $i$에 대하여 $\Ext^i_{\mathcal{O}_X}(\Omega_{X/k}, \mathcal{O}_X)\cong H^i(X, \mathcal{T}_{X/k})$이다.
:::
::: 증명
$X$가 smooth이면 $\Omega_{X/k}$가 locally free이므로 ([§매끄러운 사상과 에탈 사상, ⁋정의 1](/ko/math/scheme_theory/smooth_and_etale_morphisms#def1)) 국소적으로 그 자신이 free resolution이 되어 $q>0$에서 $\mathcal{E}xt^q(\Omega_{X/k}, \mathcal{O}_X)=0$이다. 그럼 [정리 6](#thm6)의 spectral sequence에서 $q>0$인 행이 전부 소멸하여 $E_2^{p, 0}=E_\infty^{p, 0}$이고, 곧 $\Ext^p=H^p(X, \mathcal{T}_{X/k})$이다.
:::

곧 [정리 3](#thm3)은 [정리 6](#thm6)의 특수한 경우이다. Smooth한 경우에 $\Ext$가 굳이 필요하지 않았던 이유는 $\mathcal{E}xt^1$이 통째로 소멸하여 국소 자료가 없었기 때문이다.

## Hypersurface의 국소 변형

$\mathcal{E}xt^1$이 실제로 무엇인지는 hypersurface에서 완전히 계산된다.

::: 예시 8
$V=\mathbb{A}^n_k$ 안의 reduced hypersurface $X=Z(f)$를 보자. Ideal sheaf는 $\mathcal{I}=(f)$이고 $\mathcal{I}/\mathcal{I}^2$은 $f$가 생성하는 rank $1$의 free $\mathcal{O}_X$-module이므로, [명제 5](#prop5)의 resolution은

$$\operatorname{NL}=\bigl[\mathcal{O}_X\overset{\bar d}{\longrightarrow}\mathcal{O}_X^{\oplus n}\bigr],\qquad \bar d(1)=\Bigl(\frac{\partial f}{\partial \x_1},\ldots,\frac{\partial f}{\partial \x_n}\Bigr)$$

이다. 이를 $\mathcal{O}_X$로 dual하면 $(a_1,\ldots, a_n)\mapsto \sum_ia_i\partial f/\partial \x_i$로 주어지는 사상 $\mathcal{O}_X^{\oplus n}\rightarrow\mathcal{O}_X$가 되고, 따라서

$$\mathcal{E}xt^1(\Omega_{X/k}, \mathcal{O}_X)\cong\mathcal{O}_X\big/\Bigl(\frac{\partial f}{\partial \x_1},\ldots,\frac{\partial f}{\partial \x_n}\Bigr)$$

를 얻는다. 오른쪽을 $f$의 *Tjurina algebra*라 부르며, 이는 $f$와 그 편미분들이 함께 생성하는 ideal로 $k[\x_1,\ldots,\x_n]$을 나눈 것이다. 특히 이 층은 $X$의 singular point에만 지지되는데, $f$의 편미분이 모두 소멸하는 점이 곧 singular point이기 때문이다.

두 개의 곡선 singularity에서 이를 계산해 보자. 먼저 $n=2$, $f=\x\y$이면 편미분은 $\y$와 $\x$이므로

$$\mathcal{E}xt^1=k[\x, \y]/(\x\y, \y, \x)=k$$

로 원점에 놓인 $1$차원 vector space이다. 다음으로 $f=\y^2-\x^3$이면 편미분은 $-3\x^2$과 $2\y$이고, $k$의 characteristic이 $2$도 $3$도 아니라 하면

$$\mathcal{E}xt^1=k[\x, \y]/(\y^2-\x^3, \x^2, \y)=k[\x]/(\x^2)$$

로 원점에 놓인 $2$차원 vector space이다. 두 singularity 모두 [정리 6](#thm6)에서 유한 차원의 국소 변형을 기여하며, 그 차원이 종류를 구별한다.
:::

첫째 계산이 주는 $1$차원은 방정식 $\x\y=0$을 $\x\y=t$로 흔드는 단 하나의 방향에 해당한다. 이 방향이 정확히 무엇을 하는지, 그리고 그런 singularity를 유한 개 가진 곡선에서 [정리 6](#thm6)이 어떤 모습이 되는지가 다음 글의 주제이다.

---

**참고문헌**

**[Har]** R. Hartshorne, *Deformation theory*, Graduate Texts in Mathematics 257, Springer, 2010.  
**[Ill]** L. Illusie, *Complexe cotangent et déformations I, II*, Lecture Notes in Mathematics 239, 283, Springer, 1971--1972.  
**[Ser]** E. Sernesi, *Deformations of algebraic schemes*, Grundlehren der mathematischen Wissenschaften 334, Springer, 2006.
