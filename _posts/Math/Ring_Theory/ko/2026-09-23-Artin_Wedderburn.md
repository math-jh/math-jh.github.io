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

published: false

---

[§반단순가군](/ko/math/ring_theory/semisimple_modules){: data-lid="bkiu1" data-relation="required" }에서 우리는 simple module들의 직합으로 분해되는 module을 다루었다. 가장 흥미로운 응용 중 하나는 ring $A$를 자기자신 위의 module로 보았을 때 semisimple module이 되는 *semisimple ring*으로, 이러한 ring은 matrix ring들 유한개의 곱으로 분해된다는 것이 이번 글의 핵심적인 결과이다. 

이 글에서도 ring은 항등원을 갖는, ring이며 별도의 commutativity는 가정하지 않는다. 또, $A$-module은 언제나 left $A$-module을 의미하는 것으로 이해한다.

## 반단순환

::: 정의 1
Ring $A$가 자기 자신 위의 left $A$-module로서 semisimple이라면, $A$를 *semisimple ring<sub>반단순환</sub>*이라 부른다.
:::

Left $A$-module $A$의 submodule은 정확히 $A$의 left ideal이므로, 이 정의는 [§반단순가군, ⁋정의 2](/ko/math/ring_theory/semisimple_modules#def2){: data-lid="apyw2" data-relation="weak" }를 $M=A$에 적용한 것에 불과하다. 한편 다음이 성립한다. 

::: 명제 2
Ring $A$에 대하여, $A$가 semisimple ring인 것은 모든 left $A$-module이 semisimple인 것과 동치이다.
:::
::: 증명
모든 left $A$-module이 semisimple이라면 특히 left $A$-module $A$가 semisimple이다. 거꾸로 $A$가 semisimple ring이라 하자. 임의의 index 집합 $I$에 대하여 free module $A^{(I)}$는 $A$의 복사본들의 직합이고, 각 복사본이 simple submodule들의 합이므로 $A^{(I)}$ 또한 simple submodule들의 합이다. 따라서 [§반단순가군, ⁋정리 5](/ko/math/ring_theory/semisimple_modules#thm5){: data-lid="sgjq3" data-relation="required" }에 의해 $A^{(I)}$는 semisimple이다. 이제 임의의 left $A$-module $M$은 [\[다중선형대수학\] §기저, ⁋명제 2](/ko/math/multilinear_algebra/basis_of_free_modules#prop2){: data-relation="required" }에 의해 어떤 free module의 quotient이므로, [§반단순가군, ⁋따름정리 6](/ko/math/ring_theory/semisimple_modules#cor6){: data-lid="cx5wl" data-relation="required" }에 의해 semisimple이다.
:::

::: 명제 3
$A$가 semisimple ring이면 $A$는 유한개의 simple left ideal의 직합이다.
:::
::: 증명
$A=\bigoplus_{i\in I}L_i$를 simple left ideal들의 직합이라 하자. 항등원을 이 분해에 따라 $1=\sum_{i\in F}x_i$로 쓰면 $F$는 유한집합이다. 그럼 임의의 $a\in A$에 대하여 $a=a\cdot 1\in\sum_{i\in F}L_i$이므로 $A=\bigoplus_{i\in F}L_i$이다.
:::

따라서 semisimple ring은 left module로서 finite composition series를 갖는다 ([\[가환대수학\] §조르단-횔더 정리, ⁋정의 2](/ko/math/commutative_algebra/Jordan-Holder_theorem#def2){: data-lid="3l9ro" data-relation="weak" }). 직합 인자를 하나씩 쌓은 chain이 그것이며, 특히 semisimple ring은 left Artinian이자 left Noetherian이다.

## 나눗셈환 위의 행렬환

구조 정리의 building block은 division ring 위의 행렬환이다. 이를 다루기 위해 먼저 곱셈의 순서를 뒤집은 ring을 정의한다.

::: 정의 4
Ring $A$에 대하여, $A$와 같은 abelian group 위에 곱셈을 $a\ast b=ba$로 정의한 ring을 $A$의 *opposite ring<sub>반대환</sub>*이라 부르고 $A^{\mathrm{op}}$로 적는다.
:::

정의에서 바로 $(A^{\mathrm{op}})^{\mathrm{op}}=A$이고, right $A$-module은 left $A^{\mathrm{op}}$-module과 같은 것이다. 또 $D$가 division ring이면 nonzero 원소의 역원이 그대로 역원이 되므로 $D^{\mathrm{op}}$ 또한 division ring이다.

::: 명제 5
$D$가 division ring이고 $n\geq 1$이라 하자. 열벡터들의 공간 $D^n$을 행렬 곱셈으로 left $\Mat_n(D)$-module로 보면 다음이 성립한다.

1. $D^n$은 simple module이다.
2. $k$번째 열 밖에서 $0$인 행렬들의 left ideal을 $C_k$라 하면 $\Mat_n(D)=\bigoplus_{k=1}^nC_k$이고, 각 $C_k$는 module로서 $D^n$과 isomorphic하다. 특히 $\Mat_n(D)$는 semisimple ring이다.
:::
::: 증명
2를 먼저 보자. 행렬을 열별로 나누면 $\Mat_n(D)=\bigoplus_kC_k$이고, 왼쪽에서 행렬을 곱하는 연산은 각 열에 독립적으로 작용하므로 $C_k$는 left ideal이며, $k$번째 열을 읽는 대응 $C_k\rightarrow D^n$은 module isomorphism이다.

1을 보이기 위해 $0\neq v\in D^n$과 임의의 $w\in D^n$을 택하자. $v_k\neq 0$인 성분 $k$를 고르고, 행렬 $A$를 $A_{ik}=w_iv_k^{-1}$, 나머지 성분은 $0$으로 정의하면

$$(Av)_i=A_{ik}v_k=w_iv_k^{-1}v_k=w_i$$

이므로 $Av=w$이다. 즉 $0$이 아닌 임의의 원소가 $D^n$ 전체를 생성하므로 $D^n$은 simple이다. 그럼 2의 분해가 simple module들의 직합이므로 $\Mat_n(D)$는 semisimple ring이다.
:::

::: 명제 6
위 상황에서 $\End_{\Mat_n(D)}(D^n)\cong D^{\mathrm{op}}$이다.
:::
::: 증명
$d\in D$에 대하여 성분별 오른쪽 곱셈 $\rho_d(v)=vd$를 생각하자. 임의의 행렬 $A$에 대하여 $(A(vd))_i=\sum_jA_{ij}(v_jd)=(Av)_id$이므로 $\rho_d$는 module endomorphism이다. 또 $\rho_d\circ\rho_{d'}(v)=vd'd=\rho_{d'd}(v)$이므로 $d\mapsto\rho_d$는 ring homomorphism $D^{\mathrm{op}}\rightarrow\End_{\Mat_n(D)}(D^n)$을 정의하고, $\rho_d$가 첫째 표준 열벡터 $e_1$을 $e_1d$로 보내므로 이는 단사이다.

전사임을 보이자. $\varphi$를 임의의 endomorphism이라 하고 $E_{ij}$를 matrix unit이라 하면, $E_{11}e_1=e_1$이므로 $E_{11}\varphi(e_1)=\varphi(e_1)$이고, 왼쪽 변은 $\varphi(e_1)$의 첫 성분만 남긴 벡터이므로 $\varphi(e_1)=e_1d$인 $d\in D$가 존재한다. 이제 임의의 $v\in D^n$에 대하여, $(i,1)$ 성분이 $v_i$이고 나머지가 $0$인 행렬을 $A_i$라 하면 $v=\sum_iA_ie_1$이므로

$$\varphi(v)=\sum_iA_i\varphi(e_1)=\sum_iA_i(e_1d)=vd=\rho_d(v)$$

이다. 따라서 $\varphi=\rho_d$이고 대응은 전사이다.
:::

이 두 명제로 행렬환 쪽의 재료는 끝났다. 이제 semisimple ring을 행렬환으로 옮겨 줄 endomorphism ring 계산들을 준비한다.

::: 보조정리 7
임의의 ring $A$에 대하여 $\End_A(A)\cong A^{\mathrm{op}}$이다.
:::
::: 증명
$\Phi:\End_A(A)\rightarrow A^{\mathrm{op}}$를 $\Phi(f)=f(1)$로 정의하자. $f$가 $A$-linear이므로 $f(a)=f(a\cdot 1)=af(1)$, 즉 $f$는 $f(1)$의 오른쪽 곱셈이다. $\Phi$는 additive이고 $\Phi(\id)=1$이며,

$$\Phi(f\circ g)=f(g(1))=g(1)f(1)=\Phi(f)\ast\Phi(g)$$

이므로 $A^{\mathrm{op}}$로의 ring homomorphism이다. 거꾸로 $a\in A$에 대해 오른쪽 곱셈 $x\mapsto xa$는 left module endomorphism이고 이 대응이 $\Phi$의 역을 주므로 $\Phi$는 isomorphism이다.
:::

::: 보조정리 8
$S_1,\ldots,S_k$가 서로 isomorphic하지 않은 simple module들이고 $n_1,\ldots,n_k\geq 1$일 때, $M=\bigoplus_{i=1}^kS_i^{n_i}$에 대하여

$$\End_A(M)\cong\prod_{i=1}^k\Mat_{n_i}\big(\End_A(S_i)\big)$$

이다.
:::
::: 증명
직합 인자들에 대한 inclusion과 projection을 각각 $\iota_{i,a}$, $\pi_{i,a}$로 적자 ($1\leq a\leq n_i$). Endomorphism $\varphi$의 성분 $\pi_{i,a}\circ\varphi\circ\iota_{j,b}$는 $S_j$에서 $S_i$로 가는 homomorphism인데, $i\neq j$이면 [§나눗셈환, ⁋보조정리 10](/ko/math/ring_theory/division_rings#lem10){: data-lid="wccwq" data-relation="required" }에 의해 nonzero일 경우 isomorphism이 되어 가정에 모순이므로 $0$이다. 따라서 $\varphi$는 각 $i$마다 행렬 $\varphi^{(i)}=(\pi_{i,a}\circ\varphi\circ\iota_{i,b})_{a,b}\in\Mat_{n_i}(\End_A(S_i))$들의 자료와 같다.

이 대응이 ring isomorphism임을 확인하자. 합에 대해서는 자명하고, $\sum_{j,b}\iota_{j,b}\circ\pi_{j,b}=\id_M$이므로

$$\pi_{i,a}\circ(\varphi\circ\psi)\circ\iota_{i,c}=\sum_{b}(\pi_{i,a}\circ\varphi\circ\iota_{i,b})\circ(\pi_{i,b}\circ\psi\circ\iota_{i,c})$$

이고, 이는 정확히 행렬곱의 $(a,c)$ 성분이다. 역대응은 행렬 자료로부터 $\varphi=\sum\iota\circ\varphi_{ab}\circ\pi$를 조립하면 된다.
:::

::: 보조정리 9
임의의 ring $\Delta$에 대하여 transpose는 isomorphism $\Mat_n(\Delta)^{\mathrm{op}}\cong\Mat_n(\Delta^{\mathrm{op}})$을 준다.
:::
::: 증명
$T(A)=A^{\mathsf{T}}$는 additive bijection이고 항등행렬을 보존한다. $\Mat_n(\Delta)^{\mathrm{op}}$의 곱 $A\ast B=BA$에 대하여

$$T(A\ast B)_{ij}=(BA)_{ji}=\sum_kB_{jk}A_{ki}$$

이고, $\Mat_n(\Delta^{\mathrm{op}})$에서의 곱은

$$\big(T(A)T(B)\big)_{ij}=\sum_k(A^{\mathsf{T}})_{ik}\ast(B^{\mathsf{T}})_{kj}=\sum_k(B^{\mathsf{T}})_{kj}(A^{\mathsf{T}})_{ik}=\sum_kB_{jk}A_{ki}$$

로 일치한다.
:::

마지막 준비물은 곱환의 module 이론이다.

::: 명제 10
$A=A_1\times\cdots\times A_k$라 하고, $e_i\in A$를 $i$번째 성분만 $1$인 원소라 하자.

1. $\{e_1,\ldots,e_k\}$는 central한 orthogonal idempotent의 complete set이고, 임의의 left $A$-module $M$은 $M=\bigoplus_ie_iM$으로 분해된다. 각 $e_iM$은 $A$가 $i$번째 성분을 통해 작용하는 $A_i$-module이며, 그 $A$-submodule은 $A_i$-submodule과 일치한다. 특히 simple left $A$-module은 정확히, 어떤 $i$에 대한 simple left $A_i$-module을 $i$번째 성분의 작용으로 $A$-module로 본 것들이다.
2. 각 $A_i$가 semisimple ring이면 $A$도 semisimple ring이다.
:::
::: 증명
$e_i$들이 central orthogonal idempotent의 complete set임은 성분별 계산으로 바로 확인되며, 이 상황은 [§멱등원과 곱분해, ⁋정리 5](/ko/math/ring_theory/idempotents#thm5){: data-lid="e0b4o" data-relation="required" }의 direct product decomposition에 대응하는 것이다. 임의의 $m\in M$은 $m=\sum_ie_im$으로 쓰이고, $x\in e_iM\cap\sum_{j\neq i}e_jM$이면 $e_jM$ 위에서 $e_i$가 $e_ie_j=0$으로 작용하므로 $x=e_ix=0$이다. 따라서 $M=\bigoplus_ie_iM$이다. $e_iM$ 위에서 $e_j$ ($j\neq i$) 성분은 $0$으로 작용하므로 $A$의 작용은 $i$번째 성분 $A_i$를 통해서만 이루어지고, 부분집합이 $A$-submodule인 것과 $A_i$-submodule인 것이 같아진다. Simple module의 분류는 이로부터 바로 따라온다. $M$이 simple이면 분해 $M=\bigoplus_ie_iM$의 인자 중 정확히 하나만 nonzero이고 그것이 simple $A_i$-module이며, 역도 마찬가지이다.

2의 경우, left regular module의 분해 $A=\bigoplus_iAe_i$에서 $Ae_i$는 1에 의해 $A_i$의 regular module과 같은 submodule 구조를 가지므로, $A_i$가 semisimple ring이면 $Ae_i$는 simple $A$-submodule들의 직합이다. 따라서 $A$가 simple left ideal들의 직합이 되어 semisimple ring이다.
:::

## 아틴-웨더번 정리

이제 모든 재료가 준비되었다.

::: 정리 11 (Artin-Wedderburn)
Ring $A$에 대하여 다음이 동치이다.

1. $A$는 semisimple ring이다.
2. 적당한 division ring들 $D_1,\ldots,D_k$와 자연수 $n_1,\ldots,n_k$에 대하여

$$A\cong\Mat_{n_1}(D_1)\times\cdots\times\Mat_{n_k}(D_k)$$

이다.

나아가 이 분해의 자료 $k$와 $(n_i,D_i)$들은 순서와 isomorphism을 무시하면 유일하다.
:::
::: 증명
$2\implies 1$은 [명제 5](#prop5){: data-lid="aw3ne" data-relation="required" }에 의해 각 인자가 semisimple ring이므로 [명제 10](#prop10){: data-lid="l9ws8" data-relation="required" }의 2에서 바로 얻어진다.

$1\implies 2$를 보자. [명제 3](#prop3){: data-lid="jyozf" data-relation="required" }에 의해 $A$는 유한개의 simple left ideal의 직합이고, isomorphism class별로 인자들을 모으면 서로 isomorphic하지 않은 simple module들 $S_1,\ldots,S_k$와 자연수 $n_i\geq 1$에 대하여 left module로서 $A\cong\bigoplus_iS_i^{n_i}$이다. $\Delta_i=\End_A(S_i)$로 두면 이는 [§나눗셈환, ⁋보조정리 10](/ko/math/ring_theory/division_rings#lem10){: data-lid="uauah" data-relation="required" }에 의해 division ring이고, [보조정리 7](#lem7){: data-lid="reb59" data-relation="required" }과 [보조정리 8](#lem8){: data-lid="m01xr" data-relation="required" }에 의해

$$A^{\mathrm{op}}\cong\End_A(A)\cong\prod_{i=1}^k\Mat_{n_i}(\Delta_i)$$

이다. 양변의 opposite ring을 취하면, 곱환의 opposite은 opposite들의 곱이므로 [보조정리 9](#lem9){: data-lid="2hk1d" data-relation="required" }에 의해

$$A\cong\prod_{i=1}^k\Mat_{n_i}(\Delta_i)^{\mathrm{op}}\cong\prod_{i=1}^k\Mat_{n_i}(\Delta_i^{\mathrm{op}})$$

이고, $D_i=\Delta_i^{\mathrm{op}}$는 division ring이므로 원하는 분해를 얻는다.

유일성을 보이자. $A\cong\prod_{j=1}^l\Mat_{m_j}(E_j)$가 임의의 그러한 분해라 하고 $W_j=E_j^{m_j}$를 $j$번째 성분을 통한 left $A$-module로 보자. [명제 5](#prop5){: data-lid="qlrxy" data-relation="required" }에 의해 각 $W_j$는 simple이고 $j$번째 인자의 regular module이 $W_j^{m_j}$와 isomorphic하므로, left module로서 $A\cong\bigoplus_jW_j^{m_j}$이다. 또 [명제 10](#prop10){: data-lid="yl0q8" data-relation="required" }의 1에 의해 $W_j$들은 서로 다른 성분에 속하므로 pairwise non-isomorphic하다. 그럼 [§반단순가군, ⁋명제 10](/ko/math/ring_theory/semisimple_modules#prop10){: data-lid="wprdz" data-relation="required" }에 의해 두 분해 $\bigoplus_iS_i^{n_i}\cong\bigoplus_jW_j^{m_j}$의 자료가 일치한다. 즉 $l=k$이고 재배열 후 $W_i\cong S_i$, $m_i=n_i$이다. 마지막으로 [명제 10](#prop10){: data-lid="c9hgr" data-relation="required" }의 1에 의해 $\End_A(W_i)=\End_{\Mat_{m_i}(E_i)}(E_i^{m_i})$이고 [명제 6](#prop6){: data-lid="wlly1" data-relation="required" }에 의해 이는 $E_i^{\mathrm{op}}$와 isomorphic하므로

$$E_i\cong\End_A(W_i)^{\mathrm{op}}\cong\End_A(S_i)^{\mathrm{op}}=\Delta_i^{\mathrm{op}}=D_i$$

이다. 따라서 division ring들도 isomorphism을 무시하면 유일하다.
:::

증명이 보여 주듯 분해의 각 인자는 canonical한 대상이다. 실제로 존재 방향의 분해에서 isotypic component $A_{S_i}\cong S_i^{n_i}$들은 two-sided ideal인데, 임의의 $a\in A$에 대한 오른쪽 곱셈이 left module endomorphism이고 [§반단순가군, ⁋명제 9](/ko/math/ring_theory/semisimple_modules#prop9){: data-lid="hwkom" data-relation="required" }에 의해 endomorphism이 isotypic component를 보존하기 때문이다. 따라서 $A=\bigoplus_iA_{S_i}$는 two-sided ideal들의 직합이고, [§멱등원과 곱분해, ⁋정리 5](/ko/math/ring_theory/idempotents#thm5){: data-lid="i4elc" data-relation="required" }에 의해 central idempotent의 complete set과 ring의 direct product decomposition이 대응된다. 이 central idempotent들이 정확히 [정리 11](#thm11){: data-lid="p9h4v" data-relation="required" }의 direct product decomposition에서 각 인자의 항등원이다.

::: 따름정리 12
$A\cong\prod_{i=1}^k\Mat_{n_i}(D_i)$가 semisimple ring이라 하자. 그럼 simple left $A$-module은 isomorphism을 무시하면 정확히 $V_1,\ldots,V_k$ ($V_i=D_i^{n_i}$)뿐이고, 임의의 left $A$-module은 이들의 복사본들의 직합이다.
:::
::: 증명
[명제 2](#prop2){: data-lid="c2mpv" data-relation="required" }에 의해 모든 module이 semisimple이므로 simple들의 직합이고, [명제 5](#prop5){: data-lid="pg0b4" data-relation="required" }와 [명제 10](#prop10){: data-lid="zkbod" data-relation="required" }에 의해 각 $V_i$는 simple이다. 거꾸로 $M$이 simple이면 $0\neq x\in M$에 대해 $M=Ax$이므로 전사 $A\rightarrow M$이 존재하고, left module decomposition $A\cong\bigoplus_iV_i^{n_i}$의 어떤 인자 $V_i$ 위에서 이 전사가 nonzero가 된다. 그럼 simple module 사이의 nonzero homomorphism $V_i\rightarrow M$이 존재하므로 [§나눗셈환, ⁋보조정리 10](/ko/math/ring_theory/division_rings#lem10){: data-lid="aib2j" data-relation="required" }에 의해 $M\cong V_i$이다.
:::

::: 참고 13
정의 1은 left module 구조로 주어졌지만, right module로 정의해도 같은 ring들을 얻는다. Right $A$-module은 left $A^{\mathrm{op}}$-module과 같으므로, $A$가 right semisimple이라는 것은 $A^{\mathrm{op}}$가 semisimple ring이라는 것이다. 그런데 $A$가 semisimple ring이면 [정리 11](#thm11){: data-lid="gy0gw" data-relation="required" }의 분해에 [보조정리 9](#lem9){: data-lid="t2e0p" data-relation="required" }를 적용하여 $A^{\mathrm{op}}\cong\prod_i\Mat_{n_i}(D_i^{\mathrm{op}})$ 또한 행렬환들의 곱이 되므로 semisimple ring이고, 역도 symmetric으로 성립한다. 따라서 semisimple ring의 개념은 좌우의 선택과 무관하다.
:::

::: 참고 14
Finite group $G$의 group algebra $\mathbb{C}[G]$는 이 정리의 대표적인 응용처이다. [\[표현론\] §유한군의 표현론, ⁋따름정리 7](/ko/math/representation_theory/representations_of_finite_groups#cor7){: data-lid="6mmx5" data-relation="weak" }에 의해 모든 유한차원 representation이 semisimple $\mathbb{C}[G]$-module이고, 특히 regular representation $\mathbb{C}[G]$ 자신이 그러하므로 $\mathbb{C}[G]$는 semisimple ring이다. [정리 11](#thm11){: data-lid="n8xw6" data-relation="required" }의 분해에 등장하는 division ring들은 simple module $V_i$의 endomorphism ring으로부터 나오는데, algebraically closed field 위의 유한차원 representation에서는 $\End_{\mathbb{C}[G]}(V_i)\cong\mathbb{C}$이므로 ([같은 글, ⁋보조정리 8](/ko/math/representation_theory/representations_of_finite_groups#lem8){: data-lid="ocojm" data-relation="weak" }) 모든 $D_i$가 $\mathbb{C}$가 된다. 따라서

$$\mathbb{C}[G]\cong\prod_{i=1}^k\Mat_{d_i}(\mathbb{C})$$

이고, 여기서 $d_i$는 irreducible representation들의 차원, $k$는 그 개수이다. 양변의 $\mathbb{C}$-차원을 비교하면 곧바로 $\lvert G\rvert=\sum_{i=1}^kd_i^2$를 얻는다.
:::

---

**참고문헌**

**[DF]** D. S. Dummit and R. M. Foote, *Abstract algebra*, 3rd ed., Wiley, 2004.  
**[Her]** I. N. Herstein, *Noncommutative rings*, Carus Mathematical Monographs 15, Mathematical Association of America, 1968.  
**[Lam]** T. Y. Lam, *A first course in noncommutative rings*, 2nd ed., Graduate Texts in Mathematics 131, Springer, 2001.
