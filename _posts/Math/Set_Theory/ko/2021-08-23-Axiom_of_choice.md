---

title: "선택공리"
excerpt: "선택공리와 그 동치들"

categories: [Math / Set Theory]
permalink: /ko/math/set_theory/axiom_of_choice
header:
    overlay_image: /assets/images/Set_theory/Axiom_of_choice.png
    overlay_filter: 0.5
sidebar: 
    nav: "set_theory-ko"

date: 2021-08-23
last_modified_at: 2022-04-14
weight: 21

---

이번 글에서는 드디어 선택공리를 소개한다. 이후 이전 글에서 다뤘던 ordinal number들 사이의 순서관계를 정의한다.


## 선택공리와 그 동치들

**The Axiom of Choice.** 임의의 집합은 choice function을 갖는다.
{: .misc}

여기에서 choice function이란 집합들의 모임 $\mathcal{S}$ 위에서 정의된 함수로, $f(X)\in X$가 모든 $X\in\mathcal{S}$에 대해 성립한다. 즉, $f$는 각각의 집합 $X$마다 원소를 하나씩 뽑아오는 함수이다. 우리는 사실 알게 모르게 계속해서 이 공리를 써 왔는데, 임의의 집합에서 원소를 하나 뽑은 경우가 모두 그러하다. 

이 다음에 우리는

> 임의의 well-ordered set은 어떠한 ordinal과 order isomorphic하다

는 것을 증명한다. [§서수와 정렬집합, ⁋예시 3](/ko/math/set_theory/ordinals#ex3)에서 보았듯 많은 ordered set은 well-ordered set이 아니므로 위의 명제의 조건이 매우 까다로운 것처럼 보이지만, 사실 선택공리를 잘 사용하면 다음의 정리를 보일 수 있다.

<ins id="thm1">**정리 1. (Zermelo)**</ins> 임의의 집합 $A$에 well-ordering을 줄 수 있다.
{: .proposition}

이 정리가 뜻하는 바는 집합 $A$가 원래 순서가 부여되어 있던 ordered set이든, 혹은 아무런 정보도 없는 그냥 집합이든 간에 관계 없이, 새로운 order relation을 부여할 수 있다는 것이다. 예를 들어 $(\mathbb{R},\leq)$는 well-ordered set이 아니지만, 그럼에도 불구하고 이 집합 $\mathbb{R}$을 well-ordered set으로 만드는 적당한 order relation $\preceq$을 정의할 수 있다.

<div class="proposition" markdown="1">

<ins id="lem2">**보조정리 2 (Tarski-Bourbaki)**</ins> $A$가 집합이고, $\mathcal{S}\subset\mathcal{P}(A)$, $p:\mathcal{S}\rightarrow A$가 $p(X)\not\in X$를 만족한다고 하자. 그럼 well-ordered subset $(M,\leq)$가 존재하여 다음의 조건들을 만족한다.

1. 모든 $x\in X$에 대하여, $S_x\in\mathcal{S}$이고 $p(S_x)=x$이다.
2. $M\not\in\mathcal{S}$.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$\mathcal{M}$을 다음의 조건을 만족하는 관계들 $R\subseteq A\times A$의 모임이라 하자.

1. $G$는 $R=\pr\_1R$에서의 well-ordering이다.
2. 각각의 $x\in U$에 대하여, $S_x\in\mathcal{S}$이고 $p(S_x)=x$이다.

우리는 $\mathcal{M}$의 원소 $G$마다 정의된 $U=\pr\_1G$가 [§정렬집합의 성질들, ⁋명제 4](/ko/math/set_theory/well_ordering#pp4)의 조건을 만족함을 보일 것이다. 이를 위해 임의의 $U$, $U'$에 대하여 $U$가 $U'$의 segment이거나 그 반대라는 것을 보이자.

$G$, $G'\in \mathcal{M}$가 임의로 주어졌고 $U$, $U'$가 그 정의역이라 하자. 이 때, (1) $x$를 끝점으로 갖는 segment가 $U$와 $U'$에서 동일한 집합을 나타내고, (2) 그 segment 위에서의 order가 $G$와 동일하도록 하는, $x\in U\cap U'$들을 모아 그 집합을 $V$라 하자. 만일 $x\in V$이고 $y\in U$가 $y\leq x$를 만족한다면, $U$와 $U'$ 모두에서 $y\in S_x$이다. 또, $U$에서 $y$보다 작은 원소는 $U'$에서도 $y$보다 작다. 따라서 $y\in V$이고, $V$는 $U$의 segment이다.

이제 $U$와 $U'$가 원하는 조건을 만족하기 위해서는, $U=V$이거나 반대로 $U'=V$임만 보이면 충분하다. $V\neq U$이고 $V\neq U'$라 가정하자. 그럼 $U\setminus V$와 $U'\setminus V$의 least element $x$와 $x'$에 대하여, $V=S_x=S\_{x'}$가 $U$와 $U'$ 각각에서 성립한다. 그런데 두 번째 조건에 의하여 $V\in\mathcal{S}$이므로 $x=p(S_x)=p(V)=p(S\_{x'})=x'$이고, 따라서 $x\in V$이다.

이제 [§정렬집합의 성질들, ⁋명제 4](/ko/math/set_theory/well_ordering#pp4)를 활용하여 well-ordered set $M=\bigcup\_{G\in\mathcal{M}}\pr\_1G$를 얻는다. 자명하게 $M\in\mathcal{M}$이므로 $M$은 명제의 성질 1을 만족한다. 만일 $M\in\mathcal{S}$라면 $\mathcal{S}$의 조건에서 $p(M)\not\in M$이 된다. 이제 $M$에 greatest element $a=p(M)$를 추가하면, 우리는 또 다른 well-ordered set $M'=M\cup\\{a\\}$ ($S_a=M$)를 얻는다. $S_a=M\in\mathcal{S}$이고 $p(S_a)=a$이므로, $M'$은 $\mathcal{M}$의 원소가 되어 $M$의 최대성에 모순이다. 따라서 명제의 성질 2도 성립한다.
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

이제 $\mathcal{S}$를 $A$의 부분집합 중 strict upper bound를 갖는 것들만 모아둔 집합이라 하고, $p:\mathcal{S}\rightarrow A$가 strict upper bound를 뽑아오는 함수라고 하자. 즉 모든 $S$에 대하여 $p(S)$는 $S$의 strict upper bound이다. $p(S)\not\in S$이므로, 우리는 [§정렬집합의 성질들, ⁋보조정리 5](/ko/math/set_theory/well_ordering#lem5)에 의해 well-ordered subset $M$을 얻는다. 또, 이 well-ordering은 $A$의 order relation를 $M$ 위로 제한한 것과 같다. 만일 $x&lt;y$가 $M$ 안에서 성립한다고 하면 이는 $x\in S_y$와 동치인데 ($S_y$는 $M$에서의 segment), $p(S_y)=y$이면 $y$가 $S_y$의 strict upper bound가 된다. (여기서의 $S_y$는 $M$의 부분집합이므로, segment가 아니지만 그냥 부분집합으로서 strict upper bound $y$를 갖는다.) 특히 $x\in S_y$로부터, $x&lt;y$가 $A$에서도 성립한다. $M$은 이제 well-ordered이므로, 가정에 의해 $M$은 upper bound $m$을 갖는다. 그런데 정의에 의해 $M$은 strict upper bound를 갖지 못하므로, $m\in M$이고, 만일 어떤 $m'$이 $m\leq m'$을 만족한다면 $m=m'$이 된다. 그렇지 않다면 $m'$이 $M$의 strict upper bound가 되므로.
</details>

완결성을 위해 간단하게 세 가지 명제, 그러니까 선택공리, Zermelo's theorem, Zorn's lemma가 동치임을 보이자. 우리는 Zermelo's theorem과 Zorn's lemma를 보일 때 선택공리를 썼으므로, 이제 Zermelo's theorem과 Zorn's lemma 각각을 이용해서 choice function을 만들어내면 된다. 

우선 Zermelo's theorem을 가정한다면 모든 집합은 well-ordered될 수 있으므로, 어떠한 $S\in\mathcal{P}(A)\setminus \\{\emptyset\\}$에 대해서도 least element가 존재한다. 이제 $p(S)$를 $S$의 least element로 정의하면 $p$가 원하는 choice function이다.

이제 Zorn's lemma를 가정하고, 집합 $A$의 choice function을 만들자. 우선 $A$의 어떤 부분집합 $X$ 위에 정의된 choice function들을 모아 이를 $\mathcal{F}$라 하자. 최소한 $X=\\{a\\}$ 위에서는 choice function이 존재하므로 $\mathcal{F}$는 공집합이 아니다. 이제 $\mathcal{C}$의 각 원소들은 집합이므로, $\subseteq$에 의해 순서가 주어진다. 

이제 $\mathcal{F}$의 totally ordered subset $\mathcal{C}$가 주어졌다 하자. 그럼 $\bigcup\_{X\in\mathcal{C}} F_X$는 정의역 $\mathcal{P}(\bigcup\_{X\in\mathcal{C}} X)$를 갖는 함수이므로, 이 함수들의 모임의 upper bound가 된다. 따라서 Zorn's lemma에 의해 어떤 maximal element가 존재한다. 이를 $F$라 하고 $\mathcal{P}(B)$를 정의역이라 하자. 만일 $x\in A\setminus B$라면, $B$에 $x$를 추가하고 $\tilde{f}$를

$$\tilde{f}(X)=\begin{cases}f(X)&\text{if }x\not\in X\\ x&\text{if }x\in X\end{cases}$$

로 정의함으로써 $F$를 확장하는 choice function $\tilde{f}$를 얻는다. 이는 $F$의 maximality에 모순이므로 $A\setminus B=\emptyset$, 즉 $F$는 $A$의 choice function이다.

---
**참고문헌** 

**[HJJ]** K. Hrbacek, T.J. Jeck, and T. Jech. <i>Introduction to Set Theory</i>. Lecture Notes in Pure and Applied Mathematics. M. Dekker, 1978.  
**[Bou]** N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---
