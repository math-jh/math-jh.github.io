---
title: "Richardson Variety"
excerpt: "Schubert variety와 opposite Schubert variety의 교집합으로 정의되는 Richardson variety, 그리고 Marsh-Rietsch mirror B-model에서의 역할"

categories: [Math / Lie Theory]
permalink: /ko/math/lie_theory/richardson_variety
sidebar:
    nav: "lie_theory-ko"

header:
    overlay_image: /assets/images/Math/Mirror_Symmetry/Richardson_Variety.png
    overlay_filter: 0.5

date: 2025-01-05
last_modified_at: 2025-01-05
weight: 5
---

본 글은 Lie theory 시리즈의 일부이다. [§Bruhat Decomposition](/ko/math/lie_theory/bruhat_decomposition)에서 살펴 보았듯이, generalized flag variety $X = G/P$는 Bruhat cell들의 불연속합으로 분필된다. 각 Bruhat cell은 Borel subgroup $B$의 궤도이며, 그 Zariski closure인 Schubert variety는 $X$의 중요한 닫힌 부분다양체를 이룬다. 그러나 한쪽 방향의 궤도만으로는 $X$의 교차이론이나 대칭성을 충분히 기술할 수 없으며, 서로 다른 방향에서 오는 두 가지 셀 구조의 교차를 고려해야 할 때가 많다. Richardson variety는 바로 이러한 교차에 해당하는 대상으로, Schubert variety와 opposite Schubert variety의 교집합을 통해 정의된다. 본 글에서는 Richardson variety의 기본적인 정의와 성질, 특히 이것이 smooth affine variety가 되는 이유를 직관적으로 살펴 본 뒤, Grassmannian의 mirror symmetry에서 Marsh-Rietsch가 이를 B-model domain으로 활용하는 방식을 설명한다.

## Opposite Borel과 Opposite Bruhat Cell

우리는 앞으로 복소수체 $\bbC$ 위에서 연결된 반단순 대수군 $G$를 고정하고, 그 Borel subgroup을 $B$, 최대 토르스를 $T = B \cap B^-$로 한다. 여기서 $B^-$는 $B$와 반대되는 Borel subgroup, 즉 **opposite Borel**이다. 구체적으로 $B$가 upper triangular matrices로 주어진다면 $B^-$는 lower triangular matrices에 해당하며, $B \cap B^- = T$가 성립한다. Weyl군 $W = N_G(T)/T$의 원소 $w$에 대하여, [§Bruhat Decomposition, ⁋정의 16](/ko/math/lie_theory/bruhat_decomposition#def16)에서 정의한 Bruhat cell은 $B$의 궤도

$$X_w^\circ = BwP/P$$

로 주어졌다. 이와 대칭적으로 $B^-$의 궤도를 생각하면 다음과 같다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> $w \in W$에 대하여, 집합

$$X^w_\circ = B^- w P/P$$

를 **opposite Bruhat cell**이라 부른다. 이것의 Zariski closure $\overline{X^w_\circ}$를 **opposite Schubert variety**라 하며, $X^w$로 표기한다.

</div>

Opposite Bruhat cell $X^w_\circ$는 $X$ 위에서 $B^-$의 작용에 대한 궤도이므로, Bruhat cell과 마찬가지로 affine space와 isomorphic하다. 특히 $X^w_\circ$의 차원은 $\dim(G/P) - \ell(w)$이다. 이러한 opposite cell들은 $X$에 대한 또 다른 셀 분해

$$X = \bigsqcup_{w \in W^P} X^w_\circ$$

를 제공하며, 이는 기존의 Bruhat decomposition과 서로 transversal한 위치 관계를 가진다.

## Richardson Variety의 정의

이제 서로 다른 두 방향의 셀 구조, 즉 $B$-궤도와 $B^-$-궤도의 교차를 고려한다. 두 permutation $u, w \in W^P$가 주어졌을 때, Schubert variety $X_w$는 $X_w^\circ$의 Zariski closure이고 opposite Schubert variety $X^u$는 $X^u_\circ$의 Zariski closure이다. 이 둘의 교집합을 다음과 같이 정의한다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> $u, w \in W^P$에 대하여, 집합

$$R_{u,w} = X_w \cap X^u$$

를 **Richardson variety**라 부른다. 또한 이들의 낮은 차원 부분을 제외한 교집합

$$\mathring{R}_{u,w} = X_w^\circ \cap X^u_\circ$$

를 **open Richardson variety**라 부른다.

</div>

Richardson variety는 원래 Richardson의 연구에서 처음 등장하였으며, 이후 Kazhdan-Lusztig 다항식의 기하학적 해석이나 flag variety의 $K$-이론, 그리고 최근에는 cluster algebra와 mirror symmetry의 맥락에서 중요한 역할을 하게 되었다. 정의에서 알 수 있듯이 $R_{u,w}$는 $X$의 닫힌 부분다양체이며, $\mathring{R}_{u,w}$는 $R_{u,w}$의 Zariski open subset이다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> Open Richardson variety $\mathring{R}_{u,w}$가 비어있지 않은 필요충분조건은 $u \leq w$가 Bruhat order에서 성립하는 것이다. 이 조건이 만족될 때, $\mathring{R}_{u,w}$는 차원 $\ell(w) - \ell(u)$를 갖는 smooth affine variety이며, irreducible이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$X_w^\circ$는 $B$의 궤도이고 $X^u_\circ$는 $B^-$의 궤도이므로, 둘 다 $X$ 위에서 locally closed subset이다. Bruhat decomposition에 의해 $X_w^\circ \cong \bbC^{\ell(w)}$이고 $X^u_\circ \cong \bbC^{\dim(G/P) - \ell(u)}$이며, 이들은 $X$의 서로 다른 셀 분해에 속한다. 두 셀이 교차하여 비어있지 않으려면, 해당하는 Weyl군 원소들 사이에 Bruhat order $u \leq w$가 성립해야 한다. 이는 Deodhar의 연구와 Kazhdan-Lusztig의 원래 결과에 의해 확립된 사실이다.

$u \leq w$가 성립할 때, $X_w^\circ$와 $X^u_\circ$는 $X$ 위에서 서로 **transversal**하게 만난다. 이는 $B$와 $B^-$가 $X$의 한 점에서 서로 반대되는 tangent direction을 제공하기 때문이다. 구체적으로, 임의의 $x \in \mathring{R}_{u,w}$에서 tangent space는

$$T_x \mathring{R}_{u,w} = T_x X_w^\circ \cap T_x X^u_\circ$$

로 주어지며, dimension count에 의해 이 교집합의 차원은 $\ell(w) - \ell(u)$가 된다. 특히 이 차원은 음수가 아니며, $u = w$일 때는 한 점으로 축소된다. 이 transversality로부터 $\mathring{R}_{u,w}$가 smooth하고 irreducible인 affine variety가 됨을 얻는다.

</details>

명제 [명제 3](#prop3)의 핵심은 두 개의 서로 다른 셀 분해가 transversal하게 교차할 때, 그 교집합이 자연스럽게 좋은 기하학적 성질을 물려받는다는 점이다. Schubert variety 자체는 일반적으로 특이점을 가지지만, opposite Schubert variety와의 교차를 취하면 특이한 방향들이 서로 "상쇄"되어 부드러운 구조가 남는다.

<div class="example" markdown="1">

<ins id="ex4">**예시 4**</ins> $u = w$인 경우, $\mathring{R}_{w,w} = X_w^\circ \cap X^w_\circ$는 한 점으로 구성된다. 이는 $X_w$와 $X^w$가 서로 오직 한 점 $wP/P$에서만 만나기 때문이다. 반면 $u = e$ (단위원소)이고 $w = w_0^P$ ($W^P$의 최장원소)라면, $\mathring{R}_{e, w_0^P}$는 $X$의 어떤 열린 부분집합과 같아지며, 이 경우 Richardson variety는 $X$의 가장 큰 open cell이 된다.

</div>

## Grassmannian에서의 구체적 모습

이제 $X = \operatorname{Gr}(k, n)$인 Grassmannian의 경우를 구체적으로 살펴 보자. 이때 $G = \operatorname{GL}_n(\bbC)$이고, $P$는 $k$와 $n-k$ 크기의 upper block triangular matrices로 이루어진 parabolic subgroup이다. Weyl군은 $W = S_n$이며, $W_P = S_k \times S_{n-k}$는 $P$의 Weyl군이다. minimal length coset representatives $W^P \subset W$는 각 coset $w W_P$에서 가장 짧은 길이를 갖는 permutation들의 집합이다.

Schubert variety $X_w$는 $W^P$의 원소 $w$에 의해 색인되며, 이는 Young diagram이나 partition의 언어로도 기술할 수 있다. 마찬가지로 opposite Schubert variety $X^v$도 $v \in W^P$에 의해 색인된다. 이들의 교집합인 Richardson variety $R_{v,w}$는 Grassmannian 위에서 중요한 역할을 하며, 특히 positroid variety(이후 글에서 다룰)의 일반화로도 등장한다.

Grassmannian $\operatorname{Gr}(k, n)$ 위에서 open Richardson variety $\mathring{R}_{v,w}$는 다음과 같은 좌표를 가진 affine space의 부분집합으로 실현될 수 있다. $w \in W^P$에 해당하는 Schubert cell $X_w^\circ$는 $k \times (n-k)$ 행렬들의 공간 위에서 특정 rank condition을 만족하는 점들로 기술되며, opposite cell $X^v_\circ$는 이와 transversal한 추가적인 rank condition을 부여한다. 교집합 $\mathring{R}_{v,w}$에서는 이 두 조건이 동시에 만족되며, 이로 인해 Plücker coordinate의 일부가 좌표함수로 작용한다.

이러한 좌표화는 mirror symmetry에서 중요한 역할을 하며, 특히 Marsh-Rietsch의 construction에서 superpotential을 정의하는 데 직접적으로 사용된다.

## Marsh-Rietsch Mirror에서의 역할

[§Mirror Symmetry 개요](/ko/math/mirror_symmetry/overview)에서 언급하였듯이, Grassmannian에 대한 mirror symmetry는 toric variety의 경우와 달리 Lie-theoretic 구조에 깊이 의존한다. Marsh와 Rietsch는 $X = \operatorname{Gr}(k, \bbC^n)$의 mirror dual로서 Landau-Ginzburg model $(\check{X}^\circ, W_q)$를 구성하였는데, 여기서 B-model domain $\check{X}^\circ$는 Richardson variety와 직접적으로 연결된다.

구체적으로, $w_P \in W_P$를 parabolic subgroup $P$에 해당하는 Weyl군 $W_P$의 최장원소, $w_0 \in W$를 전체 Weyl군 $W$의 최장원소라 하자. 이때 Rietsch는 임의의 homogeneous space $G/P$에 대해 mirror Landau-Ginzburg model을 다음과 같은 open Richardson variety 위에 정의하였다.

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> Mirror variety는 다음과 같이 주어지는 open Richardson variety이다.

$$\check{X}^\circ = \mathring{R}_{w_P, w_0} = (B_+ w_P B_- \cap B_- w_0 B_-) / B_- \subset G^\vee / B_-$$

여기서 $G^\vee$는 $G$의 Langlands dual group이며, $B_+, B_-$는 각각 $G^\vee$의 Borel 및 opposite Borel subgroup이다. 특히 $G = \operatorname{GL}_n(\bbC)$인 경우, $G^\vee = \operatorname{GL}_n(\bbC)$이며 type A에서는 자기쌍대(self-dual)이다.

</div>

이 variety는 차원 $\ell(w_0) - \ell(w_P) = k(n-k)$를 갖는다. 특히, 이는 원래 A-model Grassmannian $\operatorname{Gr}(k, n)$의 차원과 정확히 일치한다. 이 점이 mirror symmetry에서 필수적인 조건임은 자명하다.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> Marsh-Rietsch의 mirror construction에서, [정의 6](#def6)의 variety $\check{X}^\circ$ 위에는 superpotential $W_q: \check{X}^\circ \times \bbC_q^\ast \to \bbC$가 Plücker coordinate의 rational function으로 주어진다. 이 superpotential의 Jacobi ring $\operatorname{Jac}(W_q)$는 A-model의 quantum cohomology ring과 동형이다.

$$QH^\ast(\operatorname{Gr}(k, n)) \cong \operatorname{Jac}(W_q)$$

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

이 동형은 세 단계로 이루어진다. **Step 1.** Marsh-Rietsch는 $\check{X}^\circ$의 좌표환을 Plücker coordinate로 생성하여 superpotential $W_q$가 정의되는 가환환 $F_q$를 구성한다. **Step 2.** $W_q$를 이 좌표들의 특별한 rational function 조합으로 정의하면, 그 임계점 방정식 $\partial W_q = 0$의 해집합인 critical locus가 Peterson variety와 일치함을 보인다. **Step 3.** Dale Peterson의 고전적인 결과에 의해 이 Peterson variety는 quantum cohomology ring $QH^\ast(\operatorname{Gr}(k,n))$과 자연스럽게 동형이 되며, 따라서 $\operatorname{Jac}(W_q) \cong QH^\ast(\operatorname{Gr}(k,n))$이 성립한다.

</details>

특히 $\check{X}^\circ$가 Richardson variety임을 이용하면, 이 공간의 좌표환에 대한 명시적 기술이 가능해지며, 이는 superpotential의 구체적인 계산으로 이어진다.

<div class="example" markdown="1">

<ins id="ex8">**예시 8**</ins> $\operatorname{Gr}(1, n) = \bbP^{n-1}$의 경우, $P$는 첫 번째 좌표축을 고정하는 parabolic subgroup이고, $w_P$와 $w_0$는 각각 $S_n$에서 적절한 permutation이 된다. 이때 $\check{X}^\circ$는 $(\bbC^\ast)^{n-1}$와 isomorphic하며, 이는 toric variety의 경우 Hori-Vafa mirror construction에서 얻어지는 결과와 일치한다. Superpotential은

$$W = z_1 + \cdots + z_{n-1} + \frac{q}{z_1 \cdots z_{n-1}}$$

로 주어지며, 이는 $\bbP^{n-1}$에 대한 잘 알려진 mirror superpotential이다.

</div>

이처럼 Richardson variety는 Grassmannian mirror symmetry에서 B-model의 기하학적 무대를 제공할 뿐 아니라, 그 좌표환의 풍부한 대수구조가 quantum cohomology와의 정확한 대응을 가능하게 한다. 특히 open Richardson variety의 cluster algebra 구조는 최근에도 활발히 연구되며, mirror symmetry와의 연결을 더욱 심화시키는 중요한 도구로 작용하고 있다.

---

**참고문헌**

**[MR]** R. J. Marsh, K. Rietsch, *The B-model connection and mirror symmetry for Grassmannians*, Adv. Math. **319** (2017), 352--416.

**[Rie08]** K. Rietsch, *A mirror symmetric construction of $qH_T^\ast(G/P)_{(q)}$*, Adv. Math. **217** (2008), 2401--2442.

**[KL80]** D. Kazhdan, G. Lusztig, *Schubert varieties and Poincaré duality*, Geometry of the Laplace operator, Proc. Sympos. Pure Math. **36**, AMS, 1980.

**[Deo85]** V. V. Deodhar, *On some geometric aspects of Bruhat orderings. I. A finer decomposition of Bruhat cells*, Invent. Math. **79** (1985), 499--511.
