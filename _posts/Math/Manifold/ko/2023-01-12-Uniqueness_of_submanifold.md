---

title: "부분다양체의 유일성"
excerpt: ""

categories: [Math / Manifold]
permalink: /ko/math/manifold/uniqueness_of_submanifold
header:
    overlay_image: /assets/images/Math/Manifold/Uniqueness_of_submanifold.png
    overlay_filter: 0.5
sidebar: 
    nav: "manifold-ko"

date: 2023-01-12
last_modified_at: 2023-01-12
weight: 8

---

정의에 의하여, manifold $M$의 submanifold는 단사인 immersion을 의미한다. 이를 $\Phi:P\rightarrow M$으로 적자. 그럼 $\Phi$의 공역을 제한하여 얻어지는 함수 $\bar{\Phi}:P\rightarrow \Phi(P)$는 전단사함수이므로, $P$의 위상구조를 그대로 $\Phi(P)$ 위에 옮겨올 수 있고, 이러한 과정을 통해 $M$의 submanifold는 부분집합의 inclusion $\Phi(P)\hookrightarrow M$으로도 생각할 수 있다. 이번 글에서 우리는 이를 조금 더 자세히 살펴본다.

## 부분다양체와 $C^\infty$ 함수

우선 manifold $M$과, 그 submanifold $\Phi:P\rightarrow M$을 고정하자. 또 다른 $C^\infty$ 함수 $F:N\rightarrow M$이 $F(N)\subseteq\Phi(P)$를 만족한다 하면, 위와 같이 정의된 $\bar{\Phi}$를 사용하여 새로운 단사함수 $F_0:N\rightarrow P$를 다음의 식

$$F_0=\bar{\Phi}^{-1}\circ F$$

을 통해 정의할 수 있다. 자연스럽게 이렇게 정의된 함수 $F_0$이 immersion이 되는지를 물어볼 수 있다.

Submanifold를 단순히 원래의 manifold의 부분집합으로 본다면, 이 질문은 단순히 임의의 $C^\infty$ 함수 $F:N\rightarrow M$의 치역이 $F(N)\subseteq P\subseteq M$을 만족할 때, $F$의 공역을 $P$로 제한한 것이 $C^\infty$냐는 질문과 같다. 그러나 이 질문은 보기보다 단순하지 않으며, 실제로 항상 이것이 성립하는 것은 아니다.

<div class="example" markdown="1">

<ins id="ex1">**예시 1**</ins> 두 manifold $N,P$가 모두 자연스러운 manifold 구조가 주어진 $\mathbb{R}$이라 하고, $M=\mathbb{R}^2$에도 자연스러운 manifold 구조가 주어졌다 하자. 두 submanifold $\Phi:N\rightarrow M$과 $\Psi:P\rightarrow M$을 다음의 두 그림

![counterexample_1](/assets/images/Math/Manifold/Uniqueness_of_submanifold-1.png){:width="400px" class="invert" .align-center}

과

![counterexample_2](/assets/images/Math/Manifold/Uniqueness_of_submanifold-2.png){:width="400px" class="invert" .align-center}

처럼 정의하자. 그럼 $\Phi(N)=\Psi(P)$이며, 따라서 $N$에서 $P$로의 전단사함수 $\bar{\Psi}^{-1}\circ\Phi$가 잘 정의된다.

이제 $N$에서 원점의 충분히 작은 열린근방 $U$를 생각하고, $U$의 $\bar{\Psi}^{-1}\circ\Phi$에 의한 image를 생각하면 $(\bar{\Psi}^{-1}\circ\Phi)(U)$는 $P$에서 열린집합이 아니다. 

![counterexample_3](/assets/images/Math/Manifold/Uniqueness_of_submanifold-3.png){:width="400px" class="invert" .align-center}

즉 $(\bar{\Psi}^{-1}\circ\Phi)^{-1}$이 연속이 아니므로 이 함수는 $C^\infty$ 함수조차 되지 않는다.

</div>

그러나, 다음 명제는 위의 예시와 같은 문제를 일으키는 것이 오직 위상적인 데이터라는 것을 보여준다.

<div class="proposition" markdown="1">

<ins id="pp2">**명제 2**</ins> 워너 1.32

</div>
<details class="proof" markdown="1">
<summary>증명</summary>



</details>

## 부분다양체 사이의 동치관계

<div class="definition" markdown="1">

<ins id="df3">**정의 3**</ins> Manifold $M$과 두 submanifold $\Phi_1:N_1\rightarrow M$, $\Phi_2:N_2\rightarrow M$이 주어졌다 하자. 이들 둘이 *equivalent*하다는 것은 diffeomorphism $\theta:N_1\rightarrow N_2$가 존재하여 $\Phi_1=\Phi_2\circ\theta$가 성립하는 것이다.

</div>

이렇게 정의된 관계가 $M$의 모든 submanifold들 $(N,\Phi)$들의 집합에 동치관계를 유도한다는 것은 자명하다. 임의의 equivalence class $[(N,\Phi)]$를 택하자. 그럼 처음에 살펴본 것과 같은 쌍 

$$A=\Phi(N)\subseteq M, \qquad \iota:A\hookrightarrow M$$

을 생각할 수 있다. 이 때, $A$는 전단사함수 $\bar{\Phi}:N\rightarrow A$을 통해 $N$의 미분구조와 위상구조가 부여된 manifold이다. 그럼 $\bar{\Phi}$는 $N$과 $A$ 사이의 diffeomorphism이므로, $\bar{\Phi}^{-1}$ 또한 diffeomorphism이고 따라서 합성

$$\iota=\Phi\circ\bar{\Phi}^{-1}$$

은 $A$에서 $M$으로의 immersion이다. 즉 $(A,\iota)$는 $M$의 submanifold이다. 뿐만 아니라, 위의 식은 $(N,\Phi)$와 $(A,\iota)$가 equivalent하다는 것을 보여준다. 

반대로, manifold 구조가 주어진 부분집합 $A\subseteq M$에 대하여 inclusion $\iota:A\hookrightarrow M$이 immersion이라 하면 $(A,\iota)$는 항상 $M$의 submanifold가 된다. 이는 임의의 $x\in A$에 대하여 $d\iota_x:T_xA\rightarrow T_xM$이 단사함수임을 의미하므로, $d\iota_x$는 $T_xA$와 $d\iota_x(T_xA)$ 사이의 전단사함수를 유도한다. 약간의 표기법 상의 문제를 덮어두면 $T_xA$를 $d\iota_x(T_xA)$와 동일한 것으로 취급할 수 있다. 

## 부분다양체의 유일성

위의 절에서 정의한 $(A,\iota)$는 equivalence class $[(N,\Phi)]$마다 <em_ko>유일하게</em_ko> 결정된다. 우선 [정의 3](#df3)에서의 $\theta$는 diffeomorphism이므로 특히 전단사함수이고, 따라서 

$$\Phi_2(N_2)=\Phi_1(\theta(N_2))=\Phi_1(N_1)$$

이 성립하므로 $A$는 유일하게 결정된다. 한편 이렇게 결정되는 $M$의 부분집합 $A$와 inclusion $\iota:A\hookrightarrow M$이 $[(N,\Phi)]$에 속하기 위해서는 $\iota=\Phi\circ\theta$를 만족하는 diffeomorphism $\theta$가 존재해야 하는데, 양 변의 왼쪽에 $\bar{\Phi}^{-1}$을 취해주면 $\theta=\bar{\Phi}^{-1}$이므로 $A$의 manifold 구조는 <em_ko>반드시</em_ko> 위에서 정의한 것과 동일한 방식으로 정의되어야 한다.

반면 manifold $M$의 임의의 부분집합 $\iota:A\hookrightarrow M$에 대하여, $(A,\iota)$를 submanifold로 만드는 $A$의 manifold 구조가 유일하게 존재하는 것은 아니다. 가령 [예시 2](#ex2)와 같이 $M$의 두 submanifold $(N_1,\Phi_1),(N_2,\Phi_2)$가 서로 diffeomorphic하지 않지만 $\Phi_1(N_1)=\Phi_2(N_2)$를 만족한다면, $[(N_1,\Phi_1)]$과 $[(N_2,\Phi_2)]$에서 위의 과정을 통해 얻어지는 $(A,\iota)$ 위의 두 manifold 구조는 서로 달라야 한다. 

그럼에도 불구하고, $(A,\iota)$가 만족해야 할 조건이 추가된다면 이 위에 submanifold의 구조가 유일하게 결정될 수도 있다. 다음 글에서 소개할 정리들의 결과는 이러한 유일성까지 만족하며, 이 때 다음의 두 명제를 유용하게 사용할 수 있다.

<div class="proposition" markdown="1">

<ins id="pp4">**명제 4**</ins> 워너 1.33 (a)

</div>
<details class="proof" markdown="1">
<summary>증명</summary>



</details>

<div class="proposition" markdown="1">

<ins id="pp5">**명제 5**</ins> 워너 1.33 (b)

</div>
<details class="proof" markdown="1">
<summary>증명</summary>



</details>