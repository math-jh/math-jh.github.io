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

을 만족한다. 따라서, $E_\lambda$로 제한했을 때 $A$는 아주 다루기 쉬운 대상이 된다. 

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

이 성립하는 것이다.

</div>