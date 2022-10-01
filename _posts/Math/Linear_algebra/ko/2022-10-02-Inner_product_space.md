---

title: "내적공간"
excerpt: "실수집합 위에서 정의된 내적의 성질"

categories: [Math / Linear Algebra]
permalink: /ko/math/linear_algebra/inner_product_space
sidebar: 
    nav: "linear_algebra-ko"

header:
    overlay_image: /assets/images/Linear_algebra/Inner_product_space.png
    overlay_filter: 0.5

date: 2022-10-02
last_modified_at: 2022-10-02

weight: 17

---

## 내적과 노름

이제 우리는 더 특수한 경우를 생각한다. 

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> $\mathbb{R}$-벡터공간 $V$ 위에 정의된 symmetric bilinear form $(-,-)$이 *내적<sub>inner product</sub>*이라는 것은 모든 $v\in V$에 대하여 $\langle v,v\rangle\geq 0$이고, 이 때 등호는 오직 $v=0$일 때만 성립하는 것이다. 내적이 주어진 공간 $V$를 간단하게 *내적공간<sub>inner product space</sub>*이라 부른다.

</div>

정의를 살펴보면, 내적의 정의에서 $\langle v,v\rangle\geq 0$이라는 조건은 field $F$가 대소관계의 개념을 가지고 있어야 하기 때문에 일반적인 field $F$에 대해서는 잘 정의되지 않는다는 것을 알 수 있다. 때문에 우리는 대소관계가 잘 정의되어 있는 field인 $\mathbb{R}$에서만 이론을 전개하고, 다음 글에서는 이를 이용하여 $\mathbb{C}$에서도 내적을 정의한다.

$\mathbb{R}$-벡터공간 위에 내적이 정의된다면, 가장 좋은 것 중 하나는 벡터의 <em_ko>크기</em_ko>가 잘 정의된다는 것이다.

<div class="definition" markdown="1">

<ins id="df2">**정의 2**</ins> $\mathbb{R}$-벡터공간 $V$ 위에 정의된 *norm<sub>노름</sub>*은 다음의 조건을 만족하는 함수 $\lVert -\rVert:V\rightarrow\mathbb{R}$이다.

1. $\lVert v\rVert\geq 0$이 모든 $v$에 대하여 성립하며, 특히 등호는 오직 $v=0$일 때만 성립한다.
2. 임의의 $\alpha\in\mathbb{R}$과 $v\in V$에 대하여, $\lVert\alpha v\rVert=\lvert\alpha\rvert\lVert v\rVert$이 성립한다.
3. (삼각부등식) 임의의 $u,v\in V$에 대하여, $\lVert u+v\rVert\leq\lVert u\rVert+\lVert v\rVert$가 성립한다.

</div>

<div class="proposition" markdown="1">

<ins id="pp3">**명제 3**</ins> $\mathbb{R}$-벡터공간 $V$ 위에 정의된 내적 $(-,-)$에 대하여, 다음의 식

$$\lVert v\rVert:=(v,v)$$

으로 정의된 함수 $\lVert-\rVert:V\rightarrow \mathbb{R}$은 norm이 된다.

</div>