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

임의의 위상 $\mathcal{T}$를 다루기보다, 그 basis $\mathcal{B}$를 생각하듯, 임의의 filter 또한 적당한 filter base의 개념을 갖는다.

<div class="definition" markdown="1">

<ins id="df2">**정의 2**</ins> $X$의 부분집합들의 모임 $\mathcal{B}$가 다음의 두 조건

1. $\mathcal{B}$의 임의의 두 원소의 교집합은 $\mathcal{B}$의 어떤 원소를 포함한다.
2. $\mathcal{B}\neq\emptyset$이고 $\emptyset\not\in\mathcal{B}$이다. 

그럼 $\mathcal{B}$의 원소를 포함하는 집합들의 모임 $\mathcal{F}$가 되며, 이 때 $\mathcal{B}$를 $\mathcal{F}$의 *filter base*라 한다.

</div>

<div class="definition" markdown="1">

<ins id="df3">**정의 3**</ins> 위상공간 $X$에 대하여, $x\in X$가 filter base $\mathcal{B}$의 *cluster point*라는 것은 $\mathcal{B}$의 임의의 원소의 closure가 $x$를 항상 포함하는 것이다.

</div>

따라서, $x\in X$가 filter base $\mathcal{B}$의 cluster point라는 것은 임의의 $N\in\mathcal{N}(x)$와 $B\in\mathcal{B}$에 대하여 $N\cap B\neq\emptyset$인 것이다. ([§수열의 수렴, 명제 2](/ko/math/topology/basic_definition_3#pp2)) 

## Convergence of net

---

**참고문헌**

**[Sch]** E. Schechter, <i>Handbook of Analysis and Its Foundations</i>. Elements of mathematics. Academic Press, 1997.  
**[Mun]** J.R. Munkres, <i>Topology</i>. Featured Titles for Topology. Prentice Hall, Incorporated, 2000.

---

[^1]: 만일 수열들의 수렴에 대한 정보를 정확히 알고 있다면, 함수 $\operatorname{cl}:\mathcal{P}(X)\rightarrow\mathcal{P}(X)$를, 집합 $A$를 받아 <phrase>$A$의 원소들로 이루어진 수열의 수렴값들의 집합</phrase>으로 보내는 함수로 정의하면 된다.