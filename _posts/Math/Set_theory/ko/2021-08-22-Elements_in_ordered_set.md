---

title: "순서집합의 원소들"
excerpt: "순서집합의 최대, 최소, 극대, 극소 원소들"

lang: ko

categories: [Math / Set Theory]
permalink: /ko/math/set_theory/order_relations_2
header:
    overlay_image: /assets/images/Set_theory/Order_relations.png
    overlay_filter: 0.5
sidebar: 
    nav: "set-ko"

date: 2021-08-22
last_modified_at: 2022-04-04
weight: 11

---

## 순서집합의 원소들

이제부터 우리는 ordered set에서 특별한 성질을 갖는 원소들을 살펴볼 것이다. 이 개념들은 글로만 보면 조금 헷갈리는 부분이 있으니 diagram을 통해 살펴보도록 하자. 다음의 diagram

![diagram_representing_single_ordering](/assets/images/Set_theory/Order_relations_2-1.png){:width="15px" class="invert" .align-center}

이 $b\leq a$를 뜻하는 것이라 하자. 그럼 예를 들어 다음의 diagram

![diagram_representing_two_orderings](/assets/images/Set_theory/Order_relations_2-2.png){:width="120px" class="invert" .align-center}

은 $b\leq a$이고 $c\leq a$이지만, $b$와 $c$ 사이에는 별 관계가 없는 상황을 나타낸다. 이러한 diagram을 *Hasse diagram*이라 부른다.

<ins id="df1">**정의 1**</ins> $E$가 ordered set이라 하자. 원소 $a\in E$가 $E$의 *maximal element<sub>극대원소</sub>* (resp. *minimal element<sub>극소원소</sub>*)라는 것은 $x\leq a$ (resp. $x\geq a$)이면 $x=a$가 성립하는 것이다.
{: .definition}

이 상황에서, minimal element가 유일할 필요는 없다. 예컨대 아까와 같은 상황
    
![diagram_representing_two_orderings](/assets/images/Set_theory/Order_relations_2-2.png){:width="120px" class="invert" .align-center}

에서, $a\not\leq b$이고 $c\not\leq b$이므로, $x\leq b$를 만족하는 유일한 원소는 $x=b$ 뿐이다. 마찬가지로 $x\leq c$를 만족하는 유일한 원소는 $x=c$ 뿐이다. 즉, $x\leq b\implies x=b$이고 $x\leq c\implies x=c$이므로, $b$, $c$는 이 집합 $\left\\{a,b,c\right\\}$의 minimal element들이다. 물론 maximal element의 경우도 마찬가지. 수학자들은 보통 이런 성질을 가지는 원소가 유일하기를 바라므로, 이 상황은 그렇게 달가운 상황이 아니다. 다음의 정의를 살펴보자.

<ins id="df2">**정의 2**</ins> $E$가 ordered set이라 하자. 원소 $a\in E$가 $E$의 *least element<sub>최소원소</sub>* (resp. *greatest element<sub>최대원소</sub>*)라는 것은 모든 $x\in E$에 대해서 $a\leq x$ (resp. $x\leq a$)인 것이다.
{: .definition}

앞선 예시에서, $b$와 $c$는 least element가 될 수 없다. $b\leq c$, 혹은 $c\leq b$가 성립하지 않기 때문이다. 조금만 생각을 해 보면 least element는 유일함을 알 수 있다. 더욱이 다음이 성립한다.

<ins id="pp3">**명제 3**</ins> 만일 $E$가 least (resp. greatest) element $a$를 갖는다면, $a$는 $E$의 유일한 minimal (resp. maximal) element이다.
{: .proposition}

<details class="proof" markdown="1">
<summary>증명</summary>

임의의 $a\neq x$에 대하여, $a\leq x$가 성립하므로 $a&lt;x$이다. Asymmetry에 의해 $x\not&lt;a$이므로, 만일 $x\leq a$라면 $x=a$일 수밖에 없다.
</details>


다음은 굉장히 자명한 명제.

<ins id="pp4">**명제 4**</ins> $E$가 ordered set이고 $E'=E\sqcup\\{a\\}$이라 하자. 그럼 $E$에서 정의된 order relation을 확장하며, $a$를 greatest element로 갖는 $E'$의 order relation이 존재한다.
{: .proposition}

<details class="proof" markdown="1">
<summary>증명</summary>

기존의 order relation의 그래프 $G$에 대하여, $G\cup\bigcup\_{x\in E}\left\\{(x, a)\right\\}$를 새로운 relation의 그래프로 잡으면 된다. 이 그래프가 order relation의 조건을 만족함도 물론 보여야 하지만, 그건 너무 쉽다.
</details>

한편, $E$가 preordered set이라 하자. $A\subset E$가 $E$에서 *cofinal* (resp. *coinitial*)이라는 것은 임의의 $x\in E$에 대하여 $y\in A$가 존재하여 $x\leq y$ (resp. $y\leq x$)인 것이다. 예를 들어, 다음의 diagram

![cofinal_sequence](/assets/images/Set_theory/Order_relations_2-3.png){:width="320px" class="invert" .align-center}

을 생각하자. 그럼 집합 $\left\\{a\_{2n}\right\\}\_{n\in\mathbb{N}}$, $\left\\{a\_{1000+n}\right\\}\_{n\in\mathbb{N}}$ 등은 모두 cofinal이다.

따라서 정의에 의해 $E$가 greatest (resp. least) element를 갖는다는 것은 $E$가 cofinal (resp. coinitial)한 singleton을 부분집합으로 갖는다는 것과 동치이다.

<ins id="df5">**정의 5**</ins> $E$가 preordered set이고 $X$가 $E$의 부분집합이라 하자. 어떤 원소 $x\in E$가 모든 $y\in X$에 대해 $x\leq y$ (resp. $x\geq y$)를 만족한다면, 이를 $E$에서의 $X$의 *lower bound<sub>하계</sub>* (resp. *upper bound<sub>상계</sub>*)라 부른다.
{: .definition}

약간의 abuse of language를 통해, lower bound의 각 원소들도 모두 lower bound라 부른다.

예를 들어, 다음의 diagram

![upper_and_lower_bounds](/assets/images/Set_theory/Order_relations_2-4.png){:width="160px" class="invert" .align-center}

에서, $a$는 집합 $\left\\{c,d,e\right\\}$의 upper bound지만 $b$는 그렇지 않다. $c\not\leq b$이기 때문이다. 만일 집합 $\left\\{d,e\right\\}$를 생각한다면, $a$와 $b$ 모두 이 집합의 upper bound가 될 것이다.
Transitivity에 의하여, 만일 $x$가 $X$의 lower bound라면 모든 $z\leq x$ 또한 $X$의 lower bound가 된다. Lower bound는 $X$의 원소일 필요가 없으며, 사실 $X$에 포함된 $X$의 lower bound가 있을 조건은 $X$가 least element를 갖는 것과 동치이다. 예컨대 least element가 없는 ordered set $E$는 lower bound를 갖지 않는다. 

만약 $X\subset E$가 (공집합이 아닌) lower bound를 갖는다면, 이를 *bounded below<sub>아래로 유계</sub>*라 부르고, 비슷하게 *bounded above<sub>위로 유계</sub>*를 정의한다. 만약 $X$가 bounded below이면서 동시에 bounded above라면, 간단히 *bounded<sub>유계</sub>*라 한다. 또, preordered set $E$로의 함수가 bounded below (resp. bounded above, bounded)라는 것은 그 image가 그렇다는 것이다.

<ins id="df6">**정의 6**</ins> $E$가 ordered set이고 $X\subset E$이라 하자. $E$의 어떤 원소가 $E$에서의 $X$의 *greatest lower bound<sub>최대하계</sub>* (혹은 *infimum<sub>하한</sub>*)라는 것은 이 원소가 $X$의 lower bound 중 greatest element라는 것이다. 이와 유사하게 *least upper bound<sub>최소상계</sub>* (혹은 *supremum<sub>상한</sub>*)도 정의한다.
{: .definition}

만약 $X\subset E$의 supremum이 존재한다면, 이를 $\sup_EX$로 쓰고, infimum은 $\inf_EX$로 쓴다. 만약 $X$가 greatest element $a$를 갖는다면 $a=\sup_EX$가 될 것이다. $a$ 자기 자신이 $X$의 upper bound이며, 만일 $a'$가 또 다른 upper bound였다면, $a$는 $X$의 원소이므로 $a\leq a'$가 되어 upper bound들 가운데에선 $a$가 least가 될 것이기 때문이다.

Preordered set으로의 함수가 bounded above (below)인 것을 정의한 것과 같이, 함수의 image가 supremum을 갖는다면 $f$가 supremum을 갖는다고 표현하고, infimum도 마찬가지로 표현한다.

<ins id="pp7">**명제 7**</ins> $E$가 ordered set이고 $A$가 supremum과 infimum을 모두 갖는 $E$의 부분집합이라 하자. 만일 $A\neq\emptyset$일 경우 $\inf A\leq\sup A$이며, $A=\emptyset$이고 $A$가 supremum을 모두 갖는다면, $E$의 least, greatest element가 존재하고 $\sup A$와 $\inf A$는 각각 $E$의 least, greatest element가 된다.
{: .proposition}

<details class="proof" markdown="1">
<summary>증명</summary>
만일 $A\neq\emptyset$라면 적어도 하나의 원소가 존재한다. 이를 $x$라 하자. 그럼 정의에 의해 $\inf A\leq x$이고 $x\leq\sup A$이며 transitivity에 의해 $\inf A\leq\sup A$이다. 만일 $A=\emptyset$라면, $E$의 임의의 원소 $x$가 $A$의 lower bound이자 upper bound가 되므로 $\sup A$와 $\inf A$는 각각 $E$의 least, greatest element가 된다.
</details>

다음은 집합 간의 포함관계에 대한 명제다.

<ins id="pp8">**명제 8**</ins> $E$가 ordered set이고 $A$, $B$가 $E$의 부분집합이라 하자. 만일 $A$와 $B$가 모두 $E$에서 supremum을 갖고 $A\subset B$라면, $\sup A\leq\sup B$이다.
{: .proposition}

<details class="proof" markdown="1">
<summary>증명</summary>
$x\in A$라 하자. $A\subset B$이므로, $x\in B$이다. 임의의 $x\in B$에 대하여 $x\leq \sup B$이므로 (동시에 모든 $x\in A$에 대해서도 성립한다), $\sup B$는 $A$의 upper bound이다. 이제 정의에 의해 $\sup A\leq \sup B$이다. 
</details>

물론 위의 정리에서 supremum을 infimum으로 바꿀 수도 있으며, 이 경우 $\inf B\leq\inf A$이다.

<ins id="pp9">**명제 9**</ins> $(x_i)\_{i\in I}$, $(y_i)\_{i\in I}$가 ordered set $E$의 원소들의 family라 하고 $x_i\leq y_i$가 모든 $i\in I$에 대해 성립한다고 하자. 만일 두 family가 모두 $E$에서 supremum을 갖는다면, $\sup_{i\in I} x_i\leq \sup_{i\in I} y_i$이다.
{: .proposition}

<details class="proof" markdown="1">
<summary>증명</summary>

임의의 $i\in I$에 대하여, $x_i\leq y_i$이고 $y_i\leq \sup y_i$이므로 모든 $i$에 대해 $x_i\leq \sup y_i$이고 따라서 $\sup x_i$의 minimality에 의해 $\sup x_i\leq\sup y_i$이다.
</details>

다음은 언제나 그랬듯 일종의 결합법칙을 증명한 것이다.

<ins id="pp10">**명제 10**</ins>  $(x_i)\_{i\in I}$가 ordered set $E$의 원소들로 이루어진 family이고, $(J_k)\_{k\in K}$가 $I$의 covering이라 하자. 만일 각각의 subfamily들 $(x_i)\_{i\in J_k}$가 $E$에서 supremum을 갖는다면,  $\sup\_{i\in I} x_i$가 존재하는 것은 $\sup\_{k\in K}(\sup\_{j\in J_k}x_j)$가 존재하는 것과 동치이며 두 값은 같다.
{: .proposition}

<details class="proof" markdown="1">
<summary>증명</summary>
$b_k=\sup\_{i\in J_k} x_i$라 적자. 우선 $(x_i)\_{i\in I}$가 supremum을 갖는다고 하고, 이를 $a$라 하자. 그럼 $a\leq b_k$가 모든 $k$에 대해 성립한다. 또, 만약 $c\geq b_k$가 모든 $k$에 대해 성립한다면, 임의의 $x_i$에 대해서 $i\in J\_{k'}$인 $k'$는 $b\_{k'}\geq x_i$를 만족하고, 따라서 어떠한 $i$에 대해서도 $c\geq x_i$이다. 이제 $a$의 최소성에 의해 $c\geq a$이어야 하고, 따라서 $a$가 supremum이며 $\sup\_{i\in I}x_i=\sup\_{k\in K}(\sup\_{i\in J_k} x_j)$이다.  
반대로 $(b_k)\_{k\in K}$가 supremum $a'$를 갖는다 해도 위와 같은 방법으로 증명을 완료할 수 있다.
</details>

다음은 product.

<ins id="pp11">**명제 11**</ins>  $(E_i)\_{i\in I}$가 ordered set들의 family라 하자. $A$가 product set $E=\prod E_i$의 부분집합이고, 각각의 $i$에 대해 $A_i=\operatorname{pr}\_i A$라 하자. 그럼 $\sup_EA$가 존재하는 것과 각각의 $\sup\_{E_i}A_i$가 존재하는 것은 동치이며, $\sup_EA=(\sup\_{E_i}A_i)$이다.
{: .proposition}
<details class="proof" markdown="1">
<summary>증명</summary>
우선 $\sup\_{E_i} A_i$가 각각의 $i$에 대해 존재한다고 하자. 그럼 $(\sup\_{E_i} A_i)\_{i\in I}$가 $A$의 upper bound임은 자명하다. 만일 $(c_i)$가 $A$의 다른 upper bound였다면, 각각의 $c_i$는 $A_i$의 upper bound가 될 것이므로 $\sup\_{E_i}A_i$의 최소성에 의해 $c_i\geq\sup A_i$이고, 따라서 $(c_i)\geq(\sup A_i)\_{i\in I}$이다.  
반대로 $\sup A=(a_i)$가 존재한다고 하자. 모든 $i$에 대해서, $a_i$는 $A_i$의 upper bound이다. 만일 $x_i\in A_i$라면, $i$번째 성분으로 $x_i$를 갖는 $x\in A$가 $x\leq (a_i)$이도록 하는 $x$가 존재하기 때문이다. 이제 임의의 다른 upper bound $a_i'$에 대해, 새로운 원소 $(c_i)$를 $(a_i)$의 $i$번째 성분을 $a_i'$로 바꾸어 정의하면 $c\geq a$이므로 $a_i'\geq a_i$가 된다. 
</details>

<div class="remark" markdown="1">
<ins id="rmk4">**참고**</ins>  Ordered set $E$와 $A\subset F\subset E$에 대해서, $\sup_E A$와 $\sup_F A$ 중 하나만 존재할 수도 있고, 둘 다 존재하지만 값이 다를 수도 있다. 예컨대 $A=\\{x:x&lt;\sqrt{2}\\}$를 각각의 집합들에서 비교해보자. 

1. $\mathbb{Q}$의 부분집합으로써, 이 집합의 supremum은 존재하지 않으나 $\mathbb{R}$에서는 존재한다. 즉, $A\subset F\subset E$에서 $\sup_EA$는 존재하지만 $\sup_FA$는 존재하지 않는다.
2. 한편 집합 $F'=\left\\{x:x&lt;\sqrt{2}\right\\}\cup \left\\{2\right\\}$를 생각하자. $A\subset F'\subset F$에서 $\sup\_{F'}A=2$이지만 $\sup_FA$는 여전히 존재하지 않는다.
3. 마지막으로 $A\subset F'\subset E$에서, $\sup\_{F'}A$와 $\sup\_{E}A$는 각각 존재하지만 두 값은 다르다.   

</div>

그러나 여전히 다음을 증명할 수 있다.

<ins id="pp12">**명제 12**</ins>  $E$가 ordered set이고, $A\subset F\subset E$이라 하자. 만일 $\sup_EA$와 $\sup_FA$이 모두 존재한다면 $\sup_EA\leq\sup_FA$이다. 만일 $\sup_EA$이 존재하고 $F$에 속한다면 $\sup_FA$도 존재하고 이 값은 $\sup_EA$와 같다.
{: .proposition}
<details class="proof" markdown="1">
<summary>증명</summary>
$A$의 $F$에서의 upper bound들의 집합은 $E$에서의 upper bound들의 집합에 포함되고, 따라서 supremum은 더 크다. 만일 $\sup_EA$가 존재하고 $F$에 속한다면, 이는 자명하게 $F$에서의 $A$의 supremum이 된다.
</details>

## Directed set

<ins id="df13">**정의 13**</ins>  Preordered set $E$가 *right directed*이라는 것은 $E$의 원소 두 개짜리 임의의 부분집합이 bounded above인 것이다. 이와 비슷하게 preordered set $E$가 *left directed*라는 것은 $E$의 원소 두 개짜리 부분집합이 bounded below인 것이다.
{: .definition}

예컨대 임의의 집합 $E$에 대하여, 멱집합 $\mathcal{P}(E)$에 포함관계로 order를 주면 이는 right directed이다. 임의의 $X, Y\in\mathcal{P}(E)$에 대하여, $X\cup Y$는 $\mathcal{P}(E)$의 원소이고 $X$와 $Y$의 upper bound이기 때문이다. 이를 diagram으로 나타내면 다음과 같다.

![directed_system](/assets/images/Set_theory/Order_relations_2-5.png){:width="320px" class="invert" .align-center}

<ins id="pp14">**명제 14**</ins>  Right directed ordered set $E$에서, $E$의 maximal element $a$는 greatest element이다.
{: .proposition}

<details class="proof" markdown="1">
<summary>증명</summary>

$E$가 right directed이므로, 임의의 $x\in E$에 대하여, 어떤 $y\in E$가 존재하여 $\{x,a\}$의 upper bound이다. 그러나 $a$는 maximal이고, 따라서 $a=y$여야 하므로, 임의의 $x$에 대해 $x\leq a$가 성립한다.
</details>

Right directed인 집합들의 product은 right directed이다. 만약 product set에서 두 원소를 뽑아온다면, 우리는 각각의 성분들에 해당하는 원소 두 개씩을 뽑아온 후 원래 집합들이 right-directed임을 이용할 수 있기 때문이다. 반면 right directed set의 부분집합이 right directed가 되어야 하는 것은 일반적으로 참이 아니지만, cofinal subset은 언제나 right directed가 된다.

<ins id="df15">**정의 15**</ins> Ordered set $E$가 *lattice*라는 것은 $E$의 임의의 원소 두 개짜리 부분집합이 supremum과 infimum을 갖는 것이다.
{: .definition}

이러한 상황에서 우리는 $\sup\\{x,y\\}$와 $\inf\\{x,y\\}$ 대신 간단하게 $x\vee y$와 $x\wedge y$로 쓰고, *join*과 *meet*이라 부르기도 한다. 그럼 lattice $E$의 임의의 부분집합 $A$가 left directed일 필요충분조건은 임의의 $x,y\in A$에 대해 $x\wedge y\in A$인 것이고, 또 $A$가 right directed일 필요충분조건은 임의의 $x,y\in A$에 대해 $x\vee y\in A$인 것임을 확인할 수 있다.

수학적 귀납법을 알고 있다고 가정하면, lattice $E$의 임의의 유한한 부분집합은 supremum과 infimum을 갖는다는 것을 알 수 있지만 무한한 부분집합에 대해서는 어떠한 이야기도 할 수 없다. 만일 lattice $E$의 (무한집합을 포함한) 임의의 부분집합이 supremum과 infumum을 갖는다면, 이를 *complete lattice*라 부른다.

<ins id="df16">**정의 16**</ins> Preordered set $E$에서의 두 원소 $x$, $y$가 *comparable<sub>비교가능</sub>*하다는 것은 명제 <box>$x\leq y$ 혹은 $y\leq x$</box>이 항상 참인 것이다. 만약 집합 $E$의 임의의 원소가 comparable하다면, 이를 *totally ordered set<sub>전순서집합</sub>*이라 부른다.
{: .definition}

만약 $E$가 totally ordered set이라면, trichotomy가 성립한다. 즉,임의의 $x, y\in E$에 대하여,  $x=y$, $x&lt;y$, $x&gt;y$ 중 하나가 성립한다. 이 경우엔 $x\leq y$의 부정이 $x>y$가 된다. 하지만 totally ordered set이라는 조건이 빠진 상태에서 이는 일반적으로 성립하지 않는다. (§순서관계 (1), 명제 10 직후의 [참고](/ko/math/set_theory/order_relations_1#rmk1))

<ins id="pp17">**명제 17**</ins> Totally ordered set $E$에서 ordered set $F$로의 모든 순단조함수 $f$는 injective다. 만약 $f$가 순증가라면, $f$는 $E$에서 $f(E)$로의 isomorphism이다.
{: .proposition}
<details class="proof" markdown="1">
<summary>증명</summary>

$f$가 순단조함수라 하자. 그럼 임의의 $x\neq y$에 대하여, $x>y$ 혹은 $x&lt;y$가 성립하므로, $f(x)>f(y)$ 혹은 $f(x)&lt;f(y)$이고, 따라서 $f(x)\neq f(y)$가 되어 $f$는 injective이다. 특히 $f$가 순증가라면, 우리는 $f(x)\leq f(y)\implies x\leq y$라는 것을 보여야 하는데, 이는 대우명제가 자명하다.
</details>

위의 명제 또한 일반적인 ordered set에서는 성립하지 않았었다. (§순서관계 (1), 정의 13 직후의 [참고](/ko/math/set_theory/order_relations_1#rmk3))

<ins id="pp18">**명제 18**</ins> $E$가 totally ordered set이고 $X$가 그 부분집합이라 하자. 그럼 $b\in E$가 $X$의 supremum인 것은 $b$가 $X$의 upper bound이고, $c&lt;b$를 만족하는 임의의 $c\in E$에 대하여 $x\in X$이 존재하여 $c&lt;x\leq b$인 것과 동치이다.
{: .proposition}

<details class="proof" markdown="1">
<summary>증명</summary>

자명.

</details>

$E$가 ordered set이고, $a\leq b$라 하자. 그럼 $a\leq x\leq b$를 만족하는 모든 $x$를 모아둔 $X\subset E$를 *closed interval*이라 부르고 $[a,b]$로 적는다.  $a\leq x&lt;b$인 $x$들을 모아둔 부분집합은 *half-open interval*이라 부르고 $[a,b)$로 적으며, $(a,b]$도 마찬가지다. $(a,b)$는 *open interval*이라 부르고, 이는 $a&lt;x&lt;b$를 만족하는 모든 $x$를 모아둔 집합이다.  
추가로, $x\leq a$를 만족하는 모든 $x$를 모아둔 부분집합을 *unbounded closed interval*이라 부르고 $(-\infty, a]$로 적는다.[^1] $[a,\infty)$, $(-\infty, a)$, $(a, \infty)$도 유사하게 정의한다. 

다음은 모든 경우의 수를 나누어 증명해야 하는 매우 귀찮은 명제. 증명은 어렵지 않으므로 생략한다. 

<ins id="pp19">**명제 19**</ins> Lattice에서 두 interval의 교집합도 interval이다.
{: .proposition}



---
**참고문헌**

**[Bou]** N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---

[^1]: 물론 여기에서 $\pm\infty$는 그저 기호일 뿐이다.
