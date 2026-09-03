---
title: "변형이론과 여접 복합체"
description: "Square-zero 확대를 따른 변형과 장애를 통해 Kähler differential만으로는 부족한 이유를 밝히고, naive 여접 복합체의 H_0·H_1이 변형이론적으로 무엇을 재는지, 그리고 완전한 여접 복합체가 왜 필요한지를 동기화한다."
excerpt: "Square-zero extensions, first-order deformations T^1, obstructions T^2, and why Ω is not enough"

categories: [Math / Scheme Theory]
permalink: /ko/math/scheme_theory/deformation_theory
sidebar:
  nav: "scheme_theory-ko"

date: 2026-09-03

weight: 22

published: false
---

일반적으로 $A$-module $M$에 대하여 tensor product functor $-\otimes_A M$은 right exact functor이므로, 임의의 short exact sequence

$$0 \rightarrow N' \rightarrow N \rightarrow N'' \rightarrow 0$$

에 tensor product functor $-\otimes_AM$를 취하면 다음의 exact sequence

$$N'\otimes_A M \rightarrow N\otimes_A M \rightarrow N''\otimes_A M \rightarrow 0$$

까지밖에 얻을 수 없었다. 즉, 왼쪽 끝에 $0$을 덧붙여 단사성을 보장하는 것은 일반적으로 불가능하며, 이와 같이 단사성이 깨지는 결함을 보정하기 위하여 $-\otimes_A M$의 left derived functor를 취해 $\Tor$ functor들을 정의하였다. ([\[호몰로지 대수학\] §Ext와 Tor, ⁋정의 2](/ko/math/homological_algebra/ext_and_tor#def2)) 그럼 이 정의 하에서 위 sequence는 다음의 long exact sequence

$$\cdots \rightarrow \Tor_1^A(N'', M) \rightarrow N'\otimes_A M \rightarrow N\otimes_A M \rightarrow N''\otimes_A M \rightarrow 0$$

로 연장되며, 따라서 주어진 sequence에 tensor product를 취한 결과가 왼쪽 끝에서도 exact이기 위한 필요충분조건은 그 앞을 가로막는 첫 번째 derived functor $\Tor_1^A(N'', M)$이 소멸하는 것이다. 가령 [\[가환대수학\] §평탄성, ⁋명제 1](/ko/math/commutative_algebra/flatness#prop1)에서 우리는 ideal $\mathfrak{a}\subseteq A$에 대한 short exact sequence 

$$0\rightarrow\mathfrak{a}\rightarrow A\rightarrow A/\mathfrak{a}\rightarrow0$$

에 tensor product를 취했을 때, multiplication map $\mathfrak{a}\otimes_A M \rightarrow M$이 injective가 되는 것은 $\Tor_1^A(A/\mathfrak{a}, M)=0$과 동치라는 것을 확인하였다.

이와 마찬가지로, Kähler differential이 주는 conormal exact sequence 또한 일반적인 algebra에 대해서는 right exact만 보장된다. 즉, $A$-algebra $B$와 ideal $\mathfrak{a}\subseteq B$에 대하여 $C=B/\mathfrak{a}$라 할 때, [§미분과 여접층, ⁋명제 2](/ko/math/scheme_theory/sheaf_of_differentials#prop2)의 conormal exact sequence

$$\mathfrak{a}/\mathfrak{a}^2 \overset{\bar{d}}{\longrightarrow} \Omega_{B/A}\otimes_B C \longrightarrow \Omega_{C/A} \longrightarrow 0$$

에서 왼쪽 끝의 $\bar{d}$가 injective가 될 이유는 없으며, 우리는 위에서 $\otimes_AM$의 결함을 right derived functor $\Tor_1$로 확인했듯 이 exact sequence를 derive하여 그 결함을 측정할 수 있다. 이로부터 정의되는 것이 naive cotangent complex이며, 이를 통해 우리는 smoothness의 판정을 homological algebra의 언어로 옮겨줄 수 있다. 

한편 기하적으로 이 소멸의 기하학적 의미는 [§매끄러운 사상과 에탈 사상, ⁋정리 15](/ko/math/scheme_theory/smooth_and_etale_morphisms#thm15)에 담겨있다. 이에 따르면 square-zero extension 

$$0\rightarrow\mathfrak{b}\rightarrow R\rightarrow R_0\rightarrow0$$

를 따른 lifting $\rho:C\rightarrow R$의 존재가 smoothness를 주며, 이를 위해 우리는 cotangent complex를 도입하기로 약속하였다. 

여기서 관점을 전환하면, infinitesimal lifting criterion은 단순히 주어진 대상의 smoothness를 검사하는 도구에 그치지 않는다. 거꾸로 square-zero extension을 대상을 얹을 base로 삼아 그 위로 대상을 들어올리는 문제를 생각하면, lifting의 존재와 유일성을 따지는 질문은 대상을 무한소만큼 흔들어 연속적인 family를 구성하는 문제, 곧 *deformation theory*의 중심 과제로 변모한다. 대상이 smooth하지 않을 때 발생하는 lifting의 비유일성은 first-order deformation의 다양한 가능성을, lifting의 불가능성은 변형을 가로막는 obstruction을 정확히 가리키기 때문이다. 결국 smoothness의 결함을 측정하기 위해 고안되었던 cotangent complex와 그 dual이, deformation theory에서 변형을 분류하고 obstruction을 계산하는 가장 근본적인 대수적 기계로 작동하게 된다.

## 평탄변형과 일차변형

대수기하학에서 주어진 기하학적 대상 $X$를 "연속적으로 변형한다"는 것은, base scheme $S$와 기준점 $s_0\in S$에 대하여 $s_0$에서의 central fiber가 $X$와 동형인 family $\pi:\mathcal{X}\rightarrow S$를 구성하는 문제를 뜻한다. 만약 이러한 변형들을 매개하는 moduli space가 존재한다면, $X$ 근방에서 moduli space의 국소적인 기하, 특히 $X$에 대응하는 점에서의 tangent space를 관찰하기 위해서는 $S$ 전체를 다룰 필요 없이 기준점 $s_0$의 1차 infinitesimal neighborhood만 살펴보면 충분하다.

스킴 이론에서 한 점의 접벡터 방향은 위상공간으로서는 단 하나의 점이지만 nilpotent 방향을 품고 있는 스킴 $\Spec \mathbb{K}[\epsilon]/(\epsilon^2)$ (dual numbers)로 실현된다. 따라서 $X$의 first-order deformation이란 이 두꺼워진 점 $\Spec \mathbb{K}[\epsilon]$ 위로 $X$를 얹는 family를 뜻한다. 더 나아가 고차 infinitesimal deformation은 [§매끄러운 사상과 에탈 사상, §§Infinitesimal lifting criterion](/ko/math/scheme_theory/smooth_and_etale_morphisms#infinitesimal-lifting-criterion)에서 다룬 square-zero extension $0\rightarrow M\rightarrow A'\rightarrow A\rightarrow0$ ($M^2=0$)를 따라 base $\Spec A\hookrightarrow \Spec A'$을 점진적으로 두껍게 만드는 문제로 이해할 수 있다.

이러한 family를 다룰 때 가장 핵심적인 기하학적 조건은 *flatness*이다. 임의의 사상 $\pi:\mathcal{X}\rightarrow S$를 허용하면 fiber의 차원이 불연속적으로 뛰거나 원치 않는 성분이 불쑥 나타날 수 있어, "fiber들이 연속적으로 변한다"는 기하학적 직관이 무너진다. Flatness는 fiber들이 base를 따라 일정한 대수적 크기를 유지하며 연속적으로 변하도록 보장하는 조건이다. 특히 first-order deformation $\mathcal{X}\rightarrow \Spec \mathbb{K}[\epsilon]$의 경우, 위상공간으로서는 $\mathcal{X}$와 원래 대상 $X$가 완전히 동일하며 오직 structure sheaf만이 $\epsilon$ 방향으로 두꺼워질 뿐이다. 이때 flatness는 $X$를 정의하는 방정식들과 그들 사이의 syzygy가 무한소 방향 $\epsilon$을 따라 붕괴하지 않고 균일하게 보존된다는 것을 보증한다. 이제 대수적 언어로 변형을 정의한다.

::: 정의 1
$A$-algebra $C$와 square-zero extension $0\rightarrow M\rightarrow A'\rightarrow A\rightarrow0$이 주어졌다 하자. $C$의 $A'$ 위로의 *변형<sub>deformation</sub>*이란, $A'$ 위에서 flat한 $A'$-algebra $C'$과 $A'$-algebra isomorphism $C'\otimes_{A'}A\cong C$의 짝을 뜻한다. 두 변형 $C', C''$이 *isomorphic*이라는 것은 $A$ 위로 환원했을 때 $C$ 위의 항등사상을 유도하는 $A'$-algebra isomorphism $C'\cong C''$이 존재하는 것이다.

특히 $A=\mathbb{K}$이고 $A'=\mathbb{K}[\epsilon]$인 경우의 변형을 $C$의 *first-order deformation<sub>일차 변형</sub>*이라 부른다.
:::

직관적으로 first-order deformation은 $C$를 정의하는 방정식들의 계수를 $\epsilon$의 일차까지 흔든 것이다. $C=B/\mathfrak{a}$를 polynomial ring $B=\mathbb{K}[\x_1,\ldots,\x_n]$의 quotient로 쓰고 $\mathfrak{a}=(f_1,\ldots,f_m)$이라 하면, 각 $f_j$를 $F_j=f_j+\epsilon g_j$로 흔들어 $C'=B[\epsilon]/(F_1,\ldots,F_m)$을 얻는 것이 후보가 된다. 그러나 임의의 $g_j$가 모두 flat한 변형을 주지는 않는다. Flatness라는 제약이 어떤 $g_j$가 허용되는지를 정확히 결정하며, 이것이 변형이론의 출발점이다.

::: 명제 2
$C=B/\mathfrak{a}$, $B=\mathbb{K}[\x_1,\ldots,\x_n]$, $\mathfrak{a}=(f_1,\ldots,f_m)$이라 하고, $g_1,\ldots,g_m\in B$에 대하여 $F_j=f_j+\epsilon g_j$, $C'=B[\epsilon]/(F_1,\ldots,F_m)$이라 하자. 그럼 $C'$이 $\mathbb{K}[\epsilon]$ 위에서 flat한 것은, $(f_1,\ldots,f_m)$의 모든 syzygy $(a_1,\ldots,a_m)$, 곧 $\sum_ja_jf_j=0$인 $(a_j)\in B^m$에 대하여

$$\sum_{j}a_jg_j\in \mathfrak{a}$$

이 성립하는 것과 동치이다. 이 조건이 성립할 때, syzygy $(a_j)$는 $(F_1,\ldots,F_m)$의 syzygy로 들어올려진다.
:::
::: 증명
$\mathbb{K}[\epsilon]=\mathbb{K}[t]/(t^2)$이므로 [\[가환대수학\] §평탄성, ⁋따름정리 2](/ko/math/commutative_algebra/flatness#cor2)에 의하여 $C'$이 flat한 것은 곱셈 $\times\epsilon:C'/\epsilon C'\rightarrow\epsilon C'$이 isomorphism인 것과 동치이다. $C'/\epsilon C'=B[\epsilon]/((F_j)+\epsilon B[\epsilon])=B/(f_j)=C$이므로, 이는 다음 sequence

$$0\rightarrow C\overset{\times\epsilon}{\rightarrow}C'\rightarrow C\rightarrow0$$

가 exact, 곧 $\times\epsilon:C\rightarrow C'$이 injective인 것과 같다. 이 morphism은 $b+\mathfrak{a}\mapsto\overline{\epsilon b}$로 주어지므로, injectivity는 "$\epsilon b\in(F_1,\ldots,F_m)$이면 $b\in \mathfrak{a}$"라는 명제와 동치이다.

이제 $\epsilon b\in(F_j)$이 무엇을 뜻하는지 풀어 쓰자. $A_j=a_j+\epsilon b_j$ ($a_j, b_j\in B$)에 대하여

$$\sum_jA_jF_j=\sum_ja_jf_j+\epsilon\Bigl(\sum_ja_jg_j+\sum_jb_jf_j\Bigr)$$

이고, $\epsilon^2=0$을 사용하였다. 따라서 $\sum_jA_jF_j=\epsilon b$인 것은 $\sum_ja_jf_j=0$이며 $\sum_ja_jg_j+\sum_jb_jf_j=b$인 것과 같다. 곧 $\epsilon b\in(F_j)$인 것은, $(f_j)$의 어떤 syzygy $(a_j)$가 존재하여 $b-\sum_ja_jg_j\in \mathfrak{a}$인 것과 동치이다.

그러므로 $\times\epsilon$이 injective인 것은, 모든 syzygy $(a_j)$에 대하여 $\sum_ja_jg_j\in \mathfrak{a}$인 것과 동치이다. 마지막으로 이 조건이 성립하여 $\sum_ja_jg_j=\sum_jc_jf_j$ ($c_j\in B$)라면, $A_j=a_j-\epsilon c_j$로 두면

$$\sum_jA_jF_j=\sum_ja_jf_j+\epsilon\Bigl(\sum_ja_jg_j-\sum_jc_jf_j\Bigr)=0$$

이므로 syzygy $(a_j)$가 $(F_j)$의 syzygy로 들어올려진다.
:::

이 명제는 flat한 first-order deformation을 매우 구체적으로 기술한다. 곧 flatness는 정확히 "원래 방정식들 사이의 모든 관계가 흔들린 방정식들 사이의 관계로 살아남는다"는 조건이다. 한 가지 관찰을 덧붙이면, $\sum_ja_jf_j=0$인 syzygy에 대하여 조건 $\sum_ja_jg_j\in \mathfrak{a}$는 $C$ 위에서 $\sum_j\overline{a_j}\overline{g_j}=0$으로 적힌다. 따라서 대응 $\overline{f_j}\mapsto\overline{g_j}$는 $C$-module homomorphism

$$\varphi:\mathfrak{a}/\mathfrak{a}^2\rightarrow C$$

를 well-defined하게 정의한다. 거꾸로 임의의 $\varphi\in\Hom_C(\mathfrak{a}/\mathfrak{a}^2,C)$은 $g_j\in B$를 $\varphi(\overline{f_j})=\overline{g_j}$이도록 택하여 flat한 first-order deformation을 준다. 즉 flat한 first-order deformation의 집합은 $\Hom_C(\mathfrak{a}/\mathfrak{a}^2,C)$와 자연스럽게 대응한다.

남은 일은 이 중 어떤 것들이 isomorphic인지, 곧 trivial한 변형을 걸러내는 것이다. 변형 $C'=C[\epsilon]$ (즉 모든 $g_j=0$)에 isomorphic인 변형을 *trivial*하다 부른다. 좌표변환 $\x_i\mapsto\x_i+\epsilon\theta(\x_i)$ (각 $\theta(\x_i)\in C$를 임의로 정하고 derivation으로 확장하여 얻는 $\theta\in\Der_\mathbb{K}(B,C)$)에 의한 $B[\epsilon]$의 automorphism은 $f_j$를 $f_j+\epsilon\sum_i\theta(\x_i)(\partial f_j/\partial\x_i)=f_j+\epsilon\theta(f_j)$로 옮기므로, trivial한 변형들은 정확히 $\varphi$가 derivation에서 오는 경우, 곧 합성

$$\Der_\mathbb{K}(B,C)=\Hom_C(\Omega_{B/\mathbb{K}}\otimes_BC,C)\overset{\overline{d}^\ast}{\rightarrow}\Hom_C(\mathfrak{a}/\mathfrak{a}^2,C)$$

의 image에 속하는 경우이다. 여기서 $\overline{d}^\ast$는 conormal morphism $\overline{d}:\mathfrak{a}/\mathfrak{a}^2\rightarrow\Omega_{B/\mathbb{K}}\otimes_BC$의 dual이며, [§매끄러운 사상과 에탈 사상, ⁋정리 15](/ko/math/scheme_theory/smooth_and_etale_morphisms#thm15)의 증명에서 lift의 실패 $\delta$를 상쇄하는 데 쓰인 것과 같은 morphism이다. 그곳에서는 smoothness가 이 image를 전부로 만들어 모든 $\delta$를 없앴고, 여기서는 없앨 수 없는 부분이 변형으로 남는다.

## Naive 여접 복합체와 $T^i$

위의 두 module $\mathfrak{a}/\mathfrak{a}^2$와 $\Omega_{B/\mathbb{K}}\otimes_BC$, 그리고 그 사이의 $\overline{d}$는 정확히 naive 여접 복합체를 이룬다. [\[가환대수학\] §미분, ⁋정의 10](/ko/math/commutative_algebra/differentials#def10)에서 presentation $p:B\rightarrow C$에 대하여

$$\operatorname{NL}_{C/\mathbb{K}}=\Bigl[\mathfrak{a}/\mathfrak{a}^2\overset{\overline{d}}{\rightarrow}\Omega_{B/\mathbb{K}}\otimes_BC\Bigr]$$

를 정의하였고 ($\mathfrak{a}/\mathfrak{a}^2$는 degree $1$, $\Omega_{B/\mathbb{K}}\otimes_BC$는 degree $0$), 그 homology가

$$H_0(\operatorname{NL}_{C/\mathbb{K}})\cong\Omega_{C/\mathbb{K}},\qquad H_1(\operatorname{NL}_{C/\mathbb{K}})=\ker\overline{d}$$

이며 presentation의 선택에 무관함을 보았다 ([\[가환대수학\] §미분, ⁋명제 11](/ko/math/commutative_algebra/differentials#prop11), [\[가환대수학\] §미분, ⁋정리 14](/ko/math/commutative_algebra/differentials#thm14)). $\operatorname{NL}_{C/\mathbb{K}}$의 언어로 옮기면 [§매끄러운 사상과 에탈 사상, ⁋명제 8](/ko/math/scheme_theory/smooth_and_etale_morphisms#prop8)의 splitting은 $\operatorname{NL}_{C/\mathbb{K}}$가 projective module $\Omega_{C/\mathbb{K}}$ 하나에 quasi-isomorphic하다는 말이 된다. 앞 절의 분석은 first-order deformation의 모듈라이가 이를 $C$로 dual한 것의 cohomology로 읽힌다는 것을 시사한다. 이를 정의로 굳힌다.

::: 정의 3
$C$-module $M$에 대하여, $\operatorname{NL}_{C/\mathbb{K}}$를 $M$으로 dual한 cochain complex

$$\Hom_C(\operatorname{NL}_{C/\mathbb{K}},M):\quad \Hom_C(\Omega_{B/\mathbb{K}}\otimes_BC,M)\overset{\overline{d}^\ast}{\rightarrow}\Hom_C(\mathfrak{a}/\mathfrak{a}^2,M)$$

(왼쪽이 cohomological degree $0$, 오른쪽이 degree $1$)의 cohomology를

$$T^0(C/\mathbb{K},M)=\ker\overline{d}^\ast,\qquad T^1(C/\mathbb{K},M)=\coker\overline{d}^\ast$$

로 정의한다. $T^2$를 정의하려면 relation들을 표시하는 free module을 그대로 남겨 두고 syzygy를 한 항 더 붙여야 한다. $F=B^m$의 basis를 $e_1,\ldots,e_m$이라 하고 $F\rightarrow \mathfrak{a}$, $e_j\mapsto f_j$의 kernel을 $\operatorname{Rel}$이라 하자. 또 $\operatorname{TrivRel}\subseteq\operatorname{Rel}$을 $f_ie_j-f_je_i$ 꼴의 trivial relation들이 생성하는 submodule이라 두면, $\mathfrak{a}$는 $\operatorname{Rel}/\operatorname{TrivRel}$에 자명하게 작용하므로 이는 $C$-module이다. 이때 *Lichtenbaum–Schlessinger complex*는

$$\operatorname{LS}_{C/\mathbb{K}}=\Bigl[\operatorname{Rel}/\operatorname{TrivRel}\overset{d_2}{\rightarrow}F\otimes_BC\overset{d_1}{\rightarrow}\Omega_{B/\mathbb{K}}\otimes_BC\Bigr]$$

로 주어진다. 여기서 세 항의 homological degree는 차례로 $2,1,0$이고,

$$d_2\bigl(\overline{(a_1,\ldots,a_m)}\bigr)=\sum_j\overline{a_j}e_j,\qquad d_1(e_j)=\dd{f_j}\otimes1$$

이다. $i=0,1,2$에 대하여

$$T^i(C/\mathbb{K},M)=H^i\bigl(\Hom_C(\operatorname{LS}_{C/\mathbb{K}},M)\bigr)$$

로 정의하며, 이들을 $C$의 *Lichtenbaum–Schlessinger functor<sub>리히텐바움-슐레진저 함자</sub>*라 부른다.
:::

$T^0$는 곧바로 $\Der_\mathbb{K}(C,M)$이다. 실제로 degree $0$ cocycle은 $\mathfrak{a}$를 죽여 $C=B/\mathfrak{a}$ 위로 내려오는 derivation $B\rightarrow M$이며, 이는 $\Der_\mathbb{K}(C,M)=\Hom_C(\Omega_{C/\mathbb{K}},M)$과 일치한다. 한편 quotient

$$\bigl(F\otimes_BC\bigr)/\im d_2\cong \mathfrak{a}/\mathfrak{a}^2$$

에 의하여 degree $1$ cocycle은 $\Hom_C(\mathfrak{a}/\mathfrak{a}^2,M)$의 원소와 같다. 따라서 위 정의의 $T^1$은 앞서 얻은 $\coker\overline{d}^\ast$, 곧 "평탄 변형 modulo trivial"과 정확히 일치한다. $T^2$에서 새로 등장한 $\operatorname{Rel}/\operatorname{TrivRel}$은 방정식들 사이의 syzygy 가운데 tautological한 Koszul 관계를 넘어서는 부분을 기록한다. 이 점은 장애를 다룰 때 분명해진다.

::: 참고 4
$T^0, T^1$은 two-term complex $\operatorname{NL}_{C/\mathbb{K}}$만으로 올바르게 계산되지만, $T^2$는 Lichtenbaum–Schlessinger complex의 degree $2$ 항을 추가로 요구한다. 더 정확히는, 뒤에서 언급할 완전한 여접 복합체 $L_{C/\mathbb{K}}$에 대하여 $T^i(C/\mathbb{K},M)=\Ext^i_C(L_{C/\mathbb{K}},M)$이며, $\operatorname{NL}_{C/\mathbb{K}}$와 $\operatorname{LS}_{C/\mathbb{K}}$는 각각 $L_{C/\mathbb{K}}$의 degree $0,1$ 절단과 degree $0,1,2$ 절단을 나타낸다. $T^2$가 naive complex의 범위를 벗어난다는 이 사실이, 장애를 제대로 다루려면 적어도 한 항을 더 보아야 한다는 첫 신호이다.
:::

## 일차 변형의 분류

이제 앞의 두 절을 하나의 분류 정리로 묶는다.

::: 정리 5
Finitely generated $\mathbb{K}$-algebra $C$에 대하여, isomorphism class로 본 $C$의 first-order deformation들의 집합은 $T^1(C/\mathbb{K},C)$과 자연스럽게 일대일 대응한다. 이 대응 아래에서 trivial deformation은 $0\in T^1$에 대응하며, 임의의 변형 $C'$의 무한소 automorphism군은 $T^0(C/\mathbb{K},C)=\Der_\mathbb{K}(C,C)$과 동형이다.
:::
::: 증명
[명제 2](#prop2) 직후의 논의에서 flat한 first-order deformation들은 $\Hom_C(\mathfrak{a}/\mathfrak{a}^2,C)$과 대응하고, trivial한 것들은 정확히 $\overline{d}^\ast(\Der_\mathbb{K}(B,C))$의 image에 대응함을 보았다. 따라서 isomorphism class의 집합은

$$\Hom_C(\mathfrak{a}/\mathfrak{a}^2,C)\big/\im\overline{d}^\ast=\coker\overline{d}^\ast=T^1(C/\mathbb{K},C)$$

이며, trivial deformation이 $0$에 대응한다. 다만 두 변형 $\varphi,\varphi'$이 같은 $T^1$ 원소를 주는 것이 isomorphic임을 확인해야 하는데, 두 변형의 차이를 주는 $\varphi-\varphi'$이 derivation에서 올 때 그 derivation이 $B[\epsilon]$의 좌표변환을 주어 동형을 구성하므로 성립한다. Automorphism군에 관해서는, 변형 $C'$의 $A$ 위 항등을 유도하는 automorphism $u:C'\rightarrow C'$은 $u(c')-c'\in\epsilon C'\cong C$를 만족하고, $D(c')=u(c')-c'$이 $\epsilon^2=0$에 의하여 derivation $C\rightarrow C$가 되므로, 대응 $u\mapsto D$가 군 동형 $\Aut(C')\cong\Der_\mathbb{K}(C,C)$을 준다.
:::

이 정리는 변형이론의 가장 기본적인 사전이다. $T^1$은 "tangent space"로서 first-order deformation의 방향을 분류하고, $T^0=\Der$는 그 변형을 보는 시점의 무한소 대칭, 곧 automorphism을 분류한다. 더 일반적인 base 위의 변형에 대해서도 같은 구조가 성립한다.

::: 명제 6
$A$-algebra $C$와 $C$-module $M$에 대하여, $C$를 $M$으로 확대하는 square-zero $A$-algebra 확대 $0\rightarrow M\rightarrow C'\rightarrow C\rightarrow0$의 isomorphism class 집합 $\operatorname{Exal}_A(C,M)$은 $T^1(C/A,M)$과 자연스럽게 일대일 대응한다.
:::
::: 증명
[정리 5](#thm5)의 논증은 base가 일반적인 $A$이고 흔드는 module이 일반적인 $M$일 때로 그대로 옮겨진다. Presentation $C=B/\mathfrak{a}$에서 확대 $C'$은 각 $f\in \mathfrak{a}$를 $M$의 한 원소와 동일시하여 $B\oplus M$을 quotient한 것으로 기술되고, 그 비틂은 $\Hom_C(\mathfrak{a}/\mathfrak{a}^2,M)$의 원소가, 동형의 자유도는 $\Der_A(B,M)$이 흡수하여, isomorphism class가 $\coker=T^1(C/A,M)$로 떨어진다. 완전한 증명과 $T^1(C/A,M)\cong\Ext^1_C(L_{C/A},M)$이라는 여접 복합체 형태의 진술은 ([Ill], [Ser])에 있다.
:::

Flat한 $\mathbb{K}[\epsilon]$-algebra $C'$은 exact sequence $0\rightarrow C\overset{\times\epsilon}{\rightarrow}C'\rightarrow C\rightarrow0$을 주므로 first-order deformation은 $\operatorname{Exal}_\mathbb{K}(C,C)$의 원소로 볼 수 있고, 거꾸로 이러한 확대는 $\mathbb{K}[\epsilon]$-algebra 구조와 flatness를 복원한다. 따라서 [명제 6](#prop6)을 $A=\mathbb{K}$, $M=C$에 적용하면 [정리 5](#thm5)를 다시 얻는다. 곧 $\operatorname{Exal}$은 변형의 일차 데이터를 담는 보편적인 그릇이며, $T^1$이 그것을 측정한다.

## 장애

First-order deformation은 $\epsilon^2=0$ 수준의 변형이다. 그것을 한 단계 더 두꺼운 base 위로 연장하려는 순간, 곧 $\mathbb{K}[t]/(t^2)$ 위의 변형을 $\mathbb{K}[t]/(t^3)$ 위로 들어올리려는 순간 장애가 나타난다. 이 장애가 $T^2$에 산다는 것이 변형이론의 둘째 기둥이다.

::: 정리 7
$\xi\in T^1(C/\mathbb{K},C)$를 first-order deformation이라 하자. 그럼 $\xi$가 $\mathbb{K}[t]/(t^3)$ 위의 평탄 변형으로 연장되는 것을 막는 장애 class

$$\operatorname{ob}(\xi)\in T^2(C/\mathbb{K},C)$$

가 자연스럽게 정의되며, $\xi$가 연장 가능한 것은 $\operatorname{ob}(\xi)=0$인 것과 동치이다. 더 일반적으로, square-zero extension $0\rightarrow M\rightarrow A'\rightarrow A\rightarrow0$과 $A$ 위의 변형 $C_A$에 대하여, $C_A$를 $A'$ 위로 연장하는 것에 대한 장애는 $T^2(C_A/A,C_A\otimes_AM)$의 한 원소이고, 연장이 존재할 때 그 isomorphism class들은 $T^1(C_A/A,C_A\otimes_AM)$ 위의 torsor를 이룬다.
:::
::: 증명
$\xi$를 [명제 2](#prop2)와 같이 $F_j=f_j+tg_j$로 실현하자. Flatness에 의하여 relation $a=(a_1,\ldots,a_m)\in\operatorname{Rel}$마다 $\sum_ja_jg_j=\sum_jc_jf_j$이도록 하는 $c_j\in B$를 고를 수 있다. 이 선택으로

$$\eta(a)=\overline{\sum_jc_jg_j}\in C$$

를 정의하자. $c_j$의 다른 선택과의 차이는 다시 $\operatorname{Rel}$의 원소이고, $g_j$가 [명제 2](#prop2)의 flatness 조건을 만족하므로 그 차이는 $C$에서 $0$이 된다. 또 trivial relation 위에서는 $\eta$가 소멸하므로 이는 $C$-linear map

$$\eta:\operatorname{Rel}/\operatorname{TrivRel}\rightarrow C$$

을 준다. 그 class를 $\operatorname{ob}(\xi)=[\eta]\in T^2(C/\mathbb{K},C)$라 하자.

$\mathbb{K}[t]/(t^3)$ 위의 연장을 $F_j^{(2)}=f_j+tg_j+t^2h_j$ 꼴로 찾자. Relation $a$의 일차 lift를 $R_j=a_j-tc_j$로 두고 $t^3=0$을 이용해 전개하면

$$\sum_jR_jF_j^{(2)}=t^2\left(\sum_ja_jh_j-\sum_jc_jg_j\right)$$

을 얻는다. 여기에 $R_j$를 $t^2s_j$만큼 보정하면 괄호 안에는 $\sum_js_jf_j$를 더할 수 있다. 따라서 relation을 이차까지 lift할 수 있는 조건은

$$\sum_jc_jg_j\equiv\sum_ja_jh_j\pmod{\mathfrak{a}}$$

이다. 오른쪽은 $h=(\overline{h_1},\ldots,\overline{h_m})\in\Hom_C(F\otimes_BC,C)$가 $d_2$를 따라 만드는 coboundary의 $a$에서의 값이다. 모든 relation에 대하여 이 합동식을 만족시키는 $h_j$가 존재하는 것은 $[\eta]=0$인 것과 동치이고, 바로 이때 이차 연장이 존재한다.

$g_j$의 representative와 presentation을 바꾸어도 Lichtenbaum–Schlessinger complex 사이의 canonical homotopy equivalence 아래에서 같은 class를 얻으므로 $\operatorname{ob}(\xi)$는 $\xi$에만 의존한다. 이 선택 무관성과 일반적인 square-zero extension에 대한 진술은 Lichtenbaum–Schlessinger complex가 완전한 여접 복합체의 degree $0,1,2$ 절단과 일치한다는 정리 및 여접 복합체의 deformation theorem에서 따라온다 ([Ill], [Har], [Ser], [Stacks]). 연장이 존재할 때 두 연장의 차이에 [정리 5](#thm5)의 논증을 적용하면 그 isomorphism class들이 $T^1$ 위의 torsor를 이룬다.
:::

장애의 정체는 이렇게 명료하다. First-order deformation은 syzygy를 일차까지 들어올린 뒤 남는 이차 잔여항 $-t^2\sum c_jg_j$를 만들고, 이 잔여항을 $h_j$의 선택으로 흡수할 수 있는지가 연장 가능성이며, 흡수의 실패를 $T^2$가 잰다. 여기서 잔여항이 syzygy의 데이터로 표현되고, 그것이 trivial relation을 넘어서는 부분에서만 의미를 가지므로 $\operatorname{Rel}/\operatorname{TrivRel}$이 등장한 것이다. 이 장애를 반복적으로 소거하며 더 높은 차수로 변형을 쌓아 올리면, 그 limit으로 complete local ring 위의 formal deformation을 얻는다 ([Ser]).

## Smooth한 경우와 local complete intersection

장애와 first-order deformation이 가장 단순해지는 경우가 smooth한 경우이다.

::: 명제 8
$C$가 $\mathbb{K}$ 위에서 smooth하면 $H_1(\operatorname{NL}_{C/\mathbb{K}})=0$이고 $\Omega_{C/\mathbb{K}}$가 finitely generated projective $C$-module이며, 따라서

$$T^1(C/\mathbb{K},M)=T^2(C/\mathbb{K},M)=0\qquad(\text{모든 }C\text{-module }M)$$

이다. 곧 smooth한 $C$의 변형은 어떤 square-zero extension 위로도 동형을 무시하면 유일하게 (장애 없이) 존재하며, 그 무한소 automorphism은 vector field $\Der_\mathbb{K}(C,C)$가 통제한다.
:::
::: 증명
$C$가 smooth하면 [§매끄러운 사상과 에탈 사상, ⁋명제 8](/ko/math/scheme_theory/smooth_and_etale_morphisms#prop8)에 의하여 conormal exact sequence

$$0\rightarrow \mathfrak{a}/\mathfrak{a}^2\overset{\overline{d}}{\rightarrow}\Omega_{B/\mathbb{K}}\otimes_BC\rightarrow\Omega_{C/\mathbb{K}}\rightarrow0$$

이 왼쪽에서도 split되는 short exact sequence가 되어 $\overline{d}$가 injective이고 그 cokernel $\Omega_{C/\mathbb{K}}$이 projective이다. 따라서 $H_1(\operatorname{NL}_{C/\mathbb{K}})=\ker\overline{d}=0$이고 $\operatorname{NL}_{C/\mathbb{K}}$은 projective module $\Omega_{C/\mathbb{K}}$ 하나에 quasi-isomorphic하다. 그럼 $\Hom_C(\operatorname{NL}_{C/\mathbb{K}},M)$이 $\Hom_C(\Omega_{C/\mathbb{K}},M)$ 한 항에 집중되어 $T^1=0$이다. $T^2=0$은 [참고 4](#rmk4)의 $T^i(C/\mathbb{K},M)=\Ext^i_C(L_{C/\mathbb{K}},M)$과, smooth한 $C$에 대하여 $L_{C/\mathbb{K}}$가 이 projective module $\Omega_{C/\mathbb{K}}$ 하나에 quasi-isomorphic하다는 사실로부터 따른다. 무한소 automorphism에 관한 주장은 [정리 5](#thm5)의 일반 형태이다.
:::

이 명제는 [§매끄러운 사상과 에탈 사상, ⁋정리 15](/ko/math/scheme_theory/smooth_and_etale_morphisms#thm15)의 smooth한 쪽을 $T^i$의 언어로 옮긴 것이다. 그곳에서 lifting이 존재한다는 것은 $\delta$를 derivation으로 상쇄할 수 있다는 것, 곧 $\delta$가 정하는 class가 $T^1(C/A,\mathfrak{b})$에서 사라진다는 것이었고, 두 lifting의 차이를 통제한 것은 $T^0(C/A,\mathfrak{b})=\Der_A(C,\mathfrak{b})$였다. 여기에 $T^2=0$이 더해져, 그렇게 얻은 변형이 다시 더 두꺼운 base 위로 연장된다는 것까지 얻는다.

조금 더 약한 가정인 *local complete intersection*에서도 장애는 사라진다. $C=B/\mathfrak{a}$에서 $\mathfrak{a}$가 국소적으로 regular sequence로 생성되면 완전한 여접 복합체 $L_{C/\mathbb{K}}$가 $[0,1]$ 두 degree에 projective module로 집중되어, 그 dual의 둘째 cohomology가 자동으로 $0$이 되기 때문이다. 곧 $T^2(C/\mathbb{K},M)=0$이고 lci singular point는 항상 *unobstructed<sub>장애 없음</sub>*이다. 다만 lci라고 해서 $H_1(\operatorname{NL}_{C/\mathbb{K}})$이 소멸하는 것은 아니며, 반대로 아래 [예시 9](#ex9)처럼 singular한 lci가 $H_1(\operatorname{NL}_{C/\mathbb{K}})=0$을 만족하기도 한다. 곧 $H_1(\operatorname{NL})$의 소멸만으로는 lci 여부가 판정되지 않으며, smoothness는 $H_1(\operatorname{NL}_{C/\mathbb{K}})=0$과 $\Omega_{C/\mathbb{K}}$가 locally free라는 것이 함께 성립하는 것으로 특징지어진다.

## 예시: 매끄러운 변형부터 장애까지

이제 구체적인 singular point들로 위 이론을 검증한다.

::: 예시 9 (node)
$C=\mathbb{K}[\x,\y]/(\x\y)$를 생각하자. 이는 평면 위 두 직선이 한 점에서 만나는 _node_, 곧 $A_1$ singular point의 coordinate ring이다. Hypersurface이므로 $\mathfrak{a}=(\x\y)$이 nonzerodivisor로 생성되어 lci이고, [\[가환대수학\] §미분, ⁋예시 15](/ko/math/commutative_algebra/differentials#ex15)의 계산에서

$$\operatorname{NL}_{C/\mathbb{K}}=\Bigl[C\overline{f}\overset{\overline{d}}{\rightarrow}C \dd{\x}\oplus C \dd{\y}\Bigr],\qquad\overline{d}(\overline{f})=\y \dd{\x}+\x \dd{\y}$$

이다 ($f=\x\y$, $\partial f/\partial\x=\y$, $\partial f/\partial\y=\x$). 이 $\overline{d}$가 단사이면서도 그 image가 원점에서 direct summand를 이루지 못한다는 것, 곧 $H_1(\operatorname{NL}_{C/\mathbb{K}})=0$이면서도 $C$가 원점에서 smooth하지 않다는 것은 [§매끄러운 사상과 에탈 사상, ⁋명제 8](/ko/math/scheme_theory/smooth_and_etale_morphisms#prop8) 뒤의 논의에서 이미 확인하였다. 그곳에서 확인한 실패를 여기서는 dual 쪽에서 재어 그 크기를 얻는다. 이를 dual하면 $\overline{d}^\ast:C^2\rightarrow C$, $(c_1,c_2)\mapsto c_1\y+c_2\x$이므로

$$T^1(C/\mathbb{K},C)=\coker\overline{d}^\ast=C/(\x,\y)=\mathbb{K}[\x,\y]/(\x\y,\x,\y)\cong \mathbb{K}$$

이다. 이 $1$차원 $T^1$의 generator는 $f=\x\y$를 $\x\y-\epsilon$로 흔드는 first-order deformation에 대응하며, 이것이 _Tjurina algebra_ $\mathbb{K}[\x,\y]/(\x\y,\partial_\x f,\partial_\y f)$의 정체이다. lci이므로 $T^2=0$이고 ([명제 8](#prop8) 뒤의 논의), 이 first-order deformation은 장애 없이

$$\x\y=t$$

라는 $\mathbb{K}[t]$ 위의 flat family로 연장된다. $t\neq0$인 fiber는 smooth affine hyperbola이므로, node의 두 branch는 이 family를 따라 *smoothing*된다. 변형이론이 "singular point를 매끄럽게 펼 수 있는가"라는 질문에 $\dim T^1=1$, $T^2=0$이라는 답으로 응답한 것이다.
:::

::: 예시 10 (세 좌표축)
$C=\mathbb{K}[\x,\y,\z]/\mathfrak{a}$, $\mathfrak{a}=(\x\y,\y\z,\z\x)$를 생각하자. 이는 $\mathbb{A}^3$의 세 좌표축의 합집합으로, 차원 $1$, codimension $2$이지만 ideal이 세 원소로 최소생성되므로 complete intersection이 아니며, 따라서 lci가 아니다. 이 singular point에서 $H_1(\operatorname{NL}_{C/\mathbb{K}})$이 $0$이 아님을 직접 확인한다.

$f_1=\x\y$, $f_2=\y\z$, $f_3=\z\x$라 하면, $\overline{d}:\mathfrak{a}/\mathfrak{a}^2\rightarrow C^3$는

$$\overline{d}(\overline{f_1})=(\y,\x,0),\quad\overline{d}(\overline{f_2})=(0,\z,\y),\quad\overline{d}(\overline{f_3})=(\z,0,\x)$$

으로 주어진다 ($C^3=C \dd{\x}\oplus C \dd{\y}\oplus C \dd{\z}$). 이제 원소 $\x\cdot\overline{f_2}\in \mathfrak{a}/\mathfrak{a}^2$을 보자. $C$ 위에서 $\x\z=\x\y=0$이므로

$$\overline{d}(\x\cdot\overline{f_2})=\x\cdot(0,\z,\y)=(0,\x\z,\x\y)=(0,0,0)$$

이어서 $\x\cdot\overline{f_2}\in\ker\overline{d}=H_1(\operatorname{NL}_{C/\mathbb{K}})$이다. 한편 $\x f_2=\x\y\z$는 degree $3$이고 $\mathfrak{a}^2$의 원소는 모두 degree $4$ 이상이므로 $\x\y\z\notin \mathfrak{a}^2$, 곧 $\x\cdot\overline{f_2}=\overline{\x\y\z}\neq0$이다. 따라서

$$H_1(\operatorname{NL}_{C/\mathbb{K}})\neq0,\qquad \overline{\x\y\z}\in H_1(\operatorname{NL}_{C/\mathbb{K}})$$

이다. 이 nonzero class는 conormal morphism $\overline{d}$의 왼쪽 끝 비단사성, 곧 conormal exact sequence를 왼쪽으로 연장했을 때 비로소 보이는 정보이며, $\Omega_{C/\mathbb{K}}$만으로는 결코 검출되지 않는다. ($\overline{\x\y\z}$는 세 generator 어느 쪽으로 보아도 같은 원소로서, $\z\cdot\overline{f_1}=\x\cdot\overline{f_2}=\y\cdot\overline{f_3}$이 모두 kernel에 속한다.) 이것이 naive 여접 복합체의 $H_1$이 smoothness의 실패 가운데 conormal morphism의 비단사성을 포착하는 가장 깨끗한 사례이다.
:::

::: 예시 11 (장애가 있는 변형)
장애가 실제로 $0$이 아닌 고전적 예는 rational normal quartic curve $C_4\subseteq\mathbb{P}^4$ 위의 affine cone

$$C=\mathbb{K}[\z_0,\z_1,\z_2,\z_3,\z_4]/\mathfrak{a},\qquad X=\Spec C,\qquad M=\begin{pmatrix}\z_0&\z_1&\z_2&\z_3\\\z_1&\z_2&\z_3&\z_4\end{pmatrix}$$

이다. 여기서 $\mathfrak{a}=I_2(M)$은 $M$의 $2\times2$ minor들로 생성되는 ideal이다. 이렇게 얻는 cone은 codimension $3$이고 그 vertex가 isolated singular point이다. Pinkham이 계산한 이 singular point의 semiuniversal deformation의 base는 한 점에서 만나는 두 component, 곧 차원 $3$인 성분과 차원 $1$인 성분으로 이루어져, base가 그 교점에서 singular하다. 이는 $T^1$의 어떤 접방향(한 component의 접방향에서 벗어난 방향)이 [정리 7](#thm7)의 의미에서 *obstructed*임을, 곧 그 first-order deformation을 이차로 연장할 때 $\operatorname{ob}(\xi)\neq0\in T^2(C/\mathbb{K},C)$임을 뜻한다.

Codimension $3$ 이상에서는 이러한 장애가 나타날 수 있는 반면, $\mathbb{P}^3$ 위 rational normal cubic의 cone과 같은 codimension $2$ Cohen–Macaulay singular point는 항상 unobstructed하여 base가 매끄럽다. 따라서 [예시 10](#ex10)처럼 lci가 아니어도 장애가 없을 수 있으며, "non-lci"와 "obstructed"는 서로 다른 현상이다. 장애의 유무는 $T^2$와 그 위에서 정의되는 이차 morphism $\operatorname{ob}$이 결정하는 것이지, $\Omega$나 $H_1(\operatorname{NL})$만으로 읽히지 않는다. 이 예시의 명시적 계산은 ([Ser], [Har])를 참조하라.
:::

## 완전한 여접 복합체의 필요성

지금까지 naive 여접 복합체 $\operatorname{NL}_{C/\mathbb{K}}$로 $T^0, T^1$을 완전히 통제하였고, $T^2$는 syzygy의 셋째 항을 붙인 Lichtenbaum–Schlessinger complex로 다루었다. 그러나 이 유한한 절단만으로는 여접 복합체의 전체 구조를 볼 수 없다.

::: 참고 12
첫째, [참고 4](#rmk4)에서 보았듯 $\operatorname{NL}_{C/\mathbb{K}}$ 자체는 $T^2$를 계산하지 못한다. $\mathbb{K}[t]/(t^{n+1})\rightarrow \mathbb{K}[t]/(t^n)$는 매 단계 square-zero extension이므로 고전적인 변형의 연장에서는 매번 $T^2$가 장애를, $T^1$이 연장들의 차이를, $T^0$가 automorphism을 통제한다. Lichtenbaum–Schlessinger complex는 이 세 항을 계산하기에 충분하다. 모든 degree의 André–Quillen cohomology를 하나의 대상으로 정의하는 데에는 full cotangent complex가 쓰인다. 둘째, 변형이론은 morphism의 합성에 대한 *transitivity*를 요구하는데, Kähler differential과 naive 여접 복합체는 [§미분과 여접층, ⁋명제 1](/ko/math/scheme_theory/sheaf_of_differentials#prop1)과 같이 오른쪽 끝에서만 exact한 sequence밖에 주지 못한다. 완전한 이론은 ring morphism의 사슬 $A\rightarrow B\rightarrow C$에 대하여 exact sequence가 아니라 distinguished triangle

$$L_{B/A}\otimes_B^{\mathbb{L}}C\rightarrow L_{C/A}\rightarrow L_{C/B}\rightarrow$$

을 요구하며, 이 삼각형이 long exact sequence로 풀려 모든 $T^i$를 일관되게 연결한다. 셋째, base change의 올바른 식에는 derived tensor $\otimes^{\mathbb{L}}$가 등장하므로, $L_{C/A}$는 모든 degree의 정보를 담는 complex로 주어져야 한다.

이 세 요구를 동시에 만족하는 대상이 Quillen과 André가 simplicial resolution으로 구성한 _cotangent complex_ $L_{C/A}$이며, $\operatorname{NL}_{C/A}$는 그 degree $0,1$ 절단이다. 그 위에서 $T^i(C/A,M)=\Ext^i_C(L_{C/A},M)$이 모든 $i$에 대하여 정의되고, 변형($i=1$)과 장애($i=2$)는 이 통일된 구조의 두 단면일 뿐이다. 이 simplicial 구성과 그 변형이론적 귀결이 derived algebraic geometry로 이어지는 출발점이다.
:::

---

**참고문헌**

**[Ill]** L. Illusie, _Complexe cotangent et déformations I, II_, Lecture Notes in Mathematics 239, 283, Springer, 1971–1972.  
**[Har]** R. Hartshorne, _Deformation theory_, Graduate Texts in Mathematics 257, Springer, 2010.  
**[Ser]** E. Sernesi, _Deformations of algebraic schemes_, Grundlehren der mathematischen Wissenschaften 334, Springer, 2006.  
**[Stacks]** The Stacks project authors, _The Stacks project_, [stacks.math.columbia.edu](https://stacks.math.columbia.edu).

