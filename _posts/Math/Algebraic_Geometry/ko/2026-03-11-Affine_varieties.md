---
title: "아핀다양체"
excerpt: "Affine varieties and their basic properties"

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/affine_varieties
sidebar: 
    nav: "algebraic_geometry-ko"

header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Affine_Varieties.png
    overlay_filter: 0.5

date: 2026-03-11
last_modified_at: 2026-03-11
weight: 1

---

대수기하학은 다항식으로 정의되는 기하적 대상들을 연구하는 학문이다. 수식으로는, 벡터공간 $$\mathbb{K}^n$$이 주어졌을 때, 다음의 식

$$V(f)= \{(a_1, \ldots, a_n) \in \mathbb{R}^n \mid f(a_1, \ldots, a_n) = 0\},\qquad f\in \mathbb{K}[\x_1,\ldots, \x_n]$$

으로 주어지는 집합들을 연구하는 것이 기본적인 목적이라 할 수 있다. 일반적으로 $$\mathbb{K}=\mathbb{C}$$로 두지만, 대부분의 경우 이렇게 가정하는 것이 큰 도움이 되지는 않으므로 우리는 더 일반적인 세팅을 사용하기로 한다. 또, 다항식의 변수를 표현할 때는 위와 같이 정자 $$\x$$들을 사용하는 것을 원칙으로 한다. 

## 아핀다양체의 정의

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Field $$\mathbb{K}$$ 위에 정의된 *affine $n$-space<sub>$n$차원 아핀공간</sub>* $$\mathbb{A}^n_\mathbb{K}$$는 $$n$$차원 벡터공간 $$\mathbb{K}^n$$을 의미한다. 

</div>

Field $$\mathbb{K}$$를 생략해도 될 때는 $$\mathbb{A}^n$$과 같이 적는다. 우리는 affine space 

$$\mathbb{A}^n=\{(a_1,\ldots, a_n)\mid a_i\in \mathbb{K}\}$$

의 원소를 *점<sub>point</sub>*이라 부르고, 각각의 좌표 $$a_i$$를 *$i$번째 좌표*라 부른다. 우리가 살펴볼 기하적인 대상들은, 위에서와 같이, 다항식 $$f\in \mathbb{K}[\x_1,\ldots, \x_n]$$의 zero set $$V(f)$$로 나타나는 대상들이다. 

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> 다항식 $$f_1, \ldots, f_k \in \mathbb{2}[\x_1, \ldots, \x_n]$$에 대하여, 이들이 정의하는 *affine variety<sub>아핀다양체</sub>* $$V(f_1, \ldots, f_k)$$를

$$V(f_1, \ldots, f_k) = \{(a_1, \ldots, a_n) \in \mathbb{A}^n \mid f_1(a) = \cdots = f_k(a) = 0\}$$

으로 정의한다.

</div>

즉, 아핀다양체는 여러 다항식들 $$f_1,\ldots, f_k$$의 공통된 zero set이라 할 수 있다. 

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> 우리가 아는 대다수의 기하학적인 대상들은 대체로 다항식으로 나타나므로, 이들이 모두 affine variety의 예시가 된다. 

1. 가령, 우리는 $$\mathbb{A}^2$$ 안에서 정의된 affine variety $$V(\x^2+\y^2-1)$$를 생각할 수 있다. 정의에 의해, 이 집합은 식 $$\x^2+\y^2-1=0$$을 만족하는 $$\mathbb{A}^2$$들의 모임이므로, 이는 단위원을 나타낸다. 
2. 일반적으로, 임의의 affine space $$\mathbb{A}^n$$와 임의의 다항식 $$f\in \mathbb{K}[\x_1,\ldots, \x_n]$$에 대하여, $$V(f)$$는 초곡면을 정의할 것이다. 
3. 곧 살펴볼 [명제 5](#prop5)에서 중요하게 사용될 성질로, affine space $$\mathbb{A}^n$$ 자기자신과 공집합은 affine variety이다. 이는 다음의 두 식 $$V(0)=\mathbb{A}^n$$, $$V(1)=\emptyset$$으로부터 자명하다. 

</div>

<div class="example" markdown="1">

<ins id="ex4">**예시 4**</ins> **Twisted cubic**: 세 다항식

$$y - x^2, \quad z - x^3$$

에 의해 정의되는 아핀다양체 $C = V(y - x^2, z - x^3) \subset \mathbb{A}^3$을 *twisted cubic*이라 부른다. 이는 매개화

$$t \mapsto (t, t^2, t^3)$$

을 통해 $\mathbb{A}^1$과 일대일 대응된다.

</div>

## Zariski 위상

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> 다음이 성립한다:

1. $V(0) = \mathbb{A}^n$
2. $V(1) = \emptyset$
3. $I \subseteq J \implies V(J) \subseteq V(I)$
4. $\bigcap_{\alpha} V(I_\alpha) = V\left(\sum_\alpha I_\alpha\right)$
5. $V(I) \cup V(J) = V(I \cap J) = V(IJ)$

</div>

따라서 아핀다양체들을 닫힌집합으로 갖는 위상을 정의할 수 있다.

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> $\mathbb{A}^n$의 *Zariski 위상<sub>Zariski topology</sub>*은 아핀다양체들을 닫힌집합으로 갖는 위상이다.

</div>

<div class="example" markdown="1">

<ins id="ex7">**예시 7**</ins> $\mathbb{A}^1$에서 Zariski 위상은 *여유한 위상<sub>cofinite topology</sub>*이다. 닫힌집합들은 $\mathbb{A}^1$ 자신과 유한집합들뿐이다.

</div>

<div class="remark" markdown="1">

**참고 8** Zariski 위상은 하우스도르프가 아니다. 예를 들어 $\mathbb{A}^1$에서 서로 다른 두 점 $a \ne b$를 분리하는 열린집합이 존재하지 않는다.

</div>

## Ideals of Varieties

<div class="definition" markdown="1">

<ins id="def9">**정의 9**</ins> 부분집합 $X \subseteq \mathbb{A}^n$의 *ideal<sub>이데알</sub>* $I(X)$를

$$I(X) = \{f \in \mathbb{k}[x_1, \ldots, x_n] \mid f(a) = 0 \text{ for all } a \in X\}$$

으로 정의한다.

</div>

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10**</ins> 다음이 성립한다:

1. $I(X)$는 $\mathbb{k}[x_1, \ldots, x_n]$의 ideal이다.
2. $X \subseteq Y \implies I(Y) \subseteq I(X)$
3. $I(\emptyset) = \mathbb{k}[x_1, \ldots, x_n]$
4. $I(\mathbb{A}^n) = (0)$ (if $\mathbb{k}$ is infinite)
5. $X \subseteq V(I(X))$
6. $I \subseteq I(V(I))$

</div>

<div class="example" markdown="1">

<ins id="ex11">**예시 11**</ins>

1. $I(\{(a_1, \ldots, a_n)\}) = (x_1 - a_1, \ldots, x_n - a_n)$
2. $I(V(f)) = \sqrt{(f)}$ (radical)
3. Twisted cubic $C$에 대해 $I(C) = (y - x^2, z - x^3)$

</div>

## Hilbert 영점 정리

<div class="theorem" markdown="1">

<ins id="thm12">**정리 12**</ins> (Hilbert Nullstellensatz) $\mathbb{k}$가 대수적으로 닫힌 체이고 $I \subseteq \mathbb{k}[x_1, \ldots, x_n]$이 ideal이라 하자. 그럼

$$I(V(I)) = \sqrt{I} = \{f \mid f^m \in I \text{ for some } m \ge 1\}$$

이다.

</div>

이 정리에 의해 아핀다양체의 ideal은 항상 *radical ideal*이다.

<div class="corollary" markdown="1">

<ins id="cor13">**따름정리 13**</ins> 다음이 성립한다:

1. $V(I) = \emptyset \iff I = (1)$
2. $V(I) = V(J) \iff \sqrt{I} = \sqrt{J}$

</div>

## Coordinate Ring

<div class="definition" markdown="1">

<ins id="def14">**정의 14**</ins> 아핀다양체 $X = V(I) \subseteq \mathbb{A}^n$의 *좌표환<sub>coordinate ring</sub>* $\mathbb{k}[X]$를

$$\mathbb{k}[X] = \mathbb{k}[x_1, \ldots, x_n] / I(X)$$

으로 정의한다.

</div>

<div class="proposition" markdown="1">

<ins id="prop15">**명제 15**</ins> 좌표환 $\mathbb{k}[X]$의 원소들은 $X$ 위에서 정의된 "다항식 함수"들이다. 즉, 함수 $X \to \mathbb{k}$로 생각할 수 있다.

</div>

<div class="example" markdown="1">

<ins id="ex16">**예시 16**</ins>

1. $\mathbb{k}[\mathbb{A}^n] = \mathbb{k}[x_1, \ldots, x_n]$
2. $\mathbb{k}[V(x)] = \mathbb{k}[x, y]/(x) \cong \mathbb{k}[y]$
3. $\mathbb{k}[\text{twisted cubic}] = \mathbb{k}[t]$

</div>

## Regular Functions

<div class="definition" markdown="1">

<ins id="def17">**정의 17**</ins> 아핀다양체 $X$ 위의 *regular function<sub>정칙함수</sub>*란 좌표환 $\mathbb{k}[X]$의 원소를 말한다.

</div>

<div class="example" markdown="1">

<ins id="ex18">**예시 18**</ins> 단위원 $X = V(x^2 + y^2 - 1)$ 위에서:

- $f(x, y) = x + y$는 regular function
- $g(x, y) = \frac{x}{1+y}$는 $y \ne -1$인 점에서만 정의됨 (rational function)
- $\mathbb{k}[X] = \mathbb{k}[x, y]/(x^2 + y^2 - 1)$

</div>

## Morphisms of Affine Varieties

<div class="definition" markdown="1">

<ins id="def19">**정의 19**</ins> 아핀다양체 $X \subseteq \mathbb{A}^n$과 $Y \subseteq \mathbb{A}^m$ 사이의 *morphism<sub>사상</sub>* (또는 *regular map*)이란 함수 $\varphi: X \to Y$로서, 다항식 $f_1, \ldots, f_m \in \mathbb{k}[x_1, \ldots, x_n]$들이 존재하여

$$\varphi(a_1, \ldots, a_n) = (f_1(a), \ldots, f_m(a))$$

를 만족하는 것이다.

</div>

<div class="example" markdown="1">

<ins id="ex20">**예시 20**</ins>

1. **매개화**: $\mathbb{A}^1 \to \mathbb{A}^3$, $t \mapsto (t, t^2, t^3)$은 twisted cubic으로의 morphism
2. **투영**: $\mathbb{A}^3 \to \mathbb{A}^2$, $(x, y, z) \mapsto (x, y)$는 morphism
3. **항등사상**: $\operatorname{id}: X \to X$는 morphism

</div>

<div class="proposition" markdown="1">

<ins id="prop21">**명제 21**</ins> Morphism $\varphi: X \to Y$는 coordinate ring homomorphism $\varphi^\ast: \mathbb{k}[Y] \to \mathbb{k}[X]$를 유도한다.

</div>

## Isomorphisms

<div class="definition" markdown="1">

<ins id="def22">**정의 22**</ins> Morphism $\varphi: X \to Y$가 *isomorphism*이라는 것은 역함수 $\psi: Y \to X$가 존재하여 $\psi$도 morphism인 것이다.

</div>

<div class="example" markdown="1">

<ins id="ex23">**예시 23**</ins>

1. **Twisted cubic와 $\mathbb{A}^1$**: $\varphi: \mathbb{A}^1 \to C$, $t \mapsto (t, t^2, t^3)$은 isomorphism
   - 역함수: $(x, y, z) \mapsto x$
   - Coordinate rings: $\mathbb{k}[C] \cong \mathbb{k}[t]$

2. **Parabola와 $\mathbb{A}^1$**: $\varphi: \mathbb{A}^1 \to V(y - x^2)$, $t \mapsto (t, t^2)$는 isomorphism

</div>

---

**참고문헌**

**[Har]** J. Harris, *Algebraic Geometry: A First Course*, Springer, 1992.  
**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.  
**[Ful]** W. Fulton, *Algebraic Curves*, 2008. (Available online)
