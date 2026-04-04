---
title: "Cohomology of Line Bundles on projective spaces"
excerpt: "Bott's formula and the cohomology of line bundles on projective space"

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/cohomology_of_line_bundles
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

## 도입

우리는 앞선 글에서 line bundle $$\mathcal{O}(d)$$를 정의하고, 그 global section $$H^0(\mathbb{P}^n, \mathcal{O}(d))$$이 degree $$d$$의 homogeneous polynomial들과 동형임을 확인하였다. ([§Line Bundles, ⁋예시 16](/ko/math/algebraic_geometry/line_bundles#ex16)) 그러나 sheaf cohomology ([§Sheaf Cohomology, ⁋정의 1](/ko/math/algebraic_geometry/sheaf_cohomology#def1))는 $$H^0$$뿐만 아니라 higher cohomology group들 $$H^1, H^2, \ldots$$까지 포함하는 더 풍부한 불변량이며, 이들이 모두 합쳐져야만 line bundle의 완전한 기하학적 정보를 담을 수 있다.

이 글에서 우리의 목표는 projective space $$\mathbb{P}^n$$ 위의 line bundle $$\mathcal{O}(d)$$ ([§Line Bundles, ⁋예시 12](/ko/math/algebraic_geometry/line_bundles#ex12))의 cohomology group $$H^q(\mathbb{P}^n, \mathcal{O}(d))$$를 모든 $$q$$와 $$d$$에 대해 완전히 계산하는 것이다. 이 계산은 Bott's formula로 알려져 있으며, 그 결과는 놀랍도록 간단하다: $$H^0$$와 $$H^n$$에서만 non-zero이고, 나머지 모든 cohomology group은 사라진다. 이 계산은 대수기하학의 기본적인 도구이며, Serre duality, Riemann-Roch theorem 등의 응용에서 필수적이다.

## Bott's Formula

Bott's formula를 증명하기 위해 우리는 Čech cohomology를 사용한다. 이는 Leray's theorem ([§Čech Cohomology, ⁋명제 10](/ko/math/algebraic_geometry/cech_cohomology#prop10))에 의해, standard affine cover를 사용하면 Čech cohomology가 sheaf cohomology와 일치하기 때문이다. 따라서 우리의 전략은 각각의 affine open set들과 그 교집합 위에서 $$\mathcal{O}(d)$$의 section들을 명시적으로 기술하고, coboundary map을 직접 계산하는 것이다.

<div class="proposition" markdown="1">

<ins id="prop1">**명제 1 (Bott's Formula)**</ins> $$\mathbb{P}^n$$ 위의 line bundle $$\mathcal{O}(d)$$의 cohomology는 다음과 같다:

$$H^q(\mathbb{P}^n, \mathcal{O}(d)) = \begin{cases}
\mathbb{K}[x_0, \ldots, x_n]_d & q = 0, d \geq 0 \\
\mathbb{K}[x_0^{-1}, \ldots, x_n^{-1}]_{-d-n-1} & q = n, d \leq -n-1 \\
0 & \text{otherwise}
\end{cases}$$

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Standard affine cover $$\mathfrak{U} = \{U_0, \ldots, U_n\}$$, $$U_i = \{x_i \neq 0\}$$를 사용한다. 각 intersection $$U_{i_0 \cdots i_p}$$은 affine이고 $$\mathcal{O}(d)$$는 quasi-coherent이므로, Leray's theorem ([§Čech Cohomology, ⁋명제 10](/ko/math/algebraic_geometry/cech_cohomology#prop10))에 의해 $$H^q(\mathbb{P}^n, \mathcal{O}(d)) \cong \check{H}^q(\mathfrak{U}, \mathcal{O}(d))$$이다.

$$\mathcal{O}(d)(U_i)$$는 $$x_i^{-d}\mathbb{K}[x_0/x_i, \ldots, \hat{x_i}/x_i, \ldots, x_n/x_i]$$이므로, Čech cochain $$f \in C^p(\mathfrak{U}, \mathcal{O}(d))$$는 각 $$p+1$$-tuple $$(i_0, \ldots, i_p)$$에 대해 $$U_{i_0 \cdots i_p}$$ 위에서 regular한 섹션을 대응시키는 것이다. 교집합 $$U_{i_0 \cdots i_p}$$에서는 $$x_{i_0}, \ldots, x_{i_p}$$가 모두 non-zero이므로, 이 위에서의 섹션은 Laurent polynomial $$f_{i_0 \cdots i_p} = x_0^{a_0} \cdots x_n^{a_n}$$ (여기서 $$\sum a_j = d$$이고, $$j \notin \{i_0, \ldots, i_p\}$$인 $$a_j$$에 대해서는 $$a_j \geq 0$$이어야 한다)들로 생성된다.

Coboundary map $$\delta : C^p \to C^{p+1}$$은 $$(\delta f)_{i_0 \cdots i_{p+1}} = \sum_{k=0}^{p+1} (-1)^k f_{i_0 \cdots \hat{i_k} \cdots i_{p+1}}$$로 주어진다. 각 $$(p+1)$$-tuple에서 하나의 index를 생략한 $$p$$-tuple에 대응하는 섹션들을 교대로 합하는 것이다. 최종적으로 $$H^p = \ker \delta / \operatorname{im} \delta$$를 계산해야 한다.

**$$\mathbb{P}^1$$의 경우.** $$n = 1$$일 때 Čech 복합체는 $$0 \to C^0 \xrightarrow{\delta} C^1 \to 0$$이다. 여기서 $$C^0 = \mathcal{O}(d)(U_0) \oplus \mathcal{O}(d)(U_1)$$이고 $$C^1 = \mathcal{O}(d)(U_0 \cap U_1)$$이다. $$U_0$$에서 coordinate $$t = x_1/x_0$$, $$U_1$$에서 $$s = x_0/x_1 = t^{-1}$$를 사용하면:

$$\mathcal{O}(d)(U_0) = \mathbb{K}[t] \cdot 1, \quad \mathcal{O}(d)(U_1) = \mathbb{K}[s] \cdot s^{-d} = \mathbb{K}[s] \cdot t^d, \quad \mathcal{O}(d)(U_0 \cap U_1) = \mathbb{K}[t, t^{-1}] \cdot 1$$

Coboundary map $$\delta(f_0, f_1) = f_1 - f_0$$에서 $$f_0 \in \mathbb{K}[t]$$, $$f_1 \in t^d \mathbb{K}[t^{-1}]$$이다.

- $$d \geq 0$$: $$H^0 = \ker \delta = \{f_0 = f_1\} = \mathbb{K}[t] \cap t^d\mathbb{K}[t^{-1}] = \mathbb{K}[x_0, x_1]_d$$이며 차원은 $$d+1$$이다. $$H^1 = 0$$.
- $$d \leq -1$$: $$H^0 = \ker \delta = 0$$이고, $$H^1 = \operatorname{coker} \delta$$. $$\operatorname{im} \delta$$의 complement는 degree $$-d-1$$ 이상의 negative monomial $$\{t^{-1}, t^{-2}, \ldots, t^{-d-1}\}$$이므로, $$H^1$$의 차원은 $$-d-1$$이다. 이는 $$\mathbb{K}[x_0^{-1}, x_1^{-1}]_{-d-2}$$의 차원과 일치한다.

**일반 $$\mathbb{P}^n$$에 대한 귀납법.** 이제 $$n$$에 대한 귀납법으로 일반적인 경우를 증명한다. $$n = 1$$인 경우는 위에서 증명하였으므로, $$n \geq 2$$라 하자. $$\mathbb{P}^n$$을 hyperplane $$H = \mathbb{P}^{n-1} = \{x_n = 0\}$$과 열린집합 $$U_n = \{x_n \neq 0\} \cong \mathbb{A}^n$$의 합집합으로 분해한다. Standard affine cover $$\mathfrak{U} = \{U_0, \ldots, U_n\}$$에 대한 Čech 복합체 $$C^\bullet(\mathfrak{U}, \mathcal{O}(d))$$를 index $$n$$을 포함하는 항과 포함하지 않는 항으로 분해할 수 있다. 구체적으로, $$p$$-cochain $$f_{i_0 \cdots i_p}$$에서 모든 index가 $$\{0, \ldots, n-1\}$$에 속하는 것들은 $$\mathbb{P}^{n-1}$$의 standard affine cover $$\mathfrak{U}' = \{U_0, \ldots, U_{n-1}\}$$에 대한 Čech 복합체 $$C^\bullet(\mathfrak{U}', \mathcal{O}(d))$$의 원소들이며, 적어도 하나의 index가 $$n$$인 것들은 $$U_n$$ (혹은 $$U_n$$과 다른 $$U_i$$들의 교집합) 위에서의 section들이다.

이 분해는 다음과 같은 짧은 완전열을 제공한다. 우선 $$p$$-cochain group을 $$C^p = C^p_0 \oplus C^p_1$$으로 분해하자. 여기서 $$C^p_0$$는 모든 index가 $$\{0, \ldots, n-1\}$$에 속하는 cochain들로 이루어진 부분군이고, $$C^p_1$$은 적어도 하나의 index가 $$n$$인 cochain들로 이루어진 부분군이다. Coboundary map $$\delta$$는 이 분해를 존중한다. 구체적으로, $$\delta = \delta_0 + \delta_1$$으로 분해할 수 있는데, $$\delta_0$$는 index $$n$$을 포함하지 않는 cochain들 사이의 map이고 (이는 $$\mathbb{P}^{n-1}$$의 Čech 복합체 $$C^\bullet(\mathfrak{U}', \mathcal{O}(d))$$의 differential과 일치한다), $$\delta_1$$은 index $$n$$을 포함하는 cochain들과 연관된 부분이다.

$$C^p_1$$을 더 자세히 기술하면, 이는 index $$n$$이 반드시 포함된 $$(p+1)$$-tuple $$(i_0, \ldots, i_{p-1}, n)$$들에 대응되는 섹션들의 직합이다. 이때 $$p$$-tuple $$(i_0, \ldots, i_{p-1})$$는 $$\{0, \ldots, n\}$$의 원소들이므로, $$C^p_1$$은 사실 $$U_n$$의 standard affine cover $$\{U_0 \cap U_n, \ldots, U_{n-1} \cap U_n\}$$에 대한 Čech 복합체 $$C^{p-1}(\{U_i \cap U_n\}, \mathcal{O}(d)|_{U_n})$$에 해당한다. $$U_n \cong \mathbb{A}^n$$이므로, $$\mathcal{O}(d)|_{U_n}$$은 affine variety 위의 quasi-coherent sheaf이고 따라서 $$H^{>0}(U_n, \mathcal{O}(d)) = 0$$이다.

이로부터 짧은 완전열

$$0 \to C^\bullet(\mathfrak{U}', \mathcal{O}(d))[-1] \to C^\bullet(\mathfrak{U}, \mathcal{O}(d)) \to C^\bullet(\{U_i \cap U_n\}, \mathcal{O}(d)|_{U_n}) \to 0$$

을 얻는다. 여기서 첫 번째 map은 index $$n$$을 생략하는 inclusion이고, 두 번째 map은 index $$n$$이 포함된 항을 추출하는 surjection이며, $$[-1]$$은 차수를 1만큼 shift하는 것을 의미한다. 이 짧은 완전열에 해당하는 long exact sequence에서 $$C^\bullet(\{U_i \cap U_n\}, \mathcal{O}(d)|_{U_n})$$의 higher cohomology가 모두 사라지므로, $$0 < q < n$$에 대해 $$H^q(\mathbb{P}^n, \mathcal{O}(d)) \cong H^q(\mathbb{P}^{n-1}, \mathcal{O}(d)) = 0$$이다. $$q = 0$$의 경우 global section은 $$\mathbb{P}^n$$ 전체에서 regular인 degree $$d$$의 homogeneous polynomial들이므로 $$\mathbb{K}[x_0, \ldots, x_n]_d$$이다. $$q = n$$의 경우, $$\mathbb{P}^n$$의 Čech 복합체에서 $$n$$-cochain들은 모든 $$n+1$$개의 index를 포함하는 항 $$f_{0 1 \cdots n} \in \mathcal{O}(d)(U_{01\cdots n})$$이며, 이는 $$\mathbb{K}[x_0^{\pm 1}, \ldots, x_n^{\pm 1}]$$의 원소로 표현된다. $$H^n$$의 원소들은 coboundary image를 제외한 모든 $$a_i \leq -1$$이고 $$\sum a_i = d$$인 monomial $$x_0^{a_0} \cdots x_n^{a_n}$$들로 주어진다. 치환 $$b_i = -a_i - 1$$을 적용하면 $$b_i \geq 0$$이고 $$\sum b_i = -d - n - 1$$이 되어, $$H^n(\mathbb{P}^n, \mathcal{O}(d)) \cong \mathbb{K}[x_0^{-1}, \ldots, x_n^{-1}]_{-d-n-1}$$을 얻는다.

</details>

<div class="remark" markdown="1">

<ins id="rem2">**참고 2**</ins> 위 식에서 $$\mathbb{K}[x_0^{-1}, \ldots, x_n^{-1}]_{-d-n-1}$$은 degree $$-d-n-1$$의 "negative degree" monomial들의 공간이다. 구체적으로:

$$\mathbb{K}[x_0^{-1}, \ldots, x_n^{-1}]_k = \operatorname{Span}\{x_0^{a_0} \cdots x_n^{a_n} : a_i < 0,\, \sum a_i = k\}$$

Bott's formula가 말하는 것을 직관적으로 요약하면 다음과 같다. 먼저 $$H^0$$는 global section의 공간이며, 이는 degree $$d$$의 homogeneous polynomial들이다. 한편 $$H^n$$은 top-degree cohomology로, 오직 $$d \leq -n-1$$일 때만 살아남는다. 이는 $$\mathcal{O}(d)$$가 충분히 negative한 twist일 때만 "top cohomology"에 기여하는 nontrivial class들이 존재한다는 것을 의미한다. 가장 주목할 만한 것은 중간 차수의 cohomology, 즉 $$0 < q < n$$에 대해서는 $$H^q$$가 항상 $$0$$이라는 사실이다. 이는 projective space의 line bundle이 매우 특별한 구조를 가지고 있음을 보여준다.

</div>

<div class="example" markdown="1">

<ins id="ex3">**예시 3 ($$\mathbb{P}^1$$)**</ins>

$$\mathbb{P}^1$$에 대해 Bott's formula는 $$H^0(\mathbb{P}^1, \mathcal{O}(d)) = \mathbb{K}[x_0, x_1]_d$$를 $$d \geq 0$$에 대해, $$H^1(\mathbb{P}^1, \mathcal{O}(d)) = 0$$를 $$d \geq -1$$에 대해, 그리고 $$H^1(\mathbb{P}^1, \mathcal{O}(d)) = \mathbb{K}[x_0^{-1}, x_1^{-1}]_{-d-2}$$를 $$d \leq -2$$에 대해 부여한다. 구체적으로 $$H^1(\mathbb{P}^1, \mathcal{O}(-3))$$은 basis $$\{x_0^{-2}x_1^{-1}, x_0^{-1}x_1^{-2}\}$$를 갖고 dimension 2이다.

이 결과는 기하학적으로 다음과 같이 이해할 수 있다. $$\mathcal{O}(d)$$의 global section들은 degree $$d$$의 homogeneous polynomial들로, $$d \geq 0$$일 때만 존재한다. 이는 $$d \geq 0$$일 때 $$\mathcal{O}(d)$$가 "충분히 긍정적"이어서 bundle의 section들이 zero section을 넘어설 수 있기 때문이다. 반면 $$d \leq -2$$일 때는 global section이 존재하지 않지만, 그 대신 higher cohomology에 nontrivial 정보가 담기게 된다. 이 정보는 Serre duality에 의해 정확하게 $$H^1(\mathbb{P}^1, \mathcal{O}(d)) \cong H^0(\mathbb{P}^1, \mathcal{O}(-d-2))^\vee$$의 관계를 만족한다.

</div>

## Euler Characteristic

Bott's formula는 각 cohomology group의 차원을 개별적으로 계산하지만, 이들을 합산하여 얻는 Euler characteristic<sub>오일러 지표</sub>는 더 간단한 공식으로 표현된다. Euler characteristic은 alternating sum

$$\chi(\mathbb{P}^n, \mathcal{F}) = \sum_{i=0}^{n} (-1)^i \dim H^i(\mathbb{P}^n, \mathcal{F})$$

으로 정의되며, 이는 short exact sequence에 대해 가산적(additive)이라는 중요한 성질을 갖는다. 즉, short exact sequence $$0 \to \mathcal{F} \to \mathcal{G} \to \mathcal{H} \to 0$$에 대해 $$\chi(\mathcal{G}) = \chi(\mathcal{F}) + \chi(\mathcal{H})$$가 성립한다. 따라서 Euler characteristic은 개별 cohomology group의 정보를 잃는 대신, 계산과 조작이 훨씬 용이한 불변량이 된다.

<div class="proposition" markdown="1">

<ins id="cor4">**따름정리 4**</ins> $$\mathbb{P}^n$$ 위의 $$\mathcal{O}(d)$$의 Euler characteristic:

$$\chi(\mathbb{P}^n, \mathcal{O}(d)) = \binom{n+d}{n}$$

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Bott's formula에 의해 cohomology는 세 가지 경우로 나뉜다. 첫째, $$d \geq 0$$인 경우 $$H^0$$만 non-zero이므로 $$\chi(\mathcal{O}(d)) = \dim H^0(\mathbb{P}^n, \mathcal{O}(d)) = \dim \mathbb{K}[x_0, \ldots, x_n]_d = \binom{n+d}{n}$$이다. 둘째, $$-n \leq d \leq -1$$인 경우 모든 cohomology가 사라지므로 $$\chi(\mathcal{O}(d)) = 0$$이고, 이항계수의 일반화에 의해 $$\binom{n+d}{n}$$ 역시 $$0 \leq d+n \leq n-1$$일 때 $$0$$이므로 일치한다. 셋째, $$d \leq -n-1$$인 경우 $$H^n$$만 non-zero이므로 $$\chi(\mathcal{O}(d)) = (-1)^n \dim \mathbb{K}[x_0^{-1}, \ldots, x_n^{-1}]_{-d-n-1}$$이다. 치환 $$a_i' = -a_i - 1$$을 적용하면 $$a_i \leq -1$$이므로 $$a_i' = -a_i - 1 \geq 0$$이 되고, $$\sum a_i' = \sum(-a_i - 1) = -\sum a_i - (n+1) = d + n + 1 - (n+1) = d$$로 변환된다. 따라서 $$\dim \mathbb{K}[x_0^{-1}, \ldots, x_n^{-1}]_{-d-n-1}$$은 $$n+1$$개의 비음수 정수 $$(a_0', \ldots, a_n')$$ 중 합이 $$d$$인 것의 개수이므로 $$\binom{n+d}{n}$$이다. 결과적으로 $$\chi(\mathcal{O}(d)) = (-1)^n \binom{n+d}{n}$$이다. 한편 $$d \leq -n-1$$이면 $$n + d \leq -1$$이고, 일반화된 이항계수의 성질 $$(-1)^n \binom{n+d}{n} = \binom{n+d}{n}$$에 의해 (음수 위에서의 이항계수는 교대부호를 가지므로 $$(-1)^n$$과 정확히 상쇄됨) $$\chi(\mathcal{O}(d)) = \binom{n+d}{n}$$이 성립한다.

</details>

<div class="example" markdown="1">

<ins id="ex5">**예시 5**</ins> $$\mathbb{P}^2$$ 위의 $$\mathcal{O}(d)$$에 대해 $$\chi(\mathcal{O}(d)) = \frac{(d+1)(d+2)}{2}$$이며, 구체적으로 $$\chi(\mathcal{O}(0)) = 1$$, $$\chi(\mathcal{O}(1)) = 3$$, $$\chi(\mathcal{O}(2)) = 6$$이다. 이는 $$\mathbb{P}^2$$에서 degree $$d$$ 곡선이 갖는 기하학적 정보량을 수량화하는 하나의 측도로 이해할 수 있다. 예를 들어, $$\chi(\mathcal{O}(1)) = 3$$은 $$\mathbb{P}^2$$의 직선(line)이 세 개의 independent한 section을 가진다는 사실과 대응된다.

</div>

## Čech Cohomology를 통한 계산

Bott's formula의 증명에서 우리는 이미 standard affine cover를 사용하는 Čech cohomology가 sheaf cohomology와 일치한다는 사실을 사용하였다. 이 절에서는 이 사실을 명시적으로 기술하고, $$\mathbb{P}^1$$의 경우에 대해 Čech 복합체를 명시적으로 전개하여 Bott's formula의 계산을 보다 상세히 보여준다. 이는 앞선 명제 1의 증명에서 sketch한 계산을 보충하는 역할도 한다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> $$\mathbb{P}^n$$의 standard affine cover $$\mathfrak{U} = \{U_0, \ldots, U_n\}$$을 사용하면:

$$H^q(\mathbb{P}^n, \mathcal{O}(d)) \cong \check{H}^q(\mathfrak{U}, \mathcal{O}(d))$$

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

각 intersection $$U_{i_0 \cdots i_p} = U_{i_0} \cap \cdots \cap U_{i_p}$$는 affine이고, $$\mathcal{O}(d)$$는 quasi-coherent이므로 Leray's theorem ([§Čech Cohomology, ⁋명제 10](/ko/math/algebraic_geometry/cech_cohomology#prop10))에 의해 Čech cohomology가 sheaf cohomology와 일치한다.

</details>

<div class="example" markdown="1">

<ins id="ex7">**예시 7 ($$\mathbb{P}^1$$의 명시적 계산)**</ins>

명제 6에 의해 $$\mathbb{P}^1$$에서의 Čech cohomology가 sheaf cohomology와 일치하므로, 우리는 명시적으로 Čech 복합체를 전개하여 ([명제 1](#prop1))의 $$n = 1$$인 경우를 다시 한번 확인한다.

$$\mathfrak{U} = \{U_0, U_1\}$$에 대해 Čech 복합체는 $$0 \to C^0 \xrightarrow{\delta} C^1 \to 0$$이며, 여기서 $$C^0 = \mathcal{O}(d)(U_0) \oplus \mathcal{O}(d)(U_1)$$이고 $$C^1 = \mathcal{O}(d)(U_0 \cap U_1)$$이다. $$U_0 \cong \mathbb{A}^1$$에서 coordinate $$t = x_1/x_0$$를 사용하면 $$\mathcal{O}(d)(U_0) = \mathbb{K}[t] \cdot 1$$이고, $$U_1$$에서 $$s = x_0/x_1 = t^{-1}$$를 사용하면 $$\mathcal{O}(d)(U_1) = \mathbb{K}[s] \cdot s^{-d} = t^d \mathbb{K}[t^{-1}]$$이다. 교집합에서는 $$\mathcal{O}(d)(U_0 \cap U_1) = \mathbb{K}[t, t^{-1}] \cdot 1$$이다.

Coboundary map $$\delta : C^0 \to C^1$$은 $$(f_0, f_1) \mapsto f_1 - f_0$$로 주어진다. 따라서 $$\ker \delta = \{(f_0, f_1) \in \mathbb{K}[t] \oplus t^d\mathbb{K}[t^{-1}] : f_0 = f_1\}$$이고, 이는 $$\mathbb{K}[t] \cap t^d\mathbb{K}[t^{-1}]$$과 동형이다. $$d \geq 0$$일 때 $$\mathbb{K}[t] \cap t^d\mathbb{K}[t^{-1}] = \operatorname{Span}\{1, t, \ldots, t^d\}$$이므로 $$H^0 \cong \mathbb{K}[x_0, x_1]_d$$이고 $$\dim H^0 = d+1$$이다. $$d \leq -1$$일 때 $$\ker \delta = 0$$이므로 $$H^0 = 0$$이다.

$$H^1$$은 cokernel $$\mathbb{K}[t, t^{-1}] / \operatorname{im}\delta$$로 주어진다. $$d \geq 0$$이면 $$\operatorname{im}\delta$$는 $$t^d\mathbb{K}[t^{-1}]$$과 $$\mathbb{K}[t]$$의 합이고, $$\mathbb{K}[t, t^{-1}] = t^d\mathbb{K}[t^{-1}] + \mathbb{K}[t]$$이므로 cokernel은 $$0$$이다. $$d \leq -1$$이면 $$\operatorname{im}\delta = t^d\mathbb{K}[t^{-1}] - \mathbb{K}[t]$$이고, $$t^{-d-1}$$ 이상의 negative monomial들이 cokernel을 이룬다. $$\mathbb{K}[t, t^{-1}] = t^d\mathbb{K}[t^{-1}] + \mathbb{K}[t] + \operatorname{Span}\{t^{-d-1}, \ldots, t^{-1}\}$$이므로, $$H^1 \cong \operatorname{Span}\{t^{-d-1}, \ldots, t^{-1}\}$$이고 $$\dim H^1 = -d-1$$이다. 이는 $$\mathbb{K}[x_0^{-1}, x_1^{-1}]_{-d-2}$$의 차원과 일치한다.

</div>

## Regularity

지금까지 우리는 $$\mathcal{O}(d)$$라는 매우 특수한 sheaf의 cohomology를 계산하였다. 그러나 대수기하학에서 실제로 마주치는 sheaf는 임의의 coherent sheaf $$\mathcal{F}$$이며, 이의 cohomology를 모두 계산하는 것은 일반적으로 불가능하다. 다행히도 coherent sheaf의 cohomology를 다룰 때, “충분히 twist하면 high cohomology가 vanish한다”는 현상이 자주 나타난다. 이는 Serre vanishing theorem으로 정밀화된다: 임의의 coherent sheaf $$\mathcal{F}$$에 대해 충분히 큰 $$m$$에 대해 $$H^i(\mathbb{P}^n, \mathcal{F}(m)) = 0$$이 $$i > 0$$에 대해 성립한다. 예를 들어, Bott's formula에서 $$H^q(\mathbb{P}^n, \mathcal{O}(d))$$가 $$q > 0$$에서 vanish하는 $$d$$의 범위는 $$d \geq -n$$이다. Regularity는 이 현상을 정량화하여, 구체적으로 어느 정도 twist해야 higher cohomology가 사라지는지를 기록하는 개념이다.

<div class="definition" markdown="1">

<ins id="def8">**정의 8**</ins> Coherent sheaf $$\mathcal{F}$$ on $$\mathbb{P}^n$$이 **$$m$$-regular**라는 것은 $$i > 0$$에 대해 $$H^i(\mathbb{P}^n, \mathcal{F}(m-i)) = 0$$인 것이다.

</div>

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9 (Castelnuovo-Mumford Regularity)**</ins> $$\mathcal{F}$$가 $$m$$-regular이면 $$\mathcal{F}(m)$$은 globally generated이고, $$i > 0$$이고 $$k \geq m - i$$인 모든 $$i, k$$에 대해 $$H^i(\mathbb{P}^n, \mathcal{F}(k)) = 0$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Mumford의 증명 전략은 $$\mathbb{P}^n$$의 차원 $$n$$에 대한 귀납법이다. $$n = 0$$인 경우 coherent sheaf는 finite-dimensional vector space이고 모든 higher cohomology가 사라지므로 자명하다. 이제 $$n \geq 1$$이라 가정하자.

핵심은 hyperplane $$H \cong \mathbb{P}^{n-1}$$으로의 restriction을 이용하는 것이다. 일반적인 linear form $$s \in H^0(\mathbb{P}^n, \mathcal{O}(1))$$에 대해 다음 short exact sequence를 얻는다.

$$0 \to \mathcal{F}(k-1) \xrightarrow{\cdot s} \mathcal{F}(k) \to \mathcal{F}(k)|_H \to 0$$

이 sequence의 cohomology long exact sequence는 다음을 준다.

$$\cdots \to H^i(\mathcal{F}(k-1)) \to H^i(\mathcal{F}(k)) \to H^i(\mathcal{F}(k)|_H) \to H^{i+1}(\mathcal{F}(k-1)) \to \cdots$$

**1단계: $$\mathcal{F}$$가 $$(m+1)$$-regular임.** $$\mathcal{F}$$가 $$m$$-regular이므로 $$H^i(\mathcal{F}(m-i)) = 0$$이 $$i > 0$$에 대해 성립한다. 우선 $$\mathcal{F}|_H$$가 $$(m+1)$$-regular임을 보이자. Short exact sequence에서 $$k = m - i + 1$$ ($$i \geq 1$$)을 대입하면

$$0 \to \mathcal{F}(m-i) \to \mathcal{F}(m-i+1) \to \mathcal{F}(m-i+1)|_H \to 0$$

이고, 이의 long exact sequence에서

$$H^i(\mathcal{F}(m-i)) \to H^i(\mathcal{F}(m-i+1)) \to H^i(\mathcal{F}|_H(m-i+1)) \to H^{i+1}(\mathcal{F}(m-i))$$

이다. $$\mathcal{F}$$의 $$m$$-regularity에 의해 $$H^i(\mathcal{F}(m-i)) = 0$$ ($$i > 0$$)이고 $$H^{i+1}(\mathcal{F}(m-i)) = 0$$ ($$i+1 > 1$$)이므로, $$H^i(\mathcal{F}|_H(m-i+1)) = 0$$을 $$0 < i \leq n-1$$에 대해 얻는다. 이것은 $$\mathcal{F}|_H$$가 $$(m+1)$$-regular임을 의미한다.

이제 귀납적 가정을 $$H \cong \mathbb{P}^{n-1}$$에 적용한다. $$\mathcal{F}|_H$$가 $$(m+1)$$-regular이므로, 명제의 결론이 $$\mathbb{P}^{n-1}$$에서 성립한다고 가정하면 $$H^i(\mathcal{F}|_H(m+1-i+j)) = 0$$이 $$j \geq 0$$, $$0 < i \leq n-1$$에 대해 성립한다. 특히 $$j = 0$$일 때 $$H^i(\mathcal{F}(m+1-i)|_H) = 0$$이다.

다시 short exact sequence에서 $$k = m + 1 - i$$를 대입하면

$$H^i(\mathcal{F}(m+1-i)) \to H^i(\mathcal{F}(m+1-i)|_H) \to H^{i+1}(\mathcal{F}(m-i))$$

인데, $$H^i(\mathcal{F}(m+1-i)|_H) = 0$$ (위에서 귀납적 가정으로 얻음)이고 $$H^{i+1}(\mathcal{F}(m-i)) = 0$$ ($$m$$-regularity)이므로 $$H^i(\mathcal{F}(m+1-i)) = 0$$이다. 즉 $$\mathcal{F}$$는 $$(m+1)$$-regular이다. 귀납적으로 $$\mathcal{F}$$는 임의의 $$m' \geq m$$에 대해 $$m'$$-regular이며, 이로부터 $$k \geq m - i$$일 때 $$H^i(\mathcal{F}(k)) = 0$$이 성립한다.

**2단계: $$\mathcal{F}(m)$$은 globally generated.** Evaluation map $$\epsilon : H^0(\mathcal{F}(m)) \otimes \mathcal{O} \to \mathcal{F}(m)$$을 생각하자. 이 map이 surjective임을 보이기 위해, 임의의 점 $$p \in \mathbb{P}^n$$에서 fiber $$\mathcal{F}(m) \otimes \kappa(p)$$가 $$H^0(\mathcal{F}(m))$$의 상으로 생성됨을 보인다. $$p$$를 지나는 일반적인 hyperplane $$H$$를 택하고, 위의 short exact sequence에서 $$k = m$$을 대입하면

$$0 \to \mathcal{F}(m-1) \to \mathcal{F}(m) \to \mathcal{F}(m)|_H \to 0$$

이다. 여기서 $$H^1(\mathcal{F}(m-1)) = 0$$ ($$m$$-regularity에서 $$i = 1$$인 경우)이므로 $$H^0(\mathcal{F}(m)) \to H^0(\mathcal{F}(m)|_H)$$가 surjective이다. 귀납적 가정에 의해 $$\mathcal{F}(m)|_H$$는 $$H \cong \mathbb{P}^{n-1}$$ 위에서 globally generated이므로, $$\mathcal{F}(m)|_H$$의 fiber at $$p$$는 $$H^0(\mathcal{F}(m)|_H)$$의 상으로 생성된다. $$H^0(\mathcal{F}(m)) \to H^0(\mathcal{F}(m)|_H)$$가 surjective이므로, $$\mathcal{F}(m)$$의 global section들도 $$p$$에서의 fiber를 생성한다. 따라서 $$\mathcal{F}(m)$$은 globally generated이다.

</details>

<div class="example" markdown="1">

<ins id="ex10">**예시 10**</ins> Line bundle $$\mathcal{O}(d)$$의 regularity를 계산해보자. $$d \geq 0$$이면 Bott's formula에 의해 $$H^i(\mathbb{P}^n, \mathcal{O}(d)) = 0$$이 $$i > 0$$에 대해 성립한다. 그런데 $$\mathcal{O}(d)$$의 $$m$$-regularity 조건은 $$H^i(\mathcal{O}(d+m-i)) = 0$$ ($$i > 0$$)이다. $$m = 0$$을 택하면 $$H^i(\mathcal{O}(d-i))$$를 확인해야 하는데, $$i = 1$$일 때 $$H^1(\mathcal{O}(d-1))$$은 $$d \geq 1$$이면 $$0$$이지만 $$d = 0$$이면 $$H^1(\mathcal{O}(-1)) = 0$$ (Bott's formula에서 $$-1$$은 $$-1 \geq -n$$이므로 모든 cohomology가 $$0$$)이다. 일반적으로 $$d \geq 0$$이고 $$i > 0$$일 때 $$d - i \geq -n$$이면 $$H^i(\mathcal{O}(d-i)) = 0$$이다. 문제는 $$d - i < -n$$, 즉 $$i > d + n$$인 경우인데, 이때 $$i > n$$이 되어 어차피 $$H^i = 0$$이다. 따라서 $$\mathcal{O}(d)$$는 $$0$$-regular이다. 명제 9에 의해 $$\mathcal{O}(d)$$는 $$d \geq 0$$일 때 globally generated이며, 이는 ([§Line Bundles, ⁋예시 16](/ko/math/algebraic_geometry/line_bundles#ex16))에서 확인한 바와 일치한다.

</div>

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.
**[Bot]** R. Bott, *Homogeneous vector bundles*, Annals of Mathematics, 1957.
**[Mum]** D. Mumford, *Lectures on Curves on an Algebraic Surface*, Annals of Mathematics Studies, Princeton, 1966.
