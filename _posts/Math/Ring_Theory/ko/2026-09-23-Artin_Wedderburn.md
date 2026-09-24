---
title: "아틴-웨더번 정리"
description: "자기 자신 위의 module로서 semisimple인 환을 semisimple ring으로 정의하고, 이것이 모든 module이 semisimple인 것과 동치임을 보인다. Division ring 위의 행렬환의 module 구조와 opposite ring·endomorphism ring 계산을 거쳐, semisimple ring이 division ring 위의 행렬환 유한개의 곱으로 유일하게 분해된다는 아틴-웨더번 정리를 증명한다."
excerpt: "Semisimple ring의 구조 정리: division ring 위 행렬환들의 곱으로의 유일한 분해"

categories: [Math / Ring Theory]
permalink: /ko/math/ring_theory/artin_wedderburn
sidebar: 
    nav: "ring_theory-ko"

date: 2026-09-23

weight: 8

---

[§반단순가군](/ko/math/ring_theory/semisimple_modules){: data-lid="bkiu1" }에서 우리는 simple module들의 direct sum으로 분해되는 module을 다루었다. 가장 흥미로운 응용 중 하나는 ring $A$를 자기자신 위의 module로 보았을 때 semisimple module이 되는 *semisimple ring*으로, 이러한 ring은 matrix ring들 유한개의 곱으로 분해된다는 것이 이번 글의 핵심적인 결과이다. 

이 글에서도 ring은 항등원을 갖는 ring이며 별도의 commutativity는 가정하지 않는다. 또, $A$-module은 언제나 left $A$-module을 의미하는 것으로 이해한다.

## 반단순환

::: 정의 1
Ring $A$가 자기 자신 위의 left $A$-module로서 semisimple이라면, $A$를 *semisimple ring<sub>반단순환</sub>*이라 부른다.
:::

Left $A$-module $A$의 submodule은 정확히 $A$의 left ideal이므로, 이 정의는 [§반단순가군, ⁋정의 2](/ko/math/ring_theory/semisimple_modules#def2){: data-lid="apyw2" }를 $M=A$에 적용한 것에 불과하다. 한편 다음이 성립한다. 

::: 명제 2
Ring $A$에 대하여, $A$가 semisimple ring인 것은 모든 left $A$-module이 semisimple인 것과 동치이다.
:::
::: 증명
모든 left $A$-module이 semisimple이라면 특히 left $A$-module $A$가 semisimple이다. 따라서 반대방향만 보이면 충분하다. $A$가 semisimple ring이라 하면, 임의의 left $A$-module $M$은 어떤 free module $A^{(I)}$의 quotient이고 ([\[다중선형대수학\] §기저, ⁋명제 2](/ko/math/multilinear_algebra/basis_of_free_modules#prop2){: data-lid="451t5" }), $A$가 semisimple이므로 [§반단순가군, ⁋정리 5](/ko/math/ring_theory/semisimple_modules#thm5){: data-lid="sgjq3" }에 의해 $A^{(I)}$ 또한 semisimple $A$-module이 되어 그 quotient 또한 semisimple이다. ([§반단순가군, ⁋따름정리 6](/ko/math/ring_theory/semisimple_modules#cor6){: data-lid="cx5wl" })
:::

또, 다음이 성립한다. 

::: 명제 3
$A$가 semisimple ring이면 $A$는 유한개의 simple left ideal의 direct sum이다.
:::
::: 증명
$A=\bigoplus_{i\in I}\mathfrak{a}_i$를 simple left ideal들의 direct sum이라 하자. 항등원 $1$을 이 direct sum decomposition의 원소로 보면, 항등원은 <em-ko>유한한</em-ko> index set $J\subseteq I$에서만 $0$이 아닐 수 있다. 이제 임의의 $a\in A$에 대하여 $a=a\cdot 1\in\sum_{i\in J}\mathfrak{a}_i$이므로 $A=\bigoplus_{i\in J}\mathfrak{a}_i$이다.
:::

## 나눗셈환 위의 행렬환

우선 우리는 다음을 정의한다. 

::: 정의 4
Ring $A$에 대하여, $A$와 같은 abelian group 위에 곱셈을 $a\ast^\op b=ba$로 정의한 ring을 $A$의 *opposite ring<sub>반대환</sub>*이라 부르고 $A^\op$로 적는다.
:::

정의에서 바로 $(A^\op)^\op=A$이고, right $A$-module은 left $A^\op$-module과 같은 것이다. 또 $D$가 division ring이면 임의의 nonzero element의 역원이 $D^\op$에서도 그대로 역원의 역할을 하므로 $D^\op$ 또한 division ring이다.

::: 명제 5
$D$가 division ring이고 $n\geq 1$이라 하자. 열벡터들의 공간 $D^n$위에 행렬 곱셈으로 left $\Mat_n(D)$-module 구조를 부여하면 다음이 성립한다.

1. $D^n$은 simple $\Mat_n(D)$-module이다.
2. $k$번째 열 밖에서 $0$인 행렬들의 left ideal
    
    $$C_k=\left\{\begin{pmatrix}0&\cdots&a_{1k}&\cdots&0\\\vdots&\ddots&\vdots&\ddots&\vdots\\0&\cdots&a_{nk}&\cdots&0\end{pmatrix}\middle\vert a_{1k},\ldots,a_{nk}\in D\right\}$$
    
    에 대하여, direct sum decomposition $\Mat_n(D)=\bigoplus_{k=1}^nC_k$가 존재하며, 이 때 각 $C_k$는 $\Mat_n(D)$-module로서 $D^n$과 isomorphic하다. 특히 $\Mat_n(D)$는 semisimple ring이다.
:::
::: 증명
우선 둘째 결과의 경우, 행렬을 열별로 나누면 $\Mat_n(D)=\bigoplus_kC_k$이고, $C_k$는 left ideal인 것은 단순계산으로 확인할 수 있으며 $C_k\rightarrow D^n$은 module isomorphism인 것도 자명하다.

이제 첫째 결과를 보이자. $0\neq v\in D^n$과 임의의 $w\in D^n$을 택하자. $v_k\neq 0$인 성분 $k$를 고르고, 행렬 $A$를 $A_{ik}=w_iv_k^{-1}$, 나머지 성분은 $0$으로 정의하면

$$(Av)_i=A_{ik}v_k=w_iv_k^{-1}v_k=w_i$$

이므로 $Av=w$이다. 즉 $0$이 아닌 임의의 원소가 $D^n$ 전체를 생성하므로 $D^n$은 simple이다. 이제 둘째 결과로부터 $\Mat_n(D)$는 simple module들의 direct sum이므로 $\Mat_n(D)$는 semisimple ring이다.
:::

뿐만 아니라 다음이 성립한다.

::: 명제 6
[명제 5](#prop5){: data-lid="dx93u" }의 상황에서 $\End_{\Mat_n(D)}(D^n)\cong D^\op$이다.
:::
::: 증명
임의의 $d\in D$에 대하여, 열벡터의 각 성분에 오른쪽에서 $d$를 곱해주는 함수 $\rho_d(v)=vd$를 생각하면, 임의의 행렬 $A$에 대하여 

$$(A(vd))_i=\sum_jA_{ij}(v_jd)=(Av)_id$$

이므로 $\rho_d$는 module endomorphism이다. 뿐만 아니라 식 

$$\rho_d\circ\rho_{d'}(v)=vd'd=\rho_{d'd}(v)$$

으로부터 $d\mapsto\rho_d$는 ring homomorphism $D^\op\rightarrow\End_{\Mat_n(D)}(D^n)$을 정의하며, $\rho_d$가 첫째 표준 열벡터 $e_1$을 $e_1d$로 보내므로 이는 단사함수임이 자명하다. 

남은 것은 이것이 전사임을 보이는 것이다. $\varphi$를 임의의 endomorphism이라 하고 $E_{ij}$를 matrix unit이라 하면, $E_{11}e_1=e_1$이므로 

$$E_{11}\varphi(e_1)=\varphi(E_{11}e_1)=\varphi(e_1)$$

이고, 이 때 좌변은 $\varphi(e_1)$의 첫 성분만 남긴 벡터이므로 $\varphi(e_1)=e_1d$인 $d\in D$가 존재한다. 이제 임의의 $v\in D^n$에 대하여, $(i,1)$ 성분이 $v_i$이고 나머지가 $0$인 행렬을 $A_i$라 하면 $v=\sum_iA_ie_1$이므로

$$\varphi(v)=\sum_iA_i\varphi(e_1)=\sum_iA_i(e_1d)=vd=\rho_d(v)$$

이다. 따라서 $\varphi=\rho_d$이고 대응은 전사이다.
:::

앞서 언급했듯, 우리 글의 목적은 임의의 semisimple ring이 matrix ring들 유한개의 곱으로 분해된다는 것이며, 위의 두 명제가 이를 위한 matrix ring들의 기본 성질들을 준다. 이제 우리는 ring과 그 endomorphism에 대한 성질을 살펴보아야 한다.

::: 보조정리 7
임의의 ring $A$에 대하여 $\End_A(A)\cong A^\op$이다.
:::
::: 증명
$\Phi:\End_A(A)\rightarrow A^\op$를 $\Phi(f)=f(1)$로 정의하면 이것이 $A^\op$로의 ring homomorphism인 것은 쉽게 보일 수 있다. 거꾸로, 임의의 $a\in A$에 대해 오른쪽 곱셈 $x\mapsto xa$는 left module endomorphism이고 이 대응이 $\Phi$의 역을 주므로 $\Phi$는 isomorphism이다.
:::

그럼 우리의 다음 관찰은 semisimple module 위의 linear operator에 대한 것으로, 직관적으로 이는 semisimple module들을 이루는 각 simple module들이 (같은 type이 아닌 한) 섞일 수 없다는 것이며, 이에 대한 증명은 당연히 [§나눗셈환, ⁋보조정리 10](/ko/math/ring_theory/division_rings#lem10){: data-lid="rdgn9" }을 사용한다.

::: 보조정리 8
$S_1,\ldots,S_k$가 서로 isomorphic하지 않은 simple module들이고 $n_1,\ldots,n_k\geq 1$일 때, $M=\bigoplus_{i=1}^kS_i^{n_i}$에 대하여

$$\End_A(M)\cong\prod_{i=1}^k\Mat_{n_i}\big(\End_A(S_i)\big)$$

이다.
:::
::: 증명
Direct sum 인자들에 대한 inclusion과 projection을 각각 $\iota_{i,a}$, $\pi_{i,a}$로 적자. Endomorphism $\varphi$의 성분 $\pi_{i,a}\circ\varphi\circ\iota_{j,b}$는 $S_j$에서 $S_i$로 가는 homomorphism인데, $i\neq j$이면 [§나눗셈환, ⁋보조정리 10](/ko/math/ring_theory/division_rings#lem10){: data-lid="wccwq" }에 의해 $0$이 되어야 한다. 따라서 $\varphi$는 각 $i$마다 행렬 $\varphi^{(i)}=(\pi_{i,a}\circ\varphi\circ\iota_{i,b})_{a,b}\in\Mat_{n_i}(\End_A(S_i))$들의 자료와 정확히 같다.

이 대응이 ring isomorphism임을 확인해야 한다. 즉, 이것이 덧셈과 곱셈을 보존함을 보여야 한다. 덧셈 부분은 자명하며, 곱셈에 대해서는 $\sum_{j,b}\iota_{j,b}\circ\pi_{j,b}=\id_M$이므로

$$\pi_{i,a}\circ(\varphi\circ\psi)\circ\iota_{i,c}=\sum_{b}(\pi_{i,a}\circ\varphi\circ\iota_{i,b})\circ(\pi_{i,b}\circ\psi\circ\iota_{i,c})$$

이고, 이는 정확히 행렬곱의 $(a,c)$ 성분이다. 
:::

또, 다음이 성립한다.

::: 보조정리 9
임의의 ring $A$에 대하여 transpose는 isomorphism $\Mat_n(A)^\op\cong\Mat_n(A^\op)$을 준다.
:::
::: 증명
$T(X)=X^t$는 additive bijection이고 항등행렬을 보존한다. $\Mat_n(A)^\op$의 곱 $X\ast^\op Y=YX$에 대하여

$$T(X\ast^\op Y)_{ij}=(YX)_{ji}=\sum_k Y_{jk}X_{ki}$$

이고, $\Mat_n(A^\op)$에서의 곱은

$$\big(T(X)T(Y)\big)_{ij}=\sum_k(X^t)_{ik}\ast^\op(Y^t)_{kj}=\sum_k(Y^t)_{kj}(X^t)_{ik}=\sum_k Y_{jk}X_{ki}$$

로 일치한다.
:::

마지막 준비물은 곱환의 module 이론이다.

::: 명제 10
$A=A_1\times\cdots\times A_k$라 하고, $e_i\in A$를 $i$번째 성분만 $1$인 원소라 하자.

1. $\{e_1,\ldots,e_k\}$가 complete set of central orthogonal idempotents이고, 임의의 left $A$-module $M$은 $M=\bigoplus_ie_iM$으로 분해된다. 각 $e_iM$은 $A$가 $i$번째 성분을 통해 작용하는 $A_i$-module이며, 그 $A$-submodule은 $A_i$-submodule과 일치한다. 특히 simple left $A$-module은 정확히, 어떤 $i$에 대한 simple left $A_i$-module을 $i$번째 성분의 작용으로 $A$-module로 본 것들이다.
2. 각 $A_i$가 semisimple ring이면 $A$도 semisimple ring이다.
:::
::: 증명
1. $e_i$들이 complete set of central orthogonal idempotents임은 성분별 계산으로 바로 확인할 수 있다. ([§멱등원과 곱분해, ⁋정리 5](/ko/math/ring_theory/idempotents#thm5){: data-lid="e0b4o" }) 이 때, 식
    
    $$1=\sum e_i,\qquad e_ie_j=\delta_{ij}e_i$$
    
    로부터 $M=\bigoplus_i e_iM$임을 알고, centrality에 의해 $e_iM$에는 $i$번째 성분 $A_i$만 작용하고 나머지 성분은 $0$으로 작용하므로 $e_iM$의 $A$-submodule과 $A_i$-submodule은 서로 같은 것이다. 특히 $M\neq 0$이 simple이면 이 분해의 인자 중 정확히 하나만 nonzero이므로, $M$이 simple left $A$-module이라는 것은 $M$이 어떤 $i$에 대해 simple $A_i$-module이라는 것과 같다.

2. 각 $A_i$가 semisimple ring이면 $A_i$는 simple left ideal들의 direct sum이므로, $A\cong\bigoplus_i A_i$ 또한 simple left ideal들의 direct sum이 되어 semisimple ring이다.
:::

## 아틴-웨더번 정리

이제 모든 재료가 준비되었다.

::: 정리 11 (Artin-Wedderburn)
Ring $A$에 대하여 다음이 동치이다.

1. $A$는 semisimple ring이다.
2. 적당한 division ring들 $D_1,\ldots,D_k$와 자연수 $n_1,\ldots,n_k$에 대하여
    
    $$A\cong\Mat_{n_1}(D_1)\times\cdots\times\Mat_{n_k}(D_k)$$
    
    이다.

뿐만 아니라, 이렇게 얻어지는 semisimple ring의 decomposition을 구성하는 데이터 $k$와 $(n_i,D_i)$들은 순서와 isomorphism을 무시하면 유일하다.
:::
::: 증명
둘째 조건이 첫째 조건을 함의하는 것은 [명제 5](#prop5){: data-lid="aw3ne" }에 의해 각 인자가 semisimple ring이므로 [명제 10](#prop10){: data-lid="l9ws8" }의 둘째 결과에서 바로 얻어진다.

이제 첫째 조건을 가정하고 둘째 조건을 보이자. 우선 [명제 3](#prop3){: data-lid="jyozf" }에 의해 $A$는 유한개의 simple left ideal의 direct sum이고, isomorphism class별로 인자들을 모으면 서로 isomorphic하지 않은 simple module들 $S_1,\ldots,S_k$와 자연수 $n_i\geq 1$에 대하여 left module로서 $A\cong\bigoplus_iS_i^{n_i}$이다. $C_i=\End_A(S_i)$로 두면 이는 [§나눗셈환, ⁋보조정리 10](/ko/math/ring_theory/division_rings#lem10){: data-lid="uauah" }에 의해 division ring이고, [보조정리 7](#lem7){: data-lid="reb59" }과 [보조정리 8](#lem8){: data-lid="m01xr" }에 의해

$$A^\op\cong\End_A(A)\cong\prod_{i=1}^k\Mat_{n_i}(C_i)$$

이다. 양변에 $(-)^\op$을 취하면, [보조정리 9](#lem9){: data-lid="2hk1d" }에 의해

$$A\cong\prod_{i=1}^k\Mat_{n_i}(C_i)^\op\cong\prod_{i=1}^k\Mat_{n_i}(C_i^\op)$$

이고, $D_i=C_i^\op$는 division ring이므로 원하는 decomposition을 얻는다.

이제 이러한 성질을 만족하는 decomposition $A\cong\prod_{j=1}^l\Mat_{m_j}(E_j)$가 임의로 주어졌다 하고 유일성을 보이자. 이는 본질적으로 위의 구성을 거꾸로 따라가는 것으로, 우선 우리는 $W_j=E_j^{m_j}$를, $A$가 $j$번째 성분 $\Mat_{m_j}(E_j)$를 통해 행렬곱으로 작용하고 나머지 성분은 $0$으로 작용하는 left $A$-module 구조가 주어진 것으로 볼 수 있다. 그럼 [명제 5](#prop5){: data-lid="qlrxy" }에 의해 각 $W_j$는 simple이고 $j$번째 인자가 $W_j^{m_j}$와 isomorphic하므로, left module로서 $A\cong\bigoplus_jW_j^{m_j}$이며, [명제 10](#prop10){: data-lid="yl0q8" }의 첫째 결과에 의해 $W_j$들은 서로 다른 성분에 속하므로 pairwise non-isomorphic하다. 그럼 [§반단순가군, ⁋명제 10](/ko/math/ring_theory/semisimple_modules#prop10){: data-lid="wprdz" }에 의해 두 decomposition $\bigoplus_iS_i^{n_i}\cong\bigoplus_jW_j^{m_j}$이 같은 데이터를 주는 것을 확인할 수 있으며, 마지막으로 [명제 10](#prop10){: data-lid="c9hgr" }의 첫째 결과에 의해 $\End_A(W_i)=\End_{\Mat_{m_i}(E_i)}(E_i^{m_i})$이고 [명제 6](#prop6){: data-lid="wlly1" }에 의해 이는 $E_i^\op$와 isomorphic하므로

$$E_i\cong\End_A(W_i)^\op\cong\End_A(S_i)^\op=C_i^\op=D_i$$

이다. 
:::

직관적으로 이 정리는 semisimple ring의 action이 서로 섞이지 않는 블록들로 나뉘고, 각 블록 위에서는 division ring 위의 matrix ring처럼 작용한다는, 일종의 block diagonalization을 하는 것으로 이해할 수 있다. 그럼 semisimple ring $A$ 위의 module theory는 특히 단순하다. 

::: 따름정리 12
$A\cong\prod_{i=1}^k\Mat_{n_i}(D_i)$가 semisimple ring이라 하자. 그럼 simple left $A$-module은 isomorphism을 무시하면 정확히 $V_i=D_i^{n_i}$들로만 이루어지고, 임의의 left $A$-module은 이들과 isomorphic한 summand들로 이루어진 direct sum이다.
:::
::: 증명
[명제 2](#prop2){: data-lid="c2mpv" }에 의해 모든 $A$-module이 semisimple이므로, 이를 simple $A$-module들의 direct sum으로 나타낼 수 있고, [명제 5](#prop5){: data-lid="pg0b4" }와 [명제 10](#prop10){: data-lid="zkbod" }에 의해 각 $V_i$는 simple이다. 

거꾸로 임의의 simple $A$-module $M$이 주어졌다 하면, $0\neq x\in M$에 대해 $M=Ax$이므로 surjection $A\rightarrow M$이 존재하고, [명제 5](#prop5){: data-lid="npt9u" }의 둘째 결과로 얻어지는 left module decomposition $A\cong\bigoplus_iV_i^{n_i}$을 생각하면 $A$의 어떤 summand $V_i$ 위에서 이 전사가 nonzero가 된다. 그럼 simple module 사이의 nonzero homomorphism $V_i\rightarrow M$이 존재하므로 [§나눗셈환, ⁋보조정리 10](/ko/math/ring_theory/division_rings#lem10){: data-lid="aib2j" }에 의해 $M\cong V_i$이다.
:::

한편 [정의 1](#def1){: data-lid="dw004" }은 left module 구조로 주어졌지만, right module로 정의하더라도 같은 ring들을 얻는다. Right $A$-module은 left $A^\op$-module과 같으므로, $A$가 right semisimple이라는 것은 $A^\op$가 semisimple ring이라는 것이다. 그런데 $A$가 semisimple ring이면 [정리 11](#thm11){: data-lid="gy0gw" }의 분해에 [보조정리 9](#lem9){: data-lid="t2e0p" }를 적용하여 $A^\op\cong\prod_i\Mat_{n_i}(D_i^\op)$ 또한 행렬환들의 곱이 되므로 semisimple ring이고, 역도 마찬가지로 성립한다. 따라서 semisimple ring의 개념은 좌우의 선택과 무관하다.

---

**참고문헌**

**[DF]** D. S. Dummit and R. M. Foote, *Abstract algebra*, 3rd ed., Wiley, 2004.  
**[Rot]** J. J. Rotman, *An introduction to homological algebra*, 2nd ed., Universitext, Springer, 2009.
