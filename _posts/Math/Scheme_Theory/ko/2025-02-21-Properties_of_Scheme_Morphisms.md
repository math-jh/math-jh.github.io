---
title: "스킴 사상의 성질들"
description: "스킴 사상의 주요 성질들을 정의하고, 준옹골사상과 준분리사상의 개념 및 기본 성질을 소개한다."
excerpt: "Affine, finite, finite type 등 scheme morphism의 기본 성질"

categories: [Math / Scheme Theory]
permalink: /ko/math/scheme_theory/properties_of_scheme_morphisms
sidebar: 
    nav: "scheme_theory-ko"

date: 2025-02-21
weight: 8
drift_needed: true
---

앞선 글에서 우리는 scheme morphism을 살펴보는 몇 가지 관점을 살펴보았다. 이번 글에서 우리는 본격적으로 scheme morphism이 갖는 성질들을 정의한다. 우선 이들이 공유하는 다음 성질을 정의한다.

::: 정의 1
Scheme morphism의 성질 $$P$$가 *local on target*이라는 것은 다음 두 조건이 성립하는 것이다. 
1. 만일 scheme morphism $$\varphi:X \rightarrow Y$$가 $$P$$를 만족할 경우, $$Y$$의 임의의 open subscheme $$V$$에 대하여 scheme morphism $$\varphi\vert_{\varphi^{-1}(V)}: \varphi^{-1}(V) \rightarrow V$$ 또한 $$P$$를 만족한다. 
2. 만일 scheme morphism $$\varphi:X \rightarrow Y$$에 대하여, $$Y$$의 open covering $$\{V_j\}$$가 존재하여 $$\varphi\vert_{\varphi^{-1}(V_j)}: \varphi^{-1}(V_j) \rightarrow V_j$$가 모두 $$P$$를 만족한다면 $$\varphi$$ 또한 그러하다. 
:::

Scheme은 affine scheme으로부터 만들어진다. Scheme morphism의 성질 $$P$$가 local on target이라면, scheme morphism $$\varphi:X \rightarrow Y$$의 target $$Y$$를 $$\Spec B$$로 가정하여도 되고, 그럼 adjoint

$$\Hom_\Sch(X, \Spec B)\cong \Hom_\cRing(B, \Gamma(X, \mathcal{O}_X))$$

를 통해 우리는 scheme morphism $$X \rightarrow \Spec B$$의 성질을 ring homomorphism $$B \rightarrow \Gamma(X, \mathcal{O}_X)$$의 성질을 통해 정의할 수 있다. 

## 준옹골사상과 준분리사상

::: 정의 2
Scheme morphism $$\varphi: X \rightarrow Y$$가 *quasi-compact<sub>준옹골</sub>*이라는 것은 임의의 affine open subset $$V\subseteq Y$$가 주어질 때마다 $$\varphi^{-1}(V)$$가 quasi-compact인 것이다. 
:::

::: 명제 3
Scheme morphism $$\varphi: X \rightarrow Y$$가 quasi-compact인 것은 $$Y$$의 임의의 quasi-compact open subset의 preimage가 quasi-compact인 것과 동치이다. 
:::
::: 증명
임의의 affine scheme은 quasi-compact이므로 ([§스펙트럼, ⁋보조정리 12](/ko/math/scheme_theory/spectrums#lem12)) 주어진 조건이 [정의 2](#def2)의 조건을 함의하는 것은 당연하다.

거꾸로 quasi-compact morphism $$\varphi: X \rightarrow Y$$가 주어졌다 하자. 이제 $$Y$$의 임의의 quasi-compact open subset $$V$$가 주어졌다 하면, $$V$$를 덮는 유한히 많은 affine open subset들의 covering $$\{V_j\}$$가 존재하며 이들의 preimage $$\varphi^{-1}(V_j)$$는 모두 quasi-compact이다. 이제 

$$\varphi^{-1}(V)=\varphi^{-1}\left(\bigcup_{j\in J} V_j\right)=\bigcup_{j\in J}\varphi^{-1}(V_j)$$

이고 quasi-compact set의 유한한 합집합은 다시 quasi-compact이므로 원하는 결과를 얻는다. 
:::

그럼 [명제 3](#prop3)의 동치로부터, 임의의 quasi-compact morphism의 합성은 다시 quasi-compact임을 안다. 뿐만 아니라 다음이 성립한다.

::: 명제 4
Noetherian scheme $$X$$에 대하여, scheme morphism $$\varphi: X \rightarrow Y$$는 항상 quasi-compact이다. 
:::
::: 증명
임의의 affine open subset $$V\subseteq Y$$가 주어졌다 하고, $$\varphi^{-1}(V)$$가 quasi-compact임을 보여야 한다. 그런데 [\[위상수학\] §차원, ⁋명제 12](/ko/math/topology/dimension#prop12)와 [\[위상수학\] §차원, ⁋명제 13](/ko/math/topology/dimension#prop13)의 첫째 결과로부터 noetherian인 위상공간의 임의의 부분공간은 quasi-compact이다.
:::

비슷하게 우리는 quasi-separated morphism을 정의한다. 이를 위해서는 quasi-separated scheme을 먼저 정의해야 한다.

::: 정의 5
Scheme $$X$$가 *quasi-separated<sub>준분리</sub>*인 것은 $$X$$의 임의의 두 quasi-compact open subset의 교집합이 다시 quasi-compact인 것이다. Scheme morphism $$\varphi: X \rightarrow Y$$가 *quasi-separated*인 것은 임의의 affine open set $$V\subseteq Y$$에 대하여, $$\varphi^{-1}(V)$$가 quasi-separated인 것이다. 
:::

그럼 다음이 성립한다.

::: 명제 6
Locally noetherian scheme은 항상 quasi-separated이다. 
:::
::: 증명
Locally noetherian scheme $$X$$의 임의의 두 affine open subset $$V_1=\Spec B_1, V_2=\Spec B_2$$가 주어졌다 하고 $$V_1\cap V_2$$가 quasi-compact임을 보여야 한다. 

우선 $$X$$가 locally noetherian이므로, $$X$$를 noetherian ring들의 스펙트럼 $$\Spec A_i$$로 덮을 수 있다. 이제 각각의 $$i$$에 대하여, [§스킴의 위상구조, ⁋보조정리 11](/ko/math/scheme_theory/topology_of_schemes#lem11)에 의하여 $$U_i\cap V_1$$을 noetherian ring들의 스펙트럼 $$\Spec (A_i)_g$$들로 덮을 수 있다. 이들을 모두 모으면 $$V_1$$을 noetherian ring들의 스펙트럼들로 덮을 수 있으며, [§스펙트럼, ⁋보조정리 12](/ko/math/scheme_theory/spectrums#lem12)에 의해 $$V_1=\Spec B_1$$은 유한히 많은 noetherian ring들의 스펙트럼으로 덮인다. 따라서 [§스킴의 위상구조, ⁋보조정리 13](/ko/math/scheme_theory/topology_of_schemes#lem13)에 의해 $$B_1$$은 noetherian ring이고 따라서 $$V_1=\Spec B_1$$은 noetherian이다. 다시  [\[위상수학\] §차원, ⁋명제 12](/ko/math/topology/dimension#prop12)와 [\[위상수학\] §차원, ⁋명제 13](/ko/math/topology/dimension#prop13)의 첫째 결과로부터 noetherian인 위상공간의 임의의 부분공간은 quasi-compact이므로, 특히 $$V_1\cap V_2$$ 또한 quasi-compact이다. 
:::

그럼 quasi-compactness와 quasi-separatedness는 [정의 1](#def1)의 성질을 만족할 뿐만 아니라, 다음 명제에서 확인할 수 있듯이 *affine-local on target*이다. ([§스킴의 위상구조, ⁋정의 9](/ko/math/scheme_theory/topology_of_schemes#def9))

::: 명제 7
Scheme morphism $$\varphi: X \rightarrow Y$$에 대하여 다음이 성립한다.

1. 만일 $$Y$$의 affine open covering $$\{V_j\}$$가 존재하여 각각의 $$\varphi^{-1}(V_j)$$가 quasi-compact라면, $$\varphi$$는 quasi-compact이다. 
2. 만일 $$Y$$의 affine open covering $$\{V_j\}$$가 존재하여 각각의 $$\varphi^{-1}(V_j)$$가 quasi-separated라면, $$\varphi$$는 quasi-separated이다. 
:::
::: 증명
1. $$Y$$의 임의의 affine open subset $$V$$가 주어졌다 하자. 그럼 [§스킴의 위상구조, ⁋보조정리 11](/ko/math/scheme_theory/topology_of_schemes#lem11)에 의하여 $$V$$와 $$V_j$$ 각각에서 principal open set이 되는 열린집합들로 $$V\cap V_j$$를 덮을 수 있고, 이를 모든 $$j$$에 대해 고려한 후 $$V$$의 quasi-compactness를 사용하면 이러한 것들 중 유한히 많은 것만 택할 수 있다. 이를 $$V=\bigcup W_l$$이라 하자.   
    한편 각각의 $$j$$에 대하여, $$\varphi^{-1}(V_j)$$는 quasi-compact이므로, 이를 유한히 많은 affine open subset들 $$U_{jk}$$들로 덮을 수 있고, 이제 $$\varphi^{-1}(W_l)\cap U_{jk}$$는 [§스펙트럼, ⁋명제 8](/ko/math/scheme_theory/spectrums#prop8)에 의해 $$U_{jk}$$의 principal open set이므로 $$\varphi^{-1}(W_l)$$ 각각을 affine open set들의 유한한 합집합으로 표현할 수 있고, 따라서 $$\varphi^{-1}(V)$$도 affine open set들의 유한한 합집합으로 표현할 수 있다. 이제 quasi-compact space의 유한한 합집합은 quasi-compact이므로 원하는 결과를 얻는다.
2. 이 또한 첫째 결과와 마찬가지 방식으로, [§스킴의 위상구조, ⁋보조정리 11](/ko/math/scheme_theory/topology_of_schemes#lem11)를 사용하여 임의의 affine open subset $$V=\Spec B$$를 그 preimage가 quasi-separated인 principal open subset들로 덮은 후 증명을 하면 된다. 
:::

## 아핀사상

우리는 adjoint

$$\Hom_\Sch(X, \Spec B)\cong\Hom_\cRing (B, \Gamma(X, \mathcal{O}_X))$$

에서, 특별히 $$X=\Spec A$$인 경우 

$$\Hom_\Sch(\Spec A,\Spec B)\cong\Hom_\cRing (B, A)$$

가 성립하는 것을 안다. ([§아핀스킴, ⁋명제 11](/ko/math/scheme_theory/affine_schemes#prop11)) 따라서, 위와 같이 affine-local on target인 스킴 사상의 성질을 살펴볼 때에는, $$Y$$의 임의의 affine open subset $$V\cong\Spec B$$에 대하여 $$U=\varphi^{-1}(V)$$도 $$X$$의 open subscheme $$U\cong \Spec A$$이고, 따라서 $$\varphi\vert_U: U \rightarrow V$$가 affine scheme들 사이의 morphism이 되어 이 성질을 ring homomorphism 

$$(\varphi\vert_U)^\sharp(V): \mathcal{O}_V(V) \rightarrow \mathcal{O}_U(U)$$

으로부터 얻어낼 수 있으면 좋을 것이다. 그러나 물론 임의의 scheme morphism $$\varphi: X \rightarrow Y$$에 대하여, $$Y$$의 affine open subset의 preimage가 affine이 되지는 않는다. ([§스킴, ⁋예시 8](/ko/math/scheme_theory/schemes#ex8))

::: 정의 8
Scheme morphism $$\varphi: X \rightarrow Y$$가 *affine*이라는 것은 $$Y$$의 임의의 affine open subset $$V$$에 대하여 $$\varphi^{-1}(V)$$가 $$X$$의 affine open subset인 것이다. 
:::

그럼 affine morphism의 합성이 affine인 것은 자명하다. 뿐만 아니라 이 성질은 [정의 1](#def1)의 성질 또한 만족하는데, 이에 대한 증명은 다소 길어지는 감이 있어 생략한다. 

::: 명제 9
Scheme morphism $$\varphi:X \rightarrow Y$$에 대하여, 만일 $$Y$$의 affine open covering $$\{V_j\}$$가 존재하여 각각의 $$\varphi^{-1}(V_j)$$가 affine라면, $$\varphi$$는 affine이다. 
:::
::: 증명
$$Y$$의 affine open subset $$\Spec B$$에 대한 성질 $$P$$를 "$$\varphi^{-1}(\Spec B)$$가 $$X$$의 affine open subset이다"로 정의하자. 그럼 $$\varphi$$가 affine이라는 것은 $$Y$$의 임의의 affine open subset이 $$P$$를 만족하는 것이고 주어진 가정은 $$Y$$의 어떤 affine open covering이 $$P$$를 만족한다는 것이므로, [§스킴의 위상구조, ⁋보조정리 12](/ko/math/scheme_theory/topology_of_schemes#lem12)의 둘째 조건과 셋째 조건 사이의 동치에 의하여 $$P$$가 [§스킴의 위상구조, ⁋정의 9](/ko/math/scheme_theory/topology_of_schemes#def9)의 의미에서 affine-local property임을 보이면 충분하다. 이하에서 sheaf morphism $$\varphi^\sharp: \mathcal{O}_Y \rightarrow \varphi_\ast \mathcal{O}_X$$의 열린집합 $$V$$에서의 성분을 $$\varphi^\sharp(V): \mathcal{O}_Y(V) \rightarrow \mathcal{O}_X(\varphi^{-1}(V))$$로 적는다.

우선 [§스킴의 위상구조, ⁋정의 9](/ko/math/scheme_theory/topology_of_schemes#def9)의 첫째 조건을 확인하자. $$\varphi^{-1}(\Spec B)$$가 affine open subset $$\Spec A$$라 하면 [§아핀스킴, ⁋명제 11](/ko/math/scheme_theory/affine_schemes#prop11)에 의하여 $$\Spec A \rightarrow \Spec B$$는 적당한 ring homomorphism $$\phi: B \rightarrow A$$에 대해 $$\Spec\phi$$의 꼴이고, [§스펙트럼, ⁋명제 8](/ko/math/scheme_theory/spectrums#prop8)의 증명에서 얻어진 식

$$(\Spec\phi)^{-1}(D(f))=D(\phi(f))$$

으로부터 임의의 $$f\in B$$에 대하여 $$\varphi^{-1}(\Spec B_f)=D(\phi(f))\cong\Spec A_{\phi(f)}$$이므로 $$\Spec B_f$$ 또한 $$P$$를 만족한다.

이제 둘째 조건을 확인해야 한다. 즉 $$B=(f_1,\ldots, f_r)$$이고 각각의 $$U_i=\varphi^{-1}(D(f_i))$$가 affine이라 가정한 후, $$U=\varphi^{-1}(\Spec B)$$가 affine임을 보여야 한다. 편의상 $$R=\Gamma(U, \mathcal{O}_X)$$라 하고 $$f_i$$의 $$\varphi^\sharp(\Spec B): B \rightarrow R$$에 의한 상을 $$g_i\in R$$이라 하자. 또, $$g\in \Gamma(U, \mathcal{O}_X)$$에 대하여 $$g$$의 stalk이 $$\mathcal{O}_{X,x}$$의 maximal ideal에 속하지 <em-ko>않는</em-ko> 점 $$x$$들의 집합을 $$U_g$$로 적자. 그럼 $$U$$의 임의의 affine open subset $$\Spec A$$에 대하여 $$U_g\cap \Spec A=D(g\vert_{\Spec A})$$인 것이 정의에 의해 자명하고, 특히 $$U_g$$는 열린집합이다. 

다음의 세 가지를 관찰한다. 첫째로, $$B=(f_1,\ldots, f_r)$$이므로 $$\Spec B=\bigcup_{i=1}^rD(f_i)$$이고 따라서 $$\{U_i\}_{i=1}^r$$은 $$U$$의 유한한 affine open covering이다. 뿐만 아니라 $$1=\sum_{i=1}^rb_if_i$$인 $$b_i\in B$$를 택하여 $$\varphi^\sharp(\Spec B)$$를 취하면 $$g_1,\ldots, g_r$$이 $$R$$의 unit ideal을 생성함을 안다. 둘째로, $$\varphi$$가 locally ringed space들 사이의 morphism이므로 각각의 $$x\in U$$에서 $$\varphi^\sharp_x:\mathcal{O}_{Y,\varphi(x)} \rightarrow \mathcal{O}_{X,x}$$는 local homomorphism이고, 따라서 $$\varphi(x)\in D(f_i)$$인 것과 $$x\in U_{g_i}$$인 것이 동치이므로 $$U_i=U_{g_i}$$이다. 셋째로, $$U_i\cong \Spec A_i$$라 하고 $$\Spec A_i \rightarrow \Spec B_{f_i}$$에 대응되는 ring homomorphism을 $$\phi_i$$라 하면 $$D(f_j)\cap D(f_i)$$는 $$\Spec B_{f_i}$$의 principal open set이므로 위와 같이 [§스펙트럼, ⁋명제 8](/ko/math/scheme_theory/spectrums#prop8)을 적용하여 $$U_i\cap U_j$$가 $$\Spec A_i$$의 principal open set, 특히 affine임을 안다.

이제 각각의 $$i$$에 대하여 canonical map $$R_{g_i} \rightarrow \Gamma(U_{g_i}, \mathcal{O}_X)$$이 isomorphism임을 보인다. $$U$$의 open covering $$\{U_j\}_{j=1}^r$$에 대한 [\[위상수학\] §층, ⁋정의 1](/ko/math/topology/sheaves#def1)의 두 조건은 다음의 exact sequence

$$0 \rightarrow R \rightarrow \bigoplus_{j=1}^r \mathcal{O}_X(U_j) \rightarrow \bigoplus_{j,k=1}^r \mathcal{O}_X(U_j\cap U_k)$$

가 존재한다는 것과 같다. 여기에서 둘째 함수는 $$(s_j)_j\mapsto (s_j\vert_{U_j\cap U_k}-s_k\vert_{U_j\cap U_k})_{j,k}$$이다. 이는 $$R$$-module들의 exact sequence이고 direct sum이 유한하므로, [\[가환대수학\] §국소화의 성질들, ⁋명제 2](/ko/math/commutative_algebra/properties_of_localization#prop2)에 의하여 $$g_i$$에서 localize하여도 exactness가 보존되어 다음의 exact sequence

$$0 \rightarrow R_{g_i} \rightarrow \bigoplus_{j=1}^r \mathcal{O}_X(U_j)_{g_i} \rightarrow \bigoplus_{j,k=1}^r \mathcal{O}_X(U_j\cap U_k)_{g_i}$$

를 얻는다. (여기에서 $$\mathcal{O}_X(U_j)$$의 localization은 $$g_i$$의 $$U_j$$로의 restriction에서의 localization을 뜻한다.) 한편 $$U_j$$와 $$U_j\cap U_k$$는 모두 affine이고 affine scheme $$\Spec A$$와 $$a\in A$$에 대하여 $$\mathcal{O}_{\Spec A}(D(a))=A_a$$이므로 ([§스킴, ⁋보조정리 2](/ko/math/scheme_theory/schemes#lem2)) 위에서 관찰한 $$U_g\cap \Spec A=D(g\vert_{\Spec A})$$로부터

$$\mathcal{O}_X(U_j)_{g_i}=\mathcal{O}_X(U_j\cap U_{g_i}),\qquad \mathcal{O}_X(U_j\cap U_k)_{g_i}=\mathcal{O}_X(U_j\cap U_k\cap U_{g_i})$$

를 얻는다. 그런데 이렇게 얻어진 exact sequence는 정확히 $$U_{g_i}$$의 open covering $$\{U_j\cap U_{g_i}\}_{j=1}^r$$에 대한 층 조건이 주는 exact sequence이므로, $$R_{g_i}$$와 $$\Gamma(U_{g_i}, \mathcal{O}_X)$$는 모두 같은 함수의 kernel이 되어 canonical map $$R_{g_i} \rightarrow \Gamma(U_{g_i}, \mathcal{O}_X)$$은 isomorphism이다.

마지막으로 [§아핀스킴, ⁋정리 13](/ko/math/scheme_theory/affine_schemes#thm13)의 adjunction

$$\Hom_\Sch(U, \Spec R)\cong \Hom_\cRing(R, \Gamma(U, \mathcal{O}_X))$$

에서 $$\id_R$$에 대응되는 scheme morphism $$\psi: U \rightarrow \Spec R$$을 생각하자. $$\psi$$ 또한 locally ringed space들 사이의 morphism이므로 각각의 $$x\in U$$에서 $$\psi^\sharp_x$$는 local homomorphism이고, 합성 $$R \rightarrow \mathcal{O}_{\Spec R, \psi(x)} \rightarrow \mathcal{O}_{X,x}$$가 canonical map $$R=\Gamma(U, \mathcal{O}_X) \rightarrow \mathcal{O}_{X,x}$$이므로 $$\psi(x)$$는 이 canonical map에 의한 $$\mathcal{O}_{X,x}$$의 maximal ideal의 preimage이다. 따라서

$$\psi^{-1}(D(g_i))=U_{g_i}=U_i$$

이고, $$\psi\vert_{U_i}: U_i \rightarrow D(g_i)\cong \Spec R_{g_i}$$는 affine scheme들 사이의 morphism으로서 방금 얻은 isomorphism $$R_{g_i}\cong \Gamma(U_i, \mathcal{O}_X)$$에 대응되므로 [§아핀스킴, ⁋명제 11](/ko/math/scheme_theory/affine_schemes#prop11)에 의하여 isomorphism이다. 이제 $$g_i$$들이 $$R$$의 unit ideal을 생성하므로 $$\{D(g_i)\}$$는 $$\Spec R$$을 덮고 $$\{U_i\}$$는 $$U$$를 덮으므로, $$\psi$$는 isomorphism이다. 즉 $$U\cong\Spec R$$은 affine이다. 
:::

## 유한사상, 정수형사상과 유한형사상

::: 정의 10
Scheme morphism $$\varphi:X \rightarrow Y$$가 *finite<sub>유한</sub>*인 것은 $$\varphi$$가 affine이고, $$Y$$의 임의의 affine open subset $$V$$에 대하여, ring homomorphism

$$(\varphi\vert_{\varphi^{-1}(V)})^\sharp(V): \mathcal{O}_V(V) \rightarrow \mathcal{O}_{\varphi^{-1}(V)}(\varphi^{-1}(V))$$

이 finite ring homomorphism인 것이다. ([\[가환대수학\] §정수적 확장, ⁋정의 3](/ko/math/commutative_algebra/integral_extension#def3))
:::

이해를 돕기 위해 affine open subset $$V\subseteq Y$$를 $$\Spec B$$라 쓰자. 그럼 $$\varphi$$가 affine이라는 가정으로부터 $$U=\varphi^{-1}(V)$$는 $$X$$의 affine open subset이고 따라서 $$U\cong\Spec A$$이도록 하는 $$A$$가 존재한다. 이러한 identification을 통해, scheme morphism $$\varphi\vert_U: U \rightarrow V$$는 스펙트럼 사이의 morphism $$\Spec A \rightarrow \Spec B$$와 같은 것이고, 이제 $$\varphi$$가 finite이라는 것은 이 morphism에 해당하는 ring homomorphism $$B \rightarrow A$$가 finite인 것이다. 비슷하게 다음을 정의한다.

::: 정의 11
Scheme morphism $$\varphi:X \rightarrow Y$$가 *integral<sub>정수형</sub>*인 것은 $$\varphi$$가 affine이고, $$Y$$의 임의의 affine open subset $$V$$에 대하여, ring homomorphism

$$(\varphi\vert_{\varphi^{-1}(V)})^\sharp(V): \mathcal{O}_V(V) \rightarrow \mathcal{O}_{\varphi^{-1}(V)}(\varphi^{-1}(V))$$

이 integral ring homomorphism인 것이다. ([\[가환대수학\] §정수적 확장, ⁋정의 3](/ko/math/commutative_algebra/integral_extension#def3)) 
:::

이제 그 정의로부터 finite morphism과 integral morphism이 합성에 대해 닫혀있다는 것을 안다. 또, 이들이 [정의 1](#def1)의 조건을 만족하는 것은 [\[가환대수학\] §정수적 확장, ⁋명제 14](/ko/math/commutative_algebra/integral_extension#prop14)와 [\[가환대수학\] §정수적 확장, ⁋명제 15](/ko/math/commutative_algebra/integral_extension#prop15)로부터 알 수 있으므로 이들은 모두 affine-local on target이다. 

우리는 [\[가환대수학\] §정수적 확장, ⁋보조정리 4](/ko/math/commutative_algebra/integral_extension#lem4)에 의해 임의의 finite morphism은 integral인 것을 안다. 이제 이 보조정리를 완전하게 대수기하의 언어로 서술하기 위해서는 finite type morphism을 정의해야 한다. 

::: 정의 12
Scheme morphism $$\varphi:X \rightarrow Y$$가 *locally of finite type<sub>국소적으로 유한형</sub>*인 것은 $$Y$$의 임의의 affine open subset $$V$$와 $$\varphi^{-1}(V)$$의 임의의 affine open subset $$U$$에 대하여, 

$$(\varphi\vert_{U})^\sharp(V): \mathcal{O}_V(V) \rightarrow \mathcal{O}_U(U)$$

이 finite type인 것이다. ([\[가환대수학\] §정수적 확장, ⁋정의 3](/ko/math/commutative_algebra/integral_extension#def3)) 
:::

역시 위와 마찬가지로, $$V\cong \Spec B$$라 하고 $$U\cong\Spec A\subseteq \varphi^{-1}(V)$$라 하자. 그럼 scheme morphism $$\varphi\vert_U: U \rightarrow V$$를 $$\Spec A \rightarrow \Spec B$$로 볼 수 있고, 이에 대응하는 ring homomorphism $$B \rightarrow A$$가 finite type일 것을 요구하는 것이다. 그럼 finite type morphism은 다음과 같이 정의된다.

::: 정의 13
Scheme morphism $$\varphi:X \rightarrow Y$$가 *morphism of finite type<sub>유한형사상</sub>*이라는 것은 $$\varphi$$가 quasi-compact morphism locally of finite type인 것이다. 
:::

정의로부터 morphism of locally finite type은 affine-local on target임이 명확하다. 또, quasi-compact morphism은 [명제 7](#prop7)로부터 affine-local on target이므로 finite type morphism 또한 affine-local on target이다. 

그럼 [\[가환대수학\] §정수적 확장, ⁋보조정리 4](/ko/math/commutative_algebra/integral_extension#lem4)에 의해 다음이 성립한다.

::: 명제 14
Scheme morphism $$\varphi:X \rightarrow Y$$가 finite인 것은 $$\varphi$$가 integral morphism (locally) of finite type인 것과 동치이다. 
:::
::: 증명
한쪽 방향은 자명하다. 반대쪽 방향은 우선 $$\varphi$$가 integral이라는 가정으로부터 임의의 affine open subset $$V\subseteq Y$$에 대하여 $$\varphi^{-1}(V)$$가 $$X$$의 affine open subset임을 알고, 이렇게 얻어진 ring map에 [\[가환대수학\] §정수적 확장, ⁋보조정리 4](/ko/math/commutative_algebra/integral_extension#lem4)를 적용하면 된다. 
:::

위의 명제에서 $$\varphi$$는 integral morphism이므로 affine morphism이고, 따라서 quasi-compact morphism이므로 ([§스펙트럼, ⁋보조정리 12](/ko/math/scheme_theory/spectrums#lem12)) $$\varphi$$가 finite type이든, locally finite type이든 똑같은 가정이 된다. 

::: 예시 15
이번 절에서 살펴본 morphism들의 예시를 살펴보자. Affine scheme들의 세상에서 이는 그저 [\[가환대수학\] §정수적 확장, ⁋정의 3](/ko/math/commutative_algebra/integral_extension#def3)의 예시들을 보는 것에 지나지 않는다. 이번 예시의 목적은 이들에 기하학적인 직관을 부여하는 것이다.

우선 algebraically closed field $$\mathbb{K}$$에 대하여, ring map $$\iota:\mathbb{K}[\x] \rightarrow \mathbb{K}[\x,\y]$$를 생각하면 $$\mathbb{K}[\x,\y]$$는 $$\mathbb{K}[\x]$$-algebra로서 하나의 원소 $$\y$$에 의해 생성되므로 finite type ring homomorphism이지만, $$\mathbb{K}[\x]$$-module로서는 유한하게 생성되지 않으므로 finite ring homomorphism은 아니다. 

이제 이에 대응되는 scheme morphism $$\Spec\iota: \Spec \mathbb{K}[\x,\y] \rightarrow\Spec \mathbb{K}[\x]$$를 생각하자. 이는 임의의 prime ideal $$\mathfrak{p}\subset \mathbb{K}[\x,\y]$$를 받아 $$\mathbb{K}[\x]$$의 prime ideal $$\mathfrak{p}\cap \mathbb{K}[\x]$$를 내놓는 함수이다. 이는 기하적으로는 affine plane $$\mathbb{A}^2_\mathbb{K}$$의 점 $$(x,y)$$를 affine line $$\mathbb{A}^1_\mathbb{K}$$의 점 $$x$$에 대응시키는 함수이다. 

![finite_type_morphism](/assets/images/Math/Scheme_Theory/Properties_of_Scheme_Morphisms-1.svg){:style="width:27.72em" class="invert" .align-center}

이와 관련된 finite morphism의 예시로는 위의 ring homomorphism $$\iota:\mathbb{K}[\x]\rightarrow \mathbb{K}[\x,\y]$$에 projection map $$\pi:\mathbb{K}[\x,\y] \rightarrow \mathbb{K}[\x,\y]/(\x-\y^2)$$을 합성한 것이 있다. 그럼 $$\mathbb{K}[\x,\y]/(\x-\y^2)$$은 $$\mathbb{K}[\x]$$-module로서 $$1$$과 $$\y$$에 의해 생성되므로 $$\phi:\mathbb{K}[\x] \rightarrow \mathbb{K}[\x,\y]/(\x-\y^2)$$은 finite morphism이다. 

한편 우리는 ring homomorphism $$\pi:A \rightarrow A/\mathfrak{a}$$는 기하적으로 $$\mathfrak{a}$$가 정의하는 닫힌집합의 inclusion에 해당하는 것을 안다. 따라서 합성

$$\phi: \mathbb{K}[\x] \rightarrow \mathbb{K}[\x,\y] \rightarrow \mathbb{K}[\x,y]/(\x-\y^2)$$

이 정의하는 scheme morphism

$$\Spec\phi: \Spec \frac{\mathbb{K}[\x,\y]}{(\x-\y^2)}\rightarrow \Spec \mathbb{K}[\x,\y] \rightarrow \Spec\mathbb{K}[\x]$$

은 기하적으로 $$\x=\y^2$$의 zero set $$Z(\x-\y^2)$$에서 $$x$$축으로의 projection으로 볼 수 있다.

![finite_morphism](/assets/images/Math/Scheme_Theory/Properties_of_Scheme_Morphisms-2.svg){:style="width:25.48em" class="invert" .align-center}

이 두 예시의 기하학적인 차이는 꽤나 명확하다. 첫 번째 예시의 경우, target의 한 점에서의 fiber가 무한집합인 반면 두 번째 예시의 경우 한 점에서의 fiber가 유한집합이다. 대수적으로 이는 target $$\mathbb{A}_\mathbb{K}^1$$의 임의의 점 $$\mathfrak{p}=(\x-a)$$를 가져왔을 때, 임의의 $$\mathfrak{q}_b=(\x-a, \y-b)\in \mathbb{A}_\mathbb{K}^2$$는 $$(\Spec\iota)(\mathfrak{q}_b)=\mathfrak{p}$$를 만족하는 반면, 두 번째 예시에서는 오직 두 개의 점 $$\mathfrak{q}_+=(\x-a, \y-\sqrt{a})$$와 $$\mathfrak{q}_-=(\x-a, \y+\sqrt{a})$$만이 $$(\Spec\phi)(\mathfrak{q}_\pm)=\mathfrak{p}$$를 만족하는 것으로 확인할 수 있다. 

이와 같이, finite type morphism은 기하적으로는 fiber가 유한차원인 것과 관련이 있고, finite morphism은 fiber가 유한집합인 것과 관련이 있다. 
:::

아직은 위의 [예시 15](#ex15)과 같은 상황에서 scheme morphism의 fiber를 계산하기 위해서는 그때그떄 상황에 맞추어 우직하게 계산을 해 나가는 수밖에 없지만, 나중에 fiber product를 계산하고 나면 조금 더 정형화된 방식을 사용할 수 있게 된다. 그 떄를 위해  다음을 정의한다.

::: 정의 16
Scheme morphism $$\varphi: X \rightarrow Y$$가 *quasi-finite<sub>준유한</sub>*인 것은 $$\varphi$$가 morphism of finite type이고 임의의 $$y\in Y$$에 대하여 집합 $$\varphi^{-1}(y)$$가 항상 유한집합인 것이다. 
:::

그럼 [예시 15](#ex15)에서의 finite morphism에 대한 기하학적 직관은 항상 참이다. 즉, 임의의 finite morphism은 항상 quasi-finite이다. 이는 지금 당장 증명하는 것도 가능하지만, fiber product를 정의하고 난 후로 미룬다. 

마지막으로 다음을 정의한다. 

::: 정의 17
Scheme morphism $$\varphi: X \rightarrow Y$$가 *locally of finite presentation<sub>국소유한표시사상</sub>*이라는 것은 $$Y$$의 임의의 affine open subset $$V\cong \Spec B$$가 주어질 때마다, $$\varphi^{-1}(V)$$의 covering $$\varphi^{-1}(V)=\bigcup \Spec A_i$$가 존재하여 $$B \rightarrow A_i$$가 모두 finitely presented인 것이다. 만일 scheme morphism $$\varphi:X \rightarrow Y$$가 quasi-compact, quasi-separated, locally of finite presentation이라면 $$\varphi$$가 *morphism of finite presentation<sub>유한표시사상</sub>*이라 부른다. 
:::

대부분의 경우 우리는 모든 scheme들이 locally noetherian인 경우를 생각하고, 이 경우 [\[가환대수학\] §기본 개념들, ⁋명제 9](/ko/math/commutative_algebra/basic_notions#prop9)에 의하여 이 개념은 새로운 것이 아니다. 