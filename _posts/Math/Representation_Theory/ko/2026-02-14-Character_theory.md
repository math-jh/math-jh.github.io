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

즉, 각각의 $g\in G$를 받아서 이것이 정의하는 linear map $\rho(g):V\rightarrow V$의 trace를 내 주는 것이 이 함수가 하는 일이다. 정의에 의하여

$$\chi_\rho(hgh^{-1})=\tr(\rho(h)\rho(g)\rho(h)^{-1})=\tr(\rho(g))=\chi_\rho(g)$$

가 성립하므로 ([\[선형대수학\] §특성다항식, ⁋정리 5](/ko/math/linear_algebra/characteristic_polynomial#cor5)), 우리는 이로부터 $\chi_\rho$가 $G$의 *conjugacy class*들 위에서 상수임을 안다. 이러한 함수들에도 이름이 있다. 

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> 함수 $f:G\rightarrow\mathbb{C}$가 *class function<sub>유함수</sub>*이라는 것은 $f(hgh^{-1})=f(g)$가 모든 $g,h\in G$에 대해 성립하는 것이다. 

</div>

