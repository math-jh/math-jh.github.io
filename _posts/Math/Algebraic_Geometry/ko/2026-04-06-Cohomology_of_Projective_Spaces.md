---
title: "사영공간의 코호몰로지"
excerpt: "Bott's formula and the cohomology of line bundles on projective space"

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/cohomology_of_projective_spaces
sidebar:
    nav: "algebraic_geometry-ko"

header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Cohomology_of_Line_Bundles.png
    overlay_filter: 0.5

date: 2026-04-06
last_modified_at: 2026-04-06
weight: 14
published: false
---

우리는 일찍이 [§선다발과 벡터다발, ⁋예시 16](/ko/math/algebraic_geometry/line_bundles#ex16)에서 line bundle $$\mathcal{O}(d)$$를 정의하고, 그 global section $$H^0(\mathbb{P}^n, \mathcal{O}(d))$$이 degree $$d$$의 homogeneous polynomial들과 동형임을 확인하였다. 그러나 우리가 이전 글에서 도입한 sheaf cohomology ([§층 코호몰로지, ⁋정의 1](/ko/math/algebraic_geometry/sheaf_cohomology#def1))는 $$H^0$$뿐만 아니라 higher cohomology group들 $$H^1, H^2, \ldots$$까지 포함하는 더 풍부한 불변량이므로, 이제 우리는 $$H^0$$ 뿐만 아니라 higher cohomology group들을 사용하여 $$\mathcal{O}(d)$$의 정보를 모두 알아낼 것이다.

## Bott's Formula

$$\mathcal{O}(d)$$는 line bundle이므로 quasi-coherent sheaf이고, 따라서 sheaf cohomology를 계산하기 위해서는 Čech cohomology를 활용하여 standard affine cover $$\mathcal{U}=\{U_0,\ldots, U_n\}$$을 사용하면 충분하다. 다음은 그 계산의 결과이다.

<div class="proposition" markdown="1">

<ins id="prop1">**명제 1 (Bott)**</ins> $$\mathbb{P}^n$$ 위의 line bundle $$\mathcal{O}(d)$$의 cohomology는 다음과 같다:

$$H^q(\mathbb{P}^n, \mathcal{O}(d)) = \begin{cases}
\mathbb{K}[\x_0, \ldots, \x_n]_d & q = 0, d \geq 0 \\
\mathbb{K}[\x_0^{-1}, \ldots, \x_n^{-1}]_{-d-n-1} & q = n, d \leq -n-1 \\
0 & \text{otherwise}
\end{cases}$$

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

위에서 설명한 것과 같이 Čech cohomology를 사용한다. 우선 각각의 열린집합 위에서 section $$\mathcal{O}(d)(U_i)$$는

$$\x_i^d \cdot \mathbb{K}[\x_0/\x_i, \ldots, \widehat{\x_i/\x_i}, \ldots, \x_n/\x_i]$$

인 것을 기억하자. ([§선다발과 벡터다발, ⁋예시 12](/ko/math/algebraic_geometry/line_bundles#ex12)) 그럼 Čech cochain $$f \in \check{C}^p(\mathcal{U}, \mathcal{O}(d))$$은 각각의 $$(p+1)$$-tuple $$(i_0, \ldots, i_p)$$에 대해 열린집합 $$U_{i_0}\cap\cdots\cap U_{i_p}$$ 위에서 regular한 section을 대응시키는 것이다. 이 때, 교집합 $$U_{i_0}\cap\cdots\cap U_{i_p}$$ 위에서 section이 regular하기 위해서는 $$0$$이 되지 않는 좌표들, 즉 $$\x_{i_0}, \ldots, \x_{i_p}$$들만 분모로 허용되고, 나머지는 허용되지 않는 monomial들

$$f_{i_0 \cdots i_p} = \x_0^{a_0} \cdots \x_n^{a_n},\qquad \sum_{j=0}^n a_j=d,\quad a_j\geq 0\text{ for $j\not\in \{i_0, \ldots, i_p\}$}$$

로 생성된다.

Coboundary map $$\delta : \check{C}^p \to \check{C}^{p+1}$$의 경우,

$$(\delta f)_{i_0 \cdots i_{p+1}} = \sum_{k=0}^{p+1} (-1)^k f_{i_0 \cdots \hat{i_k} \cdots i_{p+1}}$$

로 주어진다. 각 $$(p+1)$$-tuple에서 하나의 index를 생략한 $$p$$-tuple에 대응하는 섹션들을 교대로 합하는 것이다.

이제 이들 데이터를 이용하여 각각의 cohomology group들을 계산하자. $$\mathbb{P}^1$$의 경우부터 살펴보면, Čech complex는

$$0 \longrightarrow \check{C}^0\overset{\delta}{\longrightarrow}\check{C}^1\longrightarrow 0$$

로 주어진다. 여기서

$$\check{C}^0=\mathcal{O}(d)(U_0)\oplus \mathcal{O}(d)(U_1),\qquad \check{C}^1=\mathcal{O}(d)(U_0\cap U_1)$$

이며, 각각의 section space는

$$\mathcal{O}(d)(U_0) = \x_0^d \cdot \mathbb{K}[\x_1/\x_0], \qquad \mathcal{O}(d)(U_1) = \x_1^d \cdot \mathbb{K}[\x_0/\x_1], \qquad \mathcal{O}(d)(U_0 \cap U_1) = \mathbb{K}[\x_0^{\pm 1}, \x_1^{\pm 1}]_d$$

이다. 우선 $$\check{C}^0$$에서의 cohomology를 계산하기 위해 $$\ker\delta$$를 분석하자. $$H^0(\mathbb{P}^n, \mathcal{O}(d))=\Gamma(\mathbb{P}^n, \mathcal{O}(d))$$이므로 이는 사실 [§선다발과 벡터다발, ⁋예시 16](/ko/math/algebraic_geometry/line_bundles#ex16)의 계산을 재확인하는 것에 불과하지만, 별도의 예시 대신 이 증명에서 Čech cohomology의 계산을 하는 것으로 하자.

정의에 의해 cochain $$(f_0, f_1) \in \check{C}^0$$이 $$\ker \delta$$에 속한다는 것은 $$f_0 = f_1$$이 $$\mathcal{O}(d)(U_0 \cap U_1)$$에서 성립한다는 뜻이다. 우선 $$U_0$$ 부분을 보면, 임의의 monomial이 $$\mathcal{O}(d)(U_0)$$에 속하기 위해서는 반드시 적당한 $$a\geq 0$$에 대하여 $$\x_0^{d-a}\x_1^a$$ 꼴임을 안다. 비슷하게 어떠한 monomial이 $$\mathcal{O}(d)(U_1)$$에 속하기 위해서는 적당한 $$b\geq 0$$에 대하여 $$\x_0^b\x_1^{d-b}$$의 꼴이어야 한다. 이제 특정 cocycle $$(f_0,f_1)$$이 $$\ker\delta$$에 속하기 위해서는 $$f_0=f_1$$이어야 하고, 따라서 $$a+b=d$$를 만족하는 monomial들만이 $$\ker\delta$$에 속할 수 있다. 즉, 다음의 monomial들

$$\x_0^d, \quad\x_0^{d-1}\x_1,\quad\ldots, \quad\x_0\x_1^{d-1},\quad \x_1^d$$

이 $$H^0$$의 basis이고 이것이 원하는 결과를 준다. 만일 $$d<0$$이라면 $$a,b\geq 0$$은 이 식을 만족시키지 못하므로 $$H^0$$은 $$0$$이 된다.

이제 $$H^1$$을 계산하자. 즉 $$\coker\delta$$를 계산해야 한다. 위의 계산으로부터, $$\delta$$의 image는 적당한 상수 $$a_i,b_j$$들에 대하여

$$f_1-f_0=\sum_{i\geq 0}a_i \x_0^{d-i}\x_1^i-\sum_{j\geq 0}b_j\x_0^j\x_1^{d-j}\tag{$\ast$}$$

임을 안다. 한편 $$\check{C}^1$$의 원소는 $$d$$차 monomial들

$$\x_0^{2d}\x_1^{-d},\quad,\x_0^{2d-1}\x_1^{-d+1}, \quad, \ldots,\quad \x_0^{-d+1}\x_1^{2d-1},\quad\x_0^{-d}\x_1^{2d}\tag{$\ast\ast$}$$

로 생성된다. 만일 $$d\geq 0$$이라면, 이들 각각은 위의 ($$\ast$$)으로부터 명시적으로 얻어질 수 있다. 가령 $$\x_0^{2d}\x_1^{-d}$$는 $$f_1$$의 성분 중 $$j=2d$$항에서 얻을 수 있고, $$\x_0^{-d}\x_1^{2d}$$는 $$f_0$$의 성분 중에서 $$i=2d$$ 항으로부터 얻을 수 있다. 따라서 이 경우 $$\coker\delta=0$$이다. 그러나 만일 $$d<0$$이라면 $$\delta$$의 image로 나타낼 수 없는 monomial들이 생기는데, 이는 ($$\ast$$)를 이루는 각 항들을 분석해보면 적어도 하나의 지수가 $$0$$보다 크거나 같기 때문이다. 반면 ($$\ast\ast$$)에서는 두 지수가 모두 음수인 monomial들

$$\x_0^{-1}\x_1^{d+1}, \quad \x_0^{-2}\x_1^{d+2},\quad,\ldots, \x_0^{d+1}\x_1^{-1}$$

이 생기며 이들이 $$\coker \delta$$를 생성한다. 주장의 표기법에 대해서는 증명이 끝난 후 별도로 설명하기로 한다.

이제 일반적인 경우를 위해 귀납법을 사용하자. 이를 위해 $$\mathbb{P}^n$$의 hyperplane $$H=\{\x_n=0\}$$이 $$\mathbb{P}^{n-1}$$과 isomorphic하다는 점을 이용하기 위해, 다음의 short exact sequence

$$0 \longrightarrow \mathcal{O}(d-1)\overset{\times \x_n}{\longrightarrow} \mathcal{O}(d)\longrightarrow \mathcal{O}(d)\vert_H\longrightarrow 0$$

를 생각하자. 그럼 이로부터 long exact sequence

$$\cdots \to H^{i-1}(\mathbb{P}^{n-1}, \mathcal{O}(d)) \to H^i(\mathbb{P}^n, \mathcal{O}(d-1)) \to H^i(\mathbb{P}^n, \mathcal{O}(d)) \to H^i(\mathbb{P}^{n-1}, \mathcal{O}(d)) \to \cdots$$

를 얻고 우리는 귀납적 과정에 의해 $$\mathbb{P}^{n-1}$$에서의 주장은 알고 있다. 그럼 특히 $$0<i< n$$에 대해서는

$$H^{i-1}(\mathbb{P}^{n-1}, \mathcal{O}(d))=H^i(\mathbb{P}^{n-1}, \mathcal{O}(d))=0$$

이 성립하고, 이로부터 $$H^i(\mathbb{P}^n, \mathcal{O}(d-1)) \cong H^i(\mathbb{P}^n, \mathcal{O}(d))$$를 얻는다. 즉 모든 $$d$$에 대해서 $$H^i(\mathbb{P}^n, \mathcal{O}(d))$$는 isomorphic하며, 특히 만만한 $$\mathcal{O}$$에 대한 Čech cohomology

$$H^i(\mathbb{P}^n, \mathcal{O}(d))=H^i(\mathbb{P}^n, \mathcal{O})=0$$

임을 바로 보일 수 있으므로 이로부터

$$H^i(\mathbb{P}^n, \mathcal{O}(d))=0$$

이 모든 $$0<i<n$$과 모든 $$d$$에 대해 성립함을 안다.

이제 top cohomology 부분

$$\cdots\rightarrow H^{n-1}(\mathbb{P}^{n-1}, \mathcal{O}(d))\rightarrow H^n(\mathbb{P}^n, \mathcal{O}(d-1))\rightarrow H^n(\mathbb{P}^n, \mathcal{O}(d))\rightarrow H^n(\mathbb{P}^{n-1}, \mathcal{O}(d))=0$$

을 보자. 만일 $$d\geq -n$$이라면, 다시 귀납적 가정으로부터 $$H^{n-1}(\mathbb{P}^{n-1}, \mathcal{O}(d))=0$$이므로 위와 마찬가지 논증으로 $$H^n(\mathbb{P}^n, \mathcal{O}(d))$$가 모든 $$d>-n-1$$에 대해 성립하는 것을 보일 수 있다. $$d\leq -n-1$$인 경우, $$H^n$$은 Čech complex로부터 직접 계산해야 하는데, 이를 위해 $$\check{C}^n(\mathbb{P}^n, \mathcal{O}(d))$$를 직접 계산하면 $$n$$-cochain은

$$\mathbb{K}[\x_0^{\pm 1}, \ldots, \x_n^{\pm 1}]_d$$

의 원소임을 알고, $$n-1$$-cochain의 image로 나타나지 않는 monomial들은 앞선 $$\mathbb{P}^1$$에서의 계산과 유사하게 <em-ko>모든</em-ko> 지수가 $$-1$$보다 작은 $$d$$차식이며 이로부터 원하는 결과를 얻는다. $$H^0$$의 경우는, 위에서는 직접 계산해보았지만, 이미 언급했듯 이는 [§선다발과 벡터다발, ⁋예시 16](/ko/math/algebraic_geometry/line_bundles#ex16)의 재확인에 불과하므로 여기서는 굳이 반복하지 않기로 한다.

</details>

위 증명에서 우리는 각 변수 $$\x_0,\cdots, \x_n$$ 그리고 $$d\leq -n-1$$에 대하여, $$H^n(\mathbb{P}^n, \mathcal{O}(d))$$가 다음의 monomial들

$$\x_0^{a_0} \cdots \x_n^{a_n},\qquad  a_i \leq -1, \quad \sum a_i=d$$

로 생성됨을 보았다. ($$d$$가 음수임에 유의하자.) 이는 각각의 $$\x_i^{-1}$$들을 새로운 변수 $$\y_i=\x_i^{-1}$$로 생각하였을 때, 다음 식

$$\y_0^{\lvert a_0\rvert},\cdots \y_n^{\lvert a_n\rvert}\qquad \lvert a_i\rvert\geq 1,\quad \sum \lvert a_i\rvert=\lvert d\rvert$$

들로 생성되는 공간이라 하여도 된다. 여기서 각각의 $$a_i$$와 $$d$$는 모두 음수이므로 $$\lvert a_i\rvert=-a_i$$, $$\lvert d\rvert=-d$$이다. 위의 공간은 거의 degree $$\lvert d\rvert$$ homogeneous polynomial들의 공간과 유사하지만, $$\lvert a_i\rvert$$들이 $$0$$이 될 수 없다는 차이점이 있다. 따라서 $$b_i=\lvert a_i\rvert-1$$으로 치환하면, 우리는 이 공간을 

$$\y_0^{b_i}\cdots \y_n^{b_n},\qquad b_i\geq 0,\quad \sum b_i=\lvert d\rvert-(n+1)$$

들의 공간으로 생각할 수 있다. 즉, 이 공간은 degree $$-d-n-1$$ "negative degree" monomial들의 공간으로 생각할 수 있고, 이러한 이유로 이 공간을 

$$\mathbb{K}[\x_0^{-1}, \ldots, \x_n^{-1}]_{-d-n-1}$$

으로 표기한다. 

한편 나중을 위해 우리는 Euler characteristic을 정의한다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> Variety $$X$$와 그 위에 정의된 coherent sheaf $$\mathcal{F}$$에 대하여, $$\mathcal{F}$$의 *Euler characteristic<sub>오일러 지표</sub>*을 다음의 식

$$\rchi(X, \mathcal{F}) = \sum_{i=0}^{n} (-1)^i \dim H^i(X, \mathcal{F})$$

으로 정의한다. 

</div>

특별히 $$X=\mathbb{P}^n$$이고 $$\mathcal{F}=\mathcal{O}(d)$$인 경우, 어차피 어느 경우에서건 중간 cohomology들은 모두 죽고 양 끝의 cohomology만 고려하면 되므로 다음 따름정리를 쉽게 증명할 수 있다. 

<div class="proposition" markdown="1">

<ins id="cor2">**따름정리 2**</ins> $$\mathbb{P}^n$$ 위의 $$\mathcal{O}(d)$$의 Euler characteristic:

$$\rchi(\mathbb{P}^n, \mathcal{O}(d)) = \binom{n+d}{n}$$
ㅇ
</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Bott's formula에 의해 cohomology는 세 가지 경우로 나뉜다. 

첫째, $$d \geq 0$$인 경우 $$H^0$$만 non-zero이므로 

$$\rchi(\mathcal{O}(d)) = \dim H^0(\mathbb{P}^n, \mathcal{O}(d)) = \dim \mathbb{K}[\x_0, \ldots, \x_n]_d = \binom{n+d}{n}$$

가 성립하는 것을 알 수 있다. 

둘째로, 만일 $$-n \leq d \leq -1$$인 경우 모든 cohomology가 사라지므로 $$\rchi(\mathcal{O}(d)) = 0$$이고, 이런 경우 보통 $$\binom{n+d}{n}=0$$으로 정의하므로 convention과 잘 맞아떨어진다. 

마지막으로 $$d \leq -n-1$$인 경우를 생각하자. 이 경우, $$H^n$$만 non-zero이므로 

$$\rchi(\mathcal{O}(d)) = (-1)^n \dim \mathbb{K}[\x_0^{-1}, \ldots, \x_n^{-1}]_{-d-n-1}$$

이다. [명제 1](#prop1) 직후의 설명에 의하면, 이 공간의 차원은 

$$\binom{-d-1}{n}=(-1)^n\binom{n+d}{n}$$

임을 안다. 여기서 $$\binom{n+d}{n}$$은 위의 경우와 마찬가지로 이항계수 표기에 대한 일반적인 convention을 따랐다.

</details>

Euler characteristic은 short exact sequence에 대해 가산적(additive)이라는 중요한 성질을 갖는다. 즉, short exact sequence $$0 \to \mathcal{F} \to \mathcal{G} \to \mathcal{H} \to 0$$에 대해 $$\rchi(\mathcal{G}) = \rchi(\mathcal{F}) + \rchi(\mathcal{H})$$가 성립한다. 따라서 Euler characteristic은 개별 cohomology group의 정보를 잃는 대신, 계산과 조작이 훨씬 용이한 불변량이 된다.

## Regularity

우리가 실제로 임의의 coherent sheaf의 cohomology 계산을 할 때 중요한 도구는, 이전에도 살펴보았고, [명제 1](#prop1)의 증명에서도 살펴보았듯 long exact sequence이다. 즉 우리의 

지금까지 우리는 $$\mathcal{O}(d)$$라는 매우 특수한 sheaf의 cohomology를 계산하였다. 그러나 대수기하학에서 실제로 마주치는 sheaf는 임의의 coherent sheaf $$\mathcal{F}$$이며, 이의 cohomology를 모두 계산하는 것은 일반적으로 불가능하다. 다행히도 coherent sheaf의 cohomology를 다룰 때, “충분히 twist하면 high cohomology가 vanish한다”는 현상이 자주 나타난다. 이는 Serre vanishing theorem으로 정밀화된다: 임의의 coherent sheaf $$\mathcal{F}$$에 대해 충분히 큰 $$m$$에 대해 $$H^i(\mathbb{P}^n, \mathcal{F}(m)) = 0$$이 $$i > 0$$에 대해 성립한다. 예를 들어, Bott's formula에서 $$H^q(\mathbb{P}^n, \mathcal{O}(d))$$가 $$q > 0$$에서 vanish하는 $$d$$의 범위는 $$d \geq -n$$이다. Regularity는 이 현상을 정량화하여, 구체적으로 어느 정도 twist해야 higher cohomology가 사라지는지를 기록하는 개념이다.

Coherent sheaf를 다룰 때 한 가지 근본적인 어려움은, line bundle의 경우와 달리 global section이 항상 존재한다는 보장이 없다는 점이다. 예를 들어 $$\mathcal{O}(d)$$는 $$d \geq 0$$일 때만 non-zero global section을 갖지만, 일반적인 coherent sheaf $$\mathcal{F}$$에 대해서는 $$H^0(X, \mathcal{F})$$의 차원을 섣불리 예측할 수 없다. 그럼에도 불구하고, 충분히 많은 global section이 존재하여 각 점의 stalk를 모두 생성할 수 있다면, line bundle에서 하던 것처럼 evaluation map을 통해 projective embedding이나 morphism의 구성 등 다양한 기하학적 작업을 수행할 수 있다. 이러한 상황은 선형계(linear system)가 basepoint-free일 때와 정확히 유사하다. Basepoint-free linear system이 점마다 그 점에서 vanish하지 않는 section을 제공하듯이, globally generated sheaf는 stalk의 각 원소를 global section들의 값으로 생성할 수 있다.

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> Coherent sheaf $$\mathcal{F}$$가 *globally generated*라는 것은 evaluation map

$$H^0(X, \mathcal{F}) \otimes \mathcal{O}_X \to \mathcal{F}$$

가 surjective인 것이다. 즉, global section들로 stalk를 모두 생성할 수 있다.

</div>

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> Coherent sheaf $$\mathcal{F}$$ on $$\mathbb{P}^n$$이 *$$m$$-regular*라는 것은 $$i > 0$$에 대해 $$H^i(\mathbb{P}^n, \mathcal{F}(m-i)) = 0$$인 것이다.

</div>

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6 (Castelnuovo-Mumford Regularity)**</ins> $$\mathcal{F}$$가 $$m$$-regular이면 $$\mathcal{F}(m)$$은 globally generated이고, $$i > 0$$이고 $$k \geq m - i$$인 모든 $$i, k$$에 대해 $$H^i(\mathbb{P}^n, \mathcal{F}(k)) = 0$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Mumford의 증명 전략은 $$\mathbb{P}^n$$의 차원 $$n$$에 대한 귀납법이다. $$n = 0$$인 경우 coherent sheaf는 finite-dimensional vector space이고 모든 higher cohomology가 사라지므로 자명하다. 이제 $$n \geq 1$$이라 가정하자.

핵심은 hyperplane $$H \cong \mathbb{P}^{n-1}$$으로의 restriction을 이용하는 것이다. 일반적인 linear form $$s \in H^0(\mathbb{P}^n, \mathcal{O}(1))$$에 대해 다음 short exact sequence를 얻는다.

$$0 \to \mathcal{F}(k-1) \xrightarrow{\cdot s} \mathcal{F}(k) \to \mathcal{F}(k)\vert_H \to 0$$

이 sequence의 cohomology long exact sequence는 다음을 준다.

$$\cdots \to H^i(\mathcal{F}(k-1)) \to H^i(\mathcal{F}(k)) \to H^i(\mathcal{F}(k)\vert_H) \to H^{i+1}(\mathcal{F}(k-1)) \to \cdots$$

**1단계: $$\mathcal{F}$$가 $$(m+1)$$-regular임.** $$\mathcal{F}$$가 $$m$$-regular이므로 $$H^i(\mathcal{F}(m-i)) = 0$$이 $$i > 0$$에 대해 성립한다. 우선 $$\mathcal{F}\vert_H$$가 $$(m+1)$$-regular임을 보이자. Short exact sequence에서 $$k = m - i + 1$$ ($$i \geq 1$$)을 대입하면

$$0 \to \mathcal{F}(m-i) \to \mathcal{F}(m-i+1) \to \mathcal{F}(m-i+1)\vert_H \to 0$$

이고, 이의 long exact sequence에서

$$H^i(\mathcal{F}(m-i)) \to H^i(\mathcal{F}(m-i+1)) \to H^i(\mathcal{F}\vert_H(m-i+1)) \to H^{i+1}(\mathcal{F}(m-i))$$

이다. $$\mathcal{F}$$의 $$m$$-regularity에 의해 $$H^i(\mathcal{F}(m-i)) = 0$$ ($$i > 0$$)이고 $$H^{i+1}(\mathcal{F}(m-i)) = 0$$ ($$i+1 > 1$$)이므로, $$H^i(\mathcal{F}\vert_H(m-i+1)) = 0$$을 $$0 < i \leq n-1$$에 대해 얻는다. 이것은 $$\mathcal{F}\vert_H$$가 $$(m+1)$$-regular임을 의미한다.

이제 귀납적 가정을 $$H \cong \mathbb{P}^{n-1}$$에 적용한다. $$\mathcal{F}\vert_H$$가 $$(m+1)$$-regular이므로, 명제의 결론이 $$\mathbb{P}^{n-1}$$에서 성립한다고 가정하면 $$H^i(\mathcal{F}\vert_H(m+1-i+j)) = 0$$이 $$j \geq 0$$, $$0 < i \leq n-1$$에 대해 성립한다. 특히 $$j = 0$$일 때 $$H^i(\mathcal{F}(m+1-i)\vert_H) = 0$$이다.

다시 short exact sequence에서 $$k = m + 1 - i$$를 대입하면

$$H^i(\mathcal{F}(m+1-i)) \to H^i(\mathcal{F}(m+1-i)\vert_H) \to H^{i+1}(\mathcal{F}(m-i))$$

인데, $$H^i(\mathcal{F}(m+1-i)\vert_H) = 0$$ (위에서 귀납적 가정으로 얻음)이고 $$H^{i+1}(\mathcal{F}(m-i)) = 0$$ ($$m$$-regularity)이므로 $$H^i(\mathcal{F}(m+1-i)) = 0$$이다. 즉 $$\mathcal{F}$$는 $$(m+1)$$-regular이다. 귀납적으로 $$\mathcal{F}$$는 임의의 $$m' \geq m$$에 대해 $$m'$$-regular이며, 이로부터 $$k \geq m - i$$일 때 $$H^i(\mathcal{F}(k)) = 0$$이 성립한다.

**2단계: $$\mathcal{F}(m)$$은 globally generated.** Evaluation map $$\epsilon : H^0(\mathcal{F}(m)) \otimes \mathcal{O} \to \mathcal{F}(m)$$을 생각하자. 이 map이 surjective임을 보이기 위해, 임의의 점 $$p \in \mathbb{P}^n$$에서 fiber $$\mathcal{F}(m) \otimes \kappa(p)$$가 $$H^0(\mathcal{F}(m))$$의 상으로 생성됨을 보인다. $$p$$를 지나는 일반적인 hyperplane $$H$$를 택하고, 위의 short exact sequence에서 $$k = m$$을 대입하면

$$0 \to \mathcal{F}(m-1) \to \mathcal{F}(m) \to \mathcal{F}(m)\vert_H \to 0$$

이다. 여기서 $$H^1(\mathcal{F}(m-1)) = 0$$ ($$m$$-regularity에서 $$i = 1$$인 경우)이므로 $$H^0(\mathcal{F}(m)) \to H^0(\mathcal{F}(m)\vert_H)$$가 surjective이다. 귀납적 가정에 의해 $$\mathcal{F}(m)\vert_H$$는 $$H \cong \mathbb{P}^{n-1}$$ 위에서 globally generated이므로, $$\mathcal{F}(m)\vert_H$$의 fiber at $$p$$는 $$H^0(\mathcal{F}(m)\vert_H)$$의 상으로 생성된다. $$H^0(\mathcal{F}(m)) \to H^0(\mathcal{F}(m)\vert_H)$$가 surjective이므로, $$\mathcal{F}(m)$$의 global section들도 $$p$$에서의 fiber를 생성한다. 따라서 $$\mathcal{F}(m)$$은 globally generated이다.

</details>

<div class="example" markdown="1">

<ins id="ex7">**예시 7**</ins> Line bundle $$\mathcal{O}(d)$$의 regularity를 계산해보자. $$d \geq 0$$이면 Bott's formula에 의해 $$H^i(\mathbb{P}^n, \mathcal{O}(d)) = 0$$이 $$i > 0$$에 대해 성립한다. 그런데 $$\mathcal{O}(d)$$의 $$m$$-regularity 조건은 $$H^i(\mathcal{O}(d+m-i)) = 0$$ ($$i > 0$$)이다. $$m = 0$$을 택하면 $$H^i(\mathcal{O}(d-i))$$를 확인해야 하는데, $$i = 1$$일 때 $$H^1(\mathcal{O}(d-1))$$은 $$d \geq 1$$이면 $$0$$이지만 $$d = 0$$이면 $$H^1(\mathcal{O}(-1)) = 0$$ (Bott's formula에서 $$-1$$은 $$-1 \geq -n$$이므로 모든 cohomology가 $$0$$)이다. 일반적으로 $$d \geq 0$$이고 $$i > 0$$일 때 $$d - i \geq -n$$이면 $$H^i(\mathcal{O}(d-i)) = 0$$이다. 문제는 $$d - i < -n$$, 즉 $$i > d + n$$인 경우인데, 이때 $$i > n$$이 되어 어차피 $$H^i = 0$$이다. 따라서 $$\mathcal{O}(d)$$는 $$0$$-regular이다. 반면 $$d < 0$$인 경우, $$\mathcal{O}(d)$$는 $$(-d)$$-regular이다. 명제 6에 의해 $$\mathcal{O}(d)$$는 $$d \geq 0$$일 때 globally generated이며, 이는 ([§선다발과 벡터다발, ⁋예시 16](/ko/math/algebraic_geometry/line_bundles#ex16))에서 확인한 바와 일치한다.

</div>

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.
**[Bot]** R. Bott, *Homogeneous vector bundles*, Annals of Mathematics, 1957.
**[Mum]** D. Mumford, *Lectures on Curves on an Algebraic Surface*, Annals of Mathematics Studies, Princeton, 1966.
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      