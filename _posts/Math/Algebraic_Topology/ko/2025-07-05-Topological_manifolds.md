---

title: "위상다양체"
excerpt: ""

categories: [Math / Algebraic Topology]
permalink: /ko/math/algebraic_topology/topological_manifolds
header:
    overlay_image: /assets/images/Math/Algebraic_Topology/Topological_manifolds.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_topology-ko"

date: 2025-07-05
last_modified_at: 2025-07-05
weight: 1

---

우리는 이 카테고리에서 기하학을 공부할 때 필수적이라 할 수 있는 호몰로지, 코호몰로지 등을 다룬다. 이들 개념은 일반적인 위상공간 위에 정의되지만, 이들이 잘 행동하기 위해서는 공간이 추가적인 성질들을 가져야하며, 이러한 조건들이 모두 만족되는 공간이 바로 [\[위상수학\] §옹골성, ⁋정의 9](/ko/math/topology/compactness#def9)에서 정의하였던 topological manifold이다. 이번 글에서 우리는 topological manifold의 성질과 예시들을 살펴볼 것이며, 이 다음 글에서는 호몰로지가 무엇인지 대략적인 예시를 통해 살펴볼 것이다. 이들 두 글은 이 카테고리의 큰 방향을 보여주는 것으로, 본격적인 내용은 셋째 글부터 시작한다. 

## 위상다양체의 정의

서술상의 편의를 위해 [\[위상수학\] §옹골성, ⁋정의 8](/ko/math/topology/compactness#def8)과 [\[위상수학\] §옹골성, ⁋정의 9](/ko/math/topology/compactness#def9)를 반복하면 다음과 같다. 

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 위상공간 $M$이 *locally Euclidean of dimension $m$*이라는 것은 임의의 $x\in M$이 주어질 때마다 $x$의 적당한 열린근방 $U$가 존재하여 $U$가 $\mathbb{R}^m$의 열린집합과 homeomorphic한 것이다. 

</div>

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> Second countable, Hausdorff, locally Euclidean of dimension $m$인 공간을 *topological manifold of dimension $m$*이라 부른다. 

</div>

편의상 topological manifold of dimension $m$을 *$m$-manifold*라 부르자. [\[위상수학\] §옹골성, ⁋정의 8](/ko/math/topology/compactness#def8)에서는 정의하지 않았지만, 종종 우리는 위의 정의에서 $\mathbb{R}^m$을 *half-space*

$$\mathbb{H}^m=\left\{(x_1,\ldots,x_m)\in \mathbb{R}^m\mid x_m\geq 0\right\}$$

로 바꾸어 *manfold with boundary*를 생각할 때도 있다. 

## 위상다양체의 예시

우리는 이미 위상수학에서 주어진 공간(들)을 이용하여 새로운 공간을 만들어내는 방법을 많이 배웠다. 따라서 만일 처음에 위상다양체들이 주어졌을 때, 그 결과로 나오는 공간들이 여전히 위상다양체인지 살펴보는 것이 자연스러울 것이다. 

<div class="example" markdown="1">

<ins id="ex3">**예시 3 (Open submanifold)**</ins> $m$-manifold $M$의 open subspace $U$는 다시 $m$-manifold이다. 이는 $M$의 base를 $\mathcal{B}$라 했을 때, 다음의 식

$$\mathcal{B}_U=\left\{B\cap U\mid B\in \mathcal{B}\right\}$$

이 $U$의 base가 되는 것으로부터 $U$가 second-countable이며, Hausdorff space의 subspace는 항상 Hausdorff이며 ([\[위상수학\] §하우스도르프 공간, §§하우스도르프 공간의 부분공간과 곱](/ko/math/topology/Hausdorff_spaces#하우스도르프-공간의-부분공간과-곱)) 만일 $x\in U$가 임의로 주어졌다면, $M$이 locally Euclidean이라는 가정으로부터 $x$의 $M$에서의 열린근방 $V$를 택하여 $V$가 $\mathbb{R}^m$의 열린집합과 homeomorphic하도록 할 수 있고 따라서 $U\cap V$가 $x$의 $U$에서의 열린근방이며 $\mathbb{R}^m$의 열린집합과 homeomorphic하기 때문이다. 

</div>

비슷하게 [\[위상수학\] §하우스도르프 공간, ⁋따름정리 7](/ko/math/topology/Hausdorff_spaces#cor7)의 집합 또한 다음과 같이 topological manifold의 예시를 준다. 

<div class="example" markdown="1">

<ins id="ex4">**예시 4**</ins> 열린집합 $U\subseteq \mathbb{R}^n$과 연속함수 $f:U\rightarrow\mathbb{R}^k$에 대하여, $f$의 graph 

$$\Gamma(f)=\left\{(x,f(x))\mid x\in U\right\}\subset \mathbb{R}^m\times \mathbb{R}^k$$

는 $m$-manifold이다. 사실 이는 다음의 두 연속함수

$$x\mapsto (x,f(x)),\qquad (x,f(x))\mapsto x$$

가 서로의 inverse이므로 $\Gamma(f)$와 $U$가 homeomorphic하기 때문이다. 

</div>

[\[위상수학\] §하우스도르프 공간, ⁋따름정리 7](/ko/math/topology/Hausdorff_spaces#cor7)에 의해 $\Gamma(f)$는 $\mathbb{R}^{m+k}$의 닫힌집합이므로, 이는 [예시 3](#ex3)과는 다소 다른 결의 예시를 준다. 

한편 product topology에 대해서도 다음이 성립한다. 

<div class="example" markdown="1">

<ins id="ex5">**예시 5 (Product manifold)**</ins> 두 topological manifold $M_1$, $M_2$이 주어졌다 하고 이들이 각각 $m_1,m_2$차원이라 하자. 그럼 $M_1\times M_2$는 $(m_1+m_2)$-manifold이다. 이는 $M_i$의 base를 $\mathcal{B}_i$라 했을 때, 다음의 식

$$\mathcal{B}=\left\{B_1\times B_2\mid B_i\in \mathcal{B}_i\right\}$$

으로 주어지는 $\mathcal{B}$가 $M_1\times M_2$의 basis가 되므로 $M_1\times M_2$는 second countable이며, Hausdorff space의 곱은 Hausdorff이고 ([\[위상수학\] §하우스도르프 공간, ⁋명제 8](/ko/math/topology/Hausdorff_spaces#prop8)) 임의의 $(x_1,x_1)\in M_1\times M_2$에 대하여 $U_i$가 $M_i$에서의 $x_i$의 Euclidean neighborhood라면 $U_1\times U_2$가 $(x_1,x_2)$의 $M_1\times M_2$에서의 Euclidean neighborhood가 되기 때문이다. 

</div>

마지막으로 살펴볼 일반적인 construction은 quotient space이다. 그러나 [\[위상수학\] §하우스도르프 공간, §§하우스도르프 공간의 몫공간](/ko/math/topology/Hausdorff_spaces#하우스도르프-공간의-몫공간)에서 살펴보았듯 Hausdorff space의 임의의 quotient space가 Hausdorff가 되는 것은 아니다. 또, Euclidean space의 quotient space가 Euclidean이라는 보장도 없으므로 quotient space가 topological manifold임을 보이기 위해서는 적어도 Hausdorff 조건과 locally Euclidean 조건은 따로 보여줘야 한다. 대신 second countability는 locally Euclidean 조건으로부터 따라나온다. 

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> Quotient map $X \rightarrow X/R$에 대하여, $X$가 second-countable이고 $X/R$이 locally Euclidean이라 하자. 그럼 $X/R$은 second countable이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$X/R$이 locally Euclidean이므로 $X/R$을 Euclidean neighborhood들 $(U\_i)\_{i\in I}$로 덮을 수 있으며 이들의 premimage들의 모임 $(\pi^{-1}(U\_i))\_{i\in I}$들이 $X$를 덮는다. 이제 임의의 second-countable space는 Lindelöf이므로 ([##ref##](countability)) 적당한 countable subset $J\subset I$이 존재하여 $(\pi^{-1}(U\_i)\_{i\in J}$가 $X$의 countable open cover이며, 따라서 이들에 해당하는 $(U\_i)\_{i\in J}$들이 $X/R$의 countable cover가 된다. 그런데 이들 각각은 Euclidean neighborhood이므로 다시 countable base를 가지며, 이러한 것들이 countable하게 있으므로 이들을 모두 모은 것이 $X/R$의 countable base가 된다.

</details>

이 카테고리의 흐름으로만 본다면 우리의 관심은 위상다양체로 한정지어도 충분할 것이나, 특히 코호몰로지의 곱셈 구조를 다룰 때는 미분다양체에서의 적분의 개념을 떠올리는 것이 더 편하다. 