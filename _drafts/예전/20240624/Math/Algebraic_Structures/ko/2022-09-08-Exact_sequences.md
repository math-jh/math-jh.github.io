---

title: "완전열"
excerpt: "기본정의"

categories: [Math / Algebraic Structures]
permalink: /ko/math/algebraic_structures/exact_sequences
header:
    overlay_image: /assets/images/Math/Algebraic_structures/Exact_sequences.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_structures-ko"

date: 2022-09-08
last_modified_at: 2022-09-12
weight: 202

---

## 완전열

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> $A$-module들의 열

$$\cdots\longrightarrow E\overset{f}{\longrightarrow} F\overset{g}{\longrightarrow} G\longrightarrow \cdots$$

이 주어졌다 하자. 이 열이 $F$에서 *semi-exact*라는 것은 $gf=0$인 것이다. 만일 주어진 $A$-module들의 열이 각 성분에서 모두 semi-exact라면 이를 *chain complex<sub>사슬복합체</sub>*라 부른다.

</div>

조건 $gf=0$은 $\im(f)\subseteq\ker(g)$와 동치이다. 특별히 $\im(f)=\ker(g)$가 성립할 경우, 우리는 위의 열이 $F$에서 *exact<sub>완전</sub>*하다 하고, 각 성분에서 모두 exact인 열을 *exact sequence<sub>완전열</sub>*라 부른다. 

임의의 $A$-module $E$에 대하여, zero module $0$에서 $E$로 가는 유일한 map은 $0$을 $0$으로 보내는 영함수뿐이고, $E$에서 $0$으로 가는 함수 또한 $X$의 모든 원소를 $0$으로 보내는 영함수뿐이다. 이러한 상황에서는 

$$0\longrightarrow E,\qquad E\longrightarrow 0$$

와 같이 함수에 따로 이름을 붙이지 않는다. 한편, 임의의 두 $A$-module $E,F$에 대하여, $E$의 모든 원소를 $0\in F$로 보내는 영함수 또한 생각할 수 있는데, 이러한 영함수는 두 함수 $E\rightarrow 0$과 $0\rightarrow F$의 합성으로 생각할 수 있으므로 열

$$\cdots\longrightarrow D\longrightarrow E\overset{0}{\longrightarrow} F\longrightarrow G\longrightarrow\cdots$$

이 주어진 것은 두 개의 열 

$$\cdots\longrightarrow D\longrightarrow E\longrightarrow 0,\qquad 0\longrightarrow F\longrightarrow G\longrightarrow \cdots$$

이 주어진 것으로 생각해도 무방하다. 

유한한 열

$$E\longrightarrow \cdots\longrightarrow G$$

이 주어졌다 하면, 항상 

$$\cdots\longrightarrow 0\longrightarrow 0\longrightarrow E\longrightarrow \cdots\longrightarrow G\longrightarrow 0\longrightarrow 0\longrightarrow\cdots$$

을 통해 이를 무한한 열로 취급할 수 있다. 뿐만 아니라, 임의의 함수 $f$에 영함수를 합성하면 그 결과는 항상 영함수이므로, 만일 처음의 열이 exact sequence였다면 아래와 같이 무한하게 확장한 열 또한 exact sequence가 된다. 따라서 임의의 열은 항상 $\mathbb{Z}$로 index가 주어졌다고 생각할 수 있다.

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins> 임의의 $A$-module $E$에 대하여, 다음의 열

$$0\longrightarrow E\overset{f}{\longrightarrow}F$$

이 exact라는 것은 $\ker(f)=0$이라는 것이다. 즉 $f$는 단사이다. 비슷하게, 다음의 열

$$E\overset{f}{\longrightarrow}F\longrightarrow 0 $$

이 exact라는 것은 $\im(f)=F$라는 것, 즉 $f$가 전사라는 것이다. 따라서 다음의 열

$$0\longrightarrow E\overset{f}{\longrightarrow}F\longrightarrow 0$$

이 exact라는 것은 $\ker(f)=0$이고 $\im(f)=F$라는 것이므로, $f$가 전단사라는 것이다.

</div>

따라서 exact sequence의 자명하지 않은 예시 중 가장 짧은 것은 다음의 sequence

$$0\longrightarrow E\longrightarrow F\longrightarrow G\longrightarrow 0$$

이다. 이를 *short exact sequence<sub>짧은 완전열</sub>*이라 부른다. 

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> 임의의 $A$-module $E$가 주어졌다 하자. Submodule $M\subseteq E$에 대하여, quotient module $E/M$를 생각하면 자연스러운 projection map $p:E\rightarrow E/M$가 존재하며, $\ker(p)=A$이다. 따라서 $M$에서 $E$로의 inclusion map을 생각하면, 다음의 열
    
$$0\longrightarrow M\longrightarrow E\longrightarrow E/M\longrightarrow 0$$
    
은 short exact sequence가 된다. 

혹은, 반대로 임의의 전사함수 $f:E\rightarrow F$가 주어졌다 하면 다음의 열

$$0\longrightarrow \ker f\longrightarrow E\overset{f}{\longrightarrow}F\longrightarrow 0$$

이 short exact sequence가 된다.

</div>

더 일반적으로 다음과 같이 <em_ko>임의의</em_ko> map을 exact sequence로 분리할 수 있다.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> 두 $A$-module $E,F$와 이들 사이의 map $f:E \rightarrow F$에 대하여, 다음의 sequence

$$0\longrightarrow\ker(f)\longrightarrow E\overset{f}{\longrightarrow}F\longrightarrow \coker(f)\longrightarrow 0$$

은 exact sequence가 된다.

</div>

이제 다음 글부터 우리는 exact sequence를 통하여 module의 성질들을 살펴본다. 기본적으로, exactness를 보존하는 연산들은 정보를 일어버리지 않는 것들이고, 그렇지 못한 것들은 원래의 정보를 잃어버리는 것으로 생각하는 것이 큰 흐름이다.

Product/sum 정도 하고
split/free 하고
change of scalar 하고

홈
텐서
어드조인트




---

**참고문헌**

**[Hu]** S.T. Hu, *Introduction to homological algebra*. University Microfilms, 1979.  
**[Vak]** R. Vakil, *The rising sea: foundations of algebraic geometry*. 2015. Preprint. [링크](http://math.stanford.edu/~vakil/216blog/FOAGnov1817public.pdf)


