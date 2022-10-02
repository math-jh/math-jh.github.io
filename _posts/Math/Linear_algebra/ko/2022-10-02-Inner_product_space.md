---

title: "내적공간"
excerpt: "실수집합 위에서 정의된 내적의 성질"

categories: [Math / Linear Algebra]
permalink: /ko/math/linear_algebra/inner_product_space
sidebar: 
    nav: "linear_algebra-ko"

header:
    overlay_image: /assets/images/Linear_algebra/Inner_product_space.png
    overlay_filter: 0.5

date: 2022-10-02
last_modified_at: 2022-10-02

weight: 17

---

## 내적과 노름

이제 우리는 더 특수한 경우를 생각한다. 

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> $\mathbb{R}$-벡터공간 $V$ 위에 정의된 symmetric bilinear form $\langle-,-\rangle$이 *내적<sub>inner product</sub>*이라는 것은 모든 $v\in V$에 대하여 $\langle v,v\rangle\geq 0$이고, 이 때 등호는 오직 $v=0$일 때만 성립하는 것이다. 내적이 주어진 공간 $V$를 간단하게 *내적공간<sub>inner product space</sub>*이라 부른다.

</div>

정의를 살펴보면, 내적의 정의에서 $\langle v,v\rangle\geq 0$이라는 조건은 field $F$가 대소관계의 개념을 가지고 있어야 하기 때문에 일반적인 field $F$에 대해서는 잘 정의되지 않는다는 것을 알 수 있다. 때문에 우리는 대소관계가 잘 정의되어 있는 field인 $\mathbb{R}$에서만 이론을 전개하고, 다음 글에서는 이를 이용하여 $\mathbb{C}$에서도 내적을 정의한다. 혼동을 피하기 위해 지금부터 실수 위에 정의된 내적공간을 $\mathbb{R}$-내적공간이라 적는다.

내적의 대표적인 예시는 $\mathbb{R}^n$ 상에서 정의된 *dot product*

$$\langle v,w\rangle=\sum_{i=1}^n v_iw_i$$

이다. 이것이 $\mathbb{R}^n$ 상에서의 non-degenerate bilinear form인 것은 이미 알고 있고, $\langle -,-\rangle$이 symmetric하다는 것 또한 정의로부터 자명하다. 마지막으로 임의의 $v$에 대하여

$$\langle v,v\rangle=\sum_{i=1}^n v_i^2\geq 0$$

이고 등호는 오직 $v=0$일 때만 성립한다.

한편, $\mathbb{R}$-벡터공간 위에 내적이 정의된다면, 가장 좋은 것 중 하나는 벡터의 <em_ko>크기</em_ko>가 잘 정의된다는 것이다.

<div class="definition" markdown="1">

<ins id="df2">**정의 2**</ins> $\mathbb{R}$-벡터공간 $V$ 위에 정의된 *norm<sub>노름</sub>*은 다음의 조건을 만족하는 함수 $\lVert -\rVert:V\rightarrow\mathbb{R}$이다.

1. $\lVert v\rVert\geq 0$이 모든 $v$에 대하여 성립하며, 특히 등호는 오직 $v=0$일 때만 성립한다.
2. 임의의 $\alpha\in\mathbb{R}$과 $v\in V$에 대하여, $\lVert\alpha v\rVert=\lvert\alpha\rvert\lVert v\rVert$이 성립한다.
3. (삼각부등식) 임의의 $u,v\in V$에 대하여, $\lVert u+v\rVert\leq\lVert u\rVert+\lVert v\rVert$가 성립한다.

</div>

다음 명제는 이미 고등학교 때부터 익숙했던 것이다.

<div class="proposition" markdown="1">

<ins id="pp3">**명제 3 (Cauchy-Schwarz)**</ins> $\mathbb{R}$-내적공간 $V$의 임의의 벡터 $v,w$에 대하여 다음의 식

$$\lvert \langle v,w\rangle\rvert\leq\sqrt{\langle u,u\rangle}\sqrt{\langle v,v\rangle}$$

이 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

만일 $v=0$이라면 양 변이 모두 0이므로 부등식이 성립한다. $v\neq 0$이라 가정하자. 그럼 $\langle v,v\rangle\neq 0$이다. 이제

$$\lambda=\frac{\langle u,v\rangle}{\langle v,v\rangle}$$

으로 정의하면, 다음의 식

$$0\leq \langle u-\lambda v, u-\lambda v\rangle$$

의 우변을 전개하여

$$0\leq \langle u,u\rangle-2\lambda\langle u,v\rangle+\lambda^2\langle v,v\rangle=\langle u,u\rangle-\frac{2\langle u,v\rangle^2}{\langle v,v\rangle}+\frac{\langle u,v\rangle^2}{\langle v,v\rangle}=\langle u,u\rangle-\frac{\langle u,v\rangle^2}{\langle v,v\rangle}$$

을 얻는다. 이로부터 원하는 식을 얻는다.

</details>


<div class="proposition" markdown="1">

<ins id="pp4">**명제 4**</ins> $\mathbb{R}$-내적공간 $V$에 대하여, 다음의 식

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

<ins id="pp5">**명제 5**</ins> $V$가 $\mathbb{R}$-내적공간이라 하자. 만일 $\lVert -\rVert$이 $V$의 내적으로부터 [명제 4](#pp4)의 식으로 얻어진 norm이라면, 다음의 *평행사변형 법칙<sub>parallelogram law</sub>*

$$\lVert u+v\rVert^2+\lVert u-v\rVert^2=2\lVert u\rVert^2+2\lVert v\rVert^2$$

이 모든 $u,v$에 대해 성립한다.

</div>

이에 대한 증명은 단순한 계산을 통해 쉽게 가능하다. 또, 이를 통해 내적을 통해 정의되지 않는 norm의 예시를 찾을 수 있다.

<div class="example" markdown="1">

<ins id="ex6">**예시 6**</ins> $\mathbb{R}^n$ 위에 다음의 식

$$\lVert v\rVert_1=\sum_{i=1}^n \lvert v_i\rvert$$

을 통해 $\lVert-\rVert\_1:\mathbb{R}^n\rightarrow\mathbb{R}$을 정의하자. 그럼 $\lVert-\rVert\_1$가 norm의 조건을 모두 만족한다. 만일 적당한 내적 $\langle-,-\rangle\_1$이 존재하여, $\lVert -\rVert\_1$이 

$$\lVert v\rVert_1=\sqrt{\langle v,v\rangle_1}$$

의 꼴로 쓰여질 수 있었다면, [명제 5](#pp5)에 의하여 다음의 식

$$\lVert u+v\rVert_1^2+\lVert u-v\rVert_1^2=2\lVert u\rVert^2_1+2\lVert v\rVert^2_1$$

이 성립하여야 한다. 그런데 $u=(1,0,\ldots, 0)$, 그리고 $v=(0,1,\ldots, 0)$을 대입하면 평행사변형 법칙이 만족되지 않는 것을 알 수 있다. 따라서 $\lVert -\rVert\_1$은 내적으로부터 유도되지 않는다.

</div>

사실 [명제 5](#pp5)는 역 또한 성립한다. 즉, 만일 $\lVert-\rVert$이 평행사변형 법칙을 만족한다면, 다음의 식

$$\langle u,v\rangle:=\frac{1}{4}\left(\lVert u+v\rVert^2-\lVert u-v\rVert^2\right)$$

으로 정의된 $\langle-,-\rangle$이 내적이 된다. 이에 대한 증명은 많이 어렵지는 않지만, $V$가 norm $\lVert-\rVert$를 통해 위상구조가 주어진다는 사실을 이용해야 한다. 이 결과를 지금 사용할 일은 없으므로 우리는 증명하지 않고 넘어간다.

## Gram-Schmidt 과정

실수 집합에서 $2\neq 0$임은 자명하다. 따라서 [§쌍선형형식, 명제 6](/ko/math/linear_algebra/bilinear_form#pp6)으로부터, 임의의 $\mathbb{R}$-내적공간 $V$에는 orthogonal basis가 존재한다. 지금 소개할 Gram-Schmidt 과정 또한 이와 동일한 아이디어를 사용한다.

임의의 $\mathbb{R}$-내적공간 $V$가 주어졌다 하고, $V$에 basis $\mathcal{B}=\\{v_1,\ldots, v_n\\}$이 주어졌다 하자. 우선

$$\hat{v}_1:=v_1$$

으로 정의하자. 이후 

$$\hat{v}_k:=v_k-\sum_{i=1}^{k-1}\frac{\langle v_i,v_k\rangle}{\langle v_i,v_i\rangle}v_i$$

으로 정의하면, 이 과정 끝에 얻어지는 집합 $\\{\hat{v}_1,\ldots, \hat{v}_n\\}$이 orthogonal basis가 된다는 것을 확인할 수 있다. 때때로 우리는 이렇게 얻어진 basis의 각 원소들의 크기가 1이기를 바랄 때도 있는데, 이를 위해서는 각 벡터를 자기 자신의 크기로 나누어주면 된다. 이러한 성질을 만족하는 basis를 *orthonormal basis*라 부른다.

## Projection theorem

임의의 $\mathbb{R}$-내적공간 $V$가 주어졌다 하고, $U\subseteq V$가 부분공간이라 하자. 만일 $\\{v_1,\ldots, v_{k-1}\\}$이 $U$의 부분집합이라면, 위에서 정의한 

$$\sum_{i=1}^{k-1}\frac{\langle v,v_i\rangle}{\langle v_i,v_i\rangle}v_i$$

을 벡터 $v$의 $U$로의 *projection<sub>사영</sub>*이라 생각할 수 있다. 이 벡터는 $U$의 벡터들 $u$ 가운데, $\lVert u-v\rVert$를 최소로 하는 벡터이며, 이런 측면에서 위의 벡터를 $v$를 $U$의 벡터들로 근사한 것으로 생각하기도 한다. 