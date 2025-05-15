---

title: "분해가능확대체"
excerpt: ""

categories: [Math / Field Theory]
permalink: /ko/math/field_theory/separable_extensions
header:
    overlay_image: /assets/images/Math/Field_Theory/Separable_extensions.png
    overlay_filter: 0.5
sidebar: 
    nav: "field_theory-ko"

date: 2025-05-15
last_modified_at: 2025-05-15
weight: 6

---

이제 우리는 separable extension의 개념을 정의한다. 우선 이전 글에서 살펴본 étale algebra의 characterization을 살펴볼 것이다. 

<div class="proposition" markdown="1">

<ins id="lem1">**보조정리 1**</ins> Algebraically closed field $\mathbb{K}$에 대하여, finite degree의 commutative $\mathbb{K}$-algebra $A$가 $\Omega_{A/\mathbb{K}}=0$을 만족한다 하자. 그럼 $A$의 임의의 maximal ideal $\mathfrak{m}$에 대하여, $\mathfrak{m}=\mathfrak{m}^2$이 성립한다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

Field $A/\mathfrak{m}$는 algebraically closed field $\mathbb{K}$의 finite degree extension이므로, 이는 반드시 algebraic extension이고 따라서 $[A/\mathfrak{m}:\mathbb{K}]=1$이다. 따라서 각각의 $a\in A$에 대하여 우리는 $a-\lambda\in \mathfrak{m}$이도록 하는 $\lambda\in \mathbb{K}$를 찾을 수 있다. 그럼 다음의 식

$$A \rightarrow \mathfrak{m}/\mathfrak{m}^2;\qquad a\mapsto a-\lambda)$$

으로 정의된 함수 $D:A \rightarrow \mathfrak{m}/\mathfrak{m}^2$이 $\mathbb{K}$-derivation이 되는 것이 자명하다. 이제 [\[다중선형대수학\] §미분가군, ⁋명제 8](/ko/math/multilinear_algebra/differential_modules#prop8)의 universal property로부터 $D$는 반드시 $\Omega_{A/\mathbb{K}}$를 factor through 해야 하고, 가정에 의해 이것이 $0$이므로 $D=0$이어야 한다. 

</details>

Étale algebra에 대한 우리의 characterization을 위해서는 위의 보조정리의 결과로부터 출발하는 다음의 보조정리를 보여야 한다. 

<div class="proposition" markdown="1">

<ins id="lem2">**보조정리 2**</ins> Commutative ring $A$의 finitely generated ideal $\mathfrak{a}$가 $\mathfrak{a}=\mathfrak{a}^2$를 만족한다면 적당한 idempotent $e\in A$가 존재하여 $\mathfrak{a}=Ae$이도록 할 수 있다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $\mathfrak{a}$의 generator를 $a_1,\ldots,a_n$이라고 하자. 그럼 $
\mathfrak{a}=\mathfrak{a}^2$이므로 각각의 $i$에 대하여 다음의 식

$$a_i=\sum_{j=1}^r x_{ij}a_j$$

이 성립하도록 하는 $x_{ij}$들이 존재한다. 이렇게 만들어진 $r\times r$ 행렬에 대하여, $I_r-(x_{ij})$를 $M$이라 하자. 그럼 $M$의 adjoint matrix를 통해 다음의 식

$$NM=(\det M) I_r$$

이 성립하도록 하는 $r\times r$ 행렬 $N$이 존재한다. 이제 양 변에서 $a_j$에 해당하는 열벡터가 어디로 가는지를 계산해보면 우리는 반드시 $(\det M)a_j=0$이 모든 $j$에 대해 성립해야 하는 것을 알고, 따라서 $(\det M)\mathfrak{a}=0$이 성립한다. 

한편, 행렬 $M$은 그 정의에 의하여 $\mathfrak{a}$로 자른 후에는 $I_r$이 되며, 따라서 그 행렬식 $\det M$ 또한 (modulo $\mathfrak{a}$로) $1$이 된다. 이제 $e=1-D$로 두면 $e$가 원하는 idempotent가 된다. 

</details>

그럼 étale algebra에 대한 differential characterization은 다음과 같이 주어진다. 

<div class="proposition" markdown="1">

<ins id="thm3">**정리 3**</ins> Finite degree commutative $\mathbb{K}$-algebra $A$에 대하여, $A$가 étale인 것과 $\Omega_{A/\mathbb{K}}=0$인 것이 동치이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $\Omega_{A/\mathbb{K}}$와 étale algebra의 개념은 base change에 대해 잘 행동하므로 우리는 $\mathbb{K}$가 algebraically closure라 가정해도 된다. 더 정확히 말해, $A$가 étale인 것은 $\mathbb{K}$의 algebraic closure $\overline{\mathbb{K}}$에 대해 $\overline{\mathbb{K}}$-algebra $A_{(\overline{\mathbb{K}})}=A\otimes_\mathbb{K}\overline{\mathbb{K}}$이 diagonalizable인 것과 동치이며 ([§에탈대수, ⁋명제 8](/ko/math/field_theory/etale_algebras#prop8), 한편 [\[다중선형대수학\] §미분가군, ⁋명제 12](/ko/math/multilinear_algebra/differential_modules#prop12)의 canonical isomorphism과 $\overline{\mathbb{K}}$-algebra $A_{(\overline{\mathbb{K}})}$의 정의에 의하여 다음의 isomorphism

$$\Omega_{A_{(\overline{\mathbb{K}})}/\overline{\mathbb{K}}}\cong \Omega_{A/\mathbb{K}}\otimes_A A_{(\overline{\mathbb{K}})}=\Omega_{A/\mathbb{K}}\otimes_A A\otimes_\mathbb{K}\overline{\mathbb{K}}\cong \Omega_{A/\mathbb{K}}\otimes_\mathbb{K}\overline{\mathbb{K}}$$

을 얻고, 따라서 $\Omega_{A/\mathbb{K}}=0$인 것과 $\Omega_{A_{(\overline{\mathbb{K}})}/\overline{\mathbb{K}}}=0$인 것이 동치이다. 즉, 주어진 정리를 증명하는 것은 $\mathbb{K}$가 algebraically closed라 가정하고, $A$가 diagonalizable인 것과 $\Omega_{A/\mathbb{K}}=0$인 것이 동치임을 보이면 된다. 

우선 $A$가 diagonalizable이라 가정하면, $A$는 [§에탈대수, ⁋명제 6](/ko/math/field_theory/etale_algebras#prop6)의 둘째 조건에 의하여 idempotent들로 생성된다. 그런데 임의의 idempotent $e$에 대하여, Leibniz rule을 생각하면

$$d(e)=d(e^2)=ed(e)+ed(e)=2ed(e)$$

이고 양 변에 $e$를 곱하면 $ed(e)=0$이어야 하므로, 이를 다시 위에 대입하면 $de=0$이어야 함을 안다. 한편 명시적으로 $\Omega_{A/\mathbb{K}}$는 이러한 원소들 $de$로 생성되는 free module에 적절한 relation들로 자른 것으로 나타나므로 ([\[다중선형대수학\] §미분가군, ⁋예시 10](/ko/math/multilinear_algebra/differential_modules#ex10)) 이로부터 $\Omega_{A/\mathbb{K}}=0$이어야 함을 안다. 

이제 거꾸로 $\Omega_{A/\mathbb{K}}=0$이라 가정하고 $A$가 diagonalizable임을 보이자. $A$의 degree에 대한 귀납법으로 진행하며, degree $1$인 경우는 자명하다. 이제 일반적인 경우에 $A$의 maximal ideal $\mathfrak{m}$을 하나 택하자. 그럼 [보조정리 1](#lem1)에 의하여 $\mathfrak{m}=\mathfrak{m}^2$이고, 따라서 [보조정리 2](#lem2)를 적용하면 $\mathfrak{m}=Ae$이도록 하는 idempotent $e$를 찾을 수 있다. 한편, 이로부터 $A$를 $\mathfrak{a}=(1-e)A$와 $\mathfrak{m}$의 direct sum으로 쪼개놓으면  $\mathbb{K}$가 algebraically closed라는 가정으로부터 extension $A/\mathfrak{m}$이 degree $1$이어야 함을 안다. 즉, 이 direct sum을 

$$A\cong \mathfrak{a}\oplus\mathfrak{m}\cong \mathbb{K}\times A/\mathfrak{a}$$

으로 적을 수 있다. 이제 $\Omega$가 right exact functor이므로 ([\[다중선형대수학\] §미분가군, ⁋명제 13](/ko/math/multilinear_algebra/differential_modules#prop13)) $\Omega_{(A/\mathfrak{a})/\mathbb{K}}$는 $\Omega_{A/\mathbb{K}}=0$의 quotient가 되어 $0$이다. 따라서, $A/\mathfrak{a}$는 귀납적 가정에 의하여 diagonalizable이고, 이를 $\mathbb{K}$와 곱한 $A$ 또한 마찬가지이다. 

</details>

앞서 우리는 [§제곱근확대체, ⁋예시 9](/ko/math/field_theory/radical_extensions#ex9)에서, 갈루아 이론을 전개할 때 문제가 될 수 있는 상황을 살펴보았었는데, 