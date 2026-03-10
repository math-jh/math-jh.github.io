---
title: "대수적 군"
excerpt: "Algebraic group action"

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/algebraic_groups
sidebar: 
    nav: "algebraic_geometry-ko"

header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Algebraic_Groups.png
    overlay_filter: 0.5

date: 2026-03-11
last_modified_at: 2026-03-11
weight: 1000

---

## 대수적 군

우리는 수학적 대상이 다른 대상에 작용하는 많은 예시들을 알고 있다. 대수적으로 가장 중요한 예시는 벡터공간 위에 작용하는 군일 것이며, 기하적으로는 Lie group action이 있다. 대수기하학은 대수적인 대상들에 기하학적인 의미를 부여하므로, 대수적 군의 작용은 이들 두 관점을 잘 통합하는 형태로 나타난다. 이번 글에서 우리는 편의상 $$\mathbb{k}=\mathbb{C}$$로 통일한다. 

우선 다음 정의는 자명하다. 

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> *Algebraic group<sub>대수적 군</sub>* $$G$$는 다음 조건들을 만족하는 algebraic variety이다:

1. $$G$$는 group 구조를 갖는다.
2. Multiplication $$m: G \times G \to G$$와 inverse $$i: G \to G$$가 모두 morphism of varieties이다.

</div>

Lie group에서와 마찬가지로, 가장 중요한 예시들은 보통 matrix group들이다. 

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins> 가장 기본적인 예시들은 다음과 같다:

1. *General linear group* $$\GL(n, \mathbb{C}) = \{A \in M_{n \times n}(\mathbb{C}) \mid \det A \ne 0\}$$는 $$\mathbb{C}^{n\times n}$$의 open subvariety로서 algebraic group의 구조를 갖는다.
2. *Special linear group* $$\SL(n, \mathbb{C}) = \{A \in \GL(n, \mathbb{C}) \mid \det A = 1\}$$는 $$\GL(n, \mathbb{C})$$의 closed subvariety로서 algebraic group이다.
3. 두 abelian group $$\mathbb{G}_a = \mathbb{C}$$ (덧셈)과 $$\mathbb{G}_m = \mathbb{C}^\ast$$ (곱셈)은 모두 1차원 algebraic group이다.

</div>

Algebraic group 중에서 특히 중요한 역할을 하는 것은 당연히 *affine algebraic group*이다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> Algebraic group $$G$$가 *affine algebraic group*라는 것은 $$G$$가 affine variety인 것이다. 

</div>

## 대수적 군의 작용

이제 algebraic group이 algebraic variety 위에 작용하는 방식을 정의한다.

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> Algebraic group $$G$$의 algebraic variety $$X$$ 위로의 *action<sub>작용</sub>*이란 morphism

$$\alpha: G \times X \to X$$

으로서, 다음 조건들을 만족하는 것이다:

1. $$\alpha(e, x) = x$$ for all $$x \in X$$ (항등원 보존)
2. $$\alpha(g, \alpha(h, x)) = \alpha(gh, x)$$ for all $$g, h \in G$$, $$x \in X$$ (결합법칙)

</div>

원칙적으로 algebraic group action은 affine algebraic group이 affine variety 위에 작용하는 방식만 살펴본 후 이들을 잘 붙이는 것이다. 이 경우를 더 잘 살펴보기 위해 affine algebraic group $$G = \Spec(A)$$가 affine variety $$X = \Spec(B)$$ 위에 작용하는 경우를 생각하자. $$\Spec$$이 contravariant functor이므로, action $$G \times X \to X$$는 coordinate ring 위의 구조로 번역된다. 구체적으로, 이는 다음의 데이터를 제공한다.

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> Affine algebraic group $$G = \Spec(A)$$와 affine variety $$X = \Spec(B)$$에 대하여, $$G$$의 $$X$$ 위로의 action에 대응하는 *comodule structure*란 algebra homomorphism

$$\rho: B \to B \otimes_\mathbb{C} A$$

으로서, 다음 조건들을 만족하는 것이다:

1. (Coassociativity) $$(\rho \otimes \id_A) \circ \rho = (\id_B \otimes \Delta) \circ \rho$$
2. (Counit) $$(\id_B \otimes \epsilon) \circ \rho = \id_B$$

</div>

여기서 $$\Delta: A \to A \otimes A$$는 $$G$$의 곱셈으로부터 유도되는 comultiplication이고, $$\epsilon: A \to \mathbb{C}$$는 항등원으로부터 유도되는 counit이다.

## 대수적 군의 표현

Lie group과 마찬가지로, algebraic group도 표현론을 통해 더 잘 이해할 수 있다.

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> Algebraic group $$G$$의 *representation<sub>표현</sub>*이란 유한차원 벡터공간 $$V$$와 group homomorphism

$$\rho: G \to \GL(V)$$

으로서, $$G \times V \to V$$가 morphism인 것이다.

</div>

그럼 다음 정의 또한 Lie group에서와 동일한 것이다. 

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> 표현 $$\rho: G \to \GL(V)$$의 *character<sub>지표</sub>* $$\chi_\rho: G \to \mathbb{C}$$는

$$\chi_\rho(g) = \tr(\rho(g))$$

으로 정의된다.

</div>

뿐만 아니라, 다음 명제에서 볼 수 있듯 algebraic group의 representation 또한 대수적인 본질과 기하적인 본질을 동시에 가지고 있다. 

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> Affine algebraic group $$G = \Spec(A)$$의 representation $$\rho: G \to \GL(V)$$는 $$V$$ 위의 comodule structure $$V \to V \otimes_\mathbb{C} A$$와 일대일 대응한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Representation $$\rho: G \to \GL(V)$$가 주어지면, 이는 $$G \times V \to V$$를 유도하고, $$\Spec$$의 contravariance에 의해 $$V^\ast \to V^\ast \otimes A$$를 얻는다. 

반대로 comodule structure $$V \to V \otimes A$$가 주어지면, 각 $$g \in G$$에 대해 evaluation map $$\operatorname{ev}_g: A \to \mathbb{C}$$을 통해 $$V \to V \otimes \mathbb{C} \cong V$$를 얻고, 이것이 representation을 정의한다.

</details>

## Algebraic torus와 weight decomposition

Algebraic group 중 가장 많이 접하게 되는 대상 중 하나는 torus $$T$$이다. $$1$$차원 torus는 우리가 이미 살펴보았다. ([예시 2](#ex2))

<div class="definition" markdown="1">

<ins id="def9">**정의 9**</ins> *Algebraic torus<sub>대수적 토러스</sub>*는 $$\mathbb{G}_m = \mathbb{C}^\ast$$의 finite direct sum과 isomorphic한 algebraic group이다. 즉,

$$T \cong (\mathbb{C}^\ast)^n$$

을 만족하는 $$n \ge 1$$이 존재하는 algebraic group이다.

</div>

우리는 Lie group에서, torus가 1차원 representation들로 분해되며 이들 각각에 대한 정보는 character에 담겨있는 것을 살펴보았다. 마찬가지의 일을 여기에서도 진행하자. 

<div class="definition" markdown="1">

<ins id="def10">**정의 10**</ins> Torus $$T = (\mathbb{C}^\ast)^n$$의 *character* $$\rchi: T \to \mathbb{C}^\ast$$는 다음과 같이 정의된다. 각 coordinate $$t_i \in \mathbb{C}^\ast$$에 대해

$$\rchi(t_1, \ldots, t_n) = t_1^{a_1} \cdots t_n^{a_n}$$

로서, $$a_i \in \mathbb{Z}$$이고 $$a = (a_1, \ldots, a_n) \in \mathbb{Z}^n$$이다. 

</div>

두 character $$\rchi^a$$와 $$\rchi^b$$의 곱은

$$\rchi^a \cdot \rchi^b = \rchi^{a+b}$$

으로 정의된다. 이는 $$\mathbb{Z}^n$$의 덧셈

$$a + b = (a_1 + b_1, \ldots, a_n + b_n)$$

에 대응된다. Character들의 집합 $$X^\ast(T) = \{\rchi^a \mid a \in \mathbb{Z}^n\}$$은 이 곱셈에 대해 abelian group을 이루며, 이를 torus $$T$$의 *character group*이라 부른다. 

어렵지 않게 $$\rchi: T \to \mathbb{C}^\ast$$가 group homomorphism임을 보일 수 있다.

<div class="proposition" markdown="1">

<ins id="prop11">**명제 11**</ins> Torus $$T = (\mathbb{C}^\ast)^n$$의 coordinate ring은 character들의 polynomial ring $$\mathbb{C}[\rchi_1^{\pm 1}, \ldots, \rchi_n^{\pm 1}]$$과 isomorphic하다. 여기서 $$\rchi_i(t_1, \ldots, t_n) = t_i$$는 $$i$$번째 coordinate에 대한 character이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Torus $$T = (\mathbb{C}^\ast)^n$$은 $$n$$개의 $$\mathbb{C}^\ast$$의 direct product이므로, 그 coordinate ring은 각 $$\mathbb{C}^\ast$$의 coordinate ring들의 tensor product이다. 이 때 $$\mathbb{C}^\ast = \mathbb{C} \setminus \{0\}$$의 coordinate ring은 $$\mathbb{C}[x, x^{-1}]$$임을 안다. ([§스킴, ⁋예시 10](/ko/math/algebraic_geometry/schemes#ex10))

따라서 $$T$$의 coordinate ring은

$$\mathbb{C}[x_1, x_1^{-1}] \otimes \cdots \otimes \mathbb{C}[x_n, x_n^{-1}] \cong \mathbb{C}[x_1, x_1^{-1}, \ldots, x_n, x_n^{-1}]$$

이다. 각 $$x_i$$는 $$i$$번째 coordinate function $$\rchi_i: T \to \mathbb{C}^\ast$$에 해당하며, $$\rchi_i(t_1, \ldots, t_n) = t_i$$로 정의된다. 이는 정확히 torus의 character이고, 그 inverse $$\rchi_i^{-1}$$도 마찬가지로 character이다.

따라서 $$T$$의 coordinate ring은 모든 character들로 생성되는 polynomial ring과 일치한다.

</details>

Torus $$T$$가 affine variety $$X = \Spec(A)$$ 위에 작용하는 경우, coordinate ring $$A$$는 weight space들로 분해된다.

<div class="proposition" markdown="1">

<ins id="prop12">**명제 12**</ins> Torus $$T$$가 affine variety $$X = \Spec(A)$$ 위에 action하면, coordinate ring $$A$$는 weight space들로 분해된다:

$$A = \bigoplus_{\rchi \in X^\ast(T)} A_\rchi$$

여기서 $$X^\ast(T)$$는 torus의 character group이고, 각 weight space $$A_\rchi$$는

$$A_\rchi = \{f \in A \mid t \cdot f = \rchi(t) f \text{ for all } t \in T\}$$

으로 정의된다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Torus action $$T \times X \to X$$가 주어지면, coordinate ring $$A$$ 위에 action $$t \cdot f = f(t)$$로 정의할 수 있다. 이 action은 linear하고, 각 coordinate ring의 원소 $$f$$는 eigenvalue를 가진 eigenvector로 분해될 수 있다. 이 eigenvalue들은 torus의 character들과 일치하므로, $$A$$는 weight space들의 직합으로 분해된다.

</details>

## Quotient Varieties

Action이 주어진 algebraic variety에서 우리는 종종 *quotient variety*를 구성하고자 한다. 그러나 이러한 대상이 잘 정의되는 것은 주로 대수적인 세팅에서 뿐이며, 가장 간단한 기하적인 대상인 위상공간에서도 이것이 잘 정의되지는 않았다. 이는 algebraic variety의 세상에서도 마찬가지이다. 

<div class="definition" markdown="1">

<ins id="def13">**정의 13**</ins> Algebraic group $$G$$가 algebraic variety $$X$$ 위에 작용할 때, 다음을 정의한다. 

- *Orbit*: $$G \cdot x = \{g \cdot x \mid g \in G\} \subseteq X$$
- *Stabilizer*: $$G_x = \{g \in G \mid g \cdot x = x\} \le G$$
- *Fixed point set*: $$X^G = \{x \in X \mid g \cdot x = x \text{ for all } g \in G\}$$

</div>

Quotient를 구성하기 위해서는 $$G$$-invariant function들을 살펴보아야 한다.

<div class="definition" markdown="1">

<ins id="def14">**정의 14**</ins> Affine algebraic group $$G$$가 affine variety $$X = \Spec(A)$$ 위에 작용할 때, 이에 대응하는 comodule structure $$\rho: A \to A \otimes_\mathbb{C} \mathbb{C}[G]$$에 대하여, *invariant ring* $$A^G$$는

$$A^G = \{a \in A \mid \rho(a) = a \otimes 1\}$$

으로 정의된다. 이는 $$A$$의 subalgebra이다.

</div>

Invariant ring의 원소들은 group action에 의해 변하지 않는 대칭성을 포착한다. Coordinate ring $$A$$의 원소를 $$\Spec A$$ 위의 함수로 본다면, 기하적으로 $$A^G$$의 원소들은 각각의 orbit 위에서 상수함수가 된다. 따라서 이들을 가지고 만든 공간 $$\Spec(A^G)$$는 orbit space $$X/G$$의 좋은 근사로 생각할 수 있게 된다. 그러나 문제는 $$A^G$$가 대수적으로 잘 행동하지 않을 수도 있다는 것이다. 

<div class="definition" markdown="1">

<ins id="def15">**정의 15**</ins> Affine algebraic group $$G$$가 *reductive*라는 것은 $$G$$의 모든 유한차원 representation이 completely reducible인 것이다. 즉, 임의의 representation $$V$$가 irreducible representation들의 direct sum으로 분해되는 것이다.

</div>

만일 $$G$$가 reductive group이라면 Hilbert basis theorem과 Nagata theorem을 통해 invariant ring $$A^G$$가 항상 finitely generated라는 것을 보일 수 있으며, 따라서 $$\Spec(A^G)$$가 well-defined affine variety가 된다.

<div class="example" markdown="1">

<ins id="ex16">**예시 16**</ins> 우리가 다루는 대부분의 algebraic group들은 reductive group이다. 

1. *Algebraic torus* $$(\mathbb{C}^\ast)^n$$은 reductive이다.
2. *General linear group* $$\GL(n, \mathbb{C})$$는 reductive이다.
3. *Special linear group* $$\SL(n, \mathbb{C})$$는 reductive이다.
4. *Orthogonal group, Unitary group* $$\operatorname{O}(n)$$, $$\operatorname{U}(n)$$ 등도 reductive이다.

반면, $$\mathbb{G}_a = \mathbb{C}$$는 reductive가 아니다.

</div>

[정의 15](#def15) 이후에 언급한 $$A^G$$의 finite generation에 대한 내용은 보통 Geometric Invariant Theory (GIT)에서 다루던 것으로, 이를 통해 우리는 reductive group action에 대한 quotient를 정의할 수 있다. 

<div class="definition" markdown="1">

<ins id="def17">**정의 17**</ins> Reductive group $$G$$가 affine variety $$X = \Spec(A)$$ 위에 action할 때, *GIT quotient* $$X /\!/ G$$는

$$X /\!/ G = \Spec(A^G)$$

으로 정의된다.

</div>

위에서 살펴본 것과 같이 GIT quotient $$X /\!/ G$$는 기하적으로 orbit space $$X/G$$의 좋은 근사이며, 정확히 이는 다음과 같은 의미이다. 모든 $$G$$-invariant function이 $$X /\!/ G$$로부터 pullback되며, 이는 universal property를 통해 정확히 기술된다.

지금까지의 논의는 affine variety에 대한 것이며, projective variety의 경우 상황이 더 복잡하다. Projective variety $$X \subseteq \mathbb{P}^n$$의 coordinate ring은 graded ring이고, group action이 grading을 보존한다는 보장이 없기 때문이다. 또한 $$\Spec$$ 대신 $$\Proj$$를 사용해야 하므로, affine case와 동일한 접근이 불가능하다.

<div class="definition" markdown="1">

<ins id="def18">**정의 18**</ins> Reductive group $$G$$의 projective variety $$X$$ 위로의 action에 대한 *linearization*이란, 다음을 만족하는 $$G$$의 $$\mathbb{P}^n$$ 위로의 action의 extension이다:

1. $$X \subseteq \mathbb{P}^n$$은 $$G$$-invariant
2. $$\mathbb{P}^n$$ 위의 $$G$$-action이 linear (즉, $$\GL(n+1, \mathbb{C})$$로 lift됨)

</div>

Linearization은 projective case의 어려움을 해결한다. Linear action은 homogeneous coordinate ring의 grading을 보존하므로, 각 차수 $$d$$의 성분 $$A_d$$ 위에 $$G$$가 잘 작용한다. 따라서 $$A_d^G$$를 취할 수 있고, 이를 통해 $$\Proj$$ construction을 사용할 수 있다.

Linearization이 주어지면, 우리는 *stable*과 *semistable* point들을 정의할 수 있다.

<div class="definition" markdown="1">

<ins id="def19">**정의 19**</ins> Linearization이 주어진 $$G$$-action on $$X \subseteq \mathbb{P}^n$$에 대하여:

- 점 $$x \in X$$가 *semistable*이라는 것은 $$\overline{G \cdot x} \cap X^{\mathrm{null}} = \emptyset$$인 것이다. 여기서 $$X^{\mathrm{null}}$$은 invariant homogeneous polynomial들에 의해 정의되는 *null cone*이다.
- 점 $$x \in X$$가 *stable*이라는 것은 다음 조건들을 만족하는 것이다:
  1. $$x$$는 semistable
  2. $$G_x$$는 유한군
  3. Orbit $$G \cdot x$$가 닫힌 집합

Semistable point들의 집합을 $$X^{\mathrm{ss}}$$, stable point들의 집합을 $$X^{\mathrm{s}}$$로 표기한다.

</div>

<div class="definition" markdown="1">

<ins id="def20">**정의 20**</ins> Linearization이 주어진 $$G$$-action on projective variety $$X$$에 대한 *GIT quotient*는

$$X /\!/ G = \Proj\left(\bigoplus_{d \ge 0} A_d^G\right)$$

으로 정의된다. 여기서 $$A_d$$는 $$X$$의 homogeneous coordinate ring의 $$d$$차 성분이다.

</div>

앞서 살펴본 affine case에서와 마찬가지로, projective variety의 GIT quotient 또한 충분히 좋은 근사이다. 이는 다음과 같은 뜻이다. 

1. **잘 정의됨**: Reductive group의 경우 $$A^G$$가 항상 finitely generated이므로 quotient가 존재한다.
2. **Universal property**: 임의의 $$G$$-invariant morphism $$X^{\mathrm{ss}} \to Y$$는 유일한 $$X /\!/ G \to Y$$를 통해 factor한다.
3. **Geometric interpretation**: $$X /\!/ G$$는 semistable point들의 orbit space의 "good" compactification이다. Stable point들의 경우, $$X^{\mathrm{s}} / G \hookrightarrow X /\!/ G$$는 open immersion이다.

---

**참고문헌**

**[Spr]** T. A. Springer, *Linear Algebraic Groups*, Birkhäuser, 1998.  
**[Hum]** J. E. Humphreys, *Linear Algebraic Groups*, Springer, 1975.  
**[Mil]** J. S. Milne, *Algebraic Groups*, Cambridge University Press, 2017.  
**[MFK]** D. Mumford, J. Fogarty, F. Kirwan, *Geometric Invariant Theory*, Springer, 1994.