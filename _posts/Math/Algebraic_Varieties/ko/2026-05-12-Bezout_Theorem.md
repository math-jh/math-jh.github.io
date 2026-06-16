---
title: "베주 정리"
description: "대수기하학의 베주 정리는 대수적으로 닫힌 체 위의 사영 공간에서, 공통 성분을 갖지 않는 두 곡선이 교차하는 점의 수가 두 곡선의 차수의 곱과 같다는 결과이다. 교점의 중복도를 고려하면 두 이차곡선은 정확히 네 점에서 만난다."
excerpt: "Bézout's theorem and its applications"

categories: [Math / Algebraic Varieties]
permalink: /ko/math/algebraic_varieties/bezout_theorem
sidebar: 
    nav: "algebraic_varieties-ko"

date: 2026-03-15
weight: 20

---

우리는 이번 글에서 대수기하학의 고전적인 정리인 베주 정리를 소개한다. 직관적으로, 평면 위의 두 곡선 $$C,D$$가 주어졌다 하자. 그럼 $$C$$와 $$D$$가 만나는 교점의 개수는 이들의 차수에 의족하는데, 가령 평면 위에서 정의된 이차곡선 $$\y=x^2$$과 직선은 일반적으로 두 점에서 만난다. 베주 정리는 이를 일반화한 결과이다.

<div class="proposition" markdown="1">

<ins id="prop1">**명제 1 (Bézout)**</ins> Algebraically closed field 위에서 정의된 $$\mathbb{P}^n$$ 안에서, 차수 $$d_1, \ldots, d_n$$의 hypersurface $$H_1, \ldots, H_n$$이 공통 성분을 갖지 않는다면

$$\deg(H_1 \cap \cdots \cap H_n) = d_1 \cdots d_n$$

이 성립한다. 여기서 intersection은 multiplicity를 고려한 것이다. 

</div>

특히 $$\mathbb{P}^2$$ 안에서 차수 $$m,n$$인 두 곡선은 $$mn$$개의 점에서 만난다. 다소 주의할 것은 이들이 공통 성분을 가지면 안된다는 것으로, 가령 서로 같은 두 곡선은 이를 통해 교집합을 계산할 수 없다. 

<div class="example" markdown="1">

<ins id="ex2">**예시 2 (두 이차곡선)**</ins> $$\mathbb{P}^2$$ 안의 두 이차곡선

$$C_1 = Z(\x_0^2 + \x_1^2 - \x_2^2),\qquad C_2 = Z(\x_0\x_1)$$

을 생각하자. $$C_1$$은 원뿔의 사영화이고, $$C_2$$는 두 직선 $$Z(\x_0)$$과 $$Z(\x_1)$$의 합집합이다. 이 두 곡선은 공통 성분을 갖지 않으므로 Bézout의 정리에 의하여 $$2 \times 2 = 4$$개의 교점을 가져야 한다. 실제로 교집합을 계산해보면, $$\x_0 = 0$$일 때 $$\x_1^2 = \x_2^2$$이 되어 $$[0:1:1]$$과 $$[0:1:-1]$$을 얻고, $$\x_1 = 0$$일 때 $$\x_0^2 = \x_2^2$$이 되어 $$[1:0:1]$$과 $$[1:0:-1]$$을 얻어 정확히 4점에서 만남을 확인할 수 있다.

</div>

## 증명

우리는 일반적인 경우에 증명을 하는 대신, $$\mathbb{P}^2$$에서의 Bézout theorem만 증명한다. 이를 위해 다음 보조정리를 사용한다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3 (Hilbert polynomial)**</ins> Projective variety $$X \subseteq \mathbb{P}^n$$의 homogeneous coordinate ring $$S(X)$$에 대하여, 함수 $$H(t) = \dim_\mathbb{K} S(X)_t$$를 $$X$$의 **Hilbert 함수**라 한다. Hilbert-Serre 정리에 의하면 이 함수는 $$t \gg 0$$에서 다항식 $$P_X(t)$$와 일치하며, 이 다항식을 $$X$$의 **Hilbert polynomial**이라 한다.

특히 차수 $$d$$인 곡선 $$C = Z(F) \subseteq \mathbb{P}^2$$의 경우, $$S(C) = \mathbb{K}[\x_0, \x_1, \x_2]/(F)$$의 Hilbert polynomial은

$$P_C(t) = dt + \frac{d(3-d)}{2}$$

이다. 여기서 $$P_C$$의 차수는 $$C$$의 차원인 $$1$$이고, 최고차항 계수는 $$\deg C = d$$이며, 상수항 $$P_C(0) = \frac{d(3-d)}{2} = 1 - \frac{(d-1)(d-2)}{2}$$는 $$C$$의 arithmetic genus이다.

</div>

Hilbert 함수 $$H(t)$$는 차수 $$t$$인 동차다항식 공간의 원소 가울데 $$C$$ 위에서 0이 되는 것들을 제거한 후 남은 독립적인 원소의 개수, 즉 $$C$$ 위에서 서로 다른 함수로 작용하는 동차다항식들의 개수이다. $$t$$가 커질수록 이 수는 다항식처럼 자라며, 그 차수는 $$C$$의 차원인 $$1$$과 같고, 최고차항 계수는 차수 $$d$$와 비례하며, 상수항은 arithmetic genus $$1 - \frac{(d-1)(d-2)}{2}$$와 같다.

<details class="proof" markdown="1">
<summary>증명</summary>

$$S = \mathbb{K}[\x_0, \x_1, \x_2]$$라 하자. $$(S/(F))_t$$의 차원은 $$S_t$$에서 $$F$$의 배수들을 제거하여 얻는 공간의 차원과 같다. 곱셈 $$\cdot F: S(-d) \to S$$는 단사이므로 다음 short exact sequence를 얻는다.

$$0 \to S(-d) \xrightarrow{\cdot F} S \to S/(F) \to 0$$

$$\dim_\mathbb{K} S_t = \binom{t+2}{2}$$이므로, degree $$t$$ 부분의 차원을 비교하면

$$\dim_\mathbb{K} (S/(F))_t = \binom{t+2}{2} - \binom{t-d+2}{2}$$

이다. 이를 전개하면

$$\frac{(t+2)(t+1)}{2} - \frac{(t-d+2)(t-d+1)}{2} = dt + \frac{d(3-d)}{2}$$

를 얻는다.

</details>

이 결과는 이어지는 [명제 5](#prop5)의 증명에서 핵심적으로 사용된다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> $$\mathbb{P}^2$$ 안의 차수 $$d$$ 곡선 $$C = Z(F)$$에 대하여, 임의의 일반적인 직선 $$L$$과의 교차 $$C \cap L$$은 정확히 $$d$$개의 점(중복도 포함)으로 이루어진다.

</div>

이 명제는 Bézout 정리의 가장 단순한 특수 경우이다. 차수 $$d$$ 곡선이 일반적인 직선과 $$d$$점에서 만난다는 기하학적 직관을 제공한다.

<details class="proof" markdown="1">
<summary>증명</summary>

일반성을 잃지 않고 $$L = Z(\x_2)$$라 하자. $$C$$가 차수 $$d$$ 동차다항식 $$F(\x_0, \x_1, \x_2)$$로 정의되므로, $$L \cap C$$에서 $$\x_2 = 0$$을 대입하면 $$F(\x_0, \x_1, 0)$$을 얻는다. 이는 $$\x_0, \x_1$$에 관한 차수 $$d$$ 동차다항식이며, 대수적으로 닫힌 체 위에서 정확히 $$d$$개의 근을 갖는다(중복도 포함). $$L$$이 일반적이므로 $$F(\x_0, \x_1, 0)$$은 영다항식이 아니며, 만일 그렇다면 $$\x_2$$가 $$F$$의 인수가 되어 $$C$$가 $$L$$을 성분으로 갖게 되어 가정에 모순된다.

</details>

이제 명제 1을 증명한다. 핵심은 두 가지이다. 먼저 교차 중복도의 합이 전역적인 대수적 대상의 차원과 일치함을 보이고, 둘째로 그 차원을 Hilbert 다항식으로 정확히 $$mn$$으로 계산하는 것이다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> (명제 1의 증명) $$\mathbb{P}^2$$ 안의 차수 $$m$$, $$n$$인 두 곡선 $$C = Z(F)$$, $$D = Z(G)$$가 공통 성분을 갖지 않으면 $$\sum_p i_p(C, D) = mn$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

두 단계로 나누어 증명한다.

**단계 1.** 먼저 다음 등식을 보인다.

> $$\sum_{p \in C \cap D} i_p(C, D) = \dim_\mathbb{K} (\mathbb{K}[\x_0, \x_1, \x_2]/(F, G))_t \qquad (t \gg 0)$$

$$C \cap D$$가 유한집합임은 $$C$$와 $$D$$가 공통 성분을 갖지 않는다는 가정으로부터 알려져 있다. ([§차원, ⁋예시 14](/ko/math/algebraic_varieties/dimension#ex14)) 점 $$p = [a:b:c] \in C \cap D$$에 대하여, $$c \neq 0$$이라 가정하면 $$U_2$$에서의 좌표로 $$p = (a/c, b/c)$$이고, $$F, G$$를 dehomogenize한 $$f, g \in \mathbb{K}[\x, \y]$$에 대하여

$$i_p(C, D) = \dim_\mathbb{K} \mathcal{O}_{\mathbb{A}^2, p}/(f, g)$$

이다. $$V(F, G)$$가 유한집합이므로 $$f, g$$는 affine ring $$\mathbb{K}[\x, \y]$$에서 0차원 ideal $$(f, g)$$을 생성하며, 중국인의 나머지 정리에 의하여

$$\mathbb{K}[\x, \y]/(f, g) \cong \prod_{p \in V(f,g)} \mathcal{O}_{\mathbb{A}^2, p}/(f, g)$$

이다. 따라서 $$\dim_\mathbb{K} \mathbb{K}[\x, \y]/(f, g) = \sum_p i_p(C, D)$$이다.

한편, $$S = \mathbb{K}[\x_0, \x_1, \x_2]$$의 몫 $$R = S/(F, G)$$의 Hilbert 함수 $$H(t) = \dim_\mathbb{K} R_t$$는 $$t \gg 0$$에서 상수가 되며(단계 2에서 증명), 이 상숫값은 $$\dim_\mathbb{K} \mathbb{K}[\x, \y]/(f, g)$$와 같다. 이는 $$t \gg 0$$일 때 차수 $$t$$가 충분히 크면 각 교점에서의 값을 독립적으로 조절할 수 있는 다항식이 존재하여, 평가 사상 $$R_t \to \mathbb{K}^{\lvert V(F,G) \rvert}$$이 전사가 되기 때문이다.

**단계 2.** 이제 $$\dim_\mathbb{K} (\mathbb{K}[\x_0, \x_1, \x_2]/(F, G))_t = mn$$임을 보인다($$t \gg 0$$). $$S = \mathbb{K}[\x_0, \x_1, \x_2]$$라 쓰자. $$F, G$$가 공통인 기약인자를 갖지 않으므로 곱셈사상 $$\cdot F: S(-m) \to S$$과 $$\cdot G: S/(F)(-n) \to S/(F)$$은 모두 단사이며, 다음 두 short exact sequence를 얻는다.

$$0 \to S(-m) \xrightarrow{\cdot F} S \to S/(F) \to 0$$
$$0 \to S/(F)(-n) \xrightarrow{\cdot G} S/(F) \to S/(F, G) \to 0$$

명제 3([명제 3](#prop3))에서 차수를 $$m$$으로 읽으면, $$S/(F)$$의 Hilbert 다항식은 $$P_F(t) = mt + c_1$$의 꼴이 된다. 두 번째 exact sequence에 Hilbert 다항식을 적용하면 $$S/(F, G)$$의 Hilbert 다항식은

$$P_{F,G}(t) = P_F(t) - P_F(t - n) = \bigl(mt + c_1\bigr) - \bigl(m(t-n) + c_1\bigr) = mn$$

이다. 즉 $$t \gg 0$$에 대하여 $$(S/(F, G))_t$$의 차원은 상수 $$mn$$이며, 단계 1에 의하여 $$\sum_p i_p(C, D) = mn$$이다.

</details>

## 일반화

지금까지는 $$\mathbb{P}^2$$의 곡선에 대해서만 Bézout 정리를 증명했다. 이를 임의의 사영공간과 일반적인 사영다양체로 확장하려면 Chow ring이 필요하다. 핵심 사실은

$$\operatorname{CH}^\ast(\mathbb{P}^n) \cong \mathbb{Z}[H]/(H^{n+1})$$

이다. 여기서 $$H$$는 hyperplane class이며, codimension이 $$k$$이며 차수가 $$d$$인 다양체는 class $$dH^k$$를 갖는다. 특히 차수 $$d$$인 hypersurface는 $$dH$$에 대응하므로, $$n$$개의 hypersurface $$H_1, \ldots, H_n$$의 교차곱은

$$[H_1] \cdot [H_2] \cdots [H_n] = (d_1 H)(d_2 H) \cdots (d_n H) = d_1 d_2 \cdots d_n \cdot H^n$$

이 된다. $$H^n$$은 $$\mathbb{P}^n$$ 안의 점의 class이고 그 degree가 1이므로, $$\deg(H_1 \cap \cdots \cap H_n) = d_1 \cdots d_n$$을 얻는다. 이 직관 하에서 일반화된 Bézout 정리는 다음과 같이 서술된다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6 (일반화된 Bézout 정리)**</ins> $$\mathbb{P}^n$$ 안의 두 사영다양체 $$V, W$$에 대해

$$\deg(V \cap W) \leq \deg(V) \cdot \deg(W)$$

이 성립한다. 여기서 $$\deg(V \cap W)$$는 $$V \cap W$$의 각 기약 성분들의 차수의 합이다. 등호는 $$V$$와 $$W$$가 proper intersection을 가질 때 (즉 $$V \cap W$$의 모든 기약성분 $$Z$$에 대해 $$\operatorname{codim}(Z) = \operatorname{codim}(V) + \operatorname{codim}(W)$$일 때) 성립하며, 이 경우 각 성분 $$Z$$에 교차 중복도 $$m_Z$$를 부여하면 $$\sum_Z m_Z \deg(Z) = \deg(V) \cdot \deg(W)$$이다.

</div>

<div class="example" markdown="1">

<ins id="ex7">**예시 7 ($$\mathbb{P}^3$$)**</ins> $$\mathbb{P}^3$$ 안의 두 이차곡면(quadric surface) $$Q_1, Q_2$$를 생각하자. 각각 차수 2이므로 proper intersection을 가질 때 교차 $$Q_1 \cap Q_2$$는 차원 1, 차수 4인 곡선이다. 구체적으로, $$Q_1 = Z(\x_0\x_3 - \x_1\x_2)$$와 $$Q_2 = Z(\x_0\x_2 - \x_1\x_3)$$를 잡으면 교차는 네 개의 직선(line)으로 분해되며, 이들의 차수 합은 여전히 4이다.

</div>

명제 6의 증명은 Chow ring을 통한 교차이론의 일반론에 의존한다. 자세한 내용은 ([§교차곱](/ko/math/algebraic_varieties/intersection_product))을 참조하라. ([§차원, ⁋예시 14](/ko/math/algebraic_varieties/dimension#ex14))의 부등식이 성분의 codimension에 대한 것으로 다시 나타난다.

## 응용

### Cayley-Bacharach 정리

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8 (Cayley-Bacharach 정리의 특수한 경우)**</ins> $$\mathbb{P}^2$$ 안의 두 세차곡선 $$C_1 = Z(F_1)$$, $$C_2 = Z(F_2)$$가 공통 성분을 갖지 않고, 서로 다른 9점 $$p_1, \ldots, p_9$$에서 proper intersection으로 만난다고 하자. 이 때 임의의 세차곡선 $$C_3 = Z(F_3)$$가 $$p_1, \ldots, p_8$$을 지난다면, $$C_3$$는 $$p_9$$도 지난다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

두 세차곡선 $$C_1, C_2$$가 proper intersection으로 서로 다른 9개의 점 $$p_1, \ldots, p_9$$에서 만난다고 가정하자. $$\mathbb{P}^2$$ 위의 차수 3 동차다항식 공간 $$\mathbb{K}[\x_0, \x_1, \x_2]_3$$의 차원은 $$\binom{3+2}{2} = 10$$이며, 각 점 $$p_i$$를 지나는 조건은 하나의 일차조건이므로 $$V = \{F \in \mathbb{K}[\x_0, \x_1, \x_2]_3 : F(p_i) = 0 \text{ for } i = 1, \ldots, 8\}$$은 차원 $$\dim V \ge 10 - 8 = 2$$인 부분공간이다. 한편 $$F_1, F_2 \in V$$이고 $$C_1 \neq C_2$$이므로 $$F_1, F_2$$는 일차독립이다. 8개의 점이 일반적인 위치에 있다면 $$\dim V = 2$$이며, $$F_1, F_2$$가 $$V$$의 기저를 이룬다. 따라서 임의의 $$F_3 \in V$$에 대해 상수 $$\alpha, \beta$$가 존재하여 $$F_3 = \alpha F_1 + \beta F_2$$이다. 양변에 $$p_9$$를 대입하면 $$F_3(p_9) = \alpha F_1(p_9) + \beta F_2(p_9) = 0$$이므로 $$C_3$$는 $$p_9$$도 지난다.</details>

이 결과의 직관은 다음과 같다. 두 세차곡선의 교차 9점 중 8점을 지나는 조건은 세차곡선 공간(10차원)에 8개의 선형 제약을 부과하여, 남은 1차원 공간의 원소들이 모두 9번째 점도 지나게 된다. 이는 $$3 \times 3 = 9$$라는 Bézout 정리의 결과가 우연이 아님을 보여준다.

### Pascal의 정리

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9 (Pascal의 정리)**</ins> 이차곡선(conic) 위의 6점 $$A, B, C, D, E, F$$에 대해, 세 교점

$$P = \overline{AB} \cap \overline{DE},\quad Q = \overline{BC} \cap \overline{EF},\quad R = \overline{CD} \cap \overline{FA}$$

이 모두 존재하면 이 세 점은 공선형(collinear)이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

이차곡선을 $$\Gamma$$라 표기하자. 두 세차곡선

$$X = \overline{AB} \cup \overline{CD} \cup \overline{EF},\quad Y = \overline{BC} \cup \overline{DE} \cup \overline{FA}$$

을 정의하자. 각각은 세 직선의 합집합이므로 차수 3 곡선이다. 일반적인 위치 가정 하에 $$X$$와 $$Y$$는 공통 성분을 갖지 않는다.

$$X \cap Y$$는 $$A, B, C, D, E, F$$와 $$P, Q, R$$을 모두 포함하므로 적어도 9개의 서로 다른 점을 포함한다. Bézout의 정리에 의하여 $$\sum_{p \in X \cap Y} i_p(X, Y) = 3 \times 3 = 9$$이므로, $$X \cap Y$$는 정확히 이 9점이며 각 점에서의 교차 중복도는 1이다.

이제 새로운 세차곡선 $$Z = \Gamma \cup \overline{PQ}$$를 정의하자. 이는 차수 3의 곡선으로, $$X \cap Y$$의 9점 중 $$A, B, C, D, E, F$$와 $$P, Q$$, 즉 8점을 지난다. 명제 8([명제 8](#prop8))에 의하여 $$Z$$는 9번째 점 $$R$$도 지나야 한다. $$R \in Z = \Gamma \cup \overline{PQ}$$이므로, $$R \in \Gamma$$이거나 $$R \in \overline{PQ}$$이다.

만일 $$R \in \Gamma$$라면 $$R = \overline{CD} \cap \overline{FA} \in \Gamma$$이어야 한다. 그러나 $$\overline{CD}$$와 $$\Gamma$$는 Bézout의 정리에 의해 최대 2점에서 만나며, 이미 $$C, D \in \Gamma$$이므로 $$\overline{CD} \cap \Gamma = \{C, D\}$$이다. 마찬가지로 $$\overline{FA} \cap \Gamma = \{F, A\}$$이므로 $$R \in \Gamma$$일 수 없다. 결론적으로 $$R \in \overline{PQ}$$이며, 즉 $$P, Q, R$$은 공선형이다.

</details>

### 이중점의 최대 개수

Bézout 정리로 평면곡선의 특이점 개수에 대한 상계를 얻을 수 있다.

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10**</ins> 차수 $$d$$ 기약평면곡선이 가질 수 있는 최대 ordinary double point(서로 다른 두 접선을 갖는 이중점)의 개수는 $$\binom{d-1}{2} = \frac{(d-1)(d-2)}{2}$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

차수 $$d$$ 기약곡선 $$C$$ 위에 $$n$$개의 ordinary double point $$p_1, \ldots, p_n$$이 있다고 하자. 곡선의 *genus*(기하학적 종수) $$g$$는 normalization으로 얻는 매끄러운 곡선의 genus이다. 매끄러운 사영 평면 곡선의 genus는 *genus-degree 공식*에 의해 $$(d-1)(d-2)/2$$이며, 특이점이 있는 경우 각 특이점 $$p$$의 *$$\delta$$-invariant* $$\delta_p$$만큼 genus가 감소한다. Ordinary double point의 $$\delta$$-invariant는 $$\delta_{p_i} = 1$$이다. 따라서

$$g = \frac{(d-1)(d-2)}{2} - \sum_{i=1}^n \delta_{p_i} = \frac{(d-1)(d-2)}{2} - n$$

이고, 기하학적 genus는 음수가 될 수 없으므로

$$n \leq \frac{(d-1)(d-2)}{2}$$

이다. 이 상계는 달성 가능하다. 예를 들어 매끄러운 차수 $$d$$ 곡선을 일반적인 사영(projection)으로 $$\mathbb{P}^2$$에 놓으면, 정확히 $$\frac{(d-1)(d-2)}{2}$$개의 ordinary double point를 갖는 기약 곡선을 얻는다.

</details>

---

**참고문헌**

**[Hart]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[Ful]** W. Fulton, *Intersection Theory*, Springer, 1984.  
**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.
