---
title: "From Diagonalization to Weight Spaces: A Bridge Between Linear Algebra and Lie Theory"
categories:
  - Mathematics
  - Linear Algebra
  - Lie Theory
tags:
  - diagonalization
  - eigenspace decomposition
  - Jordan canonical form
  - weight space decomposition
  - root system
  - representation theory
  - Cartan subalgebra
  - highest weight theory
---

## 1. Introduction

선형대수학에서 [대각화](/ko/math/linear_algebra/eigenspace_decomposition)와 [Jordan 표준형](/ko/math/linear_algebra/Jordan_canonical_form)은 선형변환의 구조를 파악하는 강력한 도구들이다. 복소수체 $\mathbb{C}$ 위의 유한차원 벡터공간 $V$와 선형변환 $T \in \operatorname{End}(V)$가 주어졌을 때, $T$의 고유공간 분해

$$V = \bigoplus_{\lambda \in \sigma(T)} E_\lambda(T)$$

는 $T$가 각 고유공간 위에서 스칼라곱으로 작용함을 의미하며, 이는 $T$의 가장 단순한 형태—대각행렬—를 제공한다. 대각화가 불가능한 경우에도 [일반화된 고유공간](/ko/math/linear_algebra/Jordan_canonical_form)을 통해

$$V = \bigoplus_{\lambda \in \sigma(T)} G_\lambda(T)$$

로 분해하고, 적절한 기저 아래 Jordan 표준형을 얻을 수 있다.

이번 글에서는 이러한 선형대수학의 구조들이 Lie theory에서 어떻게 자연스럽고 비약적으로 확장되는지 탐구한다. 특히 다음 대응관계에 초점을 맞춘다:

| 선형대수 | Lie theory |
|---------|-----------|
| 고유값 $\lambda$ | weight $\mu \in \mathfrak{h}^*$ |
| 고유공간 $E_\lambda(T)$ | weight space $V_\mu$ |
| 동시 대각화 가능한 가환족 | Cartan 부분대수 $\mathfrak{h}$ |
| 특성다항식 $\chi_T(t)$ | 표현의 문자 $\chi_V$ |
| 고유값의 중복도 | weight의 multiplicity |

## 2. The Analogy: From Eigenspaces to Weight Spaces

### 2.1 Cartan 부분대수와 동시 대각화

선형대수학에서 서로 교환하는 행렬들은 동시에 대각화될 수 있다. 구체적으로, 가환하는 $T_1, T_2 \in \operatorname{End}(V)$에 대해, 각각이 diagonalizable이면 $V$의 어떤 기저 아래에서 $T_1$과 $T_2$가 동시에 대각행렬이 된다.

Lie theory에서는 이 개념이 **Cartan 부분대수**로 확장된다.

**정의 2.1.** Lie 대수 $\mathfrak{g}$의 부분대수 $\mathfrak{h} \subseteq \mathfrak{g}$가 **Cartan 부분대수**라 함은 다음을 만족하는 것이다:

1. $\mathfrak{h}$는 가환(abelian)이다: $[H_1, H_2] = 0$ for all $H_1, H_2 \in \mathfrak{h}$.
2. $\mathfrak{h}$는 극대가환(maximal abelian)이다: $\mathfrak{h} \subsetneq \mathfrak{h}'$이고 $\mathfrak{h}'$가 가환인 부분대수는 존재하지 않는다.
3. 각 $H \in \mathfrak{h}$에 대해 $\operatorname{ad}_H \in \operatorname{End}(\mathfrak{g})$는 반단순(semisimple)이다.

**정리 2.2 (Cartan 부분대수의 존재성).** 임의의 유한차원 복소 반단순 Lie 대수 $\mathfrak{g}$는 Cartan 부분대수를 가진다.

**예시 2.3.** $\mathfrak{g} = \mathfrak{sl}(n; \mathbb{C})$ (trace가 0인 $n \times n$ 복소행렬)의 경우,

$$\mathfrak{h} = \{\operatorname{diag}(h_1, \ldots, h_n) : h_1 + \cdots + h_n = 0\}$$

이 Cartan 부분대수가 된다. 이는 $\mathfrak{sl}(n; \mathbb{C})$의 모든 대각행렬들이며, 차원은 $n-1$ (rank)이다.

### 2.2 Weight Space Decomposition

선형대수학에서 $T \in \operatorname{End}(V)$의 고유값 $\lambda$는 $T v = \lambda v$를 만족하는 스칼라였다. Lie theory에서는 이 개념이 선형범함수로 확장된다.

**정의 2.4.** $(\pi, V)$가 Lie 대수 $\mathfrak{g}$의 유한차원 표현이고, $\mathfrak{h} \subseteq \mathfrak{g}$가 Cartan 부분대수라 하자. 선형범함수 $\mu \in \mathfrak{h}^*$가 **weight**라 함은,

$$V_\mu = \{v \in V : \pi(H)v = \mu(H)v \text{ for all } H \in \mathfrak{h}\} \neq 0$$

을 만족하는 것이다. $V_\mu$를 **weight space**, 그 원소를 **weight vector**라 한다.

**정리 2.5 (Weight Space Decomposition).** 유한차원 복소 표현 $(\pi, V)$에 대해,

$$V = \bigoplus_{\mu \in \mathfrak{h}^*} V_\mu$$

이 성립한다. 즉, $V$는 weight space들의 직합으로 분필된다.

**증명.** $\{\pi(H) : H \in \mathfrak{h}\}$는 서로 교환하는 반단순 선형변환들의 모임이다. 교환하는 반단순 변환들은 동시에 대각화 가능하므로, $V$의 적절한 기저가 존재하여 각 $\pi(H)$가 대각행렬이 된다. 이 기저의 각 벡터는 어떤 $\mu \in \mathfrak{h}^*$에 대한 weight vector이며, weight가 다른 weight vector들은 선형독립이므로 직합 분해가 얻어진다. $\square$

**선형대수와의 비교:**
- 선형대수: 하나의 $T$에 대해 $V = \bigoplus_\lambda E_\lambda(T)$
- Lie theory: 가환족 $\{\pi(H)\}$에 대해 $V = \bigoplus_\mu V_\mu$

즉, weight space decomposition은 "다수의 동시 대각화 가능한 연산자들에 의한 공간 분해"로 이해할 수 있다.

## 3. Root Space Decomposition: The Adjoint Representation

선형대수학에서 $T$의 고유값 분해는 $T$ 자체의 구조를 이해하는 데 사용된다. 마찬가지로, Lie 대수 $\mathfrak{g}$ 자체에 adjoint representation $\operatorname{ad}: \mathfrak{g} \to \mathfrak{gl}(\mathfrak{g})$을 적용하면 $\mathfrak{g}$의 구조를 완전히 파악할 수 있다.

### 3.1 Root와 Root Space

**정의 3.1.** $\mathfrak{h} \subseteq \mathfrak{g}$가 Cartan 부분대수일 때, **root**는 $0 \neq \alpha \in \mathfrak{h}^*$로서,

$$\mathfrak{g}_\alpha = \{X \in \mathfrak{g} : [H, X] = \alpha(H)X \text{ for all } H \in \mathfrak{h}\} \neq 0$$

을 만족하는 것이다. $\mathfrak{g}_\alpha$를 **root space**라 한다.

**정리 3.2 (Root Space Decomposition).** 반단순 Lie 대수 $\mathfrak{g}$는 다음과 같이 분필된다:

$$\mathfrak{g} = \mathfrak{h} \oplus \bigoplus_{\alpha \in \Phi} \mathfrak{g}_\alpha$$

여기서 $\Phi \subseteq \mathfrak{h}^* \setminus \{0\}$는 모든 root들의 집합(root system)이다.

**해석:** 각 $H \in \mathfrak{h}$에 대해 $\operatorname{ad}_H \in \operatorname{End}(\mathfrak{g})$를 고려하면, $\operatorname{ad}_H$의 고유값이 바로 $\alpha(H)$이며, 고유공간이 $\mathfrak{g}_\alpha$가 된다. 즉, root space decomposition은 adjoint representation에 대한 weight space decomposition이다.

### 3.2 Root System의 성질

**정리 3.3.** 반단순 Lie 대수 $\mathfrak{g}$의 root system $\Phi$는 다음 성질들을 만족한다:

1. $\Phi$는 유한집합이며, $\mathfrak{h}^*$를 span한다.
2. $-\alpha \in \Phi$ for all $\alpha \in \Phi$.
3. $[\mathfrak{g}_\alpha, \mathfrak{g}_\beta] \subseteq \mathfrak{g}_{\alpha + \beta}$ for all $\alpha, \beta \in \Phi$.
4. $\dim \mathfrak{g}_\alpha = 1$ for all $\alpha \in \Phi$.

**증명 (3번).** $X \in \mathfrak{g}_\alpha$, $Y \in \mathfrak{g}_\beta$에 대해 Jacobi identity:

$$[H, [X, Y]] = [[H, X], Y] + [X, [H, Y]] = \alpha(H)[X, Y] + \beta(H)[X, Y] = (\alpha + \beta)(H)[X, Y]$$

따라서 $[X, Y] \in \mathfrak{g}_{\alpha + \beta}$. $\square$

이 정리는 Lie 대수의 bracket 구조가 root들의 "기하학"에 의해 결정됨을 보여준다: 두 root space의 bracket은 그 합이 root인 경우에만 non-zero일 수 있다.

## 4. Root System의 구조: $\mathfrak{sl}(3; \mathbb{C})$ 예시

구체적인 예로 $\mathfrak{sl}(3; \mathbb{C})$를 분석하자.

### 4.1 설정

$$\mathfrak{sl}(3; \mathbb{C}) = \{X \in M_3(\mathbb{C}) : \operatorname{tr}(X) = 0\}$$

Cartan 부분대수:
$$\mathfrak{h} = \left\{\begin{pmatrix} h_1 & 0 & 0 \\ 0 & h_2 & 0 \\ 0 & 0 & h_3 \end{pmatrix} : h_1 + h_2 + h_3 = 0\right\}$$

$"mathfrak{h}^*$는 $\mathfrak{h}$ 위의 선형범함수들의 공간이다. $L_i \in \mathfrak{h}^*$를

$$L_i\left(\operatorname{diag}(h_1, h_2, h_3)\right) = h_i$$

로 정의하면, $L_1 + L_2 + L_3 = 0$이 제약조건이 된다.

### 4.2 Root들의 계산

$E_{ij}$ ($i \neq j$)를 $(i,j)$-성분이 1이고 나머지가 0인 행렬이라 하자. $H = \operatorname{diag}(h_1, h_2, h_3) \in \mathfrak{h}$에 대해:

$$[H, E_{ij}] = (h_i - h_j)E_{ij} = (L_i - L_j)(H) \cdot E_{ij}$$

따라서 $E_{ij} \in \mathfrak{g}_{L_i - L_j}$이고, root는 다음 6개이다:

$$\Phi = \{L_1 - L_2, L_2 - L_3, L_1 - L_3, L_2 - L_1, L_3 - L_2, L_3 - L_1\}$$

즉, $\alpha = L_i - L_j$에 대해 $\mathfrak{g}_\alpha = \mathbb{C} \cdot E_{ij}$이다.

### 4.3 Root의 기하학

$L_1, L_2$를 좌표축으로 하는 평면에서 ($L_3 = -L_1 - L_2$), root들은 다음 위치에 있다:
- $\alpha_1 = L_1 - L_2 = (1, -1, 0)$: simple root
- $\alpha_2 = L_2 - L_3 = (0, 1, -1)$: simple root  
- $\alpha_1 + \alpha_2 = L_1 - L_3 = (1, 0, -1)$: positive root
- 이들의 음수: negative roots

이는 **$A_2$ type root system**의 표준 그림이다.

**Killing form**으로부터 유도된 내적 $\langle \cdot, \cdot \rangle$을 사용하면,

$$\langle L_i, L_j \rangle = \delta_{ij} - \frac{1}{3}$$

따라서
$$\langle \alpha_1, \alpha_1 \rangle = \langle \alpha_2, \alpha_2 \rangle = 2, \quad \langle \alpha_1, \alpha_2 \rangle = -1$$

두 simple root 사이의 각도는 $120°$이다.

## 5. Highest Weight Theory

선형대수학에서 diagonalizable operator $T$는 고유값들로 완전히 결정된다. 마찬가지로, 반단순 Lie 대수의 불가약 표현은 "highest weight"로 완전히 분류된다.

### 5.1 Highest Weight의 정의

**정의 5.1.** Root system $\Phi$에 대해, **positive root** $\Phi^+$를 선택하자. Weight $\mu \in \mathfrak{h}^*$가 **dominant**하다 함은 모든 $\alpha \in \Phi^+$에 대해

$$\frac{2\langle \mu, \alpha \rangle}{\langle \alpha, \alpha \rangle} \geq 0$$

을 만족하는 것이다. 또한 $\mu$가 **integral**하다 함은 위 값이 정수인 것이다.

**정의 5.2.** 표현 $(\pi, V)$의 weight $\mu$가 **highest weight**라 함은, 임의의 다른 weight $\nu$에 대해 $\nu \preceq \mu$ (즉 $\mu - \nu$가 positive root들의 non-negative 정수계수 선형결합)인 것이다.

### 5.2 Highest Weight Classification Theorem

**정리 5.3 (Theorem of the Highest Weight).** 반단순 Lie 대수 $\mathfrak{g}$의 유한차원 불가약 표현에 대해 다음이 성립한다:

1. 각 불가약 표현은 고유한 highest weight $\lambda$를 가진다.
2. Highest weight $\lambda$는 반드시 dominant integral이어야 한다.
3. Dominant integral $\lambda$마다, highest weight $\lambda$를 가지는 불가약 표현이 존재하고, 이는 동형을 제외하고 유일하다.
4. 표현 $V$는 $V = \bigoplus_{\mu} V_\mu$ (weight space들의 직합)이며, $V_\lambda$는 1차원이다.

**증명 개요:**

- **존재성:** Verma module $M_\lambda = U(\mathfrak{g}) \otimes_{U(\mathfrak{b})} \mathbb{C}_\lambda$을 구성하고, 이의 유일한 최대 proper submodule을 quotient하여 불가약 표현 $L_\lambda$를 얻는다.

- **유일성:** $\lambda$가 highest weight인 cyclic representation $V$를 생각하면, $V$는 $U(\mathfrak{n}^-) \cdot v_\lambda$로 생성되며, PBW theorem에 의해 차원이 결정된다.

- **완전환원성:** Weyl's unitary trick이나 Casimir operator의 양정값성을 이용하여, 유한차원 표현이 반드시 완전히 환원됨을 보인다. $\square$

### 5.3 Weight Diagram과 Multiplicity

**정의 5.4.** 표현 $V$에서 weight $\mu$의 **multiplicity**는 $\dim V_\mu$로 정의된다.

**정리 5.5 (Kostant's Multiplicity Formula).** Highest weight $\lambda$를 가지는 불가약 표현 $L_\lambda$에서 weight $\mu$의 multiplicity는

$$\dim (L_\lambda)_\mu = \sum_{w \in W} (-1)^{\ell(w)} \mathfrak{P}(w(\lambda + \rho) - (\mu + \rho))$$

으로 주어진다. 여기서 $W$는 Weyl group, $\rho$는 half sum of positive roots, $\mathfrak{P}$는 partition function이다.

**예시 5.6 ($\mathfrak{sl}(3; \mathbb{C})$).** Highest weight $\lambda = (m_1, m_2) = m_1 \omega_1 + m_2 \omega_2$ (여기서 $\omega_i$는 fundamental weight)에 대한 표현 $L_\lambda$의 weight diagram은 정삼각형 꼴을 이룬다. 꼭짓점들은 $\lambda$, $w_1 \cdot \lambda$, $w_2 \cdot \lambda$ (Weyl group 작용)이며, 가장자리와 내부의 weight들은 그들의 multiplicity로 표시된다.

## 6. Lie Theory에서의 Jordan Decomposition Analogy

선형대수학에서 임의의 $T \in \operatorname{End}(V)$는 Jordan-Chevalley decomposition

$$T = S + N$$

(여기서 $S$는 semisimple, $N$은 nilpotent, $[S, N] = 0$)을 가진다. 이는 Lie theory에서 다음과 같이 확장된다.

### 6.1 Abstract Jordan Decomposition

**정리 6.1.** 유한차원 복소 Lie 대수 $\mathfrak{g}$의 임의의 원소 $X \in \mathfrak{g}$는 유일하게

$$X = S + N$$

(여기서 $S$는 $\operatorname{ad}_S$가 반단순, $N$은 $\operatorname{ad}_N$이 nilpotent, $[S, N] = 0$)으로 분필된다.

**증명.** $\operatorname{ad}: \mathfrak{g} \to \mathfrak{gl}(\mathfrak{g})$가 단사인 것을 이용하여, $\operatorname{ad}_X = (\operatorname{ad}_X)_s + (\operatorname{ad}_X)_n$ (일반적인 Jordan decomposition)을 $\mathfrak{g}$로 pullback한다. $\square$

### 6.2 표현에서의 호환성

**정리 6.2.** $(\pi, V)$가 $\mathfrak{g}$의 유한차원 표현이고 $X = S + N$이 abstract Jordan decomposition이라면, $\pi(X) = \pi(S) + \pi(N)$은 $\pi(X)$의 (보통 의미의) Jordan decomposition이다.

이 정리는 표현론에서 abstract Lie 대수의 구조와 concrete matrix realization이 어떻게 일치하는지를 보여준다.

## 7. Conclusion: The Unity of Structure

선형대수학의 고유값-고유벡터 이론은 Lie theory에서 다음과 같이 풍부한 구조로 확장된다:

| 구조 | 선형대수 | Lie theory |
|-----|---------|-----------|
| 분해 대상 | $(T, V)$ | $(\pi, V)$, $\mathfrak{g}$ |
| 가환 연산자 | 단일 $T$ | Cartan $\mathfrak{h}$ |
| 스펙트럼 | 고유값 $\lambda$ | weight $\mu \in \mathfrak{h}^*$ |
| 공간 분해 | $V = \bigoplus_\lambda E_\lambda$ | $V = \bigoplus_\mu V_\mu$ |
| 고유공간 구조 | $T|_{E_\lambda} = \lambda I$ | $\pi(H)|_{V_\mu} = \mu(H) I$ |
| 추가 구조 | 없음 | root system, Weyl group |
| 분류 불변량 | 고유값들 | highest weight |
| 완전환원성 | diagonalizable = 직합 | Weyl's theorem |

특히 중요한 것은, 선형대수학에서 "대각화 불가능"은 병리적 현상이었지만, Lie theory에서는 root system의 geometric constraint가 이를 자연스럽게 해결하여, highest weight theory라는 우아한 분류 정리를 제공한다는 점이다.

## References

1. Mark S. Gockenbach, *Finite-Dimensional Linear Algebra*, CRC Press, 2011.
2. Brian C. Hall, *Lie Groups, Lie Algebras, and Representations*, 2nd ed., Springer, 2015.
3. James E. Humphreys, *Introduction to Lie Algebras and Representation Theory*, Springer, 1980.
4. William Fulton and Joe Harris, *Representation Theory: A First Course*, Springer, 1991.
