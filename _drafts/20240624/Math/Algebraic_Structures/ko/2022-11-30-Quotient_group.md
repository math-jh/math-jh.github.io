---

title: "몫군"
excerpt: "정규부분군과 몫군"

categories: [Math / Algebraic Structures]
permalink: /ko/math/algebraic_structures/quotient_group
header:
    overlay_image: /assets/images/Math/Algebraic_Structures/Quotient_group.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_structures-ko"

date: 2022-11-30
last_modified_at: 2022-11-30
weight: 5

---

앞서 [§대수적 구조, §§몫구조](/ko/math/algebraic_structures/algebraic_structure#%EB%AA%AB%EA%B5%AC%EC%A1%B0)에서 우리는 동치관계 $R$이 마그마 $A$의 연산과 compatible할 경우 그 몫집합 $A/R$ 위에 자연스러운 방식으로 마그마 구조를 줄 수 있다는 것을 증명하였으며, 뿐만 아니라 [§준군, 모노이드, 군](/ko/math/algebraic_structures/group)의 말미에서 우리는 $A$가 group일 경우, 이 방식으로 만들어진 마그마 $A/R$ 또한 group이 된다는 것을 살펴보았다. 이 때 group $A/R$을 *quotient group<sub>몫군</sub>*이라 부른다.

## 정규부분군

한편 [\[집합론\] §동치관계, ⁋명제 7](/ko/math/set_theory/equivalence_relations#prop7)을 통해 우리는 다음 두 가지가 같다는 것을 안다.

집합 $G$에 동치관계 $R$을 주는 것 $\iff$ 집합 $G$의 분할 $(G\_i)\_{i\in I}$을 택하는 것
{: .text-center}

따라서, 동치관계 $R$이 $G$의 연산과 compatible할 것을 요구하는 것이 오른쪽에서는 어떠한 것을 의미하는지를 생각해볼 수 있다. 

우선 $R$이 $G$의 연산과 compatible하다고 가정하자. 그럼 $G/R$의 각 원소들이 $G$의 분할을 이루며, 특히 그 중 항등원을 포함하는 집합은 $[e]$ 뿐이다.

<div class="proposition" markdown="1">

<ins id="prop1">**명제 1**</ins> Quotient group $G/R$에 대하여, $[e]$는 $G$의 subgroup이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$a,b\in [e]$라 하자. 즉 $a\sim e\sim b$이다. 이제 $R$은 $G$의 연산과 compatible하므로, $a\sim b$의 양 변의 오른쪽에 $b^{-1}$을 곱하여 $ab^{-1}\sim e$를 얻는다. 즉 $ab^{-1}\in[e]$이므로 [§준군, 모노이드, 군, ⁋명제 12](/ko/math/algebraic_structures/group#prop12)에 의하여 $[e]$는 subgroup인 것을 안다.

</details>

반대로 $G$의 임의의 subgroup $H$가 주어졌다 하자. 위의 증명의 $[e]$를 $H$로 바꾸어 다음의 관계를 정의할 수 있다.

$$a\sim_{\tiny r}b\iff ab^{-1}\in H$$

이렇게 정의된 $\sim_{\tiny r}$이 동치관계라는 것을 쉽게 보일 수 있다. 이를 통해 quotient group을 정의하기 위해서는 이 동치관계가 $G$의 연산과 compatible해야 한다. 임의의 $a,b,c\in G$가 주어졌다 하자. 우선 만일 $a\sim_{\tiny r}b$가 성립한다 하면, 

$$(ac)(bc)^{-1}=acc^{-1}b^{-1}=ab^{-1}\in H$$

이므로 $ac\sim_{\tiny r} bc$이 성립한다. 즉 $\sim_{\tiny r}$은 $G$의 연산과 right compatible하다. 그러나

$$(ca)(cb)^{-1}=cab^{-1}c^{-1}$$

이므로, 일반적으로 $\sim_{\tiny r}$이 $G$의 연산과 left compatible일 필요는 없다. 그러나 만일 임의의 $x\in H$에 대하여, $cxc^{-1}\in H$가 모든 $c\in G$에 대해 성립한다면 우변은 $H$의 원소가 될 것이고, 따라서 $\sim_{\tiny r}$이 $G$ 위에 compatible한 동치관계를 정의한다.

<div class="remark" markdown="1">

<ins id="rmk1">**참고**</ins> 동치관계 $\sim_r$ 대신 다음의 관계

$$a\sim_{\tiny l} b\iff a^{-1}b\in H$$

를 정의했다면, $\sim_{\tiny l}$은 left compatible하며, 

$$(ac)^{-1}(bc)=c^{-1}(a^{-1}b)c$$

이므로 right compatible은 아니다. 이 관계가 right compatible이기 위해서는 임의의 $c\in G$와 임의의 $x\in H$에 대해 $c^{-1}xc\in H$가 성립해야 하며, 이는 위에서 얻어낸 조건과 같다.

</div>

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> Group $G$의 subgroup $H$가 *normal subgroup<sub>정규부분군</sub>*이라는 것은 임의의 $g\in G$와 임의의 $h\in H$에 대하여, $ghg^{-1}\in H$가 항상 성립하는 것이다.

</div>

한편, $g$를 임의로 택할 수 있으므로, $H$가 normal subgroup인 것은 임의의 $g$에 대하여 $gHg^{-1}=H$가 성립하는 것과 동치라는 것을 보일 수 있다. 위의 논의에 의하여, $G$의 normal subgroup $H$가 주어졌을 때 그에 해당하는 quotient group을 얻을 수 있다. 이 때 얻어지는 quotient group을 $G/H$로 적는다.

[명제 1](#prop1)에서, 임의의 $a\in [e]$에 대하여 다음 식

$$a\sim e\implies gag^{-1}\sim geg^{-1}=e$$

으로부터 $[e]$는 normal subgroup이 된다는 것을 안다. 또한 $H=[e]$로 두었을 때, 이에 해당하는 $\sim_{\tiny r}$은 정확하게 원래의 동치관계 $\sim$와 동일하므로 $G/H$와 $G/R$이 서로 같다. 거꾸로 임의의 normal subgroup $H$에서 정의된 $\sim_{\tiny r}$에 대해 $G/H=G/{\sim_{\tiny r}}$ 또한 성립한다. 이로부터 $G$에 compatible한 동치관계를 주는 것은 $G$의 normal subgroup을 택하는 것과 같음을 안다. 

## 잉여류

이제 group $G$와, 임의의 subgroup $H$를 생각하자. $H$가 normal이 아니더라도 위의 논의에서 얻어낸 $\sim_{\tiny r}$과 $\sim_{\tiny l}$은 어쨌든 동치관계이므로, <em_ko>몫집합</em_ko> $G/{\sim_{\tiny r}}$과 $G/{\sim_{\tiny l}}$이 어떻게 생겼는지를 살펴볼 수 있다. 

우선 $G/{\sim_{\tiny r}}$의 원소를 생각해보자. 임의의 $a\in G$와 그 equivalence class $[a]\_{\tiny r}$에 대하여,

$$x\in [a]_{\tiny r}\iff x\sim_{\tiny r} a\iff xa^{-1}\in H$$

임을 안다. 따라서 집합 $Ha$를 다음의 식

$$Ha:=\{ha\mid h\in H\}$$

으로 정의하면 $[a]\_{\tiny r}=Ha$가 성립한다. 비슷하게, $G/{\sim_{\tiny l}}$에 대하여는 $[a]\_{\tiny l}=aH$가 성립한다. 물론 $G$의 연산이 덧셈으로 적혀있었다면 이들은 각각 $H+a$와 $a+H$로 적는 것이 관례이다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> 위에서 정의한 두 집합 $Ha$와 $aH$를 각각 *right coset<sub>오른쪽 잉여류</sub>* 그리고 *left coset<sub>왼쪽 잉여류</sub>*이라 부른다.

</div>

따라서 $G$의 임의의 subgroup $H$가 주어졌을 때, 두 동치관계 $\sim_{\tiny r}$과 $\sim_{\tiny l}$은 $G$를 각각 right coset들과 left coset들로 분할한다. 이 경우 $\sim_{\tiny r}$에 의한 $G$의 몫집합은 $H\setminus G$, 그리고 $\sim_{\tiny l}$에 의한 $G$의 몫집합은 $G/H$로 적는다.[^1] 일반적으로 $Ha\neq aH$이지만, 사실 $Ha=aH$가 성립할 필요충분조건은 $H$가 normal이라는 것을 쉽게 확인할 수 있다.

뿐만 아니라, 임의의 $a\in G$에 대하여

$${a\cdot}: H\rightarrow aH;\quad h\mapsto ah,\qquad {a^{-1}\cdot}: aH\rightarrow H;\quad ah\mapsto h$$

은 서로의 역함수임을 알 수 있으므로 right coset들과 left coset들은 모두 $H$와 같은 cardinality를 갖는 것을 알 수 있다. 또한 함수 $H\setminus G\rightarrow G/H$를 다음의 식

$$Ha\mapsto a^{-1}H$$

으로 정의하면 이 함수가 전단사임을 쉽게 확인할 수 있다. 즉 $\lvert H\setminus G\rvert=\lvert G/H\rvert$이다.

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> Group $G$와 subgroup $H$에 대하여, $H$의 *index* $[G:H]$를 $\lvert G/H\rvert$으로 정의한다.

</div>

앞서 살펴본 $G/H$의 구조와 $G/H$의 각 원소들의 크기로부터 다음 명제가 자명하다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5 (Lagrange)**</ins> Group $G$와 subgroup $H$에 대하여 $\lvert G\rvert=[G:H]\lvert H\rvert$이 성립한다.

</div>

이 명제는 $G$ 혹은 $H$가 무한집합일 때에도 성립하지만, 특별히 이들이 유한일 경우, <phrase>Group $G$의 임의의 subgroup $H$에 대하여, $\lvert H\rvert$는 $\lvert G\rvert$의 약수</phrase>라는 결과를 얻는다.

---

**참고문헌**

**[Bou]** Bourbaki, N. Algebra I. *Elements of Mathematics*. Springer. 1998.  

---

[^1]: Right coset의 표기법은 차집합의 표기와 겹치지만, right coset을 많이 사용할 일은 없으므로 별도의 표기법을 정하지는 않기로 한다. 