---

title: "부분다양체의 유일성"
excerpt: "Embedded submanifold의 유일성"

categories: [Math / Manifold]
permalink: /ko/math/manifold/uniqueness_of_submanifold
header:
    overlay_image: /assets/images/Manifold/Uniqueness_of_submanifold.png
    overlay_filter: 0.5
sidebar: 
    nav: "manifold-ko"

date: 2022-06-18
last_modified_at: 2022-06-18
weight: 8

---

앞선 글에서 살펴봤듯, manifold 사이의 역함수 정리는 유용한 따름정리들을 많이 알려준다. 이와 유사하게 manifold 사이의 음함수 정리 또한 좋은 결과를 주는데, 이 전에 submanifold에 manifold 구조를 주는 방법에 대해 조금 더 자세히 살펴볼 필요가 있다.

## Restriction of codomain

임의의 manifold $M$과 그 submanifold $F:N'\rightarrow M$이 주어졌다 하자. 그럼 $F$를 일종의 inclusion으로 생각할 수 있으므로, 만일 또 다른 어떤 manifold $N$과 $C^\infty$ 함수 $G:N\rightarrow M$에 대하여 $G(N)\subseteq F(N')$가 성립한다면 $N\rightarrow N'\overset{F}{\hookrightarrow}M$이 $G$와 같도록 하는 $C^\infty$ 함수 $\iota:N\rightarrow N'$가 존재하는지를 생각할 수 있다.

예를 들어, $M=\mathbb{R}^2$이라 하고, 두 submanifold $F:N'=\mathbb{R}\rightarrow \mathbb{R}^2$, $G:N=\mathbb{R}\rightarrow\mathbb{R}^2$를 각각 아래 그림의 오른쪽과 왼쪽의 submanifold로 생각하자. 여기에서 $F(0)=G(0)$은 모두 $\mathbb{R}^2$의 원점이다.

![figure_eight](/assets/images/Manifold/Uniqueness_of_submanifold-1.png){:width="800px" class="invert" .align-center}

집합으로서 $G(N)=F(N')$이 성립한다. 또, $F$는 injective이므로 치역을 제한하면 $F$는 $N'$과 $F(N')$ 사이의 bijection이 된다. 약간의 abuse of notation을 통해 $F^{-1}$을 이 bijection의 역함수라 하자. 그럼 $\iota=F^{-1}\circ G$로 제한하면 $\iota$는 주어진 조건 $G=F\circ\iota$를 만족하며, 뿐만 아니라 이를 만족하는 $\iota$는 오직 이것 뿐임을 알 수 있다.

한편, $N'$의 image는 $\mathbb{R}$에서의 위상구조를 물려받으므로, $\mathbb{R}$에서의 열린집합 $(-1,1)$의 image는 오른쪽 manifold에서 열린집합이 된다. (오른쪽 빨간색) 그러나 $\iota^{-1}(-1,1)$은 두 열린집합과 집합 $\\{0\\}$의 합집합이므로 (왼쪽 빨간색) 열린집합이 아니고 따라서 $\iota$는 연속함수조차 되지 않는다.

그러나 다음 정리는 오직 위와 같은 경우에만 $\iota$가 $C^\infty$가 아닐 수 있다는 것을 보여준다.

<div class="proposition" markdown="1">

<ins id="thm1">**정리 1**</ins> 임의의 manifold $M$과 그 submanifold $F:N'\rightarrow M$이 주어졌다 하자. $C^\infty$ 함수 $G:N\rightarrow M$이 $G(N)\subseteq F(N')$를 만족한다고 가정하고, $F\circ\iota=G$를 만족하는 유일한 함수 $\iota$를 생각하자. 그럼

1. 만일 $\iota$가 연속이라면 $\iota$는 $C^\infty$이기도 하다.
2. 만일 $F$가 embedding이라면 $\iota$는 연속이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$M,N,N'$이 각각 $m,n,n'$차원의 manifold라 하자. $N'$은 $M$의 submanifold이므로 $n' < m$이다.

2번 주장은 거의 자명하다. $F$가 embedding이라면, $F:N'\rightarrow F(N')$은 homeomorphism이 된다. 이는 앞선 문단의 abuse of notation을 차용하면 $F^{-1}$도 연속이라는 뜻이므로, 두 연속함수의 합성 $\iota:F^{-1}\circ G$ 또한 연속이어야 함이 자명하다.

이 정리의 핵심은 1번이라 할 수 있다. $\iota$는 연속이므로, $N'$의 임의의 열린집합 $U$에 대하여 $\iota^{-1}(U)$는 열린집합이다. 따라서 만일 $N'$를 덮는 coordinate system들 $(U,\tau)$가 존재하여, $(\tau\circ\iota)\|\_{\iota^{-1}(U)}$가 $C^\infty$이도록 할 수 있다면 임의의 점 $q\in N$에서 $\iota$가 $C^\infty$임을 보일 수 있게 된다. 

점 $p'\in N'$가 임의로 주어졌다 하고, $(V,\gamma)$가 $F(p')$를 포함하는 $M$의 coordinate system이라 하자. $F$는 immersion이므로 [§부분다양체와 역함수정리, 따름정리 10](/ko/math/manifold/submanifolds#crl10)에 의하여, $\gamma\circ F$의 성분함수들의 부분집합이 $p'\in N'$ 근방에서의 coordinate system이 된다. $\gamma=(y^j)_{j=1}^m$이라 하고, 일반성을 잃지 않고 앞선 $n'$개의 성분함수들 

$$x^j=y^j\circ F;\qquad j=1,\ldots, n'$$

이 coordinate system $(U,\tau)$를 이룬다고 하자. 이는 $\mathbb{R}^m$에서 앞선 $n'$개의 좌표 $\mathbb{R}^{n'}$으로의 projection을 $\pi$라 한다면, 이는 $\tau=\pi\circ\gamma\circ F$으로 정의하는 것과 같다. 이제

$$(\tau\circ\iota)|_{\iota^{-1}(U)}=(\pi\circ\gamma\circ F\circ\iota)|_{\iota^{-1}(U)}=(\pi\circ\gamma\circ G)|_{\iota^{-1}(U)}$$

이므로 원하는 결론을 얻는다.

</details>

## 부분다양체의 유일성

부분다양체의 유일성을 이야기하기 위해서는 우선 이 구조가 어떤 의미에서 유일한지를 정의해야 한다.

<div class="definition" markdown="1">

<ins id="df2">**정의 2**</ins> Manifold $M$과, 두 submanifold $F_1:N_1\rightarrow M$, $F_2:N_2\rightarrow M$이 주어졌다 하자. 이 때, $N_1$과 $N_2$가 *equivalent*하다는 것은 적당한 diffeomorphism $G:N_1\rightarrow N_2$가 존재하여 $F_1=F_2\circ G$를 만족하는 것이다.

</div>

어렵지 않게 위에서 정의한 relation이 equivalence relation이 된다는 것을 확인할 수 있다. 한편 만일 $F_1$과 $F_2$가 equivalent하다면, 반드시 $F_1(N_1)=F_2(N_2)$여야 한다. 따라서 이 공통의 집합을 $A$라 하고, canonical injection $\iota:A\hookrightarrow M$을 생각하자. 이제 이 equivalence class에 속하는 submanifold $F:N\rightarrow M$에 대하여, $F(N)=A$이므로, $F$는 $A$와 $N$ 사이의 bijection이고 따라서 $A$에 미분구조를 정의해줄 수 있다. 

<div class="proposition" markdown="1">

<ins id="pp3">**명제 3**</ins> Manifold $M$과 그 부분집합 $A$를 택하고, $A$ 위에 정의된 임의의 위상구조를 하나 고정하자. 그럼 $(A,\iota)$를 $M$의 submanifold로 만드는 $A$의 미분구조는 많아야 하나 존재한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$A$ 위에 위상구조 $\tau$가 주어진 것으로 생각하자. 

</details>

<div class="proposition" markdown="1">

<ins id="pp4">**명제 4**</ins> Manifold $M$과 그 부분집합 $A$를 택하고, $A$에 subspace topology $\tau$가 주어졌다 하자. 만일 $(A,\iota)$를 $M$의 submanifold로 만드는 $A$의 미분구조 $\mathcal{A}$가 존재한다면, $(A,\tau,\mathcal{A})$는 이 조건을 만족하는 유일한 manifold 구조이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>



</details>

---

**참고문헌**

**[Lee]** John M. Lee. *Introduction to Smooth Manifolds*, Graduate texts in mathematics, Springer, 2012  
**[War]** Frank W. Warner. *Foundations of Differentiable Manifolds and Lie Groups*, Graduate texts in mathematics, Springer, 2013    

---