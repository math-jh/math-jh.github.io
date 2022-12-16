---

title: "ZFC 공리계"
excerpt: "집합론의 공리들"

categories: [Math / Set Theory]
permalink: /ko/math/set_theory/zfc_axioms
header:
    overlay_image: /assets/images/Set_theory/ZFC_axioms.png
    overlay_filter: 0.5
sidebar: 
    nav: "set-ko"

date: 2021-08-07
last_modified_at: 2022-07-16
weight: 1

---

## 역사적 배경

수학의 기초라고 하면 바로 떠오르는 학문이 집합론이지만, 집합론이 지금과 같이 논리적인 완결성을 추구하며 수학의 기틀 역할을 하게 된 것은 그 역사가 길지 않다. 부르바키는 이 역사를 대충 19세기 초반부터 시작했다고 보고 있는데, 이 시기는 대략적으로 칸토어의 소박한 집합론이 완성된 시기다. 

소박한 집합론은 그 이후에 등장하는 공리적 집합론에 비교하면 말 그대로 <em_ko>소박하다</em_ko>. 이 이론에서는 대상들을 모아둔 어떠한 모임들도 모두 집합으로 인정한다. 이러한 철학을 더 형식적으로 표현하면 다음과 같이 이야기할 수 있다.

> 임의의 성질 $P$에 대하여, $P$를 만족하는 모든 원소들의 집합 $Y=\\{x:P(x)\\}$가 존재한다.

그러나 수학자들은 이 가정이 다양한 모순을 이끌어낸다는 것을 알게 된다. 

<div class="example" markdown="1">

<ins id="ex1">**예시 1 (러셀의 역설)**</ins> 집합 $\mathcal{S}$를 <phrase>$x\not\in x$를 만족하는 모든 $x$들의 모임</phrase>으로 정의하자.[^1] 

임의의 명제 $P$에 대하여, $P$는 항상 참이거나 거짓이거나 둘 중 하나가 성립한다. 따라서 $\mathcal{S}$는 자기 자신의 원소이거나, 자기 자신의 원소가 아니다.

- $\mathcal{S}$가 자기 자신의 원소라 가정하자. 그럼 $\mathcal{S}$의 정의 ($x\not\in x$)를 $\mathcal{S}$도 만족해야 하므로, $\mathcal{S}\not\in\mathcal{S}$이다. 이는 $\mathcal{S}$가 자기 자신의 원소라는 가정에 모순이므로, $\mathcal{S}$는 자기 자신의 원소가 될 수 없다.
- 그러므로 $\mathcal{S}$는 자기 자신의 원소가 아니어야 한다. 즉 $\mathcal{S}\not\in\mathcal{S}$여야 한다. 그런데 이 또한 모순이다. $\mathcal{S}$는 $x\not\in x$를 만족하는 모든 원소들의 모임이므로, 이를 만족하는 $\mathcal{S}$도 $\mathcal{S}$에 속해있어야 하기 때문이다.

따라서, $\mathcal{S}$가 자기 자신의 원소이든 아니든, 어떤 경우에도 모순이 생기게 된다. 이를 *러셀의 역설*이라 부른다.
</div>

이러한 일이 일어나는 이유는 우리가 집합이라는 것을 너무나도 소박하게 정의했기 때문이고, 이로 인해 집합이라는 대상을 단순히 <em_ko>특정한 성질을 갖는 대상들의 모임</em_ko>이 아닌 엄밀한 방법으로 정의할 필요가 생긴다. 

우리는 집합이라는 것을 직접 정의하는 대신, 집합이라는 대상이 무릇 가져야 할 성질들을 절대적인 진리로 받아들임으로써 집합이 될 수 없는 것들을 걸러낸다. 이렇게 절대적으로 받아들이는 명제들을 우리는 *공리<sub>axiom</sub>*들이라고 하고, 공리들을 모아둔 체계를 *공리계<sub>axiomatic system</sub>*라고 부른다. 

현대수학에서 주로 쓰이는 공리계는 처음 도입한 Zermelo, 그리고 이를 보완한 Frankel 두 사람의 머릿글자를 따서 *ZF system*이라고 불리며, 여기에 *선택공리<sub>axiom of choice</sub>*를 추가한 공리계를 *ZFC system*이라고 부른다. 이 글의 나머지 부분은 ZFC 공리계를 소개하는 데에 할애할 것이다.

## ZFC 공리계

집합이라는 대상이 아예 존재하지 않는다면, 우리가 집합에 대해 어떠한 명제를 적더라도 그 명제는 참이다. 논리식 $P\implies Q$는 $P$가 거짓이라면 $Q$의 참거짓에 상관 없이 항상 참이 되기 때문이다.[^2] 

따라서, 우리의 첫 번째 공리는 이 세상에 어떤 집합이 적어도 하나는 존재한다는 것이다.

<div class="misc" markdown="1">

**The Axiom of Existence.<sub>존재 공리</sub>** 어떠한 원소도 갖지 않는 집합이 존재한다.
  
</div>

어떠한 대상에 이름을 붙여주기 위해서는 이 대상이 유일하게 정의되어야 한다. 위에서 존재성이 보장된 <em_ko>어떠한 원소도 갖지 않는 집합</em_ko>에 공집합이라는 이름을 붙여주기 위해서는 먼저 이 집합이 유일하다는 것을 보여야 한다. 다음 공리가 이를 정당화한다.

<div class="misc" markdown="1">

**The Axiom of Extensionality.<sub>외연 공리</sub>** 두 집합 $A,B$에 대해 $A$의 모든 원소가 $B$의 원소이고, $B$의 모든 원소가 $A$의 원소라면 두 집합은 서로 같다.

</div>

<div class="proposition" markdown="1">

<ins id="pp2">**명제 2**</ins> 어떠한 원소도 갖지 않는 집합은 많아야 하나 존재한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

집합 $A$와 $B$가 어떠한 원소도 갖지 않는 집합이라 하자. 그럼 두 개의 명제 

$$((x\in A)\implies (x\in B)),\qquad ((x\in B)\implies (x\in A))$$

가 모두 참이다. 따라서 axiom of extensionality에 의하여 $A=B$이다. 

</details>

Axiom of existence로부터 위와 같은 집합이 적어도 하나 존재한다는 것을 알고 있으므로, <em_ko>어떠한 원소도 갖지 않는 집합</em_ko>의 존재성과 유일성이 모두 보장된다. 이제 이 집합을 *공집합*이라 부르고 $\emptyset$이라는 기호를 줄 수 있다.

공리적 집합론에서 [예시 1](#ex1)과 같은 상황을 막아주는 것은 다음의 공리다.   

<div class="misc" markdown="1">

**The Axiom schema of Comprehension.<sub>분류 공리꼴</sub>** 임의의 집합 $A$와 명제 $P$가 주어졌다 하자. 그럼 <phrase>$x\in B$인 것</phrase>과 <phrase>$x\in A$이고 $P(x)$인 것</phrase>이 동치이도록 하는 집합 $B$가 존재한다.

</div>

형식적으로 보았을 때, 위의 공리는 모든 명제 $P$에 대해서 어떤 성질이 만족된다는 주장을 하고 있다. 이를 1차 형식논리에서 표현하는 것은 불가능하기 때문에, 이를 하나의 단일한 공리 대신 공리들의 모임이라 생각하고 axiom *schema* of comprehension이라 부른다.

Extensionality에 의하여, comprehension schema가 정의하는 집합 $B$는 유일하다. 만일 $B'$가 이를 만족하는 다른 집합이라면

$$x\in B'\iff ((x\in A)\wedge P(x))\iff x\in B$$

이고 따라서 $x\in B\iff x\in B'$가 성립하므로 $B=B'$이기 때문이다. 이러한 집합을 $\\{x\in A:P(x)\\}$와 같이 적으면 적절할 것이다.

Comprehension schema가 러셀의 역설과 같은 형태의 모순을 어떻게 극복하는지 살펴보자. 
 
<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> [예시 1](#ex1)을 다시 한 번 살펴보자. 소박한 집합론에서 모순을 만들었던 것은 다음의 가정이다.

> (Unrestricted comprehension schema) $P$가 $x$에 대한 명제라 하자. 그럼 <phrase>$x\in B$인 것</phrase>과 <phrase>$P(x)$인 것</phrase>이 동치이도록 하는 집합 $B$가 존재한다.

앞서 새로 도입한 comprehension schema 상에서는 위와 달리 $\mathcal{S}=\\{x:x\not\in x\\}$를 바로 정의할 수는 없고, 이미 존재하는 집합 $A$에 대해 

$$B=\{x\in A:x\not\in x\}$$

만을 정의할 수 있다. 하지만 집합 $\mathcal{S}$와는 달리 이 집합은 어떠한 모순도 만들지 않는다. 

- 만일 $B\in B$라면 정의에 의해 $B\not\in B$이고 $B\in A$이므로 모순이다. 
- 만일 $B\not\in B$라면 $B\not\in A$ **이거나** $B\in B$이다. 

둘째 경우에서 $B\in B$라면 모순이므로 반드시 $B\not\in A$이고, 이를 통해 러셀의 역설과 같은 모순이 예방된다.

</div>

<div class="example" markdown="1">

<ins id="ex4">**예시 4**</ins> 위의 예시는 집합 $A$가 주어졌을 때, $A$에 속하지 않는 집합 $B$가 항상 존재한다는 것을 보여준다. 특히 <em_ko>모든 집합들의 집합</em_ko>, 즉 전체집합은 존재하지 않는다.  

</div>

명제 $P$를 적당하게 잘 잡아주면 comprehension schema로부터 우리가 알고 있는 여러 집합들을 만들 수 있다.

<div class="example" markdown="1">

<ins id="ex5">**예시 5**</ins> 임의의 집합 $A$, $B$에 대하여, $x$에 대한 성질 $P$가 $x\in B$로 주어졌다 하자. 그럼 집합 

$$\{x\in A:P(x)\}$$

은 $A$와 $B$에 동시에 속하는 원소들의 모임이다. 앞서 말한 것과 같이 이 집합은 성질 $P(x)$에 의해 유일하게 결정되므로, 이 집합을 우리는 $A$와 $B$의 *교집합*이라 정의하고, $A\cap B$로 적을 수 있다.

</div>

<div class="example" markdown="1">

<ins id="ex6">**예시 6**</ins> 이번에는 주어진 두 개의 집합 $A$, $B$에 대하여, $x$에 대한 성질 $Q$가 $x\not\in B$로 주어졌다 하자. 그럼 집합 

$$\{x\in A:Q(x)\}$$

은 $A$에는 속하지만 $B$에는 속하지 않는 원소들의 모임이다. 이 집합도 마찬가지로 유일하게 결정되므로, 이를 $A$에 대한 $B$의 *차집합*이라 부르고 $A\setminus B$로 적는다.

</div>

혹은, $A\setminus B$를 *$A$에 대한 $B$의 여집합*이라고도 부른다. 

<div class="remark" markdown="1">

<ins id="rmk1">**참고**</ins> 공리적인 집합론에서 단순히 *$B$의 여집합*이라는 것은 존재하지 않는다. 이를 정의하기 위해서는 전체집합이 필요하기 때문이다. 

</div>

잠시 멈춰서 우리가 알고 있는 집합이 뭐가 있는지 살펴보자. 

1. 우선 axiom of existence에 의해 그 존재성이 보장되는 $\emptyset$이 있다. 
2. Axiom of extensionality는 새로운 집합을 알려주는 공리는 아니므로 $\emptyset$ 이외의 집합을 만드는 데에는 도움이 되지 않는다.
3. 1번과 2번에서 존재성이 보장된 집합은 $\emptyset$ 뿐인데, 이 $\emptyset$에 comprehension schema를 적용하여 얻어진 집합은 $\emptyset$ 뿐이라는 것을 어렵지 않게 확인할 수 있다.

우리는 공리를 세 개나 도입했지만 존재성이 확실하게 보장된 집합은 오직 $\emptyset$ 뿐이다. 때문에 적당한 방법을 통해 공집합으로부터 새로운 집합을 만드는 방법 또한 공리로써 채택해야 한다.  
  
출발점이 되는 공리는 다음의 공리다.

<div class="misc" markdown="1">

**The Axiom of Pair.<sub>짝 공리</sub>** 임의의 집합 $A$, $B$에 대하여, <phrase>$x\in C$인 것</phrase>과 <phrase>$x=A$이거나 $x=B$인 것</phrase>이 동치이도록 하는 집합 $C$가 존재한다.

</div>

언제나처럼 이러한 집합이 유일하다는 증명을 반복하고 나면 이 집합을 $\\{A, B\\}$로 적을 수 있다.

우리가 갖고 있는 유일한 집합인 $\emptyset$을 사용하여 $A=B=\emptyset$으로 두면 집합 $\\{\emptyset, \emptyset\\}$이 생기며, 다음의 동치관계

$$x\in \{\emptyset\}\iff x=\emptyset\iff (x=\emptyset)\wedge(x=\emptyset)\iff x\in \{\emptyset,\emptyset\}$$

로부터 $\\{\emptyset, \emptyset\\}=\\{\emptyset\\}$임을 안다. 또 $\emptyset\not\in \emptyset$이므로 $\emptyset\neq\\{\emptyset\\}$이다. 


<div class="misc" markdown="1">

**The Axiom of Union.<sub>합집합 공리</sub>** 임의의 집합 $\mathcal{S}$에 대하여, <phrase>$x\in U$인 것</phrase>과 <phrase>어떤 $A\in\mathcal{S}$에 대하여 $x\in A$인 것</phrase>이 동치이도록 하는 집합 $U$가 존재한다.

</div>

예를 들어, 만일 $\mathcal{S}=\\{A,B\\}$였다면 $U$는 <phrase>$x\in A$이거나 $x\in B$인 원소들의 집합</phrase>, 즉 $A\cup B$가 된다는 것을 확인할 수 있다. 이를 표기상 $\bigcup\mathcal{S}$와 같이 쓰기도 하는데, 이 표기 자체를 자주 사용하지는 않을 것이다.

새로운 집합을 만들어내는 마지막 과정은 다음과 같다.

<div class="misc" markdown="1">

**The Axiom of Power set.<sub>멱집합 공리</sub>** 임의의 집합 $S$에 대하여, <phrase>$X\in \mathcal{P}$인 것</phrase>과 <phrase>$X\subseteq S$인 것</phrase>이 동치이도록 하는 집합 $\mathcal{P}$가 존재한다.

</div>

이 집합을 $S$의 *멱집합*, 즉 *power set*이라 부르고 $\mathcal{P}(S)$와 같이 표현한다. 





---
**참고문헌**

**[HJJ]** K. Hrbacek, T.J. Jeck, and T. Jech. *Introduction to Set Theory*. Lecture Notes in Pure and Applied Mathematics. M. Dekker, 1978.  
**[Bou]** N. Bourbaki. *Elements of the History of Mathematics*. Springer, 2013  
Wikipedia, [Naive set theory](https://en.wikipedia.org/wiki/Naive_set_theory), [Set-theoretic definition of natural numbers](https://en.wikipedia.org/wiki/Set-theoretic_definition_of_natural_numbers).

---

[^1]: 앞으로도 집합들의 집합을 나타내기 위해 캘리그래피를 사용할 것이다.
[^2]: 이를 *vacuous truth<sub>항진적 참</sub>*이라고 한다. 
