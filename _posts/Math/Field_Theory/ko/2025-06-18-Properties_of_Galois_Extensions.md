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

우리는 앞서 Galois extension과 Galois group을 정의했다. Galois theory의 핵심적인 결과는 field extension $$\mathbb{L}/\mathbb{K}$$에 대하여 Galois group $$\Gal(\mathbb{L}/\mathbb{K})$$의 subgroup들의 lattice와, $$\mathbb{L}/\mathbb{K}$$의 Galois subextension들의 lattice 사이에 order-preserving bijection이 존재한다는 것이다. 많은 경우에 이 결과는 Galois group $$\Gal(\mathbb{L}/\mathbb{K})$$이 유한한 경우만 다루지만, 우리는 $$\Gal(\mathbb{L}/\mathbb{K})$$가 무한할 경우 또한 다룰 것이므로 이를 위해서는 $$\Gal(\mathbb{L}/\mathbb{K})$$에 적절한 위상구조를 주어야 한다. 

## 갈루아 군의 위상구조

Galois extension $$\mathbb{L}/\mathbb{K}$$이 주어졌다 하고, $$\Gal(\mathbb{L}/\mathbb{K})$$이 이 extension의 Galois group이라 하자. Galois group은 어쨌든 집합 $$\mathbb{L}$$에서 $$\mathbb{L}$$로 가는 함수들의 모임이므로 우리는 $$\mathbb{L}$$에서 $$\mathbb{L}$$로의 함수들의 모임 $$\Fun(\mathbb{L},\mathbb{L})=\mathbb{L}^\mathbb{L}$$에 위상구조를 준다면 이 집합의 부분집합으로서 $$\Gal(\mathbb{L}/\mathbb{K})$$에 위상구조를 줄 수 있다. ([\[위상수학\] §부분공간, ⁋정의 1](/ko/math/topology/subspaces#def1)) 

이를 위해 $$\mathbb{L}$$ 위에 discrete topology를 부여하자. ([\[위상수학\] §열린집합, ⁋예시 2](/ko/math/topology/open_sets#ex2)) 우리는 [\[위상수학\] §곱공간](/ko/math/topology/product_spaces)의 결과로부터 이 집합의 subbase는 다음과 같은 꼴

$$U_{x,y}=\left\{\sigma\mid\sigma(x)=y \right\}$$

로 쓸 수 있는 집합들의 모임임을 알고 있으므로, $$\Gal(\mathbb{L}/\mathbb{K})$$에 subspace topology를 부여하면 임의의 $$\sigma\in\Gal(\mathbb{L}/\mathbb{K})$$에 대하여 다음과 같은 형태

$$U_{x_1,\ldots,x_n}=\left\{\tau\in\Gal(\mathbb{L}/\mathbb{K})\mid \text{$\tau(x_i)=\sigma(x_i)$ for all $i$}\right\}$$

의 집합들의 모임이 $$\sigma$$에서의 local base임을 안다. ([\[위상수학\] §위상공간의 기저, ⁋정의 4](/ko/math/topology/topological_bases#def4)) 

한편 위의 조건을 만족하는 함수들은 $$\mathbb{L}$$의 finite subextension $$\mathbb{M}=\mathbb{L}(x_1,\ldots,x_n )$$으로 제한했을 때 $$\sigma$$와 일치하는 함수들이며, 거꾸로 임의의 finite subextension $$\mathbb{M}/\mathbb{K}$$은 이러한 방식으로 $$\sigma$$의 local base의 원소를 하나 정의한다. 즉 $$\Lambda$$를 extension $$\mathbb{L}/\mathbb{K}$$의 *finite* subextension들의 모임이라 하고 임의의 $$\mathbb{M}/\mathbb{K}\in \Lambda$$와 임의의 $$\sigma\in \Gal(\mathbb{L}/\mathbb{K})$$에 대하여, $$\Gal(\mathbb{L}/\mathbb{K})$$의 부분집합 $$U_\mathbb{M}(\sigma)$$를 다음의 식 

$$U_\mathbb{M}(\sigma)=\left\{\tau\in \Gal(\mathbb{L}/\mathbb{K})\mid \sigma\vert_\mathbb{M}=\tau\vert_\mathbb{M}\right\}$$

으로 정의하면 이 집합은 $$\sigma$$의 local base의 원소가 되며, 이들을 모아둔 $$(U_\mathbb{M}(\sigma))_{\sigma\in\Lambda}$$가 정확히 $$\sigma$$에서의 local base이다.
  
<div class="example" markdown="1">

<ins id="ex1">**예시 1**</ins> 특별히 $$\mathbb{L}/\mathbb{K}$$이 finite degree Galois extension인 경우를 생각하자. 그럼 [§갈루아 확장, ⁋정의 12](/ko/math/field_theory/galois_extension#def12)이후의 논의로부터 우리는 $$\Gal(\mathbb{L}/\mathbb{K})$$이 유한집합인 것을 안다. 한편 위의 local base로부터, $$\mathbb{L}/\mathbb{K}$$이 finite degree이므로 $$\mathbb{L}/\mathbb{K}$$가 이미 $$\Lambda$$의 원소이고 따라서

$$U_\mathbb{L}(\sigma)=\left\{\tau\in\Gal(\mathbb{L}/\mathbb{K})\mid \sigma\vert_\mathbb{L}=\tau\vert_\mathbb{L}\right\}=\left\{\sigma\right\}$$

이므로 이 경우 $$\Gal(\mathbb{L}/\mathbb{K})$$는 discrete topology가 주어진 집합이 된다. 

</div>

한편, 위와 같이 정의한 위상공간 $$\Gal(\mathbb{L}/\mathbb{K})$$는 원래 $$\mathbb{K}$$-automorphism들의 합성을 연산으로 갖는 group이며, 이 때 함수들의 합성이 이 위상구조와 잘 어울리는 것을 어렵지 않게 보일 수 있다. 
  
<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> 위에서 정의한 $$\Gal(\mathbb{L}/\mathbb{K})$$는 topological group이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

즉 두 homomorphism 

$$\Gal(\mathbb{L}/\mathbb{K})\times\Gal(\mathbb{L}/\mathbb{K})\rightarrow\Gal(\mathbb{L}/\mathbb{K});\quad (\sigma,\sigma')\mapsto \sigma\sigma',\qquad \Gal(\mathbb{L}/\mathbb{K})\rightarrow\Gal(\mathbb{L}/\mathbb{K});\quad \sigma\mapsto \sigma^{-1}$$

이 연속임을 보여야한다. 우선 $$\sigma\sigma'$$의 임의의 local base의 원소 $$U_\mathbb{M}(\sigma\sigma')$$를 생각하면 정의에 의하여

$$U_\mathbb{M}(\sigma\sigma')=\left\{\tau\in\Gal(\mathbb{L}/\mathbb{K})\mid \tau\vert_\mathbb{M}=\sigma\sigma'\vert_\mathbb{M}\right\}$$

이며 따라서 당연한 이유로 $$\Gal(\mathbb{L}/\mathbb{K})\times\Gal(\mathbb{L}/\mathbb{K})$$의 열린집합 $$U_\mathbb{M}(\sigma)\times U_\mathbb{M}(\sigma')$$는 위의 집합의 preimage에 속하고 따라서 multiplication map은 연속이다. 

비슷한 방식으로 $$\sigma^{-1}$$의 local base $$U_\mathbb{M}(\sigma^{-1})$$은 다음의 식 

$$U_\mathbb{M}(\sigma^{-1})=\left\{\tau\in\Gal(\mathbb{L}/\mathbb{K})\mid \tau\vert_\mathbb{M}=\sigma^{-1}\vert_\mathbb{M}\right\}$$

으로 주어지며, 이 때 $$\sigma$$의 local base $$U_\mathbb{M}(\sigma)$$를 생각하면 이 집합은 위의 집합의 preimage에 속한다. 

</details>

특히 임의의 $$\sigma$$에서의 local base는 identity $$\id_\mathbb{L}$$의 local base를 translation map을 따라 옮긴 것으로 주어진다. 즉 임의의 $$\sigma\in \Gal(\mathbb{L}/\mathbb{K})$$에 대하여 다음의 식

$$U_\mathbb{M}(\sigma)=U_\mathbb{M}(\id_\mathbb{L})\sigma=\sigma U_\mathbb{M}(\id_\mathbb{L})$$

이 성립한다. 이로부터 우리는 위의 집합 대신 다음의 집합

$$U_\mathbb{M}(\id_\mathbb{L})=\left\{\tau\in \Gal(\mathbb{L}/\mathbb{K})\mid \tau\vert_\mathbb{M}=\id_\mathbb{M}\right\}$$

만 살펴보아도 되는 것을 안다. 그럼 

$$U_\mathbb{M}(\id_\mathbb{L})\subseteq U_\mathbb{N}(\id_\mathbb{L})\iff \mathbb{M}\supseteq \mathbb{N}$$

이며, 위의 표기로부터 집합으로서는

$$U_\mathbb{M}(\id_\mathbb{L})=\Gal(\mathbb{L}/\mathbb{M})$$

인 것을 안다. 이 때 우측의 inclusion은 단순히 $$\mathbb{M}$$-automorphism을 $$\mathbb{K}$$-automorphism으로 보아 얻어지는 것이며, 뿐만 아니라 $$\Gal(\mathbb{L}/\mathbb{M})$$에 정의된 위상구조가 정확히 $$U_\mathbb{M}(\id_\mathbb{L})$$과 같다는 것을 안다. 

이제 finite degree *Galois* extension들의 모임 $$\Lambda'$$를 생각하면 [§갈루아 확장, ⁋명제 11](/ko/math/field_theory/galois_extension#prop11)에 의해 이것이 $$\Lambda$$의 cofinal subset임을 안다. 즉 $$(U_\mathbb{M}(\id_\mathbb{L}))_{\mathbb{M}\in\Lambda}$$도 $$\id_\mathbb{L}$$의 local base이다. 그럼 임의의 $$\mathbb{M}\in \Lambda'$$에 대하여 [§갈루아 확장, ⁋명제 13](/ko/math/field_theory/galois_extension#prop13)에서 살펴보았던 restriction homomorphism $$\rho:\Gal(\mathbb{L}/\mathbb{K})\rightarrow\Gal(\mathbb{M}/\mathbb{K})$$을 생각하면, $$\mathbb{M}$$의 임의의 finite degree subextension은 $$\mathbb{L}$$의 finite degree subextension이기도 하므로 이 restriction homomorphism은 위에서 정의한 위상구조에 대하여 연속이다. 이와 같은 상황에서 $$\rho$$는 $$\Gal(\mathbb{L}/\mathbb{K})$$에서 finite discrete space $$\Gal(\mathbb{M}/\mathbb{K})$$로의 연속함수이므로 ([예시 1](#ex1)), $$\ker\rho$$는 $$\Gal(\mathbb{L}/\mathbb{K})$$의 closed subgroup이다. 그런데 정의에 의해 

$$\sigma\in\ker\rho\iff \sigma\vert_\mathbb{M}=\id\vert_\mathbb{M}\iff\sigma\in U_\mathbb{M}(\id_\mathbb{L})$$

이므로 각각의 $$U_\mathbb{M}(\id_\mathbb{L})$$들은 clopen이다. 한편 임의의 clopen set은 항상 connected component들의 합집합으로 쓸 수 있고, 따라서 clopen set들의 공집합이 아닌 임의의 교집합은 connected component를 포함해야 한다. 그러나 다음이 성립한다. 

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> 위의 상황에서 다음의 식 

$$\{\id_\mathbb{L}\}=\bigcap_{\mathbb{M}\in \Lambda'}U_\mathbb{M}(\id_\mathbb{L})$$

이 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

임의의 $$\sigma\in \Gal(\mathbb{L}/\mathbb{K})$$이 주어졌다 하자. 만일 $$\sigma\neq\id_\mathbb{L}$$이라면 $$\sigma(x)\neq x$$이도록 하는 $$x\in \mathbb{L}$$이 존재한다. 그럼 $$\mathbb{M}=\mathbb{K}(x)$$으로 잡으면 $$\sigma\not\in U_\mathbb{M}(\id_\mathbb{L})$$이 성립한다. 이제 앞서 살펴본 것과 같이 $$\Lambda'$$이 $$\Lambda$$의 cofinal subset이므로 원하는 결과를 얻는다.

</details>

따라서, 이 명제의 결과에 의해 $$\id_\mathbb{L}$$을 포함하는 connected component는 $$\left\{\id_\mathbb{L}\right\}$$이며, 이로부터 $$\Gal(\mathbb{L}/\mathbb{K})$$이 totally disconnected space임을 안다. ([\[위상수학\] §연결공간, ⁋정의 7](/ko/math/topology/connected_spaces#def7)) 뿐만 아니라 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> $$\Gal(\mathbb{L}/\mathbb{K})$$는 compact이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 각각의 $$x\in \mathbb{L}$$에 대하여, $$\mathbb{L}/\mathbb{K}$$는 algebraic extension이므로 $$x$$는 algebraic이고, 따라서 $$x$$와 conjugate한 원소들은 오직 유한 개 뿐이다. ([§갈루아 확장, ⁋명제 3](/ko/math/field_theory/galois_extension#prop3)) 바꿔 말하면, 

$$\Gal(\mathbb{L}/\mathbb{K})\hookrightarrow \prod_{x\in \mathbb{L}}\mathbb{L}\overset{\pr_x}{\longrightarrow}\mathbb{L};\qquad \sigma\mapsto \sigma(x)$$

를 생각하면 이 함수의 image는 유한집합이다. 따라서 $$\Gal(\mathbb{L}/\mathbb{K})$$는 유한집합들의 곱의 부분집합이며, 유한집합들은 compact이므로 이 곱 또한 compact이다. ([\[위상수학\] §옹골성, ⁋정리 2](/ko/math/topology/compactness#thm2)) 따라서 주어진 명제를 보이는 것은 $$\Gal(\mathbb{L}/\mathbb{K})$$이 $$\mathbb{L}^\mathbb{L}$$에서 closed임을 보이는 것과 같다. 

함수 $$u$$가 $$\Gal(\mathbb{L}/\mathbb{K})$$의 $$\mathbb{L}^\mathbb{L}$$에서의 closure에 포함된다 하자. 만일 $$u$$가 $$\Gal(\mathbb{L}/\mathbb{K})$$의 원소가 아니라면, $$u$$는 field homomorphism이 아니거나 $$u$$가 $$\mathbb{K}$$를 fix하지 않아야 한다. 첫 번째 가정을 받아들여, 가령 $$u(x+y)\neq u(x)+u(y)$$이도록 하는 $$x,y\in\mathbb{L}$$이 존재한다 하자. 그럼 다음 집합

$$\left\{f\in \mathbb{L}^\mathbb{L}\mid f(x)=u(x),f(y)=u(y),f(x+y)=u(x+y)\right\}$$

은 $$\mathbb{L}^\mathbb{L}$$의 basis 꼴의 원소이므로 열린집합이고 뿐만 아니라 $$u$$를 포함한다. 즉, 이 집합은 $$u$$의 open neighborhood이다. 그런데 가정에서

$$f(x+y)=u(x+y)\neq u(x)+u(y)=f(x)+f(y)$$

이므로 $$f$$들 또한 field homomorphism이 되지 않는다. 즉, 위의 open neighborhood는 $$\Gal(\mathbb{L}/\mathbb{K})$$와 만나지 않고 이는 $$u$$가 $$\Gal(\mathbb{L}/\mathbb{K})$$의 closure에 속한다는 가정에 모순이다. 비슷한 논리로 다른 경우의 수 또한 모두 배제할 수 있으며 이로부터 $$\Gal(\mathbb{L}/\mathbb{K})$$이 $$\mathbb{L}^\mathbb{L}$$에서 closed임을 증명할 수 있다.

</details>

한편 $$\mathbb{L}/\mathbb{K}$$이 Galois extension이라 하고, 이 extension의 Galois subextension $$\mathbb{L}_i/\mathbb{K}$$들이 $$\mathbb{L}=\bigcup_{i\in I}\mathbb{L}_i$$를 만족한다 하자. 그럼 우리는 이 위에 partial order

$$i\leq j \iff \mathbb{L}_i\subset \mathbb{L}_j$$

를 주고, 이러한 partial order 하에서 다음의 restriction map들

$$\rho_{ij}:\Gal(\mathbb{L}_j/\mathbb{K}) \rightarrow \Gal(\mathbb{L}_i/\mathbb{K})\qquad \text{whenever $i\leq j$}$$

을 정의할 수 있다. 그럼 이들은 continuous homomorphism이며, 따라서 이들의 inverse limit

$$\varprojlim_{i\in I}\Gal(\mathbb{L}_i/\mathbb{K})$$

과 canonical morphism들 $$\rho_i:\varprojlim \Gal(\mathbb{L}_i/\mathbb{K})\rightarrow\Gal(\mathbb{L}_i/\mathbb{K})$$들이 존재한다. 

한편 restriction map들

$$\lambda_i:\Gal(\mathbb{L}/\mathbb{K})\rightarrow\Gal(\mathbb{L}_i/\mathbb{K})$$

을 생각하면, 이들은 $$\lambda_i=\rho_{ij}\circ\lambda_j$$를 만족하므로 이들이 유도하는 continuous homomorphism $$\lambda:\Gal(\mathbb{L}/\mathbb{K})\rightarrow\varprojlim\Gal(\mathbb{L}_i/\mathbb{K})$$이 존재한다. 

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> 위에서 정의한 $$\lambda$$는 topological group들 사이의 isomorphism을 정의한다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[명제 3](#prop3)에 의하여 $$\Gal(\mathbb{L}_i/\mathbb{K})$$이 Hausdorff이며, Hausdorff space의 곱과 부분공간은 다시 Hausdorff이므로 이들의 inverse limit $$\varprojlim \Gal(\mathbb{L}_i/\mathbb{K})$$ 또한 Hausdorff이다. 한편 [명제 4](#prop4)에서 $$\Gal(\mathbb{L}/\mathbb{K})$$이 compact이므로, [\[위상수학\] §옹골공간, ⁋명제 9](/ko/math/topology/compact_spaces#prop9)에 의하여 주장은 $$\lambda$$가 전단사임만 보이면 충분하며, 이는 $$\mathbb{L}= \bigcup \mathbb{L}_i$$로부터 거의 자명하다.

</details>

특히 이 명제는 family $$\Lambda'$$에 대하여 잘 적용된다. 

## 갈루아 코호몰로지

Galois group은 단순한 group이 아니라 $$\mathbb{L}$$에, 특히 multiplicative group $$\mathbb{L}^\times$$에 작용하는 group이다. 이 작용이 담고 있는 산술적인 정보를 뽑아내는 표준적인 도구가 *Galois cohomology*인데, 이 글을 마치며 그 출발점에 있는 고전적인 정리인 Hilbert의 정리 90을 살펴본다. 이번 절에서 $$\mathbb{L}/\mathbb{K}$$는 finite degree Galois extension이고 $$G=\Gal(\mathbb{L}/\mathbb{K})$$이다.

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> 함수 $$\varphi:G \rightarrow \mathbb{L}^\times$$가 *1-cocycle<sub>1-코사이클</sub>*이라는 것은 임의의 $$\sigma,\tau\in G$$에 대하여 다음의 식

$$\varphi(\sigma\tau)=\varphi(\sigma)\cdot\sigma\bigl(\varphi(\tau)\bigr)$$

이 성립하는 것이다. 특별히 어떤 $$c\in\mathbb{L}^\times$$에 대하여 $$\varphi(\sigma)=\sigma(c)/c$$의 꼴로 쓰여지는 1-cocycle을 *1-coboundary<sub>1-코바운더리</sub>*라 부른다.

</div>

우선 1-coboundary가 실제로 1-cocycle인 것을 확인하면

$$\varphi(\sigma)\cdot\sigma(\varphi(\tau))=\frac{\sigma(c)}{c}\cdot\sigma\left(\frac{\tau(c)}{c}\right)=\frac{\sigma(c)}{c}\cdot\frac{\sigma\tau(c)}{\sigma(c)}=\frac{\sigma\tau(c)}{c}=\varphi(\sigma\tau)$$

이다. 또, 1-cocycle들은 pointwise 곱셈에 대해 abelian group을 이루고 1-coboundary들은 그 subgroup을 이루므로 quotient group을 생각할 수 있으며, 이를 $$H^1(G,\mathbb{L}^\times)$$로 적는다. Hilbert의 정리 90은 이 group이 아무 정보도 담고 있지 않다는, 다소 김빠지지만 대단히 유용한 정리이다.

<div class="proposition" markdown="1">

<ins id="thm7">**정리 7 (Hilbert 90)**</ins> Finite degree Galois extension $$\mathbb{L}/\mathbb{K}$$에 대하여, 임의의 1-cocycle $$\varphi:G \rightarrow \mathbb{L}^\times$$는 1-coboundary이다. 즉 $$H^1(G,\mathbb{L}^\times)$$는 자명하다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$G$$의 원소들은 $$\mathbb{L}$$에서 $$\mathbb{L}$$로의 서로 다른 homomorphism들이므로, [§에탈대수, ⁋따름정리 3](/ko/math/field_theory/etale_algebras#cor3)의 Dedekind 정리에 의하여 $$\mathbb{L}$$-벡터공간 안에서 일차독립이다. $$\varphi$$의 값들은 모두 $$0$$이 아니므로, 일차결합

$$\sum_{\tau\in G}\varphi(\tau)\,\tau$$

는 zero map이 아니고, 따라서 적당한 $$x\in\mathbb{L}$$에 대하여

$$b=\sum_{\tau\in G}\varphi(\tau)\,\tau(x)\neq0$$

이다. 이제 임의의 $$\sigma\in G$$에 대하여, cocycle 조건을 $$\sigma(\varphi(\tau))=\varphi(\sigma)^{-1}\varphi(\sigma\tau)$$로 적고 계산하면

$$\sigma(b)=\sum_{\tau\in G}\sigma(\varphi(\tau))\,\sigma\tau(x)=\varphi(\sigma)^{-1}\sum_{\tau\in G}\varphi(\sigma\tau)\,\sigma\tau(x)=\varphi(\sigma)^{-1}b$$

이다. 마지막 등식은 $$\tau$$가 $$G$$ 전체를 움직일 때 $$\sigma\tau$$도 $$G$$ 전체를 움직이기 때문이다. 따라서 $$c=b^{-1}$$로 두면

$$\varphi(\sigma)=\frac{b}{\sigma(b)}=\frac{\sigma(c)}{c}$$

이므로 $$\varphi$$는 1-coboundary이다.

</details>

고전적인 형태의 Hilbert 90은 cyclic extension에 대한 것이다. $$G=\langle\sigma\rangle$$가 order $$n$$의 cyclic group이라 하고, $$x\in\mathbb{L}$$의 *norm*을

$$N_{\mathbb{L}/\mathbb{K}}(x)=\prod_{i=0}^{n-1}\sigma^i(x)$$

으로 정의하자. $$\sigma$$를 적용하면 인수들이 자리바꿈만 하므로 $$N_{\mathbb{L}/\mathbb{K}}(x)$$는 $$G$$-invariant이고, $$\mathbb{L}/\mathbb{K}$$가 Galois이므로 [§갈루아 확장, ⁋정리 8](/ko/math/field_theory/galois_extension#thm8)에 의하여 $$N_{\mathbb{L}/\mathbb{K}}(x)\in\mathbb{K}$$이다.

<div class="proposition" markdown="1">

<ins id="cor8">**따름정리 8**</ins> $$\mathbb{L}/\mathbb{K}$$가 finite degree Galois extension이고 $$G=\Gal(\mathbb{L}/\mathbb{K})=\langle\sigma\rangle$$가 cyclic이라 하자. 그럼 $$x\in\mathbb{L}^\times$$에 대하여 다음이 동치이다.

1. $$N_{\mathbb{L}/\mathbb{K}}(x)=1$$.
2. 적당한 $$y\in\mathbb{L}^\times$$가 존재하여 $$x=\sigma(y)/y$$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 둘째 조건을 가정하면

$$N_{\mathbb{L}/\mathbb{K}}\bigl(\sigma(y)/y\bigr)=\prod_{i=0}^{n-1}\frac{\sigma^{i+1}(y)}{\sigma^i(y)}=\frac{\sigma^n(y)}{y}=1$$

이다. 가운데 등식은 telescoping이고 마지막 등식은 $$\sigma^n=\id_\mathbb{L}$$ 때문이다.

거꾸로 $$N_{\mathbb{L}/\mathbb{K}}(x)=1$$이라 가정하자. 함수 $$\varphi:G \rightarrow \mathbb{L}^\times$$를

$$\varphi(\sigma^i)=\prod_{k=0}^{i-1}\sigma^k(x)\qquad(0\leq i\leq n-1)$$

으로 정의하자. 여기서 $$i=0$$일 때는 빈 곱으로 $$\varphi(\id)=1$$이다. 이것이 1-cocycle임을 확인하자. $$0\leq a,b\leq n-1$$에 대하여

$$\varphi(\sigma^a)\cdot\sigma^a\bigl(\varphi(\sigma^b)\bigr)=\prod_{k=0}^{a-1}\sigma^k(x)\cdot\prod_{k=0}^{b-1}\sigma^{a+k}(x)=\prod_{k=0}^{a+b-1}\sigma^k(x)$$

이다. 만일 $$a+b\leq n-1$$이라면 이는 정의에 의해 $$\varphi(\sigma^{a+b})=\varphi(\sigma^a\sigma^b)$$이다. 만일 $$a+b\geq n$$이라면 $$\sigma^k=\sigma^{k-n}$$ ($$k\geq n$$)이므로

$$\prod_{k=0}^{a+b-1}\sigma^k(x)=\prod_{k=0}^{n-1}\sigma^k(x)\cdot\prod_{k=n}^{a+b-1}\sigma^k(x)=N_{\mathbb{L}/\mathbb{K}}(x)\cdot\prod_{k=0}^{a+b-n-1}\sigma^k(x)=\varphi(\sigma^{a+b-n})$$

이고, $$\sigma^a\sigma^b=\sigma^{a+b-n}$$이므로 역시 cocycle 조건이 성립한다. 마지막 등식에서 가정 $$N_{\mathbb{L}/\mathbb{K}}(x)=1$$이 사용되었다.

이제 [정리 7](#thm7)에 의하여 $$\varphi$$는 1-coboundary이다. 즉 적당한 $$c\in\mathbb{L}^\times$$에 대하여 $$\varphi(\sigma^i)=\sigma^i(c)/c$$이고, 특히 $$i=1$$에서

$$x=\varphi(\sigma)=\frac{\sigma(c)}{c}$$

이므로 $$y=c$$로 두면 된다.

</details>

<div class="remark" markdown="1">

<ins id="rmk9">**참고 9**</ins> [정의 6](#def6)의 1-cocycle은 [\[호몰로지 대수학\] §군 코호몰로지](/ko/math/homological_algebra/group_cohomology)에서 다루는 crossed homomorphism을 곱셈 표기로 옮긴 것이다. 즉 $$\mathbb{L}^\times$$를 $$G$$-module로 보면 $$H^1(G,\mathbb{L}^\times)$$는 군 코호몰로지의 $$H^1$$이고, [정리 7](#thm7)은 이것이 사라진다는 주장이며, [따름정리 8](#cor8)은 cyclic group의 코호몰로지 계산과 결합한 것이다. 한편 $$\mathbb{L}/\mathbb{K}$$가 infinite degree Galois extension인 경우에는 임의의 cocycle 대신 이 글에서 정의한 Krull topology에 대해 연속인 cocycle들을 사용해야 올바른 이론이 얻어지며, 이것이 이 글에서 위상구조를 공들여 만든 또 하나의 이유이다. 덧셈 버전, 즉 $$\mathbb{L}$$을 덧셈 group으로 보았을 때 $$H^1(G,\mathbb{L})$$이 사라진다는 것도 성립하는데, 이는 normal basis 정리와 관련이 있으므로 추후 필요할 때 다루기로 한다.

</div>

---

**참고문헌**

**[Bou]** N. Bourbaki. *Algebra II: Chapters 4–7*. Springer, 2003.  
**[Ser]** J.-P. Serre. *Local Fields*. Graduate texts in mathematics. Springer, 1979.

---

