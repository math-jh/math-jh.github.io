---

title: "벡터공간의 차원"
excerpt: "벡터공간의 기저와 차원"

categories: [Math / Basic Linear Algebra]
permalink: /ko/math/basic_linear_algebra/dimension
sidebar: 
    nav: "basic_linear_algebra-ko"

header:
    overlay_image: /assets/images/Math/Basic_Linear_Algebra/Dimension.png
    overlay_filter: 0.5

date: 2022-07-31
last_modified_at: 2022-07-31

weight: 5

---

## 벡터공간의 차원

[§벡터공간의 기저, ⁋예시 9](/ko/math/basic_linear_algebra/basis#ex9)와 [§벡터공간의 기저, ⁋예시 11](/ko/math/basic_linear_algebra/basis#ex11)로부터 벡터공간 $V$의 basis는 유일할 필요가 없다는 것을 알 수 있다. 그런데, 이 예시들을 보면 공통적으로 basis의 원소의 갯수들은 동일하게 유지된다는 것도 확인할 수 있다. 이는 우연이 아니다.

<div class="proposition" markdown="1">

<ins id="thm1">**정리 1**</ins> $\mathbb{k}$-벡터공간 $V$에 대하여, $V$의 두 basis $\mathcal{B}_1$, $\mathcal{B}_2$가 주어졌다면 $\lvert \mathcal{B}_1\rvert=\lvert \mathcal{B}_2\rvert$이 성립한다.

</div>

이 정리는 $\mathcal{B}_1$, $\mathcal{B}_2$가 무한한 경우도 포함한다. 이를 보이기 위해서는 세 단계가 필요하다.

1. 우선, 만일 $V$의 *어떤* basis가 무한하다면, 다른 basis들도 반드시 무한하며 이들의 크기는 동일하다.
2. 그러므로 $V$의 어떤 basis가 유한하다면, 다른 basis들도 모두 유한해야 한다.
3. 마지막으로, 만일 $V$의 두 유한한 basis가 주어진다면, 이들 두 basis의 원소의 갯수는 동일하다.

물론 이 정리도 지금 증명하자면 못할 것은 없지만, [§벡터공간의 기저, ⁋정리 10](/ko/math/basic_linear_algebra/basis#thm10)과 마찬가지로 이를 증명하기 위해는 약간의 집합론적인 지식이 필요하므로 별도의 글로 분리한다. 다만 마지막 단계는 별다른 배경지식 없이도 증명할 수 있다.

<div class="proposition" markdown="1">

<ins id="lem2">**보조정리 2**</ins> $\mathbb{k}$-벡터공간 $V$에 대하여, 만일 $\mathcal{B}_1$과 $\mathcal{B}_2$이 모두 $V$의 basis이고 유한하다면, $\lvert \mathcal{B}_1\rvert=\lvert \mathcal{B}_2\rvert$가 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$\mathcal{B}_1=\\{x_1,x_2,\ldots, x_m\\}$, 그리고 $\mathcal{B}_2=\\{y_1,y_2,\ldots, y_n\\}$이라 하고, $m=n$임을 보여야 한다. 결론에 반하여 $m>n$이라 하자.

우선 $x_1\in V$이므로, $x_1$은 $y_1$, $y_2$, $\ldots$, $y_n$들의 일차결합으로 나타낼 수 있다. 따라서 [§벡터공간의 기저, ⁋명제 6](/ko/math/basic_linear_algebra/basis#prop6)에 의하여, 집합 $\\{x_1,y_1,y_2,\ldots, y_n\\}$은 일차종속이다. 즉, 모두 0은 아닌 스칼라들 $\beta_1$, $\alpha_1$, $\alpha_2$, $\ldots$, $\alpha_n$이 존재하여

$$\beta_1x_1+\alpha_1y_1+\alpha_2y_2+\cdots+\alpha_n y_n=0\tag{1}$$

이도록 할 수 있다. 여기서 $\beta_1$이 0이 될 수 없음은 자명하다. 만일 $\beta_1=0$이라면 위의 식은 

$$\alpha_1y_1+\alpha_2y_2+\cdots+\alpha_ny_n=0$$

이 되어, $y_1$, $y_2$, $\ldots$, $y_n$이 일차독립이라는 가정에 모순이기 때문이다. 또, 만일 모든 $\alpha_i$가 0이라면 $\beta_1x_1=0$인데, $\beta_1\neq 0$이므로 $x_1=0$이다. 이 경우 $\\{x_1, x_2, \ldots, x_m\\}$은 자명하게 일차종속이게 되므로, 어떤 0이 아닌 $\alpha_i$가 존재한다고 가정하자. 그럼 우리는 위의 식 (1)을 변형하여 다음의 식

$$y_i=\frac{\beta_1}{\alpha_i}x_1-\frac{\alpha_1}{\alpha_i}y_1-\cdots-\frac{\alpha_{i-1}}{\alpha_i}y_{i-1}-\frac{\alpha_{i+1}}{\alpha_i}y_{i+1}-\cdots-\frac{\alpha_n}{\alpha_i}y_n$$

을 얻는다. 따라서 만일 우리가 집합 $\\{x_1, y_1, y_2, \ldots, y_n\\}$에서 $y_i$를 빼더라도 이 집합은 여전히 $V$를 span한다.  

한편, 이 집합은 일차독립이다. 어떠한 스칼라들 $\beta_1'$, $\alpha_1'$, $\ldots$, $\alpha_n'$에 대하여 

$$\beta_1'x_1+\alpha_1'y_1+\alpha_2'y_2+\cdots+\alpha_{i-1}'y_{i-1}+\alpha_{i+1}'y_{i+1}+\cdots+\alpha_n'y_n=0$$

이라고 한다면, 위에서와 같은 이유로 $\beta_1'\neq 0$이 되고, 따라서 

$$x_1=-\frac{\alpha_1'}{\beta_1'}y_1-\frac{\alpha_2'}{\beta_1'}y_2-\cdots-\frac{\alpha_{i-1}'}{\beta_1'}y_{i-1}-\frac{\alpha_{i+1}'}{\beta_1'}y_{i+1}-\cdots-\frac{\alpha_n'}{\beta_1'}y_n$$

을 앞선 식에 대입하면

$$0=\left(\frac{\alpha_1'\beta_1}{\alpha_i\beta_1'}+\frac{\alpha_1}{\alpha_i}\right)y_1+\cdots+\left(\frac{\alpha_{i-1}'\beta_1}{\alpha_i\beta_{i-1}'}+\frac{\alpha_{i-1}}{\alpha_i}\right)y_{i+1}+y_i+\left(\frac{\alpha_{i+1}'\beta_{i+1}}{\alpha_i\beta_{i+1}'}+\frac{\alpha_{i+1}}{\alpha_i}\right)y_{i+1}+\cdots+\left(\frac{\alpha_n'\beta_n}{\alpha_i\beta_n'}+\frac{\alpha_n}{\alpha_i}\right)y_n$$

을 얻는다. $y_i$의 계수가 $0$이 아니므로 이는 $\\{y_1,y_2,\ldots,y_n\\}$이 일차독립이라는 가정에 모순이다.

따라서 우리는 $V$의 새로운 basis $\\{x_1,y_1,y_2,\ldots,y_{i-1}, y_{i+1},\ldots, y_n\\}$을 얻었다. 일반성을 잃지 않고, 우리가 없앤 벡터가 $y_n$이었다고 한다면 이렇게 생긴 새 basis는 $\\{x_1, y_1, \ldots, y_{n-1}\\}$이다. 이제 다시 이 basis에 $x_2$를 넣어 $\\{x_2, x_1, y_1, y_2, \ldots, y_n\\}$을 생각하자.

$$\beta_2x_2+\beta_1x_1+\alpha_1y_1+\alpha_2y_2+\ldots+\alpha_{n-1}y_{n-1}=0$$

라 한다면 위와 같은 논리로 $\beta_2\neq 0$이고, $x_2=0$인 경우를 제외한다면 $\beta_1$, $\alpha_1$, $\ldots$, $\alpha_{n-1}$ 중 0이 아닌 계수가 존재한다. 

여기서 만일 $\beta_1$이 유일하게 0이 아닌 계수라면, 위의 식은 $\beta_2x_2+\beta_1x_1=0$이 되어 $\\{x_1,x_2\\}$가 일차종속이므로 증명이 끝난다.  

그렇지 않고 어떠한 $\alpha_i\neq 0$이 존재한다면, 우리는 위와 같은 과정을 반복하여 다시 새로운 basis $\\{x_2,x_1,y_1,y_2,\ldots,y_{n-2}\\}$를 얻는다.

이 과정을 반복하다보면 두 가지의 가능성이 있다. 

1. 만일 이 과정이 어디에선가 멈춘다면, 

    $$\beta_kx_k+\beta_{k-1}x_{k-1}+\cdots+\beta_1x_1=0$$
    
    이 될 것이므로 $\\{x_1,x_2,\ldots,x_m\\}$은 일차종속이다. 
2. 그렇지 않다면, $n$번을 반복한 후 우리는 원래의 basis $\\{y_1,y_2,\ldots, y_n\\}$을 새로운 basis $\\{x_1, x_2, \ldots, x_n\\}$으로 완전하게 교체할 것이다. 이 경우, $x_{n+1}\in V$는 $\\{x_1, x_2, \ldots, x_n\\}$들의 일차결합으로 표현할 수 있으므로 $\\{x_1,x_2,\ldots, x_{n+1}\\}$은 일차종속이고 따라서 $\\{x_1,x_2,\ldots, x_m\\}$ 또한 마찬가지이다. 

어떠한 경우든 $\\{x_1,x_2,\ldots, x_m\\}$는 일차종속이고, 따라서 basis가 될 수 없으므로 모순.

</details>

사실 위 명제의 증명은 원래의 명제보다 약간 더 강력한 다음의 명제

> 어떤 $\mathbb{k}$-벡터공간 $V$기 유한한 basis $\mathcal{B}$를 갖는다 하자. 그럼 $\mathcal{B}$보다 원소의 개수가 많은 $V$의 부분집합은 반드시 일차종속이다.

를 증명한 것이다. 어쨌든 [정리 1](#thm1)에 의해 $V$의 basis는 모두 같은 크기를 가지므로 다음 정의가 말이 된다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> $\mathbb{k}$-벡터공간 $V$에 대하여, $V$의 basis의 cardinality를 $V$의 *차원*이라 하고, $\dim V$, 혹은 $\mathbb{k}$를 강조할 필요가 있을 때는 $\dim_FV$로 적는다. 만일 $\dim V$가 유한이라면, $V$는 *유한차원* 벡터공간이고, 그렇지 않다면 $V$는 *무한차원* 벡터공간이다.

</div>

<div class="example" markdown="1">

<ins id="ex4">**예시 4**</ins> 

1. Trivial vector space $\\{0\\}$의 basis는 $\emptyset$이므로, 이 공간의 차원은 $\lvert\emptyset\rvert=0$이다.
2. 임의의 field $\mathbb{k}$에 대하여, $\mathbb{k}$ 자기 자신은 1차원 $\mathbb{k}$-벡터공간이다.
3. 임의의 field $\mathbb{k}$에 대하여, 유클리드 $n$-공간 $F^n$의 차원은 $\dim F^n=n$이다.
4. $\dim_\mathbb{R}\mathbb{C}=2$. 
5. $F[\x]$는 무한차원 벡터공간이다.

</div>

앞으로 우리가 다룰 벡터공간은 항상 유한차원임을 전제한다. 
{: .remark}

때에 따라 유한차원 벡터공간에서의 결과가 무한차원에서 성립하는 경우도 있고, 그렇지 않은 경우도 있다. 예를 들어, 다음의 명제는 무한차원인 경우로 확장할 수 있지만 이 글에서는 유한차원인 경우만 한정해서 생각하기로 한다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> $\mathbb{k}$-벡터공간 $V$와 $V$의 임의의 일차독립인 부분집합 $S$에 대하여, $S$를 포함하는 $V$의 basis $\mathcal{B}$가 존재한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

만약 $\langle S\rangle=V$라면, 더 이상 증명할 것이 없다. 그렇지 않다면 $v\not\in\langle S\rangle$인 $v\in V$가 존재한다. 이제 집합 $S_1=S\cup\\{v\\}$이라 하자. 그럼 $S_1$은 일차독립이다. 자명하게 $v\neq0$이며, 이제 $S_1$의 임의의 일차결합 

$$\sum_{x\in S_1} \alpha_xx=\sum_{x\in S}\alpha_xx+\alpha_vv=0$$  

이라 하면, $\alpha_v\neq 0$일 경우 $\alpha_vv$를 이항한 후 $-\alpha_v^{-1}$를 곱해주면 $v$를 $S$의 원소들의 일차결합으로 나타낼 수 있는데, 이는 $v$의 선택에 모순이기 때문이다. 따라서 $\alpha_v=0$이고, 그럼 $S$의 각 원소들은 일차독립이므로 $\alpha_x=0$이 모든 $x\in S$에 대해 성립한다. 따라서, $\alpha_x=0$이 모든 $x\in S_1$에 대해 성립한다.

이제 만일 $\langle S\rangle_1=V$라면 다시 증명 끝이고, 그렇지 않다면 똑같은 방식으로 $S_2=S_1\cup\\{v'\\}$을 정의하여 반복할 수 있다. 물론 $S_2$가 일차독립이라는 것을 보여야 하지만, $v'$를 $V\setminus\langle S\rangle_1$에서 뽑아왔기 때문에 이는 위에서 보인 것과 정확하게 같은 논리로 가능하다. 

이 과정은 앞선 [보조정리3](#lem3)에 의해 많아야 $\dim V$번째 과정 안에 끝나며, 이 과정이 끝날 때 우리는 원하는 basis $S_n$을 얻게 된다.

</details>

$V$의 basis는 일차독립인 동시에 $V$를 span하는 집합이다. 위의 명제는 일차독립인 집합에 적절하게 벡터를 추가하여 $V$를 span하도록 할 수 있다는 것을 말한다. 반대로 $V$를 span하는 집합이 있다면, 이들 중 겹치는 일부를 적절하게 빼서 일차독립 조건도 만족하도록 할 수 있다. 이 명제의 증명의 기본 아이디어는 [명제 5](#prop5)과 동일하지만, $S$는 무한집합일 수 있으므로 $S$에서 원소를 하나하나 빼가는 것으로는 증명이 성립하지 않는다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> $\mathbb{k}$-벡터공간 $V$와, $V$를 span하는 부분집합 $S$에 대하여, $S$의 어떤 부분집합은 $V$의 basis가 된다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$S_0=\emptyset$이라 하자. 그럼 $\langle S\rangle_0=\\{0\\}$이다. 이제 $S\setminus\langle S\rangle_0$의 원소 $x_1$을 택해 $S_1=\\{x_1\\}=S_0\cup\\{x_1\\}$이라 하고, 비슷하게 $S\setminus\langle S\rangle_1$의 원소 $x_2$를 택해 $S_2=\\{x_1,x_2\\}=S_1\cup \\{x_2\\}$를 만드는 과정을 반복한다.

이렇게 얻어진 집합 $S_i$들은 정의에 의해 일차독립인 부분집합이 되며, $\langle S\rangle_i$가 $S$와 같지 않은 한 $S_{i+1}$의 원소의 개수는 $S_i$보다 항상 하나 더 많다. 따라서 모든 $i < n = \dim V$에 대하여 $S\setminus\langle S\rangle_i$가 공집합이 아니라는 것을 보이면 충분하다. 

자연수 $m$을 $S\setminus\langle S\rangle_m=\emptyset$이도록 택하자. 즉 $S\subseteq\langle S\rangle_m$이다. 이제 [§벡터공간의 기저, ⁋보조정리 4](/ko/math/basic_linear_algebra/basis#lem4)로부터 $\span$을 취하는 것은 집합 사이의 포함관계를 유지한다는 것을 알 수 있으므로

$$\langle S\rangle\subseteq\span\bigl(\langle S\rangle_m\bigr)$$

이고, 우변의 $\langle S\rangle_m$은 이미 $V$의 부분공간이므로 [§벡터공간의 기저, ⁋보조정리 3](/ko/math/basic_linear_algebra/basis#lem3)으로부터 $\span\bigl(\langle S\rangle\bigr)=\langle S\rangle_m$임을 안다. 따라서

$$V=\langle S\rangle\subseteq\span\bigl(\langle S\rangle_m\bigr)=\langle S\rangle_m$$

으로부터 $\langle S\rangle_m=V$임을 안다. 

</details>

마지막으로 두 개의 조금 일반적인 예시를 살펴보자.

<div class="example" markdown="1">

<ins id="ex7">**예시 7**</ins> 두 $\mathbb{k}$-벡터공간 $V$, $W$가 주어졌다 하자. 그럼 이들의 *곱* $V\times W$는 임의의 $v\in V$, $w\in W$에 대하여 $(v,w)$의 꼴로 나타나는 벡터들의 벡터공간이다. 이들의 연산은 각각

$$(v_1, w_1)+(v_2,w_2)=(v_1+v_2,w_1+w_2),\quad\alpha(v,w)=(\alpha v,\alpha w)$$

으로 주어진다. 어렵지 않게, 만일 $\mathcal{B}_1$, $\mathcal{B}_2$가 각각 $V$, $W$의 basis들이라면, $V\times W$의 부분집합

$$\mathcal{B}=\{(x, y)\mid x\in \mathcal{B}_1\text{ and }y\in \mathcal{B}_2\}$$

이 $V\times W$의 basis가 되는 것을 확인할 수 있다. 특히, 만일 $V$, $W$가 모두 유한차원이라면 $V\times W$도 그러하고 $\dim(V\times W)$는 $(\dim V)+(\dim W)$와 같게 된다.

</div>

<div class="example" markdown="1">

<ins id="ex8">**예시 8**</ins> 이번에는 $\mathbb{k}$-벡터공간 $V$가 주어졌다 하고, $V$의 두 부분공간 $W_1$, $W_2$가 주어졌다 하자. 그럼 $V$의 부분공간 $W_1+W_2$는 

> 두 부분공간 $W_1$, $W_2$를 포함하는 $V$의 부분공간 중 가장 작은 것

으로 정의된다. 식으로 쓰자면 $W_1+W_2=\span(W_1\cup W_2)$라 할 수 있다. 

이제 $W_1,W_2$가 모두 유한차원이라 가정하면

$$\dim(W_1+W_2)=\dim W_1+\dim W_2-\dim(W_1\cap W_2)$$

이 성립한다.

<details class="proof" markdown="1">
<summary>증명</summary>

$W_1,W_2$이 각각 $m$, $n$차원이라 하고, $W_1\cap W_2$가 $k$차원이라 하자. 그럼 $W_1\cap W_2$의 basis $\mathcal{B}\_0=\\{x_1,\ldots, x_k\\}$가 존재한다. 이 집합은 $W_1$과 $W_2$의 일차독립인 부분집합이므로, 이 집합을 포함하는 $W_1$과 $W_2$의 basis가 각각 존재한다. 이들을 $\mathcal{B}\_1$과 $\mathcal{B}\_2$라 하자. 그럼 

$$\mathcal{B}_1=\{y_1,\ldots, y_m\},\quad \mathcal{B}_2=\{z_1,\ldots, z_n\},\qquad y_1=z_1=x_1,\ldots, y_k=z_k=x_k$$

라 할 수 있다. 이제 다음의 집합 

$$\mathcal{B}_1\cup\mathcal{B}_2=\{x_1=y_1,\ldots, x_k=y_k, \quad y_{k+1}, \ldots, y_m,\quad z_{k+1},\ldots, z_n\}$$

은 $W_1+W_2$를 span한다. 뿐만 아니라 이 집합은 일차독립이다. 이를 보이기 위해

$$\alpha_1x_1+\cdots+\alpha_kx_k+\beta_{k+1}y_{k+1}+\cdots+\beta_{m}y_m+\gamma_{k+1}z_{k+1}+\cdots+\gamma_{n}z_n=0\tag{2}$$

이라 하자. $\alpha_i=\beta_i+\gamma_i$를 만족하는 임의의 스칼라들 $\beta_i$, $\gamma_i$ ($i\leq k$)들에 대하여, 

$$\beta_1y_1+\cdots+\beta_ky_k+\beta_{k+1}y_{k+1}+\cdots+\beta_{m}y_m=-\gamma_1z_1-\cdots-\gamma_kz_k-\gamma_{k+1}z_{k+1}-\cdots-\gamma_{n}z_n$$

으로 적으면 좌변은 $W_1$의 원소, 우변은 $W_2$의 원소이므로 이 공통의 벡터는 $W_1\cap W_2$의 원소이다. $\mathcal{B}\_0$이 $W_1\cap W_2$의 basis이므로, 적당한 스칼라들 $\alpha_i'$들을 다시 잡아

$$\beta_1y_1+\cdots+\beta_my_m=\alpha_1'x_1+\cdots+\alpha_k'x_k=-\gamma_1z_1-\cdots-\gamma_nz_n$$

로 적을 수 있다. 그런데 첫째 등식의 경우, $\alpha_i'x_i$들을 다시 좌변으로 넘겨서 $\beta_iy_i$들과 합쳐주면

$$(\beta_1-\alpha_1')y_1+\cdots+(\beta_k-\alpha_k')y_k+\beta_{k+1}y_{k+1}+\cdots+\beta_my_m=0$$

이 되므로, $\mathcal{B}\_1$의 일차독립성에 의해 계수들이 모두 0이고, 특히 $\beta_{k+1}=\cdots=\beta_m=0$이다. 마찬가지로 둘째 등식에서 $\gamma_{k+1}=\cdots=\gamma_n=0$이고, 그럼 (2)에서 남는 식은 $\alpha_1x_1+\cdots+\alpha_kx_k=0$뿐인데 $x_1,\ldots,x_k$는 $W_1\cap W_2$의 basis이므로 다시 일차독립성에 의해 이들도 모두 0이다. 즉, $\mathcal{B}\_1\cup\mathcal{B}\_2$는 $W_1+W_2$를 span하는 일차독립인 부분집합이고 따라서 $W_1+W_2$의 basis이다. 이제

$$\dim(W_1+W_2)=\lvert\mathcal{B}_1\cup\mathcal{B}_2\rvert=\lvert\mathcal{B}_1\rvert+\lvert\mathcal{B}_2\rvert-\lvert\mathcal{B}_0\rvert=\dim W_1+\dim W_2-\dim(W_1\cap W_2).$$

</details>

</div>

---

**참고문헌**

**[Goc]** M.S. Gockenbach, *Finite-dimensional linear algebra*, Discrete Mathematics and its applications, Taylor&Francis, 2011.

---