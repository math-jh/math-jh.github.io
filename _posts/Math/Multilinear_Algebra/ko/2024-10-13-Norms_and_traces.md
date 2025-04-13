---

title: "노름과 대각합"
excerpt: ""

categories: [Math / Multilinear Algebra]
permalink: /ko/math/multilinear_algebra/norms_and_traces
header:
    overlay_image: /assets/images/Math/Multilinear_Algebra/Norms_and_traces.png
    overlay_filter: 0.5
sidebar: 
    nav: "multilinear_algebra-ko"

date: 2024-10-13
last_modified_at: 2025-04-13
weight: 12

---

## 노름과 대각합의 정의

언제나처럼 commutative ring $A$가 주어졌다 하고, 이번에는 unital associative $A$-algebra $E$가 주어졌다 하자. 그럼 임의의 $E$-module은 항상 restriction of scalar를 통해 $A$-module로 생각할 수 있다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> $E$-module $M$이 주어졌다 하고, $M$이 $A$-module로서 유한한 basis를 갖는다 하자. 임의의 $\alpha\in E$에 대하여, 다음의 $E$-module endomorphism

$$\alpha_M: x\mapsto \alpha x$$

이 주어졌다 하자. 그럼 $\alpha_M$의 trace, determinant, characteristic polynomial을 각각 $\alpha$의 *trace*, *norm*, *characteristic polynomial*이라 부르고,

$$\tr_{M/A}(\alpha)=\tr(\alpha_M),\qquad N_{M/A}(\alpha)=\det(\alpha_M),\qquad \chi_{M/A,\alpha}(\x)=\chi_{\alpha_M}(\x)$$

으로 표기한다.

</div>

그럼 trace와 determinant의 성질로부터

$$\tr_{M/A}(\alpha+\beta)=\tr_{M/A}(\alpha)+\tr_{M/A}(\beta),\qquad \tr_{M/A}(\alpha\beta)=\tr_{M/A}(\beta\alpha),\qquad N_{M/A}(\alpha\beta)=N_{M/A}(\alpha)N_{M/A}(\beta)$$

를 얻는다. 또, 이들을 행렬의 trace, determinant, characteristic polynomial로 볼 수 있는 것도 앞선 글에서 살펴보았다. 

특히 만일 commutative $A$-algebra $A'$가 주어졌다 하자. 그럼 $M'=A'\otimes_AM$, $E'=A'\otimes_AE$를 통해 $M'$을 $E'$-module로 볼 수 있고, 이 때의 basis는 $1\in A'와 $M$의 $E$-basis를 텐서한 것으로 주어지므로, 다시 행렬 표현으로부터 

$$\tr_{M'/A'}(1 \otimes \alpha) = \tr_{M/A}(\alpha) \cdot 1,\qquad N_{M'/A'}(1 \otimes \alpha) = N_{M/A}(\alpha) \cdot 1,\qquad\chi_{M'/A',\,1 \otimes \alpha}(x) = \chi_{M/A,\,\alpha}(x) \cdot 1
$$

임을 안다. 특히 $A' = A[\x]$일 때는

$$\chi_{M/A,\,\alpha}(\x) = N_{M[\x]/A[\x]}(\x - \alpha)$$

가 성립한다.

주목할 만한 사실은 위의 선택은 $M$의 isomorphism class에만 의존한다는 것이다. 이는 $M$에서 $M'$로의 isomorphism이 있다면 이 isomorphism을 따라 $M$의 basis가 $M'$의 basis로 옮겨지며, 이 basis에 대해 $\alpha_{M'}$을 행렬로 나타낸 것이 원래의 basis에 대해 $\alpha_M$을 행렬로 나타낸 것과 같기 때문이다. 다음 명제도 비슷한 방식으로 증명할 수 있다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> $E$-module $M$의 submodule들의 decreasing sequence

$$M = M_0 \supset M_1 \supset \cdots \supset M_r = \{0\}$$

가 주어졌다 하고, 각 $P_i := M_{i-1}/M_i$가 $A$-module로 finitely generated라 하자. 

그럼 $M$ 역시 $A$-module로서 finite basis를 가지며, 모든 $\alpha \in E$에 대해 다음의 식

$$\tr_{M/A}(\alpha) = \sum_{i=1}^r \tr_{P_i/A}(\alpha),\qquad
N_{M/A}(\alpha) = \prod_{i=1}^r N_{P_i/A}(\alpha),\qquad
\chi_{M/A,\alpha}(x) = \prod_{i=1}^r \chi_{P_i/A,\alpha}(x)$$

이 성립한다. 

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$P\_i$의 $A$-basis를 $\mathcal{B}\_i'$라 하자. 이들을 lift하면 $M\_{i-1}$의 supplementary $A$-submodule $\mathcal{B}\_i$의 basis로 확장할 수 있고, 그 합집합 $\mathcal{B} = \bigcup \mathcal{B}\_i$는 $M$의 $A$-basis가 된다. 이제 각 $\alpha \in E$에 대해, endomorphism $\alpha\_{P\_i}$의 $\mathcal{B}\_i$에 대한 행렬을 $X\_{ii}$라 하면, $\alpha\_M$의 전체 행렬

$$e_M \sim
\begin{pmatrix}
X_{rr} & * & \cdots & * \\
0 & X_{r-1,r-1} & \cdots & * \\
\vdots & \ddots & \ddots & \vdots \\
0 & \cdots & 0 & X_{11}
\end{pmatrix}$$

은 block upper-triangular 형태를 가지며 각 대각블록이 $X\_{ii}$가 된다. 이제 trace는 대각합, determinant는 대각곱, characteristic polynomial은 대각 항들의 곱으로 주어지므로 명제가 성립한다.

</details>

같은 원리로 다음이 성립한다. 

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> $E, E'$를 $A$-algebra라 하고, $M$과 $M'$을 각각 $E$, $E'$-module이라 하자.  
$M$과 $M'$이 각각 $A$-module로서 free이고, 각각 rank $n$, $n'$을 갖는다 하자. 먼알 $M \otimes_A M'$은 $E \otimes_A E'$-module로 취급한다면, 임의의 $\alpha \in E$, $\alpha' \in E'$에 대해 다음의 식

$$\tr_{M \otimes M'/A}(\alpha \otimes \alpha') = \tr_{M/A}(\alpha) \cdot \tr_{M'/A}(\alpha'),\qquad N_{M \otimes M'/A}(\alpha \otimes \alpha') = N_{M/A}(\alpha)^{n'} \cdot N_{M'/A}(\alpha')^n$$

이 성립한다. 

</div>

이제 우리는 본격적인 정의에 들어간다. 본질적으로 norm은 determinant이고, determinant는 행렬의 가역성을 판단하는 도구이므로 다음이 성립하는 것은 이상한 일이 아니다. 

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> $E$가 유한한 $A$-basis를 갖는 $A$-algebra라고 하자.  
$\alpha \in E$가 invertible하기 위한 필요충분조건은 $N_{E/A}(\alpha)$가 $A$에서 invertible인 것이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$\alpha$가 $E$에서 inverse $\alpha' \in E$를 갖는다고 하자. 이때

$$N_{E/A}(\alpha)N_{E/A}(\alpha') = N_{E/A}(\alpha\alpha') = N_{E/A}(1) = 1$$

이므로 $N_{E/A}(\alpha)$는 $A$에서 invertible이다.

반대로, $N_{E/A}(\alpha)$가 $A$에서 invertible이라 하자. 그러면 $A$-module endomorphism

$$h : x \mapsto \alpha x$$

는 injective이고 $E$는 finitely generated이므로 $h$는 bijective이다. 이제 $\alpha\alpha' = 1$인 $\alpha' \in E$를 잡으면,

$$h(\alpha'\alpha- 1) = \alpha\alpha'\alpha - \alpha = (\alpha'\alpha - 1)\alpha = 0$$

이므로 $\alpha'\alpha = 1$이 되고, $\alpha'$는 $\alpha$의 inverse가 된다.

</details>