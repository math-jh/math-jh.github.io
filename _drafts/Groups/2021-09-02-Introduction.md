---

title: "대수적 구조"
excerpt: "Semigroups, monoids, and groups"

categories: [Math / Groups]
permalink: /ko/math/groups/introduction
header:
    overlay_image: /assets/images/Groups/Introduction.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_structures"

date: 2021-09-02
last_modified_at:
weight: 1

published: false

---
<div class="notice--warning" markdown="1">

이 글은 현재 수정중입니다.

이 글은 예전에 쓴 글로, 서술 방향이 마음에 들지 않거나 표기법이 마음에 들지 않아 전체적으로 수정이 진행중입니다. 읽으실 때 참고해주세요.

</div>

## 이항연산

선형대수 때 배우는 벡터공간을 제외하면 학부 때 처음 접하게 되는 대수적인 구조는 군이다. 여기에서 *대수적인 구조*라는 것은 보편적으로 어떤 집합 위에 하나 이상의 이항연산이 주어진 것을 의미한다. 

[집합론](/set_theory)을 하며 우리가 사용한 **[Bou]**는 단순한 집합론의 내용보다는, 이 집합 위에 이항연산들을 하나씩 얹어가며 대수적인 이야기를 하기 좋게 설계되어 있다. 따라서, 우리는 이 내용을 적극 활용해가며 이야기를 전개할 것이다. 이 흐름은 일반적인 교재로 따지면 **[Hun]**과 비슷하다고 할 수 있다. 

어쨌든 이야기를 시작하기 위해서는 이항연산이 무엇인지부터 정의해야 한다.

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> 집합 $A$에 대하여, $E\times E$에서 $E$로의 함수 $\ast$를 *이항연산*이라 부른다.  이항연산이 주어져 있는 집합을 *마그마*라 부른다.[^1]

</div>

이러한 $\ast$의 함수값 $\ast(x,y)$를 종종 $x\ast y$로 줄여쓴다. 물론 이항연산을 나타내는 기호는 $\star$나 $\diamond$, $\odot$ 등등, 아무거나 택할 수 있다. 물론 이들 중 가장 보편적인 기호는 $+$와 $\times$이며, 미지수를 처음 배웠을 때부터 사용한 convention을 따라 $x\times y$는 $x\cdot y$, 혹은 더 간단하게 $xy$로 줄여서 쓰기도 한다. 

앞서 이야기했듯 기호의 선택은 전적으로 우리 맘이다. 예를 들어, 자연수 집합 $\mathbb{N}$에서, $1\star 1=2$, $1\star 2=3$, 등의 값을 갖는 연산 $\star$를 $+$ 대신 $\times$로 표시한다고 해도 논리적으로 문제가 있지는 않지만 실제로 그런 표기법을 쓰는 사람은 아무도 없다. 우리는 이미 알고 있는 연산들은 사용하던 표기를 그대로 유지하되, 추상적인 연산들에 대해서는 표기를 곱하기로 고정하기로 한다. 항등원도 $1$로 표기하기로 약속할 수도 있지만, 항등원을 1로 표기하는 것이 적절하지 않은 경우도 종종 있으므로 추상적인 연산들에 대한 항등원은 $e$로 적기로 하자. 

물론 이렇게 표기를 곱하기로 고정한 후에는 $x\times y$보다는 $xy$와 같은 위의 표기를 적용할 것이다. 다만 이렇게 연산을 생략해버리면 처음 볼 때는 혼란스러울 수도 있으므로, 이번 글에서만은 연산을 $\star$로 통일하기로 하자.

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins> 당연한 이야기이지만, 어떤 집합 위에 주어진 마그마 구조는 유일하지 않다. 

예를 들어 임의의 집합 $X$에 대하여, $X$의 멱집합 $\mathcal{P}(X)$은 이 위에 정의된 연산 $\cup$과 함께라면 마그마 구조를 가지며, $\cap$에 대해서도 마찬가지다.  
또 다른 예시로, 자연수 집합 $\mathbb{N}^{>0}$ 위에서 $+$, $\times$가 주어져도 이들은 각각 마그마가 된다.

</div>

떄문에 "마그마 $\mathcal{P}(X)$", 혹은 "마그마 $\mathbb{N}^{>0}$" 등과 같은 표현보다는 $(\mathcal{P}(X),\cup)$, $(\mathcal{P}(X),\cap)$, $(\mathbb{N}^{>0},+)$, $(\mathbb{N}^{>0},\times)$ 등과 같이 연산을 explicit하게 적어주는 것이 좋은 표기법이다. 물론, 이러한 연산이 문맥에 따라 명확하다면 이 정도는 생략할 수 있다.

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> 이번에는, 자연수 집합 $\mathbb{N}^{>0}$ 위에 $\star$를 $x\star y=x^y$로 정의해보자. 당연히 이 또한 마그마가 된다. 혹은, $\mathbb{Z}$ 위에 정의된 $x-y$ 또한 마그마를 정의한다.

</div>

[예시 2](#ex2)와 [예시 3](#ex3) 사이에는 큰 차이가 있다. 임의의 $A,B,C\in\mathcal{P}(X)$는 다음의 식

$$A\cup(B\cup C)=(A\cup B)\cup C,\qquad A\cap(B\cap C)=(A\cap B)\cap C$$

를 만족하고, $\mathbb{N}^{>0}$ 위에서 정의된 $+$와 $\times$도 비슷한 성질을 갖지만 [예시 3](#ex3)의 연산들은 그렇지 않다. 예컨대 다음과 같은 식

$$4-1-2$$

이 주어졌다고 하면, 우리는 초등학교 때부터 배운 계산규칙에 따라 $4$에서 $1$을 빼서 $3$를 얻고, 다시 여기서 $2$를 빼서 $1$을 얻을 것이다. 하지만 연산 순서를 바꾸어 $1-2$를 먼저 계산하여 $-1$을 얻고, 이후 이 값을 4에서 뺀다면 그 값은 $5$가 된다. 이를 다음과 같이 정의한다.  

<div class="definition" markdown="1">

<ins id="df4">**정의 4**</ins> 어떤 마그마 $(A,\star)$에 대하여, 임의의 $x$, $y$, $z\in A$에 대해 다음의 식

$$x\star(y\star z)=(x\star y)\star z$$

가 항상 성립하다면, $\star$가 *결합법칙을 만족한다*고 하고, 마그마 $A$ 또한 결합법칙을 만족하는 마그마라 불린다.
</div>

만일 $\star$가 결합법칙을 만족한다면, $x\star y\star z$라고 적은 식은 어떻게 계산하든 간에 같은 값이 나올 수밖에 없으므로 이 표현 자체가 잘 정의된다. 하지만 $-$와 같은 경우는 이와 같은 연산이 잘 정의되지 않으므로 추가적인 관습, 예컨대 앞에서부터 계산한다는 관습이 필요했다[^1].

한편, [예시 2](#ex2)와 [예시 3](#ex3)은 또 다른 차이점이 있다. 앞의 예시에서는 항상 $x\star y=y\star x$였는데, 뒤의 예시에서는 $x\star y\neq y\star x$일 수 있다는 것이다.

<div class="definition" markdown="1">

<ins id="df5">**정의 5**</ins> 어떤 마그마 $(A, \star)$에 대하여, 만일 임의의 $x,y\in A$에 대해 다음의 식

$$x\star y=y\star x$$

가 항상 성립한다면, $\star$가 *교환법칙을 만족한다*고 하고, 마그마 $A$ 또한 교환법칙을 만족하는 마그마라 부른다.
</div>

<div class="example" markdown="1">

<ins id="ex6">**예시 6**</ins> 어쩌다보니 예시 2의 모든 예시들은 교환법칙과 결합법칙을 동시에 만족하고, 예시 3의 모든 예시들은 둘을 모두 만족하지 않지만 이 두 개의 개념은 전혀 관련이 없다.

우선 교환법칙을 만족하진 않지만 결합법칙을 만족하는 마그마의 예시가 존재한다. 임의의 집합 $E$에 대하여, $E$에서 $E$로의 함수들의 모임 $\operatorname{Fun}(E,E)$를 생각하자. 임의의 두 함수 $f,g\in\operatorname{Fun}(E,E)$에 대하여, 여기에서의 연산을 함수의 합성 $(f,g)\mapsto f\circ g$로 준다면 이는 결합법칙을 만족하지만 교환법칙은 만족하지 않는다.

또, 결합법칙을 만족하지 않지만 교환법칙은 만족하는 마그마의 예시도 존재한다. 유리수 집합 $\mathbb{Q}^{>0}$에서, $x\star y$를 $x$와 $y$의 평균으로 정의하면, 즉 $x\star y=(x+y)/2$라면 $\star$는 교환법칙은 만족하지만 결합법칙을 만족하지는 않다.

</div>

<div class="example" markdown="1">

<ins id="ex7">**예시 7**</ins> 마그마들의 family $(A_i, \star_i)_{i\in I}$를 생각하자. 곱집합 $\prod A_i$ 위에, 다음과 같은 연산

$$(x_i)_{i\in I}\star(y_i)_{i\in I}=(x_i\star_i y_i)_{i\in I}$$

을 주면 $\prod A_i$는 $\star$에 대해 마그마 구조를 갖는다. 이렇게 얻어지는 마그마 $(\prod A_i, \star)$를 *곱*이라고 부른다. 만일 $\star_i$들이 모두 교환법칙을 만족하거나, 모두 결합법칙을 만족한다면 $\star$ 또한 그렇다는 것을 쉽게 알 수 있다. 

</div>

## 준동형사상, 부분구조와 몫구조

앞서 언급한 것과 같이 집합론에서 우리 이야기의 흐름은 집합 위에 이항연산 등의 추가적인 구조가 생겼을 때도 잘 작동하도록 짜여져 있었다. 따라서 집합론때와 마찬가지로 큰 흐름을 따라가보자.

관계들 가운데 가장 처음 살펴본 것은 함수였다. 두 마그마들 $A$, $A'$가 주어져있다고 하자. $A$와 $A'$는 어쨌건 집합이므로, 임의의 함수 $f:A\rightarrow A'$는 집합으로써 두 마그마 사이의 함수를 정의한다. 하지만 마그마는 단순한 집합이 아니라 연산 또한 정의된 집합이므로, 다음과 같이 연산을 보존하는 함수만을 생각하는 것이 자연스럽다.

<div class="definition" markdown="1">

<ins id="df8">**정의 8**</ins> 두 마그마 $(A,\star)$, $(A',\star')$ 사이의 함수 $f:A\rightarrow A'$가 다음의 식

$$f(x\star y)=f(x)\star'f(y)$$

을 모든 $x$, $y\in A$에 대해 만족한다면, 이 함수 $f$를 *준동형사상*, 강조가 필요할 때는 *마그마 준동형사상*이라 부른다. 만약 또 다른 마그마 준동형사상 $g:A'\rightarrow A$가 존재하여 

$$g\circ f=\operatorname{id}_A,\qquad f\circ g=\operatorname{id}_{A'}$$

가 성립한다면, $f$와 $g$가 서로의 *역 준동형사상*이라 부르고, $f$와 $g$를 *동형사상*이라 부른다. 이 때, $A$와 $A'$는 *동형*이라고 부르고, 기호로 $A\cong A'$와 같이 표기한다.

</div>

대수학에서는 $f$의 image를 $f(A)$ 대신 $\operatorname{im}f$와 같이 적는 것이 보통이다. $\operatorname{im}f$는 자명하게 $A'$의 부분집합이다. 그런데, $A'$는 단순히 부분집합일 뿐만 아니라, $\operatorname{im}f$ 그 자체로도 마그마가 된다. 즉, $\operatorname{im}f$는 $\star'$에 대해 닫혀있다.  

임의의 $w,z\in\operatorname{im}f$를 택하자. 그럼 어떤 $x,y\in A$가 존재하여 $w=f(x)$이고, $z=f(y)$이다. 이제

$$w\star'z=f(x)\star'f(y)=f(x\star y)$$

이고, $x\star y\in A$이므로, $w\star'z\in\operatorname{im}f$가 성립한다.

이와 같이 연산에 대해 닫혀있는 마그마의 부분집합을 다음과 같이 정의한다.

<div class="definition" markdown="1">

<ins id="df9">**정의 9**</ins> 마그마 $(A,\star)$에 대하여, 만일 $A$의 어떤 부분집합 $S$가 $\star$에 대해 닫혀있다면, $S$를 $A$의 *부분마그마*라고 부른다.

</div>

그 다음 차례는 동치관계다. 마그마의 연산을 잊어버리고 집합으로 취급해도 이들 사이에 함수가 잘 정의되었듯이, 단순한 집합으로써 마그마 위의 동치관계 또한 잘 정의된다. 

하지만 단순한 동치관계 또한 마그마를 다룰 때에는 적절한 도구가 아니다. 예를 들어, 어떤 마그마 $A$ 위에서 $x\equiv x'\pmod{R}$, $y\equiv y'\pmod{R}$가 성립한다 하자. $x$와 $x'$, 그리고 $y$와 $y'$가 $R$에 의해 같은 원소로 취급되고 있으므로, 다음의 식

$$x\star y\equiv x'\star y'\pmod{R}$$

을 기대하는 것이 합리적이다. 하지만 $R$에 어떤 조건도 걸려있지 않다면 이 식이 성립할 이유가 없다. 따라서, 다음과 같은 조건을 추가로 정의한다.

<div class="definition" markdown="1">

<ins id="df10">**정의 10**</ins> 마그마 $(A,\star)$가 주어졌다고 하자. 만일 집합 $A$ 위에 정의된 동치관계 $R$과, 임의의 $a\in A$에 대하여

$$x\equiv x'\implies a\star x\equiv a\star x'$$

을 만족한다면, $R$이 $\star$와 *left compatible*하다고 말한다. 비슷하게 만일 

$$x\equiv x'\implies x\star a\equiv x'\star a$$

가 모든 $a$에 대하여 성립한다면, $R$이 $\star$와 *right compatible*하다고 말한다. Left compatible인 동시에 right compatible인 동치관계를 간단히 *compatible*하다고 한다.
</div>

물론 위의 식에서 $\equiv$는 항상 관계 $R$에 대한 것을 뜻한다.

$R$이 동치관계라면 집합으로써 *몫집합* $A/R$이 잘 정의된다는 것은 이미 집합론에서 살펴본 적이 있다. ([Set Theory, §동치관계, 정의 6](/ko/math/set_theory/equivalence_relations#df6)) 만일 $R$이 마그마 $A$의 연산과 *compatible*한 동치관계라면 집합 $A/R$은 자연스러운 마그마 구조까지 가진다.

우선, $R$에 대한 별다른 가정 없이 $A/R$에 연산을 정의한다고 생각해보자. $x\in A$의 대표원소를 $[x]$로 적자. $A$의 연산을 이용하여 $A/R$ 위의 연산 $\tiny\char\"2606$을 정의한다면, 이는 당연히

$$[x]\mathbin{\tiny\char"2606}[y]=[x\star y]$$

여야 할 것이다. 

이 정의에서 생기는 문제는 $[x]$의 대표원소 $x$를 택하는 방법이 유일하지 않다는 것이다. 위의 식이 의미를 갖기 위해서는, 가령 $[x]$의 대표원소로 $x$ 대신 $x'$를 택했더라도 $[x]\mathbin{\tiny\char\"2606}[y]$의 값이 잘 정의되어야 한다. 즉, 다음의 식

$$[x]\mathbin{\tiny\char"2606}[y]=[x'\star y]$$

가 성립해야 할 것이고, 이를 위해서는 다음의 질문

> 만약 $x'\in[x]$이라면, $[x'\star y]=[x\star y]$?

에 대한 답이 긍정적이어야 한다. 뒤의 식은

$$x'\star y\equiv x\star y\mod R$$

로 바꾸어 쓸 수 있고, 앞선 정의를 따르자면 이는 정확히 $R$이 *right* compatible해야 한다는 의미다. 

마찬가지 논리로, $[y]$의 대표원소의 선택에도 연산 $\mathbin{\tiny\char\"2606}$의 값이 변하지 않아야 하므로

$$x\star y\equiv x\star y'\mod R$$

가 성립해야 하고, 이는 정확히 $R$이 *left* compatible해야 한다는 의미가 된다.
 
즉, $A/R$이 마그마가 되기 위해서는 $R$이 $A$의 연산과 compatible한 동치관계여야 한다. 실제로, 만일 이것이 성립한다면 $x\equiv x'$, $y\equiv y'$를 만족하는 $A$의 원소들에 대하여

$$x\star y\equiv x'\star y\equiv x'\star y'\mod R$$

이 성립하므로, $[x]$와 $[y]$의 대표원소를 모두 다르게 뽑아오더라도 연산의 정의에 문제가 생기지 않는다. 

이 논의를 정리하여, 다음과 같이 새로 정의한다.

<div class="definition" markdown="1">

<ins id="df11">**정의 11**</ins> 마그마 $A$와, $A$의 연산과 compatible한 동치관계 $R$에 대하여 위와 같이 얻어지는 마그마 $A/R$을 *몫마그마*라 부른다.

</div>

만일 $\star$가 결합법칙 혹은 교환법칙을 만족하면 $\mathbin{\tiny\char\"2606}$ 또한 그러하다는 것을 쉽게 확인할 수 있다. 위의 construction에서는 구별을 위해 $\star$와 $\mathbin{\tiny\char\"2606}$를 다르게 표기하였으나, 이들은 문맥상 쉽게 구별할 수 있으므로 몫마그마에서의 연산 또한 $\star$와 같이 적는 것이 보통이다.

<div class="remark" markdown="1">

<ins id="rmk1">**참고**</ins> 한편, 동치관계와 분할은 같은 것이므로, compatible한 동치관계의 분할은 어떠한 조건을 만족해야 하는지도 궁금하다. 

여기에서 가장 유력한 후보는 부분마그마이다. 마그마 $(A,\star)$와 부분마그마 $S$를 생각하자. 그럼 부분마그마 $S$가 $A/R$의 한 원소이도록 하는 동치관계 $R$이 존재할까? 이에 대한 답을 하기에 마그마는 너무 담고 있는 정보가 부족하기 때문에, 이에 대한 답은 군을 정의한 후 찾을 수 있다. 

</div>

## 준군과 모노이드

지금까지 우리는 가장 일반적인 가정 하에서 논리를 풀어왔다. 하지만 우리는 대부분 마그마의 연산이 결합법칙을 만족하는 경우만을 생각하게 된다.

<div class="definition" markdown="1">

<ins id="df12">**정의 12**</ins> 결합법칙을 만족하는 마그마 $(A, \star)$를 *준군*이라 부른다.

</div>

우리가 이전에 정의했던 준동형사상이나 부분구조, 몫구조들은 어떠한 변화도 필요 없이 준군에서의 준동형사상이나 부분구조, 몫구조를 정의한다. 예를 들어, *준군 준동형사상*이라는 것은 단순히 마그마로써의 준동형사상이고, 부분준군은 이 준군을 마그마로 보았을 때의 부분마그마를 의미한다. 

준군의 부분마그마는 그 자체로 준군이 된다. $S\subset A$가 semigroup $(A,\star)$의 부분마그마라면, 임의의 $a,b,c\in S$는 $S$의 원소이기 이전에 $A$의 원소이므로 다음의 식

$$a\star(b\star c)=(a\star b)\star c$$

이 성립하기 때문이다. 

준군의 몫준군 또한 준군이 된다. 역시 혼동을 피하기 위해 $A/R$ 상에서의 연산을 $\mathbin{\tiny\char\"2606}$로 적으면, 

$$([x]\mathbin{\tiny\char"2606}[y])\mathbin{\tiny\char"2606}[z]=[x\star y]\mathbin{\tiny\char"2606}[z]=[(x\star y)\star z]=[x\star(y\star z)]=\cdots=[x]\mathbin{\tiny\char"2606}([y]\mathbin{\tiny\char"2606}[z])$$

임을 쉽게 확인할 수 있기 때문이다.

준군의 준동형사상이나 부분준군, 몫준군 등이 마그마와 동일하게 정의되는 이유는 $\star$의 결합법칙이 원소에 대한 성질이 아니라, 연산 $\star$에 대한 성질이기 때문이다. 다음과 같이 준군에 원소에 관한 조건을 추가하면 조금 더 흥미로운 모노이드 구조를 얻는다.

<div class="definition" markdown="1">

<ins id="df13">**정의 13**</ins> 임의의 마그마 $(A,\star)$에 대하여, 어떤 $e\in A$가 모든 $x\in A$에 대하여

$$x\star e=e\star x=x$$

를 만족한다면, $e$를 *항등원*이라 부른다. 

</div>

임의의 마그마 $A$는 많아야 하나의 항등원을 갖는다. 만일 $e$와 $e'$가 모두 $A$의 항등원이라면, 

$$e=e\star e'=e'\star e=e'$$

가 되기 때문이다. 위의 식들에서, 마그마 $A$는 교환법칙을 만족할 필요는 없지만, 항등원은 반드시 $A$의 모든 원소와 교환법칙을 만족해야 한다는 것 또한 눈여겨 볼 만 하다.

<div class="definition" markdown="1">

<ins id="df14">**정의 14**</ins> 결합법칙을 만족하고, 항등원을 갖는 마그마 $(A,\star)$를 *모노이드*라 부른다. 

</div>

준군을 정의한 후에는 준동형사상이나 부분준군, 몫준군 등에 대해 전혀 신경을 쓸 필요가 없었다. 하지만 항등원이라는 것은 연산 $\star$가 갖는 성질이 아니라 마그마 $A$의 원소에 대한 성질이므로 이번에는 약간의 수정이 필요하다. 

예를 들어, 두 개의 모노이드 $(A,\star)$, $(A',\star')$와 그들의 항등원 $e$, $e'$에 대하여, 만일 $f$가 $A$에서 $A'$로의 마그마 준동형사상이라면 $f(e)=e'$일 이유가 전혀 없다. 따라서, 이번에는 새롭게 다음과 같이 정의한다.

<div class="definition" markdown="1">

<ins id="df15">**정의 15**</ins> 두 모노이드 $(A, \star, e)$, $(A',\star', e')$에 대하여, $f(e)=e'$를 만족하는 마그마 준동형사상을 *모노이드 준동형사상*이라 부른다. 

</div>

그리고, 부분모노이드 역시 항등원을 포함해야 한다. 부분마그마의 유일한 조건은 "$\star$에 대해 닫혀있을 것"이었으므로, 이 정의 또한 마그마와는 달라지는 모노이드만의 특징이지만, 만일 우리가 부분마그마를 정의할 때

> **정의 9'.** $(A,\star)$의 부분마그마는 그 자체로 $\star$에 대한 마그마 구조를 가지는 $A$의 부분집합 $S$를 뜻한다.

라고 정의했다면, 부분모노이드도 동일하게 *$\star$에 대한 모노이드 구조를 갖는 $A$의 부분집합*으로 정의될 수 있을 것이고, 이는 모든 대수적인 구조에 대해 성립한다.

다행히도 몫구조는 크게 신경쓰지 않아도 된다. 즉, 모노이드 $(A, \star)$와, $\star$와 compatible한 동치관계 $R$이 주어졌다고 하면, $A/R$은 자연스럽게 모노이드 구조를 갖는다. 이를 살펴보기 위해서는 $A/R$에서 항등원의 역할을 하는 원소를 찾아야 한다. $A/R$의 각 원소들은 $A$의 분할이므로, 여기에 $e$를 포함하는 분할 $[e]$가 유일하게 존재할텐데, 그럼 임의의 다른 분할 $[x]$에 대하여

$$[x]\mathbin{\tiny\char"2606}[e]=[x\star e]=[x]=[e\star x]=[e]\mathbin{\tiny\char"2606}[x]$$

가 성립하기 때문이다. 

## 군

이 카테고리의 글들은 군의 성질에 대한 글들이다. 군은 직관적으로 *모든 원소들이 역원을 갖는 모노이드*라고 생각할 수 있다.

<div class="definition" markdown="1">

<ins id="df16">**정의 16**</ins> 모노이드 $(A,\star,e)$에 대하여, $x$가 $y$의 *왼쪽 역원*이라는 것은 $x\star y=e$가 성립하는 것이다. 비슷하게, $x$가 $y$의 *오른쪽 역원*이라는 것은 $y\star x=e$인 것이다. 만일 $x$가 $y$의 왼쪽 역원인 동시에 오른쪽 역원이라면, 즉 $x\star y=y\star x=e$가 성립한다면 $x$가 $y$의 역원이라고 부르고, 이 때 $y$는 *가역*이라고 부른다.

</div>

당연하게 왼쪽 역원의 존재성과 오른쪽 역원의 존재성은 서로 관련이 없다. 무한집합 $E$에 대하여, $E$에서 $E$로의 함수들의 모임 $\operatorname{Fun}(E,E)$를 생각하면 이 집합은 함수의 합성을 연산으로, $\operatorname{id}\_E$를 항등원으로 갖는 모노이드가 되지만 이 집합에는 왼쪽 가역이지만 오른쪽 가역은 아닌 원소와, 오른쪽 가역이지만 왼쪽 가역은 아닌 원소가 모두 존재한다. ([Set Theory, §함수, 정의 10](/ko/math/set_theory/functions#df10))

만일 $x$가 $y$의 오른쪽 역원이라면 $y$는 $x$의 왼쪽 역원이 된다는 것은 정의로부터 자명하다. 따라서 $y$가 가역이라면 $x$ 또한 가역이고, $y$가 $x$의 역원이 된다. 일반적으로 $x$의 역원을 $x^{-1}$으로 적지만, 만약 연산이 $+$로 주어졌다면 이 대신 $-x$와 같이 적는다. 물론, 이렇게 적기 위해서는 역원이 유일하게 결정되어야 한다.

<div class="proposition" markdown="1">

<ins id="pp17">**명제 17**</ins> 모노이드 $(A, \star, e)$에 대하여, $x\in A$가 $A$의 가역인 원소라 하면 $x$의 역원은 유일하다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

만일 $x'$와 $x''$가 $x$의 역원이었다면,

$$x'=x'\star e=x'\star( x\star x'')=(x'\star x)\star x''=e\star x''=x''$$

이므로 $x'=x''$이다.

</details>

이를 이용하면 다음의 따름정리를 얻는다. 

<div class="proposition" markdown="1">

<ins id="crl18">**따름정리 18**</ins> 모노이드 $(A,\star,e)$와, 가역인 $A$의 원소 $a$, $b$에 대하여, 다음이 성립한다.

1. $(a^{-1})^{-1}=a$
2. $(a\star b)^{-1}=b^{-1}\star a^{-1}$.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

앞선 명제에 의하여 역원은 유일하므로, 주어진 식들의 우변이 역원의 조건을 만족한다는 것을 직접 계산하여 보이면 충분하다.

우선, $a^{-1}$의 역원이 $a$인지 살펴보자. $a^{-1}$의 역원은 다음의 두 식

$$a^{-1}\star x=x\star a^{-1}=e$$

를 만족하는 $x$이다. 그런데, 

$$a^{-1}\star a=a\star a^{-1}=e$$

가 $a^{-1}$의 정의에 의해 성립하므로, $x=a$가 앞선 식을 만족한다. 이제 $a^{-1}$의 역원은 유일하므로, $a^{-1}$의 역원은 $(a^{-1})^{-1}$은 *반드시* $a$가 되어야 한다.

비슷하게, 두 번째 주장 또한 다음의 두 식으로부터 자명하게 따라온다.

$$\begin{aligned}(a\star b)\star(b^{-1}\star a^{-1})&=a\star(b\star b^{-1})\star a^{-1}=a\star e\star a^{-1}=a\star a^{-1}=e,\\(b^{-1}\star a^{-1})\star(a\star b)&=b^{-1}\star(a^{-1}\star a)\star b=b^{-1}\star e\star b=b^{-1}\star b=e.\end{aligned}$$

</details>


이제 군은 다음과 같이 정의된다.

<div class="definition" markdown="1">

<ins id="df19">**정의 19**</ins> 임의의 원소가 가역인 모노이드 $(A,\star,e)$를 *군*이라 부른다. 만일 $\star$가 교환법칙을 만족한다면, $(A,\star,e)$가 *가환군* (혹은 *아벨군*)이라 부른다. 

</div>

다음 글부터 우리는 관례를 따라 군 $G$의 연산을 모두 곱하기로 고정할 것인데, 가환군들의 연산은 덧셈으로 적는 것이 또 하나의 관례이다. 따라서 가환군들의 항등원 또한 $0$으로 적게 된다.

군 준동형사상을 살펴보자. 처음에 준군을 정의할 때, 결합법칙은 연산이 갖는 성질이기 때문에 마그마 준동형사상과 준군 준동형사상은 정확히 같은 것이 되었다. 한편, 모노이드를 정의할 때 항등원은 집합 $A$가 갖는 성질이기 때문에, 우리가 따로 $f(e)=e'$라는 조건을 달아줘야 했었다. 

군에서 새로 추가된 조건은 이 둘 사이 어딘가에 있다. 가역이라는 성질은 각각의 원소들이 갖는 성질이므로 (즉 연산이 가지고 있는 성질이 아니므로) $f:A\rightarrow A'$를 타고 보낸 원소들이 모두 가역이라는 조건을 추가하는 것이 자연스럽겠지만, 군의 정의는 *모든* 원소들이 가역이라는 것이기 때문에 임의의 $x\in A$에 대하여 $f(x)\in A'$는 군 $A'$의 원소로써 자연스럽게 가역이어야 한다.  

우리는 심지어 모노이드 준동형사상의 조건, 즉 $f(e)=e'$마저도 생략할 수 있는데, 만일 $f$가 연산을 보존한다면

$$e'\star' f(e)=f(e)=f(e\star e)=f(e)\star'f(e)$$

이고, $f(e)$는 가역이므로 양 변의 오른쪽에 $f(e)$의 역원을 연산해주면 $e'=f(e)$를 얻을 것이기 때문이다.

위의 논증에서는 다음과 같은 명제를 사용하였다.

<div class="proposition" markdown="1">

<ins id="pp20">**명제 20 (Cancellation law)**</ins> 군 $(G, \star, e)$와 그 원소들 $a,b,c$에 대하여, 만일 $a\star b=a\star c$ 혹은 $b\star a=c\star a$가 성립한다면 $b=c$가 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

양 변의 왼쪽 혹은 오른쪽에 $a$의 역원을 연산해주면 된다.

</details>

한편, 부분군은 조금 전에 새롭게 정의한 부분마그마의 정의와 동일하게 쓸 수 있다.

<div class="definition" markdown="1">

<ins id="df21">**정의 21**</ins> 군 $(G, \star, e)$의 부분집합 $S$가 $G$의 *부분군*이라는 것은 $S$ 자기 자신이 $\star$에 대한 군의 구조를 갖는 것이다. 

</div>

앞서 언급한 것과 같이, 추상적인 군 $G$의 연산은 곱하기로 적는 것이 관례이므로 앞으로는 간단히 

> $G$가 군이라 하자.

와 같은 말을 사용할 것이다. 다만, 가환군의 경우에는 앞서 말한 것과 같이 연산을 곱하기가 아니라 더하기로 적는 것이 관례이다.

다음의 명제는 항등원이 존재하는지, 역원에 대해 닫혀있는지 등등을 모두 생략하고 단 하나의 기준만으로 주어진 부분집합이 부분군인지의 여부를 알려준다.

<div class="proposition" markdown="1">

<ins id="pp22">**명제 22**</ins> 군 $(G, \star, e)$의 공집합이 아닌 부분집합 $S$가 $G$의 부분군인 것은, 임의의 $a,b\in S$에 대해 $a\star b^{-1}\in S$가 항상 성립하는 것과 동치이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

만일 $S$가 $G$의 부분군이라면, $b\in S$이므로 $b^{-1}\in S$이고, 따라서 $a\star b^{-1}\in S$는 자명하게 성립한다.

따라서 반대방향만 보이면 충분하다. 우선 $S$가 공집합이 아니므로, 어떤 $a\in S$가 존재하고, 그럼 $a\star a^{-1}\in S$이므로 $e\in S$이다. 이제 임의의 $a\in S$에 대하여, $a^{-1}=e\star a^{-1}\in S$가 성립한다. 또, 임의의 $a,b\in S$에 대하여 $a\star b^{-1}=a\star(b^{-1})^{-1}\in S$가 성립한다.

</details>

하지만 일반적으로 이 명제를 사용하는 것은 위의 정의를 적용하는 것에 비해 특별히 어렵지도, 쉽지도 않다.

마지막으로 몫군 또한 별다른 수정 없이 잘 정의된다. 군 $(G, \star, e)$와, $\star$와 compatible한 동치관계 $R$에 대하여 $G/R$은 모노이드 구조를 갖는다는 것을 앞에서 확인했었다. $G/R$이 군의 구조를 갖는다는 것을 확인하려면, $G/R$의 임의의 원소 $[x]$가 가역이라는 것만 보이면 되는데, 

$$[x]\mathbin{\tiny\char"2606}\bigl[x^{-1}\bigr]=\bigl[x\star (x^{-1})\bigr]=[e]=\bigl[x^{-1}\star x\bigr]=\bigl[x^{-1}\bigr]\mathbin{\tiny\char"2606}[x]$$

가 성립하므로, $G/R$의 임의의 원소는 가역임을 알 수 있다. 


---
**Reference**

**[Bou]** Bourbaki, N. Algebra. I. Chapters 1-3. Translated from the French. Reprint of the 1989 English translation. *Elements of Mathematics. Springer-Verlag, Berlin,* 1998.  

---
[^1]: *마그마* (magma)는 **[Bou]**에서 처음 도입된 용어인데, 프랑스어로는 잡동사니라는 뜻을 가지고 있다.
[^1]: 사실 $-1$을 *1의 역원을 더하는 것*으로 해석하면, 즉 주어진 식을 $4+(-1)+(-2)$로 해석하면 $+$는 associative하므로 연산순서는 관련이 없다. 