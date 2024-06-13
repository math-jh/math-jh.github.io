---

title: "모노이드 범주"
excerpt: ""

categories: [Math / Category Theory]
permalink: /ko/math/category_theory/monoidal_categories
header:
    overlay_image: /assets/images/Math/Category_Theory/Monoidal_categories.png
    overlay_filter: 0.5
sidebar: 
    nav: "category_theory-ko"

date: 2024-06-12
last_modified_at: 2024-06-12
weight: 5

---

이번 글에서는 monoidal category와 그 안에서 정의된 monoidal object에 대해 살펴본다. 대략적으로 이야기해서 monoid object란 대수적으로 정의했던 monoid와 비슷한 성질을 갖는 어떤 category의 대상인데, 이 때 monoid와 비슷한 성질을 갖는다는 이야기를 하기 위해서는 이 category가 monoidal category여야 한다. 따라서 우리는 우선 대수적으로 monoid가 어떤 것이었는지를 가볍게 복습한 후, 어떻게 하면 이 이야기를 category의 언어로 바꾸어 쓸 수 있는지를 생각해본다.

## 모노이드

우리는 associative unital magma를 *monoid<sub>모노이드</sub>*라 부르기로 하였다. ([\[대수적 구조\] §준군, 모노이드, 군, ⁋정의 3](/ko/math/algebraic_structures/group#def3)) 이를 풀어 써보자면 $M$이 monoid라는 것은 다음과 같은 뜻이다. 

> $M$ 위에서 정의된 이항연산 $\star:M\times M \rightarrow M$과, $M$의 원소 $e\in M$이 존재하여,
>
> 1. (Associativity) 임의의 $a,b,c\in M$에 대하여 $(a\star b)\star c=a\star(b\star c)$가 성립한다.
> 2. (Unit element) $e\in M$은 임의의 $a\in M$에 대하여, $a\star e=e\star a=a$를 만족한다.

그런데, 이들 조건들은 각각 commutative diagram으로 나타낼 수 있다. 우선 associativity의 경우, 다음 diagram이 commute한다는 것과 같은 뜻이다.

img

이는 당연한 것이, 왼쪽 위에 있는 집합의 임의의 원소 $(a,b,c)$를 뽑아오면, $\urcorner$ 방향으로 진행할 경우에는 

$$\star(\star(a,b),c)=\star(a\star b,c)=(a\star b)\star c$$

를 얻고, 비슷하게 $\llcorner$ 방향으로 진행할 경우에는

$$\star(a,\star(b,c))=\star(a,b\star c)=a\star(b\star c)$$

를 얻는데, 이 diagram이 commute한다는 것이 정확히 이 두 $M$의 원소가 서로 같다는 뜻이기 때문이다.

비슷하게 항등원 $e$의 경우는, 집합 $I=\\{e\\}$와 inclusion $i:I\hookrightarrow M$을 이용하면 다음 diagram

img

이 commute한다는 것으로 쓸 수 있다.

범주론에서는 어떤 대상에서 원소를 뽑아오거나 하는 것이 불가능하다. 따라서 맨 처음 살펴본 monoid의 정의는 범주론을 이용하여 설명하기 부적절하다. 그러나 위와 같이 모든 것을 diagram으로 나타내게 되면, 이를 적당히 범주론의 언어로 올려줄 수 있다. 이를 위해서는 우선 우리가 자연스럽게 사용했던 $M\times M$이 무엇인지부터 정의해야 할 것이다.[^1] 이를 살펴보기 앞서, 우리는 쉬어가는 의미에서 commutative diagram이라는 것도 사실 범주론의 언어로 쓸 수 있다는 것을 살펴본다.


## Diagram

우리는 임의의 preordered set을 category로 볼 수 있다는 것을 살펴보았다. ([§카테고리, ⁋예시 3](/ko/math/category_theory/categories#ex3)) 다음 정의는 이 예시에 새로운 관점을 부여한다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Small category $\mathcal{I}$와 임의의 category $\mathcal{A}$에 대하여, functor $F:\mathcal{I}\rightarrow \mathcal{A}$를 *$\mathcal{I}$-shaped diagram in $\mathcal{A}$*라 부른다.

</div>

Category $\mathcal{A}$가 문맥상 명확할 때는 이를 간단히 $\mathcal{I}$-shaped diagram, 혹은 둘 모두 문맥에 따라 명확할 경우는 이를 그냥 *diagram*이라 부른다. 

앞서 언급한 것과 같이, 이 정의는 특히 $\mathcal{I}$가 preordered set으로부터 나오는 category일 때 특별히 명확한 의미를 갖는다.

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins> 집합 $I_1=\\{a,b,c\\}$와, 다음 관계 $a\leq b\leq c$로 주어진 preorder relation을 생각하자. 그럼 $(I_1,\leq)$로부터 만들어지는 category $\mathcal{I}_1$은 다음 그림

img

으로 표현할 수 있다. 이제 functor $F:\mathcal{I}_1 \rightarrow \mathcal{A}$는 다음 조건

$$F(\beta)\circ F(\alpha)=F(\beta\circ\alpha)=F(\gamma)$$

을 만족한다. 즉, $\mathcal{A}$의 대상 $F(a),F(b),F(c)$와 이들 사이의 morphism $F(\alpha):F(a) \rightarrow F(b)$, $F(\beta):F(b) \rightarrow F(c)$, $F(\gamma): F(a) \rightarrow F(c)$에 대하여 다음 그림

img

이 (이전까지 생각해왔던 의미로서) commutative triangle이 된다. 거꾸로 이러한 조건을 만족하는 데이터는 모두 이와 같은 식으로 $\mathcal{I}_1$으로부터의 functor로 생각할 수 있다.

비슷하게, 집합 $I_2=\\{a,b,c,d\\}$ 위에 다음 관계들 $a\leq b,c$, 그리고 $b,c\leq d$로 preorder relation을 주면 functor $\mathcal{I}_2 \rightarrow \mathcal{A}$는 commutative square가 된다.

</div>


## Bifunctor

다음 정의는 우리가 이미 알고있는 것들로만 이루어져 있긴 하지만, 그래도 이름을 붙여주면 종종 요긴하게 사용할 수 있다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> 세 category $\mathcal{A}, \mathcal{B}, \mathcal{C}$에 대하여, functor $\mathcal{A}\times \mathcal{B}\rightarrow \mathcal{C}$를 *bifunctor*라 부른다.

</div>

<div class="example" markdown="1">

<ins id="ex4">**예시 4**</ins> 임의의 (locally small) category $\mathcal{A}$에 대하여, $\Hom_\mathcal{A}(-,-): \mathcal{A}^\op\times \mathcal{A}\rightarrow \Set$는 bifunctor이다.

이를 확인하기 위해서는 functoriality만 확인하면 충분하다. 정의에 의하여, $\mathcal{A}^\op\times \mathcal{A}$의 morphism은 

$$(g,h):(A_1,A_2) \rightarrow (A_1',A_2');\qquad g\in \Hom_{\mathcal{A}^\op}(A_1,A_1'),\quad h\in \Hom_\mathcal{A}(A_2,A_2')$$

의 꼴이며, bifunctor $\Hom_\mathcal{A}(-,-)$를 통해 이 morphism은 다음 morphism

$$\Hom_\mathcal{A}(g,h):\Hom_\mathcal{A}(A_1,A_2) \rightarrow \Hom_\mathcal{A}(A_1',A_2');\qquad f\mapsto h\circ f\circ g$$

으로 보내진다. 여기에서 $\mathcal{A}'$에서의 morphism $g$를 $\mathcal{A}$에서의 morphism $A_1'\rightarrow A_1$으로 보았다.

</div>

## 모노이드 범주

간단히 말해서, monoidal category란 대상들 사이의 monoid operation, 즉 associative하고 항등원을 가지는 연산이 주어지는 category이다. 얘컨대 우리가 맨 앞에서 monoid를 정의할 때 사용했던 $\times$는 $\Set$을 monoidal category로 만든다는 것을 곧 살펴볼 것이다. 

정의를 하기에 앞서, monoid를 정의하는 두 diagram에서 $M\times(M\times M)$과 $(M\times M)\times M$은 서로 다른 집합이고, $M$, $I\times M$, $M\times I$도 서로 다른 집합이라는 것을 기억하자. 이들은 분명 서로 다른 집합들이며, 다만 이들 사이에 자연스러운 isomorphism들이 존재할 뿐이다. 

<div class="definition" markdown="1">

<ins id="def5">**정의 5 (Monoidal category)**</ins> *Monoidal category<sub>모노이드 범주</sub>*는 데이터 $(\mathcal{A},\otimes, I)$로 이루어진다. 여기서 $\mathcal{A}$는 category이고, $I\in\obj(\mathcal{A})$이며, $\otimes:\mathcal{A}\times \mathcal{A}\rightarrow \mathcal{A}$가 bifunctor이다. 이들은 다음 조건을 만족한다. 

1. $\mathcal{A}\times \mathcal{A}\times \mathcal{A}$에서 $\mathcal{A}$로의 두 functor $-\otimes(-\otimes-)$와 $(-\otimes-)\otimes-$사이의 natural isomorphism
    
    $$\alpha_{A,B,C}:A\otimes(B\otimes C)\rightarrow (A\otimes B)\otimes C$$

    이 존재한다. 이를 *associator*라 부른다.
2. $\mathcal{A}$에서 $\mathcal{A}$로의 세 functor $I\otimes-$, $-\otimes I$, $\id_\mathcal{A}$들 간의 natural isomorphism들

    $$\lambda_A:I\otimes A\rightarrow A,\qquad \rho_A:A\otimes I\rightarrow A$$

    이 존재한다. $\lambda$와 $\rho$를 각각 *left unitor*와 *right unitor*라 부른다.
3. (Coherence condition) 다음 두 diagram이 모두 commute한다.
  - (Associator)
    img
  - (Unitor)
    img

만일 monoidal category $(\mathcal{A},\otimes,I)$에 추가적으로 $\otimes$의 symmetric 조건이 추가되면 이를 *symmetric monoidal category*라 부른다. 이는 natural isomorphism (*symmetor*) $\gamma_{AB}:A\otimes B \rightarrow B\otimes A$과, 다음의 추가적인 coherence diagram

img

그리고

img

으로 나타난다.

</div>

만일 symmetric monoidal category에서, $\gamma_{A,B}:A\otimes B\rightarrow B\otimes A$와 $\gamma_{B,A}:B\otimes A \rightarrow A\otimes B$가 서로의 inverse가 아니라면, 이를 *braided monoidal category*라 부른다.

<div class="proposition" markdown="1">

<ins id="thm6">**정리 6 (Mac Lane's coherence theorem)**</ins> 위의 coherence condition들이 모두 만족된다면, 모든 종류의 

</div>

[^1]: 앞에서 두 category 사이의 곱을 정의한 적은 있어도, 한 category 안에서 두 대상들의 곱은 정의한 적이 없다.