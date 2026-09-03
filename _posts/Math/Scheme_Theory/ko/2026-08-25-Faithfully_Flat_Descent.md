---
title: "충실평탄하강"
description: "Faithfully flat morphism을 따라 algebraic·geometric data를 내려보내는 Grothendieck의 descent theory를 다룬다. Amitsur complex의 exactness로부터 module의 descent 정리를 유도하고, descent datum의 category가 base ring 위의 module category와 equivalent함을 보인 뒤, 이를 fpqc topology 위의 quasi-coherent sheaf와 morphism의 descent로 확장한다."
excerpt: "Faithfully flat descent, descent datum, the cocycle condition, fpqc topology and effective descent"

categories: [Math / Scheme Theory]
permalink: /ko/math/scheme_theory/faithfully_flat_descent
sidebar: 
    nav: "scheme_theory-ko"

date: 2026-08-25
weight: 27
---

Algebraic geometry에서 가장 흔한 construction 가운데 하나는 국소적인 대상들을 붙여 하나의 대상으로 만드는 것으로, 가장 익숙한 예는 open cover를 따라 sheaf의 section을 붙이는 것이다. 이는 본질적으로 localization으로 주어지는 특별한 종류의 base change만을 사용하는 것인데, 우리가 실제로 다루고 싶은 많은 상황은 이보다 일반적인 것이다. 예를 들어 field extension $\mathbb{L}/\mathbb{K}$에 대응되는 $\Spec \mathbb{L}\rightarrow \Spec \mathbb{K}$는 residue field가 달라지므로 open embedding으로 볼 수 없다. 

이를 해결하기 위한 아이디어는 open embedding 뿐만 아니라, faithfully flat하며 quasi-compact한 morphism들도 유효한 covering으로 취급하자는 것이다. 우리는 이들을 유효한 covering으로 취급할 수 있는 algebraic 이유를 먼저 살펴본 후, 이를 geometry로 옮긴다. 

## 충실평탄사상

그 이름에서 알 수 있듯 faithful flatness는 flatness에 일종의 전사성을 더한 조건이다.

::: 정의 1
Ring homomorphism $\phi: A \rightarrow B$가 *faithfully flat<sub>충실평탄</sub>*하다는 것은, $B$가 flat $A$-module이고, 동시에 임의의 $A$-module $M$에 대하여 $M\otimes_A B=0$이면 $M=0$인 것이다.
:::

즉 $-\otimes_A B$가 $0$이 아닌 module을 $0$으로 보내지 않는다는 것이 flatness에 붙는 추가적인 faithfulness이다. 이는 다음과 같은 동치조건을 가진다.

::: 명제 2
Flat ring homomorphism $\phi: A \rightarrow B$에 대하여 다음이 동치이다.

1. $\phi$는 faithfully flat이다.
2. $A$-module의 sequence $M' \rightarrow M \rightarrow M''$이 exact인 것은, $B$-module의 sequence $M'\otimes_A B \rightarrow M\otimes_A B \rightarrow M''\otimes_A B$가 exact인 것과 동치이다.
3. $\phi$에 대응하는 scheme morphism $\varphi: \Spec B \rightarrow \Spec A$는 surjective이다.
:::
::: 증명
우선 첫째 조건과 둘째 조건이 동치임을 보인다. 이를 위해 첫째 조건을 가정하자. 그럼 가정에 의해 $B$가 flat이므로 exact sequence는 $-\otimes_A B$ 후에도 exact하며, 둘째 조건의 한쪽 방향은 자명하다. 핵심은 반대방향으로, 이를 보이기 위해 

$$M'\otimes_AB \overset{f\otimes_AB}{\longrightarrow} M\otimes_AB \overset{g\otimes_AB}{\longrightarrow} M''\otimes_AB$$

이 exact sequence라 하자. 그럼 우선 

$$0=(g\otimes B)\circ(f\otimes B)=(g\circ f)\otimes B$$

이므로, inclusion으로부터 오는 

$$\im(g\circ f)\otimes_A B \rightarrow M''\otimes_A B$$ 

의 image 또한 $0$이다. 그런데 이를 $\im(g\circ f)\hookrightarrow M''$에서 오는 것으로 생각하면, $B$가 flat이므로 위의 morphism 또한 injective이며, 따라서 faithfulness에 의해 $\im(g\circ f)=0$이고 $\im f\subseteq \ker g$가 성립한다. 이제 exactness를 확인하기 위해 $H=\ker g/\im f$가 $0$임을 보이면 되는데, 이는 $B$가 flat이므로 자명하다. 그럼 앞서와 같은 논리로, faithfulness에 의해 $H=0$이고 따라서 원래 sequence가 exact하다.

거꾸로 둘째 조건을 가정하고 첫째 조건을 보이자. $M\otimes_A B=0$이라 하면, sequence $0 \rightarrow M \rightarrow 0$이 $-\otimes_A B$ 후 exact하므로 가정에 의해 $0 \rightarrow M \rightarrow 0$이 exact하다. 즉 $M=0$이고 $\phi$는 faithfully flat이다.

이제 첫째 조건과 셋째 조건의 동치를 보인다. 우선 첫째 조건을 가정하고 임의의 $\mathfrak{p}\in \Spec A$를 택하자. 그럼 $\mathfrak{p}$가 $\varphi$의 image에 속하는 것은 그 fiber $\Spec(B\otimes_A \kappa(\mathfrak{p}))$가 nonempty인 것, 즉 $B\otimes_A \kappa(\mathfrak{p})\neq 0$인 것과 동치이다. 그런데 faithfully flatness에 의하여, $\kappa(\mathfrak{p})\neq 0$이라면 그 base change $B\otimes_A \kappa(\mathfrak{p})$도 그러하므로 이것이 성립한다. 

마지막으로 셋째 조건을 가정하고 첫째 조건을 보이자. 이를 위해 $M\neq 0$인 임의의 $A$-module $M$에 대하여 $M\otimes_A B\neq 0$임을 보이면 충분하다. $0\neq x\in M$을 택하면 $Ax\cong A/{\ann(x)}$이고, 이는 $M$의 submodule이다. 이제 $\ann(x)\subseteq \mathfrak{m}$인 maximal ideal $\mathfrak{m}$을 택하자. 그럼 가정에 의해 이는 $\varphi$의 image에 속하므로 $\kappa(\mathfrak{m})\otimes_A B\neq 0$이다. 한편 surjection $A/{\ann(x)}\twoheadrightarrow A/\mathfrak{m}=\kappa(\mathfrak{m})$에 $-\otimes_A B$를 적용하면 surjection

$$(A/{\ann(x)})\otimes_A B\twoheadrightarrow \kappa(\mathfrak{m})\otimes_A B$$

를 얻으므로 $(A/{\ann(x)})\otimes_A B\neq 0$이다. 또한 $B$가 flat이므로 inclusion $A/{\ann(x)}\cong Ax\hookrightarrow M$에 $-\otimes_A B$를 적용하면 inclusion

$$(A/{\ann(x)})\otimes_A B\hookrightarrow M\otimes_A B$$

을 얻는다. 따라서 $M\otimes_A B\neq 0$이고, $B$는 faithful $A$-module이다.
:::

이 명제에서 특히 주목할 만한 것은 둘째 조건으로, exactness를 base change를 한 후 확인해도 된다는 것을 보여준다. 셋째 조건은 이렇게 대수적으로 정의된 성질이 정확히 morphism $\Spec B \rightarrow \Spec A$의 surjectivity에 대응함을 보여주며, 따라서 faithfully flat ring homomorphism은 [§평탄사상, ⁋정의 1](/ko/math/scheme_theory/flat_morphisms#def1)의 affine faithfully flat morphism으로 생각할 수 있다.

특수한 예시는 $A$의 원소들 $f_1,\ldots, f_n$이 $A$ 전체를 생성할 때 얻어지는 $A \rightarrow \prod_i A_{f_i}$으로, 각각의 $A_{f_i}$가 flat이므로 그 곱도 flat이고, $\Spec \prod A_{f_i}=\coprod D(f_i)$가 $\Spec A$를 덮으므로 surjective이다. 이는 정확히 affine scheme의 Zariski cover이며, 위의 개념이 일상적인 sheaf의 gluing을 커버할 수 있음을 보여준다. 뿐만 아니라, 위에서 open embedding으로 설명할 수 없었던 field extension $\mathbb{L}/\mathbb{K}$의 경우, $\mathbb{L}$이 $\mathbb{K}$-vector space로서 (당연히) free이고, 이들 사이의 기하적인 morphism은 한 점을 한 점으로 보내는 surjective morphism이므로 이는 faithfully flat이다. 

## Amitsur complex

Ring homomorphism $\phi: A \rightarrow B$가 주어지면 두 morphism

$$d^0, d^1: B \rightrightarrows B\otimes_A B,\qquad d^0(b)=b\otimes 1,\quad d^1(b)=1\otimes b$$

이 주어진다. 이는 $B$를 $B\otimes_AB$에 어떠한 방식으로 집어넣을지를 반영하는 두 homomorphism이며, 이들의 차 $d=d^1-d^0$을 생각하여 morphism $d: B\rightarrow B\otimes_AB$을 생각할 수 있다. 뿐만 아니라, $A$에서 온 원소는 tensor product의 성질에 의하여 $d$의 kernel에 속하므로, 다음의 sequence

$$0\rightarrow A \overset{\phi}{\longrightarrow}B\overset{d}{\longrightarrow}B\otimes_AB$$

를 생각할 수 있다. 

더 일반적으로, $B$의 $(n+1)$-th tensor power를 $C^n=B^{\otimes (n+1)}$이라 하고, $C^n$에서 $C^{n+1}$로 가는 다음의 morphism

$$\delta_i: C^n \rightarrow C^{n+1};\qquad \delta_i(b_0\otimes \cdots \otimes b_n)=b_0\otimes \cdots \otimes b_{i-1}\otimes 1\otimes b_i\otimes \cdots \otimes b_n$$

을 생각하자. 즉 이는 $i$번째 자리에 $1$을 끼워넣는 morphism이며, 이들의 부호를 번갈아 붙여 더한

$$\partial^n=\sum_{i=0}^{n+1}(-1)^i\delta_i: C^n \rightarrow C^{n+1}$$

은 $C^n$에서 $C^{n+1}$로의 morphism이 된다. 약간의 계산을 통해 이것이 complex가 되는 것을 확인할 수 있으며, 여기에 위와 같이 $\phi$를 붙여서 얻어지는

$$0 \rightarrow A \overset{\phi}{\longrightarrow} B \overset{\partial^0}{\longrightarrow} B\otimes_A B \overset{\partial^1}{\longrightarrow} B\otimes_A B\otimes_A B \rightarrow \cdots$$

를 $\phi$의 *Amitsur complex<sub>Amitsur 복합체</sub>*라 부른다. 

핵심적인 관찰은 만일 $\phi$가 faithfully flat이라면 이 complex가 exact가 되어, $C^\bullet$이 $A$의 resolution이 된다는 것이다. 다만 이 글에서 우리가 실제로 쓰는 것은 이 resolution 전체가 아니라 처음 두 개의 morphism 뿐이므로 우리는 다음만 주장한다. 

::: 보조정리 3
Ring homomorphism $\phi: A \rightarrow B$에 대하여, 위의 sequence에 $-\otimes_A B$를 취하여 얻어지는 $B$-module의 sequence

$$0 \rightarrow B \overset{\phi\otimes B}{\longrightarrow} B\otimes_A B \overset{d\otimes B}{\longrightarrow} B\otimes_A B\otimes_A B$$

는 split exact하다. 특히 $\phi$가 faithfully flat이면 sequence

$$0 \rightarrow A \overset{\phi}{\longrightarrow} B \overset{d}{\longrightarrow} B\otimes_A B$$

는 exact하다. 
:::
::: 증명
우선 $-\otimes_A B$를 적용하여 얻어진 sequence

$$0 \rightarrow B \overset{\phi\otimes B}{\longrightarrow} B\otimes_A B \overset{d\otimes B}{\longrightarrow} B\otimes_A B\otimes_A B$$

를 생각하자. 우리 주장은 이것이 split exact sequence라는 것이다. 

이를 확인하기 위해 두 map

$$s: B\otimes_AB \rightarrow B;\quad b\otimes b'\mapsto bb',\qquad t: B\otimes_AB\otimes_AB\rightarrow B\otimes_AB;\quad b\otimes b'\otimes b''\mapsto b\otimes b'b''$$

을 생각하자. $B\otimes_AB$와 $B\otimes_AB\otimes_AB$ 각각에 $B$-module 구조를 가장 오른쪽 $B$에 작용하는 것으로 주면, 이 두 map은 $B$-linear map이 되며 다음 식

$$s\circ(\phi\otimes B)=\id_B$$

이 성립하는 것이 자명하다. 즉 $\phi\otimes B$는 injective이다. 뿐만 아니라, 만일 $b\otimes b'\in\ker(d\otimes B)$라면, 그 정의에 의해

$$0=(d\otimes B)(b\otimes b')=1\otimes b\otimes b'-b\otimes 1\otimes b'$$

이므로 $1\otimes b\otimes b'=b\otimes 1\otimes b'$이고, 여기에 $t$를 적용하면

$$b\otimes b'=t(b\otimes 1\otimes b')=t(1\otimes b\otimes b')=1\otimes bb'=(\phi\otimes B)(s(b\otimes b'))$$

이므로 $\ker(d\otimes B)\subseteq \im(\phi\otimes B)$이다. 반대쪽 포함관계는 $d\circ \phi=0$으로부터 자명하므로 base change된 sequence는 exact하다. 특히 $\phi$가 faithfully flat이면 [명제 2](#prop2)에 의하여 원래 sequence도 exact하다.

Split exactness의 주장을 완결하기 위해 $t$쪽을 다시 살펴보면, 임의의 $b\otimes b'$에 대하여 $t((d\otimes B)(b\otimes b'))=1\otimes bb'-b\otimes b'$이므로

$$(\phi\otimes B)\circ s-t\circ (d\otimes B)=\id_{B\otimes_AB}$$

이고, 이는 $s\circ (\phi\otimes B)=\id_B$와 함께 $(s,-t)$가 이 sequence의 contracting homotopy임을 확인할 수 있다. 
:::

이는 앞서 본 affine scheme의 Zariski open cover를 보면 이것이 gluing의 엔진이 되는 이유가 명확하게 드러난다. $A=(f_1,\ldots, f_n)$이라 하고, $B=\prod_i A_{f_i}$라 하자. 그럼

$$B\otimes_AB=\left(\prod_i A_{f_i}\right)\otimes_A \left(\prod_j A_{f_j}\right)$$

이고, 이 때 곱이 유한하므로 이들을 합쳐

$$B\otimes_AB \cong\prod_{i,j} A_{f_i}\otimes A_{f_j}\cong\prod_{i,j} A_{f_if_j}$$

으로 생각할 수 있다. ([\[가환대수학\] §국소화의 성질들, ⁋보조정리 1](/ko/math/commutative_algebra/properties_of_localization#lem1)) 그럼 이 identification 하에서, $d^0$은 $B$의 원소를 앞쪽 $i$ 성분으로 넣는 것이고, $d^1$은 $B$의 원소를 뒤쪽 $j$ 성분으로 넣는 것이다. 

기하적으로는 $D(f_i)\cap D(f_j)=D(f_if_j)$이므로, $B\otimes_AB$는 $D(f_i)\cap D(f_j)$ 위에 정의된 함수들이 이루는 ring으로 생각할 수 있고, 이 때 $d^0$과 $d^1$은 각각 restriction

$$d^0\bigl((s_i)_i\bigr)=\bigl(s_i\vert_{D(f_if_j)}\bigr)_{i,j},\qquad d^1\bigl((s_i)_i\bigr)=\bigl(s_j\vert_{D(f_if_j)}\bigr)_{i,j}$$

가 된다. 즉, 두 morphism의 차이는 overlap $D(f_if_j)$ 위에서 $s_i$와 $s_j$ 중 어느것을 보는지에 따라 달라지는 것으로, $B$의 원소 $(s_i)_i$가 $d$의 kernel에 속한다는 것은 모든 $i,j$에 대하여 $s_i$와 $s_j$가 그 overlap 위에서 일치한다는 것이다. 즉, $D(f_i)$마다 정의된 $s_i$들의 gluing condition을 주는 것이다. 뿐만 아니라, $\phi$의 injectivity는 정확하게 모든 $D(f_i)$ 위에서 $0$이 되는 $A$의 원소가 $0$이라는 주장이므로 sheaf의 identity condition을 주며, 따라서 [보조정리 3](#lem3)은 open cover $\{D(f_i)\}_i$에 대한 $\mathcal{O}_{\Spec A}$의 sheaf condition에 불과하다. 더 일반적으로 Amitsur complex의 나머지 항들은 이 cover의 Čech complex가 된다.

## 하강의 재료

[보조정리 3](#lem3)은 $A$가 $B$의 데이터로부터 어떻게 복원되는지를 정확하게 말해주며, 슬로건은 $B$ 안에서 두 방식의 base change가 일치하는 원소들을 모아두면 그것이 정확히 $A$가 된다는 것이다.

이 원리를 module로 올린 것이 descent이다. $B$-module $N$이 주어졌다 하고, 여기에 $-\otimes_AB$ 혹은 $B\otimes_A-$를 취해 $B\otimes_AB$-module 구조를 얻는 과정을 생각하자. Ring에서와 마찬가지로, 이 두 $B\otimes_AB$-module $N\otimes_AB$와 $B\otimes_AN$은 $N$이 첫째 factor로 들어가는지, 둘째 factor로 들어가는지에 따라 달라지는 두 구조이며 이 둘을 비교하여 그 equalizer를 생각하는 것이 우리의 목표이다. 문제는 ring에서의 상황과 다르게, $N\otimes_AB$와 $B\otimes_AN$은 <em-ko>정말로</em-ko> 다른[^1] 두 대상이라는 것이다. 따라서 이들을 비교하여 equalizer를 계산하기 위해서는 추가적인 입력, 즉 $N\otimes_AB$와 $B\otimes_AN$ 사이의 identification이 필요하며 이것이 정확히 descent datum이다. 

이를 다루기 위해 표기를 고정하자. 우리는 morphism

$$p_1: B\rightarrow B\otimes_AB;\quad b\mapsto b\otimes 1, \qquad p_2: B\rightarrow B\otimes_AB;\quad b\mapsto 1\otimes b$$

를 정의하고, 이와 비슷하게

$$p_{12}, p_{13}, p_{23}: B\otimes_A B \rightarrow B\otimes_A B\otimes_A B$$

들을, 세 factor들 가운데 index가 지정하는 두 factor로 보내주는 morphism으로 정의한다. 그럼 $B$-module $N$에 대하여 $p_1^\ast N=N\otimes_A B$이고 $p_2^\ast N=B\otimes_A N$임을 안다.

::: 정의 4
Ring homomorphism $\phi: A \rightarrow B$에 대한 *descent datum<sub>하강 자료</sub>*은 $B$-module $N$과 $B\otimes_A B$-module isomorphism

$$\Phi_N: p_1^\ast N=N\otimes_A B \overset{\sim}{\longrightarrow} B\otimes_A N=p_2^\ast N$$

의 pair $(N, \Phi_N)$으로서, $B\otimes_A B\otimes_A B$ 위에서 *cocycle condition*

$$p_{13}^\ast \Phi_N=p_{23}^\ast \Phi_N\circ p_{12}^\ast \Phi_N$$

을 만족하는 것이다. 두 descent datum $(N, \Phi_N)$과 $(N', \Phi_{N'})$ 사이의 *morphism*은 $B$-module homomorphism $g: N \rightarrow N'$ 중 $\Phi_{N'}\circ(g\otimes B)=(B\otimes g)\circ \Phi_N$을 만족하는 것이다. 이들이 이루는 category를 $\Desc(B/A)$로 적는다.
:::

여기서 cocycle condition은 triple intersection 위에서 gluing이 모순없이 잘 정의된다는 것으로, 다음의 diagram

{% diagram Math/Scheme_Theory/Faithfully_Flat_Descent-1.svg width="15.94em" alt="cocycle condition" %}

으로 나타낼 수 있으며, 각 morphism의 경우, 예를 들어 $p_{12}^\ast \Phi_N: p_1^\ast N\rightarrow p_2^\ast N$은 다음의 식

$$N\otimes_A B\otimes_A B \rightarrow B\otimes_A N\otimes_A B;\qquad n\otimes b\otimes b'\mapsto \Phi_N(n\otimes b)\otimes b'$$

으로 주어지는 것이다. 

Ring에서의 Amitsur complex를 보기 위해 우리는 우선 $d=d^1-d^0$의 kernel이 $A$를 이미 포함하는 것을 관찰했었다. Module 상황에서 이에 대응하는 것은 $B$-module $N$이 어떤 $A$-module $M$의 base change $M\otimes_A B$로부터 온 경우로, 이 때에는 위에서 추가 입력으로 요구한 identification이 저절로 주어진다. 이 경우 두 base change는

$$p_1^\ast N=M\otimes_A B\otimes_A B,\qquad p_2^\ast N=B\otimes_A M\otimes_A B$$

로, 위에서 살펴본 일반적인 경우와 마찬가지로 서로 다른 $B\otimes_AB$-module이 된다. 그러나 이 두 경우 모두 $B\otimes_AB$의 첫째 factor는 왼쪽 $B$-factor에, 둘째 factor는 오른쪽 $B$-factor에 작용하는 방식으로 $B\otimes_AB$-module 구조가 주어지며, $A$의 commutativity를 사용하여 $p_2^\ast N$의 $M$-factor를 앞으로 옮겨주면 이것은 $B\otimes_AB$-module isomorphism이며 이를 통해 $p_1^\ast N$과 $p_2^\ast N$을 비교할 수 있다. 

::: 예시 5
$A$-module $M$에 대하여 $N=M\otimes_A B$로 두면, 위에서 본 두 base change $p_1^\ast N=M\otimes_A B\otimes_A B$와 $p_2^\ast N=B\otimes_A M\otimes_A B$ 사이의 $B\otimes_A B$-module isomorphism

$$\sigma_M: M\otimes_A B\otimes_A B \overset{\sim}{\longrightarrow} B\otimes_A M\otimes_A B;\qquad m\otimes x\otimes y\mapsto x\otimes m\otimes y$$

이 descent datum $(M\otimes_A B, \sigma_M)$을 정의한다. 이를 $M$에 딸린 *canonical descent datum*이라 부른다. 

더 일반적으로 $A$-module homomorphism $M \rightarrow M'$은 base change하여 canonical descent datum 사이의 morphism을 주므로, 대응 $M\mapsto (M\otimes_A B, \sigma_M)$은 functor

$$\rMod{A} \rightarrow \Desc(B/A)$$

를 정의한다.
:::

## 충실평탄하강

이제 우리는 이 글의 핵심적인 주장을 세울 준비가 됐다. 이는 기본적으로 [보조정리 3](#lem3)에서 확인한 원리를 다시 쓴 것에 지나지 않는다. 
::: 정리 6 (Grothendieck)
Ring homomorphism $\phi: A \rightarrow B$가 faithfully flat이면, [예시 5](#ex5)의 functor

$$\rMod{A} \rightarrow \Desc(B/A);\qquad M\mapsto (M\otimes_A B, \sigma_M)$$

은 categorical equivalence이다. 그 inverse functor는 descent datum $(N, \Phi_N)$에 대하여

$$N^\Phi=\{n\in N\mid \Phi_N(n\otimes 1)=1\otimes n\}$$

으로 주어진다.
:::
::: 증명
우선 $A$-module $M$이 주어졌다 하고, 이것이 정의하는 canonical descent datum $(M\otimes_A B, \sigma_M)$을 생각하자. 여기에 위의 inverse functor를 적용하면

$$(M\otimes_AB)^\sigma=\{x\in M\otimes_A B\mid \sigma_M(x\otimes 1)=1\otimes x\}$$

를 얻고, $\sigma_M$은 $M$-factor를 옮길 뿐이므로 양변의 $M$-factor를 앞으로 되돌려 $M\otimes_A B\otimes_A B$ 안에서 읽으면 조건은 $x\otimes 1=1\otimes x$이다. 따라서 보여야 할 것은 sequence

$$0 \rightarrow M \rightarrow M\otimes_A B \rightarrow M\otimes_A B\otimes_A B$$

의 exactness이며, 이는 [보조정리 3](#lem3)의 증명에 coefficient $M$을 붙여 그대로 반복하면 얻어진다. 

본질적으로 내용이 있는 부분은 반대방향이다. 즉, descent datum $(N, \Phi_N)$에 대하여 $M=N^\Phi$라 두었을 때, $B$-module morphism

$$u: M\otimes_A B \rightarrow N;\qquad m\otimes b\mapsto bm$$

이 descent datum $(M\otimes_AB, \sigma_M)$에서 $(N, \Phi_N)$으로의 isomorphism임을 보여야 한다. 

이제 우리는 $u$의 inverse $v: N\rightarrow M\otimes_AB$를 만든다. 아이디어는 어차피 $N$의 원소를 받아서 $M\otimes_AB$로 넣기 위해서는 $n$을 $n\otimes 1$과 같은 류의 원소로 보낼 수밖에 없다는 것이며, 이를 염두에 두고 약간의 계산을 해 보면 우리는 descent datum을 사용하여 $n\mapsto \Phi_N^{-1}(1\otimes n)$과 같이 정의해야만 하는 것을 안다. 편의상 $\Psi=\Phi_N^{-1}$로 적으면, 우리 주장은 이 대응 $n\mapsto \Psi(1\otimes n)$의 치역이 $M\otimes_AB$로 떨어진다는 것이다. 

이를 확인하기 위해 $\Psi(1\otimes n)=\sum_j n_j\otimes c_j$라 하자. 그럼 cocycle condition에 의해 $p_{13}^\ast \Psi=p_{12}^\ast \Psi\circ p_{23}^\ast \Psi$이고, 양변을 원소 $1\otimes 1\otimes n\in B\otimes_A B\otimes_A N$에서 계산하면

$$p_{13}^\ast \Psi(1\otimes 1\otimes n)=\sum_j n_j\otimes 1\otimes c_j,\qquad (p_{12}^\ast \Psi\circ p_{23}^\ast \Psi)(1\otimes 1\otimes n)=\sum_j \Psi(1\otimes n_j)\otimes c_j$$

이다. 이제 이들 둘을 같은 것으로 두고, 양 변에 $p_{12}^\ast \Phi_N$을 적용하면 다음 등식

$$\sum_j \Phi_N(n_j\otimes 1)\otimes c_j=\sum_j (1\otimes n_j)\otimes c_j$$

을 얻는다. 따라서 $d_N: N \rightarrow B\otimes_A N$을 $d_N(n)=\Phi_N(n\otimes 1)-1\otimes n$으로 정의하면 $(d_N\otimes B)\bigl(\sum_j n_j\otimes c_j\bigr)=0$이 성립한다. 그럼 우리 주장은 $\ker(d_N\otimes B)=M\otimes_AB$이고 따라서 위의 대응이 $M\otimes_AB$로 간다는 것이다. 이제 $M$의 정의에 의하여 sequence $0 \rightarrow M \rightarrow N \overset{d_N}{\longrightarrow} B\otimes_A N$이 exact하고, $B$가 flat이므로 여기에 $-\otimes_AB$를 취한

$$0 \rightarrow M\otimes_A B \rightarrow N\otimes_A B \overset{d_N\otimes B}{\longrightarrow} B\otimes_A N\otimes_A B$$

또한 exact하다. 즉 $N\otimes_A B$ 안에서 $M\otimes_A B=\ker(d_N\otimes B)$이다.

이제 이렇게 만든 대응 $v: n\mapsto \Psi(1\otimes n)$이 실제로 $u$의 역함수임을 보이자. 우선 

$$v(u(m\otimes b))=\Psi(1\otimes bm)=(1\otimes b)\Psi(1\otimes m)=(1\otimes b)(m\otimes 1)=m\otimes b$$

임은 자명하다. 반대로 $u(v(n))=n$의 경우, 우선 $v(n)$이 $M\otimes_A B$의 원소이므로 $m_k\in M$들을 택해 $v(n)=\sum_k m_k\otimes b_k$의 꼴로 쓸 수 있고, 여기에 $\Phi_N$을 적용하면 $\Phi_N(v(n))=\Phi_N(\Psi(1\otimes n))=1\otimes n$이고 따라서

$$1\otimes n=\sum_k (1\otimes b_k)\Phi_N(m_k\otimes 1)=\sum_k (1\otimes b_k)(1\otimes m_k)=1\otimes \sum_k b_km_k$$

이다. 그런데 $n\mapsto n\otimes 1$의 injectivity는 [보조정리 3](#lem3)(의 $M$-coefficient 버전)이 주고, 여기에서 순서만 바꾼 $n\mapsto 1\otimes n: N \rightarrow B\otimes_A N$ 또한 그러하므로 $u(v(n))=\sum_k b_km_k=n$이다. 

이제 마지막으로 $u$가 실제로 descent datum의 isomorphism이라는 것은 $m\otimes b\otimes b'$에 두 합성을 적용하여 확인하면 되고, naturality 또한 약간의 계산을 통해 보일 수 있다.
:::

[정리 6](#thm6)의 categorical equivalence에는 논리적으로 서로 다른 두 주장이 들어 있다. Full faithfulness는 두 $A$-module $M,M'$이 이미 주어졌을 때, canonical descent datum 사이의 compatible한 $B$-module morphism $M\otimes_A B\rightarrow M'\otimes_A B$이 유일한 $A$-module morphism $M\rightarrow M'$으로부터 온다는 뜻이다. 여기서는 source와 target이 global하게 주어져 있고 그 사이의 morphism만 붙인다. 이것이 morphism에 대한 descent이다.

Essential surjectivity에서는 global $A$-module이 미리 주어져 있지 않다. 임의의 descent datum $(N,\Phi_N)$으로부터 $A$-module $M$을 찾아 $(N,\Phi_N)\cong(M\otimes_A B,\sigma_M)$으로 나타내야 하며, 위 증명에서는 이 $M$을 $N^\Phi$로 구성했다. 이것이 대상에 대한 effective descent이다. Full faithfulness만으로 essential surjectivity가 따라오지는 않으므로, morphism을 붙일 수 있다는 사실만으로 대상을 붙일 수 있는 것은 아니다.

이 정리의 직접적인 결과로, $A$-module $M$의 여러 성질을 $M$ 자신이 아니라 $B$ 위로 올린 $M\otimes_A B$에서 확인해도 된다. 가령 $M\otimes_A B$가 finitely generated $B$-module이면 $M$도 finitely generated이고, $M\otimes_A B$가 finitely presented이면 $M$도 finitely presented이며, $M\otimes_A B$가 flat이면 $M$ 역시 그러하다. 이들은 모두 해당 성질이 exact sequence로 표현되고 [명제 2](#prop2)가 그 exactness를 $A$ 위로 반영하기 때문이다.

::: 명제 7
Ring homomorphism $\phi: A \rightarrow B$가 faithfully flat이고 $M$이 $A$-module이라 하자. 그럼 $M$이 finitely generated (resp. finitely presented, flat, locally free of finite rank)인 것은 $M\otimes_A B$가 $B$-module로서 finitely generated (resp. finitely presented, flat, locally free of finite rank)인 것과 동치이다.
:::
::: 증명
$M$이 성질을 가지면 $M\otimes_A B$도 가진다는 방향은 각 성질이 base change에 대해 보존되므로 자명하고, 이 명제의 핵심은 그 반대방향들이 성립한다는 것에 있다. 

우선 $M\otimes_AB$가 $y_1,\ldots, y_n$으로 생성된다 하자. 그럼 각 $y_i$는 유한히 많은 $m_{ij}\otimes b_{ij}$의 합으로 쓸 수 있으므로, $m_{ij}$들을 모두 모아 $M$의 finitely generated submodule $M_0\subseteq M$을 정의할 수 있다. 그럼 $M_0\otimes_AB\rightarrow M\otimes_AB$가 surjective이고, 따라서 $(M/M_0)\otimes_A B=0$이므로 faithfulness에 의해 $M/M_0=0$이다. 즉 $M=M_0$은 finitely generated이다.

이제 finite presentation의 경우를 보자. 우선 이 가정에서, $M$이 finitely generated임은 이미 위에서 얻었으므로 $A^n \twoheadrightarrow M$의 kernel $K$가 finitely generated임을 보이면 충분하다. 이를 위해 exact sequence

$$0 \rightarrow K \rightarrow A^n \rightarrow M \rightarrow 0$$

을 $B$로 base change하면 

$$0 \rightarrow K\otimes_A B \rightarrow B^n \rightarrow M\otimes_A B \rightarrow 0$$

이 exact하고, $M\otimes_A B$가 finitely presented이므로 $K\otimes_A B$는 finitely generated이다. ([\[가환대수학\] §평탄성, ⁋따름정리 6](/ko/math/commutative_algebra/flatness#cor6) 이후의 논의) 따라서 위 finitely generated의 결과를 $K$에 적용하면 $K$도 finitely generated이고 $M$은 finitely presented이다.

Flatness의 경우, $M$이 flat임을 보이려면 임의의 injective $A$-module morphism $M' \hookrightarrow M''$에 대해 $M'\otimes_A M \rightarrow M''\otimes_A M$이 injective임을 보이면 된다. 역시 여기에 $-\otimes_AB$를 취하면 morphism $M'\otimes_A M\otimes_A B \rightarrow M''\otimes_A M\otimes_A B$을 얻는데, 이는 injective homomorphism $M'\otimes_A B \rightarrow M''\otimes_A B$에 flat $B$-module $M\otimes_A B$를 다시 텐서하여 얻어진 것으로 생각할 수 있으므로 다시 injective이다. 

마지막으로 locally free of finite rank는 finitely presented이면서 flat인 것과 동치이므로 ([\[가환대수학\] §평탄성, ⁋따름정리 6](/ko/math/commutative_algebra/flatness#cor6)) 더는 증명할 것이 없다.
:::

## 준연접층의 하강

이제 우리는 gluing을 위한 모든 도구를 갖추었다. 남은 것은 단지 여기에 적절한 이름을 붙여주는 것 뿐이다. 즉, open embedding의 개념을 faithfully flat morphism으로 확장하여도 gluing이 잘 작동하는 것을 보았으므로, 아예 이 faithfully flat morphism들을 가지고 <em-ko>열린집합</em-ko>의 개념을 새로 써 버리면 된다. 

::: 정의 8
Fiber product를 가지는 category $\mathcal{C}$ 위의 *Grothendieck pretopology<sub>그로텐디크 준위상</sub>*란, 각 대상 $U$에 codomain이 $U$인 morphism들의 family $\{f_i: U_i \rightarrow U\}_{i\in I}$의 모임을 대응시키는 것으로서, 그 원소를 $U$의 *covering<sub>덮개</sub>*이라 부른다. 이들은 다음 세 조건을 만족한다.

1. $f: V \rightarrow U$가 isomorphism이면 $\{f: V \rightarrow U\}$은 covering이다.
2. $\{f_i: U_i \rightarrow U\}$가 covering이고 $g: V \rightarrow U$가 임의의 morphism이면, base change가 주는 $\{U_i\times_U V \rightarrow V\}_{i\in I}$ 또한 covering이다.
3. $\{f_i: U_i \rightarrow U\}$가 covering이고 각 $i$마다 $\{g_{ij}: U_{ij} \rightarrow U_i\}_{j\in J_i}$가 covering이면, 합성이 주는 $\{f_i\circ g_{ij}: U_{ij} \rightarrow U\}_{i, j}$ 또한 covering이다.
:::

특히 $\Sch$는 fiber product를 가지므로 ([§올곱, ⁋정리 8](/ko/math/scheme_theory/fiber_products#thm8)) 이 정의를 적용할 수 있다. 위상공간의 open cover $\{U_i\}$를 inclusion들의 족 $\{U_i\hookrightarrow U\}$으로 읽으면 위의 세 조건이 성립하며, 이 때 $U_i\times_U V$는 교집합 $U_i\cap V$이다. 즉 세 조건은 자기 자신이 자기 자신을 덮는다는 것, covering을 제한한 것이 다시 covering이라는 것, covering의 covering이 covering이라는 것을 요구할 뿐이다. 우리가 쓸 topology는 faithfully flat인 morphism들이 quasi-compact 조건을 만족하는 covering을 사용하는 것으로, 그 이름 *fidèlement plat quasi-compact*를 줄여 fpqc topology라 부른다.

::: 정의 9
Scheme $X$ 위의 morphism들의 모임 $\{\psi_i: U_i \rightarrow X\}_{i\in I}$이 *fpqc cover<sub>fpqc 덮개</sub>*라는 것은, 각 $\psi_i$가 flat이고, $\coprod_i U_i \rightarrow X$가 surjective이며, 각 affine open $V\subseteq X$가 유한히 많은 $U_i$의 affine open들 $W_{ij}$의 image로 덮이는 quasi-compact 조건을 만족하는 것이다. 이러한 covering들이 정의하는 $\Sch$ 위의 Grothendieck topology를 *fpqc topology*이라 부른다.
:::

Fpqc topology에서 한 affine scheme $\Spec A$를 덮는 가장 단순한 covering은 faithfully flat ring homomorphism $A \rightarrow B$ 하나로 이루어진 $\{\Spec B \rightarrow \Spec A\}$이다. 

우리가 [보조정리 3](#lem3)을 굳이 module로 올린 것은, 당연히, quasi-coherent sheaf를 다루기 위한 것이다. ([§준연접층, ⁋정의 8](/ko/math/scheme_theory/quasicoherent_sheaves#def8))

::: 정리 10
임의의 scheme $X$와 $X$ 위의 quasi-coherent sheaf $\mathcal{F}$에 대하여, presheaf

$$T\mapsto \Gamma(T, \psi^\ast \mathcal{F})\qquad (\psi: T \rightarrow X)$$

은 fpqc topology에 대한 sheaf이다. 즉 임의의 fpqc cover $\{T_i \rightarrow T\}$에 대하여, sequence

$$\Gamma(T, \psi^\ast\mathcal{F}) \rightarrow \prod_i \Gamma(T_i, \psi_i^\ast\mathcal{F}) \rightrightarrows \prod_{i,j}\Gamma(T_i\times_T T_j, \psi_{ij}^\ast\mathcal{F})$$

는 exact하다.
:::
::: 증명
문제가 local하고 quasi-compact 조건 덕분에 finite covering으로 환원되므로, $T=\Spec A$가 affine이고 covering이 단일 faithfully flat morphism $\{\Spec B \rightarrow \Spec A\}$인 경우만 보이면 충분하다. 이 때 $\mathcal{F}=\widetilde M$인 $A$-module $M$을 택하면 pullback이 base change로 주어지므로 ([§준연접층, ⁋명제 15](/ko/math/scheme_theory/quasicoherent_sheaves#prop15)) 위 sequence는

$$M \rightarrow M\otimes_A B \rightrightarrows M\otimes_A B\otimes_A B$$

이다. 그럼 주장은 [보조정리 3](#lem3)을 $M$을 coefficient로 두어 일반화한 sequence

$$0 \rightarrow M \rightarrow M\otimes_A B \rightarrow M\otimes_A B\otimes_A B$$

의 exactness로, 이미 [정리 6](#thm6)의 증명에서 보인 것이다. 이제 두 morphism $d^0, d^1$의 equalizer가 $M$임이 곧 위의 sheaf 조건이므로 결론을 얻는다.
:::

[정리 10](#thm10)은 quasi-coherent sheaf의 global section을 faithfully flat covering 위에서 계산할 수 있게 해준다. 이로부터 quasi-coherent sheaf 자체의 descent를 얻는다.

::: 정리 11
Family $\{\psi_i: U_i \rightarrow X\}$가 fpqc cover라 하자. 그럼 $X$ 위의 quasi-coherent sheaf를 주는 것은, 각 $U_i$ 위의 quasi-coherent sheaf $\mathcal{F}_i$들과, $U_i\times_X U_j$ 위에서 cocycle 조건을 만족하는 isomorphism $\Phi_{ij}: \pr_2^\ast \mathcal{F}_j\cong \pr_1^\ast \mathcal{F}_i$들의 데이터를 주는 것과 동치이다.
:::
::: 증명
문제가 local하므로 $X=\Spec A$이고 covering이 단일한 faithfully flat morphism $\Spec B \rightarrow \Spec A$인 경우만 보면 충분하다. 그럼 이 상황에서 $U_i\times_X U_j$는 $\Spec(B\otimes_A B)$이고, 주어진 데이터는 정확히 $B$-module $N=\Gamma(\Spec B, \mathcal{F}_1)$과 $B\otimes_A B$-module isomorphism $\Phi_N$의 cocycle 쌍, 즉 [정의 4](#def4)의 descent datum이다. 이 데이터는 $\Desc(B/A)$의 대상에 정확히 대응하므로 [정리 6](#thm6)에 의해 이는 유일한 $A$-module $M$, 즉 유일한 quasi-coherent sheaf $\widetilde M$으로부터 오며, 이 correspondence는 morphism까지 보존한다.

일반적인 fpqc cover의 경우, quasi-compact 조건으로 finite subcover를 잡고 그 disjoint union을 단일한 affine faithfully flat morphism으로 만들어 위 affine 경우를 적용한 뒤, 결과들을 $X$의 affine open들 위에서 gluing하면 된다. Gluing의 consistency는 [정리 10](#thm10)의 sheaf 성질이 보장한다.
:::

역시 [정리 11](#thm11)에서 핵심적인 사실은 위의 형태의 descent datum $(\mathcal{F}_i, \Phi)$가 주어졌을 때 이들을 실제로 붙여서 단일한 sheaf $\mathcal{F}$를 붙일 수 있다는 것이다.

## 사상의 하강

이제 quasi-coherent sheaf보다 한 단계 더 기하적인 대상을 붙이는 문제를 살펴본다. 우리의 첫째 목표는 scheme들을 붙이는 것으로, fpqc cover $\{\psi_i:U_i\rightarrow S\}$가 주어졌다 하고, 각각의 $i$마다 $U_i$-scheme $V_i\rightarrow U_i$ 구조가 주어졌으며, 각각의 overlap $U_i\times_SU_j$ 위에서 이들이 cocycle condition을 만족하는 isomorphism을 통한 identification이 이미 주어져있다 하자. 우리의 목표는 이들 $U_i$-scheme들을 이어붙이는 $S$-scheme $V\rightarrow S$를 찾는 것으로, 이것이 $V_i$들을 확장한다는 조건은 다음의 isomorphism

$$V\times_SU_i\cong V_i$$

으로 주어진다. 일반적으로 이러한 구성이 항상 가능한 것은 아니며, 이를 가능하게 하는 조건 중 가장 기초적인 것은 $V_i\rightarrow U_i$들이 affine인 것이다. 

::: 정리 12
주어진 fpqc cover $\{\psi_i:U_i \rightarrow S\}$와 이들 각각 위에 정의된 affine morphism $V_i \rightarrow U_i$들, 그리고 이들을 교집합 $U_i\times_S U_j$ 위에서 identify하는 cocycle isomorphism 데이터가 주어졌다 하자. 그럼 $S$ 위의 affine morphism $V\rightarrow S$와 주어진 cocycle isomorphism들과 compatible한 isomorphism $V\times_SU_i\cong V_i$들이 존재하며, 이러한 $V$는 up to unique isomorphism으로 유일하다. 
:::
::: 증명
우리의 전략은 이미 가지고 있는 quasi-coherent sheaf의 gluing을 이용하는 것으로, 이를 위해 affine morphism들 $\varphi_i: V_i\rightarrow U_i$를 quasi-coherent $\mathcal{O}_{U_i}$-algebra

$$\mathcal{A}_i=(\varphi_i)_\ast\mathcal{O}_{V_i}$$

로 생각한다. ([§준연접층, ⁋정리 20](/ko/math/scheme_theory/quasicoherent_sheaves#thm20)) 즉 $V_i$를 relative spec $\rSpec_{U_i}(\mathcal{A}_i)$으로 생각하는 것으로, 우리는 이 quasi-coherent algebra들을 붙여서 단일한 quasi-coherent algebra를 얻은 후 이를 다시 affine morphism으로 돌려놓으면 된다. 

이제 $V_i$들 사이의 cocycle isomorphism들은 이 언어에서 $\mathcal{A}_i$들의 pullback 사이의 cocycle isomorphism으로 번역되므로, [정리 11](#thm11)을 적용하면 $S$ 위의 quasi-coherent sheaf $\mathcal{A}$와 isomorphism

$$\psi_i^\ast\mathcal{A}\cong\mathcal{A}_i$$

를 얻는다. 이제 이 위에 algebra 구조를 줘야 한다. [§준연접층, ⁋명제 22](/ko/math/scheme_theory/quasicoherent_sheaves#prop22)의 증명에서 확인했듯 pullback은 tensor product와 호환되고 $\psi_i^\ast\mathcal{O}_S\cong\mathcal{O}_{U_i}$이므로, 각 $\mathcal{A}_i$의 multiplication과 unit

$$\mu_i:\mathcal{A}_i\otimes\mathcal{A}_i\rightarrow\mathcal{A}_i,\qquad \eta_i:\mathcal{O}_{U_i}\rightarrow\mathcal{A}_i$$

은 각각 $\mathcal{A}\otimes\mathcal{A}$와 $\mathcal{A}$의 pullback 사이, 그리고 $\mathcal{O}_S$와 $\mathcal{A}$의 pullback 사이의 morphism으로 볼 수 있다. 이들은 주어진 algebra isomorphism들과 compatible하므로, [정리 11](#thm11)의 morphism에 대한 correspondence를 통해 유일한 morphism

$$\mu:\mathcal{A}\otimes\mathcal{A}\rightarrow\mathcal{A},\qquad \eta:\mathcal{O}_S\rightarrow\mathcal{A}$$

이 존재하고, 그 pullback은 각각 $\mu_i$ 및 $\eta_i$와 일치한다. Associativity와 unit law는 $U_i$ 위로 pullback하면 성립하고, fpqc cover 위에서 일치하는 sheaf morphism들은 $S$ 위에서도 일치하므로 $\mathcal{A}$는 quasi-coherent $\mathcal{O}_S$-algebra가 된다. 따라서

$$V=\rSpec_S(\mathcal{A})$$

로 두면 이는 $S$ 위의 affine scheme이다. [§준연접층, ⁋명제 22](/ko/math/scheme_theory/quasicoherent_sheaves#prop22)에 의하여 relative spectrum은 base change와 호환되므로

$$V\times_SU_i\cong\rSpec_{U_i}(\psi_i^\ast\mathcal{A})\cong\rSpec_{U_i}(\mathcal{A}_i)\cong V_i$$

이고, 이 isomorphism들은 처음에 주어진 cocycle 데이터를 회복한다. 또한 $\mathcal{A}$와 그 algebra structure가 [정리 11](#thm11)에 의해 unique isomorphism을 제외하고 유일하고 affine morphism이 그 quasi-coherent algebra로부터 복원되므로 $V$도 동일한 의미에서 유일하다.
:::

더 일반적으로, quasi-compact, quasi-separated scheme morphism $\varphi:V\rightarrow U$이 *quasi-affine*인 것은 canonical morphism $V\rightarrow\rSpec_U(\varphi_\ast\mathcal{O}_V)$가 quasi-compact open immersion인 것이다. 이 경우에도 [정리 12](#thm12)의 결론이 성립한다. 다른 방향의 일반화는 quasi-projective morphism의 경우로, morphism이 quasi-projective인 것만으로는 부족하고 ample line bundle과 그 위의 compatible한 descent datum이 함께 주어져야 한다. 대략적인 증명은 ample line bundle의 section algebra를 내려보내 relative Proj를 만들면 원래 scheme은 그 안의 open subscheme으로 나타나므로 이들을 이어붙이는 것이다. 

한편, faithfully flat base change는 exact functor일 뿐 아니라, 여기서 확인한 exactness를 원래대로 돌릴 수도 있다는 것이 핵심적인 성질이며, [명제 7](#prop7)은 이를 이용해 module의 flatness와 finiteness 조건들을 내려보냈다. 같은 논의를 affine-local하게 적용하면 이미 주어진 scheme morphism $\psi:X\rightarrow Y$의 성질도 cover 위에서 확인할 수 있다. 이를 위해 $Y$의 fpqc cover $\{Y_i\rightarrow Y\}$를 잡으면 $\psi$는 morphism

$$\psi_i:X\times_YY_i\rightarrow Y_i$$

들을 정의한다. 그럼 [명제 7](#prop7)을 scheme-theoretic하게 올리면 다음 명제의 flatness와 finiteness를 얻을 수 있으며, surjectivity와 affineness는 [정리 12](#thm12)와 같은 방식으로 처리할 수 있다. 

::: 명제 13
Scheme morphism $\psi: X\rightarrow Y$와 $Y$의 fpqc cover $\{Y_i \rightarrow Y\}$가 주어졌다 하자. 그럼 $\psi$가 다음 성질들 가운데 하나를 가지는 것은, 각 base change $\psi_i: X\times_Y Y_i \rightarrow Y_i$가 그 성질을 가지는 것과 동치이다.

> Flat, faithfully flat, affine, locally of finite type, locally of finite presentation, surjective.
:::

---

**참고문헌**

**[Vak]** R. Vakil, *The rising sea: Foundations of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/).  
**[FGA]** B. Fantechi, L. Göttsche, L. Illusie, S. Kleiman, N. Nitsure, A. Vistoli, *Fundamental algebraic geometry: Grothendieck's FGA explained*. Mathematical Surveys and Monographs. American Mathematical Society, 2005.  

---

[^1]: Ring에서는 이 두 대상이 모두 $B\otimes_AB$였다. 
