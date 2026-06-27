---
title: "최소다항식"
description: "행렬에 다항식을 대입하는 연산을 정의하고, 일차분해정리를 이용해 케일리-해밀턴 정리를 증명한다. 나아가 최소다항식을 도입하여 특성다항식을 나눈다는 사실과 대각화가능성의 판정법을 다룬다. 끝으로 작용소를 diagonalizable 부분과 nilpotent 부분으로 가르는 조르당-슈발레 분해를 구성한다."
excerpt: "케일리-해밀턴 정리와 최소다항식"

categories: [Math / Linear Algebra]
permalink: /ko/math/linear_algebra/minimal_polynomial
sidebar: 
    nav: "linear_algebra-ko"


date: 2026-06-28

weight: 18
---

Jordan canonical form을 통해 우리는 임의의 linear operator를 generalized eigenspace 위에서 Jordan block들로 분해하였다. 이러한 구조는 다항식과 linear operator 사이의 관계를 살펴보는 데에도 유용하게 쓰인다. 이번 글에서는 행렬에 다항식을 대입하는 연산을 정의하고, 이를 통해 케일리-해밀턴 정리와 최소다항식을 다룬다. 

## 행렬에서의 다항식

행렬의 거듭제곱과 스칼라곱, 그리고 덧셈은 모두 잘 정의되므로, 행렬에 다항식을 대입하는 것 또한 자연스럽게 정의된다. 이 글에서 $$\mathbb{K}[\x]$$는 [§부분공간, ⁋예시 5](/ko/math/linear_algebra/subspaces#ex5)에서 정의한 (유한차수) 다항식들의 공간을 의미한다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> $$n\times n$$ 행렬 $$A$$와 다항식 $$p(\x)=\sum_{i=0}^d a_i\x^i\in\mathbb{K}[\x]$$에 대하여, $$p$$에 $$A$$를 *대입<sub>evaluation</sub>*한 행렬을 다음의 식

$$p(A)=\sum_{i=0}^d a_iA^i=a_dA^d+\cdots+a_1A+a_0I$$

으로 정의한다. 여기서 $$A^0=I$$로 약속한다. 같은 정의를 linear operator $$L:V\rightarrow V$$에 대해서도 적용하여 $$p(L)$$을 정의한다.

</div>

이 대입은 다항식의 덧셈과 곱셈을 행렬의 그것으로 옮긴다. 특히 다음 명제는 앞으로의 논의에서 자주 쓰인다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> $$n\times n$$ 행렬 $$A$$와 임의의 두 다항식 $$p,q\in\mathbb{K}[\x]$$에 대하여, 다음의 두 식

$$(p+q)(A)=p(A)+q(A),\qquad (pq)(A)=p(A)q(A)$$

이 성립한다. 특히 $$p(A)$$와 $$q(A)$$는 commute한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

덧셈에 대한 식은 정의로부터 자명하다. 곱셈의 경우, $$p(\x)=\sum_i a_i\x^i$$, $$q(\x)=\sum_j b_j\x^j$$이라 하면 $$pq$$의 $$\x^k$$의 계수는 $$\sum_{i+j=k}a_ib_j$$이므로

$$(pq)(A)=\sum_k\left(\sum_{i+j=k}a_ib_j\right)A^k=\sum_{i,j}a_ib_jA^{i+j}=\left(\sum_i a_iA^i\right)\left(\sum_j b_jA^j\right)=p(A)q(A)$$

이다. 여기서 $$A^iA^j=A^{i+j}=A^jA^i$$인 것을 사용하였다. 마지막으로 다항식의 곱셈은 commute하므로 $$p(A)q(A)=(pq)(A)=(qp)(A)=q(A)p(A)$$이다.

</details>

## 케일리-해밀턴 정리

이제 임의의 행렬을 그 특성다항식에 대입하면 항상 영행렬이 된다는 놀라운 사실을 증명한다. 그 전에, nilpotent operator의 nilpotency index가 공간의 차원을 넘지 못한다는 (당연한) 사실을 짚고 넘어가자. 

<div class="proposition" markdown="1">

<ins id="lem3">**보조정리 3**</ins> $$m$$차원 벡터공간 $$V$$ 위에 정의된 nilpotent operator $$N:V\rightarrow V$$에 대하여, $$N^m=0$$이 성립한다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[§조르당 표준형, ⁋보조정리 1](/ko/math/linear_algebra/Jordan_canonical_form#lem1)에 의하여 다음의 filtration

$$0=\ker N^0\subsetneq\ker N^1\subsetneq\cdots\subsetneq\ker N^k=\ker N^{k+1}=\cdots$$

이 존재하며, 여기서 $$k$$는 $$N$$의 nilpotency index이다. $$N$$이 nilpotent이므로 적당한 정수에서 $$\ker N^k=V$$가 되어야 하고, 위 포함관계가 모두 진부분집합이므로 

$$0=\dim\ker N^0<\dim\ker N^1<\cdots<\dim\ker N^k=m$$

에서 각 단계마다 차원이 적어도 $$1$$씩 증가한다. 따라서 $$k\leq m$$이고, 특히 $$N^m=0$$이다.

</details>

그럼 다음을 증명할 수 있다.

<div class="proposition" markdown="1">

<ins id="thm4">**정리 4 (Cayley-Hamilton)**</ins> 유한차원 벡터공간 $$V$$ 위에 정의된 임의의 linear operator $$A:V\rightarrow V$$와 그 특성다항식 $$p_A$$에 대하여, $$p_A(A)=0$$이 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$\mathbb{K}$$가 algebraically closed라 가정하자. [§조르당 표준형, ⁋정리 6](/ko/math/linear_algebra/Jordan_canonical_form#thm6)에 의하여 $$A$$의 서로 다른 eigenvalue들을 $$\lambda_1,\ldots,\lambda_r$$이라 할 때

$$V=G_{\lambda_1}(A)\oplus\cdots\oplus G_{\lambda_r}(A)$$

으로 분해된다. 그럼 [§조르당 표준형](/ko/math/linear_algebra/Jordan_canonical_form)의 결과에 의하여, 각 $$\lambda=\lambda_i$$에 대해 $$(A-\lambda I)\vert_{G_\lambda(A)}$$는 $$G_\lambda(A)$$ 위의 nilpotent operator이고, 그 차원은 $$\dim G_\lambda(A)=d_\lambda$$이며 여기서 $$d_\lambda$$는 $$\lambda$$의 대수적 중복도이다. 따라서 [보조정리 3](#lem3)에 의하여 

$$(A-\lambda I)^{d_\lambda}v=0\qquad\text{for all $v\in G_\lambda(A)$}$$

이 성립한다. 이제 $$p_A(\x)=\prod_{i=1}^r(\x-\lambda_i)^{d_{\lambda_i}}$$이므로, 임의의 $$v\in G_\lambda(A)$$에 대하여 [명제 2](#prop2)로부터 각 인수들이 commute한다는 사실을 이용하면

$$p_A(A)v=\left(\prod_{\mu\neq\lambda}(A-\mu I)^{d_\mu}\right)(A-\lambda I)^{d_\lambda}v=0$$

이다. $$V$$가 $$G_\lambda(A)$$들의 direct sum이므로 임의의 $$v\in V$$에 대하여 $$p_A(A)v=0$$이고, 따라서 $$p_A(A)=0$$이다. 

</details>

우리는 $$\mathbb{K}$$가 algebraically closed field인 경우만 생각하였는데, 만일 그렇지 않다면 $$\mathbb{K}$$를 포함하는 아무 algebraically closed field $$\mathbb{L}$$를 생각한 후 (가령 $$\mathbb{R}$$의 경우 $$\mathbb{C}$$), $$p$$를 $$\mathbb{L}$$의 다항식으로 보면 된다. 이 때, $$A$$의 특성다항식은 $$\mathbb{L}$$에서도 마찬가지로 $$p_A$$이므로, 위의 증명에 의해 똑같이 $$p_A(A)=0$$임을 확인할 수 있으며, 이 다항식은 ($$\mathbb{L}$$에서의 다항식이라 하기는 하였지만) 모든 성분이 $$\mathbb{K}$$에 속하므로 이 등식이 $$\mathbb{K}$$에서도 성립한다. 다만, 이러한 $$\mathbb{L}$$의 존재성을 보이는 것은 현재 수준에서는 어려운 일이므로 증명 바깥에서 간략히 설명하였다. 어쨌든 직관적으로 케일리-해밀턴 정리는, 특성다항식이 $$A$$의 모든 eigenvalue를 충분히 높은 중복도로 담고 있어 $$A$$를 대입하면 각 generalized eigenspace 위에서의 nilpotent 부분까지 모두 소멸시킨다는 것을 말한다. 

## 최소다항식

케일리-해밀턴 정리는 $$p(A)=0$$을 만족하는 영이 아닌 다항식 $$p$$가 항상 존재함을 보여준다. 그러한 다항식 중 가장 간단한 것에 이름을 붙이자.

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> $$n\times n$$ 행렬 $$A$$에 대하여, $$p(A)=0$$을 만족하는 monic polynomial 가운데 차수가 가장 작은 것을 $$A$$의 *최소다항식<sub>minimal polynomial</sub>*이라 부르고 $$m_A$$로 적는다.

</div>

[정리 4](#thm4)에 의하여 $$p_A(A)=0$$이고, $$p_A$$를 최고차항의 계수로 나누면 monic polynomial을 얻으므로 위 정의에서 차수가 가장 작은 monic polynomial은 반드시 존재한다. 다음 명제는 이 최소다항식이 유일하며, $$A$$를 소멸시키는 모든 다항식을 나눈다는 것을 보여준다. 

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> $$n\times n$$ 행렬 $$A$$에 대하여, 다항식 $$p$$가 $$p(A)=0$$을 만족하면 $$m_A\mid p$$이다. 특히 $$A$$의 최소다항식은 유일하며, $$m_A\mid p_A$$가 성립한다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

다항식의 나눗셈 정리에 의하여, $$p=qm_A+r$$이고 $$r=0$$이거나 $$\deg r<\deg m_A$$이도록 하는 다항식 $$q,r$$이 존재한다. [명제 2](#prop2)에 의하여 

$$r(A)=p(A)-q(A)m_A(A)=0-q(A)\cdot 0=0$$

이다. 만일 $$r\neq 0$$이라면, $$r$$을 최고차항의 계수로 나누어 $$m_A$$보다 차수가 작으면서 $$A$$를 소멸시키는 monic polynomial을 얻게 되어 $$m_A$$의 최소성에 모순이다. 따라서 $$r=0$$이고 $$m_A\mid p$$이다. 

유일성을 보이기 위해 $$m_A'$$ 또한 최소다항식의 조건을 만족한다 하자. 그럼 위 논증에 의해 $$m_A\mid m_A'$$이고 $$m_A'\mid m_A$$이며, 둘 다 같은 차수의 monic polynomial이므로 $$m_A=m_A'$$이다. 마지막으로 [정리 4](#thm4)에서 $$p_A(A)=0$$이므로 $$m_A\mid p_A$$이다.

</details>

최소다항식의 근은 특성다항식의 근과 정확히 일치한다. 즉, 차수는 더 작을 수 있지만, 차수가 빠지는 방식은 중복된 eigenvalue에서 중복도를 낮추는 방식으로만 일어나며, 따라서 이 과정에서 어떤 eigenvalue도 빠뜨리지 않는다. 

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> $$n\times n$$ 행렬 $$A$$에 대하여, $$m_A$$의 근들의 집합은 $$A$$의 eigenvalue들의 집합과 같다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 임의의 다항식 $$p$$와 eigenvalue $$\lambda$$, 그리고 이에 해당하는 eigenvector $$v$$에 대하여 $$A^iv=\lambda^iv$$이므로 $$p(A)v=p(\lambda)v$$가 성립한다. 이제 $$\lambda$$가 $$A$$의 eigenvalue라 하고 $$v\neq 0$$을 이에 해당하는 eigenvector라 하면 

$$0=m_A(A)v=m_A(\lambda)v$$

이고 $$v\neq 0$$이므로 $$m_A(\lambda)=0$$이다. 즉 모든 eigenvalue는 $$m_A$$의 근이다. 거꾸로 $$\lambda$$가 $$m_A$$의 근이라 하면 [명제 6](#prop6)의 $$m_A\mid p_A$$로부터 $$\lambda$$는 $$p_A$$의 근, 즉 $$A$$의 eigenvalue이다.

</details>

이제 조르당 표준형을 이용하면 최소다항식의 정확한 형태를 결정할 수 있다. 다음 정리에서 $$e_\lambda$$는 generalized eigenspace $$G_\lambda(A)$$ 위에서의 nilpotent operator $$(A-\lambda I)\vert_{G_\lambda(A)}$$의 nilpotency index, 즉 $$\lambda$$에 해당하는 가장 큰 Jordan block의 크기이다.

<div class="proposition" markdown="1">

<ins id="thm8">**정리 8**</ins> $$\mathbb{K}$$가 algebraically closed라 하자. $$n\times n$$ 행렬 $$A$$의 서로 다른 eigenvalue들을 $$\lambda_1,\ldots,\lambda_r$$이라 하면, 다음의 식

$$m_A(\x)=\prod_{i=1}^r(\x-\lambda_i)^{e_{\lambda_i}}$$

이 성립한다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$\lambda=\lambda_i$$를 하나 고정하고, $$N_\lambda=(A-\lambda I)\vert_{G_\lambda(A)}$$의 nilpotency index를 $$e_\lambda$$라 하자. 임의의 monic polynomial $$p$$를 $$\lambda$$를 중심으로 전개하여

$$p(\x)=\sum_{j\geq 0}c_j(\x-\lambda)^j$$

이라 적으면, $$G_\lambda(A)$$ 위에서 $$(A-\lambda I)\vert_{G_\lambda(A)}=N_\lambda$$이므로 [명제 2](#prop2)에 의하여

$$p(A)\vert_{G_\lambda(A)}=\sum_{j\geq 0}c_jN_\lambda^j=\sum_{j=0}^{e_\lambda-1}c_jN_\lambda^j$$

이다. 마지막 등호는 $$j\geq e_\lambda$$에 대하여 $$N_\lambda^j=0$$인 것으로부터 따라온다. 한편 $$N_\lambda^{e_\lambda-1}\neq 0$$이므로 $$N_\lambda^{e_\lambda-1}w\neq 0$$인 $$w\in G_\lambda(A)$$가 존재하고, [§조르당 표준형, ⁋보조정리 8](/ko/math/linear_algebra/Jordan_canonical_form#lem8)에 의하여 $$w, N_\lambda w,\ldots, N_\lambda^{e_\lambda-1}w$$은 일차독립이다. 따라서 $$\sum_{j=0}^{e_\lambda-1}c_jN_\lambda^jw=0$$이려면 $$c_0=\cdots=c_{e_\lambda-1}=0$$이어야 하고, 결국 

$$p(A)\vert_{G_\lambda(A)}=0\iff (\x-\lambda)^{e_\lambda}\mid p$$

가 성립한다. 

이제 [§조르당 표준형, ⁋정리 6](/ko/math/linear_algebra/Jordan_canonical_form#thm6)의 분해 $$V=\bigoplus_i G_{\lambda_i}(A)$$로부터, $$p(A)=0$$인 것은 모든 $$i$$에 대하여 $$p(A)\vert_{G_{\lambda_i}(A)}=0$$인 것과 동치이고, 이는 다시 모든 $$i$$에 대하여 $$(\x-\lambda_i)^{e_{\lambda_i}}\mid p$$인 것, 즉 $$\prod_i(\x-\lambda_i)^{e_{\lambda_i}}\mid p$$인 것과 동치이다. 이러한 monic polynomial 가운데 차수가 가장 작은 것은 $$\prod_i(\x-\lambda_i)^{e_{\lambda_i}}$$ 자신이므로, 이것이 곧 $$m_A$$이다.

</details>

특히 최소다항식은 대각화가능성을 간결하게 판정해준다. 

<div class="proposition" markdown="1">

<ins id="cor9">**따름정리 9**</ins> $$\mathbb{K}$$가 algebraically closed라 하자. $$n\times n$$ 행렬 $$A$$가 diagonalizable인 것은 $$m_A$$가 서로 다른 일차식들의 곱, 즉

$$m_A(\x)=\prod_{i=1}^r(\x-\lambda_i)$$

의 꼴인 것과 동치이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$A$$가 diagonalizable인 것은 모든 eigenvalue $$\lambda$$에 대하여 $$\ker(A-\lambda I)^2=\ker(A-\lambda I)$$인 것, 즉 $$G_\lambda(A)=\ker(A-\lambda I)$$인 것과 동치이다. ([§고유공간분해, ⁋명제 12](/ko/math/linear_algebra/eigenspace_decomposition#prop12)) 이는 다시 모든 $$\lambda$$에 대하여 $$N_\lambda=0$$, 즉 $$e_\lambda=1$$인 것과 동치이다. [정리 8](#thm8)에 의하여 이는 $$m_A$$가 서로 다른 일차식들의 곱인 것과 동치이다. 

</details>

<div class="example" markdown="1">

<ins id="ex10">**예시 10**</ins> [§조르당 표준형, ⁋예시 2](/ko/math/linear_algebra/Jordan_canonical_form#ex2)의 행렬

$$A=\begin{pmatrix}1&1&1\\0&1&1\\0&0&1\end{pmatrix}$$

을 생각하자. 이 행렬의 특성다항식은 $$(\x-1)^3$$이고 유일한 eigenvalue $$1$$에 대하여 $$(A-I)^2\neq 0$$이지만 $$(A-I)^3=0$$이므로 $$e_1=3$$이다. 따라서 $$m_A(\x)=(\x-1)^3=p_A(\x)$$이고, 이는 일차식의 거듭제곱이므로 [따름정리 9](#cor9)에 의해 $$A$$는 diagonalizable이 아니다. 반면 행렬

$$B=\begin{pmatrix}0&1\\1&0\end{pmatrix}$$

의 특성다항식은 $$\x^2-1=(\x-1)(\x+1)$$이고, $$B^2=I$$이므로 $$(B-I)(B+I)=B^2-I=0$$이다. 따라서 $$m_B(\x)=(\x-1)(\x+1)$$인데, 이는 서로 다른 두 일차식의 곱이므로 [따름정리 9](#cor9)에 의해 $$B$$는 diagonalizable이다. 즉, 대각화가능성을 가르는 것은 특성다항식이 아니라 최소다항식에 중복인수가 남는지의 여부이며, $$A$$의 경우 $$m_A=(\x-1)^3$$에 중복인수가 남아 대각화에 실패한다. 

</div>

## 조르당-슈발레 분해

지금까지의 논의에서, 핵심적인 도구이자 motivation 역할을 한 것은 Jordan form이었다. 한편 각각의 Jordan block을 생각하면, 이 block은 두 개의 조각, 즉 eigenvalue를 담고 있는 diagonal part와, 그 위에 super-diagonal 성분으로 나타나는 nilpotent부분으로 나뉘었다. 우리는 지금까지의 논의를 적용하여, 이 분해를 공간 전체로 확장하는 작업으로 이 글을 마무리한다. 

우선 분해의 유일성에 필요한 세 가지 사실을 관찰해 두자. 

1. Diagonalizable이면서 동시에 nilpotent인 작용소는 $$0$$뿐이다. 그러한 작용소는 nilpotent이라 모든 eigenvalue가 $$0$$이고, diagonalizable이라 적당한 기저에서 모든 대각성분이 $$0$$인 대각행렬과 같기 때문이다. 
2. Commute하는 두 diagonalizable 작용소의 차는 다시 diagonalizable이다. [§고유공간분해, ⁋명제 10](/ko/math/linear_algebra/eigenspace_decomposition#prop10)에 의해 commute하는 두 diagonalizable operator는 simultaneously diagonalizable이므로, 공통의 고유기저에서 두 operator가 모두 대각이고 그 차 또한 같은 기저에서 대각이기 때문이다. 
3. Commute하는 두 nilpotent operator $$N,M$$의 차는 다시 nilpotent이다. $$N^a=M^b=0$$이면 $$N,M$$이 commute하므로 이항정리로부터 $$(N-M)^{a+b}=0$$이기 때문이다.

<div class="proposition" markdown="1">

<ins id="thm11">**정리 11 (조르당-슈발레 분해)**</ins> $$\mathbb{K}$$가 algebraically closed라 하자. 임의의 linear operator $$A:V\rightarrow V$$에 대하여, 다음을 만족하는 diagonalizable 작용소 $$A_s$$와 nilpotent 작용소 $$A_n$$이 유일하게 존재한다:

$$A=A_s+A_n,\qquad A_sA_n=A_nA_s.$$

나아가 $$A_s$$와 $$A_n$$은 상수항이 없는 $$A$$의 다항식으로 표현된다. $$A_s$$를 $$A$$의 diagonalizable 부분, $$A_n$$을 nilpotent 부분이라 부른다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

우선 존재성을 보이자. [§조르당 표준형, ⁋정리 6](/ko/math/linear_algebra/Jordan_canonical_form#thm6)에 의하여, $$A$$의 서로 다른 eigenvalue $$\lambda_1,\ldots,\lambda_r$$에 대해

$$V=G_{\lambda_1}(A)\oplus\cdots\oplus G_{\lambda_r}(A)$$

로 분해되고, [정리 8](#thm8)에서와 같이 $$(A-\lambda_iI)\vert_{G_{\lambda_i}(A)}$$의 nilpotency index를 $$e_i$$라 하면 $$G_{\lambda_i}(A)$$ 위에서 $$(A-\lambda_iI)^{e_i}=0$$이고 

$$m_A(\x)=\prod_{i=1}^r(\x-\lambda_i)^{e_i}$$

이다. 각 $$G_{\lambda_i}(A)$$ 위에서 $$A$$는 스칼라 $$\lambda_iI$$와 nilpotent operator $$A-\lambda_iI$$의 합이므로, 이를 전체로 모아 $$A_s$$를 각 $$G_{\lambda_i}(A)$$ 위에서 $$\lambda_iI$$로, $$A_n=A-A_s$$로 두면, $$A_s$$는 diagonalizable, $$A_n$$은 nilpotent이며, $$A_s$$가 각 조각에서 스칼라이므로 이들은 commute하여 분해 $$A=A_s+A_n$$을 얻는다.

따라서 주장의 핵심은 나머지 부분, 특히 다항식으로 표현된다는 부분이다. 이는 우선 서로 다른 $$\lambda_i$$에 대해 다항식 $$(\x-\lambda_i)^{e_i}$$들은 쌍마다 서로소이므로, 다음 조건

$$p(\x)\equiv\lambda_i\pmod{(\x-\lambda_i)^{e_i}}\quad(i=1,\ldots,r),\qquad p(\x)\equiv 0\pmod{\x}$$

를 모두 만족하는 다항식 $$p$$가 존재한다는 것부터 시작한다. 이는 중국인의 나머지정리의 일반화로, 그 명확한 statement와 증명은 환론에서 따로 다루게 된다. 어쨌든 이를 받아들이고 나면, 각 $$i$$에 대하여 $$p(\x)-\lambda_i$$는 $$(\x-\lambda_i)^{e_i}$$로 나누어떨어지므로 $$G_{\lambda_i}(A)$$ 위에서 $$(A-\lambda_iI)^{e_i}=0$$임을 쓰면 [명제 2](#prop2)로부터 $$p(A)-\lambda_iI=0$$, 즉 $$p(A)=\lambda_iI=A_s$$를 얻는다. 따라서 $$A_s=p(A)$$이고 $$p(0)=0$$이라 $$p$$는 상수항이 없으며, $$A_n=A-p(A)=q(A)$$ ($$q(\x)=\x-p(\x)$$) 또한 상수항이 없는 $$A$$의 다항식이다.

마지막으로 유일성을 보이기 위해 $$A=S+N$$이 같은 조건, 즉 $$S$$ diagonalizable, $$N$$ nilpotent, $$SN=NS$$을 만족한다 하자. 그럼 $$S$$와 $$N$$은 $$S+N=A$$와 commute하므로, $$A$$의 다항식인 $$A_s=p(A)$$, $$A_n=q(A)$$와도 commute한다. 이제 $$A=A_s+A_n=S+N$$으로부터

$$A_s-S=N-A_n$$

이다. 좌변에서 $$A_s$$와 $$S$$는 commute하는 두 diagonalizable operator들이므로 그 차는 diagonalizable이고, 우변에서 $$N$$과 $$A_n$$은 commute하는 두 nilpotent operator이므로 그 차는 nilpotent이다. 따라서 $$A_s-S$$는 diagonalizable이면서 동시에 nilpotent이라 $$0$$이고, 결국 $$A_s=S$$, $$A_n=N$$이다.

</details>

이 정리의 핵심적인 내용은, 그 증명에서도 알 수 있듯, 분해의 두 부분 $$A_s$$와 $$A_n$$이 $$A$$의 다항식이라는 점이다. 즉, 이들의 construction 자체는 Jordan canonical form으로부터 거의 바로 따라오지만, 이것이 $$A$$에 대한 다항식으로 나타난다는 사실이 가장 nontrivial하며, 그 쓸모도 가장 많다. 가령 다음이 성립한다. 

<div class="proposition" markdown="1">

<ins id="cor12">**따름정리 12**</ins> $$A_s$$와 $$A_n$$은 $$A$$와 commute하는 모든 operator $$B$$와 commute한다. 특히 $$A$$-invariant subspace들은 $$A_s$$-invariant이면서 $$A_n$$-invariant이기도 하다. 

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

[정리 11](#thm11)에서 $$A_s=p(A)$$, $$A_n=q(A)$$가 $$A$$의 다항식이다. $$AB=BA$$이면 $$A^iB=BA^i$$이므로 $$p(A)B=Bp(A)$$, $$q(A)B=Bq(A)$$이다. 또 $$W$$가 $$A$$-invariant, 즉 $$A(W)\subseteq W$$이면 모든 $$i$$에 대해 $$A^i(W)\subseteq W$$이므로 $$p(A)(W)\subseteq W$$, 즉 $$A_s(W)\subseteq W$$이고 마찬가지로 $$A_n(W)\subseteq W$$이다.

</details>

<div class="example" markdown="1">

<ins id="ex13">**예시 13**</ins> 행렬

$$A=\begin{pmatrix}2&1&0\\0&2&0\\0&0&3\end{pmatrix}$$

를 생각하자. eigenvalue $$2$$의 generalized eigenspace는 $$e_1,e_2$$가 생성하는 $$2$$차원 공간이고 그 위에서 $$A-2I$$의 nilpotency index는 $$2$$이며, eigenvalue $$3$$의 generalized eigenspace는 $$e_3$$이 생성한다. $$p(\x)=\x^2-4\x+6$$으로 두면 $$p(2)=2$$, $$p'(2)=0$$, $$p(3)=3$$이라 $$p$$는 [정리 11](#thm11)의 합동식 $$p\equiv 2\pmod{(\x-2)^2}$$, $$p\equiv 3\pmod{\x-3}$$을 만족하고,

$$A_s=p(A)=A^2-4A+6I=\begin{pmatrix}2&0&0\\0&2&0\\0&0&3\end{pmatrix},\qquad A_n=A-A_s=\begin{pmatrix}0&1&0\\0&0&0\\0&0&0\end{pmatrix}$$

이다. $$A_s$$는 diagonalizable, $$A_n$$은 nilpotent이며 두 작용소는 commute하고 $$A=A_s+A_n$$이다.

</div>

---

**참고문헌**

**[Goc]** M.S. Gockenbach, *Finite-dimensional linear algebra*, Discrete Mathematics and its applications, Taylor&Francis, 2011.  
**[Lee]** 이인석, *선형대수와 군*, 서울대학교 출판문화원, 2005.

---
