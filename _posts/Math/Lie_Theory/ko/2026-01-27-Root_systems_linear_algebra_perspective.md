---

title: "근계: G-모듈과 선형대수"
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

## G-모듈로서의 표현

[§표현](/ko/math/Lie_theory/Representations)에서 우리는 Lie group $G$의 표현을 다음과 같이 정의했다: $G$의 표현은 벡터공간 $V$와 함께 행동 

$$G \times V \to V, \quad (g, v) \mapsto \rho(g)(v)$$

를 정의하는 것이다. 

이를 다른 관점에서 보면, 우리는 벡터공간 $V$를 $G$-모듈로 생각할 수 있다. 즉, $G$의 각 원소가 $V$ 위의 선형변환으로 작용하는 구조를 가진 벡터공간이다. 더 나아가 $\mathfrak{g} = \text{Lie}(G)$의 표현도 마찬가지이다. Lie algebra의 표현은 벡터공간 $V$와 $\mathfrak{g} \to \mathfrak{gl}(V)$의 Lie algebra homomorphism $\rho$로 정의되며, 이를 통해 $V$를 $\mathfrak{g}$-모듈로 본다.

이러한 관점은 매우 유용하다. 왜냐하면 **$\mathfrak{g}$-모듈 위의 구조를 이해하는 것은 선형대수의 관점에서 보면, 일련의 commuting (또는 related) linear operators 위의 구조를 이해하는 것**이기 때문이다. 

## Adjoint representation과 root space decomposition

이제 특별한 표현 하나를 생각하자: adjoint representation이다. [§리 군, ⁋정의 19](/ko/math/Lie_theory/Lie_groups#def19)에서 정의한 바와 같이, Lie algebra $\mathfrak{g}$는 adjoint action을 통해 자기 자신 위에 표현된다:

$$\text{ad}: \mathfrak{g} \to \mathfrak{gl}(\mathfrak{g}), \quad \text{ad}_X(Y) = [X, Y]$$

따라서 $\mathfrak{g}$는 $\mathfrak{g}$-모듈이다.

이제 Semisimple Lie algebra $\mathfrak{g}$의 Cartan subalgebra $\mathfrak{h}$를 고정하자. $\mathfrak{h}$는 maximal abelian Lie subalgebra이므로, 그 위의 모든 원소들은 서로 commute한다:

$$[H_1, H_2] = 0 \quad \text{for all } H_1, H_2 \in \mathfrak{h}$$

선형대수의 관점에서 보면, $\mathfrak{h}$의 모든 adjoint operator들은 서로 commute한다:

$$[\text{ad}_{H_1}, \text{ad}_{H_2}] = 0$$

이는 중요한 결과를 의미한다. **Commuting linear operators들은 동시에 대각화 가능하다.** 따라서 우리는 $\mathfrak{g}$를 이들의 동시 고유공간(simultaneous eigenspace)들로 분해할 수 있다.

구체적으로, 각 linear functional $\lambda: \mathfrak{h} \to \mathbb{C}$에 대하여, 다음과 같이 정의한다:

$$\mathfrak{g}_\lambda = \{X \in \mathfrak{g} \mid [H, X] = \lambda(H)X \text{ for all } H \in \mathfrak{h}\}$$

그러면 

$$\mathfrak{g} = \bigoplus_{\lambda \in \mathfrak{h}^*} \mathfrak{g}_\lambda$$

이다. 이것이 **weight space decomposition**이다.

## Root space와 근계의 정의

이제 이 분해에서 특별한 부분들을 주목하자. $\lambda = 0$인 경우:

$$\mathfrak{g}_0 = \{X \in \mathfrak{g} \mid [H, X] = 0 \text{ for all } H \in \mathfrak{h}\}$$

이는 $\mathfrak{h}$의 centralizer이고, $\mathfrak{h}$의 maximality에 의해 $\mathfrak{g}_0 = \mathfrak{h}$이다.

따라서 분해를 다시 쓰면:

$$\mathfrak{g} = \mathfrak{h} \oplus \bigoplus_{\lambda \in \mathfrak{h}^* \setminus \{0\}} \mathfrak{g}_\lambda$$

**Nonzero functional들** 중에서 $\mathfrak{g}_\lambda \neq 0$인 것들을 **root**라고 부른다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Semisimple Lie algebra $\mathfrak{g}$와 Cartan subalgebra $\mathfrak{h}$에 대하여, **root**들의 집합은

$$\Phi = \{\alpha \in \mathfrak{h}^* \setminus \{0\} \mid \mathfrak{g}_\alpha \neq 0\}$$

이다. 각 $\alpha \in \Phi$에 대해 $\mathfrak{g}_\alpha$를 **root space**라 부른다.

</div>

이제 root space decomposition은 다음과 같이 쓸 수 있다:

$$\mathfrak{g} = \mathfrak{h} \oplus \bigoplus_{\alpha \in \Phi} \mathfrak{g}_\alpha$$

선형대수와의 유사성을 명확히 하면:

| 선형대수 | Lie 이론 |
|---------|---------|
| 행렬 $A$의 고유값 | Cartan subalgebra $\mathfrak{h}$에 대한 root |
| 고유공간 $E_\lambda$ | Root space $\mathfrak{g}_\alpha$ |
| 고유벡터 | Root vector |
| 고유공간 분해 $V = \bigoplus E_\lambda$ | Root space 분해 $\mathfrak{g} = \bigoplus \mathfrak{g}_\alpha$ |

차이는 단일 operator $A$ 대신 Cartan subalgebra $\mathfrak{h}$라는 **전체 family of commuting operators**를 동시에 대각화한다는 점이다.

## Killing form과 근계의 구조

지금까지는 purely algebraic한 구조를 다루었다. 이제 **기하학적 구조**를 도입한다.

Semisimple Lie algebra는 Killing form을 가진다:

$$B(X, Y) = \text{tr}(\text{ad}_X \circ \text{ad}_Y)$$

이 form은 non-degenerate이며, $\mathfrak{h}$ 위에도 non-degenerate하다. 따라서 canonical isomorphism 

$$\mathfrak{h} \xrightarrow{\sim} \mathfrak{h}^*: H \mapsto B(H, \cdot)$$

이 존재한다. 이를 통해 $\mathfrak{h}^*$를 inner product space로 볼 수 있다. 구체적으로, $\alpha, \beta \in \mathfrak{h}^*$에 대응되는 $H_\alpha, H_\beta \in \mathfrak{h}$가 있을 때,

$$(\alpha, \beta) := B(H_\alpha, H_\beta)$$

로 정의한다. 이제 roots들이 이 inner product에 대해 어떤 구조를 가지는지 살펴보자.

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

Root system의 조건들은 roots의 기하학적 관계가 매우 제한적임을 보여준다. 조건 4의 정수성과 조건 2의 정규화로부터, 두 roots가 이룰 수 있는 각도는 $30°, 45°, 60°, 90°, 120°, 135°, 150°$ 등으로 극히 제한된다.

<div class="proposition" markdown="1">

<ins id="prop1">**명제 1**</ins> Semisimple Lie algebra $\mathfrak{g}$의 Cartan subalgebra $\mathfrak{h}$에 대하여, Killing form으로부터 정의된 roots의 집합 $\Phi \subset \mathfrak{h}^*$는 $\mathfrak{h}^*$의 root system이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

조건 1은 root space decomposition으로부터 명백하다. 조건 2도 root의 정의에서 자명하다.

조건 3을 위해, $\alpha, \beta \in \Phi$이고 $E_\alpha \in \mathfrak{g}_\alpha$, $E_\beta \in \mathfrak{g}_\beta$라 하자. Jacobi identity 

$$[H, [E_\alpha, E_\beta]] = [[H, E_\alpha], E_\beta] + [E_\alpha, [H, E_\beta]]$$

로부터

$$[H, [E_\alpha, E_\beta]] = (\alpha(H) + \beta(H))[E_\alpha, E_\beta]$$

가 따른다. 따라서 $[E_\alpha, E_\beta]$는 weight $\alpha + \beta$를 가지거나 영벡터이다. 더 자세한 분석 (예: string representation)을 통해 reflection $s_\alpha$가 roots를 보존함을 보일 수 있다.

조건 4의 정수성은 root space와 Killing form의 구조로부터 자명하다.

</details>

## Simple roots와 Cartan matrix

Root space decomposition의 구조는 매우 복잡하지만, 모든 roots를 명시적으로 알 필요는 없다. 마치 고유공간의 basis들로 충분하듯이, **simple roots**만으로 전체 root system을 재구성할 수 있다.

먼저 positive roots의 system $\Phi^+ \subset \Phi$를 선택한다. 이는 각 root에 대해 정확히 하나의 방향을 선택하는 것이고, 적절한 ordering으로부터 정의된다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> Positive roots $\Phi^+ \subset \Phi$에 대하여, $\alpha \in \Phi^+$가 **simple root**라는 것은 $\alpha$를 $\Phi^+$의 다른 원소들의 음이 아닌 정수 일차결합으로 표현할 수 없는 것이다. Simple roots의 모임을 $\Delta$라 표기한다.

</div>

중요한 사실은 모든 positive root가 simple roots의 음이 아닌 정수 일차결합으로 **유일하게** 표현된다는 것이다. 따라서 root system 전체는 simple roots의 구조, 즉 그들 사이의 inner products에 의해 완전히 결정된다.

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> Simple roots $\Delta = \{\alpha_1, \ldots, \alpha_l\}$에 대하여, **Cartan matrix**는

$$A = (a_{ij})_{1 \le i,j \le l}, \quad a_{ij} = \langle \alpha_i, \alpha_j \rangle = 2\frac{(\alpha_i, \alpha_j)}{(\alpha_j, \alpha_j)}$$

로 정의된다.

</div>

Cartan matrix는 다음의 성질을 가진다:
- 대각 성분: $a_{ii} = 2$
- 비대각 성분 $a_{ij}$ ($i \neq j$): root 사이의 각도 제약에 의해 $a_{ij} \in \{-3, -2, -1, 0\}$
- 행과 열을 permute했을 때 다른 형태가 되면, root system도 decomposable이다.

이 유한한 행렬 하나가 **전체 semisimple Lie algebra의 root space 구조를 완전히 결정한다**. 

## Weyl group과 근계의 대칭성

Root system의 정의 조건 3에서 각 root에 대한 reflection이 $\Phi$를 보존한다고 했다. 이러한 reflections들로 생성되는 group을 정의하자.

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> Root system $\Phi$의 **Weyl group**은

$$W(\Phi) := \langle s_\alpha \mid \alpha \in \Phi \rangle \subset O(E)$$

이다. 즉, 모든 root reflections로 생성되는 orthogonal group의 부분군이다.

</div>

Weyl group은 root system의 **모든 대칭**을 담당한다. 

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> 임의의 root system $\Phi$에 대하여, Weyl group $W(\Phi)$는 유한군이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

각 reflection $s_\alpha$는 유한집합 $\Phi$ 위에 작용한다. Root system의 조건 3에 의해 모든 reflections는 $\Phi$를 보존하므로, Weyl group은 대칭군 $S_\Phi$의 부분군이다. 따라서 유한하다.

</details>

중요한 관찰은 Weyl group이 simple reflections $\{s_{\alpha_i}\}$ (simple roots에 대한 reflection)로 생성된다는 것이다. 따라서 Cartan matrix를 알면 Weyl group의 구조도 파악할 수 있다.

## 결론: 선형대수에서 근계로

우리는 다음과 같은 길을 걸어왔다:

1. **G-모듈 관점**: Lie algebra $\mathfrak{g}$의 표현을 $\mathfrak{g}$-모듈로 본다.
2. **동시 대각화**: Cartan subalgebra $\mathfrak{h}$의 모든 원소들이 동시에 대각화 가능하다.
3. **Weight space decomposition**: $\mathfrak{g}$를 동시 고유공간들로 분해한다.
4. **Root space decomposition**: Nonzero weight들만 따로 모아 roots를 정의한다.
5. **기하학적 구조**: Killing form으로부터 정의된 inner product에서 roots는 root system을 이룬다.
6. **간결한 표현**: Simple roots와 Cartan matrix로 전체 구조를 인코딩한다.
7. **대칭성**: Weyl group이 모든 대칭을 담당한다.

이는 모두 선형대수의 기본 개념 **"행렬의 동시 고유공간 분해"**에서 출발한 것이다. Lie theory는 이 아이디어를 여러 개의 non-commuting operators로 확장하고, 그 결과적 구조를 깊이 있게 분석하는 학문이라고 할 수 있다.

---

**참고문헌**
- Humphreys, J. E. *Introduction to Lie Algebras and Representation Theory*. Springer, 1972.
- Serre, J.-P. *Complex Semisimple Lie Algebras*. Springer, 1987.

