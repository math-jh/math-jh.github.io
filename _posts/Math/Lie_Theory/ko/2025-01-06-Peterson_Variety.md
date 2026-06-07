---
title: "Peterson Variety"
description: "복소 반단순 대수군의 nilpotent cone과 flag variety를 잇는 Peterson variety는 정칙 멱영 원소가 결정하는 특수한 부분다양체로, 그 정의와 차원, 기본적 계층화를 다룬다."
excerpt: "Regular nilpotent element를 이용하여 정의되는 flag variety의 부분다양체 Peterson variety의 정의와 기본적인 기하학적 성질"

categories: [Math / Lie Theory]
permalink: /ko/math/lie_theory/peterson_variety
sidebar: 
    nav: "Lie_theory-ko"

date: 2025-01-06
last_modified_at: 2025-01-06
weight: 7

published: false
---

Complex semisimple algebraic group $$G$$의 nilpotent cone과 flag variety는 모두 $$G$$의 표현론과 기하학에서 핵심적인 대상이다. 이 둘은 *Springer fiber*, *Hessenberg variety* 등 다양한 형태로 서로 얽혀 등장하는데, 그 가운데 *Peterson variety*는 *regular nilpotent element*가 결정하는 한 가지 특별한 fiber에 해당한다. 본 글에서는 [§Borel subgroup과 flag variety](/ko/math/lie_theory/borel_subgroup)와 [§Bruhat decomposition과 parabolic subgroup](/ko/math/lie_theory/bruhat_decomposition)의 결과를 바탕으로 Peterson variety의 정의를 정확히 기술하고, 그 차원과 기본적인 stratification을 살펴 본다.

## Regular nilpotent element

우리는 complex semisimple Lie algebra $$\mathfrak{g}$$와 그에 대응하는 simply-connected algebraic group $$G$$를 고정한다. $$B \subset G$$를 Borel subgroup, $$B_- \subset G$$를 opposite Borel subgroup이라 하며, 이들의 Lie algebra를 각각 $$\mathfrak{b}$$, $$\mathfrak{b}_-$$로 표기한다. 또한 $$\mathfrak{n} = [\mathfrak{b}, \mathfrak{b}]$$와 $$\mathfrak{n}_- = [\mathfrak{b}_-, \mathfrak{b}_-]$$를 각각 positive, negative nilpotent subalgebra라 하고, [§근계](/ko/math/lie_theory/root_systems)에서의 root space decomposition

$$\mathfrak{g} = \mathfrak{h} \oplus \bigoplus_{\alpha \in \Phi} \mathfrak{g}_\alpha$$

를 가정한다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Nilpotent element $$e \in \mathfrak{g}$$가 *regular*라는 것은 그 centralizer $$\mathfrak{z}_{\mathfrak{g}}(e) = \{X \in \mathfrak{g} \mid [X, e] = 0\}$$의 차원이 $$\operatorname{rank}(\mathfrak{g})$$와 같은 것이다.

</div>

구체적으로, 각 simple root $$\alpha_i$$마다 $$0 \neq e_i \in \mathfrak{g}_{\alpha_i}$$를 하나씩 선택하여 

$$e = \sum_i e_i$$

으로 두면 이 $$e$$는 regular nilpotent이며, 모든 regular nilpotent는 $$G$$의 adjoint action에 의해 서로 conjugate하다. 이는 Kostant의 고전적인 결과이며, regular nilpotent의 centralizer가 abelian이고 그 차원이 정확히 $$\operatorname{rank}(\mathfrak{g})$$임을 함께 보여 준다.

## Peterson variety의 정의

이제 위에서 고정한 regular element $$e \in \mathfrak{g}$$를 이용하여 flag variety $$G/B$$의 한 부분다양체를 정의한다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> Parabolic subgroup $$P \supseteq B$$에 대하여, $$G/P$$의 *Peterson variety* $$Y_P^\circ$$는 $$R = G/B_-$$의 부분다양체

$$Y_P^\circ = \{\, gB_- \in R \;\mid\; \operatorname{Ad}^\ast(g^{-1}) \cdot F \in [\mathfrak{n}_-, \mathfrak{n}_-]^\perp \,\}$$

로 정의된다. 여기서 $$F = e_1^\ast + e_2^\ast + \cdots + e_{n-1}^\ast \in \mathfrak{g}^\ast$$는 dualized positive Chevalley generator들의 합 ($$\mathfrak{g}^\ast$$에서의 regular nilpotent에 해당), $$\operatorname{Ad}^\ast$$는 $$G$$의 coadjoint action, $$[\mathfrak{n}_-, \mathfrak{n}_-]^\perp \subseteq \mathfrak{g}^\ast$$는 derived subalgebra의 annihilator이다.

</div>

$$P = B$$일 때의 정의는 Kostant-Peterson의 원래 정의 [Pet]이며, 일반의 $$P$$에 대한 위의 형태는 후속 연구 [Rie]에서 표준적으로 사용되는 형태이다. 정의에서 $$F$$가 regular nilpotent이고 그 centralizer가 $$\operatorname{rank}(\mathfrak{g})$$차원의 abelian subalgebra가 된다는 Kostant의 정리가 $$Y_P^\circ$$의 기하학적 차원을 결정한다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> $$P = B$$인 경우, Peterson variety $$Y_B^\circ \subset G/B_-$$의 차원은 $$\operatorname{rank}(\mathfrak{g})$$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$F \in \mathfrak{g}^\ast$$를 regular nilpotent로 잡았으므로 Kostant의 정리에 의해 그 coadjoint stabilizer $$G_F = \{g \in G \mid \operatorname{Ad}^\ast(g) \cdot F = F\}$$의 connected component는 abelian이고 그 차원은 $$\operatorname{rank}(\mathfrak{g})$$이다. $$G/B_-$$를 $$G$$의 $$B_-$$ 위에서의 quotient로 생각하면, 정의에서 부과한 조건 $$\operatorname{Ad}^\ast(g^{-1}) \cdot F \in [\mathfrak{n}_-, \mathfrak{n}_-]^\perp$$은 $$\mathfrak{g}^\ast$$ 위의 codimension $$\dim[\mathfrak{n}_-, \mathfrak{n}_-]$$의 affine subspace를 자른다. 두 차원의 차이를 계산하면 정확히 $$\operatorname{rank}(\mathfrak{g})$$가 남는다. 자세한 dimension count는 [Pet], [Rie]를 참조한다.

</details>

이 차원 결과는 $$\operatorname{rank}(\mathfrak{g})$$가 simple root의 개수와 같다는 사실과 잘 맞물린다. 더 일반적인 parabolic $$P$$에 대해서도 비슷한 dimension formula가 성립하여, $$\dim Y_P^\circ$$는 $$G/P$$의 maximal parabolic factor의 수와 일치한다.

## Hessenberg variety로서의 기술

Peterson variety는 *Hessenberg variety*라 불리는 더 일반적인 부분다양체 집합의 특수한 예시로 기술될 수도 있다. Hessenberg variety의 정의는 다음과 같다.

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> $$X \in \mathfrak{g}$$와 $$\mathfrak{b}$$를 포함하는 $$\operatorname{ad}$$-stable subspace $$H \subseteq \mathfrak{g}$$ (즉 $$[\mathfrak{b}, H] \subseteq H$$)가 주어졌을 때, *Hessenberg variety*는

$$\mathcal{B}(X, H) = \{\, gB \in G/B \;\mid\; \operatorname{Ad}(g^{-1}) X \in H \,\}$$

로 정의된다.

</div>

$$X$$가 regular nilpotent이고 $$H = \mathfrak{b} \oplus \bigoplus_i \mathbb{C} f_i$$ (여기서 $$f_i \in \mathfrak{g}_{-\alpha_i}$$는 simple negative root vector)인 경우의 Hessenberg variety가 바로 위에서 정의한 Peterson variety의 affine chart에 해당한다. 이러한 Hessenberg variety의 관점은 $$Y_B^\circ$$를 $$\mathfrak{n}^-$$의 적절한 affine chart 위의 algebraic variety로 직접 기술할 수 있게 해 주며, Insko-Tymoczko 등의 후속 연구에서 활용된다.

## Stratification

Peterson variety는 자연스러운 stratification을 갖는다. $$Y_P^\circ$$의 각 stratum $$Y_{P,w}^\ast$$는 Weyl group element $$w$$에 의해 인덱싱되며, 이는 [§Bruhat decomposition과 parabolic subgroup, ⁋정리 14](/ko/math/lie_theory/bruhat_decomposition#thm14)의 Bruhat decomposition을 $$G/B_-$$로 옮긴 형태와 호환된다. 구체적으로

$$Y_P^\circ = \bigsqcup_{w \in W^P} Y_{P,w}^\ast,\qquad Y_{P,w}^\ast = Y_P^\circ \cap (B w B_-)/B_-$$

로 분해되며, 이 stratification은 본질적으로 Peterson variety가 어떤 Bruhat cell과 만나는가에 의해 결정된다.

특히 중요한 것은 open stratum $$Y_{P, e}^\ast$$이다. 여기서 $$e$$는 identity element를 의미하며, 이 stratum은 $$Y_P^\circ$$의 가장 큰 Zariski open subset이다. 이는 Big Bruhat cell $$B \cdot B_- / B_- \subset G/B_-$$와 Peterson variety의 교집합으로 주어지며, $$Y_P^\circ$$의 affine geometry를 분석할 때 표준적인 출발점이 된다.

이러한 stratification은 $$Y_P^\circ$$의 좌표환을 Weyl group에 의해 색인된 조각들의 합으로 분해할 수 있게 해 주며, Peterson variety의 $$T$$-fixed point set이 $$W^P$$와 자연스럽게 일대일대응됨을 함께 보여 준다.

---

**참고문헌**

**[Kos]** B. Kostant, *The principal three-dimensional subgroup and the Betti numbers of a complex simple Lie group*, Amer. J. Math. **81** (1959), 973--1032.

**[Pet]** D. Peterson, Lecture notes, Massachusetts Institute of Technology, Spring 1997 (unpublished).

**[Rie]** K. Rietsch, *Totally positive Toeplitz matrices and quantum cohomology of partial flag varieties*, J. Amer. Math. Soc. **16** (2003), 363--392.

**[IT]** E. Insko, J. Tymoczko, *Affine pavings of regular nilpotent Hessenberg varieties and intersection theory of the Peterson variety*, J. Combin. Theory Ser. A **187** (2022), 105572.
