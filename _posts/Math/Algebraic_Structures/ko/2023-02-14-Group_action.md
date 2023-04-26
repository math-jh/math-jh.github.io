---

title: "군의 작용 (작성중)"
excerpt: "Group action"

categories: [Math / Algebraic Structures]
permalink: /ko/math/algebraic_structures/group_action
header:
    overlay_image: /assets/images/Math/Algebraic_Structures/Group_action.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_structures-ko"

date: 2023-02-14
last_modified_at: 2023-02-14
weight: 10

---

복잡한 대수적 구조를 다룰 때 유효한 전략 중 하나는 이 구조를 직접 분석하는 대신, 주어진 대수적 대상이 다른 대수적 대상에 어떻게 작용하는지를 살펴보는 것이다. 

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> 임의의 monoid $M$이 주어졌다 하고, 집합 $E$를 고정하자. $M$이 $E$ 위에 왼쪽에서 *act<sub>작용</sub>*한다는 것은 monoid homomorphism $\rho:M\rightarrow\Fun(E,E)$가 주어진 것이다. 이 때, 집합 $E$를 *left $M$-set*이라 부른다.

임의의 $\alpha\in M$과 $x\in E$에 대하여, 함숫값 $\rho(\alpha)(x)$를 간단히 $\alpha\cdot x$로 표기한다. 

</div>

여기서 $\Fun(E,E)$는 함수의 합성 $\circ$와 항등원 $\id_E$에 의해 자명한 monoid 구조가 주어져 있다. 바꿔 말하자면 $M$이 $E$에 왼쪽에서 act한다는 것은 임의의 $\alpha,\beta\in M$과 $x\in E$에 대하여, 다음의 식

$$(\alpha\beta)\cdot x=\alpha\cdot(\beta\cdot x),\qquad e\cdot x=x$$

이 성립하는 것이다.

일반적인 경우, 우리는 위와 같이 주어진 대상이 다른 대상에 왼쪽에서 act하는 경우를 생각하지만, 종종 오른쪽에서 act하는 것이 자연스러울 때도 있다. 이를 [정의 1](#df1)과 비슷한 형태로 정의하기 위해서는 다음 정의가 필요하다.

<div class="definition" markdown="1">

<ins id="df2">**정의 2**</ins> 임의의 마그마 $(M,\ast)$에 대하여, $M$의 *opposite magma<sub>반대 마그마</sub>* $(M^\op,\ast^\op)$는 다음과 같이 정의된 마그마이다.

1. $M^\op=M$이다.
2. 임의의 $x,y\in M^\op$에 대하여, $x\ast^\op y$는 $y\ast x$로 정의된다.

</div>

그럼 monoid의 *right action*은 다음과 같이 정의된다.

<div class="definition" markdown="1">

<ins id="df3">**정의 3**</ins> 임의의 monoid $M$과 집합 $E$에 대하여, $M$이 $E$ 위에 오른쪽에서 *act<sub>작용</sub>*한다는 것은 monoid homomorphism $\rho:M\rightarrow \Fun(E,E)^\op$가 주어진 것이다. 이 때, 집합 $E$를 *right $M$-set*이라 부른다.

임의의 $\alpha\in M$과 $x\in E$에 대하여, 함숫값 $\rho(\alpha)(x)$를 간단히 $x\cdot\alpha$로 표기한다.

</div>

이를 다시 쓰자면 

$$x\cdot(\beta\alpha)=(x\cdot\beta)\cdot\alpha,\qquad x\cdot e=x$$

라 할 수 있다. 

Left action과 right action은 표기상의 차이일 뿐, 본질적으로는 동일한 의미를 갖는다. 즉, $E$가 left $M$-set이라 하면 이는 자연스럽게 right $M^\op$-set으로 생각할 수 있고, 거꾸로 $E$가 right $M$-set이라 하면 이는 자연스럽게 left $M^\op$-set으로 생각할 수 있다. 따라서 앞으로 일반적인 이론을 전개할 때는 모든 action이 left action인 것으로 생각한다.