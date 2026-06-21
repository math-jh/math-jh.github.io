---
title: "Quiver와 경로대수"
description: "quiver Q로부터 경로대수 kQ를 paths를 basis로, concatenation을 곱셈으로 하여 구성하고, Q의 representation들이 이루는 category가 left kQ-module들의 category와 동치임을 증명한다. 선형 A_n quiver, one-loop quiver, Kronecker quiver를 예시로 다룬다."
excerpt: "Quiver의 path algebra와 Rep(Q) ≅ kQ-module의 동치"

categories: [Math / Representation Theory]
permalink: /ko/math/representation_theory/path_algebras
sidebar: 
    nav: "representation_theory-ko"

date: 2026-06-20
weight: 10

published: false

---

표현론의 기본적인 전략은 추상적인 대수적 대상을 벡터공간 위의 선형사상으로 실현하여 선형대수학의 언어로 분석하는 것이다. 앞선 글들에서 우리는 finite group $$G$$와 유한차원 가환대수를 그러한 방식으로 다루었다. 이번 글에서 우리는 *quiver*, 곧 유향그래프를 출발점으로 삼는다. Quiver $$Q$$ 하나에는 *path algebra* $$kQ$$라 부르는 결합대수가 자연스럽게 따라붙으며, $$Q$$의 *representation*은 각 vertex에 벡터공간을, 각 arrow에 선형사상을 얹은 자료이다. 이 글의 핵심은 $$Q$$의 representation들이 이루는 category가 $$kQ$$ 위의 left module들이 이루는 category와 동치라는 것이다. 이 동치는 이어지는 논의들의 토대가 된다.

이 글에서 $$k$$는 field를 가리킨다. Quiver는 vertex의 집합과 arrow의 집합이 모두 유한한 경우만을 다루며, 대수와 module의 일반론은 [\[대수적 구조\] §대수](/ko/math/algebraic_structures/algebras)와 [\[대수적 구조\] §가군](/ko/math/algebraic_structures/modules)에서 다룬 것을 따른다. 특히 associative unital $$k$$-algebra란 곱셈이 결합법칙을 만족하고 항등원을 가지는 $$k$$-algebra를 뜻한다 ([\[대수적 구조\] §대수, ⁋정의 1](/ko/math/algebraic_structures/algebras#def1)).

## Quiver와 path

먼저 우리가 다루는 조합론적 대상을 정의한다. Quiver는 다중간선과 loop를 허용하는 유향그래프에 다름 아니다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> *Quiver<sub>quiver</sub>* $$Q=(Q_0,Q_1,s,t)$$는 다음의 자료로 이루어진다. 유한집합 $$Q_0$$의 원소를 *vertex<sub>꼭짓점</sub>*라 부르고, 유한집합 $$Q_1$$의 원소를 *arrow<sub>화살표</sub>*라 부른다. 두 함수

$$s,t:Q_1\rightarrow Q_0$$

은 각 arrow $$\alpha\in Q_1$$에 그 *source<sub>시작점</sub>* $$s(\alpha)$$와 *target<sub>끝점</sub>* $$t(\alpha)$$를 대응시킨다. Source가 $$i$$이고 target이 $$j$$인 arrow $$\alpha$$를 $$\alpha:i\rightarrow j$$로 표기한다.

</div>

같은 source와 target을 가지는 여러 개의 arrow가 존재할 수 있고, $$s(\alpha)=t(\alpha)$$인 arrow, 곧 *loop*도 허용된다. 이제 arrow들을 이어붙여 얻어지는 path를 정의한다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> Quiver $$Q$$에서 길이 $$\ell\geq 1$$인 *path<sub>경로</sub>*는 arrow들의 나열

$$p=\alpha_\ell\alpha_{\ell-1}\cdots\alpha_1$$

로서, 각 $$1\leq r<\ell$$에 대하여 $$t(\alpha_r)=s(\alpha_{r+1})$$을 만족하는 것이다. 즉 $$\alpha_1$$의 target이 $$\alpha_2$$의 source가 되는 식으로 이어진다. 이 path의 source와 target을 $$s(p)=s(\alpha_1)$$, $$t(p)=t(\alpha_\ell)$$로 정의한다. 추가로 각 vertex $$i\in Q_0$$에 대하여 길이 $$0$$인 *trivial path<sub>자명한 경로</sub>* $$e_i$$를 두고, $$s(e_i)=t(e_i)=i$$로 정의한다.

</div>

Path를 적는 순서에는 두 가지 관행이 있는데, 우리는 함수의 합성과 같은 방향, 곧 오른쪽에서 왼쪽으로 읽는 순서를 택하였다. 이렇게 두면 arrow $$\alpha:i\rightarrow j$$에 선형사상 $$x_\alpha$$를 대응시켰을 때 path $$\alpha_\ell\cdots\alpha_1$$이 합성 $$x_{\alpha_\ell}\circ\cdots\circ x_{\alpha_1}$$에 대응하여 표기가 일관된다. 우리는 $$Q$$의 모든 path들의 집합, 곧 길이 $$0$$인 trivial path들과 길이 $$\geq 1$$인 path들을 합한 집합을 가지고 다음 절에서 대수를 구성한다.

## 경로대수

Path들을 형식적인 basis로 삼고, 두 path를 이어붙이는 연산을 곱셈으로 삼으면 $$k$$ 위의 대수를 얻는다. 두 path를 이어붙일 수 없을 때, 곧 한쪽의 target과 다른 쪽의 source가 맞지 않을 때는 곱을 $$0$$으로 둔다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> Quiver $$Q$$와 field $$k$$에 대하여, *path algebra<sub>경로대수</sub>* $$kQ$$는 $$Q$$의 모든 path들을 basis로 가지는 $$k$$-벡터공간이다. 두 path $$p,q$$에 대하여 그 곱을

$$p\cdot q=\begin{cases}pq&\text{if }s(p)=t(q)\\0&\text{otherwise}\end{cases}$$

으로 정의한다. 여기서 $$pq$$는 $$q$$ 다음에 $$p$$를 이어붙여 얻는 path이며, trivial path $$e_i$$가 곱해지는 경우에는 $$e_{t(p)}\,p=p=p\,e_{s(p)}$$로 약속한다. 이 곱셈을 $$k$$-bilinear하게 확장하여 $$kQ$$ 위의 곱셈을 정의한다.

</div>

정의에서 곱 $$p\cdot q$$가 $$0$$이 아니려면 $$q$$의 target $$t(q)$$가 $$p$$의 source $$s(p)$$와 일치해야 하며, 이는 함수를 합성할 때 안쪽 함수의 치역이 바깥쪽 함수의 정의역과 맞아야 하는 것과 같다. 곱셈을 basis인 path들 위에서 정의한 뒤 양변에 대해 선형으로 확장하였으므로, $$kQ$$의 일반적인 두 원소의 곱은 각 path 곱들의 $$k$$-선형결합이다. 이 곱셈이 실제로 결합대수의 구조를 줌을 확인한다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> $$kQ$$는 [정의 3](#def3)의 곱셈에 대하여 associative $$k$$-algebra이며, 원소

$$1=\sum_{i\in Q_0}e_i$$

을 항등원으로 가진다. 따라서 $$kQ$$는 associative unital $$k$$-algebra이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

곱셈을 basis 위에서 정의하고 bilinear하게 확장하였으므로, 곱셈이 $$k$$-bilinear인 것은 정의에 의하여 성립한다. 결합법칙은 basis인 path들에 대해서만 확인하면 충분하다. 세 path $$p,q,r$$를 택하자. $$(p\cdot q)\cdot r$$과 $$p\cdot(q\cdot r)$$이 모두 $$0$$이 아니려면, 각 곱이 정의되기 위한 조건

$$s(p)=t(q),\qquad s(q)=t(r)$$

이 모두 성립해야 한다. 이 조건이 성립하지 않으면 양변 모두 $$0$$이므로 등식이 성립한다. 두 조건이 성립할 때, $$pq$$는 source가 $$s(q)$$이고 target이 $$t(p)$$인 path이며 $$qr$$는 source가 $$s(r)$$이고 target이 $$t(q)$$인 path이다. 그럼 $$(pq)\cdot r$$는 $$s(pq)=s(q)=t(r)$$이므로 정의되고, $$p\cdot(qr)$$는 $$s(p)=t(q)=t(qr)$$이므로 정의된다. 두 경우 모두 arrow들의 나열로서 $$p$$의 arrow들 뒤에 $$q$$의 arrow들, 그 뒤에 $$r$$의 arrow들을 이어붙인 동일한 path $$pqr$$를 얻으므로

$$(p\cdot q)\cdot r=pqr=p\cdot(q\cdot r)$$

이다. Trivial path가 끼는 경우도 $$e_i$$가 양옆의 path를 그대로 둔다는 약속으로부터 같은 결론을 얻는다. 따라서 결합법칙이 성립한다.

다음으로 $$1=\sum_{i\in Q_0}e_i$$이 항등원임을 보인다. 임의의 path $$p$$에 대하여

$$1\cdot p=\sum_{i\in Q_0}e_i\cdot p$$

인데, $$e_i\cdot p$$는 $$s(e_i)=i$$가 $$t(p)$$와 일치할 때, 곧 $$i=t(p)$$일 때만 $$0$$이 아니고 그 값은 $$p$$이다. 따라서 $$1\cdot p=p$$이다. 마찬가지로 $$p\cdot 1=\sum_{i\in Q_0}p\cdot e_i$$에서 $$p\cdot e_i$$는 $$t(e_i)=i$$가 $$s(p)$$와 일치할 때, 곧 $$i=s(p)$$일 때만 $$0$$이 아니고 그 값은 $$p$$이므로 $$p\cdot 1=p$$이다. 선형성에 의하여 $$1$$은 $$kQ$$ 전체의 항등원이다.

</details>

명제 4의 trivial path들 $$e_i$$는 단순한 항등원의 조각이 아니라 그 자체로 구조적인 의미를 가진다. 각 $$e_i$$에 대하여 $$e_i\cdot e_i=e_i$$이고, $$i\neq j$$이면 $$e_i\cdot e_j=0$$이므로 $$\{e_i\}_{i\in Q_0}$$은 서로 직교하는 idempotent들의 모임을 이루며, 그 합이 $$1$$이다. 더 나아가 임의의 path $$p$$에 대하여 $$e_{t(p)}\,p\,e_{s(p)}=p$$가 성립하므로, $$e_i\,kQ\,e_j$$는 정확히 source가 $$j$$이고 target이 $$i$$인 path들이 생성하는 부분공간이다.

$$kQ$$의 곱셈은 일반적으로 commutative가 아니다. 가령 arrow $$\alpha:1\rightarrow 2$$가 있으면 $$\alpha=e_2\,\alpha\,e_1$$이고 $$e_1\,\alpha=0$$이므로 $$\alpha\,e_1=\alpha\neq 0=e_1\,\alpha$$이다. 한편 $$kQ$$의 $$k$$ 위의 차원은 $$Q$$의 path의 개수와 같으므로, 다음 명제가 path algebra가 유한차원이 되는 경우를 정확히 가려낸다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> $$kQ$$가 유한차원 $$k$$-algebra인 것은 $$Q$$가 *oriented cycle*, 곧 길이 $$\geq 1$$이면서 source와 target이 같은 path를 가지지 않는 것과 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$kQ$$의 차원은 $$Q$$의 path의 개수이고, $$Q_0$$와 $$Q_1$$이 모두 유한이므로 이는 곧 path의 개수가 유한한지를 묻는 것이다.

먼저 $$Q$$에 oriented cycle $$c=\alpha_\ell\cdots\alpha_1$$이 있다고 하자. 그럼 $$s(c)=t(c)$$이므로 $$c$$를 자기 자신과 임의의 횟수만큼 이어붙인

$$c,\ c c,\ c c c,\ \ldots$$

은 모두 서로 다른 길이의 path이고, 따라서 path의 개수는 무한이다. 곧 $$kQ$$는 무한차원이다.

거꾸로 $$Q$$에 oriented cycle이 없다고 하자. 길이 $$\geq 1$$인 path $$p=\alpha_\ell\cdots\alpha_1$$를 따라 vertex들의 나열

$$s(\alpha_1),\ t(\alpha_1)=s(\alpha_2),\ \ldots,\ t(\alpha_\ell)$$

을 생각하면, 만일 이 나열에서 어떤 vertex가 두 번 등장한다면 그 사이의 arrow들이 oriented cycle을 이루어 가정에 모순이다. 따라서 path 위의 vertex들은 모두 서로 다르며, path의 길이는 $$\lvert Q_0\rvert$$를 넘을 수 없다. 길이가 $$\lvert Q_0\rvert$$ 이하인 path는 유한개의 arrow를 유한 번 이어붙인 것이므로 유한개뿐이고, trivial path도 $$\lvert Q_0\rvert$$개이다. 따라서 path의 개수는 유한이며 $$kQ$$는 유한차원이다.

</details>

## 경로대수의 예시

추상적인 정의를 구체적인 quiver 몇 개에 적용해 본다. 첫 번째 예시는 vertex들이 일렬로 늘어선 선형 quiver이며, 이는 다음 글들에서 indecomposable representation의 분류를 다룰 때 가장 기본이 되는 예시이다.

<div class="example" markdown="1">

<ins id="ex6">**예시 6**</ins> $$n\geq 1$$에 대하여 *선형 $$A_n$$ quiver*를 vertex 집합 $$Q_0=\{1,2,\ldots,n\}$$과 arrow $$\alpha_i:i\rightarrow i+1$$ ($$1\leq i\leq n-1$$) 로 정의한다.

$$1\xrightarrow{\ \alpha_1\ }2\xrightarrow{\ \alpha_2\ }3\rightarrow\cdots\rightarrow n-1\xrightarrow{\ \alpha_{n-1}\ }n$$

이 quiver에는 oriented cycle이 없으므로 [명제 5](#prop5)에 의하여 $$kQ$$는 유한차원이다. 각 $$i\leq j$$에 대하여 $$i$$에서 $$j$$로 가는 path는

$$\alpha_{j-1}\alpha_{j-2}\cdots\alpha_i$$

하나뿐이고 ($$i=j$$일 때는 $$e_i$$), $$i>j$$인 경우에는 $$i$$에서 $$j$$로 가는 path가 없다. 따라서 path의 총 개수는 $$\binom{n+1}{2}$$이며 $$kQ$$의 차원은 $$\binom{n+1}{2}$$이다. 이 path algebra는 $$k$$ 위의 $$n\times n$$ 하삼각행렬들이 이루는 대수와 isomorphic하다. $$i$$에서 $$j$$로 가는 유일한 path를 행렬단위 $$E_{ji}$$ (단, $$(j,i)$$ 성분만 $$1$$) 에 대응시키면, path의 concatenation이 행렬단위의 곱

$$E_{kj}E_{ji}=E_{ki},\qquad E_{kl}E_{ji}=0\ (l\neq j)$$

과 정확히 같은 규칙을 따르고, trivial path $$e_i$$는 대각성분 $$E_{ii}$$에 대응하기 때문이다.

</div>

위 예시에서 path algebra가 행렬대수의 부분대수로 실현되는 것은 path algebra를 곱셈규칙이 path의 잇기로 주어지는 행렬과 같다고 보는 관점을 잘 보여 준다. 다음 예시는 oriented cycle을 가지는 가장 단순한 경우이다.

<div class="example" markdown="1">

<ins id="ex7">**예시 7**</ins> *one-loop quiver*를 vertex 하나 $$Q_0=\{1\}$$과 loop $$\alpha:1\rightarrow 1$$ 하나로 정의한다. 이 quiver의 path는 trivial path $$e_1$$과, $$\alpha$$를 $$m\geq 1$$번 이어붙인 $$\alpha^m$$들이다. 모든 path가 $$1$$에서 $$1$$로 가므로 임의의 두 path는 항상 이어붙일 수 있고, 그 곱은

$$\alpha^m\cdot\alpha^{m'}=\alpha^{m+m'}$$

이다 (단, $$\alpha^0=e_1$$). 따라서 대응 $$\alpha^m\mapsto \x^m$$은 $$k$$-algebra isomorphism

$$kQ\xrightarrow{\ \cong\ }k[\x]$$

을 준다. 실제로 이 대응은 basis $$\{e_1,\alpha,\alpha^2,\ldots\}$$를 polynomial algebra의 basis $$\{1,\x,\x^2,\ldots\}$$로 일대일로 보내고 곱셈규칙 $$\alpha^m\cdot\alpha^{m'}=\alpha^{m+m'}$$이 $$\x^m\x^{m'}=\x^{m+m'}$$과 일치하므로, 선형으로 확장하면 곱셈을 보존하는 가역사상이 된다. 특히 $$kQ\cong k[\x]$$은 commutative이고 무한차원이다. 후자는 one-loop quiver가 oriented cycle $$\alpha$$를 가진다는 사실과 [명제 5](#prop5)에 부합한다.

</div>

마지막 예시는 다중 arrow를 가지는 경우로, indecomposable representation의 구조가 풍부하여 표현론에서 핵심적인 역할을 한다.

<div class="example" markdown="1">

<ins id="ex8">**예시 8**</ins> *Kronecker quiver*를 vertex 집합 $$Q_0=\{1,2\}$$과 $$1$$에서 $$2$$로 가는 두 arrow $$\alpha,\beta:1\rightarrow 2$$로 정의한다.

$$1\ \substack{\xrightarrow{\ \alpha\ }\\[-0.3em]\xrightarrow{\ \beta\ }}\ 2$$

이 quiver에는 oriented cycle이 없으므로 [명제 5](#prop5)에 의하여 $$kQ$$는 유한차원이다. Path는 trivial path $$e_1,e_2$$와 두 arrow $$\alpha,\beta$$의 넷뿐이며, 길이 $$2$$ 이상의 path는 없다. $$\alpha$$와 $$\beta$$의 source가 모두 $$1$$이고 target이 모두 $$2$$이므로 $$\alpha\cdot\beta$$와 $$\beta\cdot\alpha$$는 둘 다 source와 target이 맞지 않아 $$0$$이기 때문이다. 따라서 $$\dim_k kQ=4$$이고, $$kQ$$는 $$k$$ 위의 행렬대수

$$\begin{pmatrix}k&0\\k^2&k\end{pmatrix}=\left\{\begin{pmatrix}a&0\\v&b\end{pmatrix}\ \middle\vert\ a,b\in k,\ v\in k^2\right\}$$

과 isomorphic하다. 여기서 $$e_1,e_2$$는 두 대각성분에, $$\alpha,\beta$$는 왼쪽 아래의 $$k^2$$ 자리의 두 basis에 대응한다.

</div>

## Quiver의 representation

이제 path algebra의 module을 직접 다루는 대신, 그와 동등하면서도 더 기하학적인 자료인 representation을 정의한다. Representation은 각 vertex에 벡터공간을, 각 arrow에 선형사상을 배정한 것이다.

<div class="definition" markdown="1">

<ins id="def9">**정의 9**</ins> Quiver $$Q$$의 *representation<sub>표현</sub>* $$V$$는 다음의 자료로 이루어진다. 각 vertex $$i\in Q_0$$에 $$k$$-벡터공간 $$V_i$$를 배정하고, 각 arrow $$\alpha:i\rightarrow j$$에 $$k$$-선형사상

$$V_\alpha:V_i\rightarrow V_j$$

를 배정한다. 모든 $$V_i$$가 유한차원일 때 $$V$$를 *유한차원 representation*이라 부른다.

</div>

Representation $$V$$를 적을 때 우리는 각 vertex 위의 벡터공간과 각 arrow 위의 선형사상을 명시한다. 가령 선형 $$A_2$$ quiver $$1\xrightarrow{\alpha}2$$의 representation은 두 벡터공간 $$V_1,V_2$$와 하나의 선형사상 $$V_\alpha:V_1\rightarrow V_2$$를 정하는 것, 곧 선형사상 하나를 정하는 것과 같다. 두 representation 사이의 사상은 각 vertex에서의 선형사상이 arrow를 따라 호환되는 것으로 정의한다.

<div class="definition" markdown="1">

<ins id="def10">**정의 10**</ins> Quiver $$Q$$의 두 representation $$V,W$$에 대하여, $$V$$에서 $$W$$로의 *morphism* $$f=(f_i)_{i\in Q_0}$$은 각 vertex $$i$$마다 주어진 선형사상 $$f_i:V_i\rightarrow W_i$$들의 모임으로서, 각 arrow $$\alpha:i\rightarrow j$$에 대하여

$$f_j\circ V_\alpha=W_\alpha\circ f_i$$

를 만족하는 것이다. 즉 다음 diagram이 commute한다.

![quiver representation 사상의 commutativity](/assets/images/Math/Representation_Theory/Path_Algebras-1.svg){:style="width:7.13em" class="invert" .align-center}

</div>

각 vertex에서 $$f_i$$가 모두 isomorphism이면 $$f$$를 *isomorphism*이라 부른다. Morphism의 합성은 vertex별 합성 $$(g\circ f)_i=g_i\circ f_i$$으로 정의하며, 이것이 다시 morphism의 조건을 만족함은 각 vertex에서의 commutativity를 이어붙이면 곧바로 따라온다. 이로써 $$Q$$의 representation들을 대상으로, 위의 morphism들을 사상으로 하는 category를 얻으며, 이를 $$\Rep(Q)$$로 표기한다. 우리는 주로 유한차원 representation들이 이루는 full subcategory를 다룬다.

Representation에 대해서도 module에서와 같은 부분구조와 연산을 정의할 수 있다. 핵심은 모든 구성이 vertex별로, arrow와 호환되도록 이루어진다는 것이다.

<div class="definition" markdown="1">

<ins id="def11">**정의 11**</ins> Quiver $$Q$$의 representation $$V$$에 대하여 다음을 정의한다.

1. 각 vertex $$i$$마다 부분공간 $$W_i\subseteq V_i$$가 주어지고, 모든 arrow $$\alpha:i\rightarrow j$$에 대하여 $$V_\alpha(W_i)\subseteq W_j$$가 성립할 때, 자료 $$(W_i, V_\alpha\vert_{W_i})$$을 $$V$$의 *subrepresentation<sub>부분표현</sub>*이라 부른다.
2. 두 representation $$V,W$$의 *direct sum<sub>직합</sub>* $$V\oplus W$$는 각 vertex에 $$V_i\oplus W_i$$를, 각 arrow $$\alpha:i\rightarrow j$$에 선형사상

$$V_\alpha\oplus W_\alpha:V_i\oplus W_i\rightarrow V_j\oplus W_j$$

를 배정하여 얻는 representation이다.

</div>

Subrepresentation에서 부분공간들이 arrow를 따라 닫혀 있어야 한다는 조건은 morphism의 commutativity 조건을 부분공간에 제한한 것이며, 이 조건 덕분에 제한된 선형사상 $$V_\alpha\vert_{W_i}:W_i\rightarrow W_j$$가 잘 정의된다. Direct sum의 경우 포함사상 $$V\hookrightarrow V\oplus W$$와 사영사상 $$V\oplus W\twoheadrightarrow V$$가 모두 $$\Rep(Q)$$의 morphism이 되며, 이는 module의 direct sum이 가지는 보편적 성질 ([\[대수적 구조\] §가군의 직접곱과 직합, 텐서곱, ⁋정리 1](/ko/math/algebraic_structures/operations_of_modules#thm1)) 의 representation 판본이다. 이러한 평행성은 우연이 아니며, 다음 절에서 보일 category 동치로 완전히 설명된다.

## $$\Rep(Q)$$와 $$kQ$$-module의 동치

이 글의 주된 정리는 quiver의 representation이 path algebra 위의 module과 본질적으로 같은 자료라는 것이다. 직관적으로, representation $$V$$가 주어지면 각 vertex의 공간들을 모두 모은 $$M=\bigoplus_i V_i$$ 위에 path들이 작용하게 만들 수 있다. Trivial path $$e_i$$는 $$M$$을 $$i$$번째 성분 $$V_i$$로 사영하는 사상으로, arrow $$\alpha:i\rightarrow j$$는 $$V_\alpha$$를 통해 $$V_i$$를 $$V_j$$로 보내는 사상으로 작용시키는 것이다. 거꾸로 $$kQ$$-module $$M$$이 주어지면 idempotent $$e_i$$가 잘라내는 부분공간 $$e_iM$$을 vertex $$i$$ 위의 공간으로, arrow의 작용을 그 사이의 선형사상으로 회복할 수 있다.

<div class="proposition" markdown="1">

<ins id="thm12">**정리 12**</ins> Quiver $$Q$$와 field $$k$$에 대하여, 위에서 서술한 대응은 category 동치

$$\Rep(Q)\cong \lMod{kQ}$$

를 준다. 이 동치는 유한차원 representation들과 $$k$$ 위에서 유한차원인 $$kQ$$-module들 사이의 동치로 제한된다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

두 방향의 functor를 구성하고 이들이 서로 역임을 보인다.

**Representation에서 module으로.** Representation $$V=(V_i,V_\alpha)$$가 주어졌다 하자. $$k$$-벡터공간

$$M=\bigoplus_{i\in Q_0}V_i$$

위에 $$kQ$$-action을 정의한다. 곱셈을 basis인 path들 위에서 정의하면 충분하다. Trivial path $$e_i$$는 $$M$$에서 $$V_i$$로의 사영을 $$M$$ 안으로 다시 넣은 사상으로 작용시키고, arrow $$\alpha:i\rightarrow j$$는 먼저 $$V_i$$ 성분으로 사영한 뒤 $$V_\alpha$$를 적용하여 $$V_j$$ 성분에 넣는 사상으로 작용시킨다. 길이 $$\geq 1$$인 path $$p=\alpha_\ell\cdots\alpha_1$$은 합성

$$V_{\alpha_\ell}\circ\cdots\circ V_{\alpha_1}$$

(을 적절한 성분에 넣은 것) 으로 작용시킨다. 이 작용이 $$kQ$$-module 구조를 줌을 확인하자. 우선 $$\sum_i e_i$$는 각 성분 $$V_i$$를 그대로 두므로 $$M$$ 위에서 항등사상으로 작용한다. 또 두 path $$p,q$$에 대하여, $$s(p)\neq t(q)$$이면 $$q$$의 작용의 image는 $$V_{t(q)}$$ 성분에 놓이는데 $$p$$의 작용은 $$V_{s(p)}$$ 성분에서만 비자명하므로 합성이 $$0$$이고, 이는 $$kQ$$에서 $$p\cdot q=0$$인 것과 일치한다. $$s(p)=t(q)$$이면 $$p$$의 작용과 $$q$$의 작용의 합성은 path $$pq$$를 따라 선형사상들을 차례로 합성한 것이며, 이는 $$pq$$의 작용과 같다. 따라서 작용은 곱셈을 보존하고 $$M$$은 left $$kQ$$-module이다. 이 대응을 $$M=F(V)$$로 적는다. Morphism $$f:V\rightarrow W$$에 대해서는 $$F(f)=\bigoplus_i f_i:\bigoplus_i V_i\rightarrow\bigoplus_i W_i$$로 정의한다. 이것이 $$kQ$$-linear임은, $$e_i$$의 작용과 $$F(f)$$의 교환은 $$f$$가 성분을 보존한다는 사실로부터, arrow $$\alpha$$의 작용과의 교환은 정확히 [정의 10](#def10)의 조건 $$f_j\circ V_\alpha=W_\alpha\circ f_i$$로부터 따라온다.

**Module에서 representation으로.** Left $$kQ$$-module $$M$$이 주어졌다 하자. 각 vertex $$i$$에 대하여

$$V_i=e_iM$$

으로 두고, 각 arrow $$\alpha:i\rightarrow j$$에 대하여 선형사상 $$V_\alpha:V_i\rightarrow V_j$$를 $$m\mapsto \alpha m$$으로 정의한다. 이것이 잘 정의됨을 보이자. $$m\in e_iM$$이면 $$e_im=m$$이고, $$\alpha=e_j\alpha e_i$$이므로

$$\alpha m=\alpha e_i m=e_j\alpha e_i m=e_j(\alpha m)\in e_jM=V_j$$

이다. 곧 $$V_\alpha$$의 image가 $$V_j$$에 놓인다. 한편 $$\{e_i\}$$이 서로 직교하는 idempotent이고 그 합이 $$1$$이므로

$$M=1\cdot M=\sum_{i\in Q_0}e_iM=\bigoplus_{i\in Q_0}V_i$$

이다. 직합인 것은 $$e_ie_j=\delta_{ij}e_i$$에 의하여 각 $$e_iM$$이 서로 만나지 않기 때문이다. 이 대응을 $$V=G(M)$$으로 적는다. Module homomorphism $$\varphi:M\rightarrow N$$에 대해서는 $$G(\varphi)_i=\varphi\vert_{e_iM}:e_iM\rightarrow e_iN$$으로 정의한다. $$\varphi$$가 $$e_i$$와 교환하므로 $$\varphi(e_iM)\subseteq e_iN$$이어서 제한이 잘 정의되고, $$\alpha$$와의 교환으로부터 [정의 10](#def10)의 commutativity 조건이 성립하여 $$G(\varphi)$$는 morphism이다.

**두 functor가 서로 역.** Representation $$V$$에서 출발하여 $$G(F(V))$$를 계산하면, $$F(V)=\bigoplus_i V_i$$ 위에서 $$e_i$$의 작용이 $$V_i$$ 성분으로의 사영이므로 $$e_i\bigl(\bigoplus_j V_j\bigr)=V_i$$이고, arrow $$\alpha$$의 작용은 정의에 의하여 $$V_\alpha$$이다. 따라서 $$G(F(V))=V$$이며, 이 동일시는 morphism에 대해서도 자연스럽다. 거꾸로 module $$M$$에서 출발하면, $$G(M)$$의 vertex 공간은 $$e_iM$$이고 그 direct sum은 위에서 본 것처럼 $$M$$ 자신이며, 이 동일시 아래에서 path $$p$$의 작용은 $$G(M)$$ 위에서 정의한 arrow별 작용의 합성과 일치한다. 따라서 $$F(G(M))=M$$이다. 두 동일시가 natural isomorphism을 이루므로 $$F,G$$는 서로 quasi-inverse인 functor이고, $$\Rep(Q)\cong\lMod{kQ}$$이다.

마지막으로 차원에 관한 주장을 보자. $$V$$가 유한차원이면 $$\dim_k F(V)=\sum_i\dim_k V_i<\infty$$이고, 거꾸로 $$M$$이 $$k$$ 위에서 유한차원이면 각 $$V_i=e_iM$$이 $$M$$의 부분공간으로서 유한차원이다. 따라서 동치는 유한차원 대상들 사이로 제한된다.

</details>

정리 12의 동치 아래에서 [정의 11](#def11)의 representation 구성들은 정확히 module의 대응하는 구성으로 번역된다. Subrepresentation은 $$kQ$$-submodule에 대응하는데, 부분공간들이 arrow를 따라 닫혀 있다는 조건이 바로 $$\bigoplus_i W_i$$가 $$kQ$$의 작용에 대하여 닫혀 있다는 조건이기 때문이다. 마찬가지로 representation의 direct sum은 module의 direct sum에 대응한다. 따라서 representation에 대한 모든 분해 이론을 module의 언어로, 또는 그 반대로 옮길 수 있으며, 우리는 다음 글들에서 이 자유로운 번역을 전제로 한다.

이 동치는 또한 representation을 다룰 때 굳이 path algebra 전체를 명시하지 않고 quiver의 자료만으로 작업해도 좋다는 것을 정당화한다. 가령 선형 $$A_2$$ quiver의 representation은 선형사상 $$V_\alpha:V_1\rightarrow V_2$$ 하나이고, 이를 분류하는 것은 곧 선형사상을 isomorphism 차이를 무시하고 분류하는 문제, 곧 rank에 의한 분류이다. 
---

**참고문헌**

**[ASS]** I. Assem, D. Simson, and A. Skowroński, *Elements of the representation theory of associative algebras, Volume 1: Techniques of representation theory*, Cambridge University Press, 2006.

**[Sch]** R. Schiffler, *Quiver representations*, Springer, 2014.

**[DW]** H. Derksen and J. Weyman, *An introduction to quiver representations*, American Mathematical Society, 2017.
