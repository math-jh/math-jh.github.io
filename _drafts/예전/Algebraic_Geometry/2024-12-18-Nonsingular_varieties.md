---

title: "비퇴화다양체"
excerpt: ""

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/nonsingular_varieties
header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Nonsingular_varieties.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_geometry-ko"

date: 2024-12-18
last_modified_at: 2024-12-18
weight: 4

---

이제 우리는 좋은 다양체들에 대해 살펴본다. 

## 정의

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Affine variety $X\subseteq \mathbb{A}^n$이 주어졌다 하고, $X$에 해당하는 ideal

$$I(X)\subseteq \mathbb{k}[\x_1,\ldots, \x_n]$$

의 generator $f_1,\ldots, f_t$이 주어졌다 하자. 그럼 $X$가 점 $x\in X$에서 *nonsingular<sub>비퇴화</sub>*라는 것은 행렬

$$J_{X,x}=\begin{pmatrix}\frac{\partial f_1}{\partial \x_1}(x)&\frac{\partial f_1}{\partial \x_2}(x)&\cdots&\frac{\partial f_1}{\partial \x_n}(x)\\\frac{\partial f_2}{\partial \x_1}(x)&\frac{\partial f_2}{\partial \x_2}(x)&\cdots&\frac{\partial f_2}{\partial \x_n}(x)\\\vdots&\vdots&\ddots&\vdots\\\frac{\partial f_t}{\partial \x_1}(x)&\frac{\partial f_t}{\partial \x_2}(x)&\cdots&\frac{\partial f_t}{\partial \x_n}(x)\\\end{pmatrix}$$

의 rank가 $\codim X$와 같은 것이다. 만일 $X$가 모든 점에서 nonsingular라면, 이를 간단히 nonsingular라 부른다. 

</div>

이에 대한 설명은 다음과 같다. 아직 정의하지는 않았지만, affine variety $X\subseteq \mathbb{A}^n$의 tangent space를 생각하면, 점 $x\in X$에서의 tangent space $T_xX$를 $T_x \mathbb{A}^n$의 subspace로 생각할 수 있다. 이 때, $T_xX$는 Jacobian matrix $J_{X,x}$의 kernel로 정해지므로 그 codimension은 $J_{X,x}$의 rank와 같아야 한다. 

한편, 우리는 manifold의 경우에서 일상적이지 않은 정의를 사용해서 cotangent space를 굳이 sheaf를 사용해서 $\mathfrak{m}/\mathfrak{m}^2$으로 정의했는데, 이는 지금의 정의를 조금 더 친숙하게 하기 위한 것이었다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> Noetherian local ring $A$가 maximal ideal $\mathfrak{m}$, 그리고 residue field $\kappa=A/\mathfrak{m}$을 갖는다고 하자. 만일 $\dim A=\dim_\kappa \mathfrak{m}/\mathfrak{m}^2$라면, $A$를 *regular local ring*이라 부른다.

</div>

그럼 다음의 정리가 성립한다.

<div class="proposition" markdown="1">

<ins id="thm3">**정리 3**</ins> Affine variety $X\subseteq \mathbb{A}^n$와 한 점 $x\in X$에 대하여, $X$가 $x$에서 nonsingular인 것과 local ring $\mathscr{O}_{X,x}$가 regular local ring인 것이 동치이다. 

</div>

이를 직관삼아 일반적인 경우에는 다음과 같이 정의할 수 있다. 

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> 임의의 variety $X$에 대하여, $X$가 $x\in X$에서 *nonsingular<sub>비퇴화</sub>*라는 것은 $\mathscr{O}_{X,x}$가 regular local ring인 것이다. 만일 $X$가 모든 점에서 nonsingular라면 이를 간단히 *nonsingular*라 부르고, 그렇지 않다면 *singular*라 부른다. 

</div>

그럼 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="thm5">**정리 5**</ins> 임의의 variety $X$에 대하여, $X$의 singular point들의 모임 $\Sing X$는 $X$의 proper인 닫힌집합이다.

</div>

임의의 variety에서 열린집합은 크고, 닫힌집합은 작으므로, 위의 정리는 variety가 대부분의 점에서 non-singular라는 것이다.

한편, 아직 우리가 미분을 정의하지는 않았지만, [##ref##](Cohen_structure_thm)을 생각하면 대수적으로 미분과 completion이 서로 관련되어 있고, 또 정의로부터 알 수 있듯 $X$가 nonsingular라는 것 또한 미분을 통해 서술된다. 이를 엄밀한 언어로 쓰기 위해서는 module of differential을 사용해야 하지만, 

## 비퇴화곡선

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> Field $K$에 포함되어 있는 두 local ring $A,B$에 대하여, 만일 $A\subseteq B$이고 $\mathfrak{m}_B\cap A=\mathfrak{m}_A$라면 $B$가 $A$를 *dominate*한다고 말한다.

</div>