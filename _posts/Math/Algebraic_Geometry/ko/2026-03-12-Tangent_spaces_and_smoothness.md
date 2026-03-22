---
title: "접공간과 매끄러움"
excerpt: "Tangent spaces and smoothness of algebraic varieties"

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/tangent_spaces_and_smoothness
sidebar: 
    nav: "algebraic_geometry-ko"

header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Tangent_Spaces.png
    overlay_filter: 0.5

date: 2026-03-12
last_modified_at: 2026-03-22
weight: 6

---

미분기하학에서와 마찬가지로 대수기하학에서도 접공간은 다양체의 국소적 구조를 이해하는 핵심 도구이다.

## 접공간의 정의

미분기하학에서 우리는 $$M$$ 위에 정의된 smooth function들의 sheaf $$\mathcal{C}^\infty_M$$에 대하여, 점 $$p\in M$$에서 vanish하는 모든 germ들의 모임

$$\mathfrak{m}_p=\{\mathbf{f}\in \mathcal{C}^\infty_p\mid \mathbf{f}(p)=0\}$$

이 maximal ideal임을 확인하였다. 그 후 우리는 tangent space를 

$$(\mathfrak{m}_p/\mathfrak{m}_p^2)^\ast$$

로 볼 수 있다는 것을 증명하였다. ([\[미분다양체\] §여접공간, ⁋보조정리 1](/ko/math/manifold/cotangent_space#lem1)) 이 과정은 보통 미분기하학에서는 잘 다루지 않으나, algebraic variety로의 일반화에 큰 도움을 준다. 즉, (편의상 affine case로 고정한다면) 우리는 이미 algebraic variety들 위에 정의된 함수가 무엇인지 알고 ([§준사영다양체, ⁋정의 7](/ko/math/algebraic_geometry/quasi_projective_varieties#def7)), 이 때 $$x\in X$$에서 vanish하는 모든 함수들의 모임은 이 점에 해당되는 $$\mathbb{K}[X]$$의 maximal ideal에 해당한다는 것도 안다. 따라서 이를

$$\mathfrak{m}_x=\{f\in \mathbb{K}[X]\mid f(x)=0\}$$

으로 정의하고, $$\mathbb{K}[X]$$의 이 maximal ideal에서의 localization $$\mathbb{K}[X]_{\mathfrak{m}_x}=\mathcal{O}_{X,x}$$을 생각할 수 있다. ([\[가환대수학\] §국소화, ⁋정의 1](/ko/math/commutative_algebra/localization#def1)) 기하적으로는 [§아핀다양체, ⁋정의 14](/ko/math/algebraic_geometry/affine_varieties#def14)를 생각하면 이들은 점 $$x$$에서의 regular function들의 germ으로 정의할 수 있다. 

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Variety $$X$$의 점 $$p$$에서의 *Zariski tangent space<sub>Zariski 접공간</sub>* $$T_x X$$를

$$T_x X = (\mathfrak{m}_x / \mathfrak{m}_x^2)^\ast$$

으로 정의한다. 여기서 $$\mathfrak{m}_x$$는 점 $$x$$에서의 local ring $$\mathcal{O}_{X,x}$$의 유일한 maximal ideal이다. 

</div>

결국 이 정의의 핵심은, quotient $$\mathfrak{m}_x / \mathfrak{m}_x^2$$는 $$x$$에서의 first-order infinitesimal data를 담고 있으므로 이를 *Zariski cotangent space* $$T_x^\ast X$$로 정의하겠다는 것이다. 그리고 dual인 $$T_x X$$는 이 data에 작용하는 linear functional들, 즉 방향미분연산자들의 공간이며, 이 정의는 $$T_xX=\Der_\mathbb{K}(\mathscr{O}_{X,x}, \mathbb{K})$$으로 정의하는 것과 맞아떨어진다. 

우리는 해석학 스타일의 $$\epsilon$$-$$\delta$$ 꼴의 미분을 사용하지는 않으나, 본질적으로 variety들은 다항식으로 정의되며 이들의 미분은 형식적으로 $$\x^n$$을 미분하면 $$n\cdot \x^{n-1}$$이 나오는 것으로 생각할 수 있다. 특히 affine variety의 경우 이는 더 명확하게 써 줄 수 있다. 

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> 아핀다양체 $$X = V(f_1, \ldots, f_k) \subseteq \mathbb{A}^n$$의 점 $$p = (p_1, \ldots, p_n)$$에서,

$$T_p X \cong \{v \in \mathbb{K}^n \mid (df_i)_p(v) = 0 \text{ for all } i\}$$

이다. 여기서 $$(df_i)_p$$는 $$f_i$$의 $$p$$에서의 differential로,

$$(df_i)_p(v) = \sum_{j=1}^n \frac{\partial f_i}{\partial x_j}(p) v_j$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$X$$의 coordinate ring $$\mathbb{K}[X] = \mathbb{K}[x_1, \ldots, x_n] / (f_1, \ldots, f_k)$$를 생각하자. $$\mathfrak{m}_x = (x_1 - x_1, \ldots, x_n - x_n) / (f_1, \ldots, f_k)$$이므로,

$$\mathfrak{m}_x / \mathfrak{m}_x^2 \cong (x_1 - x_1, \ldots, x_n - x_n) / \left( (x_1 - x_1, \ldots, x_n - x_n)^2 + (f_1, \ldots, f_k) \right)$$

이다. 각 $$f_i$$를 $$x$$에서 Taylor 전개하면

$$f_i = \sum_{j=1}^n \frac{\partial f_i}{\partial x_j}(x) (x_j - x_j) + \text{higher order terms}$$

이고, higher order terms는 $$(x_1 - x_1, \ldots, x_n - x_n)^2$$에 속한다. 따라서 $$\mathfrak{m}_x / \mathfrak{m}_x^2$$에서 $$f_i$$들의 linear part $$\sum_j \frac{\partial f_i}{\partial x_j}(x) (x_j - x_j)$$가 0이 된다.

한편, $$\mathfrak{m}_x / \mathfrak{m}_x^2$$는 $$x_j - x_j$$들의 linear combination으로 생성되므로 $$\mathbb{K}^n$$의 quotient로 볼 수 있다. 이때 differential $$(df_i)_x$$의 kernel이 정확히 $$\mathfrak{m}_x / \mathfrak{m}_x^2$$에서 사라지는 방향들에 해당한다. Dual을 취하면

$$T_x X = (\mathfrak{m}_x / \mathfrak{m}_x^2)^\ast \cong \{v \in \mathbb{K}^n \mid (df_i)_x(v) = 0 \text{ for all } i\}$$

을 얻는다.

</details>

이 명제는 접공간을 기하학적으로 이해하게 해준다. $$T_p X$$는 $$p$$를 지나면서 $$X$$에 "접하는" 모든 직선들의 모임이다. 점 $$p + \epsilon v$$가 $$X$$ 위에 있다면 ($$\epsilon$$이 매우 작을 때), $$v \in T_p X$$이다. 이는 $$f_i(p + \epsilon v) \approx f_i(p) + \epsilon (df_i)_p(v) = \epsilon (df_i)_p(v)$$이고, $$f_i(p) = 0$$이므로 $$(df_i)_p(v) = 0$$이어야 하기 때문이다. 즉, 접공간은 다양체 위를 "이동"할 수 있는 방향들의 집합이다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> $$T_p X$$는 $$\mathbb{K}$$-벡터공간이며, 그 차원은 $$n - \operatorname{rank}(J_p)$$이다. 여기서 $$J_p$$는 $$k \times n$$ Jacobian matrix

$$J_p = \left(\frac{\partial f_i}{\partial x_j}(p)\right)_{1 \le i \le k, 1 \le j \le n}$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

각 $$(df_i)_p: \mathbb{K}^n \to \mathbb{K}$$는 linear functional이다. [명제 2](#prop2)에서 $$T_p X$$는 이들의 kernel들의 교집합이므로 $$\mathbb{K}^n$$의 부분공간이다. Jacobian matrix $$J_p$$의 행들은 이 linear functional들의 좌표표현이므로,

$$T_p X = \ker(J_p) = \{v \in \mathbb{K}^n \mid J_p v = 0\}$$

이다. Rank-nullity theorem에 의해 $$\dim T_p X = n - \operatorname{rank}(J_p)$$이다.

</details>

이 명제는 접공간의 차원을 계산하는 실용적인 방법을 제공한다. Jacobian matrix의 rank가 높을수록 (즉, 더 많은 independent constraint가 있을수록) 접공간의 차원이 낮아진다. 이는 "더 많은 제약 = 더 작은 접공간"이라는 직관과 일치한다.

## 매끄러운 점과 특이점

접공간의 차원은 항상 다양체의 차원 이상이다. 특이점에서는 접공간이 "너무 커서" 다양체의 차원보다 크다. 이는 특이점에서 다양체가 "여러 방향으로 갈라지거나" "뾰족하게 끝나서" 접공간이 예상보다 커진다는 것을 의미한다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> Irreducible variety $$X$$의 임의의 점 $$p$$에 대해 $$\dim T_p X \ge \dim X$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$X = V(f_1, \ldots, f_k) \subseteq \mathbb{A}^n$$이 irreducible하고 $$\dim X = d$$라 하자. 구체적으로, $$\dim X = d$$라는 것은 $$X$$가 "본질적으로 $$d$$개의 독립적인 변수"로 기술될 수 있음을 의미한다. 예를 들어, 평면 위의 곡선은 1개의 매개변수로 기술되므로 차원이 1이고, 공간 위의 곡면은 2개의 매개변수가 필요하므로 차원이 2이다. 일반적으로, $$X \subseteq \mathbb{A}^n$$에서 $$n-d$$개의 defining equation은 $$d$$개의 "자유로운 방향"만 남긴다.

이제 irreducibility가 핵심적으로 작용한다. Irreducible variety $$X$$의 coordinate ring $$\mathbb{K}[X]$$ 위에서는, 서로 다른 정칙함수들 사이에 대수적 관계가 존재하여, 임의의 점에서 Jacobian matrix $$J_p$$의 행들이 서로 선형종속이 될 수밖에 없다. Krull의 Hauptidealsatz에 따르면, irreducible variety에서의 정칙함수 한 개는 차원을 정확히 1 감소시킨다. 따라서 $$k$$개의 defining equation의 "유효 rank"는 $$X$$의 차원을 $$n-d$$로 줄이는 데 필요한 수, 즉 $$n-d$$를 넘을 수 없다. 즉, 모든 점 $$p$$에서

$$\operatorname{rank}(J_p) \le n - d$$

이고, $$\dim T_p X = n - \operatorname{rank}(J_p) \ge d = \dim X$$이다. 차원의 엄밀한 정의와 이에 대한 완전한 증명은 차원 이론에서 다루게 된다.

</details>

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> 점 $$p \in X$$가 *smooth point<sub>매끄러운 점</sub>* (또는 *nonsingular point*)라는 것은 $$\dim T_p X = \dim X$$인 것이다. 그렇지 않으면 (즉, $$\dim T_p X > \dim X$$이면) *singular point<sub>특이점</sub>*이라 부른다.

</div>

<div class="example" markdown="1">

<ins id="ex6">**예시 6**</ins> Smooth point와 singular point의 기본 예시들이다.

1. $$\mathbb{A}^n$$의 모든 점은 smooth point이다. $$\mathbb{A}^n$$은 defining equation이 없으므로 $$T_p \mathbb{A}^n = \mathbb{K}^n$$이고, $$\dim T_p \mathbb{A}^n = n = \dim \mathbb{A}^n$$이다. 이는 affine space가 "가장 간단한" 매끄러운 다양체임을 보여준다.
2. Parabola $$V(\y - \x^2)$$의 모든 점은 smooth point이다. $$f = \y - \x^2$$에 대해 $$\nabla f = (-2x, 1)$$이고, 이는 모든 점에서 nonzero이다. 따라서 $$\dim T_p X = 2 - 1 = 1 = \dim X$$이다. 이는 parabola가 어디서나 "매끄럽게" 휘어있음을 보여준다.
3. **Cusp** $$V(\y^2 - \x^3)$$의 원점은 singular point이다. $$f = \y^2 - \x^3$$에 대해 $$\nabla f = (-3x^2, 2y)$$이고, 원점에서 $$\nabla f(0,0) = (0, 0)$$이다. 따라서 $$T_0 X = \mathbb{K}^2$$이고 $$\dim T_0 X = 2 > 1 = \dim X$$이다. 기하학적으로, 접공간이 2차원이라는 것은 원점에서 모든 방향이 "접한다"는 것을 의미하며, 이는 곡선이 너무 뾰족해서 어떤 방향으로도 접선을 정의할 수 없음을 나타낸다. Cusp는 "가장 극단적인" 특이점 중 하나이다.

</div>

<div class="example" markdown="1">

<ins id="ex7">**예시 7**</ins> **Node**: $$X = V(\y^2 - \x^2(\x+1)) \subset \mathbb{A}^2$$를 생각하자. 이 곡선은 원점에서 두 갈래로 갈라진다. 원점에서의 Jacobian은

$$J_0 = \begin{pmatrix} -2x - 3x^2 & 2y \end{pmatrix}_{(0,0)} = \begin{pmatrix} 0 & 0 \end{pmatrix}$$

이므로 원점은 singular point이다. 기하학적으로, 접공간이 2차원이라는 것은 두 갈래의 접선 방향이 모두 포함된다는 것을 의미한다. 구체적으로, $$\y^2 - \x^2(\x+1) \approx \y^2 - \x^2 = (\y-\x)(\y+\x)$$이므로, 원점 근처에서 곡선은 $$\y = \x$$와 $$\y = -\x$$ 두 직선의 합집합처럼 보인다. Node는 "가장 온화한" 특이점 중 하나이다.

</div>

## Jacobian Criterion

Jacobian criterion은 smooth point를 효율적으로 판별하는 방법이다. 이는 접공간의 차원을 Jacobian matrix의 rank로 계산할 수 있다는 사실을 이용한다.

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> (Jacobian Criterion) $$X = V(f_1, \ldots, f_k) \subseteq \mathbb{A}^n$$이 irreducible하고 $$x \in X$$라 하자. 그럼 $$x$$가 smooth point일 필요충분조건은 Jacobian matrix $$J_x$$의 rank가 $$n - \dim X$$인 것이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

[명제 2](#prop2)에서 $$\dim T_x X = n - \operatorname{rank}(J_x)$$임을 보였다. [정의 5](#def5)에서 $$x$$가 smooth point라는 것은 $$\dim T_x X = \dim X$$인 것이다. 따라서 $$x$$가 smooth point일 필요충분조건은

$$n - \operatorname{rank}(J_x) = \dim X$$

즉, $$\operatorname{rank}(J_x) = n - \dim X$$인 것이다.

</details>

이 정리는 smooth point를 판별하는 실용적인 방법을 제공한다. $$X = V(f_1, \ldots, f_k)$$이고 $$\dim X = d$$라면, $$p$$가 smooth point이려면 $$J_p$$의 rank가 정확히 $$n - d$$이어야 한다. 이는 $$k$$개의 defining equation 중 정확히 $$n - d$$개가 $$p$$에서 "독립적"이어야 함을 의미한다. 만약 더 많은 equation이 독립적이면 (rank가 더 높으면), 접공간이 너무 작아지고, 더 적으면 (rank가 더 낮으면), 접공간이 너무 커진다.

<div class="misc" markdown="1">

Jacobian criterion을 적용하려면 $$X$$의 차원을 미리 알아야 한다. 차원을 모르는 경우, $$J_x$$의 rank의 최댓값을 $$r$$이라 하면 $$\dim X \ge n - r$$이고, $$x$$가 smooth point이면 $$\dim X = n - r$$이다. 이는 차원을 계산하는 한 가지 방법을 제공한다.

</div>

## 매끄러운 점들의 존재

Irreducible variety는 "대부분의 점에서" 매끄럽다. 이는 대수기하학의 기본 정리 중 하나이며, 대수다양체가 "잘 작동한다"는 것을 보여준다.

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> Irreducible variety $$X$$의 smooth points들의 집합 $$X_{\text{sm}}$$은 $$X$$의 dense open subset이다. 특히, $$X_{\text{sm}} \ne \emptyset$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$X = V(f_1, \ldots, f_k) \subseteq \mathbb{A}^n$$이 irreducible하고 $$\dim X = d$$라 하자. [명제 8](#prop8)의 Jacobian criterion에 의해,

$$X_{\text{sm}} = \{p \in X \mid \operatorname{rank}(J_p) = n - d\}$$

이다. 이제 이 집합이 dense open subset임을 보인다.

**(1) $$X_{\text{sm}}$$이 열린집합:** Rank가 정확히 $$n-d$$라는 것은 두 조건의 동시 성립을 의미한다. 첫째, rank가 $$n-d$$ *이상*이라는 것은, 어떤 $$(n-d) \times (n-d)$$ 부분행렬의 행렬식이 0이 아닌 것과 동치이고, 이는 Zariski 위상에서 열린조건이다. 둘째, rank가 $$n-d$$ *이하*라는 것은, 모든 $$(n-d+1) \times (n-d+1)$$ 부분행렬의 행렬식이 0인 것과 동치이고, 이는 닫힌조건이다. 따라서 rank가 정확히 $$n-d$$인 점들의 집합은 열린조건과 닫힌조건의 교집합으로, $$X$$의 부분공간 위상에서 열린집합이다.

**(2) $$X_{\text{sm}} \ne \emptyset$$:** [명제 4](#prop4)에서 보였듯이, irreducible variety $$X$$에서 Jacobian $$J_p$$의 rank는 모든 점에서 $$n - d$$를 넘을 수 없다. 이제 이 상한이 실제로 달성됨을 보여야 한다. $$J_p$$의 rank가 모든 점에서 $$n - d$$ 미만이라면, $$\dim T_p X = n - \operatorname{rank}(J_p) > d$$가 모든 점에서 성립하여 $$X$$의 차원이 $$d$$라는 것과 모순된다. (구체적으로, Krull의 Hauptidealsatz에 의해 $$X$$의 generic point[^1]에서는 $$J_p$$의 rank가 정확히 $$n-d$$에 도달하며, rank가 최댓값에 도달하는 점들의 집합은 $$X$$의 비어있지 않은 Zariski 열린집합이다.) 따라서 $$X_{\text{sm}} \ne \emptyset$$이다.

**(3) $$X_{\text{sm}}$$이 조밀하다:** $$X$$는 irreducible하므로, $$X$$의 임의의 비어있지 않은 열린집합은 $$X$$에서 조밀하다. (1)에서 $$X_{\text{sm}}$$이 열린집합이고, (2)에서 비어있지 않으므로, $$X_{\text{sm}}$$은 $$X$$의 dense open subset이다.

</details>

<div class="definition" markdown="1">

<ins id="def10">**정의 10**</ins> 다양체 $$X$$가 *smooth* (또는 *nonsingular*)라는 것은 모든 점이 smooth point인 것이다. 즉, $$X_{\text{sm}} = X$$이다. 그렇지 않으면 (즉, singular point가 존재하면) *singular*라 부른다.

</div>

<div class="example" markdown="1">

<ins id="ex11">**예시 11**</ins> Smooth variety와 singular variety의 예시들이다.

1. $$\mathbb{A}^n$$과 $$\mathbb{P}^n$$은 smooth하다. 이들의 모든 점에서 접공간의 차원이 $$n$$으로 일치한다. 이는 "가장 기본적인" 매끄러운 다양체들이다.
2. Parabola $$V(\y - \x^2)$$는 smooth하다. 모든 점에서 $$\nabla(\y - \x^2) \ne 0$$이다. 이는 모든 conic(2차 다항식으로 정의되는 사영평면 위의 곡선)이 smooth임의 특별한 경우이다.
3. Cusp $$V(\y^2 - \x^3)$$은 singular이다. 원점이 singular point이다. 이는 "가장 극단적인" 특이점의 예시이다.
4. Node $$V(\y^2 - \x^2(\x+1))$$은 singular이다. 원점이 singular point이다. 이는 "가장 온화한" 특이점의 예시이다.
5. Smooth projective curve는 모든 점에서 매끄러운 1차원 사영다양체이다. 예를 들어 smooth plane curve $$V(F) \subset \mathbb{P}^2$$ ($$F$$가 irreducible 동차다항식)는 모든 점 $$p$$에서 $$\nabla F(p) \ne 0$$이면 smooth하다. 이는 대수기하학에서 가장 중요한 다양체들 중 하나이다.

</div>

## 접원뿔

Singular point에서는 tangent space가 너무 커서 다양체의 국소적 구조를 정확히 반영하지 못한다. 이 경우 *tangent cone*이 더 정확한 정보를 제공한다. 접선들의 방향만 남기고 "길이" 정보를 없애면, singular point에서도 의미 있는 기하학적 정보를 얻을 수 있다. Tangent cone은 다양체를 singular point에서 "무한히 확대"하여 가장 낮은 차수의 항만 남긴 것이다.

<div class="definition" markdown="1">

<ins id="def12">**정의 12**</ins> 점 $$p \in X$$에서의 *tangent cone* $$TC_p X$$는 $$p$$에서의 initial ideal로 정의되는 cone이다. 구체적으로, $$X = V(f_1, \ldots, f_k)$$이고 각 $$f_i$$를 $$p$$에서 전개하면

$$f_i = f_i^{(d_i)} + \text{higher order terms}$$

이고, 여기서 $$f_i^{(d_i)}$$는 $$f_i$$의 lowest degree homogeneous part (initial form)이다. 그럼

$$TC_p X = V(f_1^{(d_1)}, \ldots, f_k^{(d_k)})$$

이다.

</div>

Tangent cone은 다양체를 점 $$x$$에서 "확대"하여 가장 낮은 차수의 항만 남긴 것이다. Smooth point에서는 tangent cone이 tangent space와 같다. Singular point에서는 tangent cone이 tangent space보다 더 정확한 정보를 준다. 이는 tangent cone이 "가장 낮은 차수의 근사"를 제공하기 때문이다.

<div class="example" markdown="1">

<ins id="ex13">**예시 13**</ins> **Cusp의 tangent cone**: [예시 6(3)](#ex6)의 곡선 $$X = V(\y^2 - \x^3)$$에서, $$f$$의 lowest degree term은 $$\y^2$$이므로

$$TC_0 X = V(\y^2)$$

이다. 이는 $$\y = 0$$ 직선을 "두 번" count한 것이며, cusp가 $$\x$$-축 방향으로 뾰족하게 끝남을 보여준다. 비교하면, tangent space $$T_0 X = \mathbb{K}^2$$는 모든 방향을 포함하여 너무 크다.

</div>

<div class="example" markdown="1">

<ins id="ex14">**예시 14**</ins> **Node의 tangent cone**: [예시 7](#ex7)의 곡선 $$X = V(\y^2 - \x^2(\x+1))$$에서, $$f$$의 lowest degree term은 $$\y^2 - \x^2 = (\y-\x)(\y+\x)$$이므로

$$TC_0 X = V(\y-\x) \cup V(\y+\x)$$

이다. 이는 node가 두 직선 $$\y = \x$$와 $$\y = -\x$$의 방향으로 갈라짐을 정확히 보여준다.

</div>

Tangent cone은 특이점 분류와 국소적 구조 이해에 핵심적인 도구이다. Cusp의 tangent cone은 "double line"이고 node의 tangent cone은 "two lines"으로, tangent cone의 구조만으로 특이점의 종류를 구별할 수 있다. 또한 tangent cone은 유리사상 ([§유리사상](/ko/math/algebraic_geometry/rational_maps))에서 다루는 blow-up의 exceptional divisor와 밀접한 관계가 있어, 특이점 해소 이론의 기초가 된다. 마지막으로, tangent cone은 singular point 근처에서 다양체가 어떻게 생겼는지에 대한 정보를 제공한다.

---

[^1]: 스킴 이론에서 다양체의 가장 일반적인 점을 나타내는 개념. 여기서는 직관적으로 "일반적인 위치의 점"으로 이해하면 된다.

---

**참고문헌**

**[Har]** J. Harris, *Algebraic Geometry: A First Course*, Springer, 1992.  
**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.
