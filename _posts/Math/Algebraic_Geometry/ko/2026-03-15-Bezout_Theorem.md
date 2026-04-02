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
last_modified_at: 2026-04-02
weight: 21
published: false
---

## 도입

$$\mathbb{P}^2$$ 안의 두 곡선 $$C, D$$가 주어졌다 하자. 직관적으로 차수가 높은 곡선일수록 더 복잡한 모양을 가지며, 따라서 두 곡선이 만나는 점의 개수도 차수에 의존할 것이라는 기대가 자연스럽다. **Bézout의 정리(Bézout's theorem)**는 이 직관을 정밀하게 만들어주는 정리로, 가장 간단한 형태로 $$\mathbb{P}^2$$ 안의 차수 $$m$$, $$n$$인 두 곡선은 공통 성분이 없으면 정확히 $$mn$$개의 점에서 만난다는 것을 말한다.

물론 두 곡선이 만나는 점의 개수를 센다는 것은 애매하다. 두 직선은 (평행한 경우를 포함하여) 항상 한 점에서 만나지만, $$\mathbb{A}^2$$에서의 직선 $$\y=0$$과 포물선 $$\y=\x^2$$은 원점에서만 만나므로 교점이 하나이다. 그러나 원점에서 두 곡선은 서로 접하고 있으므로, 이 점을 *한 점*으로 세는 것이 아니라 *중복도 2의 교점*으로 세어야 한다는 것이 이 예시로부터 자연스럽게 동기부여된다. 사영공간 $$\mathbb{P}^n$$ 안에서의 Bézout의 정리는 이러한 관찰을 일반화한 것이다.

보다 일반적으로, $$\mathbb{P}^n$$ 안의 $$n$$개의 초곡면 $$H_1, \ldots, H_n$$이 주어졌을 때, 이들이 공통 성분을 갖지 않는다면 그 교차는 유한개의 점으로 이루어지며 그 점의 개수(중복도 포함)는 각 초곡면의 차수의 곱과 같다. 이는 대수기하학에서 교차 이론의 가장 기본적인 결과이며, Pascal의 정리, Cayley-Bacharach 정리 등 많은 고전적인 결과들이 Bézout의 정리로부터 자연스럽게 유도된다.

## 정리의 진술

<div class="proposition" markdown="1">

<ins id="prop1">**명제 1 (Bézout의 정리)**</ins> 대수적으로 닫힌 체 위의 $$\mathbb{P}^n$$ 안에서, 차수 $$d_1, \ldots, d_n$$의 초곡면 $$H_1, \ldots, H_n$$이 공통 성분을 갖지 않는다면(즉, $$H_i$$들을 정의하는 동차다항식들이 공통인 기약인자를 갖지 않는다면):

$$\deg(H_1 \cap \cdots \cap H_n) = d_1 \cdots d_n$$

여기서 교차는 중복도(multiplicity)를 고려한 것이며, $$\deg$$는 점의 개수(중복도 포함)를 의미한다. 초곡면의 개수가 $$n$$이므로 교차는 0차원이어야 한다. ([§차원, ⁋예시 14](/ko/math/algebraic_geometry/dimension#ex14))

</div>

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2 ($$\mathbb{P}^2$$ 안의 곡선)**</ins> 대수적으로 닫힌 체 위의 $$\mathbb{P}^2$$ 안에서, 차수 $$m$$, $$n$$인 두 곡선 $$C, D$$가 공통 성분을 갖지 않으면:

$$\sum_{p \in C \cap D} i_p(C, D) = mn$$

여기서 $$i_p(C, D)$$는 점 $$p$$에서의 교차 중복도(intersection multiplicity)이다.

</div>

명제 1과 명제 2에서 "공통 성분이 없다"는 조건은 필수적이다. 예를 들어 $$C = D$$이면 두 곡선은 곡선 전체에서 만나므로 결론이 성립하지 않는다. 이 조건은 달리 말하면 $$C$$와 $$D$$를 정의하는 동차다항식들이 공통인 irreducible factor를 갖지 않는다는 것이다.

## 예시

<div class="example" markdown="1">

<ins id="ex3">**예시 3 (직선과 곡선)**</ins> $$\mathbb{P}^2$$ 안의 차수 $$d$$ 곡선 $$C$$와 직선 $$L$$을 생각하자. $$L$$이 $$C$$의 성분이 아니면, Bézout의 정리에 의하여 $$\lvert C \cap L \rvert = d$$이다(교차 중복도 포함). 이는 직선이 곡선을 뚫고 지나가는 횟수가 정확히 곡선의 차수와 같다는 것을 의미한다. 가령 차수 3 곡선(cubic curve)은 일반적인 직선과 정확히 3점에서 만나며, 차수 4 곡선(quartic curve)은 직선과 4점에서 만난다.

</div>

<div class="example" markdown="1">

<ins id="ex4">**예시 4 (두 이차곡선)**</ins> $$\mathbb{P}^2$$ 안의 두 이차곡선

$$C_1 = Z(\x_0^2 + \x_1^2 - \x_2^2),\qquad C_2 = Z(\x_0\x_1)$$

을 생각하자. $$C_1$$은 원뿔의 사영화이고, $$C_2$$는 두 직선 $$Z(\x_0)$$과 $$Z(\x_1)$$의 합집합이다. 이 두 곡선은 공통 성분을 갖지 않으므로 Bézout의 정리에 의하여 $$2 \times 2 = 4$$개의 교점을 가져야 한다. 실제로 교집합을 계산해보면, $$\x_0 = 0$$일 때 $$\x_1^2 = \x_2^2$$이 되어 $$[0:1:1]$$과 $$[0:1:-1]$$을 얻고, $$\x_1 = 0$$일 때 $$\x_0^2 = \x_2^2$$이 되어 $$[1:0:1]$$과 $$[1:0:-1]$$을 얻어 정확히 4점에서 만남을 확인할 수 있다.

</div>

<div class="example" markdown="1">

<ins id="ex5">**예시 5 (접하는 경우)**</ins> $$\mathbb{P}^2$$에서 곡선 $$C = Z(\x_2\x_0 - \x_1^2)$$와 직선 $$L = Z(\x_2)$$를 생각하자. $$C$$의 차수는 2이고 $$L$$의 차수는 1이므로 Bézout의 정리에 의하여 교점의 수(중복도 포함)는 $$2 \times 1 = 2$$이어야 한다.

실제로 $$U_0$$에서 이 두 곡선은 $$\x_2 = 0$$이므로 $$C$$의 방정식은 $$-\x_1^2 = 0$$, 즉 $$\x_1 = 0$$이 된다. 따라서 교점은 $$[1:0:0]$$뿐이며, 이 점에서 $$\x_1^2$$의 중복도가 2이므로 교차 중복도는 2이다. 즉 하나의 교점이 중복도 2로 세어져 총 교차수가 $$2$$가 되어 Bézout의 정리와 일치한다.

</div>

<div class="example" markdown="1">

<ins id="ex6">**예시 6 (삼차곡선과 직선)**</ins> $$\mathbb{P}^2$$에서 삼차곡선 $$C = Z(\y^2\x_2 - \x^3 - \x_2^3)$$와 직선 $$L = Z(\x)$$를 생각하자. $$L$$의 방정식 $$\x = 0$$을 $$C$$의 방정식에 대입하면 $$\y^2\x_2 = \x_2^3$$, 즉 $$\x_2(\y^2 - \x_2^2) = 0$$을 얻는다. 따라서 교점은 $$\x_2 = 0$$일 때 $$[0:1:0]$$, $$\y = \x_2$$일 때 $$[0:1:1]$$, $$\y = -\x_2$$일 때 $$[0:1:-1]$$이며, 모두 서로 다르므로 중복도 1씩 3개의 교점이 존재한다. 이는 $$\deg C \cdot \deg L = 3 \times 1 = 3$$과 일치한다.

</div>

## 교차 중복도

명제 2에서 등장한 교차 중복도 $$i_p(C, D)$$를 정의하기 위해, 우선 $$\mathbb{P}^2$$ 안의 두 곡선 $$C = Z(F)$$, $$D = Z(G)$$가 주어졌고 $$p = [a:b:c]$$가 $$C \cap D$$의 점이라 하자. $$c \neq 0$$이라 가정하고 affine chart $$U_2$$에서 생각하면, $$p$$는 $$(a/c, b/c)$$이고 $$F, G$$는 affine 다항식 $$f, g$$로 dehomogenize된다.

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> 점 $$p$$에서의 교차 중복도를 다음과 같이 정의한다.

$$i_p(C, D) = \dim_\mathbb{K} \mathcal{O}_{\mathbb{A}^2, p} / (f, g)$$

여기서 $$\mathcal{O}_{\mathbb{A}^2, p}$$는 점 $$p$$에서의 local ring이고, $$(f, g)$$는 $$f, g$$로 생성되는 ideal이다.

</div>

이 정의는 직관적으로 $$p$$ 근방에서 $$f$$와 $$g$$가 얼마나 "강하게" 만나는지를 측정한다. $$i_p = 1$$이면 두 곡선이 $$p$$에서 transversally 만나고, $$i_p > 1$$이면 더 복잡한 교차가 일어난다. 다음 명제는 이 정의가 기하적인 직관과 맞아떨어짐을 보여준다.

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> $$C = Z(f)$$와 $$D = Z(g)$$가 $$\mathbb{A}^2$$의 곡선이고 $$p \in C \cap D$$라 하자.

1. $$i_p(C, D) \ge 1$$이다.
2. $$i_p(C, D) = 1$$일 필요충분조건은 $$C$$와 $$D$$가 $$p$$에서 매끄럽고 서로 다른 접선을 갖는 것이다.
3. $$i_p(C, D) \ge 2$$일 필요충분조건은 $$C$$와 $$D$$가 $$p$$에서 접하는 것이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

1. $$p \in C \cap D$$이면 $$f(p) = g(p) = 0$$이므로 $$f, g \in \mathfrak{m}_p$$이다. 따라서 $$(f, g) \subseteq \mathfrak{m}_p$$이며, 몫공간 $$\mathcal{O}_{\mathbb{A}^2, p}/(f, g)$$는 $$\mathcal{O}_{\mathbb{A}^2, p}/\mathfrak{m}_p \cong \mathbb{K}$$를 further quotient로 가지므로 $$\dim_\mathbb{K} \mathcal{O}_{\mathbb{A}^2, p}/(f, g) \ge 1$$, 즉 $$i_p \ge 1$$이다.
2. $$i_p = 1$$이라는 것은 $$\mathcal{O}_{\mathbb{A}^2, p}/(f, g) \cong \mathbb{K}$$라는 것이다. 이는 $$(f, g) = \mathfrak{m}_p$$와 동치이며, 이는 곧 $$f$$와 $$g$$가 $$\mathfrak{m}_p / \mathfrak{m}_p^2$$에서 일차독립이라는 것이다. 즉, $$\nabla f(p)$$와 $$\nabla g(p)$$가 서로 다른 방향을 가리킨다는 뜻이고, 이는 $$C$$와 $$D$$가 $$p$$에서 매끄럽고 서로 다른 접선을 갖는 것과 동치이다.
3. $$i_p \ge 2$$일 필요충분조건은 $$C$$와 $$D$$가 $$p$$에서 접하는 것이다. 구체적으로, $$p$$에서 $$C$$와 $$D$$의 (적어도 하나의) 접선 방향이 일치하거나, $$p$$가 $$C$$ 또는 $$D$$의 특이점인 경우에 해당한다. 증명: $$i_p \ge 2$$는 $$\mathcal{O}_{\mathbb{A}^2, p}/(f, g)$$의 $$\mathbb{K}$$-차원이 2 이상이라는 것이고, 이는 $$(f, g) \subsetneq \mathfrak{m}_p$$를 의미한다. 즉 $$f$$와 $$g$$의 일차항(선형 부분)이 $$\mathfrak{m}_p / \mathfrak{m}_p^2$$에서 일차종속이거나, 둘 다 영이므로, $$\nabla f(p)$$와 $$\nabla g(p)$$가 일차종속이다. 이는 $$p$$에서 두 곡선의 접선 방향이 일치하거나 $$p$$가 특이점인 경우이다.

</details>

## 증명

명제 2의 증명, 즉 $$\mathbb{P}^2$$에서의 Bézout의 정리를 증명하기 위해, 우리는 다음의 보조정리를 사용한다.

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9 (Hilbert 다항식)**</ins> 차수 $$d$$인 동차다항식 $$F \in \mathbb{K}[\x_0, \x_1, \x_2]$$에 의하여 정의되는 곡선 $$C = Z(F)$$의 coordinate ring $$S(C) = \mathbb{K}[\x_0, \x_1, \x_2]/(F)$$의 Hilbert 함수 $$H(t) = \dim_\mathbb{K} S(C)_t$$는 $$t$$가 충분히 클 때 $$H(t) = dt + \frac{d(3-d)}{2}$$이다. 특히 Hilbert 다항식의 차수는 1이고 그 일차항의 계수는 $$d$$이다.

</div>

명제 2의 증명은 본질적으로 Chow 환 $$\operatorname{CH}^\ast(\mathbb{P}^n) = \mathbb{Z}[H]/(H^{n+1})$$을 통하여 이루어지지만, 이 개념은 아직 소개하지 않았으므로 여기서는 $$\mathbb{P}^2$$의 경우에 대해 보다 직접적인 증명을 제시한다. 핵심적인 관찰은 $$\mathbb{P}^2$$ 안에서 "차수 $$d$$ 곡선"이란 것이 $$\operatorname{CH}^1(\mathbb{P}^2) = \mathbb{Z}$$의 원소 $$dH$$에 해당한다는 것이다. 여기서 $$H$$는 hyperplane class, 즉 직선의 class이다.

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10**</ins> $$\mathbb{P}^2$$ 안의 차수 $$d$$ 곡선 $$C = Z(F)$$에 대하여, 임의의 일반적인 직선 $$L$$과의 교차 $$C \cap L$$은 정확히 $$d$$개의 점(중복도 포함)으로 이루어진다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

일반성을 잃지 않고 $$L = Z(\x_2)$$라 하자. $$C$$가 차수 $$d$$ 동차다항식 $$F(\x_0, \x_1, \x_2)$$로 정의되므로, $$L \cap C$$에서 $$\x_2 = 0$$을 대입하면 $$F(\x_0, \x_1, 0)$$을 얻는다. 이는 $$\x_0, \x_1$$에 관한 차수 $$d$$ 동차다항식이며, 대수적으로 닫힌 체 위에서 이는 (대수학의 기본정리에 의하여) 정확히 $$d$$개의 근 $$[\alpha_i : \beta_i : 0]$$을 갖는다(중복도 포함). $$L$$이 일반적이라는 가정에 의하여 $$F(\x_0, \x_1, 0)$$이 영다항식이 아니라고 할 수 있다. 만일 $$F(\x_0, \x_1, 0) = 0$$이라면 $$\x_2$$가 $$F$$의 인수가 되어 $$C$$가 직선 $$Z(\x_2)$$를 성분으로 갖게 되므로, $$C$$와 $$L$$이 공통 성분을 갖는 것과 모순된다.

</details>

이제 명제 2를 증명한다. 증명의 핵심은 두 가지이다. 첫째, 교차 중복도의 합이 전역적인 대수적 대상의 차원과 일치한다는 것을 보이고, 둘째, 그 대상의 차원이 Hilbert 다항식을 이용하여 정확히 $$mn$$으로 계산된다는 것을 보이는 것이다.

<div class="proposition" markdown="1">

<ins id="prop11">**명제 11**</ins> (명제 2의 증명) $$\mathbb{P}^2$$ 안의 차수 $$m$$, $$n$$인 두 곡선 $$C = Z(F)$$, $$D = Z(G)$$가 공통 성분을 갖지 않으면 $$\sum_p i_p(C, D) = mn$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

두 가지 단계로 나누어 증명한다.

**단계 1.** 우선 다음을 보인다.

> $$\sum_{p \in C \cap D} i_p(C, D) = \dim_\mathbb{K} (\mathbb{K}[\x_0, \x_1, \x_2]/(F, G))_t \qquad (t \gg 0)$$

$$C \cap D$$가 유한집합이라는 것은 $$C$$와 $$D$$가 공통 성분을 갖지 않는다는 가정으로부터 알려져 있다.([§차원, ⁋예시 14](/ko/math/algebraic_geometry/dimension#ex14)) 점 $$p = [a:b:c] \in C \cap D$$에 대하여, $$c \neq 0$$이라 가정하면 $$U_2$$에서의 좌표로 $$p = (a/c, b/c)$$이고, $$F, G$$를 dehomogenize한 $$f, g \in \mathbb{K}[\x, \y]$$에 대하여

$$i_p(C, D) = \dim_\mathbb{K} \mathcal{O}_{\mathbb{A}^2, p}/(f, g)$$

이다. $$V(F, G)$$가 유한집합이므로 $$f, g$$는 affine ring $$\mathbb{K}[\x, \y]$$에서 0차원 ideal $$(f, g)$$을 생성하며, 중국인의 나머지 정리에 의하여

$$\mathbb{K}[\x, \y]/(f, g) \cong \prod_{p \in V(f,g)} \mathcal{O}_{\mathbb{A}^2, p}/(f, g)$$

이다. 따라서 $$\dim_\mathbb{K} \mathbb{K}[\x, \y]/(f, g) = \sum_p i_p(C, D)$$이다.

한편, $$S = \mathbb{K}[\x_0, \x_1, \x_2]$$의 몫 $$R = S/(F, G)$$의 Hilbert 함수 $$H(t) = \dim_\mathbb{K} R_t$$는 $$t \gg 0$$에서 상수가 되며(단계 2에서 증명), 이 상숫값은 $$\dim_\mathbb{K} \mathbb{K}[\x, \y]/(f, g)$$와 같다. 이는 $$t \gg 0$$일 때 차수 $$t$$ 동차다항식들의 평가 사상 $$R_t \to \mathbb{K}^{\lvert V(F,G) \rvert}$$이 전사이기 때문이다.

**단계 2.** 이제 $$\dim_\mathbb{K} (\mathbb{K}[\x_0, \x_1, \x_2]/(F, G))_t = mn$$임을 보인다($$t \gg 0$$). $$S = \mathbb{K}[\x_0, \x_1, \x_2]$$라 쓰자. $$F, G$$가 공통인 기약인자를 갖지 않으므로 곱셈사상 $$\cdot F: S(-m) \to S$$과 $$\cdot G: S/(F)(-n) \to S/(F)$$은 모두 단사이며, 다음 두 short exact sequence를 얻는다.

$$0 \to S(-m) \xrightarrow{\cdot F} S \to S/(F) \to 0$$
$$0 \to S/(F)(-n) \xrightarrow{\cdot G} S/(F) \to S/(F, G) \to 0$$

[명제 9](#prop9)에 의하여 $$S/(F)$$의 Hilbert 다항식은 $$P_F(t) = mt + c_1$$이다. 두 번째 exact sequence의 Hilbert 다항식에 의하여 $$S/(F, G)$$의 Hilbert 다항식은

$$P_{F,G}(t) = P_F(t) - P_F(t - n) = \bigl(mt + c_1\bigr) - \bigl(m(t-n) + c_1\bigr) = mn$$

이다. 즉 $$t \gg 0$$에 대하여 $$(S/(F, G))_t$$의 차원은 상수 $$mn$$이며, 단계 1에 의하여 $$\sum_p i_p(C, D) = mn$$이다.

</details>

## 일반화

<div class="proposition" markdown="1">

<ins id="prop12">**명제 12 (일반화된 Bézout 정리)**</ins> $$\mathbb{P}^n$$ 안의 두 다형체 $$V, W$$에 대해:

$$\deg(V \cap W) \leq \deg(V) \cdot \deg(W)$$

여기서 $$\deg(V \cap W)$$는 $$V \cap W$$의 각 기약성분들의 차수의 합이다. 등호는 $$V$$와 $$W$$가 proper intersection을 가질 때(즉, $$V \cap W$$의 모든 기약성분 $$Z$$에 대하여 $$\operatorname{codim}(Z) = \operatorname{codim}(V) + \operatorname{codim}(W)$$일 때) 성립한다. 이 경우 $$V \cap W$$의 각 성분 $$Z$$에 교차 중복도 $$m_Z$$를 부여하면 $$\sum_Z m_Z \deg(Z) = \deg(V) \cdot \deg(W)$$이다. ([§차원, ⁋예시 14](/ko/math/algebraic_geometry/dimension#ex14))

</div>

<div class="example" markdown="1">

<ins id="ex13">**예시 13 ($$\mathbb{P}^3$$)**</ins> $$\mathbb{P}^3$$ 안의 두 이차곡면(quadric surface) $$Q_1, Q_2$$를 생각하자. $$Q_1$$과 $$Q_2$$는 각각 차수 2이므로, proper intersection을 가질 때 그 교차 $$Q_1 \cap Q_2$$는 차원 1, 차수 $$2 \times 2 = 4$$인 곡선이다. 이 곡선은 타원곡선(genus 1의 매끄러운 곡선)이거나, 유리곡선의 합집합일 수 있다. 구체적으로, $$Q_1 = Z(\x_0\x_3 - \x_1\x_2)$$와 $$Q_2 = Z(\x_0\x_2 - \x_1\x_3)$$를 잡고 교집합을 계산하면, 두 곡면이 모두 포함하는 직선들이 존재하여 교차가 두 개의 conic으로 분해되는 경우를 관찰할 수 있다. 이 경우 교차는 여전히 차수 4이지만, 두 conic의 합집합으로 나타난다.

</div>

명제 1의 $$\mathbb{P}^n$$에서의 일반적인 증명은 Chow 환을 사용한다. 핵심적인 사실은 $$\operatorname{CH}^\ast(\mathbb{P}^n) \cong \mathbb{Z}[H]/(H^{n+1})$$이라는 것이며, 여기서 $$H$$는 hyperplane의 class이다. 차수 $$d_i$$의 초곡면 $$H_i$$는 class $$d_i H$$를 가지며, 따라서 $$n$$개의 초곡면의 교차곱은

$$[H_1] \cdot [H_2] \cdots [H_n] = (d_1 H)(d_2 H) \cdots (d_n H) = d_1 d_2 \cdots d_n \cdot H^n$$

이 된다. $$H^n$$은 $$\mathbb{P}^n$$ 안의 점의 class이고 그 degree는 1이므로, $$\deg(H_1 \cap \cdots \cap H_n) = d_1 \cdots d_n$$을 얻는다.

## 응용

### Cayley-Bacharach 정리

<div class="proposition" markdown="1">

<ins id="prop14">**명제 14 (Cayley-Bacharach 정리의 특수한 경우)**</ins> $$\mathbb{P}^2$$ 안의 두 세차곡선 $$C_1 = Z(F_1)$$, $$C_2 = Z(F_2)$$가 공통 성분을 갖지 않고 9점 $$p_1, \ldots, p_9$$에서 만난다고 하자. 이 때 임의의 세차곡선 $$C_3 = Z(F_3)$$가 $$p_1, \ldots, p_8$$을 지난다면, $$C_3$$는 $$p_9$$도 지난다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

두 세차곡선 $$C_1, C_2$$가 proper intersection으로 서로 다른 9개의 점 $$p_1, \ldots, p_9$$에서 만난다고 가정하자. $$\mathbb{P}^2$$ 위의 차수 3 동차다항식 공간 $$\mathbb{K}[\x_0, \x_1, \x_2]_3$$의 차원은 $$\binom{3+2}{2} = 10$$이며, 각 점 $$p_i$$를 지나는 조건은 하나의 일차조건이므로

$$V = \{F \in \mathbb{K}[\x_0, \x_1, \x_2]_3 : F(p_i) = 0 \text{ for } i = 1, \ldots, 8\}$$

은 차원 $$\dim V \ge 10 - 8 = 2$$인 부분공간이다.

한편 $$F_1, F_2 \in V$$이고 $$C_1 \neq C_2$$이므로 $$F_1, F_2$$는 일차독립이며, 따라서 $$\dim V \ge 2$$이다. $$F_1, F_2$$는 $$C_1 \cap C_2 = \{p_1, \ldots, p_9\}$$를 정의하므로, $$V$$ 안의 임의의 원소 $$F_3$$에 대하여 $$C_3 = Z(F_3)$$와 $$C_1 = Z(F_1)$$의 교차를 생각하면 다음과 같다. 만일 $$F_3$$가 $$F_1$$의 상수배이면 $$C_3 = C_1$$이므로 자명하게 $$p_9 \in C_3$$이다. 그렇지 않으면 $$F_3$$와 $$F_1$$은 공통인 기약인자를 가질 수 없는데, 만일 공통 기약인자 $$G$$가 있다면 $$Z(G) \subseteq C_1 \cap C_3$$이고 $$Z(G)$$는 곡선이므로 $$C_1 \cap C_3$$가 무한집합이 되어야 하지만, $$C_1$$과 $$C_3$$는 차수가 각각 3이고 공통 성분이 없으므로 Bézout의 정리에 의하여 $$\lvert C_1 \cap C_3 \rvert \le 9$$이어서 모순이다. 따라서 $$C_1$$과 $$C_3$$는 공통 성분을 갖지 않고, Bézout의 정리에 의하여 $$\lvert C_1 \cap C_3 \rvert = 9$$이다.

$$F_3 \in V$$이므로 $$C_3$$는 $$p_1, \ldots, p_8$$을 지난다. 이 8점은 모두 $$C_1$$ 위에 있으므로 $$\{p_1, \ldots, p_8\} \subseteq C_1 \cap C_3$$이다. $$\lvert C_1 \cap C_3 \rvert = 9$$이므로 $$C_1 \cap C_3$$의 아홉 번째 점은 $$C_1 \cap C_2 = \{p_1, \ldots, p_9\}$$의 원소여야 한다. 즉 $$C_1 \cap C_3 = \{p_1, \ldots, p_8, p_9\}$$이며, 따라서 $$p_9 \in C_3$$이다.

</details>

이 결과의 직관적인 의미를 생각해보면, 두 세차곡선 $$C_1, C_2$$의 교차 9점 중 8점을 지나는 제약조건이 세차곡선 공간(10차원)에 부과하는 여차원이 정확히 8이어서, 남은 1차원 공간의 원소들이 모두 9번째 점을 지나게 된다는 것이다. 이는 $$3 \times 3 = 9$$라는 Bézout의 정리의 결과가 우연이 아니라는 것을 보여주는 강력한 예시이다.

### Pascal의 정리

<div class="proposition" markdown="1">

<ins id="prop15">**명제 15 (Pascal의 정리)**</ins> 이차곡선(conic) 위의 6점 $$A, B, C, D, E, F$$에 대해, 세 교점

$$P = \overline{AB} \cap \overline{DE},\quad Q = \overline{BC} \cap \overline{EF},\quad R = \overline{CD} \cap \overline{FA}$$

이 모두 존재하면 이 세 점은 공선형(collinear)이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

이차곡선을 $$\Gamma$$라 표기하자. 두 세차곡선

$$X = \overline{AB} \cup \overline{CD} \cup \overline{EF},\quad Y = \overline{BC} \cup \overline{DE} \cup \overline{FA}$$

을 정의하자. 각각은 세 직선의 합집합이므로 차수 3 곡선이다. $$X \cap Y$$를 생각하면, $$A, B, C, D, E, F$$는 모두 $$X$$와 $$Y$$ 위에 있고, $$P, Q, R$$도 $$X$$와 $$Y$$ 위에 있으므로 $$X \cap Y$$는 적어도 9개의 점을 포함한다. Bézout의 정리에 의하여 $$\sum_{p \in X \cap Y} i_p(X, Y) = 3 \times 3 = 9$$이므로, $$X \cap Y = \{A, B, C, D, E, F, P, Q, R\}$$이며 각 점에서의 교차 중복도는 1이다. (특히 $$X$$와 $$Y$$는 공통 성분을 갖지 않는다.)

이제 새로운 세차곡선 $$Z = \Gamma \cup \overline{PQ}$$를 정의하자. 이 역시 차수 $$2 + 1 = 3$$의 곡선이다. $$Z$$는 $$X \cap Y$$의 9점 중 $$A, B, C, D, E, F$$ (이들은 $$\Gamma$$ 위에 있음)와 $$P, Q$$ (이들은 $$\overline{PQ}$$ 위에 있음), 즉 8점을 지난다.

이제 [명제 14](#prop14)를 적용하자. $$X$$와 $$Y$$는 공통 성분이 없는 두 세차곡선으로서 9점에서 만나며, $$Z$$는 이 중 8점을 지나는 세차곡선이다. 따라서 명제 14에 의하여 $$Z$$는 9번째 점 $$R$$도 지나야 한다. $$R$$을 쓰는 방법을 생각해보면, $$R \in Z = \Gamma \cup \overline{PQ}$$이므로 $$R \in \Gamma$$이거나 $$R \in \overline{PQ}$$이다.

만일 $$R \in \Gamma$$라고 하자. 그러면 $$R = \overline{CD} \cap \overline{FA} \in \Gamma$$이어야 한다. $$\Gamma$$ 위에는 이미 $$C, D$$가 있고, $$\overline{CD}$$와 $$\Gamma$$는 Bézout의 정리에 의하여 차수 $$1 \times 2 = 2$$이므로 최대 2점에서 만난다. 즉 $$\overline{CD} \cap \Gamma = \{C, D\}$$이며, 마찬가지로 $$\overline{FA} \cap \Gamma = \{F, A\}$$이다. 따라서 $$R \notin \overline{CD} \cap \Gamma$$이고 $$R \notin \overline{FA} \cap \Gamma$$이므로 $$R \in \Gamma$$일 수 없다. 결론적으로 $$R \in \overline{PQ}$$이며, 즉 $$P, Q, R$$은 공선형이다.

</details>

### 이중점의 최대 개수

Bézout의 정리를 사용하여 평면곡선이 가질 수 있는 특이점의 개수에 대한 상계를 얻을 수 있다.

<div class="proposition" markdown="1">

<ins id="prop16">**명제 16**</ins> 차수 $$d$$ 기약평면곡선이 가질 수 있는 최대 ordinary double point(서로 다른 두 접선을 갖는 이중점)의 개수는 $$\binom{d-1}{2} = \frac{(d-1)(d-2)}{2}$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

차수 $$d$$ 기약곡선 $$C$$ 위에 $$n$$개의 ordinary double point $$p_1, \ldots, p_n$$이 있다고 하자. 즉 각 $$p_i$$에서 $$C$$는 서로 다른 두 개의 접선을 갖는다. $$C$$는 기약이므로 기약다항식 $$F$$에 의하여 정의된다.

**단계 1.** 먼저 약한 상계를 얻기 위해, 일반적인 직선 $$L$$과 곡선 $$C$$의 교점을 생각하자. 각 ordinary double point $$p_i$$에서 곡선 $$C$$는 서로 다른 두 접선을 갖는다. 일반적인 직선 $$L$$은 이 접선들과 다른 방향이므로 [명제 8](#prop8)에 의하여 $$i_{p_i}(C, L) = 1$$이다. [명제 10](#prop10)과 Bézout의 정리에 의하여 $$\sum_{p \in C \cap L} i_p(C, L) = d$$이다. $$C$$가 기약이므로 $$C \neq L$$이며 교점이 존재한다.

각 $$p_i$$는 $$C \cap L$$에 속하므로 $$n$$개의 교점이 각각 중복도 1로 세어지고, 그 합만으로 $$n$$이다. 나머지 교점들의 중복도 합이 $$d - n$$이므로 $$d \geq n$$, 즉 $$n \leq d$$이다. 더 강한 상계는 단계 2에서 genus-degree 공식을 통해 얻는다.

**단계 2.** 더 정밀한 상계를 얻기 위해, genus-degree 공식을 사용한다. 곡선의 *genus*(기하학적 종수, geometric genus) $$g$$는 곡선을 normalization(정규화, 특이점을 모두 풀어 매끄러운 곡선을 얻는 과정)한 결과로 얻는 매끄러운 곡선의 genus이다. 매끄러운 사영 평면 곡선의 genus는 $$(d-1)(d-2)/2$$로 주어지며, 이를 *genus-degree 공식*이라 한다. 특이점이 있는 기약 평면 곡선의 경우, 각 특이점 $$p$$에서의 *$$\delta$$-invariant* $$\delta_p$$는 해당 특이점의 '복잡도'를 측정하는 양으로, normalization에서 해당 점 위에 놓이는 점들의 수와 관련된다. 기하학적 genus와 $$\delta$$-invariant 사이의 관계는

$$g = \frac{(d-1)(d-2)}{2} - \sum_{i=1}^n \delta_{p_i}$$

이다. Ordinary double point의 $$\delta$$-invariant는 $$\delta_{p_i} = 1$$이다. 기하학적 genus는 음수가 될 수 없으므로

$$\frac{(d-1)(d-2)}{2} - n \geq 0$$

이고, 따라서 $$n \leq \frac{(d-1)(d-2)}{2}$$이다. 이 상계는 달성 가능하다. 예를 들어, 매끄러운 차수 $$d$$ 곡선을 일반적인 사영(projection)하여 $$\mathbb{P}^2$$ 위에 놓이게 하면, 정확히 $$\frac{(d-1)(d-2)}{2}$$개의 ordinary double point를 갖는 기약 곡선을 얻을 수 있다.

</details>

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[Ful]** W. Fulton, *Intersection Theory*, Springer, 1984.  
**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.
