---
title: "순서쌍"
excerpt: "집합의 포함관계와 순서쌍의 정의"

categories: [Math / Set Theory]
permalink: /ko/math/set_theory/ordered_pair

header:
    overlay_image: /assets/images/Set_theory/Ordered_pair.png
    overlay_filter: 0.5

sidebar: 
    nav: "set-ko"

date: 2021-08-09
last_modified_at: 2021-05-17

weight: 2

---

## 집합의 포함관계

ZFC 공리계는 [앞선 글](/ko/math/set_theory/zfc_axioms)에서 소개한 공리들 외에도 여러가지 공리들을 포함하고 있지만, ZFC 공리계에 대한 소개는 일단은 이쯤에서 멈춘다. 

러셀의 역설을 필두로 한 여러 모순들은 기존의 소박한 집합론에 경각심을 주긴 하였지만, 그렇다고 해서 기존의 이론을 사용할 수 없다는 이야기는 아니다. 오히려 공리적 집합론은 우리가 안심하고 기존의 소박한 집합론을 사용할 수 있도록 토대를 다져주는 역할을 한다. 

때문에 남은 글들에서는 집합론을 완전하게 공리적으로 접근하기보다, 기존의 소박한 집합론의 관점으로 접근하되 필요한 부분만 그때그때 공리들을 언급해나가는 방향으로 진행할 것이다. 하지만 이들은 모두 ZFC 공리들에 의해 완벽하게 정당화될 수 있다. 

본격적인 이야기를 시작하기 전에 앞으로 사용할 정의를 하나 새로 만들자.

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> $A\subseteq B$라는 것은 임의의 $x$에 대하여, 명제 $x\in A\implies x\in B$이 항상 참인 것이다. 

</div>

다음의 두 명제들은 $\subset$의 두 성질들이다. (참고: [§순서관계 (1), 정의 1](/ko/math/set_theory/order_relations#df1))

<div class="proposition" markdown="1">

<ins id="pp2">**명제 2**</ins> $A\subseteq A$가 항상 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$x\in A\implies x\in A$가 항상 참이다.

</details>

<div class="proposition" markdown="1">

<ins id="pp3">**명제 3**</ins> $A\subseteq B$이고 $B\subseteq C$이면 $A\subseteq C$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 전제는 임의의 $x$에 대하여 두 명제 $x\in A\implies x\in B$와 $x\in B\implies x\in C$가 참이라는 것을 뜻한다. 따라서 삼단논법에 의해 $x\in A\implies x\in C$도 참이고, $x$는 임의로 택할 수 있으므로 $A\subseteq C$가 성립한다. 

</details>

## 순서쌍

이제 본격적으로 집합론을 시작한다. 

집합론에서 가장 중요하게 사용하는 것은 이항관계다. 이항관계는 *binary relation*이라는 말 그대로 <em_ko>두 개의 원소들 사이의 관계</em_ko>를 뜻한다. *단항관계<sub>unary relation</sub>* 등의 다른 관계도 있지만, 가장 빈번하게 사용되는 것은 이항관계이므로 앞으로 별다른 접두사 없이 간단히 관계라 지칭하는 것들은 모두 이항관계를 뜻하는 것으로 생각한다. 관계의 예시들은 다음과 같다.

- $x=y$는 $x$와 $y$ 사이의 관계다. 
- $y=f(x)$는 $x$와 $y$ 사이의 관계다.
- $x < y$는 $x$와 $y$ 사이의 관계다.

이 세 종류의 관계들은 각각 *동치관계<sub>equivalence relation</sub>*, *함수<sub>function</sub>*, 그리고 *순서관계<sub>order relation</sub>*라 부르며, 이들 셋을 모두 살펴보면 집합론에 대한 이 글타래는 끝이 난다. 

모든 관계가 순서쌍으로 표현 가능한 것은 아니지만, 우리가 도입한 공리를 통해 형식화할 수 있는 관계들은 순서쌍을 이용해 표현할 수 있다. 하지만 우리가 정의한 집합들 중에는 중고등학교때 배운 순서쌍의 역할을 할 도구가 없다. 강력한 후보는 axiom of pair에 의해 얻어지는 집합 $\\{A,B\\}$인데,

$$x\in \{A,B\}\iff (x=A)\wedge(x=B)\iff (x=B)\wedge(x=A)\iff x\in\{B,A\}$$

이므로 $\\{A,B\\}=\\{B,A\\}$가 되어 이 집합은 $A$와 $B$의 순서에 관계 없이 같은 집합을 나타낸다. 따라서, 순서쌍을 정의하기 위해서는 뭔가 새로운 아이디어가 필요하다.

<div class="definition" markdown="1">

<ins id="df4">**정의 4**</ins> *순서쌍<sub>ordered pair</sub>* $(x,y)$를 집합 $\big\\{\\{x\\}, \\{x,y\\}\big\\}$으로 정의한다.

</div>

위의 정의가 의미를 갖기 위해서는 다음의 보조정리를 먼저 보여야 한다. 편의상, 이 증명을 마지막으로 앞으로는 매 과정마다 사용한 공리들을 일일히 열거하는 대신 간단히 논증만 전개하기로 한다. 

<div class="proposition" markdown="1">

<ins id="lem5">**보조정리 5**</ins> 두 집합 $x$, $y$에 대하여, 집합 $(x,y)$는 항상 존재하고 유일하다.  

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

집합 $\\{x\\}=\\{x,x\\}$와 $\\{x,y\\}$가 각각 axiom of pair에 의해 존재하며, 따라서 다시 axiom of pair에 의해 집합 $\big\\{\\{x\\}, \\{x,y\\}\big\\}$도 존재한다. 

유일성의 경우 $\\{x\\}=\\{x,x\\}$와 $\\{x,y\\}$가 우선 유일하게 결정되고, 또 다시 이들에 axiom of pair를 적용하여 얻어지는 집합 $(x,y)$도 유일하게 결정된다는 것을 extensionality를 두 번 써서 확인할 수 있다.

</details>

순서쌍 $(x,y)$는 잘 정의된다는 것을 확인했지만, 이것이 정말 우리가 원하는 성질을 가지고 있는지는 아직 확인해보지 않았다. 즉, $(x,y)$와 $(y,x)$가 실제로 다른지를 확인해봐야 한다. 이는 더 일반적인 다음 명제의 결과이다.

<div class="proposition" markdown="1">

<ins id="pp6">**명제 6**</ins> 두 개의 순서쌍 $(x,y)$, $(x',y')$에 대하여, <phrase>$(x,y)=(x',y')$인 것</phrase>과 <phrase>$x=x'$이고 $y=y'$인 것</phrase>이 서로 동치이다.

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

직관적으로 $z=(x,y)=\big\\{\\{x\\}, \\{x,y\\}\big\\}$의 첫 번째와 두 번째 성분을 각각 뽑아오기 위해서는 $(x,y)$의 두 원소 중 하나의 원소만 갖는 집합의 유일한 원소를 뽑아와서 이걸 첫 번째 성분이라 부르고, 남은 하나를 두 번째 성분이라 부르면 된다. 하지만 우리는 원소의 개수라는 것도 아직 정의하지 않았으므로 다른 방법이 필요하다.

집합 $\bigcup z$를 생각하자. 정의에 의해, 이 집합은 $\bigcup z=\\{x\\}\cup\\{x,y\\}=\\{x,y\\}$이다. 이제 다음과 같이 성질  

> $P(s)$: 어떠한 $t$가 존재하여 $z=(s,t)$이다.  

을 정의하면, 우리는 앞선 집합 $\bigcup z$의 부분집합  

$$\left\{s\in\bigcup z: P(s)\right\}$$  

을 얻게 된다. 이 집합은 원소 하나짜리 집합 $\\{x\\}$이다. 성질 $Q$를 비슷하게 잘 정의하면 원소 하나짜리 집합 $\\{y\\}$를 얻는다. 

<div class="definition" markdown="1">

<ins id="df7">**정의 7**</ins> 위의 과정으로 얻어진 두 집합 $\\{x\\}$, $\\{y\\}$에 대하여, $\\{x\\}$의 유일한 원소 $x$를 $z=(x,y)$의 *첫 번째 성분*, $\\{y\\}$의 유일한 원소 $y$를 $z=(x,y)$의 *두 번째 성분*이라 부르며, 이를 각각 

$$x=\operatorname{pr}_1 z,\qquad y=\operatorname{pr}_2 z$$

와 같이 표시한다. 

</div>

여기서 $\operatorname{pr}$은 **pr**ojection의 약자이다. 저자에 따라 $P$, $\pi$ 등 다양한 표기를 사용한다.

한편, 다음과 같이 두 집합 $A$, $B$의 곱 $A\times B$를 정의할 수 있다.

<div class="definition" markdown="1">

<ins id="df8">**정의 8**</ins> 두 집합 $A$, $B$에 대하여, 다음의 집합

$$\{z:(z=(x,y))\wedge (x\in A)\wedge(y\in B)\}$$

을 $A$와 $B$의 *cartesian product<sub>데카르트 곱</sub>*라 부르고, 간단히 $A\times B$로 표시한다. 

또, [정의 7](#df7)과 유사하게 집합 $A$와 $B$를 $A\times B$의 첫 번째와 두 번째 성분이라 부른다.

</div>

두 곱집합 $A\times B$와 $A'\times B'$가 동일해질 조건을 알기 위해서는 하나의 곱집합이 다른 곱집합에 언제 <em_ko>포함되는지</em_ko>만 확실하게 결정해주면 된다. 이를 알면 우리는 두 명제

$$A\times B\subseteq A'\times B',\qquad A'\times B'\subseteq A\times B$$

가 각각 언제 성립하는지를 알기 때문이다.

<div class="proposition" markdown="1">

<ins id="pp9">**명제 9**</ins> 공집합이 아닌 두 집합 $A'$, $B'$에 대하여, <phrase>$A'\times B'\subseteq A\times B$인 것</phrase>과 <phrase>$A'\subseteq A$이고 $B'\subseteq B$인 것</phrase>이 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

먼저, $A'\times B'\subseteq A\times B$라 가정하자. $A'\subseteq A$를 보여야 하므로, 임의의 $a'\in A'$가 주어졌다 하고 $a'\in A$임을 보이자.  
$B'$는 공집합이 아니므로, 어떤 원소 $b'\in B'$가 존재한다. 따라서 $(a',b')\in A'\times B'$이고, 이제 $A'\times B'\subseteq A\times B$이므로 $(a',b')\in A\times B$이고 $a'\in A$이다. 이와 비슷하게 $B'\subseteq B$도 보일 수 있다.

반대로 $A'\subseteq A$이고 $B'\subseteq B$라 하자. 임의의 $z'\in A'\times B'$가 주어졌을 때 $z'\in A\times B$임을 보여야 한다.  
$z'=(a',b')$이라 하자. 즉 $a'\in A'$, $b'\in B'$인데, 가정에 의해 $a'$와 $b'$는 $A$와 $B$의 원소이기도 하므로 $(a,b)\in A\times B$이다.

</details>

이 증명에서, 예를 들어 만일 $B'$가 공집합이었다면 $A'\times B'\subseteq A\times B$로부터 $A'\subseteq A$를 보일 때 어떤 원소 $b'\in B'$를 뽑아올 수 없으므로 이 증명을 사용할 수 없다. 따라서 $A',B'$가 공집합이라는 가정이 필수적이다. 둘 중 하나가 공집합일 때는 다음 명제가 해결해준다.

<div class="proposition" markdown="1">

<ins id="pp10">**명제 10**</ins> 두 집합 $A$, $B$에 대하여, <phrase>$A\times B=\emptyset$인 것</phrase>과 <phrase>$A=\emptyset$이거나 $B=\emptyset$인 것</phrase>이 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $A\times B=\emptyset$이라 하자. 만일 $A$, $B$가 모두 공집합이 아니라 하면, 우리는 어떤 $a\in A$와 $b\in B$를 뽑아올 수 있으므로 $(a,b)\in A\times B$가 되어 모순이다. 

거꾸로 $A$ 혹은 $B$가 공집합이라 가정하자. 이번에도 결론을 부정하에 $A\times B$가 공집합이 아니라면, 어떤 원소 $(a,b)\in A\times B$가 존재한다. 따라서 $a\in A$이고 $b\in B$이므로, 이는 $A$ 혹은 $B$가 공집합이라는 가정에 모순이다. 증명 끝.

</details>

귀납적으로 $n$-tuple을 

$$(a,b,c)=\bigl(a,(b,c)\bigr), \quad (a,b,c,d)=\bigl(a,(b,c,d)\bigr),\quad\cdots$$

으로 정의할 수 있다. 하지만 우리는 함수를 정의한 후 더 일반적으로 순서쌍의 개념을 확장할 것이므로 이 정의에 대해서는 크게 신경쓰지 않기로 한다.

---
**참고문헌**

**[HJJ]** K. Hrbacek, T.J. Jeck, and T. Jech. *Introduction to Set Theory*. Lecture Notes in Pure and Applied Mathematics. M. Dekker, 1978.  
**[Bou]** N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---