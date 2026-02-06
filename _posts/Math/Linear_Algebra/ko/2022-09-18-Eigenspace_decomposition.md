---

title: "고유공간분해"
excerpt: "벡터공간의 고유공간분해"

categories: [Math / Linear Algebra]
permalink: /ko/math/linear_algebra/eigenspace_decomposition
sidebar: 
    nav: "linear_algebra-ko"

header:
    overlay_image: /assets/images/Math/Linear_Algebra/Eigenspace_decomposition.png
    overlay_filter: 0.5

date: 2022-09-18
last_modified_at: 2022-09-18

weight: 16

---

## 공간의 직합

$n\times n$ 행렬 $A$와, 한 고윳값 $\lambda$를 생각하자. 정의에 의해 $\lambda$에 해당하는 고유공간 $E_\lambda$의 임의의 벡터 $v$는 반드시 다음의 식

$$Av=\lambda v$$

을 만족한다. 따라서, $E_\lambda$로 제한했을 때 $A$는 아주 다루기 쉬운 대상인 $v\mapsto \lambda v$가 된다. 

더 일반적으로, $A$를 $\mathbb{K}^n$에서 $\mathbb{K}^n$으로의 linear map으로 생각하고, 정의역 $\mathbb{K}^n$을 고유공간 $E_\lambda$들로 덮을 수 있다 가정하자. 즉

$$\mathbb{K}^n=\span\left(\bigcup_{\lambda\in\sigma(A)}E_\lambda\right)$$

이라 하자. 그럼 임의의 $v\in\mathbb{K}^n$에 대하여, $v_\lambda\in E_\lambda$들이 각각 존재하여

$$v=\sum_{\lambda\in\sigma(A)}v_\lambda$$

이라 쓸 수 있으며, 따라서 

$$Av=A\left(\sum_{\lambda\in\sigma(A)}v_\lambda\right)=\sum_{\lambda\in\sigma(A)}Av_\lambda$$

이고, 위의 논증에 의하여 $Av_\lambda=\lambda v_\lambda$이므로 다음의 식

$$Av=\sum_{\lambda\in\sigma(A)}\lambda v_\lambda$$

을 얻는다. 물론 위의 계산이 말이 되기 위해서는 $v$를 $v_\lambda$들의 합으로 나타내는 방법이 유일해야 한다. 이를 다음과 같이 정의한다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 임의의 $\mathbb{K}$-벡터공간 $V$가 그 부분공간 $(W\_i)\_{i\in I}$들의 *direct sum<sub>직합</sub>*이라는 것은, 임의의 $v\in V$가 주어질 때마다 적당한 $(v\_i)\_{i\in I}$가 <em_ko>유일하게</em_ko> 존재하여 

$$v=\sum_{i\in I} v_i$$

이 성립하는 것이다.[^1] 이를 $V=\bigoplus\_{i\in I}W_i$와 같이 적는다. 

</div>

자명하지 않은 경우 중 가장 쉬운 것은 $I$가 원소 두 개짜리 집합일 때이다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> $\mathbb{K}$-벡터공간 $V$의 두 부분공간 $W_1,W_2$에 대하여, $V=W_1\oplus W_2$인 것은 $V=W_1+W_2$이고 $W_1\cap W_2=\\{0\\}$인 것과 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $V=W_1\oplus W_2$라 가정하자. 정의에 의해 $W_1+W_2\subseteq V$인 것은 자명하다. 거꾸로 임의의 $v\in V$를 택하면, $v=w_1+w_2$이도록 하는 $w_i\in W_i$가 존재하므로 $V\subseteq W_1+W_2$ 또한 성립한다. 이로부터 $V=W_1+W_2$임을 안다. 한편, 만일 $W_1\cap W_2\neq \\{0\\}$이라면, 영이 아닌 $w\in W_1+W_2$에 대하여

$$w=0+w=w+0$$

이므로 [정의 1](#def1)에서의 유일성에 모순이 된다. 

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

또 다른 예시로, $V$의 basis $\mathcal{B}=\\{x_1,\ldots, x_n\\}$을 하나 택하자. $W_i=\mathbb{K}x_i$이라 하면, $\mathcal{B}$가 basis라는 조건은 정확하게 $V$가 $W_i$들의 direct sum이라는 조건과 일치하게 된다. 더 일반적으로 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> 임의의 $\mathbb{K}$-벡터공간 $V$와, 부분공간 $(W\_i)\_{i\in I}$에 대하여 $V=\bigoplus\_{i\in I} W\_i$인 것은 $W_i$의 basis $\mathcal{B}\_i$들이 $i\neq j$일 때마다 $\mathcal{B}\_i\cap\mathcal{B}\_j=\emptyset$을 만족하고, $\bigcup\_{i\in I}\mathcal{B}\_i$가 $V$의 basis가 되는 것과 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $V=\bigoplus W\_i$라 가정하고, $W\_i$들의 basis $\mathcal{B}\_i$를 택하자. 만일 $\mathcal{B}\_i\cap\mathcal{B}\_j\neq\emptyset$이라면 $W\_i\cap W\_j\neq\emptyset$가 되어 [명제 2](#prop2) 이후의 논의에 모순이므로, 반드시 $\mathcal{B}\_i\cap\mathcal{B}\_j=\emptyset$이어야 한다. 임의의 $v\in V$에 대하여, $V=\bigoplus W\_i$로부터 다음의 식

$$v=\sum\_{i\in I} w\_i$$

을 만족하는 $w\_i$들이 유일하게 존재한다. 또, $W\_i$들 각각에서 $w\_i$들을 $\mathcal{B}\_i$의 원소들의 일차결합으로 유일하게 표현할 수 있다. 이로부터 $\bigcup\mathcal{B}\_i$가 $V$의 basis가 된다는 것을 알 수 있다.

이 논증을 거꾸로 뒤집으면 반대방향 또한 보일 수 있다.

</details>

따라서 $\dim V=\sum\_{i\in I}\dim W\_i$임을 알 수 있다. 

## 대각화

이제 $\mathbb{K}^n$을 고유공간으로 분해하는 법을 살펴본다. 앞선 [명제 3](#prop3)으로부터 벡터공간 $\mathbb{K}^n$을 고유공간들 $E\_\lambda$로 분해하는 것은 $E\_\lambda$의 basis들을 모아서 $\mathbb{K}^n$의 basis를 나타내는 것과 같다는 것을 안다. 또, 영이 아닌 벡터 $x\_1$이 고윳값 $\lambda\_1$에 대응되는 고유벡터라 하면, 또 다른 고윳값 $\lambda\_2$에 대하여

$$Ax_1=\lambda_1x_1\neq\lambda_2 x_1$$

이므로 $x\_1\not\in E\_{\lambda\_2}$임을 안다. 따라서 $E\_\lambda$들의 basis를 어떻게 잡더라도, 서로 다른 $\lambda\_1,\lambda\_2$에 대하여 $E\_{\lambda\_1}, E\_{\lambda\_2}$의 basis가 겹치는 일은 없다. 뿐만 아니라 다음이 성립한다. 

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> 임의의 행렬 $A$에 대하여, $x\_1,\ldots, x\_m$들이 각각 서로 다른 고윳값들 $\lambda\_1,\ldots,\lambda\_m$들에 대응되는 고유벡터들이라 하자. 그럼 집합 $\\{x\_1,\ldots,x\_m\\}$은 일차독립이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

결론을 부정하여 집합 $\\{x\_1,x\_2,\ldots, x\_m\\}$이 일차종속이라 하자. 즉, 다음의 식


$$\alpha_1x_1+\alpha_2x_2+\cdots+\alpha_mx_m=0\tag{1}$$

을 만족하며 모두 영은 아닌 스칼라들 $\alpha\_i$들이 존재한다. 이제 이를 만족하는 $(\alpha\_i)\_{1\leq i\leq m}$들 중, $\supp(\alpha\_i)$가 가장 작도록 하는 모임을 골라 이를 $(\beta\_i)\_{1\leq i\leq m}$라 하자. 즉, 만일 $\beta\_i\neq0$을 만족하는 $i$의 갯수가 $k$개라면, $k$개 미만의 $i$에 대하여 $\alpha\_i\neq 0$을 만족하는 $(\alpha\_i)\_{1\leq i\leq m}$은 위의 식 (1)을 만족하지 않는다.

이제 적어도 2개의 $\beta\_i$에 대하여 $\beta\_i\neq 0$이므로, 일반성을 잃지 않고 $\beta\_m\neq 0$이라 하자. 그럼

$$x_m=\sum_{i=1}^{m-1}\left(-\frac{\beta_i}{\beta_m}\right)x_i$$

이다. 편의상 이를 $x\_m=\sum\_{i=1}^{m-1}\beta'\_ix\_i$라 하자. 양 변에 $A$를 곱하면

$$Ax_m=\sum_{i=1}^{m-1}\beta'_i(Ax_i)$$

이고, $x\_m$들은 고유벡터들이므로

$$\lambda_mx_m=\sum_{i=1}^{m-1}\beta'_i\lambda_i x_i$$

이다. 그런데 $x\_m=\sum\_{i=1}^{m-1}\beta'\_ix\_i$의 양변에 $\lambda\_m$을 곱하면

$$\lambda_mx_m=\sum_{i=1}^{m-1}\beta_i'\lambda_mx_i$$

이므로, 이를 앞서서 얻은 식과 연립하면

$$0=\sum_{i=1}^{m-1}\beta_i'(\lambda_i-\lambda_m)x_i$$

이고, $\beta\_i'=-(\beta\_i/\beta\_m)$이므로 양 변에 $\beta\_m$을 곱해 위의 식을 정리하면

$$0=\sum_{i=1}^{m-1}\beta_i(\lambda_i-\lambda_m)x_i$$

이다. 만일 $(\beta''\_i)\_{1\leq i\leq n}$을 다음의 식

$$\beta_i''=\begin{cases}\beta_i(\lambda_i-\lambda_m)&1\leq i\leq m-1\\0&i=m\end{cases}$$

으로 정의하면 위의 식은 

$$\beta_1''x_1+\beta_2''x_2+\cdots+\beta_m''x_m=0$$

이 된다. 가정에 의해 $\lambda_i-\lambda_m\neq 0$이므로, $1\leq i\leq m-1$에 대해서는 $\beta_i''=0$인 것과 $\beta_i=0$인 것이 동치이다. 따라서 $\beta_i''\neq 0$을 만족하는 $1\leq i\leq m-1$은 $k-1$개이고, $\beta\_m''=0$이므로 $\supp(\beta\_i'')\_{1\leq i\leq m}$의 크기는 $k-1$이다. 이는 $(\beta\_i)\_{1\leq i\leq m}$의 최소성에 모순이므로, 집합 $\\{x_1,x_2,\ldots, x_m\\}$은 일차독립이다.

</details>

이로부터, 임의의 행렬 $A$와 그 고윳값들 $\lambda\in\sigma(A)$, 이에 대응되는 고유공간들을 $E\_\lambda$, 그리고 이들의 basis를 $\mathcal{B}\_\lambda$라 한다면 $\mathcal{B}=\bigcup\_{\lambda\in\sigma(A)}\mathcal{B}\_\lambda$가 $\mathbb{K}^n$의 일차독립인 부분집합이 된다는 것을 안다. 그러나 일반적으로 $\mathcal{B}$가 $\mathbb{K}^n$의 basis가 될 이유는 없다. 가령 [§특성다항식, ⁋예시 7](/ko/math/linear_algebra/characteristic_polynomial#ex7)을 보면, $\mathbb{K}=\mathbb{R}$에서 $\sigma(J)=\emptyset$이므로 $\mathcal{B}=\emptyset$이다. 뿐만 아니라 $A$의 특성다항식이 정확히 $n$개의 해를 갖는다고 가정해도 비슷한 문제가 생길 수 있는데, 가령 다음의 행렬

$$A=\begin{pmatrix}1&1&1\\0&1&1\\0&0&1\end{pmatrix}$$

의 특성다항식은 $(\mathbf{x}-1)^3=0$이지만, 고윳값 $1$에 해당하는 고유벡터는 오직 $(1,0,0)$ 뿐임을 알 수 있다. 이를 이전 글에서 도입한 언어로 바꾸어 쓰자면, 고윳값 $1$의 대수적 중복도는 $3$이고, 기하적 중복도는 $1$이라 할 수 있다. 

다음 명제는 <em_ko>항상</em_ko> 행렬의 고윳값의 기하적 중복도는 대수적 중복도를 넘을 수 없음을 보여준다. 

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> $n\times n$ 행렬 $A$의 고윳값 $\lambda\in\mathbb{K}$에 대하여, $\lambda$의 기하적 중복도는 항상 $\lambda$의 대수적 중복도를 넘지 못한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$\lambda$의 기하적 중복도가 $k$라 하고, $E_\lambda(A)$를 span하는 $k$개의 일차독립인 벡터들 $x_1,\ldots, x_k$를 생각하자. 여기에 $(n-k)$개의 벡터 $x_{k+1},\ldots, x_k$를 추가하여 $\mathbb{K}^n$의 새로운 basis $\\{x_1,\ldots, x_n\\}$을 만들 수 있다. 이제 행렬 $X$를

$$X=(x_1|x_2|\cdots|x_n)$$

으로 정의한다면, $X$의 열들이 일차독립이므로 $X^{-1}$이 존재한다. $X^{-1}$의 각 row들을 $y_i$라 하자. 식 $X^{-1}X=XX^{-1}=I$에서

$$y_i\cdot x_j=\begin{cases}1&i=j\\ 0&i\neq j\end{cases}$$

이 성립한다. 따라서 $A'=X^{-1}AX$라 한다면 

$$\begin{aligned}A'&=X^{-1}(AX)=\begin{pmatrix}y_1\\ y_2\\ \vdots\\ y_n\end{pmatrix}(Ax_1|Ax_2|\cdots|Ax_n)\\
&=\begin{pmatrix}y_1\cdot Ax_1&y_1\cdot Ax_2&\cdots& y_1\cdot Ax_k&\cdots&y_1\cdot Ax_n\\ y_2\cdot Ax_1&y_2\cdot Ax_2&\cdots &y_2\cdot Ax_k&\cdots &y_2\cdot Ax_n\\ \vdots&\vdots&\ddots&\vdots&\ddots&\vdots\\ y_k\cdot Ax_1&y_k\cdot Ax_2&\cdots&y_k\cdot Ax_k&\cdots&y_k\cdot Ax_n\\ \vdots&\vdots&\ddots&\vdots&\ddots&\vdots\\ y_n\cdot Ax_1&y_n\cdot Ax_2&\cdots &y_n\cdot Ax_k&\cdots&y_n\cdot Ax_n \end{pmatrix}\\
&=\begin{pmatrix}y_1\cdot (\lambda x_1)&y_1\cdot (\lambda x_2)&\cdots& y_1\cdot (\lambda x_k)&\cdots&y_1\cdot Ax_n\\ y_2\cdot (\lambda x_1)&y_2\cdot (\lambda x_2)&\cdots &y_2\cdot (\lambda x_k)&\cdots &y_2\cdot Ax_n\\ \vdots&\vdots&\ddots&\vdots&\ddots&\vdots\\ y_k\cdot (\lambda x_1)&y_k\cdot (\lambda x_2)&\cdots&y_k\cdot (\lambda x_k)&\cdots&y_k\cdot Ax_n\\ \vdots&\vdots&\ddots&\vdots&\ddots&\vdots\\ y_n\cdot (\lambda x_1)&y_n\cdot (\lambda x_2)&\cdots &y_n\cdot (\lambda x_k)&\cdots&y_n\cdot Ax_n \end{pmatrix}\\
&=\begin{pmatrix}\lambda&0&\cdots& 0&\cdots&y_1\cdot Ax_n\\ 0&\lambda&\cdots &0&\cdots &y_2\cdot Ax_n\\ \vdots&\vdots&\ddots&\vdots&\ddots&\vdots\\ 0&0&\cdots&\lambda&\cdots&y_k\cdot Ax_n\\ \vdots&\vdots&\ddots&\vdots&\ddots&\vdots\\ 0&0&\cdots &0&\cdots&y_n\cdot Ax_n \end{pmatrix}\\
&=\begin{pmatrix}\lambda I_k&B\\ 0&C\end{pmatrix}\end{aligned}$$

이 된다. 따라서 $A$의 특성다항식을 $p_A(\mathbf{x})$라 적으면, [§특성다항식, ⁋정리 4](/ko/math/linear_algebra/characteristic_polynomial#cor4)으로부터 $p_A(\mathbf{x})=p_{A'}(\mathbf{x})$이고 따라서

$$p_A(\mathbf{x}=p_{A'}(\mathbf{x})=\det(\mathbf{x}I-A')=(\mathbf{x}-\lambda)^k\det(\mathbf{x}I_{n-k}-C)$$

임을 안다. 즉, $p_A$에서 $\lambda$의 대수적 중복도는 최소 $k$이다. 

</details>

$n\times n$ 행렬 $A$가 주어졌다 하고, $A$의 특성다항식을 $p_A$라 하면, 고윳값 $\lambda$들의 대수적 중복도의 합은 $p_A$의 차수인 $n$을 넘지 못한다. 또, 고정된 고윳값 $\lambda$에 대해, 위 명제는 $\lambda$의 기하적 중복도가 대수적 중복도를 넘지 못한다는 것을 보여준다. 마지막으로 [명제 4](#prop4) 이후의 논증으로부터, $\mathbb{K}^n$을 고유공간으로 분해하기 위해서는 $\lambda$들의 기하적 중복도를 모두 합쳤을 때 $n$이 되어야 한다는 사실을 알 수 있다. 이를 모두 정리하면 다음 명제를 얻는다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> 임의의 $n\times n$ 행렬 $A$에 대하여, $\mathbb{K}^n$이 $A$의 고유공간들의 direct sum으로 표현가능할 필요충분조건은 

1. $A$의 특성다항식이 중복도를 고려하였을 때 $n$개의 근을 가지며,
2. 이 때 각각의 고윳값의 기하적 중복도와 대수적 중복도가 같은 것이다.

</div>

특별히 $\mathbb{K}$가 algebraically closed field라면 첫째 조건은 항상 만족되므로, 둘째 조건만 고려하면 된다.

우리는 행렬의 대각화를 다루는 동안에는 field $\mathbb{K}$가 algebraically closed임을 가정한다. 이는 오직 편의를 위한 것으로, 만일 $\mathbb{K}$가 algebraically closed가 아닐 경우, 관심있는 행렬의 특성다항식의 해를 직접 넣어준 field extension을 생각하면 된다. ([\[체론\] §대수적 확장](/ko/math/field_theory/algebraic_extensions)) 이는, 예를 들어 방정식 $\x^2+1=0$의 허근 $i$를 추가하여 $\mathbb{R}$에서 $\mathbb{C}$를 얻어내는 것과 정확히 똑같은 것이다. 

## 행렬의 대각화

우리는 앞서 임의의 $n\times n$ 행렬 $A$가 주어졌을 때, $A$의 고윳값과 고유공간을 통해 $\mathbb{R}^n$을 분해하는 방법을 살펴보았고, [명제 6](#prop6)으로부터 이러한 분해가 언제 가능한지 또한 알게 되었다. 이를 증명하기 위해 사용했던 [명제 5](#prop5)의 증명을 다시 한 번 살펴보자. 우리는 $E_\lambda$의 basis $x_1,\ldots, x_k$에 $n-k$개의 임의의 벡터를 추가한 후, 이를 통해 행렬 $X=(x\_1\|\cdots\|x\_n)$을 정의한 후 계산을 통해

$$XAX^{-1}=\begin{pmatrix}\lambda I_k&B\\0&C\end{pmatrix}$$

의 왼쪽 위 $k\times k$ 블록행렬이 대각행렬 $\lambda I_k$가 된다는 것을 보았다. 그런데 만일 $A$가 [명제 6](#prop6)의 조건을 모두 만족한다면, $n-k$개의 벡터들 $x\_{k+1},\ldots, x_n$을 마구잡이로 추가할 것이 아니라, $n$개의 벡터들 $x_1,\ldots, x_n$이 모두 $A$의 고유공간의 basis가 되도록 잡을 수 있다. 그럼 [명제 5](#prop5)의 증명 중

$$y_i\cdot x_j=\begin{cases}1&i=j\\0&i\neq j\end{cases}$$

으로부터 $C$도 대각행렬이 되고, $B$는 영행렬이 된다는 것을 알 수 있다. 따라서 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> [명제 6](#prop6)의 조건을 모두 만족하는 $n\times n$ 행렬 $A$를 생각하고, 고유공간들의 basis로 이루어진 $\mathbb{R}^n$의 basis를 잡아 이를 $x_1,\ldots, x_n$이라 하자. $Ax_i=\lambda_ix_i$라 하고, $X=(x\_1\|\cdots\|x\_n)$이라 하면, 대각행렬

$$D=\begin{pmatrix}\lambda_1&0&\cdots&0\\ 0&\lambda_2&\cdots&0\\ \vdots&\vdots&\ddots&\vdots\\0&0&\cdots&\lambda_n\end{pmatrix}$$

에 대하여 $A=XDX^{-1}$이 성립한다. 

</div>

따라서 이 조건을 만족하는 행렬 $A$에 그럴듯한 이름을 붙여줄 수 있다.

<div class="definition" markdown="1">

<ins id="def8">**정의 8**</ins> [명제 5](#prop5)의 조건을 모두 만족하는 $n\times n$ 행렬 $A$를 *diagonalizable<sub>대각화가능</sub>*이라 한다.

</div>

혹은, [명제 6](#prop6)은 필요충분조건이었으므로, 대각행렬과 닮은 행렬을 diagonalizable한 행렬이라 불러도 아무런 문제가 없다. 바꾸어 말하자면 임의의 diagonalizable matrix의 eigenvalue에 의해 완전하게 결정된다. 

Diagonalizable matrix들이 개념적으로 중요하다는 것은 위에서 충분히 살펴보았다. 이 뿐만 아니라 diagonalizable matrix들은 계산의 편의성 측면에서도 크게 도움이 된다. 가령 행렬 $A$가 대각화 가능하여 $A=XDX^{-1}$이라면, $A$의 거듭제곱은 $A^k=XD^kX^{-1}$로 주어지며 대각행렬의 거듭제곱은 각 성분의 거듭제곱으로 만들어진 대각행렬에 불과하므로 $A$의 거듭제곱을 계산하는 것은 아주 쉬운 일이 된다. 

더 일반적으로 만일 행렬들 $A_1,\ldots, A_k$가 같은 행렬 $X$를 통해 diagonalizable이라면, 즉 

$$A_i=XD_iX^{-1}$$

라면

$$A_1A_2\cdots A_k =XD_1D_2\cdots D_kX^{-1}$$

이고 대각행렬의 곱은 대각성분들의 곱으로 이루어진 대각행렬에 불과하므로 $A_1A_2\cdots A_k$를 계산하는 것 또한 크게 어렵지 않은 일이 될 수도 있다. 이런 경우를 우리는 다음과 같이 이름붙인다. 

<div class="definition" markdown="1">

<ins id="def9">**정의 9**</ins> 행렬들의 family $\\{A_i\\}$가 *simultaneously diagonalizable<sub>동시대각화가능</sub>*이라는 것은 적당한 invertible matrix $X$가 존재하여 모든 $i$에 대하여 $X^{-1}A_iX$이 대각행렬이도록 할 수 있다는 것이다. 

</div>

만일 두 행렬 $A,B$가 고정된 행렬 $X$를 통해 simultaneously diagonalizable이라면, 다음의 식

$$AB=XD_AX^{-1}XD_BX^{-1}=XD_AD_BX^{-1}=XD_BD_AX^{-1}=BA$$

으로부터 두 행렬 $A, B$는 commute한다는 것을 안다. 다음 명제는 (diagonalizable인 행렬에 대해서는) 그 역 또한 성립함을 보여준다. 

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10**</ins> 두 diagonalizable matrix $A,B$가 조건 $AB=BA$를 만족한다면, $A, B$는 simultaneously diagonalizable이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

본질적으로, 이는 두 행렬 $A,B$가 같은 eigenspace decomposition을 준다는 것을 보이면 충분하다. $A$를 사용한 eigenspace decomposition

$$V=\bigoplus_{\lambda}E_\lambda(A)$$

를 생각하자. 그럼 임의의 $v\in E_\lambda(A)$에 대하여, 다음의 식

$$A(Bv)=ABv=BAv=B(\lambda v)=\lambda(Bv)$$

인 것으로부터 $Bv\in E_\lambda(A)$임을 안다. 이제 $B$를 벡터공간 $E_\lambda(A)$ 위에서의 linear operator로 보면, 원래의 linear operator $B$가 diabonalizable이었으므로 $B$는 $E_\lambda(A)$ 위에서도 diagonalizable이고 따라서 $B$의 eigenvector들로 이루어진 $E_\lambda(A)$의 basis가 존재한다. 이제 $E_\lambda(A)$의 임의의 원소는 $A$의 (eigenvalue $\lambda$에 해당하는) eigenvector들이므로, 이들은 $A$의 eigenvector이기도 하다. 

</details>

## 선형연산자의 고유공간분해

지금까지 우리는 주어진 행렬을 대각화하는 과정을 살펴보았고, 기본적으로 이는 (대각화가능한) 선형연산자가 주어졌을 때 벡터공간을 고유공간들로 분해하는 것과 같다. 이에 대한 증명을 위해 우리는 고유공간의 기저를 적극적으로 활용했다. 이를 기저의 선택없이 설명하는 것은 다음 글에서 다룰 조르당 표준형을 살펴볼 때 도움이 될 것이다. 

유한차원 벡터공간 $V$와 linear operator $L:V\rightarrow V$에 대하여, 우리는 다음의 식

$$\rank L +\nullity L=\dim V$$

이 성립하는 것을 보았다. ([§동형사상, ⁋정리 7](/ko/math/linear_algebra/isomorphic_vector_spaces#thm7)) 여기서 $\rank L=\dim\im L$이고 $\nullity L=\dim\ker L$이다. 그러나 이것이 곧 $V$를 $\im L$과 $\ker L$의 direct sum으로 나타낼 수 있다는 뜻은 아니다. 가령, [명제 4](#def4) 이후에 대각화 불가능한 예시였던 행렬 $A$에 대하여,

$$A-I=\begin{pmatrix}0&1&1\\0&0&1\\0&0&0\end{pmatrix}$$

이 정의하는 operator를 생각하면 $\ker (A-I)\cap \im(A-I)\neq \\{0\\}$이다. 허나 만일 $\ker L\cap \im L=\\{0\\}$이 성립하기만 한다면, [§벡터공간의 차원, ⁋예시 8](/ko/math/linear_algebra/dimension#ex8)과 [명제 2](#prop2)로부터 우리는 반드시 $V=\ker L\oplus \im L$인 것을 안다. 다음 보조정리는 이 조건과 동치인 조건을 준다. 

<div class="proposition" markdown="1">

<ins id="lem10">**보조정리 10**</ins> 위와 같은 상황에서, $\ker L\cap \im L=\\{0\\}$인 것은 $\ker L^2=\ker L$인 것과 동치이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

약간의 생각을 통해, $\ker L^2=\ker L$은 $\ker L^2\subset \ker L$과 동치임을 안다. 따라서 보여야 할 것은 다음의 동치관계

$$\ker L\cap \im L=\{0\}\iff \ker L^2\subset\ker L$$

이다. 

우선 $\ker L\cap \im L=\\{0\\}$이라 하고 $v\in\ker L^2$이라 하자. 그럼 $0=L^2 v=L(Lv)$이므로 $Lv\in\ker L$이고, 따라서 가정에 의해 $Lv=0$이어야 한다. 즉 $v\in\ker L$이다. 거꾸로 $\ker L^2\subset \ker L$라 가정하고 $v\in \ker L\cap \im L$이라 하자. 그럼 $v\in \im L$이므로 $v=Lw$를 만족하는 $w\in V$가 존재한다. 그런데 $v\in\ker L$이기도 하므로,

$$0=Lv=L(Lw)=L^2w\implies w\in\ker(L^2)\subset \ker L$$

이므로 $w\in \ker L$이다. 즉, $v=Lw=0$이다. 

</details>

다시 원래의 이야기로 돌아오면, 우리는 특별히 $L$이 어떠한 linear operator와 그 eigenvalue에 대하여 $A-\lambda I$의 꼴인 경우가 특별히 궁금하다. 다음 명제는 [보조정리 10](#lem10)을 사용하여 diagonalizability를 간결하게 특징짓는다.

<div class="proposition" markdown="1">

<ins id="prop11">**명제 11**</ins> Linear operator $A:V\rightarrow V$가 diagonalizable인 것은 모든 고윳값 $\lambda\in\sigma(A)$에 대하여 

$$\ker(A-\lambda I)^2=\ker(A-\lambda I)$$

인 것과 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $A$가 diagonalizable이라 하자. 그럼 $V=\bigoplus_{\mu\in\sigma(A)} E_\mu(A)$이다. 임의의 $v\in\ker(A-\lambda I)^2$를 취하면, $v=\sum_{\mu\in\sigma(A)}v_\mu$로 유일하게 쓸 수 있고, 

$$(A-\lambda I)^2v=\sum_{\mu\in\sigma(A)}(A-\lambda I)^2v_\mu=\sum_{\mu\in\sigma(A)}(\mu-\lambda)^2v_\mu=0$$

이다. 고유공간 분해의 유일성으로부터 $(\mu-\lambda)^2v_\mu=0$이 모든 $\mu$에 대해 성립해야 하고, $\mu\neq\lambda$일 때는 $v_\mu=0$이므로

$$v=v_\lambda\in E_\lambda(A)=\ker(A-\lambda I)$$

이다.

거꾸로 모든 고윳값 $\lambda$에 대하여 $\ker(A-\lambda I)^2=\ker(A-\lambda I)$라 하자. [보조정리 10](#lem10)으로부터 각 $\lambda$에 대해 

$$\ker(A-\lambda I)\cap\im(A-\lambda I)=\{0\}$$

이고, [§동형사상, ⁋정리 7](/ko/math/linear_algebra/isomorphic_vector_spaces#thm7)에 의하여

$$\dim\ker(A-\lambda I)+\dim\im(A-\lambda I)=\dim V$$

이므로 $V=\ker(A-\lambda I)\oplus\im(A-\lambda I)$이다. 편의를 위해 $\ker(A-\lambda I)=E_\lambda(A)$, $\im (A-\lambda I)=W_\lambda(A)$로 적자. 우리는 우선 임의의 $v\in W_\lambda(A)$에 대하여, $v=(A-\lambda I)w$라 하면

$$Av=A(A-\lambda I)w=(A-\lambda I)Aw\in W_\lambda(A)$$

인 것으로부터 $W_\lambda(A)$는 $A$-invariant subspace임을 안다. 즉

$$A\vert_{W_\lambda(A)}: W_\lambda(A) \rightarrow W_\lambda(A)$$

가 잘 정의된다. 그럼 [명제 4](#prop4)로부터, 만일 $w\in W_\lambda(A)$가 고유값 $\mu$를 갖는 $A\vert_{W_\lambda(A)}$의 고유벡터라면 $w$를 $V$의 원소로 본 것 또한 $A$의 (eigenvalue $\mu$에 해당하는) 고유벡터이며 거꾸로 $A$의 고유값 $\mu\neq \lambda$과 그에 해당하는 고유벡터가 주어진다면 이는 $A\vert_{W_\lambda(A)}$의 고유값--고유벡터 쌍으로 볼 수 있다는 것도 안다. 또, $A\vert_{W_\lambda(A)}$의 임의의 고유값 $\mu$에 대하여, 

$$\ker (A_{W_\lambda(A)}-\mu I)_\ker (A_{W_\lambda(A)}-\mu I)^2$$

도 비슷한 이유로 $W_\lambda(A)$ 위에서 성립하는 것을 안다. 즉, 우리는 이 과정을 귀납적으로 반복할 수 있다. 한편 우리는 $\mathbb{K}$가 algebraically closed임을 가정하고 있으므로 임의의 linear operator $W \rightarrow W$는, $W$가 $0$차원이 아닌 한, 항상 고유값을 가진다는 것을 알고 이로부터 이 귀납법이 <em_ko>정확히</em_ko> $A$의 eigenspace decomposition을 준다는 것을 안다. 

</details>

---

**[Goc]** M.S. Gockenbach, *Finite-dimensional linear algebra*, Discrete Mathematics and its applications, Taylor&Francis, 2011.  
**[Lee]** 이인석, *선형대수와 군*, 서울대학교 출판문화원, 2005.

---

[^1]: 물론, 언제나와 같이 이 합은 사실은 유한합인 것으로 가정한다. 즉 $(v\_i)\_{i\in I}$는 finitely supported인 것으로 가정한다.