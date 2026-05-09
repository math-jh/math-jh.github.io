---
title: "고다이라 소멸정리"
permalink: /ko/math/algebraic_varieties/kodaira_vanishing
excerpt: "Kodaira vanishing theorem과 그 응용"
categories: [Math / Algebraic Varieties]

sidebar:
    nav: "algebraic_varieties-ko"
    
header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Kodaira_Vanishing.png
    overlay_filter: 0.5

date: 2026-05-07
last_modified_at: 2026-05-09
weight: 17
published: false
---

[§사영공간의 코호몰로지, ⁋명제 4](/ko/math/algebraic_varieties/cohomology_of_projective_spaces#prop4)의 Serre vanishing theorem은 projective variety 위의 ample line bundle $$\mathcal{L}$$과 coherent sheaf $$\mathcal{F}$$에 대해, 충분히 큰 $$m$$에 대하여 $$H^i(X, \mathcal{F} \otimes \mathcal{L}^{\otimes m}) = 0$$ ($$i > 0$$)이 성립함을 보장한다. 그러나 이 결과는 단지 asymptotic한 성질에 불과하며, 구체적으로 어떤 $$m$$에서부터 vanishing이 시작되는지에 대해서는 아무 정보도 주지 않는다.

Kodaira vanishing theorem은 훨이보다 씬 더 정교한 결과로, canonical bundle $$\omega_X$$와 ample line bundle $$\mathcal{L}$$의 tensor product $$\omega_X \otimes \mathcal{L}$$에 대해 higher cohomology가 *항상* 사라진다는 사실을 보장한다. 우리는 이 글에서 Kodaira vanishing theorem과 그 응용, 그리고 이 정리가 algebraic geometry에서 어떻게 활용되는지를 살펴 본다.

## 고다이라 소멸정리

우리가 다룰 기본적인 설정은 다음과 같다. $$X$$는 $$n$$차원 smooth projective variety이고, $$\mathcal{L}$$은 $$X$$ 위의 ample line bundle, $$\omega_X = \det \Omega_X^1 = \Omega_X^n$$은 canonical line bundle이다. ([§표준선다발, ⁋정의 1](/ko/math/algebraic_varieties/canonical_bundle#def1)) 그럼 Kodaira vanishing theorem은 다음과 같이 쓸 수 있다. 

<div class="proposition" markdown="1">

<ins id="prop1">**명제 1 (Kodaira vanishing)**</ins> $$n$$차원 smooth projective variety $$X$$, ample line bundle $$\mathcal{L}$$이 주어졌다 하자. 그럼 모든 $$i > 0$$에 대하여

$$H^i(X, \omega_X \otimes \mathcal{L}) = 0$$

이 성립한다. 더 일반적으로, $$p+q>n$$을 만족하는 $$p,q$$에 대하여

$$H^p(X, \Omega^q\otimes \mathcal{L})_0$$

이 성립한다. 

</div>

첫째 주장은 둘째 주장에서 $$q=n$$으로 두어 얻어지는 것이다. 이 명제에 대한 증명은 꽤나 기술적인 부분이 있어 이번 글에서는 이를 엄밀하게 증명하기보다는 대수기하학에서 어떻게 사용되는지에 초점을 맞춘다. 

명제의 서술에서 알 수 있듯, Kodaira vanishing은 canonical bundle에 대한 twist 이후의 higher cohomology를 제거한다. Serre duality를 사용하면 이는 다음의 동치된 서술로 바꾸어 쓸 수 있다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> [명제 1](#prop1)의 가정 아래, 모든 $$i < n$$에 대하여

$$H^i(X, \mathcal{L}^{-1}) = 0$$

이 성립한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

[§세르 쌍대성, ⁋명제 2](/ko/math/algebraic_varieties/serre_duality#prop2)의 Serre duality에 의해

$$H^i(X, \mathcal{L}^{-1}) \cong H^{n-i}(X, \omega_X \otimes \mathcal{L})^\vee$$

이 성립한다. $$i < n$$이면 $$n - i > 0$$이므로, [명제 1](#prop1)에 의해 우변은 $$0$$이다.

</details>

이 두 formulation은 위의 증명에서 살펴본 것과 같이 Serre duality를 통해 완전히 동치이므로 상황에 따라 더 편한 쪽을 사용하면 된다.

## 사영공간에서의 검증

Kodaira vanishing이 가장 단순한 non-trivial한 예시를 제공하는 것은 바로 projective space $$X = \mathbb{P}^n$$이다. 우리는 [§표준선다발, ⁋명제 7](/ko/math/algebraic_varieties/canonical_bundle#prop7)에서

$$\omega_{\mathbb{P}^n} \cong \mathcal{O}(-n-1)$$

임을 확인하였고, [§선다발과 벡터다발, ⁋예시 16](/ko/math/algebraic_varieties/line_bundles#ex16)에서 $$\mathbb{P}^n$$ 위의 임의의 line bundle은 $$\mathcal{O}(d)$$ 꼴임을 확인하였다. Ample line bundle은 $$d > 0$$인 경우 $$\mathcal{O}(d)$$이므로, Kodaira vanishing은 다음을 주장해야 한다.

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> $$\mathbb{P}^n$$ 위에서 $$d > 0$$일 때, 모든 $$i > 0$$에 대하여

$$H^i(\mathbb{P}^n, \mathcal{O}(d - n - 1)) = 0$$

이 성립한다.

</div>

이는 [§사영공간의 코호몰로지, ⁋명제 1](/ko/math/algebraic_varieties/cohomology_of_projective_spaces#prop1)의 Bott formula를 통해 직접 검증할 수 있다. Bott formula에 따륨면 $$H^i(\mathbb{P}^n, \mathcal{O}(k))$$는 $$0 < i < n$$인 경우 언제나 $$0$$이고, $$i = n$$인 경우는 $$k \leq -n-1$$일 때만 non-zero이다. 우리가 관심 있는 경우는 $$k = d - n - 1$$이며 $$d > 0$$이므로 $$k > -n - 1$$이다. 따라서 $$i = n$$인 경우에도 cohomology는 $$0$$이 된다. $$i > n$$인 경우는 dimension reason으로 $$0$$이므로, Kodaira vanishing이 $$\mathbb{P}^n$$에서 성립함을 확인할 수 있다.

## 활용

Kodaira vanishing theorem은 algebraic geometry에서 다양한 중요한 결과들의 핵심적인 ingredient로 작용한다. 증명의 자세한 내용보다는, 이 정리가 실제 문제 해결에서 어떻게 활용되는지를 중심으로 살펴 보자.

### 히제브루흐-리만-로흐 공식과의 연결

Riemann-Roch 공식은 surface $$S$$ 위의 divisor $$D$$에 대해

$$\rchi(\mathcal{O}_S(D)) = \frac{1}{2} D \cdot (D - K_S) + \rchi(\mathcal{O}_S)$$

를 준다. 여기서 $$K_S$$는 canonical divisor를 나타내고, $$\rchi(S, \mathcal{O}_S(D)) = \sum_{i=0}^{2} (-1)^i \dim H^i(S, \mathcal{O}_S(D))$$는 Euler 지표이다. 이 공식의 강력함은 $$\rchi$$를 순전히 대수적·위상적 데이터로 계산할 수 있다는 데 있지만, 문제는 $$\rchi$$가 $$h^0, h^1, h^2$$의 교대합이라는 점이다. 따라서 단순히 $$h^0(S, \mathcal{O}_S(D))$$만을 알고 싶을 때는 higher cohomology들의 값을 각각 따로 구해야 하므로, Riemann-Roch 공식만으로는 직접적인 답을 얻기 어렵다.

특히 Kodaira vanishing에서 다루는 $$\omega_S \otimes \mathcal{L}$$에 대해서는, $$\mathcal{L} \cong \mathcal{O}_S(L)$$로 두면 $$\omega_S \otimes \mathcal{L} \cong \mathcal{O}_S(K_S + L)$$이 되어 위 공식에 $$D = K_S + L$$을 대입할 수 있다. $$\mathcal{L}$$이 ample line bundle이면 명제 1에 의해 $$H^i(S, \omega_S \otimes \mathcal{L}) = 0$$ ($$i > 0$$)이므로,

$$\rchi(S, \omega_S \otimes \mathcal{L}) = h^0(S, \omega_S \otimes \mathcal{L})$$

가 된다. 따라서 Riemann-Roch 공식의 우변을 계산하는 것만으로 곧바로 $$h^0(S, \omega_S \otimes \mathcal{L})$$를 얻을 수 있다.

비슷하게 $$\mathcal{L}^{\otimes m}$$에 대해서도 동일한 논리가 적용되어, 충분히 큰 $$m$$에서 $$h^0(S, \omega_S \otimes \mathcal{L}^{\otimes m})$$를 효율적으로 계산할 수 있다. 더 높은 차원에서도 성립하는 Hirzebruch-Riemann-Roch formula에서도 동일한 원리가 적용된다.

### 플루리게네라

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> Smooth projective variety $$X$$의 *m-th plurigenus* $$P_m(X)$$는

$$P_m(X) = \dim H^0(X, \omega_X^{\otimes m})$$

로 정의된다. 특히 $$m=1$$인 경우, $$P_1(X) = \dim H^0(X, \omega_X)$$를 *geometric genus* $$p_g(X)$$라 한다.

</div>

Kodaira vanishing은 이들 불변량을 계산하는 데 직접적으로 사용될 수 있다.

가령 curve $$C$$의 경우, Riemann-Roch theorem ([§곡선에서의 리만-로흐 정리, ⁋명제 3](/ko/math/algebraic_varieties/riemann_roch_theorem#prop3))과 Serre duality에 의해

$$\dim H^0(C, \omega_C^{\otimes m}) - \dim H^1(C, \omega_C^{\otimes m}) = m(2g - 2) + 1 - g$$

이다. $$m \geq 2$$이면 $$\deg(\omega_C^{\otimes m}) = m(2g - 2) > 2g - 2$$이므로 $$H^1(C, \omega_C^{\otimes m}) = 0$$이 Kodaira vanishing (혹은 그보다 약한 Serre duality와 degree 계산)에 의해 성립한다. 따라서

$$P_m(C) = m(2g - 2) + 1 - g = (2m - 1)(g - 1)$$

을 얻는다. 이는 curve의 birational invariant로서 moduli problem을 다룰 때 중요한 역할을 한다.

Surface의 경우도 유사하다. [§곡면에서의 리만-로흐 정리](/ko/math/algebraic_varieties/riemann_roch_surfaces)에서 보듯, surface $$S$$ 위의 divisor $$D$$에 대해 Riemann-Roch formula는

$$\rchi(\mathcal{O}_S(D)) = \frac{1}{2} D \cdot (D - K_S) + \rchi(\mathcal{O}_S)$$

으로 주어진다. $$\omega_S^{\otimes m} \cong \mathcal{O}_S(mK_S)$$이므로 $$D = mK_S$$를 대입하면

$$\rchi(\mathcal{O}_S(mK_S)) = \frac{m(m-1)}{2} K_S^2 + \rchi(\mathcal{O}_S)$$

이다. $$m \geq 2$$이고 $$K_S$$가 nef이거나 ample한 상황에서 Kodaira vanishing을 사용하면 higher cohomology가 사라지므로, 이 formula로부터 직접 $$P_m(S) = h^0(S, \mathcal{O}_S(mK_S))$$을 계산할 수 있다. 이러한 plurigenera의 계산은 surface의 classification theory, 특히 Enriques-Kodaira classification에서 핵심적인 역할을 한다.

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> Surface $$S$$의 *Kodaira dimension* $$\kappa(S)$$는 $$P_m(S)$$의 $$m$$에 대한 증가 차수로 정의된다. 구체적으로, 모든 $$m \ge 1$$에 대해 $$P_m(S) = 0$$이면 $$\kappa = -\infty$$이다. 그렇지 않은 경우, $$\kappa(S)$$는 $$P_m(S) / m^\kappa$$가 유계(bounded)가 되는 최소의 정수 $$\kappa$$로 정의된다. 즉 $$\kappa(S) = \min\{k \in \mathbb{Z}_{\ge 0} : P_m(S) = O(m^k)\}$$이다. 이 정의에 의하면 $$\kappa = 0$$은 $$P_m(S)$$가 항상 $$0$$ 또는 $$1$$이면서 모든 $$m$$에 대해 $$0$$인 것은 아닌 경우이며, $$\kappa = 1$$은 $$P_m(S) \sim cm$$으로 선형 성장하는 경우, $$\kappa = 2$$는 $$P_m(S) \sim cm^2$$으로 이차 성장하는 경우이다. Surface의 경우 $$\kappa \in \{-\infty, 0, 1, 2\}$$이다.

</div>

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> $$m \ge 2$$에 대해, 만일 $$h^0(\mathcal{O}_S((1-m)K_S)) = 0$$이면

$$P_m(S) \ge \rchi(\mathcal{O}_S) + \frac{m(m-1)}{2} K_S^2$$

이다. 가설 $$h^0(\mathcal{O}_S((1-m)K_S)) = 0$$은 Serre duality에 의해 $$h^2(\mathcal{O}_S(mK_S)) = 0$$과 동치이며, 이는 $$m \gg 0$$에서 항상 만족된다—$$(1-m)K_S$$가 어떤 effective divisor보다도 "더 음수"이기 때문이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Riemann–Roch 공식 ([§곡면에서의 리만-로흐 정리, ⁋명제 4](/ko/math/algebraic_varieties/riemann_roch_surfaces#prop4))에 $$D = mK_S$$를 대입한다:

$$\rchi(\mathcal{O}_S(mK_S)) = \rchi(\mathcal{O}_S) + \frac{1}{2}\left((mK_S)^2 - (mK_S) \cdot K_S\right) = \rchi(\mathcal{O}_S) + \frac{1}{2}\left(m^2 K_S^2 - m K_S^2\right)$$

$$= \rchi(\mathcal{O}_S) + \frac{m(m-1)}{2} K_S^2$$

한편 $$\rchi(\mathcal{O}_S(mK_S)) = h^0(\mathcal{O}_S(mK_S)) - h^1(\mathcal{O}_S(mK_S)) + h^2(\mathcal{O}_S(mK_S))$$이다. Serre duality에 의해 $$h^2(\mathcal{O}_S(mK_S)) = h^0(\mathcal{O}_S((1-m)K_S))$$이다. 이 값은 명제의 가설에 의해 $$0$$이다. 따라서

$$P_m(S) = h^0(\mathcal{O}_S(mK_S)) = \rchi(\mathcal{O}_S(mK_S)) + h^1(\mathcal{O}_S(mK_S)) \ge \rchi(\mathcal{O}_S(mK_S)) = \rchi(\mathcal{O}_S) + \frac{m(m-1)}{2} K_S^2$$

이다. 이로써 부등식이 얻어진다.

등식이 성립하기 위해서는 추가적인 vanishing theorem이 필요하며, 이는 Kodaira vanishing theorem으로부터 얻어진다.

</details>

### 고다이라 임베딩정리

Kodaira vanishing의 가장 유명한 응용은 Kodaira embedding theorem이다.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7 (Kodaira embedding)**</ins> $$X$$를 smooth projective variety, $$\mathcal{L}$$을 ample line bundle이라 하자. 충분히 큰 $$k$$에 대해 $$\mathcal{L}^{\otimes k}$$는 very ample이다. 즉 $$\mathcal{L}^{\otimes k}$$는 $$X$$를 어떤 projective space로 embedding하는 linear system을 정의한다.

</div>

명제 7의 증명에서 Kodaira vanishing은 higher cohomology의 소멸을 통해 $$H^0(X, \mathcal{L}^{\otimes k})$$의 dimension을 계산하고, 이를 통해 sections가 base points를 갖지 않으며 separating property를 만족함을 보이는 데 사용된다. 이 정리는 ample line bundle의 존재가 projectivity를 보장함을 나타내며, algebraic geometry에서 기본적인 embedding 도구로 사용된다.

### very ampleness와 projective normality

Kodaira vanishing은 very ampleness와 projective normality를 판정할 때에도 핵심적인 역할을 한다. Line bundle $$\mathcal{L}$$이 very ample이려면 그 global sections가 임의의 두 점을 분리하고(separation of points), 임의의 점에서 tangent vectors를 분리(separation of tangent vectors)해야 한다. 이러한 성질들은 보통 cohomology long exact sequence를 통해 검증되며, 그 과정에서 $$H^1$$이 방해 요소로 등장한다.

구체적으로, $$\mathcal{L}$$이 ample이면 Kodaira vanishing은 $$H^i(X, \omega_X \otimes \mathcal{L}^{\otimes m}) = 0$$ ($$i > 0$$)을 보장하고, 이를 통해 충분히 큰 $$m$$에서 $$\mathcal{L}^{\otimes m}$$의 sections가 위의 separation 조건들을 만족함을 보일 수 있다. 이는 Kodaira embedding theorem의 증명에서 핵심적으로 사용되는 바이다. 더 나아가 $$\mathcal{L}^{\otimes m}$$이 very ample일 뿐만 아니라 그에 의한 embedding이 projectively normal이 되도록 하는 조건도, Kodaira vanishing을 통해 관련된 multiplication map

$$S^\mu H^0(X, \mathcal{L}^{\otimes m}) \longrightarrow H^0(X, \mathcal{L}^{\otimes \mu m})$$

의 surjectivity를 검증함으로써 얻을 수 있다. 이러한 vanishing은 higher cohomology가 sections의 생성을 방해하지 않음을 보장하여, linear system의 풍부함을 정량적으로 다룰 수 있게 한다.

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.

**[Laz]** R. Lazarsfeld, *Positivity in Algebraic Geometry I & II*, Ergebnisse der Mathematik, Springer, 2004.

**[DI]** P. Deligne, L. Illusie, *Relèvements modulo $$p^2$$ et décomposition du complexe de de Rham*, Inventiones Mathematicae, 1987.

**[Kod]** K. Kodaira, *On a differential-geometric method in the theory of analytic stacks*, Proceedings of the National Academy of Sciences, 1953.
