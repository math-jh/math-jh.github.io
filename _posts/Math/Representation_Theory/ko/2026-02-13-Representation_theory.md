---

title: "유한군의 표현론"
excerpt: ""

categories: [Math / Representation Theory]
permalink: /ko/math/representation_theory/representations_of_finite_groups
header:
    overlay_image: /assets/images/Math/Representation_Theory/Representations_of_finite_groups.png
    overlay_filter: 0.5
sidebar: 
    nav: "representation_theory-ko"

date: 2026-02-13
last_modified_at: 2026-02-13
weight: 1

---

일반적으로 그 구조가 복잡한 수학적인 대상을 다룰 때 좋은 전략 중 하나는 이 대상이 다른 단순한 대상 위에 어떻게 작용하는지를 보는 것이다. 이 카테고리에서 우리는 표현론, 그 중에서도 finite group의 표현론에 대해 살펴본다. 

## 표현론의 기본 개념들

우선 다음의 정의부터 시작하자. 

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 임의의 finite group $G$에 대하여, $G$의 *representation<sub>표현</sub>*은 벡터공간 $V$와, group action의 조건을 만족하는 함수

$$\rho: G\times V \rightarrow V$$

가 주어져서 각각의 $\rho(g,-)$가 linear map인 것이다.

</div>

일반적으로 ground field $\mathbb{K}$는 임의의 ring $A$로 대체해도 아무런 문제는 없지만, 우리의 논의에서는 $\mathbb{K}=\mathbb{C}$로 두어도 충분하므로 이렇게 고정하기로 한다. 또, 우리는 주로 *유한차원* 벡터공간 $V$를 representation space로 갖는 경우를 생각한다.

위의 정의는 간략하게 $G\rightarrow\Aut(V)$가 주어진 것으로 생각할 수 있다. 우리는 $\rho(g,-): V\rightarrow V$



우리는 주로 표기 $\rho(g,v)$ 대신 $g\cdot v$와 같은 표현을 쓰기도 하고, 

혹은, 더 간략하게 group homomorphism $G\rightarrow \Aut(V)$가 주어진 것으로 생각할 수도 있다. 우리는 편의를 위해 함수 $\rho$가 문맥에 따라 명확하다면 $V$를 $G$의 representation이라 부르기도 한다. 






고정된 (finite) group $G$와 $G$의 두 representation 사이의 morphism은 $G$-equivariant map들, 즉 다음의 diagram

![G-equivariant_maps](/assets/images/Math/Representation_Theory/Representations_of_finite_groups-1.png){:style="width:10em" class="invert" .align-center}

으로 주어진다. 이들의 합성이 잘 행동하는 것은 자명하므로, 고정된 group $G$에 대하여 $G$의 representation들의 category $\Rep_\mathbb{C}(G)$가 존재한다. 

한편 $V$에 적용되는 선형대수학의 언어를 차용하면 다음을 정의할 수 있다. 

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> Group $G$의 representation $G\times V\rightarrow V$에 대하여 다음을 정의한다. 

1. $V$의 subspace $W$가 *$G$-invariant<sub>$G$-불변공간</sub>*라는 것은 임의의 $g\in G$와 임의의 $w\in W$에 대하여 $g\cdot w\in W$가 항상 성립하는 것이다.
2. 임의의 $G$-invariant subspace $W$에 대하여, representation $G\times W\rightarrow W$를 $V$의 *subrepresentation<sub>부분표현</sub>*이라 부른다. 
3. 만일 $V$가 zero representation이 아니고 $V$의 subrepresentation들이 trivial subrepresentation들, 즉 자기 자신과 $G\times\\{0\\}\rightarrow\\{0\\}$ 뿐이라면 $V$를 *irreducible representation<sub>기약표현</sub>*이라 부른다. 

</div>

임의의 representation $G\rightarrow \Aut(V)$가 주어졌을 때, 우리는 $G$-fixed point들의 집합

$$V^G=\{v\in V\mid g\cdot v=v\text{ for all $g\in G$}\}$$

이 $G$-invariant subspace임을 안다. 따라서 representation $G\rightarrow \Aut(V)$이 irreducible representation이기 위해서는 $V^G=V$이거나 $V^G=\\{0\\}$이어야 한다. 그런데 $V^G=V$이라면, $V$의 임의의 subspace가 $G$-invariant일 것이므로 $G\rightarrow \Aut(V)$가 irreducible representation이기 위해서는 $V^G=\\{0\\}$이거나 $V$가 $1$차원이어야 한다. 

이 $G$-fixed point set $V^G$은 주어진 $G$-representation $V$로부터 새로운 $G$-representation을 얻어내는 하나의 방법이다. 이 외에도 주어진 $G$-representation들로부터 새로운 $G$-representation을 구성하는 방법들이 여럿 존재한다. 가령 선형대수의 각종 construction들을 생각하고, 그 위에 $G$-action을 정의해주면 다음을 얻는다. 

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> $G$-representation $V, W$에 대하여, 다음의 $G$-action을 통해 새로운 $G$-representation들을 정의한다.

1. Direct sum $V\oplus W$; $G$-action $g\cdot(v,w)=(g\cdot v,g\cdot w)$
2. Tensor product $V\otimes W$; $G$-action $g\cdot(v\otimes w)=(g\cdot v)\otimes (g\cdot w)$
3. $\Hom_\mathbb{C}(V,W)$; $G$-action $(g\cdot f)(v)=g\cdot f(g^{-1}\cdot v)$
4. 3번에서 $W=\mathbb{C}$로 두어 얻어지는 *dual representation* $V^\ast$
5. 스칼라곱을 conjugate으로 바꾸어 얻어지는 *conjugate representation* $\overline{V}$
6. 그 외 exterior power $\bigwedge^k V$, symmetric power $\operatorname{Sym}^k V$ 등에도 자연스럽게 정의되는 $G$-action들.

</div>

이러한 construction들을 체계적으로 다루기 위해서는 group algebra의 언어가 유용하다. ([\[대수적 구조\] §대수, ⁋정의 5](/ko/math/algebraic_structures/algebras#def5)) 이를 간단히 리뷰하자면 집합으로서 $\mathbb{C}[G]$는 $G$에서 $\mathbb{C}$로의 함수들의 모임이었다. 각각의 $x\in G$에 대하여 $\delta_x:G\rightarrow \mathbb{C}$를

$$\delta_x(y)=\begin{cases}1&\text{if $y=x$}\\0&\text{otherwise}\end{cases}$$

으로 정의하면, 임의의 $f\in\mathbb{C}[G]$는 

$$f=\sum_{x\in G}f(x)\delta_x$$

로 나타낼 수 있으므로 $\delta_x$들이 $\mathbb{C}[G]$의 basis를 이룬다. 우리가 다룰 $\mathbb{C}[G]$가 단순히 $G$에서 $\mathbb{C}$로의 함수들이 이루는 ring과 같지 않은 부분은 이 위에 정의된 곱셈이다. 두 함수 $f,g$의 곱셈을

$$(fg)(x)=f(x)g(x), \qquad \text{for all $x\in G$}$$

으로 정의하는 대신 이 위에는 convolution product

$$(f\ast g)(x)=\sum_{y\in G}f(y)g(y^{-1}x)$$

가 곱셈을 정의한다. 만일 우리가 위의 delta function $\delta_x$와 $x\in G$를 identify한다면, 다음의 식

$$\left(\sum_{x\in G}f(x)\cdot x\right)\left(\sum_{y\in G} g(y)\cdot y\right)=\sum_{x,y\in G} f(x)g(y) \cdot(xy)=\sum_{z\in G}\left(\sum_{x\in G} f(x)g(x^{-1}z)\right)\cdot z$$

이 성립하므로 이러한 곱셈을 선택하는 것이 자연스럽다. 가령 $\delta_x$와 $\delta_y$의 곱은 $0$이지만, 이 둘의 convolution은 $\delta_{xy}$이므로, group action에 포함되는 다음의 식

$$(\delta_x\ast \delta_y)\cdot v=\delta_x\cdot(\delta_y\ast v)$$

와 같은 것들이 말이 되기 위해서는 이러한 선택이 필연적이다.

임의의 $G$-representation $\rho:G\rightarrow \Aut(V)$에 대하여, 다음의 식

$$\widetilde{\rho}\left(\sum_{x\in G} a_x x, v\right)= \sum_{x\in G} a_x\rho(x)v$$

은 $V$ 위에 $\mathbb{C}[G]$-module 구조를 준다. 거꾸로 임의의 $\mathbb{C}[G]$-module $V$가 주어졌다 하면, 각 $x\in G$에 대하여 $x$가 $V$에 작용하는 방식을 통해 $G$-representation을 얻을 수 있다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> 위의 대응들은 categorical equivalence

$$\Rep_\mathbb{C}(G)\cong \lMod{\mathbb{C}[G]}$$

을 준다.

</div>

약간의 abuse of language를 통해 우리는 $\mathbb{C}[G]$-module을 간단히 $G$-module이라 부르기도 한다. 근본적으로 임의의 $x\in G$가 임의의 $v\in V$를 어디로 옮기는지만 알면 위의 식을 통해 $\mathbb{C}[G]$-action이 결정된다는 점에서 이 명칭은 상당히 적절하다고 할 수 있다. 

실제로 위에서 논의한 대부분의 것들이 이 categorical equivalence로 설명될 수 있다. 가령 임의의 $G$-representation $V$에 대하여, $V$의 subrepresentation은 $V$의 $G$-submodule (정확히는 $\mathbb{C}[G]$-submodule)이다. 또, [정의 3](#def3)의 tensor product도 납득할만한데, 일반적으로 coproduct $\Delta:A\rightarrow A\otimes A$가 주어진 $\mathbb{K}$-algebra $A$와 두 $A$-module $M,N$에 대하여 이들의 텐서곱을 정의하기 위해서는 $\Delta$를 활용하여 

$$A\otimes (M\otimes N)\rightarrow (A\otimes A)\otimes (M\otimes N)\rightarrow (A\otimes M)\otimes (A\otimes N)\rightarrow M\otimes N$$

을 사용해야 하고, 이 때 사용하는 coproduct $A\rightarrow A\otimes A$이 $\mathbb{C}[G]$의 경우에는 

$$\mathbb{C}[G]\rightarrow \mathbb{C}[G]\otimes \mathbb{C}[G]$$

이기 때문이다. 그럼 마찬가지로 [정의 3](#def3)에서 정의한 $\Hom$이 이 $\otimes$와 adjunction 관계에 있고, 따라서 $\Rep_G(\mathbb{C})$를 closed monoidal category로 만드는 것 또한 보일 수 있다. 

특별히 $G$의 subrepresentation과 $\mathbb{C}[G]$-submodule이 같은 것이라는 것을 생각하면, $V$가 irreducible representation인 것은 $V$가 *simple* $\mathbb{C}[G]$-module인 것과 같다. 