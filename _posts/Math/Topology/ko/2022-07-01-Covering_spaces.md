---

title: "피복공간"
excerpt: "Covering space"

categories: [Math / Topology]
permalink: /ko/math/topology/covering_spaces
header:
    overlay_image: /assets/images/Topology/Covering_spaces.png
    overlay_filter: 0.5
sidebar: 
    nav: "topology-ko"

date: 2022-07-01
last_modified_at: 2022-07-01
weight: 103
    
---

우리는 앞서 $S^1$의 fundamental group을 계산하기 위해 covering space를 사용했다. 이번 글에서는 covering space들의 더 깊은 성질들을 살펴본다. 우선 다음의 정의를 기억하자.

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> 위상공간 $X$에 대하여, $p:\tilde{X}\rightarrow X$가 *covering space<sub>피복공간</sub>*이라는 것은 각각의 $x\in X$마다 적당한 열린근방 $U$가 존재하여 $p^{-1}(U)$가 $U$와 homeomorphic한 여러 개의 slice들의 disjoint union으로 표현할 수 있는 것이다.

</div>


$p:\tilde{X}\rightarrow X$에 대하여, 위의 조건을 만족하는 열린근방 $U$는 $p$에 의하여 *evenly covered*되었다고 한다. 따라서 위의 조건은 임의의 $x\in X$마다 evenly covered open neighborhood가 존재한다는 것으로 간추릴 수 있다. 

다음 명제 또한 지난 글에서 이미 증명했던 것이다.

<div class="proposition" markdown="1">

<ins id="pp2">**명제 2**</ins> Covering space $p:\tilde{X}\rightarrow X$가 주어졌다 하고, $f_0, f_1:Y\rightarrow X$ 사이의 homotopy $(f\_t)\_{0\leq t\leq 1}$가 주어졌다 하자. 만일 $\tilde{f}\_0:Y\rightarrow\tilde{X}$가 $p\circ\tilde{f}\_0=f\_0$을 만족한다면, $p\circ\tilde{f}\_t=f\_t$를 만족하는 homotopy $(\tilde{f}\_t)\_{0\leq t\leq 1}$이 존재한다.

</div>

일반적으로 $X$에서 정의된 path $\sigma$가 있을 때, 이 $\tilde{X}$에서의 path 중 그 image $p\circ\tilde{\sigma}$가 $\sigma$와 일치하도록 하는 $\tilde{\sigma}$는 무수히 많을 수 있다. 예를 들어 $\mathbb{R}\rightarrow S^1$에서, $S^1$ 상의 점 $(1,0)$에서 출발하여 원주 $1/4$바퀴를 도는 path $\sigma$가 주어졌다 하자. 그럼 $\mathbb{R}$로 올라갔을 때는 $[n, n+1/4]$를 움직이는 path들 중 어떠한 것을 택하더라도 이들의 image가 $\sigma$가 된다. 하지만 위의 명제와 같이 시작점 $n$이 고정된다면 이러한 path는 유일하게 결정된다. 

또, 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="pp3">**명제 3**</ins> $p:\tilde{X}\rightarrow X$가 covering space이고, $p(\tilde{x}\_0)=x\_0$이라 하자. 그럼 $p\_\ast:\pi\_1(\tilde{X},\tilde{x}\_0)\rightarrow\pi\_1(X,x\_0)$는 injection이며, 그 image는 $x\_0$를 base point로 갖는 고리들 중 $\tilde{x}\_0$를 base point로 갖는 고리들이다.

</div>

