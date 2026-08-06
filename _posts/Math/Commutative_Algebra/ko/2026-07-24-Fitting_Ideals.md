---
title: "Fitting 아이디얼"
description: "유한 표시 행렬의 소행렬식이 이루는 아이디얼이 모듈의 불변량이라는 Fitting의 보조정리를 증명하고, base change와 소멸자, 자유성 판정으로 응용한다."
excerpt: "Fitting ideal의 정의와 표시 독립성, 자유성 판정"

categories: [Math / Commutative Algebra]
permalink: /ko/math/commutative_algebra/fitting_ideals
sidebar: 
    nav: "commutative_algebra-ko"

date: 2026-07-24
weight: 29
published: false
drift_needed: true

---

임의의 finitely generated $A$-module $M$은 유한한 generator와 그 사이의 relation이 주어지는 presentation을 가지며, 이 자료는 두 free module 사이의 하나의 $A$-linear map $\varphi$로 압축된다. 이 글의 출발점은 $\varphi$를 행렬로 적었을 때 그 소행렬식들이 생성하는 ideal이 presentation의 선택에 전혀 의존하지 않는다는 관찰이다. 앞선 글에서 free resolution이 담는 정보가 그 길이에 그치지 않으며 resolution을 이루는 행렬 자체를 정밀하게 읽어내는 도구가 필요하다고 예고하였는데, 그 도구가 바로 이 ideal이다. 우리는 이를 Fitting ideal로 정의하고 presentation의 선택에 대한 독립성을 증명한 뒤, base change와 annihilator, 그리고 free module 판정으로 그 쓰임을 살펴본다.

## Finite presentation과 소행렬식 아이디얼

Noetherian ring $A$ 위에서 finitely generated $A$-module은 언제나 finitely presented이므로 ([§기본 개념들, ⁋명제 9](/ko/math/commutative_algebra/basic_notions#prop9)), $M$은 적당한 free module들 사이의 exact sequence

$$A^m\overset{\varphi}{\longrightarrow}A^n\longrightarrow M\longrightarrow 0$$

을 presentation으로 가진다. 여기서 $A^n\to M$의 상은 $M$의 $n$개의 generator를 주고, $\varphi$의 상은 이 generator들 사이의 relation 전체를 이룬다. 우리는 $\varphi$를 표준 basis에 대한 $n\times m$ 행렬로 보고 ([\[다중선형대수학\] §행렬과 선형사상, ⁋정의 1](/ko/math/multilinear_algebra/matrices_and_linear_maps#def1)), 이 행렬의 소행렬식을 다룬다.

::: 정의 1
Free module 사이의 $A$-linear map $\varphi:A^m\to A^n$과 정수 $r$에 대하여, $\varphi$의 *ideal of minors* $I_r(\varphi)$를 다음과 같이 정의한다. $\varphi$를 표준 basis에 대한 $n\times m$ 행렬로 볼 때, $1\le r\le\min(m,n)$이면 $I_r(\varphi)$는 $\varphi$의 모든 $r\times r$ 소행렬식으로 생성되는 $A$의 ideal이고, $r\le 0$이면 $I_r(\varphi)=A$, $r>\min(m,n)$이면 $I_r(\varphi)=0$으로 둔다.
:::

여기서 $r\times r$ 소행렬식이란 $\varphi$의 행렬에서 $r$개의 행과 $r$개의 열을 골라 만든 부분행렬의 행렬식을 뜻한다 ([\[다중선형대수학\] §행렬식, ⁋보조정리 4](/ko/math/multilinear_algebra/determinants#lem4)). 관례 $I_0(\varphi)=A$는 빈 부분행렬의 행렬식을 $1$로 본 것이고, 행이나 열의 수보다 큰 크기의 부분행렬은 존재하지 않으므로 $r>\min(m,n)$에서 $I_r(\varphi)=0$이다. 또한 각각의 $r$에 대하여

$$I_{r+1}(\varphi)\subseteq I_r(\varphi)$$

가 성립한다. 행렬식은 각 행에 대하여 multilinear이고 두 행이 같으면 $0$이 되므로, $(r+1)\times(r+1)$ 부분행렬의 행렬식을 한 행에 대하여 전개하면 그 행의 성분들과 $r\times r$ 소행렬식들의 곱의 합이 되어 $I_r(\varphi)$에 속하기 때문이다.

이제 module의 불변량이 될 대상을 정의한다.

::: 정의 2
Finitely presented $A$-module $M$이 presentation $A^m\overset{\varphi}{\to}A^n\to M\to0$을 가질 때, 각각의 정수 $i\ge0$에 대하여 $M$의 *$i$번째 Fitting ideal*을

$$\operatorname{Fitt}_i(M)=I_{n-i}(\varphi)$$

로 정의한다.
:::

정의를 그대로 따르면 $\operatorname{Fitt}_i(M)=I_{n-i}(\varphi)$이므로, $i\ge n$에서는 $n-i\le0$이 되어 $\operatorname{Fitt}_i(M)=A$이고, 소행렬식 ideal의 포함관계 $I_{r+1}\subseteq I_r$로부터

$$\operatorname{Fitt}_0(M)\subseteq\operatorname{Fitt}_1(M)\subseteq\cdots\subseteq\operatorname{Fitt}_n(M)=A$$

인 상승하는 사슬을 얻는다. 이 정의는 겉보기에 presentation $\varphi$에 의존하지만, 다음 정리가 그렇지 않음을 보인다. 이것이 이론 전체의 초석이다.

::: 정리 3 (Fitting)
Finitely presented $A$-module $M$의 Fitting ideal $\operatorname{Fitt}_i(M)$은 $M$의 presentation의 선택에 의존하지 않는다.
:::
::: 증명
두 presentation이 같은 generating set에서 오는 경우를 먼저 다룬다. Surjection $\pi:A^n\to M$을 고정하고 $R=\ker\pi$라 하자. 상이 $R$인 두 $A$-linear map $\varphi:A^m\to A^n$, $\varphi':A^{m'}\to A^n$에 대하여 $I_{n-i}(\varphi)=I_{n-i}(\varphi')$임을 보인다.

우선 한 열을 덧붙이는 연산을 살펴본다. $\varphi$의 열들을 $c_1,\ldots,c_m\in A^n$이라 하고, $v\in\operatorname{im}\varphi$인 열 $v$를 오른쪽에 덧붙여 얻은 $n\times(m+1)$ 행렬을 $[\varphi\mid v]$라 하자. $\varphi$의 소행렬식은 $[\varphi\mid v]$의 소행렬식이기도 하므로 $I_r(\varphi)\subseteq I_r([\varphi\mid v])$이다. 거꾸로 $[\varphi\mid v]$의 $r\times r$ 소행렬식을 하나 고정하자. 이 소행렬식이 마지막 열 $v$를 쓰지 않으면 이는 $\varphi$의 소행렬식이다. $v$를 쓰는 경우, $v=\sum_k a_kc_k$로 적고 $v$가 놓인 열에 대한 행렬식의 multilinearity를 쓰면 이 소행렬식은 $v$를 $c_k$로 바꾼 소행렬식들에 $a_k$를 곱해 더한 것이 된다. $c_k$가 이미 선택된 다른 열에 나타나면 그 항은 두 열이 같아 $0$이고, 그렇지 않으면 $\varphi$의 $r\times r$ 소행렬식에 부호를 붙인 것이다. 어느 경우든 그 값은 $I_r(\varphi)$에 속하므로 $I_r([\varphi\mid v])\subseteq I_r(\varphi)$, 곧 $I_r([\varphi\mid v])=I_r(\varphi)$이다.

이제 $\varphi'$의 각 열은 $R=\operatorname{im}\varphi$에 속하므로, 이들을 하나씩 $\varphi$에 덧붙이면 $I_r([\varphi\mid\varphi'])=I_r(\varphi)$이고, 같은 논증을 $\varphi'$에 대해 반복하면 $I_r([\varphi\mid\varphi'])=I_r(\varphi')$이다. 따라서 모든 $r$에 대하여 $I_r(\varphi)=I_r(\varphi')$이다.

다음으로 generator를 하나 늘리는 경우를 다룬다. presentation $A^m\overset{\varphi}{\to}A^n\to M\to0$의 generator를 $g_1,\ldots,g_n$이라 하고, $g_{n+1}=\sum_ib_ig_i\in M$을 새 generator로 추가하자. 새 generating set $g_1,\ldots,g_{n+1}$에 대한 relation은 옛 relation $(c,0)$ (단 $c\in R$)들과 $(b_1,\ldots,b_n,-1)$로 생성된다. 실제로 $(a_1,\ldots,a_{n+1})$이 relation이면 $g_{n+1}=\sum b_ig_i$를 대입하여 $\sum_{i\le n}(a_i+a_{n+1}b_i)g_i=0$이므로 $(a_1+a_{n+1}b_1,\ldots,a_n+a_{n+1}b_n)\in R$이고,

$$(a_1,\ldots,a_{n+1})=(a_1+a_{n+1}b_1,\ldots,a_n+a_{n+1}b_n,0)-a_{n+1}(b_1,\ldots,b_n,-1)$$

이기 때문이다. 그러므로

$$\varphi'=\begin{pmatrix}\varphi&b\\0&-1\end{pmatrix}$$

은 새 generating set에 대한 $M$의 presentation이다. 여기서 마지막 행에 $b_i$배를 곱해 $i$번째 행에 더하는 elementary row 연산을 차례로 적용하면, 이 연산은 행렬식의 multilinearity와 alternating 성질에 의하여 모든 $I_r$를 보존하며 $\varphi'$를

$$\begin{pmatrix}\varphi&0\\0&-1\end{pmatrix}$$

로 바꾼다. 이 블록 행렬의 $\big((n+1)-i\big)\times\big((n+1)-i\big)$ 소행렬식을 생각하자. 마지막 행과 마지막 열은 오른쪽 아래 성분에만 $-1$을 갖고 나머지는 $0$이다. 소행렬식이 마지막 행과 마지막 열을 모두 포함하면 그 행에 대해 전개하여 $-1$ 곱하기 $\varphi$의 $\big(n-i\big)\times\big(n-i\big)$ 소행렬식을 얻고, 마지막 행만 또는 마지막 열만 포함하면 그 행 혹은 열이 $0$이 되어 소행렬식이 $0$이며, 둘 다 포함하지 않으면 $\varphi$의 $\big((n+1)-i\big)\times\big((n+1)-i\big)$ 소행렬식이다. 따라서

$$I_{(n+1)-i}(\varphi')=I_{n-i}(\varphi)+I_{(n+1)-i}(\varphi)=I_{n-i}(\varphi)$$

이고, 마지막 등호는 $I_{(n+1)-i}(\varphi)\subseteq I_{n-i}(\varphi)$에 의한 것이다. 곧 새 generating set으로 계산한 $\operatorname{Fitt}_i$가 처음의 것과 같다.

마지막으로 임의의 두 presentation을 비교한다. 두 presentation의 generating set을 각각 $G$, $G'$이라 하자. $G'$의 원소들은 $M$의 원소이므로 $G$의 generator들로 표현되며, 이들을 하나씩 $G$에 추가하여 합집합 $G\cup G'$에 이르는 각 단계에서, 방금 보인 결과에 의하여 $\operatorname{Fitt}_i$가 변하지 않는다. 각 단계에서 어떤 relation 행렬을 택하든 그 값이 같다는 것은 첫 부분에서 보장되므로, $G$로 계산한 $\operatorname{Fitt}_i(M)$은 $G\cup G'$로 계산한 것과 같다. 마찬가지로 $G'$로 계산한 것과도 같으므로, 두 presentation은 같은 Fitting ideal을 준다.
:::

가장 익숙한 예로 finitely generated abelian group에서 Fitting ideal을 계산해 본다.

::: 예시 4
$A=\mathbb{Z}$이고 $d_1\mid d_2\mid d_3$인 양의 정수들에 대하여

$$M=\mathbb{Z}/d_1\mathbb{Z}\oplus\mathbb{Z}/d_2\mathbb{Z}\oplus\mathbb{Z}/d_3\mathbb{Z}$$

를 생각하자. 대각 행렬 $\varphi=\operatorname{diag}(d_1,d_2,d_3):\mathbb{Z}^3\to\mathbb{Z}^3$은 $M$의 presentation을 주며, 여기서 $n=3$이다. 대각 행렬의 $2\times2$ 부분행렬은 고른 행의 집합과 열의 집합이 일치할 때에만 두 대각 성분의 곱을 행렬식으로 갖고 그 외에는 성분에 $0$을 포함하므로, $I_2(\varphi)=(d_1d_2,d_1d_3,d_2d_3)$이다. $d_1\mid d_2\mid d_3$이므로 $d_1d_2$가 나머지 둘을 나누어 $I_2(\varphi)=(d_1d_2)$이며, 같은 방식으로 $I_1(\varphi)=(d_1,d_2,d_3)=(d_1)$이고 $I_3(\varphi)=(d_1d_2d_3)$이다. 따라서

$$\operatorname{Fitt}_0(M)=(d_1d_2d_3),\quad\operatorname{Fitt}_1(M)=(d_1d_2),\quad\operatorname{Fitt}_2(M)=(d_1),\quad\operatorname{Fitt}_3(M)=\mathbb{Z}$$

를 얻는다. 각 Fitting ideal의 generator의 연속한 비 $d_1$, $d_1d_2/d_1$, $d_1d_2d_3/(d_1d_2)$는 정확히 $M$의 구조를 결정하는 invariant factor $d_1,d_2,d_3$이다. Fitting ideal이 presentation과 무관한 이 불변량을 복원한다는 사실은 [정리 3](#thm3)을 구체적으로 확인해 준다.
:::

## Fitting 아이디얼의 성질

[정리 3](#thm3)에 의하여 Fitting ideal은 임의의 presentation으로 계산해도 되므로, 이를 활용하여 세 가지 성질을 얻는다. 첫째는 ring을 바꾸는 조작과의 호환성이다.

::: 명제 5
Ring homomorphism $A\to B$와 finitely presented $A$-module $M$에 대하여

$$\operatorname{Fitt}_i(M\otimes_AB)=\operatorname{Fitt}_i(M)B$$

가 성립한다. 여기서 우변은 $\operatorname{Fitt}_i(M)$이 $B$에서 생성하는 ideal이다.
:::
::: 증명
$M$의 presentation $A^m\overset{\varphi}{\to}A^n\to M\to0$에 $B\otimes_A-$를 적용하면, tensor product가 right exact이므로 ([\[다중선형대수학\] §사영가군, 단사가군, 평탄가군, ⁋명제 6](/ko/math/multilinear_algebra/various_modules#prop6)) exact sequence

$$B^m\overset{\varphi_B}{\longrightarrow}B^n\longrightarrow M\otimes_AB\longrightarrow0$$

을 얻는다. 이는 $B$-module $M\otimes_AB$의 presentation이며, $\varphi_B$의 행렬은 $\varphi$의 행렬의 각 성분을 $A\to B$로 보낸 것이다. 소행렬식은 성분들의 다항식이고 $A\to B$가 ring homomorphism이므로, $\varphi_B$의 $r\times r$ 소행렬식은 $\varphi$의 대응하는 소행렬식의 image이다. 따라서 $I_r(\varphi_B)$는 $I_r(\varphi)$의 generator들의 image로 생성되는 $B$의 ideal, 곧 $I_r(\varphi)B$이고,

$$\operatorname{Fitt}_i(M\otimes_AB)=I_{n-i}(\varphi_B)=I_{n-i}(\varphi)B=\operatorname{Fitt}_i(M)B$$

이다.
:::

특히 multiplicative subset $S\subseteq A$에 대하여 $S^{-1}M\cong S^{-1}A\otimes_AM$이므로 ([§국소화의 성질들, ⁋보조정리 1](/ko/math/commutative_algebra/properties_of_localization#lem1)), [명제 5](#prop5)를 $B=S^{-1}A$에 적용하면 $\operatorname{Fitt}_i(S^{-1}M)=S^{-1}(\operatorname{Fitt}_i(M))$을 얻는다. 곧 Fitting ideal의 형성은 localization과 교환하며, 이 사실은 뒤에서 국소적 판정과 대역적 판정을 잇는 다리가 된다.

둘째 성질은 $\operatorname{Fitt}_0$과 annihilator의 관계이다.

::: 명제 6
$n$개의 원소로 생성되는 finitely presented $A$-module $M$에 대하여

$$\ann(M)^n\subseteq\operatorname{Fitt}_0(M)\subseteq\ann(M)$$

이 성립한다.
:::
::: 증명
$M$의 presentation $A^m\overset{\varphi}{\to}A^n\to M\to0$을 generator $g_1,\ldots,g_n$과 함께 고정하자. $\operatorname{Fitt}_0(M)=I_n(\varphi)$는 $\varphi$의 $n$개의 열을 골라 만든 $n\times n$ 부분행렬 $\psi$들의 행렬식으로 생성된다.

먼저 $\operatorname{Fitt}_0(M)\subseteq\ann(M)$을 보인다. 이러한 $\psi=(\psi_{il})$의 각 열은 $\varphi$의 열, 곧 relation이므로 각각의 $l$에서 $\sum_i\psi_{il}g_i=0$이다. 행벡터 $g=(g_1,\ldots,g_n)$으로 적으면 이는 $g\psi=0$을 뜻한다. Commutative ring 위의 정사각행렬 $\psi$에 대하여 $\psi\operatorname{adj}(\psi)=(\det\psi)I$를 만족하는 수반행렬<sub>adjugate</sub> $\operatorname{adj}(\psi)$이 존재하므로 ([\[다중선형대수학\] §행렬식, ⁋명제 9](/ko/math/multilinear_algebra/determinants#prop9)의 증명에서 이 항등식을 확인하였다), 오른쪽에 $\operatorname{adj}(\psi)$를 곱하면

$$0=g\psi\operatorname{adj}(\psi)=(\det\psi)g$$

이다. 곧 각각의 $i$에서 $(\det\psi)g_i=0$이고, $g_i$들이 $M$을 생성하므로 $\det\psi\in\ann(M)$이다. 이러한 $\det\psi$들이 $\operatorname{Fitt}_0(M)$을 생성하므로 $\operatorname{Fitt}_0(M)\subseteq\ann(M)$이다.

이제 $\ann(M)^n\subseteq\operatorname{Fitt}_0(M)$을 보인다. $a_1,\ldots,a_n\in\ann(M)$을 택하면 각각의 $j$에서 $a_jg_j=0$이므로 $a_je_j\in A^n$은 $A^n\to M$의 kernel, 곧 $\operatorname{im}\varphi$에 속한다. 따라서 $a_je_j$는 $\varphi$의 열 $c_1,\ldots,c_m$의 $A$-linear combination이다. $\bigwedge^n(A^n)$에서

$$(a_1e_1)\wedge\cdots\wedge(a_ne_n)=a_1\cdots a_n(e_1\wedge\cdots\wedge e_n)$$

인데, 좌변의 각 $a_je_j$를 $c_k$들의 조합으로 전개하면 이는 $c_{k_1}\wedge\cdots\wedge c_{k_n}$ 꼴의 항들의 $A$-linear combination이 되고, [\[다중선형대수학\] §행렬식, ⁋보조정리 4](/ko/math/multilinear_algebra/determinants#lem4)에 의하여 각 항은 $\varphi$의 $n\times n$ 소행렬식에 $e_1\wedge\cdots\wedge e_n$을 곱한 것이다. 두 표현의 $e_1\wedge\cdots\wedge e_n$ 계수를 비교하면 $a_1\cdots a_n\in I_n(\varphi)=\operatorname{Fitt}_0(M)$이다. 이러한 곱들이 $\ann(M)^n$을 생성하므로 $\ann(M)^n\subseteq\operatorname{Fitt}_0(M)$이다.
:::

두 포함관계에 radical을 취하고 $\sqrt{\ann(M)^n}=\sqrt{\ann(M)}$임을 쓰면 $\sqrt{\operatorname{Fitt}_0(M)}=\sqrt{\ann(M)}$을 얻는다. 곧 $\operatorname{Fitt}_0(M)$은 annihilator와 같은 radical을 가지므로, radical의 수준에서 $M$이 소멸하는 자리를 그대로 기억한다.

셋째 성질은 local ring에서 generator의 개수를 읽어내는 것이다.

::: 명제 7
Noetherian local ring $(A,\mathfrak{m},\kappa)$ 위의 finitely generated $A$-module $M$에 대하여 $\mu(M)=\dim_\kappa(M/\mathfrak{m}M)$이라 하면, 각각의 $i\ge0$에서

$$\operatorname{Fitt}_i(M)=A\iff i\ge\mu(M)$$

이 성립한다. 곧 $\mu(M)=\min\{i\mid\operatorname{Fitt}_i(M)=A\}$이다.
:::
::: 증명
$\mu=\mu(M)$이라 하자. [§정수적 확장, ⁋보조정리 8](/ko/math/commutative_algebra/integral_extension#lem8)에 의하여 $M/\mathfrak{m}M$의 $\kappa$-basis로 image가 내려가는 원소들 $x_1,\ldots,x_\mu$은 $M$의 최소 생성 집합을 이루며, [§호몰로지 차원, ⁋명제 9](/ko/math/commutative_algebra/homological_dimension#prop9)가 주는 minimal free resolution의 첫 두 항을 떼면 presentation

$$A^s\overset{\varphi}{\longrightarrow}A^\mu\longrightarrow M\longrightarrow0$$

을 얻는다. Minimal이라는 것은 $\varphi$의 상이 $\mathfrak{m}A^\mu$에 포함된다는 것이므로 ([§호몰로지 차원, ⁋정의 8](/ko/math/commutative_algebra/homological_dimension#def8)), $\varphi$의 모든 성분이 $\mathfrak{m}$에 속한다. 여기서 $n=\mu$이다.

$i\ge\mu$이면 $\operatorname{Fitt}_i(M)=I_{\mu-i}(\varphi)$이고 $\mu-i\le0$이므로 $\operatorname{Fitt}_i(M)=A$이다. $i<\mu$이면 $\operatorname{Fitt}_i(M)=I_{\mu-i}(\varphi)$이고 $\mu-i\ge1$인데, $\varphi$의 성분이 모두 $\mathfrak{m}$에 속하므로 $(\mu-i)\times(\mu-i)$ 소행렬식은 $\mathfrak{m}$의 원소들의 곱의 합, 곧 $\mathfrak{m}$의 원소이다. 따라서 $\operatorname{Fitt}_i(M)\subseteq\mathfrak{m}\subsetneq A$이다. 종합하면 $\operatorname{Fitt}_i(M)=A$인 것은 $i\ge\mu$인 것과 동치이다.
:::

이 판정은 localization을 통해 일반적인 Noetherian ring으로 옮겨진다. Finitely generated $M$과 prime ideal $\mathfrak{p}$에 대하여 $\operatorname{Fitt}_i(M)_\mathfrak{p}=\operatorname{Fitt}_i(M_\mathfrak{p})$이므로 ([명제 5](#prop5)), $\operatorname{Fitt}_i(M)\not\subseteq\mathfrak{p}$인 것은 $\operatorname{Fitt}_i(M_\mathfrak{p})=A_\mathfrak{p}$인 것, 곧 [명제 7](#prop7)에 의하여 $M_\mathfrak{p}$가 $i$개 이하의 원소로 생성되는 것과 동치이다. 따라서 $M_\mathfrak{p}$의 최소 generating set의 크기 $\mu(M_\mathfrak{p})$는 $\operatorname{Fitt}_i(M)\not\subseteq\mathfrak{p}$를 만족하는 가장 작은 $i$로 읽힌다.

같은 판정의 극단은 $M$이 free module인 경우이다. 이때 Fitting ideal의 두 항만으로 자유성과 그 rank가 결정된다.

::: 정리 8
Noetherian local ring $(A,\mathfrak{m})$ 위의 finitely generated $A$-module $M$과 정수 $r\ge1$에 대하여 다음이 동치이다.

1. $M$은 rank $r$의 free module이다.
2. $\operatorname{Fitt}_{r-1}(M)=0$이고 $\operatorname{Fitt}_r(M)=A$이다.
:::
::: 증명
첫째 조건을 가정하자. $M\cong A^r$이면 relation이 없는 presentation $A^0\overset{\varphi}{\to}A^r\to M\to0$을 가지며, $\varphi$는 열이 없는 행렬이다. 따라서 $1\times1$ 소행렬식이 없어 $\operatorname{Fitt}_{r-1}(M)=I_1(\varphi)=0$이고, $\operatorname{Fitt}_r(M)=I_0(\varphi)=A$이다.

둘째 조건을 가정하자. $\operatorname{Fitt}_r(M)=A$이므로 [명제 7](#prop7)에 의하여 $\mu(M)\le r$이고, $\operatorname{Fitt}_{r-1}(M)=0\ne A$이므로 같은 명제에 의하여 $r-1<\mu(M)$, 곧 $\mu(M)\ge r$이다. 따라서 $\mu(M)=r$이며, minimal free resolution의 첫 두 항이 주는 presentation $A^s\overset{\varphi}{\to}A^r\to M\to0$은 성분이 모두 $\mathfrak{m}$에 속하는 $\varphi$를 갖는다. 그런데

$$\operatorname{Fitt}_{r-1}(M)=I_{r-(r-1)}(\varphi)=I_1(\varphi)=0$$

이고 $I_1(\varphi)$은 $\varphi$의 모든 성분으로 생성되므로 $\varphi=0$이다. 그럼 $M\cong A^r/\operatorname{im}\varphi=A^r$이 되어 $M$은 rank $r$의 free module이다.
:::

일반적인 Noetherian ring $A$에 대해서도 [명제 5](#prop5)의 localization 형태와 [정리 8](#thm8)을 결합하면 대역적인 판정을 얻는다. Finitely generated $M$에 대하여 $\operatorname{Fitt}_j(M)_\mathfrak{p}=\operatorname{Fitt}_j(M_\mathfrak{p})$이므로, $\operatorname{Fitt}_{r-1}(M)=0$은 모든 maximal ideal $\mathfrak{m}$에서 $\operatorname{Fitt}_{r-1}(M_\mathfrak{m})=0$인 것과 동치이고 ([§국소화의 성질들, ⁋보조정리 3](/ko/math/commutative_algebra/properties_of_localization#lem3)), $\operatorname{Fitt}_r(M)=A$는 모든 maximal ideal $\mathfrak{m}$에서 $\operatorname{Fitt}_r(M)\not\subseteq\mathfrak{m}$인 것, 곧 $\operatorname{Fitt}_r(M_\mathfrak{m})=A_\mathfrak{m}$인 것과 동치이다. 따라서 이 두 조건은 모든 maximal ideal $\mathfrak{m}$에서 $M_\mathfrak{m}$가 rank $r$의 free module인 것과 동치이며, $M$이 국소적으로 rank $r$의 free module임을 판정한다.

$r=1$인 경우가 특히 중요하다. $\operatorname{Fitt}_0(M)=0$이고 $\operatorname{Fitt}_1(M)=A$인 finitely generated module $M$은 모든 maximal ideal에서 rank $1$의 free module, 곧 $M_\mathfrak{m}\cong A_\mathfrak{m}$을 만족하므로 [§분수아이디얼, ⁋정의 1](/ko/math/commutative_algebra/fractional_ideals#def1)의 invertible module이고, 거꾸로 invertible module은 이 두 조건을 만족한다. 이렇게 Fitting ideal은 invertible module을 국소적 자유성의 판정으로 곧바로 특징짓는다.

::: 예시 9
1. $A=\mathbb{K}[[\x,\y]]$의 maximal ideal $\mathfrak{m}=(\x,\y)$를 $A$-module로 보자. [§Auslander-Buchsbaum 공식, ⁋예시 6](/ko/math/commutative_algebra/auslander_buchsbaum_formula#ex6)에서 살펴본 presentation

    $$A\overset{\varphi}{\longrightarrow}A^2\longrightarrow\mathfrak{m}\longrightarrow0,\qquad\varphi(1)=(-\y,\x)$$

    에서 $\varphi$는 $2\times1$ 행렬이므로 $2\times2$ 소행렬식이 없어 $\operatorname{Fitt}_0(\mathfrak{m})=I_2(\varphi)=0$이고, $\operatorname{Fitt}_1(\mathfrak{m})=I_1(\varphi)=(-\y,\x)=\mathfrak{m}$이다. $\operatorname{Fitt}_1(\mathfrak{m})=\mathfrak{m}\ne A$이므로 [명제 7](#prop7)에 의하여 $\mu(\mathfrak{m})\ge2$이고, 따라서 $\mathfrak{m}$은 [정리 8](#thm8)에 의하여 rank $1$의 free module이 아니다. 곧 Fitting ideal은 $2$차원 regular local ring의 maximal ideal이 principal ideal이 아니라는 사실을 즉시 감지한다.

2. $B=\mathbb{K}[\x]$ 위에서 두 module $M=B/(\x^2)$과 $M'=B/(\x)\oplus B/(\x)$을 비교하자. presentation $B\overset{\x^2}{\to}B\to M\to0$에서 $\operatorname{Fitt}_0(M)=(\x^2)$이고 $\operatorname{Fitt}_1(M)=I_0(\varphi)=B$이다. 한편 presentation $B^2\overset{\operatorname{diag}(\x,\x)}{\longrightarrow}B^2\to M'\to0$에서 $\operatorname{Fitt}_0(M')=I_2=(\x^2)$이고 $\operatorname{Fitt}_1(M')=I_1=(\x)$이다. 두 module은 같은 $\operatorname{Fitt}_0=(\x^2)$을 갖지만 $\operatorname{Fitt}_1$이 각각 $B$와 $(\x)$로 달라, Fitting ideal의 전체 열이 이 두 length $2$ module의 구조를 구별한다.
:::

Free resolution의 각 행렬에서 뽑은 소행렬식 ideal의 depth가 그 complex의 exactness 자체를 판정한다는 Buchsbaum--Eisenbud 정리가 이 방법의 다음 장을 이룬다.

---

**참고문헌**

**[Eis]** David Eisenbud. *Commutative Algebra: with a view toward algebraic geometry*. Springer, 1995.  
**[Mat]** Hideyuki Matsumura. *Commutative Ring Theory*. Cambridge University Press, 1986.  
**[Stacks]** The Stacks Project Authors. *The Stacks Project*. [https://stacks.math.columbia.edu](https://stacks.math.columbia.edu).

---
