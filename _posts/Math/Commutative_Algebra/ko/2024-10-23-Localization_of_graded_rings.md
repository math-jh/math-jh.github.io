---

title: "등급환의 국소화"
excerpt: ""

categories: [Math / Commutative Algebra]
permalink: /ko/math/commutative_algebra/localization_of_graded_rings
header:
    overlay_image: /assets/images/Math/Commutative_Algebra/Localization_of_graded_rings.png
    overlay_filter: 0.5
sidebar: 
    nav: "commutative_algebra-ko"

date: 2024-10-23
last_modified_at: 2024-10-23
weight: 4

---

우리는 임의의 graded ring, 더 일반적으로는 임의의 graded module을 localize하는 방법을 살펴본다. 이번 글에서는 별다른 말이 없다면 모든 graded ring은 $\mathbb{N}_{\geq 0}$-graded인 것으로 생각하고, $A=\bigoplus A_i$, $M=\bigoplus M_i$를 고정하기로 한다. 그럼 임의의 $n$에 대하여,

$$M(n)_k=M_{n+k}\qquad\text{for all $k$}$$

으로 정의된 $M(n)$은 자연스럽게 graded $A$-module 구조를 갖는다. 

한편, 우리는 [\[대수적 구조\] §등급환, ⁋명제 6](/ko/math/algebraic_structures/graded_rings#prop6)에서 임의의 homogeneous ideal은 항상 homogeneous element들로 생성됨을 보였는데, 이를 이용하면 다음을 보일 수 있다. 

<div class="proposition" markdown="1">

<ins id="lem1">**보조정리 1**</ins> Graded ring $A와 $A$의 homogeneous ideal들 $\mathfrak{a},\mathfrak{b}$에 대하여 다음이 성립한다. 다음이 성립한다.

1. $\sqrt{\mathfrak{a}}$는 homogeneous ideal이다. 
2. $(\mathfrak{a}:\mathfrak{b})$는 homogeneous ideal이다. 
3. 임의의 homogeneous element $a,b\in A$가 $ab\in \mathfrak{a}$를 만족할 때마다 $a\in \mathfrak{a}$ 혹은 $b\in \mathfrak{a}$가 성립한다 하자. 그럼 $\mathfrak{a}$는 prime ideal이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>



</details>

특히 임의의 ring의 prime ideal에서의 localization이 중요한 예시였던 것과 같이, $A$가 graded ring일 경우에도 *homogeneous* prime ideal $\mathfrak{p}$에서의 localization은 중요한 예시가 된다. 따라서 위 보조정리의 세 번째 결과는 특히 기억할만하다. 

어쨌든 우선 우리는 일반적인 경우부터 시작한다. 다음 명제는 원소들의 degree가 어떻게 행동하는지만 살펴보면 중명할 수 있으며 그 증명도 자명하다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> $A$의 multiplicative subset $S$의 모든 원소가 homogeneous라 하자. 그럼 임의의 homogeneous element $x\in M_n$과 $s\in S$에 대하여, $x/s\in S^{-1}M$를 degree $n-\deg s$에 있는 것으로 정의하면 $S^{-1}M$는 $\mathbb{Z}$-graded $A$-module의 구조를 갖는다. 

</div>

만일 $M=A$인 경우, 위의 정의는 $S^{-1}A$ 위에 정의된 곱셈에 대하여도 잘 작동하여 $S^{-1}A$를 graded ring으로 만든다는 것을 알 수 있다. 

우리는 canonical inclusion $A_0 \hookrightarrow A$를 통해 $S^{-1}M$을 $A_0$-module로 생각할 수 있으며, $S^{-1}M$의 degree $0$ 부분 $(S^{-1}M)_0$을 생각하면 이는 $A_0$-module 구조를 갖는다. 마찬가지로 $M=A$인 경우로 한정하여 생각하면, degree $0$ 부분은 곱셈에 대하여도 닫혀있으므로 $(S^{-1}A)_0$은 ring의 구조를 갖는다.

특별히 중요한 예시 중 하나는 degree $1$의 homogeneous element $f\in A_1$에 대하여 $S=\\{1,f,f^2,\cdots\\}$인 경우이다. 이 경우 다음 명제가 성립하며, 그 증명도 자명하다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> 위와 같은 상황에서 $S^{-1}A\cong (S^{-1}A)_0[\x,\x^{-1}]$이 성립한다. 여기에서 $\x$는 degree $1$을 주는 형식적인 변수이다. 

</div>

## 동차국소화

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> 앞서 정의한 $(S^{-1}A)_0$와 $(S^{-1}M)_0$을 각각 $A$와 $M$의 *homogeneous localization<sub>동차국소화</sub>*이라 부른다.

</div>

이번 글의 목표는 이들을 우리가 알고 있는 방식으로 표현하는 것이다. 남은 글에서, 임의의 graded $A$-module $M$에 대하여 

$$M^{(d)}=\bigoplus_{k\geq 0} M_{kd}$$

으로 적기로 한다. 또, 임의의 homogeneous element $f\in A$에 대하여, $S=\\{1,f,f^2,\cdots\\}$으로 얻어지는 homogeneous localization $(S^{-1}M)\_0$을 $M\_{(f)}$으로 적기로 한다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> Degree $d$의 homogeneous element $f\in A$를 고정하자. 그럼 다음의 isomorphism

$$M_{(f)}\cong M^{(d)}/(f-1)M^{(d)}$$

이 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

주어진 isomorphism은 적당한 $u:M^{(d)} \rightarrow M_{(f)}$에 first isomorphism theorem을 적용하여 얻어지며, $u$는 다음의 식

$$u_k:M_{kd} \rightarrow M_{(f)};\qquad x\mapsto x/f^k$$

을 통해 얻어진다. 그럼 $u$가 surjective인 것과 $\ker u=(f-1)M^{(d)}$인 것을 어렵지 않게 보일 수 있다. 

</details>

만일 $\deg f=1$이라면 위의 isomorphism은 $M_{(f)}\cong M/(f-1)M$으로 쓸 수 있다. 편의상 $S$가 degree $1$의 원소를 하나 이상 포함한다 하면, [명제 3](#prop3)을 각각의 원소에 적용하여 다음을 얻는다. 

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> $S$가 degree $1$의 원소를 적어도 하나 포함하는 homogeneous multiplicative set이라면 $S^{-1}A\cong (S^{-1}A)_0[\x,\x^{-1}]$이 성립한다.

</div>

특별히 homogeneous prime ideal $\mathfrak{p}$을 하나 고정하고, $\mathfrak{p}$가 $A\_1$을 전부 포함하지 않는다고 가정하자. $S=A\setminus \mathfrak{p}$로 얻어지는 homogeneous localization $(S^{-1}A)\_0$을 $A\_{(\mathfrak{p})}$로 쓰기로 하면, 앞선 명제로부터 다음의 식

$$A_{\mathfrak{p}}\cong A_{(\mathfrak{p})}[\x,\x^{-1}]$$

을 얻는다. 한편, 위와 같은 상황에서는 $f\in A_1\setminus \mathfrak{p}$인 homogeneous element $f$를 찾을 수 있으며, 이 때 [명제 5](#prop5)에 의하여 canonical map $p:A \rightarrow A/(f-1)$이 존재한다. 

<div class="proposition" markdown="1">

<ins id="lem7">**보조정리 7**</ins> 위의 상황에서, $\mathfrak{p}$의 $p$에 의한 image $\mathfrak{q}=\im \mathfrak{p}$는 prime ideal이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>


</details>

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> 위와 같은 상황에서, $A\_{(\mathfrak{p})}=(A/(f-1))_{\mathfrak{q}}$이 성립한다. 

</div>