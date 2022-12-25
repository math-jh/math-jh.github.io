---

title: "이항관계"
excerpt: "이항관계의 정의"

categories: [Math / Set Theory]
permalink: /ko/math/set_theory/binary_relation

header:
    overlay_image: /assets/images/Set_theory/Binary_relation.png
    overlay_filter: 0.5

sidebar: 
    nav: "set-ko"

date: 2021-08-14
last_modified_at: 2022-11-22

weight: 3

---

## 이항관계

우선 정의부터 시작한다. 다음 정의는 별다른 것은 아니고, [이전 글](/ko/math/set_theory/ordered_pair#%EC%88%9C%EC%84%9C%EC%8C%8D)에서 순서쌍을 도입해야 하는 당위성을 설명하며 나왔던 <em_ko>순서쌍들의 집합</em_ko>에 이름을 준 것에 불과하다. 

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> 집합 $R$이 *이항관계<sub>binary relation</sub>*라는 것은 $R$의 모든 원소가 순서쌍이라는 것이다.[^1]

</div>

따라서, 다음과 같이 집합들 사이에 정의된 등호 ($=$)는 더 이상 이항관계라고 할 수 없다.

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins> 집합들 사이에서 $=$가 이항관계라면, 이를 나타내는 집합

$$E=\{(A,A):\text{$A$ any set}\}$$

이 존재한다. 즉, $E$는 전체집합 두 개의 곱이어야 한다.

</div>

전체집합 두 개의 곱이 존재한다면, 다음 명제에 의해 전체집합 또한 존재해야 하고 이는 [§ZFC 공리계, 예시 4](/ko/math/set_theory/zfc_axioms#ex4)에 모순이므로 모든 집합들 사이에 정의된 $=$는 이항관계가 될 수 없다. 

<div class="proposition" markdown="1">

<ins id="pp3">**명제 3**</ins> $R$이 이항관계라 하자. 그럼 유일한 두 개의 집합 $A$, $B$가 존재하여,  

<ul>
<li> <phrase>$x\in A$인 것</phrase>과 <phrase>어떤 $y$가 존재하여 $(x,y)\in R$인 것</phrase>이 동치이고,</li>
<li> <phrase>$y\in B$인 것</phrase>과 <phrase>어떤 $x$가 존재하여 $(x,y)\in R$인 것</phrase>이 동치이다.</li>
</ul>

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$R$이 이항관계라 하고 $\bigcup(\bigcup R)$를 생각하자. 계산을 통해 $(x,y)\in R\implies x,y\in\bigcup(\bigcup R))$임을 알 수 있다. $P$를

> $P(t)$: 어떠한 $s$가 존재하여 $(s,t)\in R$이다.

로 정의하면, 다음의 집합

$$A=\left\{x:\left(x\in\bigcup\left(\bigcup R\right)\right)\wedge P(x)\right\}$$

를 얻는다. 따라서 첫 번째 주장이 성립하며, 이와 유사하게 성질 $Q$를

> $Q(s)$: 어떠한 $t$가 존재하여 $(s,t)\in R$이다.

로 정의하면 집합 $B$를 얻는다.

</details>

[§순서쌍, 정의 7](/ko/math/set_theory/ordered_pair#df7)과 마찬가지로 이들을 각각 첫 번째와 두 번째 *projection*이라 부르고, $\operatorname{pr}_1R$과 $\operatorname{pr}_2R$로 쓴다.

간혹 이항관계의 첫 번째 성분과 두 번째 성분이 어느 집합에 속하는지를 명확하게 해야 할 때가 있다. 이를 위해 주어진 두 집합 $A,B$와 $\operatorname{pr}\_1R\subseteq A$, $\operatorname{pr}\_2R\subseteq B$를 만족하는 이항관계 $R$을 triple $(R,A,B)$와 같이 생각하기도 한다. 이 경우, $A$를 $R$의 *source*, $B$를 $R$의 *target*이라 부르며, 이런 상황에서는 같은 집합 $R$에 대해서도 $(R,A,B)$와 $(R,A',B')$를 다른 것으로 생각한다. 

<div class="remark" markdown="1">

<ins id="rmk1">**참고**</ins> 위의 조건 $\operatorname{pr}\_1R\subseteq A$, $\operatorname{pr}\_2R\subseteq B$를 만족하는 이항관계 $R$이 주어졌다 하자. [§순서쌍, 명제 9](/ko/math/set_theory/ordered_pair#pp9)에 의하여,

$$R\subseteq \operatorname{pr}_1 R\times\operatorname{pr}_2R\subseteq A\times B$$

이므로 데카르트 곱 $A\times B$는 $A$를 source로, $B$를 target으로 갖는 이항관계 중 가장 큰 것이라 할 수 있다.

</div>

## 이항관계의 상

<div class="definition" markdown="1">

<ins id="df5">**정의 5**</ins> 이항관계 $(R,A,B)$와 부분집합 $A'\subseteq A$를 생각하자. 그럼 <phrase>$R$에 의해 $A'$의 원소와 관계되는 모든 원소들의 집합</phrase>을 $R$에 의한 $A'$의 *상<sub>image</sub>*라 부르고 , $R(A')$로 표기한다.

</div>

위의 정의를 식으로 풀어쓰면

$$R(A')=\bigcup_{x\in A'} \{y\in B:(x,y)\in R\}$$

이다. 엄밀히 이야기하자면 우변의 집합 $\\{y\in B:(x,y)\in R\\}$은 이항관계 $R$의 target $B$가 주어지지 않았다면

$$\{y:(x,y)\in R\}$$

과 같은 형태가 되며, comprehension schema에 의하여 존재성이 보장되는 위의 집합과 달리 이 집합은 존재하지 않을 수도 있다. 

이와 같은 문제는 집합론을 공부하며 항상 주의해야 한다. 다만 우리는 집합론을 공부하는 게 목적이 아니라, 다른 곳에서 유용하게 사용할 명제들을 증명하는 것이 목적이므로 앞으로 이 정도의 사소한 서술상의 문제는 별 생각없이 넘어가기로 한다.

<div class="proposition" markdown="1">

<ins id="pp6">**명제 6**</ins> $R$이 이항관계라 하고, 임의의 집합 $A$와 그 부분집합 $X$를 생각하자. 그럼 $R(X)\subseteq R(A)$가 성립한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$y\in R(X)$라 하자. 그럼 어떤 $x\in X$가 존재하여 $(x,y)\in R(X)$이다. 이제 $X\subseteq A$로부터 $x\in A$이므로, $y\in R(A)$이다.

</details>

위의 명제에 의하여 임의의 $A$에 대해 

$$R(A)=\operatorname{pr}_2\{z\in R:\text{$\operatorname{pr}_1z\in A$}\}\subset\operatorname{pr}_2R$$

이고, 따라서 $R(A)\subset\operatorname{pr}_2R$가 성립한다. 특히 $A=\emptyset$이라면 $R(A)=\emptyset$이며, 더 일반적으로 만일 $A\cap\operatorname{pr}_1R=\emptyset$이라면 $R(A)=\emptyset$이다.

만일 어떤 $x$에 대해 $A=\\{x\\}$라면 $R(A)$를 마치 $x$에서의 $R$의 함숫값처럼 생각할 수 있다. 

<div class="definition" markdown="1">

<ins id="df7">**정의 7**</ins> 이항관계 $R$에 대하여, 집합 $R(\\{x\\})$를 $x$에서의 $R$의 *section*이라 부른다.

</div>

이 집합을 마치 $x$에서의 $R$의 함숫값처럼 $R(x)$로 적기도 한다. 이 <em_ko>함숫값</em_ko>은 유일하지 않으며, 따라서 $R(x)$ 또한 여러 개의 원소를 가질 수 있다.

---
**참고문헌**

**[HJJ]** K. Hrbacek, T.J. Jeck, and T. Jech. *Introduction to Set Theory*. Lecture Notes in Pure and Applied Mathematics. M. Dekker, 1978.  
**[Bou]** N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---

[^1]: **[Bou]**에서는 이러한 집합을 *그래프*라 부르고, 이항관계 중 그래프를 갖는 것과 갖지 않는 것을 구분하여 생각한다. 이는 그렇게 흔한 정의는 아니므로, 우리는 **[HJJ]**를 따라 위의 정의를 그대로 사용한다.