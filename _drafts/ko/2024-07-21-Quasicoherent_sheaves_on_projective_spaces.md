---

title: "사영스킴 위에 정의된 준연접층"
excerpt: ""

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/quasicoherent_sheaves_on_projective_spaces
header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Quasicoherent_sheaves_on_quasicoherent_sheaves.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_geometry-ko"

date: 2024-07-21
last_modified_at: 2024-07-21
weight: 11

---





## 준연접층의 성질들

이제 우리는 quasicoherent sheaf 및 coherent sheaf들의 성질을 살펴본다. 

가장 처음으로 살펴봐야 할 것은 다음의 정리이다. 

<div class="proposition" markdown="1">

<ins id="thm8">**정리 8**</ins> $\QCoh(X)$와 $\Coh(X)$는 abelian category이다.

</div>

물론 언제나와 같이, $\Coh(X)$의 경우 $X$는 noetherian인 것을 가정하고 있다. 뿐만 아니라, 앞서 [§준연접층](/ko/math/algebraic_geometry/quasicoherent_sheaves)에서 정의했던 $f^\ast$나 $f_\ast$에 대해서도 이들이 잘 행동한다. 

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> Scheme morphism $f:X \rightarrow Y$가 주어졌다 하자. 

1. $f^\ast$는 $\QCoh(Y)$에서 $\QCoh(X)$로의 functor이며, 만일 $X,Y$가 모두 noetherian이라면 이는 $\Coh(Y)$에서 $\Coh(X)$로의 functor이기도 하다. 
2. 만일 $X$가 noetherian이거나, $f$가 quasicompact, separated라면 $f_\ast$는 $\QCoh(X)$에서 $\QCoh(Y)$로의 functor이다. 

</div>

## Closed subscheme

<div class="definition" markdown="1">

<ins id="def10">**정의 10**</ins> Scheme $X$와 closed subscheme $i:Y\hookrightarrow X$를 생각하자. 그럼 $\ker i^\sharp$를 $Y$의 *ideal sheaf<sub>아이디얼 층</sub>*이라 부르고 $\mathscr{I}\_Y$ 혹은 $\mathscr{I}\_{Y/X}$와 같이 적는다. 

</div>

그럼 다음이 성립한다. 

<div class="proposition" markdown="1">

<ins id="prop11">**명제 11**</ins> 위와 같은 상황에서 $\mathscr{I}_Y\in\QCoh(X)$가 성립한다. 거꾸로 만일 $\mathscr{I}\in\QCoh(X)$가 $X$ 위에 정의된 ideal들의 quasicoherent sheaf라면 이것이 유일하게 $X$의 closed subscheme을 정의한다. 

</div>

## 세르 뒤틀림 층

이제 우리의 관심을 좁혀서 projective scheme 위에 정의된 quasicoherent sheaf들에 대해 살펴본다. 물론 projective scheme은 일단 scheme이므로 앞서 논의한 것들이 모두 적용되긴 하지만, 처음 projective scheme은 $\Proj$ functor를 통해 graded ring으로부터 만들어졌었으므로 대수적인 설명을 조금 더 할 수 있어야 할 것이다. 즉, 우리는 quasicoherent sheaf를 처음 정의할 때처럼, 임의의 graded ring $S$와 graded $S$-module $M$으로부터 시작해서 $\Proj S$ 위의 quasicoherent sheaf를 정의할 것이다. 

Graded ring $S^\bullet$이 주어졌다 하고, graded $S^\bullet$-module $M^\bullet$을 생각하자. 그럼 각각의 $\mathfrak{p}\in\Proj(S^\bullet)$에 대하여, [§스킴, §§사영스킴](/ko/math/algebraic_geometry/schemes#사영스킴)에서 정의한 것과 마찬가지로 $M_{(\mathfrak{p})}$를 정의하고, 이를 통해 $\widetilde{M}(U)$를 정의할 수 있다. 

<div class="proposition" markdown="1">

<ins id="prop1">**명제 1**</ins> 위와 같은 상황에서, 다음이 성립한다. 

1. 임의의 $\mathfrak{p}\in\Proj S^\bullet$에 대하여 $\widetilde{M}\_{\mathfrak{p}}\cong M\_{(\mathfrak{p})}$이 성립한다. 
2. 임의의 homogeneous element $f\in A$에 대하여, [§스킴, ⁋명제 6](/ko/math/algebraic_geometry/schemes#prop6)의 두 번째 결과의 isomorphism은 $\widetilde{M}\vert_{D_+(f)}\cong(M_{(f)})^\sim$을 유도한다. 
3. $\widetilde{M}$은 quasicoherent sheaf이며, 만일 $S^\bullet$이 noetherian이고 $M$이 finitely generated라면 $\widetilde{M}$은 coherent이다. 

</div>

한편, projective scheme들의 경우에는 특별한 sheaf들이 존재한다. 표기의 편의를 위해 $X=\Proj(S^\bullet)$이라 하자. 

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> 여전히 위와 같은 상황에서, sheaf $\mathscr{O}\_X(n)$을 $S(n)^\sim$으로 정의한다. 이 때 $\mathscr{O}(1)$을 *Serre twisting sheaf<sub>세르 뒤틀림 층</sub>*이라 부른다. 더 일반적으로, $X$ 위에 정의된 임의의 $\mathscr{O}_X$-module $\mathscr{F}$에 대하여 $\mathscr{F}(n)=\mathscr{F}\otimes\_{\mathscr{O}_X}\mathscr{O}\_X(n)$으로 정의한다. 

</div>

더 일반적으로, 임의의 scheme $Y$에 대해서, $\mathbb{P}^r_Y$의 twisting sheaf $\mathscr{O}(1)$을 $\mathbb{P}^r_\mathbb{Z}$ 위에 정의된 $\mathscr{O}(1)$의 pullback으로 정의한다. 

그럼 다음이 성립한다. 

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> 위와 같은 상황에서, $S$가 $S_0$-algebra로서 $S^1$에 의해 생성된다 가정하자. 그럼 다음이 성립한다.

1. $\mathscr{O}_X(n)$은 $X$ 위에 정의된 rank 1 locally free $\mathscr{O}_X$-module이다.
2. 임의의 graded $S$-module $M$에 대하여, $\widetilde{M}(n)\cong(M(n))^\sim$이고 특히, $\mathscr{O}_X(n)\otimes \mathscr{O}_X(m)\cong \mathscr{O}_X(m+n)$이 성립한다. 
3. $T$가 $S$와 동일한 조건을 만족하는 graded ring이고, $\phi:S \rightarrow T$가 degree-preserving homomorphism이라 하자. 그럼 $\phi$에 의해 유도되는 scheme morphism $f:U \rightarrow \Proj T$에 대하여, $f^\ast(\mathscr{O}\_X(n))\cong \mathscr{O}\_Y(n)\vert\_U$이고 $f\_\ast(\mathscr{O}\_Y(n)\vert\_U)\cong (f\_\ast \mathscr{O}\_U)(n)$이다. 

</div>

한편, [§스펙트럼, ⁋명제 5](/ko/math/algebraic_geometry/spectrums#prop5)의 세 번째 조건에서 우리는 affine scheme으로부터 그를 정의하는 ring을 복원하는 방법을 알고 있다. 이는 그냥 global section functor $\Gamma(\Spec A,-)$를 취하면 된다. 반면, 예를 들어 $\mathbb{P}^n$과 같은 경우에는 global section이 없기 때문에, $\Gamma$를 통해 global section을 복원해올 수 없다. 이는 $\Gamma$가 볼 수 있는 것은 degree zero part 뿐이기 때문인데, 위의 과정을 통해 degree를 다시 매겨주면 원래의 ring을 복원해줄 수 있다. 

즉, 다음을 정의하자. 

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> $X=\Proj S^\bullet$과 $\mathscr{F}\in \lMod{\mathscr{O}_X}$에 대하여, 

$$\Gamma_\bullet(\mathscr{F})=\bigoplus_{n\in \mathbb{Z}}\Gamma(X, \mathscr{F}(n))$$

으로 정의하자. 각각의 $s\in S^d=S(d)^0$은 $\Gamma(X, \mathscr{O}_X(d))$의 원소를 결정해주므로, 다음 식

$$\Gamma(X, \mathscr{O}_X(d)\otimes_{\Gamma(X, \mathscr{O}_X)} \Gamma(X, \mathscr{F}(n)) \rightarrow \Gamma(X, \mathscr{F}(n+d));\qquad (s, t)\mapsto st$$

를 통해 $\Gamma_\bullet(\mathscr{F})$를 $S$-module로 만들어줄 수 있다. 이를 *graded $S$-module associated to $\mathscr{F}$*라 부른다.

</div>

그럼 $S=A[x_0,\ldots, x_r]$이라 하고, 이에 의해 정의되는 projective space $\Proj S$를 생각하면 $\Gamma_\ast(\mathscr{O}
_X)\cong S$가 성립한다는 것을 알 수 있다. 

이제 다음을 보자.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> [명제 3](#prop3)의 상황을 가정하고, $\mathscr{F}\in\QCoh(X)$라 하면 natural isomorphism $\Gamma_\ast(\mathscr{F})^\sim \rightarrow \mathscr{F}$가 존재한다. 

</div>

## Ample invertible sheaf

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> 임의의 $X\in\Sch_{/Y}$에 대하여, $X$ 위에 정의된 rank 1 locally free sheaf $\mathscr{L}$이 주어졌다 하자. 만약 적당한 $r>0$과 immersion $i:X \rightarrow \mathbb{P}^r_Y$가 존재하여 $i^\ast \mathscr{O}(1)\cong \mathscr{L}$이도록 할 수 있으면 $\mathscr{L}$을 *very ample*이라 부른다. 

</div>

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> Scheme $X$와 $\mathscr{F}\in\lMod{\mathscr{O}_X}$를 생각하자. $\mathscr{F}$가 *globally generated*라는 것은 global section들 $(s_i)$가 존재하여, 모든 $x\in X$에 대해 $\mathscr{F}_x$가 $\mathscr{O}_x$-module로서 $s_i$들에 의해 생성되는 것이다. 

</div>

다음 정리는 나중에 유용하게 쓰일 것이다. 

<div class="proposition" markdown="1">

<ins id="thm8">**정리 8**</ins> $X$가 noetherian ring $A$로부터 정의된 projective scheme이라 하고, $\mathscr{O}(1)$이 very ample invertible sheaf라 하자. 그럼 $\mathscr{F}\in\Coh(X)$가 주어질 때마다 적당한 $n_0$가 존재하여, $n\geq n_0$인 모든 $n$에 대해 $\mathscr{F}(n)$이 유한한 section들로 globally generated이도록 할 수 있다. 

</div>