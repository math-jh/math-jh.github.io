---

title: "집합의 내부, 폐포, 경계"
excerpt: "위상수학의 기본 개념들"

categories: [Math / Topology]
permalink: /ko/math/topology/other_concepts
header:
    overlay_image: /assets/images/Math/Topology/Other_concepts.png
    overlay_filter: 0.5
sidebar: 
    nav: "topology-ko"

date: 2022-11-09
last_modified_at: 2022-11-09
weight: 3

---

본격적으로 연속함수, 수열 등의 개념을 다루기 전에 위상수학에서 사용하는 언어들을 마저 도입한다.

## 닫힌집합

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> 위상공간 $X$에 대하여, 집합 $A$가 *닫힌집합<sub>closed set</sub>*이라는 것은 $A$의 여집합 $A^c=X\setminus A$가 열린집합인 것이다.

</div>

$X$ 위의 임의의 위상 $\mathcal{T}$에서 $\emptyset$과 $X$는 열린집합인 동시에 닫힌집합이고, 아예 discrete topology를 주면 임의의 부분집합이 열린집합인 동시에 닫힌집합이 된다. 따라서 닫힌집합과 열린집합은 반대개념이 아니라, 오히려 같은 것을 다른 방식으로 표현한 것에 가깝다. 예컨대, 위상 $\mathcal{T}$는 사실 닫힌집합들을 이용하여 다음과 같이 정의할 수 있다.

<div class="proposition" markdown="1">

<ins id="pp2">**명제 2**</ins> 집합 $X$ 위에 다음의 조건들을 만족하는 모임 $\mathcal{C}$가 주어졌다 하자.

1. $\emptyset$, $X\in\mathcal{C}$
2. $\mathcal{C}$는 임의의 교집합에 대하여 닫혀있다.
3. $\mathcal{C}$는 <em_ko>유한한</em_ko> 합집합에 대하여 닫혀있다.

그럼 $\mathcal{C}$의 각 원소들의 여집합을 열린집합으로 갖는 위상 $\mathcal{T}$가 유일하게 존재한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

다음의 De Morgan 법칙 ([\[집합론\] §합집합과 교집합, ⁋명제 8](/ko/math/set_theory/union_and_intersection#pp8))

$$\left(\bigcap A_i\right)^c=\bigcup A_i^c,\quad\left(\bigcup A_i\right)^c=\bigcap A_i^c$$

으로부터 자명하다.

</details>

앞선 명제의 세 번째 조건을 더 다듬을 수 있다.

<div class="definition" markdown="1">

<ins id="df3">**정의 3**</ins> 위상공간 $X$가 주어졌다 하고, $X$의 부분집합들의 family $(A\_i)\_{i\in I}$가 주어졌다 하자. 그럼 $(A\_i)$가 *locally finite<sub>국소적으로 유한</sub>*이라는 것은 임의의 $x\in X$마다, 적당한 근방 $V$가 존재하여 $V\cap A_i\neq\emptyset$을 만족하는 $i$가 오직 유한 개 뿐인 것이다.

</div>

임의의 유한한 family가 locally finite인 것은 자명하므로 위 정의는 유한한 family의 일반화라 할 수 있다. 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="pp4">**명제 4**</ins> 위상공간 $X$가 주어졌다 하자. 만일 $(A\_i)\_{i\in I}$가 locally finite인 닫힌집합들의 모임이라면, $A=\bigcup A\_i$는 닫힌집합이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

이를 위해서는 $A^c$가 열린집합임을 보이면 된다. $x\in A^c$라 하자. 그럼 $x\in A_i^c$가 모든 $i$에 대해 성립한다. 한편, $(A\_i)$는 locally finite이므로 $x$의 근방 $V$가 존재하여 $V\cap A_i\neq\emptyset$을 만족하는 $i$가 오직 유한 개 뿐이도록 할 수 있다. 이러한 $i$들을 모아둔 $I$의 부분집합을 $J$라 하자. 그럼 임의의 $j\in J$에 대하여, $A_j^c$는 모두 열린집합이며, 따라서 다음 집합

$$V\cap\bigcap_{j\in J} A_j^c$$

은 $x$의 근방이 되며, $A^c$의 부분집합이다. 이로부터 $A^c$는 열린집합임을 알고, 따라서 $A$는 닫힌집합이다.

</details>

## 집합의 내부와 폐포

위상공간 $(X,\mathcal{T})$가 주어졌다고 하자. $X$의 임의의 부분집합 $A$에 대하여, <phrase>$A$를 포함하는 닫힌집합</phrase>과 <phrase>$A$에 포함되어 있는 열린집합</phrase>이 항상 존재한다. ($X$와 $\emptyset$). 한편, 닫힌집합들의 임의의 교집합은 닫힌집합이고, 열린집합들의 임의의 합집합은 열린집합이므로, <phrase>$A$를 포함하는 가장 작은 닫힌집합</phrase>과 <phrase>$A$에 포함된 가장 큰 열린집합</phrase>이 모두 존재한다. 이들을 다음과 같이 정의한다.

<div class="definition" markdown="1">

<ins id="df5">**정의 5**</ins> 위상공간 $X$의 임의의 부분집합 $A$에 대하여, $A$를 포함하는 가장 작은 닫힌집합을 $A$의 *closure<sub>폐포</sub>*, $A$에 포함된 가장 큰 열린집합을 $A$의 *interior<sub>내부</sub>*라 부르고, 이를 각각 $\cl(A)$와 $\interior(A)$로 적는다. 

</div>

이렇게 정의하면 두 연산자 $\cl$과 $\interior$가 포함관계를 유지한다는 것은 자명하다. 

다음의 식

$$\interior(A^c)=(\cl(A))^c$$

을 증명해보자. 정의에 의해, $\interior(A^c)$는 $A^c$에 포함된 열린집합 중 가장 큰 것이고, 이는 $A$를 포함하지 않는 열린집합 중 가장 큰 것이라는 말과 동일하다. 한편 $\cl(A)$는 $A$를 포함하는 닫힌집합 중 가장 작은 것이고, 따라서 $(\cl(A))^c$는 $A$를 포함하지 않는 열린집합 중 가장 큰 것이 되어 이 둘은 동일해야 한다. 우리는 이 집합을 $A$의 *exterior<sub>외부</sub>*라 부른다.

위와 같은 논증을 통해 interior와 closure, exterior 중 어느 하나만 있더라도 다른 둘을 만들 수 있다는 것을 안다. 

집합 $A$의 interior를 생각하자. $x\in\interior(A)$라는 것은 $x$를 포함하고, $A$에 포함되는 열린집합 $U$가 존재한다는 뜻이고, 따라서 $A$가 $x$의 근방이라는 것과 동치이다. 따라서 임의의 두 집합 $A,B$에 대하여, $x\in\interior(A\cap B)$인 것은 $x\in\interior(A)\cap\interior(B)$인 것과 동치이다. ([§열린집합, ⁋명제 6](/ko/math/topology/open_sets#pp6)의 둘째 조건) 이를 위에서 설명한 방식을 따라 closure에 대한 명제로 바꾸면 다음 등식

$$\cl(A\cup B)=\cl(A)\cup\cl(B)$$

을 얻는다.

<div class="proposition" markdown="1">

<ins id="pp6">**명제 6**</ins> 위상공간 $X$와 부분집합 $A$에 대하여, 두 조건 

1. $x\in\cl A$인 것,
2. $x$의 임의의 근방 $U$가 $A$와 만나는 것

이 서로 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

대우명제를 보이는 것이 편하다. $x\not\in\cl A$라 하자. 그럼 $x\in(\cl A)^c=\ext A$는 $x$를 포함하며, $\cl A$와 만나지 않는 열린집합이고, 따라서 $A$와도 만나지 않는 열린집합이 된다. 즉, 명제 <phrase>$A$와 만나지 않는 $x$의 어떠한 근방이 존재한다</phrase>가 참이다. 

거꾸로, $A$와 만나지 않는 $x$의 어떠한 근방이 존재한다 가정하자. 그럼 이 근방에 포함된 $x$의 열린근방 $U$가 $A$와 만나지 않으므로, $U\cap A=\emptyset$이다. 이제 $U^c\cap A=A$이므로 $U^c$는 $A$를 포함하는 닫힌집합이고, closure의 최소성에 의하여 $U^c$는 $\cl A$ 또한 포함한다. 즉, $x\not\in U^c$이면 $x\not\in\cl A$이고, 따라서 반대방향도 성립한다.  

</details>

<div class="proposition" markdown="1">

<ins id="crl7">**따름정리 7**</ins> 위상공간 $X$가 주어졌다 하자. 열린집합 $A$와 임의의 집합 $B$에 대하여, 다음의 식

$$A\cap\cl(B)\subseteq\cl(A\cap B)$$

이 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$x\in A\cap\cl(B)$라 하자. $A$는 $x$의 열린근방이므로, $x$의 임의의 근방 $V$에 대하여 $V\cap A$ 또한 $x$의 근방이 된다. 따라서 $x\in\cl(B)$인 것과 [명제 6](#pp6)으로부터 $(V\cap A)\cap B\neq\emptyset$임을 안다. 그런데 이는 $A\cap B$와 $V$의 교집합이 공집합이 아니라는 것으로 해석할 수도 있고, $V$는 $x$의 임의의 근방이므로 다시 [명제 6](#pp6)에 의하여 $x\in\cl(A\cap B)$이다.

</details>

<div class="definition" markdown="1">

<ins id="df8">**정의 8**</ins> 위상공간 $X$와 $X$의 임의의 부분집합 $A$에 대하여, $x\in X$가 $A$의 *limit point<sub>극한점</sub>*이라는 것은 $x$의 임의의 근방이 $x$ 자기 자신을 제외한 점에서 $A$와 만나는 것이다. 

</div>

만일 $x\in\cl(A)\setminus A$라면, [명제 6](#pp6)에 의하여 $x$는 반드시 $A$의 limit point여야 하는 것을 안다. 반면, $x\in A$라 하면 이것이 반드시 참일 필요가 없다. 이와 같이 $x\in A$에 대하여 적당한 근방 $V$가 존재하여 $V\cap A=\\{x\\}$이도록 할 수 있다면 $x$가 $A$의 *isolated point<sub>고립접</sub>*이라 부른다. Isolated point를 갖지 않는 닫힌집합을 *perfect set<sub>완전집합</sub>*이라 부른다.

## 집합의 경계

<div class="definition" markdown="1">

<ins id="df9">**정의 9**</ins> 위상공간 $X$의 임의의 부분집합 $A$에 대하여, $A$의 *boundary<sub>경계</sub>*는 다음의 식

$$\partial A=\cl A\setminus\interior A$$

으로 정의되는 집합 $\partial A$이다. 

</div>

따라서 $\partial A$는 닫힌집합이다. 

## 조밀집합

<div class="definition" markdown="1">

<ins id="df10">**정의 10**</ins> 위상공간 $X$의 임의의 부분집합 $A$가 *dense subset<sub>조밀 부분집합</sub>*이라는 것은 $\cl(A)=X$인 것이다.

</div>

[명제 6](#pp6)에 의하여, $A$가 $X$에서 dense라는 것은 공집합이 아닌 $X$의 열린집합이 반드시 $A$와 만난다는 것을 의미한다. 직관적으로 $X$의 dense subset을 찾으면, 약간의 perturbation만 거치면 $X$를 전부 얻어낼 수 있다는 것으로 생각할 수 있다. 이를 더 일상적인 언어로 쓰면 $X$의 dense subset은 $X$의 "거의 모든" 부분을 포함한다고 생각할 수 있다.

한편, 위상수학에서도 크기의 개념은 basis의 크기로 주어지는데, 이는 다음 명제에 따른 것이다.

<div class="proposition" markdown="1">

<ins id="pp11">**명제 11**</ins> 위상공간 $X$의 basis $\mathcal{B}$에 대하여, $\card(D)\leq\card(\mathcal{B})$이도록 하는 $X$의 dense subset $D$가 존재한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

각각의 $U\in\mathcal{B}$마다 원소 $x_U\in U$를 하나씩 뽑아, 이들의 모임을 $D$로 잡으면 된다. 집합 $D$가 dense인 것은 임의의 열린집합 $V$가 주어질 때마다, 이를 $\mathcal{B}$의 원소들의 합집합으로 표현할 수 있고, 이 합집합은 반드시 어떤 $x_U$를 포함해야 하므로 $V\cap D\neq\emptyset$이기 때문에 성립한다.

</details>