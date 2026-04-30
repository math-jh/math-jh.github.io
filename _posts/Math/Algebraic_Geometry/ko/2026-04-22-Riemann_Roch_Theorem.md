---
title: "곡선에서의 리만-로흐 정리"
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

일반적으로 우리는 $$\mathcal{O}_X(D)$$를 $$D$$를 따라 order $$1$$의 pole을 가질 수 있는 rational function들의 sheaf로 생각하므로, 이러한 관점에서 $$H^0(C, \mathcal{O}_C(D))$$는 $$X$$ 위에서 정의된 함수들이 이루는 공간이라 생각할 수 있다. 

그럼 Serre duality에 의하여

$$H^1(C, \mathcal{O}_C(D)) \cong H^0(C, \omega_C \otimes \mathcal{O}_C(-D))^\vee = H^0(C, \mathcal{O}_C(K_C - D))^\vee$$

이 성립하는 것은 자명하다. ([§세르 쌍대성, ⁋명제 2](/ko/math/algebraic_geometry/serre_duality#prop2)) 여기서 canonical divisor $$K_C$$는 canonical line bundle에 대응되는 divisor였던 것을 기억하자. 그럼 다음 보조정리에 의해 $$\mathcal{O}_C(D)$$의 Euler characteristic에서 등장하는 항은 단 두 개 뿐임을 유도할 수 있다. 여기서 base field $$\mathbb{K}$$는 infinite field인 것으로 가정한다. 

<div class="proposition" markdown="1">

<ins id="lem2">**보조정리 2**</ins> Smooth projective curve $$C$$ 위의 임의의 coherent sheaf $$\mathcal{F}$$에 대해

$$H^i(C, \mathcal{F}) = 0 \quad (i \ge 2)$$

가 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

Embedding $$C\hookrightarrow \mathbb{P}^N$$을 고정하면, dimension count를 통해 $$C\cap H_1\cap H_2=\emptyset$$이도록 하는 hyperplane $$H_1,H_2$$가 존재한다. 따라서 $$U_i=C\setminus H_i$$로 두면 이들은 $$C$$의 affine open cover를 이루는 것을 안다. 

이제 $$\{U_1,U_2\}$$에 대한 Čech cohomology를 생각하자. [§층 코호몰로지, ⁋명제 12](/ko/math/algebraic_geometry/sheaf_cohomology#prop12) 직후에 간략하게 소개했듯, projective variety 위의 임의의 affine open cover는 [§층 코호몰로지, ⁋정리 11](/ko/math/algebraic_geometry/sheaf_cohomology#thm11)의 전제조건을 만족하며 따라서 구하고자 하는 sheaf cohomology는 정확하게 이 affine open cover에 대한 계산으로 귀결된다. 이제 Čech complex가 단순히

$$\check{C}(\mathcal{U}, \mathcal{F}):\qquad \mathcal{F}(U)\oplus \mathcal{F}(V)\rightarrow \mathcal{F}(U\cap V)\rightarrow 0$$

으로 끝나므로 원하는 보조정리는 자명하다. 

</details>

따라서, 이 결과에 의해 임의의 divisor $$D$$에 대해

$$\chi(\mathcal{O}_C(D)) = h^0(C, \mathcal{O}_C(D)) - h^1(C, \mathcal{O}_C(D))\tag{$\ast$}$$

가 성립한다. 여기서 $$h^i$$는 $$H^i$$의 dimension에 대한 shorthand notation이다.

한편, 우리는 위상수학적 관점에서 genus $$g$$ compact Riemann surface $$S$$의 Euler characteristic은

$$\chi(S)=2(1-g)$$

로 주어진다는 사실을 잘 알고 있다. 이 때 Euler characteristic은 triangulation을 사용하여 꼭짓점 수 $$V$$, 모서리 수 $$E$$, 면 수 $$F$$를 사용하여 $$V-E+F$$로 생각할 수도 있고[^1], 혹은 Gauss-Bonnet 정리 등의 미분기하적 도구를 사용하여 정의된 것으로 생각해도 된다. 

대수기하학에서 우리는 보편적으로 underlying field $$\mathbb{K}$$가 복소수인 것으로 생각하므로, 위에서의 genus $$g$$ compact Riemann surface는 대수기하 관점에서는 1차원 곡선 $$C_S$$에 불과하다. 이 때, 대수기하적 관점에서의 Euler characteristic은 따라서 위의 식 ($$\ast$$)에 $$D=0$$을 대입한

$$\chi(\mathcal{O}_{C_S})=h^0(C_S, \mathcal{O}_{C_S})-h^1(C_S, \mathcal{O}_{C_S})$$

으로 주어진다. 한편, 위상수학에서 $$1$$차원 구멍이 $$H^1$$을 통해 나타나듯 대수기하에서의 1차원 구멍, 즉 위상수학 관점에서의 2차원 구멍인 genus는 $$g=h^1(C_S, \mathcal{O}_{C_S})$$로 정의되며, global section은 상수함수 뿐이므로 $$C_S$$의 Euler characteristic은

$$\chi(\mathcal{O}_{C_S})=h^0(C_S, \mathcal{O}_{C_S})-h^1(C_S, \mathcal{O}_{C_S})=1-g$$

로 나타난다. 이 값이 위상수학적인 Euler characteristic의 절반이라는 것은 우연이 아니며, Hodge theory를 통해 확인할 수 있지만 이것은 우리의 목표와는 무관하므로 우선은 넘기기로 한다. 중요한 것은 대수기하에서의 Euler characteristic과, 이를 curve에서 계산했을 때의 값이 $$1-g$$가 나오는 것이 뜬금없는 것이 아니라 위상수학에서의 결과를 재해석하는 것이라는 것이다. 

이번 글의 주제인 Riemann-Roch 정리는 여기에 한 가지의 작업을 추가한다. 위의 계산은 아무것도 붙이지 않은 trivial sheaf $$\mathcal{O}_{C_S}$$에 대한 것이므로, 이를 임의의 divisor $$D$$를 사용하여 twist한 sheaf $$\mathcal{O}_{C_S}(D)$$를 생각하는 것이다. 그럼 이 때의 보정항이 $$\deg D$$만큼 생긴다는 것이 Riemann-Roch 정리의 결과이다. 

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> (Riemann–Roch for curves) Smooth projective curve $$C$$ 위의 divisor $$D$$에 대해

$$\ell(D) - \ell(K_C - D) = \deg D + 1 - g$$

이 성립한다. 여기서 $$g$$는 $$C$$의 genus, $$K_C$$는 canonical divisor이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

위의 계산들과 정의들에 의하여

$$\chi(\mathcal{O}_C(D)) = h^0(C, \mathcal{O}_C(D)) - h^1(C, \mathcal{O}_C(D)) = \ell(D) - \ell(K_C - D)$$

인 것은 자명하다. 한편, effective divisor $$D$$에 대해 short exact sequence 

$$0 \to \mathcal{O}_C \to \mathcal{O}_C(D) \to \mathcal{O}_D \to 0$$

이 존재하며, 그럼 Euler characteristic의 additivity에 의해 $$\chi(\mathcal{O}_C(D)) = \chi(\mathcal{O}_C) + \chi(\mathcal{O}_D)$$이다. 

여기서 $$\mathcal{O}_D$$는 차수 $$\deg D$$의 skyscraper sheaf이므로 $$\chi(\mathcal{O}_D) = \deg D$$이고, 위에서 살펴본 것과 같이 $$\chi(\mathcal{O}_C)=1-g$$이므로 이를 앞선 식과 결합하면 원하는 결과를 얻는다. 일반적인 (effective가 아닌) divisor에 대해서는 $$D$$를 effective divisor $$D'$$과의 차이로 표현한 후 동일한 additivity 논증을 적용하면 된다. 

</details>

이제 이 정리의 기하학적 의미를 살펴보기 위해 등식을 항별로 읽어보자. 우선 정의에 의해 

$$\ell(D) = \dim H^0(C, \mathcal{O}_C(D))$$

이며, 이 때 우변의 공간 $$H^0(C, \mathcal{O}_C(D))$$는 기하적으로 

$$\divisor(f)+d\geq 0$$

을 만족하는 meromorphic function들의 모임이다. 

Riemann–Roch 정리의 의미를 $$\ell(D) - \ell(K_C - D) = \deg D + 1 - g$$의 각 항에 대해 기하학적으로 읽어보자. $$\ell(D) = \dim H^0(C, \mathcal{O}_C(D))$$의 global section은 $$\operatorname{div}(f) + D \ge 0$$을 만족하는 meromorphic 함수 $$f$$이므로, $$D$$가 함수의 pole 위치와 최대 차수를 지정하는 셈이다. 따라서 $$\deg D$$가 커질수록 $$\ell(D)$$도 커져야 하며 자명한 부등식 $$\ell(D) \le \deg D + 1$$이 성립한다 ([§선형계, ⁋명제 5](/ko/math/algebraic_geometry/linear_systems#prop5)). 한편 Serre duality에 의해 $$\ell(K_C - D) = \dim H^1(C, \mathcal{O}_C(D))^\vee$$이므로, 이 항은 $$\ell(D)$$가 자명한 한계로부터 얼마나 끌어내려지는지를 측정하는 수정항이다. 기하학적으로는 "$$D$$의 모든 점에서 영점을 갖는 regular differential form"의 공간이며, $$D$$의 위치에 따라 이 차원이 달라진다.

큰 degree, 즉 $$\deg D > 2g - 2$$인 경우 $$\deg(K_C - D) < 0$$이 되어 $$\ell(K_C - D) = 0$$이고 $$\ell(D) = \deg D + 1 - g$$로 단순화된다. 자명한 한계와 정확히 $$g$$만큼 차이가 나는데, 이 결손이 바로 curve의 위상수학적 복잡도(genus)가 함수론에 새기는 흔적이다. $$\mathbb{P}^1$$ ($$g = 0$$)에서는 결손이 없어 등호가 성립하지만, genus가 커질수록 같은 degree의 divisor가 만드는 함수공간이 그만큼 좁아진다.

반면 $$\deg D \le 2g - 2$$인 영역에서는 $$\ell(K_C - D)$$가 $$D$$의 위치—$$D$$가 어떤 점들로 이루어졌는지—에 민감하게 의존한다. 같은 degree라도 $$D$$의 점들이 canonical class와 어떤 관계에 있느냐에 따라 $$\ell(D)$$가 달라지며, 이는 *special divisor*의 현상으로 [응용 섹션의 Brill–Noether theory](#brill-noether)에서 본격적으로 다룬다. Canonical divisor $$K_C$$ 자체에 대해서는 $$\ell(K_C) = h^0(C, \omega_C) = g$$인데, 이는 genus의 미분기하학적 정의—독립적인 global regular 1-form의 개수—와 정확히 일치한다. 정리의 우변 $$\deg D + 1 - g$$도 "$$D$$가 자명하게 기여하는 자유도 ($$\deg D$$)" 더하기 "구조층의 Euler characteristic ($$\chi(\mathcal{O}_C) = 1 - g$$)"이라는 두 부분의 합으로 읽을 수 있다.

정리하면, $$\ell(D)$$는 $$D$$의 complete linear system의 차원, $$\ell(K_C - D)$$는 $$K_C$$가 $$D$$ 위에 부과하는 수정항이며, 큰 degree에서는 이 수정항이 사라지고 작은 degree에서는 $$K_C$$의 기하학적 정보를 반영한다.

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

**Degree-genus formula**

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

**Brill–Noether theory**

Riemann–Roch 정리가 divisor의 complete linear system $$\lvert D\rvert$$의 차원을 계산하는 공식임을 생각하면, 자연스러운 다음 질문이 떠오른다. 주어진 곡선 $$C$$ (genus $$g$$) 위에서, degree $$d$$이고 차원이 $$r$$ 이상인 linear system을 갖는 divisor가 존재하는가? 그리고 그런 divisor들이 이루는 공간은 어떤 기하학적 구조를 갖는가? 이것이 Brill–Noether 이론의 출발점이다.

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

$$d = 3$$, $$r = 1$$의 경우 $$\rho = 2 - (1+1)(2-3+1) = 2 - 0 = 2 > 0$$이므로 $$W^1_3$$은 차원 2의 nonempty variety이다. [명제 9](#prop9)에 의해서도 $$d = 3 \ge r + g = 3$$이므로 $$\ell(D) \ge 2$$가 보장된다. Riemann–Roch에 의해 $$\ell(D) \ge 3 + 1 - 2 = 2$$이다.

$$d = 0$$, $$r = 0$$의 경우 $$\rho = 2 - 1 \cdot 2 = 0$$이고, $$W^0_0 = \{0\}$$로 trivial divisor가 유일한 점이다.

</div>

### Canonical Divisor의 Degree와 Genus

Riemann–Roch 정리에서 $$D = K_C$$를 대입하면 $$\ell(K_C) - \ell(0) = \deg K_C + 1 - g$$를 얻는다. $$\ell(0) = 1$$이고 $$\ell(K_C) = h^0(C, \omega_C) = g$$이므로, $$\deg K_C = 2g - 2$$라는 기본적인 관계式이 따라 나온다. 이 결과는 degree-genus formula ([명제 7](#prop7))의 증명에서도 이미 사용되었음을 기억하자.

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

---

[^1]: 이것은 cohomology의 alternating sum으로서 Euler characteristic을 정의하는 것과 맞아떨어진다. 