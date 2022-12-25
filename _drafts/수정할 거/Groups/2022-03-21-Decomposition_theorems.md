---

title: "분해정리"
excerpt: "Decomposition_theorems"

categories: [Math / Groups]
permalink: /ko/math/groups/decomposition_theorems
header:
    overlay_image: /assets/images/Groups/Group_action.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_structures"

date: 2022-03-21
last_modified_at: 2022-03-21
weight: 6

published: false

---
<div class="notice--warning" markdown="1">

이 글은 현재 수정중입니다.

이 글은 예전에 쓴 글로, 서술 방향이 마음에 들지 않거나 표기법이 마음에 들지 않아 전체적으로 수정이 진행중입니다. 읽으실 때 참고해주세요.

</div>


<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> 두 group $F,G$가 주어졌다 하자. Group $G$를 $F$를 통해 *extend*한다는 것은 다음과 같은 성질을 만족하는 triple $(E,i,p)$를 찾는 것이다.

1. $E$는 group이며, $i:F\rightarrow E$는 injective homomorphism, $p:F\rightarrow G$는 surjective homomorphism이다.
2. $\imi=\ker p$가 성립한다.

이 때, $r\circ i=\id_F$를 만족하는 $r:E\rightarrow F$와, $p\circ s=\id_G$를 만족하는 $s:G\rightarrow E$를 각각 이 extension의 *retraction*과 *section*이라 부른다. ([Set Theory, §함수, 정의 10](/ko/math/set_theory/functions#df10))

</div>

그럼 $E$의 normal subgroup 중, $F$와 isomorphic한 normal subgroup $F'$가 존재하며 $E/F'\cong G$가 성립한다. 거꾸로 이러한 조건이 만족되면 $E$를 $F$를 통한 $G$의 extension으로 볼 수 있다는 것 또한 자명하다. 

Diagram을 통해 설명하자면 $E$가 $F$를 통한 $G$의 extension이라는 것은 

---
**Reference**

**[Bou]** Bourbaki, N., *Algebra I*, Elements of Mathematics, Springer, 1989.  
**[Hun]** Thomas W. Hungerford, *Algebra*, Graduate texts in mathematics, Springer, 2003.

---
