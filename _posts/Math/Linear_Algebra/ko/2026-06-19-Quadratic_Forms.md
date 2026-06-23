---
title: "이차형식과 실베스터 관성법칙"
description: "대칭 쌍선형형식으로부터 이차형식을 정의하고, 실수 위에서 적절한 기저를 택하면 대각형으로 환원됨을 보인다. 나아가 부호수가 기저의 선택과 무관함을 주장하는 실베스터 관성법칙을 증명한다."
excerpt: "실수 대칭 쌍선형형식의 분류"

categories: [Math / Linear Algebra]
permalink: /ko/math/linear_algebra/quadratic_forms
sidebar: 
    nav: "linear_algebra-ko"


date: 2026-06-19

weight: 125

published: false

---

앞서 우리는 쌍선형형식을 정의하고, $$\ch\mathbb{K}\neq 2$$인 field 위에서 symmetric non-degenerate bilinear form이 항상 orthogonal basis를 가짐을 보았다. ([§쌍선형형식, ⁋명제 7](/ko/math/linear_algebra/bilinear_form#prop7)) 이제 우리는 $$\mathbb{K}=\mathbb{R}$$인 경우에 집중하여, symmetric bilinear form이 적절한 기저 위에서 얼마나 단순한 형태로 환원되는지를 살펴본다. 이 글에서 다루는 모든 bilinear form은 symmetric인 것으로 가정한다. 

## 이차형식

Symmetric bilinear form은 두 벡터를 입력받지만, 두 입력에 같은 벡터를 넣으면 한 벡터에 대한 함수를 얻는다. 

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> $$\mathbb{R}$$-벡터공간 $$V$$ 위에 정의된 symmetric bilinear form $$\langle -,-\rangle$$에 대하여, 다음의 식

$$Q(v)=\langle v,v\rangle$$

으로 정의된 함수 $$Q:V\rightarrow\mathbb{R}$$을 $$\langle-,-\rangle$$에 대응되는 *이차형식<sub>quadratic form</sub>*이라 부른다.

</div>

이차형식은 원래의 bilinear form의 정보를 모두 담고 있다. 임의의 $$v,w\in V$$에 대하여 

$$Q(v+w)=\langle v+w,v+w\rangle=\langle v,v\rangle+2\langle v,w\rangle+\langle w,w\rangle=Q(v)+2\langle v,w\rangle+Q(w)$$

이므로, 다음의 식

$$\langle v,w\rangle=\frac{1}{2}\bigl(Q(v+w)-Q(v)-Q(w)\bigr)\tag{1}$$

이 성립하기 때문이다. 이 식을 *편극항등식<sub>polarization identity</sub>*이라 부른다. 즉 $$\mathbb{R}$$ 위에서 symmetric bilinear form과 이차형식은 서로를 유일하게 결정하며, 우리는 둘을 자유롭게 오갈 수 있다. 식 (1)이 성립하는 데에는 $$2$$로 나눌 수 있다는 사실, 즉 $$\ch\mathbb{R}\neq 2$$이라는 사실이 본질적으로 쓰였다.

## 합동과 대각형

$$V$$ 위에 symmetric bilinear form $$\langle -,-\rangle$$이 주어졌다 하고, $$V$$의 basis $$\mathcal{B}$$를 택하자. 그럼 [§쌍선형형식, §§Gram matrix](/ko/math/linear_algebra/bilinear_form#gram-matrix)에서 살펴본 대로, $$(i,j)$$ 성분이 $$\langle x_i,x_j\rangle$$인 Gram matrix $$G_\mathcal{B}$$에 대하여 $$\langle v,w\rangle=[v]_\mathcal{B}^tG_\mathcal{B}[w]_\mathcal{B}$$이 성립하며, $$\langle-,-\rangle$$이 symmetric이므로 $$G_\mathcal{B}$$는 대칭행렬이다. 또 다른 basis $$\mathcal{C}$$를 택하면, 기저변환행렬 $$P=[\id]_\mathcal{C}^\mathcal{B}$$에 대하여 

$$G_\mathcal{C}=P^tG_\mathcal{B}P$$

이 성립함을 보았다. 이렇게 가역행렬 $$P$$에 대하여 $$G'=P^tGP$$의 관계로 이어지는 두 대칭행렬 $$G,G'$$을 서로 *합동<sub>congruent</sub>*이라 부른다. 즉 같은 bilinear form을 서로 다른 basis로 적은 Gram matrix들은 서로 합동이다. 우리의 목표는 합동인 행렬들 가운데 가장 단순한 대표를 찾는 것이다. 

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> $$\mathbb{R}$$-벡터공간 $$V$$ 위에 정의된 임의의 symmetric bilinear form $$\langle-,-\rangle$$에 대하여, $$V$$의 적당한 basis $$\{e_1,\ldots, e_n\}$$이 존재하여 $$i\neq j$$일 때 $$\langle e_i,e_j\rangle=0$$이고, 각 $$\langle e_i,e_i\rangle$$은 $$1$$, $$-1$$, $$0$$ 중 하나이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 orthogonal basis의 존재성을 $$\dim V$$에 대한 귀납법으로 보인다. $$\dim V=0$$이거나 $$\langle-,-\rangle$$이 항등적으로 $$0$$인 경우, $$V$$의 임의의 basis가 조건을 만족하므로 보일 것이 없다. 그렇지 않다면 $$\langle u,v\rangle\neq 0$$인 $$u,v$$가 존재하고, 

$$2\langle u,v\rangle=\langle u+v,u+v\rangle-\langle u,u\rangle-\langle v,v\rangle$$

에서 좌변이 $$0$$이 아니므로 우변의 세 항 중 적어도 하나는 $$0$$이 아니다. 즉 $$\langle w,w\rangle\neq 0$$인 $$w\in V$$가 존재한다. 이제 $$W=\span w$$라 하면 $$\langle w,w\rangle\neq 0$$으로부터 임의의 $$v\in V$$를 

$$v=\frac{\langle v,w\rangle}{\langle w,w\rangle}w+\left(v-\frac{\langle v,w\rangle}{\langle w,w\rangle}w\right)$$

으로 적어 $$V=W\oplus w^\perp$$임을 알 수 있다. ([§쌍선형형식, ⁋명제 7](/ko/math/linear_algebra/bilinear_form#prop7)의 증명과 같다.) 여기서 $$w^\perp=\{v\mid\langle v,w\rangle=0\}$$이다. $$w^\perp$$로 제한한 bilinear form도 symmetric이므로 귀납적 가정에 의하여 $$w^\perp$$의 orthogonal basis가 존재하고, 여기에 $$w$$를 더하면 $$V$$의 orthogonal basis $$\{f_1,\ldots,f_n\}$$을 얻는다. 

이제 각 $$f_i$$를 적절히 스칼라배하여 $$\langle f_i,f_i\rangle$$을 $$1$$, $$-1$$, $$0$$ 중 하나로 만든다. 만일 $$\langle f_i,f_i\rangle=0$$이라면 $$e_i=f_i$$로 두고, 그렇지 않다면 $$c=\sqrt{\lvert\langle f_i,f_i\rangle\rvert}$$에 대하여 $$e_i=f_i/c$$로 두면 

$$\langle e_i,e_i\rangle=\frac{\langle f_i,f_i\rangle}{\lvert\langle f_i,f_i\rangle\rvert}=\pm 1$$

이 된다. 스칼라배는 orthogonality를 보존하므로 $$\{e_1,\ldots,e_n\}$$은 원하는 조건을 모두 만족하는 basis이다.

</details>

[명제 2](#prop2)의 basis에 대한 Gram matrix는 대각성분이 $$1$$, $$-1$$, $$0$$인 대각행렬이다. 기저를 적절히 재배열하면, 이 대각행렬을 $$1$$이 $$p$$개, $$-1$$이 $$q$$개, $$0$$이 $$r$$개 나타나는 다음의 꼴

$$\begin{pmatrix}I_p&&\\&-I_q&\\&&0_r\end{pmatrix}$$

로 만들 수 있다. 따라서 임의의 실대칭행렬은 이 꼴의 행렬과 합동이다. 이 때 이차형식은 이 basis에 대한 좌표 $$v=\sum a_ie_i$$로 적었을 때 

$$Q(v)=a_1^2+\cdots+a_p^2-a_{p+1}^2-\cdots-a_{p+q}^2$$

으로 표현된다. 

## 실베스터 관성법칙

[명제 2](#prop2)는 적절한 basis를 택하면 이차형식이 부호 붙은 제곱들의 합으로 환원됨을 보여주지만, 그 과정에서 나타난 $$p,q,r$$이 basis의 선택에 따라 달라질 수 있는지는 아직 분명하지 않다. 다음 정리는 이 세 수가 사실은 bilinear form 자체의 불변량임을 보여준다. 

<div class="proposition" markdown="1">

<ins id="thm3">**정리 3 (Sylvester 관성법칙)**</ins> $$\mathbb{R}$$-벡터공간 $$V$$ 위에 정의된 symmetric bilinear form $$\langle-,-\rangle$$에 대하여, [명제 2](#prop2)와 같은 basis에서 나타나는 $$\langle e_i,e_i\rangle$$의 값이 $$1$$인 것의 개수 $$p$$, $$-1$$인 것의 개수 $$q$$, 그리고 $$0$$인 것의 개수 $$r$$은 basis의 선택과 무관하게 결정된다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[명제 2](#prop2)의 basis를 $$\{e_1,\ldots, e_n\}$$이라 하고, $$p$$개의 $$+1$$, $$q$$개의 $$-1$$, $$r$$개의 $$0$$이 나타나도록 재배열하였다 하자. Gram matrix의 rank는 합동변환에 대해 불변이고 ($$P$$가 가역이면 $$\rank(P^tGP)=\rank G$$이므로) 이 basis에서 rank는 $$p+q$$이므로, $$p+q$$는 basis의 선택과 무관하다. 따라서 $$r=n-(p+q)$$ 또한 그러하다. 이제 $$p$$가 불변임을 보이면 $$q$$도 따라서 불변이다. 

$$p$$를 다음의 식

$$p=\max\{\dim U\mid U\leq V,\ Q(v)>0\text{ for all nonzero }v\in U\}$$

으로 특징지을 수 있음을 보인다. 이 우변이 basis와 무관함은 정의상 자명하므로, 이를 보이면 충분하다. 

우선 $$U_+=\span\{e_1,\ldots, e_p\}$$을 생각하면, 임의의 $$0\neq v=\sum_{i=1}^p a_ie_i\in U_+$$에 대하여 

$$Q(v)=\sum_{i=1}^p a_i^2>0$$

이므로 $$\dim U_+=p$$인 부분공간 위에서 $$Q$$가 양의 정부호이다. 따라서 위 최댓값은 $$p$$ 이상이다. 거꾸로 $$Q$$가 양의 정부호인 임의의 부분공간 $$U$$를 생각하고, $$U_-=\span\{e_{p+1},\ldots, e_n\}$$이라 하자. 임의의 $$v=\sum_{i=p+1}^n a_ie_i\in U_-$$에 대하여 

$$Q(v)=-\sum_{i=p+1}^{p+q}a_i^2\leq 0$$

이므로, 만일 $$0\neq v\in U\cap U_-$$가 존재한다면 $$Q(v)>0$$과 $$Q(v)\leq 0$$이 동시에 성립하여 모순이다. 따라서 $$U\cap U_-=\{0\}$$이고, [§벡터공간의 차원, ⁋예시 8](/ko/math/linear_algebra/dimension#ex8)에 의하여 

$$\dim U+\dim U_-=\dim(U+U_-)\leq n$$

이다. $$\dim U_-=n-p$$이므로 $$\dim U\leq p$$이다. 즉 최댓값은 $$p$$이고, 이로써 $$p$$가 basis와 무관함을 보였다.

</details>

이로써 다음 정의가 말이 된다.

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> $$\mathbb{R}$$-벡터공간 $$V$$ 위에 정의된 symmetric bilinear form $$\langle-,-\rangle$$에 대하여, [정리 3](#thm3)에서 결정되는 세 수 $$(p,q,r)$$을 $$\langle-,-\rangle$$의 *부호수<sub>signature</sub>*라 부른다. 

</div>

부호수에서 $$p+q$$는 Gram matrix의 rank이고, $$r$$은 $$\langle-,-\rangle$$이 퇴화하는 정도, 즉 모든 벡터와 직교하는 벡터들이 이루는 부분공간의 차원이다. 특히 $$\langle-,-\rangle$$이 non-degenerate인 것은 $$r=0$$인 것과 동치이다. 

관성법칙은 곧바로 실대칭행렬의 합동에 의한 완전한 분류를 준다.

<div class="proposition" markdown="1">

<ins id="cor5">**따름정리 5**</ins> 두 실대칭행렬이 서로 합동인 것은 이들이 정의하는 bilinear form의 부호수가 같은 것과 동치이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

두 행렬 $$G,G'$$이 합동이라 하면 이들은 같은 bilinear form을 서로 다른 basis로 적은 것이므로 부호수가 같다. 거꾸로 부호수가 $$(p,q,r)$$로 같다면, [명제 2](#prop2)에 의하여 $$G$$와 $$G'$$은 모두 $$1$$이 $$p$$개, $$-1$$이 $$q$$개, $$0$$이 $$r$$개인 같은 대각행렬과 합동이고, 합동은 동치관계이므로 $$G$$와 $$G'$$은 서로 합동이다. 

</details>

## 양의 정부호성

부호수가 $$(n,0,0)$$인 경우, 즉 $$Q$$가 영이 아닌 모든 벡터에서 양수인 경우는 특별히 중요하다. 

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> $$\mathbb{R}$$-벡터공간 $$V$$ 위에 정의된 symmetric bilinear form $$\langle-,-\rangle$$이 *양의 정부호<sub>positive definite</sub>*라는 것은 모든 $$0\neq v\in V$$에 대하여 $$\langle v,v\rangle>0$$인 것이다.

</div>

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> $$\mathbb{R}$$-벡터공간 $$V$$ 위에 정의된 symmetric bilinear form $$\langle-,-\rangle$$에 대하여, 다음은 모두 동치이다.

1. $$\langle-,-\rangle$$이 양의 정부호이다.
2. $$\langle-,-\rangle$$의 부호수가 $$(n,0,0)$$이다.
3. $$\langle-,-\rangle$$이 $$V$$ 위의 내적이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[명제 2](#prop2)의 basis $$\{e_1,\ldots, e_n\}$$에 대하여 $$v=\sum a_ie_i$$이면 $$Q(v)=\sum_i\langle e_i,e_i\rangle a_i^2$$이다. 만일 어떤 $$\langle e_i,e_i\rangle$$이 $$-1$$이거나 $$0$$이라면 $$v=e_i$$에 대하여 $$Q(e_i)\leq 0$$이므로 양의 정부호가 아니다. 거꾸로 모든 $$\langle e_i,e_i\rangle$$이 $$1$$이라면, 즉 부호수가 $$(n,0,0)$$이라면 임의의 $$0\neq v$$에 대하여 $$Q(v)=\sum a_i^2>0$$이다. 따라서 1번과 2번이 동치이다. 

한편 내적의 정의는 symmetric bilinear form이면서 모든 $$v$$에 대해 $$\langle v,v\rangle\geq 0$$이고 등호가 오직 $$v=0$$일 때만 성립하는 것이므로 ([§내적공간, ⁋정의 1](/ko/math/linear_algebra/inner_product_spaces#def1)) 이는 정확히 양의 정부호라는 조건이다. 따라서 1번과 3번이 동치이다. 

</details>

즉 내적이란 부호수가 $$(n,0,0)$$인 symmetric bilinear form에 다름 아니며, 관성법칙의 관점에서 내적공간은 가능한 부호수들 가운데 가장 특별한 한 점에 해당한다. 

<div class="remark" markdown="1">

<ins id="rmk8">**참고 8**</ins> [명제 2](#prop2)는 가역행렬에 의한 합동변환 $$G\mapsto P^tGP$$을 통해 대각형을 얻은 것이며, 이 때 대각성분의 절댓값에는 아무런 정보가 없다. 만일 $$P$$를 orthogonal matrix로 제한하면, 합동변환은 닮음변환 $$G\mapsto P^tGP=P^{-1}GP$$과 일치하므로 [§스펙트럼 정리](/ko/math/linear_algebra/spectral_theorem)에 의하여 $$G$$를 그 eigenvalue들로 이루어진 대각행렬로 만들 수 있다. 이렇게 얻어진 대각성분은 더 이상 $$1,-1,0$$이 아니라 $$G$$의 실제 eigenvalue들이며, 그 부호의 분포가 곧 부호수 $$(p,q,r)$$이 된다. 이를 *주축정리<sub>principal axis theorem</sub>*라 부른다. 관성법칙은 합동에 대한 불변량을, 주축정리는 닮음에 대한 불변량을 다룬다는 점에서 둘은 구별된다. 

</div>

---

**참고문헌**

**[Lee]** 이인석, *선형대수와 군*, 서울대학교 출판문화원, 2005.  
**[Goc]** M.S. Gockenbach, *Finite-dimensional linear algebra*, Discrete Mathematics and its applications, Taylor&Francis, 2011.

---
