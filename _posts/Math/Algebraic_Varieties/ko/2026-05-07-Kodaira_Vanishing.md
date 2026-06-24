---
title: "고다이라 소멸정리"
description: "세르 소멸정리가 충분히 큰 차수에서만 코호몰로지 소멸을 보장하는 반면, 고다이라 소멸정리는 표준선다발과 충분한 선다발의 텐서 곱에 대해 모든 차수에서 높은 코호몰로지가 항상 사라짐을 보여준다. 대수기하학에서의 활용과 응용을 함께 살펴본다."
permalink: /ko/math/algebraic_varieties/kodaira_vanishing
excerpt: "Kodaira vanishing theorem과 그 응용"
categories: [Math / Algebraic Varieties]

sidebar:
    nav: "algebraic_varieties-ko"
    
date: 2026-05-07
weight: 17


---

[§사영공간의 코호몰로지, ⁋명제 4](/ko/math/algebraic_varieties/cohomology_of_projective_spaces#prop4)의 Serre vanishing theorem은 projective variety 위의 ample line bundle $$\mathcal{L}$$과 coherent sheaf $$\mathcal{F}$$에 대해, 충분히 큰 $$m$$에 대하여 $$H^i(X, \mathcal{F} \otimes \mathcal{L}^{\otimes m}) = 0$$ ($$i > 0$$)이 성립함을 보장한다. 그러나 이 결과는 단지 asymptotic한 성질에 불과하며, 구체적으로 어떤 $$m$$에서부터 vanishing이 시작되는지에 대해서는 아무 정보도 주지 않는다.

 Kodaira vanishing theorem은 이보다 훨씬 더 정교한 결과로, canonical bundle $$\omega_X$$와 ample line bundle $$\mathcal{L}$$의 tensor product $$\omega_X \otimes \mathcal{L}$$에 대해 higher cohomology가 *항상* 사라진다는 사실을 보장한다. 우리는 이 글에서 Kodaira vanishing theorem과 그 응용, 그리고 이 정리가 algebraic geometry에서 어떻게 활용되는지를 살펴 본다.

## 고다이라 소멸정리

우리가 다룰 기본적인 설정은 다음과 같다. $$X$$는 $$n$$차원 smooth projective variety이고, $$\mathcal{L}$$은 $$X$$ 위의 ample line bundle, $$\omega_X = \det \Omega_X^1 = \Omega_X^n$$은 canonical line bundle이다. ([§표준선다발, ⁋정의 5](/ko/math/algebraic_varieties/canonical_bundle#def5)) 그럼 Kodaira vanishing theorem은 다음과 같이 쓸 수 있다. 

<div class="proposition" markdown="1">

<ins id="prop1">**명제 1 (Kodaira vanishing)**</ins> $$n$$차원 smooth projective variety $$X$$, ample line bundle $$\mathcal{L}$$이 주어졌다 하자. 그럼 모든 $$p > 0$$에 대하여
 
$$H^p(X, \omega_X \otimes \mathcal{L}) = 0$$

이 성립한다. 더 일반적으로, $$p+q>n$$을 만족하는 $$p,q$$에 대하여

$$H^p(X, \Omega^q\otimes \mathcal{L})=0$$

이 성립한다. 

 </div>

첫째 주장은 둘째 주장에서 $$q=n$$으로 두어 얻어지는 것이다. 이 명제에 대한 증명은 꽤나 기술적인 부분이 있어 이번 글에서는 이를 엄밀하게 증명하기보다는 대수기하학에서 어떻게 사용되는지에 초점을 맞춘다. 

명제의 서술에서 알 수 있듯, Kodaira vanishing은 canonical bundle에 대한 twist 이후의 higher cohomology를 제거한다. Serre duality를 사용하면 이는 다음의 동치된 서술로 바꾸어 쓸 수 있다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> [명제 1](#prop1)의 가정 아래, 모든 $$p < n$$에 대하여

$$H^p(X, \mathcal{L}^{-1}) = 0$$

이 성립한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

[§세르 쌍대성](/ko/math/algebraic_varieties/serre_duality)의 Serre duality에 의해

$$H^p(X, \mathcal{L}^{-1}) \cong H^{n-p}(X, \omega_X \otimes \mathcal{L})^\vee$$

이 성립한다. $$p < n$$이면 $$n - p > 0$$이므로, [명제 1](#prop1)에 의해 우변은 $$0$$이다.

</details>

이 두 formulation은 위의 증명에서 살펴본 것과 같이 Serre duality를 통해 완전히 동치이므로 상황에 따라 더 편한 쪽을 사용하면 된다.

Kodaira vanishing이 가장 단순한 nontrivial한 예시를 제공하는 것은 projective space $$X = \mathbb{P}^n$$에서이다. 

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> 우리는 [§표준선다발, ⁋명제 7](/ko/math/algebraic_varieties/canonical_bundle#prop7)에서

$$\omega_{\mathbb{P}^n} \cong \mathcal{O}(-n-1)$$

임을 확인하였고, [§선다발과 벡터다발, ⁋예시 12](/ko/math/algebraic_varieties/line_bundles#ex12)에서 $$\mathbb{P}^n$$ 위의 임의의 line bundle은 $$\mathcal{O}(d)$$ 꼴임을 확인하였다. 이 중 $$d>0$$인 $$\mathcal{O}(d)$$들이 ample line bundle이다. 따라서, Kodaira vanishing은 다음의 vanishing

$$H^p(\mathbb{P}^n, \mathcal{O}(d - n - 1)) = 0$$

이 모든 $$d>0$$과 모든 $$i>0$$에 대해 성립함을 주장한다. 

우리는 [§사영공간의 코호몰로지, ⁋명제 1](/ko/math/algebraic_varieties/cohomology_of_projective_spaces#prop1)를 통해 모든 line bundle의 cohomology를 알고 있으므로 이를 직접 검증할 수 있다. 이에 따르면

$$H^q(\mathbb{P}^n, \mathcal{O}(k)) = \begin{cases}
\mathbb{K}[\x_0, \ldots, \x_n]_k & q = 0, k \geq 0 \\
\mathbb{K}[\x_0^{-1}, \ldots, \x_n^{-1}]_{-k-n-1} & q = n, k \leq -n-1 \\
0 & \text{otherwise}
\end{cases}$$

이며, 이로부터 자동으로 $$q\neq 0$$에 대해서는 모든 cohomology가 사라지므로 우리의 관심사는 $$q=n$$일 때 뿐이다. 이제 위의 식에 따르면 이것이 nonzero가 되기 위해서는 $$k\leq -n-1$$이 성립해야 한다. 그런데 우리 상황에서는 $$k=d-n-1$$이고 $$d>0$$이므로 이는 불가능하고, 따라서 Kodaira vanishing theorem을 다시 검증할 수 있다. 

</div>

## 고다이라 소멸정리의 응용

이제 우리는 앞서 예고한대로 Kodaira vanishing theorem의 응용을 살펴본다. 우선 앞선 글인 Riemann-Roch theorem에 따르면, surface $$S$$ 위의 divisor $$D$$에 대해

$$\rchi(\mathcal{O}_S(D)) = \frac{1}{2} D \cdot (D - K_S) + \rchi(\mathcal{O}_S)$$

를 준다. ([§곡면에서의 리만-로흐 정리, ⁋명제 4](/ko/math/algebraic_varieties/riemann_roch_surfaces#prop4)) 이 공식의 강력함은 $$\rchi$$를 순전히 대수적·위상적 데이터로 계산할 수 있다는 데 있지만, 문제는 $$\rchi$$가 $$h^0, h^1, h^2$$의 alternating sum이라는 점이다. 따라서 단순히 $$h^0(S, \mathcal{O}_S(D))$$만을 알고 싶을 때는 higher cohomology들의 값을 각각 따로 구해야 하므로, Riemann-Roch 공식만으로는 직접적인 답을 얻기 어렵다. 

이런 상황에서 Kodaira vanishing theorem을 사용하기 위해 $$\mathcal{L}\cong \mathcal{O}_S(L)$$이 ample line bundle라 하면, 우리는

$$\omega_S\otimes \mathcal{L}\cong \mathcal{O}_S(K_S+L)$$

임을 알고 있으며, 이를 위에 대입하면

$$\rchi(S, \omega_S \otimes \mathcal{L}) = h^0(S, \omega_S \otimes \mathcal{L})$$

를 얻고, 따라서 Riemann-Roch 공식의 우변을 계산하는 것만으로 곧바로 $$h^0(S, \omega_S \otimes \mathcal{L})$$를 얻을 수 있다. 

또 다른 활용은 plurigenus의 계산이다. Smooth projective variety $$X$$의 plurigenus $$P_m(X)$$는 geometric genus $$p_g(X)$$의 일반화로, surface의 birational invariant이다. ([§곡면에서의 리만-로흐 정리, ⁋정의 12](/ko/math/algebraic_varieties/riemann_roch_surfaces#def12)) Kodaira vanishing은 이들 불변량을 계산하는 데 직접적으로 사용될 수 있다.

가령 curve $$C$$의 경우 우리는 이들의 birational class가 genus에 의해 결정된다는 것을 알고 있으며, plurigenus $$P_m(g)$$는 $$g$$ (와 $$m$$)에 대한 함수로 주어진다. 즉 본질적으로 curve $$C$$에 대해서는 plurigenus가 흥미로운 불변량은 아니다. 이것이 흥미로운 경우는 surface 등의 고차원의 경우로, 여기서는 birational invariant가 하나의 숫자로 결정되는 것이 아니며 본격적으로 plurigenus 모두가 필요해진다. 

[§곡면에서의 리만-로흐 정리](/ko/math/algebraic_varieties/riemann_roch_surfaces)에서 보듯, surface $$S$$ 위의 divisor $$D$$에 대해 Riemann-Roch formula는

$$\rchi(\mathcal{O}_S(D)) = \frac{1}{2} D \cdot (D - K_S) + \rchi(\mathcal{O}_S)$$

으로 주어지며, plurigenera를 계산하기 위해 $$\omega_S^{\otimes m} \cong \mathcal{O}_S(mK_S)$$를 사용하여 $$D = mK_S$$를 대입하면

$$\rchi(\mathcal{O}_S(mK_S)) = \frac{m(m-1)}{2} K_S^2 + \rchi(\mathcal{O}_S)$$

이다. 그런데 만일 $$m \geq 2$$이고 $$K_S$$가 ample이면 $$(m-1)K_S$$도 ample이므로, $$mK_S = K_S + (m-1)K_S$$에 [명제 1](#prop1)의 Kodaira vanishing을 적용하여 $$h^1 = h^2 = 0$$을 얻는다. 따라서 이 formula로부터 직접 $$P_m(S) = h^0(S, \mathcal{O}_S(mK_S))$$를 계산할 수 있게 된다.

한편 이러한 경우 plurigenera의 식은 asymptotically 2차식인 것으로 생각할 수 있다. 이는 

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> Smooth projective variety $$X$$의 *Kodaira dimension<sub>고다이라 차원</sub>* $$\kappa(X)$$는 다음과 같이 정의된다. 모든 $$m \geq 1$$에 대해 $$P_m(X) = 0$$이면 $$\kappa(X) = -\infty$$이다. 그렇지 않은 경우, $$\kappa(X)$$는 $$P_m(X) = O(m^\kappa)$$를 만족하는 최소의 정수 $$\kappa \geq 0$$로 정의된다. 즉

$$\kappa(X) = \min\{k \in \mathbb{Z}_{\geq 0} : P_m(X) = O(m^k)\}$$

이다. 동등하게,

$$\kappa(X) = \limsup_{m \to \infty} \frac{\log P_m(X)}{\log m}$$

으로도 쓸 수 있다.

</div>

우리는 위의 계산으로부터, surface의 경우 $$\kappa \in \{-\infty, 0, 1, 2\}$$인 것을 안다. [Enriques–Kodaira classification](https://en.wikipedia.org/wiki/Enriques-Kodaira_classification)은 surface를 크게는 Kodaira dimension에 의해 분류하고, 여기에 $$\kappa=0$$과 $$\kappa=-\infty$$인 경우는 geometric genus $$p_g$$와 irregularity $$q$$를 사용하여 추가적인 세부 분류를 해 준다. 

우리는 [§선형계, ⁋정의 9](/ko/math/algebraic_varieties/linear_systems#def9)에서 line bundle $$\mathcal{L}$$이 very ample이라는 것은 complete linear system $$\lvert \mathcal{L} \rvert$$가 정의하는 사상 $$\varphi_{\mathcal{L}}: X \to \mathbb{P}(\Gamma(X, \mathcal{L}))$$이 closed embedding인 것으로 정의하였다. 당시에는 sheaf cohomology의 언어가 없었으나, 지금은 sheaf cohomology를 도입하였으므로 이를 조금 더 잘 사용할 수 있다. 

우선 very ample line bundle $$\mathcal{L}$$이 주어졌다 하고, 이로부터 정의되는 closed embedding $$\varphi_\mathcal{L}: X\rightarrow \mathbb{P}^N$$을 생각하자. 그럼 $$\varphi$$가 embedding인 것으로부터 $$\varphi_\mathcal{L}(p)\neq \varphi_\mathcal{L}(q)$$가 성립하는 것을 알고, 뿐만 아니라 $$\varphi_\mathcal{L}$$이 closed embedding이므로 $$d\varphi_\mathcal{L}$$이 injective이고, 따라서 cotangent space에서의 dual map $$\mathfrak{m}_{\varphi_{\mathcal{L}}(p)}/\mathfrak{m}_{\varphi_{\mathcal{L}}(p)}^2 \longrightarrow \mathfrak{m}_p/\mathfrak{m}_p^2$$은 surjective이다. 이로부터 다음의 두 결과가 성립함을 안다. 

1. *$$\varphi_\mathcal{L}$$ separates points.* 즉, 임의의 두 서로 다른 closed point $$p, q \in X$$에 대하여, $$s(p) = 0$$이고 $$s(q) \neq 0$$인 global section $$s \in H^0(X, \mathcal{L})$$가 존재한다.
2. *$$\varphi_\mathcal{L}$$ separates tangent vectors.* 즉, 임의의 closed point $$p \in X$$에 대하여, $$p$$에서 vanish하는 sections의 모음 $$\{ s \in H^0(X, \mathcal{L}) : s(p) = 0 \}$$가 cotangent space에 대응하는 벡터공간 $$\mathfrak{m}_p\mathcal{L}_p / \mathfrak{m}_p^2\mathcal{L}_p$$를 span한다.

첫 번째 조건은 evaluation map

$$H^0(X, \mathcal{L}) \longrightarrow \mathcal{L}_p \oplus \mathcal{L}_q$$

이 surjective임을 의미하고, 두 번째 조건은 $$p$$에서 vanish하는 sections들에 의한 restriction map

$$\{s \in H^0(X, \mathcal{L}) : s(p) = 0\} \longrightarrow \mathfrak{m}_p\mathcal{L}_p / \mathfrak{m}_p^2\mathcal{L}_p$$

의 image가 전체 $$\mathfrak{m}_p\mathcal{L}_p / \mathfrak{m}_p^2\mathcal{L}_p$$를 span함을 의미한다. 어렵지 않게 이들의 반대방향 또한 성립한다는 것을 확인할 수 있다. 즉 다음이 성립한다. 

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> Projective variety $$X$$ 위의 line bundle $$\mathcal{L}$$에 대해, $$\mathcal{L}$$이 very ample인 것은 위의 두 가지 separation 조건을 동시에 만족하는 것과 동치이다.

</div>

이제 이러한 separation 조건들이 cohomology를 통해 검증되는 방식을 살펴 보자. 먼저 (1)의 경우, 두 점 $$p \neq q$$를 포함하는 closed subvariety $$Z = \{p\} \cup \{q\}$$를 생각하면, $$Z$$를 정의하는 ideal sheaf $$\mathcal{I}_Z$$에 대해 short exact sequence

$$0 \longrightarrow \mathcal{I}_Z \otimes \mathcal{L}^{\otimes m} \longrightarrow \mathcal{L}^{\otimes m} \longrightarrow \mathcal{L}^{\otimes m} \otimes \mathcal{O}_Z \longrightarrow 0$$

을 얻는다. 여기서 $$\mathcal{L}^{\otimes m} \otimes \mathcal{O}_Z$$는 $$Z$$ 위의 line bundle이고,

$$H^0(Z, \mathcal{L}^{\otimes m}\rvert_Z) \cong \mathcal{L}^{\otimes m}_p \oplus \mathcal{L}^{\otimes m}_q$$

이다. 이로부터 유도되는 long exact sequence

$$H^0(X, \mathcal{L}^{\otimes m}) \longrightarrow H^0(Z, \mathcal{L}^{\otimes m}\rvert_Z) \longrightarrow H^1(X, \mathcal{I}_Z \otimes \mathcal{L}^{\otimes m})$$

를 고려하면, 만약 $$H^1(X, \mathcal{I}_Z \otimes \mathcal{L}^{\otimes m}) = 0$$이면 evaluation map이 surjective가 되어 separation of points가 성립함을 알 수 있다.

마찬가지로 (2)의 경우, 점 $$p$$의 first infinitesimal neighborhood $$\operatorname{Spec}(\mathcal{O}_{X,p}/\mathfrak{m}_p^2)$$를 생각하여, $$\mathcal{I}_p$$를 $$p$$의 ideal sheaf라 할 때 short exact sequence

$$0 \longrightarrow \mathcal{I}_p^2 \otimes \mathcal{L}^{\otimes m} \longrightarrow \mathcal{L}^{\otimes m} \longrightarrow \mathcal{L}^{\otimes m} \otimes (\mathcal{O}_X / \mathcal{I}_p^2) \longrightarrow 0$$

에서 유도되는 long exact sequence

$$H^0(X, \mathcal{L}^{\otimes m}) \longrightarrow H^0(Z, \mathcal{L}^{\otimes m}\rvert_Z) \longrightarrow H^1(X, \mathcal{I}_p^2 \otimes \mathcal{L}^{\otimes m})$$

를 고려하면, $$H^1(X, \mathcal{I}_p^2 \otimes \mathcal{L}^{\otimes m}) = 0$$이면 separation of tangent vectors가 성립한다.

구체적으로, $$\mathcal{L}$$이 ample이면 Kodaira vanishing은 $$H^i(X, \omega_X \otimes \mathcal{L}^{\otimes m}) = 0$$ ($$i > 0$$)을 보장한다. 적절한 twist와 Serre duality를 사용하면 위의 $$H^1$$들 역시 vanishing하게 되어, 충분히 큰 $$m$$에서 $$\mathcal{L}^{\otimes m}$$의 sections가 위의 separation 조건들을 만족함을 보일 수 있다. 이는 [명제 6](#prop6)의 Kodaira embedding theorem의 증명에서 핵심적으로 사용되는 바이다. 더 나아가 $$\mathcal{L}^{\otimes m}$$이 very ample일 뿐만 아니라 그에 의한 embedding이 projectively normal이 되도록 하는 조건도, Kodaira vanishing을 통해 관련된 multiplication map

$$S^\mu H^0(X, \mathcal{L}^{\otimes m}) \longrightarrow H^0(X, \mathcal{L}^{\otimes \mu m})$$

의 surjectivity를 검증함으로써 얻을 수 있다. 이러한 vanishing은 higher cohomology가 sections의 생성을 방해하지 않음을 보장하여, linear system의 풍부함을 정량적으로 다룰 수 있게 한다.


## 고다이라 매장정리

Kodaira vanishing의 가장 유명한 응용은 Kodaira embedding theorem이다. 다만 이는 complex manifold의 영역으로 나가는 감이 있어 우리 글에서는 간단히만 소개한다. 우선 Compact complex manifold $$X$$가 **Kähler manifold**라는 것은, $$X$$ 위에 서로 호환되는 Riemannian metric, symplectic form, complex structure가 정의된 것이다. 이 때, Line bundle $$\mathcal{L}$$에 Hermitian metric $$h$$가 주어지면, 그 curvature form $$\Theta_h$$가 정의되며 $$\mathcal{L}$$이 **positive**라는 것은 $$\frac{i}{2\pi}\Theta_h$$가 positive definite $$(1,1)$$-form이 되는 것이다. 그럼 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6 (Kodaira embedding)**</ins> $$X$$를 compact Kähler manifold, $$\mathcal{L}$$을 positive line bundle이라 하자. 그럼 충분히 큰 $$k$$에 대해 $$\mathcal{L}^{\otimes k}$$는 very ample이며, 특히 $$\mathcal{L}$$은 ample line bundle이다. 따라서 $$X$$는 projective variety이다.

</div>

즉 이 명제를 사용하면 Kähler manifold가 projective variety가 되는 것을 보일 수 있다. 

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[Laz]** R. Lazarsfeld, *Positivity in Algebraic Geometry I & II*, Ergebnisse der Mathematik, Springer, 2004.  
**[Kod]** K. Kodaira, *On a differential-geometric method in the theory of analytic stacks*, Proceedings of the National Academy of Sciences, 1953.
