---

title: "등급구조"
excerpt: "대수적 구조 위에 정의된 등급구조"

categories: [Math / Multilinear Algebra]
permalink: /ko/math/multilinear_algebra/graduation
header:
    overlay_image: /assets/images/Math/Multilinear_Algebra/Graduation.png
    overlay_filter: 0.5
sidebar: 
    nav: "multilinear_algebra-ko"

date: 2022-12-02
last_modified_at: 2022-12-02
weight: 1

---

이제 우리는 주어진 대수적 구조가 특정한 등급 $\Delta$에 의해 나뉘어진 구조를 살펴본다. 이 구조의 가장 자연스러운 예시는 polynomial algebra $A[\x]$로, $\x$의 차수에 따라 단항식들을 $0$차식, $1$차식 등과 같이 나눌 수 있다. 이를 $\mathbb{Z}^{\geq 0}$-graded algebra라고 부른다. 

이번 글에서 $(\Delta, +,0)$는 항상 commutative monoid를 뜻한다.

## 등급가환군

다음 정의에서 $\Delta$의 덧셈구조는 하는 일이 없지만, 이후 graded ring, graded module과 graded algebra를 정의하는 과정에서는 $\Delta$의 덧셈구조를 사용한다.

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> Abelian group $G$가 *$\Delta$-graded abelian group<sub>$\Delta$-등급가환군</sub>*이라는 것은 $G$의 subgroup들 $(G\_\alpha)\_{\alpha\in\Delta}$가 존재하여 $G=\bigoplus_{\alpha\in\Delta} G\_\alpha$가 성립하는 것이다.

이 경우, 원소 $x\in G$가 $x\in G\_\alpha$를 만족한다면 $x$가 *homogeneous of degree $\alpha$<sub>$\alpha$차 동차원소</sub>*라 부른다.

</div>

만일 $\Delta=\Delta_1\times\Delta_2$를 만족하는 두 monoid $\Delta_1,\Delta_2$가 존재한다면 $G$에 *bidegree*가 주어졌다고 표현한다. 즉

$$G=\bigoplus_{(\alpha,\beta)\in\Delta_1\times\Delta_2}G_{\alpha,\beta}$$

이라 쓸 수 있다. 이 경우, 고정된 $\alpha\in \Delta_1$와 $\beta\in\Delta_2$에 대하여, 다음의 식

$$G_\alpha'=\bigoplus_{\gamma\in\Delta_2}G_{\alpha,\gamma},\qquad G_\beta''=\bigoplus_{\gamma\in\Delta_1}G_{\gamma,\beta}$$

을 통해 $\Delta_1$-graded abelian group $G=\bigoplus_{\alpha\in\Delta_1}G_\alpha'$와 $\Delta_2$-graded abelian group $G=\bigoplus_{\beta\in\Delta_2}G_\beta''$을 각각 얻는다. 특히 $G_\alpha'\cap G_\beta''=G_{\alpha,\beta}$가 성립한다. 

## 등급환

본격적인 등급구조는 곱셈이 정의되며 등장하게 된다.

<div class="definition" markdown="1">

<ins id="df2">**정의 2**</ins> 주어진 ring $A$가 *$\Delta$-graded ring<sub>$\Delta$-등급환</sub>*이라는 것은 $(A,+,0)$이 $\Delta$-graded abelian group $A=\bigoplus_{\alpha\in\Delta}A_\alpha$인 동시에, 임의의 $\alpha,\beta\in\Delta$에 대해 

$$A_\alpha A_\beta\subseteq A_{\alpha+\beta}$$

이 성립하는 것이다.

</div>

예를 들어, $A[\x]$의 $A$-module 구조를 잊어버리고 이를 ring으로 생각한다면, 

$$A[\x]=\bigoplus_{n\geq 0}A\x^n$$

을 통해 $A$를 graded ring으로 생각할 수 있으며, 이 때 위의 조건 $A_\alpha A_\beta\subseteq A_{\alpha+\beta}$는 차수 $\alpha$의 단항식과 차수 $\beta$의 단항식을 곱할 경우, 차수 $\alpha+\beta$의 단항식이 나온다는 것을 뜻한다. 

<div class="proposition" markdown="1">

<ins id="pp3">**명제 3**</ins> Graded ring $A=\bigoplus A\_\alpha$에 대하여, $A_0$은 덧셈과 곱셈에 대하여 닫혀있다. 

만일 $\Delta$의 임의의 원소 $\alpha,\beta,\gamma$에 대하여 다음 식

$$\alpha+\gamma=\beta+\gamma\implies \alpha=\beta$$

이 성립하고, $1\in A$라면 $1\in A_0$ 또한 성립한다. 따라서 $A_0$은 $A$의 subring[^1]이 된다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 

$$A_0A_0\subseteq A_0$$

이 성립하고, 또 $A_0$은 덧셈에 대하여 닫혀있으므로 앞선 주장은 자명하다.

$A$가 $1$을 갖는다 가정하고, 

$$1=\sum_{\alpha\in \Delta} e_\alpha$$

이라 하자. 이제 임의의 $x\in A_\beta$에 대하여

$$x=1x=\sum_{\alpha\in\Delta}e_\alpha x$$

이고, 이 때 $\beta=\alpha+\beta$를 만족하는 $\alpha$는 $0$뿐이므로 양 변을 차수별로 비교하여 $x=e_0x$를 얻는다. 비슷하게 $x=xe_0$ 또한 증명할 수 있고, 이 두 식이 모든 homogeneous element에 대해 성립하므로 $A$의 임의의 원소에 대해서도 성립한다. 즉 $1=e_0\in A_0$이 성립한다.

</details>

## 등급가군

임의의 $A$-module에는 곱셈이 정의되지 않으므로 graduation을 정의하기가 조금 애매하지만, module이 *graded* ring $A$ 위에 정의되었다면 스칼라곱을 통해 graduation을 줄 수 있다.

<div class="definition" markdown="1">

<ins id="df4">**정의 4**</ins> $\Delta$-graded ring $A=\bigoplus A\_\alpha$이 주어졌다 하자. 그럼 $A$-module $M$이 *$\Delta$-graded left $A$-module<sub>$\Delta$-등급왼쪽가군</sub>*이라는 것은 $(M,+,0)$이 $\Delta$-graded abelian group $M=\bigoplus_{\alpha\in \Delta}M\_\alpha$인 동시에, 임의의 $\alpha,\beta\in\Delta$에 대하여

$$A_\alpha M_\beta\subseteq M_{\alpha+\beta}$$

이 성립하는 것이다. 비슷하게 $\Delta$-graded right $A$-module 또한 정의할 수 있다. 

</div>

특히 정의로부터 $A_0 M_\alpha\subseteq M_\alpha$가 성립하며, 이를 통해 임의의 $\alpha\in\Delta$에 대해 $M_\alpha$를 left $A_0$-module로 생각할 수 있다. 만일 $A$가 다음의 graduation

$$A_0=A,\quad A_\alpha=0\text{ for all $\alpha\neq 0$}\tag{1}$$

이 주어져있다면 $M_\alpha$들은 $M$의 submodule들이며, 거꾸로 $M$의 submodule들의 family $(M_\alpha)$가 $M=\bigoplus M_\alpha$를 만족한다면 항상 이를 통해 $M$을 graded $A$-module로 생각할 수 있다.

## 등급대수

마지막으로 다음을 정의한다.

<div class="definition" markdown="1">

<ins id="df5">**정의 5**</ins> $\Delta$-graded commutative ring $A=\bigoplus A\_\alpha$이 주어졌다 하자. 그럼 $A$-algebra $E$가 *$\Delta$-graded $A$-algebra<sub>$\Delta$-등급대수</sub>*라는 것은 $(E,+,0)$이 $\Delta$-graded abelian group $E=\bigoplus_{\alpha\in\Delta} E_\alpha$인 동시에 다음 식

$$A_\alpha E_\beta\subseteq E_{\alpha+\beta},\qquad E_\alpha E_\beta\subseteq E_{\alpha+\beta}$$

이 모두 성립하는 것이다.

</div>

대부분의 경우, $A$는 graduation이 없는 ring이고 $E$가 graduation $\Delta$가 주어진 상태이며, 위의 식 (1)을 통해 $A$에 trivial graduation을 주고 이를 graded $A$-algebra로 생각하는 것이 보통이다. 

---

**참고문헌**

**[Bou]** Bourbaki, N. Algebra I. *Elements of Mathematics*. Springer. 1998.  

---

[^1]: 정의에 의하여 $A$의 subring은 $(A,+,0)$의 subgroup인 동시에 곱셈에 대해 닫혀있는 집합이었고, 만일 $1\in A$라면 여기에 더하여 $1$까지 포함하는 것만 subring으로 생각하기로 하였다.