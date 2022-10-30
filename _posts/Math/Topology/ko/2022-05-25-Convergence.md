---

title: "위상공간과 수렴<sup>†</sup>"
excerpt: "Closure axiom, Filter, "

categories: [Math / Topology]
permalink: /ko/math/topology/convergence
header:
    overlay_image: /assets/images/Topology/Topological_basis.png
    overlay_filter: 0.5
sidebar: 
    nav: "topology-ko"

date: 2022-05-25
last_modified_at: 2022-05-25
weight: 8
    
---

앞서 [§거리위상 (2), 보조정리 5](#/ko/math/topology/metric_topology_2)를 다시 쓰면 다음과 같다.

<div class="proposition" markdown="1">

<ins id="lem0">**보조정리 (The sequence lemma)**</ins> 거리공간 $X$와 그 부분집합 $A$에 대하여, $x\in\operatorname{cl}A$인 것과, <phrase>적당한 $A$의 수열 $(x_n)$이 존재하여 $x_n\rightarrow x$인 것</phrase>이 동치이다.

</div>

바꾸어 말하자면, 만일 $X$가 거리공간이라면, <em_ko>어떠한 수열이 언제, 어디로 수렴하는지</em_ko>만 정확하게 안다면, 임의의 부분집합 $A$에 대하여 $\operatorname{cl}A$를 정의할 수 있고[^1], 그럼 [§위상공간의 다른 정의들, 정의 1](/ko/math/topology/equivalent_definition_of_topology)을 통해 $X$의 위상구조를 정확하게 알아낼 수 있다. 

반면 $X$가 거리공간이 아니라면 이것이 성립하지 않을 수도 있다. 이를 해결하기 위해 우리는 수렴성을 확장해야 하는데, 이는 크게 filter와 net을 이용한 두 가지의 방법이 있다. 이들은 수열의 수렴과는 달리 어떠한 공간에 대해서도 주어진 집합의 closure를 묘사할 때 절대로 실패하지 않는다.

## Convergence of filter

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> 위상공간 $X$가 주어졌다 하자. $X$ 위에 정의된 filter $\mathcal{F}$에 대하여, $x\in X$가 $\mathcal{F}$의 *limit point*라는 것은 $\mathcal{N}(x)\subset\mathcal{F}$인 것이다. 이 경우, $\mathcal{F}$가 $x$로 수렴한다고 한다.

</div>

$\mathcal{F}$가 $x$로 수렴하는 filter라 하자. 정의에 의해, $\mathcal{F}$보다 강한 filter $\mathcal{F}'$가 주어진다면 다음의 식

$$\mathcal{N}(x)\subseteq\mathcal{F}\subseteq\mathcal{F}'$$

으로부터 $\mathcal{F}'$ 또한 $x$로 수렴한다는 것을 안다. 비슷한 이유로, 집합 $X$ 위에 정의된 filter $\mathcal{F}$를 고정하고 $X$ 위의 위상 $\mathcal{T}$를 약한 위상 $\mathcal{T}'$로 대체한다면, 다음의 식

$$\mathcal{N}'(x)\subseteq\mathcal{N}(x)\subseteq\mathcal{F}$$

이므로 이 새로운 위상에서 filter $\mathcal{F}$ 또한 $x$로 수렴한다. 따라서 위상이 강해지면 강해질수록 특정한 점 $x$로 수렴하는 filter는 점점 더 적어지게 된다. 

이제 $\mathcal{C}$를 $X$ 위에 정의된 filter들 중, $x\in X$로 수렴하는 것들의 모임이라 하자. 그럼 $\Phi$에 속하는 임의의 filter $\mathcal{F}$에 대하여

$$\mathcal{N}(x)\subseteq\mathcal{F}$$

가 성립하므로, $\mathcal{N}(x)$는 $\bigcap\mathcal{C}$에 포함된다. 어렵지 않게 $\bigcap\mathcal{C}$ 자신도 filter가 됨을 확인할 수 있으므로, 이는 곧 $\mathcal{N}(x)$가 $\bigcap\mathcal{C}$보다 약한 filter가 된다는 것과 동등한 말이다. 따라서, 임의의 filter $\mathcal{F}$가 $x$로 수렴하는 것을 확인하기 위해서는 $\mathcal{F}$보다 강한 임의의 ultrafilter가 $x$로 수렴한다는 것을 증명하면 된다. 

임의의 위상 $\mathcal{T}$를 다루기보다 그 basis $\mathcal{B}$를 생각하듯, 임의의 filter 또한 적당한 filter base의 개념을 갖는다.

<div class="definition" markdown="1">

<ins id="df2">**정의 2**</ins> $X$의 부분집합들의 모임 $\mathcal{B}$가 다음의 두 조건

1. $\mathcal{B}$의 임의의 두 원소의 교집합은 $\mathcal{B}$의 어떤 원소를 포함한다.
2. $\mathcal{B}\neq\emptyset$이고 $\emptyset\not\in\mathcal{B}$이다. 

그럼 $\mathcal{B}$의 원소를 포함하는 집합들의 모임 $\mathcal{F}$가 filter가 되며, 이 때 $\mathcal{B}$를 $\mathcal{F}$의 *filter base*라 한다.

</div>

<div class="definition" markdown="1">

<ins id="df3">**정의 3**</ins> 위상공간 $X$에 대하여, $x\in X$가 filter base $\mathcal{B}$의 *cluster point*라는 것은 $\mathcal{B}$의 임의의 원소의 ($X$에서의) closure가 $x$를 항상 포함하는 것이다.

</div>

따라서, $x\in X$가 filter base $\mathcal{B}$의 cluster point라는 것은 임의의 $N\in\mathcal{N}(x)$와 $B\in\mathcal{B}$에 대하여 $N\cap B\neq\emptyset$인 것이다. ([§수열의 수렴, 명제 2](/ko/math/topology/basic_definition_3#pp2)) 

<div class="proposition" markdown="1">

<ins id="thm4">**정리 4**</ins> 위상공간 $X$와 $X$의 부분집합 $A$를 생각하자. 그럼 $A$에서 정의된 임의의 filter base $\mathcal{B}$에 대하여, $\mathcal{B}$의 모든 cluster point는 $\operatorname{cl}A$에 속한다. 거꾸로 $\operatorname{cl}A$의 모든 점은 $A$ 위에서 정의된 어떤 filter의 limit point가 된다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

앞선 정의에 의하여, $\mathcal{B}$의 cluster point들의 모임은 다음의 식

$$\bigcap_{B\in\mathcal{B}}\operatorname{cl}B$$

으로 주어지고, 이는 닫힌집합들의 교집합이므로 닫힌집합이다. 또, 만일 위의 집합이 원소 $x$를 갖는다면 모든 $B\in\mathcal{B}$에 대하여 $x\in\operatorname{cl}B$이고 따라서 $x$의 임의의 근방이 $B$와 만난다. 그런데 $B\subseteq A$이므로, 이러한 근방은 반드시 $A$와도 만나고 따라서 $x\in\operatorname{cl}A$가 성립한다.

거꾸로 $x\in\operatorname{cl}A$라 하자. 그럼 $x$의 neighborhood filter $\mathcal{N}(x)$에 대하여, 다음의 식

$$\mathcal{N}_A(x)=\{N\cap A: N\in\mathcal{N}(x)\}$$

으로 정의된 집합 $\mathcal{N}_A(x)$를 생각하자. 우선 $x\in\operatorname{cl}A$로부터 $\mathcal{N}_A(x)$는 $\emptyset$을 포함하지 않으며, 

1. 만일 $N_1\cap A, N_2\cap A\in\mathcal{N}_A(x)$라면 $(N_1\cap A)\cap(N_2\cap A)=(N_1\cap N_2)\cap A$이고
2. 만일 $N\cap A\in\mathcal{N}_A(x)$에 대하여, $N\cap A\subseteq P\subseteq A$라 하면 $P=(N\cup P)\cap A$이고 $N\cup P\in\mathcal{N}(x)$

이므로 $\mathcal{N}_A(x)$가 $A$ 위에서 정의된 filter가 된다. 뿐만 아니라, $x$는 $\mathcal{N}_A(x)$의 limit point이다.

</details>

## Convergence of net

Filter의 limit point의 개념은 이를 정의하기 위해 공간 $X$ 바깥의 어떠한 대상도 필요하지 않다는 점에서 내재적인 개념이라 할 수 있다. 반면 $X$에서 정의된 수열 $(x\_n)\_{n\in\mathbb{N}}$의 경우, 이를 정의하기 위해 집합 $\mathbb{N}$이 필요하다는 점에서 filter보다는 덜 내재적이다. 그럼에도 불구하고 수열은 우리에게 익숙하고, 다루기 쉬운 대상이므로 수열을 일반화하여 *net*을 정의한다.

<div class="definition" markdown="1">

<ins id="df5">**정의 5**</ins> 임의의 위상공간 $X$와 (right) directed set $I$에 대하여, 함수 $I\rightarrow X$를 $X$에서의 *net<sub>그물</sub>*이라 부른다. ([집합론, §순서집합의 원소들, 정의 13](/ko/math/set_theory/elements_in_ordered_set#df13))

</div>

특별히 수열은 $I=\mathbb{N}$인 경우의 net으로 생각할 수 있다. Net의 극한은 다음과 같이 정의할 수 있다.

<div class="definition" markdown="1">

<ins id="df6">**정의 6**</ins> 위상공간 $X$에서 정의된 net $(x\_i)\_{i\in I}$을 생각하자. $X$의 부분집합 $A$에 대하여, $(x\_i)$가 *eventually in $S$*라는 것은 적당한 $i\in I$가 존재하여, $j\geq i$를 만족하는 임의의 $j$마다 $x_j\in A$인 것이다. 만일 어떠한 $x\in X$에 대하여, $x$의 임의의 근방 $U$마다 $(x\_i)$가 eventually in $U$라면 $x$가 net $(x\_i)$의 *limit point*라 한다.

</div>

만일 $X$가 Hausdorff였다면 임의의 net은 많아야 하나의 limit point로만 수렴한다. 위에서 살펴본 filter와 마찬가지로, net의 수렴성 또한 집합의 closure를 정확하게 묘사할 수 있다.

<div class="proposition" markdown="1">

<ins id="thm7">**정리 7**</ins> 위상공간 $X$와 부분집합 $A$에 대하여, 임의의 net $I\rightarrow A$의 limit point는 반드시 $\operatorname{cl}A$에 속한다. 거꾸로 $\operatorname{cl}A$의 모든 점은 $A$ 위에서 정의된 어떤 net의 limit point가 된다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$A$ 위에서 정의된 net $(a\_i)\_{i\in I}$를 생각하자. $(a\_i)$의 임의의 limit point $a$와 근방 $U$에 대하여, $(a\_i)$가 eventually in $U$이므로 $U\cap A\neq\emptyset$이 반드시 성립한다. 따라서 [§수열의 수렴, 명제 2](/ko/math/topology/basic_definition_3#pp2)에 의하여 $a\in\operatorname{cl}A$가 성립한다.

거꾸로 $a\in\operatorname{cl}A$를 택하자. $a$의 neighborhood filter $\mathcal{N}(a)$를 생각하고, 여기에 다음의 식

$$U\leq V\iff U\supseteq V$$

으로 크기를 주면 임의의 $U,V\in\mathcal{N}(a)$에 대하여 $U\cap V\in\mathcal{N}(a)$이고 $U,V\leq U\cap V$이므로 $(\mathcal{N}(a),\leq)$는 directed set이 된다. 다시 [§수열의 수렴, 명제 2](/ko/math/topology/basic_definition_3#pp2)에 의해 임의의 $U\in\mathcal{N}(a)$마다 $A$의 원소 $a_U$를 하나씩 택할 수 있으므로, net $(a\_U)\_{U\in\mathcal{N}(a)}$를 만들 수 있다. 뿐만 아니라, $a$는 이 net의 limit point가 되는데, $a$의 임의의 근방 $U$가 주어졌을 때, $V\geq U$를 만족하는 임의의 $V$마다 $x_V\in V\subseteq U$이기 때문이다. 

</details>

---

**참고문헌**

**[Sch]** E. Schechter, <i>Handbook of Analysis and Its Foundations</i>. Elements of mathematics. Academic Press, 1997.  
**[Mun]** J.R. Munkres, <i>Topology</i>. Featured Titles for Topology. Prentice Hall, Incorporated, 2000.

---

[^1]: 만일 수열들의 수렴에 대한 정보를 정확히 알고 있다면, 함수 $\operatorname{cl}:\mathcal{P}(X)\rightarrow\mathcal{P}(X)$를, 집합 $A$를 받아 <phrase>$A$의 원소들로 이루어진 수열의 수렴값들의 집합</phrase>으로 보내는 함수로 정의하면 된다.