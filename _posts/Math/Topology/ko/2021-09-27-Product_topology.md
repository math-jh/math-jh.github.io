---
title: "곱위상"
excerpt: "위상공간의 product"

lang: ko

categories: [Math / Topology]
permalink: /ko/math/topology/product_topology
header:
    overlay_image: /assets/images/Topology/Topological_basis.png
    overlay_filter: 0.5
sidebar: 
    nav: "topology-ko"

date: 2021-09-26
last_modified_at: 2022-04-07
weight: 10
    
---

## Product space와 box topology

이번 글에서 우리가 살펴볼 건 곱위상이다. 즉, 위상공간들의 family $(X_i)$가 주어졌을 때, 곱집합 $\prod X_i$ 위에 위상구조를 주려 한다. 여기에는 크게 두 가지 방법이 있다. 

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> 위상공간 $X_i$의 열린집합들 $U_i$에 대하여, $\prod U_i$의 꼴로 쓰여지는 $\prod X_i$의 부분집합들의 모임을 $\mathcal{B}$라 하자. 그럼 $\mathcal{B}$에 의해 만들어지는 위상을 *box topology<sub>상자위상</sub>*이라 부른다. 한편, canonical projection들 $\operatorname{pr}\_i:\prod X_i\rightarrow X_i$에 대하여, $\operatorname{pr}\_i^{-1}(U\_i)$들의 모임 $\mathcal{S}$를 subbasis로 하여 만들어지는 $\prod X\_i$ 위의 위상을 *product topology<sub>곱위상</sub>*이라 부른다.  

</div>

Box topology는 꽤나 직관적으로 그럴듯해 보인다. 반면 product topology는 좀 덜 직관적으로 보이는데, 이를 자세히 살펴보자. 우선 $\operatorname{pr}_i^{-1}(U_i)$들이 어떻게 생겼는지를 볼 필요가 있다. 집합으로서

$$\operatorname{pr}_{i_0}^{-1}(U_{i_0})=\{(x_i)_{i\in I}: x_{i_0}\in U_{i_0}\}$$ 

이므로, 이 집합은 $i_0$번째 좌표가 $U_i$에 속하는 순서쌍들의 모임이다. 즉, 

$$\operatorname{pr}_{i_0}^{-1}(U_{i_0})=\prod_{i\in I} U_i,\qquad U_i=\begin{cases}X_i&i\neq i_0\\ U_{i_0}&i=i_0\end{cases}$$

이다. 그럼 이제 subbasis $\mathcal{S}$로 만들어지는 basis의 원소들은 이들의 유한한 교집합이므로 *유한 개의* 성분들만 $X_i$의 열린 진부분집합이고, 나머지 성분들은 모두 전체집합 $X_i$인 집합들로 이루어진다. 
 
따라서, 만일 주어진 family가 유한집합이라면 두 위상의 차이는 없다. 두 위상이 차이가 있는 것은 index set이 무한집합일 때 뿐이다. 그렇다면 왜 상대적으로 덜 자명해보이는 정의를 product topology라 부르는지가 의문인데, 이는 다음의 명제에 따른 것이다.

<div class="proposition" markdown="1">

<ins id="pp2">**명제 2**</ins> 위상공간들 사이의 함수 $f:Y\rightarrow\prod X_i$가 다음의 식

$$f(y)=(f_i(y))_{i\in I}$$

으로 정의되었다고 하자. 여기서 $f_i:Y\rightarrow X_i$이고, $\prod X_i$는 product topology가 주어져 있다. 그럼 $f$가 연속인 것은 각각의 $f_i$가 연속인 것과 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 임의의 index $i_0\in I$에 대하여 $\operatorname{pr}\_{i\_0}:\prod X_i\rightarrow X\_{i\_0}$는 모두 연속이다. $X\_{i\_0}$의 임의의 열린집합 $U\_{i\_0}$에 대하여, $\operatorname{pr}\_{i\_0}^{-1}(U\_{i\_0})$은 정의에 의해 $\prod X_i$에서 열린집합이기 때문이다. 따라서, 만일 $f$가 연속이라면, $f_i=\operatorname{pr}_i\circ f$는 연속함수들의 합성이므로 당연히 연속이다.

이제 반대방향을 보여야 한다. 즉, $f_i$가 모두 연속이라는 것을 가정하고, $f$가 연속이라는 것을 보여야 한다. 이를 위해서는 임의의 열린집합 $U$에 대하여, $f^{-1}(U)$가 열린집합임을 보여야 한다. 그런데, $f^{-1}$은 합집합과 교집합을 항상 보존하므로 사실 우리는 이를 임의의 subbasis의 원소에 대해서만 보이면 충분하다. 그런데,

$$f^{-1}(\operatorname{pr}_j^{-1}(U_j))=(f^{-1}\circ \operatorname{pr}_j^{-1})(U_j)=(\operatorname{pr}_j\circ f)^{-1}(U_j)=f_{j}^{-1}(U_j)$$

이고, $f_j$의 연속성에 의해 이 또한 $A$에서 열린집합이므로 증명이 끝난다. 

</details>

즉, 우리가 product topology라는 이름을 붙인 건 다름아닌 product의 universal property에 대한 analogue인 것이다. (예를 들어 <#ref#>) 이는 즉 box topology는 위의 명제를 만족하지 않는다는 말이기도 하다.

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> 예를 들어, $\mathbb{R}$에서 $\mathbb{R}^\omega=\prod_{n=1}^\infty \mathbb{R}$으로의 함수 $f$를 각각의 $n$에 대해 $f_n(t)=t$로 정의하자. 그럼 각각의 $f_n$는 연속이지만, box topology의 basis element

$$B=(-1,1)\times\left(-\frac{1}{2},\frac{1}{2}\right)\times\cdots$$

의 preimage는 $\mathbb{R}$에서 열린집합이 아니다. $0\in f^{-1}(B)$를 포함하는 $f^{-1}(B)=\\{0\\}$의 열린 부분집합이 존재하지 않기 때문이다.

</div>

Product topology는 새로운 위상구조를 만들 때 종종 쓰게 된다. 예를 들어, 우리는 앞서 $\mathbb{R}^n$에 위상구조를 정의했는데, 이는 $\mathbb{R}$을 곱하여 얻어지는 구조와 동일하다.

<div class="proposition" markdown="1">

<ins id="pp4">**명제 4**</ins> $\mathbb{R}^n$에 주어진 metric topology는 standard metric이 주어진 $\mathbb{R}$들의 product topology와 동일하다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

의외로 아주 쉽다. $\mathbb{R}$들의 product topology들의 basis는 $\prod (a_i, b_i)$들로 나타나는데, 그건 metric topology도 마찬가지다. ([§거리위상 (2), 정의 1](/ko/math/topology/metric_topology_2#df1)) 이 사실을 이용하면, [§위상공간의 기저, 보조정리 8](/ko/math/topology/basic_definition_2#lem8)을 이용해 원하는 결과를 얻는다.

</details>

## Uniform topology

미묘한 부분은 $n=\infty$일 때 발생한다. 예를 들어, $\mathbb{R}^\omega$에는 쉽게 product topology를 줄 수 있다. 반면, $\mathbb{R}^\omega$에 적절한 metric을 주는 방법은 쉽게 보이지 않는다. 예를 들어, 원래의 정의

$$d(x,y)=\lVert x-y\rVert_2=\sqrt{\sum_{i=1}^n x_i^2}$$

는 수렴성 때문에 정의로 채택할 수 없고, 이는 square metric

$$\rho(x,y)=\lVert x-y\rVert_\infty=\max_{1\leq i\leq n}\{\lvert x_i-y_i\rvert\}$$

도 마찬가지다. 

결국 문제는 무한차원에서는 metric이 유한하게 잘 주어지지 않을 수 있다는 것인데, 우리는 마침 이렇게 무한대로 발산하는 경우를 잘 컨트롤해줄 수 있는 도구를 하나 갖고 있다. ([§거리위상 (2), 명제 3](/ko/math/topology/metric_topology_2#pp3)) 따라서 다음과 같이 정의하자.

<div class="definition" markdown="1">

<ins id="df5">**정의 5**</ins> 임의의 index set $J$에 대하여, $\mathbb{R}^J$ 위에 다음과 같은 metric $\overline{\rho}$를 정의하자.

> 임의의 $x=(x\_i)\_{i\in J}$, $y=(y\_i)\_{i\in J}$에 대하여, 함수 $\overline{\rho}$는
>
> $$\overline{\rho}(x,y)=\sup_{i\in J}\left\{\overline{d}(x_i, y_i)\right\}$$
>
> 와 같이 정의된 함수이다. 여기서 $\overline{d}$는 $\mathbb{R}$에서의 standard bounded metric, 곧 
>
> $$\overline{d}(x, y)=\min\left\{\left\lvert x-y\right\rvert,1\right\}$$
>
> 이다.

이 metric을 $\mathbb{R}^J$ 위에서의 *uniform metric<sub>균등거리</sub>*이라 부르고, $\overline{\rho}$에 의해 만들어지는 위상을 *uniform topology<sub>균등위상</sub>*이라 부른다.

</div>

<div class="remark" markdown="1">

<ins id="rmk1">**참고**</ins> 여기서 uniform이라는 단어는 uniform convergence, 혹은 나중에 다룰 uniform continuity와는 관련이 크게 없고, $\sup$-norm을 uniform norm이라고도 부르는 관례에 따른 것이다.

</div>

그러나, 이렇게 정의된 위상구조는 box topology와도, product topology와도 다르다.

<div class="proposition" markdown="1">

<ins id="pp6">**명제 6**</ins> $\mathbb{R}^J$ 위에 uniform, box, product topology들이 각각 정의되었다고 하자. 그럼 box topology는 uniform topology보다 강하고, uniform topology은 product topology보다 강하다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

임의의 $x\in\mathbb{R}^J$를 고정하자.

$x$를 포함하는 product topology의 basis $\prod U_i$에 대하여, $i_1$, $\ldots$, $i_n$들이 $U_i\neq \mathbb{R}$인 index들이라 하자. 그럼 각각의 $U_{i_k}$에 대하여, 우리는 적당한 $\epsilon_{i_k}>0$들을 잡아

$$B_{\overline{d}}(x_{i_k},\epsilon_{i_k})\subset U_{i_k}$$

이도록 할 수 있다. 이제 $\epsilon=\min_{1\leq k\leq n}\left\\{\epsilon_{i_k}\right\\}$이라 하고 $B_{\overline{\rho}}(x, \epsilon)$을 생각하자. 만약 $z\in  B_{\overline{\rho}}(x, \epsilon)$라면, 모든 $i\in J$에 대하여 $\overline{d}(x_i, z_i)&lt;\epsilon$이고, 따라서 $z$는 $\prod U_i$에 속한다. 즉, 우리는 임의로 주어진 $x$와 $x$를 포함하는 product topology의 basis element에 대하여, uniform topology의 어떤 basis element가 존재하여 $x$를 포함하고 $\prod U_i$에 포함됨을 보였으므로 product topology보다 uniform topology가 강하다.

이제 이와 비슷하게, [§위상공간의 기저, 보조정리 8](/ko/math/topology/basic_definition_2#lem8)을 이용해서 box topology가 uniform topology보다 강하다는 것을 보이자. $x$를 포함하는 uniform topology의 basis element $B_{\overline{\rho}}(x,\epsilon)$과, box topology의 basis element $\prod \left(x_i-\frac{1}{2}\epsilon, x_i+\frac{1}{2}\epsilon\right)$를 생각하자. 그럼 임의의 $z\in\prod \left(x_i-\frac{1}{2}\epsilon, x_i+\frac{1}{2}\epsilon\right)$에 대하여, $\overline{d}(x_i, z_i)&lt;\frac{1}{2}\epsilon$이 모든 $i$에 대해 성립하므로 $\overline{\rho}(x,y)\leq \frac{1}{2}\epsilon&lt;\epsilon$이 성립한다. 즉, $z\in B_{\overline{\rho}}(x,\epsilon)$이므로 box topology는 uniform topology보다 강하다.

</details>

물론, $J$가 유한집합일 경우 product topology와 box topology가 같으므로, 이 세 위상구조는 모두 동일하다. 차이는 $J$가 무한집합일 때 발생하는데, 이들은 모두 strict하게 강하다.

<div class="example" markdown="1">

<ins id="ex7">**예시 7**</ins> 예컨대 $J=\mathbb{N}$일 경우, $\prod \left(-\frac{1}{2^n},\frac{1}{2^n}\right)$는 box topology에서 열린집합이지만, 원점 $\mathbf{0}$을 포함하고 이 집합에 포함되는 uniform topology의 basis element가 존재하지 않으므로 이 집합은 uniform topology에서 열린집합이 아니다.
  
또, uniform topology에서의 open ball $B_{\overline{\rho}}\left(\mathbf{0},\frac{1}{2}\right)$에 대하여 $\mathbf{0}$을 포함하고 이 집합에 포함되는 product topolgoy의 basis element가 존재하지 않으므로 이 집합은 product topology에서 열린집합이 아니다.

</div>

한편, 우리는 metrizable인 공간이 여러모로 다루기 쉽다는 것을 언급한 적이 있는데, 다음과 같이 product topology가 주어진 $\mathbb{R}^\omega$가 metrizable하다는 것을 확인할 수 있다. 

<div class="proposition" markdown="1">

<ins id="pp16">**명제 16**</ins> $\mathbb{R}^\omega$ 위에 다음의 식

$$D(x,y)=\sup\left\{\frac{\overline{d}(x_i, y_i)}{i}\right\}$$

로 정의된 함수는 metric이며, 이 metric에 의해 정의된 위상은 product topology와 같다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

이제 $D$가 metric인 것을 보이는 것 정도는 너무 쉽다. 이 metric에 의해 정의되는 metric topology가 product topology와 같음을 보이기 위해, 우선 $x\in\mathbb{R}^\omega$와 이를 포함하는 metric topology에서의 열린집합 $U$를 택하자. $U$가 $D$에 의해 정의되는 metric topology에서 열린집합이므로, 어떠한 $\epsilon$-ball $B_D(x,\epsilon)$이 존재하여 $B_D(x,\epsilon)\subset U$이다. $\epsilon$을 고정하고,  $1/N&lt;\epsilon$을 만족하는 충분히 큰 $N$에 대하여 
  
$$V=\left(x_1-\epsilon, x_1+\epsilon\right)\times\cdots\times(x_N-\epsilon,x_N+\epsilon)\times\mathbb{R}\times\mathbb{R}\times\cdots$$

이라 하자. 정의에 의하여 $\overline{d}(x,y)\leq 1$이 항상 성립하므로, $i\geq N$에 대해서는

$$\frac{\overline{d}(x_i, y_i)}{i}\leq\frac{1}{N}$$

이 항상 성립하고, 따라서 

$$D(x, y)=\sup\left\{\frac{\overline{d}(x_i, y_i)}{i}\right\}\leq\max \left\{\frac{\overline{d}(x_1, y_1)}{1},\cdots, \frac{\overline{d}(x_N, y_N)}{N},\frac{1}{N}\right\}$$

이 성립한다. 만일 $y\in V$라면 위의 식에서 $\overline{d}(x_i, y_i)$들 각각이 $\epsilon$보다 작고, $1/N$도 $\epsilon$보다 작으므로 우변이 $\epsilon$보다 작다. 즉 $V\subset B_D(x,\epsilon)$이 성립한다.

반대로 임의의 $x\in\mathbb{R}^\omega$와 $x$를 포함하는 product topology의 basis element $\prod U_i$를 생각하자. Product topology의 정의에 의하여, 유한개의 index를 제외하면 $U_i=\mathbb{R}$이다. 이 유한개의 index들을 $i_1$, $\ldots$, $i_k$라 하면, 우리는 이들 각각에 대하여 적당한 $\epsilon_{i_k}>0$들을 잡아 $(x_{i_k}-\epsilon_{i_k},x_{i_k}+\epsilon_{i_k})$가 $U_{i_k}$ 안에 속하도록 할 수 있다. 이제 $\epsilon_{i_k}$들을 1보다 작도록 잡고, $\epsilon=\min_{1\leq k\leq n}\left\\{\epsilon_{i_k}/i_k\right\\}$이라 하면 $\epsilon\leq\epsilon_{i_k}/i_k$이다. 임의의 $y\in B_D(x,\epsilon)$에 대하여,

$$\frac{\overline{d}(x_i, y_i)}{i}\leq D(x,y)<\epsilon$$

이 성립하고, 특히 index $i_1$, $\ldots$, $i_k$에 대해서도 위의 식이 성립하므로 

$$\frac{\overline{d}(x_{i_k}, y_{i_k})}{i_k}<\epsilon\leq\frac{\epsilon_{i_k}}{i_k},$$

즉 $\left\lvert x_{i_k}-y_{i_k}\right\rvert&lt;\epsilon_{i_k}$이므로 $y\in \prod U_i$이다. 즉 $B_D(x,\epsilon)\subset \prod U_i$이다.

</details>



---

**참고문헌**

**[Mun]** J.R. Munkres, <i>Topology</i>. Featured Titles for Topology. Prentice Hall, Incorporated, 2000.

---


