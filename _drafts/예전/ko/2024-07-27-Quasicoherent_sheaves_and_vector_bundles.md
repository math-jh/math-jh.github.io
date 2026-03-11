---

title: "준연접층과 벡터다발"
excerpt: ""

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/quasicoherent_sheaves_and_vector_bundles
header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Quasicoherent_sheaves_and_vector_bundles.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_geometry-ko"

date: 2024-07-27
last_modified_at: 2024-07-27
weight: 10

---

이번 글에서는 우리가 알고 있는 두 대상, 즉 quasicoherent sheaf와 vector bundle의 관계에 대해 살펴본다. 직관적으로 이야기해서 vector bundle은 


이를 위해서는 우선 relative spec에 대해 알아야한다.

## Relative Spec

Scheme morphism $f:X \rightarrow Y$가 *affine*이라는 것은 $Y$의 모든 open affine subset $V$마다 $f^{-1}(V)$도 affine인 것이다. 이 개념을 사용하면 다음을 정의할 수 있다.

<div class="proposition" markdown="1">

<ins id="prop1">**명제 1**</ins> Scheme $Y$와 그 위에 정의된 $\mathscr{O}_Y$-algebra들의 quasicoherent sheaf $\mathscr{A}$를 생각하자. 그럼 유일한 scheme $X$와 morphism $f:X \rightarrow Y$가 존재하여 임의의 open affine subset $V\subseteq Y$가 주어질 때마다 $f^{-1}(V)\cong\Spec \mathscr{A}(V)$이고, 이 isomorphism을 통해 보면 open affine subset들 $U\hookrightarrow V$마다 정의된 morphism $f^{-1}(U) \rightarrow f^{-1}(V)$가 restriction $\mathscr{A}(V) \rightarrow \mathscr{A}(U)$와 같도록 할 수 있다. 

</div>

이 결과로 나오는 scheme $X$를 *relative Spec*이라 부르며 $\rSpec \mathscr{A}$으로 표기한다. 

## 준연접층과 벡터다발

한편 quasicoherent sheaf는 다른 기하학에서 다루는 vector bundle과 관련이 있다. 이를 설명하기 위해 먼저 vector bundle의 개념을 대수기하학의 언어로 적어보자.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> Scheme $Y$에 대하여, 이 위에 정의된 *vector bundle of rank $n$*은 다음의 조건을 만족하는 데이터들이다. 

1. Morphism $f:X \rightarrow Y$,
2. $Y$의 open covering $(U\_i)$, 그리고 isomorphism들 $\psi_i:f^{-1}(U\_i)\rightarrow \mathbb{A}^n\times U\_i=\mathbb{A}^n\_{U\_i}$

이들은 다음 조건을 만족한다. 

> 각각의 $i,j$ 그리고 $V=\Spec A\subseteq U_i\cap U_j$를 만족하는 open affine subset $V$가 주어질 때마다, $\mathbb{A}_V^n=\Spec A[x_1,\ldots, x_n]$의 automorphism $\psi=\psi_j\circ\psi_i^{-1}$이 $A[x_1,\ldots, x_n]$의 linear isomorphism으로 주어진다. 

</div>

우선 임의의 rank $n$ locally free sheaf $\mathscr{E}$가 주어졌다 하자. 그럼 $\mathscr{E}^\vee$의 symmetric algebra $\Sym(\mathscr{E}^\vee)$도 다시 locally free이다. 따라서 $\Sym(\mathscr{E}^\vee)$의 relative Spec $\pi:\rSpec\Sym(\mathscr{E}^\vee)\rightarrow Y$를 생각할 수 있다. 이제 $Y$의 open affine set $U$를 충분히 작게 잡아 다음의 isomorphism

$$\Sym(\mathscr{E}^\vee(U))\cong \mathscr{O}_Y(U)[x_1,\ldots, x_n]$$

을 얻자. $\Sym(\mathscr{E}^\vee)$는 locally free이므로, 이러한 isomorphism이 존재하도록 하는 open affine $(U_i)$들로 $Y$를 모두 덮을 수 있다. 이러한 각각의 $U
_i$에 대해, [명제 1](#prop1)을 적용하면 다음 isomorphism

$$\psi_i:f^{-1}(U_i)\cong\Spec \Sym(\mathscr{E}^\vee(U_i))\cong \Spec \mathscr{O}_Y(U_i)[x_1,\ldots, x_n]$$

이 존재한다. 

<div class="proposition" markdown="1">

<ins id="lem3">**보조정리 3**</ins> 위와 같은 상황에서 $\pi:\rSpec\Sym(\mathscr{E}^\vee) \rightarrow Y$와 open covering들 $(U_i)$, 그리고 isomorphism들 $\psi_i$들은 vector bundle이다. 

</div>

거꾸로, $\pi:\rSpec \Sym(\mathscr{E}^\vee)\rightarrow Y$에 의해 $Y$ 위에 정의된 sheaf of sections $\mathscr{F}$를 생각하자. 일반적으로 임의의 rank $n$ vector bundle $f:X \rightarrow Y$를 통해 정의되는 sheaf of sections는 locally free $\mathscr{O}_Y$-module of rank $n$임을 보일 수 있으며, 따라서 $\mathscr{F}$는 locally free $\mathscr{O}_Y$-module of rank $n$이다. 

<div class="proposition" markdown="1">

<ins id="lem4">**보조정리 4**</ins> 위와 같은 상황에서 $\mathscr{F}\cong \mathscr{E}^{\vee\vee}\cong \mathscr{E}$이 성립한다. 

</div>

우선 임의의 section $s\in\Gamma(U, \mathscr{E}^{\vee\vee})$가 주어졌다 하자. 이는 

$$\mathscr{E}^{\vee\vee}=\mathscr{Hom}(\mathscr{E}^\vee, \mathscr{O}_X)(U)=\Hom(\mathscr{E}^\vee\vert_U, \mathscr{O}_U)$$

의 원소이므로, $\mathscr{O}_U$-algebra homomorphism $\Sym(\mathscr{E}^\vee\vert_U)\rightarrow \mathscr{O}_U$를 정의한다. 따라서 relative Spec을 취하면

$$U=\rSpec \mathscr{O}_U \rightarrow \rSpec\Sym(\mathscr{E}^\vee\vert_U)=f^{-1}(U)$$

가 복원된다. 

즉, 두 보조정리를 정리하자면 scheme $Y$ 위에 정의된 vector bundle of rank $n$과 $Y$ 위에 정의된 locally free sheaf of rank $n$ 사이에는 일대일대응이 있다. 여기서 locally free sheaf는 vector bundle의 section에 해당하는 것이다. 이와 같은 이유로 locally free sheaf of rank $1$을 종종 *line bundle*이라 부르기도 한다. 