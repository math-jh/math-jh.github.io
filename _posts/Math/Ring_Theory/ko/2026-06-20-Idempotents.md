---
title: "Idempotent과 곱분해"
description: "Idempotent과 orthogonal idempotent의 complete set을 정의하고, central idempotent이 환의 곱분해와 일대일대응함을 증명한 뒤, 이를 일반 환에서의 중국인의 나머지정리와 연결한다."
excerpt: "Central idempotent과 환의 곱분해, 그리고 일반 환에서의 중국인의 나머지정리"

categories: [Math / Ring Theory]
permalink: /ko/math/ring_theory/idempotents
sidebar: 
    nav: "ring_theory-ko"

date: 2026-06-20
weight: 2.5

published: false

---

앞선 글 ([§중국인의 나머지정리, ⁋명제 5](/ko/math/ring_theory/chinese_remainder_theorem#prop5))에서 우리는 쌍별로 comaximal한 two-sided ideal들에 대해 환이 몫환들의 곱으로 분해됨을 보았다. 그 글의 마지막 ([§중국인의 나머지정리, ⁋명제 6](/ko/math/ring_theory/chinese_remainder_theorem#prop6))에서는 이러한 곱분해가 환의 center에 놓인 특정한 원소들, 즉 idempotent들로 기술된다는 사실이 짧게 언급되었다. 이 글에서는 그 원소들을 본격적으로 다룬다. 우리는 idempotent의 성질을 정리하고, central idempotent의 complete orthogonal set이 환의 직접곱 분해와 일대일대응함을 증명한 뒤, 이로부터 일반 환에서의 중국인의 나머지정리를 다시 조명한다.

별도의 언급이 없는 한 $$A$$는 항등원 $$1\neq 0$$을 갖는 환이며, commutativity는 가정하지 않는다. 가환성이 필요한 곳에서는 그때그때 명시한다.

## Idempotent

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 환 $$A$$의 원소 $$e\in A$$가 $$e^2=e$$를 만족하면 이를 *idempotent<sub>멱등원</sub>*이라 한다. 두 idempotent $$e,f$$가 $$ef=fe=0$$을 만족하면 이들이 *orthogonal<sub>직교</sub>*하다고 한다. 또, idempotent $$e$$가 $$A$$의 center $$C(A)=\{c\in A: cx=xc\text{ for all }x\in A\}$$에 속하면 이를 *central idempotent<sub>중심 멱등원</sub>*이라 한다.

</div>

임의의 환은 두 idempotent $$0$$과 $$1$$을 가지며, 이 둘은 항상 central이다. 이들을 *trivial<sub>자명한</sub>* idempotent이라 부른다. Idempotent $$e$$가 주어지면 $$1-e$$ 또한 idempotent인데, 이는

$$(1-e)^2=1-2e+e^2=1-2e+e=1-e$$

로부터 따라온다. 더욱이 $$e(1-e)=e-e^2=0$$이고 $$(1-e)e=e-e^2=0$$이므로 $$e$$와 $$1-e$$는 서로 orthogonal하다. 우리는 $$e$$를 *complementary idempotent* $$1-e$$와 짝지어 다룰 것이며, $$e$$가 central인 것과 $$1-e$$가 central인 것은 동치이다.

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins> 환 $$A=\mathbb{Z}/6\mathbb{Z}$$를 보자. 이 환에서 $$x^2=x$$를 만족하는 원소는 $$0,1,3,4$$인데, 가령 $$3^2=9=3$$, $$4^2=16=4$$이다. 한편 $$3+4=7=1$$이고 $$3\cdot 4=12=0$$이므로, $$3$$과 $$4$$는 서로 complementary한 orthogonal idempotent이며 그 합은 $$1$$이다. $$A$$가 가환이므로 이 둘은 자동으로 central이다.

반면 $$\mathbb{Z}/4\mathbb{Z}$$에서는 $$x^2=x$$를 푸는 원소가 $$0,1$$뿐이다. 즉 trivial idempotent만 존재한다.

</div>

위의 두 환의 대비는 우연이 아니다. $$6=2\cdot 3$$은 서로 다른 소수의 곱이라 $$\mathbb{Z}/6\mathbb{Z}$$가 두 환의 곱으로 쪼개지는 반면, $$4=2^2$$는 소수의 거듭제곱이라 더 쪼개지지 않는다. 이 현상이 idempotent의 존재로 정확히 포착된다는 것이 이 글의 주제이며, 우리는 이를 [정리 5](#thm5)와 [예시 8](#ex8)에서 명확히 한다.

## Complete set of orthogonal idempotents

여러 개의 idempotent를 한꺼번에 다루기 위해 다음 개념을 도입한다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> 환 $$A$$의 원소들 $$e_1,\ldots, e_n$$이 다음 세 조건

$$e_i^2=e_i\ (\text{모든 }i),\qquad e_ie_j=0\ (i\neq j),\qquad e_1+\cdots+e_n=1$$

을 모두 만족하면, $$\{e_1,\ldots, e_n\}$$을 *orthogonal idempotent의 complete set<sub>완전 직교 멱등원 모임</sub>*이라 한다. 만일 각 $$e_i$$가 모두 central이면 이를 *central*한 complete set이라 한다.

</div>

조건에서 $$i\neq j$$일 때 $$e_ie_j=0$$만을 요구하였으나, 사실 $$e_je_i=0$$도 자동으로 따라온다. 이는 아래 [명제 4](#prop4)의 증명 과정에서 확인된다. 가장 단순한 complete set은 $$n=1$$일 때의 $$\{1\}$$이며, [예시 2](#ex2)의 $$\{3,4\}\subset\mathbb{Z}/6\mathbb{Z}$$는 $$n=2$$인 central complete set의 예이다.

하나의 idempotent $$e$$가 주어지면 $$\{e,1-e\}$$는 언제나 orthogonal idempotent의 complete set이 된다. 따라서 complete set은 idempotent를 여러 조각으로 분할하는 일반화로 볼 수 있다. 이제 이 분할이 환을 어떻게 쪼개는지 살펴본다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> $$\{e_1,\ldots, e_n\}$$이 환 $$A$$의 orthogonal idempotent의 complete set이라 하자. 그럼 left $$A$$-module로서의 분해

$$A=Ae_1\oplus\cdots\oplus Ae_n$$

이 성립한다. 더욱이 각 $$e_i$$가 central이면 각 $$Ae_i$$는 $$A$$의 two-sided ideal이고, 이 때 $$e_je_i=0\ (i\neq j)$$ 또한 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

임의의 $$x\in A$$에 대하여, $$e_1+\cdots+e_n=1$$로부터

$$x=x\cdot 1=xe_1+\cdots+xe_n$$

이고 각 $$xe_i\in Ae_i$$이므로 $$A=Ae_1+\cdots+Ae_n$$이다. 합이 직합임을 보이기 위해, 어떤 원소가 두 가지 방식으로 표현된다 하자. 즉 $$a_1e_1+\cdots+a_ne_n=0$$이라 하자 (단 $$a_i\in A$$). 이 식의 오른쪽에 $$e_j$$를 곱하면, $$i\neq j$$에 대해 $$e_ie_j=0$$이고 $$e_j^2=e_j$$이므로

$$0=(a_1e_1+\cdots+a_ne_n)e_j=\sum_{i=1}^n a_i(e_ie_j)=a_je_j$$

를 얻는다. 즉 $$j$$번째 성분 $$a_je_j$$가 $$0$$이다. 모든 $$j$$에 대해 이것이 성립하므로 표현은 유일하며, 합은 직합이다.

이제 각 $$e_i$$가 central이라 하자. $$Ae_i$$가 left ideal임은 정의상 자명하다. Right ideal임을 보이려면 임의의 $$ae_i\in Ae_i$$와 $$x\in A$$에 대해 $$(ae_i)x\in Ae_i$$임을 확인하면 되는데, $$e_i$$가 central이므로

$$(ae_i)x=a(e_ix)=a(xe_i)=(ax)e_i\in Ae_i$$

이다. 따라서 $$Ae_i$$는 two-sided ideal이다. 마지막으로 $$e_i$$가 central이면 $$i\neq j$$일 때 $$e_je_i=e_ie_j=0$$이므로 나머지 직교 조건도 성립한다.

</details>

명제의 첫 부분은 idempotent가 일반적이라면 left module 수준의 분해까지만 보장함을 말한다. 분해 $$A=Ae_1\oplus\cdots\oplus Ae_n$$은 $$A$$를 그 위의 left module로 본 직합이며, 각 $$Ae_i$$가 환의 ideal이 되려면 centrality가 필요하다. 이 차이가 곧 module 분해와 환의 곱분해를 가르는 지점이다.

각 $$e_i$$가 central일 때 $$Ae_i$$는 그 자체로 환의 구조를 갖는다. $$Ae_i$$는 $$A$$의 곱셈을 물려받되, 그 항등원은 $$1$$이 아니라 $$e_i$$이다. 실제로 임의의 $$ae_i\in Ae_i$$에 대해 $$e_i$$가 idempotent이고 central이므로

$$e_i\cdot(ae_i)=(e_ia)e_i=(ae_i)e_i=ae_i^2=ae_i$$

이고 마찬가지로 $$(ae_i)\cdot e_i=ae_i$$이다. 즉 $$e_i$$는 $$Ae_i$$의 양쪽 항등원으로 작동한다. 이것이 다음 정리에서 곱분해의 각 성분이 되는 환들이다.

## Central idempotent과 곱분해

이제 central한 complete set이 환의 직접곱 분해와 정확히 대응함을 보인다. 환 $$A$$가 환들 $$A_1,\ldots, A_n$$의 직접곱 $$A\cong A_1\times\cdots\times A_n$$으로 쓰인다는 것은, 성분별 덧셈과 곱셈을 갖는 곱환 $$\prod A_i$$로의 환동형사상이 존재함을 뜻한다.

<div class="proposition" markdown="1">

<ins id="thm5">**정리 5**</ins> 환 $$A$$에 대하여 다음 두 자료 사이에 일대일대응이 존재한다.

1. $$A$$의 central한 orthogonal idempotent의 complete set $$\{e_1,\ldots, e_n\}$$.
2. $$A$$를 $$n$$개의 nonzero two-sided ideal의 직합 $$A=\mathfrak{a}_1\oplus\cdots\oplus\mathfrak{a}_n$$으로 쓰는 분해. 단, 이는 환의 직접곱 분해 $$A\cong\prod_{i=1}^n \mathfrak{a}_i$$를 준다.

이 대응에서 $$\mathfrak{a}_i=Ae_i$$이고, 거꾸로 $$e_i$$는 분해 $$1=e_1+\cdots+e_n$$의 $$i$$번째 성분, 즉 $$\mathfrak{a}_i$$의 항등원이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$(1)\Rightarrow(2)$$. Central한 complete set $$\{e_1,\ldots, e_n\}$$이 주어졌다 하자. [명제 4](#prop4)에 의해 $$\mathfrak{a}_i:=Ae_i$$는 two-sided ideal이고 $$A=\mathfrak{a}_1\oplus\cdots\oplus\mathfrak{a}_n$$은 left module로서의 직합이다. 사상

$$\varphi:A\longrightarrow \prod_{i=1}^n Ae_i,\qquad \varphi(x)=(xe_1,\ldots, xe_n)$$

을 생각하자. 이는 덧셈을 보존하며, $$e_i$$가 central이고 orthogonal하므로

$$\varphi(x)\varphi(y)=(xe_1\cdot ye_1,\ldots, xe_n\cdot ye_n)=(xye_1,\ldots, xye_n)=\varphi(xy)$$

에서 곱셈도 보존한다. 여기서 각 성분의 곱 $$xe_i\cdot ye_i=xy e_i^2=xye_i$$를 사용하였으며, 이는 $$e_i$$의 centrality에 의해 $$e_iy=ye_i$$이기 때문이다. 또 $$\varphi(1)=(e_1,\ldots, e_n)$$이고 각 $$e_i$$가 $$Ae_i$$의 항등원이므로 $$\varphi$$는 환준동형사상이다. $$\varphi$$가 동형임은 [명제 4](#prop4)의 직합 분해가 곧 $$x\mapsto (xe_1,\ldots, xe_n)$$의 단사성과 전사성을 주기 때문이다. 즉 $$\varphi(x)=0$$이면 모든 $$xe_i=0$$이고 $$x=\sum xe_i=0$$이며, 임의의 $$(a_1e_1,\ldots, a_ne_n)$$은 $$x=a_1e_1+\cdots+a_ne_n$$의 상이다.

$$(2)\Rightarrow(1)$$. 거꾸로 $$A=\mathfrak{a}_1\oplus\cdots\oplus\mathfrak{a}_n$$이 nonzero two-sided ideal들의 직합이라 하자. 항등원을 이 분해에 따라

$$1=e_1+\cdots+e_n,\qquad e_i\in\mathfrak{a}_i$$

로 유일하게 쓴다. 임의의 $$x\in\mathfrak{a}_j$$에 대하여 $$\mathfrak{a}_i$$가 ideal이므로 $$xe_i\in\mathfrak{a}_i$$이고, 또

$$x=x\cdot 1=xe_1+\cdots+xe_n$$

인데 좌변 $$x\in\mathfrak{a}_j$$를 직합 분해의 유일성과 비교하면 $$xe_j=x$$이고 $$i\neq j$$에 대해 $$xe_i=0$$이다. 같은 논증을 $$1\cdot x$$에 적용하면 $$e_jx=x$$, $$e_ix=0\ (i\neq j)$$도 얻는다. 특히 $$x=e_j\in\mathfrak{a}_j$$를 대입하면 $$e_j^2=e_j$$이고 $$i\neq j$$에 대해 $$e_ie_j=e_je_i=0$$이다. 즉 $$\{e_1,\ldots, e_n\}$$은 orthogonal idempotent의 complete set이다. Centrality는 다음과 같이 확인된다. 임의의 $$y\in A$$를 $$y=y_1+\cdots+y_n$$ ($$y_i\in\mathfrak{a}_i$$)로 쓰면 위에서 $$y_ie_j$$는 $$i=j$$일 때 $$y_i$$, 아닐 때 $$0$$이므로 $$ye_j=y_j=e_jy$$이다. 따라서 각 $$e_j$$는 모든 $$y$$와 가환이며 central이다.

두 구성은 서로 역이다. $$(1)$$에서 출발해 $$\mathfrak{a}_i=Ae_i$$를 만들고 다시 그 항등원을 취하면 $$Ae_i$$의 항등원이 $$e_i$$임은 [명제 4](#prop4) 뒤에서 확인하였으므로 원래의 $$e_i$$로 돌아온다. 반대로 $$(2)$$의 분해에서 $$e_i$$를 얻은 뒤 $$Ae_i$$를 만들면, 위에서 $$\mathfrak{a}_i$$의 모든 원소 $$x$$가 $$x=xe_i\in Ae_i$$를 만족하고 거꾸로 $$Ae_i\subseteq\mathfrak{a}_i$$이므로 $$Ae_i=\mathfrak{a}_i$$이다. 따라서 대응은 일대일이다.

</details>

이 정리는 환의 곱분해를 다루는 일이 곧 central idempotent를 다루는 일과 같음을 말한다. 곱분해가 더 이상 쪼개지지 않는다는 것은 nontrivial central idempotent가 존재하지 않는다는 것, 즉 $$0$$과 $$1$$만이 유일한 central idempotent라는 것과 같다. 이러한 환을 *connected* 혹은 *indecomposable*하다고 부른다. [예시 2](#ex2)에서 $$\mathbb{Z}/4\mathbb{Z}$$가 trivial idempotent만 가졌던 것은 이 환이 더 이상 곱으로 분해되지 않음을 반영한다.

가환환의 경우 모든 idempotent가 자동으로 central이므로, 정리의 대응은 단순히 "orthogonal idempotent의 complete set ↔ 곱분해"가 된다. Noncommutative한 경우에는 centrality 조건이 본질적이다. 다음 예시는 centrality가 빠지면 곱분해 대신 module 분해만 남음을 보여준다.

<div class="example" markdown="1">

<ins id="ex6">**예시 6**</ins> 환 $$R$$에 대하여 $$n\times n$$ 행렬환 $$A=M_n(R)$$을 생각하자. $$E_{ij}$$를 $$(i,j)$$ 성분이 $$1$$이고 나머지가 $$0$$인 matrix unit이라 하면, 대각 성분들 $$E_{11},\ldots, E_{nn}$$은

$$E_{ii}^2=E_{ii},\qquad E_{ii}E_{jj}=0\ (i\neq j),\qquad E_{11}+\cdots+E_{nn}=I$$

를 만족하므로 orthogonal idempotent의 complete set이다. 따라서 [명제 4](#prop4)에 의해 left module 분해

$$M_n(R)=M_n(R)E_{11}\oplus\cdots\oplus M_n(R)E_{nn}$$

을 얻는데, $$M_n(R)E_{ii}$$는 $$i$$번째 열에만 성분이 있는 행렬들의 집합이다.

그러나 $$n\geq 2$$이면 $$E_{ii}$$는 central이 아니다. 가령 $$n=2$$에서 $$E_{11}E_{12}=E_{12}$$이지만 $$E_{12}E_{11}=0$$이므로 $$E_{11}$$은 $$E_{12}$$와 가환이 아니다. 따라서 이 분해는 환의 곱분해를 주지 않으며, 실제로 $$R$$이 division ring이면 $$M_n(R)$$은 nontrivial two-sided ideal을 갖지 않아 곱으로 분해되지 않는다. 즉 $$M_n(R)$$의 유일한 central idempotent는 $$0$$과 $$I$$뿐이다.

진짜 곱분해는 block 구조에서 나온다. $$n=n_1+\cdots+n_r$$로 분할하고, 대각선을 따라 처음 $$n_1\times n_1$$ block, 다음 $$n_2\times n_2$$ block 식으로 놓인 block-diagonal 행렬들만 모은 부분환

$$B=\left\{\operatorname{diag}(M_1,\ldots, M_r):M_k\in M_{n_k}(R)\right\}\cong\prod_{k=1}^r M_{n_k}(R)$$

을 보자. $$B$$ 안에서 $$k$$번째 block에만 항등행렬을 놓은 원소 $$P_k$$는 $$B$$의 central idempotent이며, $$\{P_1,\ldots, P_r\}$$은 [정리 5](#thm5)의 의미에서 곱분해 $$B\cong\prod M_{n_k}(R)$$에 대응하는 central complete set이다. $$P_k$$들은 $$B$$ 안에서는 central이지만 더 큰 환 $$M_n(R)$$ 안에서는 그렇지 않다.

</div>

## 중국인의 나머지정리와의 연결

이제 앞선 글의 중국인의 나머지정리를 idempotent의 관점에서 다시 본다. 핵심은 쌍별 comaximal 조건이 곱환의 자연스러운 idempotent들을 $$A$$ 안으로 끌어온다는 것이다.

<div class="proposition" markdown="1">

<ins id="thm7">**정리 7**</ins> 환 $$A$$와 그 two-sided ideal들 $$\mathfrak{a}_1,\ldots, \mathfrak{a}_n$$이 주어졌다 하고, $$i\neq j$$에 대해 항상 $$\mathfrak{a}_i+\mathfrak{a}_j=A$$ (즉 쌍별 comaximal)라 하자. 그럼 자연스러운 사상

$$\pi:A\longrightarrow\prod_{i=1}^n A/\mathfrak{a}_i,\qquad \pi(x)=(x+\mathfrak{a}_1,\ldots, x+\mathfrak{a}_n)$$

은 전사이고 그 kernel은 $$\bigcap_{i=1}^n\mathfrak{a}_i$$이다. 따라서 환동형사상

$$\frac{A}{\bigcap_{i=1}^n\mathfrak{a}_i}\cong\prod_{i=1}^n A/\mathfrak{a}_i$$

가 존재한다. 특히 $$\bigcap_{i=1}^n\mathfrak{a}_i=0$$이면 $$A\cong\prod_{i=1}^n A/\mathfrak{a}_i$$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

이는 앞선 글 ([§중국인의 나머지정리, ⁋명제 5](/ko/math/ring_theory/chinese_remainder_theorem#prop5))에서 증명되었다. 간략히 다시 적으면, $$\ker\pi=\bigcap\mathfrak{a}_i$$임은 정의에서 곧바로 따라오고, 전사성은 다음과 같이 귀납적으로 얻어진다. $$n=1$$인 경우는 quotient의 성질로부터 자명하다. 모든 $$i<n$$에 대해 $$\pi_i(y)$$를 원하는 값으로 맞추는 $$y$$가 있다 하면, $$x=y+z$$ 꼴로 $$z\in\bigcap_{i<n}\mathfrak{a}_i$$이면서 $$z+\mathfrak{a}_n=x_n-y+\mathfrak{a}_n$$인 $$z$$를 찾으면 된다. 이러한 $$z$$의 존재는 comaximal 조건이 주는 등식

$$\mathfrak{a}_n+\bigcap_{i<n}\mathfrak{a}_i=A$$

([§중국인의 나머지정리, ⁋명제 3](/ko/math/ring_theory/chinese_remainder_theorem#prop3))으로부터 보장된다. 마지막의 동형사상은 first isomorphism theorem의 직접적 귀결이다.

</details>

이 정리가 [정리 5](#thm5)의 곱분해를 어떻게 만들어내는지 살펴보자. $$\bigcap\mathfrak{a}_i=0$$이라 가정하면 $$\pi:A\xrightarrow{\sim}\prod A/\mathfrak{a}_i$$는 환동형사상이다. 곱환 $$\prod A/\mathfrak{a}_i$$에는 자연스러운 central complete set이 있는데, 바로 $$i$$번째 성분만 $$1$$이고 나머지가 $$0$$인 원소

$$\bar e_i=(0,\ldots, 0,\underset{i}{1},0,\ldots, 0)$$

들이다. 이들이 $$\prod A/\mathfrak{a}_i$$의 central한 orthogonal idempotent의 complete set임은 성분별로 확인된다. $$\pi$$가 동형이므로 $$e_i:=\pi^{-1}(\bar e_i)$$는 $$A$$의 central한 orthogonal idempotent의 complete set을 이루고, [정리 5](#thm5)의 대응에 따라 분해 $$A\cong\prod Ae_i$$를 준다. 이 때 $$Ae_i\cong A/\mathfrak{a}_i$$이며, 실제로 $$\mathfrak{a}_i=\ker(A\to A/\mathfrak{a}_i)$$는 $$\pi$$ 아래에서 $$i$$번째 성분이 $$0$$인 부분, 즉 $$A(1-e_i)$$에 대응한다. 이는 앞선 글의 ([§중국인의 나머지정리, ⁋명제 6](/ko/math/ring_theory/chinese_remainder_theorem#prop6))에서 $$\mathfrak{a}_i=A(1-e_i)$$로 기술된 idempotent들이 바로 위의 $$e_i$$임을 말해 준다.

요약하면, 쌍별 comaximal이고 $$\bigcap\mathfrak{a}_i=0$$인 ideal들이 주어지는 것은 $$A$$가 곱으로 분해되는 것과 같고, 이는 다시 $$A$$가 central한 orthogonal idempotent의 complete set을 갖는 것과 같다. 중국인의 나머지정리는 이 세 관점을 하나로 묶는 다리이다.

이를 가장 친숙한 경우인 정수환에 적용해 보자.

<div class="example" markdown="1">

<ins id="ex8">**예시 8**</ins> $$A=\mathbb{Z}$$를 보고, $$n\geq 2$$의 소인수분해를 $$n=p_1^{a_1}\cdots p_r^{a_r}$$ (서로 다른 소수 $$p_k$$)이라 하자. $$\mathfrak{a}_k=p_k^{a_k}\mathbb{Z}$$로 두면, 서로 다른 $$k,l$$에 대해 $$p_k^{a_k}$$와 $$p_l^{a_l}$$이 서로소이므로 적당한 정수 $$u,v$$가 존재하여 $$up_k^{a_k}+vp_l^{a_l}=1$$이고, 따라서 $$\mathfrak{a}_k+\mathfrak{a}_l=\mathbb{Z}$$로 쌍별 comaximal하다. 또 $$\bigcap_k\mathfrak{a}_k=\operatorname{lcm}(p_1^{a_1},\ldots, p_r^{a_r})\mathbb{Z}=n\mathbb{Z}$$이다. [정리 7](#thm7)을 몫환 $$\mathbb{Z}/n\mathbb{Z}$$에 적용하면 환동형사상

$$\mathbb{Z}/n\mathbb{Z}\cong\prod_{k=1}^r\mathbb{Z}/p_k^{a_k}\mathbb{Z}$$

을 얻는다. 이것이 고전적인 중국인의 나머지정리이다.

구체적으로 $$n=6=2\cdot 3$$인 경우를 보면 $$\mathbb{Z}/6\mathbb{Z}\cong\mathbb{Z}/2\mathbb{Z}\times\mathbb{Z}/3\mathbb{Z}$$이다. 곱환 $$\mathbb{Z}/2\mathbb{Z}\times\mathbb{Z}/3\mathbb{Z}$$의 두 idempotent $$\bar e_1=(1,0)$$, $$\bar e_2=(0,1)$$을 동형사상으로 끌어오면, $$\mathbb{Z}/6\mathbb{Z}$$에서 $$(1,0)$$에 대응하는 원소는 $$3$$, $$(0,1)$$에 대응하는 원소는 $$4$$이다. 실제로 $$3\equiv 1\ (\mathrm{mod}\ 2)$$, $$3\equiv 0\ (\mathrm{mod}\ 3)$$이고 $$4\equiv 0\ (\mathrm{mod}\ 2)$$, $$4\equiv 1\ (\mathrm{mod}\ 3)$$이다. 이는 [예시 2](#ex2)에서 손으로 찾은 idempotent $$3,4$$와 정확히 일치한다.

</div>

마지막으로, 곱으로 더 쪼갤 수 없는 경우와의 대비를 명시해 둔다.

<div class="remark" markdown="1">

<ins id="rmk9">**참고 9**</ins> [예시 8](#ex8)의 분해에서 각 인수는 소수의 거듭제곱 $$p_k^{a_k}$$의 몫이다. $$\mathbb{Z}/p^a\mathbb{Z}$$는 $$0,1$$ 외의 idempotent를 갖지 않는데, 이는 $$x^2\equiv x\ (\mathrm{mod}\ p^a)$$가 $$x(x-1)\equiv 0\ (\mathrm{mod}\ p^a)$$와 같고, $$x$$와 $$x-1$$이 서로소라 $$p^a$$이 둘 중 하나만을 나누어야 하기 때문이다. 따라서 $$\mathbb{Z}/p^a\mathbb{Z}$$는 [정리 5](#thm5)의 의미에서 indecomposable하며, 소인수분해에 따른 곱분해는 더 이상 쪼갤 수 없는 가장 미세한 분해이다. 이는 [예시 2](#ex2)에서 $$\mathbb{Z}/4\mathbb{Z}$$가 trivial idempotent만 가졌던 관찰의 일반화이다.

</div>

---

**참고문헌**

**[AM]** M. F. Atiyah and I. G. Macdonald, *Introduction to commutative algebra*, Addison–Wesley, 1969.

**[DF]** D. S. Dummit and R. M. Foote, *Abstract algebra*, 3rd ed., Wiley, 2004.

**[Lam]** T. Y. Lam, *A first course in noncommutative rings*, 2nd ed., Graduate Texts in Mathematics 131, Springer, 2001.
