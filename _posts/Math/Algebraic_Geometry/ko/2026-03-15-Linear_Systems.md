---
title: "Linear Systems"
excerpt: "Complete linear systems, base loci, and ampleness"

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/linear_systems
sidebar:
    nav: "algebraic_geometry-ko"

header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Linear_Systems.png
    overlay_filter: 0.5

date: 2026-03-15
last_modified_at: 2026-03-15
weight: 12

---

[§Divisors](/ko/math/algebraic_geometry/divisors)에서 우리는 divisor의 개념을, [§Line Bundles](/ko/math/algebraic_geometry/line_bundles)에서 line bundle과 global sections $$H^0(X, \mathcal{L})$$의 개념을, [§Picard Group](/ko/math/algebraic_geometry/picard_group)에서 $$\operatorname{Pic}(X) \cong \operatorname{Cl}(X)$$의 대응을 각각 다루었다. 이제 *linear system*을 정의한다. Linear system은 주어진 line bundle의 global section들이 이루는 family를 체계적으로 조직화하는 방법이다. 이를 통해 우리는 *동일한 line bundle class*에 속하는 effective divisor들의 모임을 projective space로 parameterize할 수 있으며, basepoint-free linear system은 다양체에서 사영공간으로의 사상을 자연스럽게 정의한다. 또한 very ample line bundle을 판별하는 실용적 기준을 제공하며, Riemann-Roch 정리의 주된 응용 대상이 된다.

## Complete Linear System의 정의

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 다양체 $$X$$ 위의 line bundle $$\mathcal{L}$$에 대하여, $$\mathcal{L}$$의 *complete linear system*은 $$\mathcal{L}$$의 global section space $$H^0(X, \mathcal{L})$$의 projectivization이다.

$$\lvert \mathcal{L} \rvert = \mathbb{P}(H^0(X, \mathcal{L}))$$

이는 유효한 점을 갖는 모든 nonzero section의 등가류들의 집합이다. $$\dim H^0(X, \mathcal{L}) = r + 1$$이면, $$\lvert \mathcal{L} \rvert$$는 차원 $$r$$의 projective space이다.

</div>

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> $$\mathcal{L}$$에 대한 *linear system*은 $$\lvert \mathcal{L} \rvert$$의 nonempty projective subspace이다. 즉, 부분벡터공간 $$V \subseteq H^0(X, \mathcal{L})$$에 대해 $$\mathbb{P}(V) \subseteq \lvert \mathcal{L} \rvert$$의 꼴이다.

</div>

Linear system의 차원은 $$\dim V - 1$$로 정의한다. $$V$$가 $$r+1$$차원이면, 이 linear system은 *$$r$$-dimensional*이라 불린다. 1차원 linear system을 *pencil*, 2차원을 *net*, 3차원을 *web*이라 부르기도 한다.

<div class="misc" markdown="1">
**기하학적 해석.** Complete linear system $$\lvert \mathcal{L} \rvert = \mathbb{P}(H^0(X, \mathcal{L}))$$는 $$\mathcal{L}$$에 대응하는 divisor class 안의 모든 effective divisor들의 모임과 자연스럽게 대응된다. 구체적으로, nonzero section $$s \in H^0(X, \mathcal{L})$$는 $$\mathcal{L}$$의 zero divisor $$\operatorname{div}(s)$$를 정의하며, scalar multiple인 section들은 같은 effective divisor를 정의한다. 따라서 $$\lvert \mathcal{L} \rvert$$의 한 점은 $$\mathcal{L}$$ class의 한 effective divisor를 나타낸다.
</div>

## 사영공간에서의 Complete Linear System

앞서 [§Line Bundles, ⁋예시 19](/ko/math/algebraic_geometry/line_bundles#ex19)에서 $$H^0(\mathbb{P}^n, \mathcal{O}_{\mathbb{P}^n}(d))$$가 차수 $$d$$의 동차다항식들의 공간 $$\mathbb{K}[\x_0, \ldots, \x_n]_d$$와 동형임을 보았다. 따라서 ([§Picard Group, ⁋예시 6](/ko/math/algebraic_geometry/picard_group#ex6))의 맥락에서, divisor $$dH$$에 대응하는 line bundle $$\mathcal{O}_{\mathbb{P}^n}(d)$$의 complete linear system은 다음과 같다.

$$\lvert \mathcal{O}_{\mathbb{P}^n}(d) \rvert = \mathbb{P}(H^0(\mathbb{P}^n, \mathcal{O}_{\mathbb{P}^n}(d))) \cong \mathbb{P}(\mathbb{K}[\x_0, \ldots, \x_n]_d) \cong \mathbb{P}^{\binom{n+d}{d} - 1}$$

이것은 "차수 $$d$$의 hypersurface들의 family"의 정확한 정의이다. [§사영다양체](/ko/math/algebraic_geometry/projective_varieties)에서 보았듯, $$\mathbb{P}^n$$의 Zariski topology는 homogeneous polynomial의 zero set으로 정의되며, $$\mathbb{K}[\x_0, \ldots, \x_n]_d$$는 차수 $$d$$의 homogeneous polynomial들의 $$\mathbb{K}$$-벡터공간이다. $$\mathbb{P}^n$$에서 차수 $$d$$의 hypersurface는 원소 $$F \in \mathbb{K}[\x_0, \ldots, \x_n]_d \setminus \{0\}$$의 zero set $$Z(F)$$로 나타내어진다.

이제 우리는 다음 관찰을 한다. 스칼라 $$\lambda \in \mathbb{K}^\ast$$에 대해 $$Z(\lambda F) = Z(F)$$. 즉, nonzero scalar multiple들은 같은 hypersurface를 정의한다. 따라서 "차수 $$d$$의 hypersurface"들은 projective space $$\mathbb{P}(\mathbb{K}[\x_0, \ldots, \x_n]_d)$$의 한 점으로 나타내어진다. $$\dim \mathbb{K}[\x_0, \ldots, \x_n]_d = \binom{n+d}{d}$$이므로, 이 projective space의 차원은 $$\binom{n+d}{d} - 1$$이다.

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> **$$\mathbb{P}^2$$의 직선 family**: $$n = 2$$, $$d = 1$$인 경우, $$\mathbb{K}[\x_0, \x_1, \x_2]_1$$의 기저는 $$\{\x_0, \x_1, \x_2\}$$이다. 따라서 차수 1의 hypersurface (직선)들의 family는 $$\mathbb{P}^2$$와 동형이다. 한 점 $$[a_0 : a_1 : a_2] \in \mathbb{P}^2$$는 직선 $$Z(a_0 \x_0 + a_1 \x_1 + a_2 \x_2)$$에 대응된다.

</div>

## Linear System의 구체적 예시

<div class="example" markdown="1">

<ins id="ex4">**예시 4**</ins> **$$\mathbb{P}^2$$의 conic pencil**: 두 conic $$C_1 = Z(F_1)$$, $$C_2 = Z(F_2)$$의 *pencil*은

$$\{Z(\lambda F_1 + \mu F_2)\}_{[\lambda:\mu] \in \mathbb{P}^1}$$

이다. 이는 $$\lvert \mathcal{O}_{\mathbb{P}^2}(2) \rvert$$의 1차원 subspace이다. Pencil의 각 원소는 차수 2의 plane curve이며, 이들은 모두 $$C_1 \cap C_2$$를 지난다. $$\dim \mathbb{K}[\x_0, \x_1, \x_2]_2 = 6$$이므로 $$\lvert \mathcal{O}_{\mathbb{P}^2}(2) \rvert \cong \mathbb{P}^5$$이고, pencil은 이 $$\mathbb{P}^5$$의 1차원 부분공간이다.

</div>

## Closed Subvariety 위의 Linear System

이제 closed subvariety $$X \subseteq \mathbb{P}^n$$ 위에서의 linear system을 정의한다. $$\mathbb{P}^n$$의 linear system $$\mathbb{P}(V)$$에 대해, 각 $$F \in V$$는 $$X$$와의 교차 $$X \cap Z(F)$$를 정의한다. 이것이 $$X$$ 위의 linear system의 기하학적 내용이다.

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> Closed subvariety $$X \subseteq \mathbb{P}^n$$ 위에서, 부분벡터공간 $$V \subseteq \mathbb{K}[\x_0, \ldots, \x_n]_d$$가 정의하는 *linear system*은 $$\mathbb{P}(V)$$의 각 원소 $$[F]$$가 $$X$$ 위의 교차 $$X \cap Z(F)$$에 대응되는 family이다.

</div>

이때 $$X$$ 위에서 두 다항식 $$F, G$$가 같은 교차를 정의하는 것은 $$F \equiv G \pmod{I(X)}$$일 때, 즉 $$F - G$$가 $$X$$의 defining ideal $$I(X)$$에 속할 때이다. 따라서 $$X$$ 위에서의 실제 parameter space는 $$\mathbb{P}(V / (V \cap I(X)))$$이다.

<div class="example" markdown="1">

<ins id="ex6">**예시 6**</ins> **$$\mathbb{P}^1$$ 위의 점들의 family**: $$\mathbb{P}^1$$에서 차수 1의 hypersurface는 점 한 개이다. $$\mathbb{K}[\x_0, \x_1]_1$$의 기저는 $$\{\x_0, \x_1\}$$이고, $$\lvert \mathcal{O}_{\mathbb{P}^1}(1) \rvert \cong \mathbb{P}^1$$이다. 한 점 $$[a : b] \in \mathbb{P}^1$$은 $$\mathbb{P}^1$$의 점 $$Z(a \x_0 + b \x_1) = [b : -a]$$에 대응된다.

</div>

## Base Locus

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> Linear system $$L \subseteq \lvert \mathcal{L} \rvert$$의 *base locus* $$\operatorname{Bs}(L)$$는 $$L$$의 모든 원소가 공유하는 closed subset이다. 구체적으로, $$L = \mathbb{P}(V)$$에서 $$V \subseteq H^0(X, \mathcal{L})$$일 때,

$$\operatorname{Bs}(L) = \bigcap_{s \in V \setminus \{0\}} \operatorname{Supp}(\operatorname{div}(s))$$

여기서 $$\operatorname{div}(s)$$는 section $$s$$의 zero divisor이다. $$\mathbb{P}^n$$의 hypersurface 계산에서는 $$V \subseteq \mathbb{K}[\x_0, \ldots, \x_n]_d$$에 대해 $$\operatorname{Bs}(L) = \bigcap_{[F] \in L} Z(F)$$와 동일하다.

</div>

<div class="definition" markdown="1">

<ins id="def8">**정의 8**</ins> $$L$$이 *basepoint-free*라는 것은 $$\operatorname{Bs}(L) = \emptyset$$인 것이다. 즉, 임의의 점 $$p \in X$$에서 $$p$$를 지나지 않는 $$L$$의 원소가 항상 존재한다.

</div>

<div class="example" markdown="1">

<ins id="ex9">**예시 9**</ins> **$$\mathbb{P}^n$$의 hyperplane system**: $$\lvert \mathcal{O}_{\mathbb{P}^n}(1) \rvert = \mathbb{P}(\mathbb{K}[\x_0, \ldots, \x_n]_1)$$는 basepoint-free이다. 임의의 점 $$p = [p_0 : \cdots : p_n] \in \mathbb{P}^n$$에 대해, $$p$$를 지나지 않는 hyperplane $$Z(\x_i)$$ (단, $$p_i \ne 0$$인 $$i$$를 택함)이 존재하기 때문이다. 즉, $$p \notin \operatorname{Bs}(\lvert \mathcal{O}_{\mathbb{P}^n}(1) \rvert)$$이다.

</div>

<div class="example" markdown="1">

<ins id="ex10">**예시 10**</ins> **Pencil의 base locus**: [예시 4](#ex4)의 conic pencil의 base locus는 $$C_1 \cap C_2$$이다. Bézout's theorem ([§Bézout 정리](/ko/math/algebraic_geometry/bezout_theorem))에 의해, $$\mathbb{P}^2$$에서 두 conic의 교차는 (중복도를 포함하여) 4개의 점으로 구성된다.

</div>

## Basepoint-Free Linear System이 정의하는 사상

Basepoint-free linear system의 핵심 성질은, 이것이 다양체에서 사영공간으로의 사상을 자연스럽게 정의한다는 것이다.

<div class="proposition" markdown="1">

<ins id="prop11">**명제 11**</ins> Closed subvariety $$X \subseteq \mathbb{P}^n$$ 위의 basepoint-free linear system $$L = \mathbb{P}(V)$$에서, $$V$$의 기저 $$F_0, \ldots, F_r \in \mathbb{K}[\x_0, \ldots, \x_n]_d$$가 다음 조건을 만족한다고 하자:

$$\bigcap_{i=0}^r Z(F_i) \cap X = \emptyset$$

그러면 $$V$$는 $$X$$에서 사영공간으로의 정칙사상

$$\varphi_L: X \to \mathbb{P}^r, \quad p \mapsto [F_0(p) : \cdots : F_r(p)]$$

을 정의한다. 여기서 $$F_i(p)$$는 $$F_i$$의 $$p$$에서의 값을 나타낸다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

우선 $$\varphi_L$$이 well-defined임을 보여야 한다. $$p \in X$$일 때, $$p \in \operatorname{Bs}(L) = \emptyset$$이므로 어떤 $$i$$에 대해 $$F_i(p) \ne 0$$이다. 따라서 $$[F_0(p) : \cdots : F_r(p)]$$는 $$\mathbb{P}^r$$의 정상적인 점이다.

다음으로 $$\varphi_L$$이 정칙사상임을 보이자. $$X$$의 affine open cover $$U_\alpha = X \cap (\mathbb{P}^n \setminus Z(G_\alpha))$$를 생각하자. 각 $$U_\alpha$$에서 $$G_\alpha \ne 0$$이므로, $$F_i / G_\alpha^d$$는 $$U_\alpha$$에서 정의되는 regular function이다. $$\varphi_L$$의 $$j$$번째 좌표는 이 regular function들의 비율로 나타나므로, $$\varphi_L$$은 $$U_\alpha$$에서 정칙사상이다.

</details>

<div class="example" markdown="1">

<ins id="ex12">**예시 12**</ins> **Rational normal curve**: $$\mathbb{P}^1$$에서 $$d \ge 1$$일 때, $$\lvert \mathcal{O}_{\mathbb{P}^1}(d) \rvert$$의 complete linear system이 정의하는 사상은 *Veronese 사상* 또는 *rational normal curve*이라 불린다.

$$\nu_d: \mathbb{P}^1 \to \mathbb{P}^d, \quad [s : t] \mapsto [s^d : s^{d-1}t : \cdots : t^d]$$

이 사상의 image는 $$\mathbb{P}^d$$에서 degree $$d$$의 *rational normal curve*이다. $$d = 2$$일 때는 $$\mathbb{P}^2$$의 conic (parabola의 projective closure), $$d = 3$$일 때는 $$\mathbb{P}^3$$의 twisted cubic이다.

</div>

## Very Ample과 Ample

<div class="definition" markdown="1">

<ins id="def13">**정의 13**</ins> Line bundle $$\mathcal{L}$$ (또는 대응하는 linear system $$\lvert \mathcal{L} \rvert$$)이 *very ample*이라는 것은, complete linear system $$\lvert \mathcal{L} \rvert = \mathbb{P}(H^0(X, \mathcal{L}))$$이 정의하는 사상 $$\varphi_{\mathcal{L}}: X \to \mathbb{P}(H^0(X, \mathcal{L}))$$이 closed embedding인 것이다.

</div>

<div class="definition" markdown="1">

<ins id="def14">**정의 14**</ins> $$\mathcal{L}$$이 *ample*이라는 것은 어떤 $$m > 0$$에 대해 $$\mathcal{L}^{\otimes m}$$이 very ample인 것이다.

</div>

<div class="proposition" markdown="1">

<ins id="prop15">**명제 15**</ins> Very ample line bundle은 항상 basepoint-free이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$\varphi_{\mathcal{L}}: X \hookrightarrow \mathbb{P}^r$$이 embedding이면 모든 점에서 정의된다. $$\varphi_{\mathcal{L}}(p) = [s_0(p) : \cdots : s_r(p)]$$ (여기서 $$s_0, \ldots, s_r$$은 $$H^0(X, \mathcal{L})$$의 기저)이므로, 각 $$p \in X$$에 대해 어떤 $$i$$가 $$s_i(p) \ne 0$$이다. 따라서 $$\operatorname{Bs}(\lvert \mathcal{L} \rvert) = \emptyset$$이다.

</details>

<div class="example" markdown="1">

<ins id="ex16">**예시 16**</ins> **$$\mathcal{O}_{\mathbb{P}^n}(1)$$은 very ample**: $$\lvert \mathcal{O}_{\mathbb{P}^n}(1) \rvert = \mathbb{P}(\mathbb{K}[\x_0, \ldots, \x_n]_1)$$는 identity embedding $$\mathbb{P}^n \hookrightarrow \mathbb{P}^n$$을 정의한다. $$F_i = \x_i$$로 놓으면 $$\varphi_L([x_0 : \cdots : x_n]) = [x_0 : \cdots : x_n]$$이다.

</div>

<div class="example" markdown="1">

<ins id="ex17">**예시 17**</ins> **$$\mathcal{O}_{\mathbb{P}^n}(d)$$도 very ample**: $$d > 0$$이면 $$\lvert \mathcal{O}_{\mathbb{P}^n}(d) \rvert$$는 *Veronese embedding*

$$\nu_d: \mathbb{P}^n \hookrightarrow \mathbb{P}^N, \quad [x_0 : \cdots : x_n] \mapsto [\text{모든 차수 } d \text{의 단일항식}]$$

을 정의한다. 여기서 $$N = \binom{n+d}{d} - 1$$이다. 이 사상은 $$\mathbb{P}^n$$을 $$\mathbb{P}^N$$의 smooth degree $$d$$의 subvariety로 embedding한다.

</div>

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.
