---

title: "선택공리"
excerpt: "선택공리와 동치들, 서수들의 순서관계 마무리"

categories: [Math / Set Theory]
permalink: /ko/math/set_theory/axiom_of_choice
header:
    overlay_image: /assets/images/Set_theory/Ordinals.png
    overlay_filter: 0.5
sidebar: 
    nav: "set-ko"

date: 2021-08-23
last_modified_at: 2022-04-14
weight: 16

---

이 글은 현재 수정중입니다.
{: .notice--warning}


이번 글에서는 드디어 선택공리를 소개한다. 이후 이전 글에서 다뤘던 ordinal number들 사이의 순서관계를 정의한다.


## 선택공리와 그 동치들

**The Axiom of Choice.** 임의의 집합은 choice function을 갖는다.
{: .misc}

여기에서 choice function이란 집합들의 모임 $\mathcal{S}$ 위에서 정의된 함수로, $f(X)\in X$가 모든 $X\in\mathcal{S}$에 대해 성립한다. 즉, $f$는 각각의 집합 $X$마다 원소를 하나씩 뽑아오는 함수이다. 우리는 사실 알게 모르게 계속해서 이 공리를 써 왔는데, 임의의 집합에서 원소를 하나 뽑은 경우가 모두 그러하다. 예컨대 [§순서쌍, 명제 9](/ko/math/set_theory/ordered_pair#pp9)의 증명에서, 공집합이 아닌 집합 $B'$는 어떤 원소를 갖는 것은 사실이지만, 이 중 하나를 <em_ko>뽑아서</em_ko> 그 원소를 $b'$라 이름붙이는 것은 선택공리의 도움이 필요하다.

이 다음에 우리는

> 임의의 well-ordered set은 어떠한 ordinal과 order isomorphic하다

는 것을 증명한다. [§서수와 정렬집합<sup>†</sup>, 예시 3](/ko/math/set_theory/ordinals#ex3)에서 보았듯 많은 ordered set은 well-ordered set이 아니므로 위의 명제의 조건이 매우 까다로운 것처럼 보이지만, 사실 선택공리를 잘 사용하면 다음의 정리를 보일 수 있다.

<ins id="thm1">**정리 1. (Zermelo)**</ins> 임의의 집합 $A$에 well-ordering을 줄 수 있다.
{: .proposition}

이 정리가 뜻하는 바는 집합 $A$가 원래 순서가 부여되어 있던 ordered set이든, 혹은 아무런 정보도 없는 그냥 집합이든 간에 관계 없이, 새로운 order relation을 부여할 수 있다는 것이다. 예를 들어 $(\mathbb{R},\leq)$는 well-ordered set이 아니지만, 그럼에도 불구하고 이 집합 $\mathbb{R}$을 well-ordered set으로 만드는 적당한 order relation $\preceq$을 정의할 수 있다.

<div class="proposition" markdown="1">

<ins id="lem2">**보조정리 2 (Tarski-Bourbaki)**</ins> $A$가 집합이고, $\mathcal{S}\subset\mathcal{P}(A)$, $p:\mathcal{S}\rightarrow A$가 $P(X)\not\in X$를 만족한다고 하자. 그럼 well-ordered subset $(M,\leq)$가 존재하여 다음의 조건들을 만족한다.

1. 모든 $x\in X$에 대하여, $S_x\in\mathcal{S}$이고 $p(S_x)=x$이다.
2. $M\not\in\mathcal{S}$.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$\mathcal{M}$가 다음의 조건을 만족하는 graph들 $G\subseteq A\times A$의 모임이라 하자.

1. $G$는 $U=\operatorname{pr}\_1G$에서의 well-ordering이다.
2. 각각의 $x\in U$에 대하여, $S_x\in\mathcal{S}$이고 $p(S_x)=x$이다.

우리는 $\mathcal{M}$의 원소 $G$마다 정의된 $U=\operatorname{pr}\_1G$가 [§정렬집합의 성질들<sup>†</sup>, 명제 1](/ko/math/set_theory/well_ordering#pp1)의 조건을 만족함을 보일 것이다. 이를 위해 임의의 $U$, $U'$에 대하여 $U$가 $U'$의 segment이거나 그 반대라는 것을 보이자.

$G$, $G'\in \mathcal{M}$가 임의로 주어졌고 $U$, $U'$가 그 정의역이라 하자. 이 때, (1) $x$를 끝점으로 갖는 segment가 $U$와 $U'$에서 동일한 집합을 나타내고, (2) 그 segment 위에서의 order가 $G$와 동일하도록 하는, $x\in U\cap U'$들을 모아 그 집합을 $V$라 하자. 만일 $x\in V$이고 $y\in U$가 $y\leq x$를 만족한다면, $U$와 $U'$ 모두에서 $y\in S_x$이다. 또, $U$에서 $y$보다 작은 원소는 $U'$에서도 $y$보다 작다. 따라서 $y\in V$이고, $V$는 $U$의 segment이다.

이제 $U$와 $U'$가 원하는 조건을 만족하기 위해서는, $U=V$이거나 반대로 $U'=V$임만 보이면 충분하다. $V\neq U$이고 $V\neq U'$라 가정하자. 그럼 $U\setminus V$와 $U'\setminus V$의 least element $x$와 $x'$에 대하여, $V=S_x=S\_{x'}$가 $U$와 $U'$ 각각에서 성립한다. 그런데 두 번째 조건에 의하여 $V\in\mathcal{S}$이므로 $x=p(S_x)=p(V)=p(S\_{x'})=x'$이고, 따라서 $x\in V$이다.

이제 [§정렬집합의 성질들<sup>†</sup>, 명제 1](/ko/math/set_theory/well_ordering#pp1)을 활용하여 well-ordered set $M=\bigcup\_{G\in\mathcal{M}}\operatorname{pr}\_1G$를 얻는다. 자명하게 $M\in\mathcal{M}$이므로 $M$은 명제의 성질 1을 만족한다. 만일 $M\in\mathcal{S}$라면 $\mathcal{S}$의 조건에서 $p(M)\not\in M$이 된다. 이제 $M$에 greatest element $a=p(M)$를 추가하면, 우리는 또 다른 well-ordered set $M'=M\cup\\{a\\}$ ($S_a=M$)를 얻는다. $S_a=M\in\mathcal{S}$이고 $p(S_a)=a$이므로, $M'$은 $\mathcal{M}$의 원소가 되어 $M$의 최대성에 모순이다. 따라서 명제의 성질 2도 성립한다.
</details>

<details class="proof--alone" markdown="1">
<summary>정리 1의 증명</summary>

$\mathcal{S}=\mathcal{P}(A)\setminus\\{A\\}$라 하자. 또, 함수 $p:\mathcal{S}\rightarrow A$의 값 $P(X)$를 $A\setminus X$의 어떤 원소로 정의하자. (즉, $P$는 choice function이다.) 그럼 $P(X)\not\in X$이다. 이제 앞선 보조정리에 의해 어떤 well-ordered subset $M\subseteq A$가 존재하여 위 보조정리의 1과 2를 만족한다. 특히, $M\not\in\mathcal{S}$인데, 이를 만족할 수 있는 유일한 $M$은 $A$ 뿐이다.
</details>

이제 가장 범용적으로 쓰이는 선택공리의 동치인 Zorn's lemma를 소개할 차례다. 우선 다음을 정의하자.

<ins id="df3">**정의 3**</ins> Ordered set $A$가 *inductive*하다는 것은 임의의 totally ordered subset이 upper bound를 갖는 것이다.
{: .definition}

Inductive set은 저자에 따라 전혀 다른 개념을 뜻하기도 하므로 주의가 필요하다. Totally ordered subset은 *chain*이라 부르기도 한다. 

<ins id="thm4">**정리 4 (Zorn's lemma)**</ins> 임의의 inductive set은 maximal element를 갖는다.
{: .proposition}

모든 well-ordered set은 totally ordered set이기도 하므로, 만일 우리가 다음의 정리를 증명할 수 있다면 위의 정리는 자명하다.

<ins id="pp5">**명제 5**</ins> 모든 well-ordered subset이 bounded above인 ordered set $A$는 maximal element를 갖는다.
{: .proposition}

<details class="proof" markdown="1">
<summary>증명</summary>

만약 $v$가 $X\subseteq A$의 upper bound이고 $v\not\in X$라면 $v\in A$를 $X$의 *strict upper bound*라 부르자. 

이제 $\mathcal{S}$를 $A$의 부분집합 중 strict upper bound를 갖는 것들만 모아둔 집합이라 하고, $p:\mathcal{S}\rightarrow A$가 strict upper bound를 뽑아오는 함수라고 하자. 즉 모든 $S$에 대하여 $p(S)$는 $S$의 strict upper bound이다. $p(S)\not\in S$이므로, 우리는 [§정렬집합의 성질들<sup>†</sup>, 보조정리 5](/ko/math/set_theory/well_ordering#lem5)에 의해 well-ordered subset $M$을 얻는다. 또, 이 well-ordering은 $A$의 order relation를 $M$ 위로 제한한 것과 같다. 만일 $x&lt;y$가 $M$ 안에서 성립한다고 하면 이는 $x\in S_y$와 동치인데 ($S_y$는 $M$에서의 segment), $p(S_y)=y$이면 $y$가 $S_y$의 strict upper bound가 된다. (여기서의 $S_y$는 $M$의 부분집합이므로, segment가 아니지만 그냥 부분집합으로서 strict upper bound $y$를 갖는다.) 특히 $x\in S_y$로부터, $x&lt;y$가 $A$에서도 성립한다. $M$은 이제 well-ordered이므로, 가정에 의해 $M$은 upper bound $m$을 갖는다. 그런데 정의에 의해 $M$은 strict upper bound를 갖지 못하므로, $m\in M$이고, 만일 어떤 $m'$이 $m\leq m'$을 만족한다면 $m=m'$이 된다. 그렇지 않다면 $m'$이 $M$의 strict upper bound가 되므로.
</details>

완결성을 위해 간단하게 세 가지 명제, 그러니까 선택공리, Zermelo's theorem, Zorn's lemma가 동치임을 보이자. 우리는 Zermelo's theorem과 Zorn's lemma를 보일 때 선택공리를 썼으므로, 이제 Zermelo's theorem과 Zorn's lemma 각각을 이용해서 choice function을 만들어내면 된다. 

우선 Zermelo's theorem을 가정한다면 모든 집합은 well-ordered될 수 있으므로, 어떠한 $S\in\mathcal{P}(A)\setminus \\{\emptyset\\}$에 대해서도 least element가 존재한다. 이제 $p(S)$를 $S$의 least element로 정의하면 $p$가 원하는 choice function이다.

이제 Zorn's lemma를 가정하고, 집합 $A$의 choice function을 만들자. $A$의 부분집합 $X$에 대하여, $F_X$를 $X$를 정의역으로 갖는 choice function의 그래프라 하자. 포함관계에 의하여 order relation이 주어진 이 그래프들의 totally ordered subset $\mathcal{C}$에 대하여, $\bigcup\_{X\in\mathcal{C}} F_X$는 정의역 $\mathcal{P}(\bigcup\_{X\in\mathcal{C}} X)$를 갖는 함수이므로, 이 함수들의 모임의 upper bound가 된다. 따라서 Zorn's lemma에 의해 어떤 maximal element가 존재한다. 이를 $F$라 하고 $\mathcal{P}(B)$를 정의역이라 하자. 만일 $x\in A\setminus B$라면, $B$에 $x$를 추가하고 $\tilde{f}$를

$$\tilde{f}(X)=\begin{cases}f(X)&\text{if }x\not\in X\\ x&\text{if }x\in X\end{cases}$$

로 정의함으로써 $F$를 확장하는 choice function $\tilde{f}$를 얻는다. 이는 $F$의 maximality에 모순이므로 $A\setminus B=\emptyset$, 즉 $F$는 $A$의 choice function이다.

## Ordinal들 사이의 순서관계<sup>†</sup>

임의의 ordinal은 정의에 의해 well-ordered set이다. 뿐만 아니라, 그 역 또한 성립한다고 할 수 있다.

<div class="proposition" markdown="1">

<ins id="pp6">**명제 6**</ins> $A,B$가 두 well-ordered set들이라 하자. 그럼 적어도 다음 중 하나가 성립한다.
1. $A$에서 $B$의 segment로의 order isomorphism이 존재하거나,
2. $B$에서 $A$의 segment로의 order isomorphism이 존재한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$\mathcal{F}$를 $A$의 segment에서 $B$의 segment로의 isomorphism들의 집합이라 하자. 우선 우리는 $\mathcal{F}$가 inductive임을 보인다.

$\mathcal{F}$의 totally ordered subset $\mathcal{G}$가 주어졌다고 하자. 그럼 $u\in\mathcal{G}$들의 정의역을 모두 합집합하여 집합 $S$를 만들 수 있다. 이 집합 $S$는 $A$의 segment들의 합집합이므로 다시 $A$의 segment이다. 한편, $\operatorname{fun}(A,B)$를 $A$의 부분집합에서 $B$로의 함수들의 모임이라 하자. 그럼 이 집합이 함수의 확장에 대해 inductive하다는 것은 자명하다. 이제 $\bigcup\mathcal{G}$는 $A$의 부분집합에서 $B$의 부분집합의 함수들이므로, $\mathcal{G}$의 $\operatorname{fun}(A,B)$에서의 least upper bound를 $v$라 하자. 그럼 $v(S)$는 $u\in\mathcal{G}$들의 치역의 합집합이므로 $F$의 segment가 되며, 임의의 $x, y$에 대하여 $x$와 $y$를 둘 다 포함하는 $u\in \mathcal{G}$를 골라오면

$$v(x)=u(x)<u(y)=v(y)$$
  
에서 $v$는 $S$에서 $v(S)$로의 isomorphism이다. 따라서 $\mathcal{F}$는 inductive이다.

이제 Zorn's lemma에 의해 $\mathcal{F}$는 maximal element를 갖는다. 이를 $u_0$이라 하고, 이의 정의역을 $S_0$이라 하자. 우리는 $S_0=A$이거나 $u_0(S_0)=B$임을 보여야 한다. 

만일 그렇지 않다면, 어떤 $a\in A$와 $b\in B$가 존재하여 $S_0=(-\infty, a)$이고 $u_0(S_0)=(-\infty, b)$일 것이다. 이제 $u_0$에 $(a,b)$를 추가하면 $u_0$을 strict하게 확장하는 새로운 함수가 생기고, 이는 $u_0$의 maximality에 모순이므로 $S_0=A$이거나 $u_0(S_0)=B$이다.

</details>

앞서 말한 것과 같이 임의의 ordinal은 well-ordered set이므로, 위 명제에 의하면 임의의 well-ordered set을 어떤 ordinal의 initial segment와 order isomorphic한 segment로 볼 수 있는 길이 열렸다. 그러나, 이를 위해서는 다음의 새로운 공리를 도입해야 한다.

<div class="misc" markdown="1">

**The Axiom schema of Replacement.** $P(x,y)$가 

> 임의의 $x$에 대하여, $P(x,y)$를 성립하도록 하는 $y$가 항상 존재한다

를 만족하는 성질이라 하자. 그럼 임의의 집합 $A$에 대하여, 또 다른 집합 $B$가 존재하여, 

> $x\in A$마다, 적절한 $y\in B$가 존재하여 $P(x,y)$가 성립

하도록 할 수 있다.

</div>

위의 조건을 만족하는 $P$가 주어지면, 이를 $x$를 넣었을 때 $y$가 나오는 함수 $F$로 생각할 수도 있다. 다만 함수는 기본적으로 target이 정의된 상태에서 정의되었는데, 이 조건 $P$로 만들어지는 대응은 target에 대한 정보가 아무것도 없기 때문에 단일 공리 대신 axiom schema가 필요한 것이다. 어쨌든 replacement schema가 주어진다면 target $B$를 잘 정의해줄 수 있고, 이 때 $B$에 comprehension schema를 이용해 

> $(x,y)\in F$ for some $x$

조건을 걸어주면 $A$의 $F$를 통한 *image*를 동일하게 정의할 수 있게 된다.  

<div class="proposition" markdown="1">

<ins id="thm7">**정리 7**</ins> 임의의 well-ordered set은 어떤 유일한 ordinal과 order isomorphic하다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$A$가 well-ordered set이라 하고, 집합 $X$를

> $S_x$가 어떠한 ordinal과 order isomorphic하다

를 만족하는 $x\in A$들의 집합이라 하자. 임의의 ordinal은 자신을 제외한 ordinal과는 order isomorphic하지 않으므로, $X$에 속해있는 $x\in A$마다 유일한 ordinal $\alpha_x$를 지정해 줄 수 있다. 우리의 목표는 이러한 ordinal들을 모은 집합 $B$가 $A$와 order isomorphic한 ordinal이 된다는 것을 보이는 것인데, 그를 위해서는 이 집합이 존재한다는 것부터 우선 보여야 한다.  

이를 위해, 성질 $P(x,y)$를 다음과 같이 정의하자.

> (i) $x\in X$이고 $y$가 $S_x$와 order isomorphic한 ordinal이거나, 
> (ii) $x\not\in X$이고 $y=\emptyset$이다.

이 성질은, 앞서 말한 것과 같이 유일한 ordinal $y$를 지정하거나, 혹은 (마찬가지로 유일한) 공집합 $\emptyset$을 지정하므로, axiom schema of replacement를 사용할 수 있다. 이를 적용하면, $P$에 의해 정의되는 함수 $F$에 대하여 집합 $F(A)$가 존재한다는 것을 알 수 있다. 이 집합을 $B$라 하자. 

1. $B$는 ordinal들의 집합이므로, $\in$에 의해 well-ordering이 주어져있다. 
2. 임의의 $\alpha_x\in B$에 대하여, 만일 $\gamma\in\alpha_x$라면 $\alpha_x$와 $S_x$ 사이의 order isomorphism $\varphi$에 의한 inverse image $\varphi^{-1}(\gamma)\in S_x$를 생각할 수 있다. 이를 $c$라 하면, $\varphi$를 $S_c$로 제한한 함수가 $S_c$와 $\gamma$ 사이의 order isomorphism을 정의하므로 $B$의 정의에 의해 $\gamma\in B$이다. 

이상에서 $B$는 ordinal number임을 알 수 있다. 또, 2번 증명을 똑같이 적용한다면 임의의 $x\in X$에 대하여, 만일 $y&lt;x$라면 $y\in X$임도 보일 수 있다. 즉, $X$는 $A$의 segment이고, 따라서 $X=S_x$이거나 $X=A$이다. 

이제 $X=A$임을 보이기 위해, 결론을 부정하여 모순을 찾자. 우선 우리는 $f:X\rightarrow B$를 $f(x)=\alpha_x$로 정의할 수 있으며, 이 경우 $f$는 $B$와 $X$ 사이의 order isomorphism이 된다는 것을 확인할 수 있다. 그런데 만일 $X=S_x$였다면, $B$는 ordinal이므로, $S_x$가 ordinal $B$와 isomorphic하다는 이야기가 되므로, 정의에 의해 $x\in X$여야 한다. 이는 모순이므로, $X=A$이다. 

</details>

## Cardinal number의 정의<sup>†</sup>

이제 우리는 cardinality의 엄밀한 정의를 소개한다. 다만, 우리가 본격적으로 cardinal에 대해 다루는 것은 (엄밀하지 않은 정의를 사용하는) 다음 글이 될 것이며, 지금 할 내용은 어디까지나 <em_ko>엄밀한 방법으로 집합의 크기를 정의</em_ko>하는 것에 초점을 맞춘다. 예를 들어 이들 간의 연산 등을 정의하는 것은 엄밀하지 않은 다음 글에서의 정의를 사용할 것이며, 혹시 이들을 엄밀하게 정의하고 싶다면 **[HJJ]**의 7장과 9장을 참고.

우리가 다음 글에서 생각할 cardinality의 정의는 집합들 사이의 전단사함수를 이용해 집합의 크기를 정의한다. 예를 들어, 원소 두 개짜리 집합들 간에는 전단사함수가 존재하므로 이들의 크기가 같다고 생각할 것이다. 이러한 정의는 어떻게 보면 ordinal과는 잘 맞지 않는데, 예를 들어 $\omega$와 $\omega+1$은 분명 ordinal 측면에서는 다른 집합이지만 이들 간의 (순서를 무시하는) 전단사함수는 존재하기 때문이다. 이들을 합치려면 다음과 같이 정의하면 된다.

<div class="definition" markdown="1">

<ins id="df8">**정의 8**</ins> 임의의 집합 $A$에 대하여, $A$의 어떠한 부분집합과도 전단사함수가 존재하지 않는 가장 작은 ordinal number를 $A$의 *Hartogs number*라고 부르고, $h(A)$로 표기한다. 

</div>

Successor ordinal들은 이들의 <em_ko>이전</em_ko> ordinal과의 전단사함수가 존재하므로, 이들은 어떤 집합의 Hartogs number가 될 수 없다. 그렇다고 limit ordinal을 살펴보려 해도, $\omega$나 $\omega\cdot 2$나 크기 자체는 같아야 한다. 때문에 다음의 개념을 새롭게 정의한다.

<div class="definition" markdown="1">

<ins id="df9">**정의 9**</ins> Ordinal $\alpha$가 *initial ordinal*이라는 것은, $\beta&lt;\alpha$를 만족하는 모든 $\beta$에 대해, $\beta$와 $\alpha$ 사이의 전단사함수가 존재하지 않는 것이다.

</div>

그렇다면 임의의 집합의 크기는 initial ordinal의 크기로 표현할 수 있다. 어떤 집합 $X$가 주어졌을 때, 여기에 well-order를 주어 ordinal $\alpha$를 택한 다음, 이와 같은 크기를 갖는 ordinal들 중 가장 작은 것을 (well-ordering에 의해) 뽑아오면 된다. 

우리는 ordinal number를 이용해서 cardinal number를 정의할 수 있다. 무한한 initial ordinal들을 모아둔 다음, 여기에 순서대로 $0, 1, \ldots$번째 순서를 붙인다고 생각하자. 즉, $\omega_0$은 0번째 initial ordinal, 즉 $\omega$와 같고, 그 후로 집합의 크기가 strict하게 커지는 $\omega_1,\omega_2,\ldots$와 같이 정의하는 것이다. Cardinal을 정의할 때에는, 이들을 (ordinal을 정의하는 문자인 $\omega$ 대신) $\aleph_\alpha$와 같이 적는 것이 보통이다.  


---
**참고문헌** 

**[HJJ]** K. Hrbacek, T.J. Jeck, and T. Jech. <i>Introduction to Set Theory</i>. Lecture Notes in Pure and Applied Mathematics. M. Dekker, 1978.  
**[Bou]** N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---
