---

title: "대각화"
excerpt: "행렬의 대각화와 고유공간분해"

categories: [Math / Linear Algebra]
permalink: /ko/math/linear_algebra/diagonalization
sidebar: 
    nav: "linear_algebra-ko"

header:
    overlay_image: /assets/images/Linear_algebra/Diagonalization.png
    overlay_filter: 0.5

date: 2022-09-18
last_modified_at: 2022-09-18

weight: 20

---

## 공간의 직합

$n\times n$ 행렬 $A$와, 한 고윳값 $\lambda$를 생각하자. 정의에 의해 $\lambda$에 해당하는 고유공간 $E_\lambda$의 임의의 벡터 $v$는 반드시 다음의 식

$$Av=\lambda v$$

을 만족한다. 따라서, $E_\lambda$로 제한했을 때 $A$는 아주 다루기 쉬운 대상인 $v\mapsto \lambda v$가 된다. 

더 일반적으로, $A$를 $\mathbb{R}^n$에서 $\mathbb{R}^n$으로의 linear map으로 생각하고, 정의역 $\mathbb{R}^n$을 고유공간 $E_\lambda$들로 덮을 수 있다 가정하자. 즉

$$\mathbb{R}^n=\operatorname{span}\left(\bigcup_{\lambda\in\operatorname{Spec}(A)}E_\lambda\right)$$

이라 하자. 그럼 임의의 $v\in\mathbb{R}^n$에 대하여, $v_\lambda\in E_\lambda$들이 각각 존재하여

$$v=\sum_{\lambda\in\operatorname{Spec}(A)}v_\lambda$$

이라 쓸 수 있으며, 따라서 

$$Av=A\left(\sum_{\lambda\in\operatorname{Spec}(A)}v_\lambda\right)=\sum_{\lambda\in\operatorname{Spec}(A)}Av_\lambda$$

이고, 위의 논증에 의하여 $Av_\lambda=\lambda v_\lambda$이므로 다음의 식

$$Av=\sum_{\lambda\in\operatorname{Spec}(A)}\lambda v_\lambda$$

을 얻는다. 물론 위의 계산이 말이 되기 위해서는 $v$를 $v_\lambda$들의 합으로 나타내는 방법이 유일해야 한다. 이를 다음과 같이 정의한다.

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> 임의의 $F$-벡터공간 $V$가 그 부분공간 $(W\_i)\_{i\in I}$들의 *direct sum<sub>직합</sub>*이라는 것은, 임의의 $v\in V$가 주어질 때마다 적당한 $(v\_i)\_{i\in I}$가 <em_ko>유일하게</em_ko> 존재하여 

$$v=\sum_{i\in I} v_i$$

이 성립하는 것이다.[^1] 이를 $V=\bigoplus\_{i\in I}W_i$와 같이 적는다. 

</div>

자명하지 않은 경우 중 가장 쉬운 것은 $I$가 원소 두 개짜리 집합일 때이다.

<div class="proposition" markdown="1">

<ins id="pp2">**명제 2**</ins> $F$-벡터공간 $V$의 두 부분공간 $W_1,W_2$에 대하여, $V=W_1\oplus W_2$인 것은 $V=W_1+W_2$이고 $W_1\cap W_2=\\{0\\}$인 것과 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $V=W_1\oplus W_2$라 가정하자. 정의에 의해 $W_1+W_2\subseteq V$인 것은 자명하다. 거꾸로 임의의 $v\in V$를 택하면, $v=w_1+w_2$이도록 하는 $w_i\in W_i$가 존재하므로 $V\subseteq W_1+W_2$ 또한 성립한다. 이로부터 $V=W_1+W_2$임을 안다. 한편, 만일 $W_1\cap W_2\neq \\{0\\}$이라면, 영이 아닌 $w\in W_1+W_2$에 대하여

$$w=0+w=w+0$$

이므로 [정의 1](#df1)에서의 유일성에 모순이 된다. 

거꾸로 $V=W_1+W_2$이고 $W_1\cap W_2=\\{0\\}$이라 하자. 임의의 $v\in V$에 대하여, $V=W_1+W_2$이므로 $v=w_1+w_2$이도록 하는 $w_1\in W_i$가 반드시 존재한다. 또, 이와 같은 표현은 유일하다. 만일

$$v=w_1+w_2=w_1'+w_2'$$

라면, 

$$w_1-w_1'=w_2-w_2'$$

에서 좌변은 $W_1$의 원소, 우변은 $W_2$의 원소이므로 조건 $W_1\cap W_2=\\{0\\}$으로부터 $w_1-w_1'=w_2-w_2'=0$이기 때문이다. 

</details>

위 명제의 한 쪽 방향은 $I$가 셋 이상의 원소를 가지고 있어도 성립한다. 즉, 만일 $V=\bigoplus_{i\in I}W_i$라면, $V=\sum_{i\in I}W_i$이고, $i\neq j$일 때마다 $W_i\cap W_j=\\{0\\}$이 성립하며, 그 증명 또한 위와 같다. 그러나 일반적으로 반대방향은 성립하지는 않는다. 

가령 $V=\mathbb{R}^2$로 두고, $V$의 두 standard basis $e_1,e_2$를 잡자. $W_1=\mathbb{R}e_1$, $W_2=\mathbb{R}e_2$, $W_3=\mathbb{R}(e_1+e_2)$으로 잡으면 $V=W_1+W_2+W_3$, 그리고 $i\neq j$일 때마다 $W_i\cap W_j$지만 $V\neq W_1\oplus W_2\oplus W_3$이다. 

$$e_1+e_2=e_1+e_2+0=0+0+(e_1+e_2)$$

와 같이, $e_1+e_2\in V$를 나타내는 방법이 유일하지 않기 때문이다. 

또 다른 예시로, $V$의 basis $\mathcal{B}=\\{v_1,\ldots, v_n\\}$을 하나 택하자. $W_i=Fv_i$이라 하면, $\mathcal{B}$가 basis라는 조건은 정확하게 $V$가 $W_i$들의 direct sum이라는 조건과 일치하게 된다. 더 일반적으로 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="pp2">**명제 2**</ins> 임의의 $F$-벡터공간 $V$와, 부분공간 $(W\_i)\_{i\in I}$에 대하여 $V=\bigoplus\_{i\in I} W\_i$인 것은 $W_i$의 basis $\mathcal{B}\_i$들이 $i\neq j$일 때마다 $\mathcal{B}\_i\cap\mathcal{B}\_j=\emptyset$을 만족하고, $\bigcup\_{i\in I}\mathcal{B}\_i$가 $V$의 basis가 되는 것과 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $V=\bigoplus W_i$라 가정하고, $W_i$들의 basis $\mathcal{B}_i$를 택하자. 만일 $\mathcal{B}_i\cap\mathcal{B}_j\neq\emptyset$이라면 $W_i\cap W_j\neq\emptyset$가 되어 [명제 2](#pp2) 이후의 논의에 모순이므로, 반드시 $\mathcal{B}_i\cap\mathcal{B}_j=\emptyset$이어야 한다. 임의의 $v\in V$에 대하여, $V=\bigoplus W_i$로부터 다음의 식

$$v=\sum_{i\in I} w_i$$

을 만족하는 

</details>

[^1]: 물론, 언제나와 같이 이 합은 사실은 유한합인 것으로 가정한다. 즉 $(v\_i)\_{i\in I}$는 finitely supported인 것으로 가정한다.