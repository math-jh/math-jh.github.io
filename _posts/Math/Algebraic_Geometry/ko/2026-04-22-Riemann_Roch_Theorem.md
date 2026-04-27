---
title: "리만-로흐 정리"
excerpt: "The Riemann–Roch theorem for curves"

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/riemann_roch_theorem
sidebar:
    nav: "algebraic_geometry-ko"

header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Riemann_Roch.png
    overlay_filter: 0.5

date: 2026-04-22
last_modified_at: 2026-04-22
weight: 16
published: false
---

우리는 이제 [§선형계, ⁋정의 2](/ko/math/algebraic_geometry/linear_systems#def2)에서 살펴본 line bundle $$\mathcal{L}$$의 complete linear system $$H^0(X, \mathcal{L})$$을 더 자세하게 살펴본다. 이는 linear system을 도입한 직후에 소개해도 되었겠지만, 증명을 위해서는 Serre duality가 필요하여 뒤로 두었다. 

## 리만-로흐 정리

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Smooth projective curve $$C$$ 위의 divisor $$D$$에 대해 *Riemann–Roch dimension*을

$$\ell(D) = \dim H^0(C, \mathcal{O}_C(D))$$

로 정의한다.

</div>

일반적으로 우리는 $$\mathcal{O}_X(D)$$를 $$D$$를 따라 order $$1$$의 pole을 가질 수 있는 rational function들의 sheaf로 생각하므로, 이러한 관점에서 $$H^0(C, \mathcal{O}_XD)$$는 $$X$$ 위에서 정의된 함수들이 이루는 공간이라 생각할 수 있다. 

그럼 Serre duality에 의하여

$$H^1(C, \mathcal{O}_C(D)) \cong H^0(C, \omega_C \otimes \mathcal{O}_C(-D))^\vee = H^0(C, \mathcal{O}_C(K_C - D))^\vee$$

이 성립하는 것은 자명하다. ([§세르 쌍대성, ⁋명제 2](/ko/math/algebraic_geometry/serre_duality#prop2)) 여기서 canonical divisor $$K_C$$는 canonical line bundle에 대응되는 divisor였던 것을 기억하자. 그럼 다음 보조정리에 의해 $$\mathcal{O}_C(D)$$의 Euler characteristic에서 등장하는 항은 단 두 개 뿐임을 유도할 수 있다. 여기서 base field $$\mathbb{K}$$는 infinite field인 것으로 가정한다. 

<div class="proposition" markdown="1">

<ins id="lem2">**보조정리 2**</ins> Smooth projective curve $C$ 위의 임의의 coherent sheaf $\mathcal{F}$에 대해

$$H^i(C, \mathcal{F}) = 0 \quad (i \ge 2)$$

가 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

Embedding $$C\hookrightarrow \mathbb{P}^N$$을 고정하면, dimension count를 통해 $$C\cap H_1\cap H_2=\emptyset$$이도록 하는 hyperplane $$H_1,H_2$$가 존재한다. 따라서 $$U_i=C\setminus H_i$$로 두면 이들은 $$C$$의 affine open cover를 이루는 것을 안다. 

이제 $$\{U_1,U_2\}$$에 대한 Čech cohomology를 생각하자. [§층 코호몰로지, ⁋명제 12](/ko/math/algebraic_geometry/sheaf_cohomology#prop12) 직후에 간략하게 소개했듯, projective variety 위의 임의의 affine open cover는 [§층 코호몰로지, ⁋정리 11](/ko/math/algebraic_geometry/sheaf_cohomology#thm11)의 전제조건을 만족하며 따라서 구하고자 하는 sheaf cohomology는 정확하게 이 affine open cover에 대한 계산으로 귀결된다. 이제 Čech complex가 단순히




그럼 이렇게 embed된 curve $$C$$에 대하여, $$\mathbb{P}^N$$의 적당한 hyperplane $$H_1, H_2$$가 존재하여 $$C\cap H_1\cap H_2=\emptyset$$이도록 할 수 있음은 차원을 생각하면 자명하다. 

</details>

여기서 

<details class="proof--alone" markdown="1">
<summary>증명</summary>

$$C$$는 projective variety이므로 $$\mathbb{P}^n$$에 임베드할 수 있다. 초평면 $$H_1 \subset \mathbb{P}^n$$을 택하면 $$C \setminus H_1$$은 affine variety이다(프로젝티브 variety에서 hyperplane section을 제거하면 affine). 한편 $$C \cap H_1$$은 curve와 hyperplane의 교차이므로 유한개의 점 $$P_1, \ldots, P_m$$으로 구성된다. $$k$$가 무한체이므로 이 점들을 모두 피하는 초평면 $$H_2$$를 택할 수 있으며, 그러면 $$C \setminus H_2$$도 affine이고 $$C = (C \setminus H_1) \cup (C \setminus H_2)$$가 된다.

$$C$$는 separated이므로 $$(C \setminus H_1) \cap (C \setminus H_2) = C \setminus (H_1 \cup H_2)$$도 affine이다. Serre's criterion에 의해 affine 위의 quasi-coherent sheaf의 higher cohomology는 소멸하므로 ([§층 코호몰로지, ⁋명제 12](/ko/math/algebraic_geometry/sheaf_cohomology#prop12)),  (Leray 정리)의 전제조건이 충족되어 $$\check{H}^i(\mathcal{U}, \mathcal{F}) \cong H^i(C, \mathcal{F})$$ ($$i \ge 0$$)가 성립한다. 한편 $$\mathcal{U} = \{C \setminus H_1, C \setminus H_2\}$$는 두 개의 open으로 구성되어 있으므로 Čech complex는 degree $$1$$에서 끝나, $$\check{H}^i(\mathcal{U}, \mathcal{F}) = 0$$ ($$i \ge 2$$)이 자명하다. 따라서 $$H^i(C, \mathcal{F}) = 0$$ ($$i \ge 2$$)를 얻는다.

</details>

이 결과에 의해 임의의 divisor $$D$$에 대해

$$\chi(\mathcal{O}_C(D)) = h^0(C, \mathcal{O}_C(D)) - h^1(C, \mathcal{O}_C(D))$$

가 성립한다.

이제 다음 명제를 증명한다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> (Riemann–Roch for curves) Smooth projective curve $$C$$ 위의 divisor $$D$$에 대해

$$\ell(D) - \ell(K_C - D) = \deg D + 1 - g$$

이 성립한다. 여기서 $$g$$는 $$C$$의 genus, $$K_C$$는 canonical divisor이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Smooth projective curve $$C$$에 대해 Serre duality 에 의하여

$$H^1(C, \mathcal{O}_C(D)) \cong H^0(C, \omega_C \otimes \mathcal{O}_C(-D))^\vee = H^0(C, \mathcal{O}_C(K_C - D))^\vee$$

이 성립한다. 따라서 $$h^1(C, \mathcal{O}_C(D)) = h^0(C, \mathcal{O}_C(K_C - D)) = \ell(K_C - D)$$이고, Euler characteristic의 정의에 의해

$$\chi(\mathcal{O}_C(D)) = h^0(C, \mathcal{O}_C(D)) - h^1(C, \mathcal{O}_C(D)) = \ell(D) - \ell(K_C - D)$$

이다. 한편 effective divisor $$D$$에 대해 short exact sequence $$0 \to \mathcal{O}_C \to \mathcal{O}_C(D) \to \mathcal{O}_D \to 0$$이 존재하며, Euler characteristic의 additivity에 의해 $$\chi(\mathcal{O}_C(D)) = \chi(\mathcal{O}_C) + \chi(\mathcal{O}_D)$$이다. 여기서 $$\mathcal{O}_D$$는 차수 $$\deg D$$의 skyscraper sheaf이므로 $$\chi(\mathcal{O}_D) = \deg D$$이고, $$\chi(\mathcal{O}_C) = h^0(\mathcal{O}_C) - h^1(\mathcal{O}_C) = 1 - g$$이다 (genus의 정의에 의해 $$g = h^1(C, \mathcal{O}_C)$$). 따라서 $$\chi(\mathcal{O}_C(D)) = \deg D + 1 - g$$이고, 이를 앞선 식과 결합하면 원하는 결과를 얻는다. 일반적인 (effective가 아닌) divisor에 대해서는 $$D$$를 effective divisor $$D'$$과의 차이로 표현한 후 동일한 additivity 논증을 적용한다.

</details>

Riemann–Roch 정리의 핵심적인 유용성은 다음과 같은 상황에서 드러난다. 만약 $$\deg D > 2g - 2$$, 즉 $$\deg(K_C - D) < 0$$이라면 $$K_C - D$$는 음수 차수를 갖고, 따라서 $$K_C - D$$는 effective divisor와 linearly equivalent할 수 없으므로 $$\ell(K_C - D) = 0$$이 되어, 식이 $$\ell(D) = \deg D + 1 - g$$로 단순화된다. 따라서 충분히 큰 degree의 divisor에 대해서는 $$\ell(D)$$를 직접적으로 계산할 수 있다. 반면 작은 degree에서는 $$\ell(K_C - D)$$ 항이 남아 정밀한 정보를 제공하는데, 이 항이 바로 canonical divisor $$K_C$$의 기하학적 의미이다.

<div class="example" markdown="1">

<ins id="ex4">**예시 4**</ins> **$$\mathbb{P}^1$$**: $$\mathbb{P}^1$$의 genus는 $$g = 0$$이고, canonical divisor는 $$K_{\mathbb{P}^1} = -2H$$이다 ([§표준선다발, ⁋예시 8](/ko/math/algebraic_geometry/canonical_bundle#ex8)). ([§선다발과 벡터다발, ⁋예시 12](/ko/math/algebraic_geometry/line_bundles#ex12))에서 $$\mathcal{O}_{\mathbb{P}^1}(d)$$의 global section이 차수 $$d$$의 동차다항식들임을 보였으므로,

$$\ell(dH) = d+1 \quad (d \ge 0), \qquad \ell(dH) = 0 \quad (d < 0).$$

Riemann–Roch 식을 확인해보면, $$D = dH$$에 대해 $$\deg D = d$$이고 $$K_C - D = (-2-d)H$$이므로

$$\ell(dH) - \ell(-2H-dH) = d + 1 - 0 = d + 1$$

이 되어 양변이 모두 $$d+1$$로 일치함을 확인할 수 있다.

</div>

<div class="example" markdown="1">

<ins id="ex5">**예시 5**</ins> **Genus 1 curve (elliptic curve)**: $$g = 1$$이므로 $$\deg K_C = 2g - 2 = 0$$이다. Riemann–Roch에서 $$D = 0$$을 대입하면 $$\ell(0) - \ell(K_C) = 0 + 1 - 1 = 0$$, 즉 $$\ell(K_C) = \ell(0) = 1$$이다. Degree가 0이고 $$\ell(K_C) = 1$$인 divisor는 반드시 trivial, 즉 $$K_C \sim 0$$이다. 따라서 Riemann–Roch 식은

$$\ell(D) - \ell(-D) = \deg D$$

이 된다. 특히 $$\deg D > 0$$이면 $$\ell(-D) = 0$$이므로 $$\ell(D) = \deg D$$이다. 또 $$\deg D = 0$$이면 $$\ell(D) = 1$$ 또는 $$0$$인데, $$D \sim 0$$인 경우에만 $$\ell(D) = 1$$이다.

</div>

<div class="example" markdown="1">

<ins id="ex6">**예시 6**</ins> **Genus 2 curve**: $$g = 2$$이면 $$\deg K_C = 2g - 2 = 2$$이다. Canonical divisor $$K_C$$는 두 점의 linear equivalence class이다. 일반적인 점 $$p$$에 대해 $$D = d \cdot p$$라고 하자.

$$d = 0$$이면 $$\ell(0) = 1$$로 상수함수만이 global section이다. $$d = 1$$의 경우, $$\ell(p) \ge 2$$라면 degree 1 사상 $$C \to \mathbb{P}^1$$이 존재하여 $$C \cong \mathbb{P}^1$$이 되지만 $$g = 2$$와 모순이므로 $$\ell(p) = 1$$이다. Riemann–Roch에 의해 $$\ell(p) - \ell(K_C - p) = 1 + 1 - 2 = 0$$이므로 $$\ell(K_C - p) = 1$$이다.

$$d = 2$$의 경우가 더 흥미롭다. 만약 $$2p \sim K_C$$이면 $$\ell(K_C - 2p) = \ell(0) = 1$$이므로 $$\ell(2p) - 1 = 2 + 1 - 2 = 1$$, 즉 $$\ell(2p) = 2$$이다. 이 경우 $$p$$를 *Weierstrass point*라 부른다. 일반적인 점에서는 $$2p \not\sim K_C$$이므로 $$\ell(K_C - 2p) = 0$$이고 $$\ell(2p) = 1$$이다. 마지막으로 $$d \ge 3$$이면 $$\deg(K_C - D) = 2 - d < 0$$이므로 $$\ell(K_C - D) = 0$$이고, 따라서 $$\ell(D) = d - 1$$이다.

</div>

지금까지 곡선에서의 Riemann–Roch 정리와 몇 가지 구체적인 예시를 살펴보았다. 이제 이 정리의 응용들을 다룬다.

## 응용

### 평면곡선의 Genus 공식

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> Degree $$d$$의 smooth plane curve $$C \subset \mathbb{P}^2$$에 대해

$$g(C) = \frac{(d-1)(d-2)}{2}$$

이 성립한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Adjunction formula ([§표준선다발, ⁋명제 9](/ko/math/algebraic_geometry/canonical_bundle#prop9))에 의해 $$K_C = (K_{\mathbb{P}^2} + C)\vert_C = (d-3)H\vert_C$$이다. 따라서 $$\deg K_C = d(d-3)$$이고, 이를 $$\deg K_C = 2g - 2$$에 대입하면

$$d(d-3) = 2g - 2 \implies g = \frac{d(d-3) + 2}{2} = \frac{(d-1)(d-2)}{2}$$

을 얻는다.

</details>

이 공식은 평면곡선의 기하학적 성질을 직접적으로 계산해준다. 예를 들어 smooth plane cubic의 genus는 1이므로, 이는 [예시 4](#ex4)에서 다룬 elliptic curve와 같다. 반면 $$d = 1, 2$$인 경우에는 $$g = 0$$으로, 직선과 원뿔곡선이 모두 $$\mathbb{P}^1$$과 birationally equivalent임을 반영한다 ([§유리사상, ⁋명제 10](/ko/math/algebraic_geometry/rational_maps#prop10)).

<div class="example" markdown="1">

<ins id="ex8">**예시 8**</ins> Degree $$d$$에 따른 genus를 계산해보면, degree 3 (cubic)의 경우 $$g = \frac{2 \cdot 1}{2} = 1$$로 elliptic curve이고, degree 4 (quartic)의 경우 $$g = \frac{3 \cdot 2}{2} = 3$$, degree 5 (quintic)의 경우 $$g = \frac{4 \cdot 3}{2} = 6$$이다. Genus가 degree에 따라 빠르게 증가하므로, 고차원의 smooth plane curve는 점점 더 복잡한 위상적 구조를 갖는다.

</div>

### Brill–Noether 이론

Riemann–Roch 정리의 자연스러운 응용 중 하나는 주어진 곡선 위에서 특정한 성질을 갖는 divisor를 찾는 것이다. 구체적으로, genus $$g$$인 곡선 $$C$$ 위에서 degree $$d$$이고 $$\ell(D) \ge r + 1$$인 divisor $$D$$가 언제 존재하는지를 묻는다. 이 질문에 대한 기본적인 답은 다음과 같다.

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> Genus $$g$$인 curve $$C$$ 위의 degree $$d$$인 divisor $$D$$에 대해, $$d \ge r + g$$이면 $$\ell(D) \ge r + 1$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Riemann–Roch에 의해 $$\ell(D) - \ell(K_C - D) = d + 1 - g$$이다. $$\ell(K_C - D) \ge 0$$이므로 $$\ell(D) \ge d + 1 - g$$이다. $$d \ge r + g$$이면 $$\ell(D) \ge r + 1$$을 얻는다.

</details>

이 결과의 역방향, 즉 $$d < r + g$$일 때 어떤 일이 일어나는지를 묻는 것이 Brill–Noether 이론의 본질적인 내용이다. 보다 정밀한 Brill–Noether 정리에 의하면, 일반적인 (general) genus $$g$$ curve에서 $$\ell(D) \ge r + 1$$인 degree $$d$$ divisor들의 parameter space $$W^r_d$$는 *Brill–Noether 수*

$$\rho(g, r, d) = g - (r+1)(g - d + r)$$

가 음이 아닐 때 ($$\rho \ge 0$$) 차원 $$\rho$$인 nonempty variety이고, $$\rho < 0$$이면 빈 집합이다. 이 수치는 $$G^r_d(C)$$ (degree $$d$$, rank $$r$$의 complete linear series들의 parameter space)가 Grassmannian $$\operatorname{Gr}(r+1, h^0(C, \mathcal{O}_C(D)))$$ 위에서 갖는 예상 차원으로부터 산출된다.

<div class="example" markdown="1">

<ins id="ex10">**예시 10**</ins> **$$g = 2$$에서의 Brill–Noether**: $$K_C$$는 degree $$2$$를 갖는다. $$d = 2$$, $$r = 1$$의 경우 Brill–Noether 수 $$\rho = 2 - (1+1)(2-2+1) = 2 - 2 = 0$$이므로, 일반적인 $$g = 2$$ 곡선에서 $$W^1_2$$는 차원 0, 즉 유한개의 점으로 구성된다. 실제로 $$D = K_C$$가 유일한 $$g^1_2$$인데, 모든 genus 2 곡선은 hyperelliptic curve이므로 canonical divisor에 의해 유일한 degree 2 map $$C \to \mathbb{P}^1$$을 갖는다.

$$d = 3$$, $$r = 1$$의 경우 $$\rho = 2 - (1+1)(2-3+1) = 2 - 0 = 2 > 0$$이므로 $$W^1_3$$은 차원 2의 nonempty variety이다. [명제 8](#prop8)에 의해서도 $$d = 3 \ge r + g = 3$$이므로 $$\ell(D) \ge 2$$가 보장된다. Riemann–Roch에 의해 $$\ell(D) \ge 3 + 1 - 2 = 2$$이다.

$$d = 0$$, $$r = 0$$의 경우 $$\rho = 2 - 1 \cdot 2 = 0$$이고, $$W^0_0 = \{0\}$$로 trivial divisor가 유일한 점이다.

</div>





## Smooth Curve의 Canonical Bundle

[명제 6](#prop6)의 degree-genus formula는 Riemann–Roch theorem의 특수한 경우이다. Curve의 차원이 1이므로 $$\omega_C = \Omega_C^1$$이며, $$\omega_C$$의 global section은 $$C$$ 위의 *regular 1-form*이다. Adjunction formula ([§표준선다발, ⁋명제 9](/ko/math/algebraic_geometry/canonical_bundle#prop9))에 의해 $$\mathbb{P}^2$$ 안의 degree $$d$$ smooth plane curve $$C$$에 대해 $$\omega_C \cong \mathcal{O}_C(d-3)$$이 된다. 따라서 $$\deg K_C = d(d-3)$$이고, [명제 6](#prop6)의 genus 공식 $$g = (d-1)(d-2)/2$$을 대입하면 $$\deg K_C = 2g - 2$$를 얻는다. 이 결과는 임의의 smooth projective curve에 대해 성립한다.

<div class="proposition" markdown="1">

<ins id="prop11">**명제 11**</ins> Smooth projective curve $$C$$의 genus가 $$g$$이면 $$\deg K_C = 2g - 2$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Riemann–Roch theorem에 의해, 임의의 divisor $$D$$에 대해 $$\ell(D) - \ell(K_C - D) = \deg D + 1 - g$$가 성립한다. $$D = 0$$을 대입하면 $$\ell(0) - \ell(K_C) = 1 - g$$이고, $$\ell(0) = 1$$, $$\ell(K_C) = h^0(C, \omega_C) = g$$이므로 자동으로 성립한다. $$D = K_C$$를 대입하면 $$\ell(K_C) - \ell(0) = \deg K_C + 1 - g$$, 즉 $$g - 1 = \deg K_C + 1 - g$$로부터 $$\deg K_C = 2g - 2$$를 얻는다.

</details>

### Genus에 따른 분류

Canonical divisor의 degree는 curve의 genus에 따라 본질적으로 다른 거동을 보인다. $$g = 0$$, 즉 $$C \cong \mathbb{P}^1$$의 경우, $$\deg K_C = -2 < 0$$이므로 $$K_C$$는 ample이 아니다. 사실 $$K_{\mathbb{P}^1} = -2P$$이므로 $$K_C$$는 negative degree를 갖는다. $$g = 1$$, 즉 *elliptic curve*의 경우를 살펴보기 전에, 이 용어를 정의하자. Genus 1인 smooth projective curve를 *elliptic curve<sub>타원곡선</sub>*라 부른다. (엄밀하게는 하나의 기준점이 선택된 genus 1 curve를 elliptic curve라 하지만, 여기서는 이 구분을 중요하게 다루지 않는다.) 이 경우 $$\deg K_C = 0$$이며 실제로 $$K_C \sim 0$$이므로 $$\omega_C \cong \mathcal{O}_C$$가 trivial하다. 따라서 $$K_C$$ 역시 ample이 아니다. $$g \ge 2$$의 경우, $$\deg K_C = 2g - 2 > 0$$이다. Curve에서 $$\deg \mathcal{L} > 0$$인 line bundle $$\mathcal{L}$$은 항상 ample이다. Riemann–Roch theorem에 의해 $$\dim H^0(C, \mathcal{L}^{\otimes m}) = m \cdot \deg \mathcal{L} - g + 1$$ ($$m$$가 충분히 클 때)이며, 이는 충분히 큰 $$m$$에 대해 $$\mathcal{L}^{\otimes m}$$이 very ample section들을 충분히 많이 가짐을 의미하므로 ([§선형계, ⁋정의 10](/ko/math/algebraic_geometry/linear_systems#def10)), $$K_C$$는 ample이다.

### Hyperelliptic Curve에서의 Canonical Bundle

Genus $$g \ge 2$$인 curve 중 $$\mathbb{P}^1$$로의 degree 2 covering이 존재하는 것을 *hyperelliptic curve<sub>초타원곡선</sub>*라 부른다. 구체적으로, $$C$$는 $$y^2 = f(\x)$$ ($$f$$는 서로 다른 근을 갖는 degree $$2g + 1$$ 또는 $$2g + 2$$ 다항식)에 의해 주어진 affine curve의 smooth completion으로 나타낼 수 있다. 주의할 점은, genus 0인 $$\mathbb{P}^1$$과 genus 1인 elliptic curve 역시 $$\mathbb{P}^1$$에 대한 degree 2 covering을 갖지만, 이들은 관례적으로 hyperelliptic curve에서 제외한다는 것이다.

이러한 $$C$$에서 canonical bundle $$K_C$$의 complete linear system $$\lvert K_C\rvert$$가 정의하는 morphism $$\varphi_{K_C} : C \rightarrow \mathbb{P}^{g-1}$$의 거동을 살펴보자. $$\deg K_C = 2g - 2$$이고 $$h^0(K_C) = g$$이므로, $$\varphi_{K_C}$$의 공역은 $$\mathbb{P}^{g-1}$$이다. 그러나 실제로 $$\varphi_{K_C}$$는 본래의 hyperelliptic double cover $$C \rightarrow \mathbb{P}^1$$로 분해되며, 2:1 covering map이 되므로 closed embedding이 아니다. 즉, $$\varphi_{K_C}$$의 image는 $$\mathbb{P}^{g-1}$$ 안의 $$\mathbb{P}^1$$로, Veronese embedding $$\mathbb{P}^1 \hookrightarrow \mathbb{P}^{g-1}$$의 image에 들어간다. 이에 대한 증명은 [Har, IV.5.2]를 참조한다.

따라서 $$K_C$$는 ample이지만 very ample이 아닌 line bundle의 구체적인 예시를 제공한다. 이는 [§선형계, ⁋정의 10](/ko/math/algebraic_geometry/linear_systems#def10)에서 언급되었던 "ample but not very ample" 현상의 실현이다. Curve에서 $$\mathcal{L}$$이 very ample이기 위한 충분조건이 $$\deg \mathcal{L} \ge 2g + 1$$임이 알려져 있으며 ([Har, IV.3.2]), $$\deg K_C = 2g - 2 < 2g + 1$$이므로 이 조건을 만족하지 못함도 확인할 수 있다. 대신 $$K_C$$의 적절한 거듭제곱이 very ample이 됨을 확인할 수 있다. $$g \ge 3$$이면 $$\deg K_C^{\otimes 2} = 4g - 4 \ge 2g + 1$$이 성립하므로 $$K_C^{\otimes 2}$$는 very ample이다. $$g = 2$$이면 $$\deg K_C^{\otimes 2} = 4 < 5 = 2g + 1$$이지만, $$\deg K_C^{\otimes 3} = 3(2g - 2) = 6 > 5 = 2g + 1$$이므로 $$K_C^{\otimes 3}$$가 very ample이다. 어느 경우에도 $$K_C$$의 어떤 거듭제곱이 very ample이 되므로, ample의 정의—어떤 거듭제곱이 very ample이면 ample—와 완벽하게 부합한다.

이와 대조적으로, $$g \ge 3$$인 non-hyperelliptic curve에서는 canonical map $$\varphi_{K_C} : C \rightarrow \mathbb{P}^{g-1}$$가 closed embedding이 되어, $$K_C$$ 자체가 very ample이다 ([Har, IV.5.4]).


---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.
**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.