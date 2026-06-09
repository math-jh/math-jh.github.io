---
title: "Richardson variety와 Peterson variety"
description: "Schubert variety와 opposite Schubert variety의 교차로 정의되는 Richardson variety와 regular nilpotent element가 잘라내는 Peterson variety를 함께 다룬다. 두 부분다양체의 정의·차원, 교차이론에서의 역할, Grassmannian과 type A에서의 구체적 모습, 그리고 Bruhat cell에 의한 stratification을 살펴본다."
excerpt: "두 opposite Schubert variety의 transversal한 교차인 Richardson variety와 regular nilpotent의 Peterson variety: 정의·차원·교차이론·계층화"

categories: [Math / Lie Theory]
permalink: /ko/math/lie_theory/richardson_peterson_variety
sidebar:
    nav: "Lie_theory-ko"

date: 2025-01-05
last_modified_at: 2026-06-09
weight: 6
published: false
---

[§Bruhat decomposition](/ko/math/lie_theory/bruhat_decomposition)에서 우리는 partial flag variety $$G/P$$가 Bruhat cell들로 분해되고, 각 cell의 closure인 Schubert variety가 $$G/P$$의 기하를 Weyl group의 조합론으로 환원함을 보았다. 이 글에서는 그 분해 위에 자연스럽게 얹히는 두 종류의 부분다양체를 다룬다. 하나는 서로 opposite인 두 Bruhat 분해를 *교차*시켜 얻는 *Richardson variety*이고, 다른 하나는 regular nilpotent element 하나가 잘라내는 *Peterson variety*이다. 전자는 Schubert variety들의 교차이론을 떠받치는 무대이고, 후자는 flag variety와 nilpotent cone을 잇는 통로이다. 두 대상 모두 Grassmannian의 거울 대칭에서 핵심적인 역할을 하는데, open Richardson variety는 Marsh–Rietsch mirror의 정의역으로, Peterson variety는 그 superpotential의 critical locus로 등장한다.

## Richardson variety

우리는 [§Bruhat decomposition](/ko/math/lie_theory/bruhat_decomposition)에서와 같이 복소수체 $$\mathbb{C}$$ 위 connected reductive algebraic group $$G$$와 그 Borel subgroup $$B$$, 그리고 $$B$$를 포함하는 parabolic subgroup $$P$$를 고정한다. Opposite Borel subgroup $$B^-$$ ($$B\cap B^-=T$$)를 함께 두면, [§Bruhat decomposition, ⁋정의 16](/ko/math/lie_theory/bruhat_decomposition#def16)에서 도입한 두 방향의 cell 구조

$$X_w^\circ=BwP/P,\qquad X^w_\circ=B^-wP/P\qquad(w\in W^P)$$

와 그 Zariski closure인 Schubert variety $$X_w=\overline{X_w^\circ}$$, opposite Schubert variety $$X^w=\overline{X^w_\circ}$$를 얻는다. 두 cell은 각각 $$X_w^\circ\cong\mathbb{A}^{\ell(w)}$$, $$X^w_\circ\cong\mathbb{A}^{\dim(G/P)-\ell(w)}$$이므로, 같은 $$w$$에 대해서도 한쪽은 작고 한쪽은 큰, 즉 서로 차원을 뒤집은 두 분해가 $$G/P$$ 위에 동시에 놓이게 된다. Richardson variety는 이 두 방향의 cell을 교차시킨 것이다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> $$u,w\in W^P$$에 대하여, Schubert variety와 opposite Schubert variety의 교집합

$$R_{u,w}=X_w\cap X^u$$

을 *Richardson variety*라 하고, 두 열린 cell의 교집합

$$\mathring{R}_{u,w}=X_w^\circ\cap X^u_\circ$$

을 *open Richardson variety*라 한다.

</div>

정의에 의해 $$R_{u,w}$$는 $$G/P$$의 닫힌 부분다양체이고, $$\mathring{R}_{u,w}$$는 그 안의 Zariski 열린 부분집합이다. 이 대상은 Richardson [Ric92]이 algebraic group의 double coset 교차를 연구하면서 처음 다루었으며, 이후 flag variety의 교차이론, $$K$$-이론, 그리고 [§Kazhdan–Lusztig polynomial](/ko/math/lie_theory/kazhdan_lusztig)의 기하학적 해석에서 표준적인 무대가 되었다. 두 cell이 각각 $$B$$와 $$B^-$$의 궤도라는 점, 곧 서로 *반대 방향*에서 오는 분해라는 점이 다음 명제에서 결정적으로 작동한다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> Open Richardson variety $$\mathring{R}_{u,w}$$가 비어있지 않을 필요충분조건은 Bruhat order에서 $$u\leq w$$인 것이다. 이 조건이 성립하면 $$\mathring{R}_{u,w}$$는 차원 $$\ell(w)-\ell(u)$$의 smooth irreducible affine variety이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$X_w^\circ$$는 $$B$$의 궤도, $$X^u_\circ$$는 $$B^-$$의 궤도이므로 둘 다 $$G/P$$ 위의 locally closed subset이고, 그 교집합 $$\mathring{R}_{u,w}$$ 역시 locally closed이다. 핵심은 두 분해가 *transversal*하게 만난다는 데 있다. $$X_w^\circ$$의 한 점 $$x$$에서의 tangent space $$T_xX_w^\circ$$는 $$\mathfrak{b}$$가 만드는 방향들로, $$T_xX^u_\circ$$는 $$\mathfrak{b}^-$$가 만드는 방향들로 채워지는데, $$\mathfrak{b}+\mathfrak{b}^-=\mathfrak{g}$$이므로 두 tangent space는 $$T_x(G/P)$$ 안에서 일반위치에 놓인다. 따라서 교집합이 비어있지 않은 한 그 위에서 두 cell은 transversal하게 만나고, Kleiman의 일반위치 정리에 의해 교집합은 smooth이며 그 차원은

$$\dim X_w^\circ+\dim X^u_\circ-\dim(G/P)=\ell(w)+\bigl(\dim(G/P)-\ell(u)\bigr)-\dim(G/P)=\ell(w)-\ell(u)$$

이다. 교집합이 비어있지 않을 조건이 정확히 $$u\leq w$$임은 Bruhat cell의 closure 관계로부터 따라나오며, 이는 Deodhar [Deo85]와 Kazhdan–Lusztig [KL80]의 결과이다. 같은 일반위치 논증이 irreducibility까지 주며, affineness는 $$\mathring{R}_{u,w}$$가 big cell의 아핀 좌표 안에서 닫힌 부분다양체로 실현됨에서 온다. 자세한 것은 Brion [Bri]를 참조한다.

</details>

명제 [명제 2](#prop2)가 말하는 바는 일반적으로 특이점을 갖는 Schubert variety라도, 반대 방향의 opposite Schubert variety와 교차시키면 특이한 방향들이 서로 상쇄되어 부드러운 구조만 남는다는 것이다. 차원 공식 $$\ell(w)-\ell(u)$$은 음이 아니어야 하므로 $$u\leq w$$ 조건과 정확히 맞물리며, $$u=w$$인 경계에서는 차원이 $$0$$으로 떨어진다.

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> 두 극단을 보자. $$u=w$$이면 $$\mathring{R}_{w,w}=X_w^\circ\cap X^w_\circ$$은 한 점 $$wP/P$$만으로 이루어진다. 이는 $$X_w$$와 $$X^w$$가 오직 그 한 점에서만 만나기 때문이며, 차원 $$\ell(w)-\ell(w)=0$$과 부합한다. 반대로 $$u=e$$ (단위원)이고 $$w=w_0^P$$ ($$W^P$$의 최장원소)이면, $$X_{w_0^P}=G/P$$이고 $$X^e_\circ$$은 open dense cell이므로 $$\mathring{R}_{e,w_0^P}=X^e_\circ$$은 $$G/P$$의 가장 큰 open cell이 되어, 차원은 $$\ell(w_0^P)-0=\dim(G/P)$$이다.

</div>

## Intersection theory와 Schubert calculus

Richardson variety가 단순한 교집합 이상의 의미를 갖는 것은 그것이 cohomology ring $$H^\ast(G/P)$$의 곱셈 구조를 직접 실현하기 때문이다. Schubert variety의 class $$[X_w]\in H^\ast(G/P)$$들은 ([§Bruhat decomposition, ⁋명제 17](/ko/math/lie_theory/bruhat_decomposition#prop17)에서 본 affine paving으로부터) $$H^\ast(G/P)$$의 additive basis를 이루며, cohomology의 곱은 일반위치에서의 transversal한 교차로 계산된다. 서로 opposite인 $$B$$와 $$B^-$$를 쓰는 것이 바로 두 Schubert variety를 일반위치로 옮기는 표준적인 방법이고, 그 교차가 Richardson variety이다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> $$u,w\in W^P$$에 대하여 cohomology ring $$H^\ast(G/P)$$에서

$$[X_w]\cdot[X^u]=[R_{u,w}]$$

이 성립한다 (단 $$u\not\leq w$$이면 $$R_{u,w}=\varnothing$$이고 양변이 $$0$$이다). 특히 $$\ell(u)=\ell(w)$$일 때

$$\int_{G/P}[X_w]\cdot[X^u]=\delta_{u,w}$$

이므로, opposite Schubert class들 $$\{[X^u]\}_{u\in W^P}$$은 Schubert class들 $$\{[X_w]\}_{w\in W^P}$$의 Poincaré dual basis를 이룬다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[명제 2](#prop2)의 증명에서 본 것처럼 $$X_w$$와 $$X^u$$는 $$B$$와 $$B^-$$가 주는 일반위치에서 transversal하게 만나므로, 그 교차 class는 두 class의 곱과 같다. 이것이 $$[X_w]\cdot[X^u]=[R_{u,w}]$$이다 (Kleiman 일반위치, [Bri] 참조). $$\ell(u)=\ell(w)$$인 경우 $$R_{u,w}$$의 차원은 $$\ell(w)-\ell(u)=0$$이고, [명제 2](#prop2)에 의해 $$u=w$$이면 reduced point 하나, $$u\neq w$$이면 ($$u\leq w$$가 깨져) 공집합이다. 따라서 그 0차원 class의 차수, 곧 $$\int_{G/P}[X_w]\cdot[X^u]$$은 $$\delta_{u,w}$$이다.

</details>

명제 [명제 4](#prop4)은 Schubert basis의 곱셈 구조상수를 Richardson variety의 차수로 환원한다. 세 class의 곱 $$[X_w]\cdot[X^u]\cdot[X_v]$$을 적분하면 세 일반위치 Schubert variety의 교차수가 나오는데, 이것이 곧 구조상수 — Grassmannian의 경우 Littlewood–Richardson 계수 — 이며, 이로부터 classical *Schubert calculus*가 전개된다. Richardson variety의 intersection cohomology가 두 Schubert variety의 Kazhdan–Lusztig polynomial의 차이로 기술된다는 사실 또한 이 일반위치 교차의 정밀화로 이해할 수 있다.

## Grassmannian에서의 Richardson variety

가장 손에 잡히는 경우는 $$G/P=\Gr_k(\mathbb{C}^n)\cong\GL_n(\mathbb{C})/P_k$$인 Grassmannian이다. 이때 $$W=S_n$$, $$W_{P_k}=S_k\times S_{n-k}$$이고, minimal length coset representative $$W^{P_k}$$은 [§Bruhat decomposition, ⁋명제 14](/ko/math/lie_theory/bruhat_decomposition#prop14)에서 본 $$(k,n-k)$$-shuffle들이다. Schubert variety $$X_w$$는 표준 flag $$E_\bullet$$에 대한 $$\dim(V\cap E_{w(a)})\geq a$$ 꼴의 rank 조건으로, opposite Schubert variety $$X^u$$는 opposite flag $$\tilde{E}_\bullet$$ ($$\tilde{E}_j=\operatorname{span}\{e_n,\ldots,e_{n-j+1}\}$$)에 대한 대칭적 rank 조건으로 잘린다. Richardson variety는 이 두 조건을 동시에 부과한 것이다.

<div class="example" markdown="1">

<ins id="ex5">**예시 5**</ins> $$\Gr_2(\mathbb{C}^4)$$에서 $$u=1324$$, $$w=2413$$을 택하자. [§Bruhat decomposition, ⁋예시 18](/ko/math/lie_theory/bruhat_decomposition#ex18)의 jump set 순서로 $$1324\leftrightarrow\{1,3\}$$, $$2413\leftrightarrow\{2,4\}$$이고 성분별로 $$1\leq2$$, $$3\leq4$$이므로 $$u\leq w$$이며, $$\ell(2413)-\ell(1324)=3-1=2$$이다. 두 Schubert 조건은 각각

$$X_{2413}=\{V\mid\dim(V\cap E_2)\geq1\},\qquad X^{1324}=\{V\mid\dim(V\cap\tilde{E}_2)\geq1\}$$

로, $$E_2=\operatorname{span}\{e_1,e_2\}$$와 $$\tilde{E}_2=\operatorname{span}\{e_3,e_4\}$$은 서로 보충하는 두 평면이다. 따라서

$$R_{1324,2413}=\{V\in\Gr_2(\mathbb{C}^4)\mid V\cap E_2\neq0,\ V\cap\tilde{E}_2\neq0\}$$

은 $$E_2$$ 안의 한 직선과 $$\tilde{E}_2$$ 안의 한 직선을 골라 span한 평면들의 모임이다. $$E_2\cap\tilde{E}_2=0$$이므로 두 직선은 항상 독립이고, 대응 $$([\,p\,],[\,q\,])\mapsto\langle p,q\rangle$$은 동형

$$R_{1324,2413}\cong\mathbb{P}(E_2)\times\mathbb{P}(\tilde{E}_2)\cong\mathbb{P}^1\times\mathbb{P}^1$$

을 준다. 차원 $$2$$의 smooth variety로, 명제 [명제 2](#prop2)의 차원과 정확히 맞는다. 그 open part는 행렬

$$V=\operatorname{rowspan}\begin{pmatrix}1&s&0&0\\0&0&1&t\end{pmatrix}\qquad(s,t)\in\mathbb{A}^2$$

로 좌표화되는데, 위 행렬의 jump set이 $$\{2,4\}$$이므로 $$V\in X_{2413}^\circ$$이고 둘째 행이 $$\tilde{E}_2$$ 안에 있으므로 $$V\in X^{1324}_\circ$$이다. 즉 $$\mathring{R}_{1324,2413}$$은 이 $$(s,t)$$-평면의 열린 부분으로, smooth affine 차원 $$2$$임이 좌표에서 곧장 드러난다.

</div>

이러한 좌표화는 Richardson variety의 좌표환을 명시적으로 다룰 수 있게 한다. 특히 parabolic 최장원소 $$w_P$$와 전체 최장원소 $$w_0$$에 대한 open Richardson variety $$\mathring{R}_{w_P,w_0}$$은 Marsh–Rietsch가 Grassmannian 거울 대칭의 mirror 정의역과 동일시한 대상으로, 거기서 boundary divisor가 cyclic하게 도는 Schubert divisor들과 맞물린다.

## Regular nilpotent element

이제 같은 flag variety를 전혀 다른 방식으로 — 한 nilpotent element가 부과하는 조건으로 — 잘라낸 Peterson variety로 넘어간다. complex semisimple Lie algebra $$\mathfrak{g}$$와 그에 대응하는 simply-connected algebraic group $$G$$를 고정하고, Borel subgroup $$B$$, opposite Borel $$B^-$$, 그리고 그 Lie algebra $$\mathfrak{b}$$, $$\mathfrak{b}^-$$를 둔다. $$\mathfrak{n}=[\mathfrak{b},\mathfrak{b}]$$, $$\mathfrak{n}^-=[\mathfrak{b}^-,\mathfrak{b}^-]$$를 각각 positive, negative nilpotent subalgebra라 하고, [§근계](/ko/math/lie_theory/root_systems)의 root space decomposition $$\mathfrak{g}=\mathfrak{h}\oplus\bigoplus_{\alpha\in\Phi}\mathfrak{g}_\alpha$$를 가정한다.

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> Nilpotent element $$e\in\mathfrak{g}$$가 *regular*라는 것은 그 centralizer $$\mathfrak{z}_{\mathfrak{g}}(e)=\{X\in\mathfrak{g}\mid[X,e]=0\}$$의 차원이 $$\operatorname{rank}(\mathfrak{g})$$와 같은 것이다.

</div>

구체적으로 각 simple root $$\alpha_i$$마다 $$0\neq e_i\in\mathfrak{g}_{\alpha_i}$$를 하나씩 골라 $$e=\sum_i e_i$$으로 두면 이 $$e$$는 regular nilpotent이고, 모든 regular nilpotent는 $$G$$의 adjoint action에 의해 서로 conjugate하다. 이는 Kostant [Kos]의 고전적 결과로, regular nilpotent의 centralizer가 abelian이며 그 차원이 정확히 $$\operatorname{rank}(\mathfrak{g})$$임을 함께 보여 준다. 이 사실이 곧 Peterson variety의 차원을 결정하게 된다.

## Peterson variety의 정의

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> Parabolic subgroup $$P\supseteq B$$에 대응하는 *Peterson variety* $$Y_P^\circ$$는 $$R=G/B^-$$의 부분다양체

$$Y_P^\circ=\{\,gB^-\in R\;\mid\;\operatorname{Ad}^\ast(g^{-1})\cdot F\in[\mathfrak{n}^-,\mathfrak{n}^-]^\perp\,\}$$

로 정의된다. 여기서 $$F=e_1^\ast+e_2^\ast+\cdots+e_{n-1}^\ast\in\mathfrak{g}^\ast$$은 dualize한 positive Chevalley generator들의 합 ($$\mathfrak{g}^\ast$$에서의 regular nilpotent에 해당), $$\operatorname{Ad}^\ast$$은 $$G$$의 coadjoint action, $$[\mathfrak{n}^-,\mathfrak{n}^-]^\perp\subseteq\mathfrak{g}^\ast$$은 derived subalgebra의 annihilator이다.

</div>

$$P=B$$일 때가 Kostant–Peterson의 원래 정의 [Pet]이며, 일반의 $$P$$에 대한 위 형태는 후속 연구 [Rie]에서 표준적으로 쓰인다. 정의에서 $$F$$가 regular nilpotent라는 점이 핵심으로, 그 coadjoint stabilizer가 $$\operatorname{rank}(\mathfrak{g})$$차원의 abelian subalgebra라는 Kostant의 정리가 $$Y_P^\circ$$의 차원을 곧장 준다.

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> $$P=B$$인 경우, Peterson variety $$Y_B^\circ\subseteq G/B^-$$의 차원은 $$\operatorname{rank}(\mathfrak{g})$$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$F\in\mathfrak{g}^\ast$$을 regular nilpotent로 잡았으므로 Kostant [Kos]의 정리에 의해 그 coadjoint stabilizer $$G_F=\{g\in G\mid\operatorname{Ad}^\ast(g)\cdot F=F\}$$의 connected component는 abelian이고 그 차원은 $$\operatorname{rank}(\mathfrak{g})$$이다. $$G/B^-$$를 $$B^-$$ 위에서의 $$G$$-quotient로 보면, 정의에서 부과한 조건 $$\operatorname{Ad}^\ast(g^{-1})\cdot F\in[\mathfrak{n}^-,\mathfrak{n}^-]^\perp$$은 codimension $$\dim[\mathfrak{n}^-,\mathfrak{n}^-]$$의 affine 조건을 자른다. 두 차원의 차이를 계산하면 정확히 $$\operatorname{rank}(\mathfrak{g})$$가 남는다. 자세한 dimension count는 [Pet], [Rie]를 참조한다.

</details>

이 결과는 $$\operatorname{rank}(\mathfrak{g})$$가 simple root의 개수와 같다는 사실과 맞물린다. type $$A_{n-1}$$에서는 $$\operatorname{rank}(\mathfrak{sl}_n)=n-1$$이므로 Peterson variety의 차원도 $$n-1$$이며, 이는 아래 Hessenberg 기술의 dimension formula와도 일치한다. 더 일반적인 parabolic $$P$$에 대해서도 비슷한 공식이 성립하여, $$\dim Y_P^\circ$$은 $$G/P$$를 결정하는 maximal parabolic factor의 수와 같다.

## Hessenberg variety로서의 기술

Peterson variety는 *Hessenberg variety*라 불리는 더 넓은 부분다양체 집합의 특수한 예로 기술된다.

<div class="definition" markdown="1">

<ins id="def9">**정의 9**</ins> $$X\in\mathfrak{g}$$와 $$\mathfrak{b}$$를 포함하는 $$\operatorname{ad}$$-stable subspace $$H\subseteq\mathfrak{g}$$ (즉 $$[\mathfrak{b},H]\subseteq H$$)에 대하여, *Hessenberg variety*는

$$\mathcal{B}(X,H)=\{\,gB\in G/B\;\mid\;\operatorname{Ad}(g^{-1})X\in H\,\}$$

로 정의된다.

</div>

$$X$$가 regular nilpotent이고 $$H=\mathfrak{b}\oplus\bigoplus_i\mathbb{C}f_i$$ ($$f_i\in\mathfrak{g}_{-\alpha_i}$$는 simple negative root vector)인 경우의 Hessenberg variety가 바로 Peterson variety이다. [정의 7](#def7)은 $$G/B^-$$ 위의 coadjoint 조건으로 적었지만, Killing form으로 $$\mathfrak{g}^\ast\cong\mathfrak{g}$$를 동일시하고 $$G/B^-\cong G/B$$를 취하면 그 annihilator 조건이 위 Hessenberg 조건 $$\operatorname{Ad}(g^{-1})X\in H$$로 옮겨지므로, 두 기술은 같은 variety를 가리킨다. 이 Hessenberg 관점은 $$Y_B^\circ$$을 $$\mathfrak{n}^-$$의 적절한 아핀 좌표 위에서 명시적인 방정식으로 다룰 수 있게 해 준다 (Insko–Tymoczko [IT]).

<div class="example" markdown="1">

<ins id="ex10">**예시 10**</ins> type $$A_{n-1}$$, 곧 $$G=\GL_n(\mathbb{C})$$에서 보자. Principal nilpotent $$N=\sum_{i=1}^{n-1}E_{i,i+1}$$ (superdiagonal 성분이 $$1$$)은 regular nilpotent이고, 위 Hessenberg 기술에서 Peterson variety는 complete flag variety $$Fl_n=\GL_n(\mathbb{C})/B$$ 안에서

$$\operatorname{Pet}_n=\{\,V_\bullet\mid NV_i\subseteq V_{i+1},\ i=1,\ldots,n-1\,\}$$

로 주어진다. 이는 Hessenberg 함수 $$h=(2,3,\ldots,n,n)$$에 대응하며, 그 차원은 $$\sum_{j=1}^n\bigl(h(j)-j\bigr)=n-1=\operatorname{rank}(\mathfrak{sl}_n)$$으로 명제 [명제 8](#prop8)과 일치한다.

$$n=3$$에서 구체적으로, $$Ne_1=0$$, $$Ne_2=e_1$$, $$Ne_3=e_2$$이고 마지막 조건 $$NV_2\subseteq V_3=\mathbb{C}^3$$은 자동이므로

$$\operatorname{Pet}_3=\{(V_1\subset V_2)\in Fl_3\mid NV_1\subseteq V_2\}$$

이다. $$\dim_\mathbb{C}Fl_3=3$$에서 조건 하나가 차원을 $$1$$ 깎아 $$\dim\operatorname{Pet}_3=2$$가 된다. 이 surface가 지나는 coordinate flag $$E^w_\bullet$$ ($$w\in S_3$$, $$V_i=\operatorname{span}\{e_{w(1)},\ldots,e_{w(i)}\}$$)들은 $$Ne_{w(1)}\in\operatorname{span}\{e_{w(1)},e_{w(2)}\}$$을 만족하는 $$w$$, 즉

$$w\in\{e,\,s_1,\,s_2,\,w_0\}=\{123,\,213,\,132,\,321\}$$

의 네 개이다. 이들은 simple root 부분집합 $$A\subseteq\{\alpha_1,\alpha_2\}$$에 그 parabolic의 longest element $$w_A$$를 대응시킨 $$2^{n-1}=4$$개의 고정점으로, Peterson variety가 simple root들의 조합론을 기억하고 있음을 보여 준다.

</div>

## Stratification

Peterson variety는 [§Bruhat decomposition, ⁋정리 13](/ko/math/lie_theory/bruhat_decomposition#thm13)의 cell 분해를 $$G/B^-$$로 옮긴 것과 호환되는 자연스러운 stratification을 가진다. 각 stratum은 $$Y_P^\circ$$가 어느 Bruhat cell과 만나는가로 정해지며, Weyl group 원소로 색인된다.

$$Y_P^\circ=\bigsqcup_{w\in W^P}Y_{P,w}^\ast,\qquad Y_{P,w}^\ast=Y_P^\circ\cap(BwB^-)/B^-$$

특히 중요한 것은 open stratum $$Y_{P,e}^\ast$$로, big Bruhat cell $$BB^-/B^-\subseteq G/B^-$$과의 교집합으로 주어지는 $$Y_P^\circ$$의 Zariski 조밀 열린 부분집합이다. 이 open stratum의 좌표환이 Peterson variety의 아핀 기하를 분석할 때 표준적인 출발점이 되며, stratification 전체는 $$Y_P^\circ$$의 좌표환을 $$W^P$$로 색인된 조각들로 분해해 준다.

<div class="remark" markdown="1">

<ins id="rmk11">**참고 11**</ins> 이 stratification은 단순한 위상적 분해를 넘어 $$G/P$$의 quantum cohomology와 직접 연결된다. Peterson이 (unpublished) 보이고 이후 Rietsch [Rie], Lam–Shimozono 등이 정식화한 결과에 따르면, open stratum $$Y_{P,e}^\ast$$의 좌표환은 $$G/P$$의 (적절히 localize한) quantum cohomology $$qH^\ast(G/P)$$와 동형이다. 바로 이 동형이 Grassmannian 거울 대칭에서 Marsh–Rietsch superpotential의 critical locus가 곧 Peterson variety의 open stratum과 일치하는 이유를 설명하는 Lie-theoretic 토대이다. 완전한 증명은 본 글의 범위를 벗어난다.

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
</content>
</invoke>
