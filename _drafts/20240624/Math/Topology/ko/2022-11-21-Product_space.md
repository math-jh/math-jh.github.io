---

title: "곱공간 (작성중)"
excerpt: "곱공간의 성질들"

categories: [Math / Topology]
permalink: /ko/math/topology/product_space
header:
    overlay_image: /assets/images/Math/Topology/Product_space.png
    overlay_filter: 0.5
sidebar: 
    nav: "topology-ko"

date: 2022-11-21
last_modified_at: 2022-11-21
weight: 9

---

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 위상공간들의 family $(X\_i)\_{i\in I}$가 주어졌다 하자. 이들의 *곱<sub>product</sub>*은 곱집합 $X=\prod\_{i\in I}X\_i$ 위에 함수들 $\pr\_i:X\rightarrow X\_i$에 대한 initial topology가 주어진 위상공간이다.

</div>

그럼 [§Initial topology와 final topology, ⁋명제 2](/ko/math/topology/initial_and_final_topology#prop2)에 의하여 $X$ 위에 주어진 product topology는 다음의 집합

$$\mathcal{S}=\{\pr_i^{-1}(U_i)\mid U_i\text{ open in }X_i\}$$

을 subbasis로 하여 생성된 공간이다. 이 때, $\mathcal{S}$에 의하여 생성되는 basis $\mathcal{B}$는 

$$\prod_{i\in I} U_i,\qquad \text{$U_i$ open in $X_i$, $U_i=\emptyset$ for all but finitely many $i$}$$

들의 모임이다. 한편 [§Initial topology와 final topology, ⁋명제 3](/ko/math/topology/initial_and_final_topology#prop3)을 적용하면 다음을 얻는다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> 곱공간 $X=\prod\_{i\in I}X\_i$와 위상공간 $Y$가 주어졌다 하고, 함수들 $f\_i:Y\rightarrow X\_i$이 주어졌다 하자. 그럼 함수 $f=(f\_i): Y\rightarrow X$가 연속인 것은 각각의 $f\_i$가 연속인 것과 동치이다.

</div>

<div class="proposition" markdown="1">

<ins id="cor3">**따름정리 3**</ins> Index set $I$를 공유하는 두 곱공간 $X=\prod\_{i\in I}X\_i$, $Y=\prod\_{i\in I}Y\_i$이 주어졌다 하고, $f\_i:X\_i\rightarrow Y\_i$들이 주어졌다 하자. 그럼 $f:(x\_i)\mapsto (f\_i(x\_i))$이 연속인 것은 각각의 $f\_i$가 연속인 것과 동치이다.

</div>

<div class="proposition" markdown="1">

<ins id="cor4">**따름정리 4**</ins> 위상공간 $X,Y$와 함수 $f:X\rightarrow Y$에 대하여, $f$가 연속인 것은 함수 $g:x\mapsto (x,f(x))$가 $X$에서 $\Gamma(f)$로의 homeomorphism인 것과 동치이다.

</div>

특히, 상수함수 $f$는 항상 연속이고, $f$가 모든 $x\in X$를 $y\in Y$로 보낸다고 하면 $\Gamma(f)=X\times\\{y\\}$가 된다. 따라서 $X$와 $X\times\\{y\\}$가 항상 homeomorphic하며, 비슷하게 $Y$와 $\\{x\\}\times Y$ 또한 항상 homeomorphic하다.

## Closure와 곱집합


