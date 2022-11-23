---

title: "Cell complexes"
excerpt: "Basic notions"

categories: [Math / Algebraic Topology]
permalink: /ko/math/algebraic_topology/cell_complexes
header:
    overlay_image: /assets/images/Algebraic_topology/Cell_complexes.png
    overlay_filter: 0.5
sidebar: 
    nav: "topology"

date: 2021-11-19
last_modified_at:
weight: 2

publilshed: false

---
<div class="notice--warning" markdown="1">

이 글은 현재 수정중입니다.

이 글은 예전에 쓴 글로, 서술 방향이 마음에 들지 않거나 표기법이 마음에 들지 않아 전체적으로 수정이 진행중입니다. 읽으실 때 참고해주세요.

</div>

본격적으로 대수위상을 시작하기 전에, 우리가 사용할 도구를 먼저 소개해야 한다.

## CW complexes

우리가 CW complex라고 부를 물건은 다음과 같은 과정을 통해 얻어지는 공간이다.

1. 우선, discrete set $X^0$부터 시작한다. 즉, 이들은 서로 연결되어있지 않은 (possibly infinite) 점들의 집합이다. 우리는 이들을 $0$-cell이라 부를 것이다. 
2. 이제 여기에 $1$-cell들을 붙인다. $1$-cell들 각각은 $n-1$ dimensional disk $D^n$과 homeomorphic한 공간들이며, 우리가 이들을 $X^0$에 붙인다는 것은, 각각의 $1$-cell들 $e_\alpha^1$에 대하여, quotient map $\varphi_\alpha: S^{n-1}\rightarrow X^{n-1}$이 주어졌다는 것이다. 여기서 $S^{n-1}$은 물론 $\partial e_\alpha^n$을 의미한다. 이 과정을 통해 만들어진 구조를 $1$-skeleton이라 부른다.
3. 이 과정을 inductive하게 진행한다. 즉, $(n-1)$-skeleton에 $n$-cell들을 붙여 $n$-skeleton을 만들고, ... 
4. 이 과정이 유한한 step 안에 끝난다면, $X=X^n$으로 정의하면 된다. 이 경우, $X^n$에는 quotient topology가 잘 정의되어 있으므로 topological structure를 크게 신경쓸 필요가 없다. 아니면 우리는 이 과정을 무한히 반복하여 $X=\bigcup X_n$으로 정의할 수도 있다. 이 경우, 우리는 $X$에 weak topology를 준다.

이렇게 얻어지는 구조를 cell complex, 혹은 CW complex라 부른다. Cell complex라는 이름은 이 구조를 이루는 성분들이 $n$-cell들이니 자연스러운 이름이지만 CW complex는 다소 낯설다. CW는 이 구조가 갖는 두 가지 성질, 즉 *closure finiteness*와 *weak topology*의 약자이다. Weak topology야 방금 우리가 정의하는 데 쓰였으니 별 다른 설명이 필요없지만, 첫 번째 성질은 설명이 필요하다.

우선 몇 가지를 정의하고 넘어가자. 만일 4번 과정에서, $X=X^n$이라 하면 $X$가 *finite-dimensional*이라 하고, 이를 만족하는 $n$ 가운데에서 가장 작은 것을 $X$의 dimension으로 정의한다. 또, attaching map $\varphi_\alpha:S^{n-1}\rightarrow X^{n-1}$을 extend하는 $\Phi_\alpha: D_\alpha^n\rightarrow X$를 *characteristic map*이라 부른다. 더 explicit하게, 이 map은 우선 $D_\alpha^n$을 $X^{n-1}\sqcup_\alpha D_\alpha^n$으로 embed한 후, 이를 $\varphi_\alpha$에 의해 결정되는 quotient map을 통해 $X^n$으로 보내고, 그 후 $X^n$을 $X$로 embed하여 얻어진다. 마지막으로, CW complex $X$에 대하여, $X$의 closed subspace 가운데 $X$를 구성하는 cell들의 union으로 나타나는 subspace $A$를 $X$의 *subcomplex*라 부르고, pair $(X,A)$를 *CW pair*라고 부른다. 

이제 CW complex의 성질인 closure-finiteness를 설명할 수 있다.  

<div class="proposition" markdown="1">

<ins id="pp1">**명제 1**</ins> CW complex의 compact subspace는 finite subcomplex에 포함된다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

CW complex $X$의 compact set $C$가 주어졌다 하자. 우리는 우선 $C$가 유한히 많은 cell들과만 만난다는 것을 보이고, 그 후 이 유한히 많은 cell들은 유한히 많은 subcomplex에만 포함된다는 것을 보일 것이다.

우선, 결론에 반하여 $C$가 무한히 많은 cell들과 만난다고 가정하자. 그럼 $C$와 이들 cell들이 만나는 점들을 하나씩 뽑아서 무한집합 $S=\\{x\_1, x\_2,\ldots\\}$를 만들 수 있다. 그럼 $X^0$은 discrete set이었으므로, $X^0\cap S$는 closed이다. 이제 inductive하게 $S\cap X^{n-1}$이 $X^{n-1}$에서 closed였다 가정하고, 각각의 $n$-cell $e\_\alpha^n$을 생각하자. 그럼 $\varphi\_\alpha^{-1}(S)$는 inductive hypothesis에 의해 $\partial D\_\alpha^n$에서 closed이다. 또, $S$는 각각의 cell들과 많아야 한 번씩만 만나므로, $\Phi\_\alpha(S)$는 $\varphi_\alpha^{-1}(S)$에 많아야 한 점을 추가한 집합이고 따라서 $D_\alpha^n$에서 closed이다. 그러므로 induction에 의하여, $S\cap X^n$은 $X^n$에서 closed이고, weak topology의 정의에 의해 $S$는 $X$에서 closed이다. 따라서 $S$는 compact set $C$의 closed subspace이므로 compact이다. 그런데 위 argument를 그대로 따라하면 $S$의 임의의 부분집합이 closed임을 보일 수 있다. 즉, $S$는 discrete topology가 주어진 무한집합인데, 이는 $S$가 compact라는 사실에 모순이다.

이제 유한히 많은 cell들은 유한히 많은 subcomplex들에만 포함된다는 사실을 보이자. 어차피 finite subcomplex들의 유한한 union은 finite subcomplex에 포함될 것이므로, 이는 그냥 $n$-cell $e_\alpha^n$이 finite subcomplex에 포함된다는 것만 증명하면 충분하다. 그런데 $\varphi_\alpha$의 image를 생각하면 이 image는 compact이고, 따라서 dimension에 대한 induction을 통해 임의의 $n$-cell이 finite subcomplex에 포함된다는 것을 보일 수 있다. 

</details>

이제, $X$를 구성하는 임의의 cell에 closure를 취하면 이 closure는 compact이므로, 앞선 명제에 의해 이 집합은 유한히 많은 다른 cell들과만 만난다. 이 성질이 CW complex의 closure-finiteness다. 

---

**Reference**

[Hat] A. Hatcher, *Algebraic Topology*. Combradge University Press, 2022 

---
