---

title: "호몰로지"
excerpt: "기본정의"

categories: [Math / Algebraic Topology]
permalink: /ko/math/algebraic_topology/singular_homology
header:
    overlay_image: /assets/images/Algebraic_topology/a.png
    overlay_filter: 0.5
sidebar: 
    nav: "topology-ko"

date: 2022-06-27
last_modified_at: 2022-06-27
weight: 101

---

위상수학에서 살짝 맛본 기본군은 직관적으로 그 의미가 명확한 불변량이다. 기본군은 고리를 통해 공간에 뚫려있는 구멍을 잡아낸다. 예를 들어 $X=\mathbb{R}^2\setminus\\{0\\}$을 생각하면, 이 공간에서 원점을 감싸는 고리는 연속적인 방법으로는 한 점으로 변형하는 것이 불가능하기 때문에 $\pi\_1(X)$가 0이 아니고, 따라서 우리는 $X$에 구멍이 뚫려 있다는 사실을 안다. 

하지만 이 개념의 한계 또한 명확하다. 예컨대 $Y=\mathbb{R}^3\setminus\\{0\\}$을 생각하면 이 공간 상의 어떠한 고리를 주어도 한 점으로 수축시킬 수 있다. 이는 <em_ko>고리</em_ko> $S^1$이 공간 상의 구멍을 탐지하는 데에 한계가 있다는 것을 보여준다. 이를 해결하기 위한 방법은 당연히 $S^1$ 대신 더 높은 차원의 <em_ko>고리</em_ko>, 예컨대 $S^2$를 사용하는 것이다. 방금의 상황에서 $S^1$ 대신 $S^2$를 사용한다면, 원점을 감싸고 있는 $S^2$는 한 점으로 수축할 수 없고, 그렇지 않은 $S^2$는 한 점으로 수축할 수 있음이 직관적으로 명확하다.

우리는 이렇게 기본군 $\pi\_1(X)$를 일반화하여 $\pi\_2(X)$, 더 나아가 $\pi\_n(X)$를 정의할 수 있다. 그러나 일반적으로 이 군들을 직접 계산하는 것은 굉장히 어렵다. 다행히도 우리가 궁금해하는 많은 성질들은 homotopy group $\pi\_n(X)$ 대신, 더 계산하기 쉬운 *homology group*들만 살펴보아도 충분하다는 것이 밝혀져 있다.

Homology group을 다루기 위해서는 ㅇ



## Simplicial homology

Homology group을 계산하는 방법은 여러가지가 있는데, 우선 우리는 simplicial homology를 먼저 살펴본다. Singular homology의 경우도 이와 계산하는 방법이 크게 다르지는 않지만 simplicial homology가 우리 직관을 더 강화해준다.

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> $\mathbb{R}^m$차원 유클리드 공간 안의 $n$개의 linearly independent인 벡터들이 주어졌다 하자. 그럼 이 벡터들의 $n$개의 끝점들과, 원점이 이루는 집합의 convex hull을 *$n$-simplex*라 부른다.

</div>

일반적인 $n$-simplex를 지칭할 때에는 $\Delta^n$과 같이 적지만, 특별히 $n$-simplex를 만드는 $n+1$개의 점들을 $v_0,\ldots, v_n$이라 하면, 이들에 의해 만들어지는 $n$-simplex는 $[v_0,\ldots, v_n]$으로 적는다. 뿐만 아니라 우리는 $n$-simplex들의 각 변이 방향을 가지기를 원하는데, 이 방향은 index가 작은 곳에서 큰 쪽으로 향하도록 정한다. 이렇게 정해준다면, $n$-simplex를 이루는 $n+1$개의 점 중 하나를 빼더라도 남은 점들 사이에 (방향이 정의된) 선분들이 잘 정의되며, 따라서 남은 $n$개의 점들도 $(n-1)$-simplex를 이룬다. 우리는 이를 원래의 simplex의 한 면이라고 부른다.

이제 공간 $X$에다 $\Delta$-complex 구조를 준다는 것은 $X$를 simplex들로 쪼개는 것으로 생각하면 된다. 더 엄밀하게 이야기하자면 이들은 다음 세 조건을 만족하는 연속함수들 $\sigma_\alpha:\Delta^n\rightarrow X$이다. (여기서 $n$은 각각의 $\alpha$마다 정해지는 자연수이다.)

1. 각각의 $\alpha$마다, $\sigma_\alpha$를 $\Delta^n$의 내부로 제한한 것은 injection이 되며, 또 $X$의 임의의 점은 이렇게 제한된 함수들의 image 중 정확히 하나에 들어간다.
2. 각각의 $\alpha$마다, $\sigma_\alpha$를 $\Delta^n$의 각 면으로 제한한 $\Delta^{n-1}\rightarrow X$ 또한 이 함수들 중 하나이다.
3. $A\subseteq X$가 열린집합인 것은 모든 $\alpha$에 대해 $\sigma_\alpha^{-1}(A)$가 $\Delta^n$에서 열린집합인 것이다. 

예를 들어 다음의 torus는 $\Delta$-complex 구조를 가진다. 

![](/assets/images//.png){:width="250px" class="invert" .align-center}

이제 우리는 simplicial homology를 정의할 수 있다. $X$가 $\Delta$-complex라 하고, 각각의 $n$에 대하여 $\Delta_n(X)$를 $X$를 이루는 $n$-simplex들로 만들어진 free abelian group으로 잡자. 또, 우리는 *boundary map*을 다음의 식

$$\partial(\sigma_\alpha)=\sum_i(-1)^i\sigma_\alpha|_{[v_0,\ldots,\hat{v}_i,\ldots, v_n]}\tag{1}$$

으로 정의한다. 그럼 $\partial$은 $\Delta_n(X)$의 원소들을 $\Delta_{n-1}(X)$로 옮기는 원소들이며, 이것이 group homomorphism임을 확인할 수 있다. 뿐만 아니라 다음의 sequence

$$\Delta_\bullet(X):\qquad \cdots\overset{\partial}{\longrightarrow}\Delta_n(X)\overset{\partial}{\longrightarrow}\Delta_{n-1}(X)\overset{\partial}{\longrightarrow}\Delta_{n-2}(X)\overset{\partial}{\longrightarrow}\cdots\overset{\partial}{\longrightarrow}\Delta_0(X)\longrightarrow 0$$

은 *semi-exact sequence*, 혹은 *complex*라 부르는 구조가 된다. 이는 $\partial^2=0$이라는 뜻이다. 혼동을 피하기 위해 $\partial_n:\Delta_n(X)\rightarrow\Delta_{n-1}(X)$과 같이 index를 주면, 이는 $\operatorname{im}\partial_{n+1}\subset\ker\partial_n$인 것과 동치이다. 그렇다면 이 complex가 exact sequence에서 얼마나 떨어져 있는지는 다음의 quotient group들

$$H_n^\Delta(X):=\ker\partial_n/\operatorname{im}\partial_{n+1}$$

을 통해 알 수 있다. 

## Singular homology

위상공간 $X$에서 정의된 *singular $n$-simplex*란 단순히 연속함수 $\sigma:\Delta^n\rightarrow X$를 뜻한다. 각각의 $n$에 대하여, $C_n(X)$를 이러한 singular $n$-simplex들을 basis로 갖는 free abelian group으로 정의하자. 

$\sigma$는 이제 단순한 연속함수지만, 오히려 그것 때문에 단순해지는 것들도 있다. 가령 $\sigma:[v_0,\ldots, v_n]\rightarrow X$를 face $[v_0,\ldots,\hat{v}_i,\ldots, v_n]$으로 제한한 것은 ($\Delta$-complex의 2번 조건을 언급할 필요 없이) 연속함수가 되고, 그 domain이 $(n-1)$-simplex이므로 결과적으로 생기는 함수는 singular $(n-1)$-simplex이다. 그리고 정확하게 이것이 boundary map을 정의할 때 필요한 전부이다. 

따라서 식 (1)을 이용하여 $\partial_n:C_n(X)\rightarrow C_{n-1}(X)$를 정의할 수 있고, 따라서 이들의 complex $C_\bullet(X)$가 잘 정의된다. 그럼 위와 마찬가지로 *singular homology group* $H_n(X)$를 정의할 수 있다. $C_n(X)$는 $\Delta_n(X)$에 비교하였을 때 엄청나게 거대하지만, homology group을 생각하면 마찬가지로 엄청나게 거대한 subgroup으로 quotient를 취해주기 때문에 다시 작아지게 된다. 실제로 singular homology group과 simplicial homology group이 동등하다는 것을 보일 수 있다. 

<div class="proposition" markdown="1">

<ins id="pp2">**명제 2**</ins> Path-connected이고, 공집합이 아닌 위상공간 $X$가 주어졌다 하자. 그럼 $H_0(X)\cong\mathbb{Z}$가 성립한다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>



</details>

<div class="proposition" markdown="1">

<ins id="pp3">**명제 3**</ins> 공집합이 아닌 위상공간 $X$에 대하여, $X$의 path-component들을 $X_\alpha$라 하면 $H_n(X)\cong\bigoplus H_n(X_\alpha)$가 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>



</details>

## Reduced homology groups

$X$가 singleton이라 하자. 그럼 모든 $n$에 대하여 $C_n(X)\cong\mathbb{Z}$이다. 이들 사이의 boundary map을 생각해보면, $\partial_n:C_n(X)\rightarrow C_{n-1}(X)$는 $n$이 짝수일 경우는 홀수 개의 항을 더하고 빼게 되므로 $\sigma_{n-1}:\Delta^{n-1}\rightarrow X$이 나오지만 $n$이 홀수인 경우에는 짝수 개의 항을 더하고 빼게 되므로 $0$이 나온다. 즉 이 경우 다음과 같은 complex

$$\cdots\longrightarrow\mathbb{Z}\overset{\sim}{\longrightarrow}\mathbb{Z}\overset{0}{\longrightarrow}\mathbb{Z}\overset{\sim}{\longrightarrow}\mathbb{Z}\overset{0}{\longrightarrow}\mathbb{Z}\longrightarrow 0$$

를 얻게 된다. 이로부터, 홀수 번째 homology group은

$$\ker 0/\operatorname{im}\operatorname{id}_\mathbb{Z}=\mathbb{Z}/\mathbb{Z}=0$$

그리고 짝수 번째 homology group은

$$\ker\operatorname{id}_\mathbb{Z}/\operatorname{im}0=(0)/(0)=0$$

이 된다는 것을 알 수 있다. 단 0번째 homology group은 $\mathbb{Z}$가 된다. 이는 [명제 2](#pp2)의 결과이기도 하고, 혹은 위의 complex에서 0번째 homology group을 계산할 때에는 $\operatorname{id}_\mathbb{Z}:\mathbb{Z}\rightarrow\mathbb{Z}$ 대신 $\mathbb{Z}\rightarrow 0$을 이용해야 하기 때문이기도 하다. 어쨌든 우리는 종종 0번째 homology group 또한 0이 되기를 원할 때가 있는데, 이를 위해 우리는 원래의 complex

$$C_\bullet(X):\qquad\cdots\overset{\partial}{\longrightarrow}C_n(X)\overset{\partial}{\longrightarrow}C_{n-1}(X)\overset{\partial}{\longrightarrow}C_{n-2}(X)\overset{\partial}{\longrightarrow}\cdots\overset{\partial}{\longrightarrow}C_0(X)\longrightarrow 0$$

대신 다음의 *augmented* complex

$$\cdots\overset{\partial}{\longrightarrow}C_n(X)\overset{\partial}{\longrightarrow}C_{n-1}(X)\overset{\partial}{\longrightarrow}C_{n-2}(X)\overset{\partial}{\longrightarrow}\cdots\overset{\partial}{\longrightarrow}C_0(X)\overset{\epsilon}{\longrightarrow}\mathbb{Z}\longrightarrow0$$

을 정의한다. 여기서 $\epsilon$은 $\epsilon(\sum n_i\sigma_i)=\sum n_i$로 정의된다. 이 complex의 homology group을 원래 complex의 *reduced homology group*이라 부르고 $\tilde{H}_n(X)$로 적는다. $n$이 0보다 클 경우 이들은 원래의 homology group들 $H_n(X)$와는 다를 것이 없지만, $H_0(X)=\tilde{H}_0(X)\oplus\mathbb{Z}$가 된다. 

## Induced chain map

연속함수 $f:X\rightarrow Y$가 주어졌다 하자. 그럼 각각의 $\sigma\in C_n(X)$에 대하여 $\sigma\mapsto f\circ\sigma$를 통해 함수 $f_n:C_n(X)\rightarrow C_n(Y)$가 정의된다. 어렵지 않게 $f_\bullet=(f_n)$이 chain transformation임을 확인할 수 있다. 이 때, 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="thm4">**정리 4**</ins> 두 연속함수 $f,g:X\rightarrow Y$가 homotopic하다면 모든 $n$에 대해 $H_n(f)=H_n(g)$가 성립한다.

</div>