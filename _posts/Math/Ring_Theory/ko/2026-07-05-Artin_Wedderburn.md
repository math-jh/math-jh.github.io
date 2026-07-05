---
title: "Artin-Wedderburn 정리"
description: "자기 자신 위의 module로서 semisimple인 환을 semisimple ring으로 정의하고, 이것이 모든 module이 semisimple인 것과 동치임을 보인다. Division ring 위의 행렬환의 module 구조와 opposite ring·endomorphism ring 계산을 거쳐, semisimple ring이 division ring 위의 행렬환 유한개의 곱으로 유일하게 분해된다는 Artin-Wedderburn 정리를 증명한다."
excerpt: "Semisimple ring의 구조 정리 — division ring 위 행렬환들의 곱으로의 유일한 분해"

categories: [Math / Ring Theory]
permalink: /ko/math/ring_theory/artin_wedderburn
sidebar: 
    nav: "ring_theory-ko"

date: 2026-07-05

weight: 2.7

published: false

---

[§Semisimple module](/ko/math/ring_theory/semisimple_modules)에서 우리는 simple module들의 직합으로 분해되는 module을 다루었다. 이 글에서는 그 개념을 환 자신에 적용한다. 환 $$R$$을 자기 자신 위의 left module로 보아 semisimple이 되는 환이 semisimple ring인데, 이는 그 위의 모든 module이 semisimple인 환과 정확히 일치하며, module 이론이 완전히 분해되는 환이라 할 수 있다. 이 글의 목표는 이러한 환의 완전한 분류인 Artin-Wedderburn 정리이다. Semisimple ring은 division ring 위의 행렬환 유한개의 곱과 정확히 같으며, 이 분해는 본질적으로 유일하다. [§Division ring, ⁋보조정리 10](/ko/math/ring_theory/division_rings#lem10)의 Schur 보조정리가 여기 등장하는 division ring의 출처이고, [§Idempotent과 곱분해, ⁋정리 5](/ko/math/ring_theory/idempotents#thm5)의 central idempotent 기계가 곱분해를 담당한다.

이 글에서도 환은 항등원을 갖는, 가환이라 가정하지 않는 환이며, module은 언제나 left module이다.

## Semisimple ring

::: 정의 1
환 $$R$$을 자기 자신 위의 left module로 보았을 때 semisimple이면, 즉 $$R$$이 simple left ideal들의 직합이면 $$R$$을 *semisimple ring<sub>반단순환</sub>*이라 부른다.
:::

Left regular module $$R$$의 submodule은 정확히 $$R$$의 left ideal이므로, 이 정의는 [§Semisimple module, ⁋정의 1](/ko/math/ring_theory/semisimple_modules#def1)을 regular module에 적용한 것이다. 정의가 left module 구조를 사용하므로 좌우 비대칭해 보이지만, 구조 정리를 거치면 이 선택이 무관하다는 것이 드러난다 ([참고 13](#rmk13)).

환 하나의 성질처럼 보이는 이 정의는 사실 그 위의 module 이론 전체를 결정한다.

::: 명제 2
환 $$R$$에 대하여, $$R$$이 semisimple ring인 것은 모든 left $$R$$-module이 semisimple인 것과 동치이다.
:::
::: 증명
모든 module이 semisimple이라면 특히 regular module $$R$$이 semisimple이다. 거꾸로 $$R$$이 semisimple ring이라 하자. 임의의 index 집합 $$I$$에 대하여 free module $$R^{(I)}$$는 $$R$$의 복사본들의 직합이고, 각 복사본이 simple submodule들의 합이므로 $$R^{(I)}$$ 또한 simple submodule들의 합이다. 따라서 [§Semisimple module, ⁋정리 4](/ko/math/ring_theory/semisimple_modules#thm4)에 의해 $$R^{(I)}$$는 semisimple이다. 이제 임의의 module $$M$$은 생성원들을 택하면 적당한 전사 $$R^{(I)}\rightarrow M$$을 가지므로 semisimple module의 quotient이고, [§Semisimple module, ⁋따름정리 5](/ko/math/ring_theory/semisimple_modules#cor5)에 의해 semisimple이다.
:::

::: 명제 3
$$R$$이 semisimple ring이면 $$R$$은 유한개의 simple left ideal의 직합이다.
:::
::: 증명
$$R=\bigoplus_{i\in I}L_i$$를 simple left ideal들의 직합이라 하자. 항등원을 이 분해에 따라 $$1=\sum_{i\in F}x_i$$로 쓰면 $$F$$는 유한집합이다. 그럼 임의의 $$r\in R$$에 대하여 $$r=r\cdot 1\in\sum_{i\in F}L_i$$이므로 $$R=\bigoplus_{i\in F}L_i$$이다.
:::

따라서 semisimple ring은 left module로서 유한한 composition series를 갖는다 ([\[가환대수학\] §조르단-횔더 정리, ⁋정의 2](/ko/math/commutative_algebra/Jordan-Holder_theorem#def2)). 직합 인자를 하나씩 쌓은 chain이 그것이며, 특히 semisimple ring은 left artinian이자 left noetherian이다.

## Division ring 위의 행렬환

구조 정리의 building block은 division ring 위의 행렬환이다. 이를 다루기 위해 먼저 곱셈의 순서를 뒤집은 환을 정의한다.

::: 정의 4
환 $$R$$에 대하여, $$R$$과 같은 abelian group 위에 곱셈을 $$a\ast b=ba$$로 정의한 환을 $$R$$의 *opposite ring<sub>반대환</sub>*이라 부르고 $$R^{\mathrm{op}}$$로 적는다.
:::

정의에서 바로 $$(R^{\mathrm{op}})^{\mathrm{op}}=R$$이고, right $$R$$-module은 left $$R^{\mathrm{op}}$$-module과 같은 것이다. 또 $$D$$가 division ring이면 nonzero 원소의 역원이 그대로 역원이 되므로 $$D^{\mathrm{op}}$$ 또한 division ring이다.

::: 명제 5
$$D$$가 division ring이고 $$n\geq 1$$이라 하자. 열벡터들의 공간 $$D^n$$을 행렬 곱셈으로 left $$\Mat_n(D)$$-module로 보면 다음이 성립한다.

1. $$D^n$$은 simple module이다.
2. $$k$$번째 열 밖에서 $$0$$인 행렬들의 left ideal을 $$C_k$$라 하면 $$\Mat_n(D)=\bigoplus_{k=1}^nC_k$$이고, 각 $$C_k$$는 module로서 $$D^n$$과 isomorphic하다. 특히 $$\Mat_n(D)$$는 semisimple ring이다.
:::
::: 증명
2를 먼저 보자. 행렬을 열별로 나누면 $$\Mat_n(D)=\bigoplus_kC_k$$이고, 왼쪽에서 행렬을 곱하는 연산은 각 열에 독립적으로 작용하므로 $$C_k$$는 left ideal이며, $$k$$번째 열을 읽는 대응 $$C_k\rightarrow D^n$$은 module isomorphism이다.

1을 보이기 위해 $$0\neq v\in D^n$$과 임의의 $$w\in D^n$$을 택하자. $$v_k\neq 0$$인 성분 $$k$$를 고르고, 행렬 $$A$$를 $$A_{ik}=w_iv_k^{-1}$$, 나머지 성분은 $$0$$으로 정의하면

$$(Av)_i=A_{ik}v_k=w_iv_k^{-1}v_k=w_i$$

이므로 $$Av=w$$이다. 즉 $$0$$이 아닌 임의의 원소가 $$D^n$$ 전체를 생성하므로 $$D^n$$은 simple이다. 그럼 2의 분해가 simple module들의 직합이므로 $$\Mat_n(D)$$는 semisimple ring이다.
:::

::: 명제 6
위 상황에서 $$\End_{\Mat_n(D)}(D^n)\cong D^{\mathrm{op}}$$이다.
:::
::: 증명
$$d\in D$$에 대하여 성분별 오른쪽 곱셈 $$\rho_d(v)=vd$$를 생각하자. 임의의 행렬 $$A$$에 대하여 $$(A(vd))_i=\sum_jA_{ij}(v_jd)=(Av)_id$$이므로 $$\rho_d$$는 module endomorphism이다. 또 $$\rho_d\circ\rho_{d'}(v)=vd'd=\rho_{d'd}(v)$$이므로 $$d\mapsto\rho_d$$는 ring homomorphism $$D^{\mathrm{op}}\rightarrow\End_{\Mat_n(D)}(D^n)$$을 정의하고, $$\rho_d$$가 첫째 표준 열벡터 $$e_1$$을 $$e_1d$$로 보내므로 이는 단사이다.

전사임을 보이자. $$\varphi$$를 임의의 endomorphism이라 하고 $$E_{ij}$$를 matrix unit이라 하면, $$E_{11}e_1=e_1$$이므로 $$E_{11}\varphi(e_1)=\varphi(e_1)$$이고, 왼쪽 변은 $$\varphi(e_1)$$의 첫 성분만 남긴 벡터이므로 $$\varphi(e_1)=e_1d$$인 $$d\in D$$가 존재한다. 이제 임의의 $$v\in D^n$$에 대하여, $$(i,1)$$ 성분이 $$v_i$$이고 나머지가 $$0$$인 행렬을 $$A_i$$라 하면 $$v=\sum_iA_ie_1$$이므로

$$\varphi(v)=\sum_iA_i\varphi(e_1)=\sum_iA_i(e_1d)=vd=\rho_d(v)$$

이다. 따라서 $$\varphi=\rho_d$$이고 대응은 전사이다.
:::

이 두 명제로 행렬환 쪽의 재료는 끝났다. 이제 semisimple ring을 행렬환으로 옮겨 줄 endomorphism ring 계산들을 준비한다.

::: 보조정리 7
임의의 환 $$R$$에 대하여 $$\End_R(R)\cong R^{\mathrm{op}}$$이다.
:::
::: 증명
$$\Phi:\End_R(R)\rightarrow R^{\mathrm{op}}$$를 $$\Phi(f)=f(1)$$로 정의하자. $$f$$가 $$R$$-linear이므로 $$f(r)=f(r\cdot 1)=rf(1)$$, 즉 $$f$$는 $$f(1)$$의 오른쪽 곱셈이다. $$\Phi$$는 additive이고 $$\Phi(\id)=1$$이며,

$$\Phi(f\circ g)=f(g(1))=g(1)f(1)=\Phi(f)\ast\Phi(g)$$

이므로 $$R^{\mathrm{op}}$$로의 ring homomorphism이다. 거꾸로 $$r\in R$$에 대해 오른쪽 곱셈 $$x\mapsto xr$$은 left module endomorphism이고 이 대응이 $$\Phi$$의 역을 주므로 $$\Phi$$는 isomorphism이다.
:::

::: 보조정리 8
$$S_1,\ldots,S_k$$가 서로 isomorphic하지 않은 simple module들이고 $$n_1,\ldots,n_k\geq 1$$일 때, $$M=\bigoplus_{i=1}^kS_i^{n_i}$$에 대하여

$$\End_R(M)\cong\prod_{i=1}^k\Mat_{n_i}\big(\End_R(S_i)\big)$$

이다.
:::
::: 증명
직합 인자들에 대한 inclusion과 projection을 각각 $$\iota_{i,a}$$, $$\pi_{i,a}$$로 적자 ($$1\leq a\leq n_i$$). Endomorphism $$\varphi$$의 성분 $$\pi_{i,a}\circ\varphi\circ\iota_{j,b}$$는 $$S_j$$에서 $$S_i$$로 가는 homomorphism인데, $$i\neq j$$이면 [§Division ring, ⁋보조정리 10](/ko/math/ring_theory/division_rings#lem10)에 의해 nonzero일 경우 isomorphism이 되어 가정에 모순이므로 $$0$$이다. 따라서 $$\varphi$$는 각 $$i$$마다 행렬 $$\varphi^{(i)}=(\pi_{i,a}\circ\varphi\circ\iota_{i,b})_{a,b}\in\Mat_{n_i}(\End_R(S_i))$$들의 자료와 같다.

이 대응이 ring isomorphism임을 확인하자. 합에 대해서는 자명하고, $$\sum_{j,b}\iota_{j,b}\circ\pi_{j,b}=\id_M$$이므로

$$\pi_{i,a}\circ(\varphi\circ\psi)\circ\iota_{i,c}=\sum_{b}(\pi_{i,a}\circ\varphi\circ\iota_{i,b})\circ(\pi_{i,b}\circ\psi\circ\iota_{i,c})$$

이고, 이는 정확히 행렬곱의 $$(a,c)$$ 성분이다. 역대응은 행렬 자료로부터 $$\varphi=\sum\iota\circ\varphi_{ab}\circ\pi$$를 조립하면 된다.
:::

::: 보조정리 9
임의의 환 $$\Delta$$에 대하여 transpose는 isomorphism $$\Mat_n(\Delta)^{\mathrm{op}}\cong\Mat_n(\Delta^{\mathrm{op}})$$을 준다.
:::
::: 증명
$$T(A)=A^{\mathsf{T}}$$는 additive bijection이고 항등행렬을 보존한다. $$\Mat_n(\Delta)^{\mathrm{op}}$$의 곱 $$A\ast B=BA$$에 대하여

$$T(A\ast B)_{ij}=(BA)_{ji}=\sum_kB_{jk}A_{ki}$$

이고, $$\Mat_n(\Delta^{\mathrm{op}})$$에서의 곱은

$$\big(T(A)T(B)\big)_{ij}=\sum_k(A^{\mathsf{T}})_{ik}\ast(B^{\mathsf{T}})_{kj}=\sum_k(B^{\mathsf{T}})_{kj}(A^{\mathsf{T}})_{ik}=\sum_kB_{jk}A_{ki}$$

로 일치한다.
:::

마지막 준비물은 곱환의 module 이론이다.

::: 명제 10
$$R=R_1\times\cdots\times R_k$$라 하고, $$e_i\in R$$를 $$i$$번째 성분만 $$1$$인 원소라 하자.

1. $$\{e_1,\ldots,e_k\}$$는 central한 orthogonal idempotent의 complete set이고, 임의의 left $$R$$-module $$M$$은 $$M=\bigoplus_ie_iM$$으로 분해된다. 각 $$e_iM$$은 $$R$$이 $$i$$번째 성분을 통해 작용하는 $$R_i$$-module이며, 그 $$R$$-submodule은 $$R_i$$-submodule과 일치한다. 특히 simple left $$R$$-module은 정확히, 어떤 $$i$$에 대한 simple left $$R_i$$-module을 $$i$$번째 성분의 작용으로 $$R$$-module로 본 것들이다.
2. 각 $$R_i$$가 semisimple ring이면 $$R$$도 semisimple ring이다.
:::
::: 증명
$$e_i$$들이 central orthogonal idempotent의 complete set임은 성분별 계산으로 바로 확인되며, 이 상황은 [§Idempotent과 곱분해, ⁋정리 5](/ko/math/ring_theory/idempotents#thm5)의 곱분해에 대응하는 것이다. 임의의 $$m\in M$$은 $$m=\sum_ie_im$$으로 쓰이고, $$x\in e_iM\cap\sum_{j\neq i}e_jM$$이면 $$e_jM$$ 위에서 $$e_i$$가 $$e_ie_j=0$$으로 작용하므로 $$x=e_ix=0$$이다. 따라서 $$M=\bigoplus_ie_iM$$이다. $$e_iM$$ 위에서 $$e_j$$ ($$j\neq i$$) 성분은 $$0$$으로 작용하므로 $$R$$의 작용은 $$i$$번째 성분 $$R_i$$를 통해서만 이루어지고, 부분집합이 $$R$$-submodule인 것과 $$R_i$$-submodule인 것이 같아진다. Simple module의 분류는 이로부터 바로 따라온다. $$M$$이 simple이면 분해 $$M=\bigoplus_ie_iM$$의 인자 중 정확히 하나만 nonzero이고 그것이 simple $$R_i$$-module이며, 역도 마찬가지이다.

2의 경우, left regular module의 분해 $$R=\bigoplus_iRe_i$$에서 $$Re_i$$는 1에 의해 $$R_i$$의 regular module과 같은 submodule 구조를 가지므로, $$R_i$$가 semisimple ring이면 $$Re_i$$는 simple $$R$$-submodule들의 직합이다. 따라서 $$R$$이 simple left ideal들의 직합이 되어 semisimple ring이다.
:::

## Artin-Wedderburn 정리

이제 모든 재료가 준비되었다.

::: 정리 11 (Artin-Wedderburn)
환 $$R$$에 대하여 다음이 동치이다.

1. $$R$$은 semisimple ring이다.
2. 적당한 division ring들 $$D_1,\ldots,D_k$$와 자연수 $$n_1,\ldots,n_k$$에 대하여

$$R\cong\Mat_{n_1}(D_1)\times\cdots\times\Mat_{n_k}(D_k)$$

이다.

나아가 이 분해의 자료 $$k$$와 $$(n_i,D_i)$$들은 순서와 isomorphism을 무시하면 유일하다.
:::
::: 증명
$$2\implies 1$$은 [명제 5](#prop5)에 의해 각 인자가 semisimple ring이므로 [명제 10](#prop10)의 2에서 바로 얻어진다.

$$1\implies 2$$를 보자. [명제 3](#prop3)에 의해 $$R$$은 유한개의 simple left ideal의 직합이고, isomorphism class별로 인자들을 모으면 서로 isomorphic하지 않은 simple module들 $$S_1,\ldots,S_k$$와 자연수 $$n_i\geq 1$$에 대하여 left module로서 $$R\cong\bigoplus_iS_i^{n_i}$$이다. $$\Delta_i=\End_R(S_i)$$로 두면 이는 [§Division ring, ⁋보조정리 10](/ko/math/ring_theory/division_rings#lem10)에 의해 division ring이고, [보조정리 7](#lem7)과 [보조정리 8](#lem8)에 의해

$$R^{\mathrm{op}}\cong\End_R(R)\cong\prod_{i=1}^k\Mat_{n_i}(\Delta_i)$$

이다. 양변의 opposite ring을 취하면, 곱환의 opposite은 opposite들의 곱이므로 [보조정리 9](#lem9)에 의해

$$R\cong\prod_{i=1}^k\Mat_{n_i}(\Delta_i)^{\mathrm{op}}\cong\prod_{i=1}^k\Mat_{n_i}(\Delta_i^{\mathrm{op}})$$

이고, $$D_i=\Delta_i^{\mathrm{op}}$$는 division ring이므로 원하는 분해를 얻는다.

유일성을 보이자. $$R\cong\prod_{j=1}^l\Mat_{m_j}(E_j)$$가 임의의 그러한 분해라 하고 $$W_j=E_j^{m_j}$$를 $$j$$번째 성분을 통한 left $$R$$-module로 보자. [명제 5](#prop5)에 의해 각 $$W_j$$는 simple이고 $$j$$번째 인자의 regular module이 $$W_j^{m_j}$$와 isomorphic하므로, left module로서 $$R\cong\bigoplus_jW_j^{m_j}$$이다. 또 [명제 10](#prop10)의 1에 의해 $$W_j$$들은 서로 다른 성분에 속하므로 pairwise non-isomorphic하다. 그럼 [§Semisimple module, ⁋명제 9](/ko/math/ring_theory/semisimple_modules#prop9)에 의해 두 분해 $$\bigoplus_iS_i^{n_i}\cong\bigoplus_jW_j^{m_j}$$의 자료가 일치한다. 즉 $$l=k$$이고 재배열 후 $$W_i\cong S_i$$, $$m_i=n_i$$이다. 마지막으로 [명제 10](#prop10)의 1에 의해 $$\End_R(W_i)=\End_{\Mat_{m_i}(E_i)}(E_i^{m_i})$$이고 [명제 6](#prop6)에 의해 이는 $$E_i^{\mathrm{op}}$$와 isomorphic하므로

$$E_i\cong\End_R(W_i)^{\mathrm{op}}\cong\End_R(S_i)^{\mathrm{op}}=\Delta_i^{\mathrm{op}}=D_i$$

이다. 따라서 division ring들도 isomorphism을 무시하면 유일하다.
:::

증명이 보여 주듯 분해의 각 인자는 canonical한 대상이다. 실제로 존재 방향의 분해에서 isotypic component $$R_{S_i}\cong S_i^{n_i}$$들은 two-sided ideal인데, 임의의 $$r\in R$$에 대한 오른쪽 곱셈이 left module endomorphism이고 [§Semisimple module, ⁋명제 8](/ko/math/ring_theory/semisimple_modules#prop8)에 의해 endomorphism이 isotypic component를 보존하기 때문이다. 따라서 $$R=\bigoplus_iR_{S_i}$$는 two-sided ideal들의 직합이고, [§Idempotent과 곱분해, ⁋정리 5](/ko/math/ring_theory/idempotents#thm5)에 의해 central idempotent의 complete set과 환의 곱분해가 대응된다. 이 central idempotent들이 정확히 [정리 11](#thm11)의 곱분해에서 각 인자의 항등원이다.

::: 따름정리 12
$$R\cong\prod_{i=1}^k\Mat_{n_i}(D_i)$$가 semisimple ring이라 하자. 그럼 simple left $$R$$-module은 isomorphism을 무시하면 정확히 $$V_1,\ldots,V_k$$ ($$V_i=D_i^{n_i}$$)뿐이고, 임의의 left $$R$$-module은 이들의 복사본들의 직합이다.
:::
::: 증명
[명제 2](#prop2)에 의해 모든 module이 semisimple이므로 simple들의 직합이고, [명제 5](#prop5)와 [명제 10](#prop10)에 의해 각 $$V_i$$는 simple이다. 거꾸로 $$M$$이 simple이면 $$0\neq x\in M$$에 대해 $$M=Rx$$이므로 전사 $$R\rightarrow M$$이 존재하고, left module 분해 $$R\cong\bigoplus_iV_i^{n_i}$$의 어떤 인자 $$V_i$$ 위에서 이 전사가 nonzero가 된다. 그럼 simple module 사이의 nonzero homomorphism $$V_i\rightarrow M$$이 존재하므로 [§Division ring, ⁋보조정리 10](/ko/math/ring_theory/division_rings#lem10)에 의해 $$M\cong V_i$$이다.
:::

::: 참고 13
정의 1은 left module 구조로 주어졌지만, right module로 정의해도 같은 환들을 얻는다. Right $$R$$-module은 left $$R^{\mathrm{op}}$$-module과 같으므로, $$R$$이 right semisimple이라는 것은 $$R^{\mathrm{op}}$$가 semisimple ring이라는 것이다. 그런데 $$R$$이 semisimple ring이면 [정리 11](#thm11)의 분해에 [보조정리 9](#lem9)를 적용하여 $$R^{\mathrm{op}}\cong\prod_i\Mat_{n_i}(D_i^{\mathrm{op}})$$ 또한 행렬환들의 곱이 되므로 semisimple ring이고, 역도 대칭적으로 성립한다. 따라서 semisimple ring의 개념은 좌우의 선택과 무관하다.
:::

::: 참고 14
유한군 $$G$$의 group algebra $$\mathbb{C}[G]$$는 이 정리의 대표적인 응용처이다. Maschke 정리 ([\[표현론\] §유한군의 표현론, ⁋따름정리 7](/ko/math/representation_theory/representations_of_finite_groups#cor7))에 의해 모든 유한차원 representation이 semisimple $$\mathbb{C}[G]$$-module이고, 특히 regular representation $$\mathbb{C}[G]$$ 자신이 그러하므로 $$\mathbb{C}[G]$$는 semisimple ring이다. [정리 11](#thm11)의 분해에 등장하는 division ring들은 simple module $$V_i$$의 endomorphism ring으로부터 나오는데, algebraically closed field 위의 유한차원 표현에서는 $$\End_{\mathbb{C}[G]}(V_i)\cong\mathbb{C}$$이므로 ([같은 글, ⁋보조정리 8](/ko/math/representation_theory/representations_of_finite_groups#lem8)) 모든 $$D_i$$가 $$\mathbb{C}$$가 된다. 따라서

$$\mathbb{C}[G]\cong\prod_{i=1}^k\Mat_{d_i}(\mathbb{C})$$

이고, 여기서 $$d_i$$는 irreducible representation들의 차원, $$k$$는 그 개수이다. 양변의 $$\mathbb{C}$$-차원을 비교하면 곧바로 $$\lvert G\rvert=\sum_{i=1}^kd_i^2$$를 얻는다.
:::

---

**참고문헌**

**[DF]** D. S. Dummit and R. M. Foote, *Abstract algebra*, 3rd ed., Wiley, 2004.

**[Her]** I. N. Herstein, *Noncommutative rings*, Carus Mathematical Monographs 15, Mathematical Association of America, 1968.

**[Lam]** T. Y. Lam, *A first course in noncommutative rings*, 2nd ed., Graduate Texts in Mathematics 131, Springer, 2001.
