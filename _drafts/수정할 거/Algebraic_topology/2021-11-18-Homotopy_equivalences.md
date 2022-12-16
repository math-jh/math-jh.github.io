---

title: "Homotopy equivalences"
excerpt: "Basic notions"

categories: [Math / Algebraic Topology]
permalink: /ko/math/algebraic_topology/homotopy_equivalences
header:
    overlay_image: /assets/images/Algebraic_topology/Homotopy_equivalences.png
    overlay_filter: 0.5
sidebar: 
    nav: "topology"

date: 2021-11-18
last_modified_at:
weight: 1

published: false

---
<div class="notice--warning" markdown="1">

이 글은 현재 수정중입니다.

이 글은 예전에 쓴 글로, 서술 방향이 마음에 들지 않거나 표기법이 마음에 들지 않아 전체적으로 수정이 진행중입니다. 읽으실 때 참고해주세요.

</div>

## Introduction

위상수학은 공간들이 갖는 위상적인 성질들을 연구하는 분야다. 우리는 point-set topology에서, 이들 공간을 homeomorphism을 통해 분류했다. 이것은 본질적으로 group classification이나, 집합들의 cardinality를 정의하는 것과 크게 다르지 않다. Categorical sense에서 이건 별다른 것이 아니라, 단지 topological space들의 category $\mathbf{Top}$에서의 isomorphism들을 통해 ($\mathbf{Grp}$이나 $\mathbf{Set}$에서 그러했듯이) topological space들을 분류한 것이기 때문이다.

이러한 classification은 충분하다면 충분하고, 부족하다면 부족하다. 본질적으로, category $\mathbf{Top}$에서의 isomorphism인 homeomorphism은 topological property들을 보존하는 map들이므로, 이 isomorphism에 의해 동일하게 취급되는 공간들은 모두 동일한 topological property를 갖는다. 하지만, 우리가 생각할 수 있는 어떤 성질들은 서로 homeomorphic하지 않은 두 공간이 동시에 가질 수도 있다. 예를 들어, 우리가 underlying set의 cardinality에 집중한다고 하면 서로 homeomorphic하지 않은 두 공간 $\mathbb{R}$과 $\mathbb{R}^2$는 같은 cardinality를 가지므로, cardinality 센스에서 이 두 공간은 같다고 할 수 있지만 homeomorphism은 이에 대해 어떠한 설명도 주지 않는다. Homeomorphism은 서로 homeomorphic한 공간은 같은 cardinality를 갖는다는 사실만 말해주는 것이지, topological하게 다른 두 공간이 반드시 다른 cardinality를 가져야 한다는 말은 아니기 때문이다.

이건 사실 우리가 말을 하지 않아서 그렇지, 우리가 지금까지 연구해오던 많은 분야에서 생기는 일이다. 예를 들어, group을 다룰 때에는 <span class="border-highlight">하나의 원소로 generate된다</span>는 조건은 분명 group이라는 물건이 가질 수 있는 흥미로운 성질 중 하나지만, 그렇다고 모든 cyclic group이 서로 isomorphic하지는 않다. 마찬가지로, <span class="border-highlight">dihedral group임</span>, <span class="border-highlight">symmetric group임</span>, 혹은, <span class="border-highlight">simple group임</span>과 같은 성질들도 그러하다. 

위상수학에서도 마찬가지다. 앞서 언급한 <span class="border-highlight">같은 cardinality를 가진다</span>은 사실 별로 와닿는 예시는 아니다. 하지만 우리가 고등학교때부터 위상수학은 이러한 것이다, 라고 학습되었던 커피잔과 도넛 이야기만 하더라도 이렇게 homeomorphic하지 않은 예시를 하나 던져준다. Point-set topology를 배운 지금 우리는 커피잔과 도넛이 같다는 이야기를 커피잔과 도넛이 homeomorphic하다는 이야기로 받아들이겠지만, 사실 이에 대한 설명은 썩 만족스럽지 않다. 보통 이에 대한 건 도넛을 (연속적으로) 잘 늘리거나 줄여서 커피잔 모양을 만들 수 있다는 식으로 설명하곤 하는데, 이 늘리거나 줄이는 행동이 별로 위상적으로 잘 설명되지 않는다.

<div class="example" markdown="1">

<ins id="ex1">**예시 1**</ins> 예를 들어, 실수의 부분집합 $I=[-1,1]$을 생각하자. 이 line을 조금씩 줄여서 우리는 $I$가 최종적으로 점 $0$과 같도록 할 수 있다. 더 explicit하게, 1초의 시간이 주어졌다고 치면 임의의 $x\in I$를 $t$초 후에는 $(1-t)x$로 옮기는 상황을 생각해보자. 그럼 $t=0$일 때 모든 점들은 제자리에 위치하지만, $t$가 늘어남에 따라 조금씩 원점 방향으로 수축하고, 최종적으로 $t=1$이 되는 순간에 모든 점들은 원점으로 가게 된다. 이 변환은 분명하게 연속적인 과정이다. 하지만 원점과 $I$는 확실하게 homeomorphic하지 않다. Cardinality는 topological property인데, $I$는 uncountable이고 원점은 유한집합이기 때문이다.

</div>

하지만 이렇게 늘리거나 줄이는 행동은 기하적으로 생각했을 때는 꽤나 매력적으로 보이는 행동이다. 때문에 우리는 homeomorphism을 조금 약화시켜서 새로운 equivalence relation을 만들 생각을 하게 된다. 우리가 정의할 equivalence relation을 *homotopy equivalence*라 부른다.

## Homotopy equivalence

이를 정의하기 위해서는 정의들이 좀 필요하다. 다음 정의에서 $I=[0,1]$로 보아도 무방하지만, 꼭 그래야 하는 것은 아니다.

<div class="definition" markdown="1">

<ins id="df2">**정의 2**</ins> 두 개의 topological space $X$, $Y$가 주어졌다 하고, $X$에서 $Y$로의 두 continuous map $f_0$, $f_1$이 주어졌다 하자. $f_0$과 $f_1$이 *homotopic*하다는 것은 적당한 continuous map $F:X\times I\rightarrow Y$가 존재하여

$$F(x,0)=f_0(x),\quad F(x,1)=f_1(x)$$

이 모든 $x$에 대해 성립하는 것이다. 이 때, $F$를 $f_0$과 $f_1$ 사이의 *homotopy*라 부르고, $f_0$, $f_1$이 서로 homotopic하다는 것을 $f_0\simeq f_1$으로 표기한다.

</div>

Continuous map $F$가 주어졌다는 것은 각 시간 $t$마다 고정된 continuous map $f_t$가 주어졌으며, 이 association $t\mapsto f_t$ 또한 continuous하다는 이야기와 비슷하다. 사실 위 정의는 Munkres에서 가져온 것인데, 여기에선 $f_0$과 $f_1$ 대신 $f$와 $f'$으로 정의되어 있었다. 이 편리한 notation은 Hatcher에 나오는 notation인데, homotopy $(f_t)_{0\leq t\leq 1}$이 주어진다면 당연히 $f_0$은 $f_0$과 같고 $f_1$은 $f_1$과 같을 것이다. 반면, Munkres의 notation 상에서는 $f_0$이 $f$와 같고 $f_1$이 $f'$와 같아야 할 notational한 이유가 보이지 않는다.

특별히 $X=I$인 경우, 우리는 $f_0$과 $f_1$을 모두 curve, 혹은 위상수학에서는 path라 부른다. 이 상황이 앞선 상황과 다른 것은 $I$에는 시작점과 끝점이 있기 때문에, $f_0$과 $f_1$의 image 또한 시작점과 끝점이 정의된다는 것이다.[^1] 이러한 경우, homotopy의 개념을 조금 더 강화할 수 있다.

<div class="definition" markdown="1">

<ins id="df3">**정의 3**</ins> 주어진 path $f_0,f_1:I\rightarrow X$에 대하여, 이들이 *path homotopic*하다는 것은 이들 둘이 같은 시작점 $x_0$, 끝점 $x_1$을 가지며, continuous map $F:I\times I\rightarrow Y$가 존재하여

$$F(s,0)=f_0(s),\quad F(s,1)=f_1(s),\quad F(0,t)=x_0,\quad F(1,t)=x_1$$

이 성립하는 것이다. 이 때 $F$를 $f_0$과 $f_1$ 사이의 *path homotopy*라 부르고, $f_0,f_1$이 서로 path homotopic하다는 것을 $f_0\simeq_p f_1$으로 표기한다.

</div>

물론, 정의에서 $F$의 domain이 반드시 $I\times I$여야 할 필요는 없고, 시간을 나타내는 두 번째 $I$는 (사실 첫 번째 $I$도 마찬가지지만) 임의의 interval로 설정해주어도 전혀 상관없다. 중요한 것은 path-homotopy는 기존의 homotopy의 정의에 더해, endpoint-preserving 조건이 추가되었다는 것이다.

어렵지 않게 다음을 보일 수 있다.

<div class="proposition" markdown="1">

<ins id="lem4">**보조정리 4**</ins> $\simeq$와 $\simeq_p$는 모두 equivalence relation이다.

</div>

우리는 지금 바로 homotopy equivalence를 정의할 수도 있지만, 우선 Hatcher를 따라 homotopy의 특수한 경우를 좀 살펴보자.

<div class="definition" markdown="1">

<ins id="df5">**정의 5**</ins> Topological space $X$와 그 subspace $A$가 주어졌다 하자. 그럼 $X$에서 $A$로의 *deformation retraction*이라는 것은 

$$f_0=\operatorname{id}_X, \quad f_1(X)=A,\quad f_t|_A=\operatorname{id}_A$$

를 만족하는 continuous map들의 family $(f_t)_{0\leq t\leq 1}$를 의미한다.

</div>

Deformation retract는, notation에서 볼 수 있듯이, 일종의 homotopy로 볼 수 있다. 

<div class="definition" markdown="1">

<ins id="df6">**정의 6**</ins> Topological space $X$와 그 subspace $A$에 대하여, continuous map $r:X\rightarrow X$가 $A$ 위로의 *retraction*이라는 것은 $r(X)=A$이고 $r\|\_A=\operatorname{id}_A$가 성립하는 것이다. 

</div>

Deformation retract의 정의에 의해, $f_1(X)=A$이고, 또 마지막 조건에 $t=1$을 대입하면 $f_1\|\_A=\operatorname{id}_A$이므로 앞서 등장한 $f_1$은 retract여야 한다.[^2] 따라서 deformation retract는 다음 조건을 만족하는, identity map $\operatorname{id}_X$에서 retraction $f_1$로의 homotopy라 볼 수 있다.

<div class="definition" markdown="1">

<ins id="df7">**정의 7**</ins> 두 개의 topological space $X$, $Y$에 대하여, homotopy $f_t:X\rightarrow Y$가 $A\subset X$ 위에서는 $t$에 independent하다고 하자. 그럼 이 homotopy를 특별히 *homotopy relative to $A$*라고 부른다.

</div>

이제 homotopy equivalence를 정의하자. 앞서 살펴본 것과 같이, 만약 $X$가 subspace $A$로 deformation retract한다고 하자. $r:X\rightarrow A$를 이 때의 retraction (즉 $f_1$) 이라 하고, $i:A\rightarrow X$를 canonical injection이라 하면 $ri=\operatorname{id}_A$이다. $ir$은 정확하게 identity map이 되지는 않지만, 그 대신 $\operatorname{id}_X$와 homotopic하다. Deformation retract의 정의에 사용된 $f_t$들이 정확히 $\operatorname{id}_X$와 $ir=r$ 사이의 homotopy를 정의하기 때문이다. 이를 일반화한 게 homotopy equivalence다.

<div class="definition" markdown="1">

<ins id="df8">**정의 8**</ins> 두 개의 topological space $X$, $Y$가 주어졌다고 하자. Continuous map $f:X\rightarrow Y$가 *homotopy equivalence*라는 것은, 적당한 map $g:Y\rightarrow X$가 존재하여 $fg\simeq\operatorname{id}_Y$이고 $gf\simeq \operatorname{id}_X$가 성립하는 것이다. $X$와 $Y$ 사이에 homotopy equivalence가 존재한다면, $X$와 $Y$가 *homotopy equivalent*하다 (혹은 같은 homotopy type을 갖는다)고 하고, 이를 $X\simeq Y$로 적는다.

</div>

---
**Reference**

[Hat] A. Hatcher, *Algebraic Topology*. Combradge University Press, 2022 

---
[^1]: 물론 시작점과 끝점이 다를 이유는 없다.
[^2]: 하지만 모든 retraction이 deformation retract로부터 얻어지는 것은 아니다. 예를 들어, 임의의 공간은 항상 한 점으로의 retraction을 갖는데, $X$에서 한 점 $x$로의 deformation retract는 $X$의 임의의 점으로부터 $x$까지의 path를 만들고, 따라서 한 점으로 deformation retract 되는 공간은 반드시 path connected여야 하기 때문이다.
