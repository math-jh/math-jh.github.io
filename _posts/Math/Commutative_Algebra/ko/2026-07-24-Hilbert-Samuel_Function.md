---
title: "힐베르트-사무엘 함수"
description: "등급가군의 힐베르트 함수와 뇌터 국소환 위의 힐베르트-사무엘 함수가 결국 다항식과 일치함을 보이고, 그 차수가 크룰 차원과 일치한다는 차원 정리와 중복도의 기본 성질을 다룬다."
excerpt: "Hilbert-Samuel 함수의 다항식성과 차원 정리, 그리고 중복도"

categories: [Math / Commutative Algebra]
permalink: /ko/math/commutative_algebra/hilbert-samuel_function
sidebar: 
    nav: "commutative_algebra-ko"

date: 2026-07-24
weight: 18
published: false
drift_needed: true

---

[§차원](/ko/math/commutative_algebra/Krull_dimension)에서 우리는 ring의 차원을 prime ideal들의 chain의 길이로 정의하였고, [§매개계](/ko/math/commutative_algebra/system_of_parameters)에서는 Noetherian local ring의 차원이 system of parameters의 크기와 일치한다는 것을 살펴보았다. 이번 글에서는 차원의 세 번째 특징화를 다룬다. Noetherian local ring $(A,\mathfrak{m})$ 위의 finitely generated module $M$에 대하여, 길이 $\length(M/\mathfrak{m}^nM)$은 $n$이 커짐에 따라 결국 다항식처럼 자라는데, 이 다항식의 degree가 정확히 $\dim M$과 일치한다는 것이 이번 글의 주된 결과이다. 이를 위해 우리는 먼저 graded module의 Hilbert function을 살펴본 뒤, filtration을 통해 이를 local ring의 경우로 옮겨와 Hilbert-Samuel function의 다항식성을 증명한다. 마지막으로 이 다항식의 leading coefficient가 담고 있는 기하적 정보인 중복도를 살펴본다.

## 수치 다항식

앞으로 등장할 다항식들은 정수에서 정수값을 갖지만, 그 계수가 정수일 필요는 없다. 가령 함수 $n\mapsto n(n+1)/2$는 모든 정수에서 정수값을 갖는 degree $2$의 다항식이지만 그 계수는 정수가 아니다. 이러한 다항식들을 다루기 위해 다음을 정의한다.

::: 정의 1
유리계수 다항식 $P\in \mathbb{Q}[\x]$가 *numerical polynomial*이라는 것은 충분히 큰 모든 정수 $n$에 대하여 $P(n)\in \mathbb{Z}$인 것이다.
:::

가장 기본적인 예시는 음이 아닌 정수 $k$에 대하여 정의되는 다음의 다항식

$$\binom{\x}{k}=\frac{\x(\x-1)\cdots(\x-k+1)}{k!}$$

이다. 이는 degree $k$의 다항식이며, 임의의 정수에서 이항계수라는 정수값을 가지므로 numerical polynomial이다. 아래 보조정리는 사실상 이들이 모든 numerical polynomial을 만들어낸다는 것을 말해준다. 앞으로 충분히 큰 정수들에서 정의된 함수 $f$에 대하여 $\Delta f(n)=f(n+1)-f(n)$으로 표기하자.

::: 보조정리 2
다음이 성립한다.

1. Degree $d$의 numerical polynomial $P$는 유일하게 결정되는 정수 $c_0,\ldots, c_d$에 대하여 다음의 꼴

    $$P=\sum_{k=0}^d c_k\binom{\x}{k}$$

    로 적을 수 있다.
2. 충분히 큰 정수들에서 정의된 정수값 함수 $f$에 대하여, 만일 $\Delta f$가 충분히 큰 $n$에서 numerical polynomial $Q$와 일치한다면, $f$ 또한 충분히 큰 $n$에서 어떠한 numerical polynomial $P$와 일치한다. 이 때 $Q=0$이면 $P$는 상수이고, $Q\neq 0$이면 $\deg P=\deg Q+1$이다.
:::
::: 증명
첫째 결과를 보이자. 다항식들 $\binom{\x}{k}$ ($0\leq k\leq d$)는 degree가 각각 $k$이므로 degree $d$ 이하의 다항식들의 $\mathbb{Q}$-벡터공간의 basis를 이루고, 따라서 위의 표현을 만족하는 유리수 $c_k$들이 유일하게 존재한다. 이제 $c_k$들이 정수임을 $d$에 대한 귀납법으로 보이자. $d=0$인 경우 $P=c_0$은 상수이므로 자명하다. $d\geq 1$인 경우, Pascal's rule에 의하여 $\Delta\binom{\x}{k}=\binom{\x}{k-1}$이므로

$$\Delta P=\sum_{k=1}^d c_k\binom{\x}{k-1}$$

이고, $\Delta P$는 충분히 큰 정수에서 두 정수의 차이므로 다시 degree $d-1$의 numerical polynomial이다. 귀납적 가정에 의하여 $c_1,\ldots, c_d$는 정수이고, 그럼 충분히 큰 정수 $n$에 대하여 $c_0=P(n)-\sum_{k=1}^d c_k\binom{n}{k}$ 또한 정수이다.

둘째 결과의 경우, 첫째 결과를 사용하여 $Q=\sum_{k=0}^{d-1} c_k\binom{\x}{k}$ ($c_k\in \mathbb{Z}$)로 적고 $P_0=\sum_{k=0}^{d-1}c_k\binom{\x}{k+1}$로 두자. 그럼 $\Delta P_0=Q$이므로 충분히 큰 $n$에 대하여 $\Delta(f-P_0)(n)=0$이고, 따라서 $f-P_0$은 충분히 큰 정수에서 어떠한 상수 $c$와 일치한다. 이 상수는 정수값 함수와 numerical polynomial의 차이므로 정수이고, $P=P_0+c$로 두면 원하는 결과를 얻는다. $Q\neq 0$이라면 $c_{\deg Q}\neq 0$이므로 $\deg P=\deg Q+1$이다.
:::

## 등급가군의 힐베르트 함수

이제 graded module의 크기가 degree를 따라 어떻게 분포하는지를 살펴본다. 그 준비로 우선 길이가 short exact sequence에 대해 additive하다는 것을 확인한다.

::: 보조정리 3
$A$-module들의 short exact sequence

$$0 \rightarrow M' \overset{u}{\longrightarrow} M \overset{v}{\longrightarrow} M'' \rightarrow 0$$

에 대하여, $M$이 유한한 길이를 갖는 것과 $M'$, $M''$이 모두 유한한 길이를 갖는 것이 동치이며, 이 때 다음의 식

$$\length(M)=\length(M')+\length(M'')$$

이 성립한다.
:::
::: 증명
우선 유한한 길이 $l=\length(N)$을 갖는 module $N$의 임의의 proper submodule $L$이 $\length(L)<l$을 만족한다는 것을 보이자. 길이 $l$의 composition series $N=N_0\supsetneq\cdots\supsetneq N_l=0$을 택하고 ([§조르단-횔더 정리, ⁋정의 2](/ko/math/commutative_algebra/Jordan-Holder_theorem#def2)) $L_k=L\cap N_k$로 두자. 그럼 각각의 $k$에 대하여 canonical map $L_k \rightarrow N_k/N_{k+1}$의 kernel이 $L\cap N_{k+1}=L_{k+1}$이므로 $L_k/L_{k+1}$은 simple module $N_k/N_{k+1}$의 submodule로 볼 수 있고, 따라서 $0$이거나 simple이다. 그러므로 chain $L=L_0\supseteq L_1\supseteq\cdots\supseteq L_l=0$에서 중복되는 항들을 제거하면 $L$의 composition series를 얻고, $\length(L)\leq l$이다. 만일 $\length(L)=l$이라면 어느 항도 제거되지 않아야 하므로 모든 $k$에 대하여 $L\cap N_k+N_{k+1}=N_k$이다. 그럼 $L\cap N_l=N_l=0$에서 시작하여, $L\cap N_{k+1}=N_{k+1}$을 가정하면 $N_{k+1}\subseteq L$이고 따라서 $N_k=L\cap N_k+N_{k+1}\subseteq L$이므로 $L\cap N_k=N_k$이다. 귀납적으로 $L\supseteq N_0=N$이 되어 $L$이 proper라는 가정에 모순이므로 $\length(L)<l$이다.

이로부터 유한한 길이의 module $N$의 submodule들의 임의의 chain $N=P_0\supsetneq P_1\supsetneq\cdots\supsetneq P_r=0$은 매 단계에서 길이가 strict하게 감소하므로 $r\leq \length(N)$을 만족한다. 특히 $N$의 임의의 composition series의 길이는 $\length(N)$ 이하인데, [§조르단-횔더 정리, ⁋정의 2](/ko/math/commutative_algebra/Jordan-Holder_theorem#def2)에서 길이는 composition series들의 길이의 최솟값으로 정의되었으므로 결국 $N$의 모든 composition series는 정확히 길이 $\length(N)$을 갖는다.

이제 주어진 short exact sequence를 보자. $M$이 유한한 길이를 갖는다면, $M'$의 submodule들의 chain은 $u$를 통해, $M''$의 submodule들의 chain은 $v^{-1}$를 통해 각각 $M$의 chain을 주고 strict한 포함관계가 보존되므로, $M'$과 $M''$에서 chain의 길이는 $\length(M)$ 이하로 유계이다. 따라서 각각에서 길이가 maximal한 chain을 택할 수 있고, maximal한 chain은 어느 두 항 사이에도 새로운 submodule을 끼워넣을 수 없으므로 composition series이다. 즉 $M'$과 $M''$은 유한한 길이를 갖는다.

거꾸로 $M'$과 $M''$이 각각 길이 $a$, $b$의 composition series $M'=M_0'\supsetneq\cdots\supsetneq M_a'=0$과 $M''=M_0''\supsetneq\cdots\supsetneq M_b''=0$을 갖는다 하자. 그럼 다음의 chain

$$M=v^{-1}(M_0'')\supsetneq \cdots\supsetneq v^{-1}(M_b'')=u(M')\supsetneq u(M_1')\supsetneq\cdots\supsetneq u(M_a')=0$$

은 $v^{-1}(M_k'')/v^{-1}(M_{k+1}'')\cong M_k''/M_{k+1}''$과 $u(M_k')/u(M_{k+1}')\cong M_k'/M_{k+1}'$이 모두 simple이므로 길이 $a+b$의 composition series이다. 앞 문단에서 살펴본 composition series의 길이의 유일성에 의하여 $\length(M)=a+b=\length(M')+\length(M'')$이다.
:::

이 절의 나머지에서 $R=\bigoplus_{n\geq 0}R_n$은 다음 조건을 만족하는 graded ring이다 ([\[대수적 구조\] §등급환, ⁋정의 1](/ko/math/algebraic_structures/graded_rings#def1)). 우선 degree $0$ part $R_0$는 Artinian ring이고, $R$는 $R_0$-algebra로서 유한히 많은 degree $1$의 원소들 $x_1,\ldots, x_s\in R_1$로 생성된다. 그럼 $R$는 polynomial ring $R_0[\x_1,\ldots, \x_s]$의 quotient이므로 [§기본 개념들, ⁋정리 12](/ko/math/commutative_algebra/basic_notions#thm12)와 [§기본 개념들, ⁋따름정리 13](/ko/math/commutative_algebra/basic_notions#cor13)에 의하여 Noetherian ring이다.

이제 finitely generated graded $R$-module $M$을 고정하자. ([\[대수적 구조\] §등급가군, ⁋정의 1](/ko/math/algebraic_structures/graded_modules#def1)) $M$의 generator들을 homogeneous 성분으로 분해하면 $M$이 유한히 많은 homogeneous 원소들 $m_1,\ldots, m_r$로 생성된다고 가정할 수 있고, $d_i=\deg m_i$라 하면 $M_n=\sum_i R_{n-d_i}m_i$이다. 각각의 $R_k$는 $x_1,\ldots, x_s$의 degree $k$ monomial들로 $R_0$-module로서 생성되므로, 각각의 $M_n$은 finitely generated $R_0$-module이다. 한편 $R_0$가 Artinian이므로 $R_0$의 임의의 prime ideal은 maximal이고 ([§조르단-횔더 정리, ⁋정리 4](/ko/math/commutative_algebra/Jordan-Holder_theorem#thm4)), 따라서 [§조르단-횔더 정리, ⁋따름정리 6](/ko/math/commutative_algebra/Jordan-Holder_theorem#cor6)에 의하여 $M_n$은 $R_0$-module로서 유한한 길이를 갖는다. 그러므로 다음 정의가 잘 정의된다.

::: 정의 4
위와 같은 상황에서, $M$의 *Hilbert function<sub>힐베르트 함수</sub>* $H_M$을 다음의 식

$$H_M(n)=\length_{R_0}(M_n)$$

으로 정의한다.
:::

정의에 의하여 $H_M$은 $M$을 degree별로 잘라 그 크기를 잰 것이다. 가령 $R_0=\mathbb{K}$가 field라면 $H_M(n)=\dim_\mathbb{K} M_n$이다. 다음 정리는 이 함수가 결국 다항식처럼 행동한다는 고전적인 결과이다.

::: 정리 5 (Hilbert)
위와 같은 상황에서, 적당한 numerical polynomial $P_M$이 존재하여 충분히 큰 $n$에 대해 $H_M(n)=P_M(n)$이 성립한다. 뿐만 아니라 $P_M=0$이거나 $\deg P_M\leq s-1$이다.
:::
::: 증명
$R$의 generator의 개수 $s$에 대한 귀납법으로 증명한다. $s=0$인 경우 $R=R_0$이고, 위에서 살펴본 것처럼 $M_n=\sum_i R_{n-d_i}m_i$인데 $R_k=0$ ($k\neq 0$)이므로 $n>\max_i d_i$에 대하여 $M_n=0$이다. 따라서 $H_M$은 결국 $0$과 일치한다.

이제 $s\geq 1$이라 하고 주장이 $s-1$개의 degree $1$ 원소로 생성되는 graded ring들에 대해 성립한다고 가정하자. 곱하기 $x_s$는 각 degree에서 $R_0$-linear map $M_n \rightarrow M_{n+1}$을 주므로, $K=\{z\in M\mid x_sz=0\}$와 $C=M/x_sM$으로 두면 각각의 $n$에 대하여 다음의 exact sequence

$$0 \rightarrow K_n \rightarrow M_n \overset{x_s}{\longrightarrow} M_{n+1} \rightarrow C_{n+1} \rightarrow 0$$

를 얻는다. 여기서 $K$가 graded submodule이라는 것은, $z\in K$를 homogeneous 성분들로 분해하여 $z=\sum z_i$로 적으면 $x_sz_i$들이 서로 다른 degree의 homogeneous 성분들이므로 $x_sz=0$이 각각의 $x_sz_i=0$을 함의한다는 것에서 알 수 있고, $x_sM$이 graded submodule이므로 $C$도 graded module이다. $R$가 Noetherian이고 $M$이 finitely generated이므로 $M$은 Noetherian module이고 ([§기본 개념들, ⁋따름정리 6](/ko/math/commutative_algebra/basic_notions#cor6)과 [§기본 개념들, ⁋명제 4](/ko/math/commutative_algebra/basic_notions#prop4)), 따라서 submodule $K$는 finitely generated이며 ([§기본 개념들, ⁋정리 3](/ko/math/commutative_algebra/basic_notions#thm3)) quotient $C$도 그러하다.

한편 $K$와 $C$는 모두 $x_s$에 의해 annihilate되므로 quotient ring $R/(x_s)$ 위의 finitely generated graded module이다. Ideal $(x_s)$는 homogeneous 원소로 생성되므로 $R/(x_s)$는 다시 graded ring이고, 그 degree $0$ part는 $R_0$ 그대로이며 $R_0$ 위에서 $x_1,\ldots, x_{s-1}$의 image들로 생성된다. 따라서 귀납적 가정에 의하여 $H_K$와 $H_C$는 충분히 큰 $n$에서 각각 $0$이거나 degree $s-2$ 이하의 numerical polynomial과 일치한다.

이제 위의 exact sequence를 image에서 둘로 쪼개어 [보조정리 3](#lem3)을 두 번 적용하면

$$H_M(n+1)-H_M(n)=H_C(n+1)-H_K(n)$$

을 얻는다. 즉 $\Delta H_M$은 충분히 큰 $n$에서 $0$이거나 degree $s-2$ 이하의 numerical polynomial과 일치하고, [보조정리 2](#lem2)의 둘째 결과에 의하여 $H_M$은 충분히 큰 $n$에서 numerical polynomial $P_M$과 일치하며 $P_M=0$이거나 $\deg P_M\leq s-1$이다.
:::

위 정리에서 얻어지는 numerical polynomial $P_M$을 $M$의 *Hilbert polynomial<sub>힐베르트 다항식</sub>*이라 부른다.

::: 예시 6
1. Field $\mathbb{K}$와 polynomial ring $R=\mathbb{K}[\x_1,\ldots,\x_s]$를 각 변수가 degree $1$을 갖는 graded ring으로 보자. 그럼 $R_n$은 degree $n$의 monomial들을 basis로 가지며, 그 개수는 중복조합의 수이므로 모든 $n\geq 0$에 대하여

    $$H_R(n)=\binom{n+s-1}{s-1}$$

    이다. 즉 $P_R$는 degree가 정확히 $s-1$이고, [정리 5](#thm5)의 degree 상한이 실제로 달성된다.  
    이제 $s\geq 2$라 하고, $0$이 아닌 degree $e$의 homogeneous polynomial $f\in R$에 대하여 $S=R/(f)$를 생각하자. $R$는 integral domain이므로 곱하기 $f$는 injective이고, 각각의 $n\geq e$에 대하여 exact sequence

    $$0 \rightarrow R_{n-e} \overset{f}{\longrightarrow} R_n \rightarrow S_n \rightarrow 0$$

    로부터 다음의 식

    $$H_S(n)=\binom{n+s-1}{s-1}-\binom{n-e+s-1}{s-1}$$

    을 얻는다. 우변의 두 다항식은 degree $s-1$과 leading coefficient $1/(s-1)!$을 공유하므로 최고차항이 소거되고, $n^{s-1}-(n-e)^{s-1}$의 최고차항이 $e(s-1)n^{s-2}$라는 것에서 $P_S$는 degree $s-2$와 leading coefficient $e/(s-2)!$을 갖는 것을 안다. 가령 $s=2$인 경우, 즉 평면곡선의 경우 $H_S$는 결국 상수 $e$와 일치한다.
2. Polynomial ring $\mathbb{K}[\x,\y]$의 degree $3n$ 부분들을 모아 $R_n=\mathbb{K}[\x,\y]_{3n}$으로 정의된 graded ring $R=\bigoplus_{n\geq 0}R_n$을 생각하자. 그럼 $R_0=\mathbb{K}$이고 $R_1$은 네 monomial $\x^3, \x^2\y,\x\y^2,\y^3$을 basis로 갖는다. Degree $3n$의 임의의 monomial $\x^a\y^b$는, $a\geq 3$이면 $\x^3$을, 아니면 $b\geq 3$이므로 $\y^3$을 뽑아내는 과정을 반복하여 degree $3$ monomial $n$개의 곱으로 적을 수 있으므로 $R$는 $R_0$ 위에서 $R_1$의 네 원소로 생성된다. 그럼 모든 $n\geq 0$에서

    $$H_R(n)=\dim_\mathbb{K}\mathbb{K}[\x,\y]_{3n}=3n+1$$

    이므로 $P_R(n)=3n+1$이고, [정리 5](#thm5)가 주는 상한 $3$과 달리 실제 degree는 $1$이다. 이 $R$는 projective space $\mathbb{P}^3$ 안의 twisted cubic curve의 homogeneous coordinate ring으로, Hilbert polynomial의 degree $1$은 곡선의 차원을, leading coefficient에 $1!$을 곱한 값 $3$은 곡선의 degree를 담고 있다. 일반적으로 projective variety의 Hilbert polynomial은 이렇게 그 차원과 degree를 기억한다.
:::

## 힐베르트-사무엘 함수

이제 Noetherian local ring $(A,\mathfrak{m})$과 $0$이 아닌 finitely generated $A$-module $M$을 고정하자. Local ring은 graded ring이 아니지만, [§부풀림 대수](/ko/math/commutative_algebra/blowup_algebra)에서 살펴본 것처럼 filtration을 통해 graded 대상 $\gr$을 얻을 수 있고, 이를 통해 앞 절의 결과를 local ring으로 옮겨올 수 있다.

Ideal $\mathfrak{a}\subseteq \mathfrak{m}$이 $M/\mathfrak{a}M$이 유한한 길이를 갖도록 한다면, $\mathfrak{a}$를 $M$의 *ideal of definition*이라 부르기로 하자. [§조르단-횔더 정리, ⁋따름정리 6](/ko/math/commutative_algebra/Jordan-Holder_theorem#cor6)의 둘째 조건에 의하면 이는 적당한 $t$에 대하여 $\mathfrak{m}^tM\subseteq \mathfrak{a}M$이 성립하는 것과 동치이다 (local ring에서 maximal ideal들의 곱은 $\mathfrak{m}$의 거듭제곱이다). 또, 같은 따름정리의 셋째 조건과 [§매개계, ⁋보조정리 4](/ko/math/commutative_algebra/system_of_parameters#lem4)를 종합하면, 이는 $\mathfrak{a}+\ann(M)$을 포함하는 prime ideal이 $\mathfrak{m}$ 뿐인 것, 즉 $A/(\mathfrak{a}+\ann(M))$이 Artinian ring인 것과도 동치이다. ([§조르단-횔더 정리, ⁋정리 4](/ko/math/commutative_algebra/Jordan-Holder_theorem#thm4)) 가장 기본적인 예시는 $\mathfrak{m}$ 자신으로, $M/\mathfrak{m}M$은 유한차원 $A/\mathfrak{m}$-벡터공간이므로 항상 ideal of definition이다. 또, [§매개계, ⁋명제–정의 3](/ko/math/commutative_algebra/system_of_parameters#prop-def3)의 parameter ideal은 정확히 $\dim M$개의 원소로 생성되는 ideal of definition이다.

이제 $M$의 ideal of definition $\mathfrak{a}$와 $\mathfrak{a}$-stable filtration $\mathcal{J}: M=M_0\supseteq M_1\supseteq\cdots$가 주어졌다 하자. ([§부풀림 대수, ⁋정의 3](/ko/math/commutative_algebra/blowup_algebra#def3)) $\mathfrak{a}$-filtration의 정의로부터 귀납적으로 $\mathfrak{a}^nM\subseteq M_n$이고, 위에서 살펴본 $\mathfrak{m}^tM\subseteq \mathfrak{a}M$으로부터 다시 귀납적으로 $\mathfrak{m}^{tn}M\subseteq \mathfrak{a}^nM$이므로, $M/M_n$은 $M/\mathfrak{m}^{tn}M$의 quotient가 되어 유한한 길이를 갖는다. 따라서 다음 정의가 잘 정의된다.

::: 정의 7
위와 같은 상황에서, $\mathcal{J}$에 대한 $M$의 *Hilbert-Samuel function<sub>힐베르트-사무엘 함수</sub>* $\chi_\mathcal{J}$를 다음의 식

$$\chi_\mathcal{J}(n)=\length(M/M_n)$$

으로 정의한다.
:::

특별히 $\mathfrak{a}$-adic filtration $M_n=\mathfrak{a}^nM$의 Hilbert-Samuel function을 $\chi_{\mathfrak{a},M}$으로 적는다. 즉 $\chi_{\mathfrak{a},M}(n)=\length(M/\mathfrak{a}^nM)$이다. 핵심적인 관찰은, short exact sequence $0 \rightarrow M_n/M_{n+1} \rightarrow M/M_{n+1} \rightarrow M/M_n \rightarrow 0$에 [보조정리 3](#lem3)을 적용하여 얻어지는 다음의 식

$$\Delta\chi_\mathcal{J}(n)=\chi_\mathcal{J}(n+1)-\chi_\mathcal{J}(n)=\length(M_n/M_{n+1})$$

의 우변이 정확히 associated graded module $\gr_\mathcal{J}M$의 degree $n$ 부분의 길이라는 것이다. 이를 통해 앞 절의 결과를 적용할 수 있다.

::: 정리 8 (Samuel)
Noetherian local ring $(A,\mathfrak{m})$과 $0$이 아닌 finitely generated $A$-module $M$, 그리고 $s$개의 원소로 생성되는 $M$의 ideal of definition $\mathfrak{a}$가 주어졌다 하자. 그럼 $M$의 임의의 $\mathfrak{a}$-stable filtration $\mathcal{J}$에 대하여 다음이 성립한다.

1. 적당한 numerical polynomial $P_\mathcal{J}$가 존재하여 충분히 큰 $n$에 대해 $\chi_\mathcal{J}(n)=P_\mathcal{J}(n)$이며, $\deg P_\mathcal{J}\leq s$이다.
2. $P_\mathcal{J}$의 degree와 leading coefficient는 $\mathfrak{a}$-stable filtration $\mathcal{J}$의 선택에 의존하지 않는다.
:::
::: 증명
우선 $\overline{A}=A/\ann(M)$과 $\overline{\mathfrak{a}}=(\mathfrak{a}+\ann(M))/\ann(M)$으로 두자. $M$을 $\overline{A}$-module로 보아도 submodule들과 길이는 변하지 않고, $\mathfrak{a}M_k=\overline{\mathfrak{a}}M_k$이므로 $\mathcal{J}$는 그대로 $\overline{\mathfrak{a}}$-stable filtration이며, $\overline{\mathfrak{a}}$는 $\mathfrak{a}$의 generator $a_1,\ldots, a_s$들의 image로 생성된다. 또 위에서 살펴본 동치에 의하여 $\overline{A}/\overline{\mathfrak{a}}=A/(\mathfrak{a}+\ann(M))$은 Artinian ring이다.

이제 associated graded ring $\gr_{\overline{\mathfrak{a}}}\overline{A}$를 생각하자. ([§부풀림 대수, ⁋정의 1](/ko/math/commutative_algebra/blowup_algebra#def1)) 임의의 $\overline{\mathfrak{a}}^k/\overline{\mathfrak{a}}^{k+1}$는 $a_i$들의 degree $k$ monomial들의 image로 생성되므로, 이 graded ring은 Artinian ring $\overline{A}/\overline{\mathfrak{a}}$ 위에서 degree $1$의 원소들, 곧 $a_i$들의 $\overline{\mathfrak{a}}/\overline{\mathfrak{a}}^2$에서의 image $s$개로 생성된다. 한편 $M$은 Noetherian module이므로 ([§기본 개념들, ⁋따름정리 6](/ko/math/commutative_algebra/basic_notions#cor6)과 [§기본 개념들, ⁋명제 4](/ko/math/commutative_algebra/basic_notions#prop4)) $\mathcal{J}$의 각 항은 finitely generated이고, 따라서 [§부풀림 대수, ⁋명제 4](/ko/math/commutative_algebra/blowup_algebra#prop4)에 의하여 $\gr_\mathcal{J}M$은 finitely generated graded $\gr_{\overline{\mathfrak{a}}}\overline{A}$-module이다. 각각의 $M_n/M_{n+1}$은 $\mathfrak{a}+\ann(M)$에 의해 annihilate되므로 그 $A$-submodule들은 $\overline{A}/\overline{\mathfrak{a}}$-submodule들과 일치하고, 두 길이도 같다. 따라서 [정리 5](#thm5)에 의하여 함수 $n\mapsto \length(M_n/M_{n+1})$은 충분히 큰 $n$에서 $0$이거나 degree $s-1$ 이하의 numerical polynomial과 일치하고, 위의 관찰과 [보조정리 2](#lem2)의 둘째 결과에 의하여 $\chi_\mathcal{J}$는 충분히 큰 $n$에서 degree $s$ 이하의 numerical polynomial $P_\mathcal{J}$와 일치한다.

둘째 결과를 보이자. $\mathcal{J}$가 $\mathfrak{a}$-stable이므로 적당한 $n_0$가 존재하여 $k\geq n_0$일 때마다 $M_{k+1}=\mathfrak{a}M_k$이고, 따라서 임의의 $n$에 대하여 $M_{n_0+n}=\mathfrak{a}^nM_{n_0}\subseteq \mathfrak{a}^nM$이다. 이를 $\mathfrak{a}^nM\subseteq M_n$과 종합하면 quotient들 사이의 surjection으로부터 다음의 부등식

$$\chi_\mathcal{J}(n)\leq \chi_{\mathfrak{a},M}(n)\leq \chi_\mathcal{J}(n_0+n)$$

을 얻는다. 충분히 큰 $n$에서 이는 다항식들 사이의 부등식 $P_\mathcal{J}(n)\leq P_{\mathfrak{a},M}(n)\leq P_\mathcal{J}(n_0+n)$이 된다. 첫째 부등식으로부터 $\deg P_\mathcal{J}\leq \deg P_{\mathfrak{a},M}$이고 둘째 부등식으로부터 $\deg P_{\mathfrak{a},M}\leq \deg P_\mathcal{J}$이므로 두 다항식의 degree는 같으며, 같은 degree의 두 다항식에 대하여 위의 부등식들은 leading coefficient의 등호까지 강제한다. 즉 $P_\mathcal{J}$의 degree와 leading coefficient는 $\mathfrak{a}$-adic filtration의 그것과 일치하므로, $\mathcal{J}$의 선택에 의존하지 않는다.
:::

특별히 $\mathfrak{a}$-adic filtration의 경우 얻어지는 다항식 $P_{\mathfrak{a},M}$을 $M$의 ($\mathfrak{a}$에 대한) *Hilbert-Samuel polynomial<sub>힐베르트-사무엘 다항식</sub>*이라 부른다. 위 정리의 degree 상한에 더하여, degree는 다음과 같이 ideal of definition의 선택에도 의존하지 않는다.

::: 따름정리 9
$M$의 임의의 두 ideal of definition $\mathfrak{a}$, $\mathfrak{b}$에 대하여 $\deg P_{\mathfrak{a},M}=\deg P_{\mathfrak{b},M}$이 성립한다.
:::
::: 증명
$\mathfrak{b}=\mathfrak{m}$인 경우를 보이면 충분하다. 우선 $\mathfrak{a}\subseteq \mathfrak{m}$으로부터 $\mathfrak{a}^nM\subseteq \mathfrak{m}^nM$이고, 따라서 $\chi_{\mathfrak{m},M}(n)\leq \chi_{\mathfrak{a},M}(n)$이므로 $\deg P_{\mathfrak{m},M}\leq \deg P_{\mathfrak{a},M}$이다. 거꾸로 위에서 살펴본 것처럼 적당한 $t$에 대하여 $\mathfrak{m}^{tn}M\subseteq \mathfrak{a}^nM$이 모든 $n$에서 성립하므로 $\chi_{\mathfrak{a},M}(n)\leq \chi_{\mathfrak{m},M}(tn)$이고, 우변은 충분히 큰 $n$에서 $n$에 대한 degree $\deg P_{\mathfrak{m},M}$의 다항식이므로 $\deg P_{\mathfrak{a},M}\leq\deg P_{\mathfrak{m},M}$이다.
:::

이 공통의 degree를 $d(M)$으로 표기하자. 반면 leading coefficient는 ideal of definition의 선택에 의존하며, 이는 마지막 절에서 중복도를 정의할 때 다시 살펴본다. 다음은 구체적인 계산의 예시이다.

::: 예시 10
Field $\mathbb{K}$에 대하여 $B=\mathbb{K}[\x,\y]/(\y^2-\x^3)$로 두자. 이는 원점에서 cusp를 갖는 평면곡선 $\y^2=\x^3$의 coordinate ring이다. $B/(\x,\y)B\cong \mathbb{K}$이므로 $\mathfrak{n}=(\x,\y)B$는 maximal ideal이고, localization $A=B_\mathfrak{n}$은 Noetherian local ring이다. ([§국소화, ⁋따름정리 9](/ko/math/commutative_algebra/localization#cor9)) $A$의 maximal ideal을 $\mathfrak{m}=\mathfrak{n}A$라 하고 $\chi_{\mathfrak{m},A}$를 계산하자.

우선 $B/\mathfrak{n}^n$은 $\mathfrak{n}^n$에 의해 annihilate되는 finitely generated $B$-module이고, $\mathfrak{n}^n$을 포함하는 prime ideal은 $\mathfrak{n}$을 포함하므로 maximal이다. 따라서 [§조르단-횔더 정리, ⁋따름정리 6](/ko/math/commutative_algebra/Jordan-Holder_theorem#cor6)에 의하여 $B/\mathfrak{n}^n$은 유한한 길이를 갖고, [§조르단-횔더 정리, ⁋정리 3](/ko/math/commutative_algebra/Jordan-Holder_theorem#thm3)의 셋째 결과에 의하여 localization을 하더라도 변하지 않는다. Localization은 quotient와 commute하므로 이는 $A/\mathfrak{m}^n\cong B/\mathfrak{n}^n$을 의미하고, 이 identification 아래에서 submodule들이 일대일 대응되므로 두 module의 길이는 같다. 한편 $B/\mathfrak{n}^n$의 임의의 simple subquotient $S$는 그 annihilator가 maximal ideal $\mathfrak{m}'$이 되어 $S\cong B/\mathfrak{m}'$인데 ([§조르단-횔더 정리, ⁋정의 1](/ko/math/commutative_algebra/Jordan-Holder_theorem#def1) 직후의 관찰), $\mathfrak{n}^n\subseteq \ann(S)$이므로 $\mathfrak{m}'=\mathfrak{n}$이다. 즉 모든 composition factor가 $B/\mathfrak{n}\cong\mathbb{K}$이므로 결국 $\chi_{\mathfrak{m},A}(n)=\dim_\mathbb{K}(B/\mathfrak{n}^n)$이다.

이제 $B/\mathfrak{n}^n=\mathbb{K}[\x,\y]/J_n$이고, 여기서 $J_n=(\y^2-\x^3)+(\x,\y)^n$이다. 임의의 monomial $\x^a\y^b$가 $b\geq 2$를 만족하면 다음의 식

$$\x^a\y^b-\x^{a+3}\y^{b-2}=\x^a\y^{b-2}(\y^2-\x^3)\in J_n$$

에서 $\x^a\y^b$를 $\x^{a+3}\y^{b-2}$로 교체할 수 있고, 이 교체는 degree를 $1$ 증가시킨다. 이를 반복하면 임의의 monomial은 modulo $J_n$으로 $\x^a$ 혹은 $\x^a\y$ 꼴의 monomial과 같아지거나, degree가 $n$ 이상이 되어 $0$이 된다. 따라서 $\mathbb{K}[\x,\y]/J_n$은 $1,\x,\ldots,\x^{n-1}$과 $\y,\x\y,\ldots, \x^{n-2}\y$로 span된다.

이들이 linearly independent라는 것을 보이기 위해 ring homomorphism $\phi:\mathbb{K}[\x,\y] \rightarrow \mathbb{K}[\z]$를 $\x\mapsto \z^2$, $\y\mapsto \z^3$으로 정의하자. 그럼 $\phi(\y^2-\x^3)=0$이고, $(\x,\y)^n$의 generator $\x^a\y^b$ ($a+b=n$)는 $\z^{2a+3b}$로 가는데 $2a+3b\geq 2n$이므로 $\phi(J_n)\subseteq (\z^{2n})$이다. 이제 $\deg p\leq n-1$, $\deg q\leq n-2$인 $p,q\in \mathbb{K}[\x]$에 대하여 $p(\x)+q(\x)\y\in J_n$이라 하면

$$p(\z^2)+\z^3q(\z^2)\in (\z^{2n})$$

인데, 좌변에서 $p(\z^2)$의 항들은 $\z$의 짝수 거듭제곱으로 그 지수가 $2n-2$ 이하이고 $\z^3q(\z^2)$의 항들은 홀수 거듭제곱으로 그 지수가 $2n-1$ 이하이므로 서로 겹치는 항이 없고 모두 $(\z^{2n})$ 바깥의 degree를 갖는다. 따라서 $p=q=0$이다.

이상으로부터 임의의 $n\geq 1$에 대하여 다음의 식

$$\chi_{\mathfrak{m},A}(n)=n+(n-1)=2n-1$$

을 얻는다. 즉 $P_{\mathfrak{m},A}(n)=2n-1$이고 $d(A)=1$이다.
:::

다음 명제는 Hilbert-Samuel function이 short exact sequence에 대하여 leading term의 수준에서 additive하다는 것을 말해준다.

::: 명제 11
Noetherian local ring $(A,\mathfrak{m})$ 위의 $0$이 아닌 finitely generated $A$-module들의 short exact sequence

$$0 \rightarrow M' \rightarrow M \rightarrow M'' \rightarrow 0$$

과 $M$의 ideal of definition $\mathfrak{a}$가 주어졌다 하자. 그럼 $\mathfrak{a}$는 $M'$과 $M''$의 ideal of definition이기도 하며, 다음이 성립한다.

1. 함수 $\chi_{\mathfrak{a},M'}+\chi_{\mathfrak{a},M''}-\chi_{\mathfrak{a},M}$은 충분히 큰 $n$에서 numerical polynomial $R$와 일치하며, 충분히 큰 $n$에서 $0\leq R(n)\leq \chi_{\mathfrak{a},M'}(n)$이고, $R=0$이거나 $\deg R<\deg P_{\mathfrak{a},M'}$이다.
2. $\deg P_{\mathfrak{a},M}=\max(\deg P_{\mathfrak{a},M'},\deg P_{\mathfrak{a},M''})$이다.
:::
::: 증명
$M'$을 $M$의 submodule과 identify하자. 우선 $M''/\mathfrak{a}M''$은 $M/\mathfrak{a}M$의 quotient이므로 유한한 길이를 갖고, 따라서 $\mathfrak{a}$는 $M''$의 ideal of definition이다. $M'$의 경우 [§매개계, ⁋보조정리 5](/ko/math/commutative_algebra/system_of_parameters#lem5)에 의하여 $\ann(M)\subseteq \ann(M')$이므로, $\mathfrak{a}+\ann(M')$을 포함하는 prime ideal은 $\mathfrak{a}+\ann(M)$을 포함하여 $\mathfrak{m}$과 같아야 하고, 앞서 살펴본 동치에 의하여 $\mathfrak{a}$는 $M'$의 ideal of definition이다.

이제 임의의 $n$에 대하여 $M''$으로의 quotient map은 $\mathfrak{a}^nM$을 $\mathfrak{a}^nM''$으로 보내므로 다음의 short exact sequence

$$0 \rightarrow M'/(M'\cap \mathfrak{a}^nM) \rightarrow M/\mathfrak{a}^nM \rightarrow M''/\mathfrak{a}^nM'' \rightarrow 0$$

이 존재한다. 여기서 첫 번째 map은 canonical isomorphism $(M'+\mathfrak{a}^nM)/\mathfrak{a}^nM\cong M'/(M'\cap \mathfrak{a}^nM)$을 통한 것이다. $\mathcal{J}': M_n'=M'\cap \mathfrak{a}^nM$으로 두면 이는 $M'$의 $\mathfrak{a}$-filtration이고, [§부풀림 대수, ⁋보조정리 7](/ko/math/commutative_algebra/blowup_algebra#lem7)에 의하여 $\mathfrak{a}$-stable이다. 그럼 [보조정리 3](#lem3)에 의하여 다음의 식

$$\chi_{\mathfrak{a},M}(n)=\chi_{\mathfrak{a},M''}(n)+\chi_{\mathcal{J}'}(n)$$

이 성립한다.

첫째 결과를 보이자. $R=\chi_{\mathfrak{a},M'}-\chi_{\mathcal{J}'}$로 두면 위의 식을 정리하여 $R=\chi_{\mathfrak{a},M'}+\chi_{\mathfrak{a},M''}-\chi_{\mathfrak{a},M}$을 얻는다. $\mathfrak{a}^nM'\subseteq M'\cap \mathfrak{a}^nM$이므로 $M'/\mathfrak{a}^nM'$에서 $M'/(M'\cap\mathfrak{a}^nM)$으로의 surjection이 존재하고, 따라서 $0\leq \chi_{\mathcal{J}'}(n)\leq \chi_{\mathfrak{a},M'}(n)$으로부터 $0\leq R(n)\leq \chi_{\mathfrak{a},M'}(n)$이다. 한편 [정리 8](#thm8)의 둘째 결과에 의하여 $P_{\mathcal{J}'}$는 $P_{\mathfrak{a},M'}$과 같은 degree, 같은 leading coefficient를 가지므로, 충분히 큰 $n$에서 $R$와 일치하는 numerical polynomial $P_{\mathfrak{a},M'}-P_{\mathcal{J}'}$는 $0$이거나 degree가 $\deg P_{\mathfrak{a},M'}$보다 작다.

둘째 결과를 보이자. 우선 $M''\neq 0$이므로 [§정수적 확장, ⁋보조정리 8](/ko/math/commutative_algebra/integral_extension#lem8)에 의하여 $M''/\mathfrak{a}M''\neq 0$이고, 따라서 충분히 큰 $n$에서 $\chi_{\mathfrak{a},M''}(n)\geq 1$이므로 $P_{\mathfrak{a},M''}\neq 0$이다. 또, [§부풀림 대수, ⁋따름정리 8](/ko/math/commutative_algebra/blowup_algebra#cor8)의 첫째 결과에 의하여 $(1-a)\left(\bigcap_n \mathfrak{a}^nM\right)=0$이도록 하는 $a\in \mathfrak{a}$가 존재하는데, $a\in \mathfrak{m}$이므로 $1-a$는 unit이고 따라서 $\bigcap_n \mathfrak{a}^nM=0$이다. $M'\neq 0$이므로 적당한 $n$에 대하여 $M'\not\subseteq \mathfrak{a}^nM$이고, 곧 $\chi_{\mathcal{J}'}(n)\geq 1$이므로 $P_{\mathcal{J}'}\neq 0$이다. 두 함수 $\chi_{\mathfrak{a},M''}$과 $\chi_{\mathcal{J}'}$는 감소하지 않으므로 두 다항식 $P_{\mathfrak{a},M''}$과 $P_{\mathcal{J}'}$의 leading coefficient는 양수이고, 따라서 그 합의 degree는 두 degree의 최댓값이다. 위의 길이 등식과 $\deg P_{\mathcal{J}'}=\deg P_{\mathfrak{a},M'}$을 종합하면 원하는 결과를 얻는다.
:::

::: 따름정리 12
Noetherian local ring $(A,\mathfrak{m})$과 $0$이 아닌 finitely generated $A$-module $M$, 그리고 $x\in \mathfrak{m}$에 대하여 곱하기 $x$가 $M$ 위에서 injective라 하자. 그럼 $M/xM\neq 0$이고 $d(M/xM)\leq d(M)-1$이다.
:::
::: 증명
곱하기 $x$는 isomorphism $M \rightarrow xM$을 주므로 short exact sequence

$$0 \rightarrow M \overset{x}{\longrightarrow} M \rightarrow M/xM \rightarrow 0$$

을 얻는다. 만일 $M/xM=0$이라면 $M=xM\subseteq \mathfrak{m}M$이므로 [§정수적 확장, ⁋보조정리 8](/ko/math/commutative_algebra/integral_extension#lem8)에 의하여 $M=0$이 되어 모순이다. 이제 [명제 11](#prop11)을 $\mathfrak{a}=\mathfrak{m}$에 대해 적용하자. Submodule 쪽의 module이 $M$과 isomorphic하므로 그 Hilbert-Samuel function은 $\chi_{\mathfrak{m},M}$과 같고, 따라서 [명제 11](#prop11)의 첫째 결과의 함수는 $\chi_{\mathfrak{m},M/xM}$ 자신이다. 즉 $\chi_{\mathfrak{m},M/xM}$은 충분히 큰 $n$에서 $0$이거나 degree가 $\deg P_{\mathfrak{m},M}=d(M)$보다 작은 numerical polynomial과 일치한다. $M/xM\neq 0$이므로 이 polynomial은 $0$이 아니고, 따라서 $d(M/xM)\leq d(M)-1$이다.
:::

## 차원 정리

이제 이 글의 주된 결과를 증명할 준비가 되었다.

::: 정리 13 (Dimension theorem)
Noetherian local ring $(A,\mathfrak{m})$과 $0$이 아닌 finitely generated $A$-module $M$에 대하여

$$d(M)=\dim M$$

이 성립한다.
:::
::: 증명
우선 $d(M)\leq \dim M$을 보이자. $\overline{A}=A/\ann(M)$으로 두면 [§차원, ⁋정의 2](/ko/math/commutative_algebra/Krull_dimension#def2)에 의하여 $\dim M=\dim \overline{A}$이고, $\overline{A}$는 maximal ideal $\overline{\mathfrak{m}}=\mathfrak{m}/\ann(M)$을 갖는 Noetherian local ring이다. $\delta=\dim M$이라 하면 [§매개계, ⁋따름정리 1](/ko/math/commutative_algebra/system_of_parameters#cor1)에 의하여 $\overline{\mathfrak{m}}^n\subseteq (\overline{b}_1,\ldots, \overline{b}_\delta)$가 충분히 큰 $n$에서 성립하도록 하는 $\overline{b}_1,\ldots,\overline{b}_\delta\in\overline{\mathfrak{m}}$이 존재한다. 이들을 $b_i\in \mathfrak{m}$으로 lift하고 $\mathfrak{b}=(b_1,\ldots, b_\delta)$로 두면 $\mathfrak{m}^n\subseteq \mathfrak{b}+\ann(M)$이고, 따라서 $\mathfrak{m}^nM\subseteq \mathfrak{b}M$이므로 $\mathfrak{b}$는 $\delta$개의 원소로 생성되는 $M$의 ideal of definition이다. [정리 8](#thm8)에 의하여 $d(M)=\deg P_{\mathfrak{b},M}\leq \delta=\dim M$이다.

이제 반대 방향 부등식 $\dim M\leq d(M)$을, $0$이 아닌 finitely generated module 전체에 대하여 $d(M)$에 대한 귀납법으로 보인다.

$d(M)=0$인 경우 $\chi_{\mathfrak{m},M}$은 결국 상수와 일치하므로, 충분히 큰 $n$에 대하여 $\length(\mathfrak{m}^nM/\mathfrak{m}^{n+1}M)=0$, 즉 $\mathfrak{m}^nM=\mathfrak{m}^{n+1}M$이다. $\mathfrak{m}^nM$은 finitely generated이므로 [§정수적 확장, ⁋보조정리 8](/ko/math/commutative_algebra/integral_extension#lem8)에 의하여 $\mathfrak{m}^nM=0$이고, 따라서 $\mathfrak{m}^n\subseteq \ann(M)$이다. 그럼 $\ann(M)$을 포함하는 임의의 prime ideal은 $\mathfrak{m}$을 포함하여 $\mathfrak{m}$과 같아야 하므로 $\dim M=\dim A/\ann(M)=0$이다.

이제 $d(M)=d\geq 1$이라 하고, $d(N)<d$를 만족하는 $0$이 아닌 finitely generated module $N$들에 대해서는 주장이 성립한다고 가정하자. $\dim M$은 $\ann(M)$을 포함하는 prime ideal들의 chain

$$\mathfrak{p}_r\supsetneq \mathfrak{p}_{r-1}\supsetneq\cdots\supsetneq \mathfrak{p}_0$$

의 길이 $r$들의 supremum이므로, 임의의 이러한 chain에 대하여 $r\leq d$임을 보이면 충분하다. [\[집합론\] §선택공리, ⁋정리 4](/ko/math/set_theory/axiom_of_choice#thm4)에 의하여 $\mathfrak{p}_0$에 포함되면서 $\ann(M)$을 포함하는 prime ideal 중 minimal한 것이 존재하고, 필요하다면 $\mathfrak{p}_0$를 이것으로 교체하여 chain의 길이를 줄이지 않을 수 있으므로, $\mathfrak{p}_0$가 $\ann(M)$을 포함하는 prime ideal들 중 minimal이라 가정하자. 그럼 [§동반소아이디얼, ⁋정리 7](/ko/math/commutative_algebra/associated_primes#thm7)의 첫째 결과에 의하여 $\mathfrak{p}_0\in \Ass M$이므로, 적당한 $y\in M$에 대하여 $\mathfrak{p}_0=\ann(y)$이고 $B=A/\mathfrak{p}_0$는 $M$의 submodule $Ay$와 isomorphic하다. 만일 $M=Ay$라면 $d(B)=d(M)$이고, 아니라면 [명제 11](#prop11)의 둘째 결과를 short exact sequence $0 \rightarrow Ay \rightarrow M \rightarrow M/Ay \rightarrow 0$에 적용하여 $d(B)\leq d(M)$을 얻는다.

$r=0$인 경우는 $r\leq d$가 자명하므로 $r\geq 1$이라 하자. $x\in \mathfrak{p}_1\setminus \mathfrak{p}_0$를 택하면, $B$는 integral domain이고 $x$의 image가 $0$이 아니므로 곱하기 $x$는 $B$ 위에서 injective이며, $x\in \mathfrak{p}_1\subseteq \mathfrak{m}$이다. 따라서 [따름정리 12](#cor12)에 의하여 $N=B/xB\neq 0$은 $d(N)\leq d(B)-1\leq d-1$을 만족한다. 한편 $\ann(N)=\mathfrak{p}_0+(x)$인데, 각각의 $i\geq 1$에 대하여 $\mathfrak{p}_i$는 $\mathfrak{p}_0$와 $x$를 모두 포함하므로 $\mathfrak{p}_r\supsetneq\cdots\supsetneq \mathfrak{p}_1$은 $\ann(N)$을 포함하는 prime ideal들의 길이 $r-1$의 chain이다. 귀납적 가정에 의하여

$$r-1\leq \dim N\leq d(N)\leq d-1$$

이므로 $r\leq d$이다.
:::

이로써 Noetherian local ring 위의 finitely generated module의 차원은 prime ideal chain의 길이 ([§차원, ⁋정의 2](/ko/math/commutative_algebra/Krull_dimension#def2)), system of parameters의 크기 ([§매개계, ⁋명제 6](/ko/math/commutative_algebra/system_of_parameters#prop6)), 그리고 Hilbert-Samuel polynomial의 degree라는 세 가지 서로 다른 방식으로 계산할 수 있게 되었다. 가령 [예시 10](#ex10)의 cusp의 local ring $A$는 $d(A)=1$이므로 $\dim A=1$이다.

::: 따름정리 14
Noetherian local ring 위의 $0$이 아닌 finitely generated module들의 short exact sequence $0 \rightarrow M' \rightarrow M \rightarrow M'' \rightarrow 0$에 대하여

$$\dim M=\max(\dim M',\dim M'')$$

이 성립한다.
:::
::: 증명
$\mathfrak{a}=\mathfrak{m}$으로 두면 [명제 11](#prop11)의 둘째 결과가 $d(M)=\max(d(M'), d(M''))$을 말해주고, [정리 13](#thm13)에 의하여 이는 주어진 등식과 같다.
:::

## 중복도

차원 정리는 Hilbert-Samuel polynomial의 degree를 완전히 결정한다. 그럼 이 다항식이 담고 있는 다음 정보는 leading coefficient이다.

::: 정의 15
$0$이 아닌 finitely generated $A$-module $M$과 $M$의 ideal of definition $\mathfrak{a}$에 대하여, $d=\dim M$이라 하고 $P_{\mathfrak{a},M}$의 leading coefficient를 $c$라 하자. 그럼 $M$의 $\mathfrak{a}$에 대한 *중복도<sub>multiplicity</sub>*를

$$e(\mathfrak{a};M)=c\cdot d!$$

으로 정의한다. 특별히 local ring $A$ 자신의 $\mathfrak{m}$에 대한 중복도 $e(\mathfrak{m};A)$를 간단히 $e(A)$로 적는다.
:::

즉 충분히 큰 $n$에 대하여 $\chi_{\mathfrak{a},M}(n)=(e(\mathfrak{a};M)/d!)n^d+(\text{lower order terms})$이다. [보조정리 2](#lem2)의 첫째 결과를 사용하여 $P_{\mathfrak{a},M}=\sum_k c_k\binom{\x}{k}$ ($c_k\in\mathbb{Z}$)로 적으면 leading coefficient는 $c_d/d!$이므로 $e(\mathfrak{a};M)=c_d$는 정수이다. 또 $\chi_{\mathfrak{a},M}$은 감소하지 않는 함수이고 [정리 13](#thm13)에 의하여 $\deg P_{\mathfrak{a},M}=d$이므로, $d\geq 1$이라면 leading coefficient는 양수여야 한다. $d=0$인 경우에는 [정리 13](#thm13)의 증명에서 살펴본 것처럼 충분히 큰 $n$에 대하여 $\mathfrak{a}^nM=0$이므로 $e(\mathfrak{a};M)=\length(M)$이고, 이 또한 양수이다. 즉 $e(\mathfrak{a};M)$은 언제나 양의 정수이다. 한편 degree와 달리 leading coefficient는 $\mathfrak{a}$의 선택에 의존하므로, 중복도는 pair $(\mathfrak{a}, M)$의 invariant이다.

중복도 또한 최고차항의 수준에서 additive하다.

::: 명제 16
[명제 11](#prop11)의 상황에서 $d=\dim M$이라 하자. $\dim M'=d$이면 $e'=e(\mathfrak{a};M')$, $\dim M'<d$이면 $e'=0$으로 정의하고, $e''$도 $M''$에 대하여 마찬가지로 정의하면

$$e(\mathfrak{a};M)=e'+e''$$

이 성립한다.
:::
::: 증명
[따름정리 14](#cor14)에 의하여 $\dim M'\leq d$이고 $\dim M''\leq d$이다. [명제 11](#prop11)의 첫째 결과에 의하여 $P_{\mathfrak{a},M'}+P_{\mathfrak{a},M''}-P_{\mathfrak{a},M}$은 $0$이거나 degree가 $\deg P_{\mathfrak{a},M'}=\dim M'\leq d$보다 작으므로, 어느 경우든 이 다항식의 $n^d$의 계수는 $0$이다. 한편 [정리 13](#thm13)에 의하여 $P_{\mathfrak{a},M'}$의 $n^d$의 계수는 $\dim M'=d$일 때 $e(\mathfrak{a};M')/d!$이고 $\dim M'<d$일 때 $0$이며, $P_{\mathfrak{a},M''}$에 대하여도 마찬가지이다. 따라서 $n^d$의 계수를 비교하면

$$\frac{e'}{d!}+\frac{e''}{d!}-\frac{e(\mathfrak{a};M)}{d!}=0$$

이므로 원하는 결과를 얻는다.
:::

이제 가장 기본적인 중복도 계산으로 regular local ring의 경우를 살펴보자. 다음 명제는 regular local ring이 associated graded ring의 수준에서는 polynomial ring과 정확히 같다는 것을 말해준다.

::: 명제 17
Noetherian local ring $(A,\mathfrak{m})$과 residue field $\kappa=A/\mathfrak{m}$에 대하여, 다음이 동치이다.

1. $A$는 regular local ring이다. ([§차원, ⁋정의 12](/ko/math/commutative_algebra/Krull_dimension#def12))
2. 적당한 $e\geq 0$에 대하여, 각 변수가 degree $1$을 갖는 graded ring으로서 $\gr_\mathfrak{m}A\cong \kappa[\x_1,\ldots,\x_e]$이도록 하는 graded $\kappa$-algebra isomorphism이 존재한다.

이 때 둘째 조건의 $e$는 반드시 $\dim A$와 같다.
:::
::: 증명
우선 $A$가 regular라 하고 $d=\dim A$라 하자. $d=0$인 경우 $\mathfrak{m}$은 $0$개의 원소로 생성되므로 $\mathfrak{m}=0$이고, $A=\kappa$와 $\gr_\mathfrak{m}A=\kappa$가 되어 증명할 것이 없다. 따라서 $d\geq 1$이라 하자. $\mathfrak{m}$의 generator $a_1,\ldots, a_d$를 택하고, graded $\kappa$-algebra homomorphism $\phi:\kappa[\x_1,\ldots,\x_d] \rightarrow \gr_\mathfrak{m}A$를 $\x_i\mapsto a_i+\mathfrak{m}^2$으로 정의하자. 각각의 $\mathfrak{m}^n$이 $a_i$들의 degree $n$ monomial들로 생성되므로 $\mathfrak{m}^n/\mathfrak{m}^{n+1}$은 이들의 image로 span되고, 따라서 $\phi$는 surjective이다.

$J=\ker\phi$로 두자. $\phi$가 grading을 보존하고 $\gr_\mathfrak{m}A$의 homogeneous 성분들의 합이 direct이므로, $J$의 원소의 homogeneous 성분들은 각각 $J$에 속한다. 즉 $J$는 homogeneous ideal이다. 결론에 반하여 $J\neq 0$이라 하고 $0$이 아닌 homogeneous $f\in J$를 택하자. Degree $0$에서 $\phi$는 identity $\kappa \rightarrow \kappa$이므로 $e_0=\deg f\geq 1$이다. 그럼 $\gr_\mathfrak{m}A\cong \kappa[\x_1,\ldots,\x_d]/J$는 $S=\kappa[\x_1,\ldots,\x_d]/(f)$의 quotient이므로 모든 $n$에 대하여 $H_{\gr_\mathfrak{m}A}(n)\leq H_S(n)$이다. [예시 6](#ex6)의 첫째 계산에 의하여 $d\geq 2$일 때 $H_S$는 결국 degree $d-2$의 numerical polynomial과 일치하고, $d=1$일 때는 $n\geq e_0$에서 $H_S(n)=0$이다. 한편 [정리 5](#thm5)에 의하여 $H_{\gr_\mathfrak{m}A}$ 또한 결국 numerical polynomial과 일치하는데, degree $d-2$의 다항식으로 위로 유계인 다항식은 degree가 $d-2$ 이하여야 하므로 이 polynomial은 $0$이거나 degree $d-2$ 이하이다. 그런데 위에서 살펴본 관찰에 의하여

$$\Delta\chi_{\mathfrak{m},A}(n)=\length(\mathfrak{m}^n/\mathfrak{m}^{n+1})=H_{\gr_\mathfrak{m}A}(n)$$

이므로, [보조정리 2](#lem2)의 둘째 결과에 의하여 $d(A)=\deg P_{\mathfrak{m},A}\leq d-1$이다. 이는 [정리 13](#thm13)의 $d(A)=\dim A=d$에 모순이므로 $J=0$이고, $\phi$는 isomorphism이다.

거꾸로 graded isomorphism $\gr_\mathfrak{m}A\cong \kappa[\x_1,\ldots,\x_e]$가 존재한다 하자. Degree $n$ part를 비교하면 $H_{\gr_\mathfrak{m}A}(n)=\binom{n+e-1}{e-1}$이므로, 위의 관찰과 [보조정리 2](#lem2)의 둘째 결과에 의하여 $d(A)=e$이고, [정리 13](#thm13)에 의하여 $\dim A=e$이다. 한편 degree $1$ part의 비교에서 $\mathfrak{m}/\mathfrak{m}^2$은 $e$차원 $\kappa$-벡터공간이므로, [§차원, ⁋정의 12](/ko/math/commutative_algebra/Krull_dimension#def12) 직후에 살펴본 것처럼 [§정수적 확장, ⁋보조정리 8](/ko/math/commutative_algebra/integral_extension#lem8)에 의하여 $\mathfrak{m}$은 $e=\dim A$개의 원소로 생성된다. 즉 $A$는 regular local ring이다.
:::

이 명제를 [§부풀림 대수, ⁋따름정리 11](/ko/math/commutative_algebra/blowup_algebra#cor11)과 종합하면, polynomial ring이 integral domain이므로 regular local ring이 integral domain이라는 것을 얻는다.

::: 따름정리 18
$d$차원의 regular local ring $(A,\mathfrak{m})$에 대하여, 임의의 $n\geq 1$에서

$$\chi_{\mathfrak{m},A}(n)=\binom{n+d-1}{d}$$

이 성립하며, 특히 $e(A)=1$이다.
:::
::: 증명
[명제 17](#prop17)에 의하여 모든 $n\geq 0$에 대해 $\length(\mathfrak{m}^n/\mathfrak{m}^{n+1})=\binom{n+d-1}{d-1}$이다. 이제 주어진 식을 $n$에 대한 귀납법으로 보이자. $n=1$인 경우 $\chi_{\mathfrak{m},A}(1)=\length(A/\mathfrak{m})=1=\binom{d}{d}$이다. 주어진 식이 $n$에서 성립한다면 Pascal's rule에 의하여

$$\chi_{\mathfrak{m},A}(n+1)=\chi_{\mathfrak{m},A}(n)+\binom{n+d-1}{d-1}=\binom{n+d-1}{d}+\binom{n+d-1}{d-1}=\binom{n+d}{d}$$

이므로 귀납이 완성된다. 마지막으로 $\binom{n+d-1}{d}$는 $n$에 대한 degree $d$의 다항식으로 leading coefficient가 $1/d!$이므로 $e(A)=d!\cdot(1/d!)=1$이다.
:::

[예시 10](#ex10)의 cusp로 돌아가자. 그 곳에서 계산한 $\chi_{\mathfrak{m},A}(n)=2n-1$과 $\dim A=1$로부터 $e(A)=1!\cdot 2=2$이다. 기하적으로 이 값은 원점을 지나는 일반적인 직선이 곡선 $\y^2=\x^3$과 원점에서 이중으로 만난다는 사실을 반영한다. 실제로 직선 $\y=t\x$를 대입하면 $\x^2(t^2-\x)=0$이 되어 교점의 방정식이 원점에서 정확히 이중근을 갖는다. 특히 $e(A)=2\neq 1$이므로 [따름정리 18](#cor18)에 의하여 $A$는 regular local ring이 아니며, 이는 원점이 이 곡선의 singular point라는 사실과 부합한다.

---

**참고문헌**

**[AM]** M. F. Atiyah, I. G. Macdonald. *Introduction to Commutative Algebra*. Addison-Wesley, 1969.  
**[Eis]** David Eisenbud. *Commutative Algebra: with a view toward algebraic geometry*. Springer, 1995.

---
