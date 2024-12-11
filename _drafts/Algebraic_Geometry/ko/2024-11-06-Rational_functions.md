---

title: "유리함수"
excerpt: ""

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/rational_functions
header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Rational_functions.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_geometry-ko"

date: 2024-11-06
last_modified_at: 2024-11-06
weight: 2

---

앞선 글에서 우리는 algebraic set $X$와 그 위에서 정의된 정칙함수들에 대해 살펴보았다. 이번 글에서는 irreducible algebraic set 위에서 정의된 유리함수들에 대해 살펴본다.

## 기약인 대수적 집합

임의의 위상공간 $X$에 대하여, $X$가 *irreducible<sub>기약</sub>*이라는 것은 $X$를 두 개 이상의 proper closed set들의 합집합으로 나타낼 수 없는 것이다. ([##ref##]()) 다음 정리는 임의의 algebraic set은 항상 irreducible closed set들의 유한한 합집합으로 분해할 수 있다는 것을 보여주는데, 그 증명에서 대수적인 개념과 기하적인 개념이 서로에게 어떠한 영향을 끼치는지도 눈여겨 볼만하다.

<div class="proposition" markdown="1">

<ins id="thm1">**정리 1**</ins> 임의의 algebraic set $X$는 항상 irreducible closed set들의 유한한 합집합으로 분해할 수 있다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

결론에 반하여 이것이 불가능하다 하자. 만일 $X$ 자신이 irreducible이었으면 그 자체로 irreducible closed set의 유한한 합집합이므로, $X$는 reducible이어야 한다. 따라서 두 proper closed set $X_1,X_1'$에 대하여 $X=X_1\cup X_1'$으로 쓸 수 있다. 마찬가지로 $X_1$과 $X_1'$이 동시에 irreducible일 수는 없으므로, $X_1$ 혹은 $X_1'$ 중 reducible인 것이 존재하고, 이와 같은 방식으로 

$$X\supsetneq X_1\supsetneq X_2\supsetneq\cdots$$

를 얻는다. 그런데 이로부터

$$I(X)\subsetneq I(X_1)\subsetneq I(X_2)\subsetneq\cdots$$

를 얻게 되고, 이는 $\mathbb{k}[\x_1,\ldots, \x_n]$이 noetherian이라는 사실에 모순이다. 

</details>

위의 증명에서 착안하여, $X$가 irreducible일 조건을 그 coordinate ring $\mathbb{k}[X]$에 대한 대수적인 조건으로 옮겨적을 수 있다. 

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> $X$가 irreducible algebraic set인 것은 $I(X)$가 $\mathbb{k}[\x_1,\ldots, \x_n]$의 prime ideal인 것과 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$X=X_1\cup X_2$가 reducible이라 하자. 그럼 $X\supsetneq X_1$이므로, $X_1$에서는 항등적으로 $0$이지만 $X$ 전체에서는 $0$이 아닌 다항식 $F_1\in \mathbb{k}[\x_1,\ldots, \x_n]$이 존재하고, 비슷한 방식으로 $X_2$에서는 항등적으로 $0$이지만 $X$ 전체에서는 $0$이 아닌 다항식 $F_2\in \mathbb{k}[\x_1,\ldots, \x_n]$을 택해올 수 있다. 그럼 이들의 곱 $F_1F_2$는 $X_1,X_2$ 모두에서 $0$이다. 즉, 이 다항식들이 정의하는 regular function들 $f_1, f_2\in \mathbb{k}[X]$를 생각하면 이들은 zerodivisor가 된다. 이 논리는 거꾸로도 성립하며, 따라서 $X$가 irreducible인 것과 $I(X)$가 prime ideal인 것이 동치이다.

</details>

## 유리사상

[명제 2](#prop2)에 의하여, $X$가 irreducible algebraic set이라면 $\mathbb{k}[X]$는 domain이 되고, 따라서 $\Frac \mathbb{k}[X]$가 잘 정의된다. 

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> Irreducible closed set $X$에 대하여, $\mathbb{k}[X]$의 field of fraction $\Frac \mathbb{k}[X]$를 $X$의 *function field*라 부르고 $\mathbb{k}(X)$로 적는다. $\mathbb{k}(X)$의 원소들을 $X$ 위에서 정의된 *rational function<sub>유리함수</sub>*들이라 부른다. 

</div>

그럼 정의에 의하여, $\mathbb{k}(X)$의 원소들은 적당한 $F, G\in \mathbb{k}[\x_1,\ldots, \x_n]$, $G\not\in I(X)$에 대하여 $F/G$의 꼴로 쓰여질 수 있다. 이는 특히 $X$의 어떤 점 $x$에서는 분모가 $0$이 될 수 있다는 것을 의미한다. 

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> Rational function $\varphi\in \mathbb{k}(X)$가 점 $x$에서 *regular*라는 것은 $f,g\in \mathbb{k}[X]$, $g(x)\neq 0$을 만족하는 $f,g$에 대하여 $\varphi=f/g$로 적을 수 있는 것이다. 이 때, $\varphi$의 함숫값 $\varphi(x)=f(x)/g(x)\in \mathbb{k}$가 잘 정의된다.

</div>

만일 유리함수를 $\mathbb{k}[\x_1,\ldots, \x_n]$의 원소들을 이용하여 $F/G$의 꼴로 적는다면, $\mathbb{k}$가 algebraically closed인 것으로부터 $G$가 상수함수가 아닌 한 $G(x)=0$이도록 하는 $x\in \mathbb{A}^n$이 반드시 존재한다. 이로부터 다음을 얻는다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> $X$ 위에서 정의된 rational function이 모든 점에서 regular라면, $X$는 regular function이다. 

</div>

Regular function에서 regular map을 정의했듯, 우리는 rational function으로부터 rational map을 정의할 수 있다. 

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> 두 algebraic set $X\subseteq \mathbb{A}^n$, $Y\subseteq \mathbb{A}^m$을 고정하자. 그럼 $X$ 위에서의 rational function들의 모임 $\varphi=(\varphi_1,\ldots, \varphi_m)$이 *rational map<sub>유리사상</sub>*이라는 것은 $\varphi_i$들이 모두 regular인 $x\in X$들에 대하여 항상 $\varphi(x)\in Y$가 성립하는 것이다. 이러한 $x$들에서 $\varphi$가 *regular*하다 말하고, 이 때 $\varphi$의 image는

$$\varphi(X)=\{\varphi(x): \text{$x\in X$ and $\varphi$ is regular at $x$}\}$$

로 정의한다. 

</div>

한편 [§대수적 집합, ⁋명제 8](/ko/math/algebraic_geometry/algebraic_sets)에서 살펴보았듯 