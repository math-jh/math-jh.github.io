---
title: "부분공간"
excerpt: "위상공간의 부분공간"

lang: ko

categories: [Math / Topology]
permalink: /ko/math/topology/subspace_topology
header:
    overlay_image: /assets/images/Topology/Topological_basis.png
    overlay_filter: 0.5
sidebar: 
    nav: "topology-ko"

date: 2021-09-26
last_modified_at: 2022-04-07
weight: 9
    
---

이제 우리는 이미 존재하는 위상구조로부터 새로운 위상공간을 얻는 방법을 소개한다. 순서대로 부분위상, 곱위상, 상위상을 먼저 소개한 후, 그 다음 글에서는 이 개념들을 잘 설명할 수 있는 *initial topology*와 *final topology*의 개념을 별도로 소개하기로 한다.

## Subspace의 정의

대수적인 구조를 다룰 때와 마찬가지로, 집합 $X$ 위에 위상구조를 준 후에는 이 구조가 부분집합 $A\subset X$에는 어떠한 방식으로 제한되는지를 살펴보는 것이 자연스럽다. 가장 먼저 드는 생각은 $X$의 열린집합들 가운데, $A$에 포함된 열린집합들만 추려 이들을 위상공간 $A$의 열린집합들로 정의하는 것이다. 그러나 이 시도는 실패할 수밖에 없는데, $A$가 $X$에서 열린집합이 아니라면, 전체집합 $A$부터가 이 모임에 속하지 않기 때문이다. 

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins>  $X$가 위상공간이라 하자. 그럼 $X$의 부분집합 $A$에 대하여, 다음의 모임

$$\mathcal{T}_A=\left\{A\cap U:U\in\mathcal{T}\right\}$$

는 $A$ 위에서의 위상이며, 이를 *subspace topology<sub>부분위상</sub>*이라 부르고, subspace topology가 주어진 집합 $A$를 $X$의 *subspace<sub>부분공간</sub>*이라 부른다.

</div>

물론 우리는 이렇게 정의한 $\mathcal{T}_A$의 원소들이 위상공간의 조건을 만족하는지를 살펴봐야 한다. 이는 합집합과 교집합 간의 분배법칙를 잘 쓰면 어렵지 않게 체크할 수 있다. 

Subspace를 다룰 때 주의해야 하는 것은, $\mathcal{T}_A$에서 열린집합이라 하더라도 $\mathcal{T}$에서는 열린집합이 아닐 수 있다는 것이다.

![open_in_subspace_but_not_in_whole](/assets/images/Topology/Constructing_topologies-1.png){:width="250px"  class="invert" .align-center}

이러한 상황은 $A$가 열린집합이었다면 쉽게 해결된다.

<div class="proposition" markdown="1">

<ins id="lem2" markdown="1">**보조정리 2**</ins> $A$가 $X$의 subspace라 하자. 만일 $A$가 $X$에서 열린집합이라면, $A$에서 열린집합인 임의의 $U$는 $X$에서도 열린집합이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

거의 자명하다. $U$가 $A$의 열린 부분집합이라면, 어떤 열린집합 $V\subset X$가 존재하여 $U=A\cap V$인데, $A$도 열린집합이므로 $A\cap V=U$도 ($X$에서) 열린집합이다.

</details>

## Subspace의 basis, closure

우리는 원래의 위상 $\mathcal{T}$가 basis를 이용해 정의되었을 경우도 생각할 수 있는데, 이 경우도 subspace가 잘 작동한다.

<div class="proposition" markdown="1">

<ins id="lem3">**보조정리 3**</ins> $X$ 위에서의 위상이 basis $\mathcal{B}$를 통해 정의되었다 하자. 그럼 다음의 모임
  
$$\mathcal{B}_A=\left\{B\cap A:B\in\mathcal{B}\right\}$$

는 $A$의 subspace topology의 basis가 된다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$A$의 임의의 열린집합을 고르자. 그럼 어떤 $X$의 열린집합 $U$에 대하여 이 집합은 $U\cap A$로 쓸 수 있다. 이제 임의의 $x\in U\cap A$에 대하여, $x\in U$이므로 어떠한 $B\in\mathcal{B}$가 존재하여 $x\in B\subset U$이다. 이제 $x\in B\cap A\subset U\cap A$이므로, $\mathcal{B}_A$는 basis의 조건을 만족하고, 따라서 $\mathcal{T}_A$의 basis가 된다.

</details>

한편 열린집합과 비슷하게 중요한 역할을 하는 것은 닫힌집합이었다. 하지만 닫힌집합은 단순히 열린집합의 여집합으로 정의되므로, 당연히 subspace topology와도 잘 어울린다. 예를 들어, 

<div class="proposition" markdown="1">

<ins id="pp4">**명제 4**</ins> $A$가 $X$의 subspace라 하자. 그럼 어떤 $C$가 $A$에서 닫힌집합인 것은, $X$의 어떤 닫힌집합 $D$가 존재하여 $C=D\cap A$인 것과 동치이다.    

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $C$가 $A$에서 닫힌집합이라 하자. 즉, $A\setminus C$는 $C$에서 열린집합이다. 그럼 $A$의 subspace topology의 정의에 의하여, $X$의 어떠한 열린집합 $V$가 존재하여 $A\setminus C=A\cap V$이다. 이제, 닫힌집합 $V^c$를 생각하면

$$A\cap V^c=A\setminus (A\cap V)=A\setminus(A\setminus C)=C$$

이므로 한쪽 방향이 성립하고, 나머지 한 쪽 방향은 이 논증을 거꾸로 뒤집으면 된다. 
</details>

그리고 [보조정리 2](#lem2) 또한 다음과 같이 새로 쓸 수 있다.

<div class="proposition" markdown="1">

<ins id="lem5">**보조정리 5**</ins> $A$가 $X$의 subspace라 하자. 만일 $C$가 $A$의 닫힌집합이고 $A$가 $X$의 닫힌집합이라면 $U$는 $X$의 닫힌집합이다.  

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[보조정리 2](#lem2)의 증명과 토씨 하나 안 틀리고 똑같다. $C$가 $A$의 닫힌집합이므로, 어떤 닫힌집합 $D\subset X$가 존재하여 $C=D\cap A$인데, $A$도 닫힌집합이므로 $D\cap A=C$도 ($X$에서) 닫힌집합이다.

</details>

뿐만 아니라, 어떤 집합 $B$의 subspace $A$에서의 closure와, 전체집합 $X$에서의 closure 간에도 다음과 같은 관계가 성립한다. 

<div class="proposition" markdown="1">

<ins id="pp6">**명제 6**</ins> $A$가 $X$의 subspace이고, $B\subset A$라 하자. 그럼 $B$의 $X$에서의 closure $\operatorname{cl}B$에 대하여, $B$의 *$A$에서의* closure는 $(\operatorname{cl}B)\cap A$로 주어진다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선, $B\subset\operatorname{cl}B$이고, $B\subset A$이므로 $B\subset(\operatorname{cl}B)\cap A$가 성립하고, 앞선 명제에 의해 이 집합은 $A$에서의 닫힌집합이다. 따라서, 이 집합이 $B$를 포함하는 임의의 ($A$에서의) 닫힌집합에 포함된다는 것만 보이면 closure의 정의로부터 원하는 결론을 얻는다.  

$C$가 $B$를 포함하는 $A$의 닫힌집합이라 하자. 그럼 어떠한 $X$의 닫힌집합 $D$가 존재하여 $C=D\cap A$이다. 그런데, $B\subset C\subset D$이므로, $D$는 $B$를 포함하는 닫힌집합이고 $\operatorname{cl}B$ 또한 포함한다. 그러므로 

$$C=D\cap A\supset(\operatorname{cl}B)\cap A$$

이고, 따라서 원하는 결론을 얻는다.  

</details>

## Subspace와 연속함수

마지막으로 우리는 연속함수와 subspace 사이의 관계 또한 생각할 수 있다. 우선, 연속함수 $f:X\rightarrow Y$를 subspace $A$로 제한한 함수는 연속이다.

<div class="proposition" markdown="1">

<ins id="pp7">**명제 7**</ins> $f:X\rightarrow Y$가 위상공간들 사이의 연속함수이고 $A$가 $X$의 subspace라면, $f\|\_A$는 연속이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

정의로부터 거의 자명하다. $Y$의 임의의 열린집합 $V$에 대하여, $(f\|\_A)^{-1}(V)$가 열린집합이면 되는데, 이는

$$(f|_A)^{-1}(V)=f^{-1}(V)\cap A$$

이고, $f^{-1}(V)$는 $f$의 연속성에 의해 열린집합이므로, $(f\|\_A)^{-1}(V)$도 $A$의 열린집합이고 따라서 $f\|\_A$는 연속함수이다.

</details>

뿐만 아니라, 연속함수들이 subspace들에서 정의되어 있다면, 이들을 모아 하나의 함수로 만들 수도 있다. (cf. <#ref#>)

<div class="proposition" markdown="1">

<ins id="pp8">**명제 8 (Pasting lemma)**</ins> 위상공간 $X$가 두 닫힌집합 $C$와 $D$에 대하여 $X=C\cup D$로 쓰여졌다고 하자. 함수 $f:C\rightarrow Y$와 $g:D\rightarrow Y$가 연속이고, $C\cap D$에서 compatible하다면 유일한 연속함수 $h:X\rightarrow Y$가 존재하여 $f$와 $g$를 확장한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

앞서 언급한 집합론에서의 명제에 의해, 이러한 함수가 유일하게 존재한다는 것이 잘 보장되어 있다. 따라서, 연속성만 보이면 충분하다. $Y$의 임의의 닫힌집합 $C'$에 대하여, $h^{-1}(C')$가 항상 닫힌집합임을 보이자. ([§연속함수, 명제 2](/ko/math/topology/basic_definition_4#pp2)의 세 번째 동치조건) 

$$h^{-1}(C')\cap C=(h|_C)^{-1}(C')=f^{-1}(C'),\quad h^{-1}(C')\cap D=(h|_D)^{-1}(C')=g^{-1}(C')$$

이므로 이 두 집합은 각각 $C$와 $D$에서 닫힌집합들이다. 그런데, $C$와 $D$는 모두 닫힌집합들이므로, 이 두 집합은 $X=C\cup D$에서 닫힌집합이기도 하고 ([보조정리 5](#lem5)) 따라서

$$h^{-1}(C')=h^{-1}(C')\cap X=h^{-1}(C')\cap(C\cup D)=(h^{-1}(C')\cap C)\cup h^{-1}(C')\cap D)\tag{1}$$

는 두 닫힌집합의 합집합이므로 닫힌집합이다. 

</details>

사실, $C$와 $D$가 둘 다 열린집합이었다 하더라도 [§연속함수, 명제 2](/ko/math/topology/basic_definition_4#pp2)의 두 번째 동치조건을 쓰면 되므로, 이 명제는 열린집합들에 대해서도 당연히 성립한다. 한편, 이 명제를 (집합론에서와 마찬가지로) $X=\bigcup C\_i$로 주고 성립 여부를 따져볼 수 있는데, 만일 $C\_i$들이 모두 열린집합이라면 식 (1)이 열린집합들의 임의의 합집합으로 바뀌므로 문제 없이 성립한다. 하지만, 이들이 모두 닫힌집합이라면, 유한한 합집합일 경우에는 이 명제가 성립하겠지만, 무한한 합집합일 때는 성립하지 않는다는 이야기도 된다.  



---

**참고문헌**

**[Mun]** J.R. Munkres, <i>Topology</i>. Featured Titles for Topology. Prentice Hall, Incorporated, 2000.

---
