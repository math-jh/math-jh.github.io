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
last_modified_at: 2022-09-08
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

## Kernel, cokernel

위의 예시를 일반화하여, 임의의 map $f:X\rightarrow Y$가 주어졌다 하고, 이로부터 만들어지는 exact sequence를 생각할 수 있다. 적절한 직관을 부여하기 위해 우선 다음 명제를 증명하자.

<div class="proposition" markdown="1">

<ins id="pp4">**명제 4**</ins> 임의의 map $f:X\rightarrow Y$이 주어졌다 하고, $K=\ker f$, 그리고 자연스러운 inclusion $i:K\rightarrow X$를 생각하자. 그럼 $fi=0$이며, 뿐만 아니라 $i:K\rightarrow X$는 다음의 universal property를 만족한다.

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

<ins id="pp5">**명제 5**</ins> 임의의 map $f:X\rightarrow Y$이 주어졌다 하고, $C=Y/\operatorname{im}(f)$, 그리고 자연스러운 projection $p:Y\rightarrow C$를 생각하자. 그럼 $pf=0$이며, 뿐만 아니라 $p:Y\rightarrow C$는 다음의 universal property를 만족한다.

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

<ins id="df6">**정의 6**</ins> 두 $R$-module $X,Y$와 이들 사이의 map $f:X\rightarrow Y$에 대하여, module $Y/\operatorname{im}(f)$를 $f$의 *cokernel<sub>여핵</sub>*이라 부르고 $\operatorname{coker}(f)$으로 적는다.

</div>

이를 이용하면 임의의 $f:X\rightarrow Y$를 exact sequence의 언어로 설명할 수 있다. 

<div class="proposition" markdown="1">

<ins id="pp7">**명제 7**</ins> 두 $R$-module $X,Y$와 이들 사이의 map $f:X\rightarrow Y$에 대하여, 다음의 sequence

$$0\longrightarrow\ker(f)\longrightarrow X\overset{f}{\longrightarrow}Y\longrightarrow \operatorname{coker}(f)\longrightarrow 0$$

은 exact sequence가 된다.

</div>



---

**참고문헌**

**[Hu]** S.T. Hu, *Introduction to homological algebra*. University Microfilms, 1979.  
**[Vak]** R. Vakil, *The rising sea: foundations of algebraic geometry*. 2015. Preprint. [링크](http://math.stanford.edu/~vakil/216blog/FOAGnov1817public.pdf)


