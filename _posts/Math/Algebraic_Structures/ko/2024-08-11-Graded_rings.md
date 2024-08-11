---

title: "등급환"
excerpt: ""

categories: [Math / Algebraic Structures]
permalink: /ko/math/algebraic_structures/graded_rings
header:
    overlay_image: /assets/images/Math/Algebraic_Structures/Graded_rings.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_structures-ko"

date: 2024-08-11
last_modified_at: 2024-08-11
weight: 106

---

## 등급환

Index set $I$가 commutative monoid일 경우, 우리는 ablian group들의 family $(A\_i)\_{i\in I}$들의 direct sum $\bigoplus\_{i\in I} A\_i$를 *graded abelian group*이라 부르기로 하였다. 당시에는 $A\_i$ 위에 어떠한 조건도 없었기 때문에 이는 별로 흥미로운 정의가 아니었으나, 이제는 $A\_i$ 위에 곱셈구조가 더해져 있으므로 이 정의가 더 의미를 갖게 된다. 

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Commutative monoid $I$와 $I$-indexed family of abelian groups $(A\_i)\_{i\in I}$가 주어졌다 하자. 만일 $\bigoplus\_{i\in I} A\_i$ 위에 정의된 곱셈구조가 이를 ring으로 만들고, 추가적으로 다음 조건

$$A_i A_j\subseteq A_{i+j}\qquad\text{for all $i,j\in I$}$$

을 만족한다면 $A$를 $I$로 index가 주어진 *graded ring<sub>등급환</sub>*이라 부른다. $A_i$에 속한 원소를 *homogeneous element<sub>동차원소</sub>*라 부른다.

</div>

정의에 의하여, $A$의 임의의 원소들은 homogeneous element들의 유한한 합으로 유일하게 표현할 수 있다. 

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> 만일 $I$의 임의의 원소가 cancellable이고 $\bigoplus\_{i\in I} A\_i$가 graded ring이라 하자. 그럼 $A_0$은 $A$의 subring이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$A_0A_0\subseteq A_0$으로부터 $A_0$이 곱셈에 대해 닫혀있음은 자명하다. 따라서 $A=\bigoplus A\_i$의 곱셈에 대한 항등원 $1$이 $A_0$에 속함을 보이면 충분하다. $1=\sum\_{i\in I} e_i$라 하자. 그럼 임의의 $x\in A\_j$에 대하여, 

$$x=1x=\sum_{i\in I} e_ix\in A_j$$

이고, 따라서 모든 $i\neq 0$에 대하서는 $e_ix=0$이고, $i=0$에 대해서만 $e_0x=x$가 성립한다. 이제 $A$의 임의의 원소는 homogeneous element들의 합으로 나타낼 수 있으므로 증명이 완료된다. 

</details>

대부분의 경우 우리가 관심있는 것은 $I=\mathbb{Z}$이거나 $I= \mathbb{N}$인 경우이다. 따라서 [명제 2](#prop2)의 전제조건이 만족된다. 

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> 임의의 abelian group $A$에 대하여, $A$에 의해 생성되는 free ring $F(A)$은 $\mathbb{N}$-graded ring이다. 

</div>

## 등급환 준동형사상

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> Commutative monoid $I$와 두 $I$-graded ring $A,A'$에 대하여, ring homomorphism $f:A \rightarrow A'$가 *graded homomorphism*이라는 것은 

</div>