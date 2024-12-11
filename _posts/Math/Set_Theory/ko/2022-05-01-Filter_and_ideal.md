---

title: "필터와 아이디얼, 갈루아 대응"
excerpt: "Filter와 ideal"

categories: [Math / Set Theory]
permalink: /ko/math/set_theory/filter_and_ideal
header:
    overlay_image: /assets/images/Math/Set_Theory/Filter_and_ideal.png
    overlay_filter: 0.5
sidebar: 
    nav: "set_theory-ko"

date: 2022-05-01
last_modified_at: 2022-04-04
weight: 18

---

**[Bou]**에는 이곳저곳에 흩어져있는 주제들과, 여기에 있지 않은 주제들을 모아 하나의 글로 묶었다. 

## Filter and ideal

우선 다음의 두 개념을 정의하자.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Ordered set $A$에 대하여, 부분집합 $X\subseteq A$가 *lower set<sub>하집합</sub>* (resp. *upper set<sub>상집합</sub>*)이라는 것은 $y\in A$가 어떤 $x\in X$에 대해 $y\leq x$ (resp. $x\leq y$)를 만족하면 반드시 $y\in X$인 것이다.

공집합이 아닌 right directed lower set을 *ideal*, 공집합이 아닌 left directed upper set을 *filter*라 부른다.

</div>

집합 $E$ 자신은 filter인 동시에 ideal이 된다. $E$가 아닌 filter와 ideal을 proper하다고 한다. 

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins> Ordered set $A$가 주어졌다 하자. 임의의 $x\in A$에 대하여, $x$의 *downward closure*[^1]

$$\downarrow x=\{y\in A\mid y\leq x\}$$

는 $A$의 ideal이 된다. 이러한 ideal을 *principal ideal*이라 부른다.

물론, 비슷하게, $x$의 *upward closure* 

$$\uparrow x=\{y\in A\mid y\geq x\}$$

는 $A$의 filter가 되며 이러한 filter를 *principal filter*라 부른다.

</div>

우리는 대부분 $A$가 lattice인 경우에 관심이 있다. 이 때,

- 공집합이 아닌 lower set $I$가 ideal인 것은 임의의 $x,y\in I$에 대하여 $x\vee y\in I$인 것과 동치이다.
- 공집합이 아닌 upper set $F$가 filter인 것은 임의의 $x,y\in F$에 대하여 $x\wedge y\in F$인 것과 동치이다.

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> 어떠한 집합 $A$가 주어졌다 하자. 그럼 $\mathcal{P}(A)$에 자연스러운 order relation $\subseteq$을 주면 $\mathcal{P}(A)$는 lattice가 되며 특히 임의의 $X,Y\in\mathcal{P}(A)$에 대하여

$$X\vee Y=X\cup Y,\qquad X\wedge Y=X\cap Y$$

가 성립한다. $\mathcal{P}(A)$에서는 추가적으로 두 연산 $\vee$와 $\wedge$가 다음의 분배법칙

$$X\vee(Y\wedge Z)=(X\vee Y)\wedge(X\vee Z),\qquad X\wedge(Y\vee Z)=(X\wedge Y)\vee(X\wedge Z)$$

을 만족한다.

</div>

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> Lattice $A$가 주어졌다 하고, $I$와 $F$가 각각 $E$의 proper ideal과 proper filter라 하자. $I$가 *prime ideal*이라는 것은 임의의 $x,y\in A$에 대하여 $x\wedge y\in I$이면 반드시 $x\in I$ 혹은 $y\in I$가 성립하는 것이다. 비슷하게 $F$가 *prime filter*라는 것은 임의의 $x,y\in A$에 대하여 $x\vee y\in F$이면 반드시 $x\in F$ 혹은 $y\in F$가 성립하는 것이다. ([\[대수적 구조\] §분수체, ⁋명제 8](/ko/math/algebraic_structures/field_of_fractions#prop8))

</div>

혹은, $I$가 prime ideal이라는 것은 $A\setminus I$가 filter라는 것으로 정의하여도 동등한 정의를 얻는다. 

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> 두 연산 $\vee$와 $\wedge$ 사이의 분배법칙이 성립하는 lattice $A$가 주어졌다 하자. 그럼 임의의 maximal ideal은 prime ideal이고 임의의 maximal filter는 prime filter이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

Maximal ideal $I$에 대해, $x\wedge y\in I$라 하자. 결론에 반하여 $x,y\not\in I$라 하고, 새로운 집합 $J$를 <phrase>$x\wedge z\in I$이도록 하는 모든 $z$들의 집합</phrase>이라 하자. 

1. 만일 $z_1,z_2\in J$라면 $x\wedge (z_1\vee z_2)=(x\wedge z_1)\vee(x\wedge z_2)\in I$가 성립하므로, $z_1\vee z_2\in J$이다. 
2. 만일 $z\in J$이고 $z'\leq z$라면 $z'\in J$이다. $(x\wedge z')\vee (x\wedge z)=x\wedge (z'\vee z)=x\wedge z$이므로 $x\wedge z'\leq x\wedge z$인데, $x\wedge z\in I$이므로 $x\wedge z'$ 또한 $I$의 원소여야 하기 때문이다.
3. 특별히 $x\not\in J$이고 $y\in J$임은 자명하다.

따라서 $J$는 $I$를 strict하게 포함하는 proper ideal이 되므로, 이는 $I$의 maximality에 모순이다. 비슷하게 임의의 maximal filter가 prime이라는 것을 보일 수 있다.

</details>


특별히 maximal filter를 *ultrafilter*라 부르기도 한다. 


두 ordered set $A,B$에 대해 증가함수 $f:A\rightarrow B$를 생각하자. 또, $B$의 임의의 lower set $Y$가 주어졌다 하고 $X=f^{-1}(Y)$이라 하자. 만일 어떤 $y\in A$에 대해 적당한 $x\in X$가 존재하여 $y\leq x$라면 $f(y)\leq f(x)$이고, $Y$는 lower set이므로 $f(y)\in Y$이 성립하여 $y\in X$이다. 즉, lower set의 preimage $X$ 또한 lower set이 된다. 

## Galois connection

지금부터 소개할 Galois connection은 그 이름에서부터 짐작할 수 있듯 field extension에 대한 갈루아 이론으로부터 나온 것이지만, 이를 추상화하여 ordered set 두 개 사이의 관계로 생각할 수 있으며, 이 추상화는 많은 분야에서 유용하게 사용된다. 

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> 두 ordered set $A,B$가 주어졌다 하자. 

1. 두 증가함수 $F:A\rightarrow B$와 $G:B\rightarrow A$가 임의의 $a\in A$, $b\in B$에 대해 다음의 조건

    $$F(a)\leq b\iff a\leq G(b)$$

    을 만족한다 하자. 그럼 $F$를 $G$의 *lower adjoint*, $G$를 $F$의 *upper adjoint*라 부르며, 이 때 쌍 $(F,G)$를 $A$와 $B$ 사이의 *monotone Galois connection<sub>갈루아 연결</sub>*이라 부른다.
2. 두 감소함수 $F:A\rightarrow B$와 $G:B\rightarrow A$가 임의의 $a\in A$, $b\in B$에 대해 다음의 조건

    $$b\leq F(a)\iff a\leq G(b)$$

    을 만족한다 하자. 그럼 $F$와 $G$를 각각의 *polarity*라 부르며, 이 때 쌍 $(F,G)$를 $A$와 $B$ 사이의 *antitone Galois connection<sub>쌍대 갈루아 연결</sub>*이라 부른다.
</div>

어떤 경우이건 간에, 함수 $G\circ F:A\rightarrow A$는 $a\leq G(F(a))$를 항상 만족한다. 우선 monotone Galois connection의 경우 

$$a\leq G(F(a))\iff F(a)\leq F(a)$$

인데 후자가 항상 참이 되며, antitone Galois connection의 경우도 마찬가지이다. 반면 $F\circ G$는 monotone인지 antitone인지에 따라 달라지는데, monotone Galois connection에 대해서는

$$F(G(b))\leq b\iff G(b)\leq G(b)$$

인데 후자가 항상 참이므로 $F(G(b))\leq b$가 성립하며, antitone Galois connection에 대해서는

$$b\leq F(G(b))\iff G(b)\leq G(b)$$

이므로 $b\leq F(G(b))$가 항상 성립한다. 

한편, $G\circ F$와 $F\circ G$는 두 증가함수의 합성이거나, 두 감소함수의 합성이므로 어떤 경우이든 증가함수가 되어야 한다.

남은 글에서는 편의상 우리는 $G\circ F$와 $F\circ G$를 각각 $GF$와 $FG$로 줄여쓰기로 하자.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> 두 ordered set $A,B$와 이들 사이의 monotone Galois connection $F:A\rightarrow B$, $G:B\rightarrow A$이 주어졌다 하자. 임의의 $y\in B$에 대하여 $GFG(y)=G(y)$가 항상 성립한다. 

만일 이들이 antitone Galois connection이라면, 임의의 $x\in A$와 $y\in B$에 대해 $GFG(y)=G(y)$와 $FGF(x)=F(x)$가 모두 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선, $a\leq GF(a)$에 $a=G(y)$를 대입하면 $G(y)\leq GFG(y)$를 얻는다. 한편, 우리는 $FG$가 임의의 $b\in B$에 대해 $FG(b)\leq b$를 만족한다는 것을 보였고 $G$는 증가함수이므로 $GFG(y)\leq G(y)$ 또한 얻는다. 따라서 $GFG(y)=G(y)$가 성립한다.

한편, 쌍 $(F,G)$가 antitone Galois connection인 경우, $G(y)\leq GFG(y)$인 것은 위와 동일하게 보일 수 있다. 또 임의의 $b\in B$에 대해 $b\leq FG(b)$가 항상 성립하고, $G$는 감소함수이므로 $G(y)\geq GFG(y)$가 다시 성립하므로 $GFG(y)=G(y)$이다. $FGF(x)=F(x)$는 $F$, $G$의 역할을 바꾸면 쉽게 증명된다.

</details>

다음 정의는 위상수학 못지않게 lattice theory에서도 중요하게 사용된다.

<div class="definition" markdown="1">

<ins id="def8">**정의 8**</ins> Ordered set $A$에 대하여, 함수 $f:A\rightarrow A$가 *closure operator<sub>폐포 연산자</sub>*라는 것은 다음의 세 조건이 모두 성립하는 것이다.

1. 임의의 $x\in A$에 대해 $x\leq f(x)$가 성립한다.
2. 임의의 $x\in A$에 대해 $f(x)=f(f(x))$.
3. 만일 $x\leq y$라면, $f(x)\leq f(y)$.

이 때, $x$가 *closed*라는 것은 $f(x)=x$인 것이다.

</div>

Antitone Galois connection을 고정하자. [명제 7](#prop7)의 결과인 $GFG(y)=G(y)$로부터, 임의의 $x\in A$에 대하여 $y=F(x)$를 대입하면

$$GFGF(x)=GF(x)$$

이 성립한다. 따라서 함수 $GF$는 위의 모든 조건을 만족하므로 closure operator이다. 마찬가지로 antitone Galois connection에서는 $FG$ 또한 closure operator가 된다. 

정의에 의하여, $x,y$가 긱긱 $GF$와 $FG$에 대해 closed라는 것은 각각 $GF(x)=x$, 그리고 $FG(y)=y$가 성립한다는 것이다. 우리는 [명제 7](#prop7)로부터 $F$와 $G$의 image에 속한 원소들은 모두 closed라는 것을 안다. 거꾸로 임의의 원소 $x$가 $GF$에 대해 closed라면 $GF(x)=x$로부터 $x$가 $G$의 image에 속한다는 것을 알고, 비슷하게 $FG$에 대한 명제 또한 증명할 수 있다.

우리는 이 과정을 통해 ordered set $A,B$ 사이의 Galois connection에 대해, closed subset들의 모임 $A'\subseteq A$, $B'\subseteq B$를 만들 수 있으며, $F$와 $G$를 이 모임에 제한한 것이 잘 정의된다. 뿐만 아니라 이들 $F\|\_{A'}$와 $G\|\_{B'}$는 일대일 대응이며, *anti-isomorphism*이 된다. 이들을 특별히 *Galois correspondence<sub>갈루아 대응</sub>*라 부른다.


---
**참고문헌**

**[Bou]** N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.
**[Wikipedia]** [Galois connection](https://en.wikipedia.org/wiki/Galois_connection)

---

[^1]: Upper set을 *upward closed set*, lower set을 *downward closed set*이라 부르기도 한다.
