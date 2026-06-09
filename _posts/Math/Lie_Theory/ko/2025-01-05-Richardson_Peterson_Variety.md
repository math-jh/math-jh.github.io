---
title: "Richardson variety와 Peterson variety"
description: "Schubert variety와 opposite Schubert variety의 intersection으로 정의되는 Richardson variety와 regular nilpotent element가 잘라내는 Peterson variety를 함께 다룬다. 두 부분다양체의 정의·차원, intersection theory에서의 역할, Grassmannian과 type A에서의 구체적 모습, 그리고 Bruhat cell에 의한 stratification을 살펴본다."
excerpt: "두 opposite Schubert variety의 transversal한 intersection인 Richardson variety와 regular nilpotent의 Peterson variety: 정의·차원·intersection theory·stratification"

categories: [Math / Lie Theory]
permalink: /ko/math/lie_theory/richardson_peterson_variety
sidebar:
    nav: "Lie_theory-ko"

date: 2025-01-05
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

정의에 의해 $$R_{u,w}$$는 $$G/P$$의 closed subvariety이고, $$\mathring{R}_{u,w}$$는 그 안의 Zariski open subset이다.

이 정의의 유용성은 Grassmannian $$\Gr(k,n)$$ (또는 일반적인 partial flag variety)에서 볼 수 있다. reference flag $$E_\bullet\colon E_1\subset E_2\subset\cdots\subset E_n=\mathbb{C}^n$$를 하나 고정하면, 각 Schubert cell은 그 안의 $$k$$차원 subspace $$V$$가 이 flag와 만나는 방식, 곧 $$\dim(V\cap E_j)$$가 $$j$$를 키울 때 어느 자리에서 뛰는지로 결정되었던 것을 기억하자. Grassmannian 안에서 두 Schubert cell의 intersection을 계산하는 것은 이들이 동시에 만족하는 incidence condition을 찾는 것이다. 그러나 두 Schubert cell을 같은 reference flag에 대해 정의하면 두 조건이 서로 독립이 아니어서 intersection이 기대 차원에서 어긋나므로, reference flag들을 서로 generic position에 있는 것으로 택해야 한다.

이것이 가장 쉽게 계산되는 예가 바로 주어진 flag $$E_i=\span\{e_1,\ldots,e_i\}$$를 거꾸로 읽는 *opposite flag* $$\tilde{E}_j=\span\{e_n,\ldots,e_{n-j+1}\}$$이다. 이렇게 잡은 두 flag는 모든 $$i,j$$에 대해 transversality condition

$$\dim(E_i\cap\tilde{E}_j)=\max(0,\,i+j-n)$$

을 만족한다. 곧 두 flag의 어느 piece 쌍을 잡아도 그 intersection이 가능한 한 작게 만난다는 뜻이다. Richardson variety는 바로 이렇게 generic position에 놓인 두 reference flag에 대한 Schubert 조건을 동시에 부과해 두 Schubert cell의 intersection을 보는 것으로, 정의에서 $$X_w$$가 $$B$$가 고정하는 표준 flag에 대한 조건, $$X^u$$가 $$B^-$$가 고정하는 opposite flag에 대한 조건이라는 사실이 바로 이 transversality에 해당한다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> Open Richardson variety $$\mathring{R}_{u,w}$$가 비어있지 않을 필요충분조건은 Bruhat order에서 $$u\leq w$$인 것이다. 이 조건이 성립하면 $$\mathring{R}_{u,w}$$는 차원 $$\ell(w)-\ell(u)$$의 irreducible affine variety이다.

</div>

직관적으로, Bruhat cell $$X_w$$는 낮은 차원에서부터 커지는 방향이고, opposite Bruhat cell $$X^u$$는 큰 차원에서부터 내려가는 방향인 것을 기억하자. 구체적으로 $$\dim X_w=\ell(w)$$이고 $$\dim X^u=\dim (G/P)-\ell(u)$$가 성립한다. 따라서 이들 opposite Bruhat cell이 nontrivial하게 만나기 위해서는 적어도 이들 두 variety의 차원의 합이 $$\dim(G/P)$$보다 커야한다. 이 때 교집합의 기대차원이 명제의

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

[명제 2](#prop2)의 증명에서 본 것처럼 $$X_w$$와 $$X^u$$는 $$B$$와 $$B^-$$가 주는 generic position에서 transversal하게 만나므로, 그 intersection class는 두 class의 곱과 같다. 이것이 $$[X_w]\cdot[X^u]=[R_{u,w}]$$이다 (Kleiman generic transversality, [Bri] 참조). $$\ell(u)=\ell(w)$$인 경우 $$R_{u,w}$$의 차원은 $$\ell(w)-\ell(u)=0$$이고, [명제 2](#prop2)에 의해 $$u=w$$이면 reduced point 하나, $$u\neq w$$이면 ($$u\leq w$$가 깨져) 공집합이다. 따라서 그 0차원 class의 차수, 곧 $$\int_{G/P}[X_w]\cdot[X^u]$$은 $$\delta_{u,w}$$이다.

</details>

명제 [명제 3](#prop3)은 Schubert basis의 곱셈 structure constant를 Richardson variety의 차수로 환원한다. 세 class의 곱 $$[X_w]\cdot[X^u]\cdot[X_v]$$을 적분하면 세 generic position Schubert variety의 intersection number가 나오는데, 이것이 곧 structure constant이고, Grassmannian의 경우에는 Littlewood–Richardson 계수가 되며, 이로부터 classical Schubert calculus가 전개된다.

역시 가장 손에 잡히는 경우는 $$G/P=\Gr(k,n)\cong\GL_n(\mathbb{C})/P_k$$인 Grassmannian이다. 이때 $$W=S_n$$, $$W_{P_k}=S_k\times S_{n-k}$$이고, minimal length coset representative $$W^{P_k}$$은 [§Bruhat decomposition, ⁋명제 14](/ko/math/lie_theory/bruhat_decomposition#prop14)에서 본 $$(k,n-k)$$-shuffle들이다. Schubert variety $$X_w$$는 표준 flag $$E_\bullet$$에 대한 $$\dim(V\cap E_{w(a)})\geq a$$ 꼴의 rank 조건으로, opposite Schubert variety $$X^u$$는 opposite flag $$\tilde{E}_\bullet$$ ($$\tilde{E}_j=\span\{e_n,\ldots,e_{n-j+1}\}$$)에 대한 대칭적 rank 조건으로 잘린다. Richardson variety는 이 두 조건을 동시에 부과한 것이다.

<div class="example" markdown="1">

<ins id="ex4">**예시 4**</ins> $$\Gr(2,4)$$에서 $$u=1324$$, $$w=2413$$을 택하자. [§Bruhat decomposition, ⁋예시 18](/ko/math/lie_theory/bruhat_decomposition#ex18)의 jump set 순서로 $$1324\leftrightarrow\{1,3\}$$, $$2413\leftrightarrow\{2,4\}$$이고 성분별로 $$1\leq2$$, $$3\leq4$$이므로 $$u\leq w$$이며, $$\ell(2413)-\ell(1324)=3-1=2$$이다. 두 Schubert 조건은 각각

$$X_{2413}=\{V\mid\dim(V\cap E_2)\geq1\},\qquad X^{1324}=\{V\mid\dim(V\cap\tilde{E}_2)\geq1\}$$

로, $$E_2=\span\{e_1,e_2\}$$와 $$\tilde{E}_2=\span\{e_3,e_4\}$$은 서로 complementary한 두 평면이다. 따라서

$$R_{1324,2413}=\{V\in\Gr(2,4)\mid V\cap E_2\neq0,\ V\cap\tilde{E}_2\neq0\}$$

은 $$E_2$$ 안의 한 line과 $$\tilde{E}_2$$ 안의 한 line을 골라 span한 평면들의 모임이다. $$E_2\cap\tilde{E}_2=0$$이므로 두 line은 항상 독립이고, 대응 $$([\,p\,],[\,q\,])\mapsto\langle p,q\rangle$$은 isomorphism

$$R_{1324,2413}\cong\mathbb{P}(E_2)\times\mathbb{P}(\tilde{E}_2)\cong\mathbb{P}^1\times\mathbb{P}^1$$

을 준다. 차원 $$2$$의 variety로, 명제 [명제 2](#prop2)의 차원과 정확히 맞는다. 그 open part는 행렬

$$V=\operatorname{rowspan}\begin{pmatrix}1&s&0&0\\0&0&1&t\end{pmatrix}\qquad(s,t)\in\mathbb{A}^2$$

로 좌표화되는데, 위 행렬의 jump set이 $$\{2,4\}$$이므로 $$V\in X_{2413}^\circ$$이고 둘째 행이 $$\tilde{E}_2$$ 안에 있으므로 $$V\in X^{1324}_\circ$$이다. 즉 $$\mathring{R}_{1324,2413}$$은 이 $$(s,t)$$-평면의 open subset으로, affine 차원 $$2$$임이 좌표에서 곧장 드러난다.

</div>

## Peterson variety의 정의

이제 우리의 관점을 다소 바꾸어 새로운 variety를 정의한다. 우리가 살펴보는 flag variety $$G/B$$의 경우, $$G$$는 자기 자신의 Borel subalgebra들 위에 다음의 conjugation action 

$$g\cdot\mathfrak{b}'=\Ad(g)\,\mathfrak{b}'$$

으로 작용한다 ([§Borel subgroup, ⁋명제 10](/ko/math/lie_theory/borel_subgroup#prop10)). 이 때, 임의의 두 Borel subalgebra는 conjugate이므로, 이 action은 transitive하고, $$\mathfrak{b}$$의 stabilizer는 그 normalizer $$N_G(\mathfrak{b})=B$$이다. 따라서 orbit-stabilizer 정리로 얻어지는 $$gB\mapsto\Ad(g)\mathfrak{b}$$가 $$G/B$$와 Borel subalgebra들의 집합 사이의 일대일 대응을 준다.

이제 이 대응 아래 $$\mathfrak{g}$$의 원소 $$X$$를 고정하면, 각 flag $$gB$$마다 $$\mathfrak{g}$$의 원소 $$\Ad(g^{-1})X$$가 결정된다. 그럼 이 원소가 $$\mathfrak{b}$$를 포함하는 $$\operatorname{ad}(\mathfrak{b})$$-stable subspace $$H\subseteq\mathfrak{g}$$에 속하는지를 묻는 조건 $$\Ad(g^{-1})X\in H$$는 $$g$$의 각 entry에 대한 다항식 조건이므로, 이를 만족하는 $$gB$$들의 집합은 $$G/B$$의 closed subvariety를 이룬다. 

$$H$$의 크기에 따라 $$H=\mathfrak{b}$$일 때부터 $$H=\mathfrak{g}$$일 때($$G/B$$ 전체)까지 variety들의 family를 얻으며, 이것이 [정의 8](#def8)에서 정의할 *Hessenberg variety*이다. $$X$$로 regular nilpotent를 택하고 $$H=\mathfrak{b}$$로 두면 조건을 만족하는 flag는 유일하게 존재하므로 variety는 한 점이다 ([명제 7](#prop7)). 여기서 $$H$$를 $$\mathfrak{b}$$ 위에 각 simple root 방향마다 자유도를 하나씩 더한 $$H=\mathfrak{b}\oplus\bigoplus_i\mathbb{C}f_i$$로 바꾸면 $$\dim=\rank(\mathfrak{g})$$인 nontrivial variety를 얻는데, 이것이 Peterson variety이다.

$$\mathfrak{g}=\mathfrak{gl}_n$$에서 이것이 구체적으로 어떤 variety인지 보자. Principal nilpotent $$N=\sum_{i=1}^{n-1}E_{i,i+1}$$에 대해 위 Hessenberg 조건 $$\Ad(g^{-1})N\in H$$는 complete flag $$V_\bullet$$의 언어로

$$\Pet_n=\{\,V_\bullet\mid NV_i\subseteq V_{i+1},\quad i=1,\ldots,n-1\,\}$$

으로 쓸 수 있다. $$n=3$$에서 $$N$$은 $$Ne_1=0$$, $$Ne_2=e_1$$, $$Ne_3=e_2$$이고, 마지막 조건 $$NV_2\subseteq V_3=\mathbb{C}^3$$은 자동이므로 조건은 $$NV_1\subseteq V_2$$ 하나뿐이다. $$V_1=\span\{v\}$$를 택하면 $$v\notin\ker N=\span\{e_1\}$$인 한 $$Nv\neq0$$이고 $$V_2=\span\{v,Nv\}$$로 결정된다. 자유 파라미터는 $$V_1\in\mathbb{P}^2$$뿐이므로 $$\dim\Pet_3=2$$이다.

이를 위해 우선 regular nilpotent을 정확히 정의한다.

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> Nilpotent element $$e\in\mathfrak{g}$$가 *regular*라는 것은 그 centralizer $$\mathfrak{z}_{\mathfrak{g}}(e)=\{X\in\mathfrak{g}\mid[X,e]=0\}$$의 차원이 $$\rank(\mathfrak{g})$$와 같은 것이다.

</div>

각 simple root $$\alpha_i$$마다 $$0\neq e_i\in\mathfrak{g}_{\alpha_i}$$를 골라 $$e=\sum_i e_i$$로 두면 regular nilpotent을 얻는다. type $$A_{n-1}$$의 $$\mathfrak{sl}_n$$에서 이는 superdiagonal이 모두 $$1$$인 principal nilpotent $$N=\sum_{i=1}^{n-1}E_{i,i+1}$$이고, 그 centralizer를 직접 계산하면 $$N$$의 polynomial들

$$\mathfrak{z}_{\mathfrak{sl}_n}(N)=\span\{N,N^2,\ldots,N^{n-1}\}$$

로, abelian이며 차원이 $$n-1=\rank(\mathfrak{sl}_n)$$이다 ($$\mathfrak{gl}_n$$에서라면 항등행렬까지 더해 $$\span\{I,N,\ldots,N^{n-1}\}$$, 차원 $$n$$). 모든 regular nilpotent이 $$G$$의 adjoint action으로 서로 conjugate하다는 것, 그리고 그 centralizer가 언제나 abelian이며 차원이 정확히 $$\rank(\mathfrak{g})$$라는 것은 Kostant [Kos]의 고전적 결과이다. 바로 이 centralizer 차원이 아래 [명제 7](#prop7)에서 Peterson variety의 차원을 결정한다.

위 interpolation 그림을 coadjoint action의 언어로 정밀하게 적으면 다음 정의가 된다.

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> Parabolic subgroup $$P\supseteq B$$에 대응하는 *Peterson variety* $$Y_P^\circ$$는 $$R=G/B^-$$의 부분다양체

$$Y_P^\circ=\{\,gB^-\in R\;\mid\;\Ad^\ast(g^{-1})\cdot F\in[\mathfrak{n}^-,\mathfrak{n}^-]^\perp\,\}$$

로 정의된다. 여기서 $$F=e_1^\ast+e_2^\ast+\cdots+e_{n-1}^\ast\in\mathfrak{g}^\ast$$은 dualize한 positive Chevalley generator들의 합 ($$\mathfrak{g}^\ast$$에서의 regular nilpotent에 해당), $$\Ad^\ast$$은 $$G$$의 coadjoint action, $$\mathfrak{n}^-=[\mathfrak{b}^-,\mathfrak{b}^-]$$는 negative nilpotent subalgebra이고, $$[\mathfrak{n}^-,\mathfrak{n}^-]^\perp\subseteq\mathfrak{g}^\ast$$은 그 derived subalgebra의 annihilator이다.

</div>

$$P=B$$일 때가 Kostant–Peterson의 원래 정의 [Pet]이며, 일반의 $$P$$에 대한 위 형태는 Rietsch [Rie]에서 표준적으로 쓰인다. 정의에서 $$F$$가 regular nilpotent라는 점이 핵심으로, 그 coadjoint stabilizer가 $$\rank(\mathfrak{g})$$차원의 abelian subalgebra라는 Kostant의 정리가 $$Y_P^\circ$$의 차원을 곧장 준다.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> $$P=B$$인 경우, Peterson variety $$Y_B^\circ\subseteq G/B^-$$의 차원은 $$\rank(\mathfrak{g})$$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$F\in\mathfrak{g}^\ast$$을 regular nilpotent로 잡았으므로 Kostant [Kos]의 정리에 의해 그 coadjoint stabilizer $$G_F=\{g\in G\mid\Ad^\ast(g)\cdot F=F\}$$의 connected component는 abelian이고 그 차원은 $$\rank(\mathfrak{g})$$이다. $$G/B^-$$를 $$B^-$$ 위에서의 $$G$$-quotient로 보면, 정의에서 부과한 조건 $$\Ad^\ast(g^{-1})\cdot F\in[\mathfrak{n}^-,\mathfrak{n}^-]^\perp$$은 codimension $$\dim[\mathfrak{n}^-,\mathfrak{n}^-]$$의 affine 조건을 자른다. 두 차원의 차이를 계산하면 정확히 $$\rank(\mathfrak{g})$$가 남는다. 자세한 dimension count는 [Pet], [Rie]를 참조한다.

</details>

이 결과는 $$\rank(\mathfrak{g})$$가 simple root의 개수와 같다는 사실과 맞물린다. type $$A_{n-1}$$에서는 $$\rank(\mathfrak{sl}_n)=n-1$$이므로 Peterson variety의 차원도 $$n-1$$이며, 이는 아래 Hessenberg 기술의 dimension formula와도 일치한다. 더 일반적인 parabolic $$P$$에 대해서도 비슷한 공식이 성립하여, $$\dim Y_P^\circ$$은 $$G/P$$를 결정하는 maximal parabolic factor의 수와 같다.

## Hessenberg variety로서의 기술

위에서 본 interpolation 그림을 형식화하면 Peterson variety는 *Hessenberg variety*라 불리는 더 넓은 부분다양체 집합의 특수한 예가 된다.

<div class="definition" markdown="1">

<ins id="def8">**정의 8**</ins> $$X\in\mathfrak{g}$$와 $$\mathfrak{b}$$를 포함하는 $$\Ad$$-stable subspace $$H\subseteq\mathfrak{g}$$ (즉 $$[\mathfrak{b},H]\subseteq H$$)에 대하여, *Hessenberg variety*는

$$\mathcal{B}(X,H)=\{\,gB\in G/B\;\mid\;\Ad(g^{-1})X\in H\,\}$$

로 정의된다.

</div>

$$H=\mathfrak{b}$$이면 $$\mathcal{B}(X,\mathfrak{b})$$은 $$X$$의 Springer fiber이고, $$H=\mathfrak{g}$$이면 $$\mathcal{B}(X,\mathfrak{g})=G/B$$ 전체이다. 그 사이에서 $$X$$가 regular nilpotent이고 $$H=\mathfrak{b}\oplus\bigoplus_i\mathbb{C}f_i$$ ($$f_i\in\mathfrak{g}_{-\alpha_i}$$는 simple negative root vector)인 경우가 바로 Peterson variety로, 위에서 말한 $$\mathfrak{b}$$ 바로 다음 단계에 해당한다. [정의 6](#def6)은 $$G/B^-$$ 위의 coadjoint 조건으로 적었지만, Killing form으로 $$\mathfrak{g}^\ast\cong\mathfrak{g}$$를 동일시하고 $$G/B^-\cong G/B$$를 취하면 그 annihilator 조건이 위 Hessenberg 조건 $$\Ad(g^{-1})X\in H$$로 옮겨지므로, 두 기술은 같은 variety를 가리킨다. 이 Hessenberg 관점은 $$Y_B^\circ$$을 $$\mathfrak{n}^-$$의 적절한 affine 좌표 위에서 명시적인 방정식으로 다룰 수 있게 해 준다 (Insko–Tymoczko [IT]).

<div class="example" markdown="1">

<ins id="ex9">**예시 9**</ins> type $$A_{n-1}$$, 곧 $$G=\GL_n(\mathbb{C})$$에서 보자. Principal nilpotent $$N=\sum_{i=1}^{n-1}E_{i,i+1}$$ (superdiagonal 성분이 $$1$$)은 regular nilpotent이고, 위 Hessenberg 기술에서 Peterson variety는 complete flag variety $$Fl_n=\GL_n(\mathbb{C})/B$$ 안에서

$$\Pet_n=\{\,V_\bullet\mid NV_i\subseteq V_{i+1},\ i=1,\ldots,n-1\,\}$$

로 주어진다. 이는 Hessenberg 함수 $$h=(2,3,\ldots,n,n)$$에 대응하며, 그 차원은 $$\sum_{j=1}^n\bigl(h(j)-j\bigr)=n-1=\rank(\mathfrak{sl}_n)$$으로 명제 [명제 7](#prop7)과 일치한다.

$$n=3$$에서 구체적으로, $$Ne_1=0$$, $$Ne_2=e_1$$, $$Ne_3=e_2$$이고 마지막 조건 $$NV_2\subseteq V_3=\mathbb{C}^3$$은 자동이므로

$$\Pet_3=\{(V_1\subset V_2)\in Fl_3\mid NV_1\subseteq V_2\}$$

이다. $$\dim_\mathbb{C}Fl_3=3$$에서 조건 하나가 차원을 $$1$$ 깎아 $$\dim\Pet_3=2$$가 된다. 이 surface가 지나는 coordinate flag $$E^w_\bullet$$ ($$w\in S_3$$, $$V_i=\span\{e_{w(1)},\ldots,e_{w(i)}\}$$)들은 $$Ne_{w(1)}\in\span\{e_{w(1)},e_{w(2)}\}$$을 만족하는 $$w$$, 즉

$$w\in\{e,\,s_1,\,s_2,\,w_0\}=\{123,\,213,\,132,\,321\}$$

의 네 개이다. 이들은 simple root 부분집합 $$A\subseteq\{\alpha_1,\alpha_2\}$$에 그 parabolic의 maximal length element $$w_A$$를 대응시킨 $$2^{n-1}=4$$개의 fixed point로, Peterson variety가 simple root들의 조합론을 기억하고 있음을 보여 준다.

</div>

## Stratification

Peterson variety는 [§Bruhat decomposition, ⁋정리 13](/ko/math/lie_theory/bruhat_decomposition#thm13)의 cell 분해를 $$G/B^-$$로 옮긴 것과 호환되는 자연스러운 stratification을 가진다. 각 stratum은 $$Y_P^\circ$$가 어느 Bruhat cell과 만나는가로 정해지며, Weyl group 원소로 색인된다.

$$Y_P^\circ=\bigsqcup_{w\in W^P}Y_{P,w}^\ast,\qquad Y_{P,w}^\ast=Y_P^\circ\cap(BwB^-)/B^-$$

특히 중요한 것은 open stratum $$Y_{P,e}^\ast$$로, big Bruhat cell $$BB^-/B^-\subseteq G/B^-$$과의 intersection으로 주어지는 $$Y_P^\circ$$의 Zariski 조밀 open subset이다. 이 open stratum의 coordinate ring이 Peterson variety의 affine 기하를 분석할 때 표준적인 출발점이 되며, stratification 전체는 $$Y_P^\circ$$의 coordinate ring을 $$W^P$$로 색인된 조각들로 분해해 준다.

<div class="remark" markdown="1">

<ins id="rmk10">**참고 10**</ins> 위 stratification은 Peterson variety의 cohomology를 조합적으로 계산하는 출발점이 된다. Insko–Tymoczko [IT]는 regular nilpotent Hessenberg variety가 affine cell들로 paving됨을 보였고, 그로부터 $$Y_P^\circ$$의 cohomology(나아가 Chow ring)가 각 cell로 색인된 basis를 갖는 free module이 됨이 따른다. 즉 [§Bruhat decomposition, ⁋명제 17](/ko/math/lie_theory/bruhat_decomposition#prop17)에서 본 flag variety의 affine paving 논법이 Peterson variety에도 그대로 작동한다.

</div>

---

**참고문헌**

**[KL80]** D. Kazhdan, G. Lusztig, *Schubert varieties and Poincaré duality*, Geometry of the Laplace operator, Proc. Sympos. Pure Math. **36**, AMS, 1980.

**[Deo85]** V. V. Deodhar, *On some geometric aspects of Bruhat orderings. I. A finer decomposition of Bruhat cells*, Invent. Math. **79** (1985), 499--511.

**[Ric92]** R. W. Richardson, *Intersections of double cosets in algebraic groups*, Indag. Math. **3** (1992), 69--77.

**[Bri]** M. Brion, *Lectures on the geometry of flag varieties*, in *Topics in cohomological studies of algebraic varieties*, Trends Math., Birkhäuser, 2005, 33--85.

**[Kos]** B. Kostant, *The principal three-dimensional subgroup and the Betti numbers of a complex simple Lie group*, Amer. J. Math. **81** (1959), 973--1032.

**[Pet]** D. Peterson, Lecture notes, Massachusetts Institute of Technology, Spring 1997 (unpublished).

**[Rie]** K. Rietsch, *Totally positive Toeplitz matrices and quantum cohomology of partial flag varieties*, J. Amer. Math. Soc. **16** (2003), 363--392.

**[IT]** E. Insko, J. Tymoczko, *Affine pavings of regular nilpotent Hessenberg varieties and intersection theory of the Peterson variety*, J. Combin. Theory Ser. A **187** (2022), 105572.
