---

title: "Grothendieck 군<sup>†</sup>"
excerpt: "Construction of abelian group from a commutative semigroup"

categories: [Math / Groups]
permalink: /ko/math/groups/grothendieck_group
header:
    overlay_image: /assets/images/Groups/Grothendieck_group.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_structures"

date: 2021-09-04
last_modified_at:
weight: 2

published: false

---
<div class="notice--warning" markdown="1">

이 글은 현재 수정중입니다.

이 글은 예전에 쓴 글로, 서술 방향이 마음에 들지 않거나 표기법이 마음에 들지 않아 전체적으로 수정이 진행중입니다. 읽으실 때 참고해주세요.

</div>


이제 본격적으로 군의 구조를 살펴보기 전에, 모노이드로부터 군을 얻는 방법을 간단히 소개하려 한다. 군에 대한 이야기를 할 때는 이 내용을 사용할 일이 없으므로 별도로 빼 두었지만, 이 아이디어는 환을 살펴보며 다시 나오게 된다. 

이 과정에서는 교환법칙이 거의 대부분의 문제를 해결해주기 때문에, 우리는 *가환모노이드*로부터 *가환군*을 얻어내는 과정을 소개한다. 사실은 주어진 모노이드의 항등원 어디에서도 사용하지 않으므로 가환인 준군만 가정해도 충분하다. 

## Universal mapping problem

가환인 준군 $(S, +)$가 주어졌다고 하자. (연산을 $+$로 주는 것은, 가환군의 연산을 덧셈으로 관례를 따른 것이다.) 우리의 목표는 $(S, +)$를 포함하는 가환군 $G_S$를 만드는 것이다. 뿐만 아니라, $G_S$는 $S$를 포함하기 위해 필요한 최소한의 조건만 만족하는 가환군이 될 것이다. 이는 종종 다음과 같은 universal mapping problem으로 주어진다.



>가환군 $G_S$와, 준동형사상 $\epsilon:S\rightarrow G_S$는 다음과 같은 성질을 만족하는 쌍이다.  
>
>![universal_property](/assets/images/Groups/Grothendieck_group-1.png){:width="120px"  class="invert" .align-center}
>     
>(Universal mapping problem) 임의의 가환군 $G$와, 임의의 준군 준동형사상 $f:S\rightarrow G$에 대하여, 군 준동형사상 $\overline{f}:G_S\rightarrow G$가 유일하게 존재하여 $f=\overline{f}\circ\epsilon$이 성립한다.

이 성질을 종종 *universal property*라고 표현하기도 한다. 

$G_S$에 대한 이 정의는 많은 정보를 담고 있다. 예를 들어, 위의 성질을 만족하는 $G_S$는 동형사상에 대해 유일하다.

<div class="proposition" markdown="1">

<ins id="pp1">**명제 1**</ins> 만일 어떠한 가환군 $H$과 준동형사상 $\eta$이 위의 universal mapping problem을 만족한다면 $G_S\cong H$가 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 다음 diagram을 살펴보자.

![uniqueness_1](/assets/images/Groups/Grothendieck_group-2.png){:width="160px"  class="invert" .align-center}

그럼 universal property에서, $\eta= \overline{\eta}\circ\epsilon$이도록 하는 $\overline{\eta}: G_S\rightarrow H$가 존재한다. 한편, 다시 다음의 diagram에서

![uniqueness_2](/assets/images/Groups/Grothendieck_group-3.png){:width="160px"  class="invert" .align-center}

$H$에 대한 universal property를 사용하면 $\epsilon=\overline{\epsilon}\circ\eta$이도록 하는 $\overline{\epsilon}:H\rightarrow G_S$가 존재한다. 그럼

$$\overline{\eta}\circ\overline{\epsilon}\circ\eta=\overline{\eta}\circ \epsilon=\eta=\id_{H}\circ \eta $$

이고, 다시 universal property에 의하여 $f\circ \eta=\eta$를 만족하는 $f$는 유일하므로 $f=\id_H=\overline{\eta}\circ \overline{\epsilon}$이 성립한다. 혹은, diagram의 언어로는, 다음 diagram을 commute하게 만드는 $H\rightarrow H$는 유일하므로 $\id_H=\overline{\eta}\circ \overline{\epsilon}$여야 한다.

![uniqueness_3](/assets/images/Groups/Grothendieck_group-4.png){:width="180px"  class="invert" .align-center}

비슷하게 $\id\_{G_S}=\overline{\epsilon}\circ \overline{\eta}$가 성립한다는 것도 보일 수 있고, 따라서 $G_S\cong H$가 성립한다.
</details>

한편, $S$가 이미 가환군이었다면, $G_S$는 $S$와 동형이어야 할 것이다.

<div class="proposition" markdown="1">

<ins id="pp2">**명제 2**</ins> 만일 $S$가 가환군이었다면, 위의 universal mapping problem을 만족하는 가환군 $G_S$는 $G_S\cong S$를 만족한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

*증명.* $S$와, 준동형사상 $\id_S$가 자명하게 universal property를 만족하므로, 앞선 [명제 1](#pp1)에 의하여 universal property를 만족하는 임의의 가환군은 $S$와 동형이어야 한다.

</details>

## Concrete construction

우리는 앞서 universal property로부터 $G_S$의 핵심적인 성질들을 증명했다. 하지만 이 논의들은 $G_S$가 실제로 존재한다는 것을 증명하지 않으면 아무런 의미도 없다. 따라서, 이제 제대로 construction을 한 번 해 보자.

$S$가 가환군이 될 수 없는 이유는 임의의 원소에 대한 역원이 존재하지 않을 수도 있기 때문이다. 따라서 우리는 곱 준군 $S\times S$를 생각한 후, $S\times S$의 둘째 부분을 *음수*부분으로 취급할 것이다.[^1] 즉, 직관적으로는 $S\times S$의 원소 $(a,b)$를 $a-b$로 취급할 것이다. 그럼 곱 준군에서의 연산

$$(a_1, b_1)+(a_2, b_2)=(a_1+a_2, b_1+b_2)$$

은 마치

$$(a_1+a_2)-(b_1+b_2)=(a_1-b_1)+(a_2-b_2)$$

를 나타내는 것처럼 생각할 수 있다. 

물론, 일반적으로 $a$와 $b$가 다르더라도 $a-b$의 값은 충분히 차이가 날 수 있기 때문에, 우리는 $S\times S$ 위에 동치관계 $R$을 다음과 같이 정의한다.[^2]

$$(a_1, b_1)\equiv (a_2, b_2)\pmod{R}\iff a_1+b_2+c=a_2+b_1+c\text{ for some $c\in S$}$$

우선 이 관계가 동치관계임을 보여야 한다.

<div class="proposition" markdown="1">

<ins id="lem3">**보조정리 3**</ins> 위에서 정의한 관계 $R$은 곱 준군 $S\times S$ 위에서의 연산과 compatible한 동치관계이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선, $R$이 동치관계임을 보이자. 임의의 $(a,b)\in S\times S$에 대하여, 

$$a+b+c=a+b+c$$

가 임의의 $c\in S$에 대해 성립하므로, $(a,b)\equiv(a,b)$이다. $(a_1,b_1)\equiv (a_2,b_2)$라 하자. 즉, 어떠한 $c\in S$에 대하여

$$a_1+b_2+c=a_2+b_1+c$$

가 성립한다. 그런데 이는 정확히 $(a_2,b_2)\equiv (a_1,b_1)$의 조건이므로, $R$은 symmetric하다. 마지막으로, $(a_1,b_1)\equiv(a_2,b_2)$이고 $(a_2,b_2)\equiv (a_3,b_3)$이라 하자. 그럼 어떤 $c$, $c'$에 대하여

$$a_1+b_2+c=a_2+b_1+c,\qquad a_2+b_3+c'=a_3+b_2+c'$$

가 성립한다. 이제 두 식을 더하면, 

$$a_1+b_3+(a_2+b_2+c+c')=a_3+b_1+(a_2+b_2+c+c')$$

이므로 $(a_1,b_1)\equiv(a_3,b_3)$이 성립한다. 즉, $R$은 동치관계가 된다.

이제 $R$이 $S\times S$의 연산과 compatible하다는 것을 보여야 한다. 이를 위해, $(a_1, b_1)\equiv(a_1',b_1')$이고 $(a_2, b_2)\equiv (a_2',b_2')$라 하자. 우리는 $(a_1+a_2, b_1+b_2)\equiv(a_1'+a_2', b_1'+b_2')$임을 보여야 한다. 주어진 조건으로부터, 적당한 $c_1$, $c_2$가 존재하여

$$a_1+b_1'+c_1=a_1'+b_1+c_1,\qquad a_2+b_2'+c_2=a_2'+b_2+c_2$$

가 성립한다. 이제, 두 식을 더하면
$$(a_1+a_2)+(b_1'+b_2')+(c_1+c_2)=(a_1'+a_2')+(b_1+b_2)+(c_1+c_2)$$

이 성립하므로, 정의에 의해 $(a_1+a_2, b_1+b_2)\equiv(a_1'+a_2', b_1'+b_2')\pmod{R}$이 성립하고, 따라서 $R$은 $S\times S$의 연산과 compatible하다. 

</details>

그러므로 $(S\times S)/R$은 가환인 준군이 된다. 이를 $G_S$라 하자. 

<div class="proposition" markdown="1">

<ins id="lem4">**보조정리 4**</ins> $G_S$는 가환군이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$G_S$가 항등원과 역원을 가짐을 보이면 된다. 우리는 $(a,b)$를 $a-b$처럼 생각하고 있으므로, 항등원은 $(a,a)$, $(a,b)$의 역원은 $-(a-b)=b-a$, 즉 $(b,a)$가 될 것이다. 이를 증명하자.

우선, 임의의 $c\in S$에 대하여, $[(c,c)]$가 항등원이 됨을 보인다. 임의의 $[(a,b)]\in G_S$에 대하여,

$$[(a,b)]+[(c,c)]=[(a+c, b+c)]$$

가 성립한다. 그런데

$$(a+c)+b+d=(b+c)+a+d$$

가 임의의 $d\in S$에 대해 성립하므로, $(a+c, b+c)\equiv (a,b)$이고 따라서 $[(a+c, b+c)]=[(a,b)]$가 성립한다. 교환법칙에 의하여 $[(c,c)]+[(a,b)]=[(a,b)]$도 당연하게 성립하므로, $[(c,c)]$는 $G_S$의 항등원이 된다. 

한편, 임의의 $[(a,b)]\in G_S$에 대하여

$$[(a,b)]+[(b+a)]=[(a+b,a+b)]$$

이므로, 앞선 논증에 의해 $[(a,b)]+[(b,a)]$는 $G_S$의 항등원이 되고, $[(a,b)]+[(b,a)]$도 마찬가지다. 따라서 $G_S$의 임의의 원소의 역원이 존재하므로, $G_S$는 군의 구조를 가진다. 
</details>

그럼 $G_S$는 우리가 찾던 가환군이 된다. 즉, $G_S$는 위의 universal mapping problem을 만족한다.

<div class="proposition" markdown="1">

<ins id="pp5">**명제 5**</ins> 준군 $(S, +)$에 대하여, 위와 같이 만들어진 가환군 $G_S$와, 자연스러운 준동형사상 $\epsilon:S\rightarrow G_S$는 universal property를 만족한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $S$에서 $G_S$로의 *자연스러운 준동형사상*이 무엇인지부터 생각해보자. 우리는 $G_S$에서 $(a,b)$를 $a-b$로 취급하고 있으므로, $a$가 $G_S$에서는 $(a+b)-b$, 즉 $[(a+b, b)]$인 것을 알 수 있다. 따라서 $\epsilon$을 $a\mapsto[(a+a, a)]$으로 정의하자. (물론 아무 $b$나 택해서 $a\mapsto[(a+b,b)]$으로 정의해도 같은 값이 나온다.) 

Universal property를 증명하기 위해, 임의의 가환군 $G$와, 준군 준동형사상 $f:S\rightarrow G$가 주어졌다고 하자. 

우선, 만약 주어진 성질을 만족하는 $\bar{f}:G_S\rightarrow S$가 존재한다면, $\bar{f}$는 반드시 유일해야 한다. 임의의 $[(a,b)]$에 대하여, 

$$\begin{align*}\bar{f}\left([(a,b)]\right)&=\bar{f}\left([(a+(a+b), b+(a+b))]\right)=\bar{f}\left([(a+a,a)]+[(b, b+b)]\right)\\ &\bar{f}\left([(a+a, a)]\right)+\bar{f}\left([(b,b+b)]\right)=\bar{f}\left(\epsilon(a)\right)-\bar{f}\left(\epsilon(b)\right)\\ &=f(a)-f(b)\end{align*}$$

이므로, 각각의 원소들에서의 함수값이 유일하게 정해지기 때문이다. 

이제 유일성 증명에서 힌트를 얻어, $\bar{f}([(a,b)])$를 $f(a)-f(a)$으로 정의하자. 우선, 이 정의는 잘 정의되어있다. 즉, 만일 $(a_1,b_1)\equiv(a_2,b_2)$라면, $f(a_2)-f(b_2)=f(a_1)-f(b_1)$이 성립한다. $(a_1,b_1)\equiv(a_2,b_2)$이므로, 어떤 $c\in S$가 존재하여 $a_1+b_2+c=a_2+b_1+c$이고, 따라서

$$f(a_1)+f(b_2)+f(c)=f(a_1+b_2+c)=f(a_2+b_1+c)=f(a_2)+f(b_1)+f(c)$$

이므로, 양 변에서 $f(c)$를 빼고 적당히 이항해서 정리해주면

$$f(a_1)-f(b_1)=f(a_2)-f(b_2)$$

을 얻는다. 

또, $\bar{f}$는 군 준동형사상이 된다. 임의의 $[(a_1, b_1)]$, $[(a_2,b_2)]$에 대하여

$$\begin{align*}\bar{f}\left([(a_1,b_1)]+[(a_2, b_2)]\right)&=\bar{f}\left([(a_1+a_2, b_1+b_2)]\right)=f(a_1+a_2)-f(b_1+b_2)\\&=f(a_1)+f(a_2)-f(b_1)-f(b_2)=(f(a_1)-f(b_1))+(f(a_2)-f(b_2))\\&=\bar{f}\left([(a_1, b_1)]\right)+\bar{f}\left([(a_2,b_2)]\right)\end{align*}$$

가 성립하기 때문이다. 

마지막으로, $\bar{f}$가 주어진 조건 $f=\bar{f}\circ\epsilon$을 만족한다는 것은 계산해보면 자명하다.

</details>

이렇게, 우리는 원했던 가환군 $G_S$를 얻었다.

지금까지의 construction을 찬찬히 뜯어보면, $S$의 교환법칙이 쓰이지 않는 곳이 없다. 바꿔 말하자면, 비가환인 준군으로부터 일반적인 군을 만들어내는 것은 불가능에 가깝다. 이는 비단 여기서만의 문제는 아니고, 일반적으로 나중에 살펴볼 환에서도 비슷한 문제가 있다. 교환법칙을 없애기 위해서는 최소한 이 과정들이 비슷하게나마 정의될 수 있도록 특정한 조건들을 넣어줘야만 한다. 

---
**Reference**

**[Bou]** Bourbaki, N. Algebra. I. Chapters 1-3. Translated from the French. Reprint of the 1989 English translation. *Elements of Mathematics. Springer-Verlag, Berlin,* 1998. 

---
[^1]: 만일 연산이 multiplicative하게 적혀있었다면, 첫 번째 부분은 분자, 둘째 부분은 분모의 역할을 한다고 생각할 수 있다.
[^2]: 만일 연산이 multiplicative하게 적혀있었다면, 이 $c$는 두 분수를 통분하는 것에 해당한다.
