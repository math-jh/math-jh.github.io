---
title: "코다이라 소멸정리"
permalink: /ko/math/algebraic_varieties/kodaira_vanishing
excerpt: "Kodaira vanishing theorem과 그 응용"
categories: [Math / Algebraic Varieties]
sidebar:
    nav: "algebraic_varieties-ko"
header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Kodaira_Vanishing.png
    overlay_filter: 0.5
date: 2026-05-07
last_modified_at: 2026-05-07
weight: 17
---

우리는 [§사영공간의 코호몰로지, ⁋명제 4](/ko/math/algebraic_varieties/cohomology_of_projective_spaces#prop4)에서 Serre vanishing theorem을 살펴 보았다. 이 정리는 projective variety 위의 ample line bundle $$\mathcal{L}$$과 coherent sheaf $$\mathcal{F}$$에 대해, 충분히 큰 $$m$$에 대하여 $$H^i(X, \mathcal{F} \otimes \mathcal{L}^{\otimes m}) = 0$$ ($$i > 0$$)이 성립함을 보장한다. 그러나 이 결과는 단지 asymptotic한 성질에 불과하며, 구체적으로 어떤 $$m$$에서부터 vanishing이 시작되는지에 대해서는 아무 정보도 주지 않는다.

이에 비해 Kodaira vanishing theorem은 훨씬 더 정교한 결과로, canonical bundle $$K_X$$와 ample line bundle $$L$$의 tensor product $$K_X \otimes L$$에 대해 higher cohomology가 *항상* 사라진다는 사실을 보장한다. 이 정리는 1950년대 Kodaira가 complex manifold 위에서 Kähler metric과 Hodge theory를 사용하여 증명한 이래, algebraic geometry의 중심에 자리 잡았으며, 이후 Deligne과 Illusie에 의해 purely algebraic한 증명이 주어지기까지 그 중요성은 계속 커져왔다. 우리는 이 글에서 Kodaira vanishing theorem과 그 일반화, 그리고 이 정리가 algebraic geometry에서 어떻게 활용되는지를 살펴 본다.

## 코다이라 소멸정리

우리가 다룰 기본적인 설정은 다음과 같다. $$X$$는 차원 $$n$$의 smooth projective variety이고, $$L$$은 $$X$$ 위의 ample line bundle이다. Canonical bundle $$K_X = \det \Omega_X^1 = \Omega_X^n$$은 [§표준선다발, ⁋정의 1](/ko/math/algebraic_varieties/canonical_bundle#def1)에서 정의한 바와 같으며, 이는 holomorphic $$n$$-forms들의 sheaf이다. Kodaira vanishing theorem은 이들 데이터에 대해 다음을 주장한다.

<div class="proposition" markdown="1">

<ins id="thm1">**정리 1 (Kodaira vanishing)**</ins> $$X$$를 차원 $$n$$인 smooth projective variety, $$L$$을 $$X$$ 위의 ample line bundle이라 하자. 그럼 모든 $$i > 0$$에 대하여

$$H^i(X, K_X \otimes L) = 0$$

이 성립한다.

</div>

정리의 서술에서 알 수 있듯, Kodaira vanishing은 canonical bundle에 대한 twist 이후의 higher cohomology를 제거한다. Serre duality를 사용하면 이는 다음의 동치된 서술로 바꾸어 쓸 수 있다.

<div class="proposition" markdown="1">

<ins id="cor2">**따름정리 2**</ins> 정리 1의 가정 아래, 모든 $$i < n$$에 대하여

$$H^i(X, L^{-1}) = 0$$

이 성립한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

[§세르 쌍대성, ⁋명제 2](/ko/math/algebraic_varieties/serre_duality#prop2)의 Serre duality에 의해

$$H^i(X, L^{-1}) \cong H^{n-i}(X, K_X \otimes L)^\vee$$

이 성립한다. $$i < n$$이면 $$n - i > 0$$이므로, [정리 1](#thm1)에 의해 우변은 $$0$$이다.

</details>

따름정리 2의 서술은 Kodaira의 원래 증명과 더 가까운 형태로, negative line bundle $$L^{-1}$$에 대한 cohomology vanishing을 다룬다. 두 서술은 Serre duality를 통해 완전히 동치이므로 상황에 따라 더 편한 쪽을 사용하면 된다.

## 나칸노 소멸정리

Kodaira vanishing은 사실 더 일반적인 정리의 특수한 경우이다. Nakano는 differential forms의 sheaf $$\Omega_X^p$$와 ample line bundle의 tensor product에 대한 더 강력한 vanishing result를 증명하였다.

<div class="proposition" markdown="1">

<ins id="thm3">**정리 3 (Nakano vanishing)**</ins> $$X$$를 차원 $$n$$인 smooth projective variety, $$L$$을 $$X$$ 위의 ample line bundle이라 하자. 그럼 모든 $$p, q$$에 대하여 $$p + q > n$$이면

$$H^q(X, \Omega_X^p \otimes L) = 0$$

이 성립한다.

</div>

Kodaira vanishing은 Nakano vanishing의 특수한 경우임을 확인할 수 있다. $$p = n$$을 대입하면 $$\Omega_X^n = K_X$$이고, $$p + q > n$$ 조건은 $$q > 0$$과 동치이므로 정리 1을 얻는다. 따라서 Nakano vanishing은 Kodaira vanishing을 포함하는 strictly stronger한 결과이다.

또 다른 관점에서, Kodaira vanishing은 $$L$$이 ample일 때 $$H^q(X, K_X \otimes L) = 0$$ ($$q > 0$$)을 주장한다. 반면 Nakano vanishing은 같은 가정 하에서 $$H^q(X, \Omega_X^p \otimes L) = 0$$ ($$p + q > n$$)을 주장하므로, intermediate degrees의 differential forms에 대해서도 vanishing이 일어남을 보장한다. 특히 $$p = 0$$일 때 $$H^q(X, L) = 0$$ ($$q > n$$)은 자명한 결과이지만, $$p = 1$$이고 $$q = n$$인 경우 $$H^n(X, \Omega_X^1 \otimes L) = 0$$은 자명하지 않은 정보를 준다.

## 사영공간에서의 검증

Kodaira vanishing이 가장 단순한 non-trivial한 예시를 제공하는 것은 바로 projective space $$X = \mathbb{P}^n$$이다. 우리는 [§표준선다발, ⁋명제 7](/ko/math/algebraic_varieties/canonical_bundle#prop7)에서

$$K_{\mathbb{P}^n} \cong \mathcal{O}(-n-1)$$

임을 확인하였고, [§선다발과 벡터다발, ⁋예시 16](/ko/math/algebraic_varieties/line_bundles#ex16)에서 $$\mathbb{P}^n$$ 위의 임의의 line bundle은 $$\mathcal{O}(d)$$ 꼴임을 확인하였다. Ample line bundle은 $$d > 0$$인 경우 $$\mathcal{O}(d)$$이므로, Kodaira vanishing은 다음을 주장해야 한다.

<div class="example" markdown="1">

<ins id="ex4">**예시 4**</ins> $$\mathbb{P}^n$$ 위에서 $$d > 0$$일 때, 모든 $$i > 0$$에 대하여

$$H^i(\mathbb{P}^n, \mathcal{O}(d - n - 1)) = 0$$

이 성립한다.

</div>

이는 [§사영공간의 코호몰로지, ⁋명제 1](/ko/math/algebraic_varieties/cohomology_of_projective_spaces#prop1)의 Bott formula를 통해 직접 검증할 수 있다. Bott formula에 따르면 $$H^i(\mathbb{P}^n, \mathcal{O}(k))$$는 $$0 < i < n$$인 경우 언제나 $$0$$이고, $$i = n$$인 경우는 $$k \leq -n-1$$일 때만 non-zero이다. 우리가 관심 있는 경우는 $$k = d - n - 1$$이며 $$d > 0$$이므로 $$k > -n - 1$$이다. 따라서 $$i = n$$인 경우에도 cohomology는 $$0$$이 된다. $$i > n$$인 경우는 dimension reason으로 자명히 $$0$$이므로, Kodaira vanishing이 $$\mathbb{P}^n$$에서 성립함을 확인할 수 있다.

비슷하게 Nakano vanishing도 $$\mathbb{P}^n$$에서 직접 확인할 수 있다. [§사영공간의 코호몰로지, ⁋명제 1](/ko/math/algebraic_varieties/cohomology_of_projective_spaces#prop1)의 증명에서 사용한 hyperplane restriction exact sequence를 반복적으로 적용하면, $$\Omega_{\mathbb{P}^n}^p \otimes \mathcal{O}(d)$$의 cohomology가 $$\mathcal{O}(k)$$들의 cohomology로 표현됨을 알 수 있으며, $$d > 0$$이고 $$p + q > n$$이면 이들이 모두 사라진다는 것을 확인할 수 있다.

## 활용

Kodaira vanishing theorem은 algebraic geometry에서 다양한 중요한 결과들의 핵심적인 ingredient로 작용한다. 증명의 자세한 내용보다는, 이 정리가 실제 문제 해결에서 어떻게 활용되는지를 중심으로 살펴 보자.

### 히제브루흐-리만-로흐 공식과의 연결

Hirzebruch-Riemann-Roch (HRR) 공식은 vector bundle $$E$$에 대해

$$\chi(X, E) = \int_X \operatorname{ch}(E) \operatorname{Td}(X)$$

를 준다. 여기서 $$\chi(X, E) = \sum_{i=0}^{\dim X} (-1)^i \dim H^i(X, E)$$는 Euler 지표이며, 우변은 Chern character와 Todd class의 교차곱으로 이루어진 위상적 불변량이다. HRR 공식의 강력함은 $$\chi$$를 순전히 대수적·위상적 데이터로 계산할 수 있다는 데 있지만, 문제는 $$\chi$$가 $$h^0, h^1, h^2, \ldots$$의 교대합이라는 점이다. 따라서 단순히 $$h^0(X, E)$$만을 알고 싶을 때는 higher cohomology들의 값을 각각 따로 구해야 하므로, HRR 공식만으로는 직접적인 답을 얻기 어렵다.

Kodaira vanishing은 바로 이 간극을 메운다. $$L$$이 ample line bundle이면 정리 1에 의해 $$H^i(X, K_X \otimes L) = 0$$ ($$i > 0$$)이므로,

$$\chi(X, K_X \otimes L) = h^0(X, K_X \otimes L)$$

가 된다. 따라서 HRR 공식의 우변을 계산하는 것만으로 곧바로 $$h^0(X, K_X \otimes L)$$를 얻을 수 있다. 예를 들어 surface $$S$$ 위에서 HRR은

$$\chi(S, K_S \otimes L) = \frac{(K_S + L) \cdot L}{2} + \chi(\mathcal{O}_S)$$

의 형태로 주어지며, Kodaira vanishing 덕분에 이 값이 곧 $$h^0(S, K_S \otimes L)$$가 된다.

비슷하게 $$L^{\otimes m}$$에 대해서도 동일한 논리가 적용되어, 충분히 큰 $$m$$에서 $$h^0(X, K_X \otimes L^{\otimes m})$$를 HRR로 효율적으로 계산할 수 있다. 이는 asymptotic Riemann-Roch의 핵심 아이디어이며, line bundle의 positivity와 variety의 geometry를 연결하는 중요한 계산 도구가 된다.

### 노이터 공식과 K3 곡면

Noether formula는 surface $$S$$에 대해

$$\chi_{top}(S) = 12\bigl(K_S^2 + \chi(\mathcal{O}_S)\bigr)$$

를 주는 classical result이다. 여기서 $$\chi(\mathcal{O}_S) = \sum (-1)^i h^i(S, \mathcal{O}_S)$$이며, Kodaira vanishing은 $$K_S$$가 nef이거나 ample한 상황에서 higher cohomology를 제거하여 $$\chi(\mathcal{O}_S)$$를 단순화하는 역할을 한다.

특히 K3 surface는 $$K_X \cong \mathcal{O}_X$$를 만족하는 simply connected compact Kähler surface이다. 이 정의로부터 $$h^0(K_X) = h^0(\mathcal{O}_X) = 1$$이고 $$H^1(X, \mathcal{O}_X) = 0$$이며, Serre duality로 $$H^2(X, \mathcal{O}_X) \cong H^0(X, K_X)^\vee \cong \mathbb{C}$$이므로 $$h^2(\mathcal{O}_X) = 1$$이다. 따라서 $$\chi(\mathcal{O}_X) = 1 - 0 + 1 = 2$$이다. Noether formula에 $$K_X^2 = 0$$과 $$\chi(\mathcal{O}_X) = 2$$를 대입하면 $$\chi_{top}(X) = 24$$이며, 이는 K3 surface의 Hodge diamond를 결정하는 핵심 계산이다.

더 일반적으로 $$K_X$$가 trivial하거나 nef인 variety에서 Kodaira vanishing은 higher cohomology의 소멸을 보장하여 $$\chi$$만으로 원하는 불변량을 계산할 수 있게 한다. 예를 들어 abelian variety $$A$$ 위의 ample line bundle $$L$$에 대해 $$K_A \cong \mathcal{O}_A$$이므로 Kodaira vanishing에 의해 $$H^i(A, L) = 0$$ ($$i > 0$$)이 되어 $$\chi(A, L) = h^0(A, L)$$가 되고, Riemann-Roch 정리로부터 $$h^0(A, L) = L^{\dim A} / (\dim A)!$$이 성립함을 알 수 있다.

### 플루리게네라

Smooth projective variety $$X$$의 *plurigenus* $$P_m(X)$$는

$$P_m(X) = \dim H^0(X, K_X^{\otimes m})$$

으로 정의된다. 특히 $$m = 1$$인 경우 $$P_1(X) = \dim H^0(X, K_X)$$는 *geometric genus* $$p_g(X)$$이다. Kodaira vanishing은 이들 불변량을 계산하는 데 직접적으로 사용될 수 있다.

가령 curve $$C$$의 경우, Riemann-Roch theorem ([§곡선에서의 리만-로흐 정리, ⁋명제 3](/ko/math/algebraic_varieties/riemann_roch_theorem#prop3))과 Serre duality에 의해

$$\dim H^0(C, K_C^{\otimes m}) - \dim H^1(C, K_C^{\otimes m}) = m(2g - 2) + 1 - g$$

이다. $$m \geq 2$$이면 $$\deg(K_C^{\otimes m}) = m(2g - 2) > 2g - 2$$이므로 $$H^1(C, K_C^{\otimes m}) = 0$$이 Kodaira vanishing (혹은 그 보다 약한 Serre duality와 degree 계산)에 의해 성립한다. 따라서

$$P_m(C) = m(2g - 2) + 1 - g = (2m - 1)(g - 1)$$

을 얻는다. 이는 curve의 birational invariant로서 moduli problem을 다룰 때 중요한 역할을 한다.

Surface의 경우도 유사하다. [§곡면에서의 리만-로흐 정리](/ko/math/algebraic_varieties/riemann_roch_surfaces)에서 보듯, surface $$S$$ 위의 line bundle $$L$$에 대해 Riemann-Roch formula는

$$\chi(L) = \frac{L \cdot (L - K_S)}{2} + \chi(\mathcal{O}_S)$$

으로 주어진다. $$L = K_S^{\otimes m}$$을 대입하면

$$\chi(K_S^{\otimes m}) = \frac{m(m-1)}{2} K_S^2 + \chi(\mathcal{O}_S)$$

이다. $$m \geq 2$$이고 $$K_S$$가 nef이거나 ample한 상황에서 Kodaira vanishing (혹은 그 일반화인 Kawamata-Viehweg vanishing)을 사용하면 higher cohomology가 사라지므로, 이 formula로부터 직접 $$P_m(S) = h^0(S, K_S^{\otimes m})$$을 계산할 수 있다. 이러한 plurigenera의 계산은 surface의 classification theory, 특히 Enriques-Kodaira classification에서 핵심적인 역할을 한다.

### 코다이라 임베딩정리

Kodaira vanishing의 가장 유명한 응용은 Kodaira embedding theorem으로, 이는 Kähler manifold가 projective manifold가 될 충분조건을 제공한다.

<div class="proposition" markdown="1">

<ins id="thm5">**정리 5 (Kodaira embedding)**</ins> Compact Kähler manifold $$X$$ 위에 positive line bundle $$L$$이 존재하면, $$X$$는 smooth projective variety이고 충분히 큰 $$k$$에 대하여 $$L^{\otimes k}$$는 very ample이다. 즉 $$L^{\otimes k}$$는 $$X$$를 어떤 projective space로 embedding하는 linear system을 정의한다.

</div>

정리 5의 증명에서 Kodaira vanishing은 higher cohomology의 소멸을 통해 $$H^0(X, L^{\otimes k})$$의 dimension을 계산하고, 이를 통해 sections가 base points를 갖지 않으며 separating property를 만족함을 보이는 데 사용된다. 이 정리는 Kähler geometry와 algebraic geometry 사이의 다리 역할을 하며, 어떤 Kähler manifold가 algebraic하려면 반드시 integral Kähler class를 가져야 한다는 필요충분조건도 함께 제공한다.

### very ampleness와 projective normality

Kodaira vanishing은 very ampleness와 projective normality를 판정할 때에도 핵심적인 역할을 한다. Line bundle $$L$$이 very ample이려면 그 global sections가 임의의 두 점을 분리하고(separation of points), 임의의 점에서 tangent vectors를 분리(separation of tangent vectors)해야 한다. 이러한 성질들은 보통 cohomology long exact sequence를 통해 검증되며, 그 과정에서 $$H^1$$이 방해 요소로 등장한다.

구체적으로, $$L$$이 ample이면 Kodaira vanishing은 $$H^i(X, K_X \otimes L^{\otimes m}) = 0$$ ($$i > 0$$)을 보장하고, 이를 통해 충분히 큰 $$m$$에서 $$L^{\otimes m}$$의 sections가 위의 separation 조건들을 만족함을 보일 수 있다. 이는 Kodaira embedding theorem의 증명에서 핵심적으로 사용되는 바이다. 더 나아가 $$L^{\otimes m}$$이 very ample일 뿐만 아니라 그에 의한 embedding이 projectively normal이 되도록 하는 조건도, Kodaira vanishing을 통해 관련된 multiplication map

$$S^\mu H^0(X, L^{\otimes m}) \longrightarrow H^0(X, L^{\otimes \mu m})$$

의 surjectivity를 검증함으로써 얻을 수 있다. 이러한 vanishing은 higher cohomology가 sections의 생성을 방해하지 않음을 보장하여, linear system의 풍부함을 정량적으로 다룰 수 있게 한다.

## 카와마타-비에흐 소멸정리

Kodaira vanishing은 birational geometry에서 더욱 일반적인 형태로 확장되었다. Kawamata와 Viehweg는 ample line bundle의 조건을 *big and nef* line bundle으로 완화하여, 이를 일반화하였다. 이들의 결과는 log terminal pair에 대한 vanishing theorem의 형태로 서술되며, modern minimal model program의 핵심적인 도구로 작용한다. 이 일반화는 Kodaira vanishing의 정신을 그대로 이어받으면서도, birational transform 하에서의 안정성을 보장하여 algebraic geometry의 더 넓은 영역에서 응용될 수 있게 한다.

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.

**[Laz]** R. Lazarsfeld, *Positivity in Algebraic Geometry I & II*, Ergebnisse der Mathematik, Springer, 2004.

**[DI]** P. Deligne, L. Illusie, *Relèvements modulo $$p^2$$ et décomposition du complexe de de Rham*, Inventiones Mathematicae, 1987.

**[Kod]** K. Kodaira, *On a differential-geometric method in the theory of analytic stacks*, Proceedings of the National Academy of Sciences, 1953.

**[Nak]** S. Nakano, *On complex analytic vector bundles*, Journal of the Mathematical Society of Japan, 1955.

---
