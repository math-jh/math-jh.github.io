---
title: "Riemann–Roch 정리"
excerpt: "The Riemann–Roch theorem for curves and surfaces"

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/riemann_roch_theorem
sidebar:
    nav: "algebraic_geometry-ko"

header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Riemann_Roch.png
    overlay_filter: 0.5

date: 2026-03-15
last_modified_at: 2026-03-15
weight: 12
published: false
---

([§선다발과 벡터다발, ⁋예시 24](/ko/math/algebraic_geometry/line_bundles#ex24))에서 우리는 variety $$X$$의 tangent bundle $$\mathcal{T}_X$$와 cotangent bundle $$\Omega_X^1$$을 정의하고, 이로부터 canonical line bundle $$\omega_X = \bigwedge^{\dim X} \Omega_X^1$$을 얻었다. 또 canonical line bundle $$\omega_X$$에 대응하는 divisor를 canonical divisor $$K_X$$라 부른다.

이제 우리는 이 두 객체를 이용하여 **Riemann–Roch 정리**를 서술한다. [§선형계, ⁋정의 2](/ko/math/algebraic_geometry/linear_systems#def2)에서 우리는 line bundle $$\mathcal{L}$$의 complete linear system $$\lvert \mathcal{L} \rvert = \mathbb{P}(H^0(X, \mathcal{L}))$$을 정의하였고, 이것이 $$\mathcal{L}$$과 linearly equivalent한 effective divisor들의 모임이라는 것을 보았다. 그렇다면 가장 자연스러운 질문은 $$H^0(X, \mathcal{L})$$의 차원, 즉 $$\dim H^0(X, \mathcal{L})$$을 어떻게 계산하느냐이다. Riemann–Roch 정리는 바로 이 질문에 대한 답을 제공하며, 특히 곡선과 곡면에 대해 매우 구체적인 결과를 준다.

## 곡선에서의 Riemann–Roch 정리

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Smooth projective curve $$C$$ 위의 divisor $$D$$에 대해 *Riemann–Roch 차원*을

$$\ell(D) = \dim H^0(C, \mathcal{O}_C(D))$$

라고 정의한다.

</div>

이 차원은 $$D$$의 complete linear system $$\lvert D \rvert$$의 dimension과 같다. ([§선형계, ⁋정의 2](/ko/math/algebraic_geometry/linear_systems#def2)) 즉, $$\ell(D) - 1$$은 $$D$$와 linearly equivalent한 effective divisor들이 이루는 projective space의 dimension이다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> (Riemann–Roch for curves) Smooth projective curve $$C$$ 위의 divisor $$D$$에 대해

$$\ell(D) - \ell(K_C - D) = \deg D + 1 - g$$

이 성립한다. 여기서 $$g$$는 $$C$$의 genus, $$K_C$$는 canonical divisor이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Smooth projective curve $$C$$에 대해 Serre duality ([§Serre Duality, ⁋정리 1](/ko/math/algebraic_geometry/serre_duality#thm1))에 의하여

$$H^1(C, \mathcal{O}_C(D)) \cong H^0(C, \omega_C \otimes \mathcal{O}_C(-D))^\vee = H^0(C, \mathcal{O}_C(K_C - D))^\vee$$

이 성립한다. 따라서 $$h^1(C, \mathcal{O}_C(D)) = h^0(C, \mathcal{O}_C(K_C - D)) = \ell(K_C - D)$$이다.

한편 Euler characteristic

$$\chi(\mathcal{O}_C(D)) = h^0(C, \mathcal{O}_C(D)) - h^1(C, \mathcal{O}_C(D)) = \ell(D) - \ell(K_C - D)$$

은 곡선에 대한 Riemann–Roch 정리에 의해 $$\chi(\mathcal{O}_C(D)) = \deg D + 1 - g$$와 같다. 이 두 식을 합치면 명제가 얻어진다. 여기서 $$g = h^1(C, \mathcal{O}_C)$$는 curve $$C$$의 *genus*라 부르는 기하학적 불변량으로, 이 값은 $$\deg K_C = 2g - 2$$ 및 $$h^0(C, \omega_C) = g$$를 만족한다.

</details>

Riemann–Roch 정리의 핵심적인 유용성은 다음과 같은 상황에서 드러난다. 만약 $$\deg D > 2g - 2$$, 즉 $$\deg(K_C - D) < 0$$이라면 $$K_C - D$$는 음수 차수를 갖고, 따라서 $$K_C - D$$는 effective divisor와 linearly equivalent할 수 없으므로 $$\ell(K_C - D) = 0$$이 되어, 식이 $$\ell(D) = \deg D + 1 - g$$로 단순화된다. 따라서 충분히 큰 degree의 divisor에 대해서는 $$\ell(D)$$를 직접적으로 계산할 수 있다. 반면 작은 degree에서는 $$\ell(K_C - D)$$ 항이 남아 정밀한 정보를 제공하는데, 이 항이 바로 canonical divisor $$K_C$$의 기하학적 의미이다.

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> **$$\mathbb{P}^1$$**: $$\mathbb{P}^1$$의 genus는 $$g = 0$$이고, canonical divisor는 $$K_{\mathbb{P}^1} = -2H$$이다 ([§Canonical Bundle, ⁋예시 8](/ko/math/algebraic_geometry/canonical_bundle#ex8)). ([§선다발과 벡터다발, ⁋예시 12](/ko/math/algebraic_geometry/line_bundles#ex12))에서 $$\mathcal{O}_{\mathbb{P}^1}(d)$$의 global section이 차수 $$d$$의 동차다항식들임을 보였으므로,

$$\ell(dH) = d+1 \quad (d \ge 0), \qquad \ell(dH) = 0 \quad (d < 0).$$

이다. Riemann–Roch 식을 확인해보면, $$D = dH$$에 대해 $$\deg D = d$$이고 $$K_C - D = (-2-d)H$$이므로

$$\ell(dH) - \ell(-2H-dH) = d + 1 - 0 = d + 1$$

이 되어 양변이 모두 $$d+1$$로 일치함을 확인할 수 있다.

</div>

<div class="example" markdown="1">

<ins id="ex4">**예시 4**</ins> **Genus 1 curve (elliptic curve)**: $$g = 1$$이므로 $$\deg K_C = 2g - 2 = 0$$이다. Riemann–Roch에서 $$D = 0$$을 대입하면 $$\ell(K_C) - \ell(0) = 0 + 1 - 1 = 0$$, 즉 $$\ell(K_C) = \ell(0) = 1$$이다. Degree가 0이고 $$\ell(K_C) = 1$$인 divisor는 반드시 trivial, 즉 $$K_C \sim 0$$이다. 따라서 Riemann–Roch 식은

$$\ell(D) - \ell(-D) = \deg D$$

이 된다. 특히 $$\deg D > 0$$이면 $$\ell(-D) = 0$$이므로 $$\ell(D) = \deg D$$이다. 또 $$\deg D = 0$$이면 $$\ell(D) = 1$$ 또는 $$0$$인데, $$D \sim 0$$인 경우에만 $$\ell(D) = 1$$이다.

</div>

<div class="example" markdown="1">

<ins id="ex5">**예시 5**</ins> **Genus 2 curve**: $$g = 2$$이면 $$\deg K_C = 2g - 2 = 2$$이다. Canonical divisor $$K_C$$는 두 점의 linear equivalence class이다. 일반적인 점 $$p$$에 대해 $$D = d \cdot p$$라고 하자.

- $$d = 0$$: $$\ell(0) = 1$$ (상수함수만).
- $$d = 1$$: $$\ell(p) \ge 2$$라면 degree 1 사상 $$C \to \mathbb{P}^1$$이 존재하여 $$C \cong \mathbb{P}^1$$이 되지만 $$g = 2$$와 모순이므로 $$\ell(p) = 1$$이다. RR에 의해 $$\ell(p) - \ell(K_C - p) = 1 + 1 - 2 = 0$$이므로 $$\ell(K_C - p) = 1$$이다.
- $$d = 2$$: 만약 $$2p \sim K_C$$이면 $$\ell(K_C - 2p) = \ell(0) = 1$$이므로 $$\ell(2p) - 1 = 2 + 1 - 2 = 1$$, 즉 $$\ell(2p) = 2$$이다. 이 경우 $$p$$를 *Weierstrass point*라 부른다. 일반적인 점에서는 $$2p \not\sim K_C$$이므로 $$\ell(K_C - 2p) = 0$$이고 $$\ell(2p) = 1$$이다.
- $$d \ge 3$$: $$\deg(K_C - D) = 2 - d < 0$$이므로 $$\ell(K_C - D) = 0$$이고, 따라서 $$\ell(D) = d - 1$$이다.

</div>

## 곡면에서의 Riemann–Roch 정리

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> Smooth projective surface $$S$$ 위의 divisor $$D$$에 대해 *Euler characteristic*을

$$\chi(\mathcal{O}_S(D)) = \sum_{i=0}^2 (-1)^i h^i(S, \mathcal{O}_S(D)) = h^0(S, \mathcal{O}_S(D)) - h^1(S, \mathcal{O}_S(D)) + h^2(S, \mathcal{O}_S(D))$$

라고 정의한다. 여기서 $$h^i(S, \mathcal{O}_S(D)) = \dim H^i(S, \mathcal{O}_S(D))$$이다.

</div>

Curve의 경우와 달리 surface에서는 $$H^2$$ 항이 추가로 등장한다. $$h^0$$은 global section의 수이고, $$h^1$$과 $$h^2$$는 더 높은 cohomology group들의 dimension이다. Smooth projective surface에 대한 Serre duality에 의해 $$h^2(S, \mathcal{O}_S(D)) = h^0(S, \omega_S \otimes \mathcal{O}_S(-D)) = h^0(S, \mathcal{O}_S(K_S - D))$$이다. Riemann–Roch for surfaces는 이 Euler characteristic을 intersection number로 계산할 수 있게 해준다.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> (Riemann–Roch for surfaces) Smooth projective surface $$S$$ 위의 divisor $$D$$에 대해

$$\chi(\mathcal{O}_S(D)) = \frac{1}{2} D \cdot (D - K_S) + \chi(\mathcal{O}_S)$$

이 성립한다. 여기서 $$D \cdot E$$는 두 divisor 사이의 intersection number이고, $$K_S$$는 canonical divisor이며, $$\chi(\mathcal{O}_S) = 1 - q + p_g$$에서 $$q = h^1(S, \mathcal{O}_S)$$는 *irregularity*, $$p_g = h^2(S, \mathcal{O}_S)$$는 *geometric genus*이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Hirzebruch–Riemann–Roch 정리를 적용한다.

$$\chi(\mathcal{O}_S(D)) = \int_S \operatorname{ch}(\mathcal{O}_S(D)) \operatorname{td}(T_S).$$

Chern character $$\operatorname{ch}(\mathcal{O}_S(D)) = 1 + D + \tfrac{1}{2}D^2$$이고, tangent bundle의 Todd class는 $$c_1(T_S) = -K_S$$임에 주의하여

$$\operatorname{td}(T_S) = 1 + \tfrac{1}{2}c_1(T_S) + \tfrac{1}{12}(c_1(T_S)^2 + c_2(T_S)) = 1 - \tfrac{1}{2}K_S + \tfrac{1}{12}(K_S^2 + c_2)$$

이다. 이들의 곱에서 차수 2인 항만 계산하면

$$\tfrac{1}{2}D^2 + D \cdot \left(-\tfrac{1}{2}K_S\right) + \tfrac{1}{12}(K_S^2 + c_2) = \tfrac{1}{2}D \cdot (D - K_S) + \tfrac{1}{12}(K_S^2 + c_2)$$

이다. HRR에서 surface의 적분은 차수 2인 항만 기여하므로, 위에서 계산한 차수 2 성분
$$\tfrac{1}{2}D \cdot (D - K_S) + \tfrac{1}{12}(K_S^2 + c_2)$$
이 곧 $\chi(\mathcal{O}_S(D))$가 되어, 최종적으로

$$\chi(\mathcal{O}_S(D)) = \tfrac{1}{2}D \cdot (D - K_S) + \tfrac{1}{12}(K_S^2 + c_2)$$

을 얻는다. 한편 $$D = 0$$을 대입하면 $$\chi(\mathcal{O}_S) = \tfrac{1}{12}(K_S^2 + c_2)$$이므로 (이것이 바로 Noether 공식이다), 이를 다시 대입하면

$$\chi(\mathcal{O}_S(D)) = \tfrac{1}{2}D \cdot (D - K_S) + \chi(\mathcal{O}_S)$$

이 된다.

</details>

Curve의 경우와 마찬가지로, 만약 $$D$$가 충분히 "양의" 방향이라면 $$h^1$$과 $$h^2$$가 사라져 $$\chi(\mathcal{O}_S(D)) = h^0(S, \mathcal{O}_S(D))$$가 된다. 이는 [§선형계, ⁋정의 9](/ko/math/algebraic_geometry/linear_systems#def9)에서 정의한 ampleness 개념과 밀접하게 관련되어 있다.

<div class="example" markdown="1">

<ins id="ex8">**예시 8**</ins> **$$\mathbb{P}^2$$**: $$K_{\mathbb{P}^2} = -3H$$이고 $$\chi(\mathcal{O}_{\mathbb{P}^2}) = 1$$이다. Divisor $$D = dH$$에 대해 intersection number $$H \cdot H = 1$$을 사용하면

$$\chi(\mathcal{O}_{\mathbb{P}^2}(d)) = \frac{1}{2}dH \cdot (dH + 3H) + 1 = \frac{1}{2}d(d+3) + 1.$$

한편 $$d \ge 0$$에 대해서는 $$h^0 = \binom{d+2}{2}$$이고 $$h^1 = h^2 = 0$$임을 알고 있으므로, $$\chi(\mathcal{O}_{\mathbb{P}^2}(d)) = \binom{d+2}{2} = \frac{(d+1)(d+2)}{2}$$가 되어 위 식과 일치함을 확인할 수 있다.

</div>

<div class="example" markdown="1">

<ins id="ex9">**예시 9**</ins> **Blow-up of $$\mathbb{P}^2$$**: 한 점 $$p$$에서의 blow-up $$\pi: \tilde{\mathbb{P}}^2 \to \mathbb{P}^2$$를 생각하자. Exceptional divisor를 $$E$$라 하면, canonical divisor는 $$K_{\tilde{\mathbb{P}}^2} = \pi^* K_{\mathbb{P}^2} + E = -3H + E$$이다. Divisor $$D = dH - kE$$에 대해 intersection number $$H \cdot H = 1$$, $$H \cdot E = 0$$, $$E \cdot E = -1$$을 사용하여

$$\chi(\mathcal{O}_{\tilde{\mathbb{P}}^2}(dH - kE)) = \frac{1}{2}(dH - kE) \cdot (dH - kE + 3H - E) + 1 = \frac{1}{2}d(d+3) - \frac{1}{2}k(k+1) + 1.$$

</div>

## 응용

### 평면곡선의 Genus 공식

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10**</ins> Degree $$d$$의 smooth plane curve $$C \subset \mathbb{P}^2$$에 대해

$$g(C) = \frac{(d-1)(d-2)}{2}$$

이 성립한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Adjunction formula ([§Canonical Bundle, ⁋명제 10](/ko/math/algebraic_geometry/canonical_bundle#prop10))에 의해 $$K_C = (K_{\mathbb{P}^2} + C)|_C = (d-3)H|_C$$이다. 따라서 $$\deg K_C = d(d-3)$$이고, 이를 $$\deg K_C = 2g - 2$$에 대입하면

$$d(d-3) = 2g - 2 \implies g = \frac{d(d-3) + 2}{2} = \frac{(d-1)(d-2)}{2}$$

을 얻는다.

</details>

이 공식은 평면곡선의 기하학적 성질을 직접적으로 계산해준다. 예를 들어 smooth plane cubic의 genus는 1이므로, 이는 [예시 4](#ex4)에서 다룬 elliptic curve와 같다. 반면 $$d = 1, 2$$인 경우에는 $$g = 0$$으로, 직선과 원뿔곡선이 모두 $$\mathbb{P}^1$$과 birationally equivalent임을 반영한다. ([§유리사상, ⁋명제 10](/ko/math/algebraic_geometry/rational_maps#prop10))

<div class="example" markdown="1">

<ins id="ex11">**예시 11**</ins> Degree $$d$$에 따른 genus의 예시들이다.

- **Degree 3 (cubic)**: $$g = \frac{2 \cdot 1}{2} = 1$$ (elliptic curve).
- **Degree 4 (quartic)**: $$g = \frac{3 \cdot 2}{2} = 3$$.
- **Degree 5 (quintic)**: $$g = \frac{4 \cdot 3}{2} = 6$$.

Genus가 degree에 따라 빠르게 증가하므로, 고차원의 smooth plane curve는 점점 더 복잡한 위상적 구조를 갖는다.

</div>

### Noether 공식

<div class="proposition" markdown="1">

<ins id="prop12">**명제 12**</ins> (Noether Formula) Smooth projective surface $$S$$에 대해

$$K_S^2 + c_2(S) = 12\,\chi(\mathcal{O}_S)$$

이 성립한다. 여기서 $$K_S^2 = K_S \cdot K_S$$는 canonical divisor의 self-intersection number이고, $$c_2(S)$$는 tangent bundle의 top Chern class이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

[명제 7](#prop7)의 증명에서 사용한 Hirzebruch–Riemann–Roch 정리를 $$D = 0$$에 적용한다.

$$\chi(\mathcal{O}_S) = \int_S \operatorname{td}(T_S).$$

Todd class $$\operatorname{td}(T_S) = 1 + \tfrac{1}{2}c_1(T_S) + \tfrac{1}{12}(c_1(T_S)^2 + c_2)$$에서 차수 2인 항만 적분하면 $$c_1(T_S) = -K_S$$이므로 $$c_1(T_S)^2 = K_S^2$$이고

$$\chi(\mathcal{O}_S) = \frac{1}{12}(K_S^2 + c_2)$$

를 얻는다. 따라서 $$K_S^2 + c_2 = 12 \cdot \chi(\mathcal{O}_S)$$이다.

</details>

Noether 공식은 곡면의 세 가지 기본적인 불변량인 canonical self-intersection $$K_S^2$$, topological Euler number $$c_2(S)$$, 그리고 holomorphic Euler characteristic $$\chi(\mathcal{O}_S)$$ 사이의 관계를 제공한다. 이는 곡면의 분류에서 핵심적인 역할을 한다.

<div class="example" markdown="1">

<ins id="ex13">**예시 13**</ins> **$$\mathbb{P}^2$$**: $$K_{\mathbb{P}^2} = -3H$$이므로 $$K_{\mathbb{P}^2}^2 = (-3H)^2 = 9$$이고, $$\chi(\mathcal{O}_{\mathbb{P}^2}) = 1$$이다. Noether 공식에 의해 $$9 + c_2 = 12$$, 즉 $$c_2(\mathbb{P}^2) = 3$$이다. 이는 $$\mathbb{P}^2$$의 topological Euler characteristic이 3이라는 것을 의미하며, 이는 $$\mathbb{P}^2$$의 cell decomposition $$\mathbb{C}^0 \cup \mathbb{C}^1 \cup \mathbb{C}^2$$ (점 + 직선 + 평면)으로부터 $$\chi_{\text{top}} = 1 + 1 + 1 = 3$$로도 확인된다.

</div>

### Brill–Noether 이론

Riemann–Roch 정리의 자연스러운 응용 중 하나는 주어진 곡선 위에서 특정한 성질을 갖는 divisor를 찾는 것이다. 구체적으로, genus $$g$$인 곡선 $$C$$ 위에서 degree $$d$$이고 $$\ell(D) \ge r + 1$$인 divisor $$D$$가 언제 존재하는지를 묻는다. 이 질문에 대한 기본적인 답은 다음과 같다.

<div class="proposition" markdown="1">

<ins id="prop14">**명제 14**</ins> Genus $$g$$인 curve $$C$$ 위의 degree $$d$$인 divisor $$D$$에 대해, $$d \ge r + g$$이면 $$\ell(D) \ge r + 1$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Riemann–Roch에 의해 $$\ell(D) - \ell(K_C - D) = d + 1 - g$$이다. $$\ell(K_C - D) \ge 0$$이므로 $$\ell(D) \ge d + 1 - g$$이다. $$d \ge r + g$$이면 $$\ell(D) \ge r + 1$$을 얻는다.

</details>

이 결과의 역방향, 즉 $$d < r + g$$일 때 어떤 일이 일어나는지를 묻는 것이 Brill–Noether 이론의 본질적인 내용이다. 보다 정밀한 Brill–Noether 정리에 의하면, 일반적인 (general) genus $$g$$ curve에서 $$\ell(D) \ge r + 1$$인 degree $$d$$ divisor들의 parameter space $$W^r_d$$는 *Brill–Noether 수*

$$\rho(g, r, d) = g - (r+1)(g - d + r)$$

가 음이 아닐 때 ($$\rho \ge 0$$) 차원 $$\rho$$인 nonempty variety이고, $$\rho < 0$$이면 빈 집합이다. 이 수치는 $$G^r_d(C)$$ (degree $$d$$, rank $$r$$의 complete linear series들의 parameter space)가 Grassmannian $$\operatorname{Gr}(r+1, h^0(C, \mathcal{O}_C(D)))$$ 위에서 갖는 예상 차원으로부터 산출된다.

<div class="example" markdown="1">

<ins id="ex15">**예시 15**</ins> **$$g = 2$$에서의 Brill–Noether**: $$K_C$$는 degree $$2$$를 갖는다.

- $$d = 2$$, $$r = 1$$: Brill–Noether 수 $$\rho = 2 - (1+1)(2-2+1) = 2 - 2 = 0$$이므로, 일반적인 $$g = 2$$ 곡선에서 $$W^1_2$$는 차원 0, 즉 유한개의 점으로 구성된다. 실제로 $$D = K_C$$가 유일한 $$g^1_2$$인데, 모든 genus 2 곡선은 hyperelliptic curve이므로 canonical divisor에 의해 유일한 degree 2 map $$C \to \mathbb{P}^1$$을 갖는다.
- $$d = 3$$, $$r = 1$$: $$\rho = 2 - (1+1)(2-3+1) = 2 - 0 = 2 > 0$$이므로 $$W^1_3$$은 차원 2의 nonempty variety이다. [명제 14](#prop14)에 의해서도 $$d = 3 \ge r + g = 3$$이므로 $$\ell(D) \ge 2$$가 보장된다. Riemann–Roch에 의해 $$\ell(D) \ge 3 + 1 - 2 = 2$$이다.
- $$d = 0$$, $$r = 0$$: $$\rho = 2 - 1 \cdot 2 = 0$$이고, $$W^0_0 = \{0\}$$ (trivial divisor)로 유일한 점이다.

</div>

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.
**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.
