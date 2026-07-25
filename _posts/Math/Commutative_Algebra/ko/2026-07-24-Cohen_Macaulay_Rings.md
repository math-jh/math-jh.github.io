---
title: "Cohen-Macaulay 환"
description: "Noetherian local ring 위에서 depth와 차원이 일치하는 Cohen-Macaulay 가군을 정의하고, system of parameters가 regular sequence를 이룬다는 특성화와 localization·차원 공식·catenary 성질, 그리고 매개계 아이디얼의 중복도가 길이와 일치함을 다룬다."
excerpt: "Depth와 차원이 일치하는 Cohen-Macaulay 환과 그 특성화"

categories: [Math / Commutative Algebra]
permalink: /ko/math/commutative_algebra/cohen_macaulay_rings
sidebar: 
    nav: "commutative_algebra-ko"

date: 2026-07-24
weight: 25
published: false
drift_needed: true

---

[§Depth](/ko/math/commutative_algebra/depth)에서 우리는 Noetherian local ring 위의 finitely generated module에 대하여 항상 $\operatorname{depth}M\leq \dim M$이 성립함을 보았고 ([§Depth, ⁋따름정리 8](/ko/math/commutative_algebra/depth#cor8)), 이 부등식에서 등호가 성립하는 대상을 Cohen--Macaulay라 이름 붙였다. 이 개념은 depth라는 대수적 불변량과 차원이라는 기하적 불변량이 정확히 맞아떨어지는, 다시 말해 module이 그 support의 모든 방향에서 균질하게 두꺼운 상황을 포착한다. 이 글에서는 Cohen--Macaulay module을 정식으로 정의하고, 이 조건이 system of parameters가 곧 regular sequence라는 사실과 동치임을 보인 뒤, 여기에서 따라오는 localization에 대한 안정성과 차원 공식, catenary 성질을 살펴본다. 마지막으로 이 이론이 중복도의 계산에서 어떻게 나타나는지를 다룬다.

## Cohen-Macaulay 가군

이 글 전체에서 $(A,\mathfrak{m})$은 Noetherian local ring이고, 특별한 언급이 없는 한 $M$은 $0$이 아닌 finitely generated $A$-module이다. [§Depth, ⁋따름정리 8](/ko/math/commutative_algebra/depth#cor8)의 부등식에서 등호가 성립하는 경우를 다음과 같이 이름 붙인다.

::: 정의 1
Noetherian local ring $(A,\mathfrak{m})$ 위의 $0$이 아닌 finitely generated $A$-module $M$이 *Cohen--Macaulay module*이라는 것은

$$\operatorname{depth}M=\dim M$$

이 성립하는 것이다. Ring $A$가 자기 자신 위의 module로서 Cohen--Macaulay일 때 $A$를 *Cohen--Macaulay local ring*이라 부른다.
:::

[§Depth, ⁋따름정리 8](/ko/math/commutative_algebra/depth#cor8)에 의하여 언제나 $\operatorname{depth}M\leq \dim M$이므로, Cohen--Macaulay 조건은 depth가 취할 수 있는 가장 큰 값에 도달한다는 것이다. 가장 단순한 예로 $\dim M=0$인 module은 $\operatorname{depth}M=0$이므로 항상 Cohen--Macaulay이며, 특히 $0$차원 Noetherian local ring은 언제나 Cohen--Macaulay local ring이다. 반대편 극단에서, 뒤에서 보겠지만 regular local ring도 Cohen--Macaulay이다. Cohen--Macaulay 조건이 실패하는 것은 module의 서로 다른 성분이 서로 다른 차원을 가질 때인데, 이를 다음 명제가 정확하게 표현한다.

::: 명제 2
$M$이 Cohen--Macaulay module이면 임의의 $\mathfrak{p}\in \Ass M$에 대하여 $\dim A/\mathfrak{p}=\dim M$이 성립한다. 특히 $M$의 associated prime은 모두 $\ann M$을 포함하는 minimal prime이며, $M$은 minimal이 아닌 associated prime, 곧 *embedded prime*을 갖지 않는다.
:::
::: 증명
$\mathfrak{p}\in \Ass M$이라 하자. [§Depth, ⁋따름정리 8](/ko/math/commutative_algebra/depth#cor8)에 의하여 $\operatorname{depth}M\leq \dim A/\mathfrak{p}$이고, 한편 $\mathfrak{p}\supseteq \ann M$이므로 $A/\mathfrak{p}$는 $A/\ann M$의 quotient가 되어 $\dim A/\mathfrak{p}\leq \dim A/\ann M=\dim M$이다. ([§차원, ⁋정의 2](/ko/math/commutative_algebra/Krull_dimension#def2)) $M$이 Cohen--Macaulay이므로 이 둘을 종합하면

$$\dim M=\operatorname{depth}M\leq \dim A/\mathfrak{p}\leq \dim M$$

이 되어 $\dim A/\mathfrak{p}=\dim M$을 얻는다. 이제 모든 associated prime $\mathfrak{p}$가 $\dim A/\mathfrak{p}=\dim M$을 만족하므로, 만일 $\mathfrak{p}\subsetneq \mathfrak{p}'$인 두 associated prime이 있다면 $\mathfrak{p}$에서 시작하는 chain의 앞에 $\mathfrak{p}'$을 끼워넣어 $\dim A/\mathfrak{p}\geq 1+\dim A/\mathfrak{p}'$을 얻는데, 이는 두 값이 같다는 것에 모순이다. 따라서 $\Ass M$의 원소들은 서로 포함관계가 없고, 특히 [§동반소아이디얼, ⁋정리 7](/ko/math/commutative_algebra/associated_primes#thm7)에서 $\ann M$을 포함하는 minimal prime들이 모두 $\Ass M$에 속하므로 $\Ass M$은 정확히 이 minimal prime들로 이루어진다.
:::

이 성질을 흔히 *unmixedness*라 부른다. Cohen--Macaulay module은 그 associated prime들이 전부 같은 차원을 갖는다는 점에서 차원의 관점에서 균질하다. 다음 명제는 Cohen--Macaulay 조건이 non-zerodivisor에 대한 quotient에 대해 잘 보존된다는 것을 말해주며, 앞으로의 귀납법에서 핵심적인 역할을 한다.

::: 명제 3
$M$이 $0$이 아닌 finitely generated $A$-module이고, 곱하기 $x$가 $M$ 위에서 injective인 $x\in \mathfrak{m}$이 주어졌다 하자. 그럼 $M$이 Cohen--Macaulay인 것과 $M/xM$이 Cohen--Macaulay인 것이 동치이다.
:::
::: 증명
[§Depth, ⁋명제 9](/ko/math/commutative_algebra/depth#prop9)에 의하여 $M/xM\neq 0$이고

$$\operatorname{depth}(M/xM)=\operatorname{depth}M-1,\qquad \dim(M/xM)=\dim M-1$$

이 성립한다. 따라서 $\operatorname{depth}M=\dim M$인 것과 $\operatorname{depth}(M/xM)=\dim(M/xM)$인 것이 동치이다.
:::

Cohen--Macaulay 조건은 depth와 차원이라는 서로 다른 두 언어로 정의되었지만, [§매개계](/ko/math/commutative_algebra/system_of_parameters)의 system of parameters를 통해 하나의 단일한 조건으로 다시 쓸 수 있다. 다음 정리가 이 글의 핵심이다.

::: 정리 4
$M$이 $0$이 아닌 finitely generated $A$-module이고 $\dim M=d$라 하자. 그럼 다음이 모두 동치이다.

1. $M$은 Cohen--Macaulay이다.
2. $M$의 어떤 system of parameters가 $M$-sequence이다.
3. $M$의 모든 system of parameters가 $M$-sequence이다.
:::
::: 증명
세 번째 조건이 두 번째 조건을 함의하는 것은 system of parameters가 언제나 존재하므로 자명하다. ([§매개계, ⁋명제 6](/ko/math/commutative_algebra/system_of_parameters#prop6))

두 번째 조건이 첫 번째 조건을 함의함을 보이자. $M$의 어떤 system of parameters $x_1,\ldots, x_d\in \mathfrak{m}$이 $M$-sequence라 하자. 이는 $\mathfrak{m}$ 안에 놓인 길이 $d$의 $M$-sequence이므로, 이를 maximal한 것으로 연장하면 $\operatorname{depth}M\geq d$이다. 한편 [§Depth, ⁋따름정리 8](/ko/math/commutative_algebra/depth#cor8)에 의하여 $\operatorname{depth}M\leq \dim M=d$이므로 $\operatorname{depth}M=d=\dim M$, 곧 $M$은 Cohen--Macaulay이다.

이제 첫 번째 조건이 세 번째 조건을 함의함을 $d=\dim M$에 대한 귀납법으로 보인다. $d=0$인 경우 system of parameters는 빈 sequence이므로 자명하게 $M$-sequence이다. 이제 $d\geq 1$이라 하고 주장이 차원 $d-1$의 Cohen--Macaulay module에 대해 성립한다고 가정하자. $x_1,\ldots, x_d$가 $M$의 임의의 system of parameters라 하자.

먼저 $x_1$이 $M$-regular임을 보인다. 결론에 반하여 $x_1$이 $M$의 zerodivisor라 하면, [§동반소아이디얼, ⁋정리 7](/ko/math/commutative_algebra/associated_primes#thm7)에 의하여 $x_1\in \mathfrak{p}$인 $\mathfrak{p}\in \Ass M$이 존재한다. [명제 2](#prop2)에 의하여 $\dim A/\mathfrak{p}=d$이다. $\mathfrak{p}\in \Ass M$이므로 $\mathfrak{p}=\ann(m)$인 $m\in M$이 존재하는데, $s\in A\setminus \mathfrak{p}$이면 $sm\neq 0$이라 $M_\mathfrak{p}$에서 $m/1\neq 0$이고 따라서 $M_\mathfrak{p}\neq 0$이다. $x_1\in \mathfrak{p}A_\mathfrak{p}$이므로 [§정수적 확장, ⁋보조정리 8](/ko/math/commutative_algebra/integral_extension#lem8)에 의하여 $M_\mathfrak{p}/x_1M_\mathfrak{p}\neq 0$이다. [§국소화의 성질들, ⁋명제 2](/ko/math/commutative_algebra/properties_of_localization#prop2)에 의하여 localization은 exact하므로 $(M/x_1M)_\mathfrak{p}=M_\mathfrak{p}/x_1M_\mathfrak{p}\neq 0$이다. 만일 $\ann(M/x_1M)\not\subseteq \mathfrak{p}$이면 어떤 $a\in \ann(M/x_1M)$이 $A_\mathfrak{p}$에서 unit이 되어 $(M/x_1M)_\mathfrak{p}=0$이 되므로, $\ann(M/x_1M)\subseteq \mathfrak{p}$이고, 따라서

$$\dim (M/x_1M)\geq \dim A/\mathfrak{p}=d$$

이다. 그런데 $x_2,\ldots, x_d$는 $M/x_1M$을 유한한 길이로 만들므로 [§매개계, ⁋명제 6](/ko/math/commutative_algebra/system_of_parameters#prop6)에 의하여 $\dim(M/x_1M)\leq d-1$이 되어 모순이다. 그러므로 $x_1$은 $M$-regular이다.

그럼 [명제 3](#prop3)에 의하여 $M/x_1M$은 Cohen--Macaulay이고, [§Depth, ⁋명제 9](/ko/math/commutative_algebra/depth#prop9)에 의하여 $\dim(M/x_1M)=d-1$이다. 또, $x_2,\ldots, x_d$가 $M/x_1M$을 유한한 길이로 만들고 이는 $d-1$개의 원소이므로 $M/x_1M$의 system of parameters이다. 귀납적 가정에 의하여 $x_2,\ldots, x_d$는 $M/x_1M$-sequence이며, $x_1$이 $M$-regular인 것과 종합하면 $x_1,\ldots, x_d$는 $M$-sequence이다.
:::

이 정리는 regular local ring이 Cohen--Macaulay라는 사실을 즉시 준다.

::: 따름정리 5
Regular local ring은 Cohen--Macaulay local ring이다.
:::
::: 증명
Regular local ring $(A,\mathfrak{m})$의 regular system of parameters는 [§정칙국소환, ⁋따름정리 3](/ko/math/commutative_algebra/regular_local_rings#cor3)에 의하여 $A$-sequence를 이룬다. 이는 $A$의 어떤 system of parameters가 $A$-sequence라는 것이므로 [정리 4](#thm4)에 의하여 $A$는 Cohen--Macaulay이다.
:::

[§정칙국소환, ⁋명제 4](/ko/math/commutative_algebra/regular_local_rings#prop4)의 증명에서는 $d$차원 Noetherian local ring이 $\mathfrak{m}$ 안에 $d$개의 원소로 이루어진 $A$-sequence를 가질 때 이를 Cohen--Macaulay local ring이라 불렀는데, [정리 4](#thm4)는 이 임시 정의가 [정의 1](#def1)과 동치임을 해명한다. 실제로 $\mathfrak{m}$ 안에 길이 $d=\dim A$의 $A$-sequence가 있으면 $\operatorname{depth}A\geq d$이고 [§Depth, ⁋따름정리 8](/ko/math/commutative_algebra/depth#cor8)과 종합하여 $\operatorname{depth}A=d=\dim A$이므로 [정의 1](#def1)의 의미에서 Cohen--Macaulay이며, 거꾸로 Cohen--Macaulay local ring은 [정리 4](#thm4)에 의하여 임의의 system of parameters, 곧 $d$개의 원소로 이루어진 $A$-sequence를 $\mathfrak{m}$ 안에 갖기 때문이다.

또, Cohen--Macaulay 조건은 regular sequence에 대한 quotient로 내려간다.

::: 따름정리 6
$A$가 Cohen--Macaulay local ring이고 $x_1,\ldots, x_r\in \mathfrak{m}$이 $A$-sequence이면, $A/(x_1,\ldots, x_r)$는 Cohen--Macaulay local ring이다.
:::
::: 증명
$r$에 대한 귀납법으로 [명제 3](#prop3)을 반복 적용한다. $x_1$은 $A$-regular이므로 곱하기 $x_1$이 $A$ 위에서 injective이고, [명제 3](#prop3)에 의하여 $A/x_1A$는 Cohen--Macaulay이다. $x_2,\ldots, x_r$은 $A/x_1A$-sequence이므로 $\overline{x}_2$가 $A/x_1A$ 위에서 injective이고, 같은 논증을 반복하면 $A/(x_1,\ldots, x_r)$가 Cohen--Macaulay임을 얻는다.
:::

특히 regular local ring $(A,\mathfrak{m})$은 [§정칙국소환, ⁋따름정리 1](/ko/math/commutative_algebra/regular_local_rings#cor1)에 의하여 integral domain이므로, $0$이 아닌 non-unit $f\in \mathfrak{m}$은 항상 $A$-regular이고, 따라서 hypersurface $A/(f)$는 [따름정리 6](#cor6)에 의하여 Cohen--Macaulay이다. 가령 formal power series ring $\mathbb{K}[[\x_1,\ldots,\x_n]]$을 $0$이 아닌 non-unit $f$ 하나로 나눈 $\mathbb{K}[[\x_1,\ldots,\x_n]]/(f)$는 언제나 Cohen--Macaulay local ring이다.

다음 예시들은 Cohen--Macaulay 조건이 실패하는 전형적인 상황과, 낮은 차원에서 이 조건이 어떻게 단순해지는지를 보여준다.

::: 예시 7
1. [§Depth, ⁋예시 11](/ko/math/commutative_algebra/depth#ex11)에서 살펴본 $A=\mathbb{K}[[\x,\y,\z]]/(\x\z,\y\z)$는 차원 $2$의 평면과 차원 $1$의 직선을 합친 것의 국소적 모형으로, $\operatorname{depth}A=1<2=\dim A$이므로 Cohen--Macaulay가 아니다. 서로 다른 차원의 두 성분이 붙어 있어 [명제 2](#prop2)의 unmixedness가 실패하는데, 실제로 저차원 성분이 주는 associated prime $(\x,\y)A$는 $\dim A/(\x,\y)A=1\neq 2$을 만족한다.
2. $A=\mathbb{K}[[\x,\y]]/(\x^2,\x\y)$를 생각하자. $(\x^2,\x\y)=\x(\x,\y)$를 포함하는 minimal prime은 $(\x)$ 하나뿐이므로 $A$의 nilradical은 $(\overline{\x})$이고, $A/(\overline{\x})\cong \mathbb{K}[[\y]]$이므로 $\dim A=1$이다. 한편 $A$에서 $\overline{\x}\neq 0$이면서 $\mathfrak{m}\overline{\x}=0$인데, 이는 $\x\cdot\x=\x^2=0$이고 $\y\cdot\x=\x\y=0$이기 때문이다. 따라서 $\ann_A(\overline{\x})=\mathfrak{m}$이 되어 $\mathfrak{m}\in \Ass A$이고, [§Depth, ⁋따름정리 4](/ko/math/commutative_algebra/depth#cor4)에 의하여 $\operatorname{depth}A=0<1=\dim A$이므로 $A$는 Cohen--Macaulay가 아니다. 이 경우 $\mathfrak{m}$이 embedded prime으로 등장하여 [명제 2](#prop2)의 unmixedness가 직접 실패한다.
3. $0$차원 Noetherian local ring은 $\operatorname{depth}A=\dim A=0$이므로 언제나 Cohen--Macaulay이다.
4. $1$차원 Noetherian local ring $(A,\mathfrak{m})$이 Cohen--Macaulay인 것은 $\operatorname{depth}A=1$인 것, 곧 $\operatorname{depth}A\geq 1$인 것과 동치이다. [§Depth, ⁋따름정리 4](/ko/math/commutative_algebra/depth#cor4)에 의하여 이는 다시 $\mathfrak{m}\notin \Ass A$인 것, 즉 $A$가 $\mathfrak{m}$을 embedded prime으로 갖지 않는 것과 동치이다.
:::

## Localization과 차원 공식

Cohen--Macaulay 조건은 localization에 대해 안정적이며, 이로부터 차원에 관한 깔끔한 공식이 따라온다. 그 출발점은 depth를 codimension으로 표현하는 다음 보조정리이다. Prime ideal $\mathfrak{p}$에 대하여 $\operatorname{depth}_\mathfrak{p}(A)$는 $\mathfrak{p}$ 안에 놓인 maximal $A$-sequence의 공통의 길이를 뜻하며, 이는 [§Depth, ⁋정리 2](/ko/math/commutative_algebra/depth#thm2)에 의하여 잘 정의된다.

::: 보조정리 8
$A$가 Cohen--Macaulay local ring이면 임의의 $\mathfrak{p}\in \Spec A$에 대하여 $\operatorname{depth}_\mathfrak{p}(A)=\codim \mathfrak{p}$이다.
:::
::: 증명
먼저 $\operatorname{depth}_\mathfrak{p}(A)\leq \codim \mathfrak{p}$를 보인다. $x_1,\ldots, x_r$이 $\mathfrak{p}$ 안의 maximal $A$-sequence라 하자. 각각의 $x_{i+1}$이 $A/(x_1,\ldots, x_i)$ 위에서 non-zerodivisor이므로, 곱하기 $x_{i+1}$이 이 module 위에서 injective이고, [§국소화의 성질들, ⁋명제 2](/ko/math/commutative_algebra/properties_of_localization#prop2)에 의하여 localization은 injectivity를 보존하므로 $x_{i+1}$은 $A_\mathfrak{p}/(x_1,\ldots, x_i)A_\mathfrak{p}$ 위에서도 non-zerodivisor이다. $(x_1,\ldots, x_r)A_\mathfrak{p}\subseteq \mathfrak{p}A_\mathfrak{p}\neq A_\mathfrak{p}$이므로 $x_1,\ldots, x_r$은 $\mathfrak{p}A_\mathfrak{p}$ 안의 $A_\mathfrak{p}$-sequence이다. 따라서 [§Depth, ⁋따름정리 8](/ko/math/commutative_algebra/depth#cor8)에 의하여

$$\operatorname{depth}_\mathfrak{p}(A)=r\leq \operatorname{depth}(A_\mathfrak{p})\leq \dim A_\mathfrak{p}=\codim \mathfrak{p}$$

이다.

반대 부등식 $\operatorname{depth}_\mathfrak{p}(A)\geq \codim \mathfrak{p}$를 $\codim \mathfrak{p}$에 대한 귀납법으로 보인다. $\codim \mathfrak{p}=0$이면 $\mathfrak{p}$는 minimal prime이므로 [§동반소아이디얼, ⁋정리 7](/ko/math/commutative_algebra/associated_primes#thm7)에 의하여 $\mathfrak{p}\in \Ass A$이고, [§Depth, ⁋따름정리 4](/ko/math/commutative_algebra/depth#cor4)에 의하여 $\operatorname{depth}_\mathfrak{p}(A)=0=\codim \mathfrak{p}$이다. 이제 $\codim \mathfrak{p}\geq 1$이라 하자. [명제 2](#prop2)에 의하여 $\Ass A$의 원소는 모두 minimal prime이고, $\mathfrak{p}$는 codimension이 $1$ 이상이라 minimal이 아니므로 어떠한 associated prime에도 포함되지 않는다. $\Ass A$는 유한집합이므로 ([§동반소아이디얼, ⁋정리 7](/ko/math/commutative_algebra/associated_primes#thm7)), [§동반소아이디얼, ⁋보조정리 2](/ko/math/commutative_algebra/associated_primes#lem2)에 의하여 어떠한 associated prime에도 속하지 않는 $x\in \mathfrak{p}$을 택할 수 있고, 이러한 $x$는 $A$-regular이다. [따름정리 6](#cor6)에 의하여 $A/xA$는 Cohen--Macaulay이다. 한편 $x/1$은 $A_\mathfrak{p}$ 위에서 non-zerodivisor이고 $x/1\in \mathfrak{p}A_\mathfrak{p}$이므로 [§Depth, ⁋명제 9](/ko/math/commutative_algebra/depth#prop9)를 local ring $A_\mathfrak{p}$에 적용하면

$$\codim_{A/xA}(\mathfrak{p}/xA)=\dim (A_\mathfrak{p}/xA_\mathfrak{p})=\dim A_\mathfrak{p}-1=\codim \mathfrak{p}-1$$

을 얻는다. 귀납적 가정을 Cohen--Macaulay local ring $A/xA$와 그 prime $\mathfrak{p}/xA$에 적용하면 $\operatorname{depth}_{\mathfrak{p}/xA}(A/xA)=\codim \mathfrak{p}-1$이므로, $\mathfrak{p}/xA$ 안의 길이 $\codim \mathfrak{p}-1$의 $A/xA$-sequence를 $\mathfrak{p}$ 안의 원소들로 lift하면 $x$와 함께 $\mathfrak{p}$ 안의 길이 $\codim \mathfrak{p}$의 $A$-sequence를 이룬다. 따라서 $\operatorname{depth}_\mathfrak{p}(A)\geq \codim \mathfrak{p}$이다.
:::

이 보조정리로부터 localization에 대한 안정성과 차원 공식이 함께 따라온다.

::: 정리 9
$A$가 Cohen--Macaulay local ring이면 다음이 성립한다.

1. 임의의 $\mathfrak{p}\in \Spec A$에 대하여 $A_\mathfrak{p}$는 Cohen--Macaulay local ring이다.
2. 임의의 $\mathfrak{p}\in \Spec A$에 대하여 $\dim A/\mathfrak{p}+\codim \mathfrak{p}=\dim A$이다.
:::
::: 증명
첫째 결과의 경우, [보조정리 8](#lem8)에 의하여 $\mathfrak{p}$ 안에 길이 $\codim \mathfrak{p}$의 $A$-sequence가 존재하고, 이는 [보조정리 8](#lem8)의 증명에서 살펴본 것처럼 $\mathfrak{p}A_\mathfrak{p}$ 안의 $A_\mathfrak{p}$-sequence로 localize된다. 따라서 $\operatorname{depth}(A_\mathfrak{p})\geq \codim \mathfrak{p}=\dim A_\mathfrak{p}$이고, [§Depth, ⁋따름정리 8](/ko/math/commutative_algebra/depth#cor8)의 반대 부등식과 종합하면 $\operatorname{depth}(A_\mathfrak{p})=\dim A_\mathfrak{p}$, 곧 $A_\mathfrak{p}$는 Cohen--Macaulay이다.

둘째 결과를 $\codim \mathfrak{p}$에 대한 귀납법으로 보인다. $\codim \mathfrak{p}=0$이면 $\mathfrak{p}$는 minimal prime이므로 [명제 2](#prop2)에 의하여 $\dim A/\mathfrak{p}=\dim A$이고, 주어진 등식이 성립한다. 이제 $\codim \mathfrak{p}\geq 1$이라 하자. [보조정리 8](#lem8)의 증명에서와 같이 $A$-regular $x\in \mathfrak{p}$을 택하면 $A/xA$는 Cohen--Macaulay이고, [§Depth, ⁋명제 9](/ko/math/commutative_algebra/depth#prop9)에 의하여 $\dim A/xA=\dim A-1$이며, 앞서 계산한 것처럼 $\codim_{A/xA}(\mathfrak{p}/xA)=\codim \mathfrak{p}-1$이다. 한편 $x\in \mathfrak{p}$이므로 $(A/xA)/(\mathfrak{p}/xA)\cong A/\mathfrak{p}$이다. 귀납적 가정을 $A/xA$와 $\mathfrak{p}/xA$에 적용하면

$$\dim A/\mathfrak{p}+(\codim \mathfrak{p}-1)=\dim A/xA=\dim A-1$$

이므로 $\dim A/\mathfrak{p}+\codim \mathfrak{p}=\dim A$를 얻는다.
:::

[정리 9](#thm9)의 둘째 결과는 [§정칙국소환, ⁋명제 4](/ko/math/commutative_algebra/regular_local_rings#prop4)에서 regular local ring에 대해 증명한 차원 공식 $\dim A/\mathfrak{p}+\codim \mathfrak{p}=\dim A$이 실은 Cohen--Macaulay local ring 전체로 확장된다는 것을 보여준다. 이 공식은 prime ideal들의 chain의 길이에 대한 강한 통제로 이어진다. 이를 정확히 서술하기 위해 다음을 정의한다.

::: 정의 10
Ring $A$가 *catenary*라는 것은, $A$의 임의의 두 prime ideal $\mathfrak{p}\subseteq \mathfrak{q}$에 대하여 $\mathfrak{p}$와 $\mathfrak{q}$ 사이의 saturated chain, 곧 어느 두 항 사이에도 새로운 prime ideal을 끼워넣을 수 없는 chain들이 모두 같은 유한한 길이를 갖는 것이다.
:::

일반적으로 Noetherian ring이라도 서로 다른 saturated chain이 다른 길이를 가질 수 있다. Cohen--Macaulay 조건은 [정리 9](#thm9)의 차원 공식을 통해 이러한 병리를 배제한다.

::: 따름정리 11
Cohen--Macaulay local ring $A$는 catenary이며, prime ideal $\mathfrak{p}\subseteq \mathfrak{q}$ 사이의 임의의 saturated chain의 길이는 $\codim \mathfrak{q}-\codim \mathfrak{p}$이다.
:::
::: 증명
우선 인접한 두 prime, 즉 $\mathfrak{p}'\subsetneq \mathfrak{p}''$이면서 그 사이에 다른 prime ideal이 없는 경우에 $\codim \mathfrak{p}''=\codim \mathfrak{p}'+1$임을 보인다. [정리 9](#thm9)의 첫째 결과에 의하여 $A_{\mathfrak{p}''}$는 Cohen--Macaulay local ring이고, [§국소화, ⁋명제 8](/ko/math/commutative_algebra/localization#prop8)에 의하여 $\mathfrak{p}'A_{\mathfrak{p}''}$는 그 prime ideal이며 $\codim(\mathfrak{p}'A_{\mathfrak{p}''})=\codim \mathfrak{p}'$이다. [정리 9](#thm9)의 둘째 결과를 Cohen--Macaulay local ring $A_{\mathfrak{p}''}$와 그 prime $\mathfrak{p}'A_{\mathfrak{p}''}$에 적용하면

$$\dim (A_{\mathfrak{p}''}/\mathfrak{p}'A_{\mathfrak{p}''})+\codim \mathfrak{p}'=\dim A_{\mathfrak{p}''}=\codim \mathfrak{p}''$$

이다. 그런데 $\mathfrak{p}'\subsetneq \mathfrak{p}''$ 사이에 다른 prime이 없으므로 $A_{\mathfrak{p}''}/\mathfrak{p}'A_{\mathfrak{p}''}$의 prime ideal은 $0$과 maximal ideal 뿐이고, 따라서 $\dim (A_{\mathfrak{p}''}/\mathfrak{p}'A_{\mathfrak{p}''})=1$이다. 이로부터 $\codim \mathfrak{p}''=\codim \mathfrak{p}'+1$을 얻는다.

이제 $\mathfrak{p}=\mathfrak{p}_0\subsetneq \mathfrak{p}_1\subsetneq \cdots\subsetneq \mathfrak{p}_n=\mathfrak{q}$이 saturated chain이라 하면 각 인접한 항에서 codimension이 정확히 $1$씩 증가하므로

$$\codim \mathfrak{q}-\codim \mathfrak{p}=\sum_{i=0}^{n-1}(\codim \mathfrak{p}_{i+1}-\codim \mathfrak{p}_i)=n$$

이다. 이 값은 chain의 선택에 의존하지 않고 $\codim \mathfrak{q}\leq \dim A$로 유계이므로 $A$는 catenary이다.
:::

## 매개계 아이디얼의 중복도

[§힐베르트-사무엘 함수](/ko/math/commutative_algebra/hilbert-samuel_function)에서 우리는 $M$의 ideal of definition $\mathfrak{a}$에 대한 Hilbert-Samuel function $\chi_{\mathfrak{a},M}(n)=\length(M/\mathfrak{a}^nM)$과 그 leading coefficient가 담고 있는 중복도 $e(\mathfrak{a};M)$을 정의하였고 ([§힐베르트-사무엘 함수, ⁋정의 7](/ko/math/commutative_algebra/hilbert-samuel_function#def7), [§힐베르트-사무엘 함수, ⁋정의 15](/ko/math/commutative_algebra/hilbert-samuel_function#def15)), regular local ring이 associated graded ring의 수준에서 polynomial ring과 일치함을 보았다. ([§힐베르트-사무엘 함수, ⁋명제 17](/ko/math/commutative_algebra/hilbert-samuel_function#prop17)) Cohen--Macaulay local ring에서는 이 현상이 임의의 parameter ideal로 확장되어, associated graded ring이 다시 polynomial ring이 되고 중복도가 길이와 정확히 일치한다. 그 핵심은 regular sequence가 만들어내는 associated graded ring을 계산하는 다음 명제이다.

::: 명제 12
Noetherian local ring $(A,\mathfrak{m})$과 $A$-sequence $x_1,\ldots, x_d$가 주어졌다 하고 $\mathfrak{q}=(x_1,\ldots, x_d)$라 하자. 그럼 $x_i+\mathfrak{q}^2$로의 대응이 유도하는 graded $(A/\mathfrak{q})$-algebra homomorphism

$$\varphi: (A/\mathfrak{q})[X_1,\ldots, X_d] \rightarrow \gr_\mathfrak{q}A=\bigoplus_{n\geq 0}\mathfrak{q}^n/\mathfrak{q}^{n+1}$$

은 isomorphism이다. ([§부풀림 대수, ⁋정의 1](/ko/math/commutative_algebra/blowup_algebra#def1))
:::
::: 증명
각각의 $\mathfrak{q}^n/\mathfrak{q}^{n+1}$은 $x_i$들의 degree $n$ monomial들의 image로 생성되므로 $\varphi$는 surjective이다. 따라서 각 degree에서 injectivity를 보이면 충분하며, 이는 다음 명제로 정리된다.

$(\ast)$ 각 $n$에 대하여, $a_I\in A$ ($\lvert I\rvert=n$)가 $\sum_{\lvert I\rvert=n}a_Ix^I\in \mathfrak{q}^{n+1}$을 만족하면 모든 $a_I\in \mathfrak{q}$이다.

여기서 $I=(i_1,\ldots, i_d)$는 $\lvert I\rvert=i_1+\cdots+i_d$인 multi-index이고 $x^I=x_1^{i_1}\cdots x_d^{i_d}$이다. 우선 $(\ast)$를 다음의 동차 관계식에 대한 주장으로 환원한다.

$(\ast\ast)$ 각 $n$에 대하여, $a_I\in A$ ($\lvert I\rvert=n$)가 $\sum_{\lvert I\rvert=n}a_Ix^I=0$을 만족하면 모든 $a_I\in \mathfrak{q}$이다.

$(\ast\ast)$를 가정하고 $(\ast)$를 보이자. $\sum_{\lvert I\rvert=n}a_Ix^I\in \mathfrak{q}^{n+1}$이면 이를 $\sum_{j=1}^d x_jg_j$의 꼴로 적을 수 있는데, 여기서 각 $g_j\in \mathfrak{q}^n$은 $g_j=\sum_{\lvert L\rvert=n}d_{L,j}x^L$로 쓸 수 있다. 그럼

$$\sum_{\lvert I\rvert=n}a_Ix^I-\sum_{\lvert I\rvert=n}\Big(\sum_{j=1}^d d_{I,j}x_j\Big)x^I=0$$

이므로 $(\ast\ast)$에 의하여 각 $a_I-\sum_j d_{I,j}x_j\in \mathfrak{q}$이고, $\sum_j d_{I,j}x_j\in \mathfrak{q}$이므로 $a_I\in \mathfrak{q}$이다.

이제 $(\ast\ast)$를 $d$에 대한 귀납법으로 증명한다. $d=1$인 경우, $x_1$은 non-zerodivisor이므로 $ax_1^n=0$이면 $a=0\in \mathfrak{q}$이다.

$d\geq 2$라 하고 주장이 $A$-sequence $x_1,\ldots, x_{d-1}$에 대해 성립한다고 가정하자. $\mathfrak{q}'=(x_1,\ldots, x_{d-1})$로 두면 $x_1,\ldots, x_{d-1}$은 $A$-sequence이고 $x_d$는 $A/\mathfrak{q}'$ 위에서 non-zerodivisor이다. ([§정칙국소환, ⁋정의 2](/ko/math/commutative_algebra/regular_local_rings#def2)) 주어진 관계식을 $x_d$의 거듭제곱으로 묶어

$$\sum_{e=0}^{n}P_ex_d^e=0,\qquad P_e=\sum_{\lvert I'\rvert=n-e}a_{I',e}x'^{I'}$$

로 적자. 여기서 $I'=(i_1,\ldots, i_{d-1})$이고 $x'^{I'}=x_1^{i_1}\cdots x_{d-1}^{i_{d-1}}$이며, $P_e$는 $x_1,\ldots, x_{d-1}$에 대한 degree $n-e$의 동차식이므로 $P_e\in (\mathfrak{q}')^{n-e}$이다. 관계식에 실제로 나타나는 $x_d$의 top power, 곧 어떤 $a_{I',l}$이 $0$이 아닌 가장 큰 $l$을 잡자. $e>l$이면 $a_{I',e}$가 모두 $0$이라 이미 $\mathfrak{q}$에 속하므로, $e\leq l$인 $a_{I',e}$가 모두 $\mathfrak{q}$에 속함을 $l$에 대한 귀납법으로 보이면 된다.

$l=0$인 경우, 관계식은 $\sum_{\lvert I'\rvert=n}a_{I',0}x'^{I'}=0$이고 이는 $x_1,\ldots, x_{d-1}$에 대한 동차 관계식이므로, $d$에 대한 귀납적 가정으로부터 모든 $a_{I',0}\in \mathfrak{q}'\subseteq \mathfrak{q}$이다.

$l\geq 1$이라 하고 top power가 $l-1$ 이하인 관계식에 대해 주장이 성립한다고 가정하자. 먼저 최고차항의 계수 $a_{I',l}$이 $\mathfrak{q}'$에 속함을 보인다. $e\leq l-1$이면 $P_e\in (\mathfrak{q}')^{n-e}\subseteq (\mathfrak{q}')^{n-l+1}$이므로

$$x_d^lP_l=-\sum_{e=0}^{l-1}P_ex_d^e\in (\mathfrak{q}')^{n-l+1}$$

이다. 즉 $\sum_{\lvert I'\rvert=n-l}(x_d^la_{I',l})x'^{I'}\in (\mathfrak{q}')^{n-l+1}$인데, $x_1,\ldots, x_{d-1}$에 대한 $(\ast\ast)$가 $d$에 대한 귀납적 가정이고 앞서 보인 환원에 의하여 이들에 대한 $(\ast)$ 또한 성립하므로 (즉 $\gr_{\mathfrak{q}'}A$의 degree $n-l$ 부분에서 monomial들이 $A/\mathfrak{q}'$-일차독립이므로), 각 계수 $x_d^la_{I',l}\in \mathfrak{q}'$이다. $x_d$가 $A/\mathfrak{q}'$ 위에서 non-zerodivisor이므로 $x_d^l$도 그러하고, 따라서 $a_{I',l}\in \mathfrak{q}'$이다.

이제 $a_{I',l}\in \mathfrak{q}'$이므로 $P_l=\sum_{\lvert I'\rvert=n-l}a_{I',l}x'^{I'}$을 $x_1,\ldots, x_{d-1}$의 degree $n-l+1$ 동차식 $P_l=\sum_{\lvert H\rvert=n-l+1}b_Hx'^H$으로 다시 적을 수 있다. 그럼 $x_d^lP_l=x_d^{l-1}\sum_{\lvert H\rvert=n-l+1}(x_db_H)x'^H$이므로, 원래의 관계식은

$$\sum_{e=0}^{l-2}P_ex_d^e+\Big(P_{l-1}+\sum_{\lvert H\rvert=n-l+1}(x_db_H)x'^H\Big)x_d^{l-1}=0$$

이 되어 top power가 $l-1$ 이하인 관계식이 된다. 이 관계식에서 $x_d^{l-1}$의 계수는 degree $n-l+1$의 동차식이고 나머지 계수 $P_e$ ($e\leq l-2$)도 각각 degree $n-e$의 동차식이므로, $l$에 대한 귀납적 가정을 적용할 수 있다. 따라서 이 관계식의 모든 계수가 $\mathfrak{q}$에 속하는데, 특히 $x_d^{l-1}$의 계수에서 $a_{H,l-1}+x_db_H\in \mathfrak{q}$이므로 $a_{H,l-1}\in \mathfrak{q}$이고, $e\leq l-2$에 대해서도 $a_{I',e}\in \mathfrak{q}$이다. 앞서 보인 $a_{I',l}\in \mathfrak{q}'\subseteq \mathfrak{q}$과 종합하면 모든 계수가 $\mathfrak{q}$에 속한다.
:::

이 명제를 Cohen--Macaulay local ring에 적용하면 parameter ideal의 Hilbert-Samuel function과 중복도가 완전히 결정된다.

::: 따름정리 13
$A$가 $d$차원 Cohen--Macaulay local ring이고 $\mathfrak{q}$가 임의의 parameter ideal이면, 모든 $n\geq 1$에 대하여

$$\chi_{\mathfrak{q},A}(n)=\length(A/\mathfrak{q})\binom{n+d-1}{d}$$

이 성립하며, 특히 $e(\mathfrak{q};A)=\length(A/\mathfrak{q})$이다.
:::
::: 증명
$\mathfrak{q}$는 $\dim A=d$개의 원소로 이루어진 system of parameters $x_1,\ldots, x_d$로 생성되며, [정리 4](#thm4)에 의하여 이들은 $A$-sequence이다. 따라서 [명제 12](#prop12)에 의하여 $\gr_\mathfrak{q}A\cong (A/\mathfrak{q})[X_1,\ldots, X_d]$이다. Degree $k$ 부분을 비교하면 $\mathfrak{q}^k/\mathfrak{q}^{k+1}$은 degree $k$ monomial들을 basis로 갖는 자유 $(A/\mathfrak{q})$-module이고, 그 monomial의 개수는 중복조합의 수 $\binom{k+d-1}{d-1}$이다. ([§힐베르트-사무엘 함수, ⁋예시 6](/ko/math/commutative_algebra/hilbert-samuel_function#ex6)) 길이가 direct sum에 대해 additive하므로 ([§힐베르트-사무엘 함수, ⁋보조정리 3](/ko/math/commutative_algebra/hilbert-samuel_function#lem3))

$$\length(\mathfrak{q}^k/\mathfrak{q}^{k+1})=\binom{k+d-1}{d-1}\length(A/\mathfrak{q})$$

이다. 이제 $\chi_{\mathfrak{q},A}(n)=\length(A/\mathfrak{q}^n)=\sum_{k=0}^{n-1}\length(\mathfrak{q}^k/\mathfrak{q}^{k+1})$이므로 ([§힐베르트-사무엘 함수, ⁋정의 7](/ko/math/commutative_algebra/hilbert-samuel_function#def7)), Pascal's rule을 반복하여 얻어지는 등식 $\sum_{k=0}^{n-1}\binom{k+d-1}{d-1}=\binom{n+d-1}{d}$과 종합하면

$$\chi_{\mathfrak{q},A}(n)=\length(A/\mathfrak{q})\binom{n+d-1}{d}$$

을 얻는다. 우변은 $n$에 대한 degree $d$의 다항식으로 leading coefficient가 $\length(A/\mathfrak{q})/d!$이므로, [§힐베르트-사무엘 함수, ⁋정의 15](/ko/math/commutative_algebra/hilbert-samuel_function#def15)에 의하여 $e(\mathfrak{q};A)=(\length(A/\mathfrak{q})/d!)\cdot d!=\length(A/\mathfrak{q})$이다.
:::

따라서 Cohen--Macaulay local ring에서는 parameter ideal의 중복도가 $\length(A/\mathfrak{q})$라는 순수하게 계량적인 양으로 주어진다. 다음 예시는 이 등식과, Cohen--Macaulay 조건이 실패할 때 나타나는 격차를 함께 보여준다.

::: 예시 14
Field $\mathbb{K}$에 대하여 $A=\mathbb{K}[[t^2,t^3]]$을 $\mathbb{K}[[t]]$의 subring으로 보자. 이는 $\x\mapsto t^2$, $\y\mapsto t^3$을 통해 $\mathbb{K}[[\x,\y]]/(\y^2-\x^3)$과 isomorphic하며, 원점에서 cusp를 갖는 곡선 $\y^2=\x^3$의 complete local ring이다. $A$는 $\mathbb{K}[[t]]$의 subring이므로 integral domain이다. 그 차원을 계산하기 위해 위의 isomorphism $A\cong \mathbb{K}[[\x,\y]]/(\y^2-\x^3)$을 쓰자. $\mathbb{K}[[\x,\y]]$는 $2$차원 regular local ring이고 $\y^2-\x^3$은 이 domain의 $0$이 아닌 non-unit이므로 non-zerodivisor이다. 따라서 [§Depth, ⁋명제 9](/ko/math/commutative_algebra/depth#prop9)에 의하여 $\dim A=\dim (\mathbb{K}[[\x,\y]]/(\y^2-\x^3))=\dim \mathbb{K}[[\x,\y]]-1=1$이다. Domain이므로 $t^2\in \mathfrak{m}=(t^2,t^3)A$은 non-zerodivisor이고, 따라서 $\operatorname{depth}A\geq 1=\dim A$가 되어 $A$는 Cohen--Macaulay local ring이다.

이제 $\mathfrak{q}=(t^2)A$를 생각하자. $(t^3)^2=t^6=(t^2)^3$이므로 $t^3\in \sqrt{\mathfrak{q}}$이고 $t^2\in \mathfrak{q}$이므로 $\sqrt{\mathfrak{q}}=\mathfrak{m}$이 되어 $\mathfrak{q}$는 parameter ideal이다. $A$는 $\mathbb{K}$-벡터공간으로서 $\{t^a\mid a\in \{0,2,3,4,\ldots\}\}$을 basis로 가지며, $\mathfrak{q}=t^2A$는 $\{t^b\mid b\in \{2,4,5,6,\ldots\}\}$으로 span되므로, $A/\mathfrak{q}$는 $\{1,t^3\}$을 basis로 갖는다. 즉 $\length(A/\mathfrak{q})=2$이다. $A$가 Cohen--Macaulay이므로 [따름정리 13](#cor13)에 의하여 $e(\mathfrak{q};A)=\length(A/\mathfrak{q})=2$이다.

대조적으로 [예시 7](#ex7)의 $B=\mathbb{K}[[\x,\y]]/(\x^2,\x\y)$를 보자. $B$는 $\dim B=1$이지만 $\operatorname{depth}B=0$이라 Cohen--Macaulay가 아니었다. Ideal $\mathfrak{q}=(\y)B$에 대하여 $B/\mathfrak{q}=\mathbb{K}[[\x,\y]]/(\x^2,\x\y,\y)\cong \mathbb{K}[[\x]]/(\x^2)$이 유한한 길이를 가지므로 $\mathfrak{q}$는 parameter ideal이고, $\length(B/\mathfrak{q})=\length(\mathbb{K}[[\x]]/(\x^2))=2$이다. 한편 $\mathfrak{q}^n=(\y^n)B$이고

$$B/\mathfrak{q}^n=\mathbb{K}[[\x,\y]]/(\x^2,\x\y,\y^n)$$

은 $\x^2=\x\y=\y^n=0$이므로 $\{1,\x,\y,\y^2,\ldots,\y^{n-1}\}$을 $\mathbb{K}$-basis로 갖는다. 따라서 $\chi_{\mathfrak{q},B}(n)=\length(B/\mathfrak{q}^n)=n+1$이고, 이는 degree $1=\dim B$의 다항식으로 leading coefficient가 $1$이므로 $e(\mathfrak{q};B)=1!\cdot 1=1$이다. 결국 $e(\mathfrak{q};B)=1<2=\length(B/\mathfrak{q})$이며, 격차 $\length(B/\mathfrak{q})-e(\mathfrak{q};B)=1$이 $B$의 Cohen--Macaulay 조건의 실패, 곧 $\operatorname{depth}B=0$을 감지한다.
:::

Cohen--Macaulay 조건은 depth라는 homological 불변량과 차원을 하나로 묶는 지점에 놓여 있으며, 이 결합은 이후 module의 projective dimension을 depth로 표현하는 Auslander--Buchsbaum 공식에서 다시 나타난다.

---

**참고문헌**

**[AM]** M. F. Atiyah, I. G. Macdonald. *Introduction to Commutative Algebra*. Addison-Wesley, 1969.

**[BH]** W. Bruns, J. Herzog. *Cohen-Macaulay Rings*. Cambridge University Press, 1993.

**[Eis]** David Eisenbud. *Commutative Algebra: with a view toward algebraic geometry*. Springer, 1995.

**[Mat]** Hideyuki Matsumura. *Commutative Ring Theory*. Cambridge University Press, 1986.

---
