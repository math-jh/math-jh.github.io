---
title: "Bruhat decomposition"
description: "Connected reductive algebraic group의 Bruhat decomposition을 정의하고, parabolic subgroup로 확장하여 partial flag variety의 cell decomposition을 구한다. Grassmannian의 구체적 대응과 Schubert cell·Schubert variety의 구조를 살펴본다."
excerpt: "Bruhat decomposition을 중심으로 한 homogeneous space의 cell decomposition, parabolic subgroup, 그리고 Grassmannian에서의 Schubert variety"

categories: [Math / Lie Theory]
permalink: /ko/math/lie_theory/bruhat_decomposition
sidebar: 
    nav: "Lie_theory-ko"

date: 2026-06-08
last_modified_at: 2026-06-08
weight: 5
published: false

---

일반적으로 기하학적 대상이 주어졌을 때 그 구조를 이해하기 위해 우리는 이 대상을 잘게 분해한다. 가령 위상적 공간 중 가장 만만한 것은 CW complex이며, 이를 cell structure로 분해하면 구체적인 계산을 할 수 있다. Lie group 또한 대수적 대상인 동시에 기하적 대상이므로, 이러한 방식을 시도해볼 수 있고, [§Borel subgroup, ⁋명제 16](/ko/math/lie_theory/borel_subgroup#prop16)에서 도입한 Bruhat decomposition이 바로 이러한 역할을 해 준다. 

우리는 이번 글에서 Bruhat decomposition을 조금 더 자세히 살펴본 후, Borel subgroup $$B$$를 포함하는 더 큰 parabolic subgroup $$P\supseteq B$$로 일반화하여 partial flag variety $$G/P$$의 cell decomposition을 살펴본다. 

## Coxeter group과 length function

Bruhat decomposition이 일반적인 cell decomposition과 다른 점은, cell들이 임의로 붙은 것이 아니라 $$G/B$$ 위 Borel subgroup $$B$$의 작용에서 orbit으로 자연스럽게 나온다는 것이다. 더 중요한 것은, 이 orbit들의 집합 $$B\backslash G/B$$가 정확히 Weyl group $$W$$ ([§근계, ⁋정의 17](/ko/math/lie_theory/root_systems#def17))로 색인된다는 점이다. 따라서 각 cell의 기하는 전적으로 $$W$$의 조합론으로 환원되며, 바로 여기서 root system이 다시 등장한다. 

이를 위해 우선 Coxeter group을 정의한다. 

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Group $$W$$와 그 generator들 $$S=\{s_1,\ldots,s_r\}$$의 쌍 $$(W,S)$$가 *Coxeter system<sub>콕세터 계</sub>*라는 것은 $$W$$가 다음의 presentation을 갖는 것이다.

$$W=\left\langle s_1,\ldots,s_r\;\middle|\;(s_is_j)^{m_{ij}}=e\right\rangle$$

여기서 $$m_{ii}=1$$이고, $$i\neq j$$에 대하여 $$m_{ij}=m_{ji}\in\{2,3,\ldots,\infty\}$$이다. 이 때 group $$W$$ 자체를 *Coxeter group<sub>콕세터 군</sub>*이라 부른다.

</div>

조건 $$m_{ii}=1$$은 각 generator가 $$s_i^2=e$$를 만족하는 involution임을 뜻하고, $$i\neq j$$에 대한 관계 $$(s_is_j)^{m_{ij}}=e$$는 *braid relation*이라 불린다. 가령 $$m_{ij}=2$$이면 $$s_is_j=s_js_i$$, 즉 두 생성원이 commute하며, $$m_{ij}=3$$이면 $$s_is_js_i=s_js_is_j$$가 된다. $$m_{ij}=\infty$$인 경우는 $$s_i$$와 $$s_j$$ 사이에 아무런 관계도 부과하지 않음을 의미한다. 

가장 작은 비자명한 경우는 생성원이 둘인 경우다. $$S=\{s_1,s_2\}$$이고 $$m_{12}=m$$이면 $$(W,S)$$는 정확히 order $$2m$$의 dihedral group ([\[대수적 구조\] §반군, 모노이드, 군, ⁋예시 16](/ko/math/algebraic_structures/groups#ex16))이며, 두 생성원은 정$$m$$각형의 인접한 두 대칭축에 대한 reflection으로, 그 곱 $$s_1s_2$$는 order $$m$$의 회전으로 실현된다. 일반적인 Coxeter group은 이러한 dihedral 조각들을 생성원을 공유하며 이어붙인 것으로 이해할 수 있다. 실제로 임의의 두 generator $$s_i,s_j$$가 만드는 부분군 $$\langle s_i,s_j\rangle$$는 언제나 위수 $$2m_{ij}$$의 dihedral group이고, [정의 1](#def1)의 presentation이 말하는 핵심은 이러한 pairwise relation 외에 셋 이상의 generator가 얽히는 새로운 relation이 없다는 것이다.

이 정수들 $$m_{ij}$$를 모은 대칭행렬이 Coxeter system의 모든 정보를 담으며, 유한 reflection group은 정확히 유한 Coxeter group으로 특징지어진다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> Weyl group $$W$$는 simple reflection들의 집합 $$S=\{s_1,\ldots,s_r\}$$에 의해 생성되며, $$(W,S)$$는 Coxeter system을 이룬다. 더욱이 각 $$m_{ij}$$ ($$i\neq j$$)는 $$2,3,4,6$$ 중 하나이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$W$$가 reflection들로 생성된다는 것은 [§근계, ⁋정의 17](/ko/math/lie_theory/root_systems#def17)의 정의이다. 두 simple reflection $$s_i,s_j$$의 곱 $$s_is_j$$는 $$\alpha_i$$와 $$\alpha_j$$가 생성하는 2차원 평면 위에서의 rotation이며, 그 rotation 각도는 두 simple root가 이루는 각의 두 배이다. [§근계](/ko/math/lie_theory/root_systems)에서 확인한 것과 같이 서로 다른 두 simple root가 이룰 수 있는 각은 $$90^\circ,120^\circ,135^\circ,150^\circ$$ 중 하나이므로, $$s_is_j$$의 위수 $$m_{ij}$$는 각각 $$2,3,4,6$$이 된다. 이들 braid relation만으로 $$W$$가 완전히 결정된다는 것이 가장 비자명한 부분으로, 이것이 바로 Coxeter의 정리에 해당하는 부분이다.

</details>

우리 경우에 이 정수 $$m_{ij}$$들은 [§Borel subgroup, ⁋정의 1](/ko/math/lie_theory/borel_subgroup#def1)의 Dynkin diagram에서 곧바로 읽힌다. 두 vertex가 연결되지 않았으면 $$m_{ij}=2$$, single edge면 $$3$$, double edge면 $$4$$, triple edge면 $$6$$이다. 예컨대 [§Borel subgroup, ⁋정의 8](/ko/math/lie_theory/borel_subgroup#def8)의 그림에서 type $$A_{n-1}$$의 Weyl group $$W=S_n$$에서 인접한 두 simple reflection은 $$m=3$$을 가지므로 익숙한 braid relation $$s_is_{i+1}s_i=s_{i+1}s_is_{i+1}$$을 만족한다.

Coxeter system $$(W,S)$$가 주어지면 각 원소를 생성원의 곱으로 표현하는 데 드는 "비용"을 잴 수 있다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> Coxeter system $$(W,S)$$의 원소 $$w$$에 대하여, $$w$$의 *length<sub>길이</sub>* $$\ell(w)$$는 $$w$$를 simple reflection들의 곱 $$w=s_{i_1}\cdots s_{i_k}$$로 나타낼 때 필요한 가장 작은 $$k$$이다. 길이가 $$\ell(w)$$인 표현을 $$w$$의 *reduced expression<sub>기약 표현</sub>*이라 한다.

</div>

정의에 의해 $$\ell(e)=0$$이고 $$\ell(s_i)=1$$이며, $$\ell(w^{-1})=\ell(w)$$이다. Length function의 의미는 root system을 통해 가장 투명하게 드러나는데, 그 출발점은 simple reflection이 positive root 전체에 미치는 영향이 극히 제한적이라는 사실이다.

[§근계, ⁋정의 9](/ko/math/lie_theory/root_systems#def9)의 reflection 공식에 의하면 simple reflection $$s_i$$는 $$\alpha_i$$를 $$-\alpha_i$$로 보낸다. 나머지 positive root $$\beta\in\Phi^+$$, $$\beta\neq\alpha_i$$에 대해서는, $$\beta$$를 simple root들의 positive linear combination으로 쓴다 생각하면 $$\alpha_i$$를 제외한 계수 중 하나가 양수인데, 해당 정의의 Cartan integer $$\langle\beta,\alpha_i\rangle$$를 사용하면 

$$s_i(\beta)=\beta-\langle\beta,\alpha_i\rangle\alpha_i$$

로 쓸 수 있으므로, $$s_i(\beta)$$에서 바꿔지는 계수는 오직 $$\alpha_i$$ 뿐이고, 따라서 위의 양수계수는 여전히 양수로 남아있기 때문이다. 즉, $$s_i$$가 작동할 때, positive root였다가 negative root로 바뀌는 것은 오직 $$\alpha_i$$ 하나 뿐이고, 따라서 임의의 Weyl group element $$w$$에는 simple reflection을 하나 곱할 때마다 $$w$$가 음근으로 보내는 양근의 개수는 정확히 $$1$$만큼 늘거나 줄어든다.

따라서, 이를 identity에서부터 reduced expression을 따라가며 따져보면 $$w$$에서 $$ws_i$$로 바뀔 때의 length의 변화량

$$\ell(ws_i)=\ell(w)+1$$

의 증감이 정확히 이를 반영해주는 것을 알 수 있다. 즉 임의의 $$w\in W$$에 대하여

$$\ell(w)=\lvert\Phi^+\cap w^{-1}\Phi^-\rvert$$

이 성립한다. 우변의 집합 $$\Phi^+\cap w^{-1}\Phi^-=\{\alpha\in\Phi^+\mid w\alpha\in\Phi^-\}$$를 $$w$$의 inversion 집합이라 부르며, 뒤에서 보겠지만 그 크기는 정확히 $$w$$에 대응하는 Bruhat cell의 차원과 일치한다.

<div class="example" markdown="1">

<ins id="ex4">**예시 4**</ins> 간략한 예시로 type $$A_{n-1}$$의 Weyl group의 경우를 보자. 이 경우 $$W=S_n$$이며 각각의 $$s_i$$는 $$(i\;i+1)$$들이다. 이 때, positive root들은 $$\Phi^+=\{e_i-e_j\mid i<j\}$$이고, 임의의 Weyl group element $$w\in W$$는 $$e_i-e_j$$를 $$e_{w(i)}-e_{w(j)}$$로 보낸다.

이제 이것이 negative가 되는 것은 $$w(i)>w(j)$$인 것과 동치이며, 따라서

$$\ell(w)=\lvert\{(i,j)\mid i<j,\ w(i)>w(j)\}\rvert=\operatorname{inv}(w)$$

는 $$w$$의 *inversion* 개수와 같다.

</div>

## Bruhat decomposition

이제 우리는 위에서 살펴본 결과들을 이용하여 Bruhat decomposition을 생각한다. 다음 정리는 [§Borel subgroup, ⁋명제 16](/ko/math/lie_theory/borel_subgroup#prop16)에서 이미 살펴본 결과로, 편의를 위해 재서술해둔다. 

<div class="proposition" markdown="1">

<ins id="thm5">**정리 5 (Bruhat decomposition)**</ins> Connected reductive algebraic group $$G$$, Borel subgroup $$B$$, maximal torus $$T\subset B$$, 그리고 Weyl group $$W=N_G(T)/T$$에 대하여, 다음의 disjoint union이 성립한다.

$$G=\bigsqcup_{w\in W}BwB$$

</div>

이 decomposition을 바라보는 가장 단순하고 직관적인 방법은 $$G$$ 위에 정의된 $$B\times B$$-action

$$(b_1,b_2)\cdot g=b_1gb_2^{-1}$$

을 생각하는 것이다. 이 action의 orbit이 바로 double coset $$BwB$$이며, 위의 정리는 이 orbit이 $$W$$로 index된다는 뜻이다. 

이것이 담고있는 기하학적 의미를 살펴보기 위해 $$G=\GL_n(\mathbb{C})$$에서의 예시를 살펴보자. 여기서 reference flag $$E_i=\operatorname{span}\{e_1,\ldots,e_i\}$$를 고정하면, 임의의 flag $$V_\bullet$$는 $$gB$$에 대응하는 $$V_i=\operatorname{span}\{ge_1,\ldots,ge_i\}$$인 것을 살펴보았다. ([§Borel subgroup, ⁋예시 13](/ko/math/lie_theory/borel_subgroup#ex13)) 일반적으로 reference flag $$E_\bullet$$과 $$V_i$$가 이루는 위치는 다음의 intersection

$$d_{ij}=\dim(V_i\cap E_j)$$

차원에 대한 정보로 나타난다. 그럼 $$G$$ 위의 $$B$$-action은 flag variety 위의 좌표를 upper triangular 행렬로 정리하는 것이므로, 같은 $$B$$-orbit 안의 두 flag는 이 교차 차원들을 공유하며 그 역도 성립한다. 그럼 이제 Bruhat decomposition이 말하는 바는, 임의의 flag $$V_\bullet$$의 교차 차원 $$d_{ij}$$가 정확히 하나의 $$w\in S_n$$에 대하여

$$d_{ij}=\dim(V_i\cap E_j)=\#\{k\leq i\mid w(k)\leq j\}$$

을 만족한다는 것이다. 즉, 이러한 방식으로 $$V_\bullet$$의 상대적인 위치가 $$W$$의 원소와 일대일로 대응되며, $$BwB$$는 상대적 위치가 $$w$$인 모든 $$g$$들의 모임이다. 이 때 각 조각 $$BwB$$를 *Bruhat cell*이라 부른다. 

이는 그 이름 그대로 open cell을 이룬다. 구체적으로, $$B$$의 unipotent radical을 $$U$$, opposite Borel subgroup $$B^-$$의 unipotent radical을 $$U^-$$라 하고, 각 $$w\in W$$에 대하여

$$U_w=U\cap wU^-w^{-1}$$

으로 정의하자. 그럼 $$U_w$$는 $$w^{-1}\gamma\in\Phi^-$$를 만족하는 positive root $$\gamma$$들의 root subgroup $$U_\gamma$$의 곱으로 주어진다.

$$U_w=\prod_{\substack{\gamma\in\Phi^+\\ w^{-1}\gamma\in\Phi^-}}U_\gamma$$

곱에 등장하는 root의 개수는 $$\ell(w)$$이므로, $$U_w$$는 affine space $$\mathbb{A}^{\ell(w)}$$와 isomorphic하다. 즉 $$U_w$$는 "$$w^{-1}$$이 음근으로 보내는 양근들"만 모은 unipotent subgroup이며, 그 차원이 곧 length이다 ($$\ell(w^{-1})=\ell(w)$$).

이하에서 $$BwB$$나 곱 $$uwb$$처럼 $$w\in W$$를 행렬로 직접 다룰 때는, $$N_G(T)$$ 안의 대표원 하나를 고른 것으로 본다. 서로 다른 대표원은 $$T\subset B$$만큼만 차이나므로 double coset $$BwB$$와 그 coset $$BwB/B$$는 대표원 선택과 무관하다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> 각 $$w\in W$$에 대하여, product map

$$U_w\times B\longrightarrow BwB,\qquad (u,b)\longmapsto uwb$$

은 variety의 isomorphism이다. 따라서 Bruhat cell은 $$BwB\cong\mathbb{A}^{\ell(w)}\times B$$이고, flag variety로 내리면

$$X_w^\circ:=BwB/B\cong\mathbb{A}^{\ell(w)}\subseteq G/B$$

가 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$B=U\rtimes T$$이고 $$U$$는 root subgroup들의 곱으로 분해된다. $$U$$를 $$U_w$$와 $$U_w'=U\cap wUw^{-1}$$의 곱으로 쓰면 $$U=U_wU_w'$$이고 $$U_w\cap U_w'=\{e\}$$이다. $$U_w'$$는 $$w^{-1}$$에 의해 positive root에서 positive root로 보내지는 root들에 해당하므로 $$w^{-1}U_w'w\subseteq U$$이고, 따라서

$$BwB=UwB=U_w(wU_w'w^{-1})wB=U_wwB$$

이다. 이제 $$u_1wb_1=u_2wb_2$$ ($$u_i\in U_w$$, $$b_i\in B$$)라 하면 $$w^{-1}u_2^{-1}u_1w=b_2b_1^{-1}\in B$$이다. 한편 $$u_2^{-1}u_1\in U_w$$이므로 $$w^{-1}u_2^{-1}u_1w\in U^-$$이고, 따라서 $$w^{-1}u_2^{-1}u_1w\in B\cap U^-=\{e\}$$이다. 이로부터 $$u_1=u_2$$, $$b_1=b_2$$이므로 map은 bijective이며, 실제로 variety의 isomorphism이다. 마지막으로 $$U_w$$는 $$\ell(w)$$개의 root subgroup의 곱이고 각 root subgroup은 $$\mathbb{G}_a$$와 isomorphic하므로 $$U_w\cong\mathbb{A}^{\ell(w)}$$이다.

</details>

이 명제의 진정한 의미는 각각의 $$B$$-orbit $$X_w^\circ=BwB/B$$들이 단순한 locally closed subset이 아니라 *affine space* $$\mathbb{A}^{\ell(w)}$$ 그 자체이며, 뿐만 아니라 이들이 $$G/B$$ 전체를 겹침 없이 덮는다는 데 있다.

$$G/B=\bigsqcup_{w\in W}X_w^\circ,\qquad X_w^\circ\cong\mathbb{A}^{\ell(w)}$$

각 cell의 closure가 더 낮은 차원의 cell들의 합집합이므로 ([§Borel subgroup, ⁋명제 16](/ko/math/lie_theory/borel_subgroup#prop16)) 이 분해는 $$G/B$$의 *affine paving*을 이루고, cell closure가 정의하는 class $$[X_w]$$들은 Chow ring $$A^\ast(G/B)$$ — 나아가 cohomology $$H^\ast(G/B)$$ — 의 basis를 정의한다. 차원이 가장 큰 cell은 longest element $$w_0$$에 대응하는 *big cell* $$X_{w_0}^\circ$$로, $$G/B$$에서 open dense이며 $$\dim X_{w_0}^\circ=\ell(w_0)=\lvert\Phi^+\rvert=\dim G/B$$이다. 반대로 가장 작은 cell은 한 점 $$X_e^\circ=\{eB\}$$로, $$B$$-fixed point이다. 이렇게 Bruhat decomposition은 flag variety의 기하를 $$(W,S,\ell)$$의 조합론으로 환원한다. 이를 위에서 살펴본 구체적인 예시 $$\GL_n$$에서 살펴보자. 

<div class="example" markdown="1">

<ins id="ex7">**예시 7**</ins> $$G=\GL_n(\mathbb{C})$$의 경우를 끝까지 따라가 보자. 여기서 $$B$$는 invertible upper triangular matrix, $$T$$는 invertible diagonal matrix들의 group이고, Weyl group은 $$W=N_G(T)/T\cong S_n$$으로, $$w\in S_n$$은 $$we_k=e_{w(k)}$$로 작용하는 permutation matrix와 동일하게 취급된다. 이 표기 아래 Bruhat decomposition $$\GL_n=\bigsqcup_{w\in S_n}BwB$$은 *Gauss elimination*의 좌표불변 버전이라 생각할 수 있다. 가역행렬 $$g$$에 왼쪽에서 upper unipotent matrix를 곱하는 것과 오른쪽에서 upper triangular matrix를 곱하는 것만으로 줄여 나가면, 마지막에 남는 것은 각 행과 열에 $$1$$이 정확히 하나씩 있는 permutation matrix $$w$$ 하나뿐이기 때문이다. 이 $$w$$가 유일하게 결정된다는 것이 곧 [정리 5](#thm5)의 disjointness이며, 그 $$w$$가 $$g$$의 Bruhat cell $$BwB$$를 가른다.

$$n=2$$의 경우를 명시적으로 보자. 그럼 $$G$$의 임의의 원소는 

$$g=\begin{pmatrix}a&b\\c&d\end{pmatrix}\in\GL_2$$

의 형태이며, 여기서 $$c=0$$이면 $$g$$는 이미 upper triangular이므로 $$g\in B=BeB$$, 즉 $$g$$는 identity에 해당하는 cell에 들어간다. 다른 원소를 살펴보자. 만일 $$c\neq 0$$이면

$$\begin{pmatrix}a&b\\c&d\end{pmatrix}=\begin{pmatrix}1&a/c\\0&1\end{pmatrix}\begin{pmatrix}0&1\\1&0\end{pmatrix}\begin{pmatrix}c&d\\0&\tfrac{bc-ad}{c}\end{pmatrix}\in BsB$$

이고, 따라서 $$\GL_2$$의 cell은 upper triangle matrix들과 그렇지 않은 부분으로 나뉘게 된다. 

이제 [명제 6](#prop6)을 따라 이들을 $$\GL_2(\mathbb{C})/B\cong \mathbb{P}^1$$으로 내리자. 위에서 보았듯 $$c=0$$에 해당하는 부분은 $$B$$ 그 자체이므로 이들은 한 점으로 떨어지며, 이는 명제의 $$\ell(w)=0$$에 해당하는 부분이다. 한편 $$c\neq 0$$인 부분에서는 위에서 살펴본 것과 같이 cell 

$$U_w\times B\rightarrow BwB;\qquad (u,b)\mapsto uwb$$

를 $$w=s$$에서 그대로 실현한 것으로, 자유롭게 움직이는 유일한 좌표 $$t=a/c$$가 isomorphism $$U_s\cong\mathbb{A}^1$$을 보여준다. 이를 flag variety $$\GL_2/B\cong\mathbb{P}^1$$로 내리면 $$\mathbb{P}^1$$의 cell 구조 그 자체가 나온다. 

$$\mathbb{C}^2$$의 flag은 $$0\subset L\subset\mathbb{C}^2$$ 꼴이라 가운데 line $$L$$ 하나로 정해지므로, $$\GL_2/B$$는 $$\mathbb{C}^2$$의 line들의 공간 $$\mathbb{P}^1$$ 그 자체이고, 이 동일시에서 $$gB$$는 그 line $$V_1=\operatorname{span}\{ge_1\}$$, 즉 $$g$$의 첫 열 $$\begin{pmatrix}a\\c\end{pmatrix}$$이 정하는 점 $$[a:c]\in\mathbb{P}^1$$로 보내진다. 그러면 앞의 두 행렬 cell이 $$\mathbb{P}^1$$의 어느 부분인지 그대로 읽힌다.

$$c=0$$인 cell $$BeB$$에서는 $$V_1=[a:0]=[1:0]=E_1$$, 곧 $$B$$가 고정하는 단 하나의 line이다. 따라서 이 cell 전체가 한 점 $$X_e^\circ=\{[1:0]\}$$로 내려가며, 이것이 $$\mathbb{P}^1$$의 closed point이자 차원 $$0$$의 cell이다 ($$\ell(e)=0$$). 반면 $$c\neq0$$인 cell $$BsB$$에서는 $$V_1=[a:c]=[t:1]$$ ($$t=a/c$$)가 $$E_1$$을 제외한 모든 line을 훑으므로, 이 cell은 그 보집합인 open dense한 big cell $$X_s^\circ=\{[t:1]\mid t\in\mathbb{C}\}\cong\mathbb{A}^1$$이 된다 ($$\ell(s)=1$$). 결국 $$\mathbb{P}^1=\{[1:0]\}\sqcup\mathbb{A}^1$$은 한 점(가장 작은 cell)과 그 보집합인 affine line(big cell)으로 갈라지고, Gauss elimination에서 $$c=0$$이냐 $$c\neq0$$이냐로 갈렸던 분기가 정확히 이 점과 직선의 분기다. 그 $$\mathbb{A}^1$$의 좌표 $$t$$ 역시 행렬 분해에서 자유롭게 움직이던 $$t=a/c$$ 그대로다.

일반적인 $$n$$에서 cell을 가르는 이산 불변량은 본문에서 본 flag의 상대적 위치다. $$gB$$에 대응하는 flag $$V_i=\operatorname{span}\{ge_1,\ldots,ge_i\}$$와 standard flag $$E_j=\operatorname{span}\{e_1,\ldots,e_j\}$$의 교차 차원 $$d_{ij}=\dim(V_i\cap E_j)$$를 모으면, 정리 5는 행렬 $$(d_{ij})$$가 cell의 완전한 불변량임을 말한다.

$$gB\in BwB/B\iff d_{ij}=\#\{k\leq i\mid w(k)\leq j\}\quad(\forall\,i,j)$$

Gauss elimination이 보존하는 양이 정확히 이 $$d_{ij}$$들이다. 이 cell의 차원은 [예시 4](#ex4)에서 본 $$\ell(w)=\operatorname{inv}(w)$$이고, 가장 큰 cell은 역순 permutation $$w_0$$에 대응하는 차원 $$\binom{n}{2}$$의 big cell이다.

이 때 차원은 두 층위를 구분해야 한다. group $$G$$ 안의 double coset $$BwB$$는 [명제 6](#prop6)의 $$BwB\cong\mathbb{A}^{\ell(w)}\times B$$에 의해 차원 $$\dim B+\ell(w)$$인 반면, flag variety로 내린 cell $$X_w^\circ=BwB/B$$는 $$\dim B$$가 빠진 차원 $$\ell(w)$$이다. 가령 $$\GL_2$$ ($$\dim B=3$$)에서 $$BeB=B$$와 $$BsB$$는 각각 $$3,4$$차원이지만 ($$BsB$$는 $$\GL_2$$에서 open dense), $$\mathbb{P}^1$$로 내리면 차원 $$0,1$$의 cell이 된다.

</div>

## Birkhoff decomposition

Borel subgroup $$B$$ 대신 그 opposite $$B^-$$를 사용하면 거울에 비친 듯한 또 하나의 분해가 얻어진다. 두 분해를 견주는 것은 단순한 대칭놀음이 아니라, 어느 쪽 cell이 "일반적<sub>generic</sub>"인지가 정반대로 뒤집힌다는 점에서 의미가 있다.

<div class="proposition" markdown="1">

<ins id="thm8">**정리 8 (Birkhoff decomposition)**</ins> $$B^-$$를 $$B$$에 대응하는 opposite Borel subgroup이라 하면 다음이 성립한다.

$$G=\bigsqcup_{w\in W}B^-wB^-$$

더 일반적으로, 서로 opposite인 두 Borel subgroup $$B^+$$, $$B^-$$에 대하여 다음의 *mixed* 분해가 성립한다.

$$G=\bigsqcup_{w\in W}B^+wB^-$$

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$B^-=w_0Bw_0^{-1}$$이고 $$w_0=w_0^{-1}$$이므로, 정리 5의 양변을 $$w_0$$로 conjugate하면

$$G=w_0Gw_0^{-1}=\bigsqcup_{w\in W}(w_0Bw_0^{-1})(w_0ww_0^{-1})(w_0Bw_0^{-1})=\bigsqcup_{w\in W}B^-(w_0ww_0)B^-$$

을 얻는다. $$w\mapsto w_0ww_0$$가 $$W$$의 automorphism이므로 첫 번째 분해가 성립한다. Mixed 분해는 $$B^+=B$$, $$B^-=w_0Bw_0^{-1}$$를 대입하여 $$BwB^-=Bww_0Bw_0^{-1}$$로 쓰고 $$w\mapsto ww_0$$로 재색인하면 정리 5로 환원된다.

</details>

첫 번째 분해 $$G=\bigsqcup B^-wB^-$$는 그저 opposite Borel에 대한 Bruhat decomposition이므로, standard Bruhat의 거울상이다. 흥미로운 것은 서로 다른 두 Borel을 섞은 mixed 분해 $$G=\bigsqcup B^-wB$$ 쪽이다. 여기서는 $$w=e$$에 해당하는 cell $$B^-\cdot B$$가 open dense, 즉 *generic*하다. Standard Bruhat에서는 generic cell이 longest element $$w_0$$에 놓였던 것과 정반대로, 두 opposite Borel을 섞으면 generic stratum이 항등원으로 옮겨가는 것이다.

이 현상은 $$GL_n$$에서 가장 손에 잡힌다. $$B^-$$를 lower triangular matrix들의 모임이라 하면, cell $$B^-\cdot B$$는 lower triangular와 upper triangular의 곱으로 쓰이는 행렬들, 즉 *LU decomposition* $$g=LU$$를 갖는 행렬들의 집합이다. 선형대수에서 잘 알려져 있듯 이는 모든 leading principal minor가 $$0$$이 아닌 행렬들과 정확히 일치하며, 그러한 행렬들은 $$GL_n$$ 안에서 open dense이다. 앞서 $$n=2$$의 계산을 다시 보면 $$B^-\cdot B$$의 원소는 $$(1,1)$$-성분이 $$0$$이 아닌 행렬들이고, 이는 행 교환 없이 Gauss elimination이 진행되는 generic한 경우에 해당한다. Birkhoff가 원래 다룬 것이 바로 이 분해로, 일반적인 행렬에 대해서는 중간에 permutation이 필요하다는 사실 — 즉 $$g=LwU$$ 꼴의 분해와 그 permutation $$w$$의 유일성 — 이 Birkhoff decomposition의 내용이고, 그 generic stratum $$w=e$$가 LU decomposable한 행렬들이다.

<div class="remark" markdown="1">

<ins id="rmk9">**참고 9**</ins> 한 Bruhat cell과 한 opposite cell의 교집합 $$BwB\cap B^-vB^-$$ ($$v\leq w$$)는 일반적으로 비어있지 않은 smooth locally closed subvariety가 되며, 이를 *Richardson variety*라 부른다. 두 opposite Borel에 대한 cell 구조를 동시에 보는 이 관점은 flag variety의 정밀한 stratification을 주며, [§Richardson Variety](/ko/math/lie_theory/richardson_variety)에서 자세히 다룬다.

</div>

## Parabolic subgroup과 generalized Bruhat decomposition

지금까지의 cell decomposition은 complete flag variety $$G/B$$에 대한 것이었다. 이를 $$B$$를 포함하는 더 큰 subgroup, 곧 *parabolic subgroup*으로 확장하면 Grassmannian을 비롯한 partial flag variety $$G/P$$의 cell decomposition을 얻는다. 직관적으로 $$P$$는 flag의 일부 단계만 기억하는 것에 대응하며, 그만큼 $$W$$의 색인도 부분군 $$W_I$$만큼 거칠어진다.

<div class="definition" markdown="1">

<ins id="def10">**정의 10**</ins> $$G$$의 closed subgroup $$P$$가 *parabolic subgroup*이라는 것은 quotient $$G/P$$가 projective variety가 되는 것이다. 동치로, $$P$$는 어떤 Borel subgroup을 포함하는 connected closed subgroup이다.

</div>

$$B$$를 포함하는 *standard* parabolic subgroup들은 simple root system $$\Delta$$의 부분집합 $$I\subseteq\Delta$$와 일대일 대응한다. $$I$$에 대응하는 parabolic subgroup은

$$P_I=BW_IB=\bigsqcup_{w\in W_I}BwB$$

으로 정의되며, 여기서 $$W_I=\langle s_i\mid\alpha_i\in I\rangle$$은 $$I$$에 속한 simple reflection들로 생성되는 $$W$$의 *parabolic subgroup*이다. $$I=\varnothing$$이면 $$P_I=B$$이고 $$I=\Delta$$이면 $$P_I=G$$이므로, standard parabolic들은 $$B$$와 $$G$$ 사이를 메우는 사다리를 이룬다.

<div class="proposition" markdown="1">

<ins id="prop11">**명제 11**</ins> $$P_I=BW_IB$$는 $$G$$의 connected closed subgroup이며, Levi decomposition $$P_I=L_I\ltimes U_I$$를 갖는다. 여기서 Levi factor $$L_I$$는 $$T$$와 $$I$$에 속한 root들의 root space로 생성되는 reductive group이고, unipotent radical $$U_I$$는 $$I$$에 속하지 않은 positive root들의 root space로 생성된다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$B=U\rtimes T$$이고 $$W_I\subseteq W$$이므로 $$P_I$$는 $$B$$와 $$W_I$$의 대표원소들로 생성되는 subgroup이다. $$W_I$$의 각 원소 $$w$$에 대해 $$BwB$$는 locally closed이고, 정리 5의 disjointness로부터 이들의 union $$P_I$$는 well-defined subgroup이자 closed subset이다. Root space 차원에서 보면 $$\mathfrak{p}_I$$는 $$\mathfrak{b}$$에 $$I$$가 생성하는 negative root들의 root space를 더한 것으로, 이를 reductive part $$\mathfrak{l}_I$$ (양·음 root가 짝지어진 부분)와 nilpotent part $$\mathfrak{u}_I$$ (나머지 positive root)로 가르면 위의 Levi decomposition을 얻는다. 따라서 $$P_I$$는 connected closed subgroup이다.

</details>

Parabolic subgroup $$P=P_I$$에 대한 $$G/P$$의 cell decomposition을 얻으려면 Weyl group $$W$$를 $$W_I$$로 quotient해야 한다. 이 때 각 coset을 대표하는 표준적 방법이 minimal length 원소를 고르는 것이다.

<div class="definition" markdown="1">

<ins id="def12">**정의 12**</ins> Parabolic subgroup $$W_I\subseteq W$$에 대하여, *minimal length coset representatives*의 모임 $$W^I$$는 다음과 같이 정의된다.

$$W^I=\{w\in W\mid\ell(ws_i)>\ell(w)\text{ for all }\alpha_i\in I\}$$

</div>

조건 $$\ell(ws_i)>\ell(w)$$는 $$w$$를 오른쪽에서 $$W_I$$의 생성원으로 곱해도 더 이상 길이를 줄일 수 없다는 뜻이며, 따라서 $$W^I$$는 각 left coset $$wW_I$$ 안에서 길이가 최소인 원소들을 모은 것이다.

<div class="proposition" markdown="1">

<ins id="prop13">**명제 13**</ins> 각 $$w\in W$$는 $$w=w^I w_I$$ ($$w^I\in W^I$$, $$w_I\in W_I$$)로 유일하게 분해되며, 이 때 $$\ell(w)=\ell(w^I)+\ell(w_I)$$이다. 특히 각 coset $$wW_I$$는 정확히 하나의 minimal length 원소를 가지므로, projection $$W^I\rightarrow W/W_I$$는 bijection이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$W_I$$는 유한군이므로 coset $$wW_I$$ 안에서 길이가 최소인 원소 $$w^I$$가 존재한다. 임의의 $$\alpha_i\in I$$에 대하여 $$w^Is_i$$ 역시 같은 coset에 속하므로 $$\ell(w^Is_i)\geq\ell(w^I)$$이고, Coxeter group에서 $$\ell(w^Is_i)=\ell(w^I)\pm1$$이므로 $$\ell(w^Is_i)=\ell(w^I)+1$$, 즉 $$w^I\in W^I$$이다. 분해의 유일성과 길이의 가산성 $$\ell(w)=\ell(w^I)+\ell(w_I)$$는 Coxeter group의 parabolic factorization 정리이다. (\[BB\] 참조) 이로부터 $$W^I$$의 각 원소가 서로 다른 coset을 대표하므로 $$W^I\rightarrow W/W_I$$는 bijection이다.

</details>

이제 minimal length 대표원소를 사용하여 $$G/P_I$$의 cell decomposition을 얻는다. 핵심은 projection $$G/B\rightarrow G/P_I$$ 아래에서 같은 $$W_I$$-coset에 속한 Bruhat cell들이 하나로 뭉치고, 각 coset에서 살아남는 대표원소가 바로 $$W^I$$의 원소라는 점이다.

<div class="proposition" markdown="1">

<ins id="thm14">**정리 14 (Generalized Bruhat decomposition)**</ins> $$P=P_I$$를 standard parabolic subgroup이라 하면 다음이 성립한다.

$$G=\bigsqcup_{w\in W^I}BwP$$

따라서 partial flag variety $$G/P$$는 affine cell들로 분해된다.

$$G/P=\bigsqcup_{w\in W^I}BwP/P,\qquad BwP/P\cong\mathbb{A}^{\ell(w)}$$

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

정리 5의 $$G=\bigsqcup_{w\in W}BwB$$와 $$P=\bigsqcup_{v\in W_I}BvB$$로부터 $$G=\bigcup_{w\in W}BwP$$이고, 명제 13의 분해 $$w=w^Iw_I$$에 의해 $$BwP=Bw^IP$$이므로 $$G=\bigcup_{w\in W^I}BwP$$이다. Disjointness를 보기 위해 $$w_1,w_2\in W^I$$에 대해 $$Bw_1P=Bw_2P$$라 하자. 그럼 $$w_1\in Bw_2P$$이고, $$P=\bigsqcup_{v\in W_I}BvB$$이므로 $$Bw_2P=\bigsqcup_{v\in W_I}Bw_2vB$$이다. (여기서 $$w_2\in W^I$$와 $$v\in W_I$$에 대해 $$\ell(w_2v)=\ell(w_2)+\ell(v)$$이므로 $$Bw_2BvB=Bw_2vB$$가 단일 cell로 합쳐진다.) 따라서 어떤 $$v\in W_I$$에 대해 $$w_1\in Bw_2vB$$가 되어, 정리 5의 disjointness로부터 $$w_1=w_2v$$이다. 즉 $$w_1$$과 $$w_2$$는 같은 coset $$w_2W_I$$에 속하고, 각 coset에 minimal length 원소가 유일하므로 $$w_1=w_2$$이다. 마지막으로 $$w\in W^I$$이면 $$\ell(w)=\ell(w^I)$$가 cell 차원을 주어 명제 6과 같은 논증으로 $$BwP/P\cong\mathbb{A}^{\ell(w)}$$를 얻는다.

</details>

각 cell $$BwP/P$$의 closure는 *Schubert variety*를 정의하며, 이는 마지막 절에서 구체적으로 다룬다. $$G/P$$ 역시 affine paving을 가지므로 명제 6에 이어지는 위상적 귀결 — 홀수 cohomology 소멸, Schubert class basis, 그리고 그 class들이 Chow ring의 basis까지 이룬다는 사실 — 이 그대로 성립한다.

## Grassmannian

Generalized Bruhat decomposition의 가장 대표적인 예시는 Grassmannian이다. 이 절에서는 $$G=GL_n(\mathbb{C})$$를 고정하고, $$B$$는 upper triangular matrix, $$T$$는 diagonal matrix로 두자. Weyl group은 $$W\cong S_n$$, simple reflection은 adjacent transposition $$s_i=(i\;\,i{+}1)$$ ($$1\leq i\leq n-1$$)이다.

<div class="definition" markdown="1">

<ins id="def15">**정의 15**</ins> $$1\leq k\leq n-1$$에 대하여, *Grassmannian* $$Gr_k(\mathbb{C}^n)$$은 $$\mathbb{C}^n$$의 $$k$$차원 부분공간들의 moduli space이다.

$$Gr_k(\mathbb{C}^n)=\{V\subseteq\mathbb{C}^n\mid\dim V=k\}$$

</div>

Grassmannian을 homogeneous space로 실현하기 위해, simple root system $$\Delta=\{\alpha_1,\ldots,\alpha_{n-1}\}$$에서 $$\alpha_k$$ 하나만 제외한 부분집합 $$I=\Delta\setminus\{\alpha_k\}$$를 택하고, 이에 대응하는 maximal parabolic subgroup을 $$P_k$$라 하자. $$P_k$$는 block upper triangular matrix들의 모임으로

$$P_k=\left\{\begin{pmatrix}A&C\\0&D\end{pmatrix}\in GL_n(\mathbb{C})\;\middle|\;A\in GL_k(\mathbb{C}),\;D\in GL_{n-k}(\mathbb{C})\right\}$$

이다. 이 subgroup은 standard $$k$$-plane $$E_k=\operatorname{span}\{e_1,\ldots,e_k\}$$를 고정하므로, $$GL_n(\mathbb{C})$$의 $$Gr_k(\mathbb{C}^n)$$ 위의 작용은 transitive하고 그 isotropy group이 정확히 $$P_k$$이다. 따라서

$$Gr_k(\mathbb{C}^n)\cong GL_n(\mathbb{C})/P_k$$

이다. 한편 $$V\mapsto\mathbb{C}^n/V$$ 또는 적절한 내적 하의 $$V\mapsto V^\perp$$에 의해 $$Gr_k(\mathbb{C}^n)$$과 $$Gr_{n-k}(\mathbb{C}^n)$$ 사이에 canonical isomorphism이 있으므로, 같은 $$P_k$$에 대해 $$Gr_{n-k}(\mathbb{C}^n)\cong GL_n(\mathbb{C})/P_k$$로도 볼 수 있다.

<div class="proposition" markdown="1">

<ins id="prop16">**명제 16**</ins> $$GL_n(\mathbb{C})/P_k\cong Gr_k(\mathbb{C}^n)$$인 경우, Weyl group $$W=S_n$$의 parabolic subgroup $$W_{P_k}$$는 $$S_k\times S_{n-k}$$과 isomorphic하며, minimal length coset representatives $$W^{P_k}$$는 다음과 같다.

$$W^{P_k}=\{w\in S_n\mid w(1)<\cdots<w(k),\ w(k+1)<\cdots<w(n)\}$$

이들은 *$$(k,n-k)$$-shuffle*이라 불리며 모두 $$\binom{n}{k}$$개이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$P_k$$는 simple reflection $$s_1,\ldots,s_{k-1}$$과 $$s_{k+1},\ldots,s_{n-1}$$을 포함하므로 $$W_{P_k}=\langle s_1,\ldots,s_{k-1},s_{k+1},\ldots,s_{n-1}\rangle$$은 처음 $$k$$개와 나머지 $$n-k$$개의 문자를 각각 내부적으로 치환하는 permutation들의 모임이고, 따라서 $$S_k\times S_{n-k}$$와 isomorphic하다. 예시 4에서 $$\ell(w)=\operatorname{inv}(w)$$임을 보았으므로, coset $$wW_{P_k}$$에서 inversion 수가 최소인 원소는 처음 $$k$$개의 값과 나머지 $$n-k$$개의 값을 각각 증가순으로 배열한 것이다. 즉 $$w(1)<\cdots<w(k)$$이고 $$w(k+1)<\cdots<w(n)$$이어야 한다. 이러한 $$w$$는 $$\{1,\ldots,n\}$$에서 앞쪽 $$k$$자리에 놓을 값을 고르는 것으로 결정되므로 $$\binom{n}{k}$$개이며, 이는 $$\lvert W/W_{P_k}\rvert$$과 일치한다.

</details>

<div class="example" markdown="1">

<ins id="ex17">**예시 17**</ins> $$n=4$$, $$k=2$$인 경우 $$W=S_4$$, $$W_{P_2}=S_2\times S_2$$이고, minimal length 대표원소는

$$W^{P_2}=\{1234,\,1324,\,1423,\,2314,\,2413,\,3412\}$$

의 여섯 개이다. 가령 $$w=1324$$는 $$w(1)=1<w(2)=3$$이고 $$w(3)=2<w(4)=4$$를 만족하는 shuffle이다. 각 대표원소의 길이는 inversion을 세어

$$\ell(1234)=0,\quad\ell(1324)=1,\quad\ell(1423)=\ell(2314)=2,\quad\ell(2413)=3,\quad\ell(3412)=4$$

이므로, $$Gr_2(\mathbb{C}^4)$$은 차원 $$0,1,2,2,3,4$$의 여섯 Schubert cell로 paving된다. 이는 $$\dim Gr_2(\mathbb{C}^4)=2\cdot 2=4$$와 정합적이며, cell의 총 개수는 $$\binom{4}{2}=6$$, 복소 차원별로는 $$0,1,2,3,4$$차에 각각 $$1,1,2,1,1$$개가 놓인다. 각 cell은 Young diagram(즉 $$2\times 2$$ 상자 안에 들어가는 partition)으로도 색인되며, $$\ell(w)$$가 그 partition의 상자 수에 해당한다.

</div>

## Schubert cell과 Schubert variety

이제 partial flag variety $$X=G/P$$ 위의 cell들과 그 closure를 이름 붙여 정리하자. $$B$$와 그 opposite Borel $$B^-$$를 고정하면 두 방향의 cell 구조를 동시에 얻는다.

<div class="definition" markdown="1">

<ins id="def18">**정의 18**</ins> $$w\in W^P$$에 대하여, *Schubert cell* $$X_w^\circ$$와 *opposite Schubert cell* $$X^w_\circ$$를 각각

$$X_w^\circ=BwP/P\subseteq G/P,\qquad X^w_\circ=B^-wP/P\subseteq G/P$$

로 정의하고, 그 closure

$$X_w=\overline{X_w^\circ},\qquad X^w=\overline{X^w_\circ}$$

를 각각 *Schubert variety*와 *opposite Schubert variety*라 한다.

</div>

정의에 의해 $$X_w^\circ\cong\mathbb{A}^{\ell(w)}$$이고 $$X^w_\circ\cong\mathbb{A}^{\dim(G/P)-\ell(w)}$$이다. 특히 $$X_{w_0^P}^\circ$$ ($$w_0^P$$는 $$W^P$$의 longest element)는 $$\ell(w_0^P)=\dim(G/P)$$인 open dense cell이고, $$X_e^\circ=\{eP\}$$는 $$B$$-fixed point이다. 대칭적으로 opposite 쪽에서는 $$X^e_\circ=B^-P/P$$가 open dense cell, $$X^{w_0^P}_\circ=\{w_0^PP\}$$가 $$B^-$$-fixed point가 된다. 즉 두 cell 구조는 서로 차원을 뒤집은 형태로 맞물린다.

Schubert variety들 사이의 포함관계는 Weyl group 위의 *Bruhat order*가 지배한다. Bruhat order $$\leq$$는 $$v$$의 어떤 reduced expression이 $$w$$의 어떤 reduced expression의 subword로 나타날 때 $$v\leq w$$로 정의되는 순서로, 기하적으로는 [§Borel subgroup, ⁋명제 16](/ko/math/lie_theory/borel_subgroup#prop16)에서 본 cell closure $$\overline{BwB}=\bigsqcup_{v\leq w}BvB$$를 통해 드러난다.

<div class="proposition" markdown="1">

<ins id="prop19">**명제 19**</ins> $$x,w\in W^P$$에 대하여 다음이 성립한다.

$$X_x\subseteq X_w\iff x\leq w\text{ in Bruhat order}$$

특히 $$X_w=\bigsqcup_{\substack{x\leq w\\ x\in W^P}}X_x^\circ$$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$X_w=\overline{BwP/P}$$이고 $$B$$는 connected solvable group이므로, $$B$$-orbit의 closure는 더 작은 차원의 $$B$$-orbit들의 union이다. Complete flag variety $$G/B$$에서 $$\overline{BwB/B}=\bigsqcup_{v\leq w}BvB/B$$가 성립함은 위에서 환기한 cell closure로부터 따라나오며, projection $$G/B\rightarrow G/P$$로 내리면 $$W_P$$-coset 내부의 차이가 무너져 $$x,w\in W^P$$에 대해 $$X_x^\circ\subseteq X_w$$가 정확히 $$x\leq w$$일 때 성립한다.

</details>

<div class="example" markdown="1">

<ins id="ex20">**예시 20**</ins> $$G/P=Gr_2(\mathbb{C}^4)$$의 경우, $$W^{P_2}$$ 위의 Bruhat order는 두 maximal chain

$$1234\leq 1324\leq 1423\leq 2413\leq 3412$$

$$1234\leq 1324\leq 2314\leq 2413\leq 3412$$

으로 그려진다. 즉 $$1324$$ 아래에는 $$1234$$만 있고, 길이가 같은 $$1423$$과 $$2314$$는 서로 비교 불가능하며 둘 다 $$1324$$ 위·$$2413$$ 아래에 놓인다. 이 Hasse diagram은 두 갈래로 갈라졌다 다시 만나는 마름모꼴로, $$Gr_2(\mathbb{C}^4)$$의 Schubert class들 사이의 포함관계를 그대로 보여준다. 가령 Schubert variety $$X_{2413}$$은 $$X_{1423}^\circ$$, $$X_{2314}^\circ$$, $$X_{1324}^\circ$$, $$X_{1234}^\circ$$를 모두 포함하는 차원 $$3$$의 subvariety이다.

</div>

Schubert variety $$X_w\subseteq G/P$$는 일반적으로 singular하며, 그 singular locus 역시 더 작은 Schubert variety들의 union으로 표현된다. 한편 cohomology class $$[X_w]\in H^\ast(G/P)$$들은 명제 6 이후 논의한 대로 $$H^\ast(G/P)$$의 additive basis를 이루며, 이로부터 classical *Schubert calculus*라 불리는 intersection theory가 전개된다. 특히 Grassmannian의 경우 Schubert variety는 Young diagram으로 색인되고, 그들의 intersection number는 Littlewood–Richardson coefficient로 주어진다.

---

**참고문헌**

**[BB]** A. Björner, F. Brenti, *Combinatorics of Coxeter groups*, Graduate Texts in Mathematics **231**, Springer, 2005.

**[Ful]** W. Fulton, *Young tableaux*, London Mathematical Society Student Texts **35**, Cambridge University Press, 1997.

**[Hum]** J. E. Humphreys, *Linear algebraic groups*, Graduate Texts in Mathematics **21**, Springer, 1975.

**[Man]** L. Manivel, *Symmetric functions, Schubert polynomials and degeneracy loci*, SMF/AMS Texts and Monographs **6**, 2001.

**[Spr]** T. A. Springer, *Linear algebraic groups*, Progress in Mathematics **9**, Birkhäuser, 1998.
