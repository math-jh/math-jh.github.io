---

title: "완전열"
excerpt: "기본정의"

categories: [Math / Homological Algebra]
permalink: /ko/math/homological_algebra/exact_sequences
header:
    overlay_image: /assets/images/Homological_algebra/a.png
    overlay_filter: 0.5
sidebar: 
    nav: "homological_algebra-ko"

date: 2022-09-08
last_modified_at: 2022-09-12
weight: 1

---

앞으로 항상 $R$은 곱셈에 대한 항등원 $1$을 갖고, commutative인 것으로 생각한다. 또, $R$-module homomorphism을 간단히 함수, 혹은 map이라 부르기로 한다.

## Exactness

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> $R$-module들의 열

$$\cdots\longrightarrow X\overset{f}{\longrightarrow} Y\overset{g}{\longrightarrow} Z\longrightarrow \cdots$$

이 주어졌다 하자. 이 열이 $Y$에서 *semi-exact*라는 것은 $gf=0$인 것이다. 만일 주어진 $R$-module들의 열이 각 성분에서 모두 semi-exact라면 이를 *chain complex<sub>사슬복합체</sub>*라 부른다.

</div>

조건 $gf=0$은 $\operatorname{im}(f)\subseteq\ker(g)$와 동치이다. 특별히 $\operatorname{im}(f)=\ker(g)$가 성립할 경우, 우리는 위의 열이 $Y$에서 *exact<sub>완전</sub>*하다 하고, 각 성분에서 모두 exact인 열을 *exact sequence<sub>완전열</sub>*라 부른다. 

임의의 $R$-module $X$에 대하여, zero module $0$에서 $X$로 가는 유일한 map은 $0$을 $0$으로 보내는 영함수뿐이고, 거꾸로 $X$에서 $0$으로 가는 함수 또한 $X$의 모든 원소를 $0$으로 보내는 영함수뿐이다. 이러한 상황에서는 

$$0\longrightarrow X,\qquad X\longrightarrow 0$$

와 같이 함수에 따로 이름을 붙이지 않는다. 한편, 임의의 두 $R$-module $X,Y$에 대하여, $X$의 모든 원소를 $0\in Y$로 보내는 영함수 또한 생각할 수 있는데, 이러한 영함수는 두 함수 $X\rightarrow 0$과 $0\rightarrow Y$의 합성으로 생각할 수 있으므로 열

$$\cdots\longrightarrow W\longrightarrow X\overset{0}{\longrightarrow} Y\longrightarrow Z\longrightarrow\cdots$$

이 주어진 것은 두 개의 열 

$$\cdots\longrightarrow W\longrightarrow X\longrightarrow 0,\qquad 0\longrightarrow Y\longrightarrow Z\longrightarrow \cdots$$

이 주어진 것으로 생각해도 무방하다. 

유한한 열

$$X\longrightarrow \cdots\longrightarrow Z$$

이 주어졌다 하면, 항상 

$$\cdots\longrightarrow 0\longrightarrow 0\longrightarrow X\longrightarrow \cdots\longrightarrow Z\longrightarrow 0\longrightarrow 0\longrightarrow\cdots$$

을 통해 이를 무한한 열로 취급할 수 있다. 뿐만 아니라, 임의의 함수 $f$에 영함수를 합성하면 그 결과는 항상 영함수이므로, 만일 처음의 열이 exact sequence였다면 아래와 같이 무한하게 확장한 열 또한 exact sequence가 된다. 따라서 임의의 열은 항상 $\mathbb{Z}$로 index가 주어졌다고 생각할 수 있다.

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins> 임의의 $R$-module $X$에 대하여, 다음의 열

$$0\longrightarrow X\overset{f}{\longrightarrow}Y$$

이 exact라는 것은 $\ker(f)=0$이라는 것이다. 즉 $f$는 단사이다. 비슷하게, 다음의 열

$$X\overset{f}{\longrightarrow}Y\longrightarrow 0 $$

이 exact라는 것은 $\operatorname{im}(f)=Y$라는 것, 즉 $f$가 전사라는 것이다. 따라서 다음의 열

$$0\longrightarrow X\overset{f}{\longrightarrow}Y\longrightarrow 0$$

이 exact라는 것은 $\ker(f)=0$이고 $\operatorname{im}(f)=Y$라는 것이므로, $f$가 전단사라는 것이다.

</div>

위의 예시로부터 다음의 열

$$0\longrightarrow X\longrightarrow 0$$

이 exact라면, $X=0$이어야 한다는 것이 자명하다. 또, 여기에 하나의 성분을 추가하여 얻어진

$$0\longrightarrow X\overset{f}{\longrightarrow}Y\longrightarrow 0$$

이 exact라는 것 또한 우리가 잘 알고 있는 조건, 즉 $f$가 전단사라는 조건과 동치이다. 따라서 exact sequence의 자명하지 않은 예시 중 가장 짧은 것은 다음의 sequence

$$0\longrightarrow X\longrightarrow Y\longrightarrow Z\longrightarrow 0$$

이다. 이를 *short exact sequence<sub>짧은 완전열</sub>*이라 부른다. 

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> 임의의 $R$-module $X$가 주어졌다 하자. Submodule $A\subseteq X$에 대하여, quotient module $X/A$를 생각하면 자연스러운 projection map $p:X\rightarrow X/A$가 존재하며, $\ker(p)=A$이다. 따라서 $A$에서 $X$로의 inclusion map을 생각하면, 다음의 열
    
$$0\longrightarrow A\longrightarrow X\longrightarrow X/A\longrightarrow 0$$
    
은 short exact sequence가 된다. 

혹은, 반대로 임의의 전사함수 $f:X\rightarrow Y$가 주어졌다 하면 다음의 열

$$0\longrightarrow \ker f\longrightarrow X\overset{f}{\longrightarrow}Y\longrightarrow 0$$

이 short exact sequence가 된다.

</div>

<div class="example" markdown="1">

<ins id="ex4">**예시 4**</ins> $R$의 ideal은 항상 $R$-module 구조를 갖는다. 이제 $R$의 두 ideal $I,J$에 대하여 $R=I+J$라 가정하자. 그럼 다음의 short exact sequence

$$0\longrightarrow I\cap J\longrightarrow I\oplus J\longrightarrow R\longrightarrow 0$$

가 존재한다. 여기서 첫째 함수는 $x\mapsto (x,-x)$로 정의된 함수이고, 둘째 함수는 $(x,y)\mapsto x+y$로 정의된 함수이다.

</div>

## Kernel, cokernel

위의 예시를 일반화하여, 임의의 map $f:X\rightarrow Y$가 주어졌다 하고, 이로부터 만들어지는 exact sequence를 생각할 수 있다. 적절한 직관을 부여하기 위해 우선 다음 명제를 증명하자.

<div class="proposition" markdown="1">

<ins id="pp5">**명제 5**</ins> 임의의 map $f:X\rightarrow Y$이 주어졌다 하고, $K=\ker f$, 그리고 자연스러운 inclusion $i:K\rightarrow X$를 생각하자. 그럼 $fi=0$이며, 뿐만 아니라 $i:K\rightarrow X$는 다음의 universal property를 만족한다.

> 임의의 $g:Z\rightarrow X$에 대하여, 만일 $gf=0$이 성립한다면 유일한 함수 $j:Z\rightarrow K$가 존재하여 $g=ij$이다. 
>
> ![universal_property_of_kernel](/assets/images/Homological_algebra/Exact_sequences-1.png){:width="212.85px" class="invert" .align-center}

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 유일성을 보이자. 만일 $ij=g=ij'$이도록 하는 두 함수 $j, j':Z\rightarrow K$가 존재한다면, 임의의 $z\in Z$에 대하여

$$0=g(z)-g(z)=i(j(z))-i(j'(z))=i(j(z)-j'(z))$$

가 성립한다. 그런데 $i$는 단사이므로, 이를 위해서는 모든 $z\in Z$에 대하여 $j(z)-j'(z)=0$, 즉 $j=j'$여야 한다. 

존재성 또한 자명하다. $g$의 공역을 $K$로 제한한 것이 주어진 조건을 만족하기 때문이다.

</details>

이제 임의의 함수 $f:X\rightarrow Y$를 고정하자. 그럼 quotient module $Y/\operatorname{im}(f)$와, 자연스러운 projection $Y\rightarrow Y/\operatorname{im}(f)$가 잘 정의된다.

<div class="proposition" markdown="1">

<ins id="pp6">**명제 6**</ins> 임의의 map $f:X\rightarrow Y$이 주어졌다 하고, $C=Y/\operatorname{im}(f)$, 그리고 자연스러운 projection $p:Y\rightarrow C$를 생각하자. 그럼 $pf=0$이며, 뿐만 아니라 $p:Y\rightarrow C$는 다음의 universal property를 만족한다.

> 임의의 $g:Y\rightarrow Z$에 대하여, 만일 $gf=0$이 성립한다면 유일한 함수 $j:C\rightarrow Z$가 존재하여 $g=jp$이다. 
>
> ![universal_property_of_cokernel](/assets/images/Homological_algebra/Exact_sequences-2.png){:width="210px" class="invert" .align-center}

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 유일성을 보이자. 만일 $jp=g=j'p$이도록 하는 $j,j':C\rightarrow Z$가 존재한다면, 임의의 $y\in Y$에 대하여

$$0=g(y)-g(y)=j(p(y))-j'(p(y))=(j-j')(p(y))$$

가 성립한다. 그런데 $p$는 전사이므로, 이는 곧 모든 $c\in C$에 대하여 $j(c)-j'(c)=0$, 곧 $j=j'$라는 뜻이다.

존재성의 경우, $\ker(p)=\operatorname{im}(f)\subseteq\ker(g)$이므로 <#ref#>로부터 자명하다. 

</details>

위의 두 명제로부터, 위에서 정의한 $C$를 다음과 같이 부르는 것이 자연스럽다.

<div class="definition" markdown="1">

<ins id="df7">**정의 7**</ins> 두 $R$-module $X,Y$와 이들 사이의 map $f:X\rightarrow Y$에 대하여, module $Y/\operatorname{im}(f)$를 $f$의 *cokernel<sub>여핵</sub>*이라 부르고 $\operatorname{coker}(f)$으로 적는다.

</div>

이를 이용하면 임의의 $f:X\rightarrow Y$를 exact sequence의 언어로 설명할 수 있다. 

<div class="proposition" markdown="1">

<ins id="pp8">**명제 8**</ins> 두 $R$-module $X,Y$와 이들 사이의 map $f:X\rightarrow Y$에 대하여, 다음의 sequence

$$0\longrightarrow\ker(f)\longrightarrow X\overset{f}{\longrightarrow}Y\longrightarrow \operatorname{coker}(f)\longrightarrow 0$$

은 exact sequence가 된다.

</div>

## Splitting exact sequence

임의의 $F$-벡터공간 $V$와 그 부분공간 $S$에 대하여, 항상 적절한 부분공간 $T$가 존재하여 $V\cong S\oplus T$이다. 더 일반적으로 임의의 $R$에 대하여, free $R$-module은 항상 이러한 성질을 가진다. 이러한 대상들로 이루어진 exact sequence

$$\cdots\longrightarrow X\overset{f}{\longrightarrow}Y\overset{g}{\longrightarrow}Z\longrightarrow\cdots$$

의 경우, $Y$의 submodule $\ker(g)=\operatorname{im}(f)$은 항상 $Y$의 direct summand로 생각할 수 있다. 물론 일반적인 경우 이것이 성립할 이유가 없으므로, 다음과 같이 정의한다.

<div class="definition" markdown="1">

<ins id="df9">**정의 9**</ins> 주어진 exact sequence

$$\cdots\longrightarrow X\overset{f}{\longrightarrow}Y\overset{g}{\longrightarrow}Z\longrightarrow\cdots$$

에서 $\ker(g)=\operatorname{im}(f)$가 $Y$의 direct summand라면 위의 열이 $Y$에서 *split*한다고 한다. 모든 성분에서 split하는 exact sequence를 *splitting exact sequence*, 혹은 간단히 *split-exact*라 부른다. 

</div>

<div class="proposition" markdown="1">

<ins id="pp10">**명제 10**</ins> 다음 exact sequence 

$$\cdots\longrightarrow X\overset{f}{\longrightarrow}Y\overset{g}{\longrightarrow}Z\longrightarrow\cdots$$

가 $Y$에서 split-exact라면,

$$Y\cong\operatorname{im}(f)\oplus\operatorname{im}(g)$$

가 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

편의상 $A=\operatorname{im}(f)=\ker(g)$라 하자. 정의에 의해 $Y=A\oplus B$이도록 하는 $Y$의 submodule $B$가 존재한다. 주어진 명제를 증명하기 위해서는 $B\cong\operatorname{im}(g)$임을 증명하면 된다.

우선 $g:Y\rightarrow Z$를 $B$ 위로 제한한 $g\|\_B$를 생각하자. 그럼 $A\cap B=0$이므로, $g\|\_B$는 단사이고, 따라서 $g\|\_B$의 치역이 $\operatorname{im}(g)$와 같다는 것만 보이면 충분하다.

임의의 $z\in\operatorname{im}(g)$를 택하고, $y\in Y$가 $g(y)=z$를 만족하는 원소라 하자. 그럼 $Y=A\oplus B$이므로, 유일한 $a\in A, b\in B$가 존재하여 $y=a+b$이다. 이제 

$$z=g(y)=g(a+b)=g(a)+g(b)=g(b)=(g\|\_B)(b)$$

이므로 원하는 명제가 성립한다.

</details>

따라서 만일 다음의 short exact sequence

$$0\longrightarrow A\longrightarrow B\longrightarrow C\longrightarrow 0$$

이 split이라면, $B\cong A\oplus C$가 성립한다. 하지만 그 역은 성립하지 않는다. 위의 short exact sequence가 split이기 위해서는 다음의 *commutative* diagram

![nonsplitting_direct_sum](/assets/images/Homological_algebra/Exact_sequences-3.png){:width="408px" class="invert" .align-center}

에서, 가운데의 map $\alpha:B\rightarrow A\oplus C$가 isomorphism이어야 하는데, 단순히 isomorphism $\alpha$가 존재한다는 것만으로는 위의 diagram이 commute한다는 것을 보장할 수 없기 때문이다.

<div class="example" markdown="1">

<ins id="ex11">**예시 11**</ins> $R=\mathbb{Z}$라 하고, $A=\mathbb{Z}$, $C=\prod\_\mathbb{N}(\mathbb{Z}/2\mathbb{Z})$, 그리고 $B=A\oplus C$라 하자. 

$$0\longrightarrow A\overset{f}{\longrightarrow}B\overset{g}{\longrightarrow}C\longrightarrow 0$$

에서 $f:A\rightarrow B$는 $f(n)=(2n, 0)$, 그리고 $g:B\rightarrow C$는 다음의 식

$$g:(a, [b_0], [b_1], \ldots, )\mapsto ([a], [b_0], [b_1],\ldots)$$

으로 정의하면 위의 열이 exact인 것을 확인할 수 있다. 

위의 diagram을 commute하게 하는 isomorphism $\alpha:B\rightarrow A\oplus C$가 존재한다 가정하자. 그럼 $\alpha\circ f={\operatorname{incl}}\circ{\operatorname{id}}$으로부터, 임의의 $n\in A$에 대하여

$$\alpha(f(n))=(n,0)$$

임을 안다. 한편 둘째 사각형의 commutativity에 의하여, $\alpha(x, y)\in A\oplus C$에서 $C$에 해당하는 두 번째 성분은 반드시 $g(x,y)$와 같아야 한다. 편의상 $\alpha(x,y)$의 첫 번째 성분을 $\tilde{f}(x,y)$라 하자. 즉 

$$\alpha(x,y)=(\tilde{f}(x,y),g(x,y))$$

이다. 그럼 위의 논의로부터

$$1=\tilde{f}(f(1))=\tilde{f}(2,0)=2\tilde{f}(1,0)$$

이 얻어지므로 모순이 된다.

</div>

위의 증명을 자세히 살펴보면, linear map $\tilde{f}$의 존재가 중요한 역할을 한다는 것을 알 수 있으며, $\tilde{f}$는 밑의 exact sequence에서는 $A\hookrightarrow A\oplus C$ 뿐만 아니라, 자연스러운 projection $A\oplus C\rightarrow A$가 존재하기 때문에 얻어질 수 있었다. 따라서 다음의 명제가 어색하지 않다.

<div class="proposition" markdown="1">

<ins id="pp12">**명제 12**</ins> $R$-module들의 short exact sequence

$$0\longrightarrow A\overset{f}{\longrightarrow}B\overset{g}{\longrightarrow}C\longrightarrow 0$$

에서, 다음이 모두 동치이다.

1. $f$의 retraction이 존재한다.
2. $g$의 section이 존재한다.
3. 위의 short exact sequence가 split-exact이다.

</div>

---

**참고문헌**

**[Hu]** S.T. Hu, *Introduction to homological algebra*. University Microfilms, 1979.  
**[Vak]** R. Vakil, *The rising sea: foundations of algebraic geometry*. 2015. Preprint. [링크](http://math.stanford.edu/~vakil/216blog/FOAGnov1817public.pdf)


