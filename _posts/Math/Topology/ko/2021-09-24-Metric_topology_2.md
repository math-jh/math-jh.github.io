---
title: "거리위상 (2)"
excerpt: "순서위상과 거리위상"

lang: ko

categories: [Math / Topology]
permalink: /ko/math/topology/metric_topology_2
header:
    overlay_image: /assets/images/Topology/Topological_basis.png
    overlay_filter: 0.5
sidebar: 
    nav: "topology-ko"

date: 2021-09-24
last_modified_at: 2022-04-07
weight: 7
    
---

이전 글의 말미에서 언급했듯 우리는 metric topology의 성질들을 조금 더 살펴본다. 우선 $\mathbb{R}$ 위에 정의된 standard topology를 임의의 $\mathbb{R}^n$으로 확장하자. 여기에는 두 가지 방법이 있다.

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> 임의의 $x=(x\_1,x\_2,\ldots, x\_n),y=(y\_1,\ldots, y\_n)\in\mathbb{R}^n$에 대하여, *Euclidean metric<sub>유클리드 거리</sub>* $d$를

$$d(x,y)=\lVert x-y\rVert=\sqrt{\sum_{i=1}^n (x_i-y_i)^2}$$

으로 정의한다. 또, *square metric<sub>상자 거리</sub>* $\rho$를 다음의 식

$$\rho(x,y)=\lVert x-y\rVert_\infty=\max\{\lvert x_1-y_1\rvert,\ldots,\lvert x_n-y_n\rvert\}$$

으로 정의한다.

</div>

그러나 이렇게 정의한 두 metric은 결과적으로 같은 위상을 준다. 수치적으로 두 함수가 주는 거리의 값이 다를 수는 있어도, 이들에 의해 정의되는 멀고 가까움의 개념은 크게 차이가 없기 때문이다. 

<div class="proposition" markdown="1">

<ins id="pp2">**명제 2**</ins> 집합 $X$ 위에 정의된 두 metric $d\_1$, $d\_2$에 대하여, 만일 두 양수 $\alpha$, $\beta$가 존재하여 모든 $x,y\in X$에 대해 다음의 식

$$\alpha d_1(x,y)\leq d_2(x,y)\leq \beta d_1(x,y)$$

이 성립한다면 $d\_1$으로 만들어지는 metric topology와 $d\_2$으로 만들어지는 metric topology는 서로 같다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

어차피 $d\_1$과 $d\_2$으로 만들어지는 위상들은 basis로 정의되므로, [§위상공간의 기저, 보조정리 8](/ko/math/topology/basic_definition_1#lem8)를 이용할 수 있다. $d\_1$과 $d\_2$으로 정의되는 metric topology를 각각 $\mathcal{T}\_1$과 $\mathcal{T}\_2$, 그리고 basis들을 $\mathcal{B}\_1$과 $\mathcal{B}\_2$라 하자.  

우선 $\mathcal{B}_1$의 임의의 원소 $B\_1=B\_{d\_1}(x, \epsilon\_1)$와, $B_1$의 임의의 원소 $y$가 주어졌다 하자. $\delta\_1=\epsilon\_1-d\_1(x,y)>0$이라 하면, 임의의 $z\in B\_{d\_2}(y, \alpha\delta\_1)$에 대하여, 

$$d_1(x,z)\leq d_1(x,y)+d_1(y,z)\leq d_1(x,y)+\alpha^{-1}d_2(y,z)<d_1(x,y)+\alpha^{-1}\alpha\delta_1=\epsilon_1$$

이므로 $z\in B_1$이다. 즉, $B\_{d\_2}(y,\alpha\delta\_1)\subset B_1$이고, 따라서 $\mathcal{T}\_2$는 $\mathcal{T}\_1$보다 강하다.  

이와 비슷하게, $\mathcal{B}\_2$의 임의의 원소 $B\_2=B\_{d\_2}(x, \epsilon\_2)$와, $B\_2$의 임의의 원소 $y$가 주어졌다 하자. $\delta\_2=\epsilon\_2-d\_2(x,y)>0$이라 하면, 임의의 $z\in B\_{d\_1}(y, \beta^{-1}\delta\_2)$에 대하여, 

$$d_2(x,z)\leq d_2(x,y)+d_2(y,z)\leq d_2(x,y)+\beta d_1(y,z)<d_2(x,y)+\beta\beta^{-1}\delta_2=\epsilon_2$$

가 성립하므로 $\mathcal{T}\_1$이 $\mathcal{T}\_2$보다 강하다. 즉, 두 위상은 서로 같다. 
</details>

$\rho$와 $d$의 정의로부터

$$\rho(x,y)\leq d(x,y)\leq\sqrt{n}\rho(x,y)$$

가 성립한다는 것은 자명하므로, 위 명제에 따르면 $\rho$와 $d$는 같은 위상을 준다. 사실 이는 그림으로 보면 좀 더 직관적인데, 우선 $\rho$와 $d$에 의해 만들어지는 basis의 원소들의 모양은 다음과 같다.

![metric_compare_1](/assets/images/Topology/Topology_on_R-2.png){:width="200px"  class="invert" .align-center}

그런데, 이 사각형과 원들을 모아둔 집합은 서로를 덮을 수 있다.

![metric_compare_2](/assets/images/Topology/Topology_on_R-3.png){:width="320px"  class="invert" .align-center}

더 일반적으로, 멀리 떨어진 점들이 멀리 떨어져있다는 사실만 기억하면, 이들이 얼마나 떨어져 있는지는 잊어버리더라도 동일한 위상을 만들 수 있다.

<div class="proposition" markdown="1">

<ins id="pp3">**명제 3**</ins> $(X,d)$가 metric space라 하자. $\overline{d}:X\times X\rightarrow\mathbb{R}$을 다음의 식

$$\overline{d}(x,y)=\min\{d(x,y), 1\}$$

으로 정의하면, $\overline{d}$는 $d$와 동일한 위상을 만든다.
</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $\overline{d}$가 metric임을 보여야 한다. 여기에서 자명하지 않은 부분은 삼각부등식 뿐이다. 즉, 다음의 식

$$\overline{d}(x,z)\leq\overline{d}(x,y)+\overline{d}(y,z)$$

을 보여야 한다. 만일 $\overline{d}(x,y)$와 $\overline{d}(y,z)$ 중 하나라도 1이 된다면 우변은 1보다 크거나 같고, 좌변은 1보다 작으므로 이 경우는 자명하다. 따라서 둘 모두가 1보다 작은 경우를 생각하자. 즉,

$$\overline{d}(x,y)=d(x,y)<1,\quad\overline{d}(y,z)=d(y,z)<1$$

이다. 그럼

$$\overline{d}(x,z)\leq d(x,z)\leq d(x,y)+d(y,z)=\overline{d}(x,y)+\overline{d}(y,z)$$

이므로 삼각부등식이 성립한다.

그런데 metric topology는 $\epsilon<1$인 $\epsilon$-ball들을 basis로 보아도 동일한 위상이 생기고, $d$와 $\overline{d}$의 $\epsilon<1$인 $\epsilon$-ball들은 정확히 같으므로 $d$에 의해 만들어지는 위상과 $\overline{d}$에 의해 만들어지는 위상이 동일하다.

</details>

이를 $d$에 대응되는 *standard bounded metric*이라 부른다. 사실, 만약 우리가 이 거리라는 값 자체에 신경을 썼었다면, 우리가 흔히 위상수학을 소개할 때 두는 커피잔과 도넛의 예시 등등은 애초에 성립하지도 않았을 것이다.

우리는 연속함수를 소개하며, 연속함수의 정의가 미적분학에서 배우는 $\epsilon$-$\delta$ 정의를 확장하는 개념이라는 것을 언급한 적이 있다. 실제로, metric topology들 사이의 함수들의 연속성은 *정확히* $\epsilon$-$\delta$ 정의로 주어진다.

<div class="proposition" markdown="1">

<ins id="pp4">**명제 4**</ins> $X$, $Y$가 metric $d_X$, $d_Y$를 갖는 metric space들이라 하고, $f:X\rightarrow Y$라 하자. 그럼 $f$가 연속인 것은 임의의 $x\in X$와 $\epsilon>0$에 대하여, 다음의 문장
  
> $d\_X(x, y)<\delta$이면 $d\_Y(f(x), f(y))<\epsilon$이다.    
  
가 성립하도록 하는 $\delta>0$이 항상 존재하는 것과 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $f$가 연속이라 하자. 그럼 임의의 $x\in X$와 $\epsilon>0$에 대하여, 집합
  
$$f^{-1}(B_{d_Y}(f(x), \epsilon))$$

는 열린집합의 preimage이므로 열린집합이다. 따라서 어떠한 $\delta>0$이 존재하여 $B\_{d\_X}(x,\delta)\subset f^{-1}(B\_{d\_Y}(f(x),\epsilon))$이 성립한다. 이제 만일 $y\in B\_{d\_X}(x,\delta)$라면, 즉 만일 $d\_X(x,y)<\delta$라면, $y\in f^{-1}(B\_{d\_Y}(f(x), \epsilon))$이므로 $f(y)\in B\_{d\_Y}(f(x), \epsilon)$이다.

반대로 $\epsilon$-$\delta$ 조건이 만족되었다고 하자. $f$가 연속임을 보이기 위해, 임의의 열린집합 $V\subset Y$를 택하고 $f^{-1}(V)$가 $X$에서 열린집합임을 보여야 한다. $x\in f^{-1}(V)$라 하자. 그럼 $f(x)\in V$이므로, 어떤 $\epsilon>0$이 존재하여 $B\_{d\_Y}(f(x),\epsilon)\subset V$이도록 할 수 있다. 이제 $\epsilon$-$\delta$ 조건에 의해, 어떠한 $\delta>0$이 존재하여 $y\in B\_{d\_X}(x,\delta)$이면 $f(y)\in B\_{d\_Y}(f(x), \epsilon)\subset V$이도록 할 수 있고, 따라서 $y\in f^{-1}(V)$이다. 즉, $B\_{d\_X}(x,\delta)\subset f^{-1}(V)$이므로 $f^{-1}(V)$도 열린집합이다. 


</details>

뿐만 아니라, 우리는 미적분학때 함수의 연속성을 판단하기 위해 사용했던 많은 정리들도 그대로 가져올 수 있다. 예를 들면, 우리는 수열판정법을 증명할 수 있는데, 그걸 위해선 다음의 보조정리를 먼저 증명해야 한다.  

<div class="proposition" markdown="1">

<ins id="lem5">**보조정리 5 (The sequence lemma)**</ins> 위상공간 $X$에 대하여, $A\subset X$라 하자. 만일 어떠한 $x\in A$에 대하여, $A$의 원소들로 이루어진 수열 $\left(x\_n\right)\_{n=1}^\infty$이 존재하여 $x_n\rightarrow x$라면 $x\in\operatorname{cl}A$가 성립한다. 만일 $X$가 metrizable이라면 그 역도 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $x\_n\rightarrow x$라 하자. 그럼 정의에 의하여, $x$의 임의의 열린근방은 반드시 어떠한 $x\_n$을 포함하고, 이는 $A$의 원소이므로 $x$의 임의의 열린근방은 반드시 $A$와 만난다. 따라서 [§수열의 수렴, 명제 2](/ko/math/topology/basic_definition_3#pp2)에 의해 $x\in\operatorname{cl}A$이다.

이제 $X$가 metrizable이라 가정하고 그 역을 보이자. 임의의 $x\in\operatorname{cl}A$에 대하여, 우리는 $x$로 수렴하는 $A$의 수열 $\left(x\_n\right)\_{n=1}^\infty$를 만들어야 한다. 각각의 $n$에 대하여, $B(x,1/n)$을 생각하자. 그럼 $x\in\operatorname{cl}A$이므로 이들은 $A$와 어떤 점에서 만난다. $B(x,1/n)\cap A$의 점들 중 하나를 뽑아 이를 $x\_n$이라 하자. 그럼 $x\_n\rightarrow x$이다. 만일 우리가 $x$의 임의의 열린근방 $U$를 잡는다면, $U$는 어떠한 $\epsilon$에 대하여 $B(x,\epsilon)$을 포함하고, 따라서 $1/N<\epsilon$이도록 하면 $n\geq N$일 때마다 $x\_n\in B(x,\epsilon)\subset U$이도록 할 수 있기 때문이다.

</details>
<div class="proposition" markdown="1">

<ins id="pp6">**명제 6**</ins> 두 위상공간 $X$, $Y$에 대하여 $f:X\rightarrow Y$라 하자. 만일 $f$가 연속이라면, 임의의 $x\in X$에 대해 $x\_n\rightarrow x$을 만족하는 수열 $\left(x_n\right)\_{n=1}^\infty$는 $f(x_n)\rightarrow f(x)$ 또한 만족한다. 만일 $X$가 metrizable이라면, 그 역 또한 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $f$가 연속이라 가정하자. $x\_n\rightarrow x$인 수열 $\left(x\_n\right)\_{n=1}^\infty$에 대하여, 우리는 $f(x\_n)\rightarrow f(x)$임을 보여야 한다. $f(x)$의 열린근방 $V$를 생각하자. 그럼 $f^{-1}(V)$는 $x$를 포함하는 열린집합이다. 따라서 어떠한 $N$이 존재하여, $n\geq N$이면 $x\_n\in f^{-1}(V)$가 성립하도록 할 수 있다. 즉, $f(x\_n)\in V$가 모든 $n\geq N$에 대해 성립하므로 $f(x\_n)\rightarrow f(x)$이다.

반대로 $A\subset X$이고 뒤쪽 조건이 성립한다고 하자. 우리는 연속함수의 동치조건 ([§연속함수, 명제 2](/ko/math/topology/basic_definition_4#pp2)) 중 $f(\operatorname{cl}A)\subset\operatorname{cl}f(A)$를 이용할 것이다. 앞선 보조정리의 역에 의하여, 만일 $x\in \operatorname{cl}A$라면 $x$로 수렴하는 $A$의 수열 $\left(x\_n\right)\_{n=1}^\infty$가 존재한다. 그런데 가정에 의하여 $f(x\_n)\rightarrow f(x)$이고, 따라서 다시 앞선 보조정리에 의해 $f(x)\in \operatorname{cl}f(A)$가 성립한다. 따라서 $f(\operatorname{cl}A)\subset\operatorname{cl}f(A)$가 성립한다.

</details>

위의 [보조정리 5](#lem5)와 [명제 6](#pp6), 그리고 앞으로 살펴볼 수열과 관련된 정리들은 metrizable한 위상공간에서 성립하는 것이 보통이다. 그러나 이를 *net*이라는 새로운 개념을 도입하면 일반적인 위상공간으로 확장할 수 있는데, 이 내용은 우리가 더 많은 위상적인 성질을 다룬 후에 살펴보기로 한다. **[Mun]**에서도 이를 Chapter 3 이후의 supplementary exercise로 빼 두었다.

한편, 미적분학 때 $\epsilon$-$\delta$ 정의를 배우면 가장 먼저 증명하는 다음의 명제가 있다.

<div class="proposition" markdown="1">

<ins id="pp7">**명제 7**</ins> 위상공간 $X$에 대하여, 만일 $f,g:X\rightarrow\mathbb{R}$이 연속이라면 $f+g$, $f-g$, $fg$ 또한 마찬가지이다. 만일 $g$가 모든 $x$에 대하여 $0$이 아니라면, $f/g$ 또한 연속이다.

</div>

그러나 앞선 명제들과는 다르게, 이건 일반적인 metric space로 확장될 수는 없다는 것이 당연하다. 덧셈이나 뺄셈 등의 *연산*을 갖고 있는 것은 metric space의 조건이 아니라, 실수의 성질이기 때문이다. 이렇게 연산이 주어진 대수적인 구조 위에 위상공간의 구조가 추가된 상황은 별도의 글로 살펴보기로 한다.

## Uniform convergence

한편, 우리는 위상공간 $X$에서 $T_1$ 공간 $Y$로 가는 연속함수들의 수열 $(f_n)$이 함수 $f:X\rightarrow Y$로 수렴하더라도 $f$가 연속은 아닐 수 있다는 것을 관찰한 적이 있다. ([§연속함수, 예시 5](/ko/math/topology/basic_definition_4#ex5)) 우리는 거리를 정의하면 이 문제를 해결할 수 있다고 언급했었는데, 이제 모든 준비를 마쳤다. 

<div class="definition" markdown="1">

<ins id="df8">**정의 8**</ins> $f\_n:X\rightarrow Y$가 집합 $X$에서 metric space $Y$로의 함수들의 수열이라 하자. 그럼 $\left(f\_n\right)\_{n=1}^\infty$이 $f:X\rightarrow Y$로 *uniformly converge<sub>균등수렴</sub>*한다는 것은, 임의의 $\epsilon>0$이 주어졌을 때, 적당한 $N$이 존재하여 
  
$$d(f_n(x), f(x))<\epsilon$$

이 모든 $x\in X$와 $n>N$에 대해 성립하는 것이다. 이를 기호로 $f_n\rightrightarrows f$로 표기한다.

</div>

사실 이 정의는 꽤나 부자연스럽기도 하고, $Y$가 metric space라는 조건은 과하기도 하다. 적절한 일반화를 통해 이러한 문제점들을 모두 해결할 수 있지만 이는 uniform continuity를 소개한 이후로 미룬다. 

어쨌든 이 조건 하에서는 앞서 언급한 예시와 같은 일은 일어나지 않는다.

<div class="proposition" markdown="1">

<ins id="pp9">**명제 9**</ins> $X$가 위상공간이고, $Y$가 metric space라 하자. 만일 연속함수들 $f\_n$에 대해 $f\_n\rightrightarrows f$라면 $f$는 연속이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$V$가 $Y$의 열린집합이라 하고, $x\_0\in f^{-1}(V)$라 하자. 우리는 $f^{-1}(V)$가 열린집합임을 보이기 위해, 어떠한 $x\_0$의 열린근방 $U$가 존재하여 $f(U)\subset V$임을 보여야 한다.

$y\_0=f(x\_0)$이라 하자. $V$는 열린집합이므로, 어떠한 $\epsilon$이 존재하여 $B(y\_0, \epsilon)\subset V$이다. 이제 $f\_n\rightrightarrows f$이므로, 어따한 $N$이 존재하여, 다음의 식

$$d(f_n(x), f(x))<\epsilon/3$$

이 모든 $n>N$과 $x\in X$에 대해 성립하도록 할 수 있다. 한편, $f\_N$은 연속이므로, $f\_N^{-1}(B(f\_N(x\_0), \epsilon/3))$은 열린집합이고, 따라서 $x\in U\subset f\_N^{-1}(B(f\_N(x\_0), \epsilon/3))$인 열린집합 $U$가 존재한다. 이제 임의의 $x\in U$에 대하여,

$$\begin{aligned}
  d(f(x), f(x_0))&\leq d(f(x), f_N(x))+d(f_N(x), f_N(x_0))+d(f_N(x_0), f(x_0))\\
  &<\epsilon/3+\epsilon/3+\epsilon/3=\epsilon
\end{aligned}$$

이므로 $f(x)\in B(y\_0,\epsilon)\subset V$이다. 즉, $f(U)\subset B(y\_0,\epsilon)\subset V$이므로 $f^{-1}(V)$가 열린집합이다.

</details>



---

**참고문헌**

**[Mun]** J.R. Munkres, <i>Topology</i>. Featured Titles for Topology. Prentice Hall, Incorporated, 2000.

---

