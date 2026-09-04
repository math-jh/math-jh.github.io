---
title: "멱등원과 곱분해"
description: "Idempotent과 orthogonal idempotent의 complete set을 정의하고, central idempotent이 환의 곱분해와 일대일대응함을 증명한 뒤, 이를 일반 환에서의 중국인의 나머지정리와 연결한다."
excerpt: "Central idempotent과 환의 곱분해, 그리고 일반 환에서의 중국인의 나머지정리"

categories: [Math / Ring Theory]
permalink: /ko/math/ring_theory/idempotents
sidebar: 
    nav: "ring_theory-ko"

date: 2026-06-20
weight: 6


---

앞서 [§중국인의 나머지정리, ⁋명제 6](/ko/math/ring_theory/chinese_remainder_theorem#prop6)에서 우리는 pairwise comaximal이고 교집합이 $0$인 two-sided ideal들이 주어진 ring을 quotient ring들의 곱으로 분해한다는 것을 보았다. 그 분해에서 각 인자를 골라내는 역할을 한 것은 $i$번째 성분만 $1$이고 나머지가 $0$인 원소였으며, 이러한 원소는 ring의 center에 놓인 *idempotent*로 특징지어진다. 

이 글에서는 이러한 idempotent들을 공식적으로 정의하고, central idempotent의 complete orthogonal set이 ring의 direct product 분해와 일대일대응함을 증명한 뒤, 이로부터 일반 ring에서의 중국인의 나머지정리가 어떻게 복원되는지 살펴본다. 

## 멱등원

우선 다음을 정의한다. 

::: 정의 1
Ring $A$의 원소 $e\in A$가 $e^2=e$를 만족하면 이를 *idempotent<sub>멱등원</sub>*라 한다. 두 idempotent $e,f$가 $ef=fe=0$을 만족하면 이들이 *orthogonal<sub>직교</sub>*하다고 한다. 또, idempotent $e$가 $A$의 center $Z(A)$에 속하면 이를 *central idempotent<sub>중심 멱등원</sub>*라 한다.
:::

임의의 ring은 항상 두 idempotent $0$과 $1$을 가지며, 이 둘은 항상 central이다. 이들을 *trivial<sub>자명한</sub>* idempotent이라 부른다. Idempotent $e$가 주어지면 $1-e$ 또한 idempotent인데, 이는

$$(1-e)^2=1-2e+e^2=1-2e+e=1-e$$

이기 때문이다. 뿐만 아니라, 

$$e(1-e)=e-e^2=0,\qquad (1-e)e=e-e^2=0$$

이므로 $e$와 $1-e$는 서로 orthogonal하다. 우리는 $e$를 *complementary idempotent* $1-e$와 짝지어 다룰 것이며, $e$가 central인 것과 $1-e$가 central인 것은 동치이다.

::: 예시 2
Ring $A=\mathbb{Z}/6\mathbb{Z}$의 idempotent는 $0,1,3,4$인 것을 간단한 계산으로 확인할 수 있으며, 여기서 $3,4$가 서로 complementary하고, $0,1$이 서로 complementary한 것을 확인할 수 있다. 뿐만 아니라, $A$는 commutative이므로 이들 네 idempotent들은 자동으로 central idempotent가 된다. 반면 $\mathbb{Z}/4\mathbb{Z}$에서는 $x^2=x$를 푸는 원소가 $0,1$뿐이므로, 이 ring은 trivial idempotent만 가진다.
:::

## Complete set of orthogonal idempotents

이제 우리는 여러 개의 idempotent를 한꺼번에 다루기 위해 다음 개념을 도입한다.

::: 정의 3
Ring $A$의 idempotent들 $e_1,\ldots, e_n$이 다음 두 조건

$$e_1+\cdots+e_n=1,\qquad e_ie_j=0\quad\text{for $i\neq j$}$$

을 모두 만족하면, $\{e_1,\ldots, e_n\}$을 *orthogonal idempotent의 complete set<sub>완전 직교 멱등원</sub>*이라 한다. 만일 각 $e_i$가 모두 central이면 이를 *central*한 complete set이라 한다.
:::

가장 단순한 complete set은 $n=1$일 때의 $\{1\}$이며, [예시 2](#ex2)에서 $\mathbb{Z}/6\mathbb{Z}$의 $\{0,1\}$과 $\{3,4\}$는 $n=2$인 central complete set의 예이다. 더 일반적으로, 하나의 idempotent $e$가 주어지면 $\{e,1-e\}$는 언제나 orthogonal idempotent의 complete set이 된다. 따라서 complete set은 idempotent를 여러 조각으로 분할하는 일반화로 볼 수 있다. 이제 이 분할이 ring을 어떻게 쪼개는지 살펴본다.

::: 명제 4
Ring $A$와 $A$의 complete set of orthogonal idempotents $\{e_1,\ldots, e_n\}$이 주어졌다 하자. 그럼 left $A$-module로서의 분해

$$A=Ae_1\oplus\cdots\oplus Ae_n$$

이 성립한다. 뿐만 아니라, 만일 각 $e_i$가 central이면 각 $Ae_i$는 $A$의 two-sided ideal이 된다.
:::
::: 증명
임의의 $x\in A$에 대하여, $e_1+\cdots+e_n=1$로부터

$$x=x\cdot 1=xe_1+\cdots+xe_n$$

이고 각 $xe_i\in Ae_i$이므로 $A=Ae_1+\cdots+Ae_n$이다. 따라서 보여야 할 것은 이 합이 direct sum이라는 것이다. 

이를 위해, 어떤 원소가 두 가지 방식으로 표현된다 하자. 즉 $a_1e_1+\cdots+a_ne_n=0$이라 하자. 그럼 이 식의 오른쪽에 $e_j$를 곱하면, $i\neq j$에 대해 $e_ie_j=0$이고 $e_j^2=e_j$이므로

$$0=(a_1e_1+\cdots+a_ne_n)e_j=\sum_{i=1}^n a_i(e_ie_j)=a_je_j$$

를 얻는다. 즉 $j$번째 성분 $a_je_j$가 $0$이 되며, 이것이 모든 $j$에 대해 성립하므로 주어진 합은 direct sum이다.

이제 마지막 부분을 보이기 위해 각 $e_i$가 central이라 하자. 그럼 $Ae_i$가 left ideal임은 정의상 자명하므로 right ideal임을 보이면 충분하다. 이를 위해서는 임의의 $ae_i\in Ae_i$와 $x\in A$에 대해 $(ae_i)x\in Ae_i$임을 확인하면 되는데, $e_i$가 central이므로

$$(ae_i)x=a(e_ix)=a(xe_i)=(ax)e_i\in Ae_i$$

가 되어 $Ae_i$는 two-sided ideal이다. 
:::

각 $e_i$가 central일 때 $Ae_i$는 그 자체로 ring의 구조를 갖는다. 특히 $Ae_i$는 항등원을 가지며, 그 항등원은 $e_i$이다. 실제로 임의의 $ae_i\in Ae_i$에 대해 $e_i$가 idempotent이고 central이므로

$$e_i\cdot(ae_i)=(e_ia)e_i=(ae_i)e_i=ae_i^2=ae_i$$

이고 마찬가지로 $(ae_i)\cdot e_i=ae_i$이다. 

## 중심멱등원과 곱분해

위의 논증으로 우리는 각 $Ae_i$가 $e_i$를 항등원으로 갖는 ring이고 $A$가 이들의 direct sum임을 안다. 다음 정리는 이 direct sum이 실은 ring의 direct product이며, 나아가 이러한 decomposition이 central한 complete set과 일대일대응함을 보여준다. 

::: 정리 5
Ring $A$에 대하여 다음 두 데이터 사이에 일대일대응이 존재한다.

1. $A$의 central한 orthogonal idempotent의 complete set $\{e_1,\ldots, e_n\}$.
2. $A$를 $n$개의 two-sided ideal의 direct product $A=\mathfrak{a}_1\times\cdots\times\mathfrak{a}_n$으로 쓰는 decomposition.

이 대응은 $\mathfrak{a}_i=Ae_i$로 주어진다.
:::
::: 증명
우선 첫째 데이터가 주어졌다 하자. 위의 대응이 주는대로 $\mathfrak{a}_i:=Ae_i$로 두면 [명제 4](#prop4)에 의해 각 $\mathfrak{a}_i$는 two-sided ideal이고 $A=\mathfrak{a}_1\oplus\cdots\oplus\mathfrak{a}_n$은 left module로서의 direct sum이다. 따라서 남은 것은 이 direct sum이 ring의 direct product이기도 하다는 것이다. Morphism

$$\varphi:A\rightarrow \prod_{i=1}^n Ae_i;\quad x\mapsto (xe_1,\ldots, xe_n)$$

을 생각하자. 이는 덧셈을 보존하며, $e_i$가 central이고 orthogonal하므로

$$\varphi(x)\varphi(y)=(xe_1\cdot ye_1,\ldots, xe_n\cdot ye_n)=(xye_1,\ldots, xye_n)=\varphi(xy)$$

에서 곱셈도 보존한다. 또 $\varphi(1)=(e_1,\ldots, e_n)$이고 각 $e_i$가 $Ae_i$의 항등원이므로 $\varphi$는 ring homomorphism이다. 이것이 isomorphism이 되는 이유는 [명제 4](#prop4)의 direct sum decomposition이 isomorphism이기 때문이다. 

거꾸로 둘째 데이터가 주어졌다 하자. Direct product decomposition은 특히 덧셈에 대한 direct sum $A=\mathfrak{a}_1\oplus\cdots\oplus\mathfrak{a}_n$을 주므로, 항등원을 이 분해에 따라

$$1=e_1+\cdots+e_n,\qquad e_i\in\mathfrak{a}_i$$

로 유일하게 쓸 수 있다. 임의의 $x\in\mathfrak{a}_j$에 대하여 $\mathfrak{a}_i$가 ideal이므로 $xe_i\in\mathfrak{a}_i$이고, 이로부터 $x$의 분해

$$x=x\cdot 1=xe_1+\cdots+xe_n$$

를 얻으며 이는 유일하다. 그런데 $x\in\mathfrak{a}_j$의 분해는 $j$번째 성분만 $x$이고 나머지가 $0$인 것이므로, 이 유일성에서 $xe_j=x$이고 $i\neq j$에 대해 $xe_i=0$이다. 특히 $x=e_j$를 대입하면 $e_j^2=e_j$이고, 모든 $i\neq j$에 대해 $e_je_i=0$임을 얻는다. 즉 $\{e_1,\ldots, e_n\}$은 orthogonal idempotent의 complete set이다. 이제 보여야 할 것 중 남은 것은 오직 centrality 뿐이다. 임의의 $y\in A$를 

$$y=y_1+\cdots+y_n,\qquad y_i\in\mathfrak{a}_i$$

로 쓰면 위에서 $y_ie_j$는 $i=j$일 때 $y_i$, 아닐 때 $0$이며 $e_jy_i$도 마찬가지이므로 $ye_j=y_j=e_jy$이다. 따라서 각 $e_j$는 모든 $y$와 commute하며 central이다.

마지막으로 이 두 구성이 서로의 역함수임을 확인하자. 첫째 데이터에서 출발하여 $\mathfrak{a}_i=Ae_i$로 두면 $1=e_1+\cdots+e_n$이 이 분해에 따른 $1$의 유일한 표현이므로, 둘째 구성이 돌려주는 idempotent는 다시 $e_i$이다. 거꾸로 둘째 데이터에서 출발하면 $e_i\in\mathfrak{a}_i$에서 $Ae_i\subseteq\mathfrak{a}_i$이고, 위에서 얻은 등식 $x=xe_i$가 임의의 $x\in\mathfrak{a}_i$에 대해 역포함을 주므로 $\mathfrak{a}_i=Ae_i$이다. 따라서 이 대응은 일대일이다.
:::

[정리 5](#thm5)에 의해, ring이 nontrivial한 central idempotent를 갖지 않는 것은 그것이 두 nonzero ring의 곱으로 쪼개지지 않는 것과 동치이다. 이러한 ring을 *connected* 혹은 *indecomposable*하다고 부른다. 가령 division ring $A$는 언제나 indecomposable하다. 만일 $A$가 두 nonzero ring의 곱으로 쪼개진다면 각 인자의 항등원에 해당하는 $(1,0)$과 $(0,1)$이 모두 nonzero이면서 그 곱이 $0$이 되어 $A$가 zero divisor를 갖게 되기 때문이다.

다음 예시는 특히 centrality 조건이 빠졌을 때 일어나는 일을 보여준다. 이 경우, [정리 5](#thm5)는 그 자체로 적용할 수 없지만, 여전히 module로서의 decomposition은 [명제 4](#prop4)에 의해 보장된다.

::: 예시 6
Ring $A$에 대하여 $n\times n$ matrix ring $\Mat_n(A)$를 생각하자. $E_{ij}$를 $(i,j)$ 성분이 $1$이고 나머지가 $0$인 matrix unit이라 하면, 대각 성분들 $E_{11},\ldots, E_{nn}$은

$$E_{ii}^2=E_{ii},\qquad E_{ii}E_{jj}=0\ (i\neq j),\qquad E_{11}+\cdots+E_{nn}=I$$

를 만족하므로 orthogonal idempotent의 complete set이다. 따라서 [명제 4](#prop4)에 의해 left module 분해

$$\Mat_n(A)=\Mat_n(A)E_{11}\oplus\cdots\oplus \Mat_n(A)E_{nn}$$

을 얻는데, 여기서 $\Mat_n(A)E_{ii}$는 $i$번째 열에만 성분이 있는 행렬들의 집합이 된다.

주의할 것은 $n\geq 2$이면 $E_{ii}$는 central이 아니라는 것이다. 가령 $n=2$에서 

$$E_{11}E_{12}=E_{12}\neq 0=E_{12}E_{11}$$

이므로 $E_{11}$은 $E_{12}$와 commute하지 않는다. 따라서 이 분해는 ring의 direct product decomposition을 주지 않는다.

실제로 임의의 ring $A$에 대하여 $\Mat_n(A)$의 center를 직접 계산할 수 있다. 행렬 $M$이 모든 matrix unit과 commute한다고 하면,

$$(E_{kl}M)_{i,j}=\delta_{ik}M_{lj},\qquad (ME_{kl})_{i,j}=M_{ik}\delta_{lj}$$

가 서로 같아야 함을 안다. 이제 $i=k$일 경우를 보자. 그럼

$$M_{lj}=M_{kk}\delta_{lj}$$

이므로, $j\neq l$이라면 $M_{lj}=0$이고, $j=l$인 곳에서는 $M_{ll}=M_{kk}$이므로 $M$은 $cI$의 꼴이어야 하는 것을 안다. 한편 이러한 $M$은 matrix unit들 뿐만 아니라 $aI$ 꼴의 행렬과도 commute해야 하므로, 이 계수 $c$가 $A$의 center $Z(A)$에 속해야 한다. 거꾸로 $c\in Z(A)$이면 임의의 $M$에 대해 $(cIM)_{i,j}=cM_{i,j}=M_{i,j}c=(McI)_{i,j}$이므로 $cI$는 모든 행렬과 commute하며, 따라서

$$Z(\Mat_n(A))=\{cI\mid c\in Z(A)\}$$

이다. 이제 $(cI)^2=c^2I$이므로 $\Mat_n(A)$의 central idempotent는 $c^2=c$인 $c\in Z(A)$에 대한 $cI$들이고, 이는 곧 $A$의 central idempotent들을 그대로 $\Mat_n(A)$에 옮겨준 것이다. 특히 만일 $A$가 division ring이면 $A$의 central idempotent가 $0,1$뿐이므로 $\Mat_n(A)$의 central idempotent는 $0$과 $I$뿐이다.
:::

한편 idempotent가 central인지는 그것을 어느 ring 안에서 보느냐에 달렸다. $n=n_1+\cdots+n_r$로 분할하고, 대각선을 따라 처음 $n_1\times n_1$ block, 다음 $n_2\times n_2$ block 식으로 놓인 block-diagonal 행렬들만 모은 subring

$$B=\left\{\diag(M_1,\ldots, M_r)\mid M_k\in \Mat_{n_k}(A)\right\}\cong\prod_{k=1}^r \Mat_{n_k}(A)$$

안에서, $k$번째 block에만 항등행렬을 놓은 원소 $P_k$는 central이어서 [정리 5](#thm5)의 대응에 따라 이 direct product decomposition을 준다. 그러나 이 $P_k$가 위의 예시 ring $\Mat_n(A)$ 안에서는 central이 아닌 것을 이미 확인하였다. 

## 중국인의 나머지정리와의 연결

한편, 우리는 [정리 5](#thm5) 이전에 이미 주어진 ring을 direct product로 분해하는 방법을 살펴본 적이 있다. ([§중국인의 나머지정리, ⁋명제 6](/ko/math/ring_theory/chinese_remainder_theorem#prop6)) 이 두 결과는 독립적인 것이 아니며, 우리는 글의 남은 부분에서 이들 둘의 관계를 살펴본다. 핵심은 pairwise comaximal 조건이 product ring의 자연스러운 idempotent들을 $A$ 안으로 끌어온다는 것으로, 다음 정리에서 $\pi:A\rightarrow\prod_{i=1}^n A/\mathfrak{a}_i$는 각 quotient로의 projection이 유도하는 morphism 

$$x\mapsto (x+\mathfrak{a}_1,\ldots, x+\mathfrak{a}_n)$$

을 뜻한다.

::: 정리 7
Ring $A$와 그 two-sided ideal들 $\mathfrak{a}_1,\ldots, \mathfrak{a}_n$이 주어졌다 하자. 다음이 모두 동치이다.

1. $\pi:A\rightarrow\prod_{i=1}^n A/\mathfrak{a}_i$가 isomorphism이다.
2. 모든 $i\neq j$에 대하여 $\mathfrak{a}_i+\mathfrak{a}_j=A$이고 $\bigcap_i\mathfrak{a}_i=0$이다.
3. $A$의 central한 orthogonal idempotent의 complete set $\{e_1,\ldots, e_n\}$이 존재하여 모든 $i$에 대해 $\mathfrak{a}_i=A(1-e_i)$이다.
:::
::: 증명
우선 첫째 조건을 가정하고 둘째 조건을 보이자. 만일 $\pi$가 isomorphism이면 $\bigcap_i\mathfrak{a}_i=\ker\pi=0$이다. 또, 고정된 pair $i\neq j$에 대하여 $i$번째 성분이 $1+\mathfrak{a}_i$이며 나머지 성분이 모두 $0$인 원소의 preimage를 $e_i\in A$라 하자. 그럼 $j$번째 성분에서 $e_i\in\mathfrak{a}_j$이고 $i$번째 성분에서 $1-e_i\in\mathfrak{a}_i$이므로

$$1=(1-e_i)+e_i\in\mathfrak{a}_i+\mathfrak{a}_j$$

이고, 따라서 $\mathfrak{a}_i+\mathfrak{a}_j=A$이다.

이제 둘째 조건을 가정하고 셋째 조건을 보이자. Pairwise comaximal 조건과 $\bigcap_i\mathfrak{a}_i=\ker\pi=0$으로부터 [§중국인의 나머지정리, ⁋명제 6](/ko/math/ring_theory/chinese_remainder_theorem#prop6)에 의해 $\pi$는 isomorphism이다. Product ring $\prod_i A/\mathfrak{a}_i$에서 $i$번째 성분만 $1+\mathfrak{a}_i$이고 나머지가 $0$인 원소

$$\bar e_i=(0,\ldots, 0,1,0,\ldots, 0)$$

들을 생각하면, 성분별 계산으로 이들이 central한 orthogonal idempotent의 complete set을 이룸을 알 수 있으며 $\pi$가 ring isomorphism이므로 $e_i:=\pi^{-1}(\bar e_i)$ 또한 $A$의 central한 orthogonal idempotent의 complete set이다. 남은 것은 등식 $\mathfrak{a}_i=A(1-e_i)$으로, $\bar e_i$의 $i$번째 성분이 $1+\mathfrak{a}_i$이므로 $1-e_i\in\mathfrak{a}_i$이고, $\mathfrak{a}_i$가 ideal이므로 $A(1-e_i)\subseteq\mathfrak{a}_i$임은 자명하다. 거꾸로 $a\in\mathfrak{a}_i$라 하면 $\pi(a)$의 $i$번째 성분이 $0$이고 $\bar e_i$는 $i$번째 성분을 제외한 모든 성분이 $0$이므로 $\pi(ae_i)=\pi(a)\bar e_i=0$이며, $\pi$가 단사이므로 $ae_i=0$이다. 따라서

$$a=ae_i+a(1-e_i)=a(1-e_i)\in A(1-e_i)$$

이다.

마지막으로 셋째 조건을 가정하고 첫째 조건을 보이자. [정리 5](#thm5)에 의해 central한 complete set $\{e_1,\ldots, e_n\}$은 ring isomorphism $x\mapsto (xe_1,\ldots, xe_n)$으로 주어지는 direct product decomposition $A\cong\prod_i Ae_i$를 준다. 한편 각 $i$에 대하여 morphism

$$A\rightarrow Ae_i;\quad a\mapsto ae_i$$

는 자명하게 전사이고, $ae_i=0$이면 $a=a(1-e_i)$이며 거꾸로 $a(1-e_i)e_i=0$이므로 그 kernel은 $A(1-e_i)=\mathfrak{a}_i$이다. 따라서 $A/\mathfrak{a}_i\cong Ae_i$이며, 이 isomorphism이 $x+\mathfrak{a}_i\mapsto xe_i$로 주어지므로 위의 direct product decomposition과 합성하면 정확히 $\pi$를 얻는다. 그러므로 $\pi$는 isomorphism이다.
:::

이를 가장 친숙한 경우인 정수환에 적용해 보자.

::: 예시 8
$n\geq 2$의 소인수분해를 $n=p_1^{a_1}\cdots p_r^{a_r}$ (서로 다른 소수 $p_k$)이라 하고, $A=\mathbb{Z}/n\mathbb{Z}$의 ideal들 $\mathfrak{a}_k=p_k^{a_k}\mathbb{Z}/n\mathbb{Z}$를 생각하자. $\mathbb{Z}$ 안에서 $p_k^{a_k}\mathbb{Z}$들은 pairwise comaximal이고 그 교차가 $n\mathbb{Z}$이므로, $A$ 안에서 $\mathfrak{a}_k$들은 pairwise comaximal이고 $\bigcap_k\mathfrak{a}_k=0$이다. 따라서 [정리 7](#thm7)이 적용되어 고전적인 중국인의 나머지정리

$$\mathbb{Z}/n\mathbb{Z}\cong\prod_{k=1}^r\mathbb{Z}/p_k^{a_k}\mathbb{Z}$$

와 함께, 이 분해에 대응하는 $\mathbb{Z}/n\mathbb{Z}$의 central한 orthogonal idempotent의 complete set을 얻는다.

구체적으로 $n=6=2\cdot 3$인 경우를 보면 $\mathbb{Z}/6\mathbb{Z}\cong\mathbb{Z}/2\mathbb{Z}\times\mathbb{Z}/3\mathbb{Z}$이다. Product ring $\mathbb{Z}/2\mathbb{Z}\times\mathbb{Z}/3\mathbb{Z}$의 두 idempotent $\bar e_1=(1,0)$, $\bar e_2=(0,1)$을 isomorphism으로 끌어오면, $\mathbb{Z}/6\mathbb{Z}$에서 $(1,0)$에 대응하는 원소는 $3$, $(0,1)$에 대응하는 원소는 $4$이다. 실제로 $3\equiv 1\ (\mathrm{mod}\ 2)$, $3\equiv 0\ (\mathrm{mod}\ 3)$이고 $4\equiv 0\ (\mathrm{mod}\ 2)$, $4\equiv 1\ (\mathrm{mod}\ 3)$이다. 이는 [예시 2](#ex2)에서 손으로 찾은 idempotent $3,4$와 정확히 일치한다.

한편 소수 $p$와 $a\geq 1$에 대하여 $\mathbb{Z}/p^a\mathbb{Z}$는 $0,1$ 외의 idempotent를 갖지 않는다. 이는 $x^2\equiv x\ (\mathrm{mod}\ p^a)$가 $x(x-1)\equiv 0\ (\mathrm{mod}\ p^a)$와 같고, $x$와 $x-1$이 서로소라 $p^a$이 둘 중 하나만을 나누어야 하기 때문이다. 따라서 위 분해의 각 인수는 [정리 5](#thm5)의 의미에서 indecomposable하며, 소인수분해에 따른 direct product decomposition은 더 이상 쪼갤 수 없는 가장 미세한 분해이다. [예시 2](#ex2)에서 $\mathbb{Z}/4\mathbb{Z}$가 trivial idempotent만 가졌던 것이 그 특수한 경우이다.
:::

---

**참고문헌**

**[AM]** M. F. Atiyah and I. G. Macdonald, *Introduction to commutative algebra*, Addison–Wesley, 1969.  
**[DF]** D. S. Dummit and R. M. Foote, *Abstract algebra*, 3rd ed., Wiley, 2004.  
**[Lam]** T. Y. Lam, *A first course in noncommutative rings*, 2nd ed., Graduate Texts in Mathematics 131, Springer, 2001.
