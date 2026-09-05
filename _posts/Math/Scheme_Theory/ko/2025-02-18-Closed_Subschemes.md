---
title: "닫힌 부분스킴"
description: "아핀 스킴의 닫힌 부분스킴을 정의할 때, 위상적인 제한으로 얻는 층과 몫환으로부터 얻는 층이 어떻게 다른지 살펴본다. 아핀 직선의 구체적 예시를 통해 두 구조층의 차이를 확인한다."
excerpt: "Ideal sheaf로부터 정의되는 closed subscheme과 vanishing scheme"

categories: [Math / Scheme Theory]
permalink: /ko/math/scheme_theory/closed_subschemes
sidebar: 
    nav: "scheme_theory-ko"

date: 2025-02-18
weight: 10
---

[§스킴, ⁋보조정리 2](/ko/math/scheme_theory/schemes#lem2)에서 우리는 affine scheme $\Spec A$에 대하여, 임의의 원소 $f$가 open affine subscheme $D(f)\cong \Spec A_f$를 정의하는 것을 살펴보았으며, 특히 이 두 structure sheaf를 비교하기 위해 우리는 $\epsilon: A \rightarrow A_f$로부터 얻어지는

$$(\Spec\epsilon)^\sharp: \mathcal{O}_{\Spec A} \rightarrow (\Spec \epsilon)_\ast \mathcal{O}_{\Spec A_f}$$

에 [\[위상수학\] §층, ⁋보조정리 11](/ko/math/topology/sheaves#lem11)을 적용하여

$$(\Spec\epsilon \vert^{D(f)})^\sharp: \mathcal{O}_{D(f)} \rightarrow (\Spec\epsilon\vert^{D(f)})_\ast \mathcal{O}_{\Spec A_f}$$

을 얻고, $\Spec A_f$가 $\Spec A$의 열린집합 $D(f)$와 isomorphic하다는 사실로부터 이것이 isomorphism이라는 사실을 얻을 수 있었다.

한편 [§스펙트럼, ⁋명제 9](/ko/math/scheme_theory/spectrums#prop9)의 둘째 결과에 의해, affine scheme $\Spec A$와 $A$의 ideal $\mathfrak{a}$가 주어지면 $\Spec$ functor를 통해 

$$\Spec\pi: \Spec A/\mathfrak{a}\rightarrow \Spec A$$

가 주어지고, 이 때 $\Spec\pi$는 injective이며 그 image는 닫힌집합 $Z(\mathfrak{a})$가 된다는 것을 안다. 이 경우에도 위에서와 마찬가지로 canonical decomposition

$$\Spec A/\mathfrak{a}\overset{\Spec\pi\vert^{Z(\mathfrak{a})}}{\longrightarrow} Z(\mathfrak{a}) \overset{\iota}{\longrightarrow}\Spec A$$

을 생각한 후,

$$(\Spec\pi)^\sharp: \mathcal{O}_{\Spec A} \rightarrow (\Spec\pi)_\ast \mathcal{O}_{\Spec A/\mathfrak{a}}$$

로부터 $Z(\mathfrak{a})$에서 정의된 sheaf들의 morphism

$$\iota^{-1} \mathcal{O}_{\Spec A} \rightarrow (\Spec\pi\vert^{Z(\mathfrak{a})})_\ast \mathcal{O}_{\Spec A/\mathfrak{a}}$$

를 만들 수 있지만, 우리는 $Z(\mathfrak{a})$에 scheme structure를 정의하지도 않았고, 따라서 $\iota^{-1}\mathcal{O}_{\Spec A}$와 $\mathcal{O}_{Z(\mathfrak{a})}$ 사이의 관계를 모를 뿐더러, 이것이 isomorphism이 된다는 보장도 없다. 실제로 이는 isomorphism이 되지 않을 가능성이 훨씬 큰데, $\iota^{-1}\mathcal{O}_{\Spec A}$는 $\Spec A$의 structure sheaf에서 닫힌집합 $Z(\mathfrak{a})$에 대한 위상적인 데이터만을 사용하여 정의된 것이지만, $(\Spec\pi)_\ast\mathcal{O}_{\Spec A/\mathfrak{a}}$는 ring $A/\mathfrak{a}$에 대한 대수적인 정보도 가지고 있기 때문이다. 


::: 예시 1
예를 들어 field $\mathbb{K}$를 고정하고, affine $1$-line $\mathbb{A}_\mathbb{K}^1=\Spec \mathbb{K}[\x]$을 생각하자. 그럼 다음의 canonical surjection

$$\pi_1:\mathbb{K}[\x] \rightarrow \mathbb{K}[\x]/(\x)\cong \mathbb{K},\qquad \pi_2:\mathbb{K}[\x] \rightarrow \mathbb{K}[\x]/(\x^2)$$

들이 존재하며, 구체적으로 $\pi_1$과 $\pi_2$는 각각 $\x\mapsto 0+(\x)$와 $\x\mapsto \x+(\x^2)$을 통해 정의된다. 

한편 $\mathbb{K}[\x]/(\x)\cong \mathbb{K}$이므로 $\Spec \mathbb{K}[\x]/(\x)$는 한 점 $(0)$만을 가진다. 마찬가지로 $\Spec \mathbb{K}[\x]/(\x^2)$ 또한 한 점만을 가진다. 이는 $\mathbb{K}[\x]/(\x^2)$의 prime ideal과 $\x^2$을 포함하는 $\mathbb{K}[\x]$의 prime ideal 사이의 일대일대응이 존재하고, $\mathbb{K}[\x]$는 principal ideal domain이므로, $\mathbb{K}[\x]$의 prime ideal을 $(p(\x))$라 쓴다면 이 ideal이 $\x^2$을 포함하기 위해서는 $p(\x)$가 $\x^2$을 나눠야 하기 때문에 반드시 $p(\x)=\x$여야 함을 안다. 

따라서 이들이 정의하는 scheme morphism

$$\Spec\pi_1:\Spec \mathbb{K}[\x]/(\x) \rightarrow \Spec \mathbb{K}[\x],\qquad \Spec\pi_2:\Spec \mathbb{K}[\x]/(\x^2) \rightarrow \Spec \mathbb{K}[\x]$$

을 생각하면, 연속함수로서 $\Spec\pi_1$은 $\Spec \mathbb{K}[\x]/(\x)$의 유일한 한 점 $(0)$을 $\Spec \mathbb{K}[\x]$의 한 점 $(\x)$으로, $\Spec\pi_2$는 $\Spec \mathbb{K}[\x]/(\x^2)$의 유일한 한 점 $(\x)$를 $\Spec \mathbb{K}[\x]$의 한 점 $(\x)$으로 보내는 것을 안다. 즉 연속함수로서 이들은 같은 함수를 정의하지만, 물론 $\Spec \mathbb{K}[\x]/(\x)$와 $\Spec \mathbb{K}[\x]/(\x^2)$는 scheme으로서 isomorphic하지 않다. 
:::

당연히 우리가 바라는 structure sheaf는 대수적인 정보를 포함하는 $(\Spec\pi)_\ast \mathcal{O}_{\Spec A/\mathfrak{a}}$의 형태이며, 이것이 $\iota^{-1}\mathcal{O}_{\Spec A}$와 어떠한 관계가 있는지는 이 글의 말미에서 살펴보게 된다.

## 닫힌 부분스킴

위에서 살펴본 것과 같이, closed subscheme에 대한 우리의 model은 canonical projection $\pi: A \rightarrow A/\mathfrak{a}$와, 이로부터 나오는 scheme morphism

$$(\Spec \pi, (\Spec\pi)^\sharp): \Spec A/\mathfrak{a} \rightarrow\Spec A$$

이다. 이 때 $\Spec\pi$는 $\Spec A$의 닫힌집합과 $\Spec A/\mathfrak{a}$ 사이의 homeomorphism을 주는 injective continuous map이고, $\Spec\pi^\sharp: \mathcal{O}_{\Spec A} \rightarrow (\Spec\pi)_\ast \mathcal{O}_{\Spec A/\mathfrak{a}}$는 [§아핀스킴, ⁋명제 9](/ko/math/scheme_theory/affine_schemes#prop9)에서 얻어진다.

한편, ring homomorphism $\pi: A \rightarrow A/\mathfrak{a}$에서 가장 중요한 성질은 $\pi$가 surjective라는 것이며, 실제로 임의의 surjective ring homomorphism $\phi: A \rightarrow B$가 주어지면 first isomorphism theorem에 의하여

$$B=\im\phi\cong A/\ker\phi$$

이므로 이 성질이 $\pi$를 정확하게 characterize한다. 한편 [\[가환대수학\] §국소화의 성질들, ⁋명제 4](/ko/math/commutative_algebra/properties_of_localization#prop4)를 생각하면, $\pi$의 surjectivity는 임의의 prime ideal $\mathfrak{p}$에서의 localization $\pi_\mathfrak{p}: A_\mathfrak{p} \rightarrow (A/\mathfrak{a})_{\mathfrak{p}}$이 surjective인지를 살펴보아 확인할 수 있으며 이는 기하적으로는 affine scheme $\Spec A$에서의 임의의 점 $\mathfrak{p}$에서의 stalk을 살펴보는 것과 같고, 따라서 [\[위상수학\] §층, ⁋명제 15](/ko/math/topology/sheaves#prop15)에 의해 $(\Spec\pi)^\sharp$이 surjective인 것과 같다. 

::: 정의 2
Scheme morphism $\iota: Z \rightarrow X$가 *closed embedding<sub>닫힌 매장</sub>*이라는 것은 $\iota$가 연속함수로서 $Z$와 $X$의 닫힌집합 사이의 homeomorphism이고, sheaf morphism $\iota^\sharp: \mathcal{O}_X \rightarrow \iota_\ast \mathcal{O}_Z$가 surjective인 것이다.

$X$로의 두 closed embedding $\iota: Z \rightarrow X$와 $\iota': Z' \rightarrow X$에 대하여 isomorphism $\theta: Z' \rightarrow Z$가 존재하여 $\iota'=\iota\circ \theta$이도록 할 수 있다면 이 둘을 서로 equivalent하다 하고, 이 equivalence class를 $X$의 *closed subscheme<sub>닫힌 부분스킴</sub>*이라 부른다.
:::

연속함수 $\iota$에 대한 조건은 자명한 것이며, $\iota^\sharp$에 대한 직관 또한 기하적인 해석이 가능한데, 그것은 $Z$의 함수들, 더 정확하게는 $\iota(Z)$의 함수들은 모두 $X$의 함수를 $Z$로 제한하여 얻어진 것이어야 한다는 것이다. 혹은, 반대로 말하면 $Z$의 임의의 함수가 주어졌을 때 이를 각 점의 근방에서 국소적으로 $X$의 함수로 확장하는 것이 가능해야 한다는 것이다. 여기서 sheaf의 전사성은 stalk에 대한 조건이므로 대역적인 확장을 뜻하지는 않는다. 가령 $X=\mathbb{P}^1$과 그 안의 두 점으로 이루어진 reduced closed subscheme $Z$를 생각하면 $\Gamma(X,\mathcal{O}_X)=\mathbb{K}$에서 $\Gamma(Z,\mathcal{O}_Z)=\mathbb{K}\times \mathbb{K}$로 가는 사상은 전사가 아니다. 한편 $\iota$가 open embedding인 경우와 대조해 볼 만하다. 이 경우 $\iota^\sharp:\mathcal{O}_X \rightarrow \iota_\ast\mathcal{O}_Z$ 자체는 isomorphism이 아니다. 가령 $X=\mathbb{A}^1_k=\Spec k[t]$와 그 열린부분 $Z=D(t)=\Spec k[t,t^{-1}]$을 생각하면 $(\iota_\ast\mathcal{O}_Z)(X)=k[t,t^{-1}]$이라 $k[t] \rightarrow k[t,t^{-1}]$은 전사가 아니다. 올바른 진술은 $\iota$가 $Z$를 열린집합으로 옮기므로 $\iota^{-1}\mathcal{O}_X\cong\mathcal{O}_Z$, 곧 $\iota(Z)$의 각 점에서의 stalk 사이에 isomorphism이 유도된다는 것이다. 

이 정의는 자연스러운 것이지만, 우리가 앞선 글에서 정의한 scheme morphism의 성질들과는 약간 결이 다르다. 따라서 우리는 이와 동치인 다음 조건을 살펴본다. 

::: 명제 3
Scheme morphism $\varphi: X \rightarrow Y$에 대하여 다음 두 조건이 동치이다.

1. $\varphi$가 closed embedding이다.
2. $\varphi$가 affine morphism이고, $Y$의 임의의 affine open subset $V\cong \Spec B$가 주어질 때마다, 그 preimage $\varphi^{-1}(V)\cong \Spec A$에 대하여 $B \rightarrow A$가 surjective이다. 
:::
::: 증명
우선 둘째 조건을 가정하고 $\varphi$가 closed embedding임을 보이자. $Y$를 affine open subset들 $\{V_i=\Spec B_i\}$로 덮으면, 가정에 의하여 $\varphi^{-1}(V_i)\cong \Spec A_i$이며 이에 대응하는 $\beta_i: B_i \rightarrow A_i$가 surjective이다. 그럼 first isomorphism theorem에 의하여 $\mathfrak{b}_i=\ker\beta_i$라 둘 때 $A_i\cong B_i/\mathfrak{b}_i$이고, 따라서 $\varphi$를 $\varphi^{-1}(V_i)$로 제한한 것은 canonical projection $\pi: B_i \rightarrow B_i/\mathfrak{b}_i$가 정의하는 $\Spec\pi$이다.

이제 [§스펙트럼, ⁋명제 9](/ko/math/scheme_theory/spectrums#prop9)에 의하여 $\Spec\pi$는 injective이고 그 image는 닫힌집합 $Z(\mathfrak{b}_i)$이며, $\Spec\pi$는 이 image 위로의 homeomorphism이다. 우선 이로부터 $\varphi$가 injective인 것을 안다. 실제로 $\varphi(x)=\varphi(x')$이라면 이 점을 포함하는 $V_i$를 택할 때 $x,x'\in \varphi^{-1}(V_i)$이고, $\varphi$를 $\varphi^{-1}(V_i)$로 제한한 것이 injective이기 때문이다. 또 각각의 $i$에 대하여 $\varphi(X)\cap V_i=Z(\mathfrak{b}_i)$가 $V_i$의 닫힌집합이고 $\{V_i\}$가 $Y$의 open cover이므로 $\varphi(X)$는 $Y$의 닫힌집합이다. 마지막으로 $X$의 임의의 열린집합 $U$에 대하여, $\varphi$가 injective인 것으로부터

$$\varphi(U)\cap V_i=\varphi(U\cap \varphi^{-1}(V_i))$$

이고 우변은 $\varphi(X)\cap V_i$의 열린집합이므로, $\varphi(U)$는 $\varphi(X)$의 열린집합이다. 즉 $\varphi$는 $X$와 $Y$의 닫힌집합 $\varphi(X)$ 사이의 homeomorphism이다.

다음으로 $\varphi^\sharp$이 surjective인 것을 보이자. [\[위상수학\] §층, ⁋명제 15](/ko/math/topology/sheaves#prop15)에 의하여 이는 각각의 $y\in Y$에서 stalk을 확인하면 충분하다. 만일 $y\not\in \varphi(X)$라면, $\varphi(X)$가 닫힌집합이므로 $\varphi(X)$와 만나지 않는 $y$의 열린근방 $W$가 존재하고, 이 때 $(\varphi_\ast \mathcal{O}_X)(W)=\mathcal{O}_X(\emptyset)=0$이므로 $(\varphi_\ast \mathcal{O}_X)_y=0$이 되어 볼 것이 없다. 이제 $y=\varphi(x)$라 하자. $\varphi$가 image 위로의 homeomorphism이므로, $x$를 포함하는 $X$의 임의의 열린집합 $U$에 대하여 $\varphi(U)=W\cap \varphi(X)$이도록 하는 $Y$의 열린집합 $W\ni y$가 존재하고 이 때 $\varphi^{-1}(W)=U$이다. 즉 $y$의 열린근방들의 preimage들은 $x$의 열린근방들 사이에서 cofinal하며, 따라서

$$(\varphi_\ast \mathcal{O}_X)_y=\varinjlim_{W\ni y}\mathcal{O}_X(\varphi^{-1}(W))\cong \mathcal{O}_{X,x}$$

이다. 이제 $y\in V_i$인 $i$를 택하고 $y$에 해당하는 $B_i$의 prime ideal을 $\mathfrak{q}$, $x$에 해당하는 $A_i$의 prime ideal을 $\mathfrak{p}=\mathfrak{q}/\mathfrak{b}_i$라 하면, [§아핀스킴, ⁋보조정리 8](/ko/math/scheme_theory/affine_schemes#lem8)에 의하여 $y$에서의 stalk 사이의 morphism은 $\beta_i$의 localization

$$(B_i)_\mathfrak{q} \rightarrow (A_i)_\mathfrak{p}\cong (B_i/\mathfrak{b}_i)_\mathfrak{q}$$

이다. 그런데 localization은 exact functor이므로 ([\[가환대수학\] §국소화의 성질들, ⁋명제 2](/ko/math/commutative_algebra/properties_of_localization#prop2)) 이 morphism은 surjective이고, 따라서 $\varphi^\sharp$은 surjective이다. 즉 $\varphi$는 closed embedding이다.

반대 방향은 형식적이지 않다. $\varphi$가 closed embedding이라 가정하고, $Y$의 affine open subset $V=\Spec B$를 고정한 후 $W=\varphi^{-1}(V)$라 쓰자. 앞선 논증에서와 마찬가지로 $\varphi$가 image 위로의 homeomorphism이라는 사실로부터, 임의의 $\mathfrak{q}=\varphi(x)\in \varphi(X)\cap V$에 대하여 $(\varphi_\ast \mathcal{O}_X)_\mathfrak{q}\cong \mathcal{O}_{X,x}$이고 $\varphi(X)$ 바깥의 점에서는 $(\varphi_\ast \mathcal{O}_X)_\mathfrak{q}=0$이다. 즉 우리는 $\varphi_\ast \mathcal{O}_X$의 stalk들을 알고 있다. 그러나 이것만으로는 $\varphi_\ast \mathcal{O}_X$가 $V$의 열린집합들 위에서 어떤 section을 갖는지 알 수 없으며, 특히 $W$가 affine scheme인지도 알 수 없다. 이를 위해 필요한 것은 closed embedding $\varphi$에 대하여 $\varphi_\ast \mathcal{O}_X$와 ideal sheaf $\ker\varphi^\sharp$이 *quasi-coherent*하다는 사실, 즉 $Y$의 affine open subset $\Spec B$와 임의의 $f\in B$에 대하여 canonical한 morphism

$$\left((\varphi_\ast \mathcal{O}_X)(\Spec B)\right)_f \rightarrow (\varphi_\ast \mathcal{O}_X)(D(f))$$

이 isomorphism이라는 사실이다. 이는 [명제 6](#prop6)에서 ideal들에 요구했던 localization 조건과 정확히 같은 형태의 조건이지만, 지금은 $\varphi$가 affine morphism인지조차 모르는 상황이므로 이를 우리가 가진 도구만으로 얻을 수는 없다. 따라서 우리는 이 사실을 증명 없이 주장하기만 하고, 나머지 논증은 우리가 이미 가진 도구들로 완결하기로 한다. 이 사실은 [§준연접층, ⁋명제 18](/ko/math/scheme_theory/quasicoherent_sheaves#prop18)이 $\varphi_\ast \mathcal{O}_X$의 quasi-coherence로 증명한다.

$C=(\varphi_\ast \mathcal{O}_X)(V)=\Gamma(W, \mathcal{O}_W)$라 두고 $\beta=\varphi^\sharp(V): B \rightarrow C$라 하자. 그럼 $D(f)$들이 $V$의 base를 이루므로 [§아핀스킴, ⁋보조정리 8](/ko/math/scheme_theory/affine_schemes#lem8)의 논증을 그대로 반복하여, 위의 사실로부터 임의의 $\mathfrak{q}\in V$에 대하여

$$(\varphi_\ast \mathcal{O}_X)_\mathfrak{q}\cong C_\mathfrak{q}$$

를 얻는다. 여기에서 $C_\mathfrak{q}$는 $B$-module $C$를 $\mathfrak{q}$에서 localization한 것이고, 이 isomorphism은 restriction map들로부터 유도된 것이다.

첫째로 $\beta$는 surjective이다. 실제로 $\varphi^\sharp$이 surjective이므로 [\[위상수학\] §층, ⁋명제 15](/ko/math/topology/sheaves#prop15)에 의하여 각각의 $\mathfrak{q}$에서 stalk 사이의 morphism $B_\mathfrak{q} \rightarrow C_\mathfrak{q}$가 surjective이고, 이는 $B$-module homomorphism $\beta$의 localization이므로 [\[가환대수학\] §국소화의 성질들, ⁋명제 4](/ko/math/commutative_algebra/properties_of_localization#prop4)에 의하여 $\beta$가 surjective이다. 따라서 $\mathfrak{b}=\ker\beta$라 하면 $C\cong B/\mathfrak{b}$이다.

둘째로 $W$는 affine scheme이다. 우선 위상적으로, $\mathfrak{q}\in V$가 $\varphi(X)$에 속하는 것은 위에서 계산한 stalk이 $0$이 아닌 것과 동치이다. $\varphi(X)$ 바깥의 점에서 stalk이 $0$인 것은 이미 보았고, $\mathfrak{q}=\varphi(x)$인 경우 stalk은 local ring $\mathcal{O}_{X,x}$이므로 $0$이 아니기 때문이다. 그런데 $(\varphi_\ast \mathcal{O}_X)_\mathfrak{q}\cong (B/\mathfrak{b})_\mathfrak{q}$이고 이것이 $0$이 아닌 것은 $\mathfrak{b}\subseteq \mathfrak{q}$인 것과 동치이므로

$$\varphi(X)\cap V=Z(\mathfrak{b})$$

이다. 이제 [§아핀스킴, ⁋정리 13](/ko/math/scheme_theory/affine_schemes#thm13)의 adjunction을 항등사상 $C \rightarrow \Gamma(W, \mathcal{O}_W)$에 적용하면 canonical한 morphism $\sigma: W \rightarrow \Spec C$를 얻고, adjunction의 naturality에 의하여 $\Spec\beta\circ \sigma=\varphi\vert_W$이다. 한편 $\Spec\beta: \Spec B/\mathfrak{b} \rightarrow \Spec B$는 $Z(\mathfrak{b})$ 위로의 homeomorphism이고 ([§스펙트럼, ⁋명제 9](/ko/math/scheme_theory/spectrums#prop9)), $\varphi\vert_W$ 또한 $\varphi(X)\cap V=Z(\mathfrak{b})$ 위로의 homeomorphism이므로 $\sigma$는 homeomorphism이다. 또 임의의 $x\in W$와 $\mathfrak{q}=\varphi(x)$에 대하여 $\sigma$가 stalk에서 유도하는 morphism은 [§아핀스킴, ⁋보조정리 8](/ko/math/scheme_theory/affine_schemes#lem8)에 의하여 $C_\mathfrak{q} \rightarrow \mathcal{O}_{W,x}$이며, 이는 restriction map들로부터 유도된 morphism, 곧 위에서 얻은 isomorphism $C_\mathfrak{q}\cong (\varphi_\ast \mathcal{O}_X)_\mathfrak{q}\cong \mathcal{O}_{W,x}$과 같은 것이다. 따라서 $\sigma$는 homeomorphism이면서 모든 stalk에서 isomorphism이므로 locally ringed space들의 isomorphism이다.

이상에서 $W\cong \Spec C=\Spec B/\mathfrak{b}$는 affine scheme이고 $B \rightarrow C$는 surjective이다. $V$는 $Y$의 임의의 affine open subset이었으므로 $\varphi$는 affine morphism이며 둘째 조건이 성립한다.
:::

그럼 임의의 closed embedding은 국소적으로는 항상 위에서 살펴본 것과 같이 적당한 $\pi: A \rightarrow A/\mathfrak{a}$로부터 오는 것으로 생각할 수 있다. 특히 $Y$가 affine scheme $\Spec B$라 하면 위의 동치에 의해 $Y$로의 임의의 closed embedding $\varphi: X \rightarrow Y$는 정확하게 $B \rightarrow B/\mathfrak{b}$에 대응되는 것을 안다. 

## 닫힌 매장의 성질들

[명제 3](#prop3)에 의하여 임의의 closed embedding은 항상 affine-local on target이고, closed embedding은 합성에 대해서도 닫혀있다는 것을 안다. 뿐만 아니라 다음이 성립한다.

::: 명제 4
임의의 closed embedding은 항상 finite morphism이다.
:::
::: 증명
Closed embedding $\varphi: X \rightarrow Y$가 주어졌다 하자. [명제 3](#prop3)에 의하여 $\varphi$는 affine morphism이고, $Y$의 임의의 affine open subset $V\cong \Spec B$에 대하여 $\varphi^{-1}(V)\cong\Spec A$이며 이에 대응되는 ring homomorphism $\beta: B \rightarrow A$는 surjective이다. 그럼 임의의 $a\in A$는 적당한 $b\in B$에 대하여 $a=\beta(b)=b\cdot 1$이므로 $A$는 $B$-module로서 $1$에 의해 생성되고, 따라서 $\beta$는 finite ring homomorphism이다. ([\[가환대수학\] §정수적 확장, ⁋정의 3](/ko/math/commutative_algebra/integral_extension#def3)의 넷째 조건) 이제 [§스킴 사상의 성질들, ⁋정의 10](/ko/math/scheme_theory/properties_of_scheme_morphisms#def10)에 의하여 $\varphi$는 finite morphism이다. 
:::

[§스킴 사상의 성질들, ⁋예시 16](/ko/math/scheme_theory/properties_of_scheme_morphisms#ex16)에서 만든 (quasi-)finite morphism의 기하학적 직관에 비추어볼 때, 적어도 closed embedding은 항상 quasi-finite이어야 하는 것이 자명하고, 여기에서 더 나아가 finite이기도 하다는 기하적인 해석이 가능하다. 

::: 정의 5
임의의 scheme $Z$에 대하여, $\mathcal{O}_Z$의 subsheaf $\mathcal{I}$ 가운데 각각의 열린집합 $U$에서 $\mathcal{I}(U)$가 $\mathcal{O}_Z(U)$의 ideal을 이루는 것을 $Z$의 *ideal sheaf*라 부른다. 특별히 closed embedding $\iota: Z \rightarrow X$에 대하여, $\mathcal{O}_X$의 subsheaf $\ker\iota^\sharp$를 $\iota$에 의해 정의되는 ideal sheaf라 부르고, 이를 $\mathcal{I}_{Z/X}$로 표기한다. 
:::

즉, 다음의 exact seqeunce

$$0 \rightarrow \mathcal{I}_{Z/X} \rightarrow \mathcal{O}_X \rightarrow \iota_\ast \mathcal{O}_Z \rightarrow 0$$

이 존재한다. 따라서 $X$의 임의의 affine open subset $U=\Spec A$에서는

$$0 \rightarrow \mathcal{I}_{Z/X}(U) \rightarrow \mathcal{O}_X(U)\cong A \rightarrow \iota_\ast \mathcal{O}_Z(U) \rightarrow 0$$

이 되므로, $\mathcal{I}_{Z/X}(U)$는 $A$의 ideal이 되어 이 이름이 적절하다 할 수 있다. 

우리는 [명제 3](#prop3) 직후에 임의의 affine scheme $Y=\Spec B$의 closed subscheme은 정확하게 $B$의 ideal에 대응되는 것을 살펴보았다. 한편 임의의 scheme은 affine scheme을 붙여서 만들어지므로, 이러한 affine scheme들마다 ideal들이 정의되고, 이들이 적당한 gluing condition을 만족한다면 이를 통해 원래 scheme의 closed subscheme이 정의될 것이다. 

::: 명제 6
Scheme $X$의 임의의 affine open subset $\Spec A$마다, ideal $\mathcal{I}(A)\subseteq A$가 주어져있다고 하자. 만일 각각의 $f\in A$에 대하여, $A \rightarrow A_f$에 의해 isomorphism $\mathcal{I}(A_f)\cong \mathcal{I}(A)_f$가 유도된다면, 이들 데이터는 $X$의 유일한 closed subscheme $Z\hookrightarrow X$를 유도한다. 
:::
::: 증명
우선 $X$를 affine open subset들 $\{\Spec A_i\}$들로 덮자. 그럼 우리가 보여야 할 것은 임의의 $i,j$에 대하여, $\Spec A_i$에서 ideal $\mathcal{I}(A_i)$에 의해 정의되는 closed subscheme과 $\Spec A_j$에서 ideal $\mathcal{I}(A_j)$에 의해 정의되는 closed subscheme이 $\Spec A_i$와 $\Spec A_j$의 교집합에서 같은 closed subscheme을 정의한다는 것이다. 


우선 [§스킴의 위상구조, ⁋보조정리 11](/ko/math/scheme_theory/topology_of_schemes#lem11)로부터 우리는 $\Spec A_i$와 $\Spec A_j$의 교집합을 principal open subset들 

$$\Spec (A_i)_{f_i}\cong\Spec (A_j)_{f_j}$$

들로 덮을 수 있다. 이제 $\Spec A_i$에서 $\mathcal{I}(A_i)$가 정의하는 closed subscheme을 $D(f_i)\cong\Spec (A_i)_{f_i}$로 제한하면 이는 ideal $\mathcal{I}(A_i)_{f_i}$가 정의하는 closed subscheme이고, 주어진 가정에 의해 $\mathcal{I}(A_i)_{f_i}\cong \mathcal{I}((A_i)_{f_i})$이다. 여기에서 $\Spec (A_i)_{f_i}$와 $\Spec (A_j)_{f_j}$는 $X$의 <em-ko>같은</em-ko> 열린집합이므로 이 isomorphism을 통해 $\mathcal{I}((A_i)_{f_i})$와 $\mathcal{I}((A_j)_{f_j})$는 같은 ideal을 지칭하며, 따라서 두 closed subscheme은 이 열린집합 위에서 일치한다.

이렇게 얻어진 국소적인 closed subscheme들은 잘 붙여진다. 실제로 서로 겹치는 두 조각은 위의 논증에 의하여 겹침을 덮는 principal open subset들 위에서 일치하고, 그 위에서의 identification은 모두 restriction map으로부터 오는 것이므로 겹침 위에서 하나의 사상으로 붙으며 ([\[위상수학\] §층, ⁋정의 1](/ko/math/topology/sheaves#def1)), 따라서 cocycle condition 또한 자동으로 성립한다. 그럼 [§스킴, ⁋보조정리 9](/ko/math/scheme_theory/schemes#lem9)에 의하여 이들은 하나의 scheme $Z$와 closed embedding $Z \rightarrow X$로 붙는다. 유일성은 [명제 3](#prop3)에 의하여 affine open subset 위의 closed subscheme이 그 위의 ideal에 의해 완전히 결정되기 때문이다. 즉 주어진 데이터를 실현하는 두 closed subscheme은 $X$의 affine open covering의 각 조각 위에서 같으며, 따라서 서로 equivalent하다. 
:::

이제 임의의 scheme $X$와 global section $s\in \Gamma(X, \mathcal{O}_X)$가 주어졌다 하자. 그럼 각각의 affine cover $U\cong\Spec A$에 대하여, $s\vert_U$는 $A$의 ideal $\mathcal{I}(A)=(s\vert_U)$를 정의하며 이렇게 정의된 $\mathcal{I}(A)$들은 $(s\vert_U)A_f=(s\vert_{D(f)})$이므로 [명제 6](#prop6)의 조건을 만족한다.

::: 정의 7
Scheme $X$와 $X$의 global section $s\in \Gamma(X, \mathcal{O}_X)$에 대하여, 위와 같이 정의된 scheme $Z(s)$를 $s$의 *vanishing scheme<sub>영점 스킴</sub>*이라 부른다.
:::

더 일반적으로, global section들의 집합 $S$에 대하여 $Z(S)$를 어떻게 정의해야 하는지도 자명하며, 따라서 특별히 $X=\Spec A$이고 $S=\mathfrak{a}$가 $A$의 ideal인 경우 $Z(\mathfrak{a})$를 어떻게 정의해야 하는지도 자명하며, 이는 affine scheme $\Spec A/\mathfrak{a}$의 structure sheaf를 $\Spec\pi$를 통해 닫힌집합 $Z(\mathfrak{a})$에 옮겨준 것이다. 앞으로 $Z(\mathfrak{a})$는 항상 이러한 scheme structure가 주어져 있는 것으로 생각한다.

::: 정의 8
Scheme morphism $\varphi: X \rightarrow Y$가 *locally closed embedding<sub>국소 닫힌 매장</sub>*이라는 것은 $Y$의 적당한 open subscheme $\iota:Z\hookrightarrow Y$가 존재하여, 다음의 canonical decomposition

$$X\overset{\varphi\vert^Z}{\longrightarrow}Z\overset{\iota}{\longrightarrow} Y$$

을 통해 $\varphi\vert^Z$가 closed embedding인 것이다. 
:::

그럼 임의의 locally closed embedding은 항상 locally of finite type이다. 이를 확인하기 위해 $Y$의 affine open subset $V=\Spec B$를 고정하자. 우선 $Z\cap V$는 $\Spec B$의 principal open subset $D(f)\cong \Spec B_f$들로 덮이고 ([§스펙트럼, ⁋보조정리 11](/ko/math/scheme_theory/spectrums#lem11)), $B \rightarrow B_f$는 $1/f$ 하나를 추가한 것이므로 finite type이다. 또 $\varphi\vert^Z$가 closed embedding이므로 [명제 3](#prop3)에 의하여 각각의 $D(f)$의 preimage는 affine이고 그 coordinate ring은 $B_f$의 quotient이므로, 합성 $B \rightarrow B_f \rightarrow B_f/\mathfrak{b}$ 또한 finite type이다. 즉 $\varphi^{-1}(V)$는 $B \rightarrow \mathcal{O}_X(-)$가 finite type인 affine open subset들로 덮이며, 따라서 [§스킴 사상의 성질들, ⁋보조정리 13](/ko/math/scheme_theory/properties_of_scheme_morphisms#lem13)에 의하여 $\varphi^{-1}(V)$의 임의의 affine open subset에 대해서도 같은 결론을 얻는다. 

## 스킴 사상의 상

이제 우리는 scheme morphism의 image를 정의한다. 당연히 임의의 scheme morphism $\varphi: X \rightarrow Y$가 주어졌을 때, 우리는 그 image $\im\varphi$ 또한 scheme 구조가 주어지기를 바랄 것이다. 그러나 위상공간 $Y$의 부분집합으로서 $\im\varphi$는 열린집합도, 닫힌집합도 아닐 수 있으므로 $Y$의 structure sheaf를 이용하여 $\im\varphi$에 structure sheaf를 정의하는 것은 요원해보인다. 

이에 대한 해결책은 $\varphi$의 image를 포함하는 closed subscheme 중 가장 작은 것을 $\varphi$의 *scheme-theoretic image*로 정의하는 것이다. 이를 위해서는 우선 $X$의 closed subscheme이 다른 closed subscheme보다 작다는 것이 무엇인지를 살펴보아야 한다.

::: 보조정리 9
두 closed embedding $\iota_1: Z_1 \rightarrow X$, $\iota_2: Z_2 \rightarrow X$가 주어졌다 하자. 그럼 적당한 scheme morphism $\varphi: Z_1 \rightarrow Z_2$가 존재하여 $\iota_1=\iota_2\circ\varphi$를 만족하는 것은 $\mathcal{I}_{Z_2/X}\subseteq \mathcal{I}_{Z_1/X}$인 것과 동치이다. 이 경우 $\varphi$는 closed embedding이 된다. 
:::

::: 증명
우선 $\iota_1=\iota_2\circ\varphi$를 만족하는 $\varphi$가 존재한다 하자. 그럼 $\iota_1^\sharp$은 다음의 합성

$$\mathcal{O}_X\overset{\iota_2^\sharp}{\longrightarrow}(\iota_2)_\ast \mathcal{O}_{Z_2}\overset{(\iota_2)_\ast \varphi^\sharp}{\longrightarrow}(\iota_2)_\ast \varphi_\ast \mathcal{O}_{Z_1}=(\iota_1)_\ast \mathcal{O}_{Z_1}$$

이므로 $\ker\iota_2^\sharp\subseteq \ker\iota_1^\sharp$이고, 곧 [정의 5](#def5)에 의하여 $\mathcal{I}_{Z_2/X}\subseteq \mathcal{I}_{Z_1/X}$이다. 

거꾸로 $\mathcal{I}_{Z_2/X}\subseteq \mathcal{I}_{Z_1/X}$이라 가정하자. $X$의 임의의 affine open subset $U=\Spec A$를 택하면 [명제 3](#prop3)에 의하여 $\iota_k^{-1}(U)$는 affine open subset이고, [정의 5](#def5) 직후의 exact sequence로부터

$$\iota_k^{-1}(U)\cong \Spec A/\mathfrak{a}_k,\qquad \mathfrak{a}_k=\mathcal{I}_{Z_k/X}(U)$$

이며 이 때 $\iota_k$의 $\iota_k^{-1}(U)$로의 restriction은 canonical projection $A \rightarrow A/\mathfrak{a}_k$에 대응된다. 가정에 의하여 $\mathfrak{a}_2\subseteq \mathfrak{a}_1$이므로 $A \rightarrow A/\mathfrak{a}_1$은 $A \rightarrow A/\mathfrak{a}_2$를 통해 유일하게 인수분해되며, 이렇게 얻어지는 $\pi_U: A/\mathfrak{a}_2 \rightarrow A/\mathfrak{a}_1$은 surjective이다. 따라서 [정의 2](#def2) 직전의 논의에 의하여 $\varphi_U=\Spec\pi_U: \iota_1^{-1}(U) \rightarrow \iota_2^{-1}(U)$는 closed embedding이고, 구성에 의하여 $\iota_1$의 $\iota_1^{-1}(U)$로의 restriction은 $\iota_2$의 restriction과 $\varphi_U$의 합성이다. 

이제 $X$의 두 affine open subset $U=\Spec A$, $U'$에 대하여 $\varphi_U$와 $\varphi_{U'}$이 교집합 위에서 일치함을 보이면 된다. [§스킴의 위상구조, ⁋보조정리 11](/ko/math/scheme_theory/topology_of_schemes#lem11)에 의하여 $U\cap U'$을 $U$와 $U'$ 모두에서 principal open set인 열린집합들로 덮을 수 있고, localization이 exact functor이므로 ([\[가환대수학\] §국소화의 성질들, ⁋명제 2](/ko/math/commutative_algebra/properties_of_localization#prop2)) 이러한 $D(f)\cong \Spec A_f$ 위에서 $\mathcal{I}_{Z_k/X}(D(f))=\mathfrak{a}_kA_f$이다. 따라서 $\varphi_U$와 $\varphi_{U'}$은 모두 $D(f)$ 위에서 $\mathfrak{a}_2A_f\subseteq \mathfrak{a}_1A_f$가 유도하는 canonical projection $A_f/\mathfrak{a}_2A_f \rightarrow A_f/\mathfrak{a}_1A_f$에 대응되어 서로 같다. 그럼 [§스킴 사이의 사상, ⁋명제 1](/ko/math/scheme_theory/morphism_of_schemes#prop1)에 의하여 이들은 scheme morphism $\varphi: Z_1 \rightarrow Z_2$로 붙고, 구성에 의하여 $\iota_1=\iota_2\circ\varphi$이다. 

마지막으로 $\iota_1=\iota_2\circ\varphi$를 만족하는 <em-ko>임의의</em-ko> $\varphi$가 closed embedding임을 보이자. $X$의 affine open subset $U$에 대하여 $\varphi^{-1}(\iota_2^{-1}(U))=\iota_1^{-1}(U)$이고, $\varphi$의 이 열린집합으로의 restriction에 대응되는 ring homomorphism $A/\mathfrak{a}_2 \rightarrow A/\mathfrak{a}_1$은 $A$로부터의 두 canonical projection과 가환이어야 하므로 위의 $\pi_U$일 수밖에 없다. 그런데 $\iota_2$가 affine morphism이므로 $U$가 $X$의 affine open covering을 훑을 때 $\iota_2^{-1}(U)$들은 $Z_2$의 affine open covering을 이루고, closed embedding은 affine-local on target이므로 ([명제 3](#prop3)) $\varphi$는 closed embedding이다. 
:::

Scheme $X$의 두 closed subscheme $Z_1,Z_2$에 대하여, closed embedding $\varphi:Z_1 \rightarrow Z_2$가 존재한다면 $Z_1$이 $Z_2$보다 <em-ko>작은</em-ko> closed subscheme인 것으로 생각하자. 

::: 정의 10
임의의 scheme morphism $\varphi: X \rightarrow Y$가 주어졌다 하자. 그럼 $\varphi$의 image가 closed subscheme $\iota: Z \rightarrow Y$에 *포함된다*는 것은 다음의 합성

$$\mathcal{I}_{Z/Y} \rightarrow \mathcal{O}_Y \rightarrow \varphi_\ast \mathcal{O}_X$$

이 $0$이 되는 것이다. 이 때, $\varphi$의 image를 포함하는 $Y$의 closed subscheme 중 가장 작은 것을 $\varphi$의 *scheme-theoretic image*라 부른다.
:::

만일 위의 식에서 $Y$가 affine scheme $\Spec B$라면, $Y$의 closed subscheme은 $B$의 ideal $\mathfrak{b}$에 의해 완전하게 결정된다. 따라서 이 경우, $\varphi$의 scheme-theoretic image는 $\mathcal{O}_Y \rightarrow \varphi_\ast \mathcal{O}_X$의 kernel이 정의하는 $Y$의 closed subscheme이 될 것이다. 더 특수한 경우로 만일 $X$도 affine scheme이라면, $\mathcal{O}_Y \rightarrow \varphi_\ast \mathcal{O}_X$는 ring homomorphism $\phi$로부터 나오는 것이므로 명시적인 계산을 해 줄 수 있다.

::: 예시 11
[예시 1](#ex1)에서 살펴본 closed embedding의 예시 $\Spec\pi: \Spec \mathbb{K}[\x]/(\x^2) \rightarrow \Spec \mathbb{K}[\x]$를 약간 변형한 예시를 살펴보자. 이 예시에서는 구별을 위해 $\mathbb{K}[\x]/(\x^2)$를 $\mathbb{K}[\epsilon]/(\epsilon^2)$으로 적는다. 

우리는 [\[대수적 구조\] §대수, ⁋명제 8](/ko/math/algebraic_structures/algebras#prop8)에 의하여 $\mathbb{K}$-algebra homomorphism $\phi:\mathbb{K}[\x_1,\ldots, \x_n] \rightarrow \mathbb{K}[\epsilon]/(\epsilon^2)$는 $\x_i$의 값에 의해 완전히 결정된다는 것을 안다. 따라서 $\phi(\x_i)=a_i+b_i\epsilon$이라 하자. 만일 $0$이 아닌 $b_i$가 존재한다면 $\phi$가 surjective임을 보일 수 있고, 따라서 $\Spec\phi$는 closed embedding이며 $\Spec\phi$의 scheme-theoretic image는 $\Spec\phi$가 정의하는 closed subscheme 자기 자신이다. 구체적으로 이를 써 보면 $\Spec\phi$는 $\mathbb{K}[\epsilon]/(\epsilon^2)$의 유일한 prime ideal $(\epsilon)$을 $\Spec \mathbb{K}[\x_1,\ldots, \x_n]$의 maximal ideal

$$(\Spec\phi)((\epsilon))=\phi^{-1}((\epsilon))=(\x_1-a_1,\ldots, \x_n-a_n)$$

로 보낸다. 실제로 $\phi(\x_i-a_i)=b_i\epsilon\in(\epsilon)$이므로 $(\x_1-a_1,\ldots, \x_n-a_n)\subseteq\phi^{-1}((\epsilon))$이며, 좌변이 maximal ideal이고 우변이 proper ideal이므로 이 포함관계는 등식이 된다. 즉 연속함수로서 $\Spec\phi$는 한점공간 $\Spec \mathbb{K}[\epsilon]/(\epsilon^2)$을 $\mathbb{A}^n$의 한 점 $(a_1,\ldots, a_n)$으로 보낸다.

기하적으로 $\Spec\phi$는 $\mathbb{A}^n$의 한 점 $(a_1,\ldots, a_n)$에서의 tangent vector $(b_1,\ldots, b_n)$에 대응된다. 이는 임의의 $f\in \mathbb{K}[\x_1,\ldots, \x_n]$에 대하여

$$\phi(f)=f(a)+\left(\sum_{i=1}^nb_i\frac{\partial f}{\partial \x_i}(a)\right)\epsilon$$

이 성립하는 것, 즉 $\phi(f)$의 $\epsilon$-계수가 정확히 점 $(a_1,\ldots, a_n)$에서 벡터 $(b_1,\ldots, b_n)$ 방향으로의 방향미분이라는 것으로부터 확인할 수 있다. 더 일반적으로 $\Spec \mathbb{K}[\epsilon]/(\epsilon^2)$ 대신 $\Spec \mathbb{K}[\epsilon]/(\epsilon^k)$를 생각하면 $\phi(f)$의 $\epsilon^j$-계수들이 $f$의 $j$차 Taylor 계수를 준다. 표수가 $0$인 경우 이는 $k-1$차 derivative까지 보는 것과 같지만, 양의 표수에서는 그렇지 않다는 것에 주의해야 한다.
:::

위의 예시에서 $X$가 affine scheme이라고 가정하기는 하였지만, $\varphi^\sharp:\mathcal{O}_Y \rightarrow \varphi_\ast \mathcal{O}_X$는 어차피 scheme morphism $\varphi$가 포함하고 있는 정보이므로 여기에는 새로울 것이 없다. 차이는 $Y$를 일반적인 scheme으로 일반화할 때 나오게 되는데, $Y$의 임의의 affine open subset $V=\Spec B$가 주어질 때마다 ideal

$$\mathcal{I}(V):=\ker(\varphi^\sharp(V))\subseteq B$$

가 $V$의 closed subscheme을 정의하지만, 이들을 이어붙여 $Y$ 전체에서 정의된 단일한 closed subscheme을 만들 수 있는지는 다른 문제이기 때문이다. 물론 우리는 이를 위해 [명제 6](#prop6)을 사용할 것이며, 이 가정은 특히 $X$가 reduced scheme이거나 $\varphi$가 quasi-compact일 경우 만족된다.

::: 따름정리 12
Scheme morphism $\varphi: X \rightarrow Y$가 주어졌다 하자. 만일 $X$가 reduced이거나, $\varphi$가 quasi-compact라면 위에서 정의한 ideal sheaf $\mathcal{I}$는 [명제 6](#prop6)의 조건을 만족하고 따라서 $\mathcal{I}$는 $Y$의 closed subscheme을 정의하며 이것이 $\varphi$의 scheme-theoretic image가 된다.
:::
::: 증명
$Y$의 affine open subset $V=\Spec B$와 $f\in B$를 고정하고 $U=\varphi^{-1}(V)$, $U'=\varphi^{-1}(D(f))$이라 하자. 그럼 [명제 6](#prop6)이 요구하는 것은 canonical map $\mathcal{I}(V)_f \rightarrow \mathcal{I}(D(f))$이 isomorphism이라는 것이다. 편의상 $f$의 $\varphi^\sharp(V): B \rightarrow \mathcal{O}_X(U)$에 의한 image를 $g$라 하자. 

$\varphi$가 locally ringed space들 사이의 morphism이므로 각각의 $x\in U$에서 $\varphi^\sharp_x$는 local homomorphism이고, 따라서 $U'$은 정확히 $g$의 stalk이 $\mathcal{O}_{X,x}$의 maximal ideal에 속하지 <em-ko>않는</em-ko> 점들의 집합이다. 특히 $U$의 임의의 affine open subset $\Spec A$에 대하여 $U'\cap \Spec A=D(g\vert_{\Spec A})$이므로 $g$의 $U'$로의 restriction은 $\mathcal{O}_X(U')$의 unit이고, 따라서 [\[가환대수학\] §국소화, ⁋명제 6](/ko/math/commutative_algebra/localization#prop6)의 universal property에 의하여 restriction map $\mathcal{O}_X(U) \rightarrow \mathcal{O}_X(U')$은 canonical map

$$\alpha: \mathcal{O}_X(U)_g \rightarrow \mathcal{O}_X(U')$$

을 유도한다. 또 $\varphi^\sharp$이 sheaf morphism이라는 것으로부터 $\varphi^\sharp(D(f)): B_f \rightarrow \mathcal{O}_X(U')$은 $\varphi^\sharp(V)$의 localization $B_f \rightarrow \mathcal{O}_X(U)_g$와 $\alpha$의 합성이다. 그런데 localization은 exact functor이므로 ([\[가환대수학\] §국소화의 성질들, ⁋명제 2](/ko/math/commutative_algebra/properties_of_localization#prop2))

$$\ker\bigl(B_f \rightarrow \mathcal{O}_X(U)_g\bigr)=\ker\bigl(\varphi^\sharp(V)\bigr)_f=\mathcal{I}(V)_f$$

이고, 따라서 $\alpha$가 injective이기만 하면 $\mathcal{I}(D(f))=\ker (\varphi^\sharp(D(f)))=\mathcal{I}(V)_f$가 되어 [명제 6](#prop6)의 조건이 성립한다. 이제 두 가정 각각에서 $\alpha$가 injective임을 보인다. 

우선 $\varphi$가 quasi-compact이라 하자. 그럼 $U$는 quasi-compact이므로 유한히 많은 affine open subset $\Spec A_1,\ldots, \Spec A_n$으로 덮인다. $s\in \mathcal{O}_X(U)$가 $s\vert_{U'}=0$을 만족한다 하면, 각각의 $l$에 대하여 $s\vert_{\Spec A_l}\in A_l$의 $U'\cap \Spec A_l=D(g\vert_{\Spec A_l})$로의 restriction이 $0$이므로 적당한 $n_l$에 대하여 $(g^{n_l}s)\vert_{\Spec A_l}=0$이다. $l$이 유한개이므로 공통의 $N$을 택하면 $g^Ns$는 모든 $\Spec A_l$ 위에서 $0$이고, 따라서 [\[위상수학\] §층, ⁋정의 1](/ko/math/topology/sheaves#def1)의 첫째 조건에 의하여 $g^Ns=0$이다. 즉 $\mathcal{O}_X(U)_g$에서 $s/g^m=0$이므로 $\alpha$는 injective이다. 

이번에는 $X$가 reduced라 하자. ([§스킴의 대수구조, ⁋정의 1](/ko/math/scheme_theory/algebra_of_schemes#def1)) $s\in \mathcal{O}_X(U)$가 $s\vert_{U'}=0$을 만족한다 하고 $gs$를 생각하면, $U'$의 점에서는 $s$의 stalk이 $0$이므로 $gs$의 stalk이 $0$이고, $U'$에 속하지 않는 점 $x$에서는 $g$의 stalk이 $\mathcal{O}_{X,x}$의 maximal ideal에 속한다. 따라서 $U$의 임의의 affine open subset $\Spec A$에 대하여 $(gs)\vert_{\Spec A}$는 $A$의 모든 prime ideal에 속하고, [\[가환대수학\] §국소화의 성질들, ⁋따름정리 8](/ko/math/commutative_algebra/properties_of_localization#cor8)과 $A$가 reduced ring이라는 사실로부터 $(gs)\vert_{\Spec A}=0$이다. 그럼 다시 sheaf 조건에 의하여 $gs=0$이고, 따라서 $s/g^m=(gs)/g^{m+1}=0$이므로 $\alpha$는 injective이다. 

이상에서 [명제 6](#prop6)에 의하여 $\mathcal{I}$는 $Y$의 closed subscheme $\iota: Z \rightarrow Y$를 유일하게 유도한다. 이것이 [정의 10](#def10)의 의미에서 $\varphi$의 image를 포함한다는 것은, $Y$의 임의의 affine open subset $V$에 대하여 $\mathcal{I}_{Z/Y}(V)=\ker (\varphi^\sharp(V))$이므로 합성 $\mathcal{I}_{Z/Y}(V) \rightarrow \mathcal{O}_Y(V) \rightarrow (\varphi_\ast \mathcal{O}_X)(V)$이 $0$이 되고, affine open subset들이 $Y$의 base를 이루기 때문이다. 거꾸로 $\varphi$의 image를 포함하는 $Y$의 임의의 closed subscheme $\iota': Z' \rightarrow Y$에 대하여 같은 합성이 $0$이므로 $\mathcal{I}_{Z'/Y}(V)\subseteq \ker (\varphi^\sharp(V))=\mathcal{I}_{Z/Y}(V)$이고, 두 ideal sheaf가 모두 $\mathcal{O}_Y$의 subsheaf이므로 이로부터 $\mathcal{I}_{Z'/Y}\subseteq \mathcal{I}_{Z/Y}$를 얻는다. 따라서 [보조정리 9](#lem9)에 의하여 closed embedding $Z \rightarrow Z'$가 존재하고, 곧 $Z$는 $\varphi$의 image를 포함하는 가장 작은 closed subscheme, 즉 $\varphi$의 scheme-theoretic image이다. 
:::

위의 조건을 가정하고 $\varphi$의 image를 각각의 affine open subset에서 확인해보면 $\varphi$의 scheme-theoretic image는 $\varphi$의 (연속함수로서의) image의 closure 위에 structure sheaf가 정의된 형태임을 확인할 수 있다. 

[따름정리 12](#cor12)의 가정이 없을 경우 이러한 일은 일어나지 않는다.

::: 예시 13
Scheme $X$를 다음의 식

$$X=\coprod_{k\geq 1} \Spec \mathbb{K}[\epsilon]/(\epsilon^k)$$

으로 정의하고 $Y=\Spec \mathbb{K}[\x]$이라 하자. 이제 $X$의 각각의 component마다 $\x\mapsto \epsilon$을 통해 scheme morphism $X \rightarrow Y$를 정의할 수 있다. 그럼 [예시 11](#ex11)으로부터 우리는 $X \rightarrow Y$의 (연속함수로서의) image는 한 점 $0\in \mathbb{A}^1$인 것을 안다. 

그러나 scheme morphism $\varphi:X \rightarrow Y$의 scheme-theoretic image는 $0$이 아니다. 이를 위해 structure sheaf들 사이의 morphism $\varphi^\sharp:\mathcal{O}_Y \rightarrow \varphi_\ast \mathcal{O}_X$를 관찰하자. 그럼 $\mathcal{O}_Y$의 원소 $f$가 $\varphi^\sharp(f)=0$을 만족하기 위해서는 임의의 $k$에 대하여 $f$의 $k$차 근사식이 $0$이 되어야 하므로, 반드시 $f=0$이어야 한다. 즉, $\mathcal{I}_{Z/Y}$는 $0$이 되어야 하고 이로부터 $\varphi$의 scheme-theoretic image는 $Y$ 전체임을 안다.
:::

## 닫힌집합 위에 정의된 축소스킴구조

이 글의 서두에서 우리는 affine scheme $\Spec A$의 임의의 닫힌집합 $Z(\mathfrak{a})$ 위에 두 개의 structure sheaf $(\Spec\pi)_\ast \mathcal{O}_{\Spec A/\mathfrak{a}}$ 그리고 $\iota^{-1} \mathcal{O}_{\Spec A}$를 정의할 수 있었다. 이 중 $(\Spec\pi)_\ast \mathcal{O}_{\Spec A/ \mathfrak{a}}$를 우리는 $Z(\mathfrak{a})$ 위에 정의된 올바른 scheme 구조로 생각하기로 하였다. 이제 우리는 $\iota^{-1} \mathcal{O}_{\Spec A}$에 대해 살펴본다.

더 일반적으로 임의의 scheme $Y$와 $Y$의 닫힌집합 $X$를 생각하자. 그럼 $Y$의 임의의 affine open subset $\Spec B$에 대하여, $\Spec B$의 닫힌집합 $X\cap \Spec B$는 [§스펙트럼, ⁋정리 15](/ko/math/scheme_theory/spectrums#thm15)에 의하여 
$B$의 radical ideal $\mathfrak{b}$에 대해 $Z(\mathfrak{b})$의 꼴로 쓸 수 있다. 뿐만 아니라, $\mathfrak{b}$는 정의에 의하여 $X\cap \Spec B= Z(\mathfrak{b}')$이도록 하는 $B$의 ideal들 중 가장 큰 것이므로 [보조정리 9](#lem9)에 의하여 $X\cap \Spec B$에 줄 수 있는 closed subscheme 구조 중 가장 작은 것이다. 또 radical은 localization과 교환하므로 ($\sqrt{\mathfrak{b}}B_f=\sqrt{\mathfrak{b}B_f}$) 이들 ideal은 [명제 6](#prop6)의 조건을 만족하고, 따라서 하나의 closed subscheme으로 붙는다.

::: 정의 14
Scheme $Y$의 임의의 닫힌집합 $X$에 대하여, $X$ 위에 앞에서 정의한 scheme 구조를 준 것을 *reduced scheme structure*라 부르고 $X^\red$으로 적는다. 
:::

그럼 특히 $X=Y$인 경우, 임의의 affine subset $\Spec B$에 대하여 $\Spec B=Z(0)$이라 적으면 $\mathfrak{b}=\mathfrak{N}(B)$이 되어 $B/\mathfrak{N}(B)$은 reduced ring이 된다. 한편 위에서 살펴본 sheaf morphism

$$\iota^{-1}\mathcal{O}_{\Spec A} \rightarrow (\Spec\pi\vert^{Z(\mathfrak{a})})_\ast \mathcal{O}_{\Spec A/\mathfrak{a}}$$

은 restriction으로부터, 곧 adjunction $\iota^{-1}\dashv \iota_\ast$로부터 유도되는 canonical한 sheaf morphism이다. 단, 이를 [보조정리 9](#lem9)가 주는 scheme morphism과 혼동하지 않아야 하는데, $(Z(\mathfrak{a}),\iota^{-1}\mathcal{O}_{\Spec A})$는 일반적으로 scheme이 아니기 때문이다. 가령 $A=\mathbb{K}[\x]$이고 $\mathfrak{a}=(\x)$이면 $Z(\mathfrak{a})$는 한 점이고 그 위의 stalk은 $\mathbb{K}[\x]_{(\x)}$인데, 한 점으로 이루어진 affine scheme의 global section ring은 prime ideal을 하나만 가져야 하므로 이 locally ringed space는 어떤 scheme과도 isomorphic하지 않다. [보조정리 9](#lem9)가 실제로 주는 canonical morphism은 $\mathfrak{a}$의 radical이 정의하는 reduced 구조에서 주어진 구조로 가는 것, 곧 $\Spec (A/\sqrt{\mathfrak{a}}) \rightarrow \Spec (A/\mathfrak{a})$ 쪽이다.

---
**참고문헌**

**[Har]** R. Hartshorne, *Algebraic geometry*. Graduate texts in mathematics. Springer, 1977.  
**[Vak]** R. Vakil, *The rising sea: Foundation of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/).

--- 