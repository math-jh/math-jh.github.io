---

title: "내적공간"
excerpt: "실수집합 위에서 정의된 내적의 성질"

categories: [Math / Linear Algebra]
permalink: /ko/math/linear_algebra/inner_product_space
sidebar: 
    nav: "linear_algebra-ko"

header:
    overlay_image: /assets/images/Math/Linear_Algebra/Inner_product_space.png
    overlay_filter: 0.5

date: 2022-10-02
last_modified_at: 2022-10-02

weight: 17

---

## 내적과 노름

이제 우리는 더 특수한 경우를 생각한다. 

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> $\mathbb{R}$-벡터공간 $V$ 위에 정의된 symmetric bilinear form $\langle-,-\rangle$이 *내적<sub>inner product</sub>*이라는 것은 모든 $v\in V$에 대하여 $\langle v,v\rangle\geq 0$이고, 이 때 등호는 오직 $v=0$일 때만 성립하는 것이다. 내적이 주어진 공간 $V$를 간단하게 *내적공간<sub>inner product space</sub>*이라 부른다.

</div>

정의를 살펴보면, 내적의 정의에서 $\langle v,v\rangle\geq 0$이라는 조건은 field $F$가 대소관계의 개념을 가지고 있어야 하기 때문에 일반적인 field $F$에 대해서는 잘 정의되지 않는다는 것을 알 수 있다. 때문에 우리는 대소관계가 잘 정의되어 있는 field인 $\mathbb{R}$에서만 이론을 전개하고, 다음 글에서는 이를 이용하여 $\mathbb{C}$에서도 내적을 정의한다. 혼동을 피하기 위해 지금부터 실수 위에 정의된 내적공간을 $\mathbb{R}$-내적공간이라 적는다.

내적의 대표적인 예시는 $\mathbb{R}^n$ 상에서 정의된 *dot product*

$$\langle v,w\rangle=\sum_{i=1}^n v_iw_i$$

이다. 이것이 $\mathbb{R}^n$ 상에서의 non-degenerate bilinear form인 것은 이미 알고 있고, $\langle -,-\rangle$이 symmetric하다는 것 또한 정의로부터 자명하다. 마지막으로 임의의 $v$에 대하여

$$\langle v,v\rangle=\sum_{i=1}^n v_i^2\geq 0$$

이고 등호는 오직 $v=0$일 때만 성립한다.

한편, $\mathbb{R}$-벡터공간 위에 내적이 정의된다면, 가장 좋은 것 중 하나는 벡터의 <em_ko>크기</em_ko>가 잘 정의된다는 것이다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> $\mathbb{R}$-벡터공간 $V$ 위에 정의된 *norm<sub>노름</sub>*은 다음의 조건을 만족하는 함수 $\lVert -\rVert:V\rightarrow\mathbb{R}$이다.

1. $\lVert v\rVert\geq 0$이 모든 $v$에 대하여 성립하며, 특히 등호는 오직 $v=0$일 때만 성립한다.
2. 임의의 $\alpha\in\mathbb{R}$과 $v\in V$에 대하여, $\lVert\alpha v\rVert=\lvert\alpha\rvert\lVert v\rVert$이 성립한다.
3. (삼각부등식) 임의의 $u,v\in V$에 대하여, $\lVert u+v\rVert\leq\lVert u\rVert+\lVert v\rVert$가 성립한다.

</div>

다음 명제는 이미 고등학교 때부터 익숙했던 것이다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3 (Cauchy-Schwarz)**</ins> $\mathbb{R}$-내적공간 $V$의 임의의 벡터 $v,w$에 대하여 다음의 식

$$\lvert \langle v,w\rangle\rvert\leq\sqrt{\langle u,u\rangle}\sqrt{\langle v,v\rangle}$$

이 성립한다. 등호는 $u=\lambda v$를 만족하는 적당한 상수 $\lambda$가 존재할 때 성립한다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

만일 $v=0$이라면 양 변이 모두 0이므로 부등식이 성립한다. $v\neq 0$이라 가정하자. 그럼 $\langle v,v\rangle\neq 0$이다. 이제

$$\lambda=\frac{\langle u,v\rangle}{\langle v,v\rangle}$$

으로 정의하면, 다음의 식

$$0\leq \langle u-\lambda v, u-\lambda v\rangle$$

의 우변을 전개하여

$$0\leq \langle u,u\rangle-2\lambda\langle u,v\rangle+\lambda^2\langle v,v\rangle=\langle u,u\rangle-\frac{2\langle u,v\rangle^2}{\langle v,v\rangle}+\frac{\langle u,v\rangle^2}{\langle v,v\rangle}=\langle u,u\rangle-\frac{\langle u,v\rangle^2}{\langle v,v\rangle}$$

을 얻는다. 등호는 정확히 $u-\lambda v=0$일 때 성립한다. 이로부터 원하는 식을 얻는다.

</details>


<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> $\mathbb{R}$-내적공간 $V$에 대하여, 다음의 식

$$\lVert v\rVert:=\sqrt{\langle v,v\rangle}$$

으로 정의된 함수 $\lVert-\rVert:V\rightarrow \mathbb{R}$은 norm이 된다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 위의 식 $\lVert v\rVert$는 $\mathbb{R}$로의 함수이다. 이는 $(v,v)\geq 0$이 항상 성립하기 때문이다.

Norm의 조건 중 첫째 조건과 둘째 조건은 자명하고, 오직 삼각부등식만 보이면 충분하다. 임의의 $u,v\in V$에 대하여, 

$$\lVert u+v\rVert=\sqrt{\langle u+v,u+v\rangle}=\sqrt{\langle u,u\rangle+2\langle u,v\rangle+\langle v,v\rangle}$$

이고, 코시-슈바르츠 부등식을 적용하면

$$\langle u,u\rangle+2\langle u,v\rangle+\langle v,v\rangle\leq \lVert u\rVert^2+2\lVert u\rVert\lVert v\rVert+\lVert v\rVert^2=(\lVert u\rVert+\lVert v\rVert)^2$$

이므로, 이로부터 삼각부등식이 증명된다.

</details>

그러나 일반적으로 위 명제의 역은 성립하지 않는다. 즉, $V$에 정의된 내적은 norm을 정의하지만, 거꾸로 norm이 주어졌다 해서 내적이 정의될 수 있는 것은 아니다. 

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> $V$가 $\mathbb{R}$-내적공간이라 하자. 만일 $\lVert -\rVert$이 $V$의 내적으로부터 [명제 4](#prop4)의 식으로 얻어진 norm이라면, 다음의 *평행사변형 법칙<sub>parallelogram law</sub>*

$$\lVert u+v\rVert^2+\lVert u-v\rVert^2=2\lVert u\rVert^2+2\lVert v\rVert^2$$

이 모든 $u,v$에 대해 성립한다.

</div>

이에 대한 증명은 단순한 계산을 통해 쉽게 가능하다. 또, 이를 통해 내적을 통해 정의되지 않는 norm의 예시를 찾을 수 있다.

<div class="example" markdown="1">

<ins id="ex6">**예시 6**</ins> $\mathbb{R}^n$ 위에 다음의 식

$$\lVert v\rVert_1=\sum_{i=1}^n \lvert v_i\rvert$$

을 통해 $\lVert-\rVert\_1:\mathbb{R}^n\rightarrow\mathbb{R}$을 정의하자. 그럼 $\lVert-\rVert\_1$가 norm의 조건을 모두 만족한다. 만일 적당한 내적 $\langle-,-\rangle\_1$이 존재하여, $\lVert -\rVert\_1$이 

$$\lVert v\rVert_1=\sqrt{\langle v,v\rangle_1}$$

의 꼴로 쓰여질 수 있었다면, [명제 5](#prop5)에 의하여 다음의 식

$$\lVert u+v\rVert_1^2+\lVert u-v\rVert_1^2=2\lVert u\rVert^2_1+2\lVert v\rVert^2_1$$

이 성립하여야 한다. 그런데 $u=(1,0,\ldots, 0)$, 그리고 $v=(0,1,\ldots, 0)$을 대입하면 평행사변형 법칙이 만족되지 않는 것을 알 수 있다. 따라서 $\lVert -\rVert\_1$은 내적으로부터 유도되지 않는다.

</div>

사실 [명제 5](#prop5)는 역 또한 성립한다. 즉, 만일 $\lVert-\rVert$이 평행사변형 법칙을 만족한다면, 다음의 식

$$\langle u,v\rangle:=\frac{1}{4}\left(\lVert u+v\rVert^2-\lVert u-v\rVert^2\right)$$

으로 정의된 $\langle-,-\rangle$이 내적이 된다. 이에 대한 증명은 많이 어렵지는 않지만, $V$가 norm $\lVert-\rVert$를 통해 위상구조가 주어진다는 사실을 이용해야 한다. 이 결과를 지금 사용할 일은 없으므로 우리는 증명하지 않고 넘어간다.

## 정규직교기저

우리는 $\ch\mathbb{R}=0$임을 알고 있으므로, [§쌍선형형식, ⁋명제 6](/ko/math/linear_algebra/bilinear_form#prop6)으로부터 임의의 $\mathbb{R}$-내적공간 $V$에는 orthogonal basis가 존재한다는 것을 안다. 

임의의 $\mathbb{R}$-내적공간 $V$가 주어졌다 하고, $V$에 basis $\mathcal{B}=\\{x_1,\ldots, x_n\\}$이 주어졌다 하자. 우선

$$\hat{x}_1:=x_1$$

으로 정의하자. 이후 

$$\hat{x}_k:=x_k-\sum_{i=1}^{k-1}\frac{\langle x_i,x_k\rangle}{\langle x_i,x_i\rangle}x_i$$

으로 정의하면, 이 과정 끝에 얻어지는 집합 $\\{\hat{x}_1,\ldots, \hat{x}_n\\}$이 orthogonal basis가 된다는 것을 확인할 수 있다. 이렇게 임의의 basis로부터 orthogonal basis를 얻어내는 방법을 *Gram-Schmidt 과정*이라 부른다. 때때로 우리는 이렇게 얻어진 basis의 각 원소들의 크기가 1이기를 바랄 때도 있는데, 이를 위해서는 각 벡터를 자기 자신의 크기로 나누어주면 된다. 이러한 성질을 만족하는 basis를 *orthonormal basis*라 부른다. 만일 $\mathcal{B}=\\{x_1, \ldots, x_n\\}$이 orthonormal basis라면, 임의의 $v\in V$에 대하여

$$v=v_1x_1+\cdots+v_nx_n$$

의 각 성분 $v_i$를 $\langle -, x_i\rangle$을 취해서 알 수 있다. 좌변은 $\langle v, x_i\rangle$이 될 것이며, 우변은 $\langle x_j,x_i\rangle=\delta_{ij}$이므로 오직 $v_i\langle x_i,x_i\rangle=v_i$만 남기 때문이다. 즉

$$v=\langle v, x_1\rangle x_1+\cdots+\langle v, x_n\rangle x_n$$

이 항상 성립한다. 만일 $\mathcal{B}$가 단순한 orthogonal basis였다면 이 계수들을 구할 때 상수배를 적절히 취했어야 할 것이다.

## 직교행렬

$\mathbb{R}$-내적공간 $V$를 생각하자. Linear map $L:V\rightarrow V$와 그 adjoint를 생각하자. 이 경우 $L$의 adjoint는 $L^\ast$ 대신 $L^t$로 적는 것이 관례이다. 그럼

$$\langle v,Lw\rangle=\langle L^t v, w\rangle$$

이 항상 성립하므로, 임의의 linear map $L$이 $\langle-,-\rangle$을 보존한다면 임의의 $v,w$에 대하여

$$\langle v,w\rangle=\langle Lv,Lw\rangle=\langle v, L^t Lw\rangle$$

이 성립하며, 따라서 $L^t L=I$이 성립한다. 따라서 다음과 같이 정의한다.

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> 임의의 $A\in\Mat_n(\mathbb{R})$에 대해, 다음의 식

$$A^tA=AA^t=I$$

가 성립한다면 $A$를 *orthogonal matrix<sub>직교행렬</sub>*이라 부른다.

</div>

Rank-nullity 정리로부터 $A^tA=I$가 성립한다면 반드시 $AA^t=I$ 또한 성립한다는 것을 안다. 따라서 $\langle-,-\rangle$을 보존하는 임의의 linear map의 행렬표현은 orthogonal matrix가 된다.

$V$에 주어진 두 orthonormal basis $\mathcal{B}=\\{x_1,\ldots, x_n\\}$, $\mathcal{C}=\\{x'\_1,\ldots, x'\_n\\}$를 생각하자. 그럼 행렬 $[\id]_\mathcal{C}^\mathcal{B}$의 $i$번째 열은 $x_i$의 $\mathcal{C}$에 대한 행렬표현과 같다. 이제

$$x_i=\langle x_i, x'_1\rangle x'_1+\cdots+\langle x_i, x'_n\rangle x'_n$$

으로부터 

$$[\id]_\mathcal{C}^\mathcal{B}=\begin{pmatrix}\langle x_1,x'_1\rangle&\langle x_2, x'_1\rangle&\cdots&\langle x_n,x'_1\rangle\\ \langle x_1,x'_2\rangle&\langle x_2,x'_2\rangle&\cdots&\langle x_n,x'_2\rangle\\ \vdots&\vdots&\ddots&\vdots\\ \langle x_1, x'_n\rangle&\langle x_2, x'_n\rangle&\cdots&\langle x_n,x'_n\rangle\end{pmatrix}$$

이 된다. $\mathcal{B}$와 $\mathcal{C}$의 역할을 바꾸면

$$[\id]_\mathcal{B}^\mathcal{C}=\begin{pmatrix}\langle x'_1,x_1\rangle&\langle x'_2, x_1\rangle&\cdots&\langle x'_n,x_1\rangle\\ \langle x'_1,x_2\rangle&\langle x'_2,x_2\rangle&\cdots&\langle x'_n,x_2\rangle\\ \vdots&\vdots&\ddots&\vdots\\ \langle x'_1, x_n\rangle&\langle x'_2, x_n\rangle&\cdots&\langle x'_n,n\rangle\end{pmatrix}$$

이므로, $\langle-,-\rangle$이 symmetric이라는 조건으로부터 두 orthonormal basis들 간의 기저변환행렬은 항상 orthogonal matrix가 된다는 것을 확인할 수 있다. 거꾸로 임의의 orthogonal matrix는 항상 orthonormal basis 사이의 기저변환행렬로 해석할 수 있다.

## Projection theorem

이제 $V$가 $\mathbb{R}$-내적공간이라 하고, 그 부분공간 $U\subseteq V$가 주어졌다 하자. 만일 $U\neq \\{0\\}$이라면 $u\neq 0$을 만족하는 임의의 $u\in U$마다 $\langle u,u\rangle>0$이 성립하므로, 특히 $V$의 내적 $\langle -,-\rangle$을 $U$로 제한한 것이 non-degenerate이고 따라서 $U$ 위에 bilinear form을 정의한다. 이렇게 정의된 bilinear form이 내적의 성질을 갖는 것은 거의 자명하므로, $\mathbb{R}$-내적공간의 임의의 부분공간은 항상 자연스러운 $\mathbb{R}$-내적공간 구조를 갖는다. 따라서 $U$의 orthonormal basis $\mathcal{B}=\\{x_1,\ldots, x_k\\}$가 존재한다. 뿐만 아니라, $\mathcal{B}$를 포함하는 $V$의 basis를 하나 택한 후, Gram-Schmidt 과정을 $x_1,\ldots, x_k$들부터 반복하면 $\mathcal{B}$를 포함하는 $V$의 orthonormal basis가 존재한다는 것도 확인할 수 있다.

이제 임의의 $v\in V$에 대하여, $v$의 $U$로의 *projection<sub>사영</sub>* $\proj_U v$를 다음의 식

$$\proj_U v=\sum_{i=1}^k \langle v, x_i\rangle x_i$$

으로 정의하자. 이 정의가 말이 되기 위해서는 위 벡터가 $U$의 orthonormal basis $\mathcal{B}$의 선택과는 관계없이 정의되어야 한다.

<div class="proposition" markdown="1">

<ins id="lem8">**보조정리 8**</ins> 위와 같은 상황에서, 만일 $\mathcal{B}=\\{x_1,\ldots, x_k\\},\mathcal{B}'=\\{x_1',\ldots, x_k'\\}$가 $U$의 두 orthonormal basis라 하면, 임의의 $v\in V$에 대하여

$$\sum_{i=1}^k \langle v, x_i\rangle x_i=\sum_{i=1}^k\langle v, x'_i\rangle x_i'$$

이 성립한다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

식

$$[v]_\mathcal{B}=[\id]^{\mathcal{B}'}_{\mathcal{B}}[v]_{\mathcal{B}'}$$

의 다른 표현일 뿐이다.

</details>

다음의 *projection theorem*은 이렇게 정의한 벡터 $\proj_Uv$가 $v$와 가장 가까운 $U$의 원소임을 알려준다.

<div class="proposition" markdown="1">

<ins id="thm9">**정리 9**</ins> $\mathbb{R}$-내적공간 $V$와 그 부분공간 $U\subseteq V$를 생각하자. 그럼 임의의 $v\in V$에 대하여, $\proj_Uv$는

$$\lVert \proj_Uv-v\rVert=\min_{w\in U}\lVert v-w\rVert$$

을 만족하며, 뿐만 아니라 위의 식을 만족하는 벡터는 오직 $\proj_Uv$ 뿐이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $u,u'\in U$가 모두 $\lVert v-w\rVert$를 최소로 만든다고 가정하자. 그럼 최소성으로부터

$$\lVert v-u\rVert=\lVert v-u'\rVert\leq\left\lVert v-\frac{u+u'}{2}\right\rVert$$

을 얻는다. 따라서

$$\lVert v-u\rVert+\lVert v-u'\rVert=\lVert (v-u)+(v-u')\rVert$$

이다. 이제 삼각부등식의 등호조건으로부터 다음의 식

$$v-u=\lambda (v-u')$$

를 만족하는 상수 $\lambda$가 존재한다는 것을 안다. 특히 

$$(1-\lambda)v=u-\lambda u'\in U$$

가 성립한다. 이로부터 $\lambda=1$이거나 $v\in U$이다. 만일 $\lambda=1$이라면 $v-u=v-u'$로부터 $u=u'$이고, $v\in U$라면 $\lVert v-w\rVert$를 최소로 만드는 $w$는 $w=v$ 뿐이므로 이 경우에도 마찬가지로 $u=u'$이다. 따라서 이 식을 최소로 만드는 벡터는 유일하다. 

이제 실제로 $\proj_Uv$가 실제로 $\lVert v-w\rVert$를 최소로 만드는 벡터임을 보여야 한다. $U$의 basis $\\{x\_1,\ldots, x\_k\\}$를 하나 택하고, 이를 포함하는 $V$의 orthonormal basis를 $\\{x\_1,\ldots, x\_n\\}$이라 하자. 그럼 $v=\sum\_{i=1}^n v\_i x\_i$, $w=\sum\_{i=1}^k w\_i x\_i$로부터

$$\lVert v-w\rVert=\left\lVert\sum_{i=1}^k(v_i-w_i)x_i+\sum_{i=k+1}^n v_ix_i\right\rVert=\sum_{i=1}^k (v_i-w_i)^2+\sum_{i=k+1}^n v_i^2\geq \sum_{i=k+1}^n v_i^2$$

이고, 등호는 모든 $1\leq i\leq k$에 대하여 $v_i=w_i$일 때 성립한다. 그럼 

$$\proj_Uv=\sum_{i=1}^k v_ix_i=\sum_{i=1}^k w_ix_i=w$$

이므로 원하는 결론을 얻는다.

</details>

뿐만 아니라, $\proj_Uv$의 정의에 의하여 $v-\proj_Uv$는 $U$에 수직인 벡터가 되는 것이 자명하다. 이 사실은 다음 글에서 유용하게 사용한다.