---
title: "Nodal curve의 변형"
description: "Node를 국소 모형으로 갖는 곡선에서 앞 글의 국소-대역 exact sequence가 완전히 계산되는 모습을 본다. 국소 변형층이 node마다 1차원인 skyscraper이고 그 generator가 방정식을 흔들어 node를 푸는 방향임을 확인하고, marked point를 실은 경우까지 포함하여 변형과 무한소 automorphism이 normalization 위의 vector field로 계산됨을 보인다. 사영 곡선에서 이것이 짧은 exact sequence로 끊어지고, Riemann-Roch로 두 차원의 차가 3g-3+n임을 유도한다."
excerpt: "Node smoothing, the local deformation sheaf, and the count 3g-3+n"

categories: [Math / Scheme Theory]
permalink: /ko/math/scheme_theory/deformations_of_nodal_curves
sidebar: 
    nav: "scheme_theory-ko"

date: 2026-09-03
weight: 24

published: false

---

[§스킴의 변형, ⁋정리 6](/ko/math/scheme_theory/deformations_of_schemes#thm6)은 변형을 국소 자료와 접합 자료로 갈라 놓았지만, 일반적인 scheme에서 두 항은 계산되지 않은 채 남는다. 곡선에서 singularity가 node뿐이면 사정이 완전히 달라진다. 국소 자료가 node마다 정확히 $1$차원이고 그 generator가 무엇을 하는지가 방정식 하나로 보이며, 접합 자료는 normalization 위의 vector field로 환원되어 Riemann--Roch로 계산되기 때문이다.

그 결과가 이 글의 마지막에 나오는 $3g-3+n$이라는 수이며, 이는 marked point를 $n$개 실은 genus $g$ 곡선의 변형 자유도에서 무한소 automorphism의 자유도를 뺀 값이다.

앞 글과 마찬가지로 $k$는 algebraically closed field이고 모든 scheme은 $k$ 위에서 separated이며 finite type이다.

## Prestable curve와 normalization

::: 정의 1
$k$ 위의 연결된 projective curve $C$가 *nodal curve<sub>노드 곡선</sub>*라는 것은, $C$의 각 singular point $p$가 어떤 affine 열린 이웃 $U$를 가져 $U$가 $Z(\x\y)\subseteq\mathbb{A}^2_k$의 원점을 포함하는 열린 subscheme과 isomorphic한 것이다. 이러한 점 $p$를 $C$의 *node<sub>노드</sub>*라 부른다.

$n$개의 *marked point<sub>표시된 점</sub>*를 갖는 genus $g$의 *prestable curve<sub>준안정 곡선</sub>*란 nodal curve $C$와 서로 다른 smooth point들 $p_1,\ldots, p_n\in C$의 짝으로서 $g=h^1(C, \mathcal{O}_C)$인 것이다.
:::

Node에서 두 좌표축 $\{\y=0\}$과 $\{\x=0\}$이 만나는 그림이 이 정의의 전부이며, 이 두 축을 떼어 놓는 것이 normalization이다. 곧 $C$의 *normalization<sub>정규화</sub>*란, smooth projective curve $\widetilde{C}$와 유한사상 $\nu:\widetilde{C}\rightarrow C$로서 node의 바깥에서 isomorphism이고 각 node 위에 정확히 두 점이 놓이는 것을 뜻한다. 국소 모형에서 이는 $Z(\x\y)$를 두 직선 $\mathbb{A}^1_\x$와 $\mathbb{A}^1_\y$의 disjoint union으로 바꾸는 것이고, ring 단계에서는 $k[\x, \y]/(\x\y)$를 $k[\x]\times k[\y]$ 안에 $\x\mapsto(\x, 0)$, $\y\mapsto(0, \y)$로 넣는 것이다. 이 포함사상의 image는 두 성분의 상수항이 일치하는 짝들의 모임이므로, node 하나마다 $\nu_\ast\mathcal{O}_{\widetilde{C}}$가 $\mathcal{O}_C$보다 정확히 $1$차원 크다. 곧 exact sequence

$$0 \rightarrow \mathcal{O}_C \rightarrow \nu_\ast\mathcal{O}_{\widetilde{C}} \rightarrow \bigoplus_{p\in \operatorname{Sing}C}k(p) \rightarrow 0$$

를 얻으며, 여기서 $k(p)$는 $p$에 놓인 skyscraper sheaf이다. 이 sequence는 곧바로 genus를 조합적인 자료로 환원해 준다.

::: 명제 2
Node를 $\delta$개, irreducible component를 $\gamma$개 갖는 nodal curve $C$의 normalization이 genus $g_1,\ldots, g_\gamma$의 성분들로 이루어졌다면

$$g=\sum_{j=1}^\gamma g_j+\delta-\gamma+1$$

이다.
:::
::: 증명
$\nu$가 유한사상이라 affine morphism이므로 $q>0$에서 $R^q\nu_\ast=0$이고 ([§스킴의 층 코호몰로지, ⁋정리 3](/ko/math/scheme_theory/sheaf_cohomology_of_schemes#thm3)), Leray spectral sequence가 $H^i(C, \nu_\ast\mathcal{G})=H^i(\widetilde{C}, \mathcal{G})$를 준다. ([\[대수다양체\] §층 코호몰로지, ⁋명제 19](/ko/math/algebraic_varieties/sheaf_cohomology#prop19)) 그럼 위 exact sequence의 Euler characteristic을 취하면 skyscraper의 $\chi$가 $\delta$이므로

$$1-g=\chi(C, \mathcal{O}_C)=\chi(\widetilde{C}, \mathcal{O}_{\widetilde{C}})-\delta=\sum_j(1-g_j)-\delta$$

이고, 이를 정리하면 주장을 얻는다.
:::

## Node에서의 국소 변형

앞 글의 hypersurface 계산이 그대로 답을 준다.

::: 명제 3
Nodal curve $C$에 대하여 $\mathcal{E}xt^1_{\mathcal{O}_C}(\Omega_{C/k}, \mathcal{O}_C)$은 node들에 지지된 skyscraper sheaf이고, 각 node에서의 stalk은 $1$차원이다. 또 $q\geq 2$에서 $\mathcal{E}xt^q_{\mathcal{O}_C}(\Omega_{C/k}, \mathcal{O}_C)=0$이다.
:::
::: 증명
Node의 바깥에서 $C$는 smooth이므로 $\Omega_{C/k}$가 locally free이고, 따라서 그 위에서 $q>0$인 $\mathcal{E}xt^q$은 소멸한다. Node $p$의 이웃에서는 [정의 1](#def1)에 의하여 $C$가 $Z(\x\y)\subseteq\mathbb{A}^2_k$의 열린 subscheme이므로 $f=\x\y$인 hypersurface의 경우이고, [§스킴의 변형, ⁋예시 8](/ko/math/scheme_theory/deformations_of_schemes#ex8)의 계산이

$$\mathcal{E}xt^1(\Omega_{C/k}, \mathcal{O}_C)=k[\x, \y]/(\x\y, \y, \x)=k$$

를 준다. 같은 계산의 resolution이 길이 $1$이므로 $q\geq2$에서 $\mathcal{E}xt^q=0$이다.
:::

이 stalk이 무엇인지는 방정식에서 곧바로 읽힌다.

::: 예시 4
Node의 국소 모형 $C_0=Z(\x\y)\subseteq\mathbb{A}^2_k$를 보자. [§스킴의 변형, ⁋명제 5](/ko/math/scheme_theory/deformations_of_schemes#prop5)에 의하여 $C_0$의 first-order deformation은 $T^1=k[\x, \y]/(\x, \y)=k$가 분류하고, 그 대응은 [§변형이론과 여접 복합체, ⁋명제 4](/ko/math/scheme_theory/deformation_theory#prop4) 직후의 논의에 따라 방정식 $\x\y$를 $\x\y+\epsilon g$로 흔드는 것이다. 여기서 $g$는 $T^1$에서의 class만이 문제이므로 $g$를 상수 $1$로 택하면 되고, 그럼 변형은

$$\mathcal{C}=\Spec k[\epsilon][\x, \y]/(\x\y-\epsilon)$$

이다. 이를 $\epsilon$ 대신 매개변수 $t$를 쓰는 족

$$\mathcal{C}_t=\Spec k[t][\x, \y]/(\x\y-t)\longrightarrow \Spec k[t]$$

로 확장하여 보면 그림이 분명해진다. Total space는 $k[t][\x,\y]/(\x\y-t)\cong k[\x, \y]$라 smooth이고, $t=0$의 fiber는 두 좌표축이 만나는 원래의 node이며, $t\neq0$의 fiber는 쌍곡선 $\x\y=t$로서 smooth이다. 곧 $T^1$의 generator는 node를 <em-ko>푸는</em-ko> 방향이며, 두 축이 만나 있던 것이 하나의 smooth한 가지로 이어진다. 반대로 $g$를 $\x$나 $\y$로 택하면 $\x\y+\epsilon\x=\x(\y+\epsilon)$처럼 여전히 인수분해되어 node가 남는데, 이는 $\x$와 $\y$가 $T^1$에서 $0$이라는 것과 정합한다.
:::

이 계산이 [명제 3](#prop3)의 $1$차원에 기하적인 이름을 준다. 각 node는 그것을 smooth하게 만드는 단 하나의 방향을 기여하며, 그 방향을 택하지 않으면 node는 그대로 남는다.

## Marked point와 접층

Marked point를 실으면 그것을 고정하는 변형만 허용해야 한다. 이는 $\Omega_{C/k}$를 marked point에서 twist하는 것으로 실현된다.

::: 정의 5
$n$개의 marked point를 갖는 prestable curve $(C, p_1,\ldots, p_n)$에 대하여, $\Sigma=p_1+\cdots+p_n$이라 두고

$$T^i(C, p_\bullet)=\Ext^i_{\mathcal{O}_C}(\Omega_{C/k}(\Sigma), \mathcal{O}_C)$$

로 적는다. 여기서 $\Omega_{C/k}(\Sigma)=\Omega_{C/k}\otimes_{\mathcal{O}_C}\mathcal{O}_C(\Sigma)$이다.
:::

$T^0$이 marked point를 고정하는 무한소 automorphism이고 $T^1$이 그러한 변형이라는 것은 아래 [명제 6](#prop6)에서 두 항이 무엇인지 계산하면 드러난다. 우선 twist가 국소 자료를 바꾸지 않음을 확인해 둔다. $\mathcal{O}_C(\Sigma)$는 line bundle이므로 $\sHom$과 $\mathcal{E}xt$에서 밖으로 빠져나와

$$\sHom(\Omega_{C/k}(\Sigma), \mathcal{O}_C)=\mathcal{T}_{C/k}(-\Sigma),\qquad \mathcal{E}xt^1(\Omega_{C/k}(\Sigma), \mathcal{O}_C)=\mathcal{E}xt^1(\Omega_{C/k}, \mathcal{O}_C)\otimes\mathcal{O}_C(-\Sigma)$$

가 되는데, 오른쪽 층은 node에 지지되고 marked point는 node가 아니므로 그 위에서 $\mathcal{O}_C(-\Sigma)$가 자명하다. 곧 $\mathcal{E}xt^1(\Omega_{C/k}(\Sigma), \mathcal{O}_C)\cong\mathcal{E}xt^1(\Omega_{C/k}, \mathcal{O}_C)$이다.

남은 것은 $\mathcal{T}_{C/k}=\sHom(\Omega_{C/k}, \mathcal{O}_C)$의 정체이다.

::: 명제 6
Nodal curve $C$의 normalization $\nu:\widetilde{C}\rightarrow C$에 대하여, node들의 preimage로 이루어진 $\widetilde{C}$의 divisor를 $D$라 하면

$$\mathcal{T}_{C/k}\cong\nu_\ast\bigl(\mathcal{T}_{\widetilde{C}/k}(-D)\bigr)$$

이다. Marked point의 preimage를 $\widetilde{\Sigma}$라 하면 마찬가지로 $\mathcal{T}_{C/k}(-\Sigma)\cong\nu_\ast(\mathcal{T}_{\widetilde{C}/k}(-D-\widetilde{\Sigma}))$이다.
:::
::: 증명
Node의 바깥에서는 $\nu$가 isomorphism이고 $D$가 비어 있으므로 주장이 자명하다. Node $p$의 이웃에서 $B=k[\x, \y]/(\x\y)$라 두고 $\Der_k(B, B)$를 계산하자. Derivation $D$는 $a=D(\x)$와 $b=D(\y)$로 결정되며, 유일한 관계는 $\x\y=0$에서 오는

$$\x b+\y a=0$$

이다. $B$의 원소는 $c_0+c_1(\x)+c_2(\y)$ 꼴로 유일하게 적히고 ($c_1, c_2$는 상수항이 없다) $\x\y=0$이므로, $a=a_0+a_1(\x)+a_2(\y)$에 대하여 $\y a=\y a_0+\y a_2(\y)$이고 $b=b_0+b_1(\x)+b_2(\y)$에 대하여 $\x b=\x b_0+\x b_1(\x)$이다. 위 관계식은 이 둘의 합이 $0$이라는 것인데 한쪽은 $\x$만의, 다른 쪽은 $\y$만의 다항식이므로 각각이 $0$이어야 하고, 곧 $a_0=a_2=0$과 $b_0=b_1=0$을 얻는다. 따라서

$$\Der_k(B, B)=\{(a, b)\mid a\in \x k[\x],\ b\in \y k[\y]\}$$

이다. 오른쪽은 정확히 두 가지 $\mathbb{A}^1$ 위의 vector field로서 각각 node의 preimage에서 소멸하는 것들의 짝, 곧 $\nu_\ast(\mathcal{T}_{\widetilde{C}/k}(-D))$의 절편이다. 두 기술이 국소적으로 일치하고 그 일치가 $\nu$에서 오는 canonical한 것이므로 sheaf의 isomorphism을 준다.

Twist한 형태는 marked point가 smooth point이고 그곳에서 $\nu$가 isomorphism이므로 위 isomorphism을 $\mathcal{O}_C(-\Sigma)$로 tensor하고 projection formula를 쓰면 얻어진다.
:::

Node에서 vector field가 소멸해야 한다는 조건이 [예시 4](#ex4)의 그림과 짝을 이룬다. Node를 유지하는 변형에서는 두 가지가 서로 미끄러질 수 없고, 그 경직성이 vector field의 소멸로 나타난다.

## 짧은 exact sequence

곡선에서는 [§스킴의 변형, ⁋정리 6](/ko/math/scheme_theory/deformations_of_schemes#thm6)의 다섯 항이 짧은 exact sequence로 끊어진다. 오른쪽 끝의 $H^2$이 소멸하기 때문이다.

::: 보조정리 7
$C$가 $k$ 위의 projective curve이고 $\mathcal{F}$가 그 위의 quasi-coherent sheaf이면 $i\geq2$에서 $H^i(C, \mathcal{F})=0$이다.
:::
::: 증명
Closed embedding $C\subseteq\mathbb{P}^N$을 고정하자. Codimension $2$의 linear subspace들이 이루는 Grassmannian을 $G$라 하면, incidence variety $\{(x, \Lambda)\in C\times G\mid x\in\Lambda\}$는 각 $x$ 위의 fiber가 $\dim G-2$차원이라 $\dim G-1$차원이고, 따라서 그 $G$로의 image는 $G$ 전체가 될 수 없다. 곧 $C$와 만나지 않는 codimension $2$의 linear subspace $\Lambda$가 존재한다.

$\Lambda=H_1\cap H_2$로 적고 $U_i=C\setminus H_i$라 하자. $\mathbb{P}^N\setminus H_i\cong\mathbb{A}^N$이고 $U_i$는 그 안의 closed subscheme이므로 $U_i$는 affine이며, 마찬가지로 $\mathbb{P}^N\setminus(H_1\cup H_2)$가 $\mathbb{A}^N$의 principal open이라 affine이고 $U_1\cap U_2$는 그 안의 closed subscheme이라 affine이다. 그리고 $U_1\cup U_2=C\setminus\Lambda=C$이다.

곧 $\{U_1, U_2\}$는 $C$의 affine open cover이고, 두 개의 열린집합으로 이루어졌으므로 그에 대한 Čech complex는 degree $2$ 이상에서 $0$이다. $C$가 separated이고 $\mathcal{F}$가 quasi-coherent이므로 이 complex의 cohomology가 $H^i(C, \mathcal{F})$이며 ([§스킴의 층 코호몰로지, ⁋따름정리 4](/ko/math/scheme_theory/sheaf_cohomology_of_schemes#cor4)), 따라서 $i\geq2$에서 소멸한다.
:::

::: 정리 8
$n$개의 marked point를 갖는 prestable curve $(C, p_\bullet)$에 대하여, $C$의 node 집합을 $\operatorname{Sing}C$라 하면 exact sequence

$$0 \rightarrow H^1\bigl(C, \mathcal{T}_{C/k}(-\Sigma)\bigr) \rightarrow T^1(C, p_\bullet) \rightarrow \bigoplus_{p\in\operatorname{Sing}C}k \rightarrow 0$$

이 성립하며, 또 $T^0(C, p_\bullet)=H^0(C, \mathcal{T}_{C/k}(-\Sigma))$이다.
:::
::: 증명
[§스킴의 변형, ⁋정리 6](/ko/math/scheme_theory/deformations_of_schemes#thm6)을 $\Omega_{C/k}(\Sigma)$에 적용한다. Nodal curve는 국소적으로 $\mathbb{A}^2_k$ 안의 hypersurface이므로 codimension $1$의 local complete intersection이고 ([§완전교차, ⁋정의 1](/ko/math/scheme_theory/complete_intersections#def1)), reduced이며 그 smooth locus가 유한집합의 여집합이라 dense하므로 그 정리의 가정을 만족한다. 그 증명이 준 다섯 항 sequence는

$$0 \rightarrow H^1(C, \mathcal{T}_{C/k}(-\Sigma)) \rightarrow T^1(C, p_\bullet) \rightarrow H^0(C, \mathcal{E}xt^1(\Omega_{C/k}(\Sigma), \mathcal{O}_C)) \rightarrow H^2(C, \mathcal{T}_{C/k}(-\Sigma))$$

인데, [보조정리 7](#lem7)에 의하여 마지막 항이 $0$이다. 가운데 오른쪽 항은 [정의 5](#def5) 직후의 관찰과 [명제 3](#prop3)에 의하여 node마다 $1$차원인 skyscraper의 global section, 곧 $\bigoplus_{p\in\operatorname{Sing}C}k$이다. $T^0$에 대해서는 spectral sequence의 전체 차수 $0$ 부분이 $E_2^{0, 0}=H^0(C, \sHom(\Omega_{C/k}(\Sigma), \mathcal{O}_C))$ 하나뿐이라는 것에서 따라온다.
:::

이 exact sequence가 변형의 두 겹을 정확히 갈라 놓는다. 왼쪽은 node를 그대로 둔 채 성분들과 그 접합만 흔드는 변형이고, 오른쪽은 각 node를 풀지 말지를 독립적으로 고르는 자유도이다. 특히 오른쪽으로의 사상이 전사이므로 어떤 node들을 골라도 그것들만 푸는 변형이 실제로 존재한다.

## 차원 계산

::: 따름정리 9
$n$개의 marked point를 갖는 genus $g$의 prestable curve $(C, p_\bullet)$에 대하여

$$\dim T^1(C, p_\bullet)-\dim T^0(C, p_\bullet)=3g-3+n$$

이 성립한다.
:::
::: 증명
$\mathcal{H}=\mathcal{T}_{C/k}(-\Sigma)$로 적자. [정리 8](#thm8)에 의하여 $\dim T^1=h^1(\mathcal{H})+\delta$와 $\dim T^0=h^0(\mathcal{H})$이므로, 구하는 값은 $\delta-\chi(C, \mathcal{H})$이다. ($\delta$는 node의 개수이다.)

[명제 6](#prop6)과 [명제 2](#prop2)의 증명에서 쓴 $H^i(C, \nu_\ast\mathcal{G})=H^i(\widetilde{C}, \mathcal{G})$에 의하여

$$\chi(C, \mathcal{H})=\chi\bigl(\widetilde{C}, \mathcal{T}_{\widetilde{C}/k}(-D-\widetilde{\Sigma})\bigr)$$

이다. 오른쪽을 성분마다 계산한다. Genus $g_j$의 성분 $\widetilde{C}_j$ 위에서 $\mathcal{T}_{\widetilde{C}_j/k}$는 차수 $2-2g_j$의 line bundle이고, 그 위에 놓인 $D+\widetilde{\Sigma}$의 점 개수를 $s_j$라 하면 twist한 line bundle의 차수는 $2-2g_j-s_j$이다. Smooth projective curve 위의 line bundle $L$에 대하여 $\chi(L)=\deg L+1-g_j$이므로 ([\[대수다양체\] §Hirzebruch-Riemann-Roch, ⁋정리 2](/ko/math/algebraic_varieties/hirzebruch_riemann_roch#thm2)를 곡선과 line bundle에 적용한 것)

$$\chi\bigl(\widetilde{C}_j, \mathcal{T}_{\widetilde{C}_j/k}(-D-\widetilde{\Sigma})\bigr)=(2-2g_j-s_j)+1-g_j=3-3g_j-s_j$$

이다. 각 node가 preimage를 두 개 주고 각 marked point가 하나를 주므로 $\sum_js_j=2\delta+n$이고, 따라서 $\gamma$개의 성분에 대하여

$$\chi(C, \mathcal{H})=\sum_{j=1}^\gamma(3-3g_j-s_j)=3\gamma-3\sum_jg_j-2\delta-n$$

이다. 여기에 [명제 2](#prop2)가 주는 $\sum_jg_j=g-\delta+\gamma-1$을 넣으면

$$\chi(C, \mathcal{H})=3\gamma-3(g-\delta+\gamma-1)-2\delta-n=-3g+\delta+3-n$$

이고, 곧 $\delta-\chi(C, \mathcal{H})=3g-3+n$이다.
:::

우변이 $\delta$와 $\gamma$에 의존하지 않는다는 것이 이 계산의 핵심이다. Node를 하나 더 만들면 국소 변형이 하나 늘지만 접합의 자유도가 그만큼 줄어, 두 차원의 차는 곡선의 위상 자료인 $g$와 $n$만으로 결정된다.

::: 예시 10
세 가지 경우에서 두 차원을 직접 계산한다.

먼저 $C=\mathbb{P}^1$이고 $n=0$이면 node가 없어 $\mathcal{H}=\mathcal{T}_{\mathbb{P}^1}=\mathcal{O}(2)$이므로 $T^0=H^0(\mathcal{O}(2))$은 $3$차원이고 $T^1=H^1(\mathcal{O}(2))=0$이다. ([§스킴의 층 코호몰로지, ⁋정리 6](/ko/math/scheme_theory/sheaf_cohomology_of_schemes#thm6)) 차는 $-3=3\cdot0-3+0$이다. $T^0$의 $3$차원은 $\mathbb{P}^1$의 automorphism group $\mathrm{PGL}_2$의 차원이며, $T^1=0$은 $\mathbb{P}^1$이 변형되지 않는다는 사실이다.

다음으로 $C=\mathbb{P}^1$이고 marked point가 $3$개이면 $\mathcal{H}=\mathcal{O}(2-3)=\mathcal{O}(-1)$이라 $T^0=T^1=0$이고 차는 $0=3\cdot0-3+3$이다. 세 점을 $0, 1, \infty$로 보내는 automorphism이 유일하다는 사실과 그 곡선이 변형되지 않는다는 사실이 함께 나타난 것이다.

마지막으로 $C$가 두 개의 $\mathbb{P}^1$을 node 하나로 붙인 곡선이고 $n=0$이라 하자. [명제 2](#prop2)에서 $\delta=1$, $\gamma=2$, $g_j=0$이므로 $g=0$이다. 각 성분 위에서 $\mathcal{T}(-D)=\mathcal{O}(2-1)=\mathcal{O}(1)$이므로 $h^0(\mathcal{H})=2+2=4$이고 $h^1(\mathcal{H})=0$이다. 그럼 [정리 8](#thm8)이 $T^0$은 $4$차원, $T^1$은 $0+1=1$차원을 주어 차가 $-3=3\cdot0-3+0$이다. $T^0$의 $4$는 각 성분에서 node를 고정하는 automorphism의 자유도 $2$를 두 번 센 것이고, $T^1$의 $1$은 [예시 4](#ex4)의 방향, 곧 두 직선을 하나의 smooth conic으로 잇는 변형이다.
:::

마지막 예시에서 $T^0$이 $T^1$보다 크다는 것은 이 곡선이 automorphism을 너무 많이 가져 그 자체로는 좋은 moduli를 이루지 못한다는 뜻이다. Marked point를 실어 automorphism을 죽이면 $T^0$이 $0$이 되고 $T^1$의 차원이 곧 $3g-3+n$이 되는데, 그것이 안정성 조건의 대수적인 내용이다.

여기까지는 곡선 자체의 변형이다. 곡선에 얹힌 사상까지 함께 흔들면 어떤 자료가 더해지는지가 다음 글의 주제이다.

---

**참고문헌**

**[ACG]** E. Arbarello, M. Cornalba, P. A. Griffiths, *Geometry of algebraic curves II*, Grundlehren der mathematischen Wissenschaften 268, Springer, 2011.  
**[DM]** P. Deligne, D. Mumford, *The irreducibility of the space of curves of given genus*, Publ. Math. Inst. Hautes Études Sci. **36** (1969), 75--109.  
**[Har]** R. Hartshorne, *Deformation theory*, Graduate Texts in Mathematics 257, Springer, 2010.  
**[Ser]** E. Sernesi, *Deformations of algebraic schemes*, Grundlehren der mathematischen Wissenschaften 334, Springer, 2006.
