---
title: "마디 곡선의 변형"
description: "Node를 국소 모형으로 갖는 곡선에서 변형이론의 국소-대역 exact sequence가 완전히 계산되는 모습을 본다. 국소 변형층이 node마다 1차원인 skyscraper이고 그 generator가 방정식을 흔들어 node를 푸는 방향임을 확인하고, marked point를 실은 경우까지 포함하여 변형과 무한소 automorphism이 normalization 위의 vector field로 계산됨을 보인다. 사영 곡선에서 이것이 짧은 exact sequence로 끊어지고, Riemann-Roch로 두 차원의 차가 3g-3+n임을 유도한다."
excerpt: "Node smoothing, the local deformation sheaf, and the count 3g-3+n"

categories: [Math / Gromov-Witten Theory]
permalink: /ko/math/gromov-witten_theory/deformations_of_nodal_curves
sidebar: 
    nav: "gromov-witten_theory-ko"

date: 2026-09-13
weight: 1


---

Gromov--Witten theory에서 우리는 target space $X$로 들어오는 stable map들 $\mu: C\rightarrow X$를 다룬다. 이 때 $\mu$의 정의역 $C$는 nodal curve에, 특별한 점들을 추가로 선택해준 것이다. 이 때문에 이 카테고리는 이들 nodal curve를 다루는 글로 시작한다. 더 구체적으로, 우리는 이 nodal curve가 어떻게 변형되고, 어떤 automorphism을 갖는지 계산하게 된다. 

Nodal curve의 대표적인, 그리고 본질적으로 유일한 예시는 $\x\y=0$이다. 이는 두 좌표축 $\{\x=0\}$과 $\{\y=0\}$의 합집합이며, 이들이 만나는 점, 즉 원점을 우리는 *node<sub>마디</sub>* 혹은 *nodal point<sub>마디점</sub>*이라 부른다. 핵심적인 성질 중 하나는 이들 node가 singular point라는 것이다. ([\[대수다양체\] §접공간과 매끄러움, ⁋예시 7](/ko/math/algebraic_varieties/tangent_spaces_and_smoothness#ex7){: data-lid="qnd3m" }) 이렇게 singular point가 존재하는 공간을 다룰 때 유효한 전략은 이를 central fiber로 갖고, 그 주변의 fiber는 모두 smooth인 deformation을 생각하는 것이다. [\[스킴\] §변형이론과 여접 복합체, ⁋예시 6](/ko/math/scheme_theory/deformation_theory#ex6){: data-lid="nwt79" }에서 살펴보았듯, $\x\y=0$에 매개변수 $\t$를 넣어 $\x\y=\t$로 바꾸면 이러한 deformation을 얻을 수 있었다.

더 일반적으로 우리는 curve $C$의 singular point가 오직 node 뿐일 경우, 즉 모든 singular point가 étale-local하게 $\x\y=0$의 꼴일 경우 이를 *nodal curve<sub>마디 곡선</sub>*라 부른다. 이러한 nodal curve들을 포함하여 이 글에서 등장하는 모든 scheme은 algebraically closed field $\mathbb{K}$ 위에서 separated이고 finite type인 것으로 생각한다. 직관적으로는 $\mathbb{K}=\mathbb{C}$로 두고, 대부분의 scheme은 (fat point가 필요한 경우를 제외하면) 모두 variety인 것으로 생각해도 대체로 무해하다.

## 준안정 곡선과 정규화

우선 다음을 정의한다. 

::: 정의 1
Connected projective nodal curve $C$의 서로 다른 smooth point $p_1,\ldots,p_n$ 각각을 $C$의 *marked point<sub>표시된 점</sub>*라 한다. 이렇게 marked point를 갖춘 짝 $(C,p_1,\ldots,p_n)$을 $n$개의 marked point를 갖는 genus $g=h^1(C,\mathcal{O}_C)$의 *prestable curve<sub>준안정곡선</sub>*라 한다.
:::

즉 prestable curve란 nodal curve 위에, node와 겹치지 않도록 몇 개의 점을 추가로 선택한 것에 불과하다. 

Nodal curve가 주어지면 이 node에서 붙은 두 branch를 떼어내는 방법이 존재한다. 이는 [\[스킴\] §차원, ⁋명제 5](/ko/math/scheme_theory/dimension#prop5){: data-lid="o8zf6" } 직후의 논의에서 정의한 normalization을 nodal curve에 적용한 것으로, 이 구체적인 상황에서 $C$의 *normalization<sub>정규화</sub>*란, smooth projective curve $\widetilde{C}$와 finite morphism $\nu:\widetilde{C}\rightarrow C$로서, node의 바깥에서 isomorphism이고 각 node 위에 정확히 두 점이 놓이는 것을 뜻한다. 

{% diagram Math/Gromov_Witten_Theory/Deformations_of_Nodal_Curves-1.svg width="7.37em" alt="normalization separates the two branches of a node" %}

위의 그림과 같이, node에서의 local model에서 이는 $Z(\x\y)$를 두 직선 $\mathbb{A}^1_\x$와 $\mathbb{A}^1_\y$의 disjoint union으로 바꾸는 것이고, ring 단계에서 이는 inclusion

$$A=\mathbb{K}[\x,\y]/(\x\y)\rightarrow \widetilde{A}=\mathbb{K}[\x]\times\mathbb{K}[\y];\qquad f(\x,\y)\mapsto (f(\x,0), f(0,\y))$$

으로 주어지는 것이다. 이 때, 두 식 $f(\x,0)$과 $f(0,\y)$를 보면 이 식들의 상수항 $c$가 반드시 같아야 하는 것을 알고, 거꾸로 그러한 쌍 $(f(\x),g(\y))$가 주어졌다면 $f+g-c$를 $\mathbb{K}[\x,\y]/(\x\y)$로 본 것이 이 inclusion의 preimage인 것을 알 수 있다. 즉, 이 inclusion의 image는 정확히 두 성분의 상수항이 일치하는 짝들의 모임이다. 따라서 $\widetilde{A}\rightarrow \mathbb{K}$를 $(f,g)\mapsto f(0)-g(0)$으로 정의하면, 다음의 short exact sequence

$$0 \rightarrow A \rightarrow \widetilde{A}\rightarrow \mathbb{K}\rightarrow 0$$

이 존재한다. 이를 sheafify하면, node 바깥에서 $\nu$는 isomorphism이고, $p$에서의 위 계산은 cokernel이 $\kappa(p)=\mathbb{K}$임을 보여주므로

$$0\rightarrow\mathcal{O}_C\rightarrow\nu_\ast\mathcal{O}_{\widetilde{C}}\rightarrow\kappa(p)\rightarrow0$$

를 얻는다. 일반적인 nodal curve에서, normalization은 이 과정을 모든 node에서 동시에 수행하는 것이며, 따라서 이 경우에는 다음의 short exact sequence

$$0\rightarrow\mathcal{O}_C\rightarrow\nu_\ast\mathcal{O}_{\widetilde{C}}\rightarrow\bigoplus_{p\in\Sing C}\kappa(p)\rightarrow0$$

를 얻는다.

이제 $C$가 node를 $d$개, irreducible component를 $c$개 갖고, $\widetilde{C}$의 각 성분의 genus가 $g_1,\ldots,g_c$라고 하자. $\nu$가 affine morphism이므로 [\[스킴\] §스킴의 층 코호몰로지, ⁋따름정리 4](/ko/math/scheme_theory/sheaf_cohomology_of_schemes#cor4){: data-lid="prlmv" }에 의하여 $H^i(C,\nu_\ast\mathcal{G})=H^i(\widetilde{C},\mathcal{G})$이다. 따라서 위 short exact sequence로부터, 다음의 식

$$\rchi(C,\nu_\ast\mathcal{O}_{\widetilde{C}})=\rchi(C,\mathcal{O}_C)+\sum_{p\in\Sing C}\rchi(C,\kappa(p))$$

을 얻으며, 이 때 각 $\kappa(p)$는 global section이 $\mathbb{K}$이고 higher cohomology가 소멸하는 skyscraper sheaf이므로 마지막 합은 $d$이다. 이를 정리하면 다음의 명제를 얻는다.

::: 명제 2
Node를 $d$개, irreducible component를 $c$개 갖는 nodal curve $C$의 normalization이 genus $g_1,\ldots, g_c$의 성분들로 이루어졌다면

$$g=\sum_{j=1}^c g_j+d-c+1$$

이다.
:::

## 준안정곡선의 변형

이제 nodal curve의 deformation theory를 살펴보자. Node $p$에서의 first-order local deformation space를 $T_p^1$로 적자. [\[스킴\] §변형이론과 여접 복합체, ⁋예시 6](/ko/math/scheme_theory/deformation_theory#ex6){: data-lid="y2bip" }에서 affine node $Z(\x\y)$에 대하여 $T_p^1\cong\mathbb{K}$이고, 그 generator를 $\x\y-\epsilon$으로 나타낼 수 있음을 이미 계산하였다. 모든 node가 이 local model을 가지는 반면 smooth point의 local deformation은 trivial하므로 다음을 얻는다.

::: 명제 3
Nodal curve $C$의 각 node $p$에서 first-order local deformation들의 공간 $T_p^1$은 $1$차원이다.
:::

이 한 차원의 기하적인 의미는 family $\x\y=\t$로 나타낼 수 있다.

{% diagram Math/Gromov_Witten_Theory/Deformations_of_Nodal_Curves-2.svg width="51.68em" alt="the local fibers xy=t over the deformation space" %}

한편 prestable curve는 nodal curve $C$의 smooth locus에 marked point $p_1,\ldots,p_n$을 둔 것이다. 따라서 위 그림에 marked point들을 더해주면, 이들은 curve가 deform됨에 따라 함께 움직이면서 각 $p_i$를 지나는 section을 정의한다. 그럼 marked point들이 서로 같아질 수 없으므로 이 section들은 disjoint하게 되며, 따라서 prestable curve의 first-order deformation은 underlying curve의 deformation과 이 marked section들을 함께 택한 자료로 주어진다. 이 때 각 자료 사이의 isomorphism은 $\Spec\mathbb{K}[\epsilon]$ 위의 family들의 isomorphism으로서, central fiber에서 identity이고, 각 marked section을 그에 대응하는 marked section으로 보내는 것이다. 이러한 isomorphism class들이 이루는 $\mathbb{K}$-vector space를 $T^1(C,p_\bullet)$로 적는다. 이는 [\[스킴\] §변형이론과 여접 복합체, ⁋정리 11](/ko/math/scheme_theory/deformation_theory#thm11){: data-lid="fqff9" }의 $T^1$을 marked curve에 적용한 것으로, 같은 방식으로 모든 marked section을 보존하는 infinitesimal automorphism들의 $\mathbb{K}$-vector space를 $T^0(C,p_\bullet)$로 적는다. 

이들 $T^0(C,p_\bullet)$과 $T^1(C,p_\bullet)$은 underlying nodal curve에 새로 추가된 marked point들이 추가로 부과하는 조건으로 정해지므로, 이 두 조건을 별도로 나누어 보는 것이 합리적이다. 우선 $T^1$의 경우, 우리는 이미 위에서 $T_p^1$은 오직 node에서만 생기는 것을 살펴보았으며, 정의에 의해 marked point들은 smooth point에만 찍히므로 여기에 영향을 미치지 않는다. 즉 node에서 계산한 $T_p^1$은 prestable curve에 대해서도 동일하게 유지된다. 

새로 추가한 marked point들이 영향을 미치는 것은 $T^0$으로, 여기서는 infinitesimal automorphism이 marked section을 보존해야 한다. 국소적으로, $C$ 위의 함수 $f$에 automorphism $\Phi$는

$$\Phi(f)=f+\epsilon v(f)$$

의 꼴이어야 하며, 이것이 곱셈을 보존하기 위해서는 $v(fg)=fv(g)+gv(f)$이 성립해야 한다. 즉 $v$는 $\mathcal{O}_C$ 위의 $\mathbb{K}$-derivation이며, 역으로 이러한 derivation은 항상 위와 같은 식으로 automorphism을 정의한다. 이제 prestable curve가 nodal curve와 다른 infinitesimal automorphism을 갖는 부분은 위에서 언급한 것과 같이 marked section 근방이므로 각 marked point $p_i$ 근방에서 이를 살펴보자. $p_i$가 local하게 $\z=0$으로 쓰인다고 가정하자. [\[스킴\] §매끄러운 사상과 에탈 사상, ⁋정리 7](/ko/math/scheme_theory/smooth_and_etale_morphisms#thm7){: data-lid="x011e" }에 의하여 $\Omega_{C/\mathbb{K}}$는 이 근방에서 rank $1$의 locally free sheaf이고 $\dd{\z}$가 local basis가 되고, 따라서 differential의 universal property에 의하여 임의의 derivation은 $\dd{\z}$의 image $v(\z)$에 의해 결정된다. 이에 대응하는 automorphism은

$$\z\mapsto\z+\epsilon v(\z)$$

로 주어지며, 우리는 $\z=0$이 (국소적으로) marked section을 나타내도록 잡았으므로 이것이 보존되기 위해서는 $v(\z)$가 marked point에서 소멸해야 한다. 즉 $v(\z)\in(\z)$이어야 한다. 이제 $\Sigma=p_1+\cdots+p_n$이라 두면 그 ideal sheaf는 $\mathcal{I}_\Sigma=\mathcal{O}_C(-\Sigma)$이므로, 이 조건을 만족하는 derivation들의 sheaf는

$$\sHom(\Omega_{C/\mathbb{K}},\mathcal{I}_\Sigma)=\mathcal{T}_{C/\mathbb{K}}\otimes\mathcal{I}_\Sigma=\mathcal{T}_{C/\mathbb{K}}(-\Sigma)$$

이고, 이것이 marked curve의 infinitesimal automorphism을 계산한다. 

이제 남은 것은 $\mathcal{T}_{C/\mathbb{K}}=\sHom(\Omega_{C/\mathbb{K}}, \mathcal{O}_C)$의 계산이다. 이를 위해 local model $R=\mathbb{K}[\x,\y]/(\x\y)$을 택하고 이 위의 derivation을 살펴보자. 임의의 derivation $v$는 generator에서의 값 $a=v(\x)$와 $b=v(\y)$로 결정되고, [\[스킴\] §변형이론과 여접 복합체, ⁋예시 6](/ko/math/scheme_theory/deformation_theory#ex6){: data-lid="7kwur" }의 계산과 같이 관계식 $\x\y=0$을 보존하려면

$$0=v(\x\y)=\y a+\x b$$

이어야 한다. 여기서 $\y a=-\x b$는 $(\y)$와 $(\x)$에 동시에 속하고, $R$에서는 $(\x)\cap(\y)=0$이므로 $\y a=\x b=0$이다. 또한 $\ann(\y)=(\x)$이고 $\ann(\x)=(\y)$이므로 $a\in\x\mathbb{K}[\x]$이고 $b\in\y\mathbb{K}[\y]$이다. 

기하적으로 이는 $R$의 normalization에서 두 branch가 나누어진 상황을 반영한다. 즉 $R$의 normalization을 $\widetilde{R}=\mathbb{K}[\x]\oplus\mathbb{K}[\y]$이라 쓴다면, 위의 $a$와 $b$는 normalization의 각 branch 위의 derivation이 되며, 각각의 원점에서 소멸하는 함수들이다. 

이제 이를 전체 nodal curve에서 보면, normalization $\nu:\widetilde{C}\rightarrow C$에서 node $p$의 두 preimage를 $p',p''$이라 하면, 이들은 각각 $p'$과 $p''$에서 소멸하는 derivation이며, node 바깥에서는 $\nu$가 isomorphism이므로 이 local identification들은 canonical하게 붙는다. 따라서 모든 node의 두 preimage를 모은 divisor를 $D$라 하면 이 계산은 다음과 같이 요약된다.

::: 명제 4
Nodal curve $C$의 normalization $\nu:\widetilde{C}\rightarrow C$와 node들의 preimage로 이루어진 $\widetilde{C}$의 divisor $D$에 대하여

$$\mathcal{T}_{C/\mathbb{K}}\cong\nu_\ast\bigl(\mathcal{T}_{\widetilde{C}/\mathbb{K}}(-D)\bigr)$$

이 성립한다. Marked point의 preimage를 $\widetilde{\Sigma}$라 하면 마찬가지로 $\mathcal{T}_{C/\mathbb{K}}(-\Sigma)\cong\nu_\ast(\mathcal{T}_{\widetilde{C}/\mathbb{K}}(-D-\widetilde{\Sigma}))$이다.
:::

실제로 두 번째 isomorphism은 marked point에서 얻은 소멸 조건을 첫 번째 isomorphism에 더한 것이다. 따라서 global section을 취하면

$$T^0(C,p_\bullet)\cong H^0\bigl(C,\nu_\ast\mathcal{T}_{\widetilde{C}/\mathbb{K}}(-D-\widetilde{\Sigma})\bigr)=H^0\bigl(\widetilde{C},\mathcal{T}_{\widetilde{C}/\mathbb{K}}(-D-\widetilde{\Sigma})\bigr)$$

이다. 여기서 마지막 등식은 pushforward의 정의에 따라 $H^0(C,\nu_\ast\mathcal{F})=H^0(\widetilde{C},\mathcal{F})$이기 때문이다. 곧 infinitesimal automorphism은 normalization 위에서 node의 모든 preimage와 marked point에서 소멸하는 derivation으로 계산된다.

표준적인 deformation theory 해석에 따라 이 계산은 nodal curve, 혹은 더 일반적으로 prestable curve의 automorphism group의 tangent space를 구한 것으로 해석할 수 있다. ([\[스킴\] §변형이론과 여접 복합체, ⁋정리 5](/ko/math/scheme_theory/deformation_theory#thm5){: data-lid="u7v2l" }) 이 automorphism group을 $G=\Aut(C,p_\bullet)$라 하고 그 항등원을 $e$라 하면, 항등원에서의 tangent space $T_eG$의 원소는 $\mathbb{K}[\epsilon]$-valued point $\Spec\mathbb{K}[\epsilon]\rightarrow G$ 중 closed point가 항등원으로 가는 것들의 모임이다. ([\[스킴\] §다양체에서 스킴으로, ⁋예시 4](/ko/math/scheme_theory/from_varieties_to_schemes#ex4){: data-lid="jhbqv" }) 즉 직관적으로 이는 central fiber로 제한했을 때 항등사상이 되는 automorphism들의 family로 생각할 수 있으며, 이로부터 다음의 identification 

$$T_eG\cong T^0(C,p_\bullet)\cong H^0\bigl(\widetilde{C},\mathcal{T}_{\widetilde{C}/\mathbb{K}}(-D-\widetilde{\Sigma})\bigr)$$

을 얻는다. 위의 계산에서 우리는 임의의 automorphism은 국소적으로 $f\mapsto f+\epsilon v(f)$의 꼴로 쓰이는 것을 알고 있으며, 이때 derivation $v$는 smooth curve $\widetilde{C}$ 위에서 vector field를 의미하므로 이 식은 automorphism을 항등원에서 infinitesimal하게 움직이는 방향이 normalization 위의 vector field로 나타난다는 것으로 해석할 수 있다.

## 차원 계산

Deformation space $T^1(C,p_\bullet)$은 marked prestable curve $(C,p_\bullet)$라는 한 점에서 이웃한 점으로 움직이는 방향을 나타내므로, 이들 prestable curve들을 모아둔 공간에서 보면 tangent space 역할을 한다. 여기서 같은 점을 나타내는 infinitesimal automorphism의 자유도 $T^0(C,p_\bullet)$는 빼줘야 하며, 우리 목표는 이 차이를 계산하는 것이다. 

이를 위해 prestable curve에 대한 cohomology vanishing이 필요한데, 이를 위해 projective embedding $C\subseteq\mathbb{P}^N$을 잡고 $C$와 만나지 않는 codimension $2$의 linear subspace $\Lambda=H_1\cap H_2$를 택하자. 그럼 $U_i=C\setminus H_i$는 affine이고 $U_1\cup U_2=C$이므로, $C$ 위의 임의의 quasi-coherent sheaf $\mathcal{F}$의 sheaf cohomology를 Čech cohomology로 계산하면 degree $2$ 이상에서는 $H^i(C, \mathcal{F})=0$이 성립하는 것을 안다. 이를 사용하면 다음을 보일 수 있다. 

::: 정리 5
$n$개의 marked point를 갖는 prestable curve $(C, p_\bullet)$에 대하여, $C$의 node 집합을 $\Sing C$라 하면 exact sequence

$$0 \rightarrow H^1\bigl(C, \mathcal{T}_{C/\mathbb{K}}(-\Sigma)\bigr) \rightarrow T^1(C, p_\bullet) \rightarrow \bigoplus_{p\in\Sing C}\mathbb{K} \rightarrow 0$$

이 성립하며, 또 $T^0(C, p_\bullet)=H^0(C, \mathcal{T}_{C/\mathbb{K}}(-\Sigma))$이다.
:::
::: 증명
앞에서 계산한 대로 marked point들은 automorphism sheaf에 twist $(-\Sigma)$를 더하지만, node의 local deformation space $T_p^1$은 바꾸지 않는다. 따라서 [\[스킴\] §변형이론과 여접 복합체, ⁋정리 12](/ko/math/scheme_theory/deformation_theory#thm12){: data-lid="940xu" }로부터

$$0\rightarrow H^1\bigl(C,\mathcal{T}_{C/\mathbb{K}}(-\Sigma)\bigr)\rightarrow T^1(C,p_\bullet)\rightarrow\bigoplus_{p\in\Sing C}T_p^1\rightarrow H^2\bigl(C,\mathcal{T}_{C/\mathbb{K}}(-\Sigma)\bigr)$$

를 얻으며, 이 때 위의 vanishing에 의하여 마지막 항이 $0$이다. 또, [명제 3](#prop3){: data-lid="8ouk8" }에 의하여 $T_p^1\cong\mathbb{K}$이므로 이로부터 원하는 short exact sequence를 얻는다. 마지막 주장의 경우 이 long exact sequence의 degree $0$ 부분을 본 것이다.
:::

직관적으로 이 exact sequence는 prestable curve의 deformation을 두 겹으로 갈라놓는다. 왼쪽 항은 모든 node의 local model을 유지하면서 normalization의 성분들과 그 위의 node preimage 및 marked point의 위치를 변형하는 자유도이고, 오른쪽 항은 어떤 node를 smoothing할지를 고르는 자유도이다. 그럼 우리의 핵심적인 주장은 다음과 같다. 

::: 따름정리 6
$n$개의 marked point를 갖는 genus $g$의 prestable curve $(C, p_\bullet)$에 대하여

$$\dim T^1(C, p_\bullet)-\dim T^0(C, p_\bullet)=3g-3+n$$

이 성립한다.
:::
::: 증명
표기의 편의상 $\mathcal{H}=\mathcal{T}_{C/\mathbb{K}}(-\Sigma)$로 적고, $C$의 node의 갯수를 $d$라 하면 [정리 5](#thm5){: data-lid="c3l1e" }에 의하여 

$$\dim T^1=h^1(\mathcal{H})+d,\qquad \dim T^0=h^0(\mathcal{H})$$

이므로 구하고자 하는 값은 $d-\rchi(C, \mathcal{H})$이다. 이제 [명제 4](#prop4){: data-lid="arwum" }와 [\[스킴\] §스킴의 층 코호몰로지, ⁋따름정리 4](/ko/math/scheme_theory/sheaf_cohomology_of_schemes#cor4){: data-lid="tpsgt" }에 의하여

$$\rchi(C, \mathcal{H})=\rchi\bigl(\widetilde{C}, \mathcal{T}_{\widetilde{C}/\mathbb{K}}(-D-\widetilde{\Sigma})\bigr)$$

이다. 

위 등식의 우변을 각 성분마다 계산하자. [\[대수다양체\] §곡선에서의 리만-로흐 정리, ⁋명제 3](/ko/math/algebraic_varieties/riemann_roch_theorem#prop3){: data-lid="khrzv" }을 genus $g_j$의 성분 $\widetilde{C}_j$의 canonical divisor $K_{\widetilde{C}_j}$에 적용하면 $\deg\omega_{\widetilde{C}_j}=2g_j-2$를 얻는다. 따라서 $\mathcal{T}_{\widetilde{C}_j/\mathbb{K}}\cong\omega_{\widetilde{C}_j}^\vee$는 차수 $2-2g_j$의 line bundle이다. 그 위에 놓인 $D+\widetilde{\Sigma}$의 점 개수를 $s_j$라 하면 twisted line bundle의 차수는 $2-2g_j-s_j$이고, 같은 명제에 의하여

$$\rchi\bigl(\widetilde{C}_j, \mathcal{T}_{\widetilde{C}_j/\mathbb{K}}(-D-\widetilde{\Sigma})\bigr)=(2-2g_j-s_j)+1-g_j=3-3g_j-s_j$$

이다. 이제 node가 preimage를 두 개 주고 각 marked point가 하나를 주므로 $\sum_js_j=2d+n$이고, 따라서 $c$개의 성분에 대하여

$$\rchi(C, \mathcal{H})=\sum_{j=1}^c(3-3g_j-s_j)=3c-3\sum_jg_j-2d-n$$

이다. 여기에 [명제 2](#prop2){: data-lid="b8s52" }가 주는 $\sum_jg_j=g-d+c-1$을 넣으면

$$\rchi(C, \mathcal{H})=3c-3(g-d+c-1)-2d-n=-3g+d+3-n$$

이 되어 원하는 결과를 얻는다.
:::

우변이 $d$와 $c$에 의존하지 않는다는 것이 이 계산의 핵심이다. Node를 하나 더 만들면 국소 변형이 하나 늘지만 접합의 자유도가 그만큼 줄어, 두 차원의 차는 곡선의 위상 자료인 $g$와 $n$만으로 결정된다. 이 결과는 다음 글에서 stable map moduli의 차원을 계산할 때 중요한 역할을 한다.

---

**참고문헌**

**[HKK+]** K. Hori, S. Katz, A. Klemm, R. Pandharipande, R. Thomas, C. Vafa, R. Vakil, E. Zaslow, *Mirror Symmetry*, Clay Mathematics Monographs **1**, AMS, 2003.
