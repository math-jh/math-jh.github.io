---
title: "선형계 (Linear Systems)"
excerpt: "Linear systems on algebraic varieties"

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/linear_systems
sidebar:
    nav: "algebraic_geometry-ko"

header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Linear_Systems.png
    overlay_filter: 0.5

date: 2026-03-12
last_modified_at: 2026-03-15
weight: 12

---

선형계(linear system)는 대수다양체 위의 divisor들의 linear subspace이다. 이는 다양체 위의 "가장 기본적인" hyperplane sections의 모임이며, 후속 섹션에서 소개할 Riemann-Roch theorem을 연구하는 기초이다. 선형계는 Picard group와 divisor class group의 intersection으로 볼 수 있다.

## 정의

선형계의 기본 아이디어는 divisor들의 linear subspace를 정의하는 것이다. 즉, divisor들의 vector space (projective version)을 만드는 것이다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 다양체 $$X$$ 위의 line bundle $$\mathcal{L}$$와 non-zero section $$s \in H^0(X, \mathcal{L})$$에 대해, *linear system* $$|\mathcal{L}|$$를\n\n$$|\mathcal{L}| = \{\mathrm{div}(t \cdot s) \mid t \in \mathbb{K}^\ast\}$$\n\n로 정의한다. 여기서 $$t \in \mathbb{K}^\ast$$는 scalar.\n\n</div>

기하학적으로, linear system은 divisor들의 "flat" subspace이다. 각 scalar multiple $$t \cdot s$$는 다른 divisor이지만, linear system 안에서는 "parallel"한 위치에 있다. 이는 "parallel lines"의 1-dimensional version으로 볼 수 있다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> Linear system $$|\mathcal{L}|$$의 elements는 projective space $$\mathbb{P}(H^0(X, \mathcal{L}))$$의 points에 대응된다.\n\n</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Section space $$H^0(X, \mathcal{L})$$는 vector space이고, projective space $$\mathbb{P}(H^0(X, \mathcal{L}))$$는 line bundle이고, linear system은 quotient of this projective space by scaling. Thus each point corresponds to a linear system.\n\n</details>

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> Linear system $$|\mathcal{L}|$$의 dimension $$\dim |\mathcal{L}|$$는 다음과 같이 계산된다.\n\n$$\dim |\mathcal{L}| = \dim H^0(X, \mathcal{L}) - 1$$\n\n</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$H^0(X, \mathcal{L})$$는 vector space이고, $$\mathbb{P}(H^0(X, \mathcal{L}))$$는 projective space이므로, dimension은 vector space의 dimension에서 1을 뺀 것이다.\n\n</details>

## Complete Linear System

가장 기본적인 linear system은 *complete linear system*이다.

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> *Complete linear system* $$|\mathcal{L}|$$는 모든 sections $$s \in H^0(X, \mathcal{L})$$에 대해 linear system이다.\n\n</div>

기하학적으로, complete linear system은 "가장 자연스러운" linear system이다. 그러나 complete linear system가 항상 "효과적인" divisor를 갖는 것은 아니다. Section이 vanish하지 않는 경우 (effective section)에만 effective linear system이다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> Complete linear system $$|\mathcal{L}|$$의 dimension은 $$\mathrm{h}^0(\mathcal{L}) - 1$$이다. 여기서 $$\mathrm{h}^0(\mathcal{L}) = \dim H^0(X, \mathcal{L})$$.\n\n</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$H^0(X, \mathcal{L})$$의 dimension이 $$\mathrm{h}^0(\mathcal{L})$$이므로, projective space의 dimension은 $$\mathrm{h}^0(\mathcal{L}) - 1$$이다.\n\n</details>

<div class="example" markdown="1">

<ins id="ex6">**예시 6**</ins> **Linear system의 예시들**\n\n1. $$\mathbb{P}^n$$의 hyperplane bundle $$\mathcal{O}_{\mathbb{P}^n}(1)$$: $$|\mathcal{O}_{\mathbb{P}^n}(1)|$$은 hyperplane sections의 complete linear system. Dimension $$\mathrm{h}^0(\mathcal{O}_{\mathbb{P}^n}(1)) - 1 = n+1 - 1 = n$$.\n2. $$\mathbb{P}^n$$의 $$k$$-times tensor $$\mathcal{O}_{\mathbb{P}^n}(k)$$: $$|\mathcal{O}_{\mathbb{P}^n}(k)|$$는 degree $$k$$ hypersurfaces. Dimension $$\mathrm{h}^0(\mathcal{O}_{\mathbb{P}^n}(k)) - 1 = \binom{n+k}{k} - 1$$.\n3. Curve $$C$$의 degree $$d$$ divisor: $$|\mathcal{O}_C(d)|$$는 degree $$d$$ effective divisors. Dimension depends on genus $$g$$.\n\n</div>

## Base Points

Linear system $$|\mathcal{L}|$$의 *base points*는 모든 divisor에 포함되는 점들의 집합이다.

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> Linear system $$|\mathcal{L}|$$의 *base locus* $$\mathrm{Bs}(|\mathcal{L}|)$$는 모든 $$D \in |\mathcal{L}|$$에 대해 $$D \supseteq B$$인 가장 큰 closed subset이다.\n\n</div>

기하학적으로, base locus은 linear system이 "generic divisor"에서도 vanish하는 점들의 집합이다. Base point가 없으면 linear system은 "generic" divisor가 effective이고 "generic" point에서 vanish하지 않는다.

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> Linear system $$|\mathcal{L}|$$의 base locus $$\mathrm{Bs}(|\mathcal{L}|)$$는 closed subset이다.\n\n</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Base locus은 intersection of all divisors in $$|\mathcal{L}|$$. Divisors are closed sets, so their intersection is closed.\n\n</details>

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> Complete linear system $$|\mathcal{L}|$$가 base point를 갖는 필요충분조건은 $$\mathrm{h}^0(\mathcal{L}) > \mathrm{h}^0(\mathcal{L} \otimes \mathcal{I}_p)$$ for some point $$p \in X$$. 여기서 $$\mathcal{I}_p$$는 $$p$$의 ideal sheaf.\n\n</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Base point가 존재하면, 모든 section이 vanish하므로 $$\mathrm{h}^0(\mathcal{L}) > \mathrm{h}^0(\mathcal{L} \otimes \mathcal{I}_p)$$. 이 converse도 true: base point가 없으면 generic point에서 vanish하지 않는 section이 존재.\n\n</details>

## Linear System의 응용

선형계는 다양한 기하학적 문제에 응용된다.

<div class="example" markdown="1">

<ins id="ex10">**예시 10**</ins> **Hyperplane sections**: $$\mathbb{P}^n$$에서 hyperplane bundle $$\mathcal{O}_{\mathbb{P}^n}(1)$$의 linear system $$|\mathcal{O}_{\mathbb{P}^n}(1)|$$은 hyperplane sections의 모임이다. 이는 projective geometry의 기본 도구이다.\n\n</div>

<div class="example" markdown="1">

<ins id="ex11">**예시 11**</ins> **Ruled surfaces**: Two-line bundle $$\mathcal{L}_1, \mathcal{L}_2$$의 linear system $$|\mathcal{L}_1 - \mathcal{L}_2|$$은 ruled surface의 parametrization에 사용된다. 이는 birational map의 구체적인 form이다.\n\n</div>

<div class="example" markdown="1">

<ins id="ex12">**예시 12**</ins> **Pencil**: Linear system $$|\mathcal{L}|$$의 1-dimensional subsystem $$|D_1 + D_2|$$ where $$D_1, D_2$$는 divisors. 이는 두 divisor의 family이다. Pencil은 curve의 genus 계산에 사용된다.\n\n</div>

---\n\n**참고문헌**\n\n**[Har]** J. Harris, *Algebraic Geometry: A First Course*, Springer, 1992.\n**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.\n**[Gr]** P. Griffiths and J. Harris, *Principles of Algebraic Geometry*, Wiley, 1978.\n**[Ful]** W. Fulton, *Intersection Theory*, Springer, 1984.\n