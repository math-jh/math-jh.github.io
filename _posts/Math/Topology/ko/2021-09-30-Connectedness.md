---

title: "연결공간"
excerpt: ""

categories: [Math / Topology]
permalink: /ko/math/topology/connectedness
header:
    overlay_image: /assets/images/Topology/Topological_basis.png
    overlay_filter: 0.5
sidebar: 
    nav: "topology-ko"

date: 2021-09-29
last_modified_at: 2022-04-07
weight: 13
    
---

우리는 지금까지 위상공간을 정의하고, 이 위에서 정의된 수열의 수렴이나 연속함수를 살펴봤다. 그러나 아직까지 위상공간이 우리가 알고 있던 일상적인 공간을 어떤 방식으로 설명하는지는 명확하지 않다. 때문에 당분간은 우리가 일상적으로 알고 있는 공간들이 갖는 성질을 위상수학의 언어로 바꿔가는 일을 계속 할 것이다. 

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> 위상공간 $X$가 주어졌다 하자. 두 부분집합 $U,V$가 $X$의 *separation<sub>분리</sub>*이라는 것은 $U,V$가 모두 공집합이 아닌 열린집합이고 이들이 $X$의 partition을 이루는 것이다. 만일 $X$의 separation이 존재하지 않는다면 $X$를 *connected space<sub>연결공간</sub>*라 부른다. 

</div>

만일 서로소이고 공집합이 아닌 두 열린집합 $U,V$에 대하여 $X=U\cup V$라면 $V=U^c$이므로 $V$는 닫힌집합이기도 하며, $U$ 또한 마찬가지이다. 따라서 $X$가 connected가 아니라면 공집합도, $X$ 전체도 아닌 clopen set이 존재한다. 거꾸로 $X$가 공집합도, 전체집합도 아닌 clopen set $U$를 갖는다면 $U$는 닫힌집합이므로 $U^c$는 열린집합이고, 따라서 $XU\cup U^c$에서 $X$가 connected가 아님을 안다. 



---

**참고문헌**

**[Bou]** N. Bourbaki, <i>General Topology</i>. Elements of mathematics. Springer, 1995.

---
