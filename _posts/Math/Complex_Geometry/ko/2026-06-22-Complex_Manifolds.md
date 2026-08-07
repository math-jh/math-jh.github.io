---
title: "복소다양체"
description: "여러 변수 복소정칙함수에서 출발하여 복소다양체를 위상다양체에 복소정칙 전이함수를 갖는 holomorphic atlas로 정의한다. 복소사영공간, 복소토러스, Riemann 곡면 등의 예시를 다루고, 복소정칙접공간과 holomorphic tangent bundle을 도입한다. 끝으로 콤팩트 연결 복소다양체 위의 복소정칙함수가 상수임을 최대원리로 증명한다."
excerpt: "여러 변수 복소정칙함수, holomorphic atlas, 복소차원, CP^n, 복소토러스, Riemann 곡면, holomorphic tangent space, Wirtinger 미분, 최대원리"

categories: [Math / Complex Geometry]
permalink: /ko/math/complex_geometry/complex_manifolds
sidebar:
    nav: "complex_geometry-ko"

date: 2026-06-22
weight: 1

published: false
---

미분다양체는 국소적으로 $\mathbb{R}^n$처럼 보이며 transition function이 smooth 공간이었다 ([\[미분다양체\] §미분다양체, ⁋정의 1](/ko/math/manifolds/smooth_manifolds#def1)). Complex manifold는 같은 도식을 한 단계 더 강화한 것으로, 국소 모형을 $\mathbb{C}^n$으로 바꾸고 transition function에 매끄러움 대신 *holomorphicity*를 요구한다. $\mathbb{C}^n$을 $\mathbb{R}^{2n}$과 동일시하면 모든 complex manifold는 자동으로 차원 $2n$의 실 미분다양체가 되지만, holomorphic transition function이라는 추가 조건은 smooth 구조만으로는 보이지 않는 강한 강성을 만들어낸다. 이 강성의 가장 단적인 표현이 이 글의 마지막 정리, 곧 콤팩트 connected complex manifold 위의 holomorphic function이 상수밖에 없다는 사실이다.

이 글의 목표는 complex manifold의 정의를 세우고, 표준적인 예시들을 직접 구성하며, 점에서의 holomorphic tangent space를 도입하는 것이다. 한 변수 holomorphic function의 기초는 이미 다루었으므로 ([\[복소해석학\] §정칙함수, ⁋정의 2](/ko/math/complex_analysis/holomorphic_functions#def2)) 여기서는 여러 변수로의 extension에서 출발한다.

## 여러 변수 복소정칙함수

Complex manifold의 transition function은 $\mathbb{C}^n$의 열린집합 사이의 morphism이므로, 먼저 그러한 morphism의 holomorphicity를 정의해야 한다.

::: 정의 1
열린집합 $U \subseteq \mathbb{C}^n$ 위의 함수 $f : U \rightarrow \mathbb{C}$가 *holomorphic<sub>정칙</sub>*하다는 것은, $f$가 $U$에서 연속이고 각 변수에 대하여 따로 holomorphic인 것이다. 곧 임의의 점 $a = (a_1, \ldots, a_n) \in U$와 각 $j$에 대하여, 나머지 좌표를 고정하고 얻는 한 변수 함수

$$
z_j \longmapsto f(a_1, \ldots, a_{j-1}, z_j, a_{j+1}, \ldots, a_n)
$$

이 $a_j$의 근방에서 (한 변수 함수로서) holomorphic이다.
:::

여기서 "연속이고 각 변수에 대해 holomorphic"이라는 조건은 보기보다 약하지 않다. Hartogs의 정리에 따르면 연속성 가정을 떼더라도, 곧 각 변수에 대한 holomorphicity만 가정하더라도 $f$는 자동으로 연속이 되어 위의 의미로 holomorphic이 된다. 또한 Osgood의 정리에 따르면 위의 정의를 만족하는 함수는 (여러 변수의 의미에서) holomorphic이며, 따라서 국소적으로 여러 변수 멱급수

$$
f(z) = \sum_{\alpha \in \mathbb{N}^n} c_\alpha (z - a)^\alpha, \qquad (z-a)^\alpha = \prod_{j=1}^n (z_j - a_j)^{\alpha_j}
$$

로 전개된다. 이 글에서는 이러한 동치성을 사용하기보다 정의 1을 그대로 작업 정의로 삼는다. 핵심은 한 변수 holomorphicity가 가진 좋은 성질들, 곧 무한 미분가능성과 해석성이 여러 변수로 그대로 올라간다는 점이다.

$\mathbb{C}^n$ 사이의 morphism의 holomorphicity는 성분별로 정의한다.

::: 정의 2
열린집합 $U \subseteq \mathbb{C}^n$과 morphism $F = (f_1, \ldots, f_m) : U \rightarrow \mathbb{C}^m$에 대하여, $F$가 *holomorphic*하다는 것은 각 성분 $f_k : U \rightarrow \mathbb{C}$이 [정의 1](#def1)의 의미로 holomorphic인 것이다. Holomorphic morphism $F : U \rightarrow V$가 holomorphic 역사상 $F^{-1} : V \rightarrow U$를 갖는 전단사이면 $F$를 *biholomorphism<sub>쌍정칙사상</sub>*이라 한다.
:::

Biholomorphism은 복소해석적 isomorphism에 해당한다. 두 열린집합이 biholomorphic하게 동치이면 그 위의 holomorphic 함수론은 완전히 같다. Complex manifold란 바로 이런 biholomorphic 동치를 풀로 삼아 $\mathbb{C}^n$의 조각들을 이어 붙인 공간이다.

한 변수의 Wirtinger 미분 ([\[복소해석학\] §정칙함수, ⁋정의 7](/ko/math/complex_analysis/holomorphic_functions#def7)) 은 변수마다 그대로 복제된다. 좌표 $z_j = x_j + i y_j$에 대하여

$$
\frac{\partial}{\partial z_j} = \frac{1}{2}\left( \frac{\partial}{\partial x_j} - i \frac{\partial}{\partial y_j} \right), \qquad
\frac{\partial}{\partial \bar{z}_j} = \frac{1}{2}\left( \frac{\partial}{\partial x_j} + i \frac{\partial}{\partial y_j} \right)
$$

로 정의하면, $C^1$급 함수 $f$가 정의 1의 의미로 holomorphic인 것은 모든 $j$에 대하여 Cauchy–Riemann 방정식

$$
\frac{\partial f}{\partial \bar{z}_j} = 0 \quad (j = 1, \ldots, n)
$$

이 성립하는 것과 동치이다. 각 변수에 대한 한 변수 Cauchy–Riemann 방정식을 모은 것에 지나지 않으므로 이는 즉시 따라온다. 이 관점은 뒤에서 holomorphic tangent space를 다룰 때 다시 등장한다.

## 복소다양체

이제 holomorphic transition function을 갖는 manifold를 정의한다.

::: 정의 3
$M$을 topological manifold라 하자. $M$ 위의 *holomorphic atlas<sub>정칙 좌표계 모임</sub>*는 차트들의 모임 $\{(U_\alpha, \varphi_\alpha)\}$로서, 각 $\varphi_\alpha : U_\alpha \rightarrow \varphi_\alpha(U_\alpha) \subseteq \mathbb{C}^n$이 homeomorphism이고 $\bigcup_\alpha U_\alpha = M$이며, $U_\alpha \cap U_\beta \neq \emptyset$일 때마다 *transition map<sub>전이함수</sub>*

$$
\varphi_\beta \circ \varphi_\alpha^{-1} : \varphi_\alpha(U_\alpha \cap U_\beta) \longrightarrow \varphi_\beta(U_\alpha \cap U_\beta)
$$

이 [정의 2](#def2)의 의미로 holomorphic인 것이다. 이때 두 holomorphic atlas는 합집합이 다시 holomorphic atlas이면 서로 *compatible<sub>양립가능</sub>*하다 하고, 양립가능성에 의한 equivalence class, 곧 maximal holomorphic atlas를 $M$의 *complex structure<sub>복소구조</sub>*라 한다. 복소구조를 갖춘 topological manifold를 *complex manifold<sub>복소다양체</sub>*라 하고, 국소 모형 $\mathbb{C}^n$의 $n$을 그 *complex dimension<sub>복소차원</sub>* $\dim_{\mathbb{C}} M = n$이라 한다.
:::

Transition function이 holomorphic이면 그 역사상도 holomorphic이므로 (holomorphic morphism의 합성과 역에 대한 닫힘성에서), 두 차트 $\varphi_\alpha, \varphi_\beta$ 사이의 관계는 biholomorphic이다. $\mathbb{C}^n$을 표준 동일시 $z_j = x_j + i y_j$로 $\mathbb{R}^{2n}$과 동일시하면 holomorphic transition function은 특히 매끄럽고, 따라서 모든 복소차원 $n$의 complex manifold는 실차원 $2n$의 smooth manifold를 바탕으로 한다. 이 바탕 위에 얹힌 "holomorphic transition function"라는 조건이 복소구조이며, 같은 smooth manifold가 서로 다른 복소구조를 가질 수도, 아예 하나도 갖지 못할 수도 있다.

Complex manifold 사이의 morphism에 대한 holomorphicity도 국소 차트로 옮겨 정의한다.

::: 정의 4
$M, N$을 complex manifold라 하고 $f : M \rightarrow N$을 연속사상이라 하자. $f$가 *holomorphic*하다는 것은, $M$의 임의의 점 $p$에 대하여 $p$를 포함하는 차트 $(U, \varphi)$와 $f(p)$를 포함하는 차트 $(V, \psi)$ ($f(U) \subseteq V$) 를 잡았을 때 국소 표현

$$
\psi \circ f \circ \varphi^{-1} : \varphi(U) \longrightarrow \psi(V)
$$

이 [정의 2](#def2)의 의미로 holomorphic인 것이다. 특히 $N = \mathbb{C}$인 경우의 holomorphic morphism을 $M$ 위의 *holomorphic function<sub>정칙함수</sub>*이라 하고, 그 전체를 $\mathcal{O}(M)$으로 적는다. Holomorphic 전단사사상 $f : M \rightarrow N$으로 역사상도 holomorphic인 것을 *biholomorphism*이라 하며, 그러한 morphism이 존재하면 $M, N$은 *biholomorphic<sub>쌍정칙</sub>*하다 한다.
:::

이 정의는 차트의 선택에 무관하다. 다른 차트를 잡으면 두 국소 표현은 holomorphic인 transition function을 좌우에서 합성한 것만큼 차이가 나고, holomorphic morphism의 합성은 다시 holomorphic이기 때문이다. Holomorphic function 전체 $\mathcal{O}(M)$은 점별 덧셈과 곱셈에 대해 $\mathbb{C}$-대수를 이룬다. 미분다양체에서 smooth 함수의 대수 $C^\infty(M)$이 풍부했던 것과 달리, 콤팩트 complex manifold에서는 $\mathcal{O}(M)$이 상수함수밖에 없을 만큼 빈약해진다. 이 사실은 [정리 14](#thm14)에서 증명한다.

## 예시

::: 예시 5 ($\mathbb{C}^n$)
$\mathbb{C}^n$ 자체가 단 하나의 차트 $(\mathbb{C}^n, \id)$로 이루어진 holomorphic atlas를 가지며, 복소차원 $n$의 complex manifold이다. 이 위의 holomorphic function은 정의 1의 의미의 holomorphic function과 정확히 일치한다. 열린부분집합 $U \subseteq \mathbb{C}^n$ 역시 같은 차트의 restriction으로 complex manifold가 된다.
:::

가장 기본적인 비자명 예는 complex projective space이다. 이는 알려진 projective space의 복소 버전이며 ([\[대수다양체\] §사영다양체, ⁋정의 1](/ko/math/algebraic_varieties/projective_varieties#def1)), 콤팩트 complex manifold의 원형이다.

::: 예시 6 (complex projective space $\mathbb{CP}^n$)
집합

$$
\mathbb{CP}^n = \left( \mathbb{C}^{n+1} \setminus \{0\} \right) \big/ \sim, \qquad
(z_0, \ldots, z_n) \sim (\lambda z_0, \ldots, \lambda z_n) \ \ (\lambda \in \mathbb{C}^\ast)
$$

을 equivalence class $[z_0 : \cdots : z_n]$들의 공간으로 두고, quotient topology를 준다. 각 $i = 0, \ldots, n$에 대하여

$$
U_i = \{ [z_0 : \cdots : z_n] \in \mathbb{CP}^n \mid z_i \neq 0 \}
$$

는 열린집합이며, morphism

$$
\varphi_i : U_i \longrightarrow \mathbb{C}^n, \qquad
\varphi_i([z_0 : \cdots : z_n]) = \left( \frac{z_0}{z_i}, \ldots, \widehat{\frac{z_i}{z_i}}, \ldots, \frac{z_n}{z_i} \right)
$$

는 homeomorphism이다 (모자는 그 항의 생략, 곧 항상 $1$이 되는 $i$번째 좌표를 뺀다는 뜻이다). $\{(U_i, \varphi_i)\}_{i=0}^n$이 $\mathbb{CP}^n$을 복소차원 $n$의 complex manifold로 만든다.
:::

Transition function의 holomorphicity를 직접 확인하자. $i < j$라 하고 $U_i \cap U_j$ 위에서 $\varphi_j \circ \varphi_i^{-1}$을 계산한다. $\varphi_i$의 상 좌표를 $w = (w_0, \ldots, \widehat{w_i}, \ldots, w_n)$이라 하면, 이는 점 $[w_0 : \cdots : w_{i-1} : 1 : w_{i+1} : \cdots : w_n]$에 대응한다 (여기서 $1$은 $i$번째 자리). $U_i \cap U_j$ 위에서는 $j$번째 좌표 $w_j$가 $0$이 아니므로, 이 점을 $j$번째 좌표로 normalize하면 $\varphi_j$의 상은

$$
\left( \frac{w_0}{w_j}, \ldots, \frac{w_{i-1}}{w_j}, \frac{1}{w_j}, \frac{w_{i+1}}{w_j}, \ldots, \widehat{\frac{w_j}{w_j}}, \ldots, \frac{w_n}{w_j} \right)
$$

이 된다. 각 성분은 $w_k / w_j$ 또는 $1/w_j$ 꼴이고, 정의역 $\varphi_i(U_i \cap U_j) = \{ w \mid w_j \neq 0 \}$에서 분모 $w_j$가 결코 $0$이 아니므로, 모든 성분은 $w$의 holomorphic function이다 (다항식을 영점이 아닌 holomorphic function으로 나눈 것이므로). 따라서 $\varphi_j \circ \varphi_i^{-1}$은 holomorphic이고, 대칭으로 $\varphi_i \circ \varphi_j^{-1}$도 holomorphic이다. 곧 모든 transition function이 biholomorphic이며, $\{(U_i, \varphi_i)\}$는 holomorphic atlas이다. $\mathbb{CP}^n$은 콤팩트 Hausdorff 공간이므로 (단위구면 $S^{2n+1} \subseteq \mathbb{C}^{n+1}$의 연속 전사상이므로) 콤팩트 complex manifold이다.

다음 예는 lattice에 의한 quotient로, 모든 차원에서 콤팩트 complex manifold를 만들어내는 또 하나의 표준적인 방법이다.

::: 예시 7 (복소토러스 $\mathbb{C}^n / \Lambda$)
$\Lambda \subseteq \mathbb{C}^n$을 $\mathbb{R}$ 위에서 $\mathbb{C}^n = \mathbb{R}^{2n}$의 기저가 되는 $2n$개의 벡터로 생성된 *lattice<sub>격자</sub>*라 하자. 곧 $\Lambda \cong \mathbb{Z}^{2n}$이고 $\Lambda \otimes_{\mathbb{Z}} \mathbb{R} = \mathbb{C}^n$이다. Quotient group

$$
T = \mathbb{C}^n / \Lambda
$$

에 quotient topology를 주면, $T$는 콤팩트 topological manifold이며 복소차원 $n$의 complex manifold 구조를 가진다.
:::

복소구조는 다음과 같이 얻는다. Quotient map $\pi : \mathbb{C}^n \rightarrow T$는 국소 homeomorphism이다. 충분히 작은 열린집합 $V \subseteq \mathbb{C}^n$을 잡아 $\pi\vert_V$가 그 상 $U = \pi(V)$ 위로의 homeomorphism이 되게 하고, $\varphi = (\pi\vert_V)^{-1} : U \rightarrow V$를 차트로 삼는다. 이런 차트 둘 $\varphi, \varphi'$의 transition function을 보면, 두 국소 preimage는 같은 $T$의 점을 덮으므로 차이가 항상 $\Lambda$의 한 원소만큼의 평행이동

$$
z \longmapsto z + \lambda, \qquad \lambda \in \Lambda
$$

이다. 평행이동은 holomorphic이므로 모든 transition function이 holomorphic이고, $T$는 complex manifold가 된다. 또한 $T$는 기본영역 (lattice의 closed 평행육면체) 의 연속 전사상이므로 콤팩트하다.

복소차원 $1$의 경우 $T = \mathbb{C}/\Lambda$는 *elliptic curve<sub>타원곡선</sub>*의 복소해석적 모습이며 항상 projective variety로 실현된다. 그러나 차원이 올라가면 사정이 달라진다. 일반적인 lattice $\Lambda \subseteq \mathbb{C}^n$ ($n \geq 2$) 에 대한 복소토러스는 어떠한 $\mathbb{CP}^N$에도 holomorphic하게 embedding되지 않는다. 곧 *비대수적*이다. Projective이 되기 위해서는 lattice가 추가적인 정수 대수적 조건 (Riemann 관계식) 을 만족해야 하는데, 이를 만족하는 lattice는 전체 가운데 진부분집합을 이루므로 무작위로 잡은 lattice는 이를 만족하지 않는다. 모든 콤팩트 complex manifold가 대수적이지는 않다는 사실의 가장 손쉬운 출처가 바로 이 복소토러스이다.

복소차원 $1$의 complex manifold에는 따로 이름이 붙는다.

::: 정의 8
복소차원 $1$의 connected complex manifold를 *Riemann surface<sub>리만 곡면</sub>*라 한다.
:::

Riemann surface는 실차원 $2$의 smooth 곡면 위에 holomorphic transition function을 얹은 것이다. 차원이 가장 낮은 만큼 복소기하학의 거의 모든 현상이 처음 나타나는 시험장이며, 앞서의 타원곡선 $\mathbb{C}/\Lambda$도 그 한 예이다. 가장 단순한 콤팩트 Riemann surface는 $\mathbb{CP}^1$이다.

::: 예시 9 (Riemann 구면 $\mathbb{CP}^1$)
[예시 6](#ex6)에서 $n = 1$인 경우 $\mathbb{CP}^1$은 두 차트

$$
U_0 = \{[z_0 : z_1] \mid z_0 \neq 0\}, \quad \varphi_0([z_0:z_1]) = \frac{z_1}{z_0}, \qquad
U_1 = \{[z_0 : z_1] \mid z_1 \neq 0\}, \quad \varphi_1([z_0:z_1]) = \frac{z_0}{z_1}
$$

로 덮인다. $U_0$의 좌표를 $z = z_1/z_0$, $U_1$의 좌표를 $w = z_0/z_1$이라 하면, $U_0 \cap U_1$ ($z_0, z_1$ 모두 $0$이 아닌 곳) 위에서 transition function은

$$
w = \frac{z_0}{z_1} = \frac{1}{z}, \qquad z \in \mathbb{C}^\ast
$$

이다. $\mathbb{C}^\ast$에서 $z \mapsto 1/z$는 holomorphic이므로 이는 holomorphic atlas이다. 위상적으로 $\mathbb{CP}^1$은 $\mathbb{C}$에 한 점 ($[0:1]$에 해당하는 $z = \infty$) 을 더한 것으로, $2$차원 구면 $S^2$와 homeomorphic이다. 이것이 확장복소평면 $\widehat{\mathbb{C}}$의 ([\[복소해석학\] §복소수와 복소평면, ⁋정의 13](/ko/math/complex_analysis/complex_numbers#def13)) complex manifold 구조이며, *Riemann 구면*이라 부른다.
:::

마지막으로, 가장 풍부한 예시의 출처는 projective algebraic geometry가다. $\mathbb{CP}^N$ 안의 smooth projective algebraic variety, 곧 homogeneous 다항식들의 공통 영점집합으로 정의되고 매끄러움 조건 (Jacobian의 최대 계수) 을 만족하는 부분집합은, 자연스럽게 complex manifold 구조를 물려받는다. 음함수 정리의 holomorphic 버전이 국소적으로 그러한 영점집합을 $\mathbb{C}^k$의 그래프로 펴주기 때문이다. 이렇게 얻는 complex manifold는 정의상 projective이며 따라서 algebraic하다. 앞서 본 복소토러스의 예와 합치면, 콤팩트 complex manifold의 세계는 projective인 것 (대수적) 과 non-projective인 것 (비대수적) 으로 갈린다. 어느 쪽인지를 가르는 기준을 추구하는 것이 복소기하학의 한 주된 동력이다.

## 복소정칙접공간

Complex manifold $M$은 실차원 $2n$의 smooth manifold이기도 하므로, 각 점 $p$에서 실 tangent space $T_p M$이 정의된다 ([\[미분다양체\] §접공간, ⁋정의 3](/ko/math/manifolds/tangent_space#def3)). 이는 실차원 $2n$의 실벡터공간이다. 복소구조를 활용하려면 이를 복소화하여 holomorphic 방향과 antiholomorphic 방향으로 나눠야 한다.

국소 holomorphic coordinates를 $z_j = x_j + i y_j$ ($j = 1, \ldots, n$) 라 하자. 그러면 $(x_1, y_1, \ldots, x_n, y_n)$은 실 국소좌표이며, 실 tangent space는 실 기저

$$
\frac{\partial}{\partial x_1}, \frac{\partial}{\partial y_1}, \ldots, \frac{\partial}{\partial x_n}, \frac{\partial}{\partial y_n}
$$

를 가진다. 이 공간을 $\mathbb{C}$ 위로 복소화한다.

::: 정의 10
Complex manifold $M$의 점 $p$에서 *complexified tangent space<sub>복소화 접공간</sub>*를

$$
T_p M \otimes_{\mathbb{R}} \mathbb{C}
$$

로 정의한다. 이 안에서 Wirtinger 미분에 따른 벡터

$$
\frac{\partial}{\partial z_j} = \frac{1}{2}\left( \frac{\partial}{\partial x_j} - i \frac{\partial}{\partial y_j} \right), \qquad
\frac{\partial}{\partial \bar{z}_j} = \frac{1}{2}\left( \frac{\partial}{\partial x_j} + i \frac{\partial}{\partial y_j} \right)
$$

를 둔다. *holomorphic tangent space<sub>정칙접공간</sub>* $T_p^{1,0} M$과 *antiholomorphic tangent space<sub>반정칙접공간</sub>* $T_p^{0,1} M$을 각각

$$
T_p^{1,0} M = \span_{\mathbb{C}}\left\{ \frac{\partial}{\partial z_1}, \ldots, \frac{\partial}{\partial z_n} \right\}, \qquad
T_p^{0,1} M = \span_{\mathbb{C}}\left\{ \frac{\partial}{\partial \bar{z}_1}, \ldots, \frac{\partial}{\partial \bar{z}_n} \right\}
$$

로 정의한다.
:::

집합 $\{\partial/\partial z_j, \partial/\partial \bar{z}_j\}_j$는 $\{\partial/\partial x_j, \partial/\partial y_j\}_j$와 가역 일차변환으로 이어지므로, 이들은 $T_p M \otimes_{\mathbb{R}} \mathbb{C}$의 복소 기저이다. 따라서 direct sum 분해

$$
T_p M \otimes_{\mathbb{R}} \mathbb{C} = T_p^{1,0} M \oplus T_p^{0,1} M
$$

이 성립하고, 양변은 각각 복소차원 $n$이다. 이 분해가 좌표 선택에 무관하다는 것, 곧 다른 holomorphic coordinates로 바꾸어도 같은 부분공간을 얻는다는 것은 transition function이 holomorphic이라는 사실 ($\partial/\partial \bar{z}'_k$가 $\partial/\partial \bar{z}_j$들만의 일차결합으로 표현됨) 에서 나온다. 이 부분공간들을 본질적으로 규정하는 관점, 곧 복소구조에서 유도되는 endomorphism $J$의 $\pm i$-고유공간으로 보는 관점이 있다. $T_p^{1,0}M$은 정확히 $+i$-고유공간이고 $T_p^{0,1}M$은 $-i$-고유공간이다. 이 구조적 시각에서 $(p,q)$형 분해로 나아가는 일반론은 거의 복소구조를 다루는 글의 몫으로 남긴다.

Holomorphic tangent space들이 점마다 매끄럽게 (실은 holomorphic하게) 변하면 다발을 이룬다.

::: 정의 11
Complex manifold $M$ 위의 *holomorphic tangent bundle<sub>정칙접다발</sub>* $T^{1,0} M$은 각 점 $p$에서의 fiber가 $T_p^{1,0} M$인 복소 vector bundle이다. 그 dual bundle을 *holomorphic cotangent bundle<sub>정칙여접다발</sub>* $(T^{1,0}M)^\ast$이라 하고, 그 holomorphic 단면 전체를 $\Omega^1_{\mathrm{hol}}(M)$으로 적어 *holomorphic 1-form<sub>정칙 1-형식</sub>*들의 공간이라 한다.
:::

Cotangent bundle의 구성은 smooth 경우의 추상적 다발 functor 구성을 ([\[미분다양체\] §접다발과 여접다발, ⁋정의 7](/ko/math/manifolds/tangent_and_cotangent_bundles#def7)) holomorphic 범주에서 반복한 것이다. 국소좌표에서 $\partial/\partial z_j$의 쌍대 기저가 $\dd{z_j}$이고 $\partial/\partial \bar{z}_j$의 쌍대 기저가 $\dd{\bar{z}_j}$이며,

$$
\dd{z_j} = \dd{x_j} + i\dd{y_j}, \qquad \dd{\bar{z}_j} = \dd{x_j} - i\dd{y_j}
$$

이다. Holomorphic 1-form은 국소적으로 $\sum_j f_j\dd{z_j}$ 꼴로 적히되 계수 $f_j$가 holomorphic인 형식이다. $\dd{\bar{z}_j}$ 항이 없다는 점이 핵심이며, 이는 holomorphicity가 antiholomorphic 방향의 부재로 표현된다는 [정의 1](#def1) 직후의 Cauchy–Riemann 조건과 정확히 같은 내용이다. $\Omega^1_{\mathrm{hol}}$을 비롯한 holomorphic forms의 미분과 cohomology는 다음 글들에서 본격적으로 다룬다.

## 콤팩트 복소다양체와 최대원리

Complex manifold가 smooth manifold와 결정적으로 갈라지는 지점이 holomorphic function의 강성이다. 한 변수 holomorphic function의 최대절대값 원리가 여러 변수, 나아가 manifold 위로 올라가면, 콤팩트성 아래에서 holomorphic function이 상수밖에 없다는 강력한 결론을 낳는다. 먼저 국소판 최대원리를 정리한다.

::: 명제 12 (여러 변수 최대절대값 원리)
$U \subseteq \mathbb{C}^n$이 connected 열린집합이고 $f : U \rightarrow \mathbb{C}$가 holomorphic이라 하자. $\lvert f \rvert$가 어떤 interior point $a \in U$에서 국소 최댓값을 가지면, $f$는 $U$에서 상수이다.
:::

::: 증명
$\lvert f \rvert$가 $a$에서 국소 최댓값을 가진다고 하자. $a$를 지나는 임의의 복소 직선

$$
\ell_v(\zeta) = a + \zeta v, \qquad v \in \mathbb{C}^n,\ \zeta \in \mathbb{C}
$$

을 생각하면, $\zeta$가 $0$ 근방에서 움직일 때 $g_v(\zeta) = f(a + \zeta v)$는 한 변수 holomorphic function이다 (holomorphic morphism $\zeta \mapsto a + \zeta v$와 $f$의 합성). $\lvert f \rvert$가 $a$에서 국소 최댓값을 가지므로, 공 $B(a, \varepsilon) \subseteq U$를 충분히 작게 잡아 그 위에서 $\lvert f \rvert \leq \lvert f(a) \rvert$가 되게 할 수 있다. 단위벡터 $v$ ($\lvert v \rvert = 1$) 에 대하여 $g_v(\zeta) = f(a + \zeta v)$는 원판 $\lvert \zeta \rvert < \varepsilon$에서 정의된 한 변수 holomorphic function이고, 그 위에서 $\lvert g_v(\zeta) \rvert \leq \lvert f(a) \rvert = \lvert g_v(0) \rvert$이므로 $\lvert g_v \rvert$가 interior point $\zeta = 0$에서 최댓값을 가진다. 한 변수 최대절대값 원리에 의해 $g_v$는 원판 $\lvert \zeta \rvert < \varepsilon$ 전체에서 상수 $f(a)$이다. 이제 임의의 $b \in B(a, \varepsilon)$에 대하여, $b \neq a$이면 $v = (b - a)/\lvert b - a \rvert$, $\zeta_0 = \lvert b - a \rvert < \varepsilon$로 두어 $f(b) = g_v(\zeta_0) = f(a)$이고 $b = a$이면 자명하므로, $f$는 공 $B(a, \varepsilon)$ 전체에서 상수값 $f(a)$를 가진다.

이제 $f$가 $a$ 근방에서 상수이면 $U$ 전체에서 상수임을 보인다. 집합

$$
S = \{ z \in U \mid f \text{가 } z \text{의 한 근방에서 상수 } f(a) \}
$$

를 두면, $S$는 정의상 열려 있고 $a \in S$이므로 공집합이 아니다. $S$가 닫혀 있음을 보이자. $z_0 \in U$가 $S$의 limit point라 하자. $f$는 holomorphic이므로 ([정의 1](#def1) 직후에서 언급한 해석성에 의해) $z_0$의 한 다중원판 근방에서 수렴 멱급수로 전개된다. $S$의 점들이 $z_0$에 집적하고 그 위에서 $f - f(a)$가 항등적으로 $0$이므로, 멱급수의 모든 계수가 $0$이 되어 $f \equiv f(a)$가 $z_0$의 근방에서 성립한다. 따라서 $z_0 \in S$이고 $S$는 닫혀 있다. $U$가 connected이므로 $S = U$, 곧 $f$는 $U$에서 상수이다.
:::

증명에서 본 두 단계, 곧 직선으로 잘라 한 변수 최대원리를 쓰는 단계와 연결성으로 국소 상수성을 전역으로 퍼뜨리는 단계는, manifold 위에서 그대로 재활용된다. Manifold에는 전역 좌표가 없으므로 직선 대신 차트를 쓰지만, 논리의 골격은 동일하다. 이를 위해 차트로 옮긴 국소 상수성을 준비해 둔다.

::: 명제 13
$M$을 connected complex manifold라 하고 $f \in \mathcal{O}(M)$이라 하자. $\lvert f \rvert$가 어떤 점 $p \in M$에서 전역 최댓값을 가지면, $f$는 $M$에서 상수이다.
:::

::: 증명
집합

$$
S = \{ q \in M \mid f \text{가 } q \text{의 한 근방에서 상수} \}
$$

를 둔다. $S$는 정의상 열려 있다. $S$가 닫혀 있음과 비어 있지 않음을 보이면, $M$의 연결성으로 $S = M$이 되어 결론이 따른다.

먼저 $S \neq \emptyset$을 보인다. $\lvert f \rvert$가 $p$에서 전역 최댓값을 가지므로, $p$를 포함하는 차트 $(U, \varphi)$를 잡아 $U$를 connected로 택하면, $g = f \circ \varphi^{-1} : \varphi(U) \rightarrow \mathbb{C}$는 holomorphic이고 $\lvert g \rvert$가 interior point $\varphi(p)$에서 (적어도 국소) 최댓값을 가진다. [명제 12](#prop12)에 의해 $g$는 connected 열린집합 $\varphi(U)$에서 상수이므로 $f$는 $U$에서 상수이고, 따라서 $p \in S$이다.

다음으로 $S$가 닫혀 있음을 보인다. $q_0 \in M$이 $S$의 limit point라 하자. $q_0$를 포함하는 connected 차트 $(V, \psi)$를 잡으면 $h = f \circ \psi^{-1} : \psi(V) \rightarrow \mathbb{C}$는 holomorphic이다. $S$의 한 점 $q_1 \in V \cap S$가 존재하고, $f$는 $q_1$의 근방에서 상수 $c = f(q_1)$이다. 그러면 $h - c$는 $\psi(V)$의 한 열린 부분집합 ($q_1$의 근방의 상) 에서 항등적으로 $0$이다. [명제 12](#prop12)의 증명에서 쓴 해석성 논법에 의해, holomorphic function $h - c$가 connected 열린집합 $\psi(V)$의 어떤 열린 부분집합에서 소멸하면 $\psi(V)$ 전체에서 소멸한다. 따라서 $f \equiv c$가 $V$에서 성립하고, 특히 $q_0$의 근방에서 $f$가 상수이므로 $q_0 \in S$이다.

이로써 $S$는 비어 있지 않고 열려 있으며 닫혀 있다. $M$이 connected이므로 $S = M$이고, $f$는 $M$ 전체에서 (한 근방마다 상수이며 connected이므로) 상수이다.
:::

마지막으로 콤팩트성을 더하면 최댓값의 존재가 보장되어, holomorphic function이 상수로 결정된다.

::: 정리 14 (콤팩트 연결 complex manifold 위의 holomorphic function은 상수)
$M$이 콤팩트 connected complex manifold이면, $M$ 위의 모든 holomorphic function은 상수이다. 곧 $\mathcal{O}(M) = \mathbb{C}$이다.
:::

::: 증명
$f \in \mathcal{O}(M)$이라 하자. $f$는 holomorphic이므로 연속이고, 따라서 $\lvert f \rvert : M \rightarrow \mathbb{R}$은 연속함수이다. $M$이 콤팩트이므로 연속함수 $\lvert f \rvert$는 $M$의 어떤 점 $p$에서 전역 최댓값을 가진다. $M$이 connected이므로 [명제 13](#prop13)에 의해 $f$는 $M$에서 상수이다. $f$가 임의의 holomorphic function이었으므로 $\mathcal{O}(M)$의 모든 원소는 상수이고, 상수함수는 모두 holomorphic이므로 $\mathcal{O}(M) = \mathbb{C}$이다.
:::

이 정리는 complex manifold와 미분다양체의 차이를 한눈에 보여준다. Smooth manifold에서는 partition of unity로 만든 함수들 덕분에 $C^\infty(M)$이 언제나 무한차원으로 풍부하지만, 콤팩트 complex manifold에서는 전역 holomorphic function이 상수밖에 없다. 전역 holomorphic function으로는 점을 구별조차 할 수 없으므로, 콤팩트 complex manifold의 기하를 들여다보려면 함수 대신 더 유연한 대상, 곧 holomorphic 다발의 단면이나 전역 유리형 함수를 동원해야 한다. 충분히 많은 단면을 모아 $\mathbb{CP}^N$으로의 embedding을 줄 수 있는가 하는 물음이 자연스럽게 떠오르며, 이것이 사영성과 대수성을 가르는 기준으로 이어진다. 앞서 본 복소토러스의 비대수성 ([예시 7](#ex7)) 도 정확히 이 단면들의 부족으로 설명된다.

---

**참고문헌**

**[Griffiths–Harris]** P. Griffiths and J. Harris, *Principles of Algebraic Geometry*, Wiley, 1978.  
**[Huybrechts]** D. Huybrechts, *Complex Geometry: An Introduction*, Springer, 2005.  
**[Wells]** R. O. Wells, *Differential Analysis on Complex Manifolds*, 3rd ed., Springer, 2008.  
**[Kodaira]** K. Kodaira, *Complex Manifolds and Deformation of Complex Structures*, Springer, 1986.  
**[Hörmander]** L. Hörmander, *An Introduction to Complex Analysis in Several Variables*, 3rd ed., North-Holland, 1990.
