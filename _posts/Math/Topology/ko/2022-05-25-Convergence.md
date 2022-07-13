---

title: "위상공간과 수렴<sup>†</sup>"
excerpt: "Closure axiom, Filter, "

lang: ko

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

<ins id="lem0">**보조정리 (The sequence lemma)**</ins> 거리공간 $X$와 그 부분집합 $A$에 대하여, $x\in\operatorname{cl}A$인 것과, <box>적당한 $A$의 수열 $(x_n)$이 존재하여 $x_n\rightarrow x$인 것</box>이 동치이다.

</div>

바꾸어 말하자면, 만일 $X$가 거리공간이라면, <em_ko>어떠한 수열이 언제, 어디로 수렴하는지</em_ko>만 정확하게 안다면, 임의의 부분집합 $A$에 대하여 $\operatorname{cl}A$를 정의할 수 있고[^1], 그럼 [§위상공간의 다른 정의들, 정의 1](/ko/math/topology/equivalent_definition_of_topology)을 통해 $X$의 위상구조를 정확하게 알아낼 수 있다. 물론 


그러나 $X$가 거리공간이 아니라면 이것이 불가능하다. 이를 해결하기 위해 우리는 수렴성을 확장해야 하는데, 이는 크게 filter와 net을 이용한 두 가지의 방법이 있다.

## Convergence of filter

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> 위상공간 $X$가 주어졌다 하자. $X$ 위에 정의된 filter $\mathcal{F}$에 대하여, $x\in X$가 $\mathcal{F}$의 *limit point*라는 것은 $\mathcal{N}(x)\subset\mathcal{F}$인 것이다. 

</div>


## Convergence of net

---

**참고문헌**

**[Mun]** J.R. Munkres, <i>Topology</i>. Featured Titles for Topology. Prentice Hall, Incorporated, 2000.

---

[^1]: 만일 수열들의 수렴에 대한 정보를 정확히 알고 있다면, 함수 $\operatorname{cl}:\mathcal{P}(X)\rightarrow\mathcal{P}(X)$를, 집합 $A$를 받아 <box>$A$의 원소들로 이루어진 수열의 수렴값들의 집합</box>으로 보내는 함수로 정의하면 된다.