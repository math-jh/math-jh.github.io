---
title: "실수의 완비성"
description: "실수를 순서체로 보고, 해석학 전체를 떠받치는 완비성 공리(상한 성질)를 도입한다. 이로부터 아르키메데스 성질과 유리수의 조밀성을 유도하고, 완비성이 유리수와 실수를 가르는 본질적 차이임을 본다."
excerpt: "순서체와 상한 공리, 아르키메데스 성질, 유리수의 조밀성"

categories: [Math / Analysis]
permalink: /ko/math/analysis/completeness_of_reals
sidebar: 
    nav: "analysis-ko"

date: 2026-06-02
last_modified_at: 2026-06-02
weight: 1

published: false
---

[\[미적분학\] §함수와 극한](/ko/math/calculus/functions_and_limits)에서 우리는 극한을 다루며 실수의 "빈틈 없음"을 직관적으로 사용하였고, [\[미적분학\] §연속함수, ⁋정리 4](/ko/math/calculus/continuity#thm4)의 중간값 정리가 유리수 위에서는 성립하지 않음을 지적하였다. 해석학은 이 직관적 성질을 하나의 공리로 명확히 못박는 데서 출발한다. 그것이 *완비성*이며, 미적분학의 모든 존재 정리 — 극한, 최댓값, 적분의 존재 — 가 궁극적으로 여기에 기댄다.

## 순서체로서의 실수

실수 $$\mathbb{R}$$은 사칙연산과 대소관계를 갖춘 *순서체<sub>ordered field</sub>*이다. 즉 $$\mathbb{R}$$은 체이면서 전순서 $$\leq$$ ([\[집합론\] §순서관계의 정의](/ko/math/set_theory/order_relations))를 가지고, 그 순서가 연산과 다음과 같이 호환된다: $$a \leq b$$이면 $$a + c \leq b + c$$이고, $$a \leq b$$이고 $$0 \leq c$$이면 $$ac \leq bc$$이다. 유리수 $$\mathbb{Q}$$ 역시 순서체이므로, 이 성질만으로는 $$\mathbb{R}$$과 $$\mathbb{Q}$$가 구별되지 않는다. 둘을 가르는 것이 바로 다음에 도입할 완비성이다.

먼저 순서로부터 정해지는 상계와 상한의 개념을 정리한다 ([\[집합론\] §순서집합의 원소들](/ko/math/set_theory/elements_in_ordered_set)).

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> $$S \subseteq \mathbb{R}$$가 공집합이 아니라 하자. 실수 $$M$$이 $$S$$의 *상계<sub>upper bound</sub>*라는 것은 모든 $$s \in S$$에 대해 $$s \leq M$$인 것이고, 상계가 하나라도 존재하면 $$S$$를 *위로 유계<sub>bounded above</sub>*라 한다. $$S$$의 상계 중 가장 작은 것이 존재하면 그것을 $$S$$의 *상한<sub>supremum</sub>*이라 하고 $$\sup S$$로 적는다. 대칭적으로 *하계*, *아래로 유계*, *하한* $$\inf S$$를 정의한다.

</div>

상한 $$\alpha = \sup S$$는 두 조건으로 특징지어진다: (i) $$\alpha$$는 상계이다 (모든 $$s \in S$$에 대해 $$s \leq \alpha$$); (ii) $$\alpha$$는 가장 작은 상계이다 — 즉 임의의 $$\varepsilon > 0$$에 대해 $$\alpha - \varepsilon$$은 더 이상 상계가 아니므로 $$s > \alpha - \varepsilon$$인 $$s \in S$$가 존재한다. 조건 (ii)의 이 형태는 앞으로 거듭 쓰인다.

## 완비성 공리

<div class="definition" markdown="1">

<ins id="def2">**정의 2 (완비성 공리)**</ins> 순서체 $$\mathbb{R}$$은 *완비<sub>complete</sub>*하다. 즉 위로 유계인 공집합이 아닌 모든 부분집합 $$S \subseteq \mathbb{R}$$은 상한 $$\sup S \in \mathbb{R}$$를 갖는다. 이를 *상한 성질<sub>least upper bound property</sub>*이라 부른다.

</div>

이것이 실수를 정의하는 마지막 공리이며, $$\mathbb{Q}$$에서는 성립하지 않는다. 예를 들어 $$S = \{x \in \mathbb{Q} \mid x^2 < 2\}$$는 $$\mathbb{Q}$$ 안에서 위로 유계이지만, 그 상한은 $$\sqrt{2}$$여야 하는데 이것이 유리수가 아니므로 $$\mathbb{Q}$$ 안에는 상한이 없다. 완비성은 바로 이런 "빈틈"이 $$\mathbb{R}$$에는 없음을 단언한다.

하한에 대한 대응 명제는 공리로 따로 둘 필요가 없다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> 아래로 유계인 공집합이 아닌 모든 $$S \subseteq \mathbb{R}$$은 하한 $$\inf S$$를 갖는다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$-S = \{-s \mid s \in S\}$$를 생각하자. $$S$$가 하계 $$m$$을 가지면 $$-m$$은 $$-S$$의 상계이므로 $$-S$$는 위로 유계이고, 완비성 공리에 의해 $$\alpha = \sup(-S)$$가 존재한다. 그러면 $$-\alpha = \inf S$$임이 정의로부터 직접 확인된다.

</details>

## 아르키메데스 성질과 조밀성

완비성의 첫 수확은 "자연수가 한없이 커진다"는 당연해 보이는 사실인데, 놀랍게도 이는 완비성 없이는 보장되지 않는다.

<div class="proposition" markdown="1">

<ins id="thm4">**정리 4 (아르키메데스 성질)**</ins> 임의의 실수 $$x$$에 대하여, $$n > x$$인 자연수 $$n$$이 존재한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

자연수 집합 $$\mathbb{N}$$이 위로 유계라 가정하고 모순을 이끌자. 그러면 완비성에 의해 $$\alpha = \sup \mathbb{N}$$가 존재한다. $$\alpha$$가 가장 작은 상계이므로 $$\alpha - 1$$은 상계가 아니고, 따라서 $$n > \alpha - 1$$인 자연수 $$n$$이 있다. 그러면 $$n + 1 > \alpha$$인데 $$n + 1$$도 자연수이므로 $$\alpha$$가 상계라는 데 모순이다. 따라서 $$\mathbb{N}$$은 위로 유계가 아니고, 임의의 $$x$$에 대해 $$n > x$$인 $$n$$이 존재한다.

</details>

아르키메데스 성질의 동치 형태로, 임의의 $$\varepsilon > 0$$에 대해 $$\frac{1}{n} < \varepsilon$$인 자연수 $$n$$이 존재한다 ($$n > 1/\varepsilon$$을 잡으면 된다). 이로부터 유리수가 실수 안에 촘촘히 들어차 있음을 얻는다.

<div class="proposition" markdown="1">

<ins id="thm5">**정리 5 (유리수의 조밀성)**</ins> 임의의 두 실수 $$a < b$$ 사이에는 유리수 $$q$$가 존재한다. 즉 $$a < q < b$$인 $$q \in \mathbb{Q}$$가 있다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$b - a > 0$$이므로 아르키메데스 성질에 의해 $$\frac{1}{n} < b - a$$, 즉 $$nb - na > 1$$인 자연수 $$n$$이 있다. 두 실수의 차가 $$1$$보다 크므로 그 사이에 정수가 존재한다 — 구체적으로 $$m = \lfloor na\rfloor + 1$$로 두면 $$na < m \leq na + 1 < nb$$이다. 양변을 $$n$$으로 나누면 $$a < \frac{m}{n} < b$$이고, $$q = m/n$$이 원하는 유리수이다.

</details>

조밀성은 한 번 더 쓰면 두 실수 사이에 유리수가 *무한히* 많이 있음을 준다. 실제로 $$a < q_1 < b$$인 유리수 $$q_1$$을 잡고, 다시 정리 5를 구간 $$(q_1, b)$$에 적용하면 $$q_1 < q_2 < b$$인 $$q_2$$를 얻으며, 이를 되풀이하면 서로 다른 유리수 $$q_1 < q_2 < q_3 < \cdots$$가 모두 $$(a, b)$$ 안에 놓인다. 같은 방식으로 무리수도 조밀하다: $$a < b$$이면 $$a - \sqrt{2} < b - \sqrt{2}$$이므로 그 사이에 유리수 $$q$$가 있고, 그러면 $$q + \sqrt{2}$$는 $$(a, b)$$에 속하는 무리수이다 (유리수에 무리수를 더하면 무리수이므로). 따라서 유리수와 무리수는 실직선 위에 서로 뒤섞여 촘촘히 깔려 있다.

## 상한의 계산과 활용

상한 성질은 추상적인 존재 단언으로 그치지 않고, 구체적인 집합의 상한을 정의 (i), (ii) 의 두 조건으로 직접 확인하는 데 쓰인다. 어떤 후보 값 $$\alpha$$가 $$\sup S$$임을 보이려면, $$\alpha$$가 상계임을 보이고 ($$s \leq \alpha$$ for all $$s \in S$$), 임의의 $$\varepsilon > 0$$에 대해 $$s > \alpha - \varepsilon$$인 $$s \in S$$를 찾으면 된다. 몇 가지 표준적인 예를 통해 이 절차를 익히자.

<div class="example" markdown="1">

<ins id="ex6">**예시 6 (반열린 구간의 상한)**</ins> $$S = [0, 1) = \{x \in \mathbb{R} \mid 0 \leq x < 1\}$$이라 하자. 우리는 $$\sup S = 1$$임을 주장한다. 먼저 $$1$$은 상계이다: 모든 $$s \in S$$에 대해

$$s < 1 \leq 1$$

이다. 다음으로 $$1$$이 가장 작은 상계임을 본다. 임의의 $$\varepsilon > 0$$이 주어지면, $$\varepsilon \geq 1$$일 때는 $$0 \in S$$가 이미 $$1 - \varepsilon \leq 0$$를 넘고, $$0 < \varepsilon < 1$$일 때는

$$s = 1 - \tfrac{\varepsilon}{2} \in [0, 1) = S, \qquad s = 1 - \tfrac{\varepsilon}{2} > 1 - \varepsilon$$

이므로 $$1 - \varepsilon$$은 상계가 될 수 없다. 따라서 $$1$$보다 작은 어떤 수도 상계가 아니고 $$\sup S = 1$$이다. 특히 $$1 \notin S$$이므로 상한이 집합에 속하지 않을 수 있음을 본다.

</div>

상한이 집합의 원소일 때 그것을 *최댓값<sub>maximum</sub>*이라 부른다. 예시 6에서 보듯 $$\sup S$$가 항상 $$S$$의 원소인 것은 아니며, $$\sup S \in S$$인 경우에만 $$\max S$$가 존재한다. 위 집합을 닫힌 구간 $$[0,1]$$로 바꾸면 $$\sup [0,1] = 1 \in [0,1]$$이 되어 최댓값이 존재한다. 다음 예시는 상한이 집합의 원소가 아닌 또 다른 전형이다.

<div class="example" markdown="1">

<ins id="ex7">**예시 7 (수열로 주어진 집합)**</ins> $$S = \left\{ 1 - \tfrac{1}{n} \mathrel{\Big\vert} n \in \mathbb{N} \right\} = \left\{ 0, \tfrac12, \tfrac23, \tfrac34, \dots \right\}$$의 상한을 구하자. 모든 $$n$$에 대해 $$1 - \tfrac1n < 1$$이므로 $$1$$은 상계이다. 한편 임의의 $$\varepsilon > 0$$에 대해, 아르키메데스 성질 (정리 4) 로 $$\tfrac1n < \varepsilon$$인 $$n$$을 잡으면

$$1 - \frac{1}{n} > 1 - \varepsilon$$

이므로 $$1 - \varepsilon$$은 상계가 아니다. 따라서

$$\sup S = 1, \qquad 1 \notin S$$

이다. 즉 $$S$$는 자신의 상한에 한없이 다가가지만 결코 도달하지 않으며, $$\max S$$는 존재하지 않는다. 한편 $$\inf S = 0 = 1 - \tfrac11 \in S$$이므로 하한은 집합에 속해 $$\min S = 0$$이다.

</div>

상한 연산은 집합의 평행이동·스칼라배와 잘 호환된다. 이 단순한 규칙들은 이후 극한 계산에서 거듭 쓰이므로 명제로 정리해 둔다.

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8 (상한의 평행이동과 양의 스칼라배)**</ins> 위로 유계인 공집합이 아닌 $$S \subseteq \mathbb{R}$$와 실수 $$c$$, $$\lambda > 0$$에 대하여, $$c + S = \{c + s \mid s \in S\}$$와 $$\lambda S = \{\lambda s \mid s \in S\}$$ 역시 위로 유계이고

$$\sup(c + S) = c + \sup S, \qquad \sup(\lambda S) = \lambda \sup S$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$\alpha = \sup S$$로 두자. 평행이동의 경우, 모든 $$s \in S$$에 대해 $$s \leq \alpha$$이므로 $$c + s \leq c + \alpha$$이고, 따라서 $$c + \alpha$$는 $$c + S$$의 상계이다. 또 임의의 $$\varepsilon > 0$$에 대해 $$s > \alpha - \varepsilon$$인 $$s \in S$$가 있으므로

$$\begin{aligned}
c + s &> c + \alpha - \varepsilon
\end{aligned}$$

이고 $$c + s \in c + S$$이다. 따라서 $$c + \alpha - \varepsilon$$은 상계가 아니어서 $$c + \alpha$$가 가장 작은 상계, 곧 $$\sup(c + S) = c + \alpha$$이다.

스칼라배의 경우도 같다. $$\lambda > 0$$이므로 $$s \leq \alpha$$에서 $$\lambda s \leq \lambda \alpha$$를 얻어 $$\lambda \alpha$$가 $$\lambda S$$의 상계이고, 임의의 $$\varepsilon > 0$$에 대해 $$s > \alpha - \tfrac{\varepsilon}{\lambda}$$인 $$s$$를 잡으면

$$\begin{aligned}
\lambda s &> \lambda\left(\alpha - \frac{\varepsilon}{\lambda}\right) = \lambda\alpha - \varepsilon
\end{aligned}$$

이므로 $$\lambda\alpha - \varepsilon$$ 또한 상계가 아니다. 따라서 $$\sup(\lambda S) = \lambda\alpha$$이다.

</details>

위 명제에서 $$\lambda > 0$$이라는 가정은 본질적이다. $$\lambda = -1$$이면 부등호의 방향이 뒤집혀 상계가 하계로 바뀌고, 실제로 명제 3의 증명에서 본 대로 $$\sup(-S) = -\inf S$$가 된다. 일반적으로 음수배는 상한과 하한을 맞바꾼다.

## 중첩구간정리

완비성의 가장 기하학적인 표현 가운데 하나는 "끝없이 줄어드는 닫힌 구간들의 사슬은 빈 곳을 남기지 않는다"는 것이다. 이는 다음 글에서 다룰 수열의 수렴과 직결되며, 십진법 전개로 실수를 구성하는 직관의 바탕이 된다.

<div class="proposition" markdown="1">

<ins id="thm9">**정리 9 (중첩구간정리)**</ins> 닫힌 구간들의 중첩하는 사슬 $$I_1 \supseteq I_2 \supseteq I_3 \supseteq \cdots$$, $$I_n = [a_n, b_n]$$ ($$a_n \leq b_n$$) 에 대하여 교집합 $$\bigcap_{n=1}^\infty I_n$$은 공집합이 아니다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

중첩 조건 $$I_{n+1} \subseteq I_n$$은 좌끝점이 비감소, 우끝점이 비증가임을 뜻한다:

$$\begin{aligned}
a_1 \leq a_2 \leq a_3 \leq \cdots, \qquad \cdots \leq b_3 \leq b_2 \leq b_1.
\end{aligned}$$

게다가 임의의 $$m, n$$에 대해 $$a_m \leq b_n$$이다. 실제로 $$k = \max(m, n)$$으로 두면 $$a_m \leq a_k \leq b_k \leq b_n$$이기 때문이다. 따라서 집합 $$A = \{a_n \mid n \in \mathbb{N}\}$$은 위로 유계이고 (예컨대 $$b_1$$이 상계), 완비성에 의해

$$\alpha = \sup A$$

가 존재한다. $$\alpha$$가 $$A$$의 상계이므로 모든 $$n$$에 대해 $$a_n \leq \alpha$$이고, 한편 모든 $$b_n$$이 $$A$$의 상계이므로 가장 작은 상계인 $$\alpha$$는 $$\alpha \leq b_n$$을 만족한다. 두 부등식을 합치면

$$a_n \leq \alpha \leq b_n \quad (\forall n), \qquad \text{즉} \quad \alpha \in \bigcap_{n=1}^\infty I_n$$

이므로 교집합은 비어 있지 않다.

</details>

닫힌 구간이라는 조건은 없앨 수 없다. 반열린 구간 $$I_n = \left(0, \tfrac1n\right]$$을 보면 모두 중첩하지만 임의의 $$x > 0$$은 아르키메데스 성질로 $$\tfrac1n < x$$가 되는 순간 빠져나가므로 $$\bigcap_n I_n = \varnothing$$이다. 구간의 길이 $$b_n - a_n$$이 $$0$$으로 줄어드는 경우에는 교집합이 정확히 한 점이 되며, 이 한 점이 모든 $$a_n$$의 상한이자 모든 $$b_n$$의 하한이다.

<div class="example" markdown="1">

<ins id="ex10">**예시 10 (길이가 줄어드는 구간과 십진 전개)**</ins> 실수 $$x$$의 십진 전개는 중첩구간정리의 전형적 사례이다. $$x = 0.\,d_1 d_2 d_3 \cdots$$ ($$d_k \in \{0, 1, \dots, 9\}$$) 에 대해

$$I_n = \left[\, 0.d_1\cdots d_n,\ \ 0.d_1\cdots d_n + 10^{-n} \,\right]$$

로 두면 $$I_1 \supseteq I_2 \supseteq \cdots$$이고 길이는 $$10^{-n} \to 0$$이다. 정리 9에 의해 교집합은 비어 있지 않고, 길이가 $$0$$으로 가므로 교집합은 한 점뿐이다. 그 점이 바로 무한소수가 나타내는 실수 $$x$$이다. 완비성이 없다면 이 교집합이 빌 수도 있어, 무한소수가 수렴할 대상이 보장되지 않는다.

</div>

## 제곱근의 존재

완비성이 "빈틈"을 메운다는 말을 가장 또렷이 보여 주는 것은, $$\mathbb{Q}$$에는 없던 $$\sqrt{2}$$ 같은 수가 $$\mathbb{R}$$ 안에 실제로 존재함을 증명하는 일이다. 이는 도입부에서 예고한 집합 $$\{x \mid x^2 < 2\}$$의 상한이 정말로 제곱하면 $$2$$가 됨을 확인하는 작업이다.

<div class="proposition" markdown="1">

<ins id="thm11">**정리 11 (양의 제곱근의 존재)**</ins> 임의의 실수 $$c > 0$$에 대하여 $$\alpha^2 = c$$인 유일한 양의 실수 $$\alpha$$가 존재한다. 이를 $$\sqrt{c}$$로 적는다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$S = \{x > 0 \mid x^2 < c\}$$로 두자. $$S$$는 공집합이 아니고 (작은 $$x$$에 대해 $$x^2 < c$$), $$1 + c$$가 상계이므로 (만약 $$x > 1 + c$$이면 $$x^2 > x > c$$) 위로 유계이다. 완비성에 의해 $$\alpha = \sup S > 0$$이 존재한다. 우리는 $$\alpha^2 = c$$임을 두 부등식을 배제하여 보인다.

먼저 $$\alpha^2 < c$$라 가정하자. 작은 $$h \in (0, 1)$$에 대해

$$\begin{aligned}
(\alpha + h)^2 &= \alpha^2 + 2\alpha h + h^2 \\
&\leq \alpha^2 + 2\alpha h + h = \alpha^2 + (2\alpha + 1)h
\end{aligned}$$

이고, $$c - \alpha^2 > 0$$이므로 $$h < \dfrac{c - \alpha^2}{2\alpha + 1}$$이면서 $$h < 1$$인 $$h$$를 잡으면 $$(\alpha + h)^2 < c$$가 되어 $$\alpha + h \in S$$이다. 이는 $$\alpha$$가 상계라는 데 모순이다.

다음으로 $$\alpha^2 > c$$라 가정하자. $$k = \dfrac{\alpha^2 - c}{2\alpha} > 0$$로 두면 $$0 < k < \alpha$$이고

$$\begin{aligned}
(\alpha - k)^2 &= \alpha^2 - 2\alpha k + k^2 \\
&> \alpha^2 - 2\alpha k = \alpha^2 - (\alpha^2 - c) = c
\end{aligned}$$

이다. 그러면 임의의 $$x \geq \alpha - k$$인 양수는 $$x^2 \geq (\alpha - k)^2 > c$$이어서 $$S$$에 속하지 않으므로, $$\alpha - k$$가 $$S$$의 상계가 된다. 이는 $$\alpha$$가 가장 작은 상계라는 데 모순이다.

두 부등식이 모두 모순이므로 $$\alpha^2 = c$$이다. 유일성은 $$0 < \alpha < \beta$$이면 $$\alpha^2 < \beta^2$$이라는 단조성에서 즉시 따른다.

</details>

특히 $$c = 2$$를 넣으면 $$\alpha^2 = 2$$인 양의 실수가 존재하며, 이것이 곧 $$\sqrt{2}$$이다. 도입부에서 본 대로 이 수는 유리수가 아니므로, 정리 11은 완비성이 $$\mathbb{Q}$$의 빈틈을 정확히 메운다는 사실의 결정적 증거이다. 같은 논증을 $$n$$제곱근으로 일반화하면 모든 양수가 임의의 자연수 차수의 양의 실근을 가짐을 얻는다.

<div class="example" markdown="1">

<ins id="ex12">**예시 12 ($$\sqrt{2}$$의 무리성과 완비성의 역할)**</ins> 정리 11이 보장하는 $$\sqrt{2}$$가 유리수가 아님을 확인하자. 만약 $$\sqrt{2} = \tfrac{p}{q}$$ ($$p, q$$는 서로소인 자연수) 라면

$$2 = \frac{p^2}{q^2} \implies p^2 = 2q^2$$

이므로 $$p^2$$이 짝수, 따라서 $$p$$가 짝수이다. $$p = 2r$$로 쓰면 $$4r^2 = 2q^2$$, 곧 $$q^2 = 2r^2$$이 되어 $$q$$도 짝수이다. 이는 $$p, q$$가 서로소라는 데 모순이다. 따라서 $$\sqrt{2} \notin \mathbb{Q}$$이다. 핵심은 이 무리수가 *존재한다*는 사실 자체가 완비성에서 나온다는 점이다 — $$\mathbb{Q}$$ 안에서는 $$\{x \mid x^2 < 2\}$$가 상한을 갖지 않아 제곱근이 아예 없지만, $$\mathbb{R}$$의 상한 성질이 그 빈자리를 채운다.

</div>

이처럼 완비성 하나로부터 실수의 핵심 성질들이 줄줄이 따라 나온다. 다음 글 [§수열의 수렴](/ko/math/analysis/convergence_of_sequences)에서는 완비성을 수열의 언어로 옮겨 단조수렴정리를 얻고, 이어 [§Cauchy 수열과 완비성](/ko/math/analysis/cauchy_sequences)에서 완비성의 또 다른 동치 형태를 본다. 이 완비성이 있어야 비로소 [\[미적분학\] §연속함수](/ko/math/calculus/continuity)에서 도구로 받아들였던 최대·최소 정리와 중간값 정리를 [§연속함수의 성질](/ko/math/analysis/continuous_functions), [§연결성과 중간값 정리](/ko/math/analysis/connectedness)에서 증명할 수 있다.
