---

title: "원환면의 작용 - 추가 예정"
excerpt: ""

categories: [Math / Lie Theory]
permalink: /ko/math/lie_theory/torus_action
header:
    overlay_image: /assets/images/Math/Lie_Theory/Torus_action.png
    overlay_filter: 0.5
sidebar: 
    nav: "Lie_theory-ko"

date: 2026-02-24
last_modified_at: 2026-02-27
weight: 2

---

## 예시: $SU(2)$

지금까지의 논의를 구체적인 예시에서 확인해보자. Special unitary group

$$SU(2)=\{A\in\GL(2,\mathbb{C})\mid A^\dagger A=I,\ \det A=1\}$$

은 compact connected Lie group이다. 이 group의 maximal torus를 찾아보자.

<div class="proposition" markdown="1">

<ins id="propXX">**명제 XX**</ins> 다음 subgroup

$$T=\left\{\begin{pmatrix}e^{i\theta}&0\\0&e^{-i\theta}\end{pmatrix}\mid \theta\in\mathbb{R}/2\pi\mathbb{Z}\right\}$$

은 $SU(2)$의 maximal torus이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$T$는 diagonal matrix들의 모임이므로 abelian이고, $S^1$과 동형이므로 torus이다. Maximality를 보이기 위해, $T$를 포함하는 abelian subgroup $A$가 있다 하자. 임의의 $\begin{pmatrix}a&b\\c&d\end{pmatrix}\in A$가 $T$의 모든 원소와 commute하여야 하므로, 특히 $\begin{pmatrix}i&0\\0&-i\end{pmatrix}$와 commute해야 한다. 이로부터 $b=c=0$임을 알 수 있고, 따라서 $A\subset T$이다.

</details>

이제 Weyl group을 계산하자. $T$의 normalizer를 찾아야 한다.

<div class="proposition" markdown="1">

<ins id="propXX">**명제 XX**</ins> $N_{SU(2)}(T)$는 다음 집합

$$N_{SU(2)}(T)=T\cup \begin{pmatrix}0&1\\-1&0\end{pmatrix}T$$

이며, 따라서 $W\cong\mathbb{Z}_2$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

임의의 $g\in SU(2)$에 대하여, $gTg^{-1}=T$이려면 $g$가 $T$를 보존해야 한다. $T$의 원소들은 eigenvalue가 $\{e^{i\theta}, e^{-i\theta}\}$인 diagonalizable matrix들이다. $gTg^{-1}=T$이면 각 $t\in T$에 대하여 $gtg^{-1}$도 diagonal이어야 한다.

한편 $g=\begin{pmatrix}a&b\\-b^*&a^*\end{pmatrix}$ ($|a|^2+|b|^2=1$)로 쓰면, 계산을 통해 $g$가 $T$를 보존하는 것은 $ab=0$인 것과 동치임을 알 수 있다. 즉, $b=0$이면 $g\in T$이고, $a=0$이면 $g=\begin{pmatrix}0&b\\-b^*&0\end{pmatrix}=\begin{pmatrix}0&1\\-1&0\end{pmatrix}\begin{pmatrix}b^*&0\\0&-b\end{pmatrix}\in\begin{pmatrix}0&1\\-1&0\end{pmatrix}T$이다.

</details>

Weyl group $W\cong\mathbb{Z}_2$의 nontrivial element는 $\begin{pmatrix}0&1\\-1&0\end{pmatrix}$에 해당한다. 이 원소의 $T$ 위에서의 action을 계산하면

$$\begin{pmatrix}0&1\\-1&0\end{pmatrix}\begin{pmatrix}e^{i\theta}&0\\0&e^{-i\theta}\end{pmatrix}\begin{pmatrix}0&-1\\1&0\end{pmatrix}=\begin{pmatrix}e^{-i\theta}&0\\0&e^{i\theta}\end{pmatrix}$$

이다. 즉, Weyl group action은 $\theta\mapsto -\theta$로, torus $S^1$ 위에서의 reflection에 해당한다.

### Weight decomposition

$SU(2)$의 기본적인 representation을 생각하자. 자연스러운 representation $\rho:SU(2)\rightarrow\GL(2,\mathbb{C})$에서 각 $g\in SU(2)$는 $2\times 2$ 행렬로 작용한다. 이를 $T$로 제한하면

$$\rho\vert_T\left(\begin{pmatrix}e^{i\theta}&0\\0&e^{-i\theta}\end{pmatrix}\right)=\begin{pmatrix}e^{i\theta}&0\\0&e^{-i\theta}\end{pmatrix}$$

이므로, weight decomposition은 자명하게 $V=\mathbb{C}e_1\oplus\mathbb{C}e_2$로 주어진다. 여기서 weight들은 $\lambda_1(\theta)=\theta$, $\lambda_2(\theta)=-\theta$이다.

더 흥미로운 예시로, symmetric power $S^n(\mathbb{C}^2)$를 생각하자. 이는 $(n+1)$차원 representation으로, basis가 $e_1^n, e_1^{n-1}e_2, \ldots, e_2^n$으로 주어진다. $T$의 작용은

$$\begin{pmatrix}e^{i\theta}&0\\0&e^{-i\theta}\end{pmatrix}\cdot e_1^{n-k}e_2^k = e^{i(n-2k)\theta}e_1^{n-k}e_2^k$$

이다. 따라서 weight들은 $n, n-2, n-4, \ldots, -n$이며, 각 weight의 multiplicity는 1이다.

### Weyl group action on weights

Weyl group $W=\mathbb{Z}_2$가 weight들 위에 작용한다. Weight $\lambda(\theta)=n\theta$에 대하여, $w\cdot\lambda(\theta)=\lambda(-\theta)=-n\theta$이다. 즉, weight $n$은 $-n$으로 보내진다.

$S^n(\mathbb{C}^2)$의 경우, weight들이 $n, n-2, \ldots, -n$으로 대칭적으로 배열되어 있음을 알 수 있다. 이는 Weyl group이 weight set을 보존한다는 일반적인 사실의 구체적인 예시이다.

## Regular 원소와 Singular 원소

Maximal torus $T$의 원소를 그 "genericity"에 따라 분류할 수 있다.

<div class="definition" markdown="1">

<ins id="defXX">**정의 XX**</ins> Maximal torus $T$의 원소 $t$가 *regular*라는 것은 $wtw^{-1}=t$를 만족하는 $w\in W$가 오직 $w=e$뿐인 것이다. 반대로, $wtw^{-1}=t$인 $w\neq e$가 존재하면 $t$를 *singular*라 한다.

</div>

즉, regular 원소는 Weyl group action의 stabilizer가 자명한 원소이고, singular 원소는 비자명한 stabilizer를 갖는 원소이다.

<div class="example" markdown="1">

<ins id="exXX">**예시 XX**</ins> $SU(2)$의 경우, $T=\{\text{diag}(e^{i\theta}, e^{-i\theta})\}$이고 $W=\mathbb{Z}_2$가 $\theta\mapsto -\theta$로 작용한다. 따라서:

- **Regular:** $\theta \neq 0, \pi$인 원소들. 이들은 reflection의 fixed point가 아니다.
- **Singular:** $\theta=0$ (항등원)과 $\theta=\pi$ ($\text{diag}(-1,-1)$). 이들은 reflection에 의해 고정된다.

Torus $T\cong S^1$에서 singular 원소는 정확히 두 점이며, regular 원소들은 그 여집합이다.

</div>

일반적으로 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="propXX">**명제 XX**</ins> Compact connected Lie group $G$의 maximal torus $T$에 대하여:

1. Regular 원소들은 $T$에서 dense open subset을 이룬다.
2. Singular 원소들은 $T$에서 codimension $\geq 1$인 closed subset을 이룬다.
3. Singular 원소들의 집합은 유한 개의 subgroup들의 합집합이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

(1)과 (2): 각 $w\in W$, $w\neq e$에 대하여, fixed point set $\{t\in T: wtw^{-1}=t\}$는 $T$의 proper closed subgroup이다. Singular 원소들의 집합은 이들의 유한 합집합이므로 closed이고, 그 여집합(regular 원소들)은 dense open이다.

(3): 각 $w\neq e$에 대한 fixed point set이 $T$의 closed subgroup이고, $W$가 유한이므로 유한 개의 subgroup들의 합집합이다.

</details>

### Geometric interpretation

Singular 원소들이 $T$에서 형성하는 집합은 torus를 여러 조각으로 나눈다. $SU(2)$의 경우, singular 원소 두 점이 $S^1$을 두 개의 arc로 나눈다. 각 arc에서 Weyl group은 자유롭게 작용하며, 두 arc는 Weyl group action에 의해 서로 대응된다.

이 관점에서 보면, $T$의 regular 원소들의 quotient $T_{\text{reg}}/W$는 연결된 공간이며, 이를 *Weyl chamber*의 개념과 연결할 수 있다. $SU(2)$의 경우 $T_{\text{reg}}/W \cong (0,\pi)$는 1차원 interval이고, 이것이 바로 1차원 Weyl chamber에 해당한다.

더 일반적인 Lie group에서는 singular 원소들이 torus를 여러 chamber들로 나누고, 각 chamber는 Weyl group action의 fundamental domain 역할을 한다. 이것이 다음 글에서 다룰 root system과 Weyl chamber의 기하적 토대가 된다.
