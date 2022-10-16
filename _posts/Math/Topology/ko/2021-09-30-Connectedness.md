---

title: "연결공간"
excerpt: ""

categories: [Math / Topology]
permalink: /ko/math/topology/connectedness
header:
    overlay_image: /assets/images/Topology/Connectedness.png
    overlay_filter: 0.5
sidebar: 
    nav: "topology-ko"

date: 2021-09-29
last_modified_at: 2022-04-07
weight: 13

published: false
    
---

우리는 지금까지 위상공간을 정의하고, 이 위에서 정의된 수열의 수렴이나 연속함수를 살펴봤다. 그러나 아직까지 위상공간이 우리가 알고 있던 일상적인 공간을 어떤 방식으로 설명하는지는 명확하지 않다. 때문에 당분간은 우리가 일상적으로 알고 있는 공간들이 갖는 성질을 위상수학의 언어로 바꿔가는 일을 계속 할 것이다. 

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> 위상공간 $X$가 주어졌다 하자. 두 부분집합 $U,V$가 $X$의 *separation<sub>분리</sub>*이라는 것은 $U,V$가 모두 공집합이 아닌 열린집합이고 이들이 $X$의 partition을 이루는 것이다. 만일 $X$의 separation이 존재하지 않는다면 $X$를 *connected space<sub>연결공간</sub>*라 부른다. 

</div>

만일 서로소이고 공집합이 아닌 두 열린집합 $U,V$에 대하여 $X=U\cup V$라면 $V=U^c$이므로 $V$는 닫힌집합이기도 하며, $U$ 또한 마찬가지이다. 따라서 $X$가 connected가 아니라면 공집합도, $X$ 전체도 아닌 clopen set이 존재한다. 거꾸로 $X$가 공집합도, 전체집합도 아닌 clopen set $U$를 갖는다면 $U$는 닫힌집합이므로 $U^c$는 열린집합이고, 따라서 $X=U\cup U^c$에서 $X$가 connected가 아님을 안다. 

<div class="definition" markdown="1">

<ins id="df2">**정의 2**</ins> 위상공간 $X$와 한 점 $x\in X$에 대하여, $x$를 포함하는 $X$의 connected subspace 가운데 가장 큰 것을 $x$를 포함하는 *component*라 정의한다.

</div>

이를 위해서는 점 $x$를 포함하는 임의의 connected subspace들 $A_i$의 합집합이 여전히 $X$의 connected subspace가 된다는 것을 보여야 한다.

<div class="proposition" markdown="1">

<ins id="lem3">**보조정리 3**</ins> 임의의 점 $x\in X$와 $x$를 포함하는 connected subspace들의 모임 $\\{A\_i\\}\_{i\in I}$에 대하여, $A=\bigcup A_i$는 $X$의 connected subspace이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$X$의 두 열린집합 $U,V$에 대하여, $U'=U\cap A$, $V'=V\cap A$가 다음의 식

$$U'\cup V'=A,\qquad U'\cap V'=\emptyset$$

을 만족한다. 이제 $x\in A$이므로, $U'$과 $V'$ 중 $x$를 포함하는 집합이 정확히 하나 존재한다. 일반성을 잃지 않고 $x\in U'$이라 하자. 임의의 $i\in I$에 대하여, 

$$(U\cap A_i)\cup(V\cap A_i)=(U\cup V)\cap A_i=A_i,\qquad (U\cap A_i)\cap(V\cap A_i)=\emptyset$$

이고 $A_i$들은 모두 connected이며 $x\in U\cap A_i$이므로 반드시 $V\cap A_i=\emptyset$이다. 따라서 

$$V'=V\cap A=V\cap\left(\bigcup_{i\in I} A_i\right)=\bigcup_{i\in I} (V\cap A_i)=\emptyset$$

이 되어 $A$는 connected이다.

</details>

한편 임의의 $x\in X$에 대하여 $\\{x\\}$는 connected subspace이므로, 이를 통해 임의의 공간 $X$는 connected component들로 이루어진 partition을 갖는다는 것을 확인할 수 있다. 이를 $\\{U\_i\\}\_{i\in I}$라 하자. 만일 $I_1,I_2$가 $I$의 분할이라면 

$$X=\left(\bigcup_{i\in I_1}U_i\right)\cup\left(\bigcup_{i\in I_2}U_i\right),\qquad \left(\bigcup_{i\in I_1}U_i\right)\cap\left(\bigcup_{i\in I_2}U_i\right)=\emptyset$$

이므로 이들 집합들이 $X$의 separation을 이룬다. 거꾸로 $X$의 임의의 separation은 반드시 이런 식으로 표현될 수 있다. 또, [보조정리 3](#lem3)으로부터, $X$의 임의의 connected subset은 반드시 $U_i$들 중 하나에 완전히 포함되어야 한다는 사실을 안다.

<div class="proposition" markdown="1">

<ins id="crl4">**따름정리 4**</ins> Connected space $X,Y$에 대하여, $X\times Y$ 또한 connected이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>



</details>

따라서 임의의 유한한 곱에 대한 connected space들의 곱은 connected이다. 그러나 이는 무한한 곱에 대해서는 성립할 필요가 없다.

Connectedness를 살펴봐야 할 이유는 이것이 위상적인 성질이기 때문이다. 즉, connectedness는 연속함수에 의해 보존된다.

<div class="proposition" markdown="1">

<ins id="pp5">**명제 5**</ins> 임의의 공간 $X,Y$와 연속함수 $f:X\rightarrow Y$에 대하여, 만일 $X$가 connected space라면 $f(X)$는 $Y$의 connected subspace이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>



</details>

Connected set의 예시 중 대표적인 것은 $\mathbb{R}$이며, 더 일반적으로 $\mathbb{R}$의 임의의 interval들은 connected임을 확인할 수 있다. 따라서 다음 정리는 미적분학때 다루었던 중간값 정리의 일반화라 할 수 있다.

<div class="proposition" markdown="1">

<ins id="thm6">**정리 6**</ins> Connected space $X$에 대하여, 연속함수 $f:X\rightarrow\mathbb{R}$이 주어졌다 하자. 임의의 $a,b\in X$와, $f(a),f(b)$ 사이의 점 $r\in Y$가 주어졌다 하면 $f(c)=r$을 만족하는 점 $c\in X$가 존재한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>



</details>

이 정리는 $\mathbb{R}$ 대신 order topology가 주어진 집합 $Y$로 대체하여도 성립하며, 그 증명도 동일하다. 하지만 어쨌든 더 일반화된 버전을 사용할 일이 별로 없다.

<div class="definition" markdown="1">

<ins id="df7">**정의 7**</ins> 위상공간 $X$가 *locally connected*라는 것은 임의의 $x\in X$와 $x$의 neighborhood $U$가 주어질 때마다, $U$에 포함되는 $x$의 connected neighborhood $V$가 존재하는 것이다.

</div>

다음 명제를 어렵지 않게 증명할 수 있다.

<div class="proposition" markdown="1">

<ins id="pp8">**명제 8**</ins> 위상공간 $X$가 locally connected인 것은 임의의 열린집합 $U$에 대하여, $U$의 component들이 $X$의 부분집합으로서도 열린집합인 것이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>



</details>

---

**참고문헌**

**[Bou]** N. Bourbaki, <i>General Topology</i>. Elements of mathematics. Springer, 1995.

---
