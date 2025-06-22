---

title: "갈루아 군의 성질들"
excerpt: ""

categories: [Math / Field Theory]
permalink: /ko/math/field_theory/properties_of_galois_extensions
header:
    overlay_image: /assets/images/Math/Field_Theory/Properties_of_Galois_extensions.png
    overlay_filter: 0.5
sidebar: 
    nav: "field_theory-ko"

date: 2025-06-18
last_modified_at: 2025-06-18
weight: 9
 
---

우리는 앞서 Galois extension과 Galois group을 정의했다. Galois theory의 핵심적인 결과는 field extension $\mathbb{L}/\mathbb{K}$에 대하여 Galois group $\Gal(\mathbb{L}/\mathbb{K})$의 subgroup들의 lattice와, $\mathbb{L}/\mathbb{K}$의 Galois subextension들의 lattice 사이에 order-preserving bijection이 존재한다는 것이다. 많은 경우에 이 결과는 Galois group $\Gal(\mathbb{L}/\mathbb{K})$이 유한한 경우만 다루지만, 우리는 $\Gal(\mathbb{L}/\mathbb{K})$가 무한할 경우 또한 다룰 것이므로 이를 위해서는 $\Gal(\mathbb{L}/\mathbb{K})$에 적절한 위상구조를 주어야 한다.

## 갈루아 군의 위상구조

Galois extension $\mathbb{L}/\mathbb{K}$이 주어졌다 하고, $\Gal(\mathbb{L}/\mathbb{K})$이 이 extension의 Galois group이라 하자. 그럼 우선 우리는 집합 $\mathbb{L}$ 위에 discrete topology를 부여한 후, $\mathbb{L}$에서 $\mathbb{L}$로의 함수들의 모임 $\Fun(\mathbb{L},\mathbb{L})=\mathbb{L}^\mathbb{L}$에 product topology를 준다. 이 때 우리는 [\[위상수학\] §곱공간](/ko/math/topology/product_spaces)의 결과로부터 이 집합의 subbase는 다음과 같은 꼴

$$U_{x,y}=\left\{\sigma\mid\sigma(x)=y \right\}$$

로 쓸 수 있는 집합들의 모임이며, $\Gal(\mathbb{L}/\mathbb{K})$를 이 집합의 부분집합으로 보아 subspace topology를 부여하면 임의의 $\sigma\in\Gal(\mathbb{L}/\mathbb{K})$에 대하여 $\sigma$에서의 local base는 이러한 꼴의 집합들의 유한한 합집합 꼴로 나타나는 다음과 같은 형태

$$U_{x_1,\ldots,x_n}=\left\{\tau\in\Gal(\mathbb{L}/\mathbb{K})\mid \text{$\tau(x_i)=\sigma(x_i)$ for all $i$}\right\}$$

의 집합들의 모임이다. 한편 위의 조건을 만족하는 함수들은 $\mathbb{L}$의 finite subextension $\mathbb{M}=\mathbb{L}(x_1,\ldots,x_n )$으로 제한했을 때 $\sigma$와 일치하는 함수들이며, 거꾸로 임의의 finite subextension $\mathbb{M}/\mathbb{K}$은 이러한 방식으로 $\sigma$의 local base의 원소를 하나 정의한다. 즉 $\Lambda$를 extension $\mathbb{L}/\mathbb{K}$의 *finite* subextension들의 모임이라 하고 임의의 $\mathbb{M}/\mathbb{K}\in \Lambda$와 임의의 $\sigma\in \Gal(\mathbb{L}/\mathbb{K})$에 대하여, $\Gal(\mathbb{L}/\mathbb{K})$의 부분집합 $U_\mathbb{M}(\sigma)$를 다음의 식 

$$U_\mathbb{M}(\sigma)=\left\{\tau\in \Gal(\mathbb{L}/\mathbb{K})\mid \sigma\vert_\mathbb{M}=\tau\vert_\mathbb{M}\right\}$$

으로 정의하면 이 집합은 $\sigma$의 local base의 원소가 된다. 특히 만일 $\mathbb{L}$이 finite degree Galois extension이었다면 $\Gal(\mathbb{L}/\mathbb{K })$는 discrete topology가 되어 위상구조에 별다른 관심을 기울이지 않아도 된다. 

한편 우리는 앞선 글에서 임의의 Galois extension $\mathbb{L}/\mathbb{K}$와 그 subextension $\mathbb{M}/\mathbb{K}$에 대하여 canonical homomorphism 

$$\Gal(\mathbb{L}/\mathbb{K})\rightarrow\Gal(\mathbb{M}/\mathbb{K })$$

이 존재함을 보였는데, 위의 관찰에 따르면 $\mathbb{M}$의 임의의 finite subextension은 $\mathbb{L}$의 finite subextension이기도 하므로 자명한 이유에서 이 restriaction map이 연속임을 안다. 

뿐만 아니라 $\Gal(\mathbb{L}/\mathbb{K})$는 자연스러운 곱셈 연산, 합성을 가지고 있으며 이 연산은 위성구조와 잘 호환된다. 즉 $\Gal(\mathbb{L}/\mathbb{K})$는 topological group이며 그 증명 또한 자명하다.

<div class="proposition" markdown="1">

<ins id="prop1">**명제 1**</ins> Galois group $\Gal(\mathbb{L}/\mathbb{K}) $는 compact, totally disconnected topological group이다. 

</div>