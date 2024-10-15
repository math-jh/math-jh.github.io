---

title: "행렬식"
excerpt: ""

categories: [Math / Linear Algebra]
permalink: /ko/math/linear_algebra/determinants
header:
    overlay_image: /assets/images/Math/Linear_Algebra/Determinants.png
    overlay_filter: 0.5
sidebar: 
    nav: "linear_algebra-ko"

date: 2024-10-07
last_modified_at: 2024-10-07
weight: 11

---

## 행렬식

앞선 글에서 우리는 임의의 free $A$-module $M$에 대하여, $M$이 basis $(e\_i)\_{i\in I}$를 갖는다면 다음의 식

$$e_J=e_{j_1}\wedge e_{j_2}\wedge\cdots\wedge e_{j_k},\qquad j_1<\cdots < j_k, \quad J=\{j_1,\ldots, j_k\}$$

의 꼴로 나타나는 원소 $e_J$들이 $\bigwedge(M)$의 basis가 되는 것을 확인했다. 특히, $\lvert J\rvert=n$을 만족하는 $J$들을 모아둔다면 이들은 $\bigwedge^n(M)$의 basis가 된다. 

이제 $M$이 유한한 basis $e_1,\ldots, e_n$을 갖는다 하자. 그럼 $\bigwedge^n(M)$의 basis는 단 하나의 원소 $e_1\wedge\cdots\wedge e_n$ 뿐이다. 한편 임의의 $u\in\End_\rMod{A}(M)$에 대하여, $\bigwedge$의 functoriality로부터 $\bigwedge^n(u):\bigwedge^n(M)\rightarrow\bigwedge^n(M)$이 유도되며, 위의 논의로부터 이 linear map은 반드시 $x\mapsto \alpha x$의 꼴로 쓰여야 한다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Free $A$-module $M$이 basis $(e\_i)\_{i\in I}$를 갖는다 하자. 그럼 임의의 $u:M \rightarrow M$에 대하여, 위의 논의에서 얻어지는 $\alpha\in A$를 $u$의 *행렬식<sub>determinant</sub>*이라 부르고 $\det u$로 적는다.

</div>

그럼 정의로부터 다음 명제가 자명하다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> 다음이 성립한다. 

1. 임의의 $u,v\in\End_\rMod{A}(M)$에 대하여, $\det(u\circ v)=(\det u)(\det v)$가 성립한다.
2. $\det(\id_M)=1$이다.
3. 임의의 $u\in\Aut_\rMod{A}(M)$에 대하여, $\det u$는 $A$에서 곱셈에 대한 역원이 존재하며 그 값은 $\det(u)^{-1}=\det(u^{-1})$과 같다.

</div>

<div class="proposition" markdown="1">

<ins id="cor3">**따름정리 3**</ins> 유한차원 free $A$-module $M$과 $u\in\End_\rMod{A}(M)$에 대하여 다음이 동치이다.

1. $u$가 bijective이다.
2. $\det u$가 $A$에서 가역이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

2번 조건을 가정하고 1번 조건을 보이면 충분하다. 이를 위해서는 $x_i=u(e_i)$로 정의하여

$$x_1\wedge \cdots\wedge x_n=\det(u) e_1\wedge\cdots\wedge e_n$$

를 얻은 후, 양 변에 $\det(u)^{-1}$을 곱한 후 그 식으로부터 얻어지는 기저변환을 생각하면 된다.

</details>

Free $A$-module $M$과 그 basis $e_1,\ldots, e_n$을 고정하면, 임의의 $M$의 원소들 $x_1,\ldots, x_n$에 대하여

$$x_1\wedge \cdots\wedge x_n=\alpha e_1\wedge\cdots\wedge e_n$$

이도록 하는 $\alpha$가 존재하며, 이를 $\det(x_1,\ldots, x_n)$과 같이 적는다. 이 값을 실제로 계산하기 위해서는 $x_i$들 각각을 $e_1,\ldots, e_n$에 대한 linear combination으로 나타낸 후 $e_i\wedge e_i=0$과 $e_i\wedge e_j=-e_j\wedge e_i$를 이용하여 이를 모두 정리해주면 된다. $A=\mathbb{k}$인 경우 이는 이미 [\[기초 선형대수학\] §행렬식의 존재성과 유일성, 식 (2)](/ko/math/basic_linear_algebra/existence_and_uniqueness_of_determinant#lem2)에서 살펴본 것이다. 조금 더 자세히 설명하자면, 임의의 $X\in\Mat_n(A)$를 열벡터들을 이용해 $X=(x_1,\ldots, x_n)$으로 적을 경우, $u(e_i)=x_i$를 만족하는 유일한 $u\in\End_\rMod{A}(M)$에 대하여 $\det(u)$가 잘 정의되며, 이는 [따름정리 3](#cor3)의 증명에서 나온 식과 비교해보면 $\det (x_1,\ldots, x_n)=\det(u)$이다. 그럼 이로부터 [명제 2](#prop2)의 행렬 버전의 명제를 만들 수 있으며, 이를 계산하는 과정이 곧 [\[기초 선형대수학\] §행렬식의 존재성과 유일성, 식 (2)](/ko/math/basic_linear_algebra/existence_and_uniqueness_of_determinant#lem2)이 된다. 특히 이로부터 $\det(u^\ast)=\det(u)$인 것을 알 수 있다.

## 행렬의 소행렬식

한편 행렬식을 계산하는 방법 중, 라플라스 전개를 이용하는 [\[기초 선형대수학\] §행렬식의 존재성과 유일성, ⁋정리 13](/ko/math/basic_linear_algebra/existence_and_uniqueness_of_determinant#thm13)이 있었는데, 이 계산 자체는 이미 다루었으므로 반복하지 않지만, 여기에서 등장했던 $\det A^{(i,j)}$들을 일반화할 수 있다.

이를 위해 임의의 $X=(\xi_{ij})\in\Mat_{I\times J}$가 주어졌다 하자. $I$와 $J$ 위에 정의된 total ordering를 하나 고정하면, 임의의 유한한 부분집합 $H\subseteq I$, $K\subseteq J$가 주어질 때마다 이들로 만들어진 부분행렬 $X_{H,K}=(\xi_{i,j})_{i\in H,j\in K}$의 index에도 total order가 주어진다. 특히 만일 $\lvert H\rvert=\lvert K\rvert$인 경우를 생각하자. 그럼 다음의 보조정리는 자명하다.

<div class="proposition" markdown="1">

<ins id="lem4">**보조정리 4**</ins> Free $A$-module $M$의 basis $(e\_i)\_{i\in I}$가 주어졌다 하고, $I$의 total ordering을 하나 고정하자. 또, 임의의 자연수 $p$에 대하여, $\bigwedge^p(M)$의 basis

$$(e_J=e_{j_1}\wedge\cdots\wedge e_{j_p})_{\lvert J\rvert=p}$$

를 생각하자. $M$의 임의의 $p$개의 원소 $x_1,\ldots, x_p$가 주어졌다 하고, 이들을

$$x_j=\sum_{i\in I} \xi_{ij}e_i$$

의 꼴로 쓴 후 행렬 $X=(\xi\_{ij})\_{(i,j)\in I\times p}\in\Mat\_{I\times p}(A)$를 정의하자. 그럼 다음의 식

$$x_1\wedge x_2\wedge\cdots\wedge x_p=\sum_{\lvert J\rvert=p}\det X_{I,J}e_J$$

이 성립한다. 

</div>

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> 두 free $A$-moduile $M,N$과 이들의 유한한 basis $(e\_i)\_{1\leq i\leq m}$, $(f\_j)\_{1\leq j\leq n}$가 각각 주어졌다 하자. 이제 $\min(m,n)$보다 작은 자연수 $p$에 대하여, $\bigwedge^p(u):\bigwedge^p(M) \rightarrow\bigwedge^p(N)$을 basis $(e\_I)\_{\lvert I\rvert=p}$, $(f\_J)\_{\lvert J\rvert=p}$에 대하여 행렬로 표현한 것은 $(\det(X\_{J,I}))$로 주어진다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

주어진 상황에서 $I$의 원소들을 $i\_1<\cdots i\_p$로 크기 순으로 나열하자. 그럼 $\bigwedge^p(u)$의 정의에 의하여

$${\bigwedge}^p(u)=u(e_{i_1})\wedge\cdots\wedge u(e_{i_p})$$

이므로, 앞선 보조정리를 적용하면 된다.

</details>

<div class="proposition" markdown="1">

<ins id="cor6">**따름정리 6**</ins> Free $A$-module $M$이 유한한 basis $(e\_i)\_{1\leq i\leq n}$을 갖는다 하자. 그럼 임의의 $u\in\End_\rMod{A}(M)$과 $\alpha,\beta\in A$에 대하여 다음 식

$$\det(\alpha\cdot\id_M+\beta u)=\sum_{k\geq 0}\tr\left({\bigwedge}^k(u)\right)\alpha^{n-k}\beta^k$$

를 얻는다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

좌변은 다음의 wedge

$$(\alpha e_1+\beta u(e_1))\wedge\cdots\wedge(\alpha e_n+\beta u(e_n))$$

를 $e_1\wedge\cdots\wedge e_n$의 배수로 되돌려 놓으며 생긴다. 위의 식을 전부 전개하면, 이는 $0\leq p\leq n$을 만족하는 정수 $p$, $\lvert P\rvert=p$를 만족하는 $\\{1,\ldots, n\\}$의 부분집합 $P$, 그리고 다음의 식

$$x_i=\begin{cases}u(e_i)&\text{if $i\in P$}\\e_i&\text{otherwise}\end{cases}$$

으로 정의된 $x_i$들로 정의한 $\bigwedge^n(M)$의 원소 $x_P=x_1\wedge\cdots\wedge x_n$에 대하여 $\alpha^{n-p}\beta^p x_P$들을 다 더한 것과 같다. 

위의 꼴의 $x_P$를 단순화하기 위해, $\\{1,\ldots, n\\}\setminus P=Q$라 하고, $P,Q$의 원소들을 각각 크기별로 배열하여

$$P=\{i_1< i_2<\cdots< i_p\},\qquad Q=\{j_1< j_2<\cdots < j_{n-p}\}$$

라 하자. 그럼 $P$의 원소들과 $Q$의 원소들의 순서를 각각 바꾸어

$$x_P=\gamma_{P,Q}e_{j_1}\wedge\cdots\wedge e_{j_{n-p}}\wedge u(e_{i_1})\wedge\cdots u(e_{i_{n-p}})$$

로 쓸 수 있다. 여기서 $\gamma_{P,Q}$는 이들의 순서를 바꾸며 생기는 부호이며, 구체적으로는 다음 식

$$\gamma_{P,Q}=(-1)^{\lvert A\rvert},\qquad A=\{(p,q)\in P\times Q: p>q\}$$

으로 주어진다. 그럼 $X$의 정의와 [보조정리 4](#lem4)에 의해 

$$u(e_{i_1})\wedge\cdots\wedge u(e_{i_p})=\sum_{\lvert I\rvert=p}\det(X_{I,Q})e_Q$$

이므로, 이를 대입하면

$$x_P=\gamma_{P,Q}\sum_{\lvert I\rvert=p}\det X_{I,P} e_Q\wedge e_I$$

를 얻는다. 그런데 $\lvert I\rvert=p$이고 $\lvert Q\rvert=n-p$이므로, 이들은 $I=P$가 아닌 이상 항상 겹치는 $e_i$를 갖고 따라서 위의 식은

$$x_P=\det (X_{P,P} )e_1\wedge e_2\wedge\cdots\wedge e_n$$

으로 쓸 수 있다. [명제 5](#prop5)에 의하여, 고정된 $p$에 대해 $\lvert P\rvert=p$를 만족하는 모든 $p$에 대해 $\det(X_{p,p})$를 모두 더한 것이 $\tr\left(\bigwedge^k(u)\right)$이므로 이로써 증명이 완료된다. 

</details>

특히 $\alpha=\beta=1$로 두면 $\tr(\bigwedge(u))=\det(\id_M+u)$를 얻는다. 

## 특성다항식

이제 우리는 특성다항식을 정의한다. 

Polynomial algebra $A[\x]$와 canonical inclusion $\iota: A \hookrightarrow A[\x]$를 생각하면, extension of scalar를 통해 $\iota_!M=A[\x]\otimes_A M$ 위에 $A[\x]$-module의 구조가 정의된다. ([\[대수적 구조\] §스칼라의 변환, ⁋정의 3](/ko/math/algebraic_structures/change_of_base_ring#def3)) 뿐만 아니라, 임의의 $u\in\End_\rMod{A}(M)$이 주어질 때마다 $\iota_!u\in\End_\rMod{A[\x]}(\iota_!M)$ 또한 정의된다.

임의의 $u\in\End_\rMod{A}(M)$에 대하여, 다음 표기법

$$u^k=\underbrace{u\circ\cdots\circ u}_\text{$k$ times}$$

을 도입하자. 그럼 임의의 $p\in A[\x]$에 대해서 $p(u)$를 $\End_\rMod{A}(M)$의 원소로 생각할 수 있으며, 이 경우 임의의 $p,q\in A[\x]$에 대하여

$$(pq)(u)=p(u)\circ q(u)=q(u)\circ p(u)$$

가 성립한다. 따라서, $M$ 위에 $A[\x]$-action을 다음 식

$$p\bullet x=p(u)(x)$$

으로 정의하면 이는 $M$ 위에 $A[\x]$-module 구조를 준다. 즉, 방금 정의한 스칼라곱에 의하여

$$\rho: A[\x]\otimes_A M \rightarrow M;\qquad p\otimes_A x\mapsto p\bullet x\tag{1}$$

이 정의되며, 이는 $A$-linear이다. 뿐만 아니라 $\rho$는 $A[\x]$-linear map이다. 임의의 $p\in A[\x]$와 $q\otimes x\in \iota_!M$에 대하여,

$$\rho(p(q\otimes_Ax))=\rho((pq)\otimes_Ax)=(pq)\bullet x=(pq)(u)(x)=p(u)(q(u)x)=p\bullet\rho(q\otimes_Ax)$$

이기 때문이다. 

혼동을 피하기 위해, $M$을 $A[\x]$-module로 취급한 것을 $M_u$라 적자. 이제 $u$를 $M_u$에서 $M_u$로의 함수로 보면 다음의 식

$$u(p\bullet x)=u(p(u)(x))=(\x p)\bullet x=(p\x)\bullet x=p\bullet(u(x))$$

이 성립하므로 $u$는 $A[\x]$-module endomorphism이 된다. 그럼 위의 식과 (1)로부터 다음의 식

$$\rho\circ(\iota_!u)=u\circ\rho$$

이 성립하는 것을 안다.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> 위와 같은 상황에서, $A[\x]$-endomorphism $\psi=\x-\iota_!u$를 다음 식

$$\psi(p\otimes_Ax)=(\x p)\otimes_Ax -p\otimes_A u(x)$$

으로 정의하자. 그럼 다음의 $A[\x]$-module들의 exact sequence

$$\iota_!M\overset{\psi}{\longrightarrow}\iota_!M\overset{\rho}{\longrightarrow}M_u\longrightarrow 0$$

이 exact이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$\ker\rho\subseteq \im\psi$인 것만 보이면 충분하다. $z\in\ker\rho$가 임의로 주어졌다 하자. 그럼 $z$를 $p\otimes_A x$의 꼴의 원소들의 합으로 분해한 후, 다시 $p$들을 $1,\x,\x^2,\ldots$들의 일차결합으로 생각하여 분해한 후 $\x^k$들에 맞추어 합을 다시 쓰는 방식으로 

$$z=\sum_k \x^k\otimes_A x_k,\qquad x_k\in M$$

으로 적어줄 수 있다. 그럼 $z\in\ker\rho$라는 조건으로부터,

$$\rho(z)=\sum_k u^k(\x_k)=0$$

을 얻는다. 이제 $\sum 1\otimes u^k(x_k)=0$이므로, 이로부터

$$z=\sum_k (\x^k\otimes_A x_k-1\otimes_A u^k(x_k))=\sum_k (\x^k-\iota_!u^k))(1\otimes x_k)$$

인데, 어차피 $\iota_!M=A[\x]\otimes_A M$에서 $\x$는 $A[\x]$ 부분에 작용하고, $\iota_!u$는 $M$에 작용하므로 이들의 곱셈은 순서를 바꿀 수 있다. 즉 위의 식을

$$\sum_k (\x-\iota_!u)\circ\left(\sum_{j=0}^{k-1} \x^j (\iota_!u)^{k-j-1}\right)$$

으로 쓸 수 있으므로 증명이 완료된다. 

</details>

한편, $\psi$의 행렬식을 생각하면 [따름정리 6](#cor6)으로부터 

$$\det (\x-\iota_!u)=\sum_{k=0}^n (-1)^k\tr\left({\bigwedge}^j(\iota_!u)\right)\x^{n-k}$$

을 얻는다. 한편 $u$의 행렬표현 $[u]\_\mathcal{B}^\mathcal{B}$는, $M[\x]$의 $A[\x]$-basis $\mathcal{B}'=(1\otimes e_i)\_{1\leq i\leq n}$에 대한 $\iota\_!u$의 행렬표현 $[\iota\_!u]\_{\mathcal{B}'}^{\mathcal{B}''}$와 같으므로 위의 식은

$$\det (\x-\iota_!u)=\sum_{k=0}^n (-1)^k\tr\left({\bigwedge}^j(u)\right)\x^{n-k}$$

으로 쓸 수 있다. 

<div class="definition" markdown="1">

<ins id="def8">**정의 8**</ins> 위에서 정의한 다항식 $\det(\x-\iota_!u)$를 $u$의 *characteristic polynomial<sub>특성다항식</sub>*이라 부르고 $\chi_u(\x)$로 적는다. 

</div>

그럼 앞선 식으로부터, characteristic polynomial에서 $\x^n$의 계수는 $1$, $\x^{n-1}$의 계수는 $-\tr(u)$이며 상수항은 $(-1)^n\det(u)$임을 알 수 있다. 

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9 (Cayley-Hamilton)**</ins> $\chi_u(u)=0$.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

보여야 할 것은 임의의 $x\in M$에 대하여 $\chi_u(u)(x)=0$인 것을 보여야 한다. 그런데 $\chi_u(u)(x)$는, 식 (1)을 사용하면, $\rho(\chi_u(\x)\otimes_Ax)$와 같다. 이제

$$\chi_u(\x)\otimes_Ax=\chi_u(\x)(1\otimes_Ax)=\det(\x-\iota_!u)(1\otimes_Ax)$$

이다. 그런데 라플라스 전개를 생각하면 임의의 행렬 $X$와 $X$의 cofactor $Y$에 대해 $XY^t=(\det X)I$가 성립하므로, 적당한 $v\in\End_\rMod{A[\x]}(\iota_!M)$이 존재하여 

$$\det(\x-\iota_!u)(1\otimes_Ax)=(\x-\iota_!u)(v(1\otimes_A x)$$

으로 쓸 수 있고 따라서 [명제 7](#prop7)에 의해 원하는 결과를 얻는다.w

</details>