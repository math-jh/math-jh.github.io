---

title: "기저변환"
excerpt: "기저변환행렬"

categories: [Math / Linear Algebra]
permalink: /ko/math/linear_algebra/change_of_basis
sidebar: 
    nav: "linear_algebra-ko"

header:
    overlay_image: /assets/images/Linear_algebra/Change_of_basis.png
    overlay_filter: 0.5

date: 2022-08-30
last_modified_at: 2022-08-30

weight: 14

---

우리는 [선형대수학의 기본정리]()로부터, 두 $F$-벡터공간 $V,W$에 basis의 선택이 주어진다면 임의의 linear map $L:V\rightarrow W$를 그 행렬표현 $[L]_\mathcal{C}^\mathcal{B}$와 동일하게 취급할 수 있다는 것을 살펴보았다. 이제 우리는 basis가 바뀌었을 때 이 표현들이 어떻게 바뀌는지를 살펴본다. 

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> 임의의 유한차원 $F$-벡터공간 $V$와, $V$의 두 basis $\mathcal{B},\mathcal{B}'$에 대하여, $\mathcal{B}$에서 $\mathcal{B}'$로의 *change-of-basis matrix<sub>기저변환행렬</sub>*은 

$$[\operatorname{id}_V]_{\mathcal{B}'}^\mathcal{B}$$

를 의미한다.

</div>

벡터공간의 차원이 잘 정의된다는 것으로부터 이러한 행렬은 반드시 정사각행렬이 되어야 한다는 것이 자명하다. 또, 다음의 식

$$I=[\operatorname{id}_V]^{\mathcal{B}}_{\mathcal{B}}=[\operatorname{id}_V]_{\mathcal{B}}^{\mathcal{B}'}[\operatorname{id}_V]^\mathcal{B}_{\mathcal{B}'}$$

으로부터 이러한 행렬은 항상 가역이라는 것을 알 수 있다.

Change-of-basis matrix가 어떤 방식으로 작동하는지를 살펴보기 위해, 유한차원 $F$-벡터공간 $V$를 고정하고, $V$ 위에 정의된 두 basis $\mathcal{B},\mathcal{B}'$가 주어졌다 하자. 선형대수학의 기본정리는 다음의 diagram이 commute한다는 것을 의미한다.

![change_of_basis](/assets/images/Linear_algebra/Change_of_basis-1.png){:width="144.00px" class="invert" .align-center}

이 때 두 개의 수직방향 함수는 각각 $v\mapsto [v]\_\mathcal{B}$와 $v\mapsto[v]\_{\mathcal{B}'}$를 의미한다. 따라서 change-of-basis matrix는 $v\in V$의 $\mathcal{B}$에 대한 좌표표현을 받아, $\mathcal{B}'$에 대한 좌표표현으로 바꾸어주는 행렬이라 생각할 수 있다. 더 일반적으로 임의의 linear map $L:V\rightarrow W$가 주어졌다 하고, $V,W$의 basis $\mathcal{B},\mathcal{C}$, 그리고 또 다른 basis $\mathcal{B}',\mathcal{C}'$가 주어졌다 하면, 선형대수학의 기본정리로부터 다음의 식

$$[L]_{\mathcal{C}'}^{\mathcal{B}'}=[\operatorname{id}_W]_{\mathcal{C}'}^\mathcal{C}[L]_{\mathcal{C}}^\mathcal{B}[\operatorname{id}_V]^{\mathcal{B}'}_{\mathcal{B}}$$

를 얻는다.

두 $n\times n$ 행렬 $A,B$가 주어졌다 하자. 그럼 위의 식에서부터, 만일 적당한 두 가역행렬 $P,Q$가 존재하여 다음의 식

$$B=PAQ$$

를 만족한다면, 이 둘을 같은 것으로 취급하고 싶은 유혹이 있다. 물론 이 관계는 동치관계지만, 