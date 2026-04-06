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

date: 2026-03-15
last_modified_at: 2026-03-15
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

이다. 우선 $$\check{C}^0$$에서의 cohomology를 계산하기 위해 $$\ker\delta$$를 분석하자. 정의에 의해 cochain $$(f_0, f_1) \in \check{C}^0$$이 $$\ker \delta$$에 속한다는 것은 $$f_0 = f_1$$이 $$\mathcal{O}(d)(U_0 \cap U_1)$$에서 성립한다는 뜻이다. 우선 $$U_0$$ 부분을 보면, 임의의 monomial이 $$\mathcal{O}(d)(U_0)$$에 속하기 위해서는 반드시 적당한 $$a\geq 0$$에 대하여 $$\x_0^{d-a}\x_1^a$$ 꼴임을 안다. 비슷하게 어떠한 monomial이 $$\mathcal{O}(d)(U_1)$$에 속하기 위해서는 적당한 $$b\geq 0$$에 대하여 $$\x_0^b\x_1^{d-b}$$의 꼴이어야 한다. 이제 특정 cocycle $$(f_0,f_1)$$이 $$\ker\delta$$에 속하기 위해서는 $$f_0=f_1$$이어야 하고, 따라서 $$a+b=d$$를 만족하는 monomial들만이 $$\ker\delta$$에 속할 수 있다. 즉, 다음의 monomial들

$$\x_0^d, \quad\x_0^{d-1}\x_1,\quad\ldots, \quad\x_0\x_1^{d-1},\quad \x_1^d$$

이 $$H^0$$의 basis이고 이것이 원하는 결과를 준다. 만일 $$d<0$$이라면 $$a,b\geq 0$$은 이 식을 만족시키지 못하므로 $$H^0$$은 $$0$$이 된다. 

이제 $$H^1$$을 계산하자. 즉 $$\coker\delta$$를 계산해야 한다. 위의 계산으로부터, $$\delta$$의 image는 적당한 상수 $$a_i,b_j$$들에 대하여

$$f_1-f_0=\sum_{i\geq 0}a_i \x_0^{d-i}\x_1^i-\sum_{j\geq 0}b_j\x_0^j\x_1^{d-j}$$

임을 안다. 만일 $$d\geq 0$$이라면 이를 사용하여 임의의 $$\mathcal{O}(d)(U_0\cap U_1)$$의 원소들의 계수를 맞춰줄 수 있으므로 $$\coker\delta=0$$이다. 만일 $$d\leq -1$$이라면, 

$$H^1 = \coker \delta$$: $$\im \delta = f_1 - f_0$$에서 $$f_0 = \sum_{i \geq 0} c_i \x_0^{d-i}\x_1^i$$, $$f_1 = \sum_{j \geq 0} d_j \x_0^j \x_1^{d-j}$$이다. $$d \geq 0$$이면 임의의 monomial $$\x_0^a \x_1^{d-a}$$에 대해 $$a \geq 0$$이면 $$f_0$$에서, $$a \leq 0$$이면 $$f_1$$에서 얻을 수 있으므로 모든 monomial이 $$\im \delta$$에 속하고 $$\coker \delta = 0$$이다. $$d \leq -1$$이면 $$\im \delta$$에 속하는 monomial은 적어도 하나의 지수가 $$\geq 0$$이고, cokernel은 두 지수 모두 음수인 monomial $$\x_0^a \x_1^{d-a}$$ ($$a = d+1, \ldots, -1$$)로 생성되어 $$\dim H^1 = -d-1$$이다. 이는 $$\mathbb{K}[\x_0^{-1}, \x_1^{-1}]_{-d-2}$$의 차원과 일치한다.

이제 $$n \geq 2$$에 대해 이중 귀납법으로 일반적인 경우를 증명한다. 외부 귀납은 $$n$$에 대한 것으로, $$\mathbb{P}^{n-1}$$ 위에서 공식이 성립한다고 가정한다. $$\mathbb{P}^n$$의 초평면 $$H = \{\x_n = 0\} \cong \mathbb{P}^{n-1}$$에 대해 다음 짧은 완전열을 얻는다:

$$0 \to \mathcal{O}_{\mathbb{P}^n}(d-1) \xrightarrow{\cdot \x_n} \mathcal{O}_{\mathbb{P}^n}(d) \to \mathcal{O}_H(d) \to 0$$

이 완전열의 cohomology long exact sequence를 $$\mathbb{P}^n$$ 위에서의 각 $$d$$에 대해 적용한다.

**1단계: 중간 차수 cohomology의 소거.** $$0 < q < n$$에 대해 long exact sequence의

$$H^{q-1}(\mathbb{P}^{n-1}, \mathcal{O}(d)) \to H^q(\mathcal{O}(d-1)) \to H^q(\mathcal{O}(d)) \to H^q(\mathbb{P}^{n-1}, \mathcal{O}(d))$$

에서 외부 귀납적 가정에 의해 $$H^q(\mathbb{P}^{n-1}, \mathcal{O}(d)) = 0$$이고 마찬가지로 $$H^{q-1}(\mathbb{P}^{n-1}, \mathcal{O}(d)) = 0$$이다. 이는 $$q \leq n-1$$이므로 $$H^q, H^{q-1}$$ 모두 $$\mathbb{P}^{n-1}$$ 위에서 중간 차수 cohomology (각각 $$0 < q \leq n-1$$과 $$0 \leq q-1 \leq n-2$$)이거나 top cohomology이지만, $$\mathbb{P}^{n-1}$$에서 $$H^{n-1}$$가 non-zero인 것은 $$d \leq -n$$일 때뿐이고, $$H^{q-1}$$는 $$q-1 \leq n-2 < n-1$$이므로 항상 $$0$$이다. 또한 $$q = n-1$$일 때 $$H^q = H^{n-1}$$이 $$d \leq -n$$에서 non-zero일 수 있지만, 이 경우 $$H^{q-1} = H^{n-2} = 0$$이므로 $$H^{n-1}(\mathcal{O}(d-1)) \hookrightarrow H^{n-1}(\mathcal{O}(d))$$라는 단사만 얻고, $$d \geq 0$$에서 $$H^{n-1} = 0$$임을 알고 있으므로 내림차순 귀납에 의해 $$H^{n-1}(\mathcal{O}(d)) = 0$$을 모든 $$d$$에 대해 얻는다. $$q \leq n-2$$인 경우에는 동형사 $$H^q(\mathcal{O}(d-1)) \cong H^q(\mathcal{O}(d))$$이 성립하므로 $$H^q(\mathbb{P}^n, \mathcal{O}(d)) = 0$$을 얻는다.

**2단계: $$H^0$$의 계산.** Long exact sequence의 $$H^0$$ 부분

$$0 \to H^0(\mathcal{O}(d-1)) \to H^0(\mathcal{O}(d)) \to H^0(\mathbb{P}^{n-1}, \mathcal{O}(d)) \to H^1(\mathcal{O}(d-1))$$

에서 1단계에 의해 $$H^1(\mathcal{O}(d-1)) = 0$$ ($$n \geq 2$$이므로 $$0 < 1 < n$$)이고, 따라서

$$0 \to H^0(\mathcal{O}(d-1)) \to H^0(\mathcal{O}(d)) \to H^0(\mathbb{P}^{n-1}, \mathcal{O}(d)) \to 0$$

이 완전열이 된다. $$d \geq 0$$에 대해 $$d$$에 대한 오름차순 귀납법으로 $$H^0(\mathbb{P}^n, \mathcal{O}(d)) \cong \mathbb{K}[\x_0, \ldots, \x_n]_d$$임을 보인다. $$d = 0$$이면 $$H^0(\mathcal{O}(0)) = \mathbb{K}$$이고 외부 귀납적 가정으로 $$H^0(\mathbb{P}^{n-1}, \mathcal{O}(0)) \cong \mathbb{K}$$이므로, 위 완전열에서 $$H^0(\mathcal{O}(-1)) = 0$$을 얻는다. $$d \geq 1$$에 대해 귀납적 가정 $$H^0(\mathcal{O}(d-1)) \cong \mathbb{K}[\x_0, \ldots, \x_n]_{d-1}$$를 사용하면, 외부 귀납적 가정 $$H^0(\mathbb{P}^{n-1}, \mathcal{O}(d)) \cong \mathbb{K}[\x_0, \ldots, \x_{n-1}]_d$$와 함께

$$H^0(\mathcal{O}(d)) \cong \mathbb{K}[\x_0, \ldots, \x_n]_{d-1} \oplus \mathbb{K}[\x_0, \ldots, \x_{n-1}]_d \cong \mathbb{K}[\x_0, \ldots, \x_n]_d$$

를 얻는다. $$d \leq -1$$에 대해서는 위 완전열에서 $$H^0(\mathcal{O}(d-1))$$이 $$H^0(\mathcal{O}(d))$$에 단사적으로 매장되고, 외부 귀납적 가정에 의해 $$H^0(\mathbb{P}^{n-1}, \mathcal{O}(d)) = 0$$ ($$d < 0$$)이므로 $$H^0(\mathcal{O}(d)) \cong H^0(\mathcal{O}(d-1))$$이다. $$H^0(\mathcal{O}(-1)) = 0$$이므로, 내림차순 귀납에 의해 $$H^0 = 0$$을 모든 $$d \leq -1$$에 대해 얻는다.

**3단계: $$H^n$$의 계산.** 1단계에 의해 $$H^{n-1}(\mathcal{O}(d)) = 0$$이므로 long exact sequence에서

$$0 \to H^{n-1}(\mathbb{P}^{n-1}, \mathcal{O}(d)) \to H^n(\mathcal{O}(d-1)) \to H^n(\mathcal{O}(d)) \to 0$$

을 얻는다. 외부 귀납적 가정에 의해 $$H^{n-1}(\mathbb{P}^{n-1}, \mathcal{O}(d))$$는 $$d \leq -n$$일 때만 non-zero이고, 이때 $$\dim H^{n-1}(\mathbb{P}^{n-1}, \mathcal{O}(d)) = \binom{-d-1}{n-1}$$이다. $$d \geq -n+1$$이면 $$H^{n-1}(\mathbb{P}^{n-1}, \mathcal{O}(d)) = 0$$이므로 $$H^n(\mathcal{O}(d-1)) \cong H^n(\mathcal{O}(d))$$이고, 따라서 $$H^n(\mathcal{O}(d))$$는 $$d \geq -n+1$$에서 상수이다. $$d \geq 0$$에 대해서는 Čech complex에서 $$H^n = 0$$임을 확인할 수 있으므로 (모든 지수가 음수인 monomial은 $$d \geq 0$$일 때 존재하지 않음), 내림차순 귀납에 의해 $$H^n(\mathcal{O}(d)) = 0$$을 모든 $$d \geq -n$$에 대해 얻는다.

$$d \leq -n-1$$에 대해서는 위 완전열에서

$$\dim H^n(\mathcal{O}(d-1)) = \dim H^n(\mathcal{O}(d)) + \binom{-d-1}{n-1}$$

이 성립한다. $$H^n(\mathcal{O}(-n)) = 0$$을 알고 있으므로, 내림차순 귀납에 의해

$$\dim H^n(\mathcal{O}(d)) = \sum_{k=d}^{-n-1} \binom{-k-1}{n-1} = \binom{-d-1}{n}$$

을 얻는다. 마지막 등식은 이항계수의 합 공식 $$\sum_{j=0}^{m} \binom{r+j}{j} = \binom{r+m+1}{m}$$에 의해 성립한다. 실제로 $$H^n$$의 원소는 monomial로 직접 계산할 수도 있다. $$\mathbb{P}^n$$의 standard affine cover $$\mathcal{U} = \{U_0, \ldots, U_n\}$$에 대한 Čech 복합체에서 $$n$$-cochain은 항 $$f_{0 1 \cdots n} \in \mathcal{O}(d)(U_{0 1 \cdots n})$$이며, 이는 $$\mathbb{K}[\x_0^{\pm 1}, \ldots, \x_n^{\pm 1}]_d$$의 원소이다. 이 항은 coboundary map의 source가 아니므로 $$(n-1)$$-cochain의 coboundary에 속하지 않는 monomial들이 $$H^n$$을 이룬다. $$(n-1)$$-cochain $$g_{i_0 \cdots i_{n-1}}$$은 적어도 하나의 index가 빠져 있으므로, 그 coboundary image에 속하는 monomial은 적어도 하나의 지수가 $$\geq 0$$이다. 따라서 $$H^n$$은 모든 $$a_i \leq -1$$이고 $$\sum a_i = d$$인 monomial $$\x_0^{a_0} \cdots \x_n^{a_n}$$들로 생성된다. 치환 $$b_i = -a_i - 1$$을 적용하면 $$b_i \geq 0$$이고 $$\sum b_i = -d - n - 1$$이 되어, $$H^n(\mathbb{P}^n, \mathcal{O}(d)) \cong \mathbb{K}[\x_0^{-1}, \ldots, \x_n^{-1}]_{-d-n-1}$$을 얻는다.

</details>

**참고.** 위 식에서 $$\mathbb{K}[\x_0^{-1}, \ldots, \x_n^{-1}]_{-d-n-1}$$은 degree $$-d-n-1$$의 "negative degree" monomial들의 공간이다. 구체적으로:

$$\mathbb{K}[\x_0^{-1}, \ldots, \x_n^{-1}]_k = \span\{\x_0^{a_0} \cdots \x_n^{a_n} : a_i \leq -1,\, \textstyle\sum a_i = -k - n - 1\}$$

이 정의는 명제 1의 증명에서 수행한 치환 $$b_i = -a_i - 1$$과 일치한다. 원소 $$\x_0^{a_0} \cdots \x_n^{a_n}$$은 $$a_i \leq -1$$이고 $$\sum a_i = d$$를 만족하는데, 치환 후 $$b_i \geq 0$$이고 $$\sum b_i = -d - n - 1$$이므로 첨자 $$k = -d - n - 1$$은 $$b_i$$들의 합을 나타낸다. 즉 $$\mathbb{K}[\x_0^{-1}, \ldots, \x_n^{-1}]_k \cong \mathbb{K}[\x_0, \ldots, \x_n]_k$$이다.

Bott's formula가 말하는 것을 직관적으로 요약하면 다음과 같다. 먼저 $$H^0$$는 global section의 공간이며, 이는 degree $$d$$의 homogeneous polynomial들이다. 한편 $$H^n$$은 top-degree cohomology로, 오직 $$d \leq -n-1$$일 때만 살아남는다. 이는 $$\mathcal{O}(d)$$가 충분히 negative한 twist일 때만 "top cohomology"에 기여하는 nontrivial class들이 존재한다는 것을 의미한다. 가장 주목할 만한 것은 중간 차수의 cohomology, 즉 $$0 < q < n$$에 대해서는 $$H^q$$가 항상 $$0$$이라는 사실이다. 이는 projective space의 line bundle이 매우 특별한 구조를 가지고 있음을 보여준다.

<div class="example" markdown="1">

<ins id="ex2">**예시 2 ($$\mathbb{P}^1$$)**</ins>

$$\mathbb{P}^1$$에 대해 Bott's formula는 $$H^0(\mathbb{P}^1, \mathcal{O}(d)) = \mathbb{K}[\x_0, \x_1]_d$$를 $$d \geq 0$$에 대해, $$H^1(\mathbb{P}^1, \mathcal{O}(d)) = 0$$를 $$d \geq -1$$에 대해, 그리고 $$H^1(\mathbb{P}^1, \mathcal{O}(d)) = \mathbb{K}[\x_0^{-1}, \x_1^{-1}]_{-d-2}$$를 $$d \leq -2$$에 대해 부여한다. 구체적으로 $$H^1(\mathbb{P}^1, \mathcal{O}(-3))$$은 basis $$\{\x_0^{-2}\x_1^{-1}, \x_0^{-1}\x_1^{-2}\}$$를 갖고 dimension 2이다.

이 결과는 기하학적으로 다음과 같이 이해할 수 있다. $$\mathcal{O}(d)$$의 global section들은 degree $$d$$의 homogeneous polynomial들로, $$d \geq 0$$일 때만 존재한다. 이는 $$d \geq 0$$일 때 $$\mathcal{O}(d)$$가 "충분히 긍정적"이어서 bundle의 section들이 zero section을 넘어설 수 있기 때문이다. 반면 $$d \leq -2$$일 때는 global section이 존재하지 않지만, 그 대신 higher cohomology에 nontrivial 정보가 담기게 된다. 이 정보는 Serre duality에 의해 정확하게 $$H^1(\mathbb{P}^1, \mathcal{O}(d)) \cong H^0(\mathbb{P}^1, \mathcal{O}(-d-2))^\vee$$의 관계를 만족한다.

</div>

## Euler Characteristic

Bott's formula는 각 cohomology group의 차원을 개별적으로 계산하지만, 이들을 합산하여 얻는 Euler characteristic<sub>오일러 지표</sub>는 더 간단한 공식으로 표현된다. Euler characteristic은 alternating sum

$$\chi(\mathbb{P}^n, \mathcal{F}) = \sum_{i=0}^{n} (-1)^i \dim H^i(\mathbb{P}^n, \mathcal{F})$$

으로 정의되며, 이는 short exact sequence에 대해 가산적(additive)이라는 중요한 성질을 갖는다. 즉, short exact sequence $$0 \to \mathcal{F} \to \mathcal{G} \to \mathcal{H} \to 0$$에 대해 $$\chi(\mathcal{G}) = \chi(\mathcal{F}) + \chi(\mathcal{H})$$가 성립한다. 따라서 Euler characteristic은 개별 cohomology group의 정보를 잃는 대신, 계산과 조작이 훨씬 용이한 불변량이 된다.

<div class="proposition" markdown="1">

<ins id="cor3">**따름정리 3**</ins> $$\mathbb{P}^n$$ 위의 $$\mathcal{O}(d)$$의 Euler characteristic:

$$\chi(\mathbb{P}^n, \mathcal{O}(d)) = \binom{n+d}{n}$$

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Bott's formula에 의해 cohomology는 세 가지 경우로 나뉜다. 첫째, $$d \geq 0$$인 경우 $$H^0$$만 non-zero이므로 $$\chi(\mathcal{O}(d)) = \dim H^0(\mathbb{P}^n, \mathcal{O}(d)) = \dim \mathbb{K}[\x_0, \ldots, \x_n]_d = \binom{n+d}{n}$$이다. 둘째, $$-n \leq d \leq -1$$인 경우 모든 cohomology가 사라지므로 $$\chi(\mathcal{O}(d)) = 0$$이고, 이항계수의 일반화에 의해 $$\binom{n+d}{n}$$ 역시 $$0 \leq d+n \leq n-1$$일 때 $$0$$이므로 일치한다. 셋째, $$d \leq -n-1$$인 경우 $$H^n$$만 non-zero이므로 $$\chi(\mathcal{O}(d)) = (-1)^n \dim \mathbb{K}[\x_0^{-1}, \ldots, \x_n^{-1}]_{-d-n-1}$$이다. 치환 $$a_i' = -a_i - 1$$을 적용하면 $$a_i \leq -1$$이므로 $$a_i' = -a_i - 1 \geq 0$$이 되고, $$\sum a_i' = \sum(-a_i - 1) = -\sum a_i - (n+1) = -d - (n+1)$$로 변환된다. 따라서 $$\dim \mathbb{K}[\x_0^{-1}, \ldots, \x_n^{-1}]_{-d-n-1}$$은 $$n+1$$개의 비음수 정수 $$(a_0', \ldots, a_n')$$ 중 합이 $$-d - n - 1$$인 것의 개수, 즉 $$\binom{-d-1}{n}$$이다. 결과적으로 $$\chi(\mathcal{O}(d)) = (-1)^n \binom{-d-1}{n}$$이다. 일반화된 이항계수의 항등식 $$(-1)^n\binom{-d-1}{n} = \binom{n+d}{n}$$에 의해 $$\chi(\mathcal{O}(d)) = \binom{n+d}{n}$$이 성립한다.

</details>

<div class="example" markdown="1">

<ins id="ex4">**예시 4**</ins> $$\mathbb{P}^2$$ 위의 $$\mathcal{O}(d)$$에 대해 $$\chi(\mathcal{O}(d)) = \frac{(d+1)(d+2)}{2}$$이며, 구체적으로 $$\chi(\mathcal{O}(0)) = 1$$, $$\chi(\mathcal{O}(1)) = 3$$, $$\chi(\mathcal{O}(2)) = 6$$이다. 이는 $$\mathbb{P}^2$$에서 degree $$d$$ 곡선이 갖는 기하학적 정보량을 수량화하는 하나의 측도로 이해할 수 있다. 예를 들어, $$\chi(\mathcal{O}(1)) = 3$$은 $$\mathbb{P}^2$$의 직선(line)이 세 개의 independent한 section을 가진다는 사실과 대응된다.

</div>

## Čech Cohomology를 통한 계산

Bott's formula의 증명에서 우리는 이미 standard affine cover를 사용하는 Čech cohomology가 sheaf cohomology와 일치한다는 사실을 사용하였다. 이 절에서는 이 사실을 명시적으로 기술하고, $$\mathbb{P}^1$$의 경우에 대해 Čech 복합체를 명시적으로 전개하여 Bott's formula의 계산을 보다 상세히 보여준다. 이는 앞선 명제 1의 증명에서 sketch한 계산을 보충하는 역할도 한다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> $$\mathbb{P}^n$$의 standard affine cover $$\mathcal{U} = \{U_0, \ldots, U_n\}$$을 사용하면:

$$H^q(\mathbb{P}^n, \mathcal{O}(d)) \cong \check{H}^q(\mathcal{U}, \mathcal{O}(d))$$

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

각 intersection $$U_{i_0 \cdots i_p} = U_{i_0} \cap \cdots \cap U_{i_p}$$는 affine이고, $$\mathcal{O}(d)$$는 quasi-coherent이므로 Leray's theorem ([§층 코호몰로지, ⁋명제 12](/ko/math/algebraic_geometry/sheaf_cohomology#prop12))에 의해 Čech cohomology가 sheaf cohomology와 일치한다.

</details>

<div class="example" markdown="1">

<ins id="ex6">**예시 6 ($$\mathbb{P}^1$$의 명시적 계산)**</ins>

명제 5에 의해 $$\mathbb{P}^1$$에서의 Čech cohomology가 sheaf cohomology와 일치하므로, 우리는 명시적으로 Čech 복합체를 전개하여 ([명제 1](#prop1))의 $$n = 1$$인 경우를 다시 한번 확인한다.

$$\mathcal{U} = \{U_0, U_1\}$$에 대해 Čech 복합체는 $$0 \to \check{C}^0 \xrightarrow{\delta} \check{C}^1 \to 0$$이며, 여기서

$$\mathcal{O}(d)(U_0) = \x_0^d \cdot \mathbb{K}[\x_1/\x_0], \qquad \mathcal{O}(d)(U_1) = \x_1^d \cdot \mathbb{K}[\x_0/\x_1], \qquad \mathcal{O}(d)(U_0 \cap U_1) = \mathbb{K}[\x_0^{\pm 1}, \x_1^{\pm 1}]_d$$

이다. Coboundary map $$\delta(f_0, f_1) = f_1 - f_0$$에서 일치 조건 $$f_0 = f_1$$을 monomial $$\x_0^a \x_1^b$$ 단위로 분석한다.

$$\ker \delta$$: $$f_0$$의 monomial은 $$\x_0^{d-a}\x_1^a$$ ($$a \geq 0$$), $$f_1$$의 monomial은 $$\x_0^b\x_1^{d-b}$$ ($$b \geq 0$$) 꼴이다. $$f_0 = f_1$$이면 $$a+b = d$$이므로 $$d \geq 0$$일 때 $$\dim H^0 = d+1$$, $$d \leq -1$$일 때 $$\ker \delta = 0$$이고 $$H^0 = 0$$이다.

$$H^1 = \coker \delta$$: $$\im \delta = f_1 - f_0$$에서 $$f_0 = \sum_{i \geq 0} c_i \x_0^{d-i}\x_1^i$$ ($$\x_1$$ 지수 $$\geq 0$$), $$f_1 = \sum_{j \geq 0} d_j \x_0^j \x_1^{d-j}$$ ($$\x_0$$ 지수 $$\geq 0$$)이다. $$d \geq 0$$이면 임의의 monomial $$\x_0^a \x_1^b$$ ($$a+b=d$$)이 $$\im \delta$$에 속하므로 $$\coker \delta = 0$$이다. $$d \leq -1$$이면 $$\im \delta$$에 속하는 monomial은 적어도 하나의 지수가 $$\geq 0$$이고, cokernel은 두 지수 모두 음수인 monomial $$\x_0^a \x_1^{d-a}$$ ($$a = d+1, \ldots, -1$$)로 생성되어 $$\dim H^1 = -d-1$$이다. 이는 $$\mathbb{K}[\x_0^{-1}, \x_1^{-1}]_{-d-2}$$의 차원과 일치한다.

</div>

## Regularity

지금까지 우리는 $$\mathcal{O}(d)$$라는 매우 특수한 sheaf의 cohomology를 계산하였다. 그러나 대수기하학에서 실제로 마주치는 sheaf는 임의의 coherent sheaf $$\mathcal{F}$$이며, 이의 cohomology를 모두 계산하는 것은 일반적으로 불가능하다. 다행히도 coherent sheaf의 cohomology를 다룰 때, “충분히 twist하면 high cohomology가 vanish한다”는 현상이 자주 나타난다. 이는 Serre vanishing theorem으로 정밀화된다: 임의의 coherent sheaf $$\mathcal{F}$$에 대해 충분히 큰 $$m$$에 대해 $$H^i(\mathbb{P}^n, \mathcal{F}(m)) = 0$$이 $$i > 0$$에 대해 성립한다. 예를 들어, Bott's formula에서 $$H^q(\mathbb{P}^n, \mathcal{O}(d))$$가 $$q > 0$$에서 vanish하는 $$d$$의 범위는 $$d \geq -n$$이다. Regularity는 이 현상을 정량화하여, 구체적으로 어느 정도 twist해야 higher cohomology가 사라지는지를 기록하는 개념이다.

Coherent sheaf를 다룰 때 한 가지 근본적인 어려움은, line bundle의 경우와 달리 global section이 항상 존재한다는 보장이 없다는 점이다. 예를 들어 $$\mathcal{O}(d)$$는 $$d \geq 0$$일 때만 non-zero global section을 갖지만, 일반적인 coherent sheaf $$\mathcal{F}$$에 대해서는 $$H^0(X, \mathcal{F})$$의 차원을 섣불리 예측할 수 없다. 그럼에도 불구하고, 충분히 많은 global section이 존재하여 각 점의 stalk를 모두 생성할 수 있다면, line bundle에서 하던 것처럼 evaluation map을 통해 projective embedding이나 morphism의 구성 등 다양한 기하학적 작업을 수행할 수 있다. 이러한 상황은 선형계(linear system)가 basepoint-free일 때와 정확히 유사하다. Basepoint-free linear system이 점마다 그 점에서 vanish하지 않는 section을 제공하듯이, globally generated sheaf는 stalk의 각 원소를 global section들의 값으로 생성할 수 있다.

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> Coherent sheaf $$\mathcal{F}$$가 *globally generated*라는 것은 evaluation map

$$H^0(X, \mathcal{F}) \otimes \mathcal{O}_X \to \mathcal{F}$$

가 surjective인 것이다. 즉, global section들로 stalk를 모두 생성할 수 있다.

</div>

<div class="definition" markdown="1">

<ins id="def8">**정의 8**</ins> Coherent sheaf $$\mathcal{F}$$ on $$\mathbb{P}^n$$이 *$$m$$-regular*라는 것은 $$i > 0$$에 대해 $$H^i(\mathbb{P}^n, \mathcal{F}(m-i)) = 0$$인 것이다.

</div>

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9 (Castelnuovo-Mumford Regularity)**</ins> $$\mathcal{F}$$가 $$m$$-regular이면 $$\mathcal{F}(m)$$은 globally generated이고, $$i > 0$$이고 $$k \geq m - i$$인 모든 $$i, k$$에 대해 $$H^i(\mathbb{P}^n, \mathcal{F}(k)) = 0$$이다.

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

<ins id="ex10">**예시 10**</ins> Line bundle $$\mathcal{O}(d)$$의 regularity를 계산해보자. $$d \geq 0$$이면 Bott's formula에 의해 $$H^i(\mathbb{P}^n, \mathcal{O}(d)) = 0$$이 $$i > 0$$에 대해 성립한다. 그런데 $$\mathcal{O}(d)$$의 $$m$$-regularity 조건은 $$H^i(\mathcal{O}(d+m-i)) = 0$$ ($$i > 0$$)이다. $$m = 0$$을 택하면 $$H^i(\mathcal{O}(d-i))$$를 확인해야 하는데, $$i = 1$$일 때 $$H^1(\mathcal{O}(d-1))$$은 $$d \geq 1$$이면 $$0$$이지만 $$d = 0$$이면 $$H^1(\mathcal{O}(-1)) = 0$$ (Bott's formula에서 $$-1$$은 $$-1 \geq -n$$이므로 모든 cohomology가 $$0$$)이다. 일반적으로 $$d \geq 0$$이고 $$i > 0$$일 때 $$d - i \geq -n$$이면 $$H^i(\mathcal{O}(d-i)) = 0$$이다. 문제는 $$d - i < -n$$, 즉 $$i > d + n$$인 경우인데, 이때 $$i > n$$이 되어 어차피 $$H^i = 0$$이다. 따라서 $$\mathcal{O}(d)$$는 $$0$$-regular이다. 명제 9에 의해 $$\mathcal{O}(d)$$는 $$d \geq 0$$일 때 globally generated이며, 이는 ([§선다발과 벡터다발, ⁋예시 16](/ko/math/algebraic_geometry/line_bundles#ex16))에서 확인한 바와 일치한다.

</div>

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.
**[Bot]** R. Bott, *Homogeneous vector bundles*, Annals of Mathematics, 1957.
**[Mum]** D. Mumford, *Lectures on Curves on an Algebraic Surface*, Annals of Mathematics Studies, Princeton, 1966.
                                                                                                                                                                                                                                                                                                                                                                                                                             