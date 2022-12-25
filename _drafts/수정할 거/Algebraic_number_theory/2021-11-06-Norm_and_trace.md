---

title: "Norm and trace"
excerpt: "Fractional ideals and the Class group"

categories: [Math / Algebraic Number Theory]
permalink: /ko/math/algebraic_number_theory/norm_and_trace
header:
    overlay_image: /assets/images/Algebraic_number_theory/Norm_and_trace.png
    overlay_filter: 0.5
sidebar: 
    nav: "further_topics"
lang: ko

date: 2021-11-06
last_modified_at:
weight: 4

published: false

---

<div class="notice--warning" markdown="1">

이 글은 현재 수정중입니다.

이 글은 예전에 쓴 글로, 서술 방향이 마음에 들지 않거나 표기법이 마음에 들지 않아 전체적으로 수정이 진행중입니다. 읽으실 때 참고해주세요.

</div>


## Review of norm and trace

우리는 field theory를 다루며 extension의 norm과 trace를 간단히 다뤘었는데, 이를 잠깐 복습하자.

임의의 finite-dimensional field extension $L/K$는 $K$-algebra $L$이 주어진 것으로 생각할 수 있다. 각각의 $x\in L$에 대해, $r_x$를 다음과 같은 translation map

$$r_x:y\mapsto yx$$

으로 정의하면 $r_x$가 linear map이 된다는 것을 확인할 수 있다. 따라서, 만일 $L$의 basis $u_1,\ldots, u_n$을 선택한다면 $r_x$를 다음의 식

$$r_x(u_i)=u_ix=\sum_j a_{ij}u_j$$

를 만족하는 행렬 $[a_{ij}]$으로 나타낼 수 있다. 물론 이는 일반적으로 basis의 choice에 depend하지만, 기초적인 선형대수 지식으로부터 이 행렬의 trace와 determinant는 basis의 choice와는 independent하다는 것을 알고 있다. 따라서 다음이 잘 정의된다.

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> $L/K$가 finite-dimensional field extension이라 하자. 그럼 $L/K$의 *trace*는 $T_{L/K}(x)=\tr(r_x)$, $L/K$의 *norm*은 $N_{L/K}(x)=\det(r_x)$으로 정의된 함수이다.

</div>

그럼 몇 가지 성질들이 성립한다.

<div class="proposition" markdown="1">

<ins id="pp2">**명제 2**</ins> $L/K$가 finite-dimensional field extension이라 하고, $x,y\in L$, 그리고 $a\in K$라 하자. 다음이 성립한다.

1. $T_{L/K}(x+y)=T_{L/K}(x)+T_{L/K}$.
2. $T_{L/K}(ax)=aT_{L/K}(x)$.
3. $N_{L/K}(xy)=N_{L/K}(x)N_{L/K}(y)$.
4. $N_{L/K}(ax)=a^nN_{L/K}(x)$ where $n=[L:K]$.
5. $L/E/K$가 extension들의 tower라면, $T_{L/K}(x)=T_{E/K}(T_{L/E}(x))$.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선, $r_{x+y}=r_x+r_y$이므로 trace의 linearity에 의하여 1번과 2번이 성립한다. 또, $r_{xy}=r_xr_y$가 성립하므로, 3번은 determinant의 multiplicative property로부터 자명하다. 4번도 마찬가지로 determinant의 성질이다.

따라서 5번 성질만 보이면 충분하다. $(a\_i)\_{1\leq i\leq s}$들이 $E/K$의 basis이고, $(b\_j)\_{1\leq j\leq t}$들이 $L/E$의 basis라 하자. 우선 $T_{L/E}(x)$와 $T_{E/K}(y)$를 각각 계산해보자. 각각의 $i=1,2,\ldots s$에 대하여, 

$$xb_j=\sum_{q=1}^t\beta^{(j)}_q(x)b_q$$

라 하자. 그럼 $T_{L/E}(x)$의 값은 단순히 diagonal들의 합인

$$T_{L/E}(x)=\sum_{j=1}^t\beta_j^{(j)}(x)$$

가 된다. 이와 비슷하게, $T_{E/K}(y)$를 계산하기 위해

$$ya_i=\sum_{p=1}^s\alpha^{(i)}_p(y)a_p$$

라 하면

$$T_{E/K}(y)=\sum_{i=1}^s\alpha_i^{(i)}(y)$$

가 성립한다. 따라서

$$T_{E/K}(T_{L/E}(x))=\sum_{i=1}^s\alpha_i^{(i)}\left(\sum_{j=1}^t\beta_j^{(j)}(x)\right)=\sum_{i=1}^s\sum_{j=1}^t\alpha_i^{(i)}(\beta_j^{(j)}(x))$$

이다. 한편, $a_ib_j$들의 모임이 $L/K$의 basis가 되므로, 마찬가지의 계산을 이번에는 $L/K$에서 해 보면, 고정된 pair $(i,j)$에 대하여

$$xa_ib_j=a_i(xb_j)=\left(\sum_{q=1}^t\beta_q^{(j)}(x)b_q\right)a_i=\sum_{p=1}^s\alpha_p^{(i)}\left(\sum_{q=1}^t\beta_q^{(j)}(x)b_q\right)a_p=\sum_{p=1}^s\sum_{q=1}^t\alpha_p^{(i)}(\beta_q^{(j)}(x))a_pb_q$$

가 된다. 따라서 $T_{L/K}(x)$는 diagonal들의 합

$$T_{L/K}(x)=\sum_{i=1}^s\sum_{j=1}^t\alpha_i^{(i)}(\beta_j^{(j)}(x))$$

이 되므로, 이를 앞선 식과 연립하면 5번을 얻는다. 

</details>

물론 5번 또한 norm에 대한 analogue가 존재한다. 하지만 이를 직접 보이기보다는 우선 우리 이야기를 먼저 진행하자. 우선 만약 $x\in L$이라면, $x$의 minimal polynomial $f$가 존재할 것이다. 한편, $x$가 정의하는 자연스러운 map $r_x$는 행렬로써 characteristic polynomial $g$를 갖는다. Cayley-Hamilton 정리에 의해 $g(r_x)=0$인데, $r_x$는 그냥 $x$를 곱하는 translation map이므로, 이는 곧 $g(x)=0$이라는 뜻이고 따라서 $f$는 $g$를 나눈다. 이는 우리가 앞으로 종종 사용할 사실인데, 특히 우리는 characteristic polynomial의 상수항과, 두 번째로 큰 차수의 항 (즉 $n-1$차항)의 계수가 trace와 determinant로 각각 주어진다는 것을 알고 있으므로, 이 사실과 함께 사용하면 많은 것을 증명할 수 있다.

## Trace form and separable extensions

우리는 trace map $T$를 이용해서 다음과 같은 bilinear form $L\times L\rightarrow K$를 식

$$(x,y)=T_{L/K}(xy)$$

으로 정의할 수 있다. 이 map은 자명하게 symmetric bilinear form이 된다. 

<div class="proposition" markdown="1">

<ins id="pp3">**명제 3**</ins> 위에서 정의한 bilinear form이 nondegnerate하는 것은 $L/K$가 separable인 것과 동치이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $L/K$가 separable이라 가정하자. 그럼 primitive element theorem에 의해, $L=K(\theta)$인 $\theta\in L$이 존재한다. 이제 $1,\theta, \ldots, \theta^{n-1}$이 $L/K$의 basis를 이루므로, 위에서 정의한 bilinear form이 nondegenerate인 것은 이 basis에 대한 다음의 Gram matrix

$$\begin{pmatrix}(1,1)&(1,\theta)&\cdots&(1,\theta^{n-1})\\ (\theta,1)&(\theta,\theta)&\cdots&(\theta, \theta^{n-1})\\ \vdots&\vdots&\ddots&\vdots\\ (\theta^{n-1},1)&(\theta^{n-1},\theta)&\cdots&(\theta^{n-1},\theta^{n-1})\end{pmatrix}$$

이 nonsingular인 것과 동치이다. $f$가 $\theta$의 minimal polynomial이라 하자. 그럼 $f$의 degree는 $[L:K]$와 같다. 적당한 splitting field $E$에 대하여, $f$를

$$f(\x)=(\x-\theta_1)(\x-\theta_2)\cdots(\x-\theta_n),\quad \theta=\theta_1$$

이라 쓸 수 있고, $f$는 separable이므로 이들 $\theta_i$들은 모두 서로 다르다. 한편, $\theta$의 (linear map $r_\theta$로서의) characteristic polynomial 또한 마찬가지로 degree $n$이므로, $f$가 정확하게 $\theta$의 characteristic polynomial이 된다. 따라서 $f$의 $\x^{n-1}$의 계수를 비교하면,

$$T_{L/K}(\theta)=\theta_1+\theta_2+\cdots+\theta_n$$

을 얻는다. 한편, $r_\theta$의 characteristic polynomial $f$가 linear factor들로 정확하게 split하므로, $r_\theta$를 나타내는 행렬은 diagonalizable하고, 따라서 이 행렬을 $M_\theta$라 하면 다음의 식

$$U^{-1}M_\theta U=\begin{pmatrix}\theta_1&0&\cdots&0\\ 0&\theta_2&\cdots&0\\ \vdots&\vdots&\ddots&\vdots\\ 0&0&\cdots&\theta_n\end{pmatrix}$$

이 성립한다. 이제 양 변을 거듭제곱하면

$$U^{-1}M_\theta^k U=\begin{pmatrix}\theta_1^k&0&\cdots&0\\ 0&\theta_2^k&\cdots&0\\ \vdots&\vdots&\ddots&\vdots\\ 0&0&\cdots&\theta_n^k\end{pmatrix}$$

를 얻으므로, 이를 통해 앞선 식을 일반화하여

$$T_{L/K}(\theta^k)=\theta_1^k+\theta_2^k+\cdots+\theta_n^k$$

라 할 수 있다. 행렬 $V$를 다음의 식

$$V=\begin{pmatrix}1&1&\cdots&1\\ \theta_1&\theta_2&\cdots&\theta_n\\ \theta_1^2&\theta_2^2&\cdots&\theta_n^2\\ \vdots&\vdots&\ddots&\vdots\\ \theta_1^{n-1}&\theta_2^{n-1}&\cdots&\theta_n^{n-1}\end{pmatrix}$$

으로 정의하면, $VV^t$의 각 성분은 정확히

$$\sum_k\theta_k^{i-1}\theta_k^{j-1}=\sum\theta_k^{i+j-2}=T_{L/K}(\theta^{i-1}\theta^{j-1}$$

이므로, $VV^t$가 Gram matrix가 된다. 한편, $\theta_i$들이 모두 다르므로 $V$의 determinant

$$\det V=\prod_{i>j}(\theta_i-\theta_j)$$

는 0이 아니고, 따라서 Gram matrix 또한 nonsignular이다. 

이제 반대방향을 보여야 한다. $L/K$가 separable이 아니라 하면, $K$는 characteristic $p$를 가진다. $L$에 대한 $K$의 relative separable closure를 $F$라 하자. 그럼 임의의 $x\in L\setminus F$와 $y\in L$에 대해 $(x,y)=0$이 성립한다. 즉, bilinear form $(-,-)$이 degenerate한다. 이를 증명하기 위해 우리는 두 가지 경우를 나눠 생각한다.

1. 우선 $xy\not\in F$라 하자. 그럼 적당한 $a\in F$가 존재하여, $xy$의 $F$에 대한 minimal polynomial은 $\x^p-a$이다. 한편, $L/F$에서 $xy$의 characteristic polynomial은 이제 degree를 고려하면 $(\x^p-a)^{p^{m-1}}$이 되어야 하므로 ($[L:F]=p^m$), 이 식을 전개한 후 trace를 살펴보면 $T_{L/F}(xy)=0$임을 알고 따라서 trace의 transitivity에 의해 $T_{L/K}(xy)=0$이 성립한다. 

2. 이제 $xy\in F$인 경우를 생각하면, $T_{L/F}(xy)=xyT_{L/F}(1)$이고, $T_{L/F}=p^m$이므로 마찬가지로 $T_{L/F}(xy)=0$이 되어 transitivity에 의해 $T_{L/K}(xy)=0$이다. 

</details> 

## Galois extensions

$F/L/K$가 separable field extension들의 tower이고, $F/K$가 Galois라 하자. 그럼 $G=\Gal(F/K)$는 $H=\Gal(F/L)$을 포함하는 group이 되며, 이 때 $H$는 $L$을 fix하는 $K$-automorphism들의 subgroup이다. $G/H$의 원소들을

$$\sigma_1H,\sigma_2H,\ldots, \sigma_nH$$

이라 하자. 그럼 Galois theory에 의해 $n=[L:K]$이고, $\sigma_i$들은 각각 $L$에서 $F$로 들어가는 injection들이다.  

<div class="proposition" markdown="1">

<ins id="thm4">**정리 4**</ins> 위와 같은 상황에서, 임의의 $x\in L$에 대하여 

$$T_{L/K}(x)=\sigma_1(x)+\cdots+\sigma_n(x),\qquad N_{L/K}(x)=\sigma_1(x)\cdots\sigma_n(x)$$

이 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

임의의 $x\in L$에 대하여, $x$의 $K$에 대한 minimal polynomial을 $q(\x)$라 하자. 그럼 앞서 살펴본 것과 같이, $q$는 정확히 $r_x:K(x)\rightarrow K(x)$의 characteristic polynomial이 된다. 이제 $[L:K(x)]=d$, $[K(x):K]=m$이라 하면 $L$은 $d$개의 $K(x)$들의 direct sum이 되고, 따라서 $x$의 characteristic polynomial은 $q(\x)^d$가 된다. 이제 $x_1,\ldots, x_m$이 $q(\x)$의 근이라 하고, $x=x_1$이라 하자. 즉,

$$q(\x)=\prod(\x-x_i)$$

이다. 그럼 $L$ 위에서 $r_x$의 characteristic polynomial은 $q(\x)^d$이므로, 이를 전개한 후 계수를 비교해보면

$$T_{L/K}(x)=d(x_1+\cdots+x_m),\qquad N_{L/K}(x)=(x_1x_2\ldots x_m)^d$$

임을 알 수 있다. 이제 $H_1$을 $K(x)$를 fix하는 $G$의 subgroup이라 하자. 그럼 $K\subset K(x)$이므로, $H\subset H_1$이고 $d=[H_1:H]$, $m=[G:H_1]$이다. 이들 coset이 

$$\gamma_1 H\cup\cdots\cup\gamma_dH=H_1,\qquad \tau_1H_1\cup\cdots\cup\tau_mH_1=G$$

으로 나타났다 하자. 첫째 식을 둘째 식에 넣으면, $H$에 대한 $G$의 coset들의 representative들이 $\tau_i\gamma_j$로 주어지는 것을 확인할 수 있다. 어차피 $\sigma_k$와, 이에 해당되는 $\tau_i\gamma_j$는 $H$의 원소, 즉 $x$를 fix하는 morphism만큼만 차이나므로 우리는 trace와 norm을 계산할 때 방금 구한 representative들 $\tau_i\gamma_j$들을 이용해도 된다. 그럼 $\gamma_j(x)=x$가 항상 성립하므로, 적당한 renumbering을 통해 $\tau(x)=x_i$라 할 수 있고, 따라서

$$\begin{aligned}\sum_k\sigma_k(x)&=\sum_i\sum_j\tau_i\gamma_j(x)=d\sum_i\tau_i(x)=d\sum_i x_i=T_{L/K}(x)\\ \prod_k\sigma_k(x)&=\prod_i\prod_j\tau_i\gamma_j(x)=\prod_i\tau_i(x^d)=\left(\prod_i x_i\right)^d=N_{L/K}(x))\end{aligned}$$

이 성립한다. 

</details>

따라서 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="crl5">**따름정리 5**</ins> $L/E/K$가 finite-dimensional separable extension들의 tower라 하면 

$$N_{L/K}(x)=N_{E/K}(N_{L/E}(x))$$

가 항상 성립한다.
</div>


---

**References**

[Jan] Gerald J. Janusz. *Algebraic Number Fields*, American  Mathematical Soc., 1995

---
