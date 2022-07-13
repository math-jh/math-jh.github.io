---

title: "정렬집합의 성질들<sup>†</sup>"
excerpt: "Ordinal의 정의와 정렬집합의 성질들"

lang: ko

categories: [Math / Set Theory]
permalink: /ko/math/set_theory/well_ordering
header:
    overlay_image: /assets/images/Set_theory/Ordinals.png
    overlay_filter: 0.5
sidebar: 
    nav: "set-ko"

date: 2021-08-23
last_modified_at: 2022-04-14
weight: 15

---

## Ordinal의 엄밀한 정의

우리는 앞선 글에서 ordinal을 간략하게 소개한 후, 이를 정의하는 것은 well-ordered set을 정의한 이후로 미뤄뒀었다. 이제 우리는 ordinal number를 엄밀하게 정의할 준비가 되었다. 

<div class="proposition" markdown="1">

<ins id="pp1">**명제 1**</ins> Well-ordered set $E$의 segment들을 모두 모은 집합을 $E^\ast$라 하자. 그럼 이 집합 또한 포함관계에 의하여 well-ordered set이 된다. 또, 함수 $x\mapsto S_x$은 well-ordered set $E$와 $E^\ast\setminus\\{E\\}$ 간의 order isomorphism이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

함수 $S:x\mapsto S_x$가 $E$와 $E^\ast\setminus\\{E\\}$ 간의 isomorphism을 정의한다는 것을 보이기 위해, 우리는 [§순서관계 (2), 명제 16](/ko/math/set_theory/order_relations_2#pp16)을 사용할 것이다. 따라서, $S$가 순증가이고 $S(E)=E^\ast\setminus\\{E\\}$임을 보이자. 

$S$가 증가함수인 것은 자명하다. 만약 $x\leq y$이고 $a\in S_x$라면, $a&lt;x\leq y$이므로 $a\in S_y$이기 때문이다. 또, 이 포함관계는 strict한데, 만약 $x&lt;y$라면, $x\not&lt;x$이고 $x&lt;y$이므로 $x\not\in S_x$지만 $x\in S_y$이기 때문이다. 따라서 함수 $S$는 $E$와 그 image 사이의 isomorphism이다. 그런데 [§서수와 정렬집합<sup>†</sup>,명제 5](/ko/math/set_theory/ordinals#pp5)와, 앞서 말한대로 어떠한 $S_x$도 $E$와 같아질 수 없다는 것을 종합하면 $S(E)=E^\ast\setminus\\{E\\}$이다.

마지막으로 $E^\ast$가 well-ordered임을 보이자. $S(E)$가 well-ordered이므로, $S(E)=E^\ast\setminus\\{E\\}$에 최대원소 $E$를 추가하면 ([§순서관계 (2), 명제 4](/ko/math/set_theory/order_relations_2#pp4)) $E^\ast$를 얻고, 이렇게 얻어진 집합은 다시 well-ordered이다. 

</details>

우리는 이전 글에서 motivation으로써 페아노 공리계를 만족하는 자연수의 모델을 소개했었는데, 사실은 이 명제가 모델의 motivation이라 보는 것이 타당하다. 이 명제는 well-ordered set의 원소들과, well-ordered set에 포함된 initial segment들 사이의 isomorphism을 보여준다. $E$의 원소 $a$를 $(-\infty, a)$와 같게 본다면, $a$보다 작은 원소는 $(-\infty, a)$의 원소여야 하고, 혹은 그러한 원소도 initial segment로 본다면, $(-\infty,a)$의 부분집합이어야 한다. 따라서, 이걸 거꾸로 생각하면 well-ordered set을 정의할 때, 

> 각각의 well-ordered set은, 자신보다 작은 well-ordered set들에 $\subset$으로 포함관계가 주어진 집합이다.

로 정의된 것처럼 취급해도 된다는 뜻이다. 

<div class="definition" markdown="1">

<ins id="df2">**정의 2 (von Neumann)**</ins> 집합 $S$가 *ordinal<sub>서수</sub>*이라는 것은, $S$의 각각의 원소들이 $\in$으로 strictly well-ordered되어있고, 또 $S$의 각각의 원소들이 $S$의 부분집합이기도 한 것이다. 

</div>

우선, 임의의 ordinal은 $\in$이 strict ordering이므로 다른 ordinal과는 같을 수 없다. 또, $\emptyset$은 vacuous하게 ordinal이고, 모든 자연수들도 ordinal이 된다. 자연수를 나타내는 집합은 (유한집합이고 totally ordered set이므로) well-ordered set임은 자명하고, 또 예를 들어, $2\in 3=\\{0,1,2\\}$라면 $2=\\{0,1\\}$ 또한 $3$의 부분집합이 되기 때문이다. 일반적인 ordinal들은 그리스 소문자로 적는 것이 관례이다. 

더 일반적으로, 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="pp3">**명제 3**</ins> 만일 $\alpha$가 ordinal number라면, $\alpha$의 successor $S(\alpha)=\alpha\cup\\{\alpha\\}$ 또한 ordinal이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선, $S(\alpha)=\alpha\cup\\{\alpha\\}$의 모든 원소는 $S(\alpha)$의 부분집합이다. 집합 $\alpha$에 들어있던 원소들은 $\alpha$를 포함하는 집합인 $S(\alpha)$에도 들어있을 것이고, 우리가 새로 추가한 <em_ko>원소</em_ko> $\alpha$는 정의에 의해 $S(\alpha)$의 부분집합이기도 하다.   

</details>

다음 명제는 이렇게 successor funcion $S$를 도입하는 것보다 더더욱 일반적인 방법으로 <em_ko>더 큰</em_ko> ordinal을 만드는 방법을 보여준다. 

<div class="proposition" markdown="1">

<ins id="pp4">**명제 4**</ins> $(X_i)\_{i\in I}$가 well-ordered set들의 family이고, 어떠한 $i,j\in I$에 대해서도 $X_i$와 $X_j$ 중 어느 하나는 다른 하나의 segment라 하자. 그럼 집합 $E=\bigcup\_{i\in I}X_i$ 위에서의 유일한 order relation이 존재하며, 이 relation은 well-ordering이고 $X_i$의 segment는 $E$의 segment가 되며, $E$ 자기자신을 제외한 $E$의 segment는 어떤 $X_i$의 segment가 된다.

</div>

원하는 order relation의 존재성과 유일성을 직접 보이는 대신, 이 조건보다 더 약화된 조건 하에서 더 일반적인 결과를 보이자.

<div class="proposition" markdown="1">

<ins id="lem5">**보조정리 5**</ins> $(X\_\alpha)\_{\alpha\in A}, \subset)$가 

1. 이들은 ordered set들의 directed set이고, 
2. 만약 $X\_\alpha\subset X\_\beta$라면, <box>$X\_\beta$의 order relation을 $X\_\alpha$로 제한한 relation</box>이 <box>$X\_\alpha$의 relation</box>과 동일하다고 하자. 그럼 각각의 order relation 모두를 확장하는 $E=\bigcup\_{\alpha\in A} X\_\alpha$ 위의 order relation이 유일하게 존재한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

각각의 $X\_\alpha$에 대하여, $G\_\alpha$가 order relation들의 그래프라 하자. 만약 각각의 order relation을 확장하는 $E$ 위의 ordering $G$가 존재한다면, $G\_\alpha\subset G$이다. 반대로 만일 $(x,y)\in G$라면, 어떤 $X\_\alpha$, $X\_\beta$가 각각 $x$와 $y$를 포함하므로, right directedness에 의해 어떤 $X\_\gamma$가 존재하여  $x$와 $y$를 동시에 포함한다. 한편 $(x,y)\in G\_\gamma$이므로 $(x,y)\in\bigcup\_{\alpha\in A}G\_\alpha$이다. 따라서 만일 그러한 relation이 존재한다면 이는 유일하고, 그 그래프는 반드시 $\bigcup\_{\alpha\in A}G\_\alpha$가 되어야 한다.

따라서 이 $G=\bigcup\_{\alpha\in A}G\_\alpha$가 실제로 이 조건들을 만족함을 보이면 된다. (존재성) 우선 정의에 의해 $G$가 모든 $G\_\alpha$를 확장하는 것은 자명하므로, $G$가 order relation임을 보이자. 임의의 $x\in E$에 대하여, 만일 $x\in X\_\alpha$라면 $(x,x)\in G\_\alpha\subset G$가 되므로 $(x,x)\in G$이다.  비슷하게 만일 $(x,y)\in G$라면, 어떤 $X\_\gamma$가 존재하여 $x$와 $y$를 동시에 포함하며, 이 집합에서의 order relation들의 조건에 의해 $(y,x)\in G\_\gamma\subset G$이다. Transitivity을 보이기 위해서는, $(x,y)\in G$와 $(y,z)\in G$를 가정한 후, $x$, $y$, $z$를 모두 포함하는 집합 $X\_\delta$를 찾아서 (directed 조건을 두 번 사용하면 된다), $(x,z)\in G\_\delta$로 결론을 내리면 된다.

</details>

이제 이렇게 정의된 order relation이 주어진 성질들을 모두 만족함을 보이면 된다.

<details class="proof--alone" markdown="1">
<summary>명제 4의 증명</summary>

우선 모든 $X_i$와 이들의 segment들이 $E$의 segment가 됨을 보이자. 임의의 $X_i$와 $x\in X_i$에 대하여, 어떠한 $y\in E$가 주어졌다고 하자. 그럼 어떤 $X_j$가 존재하여 $y\in X_j$이다. 이제 $y\leq x$라 하자. 그럼 $X_i$가 $X_j$의 segment이거나 $X_j$가 $X_i$의 segment이다. 만일 $X_i$가 $X_j$의 segment라면, $X_j$의 원소로서 $y\leq x$는 $y\in X_i$이다. 만약 반대로 $X_j$가 $X_i$의 segment였다면, $X_j\subset X_i$이고, 특히 $y\in X_i$이다. 어떤 경우이건 $y\in X_i$이고, 따라서 $X_i$는 $E$의 segment이다. $X_i$의 segment들도 비슷하게 $E$의 segment임을 보일 수 있다.

이제 $E$가 well-ordered임을 보이자. $H$가 $E$의 임의의 부분집합이라 하자. 그럼 어떤 $X_i$가 존재하여 $H\cap X_i\neq\emptyset$이다. Well-ordered set $X_i$의 부분집합으로서, $H\cap X_i$의 least element가 존재한다. 이를 $a$라 하자. 이제 $a$가 $H$의 least element임을 보일 것이다. 임의의 $x\in H$에 대하여, $x\in X_j$인 $X_j$가 존재하며, 이는 $X_i$의  segment이거나 $X_i$를 segment로 포함한다. 만일 $X_j$가 $X_i$의 segment라면, $x\in X_i$이고, 따라서 $x\in X_i\cap H$이고 $a\leq x$이다 (minimality of $a$). 반대로 $X_i$가 $X_j$의 segment라면, $x&lt;a$는 불가능하다. 그렇게 된다면 $x\in X_i$이므로 $a$의 minimality에 모순이기 때문이다. 어떠한 경우든, 임의의 $x\in H$에 대하여 $a\leq x$이므로 $a$는 $H$의 least element이다.

마지막으로, 임의의 segment $X$는 $(-\infty, x)$의 꼴이므로 $x\in X_i$이도록 $X_i$를 잡으면 $(-\infty, x)$는 $X_i$의 segment가 된다.

</details>

자연수에서 귀납법이 성립하는 가장 큰 이유는 각각의 자연수들이 $S$를 이용해서 순차적으로 정의되었기 때문이다. 그러나, 이 아이디어를 일반적인 ordinal로 확장하는 것은 다소 어려움이 있다. Ordinal $\omega+1$의 순서 구조를 살펴보면,

$$0,1,2,\cdots; \omega$$

와 같이 $\omega$ 이전에 무한히 많은 자연수들을 거쳐야 하기 때문에, 귀납법을 순차적으로 사용하는 것이 불가능하기 때문이다. 이건 $\omega$가 갖는 특정한 성질 때문이다. 즉, $\omega$ 이전에 나오는 $0,1,2,\cdots$는 $\omega$의 원소들인데, 이들이 maximal element를 갖지 않기 때문이다. 우선 이러한 상황을 다음과 같이 정의한다.

<div class="definition" markdown="1">

<ins id="df6">**정의 6**</ins> 임의의 ordinal $\alpha$에 대하여, $\alpha$의 maximal element $\beta$가 존재하면 $\alpha$를 *successor ordinal<sub>따름서수</sub>*이라 정의하고, 그렇지 않다면 $\alpha$를 *limit ordinal<sub>극한서수</sub>*이라 부른다.

</div>

만약 $\alpha$가 successor ordinal이고, $\beta$가 $\alpha$의 maximal element라면 $\alpha=S(\beta)=\beta+1$이라 할 수 있기 때문에 그러한 이름을 붙여주었다.  

하지만 limit ordinal의 존재에도 불구하고, ordinal에 대해서도 귀납법 비슷한 것을 사용하는 것이 가능하다. 

<div class="proposition" markdown="1">

<ins id="lem7">**보조정리 7 (Transfinite induction)**</ins> $E$가 well-ordered set이고, $\mathcal{S}$가 다음의 조건을 만족하는 segment들의 모임이라 하자.

1. $\mathcal{S}$는 임의의 합집합에 대하여 닫혀있다.
2. 만일 $S_a\in\mathcal{S}$라면, $S_a\cup\\{a\\}\in\mathcal{S}$

그럼 $E$의 모든 segment는 $\mathcal{S}$에 속한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

결론을 부정하여 모순을 찾자. $\mathcal{S}\subset E^\ast$이므로, $E^\ast\setminus\mathcal{S}$의 least element $S$가 존재한다. 만일 $S$가 greatest element를 갖지 않는다면, $S=\bigcup\_{x\in S}S_x$인데, 최소성에 의해 각각의 $S_x$는 $\mathcal{S}$의 원소이고, 1에 의해, $S\in\mathcal{S}$이다. 만일 $S$가 greatest element $a$를 갖는다면, $S=S_a\cup\\{a\\}$인데, 다시 최소성에 의해 $S_a\in\mathcal{S}$이다. 이제 (ii)에 의해 $S=S_a\cup\\{a\\}\in\mathcal{S}$여야 한다. 이는 모순이므로 $E^\ast\setminus\mathcal{S}$의 least element는 존재하지 않고, 따라서 $\mathcal{S}=E^\ast$이다.
</details>

여기에서, $E$는 어떤 큰 ordinal (limit ordinal이건 successor ordinal이건 상관 없이)이고, 따라서 귀납법을 일반화할 때 걸리적거렸던 limit ordinal의 존재가 이 보조정리를 통해 해소된다. 이것을 가능하게 만드는 것은 1번의 조건이다. 예를 들어, $\omega$는 $1,2,\ldots$의 무한한 합집합으로 만들 수 있기 때문이다.

이와 비슷하게, ordinal에 대해서도 transfinite recursion theorem을 만들어서 ordinal들의 연산을 정의할 수 있다. 하지만, 우리는 대부분의 경우에 ordinal들의 모임에 주어진 order relation이 궁금하기 때문에 이는 다루지 않기로 한다.

---
**참고문헌** 

**[HJJ]** K. Hrbacek, T.J. Jeck, and T. Jech. <i>Introduction to Set Theory</i>. Lecture Notes in Pure and Applied Mathematics. M. Dekker, 1978.  
**[Bou]** N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---



