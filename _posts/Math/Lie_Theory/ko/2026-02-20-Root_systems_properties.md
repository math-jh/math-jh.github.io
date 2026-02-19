---
title: "Root System의 정의와 성질"
excerpt: "Formal definition과 basic properties"

categories: [Math / Lie Theory]
permalink: /ko/math/Lie_theory/root_systems_properties
header:
    overlay_image: /assets/images/Math/Lie_Theory/Root_systems.png
    overlay_filter: 0.5
sidebar: 
    nav: "Lie_theory-ko"

date: 2026-02-20
last_modified_at: 2026-02-20
weight: 3

---

## Root System의 정의

우리는 유한차원 real vector space $V$에서 정의되는 root system의 개념으로 시작한다. 이는 리 대수의 구조를 연구하는 데 있어 핵심적인 역할을 하며, 특히 semisimple Lie 대수의 분류와 표현론으로 연결되는 다리 역할을 한다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 실수 벡터공간 $V$의 유한 부분집합 $\Phi \subset V$가 다음 조건들을 만족할 때, $\Phi$를 *root system*이라 부른다:

1. $\Phi$는 $V$의 원점이 아닌 벡터들이며, $0 \notin \Phi$.
2. $\Phi$가 generate하는 실 벡터공간의 차원은 $V$와 같다.
3. $\Phi$에 대해 정의된 reflection $s_\alpha \in \Aut(V)$가 $\Phi$를 보존한다: $s_\alpha(\Phi) = \Phi$ for all $\alpha \in \Phi$.
4. $\Phi$에 대해 정의된 쌍선형 형식 $(\cdot, \cdot)$이 양의 정부호 symmetric form이라 하자. 각 $\alpha, \beta \in \Phi$에 대하여, 정수 $n_{\beta, \alpha} := \frac{2(\beta, \alpha)}{(\alpha, \alpha)}$는 $\beta - n_{\beta, \alpha}\alpha \in \Phi$임을 의미한다.

여기서 reflection $s_\alpha$는 다음과 같이 정의된다:

$$s_\alpha(v) = v - 2\frac{(\alpha, v)}{(\alpha, \alpha)}\alpha.$$

</div>

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins> $V = \mathbb{R}^2$에서 root system $A_2$를 고려한다. $\Phi = \{\pm e_1 \pm e_2, \pm e_1, \pm e_2\}$로 정의한다. 여기서 $e_1, e_2$는 표준 기저이다. 이 집합은 $A_2$ type의 root system을 이룬다.

</div>

root system의 중요한 성질 중 하나는 이들의 간격이 정수 배수 관계로 연결된다는 점이다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> 임의의 root system $\Phi$에서, 두 roots $\alpha, \beta \in \Phi$에 대하여, 다음의 정수 값들이 존재한다:

$$r_{\alpha, \beta} = \frac{2(\alpha, \beta)}{(\beta, \beta)}, \quad s_{\alpha, \beta} = \frac{2(\alpha, \beta)}{(\alpha, \alpha)}$$

그리고 $\alpha - r_{\alpha, \beta}\beta$와 $\beta - s_{\alpha, \beta}\alpha$는 $\Phi$의 원소이다.

</div>

<div class="proof" markdown="1">

<details class="proof" markdown="1">
<summary>증명</summary>

$\Phi$의 정의에 따르면, $n_{\alpha, \beta} = \frac{2(\alpha, \beta)}{(\beta, \beta)}$는 정수이며, $\beta - n_{\alpha, \beta}\alpha \in \Phi$이다. 이는 $r_{\alpha, \beta}$가 정수임을 의미한다. 마찬가지로 $s_{\alpha, \beta}$도 정수이다.

</details>
</div>

<div class="lemma" markdown="1">

<ins id="lemma4">**보조정리 4**</ins> 임의의 root system $\Phi$에서, $\Phi$를 생성하는 basis가 존재한다. 즉, $\Phi$의 원소들을 linear combination으로 표현할 수 있는 기저 $\Delta \subset \Phi$가 존재하며, $\Delta$의 원소들은 모두 positive root이거나 negative root이다.

</div>

## Root System의 분류를 위한 준비

Root system을 분류하기 전에 몇 가지 기본 개념을 정의해야 한다.

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> root system $\Phi$에 대하여, $\Phi^+$와 $\Phi^-$를 각각 positive root과 negative root의 집합이라고 부른다. 이들은 임의의 hyperplane $H$에 의해 결정되며, $\Phi = \Phi^+ \cup \Phi^-$이고, $\Phi^+ \cap \Phi^- = \emptyset$이다.

</div>

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> root system $\Phi$의 기저 $\Delta$는 $\Phi^+$의 원소들 중 다음 두 조건을 만족하는 subset이다:

1. $\Delta$는 $\Phi^+$를 생성하는 basis이다.
2. $\Delta$의 각 원소는 irreducible하게 표현될 수 있다.

</div>

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> 임의의 root system $\Phi$에 대하여, 기저 $\Delta$는 유한하며, $\Phi$의 모든 positive root은 $\Delta$의 elements의 정수 선형결합으로 표현될 수 있다. 또한, coefficients는 모두 비음수 정수이다.

</div>

<div class="proof" markdown="1">

<details class="proof" markdown="1">
<summary>증명</summary>

$\Phi^+$가 유한집합이고, $\Delta$가 basis이므로, 각 positive root $\alpha \in \Phi^+$는 $\Delta$의 elements의 선형결합으로 표현된다. $\Phi$의 정의에 따르면, $\Delta$의 각 원소는 irreducible하게 표현되므로 coefficients는 모두 비음수 정수이다.

</details>
</div>

## Cartan Matrix

Root system의 분류는 주로 Cartan matrix를 통해 이루어진다.

<div class="definition" markdown="1">

<ins id="def8">**정의 8**</ins> root system $\Phi$의 기저 $\Delta = \{\alpha_1, \alpha_2, \dots, \alpha_n\}$가 주어졌을 때, *Cartan matrix* $A$는 다음과 같이 정의된다:

$$A_{ij} = \frac{2(\alpha_i, \alpha_j)}{(\alpha_i, \alpha_i)}.$$

</div>

Cartan matrix는 중요한 성질들을 가지고 있다.

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> Cartan matrix $A$는 정수행렬이며, 대각선 원소는 $2$이고, $i \neq j$인 경우 $A_{ij} \leq 0$이다. 또한, $A$는 대각 행렬이 아닌 경우 모두 $0$이 아닌 원소를 가진다.

</div>

<div class="example" markdown="1">

<ins id="ex10">**예시 10**</ins> $A_n$ type의 root system에서, 기저 $\Delta = \{\alpha_1, \alpha_2, \dots, \alpha_n\}$는 다음의 Cartan matrix를 가진다:

$$A = \begin{pmatrix}
2 & -1 & 0 & \cdots & 0 \\
-1 & 2 & -1 & \cdots & 0 \\
0 & -1 & 2 & \cdots & 0 \\
\vdots & \vdots & \vdots & \ddots & -1 \\
0 & 0 & 0 & -1 & 2
\end{pmatrix}.$$

</div>

## Root System의 몇 가지 기본 성질

<div class="theorem" markdown="1">

<ins id="thm11">**정리 11**</ins> 임의의 root system $\Phi$에 대하여, $\Phi$의 cardinality는 $|\Phi| = 2m$이며, 여기서 $m$은 positive root의 개수이다.

</div>

<div class="corollary" markdown="1">

<ins id="cor12">**따름정리 12**</ins> root system $\Phi$에서 모든 root는 같은 길이를 가지지 않을 수 있지만, $\Phi$가 irreducible할 때, 적어도 두 개의 서로 다른 길이를 가진 root들이 존재한다.

</div>

<div class="proposition" markdown="1">

<ins id="prop13">**명제 13**</ins> root system $\Phi$의 모든 roots는 같은 길이를 가지거나, 두 개의 다른 길이를 가진다. 전자의 경우, $\Phi$를 simply laced라고 부르고, 후자의 경우, long roots와 short roots가 존재한다.

</div>

---

**참고문헌**

**[Humph]** J. E. Humphreys, *Introduction to Lie Algebras and Representation Theory*, Springer, 1972  
**[Var]** V. S. Varadarajan, *Lie Groups, Lie Algebras, and Their Representations*, Springer, 1984  
**[Knapp]** A. W. Knapp, *Lie Groups Beyond an Introduction*, Birkhäuser, 2002
