---
title: "사영공간의 코호몰로지"
description: "층 코호몰로지는 고차 코호몰로지 군을 포함하는 더 풍부한 불변량이며, 사영공간 위의 선다발에 대해 Bott 공식으로 이를 완전히 계산한다. Čech 코호몰로지를 활용한 증명을 포함한다."
excerpt: "Bott's formula and the cohomology of line bundles on projective space"

categories: [Math / Algebraic Varieties]
permalink: /ko/math/algebraic_varieties/cohomology_of_projective_spaces
sidebar:
    nav: "algebraic_varieties-ko"

header:
    overlay_image: /assets/images/Math/Algebraic_Varieties/Cohomology_of_Line_Bundles.png
    overlay_filter: 0.5

date: 2026-04-06
last_modified_at: 2026-05-09
weight: 13
---

우리는 일찍이 [§선다발과 벡터다발, ⁋예시 16](/ko/math/algebraic_varieties/line_bundles#ex16)에서 line bundle $$\mathcal{O}(d)$$를 정의하고, 그 global section $$H^0(\mathbb{P}^n, \mathcal{O}(d))$$이 degree $$d$$의 homogeneous polynomial들과 동형임을 확인하였다. 그러나 우리가 이전 글에서 도입한 sheaf cohomology ([§층 코호몰로지, ⁋정의 1](/ko/math/algebraic_varieties/sheaf_cohomology#def1))는 $$H^0$$뿐만 아니라 higher cohomology group들 $$H^1, H^2, \ldots$$까지 포함하는 더 풍부한 불변량이므로, 이제 우리는 $$H^0$$ 뿐만 아니라 higher cohomology group들을 사용하여 $$\mathcal{O}(d)$$의 정보를 모두 알아낼 것이다.

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

인 것을 기억하자. ([§선다발과 벡터다발, ⁋예시 12](/ko/math/algebraic_varieties/line_bundles#ex12)) 그럼 Čech cochain $$f \in \check{C}^p(\mathcal{U}, \mathcal{O}(d))$$은 각각의 $$(p+1)$$-tuple $$(i_0, \ldots, i_p)$$에 대해 열린집합 $$U_{i_0}\cap\cdots\cap U_{i_p}$$ 위에서 regular한 section을 대응시키는 것이다. 이 때, 교집합 $$U_{i_0}\cap\cdots\cap U_{i_p}$$ 위에서 section이 regular하기 위해서는 $$0$$이 되지 않는 좌표들, 즉 $$\x_{i_0}, \ldots, \x_{i_p}$$들만 분모로 허용되고, 나머지는 허용되지 않는 monomial들

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

이다. 우선 $$\check{C}^0$$에서의 cohomology를 계산하기 위해 $$\ker\delta$$를 분석하자. $$H^0(\mathbb{P}^n, \mathcal{O}(d))=\Gamma(\mathbb{P}^n, \mathcal{O}(d))$$이므로 이는 사실 [§선다발과 벡터다발, ⁋예시 16](/ko/math/algebraic_varieties/line_bundles#ex16)의 계산을 재확인하는 것에 불과하지만, 별도의 예시 대신 이 증명에서 Čech cohomology의 계산을 하는 것으로 하자.

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

를 얻고 우리는 귀납적 과정에 의해 $$\mathbb{P}^{n-1}$$에서의 주장은 알고 있다. 그럼 특히 $$0<i<n$$에 대해서는

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

의 원소임을 알고, $$n-1$$-cochain의 image로 나타나지 않는 monomial들은 앞선 $$\mathbb{P}^1$$에서의 계산과 유사하게 <em-ko>모든</em-ko> 지수가 $$-1$$보다 작은 $$d$$차식이며 이로부터 원하는 결과를 얻는다. $$H^0$$의 경우는, 위에서는 직접 계산해보았지만, 이미 언급했듯 이는 [§선다발과 벡터다발, ⁋예시 16](/ko/math/algebraic_varieties/line_bundles#ex16)의 재확인에 불과하므로 여기서는 굳이 반복하지 않기로 한다.

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

<ins id="cor3">**따름정리 3**</ins> $$\mathbb{P}^n$$ 위의 $$\mathcal{O}(d)$$의 Euler characteristic은 다음의 식

$$\rchi(\mathbb{P}^n, \mathcal{O}(d)) = \binom{n+d}{n}$$


으로 주어진다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

[명제 1](#prop1)에 의해 cohomology는 세 가지 경우로 나뉜다.

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

Euler characteristic은 short exact sequence에 대해 additivity라는 중요한 성질을 갖는다. 즉, short exact sequence 

$$0 \to \mathcal{F} \to \mathcal{G} \to \mathcal{H} \to 0$$

에 대해 $$\rchi(\mathcal{G}) = \rchi(\mathcal{F}) + \rchi(\mathcal{H})$$가 성립한다. 따라서 Euler characteristic은 개별 cohomology group의 정보를 잃는 대신, 계산과 조작이 훨씬 용이한 불변량이 된다.

## Serre Vanishing

[명제 1](#prop1)에 따르면, $$\mathbb{P}^n$$ 위에서는 충분히 큰 $$d$$에 대해 $$\mathcal{O}(d)$$의 higher cohomology가 모두 사라진다. $$\mathbb{P}^n$$ 위의 임의의 line bundle은 모두 어떠한 $$d$$에 대하여 $$\mathcal{O}(d)$$의 꼴이므로, 이는 $$\mathbb{P}^n$$의 임의의 line bundle $$\mathcal{L}$$에 대하여, 충분히 큰 $$d\gg 0$$에 대하여 $$\mathcal{O}(d)$$를 사용한 twisted line bundle

$$\mathcal{L}\otimes \mathcal{O}(d)$$

은 반드시 higher cohomology가 $$0$$이라는 것을 의미한다. 

더 일반적으로 우리는 이를 임의의 projective variety와 그 위에 정의된 임의의 coherent sheaf로 확장할 수 있다. 이를 위해서는 우선 $$\mathcal{O}(1)$$의 역할을 할 것이 필요한데, 우리의 정의에서 projective variety $$X$$는 항상 embedding $$X\hookrightarrow\mathbb{P}^N$$으로 주어지므로 $$\mathbb{P}^N$$ 위의 $$\mathcal{O}(1)$$들을 끌어오면 된다. 

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4 (Serre Vanishing)**</ins> $$X$$를 projective variety, $$\mathcal{L}$$을 ample line bundle, $$\mathcal{F}$$를 coherent sheaf라 하자. 그럼 충분히 큰 $$m$$에 대해

$$H^i(X, \mathcal{F} \otimes \mathcal{L}^{\otimes m}) = 0 \quad (i > 0)$$

이 성립한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$\mathcal{L}$$이 ample이므로, 충분히 큰 $$m_0$$에 대해 $$\mathcal{L}^{\otimes m_0}$$은 very ample이다. 즉, 적당한 embedding $$i \colon X \hookrightarrow \mathbb{P}^N$$이 존재하여 $$\mathcal{L}^{\otimes m_0} = i^*\mathcal{O}(1)$$이 성립한다. $$\mathbb{P}^N$$의 standard affine cover $$\{U_i\}$$를 $$X$$에 restrict하면 affine open cover $$\{X \cap U_i\}$$를 얻는다. Finite intersection $$U_{i_0} \cap \cdots \cap U_{i_p}$$은 affine이므로 $$(X \cap U_{i_0}) \cap \cdots \cap (X \cap U_{i_p}) = X \cap (U_{i_0} \cap \cdots \cap U_{i_p})$$도 affine이다. 따라서 두 Čech complex가 literally 같으므로

$$\check{H}^i(\{X \cap U_j\}, \mathcal{F}) = \check{H}^i(\{U_j\}, i_*\mathcal{F})$$

이 성립한다. $$X$$와 $$\mathbb{P}^N$$은 separated scheme이므로 ([§층 코호몰로지, ⁋정리 11](/ko/math/algebraic_varieties/sheaf_cohomology#thm11)), quasi-coherent sheaf에 대해 Čech cohomology = sheaf cohomology:

$$H^i(X, \mathcal{F}) = \check{H}^i(\{X \cap U_j\}, \mathcal{F}) = \check{H}^i(\{U_j\}, i_*\mathcal{G}) = H^i(\mathbb{P}^N, i_*\mathcal{G})$$ 따라서 다음을 보이면 충분하다: $$\mathbb{P}^N$$ 위의 coherent sheaf $$\mathcal{G}$$에 대해, 충분히 큰 $$n$$에 대해 $$H^i(\mathbb{P}^N, \mathcal{G}(n)) = 0$$ ($$i > 0$$). 여기서 $$\mathcal{G}(n) = \mathcal{G} \otimes \mathcal{O}_{\mathbb{P}^N}(n)$$이다.

**핵심 보조정리**. $$\mathcal{G}(n)$$이 충분히 큰 $$n$$에 대해 globally generated임을 보인다. (아래 [정의 6](#def6) 참조.)

$$S = \mathbb{K}[\x_0, \ldots, \x_N]$$로 하고, $$M = \bigoplus_{n \in \mathbb{Z}} \Gamma(\mathbb{P}^N, \mathcal{G}(n))$$을 연결 graded $$S$$-module이라 하자. 각 표준 affine 열린집합 $$D_+(\x_j)$$ 위에서, $$\Gamma(D_+(\x_j), \mathcal{G})$$는 degree-0 localisation $$M_{(\x_j)}$$이고, 이는 $$S_{(\x_j)}$$ 위의 finitely generated module이다. Generator들 $$\bar{m}_1, \ldots, \bar{m}_{r_j} \in M_{(\x_j)}$$을 택하자. 각 $$\bar{m}_k$$는 $$m_k / \x_j^{d_k}$$ 꼴로 쓸 수 있으며, 여기서 $$m_k \in M$$은 homogeneous element이다. $$d_0 = \max_j \max_k d_k$$로 하면, 각 generator에 $$\x_j^{d_0 - d_k}$$를 곱하여 homogeneous element $$m_k \cdot \x_j^{d_0 - d_k} \in M_{d_0}$$를 얻는다. 이는 $$\Gamma(\mathbb{P}^N, \mathcal{G}(d_0))$$의 원소이며, $$D_+(\x_j)$$ 위에서 $$\mathcal{G}$$의 stalk를 생성함을 알 수 있다. $$j$$에 대한 최대값을 취하면, $$\mathcal{G}(d_0)$$이 globally generated임을 얻는다.

**Vanishing**. 이제 $$H^i(\mathbb{P}^N, \mathcal{G}(n)) = 0$$ ($$i > 0$$, $$n \gg 0$$)을 보인다.

$$N = 0$$인 경우 $$\mathbb{P}^0$$은 한 점이므로 자명하다. $$N \geq 1$$이라 하자. 위의 보조정리에 의해 $$\mathcal{G}(n_0)$$은 globally generated ($$n_0 \gg 0$$)이므로, 적당한 surjection

$$\mathcal{O}_{\mathbb{P}^N}^{\oplus r_0} \twoheadrightarrow \mathcal{G}(n_0)$$

이 존재한다. Kernel $$\mathcal{K}_0$$는 coherent하다. Short exact sequence

$$0 \to \mathcal{K}_0 \to \mathcal{O}^{\oplus r_0} \to \mathcal{G}(n_0) \to 0$$

의 long exact sequence에서, [명제 1](#prop1)에 의해 $$H^j(\mathbb{P}^N, \mathcal{O}^{\oplus r_0}) = 0$$ ($$j > 0$$)이므로,

$$H^j(\mathcal{G}(n_0)) \cong H^{j+1}(\mathcal{K}_0) \quad (j \geq 1)$$

을 얻는다. 이제 $$\mathcal{K}_0$$에 대해 같은 과정을 반복한다. 즉, $$\mathcal{K}_0(n_1)$$이 globally generated인 $$n_1 \gg 0$$을 택하고, surjection

$$\mathcal{O}^{\oplus r_1} \twoheadrightarrow \mathcal{K}_0(n_1)$$

의 kernel $$\mathcal{K}_1$$에 대해

$$0 \to \mathcal{K}_1 \to \mathcal{O}^{\oplus r_1} \to \mathcal{K}_0(n_1) \to 0$$

의 long exact sequence에서

$$H^{j+1}(\mathcal{K}_0(n_1)) \cong H^{j+2}(\mathcal{K}_1) \quad (j \geq 1)$$

을 얻는다. 이 과정을 $$N$$회 반복하면

$$H^j(\mathcal{G}(n_0)) \cong H^{j+N}(\mathcal{K}_{N-1})$$

을 얻는다. $$\mathbb{P}^N$$의 cohomological dimension은 $$N$$이므로 $$H^{j+N} = 0$$ ($$j \geq 1$$, $$j + N \geq N+1 > N$$), 따라서 $$H^j(\mathcal{G}(n_0)) = 0$$이다.

마지막으로, $$\mathcal{G}(n_0)$$이 globally generated이므로 $$\mathcal{G}(n) = \mathcal{G}(n_0) \otimes \mathcal{O}(n - n_0)$$ 역시 $$n \geq n_0$$에 대해 globally generated이고, 따라서 위와 동일한 resolution 인자를 $$\mathcal{G}(n)$$에 대해서도 구성할 수 있으므로 vanishing은 $$n \geq n_0$$인 모든 $$n$$에 대해 성립한다.

</details>

## Regularity

[명제 4](#prop4)는 higher cohomology가 충분히 큰 twisting 후 vanish한다는 qualitative한 결과를 주었다. Regularity는 이를 정량화하여, 구체적으로 얼마만큼의 twisting이 필요한지를 측정하는 개념이다.

직관적으로 higher cohomology는 낮은 degree cohomology에서의 실패로 인해 생기는 것이므로, 이 twisting은 높은 차수에서는 "덜" 필요하다. 이를 염두에 두면 다음의 정의가 자연스럽다.

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> Projective variety $$X$$와 그 위의 ample line bundle $$\mathcal{L}$$이 고정되었다고 하자. 그럼 $$X$$ 위의 coherent sheaf $$\mathcal{F}$$가 *$$m$$-regular*라는 것은 모든 $$i>0$$에 대하여

$$H^i(X, \mathcal{F} \otimes \mathcal{L}^{\otimes m - i}) = 0$$

이 성립하는 것이다.

</div>

일반적으로 coherent sheaf의 cohomology를 모두 계산하는 것은 거의 불가능하지만, 충분히 twist하면 higher cohomology가 vanish한다는 것이 우리의 기본적인 아이디어이다. Regularity는 여기에서 더 나아가, 구체적으로 얼마만큼의 twisting이 필요한지를 측정해주는 개념이다. 

Coherent sheaf를 다룰 때 이러한 twisting이 유용해지는 핵심적인 이유 중 하나는, 충분히 twist하면 coherent sheaf가 *globally generated*가 되기 때문이다. 이 개념의 직관을 얻기 위해 우선 line bundle의 경우를 생각해보자. Line bundle $$\mathcal{L}$$이 [§선형계, ⁋정의 5](/ko/math/algebraic_varieties/linear_systems#def5)에서 정의된 바와 같이 *basepoint-free*라는 것은, 모든 점 $$p \in X$$에 대해 $$s(p) \neq 0$$인 global section $$s \in H^0(X, \mathcal{L})$$가 존재한다는 뜻이다. 즉 base locus가 비어있어, linear system $$\lvert \mathcal{L} \rvert$$가 각 점에서 반드시 nonzero 값을 제공한다. 이는 evaluation map

$$H^0(X, \mathcal{L}) \otimes \mathcal{O}_X \to \mathcal{L}$$

이 surjective인 것과 동치이다. *Globally generated*는 이 조건을 임의의 coherent sheaf로 일반화한 것이다: coherent sheaf $$\mathcal{F}$$가 globally generated라는 것은, 마찬가지로 위와 같은 형태의 evaluation map이 surjective가 되어 global section들로 각 점의 stalk를 모두 생성할 수 있다는 의미이다. 특히 line bundle의 경우에는 globally generated인 것과 basepoint-free인 것이 동치이다. 이 성질은 [명제 4](#prop4)의 증명에서도 핵심적인 역할을 하였다.

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> Coherent sheaf $$\mathcal{F}$$가 *globally generated*라는 것은 evaluation map

$$H^0(X, \mathcal{F}) \otimes \mathcal{O}_X \to \mathcal{F}$$

가 surjective인 것이다. 즉, global section들로 stalk를 모두 생성할 수 있다.

</div>

Regularity를 일반적으로 정의하기 위해서는, 우선 twist의 개념이 필요하다. $$\mathbb{P}^n$$에서는 $$\mathcal{O}(1)$$을 기본으로 사용하므로 $$\mathcal{F}(d) := \mathcal{F} \otimes \mathcal{O}(d)$$로 쓴다. 임의의 projective variety $$X$$ 위에서는 ample line bundle $$\mathcal{L}$$을 택하고 $$\mathcal{F}(d) := \mathcal{F} \otimes \mathcal{L}^{\otimes d}$$로 정의한다. Twist는 다음의 성질들을 만족한다. Tensor product의 결합법칙에 의해 $$\mathcal{F}(d)(e) = \mathcal{F}(d+e)$$가 성립한다. 또한, tensor product functor $$- \otimes \mathcal{L}^{\otimes d}$$는 line bundle이므로 exact이고, 따라서 short exact sequence

$$0 \to \mathcal{F} \to \mathcal{G} \to \mathcal{H} \to 0$$

에 대해

$$0 \to \mathcal{F}(d) \to \mathcal{G}(d) \to \mathcal{H}(d) \to 0$$

역시 short exact sequence가 된다.


<div class="proposition" markdown="1">

<ins id="prop7">**명제 7 (Castelnuovo-Mumford Regularity)**</ins> $$X$$를 projective variety, $$\mathcal{L}$$을 ample line bundle, $$\mathcal{F}$$를 coherent sheaf라 하자. $$\mathcal{F}$$가 $$\mathcal{L}$$에 대해 $$m$$-regular이면 다음이 성립한다.

1. $$\mathcal{F} \otimes \mathcal{L}^{\otimes m}$$은 globally generated이다.
2. $$\mathcal{F} \otimes \mathcal{L}^{\otimes p}$$는 모든 $$p \geq 0$$에 대해 $$\mathcal{L}$$에 대해 $$(m+p)$$-regular이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$X$$의 차원에 대한 귀납법으로 증명한다. $$\dim X = 0$$인 경우 $$X$$는 한 점이고 coherent sheaf $$\mathcal{F}$$는 finite-dimensional vector space이므로 $$H^0$$ 이외의 cohomology는 자동으로 사라진다. 이제 $$\dim X \geq 1$$이라 가정하자.

핵심은 $$\mathcal{L}$$의 global section $$s \in H^0(X, \mathcal{L})$$으로 정의되는 effective divisor $$D$$에 대한 restriction exact sequence를 이용하는 것이다. 일반적인 $$s$$를 택하면 Bertini의 정리에 의해 $$D$$는 smooth이며, 다음 short exact sequence를 얻는다.

$$0 \to \mathcal{F} \otimes \mathcal{L}^{\otimes k-1} \xrightarrow{\cdot s} \mathcal{F} \otimes \mathcal{L}^{\otimes k} \to \mathcal{F} \otimes \mathcal{L}^{\otimes k}\vert_D \to 0$$

이 sequence의 cohomology long exact sequence는 다음을 준다.

$$\cdots \to H^i(\mathcal{F} \otimes \mathcal{L}^{\otimes k-1}) \to H^i(\mathcal{F} \otimes \mathcal{L}^{\otimes k}) \to H^i(\mathcal{F} \otimes \mathcal{L}^{\otimes k}\vert_D) \to H^{i+1}(\mathcal{F} \otimes \mathcal{L}^{\otimes k-1}) \to \cdots$$

$$\mathbb{P}^n$$의 특수 경우에는 $$\mathcal{L} = \mathcal{O}(1)$$이고, $$s$$는 일반적인 linear form이며, $$D$$는 $$\mathbb{P}^{n-1}$$과 isomorphic한 hyperplane $$H$$가 된다.

**1단계: $$\mathcal{F}\vert_D$$의 $$m$$-regularity.** $$\mathcal{F}$$가 $$\mathcal{L}$$에 대해 $$m$$-regular이므로 $$H^i(\mathcal{F} \otimes \mathcal{L}^{\otimes m-i}) = 0$$이 $$i > 0$$에 대해 성립한다. $$\mathcal{F}\vert_D$$가 $$\mathcal{L}\vert_D$$에 대해 $$m$$-regular임을 보이자. Restriction sequence에서 $$k = m - i$$를 대입하면 ($$0 < i \leq n-1$$)

$$0 \to \mathcal{F} \otimes \mathcal{L}^{\otimes m-i-1} \to \mathcal{F} \otimes \mathcal{L}^{\otimes m-i} \to \mathcal{F}\vert_D \otimes (\mathcal{L}\vert_D)^{\otimes m-i} \to 0$$

이고, 이의 long exact sequence에서

$$H^i(\mathcal{F} \otimes \mathcal{L}^{\otimes m-i}) \to H^i(\mathcal{F}\vert_D \otimes (\mathcal{L}\vert_D)^{\otimes m-i}) \to H^{i+1}(\mathcal{F} \otimes \mathcal{L}^{\otimes m-i-1})$$

이다. $$m$$-regularity에 의해 $$H^i(\mathcal{F} \otimes \mathcal{L}^{\otimes m-i}) = 0$$이고, $$H^{i+1}(\mathcal{F} \otimes \mathcal{L}^{\otimes m-i-1}) = 0$$ ($$i+1 > 0$$)이므로

$$H^i(\mathcal{F}\vert_D \otimes (\mathcal{L}\vert_D)^{\otimes m-i}) = 0$$

을 $$0 < i \leq n-1$$에 대해 얻는다. 이것은 $$\mathcal{F}\vert_D$$가 $$\mathcal{L}\vert_D$$에 대해 $$m$$-regular임을 의미한다.

**2단계: $$\mathcal{F} \otimes \mathcal{L}^{\otimes m}$$이 globally generated.** 귀납적 가정을 $$D$$에 적용한다. $$D$$는 projective variety이고 $$\dim D < \dim X$$이며, $$\mathcal{L}\vert_D$$는 ample line bundle이다. $$\mathcal{F}\vert_D$$가 $$m$$-regular이므로 귀납적 가정에 의해 $$\mathcal{F}\vert_D \otimes (\mathcal{L}\vert_D)^{\otimes m}$$은 $$D$$ 위에서 globally generated이다.

이제 $$\mathcal{F} \otimes \mathcal{L}^{\otimes m}$$이 globally generated임을 보이자. 임의의 점 $$p \in X$$에서 fiber $$(\mathcal{F} \otimes \mathcal{L}^{\otimes m})_p$$가 global section들의 상으로 생성됨을 확인하면 충분하다. $$p$$를 지나는 일반적인 divisor $$D$$를 택하고, restriction sequence에서 $$k = m$$을 대입하면

$$0 \to \mathcal{F} \otimes \mathcal{L}^{\otimes m-1} \to \mathcal{F} \otimes \mathcal{L}^{\otimes m} \to \mathcal{F}\vert_D \otimes (\mathcal{L}\vert_D)^{\otimes m} \to 0$$

이다. $$m$$-regularity에서 $$i = 1$$인 경우에 $$H^1(\mathcal{F} \otimes \mathcal{L}^{\otimes m-1}) = 0$$이므로

$$H^0(\mathcal{F} \otimes \mathcal{L}^{\otimes m}) \to H^0(\mathcal{F}\vert_D \otimes (\mathcal{L}\vert_D)^{\otimes m})$$

는 surjective이다. 귀납적 가정에 의해 $$\mathcal{F}\vert_D \otimes (\mathcal{L}\vert_D)^{\otimes m}$$은 $$D$$ 위에서 globally generated이므로, 이 fiber at $$p$$는 $$H^0(\mathcal{F}\vert_D \otimes (\mathcal{L}\vert_D)^{\otimes m})$$의 상으로 생성된다. Restriction map이 surjective이므로 $$\mathcal{F} \otimes \mathcal{L}^{\otimes m}$$의 global section들도 $$p$$에서의 fiber를 생성한다. 따라서 $$\mathcal{F} \otimes \mathcal{L}^{\otimes m}$$은 globally generated이다.

**3단계: $$\mathcal{F} \otimes \mathcal{L}^{\otimes p}$$가 $$(m+p)$$-regular.** $$\mathcal{F} \otimes \mathcal{L}^{\otimes m}$$이 globally generated이므로, 적당한 $$r_0$$에 대하여 다음의 surjection이 존재한다.

$$\mathcal{O}_X^{\oplus r_0} \twoheadrightarrow \mathcal{F} \otimes \mathcal{L}^{\otimes m}$$

이것에 $$\mathcal{L}^{\otimes p}$$를 tensor하면

$$\mathcal{L}^{\oplus r_0} \twoheadrightarrow \mathcal{F} \otimes \mathcal{L}^{\otimes m+p}$$

을 얻는다. 따라서 임의의 $$i > 0$$과 $$p \geq 0$$에 대해 $$H^i(X, \mathcal{L}^{\otimes p}) = 0$$이면 $$H^i(\mathcal{F} \otimes \mathcal{L}^{\otimes m+p}) = 0$$이 성립한다. $$p = 0$$인 경우 $$H^i(\mathcal{F} \otimes \mathcal{L}^{\otimes m}) = 0$$ ($$i > 0$$)은 $$\mathcal{F}$$의 $$m$$-regularity 정의 자체에 해당한다. $$p \geq 1$$인 경우, $$\mathcal{L}$$이 ample이므로 [명제 4](#prop4)에 의해 충분히 큰 $$p$$에 대해 $$H^i(\mathcal{L}^{\otimes p}) = 0$$이지만, $$p$$가 작은 경우에는 이 인자가 vanish하지 않을 수 있다.

이 문제를 해결하기 위해 $$p$$에 대한 귀납법을 사용한다. $$p = 0$$일 때 $$\mathcal{F}(m)$$이 $$m$$-regular인 것은 정의이다. $$p \geq 1$$이라 가정하고, $$\mathcal{F}(m+p)$$가 $$(m+p)$$-regular임, 즉 $$H^i(\mathcal{F} \otimes \mathcal{L}^{\otimes m+p-i}) = 0$$ ($$i > 0$$)을 보이자. $$i = 1$$인 경우, restriction sequence에서 $$k = m + p - 1$$을 대입하면

$$H^0(\mathcal{F}\vert_D \otimes (\mathcal{L}\vert_D)^{\otimes m+p-1}) \to H^1(\mathcal{F} \otimes \mathcal{L}^{\otimes m+p-2}) \to H^1(\mathcal{F} \otimes \mathcal{L}^{\otimes m+p-1})$$

이다. 귀납적 가정 ($$p-1$$에 대한)에 의해 $$H^1(\mathcal{F} \otimes \mathcal{L}^{\otimes m+p-2}) = 0$$이다. 또한, $$\mathcal{F}\vert_D$$가 $$m$$-regular이므로 (2단계) 차원에 대한 귀납적 가정에 의해 $$\mathcal{F}\vert_D \otimes (\mathcal{L}\vert_D)^{\otimes p}$$이 $$(m+p)$$-regular이고, 따라서 $$H^1(\mathcal{F}\vert_D \otimes (\mathcal{L}\vert_D)^{\otimes m+p-1}) = 0$$이다. 정확한 열에서 $$H^1(\mathcal{F} \otimes \mathcal{L}^{\otimes m+p-1})$$은 $$H^1(\mathcal{F}\vert_D \otimes (\mathcal{L}\vert_D)^{\otimes m+p-1})$$에 매장되므로 $$H^1(\mathcal{F} \otimes \mathcal{L}^{\otimes m+p-1}) = 0$$을 얻는다. $$i \geq 2$$인 경우, 같은 restriction sequence에서

$$H^{i-1}(\mathcal{F}\vert_D \otimes (\mathcal{L}\vert_D)^{\otimes m+p-i}) \to H^i(\mathcal{F} \otimes \mathcal{L}^{\otimes m+p-i-1}) \to H^i(\mathcal{F} \otimes \mathcal{L}^{\otimes m+p-i}) \to H^i(\mathcal{F}\vert_D \otimes (\mathcal{L}\vert_D)^{\otimes m+p-i})$$

이다. 귀납적 가정에 의해 $$H^i(\mathcal{F} \otimes \mathcal{L}^{\otimes m+p-i-1}) = 0$$ ($$p' = p-1$$, $$j = i$$에 대한 가정)이고, $$\mathcal{F}\vert_D$$에 대한 귀납적 가정 (차원에 대한 귀납)에 의해 $$H^{i-1}(\mathcal{F}\vert_D \otimes (\mathcal{L}\vert_D)^{\otimes m+p-i}) = 0$$과 $$H^i(\mathcal{F}\vert_D \otimes (\mathcal{L}\vert_D)^{\otimes m+p-i}) = 0$$이 $$i-1 \geq 1$$, $$i \leq n-1$$에 대해 성립한다. 따라서 $$H^i(\mathcal{F} \otimes \mathcal{L}^{\otimes m+p-i}) = 0$$을 얻는다.

</details>

<div class="example" markdown="1">

<ins id="ex8">**예시 8**</ins> $$\mathbb{P}^n$$ 위의 line bundle $$\mathcal{O}(d)$$의 regularity를 계산해보자. 여기서 $$\mathcal{L} = \mathcal{O}(1)$$이므로 twist는 $$\mathcal{O}(d) \otimes \mathcal{O}(m) = \mathcal{O}(d+m)$$이다. $$m$$-regularity 조건은 $$H^i(\mathbb{P}^n, \mathcal{O}(d+m-i)) = 0$$ ($$i > 0$$)이다. $$d \geq 0$$이고 $$m = 0$$을 택하면 $$H^i(\mathcal{O}(d-i))$$를 확인해야 하는데, $$i = 1$$일 때 $$H^1(\mathcal{O}(d-1))$$은 $$d \geq 1$$이면 $$0$$이고 $$d = 0$$이면 $$H^1(\mathcal{O}(-1)) = 0$$ (Bott's formula에서 $$-1 \geq -n$$이므로 모든 cohomology가 $$0$$)이다. 일반적으로 $$d \geq 0$$이고 $$i > 0$$일 때 $$d - i \geq -n$$이면 $$H^i(\mathcal{O}(d-i)) = 0$$이고, $$d - i < -n$$, 즉 $$i > d + n$$인 경우에는 $$i > n$$이 되어 어차피 $$H^i = 0$$이다. 따라서 $$\mathcal{O}(d)$$는 $$\mathcal{L} = \mathcal{O}(1)$$에 대해 $$0$$-regular이다. 반면 $$d < 0$$인 경우, $$\mathcal{O}(d)$$는 $$(-d)$$-regular이다. [명제 7](#prop7)에 의해 $$\mathcal{O}(d) \otimes \mathcal{L}^{\otimes 0} = \mathcal{O}(d)$$는 $$d \geq 0$$일 때 globally generated이며, 이는 ([§선다발과 벡터다발, ⁋예시 16](/ko/math/algebraic_varieties/line_bundles#ex16))에서 확인한 바와 일치한다.

</div>

## Very ample과 ample의 성질

위의 [명제 4](#prop4)와 [명제 7](#prop7)은 ample line bundle의 성질에 대한 대표적인 결과이다. 우리는 이 글을 ample line bundle과 very ample line bundle에 대한 추가적인 성질을 살펴보며 마무리한다. 

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> $$\mathcal{L}$$이 very ample이고 $$\mathcal{M}$$이 globally generated이면, $$\mathcal{L} \otimes \mathcal{M}$$은 very ample이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$\mathcal{L}$$이 very ample이므로, projective embedding $$i: X \hookrightarrow \mathbb{P}^N$$이 존재하여 $$\mathcal{L} = i^*\mathcal{O}_{\mathbb{P}^N}(1)$$이도록 할 수 있다. 한편, $$\mathcal{M}$$이 globally generated이므로, global section들 $$s_0, \ldots, s_n \in H^0(X, \mathcal{M})$$가 모든 점에서 stalk를 generate하며, 이로부터 morphism $$\phi: X \to \mathbb{P}^n$$를 정의할 수 있다.

이제 closed embedding $$(i, \phi): X \to \mathbb{P}^N \times \mathbb{P}^n$$을 생각하자. 그럼 여기에 Segre embedding ([§사영다양체, ⁋예시 16](/ko/math/algebraic_varieties/projective_varieties#ex16)) 

$$\sigma: \mathbb{P}^N \times \mathbb{P}^n \hookrightarrow \mathbb{P}^{Nn+N+n}$$

을 합성하면 $$\sigma^*\mathcal{O}(1) = \pi_1^*\mathcal{O}(1) \otimes \pi_2^*\mathcal{O}(1)$$이므로,

$$(\sigma \circ (i, \phi))^*\mathcal{O}(1) = i^*\mathcal{O}(1) \otimes \phi^*\mathcal{O}(1) = \mathcal{L} \otimes \mathcal{M}$$

인 것을 안다. 즉 $$\mathcal{L} \otimes \mathcal{M}$$은 very ample이다.

</details>

즉, 다소 복잡하게 설명하기는 했으나 핵심은 globally generated line bundle $$\mathcal{M}$$이 정의하는 morphism $$\phi:X\rightarrow \mathbb{P}^n$$은 closed embedding이 아닐 수 있으나, 이를 $$\mathcal{L}$$과 텐서하여 $$(i,\phi)$$ 형태로 projective space에 넣어주면 첫 번째 성분인 $$i$$가 이 map을 closed embedding으로 만들어준다는 것이다. 그럼 이로부터 다음의 유용한 결과 또한 증명할 수 있다. 

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10**</ins> Projective variety $$X$$ 위에 정의된 ample line bundle $$\mathcal{L}$$과 임의의 line bundle $$\mathcal{M}$$에 대하여, 충분히 큰 $$n$$에 대해 $$\mathcal{M} \otimes \mathcal{L}^{\otimes n}$$은 very ample이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

우선 $$\mathcal{L}$$이 ample이므로 적당한 $$m>0$$에 대해 $$\mathcal{L}^{\otimes m}$$이 very ample이다. 한편, [명제 4](#prop4)에 의해 우리는 충분히 큰 $$k$$에 대해서는 $$\mathcal{M}\otimes \mathcal{L}^{\otimes k}$$의 higher cohomology가 사라지도록 할 수 있으므로, 이러한 $$k$$에 대해서 $$\mathcal{M}\otimes \mathcal{L}^{\otimes k}$$는 globally generated이다. 이제 [명제 9](#prop9)에 의해 

$$(\mathcal{M} \otimes \mathcal{L}^{\otimes k}) \otimes \mathcal{L}^{\otimes m} = \mathcal{M} \otimes \mathcal{L}^{\otimes (k+m)}$$

은 very ample이고, 이로부터 $$n = k + m$$으로 두면 증명이 완료된다.

</details>

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[Bot]** R. Bott, *Homogeneous vector bundles*, Annals of Mathematics, 1957.  
**[Laz]** R. Lazarsfeld, *Positivity in Algebraic Geometry I*, Ergebnisse der Mathematik, Springer, 2004.  
**[Mum]** D. Mumford, *Lectures on Curves on an Algebraic Surface*, Annals of Mathematics Studies, Princeton, 1966.