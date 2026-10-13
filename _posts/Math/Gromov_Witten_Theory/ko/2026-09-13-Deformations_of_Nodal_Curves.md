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
drift_needed: true


---

Gromov--Witten theory에서 우리는 target space $X$로 들어오는 stable map들 $\mu: C\rightarrow X$를 다룬다. 이 때 $\mu$의 정의역 $C$는 nodal curve에, 특별한 점들을 추가로 선택해준 것이다. 이 때문에 이 카테고리는 이들 nodal curve를 다루는 글로 시작한다. 더 구체적으로, 우리는 이 nodal curve가 어떻게 변형되고, 어떤 automorphism을 갖는지 계산하게 된다. 

Nodal curve의 대표적인, 그리고 본질적으로 유일한 예시는 $\x\y=0$이다. 이는 두 좌표축 $\{\x=0\}$과 $\{\y=0\}$의 합집합이며, 이들이 만나는 점, 즉 원점을 우리는 *node<sub>마디</sub>* 혹은 *nodal point<sub>마디점</sub>*이라 부른다. 핵심적인 성질 중 하나는 이들 node가 singular point라는 것이다. ([\[대수다양체\] §접공간과 매끄러움, ⁋예시 7](/ko/math/algebraic_varieties/tangent_spaces_and_smoothness#ex7){: data-lid="qnd3m" }) 이렇게 singular point가 존재하는 공간을 다룰 때 유효한 전략은 이를 central fiber로 갖고, 그 주변의 fiber는 모두 smooth인 deformation을 생각하는 것이다. [\[스킴\] §변형이론과 여접 복합체, ⁋예시 6](/ko/math/scheme_theory/deformation_theory#ex6){: data-lid="nwt79" }에서 살펴보았듯, $\x\y=0$에 매개변수 $\t$를 넣어 $\x\y=\t$로 바꾸면 이러한 deformation을 얻을 수 있었다.

더 일반적으로 우리는 curve $C$의 singular point가 오직 node 뿐일 경우, 즉 모든 singular point가 étale-local하게 $\x\y=0$의 꼴일 경우 이를 *nodal curve<sub>마디 곡선</sub>*라 부른다. 이러한 nodal curve들을 포함하여 이 글에서 등장하는 모든 scheme은 algebraically closed field $\mathbb{K}$ 위에서 separated이고 finite type인 것으로 생각한다. 직관적으로는 $\mathbb{K}=\mathbb{C}$로 두고, 대부분의 scheme은 (fat point가 필요한 경우를 제외하면) 모두 variety인 것으로 생각해도 대체로 무해하다.

## 준안정 곡선과 정규화

우선 다음을 정의한다. 

::: 정의 1
Connected projective nodal curve $C$의 서로 다른 smooth point $p_1,\ldots,p_n$ 각각을 $C$의 *marked point<sub>표시된 점</sub>*라 한다. 이렇게 marked point를 갖춘 짝 $(C,p_1,\ldots,p_n)$을 $n$개의 marked point를 갖는 genus $g=h^1(C,\mathcal{O}_C)$의 *prestable curve<sub>준안정 곡선</sub>*라 한다.
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
Node를 $d$개, irreducible component를 $c$개 갖는 connected nodal curve $C$의 normalization이 genus $g_1,\ldots, g_c$의 성분들로 이루어졌다면

$$g=\sum_{j=1}^c g_j+d-c+1$$

이다.
:::

Projective nodal curve $C$는 étale-local하게 hypersurface이므로 Cohen-Macaulay이고, 따라서 dualizing sheaf $\omega_C$를 갖는다. ([\[대수다양체\] §세르 쌍대성, §§세르 쌍대성의 일반화](/ko/math/algebraic_varieties/serre_duality#세르-쌍대성의-일반화){: data-lid="jenro" }) 이는 node 바깥에서는 $\Omega_C$와 isomorphic한 것이므로, 우리는 각 node를 포함하는 열린집합 $U\subseteq C$에 대하여 section $\omega_C(U)$를 기술하면 충분하다. 

이를 위해 $C$의 normalization $\nu:\widetilde{C}\rightarrow C$를 생각한 후, node $p$의 normalization에 의한 두 preimage를 $p_1,p_2$라 하자. Node의 étale-local model $A=\mathbb{K}[\x,\y]/(\x\y)$에서 $\omega_C$의 section은 두 branch 위의 rational 1-form의 pair $(\eta_1,\eta_2)$ 가운데 적당한 $a\in\mathbb{K}$와 $f_1\in\mathbb{K}[\x]$, $f_2\in\mathbb{K}[\y]$에 대하여

$$\eta_1=\Bigl(\frac{a}{\x}+f_1(\x)\Bigr)\dd{\x},\qquad\eta_2=\Bigl(-\frac{a}{\y}+f_2(\y)\Bigr)\dd{\y}$$

의 꼴로 주어지는 것들이다.

위의 pair는 모두 $(\dd{\x}/\x,-\dd{\y}/\y)$에 $A$의 원소를 곱한 것으로 유일하게 쓰이므로, $\omega_C$는 node 근방에서 이 pair를 basis로 갖는 line bundle이며, 이를 $\nu$로 당기면 각 branch의 local basis는 $\dd{\x}/\x$, $-\dd{\y}/\y$가 된다. 이들은 node의 preimage에서 simple pole을 허용하는 1-form들의 line bundle의 basis이므로, node들의 preimage를 모은 divisor를 $D$라 하면

$$\nu^\ast\omega_C\cong\omega_{\widetilde{C}}(D)$$

이다. 여기서 $D_j$를 $D$ 가운데 성분 $\widetilde{C}_j$ 위의 점들을 모은 divisor라 하고, 그 점들의 개수를 $m_j$라 하자. 위 식을 $\widetilde{C}_j$로 제한하면 $\omega_C$를 이 성분으로 당긴 line bundle은 $\omega_{\widetilde{C}_j}(D_j)$와 isomorphic하다. Smooth curve $\widetilde{C}_j$의 canonical bundle의 degree는 $2g_j-2$이고, divisor로 twist하면 그 degree가 더해지므로

$$\deg\omega_{\widetilde{C}_j}(D_j)=\deg\omega_{\widetilde{C}_j}+\deg D_j=2g_j-2+m_j$$

이다. 각 node는 normalization에서 두 preimage를 가지므로 $\sum_{j=1}^c m_j=2d$이고, 따라서 이 degree들의 합은 [명제 2](#prop2){: data-lid="lhuop" }에 의하여

$$\sum_{j=1}^c(2g_j-2)+2d=2(g-d+c-1)-2c+2d=2g-2$$

이다. 마찬가지로 marked point $p_1,\ldots,p_n$을 더한 $\omega_C(p_1+\cdots+p_n)$을 당긴 것의 degree의 합은 $2g-2+n$이다.

## 준안정 곡선의 변형

이제 nodal curve의 deformation theory를 살펴보자. Node $p$에서의 first-order local deformation space를 $T_p^1$로 적자. [\[스킴\] §변형이론과 여접 복합체, ⁋예시 6](/ko/math/scheme_theory/deformation_theory#ex6){: data-lid="y2bip" }에서 affine node $Z(\x\y)$에 대하여 $T_p^1\cong\mathbb{K}$이고, 그 generator를 $\x\y-\epsilon$으로 나타낼 수 있음을 이미 계산하였다. 모든 node가 이 local model을 가지는 반면 smooth point의 local deformation은 trivial하므로 다음을 얻는다.

::: 명제 3
Nodal curve $C$의 각 node $p$에서 first-order local deformation들의 공간 $T_p^1$은 $1$차원이다.
:::

이 한 차원의 기하적인 의미는 family $\x\y=\t$로 나타낼 수 있다.

{% diagram Math/Gromov_Witten_Theory/Deformations_of_Nodal_Curves-2.svg width="51.68em" alt="the local fibers xy=t over the deformation space" %}

한편 prestable curve는 nodal curve $C$의 smooth locus에 marked point $p_1,\ldots,p_n$을 둔 것이다. 따라서 위 그림에 marked point들을 더해주면, 이들은 curve가 deform됨에 따라 함께 움직이면서 각 $p_i$를 지나는 section을 정의한다. 그럼 marked point들이 서로 같아질 수 없으므로 이 section들은 disjoint하게 되며, 따라서 prestable curve의 first-order deformation은 underlying curve의 deformation과 이 marked section들을 함께 택한 자료로 주어진다. 이 때 각 자료 사이의 isomorphism은 $\Spec\mathbb{K}[\epsilon]$ 위의 family들의 isomorphism으로서, central fiber에서 identity이고, 각 marked section을 그에 대응하는 marked section으로 보내는 것이다. 이러한 isomorphism class들이 이루는 $\mathbb{K}$-vector space를 $T^1(C,p_\bullet)$로 적는다. 이는 [\[스킴\] §변형이론과 여접 복합체, ⁋정리 11](/ko/math/scheme_theory/deformation_theory#thm11){: data-lid="fqff9" }의 $T^1$을 marked curve에 적용한 것으로, 같은 방식으로 모든 marked section을 보존하는 infinitesimal automorphism들의 $\mathbb{K}$-vector space를 $T^0(C,p_\bullet)$로 적는다. 

이들 $T^0(C,p_\bullet)$과 $T^1(C,p_\bullet)$은 underlying nodal curve에 새로 추가된 marked point들이 추가로 부과하는 조건으로 정해지므로, 이 두 조건을 별도로 나누어 보는 것이 합리적이다. 우선 deformation 쪽의 경우, 우리는 이미 위에서 $T_p^1$은 오직 node에서만 생기는 것을 살펴보았으며, 정의에 의해 marked point들은 smooth point에만 찍히므로 여기에 영향을 미치지 않는다. 즉 node에서 계산한 $T_p^1$은 prestable curve에 대해서도 동일하게 유지된다. 

새로 추가한 marked point들이 영향을 미치는 것은 automorphism 쪽으로, 여기서는 infinitesimal automorphism이 marked section을 보존해야 한다. 국소적으로, $C$ 위의 함수 $f$에 automorphism $\Phi$는

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

지금까지의 계산을 [\[스킴\] §변형이론과 여접 복합체, ⁋정리 11](/ko/math/scheme_theory/deformation_theory#thm11){: data-lid="6chlh" }의 언어로 다시 정리해 두자. 이를 통해 우리는 앞선 명제들에서 수행한 local한 계산을 곡선 전체의 deformation으로 이어 붙이고, 고차 deformation의 obstruction이 놓이는 $T^2$까지 계산할 수 있다. 표기의 편의를 위해 $\LL_C=\LL_{C/\mathbb{K}}$, $\Omega_C=\Omega_{C/\mathbb{K}}$라 하면, marked point가 없는 경우, 이 정리가 주는 공간

$$T^i(C)=\Ext^i_C(\LL_C,\mathcal{O}_C)$$

들 중 $i=0,1,2$는 다음과 같이 기하적으로 해석할 수 있다. 

- $T^1(C)$는 $\Spec\mathbb{K}[\epsilon]$ 위의 flat family 가운데 central fiber가 $C$인 것들, 곧 $C$의 first-order deformation들의 isomorphism class를 잰다. 여기서 trivial deformation $C\times\Spec\mathbb{K}[\epsilon]$은 $0$에 대응한다.
- $T^0(C)$는 trivial deformation의 automorphism 가운데 central fiber에서 identity인 것들, 곧 $C$의 infinitesimal automorphism을 잰다. 앞에서 본 것과 같이 이들은 국소적으로 $f\mapsto f+\epsilon v(f)$의 꼴이므로 $T^0(C)$는 $C$ 위의 global vector field들의 공간이며, $\Aut(C)$의 항등원에서의 tangent space이다.
- $T^2(C)$는 이러한 deformation을 고차의 deformation으로 연장할 때의 obstruction을 통제한다.

일반적으로 $\LL_C$는 degree $0$ 이상에서 항을 갖는 complex로, 일반적인 singular scheme에서는 이 complex가 담고 있는 정보를 $\Omega_C$로 옮기는 방법이 존재하지 않는다. 그러나 우리의 경우인 nodal curve에서는 $\LL_C$는 degree $0$에 놓인 $\Omega_C$와 quasi-isomorphic하며, 아래에서 보듯 이는 node의 local model이 hypersurface이고 reduced라는 데서 온다. 이를 확인하기 위해 우선 $\LL_C\rightarrow H_0(\LL_C)$를 정의하자. 이는 오직 degree $0$에서만 quotient map $(\LL_C)_0\rightarrow H_0(\LL_C)$로, 나머지 degree에서는 $0$으로 정의되는 map이다. 이 map은 $\LL_C$를 나타내는 complex의 선택에 의존하지 않고 잘 정의되는 것을 확인할 수 있다. 또 [\[스킴\] §변형이론과 여접 복합체, ⁋명제 9](/ko/math/scheme_theory/deformation_theory#prop9){: data-lid="cj6r9" } 직전에서 본 것과 같이 $H_0(\LL_C)=\Omega_C$이므로 이 map은 morphism $\LL_C\rightarrow\Omega_C$이고, 정의에 의하여 $H_0$에서 isomorphism이다.

우리 주장은 이것이 모든 $i\geq1$에 대하여도 $H_i(\LL_C)=0$을 만족한다는 것이며, 이는 국소적인 조건이므로 각 점의 근방에서 확인하면 된다. 우선 $C$의 smooth point 근방에서는 [\[스킴\] §변형이론과 여접 복합체, ⁋명제 9](/ko/math/scheme_theory/deformation_theory#prop9){: data-lid="xoabf" }의 증명에서와 같이 cotangent complex가 locally free sheaf $\Omega_C$ 하나와 quasi-isomorphic하므로 더 보일 것이 없다. 문제가 될 수 있는 것은 node 근방으로, $C$는 étale-local하게 local model $R=\mathbb{K}[\x,\y]/(\x\y)$로 주어지고, cotangent complex는 étale morphism에 의한 pullback과 compatible하므로 $R$에서 확인하면 충분하다. 이는 $\mathbb{K}[\x,\y]$를 nonzerodivisor 하나로 자른 것이므로 local complete intersection이고 ([\[스킴\] §완전교차, ⁋정의 1](/ko/math/scheme_theory/complete_intersections#def1){: data-lid="9arnl" }), 따라서 [\[스킴\] §변형이론과 여접 복합체, §§소박한 여접 복합체와 매끄러움](/ko/math/scheme_theory/deformation_theory#소박한-여접-복합체와-매끄러움){: data-lid="mc2dh" }에서 보았듯 $\LL_R$은 presentation $\mathbb{K}[\x,\y]\rightarrow R$에 대한 naive cotangent complex $\NL_R$과 quasi-isomorphic하다. 이 presentation의 conormal module $(\x\y)/(\x\y)^2$는 $\x\y$의 class 하나를 basis로 갖는 free $R$-module이므로, 해당 링크에서의 Jacobian 계산에 $f=\x\y$를 대입하면

$$\LL_R\simeq \NL_R\cong\Bigl[\at{1}{R}\overset{\bar{d}}{\longrightarrow}\at{0}{R\dd{\x}\oplus R\dd{\y}}\Bigr],\qquad\bar{d}(1)=\y\dd{\x}+\x\dd{\y}$$

을 얻는다. 이제 우리가 보여야 할 것은 $H_1(\NL_R)=\ker\bar{d}$가 $0$이 된다는 것 뿐이다. 실제로, 만일 

$$\bar{d}(c)=c(\y\dd{\x}+\x\dd{\y})=0$$

이라면 $R\dd{\x}\oplus R\dd{\y}$가 free이므로 $c\y=c\x=0$이고, 앞에서 살펴보았듯

$$\ann(\y)=(\x),\qquad \ann(\x)=(\y)$$

이고 $(\x)\cap(\y)=0$이므로 $c=0$이다. 또 $\NL_R$은 degree $0$과 $1$에만 항을 가지므로 $i\geq2$에서도 $H_i(\LL_R)=0$이다. 이로써 smooth point 근방과 node 근방 모두에서 $i\geq1$에 대하여 $H_i(\LL_C)=0$임을 확인하였으므로 $\LL_C\rightarrow\Omega_C$는 quasi-isomorphism이다. 한편 $T^i(C)=\Ext^i_C(\LL_C,\mathcal{O}_C)$와 $\mathcal{T}^q_{C/\mathbb{K}}=\sExt^q(\LL_C,\mathcal{O}_C)$는 원래 derived category $D(\mathcal{O}_C)$에서 정의된 대상이므로, 이제 이들을 계산할 때 $\LL_C$를 $\Omega_C$로 바꾸어도 된다. 즉

$$T^i(C)=\Ext^i_C(\Omega_C,\mathcal{O}_C),\qquad\mathcal{T}^q_{C/\mathbb{K}}=\sExt^q(\Omega_C,\mathcal{O}_C)$$

이 성립한다. 여기서 $\mathcal{T}^q_{C/\mathbb{K}}$는 [\[스킴\] §변형이론과 여접 복합체, ⁋정리 12](/ko/math/scheme_theory/deformation_theory#thm12){: data-lid="6d3kc" }의 국소 자료이며, 특히 $\mathcal{T}^0_{C/\mathbb{K}}$는 앞에서 계산한 $\mathcal{T}_{C/\mathbb{K}}$이다.

그럼 우선 marked point들은 smooth locus에 놓여 있으므로 $\mathcal{O}_C(\Sigma)$는 line bundle이며, 우리는 $\Omega_C$를 이것으로 twist한 $\Omega_C(\Sigma)=\Omega_C\otimes\mathcal{O}_C(\Sigma)$의 sheaf Ext를 계산한다. 우리가 보일 것은 다음의 식들

$$\sHom(\Omega_C(\Sigma),\mathcal{O}_C)=\mathcal{T}_{C/\mathbb{K}}(-\Sigma),\qquad\sExt^1(\Omega_C(\Sigma),\mathcal{O}_C)=\bigoplus_{p\in\Sing C}T_p^1,\qquad\sExt^q(\Omega_C(\Sigma),\mathcal{O}_C)=0\quad(q\geq2)$$

이다. Smooth point 근방에서는 $\Omega_C(\Sigma)=\Omega_C\otimes\mathcal{O}_C(\Sigma)$가 line bundle이므로 $q\geq1$에서 $\sExt^q=0$이고, $\sHom$은 그 dual $\mathcal{T}_{C/\mathbb{K}}\otimes\mathcal{O}_C(-\Sigma)=\mathcal{T}_{C/\mathbb{K}}(-\Sigma)$, 곧 marked point를 보존하는 infinitesimal automorphism들의 sheaf이다. 문제가 되는 것은 node 근방으로, marked point는 node와 만나지 않으므로 이 근방에서는 $\Omega_C(\Sigma)=\Omega_C$이고, 앞에서와 같이 local model $R=\mathbb{K}[\x,\y]/(\x\y)$에서 $\Ext^q_R(\Omega_R,R)$을 계산하면 된다. 우선, 앞에서 $\bar{d}$가 injective임을 보였으므로

$$0\longrightarrow R\overset{\bar{d}}{\longrightarrow}R\dd{\x}\oplus R\dd{\y}\longrightarrow\Omega_R\longrightarrow0$$

은 두 항으로 이루어진 $\Omega_R$의 free resolution이며 여기에 $\Hom_R(-,R)$를 취하면 $\Ext^q_R(\Omega_R,R)$은 complex

$$\at{0}{\Hom_R(R\dd{\x}\oplus R\dd{\y},R)}\overset{\bar{d}^\ast}{\longrightarrow}\at{1}{\Hom_R(R,R)}$$

의 $q$번째 cohomology로 계산할 수 있으며, 특히 $q\geq 2$에서는 이 값이 $0$이 되어 node 근방에서도 local obstruction이 없다. 위 complex의 왼쪽 항의 원소는 $\dd{\x}$, $\dd{\y}$에서의 값 $(a,b)$로, 오른쪽 항의 원소는 $1$에서의 값으로 정해지며, $\bar{d}(1)=\y\dd{\x}+\x\dd{\y}$이므로 $\bar{d}^\ast$는

$$R^2\rightarrow R,\qquad(a,b)\mapsto a\y+b\x$$

로 쓸 수 있다. 이 명시적인 함수를 통해 cohomology를 직접 계산하면, degree $0$의 cohomology $\ker\bar{d}^\ast$는 $a\y+b\x=0$을 만족하는 $(a,b)$들의 모임인데, 이는 [명제 4](#prop4){: data-lid="4akca" } 앞에서 derivation $v$에 대해 얻은 조건 $v(\x\y)=\y a+\x b=0$과 같으므로 $\Hom_R(\Omega_R,R)=\Der_\mathbb{K}(R,R)$이며, 이 근방의 infinitesimal automorphism들의 sheaf $\mathcal{T}_{C/\mathbb{K}}$를 다시 얻는다. Degree $1$의 cohomology는 $\coker\bar{d}^\ast$이고, $\bar{d}^\ast$의 image가 $\x$와 $\y$로 생성되는 ideal이므로 이는 $R/(\x,\y)=\mathbb{K}$가 되며, 이들은 node 하나에 놓인 $1$차원 공간을 주므로 identification $\mathcal{T}^1_{C/\mathbb{K}}=\sExt^1(\Omega_C,\mathcal{O}_C)$에 의해 이것이 곧 node의 deformation space $T_p^1$임을 안다. 즉 앞에서 marked point의 영향을 $T^0$과 $T^1$으로 나누어 살펴본 것은 $\Omega_C(\Sigma)$의 sheaf Ext를 계산한 것이다.

실제로 $\Omega_C(\Sigma)$는 marked point가 있을 때의 deformation을 재는 대상이다. 이를 확인하기 위해 우선 다음의 short exact sequence

$$0\rightarrow\Omega_C\rightarrow\Omega_C(\Sigma)\rightarrow\bigoplus_{j=1}^n\kappa(p_j)\rightarrow0$$

을 생각하자. 여기에 $\Hom_C(-,\mathcal{O}_C)$를 적용하면 long exact sequence

$$0\rightarrow\Ext^0_C(\Omega_C(\Sigma),\mathcal{O}_C)\rightarrow\Ext^0_C(\Omega_C,\mathcal{O}_C)\rightarrow\bigoplus_{j=1}^nT_{p_j}C\rightarrow\Ext^1_C(\Omega_C(\Sigma),\mathcal{O}_C)\rightarrow\Ext^1_C(\Omega_C,\mathcal{O}_C)\rightarrow0$$

과 isomorphism $\Ext^2_C(\Omega_C(\Sigma),\mathcal{O}_C)\cong\Ext^2_C(\Omega_C,\mathcal{O}_C)$를 얻는다. 여기서 우리는 다음의 isomorphism

$$\Ext^q_C(\kappa(p_j),\mathcal{O}_C)\cong\begin{cases}T_{p_j}C&q=1\\0&q\neq1\end{cases}$$

을 사용하였다.

한편 marked point를 잊는 과정을 deformation의 언어로 직접 따라가면 다음의 exact sequence

$$0\rightarrow T^0(C,p_\bullet)\rightarrow T^0(C)\rightarrow\bigoplus_{j=1}^nT_{p_j}C\rightarrow T^1(C,p_\bullet)\rightarrow T^1(C)\rightarrow0$$

를 얻는다. 여기서 $T^0(C)\rightarrow\bigoplus_{j=1}^nT_{p_j}C$는 vector field를 각 $p_j$에서의 값으로 보내고, $\bigoplus_{j=1}^nT_{p_j}C\rightarrow T^1(C,p_\bullet)$은 곡선은 그대로 둔 채 marked point만 움직이며, $T^1(C,p_\bullet)\rightarrow T^1(C)$는 marked point를 잊는다. 이를 위의 long exact sequence와 비교하면 $T^0(C,p_\bullet)=\Ext^0_C(\Omega_C(\Sigma),\mathcal{O}_C)$, $T^i(C)=\Ext^i_C(\Omega_C,\mathcal{O}_C)$이고 evaluation map도 같으므로, 남은 두 항 $T^1(C,p_\bullet)$과 $\Ext^1_C(\Omega_C(\Sigma),\mathcal{O}_C)$도 같은 차원을 가지며 실제로 canonical하게 isomorphic하다. 즉 위의 long exact sequence는 marked point를 잊는 과정을 $\Ext$로 적은 것이다. 따라서 앞으로 $i=0,1,2$에 대하여 $T^i(C,p_\bullet)=\Ext^i_C(\Omega_C(\Sigma),\mathcal{O}_C)$로 적으며, $i=2$인 경우 이는 위의 isomorphism에 의하여 $T^2(C)$와 같다. 

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
표기의 편의상 $\mathcal{H}=\mathcal{T}_{C/\mathbb{K}}(-\Sigma)$로 적고, $C$의 node의 개수를 $d$라 하면 [정리 5](#thm5){: data-lid="c3l1e" }에 의하여 

$$\dim T^1=h^1(\mathcal{H})+d,\qquad \dim T^0=h^0(\mathcal{H})$$

이므로 구하고자 하는 값은 $d-\rchi(C, \mathcal{H})$이다. 이제 [명제 4](#prop4){: data-lid="arwum" }와 [\[스킴\] §스킴의 층 코호몰로지, ⁋따름정리 4](/ko/math/scheme_theory/sheaf_cohomology_of_schemes#cor4){: data-lid="tpsgt" }에 의하여

$$\rchi(C, \mathcal{H})=\rchi\bigl(\widetilde{C}, \mathcal{T}_{\widetilde{C}/\mathbb{K}}(-D-\widetilde{\Sigma})\bigr)$$

이다. 

위 등식의 우변을 각 성분마다 계산하자. [\[대수다양체\] §곡선에서의 리만-로흐 정리, ⁋명제 3](/ko/math/algebraic_varieties/riemann_roch_theorem#prop3){: data-lid="khrzv" }을 genus $g_j$의 성분 $\widetilde{C}_j$의 canonical divisor $K_{\widetilde{C}_j}$에 적용하면 $\deg\omega_{\widetilde{C}_j}=2g_j-2$를 얻는다. 따라서 $\mathcal{T}_{\widetilde{C}_j/\mathbb{K}}\cong\omega_{\widetilde{C}_j}^\vee$는 degree $2-2g_j$의 line bundle이다. 그 위에 놓인 $D+\widetilde{\Sigma}$의 점 개수를 $s_j$라 하면 twisted line bundle의 degree는 $2-2g_j-s_j$이고, 같은 명제에 의하여

$$\rchi\bigl(\widetilde{C}_j, \mathcal{T}_{\widetilde{C}_j/\mathbb{K}}(-D-\widetilde{\Sigma})\bigr)=(2-2g_j-s_j)+1-g_j=3-3g_j-s_j$$

이다. 이제 node가 preimage를 두 개 주고 각 marked point가 하나를 주므로 $\sum_js_j=2d+n$이고, 따라서 $c$개의 성분에 대하여

$$\rchi(C, \mathcal{H})=\sum_{j=1}^c(3-3g_j-s_j)=3c-3\sum_jg_j-2d-n$$

이다. 여기에 [명제 2](#prop2){: data-lid="b8s52" }가 주는 $\sum_jg_j=g-d+c-1$을 넣으면

$$\rchi(C, \mathcal{H})=3c-3(g-d+c-1)-2d-n=-3g+d+3-n$$

이 되어 원하는 결과를 얻는다.
:::

우변이 $d$와 $c$에 의존하지 않는다는 것이 이 계산의 핵심이다. Node를 하나 더 만들면 국소 변형이 하나 늘지만 접합의 자유도가 그만큼 줄어, 두 차원의 차는 곡선의 위상 자료인 $g$와 $n$만으로 결정된다.

## 장애의 소멸

앞에서 우리는 $T^1(C,p_\bullet)$이 prestable curve들을 모아둔 공간에서 tangent space의 역할을 하는 것을 보았다. 만일 stack이 smooth라면 그 차원은 $\dim T^1(C,p_\bullet)-\dim T^0(C,p_\bullet)$이다. 그러나 일반적으로 moduli space들은 아주 singular하므로, 이를 기대할 수는 없다. 따라서 smoothness를 확인하기 위해, 주어진 deformation을 더 두꺼운 base 위로 계속 연장할 수 있는지 살펴보자. 이를 위해 $\mathbb{K}[\epsilon]$을 residue field가 $\mathbb{K}$인 일반적인 local Artin $\mathbb{K}$-algebra $A$로 바꾼다.

Local Artin $\mathbb{K}$-algebra $A$에 대하여, $(C,p_\bullet)$의 $A$ 위의 *deformation*은 flat proper family $\pi_A:\mathcal{C}_A\rightarrow\Spec A$와 central fiber의 identification $\mathcal{C}_A\times_{\Spec A}\Spec\mathbb{K}\cong C$, 그리고 이 identification 아래에서 $p_j$로 제한되는 서로 만나지 않는 section $\sigma_{j,A}:\Spec A\rightarrow\mathcal{C}_A$들을 택한 것이다. 앞에서 살펴본 first-order deformation은 $A=\mathbb{K}[\epsilon]$인 특수한 경우이다. Surjection $A'\rightarrow A$를 따라 이를 연장한다는 것은 $A'$ 위의 deformation을 찾아

$$\mathcal{C}_{A'}\times_{\Spec A'}\Spec A\cong\mathcal{C}_A$$

가 central fiber의 identification과 marked section들을 보존하도록 하는 것이다. 즉 이미 정해진 deformation을 유지하면서 더 높은 차수의 자료를 보태는 것이다. 

위에서 주어진 surjection $A'\rightarrow A$의 kernel을 $J$, $A'$의 maximal ideal을 $\mathfrak{m}$이라 하자. $A'$이 local Artin ring이므로 $\mathfrak{m}^N=0$인 $N$이 존재하고, 따라서 이 surjection은

$$A'=A'/\mathfrak{m}^NJ\longrightarrow\cdots\longrightarrow A'/\mathfrak{m}J\longrightarrow A'/J=A$$

로 분해된다. 각 단계의 kernel $\mathfrak{m}^rJ/\mathfrak{m}^{r+1}J$는 source ring의 maximal ideal에 의해 소멸하므로, $\mathfrak{m}_{A'}I=0$인 kernel $I$를 갖는 surjection $A'\rightarrow A$에 대해서만 연장을 보이면 충분하다. 이 경우 $I^2=0$이므로 $A'\rightarrow A$는 square-zero extension이 되며, 따라서 [\[스킴\] §변형이론과 여접 복합체, ⁋정리 11](/ko/math/scheme_theory/deformation_theory#thm11){: data-lid="cmkkl" }을 적용할 수 있게 된다. 그럼 coefficient sheaf가 central fiber 위의 $\mathcal{O}_C\otimes_\mathbb{K}I$이므로, flat base change와 $L_C\simeq\Omega_C$를 사용하면 이 obstruction은

$$\ob(\mathcal{C}_A/A')\in\Ext^2_C(\Omega_C,\mathcal{O}_C\otimes_\mathbb{K}I)\cong T^2(C)\otimes_\mathbb{K}I$$

에 놓이며, 이것이 $0$인 것은 연장이 존재하는 것과 동치이다. 곡선을 연장한 뒤 marked section은 $p_j$ 근방의 smoothness에 의해 항상 extend되므로, 보여야 할 것은 $T^2(C)\cong\Ext^2_C(\Omega_C(\Sigma),\mathcal{O}_C)$가 $0$이라는 것이다. 이를 확인하기 위해 [\[층론\] §층의 유도 범주와 유도 functor, ⁋따름정리 11](/ko/math/sheaf_theory/derived_category_of_sheaves#cor11){: data-lid="r5mnh" }이 주는 spectral sequence

$$E_2^{p,q}=H^p\bigl(C,\sExt^q(\Omega_C(\Sigma),\mathcal{O}_C)\bigr)\Longrightarrow\Ext^{p+q}_C(\Omega_C(\Sigma),\mathcal{O}_C)$$

의 total degree $2$ 부분을 보면 다음을 얻는다.

::: 명제 7
$n$개의 marked point를 갖는 prestable curve $(C,p_\bullet)$에 대하여 $\Ext^2_C(\Omega_C(\Sigma),\mathcal{O}_C)=0$이다. 따라서 $(C,p_\bullet)$의 deformation은 *unobstructed*이다. 
:::
::: 증명
[정리 5](#thm5){: data-lid="suizo" } 앞에서 본 것과 같이 $C$ 위의 quasi-coherent sheaf의 cohomology는 degree $2$ 이상에서 소멸하므로 

$$E_2^{2,0}=H^2\bigl(C,\sExt^0(\Omega_C(\Sigma),\mathcal{O}_C)\bigr)=H^2(C,\mathcal{T}_{C/\mathbb{K}}(-\Sigma))=0$$

이다. 또, 같은 곳에서 $\sExt^1(\Omega_C(\Sigma),\mathcal{O}_C)$는 node들에 놓인 skyscraper sheaf인 것을 확인하였으므로 그 higher cohomology가 소멸하여 

$$E_2^{1,1}=H^1\bigl(C,\sExt^1(\Omega_C(\Sigma),\mathcal{O}_C)\bigr)=0$$

이고, 마지막으로 $\sExt^2(\Omega_C(\Sigma),\mathcal{O}_C)=0$이므로 $E_2^{0,2}=0$이다. 따라서 total degree $2$의 $E_2$항이 모두 $0$이므로 $\Ext^2_C(\Omega_C(\Sigma),\mathcal{O}_C)=0$이다.
:::

점 $[(C,p_\bullet)]$의 formal neighborhood를 생각하자. 이는 residue field가 $\mathbb{K}$인 complete local $\mathbb{K}$-algebra $S$로, 직관적으로 $S/\mathfrak{m}_S^{k+1}$은 그 점의 $k$차 무한소 근방, 곧 $k$차까지만 두께를 갖는 점이고, $S$는 이들의 inverse limit이므로 $S$를 본다는 것은 이를 점차 늘리는 극한을 취해 전체 차수를 보는 것이다. 이제 각각의 $k$마다 $S/\mathfrak{m}_S^{k+1}$ 위에 정의된 $(C,p_\bullet)$의 $k$차 deformation $\mathcal{C}_k$들이 이 inverse system과 호환된다면, 즉 $\mathcal{C}_{k+1}$을 $S/\mathfrak{m}_S^{k+1}$로 base change한 것이 deformation으로서 $\mathcal{C}_k$와 isomorphic하다면 이를 $S$ 위의 *formal deformation*이라 부른다. 예를 들어 $S=\mathbb{K}[[\t]]$이면 이는 $\t$에 대한 차수를 늘려가며 맞춘 family들을 차례로 연장하며 모은 것이다. $S$가 local Artin $\mathbb{K}$-algebra이면 충분히 큰 $k$에 대하여 $S/\mathfrak{m}_S^{k+1}=S$이므로 $S$ 위의 formal deformation은 곧 $S$ 위의 deformation이다. 즉 local Artin $\mathbb{K}$-algebra 위의 deformation은 두께가 유한하다는 finiteness 조건이 붙은 formal deformation의 특수한 경우이다.

이제 residue field가 $\mathbb{K}$인 complete local $\mathbb{K}$-algebra $R$을 고정하자. 그럼 이 위에 정의된 formal deformation $\mathcal{X}$가 *versal*이라는 것은 임의의 formal deformation이 주어졌을 때 이것이 $\mathcal{X}$의 pullback으로 결정되는 것이다. 더 정확하게 말하자면, residue field가 $\mathbb{K}$인 임의의 complete local $\mathbb{K}$-algebra $S$ 위의 임의의 formal deformation이 주어졌을 때, 어떠한 local homomorphism $R\rightarrow S$를 따라 $\mathcal{X}$를 당겨 이 formal deformation을 얻을 수 있는 것이며, 우리는 추가로 $S=\mathbb{K}[\epsilon]$인 경우 이러한 local homomorphism이 <em-ko>유일하게</em-ko> 결정될 것 또한 요구한다. 직관적으로 local homomorphism $R\rightarrow\mathbb{K}[\epsilon]$은 곧 $R$의 tangent vector이며, $\mathbb{K}[\epsilon]$ 위의 deformation들은 $T^1(C, p_\bullet)$을 이루므로 이 조건은 $R$의 tangent space와 $T^1(C, p_\bullet)$을 identify하는 것이다. 

그럼 $(C,p_\bullet)$은 versal formal deformation을 가진다는 것이 알려져 있다. 직관적으로 이는 $N=\dim T^1(C,p_\bullet)$에 대하여 $T^1(C,p_\bullet)$의 basis에 대응하는 coordinate $\s_1,\ldots,\s_N$을 잡고, $\mathbb{K}[[\s_1,\ldots,\s_N]]/(\s_1,\ldots,\s_N)^2$ 위의 first-order deformation에서 출발하여 이를 한 차수씩 연장해 나가는 것이다. 각 단계의 연장에 대한 obstruction은 [\[스킴\] §변형이론과 여접 복합체, ⁋정리 11](/ko/math/scheme_theory/deformation_theory#thm11){: data-lid="lqfm6" }에 의하여 $T^2(C)$로 통제되므로, 이 obstruction이 사라지도록 $\s_1,\ldots,\s_N$ 사이에 관계식을 넣어야만 연장이 된다. 이렇게 얻어진 결과는 이 관계식들이 생성하는 ideal $J$에 대하여

$$R\cong\mathbb{K}[[\s_1,\ldots,\s_N]]/J\tag{$\ast$}$$

이며, 이 때 필요한 관계식의 개수는 $\dim T^2(C)$ 이하이다. 그런데 우리 경우에는 [명제 7](#prop7){: data-lid="ctbij" }에 의하여 $T^2(C)=0$이므로 $J=0$이고, 따라서 $R\cong\mathbb{K}[[\s_1,\ldots,\s_N]]$이다. 이는 점 $[(C,p_\bullet)]$의 formal neighborhood가 smooth하다는 뜻이다. ([\[가환대수학\] §정칙국소환, ⁋명제 4](/ko/math/commutative_algebra/regular_local_rings#prop4){: data-lid="v5ayc" }, [\[스킴\] §매끄러운 사상과 에탈 사상, ⁋정의 1](/ko/math/scheme_theory/smooth_and_etale_morphisms#def1){: data-lid="fzprr" }) 이 $R$을 $(C,p_\bullet)$의 *versal base*라 부른다. 특히 $T^0(C,p_\bullet)=0$이면 위의 local homomorphism이 $S=\mathbb{K}[\epsilon]$뿐만 아니라 모든 $S$에 대하여 유일하며, 이 경우 versal formal deformation을 *universal*이라 부른다. 

## 준안정 곡선의 모듈라이 스택

지금까지의 계산은 한 곡선 $(C,p_\bullet)$의 근방, 곧 그 versal base 위에서 이루어졌다. 그러나 이 논의는 임의의 prestable curve $(C,p_\bullet)$에 대하여 성립하므로, prestable curve들을 모은 moduli는 모든 점에서 smooth할 것이다. 이 moduli space를 정의하기 위해서는 임의의 scheme $T$ 위에 정의된 family를 명시해주면 된다 ([\[스택\] §모듈라이 공간, ⁋정의 1](/ko/math/stacks/moduli_spaces#def1){: data-lid="lvrdq" })

::: 정의 8
Scheme $T$ 위의 genus $g$, $n$개의 marked point를 갖는 *prestable curve*란 flat proper morphism $\pi:\mathcal{C}\rightarrow T$와 section $\sigma_1,\ldots,\sigma_n:T\rightarrow\mathcal{C}$들의 짝으로서, $T$의 각 geometric point $\bar{t}$ 위의 fiber $(\mathcal{C}_{\bar{t}},\sigma_1(\bar{t}),\ldots,\sigma_n(\bar{t}))$가 $n$개의 marked point를 갖는 genus $g$의 prestable curve인 것이다. 각 scheme $T$에 이들과, 그 사이의 $T$-isomorphism 가운데 section을 보존하는 것들이 이루는 groupoid를 대응시키는 moduli functor를 $\mathfrak{M}_{g,n}$으로 적는다.
:::

이 moduli functor가 locally of finite type인 algebraic stack, 곧 [\[스택\] §모듈라이 공간, ⁋정의 6](/ko/math/stacks/moduli_spaces#def6){: data-lid="fvex6" }의 moduli stack이 된다는 것은 잘 알려져 있다. $\mathfrak{M}_{g,n}$의 $\Spec\mathbb{K}$ 위의 object는 [정의 1](#def1){: data-lid="9o4n7" }의 prestable curve이고, 그 stabilizer는 automorphism group $\Aut(C,p_\bullet)$이며, 앞에서 본 것과 같이 그 tangent space가 $T^0(C,p_\bullet)$이다. 또 $(C,p_\bullet)$의 $A$ 위의 deformation은 central fiber를 $(C,p_\bullet)$로 identify하는 자료와 함께 택한 morphism $\Spec A\rightarrow\mathfrak{M}_{g,n}$이다. Algebraic stack이 한 점에서 smooth하다는 것은 그 점의 versal base가 power series ring이라는 것과 같고, 앞 절에서 각 점 $[(C,p_\bullet)]$의 versal base가 power series ring임을 보였으므로 $\mathfrak{M}_{g,n}$은 smooth하다. 따라서 다음이 성립한다.

::: 정리 9
$\mathfrak{M}_{g,n}$은 차원 $3g-3+n$의 smooth algebraic stack이다.
:::
::: 증명
앞에서 본 것과 같이 $\mathfrak{M}_{g,n}$은 locally of finite type인 smooth algebraic stack이므로, 차원에 대한 주장만 보이면 충분하다. $(C,p_\bullet)$을 나타내는 점 근방의 smooth atlas $W\rightarrow\mathfrak{M}_{g,n}$과 그 점 위의 closed point $w\in W$를 택하자. 이 점에서의 차원은 $w$에서 $W\rightarrow\mathfrak{M}_{g,n}$의 relative dimension $r$에 대하여 $\dim_wW-r$로 주어진다. ([\[스택\] §대수적 스택, ⁋정의 6](/ko/math/stacks/algebraic_stacks#def6){: data-lid="5ac8a" }) 그럼 $(C,p_\bullet)$을 나타내는 점 $\Spec\mathbb{K}\rightarrow\mathfrak{M}_{g,n}$ 위의 fiber $W_0=W\times_{\mathfrak{M}_{g,n}}\Spec\mathbb{K}$는 차원 $r$의 smooth scheme이고, $w$에 대응하는 점에서 tangent space 사이의 exact sequence

$$0\rightarrow T^0(C,p_\bullet)\rightarrow T_wW_0\rightarrow T_wW\rightarrow T^1(C,p_\bullet)\rightarrow0$$

가 존재한다. 여기서 $W_0$은 $W$의 점과, 그 위의 곡선을 $(C, p_\bullet)$과 identify해 주는 isomorphism의 pair로 생각할 수 있다. 그럼 첫째 map $T^0\rightarrow T_wW_0$은 이 identification을 infinitesimal automorphism만큼 바꾸는 것을 의미하고, 둘째 map은 identification을 잊는 $W_0\rightarrow W$의 미분으로 주어지며, 셋째 map은 $W$의 tangent vector $\Spec\mathbb{K}[\epsilon]\rightarrow W$를 따라 $W$ 위의 family를 당겨 얻는 first-order deformation이다. 따라서 이 exact sequence로부터

$$\dim_wW-r=\dim T_wW-\dim T_wW_0=\dim T^1(C,p_\bullet)-\dim T^0(C,p_\bullet)=3g-3+n$$

을 얻으며, 여기서 마지막 등식은 [따름정리 6](#cor6){: data-lid="a0i84" }에 의한 것이다.
:::

위의 증명에서 $T^0(C,p_\bullet)$은 identification을 바꾸는 infinitesimal automorphism, 곧 점 $[(C,p_\bullet)]$의 stabilizer의 tangent space로 나타났으므로, $T^0(C,p_\bullet)\neq0$인 점에서는 stabilizer가 unramified하지 않고 따라서 $\mathfrak{M}_{g,n}$은 일반적으로 Deligne–Mumford stack이 아니다. ([\[스택\] §대수적 스택, ⁋정의 6](/ko/math/stacks/algebraic_stacks#def6){: data-lid="z8p7i" })

## Smoothing parameter

우리는 앞에서 [명제 7](#prop7){: data-lid="wetkp" }을 적용하면 versal base가 ($\ast$)와 같이

$$R\cong\mathbb{K}[[\s_1,\ldots,\s_N]]$$

으로 쓰여질 수 있음을 보았다. 정의에 의해 $R$의 각 coordinate는 prestable curve를 deform하는 방향을 나타내지만, 이렇게 적은 $\s_1,\ldots, \s_N$은 $T^1(C,p_\bullet)$의 basis에 대응하도록 잡은 것일 뿐 기하적인 의미는 없었다. 

이번 절에서 우리는 이 방향들을 조금 더 자세히 살펴본다. 구체적으로, 우리는 각각의 node $p$에서 [§§준안정 곡선의 변형](#준안정-곡선의-변형){: data-lid="9wb6j" }에서와 같이 node를 펴 주는 정도를 나타내는 smoothing parameter $\t_p$를 정의하고, 이들이 $R$에서 서로 독립적이며 따라서 위의 coordinate $\s_1,\ldots, \s_N$ 가운데 일부를 이들로 택할 수 있음을 보인다. 

Node $p$에서 $C$의 complete local ring은 앞에서 본 node의 국소 모형 $\mathbb{K}[\x,\y]/(\x\y)$를 completion하여 얻어지는 

$$\widehat{\mathcal{O}}_{C,p}\cong\mathbb{K}[[\u,\v]]/(\u\v)$$

으로 주어진다. 여기서 $\u$와 $\v$는 각각 normalization에서 node의 두 preimage가 속한 branch의 coordinate들이다. 그럼 앞서 논의한 deformation의 정의와 마찬가지로, local Artin $\mathbb{K}$-algebra $A$ 위의 $\widehat{\mathcal{O}}_{C,p}$의 deformation은 flat $A$-algebra $B$와, 각 fiber의 identification $B\otimes_A\mathbb{K}\cong\widehat{\mathcal{O}}_{C,p}$의 짝으로 주어진다. 이 때, 우리는 [명제 3](#prop3){: data-lid="p1den" }에 의하여 first-order deformation들의 공간 $T_p^1$은 $1$차원인 것을 알고, 해당 명제 직전에 그 원소들은 $\u\v=c\epsilon$의 꼴로 쓰일 수 있음을 보았다. 

이제 node의 versal formal deformation은 $\mathbb{K}[[\t]]$ 위의 family

$$\mathbb{K}[[\u,\v,\t]]/(\u\v-\t)$$

로 주어진다. 실제로 residue field가 $\mathbb{K}$인 complete local $\mathbb{K}$-algebra $S$ 위의 $\widehat{\mathcal{O}}_{C,p}$의 formal deformation은 coordinate를 적당히 잡으면 어떤 $f\in\mathfrak{m}_S$에 대하여 $S[[\u,\v]]/(\u\v-f)$의 꼴로 주어진다. 이러한 deformation은 $\u\v$를 들어 올린 방정식 하나로 잘리는데, 이 방정식을 $\mathfrak{m}_S$의 차수별로 정리하면 각 차수에서 오차항 가운데 $\u a+\v b$ 꼴의 부분은 coordinate를 $\u+b$, $\v+a$로 바꾸어 흡수되므로 상수항만 남기 때문이다. 이는 [\[스킴\] §변형이론과 여접 복합체, ⁋예시 6](/ko/math/scheme_theory/deformation_theory#ex6)에서 first-order deformation $\u\v=\epsilon h$가 $h(0)$만으로 결정되던 계산을 각 차수에서 반복한 것이다. 즉, 임의의 formal deformation은 위의 family를 local homomorphism $\t\mapsto f$를 따라 당긴 것이고, $S=\mathbb{K}[\epsilon]$이면 이 homomorphism $\t\mapsto c\epsilon$은 $T_p^1$의 원소 $\u\v=c\epsilon$에 의하여 유일하게 결정된다.

이제 $(C,p_\bullet)$의 versal formal deformation을 node $p$의 근방으로 제한하면 $\widehat{\mathcal{O}}_{C,p}$의 $R$ 위 formal deformation을 얻고, 위의 versality에 의하여 이는 node의 versal family를 어떤 local homomorphism $\mathbb{K}[[\t]]\rightarrow R$로 당긴 것이다. 이 homomorphism이 $\t$를 보내는 원소를 $\t_p\in\mathfrak{m}_R$로 적자. 그럼 tangent space 사이의 map

$$T^1(C,p_\bullet)\longrightarrow\bigoplus_{p\in\Sing C}T_p^1$$

은 deformation을 각 node 근방의 local deformation으로 제한하는 것이므로 [정리 5](#thm5){: data-lid="zx1zj" }의 오른쪽 map과 같고, 따라서 surjective이다. 이 일차 정보가 versal base 전체로 연장된다는 것이 다음 명제이다.

::: 명제 10
$n$개의 marked point와 $d$개의 node를 갖는 prestable curve $(C,p_\bullet)$의 versal base를 $R$이라 하고 $N=\dim T^1(C,p_\bullet)$이라 하자. 그럼 위의 원소 $\t_p$ ($p\in\Sing C$)와 적당한 $\s_1,\ldots,\s_{N-d}\in\mathfrak{m}_R$에 대하여

$$R=\mathbb{K}[[\{\t_p\}_{p\in\Sing C},\s_1,\ldots,\s_{N-d}]]$$

이다. 즉 node마다의 smoothing parameter $\t_p$들을 versal base의 coordinate의 일부로 택할 수 있으며, 이 coordinate에서 versal family의 node $p$ 근방의 complete local ring은 $R[[\u_p,\v_p]]/(\u_p\v_p-\t_p)$이다.
:::
::: 증명
Tangent space 사이의 map $T^1(C,p_\bullet)\rightarrow\bigoplus_pT_p^1$은 cotangent space 사이의 map, 곧 각 $\t_p$를 $\mathfrak{m}_R/\mathfrak{m}_R^2$에서의 class로 보내는 map의 dual이다. 따라서 [정리 5](#thm5){: data-lid="38w02" }에 의하여 이 map이 surjective라는 것은 $\t_p$들의 class가 $\mathfrak{m}_R/\mathfrak{m}_R^2$에서 linearly independent하다는 것과 같다. 이들을 basis로 확장하도록 $\s_1,\ldots,\s_{N-d}\in\mathfrak{m}_R$을 택하자. $R$은 $N$변수 power series ring이므로, class들이 $\mathfrak{m}_R/\mathfrak{m}_R^2$의 basis를 이루는 $N$개의 원소는 $R$의 변수로 택할 수 있다. 마지막 주장은 node $p$ 근방의 restriction이 local versal family $\mathbb{K}[[\u,\v,\t]]/(\u\v-\t)$를 $\t\mapsto\t_p$로 당긴 것이라는 $\t_p$의 정의에서 나온다.
:::

[명제 10](#prop10){: data-lid="s6m44" }에 의하여 node를 smoothing하는 것은 독립적으로 작용한다. 각 node $p$ 근방에서 versal family는 $\u_p\v_p=\t_p$의 꼴이며, 이 node 바깥에서는 $C$와 같이 smooth하므로 node $p$가 풀리지 않은 채 node로 남아있는 locus는 정확히 $\t_p=0$으로 정의되는 곳이다. 따라서 곡선이 node를 하나 이상 갖는 locus는

$$\prod_{p\in\Sing C}\t_p=0$$

으로 주어진다. 이는 서로 다른 coordinate hyperplane들의 합집합, 곧 normal crossings divisor이며 그 성분은 $C$의 node와 일대일로 대응한다. 특히 $C$의 node가 모두 남는 locus $\{\t_p=0\}_{p\in\Sing C}$의 tangent space는 [정리 5](#thm5){: data-lid="7y4l8" }의 오른쪽 map의 kernel, 곧 $H^1(C,\mathcal{T}_{C/\mathbb{K}}(-\Sigma))$이며, 이는 [정리 5](#thm5){: data-lid="i6j6b" } 뒤에서 이 항을 모든 node의 local model을 유지하는 변형으로 읽은 것과 일치한다.

지금까지의 결과는 versal base $R$에 대한 것이다. 이를 stack으로 올리기 위해서는 smooth atlas $W\rightarrow\mathfrak{M}_{g,n}$을 거쳐야 한다. 문제는 smooth atlas는 stack이 기억하던 isomorphism을 <em-ko>펼쳐준</em-ko> scheme이므로, 여기에는 곡선의 isomorphism class를 바꾸지 않는 방향이 더 있을 수 있다는 것이다. 따라서 $(C,p_\bullet)$을 나타내는 점 $w\in W$에서 $\widehat{\mathcal{O}}_{W,w}$는 $R$보다 클 수 있으며, $\t_p$들이 $W$ 위에서도 coordinate로 남는지는 따로 확인해야 한다. 이를 위해 [정리 9](#thm9){: data-lid="iq442" }의 증명을 다시 보면, $W$ 위의 family는 versality에 의하여 어떤 local homomorphism $R\rightarrow\widehat{\mathcal{O}}_{W,w}$를 따라 versal formal deformation을 당긴 것이고, 그 증명의 exact sequence에서 $T_wW\rightarrow T^1(C,p_\bullet)$가 surjective이므로 [명제 10](#prop10){: data-lid="ds93e" }의 증명과 같은 논법으로 $R$의 변수들이 $\widehat{\mathcal{O}}_{W,w}$의 변수의 일부가 된다. 즉 smoothing parameter $\t_p$들은 smooth atlas 위에서도 local coordinate의 일부이고, $\mathfrak{M}_{g,n}$ 안에서 node를 갖는 곡선들의 locus는 normal crossings divisor이며, 정확히 $k$개의 node를 갖는 곡선들의 locus는 codimension $k$이다.

위에서 살펴본 것은 versal family에 대한 내용이므로, 실제로 이를 사용하기 위해서는 임의의 family 위에서도 계산이 가능해야 한다. Residue field가 $\mathbb{K}$인 complete local $\mathbb{K}$-algebra $S$ 위의 $(C,p_\bullet)$의 formal deformation이 주어졌다 하자. 그럼 versality에 의하여 이는 적당한 local homomorphism $\phi:R\rightarrow S$를 따라 versal formal deformation을 pullback해서 얻어진 것이며, node $p$에서의 complete local ring은 $S[[\u,\v]]/(\u\v-\phi(\t_p))$이다. 특히 scheme $T$ 위의 prestable curve가 closed point $t$ 위의 fiber로 $(C,p_\bullet)$을 가지면, 이를 $t$에서 completion한 것은 $\widehat{\mathcal{O}}_{T,t}$ 위의 formal deformation이므로 위의 결과를 $S=\widehat{\mathcal{O}}_{T,t}$에 적용할 수 있고, 따라서 node가 어디서 남고 어떻게 펴지는지는 $\t_p$를 당긴 함수 $\phi(\t_p)\in\widehat{\mathcal{O}}_{T,t}$ 하나로 정해진다.

이제 우리는 boundary divisor의 normal bundle이 무엇인지 살펴본다. 위에서 살펴본 것에 의하여, boundary는 $\{\t_p=0\}$으로 주어지는 locus들이다. 이제 여기에서 벗어나는 방향을 보면, $\t_p$는 node의 versal base $\mathbb{K}[[\t]]$의 coordinate를 당긴 것이므로, versal base에서 $\{\t_p=0\}$의 normal 방향은 $T^1(C,p_\bullet)\rightarrow T_p^1$에 의하여 $T_p^1$과 identify된다. 즉 boundary에서 벗어나는 것은 node $p$를 일차로 펴는 방향에 해당한다. 이 때, node를 펴는 크기를 $\u\v=c\epsilon$의 숫자 $c$로 적는 것은 coordinate에 의존하며, 실제로 coordinate를 $\u'=\lambda\u$, $\v'=\mu\v$로 바꾸면 같은 deformation이 $\u'\v'=\lambda\mu c\epsilon$으로 적히게 된다. 이 때, 이 변화는 $\partial_{\u}\otimes\partial_{\v}=\lambda\mu(\partial_{\u'}\otimes\partial_{\v'})$와 정확히 상쇄되므로, deformation $\u\v=c\epsilon$에 $c(\partial_{\u}\otimes\partial_{\v})$를 대응시키면 coordinate에 의존하지 않는 isomorphism

$$T_p^1\cong T_{p'}\widetilde{C}\otimes T_{p''}\widetilde{C}$$

를 얻는다. 일반적인 coordinate $\u'=\u\alpha(\u)$, $\v'=\v\beta(\v)$에서도 [\[스킴\] §변형이론과 여접 복합체, ⁋예시 6](/ko/math/scheme_theory/deformation_theory#ex6)에 의하여 first-order deformation은 상수항만으로 결정되므로 $\lambda=\alpha(0)$, $\mu=\beta(0)$만 남아 마찬가지이다. 즉 node를 펴는 크기는 두 branch의 tangent vector의 tensor product로 잴 수 있다. 이 isomorphism은 canonical하므로 boundary의 점마다 얻은 것들이 서로 붙어 boundary 성분 $\{\t_p=0\}$의 normal line bundle을 주며, 두 branch를 맞바꾸어도 $\u\v=\t_p$의 $\t_p$는 바뀌지 않으므로 이는 두 branch의 순서에도 의존하지 않는다.

마지막으로 automorphism이 smoothing 방향에 작용하는 예를 하나 보자. $(C,p_\bullet)$의 automorphism $\sigma$는 first-order deformation $(X,\iota)$를 $(X,\sigma\circ\iota)$로 보내는 것으로 $T^1(C,p_\bullet)$에 작용하며, $\sigma$가 $T^1$의 한 원소를 고정하는 것은 그 원소가 나타내는 deformation으로 $\sigma$가 연장되는 것과 같다.

::: 예시 11
두 elliptic curve $E_1$, $E_2$의 원점 $p'$, $p''$을 하나의 node $p$로 붙인 genus $2$ 곡선 $C$를 생각하고, $\mathbb{K}$의 characteristic은 $2$가 아니라 하자. Elliptic curve의 tangent sheaf는 trivial하므로 [명제 4](#prop4){: data-lid="6wm2c" }에 의하여 $\mathcal{T}_{C/\mathbb{K}}$는 $\mathcal{O}_{E_1}(-p')\oplus\mathcal{O}_{E_2}(-p'')$의 pushforward이고, 각 항은 $h^0=0$, $h^1=1$이다. 따라서 [정리 5](#thm5){: data-lid="qqbud" }에 의하여 $T^0(C)=0$이고, $T^1(C)$는 $(E_1,p')$와 $(E_2,p'')$를 각각 변형하는 $2$차원과 node를 펴는 $T_p^1$의 $1$차원으로 이루어진다.

$E_1$의 inversion $[-1]$과 $E_2$의 항등사상을 붙인 automorphism을 $\sigma_1$이라 하자. $(E_1,p')$의 deformation은 $p'$을 원점으로 하는 group scheme이므로 $[-1]$이 그 위로 연장되고, 따라서 $\sigma_1$은 앞의 $2$차원에 trivial하게 작용한다. 반면 $[-1]$은 $T_{p'}E_1$에 $-1$로 작용하므로 $\sigma_1$은 $T_p^1\cong T_{p'}E_1\otimes T_{p''}E_2$에 $-1$로 작용한다. 즉 $\sigma_1=\operatorname{diag}(1,1,-1)$이고, $E_2$ 쪽의 inversion $\sigma_2$도 마찬가지이므로 $\sigma_1\sigma_2$는 $T^1(C)$에 trivial하게 작용한다.
:::

이 예시에서 $T^0(C)=0$이지만, $\sigma_1$이 node를 $\epsilon$만큼 펴는 deformation과 $-\epsilon$만큼 펴는 deformation을 서로 바꾸므로 versal base의 서로 다른 방향이 같은 곡선을 준다. [정리 9](#thm9){: data-lid="o3ctj" }의 $\mathfrak{M}_{2,0}$은 이 중복을 stabilizer $\Aut(C)$로 기억한다.

---

**참고문헌**

**[HKK+]** K. Hori, S. Katz, A. Klemm, R. Pandharipande, R. Thomas, C. Vafa, R. Vakil, E. Zaslow, *Mirror Symmetry*, Clay Mathematics Monographs **1**, AMS, 2003.
