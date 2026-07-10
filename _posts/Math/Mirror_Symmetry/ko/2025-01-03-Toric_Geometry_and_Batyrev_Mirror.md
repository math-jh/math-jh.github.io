---
title: "Reflexive Polytope과 Batyrev Mirror"
description: "리플렉시브 폴리토프와 그 이중 폴리토프의 관계를 통해 배트레프 미러 구성이 토릭 기하학에서 칼라비-야우 다양체를 자연스럽게 만들어내는 원리를 소개하고, 구체적 계산 예시와 그래스만니안 미러 대칭과의 연결을 다룬다."
excerpt: "Reflexive polytope의 쌍대성으로부터 얻는 Calabi-Yau mirror pair"

categories: [Math / Mirror Symmetry]
permalink: /ko/math/mirror_symmetry/toric_geometry_batyrev
sidebar: 
    nav: "mirror_symmetry-ko"

date: 2025-01-03
weight: 2
published: false
---

Toric geometry에서 ([\[토릭 기하학\] §토릭 다양체의 정의, ⁋명제 8](/ko/math/toric_geometry/toric_varieties#prop8))에서 살펴 보았듯이, full-dimensional lattice polytope $$P$$의 normal fan $$\Sigma_P$$로부터 projective toric variety $$X_{\Sigma_P}$$를 구성할 수 있다. Batyrev는 이러한 toric variety의 특별한 경우, 즉 reflexive polytope이라는 조건 아래에서 두 개의 dual polytope으로부터 자연스럽게 mirror pair가 생겨남을 보였다. 본 글에서는 reflexive polytope과 그 dual의 정의를 소개하고, Batyrev mirror construction의 정수를 설명한다. 마지막으로 $$\mathbb{P}^2$$ 예제를 통해 이 construction이 실제로 어떻게 작동하는지를 구체적으로 계산하고, 이후 논의될 Grassmannian mirror symmetry와의 연결을 예고한다.

Reflexive polytope의 정의와 기본 성질은 ([\[토릭 기하학\] §파노 다양체, ⁋정의 1](/ko/math/toric_geometry/reflexive_polytope_fano#def1))에서 자세히 다루었으므로, 여기서는 그 결과를 바탕으로 Batyrev mirror construction을 설명한다. 핵심 사실은 reflexive polytope $$\Delta \subset M_{\mathbb{R}}$$와 그 dual $$\Delta^\circ \subset N_{\mathbb{R}}$$가 서로 쌍대 관계를 이루며, 그 normal fan으로부터 정의되는 toric variety $$X_\Delta$$, $$X_{\Delta^\circ}$$가 각각 Gorenstein Fano variety가 된다는 것이다.

## Batyrev mirror construction

Reflexive polytope $$\Delta \subset M_{\mathbb{R}}$$로부터 toric variety $$X_\Delta = X_{\Sigma_\Delta}$$가 Gorenstein Fano variety로 정의된다 ([\[토릭 기하학\] §파노 다양체, ⁋명제 4](/ko/math/toric_geometry/reflexive_polytope_fano#prop4)). 그 anticanonical divisor $$-K_{X_\Delta}$$의 global section은 $$\Delta$$의 lattice points $$\Delta \cap M$$에 의해 indexing된다 ([\[토릭 기하학\] §파노 다양체, ⁋명제 5](/ko/math/toric_geometry/reflexive_polytope_fano#prop5)).

::: 정의 1
Reflexive polytope $$\Delta \subset M_{\mathbb{R}}$$에 대하여, $$\Delta$$의 lattice points $$\Delta \cap M = \{m_0, \ldots, m_s\}$$를 이용하여 다음의 *general anticanonical section*을 정의한다.

$$f_\Delta(\x) = \sum_{i=0}^{s} c_i \x^{m_i} \in \mathbb{C}[M]$$

여기서 $$c_i \in \mathbb{C}$$는 일반적인 계수이고, $$\x^{m_i}$$는 character $$\chi^{m_i} : T_N \to \mathbb{C}^\ast$$에 해당하는 monomial이다. $$f_\Delta = 0$$으로 정의되는 $$T_N$$의 부분다양체를 *ambient* $$X_\Delta$$ 안으로 취한 closure를 $$Y_\Delta$$라 하면, 일반적인 $$c_i$$에 대해 $$Y_\Delta$$는 ($$n-1$$이 충분히 작거나 crepant resolution 후) *Calabi-Yau variety<sub>칼라비-야우 다양체</sub>*가 된다.
:::

Batyrev의 핵심 관찰은 다음과 같다. $$\Delta$$가 reflexive이면 $$\Delta^\circ$$ 또한 reflexive이므로, 동일한 construction을 $$\Delta^\circ$$에 대해 반복하여 mirror Calabi-Yau $$Y$$를 얻는다. 즉 $$\Delta^\circ$$의 lattice points로부터 toric variety $$X_\Delta$$ 위의 anticanonical section을 정의하고, 그 zero locus를 취한다.

::: 명제 2 (Batyrev mirror symmetry)
$$\dim X_\Delta = n \ge 4$$이고 $$\Delta$$가 reflexive polytope라 하자. $$\Delta$$와 그 dual $$\Delta^\circ$$로부터 (필요시 crepant resolution을 거쳐) 얻어지는 Calabi-Yau pair $$(Y_\Delta, Y_{\Delta^\circ})$$의 *stringy* Hodge number는 다음 mirror symmetry를 만족한다:

$$h^{1,1}_{\mathrm{st}}(Y_\Delta) = h^{n-2,1}_{\mathrm{st}}(Y_{\Delta^\circ}), \qquad h^{n-2,1}_{\mathrm{st}}(Y_\Delta) = h^{1,1}_{\mathrm{st}}(Y_{\Delta^\circ}).$$

(Batyrev–Borisov 형태에서는 일반 $$h^{p,q}_{\mathrm{st}}(Y_\Delta) = h^{n-1-p,q}_{\mathrm{st}}(Y_{\Delta^\circ})$$로 확장됨.)
:::

::: 증명
면 $$\Theta$$ 위의 lattice points 개수를 $$l(\Theta)$$, 상대 내부 lattice points 개수를 $$l^\ast(\Theta)$$라 표기하자. Batyrev는 toric variety의 조합론적 성질을 이용하여 stringy Hodge number를 lattice point count로 직접 표현하였다:

$$h^{1,1}_{\mathrm{st}}(Y_\Delta) = l(\Delta^\circ) - 1 - n - \sum_{\operatorname{codim} \Theta^\circ = 1} l^\ast(\Theta^\circ) + \sum_{\operatorname{codim} \Theta^\circ = 2} l^\ast(\Theta^\circ) l^\ast(\Theta),$$

$$h^{n-2,1}_{\mathrm{st}}(Y_\Delta) = l(\Delta) - 1 - n - \sum_{\operatorname{codim} \Theta = 1} l^\ast(\Theta) + \sum_{\operatorname{codim} \Theta = 2} l^\ast(\Theta) l^\ast(\Theta^\circ).$$

$$\Delta$$와 $$\Delta^\circ$$의 역할을 바꾸면 두 식이 정확히 서로 swap되므로, 위 mirror symmetry가 따라온다. 자세한 유도는 [Bat]와 [CK, Theorem 4.1.5]를 참고한다.
:::

## $$\mathbb{P}^2$$ 예제

이제 $$\mathbb{P}^2$$를 toric variety로서 구체적으로 분석하고, 이로부터 reflexive polytope과 그 dual을 계산한다.

::: 예시 3
$$\mathbb{P}^2$$는 lattice $$N = \mathbb{Z}^2$$에서 다음의 세 ray

$$v_1 = (1,0), \qquad v_2 = (0,1), \qquad v_3 = (-1,-1)$$

로 생성되는 fan $$\Sigma$$에 의해 정의되는 toric variety이다. Maximal cone들은

$$\sigma_1 = \operatorname{Cone}(v_2, v_3), \qquad \sigma_2 = \operatorname{Cone}(v_1, v_3), \qquad \sigma_3 = \operatorname{Cone}(v_1, v_2)$$

이며, 각각 $$\mathbb{C}^2$$에 해당하는 affine chart를 준다. 이들은 $$\mathbb{P}^2$$의 표준적인 좌표차트 $$U_i = \{[x_0:x_1:x_2] \mid x_i \neq 0\}$$와 일치한다.
:::

$$\mathbb{P}^2$$의 fan $$\Sigma$$는 어떤 lattice polytope의 normal fan인가? $$N_{\mathbb{R}}$$에서 $$\Delta^\circ = \operatorname{Conv}\{(1,0), (0,1), (-1,-1)\}$$라 하자. 이 polytope의 각 면에 대응하는 inner normal vector를 계산하면 다음과 같다.

Facet $$\Theta_1 = \operatorname{Conv}\{(0,1), (-1,-1)\}$$를 생각하자. 이 edge를 포함하는 직선은 $$y = 2x + 1$$, 즉 $$2x - y = -1$$이다. 임의의 $$(x,y) \in \Delta^\circ$$에 대해 $$2x - y \ge -1$$를 확인할 수 있는데, $$(1,0)$$에서 $$2 > -1$$이고 $$(0,1), (-1,-1)$$에서는 등호가 성립한다. 따라서 $$\langle (x,y), (2,-1) \rangle = 2x - y = -1$$이 되며, 정수 벡터 $$(2,-1) \in N$$에 의해 $$\Theta_1$$가 정의된다.

Facet $$\Theta_2 = \operatorname{Conv}\{(1,0), (-1,-1)\}$$는 직선 $$x - 2y = 1$$ 위에 있다. 정수 벡터 $$(-1, 2) \in N$$에 대해 $$\langle (x,y), (-1, 2) \rangle = -x + 2y = -1$$이 되며, $$\Delta^\circ$$의 내부인 원점에서는 $$0 > -1$$이므로 이것이 inner normal direction임을 확인할 수 있다. 남은 점 $$(0,1)$$에 대해서는 $$\langle (0,1), (-1,2) \rangle = 2 > -1$$이므로 $$(-1,2)$$는 올바른 inner normal vector이다.

Facet $$\Theta_3 = \operatorname{Conv}\{(1,0), (0,1)\}$$는 직선 $$x + y = 1$$ 위에 있다. 정수 벡터 $$(-1,-1) \in N$$에 대해 $$\langle (x,y), (-1,-1) \rangle = -x-y = -1$$이 되어 역시 reflexive 조건을 만족한다.

원점 $$(0,0)$$은 $$\Delta^\circ$$의 내부에 있으므로, 위의 계산에 의해 $$\Delta^\circ$$는 reflexive polytope임을 확인할 수 있다. 이제 dual polytope $$\Delta$$를 계산한다.

$$\Delta = \{u \in M_{\mathbb{R}} \mid \langle u, v \rangle \ge -1 \text{ for all } v \in \Delta^\circ\}$$

각 꼭짓점 $$v \in \Delta^\circ$$에 대해 $$\langle u, v \rangle \ge -1$$를 적용하면:
- $$v = (1,0)$$: $$u_1 \ge -1$$
- $$v = (0,1)$$: $$u_2 \ge -1$$
- $$v = (-1,-1)$$: $$-u_1 - u_2 \ge -1$$, 즉 $$u_1 + u_2 \le 1$$

따라서 $$\Delta$$는 다음 부등식 시스템으로 정의된다.

$$\Delta = \{(u_1, u_2) \in M_{\mathbb{R}} \mid u_1 \ge -1, \; u_2 \ge -1, \; u_1 + u_2 \le 1\}$$

$$\Delta$$의 꼭짓점은 이들 직선의 교점들이므로 $$(-1,-1), (2,-1), (-1,2)$$이다. $$\Delta$$ 위의 lattice points를 세면:

- $$u_1 = -1$$: $$u_2 = -1, 0, 1, 2$$ (4점)
- $$u_1 = 0$$: $$u_2 = -1, 0, 1$$ (3점)
- $$u_1 = 1$$: $$u_2 = -1, 0$$ (2점)
- $$u_1 = 2$$: $$u_2 = -1$$ (1점)

따라서 $$l(\Delta) = 10$$이다. 한편 $$\Delta^\circ$$의 lattice points는 꼭짓점 $$(1,0), (0,1), (-1,-1)$$과 원점 $$(0,0)$$뿐이므로 $$l(\Delta^\circ) = 4$$이다.

$$\Delta$$의 facets는 $$u_1 = -1$$, $$u_2 = -1$$, $$u_1 + u_2 = 1$$이며, 이들의 primitive inner normal vectors는 각각 $$(1,0), (0,1), (-1,-1)$$이다. 따라서 $$\Delta$$의 normal fan은 ray generator들이 $$(1,0), (0,1), (-1,-1)$$인 fan으로, 이는 $$\mathbb{P}^2$$의 standard fan이다. 즉 ambient $$X_\Delta \cong \mathbb{P}^2$$. 반면 $$\Delta^\circ$$의 normal fan을 계산하면 ray들이 $$(2,-1), (-1,2), (-1,-1)$$이 되어 ($$\mathbb{P}^2$$의 fan과 lattice-동형이 아니며, 인접 두 ray의 determinant가 $$\pm 3$$이다), $$X_{\Delta^\circ}$$는 세 점에 $$\mathbb{Z}/3$$ 특이점을 갖는 singular Gorenstein Fano surface가 된다. ([\[토릭 기하학\] §파노 다양체, ⁋예시 6](/ko/math/toric_geometry/reflexive_polytope_fano#ex6)에서 같은 reflexive pair를 다룬다.)

$$n=2$$인 경우 anticanonical hypersurface $$Y_\Delta \subset X_\Delta = \mathbb{P}^2$$는 일반적으로 차원 $$1$$의 smooth genus-$$1$$ curve (elliptic curve)가 된다 (anticanonical class $$-K_{\mathbb{P}^2} = \mathcal{O}(3)$$의 generic section은 cubic curve이며 generic이면 smooth). Mirror 측 $$Y_{\Delta^\circ}$$도 적절한 crepant resolution 후 genus-$$1$$ curve가 된다. 1차원 Calabi-Yau에서 mirror symmetry는 $$g(Y_\Delta) = g(Y_{\Delta^\circ}) = 1$$로 trivial하게 표현되며, 본격적인 Batyrev mirror symmetry는 $$n \ge 4$$인 경우 (K3 surface, CY 3-fold 등)에 들어가서야 비자명한 의미를 가진다. 위의 명제 2 공식은 이 영역에서 적용되며, $$n=2$$에서는 substituting 후 자명한 항등식으로 환원된다.

## Grassmannian mirror symmetry로의 연결

Toric variety에 대한 Batyrev mirror construction은 조합론적 데이터의 쌍대성을 통해 mirror pair를 명시적으로 구성하는 아름다운 예시이다. 그러나 toric variety는 homogeneous space의 특별한 경우에 불과하며, 더 일반적인 공간으로의 확장은 비자명한 문제이다. 특히 Grassmannian $$\Gr(k, n)$$은 toric variety가 아니므로 Batyrev의 construction을 직접 적용할 수 없다.

([§거울대칭 개요](/ko/math/mirror_symmetry/overview))에서 살펴 보았듯이, toric variety의 mirror는 Landau-Ginzburg model $$(\bar{X}, W)$$의 형태를 띠며, 이는 charge matrix를 통해 구체적으로 기술된다. Grassmannian의 경우 Marsh와 Rietsch는 Plücker coordinate를 이용하여 이와 유사한 Landau-Ginzburg model을 구성하였고 ([§Marsh–Rietsch superpotential](/ko/math/mirror_symmetry/marsh_rietsch_superpotential)), 그 Jacobi ring이 quantum cohomology ring과 동형임을 보였다 ([§Marsh-Rietsch Mirror Theorem](/ko/math/mirror_symmetry/mr_mirror_theorem)). 이 construction은 toric case에서의 Batyrev mirror가 갖는 조합론적 투명성을 완전히 잃는 대신, Lie theory와 cluster algebra의 풍부한 구조를 대신 활용한다. Grassmannian mirror symmetry는 본 시리즈의 연구용 stream에 모아 두었으며, Bruhat decomposition, Richardson variety, Peterson variety 등의 Lie-theoretic 도구들이 본 글의 toric/Batyrev 흐름과 어떻게 차별화되는지 그 stream에서 다룬다. 그 stream은 거울 대칭의 우변에 해당하는 [§Grassmannian의 양자 코호몰로지](/ko/math/mirror_symmetry/quantum_cohomology_of_grassmannians)에서 출발하여, 거울 대칭이 Grassmannian을 넘어 그 안의 특이 Schubert variety로까지 확장되는 [§Schubert variety의 거울과 head-over-tails superpotential](/ko/math/mirror_symmetry/schubert_variety_mirror)에서 정점에 이른다.

---

**참고문헌**

**[Bat]** V. V. Batyrev, *Dual polyhedra and mirror symmetry for Calabi-Yau hypersurfaces in toric varieties*, J. Algebraic Geom. **3** (1994), 493--545.

**[CK]** D. A. Cox, S. Katz, *Mirror symmetry and algebraic geometry*, Mathematical Surveys and Monographs **68**, AMS, 1999.

**[CLS]** D. Cox, J. Little, H. Schenck, *Toric Varieties*, Graduate Studies in Mathematics **124**, AMS, 2011.

**[Ful]** W. Fulton, *Introduction to Toric Varieties*, Annals of Mathematics Studies **131**, Princeton University Press, 1993.
