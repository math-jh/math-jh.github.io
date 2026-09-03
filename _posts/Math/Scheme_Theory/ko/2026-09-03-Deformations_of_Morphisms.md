---
title: "사상의 변형"
description: "곡선에서 smooth variety로 가는 morphism의 변형을 다룬다. Source를 고정하면 변형이 당김 tangent sheaf의 global section이고 lifting의 obstruction이 그 첫째 cohomology에 놓임을 Čech cocycle로 보인다. 이어서 domain까지 함께 흔드는 변형을 mapping cone이 정하는 complex의 Ext로 재고, distinguished triangle의 long exact sequence가 곡선 쪽 자료와 morphism 쪽 자료를 잇는 일곱 항 exact sequence를 줌을 확인한다. Nodal curve 위의 Riemann-Roch와 앞 글의 3g-3+n을 넣어 두 차원의 차를 닫힌 꼴로 계산한다."
excerpt: "Deformations of a morphism, the cone complex, and the tangent-obstruction sequence"

categories: [Math / Scheme Theory]
permalink: /ko/math/scheme_theory/deformations_of_morphisms
sidebar: 
    nav: "scheme_theory-ko"

date: 2026-09-03
weight: 27

published: false

---

앞의 두 글은 곡선 자체를 흔들었다. 이제 곡선 위에 사상 $\mu:C\rightarrow X$가 얹혀 있고, 곡선과 사상을 함께 흔드는 상황을 다룬다. 자료가 둘이므로 답도 두 겹이 되며, 그 둘을 잇는 것이 이 글의 마지막에 나오는 일곱 항 exact sequence이다.

순서는 쉬운 쪽부터이다. Domain을 고정하고 사상만 흔들면 변형과 obstruction이 당김 tangent sheaf의 cohomology로 곧바로 나오며, 이는 [§매끄러운 사상과 에탈 사상, ⁋정리 15](/ko/math/scheme_theory/smooth_and_etale_morphisms#thm15)의 lifting 판정을 Čech 자료로 조립한 것에 지나지 않는다. Domain까지 흔들면 [§Nodal curve의 변형, ⁋정의 5](/ko/math/scheme_theory/deformations_of_nodal_curves#def5)의 자료가 더해지고, 두 자료를 한 대상에 담는 것이 mapping cone이다.

이 글에서 $k$는 algebraically closed field이고, $X$는 $k$ 위의 smooth scheme, $C$는 $n$개의 marked point $p_1,\ldots, p_n$을 갖는 genus $g$의 prestable curve이며 $\Sigma=p_1+\cdots+p_n$이다. ([§Nodal curve의 변형, ⁋정의 1](/ko/math/scheme_theory/deformations_of_nodal_curves#def1)) 또 $k[\epsilon]=k[t]/(t^2)$로 적는다.

## Domain을 고정한 변형

::: 정의 1
Morphism $\mu:C\rightarrow X$의 *first-order deformation<sub>일차 변형</sub>*이란 $k[\epsilon]$-morphism

$$\mathcal{M}:C\times_{\Spec k}\Spec k[\epsilon]\longrightarrow X$$

로서 $C$로 제한하면 $\mu$가 되는 것을 뜻한다.
:::

여기서 domain은 곱 $C\times\Spec k[\epsilon]$으로 고정되어 있고 흔들리는 것은 사상뿐이다. $C$는 이 domain 안에 square-zero closed subscheme으로 앉아 있으며 그 ideal은 $\epsilon\mathcal{O}_C\cong\mathcal{O}_C$이므로, [§매끄러운 사상과 에탈 사상, ⁋정리 15](/ko/math/scheme_theory/smooth_and_etale_morphisms#thm15)가 그대로 적용되는 상황이다.

::: 명제 2
$\mu:C\rightarrow X$의 first-order deformation들의 집합은 $H^0(C, \mu^\ast\mathcal{T}_{X/k})$와 자연스럽게 일대일 대응하며, 이 대응은 자명한 변형 $\mu\circ\mathrm{pr}_1$을 $0$으로 보낸다.
:::
::: 증명
$C$의 affine open cover $\{U_i=\Spec B_i\}$를 $\mu(U_i)$가 affine $\Spec A_i\subseteq X$에 담기도록 고르자. $U_i$ 위에서 [정의 1](#def1)의 자료는 $\mu^\sharp:A_i\rightarrow B_i$를 $B_i[\epsilon]\rightarrow B_i$를 따라 올리는 $k$-algebra homomorphism $A_i\rightarrow B_i[\epsilon]$이고, [§매끄러운 사상과 에탈 사상, ⁋정리 15](/ko/math/scheme_theory/smooth_and_etale_morphisms#thm15)의 증명이 보인 대로 두 lifting의 차이는 정확히 $\Der_k(A_i, B_i)$의 원소이다. 여기서 $B_i$는 $\mu^\sharp$를 통한 $A_i$-module이다.

한편 $\Omega_{X/k}$의 universal property와 base change에 의하여

$$\Der_k(A_i, B_i)\cong\Hom_{A_i}(\Omega_{A_i/k}, B_i)\cong\Hom_{B_i}(\Omega_{A_i/k}\otimes_{A_i}B_i, B_i)$$

이고 ([\[가환대수학\] §미분, ⁋보조정리 2](/ko/math/commutative_algebra/differentials#lem2)), 오른쪽은 $\mu^\ast\Omega_{X/k}\vert_{U_i}$의 dual의 절편이다. $X$가 smooth라 $\Omega_{X/k}$가 locally free이므로 그 당김도 locally free이고, 따라서 이 dual은 $\mu^\ast\mathcal{T}_{X/k}$이다. 곧 각 $U_i$ 위에서 lifting들의 집합은 $(\mu^\ast\mathcal{T}_{X/k})(U_i)$ 위의 torsor이다.

이제 자명한 lifting $\mu\circ\mathrm{pr}_1$이 대역적으로 존재하므로 이 torsor들은 모두 기준점을 가지며, 임의의 lifting과 자명한 lifting의 차이를 취하면 각 $U_i$ 위의 절편을 얻는다. 이들은 겹치는 곳에서 같은 두 lifting의 차이이므로 일치하여 하나의 대역적 절편을 이루고, 거꾸로 대역적 절편은 자명한 lifting에 더하여 대역적 lifting을 준다. 두 구성이 서로 역이므로 주장을 얻는다.
:::

Domain을 흔들면 lifting이 대역적으로 존재하리라는 보장이 없어지고, 그 실패가 첫째 cohomology에 기록된다.

::: 명제 3
$(C, p_\bullet)$의 first-order deformation $\mathcal{C}$가 주어졌다 하자. 그럼 $\mu$를 $\mathcal{C}\rightarrow X$로 연장하는 데 대한 obstruction

$$\mathrm{ob}(\mathcal{C})\in H^1(C, \mu^\ast\mathcal{T}_{X/k})$$

가 자연스럽게 정의되며, 연장이 존재하는 것은 $\mathrm{ob}(\mathcal{C})=0$인 것과 동치이다.
:::
::: 증명
$\mathcal{C}$는 $C$와 같은 위상공간을 가지므로 [명제 2](#prop2)의 cover $\{U_i\}$를 그대로 쓸 수 있고, $\mathcal{C}\vert_{U_i}$는 affine scheme $U_i$의 square-zero thickening이라 affine이다. 그럼 $X$가 smooth이므로 [§매끄러운 사상과 에탈 사상, ⁋정리 15](/ko/math/scheme_theory/smooth_and_etale_morphisms#thm15)의 첫째 주장이 각 $U_i$ 위에서 lifting $\varrho_i:\mathcal{C}\vert_{U_i}\rightarrow X$의 존재를 준다.

겹치는 곳 $U_{ij}$에서 $\varrho_i$와 $\varrho_j$는 같은 $\mu\vert_{U_{ij}}$의 두 lifting이므로, [명제 2](#prop2)의 증명이 보인 대로 그 차이는 $\tau_{ij}\in(\mu^\ast\mathcal{T}_{X/k})(U_{ij})$이다. 세 겹치는 곳에서 차이들이 더해지므로 $\tau_{ij}+\tau_{jk}=\tau_{ik}$가 성립하여 $(\tau_{ij})$는 Čech $1$-cocycle이고, 각 $\varrho_i$를 절편 $\eta_i$만큼 바꾸면 $\tau_{ij}$가 $\eta_i-\eta_j$만큼 달라지므로 그 class는 lifting의 선택에 무관하다. 이를 $\mathrm{ob}(\mathcal{C})$로 정의한다.

이 class가 $0$이라는 것은 적당한 $(\eta_i)$로 모든 $\tau_{ij}$를 없앨 수 있다는 것, 곧 $\varrho_i$들을 겹치는 곳에서 일치하도록 고칠 수 있다는 것이고, 그렇게 고친 lifting들은 하나의 대역적 사상 $\mathcal{C}\rightarrow X$로 붙는다. 역방향은 대역적 lifting의 제한을 $\varrho_i$로 택하면 $\tau_{ij}=0$이다.
:::

## 쌍의 변형을 재는 complex

두 자료를 하나로 담는 대상은 codifferential이 정하는 mapping cone이다. Morphism $\mu$는 $\mu^\ast\Omega_{X/k}\rightarrow\Omega_{C/k}$를 유도하고 ([§미분과 여접층, ⁋명제 1](/ko/math/scheme_theory/sheaf_of_differentials#prop1)), 이를 $\Omega_{C/k}\subseteq\Omega_{C/k}(\Sigma)$와 합성한다.

::: 정의 4
Morphism $\mu:C\rightarrow X$와 marked point들에 대하여, codifferential $\mathrm{d}\mu^\vee:\mu^\ast\Omega_{X/k}\rightarrow\Omega_{C/k}(\Sigma)$의 mapping cone

$$L_\mu=\Cone\bigl(\mu^\ast\Omega_{X/k}\longrightarrow\Omega_{C/k}(\Sigma)\bigr)$$

을 두고 ([\[호몰로지 대수학\] §긴 완전열, ⁋정의 8](/ko/math/homological_algebra/long_exact_sequence#def8)), $T^i(C, p_\bullet, \mu)=\Ext^i_{\mathcal{O}_C}(L_\mu, \mathcal{O}_C)$로 적는다.
:::

이 정의가 옳은 이유는 아래 [정리 5](#thm5)가 $T^i$를 곡선 쪽 자료와 사상 쪽 자료로 정확히 갈라 놓는 데 있다. 두 극단에서 이미 계산된 것이 그 두 자료이다.

::: 정리 5
위의 상황에서 exact sequence

$$0 \rightarrow T^0(C, p_\bullet, \mu) \rightarrow T^0(C, p_\bullet) \rightarrow H^0(C, \mu^\ast\mathcal{T}_{X/k}) \rightarrow T^1(C, p_\bullet, \mu) \rightarrow T^1(C, p_\bullet) \rightarrow H^1(C, \mu^\ast\mathcal{T}_{X/k}) \rightarrow T^2(C, p_\bullet, \mu) \rightarrow 0$$

이 성립한다.
:::
::: 증명
[정의 4](#def4)의 mapping cone은 derived category에서 distinguished triangle

$$\mu^\ast\Omega_{X/k}\longrightarrow\Omega_{C/k}(\Sigma)\longrightarrow L_\mu\longrightarrow \mu^\ast\Omega_{X/k}[1]$$

을 이룬다. ([\[호몰로지 대수학\] §유도카테고리, ⁋정의 11](/ko/math/homological_algebra/derived_categories#def11)) 여기에 첫째 변수에 대한 반변 functor $R\Hom_{\mathcal{O}_C}(-, \mathcal{O}_C)$를 적용하면 다시 distinguished triangle을 얻으며 ([\[호몰로지 대수학\] §유도카테고리, ⁋명제 12](/ko/math/homological_algebra/derived_categories#prop12)), 그 cohomology를 취하면 mapping cone의 long exact sequence가 ([\[호몰로지 대수학\] §긴 완전열, ⁋정의 8](/ko/math/homological_algebra/long_exact_sequence#def8) 직후)

$$\cdots \rightarrow \Ext^i(L_\mu, \mathcal{O}_C) \rightarrow \Ext^i(\Omega_{C/k}(\Sigma), \mathcal{O}_C) \rightarrow \Ext^i(\mu^\ast\Omega_{X/k}, \mathcal{O}_C) \rightarrow \Ext^{i+1}(L_\mu, \mathcal{O}_C) \rightarrow\cdots$$

를 준다.

이제 세 종류의 항을 각각 정리한다. 첫째, $\Ext^i(\Omega_{C/k}(\Sigma), \mathcal{O}_C)$은 정의에 의하여 $T^i(C, p_\bullet)$이다. ([§Nodal curve의 변형, ⁋정의 5](/ko/math/scheme_theory/deformations_of_nodal_curves#def5)) 둘째, $\mu^\ast\Omega_{X/k}$가 locally free이므로 $q>0$에서 $\mathcal{E}xt^q(\mu^\ast\Omega_{X/k}, \mathcal{O}_C)=0$이고, 따라서 [§스킴의 변형, ⁋따름정리 7](/ko/math/scheme_theory/deformations_of_schemes#cor7)과 같은 이유로

$$\Ext^i(\mu^\ast\Omega_{X/k}, \mathcal{O}_C)=H^i(C, \sHom(\mu^\ast\Omega_{X/k}, \mathcal{O}_C))=H^i(C, \mu^\ast\mathcal{T}_{X/k})$$

이다. 셋째, sequence가 $i=1$ 다음에서 끊어지는 것은 $\Ext^2(\Omega_{C/k}(\Sigma), \mathcal{O}_C)=0$이기 때문이다. 실제로 [§스킴의 변형, ⁋정리 6](/ko/math/scheme_theory/deformations_of_schemes#thm6)의 spectral sequence에서 $\Ext^2$에 기여할 수 있는 항은 $E_2^{2, 0}$과 $E_2^{1, 1}$뿐인데, 앞의 것은 $H^2(C, \mathcal{T}_{C/k}(-\Sigma))$이라 [§Nodal curve의 변형, ⁋보조정리 7](/ko/math/scheme_theory/deformations_of_nodal_curves#lem7)로 소멸하고, 뒤의 것은 node에 지지된 skyscraper의 $H^1$이라 소멸한다. ([§Nodal curve의 변형, ⁋명제 3](/ko/math/scheme_theory/deformations_of_nodal_curves#prop3)) 또 $\Ext^i$는 $i<0$에서 소멸하므로 sequence가 왼쪽 끝에서 $0$으로 시작한다.
:::

이 sequence의 각 항이 무엇을 재는지는 이미 확보되어 있다. 오른쪽 두 항 $H^i(C, \mu^\ast\mathcal{T}_{X/k})$은 [명제 2](#prop2)와 [명제 3](#prop3)에 의하여 domain을 고정한 사상의 변형과 그 lifting의 obstruction이고, 가운데 두 항 $T^i(C, p_\bullet)$은 [§Nodal curve의 변형, ⁋정리 8](/ko/math/scheme_theory/deformations_of_nodal_curves#thm8)이 계산한 곡선 쪽 자료이다. 그럼 sequence는 다음과 같이 읽힌다. 곡선의 무한소 automorphism 가운데 $\mu$를 보존하는 것이 $T^0(C, p_\bullet, \mu)$이고, 도중의 $T^1(C, p_\bullet, \mu)$은 domain을 고정한 사상의 변형과 곡선 자체의 변형을 함께 담되 곡선의 automorphism으로 옮겨지는 만큼을 상쇄한 것이며, $T^1(C, p_\bullet)\rightarrow H^1(C, \mu^\ast\mathcal{T}_{X/k})$은 [명제 3](#prop3)의 $\mathrm{ob}$ 그 자체이다. 마지막 $T^2$은 그 obstruction 사상의 cokernel이므로, 곡선 쪽에서 이미 실현된 변형을 제외하고 남은 obstruction만을 담는다.

$T^0(C, p_\bullet, \mu)=0$인 경우가 특히 중요하다. 이는 $\mu$를 보존하는 곡선의 무한소 automorphism이 없다는 것, 곧 $(C, p_\bullet, \mu)$의 automorphism group이 유한하다는 안정성 조건의 무한소 형태이다. 이 경우 [정리 5](#thm5)는 여섯 항으로 줄어든다.

## 차원

::: 보조정리 6
Genus $g$의 prestable curve $C$와 그 위의 rank $r$인 locally free sheaf $\mathcal{E}$에 대하여

$$\chi(C, \mathcal{E})=\deg\mathcal{E}+r(1-g)$$

이다. 여기서 $\deg\mathcal{E}$는 normalization $\nu:\widetilde{C}\rightarrow C$ 위에서 잰 $\nu^\ast\mathcal{E}$의 차수이다.
:::
::: 증명
[§Nodal curve의 변형, ⁋명제 2](/ko/math/scheme_theory/deformations_of_nodal_curves#prop2)의 증명이 쓴 exact sequence에 locally free sheaf $\mathcal{E}$를 tensor하면, projection formula에 의하여 $\mathcal{E}\otimes\nu_\ast\mathcal{O}_{\widetilde{C}}=\nu_\ast(\nu^\ast\mathcal{E})$이므로

$$0 \rightarrow \mathcal{E} \rightarrow \nu_\ast(\nu^\ast\mathcal{E}) \rightarrow \bigoplus_{p\in\operatorname{Sing}C}\mathcal{E}\otimes k(p) \rightarrow 0$$

을 얻는다. Node의 개수를 $\delta$, irreducible component의 개수를 $\gamma$, normalization의 성분 genus를 $g_j$라 하면 오른쪽 항의 $\chi$가 $\delta r$이므로, 같은 명제의 증명이 쓴 $H^i(C, \nu_\ast\mathcal{G})=H^i(\widetilde{C}, \mathcal{G})$와 성분별 Riemann--Roch에 의하여

$$\chi(C, \mathcal{E})=\sum_j\bigl(\deg\nu^\ast\mathcal{E}\vert_{\widetilde{C}_j}+r(1-g_j)\bigr)-\delta r=\deg\mathcal{E}+r\Bigl(\gamma-\sum_jg_j-\delta\Bigr)$$

이다. [§Nodal curve의 변형, ⁋명제 2](/ko/math/scheme_theory/deformations_of_nodal_curves#prop2)가 $\gamma-\sum_jg_j-\delta=1-g$를 주므로 주장을 얻는다.
:::

::: 따름정리 7
$T^0(C, p_\bullet, \mu)=0$이면

$$\dim T^1(C, p_\bullet, \mu)-\dim T^2(C, p_\bullet, \mu)=\deg\mu^\ast\mathcal{T}_{X/k}+(\dim X-3)(1-g)+n$$

이다.
:::
::: 증명
[정리 5](#thm5)의 exact sequence에서 차원의 교대합이 $0$이므로

$$\dim T^1(C, p_\bullet, \mu)-\dim T^2(C, p_\bullet, \mu)=\chi(C, \mu^\ast\mathcal{T}_{X/k})+\bigl(\dim T^1(C, p_\bullet)-\dim T^0(C, p_\bullet)\bigr)$$

이다. 오른쪽 첫 항은 $\mu^\ast\mathcal{T}_{X/k}$의 rank가 $\dim X$이므로 [보조정리 6](#lem6)에 의하여 $\deg\mu^\ast\mathcal{T}_{X/k}+\dim X(1-g)$이고, 둘째 항은 [§Nodal curve의 변형, ⁋따름정리 9](/ko/math/scheme_theory/deformations_of_nodal_curves#cor9)에 의하여 $3g-3+n$이다. 둘을 더하면

$$\deg\mu^\ast\mathcal{T}_{X/k}+\dim X(1-g)+3g-3+n=\deg\mu^\ast\mathcal{T}_{X/k}+(\dim X-3)(1-g)+n$$

을 얻는다.
:::

이 값이 $\mu$의 차수와 $\dim X$, $g$, $n$이라는 이산적인 자료만으로 결정된다는 것이 요점이다. 두 차원 $\dim T^1$과 $\dim T^2$은 각각 $\mu$를 움직이면 뛸 수 있지만 그 차는 뛰지 않는다.

::: 예시 8
두 극단에서 이를 확인한다. 먼저 $X=\mathbb{P}^r$, $C=\mathbb{P}^1$, $n=0$이고 $\mu$가 직선 위로의 isomorphism이라 하자. $\mu$가 embedding이라 $\mu\circ\phi=\mu$인 $\mathbb{P}^1$의 automorphism은 항등뿐이고, 따라서 $T^0(C, p_\bullet, \mu)=0$이라 [따름정리 7](#cor7)을 쓸 수 있다. [§미분과 여접층, ⁋정리 10](/ko/math/scheme_theory/sheaf_of_differentials#thm10)에 의하여 $\mathcal{T}_{\mathbb{P}^r}$의 차수는 직선 위에서 $r+1$이므로, $g=0$에서

$$\dim T^1-\dim T^2=(r+1)+(r-3)+0=2r-2$$

이다. 실제로 $\mu^\ast\mathcal{T}_{\mathbb{P}^r}=\mathcal{O}(2)\oplus\mathcal{O}(1)^{\oplus(r-1)}$이라 $H^1=0$이고, [정리 5](#thm5)에서 $T^1(C, p_\bullet)=H^1(\mathbb{P}^1, \mathcal{O}(2))=0$이므로 $T^2=0$이다. 곧 이 경우 obstruction이 없고 $\dim T^1=2r-2$이며, 이는 $\mathbb{P}^r$ 안의 직선들이 이루는 $\Gr(2, r+1)$의 차원과 일치한다.

반대쪽 극단으로 $C$가 marked point 하나를 갖는 smooth genus $1$ 곡선이고 $\mu$가 상수사상이라 하자. $\mu^\ast\mathcal{T}_{X/k}=\mathcal{O}_C^{\oplus d}$ ($d=\dim X$)이므로 $h^0=h^1=d$이고, $\mathcal{T}_{C/k}(-\Sigma)=\mathcal{O}_C(-p)$이라 $h^0=0$, $h^1=1$이며 곧 $T^0(C, p)=0$, $T^1(C, p)=1$이다. 상수사상은 domain을 어떻게 흔들어도 그대로 연장되므로 [명제 3](#prop3)의 $\mathrm{ob}$이 $0$ 사상이고, 따라서 [정리 5](#thm5)는 $\dim T^1=d+1$과 $\dim T^2=d$를 준다. 차는 $1=0+(d-3)\cdot0+1$로 [따름정리 7](#cor7)과 맞는다. 여기서는 $T^2$이 $0$이 아니며, 그 $d$차원이 상수사상들의 족이 기대보다 두꺼워지는 정도를 정확히 기록한다.
:::

둘째 경우처럼 $T^2\neq0$이면 변형들의 moduli는 기대 차원보다 큰 성분을 가질 수 있고, 그 위에서 intersection theory를 하려면 fundamental class를 대체할 class가 필요하다. [따름정리 7](#cor7)의 우변이 그 class가 놓여야 할 차원이다.

---

**참고문헌**

**[ACG]** E. Arbarello, M. Cornalba, P. A. Griffiths, *Geometry of algebraic curves II*, Grundlehren der mathematischen Wissenschaften 268, Springer, 2011.  
**[BF]** K. Behrend, B. Fantechi, *The intrinsic normal cone*, Invent. Math. **128** (1997), 45--88.  
**[Har]** R. Hartshorne, *Deformation theory*, Graduate Texts in Mathematics 257, Springer, 2010.  
**[Ser]** E. Sernesi, *Deformations of algebraic schemes*, Grundlehren der mathematischen Wissenschaften 334, Springer, 2006.
