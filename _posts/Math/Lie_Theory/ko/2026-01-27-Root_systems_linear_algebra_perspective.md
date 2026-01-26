---

title: "근계: 선형대수에서 리 이론으로"
excerpt: ""

categories: [Math / Lie Theory]
permalink: /ko/math/Lie_theory/root_systems_linear_algebra
header:
    overlay_image: /assets/images/Math/Lie_Theory/Root_systems.png
    overlay_filter: 0.5
sidebar: 
    nav: "Lie_theory-ko"

date: 2026-01-27
last_modified_at: 2026-01-27
weight: 3

---

## 고유공간 분해에서의 출발

선형대수에서 우리가 학습한 고유공간 분해(eigenspace decomposition)의 핵심은 다음과 같다. 행렬 $A\in \mathfrak{gl}(V)$에 대하여 $V$를 eigenspace들의 직합으로 표현할 수 있다:

$$V = \bigoplus_{\lambda \in \sigma(A)} E_\lambda(A), \quad E_\lambda(A) = \ker(A - \lambda I)$$

이러한 분해는 $A$의 구조를 완전히 파악하기 위한 기본적인 도구이다. 특히 diagonalizable operator의 경우, 이 분해만으로 operator의 모든 정보를 담을 수 있다.

한편 우리는 [§조르당 표준형](/ko/math/linear_algebra/Jordan_canonical_form)에서 diagonalizable하지 않은 operator의 경우도 다루었다. 이 경우 eigenspace $E_\lambda = \ker(A-\lambda I)$는 너무 작을 수 있으므로, generalized eigenspace $G_\lambda = \ker(A-\lambda I)^k$ (충분히 큰 $k$에 대해)로 확장하여 전체 공간을 분해했다. 

이제 우리는 이러한 아이디어를 **Lie algebra의 세계로 옮기고자 한다**.

## Cartan subalgebra와 동시 대각화

Semisimple Lie algebra $\mathfrak{g}$를 고정하자. Adjoint representation $\ad: \mathfrak{g} \to \mathfrak{gl}(\mathfrak{g})$는 다음과 같이 정의된다:

$$\ad_X(Y) = [X, Y]$$

선형대수에서 여러 행렬을 동시에 대각화하는 아이디어를 생각해보자. 만약 행렬들이 서로 commute한다면, 공통의 eigenbasis를 가질 수 있다. Lie algebra에서도 유사한 상황이 일어난다.

**Cartan subalgebra** $\mathfrak{h}$는 maximal abelian subalgebra이다. 즉, $\mathfrak{h}$의 모든 원소들은 서로 commute한다:

$$[H_1, H_2] = 0 \quad \text{for all } H_1, H_2 \in \mathfrak{h}$$

이 성질의 중요한 결과는 $\mathfrak{h}$의 모든 원소들이 $\mathfrak{g}$ 위에서 동시에 대각화 가능하다는 것이다 (적절한 field extension 이후). 따라서 우리는 $\mathfrak{g}$를 다음과 같이 분해할 수 있다:

$$\mathfrak{g} = \bigoplus_{\lambda \in \mathfrak{h}^*} \mathfrak{g}_\lambda$$

여기서 

$$\mathfrak{g}_\lambda = \{X \in \mathfrak{g} \mid [H, X] = \lambda(H)X \text{ for all } H \in \mathfrak{h}\}$$

이고, $\lambda: \mathfrak{h} \to \mathbb{C}$는 linear functional이다.

## Root space decomposition

위의 분해에서 $\lambda = 0$인 경우를 특별히 살펴보자:

$$\mathfrak{g}_0 = \{X \in \mathfrak{g} \mid [H, X] = 0 \text{ for all } H \in \mathfrak{h}\}$$

이는 정확히 $\mathfrak{h}$의 centralizer이며, $\mathfrak{h}$가 maximal abelian이라는 조건에 의해 $\mathfrak{g}_0 = \mathfrak{h}$가 성립한다.

따라서 우리는 다음의 분해를 얻는다:

$$\mathfrak{g} = \mathfrak{h} \oplus \bigoplus_{\lambda \neq 0} \mathfrak{g}_\lambda$$

이제 **nonzero linear functionals** $\lambda$에 주목하되, $\mathfrak{g}_\lambda \neq 0$인 것들만 고려한다. 이러한 $\lambda$들을 **root**라고 부른다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Semisimple Lie algebra $\mathfrak{g}$와 Cartan subalgebra $\mathfrak{h}$에 대하여, **root**들의 집합은

$$\Phi = \{\alpha \in \mathfrak{h}^* \setminus \{0\} \mid \mathfrak{g}_\alpha \neq 0\}$$

이다. 각 $\alpha \in \Phi$에 대해 $\mathfrak{g}_\alpha$를 **root space**라 부른다. Root space의 원소들을 **root vector**라 부른다.

</div>

이제 우리가 할 관찰은 다음과 같다. 이는 선형대수의 고유공간 분해와 정확히 같은 구조이다. 선형대수에서는:

- 고유벡터: $Av = \lambda v$ (단일 operator $A$)
- 고유공간: $E_\lambda = \{v \mid Av = \lambda v\}$

Lie theory에서는:

- 근 벡터: $[H, X] = \alpha(H)X$ (모든 $H \in \mathfrak{h}$)
- 근 공간: $\mathfrak{g}_\alpha = \{X \mid [H, X] = \alpha(H)X \text{ for all } H \in \mathfrak{h}\}$

차이는 단일한 operator가 아니라 전체 Cartan subalgebra가 동시에 대각화되고 있다는 점뿐이다. 이는 동시 대각화(simultaneous diagonalization)의 자연스러운 확장이다.

## Killing form과 기하학적 구조

선형대수에서 고유벡터들 사이의 관계를 이해하기 위해 종종 내적을 사용한다. Lie algebra에서도 유사하게, Killing form을 통해 roots 사이의 기하학적 관계를 파악할 수 있다.

Semisimple Lie algebra는 Killing form을 가진다:

$$B(X, Y) = \text{tr}(\ad_X \circ \ad_Y)$$

이 form은 non-degenerate이며, $\mathfrak{h}$에 제한했을 때도 non-degenerate이다. 따라서 canonical isomorphism

$$\mathfrak{h} \to \mathfrak{h}^*: H \mapsto B(H, \cdot)$$

이 존재한다. 이를 통해 $\mathfrak{h}^*$를 Euclidean space로 볼 수 있으며, roots 위에도 자연스럽게 inner product가 정의된다. Specifically, $\alpha, \beta \in \mathfrak{h}^*$에 대하여, 이에 대응되는 $H_\alpha, H_\beta \in \mathfrak{h}$가 있을 때,

$$(\alpha, \beta) := B(H_\alpha, H_\beta)$$

로 정의한다.

이제 roots 모임 $\Phi$가 특별한 기하학적 구조를 가지는지 살펴보자.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> 유한차원 inner product space $(E, (\cdot, \cdot))$의 nonzero vectors의 유한집합 $\Phi$가 **root system**이라는 것은 다음의 조건들을 만족하는 것이다:

1. $\Phi$의 원소들이 $E$를 span한다.
2. $\alpha \in \Phi$이고 $c \in \mathbb{R}$일 때, $c\alpha \in \Phi$이기 위해서는 $c = \pm 1$이어야 한다.
3. 각 $\alpha \in \Phi$에 대하여, reflection
   $$s_\alpha(\beta) := \beta - 2\frac{(\beta, \alpha)}{(\alpha, \alpha)}\alpha$$
   는 $\Phi$를 보존한다.
4. 모든 $\alpha, \beta \in \Phi$에 대하여,
   $$\langle \beta, \alpha \rangle := 2\frac{(\beta, \alpha)}{(\alpha, \alpha)} \in \mathbb{Z}$$
   이 성립한다.

</div>

Root system의 조건들은 roots의 기하학적 구조가 극도로 제한적임을 보여준다. 예를 들어, 조건 4의 정수성과 조건 2의 정규화 조건으로부터, 두 roots가 이룰 수 있는 각도는 극히 제한된다. 구체적으로,

$$\langle \beta, \alpha \rangle \langle \alpha, \beta \rangle = 4\cos^2\theta$$

이고 이는 정수이므로, $\cos\theta \in \{0, \pm\frac{1}{2}, \pm\frac{\sqrt{2}}{2}, \pm\frac{\sqrt{3}}{2}, \pm 1\}$이어야 한다. 조건 2에 의해 $\cos\theta = \pm 1$은 배제되므로, roots는 $30°, 45°, 60°, 90°, 120°, 135°, 150°$의 각도만 이룰 수 있다.

<div class="proposition" markdown="1">

<ins id="prop1">**명제 1**</ins> Semisimple Lie algebra $\mathfrak{g}$의 Cartan subalgebra $\mathfrak{h}$에 대하여, Killing form으로부터 정의된 roots의 집합 $\Phi \subset \mathfrak{h}^*$는 $\mathfrak{h}^*$의 root system이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

조건 1은 root space decomposition의 구조로부터 직접 따른다. 조건 2도 root의 정의에서 명백하다.

조건 3의 경우, $s_\alpha$가 $\Phi$를 보존함은 다음과 같이 보인다. $E_\alpha \in \mathfrak{g}_\alpha$, $E_\beta \in \mathfrak{g}_\beta$라 하고, $\text{ad}_{E_\alpha}$를 생각하자. $\mathfrak{h}$의 모든 원소와 commute하고 root space들을 연결하는 성질들이 있으며, 이를 통해 $s_\alpha(\beta) \in \Phi$ (혹은 $s_\alpha(\beta) = 0$)임을 보일 수 있다. (자세한 증명은 adjoint representation의 성질에 관한 deeper analysis를 요구하므로 여기서는 생략한다.)

조건 4의 정수성은 root space와 Killing form의 정의로부터 자명하다.

</details>

## Simple roots와 Cartan matrix

선형대수에서 전체 eigenspace를 알기 위해 각 eigenvalue에 대한 하나의 고유벡터만 필요하듯이, Lie theory에서도 모든 roots를 알 필요는 없다. 다음의 개념이 중요하다.

먼저 positive root system $\Phi^+ \subset \Phi$를 선택한다. 이는 각 root $\alpha$에 대해 $\alpha \in \Phi^+$ 또는 $-\alpha \in \Phi^+$ 중 정확히 하나가 성립하도록 하고, $\alpha, \beta \in \Phi^+$이면 $\alpha + \beta \in \Phi^+$ (만약 $\alpha + \beta \in \Phi$이면) 조건을 만족한다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> Positive root system $\Phi^+ \subset \Phi$에서, $\alpha \in \Phi^+$가 **simple root**라는 것은 $\alpha$를 $\Phi^+$의 다른 원소들의 합으로 표현할 수 없는 것이다. Simple roots의 모임을 $\Delta$라 표기한다.

</div>

중요한 사실은 $\Phi$의 모든 원소가 simple roots의 음이 아닌 정수 일차결합으로 표현된다는 것이다. 따라서 root system 전체는 simple roots 사이의 inner products만으로 결정된다.

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> Simple roots $\Delta = \{\alpha_1, \ldots, \alpha_l\}$에 대하여, **Cartan matrix**는

$$A = (a_{ij})_{1 \le i,j \le l}, \quad a_{ij} = \langle \alpha_i, \alpha_j \rangle = 2\frac{(\alpha_i, \alpha_j)}{(\alpha_j, \alpha_j)}$$

로 정의된다.

</div>

Cartan matrix는 다음의 성질을 가진다:
- 대각 성분: $a_{ii} = 2$
- 비대각 성분: $a_{ij} \in \{-3, -2, -1, 0\}$ (root 사이의 각도 제약으로부터)
- 행렬이 indecomposable이면 root system도 indecomposable이다.

이 행렬 하나가 **전체 root system의 구조를 완전히 결정한다**. Roots 사이의 모든 관계가 이 유한한 데이터에 담겨있다.

## Weyl group: 근계의 대칭

Root system의 정의 조건 3에서, 각 root에 대한 reflection들이 $\Phi$를 보존한다고 했다. 이러한 reflections들로 생성되는 group을 정의하자.

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> Root system $\Phi$의 **Weyl group**은

$$W(\Phi) := \langle s_\alpha \mid \alpha \in \Phi \rangle$$

이다. 즉, roots에 대한 모든 reflections로 생성되는 orthogonal group의 부분군이다.

</div>

중요한 관찰은 다음과 같다:

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> 임의의 root system $\Phi$에 대하여, Weyl group $W(\Phi)$는 유한군이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

각 reflection $s_\alpha$는 유한집합 $\Phi$ 위에 작용한다. Weyl group이 faithful하게 $\Phi$ 위에 작용하므로 (조건 1에 의해), Weyl group은 대칭군 $S_\Phi$의 부분군이다. 따라서 유한하다.

</details>

Simple reflections $s_{\alpha_i}$ (simple roots에 대한 reflection)는 Weyl group을 생성한다. 따라서 Cartan matrix와 simple roots의 관계만으로 전체 Weyl group의 구조를 파악할 수 있다.

## 선형대수와의 종합

이제 우리가 한 전체 구성을 정리하자.

**선형대수**: 행렬 $A$의 고유공간 분해
- Eigenvalue들: 스칼라
- Eigenspace들: 각 eigenvalue에 대한 부분공간
- 고유벡터들의 성질: 일반적으로 제약이 없음

**Lie theory**: Semisimple Lie algebra의 root space decomposition
- Roots: Cartan subalgebra 위의 linear functionals
- Root spaces: 각 root에 대한 부분공간
- Roots의 기하학적 관계: Root system의 엄격한 조건들로 제약됨

후자는 전자의 자연스러운 확장이다. 단일 operator의 고유공간 분해에서 출발하여, commuting family of operators (Cartan subalgebra)의 동시 고유공간 분해로 나아갔고, 그 결과 얻어지는 구조 (root system)는 예상보다 훨씬 풍부한 기하학적 성질을 가진다.

Root system은 단순한 대수적 대상이 아니라, 기하학적으로도 매우 특별한 구조이며, 이는 Lie algebra의 깊은 구조를 반영한다. Weyl group은 이러한 기하학적 구조의 모든 대칭을 담당하며, 결과적으로 Lie algebra를 완전히 결정한다.

---

**참고**
- Humphreys, J. E. *Introduction to Lie Algebras and Representation Theory*. Springer, 1972.
- Serre, J.-P. *Complex Semisimple Lie Algebras*. Springer, 1987.

