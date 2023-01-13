---

title: "서수들 사이의 순서관계"
excerpt: "서수들의 순서관계와 기수의 엄밀한 정의"

categories: [Math / Set Theory]
permalink: /ko/math/set_theory/order_relations_between_ordinals
header:
    overlay_image: /assets/images/Math/Set_Theory/Order_relations_between_ordinals.png
    overlay_filter: 0.5
sidebar: 
    nav: "set_theory-ko"

date: 2022-11-29
last_modified_at: 2022-11-29
weight: 22

---

## Ordinal들 사이의 순서관계

임의의 ordinal은 정의에 의해 well-ordered set이다. 뿐만 아니라, 그 역 또한 성립한다고 할 수 있다.

<div class="proposition" markdown="1">

<ins id="pp1">**명제 1**</ins> $A,B$가 두 well-ordered set들이라 하자. 그럼 적어도 다음 중 하나가 성립한다.
1. $A$에서 $B$의 segment로의 order isomorphism이 존재하거나,
2. $B$에서 $A$의 segment로의 order isomorphism이 존재한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$\mathcal{F}$를 $A$의 segment에서 $B$의 segment로의 isomorphism들의 집합이라 하자. 우선 우리는 $\mathcal{F}$가 inductive임을 보인다.

$\mathcal{F}$의 totally ordered subset $\mathcal{G}$가 주어졌다고 하자. 그럼 $u\in\mathcal{G}$들의 정의역을 모두 합집합하여 집합 $S$를 만들 수 있다. 이 집합 $S$는 $A$의 segment들의 합집합이므로 다시 $A$의 segment이다. 한편, $\fun(A,B)$를 $A$의 부분집합에서 $B$로의 함수들의 모임이라 하자. 그럼 이 집합이 함수의 확장에 대해 inductive하다는 것은 자명하다. 이제 $\bigcup\mathcal{G}$는 $A$의 부분집합에서 $B$의 부분집합의 함수들이므로, $\mathcal{G}$의 $\fun(A,B)$에서의 least upper bound를 $v$라 하자. 그럼 $v(S)$는 $u\in\mathcal{G}$들의 치역의 합집합이므로 $F$의 segment가 되며, 임의의 $x, y$에 대하여 $x$와 $y$를 둘 다 포함하는 $u\in \mathcal{G}$를 골라오면

$$v(x)=u(x) < u(y)=v(y)$$
  
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

<ins id="thm2">**정리 2**</ins> 임의의 well-ordered set은 어떤 유일한 ordinal과 order isomorphic하다.

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

## Cardinal number의 정의

이제 우리는 cardinality의 엄밀한 정의를 소개한다. 다만, 우리가 본격적으로 cardinal에 대해 다루는 것은 (엄밀하지 않은 정의를 사용하는) 다음 글이 될 것이며, 지금 할 내용은 어디까지나 <em_ko>엄밀한 방법으로 집합의 크기를 정의</em_ko>하는 것에 초점을 맞춘다. 예를 들어 이들 간의 연산 등을 정의하는 것은 엄밀하지 않은 다음 글에서의 정의를 사용할 것이며, 혹시 이들을 엄밀하게 정의하고 싶다면 **[HJJ]**의 7장과 9장을 참고.

우리가 다음 글에서 생각할 cardinality의 정의는 집합들 사이의 전단사함수를 이용해 집합의 크기를 정의한다. 예를 들어, 원소 두 개짜리 집합들 간에는 전단사함수가 존재하므로 이들의 크기가 같다고 생각할 것이다. 이러한 정의는 어떻게 보면 ordinal과는 잘 맞지 않는데, 예를 들어 $\omega$와 $\omega+1$은 분명 ordinal 측면에서는 다른 집합이지만 이들 간의 (순서를 무시하는) 전단사함수는 존재하기 때문이다. 이들을 합치려면 다음과 같이 정의하면 된다.

<div class="definition" markdown="1">

<ins id="df3">**정의 3**</ins> 임의의 집합 $A$에 대하여, $A$의 어떠한 부분집합과도 전단사함수가 존재하지 않는 가장 작은 ordinal number를 $A$의 *Hartogs number*라고 부르고, $h(A)$로 표기한다. 

</div>

Successor ordinal들은 이들의 <em_ko>이전</em_ko> ordinal과의 전단사함수가 존재하므로, 이들은 어떤 집합의 Hartogs number가 될 수 없다. 그렇다고 limit ordinal을 살펴보려 해도, $\omega$나 $\omega\cdot 2$나 크기 자체는 같아야 한다. 때문에 다음의 개념을 새롭게 정의한다.

<div class="definition" markdown="1">

<ins id="df4">**정의 4**</ins> Ordinal $\alpha$가 *initial ordinal*이라는 것은, $\beta&lt;\alpha$를 만족하는 모든 $\beta$에 대해, $\beta$와 $\alpha$ 사이의 전단사함수가 존재하지 않는 것이다.

</div>

그렇다면 임의의 집합의 크기는 initial ordinal의 크기로 표현할 수 있다. 어떤 집합 $X$가 주어졌을 때, 여기에 well-order를 주어 ordinal $\alpha$를 택한 다음, 이와 같은 크기를 갖는 ordinal들 중 가장 작은 것을 (well-ordering에 의해) 뽑아오면 된다. 

우리는 ordinal number를 이용해서 cardinal number를 정의할 수 있다. 무한한 initial ordinal들을 모아둔 다음, 여기에 순서대로 $0, 1, \ldots$번째 순서를 붙인다고 생각하자. 즉, $\omega_0$은 0번째 initial ordinal, 즉 $\omega$와 같고, 그 후로 집합의 크기가 strict하게 커지는 $\omega_1,\omega_2,\ldots$와 같이 정의하는 것이다. Cardinal을 정의할 때에는, 이들을 (ordinal을 정의하는 문자인 $\omega$ 대신) $\aleph_\alpha$와 같이 적는 것이 보통이다.  

---
**참고문헌**

**[HJJ]** K. Hrbacek, T.J. Jeck, and T. Jech. *Introduction to Set Theory*. Lecture Notes in Pure and Applied Mathematics. M. Dekker, 1978. 

---