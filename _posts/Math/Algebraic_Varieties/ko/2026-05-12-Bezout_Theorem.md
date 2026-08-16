---
title: "베주 정리"
description: "대수기하학의 베주 정리는 대수적으로 닫힌 체 위의 사영 공간에서, 공통 성분을 갖지 않는 두 곡선이 교차하는 점의 수가 두 곡선의 차수의 곱과 같다는 결과이다. 교점의 중복도를 고려하면 두 이차곡선은 정확히 네 점에서 만난다."
excerpt: "Bézout's theorem and its applications"

categories: [Math / Algebraic Varieties]
permalink: /ko/math/algebraic_varieties/bezout_theorem
sidebar: 
    nav: "algebraic_varieties-ko"

date: 2026-03-15
weight: 21
published: false

---

우리는 이번 글에서 algebraic geometry의 고전적인 정리인 Bézout theorem을 소개한다. 직관적으로, 평면 위의 두 곡선 $C,D$가 주어졌다 하자. 그럼 $C$와 $D$가 만나는 교점의 개수는 이들의 degree에 의존하는데, 가령 평면 위에서 정의된 이차곡선 $\y=\x^2$과 직선은 일반적으로 두 점에서 만난다. Bézout theorem은 이를 일반화한 결과이다.

::: 명제 1 (Bézout)
Algebraically closed field 위에서 정의된 $\mathbb{P}^n$ 안에서, degree $d_1, \ldots, d_n$의 hypersurface $H_1, \ldots, H_n$이 공통 성분을 갖지 않고 $H_1 \cap \cdots \cap H_n$이 유한집합이라면

$$\deg(H_1 \cap \cdots \cap H_n) = d_1 \cdots d_n$$

이 성립한다. 여기서 intersection은 multiplicity를 고려한 것이다. 
:::

특히 $\mathbb{P}^2$ 안에서 degree $m,n$인 두 곡선은 중복도를 고려하면 $mn$개의 점에서 만난다. 다소 주의할 것은 이들이 공통 성분을 가지면 안된다는 것으로, 가령 서로 같은 두 곡선은 이를 통해 교집합을 계산할 수 없다. 

::: 예시 2 (두 이차곡선)
$\mathbb{P}^2$ 안의 두 이차곡선

$$C_1 = Z(\x_0^2 + \x_1^2 - \x_2^2),\qquad C_2 = Z(\x_0\x_1)$$

을 생각하자. $C_1$은 원뿔의 projectivization이고, $C_2$는 두 직선 $Z(\x_0)$과 $Z(\x_1)$의 합집합이다. 이 두 곡선은 공통 성분을 갖지 않으므로 Bézout의 정리에 의하여 $2 \times 2 = 4$개의 교점을 가져야 한다. 실제로 교집합을 계산해보면, $\x_0 = 0$일 때 $\x_1^2 = \x_2^2$이 되어 $[0:1:1]$과 $[0:1:-1]$을 얻고, $\x_1 = 0$일 때 $\x_0^2 = \x_2^2$이 되어 $[1:0:1]$과 $[1:0:-1]$을 얻어 정확히 4점에서 만남을 확인할 수 있다.
:::

## 증명

우리는 일반적인 경우에 증명을 하는 대신, $\mathbb{P}^2$에서의 Bézout theorem만 증명한다. 이를 위해 다음 보조정리를 사용한다.

::: 명제 3 (Hilbert polynomial)
Projective variety $X \subseteq \mathbb{P}^n$의 homogeneous coordinate ring $S(X)$에 대하여, 함수 $H(t) = \dim_\mathbb{K} S(X)_t$를 $X$의 **Hilbert function**라 한다. Hilbert-Serre 정리에 의하면 이 함수는 $t \gg 0$에서 다항식 $P_X(t)$와 일치하며, 이 다항식을 $X$의 **Hilbert polynomial**이라 한다.

특히 degree $d$인 곡선 $C = Z(F) \subseteq \mathbb{P}^2$의 경우, $S(C) = \mathbb{K}[\x_0, \x_1, \x_2]/(F)$의 Hilbert polynomial은

$$P_C(t) = dt + \frac{d(3-d)}{2}$$

이다. 여기서 $P_C$의 degree는 $C$의 차원인 $1$이고, 최고차항 계수는 $\deg C = d$이며, 상수항 $P_C(0) = \frac{d(3-d)}{2} = 1 - \frac{(d-1)(d-2)}{2}$로부터 $C$의 arithmetic genus $1 - P_C(0) = \frac{(d-1)(d-2)}{2}$를 얻는다.
:::

Hilbert function $H(t)$는 degree $t$인 homogeneous polynomial 공간의 원소 가운데 $C$ 위에서 0이 되는 것들을 제거한 후 남은 독립적인 원소의 개수, 즉 $C$ 위에서 서로 다른 함수로 작용하는 homogeneous polynomial들의 개수이다. $t$가 커질수록 이 수는 다항식처럼 자라며, 그 degree는 $C$의 차원인 $1$과 같고, 최고차항 계수는 degree $d$와 비례하며, 상수항은 $1$에서 arithmetic genus $\frac{(d-1)(d-2)}{2}$를 뺀 값과 같다.

::: 증명
$S = \mathbb{K}[\x_0, \x_1, \x_2]$라 하자. $(S/(F))_t$의 차원은 $S_t$에서 $F$의 배수들을 제거하여 얻는 공간의 차원과 같다. 곱셈 $\cdot F: S(-d) \rightarrow S$는 단사이므로 다음 short exact sequence를 얻는다.

$$0 \rightarrow S(-d) \xrightarrow{\cdot F} S \rightarrow S/(F) \rightarrow 0$$

$\dim_\mathbb{K} S_t = \binom{t+2}{2}$이므로, degree $t$ 부분의 차원을 비교하면

$$\dim_\mathbb{K} (S/(F))_t = \binom{t+2}{2} - \binom{t-d+2}{2}$$

이다. 이를 전개하면

$$\frac{(t+2)(t+1)}{2} - \frac{(t-d+2)(t-d+1)}{2} = dt + \frac{d(3-d)}{2}$$

를 얻는다.
:::

이 결과는 이어지는 [명제 5](#prop5)의 증명에서 핵심적으로 사용된다.

::: 명제 4
$\mathbb{P}^2$ 안의 degree $d$ curve $C = Z(F)$와 $C$의 성분이 아닌 직선 $L$에 대하여, 교차 $C \cap L$은 정확히 $d$개의 점(중복도 포함)으로 이루어진다.
:::

이 명제는 Bézout 정리의 가장 단순한 특수 경우이다. Degree $d$ 곡선이 자신의 성분이 아닌 직선과 $d$점에서 만난다는 기하학적 직관을 제공한다.

::: 증명
일반성을 잃지 않고 $L = Z(\x_2)$라 하자. $L$이 $C$의 성분이 아니므로 $\x_2$는 $F$의 인수가 아니고, 따라서 $\x_2 = 0$을 대입하여 얻는 $F(\x_0, \x_1, 0)$은 영다항식이 아니다. 이는 $\x_0, \x_1$에 관한 degree $d$ homogeneous polynomial이므로 algebraically closed field 위에서 일차식들의 곱

$$F(\x_0, \x_1, 0) = c\prod_{i=1}^{k}(b_i\x_0 - a_i\x_1)^{e_i},\qquad \sum_{i=1}^{k}e_i = d$$

으로 분해되며, 서로 다른 인수들은 $L$ 위의 서로 다른 점 $p_i = [a_i : b_i : 0]$에 대응한다.

남은 것은 근의 중복도 $e_i$가 $i_{p_i}(C, L)$과 같음을 확인하는 것이다. $\x_0, \x_1$의 좌표를 바꾸어 $p_i = [1:0:0]$이라 두고 affine chart $\x_0 = 1$에서 좌표를 $(\y, \z) = (\x_1, \x_2)$로 쓰면 $L$의 국소 방정식은 $\z$이고 $C$의 국소 방정식은 $f(\y, \z) = F(1, \y, \z)$이므로

$$i_{p_i}(C, L) = \dim_\mathbb{K} \mathcal{O}_{\mathbb{A}^2, p_i}/(f, \z) = \dim_\mathbb{K} \mathcal{O}_{\mathbb{A}^1, 0}/(f(\y, 0))$$

이고, 이는 $f(\y, 0) = F(1, \y, 0)$이 $\y = 0$에서 갖는 근의 중복도, 곧 $e_i$이다. 따라서 $\sum_i i_{p_i}(C, L) = \sum_i e_i = d$이다.
:::

이제 명제 1을 증명한다. 핵심은 두 가지이다. 먼저 intersection multiplicity의 합이 전역적인 대수적 대상의 차원과 일치함을 보이고, 둘째로 그 차원을 Hilbert 다항식으로 정확히 $mn$으로 계산하는 것이다.

::: 명제 5
(명제 1의 $\mathbb{P}^2$ 경우) $\mathbb{P}^2$ 안의 degree $m$, $n$인 두 곡선 $C = Z(F)$, $D = Z(G)$가 공통 성분을 갖지 않으면 $\sum_p i_p(C, D) = mn$이다.
:::

::: 증명
두 단계로 나누어 증명한다.

**단계 1.** 먼저 다음 등식을 보인다.

> $\sum_{p \in C \cap D} i_p(C, D) = \dim_\mathbb{K} (\mathbb{K}[\x_0, \x_1, \x_2]/(F, G))_t \qquad (t \gg 0)$

$C \cap D$가 유한집합임은 $C$와 $D$가 공통 성분을 갖지 않는다는 가정으로부터 알려져 있다. ([§차원, ⁋명제 9](/ko/math/algebraic_varieties/dimension#prop9)) $\mathbb{K}$가 algebraically closed field이라 무한집합이므로 $C \cap D$의 어느 점도 지나지 않는 직선이 존재하고, 좌표를 바꾸어 이 직선을 $Z(\x_2)$라 둘 수 있다. 즉 $C \cap D \subseteq U_2 = \{\x_2 \neq 0\}$이라 가정하여도 좋으며, 이 가정은 아래에서 중국인의 나머지 정리를 한 chart 위에서 쓰기 위해 필요하다. 점 $p = [a:b:c] \in C \cap D$는 $U_2$에서의 좌표로 $p = (a/c, b/c)$이고, $F, G$를 dehomogenize한 $f, g \in \mathbb{K}[\x, \y]$에 대하여

$$i_p(C, D) = \dim_\mathbb{K} \mathcal{O}_{\mathbb{A}^2, p}/(f, g)$$

이다. ([§교차곱, ⁋정의 1](/ko/math/algebraic_varieties/intersection_product#def1)) $V(F, G)$가 유한집합이므로 $f, g$는 affine ring $\mathbb{K}[\x, \y]$에서 0차원 ideal $(f, g)$을 생성하며, 중국인의 나머지 정리에 의하여

$$\mathbb{K}[\x, \y]/(f, g) \cong \prod_{p \in V(f,g)} \mathcal{O}_{\mathbb{A}^2, p}/(f, g)$$

이다. 따라서 $\dim_\mathbb{K} \mathbb{K}[\x, \y]/(f, g) = \sum_p i_p(C, D)$이다.

한편, $S = \mathbb{K}[\x_0, \x_1, \x_2]$의 quotient $R = S/(F, G)$의 Hilbert function $H(t) = \dim_\mathbb{K} R_t$는 $t \gg 0$에서 상수 $mn$이 되며(단계 2에서 증명), 이 상숫값이 $\dim_\mathbb{K} \mathbb{K}[\x, \y]/(f, g)$와 같음을 보이면 된다. 이를 위해 dehomogenization

$$\varphi_t: R_t \rightarrow \mathbb{K}[\x, \y]/(f, g),\qquad H \mapsto H(\x, \y, 1)$$

이 $t \gg 0$에서 동형임을 확인한다. 먼저 $Z(\x_2)$가 $V(F, G)$를 만나지 않으므로 $(F, G, \x_2)$의 zero set은 공집합이고, 따라서 Nullstellensatz에 의하여 $R/\x_2R = S/(F, G, \x_2)$는 유한차원이다. 즉 $t \gg 0$에서 $(R/\x_2R)_{t+1} = 0$이므로 곱셈 $\cdot\x_2: R_t \rightarrow R_{t+1}$은 전사이고, 양쪽 모두 차원이 $mn$이므로 이는 동형이다. 이제 $H \in R_t$의 dehomogenization이 $(f, g)$에 속한다면 등식의 양변을 homogenize하여 적당한 $N$에 대하여 $\x_2^N H \in (F, G)$를 얻고, 방금 본 단사성을 반복하여 $H = 0$을 얻으므로 $\varphi_t$는 단사이다. 또 $\mathbb{K}[\x, \y]/(f, g)$가 유한차원이므로 그 기저를 나타내는 다항식들의 degree보다 $t$를 크게 잡으면, 각 다항식에 $\x_2$의 거듭제곱을 곱하여 degree $t$로 homogenize할 수 있어 $\varphi_t$는 전사이다.

**단계 2.** 이제 $\dim_\mathbb{K} (\mathbb{K}[\x_0, \x_1, \x_2]/(F, G))_t = mn$임을 보인다($t \gg 0$). $S = \mathbb{K}[\x_0, \x_1, \x_2]$라 쓰자. $F, G$가 공통인 irreducible factor를 갖지 않으므로 곱셈 morphism $\cdot F: S(-m) \rightarrow S$과 $\cdot G: S/(F)(-n) \rightarrow S/(F)$은 모두 단사이며, 다음 두 short exact sequence를 얻는다.

$$0 \rightarrow S(-m) \xrightarrow{\cdot F} S \rightarrow S/(F) \rightarrow 0$$
$$0 \rightarrow S/(F)(-n) \xrightarrow{\cdot G} S/(F) \rightarrow S/(F, G) \rightarrow 0$$

[명제 3](#prop3)에서 degree를 $m$으로 읽으면, $S/(F)$의 Hilbert 다항식은 $P_F(t) = mt + c_1$의 꼴이 된다. 두 번째 exact sequence에 Hilbert 다항식을 적용하면 $S/(F, G)$의 Hilbert 다항식은

$$P_{F,G}(t) = P_F(t) - P_F(t - n) = \bigl(mt + c_1\bigr) - \bigl(m(t-n) + c_1\bigr) = mn$$

이다. 즉 $t \gg 0$에 대하여 $(S/(F, G))_t$의 차원은 상수 $mn$이며, 단계 1에 의하여 $\sum_p i_p(C, D) = mn$이다.
:::

## 일반화

지금까지는 $\mathbb{P}^2$의 곡선에 대해서만 Bézout 정리를 증명했다. 이를 임의의 projective space와 일반적인 projective variety로 확장하려면 Chow ring이 필요하다. 핵심 사실은

$$\CH^\ast(\mathbb{P}^n) \cong \mathbb{Z}[H]/(H^{n+1})$$

이다. ([§교차곱, ⁋예시 10](/ko/math/algebraic_varieties/intersection_product#ex10)) 여기서 $H$는 hyperplane class이며, codimension이 $k$이며 degree가 $d$인 variety는 class $dH^k$를 갖는다. 특히 degree $d$인 hypersurface는 $dH$에 대응하므로, $n$개의 hypersurface $H_1, \ldots, H_n$의 교차곱은

$$[H_1] \cdot [H_2] \cdots [H_n] = (d_1 H)(d_2 H) \cdots (d_n H) = d_1 d_2 \cdots d_n \cdot H^n$$

이 된다. $H^n$은 $\mathbb{P}^n$ 안의 점의 class이고 그 degree가 1이므로, $\deg(H_1 \cap \cdots \cap H_n) = d_1 \cdots d_n$을 얻는다. 이 직관 하에서 일반화된 Bézout 정리는 다음과 같이 서술된다.

::: 명제 6 (일반화된 Bézout 정리)
$\mathbb{P}^n$ 안의 두 projective variety $V, W$에 대해

$$\deg(V \cap W) \leq \deg(V) \cdot \deg(W)$$

이 성립한다. 여기서 $\deg(V \cap W)$는 $V \cap W$의 각 irreducible component들의 degree의 합이다. 등호는 $V$와 $W$가 proper intersection을 가지고 (즉 $V \cap W$의 모든 irreducible component $Z$에 대해 $\operatorname{codim}(Z) = \operatorname{codim}(V) + \operatorname{codim}(W)$이고) 각 성분에서의 intersection multiplicity가 모두 $1$일 때 성립하며, 이 경우 각 성분 $Z$에 intersection multiplicity $m_Z$를 부여하면 $\sum_Z m_Z \deg(Z) = \deg(V) \cdot \deg(W)$이다.
:::

::: 예시 7 ($\mathbb{P}^3$)
$\mathbb{P}^3$ 안의 두 이차곡면(quadric surface) $Q_1, Q_2$를 생각하자. 각각 degree 2이므로 proper intersection을 가질 때 교차 $Q_1 \cap Q_2$는 차원 1, degree 4인 곡선이다. 구체적으로, $Q_1 = Z(\x_0\x_3 - \x_1\x_2)$와 $Q_2 = Z(\x_0\x_2 - \x_1\x_3)$를 잡으면 교차는 네 개의 직선(line)으로 분해되며, 이들의 degree 합은 여전히 4이다.
:::

명제 6의 증명은 Chow ring을 통한 intersection theory의 일반론에 의존한다. 자세한 내용은 [§교차곱](/ko/math/algebraic_varieties/intersection_product)을 참조하라. [§차원, ⁋예시 14](/ko/math/algebraic_varieties/dimension#ex14)의 부등식이 성분의 codimension에 대한 것으로 다시 나타난다.

## 응용

### Cayley-Bacharach 정리

::: 명제 8 (Cayley-Bacharach 정리의 특수한 경우)
$\mathbb{P}^2$ 안의 두 세차곡선 $C_1 = Z(F_1)$, $C_2 = Z(F_2)$가 공통 성분을 갖지 않고, 서로 다른 9점 $p_1, \ldots, p_9$에서 proper intersection으로 만난다고 하자. 이 때 임의의 세차곡선 $C_3 = Z(F_3)$가 $p_1, \ldots, p_8$을 지난다면, $C_3$는 $p_9$도 지난다.
:::

::: 증명
두 세차곡선 $C_1, C_2$가 proper intersection으로 서로 다른 9개의 점 $p_1, \ldots, p_9$에서 만난다고 가정하자. $\mathbb{P}^2$ 위의 degree 3 homogeneous polynomial 공간 $\mathbb{K}[\x_0, \x_1, \x_2]_3$의 차원은 $\binom{3+2}{2} = 10$이며, 각 점 $p_i$를 지나는 조건은 하나의 일차조건이므로 $V = \{F \in \mathbb{K}[\x_0, \x_1, \x_2]_3 \mid F(p_i) = 0 \text{ for } i = 1, \ldots, 8\}$은 차원 $\dim V \ge 10 - 8 = 2$인 부분공간이다. 한편 $F_1, F_2 \in V$이고 $C_1 \neq C_2$이므로 $F_1, F_2$는 일차독립이다. 남은 것은 $\dim V = 2$, 곧 여덟 점이 degree 3 form들에 독립적인 조건을 부과함을 보이는 것이다.

먼저 $\Gamma = \{p_1, \ldots, p_9\}$의 서로 다른 네 점은 한 직선 위에 놓일 수 없다. 직선 $L$이 $\Gamma$의 네 점을 지난다면 $L$과 $C_j$의 교점이 넷 이상이 되어 [명제 5](#prop5)에 어긋나므로 $L$은 $C_j$의 성분이어야 하고, 이것이 $j = 1, 2$ 모두에 대해 성립하여 $C_1$과 $C_2$가 공통 성분을 갖기 때문이다. 같은 방식으로 $\Gamma$의 일곱 점도 하나의 conic 위에 놓일 수 없다. 그 conic이 irreducible이면 [명제 5](#prop5)에 의하여 $C_j$와의 교점이 여섯을 넘지 못하여 다시 $C_1, C_2$의 공통 성분이 되고, 직선들의 합집합이면 그 중 한 직선이 $\Gamma$의 네 점을 지나기 때문이다.

이제 $A = \{p_1, \ldots, p_8\}$의 각 점 $q$에 대하여 $A \setminus \{q\}$의 일곱 점에서는 $0$이 되고 $q$에서는 $0$이 아닌 degree 3 form $H_q$를 만든다. $q$를 지나는 한 직선은 $\Gamma$의 다른 점을 많아야 둘 포함하므로 $A \setminus \{q\}$의 일곱 점이 그러한 직선 하나에 모두 담길 수 없고, 따라서 $q, a, b$가 collinear가 아닌 $a, b \in A \setminus \{q\}$를 고를 수 있다. $R = A \setminus \{q, a, b\}$라 두면 $\lvert R\rvert = 5$이고 degree 2 form들의 공간은 6차원이므로 $R$의 다섯 점에서 $0$이 되는 conic이 존재하는데, 그러한 conic 가운데 $q$를 지나지 않는 것 $Q$가 있으면 $a, b$를 지나는 직선의 방정식 $L_{ab}$에 대하여 $H_q = L_{ab}Q$로 두면 된다.

$R$의 다섯 점을 지나는 모든 conic이 $q$도 지난다고 하자. 그럼 $R \cup \{q\}$를 지나는 conic $Q$가 있다. 직선 $\overline{qa}$는 $\Gamma$의 점을 셋까지만 포함하므로 $q, a, c$가 collinear가 아닌 $c \in R$을 고를 수 있고, 다섯 점 $\{b\} \cup (R \setminus \{c\})$에 같은 논증을 되풀이한다. 이 다섯 점을 지나면서 $q$를 지나지 않는 conic $Q''$이 있으면 $a, c$를 지나는 직선의 방정식 $L_{ac}$에 대하여 $H_q = L_{ac}Q''$으로 두면 된다. 그렇지 않다면 이 다섯 점과 $q$를 함께 지나는 conic $Q'$이 존재하는데, $Q$와 $Q'$은 $\{q\} \cup (R \setminus \{c\})$의 다섯 점을 공유한다. 두 conic이 공통 성분을 갖지 않으면 [명제 5](#prop5)에 의하여 공유하는 점이 넷을 넘지 못하고, 공통 직선을 가지면 그 직선 위에 $\Gamma$의 점이 셋까지만 있고 남은 두 직선은 한 점에서만 만나므로 역시 넷을 넘지 못한다. 따라서 $Q = Q'$인데 이 conic은 $R \cup \{q, b\}$의 일곱 점을 지나 앞 문단에 모순이다.

각 점의 homogeneous coordinate를 하나씩 고정하면 평가 $F \mapsto F(q)$는 $\mathbb{K}[\x_0, \x_1, \x_2]_3$ 위의 선형함수이고, $\sum_{q \in A} \lambda_q F(q) = 0$이 모든 $F$에 대해 성립한다면 $F = H_q$를 대입하여 $\lambda_q = 0$을 얻으므로 여덟 개의 평가 함수는 일차독립이다. 즉 $\mathbb{K}[\x_0, \x_1, \x_2]_3 \rightarrow \mathbb{K}^8$의 rank가 $8$이므로 $\dim V = 10 - 8 = 2$이고, $F_1, F_2$가 $V$의 기저를 이룬다. 따라서 임의의 $F_3 \in V$에 대해 상수 $\alpha, \beta$가 존재하여 $F_3 = \alpha F_1 + \beta F_2$이다. 양변에 $p_9$를 대입하면 $F_3(p_9) = \alpha F_1(p_9) + \beta F_2(p_9) = 0$이므로 $C_3$는 $p_9$도 지난다.
:::

이 결과의 직관은 다음과 같다. 두 세차곡선의 교차 9점 중 8점을 지나는 조건은 세차곡선 공간(10차원)에 8개의 선형 제약을 부과하여, 남은 1차원 공간의 원소들이 모두 9번째 점도 지나게 된다. 이는 $3 \times 3 = 9$라는 Bézout 정리의 결과가 우연이 아님을 보여준다.

### Pascal의 정리

::: 명제 9 (Pascal)
Irreducible 이차곡선 위의 서로 다른 6점 $A, B, C, D, E, F$에 대해, 세 교점

$$P = \overline{AB} \cap \overline{DE},\quad Q = \overline{BC} \cap \overline{EF},\quad R = \overline{CD} \cap \overline{FA}$$

이 모두 존재하면 이 세 점은 collinear이다.
:::

::: 증명
이차곡선을 $\Gamma$라 표기하자. 두 세차곡선

$$X = \overline{AB} \cup \overline{CD} \cup \overline{EF},\quad Y = \overline{BC} \cup \overline{DE} \cup \overline{FA}$$

을 정의하자. 각각은 세 직선의 합집합이므로 degree 3 곡선이다. 일반적인 위치 가정 하에 $X$와 $Y$는 공통 성분을 갖지 않는다.

$X \cap Y$는 $A, B, C, D, E, F$와 $P, Q, R$을 모두 포함하므로 적어도 9개의 서로 다른 점을 포함한다. Bézout의 정리에 의하여 $\sum_{p \in X \cap Y} i_p(X, Y) = 3 \times 3 = 9$이므로, $X \cap Y$는 정확히 이 9점이며 각 점에서의 intersection multiplicity는 1이다.

이제 새로운 세차곡선 $Z = \Gamma \cup \overline{PQ}$를 정의하자. 이는 degree 3의 곡선으로, $X \cap Y$의 9점 중 $A, B, C, D, E, F$와 $P, Q$, 즉 8점을 지난다. [명제 8](#prop8)에 의하여 $Z$는 9번째 점 $R$도 지나야 한다. $R \in Z = \Gamma \cup \overline{PQ}$이므로, $R \in \Gamma$이거나 $R \in \overline{PQ}$이다.

만일 $R \in \Gamma$라면 $R = \overline{CD} \cap \overline{FA} \in \Gamma$이어야 한다. 그러나 $\overline{CD}$와 $\Gamma$는 Bézout의 정리에 의해 최대 2점에서 만나며, 이미 $C, D \in \Gamma$이므로 $\overline{CD} \cap \Gamma = \{C, D\}$이다. 마찬가지로 $\overline{FA} \cap \Gamma = \{F, A\}$이므로 $R \in \Gamma$일 수 없다. 결론적으로 $R \in \overline{PQ}$이며, 즉 $P, Q, R$은 공선형이다.
:::

### 이중점의 최대 개수

Bézout 정리로 평면곡선의 singular point 개수에 대한 상한을 얻을 수 있다.

::: 명제 10
Degree $d$ irreducible plane curve가 가질 수 있는 최대 ordinary double point의 개수는 $\binom{d-1}{2} = \frac{(d-1)(d-2)}{2}$이다.
:::

::: 증명
Degree $d$ irreducible curve $C$ 위에 $n$개의 ordinary double point $p_1, \ldots, p_n$이 있다고 하자. $d \leq 2$이면 $C$를 정의하는 form이 irreducible이므로 $C$는 직선이거나 nondegenerate conic이어서 singular point를 갖지 않고, $n = 0 = \binom{d-1}{2}$으로 부등식이 성립한다. 이하 $d \geq 3$이라 하고 $n \geq \binom{d-1}{2} + 1$이라 가정하여 모순을 이끈다.

$k = \binom{d-1}{2} + 1$이라 두고, 주어진 double point 가운데 $k$개와, 이들과 겹치지 않는 $C$ 위의 서로 다른 점 $q_1, \ldots, q_{d-3}$을 고르자. Degree $d-2$ form들의 공간은 $\binom{d}{2}$차원이고 한 점에서 $0$이 되는 것은 하나의 일차조건이며

$$k + (d - 3) = \frac{(d-1)(d-2)}{2} + d - 2 = \binom{d}{2} - 1$$

이므로, 고른 $k + d - 3$개의 점에서 모두 $0$이 되는 $0$이 아닌 degree $d-2$ form $G$가 존재한다. $C$는 irreducible이고 $\deg C = d > d - 2$이므로 $D = Z(G)$의 성분이 될 수 없고, 따라서 $C$와 $D$는 공통 성분을 갖지 않는다.

각 ordinary double point $p_i$에서 $C$의 국소 방정식 $f$는 lowest degree 항이 이차이므로 $\mathfrak{m}^2$에 속하고, $D$가 $p_i$를 지나므로 그 국소 방정식 $g$는 $\mathfrak{m}$에 속한다. 여기서 $\mathfrak{m}$은 $\mathcal{O}_{\mathbb{A}^2, p_i}$의 maximal ideal이다. 그럼 $(f, g) \subseteq \mathfrak{m}^2 + (g)$인데 $\mathfrak{m}/\mathfrak{m}^2$은 2차원이고 $\mathfrak{m}^2 + (g)$가 그 안에서 잘라내는 부분공간은 많아야 1차원이므로, $i_{p_i}(C, D) = \dim_\mathbb{K}\mathcal{O}_{\mathbb{A}^2, p_i}/(f, g) \geq 2$이다. 나머지 점 $q_j$에서는 $i_{q_j}(C, D) \geq 1$이므로 [명제 5](#prop5)에 의하여

$$d(d-2) = \sum_p i_p(C, D) \geq 2k + (d - 3) = (d-1)^2$$

인데, 이는 $d^2 - 2d \geq d^2 - 2d + 1$이라 모순이다. 그러므로

$$n \leq \frac{(d-1)(d-2)}{2}$$

이다. 이 상한은 달성 가능하다. 예를 들어 $\mathbb{P}^d$ 안의 rational normal curve를 일반적인 사영(projection)으로 $\mathbb{P}^2$에 놓으면, 정확히 $\frac{(d-1)(d-2)}{2}$개의 ordinary double point를 갖는 irreducible 곡선을 얻는다.
:::

---

**참고문헌**

**[Hart]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[Ful]** W. Fulton, *Intersection Theory*, Springer, 1984.  
**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.
