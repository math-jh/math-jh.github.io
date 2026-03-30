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
weight: 15
published: false
---

## 도입

Projective space $$\mathbb{P}^n$$ 위의 line bundle $$\mathcal{O}(d)$$ ([§Line Bundles, ⁋예시 12](/ko/math/algebraic_geometry/line_bundles#ex12))의 cohomology ([§Sheaf Cohomology, ⁋정의 1](/ko/math/algebraic_geometry/sheaf_cohomology#def1))는 완전히 계산된다. 이 계산은 대수기하학의 기본적인 도구이며, Serre duality, Riemann-Roch theorem 등의 응용에서 필수적이다.

## Bott's Formula

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

Standard affine cover $$\mathfrak{U} = \{U_0, \ldots, U_n\}$$, $$U_i = \{x_i \neq 0\}$$를 사용한다. 각 intersection $$U_{i_0 \cdots i_p}$$은 affine이고 $$\mathcal{O}(d)$$는 quasi-coherent이므로, [Leray's theorem](/ko/math/algebraic_geometry/cech_cohomology#prop10)에 의해 $$H^q(\mathbb{P}^n, \mathcal{O}(d)) \cong \check{H}^q(\mathfrak{U}, \mathcal{O}(d))$$이다.

$$\mathcal{O}(d)(U_i)$$는 $$x_i^{-d}\mathbb{K}[x_0/x_i, \ldots, \hat{x_i}/x_i, \ldots, x_n/x_i]$$이므로, Čech cochain $$f \in C^p(\mathfrak{U}, \mathcal{O}(d))$$는 각 $$p+1$$-tuple $$(i_0, \ldots, i_p)$$에 대해 $$U_{i_0 \cdots i_p}$$ 위에서 regular한 섹션을 대응시키는 것이다. 이는 Laurent polynomial $$f_{i_0 \cdots i_p} = x_0^{a_0} \cdots x_n^{a_n}$$ (모든 $$a_j \geq -1$$이고 $$\sum a_j = d$$)들로 표현된다.

Coboundary map $$\delta : C^p \to C^{p+1}$$은 $$(\delta f)_{i_0 \cdots i_{p+1}} = \sum_{k=0}^{p+1} (-1)^k f_{i_0 \cdots \hat{i_k} \cdots i_{p+1}}$$로 주어진다. Cochain $$f_{i_0 \cdots i_p} = x_0^{a_0} \cdots x_n^{a_n}$$을 monomial로 생각하면, coboundary는 각 항에서 하나의 index를 제거하는 것이므로, $$H^p = \ker \delta / \operatorname{im} \delta$$의 차원을 계산하면 된다.

**$$\mathbb{P}^1$$의 경우.** $$n = 1$$일 때 Čech 복합체는 $$0 \to C^0 \xrightarrow{\delta} C^1 \to 0$$이다. 여기서 $$C^0 = \mathcal{O}(d)(U_0) \oplus \mathcal{O}(d)(U_1)$$이고 $$C^1 = \mathcal{O}(d)(U_0 \cap U_1)$$이다. $$U_0$$에서 coordinate $$t = x_1/x_0$$, $$U_1$$에서 $$s = x_0/x_1 = t^{-1}$$를 사용하면:

$$\mathcal{O}(d)(U_0) = \mathbb{K}[t] \cdot 1, \quad \mathcal{O}(d)(U_1) = \mathbb{K}[s] \cdot s^{-d} = \mathbb{K}[s] \cdot t^d, \quad \mathcal{O}(d)(U_0 \cap U_1) = \mathbb{K}[t, t^{-1}] \cdot 1$$

Coboundary map $$\delta(f_0, f_1) = f_1 - f_0$$에서 $$f_0 \in \mathbb{K}[t]$$, $$f_1 \in t^d \mathbb{K}[t^{-1}]$$이다.

- $$d \geq 0$$: $$H^0 = \ker \delta = \{f_0 = f_1\} = \mathbb{K}[t] \cap t^d\mathbb{K}[t^{-1}] = \mathbb{K}[x_0, x_1]_d$$이며 차원은 $$d+1$$이다. $$H^1 = 0$$.
- $$d \leq -1$$: $$H^0 = \ker \delta = 0$$이고, $$H^1 = \operatorname{coker} \delta$$. $$\operatorname{im} \delta$$의 여집합은 degree $$-d-1$$ 이하의 negative monomial $$\{t^{-d-1}, t^{-d-2}, \ldots\}$$이므로, $$H^1$$의 차원은 $$-d-1$$이다. 이는 $$\mathbb{K}[x_0^{-1}, x_1^{-1}]_{-d-2}$$의 차원과 일치한다.

**일반 $$\mathbb{P}^n$$에 대한 귀납법.** $$\mathbb{P}^n$$의 Čech 복합체 $$C^\bullet(\mathfrak{U}, \mathcal{O}(d))$$에서 각 cochain $$f_{i_0 \cdots i_p}$$은 index $$i_0, \ldots, i_p$$에 해당하는 variable들이 coefficient $$\geq -1$$인 monomial $$x_0^{a_0} \cdots x_n^{a_n}$$ ($$\sum a_j = d$$)로 표현된다.

우리는 $$n$$에 대한 귀납법으로 증명한다. $$\mathbb{P}^n = \mathbb{P}^{n-1} \cup U_n$$에서, $$U_n \cong \mathbb{A}^n$$이므로 $$H^{>0}(U_n, \mathcal{O}(d)) = 0$$이다. Mayer-Vietoris sequence (또는 Čech 복합체를 $$U_n$$이 포함/미포함된 항으로 분해하는 방법)를 사용하면 $$\mathbb{P}^{n-1}$$ 위의 cohomology로 귀납할 수 있다. 귀납적 가정과 $$\mathbb{P}^{n-1} \cap U_n \cong \mathbb{A}^n$$에서의 acyclicity를 결합하면, $$H^q(\mathbb{P}^n, \mathcal{O}(d))$$가 $$q = 0, n$$에서만 non-zero이고 그 값이 주어진 공간과 일치함을 얻는다.

</details>

<div class="remark" markdown="1">

<ins id="rem2">**참고 2**</ins> 위 식에서 $$\mathbb{K}[x_0^{-1}, \ldots, x_n^{-1}]_{-d-n-1}$$은 degree $$-d-n-1$$의 "negative degree" monomial들의 공간이다. 예를 들어:

$$\mathbb{K}[x_0^{-1}, \ldots, x_n^{-1}]_k = \operatorname{Span}\{x_0^{a_0} \cdots x_n^{a_n} : a_i < 0, \sum a_i = k\}$$

</div>

<div class="example" markdown="1">

<ins id="ex3">**예시 3 ($$\mathbb{P}^1$$)**</ins>

$$\mathbb{P}^1$$에 대해 Bott's formula는 $$H^0(\mathbb{P}^1, \mathcal{O}(d)) = \mathbb{K}[x_0, x_1]_d$$를 $$d \geq 0$$에 대해, $$H^1(\mathbb{P}^1, \mathcal{O}(d)) = 0$$를 $$d \geq -1$$에 대해, 그리고 $$H^1(\mathbb{P}^1, \mathcal{O}(d)) = \mathbb{K}[x_0^{-1}, x_1^{-1}]_{-d-2}$$를 $$d \leq -2$$에 대해 부여한다. 구체적으로 $$H^1(\mathbb{P}^1, \mathcal{O}(-3))$$은 basis $$\{x_0^{-2}x_1^{-1}, x_0^{-1}x_1^{-2}\}$$를 갖고 dimension 2이다.

</div>

## Euler Characteristic

<div class="corollary" markdown="1">

<ins id="cor4">**따름정리 4**</ins> $$\mathbb{P}^n$$ 위의 $$\mathcal{O}(d)$$의 Euler characteristic:

$$\chi(\mathbb{P}^n, \mathcal{O}(d)) = \binom{n+d}{n}$$

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Bott's formula에서 $$H^0$$만 non-zero인 경우($$d \geq 0$$)를 고려하면 $$\chi(\mathcal{O}(d)) = \dim H^0(\mathcal{O}(d)) = \dim \mathbb{K}[x_0, \ldots, x_n]_d = \binom{n+d}{n}$$이다. $$d \leq -n-1$$인 경우에는 $$H^n$$만 non-zero이므로 $$\chi(\mathcal{O}(d)) = (-1)^n \dim \mathbb{K}[x_0^{-1}, \ldots, x_n^{-1}]_{-d-n-1}$$이다. 치환 $$a_i' = -a_i - 1$$을 적용하면 $$a_i < 0$$, $$\sum a_i = -d - n - 1$$인 조건이 $$a_i' \geq 0$$, $$\sum a_i' = d$$로 변환되어, $$\dim \mathbb{K}[x_0^{-1}, \ldots, x_n^{-1}]_{-d-n-1} = \dim \mathbb{K}[x_0, \ldots, x_n]_d = \binom{n+d}{n}$$이므로 동일한 formula를 얻는다.

</details>

<div class="example" markdown="1">

<ins id="ex5">**예시 5**</ins> $$\mathbb{P}^2$$ 위의 $$\mathcal{O}(d)$$에 대해 $$\chi(\mathcal{O}(d)) = \frac{(d+1)(d+2)}{2}$$이며, 구체적으로 $$\chi(\mathcal{O}(0)) = 1$$, $$\chi(\mathcal{O}(1)) = 3$$, $$\chi(\mathcal{O}(2)) = 6$$이다.

</div>

## Čech Cohomology를 통한 계산

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> $$\mathbb{P}^n$$의 standard affine cover $$\mathfrak{U} = \{U_0, \ldots, U_n\}$$을 사용하면:

$$H^q(\mathbb{P}^n, \mathcal{O}(d)) \cong \check{H}^q(\mathfrak{U}, \mathcal{O}(d))$$

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

각 intersection $$U_{i_0 \cdots i_p} = U_{i_0} \cap \cdots \cap U_{i_p}$$는 affine이고, $$\mathcal{O}(d)$$는 quasi-coherent이므로 [Leray's theorem](/ko/math/algebraic_geometry/cech_cohomology#prop10)에 의해 Čech cohomology가 sheaf cohomology와 일치한다.

</details>

<div class="example" markdown="1">

<ins id="ex7">**예시 7 (Explicit calculation for $$\mathbb{P}^1$$)**</ins>

$$\mathfrak{U} = \{U_0, U_1\}$$에 대해 Čech 복합체는 $$0 \to C^0 \xrightarrow{\delta} C^1 \to 0$$이며, 여기서 $$C^0 = \mathcal{O}(d)(U_0) \oplus \mathcal{O}(d)(U_1)$$이고 $$C^1 = \mathcal{O}(d)(U_0 \cap U_1)$$이다. $$U_0 \cong \mathbb{A}^1$$에서 coordinate $$t = x_1/x_0$$를 사용하면 $$\mathcal{O}(d)(U_0) = \mathbb{K}[t] \cdot 1$$이고, $$U_1$$에서 $$s = x_0/x_1 = t^{-1}$$를 사용하면 $$\mathcal{O}(d)(U_1) = \mathbb{K}[s] \cdot s^{-d} = t^d \mathbb{K}[t^{-1}]$$이다. 교집합에서는 $$\mathcal{O}(d)(U_0 \cap U_1) = \mathbb{K}[t, t^{-1}] \cdot 1$$이다.

Coboundary map $$\delta : C^0 \to C^1$$은 $$(f_0, f_1) \mapsto f_1 - f_0$$로 주어진다. 따라서 $$\ker \delta = \{(f_0, f_1) \in \mathbb{K}[t] \oplus t^d\mathbb{K}[t^{-1}] : f_0 = f_1\}$$이고, 이는 $$\mathbb{K}[t] \cap t^d\mathbb{K}[t^{-1}]$$과 동형이다. $$d \geq 0$$일 때 $$\mathbb{K}[t] \cap t^d\mathbb{K}[t^{-1}] = \operatorname{Span}\{1, t, \ldots, t^d\}$$이므로 $$H^0 \cong \mathbb{K}[x_0, x_1]_d$$이고 $$\dim H^0 = d+1$$이다. $$d \leq -1$$일 때 $$\ker \delta = 0$$이므로 $$H^0 = 0$$이다.

$$H^1$$은 cokernel $$\mathbb{K}[t, t^{-1}] / \operatorname{im}\delta$$로 주어진다. $$d \geq 0$$이면 $$\operatorname{im}\delta$$는 $$t^{-\infty}, \ldots, t^{-1}, t^0, t^1, \ldots, t^d$$의 span이므로 cokernel은 $$0$$이다. $$d \leq -1$$이면 $$\operatorname{im}\delta = t^d\mathbb{K}[t^{-1}] - \mathbb{K}[t]$$이고, $$t^{-d-1}$$ 이상의 negative monomial들이 cokernel을 이룬다. $$\mathbb{K}[t, t^{-1}] = t^d\mathbb{K}[t^{-1}] + \mathbb{K}[t] + \operatorname{Span}\{t^{-d-1}, \ldots, t^{-1}\}$$이므로, $$H^1 \cong \operatorname{Span}\{t^{-d-1}, \ldots, t^{-1}\}$$이고 $$\dim H^1 = -d-1$$이다. 이는 $$\mathbb{K}[x_0^{-1}, x_1^{-1}]_{-d-2}$$의 차원과 일치한다.

</div>

## Regularity

Coherent sheaf의 cohomology를 다룰 때, "충분히 twist하면 high cohomology가 vanish한다"는 현상이 자주 나타난다. Regularity는 이 현상을 정량화하여, 구체적으로 어느 정도 twist해야 하는지를 기록하는 개념이다. 예를 들어, Bott's formula에서 $$H^q(\mathbb{P}^n, \mathcal{O}(d))$$가 $$q > 0$$에서 vanish하는 $$d$$의 범위는 $$d \geq -n$$이며, regularity는 이러한 vanishing threshold를 coherent sheaf 일반에 대해 체계화한 것이다.

<div class="definition" markdown="1">

<ins id="def8">**정의 8**</ins> Coherent sheaf $$\mathcal{F}$$ on $$\mathbb{P}^n$$이 **$$m$$-regular**라는 것은 $$i > 0$$에 대해 $$H^i(\mathbb{P}^n, \mathcal{F}(m-i)) = 0$$인 것이다.

</div>

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9 (Castelnuovo-Mumford Regularity)**</ins> $$\mathcal{F}$$가 $$m$$-regular이면 $$\mathcal{F}(m)$$은 globally generated이고, $$H^i(\mathbb{P}^n, \mathcal{F}(k)) = 0$$ for $$i > 0$$ and $$k \geq m - i$$이다.

</div>

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[Bot]** R. Bott, *Homogeneous vector bundles*, Annals of Mathematics, 1957.
