---

title: "하우스도르프 공간"
excerpt: ""

categories: [Math / Topology]
permalink: /ko/math/topology/Hausdorff_spaces
header:
    overlay_image: /assets/images/Math/Topology/Hausdorff_spaces.png
    overlay_filter: 0.5
sidebar: 
    nav: "topology-ko"

date: 2024-12-03
last_modified_at: 2024-12-03
weight: 13

---

이제 우리는 하우스도르프 공간을 정의한다. 그 전에 우선 다음을 정의한다.

## 점열의 수렴

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 위상공간 $X$에 대하여, 함수 $\mathbb{N} \rightarrow X$를 $X$의 점들로 이루어진 *점열<sub>sequence</sub>*이라 부르고, 이를 $(x\_n)\_{n\geq 1}$과 같이 나타낸다. 점열 $(x\_n)\_{n\geq 1}$이 $x\in X$로 *수렴<sub>converge</sub>*한다는 것은 $x$의 임의의 근방 $U$가 주어질 때마다, 적당한 $N\in \mathbb{N}$이 존재하여 다음 명제 

$$n\geq N\implies x_n\in U$$

가 참이도록 할 수 있는 것이다. 

</div>

이는 미적분학 등에서 이미 다루었던 수열의 수렴의 $\epsilon$-$N$ 정의에서, $x$에 가까운 점을 나타내기 위해 $\epsilon$-ball 대신 열린집합 $U$를 사용한 것만이 다르다. 만일 점열 $(x\_n)$가 $x$에 수렴한다면 이를 $\lim_{n \rightarrow\infty}x_n$과 같이 적고 싶은 것이 당연하겠지만, 다음 예시에서 이 표기가 잘 정의되지조차 않는다는 것을 알 수 있다. 

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins> 임의의 집합 $X$에 trivial topology를 주어 $X$를 위상공간으로 생각하자. 그럼 $X$의 임의의 점열은 $X$의 임의의 점으로 수렴한다. 

</div>

## 분리공리들

위의 [예시 2](#ex2)와 같은 현상이 일어나는 이유는 직관적으로 $X$ 위에 정의된 위상이 $X$의 점들을 분리시켜줄만큼 충분히 강하지 않기 때문이다. 우리는 위상공간에서 점들을 분리하는 정도에 따라 다양한 종류의 *separation axiom<sub>분리공리</sub>*들을 정의하고 이들 각각을 만족하는 공간들을 분류할 수 있다. 이를 위해 몇 가지 용어를 정리하자.

- 위상공간 $X$의 두 점 $x,y$가 서로 다르다는 것은 $x\neq y$인 것이다. 
- 위상공간 $X$의 두 점 $x,y$가 *위상적으로 구별가능<sub>topologically distinguishable</sub>*하다는 것은 $\mathcal{N}(x)\neq \mathcal{N}(y)$인 것이다.[^1] ([§열린집합, §§Neighborhood filter](/ko/math/topology/open_sets#neighborhood-filter))
- 위상공간 $X$의 두 부분집합 $A,B$가 *분리가능<sub>separated</sub>*이라는 것은 $x,y$ 각각이 서로를 포함하지 않는 근방을 갖는 것이다.
- 위상공간 $X$의 두 부분집합 $A,B$가 *근방으로 분리가능<sub>separated by neighborhoods</sub>*이라는 것은 이들이 서로소인 근방을 갖는 것이다.
- 위상공간 $X$의 두 부분집합 $A,B$가 *닫힌근방으로 분리가능<sub>separated by closed neighborhoods</sub>*이라는 것은 이들이 서로소인 닫힌근방을 갖는 것이다.
- 위상공간 $X$의 두 부분집합 $A,B$가 *연속함수로 분리가능<sub>separated by continuous functions</sub>*이라는 것은 적당한 연속함수 $f:X \rightarrow \mathbb{R}$이 존재하여 $A\subseteq f^{-1}(\\{0\\})$이고 $B\subseteq f^{-1}(\\{1\\})$인 것이다. 
- 위상공간 $X$의 두 부분집합 $A,B$가 *연속함수로 정확히 분리가능<sub>precisely separated by continuous functions</sub>*이라는 것은 적당한 연속함수 $f:X \rightarrow \mathbb{R}$이 존재하여 $A= f^{-1}(\\{0\\})$이고 $B= f^{-1}(\\{1\\})$인 것이다. 

위의 조건들은 강한 순서대로 나열되어 있다. 즉, 연속함수로 정확히 분리가능한 두 부분집합은 연속함수로 분리가능하고, 연속함수로 분리가능한 두 부분집합은 닫힌근방으로 분리가능하며, 닫힌근방으로 분리가능한 두 부분집합은 근방으로 분리가능하고, 근방으로 분리가능한 두 부분집합은 분리가능하고, 분리가능한 두 점은 위상적으로 구별가능하며 모든 위상적으로 구별가능한 점들은 서로 다르다.

이제 다음을 정의한다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> 위상공간 $X$에 대하여, 다음을 정의한다. 

1. $X$가 *$T_0$-space<sub>$T_0$-공간</sub>*, 혹은 *Kolmogorov space<sub>콜모고로프 공간</sub>*라는 것은 임의의 서로 다른 두 점 $x,y$가 위상적으로 구별가능한 것이다.
2. $X$가 *$R_0$-space<sub>$R_0$-공간</sub>*이라는 것은 임의의 두 위상적으로 구별가능한 점들이 분리가능한 것이다.
3. $X$가 *$T_1$-space<sub>$T_1$-공간</sub>*, 혹은 *Fréchet space<sub>프레셰 공간</sub>*라는 것은 임의의 서로 다른 두 점이 분리가능한 것이다. 따라서, $X$가 $T_1$인 것과 $X$가 $T_0$이며 $R_0$인 것이 동치이다.
4. $X$가 *$R_1$-space<sub>$R_1$-공간</sub>*이라는 것은 임의의 두 위상적으로 구별가능한 점들이 근방으로 분리가능한 것이다. 따라서 임의의 $R_1$-space는 $R_0$-space이다.
5. $X$가 *$T_2$-space<sub>$T_2$-공간</sub>*이라는 것은 임의의 서로 다른 두 점이 근방으로 분리가능한 것이다. 따라서, $X$가 $T_2$인 것과 $X$가 $T_0$이며 $R_1$인 것이 동치이고, 임의의 $T_2$-space는 $T_1$이다. 
6. $X$가 *$T_{2\frac{1}{2}}$-space<sub>$T_{2\frac{1}{2}}$-공간</sub>*, 혹은 *Urysohn space<sub>유리손 공간</sub>*이라는 것은 임의의 두 위상적으로 구별가능한 점들이 닫힌근방으로 분리가능한 것이다. 따라서, 임의의 $T_{2\frac{1}{2}}$-space는 $T_2$이다. 
7. $X$가 *completely $T_2$-space<sub>완전 $T_2$-공간</sub>*, 혹은 *completely Hausdorff space<sub>완전 하우스도르프 공간</sub>*인 것은 임의의 서로 다른 두 점이 연속함수로 분리 가능한 것이다.
8. $X$가 *regular space<sub>정칙공간</sub>*이라는 것은 임의의 점 $x\in X$와 $x$를 포함하지 않는 닫힌집합 $A\subseteq X$가 항상 근방으로 분리가능한 것이다.
9. $X$가 *$T_3$-space<sub>$T_3$-공간</sub>*, 혹은 *regular Hausdorff space<sub>정칙 하우스도르프 공간</sub>*이라는 것은 $X$가 $T_0$이며 regular인 것이다. 임의의 $T_3$-space는 $T_{2\frac{1}{2}}$이다. 
10. $X$가 *completely regular space<sub>완전정칙공간</sub>*이라는 것은 임의의 점 $x\in X$와 $x$를 포함하지 않는 닫힌집합 $A\subseteq X$가 항상 연속함수로 분리가능한 것이다.
11. $X$가 *completely $T_3$-space<sub>완전 $T_3$-공간</sub>*, 혹은 *Tychonoff space<sub>티코노프 공간</sub>*인 것은 $X$가 $T_0$이고 completely regular인 것이다. 따라서 $X$가 completely $T_3$이면 completely Hausdorff이고 regular Hausdorff이므로, 이를 *completely regular Hausdorff space<sub>완전 정칙 하우스도르프 공간</sub>*라 부르기도 한다.
12. $X$가 *normal space<sub>정규공간</sub>*인 것은 임의의 서로소인 두 닫힌집합이 근방으로 분리가능한 것이다. 
13. $X$가 *normal regular space<sub>정규정칙공간</sub>*인 것은 $X$가 normal이고 $R_0$인 것이다. 따라서 $X$가 normal regular라면 $X$는 completely regular이다. 
14. $X$가 *$T_4$-space<sub>$T_4$-공간</sub>*, 혹은 *normal Hausdorff space<sub>정규 하우스도르프 공간</sub>*인 것은 $X$가 $T_1$이며 normal인 것이다. 임의의 $T_1$-space는 $R_0$이므로 임의의 $T_4$-space는 normal regular이고, 따라서 completely regular이다. 한편 임의의 $T_1$-space는 $T_0$-space이므로 이로부터 임의의 $T_4$-space는 completely $T_3$인 것을 안다.
15. $X$가 *completely normal space<sub>완전정규공간</sub>*인 것은 임의의 두 분리가능한 집합이 근방으로 분리가능한 것이다. 그럼 임의의 completely normal space는 normal이다.
16. $X$가 *completely $T_4$-space<sub>완전 $T_4$-공간</sub>*인 것은 $X$가 completely normal이고 $T_1$인 것이다. 따라서 임의의 completely $T_4$-space는 $T_4$이다.
17. $X$가 *perfectly normal space*인 것은 임의의 두 서로소인 닫힌집합이 연속함수로 정확히 분리가능한 것이다.
18. $X$가 *perfectly $T_4$-space*인 것은 $X$가 perfectly normal이고 $T_0$인 것이다. 

</div>

## 하우스도르프 공간

[정의 3](#def3)에서 특히 중요한 것 중 하나는 Hausdorff space이다. 여기에서는 우리의 직관이 잘 성립한다. 

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> Hausdorff space $X$의 임의의 점열 $(x_n)$에 대하여, $(x_n)$가 수렴하는 점은 많아야 하나 존재한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

결론에 반하여 $(x_n)$이 두 점 $x,y$로 수렴한다 하자. 그럼 $x$와 $y$의 서로소인 열린근방 $U,V$를 각각 잡을 수 있다. 이제 $(x_n)$이 $x$와 $y$로 각각 수렴한다는 가정으로부터, 적당한 $M,N$이 존재하여

$$m\geq M \implies x_m\in U,\qquad n\geq N\implies x_n\in V$$

이므로 $K=\max(M,N)$이라 하면 $x_K$는 $U$와 $V$에 동시에 속해야 하므로 모순이다.

</details>

한편, $X$가 Hausdorff임을 보일 때에는 다음의 보조정리도 유용하게 사용된다.

<div class="proposition" markdown="1">

<ins id="lem5">**보조정리 5**</ins> 위상공간 $X$가 Hausdorff space인 것은 $X\times X$의 부분집합

$$\Delta_X=\{(x,x)\mid x\in X\}$$

이 닫힌집합인 것과 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $X$가 Hausdorff라 가정하자. 그럼 임의의 $(x,y)\not\in\Delta_X$에 대하여, $x\neq y$이므로 $x$와 $y$의 서로소인 근방 $U,V$를 잡을 수 있다. 그럼 $U\times V$는 $(x,y)$를 포함하며 $\Delta_X$와 만나지 않는 열린집합이다. 

거꾸로 $\Delta_X$가 $X\times X$의 닫힌집합이라면, $x\neq y$인 임의의 $x,y\in X$에 대하여 $(x,y)\not\in\Delta_X$이고, 따라서 $\Delta_X$와 만나지 않는 $(x,y)$의 열린근방이 존재하며, product topology의 base를 생각하면 여기에 포함되는 $U\times V$ 꼴의 열린집합이 존재한다. 

</details>

더 일반적으로 $X$가 Hausdorff space인 것과, 임의의 index set $I$에 대하여 $X^I=\prod_{i\in I}X$에서의 diagonal

$$\Delta_X=\{(x_i)_{i\in I}:\text{$x_i=x$ for all $i$, where $x\in X$}\}$$

이 닫힌집합인 것이 서로 동치라는 것을 동일한 논증으로 보일 수 있다. [보조정리 5](#lem5)로부터 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="cor6">**따름정리 6**</ins> 연속함수 $f,g:X \rightarrow Y$에 대하여, 만일 $Y$가 Hausdorff라면 다음 집합

$$E=\{x\in X\mid f(x)=g(x)\}$$

는 $X$의 닫힌집합이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$X$에서 $Y\times Y$로의 연속함수 $x\mapsto (f(x), g(x))$를 생각하면 주어진 집합은 $Y\times Y$의 닫힌집합 $\Delta_Y$의 이 연속함수에 대한 preimage이다. 

</details>

<div class="proposition" markdown="1">

<ins id="cor7">**따름정리 7**</ins> 연속함수 $f:X \rightarrow Y$에 대하여, 만일 $Y$가 Hausdorff라면 다음 집합

$$\Gamma(f)=\{(x,f(x))\mid x\in X\}$$

은 $X\times Y$의 닫힌집합이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$X\times Y$에서 $Y$로의 두 연속함수

$$(x,y)\mapsto f(x),\quad (x,y)\mapsto y$$

를 생각한 후 [따름정리 6](#cor6)을 적용하면 된다. 

</details>

## 하우스도르프 공간의 부분공간과 곱

임의의 Hausdorff space $X$에 대하여, $X$의 부분공간 $A$도 Hausdorff인 것은 쉽게 확인할 수 있다. 이는 임의의 $x,y\in A$가 주어졌을 때, 이들의 $X$에서의 서로소인 열린근방 $U,V$를 잡으면 $U\cap A, V\cap A$가 $A$에서의 $x,y$의 서로소인 열린근방이 되기 때문이다. 한편 Hausdorff space의 곱 또한 Hausdorff이다.

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> 공집합이 아닌 $X_i$들에 대하여, $X=\prod_{i\in I}X_i$가 Hausdorff인 것과 $X_i$들 각각이 Hausdorff인 것이 동치이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $X_i$들이 Hausdorff이고 $x,y\in X$가 주어졌다 하면 $x_i\neq y_i$이도록 하는 $i$가 존재하고, 이러한 $X_i$ 안에서 $x_i$와 $y_i$를 분리하는 열린근방 $U,V$를 잡자. 그럼 $i$번째 성분만 각각 $U,V$이고 나머지 $j$번째 성분들은 $X_j$들인 $X=\prod X_i$의 base를 생각하면 이들이 $x,y$를 분리한다. 

거꾸로 $X$가 Hausdorff라면, 임의로 택한 $X_j$의 원소들 $x_j$에 대하여, 

$$\prod_{j\in I} A_j,\qquad A_j=\begin{cases}A_i&i=j\\\{x_j\}&\text{otherwise}\end{cases}$$

으로 정의된 $\prod A_j$는 $X_i$와 위상동형인 $X$의 부분집합이다. 

</details>

## 하우스도르프 공간의 몫공간

일반적으로 Hausdorff space $X$의 몫공간 $X/R$이 Hausdorff space인 것은 아니다. 뿐만 아니라 $X/R$이 Hausdorff일 필요충분조건 또한 쉽게 알아볼 수 있는데, $X/R$에서의 열린집합은 $R$-saturated인 $X$의 열린집합에 일대일로 대응되므로 $X/R$이 Hausdorff이기 위해서는 서로 다른 equivalence에 속하는 $x,y\in X$에 대해, 이들을 분리하는 $R$-saturated open set이 존재하는 것과 동치이다. 특히 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> 연속함수 $f:X \rightarrow Y$에 대하여, 만일 $Y$가 Hausdorff라면 다음 동치관계

$$x\sim y\iff f(x)=f(y)$$

에 대하여, 몫공간 $X/{\sim}$은 Hausdorff이다.

</div>



[^1]: 이는 $x$와 $y$를 각각 포함하는 열린집합들의 모임이 서로 같지 않다는 것과 동치이다. 