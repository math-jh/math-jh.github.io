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

로 쓸 수 있으므로, $$s_i(\beta)$$에서 바꿔지는 계수는 오직 $$\alpha_i$$ 뿐이고, 따라서 위의 양수계수는 여전히 양수로 남아있기 때문이다. 즉, $$s_i$$가 작동할 때, positive root였다가 negative root로 바뀌는 것은 오직 $$\alpha_i$$ 하나 뿐이고, 따라서 임의의 Weyl group element $$w$$에는 simple reflection을 하나 곱할 때마다 $$w$$가 negative root로 보내는 positive root의 개수는 정확히 $$1$$만큼 늘거나 줄어든다.

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

이는 그 이름 그대로 open cell을 이룬다. 구체적으로, $$B$$는 maximal torus $$T$$와 unipotent radical의 semidirect product $$B=U\rtimes T$$로 분해되며, 이 unipotent radical $$U$$는 positive root들의 subgroup의 곱 $$U=\prod_{\alpha\in\Phi^+}U_\alpha$$ (각 $$U_\alpha\cong\mathbb{G}_a$$)이다. opposite Borel subgroup $$B^-$$의 unipotent radical을 $$U^-$$라 할 때, 각 $$w\in W$$에 대하여

$$U_w=U\cap wU^-w^{-1}$$

으로 정의하자. 그럼 $$U_w$$는 $$w^{-1}\gamma\in\Phi^-$$를 만족하는 positive root $$\gamma$$들의 root subgroup $$U_\gamma$$의 곱으로 주어진다.

$$U_w=\prod_{\substack{\gamma\in\Phi^+\\ w^{-1}\gamma\in\Phi^-}}U_\gamma$$

곱에 등장하는 root의 개수는 $$\ell(w)$$이므로, $$U_w$$는 affine space $$\mathbb{A}^{\ell(w)}$$와 isomorphic하다. 즉 $$U_w$$는 "$$w^{-1}$$이 negative root로 보내는 positive root들"만 모은 unipotent subgroup이며, 그 차원이 곧 length이다 ($$\ell(w^{-1})=\ell(w)$$).

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

각 cell의 closure가 더 낮은 차원의 cell들의 합집합이므로 ([§Borel subgroup, ⁋명제 16](/ko/math/lie_theory/borel_subgroup#prop16)) 이 분해는 $$G/B$$의 *affine paving*을 이루고, cell closure가 정의하는 class $$[X_w]$$들은 Chow ring $$A^\ast(G/B)$$(나아가 cohomology $$H^\ast(G/B)$$)의 basis를 정의한다. 차원이 가장 큰 cell은 longest element $$w_0$$에 대응하는 *big cell* $$X_{w_0}^\circ$$로, $$G/B$$에서 open dense이며 $$\dim X_{w_0}^\circ=\ell(w_0)=\lvert\Phi^+\rvert=\dim G/B$$이다. 반대로 가장 작은 cell은 한 점 $$X_e^\circ=\{eB\}$$로, $$B$$-fixed point이다. 이렇게 Bruhat decomposition은 flag variety의 기하를 $$(W,S,\ell)$$의 조합론으로 환원한다. 이를 위에서 살펴본 구체적인 예시 $$\GL_n$$에서 살펴보자. 

<div class="example" markdown="1">

<ins id="ex7">**예시 7**</ins> $$G=\GL_n(\mathbb{C})$$의 경우를 끝까지 따라가 보자. 여기서 $$B$$는 invertible upper triangular matrix, $$T$$는 invertible diagonal matrix들의 group이고, Weyl group은 $$W=N_G(T)/T\cong S_n$$으로, $$w\in S_n$$은 $$we_k=e_{w(k)}$$로 작용하는 permutation matrix와 동일하게 취급된다. 이 표기 아래 Bruhat decomposition $$\GL_n=\bigsqcup_{w\in S_n}BwB$$은 *Gauss elimination*의 좌표불변 버전이라 생각할 수 있다. 가역행렬 $$g$$에 왼쪽에서 upper unipotent matrix를 곱하는 것과 오른쪽에서 upper triangular matrix를 곱하는 것만으로 줄여 나가면, 마지막에 남는 것은 각 행과 열에 $$1$$이 정확히 하나씩 있는 permutation matrix $$w$$ 하나뿐이기 때문이다. 이 $$w$$가 유일하게 결정된다는 것이 곧 [정리 5](#thm5)의 disjointness이며, 그 $$w$$가 $$g$$의 Bruhat cell $$BwB$$를 가른다.

$$n=2$$의 경우를 명시적으로 보자. 그럼 $$G$$의 임의의 원소는 

$$g=\begin{pmatrix}a&b\\c&d\end{pmatrix}\in\GL_2(\mathbb{C})$$

의 형태이며, 여기서 $$c=0$$이면 $$g$$는 이미 upper triangular이므로 $$g\in B=BeB$$, 즉 $$g$$는 identity에 해당하는 cell에 들어간다. 다른 원소를 살펴보자. 만일 $$c\neq 0$$이면

$$\begin{pmatrix}a&b\\c&d\end{pmatrix}=\begin{pmatrix}1&a/c\\0&1\end{pmatrix}\begin{pmatrix}0&1\\1&0\end{pmatrix}\begin{pmatrix}c&d\\0&\tfrac{bc-ad}{c}\end{pmatrix}\in BsB$$

이고, 따라서 $$\GL_2(\mathbb{C})$$의 cell은 upper triangle matrix들과 그렇지 않은 부분으로 나뉘게 된다. 

이제 [명제 6](#prop6)을 따라 이들을 $$\GL_2(\mathbb{C})/B\cong \mathbb{P}^1$$으로 내리자. 위에서 보았듯 $$c=0$$에 해당하는 부분은 $$B$$ 그 자체이므로 이들은 한 점으로 떨어지며, 이는 명제의 $$\ell(w)=0$$에 해당하는 부분이다. 한편 $$c\neq 0$$인 부분에서는 위에서 살펴본 것과 같이 하나의 좌표 $$a/c$$로 매개되는 $$\mathbb{P}^1$$의 점 $$[a:c]\in \mathbb{P}^1$$이 나온다. 즉, $$c=0$$에 해당하는 flag variety의 점은 $$[1:0]$$이며, 나머지는 $$\mathbb{A}^1$$의 형태로 여기에 붙어있는 것이다. 

</div>

위의 $$\GL_n(\mathbb{C})$$의 Bruhat decomposition에서 우리는 Borel subalgebra $$B$$가 upper triangular matrix라는 것을 활용하여 선형대수학의 언어로 살펴볼 수 있었다. 한편 opposite Bruhat cell은 lower triangular matrix들의 모임이므로, 이들을 활용해도 비슷한 분해를 얻어낼 수 있으며 뿐만 아니라 다음과 같이 mixed decomposition을 생각할 수도 있다.  

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

이는 $$\GL_n(\mathbb{C})$$에서는 그 의미가 명확한데, identity cell $$B^-B$$는 lower triangular matrix와 upper triangular matrix의 곱으로 나타나는 행렬들, 곧 *LU decomposition*을 갖는 행렬들의 모임이다. 선형대수에서 잘 알려져 있듯 이는 모든 leading principal minor가 $$0$$이 아닌 행렬들과 정확히 일치하며, 그러한 행렬들은 $$\GL_n$$ 안에서 open dense이다. 

앞서 [예시 7](#ex7)의 $$n=2$$ 상황을 생각하면, $$2\times2$$ 행렬의 leading principal minor는 첫 행 $$g_{11}$$, 그리고 전체 determinant $$\det g$$ 둘이다. 그런데 $$\GL_2(\mathbb{C})$$에서는 $$\det g\neq0$$이 자동이므로 LU 조건은 $$g_{11}\neq0$$ 하나로 줄어들게 되므로, $$B^-B$$의 원소는 정확히 $$(1,1)$$-성분이 $$0$$이 아닌 행렬들이며 이는 정확히 첫 pivot이 살아 있어 행 교환 없이 Gauss elimination이 진행되는 성분들이다. 이와 같이, 일반적으로 leading principal minor들은 Gauss elimination의 pivot에 대응하여, 어느 단계에서 minor가 $$0$$이 되면 그 자리의 pivot이 사라져 행 교환이 불가피해진다. 이 행 교환의 패턴을 기록하는 것이 permutation $$w$$이며, Birkhoff가 보인 것은 임의의 $$g$$가

$$g=LwU\qquad(L\in B^-,\ U\in B,\ w\in W)$$

꼴로 쓰이고 그 $$w$$가 유일하게 결정된다는 사실이다. 이것이 곧 pair $$(B^-,B)$$에 대한 Bruhat decomposition $$G=\bigsqcup_w B^-wB$$이며, $$w$$는 $$g$$가 LU 분해에서 얼마나 벗어났는지를 잰다.

기하적으로 Bruhat decomposition은 reference flag의 크기를 키워가며 해당하는 incidence condition을 보여주는 것이었다. 그럼 위의 mixed cell의 경우, reference flag가 전체공간으로부터 떨어져 내려오는 방향(opposite Bruhat cell)까지 고려하며 incidence condition을 부여한 것이다. Flag variety 안에서 intersection theory를 하기 위해서는 Schubert variety들을 생각할 때 general position에 있는 reference flag들을 택해야 하므로 이 분해가 본격적으로 유용하게 사용된다. 

## Parabolic subgroup과 generalized Bruhat decomposition

지금까지의 cell decomposition은 complete flag variety $$G/B$$에 대한 것이었다. 이를 $$B$$를 포함하는 더 큰 subgroup, 곧 *parabolic subgroup*으로 확장하면 Grassmannian을 비롯한 partial flag variety $$G/P$$의 cell decomposition을 얻는다. 직관적으로 $$P$$는 flag의 일부 단계만 기억하는 것에 대응하며, 그만큼 $$W$$의 index도 subgroup $$W_I$$만큼 거칠어진다.

<div class="definition" markdown="1">

<ins id="def9">**정의 9**</ins> $$G$$의 closed subgroup $$P$$가 *parabolic subgroup*이라는 것은 quotient $$G/P$$가 projective variety가 되는 것이다. 동치로, $$P$$는 어떤 Borel subgroup을 포함하는 connected closed subgroup이다.

</div>

$$B$$를 포함하는 *standard* parabolic subgroup들은 simple root system $$\Delta$$의 부분집합 $$I\subseteq\Delta$$와 일대일 대응된다. 이 때, $$I$$에 대응하는 parabolic subgroup은

$$P_I=BW_IB=\bigsqcup_{w\in W_I}BwB$$

으로 정의되며, 여기서 $$W_I=\langle s_i\mid\alpha_i\in I\rangle$$은 $$I$$에 속한 simple reflection들로 생성되는 $$W$$의 parabolic subgroup이다. 두 극단은 $$I=\emptyset$$이면 $$P_I=B$$이고 $$I=\Delta$$이면 $$P_I=G$$으로, 그 사이의 standard parabolic들은 complete flag variety와 0-step variety 사이에 있는 flag variety들을 정의하게 된다. 

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10**</ins> $$P_I=BW_IB$$는 $$G$$의 connected closed subgroup이며, Levi decomposition $$P_I=L_I\ltimes U_I$$를 갖는다. 여기서 Levi factor $$L_I$$는 $$T$$와 $$I$$에 속한 root들의 root space로 생성되는 reductive group이고, unipotent radical $$U_I$$는 $$I$$에 속하지 않은 positive root들의 root space로 생성된다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$B=U\rtimes T$$이고 $$W_I\subseteq W$$이므로 $$P_I$$는 $$B$$와 $$W_I$$의 대표원소들로 생성되는 subgroup이다. $$W_I$$의 각 원소 $$w$$에 대해 $$BwB$$는 locally closed이고, 정리 5의 disjointness로부터 이들의 union $$P_I$$는 well-defined subgroup이자 closed subset이다. Root space 차원에서 보면 $$\mathfrak{p}_I$$는 $$\mathfrak{b}$$에 $$I$$가 생성하는 negative root들의 root space를 더한 것으로, 이를 reductive part $$\mathfrak{l}_I$$ (양·음 root가 짝지어진 부분)와 nilpotent part $$\mathfrak{u}_I$$ (나머지 positive root)로 가르면 위의 Levi decomposition을 얻는다. 따라서 $$P_I$$는 connected closed subgroup이다.

</details>

[명제 10](#prop10)의 Levi decomposition은 Borel subgroup의 분해 $$B=U\rtimes T$$를 한 단계 키운 것으로 보면 자연스럽다. 즉, $$B$$가 torus $$T$$와 위쪽 unipotent $$U$$의 두 정보로 구성되었듯, $$P_I$$는 더 큰 reductive part $$L_I$$와 그 위의 unipotent $$U_I$$의 semidirect product이다. $$I$$에 속한 root들은 positive root와 negative root가 짝을 이뤄 살아남아 ($$T$$를 maximal torus로 갖는) reductive group $$L_I$$를 이루고, $$I$$ 밖의 positive root들은 짝이 없어 nilpotent radical $$U_I$$를 이룬다. 특히 $$L_I$$의 Weyl group은 정확히 $$W_I$$로, 바로 아래에서 $$W$$를 quotient하게 될 그 부분군이다.

$$G=\GL_n(\mathbb{C})$$에서는 이 분해가 block 행렬로 곧장 드러난다. $$I$$에서 빠진 simple root $$\alpha_k$$마다 $$k$$와 $$k+1$$ 사이가 끊겨 $$\{1,\ldots,n\}$$이 토막으로 나뉘고, $$P_I$$는 그 토막들을 대각 block으로 갖는 block upper triangular matrix들의 모임이다. 이 때 대각 block들이 reductive Levi $$L_I\cong\GL_{k_1}\times\cdots\times\GL_{k_r}$$를, 대각 위쪽 block들이 unipotent radical $$U_I$$를 이룬다. 이제 parabolic subgroup $$P=P_I$$에 대한 $$G/P$$의 cell decomposition을 얻으려면 Weyl group $$W$$를 $$W_I$$로 quotient해야 한다. 이 때 각 coset을 대표하는 표준적인 방법은 minimal length 원소를 고르는 것이다.

<div class="definition" markdown="1">

<ins id="def11">**정의 11**</ins> Parabolic subgroup $$W_I\subseteq W$$에 대하여, *minimal length coset representatives*의 모임 $$W^I$$는 다음과 같이 정의된다.

$$W^I=\{w\in W\mid\ell(ws_i)>\ell(w)\text{ for all }\alpha_i\in I\}$$

</div>

조건 $$\ell(ws_i)>\ell(w)$$는 $$w$$를 오른쪽에서 $$W_I$$의 생성원으로 곱해도 더 이상 길이를 줄일 수 없다는 뜻이며, 따라서 $$W^I$$는 각 left coset $$wW_I$$ 안에서 길이가 최소인 원소들을 모은 것이다. 앞서 Weyl group element의 length가 Bruhat cell의 차원을 주듯, 이들은 곧 partial flag variety를 분해했을 때 각 cell의 차원이 될 것이다. 이를 위해서는 다음의 다리가 필요하다. 

<div class="proposition" markdown="1">

<ins id="prop12">**명제 12**</ins> 각 $$w\in W$$는 $$w=w^I w_I$$ ($$w^I\in W^I$$, $$w_I\in W_I$$)로 유일하게 분해되며, 이 때 $$\ell(w)=\ell(w^I)+\ell(w_I)$$이다. 특히 각 coset $$wW_I$$는 정확히 하나의 minimal length 원소를 가지므로, projection $$W^I\rightarrow W/W_I$$는 bijection이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$W_I$$는 유한군이므로 coset $$wW_I$$ 안에서 길이가 최소인 원소 $$w^I$$가 존재한다. 임의의 $$\alpha_i\in I$$에 대하여 $$w^Is_i$$ 역시 같은 coset에 속하므로 $$\ell(w^Is_i)\geq\ell(w^I)$$이고, Coxeter group에서 $$\ell(w^Is_i)=\ell(w^I)\pm1$$이므로 $$\ell(w^Is_i)=\ell(w^I)+1$$, 즉 $$w^I\in W^I$$이다. 분해의 유일성과 길이의 가산성 $$\ell(w)=\ell(w^I)+\ell(w_I)$$는 Coxeter group의 parabolic factorization 정리이다. (\[BB\] 참조) 이로부터 $$W^I$$의 각 원소가 서로 다른 coset을 대표하므로 $$W^I\rightarrow W/W_I$$는 bijection이다.

</details>

이제 minimal length 대표원소를 사용하여 $$G/P_I$$의 cell decomposition을 얻는다. 핵심은 projection $$G/B\rightarrow G/P_I$$ 아래에서 같은 $$W_I$$-coset에 속한 Bruhat cell들이 하나로 뭉치고, 각 coset에서 살아남는 대표원소가 바로 $$W^I$$의 원소라는 점이다.

<div class="proposition" markdown="1">

<ins id="thm13">**정리 13 (Generalized Bruhat decomposition)**</ins> $$P=P_I$$를 standard parabolic subgroup이라 하면 다음이 성립한다.

$$G=\bigsqcup_{w\in W^I}BwP$$

따라서 partial flag variety $$G/P$$는 affine cell들로 분해된다.

$$G/P=\bigsqcup_{w\in W^I}BwP/P,\qquad BwP/P\cong\mathbb{A}^{\ell(w)}$$

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

정리 5의 $$G=\bigsqcup_{w\in W}BwB$$와 $$P=\bigsqcup_{v\in W_I}BvB$$로부터 $$G=\bigcup_{w\in W}BwP$$이고, 명제 12의 분해 $$w=w^Iw_I$$에 의해 $$BwP=Bw^IP$$이므로 $$G=\bigcup_{w\in W^I}BwP$$이다. Disjointness를 보기 위해 $$w_1,w_2\in W^I$$에 대해 $$Bw_1P=Bw_2P$$라 하자. 그럼 $$w_1\in Bw_2P$$이고, $$P=\bigsqcup_{v\in W_I}BvB$$이므로 $$Bw_2P=\bigsqcup_{v\in W_I}Bw_2vB$$이다. (여기서 $$w_2\in W^I$$와 $$v\in W_I$$에 대해 $$\ell(w_2v)=\ell(w_2)+\ell(v)$$이므로 $$Bw_2BvB=Bw_2vB$$가 단일 cell로 합쳐진다.) 따라서 어떤 $$v\in W_I$$에 대해 $$w_1\in Bw_2vB$$가 되어, 정리 5의 disjointness로부터 $$w_1=w_2v$$이다. 즉 $$w_1$$과 $$w_2$$는 같은 coset $$w_2W_I$$에 속하고, 각 coset에 minimal length 원소가 유일하므로 $$w_1=w_2$$이다. 마지막으로 $$w\in W^I$$이면 $$\ell(w)=\ell(w^I)$$가 cell 차원을 주어 명제 6과 같은 논증으로 $$BwP/P\cong\mathbb{A}^{\ell(w)}$$를 얻는다.

</details>

## Grassmannian

Generalized Bruhat decomposition의 가장 대표적인 예시는 Grassmannian $$\Gr_k(\mathbb{C}^n)$$이다. ([\[대수다양체\] §그라스만 다양체, ⁋정의 1](/ko/math/algebraic_varieties/grassmannians#def1)) 이는 그 정의에 의하여 1-step partial flag variety로 생각할 수 있다. 이를 위해 simple root system $$\Delta=\{\alpha_1,\ldots,\alpha_{n-1}\}$$에서 $$\alpha_k$$ 하나만 제외한 부분집합 $$I=\Delta\setminus\{\alpha_k\}$$를 택하고, 이에 대응하는 maximal parabolic subgroup을 $$P_k$$라 하자. $$P_k$$는 block upper triangular matrix들의 모임으로

$$P_k=\left\{\begin{pmatrix}A&C\\0&D\end{pmatrix}\in \GL_n(\mathbb{C})\;\middle|\;A\in \GL_k(\mathbb{C}),\;D\in \GL_{n-k}(\mathbb{C})\right\}$$

이다. 이 subgroup은 standard $$k$$-plane $$E_k=\operatorname{span}\{e_1,\ldots,e_k\}$$를 고정하므로, $$\GL_n(\mathbb{C})$$의 $$\Gr_k(\mathbb{C}^n)$$ 위의 작용은 transitive하고 그 isotropy group이 정확히 $$P_k$$이다. 따라서

$$\Gr_k(\mathbb{C}^n)\cong \GL_n(\mathbb{C})/P_k$$

이다. 한편 $$V\mapsto\mathbb{C}^n/V$$ 또는 적절한 내적 하의 $$V\mapsto V^\perp$$에 의해 $$\Gr_k(\mathbb{C}^n)$$과 $$\Gr_{n-k}(\mathbb{C}^n)$$ 사이에 canonical isomorphism이 있으므로, 같은 $$P_k$$에 대해 $$\Gr_{n-k}(\mathbb{C}^n)\cong \GL_n(\mathbb{C})/P_k$$로도 볼 수 있다.

<div class="proposition" markdown="1">

<ins id="prop14">**명제 14**</ins> $$\GL_n(\mathbb{C})/P_k\cong \Gr_k(\mathbb{C}^n)$$인 경우, Weyl group $$W=S_n$$의 parabolic subgroup $$W_{P_k}$$는 $$S_k\times S_{n-k}$$과 isomorphic하며, minimal length coset representatives $$W^{P_k}$$는 다음과 같다.

$$W^{P_k}=\{w\in S_n\mid w(1)<\cdots<w(k),\ w(k+1)<\cdots<w(n)\}$$

이들은 *$$(k,n-k)$$-shuffle*이라 불리며 모두 $$\binom{n}{k}$$개이다.

</div>

이는 결국 Grassmannian이 1-step partial flag variety이므로, 전체 공간 $$\GL_n(\mathbb{C})$$와 그 위에 작용하는 $$S_n$$ 전체 가운데 하나가 <em-ko>끊겨있는</em-ko> $$S_k\times S_{n-k}$$는 같은 것으로 생각할 수 있다는 것이다. 

Grassmannian은 구체적인 예시 중 가장 단순하고도 강력한 예시이므로 이 경우의 표기법을 정리해두자. 우선, 임의의 $$w\in S_n$$의 원소들을

$$w=w(1)w(2)\ldots w(n)$$

과 같이 쓰자. 가령 $$S_4$$의 원소 $$2413$$은 

$$w(1)=2, \quad w(2)=4, \quad w(3)=1,\quad w(4)=3$$

을 만족하는 원소이다. 그럼 우리는 이 원소가 정확히 $$(2,2)$$-shuffle임을 확인할 수 있으며, 예를 들어 $$1342$$는 $$(3,1)$$-shuffle이다. 즉, 이 표기법 상에서 블록들은 숫자가 떨어지는 자릿수에서 새 블록이 시작된다는 규칙을 통해 구분된다. 

한편 우리는 근본적으로 Grassmannian (혹은 더 일반적으로 partial flag variety)가 reference flag에 대한 incidence condition으로 나온다는 것을 기억한다. Flag variety $$\Fl(d_1, d_2, \ldots, d_m; n)$$을 생각하자. 이 variety의 원소는 다음의 flag

$$0\subset V_1\subset \cdots \subset V_m\subset \mathbb{C}^n,\qquad \dim V_k=d_k$$

들로 구성되는 것이며, 이 flag의 위치는 reference flag와의 교차 차원 $$\dim(V_i\cap E_j)$$가 모두 결정하며, 이 정보를 공유하는 대상들이 바로 Bruhat cell이었다. 

이 두 정보를 엮기 위해, 위의 reference flag와의 jump 데이터를 길이 $$n$$의 word $$u_1\cdots u_n$$로 생각하자. 이 때, $$u_j$$는 방향 $$e_j$$가 flag에 처음 들어오는 step의 번호이며, 즉 $$j$$를 고정한 상태로

$$\dim (V_1\cap E_j)\leq \dim (V_2\cap E_j)\leq\cdots$$

을 봤을 때 차원이 뛰는 곳을 의미하며, 만일 최종적으로 $$V_m$$에도 들어가지 않는 방향이 있다면 번호 $$m+1$$을 부여한다. 가령 Grassmannian $$\Gr(2,4)$$의 경우, $$V=\span\{e_1, e_2+e_3\}$$에 대해서는 $$E_j=\span\{e_1,\ldots,e_j\}$$와의 교차 차원이

$$\dim(V\cap E_j)=0,\,1,\,1,\,2,\,2\qquad(j=0,1,2,3,4)$$

이다. 차원이 뛰는 자리는 $$j=1$$ ($$e_1$$이 들어옴)과 $$j=3$$ ($$e_2+e_3$$ 방향이 들어옴)이고 $$j=2,4$$에서는 뛰지 않으므로, 들어오는 자리에 $$1$$, 그렇지 않은 자리에 ($$m=1$$이라) $$m+1=2$$를 주면

$$u=1\,2\,1\,2$$

이다. 관례대로 $$2$$를 $$0$$으로 적으면 $$0/1$$ word $$1010$$이고, 이는 pivot column $$\{1,3\}$$, 곧 $$(2,2)$$-shuffle $$w=1324$$에 대응한다 ($$\ell(w)=1$$). 그 cell은 아래 예시의 둘째 행렬 $$\begin{pmatrix}1&0&0&0\\0&\ast&1&0\end{pmatrix}$$ ($$\ast=1$$)이다. 


 하나로 적으면 깔끔하다. column $$j$$의 방향 $$e_j$$가 flag에 처음 들어오는 step의 번호를 $$u_j$$로 두는 것이다. 곧 $$u_j=c$$는 $$\dim(V_{a_c}\cap E_j)$$는 뛰지만 그 앞 step $$V_{a_{c-1}}$$까지는 안 뛴다는 뜻이고, $$V_{a_m}$$에도 끝내 안 들어오는 자리는 $$u_j=m+1$$로 둔다. 그러면 글자 $$c$$의 개수가 정확히 step 크기 $$a_c-a_{c-1}$$ ($$a_0=0$$, $$a_{m+1}=n$$)이 되고, 이런 word가 minimal coset representative $$W^P$$와 일대일로 대응한다. 거꾸로 word에서 글자 $$c$$가 놓인 자리를 증가순으로 읽으면 $$w$$의 $$c$$번째 블록 $$w(a_{c-1}+1)<\cdots<w(a_c)$$가 복원된다. 가령 $$2$$-step flag $$Fl(a,b;n)$$이면 세 글자 $$\{1,2,3\}$$의 word로, $$1$$이 $$a$$개, $$2$$가 $$b-a$$개, $$3$$이 $$n-b$$개이다. 우리가 다루는 Grassmannian은 step이 하나뿐인 $$m=1$$의 경우라 글자가 둘 ($$V_k$$에 들어오는 자리와 그렇지 않은 자리)뿐이고, 관례상 이를 $$1$$과 $$0$$으로 적어 $$0/1$$ word가 된다. 아래 예시에서 이를 $$\Gr_2(\mathbb{C}^4)$$에 대해 끝까지 따라간다. 

<div class="example" markdown="1">

<ins id="ex15">**예시 15**</ins> $$n=4$$, $$k=2$$인 경우 $$W=S_4$$, $$W_{P_2}=S_2\times S_2$$이고, minimal length 대표원소는

$$W^{P_2}=\{1234,\,1324,\,1423,\,2314,\,2413,\,3412\}$$

의 여섯 개이다. 가령, 원소 $$w=1324$$는 $$w(1)=1<w(2)=3$$이고 $$w(3)=2<w(4)=4$$를 만족하는 shuffle이다. 각 대표원소의 길이는 inversion을 세어

$$\ell(1234)=0,\quad\ell(1324)=1,\quad\ell(1423)=\ell(2314)=2,\quad\ell(2413)=3,\quad\ell(3412)=4$$

이므로, $$\Gr_2(\mathbb{C}^4)$$은 차원 $$0,1,2,2,3,4$$의 여섯 Schubert cell로 paving된다. 이는 $$\dim \Gr_2(\mathbb{C}^4)=2\cdot 2=4$$와 정합적이며, cell의 총 개수는 $$\binom{4}{2}=6$$, 복소 차원별로는 $$0,1,2,3,4$$차에 각각 $$1,1,2,1,1$$개가 놓인다. 각 cell은 Young diagram(즉 $$2\times 2$$ 상자 안에 들어가는 partition)으로도 색인되며, $$\ell(w)$$가 그 partition의 상자 수에 해당한다.

이 여섯 cell이 $$\Gr_2(\mathbb{C}^4)$$에서 구체적으로 무엇인지는 행렬로 곧장 드러난다. $$2$$-plane $$V$$를 그 기저를 행으로 갖는 $$2\times4$$ 행렬로 적고, 각 행의 pivot($$=1$$)을 가장 오른쪽 nonzero 성분, 곧 $$\dim(V\cap E_j)$$가 뛰는 자리로 두면, pivot은 정확히 column $$\{w(1),w(2)\}$$에 놓이고 그 왼쪽의 non-pivot column 자리만 자유 좌표 $$\ast$$로 남는다. $$W^{P_2}=\{1234,1324,1423,2314,2413,3412\}$$ 순서대로

$$\begin{pmatrix}1&0&0&0\\0&1&0&0\end{pmatrix},\quad\begin{pmatrix}1&0&0&0\\0&\ast&1&0\end{pmatrix},\quad\begin{pmatrix}1&0&0&0\\0&\ast&\ast&1\end{pmatrix},$$

$$\begin{pmatrix}\ast&1&0&0\\\ast&0&1&0\end{pmatrix},\quad\begin{pmatrix}\ast&1&0&0\\\ast&0&\ast&1\end{pmatrix},\quad\begin{pmatrix}\ast&\ast&1&0\\\ast&\ast&0&1\end{pmatrix}$$

이다. 자유 좌표 $$\ast$$의 개수 $$0,1,2,2,3,4$$가 정확히 위에서 센 $$\ell(w)$$이고, 이것이 $$BwP/P\cong\mathbb{A}^{\ell(w)}$$의 명시적 좌표화다. 양 끝을 보면 $$\{1,2\}$$은 $$V=E_2$$ 한 점이고, $$\{3,4\}$$은 $$E_2$$와 transverse한 ($$\dim(V\cap E_2)=0$$) generic $$2$$-plane들의 big cell이다.

이 모든 데이터는 $$01$$-word, 곧 $$k\times(n-k)$$ 직사각형 위의 lattice path 하나로 압축된다. $$w\in W^{P_k}$$에 대해 $$b_j$$를 $$j$$가 pivot column ($$j\in\{w(1),\ldots,w(k)\}$$)이면 $$1$$, free column이면 $$0$$으로 두어 길이 $$n$$의 word $$b_1\cdots b_n$$을 적으면, $$1$$을 $$k$$개 가진 $$0/1$$ 수열이 되고, $$1$$을 세로 step, $$0$$을 가로 step으로 읽으면 직사각형의 한 꼭짓점에서 맞은편으로 가는 lattice path가 된다. 위 여섯 cell은 순서대로

$$1234\leftrightarrow1100,\quad1324\leftrightarrow1010,\quad1423\leftrightarrow1001,\quad2314\leftrightarrow0110,\quad2413\leftrightarrow0101,\quad3412\leftrightarrow0011$$

이다. word에서 $$0$$이 $$1$$보다 앞서는 쌍의 개수가 정확히 $$\ell(w)$$이고 ($$\ast$$ 행렬에서 각 pivot 왼쪽의 free 자리 수와 같다), 각 $$1$$ 앞에 놓인 $$0$$의 개수를 내림차순으로 적은 것이 그 cell의 partition $$\lambda$$, 곧 path가 가두는 Young diagram이다. 가령 $$0101$$은 $$0$$이 앞서는 쌍이 셋이라 $$\ell=3$$, $$\lambda=(2,1)$$에 대응한다. 거꾸로 word(또는 partition) 하나만 주어지면 $$1$$의 자리에서 pivot column $$\{w(1),\ldots,w(k)\}$$을 읽고 그 왼쪽 free 자리를 $$\ast$$로 채워 위 echelon 행렬과 cell을 통째로 복원할 수 있다. 결국 $$0/1$$ 수열, $$(k,n-k)$$-shuffle, partition, $$\ast$$ 행렬, Schubert cell은 한 데이터의 다섯 가지 표현인 셈이다.

각 cell의 closure가 Grassmannian의 Schubert variety로, $$\dim(V\cap E_{w(a)})\ge a$$ ($$1\le a\le k$$)라는 rank 조건으로 잘린다. 위 $$2\times2$$ Young diagram이 그 조건을 담는다.

</div>

## Schubert cell과 Schubert variety

이제 partial flag variety $$X=G/P$$ 위의 cell들과 그 closure를 이름 붙여 정리하자. $$B$$와 그 opposite Borel $$B^-$$를 고정하면 두 방향의 cell 구조를 동시에 얻는다.

<div class="definition" markdown="1">

<ins id="def16">**정의 16**</ins> $$w\in W^P$$에 대하여, *Schubert cell* $$X_w^\circ$$와 *opposite Schubert cell* $$X^w_\circ$$를 각각

$$X_w^\circ=BwP/P\subseteq G/P,\qquad X^w_\circ=B^-wP/P\subseteq G/P$$

로 정의하고, 그 closure

$$X_w=\overline{X_w^\circ},\qquad X^w=\overline{X^w_\circ}$$

를 각각 *Schubert variety*와 *opposite Schubert variety*라 한다.

</div>

정의에 의해 $$X_w^\circ\cong\mathbb{A}^{\ell(w)}$$이고 $$X^w_\circ\cong\mathbb{A}^{\dim(G/P)-\ell(w)}$$이다. 특히 $$X_{w_0^P}^\circ$$ ($$w_0^P$$는 $$W^P$$의 longest element)는 $$\ell(w_0^P)=\dim(G/P)$$인 open dense cell이고, $$X_e^\circ=\{eP\}$$는 $$B$$-fixed point이다. 대칭적으로 opposite 쪽에서는 $$X^e_\circ=B^-P/P$$가 open dense cell, $$X^{w_0^P}_\circ=\{w_0^PP\}$$가 $$B^-$$-fixed point가 된다. 즉 두 cell 구조는 서로 차원을 뒤집은 형태로 맞물린다.

Schubert variety들 사이의 포함관계는 Weyl group 위의 *Bruhat order*가 지배한다. Bruhat order $$\leq$$는 $$v$$의 어떤 reduced expression이 $$w$$의 어떤 reduced expression의 subword로 나타날 때 $$v\leq w$$로 정의되는 순서로, 기하적으로는 [§Borel subgroup, ⁋명제 16](/ko/math/lie_theory/borel_subgroup#prop16)에서 본 cell closure $$\overline{BwB}=\bigsqcup_{v\leq w}BvB$$를 통해 드러난다.

<div class="proposition" markdown="1">

<ins id="prop17">**명제 17**</ins> $$x,w\in W^P$$에 대하여 다음이 성립한다.

$$X_x\subseteq X_w\iff x\leq w\text{ in Bruhat order}$$

특히 $$X_w=\bigsqcup_{\substack{x\leq w\\ x\in W^P}}X_x^\circ$$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$X_w=\overline{BwP/P}$$이고 $$B$$는 connected solvable group이므로, $$B$$-orbit의 closure는 더 작은 차원의 $$B$$-orbit들의 union이다. Complete flag variety $$G/B$$에서 $$\overline{BwB/B}=\bigsqcup_{v\leq w}BvB/B$$가 성립함은 위에서 환기한 cell closure로부터 따라나오며, projection $$G/B\rightarrow G/P$$로 내리면 $$W_P$$-coset 내부의 차이가 무너져 $$x,w\in W^P$$에 대해 $$X_x^\circ\subseteq X_w$$가 정확히 $$x\leq w$$일 때 성립한다.

</details>

<div class="example" markdown="1">

<ins id="ex18">**예시 18**</ins> $$G/P=\Gr_2(\mathbb{C}^4)$$의 경우, $$W^{P_2}$$ 위의 Bruhat order는 두 maximal chain

$$1234\leq 1324\leq 1423\leq 2413\leq 3412$$

$$1234\leq 1324\leq 2314\leq 2413\leq 3412$$

으로 그려진다. 즉 $$1324$$ 아래에는 $$1234$$만 있고, 길이가 같은 $$1423$$과 $$2314$$는 서로 비교 불가능하며 둘 다 $$1324$$ 위·$$2413$$ 아래에 놓인다. 이 Hasse diagram은 두 갈래로 갈라졌다 다시 만나는 마름모꼴로, $$\Gr_2(\mathbb{C}^4)$$의 Schubert class들 사이의 포함관계를 그대로 보여준다. 가령 Schubert variety $$X_{2413}$$은 $$X_{1423}^\circ$$, $$X_{2314}^\circ$$, $$X_{1324}^\circ$$, $$X_{1234}^\circ$$를 모두 포함하는 차원 $$3$$의 subvariety이다.

이 순서는 [예시 15](#ex15)의 jump set으로 곧장 읽힌다. $$w$$를 그 jump set $$\{w(1)<w(2)\}$$으로 보면 Bruhat order는 성분별 순서, 즉 $$v\le w\iff v(1)\le w(1)$$이고 $$v(2)\le w(2)$$이다. 그래서 두 maximal chain은 $$\{1,2\}\le\{1,3\}\le\{1,4\}\le\{2,4\}\le\{3,4\}$$와 $$\{1,2\}\le\{1,3\}\le\{2,3\}\le\{2,4\}\le\{3,4\}$$이고, $$1423\leftrightarrow\{1,4\}$$와 $$2314\leftrightarrow\{2,3\}$$이 비교 불가능한 것은 $$4\not\le3$$이면서 $$2\not\le1$$이기 때문이다.

포함관계도 rank 조건으로 손에 잡힌다. $$X_{2413}$$의 조건 $$\dim(V\cap E_2)\ge1$$, $$\dim(V\cap E_4)\ge2$$ 중 뒤는 $$E_4=\mathbb{C}^4$$이라 자동이므로

$$X_{2413}=\{V\in\Gr_2(\mathbb{C}^4)\mid\dim(V\cap E_2)\ge1\},$$

곧 $$E_2$$와 만나는 $$2$$-plane 전체다. [예시 15](#ex15)의 여섯 cell 중 $$E_2$$와 transverse한 big cell $$3412$$만 이 조건을 어기므로, $$X_{2413}$$은 나머지 다섯 cell을 정확히 머금는다.

</div>

Schubert variety $$X_w\subseteq G/P$$는 일반적으로 singular하며, 그 singular locus 역시 더 작은 Schubert variety들의 union으로 표현된다. 한편 cohomology class $$[X_w]\in H^\ast(G/P)$$들은 명제 6 이후 논의한 대로 $$H^\ast(G/P)$$의 additive basis를 이루며, 이로부터 classical *Schubert calculus*라 불리는 intersection theory가 전개된다. 특히 Grassmannian의 경우 Schubert variety는 Young diagram으로 색인되고, 그들의 intersection number는 Littlewood–Richardson coefficient로 주어진다.

---

**참고문헌**

**[BB]** A. Björner, F. Brenti, *Combinatorics of Coxeter groups*, Graduate Texts in Mathematics **231**, Springer, 2005.

**[Ful]** W. Fulton, *Young tableaux*, London Mathematical Society Student Texts **35**, Cambridge University Press, 1997.

**[Hum]** J. E. Humphreys, *Linear algebraic groups*, Graduate Texts in Mathematics **21**, Springer, 1975.

**[Man]** L. Manivel, *Symmetric functions, Schubert polynomials and degeneracy loci*, SMF/AMS Texts and Monographs **6**, 2001.

**[Spr]** T. A. Springer, *Linear algebraic groups*, Progress in Mathematics **9**, Birkhäuser, 1998.
