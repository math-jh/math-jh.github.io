---

title: "자연수와 무한집합"
excerpt: "자연수의 정의와 무한집합의 성질들"

categories: [Math / Set Theory]
permalink: /ko/math/set_theory/natural_numbers
header:
    overlay_image: /assets/images/Set_theory/Natural_numbers.png
    overlay_filter: 0.5
sidebar: 
    nav: "set-ko"

date: 2021-09-04
last_modified_at: 2022-04-14
weight: 18

---

## 자연수의 정의 (2)

우리는 앞서 ordinal을 정의하며 motivation을 주기 위해 자연수 또한 정의했었다. ([§Ordinal과 well-ordering<sup>†</sup>](/ko/math/set_theory/ordinals)) 이제 우리는 이 방법 대신 우리가 이미 정의한 cardinal을 사용해서 자연수를 만들고, cardinal number들 위에서 정의했던 연산과 대소관계를 이용해 자연수의 구조를 탐구할 것이다.

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> Cardinal $\mathfrak{a}$가 *유한하다<sub>finite</sub>*는 것은 $\mathfrak{a}\neq\mathfrak{a}+\mathbf{1}$인 것이다. 유한한 cardinal을 *자연수<sub>natural number</sub>*라고 부른다. 집합 $E$에 대하여, cardinal $\operatorname{card} E$가 유한하다면 이 집합을 유한하다고 부르며, 이 때 $\operatorname{card} E$를 집합 $E$의 *원소의 갯수*라고 부른다.

</div>

자연수는 cardinal들의 집합의 부분집합이므로 well-ordered이다. ([§Cardinal, 명제 5](/ko/math/set_theory/cardinals#pp5)) 따라서 자연수에서 귀납법을 사용할 수 있다. ([§Ordinal과 well-ordering<sup>†</sup>, 보조정리 12](/ko/math/set_theory/ordinals#lem12))

<div class="proposition" markdown="1">

<ins id="pp2">**명제 2**</ins> Cardinal $\mathfrak{a}$가 유한한 것과 $\mathfrak{a}+\mathbf{1}$이 유한한 것이 동치이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

[§Cardinal, 명제 11](/ko/math/set_theory/cardinals#pp11)에 의하여, $\mathfrak{a}=\mathfrak{b}$인 것은 $\mathfrak{a}+\mathbf{1}=\mathfrak{b}+\mathbf{1}$인 것과 동치이다. 이제 $\mathfrak{b}=\mathfrak{a}+\mathbf{1}$로 잡으면, 가정에 의해 $\mathfrak{a}\neq\mathfrak{b}$이고, 따라서

$$\mathfrak{b}=\mathfrak{a}+\mathbf{1}\neq\mathfrak{b}+\mathbf{1}$$

이므로 $\mathfrak{a}$가 유한한 것은 $\mathfrak{b}=\mathfrak{a}+\mathbf{1}$이 유한인 것과 동치이다.

</details>

이제부터 자연수들은 블랙레터 $\mathfrak{a}$, $\mathfrak{b}$ 대신 $m$, $n$ 등과 같은 일반적인 알파벳으로, 그리고 cardinal number인 $\mathbf{0}$과 $\mathbf{1}$도 간단히 $0$과 $1$로 쓰기로 한다. 우리는 자연수들 사이의 대소관계를 정의할 것이다. 우선 간단한 보조정리 하나를 보이자.

<div class="proposition" markdown="1">

<ins id="lem3">**보조정리 3**</ins> $\mathfrak{a}$와 $\mathfrak{b}$가 cardinal이라 하자. 그럼 $\mathfrak{a}\geq\mathfrak{b}$인 것은 어떠한 cardinal $\mathfrak{c}$가 존재하여 $\mathfrak{a}=\mathfrak{b}+\mathfrak{c}$인 것과 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$\mathfrak{a}\geq\mathfrak{b}$인 것은, cardinal $\mathfrak{a}$와 $\mathfrak{b}$를 갖는 집합 $A$, $B$가 각각 존재하여 $A\supset B$인 것과 동치이다. 이제 $A=B\cup(A\setminus B)$.

</details>

<div class="proposition" markdown="1">

<ins id="pp4">**명제 4**</ins> $n$이 자연수라 하자. 그럼 $\mathfrak{a}\leq n$을 만족하는 모든 cardinal $\mathfrak{a}$도 자연수이다. 만일 $n\neq 0$이라면, 유일한 자연수 $m$이 존재하여 $n=m+1$이다. 이 때, $a$에 관한 unary relation $a&lt;n$은 $a\leq m$과 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 첫 번째를 보이기 위해 $\mathfrak{a}$가 $\mathfrak{a}\leq n$을 만족하는 cardinal이라 하자. 그럼 어떤 cardinal $\mathfrak{b}$가 존재하여 $n=\mathfrak{a}+\mathfrak{b}$이다. 이제

$$(\mathfrak{a}+1)+\mathfrak{b}=(\mathfrak{a}+\mathfrak{b})+1=n+1\neq n$$

이므로 $(\mathfrak{a}+1)+\mathfrak{b}\neq\mathfrak{a}+\mathfrak{b}$이다. 따라서 $\mathfrak{a}+1\neq\mathfrak{a}$이므로 $\mathfrak{a}$는 자연수다.

만일 $n\neq 0$이라면 $n\geq 1$이므로, 앞선 보조정리에 의해 $n=m+1$인 cardinal $m$이 존재하며, 앞선 논리에 의해 $m$도 자연수이다. 따라서  $a&lt;n$이 $a\leq m$과 동치임만 보이면 된다.

우선 $a&lt;n$이라면, 유일한 자연수 $b$가 존재하여 $n=a+b$이다. $b\neq 0$이므로, 어떠한 $c$에 대해 $b=c+1$이다. 그럼

$$m+1=n=a+b=a+(c+1)=(a+c)+1$$

에서 $m=a+c$이다. 따라서 $a\leq m$이다. 반대로 만일 $a\leq m$일 경우, 

$$a\leq m+1=n$$

이고, $a=n=m+1>m$은 모순이므로 $a\neq n$이다. 따라서 $a&lt;n$이다.

</details>

<div class="proposition" markdown="1">

<ins id="pp5">**명제 5**</ins> $a$와 $b$가 자연수라 하자. $a&lt;b$는 어떤 자연수 $c>0$가 존재하여 $b=a+c$인 것과 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[보조정리 3](#lem3)의 직접적인 결과다. $a\leq b$이므로 그러한 $c\geq 0$가 존재하는데, $c=0$이라면 $a=b$이기에 $c\neq 0$이기 때문이다.

</details>

지금까지 한 것들을 정리하면 다음을 얻는다. 

<div class="proposition" markdown="1">

<ins id="pp6">**명제 6**</ins> $a$와 $b$가 자연수라 하자. 그럼 함수 $x\mapsto a+x$는 구간 $[0,b]$에서 $[a,a+b]$로의 strictly increasing order isomorphism이다.

</div>

따라서 임의의 구간 $[a,b]$를 원소의 갯수 $b-a+1$개짜리 집합과 동일하게 취급할 수 있다. 유한한 정의역을 가지는 함수를 *유한수열*이라 부르는데, 모든 유한집합은 위의 정리에 의해 $[1,n]$과 동일시될 수 있으므로 우리는 항상 유한수열이 $1$부터 $n$까지의 자연수 위에서 정의된 것으로 취급할 수 있다. 

<div class="proposition" markdown="1">

<ins id="pp7">**명제 7**</ins> $(a_i)_{i\in I}$가 자연수를 값으로 갖는 유한수열이라 하자. 그럼 $\sum a_i$와 $\prod a_i$는 모두 자연수이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$I$가 유한이므로, 임의의 자연수 $a$와 $b$에 대해 $a+b$와 $ab$가 자연수임만 보이면 충분하다. 이는 $b$에 대한 귀납법으로 보이면 된다. 우선 $a+0=a$가 자연수이고, $a+k$가 자연수라면 $a+(k+1)=(a+k)+1$ 또한 마찬가지이므로 쉽게 보일 수 있다. 곱셈도 마찬가지.

</details>

## 자연수 집합의 성질들

<div class="definition" markdown="1">

<ins id="df8">**정의 8**</ins> $E$가 공집합이 아니고 $A$가 $E$의 부분집합이라 하자. $A$의 *특성함수<sub>characteristic function</sub>*는 함수 $\chi_A:E\rightarrow \\{0,1\\}$이며, 그 값은 다음의 식

$$\chi_A(x)=\begin{cases}1&\text{if $x\in A$}\\ 0&\text{if $x\in E\setminus A$}\end{cases}$$

으로 주어진다.

</div>

종종 조금 더 현대적인 표기법으로, $\chi_A$ 대신 $1_A$ 등과 같이 쓰기도 한다.  
다음의 정리는 자명하게 보일 수 있다.

<div class="proposition" markdown="1">

<ins id="pp9">**명제 9**</ins> 집합 $E$의 두 부분집합 $A$와 $B$에 대하여,

$$\begin{aligned}
\chi_{E\setminus A}(x)&=1-\chi_A(x)\\
\chi_{A\cap B}(x)&=\chi_A(x)\chi_B(x)\\
\chi_{A\cup B}(x)+\chi_{A\cap B}(x)&=\chi_A(x)+\chi_B(x)
\end{aligned}$$

가 성립한다.
</div>


이제 집합론보다는 다른 여러 곳에서 쓸 자연수의 성질을 조금 정리하고 넘어가자. 우선 다음은 유클리드 호제법이라 불리는 나눗셈 알고리즘이다.

<div class="proposition" markdown="1">

<ins id="thm10">**정리 10**</ins>  $a$와 $b$가 $b>0$를 만족하는 자연수들이라 하자. 그럼 유일한 자연수 $Q$와 $R$가 존재하여 $a=bq+r$이고 $r<b$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

만일 그러한 쌍이 존재한다면 $Q$는 $a&lt;b(q+1)$를 만족하는 가장 작은 자연수여야 한다. 그렇지 않으면

$$r=a-bq<0\quad\text{or}\quad r=a-bq\geq b$$

이 되기 때문이다. 존재성을 보이기 위해, $a&lt;a+1&lt;b(a+1)$라 하자. 그럼 $a&lt;bp$를 만족하는 $P$의 집합은 공집합이 아니다. 이제 well-orderedness에 의해, least element $m$이 존재하므로 $m=q+1$라 하면 $Q$가 주어진 조건을 만족한다.

</details>

이 정리에서, $R$을 $a$를 $b$로 나눈 *나머지*라 한다. 만일 $r=0$라면 $a$가 $b$의 *배수*라 하거나, $a$가 $b$에 의해 나누어떨어진다고 하고, $b$가 $a$의 *약수*라고도 한다. 이 경우 자연수 $Q$를 $a$를 $b$로 나눈 *몫*이라 하고 $a/b$로 적는다.  
만일 두 자연수 $a$와 $b$가 같은 약수를 가진다면, 이를 $a$와 $b$의 *공약수*라 하고, 공약수 중 가장 큰 것을 *최대공약수*라 한다. 또, $a$와 $b$를 약수로 가지는 어떠한 수가 있다면, 그 수를 $a$와 $b$의 *공배수*라 하고, 그 중 가장 작은 것을 *최소공배수*라 한다.

우리는 아직 정수를 정의하지는 않았지만, 위 정리는 $a$와 $b$가 자연수가 아니라 정수여도 마찬가지로 성립한다. 이에 따른 결과가 다음의 *Bézout's lemma*이다.

<div class="proposition" markdown="1">

<ins id="crl11">**따름정리 11 (Bézout's lemma)**</ins> 임의의 두 정수 $a$, $b$가 최대공약수 $d$를 갖는다고 하자. 그럼 적당한 두 정수 $x$와 $b$가 존재하여 $ax+by$이도록 할 수 있다. 

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

집합 $S$를 $ax+by>0$을 만족하는 $ax+by$들의 집합이라 하자. 그럼 자연수의 well-orderedness에 의하여 이 집합의 최소 원소 $d$가 존재한다. 이제 앞선 유클리드 호제법에서, $a=dq+r$이라 하자. 그럼 $d=ax+by$를 대입하여 $a(xq-1)+r+byq=0$, 혹은 $r=a(1-xq)+b(-yq)$를 얻는다. 만일 $r\neq 0$이라면 $r\in S$이고, 따라서 $r\geq d$인데 이는 모순이다. 따라서 $r=0$이고 $d$는 $a$를 나눈다. 이와 비슷하게 $d$는 $b$도 나누므로 $d$는 $a$와 $b$의 공약수이고, $a$와 $b$의 임의의 공약수는 $ax+by=d$ 또한 나눠야 하므로 $d$가 최대공약수이다.

</details>

## 무한집합의 정의와 성질들
<div class="definition" markdown="1">

<ins id="df11">**정의 11**</ins> 집합이 *무한하다<sub>infinite</sub>*는 것은 유한하지 않다는 것이다.

</div>

이제 infinite cardinal의 성질에 대해 살펴보자. 앞서 finite cardinal은 $\mathfrak{a}\neq\mathfrak{a}+1$을 만족했다. 다음 정리는 이와 유사한 infinite cardinal만의 성질이다.

<div class="proposition" markdown="1">

<ins id="pp12">**명제 12**</ins> 모든 infinite cardinal $\mathfrak{a}$에 대하여 $\mathfrak{a}^2=\mathfrak{a}$가 성립한다.

</div>

이를 보이기 위해서는 다음의 보조정리들을 먼저 증명해야 한다.

<div class="proposition" markdown="1">

<ins id="lem13">**보조정리 13**</ins> 임의의 무한집합 $E$는 $\mathbb{N}$과 equipotent한 부분집합을 포함한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$E$의 well-ordering이 존재한다. 자신을 제외한 $\mathbb{N}$의 임의의 segment는 항상 유한하므로, $E$는 $\mathbb{N}$의 segment와 isomorphic할 수 없다. 따라서 $\mathbb{N}$이 $E$의 segment와 isomorphic하다. ([§<sup>†</sup>Ordinal과 well-ordering, 명제 18](/ko/math/set_theory/ordinals#pp18))

</details>
<div class="proposition" markdown="1">

<ins id="lem14">**보조정리 14**</ins> 집합 $\mathbb{N}\times\mathbb{N}$은 $\mathbb{N}$과 equipotent하다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

다음의 수열

$$(1,1),\;\; (1,2),(2,1),\;\; (1,3),(2,2),(3,1),\;\; \cdots$$

에 의해 자명.

</details>

<details class="proof--alone" markdown="1">
<summary>명제 12의 증명</summary>

$E$가 cardinal $\mathfrak{a}$를 갖는 집합이라 하자. 그럼 첫 번째 보조정리로부터 어떤 $D\subset E$는 $\mathbb{N}$과 equipotent하고, 따라서 두 번째 보조정리에 의해 $D\times D$와 $D$ 사이의 bijection이 존재한다. 이를 $f$라 하자. 

$D$를 포함하는 $E$의 부분집합 $X$와, 그 위에서 정의된 $f$의 extension $\psi:X\rightarrow X\times X$에 대해 $\mathfrak{M}$이 이러한 쌍 $(X,\psi)$들의 모임이라 하자. 그럼 $\mathfrak{M}$의 임의의 chain에 대하여 가장 큰 정의역을 갖는 쌍이 maximal element가 되므로, $\mathfrak{M}$은 inductive한 집합이고, 따라서 Zorn's lemma에 의해 $\mathfrak{M}$의 maximal element $(F, \tilde{f})$가 존재한다.

이제 $\operatorname{card} F=\mathfrak{a}$임을 보이면 충분하다. 만일 $\operatorname{card} F=\mathfrak{b}&lt;\mathfrak{a}$라면, bijection $\tilde{f}$에 의해 $\mathfrak{b}=\mathfrak{b}^2$이므로 

$$\mathfrak{b}\leq 2\mathfrak{b}\leq 3\mathfrak{b}\leq \mathfrak{b}^2=\mathfrak{b}$$

에서 $\mathfrak{b}=2\mathfrak{b}=3\mathfrak{b}$이다. 그럼 $\mathfrak{b}&lt;\mathfrak{a}$에서 $\operatorname{card}(E\setminus F)>\mathfrak{b}$이다. 그렇지 않다면

$$\mathfrak{a}=\operatorname{card} E=\operatorname{card}(F\cup(E\setminus F))\leq\operatorname{card} F+\operatorname{card}(E\setminus F)\leq\mathfrak{b}+\mathfrak{b}=2\mathfrak{b}=\mathfrak{b}$$

가 되어 모순이기 때문이다. 따라서 어떤 $Y\subset E\setminus F$가 존재하여 $\operatorname{card} Y=\mathfrak{b}$이다. $Z=F\cup Y$라 하자. 그럼

$$Z\times Z=(F\times F)\cup(F\times Y)\cup(Y\times F)\cup (Y\times Y)$$

이고, 우변의 네 항들은 모두 mutually disjoint한 집합들이다. $F$와 $Y$가 equipotent하므로, 

$$\operatorname{card}(F\times Y)=\operatorname{card}(Y\times F)=\operatorname{card}(F\times F)=\mathfrak{b}^2=\mathfrak{b}$$

이고 따라서

$$\operatorname{card}((F\times Y)\cup(Y\times F)\cup(Y\times Y))=3\mathfrak{b}=\mathfrak{b}=\operatorname{card} Y$$

이다. 그러므로 $Y$에서 이 집합들의 합집합으로의 bijection이 존재하고, 따라서 $Z=F\cup Y$에서 $Z\times Z$로의 bijection이 존재한다. $F$에서는 $\tilde{f}:F\rightarrow F\times F$로, $Y$에서는 방금 만든 bijection을 이용하면 되기 때문이다. 이는 $F$의 maximality에 모순이므로 $\operatorname{card} F=\mathfrak{a}$여야 한다.

</details>

이를 활용하면 다음은 쉽게 보일 수 있다.

<div class="proposition" markdown="1">

<ins id="crl15">**따름정리 15**</ins> $\mathfrak{a}$가 infinite cardinal이라면, 임의의 $n\geq 1$에 대해 $\mathfrak{a}^n=\mathfrak{a}$이다. 0이 아닌 cardinal들의 유한한 family $(\mathfrak{a}\_i)_{i\in I}$에 대하여, 만일 이들 중 가장 큰 cardinal이 infinite cardinal $\mathfrak{a}$라면 이들의 곱과 합은 모두 $\mathfrak{a}$이다.

</div>

우리는 무한집합들 중 $\mathbb{N}$과 equipotent한 것을 특별히 *countable*이라 부른다.


---
**참고문헌**

**[Bou]** N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---
