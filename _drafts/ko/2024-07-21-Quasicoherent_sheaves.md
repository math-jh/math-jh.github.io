---

title: "준연접층"
excerpt: ""

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/quasicoherent_sheaves
header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Quasicoherent_sheaves.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_geometry-ko"

date: 2024-07-21
last_modified_at: 2024-07-21
weight: 9

---

이번 글에서 우리는 module처럼 행동하는 sheaf들을 살펴본다. 

## $\mathscr{O}_X$-가군

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Ringed space $(X, \mathscr{O}_X)$에 대하여, sheaf $\mathscr{F}$가 *$\mathscr{O}_X$-module<sub>$\mathscr{O}_X$-가군</sub>*이라는 것은 임의의 열린집합 $U$마다 $\mathscr{F}(U)$가 $\mathscr{O}_X(U)$-module 구조를 가지고, 이것이 restriction map들에 대해 잘 행동하는 것이다. 비슷하게, $\mathscr{O}_X$-module homomorphism은 각각의 열린집합마다 $\mathscr{F}(U)\rightarrow \mathscr{G}(U)$가 $\mathscr{O}_X(U)$-module homomorphism이 되는 morphism을 뜻한다. 

</div>

그럼 $\mathscr{O}_X$-module들의 category는 abelian category가 되는 것을 알 수 있다. 한편 module들을 다룰 때 $\Hom$과 $\otimes$가 중요한 역할을 했었으므로, 우리는 이들 또한 각각 sheaf $\Hom$과 텐서곱을 이용하여

$$\mathscr{Hom}_{\mathscr{O}_X}(\mathscr{F},\mathscr{G}):=\left(U\mapsto \mathscr{Hom}_{\mathscr{O}_X\vert_U}(\mathscr{F}\vert_U,\mathscr{G}\vert_U)\right)$$

그리고

$$\mathscr{F}\otimes_{\mathscr{O}_X}\mathscr{G}:=\left(U\mapsto \mathscr{F}(U)\otimes_{\mathscr{O}_X(U)}\mathscr{G}(U)\right)^\dagger$$

으로 정의한다. 또, $\mathscr{F}$가 $\mathscr{O}_X$들의 direct sum으로 나타난다면 이를 *free $\mathscr{O}_X$-module*이라 부르고, 만일 각각의 $U$마다 $\mathscr{F}\vert_U$가 free $\mathscr{O}_X\vert_U$-module이라면 이를 *locally free*라 부른다. 이 때, $\mathscr{F}$의 $U$에서의 rank를 $\mathscr{F}\vert_U$의 $\mathscr{O}_X\vert$-module로서의 rank로 정의한다. 만일 $X$가 connected라면 어차피 이들의 rank가 모두 같을 것이므로 $\mathscr{F}$의 rank 또한 정의된다. 

앞서 우리는 continuous map이 sheaf에서의 pushforward를 정의하는 것을 살펴보았는데, 비슷하게 $f:(X, \mathscr{O}\_X) \rightarrow (Y, \mathscr{O}\_Y)$가 ringed space들 사이의 morphism이라 하자. 우선 $f\_\ast$의 functoriality에 의하여 $f\_\ast \mathscr{F}$는 $\mathscr{f}\_\ast \mathscr{O}\_X$-module인 것으로 생각할 수 있다. 한편 $f^\sharp:\mathscr{O}\_Y \rightarrow f\_\ast \mathscr{O}\_X$에 의하여, $f\_\ast \mathscr{F}$를 $\mathscr{O}_Y$-module로 취급할 수 있고, 이러한 방식으로 ringed space morphism은 $\mathscr{O}_X$-module 사이의 pushforward를 정의한다. 

이제 $f:(X, \mathscr{O}\_X)\rightarrow (Y, \mathscr{O}_Y)$가 ringed space들 사이의 morphism이라 하고, $\mathscr{O}_Y$-module $\mathscr{G}$가 주어졌다 하자. 그럼 우선 $f^{-1}\mathscr{G}$가 $f^{-1}\mathscr{O}_Y$-module이다. 한편 다음의 natural isomorphism

$$\Hom_{\PSh(X)}(f^{-1}\mathscr{O}_Y,\mathscr{O}_X)\cong \Hom_{\PSh(Y)}(\mathscr{O}_Y, f_\ast \mathscr{O}_X)$$

를 통해, 우변에 속하는 $f^\sharp$은 sheaf morphism $f^{-1}\mathscr{O}_Y \rightarrow \mathscr{O}_X$를 유도하므로, extension of scalar를 통해 pullback $f^\ast \mathscr{G}$를 다음의 $\mathscr{O}_X$-module

$$f^\ast \mathscr{G}=f^{-1}\mathscr{G}\otimes_{f^{-1}\mathscr{O}_Y}\mathscr{O}_X$$

으로 정의할 수 있다. 그럼 adjoint

$$\Hom_{\mathscr{O}_X}(f^\ast \mathscr{G}, \mathscr{F})\cong\Hom_{\mathscr{O}_Y}(\mathscr{G},f_\ast \mathscr{F})$$

를 보일 수 있다. 

이와 마찬가지 방식으로 대부분의 대수적인 성질들을 $\mathscr{O}_X$-module로 옮겨올 수 있다. 예를 들어, finite rank $\mathscr{O}_X$-module $\mathscr{E}$에 대해

$$\check{\mathscr{E}}:=\mathscr{Hom}_{\mathscr{O}_X}(\mathscr{E},\mathscr{O}_X)$$

으로 정의하자. 그럼 다음의 isomorphism들

$$\check{\mathscr{E}}^\vee\cong \mathscr{E},\qquad \mathscr{Hom}_{\mathscr{O}_X}(\mathscr{E},\mathscr{F})\cong \check{\mathscr{E}}\otimes_{\mathscr{O}_X}\mathscr{F}, \qquad \Hom_{\mathscr{O}_X}(\mathscr{E}\otimes \mathscr{F},\mathscr{G})\cong \mathscr{Hom}_{\mathscr{O}_X}(\mathscr{F},\mathscr{Hom}_{\mathscr{O}_X}(\mathscr{E},\mathscr{G}))$$

이 성립한다. 이보다 덜 자명한 것은 다음의 projection formula

$$f_\ast(\mathscr{F}\otimes_{\mathscr{O}_X}f^\ast \mathscr{E})\cong f_\ast \mathscr{F}\otimes_{\mathscr{O}_X}\mathscr{E},\qquad \mathscr{E}\text{ locally free of finite rank}$$

정도이다.

## 준연접층과 연접층

한편 지금까지의 논의를 그대로 사용하기에는 너무 추상적인 면이 있다. 우리는 실제로 대수적인 대상인 $\cRing$으로부터 affine scheme을 만들고, 이를 이어붙여 scheme을 만들었듯 같은 일을 $\mathscr{O}_X$-module에 대해서도 할 수 있기를 바란다. 그 첫 단계는 다음의 정의일 것이다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> Ring $A$와 $A$-module $M$을 고정하자. 그럼 $\Spec A$ 위에 정의된 *sheaf associated to $M$*은 다음과 같이 정의된 sheaf $\widetilde{M}$이다. 

> 각각의 열린집합 $U$마다 $\widetilde{M}(U)$는 함수들 $s:U \rightarrow \coprod_{\mathfrak{p}\in U} M_\mathfrak{p}$들 중 local하게 fraction $m/f$로 쓸 수 있는 것들을 의미한다. 

</div>

이는 $A$로부터 structure sheaf $\mathscr{O}_{\Spec A}$를 만들었던 과정과 정확히 동일하다. 그럼 다음은 [§스펙트럼, ⁋명제 5](/ko/math/algebraic_geometry/spectrums#prop5)의 analogue이다.

<div class="proposition" markdown="1">
 
<ins id="prop3">**명제 3**</ins> Ring $A$와 $A$-module $M$, 그리고 위에서 정의한 $\widetilde{M}$을 생각하면, $\widetilde{M}$은 $\mathscr{O}_X$-module이며 다음이 성립한다. 

1. 임의의 $\mathfrak{p}\in\Spec A$에 대하여, $\widetilde{M}\_\mathfrak{p}$는 $M\_\mathfrak{p}$와 isomorphic하다.
2. 임의의 $f\in A$에 대하여, $\widetilde{M}(D(f))$와 $M_f$가 isomorphic하다.
3. 따라서, $f=1$로 두면 $\Gamma(\Spec A, \widetilde{M})\cong M$이 성립한다.

</div> 

그럼 $\Spec$은 $\cRing$에서 $\AffSch$로의 (contravariant) categorical equivalence였으며, 우리는 이를 이용해서 $\cRing$의 텐서곱 $\otimes$를 $\AffSch$으로 옮기는 등의 일을 했었다. $\sim$ functor에 대해서도 비슷한 것들이 성립하는데, 이번에는 $\sim$의 source, target category에 추가적인 구조들이 있으므로 신경을 쓸 것이 조금 더 추가된다. 어쨌든 중요한 것은 $\sim$이 이들 또한 모두 보존한다는 것이다. 

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> Ring $A$를 고정하자. 그럼 대응 $M\mapsto \widetilde{M}$은 $\lMod{A}$에서 $\lMod{\mathscr{O}_X}$로의 fully faithful functor이며, 추가적으로 다음이 성립한다. 

1. 위의 functor는 exact functor이다. 
2. $(M\otimes_A N)^\sim\cong \widetilde{M}\otimes_{\mathscr{O}_X} \widetilde{N}$이 항상 성립한다.
3. $(\bigoplus M_i)^\sim\cong \bigoplus \widetilde{M}_i$이 항상 성립한다. 

</div>

추가적으로 ring homomorphism $\phi:A \rightarrow B$가 주어졌다 하자. 그럼 이를 통해 

$$\phi_!:\lMod{A}\rightarrow \lMod{B};\qquad M\mapsto \varphi_!M=M\otimes_AB$$

그리고

$$\phi^\ast:\lMod{B} \rightarrow \lMod{A}$$

이 정의된다. $\sim$은 이들 또한 보존한다. 

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> Ring homomorphism $\phi:A \rightarrow B$와 이를 통해 유도된 ringed space morphism $(f,f^\sharp):(\Spec B, \mathscr{O}\_{\Spec B})\rightarrow (\Spec A, \mathscr{O}_{\Spec A})$가 주어졌다 하자. 그럼 임의의 $M\in\lMod{A}$, $N\in\lMod{B}$에 대하여,

1. $f_\ast (\widetilde{N})\cong(\phi^\ast N)^\sim$이 성립한다.
2. $f^\ast(\widetilde{M})\cong (\phi_! M)^\sim$이 성립한다. 

</div>

이제 드디어 quasicoherent sheaf와 coherent sheaf를 정의할 수 있다. Quasicoherent sheaf는 affine scheme에서 scheme을 만들었듯 $\widetilde{M}$들을 붙여서 만들어지는 sheaf를 뜻하고, coherent sheaf는 finite rank를 갖는 것들을 뜻한다. 

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> Scheme $(X,\mathscr{O}\_X)$에 대하여, 만일 open affine covering $(U\_i=\Spec A\_i)\_{i\in I}$가 존재하여, 모든 $i$에 대해 $\mathscr{F}\vert\_{U\_i}\cong \widetilde{M\_i}$이도록 하는 $A\_i$-module들 $M\_i$를 찾을 수 있다면 $\mathscr{F}$를 *quasi-coherent sheaf<sub>준연접층</sub>*이라 부른다. 만일 이들 $M\_i$들이 finitely generated module로 택해질 수 있다면, $\mathscr{F}$를 *coherent sheaf<sub>연접층</sub>*이라 부른다. $X$ 위에 정의된 quasi-coherent sheaf들의 category를 $\QCoh(X)$로, coherent sheaf들의 category를 $\Coh(X)$로 적는다.

</div>

그럼 다음 명제에 의하여 $\QCoh(X)$와 $\Coh(X)$의 관계가, 앞에서 설명한 것과 같이 $\AffSch$와 $\Sch$의 관계에 대응된다는 것을 확인할 수 있다. 

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> Scheme $X$에 대하여, $\mathscr{O}_X$-module $\mathscr{F}$가 quasicoherent인 것과, 임의의 open affine subset $U=\Spec A$마다 적당한 $A$-module $M$이 존재하여 $\mathscr{F}\vert_U\cong \widetilde{M}$이도록 할 수 있는 것이 동치이다. 

만일 $X$가 noetherian이라면, $\mathscr{F}$가 coherent인 것과, 임의의 open affine subset $U=\Spec A$마다 적당한 finitely generated $A$-module $M$이 존재하여 $\mathscr{F}\vert_U\cong \widetilde{M}$이도록 할 수 있는 것이 동치이다. 

</div>

위의 명제와 마찬가지로, coherent sheaf를 말할 때에는 $X$에 noetherian 조건이 꼭 필요하다. 따라서 앞으로 $X$ 위에 정의된 coherent sheaf를 생각할 때에는 $X$가 noetherian인 것도 가정하는 것으로 한다. 

앞선 주장을 더 엄밀하게 말하면, 다음의 adjoint

$$\Hom_{\lMod{A}}(M, \Gamma(X, \mathscr{F}))\cong\Hom_{\mathscr{O}_X}(\widetilde{M},\mathscr{F})$$

가 성립한다. 