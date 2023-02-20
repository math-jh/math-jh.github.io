---

title: "미분 아이디얼"
excerpt: "Differential ideal과 Frobenius theorem"

categories: [Math / Manifold]
permalink: /ko/math/manifold/differential_ideal
header:
    overlay_image: /assets/images/Math/Manifold/Differential_ideal.png
    overlay_filter: 0.5
sidebar: 
    nav: "manifold-ko"

date: 2023-01-16
last_modified_at: 2023-01-16
weight: 16

---

우리는 앞서 differential form들의 모임이 $C^\infty(M)$-algebra가 된다는 것을 확인했다. 대수적으로 이 모임의 아이디얼을 생각할 수 있으며, 뿐만 아니라 이 모임 $\Omega^\ast(M)$은 dg-algebra였으므로 정확한 맥락에서는 지금 정의할 *differential ideal*을 생각하는 것이 더 자연스럽다.

## 미분 아이디얼의 정의

우선 다음 정의부터 시작한다.

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> Manifold $M$ 위에 정의된 $k$차원 distribution $\mathcal{D}$를 생각하자. $l$-form $\omega$가 $\mathcal{D}$를 *annihilate*한다는 것은 각각의 $p\in M$에 대하여

$$\omega_p(v_1,\ldots, v_l)=0,\qquad v_i\in\mathcal{D}(p)$$

이 성립하는 것이다. 더 일반적으로, 임의의 form $\omega$가 $\mathcal{D}$를 *annihilate*한다는 것은 $\omega$의 homogeneous part들이 각각 $\mathcal{D}$를 annihilate하는 것이다.

</div>

이 때, $\mathcal{D}$를 annihilate하는 differential form들의 모임을

$$\mathcal{I}(\mathcal{D})=\{\omega\in\Omega^\ast(M)\mid\text{$\omega$ annihilates $\mathcal{D}$}\}$$

으로 정의한다. 

<div class="proposition" markdown="1">

<ins id="pp2">**명제 2**</ins> Manifold $M$ 위에 정의된 $k$차원 distribution $\mathcal{D}$를 생각하자. 

1. $\mathcal{I}(\mathcal{D})$는 $\Omega^\ast(M)$의 ideal이다.
2. $\mathcal{I}(\mathcal{D})$는 국소적으로 $m-k$개의 1-form들로 생성된다.
3. 만일 $\mathcal{I}$가 위의 두 조건을 만족하는 ideal이라면, 유일한 $k$차원 distribution $\mathcal{D}$가 존재하여 $\mathcal{I}=\mathcal{I}(\mathcal{D})$이도록 할 수 있다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

첫째 주장은 정의로부터 자명하다. 

둘째 주장을 보이기 위해, $p\in M$이라 하자. 그럼 $p$ 근방에서 $\mathcal{D}$를 생성하는 independent한 벡터장들 $X_{m-k+1},\ldots, X_m$이 존재한다. 이제 이 집합에 벡터장들 $X_1,\ldots, X_{m-k}$를 추가하여 $\\{X_1,\ldots, X_m\\}$이 $p$의 근방 $U$에서 tangent space들의 local basis가 된다고 하자. 그럼 이들의 dual을 취하여 $1$-form들 $\omega_1,\ldots, \omega_m$을 얻을 수 있으며, 이 때

$$\omega_i(X_j)=\delta_{ij}$$

이므로 $\omega_1,\ldots,\omega_{m-k}$들이 원하는 $1$-form들이 된다는 것을 쉽게 보일 수 있다. 

셋째 주장은 위의 증명들을 거꾸로 뒤집으면 된다. 

</details>

$\Omega^\ast(M)$는 differential graded algebra이므로, ideal들 또한 differential $d:\Omega^\ast(M)\rightarrow\Omega^\ast(M)$에 대해서도 닫혀있는 것들에 관심을 가지는 것이 자연스럽다. 

<div class="definition" markdown="1">

<ins id="df3">**정의 3**</ins> $\Omega^\ast(M)$의 ideal $\mathcal{I}$가 *differential ideal<sub>미분 아이디얼</sub>*이라는 것은 $\mathcal{I}$가 $d$에 대하여 닫혀있는 것이다.

</div>

## Differential ideal과 프로베니우스 정리

이제 우리는 앞선 글에서 살펴본 프로베니우스 정리를 differential form의 언어로 서술한다. 이는 별다른 것은 아니고, 벡터장에 대한 것을 그 dual $1$-form들에 대한 것으로 바꾸는 것에 불과하다.

<div class="proposition" markdown="1">

<ins id="pp4">**명제 4**</ins> Manifold $M$ 위에 정의된 distribution $\mathcal{D}$에 대하여, $\mathcal{D}$가 involutive인 것과 $\mathcal{I}(\mathcal{D})$가 differential ideal인 것이 동치이다.

</div>

<div class="definition" markdown="1">

<ins id="df5">**정의 5**</ins> Manifold $M$과 submanifold $\Phi:N\rightarrow M$에 대하여, $N$이 ideal $\mathcal{I}$의 *integral manifold*인 것은 임의의 $\omega\in\mathcal{I}$에 대하여 $(d\Phi)^\ast(\omega)\equiv 0$이 성립하는 것이다. 

</div>

그럼 이러한 조건에서 프로베니우스 정리는 다음과 같이 쓸 수 있다.

<div class="proposition" markdown="1">

<ins id="thm6">**정리 6**</ins> $m$차원 manifold $M$과, $m-k$개의 independent 1-form들로 생성된 differential ideal $\mathcal{I}$가 주어졌다 하자. 그럼 각각의 $p\in M$마다, $p$를 지나는 $\mathcal{I}$의 integral manifold가 존재하며, 이 때 integral manifold는 $k$차원이다.

</div>

## 그래프와 differential form

다음 정리는 리 군과 리 대수 사이의 관계를 탐구하는 데에 중요하게 사용된다.

<div class="proposition" markdown="1">

<ins id="thm7">**정리 7**</ins> 두 manifold $M^m,N^n$이 주어졌다 하고, $\pi_1:N\times M\rightarrow N$과 $\pi_2:N\times M\rightarrow M$이 각각 canonical projection이라 하자. 또, $M$에서 정의된 1-form들의 모임이 basis $\\{\omega_1,\ldots,\omega_m\\}$을 갖는다 가정하자. 

1. 임의의 $f:N\rightarrow M$에 대하여, $\graph(f)$는 다음의 집합

    $$\{(d(f\circ \pi_1))^\ast(\omega_i)-(d\pi_2)^\ast(\omega_i)\mid i=1,\ldots, m\}$$

    으로 생성되는 ideal $\mathcal{I}$의 integral manifold이다.
2. $N$ 위의 1-form들 $\alpha_1,\ldots,\alpha_m$에 대하여, 다음의 집합

    $$\{(d\pi_1)^\ast(\alpha_i)-(d\pi_2)^\ast(\omega_i)\mid i=1,\ldots,m\}$$

    으로 생성되는 ideal이 differential ideal이라 가정하자. 그럼 임의의 $q_0\in N,p_0\in M$이 주어질 때마다, $q_0$의 적당한 열린근방 $U$와, $f(q_0)=p_0$을 만족하는 $C^\infty$ 함수 $f:U\rightarrow M$이 존재하여

    $$(df)^\ast(\omega_i)=\alpha_i|_U$$

    가 성립하도록 할 수 있다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

간단히 흐름만 소개한다.

1. 우선 [§미분다양체의 예시들, ⁋예시 5](/ko/math/manifold/examples_of_manifolds#ex5)를 따라 다음의 집합
    
    $$\graph(f)=\{(p,q)\mid f(p)=q\}$$
    
    이 $N\times M$의 submanifold가 된다는 것을 보인다. 이 때 inclusion map은 자연스러운 함수
    
    $$\iota:\graph(f)\rightarrow N\times M;\qquad (p,q)\mapsto (p,q)$$
    
    로 주어진다. 이제 $\mathcal{I}$가 이를 integral manifold로 갖는다는 것을 증명하려면 주어진 form들 

    $$\mu_i:=(d(f\circ\pi_1))^\ast(\omega_i)-(d\pi_2)^\ast(\omega_i)$$

    이 $(d\iota)^\ast(\omega_i)=0$을 만족한다는 것을 보여야 한다. 이는
    
    $$(d\iota)^\ast(\mu_i)=(d(\pi_1\circ\iota))^\ast(df)^\ast(\omega_i)-(d(\pi_2\circ\iota))^\ast(\omega_i)=(df)^\ast(\omega_i)-(df)^\ast(\omega_i)=0$$

    으로부터 분명하다.

2. 주어진 form들의 집합으로 생성되는 ideal을 $\mathcal{I}$라 하자. 그럼 프로베니우스 정리에 의하여, $\mathcal{I}$는 $(m+n)-m=c$차원의 integral manifold $I$를 갖는다. 이후, 임의의 점 $q\in I$에 대하여, $d\pi_1$을 $I_q$로 제한한 것이 전단사함수임을 보이면 된다. 

</details>

---

**참고문헌**

**[War]** Frank W. Warner. *Foundations of Differentiable Manifolds and Lie Groups*, Graduate texts in mathematics, Springer, 2013  
**[Lee]** John M. Lee. *Introduction to Smooth Manifolds*, Graduate texts in mathematics, Springer, 2012  

---