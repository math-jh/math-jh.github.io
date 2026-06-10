---
title: "곱공간"
description: "위상공간들의 곱에 대한 곱_topology의 정의와 성질을 다룬다. 곱공간 위의 연속 함수의 성질을 universal property로 기술하고, 함수의 그래프와 homeomorphism에 적용하여 따름정리들을 유도한다."
excerpt: "곱공간의 성질들"

categories: [Math / Topology]
permalink: /ko/math/topology/product_spaces
sidebar: 
    nav: "topology-ko"

date: 2022-11-21
last_modified_at: 2022-11-21
weight: 11
published: false

---

## 곱공간의 정의와 성질들

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 위상공간들의 family $$(X_i)_{i\in I}$$가 주어졌다 하자. 이들의 *곱<sub>product</sub>*은 곱집합 $$X=\prod_{i\in I}X_i$$ 위에 함수들 $$\pr_i:X\rightarrow X_i$$에 대한 initial topology가 주어진 위상공간이다.

</div>

그럼 [§Initial topology와 final topology, ⁋명제 2](/ko/math/topology/initial_and_final_topology#prop2)에 의하여 $$X$$ 위에 주어진 product topology는 다음의 집합

$$\mathcal{S}=\{\pr_i^{-1}(U_i)\mid U_i\text{ open in }X_i\}$$

을 subbase로 하여 생성된 공간이다. 이 때, $$\mathcal{S}$$에 의하여 생성되는 base $$\mathcal{B}$$는 

$$\prod_{i\in I} U_i,\qquad \text{$U_i$ open in $X_i$, $U_i=X_i$ for all but finitely many $i$}$$

들의 모임이다. 

[\[집합론\] §곱집합의 성질, ⁋명제 3](/ko/math/set_theory/property_of_products#prop3)과 마찬가지 이유에 의하여 공간들의 곱을 취하는 것은 결합법칙을 만족한다는 것을 알 수 있으며, 비슷하게 교환법칙에 대한 명제 또한 존재한다. 이들은 꽤나 자명한 명제이므로 별도로 언급하고 넘어가지 않는다.

한편 [§Initial topology와 final topology, ⁋명제 3](/ko/math/topology/initial_and_final_topology#prop3)을 적용하면 다음을 얻는다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> 곱공간 $$X=\prod_{i\in I}X_i$$와 위상공간 $$Y$$가 주어졌다 하고, 함수들 $$f_i:Y\rightarrow X_i$$이 주어졌다 하자. 그럼 함수 $$f=(f_i): Y\rightarrow X$$가 연속인 것은 각각의 $$f_i$$가 연속인 것과 동치이다.

</div>

이로부터 다음 두 개의 따름정리를 얻는다. 

<div class="proposition" markdown="1">

<ins id="cor3">**따름정리 3**</ins> Index set $$I$$를 공유하는 두 곱공간 $$X=\prod_{i\in I}X_i$$, $$Y=\prod_{i\in I}Y_i$$이 주어졌다 하고, $$f_i:X_i\rightarrow Y_i$$들이 주어졌다 하자. 그럼 $$f:(x_i)\mapsto (f_i(x_i))$$이 연속인 것은 각각의 $$f_i$$가 연속인 것과 동치이다.

</div>

임의의 집합 $$X, Y$$와 함수 $$f:X \rightarrow Y$$에 대하여, $$f$$의 *graph* $$\Gamma(f)$$는 $$X\times Y$$의 부분집합

$$\Gamma(f)=\{(x,f(x)\mid x\in X\}\subseteq X\times Y$$

으로 주어진다. 만일 $$X, Y$$가 모두 위상공간이었다면 $$\Gamma(f)$$는 product space $$X\times Y$$로부터 subspace topology를 물려받는다.

<div class="proposition" markdown="1">

<ins id="cor4">**따름정리 4**</ins> 위상공간 $$X,Y$$와 함수 $$f:X\rightarrow Y$$에 대하여, $$f$$가 연속인 것은 함수 $$g:x\mapsto (x,f(x))$$가 $$X$$에서 $$\Gamma(f)$$로의 homeomorphism인 것과 동치이다.

</div>

뿐만 아니라, 위의 함수 $$g$$의 자명한 역함수

$$\pr_X\vert_{\Gamma(f)}:\Gamma(f) \rightarrow X$$

또한 알고 있다. 

특히 $$X$$의 모든 점을 $$y_0\in Y$$로 보내는 상수함수는 연속이므로, 위의 따름정리에 의하여 homeomorphism

$$X\rightarrow X\times\{y_0\}$$

을 얻는다. 한편 $$X\times Y$$의 임의의 집합 $$A$$를 생각하자. 그럼 

$$A\cap (X\times \{y_0\})=\{(x,y)\mid (x,y)\in A,\quad y=y_0\}=\{(x,y_0)\mid (x,y_0)\in A\}$$

이다. 이제 $$\Gamma(f)$$는 $$X\times Y$$의 subspace topology가 주어져 있으므로, 위의 집합은 $$A$$가 $$X\times Y$$의 열린집합이라면 $$\Gamma(f)$$의 열린집합이 되고, $$A$$가 $$X\times Y$$의 닫힌집합이라면 $$\Gamma(f)$$의 닫힌집합이 된다. 따라서 다시 [따름정리 4](#cor4)를 적용하여 위의 집합을 $$X$$로 보내면 해당하는 집합 또한 열린집합 혹은 닫힌집합이 된다. 이 집합을 $$A(y_0)\subseteq X$$로 적자. 물론 비슷한 논증을 $$X$$와 $$Y$$의 역할을 바꾸어 $$Y$$의 부분집합 $$A(x_0)$$을 얻을 수도 있다. 

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> $$X\times Y$$의 임의의 열린집합 $$U$$에 대하여, $$\pr_X(U)$$와 $$\pr_Y(U)$$는 $$X,Y$$의 열린집합이 된다.  

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

위의 논증과 다음 식

$$\pr_X(U)=\bigcup_{y\in Y} U(y),\qquad \pr_Y(U)=\bigcup_{x\in X} U(x)$$

으로부터 자명하다. 

</details>

그러나 닫힌집합들의 임의의 합집합은 닫힌집합일 필요가 없으므로, 위의 명제에서 $$A$$를 닫힌집합으로 바꾼 주장은 성립하지 않는다. 한편, [따름정리 4](#cor4)에 의하여 다음의 명제 또한 얻는다. 

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> 함수 $$f:X_1\times X_2 \rightarrow Y$$가 $$(a_1,a_2)\in X_1\times X_2$$에서 연속이라면, 다음의 식

$$x_1\mapsto f(x_1, a_2),\qquad x_2\mapsto f(a_1,x_2)$$

으로 정의된 $$X_1$$에서 $$Y$$, $$X_2$$에서 $$Y$$로의 함수들은 각각 점 $$x_1=a_1$$, $$x_2=a_2$$에서 연속이다. 

</div>

그러나 이 명제의 역은 성립하지 않는다. 

## 내부와 폐포

이제 우리는 곱집합과 내부, 폐포의 관계를 알아본다. 우선 폐포를 취하는 것은 곱집합에 대해 잘 행동한다. 즉 다음이 성립한다. 

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> Product space $$X=\prod_{i\in I} X_i$$와, $$X_i$$의 임의의 부분집합 $$A_i$$들이 주어졌다 하자. 그럼 다음 식

$$\prod_{i\in I} \cl A_i=\cl\left(\prod_{i\in I} A_i\right)$$

이 성립한다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $$\prod_{i\in I}\cl A_i$$는 닫힌집합이다. 이는 다음의 식

$$\prod_{i\in I}\cl A_i=\bigcap_{i\in I}\pr_i^{-1}(\cl A_i)$$

과, projection들이 연속이므로 각각의 $$\pr_i^{-1}(\cl A_i)$$가 닫힌집합이라는 것, 그리고 닫힌집합들의 임의의 교집합이 닫힌집합이라는 것에 따른 것이다. 그럼 $$\prod A_i\subseteq \prod\cl A_i$$이므로 closure의 최소성에 의하여

$$\cl\left(\prod_{i\in I}A_i\right)\subseteq \prod_{i\in I}\cl A_i$$

이다.

거꾸로 $$x=(x_i)\in\prod_{i\in I}\cl A_i$$가 주어졌다 하고, $$x$$의 임의의 근방 $$V$$를 생각하자. 그럼 product topology의 base를 생각하면, $$x\in\prod U_i\subseteq V$$이고 유한 개의 $$i$$를 제외하면 $$U_i=X_i$$이도록 하는 열린집합들 $$U_i$$가 존재한다. 각각의 $$i$$에 대하여 $$x_i\in \cl A_i$$이고 $$U_i$$가 $$x_i$$의 근방이므로, [§집합의 내부, 폐포, 경계, ⁋명제 6](/ko/math/topology/other_concepts#prop6)에 의하여 $$U_i\cap A_i\neq\emptyset$$이고, 원소 $$a_i\in U_i\cap A_i$$를 택할 수 있다. 그럼 $$a=(a_i)$$는 $$V\cap \prod A_i$$의 원소이므로 $$x$$의 임의의 근방이 $$\prod A_i$$와 만나고, 다시 [§집합의 내부, 폐포, 경계, ⁋명제 6](/ko/math/topology/other_concepts#prop6)에 의하여 $$x\in \cl\left(\prod A_i\right)$$이다.

</details>

그러나 위의 명제는 interior에 대해서는 항상 성립하는 것은 아니며, $$I$$가 유한집합일 때만 성립한다.

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> Index set $$I$$가 유한집합인 product space $$\prod_{i\in I} X_i$$와, $$X_i$$의 임의의 부분집합 $$A_i$$들이 주어졌다 하자. 그럼 다음 식

$$\prod_{i\in I} \interior A_i=\interior\left(\prod_{i\in I} A_i\right)$$

이 성립한다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$I$$가 유한집합이므로 $$\prod_{i\in I}\interior A_i$$는 위에서 살펴본 product topology의 base에 속하는 열린집합이고, $$\prod A_i$$에 포함된다. 따라서 interior의 최대성에 의하여

$$\prod_{i\in I}\interior A_i\subseteq \interior\left(\prod_{i\in I}A_i\right)$$

이다.

거꾸로 $$x=(x_i)\in\interior\left(\prod A_i\right)$$라 하자. 그럼 base를 생각하면 $$x\in \prod U_i\subseteq \prod A_i$$이도록 하는 열린집합들 $$U_i$$가 존재한다. 각각의 $$j\in I$$를 고정하면, 임의의 $$y_j\in U_j$$에 대하여 $$x$$의 $$j$$번째 성분만 $$y_j$$로 바꾼 원소는 여전히 $$\prod U_i$$에 속하고 (다른 성분들은 $$x_i\in U_i$$), 따라서 $$\prod A_i$$에 속한다. 이 원소의 $$j$$번째 성분을 읽으면 $$y_j\in A_j$$이다. 즉 $$U_j\subseteq A_j$$이고, $$U_j$$가 열린집합이므로 $$x_j\in U_j\subseteq \interior A_j$$이다. 이것이 모든 $$j$$에 대해 성립하므로 $$x\in\prod_{i\in I}\interior A_i$$이다.



</details>