---

title: "준연접가군층"
excerpt: ""

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/quasicoherent_sheaves
header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Quasicoherent_sheaves.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_geometry-ko"

date: 2024-11-30
last_modified_at: 2024-11-30
weight: 14

---

## 국소자유가군층

기하학에서 중요한 개념 중 하나는 vector bundle의 개념이다. 다만 지금까지 우리가 다듬어온 정의들은 공간을 보기 위해 그 위에 정의된 함수들을 생각하는 데에 초점이 맞춰져 있으므로, 마찬가지 이유에서 vector bundle을 바로 도입하는 것보다는 vector bundle의 section들의 sheaf를 살펴보는 것이 더 일관된 접근일 것이다. ([\[위상수학\] §준층, ⁋예시 3](/ko/math/topology/presheaves#ex3)) 이것이 일반적인 sheaf와 다른 점은 

1. $X$ 위에 정의된 함수를 곱하여 새로운 section을 만들 수 있고,
2. 충분히 작은 열린집합으로 제한하면 이를 벡터공간과 열린집합의 곱으로 불 수 있다는 것이다.

이 두 가지 특징을 살려 다음을 정의한다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Scheme $X$ 위에 정의된 sheaf $\mathscr{F}$가 rank $n$의 *locally free sheaf<sub>국소자유가군층</sub>*라는 것은 $\mathscr{F}$가 $\mathscr{O}\_X$-module이고, $X$의 open cover $(U\_i)$가 존재하여 $\mathscr{F}\vert\_{U\_i}\cong \mathscr{O}\_{U\_i}^{\oplus n}$이 성립하는 것이다. 

</div>

그럼 임의의 scheme $X$에 대하여, $\mathscr{O}_X$는 자명한 이유로 locally free sheaef of rank $1$이다. 이는 $X$ 위에 정의된 trivial line bundle과 동일한 데이터이다.

이제 scheme $X$를 고정하고, 이 위에 정의된 locally free sheaf $\mathscr{F}, \mathscr{G}$가 주어졌다 하자. 그럼 $\mathscr{H}om(\mathscr{F},\mathscr{G})$는 sheaf일 뿐만 아니라, locally free sheaf가 되며 그 rank는 $\mathscr{F}$와 $\mathscr{G}$의 rank의 곱과 같다. ([\[선형대수학\] §선형사상들의 공간, ⁋정의 4](/ko/math/linear_algebra/space_of_linear_maps#def4)) 특별히 $\mathscr{G}=\mathscr{O}_X$인 경우, 우리는 

$$\mathscr{F}^\vee:=\mathscr{H}om(\mathscr{F},\mathscr{O}_X)$$

으로 표기하고 이를 $\mathscr{F}$의 *dual<sub>쌍대</sub>*이라 부른다. 비슷하게 $\mathscr{O}_X$-module들의 텐서곱을 이용하면 $\mathscr{F}\otimes \mathscr{G}$ 또한 locally free sheaf인 것을 확인할 수 있으며 이들은 일반적인 module의 $\Hom$과 $\otimes$가 만족하는 성질들을 만족한다. 가령 $\Hom$-tensor adjoint

$$\mathscr{H}om(\mathscr{F},\mathscr{G}\otimes \mathscr{E})\cong \mathscr{H}om(\mathscr{F}\otimes \mathscr{E}^\vee,\mathscr{G})\qquad \text{$\mathscr{E}$ a locally free sheaf of finite rank, $\mathscr{F},\mathscr{G}$ $\mathscr{O}_X$-modules}$$

가 성립하며, rank $1$ locally free sheaf $\mathscr{L}$에 대해서는 $\mathscr{L}\otimes \mathscr{L}^\vee\cong \mathscr{O}_X$가 성립한다. 

## 준연접가군층

그런데 locally free sheaf들의 경우, 이들을 모아둔 것이 abelian category가 되지 않는다. 이는 생각해보면 당연한 것이 kernel과 cokernel이 잘 정의되지 않기 때문이다. 때문에 우리는 이를 약간 확장하여 준연접가군층의 개념을 정의한다. 

준연접가군층은 $\mathscr{O}_X$-module로서, affine cover $\Spec A$ 위에서는 대수적으로 $A$-module $M$에 해당하는 대상이다. 이를 정확히 이야기하기 위해서는 $M$이 어떠한 방식으로 $\Spec A$ 위에 sheaf를 정의하는지를 설명해야 한다.

<div class="proposition" markdown="1">

<ins id="lem2">**보조정리 2**</ins> $A$-module $M$를 고정하고, $f\in A$라 하자. 만일

$$S=\{g\in A: D(f)\subseteq D(g)\}$$

이라면, $\widetilde{M}(D(f))=S^{-1}M$으로 정의한다.

</div>

그럼 이것이 $\Spec A$ 위에서 정의된 sheaf인 것을 [§아핀스킴](/ko/math/algebraic_geometry/affine_schemes)에서와 같은 과정을 통해 보일 수 있으며, 이는 [§아핀스킴, ⁋명제 5](/ko/math/algebraic_geometry/affine_schemes#prop5)에 대응되는 다음의 명제에 의해 얻어진다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> 위와 같은 상황에서 다음이 성립한다.

1. $\widetilde{M}$은 $\mathscr{O}\_{\Spec A}$-module이다.
2. 임의의 $\mathfrak{p}\in\Spec A$에 대하여, $\widetilde{M}\_\mathfrak{p}$는 $M\_\mathfrak{p}$와 isomorphic하다.
3. 임의의 $f\in A$에 대하여, $\widetilde{M}(D(f))$와 $M_f$가 $A_f$-module로서 isomorphic하다.
4. 특히 $f=1$로 두면 $\Gamma(X, \widetilde{M})\cong M$이 성립한다.

</div>

이에 대한 증명은 본질적으로 [§아핀스킴, ⁋명제 5](/ko/math/algebraic_geometry/affine_schemes#prop5)와 다를 것이 없다. 

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> Scheme $X$와 그 위에 정의된 $\mathscr{O}\_X$-module $\mathscr{F}$에 대하여, $\mathscr{F}$가 *quasi-coherent sheaf<sub>준연접가군층</sub>*이라는 것은 임의의 affine open subset $U=\Spec A$마다 $\mathscr{F}\vert_{\Spec A}\cong \widetilde{M}$이도록 하는 $A$-module $M$이 존재하는 것이다.

</div>

그럼 이 조건이 [§스킴의 성질들, ⁋보조정리 10](/ko/math/algebraic_geometry/properties_of_schemes#lem10)을 만족하는 것을 보일 수 있다. 특히 정의에 의하여 locally free sheaf는 항상 quasi-coherent sheaf이다. 

이렇게 정의하고 나면 $X$ 위에 정의된 quasi-coherent sheaf들의 category $\QCoh(X)$가 abelian category라는 것이 비교적 쉽게 보이는데, 임의의 $A$-module homomorphism $M \rightarrow N$의 kernel과 cokernel이 다시 $A$-module이기 때문이다. 물론 이를 제대로 보이기 위해서는 이들 데이터가 잘 붙는다는 것을 보여야 하지만, 이는 본질적으로 localization이 exact functor이기 때문에 어렵지 않게 보일 수 있다. 

마찬가지 논리로, localization은 tensor product와 commute하므로 $\otimes$ 또한 잘 정의된다. 즉 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> 임의의 $\mathscr{F},\mathscr{G}\in\QCoh(X)$에 대하여, $\mathscr{F}\otimes\mathscr{G}\in\QCoh(X)$이다.

</div>

다시 localization이 exact functor라는 것을 이용하면, tensor product에 quotient를 취해 얻어지는 다음의 대상들에도 비슷한 말을 할 수 있다.

<div class="proposition" markdown="1">

<ins id="cor6">**따름정리 6**</ins> 임의의 $\mathscr{F}\in\QCoh(X)$에 대하여, $T^n(\mathscr{F}), \Sym^n(\mathscr{F}), \bigwedge^n \mathscr{F}\in\QCoh(X)$가 성립한다.

</div>

또, 마지막으로 localization은 direct sum과 commute하므로 다음을 얻는다. 

<div class="proposition" markdown="1">

<ins id="cor7">**따름정리 7**</ins> 임의의 $\mathscr{F}\in\QCoh(X)$에 대하여, $T^\bullet(\mathscr{F}), \Sym^\bullet(\mathscr{F}), \bigwedge^\bullet \mathscr{F}\in\QCoh(X)$가 성립한다.

</div>

## 연접가군층

앞서 정의한 quasi-coherent sheaf는 한 마디로 이야기하자면 affine open cover $\Spec A$ 위에서 봤을 때 $A$-module $M$으로 볼 수 있는 것들이다. 이는 locally free sheaf에 비해 상당히 약화된 부분이 있는데, $M$이 finite rank일 것을 요구하지 않았다는 것이다. 
그럼 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> Noetherian ring $A$와 $A$-module $M$에 대하여, 다음이 모두 동치이다.

1. $M$이 finitely generated이다.
2. $M$이 finitely presented이다.
3. $M$이 coherent이다.

</div>

일반적으로 우리가 다루는 상황은 항상 $A$가 noetherian이므로, 직관적으로 coherent module은 finitely generated module인 것으로 생각해도 된다. 이 개념은 $A$가 noetherian이 아닐 때 finitely generated module의 개념을 확장하게 해 준다. 

어쨌든 다음을 정의한다.

<div class="definition" markdown="1">

<ins id="def10">**정의 10**</ins> Scheme $X$와 그 위에 정의된 $\mathscr{O}\_X$-module $\mathscr{F}$에 대하여, $\mathscr{F}$가 *of finite type*이라는 것은 임의의 affine open subset $U=\Spec A$마다 $\mathscr{F}\vert\_{\Spec A}\cong \widetilde{M}$이도록 하는 *finitely generated* $A$-module $M$이 존재하는 것이다. 비슷하게 $\mathscr{F}$가 *finitely presented*이라는 것은 임의의 affine open subset $U=\Spec A$마다 $\mathscr{F}\vert\_{\Spec A}\cong \widetilde{M}$이도록 하는 *finitely presented* $A$-module $M$이 존재하는 것이며, $\mathscr{F}$가 *coherent*라는 것은 affine open subset $U=\Spec A$마다 $\mathscr{F}\vert\_{\Spec A}\cong \widetilde{M}$이도록 하는 *coherent* $A$-module $M$이 존재하는 것이다.

</div>

그럼 [명제 9](#prop9)에 의하여, 임의의 locally noetherian scheme $X$ 위에 정의된 coherent sheaf는 locally free sheaf이다. 앞서 quasi-coherent sheaf들 $\QCoh(X)$가 (infinite rank일 수 있는) locally free sheaf들을 포함하는 abelian category였듯, coherent sheaf들의 카테고리 $\Coh(X)$는 finite rank locally free sheaf를 포함하는 abelian category가 된다. 