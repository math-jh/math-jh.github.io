---
title: "Richardson variety와 Peterson variety"
description: "Schubert variety와 opposite Schubert variety의 intersection으로 정의되는 Richardson variety와 regular nilpotent element가 잘라내는 Peterson variety를 함께 다룬다. 두 부분다양체의 정의·차원, intersection theory에서의 역할, Grassmannian과 type A에서의 구체적 모습, 그리고 Bruhat cell에 의한 stratification을 살펴본다."
excerpt: "두 opposite Schubert variety의 transversal한 intersection인 Richardson variety와 regular nilpotent의 Peterson variety: 정의·차원·intersection theory·stratification"

categories: [Math / Lie Theory]
permalink: /ko/math/lie_theory/richardson_peterson_variety
sidebar:
    nav: "Lie_theory-ko"

date: 2026-06-09
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

직관적으로, Schubert variety $$X_w$$는 한 점 $$X_e=\{eP\}$$에서 낮은 차원부터 커 가는 방향이고, opposite Schubert variety $$X^u$$는 $$G/P$$ 전체에서 큰 차원부터 내려오는 방향인 것을 기억하자. 구체적으로 $$\dim X_w=\ell(w)$$이고 $$\dim X^u=\dim(G/P)-\ell(u)$$이므로, 두 variety가 만나기 위해서는 우선 차원의 합이 $$\dim(G/P)$$ 이상, 곧 $$\ell(u)\leq\ell(w)$$이어야 하고, 이 때 교집합의 기대차원이 명제의

$$\ell(w)+\dim (G/P)-\ell(u)-\dim (G/P)=\ell(w)-\ell(u)$$

이다.

그러나 차원이 맞는 것만으로 교집합이 비어있지 않다고 결론지을 수는 없다. 가령 [§Bruhat decomposition, ⁋예시 18](/ko/math/lie_theory/bruhat_decomposition#ex18)의 비교 불가능한 쌍 $$u=1423$$, $$w=2314$$를 생각하면, 이들의 길이가 같아 기대차원이 $$0$$차원임에도 불구하고, 이들의 교집합은 점들의 집합이 아니라 공집합이다. 실제로 무슨 일이 일어나는지 $$\Gr(2,4)$$에서 직접 살펴보자. $$X_{2314}$$의 점은 rank 조건 $$\dim(V\cap E_3)\geq2$$, 곧 $$V\subseteq E_3$$을 만족한다. 반면 opposite cell $$X^{1423}_\circ=B^-\cdot\span\{e_1,e_4\}$$의 점은 모두 $$e_4$$를 포함하며 (lower triangular 행렬은 $$e_4$$를 scalar배까지 고정한다), $$e_4\in V$$는 closed 조건이므로 closure $$X^{1423}$$에서도 유지된다. $$e_4\notin E_3$$이므로 두 요구는 양립할 수 없고, 두 variety는 차원이 충분한데도 서로 비껴간다.

이러한 현상은 $$X_w$$와 $$X^u$$가 general position에 있는 임의의 subvariety들이 아니라, 둘 다 maximal torus $$T$$의 작용에 invariant인 특별한 위치의 subvariety들이라는 점에서 기인한다. 이러한 성질 때문에 이들의 교집합 $$X_w\cap X^u$$도 closed $$T$$-stable subvariety인데, 비어있지 않은 closed $$T$$-stable subvariety는 언제나 $$T$$-fixed point를 포함한다는 것이 알려져 있다 (Borel fixed point theorem, [Bri] 참조). 그런데 $$G/P$$의 $$T$$-fixed point는 coordinate point $$vP$$ ($$v\in W^P$$)들 뿐이다 ([§Bruhat decomposition, ⁋명제 19](/ko/math/lie_theory/bruhat_decomposition#prop19)). 한편 $$vP\in X_w$$는 ([§Bruhat decomposition, ⁋명제 17](/ko/math/lie_theory/bruhat_decomposition#prop17)에 의해) $$v\leq w$$와 동치이고, 대칭적으로 $$vP\in X^u$$는 $$u\leq v$$와 동치이다. 따라서

$$X_w\cap X^u\neq\emptyset\iff\text{$u\leq v\leq w$인 $v\in W^P$가 존재}\iff u\leq w$$

이다. 위의 예에서는 jump set 조건 $$\{1,4\}\leq\{v(1),v(2)\}\leq\{2,3\}$$이 $$4\leq v(2)\leq3$$을 요구하므로 그런 $$v$$가 없고, 역으로 $$u\leq w$$이면 $$v=u$$를 택할 수 있어 fixed point $$uP$$가 이미 $$R_{u,w}$$의 점이 된다. 이것이 [명제 2](#prop2)의 조건 $$u\leq w$$의 정확한 기하학적 내용이다.

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

위에서 살펴봤듯 $$X$$는 그 centralizer를 통해 variety의 크기에 영향을 미치며, 이 subspace $$H$$ 또한 마찬가지이다. 두 극단적인 상황으로, 우리는 $$H=\mathfrak{g}$$인 경우 조건 $$\Ad(g^{-1})X\in\mathfrak{g}$$가 자명하게 성립하여 Hessenberg variety는 $$G/B$$전체이다. 반대쪽 극단 $$H=\mathfrak{b}$$에서는 조건 $$\Ad(g^{-1})X\in\mathfrak{b}$$가 Borel subalgebra $$\Ad(g)\mathfrak{b}$$가 $$X$$를 포함한다는 말과 같으며, 만일 $$X$$가 nilpotent라면 우리는 이를 $$X$$의 *Springer fiber*라 부른다. 

우리가 정의할 Peterson variety는 $$X$$와 $$H$$를 이용하여 최대한의 조건을 부과한 closed subvariety로 생각할 수 있다. $$X$$에 대해서는 [정의 6](#def6) 이전의 논증에 의하여 regular nilpotent 조건이 가장 강한 조건을 부과함을 살펴보았는데, 이 경우 $$X$$는 정확히 하나의 Borel subalgebra에만 속하여 Springer fiber $$\mathcal{B}(X, \mathfrak{b})$$는 한 점으로 줄어들게 된다. 따라서 우리는 여기서 $$H$$에 대한 조건을 약간 널널하게 잡아 Peterson variety를 정의하게 된다. 

$$H$$를 어느 방향으로 키울 수 있는지는 type $$A$$에서 [정의 6](#def6)의 조건을 좌표로 직접 풀어 보면 선명해진다.

<div class="example" markdown="1">

<ins id="ex7">**예시 7**</ins> 위에서 살펴본 type $$A_{n-1}$$로 돌아가자. 이 경우, $$G=\GL_n(\mathbb{C})$$이고 $$\mathfrak{b}$$는 upper triangular 행렬들의 공간이며, $$\gl_n$$의 Cartan subalgebra는 대각행렬들의 공간 $$\mathfrak{h}$$이다.[^1]

이제 $$H$$는 $$\ad(\mathfrak{b})$$-stable이므로 $$\ad(\mathfrak{h})$$-stable이기도 해야 한다. 임의의 $$Y\in H$$와 임의의 대각행렬 $$\diag(t_1,\ldots, t_n)$$과의 bracket을 계산해보면 

$$\ad(\diag(t_1,\ldots, t_n))Y=[\diag(t_1,\ldots, t_n), Y]=((t_j-t_k)Y_{jk})_{1\leq j,k\leq n}$$

이며, $$\ad(\mathfrak{h})$$-stability가 성립하려면 이것이 다시 $$H$$에 속해야 한다. 

한편, 위의 계산은 특히 $$\ad(\diag(t_1,\ldots, t_n))$$를 $$\gl_n$$ 위에서의 linear operator로 보았을 때, 이 linear operator가 $$\gl_n$$의 basis들 $$E_{jk}$$ 모두를 eigenvector들로 가지는 것을 보여준다. 이제 $$t$$를 generic하게 잡으면 eigenvalue $$t_j-t_k$$ ($$j\neq k$$)들이 $$0$$과도 서로와도 모두 달라지고, 따라서 이 operator에 invariant한 subspace $$H$$는 각 eigenspace와의 교집합들로 쪼개져 weight decomposition

$$H=(H\cap \mathfrak{h})\oplus\bigoplus_{j\neq k}(H\cap \mathbb{C}E_{jk})$$

이 성립한다. 따라서 $$H$$는 자신이 포함하는 행렬 성분의 위치들로 결정된다. 즉, $$H$$는 대각선 전체($$\mathfrak{h}\subseteq\mathfrak{b}\subseteq H$$)와 자신이 포함하는 elementary matrix $$E_{jk}$$들의 span이다. 이제 구체적으로 어느 성분들이 $$H$$에 들어올 수 있는지 보기 위해 upper triangular 방향과의 bracket을 계산하면, $$l\leq j$$와 $$k\leq m$$에 대하여

$$[E_{lj},E_{jk}]=E_{lk}-\delta_{kl}E_{jj},\qquad[E_{jk},E_{km}]=E_{jm}-\delta_{jm}E_{kk}$$

인데 $$\delta$$ 항들은 어차피 $$\mathfrak{h}\subseteq H$$ 안이므로, $$H$$가 자리 $$(j,k)$$를 포함하면 같은 열의 위쪽 자리 $$(l,k)$$ ($$l\leq j$$) 전부와 같은 행의 오른쪽 자리 $$(j,m)$$ ($$m\geq k$$) 전부도 포함해야 한다. 곧 각 열은 위에서부터 빈틈없이 채워지고, 채워진 깊이는 오른쪽 열로 갈수록 줄지 않는다. 따라서 $$k$$번째 열의 깊이를 $$h(k)$$라 적으면, $$H$$는 $$h(i)\geq i$$를 만족하는 단조증가함수 $$h\colon\{1,\ldots,n\}\to\{1,\ldots,n\}$$ (*Hessenberg 함수<sub>Hessenberg function</sub>*)가 결정하는 staircase

$$H_h=\{\,Y\in\mathfrak{gl}_n\;\mid\;YE_i\subseteq E_{h(i)}\ \forall i\,\}=\{\,Y\;\mid\;Y_{jk}=0\ \text{whenever $j>h(k)$}\,\}$$

이며, 그 역도 쉽게 확인할 수 있다. 예컨대 $$n=4$$에서 두 staircase

$$\mathfrak{b}=H_{(1,2,3,4)}=\begin{pmatrix}\ast&\ast&\ast&\ast\\0&\ast&\ast&\ast\\0&0&\ast&\ast\\0&0&0&\ast\end{pmatrix},\qquad H_{(2,3,4,4)}=\begin{pmatrix}\ast&\ast&\ast&\ast\\\ast&\ast&\ast&\ast\\0&\ast&\ast&\ast\\0&0&\ast&\ast\end{pmatrix}$$

는 각각 $$h(i)=i$$와 $$h(i)=\min(i+1,n)$$의 경우이다.

이제 다시 flag variety의 언어로 돌아와서 coset $$gB$$에 대응하는 flag를 $$V_\bullet=g\cdot E_\bullet$$ (즉 $$V_i=\span\{ge_1,\ldots,ge_i\}$$)라 하면, 임의의 $$X\in\mathfrak{gl}_n$$에 대하여

$$\Ad(g^{-1})X\in H_h\iff g^{-1}Xg\in H_h\iff XgE_i\subseteq gE_{h(i)}\iff XV_i\subseteq V_{h(i)}$$

이 성립한다. 곧 type $$A$$의 Hessenberg variety는 $$X$$가 flag를 단계마다 $$h$$가 허용하는 만큼만 흘러내리게 한다는 조건으로 잘라낸 flag들의 variety이다.

</div>

[예시 7](#ex7)의 그림은 일반적인 경우에서도 그대로 성립한다. 이 경우, 위에서처럼 staircase가 $$\mathfrak{b}$$ 위로 더 채우는 자리들은 대각선 아래쪽, 곧 *negative* root 방향이다. 실제로 $$\mathfrak{b}=\mathfrak{h}\oplus\bigoplus_{\alpha>0}\mathfrak{g}_\alpha$$는 이미 모든 positive root 방향을 포함하므로, $$H$$를 $$\mathfrak{b}$$보다 키우는 일은 negative root 방향을 더하는 일일 수밖에 없다. 그러나, $$\ad(\mathfrak{b})$$-stability에 의하여 추가로 simple 조건이 강제되는데, 실제로 simple이 아닌 positive root $$\alpha=\beta+\gamma$$의 방향은 $$[\mathfrak{g}_\beta,\mathfrak{g}_{-\alpha}]=\mathfrak{g}_{-\gamma}$$를 통해 더 얕은 자리들을 함께 끌고 들어오는 반면, negative simple root 방향은 $$\mathfrak{b}\oplus\mathfrak{g}_{-\alpha_i}$$가 그 자체로 stable하다. 즉, $$\mathfrak{b}$$에서 한 칸씩 늘리는 최소 단위의 확장은 정확히 $$\mathfrak{g}_{-\alpha_i}$$들이고, type $$A$$에서는 위 그림의 subdiagonal 자리들이 이들이다. 그럼 $$\mathfrak{b}$$에 이 방향을 추가하여 만들어진 것이 Peterson variety의 $$H$$이다.

<div class="definition" markdown="1">

<ins id="def8">**정의 8**</ins> *Peterson variety* $$\mathcal{Y}$$는 $$G/B$$의 closed subvariety

$$\mathcal{Y}=\{\,gB\in G/B\;\mid\;\Ad(g^{-1})e\in H\,\}$$

로 정의된다. 여기서 $$e=\sum_i e_i$$는 regular nilpotent element이고, $$H=\mathfrak{b}\oplus\bigoplus_i\mathbb{C}f_i$$이며 $$f_i\in\mathfrak{g}_{-\alpha_i}$$는 simple negative root의 root vector이다.

</div>

이 정의는 여러 선택에 의존하는 것처럼 보이지만 사실상 유일하다. $$f_i$$의 선택은 $$\mathbb{C}f_i=\mathfrak{g}_{-\alpha_i}$$가 $$1$$차원이므로 $$H$$를 바꾸지 않고, $$e$$를 다른 regular nilpotent로 바꾸는 것은 ([정의 5](#def5) 직후 논의의 conjugacy에 의해) $$\mathcal{Y}$$를 $$G/B$$ 안에서 translate할 뿐이기 따문이다.

위에서 살펴봤듯, $$H$$가 $$\mathfrak{b}$$에 더한 자유도는 simple root마다 하나씩, 총 $$\rank(\mathfrak{g})$$개이다. $$H=\mathfrak{b}$$가 한 점을 주었으므로 ([정의 6](#def6) 직후의 논의), Peterson variety의 차원은 한 점에서 그만큼 자라리라 기대할 수 있다. 실제로 그렇게 된다는 것이 다음 명제의 내용이다.

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9 (Tymoczko [Tym], Precup [Pre], Insko–Tymoczko [IT])**</ins> Peterson variety $$\mathcal{Y}$$는 Bruhat 분해와의 교집합으로 affine paving 구조를 이룬다. 즉, 각각의 $$\mathcal{Y}\cap BwB/B$$들이 각각 affine space와 isomorphic하며, $$\mathcal{Y}$$는 이들의 disjoint union이다. 특히, 이 구조 하에서 가장 큰 조각의 차원이 $$\rank(\mathfrak{g})$$가 되어 $$\mathcal{Y}$$의 차원 또한 $$\rank (\mathfrak{g})$$와 같다.

</div>

이 명제의 증명은 생략하지만, 주장하는 affine paving 구조 자체는 기억할 필요가 있다. 핵심은 이 affine paving이 simple root들의 부분집합 $$\mathcal{P}(\Delta)$$로 index된다는 것으로, 가령 어떤 simple root 방향도 포함하지 않는 부분집합, 즉 공집합의 경우 $$\mathfrak{b}$$에 더해지는 방향이 없으므로 [정의 6](#def6) 이후의 논증에 의하여 이에 해당하는 affine space는 한 점이 된다. 그 위의 affine space들은 $$\Delta$$의 부분집합에 의해 결정되는 것들로, 이는 단순한 analogy가 아니라 이들의 위치관계 또한 실제로 $$\Delta$$의 부분집합이 결정한다. 

정확히 말해, $$A\subseteq\Delta$$에 대응하는 조각은 $$A$$에 해당하는 simple root들이 정의하는 reflection들로 생성되는 Weyl group의 subgroup $$W_A$$에 대하여, $$W_A$$의 longest element $$w_A$$가 정의하는 Bruhat cell과의 교집합

$$\mathcal{Y}\cap Bw_AB/B\cong \mathbb{A}^{\lvert A\rvert}$$

으로, $$H$$가 $$\mathfrak{b}$$에 더한 자유도들 가운데 정확히 $$A$$ 방향의 것들만 활성화되는 조각이다. 뿐만 아니라, 이 index 아래에서 각 조각들의 closure 관계는 $$\Delta$$의 부분집합들이 이루는 Boolean lattice를 그대로 복제한다. 즉

$$\overline{\mathcal{Y}\cap Bw_AB/B}\;=\;\bigsqcup_{A'\subseteq A}\bigl(\mathcal{Y}\cap Bw_{A'}B/B\bigr)$$

이 성립한다. 실제로 이 closure는 $$H$$를 $$A$$ 방향으로만 키운 중간 단계의 Hessenberg variety $$\mathcal{B}(e,\,\mathfrak{b}\oplus\bigoplus_{i\in A}\mathbb{C}f_i)$$와 일치하며, 나아가 $$A$$가 생성하는 Levi subgroup의 Peterson variety와 동형이다 ([IT]). 즉, Peterson variety는 더 작은 Peterson variety들이 부분집합 순서로 포개진 구조를 가지며, 자유도를 하나도 쓰지 않는 한 점 $$B/B$$ ($$A=\emptyset$$)에서 big Bruhat cell과의 교집합인 가장 큰 조각 ($$A=\Delta$$)까지 그 사이의 모든 위치관계를 simple root들의 조합론이 지배한다. 

<div class="example" markdown="1">

<ins id="ex10">**예시 10**</ins> 이 구조를 앞서 살펴본 type $$A$$에서 예시로 살펴보자. [예시 7](#ex7)과 마찬가지로 Hessenberg function을 $$h(i)=\min(i+1, n)$$으로 택하면, $$H$$는 대각선 아래로 정확히 한 칸씩을 내리는 것이 허용되는 행렬들의 모임이며, 이 예시의 마지막 동치관계에서 우리는 Peterson variety가 complete flag variety $$\Fl_n=\GL_n(\mathbb{C})/B$$ 안에서

$$\Pet_n=\{\,V_\bullet\mid NV_i\subseteq V_{i+1},\ i=1,\ldots,n-1\,\}$$

로 주어진다는 것을 안다. 그 차원은 

$$\sum_{j=1}^n\bigl(h(j)-j\bigr)=n-1$$

이며, 이는 $$\rank(\mathfrak{sl}_n)$$와 같으므로 [명제 9](#prop9)를 다시 확인할 수 있다.

이제 각각의 cell을 보기 위해 더 구체적으로 $$n=3$$인 경우를 보자. $$Ne_1=0$$, $$Ne_2=e_1$$, $$Ne_3=e_2$$이고 마지막 조건 $$NV_2\subseteq V_3=\mathbb{C}^3$$은 자동이므로 위의 정의를 그대로 사용하면

$$\Pet_3=\{(V_1\subset V_2)\in \Fl_3\mid NV_1\subseteq V_2\}$$

이다. 그럼 위에서 살펴봤듯, $$\dim_\mathbb{C}\Fl_3=3$$에서 조건 하나가 차원을 $$1$$ 깎아 $$\dim\Pet_3=2$$가 된다. 그럼 Peterson variety의 차원과 $$\rank(\mathfrak{g})$$가 같으므로, 위의 설명에 따르면 Peterson variety $$\Pet_3$$은 $$2^2=4$$개의 조각으로 나뉘어야 한다. 한편 $$\GL_3$$의 Bruhat decomposition을 생각하면, Bruhat cell은 $$w\in S_3$$에 의해 index되는 $$6$$개이다. 즉 $$6$$개의 cell들 가운데 Peterson variety의 affine paving을 정의하지 않는 것이 두 개 있는데, 이들을 identify하기 위해 coordinate flag 

$$E^w_\bullet:\qquad 0\subset \span\{e_{w(1)}\}\subset \span \{e_{w(1)}, e_{w(2)}\}\subset \span\{e_{w(1)}, e_{w(2)},e_{w(3)}\}=\mathbb{C}^3$$

를 생각하면 이것이 $$\Pet_3$$과 속하기 위해서는 $$Ne_{w(1)}\in\span\{e_{w(1)},e_{w(2)}\}$$, 즉

$$w\in\{e,\,s_1,\,s_2,\,w_0\}=\{123,\,213,\,132,\,321\}$$

의 네 개만이 남는 것을 확인할 수 있다. 실제로, 빠진 두 원소 $$231, 312$$에 해당하는 Bruhat cell의 점들을 직접 적어준 후 $$\Pet_3$$과의 교집합을 생각하면 이것이 공집합임을 쉽게 확인할 수 있다. 

위에서 구한 네 개의 flag들은 simple root 부분집합 $$A\subseteq\{\alpha_1,\alpha_2\}$$와, 이들이 정의하는 Weyl group $$W_A$$의 maximal length element $$w_A$$를 대응시킨 $$2^{n-1}=4$$개의 coordinate flag로, Peterson variety가 simple root들의 조합론을 기억하고 있음을 보여준다.

</div>

한편 [명제 9](#prop9)의 핵심적인 아이디어는 $$G/B$$의 Bruhat decomposition과 $$\mathcal{Y}$$의 교집합을 취하여 $$\mathcal{Y}$$를 분해하는 것이었다. 그런데 우리는 이미 [§Bruhat decomposition, ⁋정리 8](/ko/math/lie_theory/bruhat_decomposition#thm8)에서 opposite Borel subgroup을 통한 decomposition을 살펴보았으므로 $$\mathcal{Y}\cap B^-wB/B$$를 통해 $$\mathcal{Y}$$의 성질을 탐구할 수도 있다. 

결과의 성격은 전혀 다르다. 조각들이 더 이상 affine space가 아닌 대신, 각 조각이 그 자체로 의미를 갖는 affine variety가 된다. 이번에도 비어있지 않은 조각은 정확히 $$2^{\rank(\mathfrak{g})}$$개인데, 그 index마저 paving과 같다. 즉, 비어있지 않은 조각은 각 $$A\subseteq\Delta$$마다 같은 longest element $$w_A$$의 $$B^-$$쪽 Bruhat cell과의 교집합

$$\mathcal{Y}\cap B^-w_AB/B$$

로 주어지는 locally closed subvariety들이다 [Pet]. 이 때 부분집합 $$A\subseteq\Delta$$는 $$W_A$$를 Weyl group으로 갖는 standard parabolic subgroup $$B\subseteq P\subseteq G$$와 일대일대응하므로, 우리는 (곧 살펴볼 이유로) 이 조각을 $$\mathcal{Y}_P$$로 적어서 $$\mathcal{Y}$$의 stratification

$$\mathcal{Y}=\bigsqcup_{P\supseteq B}\mathcal{Y}_P$$

을 얻는다. 양 극단을 보면 $$P=G$$ ($$A=\Delta$$, $$w_A=w_0$$)의 stratum은 한 점 $$\{w_0B\}$$이고, $$P=B$$ ($$A=\emptyset$$, $$w_A=e$$)의 stratum은 opposite big cell과의 교집합

$$\mathcal{Y}_B=\mathcal{Y}\cap B^-B/B$$

으로 주어지는 $$\mathcal{Y}$$의 Zariski dense open subset이다. 일반적으로 $$\mathcal{Y}_P$$의 차원은 $$\lvert\Delta\setminus A\rvert$$, 곧 $$P$$에 들어있지 않은 simple root의 개수와 같다. 즉 paving의 cell과 stratification의 stratum은 같은 $$w_A$$에 매달린 두 조각으로, 개수가 같고 둘 다 점 $$w_AB$$를 담으면서 차원은 $$\lvert A\rvert$$와 $$\lvert\Delta\setminus A\rvert$$로 서로 보완적인 방향으로 자란다.

이 분해가 단순히 $$B$$를 $$B^-$$으로 바꾼 것 이상의 의미를 갖는 이유는 이것이 quantum cohomology에 대한 정보를 담고 있기 때문이다. 다음 정리에서, Lie gruop $$G$$의 *Langlands dual group<sub>랭글랜즈 쌍대군</sub>* $$G^\vee$$는 root datum에서 root와 coroot를 맞바꾼 dual group으로, 이 상황에서 [정의 8](#def8)을 따라 만든 Peterson variety가 $$\mathcal{Y}^\vee$$이고, $$G$$의 parabolic subgroup $$P$$의 Langlands dual $$P^\vee$$에 해당하는 $$\mathcal{Y}^\vee$$의 stratum을 $$\mathcal{Y}^\vee_P$$으로 쓰자.

<div class="proposition" markdown="1">

<ins id="thm11">**정리 11 (Peterson)**</ins> $$G$$의 Langlands dual $$G^\vee$$의 Peterson variety에서, 각 standard parabolic subgroup $$P\supseteq B$$에 대응하는 stratum $$\mathcal{Y}^\vee_P$$의 coordinate ring은 partial flag variety $$G/P$$의 small quantum cohomology ring과 동형이다.

$$\mathbb{C}[\mathcal{Y}^\vee_P]\cong QH^\ast(G/P)$$

</div>

이 정리는 Peterson의 1997년 MIT lecture에서 소개된 것으로, 별도의 출판본은 없지만 [강의노트](https://math.soimeme.org/~arunram/Resources/PetersonGmodBcourse1997.pdf) 등에서 그 증명을 찾아볼 수 있다. 다만 우리가 주로 살펴보던 Grassmannian의 경우, $$\GL_n$$은 Langlands self-dual이므로 $$G\cong G^\vee$$가 되어 이 duality가 잘 보이지는 않는다. 

우리는 [§Borel subgroup, ⁋정의 12](/ko/math/lie_theory/borel_subgroup#def12)에서 flag variety를 도입한 후, 지금까지 대수기하의 언어를 아주 본격적으로 사용하지는 않았지만, 이 정리의 정신을 이해하기 위해서는 이를 더 이상 미룰 수 없다. 핵심적인 것은 대수기하학에서 ring $$A$$를 그 자체로 $$\mathbb{C}$$ 위의 기하적인 공간 $$\Spec A$$으로, $$A$$는 그 공간 위의 함수들의 ring으로 해석하는 방식이다. 이 사전에서, 공간 $$\Spec A$$의 각 점들은 $$A$$의 maximal ideal에 대응되며, ring homomorphism $$A\rightarrow B$$는 기하적인 함수 $$\Spec B\rightarrow \Spec A$$에 대응된다. 중요한 특수한 케이스는 $$A=\mathbb{C}$$와 $$B=\mathbb{C}$$일 때 각각으로, 우선 $$A=\mathbb{C}$$이면 대수적인 세계에서의 $$\mathbb{C}\rightarrow B$$는 ring $$B$$를 $$\mathbb{C}$$-algebra로 보게 하는 structure morphism이다. 이에 대응되는 기하적인 세상에서는 $$\Spec \mathbb{C}$$는 한 점이므로, 함수 $$\Spec B\rightarrow \Spec A$$는 한 점으로의 함수가 된다. 만일 $$A,B$$가 모두 $$\mathbb{C}$$-algebra가 되어 다음의 commutative diagram

![$$A, B$$가 $$\mathbb{C}$$-algebra이면 unit이 주는 structure morphism $$\mathbb{C}\to A$$, $$\mathbb{C}\to B$$가 있고, ring homomorphism $$\varphi\colon A\to B$$가 이 둘과 commute하는 것(곧 $$\mathbb{C}$$를 고정하는 것)이 $$\varphi$$가 $$\mathbb{C}$$-algebra homomorphism이라는 조건이다.](/assets/images/Math/Lie_Theory/Richardson_Peterson_Variety-1.svg){:style="width:12em" class="invert" .align-center}

이 존재한다면, $$\mathbb{C}$$-algebra homomorphism $$A\rightarrow B$$는 이제 다음의 commutative diagram

![위 삼각형에 $$\operatorname{Spec}$$을 먹이면 화살표가 모두 뒤집혀, $$\operatorname{Spec}\varphi\colon\operatorname{Spec}B\to\operatorname{Spec}A$$가 한 점 $$\operatorname{Spec}\mathbb{C}$$ 위에서의 morphism이 된다.](/assets/images/Math/Lie_Theory/Richardson_Peterson_Variety-2.svg){:style="width:18em" class="invert" .align-center}

으로 번역된다. 한편 $$B=\mathbb{C}$$인 경우 ring homomorphism $$A\rightarrow \mathbb{C}$$는 기하적인 세계에서는 $$\Spec \mathbb{C}\rightarrow\Spec A$$로 번역되며, 즉 이 ring homomorphism은 그 자체로 하나의 점이 된다. 만일 $$A$$가 $$\mathbb{C}$$-algebra인 경우, 이 ring homomorphism을 우리는 보통 evaluation map으로 해석했던 것 또한 기억하자. 마지막으로, ring homomorphism $$A\rightarrow B$$로 $$B$$를 $$A$$-algebra로 보는 것은 위에서 보았듯 morphism $$\Spec B\rightarrow\Spec A$$, 곧 base $$\Spec A$$ 위에 놓인 상대적인 공간으로 해석되며, $$A$$-module은 $$\Spec A$$ 위의 sheaf(벡터다발에 준하는 대상)로 본다. 특히 rank $$N$$짜리 free module은 trivial rank $$N$$ bundle에 해당하여, 그런 $$A$$-algebra의 $$\Spec$$은 base로 보내는 fiber가 ($$\dim$$을 세면) $$N$$개인 finite morphism이 된다. 가장 기본적인 경우가 affine space로, polynomial algebra $$\mathbb{C}[\x_1,\ldots,\x_n]$$은 $$\Spec$$을 먹이면 affine $$n$$-space $$\mathbb{A}^n$$이며, 더 일반적으로 $$A[\x_1,\ldots,\x_n]$$은 base $$\Spec A$$ 위의 relative affine space에 대응한다.

이제 다시 [정리 11](#thm11)의 해석으로 돌아가기 위해 우선 $$QH^\ast(G/P)$$에 기하학적인 설정을 추가하자. 표기의 편의를 위해 $$k$$개의 quantum parameter들이 있다고 하고, 이들 family를 간단히 $$q$$라 적으면 $$QH^\ast(G/P)$$는 (module로서는) quantum parameter들의 polynomial ring $$\mathbb{C}[q]$$ 위의 rank $$N=\dim_\mathbb{C}H^\ast(G/P)$$ free module이다. 이제 structure morphism $$\mathbb{C}[q]\rightarrow QH^\ast(G/P)$$를 생각하면, 기하적으로 이는 $$\Spec QH^\ast(G/P)\rightarrow \Spec\mathbb{C}[q]$$를 정의한다. 그럼 위에서 살펴본 것과 같이 이는 $$\Spec QH^\ast(G/P)$$에서 $$\mathbb{A}^k$$로의 rank $$N$$ finite morphism이다. 

그럼 $$\Spec \mathbb{C}[q]\cong\mathbb{A}^k$$에서의 임의의 generic point $$q_0$$에서의 fiber를 생각하는 것은 다음의 diagram

![$$q=q_0$$에서의 fiber에 대응하는 commutative square. 점 $$y$$의 character $$\rchi_y$$를 $$\mathbb{C}[q]$$로 제한하면 $$q_0$$에서의 evaluation $$\operatorname{ev}_{q_0}$$가 되어, $$y$$가 $$q_0$$ 위에 놓여 있음을 뜻한다.](/assets/images/Math/Lie_Theory/Richardson_Peterson_Variety-3.svg){:style="width:14em" class="invert" .align-center}

과 정확하게 같다. 대수적으로 이는 다음의 텐서곱

$$QH^\ast(G/P)\otimes_{\mathbb{C}[q]}\mathbb{C}[q]/(q-q_0)\cong QH^\ast(G/P)/(q-q_0)$$

이며, 이 때 fiber의 한 점은 다시 ring homomorphism $$QH^\ast(G/P)/(q-q_0)\rightarrow \mathbb{C}$$이 된다. 비슷하게, [정리 11](#thm11)의 isomorphism을 적용하면 다음의 commutative diagram

![Peterson 동형이 quantum cohomology의 spectrum을 flag로 실현하는 그림. $$\mathcal{Y}^\vee_P$$의 한 점 $$y$$ (곧 $$G^\vee/B^\vee$$의 flag) 가 주는 evaluation $$\operatorname{ev}_y$$는 Peterson 동형 $$\Phi\colon a\mapsto f_a$$를 통해 character $$\rchi_y=\operatorname{ev}_y\circ\Phi$$ (오른쪽 사각형, $$\rchi_y(a)=f_a(y)$$) 로 끌어올려지고, $$\mathbb{C}[q]$$로 제한하면 $$y$$의 quantum parameter 값 $$q_0$$에서의 evaluation이 된다 (왼쪽 사각형). 곧 $$q_0$$ 위의 fiber 점 $$=$$ $$q_0$$ 위의 character $$=$$ flag.](/assets/images/Math/Lie_Theory/Richardson_Peterson_Variety-4.svg){:style="width:24em" class="invert" .align-center}

을 생각할 수 있으며, 이 때 마지막 수직방향 $$\ev_y$$가 $$\mathcal{Y}^\vee_P$$ 위의 한 점을 정의하게 된다. 이제 이 점이 무엇을 담고 있는지를 사전을 따라 풀어 보자. 우선 $$QH^\ast(G/P)/(q-q_0)$$은 $$\mathbb{C}$$ 위의 finite-dimensional algebra이고, 그 위에서 각 cohomology class $$a$$는 quantum product로 곱하는 연산자 $$a\qtimes-$$를 준다. 위에서 얻은 점 $$y$$에 대응하는 character $$\rchi_y\colon QH^\ast(G/P)/(q-q_0)\to\mathbb{C}$$는 각 $$a$$에 스칼라 $$\rchi_y(a)$$를 배정하되, ring homomorphism이므로 $$\rchi_y(a\qtimes b)=\rchi_y(a)\,\rchi_y(b)$$와 $$\rchi_y(1)=1$$을 지킨다. 이는 $$\rchi_y(a)$$가 연산자 $$a\qtimes-$$의 고유값이고, 그 고유값들이 quantum product와 모순 없이 동시에 배정된다는 말과 같다. 곧 fiber의 한 점은 generic $$q_0$$에서 모든 quantum 곱셈 연산자에 동시 고유값 한 벌을 일관되게 주는 방법이다. 

그리고 이 동시 고유값들이 어디에 놓여 있는지를 말해 주는 것이 [정리 11](#thm11)이다. Isomorphism $$\mathbb{C}[\mathcal{Y}^\vee_P]\cong QH^\ast(G/P)$$ 아래에서 각 class $$a$$는 $$\mathcal{Y}^\vee_P$$ 위의 regular function $$f_a$$에 대응하므로, 사전의 언어로 위 character $$\rchi_y$$는 다름 아닌 flag $$y$$에서의 evaluation $$\rchi_y=\ev_y$$이고, 따라서 $$\rchi_y(a)=f_a(y)$$이다. 즉 동시 고유값 $$\rchi_y(a)$$는 추상적으로 떠 있는 수가 아니라, $$G^\vee/B^\vee$$ 안의 구체적인 flag $$y$$에서 좌표함수 $$f_a$$의 값을 읽은 것이다. 이렇게 추상적인 대수 $$QH^\ast(G/P)$$의 spectrum $$\Spec QH^\ast(G/P)=\mathcal{Y}^\vee_P$$이 flag variety $$G^\vee/B^\vee$$ 안에 실제 점들로 앉고, 그 점(곧 flag) 하나하나가 quantum 곱셈의 동시 고유값 한 벌을 손에 쥐어 준다. 

가장 작은 Grassmannian $$\mathbb{P}^1=\Gr(1,2)$$에서는 이 전부를 손으로 볼 수 있다. $$n=2$$에서는 Peterson 조건 $$NV_1\subseteq V_2=\mathbb{C}^2$$이 공허하여 $$\mathcal{Y}=\Fl_2=\mathbb{P}^1$$ 전체이고, stratum $$\mathcal{Y}_B$$는 opposite big cell과의 교집합 $$\mathbb{P}^1\setminus\{w_0B\}\cong\mathbb{A}^1$$이다. 한편 $$QH^\ast(\mathbb{P}^1)=\mathbb{C}[\sigma,q]/(\sigma^2-q)\cong\mathbb{C}[\sigma]$$ 역시 한 변수 다항식환이라 정리의 동형과 부합하고, 이 동형 아래에서 quantum parameter는 affine 좌표의 제곱 $$q=\sigma^2$$으로 실현된다. generic $$q_0$$의 fiber는 $$\sigma=\pm\sqrt{q_0}$$의 두 점, 곧 $$\binom{2}{1}=2$$개이고, $$q_0=0$$의 fiber는 한 점 $$B/B$$ 위에 길이 $$2$$로 앉은 double point로서 그 좌표환이 classical cohomology $$\mathbb{C}[\sigma]/(\sigma^2)=H^\ast(\mathbb{P}^1)$$이다. 곧 quantum에서 classical로의 퇴화까지 stratum 안에서 기하적으로 일어난다.

일반적인 $$\Gr(k,n)$$에서도 마찬가지로 generic $$q_0$$의 fiber는 $$\binom{n}{k}$$개의 서로 다른 점으로 이루어진다. 이 유한 개의 점들은 또 하나의 명시적인 모델을 갖는데, 이들이 어떤 Laurent 다항식, 곧 superpotential의 critical point들로 실현된다는 것이 mirror symmetry의 내용 중 하나이며, 일반적인 $$G/P$$에 대해 이 대응을 구성하는 것은 현재도 활발히 연구되는 주제다 ([거울대칭](/ko/mirror_symmetry/) 참조).

<div class="remark" markdown="1">

<ins id="rmk12">**참고 12**</ins> [명제 9](#prop9)의 affine paving은 cohomology 계산의 출발점이기도 하다. Paving에 의해 $$\mathcal{Y}$$의 cohomology는 cell들로 색인된 basis를 갖는 free module이고 홀수 차수에서 사라진다. 즉 [§Bruhat decomposition, ⁋명제 17](/ko/math/lie_theory/bruhat_decomposition#prop17)에서 본 flag variety의 affine paving 논법이 Peterson variety에도 그대로 작동하며, Insko–Tymoczko [IT]는 이를 바탕으로 Peterson variety의 intersection theory를 전개하였다.

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

**[LS]** T. Lam, M. Shimozono, *Quantum cohomology of $$G/P$$ and homology of affine Grassmannian*, Acta Math. **204** (2010), 49--90.

**[Pet]** D. Peterson, Lecture notes, Massachusetts Institute of Technology, Spring 1997 (unpublished).

**[Tym]** J. S. Tymoczko, *Paving Hessenberg varieties by affines*, Selecta Math. (N.S.) **13** (2007), 353--367.

**[Pre]** M. Precup, *Affine pavings of Hessenberg varieties for semisimple groups*, Selecta Math. (N.S.) **19** (2013), 903--922.

**[IT]** E. Insko, J. Tymoczko, *Affine pavings of regular nilpotent Hessenberg varieties and intersection theory of the Peterson variety*, J. Combin. Theory Ser. A **187** (2022), 105572.

---
[^1]: Cartan subalgebra를 나타내는 $$\mathfrak{h}$$는 [§근계, ⁋정의 4](/ko/math/lie_theory/root_systems#def4)에서부터 오는 것으로, 우리 논의에서의 $$H$$와는 <em-ko>무관한</em-ko> 것임을 유의하자. 