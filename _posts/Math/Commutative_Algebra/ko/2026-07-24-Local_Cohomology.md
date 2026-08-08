---
title: "국소 코호몰로지"
description: "Torsion functor의 유도함자로 local cohomology를 정의하고 Čech complex로 계산하여, depth가 비소멸이 시작되는 차수이고 차원 위에서는 소멸하며 Cohen-Macaulay 가군에서는 한 차수에 집중된다는 것을 보인다."
excerpt: "Torsion functor의 유도함자와 Čech complex, depth와 차원에 의한 소멸"

categories: [Math / Commutative Algebra]
permalink: /ko/math/commutative_algebra/local_cohomology
sidebar: 
    nav: "commutative_algebra-ko"

date: 2026-07-24
weight: 33
published: false
drift_needed: true

---

이 시리즈에서 우리는 Noetherian local ring 위의 finitely generated module에 대하여 [§Depth](/ko/math/commutative_algebra/depth)에서 depth를, [§힐베르트-사무엘 함수](/ko/math/commutative_algebra/hilbert-samuel_function)에서 차원을, 그리고 [§단사가군과 Matlis 쌍대성](/ko/math/commutative_algebra/matlis_duality)에서 injective module의 구조론을 각각 세워 왔다. 이 글에서는 module에서 ideal의 거듭제곱에 의해 소멸되는 부분만을 도려내는 torsion functor를 도입하고, 그 right derived functor로 local cohomology를 정의한다. Injective module의 구조론은 이 derived functor를 유한한 localization들의 complex, 곧 Čech complex로 계산할 수 있게 해 주며, 그 결과 depth는 local cohomology가 처음으로 살아나는 차수로, 차원은 그 위로는 전부 소멸하는 상한으로 각각 나타난다. 특히 Cohen--Macaulay module의 local cohomology는 단 한 차수에 집중된다.

## Torsion functor와 국소 코호몰로지

이 글 전체에서 $A$는 Noetherian ring이고 $\mathfrak{a}\subseteq A$는 ideal이며, module에는 특별한 언급이 없는 한 유한성 조건을 가정하지 않는다. [§단사가군과 Matlis 쌍대성, ⁋보조정리 10](/ko/math/commutative_algebra/matlis_duality#lem10)에서 우리는 Noetherian local ring의 residue field의 injective hull $E(\kappa)$가 $\mathfrak{m}$의 거듭제곱들에 의해 소멸되는 원소들의 증가하는 합집합 $\bigcup_n(0:_E\mathfrak{m}^n)$과 일치한다는 것을 보았다. 임의의 module에서 이러한 부분을 모으는 조작은 functor를 이루며, 이 functor가 이 글의 출발점이다.

::: 정의 1
Ring $A$의 ideal $\mathfrak{a}$와 $A$-module $M$에 대하여, $M$의 *$\mathfrak{a}$-torsion* submodule을 다음의 식

$$\Gamma_\mathfrak{a}(M)=\{m\in M\mid \text{$\mathfrak{a}^nm=0$ for some $n\geq 1$}\}=\bigcup_{n\geq 1}(0:_M\mathfrak{a}^n)$$

으로 정의한다. 만일 $\Gamma_\mathfrak{a}(M)=M$이라면 $M$을 *$\mathfrak{a}$-torsion module*이라 부른다.
:::

우선 $\Gamma_\mathfrak{a}(M)$이 실제로 $M$의 submodule인 것을 확인하자. $\mathfrak{a}^nm=0$이고 $\mathfrak{a}^{n'}m'=0$이라면 $k=\max(n,n')$에 대하여 $\mathfrak{a}^k(m+m')=0$이고, 임의의 $a\in A$에 대하여 $\mathfrak{a}^n(am)=a(\mathfrak{a}^nm)=0$이기 때문이다. 또, 각각의 $n$에 대하여 $(0:_M\mathfrak{a}^n)$은 $\Hom_A(A/\mathfrak{a}^n,M)$과 자연스럽게 동일시된다. $A/\mathfrak{a}^n$에서 출발하는 homomorphism은 $1+\mathfrak{a}^n$의 image로 결정되고, 그 image로는 $\mathfrak{a}^n$에 의해 소멸되는 원소가 정확히 허용되기 때문이다. 이는 [§단사가군과 Matlis 쌍대성, ⁋보조정리 8](/ko/math/commutative_algebra/matlis_duality#lem8)에서 사용한 동일시와 같은 것이다.

$A$-linear map $f:M \rightarrow N$은 $\Gamma_\mathfrak{a}(M)$을 $\Gamma_\mathfrak{a}(N)$으로 보낸다. $\mathfrak{a}^nm=0$이면 $\mathfrak{a}^nf(m)=f(\mathfrak{a}^nm)=0$이기 때문이다. 따라서 $f$의 제한을 $\Gamma_\mathfrak{a}(f)$로 두면 $\Gamma_\mathfrak{a}$는 $\lMod{A}$에서 $\lMod{A}$로의 functor가 되며, 다음이 성립한다.

::: 명제 2
$\Gamma_\mathfrak{a}$는 left exact functor이다.
:::
::: 증명
$A$-module들의 exact sequence

$$0 \rightarrow M' \overset{u}{\longrightarrow} M \overset{v}{\longrightarrow} M''$$

이 주어졌다 하자. $\Gamma_\mathfrak{a}(u)$는 injective map $u$의 제한이므로 injective이다. 또 $v\circ u=0$으로부터 $\Gamma_\mathfrak{a}(v)\circ\Gamma_\mathfrak{a}(u)=0$이므로, exactness를 위해서는 $\ker\Gamma_\mathfrak{a}(v)\subseteq\im\Gamma_\mathfrak{a}(u)$만 보이면 된다. $m\in\Gamma_\mathfrak{a}(M)$이 $v(m)=0$을 만족한다면 원래 sequence의 exactness에 의하여 $m=u(m')$인 $m'\in M'$이 존재한다. $\mathfrak{a}^nm=0$이라 하면 $u(\mathfrak{a}^nm')=\mathfrak{a}^nm=0$이고 $u$가 injective이므로 $\mathfrak{a}^nm'=0$, 곧 $m'\in\Gamma_\mathfrak{a}(M')$이다.
:::

Category $\lMod{A}$는 enough injective를 가지므로 ([\[호몰로지 대수학\] §분해, ⁋명제 5](/ko/math/homological_algebra/resolutions#prop5)) 임의의 $A$-module은 injective resolution을 갖고 ([\[호몰로지 대수학\] §분해, ⁋명제 3](/ko/math/homological_algebra/resolutions#prop3)), 따라서 left exact functor $\Gamma_\mathfrak{a}$의 right derived functor가 정의된다.

::: 정의 3
$A$-module $M$에 대하여, $\Gamma_\mathfrak{a}$의 right derived functor의 값

$$H_\mathfrak{a}^i(M)=R^i\Gamma_\mathfrak{a}(M)$$

을 $M$의 $\mathfrak{a}$에서의 *local cohomology<sub>국소 코호몰로지</sub>* module이라 부른다. ([\[호몰로지 대수학\] §유도함자, ⁋정의 9](/ko/math/homological_algebra/derived_functors#def9))
:::

정의에 의하여 $H_\mathfrak{a}^i(M)$은 $M$의 injective resolution $0 \rightarrow M \rightarrow I^0 \rightarrow I^1 \rightarrow\cdots$에 $\Gamma_\mathfrak{a}$를 적용한 complex의 $i$번째 cohomology이다. $0$번째 값은 $\Gamma_\mathfrak{a}$ 자신이다. 실제로 $\Gamma_\mathfrak{a}$가 left exact이므로 exact sequence $0 \rightarrow M \rightarrow I^0 \rightarrow I^1$에 $\Gamma_\mathfrak{a}$를 적용한

$$0 \rightarrow \Gamma_\mathfrak{a}(M) \rightarrow \Gamma_\mathfrak{a}(I^0) \rightarrow \Gamma_\mathfrak{a}(I^1)$$

이 exact이고, 따라서 $H_\mathfrak{a}^0(M)=\ker(\Gamma_\mathfrak{a}(I^0) \rightarrow \Gamma_\mathfrak{a}(I^1))=\Gamma_\mathfrak{a}(M)$이다. 또, right derived functor들은 cohomological $\delta$-functor를 이루므로 임의의 short exact sequence $0 \rightarrow M' \rightarrow M \rightarrow M'' \rightarrow 0$마다 long exact sequence

$$0 \rightarrow \Gamma_\mathfrak{a}(M') \rightarrow \Gamma_\mathfrak{a}(M) \rightarrow \Gamma_\mathfrak{a}(M'') \rightarrow H_\mathfrak{a}^1(M') \rightarrow\cdots \rightarrow H_\mathfrak{a}^i(M') \rightarrow H_\mathfrak{a}^i(M) \rightarrow H_\mathfrak{a}^i(M'') \rightarrow H_\mathfrak{a}^{i+1}(M') \rightarrow\cdots$$

가 자연스럽게 존재한다. ([\[호몰로지 대수학\] §유도함자, ⁋정의 1](/ko/math/homological_algebra/derived_functors#def1)) 마지막으로 $E$가 injective module이라면 $0 \rightarrow E \rightarrow E \rightarrow 0 \rightarrow\cdots$이 $E$ 자신의 injective resolution이므로 $i\geq 1$에서 $H_\mathfrak{a}^i(E)=0$이다.

::: 명제 4
Noetherian ring $A$의 ideal $\mathfrak{a},\mathfrak{b}$와 $A$-module $M$에 대하여 다음이 성립한다.

1. $H_\mathfrak{a}^i(M)$의 임의의 원소는 $\mathfrak{a}$의 어떤 거듭제곱에 의해 소멸된다. 곧 $H_\mathfrak{a}^i(M)$은 $\mathfrak{a}$-torsion module이다.
2. 만일 $\sqrt{\mathfrak{a}}=\sqrt{\mathfrak{b}}$라면 $\Gamma_\mathfrak{a}=\Gamma_\mathfrak{b}$이고, 따라서 모든 $i$에서 $H_\mathfrak{a}^i=H_\mathfrak{b}^i$이다.
:::
::: 증명
첫째 결과를 보이자. $M$의 injective resolution $I^\bullet$을 고정하면 $H_\mathfrak{a}^i(M)$은 $\Gamma_\mathfrak{a}(I^i)$의 submodule을 그 submodule로 나눈 것이다. $\Gamma_\mathfrak{a}(I^i)$의 원소는 정의에 의하여 $\mathfrak{a}$의 어떤 거듭제곱에 의해 소멸되므로, cohomology class $[z]$는 $z$를 소멸시키는 $\mathfrak{a}^n$에 의해 소멸된다.

둘째 결과를 보이자. 우선 일반적으로 finitely generated ideal $\mathfrak{c}=(c_1,\ldots,c_t)$의 각 generator가 $c_j^{k_j}\in\mathfrak{d}$를 만족한다면, $K=(k_1-1)+\cdots+(k_t-1)+1$에 대하여 $\mathfrak{c}^K\subseteq\mathfrak{d}$이다. $\mathfrak{c}^K$는 generator들의 $K$차 monomial들로 생성되는데, 각 monomial에서는 적어도 하나의 $c_j$가 $k_j$번 이상 등장할 수밖에 없기 때문이다. 이제 $\sqrt{\mathfrak{a}}=\sqrt{\mathfrak{b}}$라 하자. $A$가 Noetherian이므로 $\mathfrak{b}$는 finitely generated이고 ([§기본 개념들, ⁋정리 3](/ko/math/commutative_algebra/basic_notions#thm3)), 각 generator는 $\sqrt{\mathfrak{b}}=\sqrt{\mathfrak{a}}$에 속하므로 radical의 정의에 의하여 ([§국소화의 성질들, ⁋따름정리 8](/ko/math/commutative_algebra/properties_of_localization#cor8)) 어떤 거듭제곱이 $\mathfrak{a}$에 속한다. 그럼 위의 관찰에 의하여 $\mathfrak{b}^K\subseteq\mathfrak{a}$인 $K$가 존재한다. 이제 $m\in\Gamma_\mathfrak{a}(M)$이 $\mathfrak{a}^nm=0$을 만족하면 $\mathfrak{b}^{Kn}\subseteq\mathfrak{a}^n$이므로 $m\in\Gamma_\mathfrak{b}(M)$이고, 같은 논증을 반대 방향으로 적용하면 반대 포함도 성립하여 $\Gamma_\mathfrak{a}(M)=\Gamma_\mathfrak{b}(M)$이다. 두 functor가 morphism 위에서도 (같은 submodule로의 제한으로) 일치하므로 $\Gamma_\mathfrak{a}=\Gamma_\mathfrak{b}$이고, derived functor도 일치한다.
:::

$\mathfrak{a}$-torsion module들은 기본적인 조작에 대해 닫혀 있다. $\mathfrak{a}$-torsion module의 submodule은 자명하게 $\mathfrak{a}$-torsion이고, quotient의 원소는 그 representative를 소멸시키는 $\mathfrak{a}$의 거듭제곱에 의해 소멸되므로 quotient도 $\mathfrak{a}$-torsion이다. 또 $\Gamma_\mathfrak{a}$는 direct sum과 교환한다. $\bigoplus_\lambda M_\lambda$의 원소는 유한히 많은 성분만을 가지므로, 모든 성분이 $\mathfrak{a}$-power torsion이라면 그 지수들의 최댓값이 원소 전체를 소멸시키기 때문이다. 이 관찰들은 다음 절에서 반복적으로 쓰인다.

## Injective module에서의 계산과 Čech complex

Derived functor의 정의는 injective resolution을 요구하므로 그 자체로는 계산 도구가 되지 못한다. 그러나 [§단사가군과 Matlis 쌍대성, ⁋정리 6](/ko/math/commutative_algebra/matlis_duality#thm6)의 구조정리는 Noetherian ring 위의 injective module을 prime ideal마다의 injective hull $E(A/\mathfrak{p})$들로 완전히 분해하므로, $\Gamma_\mathfrak{a}$의 injective module에서의 값은 각 $E(A/\mathfrak{p})$에서의 값으로 환원된다. 다음 보조정리가 그 값을 결정한다.

::: 보조정리 5
Noetherian ring $A$와 prime ideal $\mathfrak{p}$, 그리고 $E=E(A/\mathfrak{p})$에 대하여 다음이 성립한다.

1. $E$의 임의의 원소는 $\mathfrak{p}$의 어떤 거듭제곱에 의해 소멸된다.
2. $x\notin\mathfrak{p}$이면 곱하기 $x:E \rightarrow E$는 bijective이다.
3. $\mathfrak{a}\subseteq\mathfrak{p}$이면 $\Gamma_\mathfrak{a}(E)=E$이고, $\mathfrak{a}\not\subseteq\mathfrak{p}$이면 $\Gamma_\mathfrak{a}(E)=0$이다.
:::
::: 증명
첫째 결과를 보이자. $0\neq y\in E$라 하고 cyclic submodule $Ay$를 생각하면, $Ay$는 $0$이 아닌 finitely generated module이므로 [§동반소아이디얼, ⁋정리 7](/ko/math/commutative_algebra/associated_primes#thm7)에 의하여 $\Ass(Ay)\neq\emptyset$이고, [§동반소아이디얼, ⁋보조정리 5](/ko/math/commutative_algebra/associated_primes#lem5)와 [§단사가군과 Matlis 쌍대성, ⁋보조정리 5](/ko/math/commutative_algebra/matlis_duality#lem5)에 의하여 $\Ass(Ay)\subseteq\Ass E=\{\mathfrak{p}\}$이므로 $\Ass(Ay)=\{\mathfrak{p}\}$이다. [§동반소아이디얼, ⁋정리 7](/ko/math/commutative_algebra/associated_primes#thm7)의 첫째 결과에 의하여 $\mathfrak{p}\supseteq\ann(Ay)$이고, $\ann(Ay)$를 포함하는 prime ideal 중 minimal한 것들은 모두 $\Ass(Ay)=\{\mathfrak{p}\}$에 속한다. 한편 $\ann(Ay)$를 포함하는 임의의 prime ideal은 그에 포함되는 minimal한 것을 포함하므로 ([\[집합론\] §선택공리, ⁋정리 4](/ko/math/set_theory/axiom_of_choice#thm4)) 반드시 $\mathfrak{p}$를 포함하고, 따라서 [§국소화의 성질들, ⁋따름정리 8](/ko/math/commutative_algebra/properties_of_localization#cor8)에 의하여 $\sqrt{\ann(Ay)}=\mathfrak{p}$이다. $A$가 Noetherian이라 $\mathfrak{p}$는 finitely generated이고 각 generator의 어떤 거듭제곱이 $\ann(Ay)$에 속하므로, [명제 4](#prop4)의 증명에서 살펴본 논증에 의하여 $\mathfrak{p}^k\subseteq\ann(Ay)$인 $k$가 존재한다. 곧 $\mathfrak{p}^ky=0$이다.

둘째 결과를 보이자. 우선 injectivity를 본다. $K=(0:_Ex)$라 하면, $K\cap(A/\mathfrak{p})$의 $0$이 아닌 원소 $w$는 integral domain $A/\mathfrak{p}$에서 $0$이 아닌 원소 $x+\mathfrak{p}$와의 곱이 $0$이 되어 모순이므로 $K\cap(A/\mathfrak{p})=0$이고, $A/\mathfrak{p}\subseteq E$가 essential extension이므로 ([§단사가군과 Matlis 쌍대성, ⁋정의 1](/ko/math/commutative_algebra/matlis_duality#def1)) $K=0$이다. 이제 surjectivity를 본다. 곱하기 $x$가 injective이므로 $xE\cong E$는 injective module이고, identity $\id_{xE}$를 inclusion $xE\hookrightarrow E$를 따라 확장하면 $r:E \rightarrow xE$가 존재하여 $r$의 $xE$로의 제한이 identity가 된다. 그럼 임의의 $e\in E$가 $e=r(e)+(e-r(e))$로 분해되고 $xE\cap\ker r=0$이므로 $E=xE\oplus C$ ($C=\ker r$)이다. 만일 $C\neq 0$이라면 essential성에 의하여 $0\neq w\in C\cap(A/\mathfrak{p})$가 존재하는데, $xw$는 $C$의 원소이면서 $xE$의 원소이므로 $xw=0$이고, injectivity에 의하여 $w=0$이 되어 모순이다. 따라서 $C=0$이고 $xE=E$이다.

셋째 결과를 보이자. $\mathfrak{a}\subseteq\mathfrak{p}$라면 임의의 $y\in E$에 대하여 첫째 결과가 주는 $k$에 대해 $\mathfrak{a}^ky\subseteq\mathfrak{p}^ky=0$이므로 $\Gamma_\mathfrak{a}(E)=E$이다. $\mathfrak{a}\not\subseteq\mathfrak{p}$라면 $x\in\mathfrak{a}\setminus\mathfrak{p}$를 택할 수 있고, $y\in\Gamma_\mathfrak{a}(E)$가 $\mathfrak{a}^ny=0$을 만족한다면 특히 $x^ny=0$인데, 둘째 결과에 의하여 곱하기 $x^n$이 bijective이므로 $y=0$이다.
:::

이 보조정리와 구조정리를 결합하면 $\mathfrak{a}$-torsion module이 local cohomology의 관점에서 보이지 않는다는 것, 곧 $0$번째를 제외한 모든 차수에서 소멸한다는 것이 따라온다.

::: 보조정리 6
$\mathfrak{a}$-torsion module $T$에 대하여 $H_\mathfrak{a}^0(T)=T$이고, $i\geq 1$에서 $H_\mathfrak{a}^i(T)=0$이다.
:::
::: 증명
우선 임의의 $\mathfrak{a}$-torsion module $N$에 대하여 $\Gamma_\mathfrak{a}(E(N))$이 injective module임을 주장한다. 여기서 $E(N)$은 $N$의 injective hull이다. ([§단사가군과 Matlis 쌍대성, ⁋정리 3](/ko/math/commutative_algebra/matlis_duality#thm3)) 실제로 [§단사가군과 Matlis 쌍대성, ⁋정리 6](/ko/math/commutative_algebra/matlis_duality#thm6)에 의하여 $E(N)\cong\bigoplus_\lambda E(A/\mathfrak{p}_\lambda)$로 분해되고, $\Gamma_\mathfrak{a}$가 direct sum과 교환하므로 [보조정리 5](#lem5)의 셋째 결과에 의하여

$$\Gamma_\mathfrak{a}(E(N))\cong\bigoplus_{\mathfrak{a}\subseteq\mathfrak{p}_\lambda}E(A/\mathfrak{p}_\lambda)$$

이다. $A$가 Noetherian이므로 injective module들의 direct sum은 injective이고 ([§단사가군과 Matlis 쌍대성, ⁋명제 4](/ko/math/commutative_algebra/matlis_duality#prop4)), 주장을 얻는다. 또, $N$이 $\mathfrak{a}$-torsion이므로 $N\subseteq\Gamma_\mathfrak{a}(E(N))$이고, quotient $\Gamma_\mathfrak{a}(E(N))/N$은 $\mathfrak{a}$-torsion module의 quotient라 다시 $\mathfrak{a}$-torsion이다.

이제 $I^0=\Gamma_\mathfrak{a}(E(T))$, $C^1=I^0/T$로 두고, 귀납적으로 $I^j=\Gamma_\mathfrak{a}(E(C^j))$, $C^{j+1}=I^j/C^j$로 두자. 위의 주장에 의하여 각 $I^j$는 $\mathfrak{a}$-torsion인 injective module이고, [\[호몰로지 대수학\] §분해, ⁋명제 3](/ko/math/homological_algebra/resolutions#prop3)의 구성에서와 같이 이들을 이어 붙이면 injective resolution

$$0 \rightarrow T \rightarrow I^0 \rightarrow I^1 \rightarrow I^2 \rightarrow\cdots$$

을 얻는다. 각 항이 $\mathfrak{a}$-torsion이므로 $\Gamma_\mathfrak{a}(I^j)=I^j$이고, 따라서 $H_\mathfrak{a}^i(T)$는 complex $I^\bullet$ 자신의 cohomology이다. 그런데 resolution의 exactness에 의하여 이 complex는 $i\geq 1$에서 exact이고 $\ker(I^0 \rightarrow I^1)=T$이므로 원하는 결과를 얻는다.
:::

이 보조정리는 다음 절에서 유한 길이 module의 local cohomology를 처리하는 데 쓰인다. 이제 이 절의 주된 목표인 Čech complex를 도입한다. 앞으로 $S'\subseteq S\subseteq\{1,\ldots,r\}$와 원소들 $x_1,\ldots,x_r\in A$에 대하여 $x_S=\prod_{i\in S}x_i$로 적는다 (단 $x_\emptyset=1$). $x_{S'}$의 $A_{x_S}$에서의 image는 unit이므로 (그 역원은 $x_{S\setminus S'}/x_S$이다) [§국소화, ⁋명제 6](/ko/math/commutative_algebra/localization#prop6)에 의하여 canonical $A$-algebra homomorphism $\varepsilon_{S',S}:A_{x_{S'}} \rightarrow A_{x_S}$가 존재하며, 같은 명제의 유일성에 의하여 이 canonical map들은 서로 호환된다. 즉 $S''\subseteq S'\subseteq S$에 대하여 $\varepsilon_{S',S}\circ\varepsilon_{S'',S'}=\varepsilon_{S'',S}$이다.

::: 정의 7
원소들 $x=(x_1,\ldots,x_r)$에 대하여, *Čech complex<sub>체흐 복합체</sub>* $\check{C}(x)$를 다음의 $A$-module들

$$\check{C}(x)^j=\bigoplus_{\substack{S\subseteq\{1,\ldots,r\}\\ \lvert S\rvert=j}}A_{x_S}\qquad(0\leq j\leq r)$$

과 differential

$$d^j:\check{C}(x)^j \rightarrow \check{C}(x)^{j+1};\qquad (d^j\omega)_S=\sum_{i\in S}(-1)^{\sigma(i,S)}\varepsilon_{S\setminus\{i\},S}(\omega_{S\setminus\{i\}}),\qquad \sigma(i,S)=\lvert\{i'\in S\mid i'<i\}\rvert$$

로 이루어진 complex로 정의한다. 여기서 $A_{x_S}$는 multiplicative set $\{x_S^k\}_{k\geq 0}$에서의 localization이다. ([§국소화, ⁋정의 4](/ko/math/commutative_algebra/localization#def4)) 또, $A$-module $M$에 대하여 $\check{C}(x;M)=\check{C}(x)\otimes_AM$으로 정의한다.
:::

$d\circ d=0$을 확인하자. $\lvert S\rvert=j+2$인 성분에서 $(d^{j+1}d^j\omega)_S$는 $S$에서 두 원소 $i\neq i'$을 차례로 제거하는 항들의 합인데, canonical map들의 호환성에 의하여 각 항의 계수 map은 제거 순서에 무관하게 $\varepsilon_{S\setminus\{i,i'\},S}$이다. $i'<i$라 하면 $i$를 먼저 제거하는 항의 부호는 $\sigma(i,S)+\sigma(i',S\setminus\{i\})=\sigma(i,S)+\sigma(i',S)$이고 $i'$을 먼저 제거하는 항의 부호는 $\sigma(i',S)+\sigma(i,S\setminus\{i'\})=\sigma(i',S)+\sigma(i,S)-1$이므로, 두 항은 서로 소거된다. 가장 작은 두 경우를 명시적으로 적으면 $r=1$일 때

$$0 \rightarrow A \rightarrow A_{x_1} \rightarrow 0$$

이고, $r=2$일 때

$$0 \rightarrow A \rightarrow A_{x_1}\oplus A_{x_2} \rightarrow A_{x_1x_2} \rightarrow 0$$

이며, 첫 map은 $a\mapsto(a/1,a/1)$, 둘째 map은 $(\omega_1,\omega_2)\mapsto\varepsilon(\omega_2)-\varepsilon(\omega_1)$이다. 한편 $\check{C}(x;M)$의 성분은 [§국소화의 성질들, ⁋보조정리 1](/ko/math/commutative_algebra/properties_of_localization#lem1)에 의하여 $A_{x_S}\otimes_AM\cong M_{x_S}$이므로, $\check{C}(x;M)$은 $M$의 localization들 사이의 canonical map들로 이루어진 complex이다.

다음 정리가 이 글의 계산적 기초이다.

::: 정리 8 (Čech 표현)
Noetherian ring $A$와 $\mathfrak{a}=(x_1,\ldots,x_r)$, 그리고 임의의 $A$-module $M$에 대하여, $M$에 대해 자연스러운 isomorphism

$$H_\mathfrak{a}^i(M)\cong H^i(\check{C}(x;M))$$

이 모든 $i$에서 존재한다.
:::
::: 증명
증명은 세 단계로 이루어진다.

**($H^0$의 동일시)** 임의의 $M$에 대하여 $H^0(\check{C}(x;M))=\ker(M \rightarrow \bigoplus_iM_{x_i})$이다. $M_{x_i}$에서 $m/1=0$인 것은 적당한 $n_i$에 대하여 $x_i^{n_i}m=0$인 것과 동치이므로 ([§국소화, ⁋명제 5](/ko/math/commutative_algebra/localization#prop5)), 이 kernel은 모든 $i$에서 $x_i$의 어떤 거듭제곱에 의해 소멸되는 원소들의 모임이다. $\mathfrak{a}^nm=0$이면 $x_i^nm=0$이 각 $i$에서 성립하고, 거꾸로 $x_i^{n_i}m=0$이 모든 $i$에서 성립하면 $n=\max_in_i$와 $N=r(n-1)+1$에 대하여 $\mathfrak{a}^N$을 생성하는 $N$차 monomial들 각각이 어떤 $x_i$를 $n$번 이상 포함하므로 $\mathfrak{a}^Nm=0$이다. 따라서 $H^0(\check{C}(x;M))=\Gamma_\mathfrak{a}(M)=H_\mathfrak{a}^0(M)$이고, 이 동일시는 $M$에 대해 자연스럽다.

**(Injective module의 경우)** $E$가 injective module일 때 $i\geq 1$에서 $H^i(\check{C}(x;E))=0$임을 보인다. [§단사가군과 Matlis 쌍대성, ⁋정리 6](/ko/math/commutative_algebra/matlis_duality#thm6)에 의하여 $E\cong\bigoplus_\lambda E(A/\mathfrak{p}_\lambda)$이다. Localization은 direct sum과 교환하고 (원소가 유한히 많은 성분만 가지며, $t(x_S^{k'}m-x_S^km')=0$ 꼴의 조건이 성분별로 검사되기 때문이다) canonical map들도 성분별로 작동하므로, complex $\check{C}(x;E)$는 $\check{C}(x;E(A/\mathfrak{p}_\lambda))$들의 direct sum이고 cohomology도 성분별로 계산된다. 따라서 $E=E(A/\mathfrak{p})$인 경우로 환원된다.

$T=\{i\mid x_i\notin\mathfrak{p}\}$로 두자. $S\subseteq T$이면 [보조정리 5](#lem5)의 둘째 결과에 의하여 곱하기 $x_S$가 $E$ 위에서 bijective이므로 canonical map $\iota_S:E \rightarrow E_{x_S}$는 isomorphism이다. 실제로 [§국소화, ⁋명제 5](/ko/math/commutative_algebra/localization#prop5)에 의하여 $\ker\iota_S$는 $x_S$의 거듭제곱에 의해 소멸되는 원소들이므로 $0$이고, 임의의 $y/x_S^k$에 대하여 $x_S^kz=y$인 유일한 $z\in E$를 취하면 $y/x_S^k=z/1$이다. 반면 $S\not\subseteq T$이면 어떤 $i\in S$에 대하여 $x_i\in\mathfrak{p}$이고, [보조정리 5](#lem5)의 첫째 결과에 의하여 임의의 $y\in E$가 $\mathfrak{p}^k y=0$인 $k$를 가지므로 $x_S^ky=0$이 되어 $E_{x_S}=0$이다.

만일 $T=\emptyset$이라면 $\check{C}(x;E)$는 degree $0$의 $E$ 하나로 이루어지므로 상위 cohomology가 모두 $0$이다. 이제 $T\neq\emptyset$이라 하자. Isomorphism $\iota_S$들로 $S\subseteq T$인 성분들을 $E$와 identify하면, canonical map들이 $\iota$들과 호환되므로 differential의 성분 map들은 $\pm\id_E$가 되고, $\check{C}(x;E)$는 다음의 complex

$$D^j=\bigoplus_{\substack{S\subseteq T\\ \lvert S\rvert=j}}E,\qquad (\dd{\omega})_S=\sum_{i\in S}(-1)^{\sigma(i,S)}\omega_{S\setminus\{i\}}$$

와 isomorphic하다. 가령 $r=2$이고 $T=\{1,2\}$라면 이는 $0 \rightarrow E \rightarrow E\oplus E \rightarrow E \rightarrow 0$, $e\mapsto(e,e)$, $(\omega_1,\omega_2)\mapsto\omega_2-\omega_1$이고, $s(\omega_1,\omega_2)=\omega_1$과 $s(\eta)=(0,\eta)$로 두면 $\dd{s}+sd=\id$가 직접 확인된다. 일반적으로 $l\in T$를 고정하고 $h:D^{j+1} \rightarrow D^j$를 다음 식

$$(h\omega)_S=\begin{cases}0&\text{if $l\in S$}\\(-1)^{\sigma(l,S\cup\{l\})}\omega_{S\cup\{l\}}&\text{if $l\notin S$}\end{cases}$$

으로 정의하자. $l\in S$인 성분에서는 $(h\dd{\omega})_S=0$이고, $(\dd{h}\omega)_S$에서 $(h\omega)_{S\setminus\{i\}}$는 $i=l$인 항에서만 살아남으므로

$$(\dd{h}\omega)_S=(-1)^{\sigma(l,S)}(h\omega)_{S\setminus\{l\}}=(-1)^{2\sigma(l,S)}\omega_S=\omega_S$$

이다. $l\notin S$인 성분에서는

$$(\dd{h}\omega)_S=\sum_{i\in S}(-1)^{\sigma(i,S)+\sigma(l,(S\setminus\{i\})\cup\{l\})}\omega_{(S\setminus\{i\})\cup\{l\}},\qquad (h\dd{\omega})_S=\omega_S+\sum_{i\in S}(-1)^{\sigma(l,S\cup\{l\})+\sigma(i,S\cup\{l\})}\omega_{(S\setminus\{i\})\cup\{l\}}$$

인데, $i<l$이면 $\sigma(i,S\cup\{l\})=\sigma(i,S)$이고 $\sigma(l,(S\setminus\{i\})\cup\{l\})=\sigma(l,S\cup\{l\})-1$이며, $i>l$이면 $\sigma(i,S\cup\{l\})=\sigma(i,S)+1$이고 $\sigma(l,(S\setminus\{i\})\cup\{l\})=\sigma(l,S\cup\{l\})$이므로, 어느 경우에도 두 합의 대응되는 항들의 부호가 반대가 되어 소거되고 $(\dd{h}\omega)_S+(h\dd{\omega})_S=\omega_S$이다. 따라서 $\id$는 $0$과 homotopic하고 ([\[호몰로지 대수학\] §긴 완전열, ⁋정의 5](/ko/math/homological_algebra/long_exact_sequence#def5)), homotopic한 chain map들은 cohomology 위에서 같은 map을 유도하므로 ([\[호몰로지 대수학\] §긴 완전열, ⁋명제 6](/ko/math/homological_algebra/long_exact_sequence#prop6)) 모든 $i$에서 $H^i(D^\bullet)=0$이다. 특히 $T\neq\emptyset$일 때에는 $H^0(\check{C}(x;E))=0$인데, 이 경우 어떤 $x_l\notin\mathfrak{p}$이 $\mathfrak{a}$에 속해 $\mathfrak{a}\not\subseteq\mathfrak{p}$이므로 이는 [보조정리 5](#lem5)의 셋째 결과 $\Gamma_\mathfrak{a}(E)=0$과 정합적이다.

**(일반적인 경우)** 모든 $A$-module $M$에 대한 자연 동형 $H_\mathfrak{a}^i(M)\cong H^i(\check{C}(x;M))$을 $i$에 대한 귀납법으로 보인다. $i=0$은 첫째 단계에서 이미 보였다. $M$이 주어지면 [\[호몰로지 대수학\] §분해, ⁋명제 5](/ko/math/homological_algebra/resolutions#prop5)에 의하여 short exact sequence

$$0 \rightarrow M \rightarrow E \rightarrow M' \rightarrow 0\qquad\text{($E$ injective)}$$

를 택할 수 있다. Derived functor 쪽에서는 이 sequence가 long exact sequence를 주고, $i\geq 1$에서 $H_\mathfrak{a}^i(E)=0$이다. Čech 쪽에서는 각 $\check{C}(x)^j$가 localization들의 유한 direct sum이고 localization은 flat $A$-module이므로 ([§국소화의 성질들, ⁋명제 2](/ko/math/commutative_algebra/properties_of_localization#prop2)) 항별 tensor가 injectivity를 성분별로 보존하여 complex들의 short exact sequence

$$0 \rightarrow \check{C}(x;M) \rightarrow \check{C}(x;E) \rightarrow \check{C}(x;M') \rightarrow 0$$

을 얻고, 여기에 [\[호몰로지 대수학\] §긴 완전열, ⁋정리 1](/ko/math/homological_algebra/long_exact_sequence#thm1)을 적용하면 (cochain complex는 $C_{-n}=C^n$의 재배열로 같은 정리가 적용된다) cohomology의 long exact sequence를 얻으며, 둘째 단계에 의하여 $i\geq 1$에서 $H^i(\check{C}(x;E))=0$이다. 그럼 두 long exact sequence 모두에서 $H^1(M)$은 $\Gamma_\mathfrak{a}(E) \rightarrow \Gamma_\mathfrak{a}(M')$의 cokernel과 동일시되고, 첫째 단계의 $H^0$ 동일시가 자연스러우므로 두 cokernel이 일치하여 $H_\mathfrak{a}^1(M)\cong H^1(\check{C}(x;M))$이다. 또 $i\geq 1$에서는 양쪽 long exact sequence의 이웃 항들이 소멸하여

$$H_\mathfrak{a}^{i+1}(M)\cong H_\mathfrak{a}^i(M'),\qquad H^{i+1}(\check{C}(x;M))\cong H^i(\check{C}(x;M'))$$

이므로, $M'$에 귀납적 가정을 적용하면 $H_\mathfrak{a}^{i+1}(M)\cong H^{i+1}(\check{C}(x;M))$을 얻는다. Naturality는 각 단계에서 유지된다. Module homomorphism이 주어지면 선택한 embedding들이 [\[호몰로지 대수학\] §분해, ⁋정리 6](/ko/math/homological_algebra/resolutions#thm6)에 의하여 호환되는 map으로 확장되고, 양쪽의 long exact sequence가 모두 이 확장에 대해 natural하기 때문이다.
:::

[정리 8](#thm8)의 좌변은 ideal $\mathfrak{a}$만으로 결정되는 반면 우변은 generator들의 선택 $x_1,\ldots,x_r$을 통해 표현되어 있으므로, 두 서술의 일치는 곧 $H^i(\check{C}(x;M))$이 $\mathfrak{a}$의 generator 선택에 무관하다는 사실을 담고 있다. 이는 [§Depth, ⁋정리 5](/ko/math/commutative_algebra/depth#thm5)에서 Koszul homology의 최고 비소멸 차수가 generator 선택에 무관했던 것과 같은 종류의 현상이다. 나아가 [명제 4](#prop4)의 둘째 결과와 종합하면 $\check{C}(x;M)$의 cohomology는 $\mathfrak{a}$의 radical에만 의존한다.

Čech complex는 degree $r$에서 끝나므로, 이 정리는 즉시 다음의 소멸을 준다.

::: 따름정리 9
Noetherian ring $A$와 $r$개의 원소로 생성되는 ideal $\mathfrak{a}=(x_1,\ldots,x_r)$, 그리고 임의의 $A$-module $M$에 대하여 $i>r$에서 $H_\mathfrak{a}^i(M)=0$이다. 특히 Noetherian local ring $(A,\mathfrak{m})$과 임의의 $A$-module $M$에 대하여 $i>\dim A$에서 $H_\mathfrak{m}^i(M)=0$이다.
:::
::: 증명
첫째 주장은 [정리 8](#thm8)과 $j>r$에서 $\check{C}(x)^j=0$인 것으로부터 자명하다. 둘째 주장의 경우, $d=\dim A$로 두면 [§매개계, ⁋따름정리 1](/ko/math/commutative_algebra/system_of_parameters#cor1)에 의하여 $d$개의 원소 $y_1,\ldots,y_d\in\mathfrak{m}$이 존재하여 충분히 큰 $n$에서 $\mathfrak{m}^n\subseteq\mathfrak{q}=(y_1,\ldots,y_d)$이도록 할 수 있고, 이는 [§매개계, ⁋명제–정의 3](/ko/math/commutative_algebra/system_of_parameters#prop-def3)의 셋째 조건이므로 $\mathfrak{q}$는 parameter ideal이며 같은 명제의 둘째 조건에 의하여 $\sqrt{\mathfrak{q}}=\mathfrak{m}$이다. 그럼 [명제 4](#prop4)의 둘째 결과에 의하여 $H_\mathfrak{m}^i=H_\mathfrak{q}^i$이고, $\mathfrak{q}$가 $d$개의 원소로 생성되므로 첫째 주장에 의하여 $i>d$에서 $H_\mathfrak{m}^i(M)=H_\mathfrak{q}^i(M)=0$이다.
:::

이 따름정리의 둘째 소멸 상한 $\dim A$는 다음 절에서 finitely generated module $M$에 대하여 $\dim M$으로 개선된다.

## Depth 특성화와 소멸정리

이제 이 글의 주된 결과들을 증명한다. 첫째는 depth가 local cohomology의 비소멸이 시작되는 정확한 차수라는 것이다. 아래에서 $\operatorname{depth}_\mathfrak{a}(M)$은 $\mathfrak{a}$ 안의 maximal $M$-sequence의 공통의 길이이다. ([§Depth, ⁋정의 3](/ko/math/commutative_algebra/depth#def3))

::: 정리 10
Noetherian local ring $(A,\mathfrak{m})$과 $0$이 아닌 finitely generated $A$-module $M$, 그리고 $\mathfrak{a}M\neq M$을 만족하는 ideal $\mathfrak{a}$에 대하여

$$\operatorname{depth}_\mathfrak{a}(M)=\min\{i\mid H_\mathfrak{a}^i(M)\neq 0\}$$

이 성립한다.
:::
::: 증명
$t=\operatorname{depth}_\mathfrak{a}(M)$에 대한 귀납법으로 증명한다.

$t=0$인 경우, [§Depth, ⁋따름정리 4](/ko/math/commutative_algebra/depth#cor4)의 첫째 결과에 의하여 $\mathfrak{a}\subseteq\mathfrak{p}$인 $\mathfrak{p}\in\Ass M$이 존재한다. $\mathfrak{p}=\ann(y)$인 $0\neq y\in M$을 택하면 ([§동반소아이디얼, ⁋정의 1](/ko/math/commutative_algebra/associated_primes#def1)) $\mathfrak{a}y\subseteq\mathfrak{p}y=0$이므로 $y\in\Gamma_\mathfrak{a}(M)$이고, 따라서 $H_\mathfrak{a}^0(M)=\Gamma_\mathfrak{a}(M)\neq 0$이 되어 좌우변이 모두 $0$이다.

이제 $t\geq 1$이라 하고 주장이 $t-1$에 대하여 성립한다고 가정하자. $\mathfrak{a}$ 안의 maximal $M$-sequence의 첫 원소를 $x$라 하면 $x\in\mathfrak{a}$는 $M$-regular이다.

우선 $\Gamma_\mathfrak{a}(M)=0$이다. $m\in\Gamma_\mathfrak{a}(M)$이 $\mathfrak{a}^nm=0$을 만족한다면 $x^n\in\mathfrak{a}^n$이므로 $x^nm=0$인데, $x$가 $M$-regular라 곱하기 $x^n$이 injective이므로 $m=0$이기 때문이다.

다음으로 $M/xM$을 살펴보자. $x\in\mathfrak{a}$이므로 $xM\subseteq\mathfrak{a}M\neq M$이 되어 $M/xM\neq 0$이고, $\mathfrak{a}(M/xM)=\mathfrak{a}M/xM\neq M/xM$이다. [§Depth, ⁋따름정리 4](/ko/math/commutative_algebra/depth#cor4)의 둘째 결과에 의하여 $\operatorname{depth}_\mathfrak{a}(M/xM)=t-1$이므로, 귀납적 가정에 의하여

$$H_\mathfrak{a}^i(M/xM)=0\quad(i<t-1),\qquad H_\mathfrak{a}^{t-1}(M/xM)\neq 0$$

이다. 이제 곱하기 $x$가 $M$ 위에서 injective인 것으로부터 short exact sequence

$$0 \rightarrow M \overset{x}{\longrightarrow} M \rightarrow M/xM \rightarrow 0$$

과 그 long exact sequence를 얻고, 두 $H_\mathfrak{a}^i(M)$ 사이의 map은 함자성에 의하여 스칼라 곱 $x$이다.

$i<t$에서 $H_\mathfrak{a}^i(M)=0$임을 보이자. $i=0$은 위에서 보였다. $1\leq i<t$라면 long exact sequence의 조각

$$H_\mathfrak{a}^{i-1}(M/xM) \rightarrow H_\mathfrak{a}^i(M) \overset{x}{\longrightarrow} H_\mathfrak{a}^i(M)$$

에서 $i-1<t-1$이므로 왼쪽 항이 $0$이고, 따라서 곱하기 $x$는 $H_\mathfrak{a}^i(M)$ 위에서 injective이다. 그런데 [명제 4](#prop4)의 첫째 결과에 의하여 임의의 $h\in H_\mathfrak{a}^i(M)$는 $\mathfrak{a}^nh=0$인 $n$을 가지므로, $x\in\mathfrak{a}$로부터 $x^nh=0$이다. 그럼 $x(x^{n-1}h)=0$에서 injectivity로 $x^{n-1}h=0$이고, 이를 반복하면 $h=0$이다. 따라서 $H_\mathfrak{a}^i(M)=0$이다.

마지막으로 $H_\mathfrak{a}^t(M)\neq 0$을 보이자. Long exact sequence의 조각

$$H_\mathfrak{a}^{t-1}(M) \rightarrow H_\mathfrak{a}^{t-1}(M/xM) \rightarrow H_\mathfrak{a}^t(M)$$

에서 $t-1<t$이므로 방금 보인 것에 의하여 왼쪽 항이 $0$이고, 따라서 $0\neq H_\mathfrak{a}^{t-1}(M/xM)$이 $H_\mathfrak{a}^t(M)$에 embed되어 $H_\mathfrak{a}^t(M)\neq 0$이다.
:::

특별히 $\mathfrak{a}=\mathfrak{m}$인 경우가 가장 중요하다.

::: 따름정리 11
Noetherian local ring $(A,\mathfrak{m})$과 $0$이 아닌 finitely generated $A$-module $M$에 대하여

$$\operatorname{depth}M=\min\{i\mid H_\mathfrak{m}^i(M)\neq 0\}$$

이 성립한다.
:::
::: 증명
$M\neq 0$이므로 [§정수적 확장, ⁋보조정리 8](/ko/math/commutative_algebra/integral_extension#lem8)에 의하여 $\mathfrak{m}M\neq M$이고, [정리 10](#thm10)을 $\mathfrak{a}=\mathfrak{m}$에 적용하면 된다.
:::

이로써 depth는 $H_\mathfrak{m}^\bullet(M)$이 처음으로 살아나는 자리를 짚는다. 반대쪽 끝은 차원이 통제한다. [따름정리 9](#cor9)는 이미 $\dim A$ 위에서의 소멸을 주었지만, module 자신의 차원까지 상한을 내리는 것이 Grothendieck의 소멸정리이다.

::: 정리 12 (Grothendieck)
Noetherian local ring $(A,\mathfrak{m})$과 $0$이 아닌 finitely generated $A$-module $M$에 대하여, $i>\dim M$이면 $H_\mathfrak{m}^i(M)=0$이다.
:::
::: 증명
$d=\dim M$에 대한 귀납법으로 증명한다.

$d=0$인 경우, $\ann(M)$을 포함하는 임의의 prime ideal은 $\dim A/\ann(M)=0$으로부터 maximal일 수밖에 없으므로 [§조르단-횔더 정리, ⁋따름정리 6](/ko/math/commutative_algebra/Jordan-Holder_theorem#cor6)에 의하여 $M$은 유한한 길이를 갖고, 같은 따름정리의 둘째 조건에 의하여 maximal ideal들의 어떤 곱이 $M$을 소멸시킨다. Local ring에서 maximal ideal은 $\mathfrak{m}$ 하나뿐이므로 $\mathfrak{m}^kM=0$인 $k$가 존재하고, 곧 $M$은 $\mathfrak{m}$-torsion module이다. 그럼 [보조정리 6](#lem6)에 의하여 $i\geq 1>0=d$에서 $H_\mathfrak{m}^i(M)=0$이다.

이제 $d\geq 1$이라 하고, 차원이 $d$ 미만인 $0$이 아닌 finitely generated module들에 대하여 주장이 성립한다고 가정하자.

먼저 $N=\Gamma_\mathfrak{m}(M)$을 처리한다. $M$은 Noetherian module이므로 ([§기본 개념들, ⁋따름정리 6](/ko/math/commutative_algebra/basic_notions#cor6)과 [§기본 개념들, ⁋명제 4](/ko/math/commutative_algebra/basic_notions#prop4)) $N$은 finitely generated이고, 각 generator가 $\mathfrak{m}$의 어떤 거듭제곱에 의해 소멸되므로 $\mathfrak{m}^kN=0$인 $k$가 존재한다. $N$은 $\mathfrak{m}$-torsion이므로 [보조정리 6](#lem6)에 의하여 $i\geq 1$에서 $H_\mathfrak{m}^i(N)=0$이고, short exact sequence $0 \rightarrow N \rightarrow M \rightarrow M/N \rightarrow 0$의 long exact sequence로부터 $i\geq 1$에서

$$H_\mathfrak{m}^i(M)\cong H_\mathfrak{m}^i(M/N)$$

이다. 만일 $M/N=0$이라면 $M=N$이 $\mathfrak{m}$-torsion이 되어 $i\geq 1$에서 $H_\mathfrak{m}^i(M)=0$이므로 증명이 끝난다. 이제 $M/N\neq 0$이라 하자. $\Gamma_\mathfrak{m}(M/N)=0$인데, $\mathfrak{m}^n\overline{y}=0$이라면 $\mathfrak{m}^ny\subseteq N$이므로 $\mathfrak{m}^{n+k}y=0$이 되어 $y\in N$이기 때문이다. 또 $\ann(M/N)\supseteq\ann(M)$이므로 $\dim(M/N)\leq\dim M=d$이다. ([§차원, ⁋정의 2](/ko/math/commutative_algebra/Krull_dimension#def2)) 만일 $\dim(M/N)<d$라면 귀납적 가정에 의하여 $i>\dim(M/N)$에서, 특히 $i>d$에서 $H_\mathfrak{m}^i(M/N)=0$이므로 증명이 끝난다. 그러므로 $M$을 $M/N$으로 교체하여, 처음부터 $\Gamma_\mathfrak{m}(M)=0$이고 $\dim M=d$라 가정할 수 있다.

이제 $M$-regular 원소를 찾는다. $M\neq 0$이므로 $\Ass M\neq\emptyset$이고 유한하다. ([§동반소아이디얼, ⁋정리 7](/ko/math/commutative_algebra/associated_primes#thm7)) 만일 $\mathfrak{m}$의 모든 원소가 $M$의 zerodivisor라면 같은 정리의 둘째 결과에 의하여 $\mathfrak{m}\subseteq\bigcup_{\mathfrak{p}\in\Ass M}\mathfrak{p}$이고, [§동반소아이디얼, ⁋보조정리 2](/ko/math/commutative_algebra/associated_primes#lem2)에 의하여 $\mathfrak{m}\subseteq\mathfrak{p}$인 $\mathfrak{p}\in\Ass M$이 존재하여 $\mathfrak{m}=\mathfrak{p}\in\Ass M$이다. 그럼 $\ann(y)=\mathfrak{m}$인 $0\neq y\in M$이 $\Gamma_\mathfrak{m}(M)=0$의 원소가 되어 모순이므로, $M$-regular인 $x\in\mathfrak{m}$이 존재한다.

[§Depth, ⁋명제 9](/ko/math/commutative_algebra/depth#prop9)에 의하여 $M/xM\neq 0$이고 $\dim(M/xM)=d-1$이므로, 귀납적 가정에 의하여 $j>d-1$에서 $H_\mathfrak{m}^j(M/xM)=0$이다. 이제 $i>d$를 고정하고 short exact sequence $0 \rightarrow M \overset{x}{\rightarrow} M \rightarrow M/xM \rightarrow 0$의 long exact sequence의 조각

$$H_\mathfrak{m}^{i-1}(M/xM) \rightarrow H_\mathfrak{m}^i(M) \overset{x}{\longrightarrow} H_\mathfrak{m}^i(M)$$

을 보면, $i-1>d-1$이므로 왼쪽 항이 $0$이고 곱하기 $x$는 $H_\mathfrak{m}^i(M)$ 위에서 injective이다. [명제 4](#prop4)의 첫째 결과에 의하여 $H_\mathfrak{m}^i(M)$의 임의의 원소 $h$는 $\mathfrak{m}^nh=0$인 $n$을 가지므로 $x^nh=0$이고, [정리 10](#thm10)의 증명에서와 같이 injectivity를 반복 적용하면 $h=0$이다. 따라서 $i>d$에서 $H_\mathfrak{m}^i(M)=0$이다.
:::

[따름정리 11](#cor11)과 [정리 12](#thm12)를 종합하면 $H_\mathfrak{m}^i(M)$의 비소멸은 구간 $\operatorname{depth}M\leq i\leq\dim M$ 안에서만 일어날 수 있다. 두 값이 일치하는 Cohen--Macaulay module에서는 이 구간이 한 점으로 줄어든다.

::: 따름정리 13
Noetherian local ring $(A,\mathfrak{m})$ 위의 Cohen--Macaulay module $M$에 대하여 ([§Cohen-Macaulay 환, ⁋정의 1](/ko/math/commutative_algebra/cohen_macaulay_rings#def1)), $H_\mathfrak{m}^i(M)$은 $i=\dim M$에서만 $0$이 아니다. 곧 $i\neq\dim M$에서 $H_\mathfrak{m}^i(M)=0$이고 $H_\mathfrak{m}^{\dim M}(M)\neq 0$이다.
:::
::: 증명
$\operatorname{depth}M=\dim M$이므로 [따름정리 11](#cor11)에 의하여 $i<\dim M$에서 $H_\mathfrak{m}^i(M)=0$이고 $H_\mathfrak{m}^{\dim M}(M)\neq 0$이며, [정리 12](#thm12)에 의하여 $i>\dim M$에서 $H_\mathfrak{m}^i(M)=0$이다.
:::

시리즈에서 다루어 온 ring들에서 이 결과들을 구체적으로 확인한다.

::: 예시 14
1. $A=\mathbb{K}[[\x]]$를 생각하자. 이는 maximal ideal $\mathfrak{m}=(\x)$를 갖는 $1$차원 Noetherian local domain이고 ([§단사가군과 Matlis 쌍대성, ⁋예시 13](/ko/math/commutative_algebra/matlis_duality#ex13)), $\mathfrak{m}$이 한 개의 원소로 생성되므로 regular local ring이다. ([§차원, ⁋정의 12](/ko/math/commutative_algebra/Krull_dimension#def12)) 따라서 [§Cohen-Macaulay 환, ⁋따름정리 5](/ko/math/commutative_algebra/cohen_macaulay_rings#cor5)와 [따름정리 13](#cor13)에 의하여 $H_\mathfrak{m}^i(A)$는 $i=1$에서만 $0$이 아니다. [정리 8](#thm8)로 그 값을 직접 계산하면, $\mathfrak{m}=(\x)$의 Čech complex는 $0 \rightarrow A \rightarrow A_\x \rightarrow 0$이고, [§정칙국소환, ⁋명제 5](/ko/math/commutative_algebra/regular_local_rings#prop5)에 의하여 $\Frac(A)$의 임의의 원소가 $u\x^k$ ($u$ unit, $k\in\mathbb{Z}$) 꼴이므로 $A_\x=\Frac(A)=\mathbb{K}((\x))$이다. 따라서

	$$H_\mathfrak{m}^1(A)\cong A_\x/A=\mathbb{K}((\x))/\mathbb{K}[[\x]]$$

	인데, 이는 [§단사가군과 Matlis 쌍대성, ⁋예시 13](/ko/math/commutative_algebra/matlis_duality#ex13)에서 본 residue field의 injective hull $E(\kappa)$ 그 자체이다. 최고 차수의 local cohomology가 injective hull을 재생산하는 것이다.

2. $A=\mathbb{K}[[\x,\y]]$를 생각하자. [§Depth, ⁋예시 11](/ko/math/commutative_algebra/depth#ex11)의 서두에서와 같이 $A$는 $2$차원 Noetherian local ring이고, maximal ideal은 $\mathfrak{m}=(\x,\y)$이다. ([§완비화, ⁋따름정리 6](/ko/math/commutative_algebra/completion#cor6)) $\mathfrak{m}$이 두 개의 원소로 생성되므로 $A$는 regular local ring이고 ([§차원, ⁋정의 12](/ko/math/commutative_algebra/Krull_dimension#def12)), [§Cohen-Macaulay 환, ⁋따름정리 5](/ko/math/commutative_algebra/cohen_macaulay_rings#cor5)와 [따름정리 13](#cor13)에 의하여 $H_\mathfrak{m}^0(A)=H_\mathfrak{m}^1(A)=0$이고 $H_\mathfrak{m}^2(A)\neq 0$이다.

	$H_\mathfrak{m}^2(A)$를 [정리 8](#thm8)의 Čech complex $0 \rightarrow A \rightarrow A_\x\oplus A_\y \rightarrow A_{\x\y} \rightarrow 0$으로 직접 계산하자. $A_{\x\y}$의 임의의 원소 $\xi$는 $f/(\x\y)^k$ ($f\in A$) 꼴이고, $f=\sum_{a,b\geq 0}c_{ab}\x^a\y^b$로 적으면 $\xi$를 형식적인 급수 $\sum_{a,b\geq 0}c_{ab}\x^{a-k}\y^{b-k}$로 쓸 수 있다. $A$가 domain이므로 $f/(\x\y)^k=g/(\x\y)^l$인 것은 $(\x\y)^lf=(\x\y)^kg$인 것과 동치이고, 따라서 각 $(i,j)\in\mathbb{Z}^2$ 자리의 계수 $c_{ij}(\xi)$는 표현의 선택에 무관하게 잘 정의되며 덧셈과 스칼라 곱을 보존한다. $A_\x$의 image는 $g/\x^n=\y^ng/(\x\y)^n$들이므로 $j<0$인 모든 자리에서 계수가 $0$인 원소들로 이루어지고, 거꾸로 $\xi=f/(\x\y)^k$의 계수가 $j<0$에서 모두 $0$이라면 $f$의 모든 항의 $\y$-차수가 $k$ 이상이므로 $f=\y^kh$가 되어 $\xi=h/\x^k$이다. 곧 $A_\x$의 image는 정확히 $j<0$에서 소멸하는 계수를 갖는 원소들이고, 마찬가지로 $A_\y$의 image는 $i<0$에서 소멸하는 계수를 갖는 원소들이다. 이제 $f$를 $\y$-차수가 $k$ 이상인 항들, $\y$-차수가 $k$ 미만이고 $\x$-차수가 $k$ 이상인 항들, 그리고 두 차수가 모두 $k$ 미만인 유한히 많은 항들로 나누면 앞의 둘은 각각 $A_\x$와 $A_\y$의 image에 속하므로, $H_\mathfrak{m}^2(A)$에서 $\xi$의 class는 음의 지수 monomial들의 유한한 선형결합

	$$\sum_{i,j\geq 1}c_{-i,-j}(\xi)\bigl[\x^{-i}\y^{-j}\bigr]$$

	와 같다. 또 어떤 유한한 선형결합 $\sum c_{ij}\x^{-i}\y^{-j}$ ($i,j\geq 1$)이 두 image의 합에 속한다면, $(-i,-j)$ 자리의 계수를 비교할 때 $A_\x$ 쪽 성분은 $-j<0$에서, $A_\y$ 쪽 성분은 $-i<0$에서 소멸하므로 $c_{ij}=0$이다. 따라서 class들 $[\x^{-i}\y^{-j}]$ ($i,j\geq 1$)은 $H_\mathfrak{m}^2(A)$의 $\mathbb{K}$-basis를 이룬다.

	이 basis 위에서 module 구조는 지수의 이동으로 주어진다. $\x\cdot[\x^{-i}\y^{-j}]$는 $i\geq 2$일 때 $[\x^{-(i-1)}\y^{-j}]$이고 $i=1$일 때 $0$이다. $\x$-차수가 $0$ 이상이 되면 $A_\y$의 image에 흡수되기 때문이다. 그럼 $\x$가 소멸시키는 원소는 $i\geq 2$인 계수가 없는 것, $\y$가 소멸시키는 원소는 $j\geq 2$인 계수가 없는 것이므로, socle은

	$$(0:_{H_\mathfrak{m}^2(A)}\mathfrak{m})=\mathbb{K}\cdot\bigl[\x^{-1}\y^{-1}\bigr]$$

	로 $1$차원이다. Regular local ring은 Gorenstein이고 ([§Gorenstein 환, ⁋따름정리 9](/ko/math/commutative_algebra/gorenstein_rings#cor9)), Artinian Gorenstein ring은 socle이 $1$차원인 것으로 특징지어진다. ([§Gorenstein 환, ⁋정리 10](/ko/math/commutative_algebra/gorenstein_rings#thm10)) 이 $1$차원성은 그 사실들과 나란히 놓이는 현상이지만, 여기서는 관찰로만 남겨 둔다.

3. $A=\mathbb{K}[[\x,\y,\z]]/(\x\z,\y\z)$를 생각하자. [§Depth, ⁋예시 11](/ko/math/commutative_algebra/depth#ex11)에서 $\operatorname{depth}A=1<2=\dim A$임을 계산하였다. [따름정리 11](#cor11)에 의하여 $H_\mathfrak{m}^0(A)=0$이고 $H_\mathfrak{m}^1(A)\neq 0$이며, [정리 12](#thm12)에 의하여 $i>2$에서 $H_\mathfrak{m}^i(A)=0$이다. 곧 Cohen--Macaulay가 아닌 이 ring에서 local cohomology의 비소멸은 한 점에 집중되는 대신 구간 $1\leq i\leq 2$의 두 자리에 걸쳐 있을 수 있으며, depth와 차원의 격차가 cohomology의 폭으로 나타난다.
:::

---

**참고문헌**

**[BH]** W. Bruns, J. Herzog. *Cohen-Macaulay Rings*. Cambridge University Press, 1993.  
**[Eis]** David Eisenbud. *Commutative Algebra: with a view toward algebraic geometry*. Springer, 1995.  
**[Mat]** Hideyuki Matsumura. *Commutative Ring Theory*. Cambridge University Press, 1986.  
**[Stacks]** The Stacks Project Authors. *The Stacks Project*. [https://stacks.math.columbia.edu](https://stacks.math.columbia.edu).

---
