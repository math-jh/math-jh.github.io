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

weight: 24

---

## 공간의 직합

$n\times n$ 행렬 $A$와, 한 고윳값 $\lambda$를 생각하자. 정의에 의해 $\lambda$에 해당하는 고유공간 $E_\lambda$의 임의의 벡터 $v$는 반드시 다음의 식

$$Av=\lambda v$$

을 만족한다. 따라서, $E_\lambda$로 제한했을 때 $A$는 아주 다루기 쉬운 대상인 $v\mapsto \lambda v$가 된다. 

더 일반적으로, $A$를 $F^n$에서 $F^n$으로의 linear map으로 생각하고, 정의역 $F^n$을 고유공간 $E_\lambda$들로 덮을 수 있다 가정하자. 즉

$$F^n=\span\left(\bigcup_{\lambda\in\Spec(A)}E_\lambda\right)$$

이라 하자. 그럼 임의의 $v\in F^n$에 대하여, $v_\lambda\in E_\lambda$들이 각각 존재하여

$$v=\sum_{\lambda\in\Spec(A)}v_\lambda$$

이라 쓸 수 있으며, 따라서 

$$Av=A\left(\sum_{\lambda\in\Spec(A)}v_\lambda\right)=\sum_{\lambda\in\Spec(A)}Av_\lambda$$

이고, 위의 논증에 의하여 $Av_\lambda=\lambda v_\lambda$이므로 다음의 식

$$Av=\sum_{\lambda\in\Spec(A)}\lambda v_\lambda$$

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

또 다른 예시로, $V$의 basis $\mathcal{B}=\\{x_1,\ldots, x_n\\}$을 하나 택하자. $W_i=Fx_i$이라 하면, $\mathcal{B}$가 basis라는 조건은 정확하게 $V$가 $W_i$들의 direct sum이라는 조건과 일치하게 된다. 더 일반적으로 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="pp2">**명제 2**</ins> 임의의 $F$-벡터공간 $V$와, 부분공간 $(W\_i)\_{i\in I}$에 대하여 $V=\bigoplus\_{i\in I} W\_i$인 것은 $W_i$의 basis $\mathcal{B}\_i$들이 $i\neq j$일 때마다 $\mathcal{B}\_i\cap\mathcal{B}\_j=\emptyset$을 만족하고, $\bigcup\_{i\in I}\mathcal{B}\_i$가 $V$의 basis가 되는 것과 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $V=\bigoplus W\_i$라 가정하고, $W\_i$들의 basis $\mathcal{B}\_i$를 택하자. 만일 $\mathcal{B}\_i\cap\mathcal{B}\_j\neq\emptyset$이라면 $W\_i\cap W\_j\neq\emptyset$가 되어 [명제 2](#pp2) 이후의 논의에 모순이므로, 반드시 $\mathcal{B}\_i\cap\mathcal{B}\_j=\emptyset$이어야 한다. 임의의 $v\in V$에 대하여, $V=\bigoplus W\_i$로부터 다음의 식

$$v=\sum\_{i\in I} w\_i$$

을 만족하는 $w\_i$들이 유일하게 존재한다. 또, $W\_i$들 각각에서 $w\_i$들을 $\mathcal{B}\_i$의 원소들의 일차결합으로 유일하게 표현할 수 있다. 이로부터 $\bigcup\mathcal{B}\_i$가 $V$의 basis가 된다는 것을 알 수 있다.

이 논증을 거꾸로 뒤집으면 반대방향 또한 보일 수 있다.

</details>

따라서 $\dim V=\sum\_{i\in I}\dim W\_i$임을 알 수 있다. 

## 대각화

이제 $F^n$을 고유공간으로 분해하는 법을 살펴본다. 앞선 [명제 2](#pp2)로부터 벡터공간 $F^n$을 고유공간들 $E\_\lambda$로 분해하는 것은 $E\_\lambda$의 basis들을 모아서 $F^n$의 basis를 나타내는 것과 같다는 것을 안다. 또, 영이 아닌 벡터 $x\_1$이 고윳값 $\lambda\_1$에 대응되는 고유벡터라 하면, 또 다른 고윳값 $\lambda\_2$에 대하여

$$Ax_1=\lambda_1x_1\neq\lambda_2 x_1$$

이므로 $x\_1\not\in E\_{\lambda\_2}$임을 안다. 따라서 $E\_\lambda$들의 basis를 어떻게 잡더라도, 서로 다른 $\lambda\_1,\lambda\_2$에 대하여 $E\_{\lambda\_1}, E\_{\lambda\_2}$의 basis가 겹치는 일은 없다. 뿐만 아니라 다음이 성립한다. 

<div class="proposition" markdown="1">

<ins id="pp3">**명제 3**</ins> 임의의 행렬 $A$에 대하여, $x\_1,\ldots, x\_m$들이 각각 서로 다른 고윳값들 $\lambda\_1,\ldots,\lambda\_m$들에 대응되는 고유벡터들이라 하자. 그럼 집합 $\\{x\_1,\ldots,x\_m\\}$은 일차독립이다. 

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

이로부터, 임의의 행렬 $A$와 그 고윳값들 $\lambda\in\Spec(A)$, 이에 대응되는 고유공간들을 $E\_\lambda$, 그리고 이들의 basis를 $\mathcal{B}\_\lambda$라 한다면 $\mathcal{B}=\bigcup\_{\lambda\in\Spec(A)}\mathcal{B}\_\lambda$가 $F^n$의 일차독립인 부분집합이 된다는 것을 안다. 그러나 일반적으로 $\mathcal{B}$가 $F^n$의 basis가 될 이유는 없다. 가령 [§특성다항식, ⁋예시 7](/ko/math/linear_algebra/characteristic_polynomial#ex7)을 보면, $F=\mathbb{R}$에서 $\Spec(J)=\emptyset$이므로 $\mathcal{B}=\emptyset$이다. 뿐만 아니라 $A$의 특성다항식이 정확히 $n$개의 해를 갖는다고 가정해도 비슷한 문제가 생길 수 있는데, 가령 다음의 행렬

$$A=\begin{pmatrix}1&1&1\\0&1&1\\0&0&1\end{pmatrix}$$

의 특성다항식은 $(\mathbf{x}-1)^3=0$이지만, 고윳값 $1$에 해당하는 고유벡터는 오직 $(1,0,0)$ 뿐임을 알 수 있다. 이를 이전 글에서 도입한 언어로 바꾸어 쓰자면, 고윳값 $1$의 대수적 중복도는 $3$이고, 기하적 중복도는 $1$이라 할 수 있다. 

다음 명제는 <em_ko>항상</em_ko> 행렬의 고윳값의 기하적 중복도는 대수적 중복도를 넘을 수 없음을 보여준다. 

<div class="proposition" markdown="1">

<ins id="pp4">**명제 4**</ins> $n\times n$ 행렬 $A$의 고윳값 $\lambda\in F$에 대하여, $\lambda$의 기하적 중복도는 항상 $\lambda$의 대수적 중복도를 넘지 못한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$\lambda$의 기하적 중복도가 $k$라 하고, $E_\lambda(A)$를 span하는 $k$개의 일차독립인 벡터들 $x_1,\ldots, x_k$를 생각하자. 여기에 $(n-k)$개의 벡터 $x_{k+1},\ldots, x_k$를 추가하여 $F^n$의 새로운 basis $\\{x_1,\ldots, x_n\\}$을 만들 수 있다. 이제 행렬 $X$를

$$X=(x_1|x_2|\cdots|x_n)$$

으로 정의한다면, $X$의 열들이 일차독립이므로 $X^{-1}$이 존재한다. $X^{-1}$의 각 row들을 $y_i$라 하자. 식 $X^{-1}X=XX^{-1}=I$에서

$$y_i\cdot x_j=\begin{cases}1&i=j\\ 0&i\neq j\end{cases}$$

이 성립한다. 따라서 $A'=X^{-1}AX$라 한다면 

$$\begin{aligned}A'&=X^{-1}(AX)=\begin{pmatrix}y_1\\ y_2\\ \vdots\\ y_n\end{pmatrix}(Ax_1|Ax_2|\cdots|Ax_n)\\
&=\begin{pmatrix}y_1\cdot Ax_1&y_1\cdot Ax_2&\cdots& y_1\cdot Ax_k&\cdots&y_1\cdot Ax_n\\ y_2\cdot Ax_1&y_2\cdot Ax_2&\cdots &y_2\cdot Ax_k&\cdots &y_2\cdot Ax_n\\ \vdots&\vdots&\ddots&\vdots&\ddots&\vdots\\ y_k\cdot Ax_1&y_k\cdot Ax_2&\cdots&y_k\cdot Ax_k&\cdots&y_k\cdot Ax_n\\ \vdots&\vdots&\ddots&\vdots&\ddots&\vdots\\ y_n\cdot Ax_1&y_n\cdot Ax_2&\cdots &y_n\cdot Ax_k&\cdots&y_n\cdot Ax_n \end{pmatrix}\\
&=\begin{pmatrix}y_1\cdot (\lambda x_1)&y_1\cdot (\lambda x_2)&\cdots& y_1\cdot (\lambda x_k)&\cdots&y_1\cdot Ax_n\\ y_2\cdot (\lambda x_1)&y_2\cdot (\lambda x_2)&\cdots &y_2\cdot (\lambda x_k)&\cdots &y_2\cdot Ax_n\\ \vdots&\vdots&\ddots&\vdots&\ddots&\vdots\\ y_k\cdot (\lambda x_1)&y_k\cdot (\lambda x_2)&\cdots&y_k\cdot (\lambda x_k)&\cdots&y_k\cdot Ax_n\\ \vdots&\vdots&\ddots&\vdots&\ddots&\vdots\\ y_n\cdot (\lambda x_1)&y_n\cdot (\lambda x_2)&\cdots &y_n\cdot (\lambda x_k)&\cdots&y_n\cdot Ax_n \end{pmatrix}\\
&=\begin{pmatrix}\lambda&0&\cdots& 0&\cdots&y_1\cdot Ax_n\\ 0&\lambda&\cdots &0&\cdots &y_2\cdot Ax_n\\ \vdots&\vdots&\ddots&\vdots&\ddots&\vdots\\ 0&0&\cdots&\lambda&\cdots&y_k\cdot Ax_n\\ \vdots&\vdots&\ddots&\vdots&\ddots&\vdots\\ 0&0&\cdots &0&\cdots&y_n\cdot Ax_n \end{pmatrix}\\
&=\begin{pmatrix}\lambda I_k&B\\ 0&C\end{pmatrix}\end{aligned}$$

이 된다. 따라서 $A$의 특성다항식을 $p_A(\mathbf{x})$라 적으면, 이전 글의 [정의 3]() 다음의 논증으로부터 $p_A(\mathbf{x})=p_{A'}(\mathbf{x})$이고 따라서

$$p_A(\mathbf{x}=p_{A'}(\mathbf{x})=\det(\mathbf{x}I-A')=(\mathbf{x}-\lambda)^k\det(\mathbf{x}I_{n-k}-C)$$

임을 안다. 즉, $p_A$에서 $\lambda$의 대수적 중복도는 최소 $k$이다. 

</details>

$n\times n$ 행렬 $A$가 주어졌다 하고, $A$의 특성다항식을 $p_A$라 하면, 고윳값 $\lambda$들의 대수적 중복도의 합은 $p_A$의 차수인 $n$을 넘지 못한다. 또, 고정된 고윳값 $\lambda$에 대해, 위 명제는 $\lambda$의 기하적 중복도가 대수적 중복도를 넘지 못한다는 것을 보여준다. 마지막으로 [명제 3](#pp3) 이후의 논증으로부터, $F^n$을 고유공간으로 분해하기 위해서는 $\lambda$들의 기하적 중복도를 모두 합쳤을 때 $n$이 되어야 한다는 사실을 알 수 있다. 이를 모두 정리하면 다음 명제를 얻는다.

<div class="proposition" markdown="1">

<ins id="pp5">**명제 5**</ins> 임의의 $n\times n$ 행렬 $A$에 대하여, $F^n$이 $A$의 고유공간들의 direct sum으로 표현가능할 필요충분조건은 

1. $A$의 특성다항식이 중복도를 고려하였을 때 $n$개의 근을 가지며,
2. 이 때 각각의 고윳값의 기하적 중복도와 대수적 중복도가 같은 것이다.

</div>

특별히 $F$가 algebraically closed field라면 첫째 조건은 항상 만족되므로, 둘째 조건만 고려하면 된다.



[^1]: 물론, 언제나와 같이 이 합은 사실은 유한합인 것으로 가정한다. 즉 $(v\_i)\_{i\in I}$는 finitely supported인 것으로 가정한다.

---

**[Goc]** M.S. Gockenbach, *Finite-dimensional linear algebra*, Discrete Mathematics and its applications, Taylor&Francis, 2011.  
**[Lee]** 이인석, *선형대수와 군*, 서울대학교 출판문화원, 2005.

---