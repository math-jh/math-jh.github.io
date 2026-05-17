---
title: "Peterson Variety"
excerpt: "Dale Peterson의 정리를 중심으로 Peterson variety와 quantum cohomology 사이의 동형을 소개하고, 그 직관적 의미를 해석한다"

categories: [Math / Lie Theory]
permalink: /ko/math/lie_theory/peterson_variety
sidebar: 
    nav: "Lie_theory-ko"

header:
    overlay_image: /assets/images/Math/Mirror_Symmetry/Peterson_Variety.png
    overlay_filter: 0.5

date: 2025-01-06
last_modified_at: 2025-01-06
weight: 7

published: false
---

본 글은 Lie theory 시리즈의 일부이다. flag variety $$X = G/P$$의 quantum cohomology는 Gromov-Witten invariant를 통해 정의되는 풍부한 대수적 구조이다. 그러나 이 ring의 명시적 표현을 얻는 일은 일반적으로 매우 어렵다. Dale Peterson은 1990년대에 이 문제에 대한 놀라운 해답을 제시하였는데, 그는 quantum cohomology ring $$qH^\ast(G/P)$$가 특정 affine variety의 coordinate ring과 동형임을 발견하였다. 이 variety가 바로 Peterson variety이며, 이 동형은 Lie theory의 기하학과 enumerative geometry의 만남을 보여주는 대표적인 예이다.

본 글에서는 Peterson variety의 정의와 Dale Peterson의 정리를 소개한 뒤, 이 동형이 갖는 기하학적 의미를 직관적으로 해석한다. 우리는 [\[Mirror Symmetry\] \S Mirror Symmetry 개요](/ko/math/mirror_symmetry/overview)에서 quantum cohomology의 개념을, [\[§Bruhat decomposition과 parabolic subgroup\]](/ko/math/lie_theory/bruhat_decomposition)과 [\S Richardson Variety](/ko/math/lie_theory/richardson_variety)에서 flag variety의 combinatorial structure를 살펴 보았으므로, 이러한 맥락 위에서 Peterson variety의 역할을 이해할 것이다.

## Peterson variety의 정의

우리는 complex semisimple Lie algebra $$\mathfrak{g}$$와 그에 대응하는 simply-connected algebraic group $$G$$를 고정한다. $$B \subset G$$를 Borel subgroup, $$B_- \subset G$$를 opposite Borel subgroup이라 하며, 이들의 Lie algebra를 각각 $$\mathfrak{b}$$, $$\mathfrak{b}_-$$로 표기한다. 또한 $$\mathfrak{n} = [\mathfrak{b}, \mathfrak{b}]$$와 $$\mathfrak{n}_- = [\mathfrak{b}_-, \mathfrak{b}_-]$$를 각각 positive, negative nilpotent subalgebra라 한다.

regular nilpotent element $$e \in \mathfrak{g}$$는 adjoint action $$\operatorname{ad}_e$$의 kernel이 가능한 한 작게 되는 nilpotent element이다. 구체적으로, $$\mathfrak{g}$$의 root space decomposition

$$\mathfrak{g} = \mathfrak{h} \oplus \bigoplus_{\alpha \in \Phi} \mathfrak{g}_\alpha$$

를 고려할 때, $$e$$는 각 simple root $$\alpha_i$$에 대해 $$0 \neq e_i \in \mathfrak{g}_{\alpha_i}$$를 선택하여 $$e = \sum_{i} e_i$$로 주어진다. 이러한 $$e$$는 unique up to conjugation이며, 그 centralizer $$\mathfrak{z}_{\mathfrak{g}}(e)$$는 $$\dim \mathfrak{z}_{\mathfrak{g}}(e) = \operatorname{rank}(\mathfrak{g})$$를 만족한다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> $$R = G/B_-$$를 full flag variety의 opposite version이라 하고, $$F \in \mathfrak{g}^\ast$$를 dualized positive Chevalley generators의 합

$$F = e_1^\ast + e_2^\ast + \cdots + e_{n-1}^\ast$$

이라 하자 (이는 $$\mathfrak{g}^\ast$$에서의 *regular nilpotent*에 해당). Parabolic subgroup $$P \supseteq B$$에 대해, $$G/P$$의 *Peterson variety* $$Y_P^\circ \subseteq R$$는 다음과 같이 정의된다:

$$Y_P^\circ = \{\, gB_- \in R \;\mid\; g^{-1} \cdot F \in [\mathfrak{n}_-, \mathfrak{n}_-]^\perp \,\}.$$

여기서 $$g^{-1} \cdot F$$는 $$G$$의 $$\mathfrak{g}^\ast$$에 대한 coadjoint action, $$[\mathfrak{n}_-, \mathfrak{n}_-]^\perp \subseteq \mathfrak{g}^\ast$$는 derived subalgebra의 annihilator이다.

</div>

이 정의는 표준 Peterson variety가 flag variety의 *부분다양체*로 등장한다는 사실을 반영한다. $$P = B$$인 full flag 경우는 Kostant–Peterson의 원래 정의이며 ([Pet], [Rie]), 일반 $$P$$에 대해서는 Marsh-Rietsch [MR]의 일반화에 해당한다. $$F$$가 regular nilpotent이고 그 centralizer가 $$\dim = \operatorname{rank}(\mathfrak{g})$$의 abelian subalgebra가 된다는 Kostant의 정리가 본 정의의 기하학적 차원을 결정한다.

동치인 표현으로, $$\mathfrak{n}^-$$의 적절한 affine chart 위에서 $$Y_P^\circ$$는 *Hessenberg variety*의 한 예시 (regular nilpotent Hessenberg variety with Hessenberg space $$\mathfrak{b} \oplus \bigoplus_i \mathbb{C} f_i$$)로 기술된다. 이는 Insko-Tymoczko 등의 후속 work에서 활용된다.

## Quantum cohomology의 generator와 relation

$$X = G/P$$의 quantum cohomology $$qH^\ast(X)$$를 이해하기 위해, 먼저 classical cohomology $$H^\ast(X, \mathbb{C})$$를 복습한다. Schubert calculus에 의해 $$H^\ast(X, \mathbb{C})$$는 Schubert class $$\sigma^w$$들에 의해 생성되며, 이들 사이의 곱셈은 Schubert structure constants로 결정된다. 여기서 $$w$$는 Weyl group $$W$$의 element 중에서 $$P$$에 대한 minimal coset representative를 나타낸다.

quantum cohomology는 이 classical 구조에 quantum parameter $$q$$를 도입하여 deformation한 것이다. small quantum cohomology ring $$qH^\ast(X)$$는 $$\mathbb{C}[q] = \mathbb{C}[q_1, \ldots, q_r]$$-module로서

$$qH^\ast(X) \cong \mathbb{C}[q] \otimes_{\mathbb{C}} H^\ast(X, \mathbb{C})$$

이 성립한다. 여기서 $$r$$은 $$P$$가 maximal parabolic인 경우의 개수와 관련되며, 각 $$q_i$$는 $$H_2(X, \mathbb{Z})$$의 적절한 basis에 대응한다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> (Ciocan-Fontanine, Givental-Kim). type A full flag variety $$Fl(\mathbb{C}^n) = GL_n(\mathbb{C})/B$$의 quantum cohomology ring은 다음과 같이 generator와 relation으로 표현된다.

$$qH^\ast(Fl(\mathbb{C}^n))$$은 변수 $$\x_1, \ldots, \x_n$$과 $$q_1, \ldots, q_{n-1}$$에 대한 quotient ring

$$qH^\ast(Fl(\mathbb{C}^n)) \cong \mathbb{C}[\x_1, \ldots, \x_n, q_1, \ldots, q_{n-1}] / I^{\text{quant}}$$

로 주어지며, 여기서 $$I^{\text{quant}}$$는 quantized elementary symmetric polynomial들에 의해 생성되는 ideal이다. 구체적으로, tridiagonal matrix

$$\tilde{M}_n = \begin{pmatrix} \x_1 & q_1 & 0 & \cdots & 0 \\ -1 & \x_2 & q_2 & \ddots & \vdots \\ 0 & \ddots & \ddots & \ddots & 0 \\ \vdots & \ddots & -1 & \x_{n-1} & q_{n-1} \\ 0 & \cdots & 0 & -1 & \x_n \end{pmatrix}$$

의 characteristic polynomial 계수들이 0이 되는 관계식들로 생성된다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Givental과 Kim은 flag variety의 quantum cohomology를 Toda lattice의 spectral curve와 연결하였다. 핵심 아이디어는 Schubert class $$\sigma^{s_i}$$를 generator로 하는 quantum cohomology ring의 관계식이, Toda Hamiltonian의 spectral problem에서 자연스럽게 얻어진다는 점이다. Ciocan-Fontanine은 이를 algebraically 완성하여 quantized elementary symmetric polynomial의 vanishing ideal로 quantum cohomology를 기술하였다. 구체적으로 tridiagonal matrix $$\tilde{M}_n$$의 characteristic polynomial은 Toda lattice의 Lax operator와 직접 대응하며, 이 계수들이 0이 되는 조건은 quantum correction을 포함한 Schubert calculus의 관계식을 완전히 encoding한다. 자세한 내용은 [CF], [GK]를 참조한다.

</details>

위 명제에서 $$q_i = 0$$으로 specialization하면 classical cohomology $$H^\ast(Fl(\mathbb{C}^n))$$의 well-known presentation이 복원됨을 확인할 수 있다. 즉 quantum parameter $$q_i$$가 0으로 가면 classical limit으로 돌아간다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> (Quantum Chevalley formula). $$X = G/P$$의 quantum cohomology에서 simple root $$\alpha$$에 대응하는 divisor class $$\sigma^{s_\alpha}$$와 임의의 Schubert class $$\sigma^w$$의 quantum product는

$$\sigma^{s_\alpha} \star \sigma^w = \sum_{w', \beta} c_{w', \beta} \sigma^{w'} q^\beta$$

로 주어진다. 여기서 우변의 합은 classical term과 quantum correction term으로 이루어지며, quantum correction은 degree $$\beta \in H_2(X, \mathbb{Z})$$를 갖는 rational curve들의 기여를 반영한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Quantum Chevalley formula는 classical Chevalley formula의 자연스러운 양자화이다. Classical 설정에서는 divisor class $$\sigma^{s_\alpha}$$와 Schubert class $$\sigma^w$$의 곱이 Bruhat order 위로 주어지는 명시적 합으로 표현된다. Quantum setting에서는 이 classical term에 더해, degree $$\beta > 0$$인 rational curve의 기여가 추가된다. 이 quantum correction term의 계수는 3-point Gromov-Witten invariant $$\langle \sigma^{s_\alpha}, \sigma^w, \sigma_{w'} \rangle_\beta$$로 주어지며, 이는 degree $$\beta$$의 rational curve가 주어진 Schubert variety들과 만나는 횟수를 센다. Fulton과 Woodward는 이 formula가 quantum cohomology ring의 generator와 relation을 완전히 결정함을 보였다. 자세한 내용은 [CF]를 참조한다.

</details>

quantum Chevalley formula의 정확한 계수 $$c_\beta$$는 Gromov-Witten invariant를 통해 결정되며, 일반적으로 이를 직접 계산하는 일은 매우 어렵다. 그러나 이 formula는 quantum cohomology의 곱셈구조를 완전히 결정하는데, 이는 divisor class가 generator로서 $$qH^\ast(X)$$를 생성하기 때문이다.

## Dale Peterson의 정리

Dale Peterson의 핵심 발견은 다음과 같다. Peterson variety $$Y_P^\circ$$의 coordinate ring이 $$G/P$$의 quantum cohomology ring과 동형이다. 이 동형은 단순한 차원의 일치를 넘어서, Schubert class와 regular function 사이의 명시적 대응을 제공한다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> (Dale Peterson). $$G$$를 complex semisimple algebraic group, $$P \subset G$$를 parabolic subgroup이라 하자. Peterson variety $$Y_P^\circ \subset \mathfrak{n}^-$$에 대해, 그 coordinate ring $$\mathbb{C}[Y_P^\circ]$$는 $$X = G/P$$의 quantum cohomology ring $$qH^\ast(X, \mathbb{C})[q^{-1}]$$과 isomorphic하다. 즉,

$$\mathbb{C}[Y_P^\circ] \cong qH^\ast(X, \mathbb{C})[q^{-1}]$$

이 성립한다. 여기서 $$[q^{-1}]$$은 모든 quantum parameter $$q_i$$를 invert시킨 localized ring을 의미한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Peterson isomorphism의 핵심 아이디어는 quantum cohomology ring의 Schubert basis가 Peterson variety 위의 regular function으로 표현될 수 있다는 점이다. Peterson은 full flag variety의 opposite 버전 $$R = G/B_-$$ 위에 $$Y_P^\circ$$를 정의하고, coadjoint action을 이용하여 $$Y_P^\circ$$의 coordinate ring이 quantum cohomology와 동형임을 보였다. 이 증명은 Langlands dual group $$G^\vee$$의 Toda lattice integrable system과의 연결을 핵심적으로 사용하며, quantum parameter $$q_i$$는 $$Y_P^\circ$$ 위의 regular function으로 해석된다. Rietsch는 type A의 경우 이 동형이 explicit하게 주어짐을 보였으며, 최근 Lam-Shimozono와 others는 equivariant setting으로 확장하였다. 자세한 내용은 [Pet], [Rie]를 참조한다.

</details>

이 동형을 **Peterson isomorphism**이라 부른다. 위 명제에서 coordinate ring $$\mathbb{C}[Y_P^\circ]$$는 possibly non-reduced sense로 이해할 수 있으나, type A의 경우에는 $$Y_P^\circ$$가 reduced variety가 되어 reduced coordinate ring을 사용할 수 있다.

명제 4의 중요한 특징은 **좌변이 순수하게 Lie-theoretic 객체이며, 우변이 순수하게 enumerative-geometric 객체**라는 점이다. Peterson variety는 Lie algebra $$\mathfrak{g}$$의 nilpotent cone 근처에서 자연스럽게 정의되는 객체인 반면, quantum cohomology는 holomorphic curve의 개수를 세는 Gromov-Witten theory에서 비롯된다. 이 두 세계가 동일한 대수적 구조를 갖는다는 사실은 매우 비직관적이다.

## 동형의 직관적 의미

Peterson isomorphism $$\mathbb{C}[Y_P^\circ] \cong qH^\ast(X)$$가 갖는 기하학적 의미를 여러 관점에서 해석할 수 있다.

**첫째, deformation theory의 관점이다.** Classical cohomology $$H^\ast(X)$$는 $$X$$의 linearized geometric information을 담고 있다. Quantum cohomology는 이에 quantum correction을 가하여 deformation한 구조이며, 이 deformation의 방향과 크기는 $$X$$ 안의 holomorphic curve들이 결정한다. 한편 Peterson variety $$Y_P^\circ$$는 nilpotent cone의 특정한 slice로 볼 수 있으며, 이 slice의 기하학은 $$G/P$$의 combinatorics와 밀접하게 연결된다. Peterson isomorphism은 이 deformation이 Lie algebra의 representation theory에 내재되어 있음을 보여준다.

**둘째, mirror symmetry의 관점이다.** [\[Mirror Symmetry\] \S Mirror Symmetry 개요](/ko/math/mirror_symmetry/overview)에서 우리는 A-model의 quantum cohomology $$QH^\ast(X)$$가 B-model의 Jacobi ring $$\operatorname{Jac}(W)$$와 동형임을 살펴 보았다. Peterson variety는 이 mirror symmetry의 또 다른 면모를 드러낸다. $$Y_P^\circ$$ 위에는 natural한 superpotential $$W$$가 존재하며, Peterson variety의 특정 stratum은 $$W$$의 critical locus와 동형이 된다. 따라서 Peterson isomorphism은

$$qH^\ast(X) \cong \mathbb{C}[Y_P^\circ] \cong \operatorname{Jac}(W)$$

의 연쇄를 형성하여, A-model과 B-model 사이의 대응을 Lie-theoretic 언어로 재구성한다.

**셋째, integrable system의 관점이다.** Quantum cohomology ring에는 commutative differential operator들의 체계, 즉 quantum integrable system이 내재되어 있다. Peterson variety 위의 regular function들은 이 operator들의 동시 고유함수로 작용하며, $$Y_P^\circ$$의 점들은 고유값을 parameterize한다. 이는 quantum cohomology의 곱셈연산자들을 동시 대각화하는 문제를 기하학적으로 해석한 것이다.

## Strata와 quantum parameter의 대응

Peterson variety $$Y_P^\circ$$는 자연스러운 stratification을 갖는다. 이 stratification은 $$G/P$$의 Schubert decomposition과 대응하며, 각 stratum은 특정한 quantum parameter $$q$$의 값과 관련된다.

구체적으로, Peterson variety는 Bruhat decomposition의 dual 버전과 유사한 방식으로 decompose된다. $$Y_P^\circ$$의 각 stratum $$Y_{P,w}^\ast$$는 Weyl group element $$w$$에 의해 인덱싱되며, 이 stratum의 coordinate ring은 quantum cohomology에서 특정한 localization을 취한 것과 동형이 된다.

특히 중요한 것은 open stratum $$Y_{P, e}^\ast$$이다. 여기서 $$e$$는 identity element를 의미하며, 이 stratum은 $$Y_P^\circ$$의 가장 큰 Zariski open subset이다. Rietsch의 결과에 따르면, 이 open stratum의 coordinate ring $$\mathbb{C}[Y_{P,e}^\ast]$$는 localized quantum cohomology $$qH^\ast(X)_{\text{loc}}$$와 동형이며, 이는 Marsh-Rietsch의 Grassmannian mirror symmetry construction의 출발점이 된다.

quantum parameter $$q$$는 Peterson variety 위에서 geometric morphism로 해석될 수 있다. 명제 4의 동형 아래에서 $$q$$에 해당하는 regular function은 유한사상

$$q: Y_P^\circ \longrightarrow (\mathbb{C}^\ast)^r$$

을 정의하며, 여기서 $$r$$은 quantum parameter의 개수이다. 이 사상의 fiber는 특정한 $$q$$ 값을 고정했을 때의 Peterson variety를 주며, 이는 quantum cohomology의 특정한 specialization과 대응한다. 특히 $$q \to 0$$이 classical limit이며, $$q=1$$은 특수한 값으로 Gromov-Witten invariant를 직접 계산할 때 나타난다.

## 향후 방향

Peterson variety와 quantum cohomology의 동형은 Grassmannian mirror symmetry의 핵심 building block이다. Marsh와 Rietsch는 이 동형을 확장하여, Grassmannian $$\operatorname{Gr}(k, n)$$의 mirror Landau-Ginzburg model을 명시적으로 구성하였다. 그들의 construction에서는 Peterson variety의 open stratum이 mirror dual space의 일부로 등장하며, superpotential $$W$$는 Lie-theoretic data로부터 자연스럽게 정의된다.

이러한 결과는 Lie theory와 enumerative geometry 사이의 깊은 연결을 보여주며, 특히 Langlands duality의 관점에서 풍부한 해석을 허용한다. Peterson scheme의 정의를 Langlands dual group $$G^\vee$$로 확장하면, equivariant quantum cohomology까지 포괄하는 더 일반적인 동형을 얻을 수 있다. 이 방향의 최근 결과는 Peterson의 원래 발견이 갖는 힘과 범용성을 다시 한번 확인시켜 준다. Peterson stratification에 나타나는 Schubert variety의 특이점 정보는 [§Kazhdan–Lusztig polynomial](/ko/math/lie_theory/kazhdan_lusztig)을 통해 조합적으로 인코딩되며, quantum Schubert positivity의 일부 측면은 KL theory의 양성과 관련된다.

---

**참고문헌**

**[CF]** I. Ciocan-Fontanine, *On quantum cohomology rings of partial flag varieties*, Duke Math. J. **98** (1999), no. 3, 485--524.

**[GK]** A. Givental, B. Kim, *Quantum cohomology of flag manifolds and Toda lattices*, Comm. Math. Phys. **168** (1995), no. 3, 609--641.

**[Kos]** B. Kostant, *Flag manifold quantum cohomology, the Toda lattice, and the representation with highest weight $$\rho$$*, Selecta Math. (N.S.) **2** (1996), no. 1, 43--91.

**[MR]** R. J. Marsh, K. Rietsch, *The B-model connection and mirror symmetry for Grassmannians*, Adv. Math. **319** (2017), 352--416.

**[Pet]** D. Peterson, *Quantum cohomology of $$G/P$$*, Lecture notes, Massachusetts Institute of Technology, Spring 1997. (unpublished)

**[Rie]** K. Rietsch, *Mirror symmetry and Grassmannians*, in: *Trends in Mathematics*, Springer, 2019, 207--224.
