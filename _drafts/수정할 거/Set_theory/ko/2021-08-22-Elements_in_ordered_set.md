---

title: "순서집합의 원소들"
excerpt: "순서집합의 최대, 최소, 극대, 극소 원소들"

categories: [Math / Set Theory]
permalink: /ko/math/set_theory/elements_in_ordered_set
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

다음의 diagram

![diagram_representing_single_ordering](/assets/images/Set_theory/Elements_in_ordered_set-1.png){:width="29.4px" class="invert" .align-center}

이 $b\leq a$를 뜻하는 것이라 하자. 예를 들어, 다음의 diagram

![diagram_representing_two_orderings](/assets/images/Set_theory/Elements_in_ordered_set-2.png){:width="135.45px" class="invert" .align-center}

은 $b\leq a$이고 $c\leq a$이지만, $b$와 $c$ 사이에는 별 관계가 없는 상황을 나타낸다. 이러한 diagram을 *Hasse diagram*이라 부른다.

<ins id="df1">**정의 1**</ins> Ordered set $A$의 원소 $a$가 $A$의 *maximal element<sub>극대원소</sub>* (resp. *minimal element<sub>극소원소</sub>*)라는 것은 모든 $x\in A$에 대하여 $x\leq a$ (resp. $x\geq a$)이면 $x=a$가 성립하는 것이다.
{: .definition}

Minimal element가 유일할 필요는 없다. 예컨대 아까와 같은 상황
    
![diagram_representing_two_orderings](/assets/images/Set_theory/Elements_in_ordered_set-2.png){:width="135.45px" class="invert" .align-center}

에서, $a\not\leq b$이고 $c\not\leq b$이므로, $x\leq b$를 만족하는 유일한 원소는 $x=b$ 뿐이다. 마찬가지로 $x\leq c$를 만족하는 유일한 원소는 $x=c$ 뿐이다. 따라서 두 명제 <phrase>$x\leq b\implies x=b$</phrase>와 <phrase>$x\leq c\implies x=c$</phrase>가 모두 성립하므로 $b$, $c$는 집합 $\left\\{a,b,c\right\\}$의 minimal element들이다. 

수학자들은 보통 이런 성질을 가지는 원소가 유일하기를 바라므로, 이 상황은 그렇게 달가운 상황이 아니다. 

<ins id="df2">**정의 2**</ins> Ordered set $A$의 원소 $a$가 $A$의 *least element<sub>최소원소</sub>* (resp. *greatest element<sub>최대원소</sub>*)라는 것은 모든 $x\in A$에 대해서 $a\leq x$ (resp. $x\leq a$)인 것이다.
{: .definition}

앞선 예시에서, $b$와 $c$는 least element가 될 수 없다. $b\leq c$와 $c\leq b$가 성립하지 않기 때문이다. 정의에 의해 least element는 유일하다. 더욱이 다음이 성립한다.

<ins id="pp3">**명제 3**</ins> 만일 $A$가 least (resp. greatest) element $a$를 갖는다면, $a$는 $A$의 유일한 minimal (resp. maximal) element이다.
{: .proposition}

<details class="proof" markdown="1">
<summary>증명</summary>

임의의 $a\neq x$에 대하여, $a\leq x$가 성립하므로 $a&lt;x$이다. Asymmetry에 의해 $x\not&lt;a$이므로, 만일 $x\leq a$라면 $x=a$일 수밖에 없다.

</details>

때때로 ordered set의 모든 원소보다 큰 새로운 원소, 혹은 모든 원소보다 작은 새로운 원소를 생각해야 할 필요가 있다. 이러한 가상의 원소는 $\pm\infty$으로 쓰는 것이 보편적이다.

<ins id="pp4">**명제 4**</ins> $A$가 ordered set이고 $A'=A\sqcup\\{+\infty\\}$이라 하자. 그럼 $A$에서 정의된 order relation을 확장하며, $a$를 greatest element로 갖는 $A'$의 order relation이 존재한다.
{: .proposition}

<details class="proof" markdown="1">
<summary>증명</summary>

기존의 order relation의 그래프 $G$에 대하여, $G\cup\bigcup\_{x\in A}\left\\{(x, +\infty)\right\\}$를 새로운 관계의 그래프로 잡으면 된다.

</details>

한편, $A$가 preordered set이라 하자. $X\subseteq A$가 $A$에서 *cofinal* (resp. *coinitial*)이라는 것은 임의의 $x\in A$에 대하여 $y\in X$가 존재하여 $x\leq y$ (resp. $y\leq x$)인 것이다. 예를 들어, 다음의 diagram

![cofinal_sequence](/assets/images/Set_theory/Elements_in_ordered_set-3.png){:width="420.6px" class="invert" .align-center}

을 생각하자. 집합 $\left\\{a\_{2n}\right\\}\_{n\in\mathbb{N}}$, $\left\\{a\_{1000+n}\right\\}\_{n\in\mathbb{N}}$ 등은 모두 cofinal이다.

<ins id="df5">**정의 5**</ins> $A$가 preordered set이고 $X$가 $A$의 부분집합이라 하자. 어떤 원소 $a\in A$가 모든 $x\in X$에 대해 $a\leq x$ (resp. $a\geq x$)를 만족한다면, 이를 $A$에서의 $X$의 *lower bound<sub>하계</sub>* (resp. *upper bound<sub>상계</sub>*)라 부른다.
{: .definition}

약간의 abuse of language를 통해, lower bound의 각 원소들도 모두 lower bound라 부른다.

예를 들어, 다음과 같이 order relation이 주어진 집합 $A=\\{a,b,c,d,e\\}$를 생각하자.

![upper_and_lower_bounds](/assets/images/Set_theory/Elements_in_ordered_set-4.png){:width="158.4px" class="invert" .align-center}

그럼 $a$는 집합 $X=\left\\{c,d,e\right\\}$의 upper bound지만 $b$는 그렇지 않다. $c\not\leq b$이기 때문이다. 만일 집합 $X'=\left\\{d,e\right\\}$를 생각한다면, $a$와 $b$ 모두 이 집합의 upper bound가 될 것이다.

Transitivity에 의하여, 만일 $x$가 $X$의 lower bound라면 모든 $z\leq x$ 또한 $X$의 lower bound가 된다. Lower bound는 $X$의 원소일 필요가 없으며, $X$의 lower bound 중 어느 하나가 $X$에 속할 조건은 $X$가 least element를 갖는 것과 동치이다.

만약 $X\subseteq A$가 공집합이 아닌 lower bound를 갖는다면, $X$가 *bounded below<sub>아래로 유계</sub>*라 하고, 비슷하게 *bounded above<sub>위로 유계</sub>*를 정의한다. 만약 $X$가 bounded below이면서 동시에 bounded above라면, 간단히 *bounded<sub>유계</sub>*라 한다. 또, preordered set $A$로의 함수가 bounded below (resp. bounded above, bounded)라는 것은 그 image가 그렇다는 것이다.

<ins id="df6">**정의 6**</ins> $A$가 ordered set이고 $X\subseteq A$이라 하자. $A$의 어떤 원소 $a$가 $X$의 *greatest lower bound<sub>최대하계</sub>* (혹은 *infimum<sub>하한</sub>*)라는 것은 이 원소가 $X$의 lower bound 중 greatest element라는 것이다. 이와 유사하게 *least upper bound<sub>최소상계</sub>* (혹은 *supremum<sub>상한</sub>*)도 정의한다.
{: .definition}

$X\subseteq A$의 supremum이 존재한다면, 이를 $\sup_AX$로 쓰고, infimum은 $\inf_AX$로 쓴다. 

$X\subseteq A$가 greatest element $a$를 갖는다고 가정하자. 그럼 $a=\sup_AX$이다. 우선 $a$ 자기 자신이 $X$의 upper bound임은 자명하다. 또, 만일 $a'$가 또 다른 upper bound였다면 모든 $x\in X$에 대하여 $x\leq a'$이고, 특히 $a\leq a'$이기 때문이다.

Preordered set으로의 함수가 bounded above (below)인 것을 정의한 것과 같이, 함수의 image가 supremum을 갖는다면 $f$가 supremum을 갖는다고 표현하고, infimum도 마찬가지로 표현한다.

<div class="proposition" markdown="1">

<ins id="pp7">**명제 7**</ins> $A$가 ordered set이고 $X$가 supremum과 infimum을 모두 갖는 $A$의 부분집합이라 하자. 

1. 만일 $X\neq\emptyset$일 경우 $\inf_A X\leq\sup_A X$이다.
2. 만일 $X=\emptyset$이라면, $\sup_AX$와 $\inf_AX$는 각각 $A$의 least, greatest element가 된다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

1. 만일 $X\neq\emptyset$라면 적어도 하나의 원소가 존재한다. 이를 $a$라 하자. 그럼 정의에 의해 $\inf X\leq a$이고 $a\leq\sup X$이며 transitivity에 의해 $\inf_AX \leq\sup_AX$이다. 
2. 만일 $X=\emptyset$라면, $A$의 임의의 원소 $a$는 모든 $x\in X$에 대하여 $a\leq x$ 그리고 $x\leq a$를 만족한다. 따라서 $A$의 임의의 원소는 $X$의 lower bound이자 upper bound가 되며, $\sup_AX$와 $\inf_AX$는 $A$의 least, greatest element가 된다.

</details>

다음은 집합 간의 포함관계에 대한 명제다.

<ins id="pp8">**명제 8**</ins> $A$가 ordered set이고 $X$, $X'$가 $A$의 부분집합이라 하자. 만일 $X$와 $X'$가 모두 $A$에서 supremum을 갖고 $X'\subset X$라면, $\sup X'\leq\sup X$이다.
{: .proposition}

<details class="proof" markdown="1">
<summary>증명</summary>
$x\in X'$를 임의로 택하자. $X'\subseteq X$이므로, $x\in X$이다. 한편 임의의 $x\in X$에 대하여 $x\leq \sup X$가 성립하고 따라서 $\sup X$는 $X'$의 upper bound이다. 이제 정의에 의해 $\sup X'\leq \sup X$이다. 
</details>

물론 위의 정리에서 supremum을 infimum으로 바꿀 수도 있으며, 이 경우 $\inf X\leq\inf X'$이다.

<ins id="pp9">**명제 9**</ins> $(x_i)\_{i\in I}$, $(y_i)\_{i\in I}$가 ordered set $A$의 원소들의 family라 하고 $x_i\leq y_i$가 모든 $i\in I$에 대해 성립한다고 하자. 만일 두 family가 모두 $A$에서 supremum을 갖는다면, $\sup_{i\in I} x_i\leq \sup_{i\in I} y_i$이다.
{: .proposition}

<details class="proof" markdown="1">
<summary>증명</summary>

임의의 $i\in I$에 대하여, $x_i\leq y_i$이고 $y_i\leq \sup y_i$이므로 모든 $i$에 대해 $x_i\leq \sup y_i$이고 따라서 $\sup x_i$의 minimality에 의해 $\sup x_i\leq\sup y_i$이다.
</details>

다음은 언제나 그랬듯 일종의 결합법칙을 증명한 것이다.

<ins id="pp10">**명제 10**</ins>  $(x_i)\_{i\in I}$가 ordered set $A$의 원소들로 이루어진 family이고, $(J_k)\_{k\in K}$가 $I$의 covering이라 하자. 만일 각각의 subfamily들 $(x_i)\_{i\in J_k}$가 $A$에서 supremum을 갖는다면,  $\sup\_{i\in I} x_i$가 존재하는 것은 $\sup\_{k\in K}(\sup\_{j\in J_k}x_j)$가 존재하는 것과 동치이며 두 값은 같다.
{: .proposition}

<details class="proof" markdown="1">
<summary>증명</summary>
$b_k=\sup\_{i\in J_k} x_i$라 적자. 우선 $(x_i)\_{i\in I}$가 supremum을 갖는다고 하고, 이를 $a$라 하자. 그럼 $a\leq b_k$가 모든 $k$에 대해 성립한다. 또, 만약 $c\geq b_k$가 모든 $k$에 대해 성립한다면, 임의의 $x_i$에 대해서 $i\in J\_{k'}$인 $k'$는 $b\_{k'}\geq x_i$를 만족하고, 따라서 어떠한 $i$에 대해서도 $c\geq x_i$이다. 이제 $a$의 최소성에 의해 $c\geq a$이어야 하고, 따라서 $a$가 supremum이며 $\sup\_{i\in I}x_i=\sup\_{k\in K}(\sup\_{i\in J_k} x_j)$이다.  
반대로 $(b_k)\_{k\in K}$가 supremum $a'$를 갖는다 해도 위와 같은 방법으로 증명을 완료할 수 있다.
</details>

다음은 product.

<ins id="pp11">**명제 11**</ins>  $(A_i)\_{i\in I}$가 ordered set들의 family라 하자. $X$가 product set $A=\prod A_i$의 부분집합이고, 각각의 $i$에 대해 $X_i=\operatorname{pr}\_i X$라 하자. 그럼 $\sup_AX$가 존재하는 것과 각각의 $\sup\_{A_i}X_i$가 존재하는 것은 동치이며, $\sup_AX=(\sup\_{A_i}X_i)$이다.
{: .proposition}
<details class="proof" markdown="1">
<summary>증명</summary>
우선 $\sup\_{A_i} X_i$가 각각의 $i$에 대해 존재한다고 하자. 그럼 $(\sup\_{A_i} X_i)\_{i\in I}$가 $X$의 upper bound임은 자명하다. 만일 $(c_i)$가 $X$의 다른 upper bound였다면, 각각의 $c_i$는 $X_i$의 upper bound가 될 것이므로 $\sup\_{A_i}X_i$의 최소성에 의해 $c_i\geq\sup X_i$이고, 따라서 $(c_i)\geq(\sup X_i)\_{i\in I}$이다.  

반대로 $\sup X=(a_i)$가 존재한다고 하자. 모든 $i$에 대해서, $a_i$는 $X_i$의 upper bound이다. 만일 $x_i\in X_i$라면, $i$번째 성분으로 $x_i$를 갖는 $x\in X$가 $x\leq (a_i)$이도록 하는 $x$가 존재하기 때문이다. 이제 임의의 다른 upper bound $a_i'$에 대해, 새로운 원소 $(c_i)$를 $(a_i)$의 $i$번째 성분을 $a_i'$로 바꾸어 정의하면 $c\geq a$이므로 $a_i'\geq a_i$가 된다. 
</details>

<div class="remark" markdown="1">

<ins id="rmk4">**참고**</ins>  Ordered set $A$와 $X'\subseteq X\subseteq A$에 대해서, $\sup_AX'$와 $\sup_XX'$ 중 하나만 존재할 수도 있고, 둘 다 존재하지만 값이 다를 수도 있다. 예컨대 $X'=\\{x\in\mathbb{Q}:x < \sqrt{2}\\}$를 각각의 집합들에서 비교해보자. 

1. $X_1=\mathbb{Q}$의 부분집합으로써, 이 집합의 supremum은 존재하지 않으나 $A=\mathbb{R}$에서는 존재한다. 즉 $\sup_AX'$가 존재하더라도 $\sup_{X_1}X'$는 존재하지 않을 수도 있다.
2. 한편 집합 $X_2=X'\cup \left\\{2\right\\}$를 생각하자. 그럼 $X'\subseteq X_2\subseteq X_1$이고 $\sup\_{X_2}X'=2$이지만 $\sup_{X_1}A$는 존재하지 않는다.
3. 마지막으로 $X'\subseteq X_2\subseteq A$에서, $\sup\_{X_2}X'$와 $\sup\_AX'$는 각각 존재하지만 두 값은 다르다.   

</div>

그러나 여전히 다음을 증명할 수 있다.

<div class="proposition" markdown="1">

<ins id="pp12">**명제 12**</ins>  $A$가 ordered set이고, $X'\subseteq X\subseteq A$이라 하자. 만일 $\sup_AX'$와 $\sup_XX'$이 모두 존재한다면 $\sup_AX'\leq\sup_XX'$이다. 만일 $\sup_AX'$이 존재하고 $X$에 속한다면 $\sup_XX'$도 존재하고 이 값은 $\sup_AX'$와 같다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>
$X'$의 $X$에서의 upper bound들의 집합은 $A$에서의 upper bound들의 집합에 포함되고, 따라서 supremum은 더 크다. 만일 $\sup_AX'$가 존재하고 $X$에 속한다면, 이는 자명하게 $X$에서의 $X'$의 supremum이 된다.
</details>

## Directed set

<ins id="df13">**정의 13**</ins>  Preordered set $A$가 *right directed*이라는 것은 $A$의 원소 두 개짜리 임의의 부분집합이 bounded above인 것이다. 이와 비슷하게 preordered set $A$가 *left directed*라는 것은 $A$의 원소 두 개짜리 부분집합이 bounded below인 것이다.
{: .definition}

예컨대 임의의 집합 $A$에 대하여, 순서집합 $(\mathcal{P}(A),\subseteq)$는 right directed이다. 임의의 $X, Y\in\mathcal{P}(A)$에 대하여, $X\cup Y$는 $\mathcal{P}(A)$의 원소이고 $X$와 $Y$의 upper bound이기 때문이다. 이를 diagram으로 나타내면 다음과 같다.

![directed_system](/assets/images/Set_theory/Elements_in_ordered_set-5.png){:width="394.05px" class="invert" .align-center}

<ins id="pp14">**명제 14**</ins>  Right directed ordered set $A$에서, $A$의 maximal element $a$는 greatest element이다.
{: .proposition}

<details class="proof" markdown="1">
<summary>증명</summary>

$A$가 right directed이므로, 임의의 $x\in A$와 maximal element $a$로 이루어진 집합 $\\{x,a\\}$의 upper bound $y$가 존재한다. 이제 $a$의 maximality에 의하여 $a=y$여야 하므로 $x\leq a$가 성립한다.
</details>

Right directed인 집합들의 곱은 right directed이다. 만약 곱집합에서 두 원소를 뽑아온다면, 우리는 각각의 성분들에 해당하는 원소 두 개씩을 뽑아온 후 원래 집합들이 right directed임을 이용할 수 있기 때문이다. 반면 right directed set의 부분집합이 right directed가 되어야 하는 것은 일반적으로 참이 아니지만, cofinal subset은 언제나 right directed가 된다.

<ins id="df15">**정의 15**</ins> Ordered set $A$가 *lattice*라는 것은 $A$의 임의의 원소 두 개짜리 부분집합이 supremum과 infimum을 갖는 것이다.
{: .definition}

정의에 의해 lattice에서는 임의의 $x,y\in A$에 대하여 두 원소 $\sup\\{x,y\\}$와 $\inf\\{x,y\\}$가 항상 존재한다. 이들을 $x\vee y$와 $x\wedge y$로 쓰고, *join*과 *meet*이라 부른다. Lattice $A$의 임의의 부분집합 $X$가 left directed일 필요충분조건은 임의의 $x,y\in X$에 대해 $x\wedge y\in X$인 것이고, 또 $X$가 right directed일 필요충분조건은 임의의 $x,y\in X$에 대해 $x\vee y\in X$인 것임을 확인할 수 있다.

수학적 귀납법에 의해 lattice $A$의 임의의 유한한 부분집합은 supremum과 infimum을 갖는다는 것을 알 수 있지만 무한한 부분집합에 대해서는 어떠한 이야기도 할 수 없다. 만일 lattice $A$의 (무한집합을 포함한) 임의의 부분집합이 supremum과 infumum을 갖는다면, 이를 *complete lattice*라 부른다.

<ins id="df16">**정의 16**</ins> Preordered set $A$에서의 두 원소 $x$, $y$가 *comparable<sub>비교가능</sub>*하다는 것은 명제 <phrase>$x\leq y$ 혹은 $y\leq x$</phrase>이 항상 참인 것이다. 만약 집합 $A$의 임의의 원소가 comparable하다면, 이를 *totally ordered set<sub>전순서집합</sub>*이라 부른다.
{: .definition}

만약 $A$가 totally ordered set이라면, trichotomy가 성립한다. 즉,임의의 $x, y\in A$에 대하여,  $x=y$, $x < y$, $x > y$ 중 하나가 성립한다. 이 경우엔 $x\leq y$의 부정이 $x > y$가 된다. 하지만 totally ordered set이라는 조건이 빠진 상태에서 이는 일반적으로 성립하지 않는다. (§순서관계 (1), 명제 10 직후의 [참고](/ko/math/set_theory/order_relations#rmk1))

<ins id="pp17">**명제 17**</ins> Totally ordered set $A$에서 ordered set $B$로의 모든 순단조함수 $f$는 단사함수다. 만약 $f$가 순증가라면, $f$는 $A$에서 $f(A)$로의 isomorphism이다.
{: .proposition}
<details class="proof" markdown="1">
<summary>증명</summary>

$f$가 순단조함수라 하자. 그럼 임의의 $x\neq y$에 대하여, $x > y$ 혹은 $x < y$가 성립하므로, $f(x) > f(y)$ 혹은 $f(x) < f(y)$이고, 따라서 $f(x)\neq f(y)$가 되어 $f$는 단사함수다. 특히 $f$가 순증가라면, 우리는 $f(x)\leq f(y)\implies x\leq y$라는 것을 보여야 하는데, 이는 대우명제가 자명하다.
</details>

위의 명제 또한 일반적인 ordered set에서는 성립하지 않았었다. (§순서관계 (1), 정의 13 직후의 [참고](/ko/math/set_theory/order_relations#rmk3))

<ins id="pp18">**명제 18**</ins> $A$가 totally ordered set이고 $X$가 그 부분집합이라 하자. 그럼 $b\in A$가 $X$의 supremum인 것은 $b$가 $X$의 upper bound이고, $c < b$를 만족하는 임의의 $c\in A$에 대하여 $x\in X$이 존재하여 $c < x\leq b$인 것과 동치이다.
{: .proposition}

<details class="proof" markdown="1">
<summary>증명</summary>

자명.

</details>

$A$가 ordered set이고, $a\leq b$라 하자. 그럼 $a\leq x\leq b$를 만족하는 모든 $x$를 모아둔 $X\subseteq A$를 *closed interval*이라 부르고 $[a,b]$로 적는다.  $a\leq x < b$인 $x$들을 모아둔 부분집합은 *half-open interval*이라 부르고 $[a,b)$로 적으며, $(a,b]$도 마찬가지다. $(a,b)$는 *open interval*이라 부르고, 이는 $a < x < b$를 만족하는 모든 $x$를 모아둔 집합이다.  
추가로, $x\leq a$를 만족하는 모든 $x$를 모아둔 부분집합을 *unbounded closed interval*이라 부르고 $(-\infty, a]$로 적는다. $[a,\infty)$, $(-\infty, a)$, $(a, \infty)$도 유사하게 정의한다. 


<ins id="pp19">**명제 19**</ins> Lattice에서 두 interval의 교집합도 interval이다.
{: .proposition}



---
**참고문헌**

**[Bou]** N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---
