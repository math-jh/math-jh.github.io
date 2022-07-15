---

title: "수열의 수렴"
excerpt: "기본정의 3: 수열의 수렴"

categories: [Math / Topology]
permalink: /ko/math/topology/basic_definition_3
header:
    overlay_image: /assets/images/Topology/Topological_basis.png
    overlay_filter: 0.5
sidebar: 
    nav: "topology-ko"

date: 2021-09-21
last_modified_at: 2022-04-07
weight: 3

---


## 집합의 interior와 closure

위상공간 $(X,\mathcal{T})$가 주어졌다고 하자. $X$의 임의의 부분집합 $A$에 대하여, <box>$A$를 포함하는 닫힌집합</box>과 <box>$A$에 포함되어 있는 열린집합</box>이 항상 존재한다. ($X$와 $\emptyset$). 한편, 닫힌집합들의 임의의 교집합은 닫힌집합이고 ([§열린집합과 닫힌집합, 명제 8](/ko/math/topology/basic_definition_1#pp8)의 증명), 열린집합들의 임의의 합집합은 열린집합이므로, <box>$A$를 포함하는 가장 작은 닫힌집합</box>과 <box>$A$에 포함된 가장 큰 열린집합</box>이 모두 존재한다. 이들을 다음과 같이 정의한다.

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> 위상공간 $X$의 임의의 부분집합 $A$에 대하여, $A$를 포함하는 가장 작은 닫힌집합을 $A$의 *closure<sub>폐포</sub>*, $A$에 포함된 가장 큰 열린집합을 $A$의 *interior<sub>내부</sub>*라 부르고, 이를 각각 $\operatorname{cl}(A)$와 $\operatorname{int}(A)$로 적는다. 

</div>

이렇게 정의하면 두 연산자 $\mathrm{cl}$과 $\mathrm{int}$가 포함관계를 유지한다는 것은 자명하다. 

다음의 식

$$\operatorname{int}(A^c)=(\operatorname{cl}(A))^c$$

을 증명해보자. 정의에 의해, $\operatorname{int}(A^c)$는 $A^c$에 포함된 열린집합 중 가장 큰 것이고, 이는 $A$를 포함하지 않는 열린집합 중 가장 큰 것이라는 말과 동일하다. 한편 $\operatorname{cl}(A)$는 $A$를 포함하는 닫힌집합 중 가장 작은 것이고, 따라서 $(\operatorname{cl}(A))^c$는 $A$를 포함하지 않는 열린집합 중 가장 큰 것이 되어 이 둘은 동일해야 한다. 우리는 이 집합을 $A$의 *exterior<sub>외부</sub>*라 부른다.

위와 같은 논증을 통해 interior와 closure, exterior 중 어느 하나만 있더라도 다른 둘을 만들 수 있다는 것을 안다. 따라서, 이들 중 하나만 택하여 이론을 만들어내면 나머지 둘에 대한 것도 따라온다. 우리는 closure에 대한 내용을 택하기로 한다.

<div class="proposition" markdown="1">

<ins id="pp2">**명제 2**</ins> 위상공간 $X$와 부분집합 $A$에 대하여, 두 조건 

1. $x\in\operatorname{cl}A$인 것,
2. $x$의 임의의 열린근방 $U$가 $A$와 만나는 것

이 서로 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

대우명제를 보이는 것이 편하다. $x\not\in\operatorname{cl}A$라 하자. 그럼 $x\in(\operatorname{cl}A)^c=\operatorname{ext}A$는 $x$를 포함하며, $\operatorname{cl}A$와 만나지 않는 열린집합이고, 따라서 $A$와도 만나지 않는 열린집합이 된다. 즉, 명제 "$A$와 만나지 않는 $x$의 어떠한 neighborhood가 존재한다"가 참이다. 

거꾸로, 어떠한 $x$의 열린근방 $U$가 존재하여 $U\cap A=\emptyset$이라면, $U^c\cap A=A$이므로 $U^c$는 $A$를 포함하는 닫힌집합이고, closure의 최소성에 의하여 $U^c$는 $\operatorname{cl}A$ 또한 포함한다. 즉, $x\not\in U^c$이면 $x\not\in\operatorname{cl}A$이고, 따라서 반대방향도 성립한다.  

</details>

이 상황을 조금만 자세히 살펴보자.

<div class="definition" markdown="1">

<ins id="df3">**정의 3**</ins> 위상공간 $X$의 임의의 부분집합 $A$에 대하여, $A$의 *boundary<sub>경계</sub>*는 다음의 식

$$\partial A=\operatorname{cl}A\setminus\operatorname{int}A$$

으로 정의되는 집합 $\partial A$이다. 

</div>

$\partial A$를 정의하고 나면, closure를 조금 더 직관적으로 이해할 수 있다. 

$$A\cup\partial A=A\cup(\operatorname{cl}A\setminus\operatorname{int}A)=A\cup\operatorname{cl}A=\operatorname{cl}A$$

이므로 closure란 집합 $A$에, $A$의 boundary point를 더하여 만들어진 닫힌집합이다. 물론 boundaary라는 것을 closure를 통해 정의하였으므로, 이를 그냥 받아들이는 것은 순환논법이다. 

<div class="definition" markdown="1">

<ins id="df4">**정의 4**</ins> 위상공간 $X$와 $X$의 임의의 부분집합 $A$에 대하여, $x\in X$가 $A$의 *limit point<sub>극한점</sub>*이라는 것은 $x$의 임의의 열린근방이 $x$ 자기 자신을 제외한 점에서 $A$와 만나는 것이다. 

</div>

$A$의 모든 limit point들의 집합을 $A$의 *derived set<sub>도집합</sub>*이라 부르고, $A'$로 적는다. 그럼 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="pp5">**명제 5**</ins> 위상공간 $X$와 $X$의 임의의 부분집합 $A$에 대하여, 다음의 식

$$\operatorname{cl}A=A\cup A'$$

가 항상 성립한다.
</div>

다만 이 명제가 성립한다 해서 limit point와 boundary point가 같은 것은 아니다.

<div class="remark" markdown="1">

<ins id="rmk1">**참고**</ins> 집합 $X=\\{x,y,z\\}$ 위에 위상 $\mathcal{T}_1$을 다음의 식

$$\mathcal{T}_1=\{\emptyset, \{y\},\{z\},\{y,z\},X\}$$

으로 주자. 그럼 $\\{x\\}$는 닫힌집합이므로, $\operatorname{cl}\\{x\\}=\\{x\\}$이다. 또, $\\{x\\}$에 포함된 유일한 열린집합이 $\emptyset$뿐이므로, $\operatorname{int}\\{x\\}=\emptyset$이고 따라서 $\partial\\{x\\}=\\{x\\}$이다. 그러나, $x$를 포함하는 열린집합은 *반드시* $x$에서만 $\\{x\\}$와 만날 수 있으므로, $\\{x\\}$는 limit point를 갖지 않는다. 

반대방향도 일반적으로 성립하지 않는다. 예를 들어, 실수집합 $\mathbb{R}$의 일반적인 위상에서 ([§위상공간의 기저, 정의 5](/ko/math/topology/basic_definition_2#df5)) $(a,b)$의 경계는 $\\{a,b\\}$뿐이지만, $(a,b)$ 안의 임의의 점은 모두 이 집합의 limit point이다.

</div>

<div class="proposition" markdown="1">

<ins id="lem6">**보조정리 6**</ins> 위상공간 $X$와 그 부분집합 $A$에 대하여, 

$$A'\setminus A=\partial A\setminus A$$

가 항상 성립한다.
</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $x\in A'\setminus A$라 하자. $x\in A'$이므로, $x$의 임의의 열린근방 $U$는 $A$와 $x$가 아닌 점에서 만나고, 따라서 [명제 2](#pp2)에 의하여 $x\in\operatorname{cl}A$가 성립한다. 그런데 주어진 조건에서 $x\not\in A$이므로, 

$$x\in\operatorname{cl}A\setminus A\subset\operatorname{cl}A\setminus\operatorname{int}A=\partial A$$

가 성립한다. 

이제 반대로 $x\in\partial A\setminus A$라 하자. $\operatorname{int}A\subset A$이므로, 

$$\partial A\setminus A=(\operatorname{cl}A\setminus\operatorname{int}A)\setminus A=\operatorname{cl}A $$

가 성립한다. 따라서, $x\in\operatorname{cl}A$이고, 그럼 다시 [명제 2](#pp2)에 의하여 $x$의 임의의 열린근방 $U$는 $A$와 만난다. 그런데, 주어진 조건에서 $x\not\in A$이므로, $U$는 어차피 $x$에서는 $A$와 만날 수 없고, 따라서 $U$는 *반드시* $x$가 아닌 다른 점에서 $A$와 만나야 한다. 즉, $x\in A'$이고, 따라서 $x\in A'\setminus A$가 성립한다.
</details>

<details class="proof--alone" markdown="1">
<summary>명제 5의 증명</summary>

위의 보조정리에서, $A'\setminus A=\partial A\setminus A=\operatorname{cl}A\setminus A$이다. 그런데, $\operatorname{cl}A\supset A$이므로, $(\operatorname{cl}A\setminus A)\cup A=\operatorname{cl}A$이고 따라서

$$A'\cup A=(A'\setminus A)\cup A=(\operatorname{cl}A\setminus A)\cup A=\operatorname{cl}A$$

가 성립한다.
</details>

## 수열의 수렴

<div class="definition" markdown="1">

<ins id="df7">**정의 7**</ins> 위상공간 $X$와, $X$ 위의 점들로 이루어진 수열 $(x_n)_{n=1}^\infty$이 점 $x$로 *수렴<sub>converge</sub>*한다는 것은 $x$의 임의의 열린근방 $U$가 주어질 때마다, 적절한 자연수 $N$이 존재하여

$$n\geq N\implies x_n\in U$$

가 참인 것이다. 

</div>

$X$가 standard toplogy가 주어진 $\mathbb{R}$이었다면 이 정의는 $\epsilon$-$N$ 정의와 동일하다. 하지만 우리가 알고 있던 수렴하는 수열과는 다른 성질이 많은데, 예를 들어 만일 $X$가 trivial topology가 주어진 공간이었다면 $X$ 위에서 정의된 임의의 수열은 항상 수렴할 뿐만 아니라 그 수렴값 또한 $X$의 임의의 원소가 될 수 있다. 이러한 상황을 배제하기 위해서는 두 점을 분리하는 열린집합이 있어야 한다는 것을 쉽게 깨달을 수 있다. 

<div class="definition" markdown="1">

<ins id="df8">**정의 8**</ins> 위상공간 $X$가 주어졌다 하자.

1. $X$가 *$T_0$ 공간*이라는 것은 $X$의 임의의 두 점이 topologically distinguishable한 것이다.
2. $X$가 *$T_1$ 공간*이라는 것은 $X$의 임의의 두 점 $x,y$에 대하여, $x$를 포함하지만 $y$를 포함하지 않는 열린집합과 $y$를 포함하지만 $x$를 포함하지 않는 열린집합이 존재하는 것이다.
3. $X$가 *$T_2$ 공간* 혹은 *Hausdorff 공간*이라는 것은 $X$의 임의의 두 점 $x,y$에 대하여, 서로소인 $x$와 $y$의 열린근방 $U,V$가 존재하는 것이다.

</div>

$T_0$ 공간, $T_1$ 공간을 각각 *Kolmogorov 공간*, *Fréchet 공간*이라고 부르기도 하지만 $T_2$를 뜻하는 말인 Hausdorff 공간에 비하면 많이 쓰이지는 않는다. 특히 후자의 경우 같은 이름을 사용하는 전혀 다른 Fréchet 공간 또한 존재하므로 지양하는 것이 좋다.

위상공간 $X$에 topologically indistinguishable한 두 점 $x,y$가 존재한다면, $x$로 수렴하는 수열과 $y$로 수렴하는 수열을 구별할 수 없음은 자명하다. 뿐만 아니라 $T_0$ 공간에서도 수열이 한 점 이상으로 수렴할 수 있다. 예를 들어 이전 글에서 살펴본 $X=\\{x,y\\}$ 위에서의 topology $\mathcal{T}=\\{\emptyset,\\{x\\},X\\}$의 경우 다음의 수열

$$x,y,x,y,\cdots$$

는 $y$로 수렴하는 수열이다. 이는 $y$의 열린근방이 $X$ 뿐이기 때문이다. 반면, 이 수열은 $x$로 수렴하지는 않는데, $x$의 열린근방 $\\{x\\}$에 대해서는 [정의 7](#df7)의 조건이 만족되지 않기 때문이다. 반면,

$$x,x,x,x,\cdots$$

는 $x$로 수렴하는 수열인 동시에 $y$로 수렴하는 수열이기도 하다. 

<div class="proposition" markdown="1">

<ins id="pp9">**명제 9**</ins> 위상공간 $X$가 $T_1$이라면 임의의 singleton $\\{x\\}$는 닫힌집합이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$X\setminus\\{x\\}$가 열린집합임을 보이면 충분하다. 그런데 임의의 $y\in X\setminus\\{x\\}$에 대하여, $y$를 포함하지만 $x$는 포함하지 않는 열린집합 $U$가 존재한다. 이렇게 우리는 $X\setminus\\{x\\}$의 임의의 점 $y$에 대하여 $X\setminus\\{x\\}$에 포함되는 $y$의 열린근방 $U$를 항상 찾을 수 있으므로 $X\setminus\\{x\\}$는 열린집합이다.

</details>

닫힌집합의 임의의 유한한 합집합은 닫힌집합이므로, 위 명제에 의하여 $T_1$ 공간의 임의의 유한한 부분집합은 항상 닫힌집합이다. 한편 이 명제를 이용하면 우리가 정의했던 limit point에 대한 성질을 하나 추가할 수 있다.

<div class="proposition" markdown="1">

<ins id="crl10">**따름정리 10**</ins> $T_1$ 공간 $X$와, 임의의 부분집합 $A$가 주어졌다 하자. 그럼 $x\in X$가 $A$의 limit point인 것은 $x$의 임의의 열린근방이 무한히 많은 $A$의 점을 포함하는 것과 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선, $x$의 임의의 열린근방이 $A$의 무한히 많은 점을 포함한다면, 자기 자신과 다른 점에서 $A$와 만나는 것은 자명하므로 반대방향만 증명하면 충분하다.

$x$가 $A$의 limit point라 하고, 결론에 반하여 $x$의 어떤 neighborhood $U$가 $A$와 유한하게 많은 점에서만 만난다고 하자. $x$ 자기 자신을 제외하고, $U$가 $A$와 만나는 점을 $x_1,\ldots, x_n$이라 하면 $X$가 $T_1$이므로 $\\{x_1,\ldots, x_n\\}$은 닫힌집합이고 따라서 다음의 집합

$$U\setminus\{x_1,\ldots, x_n\}=U\cap\bigl(X\setminus\{x_1,\ldots, x_n\}\bigr)$$

은 열린집합이 된다. 이제 $U\setminus\\{x_1,\ldots, x_n\\}$은 $x$를 포함하는 열린집합이고 $A$와는 많아봐야 $x$에서만 만나므로 $x$가 $A$의 limit point라는 가정에 모순이 되어 원하는 결론을 얻는다.

</details>

---

**참고문헌**

**[Mun]** J.R. Munkres, <i>Topology</i>. Featured Titles for Topology. Prentice Hall, Incorporated, 2000.

---

