---

title: "완비화의 성질들"
excerpt: ""

categories: [Math / Commutative Algebra]
permalink: /ko/math/commutative_algebra/properties_of_completion
header:
    overlay_image: /assets/images/Math/Commutative_Algebra/Properties_of_completion.png
    overlay_filter: 0.5
sidebar: 
    nav: "commutative_algebra-ko"

date: 2025-01-16
last_modified_at: 2025-01-16
weight: 15

---

이제 우리는 완비화의 몇몇 성질들을 추가로 살펴본다. 

## 완비화와 완전열

<div class="proposition" markdown="1">

<ins id="thm1">**정리 1**</ins> Noetherian ring $A$와 ideal $\mathfrak{a}$를 고정하고, $\widehat{A}$가 $\mathfrak{a}$에 대한 $A$의 completion이라 하자. 그럼 다음이 성립한다.

1. $\widehat{A}$는 noetherian이다.
2. $\widehat{A}/\mathfrak{a}^i\widehat{A}=A/\mathfrak{a}^i$가 모든 $i$에 대해 성립한다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $A$가 noetherian이므로, $A/\mathfrak{a}$ 또한 noetherian이고 $\mathfrak{a}/\mathfrak{a}^2$은 finitely generated $A/\mathfrak{a}$-module이다. 이에 $\gr_\mathfrak{a}A$는 $A/\mathfrak{a}$-algebra로서, $\mathfrak{a}/\mathfrak{a}^2$에 의해 생성되고, 따라서 [##ref##](Hilbert_basis_thm)에 의하여 $\gr_\mathfrak{a}A$는 Noetherian이다. 이제 $\gr_{\widehat{\mathfrak{a}}}\widehat{A}=\gr_\mathfrak{a}A$이므로 $\gr_{\widehat{\mathfrak{a}}}\widehat{A}$ 또한 noetherian임을 안다. 한편, 임의의 ideal $\widehat{\mathfrak{a}}\subseteq \widehat{A}$에 대하여, initial ideal $\initial(\widehat{\mathfrak{a}})$은 위의 논증에 의해 유한히 많은 원소들로 생성되므로 [§완비화, ⁋명제 7](/ko/math/commutative_algebra/completion#prop7)에 의해 첫 번째 결과를 얻는다.

한편 두 번째 결과의 경우 우리는 다시 [§완비화, ⁋명제 7](/ko/math/commutative_algebra/completion#prop7)에 의해 $\widehat{\mathfrak{a}}^i$와 $\mathfrak{a}^i \widehat{A}$가 같다는 것은 곧 이들의 initial ideal이 같다는 것임을 알고, 따라서 원하는 결과를 얻는다.

</details>

다음 보조정리는 [§완비화, §§$\mathfrak{a}$진 위상](http://localhost:4000/ko/math/commutative_algebra/completion#mathfraka%EC%A7%84-%EC%9C%84%EC%83%81)에서 살펴본 completion의 위상구조 및 base와, [\[위상수학\] §위상공간의 기저, ⁋명제 2](/ko/math/topology/topological_bases#prop2)를 사용하여 위상공간의 두 base가 언제 같은 위상을 정의하는지를 따져보면 쉽게 증명할 수 있다.

<div class="proposition" markdown="1">

<ins id="lem2">**보조정리 2**</ins> Ring $A$의 두 filtration

$$\mathcal{J}:\qquad A=\mathfrak{a}_0\supseteq \mathfrak{a}_1\supseteq \mathfrak{a}_2\supseteq\cdots$$

그리고

$$\mathcal{J}': \qquad A=\mathfrak{a}_0'\supseteq \mathfrak{a}_1'\supseteq \mathfrak{a}_2'\supseteq\cdots$$

가 주어졌다 하자. 만일 각각의 $\mathfrak{a}\_i$마다 적당한 $\mathfrak{a}\_j'$가 존재하여 $\mathfrak{a}\_j'\subseteq \mathfrak{a}\_i$이고, 각각의 $\mathfrak{a}\_i'$마다 적당한 $\mathfrak{a}\_j$가 존재하여 $\mathfrak{a}\_j\subseteq \mathfrak{a}\_i'$라면 $\widehat{A}\_\mathcal{J}\cong \widehat{A}\_{\mathcal{J}'}$가 성립한다.

</div>

한편 [\[범주론\] §극한, ⁋명제 10](/ko/math/category_theory/limits#prop10)에 의하여, completion을 취하는 것은 left exact이다. 다음 보조정리는 적절한 종류의 유한성이 가정된다면, completion을 취하는 것은 right exact이기도 하다는 것을 보여준다.

<div class="proposition" markdown="1">

<ins id="lem3">**보조정리 3**</ins> Noetherian ring $A$와 ideal $\mathfrak{a}$를 고정하자. 그럼 finitely generated $A$-module들의 short exact sequence

$$0 \rightarrow A \rightarrow B \rightarrow C \rightarrow 0$$

에 대하여, 다음의 sequence

$$0 \rightarrow \varprojlim A/\mathfrak{a}^i A \rightarrow \varprojlim B/\mathfrak{a}^i B \rightarrow \varprojlim C/\mathfrak{a}^i C \rightarrow 0$$

는 exact sequence가 된다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

앞선 논증에 의하여 우리는 $\varprojlim B/\mathfrak{a}^i B \rightarrow \varprojlim C/\mathfrak{a}^i C$가 surjective인 것만 보이면 된다. 

$\varprojlim C/\mathfrak{a}^i C$의 원소 $(c_i+\mathfrak{a}^i C)$가 주어졌다 하고, 다음 두 조건

- $b_i\mapsto c_i\pmod{\mathfrak{a}^i C}$,
- $b_i\equiv b_j\pmod{\mathfrak{a}^iB}$ for $i&lt;j$

을 만족하는 $(b_i+\mathfrak{a}^iB)$를 찾자. 그럼 고정된 $i$에 대해 첫째 조건만 만족하는 $b_i$를 찾을 수 있다는 것과, 두 번째 조건은 $j=i+1$인 경우만 보이면 된다는 것이 자명하다. 따라서 귀납적으로 이 두 조건들을 만족하는 $b_1,\ldots, b_k$를 찾았다 하고 $b_{k+1}$을 찾자. 우선 $b_{k+1}'\mapsto c_{k+1}\pmod{\mathfrak{a}^{k+1} C}$를 만족하는 $b_{k+1}'$을 택하자. 그럼 $b_{k+1}'$과 $b_k$는 $C/\mathfrak{a}^k C$에서는 같은 원소로 옮겨지므로, 다음의 exact sequence

$$A/\mathfrak{a}^{k}A  \rightarrow B/ \mathfrak{a}^{k}B \rightarrow C/ \mathfrak{a}^{k}C \rightarrow 0$$

로부터 적당한 $a\in A$를 찾아 $a$가 $B/\mathfrak{a}^kB$에서 $b_k-b_{k+1}'$로 옮겨지도록 할 수 있다. 이제 $b_{k+1}=b_{k+1}'+\alpha_{k+1}(a_{k+1})$로 두면 원하는 결과를 얻는다.

</details>

이로부터 다음 정리를 얻는다. 

<div class="proposition" markdown="1">

<ins id="thm4">**정리 4**</ins> Noetherian ring $A$와 ideal $\mathfrak{a}$를 고정하고, $\widehat{A}$가 $\mathfrak{a}$에 대한 $A$의 completion이라 하자. 그럼 다음이 성립한다.

1. 임의의 finitely generated $A$-module $M$에 대하여, 
    
    $$\widehat{A}\otimes_A M \rightarrow\varprojlim_i M/\mathfrak{a}^iM$$

    이 isomorphism이다. 
2. $\widehat{A}$는 flat $A$-module이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$\varprojlim$과 $\otimes$는 모두 finite direct sum과 commute하므로, $M$이 finitely generated free module인 경우는 첫째 결과가 자명하게 성립한다. 이제 임의의 finitely generated $A$-module $M$에 대하여, $M$의 free presentation

$$F \rightarrow G \rightarrow M \rightarrow 0$$

에 $\widehat{A}\otimes_A-$를 취하면 [보조정리 3](#lem3)과 [\[호몰로지 대수학\] §Diagram chasing, ⁋명제 1](/ko/math/homological_algebra/diagram_chasing#prop1)에 의해 원하는 결과를 얻는다. 

두 번째 결과는 [§평탄성, ⁋명제 1](/ko/math/commutative_algebra/flatness#prop1)에 의해, 임의의 finitely generated ideal $\mathfrak{a}$에 대해 $\widehat{a} \rightarrow \widehat{A}$가 injective임을 보이는 것과 같아지고, 이는 다시 [보조정리 3](#lem3)에서 살펴본 completion의 left exactness로부터 자명하다. 

</details>

## 헨젤의 보조정리

Complete ring의 대표적인 예시는 [§완비화, ⁋예시 4]()에서 살펴본 ring of formal power series $A[[\x_i]]
\_{i\in I}$이다. 한편 우리는 [\[대수적 구조\] §대수, ⁋명제 8](/ko/math/algebraic_structures/algebras#prop8)에서 ring of power series $A[\x_i]
\_{i\in I}$가 free functor $\Set \rightarrow \cAlg{A}$의 역할을 하는 것을 살펴보았는데, 비슷한 종류의 universal property가 $A[[\x_i]]_{i\in I}$에 대해서도 성립한다. 

<div class="proposition" markdown="1">

<ins id="thm5">**정리 5**</ins> Ring $A$와 ideal $\mathfrak{a}$를 고정하고, $\mathfrak{a}$에 대해 complete인 $A$-algebra $E$가 주어졌다 하자. $\alpha_1,\ldots,\alpha_n\in \mathfrak{a}$라 하면, 다음이 성립한다.

1. 각각의 $x_i$들을 $\alpha_i$로 보내는 유일한 $A$-algebra homomorphism $\phi:A[[\x_1,\ldots, \x_n]]\rightarrow E$이 존재한다. 
2. 만일 $A \rightarrow E/\mathfrak{a}$가 epimorphism이고, $\alpha_i$들이 $\mathfrak{a}$를 생성한다면 $\phi$ 또한 epimorphism이다. 
3. 만일 $\gr\phi: R[\x_1,\ldots, \x_n]\cong \gr_{(\x_1,\ldots, \x_n)}R[[\x_1,\ldots, \x_n]] \rightarrow \gr_\mathfrak{a}E$가 monomorphism이라면, $\phi$ 또한 그러하다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

첫 번째 주장은 [\[대수적 구조\] §대수, ⁋명제 8](/ko/math/algebraic_structures/algebras#prop8)와 거의 동일하며, 해당 명제와 마찬가지로 무한히 많은 변수에 대해서도 성립한다. 

두 번째 주장의 경우, 주어진 가정으로부터 

$$(\x_1,\ldots, \x_n)/(\x_1,\ldots, \x_n)^2 \rightarrow \mathfrak{a}/\mathfrak{a}^2$$

이 surjective라는 것을 알고, $\mathfrak{a}/\mathfrak{a}^2$이 $\gr_\mathfrak{a}E$를 생성하므로 $\gr\phi$가 surjective인 것을 안다. 이제 임의의 $y\in E$에 대하여, $y\in \mathfrak{a}^i$이도록 하는 가장 큰 $i$가 존재한다. 따라서 $x_1\in (\x_1,\ldots, \x_n)^i$가 존재하여 $x_1$의 initial form이 $\gr\phi$에 의해 $y$의 initial form으로 옮겨지도록 할 수 있고, 그럼 $y-\phi(x_1)\in \mathfrak{a}^{i+1}$이다. 이와 같은 과정을 반복하여 $A[\x_1,\ldots, \x_n]$의 원소들의 무한한 family $(x_1,x_2,\ldots)$가 다음 합

$$y=\sum_{j=1}^\infty \phi(x_j)=\phi\left(\sum_{j=1}^\infty x_j\right)$$

을 만족하도록 할 수 있다. 

마지막 주장은 만일 $x$가 $A[[\x_1,\ldots, \x_n]]$의 $0$이 아닌 원소라면, $\initial(x)$도 $0$이 아니고 따라서 $(\gr\phi)(\initial(x))$도 $0$이 아니게 된다. 그런데 $\initial(x)$의 degree를 $d$라 하면,

$$x\equiv \initial(x)\pmod{(\x_1,\ldots, \x_n)^{d+1}}$$

이므로

$$\phi(x)\equiv(\gr\phi)(\initial(x))\pmod{\mathfrak{a}^{d+1}}$$

이 되어 $\phi(x)\neq 0$이 된다. 

</details>

그럼 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="cor6">**따름정리 6**</ins> Power series $f\in \x A[[\x]]$를 고정하고, $\phi: A[[x]] \rightarrow A[[\x]]$를 다음 식

$$\phi: A[[\x]] \rightarrow A[[\x]];\qquad \x\mapsto f$$

으로 정의하자. 그럼 $\phi$가 isomorphism인 것은 $f'(0)$이 $A$에서 unit인 것과 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $(\x)$에 속하지 않는 $A[[\x]]$의 원소들은 정확히 $0$이 아닌 상수항을 갖는 원소들이며, 조건에서 주어진 형태의 $\phi$는 이런 원소를 보존한다. 이제 $\phi$가 isomorphism이라면, 이로부터 $\phi((\x))=(\x)$이다. 뿐만 아니라 $\phi$는 $(\x)$의 generator를 다시 $(\x)$의 generator로 보내야 하므로, 이로부터 $f+(\x^2)$이 $(\x)/(\x^2)$를 생성해야 하는 것을 알고, 이제

$$f\equiv f'(0)\x\pmod{x^2}$$

이므로, 이로부터 $f'(0)$이 $A$의 unit이어야 함을 안다. 

거꾸로 $f'(0)$이 $A$의 unit이라 하자. 그럼 우선 $\gr_{(\x)}A[[\x]]\cong \gr_{(\x)}A[\x]=A[\x]$이고, $\gr\phi: A[\x] \rightarrow A[\x]$는 정의에 의해 $x$를 $ux$로 보내주게 된다. 이제 [정리 5](#thm5)의 셋째 결과에 의해 $\phi$는 injective이며, 또 적당한 $h\in A[[\x]]$에 대해 $f=u\x+h\x^2=(u+h\x)\x$이라 쓰면 $f$가 $(\x)$를 생성하는 것을 안다. 따라서 다시 [정리 5](#thm5)의 둘째 결과에 의해 원하는 결론을 얻는다.

</details>

그럼 이번 절의 핵심적인 결과인 다음 정리를 얻는다. 

<div class="proposition" markdown="1">

<ins id="thm7">**정리 7 (Hensel)**</ins> Ring $A$가 ideal $\mathfrak{a}$에 대해 complete이라 하고, $f(\x)\in A[\x]$라 하자. 만일 

$$f(a)\equiv 0\pmod{f'(a)^2 \mathfrak{a}}$$

이라면, 적당한 $b\in A$가 존재하여

$$f(b)=0,\qquad b\equiv a\pmod{f'(a)\mathfrak{a}}$$

이 성립하도록 할 수 있다. 뿐만 아니라, 만일 $f'(a)$가 non-zerodivisor라면 이러한 $b$는 유일하게 결정된다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

편한 표기를 위해 $f'(a)=e$라 하자. 그럼 

$$f(a+e\x)=f(a)+f'(a)e\x+\cdots$$

으로부터 $f(a+e\x)=f(a)+f'(a)e\x+h(x)(e\x)^2$이도록 하는 $h를 택할 수 있다. 그럼 

$$f(a+e\x)=f(a)+e^2(\x+\x^2h(\x))$$

이며, [정리 5](#thm5)의 첫째 결과에 의하여 $\x$를 $\x+\x^2h(\x)$으로 보내는 유일한 $A$-algebra homomorphism $\phi:A[[\x]] \rightarrow A[[\x]]$이 존재한다. 한편 [따름정리 6](#cor6)에 의하여 $\phi$는 isomorphism이고, 따라서 그 inverse $\phi^{-1}$이 존재한다. 이제 위의 식에 $\phi^{-1}$을 취하면

$$f(a+e\phi^{-1}(x))=f(a)+e^2x$$

를 얻으며, 주어진 가정에 의해 $f(a)=e^2\alpha$이도록 하는 $\alpha\in \mathfrak{a}$가 존재한다. 다시 [정리 5](#thm5)의 첫째 결과를 사용하여 $\x$를 $-\alpha$로 보내는 $A$-algebra homomorphism $\psi: A[[\x]] \rightarrow A[[\x]]$를 사용하면, 위의 식으로부터

$$f(a+e\psi\phi^{-1}(x))=0$$

을 얻는다. 따라서 $b=e\psi\phi^{-1}$로 두면 원하는 결과를 얻는다. 

유일성의 경우, $e$가 zero divisor가 아니라 가정하고 $b,b'$가 주어진 조건을 만족하는 두 원소라 하자. 그럼 정의에 의해 이들은 각각 $a+er$, $a+er'$의 형태여야 한다. 이제 [정리 5](#thm5)의 첫째 결과를 적용하여 $\x$를 각각 $r$과 $r'$로 보내는 $\beta,\beta': A[[\x]] \rightarrow A[[\x]]$를 택하자. 이들을 적용하면

$$f(a)+e^2(r+r^2h(r))=f(a+er)=0=f(a+er')=f(a)+e^2(r'+(r')^2h(r'))$$

이므로 $\beta(\phi(\x))=\beta'(\phi(\x))$를 얻는다. 이제 $\phi$가 isomorphism이라는 사실과 [정리 5](#thm5)의의 유일성으로부터 원하는 결과를 얻는다. 

</details>

마지막으로 다음 정리를 언급하고 마친다.

<div class="proposition" markdown="1">

<ins id="thm8">**정리 8 (Cohen structure theorem)**</ins> Complete local noethherian ring $(A, \mathfrak{m})$과 residue field $\kappa$에 대하여, 만일 $A$가 어떠한 field를 포함한다면 $A\cong\kappa[[\x_1,\ldots, \x_n]]/\mathfrak{a}$를 만족하는 적당한 $n$과 ideal $\mathfrak{a}$가 존재한다. 

</div>

---

**참고문헌**

**[Eis]** David Eisenbud. *Commutative Algebra: with a view toward algebraic geometry*. Springer, 1995.

---