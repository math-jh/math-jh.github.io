---

title: "분해가능확대체"
excerpt: ""

categories: [Math / Field Theory]
permalink: /ko/math/field_theory/separable_extensions
header:
    overlay_image: /assets/images/Math/Field_Theory/Separable_extensions.png
    overlay_filter: 0.5
sidebar: 
    nav: "field_theory-ko"

date: 2025-05-15
last_modified_at: 2025-05-15
weight: 6

---

## 에탈대수의 성질들

이제 우리는 separable extension의 개념을 정의한다. 우선 이전 글에서 살펴본 étale algebra의 성질들을 살펴볼 것이다. 

<div class="proposition" markdown="1">

<ins id="lem1">**보조정리 1**</ins> Algebraically closed field $\mathbb{K}$에 대하여, finite degree의 commutative $\mathbb{K}$-algebra $A$가 $\Omega_{A/\mathbb{K}}=0$을 만족한다 하자. 그럼 $A$의 임의의 maximal ideal $\mathfrak{m}$에 대하여, $\mathfrak{m}=\mathfrak{m}^2$이 성립한다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

Field $A/\mathfrak{m}$는 algebraically closed field $\mathbb{K}$의 finite degree extension이므로, 이는 반드시 algebraic extension이고 따라서 $[A/\mathfrak{m}:\mathbb{K}]=1$이다. 따라서 각각의 $a\in A$에 대하여 우리는 $a-\lambda\in \mathfrak{m}$이도록 하는 $\lambda\in \mathbb{K}$를 찾을 수 있다. 그럼 다음의 식

$$A \rightarrow \mathfrak{m}/\mathfrak{m}^2;\qquad a\mapsto a-\lambda)$$

으로 정의된 함수 $D:A \rightarrow \mathfrak{m}/\mathfrak{m}^2$이 $\mathbb{K}$-derivation이 되는 것이 자명하다. 이제 [\[다중선형대수학\] §미분가군, ⁋명제 8](/ko/math/multilinear_algebra/differential_modules#prop8)의 universal property로부터 $D$는 반드시 $\Omega_{A/\mathbb{K}}$를 factor through 해야 하고, 가정에 의해 이것이 $0$이므로 $D=0$이어야 한다. 

</details>

Étale algebra에 대한 우리의 characterization을 위해서는 위의 보조정리의 결과로부터 출발하는 다음의 보조정리를 보여야 한다. 

<div class="proposition" markdown="1">

<ins id="lem2">**보조정리 2**</ins> Commutative ring $A$의 finitely generated ideal $\mathfrak{a}$가 $\mathfrak{a}=\mathfrak{a}^2$를 만족한다면 적당한 idempotent $e\in A$가 존재하여 $\mathfrak{a}=Ae$이도록 할 수 있다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $\mathfrak{a}$의 generator를 $a_1,\ldots,a_n$이라고 하자. 그럼 $
\mathfrak{a}=\mathfrak{a}^2$이므로 각각의 $i$에 대하여 다음의 식

$$a_i=\sum_{j=1}^r x_{ij}a_j$$

이 성립하도록 하는 $x_{ij}$들이 존재한다. 이렇게 만들어진 $r\times r$ 행렬에 대하여, $I_r-(x_{ij})$를 $M$이라 하자. 그럼 $M$의 adjoint matrix를 통해 다음의 식

$$NM=(\det M) I_r$$

이 성립하도록 하는 $r\times r$ 행렬 $N$이 존재한다. 이제 양 변에서 $a_j$에 해당하는 열벡터가 어디로 가는지를 계산해보면 우리는 반드시 $(\det M)a_j=0$이 모든 $j$에 대해 성립해야 하는 것을 알고, 따라서 $(\det M)\mathfrak{a}=0$이 성립한다. 

한편, 행렬 $M$은 그 정의에 의하여 $\mathfrak{a}$로 자른 후에는 $I_r$이 되며, 따라서 그 행렬식 $\det M$ 또한 (modulo $\mathfrak{a}$로) $1$이 된다. 이제 $e=1-D$로 두면 $e$가 원하는 idempotent가 된다. 

</details>

그럼 étale algebra에 대한 differential characterization은 다음과 같이 주어진다. 

<div class="proposition" markdown="1">

<ins id="thm3">**정리 3**</ins> Finite degree commutative $\mathbb{K}$-algebra $A$에 대하여, $A$가 étale인 것과 $\Omega_{A/\mathbb{K}}=0$인 것이 동치이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $\Omega_{A/\mathbb{K}}$와 étale algebra의 개념은 base change에 대해 잘 행동하므로 우리는 $\mathbb{K}$가 algebraically closure라 가정해도 된다. 더 정확히 말해, $A$가 étale인 것은 $\mathbb{K}$의 algebraic closure $\overline{\mathbb{K}}$에 대해 $\overline{\mathbb{K}}$-algebra $A_{(\overline{\mathbb{K}})}=A\otimes_\mathbb{K}\overline{\mathbb{K}}$이 diagonalizable인 것과 동치이며 ([§에탈대수, ⁋명제 8](/ko/math/field_theory/etale_algebras#prop8), 한편 [\[다중선형대수학\] §미분가군, ⁋명제 12](/ko/math/multilinear_algebra/differential_modules#prop12)의 canonical isomorphism과 $\overline{\mathbb{K}}$-algebra $A_{(\overline{\mathbb{K}})}$의 정의에 의하여 다음의 isomorphism

$$\Omega_{A_{(\overline{\mathbb{K}})}/\overline{\mathbb{K}}}\cong \Omega_{A/\mathbb{K}}\otimes_A A_{(\overline{\mathbb{K}})}=\Omega_{A/\mathbb{K}}\otimes_A A\otimes_\mathbb{K}\overline{\mathbb{K}}\cong \Omega_{A/\mathbb{K}}\otimes_\mathbb{K}\overline{\mathbb{K}}$$

을 얻고, 따라서 $\Omega_{A/\mathbb{K}}=0$인 것과 $\Omega_{A_{(\overline{\mathbb{K}})}/\overline{\mathbb{K}}}=0$인 것이 동치이다. 즉, 주어진 정리를 증명하는 것은 $\mathbb{K}$가 algebraically closed라 가정하고, $A$가 diagonalizable인 것과 $\Omega_{A/\mathbb{K}}=0$인 것이 동치임을 보이면 된다. 

우선 $A$가 diagonalizable이라 가정하면, $A$는 [§에탈대수, ⁋명제 6](/ko/math/field_theory/etale_algebras#prop6)의 둘째 조건에 의하여 idempotent들로 생성된다. 그런데 임의의 idempotent $e$에 대하여, Leibniz rule을 생각하면

$$d(e)=d(e^2)=ed(e)+ed(e)=2ed(e)$$

이고 양 변에 $e$를 곱하면 $ed(e)=0$이어야 하므로, 이를 다시 위에 대입하면 $de=0$이어야 함을 안다. 한편 명시적으로 $\Omega_{A/\mathbb{K}}$는 이러한 원소들 $de$로 생성되는 free module에 적절한 relation들로 자른 것으로 나타나므로 ([\[다중선형대수학\] §미분가군, ⁋예시 10](/ko/math/multilinear_algebra/differential_modules#ex10)) 이로부터 $\Omega_{A/\mathbb{K}}=0$이어야 함을 안다. 

이제 거꾸로 $\Omega_{A/\mathbb{K}}=0$이라 가정하고 $A$가 diagonalizable임을 보이자. $A$의 degree에 대한 귀납법으로 진행하며, degree $1$인 경우는 자명하다. 이제 일반적인 경우에 $A$의 maximal ideal $\mathfrak{m}$을 하나 택하자. 그럼 [보조정리 1](#lem1)에 의하여 $\mathfrak{m}=\mathfrak{m}^2$이고, 따라서 [보조정리 2](#lem2)를 적용하면 $\mathfrak{m}=Ae$이도록 하는 idempotent $e$를 찾을 수 있다. 한편, 이로부터 $A$를 $\mathfrak{a}=(1-e)A$와 $\mathfrak{m}$의 direct sum으로 쪼개놓으면  $\mathbb{K}$가 algebraically closed라는 가정으로부터 extension $A/\mathfrak{m}$이 degree $1$이어야 함을 안다. 즉, 이 direct sum을 

$$A\cong \mathfrak{a}\oplus\mathfrak{m}\cong \mathbb{K}\times A/\mathfrak{a}$$

으로 적을 수 있다. 이제 $\Omega$가 right exact functor이므로 ([\[다중선형대수학\] §미분가군, ⁋명제 13](/ko/math/multilinear_algebra/differential_modules#prop13)) $\Omega_{(A/\mathfrak{a})/\mathbb{K}}$는 $\Omega_{A/\mathbb{K}}=0$의 quotient가 되어 ddd$0$이다. 따라서, $A/\mathfrak{a}$는 귀납적 가정에 의하여 diagonalizable이고, 이를 $\mathbb{K}$와 곱한 $A$ 또한 마찬가지이다. 

</details>

앞서 우리는 [§제곱근확대체, ⁋예시 9](/ko/math/field_theory/radical_extensions#ex9)에서 갈루아 이론을 전개할 때 문제가 될 수 있는 상황을 살펴보았었는데, 이 예시를 바탕으로 [정리 3](#thm3)을 살펴보자. 

<div class="example" markdown="1">

<ins id="ex4">**예시 4**</ins> 좋은 경우는, [§제곱근확대체](/ko/math/field_theory/radical_extensions)의 서두에서 살펴보았듯, $\mathbb{Q}(\sqrt{2})/\mathbb{Q}$가 있다. 우리는 [\[다중선형대수학\] §미분가군, ⁋예시 10](/ko/math/multilinear_algebra/differential_modules#ex10)의 계산으로부터, $\Omega_{\mathbb{Q}[\x]/\mathbb{Q}}$는 $d\x$로 생성되는 free $\mathbb{Q}[\x]$-module임을 안다. 한편 $\mathbb{Q}[\x]$의 ideal $\mathfrak{I}=(\x^2-2)$를 생각하면 [\[다중선형대수학\] §미분가군, ⁋명제 14](/ko/math/multilinear_algebra/differential_modules#prop14)로부터 다음의 exact sequence

$$\mathfrak{I}/\mathfrak{I}^2\overset{\overline{d}}{\longrightarrow}\Omega_{\mathbb{Q}[\x]/\mathbb{Q}}\otimes_\mathbb{Q}\mathbb{Q}(\sqrt{2})\overset{\Omega_0(u)}{\longrightarrow}\Omega_{\mathbb{Q}(\sqrt{2})/\mathbb{Q}}\longrightarrow 0$$

로부터 $\Omega\_{\mathbb{Q}(\sqrt{2})/\mathbb{Q}}$는 원소 $d(\sqrt{2})$로 생성되는 $\mathbb{Q}(\sqrt{2})$-module임을 안다. 그런데 다음의 계산

$$0=d(2)=d((\sqrt{2})^2)=2\sqrt{2}d(\sqrt{2})$$

와 $2\sqrt{2}$가 $\mathbb{Q}(\sqrt{2})$에서 invertible이라는 사실로부터 $d(\sqrt{2})=0$이어야 하고 따라서 $\Omega_{\mathbb{Q}(\sqrt{2})/\mathbb{Q}}=0$이어야 함을 안다. 

반면 [§제곱근확대체, ⁋예시 9](/ko/math/field_theory/radical_extensions#ex9)에서 살펴본 $\mathbb{K}=\mathbb{F}\_p(t)$의 algebraic extension $\mathbb{K}(t^{1/p})=\mathbb{K}[\x]/(\x^p-t)$에서는 위의 계산이 틀어지게 되는데, 위의 계산과 마찬가지로 $\Omega\_{\mathbb{K}(t^{1/p})/\mathbb{K}}$는 $d(t^{1/p})$로 생성되는 $\mathbb{K}(t^{1/p})$-module이지만, 다음의 계산

$$0=d(t)=d((t^{1/p})^p)=p(t^{1/p})^{p-1}d(t^{1/p})$$

은 $d(t^{1/p})=0$이라는 결과를 주지 못한다. 어차피 $\mathbb{K}(t^{1/p})$는 characteristic $p$이므로 $p(t^{1/p})^{p-1}$은 $0$이고, 따라서 위의 식은 $d(t^{1/p})$에 대한 어떠한 relation도 주지 않기 때문이다. 실제로, 명시적으로 임의의 field $\mathbb{K}$와 algebraic extension $\mathbb{K}(\alpha)=\mathbb{K}[\x]/(f)$를 생각하면

$$\Omega_{(\mathbb{K}[\x]/(f))/\mathbb{K}}\cong\frac{\Omega_{\mathbb{K}[\x]/\mathbb{K}}\otimes_\mathbb{K}\mathbb{K}(\alpha)}{\mathfrak{I}/\mathfrak{I}^2}\cong\frac{ {\mathbb{K}[\x]\mathop{d\x}}\otimes\mathbb{K}[\x]/(f)}{(df)}\cong \frac{\mathbb{K}[\x]}{(f, f')}\mathop{d\x}$$

이므로 이로부터 위의 두 계산이 따라나온다. 

</div>

우리가 배제하고자 하는 경우는 정확히 minimal polynomial $f$가 중근을 갖는 경우, 즉 $df=0$인 경우이므로 étale algebra의 개념을 유용하게 사용할 수 있을 것이다. 곧 우리는 *separable extension*을 임의의 finite degree subextension이 étale인 field extension으로 정의할 것이다. ([정의 8](#def8)) 그럼 [예시 4](#prop4)에서 살펴봤듯 $\mathbb{Q}$의 임의의 algebraic extension은 separable extension이 된다. 더 나아가 우리는 perfect field의 임의의 algebraic extension은 separable인 것을 보일 것이다. ([명제 9](#prop9)) 이 과정에서 사용할 étale algebra의 성질들을 조금 더 살펴보자. 

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> 임의의 field $\mathbb{K}$에 대하여, finite degree, commutative $\mathbb{K}$-algebra $A$가 reduced인 것은 $\mathbb{K}$의 적당한 finite degree field extension $\mathbb{L}_1,\ldots, \mathbb{L}_n$이 존재하여 $A$가 $\mathbb{L}_1\times\cdots\times \mathbb{L}_n$과 $\mathbb{K}$-algebra로서 isomorphic한 것이 동치이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$\mathbb{L}_1\times\cdots\times \mathbb{L}_n$은 reduced이므로 한쪽 방향은 자명하다. 거꾸로 $A$가 finite degree reduced commutative $\mathbb{K}$-algebra라 하자. 만일 $A$가 field라면 더 이상 보일 것이 없으므로 $A$가 field가 아닌 경우만 증명하면 충분하고, 언제나처럼 $A$의 degree에 대한 귀납법을 사용하면 임의의 (field가 아닌) reduced algebra $A$가 항상 nontrivial한 product $A_1\times A_2$로 나타난다는 것을 보이면 된다. 

이를 위해 $A$가 $0,1$이 아닌 idempotent를 갖는다는 것을 보이자. $A$의 임의의 ideal은 유한차원 $\mathbb{K}$-벡터공간이므로 $A$의 ideal들 가운데 $\mathbb{K}$-벡터공간으로서 가장 작은 차원을 갖는 ideal $\mathfrak{a}$를 택할 수 있다. 그럼 $\mathfrak{a}$의 minimality와 $A$가 reduced라는 가정으로부터 $\mathfrak{a}^2=\mathfrak{a}$이고 따라서 [보조정리 2](#lem2)를 적용할 수 있다.

</details>

그럼, 위에서 언급한 [정리 9](#thm9)의 주장은 본질적으로 다음 보조정리에 담겨있다. 

<div class="proposition" markdown="1">

<ins id="lem6">**보조정리 6**</ins> Perfect field $\mathbb{K}$에 대하여, 임의의 finite degree, reduced $\mathbb{K}$-algebra는 étale이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

주장의 조건을 만족하는 $\mathbb{K}$-algebra $A$를 생각하자. 우선 [명제 5](#prop5)로부터 $A\cong \mathbb{L}_1\times\cdots \times\mathbb{L}_n$이도록 하는 extension들이 존재한다. 한편 étale algebra들의 곱은 étale이므로 주어진 주장은 임의의 finite degree field extension over perfect field $\mathbb{K}$가 étale임을 보이면 충분하다. 따라서 [정리 3](#thm3)을 적용하여, 임의의 $\alpha\in A$에 대하여 $d\alpha=0$임을 보이면 충분하다. [예시 4](#ex4)의 계산에 의하여 우리는 식 $f'(\alpha)d\alpha=0$이 성립해야 함을 알고, 비슷한 논리에 의하여 우리는 $f'(\alpha)\neq 0$임을 보여야 한다. 

결론에 반하여 $f'(\alpha)=0$이라 하자. 어차피 $f$가 상수인 경우에는 증명할 것이 없으므로 $f$가 일차식 이상이라 가정할 수 있고, 그럼 [§체, ⁋명제 19](/ko/math/field_theory/fields#prop19)의 결과에 의하여 $\ch(\mathbb{K})=p\neq 0$이며 $f\in \mathbb{K}[\x^p]=\mathbb{K}[\x]^p$여야 한다. 그런데 $f$는 minimal polynomial이므로 irreducible이고, irreducible polynomial은 정의에 의하여 $\mathbb{K}[\x]^p$에 속할 수 없으므로 이는 모순이다. 따라서 $f'(\alpha)\neq 0$이다. 

</details>

이제 위의 보조정리를 이용하면 다음과 같이 étale algebra의 또 다른 characterization을 만들어줄 수 있다. 

<div class="proposition" markdown="1">

<ins id="thm7">**정리 7**</ins> 임의의 finite degree commutative $\mathbb{K}$-algebra $A$에 대하여 다음이 모두 동치이다. 

1. $A$가 étale이다. 
2. 임의의 extension $\mathbb{L}/\mathbb{K}$에 대하여, $A_{(\mathbb{L})}=\mathbb{L}\otimes_\mathbb{K}A$가 reduced이다.
3. 적당한 extension $\mathbb{L}/\mathbb{K}$이 존재하여 $\mathbb{L}$이 perfect이고 $A_{(\mathbb{L})}$이 reduced이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

둘째 조건이 성립하면 셋째 조건이 성립하는 것은 perfect closure의 존재성으로부터 자명하며, 첫째 조건이 둘째 조건을 함의하는 것은 [§에탈대수, ⁋명제 8](/ko/math/field_theory/etale_algebras#prop8)의 결과이다. 따라서 셋째 조건이 첫째 조건을 함의하는 것만 보이면 충분하다. 이제 셋째 결과는 다시 [보조정리 6](#lem6)과 [§에탈대수, ⁋명제 8](/ko/math/field_theory/etale_algebras#prop8)로부터 나온다. 

</details>

## 분해가능확대체

드디어 다음의 정의를 내릴 때가 왔다. 

<div class="definition" markdown="1">

<ins id="def8">**정의 8**</ins> Algebraic extension $\mathbb{L}/\mathbb{K}$가 *separable extension<sub>분해가능확대</sub>*이라는 것은 $\mathbb{L}/\mathbb{K}$의 임의의 finite degree subextension이 étale $\mathbb{K}$-algebra인 것이다. 

</div>

우리는 이 개념을 algebraic하지 않은 field extension에 대해서도 정의할 수 있지만, 당분간은 separable algebraic extension에 대해서만 살펴본다. 

정의에 의해 그 자체로 field인 임의의 finite degree $\mathbb{K}$-algebra $\mathbb{L}$에 대해서는 étale인 것과 separable인 것이 같은 말이다. 정의로부터 만일 $\mathbb{L}/\mathbb{K}$가 separable이라면 임의의 subextension이 separable인 것과, 역으로 임의의 (finite degree) subextension들이 모두 separable이라면 $\mathbb{L}/\mathbb{K}$도 separable인 것이 둘 다 자명하다. 

앞서 약속했던 주장 또한 이제 쉽게 보일 수 있다. 

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> Field $\mathbb{K}$가 perfect인 것과 임의의 algebraic extension $\mathbb{L}/\mathbb{K}$가 separable인 것이 동치이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

임의의 algebraic extension $\mathbb{L}/\mathbb{K}$는 그 자체로 finite degree reduced $\mathbb{K}$-algebra이므로, 만일 $\mathbb{K}$가 perfect라면 한쪽 주장은 [보조정리 6](#lem6)으로부터 자명하다. 따라서 반대방향만 보이면 충분하다.

결론에 반하여 $\mathbb{K}$가 perfect가 아니라 가정하고, 따라서 characteristic $p\neq 0$을 갖는다 하자. 그럼 $\mathbb{K}$가 perfect가 아니라는 가정으로부터 (algebraic closure $\overline{\mathbb{K}}/\mathbb{K}$ 안에서의 relative) $p$-radical extension $\mathbb{K}(a)/\mathbb{K}$를 생각할 수 있다. 한편, embedding $\mathbb{K}\hookrightarrow\overline{\mathbb{K}}$로부터 얻어지는 $\mathbb{K}(a)\rightarrow\overline{\mathbb{K}}$는 [§제곱근확대체, ⁋명제 6](/ko/math/field_theory/radical_extensions#prop6)에 의하여 유일하다. 다르게 말하면, 집합 $\Hom_{\Alg{\mathbb{K}}}(\mathbb{K}(a), \overline{\mathbb{K}})$는 singleton이며 따라서 

$$1=[\mathbb{K}(a):\mathbb{K}]_s\nleq [\mathbb{K}(a):\mathbb{K}]=p^e$$

이므로 $\mathbb{K}(a)$는 étale이 아니고 따라서 separable이 아니다. 

</details>

위 명제의 증명은 $[\mathbb{K}(a):\mathbb{K}]_s$를 *separable degree*라 불렀던 것을 정당화해준다. 한편 $\mathbb{K}$가 perfect가 아니라 하더라도, 특정한 다항식 $f$은 중근을 갖지 않을 수도 있다. 다음 명제는 지금까지 우리가 관찰해온 것들을 모아둔 것에 불과하다. 

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10**</ins> 다항식 $f\in \mathbb{K}[\x]$에 대하여 다음이 모두 동치이다. 

1. $f'$가 $0$이 아니다.
2. $f$와 $f'$가 $\mathbb{K}[\x]$에서 서로소이다. 
3. $f$가 $\mathbb{L}[\x]$ 안에서 simple root를 갖도록 하는 extension $\mathbb{L}/\mathbb{K}$이 존재한다. 
4. $f$가 $\mathbb{L}[\x]$ 안에서 서로 다른 일차식들의 곱으로 쪼개지도록 하는 extension $\mathbb{L}/\mathbb{K}$이 존재한다. 
5. $f$는 $\overline{\mathbb{K}}/\mathbb{K}$ 안에서 simple root만을 갖는다. 
6. $\mathbb{K}[\x]/(f)$가 étale $\mathbb{K}$-algebra이다. 
7. $\mathbb{K}$가 characteristic $0$이거나, $\ch(\mathbb{K})=p$이고 $f\not\in\mathbb{K}[\x^p]$이다. 

</div>

이 조건을 만족하는 $f$를 *separable polynomial*이라 부른다. 그럼 [명제 9](#prop9)를 다시 한 번 적어보면, $\mathbb{K}$가 perfect인 것과 $\mathbb{K}[\x]$의 모든 irreducible polynomial이 separable인 것이 동치임을 안다. 이를 $f$를 통해 추가되는 원소에 초점을 맞추면 다음과 같이 정의할 수 있다. 

<div class="definition" markdown="1">

<ins id="def11">**정의 11**</ins> Field extension $\mathbb{L}/\mathbb{K}$에 대하여, algebraic element $x\in \mathbb{L}$이 *separable element*라는 것은 $\mathbb{K}(x)/\mathbb{K}$이 separable extension인 것이다. 

</div>

정의에 의해, $x$의 minimal polynomial을 $f$라 한다면, $f$가 separable이어야 하고 이 때 $x$는 $f$의 simple root가 된다. 이들 개념은 (당연히) 모두 같은 것을 의미한다. 즉, extension $\mathbb{L}/\mathbb{K}$와 원소 $x\in\mathbb{L}$, 그리고 $x$의 minimal polynomial $f$에 대하여 다음이 모두 동치이다.

1. $x$가 separable이다.
2. $f$가 separable이다.
3. $x$가 $f$의 simple root이다.

뿐만 아니라, 모든 원소가 algebraic한 extension이 algebraic extension이듯이 다음이 성립한다. 

<div class="proposition" markdown="1">

<ins id="prop12">**명제 12**</ins> Algebraic extension $\mathbb{L}/\mathbb{K}$에 대하여 다음이 성립한다. 

1. 만일 $\mathbb{L}/\mathbb{K}$가 separable이라면 $\mathbb{L}$의 모든 원소는 separable이다. 
2. 거꾸로 만일 $A$가 $\mathbb{L}$의 separable element들로 이루어진 집합이고, $\mathbb{L}=\mathbb{K}(A)$라 하면 $\mathbb{L}$은 separable extension이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

첫째 결과는 자명하므로 둘째 결과만 보이면 충분하다. 즉, $\mathbb{L}$의 임의의 finite degree subextension $\mathbb{M}$을 잡은 후 이것이 étale임을 보여야 한다. 우선 $\mathbb{L}=\mathbb{K}(A)$이고 $\mathbb{M}$이 $\mathbb{L}$의 finite degree subextension이므로, $A$의 원소 중 유한개의 $x_1,ldots, x_m$을 택하여

$$\mathbb{M}\subset \mathbb{K}(x_1,\ldots, x_m)=\mathbb{K}[x_1,ldots, x_m]$$

이도록 할 수 있다. 이 때 각각의 $\mathbb{K}[x_i]$들이 separable extension인 것은 $A$의 가정으로부터 자명하므로 이들은 étale이고, 그럼 $\mathbb{K}[x_1,\ldots, x_m]$은 이들의 tensor product $\mathbb{K}[x_1]\otimes\cdots\otimes \mathbb{K}[x_n]$을 이들의 associativity와 commutativity를 나타내는 relation으로 잘라서 얻어지고 $\mathbb{M}$이 이것의 subalgebra이므로 [§에탈대수, ⁋따름정리 14](/ko/math/field_theory/etale_algebras#cor14)에 의하여 $\mathbb{M}$이 étale이다.

</details>

뿐만 아니라, finite degree separable extension은 단 하나의 원소로 생성될 수 있다. 즉, 만일 $\mathbb{L}/\mathbb{K}$가 finite degree separable extension이라면, 적절한 $x\in \mathbb{L}$을 택하여 $\mathbb{L}=\mathbb{K}[x]$이도록 할 수 있다. 이러한 원소를 *primitive element*라 부른다. 

[정리 14](#thm14)는 finite degree separable extension에 대해서는 항상 primitive element를 찾을 수 있다는 것을 보여준다. 이를 위해서는 다음 보조정리가 필요하다.

<div class="proposition" markdown="1">

<ins id="lem13">**보조정리 13**</ins> Infinite field $\mathbb{K}$에 대하여, commutative $\mathbb{K}$-algebra $A$를 고정하자. 만일 $A$가 오직 유한히 많은 subalgebra만을 가지고, $V$가 $A$를 생성하는 부분 벡터공간이라 하면 적당한 $x\in V$가 존재하여 $A=\mathbb{K}[x]$이도록 할 수 있다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$A$의 subalgebra들이 $A_1,\ldots, A_n$ 뿐이라 가정하자. 그럼 우선 $V$는 $A$를 생성하므로 $A_i$들을 생성할 수는 없다. 즉 $V\not\subset A_i$이다. 만일 우리가 이로부터 $V\not\subset A_1\cup\cdots\cup A_n$임을 보인다면, $x\in V\setminus A_1\cup\cdots \cup A_n$에 대하여 $A$의 subalgebra $\mathbb{K}[x]$는 어떠한 $A_i$와도 같을 수 없고, 따라서 반드시 $A=\mathbb{K}[x]$여야 하므로 원하는 것을 증명할 수 있을 것이다. 

결론에 반하여 $V\subset A_1\cup\cdots\cup A_n$이라 가정하자. 주어진 가정으로부터 $V\not\subset A_n$이므로 적당한 $x\in V\setminus A_n$이 존재한다. 그럼 임의의 $y\in V$에 대하여, 무한집합

$$\{x\}\cup \{y+\lambda x\mid \lambda\in\mathbb{K}\}$$

을 생각할 수 있다. 이 집합은 $V$의 부분집합이며 따라서 $A_1\cup\cdots\cup A_n$의 부분집합이다. 따라서, 비둘기집 원리에 의해 이들 중 적어도 두 개는 같은 $A_i$에 속해야 하며, 그럼 이 사실로부터 $x,y$를 동시에 포함하는 어떠한 $A_i$가 존재함을 안다. 가정에 의하여 $x\not\in A_n$이므로 $i$는 $n$이 될 수는 없고, 따라서 $y$는 ($x$와 마찬가지로) $A_1,\ldots, A_{n-1}$ 중 어느 하나에 속해야 한다. 이로부터 $y$가 $A_1\cup\cdots \cup A_{n-1}$에 속해야 한다는 것을 알고, $y$는 $V$의 임의의 원소이므로 $V\subset A_1\cup\cdots\cup A_{n-1}$이다. 

이제 이 과정을 귀납적으로 반복해나가면 $V\subset A_1$이 되어 모순이므로 $V\not\subset A_1\cup\cdots\cup A_n$여야 한다. 

</details>

<div class="proposition" markdown="1">

<ins id="thm14">**정리 14**</ins> Infinite field $\mathbb{K}$를 고정하자. Algebraic extension $\mathbb{L}/\mathbb{K}$에 대하여 다음이 동치이다.

1. $\mathbb{L}$이 primitive element를 갖는다. 
2. $\mathbb{L}$은 오직 유한히 많은 subextension만을 갖는다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $\mathbb{L}$이 primitive element $x$를 갖는다 하고, $f(\x)\in \mathbb{K}[\x]$가 $x$의 minimal polynomial이라 하자. 다항식 $f(\x)$를 $\mathbb{L}[\x]$에서 나누는 monic polynomial $g(\x)\in \mathbb{L}[\x]$를 생각하면, 우리는 이러한 다항식 $g$가 주어질 때마다 $g$의 계수들로 생성되는 $\mathbb{L}$의 subextension을 생각할 수 있다. 이를 $\mathbb{K}_g$로 적자. 그럼 우리 주장은 이들 $\mathbb{K}_g$들이 정확히 $\mathbb{L}$의 subextension이라는 것이다. 특히 이러한 extension들은 $f$를 $d$차식이라 할 때, 많아야 $2^d$개이므로 둘째 조건이 성립할 것이다. 

주장을 보이기 위해 임의의 subextension $\mathbb{M}$을 택하자. 그럼 $x$가 primitive element이므로 $\mathbb{M}[x]=\mathbb{L}$이 성립한다. 즉, $x$는 extension $\mathbb{L}/\mathbb{M}$의 algebraic element이므로, minimal polynomial $h(\x)\in\mathbb{M}[\x]$를 택할 수 있으며 이는 [§대수적 확장, ⁋정리 15](/ko/math/field_theory/algebraic_extensions#prop15)에 의하여 $\mathbb{L}[\x]$에서 $f$를 나누는 monic polynomial이다. 따라서 $\mathbb{K}_h$가 위와 같이 정의되며, 그 정의에 의하여 $\mathbb{K}_h\subset\mathbb{M}$이다. 한편 $x$가 $\mathbb{L}/\mathbb{K}$의 primitive element이므로, 우리는 다음의 등식

$$\mathbb{K}_h[x]=\mathbb{M}[x]=\mathbb{L}$$

을 갖는다. 그런데 정의에 의하여 $[\mathbb{L}:\mathbb{M}]=\deg h$이며, $h(\x)\in \mathbb{K}_h[\x]$가 $h(x)=0$을 만족하므로 $[\mathbb{L}:\mathbb{K}_h]\leq\deg h$이다. 이로부터 반드시 $\mathbb{K}_h=\mathbb{M}$이어야 함을 안다. 

이제 둘째 조건을 가정하면, $\mathbb{L}/\mathbb{K}$는 오직 유한히 많은 subextension들만 가지므로, $A=\mathbb{L}$로 두면 [보조정리 13](#lem13)의 가정을 만족하고 따라서 원하는 결과를 얻는다. 

</details>

특히 만일 $\mathbb{L}/\mathbb{K}$가 finite degree separable extension이라면 이는 특히 finite degree étale $\mathbb{K}$-algebra이고, 따라서 [§에탈대수, ⁋명제 9](/ko/math/field_theory/etale_algebras#prop9)로부터 위 정리의 둘째 조건이 성립한다는 것을 안다. 

[정리 14](#thm14)는 $\mathbb{K}$가 finite field여도 항상 성립하지만, 이를 증명하기 위해서는 [보조정리 13](#lem13)보다 조금 더 정교한 counting argument가 필요하므로 나중으로 미뤄둔다. ([##ref##]())

한편 seperability는 본질적으로는 (거의) étale algebra이고, étale algebra는 base change에 대해 잘 행동하므로 ([§에탈대수, ⁋따름정리 14](/ko/math/field_theory/etale_algebras#cor14)) [명제 12](#prop12)의 증명에서와 마찬가지로 약간의 수정을 가하면 다음의 두 경우에 separability도 base change에 대해 잘 행동한다는 것을 보일 수 있다. 

<div class="proposition" markdown="1">

<ins id="prop15">**명제 15**</ins> Algebraic extension $\mathbb{M}/\mathbb{L}/\mathbb{K}$에 대하여, $\mathbb{M}/\mathbb{K}$가 separable인 것과 $\mathbb{M}/\mathbb{L}$, $\mathbb{L}/\mathbb{K}$가 모두 separable인 것이 동치이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

만일 $\mathbb{M}/\mathbb{K}$가 separable이라면 그 subextension $\mathbb{L}/\mathbb{K}$가 separable인 것은 정의로부터 자명하고, 이 때 $\mathbb{M}$의 임의의 원소는 $\mathbb{K}$에 대해 separable이므로 ([명제 12](#prop12)), 이를 extension $\mathbb{M}/\mathbb{L}$로 보았을 때 $\mathbb{L}$에 대해서도 separable이다. ([명제 10](#prop10)) 즉, $\mathbb{M}$의 임의의 원소가 separable이므로 다시 [명제 12](#prop12)에 의해 $\mathbb{M}/\mathbb{L}$이 separable임을 안다. 

따라서 이 명제의 핵심은 반대방향이다. 우선, 만일 $\mathbb{M}/\mathbb{K}$가 finite degree였다면 separable algebra와 étale algebra가 같은 말이므로, 주장은 [§에탈대수, ⁋명제 12](/ko/math/field_theory/etale_algebras#prop12)의 셋째 결과로부터 자명하다. 증명의 아이디어는 위와 비슷하게, $\mathbb{M}/\mathbb{K}$는 무한한 degree를 갖더라도 특정 원소 하나만 보면 이를 finite degree로 치환할 수 있다는 것이다.

임의의 $x\in \mathbb{M}$이 주어졌다 하고, minimal polynomial $f\in\mathbb{L}[\x]$이 주어졌다 하면, $f$는 separable polynomial이다. 이제 $\mathbb{L}/\mathbb{K}$의 subextension $\mathbb{L}'$을, $f$에 등장하는 계수들을 $\mathbb{K}$에 넣어주어 생기는 subextension으로 정의하자. 그럼 $\mathbb{L}'$는 algebraic element들 유한개로 생성되므로 $\mathbb{L}'/\mathbb{K}$가 finite degree extension이다. 이제 $f$는 $\mathbb{L}$과 $\mathbb{L}'$ 모두에서 $x$의 minimal polynomial이고 $\mathbb{L}$에서 separable이므로 $\mathbb{L}'$에서도 separable이다. 즉 $x$는 extension $\mathbb{M}/\mathbb{L}'$의 separable element이며, $\mathbb{M}'=\mathbb{L}'(x)$라 하면 $\mathbb{M}'/\mathbb{L}'$는 finite degree separable extension, 즉 finite degree étale algebra다. 한편 $\mathbb{L}/\mathbb{K}$가 separable이므로 그 subextension $\mathbb{L}'$도 separable이고, 따라서 $\mathbb{L}'/\mathbb{K}$도 finite degree étale algebra다. 따라서 이들의 tower $\mathbb{M}'/\mathbb{K}$도 finite degree étale algebra이고, 따라서 finite degree separable extension이다. 즉 $x$가 $\mathbb{K4}$에 대한 separable element이며, $x$의 선택은 임의로 주어진 것이므로 원하는 결과를 얻는다. 

</details>

<div class="proposition" markdown="1">

<ins id="prop16">**명제 16**</ins> $\mathbb{K}$의 적당한 extension을 하나 고정하고, 이 extension의 subextension $\mathbb{K'}/\mathbb{K}$, 그리고 algebraic subextension $\mathbb{L}/\mathbb{K}$가 주어졌다 하자. 그럼 $\mathbb{L}'=\mathbb{K}'(\mathbb{L})$에 대하여 다음이 성립한다. 

1. 만일 $\mathbb{L}/\mathbb{K}$가 separable이라면 $\mathbb{L}'/\mathbb{K}'$도 그러하다.
2. 거꾸로 만일 $\mathbb{L}'/\mathbb{K}'$가 separable이고 $\mathbb{L}/\mathbb{K}, \mathbb{K}'/\mathbb{K}$가 linearly disjoint라면 $\mathbb{L}/\mathbb{K}$도 separable이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

1, 가정에 의해 $\mathbb{L}$의 임의의 원소가 $\mathbb{K}$에 대해 separable이므로, $\mathbb{K}'(\mathbb{L})$의 모든 원소가 $\mathbb{K}'$에 대해 separable이다.
2. 이를 보이기 위해서는 임의의 finite degree subextension $\mathbb{M}/\mathbb{K}$가 étale임을 보여야 한다. 우선 주어진 가정으로부터 $\mathbb{M}$과 $\mathbb{K}'$는 linearly disjoint이고, 따라서 $\mathbb{M}_{(\mathbb{K}')}=\mathbb{M}\otimes_\mathbb{K}\mathbb{K}'$가 $\mathbb{K}'(\mathbb{M})$과 isomorphic하다. ([§대수적 확장, ⁋명제 10](/ko/math/field_theory/algebraic_extensions#prop10)) 한편 $\mathbb{K}'(\mathbb{M})/\mathbb{K}'$는 finite degree이므로, $\mathbb{L}'/\mathbb{K}'$가 separable이라는 가정으로부터 étale이다. 이제 étale morphism은 base change에 대해 stable하므로 원하는 결과를 얻는다. ([§에탈대수, ⁋따름정리 14](/ko/math/field_theory/etale_algebras#cor14))

</details>
