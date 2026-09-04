---
title: "갈루아 군의 성질들"
description: "갈루아 군에 위상구조를 부여하는 방법을 다루며, 부분군 격자와 부분확장 격자 사이의 대응을 설명한다."
excerpt: "Krull 위상을 갖는 무한 Galois group의 구조"

categories: [Math / Field Theory]
permalink: /ko/math/field_theory/properties_of_galois_extensions
sidebar: 
    nav: "field_theory-ko"

date: 2025-06-18
weight: 9


---

우리는 앞서 Galois extension과 Galois group을 정의했다. Galois theory의 핵심적인 결과는 Galois extension $\mathbb{L}/\mathbb{K}$에 대하여 Galois group $\Gal(\mathbb{L}/\mathbb{K})$의 closed subgroup들의 lattice와, $\mathbb{L}/\mathbb{K}$의 subextension들의 lattice 사이에 포함관계를 뒤집는 bijection이 존재한다는 것이다. 많은 경우에 이 결과는 Galois group $\Gal(\mathbb{L}/\mathbb{K})$이 유한한 경우만 다루지만, 우리는 $\Gal(\mathbb{L}/\mathbb{K})$가 무한할 경우 또한 다룰 것이므로 이를 위해서는 $\Gal(\mathbb{L}/\mathbb{K})$에 적절한 위상구조를 주어야 한다. 

## 갈루아 군의 위상구조

Galois extension $\mathbb{L}/\mathbb{K}$이 주어졌다 하고, $\Gal(\mathbb{L}/\mathbb{K})$이 이 extension의 Galois group이라 하자. Galois group은 어쨌든 집합 $\mathbb{L}$에서 $\mathbb{L}$로 가는 함수들의 모임이므로 우리는 $\mathbb{L}$에서 $\mathbb{L}$로의 함수들의 모임 $\Fun(\mathbb{L},\mathbb{L})=\mathbb{L}^\mathbb{L}$에 위상구조를 준다면 이 집합의 부분집합으로서 $\Gal(\mathbb{L}/\mathbb{K})$에 위상구조를 줄 수 있다. ([\[위상수학\] §부분공간, ⁋정의 1](/ko/math/topology/subspaces#def1)) 

이를 위해 $\mathbb{L}$ 위에 discrete topology를 부여하자. ([\[위상수학\] §열린집합, ⁋예시 2](/ko/math/topology/open_sets#ex2)) 그럼 [\[위상수학\] §곱공간, ⁋정의 1](/ko/math/topology/product_spaces#def1) 이후의 논의에 의하여 projection $\pr_x:\mathbb{L}^\mathbb{L}\rightarrow\mathbb{L}$들에 대한 $\pr_x^{-1}(U)$꼴의 집합들이 $\mathbb{L}^\mathbb{L}$의 subbase를 이루며, $\mathbb{L}$이 discrete이므로 여기에서 $U$를 한원소집합으로 제한하여도 여전히 subbase를 얻는다. 즉 우리는 이 집합의 subbase는 다음과 같은 꼴

$$U_{x,y}=\left\{\sigma\mid\sigma(x)=y \right\}$$

로 쓸 수 있는 집합들의 모임임을 알고 있으므로, 이것의 subspace로서 $\Gal(\mathbb{L}/\mathbb{K})$을 보면, 임의의 $\sigma\in\Gal(\mathbb{L}/\mathbb{K})$에 대하여 다음과 같은 형태

$$U_{x_1,\ldots,x_n}(\sigma)=\left\{\tau\in\Gal(\mathbb{L}/\mathbb{K})\mid \text{$\tau(x_i)=\sigma(x_i)$ for all $i$}\right\}$$

의 집합들의 모임이 $\sigma$에서의 local base임을 안다. ([\[위상수학\] §위상공간의 기저, ⁋정의 4](/ko/math/topology/topological_bases#def4)) 

한편 위의 조건을 만족하는 함수들은 $\mathbb{L}$의 finite subextension $\mathbb{M}=\mathbb{K}(x_1,\ldots,x_n )$으로 제한했을 때 $\sigma$와 일치하는 함수들이며, 거꾸로 임의의 finite subextension $\mathbb{M}/\mathbb{K}$은 이러한 방식으로 $\sigma$의 local base의 원소를 하나 정의한다. 즉 $\Ext_{\fin}(\mathbb{L}/\mathbb{K})$를 extension $\mathbb{L}/\mathbb{K}$의 *finite* subextension들의 모임이라 하고 임의의 $\mathbb{M}/\mathbb{K}\in \Ext_{\fin}(\mathbb{L}/\mathbb{K})$와 임의의 $\sigma\in \Gal(\mathbb{L}/\mathbb{K})$에 대하여, $\Gal(\mathbb{L}/\mathbb{K})$의 부분집합 $U_\mathbb{M}(\sigma)$를 다음의 식 

$$U_\mathbb{M}(\sigma)=\left\{\tau\in \Gal(\mathbb{L}/\mathbb{K})\mid \sigma\vert_\mathbb{M}=\tau\vert_\mathbb{M}\right\}$$

으로 정의하면 이 집합은 $\sigma$의 local base의 원소가 되며, 이들을 모아둔 $(U_\mathbb{M}(\sigma))_{\mathbb{M}\in\Ext_{\fin}(\mathbb{L}/\mathbb{K})}$가 정확히 $\sigma$에서의 local base이다. 이렇게 얻어지는 $\Gal(\mathbb{L}/\mathbb{K})$의 위상구조를 *Krull topology*라 부른다.
  
::: 예시 1
특별히 $\mathbb{L}/\mathbb{K}$이 finite degree Galois extension인 경우를 생각하자. 그럼 [§갈루아 확장, ⁋정의 12](/ko/math/field_theory/galois_extension#def12) 이후의 논의로부터 우리는 $\Gal(\mathbb{L}/\mathbb{K})$이 유한집합인 것을 안다. 한편 $\mathbb{L}/\mathbb{K}$이 finite degree이므로 $\mathbb{L}/\mathbb{K}$ 자기 자신이 이미 $\Ext_{\fin}(\mathbb{L}/\mathbb{K})$의 원소이고 따라서 임의의 $\sigma\in \Gal(\mathbb{L}/\mathbb{K})$에 대하여

$$U_\mathbb{L}(\sigma)=\left\{\tau\in\Gal(\mathbb{L}/\mathbb{K})\mid \sigma\vert_\mathbb{L}=\tau\vert_\mathbb{L}\right\}=\left\{\sigma\right\}$$

가 위에서 살펴본 $\sigma$의 local base의 원소이다. 즉 한원소집합 $\left\{\sigma\right\}$가 열린집합이므로 이 경우 $\Gal(\mathbb{L}/\mathbb{K})$는 discrete topology가 주어진 집합이 된다. 
:::

한편, 위와 같이 정의한 위상공간 $\Gal(\mathbb{L}/\mathbb{K})$는 원래 $\mathbb{K}$-automorphism들의 합성을 연산으로 갖는 group이며, 이 때 함수들의 합성이 이 위상구조와 잘 어울리는 것을 어렵지 않게 보일 수 있다. 
  
::: 명제 2
위에서 정의한 $\Gal(\mathbb{L}/\mathbb{K})$는 topological group이다. 
:::
::: 증명
즉 두 함수 

$$\Gal(\mathbb{L}/\mathbb{K})\times\Gal(\mathbb{L}/\mathbb{K})\rightarrow\Gal(\mathbb{L}/\mathbb{K});\quad (\sigma,\sigma')\mapsto \sigma\sigma',\qquad \Gal(\mathbb{L}/\mathbb{K})\rightarrow\Gal(\mathbb{L}/\mathbb{K});\quad \sigma\mapsto \sigma^{-1}$$

이 연속임을 보여야한다. 우선 $\sigma\sigma'$의 임의의 local base의 원소 $U_\mathbb{M}(\sigma\sigma')$를 생각하면 정의에 의하여

$$U_\mathbb{M}(\sigma\sigma')=\left\{\tau\in\Gal(\mathbb{L}/\mathbb{K})\mid \tau\vert_\mathbb{M}=\sigma\sigma'\vert_\mathbb{M}\right\}$$

이다. 여기에서 $\sigma'$이 $\mathbb{L}$의 $\mathbb{K}$-automorphism이므로 $\sigma'(\mathbb{M})$ 또한 $\mathbb{L}$의 finite subextension이며, 만일 $\tau\in U_{\sigma'(\mathbb{M})}(\sigma)$이고 $\tau'\in U_\mathbb{M}(\sigma')$이라면 임의의 $x\in \mathbb{M}$에 대하여 $\tau'(x)=\sigma'(x)\in\sigma'(\mathbb{M})$이므로 $\tau\tau'(x)=\sigma\sigma'(x)$이다. 즉 $\Gal(\mathbb{L}/\mathbb{K})\times\Gal(\mathbb{L}/\mathbb{K})$의 열린집합 $U_{\sigma'(\mathbb{M})}(\sigma)\times U_\mathbb{M}(\sigma')$가 위의 집합의 preimage에 포함되고 따라서 multiplication map은 연속이다. 

비슷한 방식으로 $\sigma^{-1}$의 local base $U_\mathbb{M}(\sigma^{-1})$은 다음의 식 

$$U_\mathbb{M}(\sigma^{-1})=\left\{\tau\in\Gal(\mathbb{L}/\mathbb{K})\mid \tau\vert_\mathbb{M}=\sigma^{-1}\vert_\mathbb{M}\right\}$$

으로 주어지며, 이 때 $\sigma^{-1}(\mathbb{M})$ 또한 finite subextension이므로 $U_{\sigma^{-1}(\mathbb{M})}(\sigma)$를 생각할 수 있다. 임의의 $x\in \mathbb{M}$에 대하여 $\sigma^{-1}(x)\in\sigma^{-1}(\mathbb{M})$이므로 $\tau\in U_{\sigma^{-1}(\mathbb{M})}(\sigma)$라면 $\tau(\sigma^{-1}(x))=\sigma(\sigma^{-1}(x))=x$, 즉 $\tau^{-1}(x)=\sigma^{-1}(x)$이고 따라서 이 집합은 위의 집합의 preimage에 포함된다. 
:::

특히 임의의 $\sigma$에서의 local base는 identity $\id_\mathbb{L}$의 local base를 left translation map을 따라 옮긴 것으로 주어진다. 즉 임의의 $\sigma\in \Gal(\mathbb{L}/\mathbb{K})$에 대하여 다음의 식

$$U_\mathbb{M}(\sigma)=\sigma U_\mathbb{M}(\id_\mathbb{L})$$

이 성립한다. 이로부터 우리는 위의 집합 대신 다음의 집합

$$U_\mathbb{M}(\id_\mathbb{L})=\left\{\tau\in \Gal(\mathbb{L}/\mathbb{K})\mid \tau\vert_\mathbb{M}=\id_\mathbb{M}\right\}$$

만 살펴보아도 되는 것을 안다. 그럼 정의에 의해 집합으로서

$$U_\mathbb{M}(\id_\mathbb{L})=\Gal(\mathbb{L}/\mathbb{M})$$

이다. 여기에서 [§갈루아 확장, ⁋정리 8](/ko/math/field_theory/galois_extension#thm8)의 셋째 조건은 $\mathbb{K}$ 대신 $\mathbb{M}$ 위에서 보아도 성립하므로 $\mathbb{L}/\mathbb{M}$ 또한 Galois extension이며, 우측의 group에서 $\Gal(\mathbb{L}/\mathbb{K})$로의 inclusion은 단순히 $\mathbb{M}$-automorphism을 $\mathbb{K}$-automorphism으로 보아 얻어지는 것이다. 뿐만 아니라 $\Gal(\mathbb{L}/\mathbb{M})$이 갖는 위상구조는 $U_\mathbb{M}(\id_\mathbb{L})$이 $\Gal(\mathbb{L}/\mathbb{K})$로부터 물려받는 subspace topology와 같다. 그럼 같은 정리의 첫째 조건에 의하여 $\mathbb{L}^{\Gal(\mathbb{L}/\mathbb{M})}=\mathbb{M}$이므로

$$U_\mathbb{M}(\id_\mathbb{L})\subseteq U_\mathbb{N}(\id_\mathbb{L})\iff \mathbb{M}\supseteq \mathbb{N}$$

이 성립한다. 오른쪽에서 왼쪽은 정의에서 바로 나오고, 왼쪽에서 오른쪽은 $\mathbb{N}=\mathbb{L}^{\Gal(\mathbb{L}/\mathbb{N})}\subseteq\mathbb{L}^{\Gal(\mathbb{L}/\mathbb{M})}=\mathbb{M}$에서 나온다. 

이제 finite degree *Galois* subextension들의 모임 $\Ext_{\fin,\gal}(\mathbb{L}/\mathbb{K})$를 생각하면 [§갈루아 확장, ⁋명제 11](/ko/math/field_theory/galois_extension#prop11)에 의해 이것이 $\Ext_{\fin}(\mathbb{L}/\mathbb{K})$의 cofinal subset임을 안다. 즉 $(U_\mathbb{M}(\id_\mathbb{L}))_{\mathbb{M}\in\Ext_{\fin,\gal}(\mathbb{L}/\mathbb{K})}$도 $\id_\mathbb{L}$의 local base이다. 그럼 임의의 $\mathbb{M}\in \Ext_{\fin,\gal}(\mathbb{L}/\mathbb{K})$에 대하여 [§갈루아 확장, ⁋명제 13](/ko/math/field_theory/galois_extension#prop13)에서 살펴보았던 restriction homomorphism $\rho:\Gal(\mathbb{L}/\mathbb{K})\rightarrow\Gal(\mathbb{M}/\mathbb{K})$을 생각하면, $\mathbb{M}$의 임의의 finite degree subextension은 $\mathbb{L}$의 finite degree subextension이기도 하므로 이 restriction homomorphism은 위에서 정의한 위상구조에 대하여 연속이다. 이와 같은 상황에서 $\rho$는 $\Gal(\mathbb{L}/\mathbb{K})$에서 finite discrete space $\Gal(\mathbb{M}/\mathbb{K})$로의 연속함수이므로 ([예시 1](#ex1)), $\ker\rho$는 $\Gal(\mathbb{L}/\mathbb{K})$의 closed subgroup이다. 그런데 정의에 의해 

$$\sigma\in\ker\rho\iff \sigma\vert_\mathbb{M}=\id\vert_\mathbb{M}\iff\sigma\in U_\mathbb{M}(\id_\mathbb{L})$$

이므로 각각의 $U_\mathbb{M}(\id_\mathbb{L})$들은 clopen이다. 한편 임의의 clopen set은 항상 connected component들의 합집합으로 쓸 수 있고, 따라서 clopen set들의 공집합이 아닌 임의의 교집합은 connected component를 포함해야 한다. 그러나 다음이 성립한다. 

::: 명제 3
위의 상황에서 다음의 식 

$$\{\id_\mathbb{L}\}=\bigcap_{\mathbb{M}\in \Ext_{\fin,\gal}(\mathbb{L}/\mathbb{K})}U_\mathbb{M}(\id_\mathbb{L})$$

이 성립한다.
:::
::: 증명
임의의 $\sigma\in \Gal(\mathbb{L}/\mathbb{K})$이 주어졌다 하자. 만일 $\sigma\neq\id_\mathbb{L}$이라면 $\sigma(x)\neq x$이도록 하는 $x\in \mathbb{L}$이 존재한다. 그럼 $\mathbb{M}=\mathbb{K}(x)$으로 잡으면 $\sigma\not\in U_\mathbb{M}(\id_\mathbb{L})$이 성립한다. 이제 앞서 살펴본 것과 같이 $\Ext_{\fin,\gal}(\mathbb{L}/\mathbb{K})$가 $\Ext_{\fin}(\mathbb{L}/\mathbb{K})$의 cofinal subset이므로 원하는 결과를 얻는다.
:::

따라서, 이 명제의 결과에 의해 $\id_\mathbb{L}$을 포함하는 connected component는 $\left\{\id_\mathbb{L}\right\}$이다. 한편 [명제 2](#prop2)에 의하여 임의의 $\sigma$에 의한 left translation은 homeomorphism이므로 임의의 점을 포함하는 connected component 또한 한 점이고, 이로부터 $\Gal(\mathbb{L}/\mathbb{K})$이 totally disconnected space임을 안다. ([\[위상수학\] §연결공간, ⁋정의 7](/ko/math/topology/connected_spaces#def7)) 뿐만 아니라 다음이 성립한다.

::: 명제 4
$\Gal(\mathbb{L}/\mathbb{K})$는 compact이다. 
:::
::: 증명
우선 각각의 $x\in \mathbb{L}$에 대하여, $\mathbb{L}/\mathbb{K}$는 algebraic extension이므로 $x$는 algebraic이고, 따라서 $x$와 conjugate한 원소들은 오직 유한 개 뿐이다. ([§갈루아 확장, ⁋명제 3](/ko/math/field_theory/galois_extension#prop3)) 바꿔 말하면, 

$$\Gal(\mathbb{L}/\mathbb{K})\hookrightarrow \prod_{x\in \mathbb{L}}\mathbb{L}\overset{\pr_x}{\longrightarrow}\mathbb{L};\qquad \sigma\mapsto \sigma(x)$$

를 생각하면 이 함수의 image는 유한집합이다. 따라서 $\Gal(\mathbb{L}/\mathbb{K})$는 유한집합들의 곱의 부분집합이며, 유한집합들은 compact이므로 이 곱 또한 compact이다. ([\[위상수학\] §Compactness와 paracompactness, ⁋정리 2 (Tychonoff)](/ko/math/topology/compactness#thm2)) 따라서 주어진 명제를 보이는 것은 $\Gal(\mathbb{L}/\mathbb{K})$이 $\mathbb{L}^\mathbb{L}$에서 closed임을 보이는 것과 같다. 

함수 $u$가 $\Gal(\mathbb{L}/\mathbb{K})$의 $\mathbb{L}^\mathbb{L}$에서의 closure에 포함된다 하자. 우선 $\mathbb{K}$를 fix하는 field homomorphism $u:\mathbb{L}\rightarrow\mathbb{L}$은 언제나 $\Gal(\mathbb{L}/\mathbb{K})$의 원소인데, $u$는 단사이고 임의의 $x\in \mathbb{L}$에 대하여 $x$의 minimal polynomial의 $\mathbb{L}$에서의 해들이 이루는 유한집합을 자기 자신으로 보내므로 그 위에서 전단사이고, 따라서 $x$가 $u$의 image에 속하기 때문이다. 그러므로 만일 $u$가 $\Gal(\mathbb{L}/\mathbb{K})$의 원소가 아니라면, $u$는 field homomorphism이 아니거나 $u$가 $\mathbb{K}$를 fix하지 않아야 한다. 첫 번째 가정을 받아들여, 가령 $u(x+y)\neq u(x)+u(y)$이도록 하는 $x,y\in\mathbb{L}$이 존재한다 하자. 그럼 다음 집합

$$\left\{f\in \mathbb{L}^\mathbb{L}\mid f(x)=u(x),f(y)=u(y),f(x+y)=u(x+y)\right\}$$

은 $\mathbb{L}^\mathbb{L}$의 basis 꼴의 원소이므로 열린집합이고 뿐만 아니라 $u$를 포함한다. 즉, 이 집합은 $u$의 open neighborhood이다. 그런데 가정에서

$$f(x+y)=u(x+y)\neq u(x)+u(y)=f(x)+f(y)$$

이므로 $f$들 또한 field homomorphism이 되지 않는다. 즉, 위의 open neighborhood는 $\Gal(\mathbb{L}/\mathbb{K})$와 만나지 않고 이는 $u$가 $\Gal(\mathbb{L}/\mathbb{K})$의 closure에 속한다는 가정에 모순이다. 비슷한 논리로 다른 경우의 수 또한 모두 배제할 수 있으며 이로부터 $\Gal(\mathbb{L}/\mathbb{K})$이 $\mathbb{L}^\mathbb{L}$에서 closed임을 증명할 수 있다.
:::

한편 $\mathbb{L}/\mathbb{K}$이 Galois extension이라 하고, 이 extension의 Galois subextension $\mathbb{L}_i/\mathbb{K}$들이 $\mathbb{L}=\bigcup_{i\in I}\mathbb{L}_i$를 만족하며, 임의의 $i,j\in I$에 대하여 $\mathbb{L}_i\cup\mathbb{L}_j\subseteq \mathbb{L}_k$이도록 하는 $k\in I$이 존재한다 하자. 그럼 우리는 이 위에 partial order

$$i\leq j \iff \mathbb{L}_i\subseteq \mathbb{L}_j$$

를 주고, 이러한 partial order 하에서 다음의 restriction map들

$$\rho_{ij}:\Gal(\mathbb{L}_j/\mathbb{K}) \rightarrow \Gal(\mathbb{L}_i/\mathbb{K})\qquad \text{whenever $i\leq j$}$$

을 정의할 수 있다. 그럼 이들은 continuous homomorphism이며, 따라서 이들의 inverse limit

$$\varprojlim_{i\in I}\Gal(\mathbb{L}_i/\mathbb{K})=\left\{(\sigma_i)\in\prod_{i\in I}\Gal(\mathbb{L}_i/\mathbb{K})\mid\text{$\rho_{ij}(\sigma_j)=\sigma_i$ whenever $i\leq j$}\right\}$$

과 canonical morphism들 $\rho_i:\varprojlim \Gal(\mathbb{L}_i/\mathbb{K})\rightarrow\Gal(\mathbb{L}_i/\mathbb{K})$들이 존재한다. ([\[범주론\] §극한, ⁋예시 5](/ko/math/category_theory/limits#ex5)) 

한편 restriction map들

$$\lambda_i:\Gal(\mathbb{L}/\mathbb{K})\rightarrow\Gal(\mathbb{L}_i/\mathbb{K})$$

을 생각하면, 이들은 $\lambda_i=\rho_{ij}\circ\lambda_j$를 만족하므로 이들이 유도하는 continuous homomorphism $\lambda:\Gal(\mathbb{L}/\mathbb{K})\rightarrow\varprojlim\Gal(\mathbb{L}_i/\mathbb{K})$이 존재한다. 

::: 명제 5
위에서 정의한 $\lambda$는 topological group들 사이의 isomorphism을 정의한다. 
:::
::: 증명
각각의 $\Gal(\mathbb{L}_i/\mathbb{K})$은 Hausdorff space $\mathbb{L}_i^{\mathbb{L}_i}$의 부분공간이므로 Hausdorff이며, Hausdorff space의 곱과 부분공간은 다시 Hausdorff이므로 이들의 inverse limit $\varprojlim \Gal(\mathbb{L}_i/\mathbb{K})$ 또한 Hausdorff이다. 한편 [명제 4](#prop4)에서 $\Gal(\mathbb{L}/\mathbb{K})$이 compact이므로, [\[위상수학\] §옹골공간, ⁋명제 9](/ko/math/topology/compact_spaces#prop9)에 의하여 주장은 $\lambda$가 전단사임만 보이면 충분하다.

우선 $\lambda(\sigma)$가 항등원이라면 임의의 $i$에 대하여 $\sigma\vert_{\mathbb{L}_i}=\id_{\mathbb{L}_i}$이고, $\mathbb{L}=\bigcup_i\mathbb{L}_i$이므로 $\sigma=\id_\mathbb{L}$이다. 즉 $\lambda$는 단사이다. 이제 $(\sigma_i)\in\varprojlim\Gal(\mathbb{L}_i/\mathbb{K})$이 주어졌다 하고, $x\in \mathbb{L}_i$에 대하여 $\sigma(x)=\sigma_i(x)$로 정의하자. 만일 $x$가 $\mathbb{L}_i$와 $\mathbb{L}_j$에 모두 속한다면 $\mathbb{L}_i\cup\mathbb{L}_j\subseteq \mathbb{L}_k$인 $k$를 잡을 때 $\sigma_i(x)=\rho_{ik}(\sigma_k)(x)=\sigma_k(x)$이고 같은 이유로 $\sigma_j(x)=\sigma_k(x)$이므로 $\sigma$가 잘 정의되며, $\mathbb{L}$의 임의의 두 원소 또한 하나의 $\mathbb{L}_k$에 함께 속하므로 $\sigma$는 $\mathbb{K}$를 fix하는 field homomorphism이다. 한편 $\rho_{ij}$들이 homomorphism이므로 $(\sigma_i^{-1})$ 또한 $\varprojlim\Gal(\mathbb{L}_i/\mathbb{K})$의 원소이고, 같은 방식으로 얻어지는 함수가 $\sigma$의 역함수가 된다. 즉 $\sigma\in\Gal(\mathbb{L}/\mathbb{K})$이며 $\lambda(\sigma)=(\sigma_i)$이므로 $\lambda$는 전사이다.
:::

특히 finite degree Galois subextension들의 family $\Ext_{\fin,\gal}(\mathbb{L}/\mathbb{K})$는 이 명제의 조건을 만족한다. 이 family의 두 원소의 compositum은 [§갈루아 확장, ⁋명제 10](/ko/math/field_theory/galois_extension#prop10)에 의해 다시 finite degree Galois subextension이고, $\mathbb{L}$의 임의의 원소 $x$는 $\mathbb{K}(x)$를 포함하는 $\Ext_{\fin,\gal}(\mathbb{L}/\mathbb{K})$의 원소에 속하기 때문이다. 즉 임의의 Galois extension의 Galois group은 유한한 group들의 inverse limit, 곧 *profinite group*이다. 

## 갈루아 코호몰로지

Galois group은 단순한 group이 아니라 $\mathbb{L}$에, 특히 multiplicative group $\mathbb{L}^\times$에 작용하는 group이다. 이 action이 담고 있는 산술적인 정보를 뽑아내는 표준적인 도구가 *Galois cohomology*인데, 이 글을 마치며 그 출발점에 있는 고전적인 정리인 Hilbert의 정리 90을 살펴본다. 이번 절에서 $\mathbb{L}/\mathbb{K}$는 finite degree Galois extension이고 $G=\Gal(\mathbb{L}/\mathbb{K})$이다.

::: 정의 6
함수 $\varphi:G \rightarrow \mathbb{L}^\times$가 *1-cocycle<sub>1-코사이클</sub>*이라는 것은 임의의 $\sigma,\tau\in G$에 대하여 다음의 식

$$\varphi(\sigma\tau)=\varphi(\sigma)\cdot\sigma\bigl(\varphi(\tau)\bigr)$$

이 성립하는 것이다. 특별히 어떤 $c\in\mathbb{L}^\times$에 대하여 $\varphi(\sigma)=\sigma(c)/c$의 꼴로 쓰여지는 1-cocycle을 *1-coboundary<sub>1-코바운더리</sub>*라 부른다.
:::

우선 1-coboundary가 실제로 1-cocycle인 것을 확인하면

$$\varphi(\sigma)\cdot\sigma(\varphi(\tau))=\frac{\sigma(c)}{c}\cdot\sigma\left(\frac{\tau(c)}{c}\right)=\frac{\sigma(c)}{c}\cdot\frac{\sigma\tau(c)}{\sigma(c)}=\frac{\sigma\tau(c)}{c}=\varphi(\sigma\tau)$$

이다. 또, $\mathbb{L}^\times$가 abelian이므로 1-cocycle들은 pointwise multiplication에 대해 abelian group을 이루고, $c\mapsto(\sigma\mapsto\sigma(c)/c)$가 group homomorphism이므로 1-coboundary들은 그 subgroup을 이룬다. 따라서 quotient group을 생각할 수 있으며, 이를 $H^1(G,\mathbb{L}^\times)$로 적는다. Hilbert의 정리 90은 이 group이 아무 정보도 담고 있지 않다는 것이다.

::: 정리 7 (Hilbert 90)
Finite degree Galois extension $\mathbb{L}/\mathbb{K}$에 대하여, 임의의 1-cocycle $\varphi:G \rightarrow \mathbb{L}^\times$는 1-coboundary이다. 즉 $H^1(G,\mathbb{L}^\times)$는 자명하다.
:::
::: 증명
$G$의 원소들은 $\mathbb{L}$에서 $\mathbb{L}$로의 서로 다른 homomorphism들이므로, [§에탈대수, ⁋따름정리 3](/ko/math/field_theory/etale_algebras#cor3)에 의하여 $\mathbb{L}$-벡터공간 안에서 일차독립이다. $\varphi$의 값들은 모두 $0$이 아니므로, 일차결합

$$\sum_{\tau\in G}\varphi(\tau)\tau$$

는 zero map이 아니고, 따라서 적당한 $x\in\mathbb{L}$에 대하여

$$b=\sum_{\tau\in G}\varphi(\tau)\tau(x)\neq0$$

이다. 이제 임의의 $\sigma\in G$에 대하여, cocycle 조건을 $\sigma(\varphi(\tau))=\varphi(\sigma)^{-1}\varphi(\sigma\tau)$로 적고 계산하면

$$\sigma(b)=\sum_{\tau\in G}\sigma(\varphi(\tau))\sigma\tau(x)=\varphi(\sigma)^{-1}\sum_{\tau\in G}\varphi(\sigma\tau)\sigma\tau(x)=\varphi(\sigma)^{-1}b$$

이다. 마지막 등식은 $\tau$가 $G$ 전체를 움직일 때 $\sigma\tau$도 $G$ 전체를 움직이기 때문이다. 따라서 $c=b^{-1}$로 두면

$$\varphi(\sigma)=\frac{b}{\sigma(b)}=\frac{\sigma(c)}{c}$$

이므로 $\varphi$는 1-coboundary이다.
:::

고전적인 형태의 Hilbert 90은 cyclic extension에 대한 것이다. $G=\langle\sigma\rangle$가 order $n$의 cyclic group이라 하고, $x\in\mathbb{L}$의 *norm*을

$$N_{\mathbb{L}/\mathbb{K}}(x)=\prod_{i=0}^{n-1}\sigma^i(x)$$

으로 정의하자. $\sigma$를 적용하면 인수들이 자리바꿈만 하므로 $N_{\mathbb{L}/\mathbb{K}}(x)$는 $G$-invariant이고, $\mathbb{L}/\mathbb{K}$가 Galois이므로 [§갈루아 확장, ⁋정리 8](/ko/math/field_theory/galois_extension#thm8)에 의하여 $N_{\mathbb{L}/\mathbb{K}}(x)\in\mathbb{K}$이다.

::: 따름정리 8
$\mathbb{L}/\mathbb{K}$가 finite degree Galois extension이고 $G=\Gal(\mathbb{L}/\mathbb{K})=\langle\sigma\rangle$가 cyclic이라 하자. 그럼 $x\in\mathbb{L}^\times$에 대하여 다음이 동치이다.

1. $N_{\mathbb{L}/\mathbb{K}}(x)=1$.
2. 적당한 $y\in\mathbb{L}^\times$가 존재하여 $x=\sigma(y)/y$이다.
:::
::: 증명
우선 둘째 조건을 가정하면

$$N_{\mathbb{L}/\mathbb{K}}\bigl(\sigma(y)/y\bigr)=\prod_{i=0}^{n-1}\frac{\sigma^{i+1}(y)}{\sigma^i(y)}=\frac{\sigma^n(y)}{y}=1$$

이다. 가운데 등식은 telescoping이고 마지막 등식은 $\sigma^n=\id_\mathbb{L}$ 때문이다.

거꾸로 $N_{\mathbb{L}/\mathbb{K}}(x)=1$이라 가정하자. 함수 $\varphi:G \rightarrow \mathbb{L}^\times$를

$$\varphi(\sigma^i)=\prod_{k=0}^{i-1}\sigma^k(x)\qquad(0\leq i\leq n-1)$$

으로 정의하자. 여기서 $i=0$일 때는 빈 곱으로 $\varphi(\id)=1$이다. 이것이 1-cocycle임을 확인하자. $0\leq a,b\leq n-1$에 대하여

$$\varphi(\sigma^a)\cdot\sigma^a\bigl(\varphi(\sigma^b)\bigr)=\prod_{k=0}^{a-1}\sigma^k(x)\cdot\prod_{k=0}^{b-1}\sigma^{a+k}(x)=\prod_{k=0}^{a+b-1}\sigma^k(x)$$

이다. 만일 $a+b\leq n-1$이라면 이는 정의에 의해 $\varphi(\sigma^{a+b})=\varphi(\sigma^a\sigma^b)$이다. 만일 $a+b\geq n$이라면 $\sigma^k=\sigma^{k-n}$ ($k\geq n$)이므로

$$\prod_{k=0}^{a+b-1}\sigma^k(x)=\prod_{k=0}^{n-1}\sigma^k(x)\cdot\prod_{k=n}^{a+b-1}\sigma^k(x)=N_{\mathbb{L}/\mathbb{K}}(x)\cdot\prod_{k=0}^{a+b-n-1}\sigma^k(x)=\varphi(\sigma^{a+b-n})$$

이고, $\sigma^a\sigma^b=\sigma^{a+b-n}$이므로 역시 cocycle 조건이 성립한다. 마지막 등식에서 가정 $N_{\mathbb{L}/\mathbb{K}}(x)=1$이 사용되었다.

이제 [정리 7](#thm7)에 의하여 $\varphi$는 1-coboundary이다. 즉 적당한 $c\in\mathbb{L}^\times$에 대하여 $\varphi(\sigma^i)=\sigma^i(c)/c$이고, 특히 $i=1$에서

$$x=\varphi(\sigma)=\frac{\sigma(c)}{c}$$

이므로 $y=c$로 두면 된다.
:::

---

**참고문헌**

**[Bou]** N. Bourbaki. *Algebra II: Chapters 4–7*. Springer, 2003.  

---

