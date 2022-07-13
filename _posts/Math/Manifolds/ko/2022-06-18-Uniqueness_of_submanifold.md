---

title: "부분다양체의 유일성"
excerpt: "Embedded submanifold의 유일성"

lang: ko

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

임의의 manifold $M$과 그 submanifold $F:P\rightarrow M$이 주어졌다 하자. 그럼 $F$를 일종의 inclusion으로 생각할 수 있으므로, 만일 또 다른 어떤 manifold $N$과 $C^\infty$ 함수 $G:N\rightarrow M$에 대하여 $G(N)\subset F(P)$가 성립한다면 $N\rightarrow P\overset{F}{\hookrightarrow}M$이 성립하도록 하는 $C^\infty$ 함수 $\bar{G}:N\rightarrow P$가 존재하는지를 생각할 수 있다.

단순한 함수로서 $\bar{G}$가 유일하게 존재한다는 것은 자명하다. $G(N)\subset F(P)$이고, $F$는 injection이므로 임의의 $q\in N$을 $F^{-1}(G(q))$에 대응시키면 된다. 하지만 이렇게 정의된 함수 $\bar{G}$가 항상 $C^\infty$인 것은 아니다.

예를 들어, 다음과 같이 $\mathbb{R}^2$의 두 submanifold를 생각하자.

![](/assets/images//.png){:width="250px" class="invert" .align-center}

이들의 $\mathbb{R}^2$에서의 image는 서로 동일하며, $F\_1(0)=F\_2(0)=0$을 만족한다. 그러나 $\bar{F}\_1$은 $C^\infty$가 아닐 뿐더러, 연속도 아니다. 열린집합 $(-1,1)$의 $\bar{F}\_1$에 대한 preimage가 열린집합이 아니기 때문이다. 

다음 정리는 위와 같은 경우에만 $\bar{G}$가 $C^\infty$가 아닐 수 있다는 것을 보여준다.

<div class="proposition" markdown="1">

<ins id="thm1">**정리 1**</ins> 임의의 manifold $M$과 그 submanifold $F:P\rightarrow M$이 주어졌다 하자. $C^\infty$ 함수 $G:N\rightarrow M$이 $G(N)\subset F(P)$를 만족한다고 가정하고, $\bar{G}$를 위에서 정의한 것과 동일하게 정의하자. 즉 $F\circ\bar{G}=G$가 성립한다. 이 때, 

1. 만일 $\bar{G}$가 연속이라면 $\bar{G}$는 $C^\infty$이기도 하다.
2. 만일 $F$가 embedding이라면 $\bar{G}$는 연속이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

2번 명제는 자명하다. 

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