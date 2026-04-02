---
title: "Bézout's Theorem"
excerpt: "Bézout's theorem and its applications"

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/bezout_theorem
sidebar: 
    nav: "algebraic_geometry-ko"

header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Bezout_Theorem.png
    overlay_filter: 0.5

date: 2026-03-15
last_modified_at: 2026-03-31
weight: 21
published: false
---

## 도입

$$\mathbb{P}^2$$ 안의 두 곡선 $$C, D$$가 주어졌다 하자. 직관적으로 차수가 높은 곡선일수록 더 복잡한 모양을 가지며, 따라서 두 곡선이 만나는 점의 개수도 차수에 의존할 것이라는 기대가 자연스럽다. **Bézout의 정리(Bézout's theorem)**는 이 직관을 정밀하게 만들어주는 정리로, 가장 간단한 형태로 $$\mathbb{P}^2$$ 안의 차수 $$m$$, $$n$$인 두 곡선은 공통 성분이 없으면 정확히 $$mn$$개의 점에서 만난다는 것을 말한다. 물론 두 곡선이 만나는 점의 개수를 센다는 것은 애매하다. 두 직선은 (평행한 경우를 포함하여) 항상 한 점에서 만나지만, $$\mathbb{A}^2$$에서의 직선 $$\y=0$$과 포물선 $$\y=\x^2$$은 원점에서만 만나므로 교점이 하나이다. 그러나 원점에서 두 곡선은 서로 접하고 있으므로, 이 점을 *한 점*으로 세는 것이 아니라 *중복도 2의 교점*으로 세어야 한다는 것이 이 예시로부터 자연스럽게 동기부여된다. 사영공간 $$\mathbb{P}^n$$ 안에서의 Bézout의 정리는 이러한 관찰을 일반화한 것이다.

보다 일반적으로, $$\mathbb{P}^n$$ 안의 $$n$$개의 초곡면 $$H_1, \ldots, H_n$$이 주어졌을 때, 이들이 공통 성분을 갖지 않는다면 그 교차는 유한개의 점으로 이루어지며 그 점의 개수(중복도 포함)는 각 초곡면의 차수의 곱과 같다. 이는 대수기하학에서 교차 이론의 가장 기본적인 결과이며, Pascal의 정리, Cayley-Bacharach 정리 등 많은 고전적인 결과들이 Bézout의 정리로부터 자연스럽게 유도된다.

## 정리의 진술

<div class="proposition" markdown="1">

<ins id="prop1">**명제 1 (Bézout의 정리)**</ins> 대수적으로 닫힌 체 위의 $$\mathbb{P}^n$$ 안에서, 차수 $$d_1, \ldots, d_n$$의 초곡면 $$H_1, \ldots, H_n$$이 공통 성분을 갖지 않는다면:

$$\deg(H_1 \cap \cdots \cap H_n) = d_1 \cdots d_n$$

여기서 교차는 중복도(multiplicity)를 고려한 scheme-theoretic intersection이다. 초곡면의 개수가 $$n$$이므로 교차는 0차원이며, $$\deg$$는 점의 개수(중복도 포함)를 의미한다.

</div>

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2 ($$\mathbb{P}^2$$ 안의 곡선)**</ins> 대수적으로 닫힌 체 위의 $$\mathbb{P}^2$$ 안에서, 차수 $$m$$, $$n$$인 두 곡선 $$C, D$$가 공통 성분을 갖지 않으면:

$$\sum_{p \in C \cap D} i_p(C, D) = mn$$

</div>

명제 1과 명제 2에서 "공통 성분이 없다"는 조건은 필수적이다. 예를 들어 $$C = D$$이면 두 곡선은 무한히 많은 점에서 만나므로 결론이 성립하지 않는다.

## 예시

<div class="example" markdown="1">

<ins id="ex3">**예시 3 (직선과 곡선)**</ins> $$\mathbb{P}^2$$ 안의 차수 $$d$$ 곡선 $$C$$와 직선 $$L$$을 생각하자. $$L$$이 $$C$$의 성분이 아니면, Bézout의 정리에 의하여 $$\lvert C \cap L \rvert = d$$이다(교차 중복도 포함). 이는 직선이 곡선을 뚫고 지나가는 횟수가 정확히 곡선의 차수와 같다는 것을 의미한다. 가령 차수 3 곡선(cubic curve)은 일반적인 직선과 정확히 3점에서 만나며, 차수 4 곡선(quartic curve)은 직선과 4점에서 만난다.

</div>

<div class="example" markdown="1">

<ins id="ex4">**예시 4 (두 이차곡선)**</ins> $$\mathbb{P}^2$$ 안의 두 이차곡선

$$C_1 = Z(\x_0^2 + \x_1^2 - \x_2^2),\qquad C_2 = Z(\x_0\x_1)$$

을 생각하자. $$C_1$$은 원뿔의 사영화이고, $$C_2$$는 두 직선 $$Z(\x_0)$$과 $$Z(\x_1)$$의 합집합이다. 이 두 곡선은 공통 성분을 갖지 않으므로 Bézout의 정리에 의하여 $$2 \times 2 = 4$$개의 교점을 가져야 한다. 실제로 교집합을 계산하면,

- $$\x_0 = 0$$일 때: $$\x_1^2 = \x_2^2$$, 즉 $$[0:1:1]$$과 $$[0:1:-1]$$
- $$\x_1 = 0$$일 때: $$\x_0^2 = \x_2^2$$, 즉 $$[1:0:1]$$과 $$[1:0:-1]$$

로 정확히 4점에서 만남을 확인할 수 있다.

</div>

<div class="example" markdown="1">

<ins id="ex5">**예시 5 (접하는 경우)**</ins> $$\mathbb{P}^2$$에서 곡선 $$C = Z(\x_2 - \x_1^2)$$와 직선 $$L = Z(\x_2)$$를 생각하자. $$C$$의 차수는 2이고 $$L$$의 차수는 1이므로 Bézout의 정리에 의하여 교점의 수(중복도 포함)는 $$2 \times 1 = 2$$이어야 한다.

실제로 $$U_2$$에서 이 두 곡선은 $$y = x^2$$와 $$y = 0$$으로 주어지며, 그 교점은 원점 $$(0,0)$$뿐이다. 그러나 원점에서 두 곡선은 서로 접하여 있으므로, 이 점에서의 교차 중복도는 2이다. 즉 하나의 교점이 중복도 2로 세어져 총 교차수가 $$2$$가 되어 Bézout의 정리와 일치한다.

</div>

## Chow 환을 통한 증명

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> $$\operatorname{CH}^\ast(\mathbb{P}^n) = \mathbb{Z}[H] / (H^{n+1})$$에서 차수 $$d_i$$ 초곡면 $$H_i$$의 class는 $$d_i H$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

차수 $$d_i$$ 초곡면 $$H_i$$가 주어지면, ([§Chow Groups, ⁋명제 7](/ko/math/algebraic_geometry/chow_groups#prop7))에 의해 $$\operatorname{CH}^\ast(\mathbb{P}^n) = \mathbb{Z}[H]/(H^{n+1})$$이며, $$H_i$$의 class는 $$c_i H$$ 형태로 표현된다. 여기서 $$c_i$$를 결정하려면, generic hyperplane $$L$$ (class $$H$$)과 $$H_i$$의 교차를 고려하면 된다. $$H_i$$가 차수 $$d_i$$의 동차다항식 $$f$$로 정의된다고 하자. 적절한 projective linear transformation으로 $$L$$을 $$V(x_0)$$으로 잡을 수 있다. 그러면 $$H_i \cap L$$은 $$f(0, x_1, \ldots, x_n)$$로 정의되는 $$\mathbb{P}^{n-1}$$ 안의 다형체이다. $$f$$가 차수 $$d_i$$의 동차다항식이므로, $$f(0, x_1, \ldots, x_n)$$ 역시 차수 $$d_i$$의 동차다항식이다 (또는 영다항식, 이 경우 $$H_i \subset L$$이므로 $$L$$이 generic이 아님에 모순). 따라서 $$H_i \cap L$$은 $$\mathbb{P}^{n-1}$$ 안의 차수 $$d_i$$ 초곡면이며, 특히 $$n = 2$$인 경우 $$\mathbb{P}^1$$ 위의 차수 $$d_i$$ 다항식이 정의하는 $$d_i$$개의 점(을 가진 0차원 scheme)이 된다. 이는 대수학의 기본정리에 의해 차수를 고려한 점의 개수가 $$d_i$$임을 보여주며, Bézout의 정리에 의존하지 않는다. 따라서 $$H_i \cdot H = d_i$$이고, class는 $$d_i H$$가 된다.

이제 초곡면 $$H_1, \ldots, H_r$$의 교차를 생각하자 ($$r \leq n$$). Intersection product:

$$[H_1] \cdot \cdots \cdot [H_r] = (d_1 H) \cdots (d_r H) = d_1 \cdots d_r \cdot H^r$$

$$H^r$$은 여차원 $$r$$ linear subspace의 class이고, 그 degree는 1이다. 특히 $$r = n$$이면 $$H^n$$은 점의 class이므로:

$$\deg(H_1 \cap \cdots \cap H_n) = d_1 \cdots d_n$$

</details>

## 일반화

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7 (일반화된 Bézout 부등식)**</ins> $$\mathbb{P}^n$$ 안의 두 다형체 $$V, W$$에 대해, $$\operatorname{codim}(V \cap W) \leq \operatorname{codim}(V) + \operatorname{codim}(W)$$이면:

$$\deg(V \cap W) \leq \deg(V) \cdot \deg(W)$$

등호는 $$V$$와 $$W$$가 proper intersection을 가질 때 (즉, $$\operatorname{codim}(V \cap W) = \operatorname{codim}(V) + \operatorname{codim}(W)$$이고 교차가 올바르게 정의될 때) 성립한다. 초곡면의 경우 ([명제 1](#prop1))에서 Chow 환의 곱셈성을 통해 자연스럽게 유도된다.

</div>

<div class="example" markdown="1">

<ins id="ex8">**예시 8 ($$\mathbb{P}^3$$)**</ins> $$\mathbb{P}^3$$ 안의 두 이차곡면(quadric surface) $$Q_1, Q_2$$ (차수 2)의 교차는 차수 4 곡선이다.

$$Q_1 \cap Q_2$$는 타원곡선(genus 1) 또는 유리곡선의 합집합일 수 있다.

</div>

## 응용

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9 (Cubic의 9점, Cayley-Bacharach 정리의 특수한 경우)**</ins> $$\mathbb{P}^2$$ 안의 두 세차곡선 $$C_1, C_2$$가 일반적인 위치에서 9점 $$p_1, \ldots, p_9$$에서 만나면, 이 9점을 지나는 임의의 세차곡선은 $$C_1$$과 $$C_2$$의 일차결합이다. 즉, $$\mathbb{P}^2$$ 위의 세차곡선 공간에서 9점을 지나는 부분공간은 $$C_1, C_2$$가 생성하는 2차원 부분공간이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$\mathbb{P}^2$$ 위의 세차곡선은 차수 3의 동차다항식으로 정의되며, $$\dim H^0(\mathbb{P}^2, \mathcal{O}(3)) = \binom{3+2}{2} = 10$$이다. 각 점 $$p_i$$를 지나는 것은 다항식 공간에 하나의 일차조건을 부과하므로, 9개 점을 지나는 세차곡선의 공간은 여차원이 최대 9이고, 따라서 적어도 1차원이다.

$$C_1, C_2$$는 이 9점을 지나는 서로 다른 두 세차곡선이므로, 이 둘은 세차곡선 공간 안에서 독립적인 원소를 이룬다. 9개 점이 일반적인 위치에 있으므로 (즉, 9점이 어떤 세차곡선 위에 있는 다른 점들의 부분집합이 아니도록), 9점 조건의 여차원은 정확히 8이며, 따라서 9점을 지나는 세차곡선 공간은 정확히 2차원이다. 이는 정확히 $$C_1, C_2$$가 생성하는 공간이다. 따라서 9점을 지나는 임의의 세차곡선 $$C_3$$은 $$C_3 = \lambda C_1 + \mu C_2$$로 쓸 수 있다.

이 결과는 보다 일반적인 **Cayley-Bacharach 정리**의 특수한 경우이다.

</details>

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10 (Pascal의 정리)**</ins> 이차곡선(conic) 위의 6점 $$p_1, \ldots, p_6$$에 대해, $$\overline{p_1 p_2} \cap \overline{p_4 p_5}$$, $$\overline{p_2 p_3} \cap \overline{p_5 p_6}$$, $$\overline{p_3 p_4} \cap \overline{p_6 p_1}$$이 모두 존재하면 이 세 점은 공선형(collinear)이다.

</div>

<details class="proof" markdown="1">
<summary>증명 (Sketch)</summary>

이차곡선 위의 6점을 $$A, B, C, D, E, F$$로 표기하자. 두 세차곡선을 다음과 같이 정의하자:
$$X = \overline{AB} \cup \overline{CD} \cup \overline{EF}, \quad Y = \overline{BC} \cup \overline{DE} \cup \overline{FA}$$

$$X$$와 $$Y$$는 각각 세 직선의 합집합으로 이루어진 세차곡선이다. 이 두 세차곡선은 다음 9점에서 만난다: 이차곡선 위의 6점 $$A, B, C, D, E, F$$와, 세 쌍의 반대편 변들의 교점 $$P = \overline{AB} \cap \overline{DE}$$, $$Q = \overline{BC} \cap \overline{EF}$$, $$R = \overline{CD} \cap \overline{FA}$$.

이제 세차곡선 $$Z$$를 이차곡선 $$\Gamma$$와 직선 $$\overline{PQ}$$의 합집합으로 정의하자. $$Z$$ 역시 세차곡선이며, $$X \cap Y$$의 9점 $$A, B, C, D, E, F, P, Q, R$$ 중 $$A, B, C, D, E, F, P, Q$$의 8점을 지난다. [명제 9](#prop9)의 증명과 동일한 논증에 의해, 세차곡선 공간은 10차원이고 8점을 지나는 조건은 여차원이 최대 8이므로, 8점을 지나는 세차곡선 공간은 적어도 2차원이다. $$X$$와 $$Y$$는 이 8점을 지나는 서로 독립적인 두 세차곡선이므로, 이 공간의 기저를 이룬다. 일반적인 위치 조건 하에서 8점 조건의 여차원은 정확히 8이고 따라서 공간은 정확히 2차원이므로, $$Z$$는 $$X$$와 $$Y$$의 일차결합으로 표현된다. 그러면 $$Z$$ 역시 $$X \cap Y$$의 모든 9점을 지나야 하므로, $$R$$도 $$Z$$ 위에 있어야 한다. $$R$$은 이차곡선 위에 있지 않으므로 (반대편 변들의 교점은 이차곡선 위의 점이 될 수 없다), $$R$$은 직선 $$\overline{PQ}$$ 위에 있어야 한다. 즉, $$P, Q, R$$은 공선형이다.

</details>

<div class="proposition" markdown="1">

<ins id="prop11">**명제 11 (이중점의 최대 개수)**</ins> 차수 $$d$$ 평면곡선이 가질 수 있는 최대 이중점(double point)의 개수는 $$\binom{d-1}{2} = \frac{(d-1)(d-2)}{2}$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

매끄러운 차수 $$d$$ 곡선 $$C \subset \mathbb{P}^2$$의 경우, 수반공식(adjunction formula) $$K_C = (K_{\mathbb{P}^2} \otimes \mathcal{O}(C))\vert_C$$와 종수 공식 $$2g - 2 = C \cdot (C + K_{\mathbb{P}^2})$$를 적용한다. $$K_{\mathbb{P}^2} = \mathcal{O}(-3)$$이고 $$[C] = dH$$이므로:

$$2g - 2 = d(d-3) \implies g = \frac{(d-1)(d-2)}{2}$$

이중점 $$p$$에서 곡선 $$C$$가 특이점(singular)이면, 뽑기(blow-up) $$\pi: \tilde{\mathbb{P}}^2 \to \mathbb{P}^2$$에서 $$p$$를 예외적 약자(exceptional divisor) $$E$$로 교체한 strict transform $$\tilde{C}$$는 매끄러운 곡선이 된다. 특히 $$p$$가 보통 이중점(node, ordinary double point)이면 $$\tilde{C}$$는 $$E$$와 서로 다른 두 점에서 transversally 만나고, 특이점 보정항 $$\delta_p = 1$$이므로 산술 종수가 정확히 1 감소한다. 따라서 $$n$$개의 이중점이 있는 곡선의 (정규화의) 종수는:

$$g = \frac{(d-1)(d-2)}{2} - n$$

종수가 음수가 될 수 없으므로 $$n \leq \frac{(d-1)(d-2)}{2} = \binom{d-1}{2}$$이다.

</details>

## 복소 해석적 관점

<div class="proposition" markdown="1">

<ins id="prop12">**명제 12 (위상적 해석)**</ins> $$\mathbb{P}^n_\mathbb{C}$$에서 Bézout의 정리는 위상적 의미를 갖는다:

$$\sum_{p \in V \cap W} i_p(V, W) = [V] \cup [W] \in H^{2n}(\mathbb{P}^n, \mathbb{Z}) \cong \mathbb{Z}$$

Cohomology class의 cup product가 교차수(intersection number)를 계산한다. Chow 환과 코호몰로지 환 사이의 cycle class map $$\operatorname{cl}: \operatorname{CH}^\ast(X) \to H^{2\ast}(X, \mathbb{Z})$$가 $$\mathbb{P}^n$$에서 동형사상이므로, Chow 환에서의 교차곱 계산이 코호몰로지에서의 cup product로 번역된다.

</div>

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[Ful]** W. Fulton, *Intersection Theory*, Springer, 1984.
