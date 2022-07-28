---
layout: single
date: 2021-10-07
title: "가환군과 체"
categories: [Math / Linear Algebra]
permalink: /ko/math/linear_algebra/fields
header:
    overlay_image: /assets/images/Linear_algebra/Fields.png
    overlay_filter: 0.5
toc: true
toc_sticky: true
comments: true
sidebar: 
    nav: "preliminaries"
excerpt: "Fields and vector spaces"
lang: ko
weight: 1
---

선형대수학에서 다루는 공간은 *벡터공간*으로, 고등학교 때 배웠던 좌표공간을 일반화하는 개념이다. 벡터공간은 말 그대로 벡터들의 공간으로, 이들 벡터들 사이의 덧셈이 잘 정의된다. 또, 어떤 벡터에 상수를 곱하여 다른 벡터를 얻어낼 수도 있는데, 벡터공간을 다룰 때는 이 상수들을 *스칼라*라고 부른다. 스칼라들의 집합은 우리가 곧 정의할 *field*를 이루어야 한다.

이번 글에서는 field를 정의한다.

## 체

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> 집합 $G$와, $G$ 위에 정의된 이항관계 $+:G\times G\rightarrow G$가 *abelian group<sub>가환군</sub>*이라는 것은 다음의 조건들이 만족되는 것이다.

1. $+$는 *결합법칙*을 만족한다. 즉, 임의의 $a,b,c\in G$에 대하여, $(a+b)+c=a+(b+c)$가 성립한다.
2. $+$에 대한 항등원이 존재한다. 즉, 어떤 $0\in G$가 존재하여, 임의의 $a\in G$에 대해 $a+0=0+a=a$가 성립한다.
3. $+$에 대한 역원이 항상 존재한다. 즉, 임의의 $a\in G$가 주어질 때마다, $-a\in G$가 존재하여 $a+(-a)=(-a)+a=0$가 성립한다.
4. $+$는 *교환법칙*을 만족한다. 즉, 임의의 $a,b\in G$에 대하여, $a+b=b+a$가 성립한다.

</div>

만일 마지막 조건이 성립하지 않는다면 $G$를 *group<sub>군</sub>*이라 부른다. Abelian group이 아닌 group은 선형대수학에서 명시적으로 등장하지는 않지만 알아두는 것이 좋다.

어쨌든 정의를 사용해 간단한 명제를 증명할 수 있다.

<div class="proposition" markdown="1">

<ins id="pp2">**명제 2**</ins> $G$가 abelian group이라 하자. 그럼

1. $G$의 항등원은 유일하다.
2. 임의의 $a\in G$에 대하여, $a$의 역원 $-a$ 또한 유일하다.
3. 만일 $a+b=a+c$가 성립한다면, $b=c$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

1. $0'$이 [정의 1](#df1)의 둘째 조건을 만족하는 또 하나의 원소라고 하자. 그럼 $a=0$과 항등원 $0'$에 대해 둘째 조건을 적용하면, 

    $$0+0'=0'+0=0$$
    
    이 성립한다. 그런데 $a=0'$과 항등원 $0$에 대해 둘째 조건을 적용하면, 마찬가지로
    
    $$0+0'=0'+0=0'$$
    
    을 얻는다. 따라서 $0=0'$이므로, 항등원은 유일하다.

2. 첫 번째와 비슷하게 진행하면 된다. $(-a)'$가  [정의 1](#df1)의 셋째 조건을 만족하는 또 하나의 원소라고 하자. 그럼
    
    $$(-a)=(-a)+0=(-a)+(a+(-a)')=((-a)+a)+(-a)'=0+(-a)'=(-a)'$$
    
    이므로, $(-a)=(-a)'$가 성립한다.
    
3. 양 변에 $(-a)$를 더하면 된다.
</details>

다음 따름정리는 항등원과 역원의 유일성으로부터 바로 얻어진다.

<div class="proposition" markdown="1">

<ins id="crl3">**따름정리 3**</ins> Abelian group $(G,+)$와 임의의 원소 $a,b$에 대하여 다음이 성립한다.

1. $-(-a)=a$
2. $-(a+b)=-a+(-b)=-a-b$

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

1. $-a$의 역원 $-(-a)$가 $a$와 같음을 보여야 한다. 역원은 유일하므로, 만일 어떤 $x\in G$에 대하여 다음의 식

    $$(-a)+x=x+(-a)=0$$

    이 성립한다면 <em_ko>반드시</em_ko> $x=-(-a)$여야 한다. 그런데 $x=a$일 경우, $-a$가 $a$의 역원이라는 사실로부터 위의 식이 성립한다. 따라서 $a=-(-a)$이다. 
2. 앞선 증명처럼 $x=-a+(-b),-a-b$가 모두

    $$(a+b)+x=x+(a+b)=0$$

    을 만족함을 보이면 충분하다. 예를 들어 $x=-a+(-b)$인 경우, 

    $$\begin{aligned}(a+b)+x&=(a+b)+((-a)+(-b))=(b+a)+((-a)+(-b))=b+(a+(-a))+(-b)=b+(-b)\\&=0\end{aligned}$$

    이고 이와 비슷하게, 혹은 교환법칙에 의해 $x+(a+b)=0$임도 보일 수 있다. 

</details>

[정의 1](#df1)에서 우리는 $G$의 연산이 더하기라는 것을 가정했지만, 사실 반드시 연산이 더하기일 필요는 없다. 만일 $G$의 연산이 곱하기로 적혀있더라도, $G$가 1번부터 4번까지의 모든 조건을 만족한다면 여전히 $G$는 abelian group이라 불린다. 물론, 이 경우에는 항등원을 $0$ 대신 $1$이라 쓰고, 역원을 $-a$ 대신 $a^{-1}$이라 쓰는 것이 자연스러울 것이다.

<div class="example" markdown="1">

<ins id="ex4">**예시 4**</ins> 실수집합 $\mathbb{R}$는 덧셈에 대하여 abelian group이며, 이는 복소수 집합 $\mathbb{C}$도 마찬가지다.  

$\mathbb{R}$과 $\mathbb{C}$ 위에는 곱셈도 정의되어 있지만, 이들은 곱셈에 대해서는 abelian group이 아니다. $0\in\mathbb{R}$ (혹은 $\mathbb{C}$)에 대하여, $0a=a0=1$을 만족하는 실수 (혹은 복소수) $a$가 존재하지 않기 때문이다. 그 대신, $\mathbb{R}^\times=\mathbb{R}\setminus\\{0\\}$ (혹은 $\mathbb{C}^\times=\mathbb{C}\setminus\\{0\\}$)은 곱셈에 대한 가환군이 된다.   

</div>

위의 예시와 같은 상황을 다음과 같이 정의한다.

<div class="definition" markdown="1">

<ins id="df5">**정의 5**</ins> 집합 $F$ 위에 두 개의 이항관계 $+$와 $\times$가 정의되었다 하자. $F$가 *field<sub>체</sub>*라는 것은 다음의 세 조건

1. $F$는 $+$에 대하여 abelian group이다.
2. $F^\times=F\setminus\\{0\\}$은 $\times$에 대하여 abelian group이다.
3. $\times$는 $+$에 대해 *분배법칙*을 만족한다. 즉, 임의의 $a,b,c\in F$에 대하여
    
    $$a\times (b+c)=(a\times b)+(a\times c)$$
    
    가 성립한다.
    
을 만족하는 것이다.

</div>

위의 정의에서 0과 1은 서로 다른 원소여야 한다. $1\in F^\times=F\setminus\\{0\\}$이기 때문이다. 

우리는 고등학교 때부터 $\times$라는 굳이 연산을 명시하기보다는 $a\cdot b$와 같이 줄여쓰는 것을 선호하고, 사실은 그냥 연산을 생략하고 $ab$로 쓰는 것을 더 선호한다. 앞으로는 이 관습을 따라 $a\times b$ 대신 $ab$로 적기로 한다.

한편 [명제 2](#pp2)를 $F$와 $F^\times$에 각각 적용하면

1. $0$과 $1$은 유일하다.
2. 임의의 $a\in F$에 대해 $-a$는 유일하고, 또 만일 $a\neq 0$이라면 $a^{-1}$도 유일하게 존재한다.
3. 만일 $a+b=a+c$라면 $b=c$이다. 또, 만일 $a\neq 0$이고, $ab=ac$라면 $b=c$이다.

가 성립한다는 것도 쉽게 확인할 수 있다.

<div class="proposition" markdown="1">

<ins id="pp5">**명제 5**</ins> 체 $F$의 임의의 원소 $a\in F$에 대하여, $0a=0$이고, $(-1)a=-a$가 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 명제가 의미하는 것을 찬찬히 뜯어볼 필요가 있는데, $0a=0$이라는 것은 *$0$과 $a$를 곱하면 덧셈에 대한 항등원 $0$이 나온다*는 것이고, $(-1)a=-a$라는 것은 *$(-1)$과 $a$를 곱하면 $a$의 역원이 나온다*는 것이다.  
이를 위해선 [명제 2](#pp2) 직후에 몇몇 성질들을 증명했듯이, 역원과 항등원의 유일성을 이용하면 될 것 같다. 첫 번째 식을 증명하려면 $0a+b=b+0a=b$가 임의의 $b$에 대해 성립한다는 것을 보여야 하는데, $0a+b$를 단순하게 표현할만한 방법이 보이질 않는다. 뭔가 다른 방법을 찾아야 한다.  
[명제 2](#pp2)의 셋째 명제를 활용하자. 만일 우리가 $0a+0a=0a$라는 것만 보이면, $0a=0a+0$이므로, $0a+0a=0a+0$에서 $0a=0$이 된다. 따라서 $0a+0a=0a$라는 것만 보이면 되는데, 이는

$$0a+0a=(0+0)a=0a$$

으로부터 자명하다. 이것만 증명하면 둘째 부분은 더 쉽다. $(-1)a$가 $a$의 역원의 조건을 만족한다는 것을 보이면 되는데,
mx ke
$$(-1)a+a=(-1)a+1a=((-1)+1)a=0a=0$$

이므로 증명 끝.

</details>

## 벡터공간의 정의

맨 처음에 이야기했던 것처럼, 우리가 정의하려 하는 *벡터공간*은 좌표평면이나 좌표공간 등을 일반화하는 개념이다. 곰곰이 생각해보면, 이들의 원소인 *벡터*들은 (영벡터를 항등원으로 갖는) 가환군 구조를 이뤘다. 벡터들 사이의 자연스러운 곱셈을 정의하는 방법이 있지는 않았으므로, 이들은 당연히 체가 아니다.[^1] 하지만 우리가 *스칼라*라 불렀던 $\mathbb{R}$의 원소들은 [예시 3](#ex3)에서 살펴봤듯 체를 이루며, 사실 이것이 우리가 체를 정의한 유일한 이유이다. 벡터공간이라는 것은 새로운 방법으로 정의해야 한다.

<div class="definition" markdown="1">

<ins id="df6">**정의 6**</ins> $F$가 체이고, $V$가 가환군이라 하자. $V$가 *$F$에 대한 벡터공간*, 혹은 간단히 *$F$-벡터공간*이라는 것은 여기에 추가적인 연산 (*스칼라곱*) $\cdot:F\times V\rightarrow V$가 존재하여 

1. 임의의 $\alpha,\beta\in F$와 임의의 $u\in C$에 대하여 $\alpha\cdot(\beta\cdot u)=(\alpha\beta)\cdot u$가 성립한다.
2. 임의의 $\alpha\in F$와 임의의 $u,v\in V$에 대하여 $\alpha\cdot(u+\_Vv)=(\alpha\cdot u)+\_V(\alpha\cdot v)$가 성립한다.
3. 임의의 $\alpha,\beta\in F$와 임의의 $u\in V$에 대하여 $(\alpha+\_F\beta)\cdot u=(\alpha\cdot u)+\_V(\beta\cdot u)$가 성립한다.  
4. 곱셈에 대한 $F$의 항등원 $1\in F$에 대하여, $1\cdot u=u$가 임의의 $u\in V$에 대하여 성립한다.

가 모두 만족되는 것이다.
</div>

위의 정의와 같이, 앞으로는 혼동을 피하기 위해 체의 원소는 모두 그리스 소문자 $\alpha,\beta,\ldots$으로 적고, 벡터공간의 원소들은 $u,v,\ldots$와 같은 로마자 소문자로 적기로 한다.  
우리는 위의 정의에서 $+\_V$와 $+\_F$를 구별하여 적었는데, 방금 만든 표기법을 도입하면 $+$ 주위에 있는 원소가 $F$의 원소인지, $V$의 원소인지가 명확하게 구별되므로 약간의 abuse of notation을 통해 이들을 모두 $+$로만 적어도 혼동의 여지가 없다.  
이는 스칼라곱도 마찬가지인데, 위의 정의에서는 $\alpha\cdot u$와 같이 스칼라곱을 명시적으로 적어두었지만 앞으로는 $\alpha u$와 같이 적기로 한다. 그리스 소문자와 로마자 소문자가 이렇게 조합되어 있다면 이건 스칼라곱을 나타내는 말일 것이고, 그리스 소문자 두 개가 조합되어 있다면 체에서의 곱셈을 나타내는 말일 것이다. 유일한 걱정은 $\alpha\beta u$라고 쓸 경우, 이것이 $(\alpha\beta)u$인지, $\alpha(\beta u)$인지 헷갈릴 수 있다는 것인데, 이는 위 정의의 1번 조건에 의해 어떤 것을 선택하더라도 그 값은 동일하므로 걱정할 문제가 아니다.  

벡터공간은 가환군 $V$ 위에 체 $F$가 스칼라곱을 통해 간섭하고 있는 구조로 정의되었기 때문에, 기본적으로 $V$는 더하기에 대한 가환군 구조를 모두 갖는다. 예를 들어, $V$의 항등원은 유일하고, ... 등등. 따라서 $V$가 가질 수 있는 (가환군의 성질이 아닌) 추가적인 성질은 오로지 스칼라곱에서만 나온다. 이는 체가 가질 수 있는 성질이 곱하기에서만 나오는 것과 거의 유사하다. 

<div class="proposition" markdown="1">

<ins id="pp7">**명제 7**</ins> $F$-벡터공간 $V$가 주어졌다 하자. 그럼

1. 임의의 $\alpha\in F$에 대하여, $\alpha0=0$이고,
2. 임의의 $v\in V$에 대하여, $0v=0$이다.

거꾸로, 만일 $\alpha v=0$이라면, $\alpha=0$이거나 $v=0$이 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

처음 두 주장은 [명제 5](#pp5)와 비슷하게 진행하면 된다. 예를 들어, 

$$\alpha0+\alpha0=\alpha(0+0)=\alpha0$$

이므로 $\alpha0=0$이고, 이와 비슷하게

$$0v+0v=(0+0)v=0v$$

이므로 $0v=0$이다. 마지막으로, $\alpha v=0$이고 $\alpha\neq 0$이라 하자. 만일 $\alpha\neq 0$이라면, $\alpha^{-1}\in F$가 존재하여 $\alpha\alpha^{-1}=1$이고, 따라서

$$v=1v=(\alpha^{-1}\alpha)v=\alpha^{-1}(\alpha v)=\alpha^{-1}0=0$$

이므로, $v=0$이 되어 주어진 명제가 성립한다.

</details>

이 명제가 예쁜 동치관계 형태로 적히게 하기 위해서 생략했지만, $V$에서도 역원은 유일하므로 [명제 5](#pp5)의 두 번째 결론도 성립한다. 즉, $-1\in F$와, 임의의 $v\in V$에 대해 $(-1)v=-v$가 성립한다.

## 벡터공간의 예시들

이제 벡터공간의 몇 가지 예시를 살펴보자.

<div class="example" markdown="1">

<ins id="ex8">**예시 8**</ins> 가장 간단한 벡터공간의 예시는 $\\{0\\}$이다. 이 집합에 더하기 구조를 줄 수 있는 방법은 하나 뿐이고 (즉 $0+0=0$), 이 구조 하에서 이 집합은 가환군 고조를 갖는다. 뿐만 아니라, 어떤 체 $F$를 가져오더라도 이 집합에 스칼라곱을 정의할 수 있는 방법 또한 하나 뿐이며 (즉 $\alpha 0=0$), 이렇게 정의된 스칼라곱은 $\\{0\\}$를 $F$-벡터공간으로 만든다. 이를 *자명한 벡터공간*이라 부른다.

조금 덜 자명한 예시는 체 그 자체다. 임의의 체 $F$에 대하여, $F$는 $F$-벡터공간이다. $F$는 체이므로, 덧셈에 대해 가환군이 된다는 것은 자명하다. 여기에 스칼라곱 구조만 주면 충분한데, 이는 그냥 $F$에서의 곱하기 $F\times F\rightarrow F$로 주면 된다. 이렇게 정의하면 스칼라곱이 [정의 6](#df6)의 조건들을 모두 만족한다는 것을 확인할 수 있고, 따라서 $F$는 그 자체로 $F$-벡터공간이다. 

또, $F$가 체이고, 다른 어떤 체 $K$가 존재하여 $K\supset F$라 하자. (대표적인 예시로는 $\mathbb{C}\supset\mathbb{R}$이나, $\mathbb{R}\supset\mathbb{Q}$과 같은 상황이 있다.) 그럼 $K$는 $F$-벡터공간이 된다. $K$는 체이므로, 아까 전과 같이 덧셈에 대해 가환군 구조가 있으며, $F$의 원소와의 스칼라곱은 (어차피 $F$의 모든 원소는 $K$의 원소이므로) 위와 같이 $K$의 곱셈 구조를 사용하면 된다. 

</div>

<div class="example" markdown="1">

<ins id="ex9">**예시 9**</ins> 더 일반적으로, 체 $F$가 주어졌다고 하자. 그럼 *유클리드 $n$차원 공간*은 다음의 $n$-순서쌍

$$\begin{pmatrix}a_1\\a_2\\\vdots\\a_n\end{pmatrix},\qquad a_i\in F\text{ for all $i$}$$

들로 이루어진 $F$-벡터공간이다. 이들 사이의 덧셈과 스칼라곱은 각각

$$\begin{pmatrix}a_1\\a_2\\\vdots\\a_n\end{pmatrix}+\begin{pmatrix}b_1\\b_2\\\vdots\\b_n\end{pmatrix}=\begin{pmatrix}a_1+b_1\\a_2+b_2\\\vdots\\a_n+b_n\end{pmatrix},\qquad \alpha\begin{pmatrix}a_1\\a_2\\\vdots\\a_n\end{pmatrix}=\begin{pmatrix}\alpha a_1\\\alpha a_2\\\vdots\\\alpha a_n\end{pmatrix}$$

으로 정의된다. $F=\mathbb{R}$이고 $n=2,3$일 경우, 이 정의는 우리가 잘 아는 좌표평면과 좌표공간이 된다. 이런 의미에서 벡터공간이 좌표평면, 좌표공간의 일반화라는 도입부의 motivation이 설명된다. 

</div>

유클리드 공간는 우리가 특히 많이 다룰 대상이다. 고등학교 때와는 다르게, 우리는 순서쌍 $(a\_1, a\_2, \ldots, a\_n)$이라는 표기법 대신 열로 이루어진 표기법을 사용하고 있는데, 이건 충분히 그럴만한 이유가 있다. 하지만 아무리 그럴듯한 이유가 있더라도, 이 표기법을 $\begin{pmatrix}a\_1\\\a\_2\\\\\vdots\\\a\_n\end{pmatrix}$ 과 같이 본문에서 고집하는 것도 어리석은 일이다. 따라서 본문 중에서는 $(a\_1\;a\_2\;\cdots\;a\_n)^t$와 같은 표기법[^2] 혹은, 고등학교 때의 표기법을 따라 $(a\_1,a\_2,\ldots, a\_n)$와 같이 쓰기로 한다.

위에서 살펴본 두 개의 벡터공간들은 상당히 구체적인 예시에 속한다. 일반적으로 벡터공간은 시각적으로 표현될 필요가 전혀 없다.[^3]

<div class="example" markdown="1">

<ins id="ex10">**예시 10**</ins> $I$가 어떤 구간이라 하고, $I$에서 $\mathbb{R}$로의 함수들의 모임 $\operatorname{Fun}(I,\mathbb{R})$을 생각하자. 이제 이 집합 위에, 덧셈과 스칼라곱을 다음의 식

$$f+g:t\mapsto f(t)+g(t),\qquad \alpha f:t\mapsto \alpha f(t)$$

으로 정의하면 $\operatorname{Fun}(I,\mathbb{R})$이 벡터공간 구조를 갖는 것을 확인할 수 있다. 즉, $f+g$는 임의의 $t\in I$를 $f(t)+g(t)$라는 값으로 보내는 함수로, $\alpha f$는 임의의 $t\in I$를 $\alpha f(t)$로 보내는 함수로 정의된다. 

뿐만 아니라, $\operatorname{Fun}(I,\mathbb{R})$의 여러 부분집합들도 $\mathbb{R}$-벡터공간이 된다. 예를 들어, $I$에서 $\mathbb{R}$로의 연속함수들의 모임 $C(I)$ 또한 $\mathbb{R}$-벡터공간이고, 더 일반적으로 $k$번째 도함수가 연속인 함수들의 모임 $C^k(I)$들의 모임도 $\mathbb{R}$-벡터공간이 된다는 것을 확인할 수 있다.

</div>

## 부분공간

앞선 [예시 10](#ex10)을 보면, 어떤 벡터공간의 부분집합이 그 자체로 벡터공간을 이루는 경우가 종종 있다는 것을 알 수 있다. 이를 다음과 같이 정의하자.

<div class="definition" markdown="1">

<ins id="df11">**정의 11**</ins> 어떤 $F$-벡터공간 $V$에 대하여, $V$의 부분집합 $W$가 $V$의 *부분공간*이라는 것은, $V$ 위에 정의된 덧셈과 스칼라곱을 $W$ 위로 제한하였을 때 얻어지는 연산들이 $W$ 위에 다시 $F$-벡터공간을 정의하는 것이다. 이를 $W\leq V$와 같이 표현한다.

</div>

정의에 의해, $C^k(I)$는 $C(I)$의 부분공간이고, $C(I)$는 $\operatorname{Fun}(I,\mathbb{R})$의 부분공간이 된다.

정의를 문자 그대로 받아들이자면, $V$의 임의의 부분집합 $W$가 부분공간인지를 체크하기 위해서는 이들의 덧셈이 가환군을 이루는지, 그리고 스칼라곱이 [정의 6](#df6)의 조건을 모두 만족하는지 등을 모두 따져봐야 한다. 하지만, $W$ 위에 정의될 덧셈과 스칼라곱은 $V$로부터 받아오는 것이므로, 몇 가지 성질들은 굳이 체크할 필요가 없다. 예를 들어, 임의의 $w\_1,w\_2\in W$에 대해

$$w_1+w_2=w_2+w_1$$

이 성립하는지는 굳이 따져볼 필요가 없다. 왜냐하면, $w\_1,w\_2$는 $W$의 원소이기 이전에 $V$의 원소이기도 하고, $V$의 덧셈은 위 식을 항상 만족하는데, 위 식에서 정의된 $W$에서의 덧셈 $+$는 바로 그 $V$에서의 덧셈을 $W$로 제한한 것이기 때문이다. 이를 바탕으로 우리가 체크해봐야 할 성질들을 따져보면 다음과 같다.

1. $W$가 덧셈에 대해 닫혀있는지의 여부는 따로 체크해봐야 한다. 왜냐하면, $V$에서 덧셈이 닫혀있다는 것은 $w\_1+w\_2\in V$라는 것만 보장하지, $w\_1+w\_2\in W$라는 것은 보장해주지 않기 때문이다.
2. 이와 비슷하게, $V$가 덧셈에 대한 항등원과 역원을 갖는지도 체크해봐야 한다. 물론 $V$는 $0$과 $-w$를 포함하지만, 이들이 $W$에 포함되리라는 보장은 없기 때문이다.
3. 또, 임의의 스칼라 $\alpha\in F$와 $w\in W$에 대하여, $\alpha w\in W$인지의 여부도 체크해봐야 한다.

하지만 여기에서 조금 더 조건을 간추릴 수도 있다. 만일 $W$가 스칼라곱에 대해 닫혀있기만 하다면, [명제 7](#pp7), 그리고 그 후에 적어둔 remark에 의해 2번 조건은 통째로 생략할 수 있다. $W$가 스칼라곱에 대해 닫혀있으므로, $0w\in W$이고 $(-1)w\in W$여야 하는데, 이들이 각각 $0$과 $-w$이기 때문이다. 따라서 방금 우리는 다음 명제를 증명했다.

<div class="proposition" markdown="1">

<ins id="pp12">**명제 12**</ins> $F$-벡터공간 $V$에 대하여, $V$의 공집합이 아닌 부분집합 $W$가 $V$의 부분공간인 것은, $W$가 덧셈과 스칼라곱에 대해 닫혀있는 것과 동치이다.

</div>

하지만 보편적으로, $W$가 공집합이 아닌 것을 보이기 위해서는 $0\in W$임을 보이는 것이 가장 쉽기 때문에 위 성질 1번부터 3번 (에서 2번의 역원 조건을 제외한 것)은 여전히 유효하다. 다른 이야기를 더 진행하기 전에, 편리한 표기법을 하나 도입하자.

<div class="definition" markdown="1">

<ins id="df13">**정의 13**</ins> $F$-벡터공간 $V$가 주어졌다고 하자. $V$의 원소들의 family $(v\_i)\_{i\in I}$에 대하여, 이들의 *일차결합*은

$$\sum_{i\in I}\alpha_i v_i$$

의 꼴로 나타나는 벡터이다. 여기에서, $(\alpha\_i)\_{i\in I}$들은 스칼라들의 *finitely supported* family이다. 즉, $(\alpha\_i)\_{i\in I}$ 모든 $i$에 대해 $\alpha\_i\in F$이고 다음의 집합

$$\operatorname{supp}(\alpha_i)_{i\in I}=\{i\in I:\alpha_i\neq 0\}$$

이 유한집합인 family이다.

</div>

사실, 임의의 family의 일차결합은 항상

$$\sum_{v\in V}\alpha_vv$$

으로 둘 수 있으므로 이것만 정의해도 충분했겠지만, 이렇게까지 하는 건 좀 과하고, 앞으로 보통은 $I$가 특정한 부분공간 혹은 기저 등등이 될 때 이 표기를 사용하게 된다. 

특히 $(\alpha\_i)\_{i\in I}$가 finitely supported라는 조건을 신경쓸 필요가 있다. 위의 정의를 찬찬히 살펴보면, 우리는 사실 $\sum\_i\alpha\_iv\_i$가 벡터라고 선언만 했지, 실제로 이게 벡터라는 근거는 따로 부연설명을 하지 않았다. 우리는 임의의 자연수 $n$에 대하여, 다음의 식

$$\sum_{i=1}^n \alpha_iv_i=\alpha_1v_1+\alpha_2v_2+\cdots+\alpha_nv_n$$

이 벡터가 된다는 것을 쉽게 증명할 수 있다. 그러나 이것이 다음의 *무한합*

$$\sum_{i=1}^\infty \alpha_iv_i=\alpha_1v_1+\alpha_2v_2+\cdots$$

이 벡터라는 것을 보장하는 것은 당연히 아니다.[^4] 예를 들어, 우리는 [예시 8](#ex8)에서 $\mathbb{R}$ 자체가 $\mathbb{R}$-벡터공간이라는 것을 보였는데, 여기에서

$$\sum_{i=1}^\infty1=1+1+\cdots$$

은 $\mathbb{R}$의 원소가 아니다. 따라서, 앞으로 우리가 $\sum\_{i\in I}\alpha\_iv\_i$와 같은 표현을 사용할 때에는 말하지 않더라도 $(\alpha\_i)\_{i\in I}$가 finitely supported임을 전제하기로 한다. 이 표기법을 처음 보면 그냥 유한합을 사용하면 될 걸 굳이 복잡한 표기법을 도입했나 싶지만, 특히 초반부에는 이 표기법이 많은 일들을 간단하게 만들어준다. 다음을 먼저 증명하자.

<div class="proposition" markdown="1">

<ins id="lem14">**보조정리 14**</ins> 체 $F$의 원소들로 이루어진 두 family $(a\_i)\_{i\in I}$, $(b\_i)\_{i\in I}$를 생각하자. 

$$\operatorname{supp}(a_i)_{i\in I}=A,\qquad \operatorname{supp}(b_i)_{i\in I}=B$$

라 하면, 

$$\operatorname{supp} (a_ib_i)_{i\in I}=A\cap B,\qquad \operatorname{supp}(a_i+b_i)_{i\in I}\subset A\cup B$$

가 성립한다. 둘째 식은 $(a_i)$와 $(b_i)$들이 체의 원소가 아니라, 덧셈 구조가 있는 가환군의 원소여도 성립한다.

특히, 만일 $(a\_i)\_{i\in I}$, $(b\_i)\_{i\in I}$ 각각이 finitely supported라면 $(a\_i+b\_i)\_{i\in I}$ 또한 finitely supported이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

둘째 식은 한 방향만 보이면 되므로, 이것부터 보이자. 어떤 $i\in\operatorname{supp}(a\_i+b\_i)\_{i\in I}$가 주어졌다 하자. 그럼 $a\_i+b\_i\neq 0$이므로, $a\_i\neq 0$이거나 $b\_i\neq 0$이다. 따라서 $i\in A$ 혹은 $i\in B$이므로, 원하는 명제가 성립한다.

첫째 식을 보여야 한다. 위와 마찬가지로, 어떤 $i\in\operatorname{supp}(a\_ib\_i)\_{i\in I}$가 주어졌다 하자. 그럼 $a\_ib\_i\neq 0$이고, 따라서 $a\_i\neq 0$이고 $b\_i\neq 0$이므로 $i\in A$이고 $i\in B$가 되어 $i\in A\cap B$이다. 반대로, 만일 $i\in A\cap B$라면, 이 논리를 거꾸로 하면 $a\_ib\_i\neq 0$이 되므로 $i\in\operatorname{supp}(a\_ib\_i)\_{i\in I}$가 되어 증명 끝.

</details>

사실 우리가 벡터들 사이의 곱셈을 정의할 일은 거의 없으므로, 첫 번째 식은 별로 크게 쓸모가 있지는 않지만, 둘째 식은 종종 사용하게 된다.

<div class="example" markdown="1">

<ins id="ex15">**예시 15**</ins> 집합 $F[\mathrm{x}]$를 

> $F$의 원소를 계수로 갖는 $\mathrm{x}$에 대한 다항식들의 집합

으로 정의하자. 즉, $F[\mathrm{x}]$의 각각의 원소들은 적당한 $a\_i\in F$들에 대해[^5]

$$p(\mathrm{x})=a_n\mathrm{x}^n+a_{n-1}\mathrm{x}^{n-1}+\cdots+a_1\mathrm{x}+a_0$$

의 꼴이다. 바꿔 말하자면, $F[\mathrm{x}]$는 *finitely supported* family $(a\_i)\_{i=0}^\infty$에 대하여, 

$$p(\mathrm{x})=\sum_{i=0}^\infty a_i\mathrm{x}^i$$

라 할 수 있다. 우리는 이 때, $\max\operatorname{supp}(a\_i)=n$을 $p(\mathrm{x})$의 *차수*라 부른다. 최고차항의 계수가 1인 다항식은 *monic polynomial*이라 부른다. 

이제 또 다른 $F[\mathrm{x}]$의 원소 $q(\mathrm{x})=\sum b_i\mathrm{x}^i$에 대하여, 

$$p(\mathrm{x})+q(\mathrm{x})=\sum_{i=0}^\infty (a_i+b_i)\mathrm{x}^i$$

으로 정의하고, 임의의 스칼라 $\alpha\in F$에 대하여

$$\alpha p(\mathrm{x})=\sum_{i=0}^\infty(\alpha a_i)\mathrm{x}^i$$

으로 정의한다면, 앞선 [보조정리 14](#lem14)에 의해 $(a\_i+b\_i)\_{i=0}^\infty$와 $(\alpha a\_i)\_{i=0}^\infty$는 모두 finitely supported이고, 따라서 $p(\mathrm{x})+q(\mathrm{x})$와 $\alpha p(\mathrm{x})$는 각각 $F[\mathrm{x}]$의 원소가 된다. 어렵지 않게 이들 정의를 통해 $F[\mathrm{x}]$가 $F$-벡터공간 구조를 가진다는 것을 확인할 수 있다.

그럼, 어렵지 않게 $n$차 이하의 차수를 갖는 다항식들의 집합 $F^{(n)}[\mathrm{x}]$는 $F[\mathrm{x}]$의 부분공간이라는 것을 확인할 수 있다. 반면, *정확히* 차수 $n$을 갖는 다항식들의 집합은 덧셈에 대해 닫혀있지 않고 (예컨대 $\mathrm{x}^n+(-\mathrm{x}^n+1)=1$), 따라서 부분공간이 아니다. 
</div>

만약 우리가 [정의 13](#df13)의 표기법 대신 유한합만 생각했다면, 예를 들어 위에서 $p(\mathrm{x})+q(\mathrm{x})$를 정의할 떄, 

> 만약 $m>n$이라면,  
>
> $$\sum_{i=0}^na_i\mathrm{x}^i+\sum_{i=0}^mb_i\mathrm{x}^i=\sum_{i=0}^m c_i\mathrm{x}^i,\qquad c_i=\begin{cases}a_i+b_i&\text{if $0\leq i\leq n$}\\ b_i&\text{if $n<i\leq m$}\end{cases}$$
>
> 그리고 반대의 경우
>
> $$\sum_{i=0}^na_i\mathrm{x}^i+\sum_{i=0}^mb_i\mathrm{x}^i=\sum_{i=0}^m c_i'\mathrm{x}^i,\qquad c_i'=\begin{cases}a_i+\beta_i&\text{if $0\leq i\leq m$}\\ a_i&\text{if $m<i\leq n$}\end{cases}.$$

와 같은 복잡한 정의가 필요했을 것이다.

다음 예시는 우리가 앞서 정의한 일차결합의 정의와 살짝 어긋나는 듯 하여 혼란이 올 수 있지만...

<div class="example" markdown="1">

<ins id="ex16">**예시 16**</ins> 이번에는 집합 $F[[\mathrm{x}]]$를 

>$F$의 원소를 계수로 갖는 $\mathrm{x}$에 대한 formal power series들의 집합

이라 하자. 즉, 이번에도 $F[[\mathrm{x}]]$의 원소들은 모두

$$p(\mathrm{x})=\sum_{i=0}^\infty a_i\mathrm{x}^i$$

의 꼴이지만, 이번에는 $(a\_i)\_{i=0}^\infty$가 finitely supported라는 가정이 없다. 앞선 [예시 15](#ex15)와 동일한 방식으로 벡터 사이의 덧셈과 스칼라곱을 정의하면, $F[[\mathrm{x}]]$는 마찬가지로 $F$-벡터공간이 된다.  

</div>

$F[[\mathrm{x}]]$도 $F$-벡터공간이지만, 앞선 $F[\mathrm{x}]$와는 상황이 꽤 다르다. 이 차이점은 우리가 지금까지 정의한 개념들만으로도 설명할 수 있는데, 이는 $F[[\mathrm{x}]]$의 원소를 살펴보면 우리가 앞서 정의한 일차결합의 개념으로 잘 설명되지 않는 부분이 있다는 것이다. 

물론, 그렇다고 해서 이것이 $F[[\mathrm{x}]]$가 벡터공간이라는 주장에 끼치는 영향은 전혀 없다. 앞서 예로 들었던 $\mathbb{R}$-벡터공간 $\mathbb{R}$의 경우, 무한합

$$\sum_{i=0}^\infty 1=1+1+\cdots$$

은 $\mathbb{R}$의 원소가 아니지만, 예를 들어 무한합

$$\sum_{i=0}^\infty \frac{\left\lfloor\pi\cdot10^i\right\rfloor}{10^i}=3\cdot 1+1\cdot\frac{1}{10}+4\cdot\frac{1}{10^2}+\cdots$$

은 $\mathbb{R}$의 원소이다. 우리가 무한합이라는 개념을 피하는 것은 어떠한 (그리고 대부분의) 무한합이 정의되지 않을 수도 있기 때문이지, 무한합이 항상 정의되지 않아서가 아니다. 즉, 임의의 $F$-벡터공간 $V$에 대해 어떤 무한합

$$\sum_{i=0}^\infty \alpha_iv_i$$

이 $V$의 원소가 되지 않을 이유는 없다. 다만 ($\operatorname{supp}(a_i)$가 finitely supported가 아닌 이상은) 이를 일차결합이라 부르지 않는 것 뿐이다. 같은 이유로, 우리는 $F[[\mathrm{x}]]$의 원소 

$$p(\mathrm{x})=\sum_{i=0}^\infty a_i\mathrm{x}^i, \qquad\lvert\operatorname{supp}(a_i)\rvert=\infty$$

를 집합 $\\{1,\mathrm{x},\mathrm{x}^2,\ldots\\}$의 원소들의 일차결합이라 부르지는 *않지만*, 그럼에도 불구하고 이 원소는 $F[[\mathrm{x}]]$의 원소이긴 한 것이다. 그리고 사실, 모든 무한합이 $F[[\mathrm{x}]]$의 원소인 것도 아니다. 예를 들어, $i=1,2,\ldots$에 대하여 $p_i(\mathrm{x})=\mathrm{x}$라 하면

$$\sum_{i=0}^\infty p_i(\mathrm{x})\not\in F[[\mathrm{x}]]$$

이다. 반면, $F[\mathrm{x}]$의 임의의 원소는 집합 $\\{1,\mathrm{x},\mathrm{x}^2,\ldots\\}$의 원소들의 일차결합으로 나타낼 수 있다. 

우리는 임의의 다항식이나, 더 일반적으로 formal power series의 곱셈 또한 할 수 있으므로 사실 위의 두 예시는 $F[\mathrm{x}]$나 $F[[\mathrm{x}]]$를 완전하게 설명해주지는 않는다. 이 구조는 대수학을 하며 나오는데, 아주 간단하게 말해서 $F$-벡터공간 위에 추가적으로 각 벡터들 간의 곱셈이 정의된 구조를 *$F$-algebra*라고 부른다. 위 두 경우, 사실은 스칼라곱은 (상수 다항식과의 곱하기로 생각하면) 별 의미가 없으므로, 스칼라곱을 빼고, 벡터들 간의 곱하기와 더하기만 생각하기도 하며, 이러한 관점에서 둘은 *ring*이라 부르기도 한다.  

마지막으로 우리는 다음의 명제를 하나 증명하기로 한다.

<div class="proposition" markdown="1">

<ins id="pp17">**명제 17**</ins> $F$-벡터공간 $V$와, $W\leq V$가 주어졌다 하자. 그럼 $W$의 원소들의 임의의 일차결합은 $W$에 속해 있다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선, $W$의 원소들의 임의의 일차결합은 다음의 식

$$\sum_{w\in W}\alpha_w w,\qquad\text{$(\alpha_w)_{w\in W}$ finitely supported}$$

으로 쓸 수 있다. 우리는 이 원소가 $W$에 속한다는 것을 보여야 한다. $\lvert\operatorname{supp}(\alpha_w)\rvert$에 대한 induction으로 진행한다. $\lvert\operatorname{supp}(\alpha_w)\rvert=1$인 경우, 위의 식은 그냥 적당한 $w\in W$와 $\alpha\in F$에 대해 $\alpha w$가 되므로, [명제 12](#pp12)에 의해 이 원소는 $W$에 속한다.

이제 $\lvert\operatorname{supp}(\alpha_w)\rvert<n$인 모든 $(\alpha_w)$에 대해 위의 원소가 $W$에 속한다 가정하고, $\lvert\operatorname{supp}(\beta_w)\rvert=n$인 $(\beta_w)$가 주어졌다 하자. $w_0\in\operatorname{supp}(\beta_w)$인 $w_0$에 대하여, 

$$\sum_{w\in W}\beta_ww=\beta_{w_0}w_0+\sum_{w\in W\setminus\{w_0\}}\beta_ww$$

이고, $\lvert\operatorname{supp}(\beta\_w)\_{w\in W\setminus\\{w\_0\\}}\rvert=n-1$이므로 inductive hypothesis에 의하여 뒤쪽 term은 $W$의 원소이다. 한편, $\beta\_{w\_0}w_0$은 $n=1$인 경우에 의해 $W$의 원소이므로, 다시 [명제 12](#pp12)에 의하여 이들의 합인 $\sum\_{w\in W}\beta_ww$ 또한 $W$의 원소이다. 

</details>



---
**Reference**

**[Goc]** M.S. Gockenbach, *Finite-dimensional linear algebra*, Discrete Mathematics and its applications, Taylor&Francis, 2011.

---

[^1]: 예컨대, 벡터들의 내적은 벡터 두 개를 받은 후, 벡터 대신 실수값을 내놓으므로 곱셈으로 볼 수 없다. 두 벡터를 외적하면 새로운 벡터가 나오긴 하는데, $u\times v$와 $v\times u$가 서로 다른 벡터 (반대방향의 벡터)를 내놓으므로 commutative하지 않고, 따라서 체가 아니다. 
[^2]: 이 표기법의 의미 또한 나중에 알게 된다.
[^3]: 하지만, $\operatorname{Fun}(I,\mathbb{R})$을 product set $\mathbb{R}^I$라 생각하면 [예시 10](#ex10)은 [예시 9](#ex9)의 자연스러운 일반화로 볼 수도 있다. ([Set Theory, §집합의 연산, 정의 18](/ko/note/set_theory/set_operations#df18))
[^4]: 사실 이건 당연한 얘기다. 두 다항식의 합이 다항식이라 해서 $e^x=\sum x^n/n!$도 다항식인 것은 아니다.
[^5]: $F$의 원소들을 그리스 소문자로 쓰기로 하긴 했었지만, 지금 상황에서 다항식의 계수들을 그리스 소문자로 쓰는 것도 좀 어색하므로... 
