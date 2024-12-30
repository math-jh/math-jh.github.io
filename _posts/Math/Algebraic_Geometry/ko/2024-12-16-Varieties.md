---

title: "다양체"
excerpt: "고전 대수기하의 언어"

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/varieties
header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Varieties.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_geometry-ko"

date: 2024-12-16
last_modified_at: 2024-12-16
weight: 1

---

앞으로 별다른 말이 없으면 algeberaically closed field $\mathbb{k}$를 고정한다. 처음 몇 개의 글에서는 고전적인 형태의 대수기하를 살펴볼 것인데, 수학적인 증명은 나중에 스킴을 정의하면 더 일반적인 세팅에서 하게 되므로 증명이 필요한 부분은 나중 글의 링크를 남겨두기로 한다. 

## 아핀공간

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Field $\mathbb{k}$ 위에 정의된 *affine $n$-space<sub>아핀공간</sub>*은 다음 집합

$$\mathbb{A}_\mathbb{k}^n=\{(x_1,\ldots, x_n)ㅣ x_1,\ldots, x_n\in \mathbb{k}\}$$

을 의미한다. 이 때, $\mathbb{A}_\mathbb{k}^n$의 각 원소 $x=(x_1,\ldots, x_n)$을 *점<sub>point</sub>*라 하고, 각각의 $x_i$들을 $x$의 *$i$번째 좌표<sub>$i$-th coordinate</sub>*라 부른다. 

</div>

이제 $\mathbb{k}$를 계수로 갖는 다항식들로 이루어진 polynomial ring $A=\mathbb{k}[\x_1,\ldots,\x_n]$를 생각하자. 그럼 임의의 $f\in A$를 다음의 식

$$\mathbb{A}_\mathbb{k}^n \rightarrow \mathbb{k};\qquad (x_1,\ldots, x_n)\mapsto f(x_1,\ldots, x_n)$$

을 통해 $\mathbb{A}\_\mathbb{k}^n$에서 $\mathbb{k}$로의 함수로 취급할 수 있다. 이제 $A$의 임의의 부분집합 $T$에 대하여, $\mathbb{A}\_\mathbb{k}^n$의 부분집합 $Z(T)$를 다음의 식

$$Z(T)=\{(x_1,\ldots, x_n): \text{$f(x_1,\ldots, x_n)=0$ for all $f\in T$}\}$$

으로 정의하자. 즉 $Z(T)$는 $\mathbb{A}_\mathbb{k}^n$ 위에 정의된 함수들의 모임 $T$의 공통근들으로 생각할 수 있다. 

한편, 부분집합 $T$로 생성되는 $A$의 ideal $\mathfrak{a}$를 생각하면, $Z(T)=Z(\mathfrak{a})$임이 자명하다. 한편 $A$는 noetherian이므로 ([##ref##](Hilbert_basis_thm)) 이러한 $\mathfrak{a}$는 유한히 많은 원소들 $f_1,\ldots, f_r$로 생성될 수 있고 따라서 임의의 $Z(T)$는 항상 유한히 많은 함수들의 공통근들의 모임으로 쓸 수 있다. 

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> 집합 $Y=\mathbb{A}^n_\mathbb{k}$가 *algebraic set<sub>대수적 집합</sub>*이라는 것은 적당한 $T\subseteq A$가 존재하여 $Y=Z(T)$인 것이다. 

</div>

그럼 다음 명제가 성립한다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> 다음이 성립한다.

1. $\emptyset$과 $\mathbb{A}_\mathbb{k}^n$은 algebraic set이다.
2. Algebraic set들의 임의의 교집합은 다시 algebraic set이다. 특히 $\bigcap Z(\mathfrak{a}\_i)=Z(\sum \mathfrak{a}\_i)$이다. 
3. Algebraic set들의 유한한 합집합은 다시 algebraic set이다. 특히 $Z(\mathfrak{a}\_1)\cup Z(\mathfrak{a}\_2)=Z(\mathfrak{a}\_1\mathfrak{a}\_2)$이다. 

따라서 $\mathbb{A}_\mathbb{k}^n$ 위에 algebraic set들을 닫힌집합으로 갖는 유일한 위상구조가 존재한다. ([\[위상수학\] §집합의 내부, 폐포, 경계, ⁋명제 2](/ko/math/topology/other_concepts#prop2))

</div>

이에 대한 증명은 [§스펙트럼, ⁋보조정리 1](/ko/math/algebraic_geometry/spectrums#lem1)에 더 일반적인 버전으로 증명되어 있다.

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> [명제 3](#prop3)에 의해 정의되는 $\mathbb{A}_\mathbb{k}^n$ 위의 위상구조를 *Zariski topology<sub>자리스키 위상</sub>*이라 부른다. 

</div>

## 영점정리

한편, $A$의 부분집합으로부터 $\mathbb{A}\_\mathbb{k}^n$의 부분집합을 얻어내는 위의 과정은 거꾸로 할 수도 있다. $\mathbb{A}\_\mathbb{k}^n$의 부분집합 $Y$가 주어졌다 하고, $A$의 부분집합

$$I(Y)=\{f\in A: \text{$f(x_1,\ldots, x_n)=0$ for all $x\in Y$}\}$$

을 생각하자. 그럼 $I(Y)$가 $A$의 ideal이 된다는 것을 안다. 이들은 정확한 의미에서는 서로의 역은 아니지만, 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> 다음이 성립한다.

1. $A$의 부분집합 $T_1\subseteq T_2$에 대하여, $Z(T_1)\supseteq Z(T_2)$이다.
2. $\mathbb{A}_\mathbb{k}^n$의 부분집합 $Y_1\subseteq Y_2$에 대하여, $I(Y_1)\supseteq I(Y_2)$이다.
3. $\mathbb{A}_\mathbb{k}^n$의 부분집합 $Y_1,Y_2$에 대하여, $I(Y_1\cup Y_2)=I(Y_1)\cap I(Y_2)$이다.
4. 임의의 ideal $\mathfrak{a}\subseteq A$에 대하여, $I(Z(\mathfrak{a}))=\sqrt{\mathfrak{a}}$가 성립한다.
5. 임의의 부분집합 $Y\subseteq \mathbb{A}_\mathbb{k}^n$에 대하여, $Z(I(Y))=\cl(Y)$가 성립한다.

</div>

처음 세 주장은 자명하며, 나중의 두 주장은 [\[가환대수학\] §영점정리, ⁋명제 5](/ko/math/commutative_algebra/nullstellensatz#prop5)이다. 특히, 우리의 관심대상을 $\mathbb{A}_\mathbb{k}^n$의 *closed* subset (즉, algebraic set들)과 $A$의 *radical* ideal들로 제한한다면, $I$와 $Z$는 서로의 역함수가 된다. 추가로 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> Algebraic set $Y$가 irreducible인 것과 $I(Y)$가 prime ideal인 것이 동치이다.

</div>

$Y$가 irreducible일 때 $I(Y)$가 prime ideal인 것은 정의로부터 보일 수 있으며, 거꾸로 $I(Y)$가 prime ideal이라면 이는 radical ideal이기도 하므로 유일한 algebraic set $Z(I(Y))$에 대응되고, 따라서 유일성으로부터 $Z(I(Y))=Y$를 확인한 후 정의를 사용하면 된다.

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> Affine space $\mathbb{A}_\mathbb{k}^n$의 ireducible closed subset을 *affine variety<sub>아핀다양체</sub>*라 부른다. Affine variety의 열린집합을 *quasi-affine variety<sub>준아핀다양체</sub>*라 부른다. 

</div>

몇 가지 예시를 살펴보자.

<div class="example" markdown="1">

<ins id="ex8">**예시 8**</ins> 가장 간단한 예시인 $\mathbb{A}\_\mathbb{k}^1$를 보자. 그럼 $\mathbb{k}[\x]$는 PID이므로 임의의 ideal은 하나의 다항식으로 생성되고, $\mathbb{k}$가 algebraically closed라는 가정으로부터 $\mathbb{k}[\x]$의 모든 원소는 일차식들의 곱으로 인수분해 가능하다. 따라서 $\mathbb{A}\_\mathbb{k}^1$의 닫힌집합들은 유한집합, 공집합, 그리고 전체집합 뿐임을 안다. 

</div>

특히 $\mathbb{A}\_\mathbb{k}^1$은 Hausdorff space가 아니다. 뿐만 아니라 $\mathbb{A}\_\mathbb{k}^1$은 irreducible이기도 한데, 이는 $(0)$이 prime ideal이므로 자명하다. 

일반적인 $\mathbb{A}_\mathbb{k}^n$의 경우, $\mathbb{k}[\x_1,\ldots, \x_n]$의 모든 원소를 일차식의 곱으로 나타낼 수 있는 것은 아니므로 [예시 8](#ex8)과 같이 위상구조를 딱 떨어지게 설명할 수 있는 것은 아니다. 가령 임의의 irreducible polynomial $f(\x_1,\ldots, \x_n)$의 경우, $(f)$가 prime ideal이 되고 따라서 irreducible algebraic set $Z(f)$를 정의한다. 이는 정의에 의해 $f$의 근들의 모임이 되며, 나중에 적절한 방식으로 차원을 정의하고 나면 $n$차원 공간에서 하나의 식으로 정의한 이 집합이 $n-1$차원이 되는 것을 확인할 수 있다. 

한편 $\mathbb{A}_\mathbb{k}^n$의 각 점 $x=(x_1,\ldots, x_n)$은 다음의 maximal ideal

$$(\x_1-x_1,\ldots, \x_n-x_n)$$

에 대응된다. 그럼 이들 점이 *minimal*한 irreducible closed subset이라는 것으로부터, $A$의 모든 maximal ideal들은 모두 이러한 꼴이어야 한다는 것을 안다. 

## Coordinate ring

Affine variety $Y\subseteq \mathbb{A}_\mathbb{k}^n$에 대하여, $Y$ 위에서 정의된 함수를 생각하기 위해서는 $A$의 원소들이 전부 필요하지는 않다. 어차피 $Y$ 위에서 항등적으로 $0$이 되는 함수들은 $Y$ 위의 함수로서는 어떠한 역할도 하지 않기 때문이다.

<div class="definition" markdown="1">

<ins id="def9">**정의 9**</ins> Affine variety $Y\subseteq \mathbb{A}_\mathbb{k}^n$에 대하여, ring $A/I(Y)$를 $Y$의 *coordinate ring<sub>좌표환</sub>*이라 부르고 $A(Y)$로 적는다. 

</div>

정의에 의해 $Y$가 irreducible이므로 [명제 6](#prop6)에 의하여 $I(Y)$는 prime ideal이고, 따라서 $A(Y)$는 항상 integral domain이다. 뿐만 아니라, $A$가 $\mathbb{k}$-algebra로서 finitely generated이므로 $A(Y)$ 또한 그러하다. 거꾸로 임의의 finitely generated $\mathbb{k}$-algebra는 항성 적당한 affine variety의 coordinate ring으로 나오는 것을 확인할 수 있다.

대수기하학에서 차원을 다룰 때는 Krull dimension을 사용한다. ([\[위상수학\] §차원, ⁋정의 9](/ko/math/topology/dimension#def9)) 한편 우리는 ring의 차원 또한 정의한 적이 있다. ([##ref##]()) 그럼 [명제 6](#prop6)의 결과에 의하여 다음이 자명하다.

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10**</ins> Affine algebraiic set $Y\subseteq \mathbb{A}_\mathbb{k}^n$에 대하여, $\dim Y=\dim A(Y)$가 성립한다.

</div>

특히 $\dim A(Y)$는 우리가 대수적으로 알고 있는 대상이므로, 예컨대 [##ref##]()와 같은 결과를 사용할 수 있다. 특히 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="prop11">**명제 11**</ins> $\mathbb{A}_\mathbb{k}^n$의 variety $Y$가 $n-1$차원인 것과, 적당한 non-constant irreducible polynomial $f\in \mathbb{k}[\x_1,\ldots, \x_n]$이 존재하여 $Y=Z(f)$인 것이 동치이다. 

</div>

## 사영다양체

우리가 관심을 갖는 또 다른 대상은 projective space이다. Affine variety를 다룰 때 우리의 기본적인 대상이 affine space $\mathbb{A}^n\_\mathbb{k}$였듯, projective variety를 다룰 때의 기본적인 대상은 projective space $\mathbb{P}\_\mathbb{k}^n$이다. 이는 언제나 그러하듯, $\mathbb{A}\_\mathbb{k}^{n+1}\setminus\\{(0,\ldots,0)\\}$ 위에 다음의 equivalence relation

$$(x_0,\ldots, x_n)\sim (y_0,\ldots, y_n)\iff y_i=\lambda x_i \text{ for some $\lambda\neq 0$, for all $i=0,\ldots, n$}$$

을 주어 만들어진 공간이다. 그럼 affine space에서와 마찬가지로 polynomial ring $S=\mathbb{k}[\x_0,\ldots, \x_n]$의 각 원소들을 $\mathbb{P}_\mathbb{k}^n$ 위의 함수로 보고, 이를 이용해 Zariski topology를 정의하려고 하는 것이 자연스럽다. 그러나 임의의 다항식 $f\in S$에 대하여, 일반적으로

$$f(x_0,\ldots, x_n)\neq f(\lambda x_0,\ldots, \lambda x_n)$$

이므로 $f$는 $\mathbb{P}_\mathbb{k}^n$ 위의 함수를 정의하지 않는다. 그러나, affine space에 Zariski topology를 정의하기 위해 필요했던 것은 함숫값이 아니라, $f$의 해집합이었으므로 만일 $f$를 $d$차 동차다항식으로 잡는다면 다음 식

$$f(\lambda x_0,\ldots, \lambda x_n)=\lambda^d f(x_0,\ldots, x_n)\qquad\text{for any $\lambda\neq 0$ and any $x\in \mathbb{A}_\mathbb{k}^{n+1}$}$$

이 성립한다. 즉, $f$는 $\mathbb{P}_\mathbb{k}^n$ 위의 함수로서는 잘 정의되지 않더라도, 그 해집합 $Z(f)$는 잘 정의된다. 

이 논의를 이어가기 위해서는 $S$를 단순한 ring이 아니라 다항식의 차수로 grading이 주어진 graded ring으로 봐야하며, homogeneous polynomial들의 해집합만을 생각해야 한다. 이는 graded ring의 언어로 옮기면, 우리는 $S$의 *homogeneous ideal*들의 zero set $Z(\mathfrak{a})$만 생각하면 된다는 뜻이다. ([\[대수적 구조\] §등급환, ⁋명제 6](/ko/math/algebraic_structures/graded_rings#prop6))

그럼 [명제 3](#prop3)에 대응되는 결과는 다음과 같다. 

<div class="proposition" markdown="1">

<ins id="prop12">**명제 12**</ins> $S=\mathbb{k}[\x_0,\ldots, \x_n]$에 대하여 다음이 성립한다.

2. Homogeneous ideal들의 family $\\{\mathfrak{a}_i\\}$에 대하여 $Z(\sum \mathfrak{a}_i)=\bigcap Z(\mathfrak{a}_i)$이 성립한다.
1. Homogeneous ideal들 $\mathfrak{a},\mathfrak{b}$에 대하여 $Z(\mathfrak{ab})=Z(\mathfrak{a})\cup Z(\mathfrak{b})$이 성립한다.

</div>

이는 [§스킴, ⁋보조정리 8](/ko/math/algebraic_geometry/schemes#lem8)에서 일반적인 graded ring $S$에 대해 증명되어 있다. 그럼 다음을 정의한다.

<div class="definition" markdown="1">

<ins id="def13">**정의 13**</ins> $\mathbb{P}_\mathbb{k}^n$의 irreducible algebraic set을 *projective variety<sub>사영다양체</sub>*라 부른다. Projective variety의 open subset을 *quasi-projective variety<sub>준사영다양체</sub>*라 부른다. 

</div>

이제 $\mathbb{P}_\mathbb{k}^n$의 임의의 부분집합 $Y$가 주어졌다 하고, 

$$I(Y)=\{f\in S: f(x_0,\ldots, x_n)=0\text{ for all $x\in Y$ and $f$ is homogeneous}\}$$

으로 정의하자. 그럼 $I(Y)$는 $S$의 homogeneous ideal이 된다. 이제 [명제 5](#prop5)와 비슷한 다음 명제가 성립한다.

<div class="proposition" markdown="1">

<ins id="prop14">**명제 14**</ins> 다음이 성립한다.

1. $S$의 homogeneous element로 이루어진 부분집합 $T_1\subseteq T_2$에 대하여, $Z(T_1)\supseteq Z(T_2)$이다.
2. $\mathbb{P}_\mathbb{k}^n$의 부분집합 $Y_1\subseteq Y_2$에 대하여, $I(Y_1)\supseteq I(Y_2)$이다.
3. $\mathbb{P}_\mathbb{k}^n$의 부분집합 $Y_1,Y_2$에 대하여, $I(Y_1\cup Y_2)=I(Y_1)\cap I(Y_2)$이다.
4. 임의의 homogeneous ideal $\mathfrak{a}\subseteq S$가 $Z(\mathfrak{a})\neq \emptyset$을 만족한다면 $I(Z(\mathfrak{a}))=\sqrt{\mathfrak{a}}$가 성립한다.
5. 임의의 부분집합 $Y\subseteq \mathbb{P}_\mathbb{k}^n$에 대하여, $Z(I(Y))=\cl(Y)$가 성립한다.

</div>

넷째 조건에서 $Z(\mathfrak{a})\neq\emptyset$인 것과 $\sqrt{\mathfrak{a}}$가 irrelevant ideal $S_+$이거나 $S$ 전체인 것이 동치인 것을 안다. 

[명제 6](#prop6)과 마찬가지로 다음 명제 또한 쉽게 증명할 수 있다.

<div class="proposition" markdown="1">

<ins id="prop15">**명제 15**</ins> Algebraic set $Y\subseteq \mathbb{P}^n_\mathbb{k}$가 irreducible인 것과 $I(Y)$가 (homogeneous) prime ideal인 것이 동치이다. 

</div>

또, [정의 9](#def9)와 비슷한 다음의 정의를 내린다.

<div class="definition" markdown="1">

<ins id="def16">**정의 16**</ins> Projective variety $Y\subseteq \mathbb{P}_\mathbb{k}^n$에 대하여, graded ring $S/I(Y)$를 $Y$의 *coordinate ring*이라 부르고 $S(Y)$로 적는다.

</div>

한편 $\mathbb{P}\_\mathbb{k}^n$은 (일반적인 위상에서는) $\mathbb{A}\_\mathbb{k}^n$의 one-point compactification으로 생각할 수도 있는데, 이는 Zariski topology에서도 마찬가지다. 이를 엄밀하게 이야기하면, $\mathbb{P}\_\mathbb{k}^n$은 $n+1$개의 open set들

$$U_i=\{[x_0:\cdots:x_n]: x_i\neq 0\}\subseteq \mathbb{P}_\mathbb{k}^n$$

로 덮이며, 이 때

$$\varphi_i: U_i \rightarrow \mathbb{A}_\mathbb{k}^n,\qquad\text{where coordinates of $\mathbb{A}_\mathbb{k}^n$ is given by $\x_{0/i},\ldots,\x_{(i-1)/i},\x_{(i+1)/i},\ldots, \x_{n/i}$}$$

를 다음의 식

$$(x_0,\ldots, x_n)\mapsto \left(\frac{x_0}{x_i},\ldots, \frac{x_{i-1}}{x_i},\frac{x_{i+1}}{x_i},\ldots, \frac{x_n}{x_i}\right)$$

으로 정의하면 이것이 homeomorphism이 된다. 