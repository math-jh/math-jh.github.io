---
title: "최소다항식"
description: "행렬에 다항식을 대입하는 연산을 정의하고, 일차분해정리를 이용해 케일리-해밀턴 정리를 증명한다. 나아가 최소다항식을 도입하여 특성다항식을 나눈다는 사실과 대각화가능성의 판정법을 다룬다."
excerpt: "케일리-해밀턴 정리와 최소다항식"

categories: [Math / Linear Algebra]
permalink: /ko/math/linear_algebra/minimal_polynomial
sidebar: 
    nav: "linear_algebra-ko"


date: 2026-06-19

weight: 18

published: false

---

조르당 표준형을 통해 우리는 임의의 linear operator를 generalized eigenspace 위에서 "스칼라곱 더하기 nilpotent operator"의 형태로 분해하였다. 이 분해는 다항식과 linear operator 사이의 관계를 살펴보는 데에도 유용하게 쓰인다. 이번 글에서는 행렬에 다항식을 대입하는 연산을 정의하고, 이를 통해 케일리-해밀턴 정리와 최소다항식을 다룬다. 

## 행렬에서의 다항식

행렬의 거듭제곱과 스칼라곱, 그리고 덧셈은 모두 잘 정의되므로, 행렬에 다항식을 대입하는 것 또한 자연스럽게 정의된다. 이 글에서 $$\mathbb{K}[\x]$$는 [§부분공간, ⁋예시 5](/ko/math/linear_algebra/subspaces#ex5)에서 정의한 다항식들의 공간을 의미한다.

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

이제 임의의 행렬을 그 특성다항식에 대입하면 항상 영행렬이 된다는 놀라운 사실을 증명한다. 그 전에, nilpotent operator의 멱영지수가 공간의 차원을 넘지 못한다는 사실을 짚고 넘어가자. 

<div class="proposition" markdown="1">

<ins id="lem3">**보조정리 3**</ins> $$m$$차원 벡터공간 $$V$$ 위에 정의된 nilpotent operator $$N:V\rightarrow V$$에 대하여, $$N^m=0$$이 성립한다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[§조르당 표준형, ⁋보조정리 1](/ko/math/linear_algebra/Jordan_canonical_form#lem1)에 의하여 다음의 filtration

$$0=\ker N^0\subsetneq\ker N^1\subsetneq\cdots\subsetneq\ker N^k=\ker N^{k+1}=\cdots$$

이 존재하며, 여기서 $$k$$는 $$N$$의 멱영지수이다. $$N$$이 nilpotent이므로 적당한 정수에서 $$\ker N^k=V$$가 되어야 하고, 위 포함관계가 모두 진부분집합이므로 

$$0=\dim\ker N^0<\dim\ker N^1<\cdots<\dim\ker N^k=m$$

에서 각 단계마다 차원이 적어도 $$1$$씩 증가한다. 따라서 $$k\leq m$$이고, 특히 $$N^m=0$$이다.

</details>

<div class="proposition" markdown="1">

<ins id="thm4">**정리 4 (Cayley-Hamilton)**</ins> 유한차원 벡터공간 $$V$$ 위에 정의된 임의의 linear operator $$A:V\rightarrow V$$와 그 특성다항식 $$p_A$$에 대하여, $$p_A(A)=0$$이 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $$\mathbb{K}$$가 algebraically closed라 가정하자. [§조르당 표준형, ⁋정리 6](/ko/math/linear_algebra/Jordan_canonical_form#thm6)에 의하여 $$A$$의 서로 다른 eigenvalue들을 $$\lambda_1,\ldots,\lambda_r$$이라 할 때

$$V=G_{\lambda_1}(A)\oplus\cdots\oplus G_{\lambda_r}(A)$$

으로 분해된다. 각 $$\lambda=\lambda_i$$에 대하여 [§조르당 표준형](/ko/math/linear_algebra/Jordan_canonical_form)에서 살펴본 대로 $$(A-\lambda I)\vert_{G_\lambda(A)}$$는 $$G_\lambda(A)$$ 위의 nilpotent operator이고, 그 차원은 $$\dim G_\lambda(A)=d_\lambda$$이다. 여기서 $$d_\lambda$$는 $$\lambda$$의 대수적 중복도이다. 따라서 [보조정리 3](#lem3)에 의하여 

$$(A-\lambda I)^{d_\lambda}v=0\qquad\text{for all $v\in G_\lambda(A)$}$$

이 성립한다. 이제 $$p_A(\x)=\prod_{i=1}^r(\x-\lambda_i)^{d_{\lambda_i}}$$이므로, 임의의 $$v\in G_\lambda(A)$$에 대하여 [명제 2](#prop2)로부터 각 인수들이 commute한다는 사실을 이용하면

$$p_A(A)v=\left(\prod_{\mu\neq\lambda}(A-\mu I)^{d_\mu}\right)(A-\lambda I)^{d_\lambda}v=0$$

이다. $$V$$가 $$G_\lambda(A)$$들의 direct sum이므로 임의의 $$v\in V$$에 대하여 $$p_A(A)v=0$$이고, 따라서 $$p_A(A)=0$$이다. 

마지막으로 $$\mathbb{K}$$가 algebraically closed가 아닌 경우, $$p_A$$의 모든 근을 포함하는 field extension $$\mathbb{K}'\supseteq\mathbb{K}$$를 생각하면 ([\[체론\] §대수적 확장](/ko/math/field_theory/algebraic_extensions)) $$A$$를 $$\mathbb{K}'$$ 위의 행렬로 보았을 때 $$p_A(A)=0$$이 성립한다. 그런데 $$p_A(A)$$의 각 성분은 $$\mathbb{K}$$의 원소이므로, 이 등식은 $$\mathbb{K}$$ 위에서도 그대로 성립한다.

</details>

직관적으로 케일리-해밀턴 정리는, 특성다항식이 $$A$$의 모든 eigenvalue를 충분히 높은 중복도로 담고 있어 $$A$$를 대입하면 각 generalized eigenspace 위에서의 nilpotent 부분까지 모두 소멸시킨다는 것을 말한다. 

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

최소다항식의 근은 특성다항식의 근과 정확히 일치한다. 즉, 차수는 더 작을 수 있어도 어떤 eigenvalue도 빠뜨리지 않는다. 

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> $$n\times n$$ 행렬 $$A$$에 대하여, $$m_A$$의 근들의 집합은 $$A$$의 eigenvalue들의 집합과 같다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 임의의 다항식 $$p$$와 eigenvalue $$\lambda$$, 그리고 이에 해당하는 eigenvector $$v$$에 대하여 $$A^iv=\lambda^iv$$이므로 $$p(A)v=p(\lambda)v$$가 성립한다. 이제 $$\lambda$$가 $$A$$의 eigenvalue라 하고 $$v\neq 0$$을 이에 해당하는 eigenvector라 하면 

$$0=m_A(A)v=m_A(\lambda)v$$

이고 $$v\neq 0$$이므로 $$m_A(\lambda)=0$$이다. 즉 모든 eigenvalue는 $$m_A$$의 근이다. 거꾸로 $$\lambda$$가 $$m_A$$의 근이라 하면 [명제 6](#prop6)의 $$m_A\mid p_A$$로부터 $$\lambda$$는 $$p_A$$의 근, 즉 $$A$$의 eigenvalue이다.

</details>

이제 조르당 표준형을 이용하면 최소다항식의 정확한 형태를 결정할 수 있다. 다음 정리에서 $$e_\lambda$$는 generalized eigenspace $$G_\lambda(A)$$ 위에서의 nilpotent operator $$(A-\lambda I)\vert_{G_\lambda(A)}$$의 멱영지수, 즉 $$\lambda$$에 해당하는 가장 큰 Jordan block의 크기이다.

<div class="proposition" markdown="1">

<ins id="thm8">**정리 8**</ins> $$\mathbb{K}$$가 algebraically closed라 하자. $$n\times n$$ 행렬 $$A$$의 서로 다른 eigenvalue들을 $$\lambda_1,\ldots,\lambda_r$$이라 하면, 다음의 식

$$m_A(\x)=\prod_{i=1}^r(\x-\lambda_i)^{e_{\lambda_i}}$$

이 성립한다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$\lambda=\lambda_i$$를 하나 고정하고, $$N_\lambda=(A-\lambda I)\vert_{G_\lambda(A)}$$의 멱영지수를 $$e_\lambda$$라 하자. 임의의 monic polynomial $$p$$를 $$\lambda$$를 중심으로 전개하여

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

을 생각하자. 이 행렬의 특성다항식은 $$(\x-1)^3$$이고 유일한 eigenvalue $$1$$에 대하여 $$(A-I)^2\neq 0$$이지만 $$(A-I)^3=0$$이므로 $$e_1=3$$이다. 따라서 $$m_A(\x)=(\x-1)^3=p_A(\x)$$이고, 이는 일차식의 거듭제곱이므로 [따름정리 9](#cor9)에 의해 $$A$$는 diagonalizable가 아니다. 반면 행렬

$$B=\begin{pmatrix}0&1\\1&0\end{pmatrix}$$

의 특성다항식은 $$\x^2-1=(\x-1)(\x+1)$$이고, $$B^2=I$$이므로 $$(B-I)(B+I)=B^2-I=0$$이다. 따라서 $$m_B(\x)=(\x-1)(\x+1)$$인데, 이는 서로 다른 두 일차식의 곱이므로 [따름정리 9](#cor9)에 의해 $$B$$는 diagonalizable이다. 즉 대각화가능성을 가르는 것은 특성다항식이 아니라 최소다항식에 중복인수가 남는지의 여부이며, $$A$$의 경우 $$m_A=(\x-1)^3$$에 중복인수가 남아 대각화에 실패한다. 

</div>

---

**참고문헌**

**[Goc]** M.S. Gockenbach, *Finite-dimensional linear algebra*, Discrete Mathematics and its applications, Taylor&Francis, 2011.  
**[Hof]** K. Hoffman and R. Kunze, *Linear algebra*, 2nd ed., Prentice-Hall, 1971.  
**[Lee]** 이인석, *선형대수와 군*, 서울대학교 출판문화원, 2005.

---
