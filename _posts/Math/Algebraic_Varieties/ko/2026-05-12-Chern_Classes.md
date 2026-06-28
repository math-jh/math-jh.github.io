---
title: "천 특성류"
description: "복소 벡터다발의 뒤틀림을 재는 천 특성류를 공리적으로 정의하고, 직선다발에서의 기하학적 의미, splitting principle, 천 지표를 거쳐 접다발과 Euler 지표의 관계 및 구체적 계산을 다룬다."
excerpt: "벡터다발의 Chern classes와 그 성질들"

categories: [Math / Algebraic Varieties]
permalink: /ko/math/algebraic_varieties/chern_classes
sidebar: 
    nav: "algebraic_varieties-ko"

date: 2026-05-12
weight: 22
published: false
---

벡터다발은 대수기하학에서 기하적 대상을 다루는 핵심 도구이며, 이번 글에서는 주어진 벡터다발이 얼마나 뒤틀려 있는지를 재는 *Chern class*를 정의한다. 이는 complex vector bundle에 대해 정의되는 위상적·기하학적 불변량으로, 대수위상에서와 마찬가지로 공리적으로 정의한 뒤, 직선다발에서의 기하학적 의미를 보고, 계산의 핵심인 splitting principle을 거쳐, 접다발의 천 특성류와 Euler 지표의 관계 및 구체적 계산까지 다룬다. 모든 논의는 적당한 base space $$X$$ 위의 complex vector bundle에 대해 이루어지며, cohomology는 $$H^\bullet(X, \mathbb{Z})$$를 사용한다. Cohomology convention상 $$k$$차 Chern class가 $$2k$$차 cohomology에 들어감을 기억하자.

## 천 특성류의 공리

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Complex vector bundle $$\mathcal{E} \to X$$마다 cohomology class $$c_i(\mathcal{E}) \in H^{2i}(X, \mathbb{Z})$$ ($$i \geq 0$$, $$c_0(\mathcal{E})=1$$)가 주어지며, 이들을 *Chern class<sub>천 특성류</sub>*라 부른다. 이들은 다음 공리를 만족한다.

1. (*Naturality*) 연속사상 $$f: Y \to X$$에 대하여 $$c_i(f^{\ast}\mathcal{E}) = f^{\ast}c_i(\mathcal{E})$$이다. 여기서 $$f^{\ast}$$은 cohomology에서의 pullback이다.
2. (*Whitney sum formula*) 두 vector bundle $$\mathcal{E}, \mathcal{F}$$에 대하여 $$c(\mathcal{E} \oplus \mathcal{F}) = c(\mathcal{E}) \smile c(\mathcal{F})$$이다. 여기서 $$c(\mathcal{E}) = \sum_{i \geq 0} c_i(\mathcal{E})$$는 *total Chern class*이고 우변은 cup product이다.
3. (*Normalization*) line bundle $$\mathcal{L} \to X$$에 대하여 $$c(\mathcal{L}) = 1 + c_1(\mathcal{L})$$이고, $$\mathbb{P}^n$$ 위의 hyperplane bundle $$\mathcal{O}(1)$$에 대하여 $$c_1(\mathcal{O}(1))$$은 $$H^2(\mathbb{P}^n, \mathbb{Z}) \cong \mathbb{Z}$$의 생성원이다.

</div>

공리는 Chern class를 직접 구성하지 않고 그것이 따라야 할 규칙만 못박는다. Naturality는 Chern class가 다발의 위상적 정보만에 의존함을, Whitney 공식은 직합을 곱으로 옮김을, normalization은 가장 단순한 다발인 직선다발에서의 값을 고정한다. 놀랍게도 이 세 규칙만으로 Chern class가 유일하게 결정되고 또 실제로 존재하는데, 이는 splitting principle을 확립한 뒤 [명제 6](#prop6)에서 증명한다. 한편 rank $$r$$ 다발에서는 $$c_i(\mathcal{E}) = 0$$ ($$i > r$$)이므로 total Chern class는 $$c(\mathcal{E}) = 1 + c_1(\mathcal{E}) + \cdots + c_r(\mathcal{E})$$로 끝난다.

## 직선다발의 천 특성류

Chern class는 일반적으로 직접 계산하기 어렵지만, 직선다발에 대해서는 완전히 기하학적으로 이해되며, 이 경우가 이후 모든 계산의 토대가 된다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> $$X$$가 smooth variety이고 $$\mathcal{L} \to X$$가 line bundle이라 하자. $$\mathcal{L}$$의 영이 아닌 유리 section $$s$$의 zero divisor $$D = \divisor(s)$$에 대하여

$$c_1(\mathcal{L}) = [D] \in H^2(X, \mathbb{Z})$$

이며, 이 class는 $$s$$의 선택에 의존하지 않는다. 여기서 $$[D]$$는 divisor $$D$$의 cycle class이다. 특히 $$\mathcal{L} = \mathcal{O}_X(D)$$이면 $$c_1(\mathcal{O}_X(D)) = [D]$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

exponential exact sequence

$$0 \to \mathbb{Z} \to \mathcal{O}_X \xrightarrow{f\mapsto e^{2\pi if}} \mathcal{O}_X^{\ast} \to 0$$

의 long exact sequence는 connecting homomorphism $$\delta: H^1(X, \mathcal{O}_X^{\ast}) \to H^2(X, \mathbb{Z})$$를 준다. Line bundle은 transition cocycle $$\{g_{\alpha\beta}\} \in H^1(X, \mathcal{O}_X^{\ast})$$로 분류되며 ([§선다발과 벡터다발](/ko/math/algebraic_varieties/line_bundles)), $$c_1(\mathcal{L}) = \delta([\mathcal{L}])$$이 위상적 $$c_1$$과 일치한다. 한편 section $$s$$를 국소적으로 $$s_\alpha$$로 적으면 $$s_\alpha = g_{\alpha\beta}s_\beta$$이고 $$D = \divisor(s)$$는 국소방정식 $$s_\alpha = 0$$으로 주어지므로, $$\delta$$를 추적하면 $$\delta([\mathcal{L}])$$이 $$D$$의 cycle class $$[D]$$와 일치한다. 다른 section $$s'$$를 택하면 $$s'/s$$가 전역 유리함수이므로 $$\divisor(s') - \divisor(s) = \divisor(s'/s)$$는 principal divisor이고, principal divisor의 cycle class는 $$0$$이므로 $$[D]$$는 $$s$$에 무관하다. 위상적 추적의 자세한 계산은 [Har], [BT]로 미룬다.

</details>

즉 직선다발의 $$c_1$$은 임의의 section의 영점 자리이며 그 class는 section 선택에 무관한데, 이것이 Chern class의 기하학적 원형이다. 대수적으로는 이 등식이 $$\CH^1(X) = \mathrm{Pic}(X)$$에서 성립하고, cycle class map을 거쳐 $$H^2(X, \mathbb{Z})$$로 보내진 것이 위의 명제이다. 같은 그림이 높은 rank로도 이어진다. Globally generated rank $$r$$ 다발 $$\mathcal{E}$$의 generic section $$s$$는 codimension $$r$$의 영점자리 $$Z(s)$$를 가지며 그 class가 top Chern class $$c_r(\mathcal{E})$$이다. 더 일반적으로 generic section $$s_1, \ldots, s_{r-p+1}$$을 택하면, 이들이 fiber에서 일차종속이 되는 점들의 자리인 *degeneracy locus*는 codimension $$p$$의 cycle이고 그 class가 $$c_p(\mathcal{E})$$이다 ([Ful]). 요컨대 $$c_p(\mathcal{E})$$는 "$$\mathcal{E}$$가 $$r-p+1$$개의 독립 section을 갖지 못하게 하는 obstruction"을 재는 cycle이다.

직선다발의 텐서곱·쌍대는 $$c_1$$과 다음과 같이 잘 맞물린다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> 같은 base $$X$$ 위의 line bundle $$\mathcal{L}, \mathcal{M}$$에 대하여 다음이 성립한다.

1. $$c_1(\mathcal{L} \otimes \mathcal{M}) = c_1(\mathcal{L}) + c_1(\mathcal{M})$$,
2. $$c_1(\mathcal{L}^{\vee}) = -c_1(\mathcal{L})$$.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Line bundle은 transition cocycle로 $$H^1(X, \mathcal{O}_X^{\ast})$$의 원소를 주며, tensor product는 cocycle의 곱(즉 $$H^1$$에서의 덧셈)에, dual은 역원에 대응한다. [명제 2](#prop2)의 $$c_1 = \delta$$는 group homomorphism $$H^1(X, \mathcal{O}_X^{\ast}) \to H^2(X, \mathbb{Z})$$이므로 곱을 합으로, 역원을 음수로 보낸다. 따라서 1과 2가 성립한다. divisor의 언어로도 같은 결론을 얻는다. $$\mathcal{L} = \mathcal{O}_X(D)$$, $$\mathcal{M} = \mathcal{O}_X(E)$$이면 $$\mathcal{L} \otimes \mathcal{M} = \mathcal{O}_X(D+E)$$, $$\mathcal{L}^{\vee} = \mathcal{O}_X(-D)$$이므로 [명제 2](#prop2)로부터 $$c_1$$이 더해지고 부호가 뒤집힌다.

</details>

이처럼 직선다발에서는 $$c_1$$이 $$\mathrm{Pic}(X) \to H^2(X, \mathbb{Z})$$의 group homomorphism으로 완전히 이해된다. 일반적인 vector bundle은 직선다발들의 직합으로 분해되지 않지만, 이는 실계수 다항식이 실수 위에서는 인수분해되지 않아도 복소수로 올라가면 일차식들로 쪼개지는 것과 같다. 다음의 splitting principle은 이 "확장"의 기하학적 버전으로, 임의의 다발의 Chern class 계산을 직선다발의 경우로 환원해 준다.

## 사영다발 공식과 splitting principle

임의의 다발을 직선다발로 쪼개는 출발점은 그 사영화 위의 cohomology 구조이다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4 (사영다발 공식)**</ins> $$\pi: \mathbb{P}(\mathcal{E}) \to X$$를 rank $$r$$ vector bundle $$\mathcal{E}$$의 projectivization이라 하고 $$\xi = c_1(\mathcal{O}_\mathcal{E}(1)) \in H^2(\mathbb{P}(\mathcal{E}))$$라 하자. 그러면 $$H^{\ast}(\mathbb{P}(\mathcal{E}))$$는 $$\{1, \xi, \ldots, \xi^{r-1}\}$$을 자유 기저로 갖는 $$H^{\ast}(X)$$-module이며, $$H^{\ast}(X)$$-algebra로서

$$H^{\ast}(\mathbb{P}(\mathcal{E})) \cong H^{\ast}(X)[\xi] / \bigl(\xi^r + \pi^{\ast}c_1(\mathcal{E})\xi^{r-1} + \cdots + \pi^{\ast}c_r(\mathcal{E})\bigr)$$

이다. 특히 $$\pi^{\ast}$$은 단사이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

각 fiber $$\pi^{-1}(x) \cong \mathbb{P}^{r-1}$$ 위에서 $$\xi$$는 hyperplane class로 제한되므로, $$1, \xi, \ldots, \xi^{r-1}$$은 fiber cohomology $$H^{\ast}(\mathbb{P}^{r-1})$$의 기저로 제한된다. Leray–Hirsch 정리 ([BT])에 의해 $$H^{\ast}(\mathbb{P}(\mathcal{E}))$$는 이들을 자유 기저로 하는 $$H^{\ast}(X)$$-module이고, 따라서 $$\pi^{\ast}$$은 단사이다. 한편 $$\xi^r$$은 이 기저로 유일하게 전개되며, 그 전개에 나타나는 계수를 $$-\pi^{\ast}c_i(\mathcal{E})$$로 두는 것이 Grothendieck의 방식대로 Chern class의 정의와 일치한다. 따라서 위의 관계식을 얻는다.

</details>

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5 (Splitting principle)**</ins> rank $$r$$ vector bundle $$\mathcal{E} \to X$$에 대하여, 연속사상 $$f: Y \to X$$가 존재하여 다음 두 조건을 만족한다.

1. $$f^{\ast}: H^{\ast}(X, \mathbb{Z}) \to H^{\ast}(Y, \mathbb{Z})$$는 단사이다.
2. $$f^{\ast}\mathcal{E}$$는 line bundle들의 직합 $$\mathcal{L}_1 \oplus \cdots \oplus \mathcal{L}_r$$로 분해된다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$\pi: \mathbb{P}(\mathcal{E}) \to X$$를 택하면 [명제 4](#prop4)에 의해 $$\pi^{\ast}$$은 단사이다. $$\mathbb{P}(\mathcal{E})$$ 위에는 tautological line subbundle $$\mathcal{O}_\mathcal{E}(-1) \subset \pi^{\ast}\mathcal{E}$$가 있어 $$\pi^{\ast}\mathcal{E}$$가 이 직선다발과 rank $$r-1$$인 quotient $$\mathcal{Q}$$로의 짧은 완전열을 이루며, metric을 주면 직합 $$\pi^{\ast}\mathcal{E} \cong \mathcal{O}_\mathcal{E}(-1) \oplus \mathcal{Q}$$로 분리된다. 이제 $$\mathcal{Q}$$에 같은 과정을 반복하면 rank가 한 단계마다 하나씩 줄어들어, 유한 번 뒤 얻어지는 합성 $$f: Y \to X$$ 위에서 $$f^{\ast}\mathcal{E}$$가 직선다발들의 직합으로 분해된다. 각 단계의 pullback이 단사이므로 합성 $$f^{\ast}$$ 또한 단사이다.

</details>

Splitting principle의 핵심은 $$f^{\ast}$$이 단사라는 점이다. $$Y$$는 $$X$$보다 복잡한 공간이 아니라 $$X$$의 cohomology 정보를 잃지 않으면서 다발의 twist만 풀어 주는 공간이며, 따라서 $$Y$$ 위에서 성립하는 cohomology 등식은 그대로 $$X$$로 내려온다. 덕분에 임의의 다발에 대한 Chern class의 계산을 직선다발의 경우로 환원할 수 있다. 이제 공리의 정당성을 확인할 수 있다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> [정의 1](#def1)의 공리를 만족하는 Chern class는 유일하게 존재한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

**존재성.** [명제 4](#prop4)의 관계식 $$\xi^r + \pi^{\ast}c_1\xi^{r-1} + \cdots + \pi^{\ast}c_r = 0$$을 $$c_i(\mathcal{E})$$의 정의로 삼으면 (Grothendieck), 이렇게 얻은 $$c_i$$가 세 공리를 모두 만족함을 확인할 수 있다 ([BT]).

**유일성.** 공리를 만족하는 두 이론 $$c, c'$$가 있다 하자. 먼저 직선다발에서는 둘이 일치한다. 임의의 line bundle $$\mathcal{L}$$은 분류공간 $$\mathbb{P}^{\infty}$$로의 사상 $$g: X \to \mathbb{P}^{\infty}$$에 대해 $$\mathcal{L} = g^{\ast}\mathcal{O}(1)$$의 꼴이고, naturality와 normalization에 의해 $$c_1(\mathcal{L}) = g^{\ast}c_1(\mathcal{O}(1)) = c_1'(\mathcal{L})$$이기 때문이다. 일반 $$\mathcal{E}$$에 대해서는 splitting principle ([명제 5](#prop5))로 $$f^{\ast}\mathcal{E} = \bigoplus_i \mathcal{L}_i$$이고 $$f^{\ast}$$이 단사인 $$f: Y \to X$$를 택하면, Whitney 공식과 normalization으로

$$f^{\ast}c(\mathcal{E}) = \prod_i \bigl(1 + c_1(\mathcal{L}_i)\bigr) = f^{\ast}c'(\mathcal{E})$$

이고, $$f^{\ast}$$이 단사이므로 $$c(\mathcal{E}) = c'(\mathcal{E})$$이다.

</details>

## 천 근과 천 지표

Splitting principle 덕분에 우리는 임의의 다발을 마치 직선다발들의 직합인 것처럼 다룰 수 있다. 이를 형식화하자.

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> rank $$r$$ vector bundle $$\mathcal{E}$$를 splitting principle로 $$f^{\ast}\mathcal{E} = \mathcal{L}_1 \oplus \cdots \oplus \mathcal{L}_r$$로 분해하고 $$x_i = c_1(\mathcal{L}_i) \in H^2(Y)$$로 둔다. 이 $$x_1, \ldots, x_r$$을 $$\mathcal{E}$$의 *Chern root<sub>천 근</sub>*라 부른다. Whitney 공식에 의해 형식변수 $$\t$$에 대한 *Chern polynomial*은

$$c_\t(\mathcal{E}) = \prod_{i=1}^r (1 + x_i\t)$$

이며, 따라서 $$c_k(\mathcal{E})$$는 $$x_1, \ldots, x_r$$의 $$k$$차 elementary symmetric polynomial이다.

</div>

Chern root $$x_i$$ 자체는 $$Y$$ 위에서만 정의되지만, $$c_k(\mathcal{E})$$는 이들의 대칭함수이므로 $$x_i$$의 선택과 순서에 무관하게 $$H^{\ast}(X)$$로 내려온다. 즉 Chern class를 "근"으로 분해해 다항식처럼 다루되, 대칭함수만 취해 $$X$$로 되돌아오는 것이다. 한편 Chern polynomial의 한 가지 불편은 direct sum이 곱으로 나타난다는 점인데(Whitney), 곱을 합으로 바꾸는 $$\exp$$를 사용하면 이를 덧셈으로 정리할 수 있다.

<div class="definition" markdown="1">

<ins id="def8">**정의 8**</ins> Chern root $$x_1, \ldots, x_r$$를 갖는 vector bundle $$\mathcal{E}$$의 *Chern character<sub>천 지표</sub>*를

$$\chern(\mathcal{E}) = \sum_{i=1}^r e^{x_i} = r + c_1(\mathcal{E}) + \frac{c_1(\mathcal{E})^2 - 2c_2(\mathcal{E})}{2} + \cdots \in H^\bullet(X, \mathbb{Q})$$

로 정의한다. 각 차수의 항은 power sum $$\sum_i x_i^k$$를 elementary symmetric polynomial, 즉 Chern class로 다시 적은 것이다.

</div>

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> Chern character는 다음 성질을 만족한다.

1. $$\chern(\mathcal{E} \oplus \mathcal{F}) = \chern(\mathcal{E}) + \chern(\mathcal{F})$$,
2. $$\chern(\mathcal{E} \otimes \mathcal{F}) = \chern(\mathcal{E}) \smile \chern(\mathcal{F})$$.

즉 Chern character는 direct sum을 덧셈으로, tensor product를 cup product로 보낸다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

splitting principle로 $$\mathcal{E} = \bigoplus_i \mathcal{L}_i$$ (Chern root $$x_i$$), $$\mathcal{F} = \bigoplus_j \mathcal{M}_j$$ (Chern root $$y_j$$)로 가정한다. direct sum의 Chern root는 $$\{x_i\} \cup \{y_j\}$$이므로

$$\chern(\mathcal{E} \oplus \mathcal{F}) = \sum_i e^{x_i} + \sum_j e^{y_j} = \chern(\mathcal{E}) + \chern(\mathcal{F})$$

이다. 한편 $$\mathcal{E} \otimes \mathcal{F} = \bigoplus_{i,j} \mathcal{L}_i \otimes \mathcal{M}_j$$의 Chern root는 $$c_1(\mathcal{L}_i \otimes \mathcal{M}_j) = x_i + y_j$$ ([명제 3](#prop3))이므로

$$\chern(\mathcal{E} \otimes \mathcal{F}) = \sum_{i,j} e^{x_i + y_j} = \Bigl(\sum_i e^{x_i}\Bigr)\Bigl(\sum_j e^{y_j}\Bigr) = \chern(\mathcal{E}) \smile \chern(\mathcal{F})$$

이다. 두 등식 모두 $$f^{\ast}$$이 단사이므로 원래 공간 $$X$$에서 성립한다.

</details>

이 성질 덕분에 Chern character는 vector bundle들의 Grothendieck group에서 cohomology로 가는 ring homomorphism을 주며, 이것이 Riemann–Roch 류의 정리에서 Chern character가 자연스러운 언어가 되는 이유이다.

## 접다발의 천 특성류와 Euler 지표

Chern class의 대표적 응용은 다양체 자신의 접다발에 적용하여 위상 불변량을 얻는 것이다.

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10 (Poincaré–Hopf)**</ins> $$X$$가 $$n$$차원 compact complex manifold이면

$$\rchi_{\mathrm{top}}(X) = \int_X c_n(T_X)$$

이 성립한다. 여기서 $$\rchi_{\mathrm{top}}(X) = \sum_{i=0}^{2n} (-1)^i \dim_{\mathbb{Q}} H^i(X, \mathbb{Q})$$는 topological Euler characteristic이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

top Chern class $$c_n(T_X)$$는 복소 rank $$n$$ 다발 $$T_X$$를 실 rank $$2n$$의 oriented 다발로 보았을 때의 Euler class $$e(T_X)$$와 일치한다. Euler class의 적분은 generic section의 영점 수를 부호와 함께 센 것이고, $$T_X$$의 generic section은 generic vector field이므로 그 영점 수는 Poincaré–Hopf 정리에 의해 $$\rchi_{\mathrm{top}}(X)$$와 같다. 따라서 $$\int_X c_n(T_X) = \int_X e(T_X) = \rchi_{\mathrm{top}}(X)$$이다. 위상적 논증의 자세한 내용은 [BT]로 미룬다.

</details>

<div class="example" markdown="1">

<ins id="ex11">**예시 11**</ins> $$\mathbb{P}^n$$의 접다발은 Euler 완전열 ([§표준선다발, ⁋명제 7](/ko/math/algebraic_varieties/canonical_bundle#prop7))

$$0 \to \mathcal{O} \to \mathcal{O}(1)^{\oplus(n+1)} \to T_{\mathbb{P}^n} \to 0$$

을 만족한다. Whitney 공식과 $$c(\mathcal{O}) = 1$$로부터

$$c(T_{\mathbb{P}^n}) = c(\mathcal{O}(1))^{n+1} = (1+H)^{n+1}$$

이고, 여기서 $$H = c_1(\mathcal{O}(1))$$은 $$H^{\ast}(\mathbb{P}^n, \mathbb{Z}) = \mathbb{Z}[H]/(H^{n+1})$$의 생성원이다 ([§사영공간의 코호몰로지](/ko/math/algebraic_varieties/cohomology_of_projective_spaces)). 따라서 $$c_k(T_{\mathbb{P}^n}) = \binom{n+1}{k}H^k$$이며, 특히 $$c_n(T_{\mathbb{P}^n}) = (n+1)H^n$$이다. $$\int_{\mathbb{P}^n} H^n = 1$$이므로 [명제 10](#prop10)에 의해

$$\rchi_{\mathrm{top}}(\mathbb{P}^n) = \int_{\mathbb{P}^n} c_n(T_{\mathbb{P}^n}) = n+1$$

이고, 이는 $$\mathbb{P}^n$$의 cohomology가 $$0, 2, \ldots, 2n$$차에 $$\mathbb{Z}$$를 하나씩 가져 모두 $$n+1$$개임과 일치한다.

</div>

<div class="example" markdown="1">

<ins id="ex12">**예시 12**</ins> $$X \subset \mathbb{P}^3$$를 차수 $$d$$의 smooth surface라 하자. $$X$$의 normal bundle은 $$\mathcal{O}_X(d)$$이므로 ([§표준선다발](/ko/math/algebraic_varieties/canonical_bundle)) 짧은 완전열

$$0 \to T_X \to T_{\mathbb{P}^3}\vert_X \to \mathcal{O}_X(d) \to 0$$

에 Whitney 공식을 적용하면 $$H = c_1(\mathcal{O}_X(1))$$에 대하여

$$c(T_X) = \frac{c(T_{\mathbb{P}^3})\vert_X}{1 + dH} = \frac{(1+H)^4}{1 + dH}$$

이다. $$X$$가 surface라 $$H^3 = 0$$이므로 $$H^2$$까지 전개하면

$$c(T_X) = (1 + 4H + 6H^2)(1 - dH + d^2H^2) = 1 + (4-d)H + (d^2 - 4d + 6)H^2$$

이고, 따라서 $$c_2(T_X) = (d^2 - 4d + 6)H^2$$이다. $$\int_X H^2 = d$$이므로 [명제 10](#prop10)에 의해

$$\rchi_{\mathrm{top}}(X) = \int_X c_2(T_X) = d(d^2 - 4d + 6)$$

이다. $$d=1$$ (평면 $$\mathbb{P}^2$$)이면 $$3$$, $$d=2$$ (이차곡면 $$\mathbb{P}^1 \times \mathbb{P}^1$$)이면 $$4$$, $$d=3$$ (cubic surface)이면 $$9$$, $$d=4$$ (K3 surface)이면 $$24$$로, 모두 알려진 값과 일치한다.

</div>

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic geometry*, Springer, 1977.  
**[Ful]** W. Fulton, *Intersection theory*, Springer, 1998.  
**[BT]** R. Bott and L. Tu, *Differential forms in algebraic topology*, Springer, 1982.
