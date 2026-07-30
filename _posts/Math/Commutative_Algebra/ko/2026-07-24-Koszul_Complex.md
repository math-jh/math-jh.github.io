---
title: "코쥴 복합체"
description: "코쥴 복합체의 기본 성질인 양 끝 호몰로지의 계산과 소멸 아이디얼, 자기쌍대성을 살펴보고, 긴 완전열을 통해 정칙렬의 코쥴 호몰로지가 소멸함을 보인다. 뇌터 국소환에서는 역이 성립하여 정칙렬의 순서 교환 불변성이 따라오며, 정칙국소환의 잉여류체의 Tor 계산으로 마무리한다."
excerpt: "Koszul complex와 regular sequence의 homological 판정"

categories: [Math / Commutative Algebra]
permalink: /ko/math/commutative_algebra/koszul_complex
sidebar: 
    nav: "commutative_algebra-ko"

date: 2026-07-24
weight: 23
published: false
drift_needed: true

---

[§정칙국소환](/ko/math/commutative_algebra/regular_local_rings)에서 우리는 $A$-sequence의 개념을 도입하고, regular local ring의 regular system of parameters가 항상 $A$-sequence를 이룬다는 것을 살펴보았다. 한편 [\[호몰로지 대수학\] §Ext와 Tor, ⁋정의 7](/ko/math/homological_algebra/ext_and_tor#def7)에서는 Koszul complex를 정의하고, regular sequence의 Koszul complex가 free resolution을 준다는 것을 확인하였다. 이번 글에서는 이 대응을 반대 방향으로도 완성한다. 즉 Koszul complex의 homology가 주어진 원소들이 regular sequence로부터 얼마나 떨어져 있는지를 재는 불변량이라는 것을 살펴보고, 특히 Noetherian local ring에서는 이 homology의 소멸이 regular sequence 조건과 정확히 동치라는 것을 증명한다. 이로부터 local ring에서는 regular sequence의 순서를 마음대로 바꿀 수 있다는, 정의만 보아서는 명백하지 않은 사실이 따라온다.

## 코쥴 복합체

Koszul complex의 정의를 다시 떠올리자. Rank $n$의 free $A$-module $F$와 $A$-linear map $\varphi:F \rightarrow A$가 주어지면, Koszul complex $K(\varphi)$는 exterior algebra $\bigwedge F$에 chain complex 구조를 준 것이다. ([\[다중선형대수학\] §텐서대수, ⁋정의 10](/ko/math/multilinear_algebra/tensor_algebras#def10), [\[호몰로지 대수학\] §Ext와 Tor, ⁋정의 7](/ko/math/homological_algebra/ext_and_tor#def7)) 즉 $K_i=\bigwedge\nolimits^iF$이고, differential $d$는 임의의 $f\in F$에 대하여 $d(f)=\varphi(f)$로 주어지며 Leibniz rule

$$d(\xi\wedge \eta)=d\xi\wedge \eta+(-1)^{\deg\xi}\xi\wedge d\eta$$

을 만족하는 유일한 degree $-1$의 graded derivation이다. 이 글에서는 언제나 $A$의 원소들 $x_1,\ldots, x_n$을 고정하고, basis $e_1,\ldots, e_n$을 갖는 free module $F=\bigoplus_{i=1}^n Ae_i$와 $\varphi(e_i)=x_i$로 정의된 $\varphi$를 생각하며, 이 때의 $K(\varphi)$를 $K(x_1,\ldots, x_n)$으로 적는다.

[\[다중선형대수학\] §텐서대수, ⁋명제 13](/ko/math/multilinear_algebra/tensor_algebras#prop13)에 의하여 $\bigwedge\nolimits^iF$는 $i$개의 원소로 이루어진 부분집합 $J=\{j_1<\cdots<j_i\}\subseteq \{1,\ldots, n\}$들에 대응되는 원소 $e_J=e_{j_1}\wedge\cdots\wedge e_{j_i}$들을 basis로 갖는 free module이다. 특히 $K_i(x_1,\ldots,x_n)\cong A^{\oplus\binom{n}{i}}$이며, $i<0$이거나 $i>n$이면 $K_i(x_1,\ldots,x_n)=0$이다. Differential은 Leibniz rule을 반복하여 적용하면 다음의 식

$$d(e_{j_1}\wedge\cdots\wedge e_{j_i})=\sum_{k=1}^i(-1)^{k-1}x_{j_k}e_{j_1}\wedge\cdots\wedge\widehat{e_{j_k}}\wedge\cdots\wedge e_{j_i}$$

으로 주어진다. 여기서 $\widehat{e_{j_k}}$는 해당 원소를 생략한다는 표기이며, 이 식은 index들 $j_1,\ldots, j_i$가 증가하는 순서로 배열되어 있지 않아도 성립한다. $d\circ d=0$이라는 것도 이 식에서 다시 확인할 수 있는데, $d$를 두 번 적용하면 $k<l$에 대하여 $x_{j_k}x_{j_l}$이 곱해진 각 항이 $e_{j_k}$를 먼저 지우는지 $e_{j_l}$을 먼저 지우는지에 따라 부호 $(-1)^{k-1}(-1)^{l-2}$와 $(-1)^{l-1}(-1)^{k-1}$로 정확히 두 번 나타나 서로 소거되기 때문이다.

가장 작은 경우들을 적어보면, $n=1$일 때 $K(x_1)$은 다음의 complex

$$0 \rightarrow A \overset{x_1}{\longrightarrow} A \rightarrow 0$$

이고, $n=2$일 때 $K(x_1,x_2)$는 다음의 complex

$$0 \rightarrow A \overset{d_2}{\longrightarrow} A^{\oplus 2}\overset{d_1}{\longrightarrow} A \rightarrow 0$$

이며, 위의 명시적인 식에 의하여 $d_2(e_1\wedge e_2)=x_1e_2-x_2e_1$이고 $d_1(ae_1+be_2)=ax_1+bx_2$이다. 그럼 degree $1$의 cycle $ae_1+be_2$는 관계식 $ax_1+bx_2=0$에 대응되고, boundary들은 자명한 관계식 $(-x_2)x_1+x_1x_2=0$의 배수들에 대응된다. 즉 degree $1$의 homology는 $x_1,x_2$ 사이의 관계식 중 자명하지 않은 것들을 측정한다. 이러한 정보를 module에 대해서도 다루기 위해 다음을 정의한다.

::: 정의 1
Ring $A$의 원소들 $x_1,\ldots, x_n$과 $A$-module $M$에 대하여, $M$에 계수를 갖는 *Koszul complex*를

$$K(x_1,\ldots, x_n; M)=K(x_1,\ldots,x_n)\otimes_AM$$

으로 정의한다. 또, 이 complex의 $i$번째 homology를 $M$의 *$i$번째 Koszul homology*라 부르고 $H_i(x_1,\ldots, x_n;M)$으로 적는다. ([\[호몰로지 대수학\] §호몰로지, ⁋정의 2](/ko/math/homological_algebra/homology#def2))
:::

이하 표기의 편의를 위해 $x=(x_1,\ldots,x_n)$으로 줄여 $K(x;M)$, $H_i(x;M)$ 등으로 적고, $x_1,\ldots,x_n$이 생성하는 ideal을 $(x)$로, $(x)M$을 $xM$으로 적는다. 정의에 의하여 $K_i(x;M)\cong M^{\oplus\binom{n}{i}}$이므로 $H_i(x;M)$은 $0\leq i\leq n$ 바깥에서 언제나 $0$이고, $M=A$일 때는 $H_i(x;A)=H_i(K(x))$이다. 양 끝의 두 Koszul homology는 다음과 같이 익숙한 대상들이다.

::: 명제 2
위와 같은 상황에서 다음이 성립한다.

1. $H_0(x;M)=M/xM$이다.
2. $H_n(x;M)=\{m\in M\mid x_1m=\cdots=x_nm=0\}$이다.
:::
::: 증명
첫째 결과를 보이자. $d_1\otimes\id_M: F\otimes_AM \rightarrow M$은 $e_i\otimes m$을 $x_im$으로 보내므로 그 image는 정확히 $xM$이고, $K_0(x;M)=M$이므로 $H_0(x;M)=M/xM$이다.

둘째 결과를 보이자. $\omega=e_1\wedge\cdots\wedge e_n$으로 두면 $K_n(x;M)$의 원소는 $\omega\otimes m$의 꼴이고, differential의 명시적인 식에 의하여

$$(d_n\otimes\id_M)(\omega\otimes m)=\sum_{k=1}^n(-1)^{k-1}(e_1\wedge\cdots\wedge\widehat{e_k}\wedge\cdots\wedge e_n)\otimes x_km$$

이다. 그런데 $e_1\wedge\cdots\wedge\widehat{e_k}\wedge\cdots\wedge e_n$들은 $\bigwedge\nolimits^{n-1}F$의 basis를 이루므로 ([\[다중선형대수학\] §텐서대수, ⁋명제 13](/ko/math/multilinear_algebra/tensor_algebras#prop13)), 위의 식이 $0$인 것은 모든 $k$에 대하여 $x_km=0$인 것과 동치이다. $K_{n+1}(x;M)=0$이므로 원하는 결과를 얻는다.
:::

즉 $H_0$는 $x_i$들로 이루어진 quotient를, $H_n$은 $x_i$들 모두에 의해 annihilate되는 원소들을 계산하며, 그 사이의 homology들이 $x_i$들 사이의 관계에 대한 정보를 담는다. 이들을 본격적으로 다루기에 앞서, Koszul homology가 언제나 $(x)$에 의해 annihilate된다는 기본적인 사실을 확인한다.

::: 명제 3
각각의 $j$에 대하여, $K(x;M)$의 각 degree에서 곱하기 $x_j$로 주어지는 chain map은 null homotopic이다. ([\[호몰로지 대수학\] §긴 완전열, ⁋정의 5](/ko/math/homological_algebra/long_exact_sequence#def5)) 특히 모든 $i$에 대하여 $(x)H_i(x;M)=0$이다.
:::
::: 증명
각각의 $i$에 대하여 $\sigma_j: K_i(x;M) \rightarrow K_{i+1}(x;M)$을 $\xi\otimes m\mapsto (e_j\wedge \xi)\otimes m$으로 정의하자. 임의의 $\xi\in\bigwedge\nolimits^iF$에 대하여 Leibniz rule은

$$d(e_j\wedge \xi)=x_j\xi-e_j\wedge d\xi$$

를 주므로, $(d\sigma_j+\sigma_jd)(\xi\otimes m)=x_j(\xi\otimes m)$이다. 즉 $\sigma_j$는 곱하기 $x_j$와 $0$ 사이의 chain homotopy이다. 그럼 [\[호몰로지 대수학\] §긴 완전열, ⁋명제 6](/ko/math/homological_algebra/long_exact_sequence#prop6)에 의하여 곱하기 $x_j$가 각각의 $H_i(x;M)$ 위에 유도하는 map은 $0$이고, 따라서 $x_jH_i(x;M)=0$이다.
:::

따라서 각각의 $H_i(x;M)$은 $A/(x)$-module 구조를 가지며, 특히 만일 $(x)=A$라면 모든 $i$에 대하여 $H_i(x;M)=0$이다.

이 절을 마치기 전에 Koszul complex의 두드러진 구조적 성질 하나를 더 살펴본다. 각각의 $i$에 대하여 $K^i(x;M)=\Hom_A(\bigwedge\nolimits^iF, M)$으로 두면, $\delta^i=\Hom_A(d_{i+1},M):K^i(x;M) \rightarrow K^{i+1}(x;M)$은 $\delta^{i+1}\circ\delta^i=\Hom_A(d_{i+1}\circ d_{i+2},M)=0$을 만족하므로 index가 증가하는 방향의 complex를 얻고, 그 cohomology를 $H^i(x;M)=\ker\delta^i/\im\delta^{i-1}$로 적는다. 가령 $H^0(x;M)$은 $\Hom_A(A,M)\cong M$ 안에서 $\delta^0$의 kernel인데, $m\in M$에 대응되는 $\Hom_A(A,M)$의 원소에 $\delta^0$를 취하면 $e_i\mapsto x_im$이므로 $H^0(x;M)=\{m\in M\mid x_1m=\cdots=x_nm=0\}$이다. 이것이 [명제 2](#prop2)의 $H_n(x;M)$과 일치하는 것은 우연이 아니다.

::: 명제 4
임의의 $i$에 대하여 $H^i(x;M)\cong H_{n-i}(x;M)$이 성립한다.
:::
::: 증명
$\omega=e_1\wedge\cdots\wedge e_n$으로 두면 $\bigwedge\nolimits^nF=A\omega$이다. 각각의 $i$에 대하여 $A$-linear map $\theta_i:\bigwedge\nolimits^iF \rightarrow \Hom_A(\bigwedge\nolimits^{n-i}F,A)$를 다음의 식

$$\xi\wedge\eta=\theta_i(\xi)(\eta)\omega,\qquad \xi\in\bigwedge\nolimits^iF,\quad\eta\in \bigwedge\nolimits^{n-i}F$$

으로 정의하자. Basis의 수준에서 살펴보면, $i$개의 원소로 이루어진 $J\subseteq\{1,\ldots,n\}$과 $n-i$개의 원소로 이루어진 $J'$에 대하여 $e_J\wedge e_{J'}$는 $J'$가 $J$의 여집합이 아닐 때 $0$이고 여집합일 때 $\pm\omega$이므로, $\theta_i$는 basis $(e_J)$의 각 원소를 dual basis의 원소에 $\pm1$을 곱한 것으로 보낸다. 따라서 $\theta_i$는 isomorphism이다.

이제 $\xi\in \bigwedge\nolimits^iF$와 $\eta\in\bigwedge\nolimits^{n-i+1}F$에 대하여 $\xi\wedge\eta\in \bigwedge\nolimits^{n+1}F=0$이므로, Leibniz rule으로부터

$$0=d(\xi\wedge\eta)=d\xi\wedge\eta+(-1)^i\xi\wedge d\eta$$

이고, 이를 $\theta$로 옮겨 적으면 $\theta_{i-1}(d\xi)(\eta)=(-1)^{i+1}\theta_i(\xi)(d\eta)$, 곧 다음의 식

$$\theta_{i-1}\circ d_i=(-1)^{i+1}\Hom_A(d_{n-i+1},A)\circ\theta_i$$

를 얻는다. 그럼 $\theta_i'=(-1)^{i(i-1)/2}\theta_i$로 부호를 수정하면, 두 지수의 차가

$$\frac{(i-1)(i-2)}{2}+(i+1)-\frac{i(i-1)}{2}=2$$

이므로 $\theta_{i-1}'\circ d_i=\Hom_A(d_{n-i+1},A)\circ \theta_i'$이다. 즉 $D_i=\Hom_A(\bigwedge\nolimits^{n-i}F,A)$와 differential $\Hom_A(d_{n-i+1},A):D_i \rightarrow D_{i-1}$로 정의된 chain complex $D$에 대하여, $\theta'$는 chain complex들의 isomorphism $K(x) \rightarrow D$를 준다.

마지막으로 $M$을 계수로 넣자. Finite free module $N$에 대하여 canonical map $\Hom_A(N,A)\otimes_AM \rightarrow \Hom_A(N,M)$, $f\otimes m\mapsto (\xi\mapsto f(\xi)m)$은 $N=A$일 때 자명하게 isomorphism이고 finite direct sum과 compatible하므로 언제나 isomorphism이며, $N$에 대하여 functorial하다. 따라서 $D\otimes_AM$은 degree $i$에서 $\Hom_A(\bigwedge\nolimits^{n-i}F,M)=K^{n-i}(x;M)$이고 differential이 $\delta^{n-i}$인 complex와 identify된다. 그럼 $\theta'\otimes\id_M$은 isomorphism $K(x;M) \rightarrow D\otimes_AM$을 주므로

$$H_i(x;M)\cong H_i(D\otimes_AM)=\ker\delta^{n-i}/\im\delta^{n-i-1}=H^{n-i}(x;M)$$

이다.
:::

즉 Koszul complex는 degree를 뒤집은 자기 자신의 dual과 isomorphic하다. [명제 2](#prop2)와 종합하면 $H^n(x;M)\cong M/xM$이고, $H^0(x;M)$은 위에서 직접 계산한 것과 일치한다.

## 긴 완전열과 regular sequence

이제 [§정칙국소환, ⁋정의 2](/ko/math/commutative_algebra/regular_local_rings#def2)의 $A$-sequence를 module에 대한 것으로 일반화한다.

::: 정의 5
Ring $A$와 $A$-module $M$, 그리고 $A$의 원소들 $x_1,\ldots, x_n$이 주어졌다 하자. $x_1,\ldots, x_n$이 *$M$-regular sequence* 혹은 간단히 *$M$-sequence*라는 것은 $xM\neq M$이고, 각각의 $i=0,1,\ldots, n-1$에 대하여 곱하기 $x_{i+1}$이 $M/(x_1,\ldots,x_i)M$ 위에서 injective인 것이다.
:::

$i=0$의 조건은 곱하기 $x_1$이 $M$ 위에서 injective라는 것이고, $M=A$인 경우 이 정의는 [§정칙국소환, ⁋정의 2](/ko/math/commutative_algebra/regular_local_rings#def2)의 $A$-sequence와 일치한다. Ring의 경우와 마찬가지로 이 정의는 겉보기에 원소들의 순서에 민감하며, 실제로 순서를 바꾸면 $M$-sequence가 아니게 되는 예시를 [예시 11](#ex11)에서 살펴본다. 그럼에도 Noetherian local ring에서는 순서가 전혀 문제되지 않는다는 것이 이 글의 주된 결과이다.

이 결과로 가는 길은 Koszul complex의 귀납적 구조, 곧 마지막 원소를 떼어내면 나타나는 long exact sequence를 통한다.

::: 보조정리 6
$n\geq 2$라 하고 $x'=(x_1,\ldots,x_{n-1})$로 적자. 그럼 임의의 $A$-module $M$에 대하여 다음의 long exact sequence

$$\cdots \rightarrow H_i(x';M) \rightarrow H_i(x;M) \rightarrow H_{i-1}(x';M)\overset{\partial_i}{\longrightarrow} H_{i-1}(x';M) \rightarrow H_{i-1}(x;M) \rightarrow \cdots$$

이 존재하며, connecting homomorphism $\partial_i$는 곱하기 $(-1)^{i-1}x_n$으로 주어진다.
:::
::: 증명
$F'=\bigoplus_{i=1}^{n-1}Ae_i$로 두면 [\[다중선형대수학\] §텐서대수, ⁋명제 13](/ko/math/multilinear_algebra/tensor_algebras#prop13)의 basis 묘사로부터, 각각의 $i$에 대하여 basis $e_J$들을 $n\in J$인지에 따라 나누어 다음의 분해

$$\bigwedge\nolimits^iF=\bigwedge\nolimits^iF'\oplus\left(\bigwedge\nolimits^{i-1}F'\right)\wedge e_n$$

을 얻는다. $K(x')$의 differential을 $d'$로 적으면, differential의 명시적인 식에 의하여 $d$는 $\bigwedge F'$ 위에서 $d'$와 일치하고, $\alpha\in\bigwedge\nolimits^iF'$와 $\beta\in \bigwedge\nolimits^{i-1}F'$에 대하여 Leibniz rule으로부터

$$d(\alpha+\beta\wedge e_n)=d'\alpha+d'\beta\wedge e_n+(-1)^{i-1}x_n\beta=\left(d'\alpha+(-1)^{i-1}x_n\beta\right)+(d'\beta)\wedge e_n$$

이다. 이제 위의 분해에 $\otimes_AM$을 취하면 $K_i(x;M)=K_i(x';M)\oplus K_{i-1}(x';M)$이고, 위의 계산에 의하여 첫째 성분으로의 inclusion $K(x';M) \rightarrow K(x;M)$은 chain map이다. 또, chain complex $L$을 $L_i=K_{i-1}(x';M)$과 $K(x';M)$의 differential 그대로로 정의하면, 둘째 성분으로의 projection $K(x;M) \rightarrow L$ 또한 chain map이며, 정의에 의하여 $H_i(L)=H_{i-1}(x';M)$이다. 그럼 각 degree에서 위의 분해로 주어지는 short exact sequence

$$0 \rightarrow K(x';M) \rightarrow K(x;M) \rightarrow L \rightarrow 0$$

을 얻고, [\[호몰로지 대수학\] §긴 완전열, ⁋정리 1](/ko/math/homological_algebra/long_exact_sequence#thm1)이 원하는 꼴의 long exact sequence를 준다.

Connecting homomorphism을 계산하자. [\[호몰로지 대수학\] §Diagram chasing, ⁋정리 6](/ko/math/homological_algebra/diagram_chasing#thm6)의 증명에 의하면, $\partial_i$는 $L_i$의 cycle $\beta$를 $K_i(x;M)$의 원소 $(0,\beta)$로 lift하고 여기에 differential을 적용한 뒤, 그 결과를 첫째 성분 $K_{i-1}(x';M)$의 원소로 보는 것으로 계산된다. 그런데 위의 계산에 의하여 $d(0,\beta)=((-1)^{i-1}x_n\beta, d'\beta)=((-1)^{i-1}x_n\beta,0)$이므로 $\partial_i[\beta]=(-1)^{i-1}[x_n\beta]$이다.
:::

부호 $(-1)^{i-1}$은 이하의 모든 논증에서 아무런 역할도 하지 않는데, 곱하기 $x_n$과 곱하기 $-x_n$은 kernel과 image가 같기 때문이다. 이 long exact sequence의 첫 번째 응용으로 이 글의 절반에 해당하는 결과를 증명한다.

::: 정리 7
$A$-module $M$과 $M$-regular sequence $x_1,\ldots, x_n$에 대하여, 모든 $i\geq 1$에서 $H_i(x;M)=0$이다.
:::
::: 증명
$n$에 대한 귀납법을 사용한다. $n=1$인 경우 $K(x_1;M)$은 두 개의 $M$을 곱하기 $x_1$으로 이은 complex이므로, [명제 2](#prop2)에 의하여 $H_1(x_1;M)=\{m\in M\mid x_1m=0\}$이고, 곱하기 $x_1$이 $M$ 위에서 injective이므로 이는 $0$이다.

이제 $n\geq 2$라 하고 주장이 $n-1$에 대하여 성립한다고 가정하자. $x'=(x_1,\ldots,x_{n-1})$로 두면 $x'M\subseteq xM\neq M$이고 [정의 5](#def5)의 나머지 조건들은 $x$에 대한 조건들의 일부이므로, $x_1,\ldots,x_{n-1}$은 $M$-regular sequence이다. 따라서 귀납적 가정에 의하여 모든 $i\geq 1$에서 $H_i(x';M)=0$이다.

$i\geq 2$인 경우, [보조정리 6](#lem6)의 exact sequence

$$H_i(x';M) \rightarrow H_i(x;M) \rightarrow H_{i-1}(x';M)$$

에서 양 끝이 모두 $0$이므로 $H_i(x;M)=0$이다. $i=1$인 경우, 같은 보조정리로부터 다음의 exact sequence

$$0=H_1(x';M) \rightarrow H_1(x;M) \rightarrow H_0(x';M)\overset{\partial_1}{\longrightarrow}H_0(x';M)$$

을 얻는데, [명제 2](#prop2)에 의하여 $H_0(x';M)=M/x'M$이고 $\partial_1$은 곱하기 $x_n$이다. 그런데 $x_1,\ldots,x_n$이 $M$-regular sequence이므로 곱하기 $x_n$은 $M/x'M$ 위에서 injective이고, 따라서 $H_1(x;M)=0$이다.
:::

즉 canonical projection $M \rightarrow M/xM$을 augmentation으로 삼으면 다음의 complex

$$0 \rightarrow K_n(x;M) \rightarrow \cdots \rightarrow K_1(x;M) \rightarrow M \rightarrow M/xM \rightarrow 0$$

이 exact이다. $M=A$의 경우 이는 $K(x)$가 $A/(x)$의 free resolution이라는 뜻이고, 다음의 결과를 얻는다.

::: 따름정리 8
Ring $A$의 원소들 $x_1,\ldots,x_n$이 $A$-regular sequence라면 $K(x)$는 $A/(x)$의 free resolution이며, 임의의 $A$-module $N$에 대하여 다음의 isomorphism

$$\Tor_i^A(A/(x),N)\cong H_i(x;N),\qquad \Ext_A^i(A/(x),N)\cong H^i(x;N)$$

이 성립한다.
:::
::: 증명
[정리 7](#thm7)을 $M=A$에 적용하면 모든 $i\geq 1$에서 $H_i(K(x))=0$이고, [명제 2](#prop2)에 의하여 $H_0(K(x))=A/(x)$이므로 $K(x)$는 $A/(x)$의 left resolution이다. ([\[호몰로지 대수학\] §분해, ⁋정의 2](/ko/math/homological_algebra/resolutions#def2)) 각각의 $K_i$는 free이므로 자기 자신의 direct summand가 되어 projective이고 ([\[다중선형대수학\] §사영가군, 단사가군, 평탄가군, ⁋명제 4](/ko/math/multilinear_algebra/various_modules#prop4)), 따라서 $K(x)$는 $A/(x)$의 projective resolution이다. 그럼 [\[호몰로지 대수학\] §Ext와 Tor, ⁋정의 2](/ko/math/homological_algebra/ext_and_tor#def2)에 의하여

$$\Tor_i^A(A/(x),N)=H_i(K(x)\otimes_AN)=H_i(x;N)$$

이고, [\[호몰로지 대수학\] §Ext와 Tor, ⁋명제 3](/ko/math/homological_algebra/ext_and_tor#prop3)에 의하여 $\Ext$ 또한 첫째 변수의 projective resolution으로 계산할 수 있으므로

$$\Ext_A^i(A/(x),N)=H^i(\Hom_A(K(x),N))=H^i(x;N)$$

이다.
:::

이 따름정리는 [\[호몰로지 대수학\] §Ext와 Tor, ⁋정의 7](/ko/math/homological_algebra/ext_and_tor#def7) 직후에 살펴본 free resolution 논의를 다시 확인해준다. 한편 [명제 4](#prop4)의 duality와 종합하면, $A$-regular sequence $x$에 대하여 다음의 isomorphism

$$\Ext_A^i(A/(x),N)\cong\Tor_{n-i}^A(A/(x),N)$$

이 성립한다는 것도 알 수 있다.

## 국소환에서의 판정

이제 [정리 7](#thm7)의 역을 살펴본다. 일반적으로는 Koszul homology가 모두 소멸하더라도 주어진 순서의 원소들이 $M$-regular sequence가 아닐 수 있다. ([예시 11](#ex11)) 그러나 Noetherian local ring에서 원소들을 maximal ideal에서 뽑는다면 상황이 완전히 달라지는데, 이는 Nakayama lemma가 homology의 소멸을 한 단계씩 아래로 전파시켜 주기 때문이다.

::: 정리 9
Noetherian local ring $(A,\mathfrak{m})$과 $0$이 아닌 finitely generated $A$-module $M$, 그리고 원소들 $x_1,\ldots, x_n\in \mathfrak{m}$에 대하여 다음이 모두 동치이다.

1. $x_1,\ldots, x_n$은 $M$-regular sequence이다.
2. 모든 $i\geq 1$에 대하여 $H_i(x;M)=0$이다.
3. $H_1(x;M)=0$이다.
:::
::: 증명
첫째 조건이 둘째 조건을 함의한다는 것은 [정리 7](#thm7)이고, 둘째 조건이 셋째 조건을 함의하는 것은 자명하다. 셋째 조건이 첫째 조건을 함의한다는 것을 $n$에 대한 귀납법으로 보이자.

우선 다음의 관찰에서 시작한다. $x_i\in\mathfrak{m}$이므로 $xM\subseteq \mathfrak{m}M$인데, 만일 $xM=M$이라면 $\mathfrak{m}M=M$이고, $M$이 finitely generated이므로 [§정수적 확장, ⁋보조정리 8](/ko/math/commutative_algebra/integral_extension#lem8)에 의하여 $M=0$이 되어 모순이다. 따라서 $xM\neq M$은 언제나 성립한다.

$n=1$인 경우, [명제 2](#prop2)에 의하여 $H_1(x_1;M)=\{m\in M\mid x_1m=0\}=0$은 곱하기 $x_1$이 $M$ 위에서 injective라는 뜻이므로, 위의 관찰과 종합하면 $x_1$은 $M$-regular sequence이다.

이제 $n\geq 2$라 하고 주장이 $n-1$에 대하여 성립한다고 가정하자. $x'=(x_1,\ldots,x_{n-1})$로 두고 [보조정리 6](#lem6)의 exact sequence

$$H_1(x';M)\overset{\partial_2}{\longrightarrow}H_1(x';M) \rightarrow H_1(x;M)=0$$

을 생각하자. $\partial_2$는 곱하기 $-x_n$이므로 이 exact sequence는 $H_1(x';M)=x_nH_1(x';M)$을 말해준다. 한편 $A$가 Noetherian이고 $M$이 finitely generated이므로 $M$은 Noetherian module이고 ([§기본 개념들, ⁋따름정리 6](/ko/math/commutative_algebra/basic_notions#cor6)과 [§기본 개념들, ⁋명제 4](/ko/math/commutative_algebra/basic_notions#prop4)), 따라서 finite direct sum $K_i(x';M)\cong M^{\oplus\binom{n-1}{i}}$도 Noetherian이다. ([§기본 개념들, ⁋따름정리 6](/ko/math/commutative_algebra/basic_notions#cor6)) 특히 그 submodule의 quotient인 $H_1(x';M)$은 finitely generated이다. ([§기본 개념들, ⁋정리 3](/ko/math/commutative_algebra/basic_notions#thm3)과 [§기본 개념들, ⁋명제 4](/ko/math/commutative_algebra/basic_notions#prop4)) 그럼 $x_n\in\mathfrak{m}$이므로 [§정수적 확장, ⁋보조정리 8](/ko/math/commutative_algebra/integral_extension#lem8)에 의하여 $H_1(x';M)=0$이고, 귀납적 가정에 의하여 $x_1,\ldots,x_{n-1}$은 $M$-regular sequence이다.

마지막으로 [보조정리 6](#lem6)의 exact sequence

$$0=H_1(x;M) \rightarrow H_0(x';M)\overset{\partial_1}{\longrightarrow}H_0(x';M)$$

에서 $\partial_1$은 곱하기 $x_n$이므로, 곱하기 $x_n$은 $H_0(x';M)=M/x'M$ 위에서 injective이다. 이를 위의 관찰 $xM\neq M$과 종합하면 $x_1,\ldots,x_n$은 $M$-regular sequence이다.
:::

이 정리의 셋째 조건은 겉으로 보기에도 원소들의 순서에 의존하지 않는다. 이를 정확히 하면 다음을 얻는다.

::: 따름정리 10
Noetherian local ring $(A,\mathfrak{m})$과 $0$이 아닌 finitely generated $A$-module $M$에 대하여, $\mathfrak{m}$의 원소들로 이루어진 $M$-regular sequence $x_1,\ldots, x_n$이 주어졌다 하자. 그럼 임의의 permutation $\sigma$에 대하여 $x_{\sigma(1)},\ldots, x_{\sigma(n)}$ 또한 $M$-regular sequence이다.
:::
::: 증명
우선 ring과 module에 대한 아무런 가정 없이, 두 complex $K(x_{\sigma(1)},\ldots,x_{\sigma(n)};M)$과 $K(x_1,\ldots,x_n;M)$이 isomorphic하다는 것을 보인다. $A$-linear map $F \rightarrow \bigwedge F$, $e_i\mapsto e_{\sigma(i)}$는 image의 임의의 원소가 $\bigwedge F$에서 제곱하면 $0$이 되도록 하므로, [\[다중선형대수학\] §텐서대수, ⁋명제 11](/ko/math/multilinear_algebra/tensor_algebras#prop11)에 의하여 $A$-algebra homomorphism $\Psi:\bigwedge F \rightarrow \bigwedge F$로 확장된다. $\Psi$는 basis $e_J$들을 $\pm e_{\sigma(J)}$들로 보내므로 각각의 $\bigwedge\nolimits^iF$의 automorphism을 준다. 한편 $K(x_{\sigma(1)},\ldots,x_{\sigma(n)})$의 differential $d_\sigma$는 $d_\sigma(e_i)=x_{\sigma(i)}$로 결정되는데, 증가하는 순서가 아닌 index들에 대해서도 성립하는 differential의 명시적인 식에 의하여

$$\Psi(d_\sigma(e_{j_1}\wedge\cdots\wedge e_{j_i}))=\sum_{k=1}^i(-1)^{k-1}x_{\sigma(j_k)}e_{\sigma(j_1)}\wedge\cdots\wedge\widehat{e_{\sigma(j_k)}}\wedge\cdots\wedge e_{\sigma(j_i)}=d(\Psi(e_{j_1}\wedge\cdots\wedge e_{j_i}))$$

이므로 $\Psi$는 chain map이다. 따라서 $\Psi\otimes\id_M$은 두 Koszul complex 사이의 isomorphism이고, 특히 모든 $i$에 대하여 $H_i(x_{\sigma(1)},\ldots,x_{\sigma(n)};M)\cong H_i(x;M)$이다.

이제 주어진 상황으로 돌아오면, [정리 9](#thm9)에 의하여 $H_1(x;M)=0$이므로 $H_1(x_{\sigma(1)},\ldots,x_{\sigma(n)};M)=0$이고, $x_{\sigma(i)}\in\mathfrak{m}$이므로 다시 [정리 9](#thm9)에 의하여 $x_{\sigma(1)},\ldots,x_{\sigma(n)}$은 $M$-regular sequence이다.
:::

다음 예시는 local 가정이 없다면 이 모든 것이 실패한다는 것을 보여준다.

::: 예시 11
Field $\mathbb{K}$와 polynomial ring $A=\mathbb{K}[\x,\y,\z]$에서 다음의 세 원소

$$x_1=\x,\qquad x_2=\y(1-\x),\qquad x_3=\z(1-\x)$$

를 생각하자. 그럼 $x_1,x_2,x_3$은 $A$-regular sequence이다. 실제로 $A$는 integral domain이므로 곱하기 $\x$는 injective이고, $A/(x_1)\cong\mathbb{K}[\y,\z]$에서 $x_2$의 image는 $\y$이므로 곱하기 $x_2$는 injective이며, $\y=x_2+\x\y$로부터 $(x_1,x_2)=(\x,\y)$이므로 $A/(x_1,x_2)\cong \mathbb{K}[\z]$에서 $x_3$의 image는 $\z$가 되어 곱하기 $x_3$도 injective이다. 물론 $(x_1,x_2,x_3)\subseteq(\x,\y,\z)$는 proper ideal이다.

반면 순서를 바꾼 $x_2,x_3,x_1$은 $A$-regular sequence가 아니다. 다음의 식

$$x_3\y=\y\z(1-\x)=\z x_2\in (x_2)$$

에서, 곱하기 $x_3$이 $A/(x_2)$ 위에서 injective이려면 $\y\in(x_2)$여야 한다. 그런데 만일 $\y=hx_2=h\y(1-\x)$라면 $A$가 integral domain이므로 $1=h(1-\x)$인데, 양변에 $\x=1$을 대입하면 $1=0$이 되어 모순이다. 즉 $\y\not\in(x_2)$이고, 곱하기 $x_3$은 $A/(x_2)$ 위에서 injective가 아니다.

그런데 [따름정리 10](#cor10)의 증명의 앞부분은 ring에 대한 아무런 가정 없이 $H_i(x_2,x_3,x_1;A)\cong H_i(x_1,x_2,x_3;A)$를 주므로, [정리 7](#thm7)에 의하여 이들은 모든 $i\geq 1$에서 $0$이다. 즉 $x_2,x_3,x_1$은 Koszul homology가 모두 소멸함에도 $A$-regular sequence가 아니며, 따라서 [정리 9](#thm9)의 local 가정은 생략할 수 없다.

이 현상은 localization을 통해 이해할 수 있다. Maximal ideal $\mathfrak{m}=(\x,\y,\z)$에서의 localization $A_\mathfrak{m}$에서는 $1-\x$가 unit이므로 $x_2$와 $x_3$은 각각 $\y$와 $\z$의 unit배이고, 위의 첫째 문단과 같은 계산을 반복하면 $x_2,x_3,x_1$이 $A_\mathfrak{m}$-regular sequence라는 것을 알 수 있다. 즉 문제는 $1-\x$가 소멸하는 $\x=1$ 근방에서만 일어나며, $\mathfrak{m}$ 근방만을 보는 local ring은 이를 감지하지 않는다.
:::

## 정칙국소환에서의 계산

마지막으로 이 글의 도구들을 regular local ring에 적용한다. [§차원, ⁋정의 12](/ko/math/commutative_algebra/Krull_dimension#def12)에서 정의한 regular local ring의 regular system of parameters는 [§정칙국소환, ⁋따름정리 3](/ko/math/commutative_algebra/regular_local_rings#cor3)에 의하여 $A$-sequence이므로, [따름정리 8](#cor8)의 모든 결과를 적용할 수 있다.

::: 예시 12
$d$차원의 regular local Noetherian ring $(A,\mathfrak{m})$과 residue field $\kappa=A/\mathfrak{m}$, 그리고 regular system of parameters $x_1,\ldots,x_d$가 주어졌다 하자. [§정칙국소환, ⁋따름정리 3](/ko/math/commutative_algebra/regular_local_rings#cor3)에 의하여 $x=(x_1,\ldots,x_d)$는 $A$-sequence이고 $(x)=\mathfrak{m}$이므로, [따름정리 8](#cor8)에 의하여 $K(x)$는 $\kappa$의 free resolution이며 임의의 $A$-module $N$에 대하여 $\Tor_i^A(\kappa,N)=H_i(x;N)$이다.

특히 $N=\kappa$로 두자. Koszul complex의 differential에 $\otimes_A\kappa$를 취한 map의 각 성분은 differential의 명시적인 식에 의하여 $\pm x_j$의 $\kappa$에서의 image인데, $x_j\in\mathfrak{m}$이므로 이들은 모두 $0$이다. 즉 $K(x;\kappa)$의 differential은 전부 $0$이고, 따라서

$$\Tor_i^A(\kappa,\kappa)\cong K_i(x;\kappa)=\bigwedge\nolimits^iF\otimes_A\kappa\cong\bigwedge\nolimits^i_\kappa(F\otimes_A\kappa)$$

이다. 마지막 isomorphism은 [\[다중선형대수학\] §텐서대수, ⁋명제 14](/ko/math/multilinear_algebra/tensor_algebras#prop14)에 의한 것이다. 한편 $e_i\otimes1\mapsto x_i+\mathfrak{m}^2$으로 정의된 $\kappa$-linear map $F\otimes_A\kappa \rightarrow \mathfrak{m}/\mathfrak{m}^2$은 $x_i$들이 $\mathfrak{m}$을 생성하므로 surjective이고, [§매개계, ⁋명제 2](/ko/math/commutative_algebra/system_of_parameters#prop2)에 의하여 $\dim_\kappa(\mathfrak{m}/\mathfrak{m}^2)\geq d$이므로 $d$차원 $\kappa$-벡터공간에서 출발하는 이 surjection은 isomorphism이다. 종합하면 다음의 식

$$\Tor_i^A(\kappa,\kappa)\cong \bigwedge\nolimits^i_\kappa(\mathfrak{m}/\mathfrak{m}^2),\qquad \dim_\kappa\Tor_i^A(\kappa,\kappa)=\binom{d}{i}$$

을 얻는다. 이는 [\[호몰로지 대수학\] §Ext와 Tor, ⁋정의 7](/ko/math/homological_algebra/ext_and_tor#def7) 직후에 polynomial ring에 대하여 수행한 계산을 임의의 regular local ring으로 확장한 것이다. 특히 $\Tor_d^A(\kappa,\kappa)\cong\kappa\neq 0$이고, $i>d$에서는 $\Tor_i^A(\kappa,\kappa)=0$이다.
:::

이 소멸 구간이 정확히 $i=\dim A$에서 끝난다는 사실은 우연이 아니며, 이후 depth와 homological dimension을 다루는 글들에서 regular local ring의 homological 특징화로 이어진다.

---

**참고문헌**

**[Eis]** David Eisenbud. *Commutative Algebra: with a view toward algebraic geometry*. Springer, 1995.  
**[Mat]** Hideyuki Matsumura. *Commutative Ring Theory*. Cambridge University Press, 1986.

---
