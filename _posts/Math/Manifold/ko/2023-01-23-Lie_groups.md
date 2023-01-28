---

title: "리 군"
excerpt: "Lie group의 정의와 성질"

categories: [Math / Manifold]
permalink: /ko/math/manifold/Lie_groups
header:
    overlay_image: /assets/images/Math/Manifold/Lie_groups.png
    overlay_filter: 0.5
sidebar: 
    nav: "manifold-ko"

date: 2023-01-23
last_modified_at: 2023-01-23
weight: 19

---

[§리 미분, ⁋명제 4](/ko/math/manifold/Lie_derivative#pp4)에서 우리는 주어진 벡터장 $X$ 방향으로의 벡터장 $Y$의 미분 

$$\mathcal{L}_XY=\lim_{t\rightarrow 0}\frac{(d\phi^{-t})_{\phi^t(p)}(Y_{\phi^t(p)})-Y_p}{t}$$

를 정의했으며, 그 값이 Lie bracket $[X,Y]$와 같다는 것을 살펴봤다. 한편, 벡터장 $X,Y$에 대하여, 다음의 식

$$(XY)f=X(Yf)$$

으로 정의된 연산자 $XY$는 라이프니츠 법칙을 만족하지 않고 따라서 $XY\not\in\mathfrak{X}(M)$이므로, 이와 같은 곱셈에 대하여 $\mathfrak{X}(M)$은 $C^\infty(M)$-algebra가 되지 않았다. 반면 $[X,Y]\in\mathfrak{X}(M)$이므로, $[-,-]$을 $\mathfrak{X}(M)$의 곱셈으로 삼으면 이를 $C^\infty(M)$-algebra로 생각할 수 있다. 이러한 구조를 *Lie algebra<sub>리 대수</sub>*라 부른다. 

이번 글에서 우리의 목표는 리 대수와 리 군에 대한 정의를 내리고, 이들의 성질을 간단하게 살펴보는 것이다.

## 리 군

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> Group $G$가 *Lie group<sub>리 군</sub>*이라는 것은 $G$가 그 자체로 manifold 구조를 가지고 있으며, 이 manifold 구조에 대하여 다음의 함수

$$G\times G\rightarrow G;\qquad (x,y)\mapsto xy^{-1}$$

가 $C^\infty$인 것이다. 

</div>

위와 같이, 특별한 경우를 제외하고는 대수학에서의 표기를 따라 $G$의 항등원은 $e$로, $G$에서의 연산은 $xy$와 같이 표기한다. 

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins> Lie group은 우리가 이미 알고 있는 많은 예시들을 포함하는 개념이다.

1. $\mathbb{R}^n$에 덧셈구조를 주면 $\mathbb{R}^n$은 Lie group이 된다. 이는 $(\mathbf{x},\mathbf{y})\mapsto \mathbf{x}-\mathbf{y}$으로 정의된 연산 $\mathbb{R}^n\times\mathbb{R}^n\rightarrow\mathbb{R}^n$이 $C^\infty$이기 때문이다.
2. 두 Lie group $G,H$에 대하여, $G\times H$ 또한 Lie group이 된다. 
3. $\GL_n(\mathbb{R})$의 곱셈, 그리고 역원은 (분모가 $0$이 되지 않는) 유리함수에 불과하므로 $C^\infty$이고, 따라서 $\GL_n(\mathbb{R})$ 또한 Lie group이다. $\SL_n(\mathbb{R})$ 또한 마찬가지이다.

</div>

## 리 대수

리 군이 정의되면, 이 위에 정의된 자연스러운 리 대수의 구조가 존재한다. 