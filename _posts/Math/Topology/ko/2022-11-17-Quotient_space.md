---

title: "몫공간"
excerpt: "부분공간의 성질들"

categories: [Math / Topology]
permalink: /ko/math/topology/quotient_space
header:
    overlay_image: /assets/images/Math/Topology/Quotient_space.png
    overlay_filter: 0.5
sidebar: 
    nav: "topology-ko"

date: 2022-11-17
last_modified_at: 2022-11-17
weight: 10

---

이제 우리는 몫집합 위에 위상을 정의하는 방법을 살펴본다. ([\[집합론\] §동치관계, ⁋정의 6](/ko/math/set_theory/equivalence_relations#def6))

## Locally closed subspace

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 위상공간 $X$가 주어졌다 하자. 부분집합 $A$가 $x\in A$에서 *locally closed*라는 것은 $X$에서 $x$의 근방 $V$가 존재하여, $A\cap V$가 $V$에서 닫힌집합인 것이다. 만약 $A$가 모든 $x\in A$에서 locally closed라면 $A$ 자체를 locally closed라 부른다.

</div>

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> 위상공간 $X$와 부분집합 $A$에 대하여 다음이 모두 동치이다.

1. $A$가 $X$에서 locally closed이다.
2. $A$은 $X$의 열린집합과 닫힌집합의 교집합이다.
3. $A$은 자기 자신의 ($X$에서의) closure $\cl A$에 대하여 열린집합이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $A$가 locally closed라 하고, 임의의 $x\in A$에 대하여 [정의 1](#def1)의 조건을 만족하는 $X$에서의 $x$의 열린근방을 $V_x$라 하자. 그럼 $U=\bigcup\_{x\in A} V\_x$는 열린집합이다. 또, [§부분공간, ⁋명제 6 (1)](/ko/math/topology/subspace#prop6)을 적용하면 $A$는 $U$에서 닫힌집합임을 안다. 따라서 $X$의 적당한 닫힌집합 $C$에 대하여 $A=U\cap C$이므로 둘째 조건이 성립한다.

이제 $X$의 열린집합 $U$와 닫힌집합 $C$에 대하여 $A=U\cap C$가 성립한다고 가정하자. 그럼 $\cl A\subseteq C$이므로,

$$A\subseteq U\cap\cl A\subseteq U\cap C=A$$

가 성립하고, 특히 $A=U\cap\cl A$이다. 이로부터 $A$가 $\cl A$의 열린집합임을 안다.

마지막으로 만일 $A=U\cap\cl A$를 만족하는 $X$의 열린집합 $U$가 존재한다면, $A$는 집합 $U$의 닫힌집합이고 따라서 locally closed이다.

</details>

특히 2번 조건으로부터, 연속함수 $f:X\rightarrow Y$와 $Y$의 locally closed subset $B$가 주어졌다면 $f^{-1}(B)$ 또한 $X$에서 locally closed임을 알 수 있다. 

## 몫공간

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> 위상공간 $X$가 주어졌다 하고, 집합 $X$ 위에 동치관계 $R$이 주어졌다 하자. 그럼 $R$에 의한 $X$의 *몫공간<sub>quotient space</sub>*은 canonical projection $p:X\rightarrow X/R$에 의해 정의되는 final topology가 주어진 공간 $X/R$을 의미한다.

</div>

[§Initial topology와 final topology, ⁋명제 5](/ko/math/topology/initial_and_final_topology#prop5)에 의하여 $X/R$에서의 열린집합은 정확하게 $p^{-1}(U)$가 $X$에서 열린집합이도록 하는 집합을 의미한다.[^1] [\[집합론\] §동치관계의 예시들, ⁋정의 5](/ko/math/set_theory/examples_of_equivalence#def5)의 언어로 이를 풀어쓰면, $X/R$ 위의 열린집합들은 $R$에 대해 *saturated*인 $X$의 열린집합에 일대일로 대응된다는 것을 확인할 수 있다. 

한편 [§Initial topology와 final topology, ⁋명제 6](/ko/math/topology/initial_and_final_topology#prop6)에 의하여 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> 위상공간 $X$와 몫공간 $X/R$, 그리고 canonical projection $p:X\rightarrow X/R$이 주어졌다 하자. 임의의 위상공간 $Y$에 대하여, 함수 $f:X/R\rightarrow Y$가 연속인 것은 $f\circ p$가 $X$에서 $Y$로의 연속함수인 것과 동치이다.

</div>

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> 위상공간 $X$와, $X$ 위에 정의된 두 동치관계 $R,S$를 생각하자. 만일 $S$가 $R$보다 세밀한 동치관계라면, $X/S$ 위에 정의된 동치관계 $R/S$에 대하여 전단사함수 $(X/S)/(R/S)\rightarrow X/R$는 homeomorphism이 된다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$(X/S)/(R/S)\rightarrow X/R$이 전단사함수가 되는 것은 [\[집합론\] §동치관계의 예시들, ⁋정의 8](/ko/math/set_theory/examples_of_equivalence#def8)에서 이미 보인 것이다. [명제 4](#prop4)에 의하여, 이 함수가 연속인 것은 $X/S\rightarrow X/R$이 연속인 것과 동치이고, 다시 이 함수의 연속성은 $X\rightarrow X/R$이 연속인 것으로부터 얻어진다. 

이와 유사하게 $X/R\rightarrow(X/S)/(R/S)$의 연속성은 $X\rightarrow(X/S)/(R/S)$의 연속성으로부터 얻어지며, 이 함수는 두 연속함수의 합성

$$X\longrightarrow X/S\longrightarrow (X/S)/(R/S)$$

과 같으므로 연속이다. 

</details>

한편 위상공간 $X,Y$와 연속함수 $f:X\rightarrow Y$가 주어졌다 하고, $f$에 의해 정의된 동치관계 $R$을 생각하자. ([\[집합론\] §동치관계, ⁋정의 5](/ko/math/set_theory/equivalence_relations#def5)) 그럼 $f$의 canonical decomposition 

$$X\overset{p}{\longrightarrow}X/R\overset{\bar{f}}{\longrightarrow}f(X)\overset{i}{\longrightarrow}Y$$

을 생각할 수 있다. 이제 $f(X)$에 부분위상을 부여하면, [명제 4](#prop4)와 [§Initial topology와 final topology, ⁋명제 3](/ko/math/topology/initial_and_final_topology#prop3)에 의하여 $\bar{f}$가 연속인 것은 자명하다. 또, canonical decomposition의 정의에 의하여 $\bar{f}$는 전단사함수이다. 일반적으로 $\bar{f}$가 homeomorphism이 될 필요는 없지만 ([§연속함수, ⁋예시 5](/ko/math/topology/continuous_functions#ex5)), 다음의 성립한다. 

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> 위의 diagram에 대하여, 다음이 동치이다.

1. $\bar{f}$가 $X/R$에서 $f(X)$로의 homeomorphism이다. 
2. $R$에 대해 saturated인 열린집합 $U\subseteq X$에 대하여, $f(U)$는 $f(X)$에서 열린집합이다.
3. $R$에 대해 saturated인 닫힌집합 $C\subseteq X$에 대하여, $f(C)$는 $f(X)$에서 닫힌집합이다.

</div>

이는 두 번째 혹은 세 번째 조건이 정확히 $\bar{f}^{-1}$ 또한 연속이라는 의미이기 때문에 자명하다.

한편, 위와 동일한 상황에서 $f$의 <em_ko>연속인</em_ko> section $s:Y\rightarrow X$가 존재한다 하자. 그럼 $f$는 전사함수이므로 $i=\id_Y$이다. 이제 $\bar{f}$와 $p\circ s$는 모두 연속이며,

$$\bar{f}\circ(p\circ s)=f\circ s=\id_Y$$

이고, 위의 식의 왼쪽에 $\bar{f}^{-1}$, 오른쪽에 $\bar{f}$를 각각 합성해주면 

$$(p\circ s)\circ\bar{f}=\id_{X/R}$$

를 얻는다. 따라서 이 경우 $\bar{f}$는 homeomorphism이 된다. 

## 몫공간과 부분공간

이제 위상공간 $X$와 부분집합 $A$, $X$ 위에 주어진 동치관계 $R$을 생각하자. $p:X\rightarrow X/R$을 canonical projection이라 하면, $p\|\_A:A\rightarrow X/R$의 canonical decomposition

$$A\overset{q}{\longrightarrow}A/(R|_A)\overset{\overline{(p|_A)}}{\longrightarrow} f(A)\overset{j}{\longrightarrow}X/R$$

이 정의되며 위와 동일한 논증에 의해 $\overline{(p\|\_A)}$는 연속인 bijection이 된다. 다음 명제 또한 거의 자명하다.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> 위의 decomposition에서 다음이 모두 동치이다.

1. $\overline{(p\|\_A)}$가 homeomorphism이다.
2. $R\|\_A$-saturated인 열린집합 $U\subseteq A$은 $R$-saturated인 $X$의 열린집합과 $A$의 교집합이다.
3. $R\|\_A$-saturated인 닫힌집합 $C\subseteq A$은 $R$-saturated인 $X$의 닫힌집합과 $A$의 교집합이다.

</div>




[^1]: [§부분공간]에서와 마찬가지로, **[Mun]**에서는 이를 몫위상의 정의로 삼는다. 