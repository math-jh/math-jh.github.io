---

title: "Ext와 Tor"
excerpt: ""

categories: [Math / Homological Algebra]
permalink: /ko/math/homological_algebra/ext_and_tor
header:
    overlay_image: /assets/images/Math/Homological_Algebra/Ext_and_Tor.png
    overlay_filter: 0.5
sidebar: 
    nav: "homological_algebra-ko"

date: 2024-11-06
last_modified_at: 2024-11-06
weight: 6

---

앞선 글에서 우리는 일반적인 left/right exact functor에 대한 right/left derived functor를 정의했다. 이번 글에서 우리는 특별히 $\lMod{A}$에서 정의된 left exact functor $\Hom$, right exact functor $\otimes$의 derived functor에 대해 살펴본다.

## Ext 함자의 정의

임의의 $M\in\lMod{A}$에 대하여, $\Hom_\lMod{A}(M,-)$은 $\lMod{A}$에서 $\Ab$로의 left exact functor이다. 따라서 다음을 정의한다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Left exact functor $\Hom_\lMod{A}(M,-):\lMod{A} \rightarrow \Ab$의 right derived functor를

$$\Ext_A^i(M,N)=R^i\Hom_\lMod{A}(M,-)(N)$$

으로 정의하고, 이들을 *$\Ext$ group*들이라 부른다.

</div>

$\Hom_\lMod{A}(-,N)$가 exact functor인 것이 $N$가 injective object인 것과 동치이다. ([\[다중선형대수학\] §사영가군, 단사가군, 평탄가군, ⁋정의 3](/ko/math/multilinear_algebra/various_modules#def3)) 이를 derived functor를 사용해서 보면, 만일 $N$이 injective module이었다면 $0 \rightarrow N \rightarrow N \rightarrow 0$이 injective resolution이 되고, 따라서 $\Ext_A^1(M,N)=0$이 모든 $M$에 대해 성립하는 것을 안다. 그럼 임의의 short exact sequence

$$0 \rightarrow M_1 \rightarrow M_2 \rightarrow M_3 \rightarrow 0$$

에 $\Hom_\lMod{A}(-,N)$을 취하고, 그 derived functor를 생각하여 얻어지는 다음의 long exact sequence

$$\begin{aligned}0 &\rightarrow \Hom_\lMod{A}(M_3, N) \rightarrow \Hom_\lMod{A}(M_2, N) \rightarrow \Hom_\lMod{A}(M_1, N)\\ 
&\rightarrow\Ext_A^1(M_3,N) \rightarrow\Ext_A^1(M_2,N) \rightarrow\cdots\end{aligned}$$

에서, $\Ext_A^1(M_3,N)=0$이 성립하므로 $\Hom_\lMod{A}(-,N)$이 exact라는 것을 알 수 있다. 

한편, [정의 1](#def1) 대신 우리는 고정된 $N$에 대하여 $\Hom_\lMod{A}(-,N):\lMod{A} \rightarrow \Ab$를 생각한 후 이 left exact functor의 right derived functor로서 $\Ext$를 정의할 수도 있었을 것이다. 이 두 정의가 같다는 것은 <#ref#>에서 확인할 수 있다.

## Tor 함자의 정의

임의의 $N\in\rMod{A}$에 대하여, $-\otimes_A N$은 $\lMod{A}$에서 $\Ab$로의 right exact functor이므로, left derived functor를 생각할 수 있다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> Right exact functor $-\otimes_A N:\lMod{A} \rightarrow \Ab$의 left derived functor를

$$\Tor_i^A(M,N)=L_i(-\otimes_A N)(M)$$

으로 정의하고, 이들을 *$\Tor$ group*들이라 부른다.

</div>

$\Tor$를 계산하기 위해서는 $N$의 projective resolution을 사용해야 한다. 따라서, 앞선 문단에서의 계산과 마찬가지로 $N$이 projective $A$-module이었다면 $0 \rightarrow N \rightarrow N \rightarrow 0$이 $N$의 projective resolution이 되고, 이로부터 $\Tor_1^A(M,N)=0$이 모든 $M$에 대해 성립했을 것이다. 즉, 임의의 projective $A$-module은 flat $A$-module임을 다시 한 번 확인할 수 있다. 

## Balancing

