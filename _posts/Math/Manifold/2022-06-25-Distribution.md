---

title: "Distribution"
excerpt: "프로베니우스 정리"

categories: [Math / Manifold]
permalink: /ko/math/manifold/distribution
header:
    overlay_image: /assets/images/Manifold/Distribution.png
    overlay_filter: 0.5
sidebar: 
    nav: "manifold-ko"

date: 2022-06-25
last_modified_at: 2022-06-25
weight: 112

---

이번 글에서 우리의 목적은 [§벡터장, 정리 10](/ko/math/manifold/vector_fields#thm10)을 일반화하는 것이다. 이 정리를 다른 방식으로 풀어쓰면 다음과 같다.

> 임의의 manifold $M$에 대하여, 각 점 $p\in M$마다 1차원 부분공간 $V_p\subseteq T_pM$이 주어졌다 하자.[^1] 그럼 임의의 점 $p\in P$마다 $p$를 포함하는 1차원 submanifold $\gamma_p$가 존재하여, $\gamma_p$의 각 점 $q$에서의 tangent space $T_q\gamma_p$가 $V_q$와 같도록 할 수 있다.

우리는 이를 $k$차원으로 확장하려 한다. 

## Frobenius theorem, distribution version

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> $m$차원 manifold $M$과 자연수 $k\leq m$이 주어졌다 하자. 

1. $\mathscr{D}$가 rank $k$의 *regular distribution*이라는 것은 각각의 점 $p\in M$마다 $k$차원 벡터공간 $\mathscr{D}(p)\subseteq T_pM$을 대응시켜주는 것이다.
2. Regular distribution $\mathscr{D}$가 $C^\infty$라는 것은 각각의 $p\in M$마다 적당한 열린근방 $U$과 이 위에서 정의된 local section $X_1,\ldots, X_k$가 존재하여 이들이 $\mathscr{D}$를 span하는 것이다.
3. 만일 임의의 vector field $X$가 $X_p\in \mathscr{D}(p)$를 항상 만족한다면 이를 $X\in\mathscr{D}$로 적는다. 

</div>

앞으로 distribution은 항상 regular distribution인 것으로 생각한다.

위의 정의를 간단히 요약자면 rank $k$의 distribution이란 tangent bundle $TM$의 rank $k$짜리 subbundle이라는 것이다. 따라서 도입부에서 정의한 일반화된 정리를 엄밀한 언어로 표현하기 위해서는 integral curve만 일반화하면 충분하다.

<div class="definition" markdown="1">

<ins id="df2">**정의 2**</ins> Manifold $M$ 위에서 정의된 rank $k$의 distribution $\mathscr{D}$에 대하여, $M$의 submanifold $F:N\rightarrow M$이 *integral manifold*라는 것은 각각의 $p\in N$에 대하여 $dF(T_pM)=\mathscr{D}(F(p))$가 성립하는 것이다.

</div>

이제 우리의 목표는 rank $k$의 distribution $\mathscr{D}$가 주어졌을 때, 이에 해당하는 ($k$차원의) integral manifold $N$이 존재하는지를 살펴보는 것이다.

예를 들어, $\mathbb{R}^m\setminus\\{0\\}$을 $\mathbb{R}^m$의 open submanifold라 하자. 이 위에서 정의된 vector field

$$X=\sum_{i=1}^m r^i\frac{\partial}{\partial r^i}\bigg|_p$$

에 대하여, 각 점 $p$마다 $\mathscr{D}(p)$를 $X_p^{\perp}$로 정의해주면 이 distribution에 해당하는 integral manifold는 $S^{m-1}$이 될 것이다. 

이렇게 distribution $\mathscr{D}$이 주어졌을 때, 우리는 integral manifold들을 통해 원래의 manifold를 층층히 나눌 수 있다. 예컨대 위의 예시에서는 $\mathbb{R}^m\setminus\\{0\\}$을 각각의 $r>0$마다 정의된 반지름 $r$의 $m-1$차원 구의 모임으로 생각할 수 있다. 이러한 상황을 *foliation*이라 부르는데, 우리는 다루지 않을 것이다.

그러나 모든 distribution이 integral manifold를 갖는 것은 아니다.

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> $\mathbb{R}^3$에서 다음의 두 vector field

$$X=\frac{\partial}{\partial x}+y\frac{\partial}{\partial z},\qquad Y=\frac{\partial}{\partial y}$$

으로 정의된 distribution $\mathscr{D}$에 대하여, 원점을 포함하는 $\mathscr{D}$의 2차원 integral manifold $N$이 존재한다고 가정하자. 그럼 원점을 포함하는 $X$의 integral curve에 대하여, $\epsilon$을 충분히 작게 잡으면 $\sigma:(-\epsilon,\epsilon)\rightarrow \mathbb{R}^3$이 $N$에 포함되도록 할 수 있다. 이 때 $X$로부터 integral curve를 직접 계산해보면 $\sigma(t)=(t,0,0)$임을 알 수 있다.

한편, 이 integral curve의 각 점 $\sigma(t)$는 다시 $N$에 속하므로, 위와 같은 논리를 $Y$에 대해 반복하면, 점 $\sigma(t)=(t,0,0)$을 시점으로 하는 integral curve $\tau_t:(-\delta_t,\delta_t)\rightarrow N$이 존재한다. 역시 계산을 해 보면 $\tau_t(s)=(t,s,0)$임을 확인할 수 있다. 

즉, 위의 계산으로부터 

$$U=\bigcup_{t\in(-\epsilon,\epsilon)}\left(\bigcup_{s\in(-\delta_t, \delta_t)} \{(t,s,0)\}\right)$$

이라 하면 이 열린집합은 $xy$평면에 속해있고, 따라서 $N$이 원점 근방에서 $xy$ 평면의 열린집합을 포함해야 한다. 

그러나 이는 불가능하다. 똑같은 논리대로라면 $Y$의 integral curve를 먼저 따른 후에 이 integral curve의 각 점에서 다시 $X$를 따라갔을 때에도 결과적으로 이 점이 $xy$ 평면 상에 있어야 하는데, $X$의 특성 상 $y$방향으로 조금만 벗어나는 순간 $\partial/\partial z$ 성분이 0이 아니게 되어 최종적으로는 $xy$ 평면 바깥으로 나가기 때문이다.

</div>

위의 예시를 통해 임의의 distribution이 항상 integral manifold를 갖지는 않는다는 것을 알 수 있다. Integral manifold를 갖는 distribution을 *integrable*이라 부르자. 그럼 위의 예시는 모든 distribution이 integrable은 아님을 보여주는 동시에, $\mathscr{D}$가 가져야 할 조건 또한 어렴풋이 짐작할 수 있게 해 준다. 즉 다음의 명제

> 만일 임의의 $X,Y\in\mathscr{D}$에 대해 $[X,Y]=0$이라면 $\mathscr{D}$은 integrable이다.

가 성립함을 추측할 수 있다. 이 추측은 참이며, 사실은 전제 $[X,Y]=0$은 훨씬 약한 가정으로 대체될 수 있다.

<div class="definition" markdown="1">

<ins id="df4">**정의 4**</ins> Distribution $\mathscr{D}$가 *involutive*라는 것은 임의의 $X,Y\in\mathscr{D}$에 대해 $[X,Y]\in\mathscr{D}$ 또한 성립하는 것이다.

</div>

<div class="proposition" markdown="1">

<ins id="lem5">**보조정리 5**</ins> Manifold $M$과 한 점 $p\in M$, 그리고 $M$ 위에서 정의된 $C^\infty$ vector field가 $X_p\neq 0$을 만족한다 하자. 그럼 적절한 coordinate system $(U,\varphi)$가 존재하여 

$$X|_U=\frac{\partial}{\partial x^1}\bigg|_U$$

가 성립한다.

</div>

이 경우는 정확하게 distribution $\mathscr{D}$의 rank가 1인 경우에 해당한다. 더 일반적인 경우에도 한쪽 방향은 매우 쉽다.

<div class="proposition" markdown="1">

<ins id="pp6">**명제 6**</ins> Integrable $C^\infty$ distribution $\mathscr{D}$는 involutive이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>



</details>

따라서, 반대방향을 증명하는 것이 핵심적인 부분이다.

<div class="proposition" markdown="1">

<ins id="thm7">**정리 7 (Frobenius)**</ins> Manifold $M$ 위에 rank $k$의 $C^\infty$, involutive distribution $\mathscr{D}$가 주어졌다 하자.

1. 각각의 $p\in M$에 대하여, $p$를 지나는 $\mathscr{D}$의 integral manifold가 존재한다.
2. 이 때, 점 $p$ 근방에서의 coordinate system $(U,\varphi)$, $\varphi=(x^i)\_{i=1}^m$를 적당히 잡아, slice들
    
    $$S=\{q\in U: x^i(q)=r^i(p), k+1\leq i\leq m\}$$

    이 각각 $\mathscr{D}$의 integral manifold이도록 할 수 있다.
3. 마지막으로, 위와 같은 상황에서 만일 $F:N\rightarrow M$이 $\mathscr{D}$의 integral manifold이고 $F(N)\subseteq U$라 하자. 만일 $N$이 connected라면, $F(N)$은 반드시 하나의 slice에만 포함된다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>



</details>

## Frobenius theorem, differential ideal version

지금까지의 내용만 보면 왜 굳이 벡터장을 다룬 이후에 위의 내용을 소개하지 않았는지가 의아할 수 있겠지만, 이는 Frobenius 정리가 differential form들의 언어로 예쁘게 적힐 수 있기 때문이다. 

$M$ 위에 정의된 rank $k$의 $C^\infty$ distribution $\mathscr{D}$가 주어졌다 하자. 임의의 $l$-form $\omega$가 $\mathscr{D}$를 annihilate시킨다는 것은 각각의 점 $p\in M$과 $v_1,\ldots, v_l\in\mathscr{D}(p)$에 대하여 항상 $\omega_p(v_1,\ldots, v_l)=0$이라는 것이다. 더 일반적으로, 임의의 form $\omega\in\Omega^\ast(M)$이 $\mathscr{D}$를 annihilate한다는 것은 $\omega$의 각각의 homogeneous part가 $\mathscr{D}$를 annihilate시키는 것이다. 이러한 form들을 모아 $\mathscr{I}(\mathscr{D})$라 하자. 다음은 이에 대한 몇 가지 성질들이다.

<div class="proposition" markdown="1">

<ins id="pp8">**명제 8**</ins> Rank $k$의 $C^\infty$ distribution $\mathscr{D}$가 주어졌다 하자. 

1. $\mathscr{I}(\mathscr{D})$는 $\Omega^\ast(M)$의 ideal이다.
2. $\mathscr{I}(\mathscr{D})$는 $n-k$개의 independent한 1-form들로 generate될 수 있다.
3. 거꾸로 만일 $\mathscr{I}\subset\Omega^\ast(M)$이 위의 1번과 2번 조건을 만족한다면, 적당한 rank $k$의 $C^\infty$ distribution $\mathscr{D}$가 존재하여 $\mathscr{I}=\mathscr{I}(\mathscr{D})$이다.

</div>

한편, $\Omega^\ast(M)$의 ideal $\mathscr{I}$가 *differential ideal*이라는 것은 $\mathscr{I}$가 추가로 $d$에 대해서도 닫혀있는 것이다. 그럼 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="pp9">**명제 9**</ins> $M$ 위에서 정의된 $C^\infty$ distribution $\mathscr{D}$가 involutive인 것은 $\mathscr{I}(\mathscr{D})$가 differential ideal인 것과 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>



</details>

Manifold $M$과 submanifold $F:N\rightarrow M$에 대하여, $N$이 $\mathscr{I}$의 integral manifold라는 것은 임의의 $\omega\in\mathscr{I}$에 대하여 $F^\ast\omega=0$인 것이다. 위의 [명제 8](#pp8)과 앞선 [명제 9](#pp9)를 적절히 조합하면 다음을 얻는다.

<div class="proposition" markdown="1">

<ins id="thm10">**정리 10 (Frobenius)**</ins> $\mathscr{I}\subset\Omega^\ast(M)$이 $n-k$개의 1-form들로 생성되는 differential ideal이라 하자. 그럼 각각의 $p\in M$를 포함하는 유일한 maximal, connected integral manifold가 존재한다.

</div>

마지막으로 우리는 리 군을 다루며 사용할 핵심적인 도구를 소개한다.

<div class="proposition" markdown="1">

<ins id="thm11">**정리 11**</ins> 두 manifold $M,N$이 주어졌다 하고, $N\times M$에서 $N,M$으로의 projection을 각각 $\pi_1,\pi_2$라 하자. 또, $T_p^\ast M$이 global frame $\omega_1,\ldots,\omega_{m_1}$을 갖는다 하자. 

1. $F:N\rightarrow M$이 $C^\infty$라 하면, $F$의 graph는 다음의 form들

    $$\pi_1^\ast F^\ast(\omega_i)-\pi_2^\ast(\omega_i)$$

    으로 생성되는 ideal의 integral manifold이다.
2. 거꾸로, $\alpha_i=\alpha_1,\ldots,\alpha_m$이 $N$에서의 1-form들이고, 다음의 form들

    $$\pi_1^\ast(\alpha_i)-\pi_2^\ast(\omega_i)$$

    로 생성되는 ideal이 differential ideal이라 하자. 그럼 각각의 $q_0\in N$, $p_0\in M$에 대하여, $q_0$의 적당한 열린근방 $U$와 그 위에서 정의된 $C^\infty$ 함수 $F:U\rightarrow M$이 존재하여 $f(q_0)=p_0$이고 $F^\ast(\omega_i)=\alpha\_i\|\_U$가 모든 $i$에 대해 성립한다. 또, 만일 $U$가 connected라면 이러한 함수 $F$는 유일하다.

</div>


---

**참고문헌**

**[War]** Frank W. Warner. *Foundations of Differentiable Manifolds and Lie Groups*, Graduate texts in mathematics, Springer, 2013  
**[Lee]** John M. Lee. *Introduction to Smooth Manifolds*, Graduate texts in mathematics, Springer, 2012  


---

[^1]: Vector field $X$가 주어졌을 때, $X_p$로 span되는 공간 $\operatorname{span}(X_p)$를 뜻한다.