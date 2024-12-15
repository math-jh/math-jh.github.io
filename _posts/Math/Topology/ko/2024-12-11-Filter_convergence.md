---

title: "필터의 수렴"
excerpt: ""

categories: [Math / Topology]
permalink: /ko/math/topology/filter_convergence
header:
    overlay_image: /assets/images/Math/Topology/Filter_convergence.png
    overlay_filter: 0.5
sidebar: 
    nav: "topology-ko"

date: 2024-12-11
last_modified_at: 2024-12-11
weight: 15

---

우선 다음을 정의한다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 위상공간 $X$가 *limit point compact*라는 것은 $X$의 모든 무한집합이 limit point를 갖는 것을 의미한다. ([§집합의 내부, 폐포, 경계, ⁋정의 8](/ko/math/topology/other_concepts#def8))

</div>

일반적으로 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="prop22">**명제 2**</ins> Compact space는 limit point compact이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

결론에 반하여 limit point compact가 아닌 compact space $X$를 가정하자. 그럼 limit point를 갖지 않는 무한집합 $A$가 존재하며, 따라서 [§집합의 내부, 폐포, 경계, ⁋정의 8](/ko/math/topology/other_concepts#def8) 이후의 논증에 의하여 $\cl(A)\setminus A=\emptyset$이어야 한다. 즉 $A$는 닫힌집합이어야 하고, 따라서 compact이다. 한편 각각의 $a\in A$ 또한 $A$의 limit point가 아니므로, $a$의 적당한 열린근방 $U_a$가 존재하여 $A\cap U_a=\\{a\\}$이도록 할 수 있다. 그럼 $(U\_a)\_{a\in A}$는 finite subcover를 갖지 않는 $A$의 open covering이므로 모순이다.

</details>

그러나 일반적으로 그 역은 성립하지 않는다.

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> Trivial topology가 주어진 two-point space $X$와, discrete topology가 주어진 무한집합 $Y$을 생각하자. 그럼 $X\times Y$는 limit point compact이지만 compact가 아니다.

</div>

또 다음을 정의한다.

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> 위상공간 $X$가 *sequentially compact*라는 것은 $X$의 임의의 점열이 수렴하는 부분점열을 갖는 것이다.

</div>

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> Sequentially compact space는 limit point compact이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$X$가 sequentially compact space라 하고, limit point를 갖지 않는 무한집합 $A$가 존재한다고 가정하자. 그럼 $A$의 적당한 countable subset $A'$를 택하여 이를 점열 $(x\_n)\_{n\geq k}$로 만들 수 있다. 그럼 $X$는 sequentially compact이므로 수렴하는 부분점열을 가지며, 이 점열이 $x$로 수렴한다 하면 $x$가 $A'$의 limit point가 되고 따라서 $A$의 limit point가 되는 것을 확인할 수 있다. 

</details>

## 점열의 수렴

한편, [명제 5](#prop5)의 역 또한 성립하지 않는다. 이는 다소 의외라고 느껴질 수 있는데, limit point compact인 공간의 임의의 점열 $(x\_n)$이 주어졌을 때, 집합 $A=\\{x_n:n\geq 1\\}$는 유한집합이 되어 자명한 이유로 수렴하는 부분점열을 갖거나, 혹은 무한집합이 되어 limit point를 갖기 때문이다. 문제는 집합 $A$의 limit point로 수렴하는 부분점열이 존재하지 않을수도 있다는 것에 있다. 

<div class="example" markdown="1">

<ins id="ex6">**예시 6**</ins> $\mathbb{R}$의 부분집합들의 모임

$$\mathcal{B}=\{(a,\infty): a\in \mathbb{R}\}$$

을 생각하면 이 모임은 [§위상공간의 기저, ⁋따름정리 6](/ko/math/topology/topological_bases#cor6)의 조건을 만족하고 따라서 $\mathbb{R}$ 위에 위상구조를 준다.

이렇게 정의된 위상공간 $\mathbb{R}$의 점열 $(x\_n)\_{n\geq 1}$을 다음의 식

$$x_n=-n$$

으로 정의하자. 그럼 $(x_n)$은 수렴하는 부분점열을 갖지 않는다. 반면 $A=\\{x_n:n\geq 1\\}$는 limit point를 갖는데, 가령 $-2$는 $A$의 limit point이다. 이는 $-2$를 포함하는 임의의 열린집합은 반드시 $-1\in A$ 또한 포함해야 하기 때문이다.

</div>

위의 예시는 limit point를 확인할 때 점열의 수렴이 그리 좋은 개념이 아니라는 것을 보여준다. 한편 [§집합의 내부, 폐포, 경계, ⁋명제 6](/ko/math/topology/other_concepts#prop6)에 의하여, 집합 $A$의 임의의 limit point는 $A$의 closure에 속한다. 

<div class="proposition" markdown="1">

<ins id="lem7">**보조정리 7**</ins> 위상공간 $X$와 임의의 부분집합 $A\subseteq X$에 대하여, 만일 $x\in X$로 수렴하는 $A$의 점열이 존재한다면 $x\in \cl(A)$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$x$의 임의의 열린근방 $U$를 택하자. 그럼 $x$로 수렴하는 점열 $(x_n)$이 존재하므로, 적당한 $N\in \mathbb{N}$가 존재하여 $n\geq N$이면 $x_n\in U$이다. 그럼 $x_N\in U\cap A$이므로 $U\cap A\neq \emptyset$이고, 따라서 $x\in \cl(A)$이다.

</details>

그러나 위의 보조정리의 역 또한 일반적으로는 성립하지 않는다.

<div class="example" markdown="1">

<ins id="ex8">**예시 8**</ins> 일반적인 위상구조가 주어진 $\mathbb{R}$의 uncountable product $\mathbb{R}^J$를 생각하자. 집합 $A$를

$$A=\{(x_j)\in \mathbb{R}^J: x_j=1\text{ for all but finitely many $j$}\}$$

으로 정의하자. 그럼 $\mathbb{R}^J$의 원점은 $A$의 closure에 속한다. 이는 원점을 포함하는 $\mathbb{R}^J$의 base는 유한한 index를 제외하고는 모두 $\mathbb{R}$이며, 이 유한한 index들의 성분은 $0$으로 정의하고, 나머지 index의 성분은 $1$인 점이 이 base와 $A$의 교집합에 들어있기 때문이다. 그러나 $A$의 임의의 점열은 원점으로 수렴하지 않는다. 이는 $A$의 임의의 점열이 주어졌을 때, $J$가 uncountable임을 이용하면 이 점열의 모든 항의 $j$번째 성분이 $1$이도록 하는 $j\in J$가 존재한다는 것을 보일 수 있고, 그럼 $j$번째 성분이 $(-1,1)$이고 나머지 성분은 $\mathbb{R}$인 원점의 열린근방이 이 점열의 원소를 하나도 포함하지 않기 때문이다.

</div>

한편, 다음 명제는 약간의 일반화를 거치긴 했지만, 그래도 여전히 익숙한 것이다.

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> 연속함수 $f:X \rightarrow Y$와 $X$의 임의의 점열 $(x_n)$에 대하여, 만일 $(x_n)$이 $x\in X$로 수렴한다면 $(f(x_n))$은 $f(x)$로 수렴한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$f(x)$의 임의의 열린근방 $V$를 택하자. 그럼 $f$는 연속함수이므로 $f^{-1}(V)$는 $x$의 열린근방이다. 따라서 적당한 $N\in \mathbb{N}$가 존재하여 $n\geq N$이면 $x_n\in f^{-1}(V)$이다. 그럼 $f(x_n)\in V$이므로 $(f(x_n))$은 $f(x)$로 수렴한다.

</details>

한편, 만일 공간 $X$에서 [보조정리 7](#lem7)의 역이 성립한다면, 해당 결과와 [§연속함수, ⁋정리 4](/ko/math/topology/continuous_functions#thm4)의 두 번째 조건을 사용해 [명제 9](#prop9)의 역 또한 보일 수 있다. 즉, 만일 임의의 $x\in A$로 수렴하는 임의의 점열 $(x_n)$에 대하여 $f(x_n)$이 $f(x)$로 수렴한다면, $f$는 점 $x$에서 연속이다.

$X$가 [보조정리 7](#lem7)의 역이 성립한다는 공간이라 하자. 그럼 임의의 $x\in \cl(A)$에 대하여 $x$로 수렴하는 $X$의 점열 $(x_n)$를 잡을 수 있다. 그럼 $Y$의 점열 $f(x_n)$가 $f(x)$로 수렴하므로 [보조정리 7](#lem7)에 의하여 $f(x)\in \cl(f(A))$이고 [§연속함수, ⁋정리 4](/ko/math/topology/continuous_functions#thm4)로부터 원하는 결과를 얻는다.

특히 이 논증은 $X$가 *metrizable*일 경우 성립한다. ([##ref##]())

## 가산공리

위의 내용들은 지금까지 다룬 개념들을 나타내는 데에 점열의 수렴은 적절한 개념이 아니라는 것을 보여준다. [명제 11](#prop11)의 증명을 살펴보면 이를 어떠한 방식으로 일반화하는 것이 좋은지를 알 수 있다.

<div class="definition" markdown="1">

<ins id="def10">**정의 10**</ins> 위상공간 $X$에 대하여 다음을 정의한다.

1. $X$가 *first countable*이라는 것은 $X$의 임의의 점 $x\in X$에 대하여 $x$의 countable local base가 존재하는 것을 의미한다.
2. $X$가 *second countable*이라는 것은 $X$의 countable base가 존재하는 것을 의미한다.

</div>

<div class="proposition" markdown="1">

<ins id="prop11">**명제 11**</ins> $X$가 first countable $T_1$이고 limit point compact라면 $X$는 sequentially compact이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

앞서 언급한 것과 같이 임의의 점열 $(x\_n)$이 주어졌을 때, 집합 $A=\\{x_n:n\geq 1\\}$는 유한집합이 되어 자명한 이유로 수렴하는 부분점열을 갖거나, 혹은 무한집합이 되어 limit point $x$를 갖는다. 만일 $x=x_n$가 무한히 많은 $n$에 대해 성립한다면 또 다시 자명한 이유로 $x$에 수렴하는 부분점열을 잡을 수 있으므로, $x_n=x$를 만족하는 $n$아 오직 유한 개밖에 없다고 가정할 수 있고 이는 점열의 수렴에 영향을 주지 않으므로 일반성을 잃지 않고 $x_n\neq x$가 모든 $n$에 대해 성립한다고 가정할 수 있다. 

한편 $X$는 first countable이므로, $x$의 countable local base $\mathcal{B}(x)$를 생각할 수 있다. $\mathcal{B}(x)$의 원소를 $B_1,B_2,\ldots$와 같이 적는다면, $B_n$을 $B_1\cap\cdots\cap B_n$으로 바꾸어 $B_{n+1}\subseteq B_n$이 모든 $n$에 대해 성립하도록 할 수 있다. 

이제 $B_1$은 $x$를 포함하는 열린집합이고 $x$는 $A$의 limit point이므로, 적당한 $n_1$이 존재하여 $x\_{n\_1}\in B_1$이도록 할 수 있다. 이제 $X$가 $T_1$이므로 $x$를 포함하지만 $x_1,\ldots,x\_{n\_1}$을 포함하지 않는 열린집합 $U\_2$가 존재한다. 그럼 $U\_2\cap B\_2$는 다시 $x$를 포함하는 열린집합이고 $x$는 $A$의 limit point이므로, 적당한 $n_2$가 존재하여 $x\_{n\_2}\in U_2\cap B_2$이도록 할 수 있다. 이 과정을 반복하여 $x$로 수렴하는 $A$의 부분점열을 잡을 수 있다.

</details>

## 필터의 수렴

[명제 11](#prop11)의 증명에서 핵심적인 역할을 한 것은 $x$가 열린집합들의 decreasing sequence

$$B_1\supseteq B_2\supseteq\cdots$$

를 가지며, first countability에 의하여 어떠한 열린집합 $U$가 주어지더라도 충분히 큰 $n$에 대해서는 $B_n\subseteq U$이도록 할 수 있다는 것이다. 즉, 어떤 의미에서는 위의 열린집합들 그 자체가 $x$로 수렴한다고 볼 수도 있다. 이와 같은 관찰을 바탕으로 다음을 정의한다.

<div class="definition" markdown="1">

<ins id="def12">**정의 12**</ins> 위상공간 $X$와 그 위에 정의된 filter $\mathcal{F}$를 생각하자. ([§위상공간의 다른 정의들, ⁋정의 3](/ko/math/topology/equivalent_formulations_of_topology#def3)) 그럼 $\mathcal{F}$가 $x\in X$로 *수렴<sub>converge</sub>*한다는 것은 $\mathcal{N}(x)\subseteq \mathcal{F}$가 성립하는 것이다. ([§열린집합, §§Neighborhood filter](/ko/math/topology/open_sets#neighborhood-filter)) 이 때, $x$를 $\mathcal{F}$의 *limit point<sub>극한점</sub>*라 부른다. 

</div>

[정의 12](#def12)는 점열의 수렴을 일반화한 것이다. 이를 확인하기 위해서는 우선 다음을 정의해야 한다.

<div class="definition" markdown="1">

<ins id="def13">**정의 13**</ins> 집합 $X$ 위에 정의된 filter $\mathcal{F}$, 그리고 위상공간 $X$가 주어졌다 하자. 함수 $f:X \rightarrow Y$에 대하여, $y\in Y$가 $\mathcal{F}$에 대한 $f$의 *limit point*라는 것은 $y$가 filter ${\uparrow}f(\mathcal{F})$의 limit point인 것이다. ([§위상공간의 다른 정의들, ⁋명제 7](/ko/math/topology/equivalent_formulations_of_topology#prop7))

</div>

그럼 정의에 의하여, $y\in Y$가 $\mathcal{F}$에 대한 $f$의 limit point인 것은 $y$의 임의의 근방 $V$가 주어질 때마다, 적당한 $F\in \mathcal{F}$가 존재하여 $f(F)\subseteq V$인 것이다. 특히 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="prop14">**명제 14**</ins> 위상공간 $X$의 점열 $(x\_n)\_{n\geq 1}$에 대하여, $(x\_n)\_{n\geq 1}$이 $x\in X$로 수렴하는 것과 $\mathbb{N}$ 위에 정의된 Fréchet filter $\mathcal{F}$의 $n\mapsto x\_n$에 의한 image로 생성되는 filter가 $x$로 수렴하는 것이 동치이다. ([§위상공간의 다른 정의들, ⁋예시 4](/ko/math/topology/equivalent_formulations_of_topology#ex4))

</div>

따라서 필터의 수렴은 점열의 수렴을 일반화한 것임을 안다. 뿐만 아니라 이 개념을 통해 다음과 같은 명제를 증명할 수 있다. 

<div class="proposition" markdown="1">

<ins id="prop15">**명제 15**</ins> 위상공간 $X$와 임의의 부분집합 $A\subseteq X$에 대하여, $x\in\cl(A)$인 것과, $x$로 수렴하는 $A$의 filter $\mathcal{F}$가 존재하는 것이 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $x$로 수렴하는 $A$의 filter $\mathcal{F}$가 존재한다 하자. 즉 $\mathcal{F}$는 원소 $A$와 부분집합 $\mathcal{N}(x)$를 포함한다. 따라서 filter의 정의에 의하여, 임의의 근방 $U\in \mathcal{N}(x)$에 대하여 $U\cap A\neq\emptyset$이다. 

거꾸로 $x\in \cl(A)$라 하자. 그럼 $x$의 임의의 근방 $U$에 대하여, $U\cap A\neq\emptyset$이므로 다음 식

$$\mathcal{N}(x)\vert_A=\{U\cap A: U\in \mathcal{N}(x)\}$$

은 filter base를 정의한다. 이제 $\mathcal{F}$를 $\mathcal{N}(x)\vert_A$에 의해 정의되는 filter라 하면 원하는 결과를 얻는다.

</details>

따라서, [보조정리 8](#lem8) 이후의 논증에 의해 다음 명제도 자명하다.

<div class="proposition" markdown="1">

<ins id="prop16">**명제 16**</ins> 위상공간 사이의 함수 $f:X \rightarrow Y$에 대하여, 함수 $f$가 $x\in X$에서 연속인 것은 $x$로 수렴하는 임의의 filter $\mathcal{F}$에 대하여, filter base $f(\mathcal{F})$가 정의하는 filter가 $f(x)$로 수렴하는 것과 동치이다. 

</div>