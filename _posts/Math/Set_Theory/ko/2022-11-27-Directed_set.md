---

title: "유향집합"
excerpt: "유향집합과 lattice"

categories: [Math / Set Theory]
permalink: /ko/math/set_theory/directed_set
header: 
    overlay_image: /assets/images/Set_theory/Directed_set.png
    overlay_filter: 0.5
sidebar: 
    nav: "set_theory-ko"

date: 2022-11-27
last_modified_at: 2022-11-27
weight: 17

---

Preordered set $A$에 대하여, $X\subseteq A$가 $A$에서 *cofinal* (resp. *coinitial*)이라는 것은 임의의 $x\in A$에 대하여 $y\in X$가 존재하여 $x\leq y$ (resp. $y\leq x$)인 것이다. 예를 들어, 다음의 diagram

![cofinal_sequence](/assets/images/Set_theory/Directed_set-1.png){:width="420.6px" class="invert" .align-center}

에서 집합 $\left\\{a\_{2n}\right\\}\_{n\in\mathbb{N}}$, $\left\\{a\_{1000+n}\right\\}\_{n\in\mathbb{N}}$ 등은 모두 cofinal이다.

## Directed set

Hasse diagram에서, 큰 원소는 위쪽에 적는 것이 보편적이지만 바로 위의 diagram과 같이 큰 원소를 오른쪽에 적을 때도 있다.

<ins id="df1">**정의 1**</ins>  Preordered set $A$가 *right directed<sub>오른쪽으로 유향</sub>*이라는 것은 $A$의 원소 두 개짜리 임의의 부분집합이 bounded above인 것이다. 이와 비슷하게 preordered set $A$가 *left directed<sub>왼쪽으로 유향</sub>*라는 것은 $A$의 원소 두 개짜리 부분집합이 bounded below인 것이다.
{: .definition}

예컨대 임의의 집합 $A$에 대하여, 순서집합 $(\mathcal{P}(A),\subseteq)$는 right directed이다. 임의의 $X, Y\in\mathcal{P}(A)$에 대하여, $X\cup Y$는 $\mathcal{P}(A)$의 원소이고 $X$와 $Y$의 upper bound이기 때문이다. 이를 diagram으로 나타내면 다음과 같다.

![directed_system](/assets/images/Set_theory/Directed_set-2.png){:width="394.05px" class="invert" .align-center}

<ins id="pp2">**명제 2**</ins>  Ordered set $A$가 right directed라면 $A$의 maximal element는 greatest element이기도 하다.
{: .proposition}

<details class="proof" markdown="1">
<summary>증명</summary>

$A$가 right directed이므로, 임의의 $x\in A$와 maximal element $a$로 이루어진 집합 $\\{x,a\\}$의 upper bound $y$가 존재한다. 이제 $a$의 maximality에 의하여 $a=y$여야 하므로 $x\leq a$가 성립한다.
</details>

<div class="proposition" markdown="1">

<ins id="pp3">**명제 3**</ins> $(A_i)$가 right directed set들의 family라면 $\prod A\_i$ 또한 right directed이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$(x\_i),(y\_i)\in\prod A\_i$라 하자. 그럼 각각의 $i$에 대하여, $x\_i,y\_i\in A\_i$이고 $A\_i$는 right directed이므로 $x\_i,y\_i\leq z\_i$이도록 하는 $z\_i\in A\_i$가 존재한다. 이제 $(x\_i),(y\_i)\leq(z\_i)$이므로 $\prod A\_i$ 또한 right directed이다.

</details>

일반적으로 right directed set의 부분집합은 당연히 right directed가 아니다. 그러나 cofinal인 부분집합은 right directed임을 쉽게 확인할 수 있다.

<div class="definition" markdown="1">

<ins id="df4">**정의 4**</ins> Ordered set $A$가 *lattice*라는 것은 $A$의 임의의 원소 두 개짜리 부분집합이 supremum과 infimum을 갖는 것이다. 이 때, 두 원소 $\sup\\{x,y\\}$와 $\inf\\{x,y\\}$를 각각 $x,y$의 *join*과 *meet*이라 부르고, $x\vee y$와 $x\wedge y$로 적는다. 

</div>

Lattice $A$의 임의의 <em_ko>유한한</em_ko> 부분집합은 supremum과 infimum을 갖는다. 만일 $A$의 <em_ko>모든</em_ko> 부분집합이 supremum과 infumum을 갖는다면, $A$를 *complete lattice*라 부른다.

## Totally ordered set

<ins id="df5">**정의 5**</ins> Preordered set $A$에서의 두 원소 $x$, $y$가 *comparable<sub>비교가능</sub>*하다는 것은 명제 <phrase>$x\leq y$ 혹은 $y\leq x$</phrase>이 성립하는 것이다. 만약 집합 $A$의 임의의 두 원소가 comparable하다면, 이를 *totally ordered set<sub>전순서집합</sub>*이라 부른다.
{: .definition}

만약 $A$가 totally ordered set이라면, trichotomy가 성립한다. 즉,임의의 $x, y\in A$에 대하여,  

$$x=y,\qquad x < y,\qquad x > y$$

중 하나가 성립한다. 이 경우엔 $x\leq y$의 부정이 $x > y$가 된다. 하지만 totally ordered set이라는 조건이 빠진 상태에서 이는 일반적으로 성립하지 않는다. ([§순서관계의 정의, ⁋참고](/ko/math/set_theory/order_relations#rmk1))

<ins id="pp6">**명제 6**</ins> Totally ordered set $A$에서 ordered set $B$로의 모든 순단조함수 $f$는 단사함수다. 만약 $f$가 순증가라면, $f$는 $A$에서 $f(A)$로의 isomorphism이다.
{: .proposition}
<details class="proof" markdown="1">
<summary>증명</summary>

$f$가 순단조함수라 하자. 그럼 임의의 $x\neq y$에 대하여, $x > y$ 혹은 $x < y$가 성립하므로, $f(x) > f(y)$ 혹은 $f(x) < f(y)$이고, 따라서 $f(x)\neq f(y)$가 되어 $f$는 단사함수다. 특히 $f$가 순증가라면, 우리는 $f(x)\leq f(y)\implies x\leq y$라는 것을 보여야 하는데, 이는 대우명제가 자명하다.
</details>

위의 명제 또한 일반적인 ordered set에서는 성립하지 않았었다. ([§단조함수, ⁋참고](/ko/math/set_theory/monotone_functions#rmk2))

<ins id="pp7">**명제 7**</ins> $A$가 totally ordered set이고 $X$가 그 부분집합이라 하자. 그럼 $b\in A$가 $X$의 supremum인 것은 $b$가 $X$의 upper bound이고, $c < b$를 만족하는 임의의 $c\in A$에 대하여 $x\in X$이 존재하여 $c < x\leq b$인 것과 동치이다.
{: .proposition}

<details class="proof" markdown="1">
<summary>증명</summary>

자명.

</details>

$A$가 ordered set이고, $a\leq b$라 하자. 그럼 $a\leq x\leq b$를 만족하는 모든 $x$를 모아둔 $X\subseteq A$를 *닫힌구간<sub>closed interval</sub>*이라 부르고 $[a,b]$로 적는다. 구간 $(a,b)$는 *열린구간<sub>open interval</sub>*이라 부르고, 이는 $a < x < b$를 만족하는 모든 $x$를 모아둔 집합이다.  
추가로, $x\leq a$를 만족하는 모든 $x$를 모아둔 부분집합을 *unbounded*인 닫힌구간이라 부르고 $(-\infty, a]$로 적는다. $[a,\infty)$, $(-\infty, a)$, $(a, \infty)$도 유사하게 정의한다. 


<ins id="pp8">**명제 8**</ins> Lattice에서 두 interval의 교집합도 interval이다.
{: .proposition}

---
**참고문헌**

**[Bou]** N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---