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

미분기하학에서 우리는 $$M$$ 위에 정의된 smooth function들의 sheaf $$\mathcal{C}^\infty_M$$에 대하여, 점 $$x\in M$$에서 vanish하는 모든 germ들의 모임

$$\mathfrak{m}_x=\{\mathbf{f}\in \mathcal{C}^\infty_x\mid \mathbf{f}(x)=0\}$$

이 maximal ideal임을 확인하였다. 그 후 우리는 tangent space를

$$(\mathfrak{m}_x/\mathfrak{m}_x^2)^\ast$$

로 볼 수 있다는 것을 증명하였다. ([\[미분다양체\] §여접공간, ⁋보조정리 1](/ko/math/manifold/cotangent_space#lem1)) 이 과정은 보통 미분기하학에서는 잘 다루지 않으나, algebraic variety로의 일반화에 큰 도움을 준다. 즉, (편의상 affine case로 고정한다면) 우리는 이미 algebraic variety들 위에 정의된 함수가 무엇인지 알고 ([§준사영다양체, ⁋정의 7](/ko/math/algebraic_geometry/quasi_projective_varieties#def7)), 이 때 $$x\in X$$에서 vanish하는 모든 함수들의 모임은 이 점에 해당되는 $$\mathbb{K}[X]$$의 maximal ideal에 해당한다는 것도 안다. 따라서 이를

$$\mathfrak{m}_x=\{f\in \mathbb{K}[X]\mid f(x)=0\}$$

으로 정의하고, $$\mathbb{K}[X]$$의 이 maximal ideal에서의 localization $$\mathbb{K}[X]_{\mathfrak{m}_x}=\mathcal{O}_{X,x}$$을 생각할 수 있다. ([\[가환대수학\] §국소화, ⁋정의 1](/ko/math/commutative_algebra/localization#def1)) 기하적으로는 [§아핀다양체, ⁋정의 14](/ko/math/algebraic_geometry/affine_varieties#def14)를 생각하면 이들은 점 $$x$$에서의 regular function들의 germ으로 정의할 수 있다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Variety $$X$$의 점 $$x$$에서의 *Zariski tangent space<sub>Zariski 접공간</sub>* $$T_x X$$를

$$T_x X = (\mathfrak{m}_x / \mathfrak{m}_x^2)^\ast$$

으로 정의한다. 여기서 $$\mathfrak{m}_x$$는 점 $$x$$에서의 local ring $$\mathcal{O}_{X,x}$$의 유일한 maximal ideal이다.

</div>

결국 이 정의의 핵심은, quotient $$\mathfrak{m}_x / \mathfrak{m}_x^2$$는 $$x$$에서의 first-order infinitesimal data를 담고 있으므로 이를 *Zariski cotangent space* $$T_x^\ast X$$로 정의하겠다는 것이다. 그리고 dual인 $$T_x X$$는 이 data에 작용하는 linear functional들, 즉 방향미분연산자들의 공간이며, 이 정의는 $$T_xX=\Der_\mathbb{K}(\mathcal{O}_{X,x}, \mathbb{K})$$으로 정의하는 것과 맞아떨어진다.

우리는 해석학 스타일의 $$\epsilon$$-$$\delta$$ 꼴의 미분을 사용하지는 않으나, 본질적으로 variety들은 다항식으로 정의되며 이들의 미분은 형식적으로 $$\x^n$$을 미분하면 $$n\cdot \x^{n-1}$$이 나오는 것으로 생각할 수 있다. 특히 affine variety의 경우 이는 더 명확하게 써 줄 수 있다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> Affine variety $$X = Z(f_1, \ldots, f_k) \subseteq \mathbb{A}^n$$의 점 $$x = (x_1, \ldots, x_n)$$에서,

$$T_x X \cong \{v \in \mathbb{K}^n \mid (df_i)_x(v) = 0 \text{ for all } i\}$$

이다. 여기서 $$(df_i)_x$$는 $$f_i$$의 $$x$$에서의 differential로,

$$(df_i)_x(v) = \sum_{j=1}^n \frac{\partial f_i}{\partial \x_j}(x) v_j$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$X$$의 coordinate ring $$\mathbb{K}[X] = \mathbb{K}[\x_1, \ldots, \x_n] / (f_1, \ldots, f_k)$$를 생각하자. $$\mathfrak{m}_x = (\x_1 - a_1, \x_2 - a_2, \ldots, \x_n - a_n) / (f_1, \ldots, f_k)$$이므로,

$$\mathfrak{m}_x / \mathfrak{m}_x^2 \cong (\x_1 - a_1, \x_2 - a_2, \ldots, \x_n - a_n) / \left( (\x_1 - a_1, \x_2 - a_2, \ldots, \x_n - a_n)^2 + (f_1, \ldots, f_k) \right)$$

이다. 각 $$f_i$$를 $$x$$에서 Taylor 전개하면

$$f_i = \sum_{j=1}^n \frac{\partial f_i}{\partial \x_j}(x) (\x_j - a_j) + \text{higher order terms}$$

이고, higher order terms는 $$(\x_1 - a_1, \x_2 - a_2, \ldots, \x_n - a_n)^2$$에 속한다. 따라서 $$\mathfrak{m}_x / \mathfrak{m}_x^2$$에서 $$f_i$$들의 linear part $$\sum_j \frac{\partial f_i}{\partial \x_j}(x) (\x_j - a_j)$$가 0이 된다.

한편, $$\mathfrak{m}_x / \mathfrak{m}_x^2$$는 $$\x_j - a_j$$들의 linear combination으로 생성되므로 $$\mathbb{K}^n$$의 quotient로 볼 수 있다. 이때 differential $$(df_i)_x$$의 kernel이 정확히 $$\mathfrak{m}_x / \mathfrak{m}_x^2$$에서 사라지는 방향들에 해당한다. Dual을 취하면

$$T_x X = (\mathfrak{m}_x / \mathfrak{m}_x^2)^\ast \cong \{v \in \mathbb{K}^n \mid (df_i)_x(v) = 0 \text{ for all } i\}$$

을 얻는다.

</details>

증명은 maximal ideal의 언어를 사용하며 복잡하게 쓰여졌지만, 그 철학은 $$X=Z(f_i)$$에 대해 생각해보면 간단하다. 이 경우 $$(df_i)_x(v)=0$$은 ($$\mathbb{K}^n$$을 $$\mathbb{A}^n$$으로 본다면) 정확히 $$\mathbb{A}^n$$ 안에서 초곡면 $$Z(f_i)$$의 (일상적인) 접공간이다. [명제 2](#prop2)은 그 자체만으로는 affine variety에 대해서만 적용되는 것이기는 하지만, 임의의 variety $$X$$의 임의의 점 $$x$$는 affine neighborhood를 가지므로 본질적으로는 모든 variety에 대해 적용되는 것이다. 접공간의 차원에 대한 다음 명제 또한 마찬가지다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> $$T_x X$$는 $$\mathbb{K}$$-벡터공간이며, 그 차원은 $$n - \operatorname{rank}(J_x)$$이다. 여기서 $$J_x$$는 $$k \times n$$ Jacobian matrix

$$J_x = \left(\frac{\partial f_i}{\partial \x_j}(x)\right)_{1 \le i \le k, 1 \le j \le n}$$

이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

각 $$(df_i)_x: \mathbb{K}^n \to \mathbb{K}$$는 linear functional이다. [명제 2](#prop2)에서 $$T_x X$$는 이들의 kernel들의 교집합이므로 $$\mathbb{K}^n$$의 부분공간이다. Jacobian matrix $$J_x$$의 행들은 이 linear functional들의 좌표표현이므로,

$$T_x X = \ker(J_x) = \{v \in \mathbb{K}^n \mid J_x v = 0\}$$

이다. Rank-nullity theorem에 의해 $$\dim T_x X = n - \operatorname{rank}(J_x)$$이다.

</details>

## 매끄러운 점과 특이점

미분기하학에서, 임의의 점에서의 tangent space의 차원은 항상 manifold의 차원과 같았다. 그러나 이는 manifold의 정의가 다소 빡빡하기 때문으로, 대수기하학에서는 단 하나의 다항식으로 정의되는 affine variety마저 (고전적인 그림에서) manifold가 아닐 수 있다. ([예시 6](#ex6), [예시 7](#ex7)) 그럼에도 불구하고, tangent space의 차원과 variety의 차원이 아무런 관계가 없는 것은 아니다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> Irreducible variety $$X$$의 임의의 점 $$x$$에 대해 $$\dim T_x X \ge \dim X$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Affine case만 보인다. $$X = Z(f_1, \ldots, f_k) \subseteq \mathbb{A}^n$$이 irreducible하고 $$\dim X = d$$라 하자. 점 $$x \in X$$에서의 local ring $$\mathcal{O}_{X,x} = \mathbb{K}[X]_{\mathfrak{m}_x}$$를 생각하자. Localization은 차원을 보존하므로 $$\dim \mathcal{O}_{X,x} = \dim X = d$$이다. ([\[대수기하학\] §차원, ⁋명제 2](/ko/math/algebraic_geometry/dimension#prop2))

일반적으로 Noetherian local ring $$(R, \mathfrak{m})$$에 대하여 $$\dim_{\mathbb{K}}(\mathfrak{m}/\mathfrak{m}^2) \ge \dim R$$이다. ([\[가환대수학\] §매개계, ⁋명제 2](/ko/math/commutative_algebra/system_of_parameters#prop2)) 따라서

$$\dim T_x X = \dim_{\mathbb{K}}(\mathfrak{m}_x/\mathfrak{m}_x^2) \ge \dim \mathcal{O}_{X,x} = d = \dim X$$

이다.

</details>

우리의 직관을 키우기 위해서는 언제 부등식이 성립하는지를 살펴보는 것이 좋다. 이러한 점을 우리는 singular point라 부른다.

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> 점 $$x \in X$$가 *smooth point<sub>매끄러운 점</sub>* (또는 *nonsingular point*)라는 것은 $$\dim T_x X = \dim X$$인 것이다. 그렇지 않으면 (즉, $$\dim T_x X > \dim X$$이면) *singular point<sub>특이점</sub>*이라 부른다.

</div>

<div class="example" markdown="1">

<ins id="ex6">**예시 6 (Smooth points)**</ins>

1. $$\mathbb{A}^n$$의 모든 점은 smooth point이다. $$\mathbb{A}^n$$은 defining equation이 없으므로 $$T_x \mathbb{A}^n = \mathbb{K}^n$$이고, $$\dim T_x \mathbb{A}^n = n = \dim \mathbb{A}^n$$이다.
2. Parabola $$Z(\y - \x^2)$$의 모든 점은 smooth point이다. $$f = \y - \x^2$$에 대해 $$J_{(x,y)} = (-2x, 1)$$이고, 이는 모든 점에서 nonzero이다. 따라서 $$\dim T_x X = 2 - 1 = 1 = \dim X$$이다.

</div>

<div class="example" markdown="1">

<ins id="ex7">**예시 7 (Singular points)**</ins>

1. (Node) $$X = Z(\y^2 - \x^2(\x+1)) \subset \mathbb{A}^2$$를 생각하자. 이 곡선은 원점에서 두 갈래로 갈라진다.

    ![nodal_curve](/assets/images/Math/Algebraic_Geometry/Tangent_spaces_and_smoothness-1.png){:style="width:20em" class="invert" .align-center}

    이 곡선의 Jacobian은

    $$J_{(x,y)} = \begin{pmatrix} -2x - 3x^2 & 2y \end{pmatrix}$$

    이므로, 원점에서 Jacobian은 $$(0,0)$$이고, 따라서 [명제 3](#prop3)에 의해 원점은 singular point이다. 기하학적으로, 접공간이 2차원이라는 것은 두 갈래의 접선 방향이 모두 포함된다는 것을 의미한다. 구체적으로, $$\y^2 - \x^2(\x+1) \approx \y^2 - \x^2 = (\y-\x)(\y+\x)$$이므로, 원점 근처에서 곡선은 $$\y = \x$$와 $$\y = -\x$$ 두 직선의 합집합처럼 보인다. Node는 "가장 온화한" 특이점 중 하나이다.
2. (Cusp) 이번에는 $$Z(\y^2 - \x^3)\subset \mathbb{A}^2$$를 생각하자.

    ![cusp](/assets/images/Math/Algebraic_Geometry/Tangent_spaces_and_smoothness-2.png){:style="width:20em" class="invert" .align-center}

    이 때, 이 곡선의 원점은 singular point이다. 이를 확인하기 위해 Jacobian을 계산하면,

    $$J_{(x,y)}=\begin{pmatrix}-3x^2&2y\end{pmatrix}$$

    이므로 원점에서 $$\nabla f(0,0) = (0, 0)$$이다. 기하학적으로, 이 상황에서 접공간이 2차원이라는 것은 원점에서 모든 방향이 "접한다"는 것을 의미하며, 이는 곡선이 너무 뾰족해서 어떤 방향으로도 접선을 정의할 수 없음을 나타낸다.

</div>

위의 예시들에서 우리는 다음 명제를 자연스럽게 이용했다.

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> (Jacobian Criterion) $$X = Z(f_1, \ldots, f_k) \subseteq \mathbb{A}^n$$이 irreducible하고 $$x \in X$$라 하자. 그럼 $$x$$가 smooth point일 필요충분조건은 Jacobian matrix $$J_x$$의 rank가 $$n - \dim X$$인 것이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

[명제 2](#prop2)에서 $$\dim T_x X = n - \operatorname{rank}(J_x)$$임을 보였다. [정의 5](#def5)에서 $$x$$가 smooth point라는 것은 $$\dim T_x X = \dim X$$인 것이다. 따라서 $$x$$가 smooth point일 필요충분조건은

$$n - \operatorname{rank}(J_x) = \dim X$$

즉, $$\operatorname{rank}(J_x) = n - \dim X$$인 것이다.

</details>

## 매끄러운 점들의 존재

임의의 algebraic variety는 대부분의 점에서 매끄럽다. 이를 보이기 위해 *generic point*의 개념이 필요하다.

<div class="definition" markdown="1">

<ins id="def9">**정의 9**</ins> Irreducible variety $$X$$의 *generic point<sub>일반점</sub>* $$\eta$$는 $$X$$의 모든 nonempty open subset에 속하는 유일한 점이다.

</div>

Affine case $$X = \operatorname{Spec} A$$에서, $$\eta$$는 $$A$$의 minimal prime ideal (즉, $$(0)$$ ideal)에 해당하며, local ring $$\mathcal{O}_{X,\eta}$$는 정확히 function field $$\mathbb{K}(X) = \operatorname{Frac}(A)$$이다. 기하학적으로, generic point는 $$X$$의 "가장 일반적인 점"으로, $$X$$의 어떤 특정한 성질도 갖지 않는 점으로 생각하면 된다. 이러한 아이디어를 다음 증명에서 활용할 수 있다. 

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10**</ins> Variety $$X$$의 smooth points들의 집합 $$X_\sm$$은 $$X$$의 dense open subset이다. 특히, $$X_\sm \ne \emptyset$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$X = Z(f_1, \ldots, f_k) \subseteq \mathbb{A}^n$$의 차원이 $$\dim X = d$$라 하자. [명제 8](#prop8)의 Jacobian criterion에 의해

$$X_\sm = \{x \in X \mid \operatorname{rank}(J_x) = n - d\}$$

이다. 이제 이 집합이 dense open subset임을 보인다. 우선 $$X_\sm$$이 열린집합인 것은 상대적으로 자명하다.  Rank가 정확히 $$n-d$$라는 것은 두 조건의 동시 성립을 의미한다. 첫째, rank가 $$n-d$$ *이상*이라는 것은, 어떤 $$(n-d) \times (n-d)$$ 부분행렬의 행렬식이 0이 아닌 것과 동치이고, 이는 Zariski 위상에서 열린조건이다. 둘째, rank가 $$n-d$$ *이하*라는 것은, 모든 $$(n-d+1) \times (n-d+1)$$ 부분행렬의 행렬식이 0인 것과 동치이고, 이는 닫힌조건이다. 따라서 rank가 정확히 $$n-d$$인 점들의 집합은 $$X$$의 열린집합이다.

$$X_\sm$$이 공집합을 아님을 보이는 것이 다소 기술적인데, 아이디어는 일반적인 점이 smooth point가 되어야 하므로, $$X$$의 generic point $$\eta$$를 생각하는 것이다. $$\eta$$에서의 localization을 생각하면, local ring $$\mathcal{O}_{X,\eta} = \mathbb{K}(X)$$는 field이므로 regular local ring이다. 그런데 [\[가환대수학\] §매개계, ⁋명제 2](/ko/math/commutative_algebra/system_of_parameters#prop2)에 의해

$$\dim_{\mathbb{K}}(\mathfrak{m}_\eta/\mathfrak{m}_\eta^2) \ge \dim \mathcal{O}_{X,\eta} = d$$

인데, [명제 4](#prop4)에 의해 반대 부등식도 성립하므로 $$\dim T_\eta X = d$$이다. 따라서 $$\eta \in X_\sm$$이다. 이제 임의의 공집합이 아닌 열린집합은 irreducibility에 의해 dense이다. 

</details>

그럼 다음을 정의한다.

<div class="definition" markdown="1">

<ins id="def11">**정의 11**</ins> Variety $$X$$가 *smooth* (또는 *nonsingular*)라는 것은 모든 점이 smooth point인 것이다. 즉, $$X_\sm = X$$이다. 그렇지 않으면 (즉, singular point가 존재하면) *singular*라 부른다.

</div>

<div class="example" markdown="1">

<ins id="ex12">**예시 12**</ins> [예시 6](#ex6)의 variety들은 모두 smooth이고, [예시 7](#ex7)의 모든 variety들은 singular이다.

</div>

## 접원뿔

Singular point에서는 tangent space가 너무 커서 다양체의 국소적 구조를 정확히 반영하지 못한다. 이 경우 *tangent cone*이 더 정확한 정보를 제공한다. 직관적으로, tangent space가 너무 큰 것은 Jacobian의 rank가 너무 작은 것이고, 이는, 예를 들어, 주어진 함수의 일차근사만으로는 아무런 정보가 없기 때문에 일어난다. 따라서 만일 주어진 함수의 더 높은 차수의 근사를 생각한다면 상황이 달라질 수도 있을 것이다. 

이를 위해, 임의의 다항식 $$f\in \mathbb{K}[\x_1,\ldots, \x_n]$$에 대하여 $$f$$의 *initial term* $$\initial(f)$$을 $$f$$의 homogeneous component 중 가장 작은 차수를 갖는 것으로 정의한다. 그럼 임의의 ideal $$\mathfrak{a}$$에 대하여, $$\mathfrak{a}$$의 *initial ideal* $$\initial(\mathfrak{a})$$를 $$\initial(f)$$들로 생성되는 homogeneous ideal으로 정의한다. 

<div class="definition" markdown="1">

<ins id="def13">**정의 13**</ins> 임의의 affine variety $$X\subseteq \mathbb{A}^n$$에 대하여, $$\initial(I(X))$$이 정의하는 algebraic variety를 $$X$$의 원점에서의 *tangent cone*이라 정의한다.

</div>

더 일반적으로, $$f$$를 $$\x_i-x_i$$들에 대한 다항식으로 쓰고 비슷한 정의를 하면 임의의 점에서의 tangent cone을 정의할 수 있다. 이것이 cone이라 불리는 이유는, [§사영다양체, ⁋정의 12](/ko/math/algebraic_geometry/projective_varieties#def12)와 마찬가지로 homogeneous ideal의 zero set이기 때문이다.

이제 이것이 어떻게 singular point를 더 세밀하게 분류하는지 살펴보자. 

<div class="example" markdown="1">

<ins id="ex14">**예시 14**</ins> [예시 7](#ex7)의 nodal curve $$X = Z(\y^2 - \x^2(\x+1))$$에서, $$f$$의 lowest degree term은 $$\y^2 - \x^2 = (\y-\x)(\y+\x)$$이므로

$$TC_0 X = Z(\y-\x) \cup Z(\y+\x)$$

이다. 이는 node가 두 직선 $$\y = \x$$와 $$\y = -\x$$의 방향으로 갈라짐을 정확히 보여준다.

</div>

<div class="example" markdown="1">

<ins id="ex15">**예시 15**</ins> [예시 7](#ex7)의 곡선 $$X = Z(\y^2 - \x^3)$$에서, $$f$$의 lowest degree term은 $$\y^2$$이므로

$$TC_0 X = Z(\y^2)$$

이다. 이는 $$\y = 0$$ 직선을 두 번 count한 것이며, cusp가 $$\x$$-축 방향으로 뾰족하게 끝남을 보여준다. 비교하면, tangent space $$T_0 X = \mathbb{K}^2$$는 모든 방향을 포함하여 너무 크다.

</div>

일반적으로, [§유리사상, ⁋예시 12](/ko/math/algebraic_geometry/rational_maps#ex12)을 생각하면 nodal curve의 singularity는 blowup을 통해 해소할 수 있다. 즉 blowup을 하고 나면 원점에서 두 갈래 직선 $$\y-\x$$와 $$\y+\x$$는 $$\mathbb{P}^1$$에 의해 갈라지게 된다. 그러나 cusp은 그렇지 못하므로, 일반적으로 cusp이 node보다 좋지 않은 singularity로 생각한다. 

---

**참고문헌**

**[Har]** J. Harris, *Algebraic Geometry: A First Course*, Springer, 1992.
**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.
