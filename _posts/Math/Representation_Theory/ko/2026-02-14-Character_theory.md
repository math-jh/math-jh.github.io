---

title: "표현의 지표"
excerpt: ""

categories: [Math / Representation Theory]
permalink: /ko/math/representation_theory/character_theory
header:
    overlay_image: /assets/images/Math/Representation_Theory/Character_theory.png
    overlay_filter: 0.5
sidebar: 
    nav: "representation_theory-ko"

date: 2026-02-14
last_modified_at: 2026-02-14
weight: 2

---

이번 글에서 우리는 character function을 정의하고 이들의 성질에 대해 살펴본다. 이들은 representation을 분류하는 우리의 목표에 큰 도움을 줄 것이다. 

## 군 표현의 지표

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> $G$의 representation $\rho:G\rightarrow\Aut(V)$에 대응하는 *character<sub>지표</sub>* $\chi_\rho:G\rightarrow\mathbb{C}$를

$$\chi_\rho(g)=\tr(\rho(g))$$

으로 정의한다. 

</div>

즉, 각각의 $g\in G$를 받아서 이것이 정의하는 linear map $\rho(g):V\rightarrow V$의 trace를 내 주는 것이 이 함수가 하는 일이다. 앞으로 살펴보겠지만, 이 함수는 $G$의 representation을 설명하는데 큰 역할을 한다. 가령, 당장 볼 수 있는 것은 이 함수가 $V$의 차원을 담고 있는 것이다. 

$$\chi_\rho(e)=\tr(\rho(e))=\tr(\id_V)=\dim V.$$

한편 정의에 의하여

$$\chi_\rho(hgh^{-1})=\tr(\rho(h)\rho(g)\rho(h)^{-1})=\tr(\rho(g))=\chi_\rho(g)$$

가 성립하므로 ([\[선형대수학\] §특성다항식, ⁋정리 5](/ko/math/linear_algebra/characteristic_polynomial#cor5)), 우리는 이로부터 $\chi_\rho$가 $G$의 *conjugacy class*들 위에서 상수임을 안다. 이러한 함수들에도 이름이 있다. 

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> 함수 $f:G\rightarrow\mathbb{C}$가 *class function<sub>유함수</sub>*이라는 것은 $f(hgh^{-1})=f(g)$가 모든 $g,h\in G$에 대해 성립하는 것이다. 

</div>

한편, 우리는 두 linear map 

$$L_V:V\rightarrow V,\qquad L_W:W\rightarrow W$$

이 주어졌을 때 이들의 direct sum $L_V\oplus L_W: V\oplus W\rightarrow V\oplus W$, 이들의 tensor product $L_V\otimes L_W: V\otimes W \rightarrow V\otimes W$ 등이 어떻게 정의되는지 알고 있고, 이들의 trace가 어떻게 되는지 또한 (가령 행렬로 두고 계산하면) 알고 있다. 이로부터 다음의 명제를 얻는다. 

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> Representation $V, W$에 대해 다음이 성립한다. 

1. $\chi_{V\oplus W}=\chi_V\oplus \chi_W$
2. $\chi_{V\otimes W}=\chi_V\chi_W$
3. $\chi_{V^\ast}=\overline{\chi}_V$

</div>

## Projection formula

임의의 