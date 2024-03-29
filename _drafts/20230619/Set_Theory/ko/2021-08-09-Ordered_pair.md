---
title: "순서쌍"
excerpt: "집합의 포함관계와 순서쌍의 정의"

categories: [Math / Set Theory]
permalink: /ko/math/set_theory/ordered_pair

header:
    overlay_image: /assets/images/Math/Set_Theory/Ordered_pair.png
    overlay_filter: 0.5

sidebar: 
    nav: "set_theory-ko"

date: 2021-08-09
last_modified_at: 2022-11-21

weight: 2

---

## 집합의 포함관계

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> $A\subseteq B$라는 것은 임의의 $x$에 대하여, 명제 $x\in A\implies x\in B$이 항상 참인 것이다. 

</div>

다음의 두 명제들은 $\subset$의 두 성질들이다. 

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> $A\subseteq A$가 항상 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$x\in A\implies x\in A$가 항상 참이다.

</details>

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> $A\subseteq B$이고 $B\subseteq C$이면 $A\subseteq C$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 전제는 임의의 $x$에 대하여 두 명제 $x\in A\implies x\in B$와 $x\in B\implies x\in C$가 참이라는 것을 뜻한다. 따라서 삼단논법에 의해 $x\in A\implies x\in C$도 참이고, $x$는 임의로 택할 수 있으므로 $A\subseteq C$가 성립한다. 

</details>

위 두 명제로부터 $\subseteq$가 집합들 사이의 순서관계가 된다는 것을 안다. ([§순서관계 (1), ⁋정의 1](/ko/math/set_theory/order_relations#def1))

## 순서쌍

우리가 집합론에서 사용할 거의 유일한 도구는 이항관계이고, 이를 표현하는 언어는 순서쌍이다. 가령 위에서 살펴본 이항관계 $\subseteq$는 $A\subseteq B$를 만족하는 순서쌍들 $(A,B)$를 모아둔 "집합"

$$\subseteq=\{(A,B),(B,C),\cdots\}$$

으로 생각할 수 있다.[^1] 이와 비슷하게 함수 $y=f(x)$는 다음 집합

$$F=\{(x_1,f(x_1)), (x_2,f(x_2)),\cdots\}$$

으로 생각할 수 있고, 아직 정의하지 않은 *동치관계* 또한 이렇게 순서쌍들의 집합으로 나타낼 수 있다. 

하지만 우리가 정의한 집합들 중에는 중고등학교때 배운 순서쌍의 역할을 할 도구가 없다. 예컨대 $\\{A,B\\}=\\{B,A\\}$이므로 단순히 axiom of pair를 한 번 사용해서는 $A$와 $B$의 순서를 구별할 수 없다.

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> *순서쌍<sub>ordered pair</sub>* $(x,y)$를 집합 $\big\\{\\{x\\}, \\{x,y\\}\big\\}$으로 정의한다.

</div>

위의 정의가 의미를 갖기 위해서는 다음의 보조정리를 먼저 보여야 한다.[^2]

<div class="proposition" markdown="1">

<ins id="lem5">**보조정리 5**</ins> 두 집합 $x$, $y$에 대하여, 집합 $(x,y)$는 항상 존재하고 유일하다.  

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

집합 $\\{x\\}=\\{x,x\\}$와 $\\{x,y\\}$가 각각 axiom of pair에 의해 존재하며, 따라서 다시 axiom of pair에 의해 집합 $\big\\{\\{x\\}, \\{x,y\\}\big\\}$도 존재한다. 

유일성의 경우 $\\{x\\}=\\{x,x\\}$와 $\\{x,y\\}$가 우선 유일하게 결정되고, 또 다시 이들에 axiom of pair를 적용하여 얻어지는 집합 $(x,y)$도 유일하게 결정된다는 것을 extensionality를 두 번 써서 확인할 수 있다.

</details>

순서쌍 $(x,y)$는 잘 정의된다는 것을 확인했지만, 이렇게 정의된 순서쌍이 일반적인 $x,y$에 대하여 $(x,y)\neq (y,x)$를 만족하는지는 확인해봐야 한다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> 두 순서쌍 $(x,y)$, $(x',y')$에 대하여, <phrase>$(x,y)=(x',y')$인 것</phrase>과 <phrase>$x=x'$이고 $y=y'$인 것</phrase>이 서로 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$x=x'$이고 $y=y'$라면 $(x,y)=(x', y')$인 것은 자명하다. $\\{x\\}=\\{x'\\}$이고 $\\{x,y\\}=\\{x', y'\\}$이기 때문이다.  

이제 반대로 $(x,y)=(x',y')$이라 하자. 정의에 의해  

$$\big\{\{x\},\{x,y\}\big\}=\big\{\{x'\},\{x',y'\}\big\}$$

이 성립한다. $x=y$와 $x\neq y$ 가운데 정확히 하나가 반드시 성립하므로, 두 경우를 나누어 접근하자. 

- 만일 $x=y$일 경우, 위 식의 좌변은 

    $$\big\{\{x\},\{x,x\}\big\}=\big\{\{x\},\{x\}\big\}=\big\{\{x\}\big\}$$

    이 되므로  $\big\\{\\{x\\}\big\\}=\big\\{\\{x'\\},\\{x',y'\\}\big\\}$이다. 따라서 $\\{x\\}=\\{x'\\}=\\{x',y'\\}$이므로, $x=x'=y'$이고 따라서 $x=x'=y=y'$이다. 즉, $x=x'$이고 $y=y'$이므로 이 경우는 증명 끝.

- 남은 경우는 $x\neq y$이다. 이 경우, $\\{x,y\\}\neq\\{x'\\}$이므로 두 순서쌍이 같기 위해서는 반드시 $\\{x\\}=\\{x'\\}$이고 $\\{x,y\\}=\\{x',y'\\}$여야 한다. 그럼 $\\{x\\}=\\{x'\\}$에서 $x=x'$여야 하고, 이것과 $\\{x,y\\}=\\{x',y'\\}$에서 $y=y'$여야 한다. 따라서 이 경우도 증명 끝.

</details>

집합 

$$\bigcup z=\{x\}\cup\{x,y\}=\{x,y\}$$

를 생각하자. 이제 다음과 같이 성질  

> $P(s)$: 어떠한 $t$가 존재하여 $z=(s,t)$이다.  

을 정의하면, 우리는 앞선 집합 $\bigcup z$의 부분집합  

$$\left\{s\in\bigcup z\mid P(s)\right\}$$  

을 얻게 된다. 이 집합은 원소 하나짜리 집합 $\\{x\\}$이다. 성질 $Q$를 비슷하게 잘 정의하면 원소 하나짜리 집합 $\\{y\\}$를 얻는다. 

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> 위의 과정으로 얻어진 두 집합 $\\{x\\}$, $\\{y\\}$에 대하여, $\\{x\\}$의 유일한 원소 $x$를 $z=(x,y)$의 *첫 번째 성분*, $\\{y\\}$의 유일한 원소 $y$를 $z=(x,y)$의 *두 번째 성분*이라 부르며, 이를 각각 

$$x=\pr_1 z,\qquad y=\pr_2 z$$

와 같이 표시한다. 

</div>

여기서 $\pr$은 **pr**ojection의 약자이다. 한편, 다음과 같이 두 집합 $A$, $B$의 곱 $A\times B$를 정의할 수 있다.

<div class="definition" markdown="1">

<ins id="def8">**정의 8**</ins> 두 집합 $A$, $B$에 대하여, 다음의 집합

$$\{z\mid(z=(x,y))\wedge (x\in A)\wedge(y\in B)\}$$

을 $A$와 $B$의 *cartesian product<sub>데카르트 곱</sub>*라 부르고, 간단히 $A\times B$로 표시한다. 

또, [정의 7](#def7)과 유사하게 집합 $A$와 $B$를 $A\times B$의 첫 번째와 두 번째 성분이라 부른다.

</div>

두 곱집합 $A\times B$와 $A'\times B'$가 동일해질 조건을 알기 위해서는 하나의 곱집합이 다른 곱집합에 언제 <em_ko>포함되는지</em_ko>만 확실하게 결정해주면 된다. 

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> 공집합이 아닌 두 집합 $A'$, $B'$에 대하여, <phrase>$A'\times B'\subseteq A\times B$인 것</phrase>과 <phrase>$A'\subseteq A$이고 $B'\subseteq B$인 것</phrase>이 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

먼저, $A'\times B'\subseteq A\times B$라 가정하자. $A'\subseteq A$를 보여야 하므로, 임의의 $a'\in A'$가 주어졌다 하고 $a'\in A$임을 보이자.  
$B'$는 공집합이 아니므로, 어떤 원소 $b'\in B'$가 존재한다. 따라서 $(a',b')\in A'\times B'$이고, 이제 $A'\times B'\subseteq A\times B$이므로 $(a',b')\in A\times B$이고 $a'\in A$이다. 이와 비슷하게 $B'\subseteq B$도 보일 수 있다.

반대로 $A'\subseteq A$이고 $B'\subseteq B$라 하자. 임의의 $z'\in A'\times B'$가 주어졌을 때 $z'\in A\times B$임을 보여야 한다.  
$z'=(a',b')$이라 하자. 즉 $a'\in A'$, $b'\in B'$인데, 가정에 의해 $a'$와 $b'$는 $A$와 $B$의 원소이기도 하므로 $(a,b)\in A\times B$이다.

</details>

$A,B$ 둘 중 하나가 공집합일 때는 다음 명제를 적용할 수 있다.

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10**</ins> 두 집합 $A$, $B$에 대하여, <phrase>$A\times B=\emptyset$인 것</phrase>과 <phrase>$A=\emptyset$이거나 $B=\emptyset$인 것</phrase>이 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $A\times B=\emptyset$이라 하자. 만일 $A$, $B$가 모두 공집합이 아니라 하면, 우리는 어떤 $a\in A$와 $b\in B$를 뽑아올 수 있으므로 $(a,b)\in A\times B$가 되어 모순이다. 

거꾸로 $A$ 혹은 $B$가 공집합이라 가정하자. 이번에도 결론을 부정하에 $A\times B$가 공집합이 아니라면, 어떤 원소 $(a,b)\in A\times B$가 존재한다. 따라서 $a\in A$이고 $b\in B$이므로, 이는 $A$ 혹은 $B$가 공집합이라는 가정에 모순이다. 증명 끝.

</details>

---
**참고문헌**

**[HJJ]** K. Hrbacek, T.J. Jeck, and T. Jech. *Introduction to Set Theory*. Lecture Notes in Pure and Applied Mathematics. M. Dekker, 1978.  
**[Bou]** N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---

[^1]: 물론 이 "집합"은 집합이 아니다. ([§ZFC 공리계, ⁋예시 4](/ko/math/set_theory/zfc_axioms#ex4))
[^2]: 이 보조정리의 증명을 끝으로, 더 이상 증명과정에서 사용한 공리들을 언급하지 않는다.