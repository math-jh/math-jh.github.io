---

title: "준층"
excerpt: "위상공간 위에 정의된 준층"

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/presheaves
header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Presheaves.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_geometry-ko"

date: 2023-04-15
last_modified_at: 2023-04-15
weight: 1

---

## 준층

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 위상공간 $X$가 주어졌다 하자. 그럼 이 위에 정의된 *presheaf<sub>준층</sub>* $\mathscr{F}$는 다음과 같은 데이터로 이루어진다.

- 각각의 열린집합 $U\subseteq X$마다, 집합 $\mathscr{F}(U)$가 대응된다.
- 포함관계에 있는 두 열린집합 $U\subseteq V$마다 집합 사이의 함수 $\rho_{VU}:\mathscr{F}(V)\rightarrow\mathscr{F}(U)$가 대응된다.

이들은 다음 조건을 만족해야 한다.

1. 임의의 열린집합 $U\subseteq X$에 대하여, $\rho_{UU}:\mathscr{F}(U)\rightarrow\mathscr{F}(U)$는 항등함수 $\operatorname{id}_{\mathscr{F}(U)}$이다.
2. 포함관계에 있는 세 열린집합 $U\subseteq V\subseteq W$에 대하여, $\rho_{WU}=\rho_{VU}\circ\rho_{WV}$이 성립한다.

이 때, $\mathscr{F}(U)$의 원소들을 $U$ 위에서의 *section*이라 부르고, $\rho$들을 *restriction map*이라 부른다. 

</div>

위상공간 $(X,\mathscr{T})$가 주어졌다 하자. 카테고리 $\Top(X)$를 

- $\obj(\Top(X))=\mathscr{T}$,
- 임의의 $U,V\in\obj(\Top(X))$에 대하여 
  
  $$\Mor_{\Top(X)}(U,V)=\begin{cases}U\hookrightarrow V&\text{if $U\subseteq V$,}\\\emptyset&\text{otherwise.}\end{cases}$$

으로 정의한다. 그럼 $X$ 위에 presheaf를 정의하는 것은 정확하게 contravariant functor $\mathscr{F}:\Top(X)\rightarrow\Set$을 생각하는 것과 같다. 따라서 위의 [정의 1](#def1)에서, $\mathscr{F}(U)$를 집합이 아닌 abelian group이나 ring 등으로 바꿀 경우, $\mathscr{F}$를 $\Top(X)$에서 $\Ab$, $\Ring$으로의 contravariant functor로 취급할 수 있다. 그러나 presheaf와 sheaf에 대한 기본적인 성질을 살펴볼 때에는 이러한 대수적인 구조를 사용할 일이 없으므로, 우선은 이러한 차이에 관심을 두지 않는다.

한편, $\mathscr{F}(U)$들의 모임은 directed system을 이룬다. ([\[집합론\], §극한, ⁋정의 12](/ko/math/set_theory/limits#def12)) 이를 확인하기 위해, $\mathscr{T}$ 위에 순서관계 $\leq$를

$$V\leq U\iff U\subseteq V$$

으로 정의하자.[^1] 그럼 임의의 $U,V\in\mathscr{T}$에 대하여, $U,V\leq U\cap V$이므로 $(\mathscr{T},\leq)$는 right directed set이다. 또, [정의 1](#def1)에서 restriction map들에 대한 두 조건은 정확히 다음 데이터

$$\bigl((\mathscr{F}(U))_{U\in\mathscr{T}},(\rho_{VU})_{V\leq U}\bigr)$$

가 directed system임을 보여준다. 따라서 이 directed system의 direct limit ([\[집합론\], §극한, ⁋정의 13](/ko/math/set_theory/limits#def13))이 잘 정의된다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> 위상공간 $X$ 위에서 정의된 presheaf $\mathscr{F}$를 생각하자. 임의의 점 $p\in X$에 대하여, 점 $p$에서의 *stalk<sub>줄기</sub>* $\mathscr{F}_p$를

$$\mathscr{F}_p=\varinjlim_{p\in U}\mathscr{F}(U)$$

으로 정의한다. $\mathscr{F}_p$의 원소들을 점 $p$에서의 *germ<sub>싹</sub>*이라 부른다.

</div>

[\[집합론\], §극한, ⁋정의 13](/ko/math/set_theory/limits#def13) 이후에 소개한 $\varinjlim\mathscr{F}(U)$의 construction을 생각하면, 

$$\mathscr{F}_p=\{(f,U):p\in U\in\mathscr{T},f\in\mathscr{F}(U)\}/\mathnormal{\sim}$$

임을 알 수 있다. 여기서 $\sim$은 

$$(f,U)\sim(g,V)\iff\text{$\exists$ open neighborhood $W\subseteq U\cap V$ of $p$ satisfying $\rho_{UW}(f)=\rho_{VW}(g)$}$$

을 통해 정의되는 동치관계이다. 

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> 위상공간 $X$가 주어졌다 하고, 이 위에 두 presheaf $\mathscr{F},\mathscr{G}$가 주어졌다 하자. 그럼 $\mathscr{F}$에서 $\mathscr{G}$로의 *presheaf morphism<sub>준층 사상</sub>* $\phi:\mathscr{F}\rightarrow\mathscr{G}$는 $U\hookrightarrow V$일 때마다 다음 diagram

![presheaf_morphism](/assets/images/Math/Algebraic_Geometry/Presheaves-1.png){:width="186.15px" class="invert" .align-center}

을 commute하도록 하는 함수들의 모임 $(\phi(U))_{U\in\mathscr{T}}$이다. $X$ 위에서 정의된 presheaf들 $\mathscr{F}:X\rightarrow\mathscr{C}$를 object로, presheaf morphism들을 morphism으로 갖는 category를 $\PSh(X,\mathscr{C})$으로 표기한다.

</div>

Presheaf $\mathscr{F}$를 $\Top(X)$에서 $\Set$으로의 contravariant functor로 본다면, presheaf morphism은 별다른 것이 아니라 두 functor $\mathscr{F},\mathscr{G}$ 사이의 natural transformation에 불과하다. 

한편, presheaf를 direct system

$$\bigl((\mathscr{F}(U))_{U\in\mathscr{T}},(\rho_{VU})_{V\leq U}\bigr)$$

으로 생각한다면, 위의 [정의 3](#def3)은 presheaf morphism이 directed system 사이의 함수라는 의미가 된다. [\[집합론\], §극한](/ko/math/set_theory/limits)에서는 direct limit에 대한 정리를 거의 소개하지 않았지만, [\[집합론\], §극한, ⁋정의 7](/ko/math/set_theory/limits#def7)과 [\[집합론\], §극한, ⁋명제 8](/ko/math/set_theory/limits#prop8)을 direct system에 맞도록 적절히 변형하면 다음 명제를 얻는다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> 위상공간 $X$ 위에 정의된 presheaf들 사이의 morphism $\phi:\mathscr{F}\rightarrow\mathscr{G}$가 주어졌다 하자. 그럼 임의의 $p\in X$에 대하여, stalk들 사이의 함수 $\phi_p:\mathscr{F}_p\rightarrow\mathscr{G}_p$가 자연스럽게 유도된다.

</div>

## Abelian presheaf

지금까지 우리는 presheaf가 어떤 카테고리에서 값을 갖는지를 무시해왔는데, 이제 우리는 특별히 카테고리 $\Ab$에서 값을 갖는 presheaf들을 살펴본다. 카테고리 $\mathbf{Ab}$는 특히 diagram chasing을 할 수 있다는 점에서, 즉 abelian category라는 점에서 특별하다. ([\[범주론\] §아벨 카테고리, ⁋정의 7](/ko/math/category_theory/abelian_categories#def7))

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> 위상공간 $X$에 대하여, contravariant functor $\Top(X)\rightarrow\Ab$을 *abelian presheaf*라 부른다.

</div>

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> 위상공간 $X$ 위에 정의된 abelian presheaf들 사이의 morphism $\phi:\mathscr{F}\rightarrow\mathscr{G}$가 주어졌다 하자. 그럼 $\phi$의 *presheaf kernel<sub>핵 준층</sub>* $\ker\phi$는 

- 각각의 열린집합 $U\subseteq X$마다, $U\mapsto \ker(\phi(U))$
- 포함관계에 있는 두 열린집합 $U\subseteq V$마다 다음의 diagram
  
  img

  을 통해 유일하게 결정되는 restriction map $\rho_{VU}:\ker(\phi(V))\rightarrow\ker(\phi(U))$

으로 이루어진 데이터이다.

</div>

이 정의에서, $\rho_{VU}$는 $\ker(\phi(U))$의 universal property로부터 유일하게 결정되는 restriction map이다.

<div class="proposition" markdown="1">

<ins id="lem7">**보조정리 7**</ins> 위에서 정의한 $\ker\phi$는 $X$ 위에서의 (abelian) presheaf이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

다음의 두 diagram

img

와 kernel의 universal property에 의해 자명하다. 

</details>

이와 마찬가지 방법으로, *presheaf cokernel*, *presheaf image*, *presheaf coimage* 혹은 *presheaf quotient* 등등을 모두 정의할 수 있다. 두 presheaf $\mathscr{F},\mathscr{G}$의 coproduct $\mathscr{F}\oplus\mathscr{G}$는 $U\mapsto \mathscr{F}(U)\times\mathscr{G}(U)$으로 정의된다. 

a

[^1]: Functor $\mathscr{F}$가 contravariant이기 때문에, 어디에선가는 포함관계를 반대로 뒤집어주어야 한다.