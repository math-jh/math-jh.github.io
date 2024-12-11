---

title: "영점정리"
excerpt: ""

categories: [Math / Commutative Algebra]
permalink: /ko/math/commutative_algebra/nullstellensatz
header:
    overlay_image: /assets/images/Math/Commutative_Algebra/Nullstellensatz.png
    overlay_filter: 0.5
sidebar: 
    nav: "commutative_algebra-ko"

date: 2024-10-20
last_modified_at: 2024-10-20
weight: 10

---

이제 우리는 [대수기하학](/ko/algebraic_geometry/)에서 중요하게 쓰이는 영점정리를 증명한다. 우선 다음을 정의하자.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Ring $A$가 *Jacobson ring<sub>제이콥슨 환</sub>*이라는 것은 임의의 prime ideal이 maximal ideal들의 교집합으로 나타나는 것이다.

</div>

그럼 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="lem2">**보조정리 2**</ins> Ring $A$에 대하여, 다음이 동치이다.

1. $A$가 Jacobson ring이다.
2. $A$의 prime ideal $\mathfrak{p}$에 대하여, $A/\mathfrak{p}[f^{-1}]$이 field이도록 하는 $f\in A/\mathfrak{p}$가 존재한다면, $A/\mathfrak{p}$는 field이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>



</details>

그럼 영점정리는 다음과 같이 서술할 수 있다.

<div class="proposition" markdown="1">

<ins id="thm3">**정리 3**</ins> Jacobson ring $A$와, finitely generated $A$-algebra $E$가 주어졌다 하자. 그럼 $E$도 Jacobson ring이다. 또, 만일 $\mathfrak{m}$이 $E$의 maximal ideal이라면 $\mathfrak{m}\cap A$는 $A$의 maximal ideal이며, $E/\mathfrak{m}$는 $A/(\mathfrak{m}\cap A)$의 finite field extension이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>



</details>

특히 대수기하학에서는 $A$가 field $\mathbb{k}$이고 $E=\mathbb{k}[\x_1,\ldots,\x_n]$인 경우를 많이 다루게 된다. 그럼 다항식들 $f_1,\ldots, f_r\in \mathbb{k}[\x_1,\ldots, \x_n]$에 대하여,

$$X=\{(x_1,\ldots, x_n)\in \mathbb{k}^n: f_1(x_1,\ldots, x_n)=\cdots=f_r(x_1,\ldots, x_n)\}\subseteq \mathbb{k}^n$$

은 $n$차원 공간 $\mathbb{k}^n$의 점들 중 방정식

$$f_1(\x_1,\ldots, \x_n)=\cdots=f_r(\x_1,\ldots, \x_n)=0$$

을 만족하는 점들의 모임이며, 이러한 방식으로 정의된 $X$를 *algebraic set<sub>대수적 집합</sub>*이라 부른다. 그럼 임의의 algebraic set $X$에 대하여, ideal $I(X)\subseteq \mathbb{k}[\x_1,\ldots, \x_n]$을

$$I(X)=\{f\in \mathbb{k}[\x_1,\ldots, \x_n]: f(x_1,\ldots, x_n)=0\text{ for all $(x_1,\ldots, x_n)\in X$}\}$$

으로 정의한다. 거꾸로 $\mathbb{k}[\x_1,\ldots, \x_n]$의 임의의 ideal $\mathfrak{a}$에 대하여, $\mathbb{k}^n$의 부분집합 $Z(\mathfrak{a})$를

$$Z(\mathfrak{a})=\{(x_1,\ldots, x_n)\in \mathbb{k}^n: f(x_1,\ldots, x_n)=0\text{ for all $f\in \mathfrak{a}$}\}$$

으로 정의할 수 있다. 그럼 고전적인 버전의 영점정리 ([명제 5](#prop5))는 $\mathbb{k}[\x_1,\ldots,\x_n]$의 radical ideal들과 $\mathbb{k}^n$의 algebraic subset 사이에 일대일대응이 있다는 것을 보여준다. 

<div class="proposition" markdown="1">

<ins id="lem4">**보조정리 4**</ins> Field $\mathbb{k}$가 주어졌다 하자. 그럼 $\mathfrak{m}=(\x_1-a_1,\ldots, \x_n-a_n)$은 $\mathbb{k}[\x_1,\ldots, \x_n]$의 maximal ideal이다. 또, 만일 $\mathbb{k}$가 algebraically closed라면 $\mathbb{k}[\x_1,\ldots,\x_n]/(f_1,\ldots, f_r)$의 maximal ideal들과, 다음 식

$$f_1(x_1,\ldots, x_n)=\cdots=f_r(x_1,\ldots, x_n)=0$$

을 만족하는 $(x_1,\ldots, x_n)$들 사이의 일대일 대응이 존재한다. 

</div>

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> Algebraically closed field $\mathbb{k}$와 ideal $\mathfrak{a}\subseteq \mathbb{k}[\x_1,\ldots, \x_n]$이 주어졌다 하자. 그럼 

$$I(Z(\mathfrak{a}))=\sqrt{\mathfrak{a}}$$

이 성립하며, 따라서 $I$와 $Z$는 $\mathbb{k}[\x_1,\ldots,\x_n]$의 radical ideal들과 $\mathbb{k}^n$의 algebraic subset 사이에 일대일대응을 정의한다.

</div>