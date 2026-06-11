---
title: "Richardson variety와 Peterson variety"
description: "Schubert variety와 opposite Schubert variety의 intersection으로 정의되는 Richardson variety와 regular nilpotent element가 잘라내는 Peterson variety를 함께 다룬다. 두 부분다양체의 정의·차원, intersection theory에서의 역할, Grassmannian과 type A에서의 구체적 모습, 그리고 Bruhat cell에 의한 stratification을 살펴본다."
excerpt: "두 opposite Schubert variety의 transversal한 intersection인 Richardson variety와 regular nilpotent의 Peterson variety: 정의·차원·intersection theory·stratification"

categories: [Math / Lie Theory]
permalink: /ko/math/lie_theory/richardson_peterson_variety
sidebar:
    nav: "Lie_theory-ko"

date: 2026-06-09
last_modified_at: 2026-06-09
weight: 6
published: false
---

[§Bruhat decomposition](/ko/math/lie_theory/bruhat_decomposition)에서 우리는 partial flag variety $$G/P$$가 Bruhat cell들로 분해되고, 각 cell의 closure인 Schubert variety가 $$G/P$$의 기하가 Weyl group의 조합론에 담겨있는 것을 보았다. 이 글에서는 그 분해 위에 자연스럽게 얹히는 두 종류의 부분다양체를 다룬다. 하나는 서로 opposite인 두 Bruhat 분해의 intersection으로 얻는 *Richardson variety*이고, 다른 하나는 regular nilpotent element 하나가 잘라내는 *Peterson variety*이다. 

## Richardson variety

우리는 [§Bruhat decomposition](/ko/math/lie_theory/bruhat_decomposition)에서와 같이 field $$\mathbb{C}$$ 위 connected reductive algebraic group $$G$$와 그 Borel subgroup $$B$$, 그리고 $$B$$를 포함하는 parabolic subgroup $$P$$를 고정한다. Opposite Borel subgroup $$B^-$$ ($$B\cap B^-=T$$)를 함께 두면, [§Bruhat decomposition, ⁋정의 16](/ko/math/lie_theory/bruhat_decomposition#def16)에서 도입한 두 방향의 cell 구조

$$X_w^\circ=BwP/P,\qquad X^w_\circ=B^-wP/P\qquad(w\in W^P)$$

와 그 Zariski closure인 Schubert variety $$X_w=\overline{X_w^\circ}$$, opposite Schubert variety $$X^w=\overline{X^w_\circ}$$를 얻는다. 두 cell은 각각 $$X_w^\circ\cong\mathbb{A}^{\ell(w)}$$, $$X^w_\circ\cong\mathbb{A}^{\dim(G/P)-\ell(w)}$$이며, Richardson variety는 이 두 방향의 cell의 intersection이다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> $$u,w\in W^P$$에 대하여, Schubert variety와 opposite Schubert variety의 intersection

$$R_{u,w}=X_w\cap X^u$$

을 *Richardson variety*라 하고, 두 열린 cell의 intersection

$$\mathring{R}_{u,w}=X_w^\circ\cap X^u_\circ$$

을 *open Richardson variety*라 한다.

</div>

정의에 의해 $$R_{u,w}$$는 $$G/P$$의 closed subvariety이고, $$\mathring{R}_{u,w}$$는 그 안의 Zariski open subset이다. 이 intersection은 Kazhdan–Lusztig [KL80]와 Deodhar [Deo85]의 연구에서 이미 등장한 것으로, 나중 Richardson [Ric92]에 의해 일반적인 기하적 성질이 연구되었다.

이 정의의 유용성은 Grassmannian $$\Gr(k,n)$$ (또는 일반적인 partial flag variety)에서 볼 수 있다. reference flag $$E_\bullet\colon E_1\subset E_2\subset\cdots\subset E_n=\mathbb{C}^n$$를 하나 고정하면, 각 Schubert cell은 그 안의 $$k$$차원 subspace $$V$$가 이 flag와 만나는 방식, 곧 $$\dim(V\cap E_j)$$가 $$j$$를 키울 때 어느 자리에서 뛰는지로 결정되었던 것을 기억하자. Grassmannian 안에서 두 Schubert cell의 intersection을 계산하는 것은 이들이 동시에 만족하는 incidence condition을 찾는 것이다. 그러나 두 Schubert cell을 같은 reference flag에 대해 정의하면 두 조건이 서로 독립이 아니어서 intersection이 기대 차원에서 어긋나므로, reference flag들을 서로 generic position에 있는 것으로 택해야 한다.

이것이 가장 쉽게 계산되는 예가 바로 주어진 flag $$E_i=\span\{e_1,\ldots,e_i\}$$를 거꾸로 읽는 *opposite flag* $$\tilde{E}_j=\span\{e_n,\ldots,e_{n-j+1}\}$$이다. 이렇게 잡은 두 flag는 모든 $$i,j$$에 대해 transversality condition

$$\dim(E_i\cap\tilde{E}_j)=\max(0,\,i+j-n)$$

을 만족한다. 곧 두 flag의 어느 piece 쌍을 잡아도 그 intersection이 가능한 한 작게 만난다는 뜻이다. Richardson variety는 바로 이렇게 generic position에 놓인 두 reference flag에 대한 Schubert 조건을 동시에 부과해 두 Schubert cell의 intersection을 보는 것으로, 정의에서 $$X_w$$가 $$B$$가 고정하는 표준 flag에 대한 조건, $$X^u$$가 $$B^-$$가 고정하는 opposite flag에 대한 조건이라는 사실이 바로 이 transversality에 해당한다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2 (Richardson [Ric92])**</ins> Open Richardson variety $$\mathring{R}_{u,w}$$가 비어있지 않을 필요충분조건은 Bruhat order에서 $$u\leq w$$인 것이다. 이 조건이 성립하면 $$\mathring{R}_{u,w}$$는 차원 $$\ell(w)-\ell(u)$$의 smooth irreducible affine variety이고, $$R_{u,w}$$는 그 Zariski closure이다.

</div>

직관적으로, Bruhat cell $$X_w$$는 낮은 차원에서부터 커지는 방향이고, opposite Bruhat cell $$X^u$$는 큰 차원에서부터 내려가는 방향인 것을 기억하자. 구체적으로 $$\dim X_w=\ell(w)$$이고 $$\dim X^u=\dim (G/P)-\ell(u)$$가 성립한다. 따라서 이들 opposite Bruhat cell이 nontrivial하게 만나기 위해서는 이들 두 variety의 차원의 합이 $$\dim(G/P)$$ 이상이어야 한다. 이 때 교집합의 기대차원이 명제의

$$\ell(w)+\dim (G/P)-\ell(u)-\dim (G/P)=\ell(w)-\ell(u)$$

이고, 만일 $$u\leq w$$라면, 차원이 잘 맞을 뿐 아니라 이들의 방향 또한 맞아서 (즉 [§Bruhat decomposition, ⁋예시 18](/ko/math/lie_theory/bruhat_decomposition#ex18)에서의 $$1423$$과 $$2314$$와 같은 일이 일어나지 않아서) 실제로 Richardson variety가 nonempty가 된다. 

그렇다면 다음 명제를 기대하는 것이 자연스럽다. 

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> $$u,w\in W^P$$에 대하여 cohomology ring $$H^\ast(G/P)$$에서

$$[X_w]\cdot[X^u]=[R_{u,w}]$$

이 성립한다 (단 $$u\not\leq w$$이면 $$R_{u,w}=\emptyset$$이고 양변이 $$0$$이다). 특히 $$\ell(u)=\ell(w)$$일 때

$$\int_{G/P}[X_w]\cdot[X^u]=\delta_{u,w}$$

이므로, opposite Schubert class들 $$\{[X^u]\}_{u\in W^P}$$은 Schubert class들 $$\{[X_w]\}_{w\in W^P}$$의 Poincaré dual basis를 이룬다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$X_w$$와 $$X^u$$는 $$B$$와 $$B^-$$가 주는 generic position에서 transversal하게 만나므로, 그 intersection class는 두 class의 곱과 같다. 이것이 $$[X_w]\cdot[X^u]=[R_{u,w}]$$이다 (Kleiman generic transversality, [Bri] 참조). $$\ell(u)=\ell(w)$$인 경우 $$R_{u,w}$$의 차원은 $$\ell(w)-\ell(u)=0$$이고, [명제 2](#prop2)에 의해 $$u=w$$이면 reduced point 하나, $$u\neq w$$이면 ($$u\leq w$$가 깨져) 공집합이다. 따라서 그 0차원 class의 차수, 곧 $$\int_{G/P}[X_w]\cdot[X^u]$$은 $$\delta_{u,w}$$이다.

</details>

[명제 3](#prop3)은 Schubert basis의 곱셈 structure constant를 Richardson variety의 차수로 환원한다. 세 class의 곱 $$[X_w]\cdot[X^u]\cdot[X_v]$$을 적분하면 세 generic position Schubert variety의 intersection number가 나오는데, 이것이 곧 structure constant이고, Grassmannian의 경우에는 Littlewood–Richardson 계수가 되며, 이로부터 classical Schubert calculus가 전개된다.

역시 가장 손에 잡히는 경우는 $$G/P=\Gr(k,n)\cong\GL_n(\mathbb{C})/P_k$$인 Grassmannian이다. 이때 $$W=S_n$$, $$W_{P_k}=S_k\times S_{n-k}$$이고, minimal length coset representative $$W^{P_k}$$은 [§Bruhat decomposition, ⁋명제 14](/ko/math/lie_theory/bruhat_decomposition#prop14)에서 본 $$(k,n-k)$$-shuffle들이다. Schubert variety $$X_w$$는 표준 flag $$E_\bullet$$에 대한 $$\dim(V\cap E_{w(a)})\geq a$$ 꼴의 rank 조건으로, opposite Schubert variety $$X^u$$는 opposite flag $$\tilde{E}_\bullet$$ ($$\tilde{E}_j=\span\{e_n,\ldots,e_{n-j+1}\}$$)에 대한 대칭적 rank 조건으로 잘린다. Richardson variety는 이 두 조건을 동시에 부과한 것이다.

<div class="example" markdown="1">

<ins id="ex4">**예시 4**</ins> $$\Gr(2,4)$$에서 $$u=1324$$, $$w=2413$$을 택하자. [§Bruhat decomposition, ⁋예시 18](/ko/math/lie_theory/bruhat_decomposition#ex18)의 jump set 순서로 $$1324\leftrightarrow\{1,3\}$$, $$2413\leftrightarrow\{2,4\}$$이고 성분별로 $$1\leq2$$, $$3\leq4$$이므로 $$u\leq w$$이며, $$\ell(2413)-\ell(1324)=3-1=2$$이다. 두 Schubert 조건은 각각

$$X_{2413}=\{V\mid\dim(V\cap E_2)\geq1\},\qquad X^{1324}=\{V\mid\dim(V\cap\tilde{E}_2)\geq1\}$$

로, $$E_2=\span\{e_1,e_2\}$$와 $$\tilde{E}_2=\span\{e_3,e_4\}$$은 서로 complementary한 두 평면이다. 따라서

$$R_{1324,2413}=\{V\in\Gr(2,4)\mid V\cap E_2\neq0,\ V\cap\tilde{E}_2\neq0\}$$

은 $$E_2$$ 안의 한 line과 $$\tilde{E}_2$$ 안의 한 line을 골라 span한 평면들의 모임이다. $$E_2\cap\tilde{E}_2=0$$이므로 두 line은 항상 독립이고, 대응 $$([\,p\,],[\,q\,])\mapsto\langle p,q\rangle$$은 isomorphism

$$R_{1324,2413}\cong\mathbb{P}(E_2)\times\mathbb{P}(\tilde{E}_2)\cong\mathbb{P}^1\times\mathbb{P}^1$$

을 준다. 차원 $$2$$의 variety로, [명제 2](#prop2)의 차원과 정확히 맞는다. 그 open part는 행렬

$$V=\operatorname{rowspan}\begin{pmatrix}1&s&0&0\\0&0&1&t\end{pmatrix}\qquad(s,t)\in\mathbb{A}^2$$

로 좌표화되는데, 위 행렬의 jump set이 $$\{2,4\}$$이므로 $$V\in X_{2413}^\circ$$이고 둘째 행이 $$\tilde{E}_2$$ 안에 있으므로 $$V\in X^{1324}_\circ$$이다. 즉 $$\mathring{R}_{1324,2413}$$은 이 $$(s,t)$$-평면의 open subset으로, affine 차원 $$2$$임이 좌표에서 곧장 드러난다.

</div>

## Peterson variety

이제 우리의 관점을 다소 바꾸어 새로운 variety를 정의한다. 이는 우선 flag variety $$G/B$$를 보는 새로운 방법으로 시작한다. $$G$$는 자기 자신의 Borel subalgebra들 위에 다음의 conjugation action 

$$g\cdot\mathfrak{b}'=\Ad(g)\,\mathfrak{b}'$$

으로 작용하는 것을 기억하자 ([§Borel subgroup, ⁋명제 10](/ko/math/lie_theory/borel_subgroup#prop10)). 이 때, 임의의 두 Borel subalgebra는 conjugate이므로, 이 action은 transitive하고, $$\mathfrak{b}$$의 stabilizer는 그 normalizer $$N_G(\mathfrak{b})=B$$이다. 따라서 orbit-stabilizer 정리로 얻어지는 $$gB\mapsto\Ad(g)\mathfrak{b}$$가 $$G/B$$와 Borel subalgebra들의 집합 사이의 일대일 대응을 준다. 즉, $$G/B$$는 $$G$$의 Borel subalgebra들의 variety로 생각할 수 있다. 

이제 다시 $$G/B$$가 flag variety이고, $$gB$$는 이 variety의 한 점으로서 flag 하나를 결정한다는 것을 기억하자. 즉, 위의 bijection은 $$G/B$$의 flag 하나마다 그에 대응하는 Borel subalgebra $$\Ad(g)\mathfrak{b}$$를 붙여준 것이다. 그런데 이는 조금 더 일반화할 수 있다. $$\mathfrak{b}$$를 포함하는 $$\ad(\mathfrak{b})$$-stable subspace $$H\subseteq\mathfrak{g}$$를 택하면, $$H$$가 $$B$$-stable이므로 $$\Ad(g)H$$ 역시 coset $$gB$$에만 의존하기 때문이다. 즉, 각 flag마다 subspace $$\Ad(g)H$$를 하나씩 대응시켜줄 수 있다. 

이제 이 관점에서, 고정된 원소 $$X\in \mathfrak{g}$$가 이러한 subspace 중 어떤 것에 들어가는지를 생각하면 이는 flag variety에서는 적절한 종류의 incidence condition으로 해석된다. 실제로 이 조건 $$\Ad(g^{-1})X\in H$$은 $$g$$의 각 entry에 대한 다항식 조건이므로, 이를 만족하는 $$gB$$들의 집합은 실제로 $$G/B$$의 closed subvariety를 이룬다. 

우리의 관심의 대상은 이 closed variety이며, 이는 당연히 $$X$$와 $$H$$의 선택에 의존한다. 가령 $$X=0$$이면 위의 조건은 항상 성립할 것이므로 이는 flag variety $$G/B$$ 전체가 된다. $$X$$에 대한 의존성을 가늠하게 해 주는 것은 $$X$$의 centralizer이다. $$X$$를 centralize하는 $$G$$의 원소 $$z$$를 생각하자. 그럼 $$z$$가 $$G/B$$ 위에 $$gB\mapsto zgB$$에 작용하면 incidence condition의 좌변은

$$\Ad((zg)^{-1})X=\Ad(g^{-1})X$$

으로 변한다. 즉, 이 incidence condition은 $$z$$의 left translation에 대해 invariant이고 이로부터 우리가 생각하는 closed variety 위에 centralizer $$C_G(X)$$의 group action이 정의된다. 즉, 이 closed variety는 $$C_G(X)$$-orbit들의 합집합이고, 따라서 직관적으로는 centralizer가 클수록 이렇게 잘려나오는 $$G/B$$의 closed subvariety가 클 것으로 기대할 수 있다. 예를 들어 $$X=0$$인 경우는 centralizer가 $$G$$ 전체인 극단적인 경우였다. 그런데 centralizer의 차원은 어떤 $$X\in\mathfrak{g}$$를 택해도 $$\rank(\mathfrak{g})$$ 아래로 내려갈 수 없다는 것이 알려져 있으므로 ([Kos63]), 반대쪽 극단은 이 최솟값을 달성하는 원소들이다. 

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> Nilpotent element $$X\in\mathfrak{g}$$가 *regular*라는 것은 그 centralizer $$\mathfrak{z}_{\mathfrak{g}}(X)=\{Z\in\mathfrak{g}\mid[Z,X]=0\}$$의 차원이 $$\rank(\mathfrak{g})$$와 같은 것이다.

</div>

Regular nilpotent는 표준적인 구성으로 언제나 존재한다. 각각의 simple root $$\alpha_i$$마다 $$0\neq e_i\in\mathfrak{g}_{\alpha_i}$$를 골라 $$e=\sum_i e_i$$로 두면 regular nilpotent가 되기 때문이다. 

우리에게 익숙한 type $$A_{n-1}$$에서는 이것이 친숙한, 구체적인 예시가 된다. 위의 구성은 superdiagonal이 모두 $$1$$인 principal nilpotent

$$N=\sum_{i=1}^{n-1}E_{i,i+1}=\begin{pmatrix}0&1&&\\&0&\ddots&\\&&\ddots&1\\&&&0\end{pmatrix}$$

을 준다. $$[Z,N]=0$$을 성분별로 풀면 centralizer가 $$N$$의 polynomial들

$$\mathfrak{z}_{\mathfrak{sl}_n}(N)=\span\{N,N^2,\ldots,N^{n-1}\}$$

임을 알 수 있고, 이 공간의 차원이 정확히 $$n-1=\rank(\mathfrak{sl}_n)$$이므로 $$N$$은 regular이다. Jordan 표준형의 관점에서 보면 $$N$$은 Jordan block이 하나뿐인 nilpotent, 곧 partition $$(n)$$에 대응하는 원소이다. Jordan block의 수가 많을수록 centralizer가 커지므로, regular nilpotent는 nilpotent element 가운데 centralizer가 가장 작은 conjugacy class라 생각할 수 있다.

일반적인 type에서 $$e=\sum_i e_i$$가 regular라는 것, 모든 regular nilpotent가 $$G$$의 adjoint action으로 서로 conjugate하다는 것, 그리고 그 centralizer가 언제나 abelian이라는 것은 Kostant [Kos]의 고전적 결과이다.

이제 $$X$$를 고정해 두고 보던 이 closed subvariety에 $$H$$에 대한 의존성을 추가하자. 우선 편의상 이름을 먼저 붙인다. 

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> $$X\in\mathfrak{g}$$와 $$\mathfrak{b}$$를 포함하는 $$\ad(\mathfrak{b})$$-stable subspace $$H\subseteq\mathfrak{g}$$ (즉 $$[\mathfrak{b},H]\subseteq H$$)에 대하여, *Hessenberg variety*는

$$\mathcal{B}(X,H)=\{\,gB\in G/B\;\mid\;\Ad(g^{-1})X\in H\,\}$$

로 정의되는 $$G/B$$의 closed subvariety이다.

</div>

위에서 살펴봤듯 $$X$$는 그 centralizer를 통해 variety의 크기에 영향을 미치며, 이 subspace $$H$$ 또한 마찬가지이다. 두 극단적인 상황으로, 우리는 $$H=\mathfrak{g}$$인 경우 조건 $$\Ad(g^{-1})X\in\mathfrak{g}$$가 자명하게 성립하여 Hessenberg variety는 $$G/B$$전체이다. 반대쪽 극단 $$H=\mathfrak{b}$$에서는 조건 $$\Ad(g^{-1})X\in\mathfrak{b}$$가 Borel subalgebra $$\Ad(g)\mathfrak{b}$$가 $$X$$를 포함한다는 말과 같다. 만일 $$X$$가 regular nilpotent라면 이 원소는 정확히 하나의 Borel subalgebra에만 속하므로, $$\mathcal{B}(X, \mathfrak{b})$$는 한 점으로 줄어든다. 



, 이렇게 잘리는 $$\mathcal{B}(X,\mathfrak{b})$$를 $$X$$의 *Springer fiber*라 부른다. type $$A$$에서 이 조건은 한층 구체적이다. $$\Ad(g)\mathfrak{b}$$는 flag $$V_\bullet=g\cdot E_\bullet$$를 보존하는 연산자들의 집합이므로, $$\Ad(g^{-1})X\in\mathfrak{b}$$는 $$XV_i\subseteq V_i$$, 곧 "$$X$$가 그 flag를 보존한다"로 읽힌다. 특히 $$X$$가 regular nilpotent이면 $$X$$를 보존하는 complete flag은 단 하나뿐이므로 (동치로, regular nilpotent는 정확히 하나의 Borel subalgebra에 속하므로) Springer fiber $$\mathcal{B}(X,\mathfrak{b})$$는 한 점으로 줄어든다.

우리가 관심을 두는 것은 이 두 극단 사이, 정확히는 한 점짜리 $$H=\mathfrak{b}$$에서 딱 한 걸음 더 간 경우이다. $$\mathfrak{b}$$ 위에 negative simple root 방향의 자유도를 하나씩 더한 $$H=\mathfrak{b}\oplus\bigoplus_i\mathbb{C}f_i$$ ($$f_i\in\mathfrak{g}_{-\alpha_i}$$)를 택하고 $$X$$로는 regular nilpotent를 넣자. 더한 자유도가 simple root의 개수, 곧 $$\rank(\mathfrak{g})$$개이므로 한 점에서 차원이 그만큼 자라리라 기대할 수 있고, 실제로 그렇게 된다는 것이 아래 [명제 9](#prop9)의 내용이다. 그 결과로 얻어지는 Hessenberg variety가 바로 *Peterson variety*이다.

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> *Peterson variety* $$Y^\circ$$는 $$G/B$$의 closed subvariety

$$Y^\circ=\{\,gB\in G/B\;\mid\;\Ad(g^{-1})e\in H\,\}$$

로 정의된다. 여기서 $$e=\sum_i e_i$$는 regular nilpotent이고, $$H=\mathfrak{b}\oplus\bigoplus_i\mathbb{C}f_i$$이며 $$f_i\in\mathfrak{g}_{-\alpha_i}$$는 simple negative root의 root vector이다. 곧 [정의 6](#def6)에서 $$X=e$$를 regular nilpotent로, subspace $$H$$를 $$\mathfrak{b}$$ 바로 위 단계로 택한 특수한 경우이다.

</div>

이것이 Kostant–Peterson의 원래 정의 [Pet]이다. 정의가 여러 선택에 의존하는 것처럼 보이지만 사실상 유일하다. $$f_i$$의 선택은 $$\mathbb{C}f_i=\mathfrak{g}_{-\alpha_i}$$가 $$1$$차원이므로 $$H$$를 바꾸지 않고, $$e$$를 다른 regular nilpotent로 바꾸는 것은 ([정의 5](#def5) 직후 논의의 conjugacy에 의해) $$Y^\circ$$를 $$G/B$$ 안에서 translate할 뿐이다.

<div class="remark" markdown="1">

<ins id="rmk8">**참고 8**</ins> 거울대칭 문헌, 특히 Rietsch [Rie]와 그를 따르는 글들은 Peterson variety를 (Langlands dual group의) opposite flag variety $$G/B^-$$ 위에서 coadjoint 조건 $$\Ad^\ast(g^{-1})F\in[\mathfrak{n}^-,\mathfrak{n}^-]^\perp$$ ($$F$$는 regular nilpotent)로 정의한다. Killing form으로 $$\mathfrak{g}^\ast\cong\mathfrak{g}$$를 동일시하면 $$[\mathfrak{n}^-,\mathfrak{n}^-]^\perp=\mathfrak{b}^-\oplus\bigoplus_i\mathfrak{g}_{\alpha_i}$$이므로, 이는 [정의 7](#def7)의 Hessenberg 조건에서 $$B$$와 $$B^-$$의 역할을 일괄적으로 맞바꾼 것에 지나지 않는다. 곧 두 기술은 같은 variety를 두 좌표로 적은 것이며, 이 글에서는 일관되게 $$G/B$$ 컨벤션을 쓴다.

</div>

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> Peterson variety $$Y^\circ\subseteq G/B$$의 차원은 $$\rank(\mathfrak{g})$$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

핵심 도구는 Bruhat cell들과의 교집합이다. Tymoczko [Tym]와 Precup [Pre]은 regular nilpotent Hessenberg variety가 Bruhat 분해와의 교집합 $$Y^\circ\cap BwB/B$$들로 affine paving됨을 보였다. 곧 비어있지 않은 각 조각이 affine space와 동형이고, 따라서 가장 큰 조각의 차원이 $$Y^\circ$$ 전체의 차원이 된다. Peterson variety의 경우 비어있지 않은 조각을 [Tym]의 조합적 조건으로 분류하면, simple root들의 부분집합 $$A\subseteq\Delta$$마다 parabolic Weyl group $$W_A$$의 최장원소 $$w_A$$에 대응하는 cell이 비어있지 않은 조각의 전부이다 ([IT]). 각 조각의 차원은 [Tym]의 공식

$$\dim\bigl(Y^\circ\cap Bw_AB/B\bigr)=\dim\bigl(\mathfrak{b}\cap\Ad(w_A)(\mathfrak{b}^-\cap H)\bigr)-\rank(\mathfrak{g})$$

으로 주어지는데, $$\mathfrak{b}^-\cap H=\mathfrak{h}\oplus\bigoplus_i\mathfrak{g}_{-\alpha_i}$$에서 $$\mathfrak{h}$$는 $$\Ad(w_A)$$에 의해 $$\mathfrak{h}$$로 가고, $$\mathfrak{g}_{-\alpha_i}$$는 ($$w_A$$가 부호를 뒤집는 simple root가 정확히 $$A$$의 원소들이므로) $$\alpha_i\in A$$일 때에만 positive root space로 가서 $$\mathfrak{b}$$와 만난다. 따라서 이 값은 $$\rank(\mathfrak{g})+\lvert A\rvert-\rank(\mathfrak{g})=\lvert A\rvert$$이다. 결국 $$Y^\circ$$는 $$2^{\rank(\mathfrak{g})}$$개의 affine cell로 paving되며, 최대 차원의 cell은 $$A=\Delta$$, 곧 big Bruhat cell과의 교집합 $$Y^\circ\cap Bw_0B/B\cong\mathbb{A}^{\rank(\mathfrak{g})}$$이다.

</details>

이 증명은 차원 이상의 정보를 준다. $$Y^\circ$$는 simple root들의 부분집합으로 색인되는 $$2^{\rank(\mathfrak{g})}$$개의 cell로 이루어지고, 각 cell은 coordinate flag $$w_AB$$를 지난다. 이 조합론은 아래 [예시 10](#ex10)의 fixed point 목록에서 다시 만난다. type $$A_{n-1}$$에서는 $$\rank(\mathfrak{sl}_n)=n-1$$이므로 $$\dim Y^\circ=n-1$$이며, [예시 10](#ex10)에서 $$\dim\Pet_3=2=3-1$$임을 chart 계산으로 직접 확인한다.

<div class="example" markdown="1">

<ins id="ex10">**예시 10**</ins> type $$A_{n-1}$$, 곧 $$G=\GL_n(\mathbb{C})$$에서 [정의 6](#def6)의 조건을 직접 풀어 보자. coset $$gB$$에 대응하는 flag를 $$V_\bullet=g\cdot E_\bullet$$ (즉 $$V_i=\span\{ge_1,\ldots,ge_i\}$$)라 하면, principal nilpotent $$N=\sum_{i=1}^{n-1}E_{i,i+1}$$과 $$H=\mathfrak{b}\oplus\bigoplus_i\mathbb{C}f_i=\{Y\mid YE_i\subseteq E_{i+1}\ \forall i\}$$에 대하여

$$\Ad(g^{-1})N\in H\iff g^{-1}Ng\in H\iff NgE_i\subseteq gE_{i+1}\iff NV_i\subseteq V_{i+1}$$

이 성립한다 (가운데 동치는 $$H$$의 정의식 $$(g^{-1}Ng)E_i\subseteq E_{i+1}$$의 양변에 $$g$$를 씌운 것이고, $$gE_i=V_i$$이다). 따라서 Peterson variety는 complete flag variety $$Fl_n=\GL_n(\mathbb{C})/B$$ 안에서

$$\Pet_n=\{\,V_\bullet\mid NV_i\subseteq V_{i+1},\ i=1,\ldots,n-1\,\}$$

로 주어진다. 이는 Hessenberg 함수 $$h=(2,3,\ldots,n,n)$$에 대응하며, 그 차원은 $$\sum_{j=1}^n\bigl(h(j)-j\bigr)=n-1=\rank(\mathfrak{sl}_n)$$으로 [명제 9](#prop9)과 일치한다.

$$n=3$$에서 구체적으로, $$Ne_1=0$$, $$Ne_2=e_1$$, $$Ne_3=e_2$$이고 마지막 조건 $$NV_2\subseteq V_3=\mathbb{C}^3$$은 자동이므로

$$\Pet_3=\{(V_1\subset V_2)\in Fl_3\mid NV_1\subseteq V_2\}$$

이다. $$\dim_\mathbb{C}Fl_3=3$$에서 조건 하나가 차원을 $$1$$ 깎아 $$\dim\Pet_3=2$$가 된다. 이 surface가 지나는 coordinate flag $$E^w_\bullet$$ ($$w\in S_3$$, $$V_i=\span\{e_{w(1)},\ldots,e_{w(i)}\}$$)들은 $$Ne_{w(1)}\in\span\{e_{w(1)},e_{w(2)}\}$$을 만족하는 $$w$$, 즉

$$w\in\{e,\,s_1,\,s_2,\,w_0\}=\{123,\,213,\,132,\,321\}$$

의 네 개이다. 이들은 simple root 부분집합 $$A\subseteq\{\alpha_1,\alpha_2\}$$에 그 parabolic의 maximal length element $$w_A$$를 대응시킨 $$2^{n-1}=4$$개의 fixed point로, Peterson variety가 simple root들의 조합론을 기억하고 있음을 보여 준다.

</div>

## Stratification

[명제 9](#prop9)의 증명에서 우리는 $$Y^\circ$$를 $$B$$쪽 Bruhat cell들로 잘라 affine paving을 얻었다. 이번에는 반대쪽, 곧 opposite Borel $$B^-$$의 Bruhat 분해로 $$Y^\circ$$를 잘라 보자. 결과의 성격은 전혀 다르다. 조각들이 더 이상 affine space가 아닌 대신, 각 조각이 그 자체로 의미를 갖는 affine variety가 된다.

이번에도 비어있지 않은 조각은 정확히 $$2^{\rank(\mathfrak{g})}$$개이며, simple root들의 부분집합, 곧 standard parabolic subgroup $$P\supseteq B$$들로 색인되어 $$Y^\circ$$의 stratification

$$Y^\circ=\bigsqcup_{P\supseteq B}Y_P^\circ$$

을 이룬다 [Pet]. 여기서 각 stratum $$Y_P^\circ$$는 $$B^-$$쪽 Bruhat cell 하나와의 교집합으로 주어지는 locally closed subvariety이다. 양 극단을 보면 $$P=G$$의 stratum은 한 점 $$\{w_0B\}$$이고, $$P=B$$의 stratum은 opposite big cell과의 교집합

$$Y_B^\circ=Y^\circ\cap B^-B/B$$

으로 주어지는 $$Y^\circ$$의 Zariski 조밀 open subset이다. 일반적으로 $$Y_P^\circ$$의 차원은 $$P$$에 들어있지 않은 simple root의 개수와 같다. 곧 paving의 cell과 stratification의 stratum은 개수가 같으면서 차원은 서로 보완적인 방향으로 자란다.

이 분해가 단순한 기하학적 호기심이 아닌 이유는 Dale Peterson의 다음 정리 때문이다.

<div class="proposition" markdown="1">

<ins id="thm11">**정리 11 (Peterson [Pet])**</ins> 각 standard parabolic subgroup $$P\supseteq B$$에 대하여, stratum $$Y_P^\circ$$의 coordinate ring은 partial flag variety $$G/P$$의 small quantum cohomology ring과 동형이다.

$$\mathbb{C}[Y_P^\circ]\cong qH^\ast(G/P)$$

</div>

곧 flag variety 안의 단 하나의 subvariety가 모든 partial flag variety $$G/P$$의 quantum cohomology를 strata에 나누어 담고 있다는 것이다. 이 동형 아래에서 quantum parameter들은 $$Y_P^\circ$$ 위의 명시적인 regular function이 되며, stratum을 big Bruhat cell $$Bw_0B/B$$와 한 번 더 교차시킨 open subset은 quantum parameter들을 invert한 localization에 대응한다. 위 정리는 Peterson의 1997년 MIT 강의 [Pet]에서 발표되었으나 증명이 출판되지 않았고, $$P=B$$의 경우는 quantum Toda lattice를 매개로 한 Kostant [Kos96]의 결과와 동치이며, type A는 Rietsch [Rie]가, 일반형은 최근 Chow [Cho]가 증명을 완성했다. 우리는 이 정리를 ([\[거울대칭\] §Marsh-Rietsch Mirror Theorem](/ko/math/mirror_symmetry/mr_mirror_theorem))에서 Marsh–Rietsch mirror theorem의 마지막 다리로 사용한다.

<div class="remark" markdown="1">

<ins id="rmk12">**참고 12**</ins> [명제 9](#prop9) 증명의 affine paving은 cohomology 계산의 출발점이기도 하다. Paving에 의해 $$Y^\circ$$의 cohomology는 cell들로 색인된 basis를 갖는 free module이고 홀수 차수에서 사라진다. 즉 [§Bruhat decomposition, ⁋명제 17](/ko/math/lie_theory/bruhat_decomposition#prop17)에서 본 flag variety의 affine paving 논법이 Peterson variety에도 그대로 작동하며, Insko–Tymoczko [IT]는 이를 바탕으로 Peterson variety의 intersection theory를 전개하였다.

</div>

---

**참고문헌**

**[KL80]** D. Kazhdan, G. Lusztig, *Schubert varieties and Poincaré duality*, Geometry of the Laplace operator, Proc. Sympos. Pure Math. **36**, AMS, 1980.

**[Deo85]** V. V. Deodhar, *On some geometric aspects of Bruhat orderings. I. A finer decomposition of Bruhat cells*, Invent. Math. **79** (1985), 499--511.

**[Ric92]** R. W. Richardson, *Intersections of double cosets in algebraic groups*, Indag. Math. **3** (1992), 69--77.

**[Bri]** M. Brion, *Lectures on the geometry of flag varieties*, in *Topics in cohomological studies of algebraic varieties*, Trends Math., Birkhäuser, 2005, 33--85.

**[Kos]** B. Kostant, *The principal three-dimensional subgroup and the Betti numbers of a complex simple Lie group*, Amer. J. Math. **81** (1959), 973--1032.

**[Kos63]** B. Kostant, *Lie group representations on polynomial rings*, Amer. J. Math. **85** (1963), 327--404.

**[Kos96]** B. Kostant, *Flag manifold quantum cohomology, the Toda lattice, and the representation with highest weight $$\rho$$*, Selecta Math. (N.S.) **2** (1996), 43--91.

**[Pet]** D. Peterson, Lecture notes, Massachusetts Institute of Technology, Spring 1997 (unpublished).

**[Rie]** K. Rietsch, *Totally positive Toeplitz matrices and quantum cohomology of partial flag varieties*, J. Amer. Math. Soc. **16** (2003), 363--392.

**[Tym]** J. S. Tymoczko, *Paving Hessenberg varieties by affines*, Selecta Math. (N.S.) **13** (2007), 353--367.

**[Pre]** M. Precup, *Affine pavings of Hessenberg varieties for semisimple groups*, Selecta Math. (N.S.) **19** (2013), 903--922.

**[IT]** E. Insko, J. Tymoczko, *Affine pavings of regular nilpotent Hessenberg varieties and intersection theory of the Peterson variety*, J. Combin. Theory Ser. A **187** (2022), 105572.

**[Cho]** C. H. Chow, *On D. Peterson's presentation of quantum cohomology of $$G/P$$*, arXiv:2210.17382.
