---

title: "값매김환"
excerpt: "Valuative criteria for separated, properness"

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/valuative_criteria
header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Valuative_criteria.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_geometry-ko"

date: 2024-05-24
last_modified_at: 2024-05-24
weight: 12

---

이번 글에서 우리는 separated morphism과 proper morphism을 정의한다. 이들은 위상수학에서 Hausdorff 조건과 compact 조건을 대수기하로 옮겨온 것이라고 생각하면 편하다. 

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 임의의 scheme $X$이 주어졌다 하자.

1. $X$의 열린집합 $U$에 대하여, scheme $(U, \mathcal{O}\_X\vert\_U)$를 $X$의 *open subscheme*이라 부른다. $f:X \rightarrow Y$이 $X$와 $Y$의 open subscheme 사이의 isomorphism을 유도하면 $f$를 *open immersion*이라 부른다.
2. Scheme morphism $f:Y \rightarrow X$가 *closed immersion*이라는 것은 $\lvert Y\rvert$가 $f$에 의하여 $\lvert X\rvert$의 닫힌집합으로의 homeomorphism을 정의하고, $f^\sharp: \mathcal{O}\_X \rightarrow f\_\ast \mathcal{O}_Y$가 surjective인 것이다.  
만일 두 closed immersion $f:Y \rightarrow X$와 $f': Y' \rightarrow X$에 대하여, isomorphism $i:Y' \rightarrow Y$가 존재하여 $f'=f\circ i$이도록 할 수 있다면 $f$와 $f'$를 equivalent한 closed immersion들이라 생각하고, 이 때 equivalence class를 *closed subscheme*으로 정의한다. 이와 같은 closed subscheme이 주어졌을 때, $f^\sharp$의 kernel $\mathcal{I}_Y$를 *ideal sheaf*라 부른다. 
3. $f:X \rightarrow Y$가 *projective*라는 것은 적당한 $n$에 대하여, $f$를 closed immersion과 projection의 합성 $X\hookrightarrow \mathbb{P}^n_Y \rightarrow Y$의 꼴로 분해할 수 있는 것이다. 
4. $f:X \rightarrow Y$가 *quasi-projective*라는 것은 이를 적당한 open immersion $X \rightarrow X'$와 projective morphism $X' \rightarrow Y$의 합성으로 ㅅ분해할 수 있는 것이다. 

</div>

## 이산값매김환

본격적인 이야기를 시작하기 전에 다음 예시를 살펴보는 것이 좋다. 

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins> Ring $A$가 discrete valuation ring이라 하자. 즉 $A$는 principal ideal domain이곤 두 개의 prime ideal들 $(0)$, $\mathfrak{m}$을 가지며 이 중 $\mathfrak{m}$은 $A$의 유일한 maximal ideal로서 non-unit들의 모임이다. 

이로부터 $\Spec A$는 두 개의 점 $(0)$, $\mathfrak{m}$으로 이루어져 있으며,

$$V((0))=\{(0),\mathfrak{m}\},\quad V(\mathfrak{m})=\{\mathfrak{m}\}$$

이므로 $\Spec A$의 자명하지 않은 열린집합은

$$D(\mathfrak{m})=\{(0)\}$$

뿐이다. 한편 $\mathfrak{m}=(\pi)$라 하면 [§스펙트럼, ⁋명제 5](/ko/math/algebraic_geometry/spectrums#prop5)에 의하여

$$\mathscr{O}(D(\mathfrak{m}))=\mathscr{O}(D(\pi))\cong A_\pi\cong \Frac(A)$$

이다. 물론 $\mathscr{O}(\Spec A)\cong A$이다. 

한편 [§스킴, ⁋예시 6](/ko/math/algebraic_geometry/schemes#ex6)에서 우리는 기하적으로 $\Spec A$의 두 점을 살펴보는 방법을 보았다. 이에 따르면 $\Spec A$의 두 점은 각각 $A$에서 residue field $\kappa((0))$, $\kappa(\mathfrak{m})$으로 가는 ring homomorphism에 의해 결정되는데, 다시 [§스펙트럼, ⁋명제 5](/ko/math/algebraic_geometry/spectrums#prop5)을 사용하면

$$\mathscr{O}_{(0)}\cong A_{(0)}\cong \Frac(A),\qquad \mathscr{O}_\mathfrak{m}\cong A_\mathfrak{m}$$

으로부터 

$$\kappa((0))=\Frac(A), \qquad \kappa(\mathfrak{m})=A_\mathfrak{m}/\mathfrak{m}A_\mathfrak{m}\cong \Frac(A/\mathfrak{m})\cong A/\mathfrak{m}$$

을 얻는다. 

</div>

## 분리사상

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> Scheme morphism $f:X \rightarrow Y$에 대하여, *diagonal morphism<sub>대각사상</sub>*을 $\Delta: X \rightarrow X \times_Y X$으로 정의한다. 

![diagonal_morphism](/assets/images/Math/Algebraic_Geometry/Valuative_criteria-1.png){:width="275.4px" class="invert" .align-center}

만일 $\Delta$가 closed immersion이라면 $f$를 *separated<sub>분리사상</sub>*라 부르고, $X$가 $Y$에 대해 *seperated*라 부른다. 만일 $X$가 $\Spec \mathbb{Z}$에 대해 separated이면, $X$를 간단히 *separated* scheme이라 부른다.

</div>

대수기하학에서는 separatedness가 Hausdorff를 대체하는 성질이라 생각하는데, 이는 다음 명제 때문이다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> $f:X \rightarrow Y$가 separated인 것과, diagonal morphism $\Delta: X \rightarrow X\times_YX$에 의한 $X$의 image가 닫힌집합인 것이 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

정의에 의하여 $f$가 separated라면 $\Delta(X)$가 닫혀있음은 자명하다. 따라서 $\Delta(X)$가 closed임을 가정하고, $\Delta$가 closed immersion임을 보여야 한다. $\Delta(X)$가 $X\times_YX$의 닫힌집합이 되는 것은 자명하므로, $\mathcal{O}\_{X\times\_YX} \rightarrow \Delta_\ast \mathcal{O}_X$가 surjective임을 보이면 충분하다. 한편 sheaf morphism의 surjectivity는 stalk 위에서 체크할 수 있다. 임의의 $p\in X$를 택하자. 그럼 우선 $p$의 open affine subset $U$를 택할 수 있으며, 필요하다면 $U$를 제한하여 $f(U)$가 $Y$의 어떠한 open affine subset $V$에 속하도록 할 수 있다. 그럼 $U\times_VU$는 $\Delta(p)$의 open neighborhood이며, 이 위에서 $\Delta: U \rightarrow U\times_VU$는 다음의 [보조정리 4](#lem4)에 의하여 closed immersion이 되고, 증명이 완료된다.

</details>

<div class="proposition" markdown="1">

<ins id="lem5">**보조정리 5**</ins> Affine scheme 사이의 임의의 morphism $f:X \rightarrow Y$는 항상 separated이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$X=\Spec A, Y=\Spec B$라 하면 $\Delta$가 ring homomorphism 

$$A\otimes_BA \rightarrow A;\quad a\otimes a'\mapsto aa'$$

으로부터 유도되며, 이것이 surjective이므로 자명하다. 

</details>

Separated가 아닌 scheme의 예시는 [§스킴, ⁋예시 6](/ko/math/algebraic_geometry/schemes#ex6)에서 만든 line with double origin이 있다. 편의상 이 scheme을 $X$라 하자. 그럼 $X\times X$는 축 바깥에서는 일반적인 좌표평면과 똑같을 것이지만 좌표축, 특히 원점을 보면 네 개의 원점이 들어가게 된다. 직관적으로는 $\Delta$가 
$X\times X$에 어떻게 들어갈지를 생각해보면 좌표축 바깥에서는 일반적인 대각선 모양이 될 것이지만, $X$의 두 원점이 $\Delta$를 통해 $X\times X$로 옮겨졌을 때, 이 네 원점 중 어느 두 개에 들어갈지를 알 수 없다. 실제로 이 네 원점은 모두 $\Delta(X)$의 closure에 들어가므로 separated가 아닌 것을 알 수 있다. 역시, 위상수학에서 이 공간은 Hausdorff가 아닌 공간의 예시였다. 

<div class="proposition" markdown="1">

<ins id="thm6">**정리 6**</ins> Noetherian scheme $X$와 scheme morphism $f:X \rightarrow Y$에 대하여, $f$가 separated인 것은 임의의 valuation ring $A$과 그 quotient field $K=\Frac(A)$에 대하여, 임의의 scheme morphism $\Spec A \rightarrow Y$, $\Spec K \rightarrow X$와 다음 commutative diagram

![valuative_criterion_for_separatedness](/assets/images/Math/Algebraic_Geometry/Valuative_criteria-2.png){:width="173.85px" class="invert" .align-center}

의 바깥쪽 square가 주어질 때마다, 많아야 하나의 $\Spec A \rightarrow X$가 전체 diagram이 commute하도록 하는 것이 동치이다.

</div>

이 명제는 별도로 증명하지 않지만, 만일 $Y$가 noetherian이고 $f$가 finite type morphism이라면 위의 정리를 임의의 valuation ring이 아니라, 임의의 discrete valuation ring으로 대체해도 된다는 것이 알려져 있다. 이렇게 바꿔두고 나면 기하학적 직관을 이용해 정리를 설명하기가 쉬워지는데, $\Spec A$를 smooth curve의 germ을 나타내는 것으로 생각하고 $\Spec K$는 여기에서 한 점이 빠져있는 것으로 생각하면 위의 정리는 이러한 $\Spec K\hookrightarrow \Spec A$를 넣는 방법이 하나 뿐이라는 것을 말해준다. 

그럼 이로부터 다음을 얻는다.

<div class="proposition" markdown="1">

<ins id="cor7">**따름정리 7**</ins> Noetherian scheme들에 대하여, 

1. Open immersion과 closed ummersion은 모두 separated이다. 
2. 두 separated morphism의 합성은 separated이다.
3. Separated morphism은 base change에 의해 보존된다.
4. Separated morphism은 fiber product에 의해 보존된다.
5. 만일 $f:X \rightarrow Y$, $g:Y \rightarrow Z$가 scheme morphism들이고 $g\circ f$가 separated morphism이라면 $f$ 또한 separated morphism이다.

</div>

## 고유사상

<div class="definition" markdown="1">

<ins id="def8">**정의 8**</ins> $f:X \rightarrow Y$가 *universally closed*라는 것은 $f$가 closed map이고, 임의의 $Y' \rightarrow Y$에 대해서도 $X\times_Y Y' \rightarrow Y'$가 closed인 것이다. Separated, universally closed인 finite type morphism을 *proper morphism<sub>고유사상</sub>*이라 부른다. 

</div>

[정리 6](#thm6)과 마찬가지로 proper morphism에 대해서도 valuative criterion이 존재한다.

<div class="proposition" markdown="1">

<ins id="thm6">**정리 6**</ins> Noetherian scheme $X$와 scheme morphism $f:X \rightarrow Y$에 대하여, $f$가 separated인 것은 임의의 valuation ring $A$과 그 quotient field $K=\Frac(A)$에 대하여, 임의의 scheme morphism $\Spec A \rightarrow Y$, $\Spec K \rightarrow X$와 다음 commutative diagram

![valuative_criterion_for_separatedness](/assets/images/Math/Algebraic_Geometry/Valuative_criteria-2.png){:width="173.85px" class="invert" .align-center}

의 바깥쪽 square가 주어질 때마다, 정확히 하나의 $\Spec A \rightarrow X$가 존재하여 전체 diagram이 commute하는 것이 동치이다.

</div>

마찬가지로 다음 따름정리가 성립한다.

<div class="proposition" markdown="1">

<ins id="cor9">**따름정리 9**</ins> Noetherian scheme들에 대하여,

1. Closed immersion은 proper이다.
2. Proper morphism들의 합성은 proper이다. 
3. Proper morphism은 base change에 의해 보존된다.
4. Proper morphism은 fiber product에 의해 보존된다.
5. 만일 $f:X \rightarrow Y$, $g:Y \rightarrow Z$가 scheme morphism들이고 $g\circ f$가 proper morphism이라면 $f$ 또한 proper morphism이다.

</div>

<div class="proposition" markdown="1">

<ins id="thm10">**정리 10**</ins> Noetherian scheme들 사이의 projective morphism은 proper morphism이고, quasi-projective morphism은 separated, finite type morphism이다. 

</div>