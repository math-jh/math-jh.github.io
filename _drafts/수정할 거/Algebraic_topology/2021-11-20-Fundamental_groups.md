---

title: "Fundamental groups"
excerpt: "Basic notions"

categories: [Math / Algebraic Topology]
permalink: /ko/math/algebraic_topology/fundamental_groups
header:
    overlay_image: /assets/images/Background/Galois-Theory_Algebraic-extension.png
    overlay_filter: 0.5
sidebar: 
    nav: "topology"

date: 2021-11-20
last_modified_at:
weight: 300

published: false

---
<div class="notice--warning" markdown="1">

이 글은 현재 수정중입니다.

이 글은 예전에 쓴 글로, 서술 방향이 마음에 들지 않거나 표기법이 마음에 들지 않아 전체적으로 수정이 진행중입니다. 읽으실 때 참고해주세요.

</div>

## Basic definition

우리는 이미 homotopy equivalence를 설명하며 path homotopy를 정의한 적이 있다. 이 때는 두 path $f_0$, $f_1$이 path homotopic임을 나타내기 위해 $f_0\simeq_p f_1$과 같은 notation을 사용했는데, 이 notation은 아무래도 거추장스러우므로 이 경우에도 $f_0\simeq f_1$과 같이 적기로 하자.

<div class="example" markdown="1">

<ins id="ex1">**예시 1**</ins> 우리가 잘 아는 공간 $\mathbb{R}^n$에서의 예시를 먼저 생각해보자. Endpoint들을 공유하는 임의의 두 path $f_0$, $f_1$은 항상 path homotopic하다. 이는 다음의 map

$$f_t(s)=(1-t)f_0(s)+tf_1(s)$$

으로부터 자명하다. 직관적으로 이야기해서, 이 homotopy는 동일하게 parametrize된 두 path $f_0$, $f_1$이 주어졌을 때, 이 path의 시간 $s$에 해당하는 두 점을 직선으로 이어서 얻어진다. 때문에 이를 *linear homotopy*라 부른다.

</div>

더 일반적으로, $\mathbb{R}^n$의 임의의 convex subspace를 생각하면 두 path $f_0$, $f_1$ 위의 임의의 두 점을 잇는 직선이 항상 이 공간에 포함될 것이므로, 위의 예시를 동일하게 적용하여 임의의 두 path가 path homotopic임을 보일 수 있다. 또, 약간의 상상력을 발휘하면 이런 상황이 깨지는 것은 두 path 사이에 구멍이 뚫려 있는 경우가 된다는 것도 쉽게 알 수 있다. 

우리는 path homotopy를 나타내는 relation $\simeq$가 equivalence relation이라는 것을 안다. 따라서, 임의의 path $f$에 대해 이 relation에서의 equivalence class를 생각할 수 있다.

<div class="definition" markdown="1">

<ins id="df2">**정의 2**</ins> Topological space $X$와, $X$에서 정의된 path $f$를 생각하자. 그럼 path homotopy를 나타내는 equivalence relation $\simeq$에 대한 $f$의 representative를 $[f]$로 적고, 이를 $f$의 *homotopy class*라 부른다.

</div>

이들 homotopy class들의 모임에는 자연스러운 연산이 존재한다. 두 path $f$, $g$가 $f(1)=g(0)$을 만족할 경우, 즉 $f$의 끝점이 $g$의 시작점일 경우 우리는 이 두 path를 이어서 하나의 path로 취급할 수 있다. 더 explicit하게, 이 path $f\cdot g$는 다음의 식

$$f\cdot g(s)=\begin{cases} f(2s)&0\leq s\leq 1/2\\ g(2s-1)&1/2\leq s\leq 1\end{cases}$$

으로 정의되는 path이다. 이를 $f$와 $g$의 *composition*이라 부른다. $\cdot$을 일종의 연산으로 본다면, 이는 항상 결합법칙을 만족한다는 것을 알 수 있다. 또, $f$의 시작점을 함수값으로 갖는 상수함수와 $f$를 합성하면 (up to reparametrization) 그 결과는 $f$와 같고, 마찬가지로 $f$의 끝점을 함수값으로 갖는 상수함수와 $f$를 합성하여도 그 결과는 $f$와 같다는 것을 쉽게 확인할 수 있다. 즉, 상수함수가 일종의 항등원 역할을 한다. 뿐만 아니라, $f$가 주어진다면 $f$를 *거꾸로* 뒤집어둔 path $\bar{f}(s)=f(1-s)$가 $f$의 inverse가 된다는 것을 확인할 수 있다. 요컨대 $\cdot$이 주어진 homotopy class들의 집합은 groupoid를 이룬다. 일반적으로 groupoid는 그렇게 다루기 좋은 대상은 아니므로, 시작점과 끝점을 모두 동일하게 맞춰버리면 다음의 정의를 얻는다.

<div class="definition" markdown="1">

<ins id="df3">**정의 3**</ins> Topological space $X$와 $X$의 한 점 $x_0$가 주어졌다고 가정하자. 그럼 $x_0$을 basepoint로 갖는 loop들의 집합을 $\pi_1(X,x_0)$이라 적는다. 이 집합은 $\cdot$에 의해 group structure를 가지며, 이를 *fundamental group*이라 부른다. 

</div>

이렇게 시작점과 끝점을 동일하게 맞추는 것은 기본적으로 basepoint의 선택에 의존하므로, $\pi_1(X,x_0)$은 $X$ 전체에 대한 정보를 줄 이유가 전혀 없다. 하지만 다음 명제에 따르면, $\pi_1(X,x_0)$은 적어도 $x_0$이 포함되어 있는 path component 안에서는 basepoint의 선택에 의존하지 않으며, 따라서 만일 $X$가 path-connected라면 $\pi_1(X,x_0)$은 basepoint에 무관하게 결정된다는 것을 알 수 있다.

<div class="proposition" markdown="1">

<ins id="pp4">**명제 4**</ins> Topological space $X$의 한 점 $x_0$에서 정의된 fundamental group $\pi_1(X,x_0)$을 생각하자. 만일 $x_1\in X$가 $x_0$과 동일한 path component에 포함되어 있고, $h$가 $x_0$와 $x_1$을 잇는 path라면, 다음의 식

$$[f]\mapsto [h\cdot f\cdot \bar{h}]$$ 

으로 정의된 map $\beta_h:\pi_1(X,x_0)\rightarrow\pi_1(X,x_1)$은 isomorphism이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선, 임의의 $[f],[g]\in\pi_1(X,x_0)$에 대하여 

$$[h\cdot (f\cdot g)\cdot\bar{h}]=[(h\cdot f\cdot\bar{h})\cdot(h\cdot g\cdot\bar{h})]=[h\cdot f\cdot\bar{h}][h\cdot g\cdot\bar{h}]$$

이 성립하므로 $\beta_h$는 group homomorphism이다. 또, 어렵지 않게 $\beta_{\bar{h}}:\pi_1(X,x_1)\rightarrow\pi_1(X,x_0)$이 $\beta_h$의 inverse임을 확인할 수 있다. 
</details>

이런 측면에서, 만약 $X$가 path connected space라면 $\pi_1(X,x_0)$ 대신 간단히 이 group을 $\pi_1(X)$ 혹은 더 간단하게 $\pi_1X$로 적기도 한다.

## Fundamental group of the circle

우리가 fundamental group을 바탕으로 (path-connected) topological space들을 분류하기로 작정한다면, 가장 간단한 예시는 아마도 fundamental group이 trivial group일 때가 될 것이다.

<div class="definition" markdown="1">

<ins id="df5">**정의 5**</ins> Topological space $X$가 *simply connected*라는 것은 $X$가 path-connected이고, $X$의 fundamental group이 trivial인 것이다. 

</div>

앞서 우리는 [예시 1](#ex1)에서 $\mathbb{R}^n$의 임의의 convex subset에 대해서는 endpoint를 공유하는 두 path 사이에 항상 homotopy가 존재한다는 것을 언급한 적이 있다. 사실 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="pp6">**명제 6**</ins> Topological space $X$가 simply connected인 것은, $X$의 임의의 두 점에 대해, 이들을 잇는 path들의 유일한 homotopy class가 존재하는 것이다.

</div>
즉, $X$가 simply connected인 것은 임의의 두 점 $x_0,x_1\in X$가 주어져 있을 때, (1) 이들 사이의 path가 존재하고, (2) 이들 path들은 모두 서로 homotopic한 것과 동치이다.
<details class="proof--alone" markdown="1">
<summary>증명</summary>

우선 $X$가 simply connected라 가정하면, $X$는 path-connected이므로 위에서 언급한 첫 번째 조건이 성립한다. 이제 이들 path들이 모두 homotopic함을 보이자. 두 점 $x_0,x_1\in X$에 대해, $f,g$가 $x_0$과 $x_1$을 잇는 path라 하자. 그럼 우선 $f\cdot\bar{g}$는 $x_0$을 basepoint로 갖는 loop이므로, $\pi_1(X,x_0)$의 원소이고 따라서 constant loop와 homotopic하다. 또, $\bar{g}\cdot g$는 원래부터 constant loop와 homotopic하다. 이제

$$f\simeq f\cdot \bar{g}\cdot g\simeq g$$

가 성립하므로 $f$와 $g$는 homotopic하다. 

거꾸로 $X$의 임의의 두 점에 대해, 이들을 잇는 path가 모두 서로 homotopic하다고 가정하자. 그럼 양 끝점을 모두 동일하게 $x_0$으로 잡으면, 이 말은 $\pi_1(X,x_0)$의 모든 원소가 서로 homotopic하다는 것과 같은 말이고, 따라서 $x_0$을 basepoint로 갖는 임의의 loop는 $\pi_1(X,x_0)$의 원소 중 하나인 constant loop와도 homotopic해야 한다. 

</details>

우리는 해당 예시의 말미에서, 이와 같은 일이 성립하지 않는 경우는 두 개의 path 사이에 구멍이 뚫려 있는 경우라고 주장했었다. 이에 대한 대표적인 예시는 $\pi_1(S^1)$이 될 것이다. 예를 들어, $S^1$의 두 antipodal point를 잇는 위쪽 path와 아래쪽 path는 서로 path-homotopic하지 않다. 따라서 $\pi_1(S^1)$은 반드시 nontrivial한 group structure를 가져야 한다. 이 group을 직접 계산하기 위해서는 몇 가지 사전준비가 필요하다.

<div class="definition" markdown="1">

<ins id="df7">**정의 7**</ins> Topological space $X$에 대하여, 또 다른 topological space $\widetilde{X}$가 $X$의 *covering space*라는 것은, *covering map* $p:\widetilde{X}\rightarrow X$가 존재하여 다음의 조건

> 임의의 $x\in X$에 대하여, $x$의 neighborhood $U$가 존재하여 $p^{-1}(U)$는 <span class="border-highlight">각각이 $p$에 의해 homeomorphic하게 $U$로 보내지는</span> disjoint open set들의 합집합이다.

</div>

이들 한 조각을 각각 $p^{-1}(U)$의 *slice*라 부르고, 또 이 때 $U$는 $p$에 의해 *evenly covered*된다고 부른다. 대표적인 covering space의 예시는 $S^1$을 $\mathbb{R}$로 cover하는 것인데, 예를 들어 $S^1$이 $\mathbb{R}^2$ 상에 embed되어있다고 하면, $p(x)=(\cos2\pi x,\sin2\pi x)$으로 정의된 map $p$는 covering map이 된다. 

<div class="definition" markdown="1">

<ins id="df8">**정의 8**</ins> $p:\widetilde{X}\rightarrow X$가 continuous map이라 하자. 만일 $f:Y\rightarrow X$가 또 다른 topological space $Y$에서 $X$로의 continuous map이라면, $f$의 *lifting*은 $p\circ\tilde{f}=f$를 만족하는 map $\tilde{f}:Y\rightarrow \widetilde{X}$이다.   

</div>

Covering map의 중요한 성질 중 하나는 임의의 path가 항상 lift될 수 있다는 것이다. (이를 path-lifting property라 부른다.)

<div class="proposition" markdown="1">

<ins id="pp9">**명제 9**</ins> $p:\widetilde{X}\rightarrow X$가 covering map이고, $p(\tilde{x}_0)=x_0$이라 하자. 그럼 $x_0$에서 시작하는 임의의 path $f:I\rightarrow B$는 $\tilde{x}_0$에서 시작하는 유일한 lifting $\tilde{f}$를 갖는다.

</div>

또, covering map은 path 하나 뿐만이 아니라, path들 사이의 homotopy 또한 lift할 수 있다. 즉,

<div class="proposition" markdown="1">

<ins id="pp10">**명제 10**</ins> $p:\widetilde{X}\rightarrow X$가 covering map이고, $p(\tilde{x}_0)=x_0$이라 하자. $F:I\times I\rightarrow X$가 $F(0,0)=b_0$을 만족하는 continuous map이라면 $\tilde{F}(0,0)=\tilde{x}_0$인 유일한 lifting $\tilde{F}:I\times I\rightarrow E$가 존재한다. 특히, 만일 $F$가 path homotopy를 나타낸다면, $\tilde{F}$ 또한 그러하다. 

</div>

이들 두 명제는 모두 다음의 보조정리로부터 얻어진다.

<div class="proposition" markdown="1">

<ins id="lem11">**보조정리 11**</ins> 임의의 continuous map $F:Y\times I\rightarrow X$가 주어졌고, $\tilde{F}:Y\times 0\rightarrow\widetilde{X}$가 $F\|\_{Y\times 0}$의 lifting이라 하자. 그럼 $\tilde{F}$를 extend하는 map이 유일하게 존재하여 $F$의 lifting이 된다.

</div>

<div class="proposition" markdown="1">

<ins id="thm12">**정리 12**</ins> $\pi_1(S^1)\cong \mathbb{Z}$.

</div>



---

**Reference**

[Hat] A. Hatcher, *Algebraic Topology*. Combradge University Press, 2022 

---
