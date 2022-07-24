---
title: "거리위상 (1)"
excerpt: "순서위상과 거리위상"

categories: [Math / Topology]
permalink: /ko/math/topology/metric_topology_1
header:
    overlay_image: /assets/images/Topology/Topological_basis.png
    overlay_filter: 0.5
sidebar: 
    nav: "topology-ko"

date: 2021-09-24
last_modified_at: 2022-04-07
weight: 6
    
---

우리는 이전에 실수집합 위에 standard topology를 정의했었다. 사실 위상공간의 여러가지 성질들은 실수집합이 갖고 있는 성질 중 일부만 별도로 분리해서 얻어진 것이기 때문에 실수집합을 자세히 들여다보는 것이 이러한 성질들의 이해에 큰 도움이 된다. 이 중 가장 큰 성질은 당연히 *거리*의 개념이지만, 이를 살펴보기 전에 잠깐 *order topology*를 정의한다. 


## 순서위상

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> Totally ordered set $(X,<)$ 위에 정의된 *order topology<sub>순서위상</sub>*은 다음의 집합 

$$\{(a,b)\subseteq X:\text{$a<b$, $a$ or $b$ can be possibly infinite}\}$$

을 basis로 하여 정의된 위상이다.

</div>

역시 이 경우에도 위 집합이 basis가 된다는 것을 보이기는 해야하지만, 어렵지 않으므로 우리는 생략한다. $\mathbb{R}$때와는 다르게, $a$ 혹은 $b$가 $\pm\infty$인 경우도 추가되었다. 예를 들어 만일 $X$가 least element $c$를 갖는다면, $[c,d)$는 $(a,b)$의 꼴들만 모아둔 집합을 기저로 삼는다면 열린집합이 아닐 것이지만, 우리는 이러한 집합도 열린집합으로 취급하길 원하기 때문에 이렇게 $\pm\infty$를 허용하였다. 이 경우 표기법 $(-\infty, d)$는 <#ref#> 직전에 정의했던 unbounded open interval과 동일한 표기이다.

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins> $\mathbb{N}$과 $\mathbb{Z}$ 위에 정의된 order topology는 정확하게 discrete topology와 같다. 임의의 $n\in\mathbb{N}$ 혹은 $n\in\mathbb{Z}$에 대하여, $n\in (n-1,n+1)$이기 때문이다. 물론, 만일 $n=0$이라면, $\mathbb{N}$에서 이 집합은 $(-\infty, 1)$인 것으로 이해한다.
</div>

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> 임의의 ordinal은 totally ordered set이므로 여기에 order topology를 줄 수 있다. (<#ref#>) 
우리가 특히 관심을 갖는 경우는 *first uncountable ordinal*이다. 만일 이 집합이 가장 큰 원소를 갖는다면 이 원소를 하나 빼더라도 남는 집합은 여전히 uncountable이 되어 이 집합보다 앞선 uncountable ordinal이 존재하게 된다. 따라서 이 집합은 어떤 limit ordinal의 initial segment로 표현되어야 한다. 이 집합과 집합 위에 정의된 위상구조를 합쳐 $S\_\Omega$로 적는다.

</div>

## 거리위상의 정의

계속 강조해왔던 것과 같이, 실수의 가장 중요한 성질 가운데 하나는 이 집합이 *거리*개념을 갖는다는 것이다. 

<div class="definition" markdown="1">

<ins id="df4">**정의 4**</ins> 집합 $X$ 위에 주어진 *metric<sub>거리함수</sub>*는 다음의 조건을 만족하는 이변수함수 $d$이다.

1. 임의의 $x,y\in X$에 대하여 $d(x,y)\geq 0$이 성립하며, $d(x,y)=0$인 것은 $x=y$인 것과 동치이다.
2. 임의의 $x,y\in X$에 대하여, $d(x,y)=d(y,x)$가 성립한다.
3. 임의의 $x,y,z\in X$에 대하여, $d(x,y)+d(y,z)\geq d(x,z)$가 성립한다.

함수값 $d(x,y)$를 $x$와 $y$ 사이의 *거리<sub>distance</sub>*라고 부른다. 

</div>

마지막 조건을 *삼각부등식<sub>triangle inequality</sub>*라고도 부른다.

![triangle_inequality](/assets/images/Topology/Topology_on_R-1.png){:width="180px"  class="invert" .align-center}

이렇게 metric이 주어지면, 다음과 같은 *$\epsilon$-ball*들을 만들 수 있다. 

$$B(x,\epsilon)=\{y:d(x,y)<\epsilon\}$$ 

만일 $X=\mathbb{R}$이었다면 위 집합은 열린구간 $(x-\epsilon, x+\epsilon)$에 해당했을 것이다. 간혹 우리가 어떤 공간에 있는지를 신경써야 할 때에는, 위 집합을 $B\_d(x,\epsilon)$과 같이 쓰기도 한다.

구간을 일반화하는 것이 $\epsilon$-ball들이라 하였으므로, 이들을 basis로 삼을 생각을 하는 것은 당연한 일이다.

<div class="definition" markdown="1">

<ins id="df5">**정의 5**</ins> 집합 $X$ 위에 metric $d$가 정의되었다고 하면, $B\_d(x,\epsilon)$들의 모임을 basis로 하여 만들어지는 위상을 $d$에 의해 만들어지는 *metric topology<sub>거리위상</sub>*이라 부른다.

</div>

이 경우에도 $\epsilon$-ball들이 실제로 basis의 조건을 만족한다는 것을 증명해야 한다. 사실 이 또한 어렵지는 않지만, 새로운 용어들에 익숙해질 겸 직접 증명해보기로 한다. 

<div class="proposition" markdown="1">

<ins id="lem6">**보조정리 6**</ins> 임의의 $y\in B(x,\epsilon)$에 대하여, 적당한 양수 $\delta>0$이 존재하여 $B(y,\delta)\subseteq B(x,\epsilon)$이도록 할 수 있다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$\delta=\epsilon-d(x,y)$라 하자. 그럼 삼각부등식에 의하여, 임의의 $z\in B(y,\delta)$에 대해

$$d(x,z)\leq d(y,z)+d(x,y)<(\epsilon-d(x,y))+d(x,y)=\epsilon$$

이 성립하므로, $z\in B(x,\epsilon)$이 성립한다.

</details>

<div class="proposition" markdown="1">

<ins id="pp7">**명제 7**</ins> Metric $d$가 주어진 임의의 집합 $X$에 대하여, $B(x,\epsilon)$들의 모임은 basis의 조건을 만족한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 임의의 $x\in X$에 대하여 $B(x,1)$은 항상 $x$를 포함하므로 $B(x,\epsilon)$들의 모임이 $X$를 덮는 것은 자명하다. 

공집합이 아닌 교집합을 갖는 임의의 두 ball $B\_1=B(x\_1,\epsilon\_1)$과 $B\_2=B(x\_2,\epsilon\_2)$가 주어졌다고 하자. 그럼 임의의 $y\in B\_1\cap B\_2$에 대하여, 앞선 보조정리에 의해 $B(y, \delta\_1)\subseteq B\_1$, $B(y,\delta\_2)\subseteq B\_2$이도록 하는 $\delta\_1, \delta\_2$가 각각 존재한다. 이제 $\delta=\min(\delta\_1,\delta\_2)$로 두면, 

$$B(y, \delta)\subseteq B(y, \delta_i)\subseteq B(x, \epsilon_i)$$

가 $i=1,2$에 대해 성립하므로 원하는 결과를 얻는다.

</details>

위 두 명제들은 단순히 주어진 집합이 basis라는 것을 보일 때 뿐만 아니라, 종종 필요할 때 꺼내 쓸 명제이기도 하다. 한편, [보조정리 6](#lem6)을 적용하면 임의의 $x\in X$와 양수 $r>0$에 대하여, 집합 $B(x,r)$의 임의의 원소 $y$마다 적당한 $\delta_y>0$이 존재하여 $B(y,\delta_y)\subseteq B(x,r)$이도록 할 수 있으므로 다음의 식

$$B(x,r)=\bigcup_{y\in B(x,r)} B(y, \delta_y)$$

이 성립한다. 이 때 $\delta_y$의 값을 모두 1보다 작거나 같도록 고정해줄 수 있고, 이렇게 제한한 open ball들의 모임 또한 basis의 조건을 만족한다는 것을 쉽게 생각할 수 있다.

<div class="example" markdown="1">

<ins id="ex8">**예시 8**</ins> 앞서 정의한 $\mathbb{R}$의 standard topology는 metric topology와 같다. Metric을 $d(x,y)=\lvert x-y\rvert$으로 정의하면, $\mathcal{B}$의 각 원소들 $(a,b)$는 모두 open ball들 $B\_d(\frac{a+b}{2}, \frac{b-a}{2})$으로 쓸 수 있고, 거꾸로 임의의 open ball $B\_d(x,\epsilon)$은 $(x-\epsilon, x+\epsilon)$이기 때문이다.

</div>
<div class="example" markdown="1">

<ins id="ex13">**예시 13**</ins> 임의의 집합 $X$ 위에 주어진 discrete topology 또한 metric으로 표현할 수 있다. $d:X\times X\rightarrow\mathbb{R}$을 다음의 식 

$$d(x,y)=\begin{cases}0&x=y\\ 1&x\neq y\end{cases}$$

으로 정의하면, $d$는 자명하게 metric이며, $B(x,1/2)=\\{x\\}$가 임의의 $x$에 대해 성립하기 때문이다.
</div>

그러나, 주어진 위상공간 $(X,\mathcal{T})$를 metric topology으로 만드는 metric $d$가 존재한다는 것은 일반적으로 참이 아니다. 우리는 이러한 특징을 갖는 위상공간에 다음과 같은 이름을 붙인다. 

<div class="definition" markdown="1">

<ins id="df14">**정의 14**</ins> 위상공간 $(X,\mathcal{T})$에 대하여, $X$ 위에 어떠한 metric $d$가 존재하여, $\mathcal{T}$가 이 metric $d$에 의해 만들어지는 metric topology와 동일하도록 할 수 있다면 $(X,\mathcal{T})$가 *metrizable<sub>거리화 가능</sub>*하다고 하고, 이렇게 $d$가 부여된 구조 $(X,d)$를 *<sub>metric space</sub>*이라 부른다.

</div>

앞서 언급한 것과 같이, 일반적인 위상공간은 metrizable일 필요가 없다. 그러나 앞서 언급했듯 metric이라는 것은 위상이 가질 수 있는 가장 좋은 성질 중 하나에 속하기 때문에, metrizability를 판별하는 것이 중요하다. 이는 **[Mun]**의 전반부의 큰 목표 중 하나다. 하지만 이를 위해 필요한 도구가 아직 많이 부족하기 대문에, 다음 글에서는 metric topology가 갖는 좋은 성질들을 먼저 살펴보기로 한다. 

---

**참고문헌**

**[Mun]** J.R. Munkres, <i>Topology</i>. Featured Titles for Topology. Prentice Hall, Incorporated, 2000.

---

